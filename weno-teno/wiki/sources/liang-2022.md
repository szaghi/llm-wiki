---
type: Source
title: "Liang et al. (2022) — A fifth-order low-dissipation discontinuity-resolving TENO scheme for compressible flow simulation"
description: "Improves TENO5-THINC with a parameter-free discontinuity detector built from the TENO stencil flags, which also catches steps located at a cell interface, and with a two-steepness tanh interpolation of the interface flux that replaces the cell-average-constrained THINC reconstruction."
resource: "doi:10.1016/j.jcp.2022.111465"
source_kind: paper
authors: [Liang T., Xiao F., Shyy W., Fu L.]
year: 2022
venue: "J. Comput. Phys. 467:111465"
local_file: "/home/stefano/papers/mosaic/weno-teno/2022_Crossref_Journal_of_Computational_Physics_Liang_A_fifth-order_low-dissipation_discontinuity-resolving_TENO_s.pdf"
tags: [teno, thinc, interface-capturing, low-dissipation, finite-difference, troubled-cell]
timestamp: 2026-10-23T10:00:00Z
---

# Summary

The paper revises [TENO-THINC](/methods/teno-thinc.md) (Takagi et al.). That scheme runs
fifth-order [TENO](/methods/targeted-eno.md) everywhere and switches to a
[THINC](/methods/thinc-reconstruction.md) jump reconstruction in the cells that a detector,
built from the binary TENO flags $\delta_k$, marks as discontinuous. The authors raise two
objections. The detector misses steps located at the interface $x_{i+1/2}$ and, reaching
three points downwind, misclassifies high-wavenumber content. THINC's cell-average constraint
still adds much [numerical dissipation](/definitions/numerical-dissipation.md) at a jump.

The paper makes three changes. First, an improved
[discontinuity detector](/definitions/troubled-cell-indicator.md) (Eq. 24). It reuses the
cell flag $\zeta_i$, drops the point $i+3$ from the original condition and adds a second
condition for interface-located steps, with no new parameters. Second, an interpolation-like
interface flux. It is not reconstructed under a cell-average constraint. It is a tanh
interpolant through $f_{i-1}$ and $f_{i+1}$, shifted so that it passes through $f_i$, and so
it is bounded by $f_{i-1}$ and $f_{i+1}$. Non-monotone triples fall back to the second-order
central flux, and near-flat ones to the first-order flux. Third, two steepness levels,
$\mathcal A=0.91$ and $\mathcal A=1.23$. The higher one is used where a stricter "and" version
of the detector also fires.

The evidence is numerical. Static detector tests and Gaussian-pulse advection come first; the
present scheme matches the linear fifth-order errors there. Then follow Euler benchmarks:
[Sod and Lax](/benchmarks/sod-and-lax-shock-tubes.md),
[interacting blast waves](/benchmarks/woodward-colella-blast-wave.md), the
[Shu–Osher problem](/benchmarks/shu-osher-problem.md), the
[double Mach reflection](/benchmarks/double-mach-reflection.md),
[2D Riemann problems](/benchmarks/two-dimensional-riemann-problems.md),
[shock–vortex interaction](/benchmarks/shock-vortex-interaction.md), the
[triple-point problem](/benchmarks/triple-point-problem.md), the
[implosion](/benchmarks/explosion-and-implosion-problems.md),
[Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md) and the
[Mach 80 and 2000 jets](/benchmarks/high-mach-astrophysical-jet.md). The comparators are
[WENO5-Z](/methods/weno-z.md), TENO5 and TENO5-THINC. All runs use
[characteristic decomposition](/methods/characteristic-decomposition.md) with Roe averages,
[Rusanov splitting](/methods/lax-friedrichs-flux.md) and
[SSP-RK3](/methods/ssp-runge-kutta.md). The implosion and Rayleigh–Taylor runs add
[symmetry preservation](/properties/symmetry-preservation.md) and the jets the
[positivity-preserving flux limiter](/methods/positivity-preserving-flux-limiter.md). The
introduction places the scheme among [mapped WENO](/methods/mapped-weno.md),
[WENO-Z+](/methods/weno-z-plus.md), [WENO-CU6](/methods/weno-cu6.md),
[CWENO](/methods/cweno.md), [adaptive TENO](/methods/adaptive-teno.md),
[hybrid](/methods/hybrid-weno.md) and [BVD](/definitions/boundary-variation-diminishing.md)
schemes. There is no theory, cost data or positivity analysis.

# Version read

Version of record (Elsevier typeset, JCP 467 (2022) 111465), 28 pages, all read. The DOI is
printed on page 1, and title, authors and venue match Crossref. The archive also holds a byte
copy of this file under the name of Li et al. 2024 (`2024_..._Li_A_family_of_TENOA-THINC-MOOD_...`),
a known archive defect recorded in the bundle law. Numbering is that of the version of
record.

