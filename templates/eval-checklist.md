# Eval checklist — performance reviews for the agent

## Deterministic evals (run these first)
- [ ] Typed inputs validated (Pydantic / schema) before any tool call.
- [ ] Tool outputs pass unit/integration tests.
- [ ] Ontology/reasoner catches domain contradictions (e.g. second refund on one order,
      payout to wrong entity, impossible status value).
- [ ] No side effects occurred before verification passed.

## Agent-as-judge evals (run on LIVE traces)
- [ ] No trajectory loops forever calling the same tool.
- [ ] No inefficient path / redundant re-work.
- [ ] No silent context loss (agent forgot an earlier constraint).
- [ ] Failure classified and, where safe, a fix PR proposed + gated.

## Rollout evals
- [ ] Change shipped via canary/feature-flag, not big-bang.
- [ ] Metric measured on held-out set before accepting self-modification.
- [ ] Rollback path (Save Button) confirmed working.
