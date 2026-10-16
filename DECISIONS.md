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

## D17 — Second bundle; each bundle owns a self-contained archive (2026-10-08)

**Decision (user):** a second bundle, `high-order-capturing-schemes`,
covers high-order shock-capturing schemes with a broad scope. It overlaps
heavily with `div-free-amr`: WENO-based MHD, high-order CT and AMR papers
belong to both. Bundles stay mutually independent:
- An overlapping work is ingested separately in each bundle, as an
  independent Source page read for that bundle's subject and written in
  that bundle's notation.
- A bundle never links to another bundle's pages and never reuses its
  registry or bibliography.

**Archive rule.** Each bundle's Layer-1 archive is
`~/papers/mosaic/<bundle>/`, named after the bundle. A work shared with
another bundle's archive is **copied** into it, never referenced across
archives. `tools/worklist.sh` derives the corpus path from the bundle name.

**Why:** one archive per bundle keeps the derived worklist correct (D8);
pointing into a sibling archive would list all its files as pending. It
also keeps a bundle relocatable without the other. Duplicated PDFs cost
disk space only. Copying never modifies the source archive, so Layer-1
immutability holds.

## D18 — Third bundle for simulation codes (2026-10-12)

**Decision (user):** classes 7 and 8 of the ADAM paper collection
(astrophysics codes and physics; GPU/HPC frameworks), out of scope for
both existing bundles, get a third bundle, `astrophysical-simulation-codes`.
Its scope is "codes of both kinds": astrophysical (M)HD frameworks and
their physics modules, and GPU or performance-portable frameworks for
compressible flow whether astrophysical or not.

**How it relates to D12 and D17:** the frameworks that the class-7 papers
extend (Athena, Athena++, PLUTO, Castro, a GPU AMR code, STREAmS) are
already ingested in the other bundles; they are copied into this bundle's
archive and re-ingested for their code-design content, with no links
across bundles.

**Why:** the material is about software architecture, physics modules and
performance, a different subject from discretizing divergence constraints
or designing capturing schemes; folding it into either bundle would have
diluted that bundle's registry and reading guide.


## D19 — Public site, bundle cards and the consultation plugin (2026-10-13)

