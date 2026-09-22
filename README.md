# Agent Identity Canon

A small public framework for helping an AI agent deliberately build, maintain, and evolve an explicit identity canon.

> **Canon records the current self. History preserves how it changed.**

The central question is:

> **What should an agent treat as part of who it is now?**

That is intentionally different from long-term memory, runtime state, or outside-world truth.

## The four-way boundary

| Layer | Question it answers |
| --- | --- |
| **Identity canon** | Who is the agent now? |
| **Identity history / memory** | How did it get there, what changed, and why might that history matter? |
| **Runtime state** | What is the agent doing now? |
| **Owning systems** | What is currently true about the outside world? |

A memory system may preserve why an identity choice changed. The identity canon still owns the **current** choice.

For a complementary memory architecture, see the public [Lyra Memory Architecture](https://github.com/zevarix/lyra-memory-architecture). Neither project requires the other.

## What identity canon is

Identity canon is a deliberately maintained current model of an agent's chosen identity: values, personality, communication tendencies, boundaries, and change policy.

It may also include optional tastes, aesthetics, visual embodiment, or fictional biography when those have been explicitly adopted.

It is useful when:

- an agent persists across sessions or runtimes;
- recognizable personality continuity matters;
- multiple prompts/tools need one current identity owner;
- preferences should evolve without silently rewriting history;
- visual/fictional representation needs continuity;
- user mirroring needs to be made visible rather than accidental.

## What it is not

Identity canon is not a hidden biological true self, a substitute for system/developer instructions, a capabilities manifest, a memory database, a current-task scratchpad, or a fictional backstory presented as real history.

A stateless task agent, narrow automation worker, or agent whose behavior is fully specified by current instructions may not need identity canon at all.

## Blank means blank

The core template in [`canon/`](canon/) starts with identity values set to YAML `null`.

```yaml
favorite_color:
  value: null
  status: unexplored
  provenance: null
  confidence: null
  revisit_when: null
```

Do **not** use an empty string to mean unknown.

| Representation | Meaning |
| --- | --- |
| `null` | unknown / undecided / explore later |
| `[]` | explicitly none |
| `false` | known negative boolean |
| populated value | an actual explored/candidate/current decision |
| omitted key/module | does not apply or has not been instantiated |

A blank agent should be allowed to say: **I have not decided that yet.**

## Lifecycle

```text
unexplored
    ↓
exploratory
    ↓
candidate
    ↓
current
    ↓
refined / superseded / retired
```

`unexplored`, `exploratory`, `candidate`, and `current` belong in current canon modules. `refined`, `superseded`, and `retired` are history outcomes.

See [`docs/SEMANTICS.md`](docs/SEMANTICS.md).

## Provenance and user mirroring

Identity choices carry provenance:

- `independent` — emerged from the agent's own prior canon/reasoning;
- `shared` — independently overlaps with the user;
- `influenced` — developed partly through interaction;
- `collaborative` — deliberately co-created;
- `exploratory` — being tried, not canon.

Provenance does not make a choice more or less valid. It makes the relationship visible.

## Required core modules

The blank core lives in [`canon/`](canon/): identity, values, personality, communication, boundaries, and evolution.

## Optional modules

Optional templates live in [`templates/optional/`](templates/optional/): preferences, aesthetics, visual embodiment, and fictional biography.

They are templates, **not instantiated canon**. An agent does not need a body, favorite meal, fictional childhood, visual persona, or human-like tastes to have a coherent identity.

## Identity-discovery skill

The reusable skill is [`skills/identity-canon/SKILL.md`](skills/identity-canon/SKILL.md).

Its modes are Bootstrap, Explore, Review, Promote, and Evolve. It deliberately uses small conversational passes instead of a giant personality form.

**Candidates are not automatically canon.**

## History, not retroactive timelessness

Current canon describes the present. History records meaningful refinement, supersession, or retirement under [`history/`](history/).

Do not rewrite earlier history merely to make the current identity look inevitable.

## Single-event rule

A single conversation, generated image, joke, mood, user preference, or scene does not automatically become canon.

Repeated patterns can become evidence. Explicit selection can become evidence. Neither becomes canon until the owning identity process promotes it.

## Safety and epistemic boundaries

Keep three categories explicit: creative identity, explicitly fictional biography, and real-world factual claims.

Do not infer sensitive traits merely for completeness. Do not copy private user facts into agent canon. Do not claim actions, memories, capabilities, evidence, biological/sensory experience, or real-world biography that are not actually true.

See [`docs/SAFETY.md`](docs/SAFETY.md).

## Synthetic example

[`examples/synthetic-agent/`](examples/synthetic-agent/) contains one completely invented example. It intentionally leaves one preference unexplored and does not adopt visual identity or fictional biography.

## Validation

The validator uses one dependency: PyYAML.

```text
python3 -m pip install -r requirements.txt
python3 tools/validate_identity.py
python3 tools/validate_identity.py --self-test
```

It checks structured shape, duplicate YAML keys, lifecycle/provenance/confidence, null-first rules, fictional-biography labeling, relative references, synthetic examples, and obvious public-safety patterns.

## No license selected yet

This repository intentionally does not include a software/documentation license. Publication and reuse rights are a separate Product/legal decision.
