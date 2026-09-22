#!/usr/bin/env python3
"""Deterministic structural validator for Agent Identity Canon."""

from __future__ import annotations

import argparse
import re
import tempfile
from pathlib import Path
from typing import Any

import yaml

MODULE_SCHEMA = "agent-identity-canon/module/v1"
HISTORY_SCHEMA = "agent-identity-canon/history-event/v1"
EXAMPLE_SCHEMA = "agent-identity-canon/example/v1"

CURRENT_STATES = {"unexplored", "exploratory", "candidate", "current"}
HISTORY_OUTCOMES = {"refined", "superseded", "retired"}
PROVENANCE = {"independent", "shared", "influenced", "collaborative", "exploratory"}
CONFIDENCE = {"low", "medium", "high"}
CORE_MODULES = {"identity", "values", "personality", "communication", "boundaries", "evolution"}
OPTIONAL_MODULES = {"preferences", "aesthetics", "visual-identity", "fictional-biography"}

PRIVATE_PATTERNS = [
    re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+", re.I),
    re.compile(r"/home/[^/\s]+/"),
]
SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    re.compile(r"\bsb_secret_[A-Za-z0-9_-]{12,}\b"),
    re.compile(r"\bservice_role\b", re.I),
]

class UniqueKeyLoader(yaml.SafeLoader):
    pass

def construct_mapping(loader: UniqueKeyLoader, node: yaml.nodes.MappingNode, deep: bool = False) -> dict[str, Any]:
    mapping: dict[str, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                f"duplicate key: {key!r}",
                key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping

UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping)

def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.load(handle, Loader=UniqueKeyLoader)

def relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()

def find_empty_strings(value: Any, trail: str = "") -> list[str]:
    found: list[str] = []
    if value == "":
        found.append(trail or "<root>")
    elif isinstance(value, dict):
        for key, item in value.items():
            child = f"{trail}.{key}" if trail else str(key)
            found.extend(find_empty_strings(item, child))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            found.extend(find_empty_strings(item, f"{trail}[{index}]"))
    return found

def validate_record(record: Any, label: str, errors: list[str]) -> None:
    if not isinstance(record, dict):
        errors.append(f"{label}: entry must be a mapping")
        return
    required = {"value", "status", "provenance", "confidence"}
    missing = required - set(record)
    if missing:
        errors.append(f"{label}: missing keys {sorted(missing)}")
        return
    status = record.get("status")
    value = record.get("value")
    provenance = record.get("provenance")
    confidence = record.get("confidence")
    if status not in CURRENT_STATES:
        errors.append(f"{label}: unrecognized active status {status!r}")
    if provenance is not None and provenance not in PROVENANCE:
        errors.append(f"{label}: unrecognized provenance {provenance!r}")
    if confidence is not None and confidence not in CONFIDENCE:
        errors.append(f"{label}: unrecognized confidence {confidence!r}")
    if status == "unexplored" and (value is not None or provenance is not None or confidence is not None):
        errors.append(f"{label}: unexplored requires value/provenance/confidence = null")
    if status in {"candidate", "current"}:
        if value is None:
            errors.append(f"{label}: {status} requires a non-null value")
        if provenance is None:
            errors.append(f"{label}: {status} requires provenance")
        if confidence is None:
            errors.append(f"{label}: {status} requires confidence")
    if status == "exploratory" and value is not None and provenance is None:
        errors.append(f"{label}: populated exploratory value requires provenance")

def validate_references(data: dict[str, Any], path: Path, root: Path, errors: list[str]) -> None:
    refs = data.get("references")
    if refs is None:
        return
    if not isinstance(refs, list):
        errors.append(f"{relative(path, root)}: references must be null or a list")
        return
    for item in refs:
        if not isinstance(item, str) or not item:
            errors.append(f"{relative(path, root)}: reference must be a non-empty string")
            continue
        ref = Path(item)
        if ref.is_absolute() or ".." in ref.parts:
            errors.append(f"{relative(path, root)}: unsafe reference {item!r}")
        elif not (root / ref).exists():
            errors.append(f"{relative(path, root)}: missing reference {item!r}")