# Key claims

Registry notation in TENO labelling: $S_0=\{i-1,i,i+1\}$, $S_1=\{i,i+1,i+2\}$ and
$S_2=\{i-2,i-1,i\}$, with $\tau_5=\lvert\beta_1-\beta_2\rvert$. The page-local symbols are
the cell flag $\zeta_i\in\{2,1,-1,0\}$ (as on the TENO-THINC page), the steepness
$\mathcal A$, and $f_{\mathrm m}=(f_{i-1}+f_{i+1})/2$ and $f_{\mathrm j}=(f_{i+1}-f_{i-1})/2$.

1. The TENO5-THINC detector (Eq. 18) cannot capture all sharp discontinuities in broadband flows. It misclassifies high-wavenumber fluctuations "due to the excessive use of downwind stencil points" (§3.1, Figs. 3–5). **Shown**
2. For the four model steps of Eqs. (22)–(23), whose jump lies at $x_{i+1/2}$, the TENO5 flags in cell $i=5$ are $\delta_{1,5}=0$ and $\delta_{2,5}=1$. So $\zeta_5=1$, and Eq. (18), which needs $\zeta_i=0$, does not detect them (§3.1, Tables 2–3). **Shown**
3. The improved detector (Eq. 24) flags cell $i$ when condition I or condition II holds. Condition I is Eq. (18) without $\zeta_{i+3}$. Condition II reads: some $\zeta_{i-2},\zeta_{i-1}\in\{1,2\}$, and $\zeta_i=1$, $\zeta_{i+1}=-1$, $\zeta_{i+2}\in\{-1,2\}$. It detects every case of Eqs. (22)–(23), which the paper calls "straightforward to verify" (§3.1). **Stated**
4. The improved detector adds no free parameters and uses only the $\delta_k$ that TENO already computes (§3.1, §5). **Stated**
5. On $\sin(10\pi x)$ (about 12 points per wavelength) and $\sin(24\pi x)$ (about 5), with 120 points on $[0,2]$, neither detector fires anywhere (Fig. 2). **Shown**
6. On the discontinuous static functions (c)–(e), the TENO5-THINC detector "has lots of misjudgments". The present detector identifies the discontinuities "with a substantially higher accuracy" (Figs. 3–5). **Shown**
7. For some sub-cell jump configurations, the THINC cell-average constraint (Eq. 20) puts the interface value far from the exact flux (§3.2, Fig. 6 (c)–(e)). **Shown** (schematic)
8. The interpolation-like flux (Eqs. 27, 31) is bounded by $f_{i-1}$ and $f_{i+1}$ because $\lvert\tanh\rvert<1$, and needs no further limiter, since tanh "does not produce any local extreme" (§3.2). **Stated** (it follows for monotone triples)
9. In the local coordinate $x_i=0$, $x_{i\pm1}=\pm2.5$, $x_{i+1/2}=1.25$, the tanh profile through $f_{i\pm1}$ with steepness $\beta_{\mathrm T}$ and a shift fixed by point interpolation of $f_i$ (Eqs. 29–30) gives (Eq. 31) $\hat f_{i+1/2}=f_{\mathrm m}+f_{\mathrm j}\dfrac{\tanh\mathcal A+(f_i-f_{\mathrm m})/f_{\mathrm j}}{1+\tanh\mathcal A\,(f_i-f_{\mathrm m})/f_{\mathrm j}}$, with $\mathcal A=1.25\beta_{\mathrm T}$ (§3.2). **Derived** *(compiler check, not in the sources: Eq. (31) agrees with Eqs. (29)–(30) evaluated directly, e.g. 0.72566 both ways for $f_{i-1}=0$, $f_i=0.3$, $f_{i+1}=1$, $\mathcal A=0.91$)*
10. The steepness is $\mathcal A=0.91$ where Eq. (24) holds and $\mathcal A=1.23$ where the stricter Eq. (32) also holds. Eq. (32) is Eq. (24) with "or" replaced by "and" among the neighbour flags and $\zeta_{i-3}$ dropped (§3.2). **Stated** (recommended values, used in all tests)
11. Where $(f_{i+1}-f_i)(f_i-f_{i-1})\le10^{-15}$, none of the §3.2 formulas is used, and the first-order flux $\hat f_{i+1/2}=f_i$ is taken "for better numerical robustness" (Eq. 33). Non-monotone triples (Eq. 25) use the central flux $(f_i+f_{i+1})/2$ (Eq. 26). **Stated** (see Printed slips on the precedence)
12. Gaussian-pulse advection ($u_0=e^{-300(x-0.5)^2}$, $N_x=80$–$1280$): the present scheme, TENO5 and the linear fifth-order scheme have identical errors, with observed $L_\infty$ orders 4.826, 4.955, 4.988 and 4.997. Neither the TENO nonlinearity nor the interpolation-like flux switches on in smooth regions (§4.1, Table 4). **Shown**
13. Sod ($N_x=100$, $t=0.2$) and Lax ($N_x=100$, $t=0.14$): sharper shocks and contacts and a more accurate rarefaction (§4.2, Figs. 7–8). **Shown**
14. Interacting blast waves ($N_x=400$, Roe flux with entropy fix): TENO5 needs $C_T=10^{-4}$ to run stably. The present scheme captures the shocks as sharply as WENO5-Z and TENO5 and "resolves the density peak slightly better" (§4.3, Fig. 9). **Shown**
15. Shu–Osher problem ($N_x=200$, $t=1.8$): similar to TENO5-THINC, and slightly better than WENO5-Z and TENO5 on the shocklets and high-wavenumber waves (§4.4, Fig. 10). **Shown**
16. Double Mach reflection at $360\times90$ and $512\times128$: the present scheme is "significantly better" than WENO5-Z, TENO5 and TENO5-THINC "and even better than" TENO6 and TENO8. The authors say it "substantially outperforms all other schemes in the literature" on the small structures near the Mach stems and the wall jet (§4.5, Figs. 11–12). **Shown** (the literature claim is **Stated**)
17. At $1024\times256$ the small disturbances that TENO5-THINC produces near the oblique shock disappear, and the vortical structures are the best resolved (§4.5, Figs. 13–14). **Shown**
18. The double-Mach result is "not very sensitive" to $\nu=0.2$, $0.4$, $0.6$ (§4.5, Fig. 15). **Shown**
19. 2D Riemann configurations 3 ($512^2$, $1024^2$) and 7 ($1024^2$): more instability and vortical structure than WENO5-Z, TENO5 and TENO5-THINC (§4.6, Figs. 16–18). **Shown**
20. Shock–vortex interaction ($300\times150$, $t=0.6$): all schemes agree with a WENO5-JS $2000\times1000$ reference, and the present one resolves the contact wave "without adding strong disturbances" (§4.7, Fig. 19). **Shown**
21. Triple point, implosion and Rayleigh–Taylor: more interfacial and small-scale structure and sharper shocks. Implosion and Rayleigh–Taylor keep "rigorous flow symmetry" with the symmetry-preserving technique of [51,52] (§4.8–4.10, Figs. 20–23). **Shown**
22. Mach 80 and Mach 2000 jets at $800\times400$, $\nu=0.35$, with the positivity-preserving flux limiter: all schemes are stable, and the present one resolves richer small-scale structures (§4.11, Figs. 24–25). **Shown** *(compiler check, not in the sources: with the printed jet state $(\rho,p)=(5,0.4127)$ and $\gamma=5/3$, $c=0.3709$, so $v=30$ and $v=800$ give $M=80.9$ and $M=2157$; the final times are not stated)*
23. The present scheme, TENO5-THINC and TENO5 have so little dissipation that they "may cause the so-called symmetry breaking issue … due to machine round-off errors" (§4). **Stated**
24. The results are "among the best in the published literature" and can serve as "a state-of-the-art reference", with no case-by-case parameter tuning (§5). **Stated**

