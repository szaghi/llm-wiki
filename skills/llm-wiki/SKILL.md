---
name: llm-wiki
description: "Consult the compiled OKF knowledge bundles of the llm-wiki repository. TRIGGER whenever a question falls in a bundle's domain: astrophysical-simulation-codes (Athena++, AthenaK, PLUTO, Castro, Enzo, RAMSES, GAMER, Cholla, IDEFIX, Quokka, self-gravity, sink particles, Jeans criterion, radiative cooling, M1 radiation, equation of state, primitive recovery, GPU porting, Kokkos, code comparison); div-free-amr (divergence-free, div B = 0, incompressibility, constrained transport, flux-CT, projection, divergence cleaning, eight-wave, staggered grid, mimetic, compatible discretization, SBP, DEC, Whitney forms, block-structured AMR, prolongation, restriction, refluxing); high-order-capturing-schemes (WENO, ENO, TENO, CWENO, WENO-Z, WENO-AO, PPM, MP5, shock capturing, reconstruction, Riemann solver, HLL, HLLC, ADER, MOOD, positivity-preserving, SSP Runge-Kutta, inverse Lax-Wendroff, immersed boundary, cut cell, shock diffraction). Also trigger on \"llm-wiki\", \"second brain\", \"check the wiki\", \"what does the wiki say\". Read-only consultation from any directory; ingestion happens inside the repository under its CLAUDE.md."
---

# Consulting the llm-wiki bundles

The llm-wiki repository holds compiled knowledge bundles in the Open Knowledge
Format (OKF v0.1): Markdown pages with YAML frontmatter, one directory per
research domain. This skill reads them; it never writes them.

## Locate the repository

The repository root is two levels above this skill's directory. Resolve it
once per session:

```bash
readlink -f "${CLAUDE_SKILL_DIR}/../.."
```

This works for both install routes: a Claude Code plugin (a snapshot of the
repository in the plugin cache) and a symlink from `~/.claude/skills/llm-wiki`
to a clone (the live repository). Below, `<root>` is that path.

## The bundles

Generated from each bundle's `bundle.toml` and its files (`tools/bundles.py`);
the counts are those of the last regeneration.

<!-- bundles:start -->
| Bundle | Domain | Sources | Concept pages | Cited works | Updated |
| --- | --- | ---: | ---: | ---: | --- |
| Astrophysical simulation codes (`astrophysical-simulation-codes/wiki/`) | How production codes for astrophysical and compressible flows are built: (M)HD frameworks (Athena/Athena++/AthenaK, PLUTO, Castro, Enzo, RAMSES-RT, GAMER, Cholla, IDEFIX, Quokka, GRaM-X), physics modules as numerical methods (self-gravity, sink particles, cooling, radiation moments, EOS, relativistic primitive recovery), code comparisons, and GPU and performance-portable frameworks. | 43 | 67 | 2314 | 2026-10-13 |
| Divergence-free discretizations and AMR (`div-free-amr/wiki/`) | Discrete divergence constraints (div B = 0 in MHD, incompressibility in CFD) across discretizations: staggered grids and constrained transport, projection and cleaning, mimetic and compatible operators, SBP, Whitney forms and DEC, with particular depth on high-order methods and 2:1 AMR refinement interfaces. | 109 | 48 | 3711 | 2026-10-13 |
| High-order shock-capturing schemes (`high-order-capturing-schemes/wiki/`) | High-order shock-capturing schemes for hyperbolic conservation laws: ENO/WENO and their variants (mapped, Z, AO, TENO, CWENO), MP and PPM reconstruction, ADER and a posteriori limiting, positivity-preserving limiters, Riemann solvers, SSP and Runge-Kutta time stepping, boundary treatment (inverse Lax-Wendroff, immersed boundaries, cut cells), high-order AMR and MHD. | 124 | 120 | 3184 | 2026-10-13 |
<!-- bundles:end -->

## Protocol

1. **Enter at the catalog.** Read `<root>/<bundle>/wiki/index.md`, the
   curated reading guide, and follow its links: navigation is the query
   engine. For a symbol or a term, grep the bundle (frontmatter `tags` and
   `aliases`, math symbols such as `$P_D$`).
2. **Notation is registry-defined.** `<root>/<bundle>/wiki/notation.md` is
   normative; keep its symbols when quoting wiki math. Each Source page's
   `# Notation map` translates a paper's own symbols.
3. **Respect claim kind.** `status: established` is a published result;
   `status: hypothesis` is a claim a published source could still overturn.
   Report a hypothesis as such, never as literature fact.
4. **Report disagreements.** A `## Contradictions` section records sources
   that disagree, with both sides cited. Present both sides; do not pick a
   winner the page has not picked.
5. **Cite pages.** Cite the concept pages an answer rests on and, for
   provenance, their Source pages (`wiki/sources/*.md`, which carry the DOI
   or URL). A user without the repository can read the same page at
   `https://szaghi.github.io/llm-wiki/bundles/<bundle>/<path-without-.md>`.
6. **Coverage is partial.** Absence of a page is not absence of literature.
   Check the bundle's `wiki/log.md` and its bibliography (works cited but not
   ingested) before concluding; if the wiki lacks the answer, say so and
   label any answer from general knowledge as such.
7. **Bundles are independent.** Each bundle is self-contained; when a
   question spans bundles, answer from each and say which bundle says what.
8. **Read-only.** Never edit bundle content from a consultation. Gaps worth
   compiling become suggestions for an ingestion, run inside the repository
   under its `CLAUDE.md`.