def validate_module(path: Path, root: Path, errors: list[str]) -> None:
    try:
        data = load_yaml(path)
    except Exception as exc:
        errors.append(f"{relative(path, root)}: YAML error: {exc}")
        return
    if not isinstance(data, dict):
        errors.append(f"{relative(path, root)}: module must be a mapping")
        return
    for trail in find_empty_strings(data):
        errors.append(f"{relative(path, root)}: empty string at {trail}; use null if undecided")
    if data.get("schema") != MODULE_SCHEMA:
        errors.append(f"{relative(path, root)}: invalid module schema")
    module = data.get("module")
    if module not in CORE_MODULES | OPTIONAL_MODULES:
        errors.append(f"{relative(path, root)}: unrecognized module {module!r}")
    if module == "fictional-biography" and data.get("fictional") is not True:
        errors.append(f"{relative(path, root)}: fictional-biography must declare fictional: true")
    if module == "visual-identity" and data.get("creative_representation") is not True:
        errors.append(f"{relative(path, root)}: visual-identity must declare creative_representation: true")
    entries = data.get("entries")
    if not isinstance(entries, dict) or not entries:
        errors.append(f"{relative(path, root)}: entries must be a non-empty mapping")
        return
    for key, record in entries.items():
        validate_record(record, f"{relative(path, root)}:{key}", errors)
        if data.get("template") is True and isinstance(record, dict) and record.get("status") != "unexplored":
            errors.append(f"{relative(path, root)}:{key}: template entries must remain unexplored")
    validate_references(data, path, root, errors)

def validate_history(path: Path, root: Path, errors: list[str], template: bool = False) -> None:
    try:
        data = load_yaml(path)
    except Exception as exc:
        errors.append(f"{relative(path, root)}: YAML error: {exc}")
        return
    if not isinstance(data, dict):
        errors.append(f"{relative(path, root)}: history event must be a mapping")
        return
    for trail in find_empty_strings(data):
        errors.append(f"{relative(path, root)}: empty string at {trail}; use null if unknown")
    if data.get("schema") != HISTORY_SCHEMA:
        errors.append(f"{relative(path, root)}: invalid history schema")
    if template:
        return
    for key in ("event_id", "recorded_at", "module", "field", "outcome", "reason"):
        if data.get(key) is None:
            errors.append(f"{relative(path, root)}: history event requires {key}")
    if data.get("outcome") not in HISTORY_OUTCOMES:
        errors.append(f"{relative(path, root)}: outcome must be refined/superseded/retired")
    for side in ("previous", "current"):
        record = data.get(side)
        if not isinstance(record, dict):
            errors.append(f"{relative(path, root)}:{side}: must be a mapping")
            continue
        status = record.get("status")
        if status not in CURRENT_STATES:
            errors.append(f"{relative(path, root)}:{side}: invalid status {status!r}")
        provenance = record.get("provenance")
        confidence = record.get("confidence")
        if provenance is not None and provenance not in PROVENANCE:
            errors.append(f"{relative(path, root)}:{side}: invalid provenance {provenance!r}")
        if confidence is not None and confidence not in CONFIDENCE:
            errors.append(f"{relative(path, root)}:{side}: invalid confidence {confidence!r}")
    validate_references(data, path, root, errors)

def validate_examples(root: Path, errors: list[str]) -> None:
    example_dirs = [p for p in (root / "examples").glob("*") if p.is_dir()]
    if not example_dirs:
        errors.append("examples/: at least one synthetic example is required")
    for directory in sorted(example_dirs):
        manifest = directory / "manifest.yaml"
        if not manifest.exists():
            errors.append(f"{relative(directory, root)}: missing manifest.yaml")
            continue
        try:
            data = load_yaml(manifest)
        except Exception as exc:
            errors.append(f"{relative(manifest, root)}: YAML error: {exc}")
            continue
        if not isinstance(data, dict) or data.get("schema") != EXAMPLE_SCHEMA:
            errors.append(f"{relative(manifest, root)}: invalid example schema")
        if not isinstance(data, dict) or data.get("synthetic") is not True:
            errors.append(f"{relative(manifest, root)}: example must declare synthetic: true")

