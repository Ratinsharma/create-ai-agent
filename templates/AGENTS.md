# AGENTS.md — <AGENT_NAME>

> One capability, one job. This file is the **org chart**: it routes work and sets the rules.
> A skill file is an employee. An eval is a performance review.

## Mandate (one line)
<ONE_SENTENCE_CAPABILITY>

## Resolver table (org chart: task → handler)
| Task type | Handler (skill file / sub-agent / tool) | Notes |
|-----------|------------------------------------------|-------|
| <task A>  | skills/<task_a>.md                       | <when> |
| <task B>  | sub-agent: <name>                        | isolated slice only |
| <mechanical> | tool: <function>                       | deterministic, in code |

## Filing rules (internal process)
- Results worth keeping are written to the brain with **provenance** (source + timestamp).
- On contradiction, the librarian decides; the older fact is not silently overwritten.
- No side effects (external writes, sends, deploys) until the verification step passes.

## Context budget (which three books are open)
- Smart zone cap: ~<N>k tokens per turn (hard ceiling 200k even on 1M windows).
- Hot memory (always loaded): <list>.
- Cold memory (retrieved on demand): <list>.
- Compaction: allowed; rely on the brain for long-term state, not the context window.

## Verification (performance review)
- Deterministic gate: <types/tests/simulator/ontology>.
- Agent-as-judge on traces: <what failure modes to catch>.
- Human-in-the-loop for: <decisions the agent must not make alone>.

## Save Button
Before any risky/state-changing action, checkpoint via `.checkpoint/` (see checkpoint helper).
Accept/revert on evidence (diff-decide).

## Operating mode
- One strong loop, small and verified. Expand only after it earns trust.
- Start at 2–3x, not 100x.
