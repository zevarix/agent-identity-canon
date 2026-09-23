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

Optional modules are adopted identity dimensions, not a completion checklist. A reflective module belongs here only when the pattern recurs, is stable enough to outlive one task/conversation, and is not better owned by memory, runtime state, a project tracker, or another system. `aspirations-growth` must not become a task backlog; `relational-style` must not become a private relationship log; `interests-curiosities` must not become the current research queue; `learning-thinking` must describe observable preferences rather than intelligence claims or hidden chain-of-thought. `creative-practice` must not invent skills or completed work. `rituals-habits` must not become a scheduler, reminder system, or claim that a routine actually ran. `roles-archetypes` is descriptive identity only and never grants role/permission authority. `decision-style` describes preferences and never overrides current policy, risk gates, or retained owner decisions.

Optional personality typologies such as MBTI-style self-assessment are **post-canon descriptive tools only**. Do not introduce them during Bootstrap/Explore or use a type label to fill undecided canon. Build/review the identity first, then classify the resulting patterns without rewriting canon to fit the classification.

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

For readability, organize the public explainer around **reader jobs**, not one top-level section per schema concept. Prefer a small number of major editorial sections with related concepts grouped under meaningful subheads. Preserve useful deep anchors when consolidating content. The current reading arc is:

1. why explicit identity matters;
2. the model — ownership, honest unknowns, lifecycle, provenance;
3. how to build and maintain canon;
4. optional dimensions and downstream typology;
5. a synthetic example;
6. safety/epistemic boundaries;
7. maturity;
8. the paired memory relationship as a closing context.

Do not re-fragment that arc merely because a new optional module or schema field is added.

## Public document reader

Markdown remains canonical. The in-page reader is presentation-only progressive enhancement: keep real same-origin `.md` links, fetch only selected same-origin Markdown, construct DOM nodes rather than injecting raw HTML, preserve raw-source access, and verify close/Escape/focus return/mobile containment in a real browser.

Opt human-facing skill Markdown into the reader deliberately rather than intercepting every `.md` link. YAML frontmatter is machine metadata, not article prose: the formatted view may summarize safe fields such as skill name/version while the raw view remains exact. Fenced code stays literal code content; when a fence declares a language, the reader may show that language as presentation metadata without adding a syntax-highlighting dependency.

The GitHub Pages surface is intentionally static and must preserve canonical Markdown at its literal `.md` path. Keep the root `.nojekyll` marker so frontmatter-bearing skill files are served byte-for-byte instead of being transformed into Jekyll-generated HTML.

## Validation

Run:

```text
python3 -m pip install -r requirements.txt
python3 tools/validate_identity.py
python3 tools/validate_identity.py --self-test
```

## Change workflow

Keep the repository small. Prefer a focused branch/PR for schema/skill/validator changes or material public documentation changes. Read back exact public state after publication.
