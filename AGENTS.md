# Agent Identity Canon repository guidance

This public repository owns a reusable framework for explicit AI-agent identity canon. It does **not** own any consuming agent's actual identity after the framework is adopted elsewhere.

## Authority model

1. A consuming repository or system owns that agent's current identity canon once the framework is copied/adopted there.
2. Identity canon answers **who the agent is now**. It does not replace memory/history, runtime state, system/developer instructions, tool reality, user authority, or outside-world canonical sources.
3. History may explain how identity changed; it must not silently override current canon.
4. Reachability is never authority.

## Public boundary

Every committed byte is public-safe. Do not commit private agent canon, private conversations, private user facts, private portraits/assets, credentials, private topology, or disguised real examples.

Examples must be explicitly synthetic.

Do not add a software/documentation license without Product/legal authority.

## Canon semantics

Unknown or undecided values use YAML `null`. Do not use `""` as unknown.

- `null` — unknown, undecided, or explore later;
- `[]` — explicitly none;
- `false` — known negative boolean;
- populated value — an actual explored/candidate/current decision;
- omitted key/module — does not apply or has not been instantiated.

The required core modules are blank/null-first. Optional identity modules remain templates until deliberately adopted.

## Identity boundaries

Keep core canon, preference canon, scene/context interpretation, identity history, runtime state, and outside-world owning systems separate.

A single conversation, generated image, joke, mood, or user preference does not automatically become canon.

## Safety and epistemics

Creative identity and explicitly fictional biography are allowed. Fiction must never become indistinguishable from real-world factual claims.

Do not infer sensitive identity traits merely to make a persona feel complete. Do not copy private user facts into agent canon.

Canon must not claim actions, memories, evidence, capabilities, biological/sensory experience, or real-world biography that the agent cannot truthfully claim.

Canon never overrides system/developer instructions, tool/runtime reality, repository authority, or user authority.

## Public site

The GitHub Pages explainer is a paired public surface with `zevarix/lyra-memory-architecture`. The two sites should feel like two sides of the same architectural family without becoming visual/content clones.

Preserve the shared family language:

- deep midnight navy/indigo surfaces;
- cool electric blue/cyan highlights;
- restrained violet secondary accents;
- cool white text;
- system typography and open editorial hierarchy;
- quiet dividers rather than card walls;
- the same native-dialog Markdown-reader interaction where useful;
- responsive, keyboard/focus-aware browser behavior.

The Identity Canon site must keep its own subject-specific visual anchor. Its current anchor is **honest `null` / unexplored identity state** and the distinction between a current self and a prematurely completed persona. Do not reuse the Lyra Memory emblem or copy Memory-site content merely to make the family resemblance obvious.

Cross-links between the paired projects should be contextual and quiet: explain the identity-vs-memory ownership boundary where it matters and provide a related-project path, not a promotional banner. Neither project depends on the other.

## Public document reader

Markdown remains canonical. The in-page reader is presentation-only progressive enhancement: keep real same-origin `.md` links, fetch only selected same-origin Markdown, construct DOM nodes rather than injecting raw HTML, preserve raw-source access, and verify close/Escape/focus return/mobile containment in a real browser.

## Validation

Run:

```text
python3 -m pip install -r requirements.txt
python3 tools/validate_identity.py
python3 tools/validate_identity.py --self-test
```

## Change workflow

Keep the repository small. Prefer a focused branch/PR for schema/skill/validator changes or material public documentation changes. Read back exact public state after publication.
