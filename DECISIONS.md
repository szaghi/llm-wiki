# Decision Record

ADR-lite log of design decisions for this repository. The law these decisions
produce lives in `CLAUDE.md` (repo-wide) and each bundle's `CLAUDE.md`. Challenge
a rule by reopening its decision here, with the original rationale in view.

Origin: a grilling session (2026-07-08) auditing `llm-wiki-building-guide.md`
against the actual OKF v0.1 spec
(<https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md>)
and against the first real use case (bundle `div-free-amr`).

## D1 — Claude Code is the compiler

The guide's Ollama + Qwen3:14b + Python ingest stack is discarded. **Why:** a
14B local model is underpowered for dense mathematical PDF extraction; Claude
Code reads PDFs natively (including visually, which covers image-only scans),
and the sources are public literature — no privacy argument for local-only.
The guide's own code also contradicted its design (its "stateful merge" pass
was implemented as an unconditional overwrite). The ingest pipeline is a
documented *procedure* in the constitution, not a script.

## D2 — Source-agnostic ingest, trusted ab origine

Any medium (paper, book, thesis, blog, notes, slides, code, report). The human
personally reviews every source before ingestion, so there is **no trust
quarantine and no reliability scoring**. Trust is a property of the ingestion
act, not a field.

## D3 — `status` is claim-kind, not trust

