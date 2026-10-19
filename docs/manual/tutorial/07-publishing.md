---
title: 7. Publishing
---

# 7. Publishing

A bundle is already usable as files in git. This chapter publishes it: the bundle list in the README and in the
consultation skill, the checks that guard it, and this documentation site.

## The bundle registry

Each bundle carries a small card, `<bundle>/bundle.toml`, with the only facts about the bundle that are written by
hand:

```toml
title = "High-order shock-capturing schemes"
summary = "High-order shock-capturing schemes for hyperbolic conservation laws: ENO/WENO and their variants ..."
corpus = "~/papers/mosaic/high-order-capturing-schemes"   # optional: the PDF archive tools/worklist.sh reads
keywords = ["WENO", "ENO", "TENO", "shock capturing", "Riemann solver", "..."]
```

Everything else (sources, concept pages by type, cited works, frontier, contested pages, hypotheses, date of the last
log entry) is counted from the wiki by `tools/bundles.py` whenever it runs, so it cannot fall behind the content:

```bash
python3 tools/bundles.py           # the bundle table, in Markdown
python3 tools/bundles.py --json    # the same, with every statistic, as JSON
make registry                      # rewrite the bundle lists in README.md and skills/llm-wiki/SKILL.md
```

`make registry` rewrites the text between the `<!-- bundles:start -->` and `<!-- bundles:end -->` markers, and the
skill's `description:` line, which is built from every bundle's `keywords`: that is what makes the skill trigger on
questions in your domain. Run it after every ingestion and after you add or remove a bundle.

## The checks

```bash
make check
```

runs the linter on every bundle and `tools/bundles.py --check`, which fails when the README or the skill is out of
date. The same checks, plus `ruff` and the test suite, run in continuous integration on every push
(`.github/workflows/ci.yml`).

## The site

The site you are reading is built from the repository by [VitePress](https://vitepress.dev). It needs Node 20 or
newer:

```bash
make docs-dev    # live preview at http://localhost:5173/llm-wiki/
make docs        # static build into docs/.vitepress/dist
```

Both first run `tools/site_sync.py`, which turns every bundle into site pages. It never modifies a bundle; it writes
generated files that are git-ignored:

| Generated | What it is |
| --- | --- |
| `docs/bundles/<bundle>/**` | the wiki pages, with bundle-root links (`/methods/x.md`) rewritten to site links (`/bundles/<bundle>/methods/x.md`) |
| `docs/bundles/<bundle>/graph.md` | the bundle's page graph |
| `docs/public/data/*.json` | graph data, the registry and the cross-bundle overlaps for the bundle map |
| `docs/public/bundles/<bundle>/bibliography.bib` | the citation record, for download |
| `docs/.vitepress/generated/bundles.json` | the bundle sidebars and menu |

Everything else under `docs/` is written by hand and committed: the guide, this tutorial, the cookbook, the
reference, and `docs/bundles/index.md` (the bundle cards and the bundle map).

`make docs` builds the site in parts (`docs/scripts/build.mjs`): one part for the documentation and the bundle list,
then one part per bundle, each a separate VitePress build with the same base, merged into `docs/.vitepress/dist`. One
build of every page needs memory in proportion to the whole corpus, which outgrew the 16 GB of a CI runner; a part
needs memory in proportion to one bundle. A link that leaves a part loads its target in full, and the site search of a
bundle's pages covers that bundle. `make docs-dev` still serves the whole site as one.

The math is rendered with KaTeX at build time. The wiki's math law is KaTeX syntax, so the build doubles as a check:
a formula KaTeX cannot parse is shown in red on its page. VitePress also fails the build on a dead link.

## Deploying to GitHub Pages

`.github/workflows/docs.yml` builds the site and deploys it to GitHub Pages on every push to `main`. In a fork:

1. in the repository settings, under *Pages*, set the source to **GitHub Actions**;
2. change the site address where it is written: `base` and the GitHub links in `docs/.vitepress/config.mts`, and
   `REPO_URL` and `SITE_URL` in `tools/bundles.py`;
3. push to `main`.

The bundles' sources are not published: Source pages show the DOI and mark the compiler's local copy as not
distributed.

## The whole cycle

Once set up, the routine after each ingestion is short:

1. Claude ingests, lints, regenerates the registry, and stages;
2. you review and commit;
3. you push; CI checks, and the site redeploys.

That is the end of the tutorial. The [cookbook](/manual/cookbook) has short recipes for everyday tasks, and the
[reference](/reference/page-types) has the details of every format and tool.