# Printed slips

- Double Mach reflection: the §4.5 text gives "the final simulation time is t = 0.2", but the captions of Figs. 11–14 say "t = 2.0".
- Eq. (43), vortex temperature: printed $\tilde T=-\frac{(\gamma-1)\varepsilon^2e^{2a(1-\gamma^2)}}{4a\gamma}$, with $\gamma^2$ in the exponent, while $\tilde u,\tilde v$ carry $e^{a(1-\tau^2)}$. With $\gamma$ in the exponent $\tilde T$ is spatially uniform; by comparison with $\tilde u,\tilde v$ in the same Eq. (43), the exponent of a localized vortex is $2a(1-\tau^2)$.
- Eqs. (25)–(26) against Eq. (33): Eq. (33) excludes "all formulas … in this section" where $(f_{i+1}-f_i)(f_i-f_{i-1})\le\varepsilon$. Every non-monotone triple of Eq. (25) has a negative product. Read literally, the central flux (26) is never used, so the precedence is ambiguous as printed.
- Eq. (19) has an unbalanced parenthesis, "$f_++f_-(\tanh(\beta(X_i-d_i))$".
- §3.1 calls the finite-difference point values $f_i$ "the discrete cell-averaged value".
- §1: "Borgers et al. [14]" (Borges); "Hu and Adams [25]" for Hu, Wang & Adams; "gird cell".
- TENO6 and TENO8 are compared without a definition or a citation at the point of use.
- References: [6] prints "N.J. Von, R. Richtmyer" (von Neumann); [18] prints "P. Woodward" alone; [1] prints 2021 for Takagi et al. (the ingested [`takagi-2022`](/sources/takagi-2022.md)); [21] prints pages "1-27" for an article.

