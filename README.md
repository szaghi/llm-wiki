<div align="center">

# llm-wiki

#### *Scientific literature, compiled once by an LLM into a linted, cross-linked, contradiction-aware wiki*

### Knowledge bundles in the Open Knowledge Format, readable by people, editors and models alike

> Papers, books, theses, web pages and notes go in.
> A wiki comes out: one concept per page, one notation per domain, every claim cited,
> every disagreement between sources recorded instead of resolved by recency.
> No vector database, no embeddings, no retrieval lottery: the knowledge is **compiled once, navigated forever**.

[![Docs](https://img.shields.io/badge/docs-szaghi.github.io%2Fllm--wiki-blue)](https://szaghi.github.io/llm-wiki/)
[![OKF](https://img.shields.io/badge/OKF-v0.1-blue)](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
[![CI](https://github.com/szaghi/llm-wiki/actions/workflows/ci.yml/badge.svg)](https://github.com/szaghi/llm-wiki/actions/workflows/ci.yml)
[![Math](https://img.shields.io/badge/math-KaTeX-orange)](CLAUDE.md)
[![Compiler](https://img.shields.io/badge/compiler-Claude-8A2BE2)](CLAUDE.md)

**[Documentation](https://szaghi.github.io/llm-wiki/)** · **[Bundles](#bundles)** ·
**[Tutorial](https://szaghi.github.io/llm-wiki/manual/)** · **[Cookbook](https://szaghi.github.io/llm-wiki/manual/cookbook)** ·
**[Constitution](CLAUDE.md)** · **[Decision record](DECISIONS.md)**

</div>

## What this is

An implementation of the **LLM Wiki pattern**. Instead of feeding raw documents to a retrieval
pipeline at every question (stateless, forgetful, blind to contradictions between documents), an
LLM acts as a **stateful compiler**: it reads each source once, merges its claims into a web of
concept pages, records contradictions with attribution, and keeps a normative notation registry so
that hundreds of sources written in as many notations speak one mathematical language.

The format is the [Google Open Knowledge Format (OKF) v0.1][okf]: plain Markdown with YAML
frontmatter. This repository adds what a **scientific** knowledge base needs:

| Extension | What it does |
| --- | --- |
| KaTeX math | `$...$` / `$$...$$` everywhere; other delimiters are a lint error |
| Notation registry | one normative symbol table per bundle; concept pages must use it |
| Notation maps | every Source page records how the source's own symbols translate |
| `status: established \| hypothesis` | the kind of each claim: published literature, or a claim a source could still overturn |
| `## Contradictions` | disagreements between sources are content, attributed and cited; recency never wins |
| Verified identifiers | metadata from page 1 of each source, DOIs checked against Crossref |
| Complete citation record | every work any ingested source cites, with a `citedby` graph and a derived reading frontier |

## Bundles

A bundle is a self-contained wiki on one research domain. The table is generated from the files
by `tools/bundles.py`; the [documentation site](https://szaghi.github.io/llm-wiki/bundles/) renders
every bundle with an interactive page graph and a map of what the bundles share.

<!-- bundles:start -->
| Bundle | Domain | Sources | Concept pages | Cited works | Updated |
| --- | --- | ---: | ---: | ---: | --- |
| [Astrophysical simulation codes](astrophysical-simulation-codes/wiki/index.md) | How production codes for astrophysical and compressible flows are built: (M)HD frameworks (Athena/Athena++/AthenaK, PLUTO, Castro, Enzo, RAMSES-RT, GAMER, Cholla, IDEFIX, Quokka, GRaM-X), physics modules as numerical methods (self-gravity, sink particles, cooling, radiation moments, EOS, relativistic primitive recovery), code comparisons, and GPU and performance-portable frameworks. | 56 | 70 | 2522 | 2026-10-13 |
| [Chemical and air-breathing propulsion](chemical-airbreathing-propulsion/wiki/index.md) | Chemical rocket and air-breathing propulsion as physical and numerical problems: combustion instability and injector dynamics in liquid rocket engines, rotating and continuous detonation, scramjet and rocket-based combined-cycle combustors, flame holding and blowoff, hybrid and solid propellants, and combustion power systems. | 11 | 13 | 373 | 2026-10-15 |
| [Curvilinear and metric discretization](curvilinear-metric-discretization/wiki/index.md) | Vector and tensor calculus in general coordinates and its discretization: integral theorems, curvilinear coordinates, metric tensor and Christoffel symbols, covariant derivatives, metric identities, the geometric conservation law, free-stream preservation, finite differences and finite volumes on curvilinear and moving grids. | 5 | 36 | 142 | 2026-10-16 |
| [Divergence-free discretizations and AMR](div-free-amr/wiki/index.md) | Discrete divergence constraints (div B = 0 in MHD, incompressibility in CFD) across discretizations: staggered grids and constrained transport, projection and cleaning, mimetic and compatible operators, SBP, Whitney forms and DEC, with particular depth on high-order methods and 2:1 AMR refinement interfaces. | 123 | 55 | 3834 | 2026-10-13 |
| [Fourier analysis of schemes](fourier-analysis-of-schemes/wiki/index.md) | Fourier series and transforms and their use on discretizations: convergence, Gibbs phenomenon, Parseval, the discrete Fourier transform, von Neumann stability, modified wavenumber, numerical dispersion and dissipation, spectral resolution of finite-difference and finite-volume schemes. | 2 | 23 | 36 | 2026-10-14 |
| [Fusion MHD simulation](fusion-mhd-simulation/wiki/index.md) | Numerical simulation of magnetically confined fusion plasmas with MHD, extended-MHD and hybrid kinetic-MHD models: nonlinear codes (JOREK, M3D-C1, NIMROD, CLT, BOUT++, MEGA) and their discretizations, time integration and free-boundary/wall coupling; disruptions, vertical displacement events, runaway electrons, shattered pellet injection and impurity radiation; ELMs and ELM-free regimes; tearing, kink and infernal modes; energetic-particle-driven Alfvén modes; stellarator MHD and equilibria; code benchmarks and neural-operator surrogates. | 50 | 109 | 1572 | 2026-10-23 |
| [High-order shock-capturing schemes](high-order-capturing-schemes/wiki/index.md) | High-order shock-capturing schemes for hyperbolic conservation laws: ENO/WENO and their variants (mapped, Z, AO, TENO, CWENO), MP and PPM reconstruction, ADER and a posteriori limiting, positivity-preserving limiters, Riemann solvers, SSP and Runge-Kutta time stepping, boundary treatment (inverse Lax-Wendroff, immersed boundaries, cut cells), high-order AMR and MHD. | 144 | 124 | 3441 | 2026-10-16 |
| [High-speed aerothermodynamics](high-speed-aerothermodynamics/wiki/index.md) | Hypersonic and supersonic flow around and inside vehicles: inlets, isolators and bleed, waverider design, shock-wave/boundary-layer interaction, jets in supersonic crossflow, aerodynamic heating and its reduction, suborbital flight aerodynamics, and the uncertainty quantification of high-speed flow predictions. | 10 | 15 | 344 | 2026-10-15 |
| [Hyperbolic PDE theory](hyperbolic-pde-theory/wiki/index.md) | Continuum theory of partial differential equations with emphasis on hyperbolic systems: classification, characteristics, general and particular solutions, separation of variables and transform methods, well-posedness and uniqueness, weak and entropy solutions, Riemann problems, characteristic boundary conditions. | 2 | 23 | 27 | 2026-10-14 |
| [Linear and elliptic solvers](linear-elliptic-solvers/wiki/index.md) | Linear algebra for discretized PDEs and the solution of elliptic problems: vector spaces and operators, eigenproblems, Hermitian and Sturm-Liouville theory, direct and iterative solvers (relaxation, Krylov, multigrid, preconditioning), Poisson and Helmholtz problems with Green's functions and isolated boundary conditions. | 2 | 25 | 36 | 2026-10-14 |
| [ODE integration](ode-integration/wiki/index.md) | Numerical time integration of ODEs and of method-of-lines semi-discretizations of PDEs: Runge–Kutta theory (order conditions, B-series, stage order and order reduction, stability polynomials, strong stability preservation), implicit, DIRK and Rosenbrock methods, BDF and linear multistep methods, IMEX, additive and multirate methods, local time stepping, exponential integrators, stabilized and paired-explicit Runge–Kutta, relaxation and structure-preserving time stepping (entropy, energy, positivity, invariant domains, Patankar), splitting, deferred correction, ADER and multiderivative methods, asymptotic-preserving schemes, parallel-in-time integration, step-size control, solvers for implicit stages, integrator software and learned integrators. | 118 | 139 | 3771 | 2026-10-23 |
| [Orthogonal polynomials and quadrature](orthogonal-polynomials-and-quadrature/wiki/index.md) | Orthogonal polynomials and the special functions built on them, as the bases and quadratures of numerical methods: Legendre, Chebyshev, Jacobi, Hermite and Laguerre polynomials, associated Legendre functions and spherical harmonics, Bessel functions, three-term recurrences, Rodrigues formulae, Gauss, Gauss-Radau and Gauss-Lobatto quadrature, and their use in spectral, DG and multipole methods. | 3 | 20 | 89 | 2026-10-16 |
| [Plasma propulsion simulation](plasma-propulsion-simulation/wiki/index.md) | Numerical modelling of electric and plasma thrusters: Hall, gridded-ion, helicon, pulsed and laser-ablation thrusters; particle-in-cell, DSMC, hybrid and fluid models of their discharges and plumes; anomalous electron transport, oscillations and instabilities; verification, uncertainty quantification and calibration; GPU particle codes. The archive also holds the complete Acta Astronautica volume 151 (2018) as space-engineering context. | 108 | 44 | 4086 | 2026-10-15 |
| [Turbulence modelling and scale-resolving simulation](turbulence-modelling/wiki/index.md) | Turbulence modelling and simulation, 2017–2026: RANS closures (Spalart–Allmaras, k-ω SST, Reynolds-stress models) and laminar–turbulent transition models, large-eddy simulation (subgrid-scale models, explicit and implicit LES, filtering), wall models, hybrid RANS/LES (DES, PANS), data-driven and machine-learned closures (field inversion, symbolic regression, neural-network and reinforcement-learning models), high-order discretizations for scale-resolving simulation (DG, flux reconstruction, spectral elements, gas-kinetic schemes, kinetic-energy-preserving schemes), DNS of compressible and hypersonic boundary layers, immersed boundaries and mesh adaptation, turbulent combustion, and MHD, astrophysical and plasma turbulence. | 260 | 176 | 11784 | 2026-10-28 |
| [WENO, TENO and high-order compressible-flow schemes](weno-teno/wiki/index.md) | High-order discretizations of hyperbolic conservation laws and compressible flows, 2021–2026: nonlinear reconstruction (WENO-JS, Z, Z+, ZN, affine-invariant, alternative and multi-resolution WENO, Hermite WENO, WCNS, TENO, CWENO, THINC hybrids, gradient-based and learned reconstruction), central-upwind schemes and characteristic decomposition, discontinuous Galerkin and flux reconstruction (entropy-stable and kinetic-energy-preserving split forms, subcell and convex limiting, OEDG, filtering), bound preservation (geometric quasilinearization, optimal cell-average decomposition), well-balanced and asymptotic-preserving schemes, Active Flux, shock tracking and moving meshes, immersed boundaries, multiphase flows and the GPU and AMR solvers that implement them. | 204 | 224 | 5567 | 2026-10-24 |
<!-- bundles:end -->

## Use it

**Read it.** Browse the [rendered bundles](https://szaghi.github.io/llm-wiki/bundles/), or clone the
repository and open `<bundle>/wiki/` in any Markdown editor (it works as an Obsidian vault).

**Ask Claude.** Install the consultation skill as a Claude Code plugin, and Claude answers questions
in a bundle's domain from the wiki, citing pages and keeping hypotheses apart from literature:

```text
/plugin install llm-wiki --marketplace szaghi/llm-wiki
```

On Claude Code older than 2.1.275, run `/plugin marketplace add szaghi/llm-wiki`, then
`/plugin install llm-wiki@llm-wiki`. From a clone, `ln -s "$PWD/skills/llm-wiki" ~/.claude/skills/llm-wiki`
gives the same skill on the live repository.

**Build your own.** The constitution, the tools and the tutorial are domain-agnostic: clone the
repository, open Claude Code in it, and ask for a new bundle. The
[tutorial](https://szaghi.github.io/llm-wiki/manual/) walks through scaffolding, the first ingestion,
the citation record, quality control and publishing.

## Architecture

| Layer | Contents | Who writes it |
| --- | --- | --- |
| **Layer 0: law** | `CLAUDE.md` constitution, `DECISIONS.md` rationale, `tools/` | the human |
| **Layer 1: sources** | source archives, referenced in place, and `raw/` captures | nobody: immutable |
| **Layer 2: bundles** | the OKF wikis: concept pages, Source pages, notation registry, indexes, log, bibliography | the compiler (Claude) |

The compiler stages; the human reviews and commits. A source is ingested if and only if its Source
page exists, so progress is derived from the files and no queue can go stale; any new session
resumes from `CLAUDE.md` and `git log` alone.

```text
llm-wiki/
├── CLAUDE.md, DECISIONS.md     # the law and its rationale
├── tools/                      # linter, bibliography tools, bundle registry, site generator
├── skills/llm-wiki/            # the consultation skill (also a Claude Code plugin)
├── docs/                       # the VitePress documentation site
└── <bundle>/
    ├── bundle.toml             # title, summary, keywords: the bundle's card
    ├── CLAUDE.md               # bundle law: corpus location, domain notes
    ├── INGESTION-ISSUES.md     # per-chunk review digest, in bundles ingested in chunks
    ├── raw/                    # captures of sources without a durable home
    └── wiki/                   # the OKF bundle: index, log, notation, bibliography,
                                # definitions/ methods/ operators/ results/ properties/
                                # benchmarks/ software/ sources/
```

## Development

```bash
make dev        # Python virtual environment with the tools' dependencies
make check      # OKF lint of every bundle, bundle registry in sync
make test       # tool tests
make registry   # regenerate the bundle tables of this README and of the skill
make docs-dev   # documentation site with live reload (Node 20+)
make docs       # static build of the site into docs/.vitepress/dist
```

## Authors

**[Stefano Zaghi](https://github.com/szaghi)** · stefano.zaghi@gmail.com
> *Chief Yak Shaver & Curator of Unread PDFs*. CFD researcher who downloaded a folder of papers "for a quick literature check", realized he would need a second brain to hold them and, being constitutionally incapable of using an existing tool when a new repository could be founded, commissioned one. Now the proud owner of a wiki that knows his own conjectures are conjectures.

**[Claude](https://claude.ai)** (Anthropic)
> *Stateful Compiler & Recovering DOI Fabricator*. Reads every page of every scan (including the 1988 ones), translates dozens of notations into one, and has been caught by its own linter more than once.

## Lineage

The pattern follows Andrej Karpathy's *LLM Wiki* proposal; the on-disk format is Google's
[Open Knowledge Format v0.1][okf]. The scientific extensions (notation registry, claim kind,
contradiction protocol, verified identifiers, citation record) are this repository's own, codified
in [CLAUDE.md](CLAUDE.md) and argued for in [DECISIONS.md](DECISIONS.md).

[okf]: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
