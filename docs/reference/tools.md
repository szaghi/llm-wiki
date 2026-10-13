---
title: Tools
---

# Tools

All tools live in `tools/` and run from the repository root. The Python tools need Python 3.11 or newer
(`tomllib`) and PyYAML. `make dev` installs both in `.venv`.

| Tool | Purpose |
| --- | --- |
| [`lint_okf.py`](#lint-okf-py) | deterministic lint of one bundle: OKF conformance plus repository law |
| [`bib_to_md.py`](#bib-to-md-py) | generate, check or query the bibliography view |
| [`bib_merge.py`](#bib-merge-py) | batched merger of reference-list fragments, with a duplicate sweep |
| [`worklist.sh`](#worklist-sh) | derived worklist: archived PDFs with no Source page |
| [`bundles.py`](#bundles-py) | the bundle registry and its generated tables |
| [`site_sync.py`](#site-sync-py) | generate the site's bundle pages and graph data |

## lint_okf.py

```bash
python3 tools/lint_okf.py <bundle>/wiki
```

The lint runs at every ingestion and must pass before a commit. It prints one line per finding, `[FAIL]` for errors
and `[warn]` for warnings, then a summary.

| Exit | Meaning |
| --- | --- |
| 0 | no errors (warnings allowed) |
| 1 | at least one error |
| 2 | the directory does not exist |

Checks on every concept document, that is every non-reserved `.md`:

| Check | Severity |
| --- | --- |
| kebab-case file name | error |
| YAML frontmatter present, closed and parseable | error |
| non-empty `type` | error |
| `type` agrees with the folder (taxonomy map) | error |
| folder outside the taxonomy map | warning |
| Source pages: non-empty `resource`; `source_kind` one of `paper`, `book`, `thesis`, `blog`, `notes`, `slides`, `code`, `report` | error |
| other pages: `status` is `established` or `hypothesis` | error |
| non-empty `title` and `description` | error |
| `timestamp` present and ISO 8601 | error |
| no `\(` or `\[` math delimiters; balanced `$` and `$$` (code spans and ```` ``` ```` or `~~~` fenced blocks excluded) | error |
| every link resolves (`http(s)://`, `doi:`, `mailto:` skipped; `#anchor` ignored) | error |

Checks on reserved files and indexes:

| Check | Severity |
| --- | --- |
| `index.md`, `log.md`, `bibliography.md` carry no frontmatter; the root `index.md` only `okf_version` | error |
| every link in a reserved file resolves | error |
| the math rules above, in reserved files too | error |
| each folder holding concept pages has an `index.md` | error |
| every page of the folder is listed in its index, exactly once | error |
| the index description equals the frontmatter `description` (trailing period ignored) | error |

Checks on the bibliography, when `bibliography.bib` or `bibliography.md` exists:

| Check | Severity |
| --- | --- |
| `bibliography.md` exists only with a `bibliography.bib` | error |
| the `.bib` parses and validates (see [Bibliography format](/reference/bibliography#validation)) | error |
| `bibliography.md` equals the freshly generated view | error |
| ingested sources whose reference list is not merged | warning |

Graph check:

| Check | Severity |
| --- | --- |
| orphan concept page: no incoming link from another page (the notation registry is exempt) | warning |

## bib_to_md.py

```bash
python3 tools/bib_to_md.py <bundle>/wiki             # (re)write bibliography.md
python3 tools/bib_to_md.py <bundle>/wiki --check     # exit 1 if bibliography.md is out of sync
python3 tools/bib_to_md.py <bundle>/wiki --pending   # ingested sources with no merged reference list
```

Every mode first parses and validates the `.bib`, and stops with exit 1 on a problem. `--pending` prints one slug per
line on standard output and the count on standard error.

| Exit | Meaning |
| --- | --- |
| 0 | written, in sync, or pending list printed |
| 1 | parse or validation error, or `--check` found the view out of sync |
| 2 | no arguments, or no `bibliography.bib` in the directory |

## bib_merge.py

```bash
python3 tools/bib_merge.py <bundle>/wiki --frags <dir> --resolutions <r.py> --report
python3 tools/bib_merge.py <bundle>/wiki --frags <dir> --resolutions <r.py> --write
python3 tools/bib_merge.py <bundle>/wiki --dupes
```

| Option | Meaning |
| --- | --- |
| `--frags <dir>` | directory holding the `frag-<slug>.bib` fragments |
| `--resolutions <r.py>` | Python module with the resolution tables (`ORDER` required) |
| `--report` | dry run: print the per-fragment plan and every flag |
| `--write` | apply the merge; refused while any flag is open |
| `--dupes` | whole-corpus cross-key duplicate sweep, after the final batch |

| Exit | Meaning |
| --- | --- |
| 0 | report printed, merge written, or sweep printed |
| 1 | `--write` refused because flags are open |
| 2 | no `bibliography.bib`, no `ORDER`, missing fragments, unknown `REPAIRS` keys, or bad arguments |

The workflow, the tables and the flags are described in [the batched merger](/reference/bibliography#the-batched-merger).

## worklist.sh

```bash
tools/worklist.sh <bundle>
```

The script lists the PDFs of the bundle's archive whose file name no Source page contains (Source pages name
their file in `local_file`). The list goes to standard output, and `pending: N / M` to standard error. It exits 2
without a bundle argument and 1 when the archive directory does not exist.

The archive is the `corpus` key of `<bundle>/bundle.toml` (a leading `~` is expanded). Without the key, the script
falls back to this repository's layout, one archive per bundle named after it: `~/papers/mosaic/<bundle>/` (D17).

## bundles.py

```bash
python3 tools/bundles.py             # the registry as a Markdown table
python3 tools/bundles.py --json      # the registry as JSON
python3 tools/bundles.py --write     # rewrite the generated regions
python3 tools/bundles.py --check     # exit 1 if they are stale
```

A bundle is a top-level directory that holds `bundle.toml` and `wiki/index.md`. The card carries the only facts
written by hand:

```toml
title = "High-order shock-capturing schemes"
summary = "One paragraph on the domain."
keywords = ["WENO", "TENO", "Riemann solver"]   # drive the consultation skill's trigger
corpus = "~/papers/mosaic/high-order-capturing-schemes"   # optional, read by worklist.sh
```

Everything else is derived from the wiki each time the tool runs:

| Field | Derived from |
| --- | --- |
| `sources` | Source pages |
| `concepts`, `by_type` | concept pages in the seven concept folders |
| `hypotheses` | concept pages with `status: hypothesis` |
| `contested` | concept pages with a `## Contradictions` section |
| `cited_works` | entries in `bibliography.bib` |
| `frontier` | entries that are cited but not ingested |
| `updated` | the newest `## YYYY-MM-DD` heading of `log.md` |

`--write` regenerates the text between `<!-- bundles:start -->` and `<!-- bundles:end -->` in `README.md` and in
`skills/llm-wiki/SKILL.md`. It also regenerates the skill's frontmatter `description:` line, which lists each bundle
with its keywords.

| Exit | Meaning |
| --- | --- |
| 0 | done, or in sync |
| 1 | `--check` found stale regions, or a `bundle.toml` is missing or invalid, or a marker is missing |
| 2 | unknown option |

## site_sync.py

```bash
python3 tools/site_sync.py [docs-dir]     # default: docs
```

The script writes the generated part of the documentation site. It never modifies a bundle.

| Output | Content |
| --- | --- |
| `bundles/<slug>/**.md` | the wiki pages, with bundle-root links (`/methods/x.md`) rewritten to `/bundles/<slug>/methods/x.md` outside code fences, plus site keys in the frontmatter (`bundle`, `bundleTitle`, `wikiPath`) |
| `bundles/<slug>/graph.md` | the page-graph page |
| `public/data/<slug>.graph.json` | nodes (pages: id, title, type, status, url) and links |
| `public/data/bundles.json` | the registry plus pairwise overlaps: shared cited works, sources ingested in both bundles, related concepts |
| `public/bundles/<slug>/bibliography.bib` | the citation record, for download |
| `.vitepress/generated/bundles.json` | the bundle sidebars and the navigation menu |

All of these are git-ignored. Overlaps are matched as follows:

* cited works: by DOI, otherwise by normalized title and year;
* sources: by `resource`;
* concepts: by file name, title or alias. Alias matches can be loose, so the site shows the name each pair matched on.

## Makefile

| Target | Runs |
| --- | --- |
| `make dev` | creates `.venv` and installs the tools with their development extras (`pip install -e ".[dev]"`) |
| `make test` | `pytest` |
| `make lint` | `ruff check` and `ruff format --check` (read-only) |
| `make fmt` | `ruff check --fix` and `ruff format` (rewrites files) |
| `make check` | `lint_okf.py` on every bundle, plus `bundles.py --check` |
| `make registry` | `bundles.py --write` |
| `make docs` | `site_sync.py`, then the VitePress build |
| `make docs-dev` | `site_sync.py`, then the VitePress dev server |
| `make clean` | removes build artefacts and caches |

CI runs ruff, pytest, the lint of every bundle and the registry check on every push (`ci.yml`). It builds the site and
deploys it to GitHub Pages on pushes to `main` (`docs.yml`).
