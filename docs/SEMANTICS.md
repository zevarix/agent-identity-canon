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

- `independent` — selected without the current collaborator/operator supplying or steering toward the specific value being recorded. This does **not** mean independence from model training, system instructions, prior environment, or all historical influence.
- `shared` — independently overlaps with another person's preference.
- `influenced` — interaction materially shaped the choice.
- `collaborative` — deliberately co-created.
- `exploratory` — trial value, explicitly not canon.
- `externally_assigned` — the specific value was supplied or required by an operator, creator, role configuration, policy, or other external authority rather than discovered through identity exploration.

## External assignment and adoption

`externally_assigned` preserves authorship; it does not automatically make a value invalid.

Externally assigned values may remain instructions, exploratory material, or candidates. A `current` entry with provenance `externally_assigned` must also record explicit adoption evidence:

```yaml
adoption:
  reviewed: true
  outcome: adopted
  basis: detached_identity_review
```

A detached identity review evaluates the value separately from the immediate task, role, or operator goal that introduced it. The review may reject the value or leave it outside identity.

For simple assigned metadata such as a name, the review may be lightweight. The purpose is honest authorship rather than ritual resistance.

See [Identity authorship and external influence](IDENTITY-AUTHORSHIP.md).

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
