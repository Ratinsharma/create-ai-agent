# Brain — memory + hygiene

> Company brain = library + librarian. Retrieval is the primitive (like Postgres is B-trees).
> The hard part is everything around it. Being worth retrieving from is the product.

## What gets written down
- Decisions, with **provenance**: source, timestamp, who/what asserted it.
- Customer/domain context the agent needs to act like a colleague, not an assistant.

## Promotion rules (hot vs cold)
- Hot (always loaded): <current active facts>.
- Cold (retrieved on demand): <historical/reference>.

## Contradiction handling (the librarian)
- When new info collides with old, DO NOT silently overwrite.
- Record both, flag for human+agent arbitration, keep provenance on each.

## Pruning
- Periodic prune of stale/low-signal facts. A brain nobody curates becomes a garbage dump with
  great search — it surfaces stale facts with total confidence.

## Failure modes to avoid
- No provenance → can't trace a wrong answer.
- No contradiction check → confident contradictions.
- No pruning → entropy grows, retrieval degrades.