def scan_public_safety(root: Path, errors: list[str]) -> None:
    allowed_suffixes = {".md", ".yaml", ".yml", ".py", ".txt"}
    validator_source = Path(__file__).resolve()
    for path in root.rglob("*"):
        if not path.is_file() or ".git" in path.parts or "__pycache__" in path.parts:
            continue
        if path.resolve() == validator_source:
            continue
        if path.suffix.lower() not in allowed_suffixes and path.name != "requirements.txt":
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern in PRIVATE_PATTERNS:
            if pattern.search(text):
                errors.append(f"{relative(path, root)}: private-boundary pattern matched {pattern.pattern!r}")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                errors.append(f"{relative(path, root)}: secret-like pattern matched {pattern.pattern!r}")

def validate_repository(root: Path) -> list[str]:
    errors: list[str] = []
    expected = {f"{name}.yaml" for name in CORE_MODULES}
    actual = {p.name for p in (root / "canon").glob("*.yaml")}
    if expected - actual:
        errors.append(f"canon/: missing core modules {sorted(expected - actual)}")
    for path in sorted((root / "canon").glob("*.yaml")):
        validate_module(path, root, errors)
    for path in sorted((root / "templates" / "optional").glob("*.yaml")):
        validate_module(path, root, errors)
    history_template = root / "templates" / "history-entry.yaml"
    if history_template.exists():
        validate_history(history_template, root, errors, template=True)
    else:
        errors.append("templates/history-entry.yaml: missing")
    for path in sorted((root / "examples").glob("*/canon/*.yaml")):
        validate_module(path, root, errors)
    for path in sorted((root / "examples").glob("*/optional/*.yaml")):
        validate_module(path, root, errors)
    for path in sorted((root / "examples").glob("*/history/*.yaml")):
        validate_history(path, root, errors)
    validate_examples(root, errors)
    scan_public_safety(root, errors)
    return errors

def self_test() -> list[str]:
    failures: list[str] = []
    errors: list[str] = []
    validate_record({"value": None, "status": "current", "provenance": "independent", "confidence": "high"}, "self.current-null", errors)
    if not any("non-null" in item for item in errors):
        failures.append("self-test: null current value was not rejected")
    errors = []
    validate_record({"value": "x", "status": "candidate", "provenance": "invented", "confidence": "high"}, "self.bad-provenance", errors)
    if not any("unrecognized provenance" in item for item in errors):
        failures.append("self-test: invalid provenance was not rejected")
    with tempfile.TemporaryDirectory(prefix="identity-canon-selftest-") as directory:
        duplicate = Path(directory) / "duplicate.yaml"
        duplicate.write_text("a: 1\na: 2\n", encoding="utf-8")
        try:
            load_yaml(duplicate)
            failures.append("self-test: duplicate YAML key was not rejected")
        except yaml.constructor.ConstructorError:
            pass

        fictional = Path(directory) / "fictional.yaml"
        fictional.write_text(
            "schema: agent-identity-canon/module/v1\n"
            "version: 0.1.0\n"
            "module: fictional-biography\n"
            "optional: true\n"
            "entries:\n"
            "  setting:\n"
            "    value: null\n"
            "    status: unexplored\n"
            "    provenance: null\n"
            "    confidence: null\n"
            "    revisit_when: null\n",
            encoding="utf-8",
        )
        errors = []
        validate_module(fictional, Path(directory), errors)
        if not any("fictional: true" in item for item in errors):
            failures.append("self-test: unlabeled fictional biography was not rejected")
    return failures

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    errors = validate_repository(root)
    if args.self_test:
        errors.extend(self_test())
    if errors:
        print("Agent Identity Canon validation: FAIL")
        for item in errors:
            print(f"- {item}")
        return 1
    print("Agent Identity Canon validation: PASS")
    print("Validated null-first semantics, lifecycle/provenance, history, synthetic examples, references, and public-safety patterns.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
