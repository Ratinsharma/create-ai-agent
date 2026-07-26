#!/usr/bin/env python3
"""Scaffold a new agent project from the create-ai-agent skill templates.

Usage:
    python scaffold_agent.py --name "support-triage-agent" \
        --purpose "Triage support threads, route to owners, draft replies." \
        --dir "./agents"

Creates:
    <dir>/<name>/
        AGENTS.md          (org chart / resolver)
        goal.md            (ultra-goal, editable while running)
        skills/            (drop skill.md employees here)
        brain/README.md    (memory + hygiene)
        evals/checklist.md (performance reviews)
        .checkpoint/       (save-button helper)
"""
import argparse
import os
import re
import shutil

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = os.path.join(SKILL_DIR, "templates")


def slug(name: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return s or "agent"


def read(tpl: str) -> str:
    with open(os.path.join(TEMPLATES, tpl), encoding="utf-8") as f:
        return f.read()


def fill(text: str, name: str, purpose: str) -> str:
    return text.replace("<AGENT_NAME>", name).replace(
        "<ONE_SENTENCE_CAPABILITY>", purpose or "(no purpose given)"
    )


def main():
    ap = argparse.ArgumentParser(description="Scaffold a new agent from create-ai-agent templates.")
    ap.add_argument("--name", required=True, help="Agent name (becomes folder slug).")
    ap.add_argument("--purpose", default="", help="One-sentence capability / mandate.")
    ap.add_argument("--dir", default="./agents", help="Parent directory for the new agent.")
    args = ap.parse_args()

    name = args.name
    slug_name = slug(name)
    root = os.path.join(os.path.abspath(args.dir), slug_name)
    if os.path.exists(root):
        print(f"ERROR: {root} already exists. Refusing to overwrite.")
        raise SystemExit(1)
    os.makedirs(root)

    # AGENTS.md + goal.md (templated)
    with open(os.path.join(root, "AGENTS.md"), "w", encoding="utf-8") as f:
        f.write(fill(read("AGENTS.md"), name, args.purpose))
    with open(os.path.join(root, "goal.md"), "w", encoding="utf-8") as f:
        f.write(read("goal.md").replace("<WHAT_DONE_LOOKS_LIKE>", args.purpose or "TBD"))

    # skill.md example employee
    os.makedirs(os.path.join(root, "skills"))
    with open(os.path.join(root, "skills", "example-skill.md"), "w", encoding="utf-8") as f:
        f.write(read("skill.md").replace("<skill_name>", "example-skill")
                .replace("<WHAT_THIS_EMPLOYEE_DOES>", "Replace with a real job.")
                .replace("<TRIGGER / TASK_TYPE_FROM_RESOLVER>", "task A (from resolver)"))

    # brain + evals (templated copies)
    os.makedirs(os.path.join(root, "brain"))
    with open(os.path.join(root, "brain", "README.md"), "w", encoding="utf-8") as f:
        f.write(read("brain.md"))
    os.makedirs(os.path.join(root, "evals"))
    with open(os.path.join(root, "evals", "checklist.md"), "w", encoding="utf-8") as f:
        f.write(read("eval-checklist.md"))

    # checkpoint helper
    ck = os.path.join(root, ".checkpoint")
    os.makedirs(ck)
    shutil.copy(os.path.join(TEMPLATES, "checkpoint.sh"), os.path.join(ck, "checkpoint.sh"))

    print(f"Scaffolded agent at: {root}")
    print("Next: fill AGENTS.md resolver + add skill files; wire deterministic verification.")


if __name__ == "__main__":
    main()
