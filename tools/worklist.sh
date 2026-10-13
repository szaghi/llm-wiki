#!/usr/bin/env bash
# Derived worklist: corpus PDFs with no Source page referencing them.
# Usage: tools/worklist.sh <bundle>
#
# The corpus directory is the optional `corpus` key of <bundle>/bundle.toml (a leading ~ is
# expanded); without it, the Layer-1 archive named after the bundle, ~/papers/mosaic/<bundle> (D17).
set -euo pipefail

[[ $# -ge 1 ]] || { echo "usage: tools/worklist.sh <bundle>" >&2; exit 2; }
bundle="$1"
repo="$(cd "$(dirname "$0")/.." && pwd)"
sources_dir="$repo/$bundle/wiki/sources"
card="$repo/$bundle/bundle.toml"

corpus_dir=""
if [[ -f "$card" ]]; then
    corpus_dir="$(python3 -c 'import os, sys, tomllib; print(os.path.expanduser(tomllib.load(open(sys.argv[1], "rb")).get("corpus", "")))' "$card")"
fi
[[ -n "$corpus_dir" ]] || corpus_dir="$HOME/papers/mosaic/$bundle"
[[ -d "$corpus_dir" ]] || { echo "corpus not found: $corpus_dir" >&2; exit 1; }

pending=0
for pdf in "$corpus_dir"/*.pdf; do
    [[ -e "$pdf" ]] || continue
    base="$(basename "$pdf")"
    if ! grep -rqlF "$base" "$sources_dir" 2>/dev/null; then
        echo "$base"
        pending=$((pending + 1))
    fi
done
total="$(find "$corpus_dir" -maxdepth 1 -name '*.pdf' | wc -l)"
echo "---" >&2
echo "pending: $pending / $total" >&2
