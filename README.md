# create-ai-agent

A disciplined recipe + Hermes skill for **building production AI agents** the right way — not as
one-off prompt loops, but as a wired "organization" you hire, train, and manage out of markdown.

> **A skill file is an employee. A resolver table is your org chart. An eval is a performance
> review. The memory is your company brain.** You are not writing a prompt — you are building a
> workforce.

Distilled from 18 talks at **AI Engineer 2026** (the `aiDotEngineer` channel, July 2026) and
the companion `building-ai-agents-2026` field guide.

---

## Why this exists

Most "agent" projects die the same way: a `while true` loop with no verification, no checkpoint,
and no memory hygiene. This skill encodes what the best talks actually recommend:

- **Leverage is in the wiring, not the weights.** The 2X and 100X founders run the *same model*.
- **Verify deterministically.** Types, tests, simulators, ontology/reasoner — don't let the loop
  grade its own homework with more LLM calls (error compounds across iterations).
- **The Save Button.** Checkpoint a known-good state before any risky change; rollback on evidence.
- **One strong loop beats a multi-agent committee.** Split agents only when slices are truly isolated.
- **Context engineering > prompt engineering.** Compaction is fine; curate the brain.
- **Skillify, never one-off.** When the agent does something well, turn it into a reusable skill.

---

## What's in the box

```
create-ai-agent/
├── SKILL.md                      # the recipe: 9-step build + rules + anti-patterns
├── templates/
│   ├── AGENTS.md                 # org chart / resolver table (skill file = employee)
│   ├── skill.md                  # one-capability "employee" (typed inputs + verify + rollback)
│   ├── brain.md                  # memory + hygiene (library + librarian)
│   ├── eval-checklist.md         # deterministic + agent-as-judge performance reviews
│   ├── goal.md                   # ultra-goal, editable while running
│   └── checkpoint.sh             # the "Save Button" (snapshot / restore)
├── scripts/
│   └── scaffold_agent.py         # generate a new agent project from the templates
├── README.md
└── LICENSE
```

---

## Install as a Hermes skill

Clone straight into your Hermes skills directory:

```bash
git clone https://github.com/Ratinsharma/create-ai-agent.git \
  "$HOME/AppData/Local/hermes/skills/create-ai-agent"
```

Then load it when you want to build an agent:

```
skill_view(name='create-ai-agent')
```

---

## Scaffold a new agent

```bash
python scripts/scaffold_agent.py \
  --name "support-triage-agent" \
  --purpose "Triage incoming support threads, route to owners, draft replies." \
  --dir "./agents"
```

This generates:

```
agents/support-triage-agent/
├── AGENTS.md          # org chart / resolver
├── goal.md            # ultra-goal
├── skills/            # drop skill.md "employees" here
├── brain/README.md    # memory + hygiene
├── evals/checklist.md # performance reviews
└── .checkpoint/       # Save Button helper
```

> On Windows, call `python` directly (not `uv run python3` — that maps to the Store alias and
> produces zero-byte files).

---

## The 9-step build (summary)

1. **Write the mandate** — one line, one job. Need three sentences? That's three employees; split them.
2. **AGENTS.md** — resolver table routes work; sets filing rules + context budget.
3. **Split latent vs deterministic** — mechanics/state → code; taste/judgment → model.
4. **Skill files** — one per repeated task: typed inputs, verification step, rollback path.
5. **Save Button** — checkpoint before risky changes; accept/revert on evidence.
6. **Verification** — deterministic (types/ontology) + agent-as-judge on live traces.
7. **Build the brain** — provenance on every fact, contradiction handling, pruning.
8. **Start at 2–3x** — small, verified, human in the architecture. Expand only after trust.
9. **Skillify the process** — reuse these templates; adapt, don't restart.

---

## Source & attribution

Principles distilled from 18 AI Engineer 2026 conference talks, including:

- *The Company Brain* — Garry Tan (YC)
- *The Great Loops Debate* — Livingston / Huntley / Horthy / Kostruba
- *ActiveGraph / BabyAGI4* — Yohei Nakajima
- *SWE Is Not Writing Code* — Benoit Schillings (Google DeepMind)
- *Codex Workshop* — Jason Liu (OpenAI)
- *Self-Improving Agent* — Jason Lopatecki · *Agent as Judge* — Aparna (Arize)
- *Ontologies* — Frank Coyle · *Everything Is a Rollout* — Alex Shaw & Ryan Marten
- *Claude Long-Horizon* — Lance Martin · *Killed Multi-Agent* — ZS · *Arch Half-Life* — Dan Farrelly
- *Skills & New SDKs* — Elvin A · *The Harness Becomes a Claw* — Sam Bhagwat · *The Save Button* — Hamza Tahir
- *Loop Engineering* — Kyle Mistele · *The Harness Is Not Enough* — Dex Horthy · *HTML Is All Agents Need* — James Russo

Full per-talk crux: companion skill [`building-ai-agents-2026`](https://github.com/Ratinsharma).

---

## License

MIT — see [LICENSE](LICENSE). Free to use, fork, and ship.