`established | hypothesis` on every concept page. **Why:** a trustworthy source
(the human's own notes) can still carry working hypotheses; without the
distinction the wiki launders hypotheses into literature facts and feeds them
back as external confirmation — a confirmation-bias amplifier. One line,
no folder segregation, no quarantine.

## D4 — Eight-type taxonomy, folders mirror types

Definition, Method, Operator, Result, Property, Benchmark, Software, Source.
No `Person` type (authors are source metadata, not knowledge nodes). No
`Conjecture` type (= `Result` + `status: hypothesis`; a separate type would
double-encode the status axis). A `syntheses/` folder appeared in an early
layout draft and was dropped: the taxonomy stays at eight until a real page
needs a ninth type — extend by reopening this decision.

## D5 — Canonical notation, normalize at compile time

KaTeX `$`/`$$` only. Concept pages are forbidden paper-native notation; the
bundle's `notation.md` registry is normative; Source pages carry a
`# Notation map` audit trail. **Why:** every paper uses its own symbols;
compiling in native notation fragments the graph (mathematical entity
resolution). The map records each translation once, where it can be audited —
mistranslated notation is how a compiled wiki silently corrupts a theorem's
hypotheses.

## D6 — Reference-in-place; capture only the undurable

Durably archived sources (e.g. the mosaic PDF corpus) are referenced via
`local_file`, never copied. Web content is captured to `raw/web/` as markdown
snapshots; loose documents to `raw/docs/`. No `inbox/` state machine —
ingestion is an explicit act. **Why:** copying creates a second source of
truth that drifts; DOIs on Source pages are a better portability guarantee
than duplicated binaries. **Cost accepted:** the bundle alone is not
self-contained; a clone without the referenced archives has pointers, not PDFs.

## D7 — Merge semantics: evidence layers, recency never wins

Agree → add citation. Extend → integrate, cited. Contradict → `## Contradictions`,
attributed, both sides cited; closure only by explicit supersession (erratum,
corrected proof) or human fiat recorded with `status: hypothesis` attribution.
**Why:** in this domain, contradictions between papers are first-class content;
"resolving" them destroys exactly what a review must analyze.

## D8 — One repo, many bundles; law in files, progress derived

`~/llm-wiki` is a single git repo; bundles are sibling directories sharing
`CLAUDE.md`, `DECISIONS.md`, `tools/`. Multi-session continuity rests on three
instruments: (1) progress derived from artifacts (Source page exists = ingested;
worklist = corpus minus Source pages — a stored queue can lie, a derived one
cannot go stale); (2) atomic per-source commits as resume points; (3) `log.md`
as the human-readable journal. Nothing load-bearing lives in conversation
memory or the assistant's auto-memory.

## D9 — Markdown links only; curated, lint-verified indexes

Absolute bundle-relative links per OKF recommendation; `[[wikilinks]]` rejected
(viewer dialect, breaks grep-ability and conformance). Link semantics in prose —
OKF links are untyped by design. Indexes are compiler-maintained and
linter-enforced (completeness + description consistency) rather than
script-generated, so the root index stays *curated* as a reading guide.

## D10 — Two-tier verification; no vector search

Deterministic linter at every ingestion (OKF conformance + repo law + link
resolution + index consistency + math syntax; broken links are errors, stricter
than OKF). LLM deep-lint every 10 ingestions for what cannot be deterministic:
notation compliance, contradiction staleness, tag synonyms. The guide's QMD /
embedding / RRF query stack is **deleted, not deferred**: a compiled bundle of a
few hundred pages is navigated, not retrieved; adding vector infrastructure
re-imports the RAG machinery this pattern exists to replace. Reopen only if a
bundle outgrows navigation (~thousands of pages).

## D11 — Granularity: substance earns pages, stubs are forbidden

Admission: ≥2 sources, or a single source's substantive named contribution, or
an algebraic identity, or a load-bearing definition. Minimum page = frontmatter
+ real definition + one citation. The single-source clause is deliberate: in a
specialized corpus, several important methods have exactly one paper.

## D12 — Bundles are agnostic of external repositories

A bundle never references, reads, or depends on any other project repository
(in particular: the div-free-amr review workspace). Bibliographic metadata is
derived from sources themselves, not imported from external databases; tag
vocabularies are bundle-native and emergent; the notation registry was seeded
once from good existing conventions and is wiki-native law with no back-pointer.
**Why (user decision):** the wiki is a standalone second brain; other projects
may later exploit it, but that coupling is decided and recorded in *those*
projects, never here.

**Amendment (2026-10-08, user decision): frozen captures of sibling
projects.** A sibling project's records (docs, issue threads, run data) may
be ingested as a source, but only as a frozen Layer 1 capture under
`raw/docs/<slug>/`, pinned to a commit or date. The bundle never reads the
live repository. Claims from such sources are `status: hypothesis` (D3),
and they can never, on their own, promote a claim to `established` or close
a `Contradictions` entry. An evolved record is re-captured under a new slug;
captures are never refreshed in place. **Why:** D12 forbids coupling, not
content. A frozen capture keeps the bundle self-sufficient, and the
conditions stop the human's own work from re-entering the wiki as external
confirmation. First instance: `zaghi-2026`.

## D13 — The building guide is superseded, never ingested

`llm-wiki-building-guide.md` remains as the origin document with a superseded
notice. Known defects: Docs-export artifacts (mangled links, dead image
placeholders where its equations were), content-farm sourcing, a merge pass
implemented as overwrite, a linter that false-fails on `---` in bodies. Its
OKF-conformance content was verified against the real spec and absorbed into
`CLAUDE.md`.

## D14 — The compiler stages; the human commits (corrected)

**Original (2026-07-08, revoked the same day):** the compiler was granted a
standing exception to make per-source commits. The compiler acted on it for
the scaffold and the two pilot ingestions (accepted retroactively) and also
set `commit.gpgsign false` repo-locally — which would have silently disabled
the human's GPG signing (now reverted).

**Corrected rule (user decision, 2026-07-08):** the compiler's atomic unit
ends at **staging** (`git add -A`) plus a prepared Conventional Commit message
(`docs(<bundle>): ingest <source-slug>`); committing is reserved to the human,
GPG-signed. This matches the user's global no-commit rule — the "approved
protocol" reading that stretched it into commit authorization was wrong.
The multi-session resume model (D8) survives unchanged: fully-staged =
ingestion complete awaiting commit; unstaged noise = aborted, discard.
Never `Co-authored-by`.

## D15 — Bundle bibliography: `.bib` canonical, `.md` generated (2026-07-10)

Ingesting a paper means reading its reference list; before D15 that reading
was discarded, so the citation graph died at the Source-page boundary. Each
bundle with scholarly sources now maintains `wiki/bibliography.bib`: every
work cited by any ingested source, **complete and unfiltered** (relevance
filtering is a judgment call that destroys data — dedup and `citedby` counts
do the ranking), keyed by the Source-page slug convention.

**Canonical/generated split (user decision):** the user wanted both `.bib`
and `.md`; two hand-maintained formats describing the same data will diverge,
so exactly one is canonical. The `.bib` wins (LaTeX-usable directly, natural
container for reference metadata, tolerates the custom `citedby` field);
`bibliography.md` is generated by `tools/bib_to_md.py` and the linter enforces
sync. Consistent with D8, nothing is stored that can be derived: ingested-ness
= key matches a Source page; reference-extraction progress = slug appears in
≥1 `citedby` (`--pending` lists the remainder). The `citedby` graph extends
the worklist beyond PDFs already sitting in the corpus directory:
heavily-cited non-ingested entries are the objective ingestion frontier.

**Backfill (user decision):** full, for all 61 pre-D15 ingestions, in batches
of ~10 sources per staged unit — the citation graph is only honest when
complete. The `.bib` was seeded from Source-page frontmatter (metadata already
page-1-verified at ingestion; titles recovered from the display-title
convention `Authors (year) — <paper title>`); backfill batches reopen each
PDF's reference list and may refine seeded venue strings.

## D16 — Batched-backfill merger and mandatory duplicate sweep (2026-07-22)

The D15 backfill of `div-free-amr` (61 sources, ~4000 references, six batches)
was driven by a merge harness that hardened into a reusable tool,
`tools/bib_merge.py`, after the first bundle proved its shape. Two lessons from
that backfill are now encoded in the tool and in law:

**The merger flags identities; the human resolves them.** Merging ten
reference lists at once produces dense key collisions — the same slug-style key
denoting different works in different fragments, title-less (ApJ/PRD/A&A)
citations distinguishable only by venue numbers, near-duplicate variants. The
tool never guesses: it emits `[conflict]`/`[venuecheck]`/`[suspect]` flags,
takes human-reviewed resolution tables (a Python module: ALIASES, SILENCED,
NOTES, REPAIRS, FIXUPS), and refuses `--write` while any flag is open. The
`[venuecheck]` heuristic — placeholder-title merges whose journal/volume/page
numbers do not overlap — is the decisive signal for title-less lists and
caught real wrong-merges in every batch after it was added.

**A `SILENCED` pair is a claim, not a dismissal.** Silencing a flag asserts two
keys are genuinely distinct works; that assertion needs the same scrutiny as a
merge. Wrongly silencing hid real duplicates twice (a batch-3 short-title
Bossavit silence masking a distinct work; a batch-6 `stone-1992-c` silence
hiding an identical ApJS 80:791 entry). Both were caught only at the closing
audit.

**The whole-corpus duplicate sweep (`--dupes`) is mandatory after the final
batch, because the batch process is structurally blind to it.** The merge
dedups by key, and keys follow each citing source's spelling — so the same work
entered under two first-author spellings (OCR corruption, a mis-transcribed or
reordered author list) lands under two keys that no per-batch check can relate.
Only a whole-corpus grouping by (normalized title, year) finds them. On
`div-free-amr` the closing sweep found 11 such duplicates the six batches all
missed — including a JCP 150:561 paper filed once as `jiang-1999` and once, via
a wrong-author transcription, as `hu-1999`.

Scope: this tool is for the batched backfill only. A single new source's
reference list (ordinary ingestion step 5) is hand-edited into the `.bib` —
the merger's machinery earns its cost only at ~10 fragments per run.