# Notation map

| Liang et al. 2022 | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $f_i$, $\hat f_{i+1/2}$, $h(x)$ | $f_i$, $\hat f_{i+1/2}$ | point-value flux reconstruction from the primitive $h$ |
| $S_0,S_1,S_2$ | $S_0,S_1,S_2$ in TENO labelling | **differs** from the registry default ($S_0$ most upwind): here $S_0$ central, $S_1$ downwind, $S_2$ upwind |
| $\hat f_{k,i+1/2}$ | $\hat f^{(k)}_{i+1/2}$ | candidate fluxes |
| $w_k$ (Eq. 6), $\omega_k$ | $\omega_k$ | |
| $d_k=(6,3,1)/10$ | $d_k$ | |
| $\beta_{k,r}$ | $\beta_k$ | $r=3$ |
| $\tau_K$, $\tau_5=\lvert\beta_{1,3}-\beta_{2,3}\rvert$ | $\tau_K$, $\tau_5$ | outer stencils in TENO labelling |
| $\gamma_k$, $\chi_k$, $\delta_k$, $C_T$, $C$, $q$ | same | $C=1$, $q=6$, $C_T=10^{-5}$; **collision**: $\gamma$ also the ratio of specific heats |
| $\varepsilon$ | $\epsilon$; $10^{-15}$ guard; vortex strength $\mathcal E$ | three meanings in the source |
| $\zeta_i$ | $\zeta_i$ (page-local, as on [TENO-THINC](/methods/teno-thinc.md)) | **collision** with the characteristic variables $\zeta$ of §10, a different family |
| $f_+$, $f_-$ | $f_{\mathrm m}$, $f_{\mathrm j}$ | THINC mean and half-jump (§10); **not** the split fluxes $f^\pm$ |
| $\beta$ (THINC, 1.6; present steepness) | $\beta_{\mathrm T}$ | **collision** with $\beta_k$ |
| $d_i$ | jump-centre shift | fixed by a cell average (THINC) or by point interpolation (present) |
| $\mathcal A$ | $\mathcal A$ | steepness 0.91 or 1.23 |
| $T,A,B,\alpha$ (Eq. 21) | — | THINC closed form; $A\ne\mathcal A$; **collision**: $\alpha$ is not a weight |
| $N$ | $N_x$, $N_x\times N_y$ | grid size |
| $u$ (velocity in §4) | $v$ | |

# Reference list

The paper prints 64 references, numbered [1]–[64]. All parse, and the list is merged complete
into the [bibliography](/bibliography.md) with `citedby` including `liang-2022`. [1] (Takagi et
al., printed year 2021, article 110899) is the ingested `takagi-2022`. [2], [3] and [45] have no
pages, and [24] and [49] have no volume. [6] has the garbled first author "N.J. Von"
(von Neumann). No item is unparseable.

# Pages created or updated

Chunk 4 (2026-10-23), cited further in chunks 5–7 (2026-10-23). This source is cited on:

* [Adaptive TENO (TENO-A, TENO-AA)](/methods/adaptive-teno.md)
* [Central WENO (CWENO)](/methods/cweno.md)
* [Characteristic decomposition](/methods/characteristic-decomposition.md)
* [Conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
* [Double Mach reflection](/benchmarks/double-mach-reflection.md)
* [High-Mach astrophysical jets](/benchmarks/high-mach-astrophysical-jet.md)
* [Hybrid central-WENO schemes](/methods/hybrid-weno.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [Mapped WENO](/methods/mapped-weno.md)
* [Numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
* [Positivity-preserving flux limiter (Hu–Adams–Shu)](/methods/positivity-preserving-flux-limiter.md)
* [Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md)
* [Roe approximate Riemann solver](/methods/roe-riemann-solver.md)
* [Shock–vortex interaction](/benchmarks/shock-vortex-interaction.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Symmetry preservation](/properties/symmetry-preservation.md)
* [Targeted ENO (TENO)](/methods/targeted-eno.md)
* [TENO-THINC](/methods/teno-thinc.md)
* [THINC reconstruction](/methods/thinc-reconstruction.md)
* [Triple-point problem](/benchmarks/triple-point-problem.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
* [Two-dimensional explosion and implosion problems](/benchmarks/explosion-and-implosion-problems.md)
* [Two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md)
* [WENO-CU6](/methods/weno-cu6.md)
* [WENO-Z weights](/methods/weno-z.md)
* [WENO-Z+ and WENO-Z+M](/methods/weno-z-plus.md)
* [Woodward–Colella interacting blast waves](/benchmarks/woodward-colella-blast-wave.md)
