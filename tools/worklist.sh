#!/usr/bin/env bash
# Derived worklist: corpus files with no Source page referencing them.
# Usage: tools/worklist.sh <bundle>   (default: div-free-amr)
set -euo pipefail

bundle="${1:-div-free-amr}"
repo="$(cd "$(dirname "$0")/.." && pwd)"
sources_dir="$repo/$bundle/wiki/sources"

corpus_dir="$HOME/papers/mosaic/div-free-amr"   # per bundle CLAUDE.md
[[ -d "$corpus_dir" ]] || { echo "corpus not found: $corpus_dir" >&2; exit 1; }

pending=0
for pdf in "$corpus_dir"/*.pdf; do
    base="$(basename "$pdf")"
    if ! grep -rqlF "$base" "$sources_dir" 2>/dev/null; then
        echo "$base"
        pending=$((pending + 1))
    fi
done
total="$(ls "$corpus_dir"/*.pdf 2>/dev/null | wc -l)"
echo "---" >&2
echo "pending: $pending / $total" >&2
