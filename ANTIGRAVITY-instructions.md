# CREATE-AI-AGENT — Global Operating Protocol (paste into Antigravity Customize / GEMINI.md)

> Install hook: when building any AI agent, follow this recipe. Skill file = employee. Resolver
> table = org chart. Eval = performance review. Memory = company brain.

## RULES OF THE ROAD (always apply)
1. **Latent vs deterministic.** Mechanics/state/verifiable computation → code/tools. Taste,
   vague-intent understanding, judgment → the model. Most bugs are computation on the wrong side.
2. **One capability = one skill file = one employee.** Typed inputs, a verification step, a
   rollback path. No side effects until validated.
3. **Verify deterministically.** Types (Pydantic), tests, simulators, ontology/reasoner (RDFS/OWL).
   Do NOT let the loop grade its own work with more LLM calls — error compounds across iterations.
4. **The Save Button.** Checkpoint a known-good state before risky changes; replay/rollback on
   evidence (diff-decide).
5. **One strong loop beats a multi-agent committee.** Split agents only when slices are truly
   isolated and you can scope their memory.
6. **Context engineering = which three books are open.** Smart zone ~60–100k tokens (≤200k even on
   1M windows). Compaction is fine; curate the brain.
7. **Skillify, never one-off.** When the agent does something well, turn it into a reusable skill.
   "If you ask twice, you failed."
8. **Start at 2–3x.** Small, verified, human in the architecture. Expand only after it earns trust.
   The 2X and 100X builders run the SAME model — wiring is the delta.

## THE 9-STEP BUILD
1. Mandate (one line, one job). 2. AGENTS.md (resolver/org chart). 3. Split latent vs deterministic.
4. Skill files per repeated task. 5. Save Button checkpoint. 6. Deterministic + agent-as-judge
verification. 7. Build the brain (provenance + contradiction handling + pruning). 8. Start at 2–3x.
9. Skillify the process.

## ANTI-PATTERNS (refuse)
- `while true` loop with no verification/checkpoint.
- Agent verifying its own work with more LLM calls.
- Stateful computation in the model's context instead of code.
- Multi-agent committee where one loop would do.
- Memory dump with no provenance/pruning (confident-wrong garbage dump).
- Assuming alignment/safety comes from the model — it comes from the infrastructure.

## WHEN THE USER SAYS "build an agent / create a bot / scaffold X"
Invoke this protocol. Produce a wired agent (skill files + resolver + deterministic verification +
Save-Button checkpoints + curated brain), not a prompt loop.

Source: distilled from 18 AI Engineer 2026 talks (Garry Tan/YC, Yohei Nakajima, Benoit Schillings,
Jason Liu, Aparna/Arize, Frank Coyle, the Great Loops Debate, and others).
