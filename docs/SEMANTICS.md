# Identity canon semantics

Identity fields use the same shape:

```yaml
humor_style:
  value: null
  status: unexplored
  provenance: null
  confidence: null
  revisit_when: null
```

Required keys are `value`, `status`, `provenance`, `confidence`, and `revisit_when`.

## Null and absence

- `null` means unknown, undecided, or intentionally left for later exploration.
- `[]` means explicitly none.
- `false` means a known negative boolean.
- a populated value means an actual identity value is being explored/proposed/held.
- an omitted field means the schema field does not apply or has not been instantiated.
- an omitted optional module means that identity area has not been adopted.

Empty strings are invalid in structured canon.

## Current-canon lifecycle

### `unexplored`

No answer has been selected. `value`, `provenance`, and `confidence` are null.

### `exploratory`

The agent is actively trying an idea without treating it as canon. A value may still be null. A populated trial value should normally use provenance `exploratory`.

### `candidate`

A concrete proposed value. Requires non-null value, recognized provenance, and confidence.

### `current`

The active canonical value. Requires non-null value, recognized provenance, and confidence.

## History outcomes

`refined`, `superseded`, and `retired` belong to history events rather than active canon entries.

## Provenance vocabulary

- `independent` — emerged from the agent's own existing canon/reasoning/self-directed exploration.
- `shared` — independently overlaps with another person's preference.
- `influenced` — interaction materially shaped the choice.
- `collaborative` — deliberately co-created.
- `exploratory` — trial value, explicitly not canon.

## Confidence

Allowed values are `low`, `medium`, `high`, or `null` when no value has been selected.

## Core, preference, and scene

Core canon contains stable anchors changed deliberately. Preference canon contains tastes/recurring choices that can evolve naturally. Scene/context interpretation is one-off expression and should not become canon automatically.

## References

A module may optionally contain a `references` list of relative repository paths. References must not be absolute or use `..` and must resolve to existing files.

## Optional module adoption

Optional templates are marked `optional: true` and `template: true`. They are not active canon until a consuming identity owner deliberately instantiates them.

Optional module names do not imply that every agent should adopt them. See [`OPTIONAL-MODULES.md`](OPTIONAL-MODULES.md) for module-specific ownership boundaries, selective-adoption guidance, and the distinction from memory/runtime/project state.

### Post-canon personality frameworks

The optional `personality-frameworks` module is additionally marked `post_canon_only: true`. It describes established canon; it must not be used to generate canon.

For the `mbti` entry, an unexplored template uses `value: null`. A populated value is a nested descriptive assessment containing an informal self-assessment marker, `official_instrument: false`, a post-canon basis, a recognized four-letter best fit, optional nearest neighbor, rationale, caveat, and optional dimension leans.

When dimension leans are present, opposing pairs should each total 100. They are explanatory shorthand, not psychometric precision claims.
