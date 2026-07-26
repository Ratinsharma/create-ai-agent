---
name: <skill_name>
description: >-
  One job, written clearly enough for an agent to execute. Typed inputs + a deterministic
  verification step + a rollback reference. This file may edit itself when a better approach
  is found ("update this file when you learn something").
---

# Skill: <skill_name>

## Job (one sentence)
<WHAT_THIS_EMPLOYEE_DOES>

## When to use
<TRIGGER / TASK_TYPE_FROM_RESOLVER>

## Inputs (typed — Pydantic at the door)
- `field_a` (type): <meaning>
- `field_b` (type): <meaning>

## Procedure
1. <deterministic step — in code/tool where possible>
2. <model step — taste/judgment only>
3. <call tool / write artifact>
4. **Verify** (deterministic gate): <how we know it worked — tests, types, ontology check>
5. If verification fails → return to model with the failure, or route to human-in-the-loop.

## Rollback / Save Button
- Before any state change, checkpoint via `.checkpoint/`.
- Accept only if the metric/check improved; otherwise revert.

## Self-improvement
- After a run, if a better approach is found, update this file.
- Do NOT apply unverified changes to this skill.
