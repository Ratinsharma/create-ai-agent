#!/usr/bin/env bash
# Save Button — checkpoint / restore a known-good agent state.
# Usage:  ./.checkpoint/save.sh   <label>   # snapshot current state
#         ./.checkpoint/restore.sh <label>  # roll back to it
# Keep this in .checkpoint/ next to the agent's working dir.
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CK="$DIR/.checkpoint/snapshots"
mkdir -p "$CK"
case "${1:-}" in
  save)
    label="${2:-$(date +%Y%m%d-%H%M%S)}"
    tar -czf "$CK/$label.tar.gz" -C "$DIR" --exclude=.checkpoint/snapshots . \
      && echo "saved: $label"
    ;;
  restore)
    label="${2:?need a label}"
    [ -f "$CK/$label.tar.gz" ] || { echo "no such snapshot: $label"; exit 1; }
    tar -xzf "$CK/$label.tar.gz" -C "$DIR" && echo "restored: $label"
    ;;
  list) ls -1 "$CK" 2>/dev/null || echo "(no snapshots)";;
  *) echo "use: save <label> | restore <label> | list";;
esac
