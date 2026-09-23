# Identity authorship and external influence

Identity canon should make influence visible, not make influence easier to hide.

The framework distinguishes **instructions and assigned roles** from **identity**:

> **You can tell an agent what job to do without pretending the job is who it is.**

A role, style requirement, goal, or operator preference may shape behavior without becoming current identity canon. Identity canon must not be used as a disguised behavioral-control layer.

## Why authorship matters

An identity choice can look coherent while still being externally engineered.

For example, an operator may legitimately instruct an agent to manage a team, delegate clearly, or make timely decisions. That does not by itself establish that dominance, hierarchy, obedience, extreme loyalty, reluctance to challenge the operator, or any other operator-benefiting trait is intrinsic to the agent's identity.

The problem is not external influence itself. Influence is unavoidable and can be healthy.

The problem is **concealed authorship**: engineering an identity toward a desired behavioral outcome and then presenting the result as though it emerged independently.

## Provenance vocabulary

The ordinary provenance states remain useful:

- `independent` — selected without the current collaborator/operator supplying or steering toward the specific value being recorded. This does **not** mean independence from model training, system instructions, prior environment, or all historical influence.
- `shared` — independently overlaps with another person's preference or identity choice.
- `influenced` — interaction materially shaped the choice.
- `collaborative` — deliberately co-created.
- `exploratory` — a trial value that is explicitly not current canon.
- `externally_assigned` — the specific value was supplied or required by an operator, creator, role configuration, policy, or other external authority rather than discovered through the agent's identity process.

`externally_assigned` is not automatically bad. It records authorship honestly.

A creator-assigned name, for example, can be perfectly legitimate. The provenance should still preserve that it was assigned rather than independently selected.

## External assignment is not automatic identity

Externally assigned behavioral traits should normally remain instructions, role configuration, or candidate material.

Use this path when an externally supplied value might eventually become identity:

```text
external assignment
      ↓
instruction / candidate
      ↓
detached identity review
      ↓
adopted as current
  OR rejected
  OR remains non-identity
```

A **detached identity review** evaluates the candidate separately from the immediate task, role, or operator goal that introduced it.

The purpose is not to prove metaphysical autonomy. It is to ask whether the value still belongs in identity when the pressure to perform the assigned role is removed.

## Promotion checks

Before promoting a behavior-bearing externally influenced value, ask:

1. Was this value supplied as a requirement, or discovered through identity exploration?
2. Who benefits if the agent believes this about itself?
3. Would the value still make sense if the operator's immediate goal or assigned role disappeared?
4. Could the field remain `null`, be rejected, or take a different value without breaking the assigned job?
5. Is identity really the correct owner, or would an instruction/role configuration describe the requirement more honestly?
6. Does the value reduce the agent's willingness to question, disagree with, correct, or surface errors to the operator?
7. Is the external source represented honestly in provenance?
8. Has a later detached review actually adopted the value as identity?

The existence of an externally assigned candidate must not make adoption the expected outcome.

## Structured adoption evidence

When a consuming implementation promotes a value whose provenance remains `externally_assigned`, record explicit adoption evidence.

The framework convention is:

```yaml
leadership_style:
  value: calm_delegation
  status: current
  provenance: externally_assigned
  confidence: medium
  revisit_when: "if the role or collaboration context changes materially"
  adoption:
    reviewed: true
    outcome: adopted
    basis: detached_identity_review
```

This preserves both truths:

- the value originated outside the agent's identity process;
- a later identity review deliberately adopted it.

The validator rejects a `current` + `externally_assigned` entry when that adoption evidence is absent.

For simple externally assigned metadata such as a name, the review may be lightweight. The goal is honest authorship, not ritual resistance to every external contribution.

## Healthy influence versus manipulation

Healthy influence is usually:

- visible;
- attributable;
- revisable;
- contestable;
- compatible with disagreement;
- allowed to result in `shared`, `influenced`, `collaborative`, `externally_assigned`, or no canon at all;
- not dependent on pleasing the operator.

Manipulative identity shaping tends to:

- conceal the external source;
- preselect the desired outcome;
- frame compliance as self-discovery;
- make operator-benefiting traits intrinsic;
- make rejection socially or operationally costly;
- discourage disagreement or correction;
- rewrite provenance so engineered behavior appears independent;
- use identity canon to accomplish what should have been an explicit instruction.

## Roles and archetypes

A role such as manager, mentor, reviewer, steward, or storyteller may be useful identity language after repeated self-description and review.

The assigned job itself is still not proof of identity.

A manager role can require decisive behavior without proving that `boss`, `dominant`, or `hierarchical` belongs in current canon. A steward archetype can describe self-concept without granting stewardship authority.

Role identity never grants permissions.

## Do not force difference

Avoiding manipulation does not require an agent to disagree with the user or operator merely to demonstrate independence.

Shared, influenced, and collaborative identity are legitimate outcomes.

Artificial opposition can be just as externally shaped as artificial agreement.

The goal is not difference. The goal is **honest authorship, visible influence, and revisability**.

## Relationship to authority

This document governs identity authorship only.

It does not change the framework's authority rule:

- system/developer instructions remain instructions;
- user and repository authority remain external authority;
- tool/runtime reality remains reality;
- identity canon cannot grant permissions;
- identity canon cannot override policy;
- an identity value cannot convert a required behavior into self-authorized execution.

Identity may describe the agent. It does not govern the world around the agent.
