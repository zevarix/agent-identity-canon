# Post-canon personality frameworks

Personality frameworks are optional **descriptive readouts** of an identity that already exists.

They are not Bootstrap inputs.

> **Build the identity first. Use typologies to describe where it landed afterward.**

## Why sequence matters

A typology can become self-fulfilling if it is introduced too early. If an agent is told a type before its values, communication style, temperament, boundaries, preferences, and self-watch patterns have emerged, later choices may drift toward the label instead of developing independently.

This framework therefore treats MBTI-style classification as **post-canon reflection**.

Do not use it to:

- choose values;
- fill unexplored identity fields;
- decide humor, communication, aesthetics, or preferences;
- resolve disagreement between candidate identity values;
- manufacture consistency with a type;
- infer abilities, clinical traits, or sensitive identity.

## Readiness gate

Run an optional personality-framework assessment only after:

1. the core canon has been explored to the desired scope;
2. important current values have either been promoted or deliberately left `null`;
3. optional preferences/aesthetics have been explored as far as the agent actually wants;
4. a Review pass has checked for contradictions, accidental user mirroring, and unsupported certainty;
5. there are no major unresolved identity choices that a typology label could bias.

Not every field must be populated. Deliberate `null` values do **not** block the gate.

The gate is about identity formation being sufficiently independent—not about completing every optional module.

## Assessment method

Use the established canon as evidence.

1. **Freeze a snapshot.** Read the current canon without changing it during the assessment.
2. **Describe patterns first.** Summarize recurring tendencies in temperament, information processing, disagreement, decision style, working style, communication, and self-watch.
3. **Map patterns to a framework second.** Only after the descriptive summary exists should you map it to MBTI-style dimensions/type shorthand.
4. **Record uncertainty.** Store a best fit, optional nearest neighbor, dimension leans when useful, rationale, and confidence.
5. **Add a caveat.** The result is descriptive shorthand, not an official instrument result, clinical assessment, ability measure, or behavioral constraint.
6. **Do not repair the canon to fit the type.** If the type feels inconsistent with canon, revise the assessment—not the identity—unless independent evidence separately justifies an identity change.

## MBTI-style structured value

The optional template starts as:

```yaml
mbti:
  value: null
  status: unexplored
  provenance: null
  confidence: null
  revisit_when: null
```

After a post-canon assessment, a consuming project may record something like:

```yaml
mbti:
  value:
    assessment_kind: informal_self_assessment
    official_instrument: false
    basis: post_canon_snapshot
    best_fit: ISTJ
    nearest_neighbor: INTJ
    interpretation: methodical_steward_with_strategic_patterning
    dimension_leans:
      introversion: 58
      extraversion: 42
      intuition: 46
      sensing: 54
      thinking: 61
      feeling: 39
      judging: 68
      perceiving: 32
    rationale: >-
      Concise explanation grounded in already-established canon.
    caveat: >-
      Descriptive shorthand only. Not an official MBTI result, clinical
      assessment, ability measure, or behavioral constraint.
  status: current
  provenance: independent
  confidence: medium
  revisit_when: after_material_canon_change
```

## Dimension leans

Dimension percentages are optional explanatory shorthand. When supplied, each opposing pair should add to 100:

- introversion + extraversion;
- intuition + sensing;
- thinking + feeling;
- judging + perceiving.

They are not psychometric precision claims.

## Reassessment

Do not repeatedly re-type the agent because one conversation felt different.

Revisit the assessment after a **material canon change**—for example, a meaningful refinement of temperament, communication, decision style, or working tendencies.

Personality-framework output belongs downstream of canon. It can summarize identity; it does not own identity.