**Decision (user):** the repository becomes consumable by other people. It
is published (public repository, documentation site on GitHub Pages built
with VitePress like the user's other projects), every bundle is rendered on
the site, the bundles get a generated list and a visual map, and the
consultation skill ships in the repository as a Claude Code plugin.

**What it adds:**
* `<bundle>/bundle.toml`, the bundle card: `title`, `summary`, `keywords`
  (the skill's trigger vocabulary) and an optional `corpus` path that
  `tools/worklist.sh` reads. These are the only hand-written facts about a
  bundle; every count is derived from the wiki at call time
  (`tools/bundles.py`), in keeping with D8.
* Generated regions in `README.md` and `skills/llm-wiki/SKILL.md`, rewritten
  by `tools/bundles.py --write` and checked by `--check` in CI, so the
  bundle list cannot go stale.
* `tools/site_sync.py`, which copies each wiki into the site with its
  bundle-root links rewritten, and derives the page graphs and the
  bundle map. Its output is git-ignored and never edited; the bundles
  themselves are untouched.

**How it relates to D12:** bundle content still never links across
bundles. The bundle map's overlaps (cited works shared by DOI or title and
year, sources ingested in several bundles, pages with the same name or a
shared alias) are computed at build time and live only in the site. They
are navigation, not claims: an alias match can be loose, and the map shows
the matched name so a reader can judge it.

**Why:** a wiki only its author can navigate is a private notebook. The
rendered site lets a reader without Claude Code use the bundles; the plugin
lets a Claude Code user consult them from any directory; the generated
registry keeps the public bundle list honest; and KaTeX at build time turns
the math law into a check over every page.

## D20 — Four bundles founded on a textbook (2026-10-13)

**Decision (user):** four new bundles, `linear-elliptic-solvers`,
`curvilinear-metric-discretization`, `hyperbolic-pde-theory` and
`fourier-analysis-of-schemes`, are founded on one textbook, Riley, Hobson &
Bence, *Mathematical Methods for Physics and Engineering* (3rd ed., 2006),
each reading only its own chapters. Further sources are filed by the user
as needed. Variational methods were declined; integral equations and
symmetry/probability topics were deferred as lower interest.

**How it relates to D12 and D17:** the book's PDF is copied into each of
the four archives, and each bundle ingests it as `riley-2006` for its own
scope, with no links across bundles. `hyperbolic-pde-theory` and
`fourier-analysis-of-schemes` overlap `high-order-capturing-schemes` by
design: they compile continuum theory and analysis tools, and that bundle
keeps the schemes.

**Why:** the book's topics underlie the user's current work and have a
research literature beyond it. A textbook is a sound reference for
definitions and standard results, but it prints no reference list, so it
seeds no ingestion frontier; the bundles grow as the user files sources,
and the works the book cites in its text form its reference list.

## D21 — Arfken as second founding source; a fifth textbook-founded bundle (2026-10-14)

**Decision (user):** Arfken, Weber & Harris, *Mathematical Methods for
Physicists* (7th ed., 2013) is ingested as `arfken-2013` into the four D20
bundles, each for its own chapters, and founds with Riley et al. a fifth
bundle, `orthogonal-polynomials-and-quadrature` (orthogonal polynomials,
the special functions numerical methods use, Gauss-type quadrature, and
their use as bases).

**How it relates to D12, D17 and D20:** the PDF is copied into each of the
five archives. In the four existing bundles it is an ordinary ingestion
through the merge path: shared claims gain a second citation, and where
the two books differ in statement or scope the difference is recorded as a
qualification or a `Contradictions` entry, never silently reconciled.

**Why:** a second independent textbook gives every standard claim visible
corroboration, fills gaps of the first (the discrete Fourier transform,
differential forms), and, unlike Riley, brings chapter reading lists that
seed each bundle's citation record. Orthogonal polynomials and quadrature
were first set aside with Riley's special functions; they are the bases and
quadratures of DG, spectral and multipole methods, so they earn a bundle.

## D22 — Plasma-propulsion bundle with a whole journal volume as context (2026-10-14)

**Decision (user):** a bundle `plasma-propulsion-simulation` for the
numerical modelling of electric and plasma thrusters, compiled from the
108 PDFs of `~/papers/mosaic/plasma-propulsion-simulation`, in chunks of
20 sources, each staged for the human's review and commit before the next
starts, with a per-chunk digest of contradictions and other issues in
`plasma-propulsion-simulation/INGESTION-ISSUES.md`.

**The archive's composition, recorded because it shapes the bundle:** 16
papers come from the propulsion and plasma literature; the other 92 are
the complete *Acta Astronautica* vol. 151 (October 2018), including the
issue's front matter and one paper misfiled under a Bird et al. (2009)
filename, of which three papers (an ion-thruster plume PIC
study, an ablative pulsed plasma thruster, a laser-ablation plasma
thruster) are in the domain and a few more touch electric propulsion or
plasma at a distance. Asked whether to ingest the core only, the user
chose all 108.

**How the scope is kept:** every file gets a Source page and its
reference list in the bibliography, so "is it ingested?" keeps its single
answer. Concept pages are created only for the plasma-propulsion domain;
an off-domain Acta paper presenting its own named method does not seed a
concept page, and its Source page says so. The core is ingested first so
the registry and the reading guide are built from it.

**Why:** the user's instruction is explicit and the compiler cannot judge
what the human means to do with the volume. The cost is a bibliography in
which much of the citation graph lies outside the domain; the ingestion
frontier derived from it must be read with that in mind, and the scope
rule keeps the concept layer from diluting.

## D23 — Two bundles split from the plasma-propulsion archive (2026-10-14)

**Decision (user):** of the 88 *Acta Astronautica* vol. 151 files left
after the plasma-propulsion core (D22), the papers whose link to plasma
propulsion is marginal were classified by topic, and two clusters became
bundles: `high-speed-aerothermodynamics` (10 papers: inlets, isolators,
waveriders, shock/boundary-layer interaction, aeroheating) and
`chemical-airbreathing-propulsion` (11 papers: combustion instability,
injectors, rotating detonation, scramjet and RBCC combustors, hybrid and
solid propellants). Three further clusters offered (spacecraft GNC,
space structures and materials, mission and trajectory design) were not
taken.

**How it relates to D12, D17 and D22:** the 21 PDFs are copied into the
new bundles' archives and fully ingested there; the plasma-propulsion
archive is Layer 1 and keeps them, so they also get Source-only pages in
`plasma-propulsion-simulation` (user's choice), keeping its worklist
complete. Every other Acta file (the GNC, structures and mission papers,
policy, history, communications, dosimetry, astronomy, and the issue's
front matter) is ingested in `plasma-propulsion-simulation` as a
Source-only page with its reference list; the five that touch plasma or
electric propulsion (electrospray constellation, ion-beam shepherd,
ionospheric drag control, plasma wind tunnel, electrodynamic tether) are
ingested there in full. One paper keeps one slug in every bundle.

**Why:** the user wants every file ingested, and the two clusters are
coherent technical fields with their own vocabulary that the user's CFD
work touches; folding them into plasma propulsion would have diluted its
registry, and a catch-all bundle would have had none.

## D24 — Lint exemption for out-of-scope Source pages (2026-10-15)

**Decision (user, option B of three):** `tools/lint_okf.py` does not
report the orphan warning for a page with `type: Source` and the tag
`context`. Concept pages are never exempt, whatever their tags.

**Why:** the orphan check exists to catch a concept page or an in-scope
Source page that lost its last incoming link. In
`plasma-propulsion-simulation` the scope rule (D22, D23) makes 82
Source-only pages uncitable by any concept page, so their 82 permanent
warnings buried the three meaningful ones (full ingestions waiting for a
second source). Links from `index.md`, `log.md` and `bibliography.md`
still do not count as incoming, by design. The rejected options were
keeping the warnings (signal masked) and a catalog concept page linking
every context source (games the check, violates the no-stub rule).

**Consequence:** `context` is a reserved tag with lint semantics. A
bundle that uses it declares the page out of scope; putting it on an
in-scope page would hide a genuine orphan. Tests in
`tests/test_lint_okf.py` cover the exemption and its limits.

## D25 — Fusion MHD simulation bundle (2026-10-16)

**Decision (user):** a bundle `fusion-mhd-simulation` for the numerical
simulation of magnetically confined fusion plasmas with MHD,
extended-MHD and hybrid kinetic-MHD models, compiled from the 50 PDFs of
`~/papers/mosaic/fusion-mhd-simulation` (the user's research
bibliography) in chunks of 20, each staged for the human's review and
commit before the next starts, with a per-chunk digest in
`fusion-mhd-simulation/INGESTION-ISSUES.md`. The user also asked to be
told when a paper fits another bundle, existing or new, better.

**The archive's composition, recorded because it shapes the bundle:**
every file is a fusion MHD paper (no context material as in D22).
About half are JOREK papers, so one code's conventions dominate. The
rest cover M3D-C1, NIMROD, CLT, BOUT++, the hybrid energetic-particle
codes and two 3D equilibrium codes. Many files are arXiv or HAL preprints;
the bundle law makes the version read explicit on every Source page.

**How the scope is kept:** chunk 1 holds the code, method, benchmark and
review papers, so that the registry and the reading guide are built from
them, and the application papers follow. Equations are compiled in SI with
$\mu_0$ explicit: most sources compute in normalized units and the
registry records how to quote their numbers. A paper that fits another
bundle is ingested here in full and listed in the issues file as a
candidate for a D17 copy. No copy is made without the human's decision.

**Why:** the user's research subject. The overlap with the CFD-numerics
bundles (stabilized finite elements, shock capturing, time integration,
field-aligned metrics) is real but secondary: these papers are about MHD
codes and the plasma physics they resolve, and splitting them across
bundles would dilute both.

## D26 — Chunked ingestion and its deep-lint cadence in the constitution (2026-10-16)

**Context:** two bundles (`plasma-propulsion-simulation`, D22; `fusion-mhd-simulation`,
D25) ingested archives of 108 and 50 sources in chunks of 20: parallel reader
subagents, one compile by the main session, one staged unit and one commit message
per chunk, a per-chunk digest in `INGESTION-ISSUES.md`. The rule lived only in bundle
law and contradicted the constitution's "one staged unit per ingested source". The
deep-lint cadence drifted with it: `fusion-mhd-simulation` ran its first deep lint
after 50 ingestions, against the constitution's "every 10", and wrote a 50-ingestion
cadence into its own law.

**Decision (user):** amend the constitution. Chunked ingestion is a declared mode: the
per-source protocol (steps 1–8) is unchanged, staging is per chunk, and the issues
digest is mandatory. The deep lint runs with every chunk, before staging, over at
least the pages the chunk created or updated, and over the whole bundle with the
chunk that completes the archive and every 50 ingestions.

**Why:** a 20-source chunk is reviewed as one unit, so it must be audited as one
unit; scoping the per-chunk audit to the pages the chunk touched keeps the original
intent of "every 10" (drift is caught while it is small) without re-reading the whole
bundle at every chunk. The fusion-mhd chunks 1 and 2 were staged without a deep lint;
the whole-bundle deep lint #1 that ran with chunk 3 covered their pages.

