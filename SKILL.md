---
name: create-ai-agent
description: >-
  Operational recipe for BUILDING a new production AI agent, derived from the
  building-ai-agents-2026 field guide (18 AI Engineer 2026 talks). Load this skill
  whenever the user wants to create, scaffold, or architect a new agent, coding agent,
  agentic workflow, or "agent as a service." Produces a wired agent (skill files as
  employees, resolver/org chart, deterministic verification, save-button checkpoints,
  and a curated memory/brain) instead of a one-off prompt loop.
---

# Create an AI Agent — the wiring recipe

Loads the principles from `building-ai-agents-2026`. This skill turns them into a
**step-by-step build** plus templates and a scaffold script so every new agent we
create is wired the same disciplined way.

Core reframe (hold this the whole time): **a skill file is an employee, a resolver
table is your org chart, an eval is a performance review, and the memory is your
company brain.** You are not writing a prompt — you are hiring and training a workforce
out of markdown.

---

## When to load this skill
- User says "build an agent", "create a bot", "scaffold an agent for X", "make an
  autonomous X", or any "agent as a service" request.
- You are about to add agentic behavior to an existing system and need structure.
- You catch yourself about to write a one-off `while true` loop with no verification.

## Principles that must survive into the build (the "rules of the road")
1. **Latent vs deterministic.** Mechanics, state, and verifiable computation → code/tools.
   Taste, vague-intent understanding, judgment → the model. Most bugs are computation on
   the wrong side.
2. **One capability = one skill file = one employee.** Typed inputs, a verification step,
   and a rollback path. No side effects until validated.
3. **Verify deterministically where you can.** Types (Pydantic), tests, simulators,
   ontology/reasoner. Don't let the loop verify itself with more LLM calls — that compounds
   error across iterations.
4. **The Save Button.** Checkpoint a known-good state before any risky change; replay/
   rollback on evidence (diff-decide).
5. **One strong loop beats a multi-agent committee.** Split agents only when slices are
   truly isolated and you can scope their memory.
6. **Context engineering = which three books are open.** Cap the "smart zone" (~60–100k
   tokens for hard problems, ≤200k even on 1M windows). Compaction is fine; curate the brain.
7. **Skillify, never one-off.** When the agent does something well, turn it into a reusable
   skill. "If you ask twice, you failed."
8. **Start at 2–3x.** Small, verified, human-in-the-architecture. Expand only after it earns
   trust. The 2X and 100X founders run the *same model* — wiring is the delta.

---

## The build procedure (do these in order)

### Step 1 — Write the mandate (one line, one job)
Name the agent and state its single capability in one sentence. If you need three sentences,
you're describing three employees — split them now.

### Step 2 — Draft `AGENTS.md` (the org chart)
Create the resolver table that routes incoming work to the right skill file / sub-agent, plus
filing rules and a context budget. Use `templates/AGENTS.md` as the skeleton.
- Resolver: `task type → skill file / sub-agent / tool`
- Filing rules: when does a result get written to the brain? who arbitrates contradictions?
- Context budget: max tokens per turn, what's hot (loaded) vs cold (retrieved) memory.

### Step 3 — Split latent vs deterministic per task
For each task the agent does, decide what runs in code vs the model. Push anything mechanical,
stateful, or verifiable into a tool or deterministic function. The model only does the human
part (taste, judgment, vague intent).

### Step 4 — Write at least one skill file per repeated task (the employees)
Each skill = one job, written clearly enough for an agent to execute. Use
`templates/skill.md`. Must include: typed inputs, the deterministic verification step, and a
rollback/checkpoint reference. The skill may edit itself ("update this file when you learn
something better").

### Step 5 — Add the Save Button
Before any state-changing or risky action, checkpoint. Use `templates/checkpoint.sh` (or the
Python helper in `scripts/`). Capture a working snapshot so you can accept/revert on evidence.

### Step 6 — Wire verification (deterministic + agent-as-judge)
- Deterministic: types, unit tests, simulators, ontology/reasoner (RDFS/OWL) catch
  contradictions (e.g. second refund on one order, payout to wrong entity, impossible status).
- Agent-as-judge: run on **live traces** to catch trajectory-level failure (loops calling the
  same tool forever, inefficient paths, silent context loss). Use `templates/eval-checklist.md`.

### Step 7 — Build the brain (memory + hygiene)
Set up the memory store with: provenance on every fact, contradiction checks on collision, and a
librarian (human + agent) whose job is *pruning*. Retrieval is easy; being worth retrieving from
is the product. Use `templates/brain.md`.

### Step 8 — Start small, verify, expand
Ship one strong loop with deterministic verification and a human in the architecture. Run at 2–3x.
Only add sub-agents, more skills, or autonomously-applied changes after the core earns trust.

### Step 9 — Skillify the process
Turn this scaffolding into a reusable asset (this skill). Whenever you build a second agent,
reuse the templates; adapt, don't restart.

---

## Quick scaffold (recommended)
Run the scaffold script to generate the project skeleton, then fill in Steps 1–2 and 4–7:

```bash
python "C:/Users/ratin/AppData/Local/hermes/skills/create-ai-agent/scripts/scaffold_agent.py" \
  --name "support-triage-agent" \
  --purpose "Triage incoming support threads, route to owners, draft replies." \
  --dir "./agents"
```

It creates `AGENTS.md`, `skills/`, `brain/`, `evals/`, `goal.md`, and a `.checkpoint/`
helper, pre-filled from the templates. On this Windows box use `python` (not `uv run python3`).

## Anti-patterns to refuse
- A `while true` loop with no verification and no checkpoint.
- Letting the agent verify its own work with more LLM calls.
- Putting stateful computation in the model's context instead of code.
- A multi-agent committee where one wired loop would do.
- Dumping into memory with no provenance/pruning (confident-wrong garbage dump).
- Assuming alignment/safety comes from the model — it comes from the infrastructure.

## Source
Distilled from `building-ai-agents-2026` (18 AI Engineer 2026 talks). Per-talk crux:
`~/AppData/Local/hermes/skills/building-ai-agents-2026/references/crux-18-talks.md`.
