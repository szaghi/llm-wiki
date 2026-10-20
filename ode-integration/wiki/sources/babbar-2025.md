---
type: Source
title: "Babbar & Chandrashekar (2025) — Lax-Wendroff flux reconstruction on adaptive curvilinear meshes with error based time stepping for hyperbolic conservation laws"
description: "Extends Lax–Wendroff flux reconstruction to curvilinear and adaptively refined meshes with a free-stream preservation proof, and gives a single-stage method an embedded error estimate, by truncating the time-average flux one order lower, that drives a PID step-size controller."
resource: "doi:10.1016/j.jcp.2024.113622"
source_kind: paper
authors: [Babbar A., Chandrashekar P.]
year: 2025
venue: "J. Comput. Phys. 522:113622"
local_file: "/home/stefano/papers/mosaic/ode-integration/2025_Crossref_Journal_of_Computational_Physics_Babbar_Lax-Wendroff_flux_reconstruction_on_adaptive_curvilinear_mes.pdf"
tags: [lax-wendroff, step-size-control, positivity, hyperbolic-conservation-laws, software]
timestamp: 2026-10-20T10:00:00Z
---

# Summary

[Lax–Wendroff flux reconstruction](/methods/lax-wendroff-flux-reconstruction.md)
(LWFR) is a single-stage, quadrature-free scheme of order $N+1$ for
hyperbolic conservation laws. A Taylor expansion in time, with time
derivatives traded for space derivatives through the PDE, gives a
time-average flux. The approximate Lax–Wendroff procedure computes it
without Jacobians, and the solution advances in one update. The paper
extends the LWFR of [Babbar et al. (2022)](/sources/babbar-2022.md) in three
directions.

First, curvilinear body-fitted meshes, through contravariant fluxes. LWFR
is proved free-stream preserving under the discrete metric identities of
Kopriva, which hold in 2-D when the reference map has degree at most $N$.
Second, dynamically adapted non-conforming meshes with hanging nodes, through
the mortar element method and conservative transfer of $Ju$. Third,
error-based [step-size control](/methods/step-size-control.md) for a
single-stage method. An embedded lower-order solution comes from dropping
the interface terms and truncating the Taylor series of the time-average
flux one term earlier. This is the single-stage analogue of an
[embedded Runge–Kutta pair](/methods/embedded-runge-kutta-pair.md), and it
needs no extra inter-element communication. The difference of the two
element-local updates feeds the weighted RMS norm and PID controller of
Ranocha et al. Steps are rejected on a large error and on loss of
admissibility. The subcell blending limiter with provable admissibility
preservation in means ([positivity preservation](/properties/positivity-preservation.md))
is re-derived for GLL points and curved meshes.

The code TrixiLW.jl uses [Trixi.jl](/software/trixi-jl.md) as a library.
Tests on 2-D Euler include a Mach 2000 jet (automatic CFL ramp from about
$10^{-3}$ to $10^{-1}$), the [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md),
the [double Mach reflection](/benchmarks/double-mach-reflection.md), a
forward-facing step, free-stream tests, a rotating Couette flow and an
[isentropic vortex](/benchmarks/isentropic-vortex.md) on curved meshes (order
4 at $N=3$), a Mach 3 cylinder, a Mach 4 blunt body and a transonic NACA0012.
On curved meshes error-based stepping needs 1.51 to 2.08 times fewer steps
than the best hand-tuned CFL. It is the only method that finishes the
blunt-body run. The estimate costs about 4 %. The authors call this the
first error-based time stepping for a single-stage evolution method; the
[ADER](/methods/ader-time-integration.md) literature is the obvious place to
test that claim *(compiler remark, not in the source)*. The mesh uses one global step; [local time stepping](/methods/local-time-stepping.md)
is not used.

# Version read

arXiv:2402.11926v4 [math.NA], 25 September 2024, header "A PREPRINT -
SEPTEMBER 26, 2024", 39 pages (main text pp. 1–29, appendices pp. 29–37,
references pp. 37–39), all read. This is the arXiv preprint, not the JCP
version of record (522:113622), although the archive filename says
"Crossref_Journal_of_Computational_Physics". Title and authors match the
published version. The file prints no DOI. Section, equation and figure
numbers on this page are those of arXiv v4.

# Key claims

Registry notation: $h$ is the time step (source $\Delta t$), $h_n$ the step
of level $n$, $\mathrm{atol}$, $\mathrm{rtol}$ the tolerances (source
$\tau_a$, $\tau_r$), $\beta_1,\beta_2,\beta_3$ the PID exponents and
$k=\min(p,\hat p)+1$ with main and embedded orders $p$, $\hat p$ (source
$q$, $\hat q$). The PDE unknown $u$, the physical flux $f$, the degree $N$,
the time-average contravariant flux $\tilde F$ and solution $U$, and the
metric terms $J$, $Ja^i$ are page-local (see Notation map).

1. LWFR is a single-stage, quadrature-free scheme of formal order $N+1$:
   $u^{n+1}_{e,p}=u^n_{e,p}-\frac{h}{J_{e,p}}\nabla_\xi\cdot\tilde F_e(\xi_p)$,
   with $\tilde F=\sum_{k=0}^N\frac{h^k}{(k+1)!}\partial_t^k\tilde f$ the
   time-average contravariant flux (§3.2, Eqs. (23)–(28)). **Derived**
2. LWFR on curvilinear grids is conservative: multiplying (28) by
   $J_{e,p}w_p$ and summing updates the element mean through numerical
   fluxes only (Eq. (29); Appendix B, Eq. (93)). **Proved**
3. Free-stream preservation: if the discrete metric identity
   $\sum_i\partial_{\xi^i}I_N(Ja^i)=0$ (34)/(36) holds and the mesh is well
   constructed (Def. 3, Eq. (37)), LWFR preserves a constant state exactly.
   All time derivatives vanish, $\tilde F^\delta=\tilde f^\delta(c)$ and
   $U=c$ (Eqs. (38)–(40)). The required identities are those of FR/DG [26]
   (§3.3). **Proved**
4. In 2-D the metric identities hold if the reference map is interpolated
   by a degree-$N$ polynomial before the metric terms are computed; the
   curl-form choices of [26] matter only in 3-D (§3.3). **Stated**
5. The D2 dissipation, with the Rusanov jump computed from $U$ instead of
   $u^n$ (Eqs. (26)–(27)), reduces to upwinding for constant advection and
   raises the Fourier CFL limit; it was introduced in [3] (§3.2). **Stated**
   (cited from [3])
6. Refinement (interpolation of $\tilde u=Ju$, Eq. (50)) and coarsening
   ($L^2$ projection of $\tilde u$, Eqs. (51)–(53)) preserve the element
   integral. Transfer must act on the transformed solution, not the
   physical one (§4.1). **Proved**
7. The mortar element method, with $\tilde F^\delta\cdot\hat n$, $U$ and $u$
   interpolated to the mortars and the mortar fluxes $L^2$-projected back
   (59), conserves the total flux over a non-conforming face (§4.2.3).
   **Proved**
8. Free-stream preservation also holds on non-conforming 2-D AMR meshes,
   since $(I_N)_{e_L}(Ja^i)=(I_N)_{e_R}(Ja^i)$ in 2-D. In 3-D recomputing
   metric terms from interpolated reference maps can break it (Remark 3.1).
   **Derived** (2-D); **Stated** (3-D)
9. AMR creates non-solution points (mortar values, child means) where
   admissibility can fail. The remedy is extra Zhang–Shu scaling of these
   values toward the admissible parent mean (Remark 3.2). **Stated**
10. Fourier stability analysis applies only to uniform Cartesian grids, so
    the wave-speed CFL formula (60)/(66) does not guarantee $L^2$ stability
    on curvilinear grids and needs per-problem tuning (§5, §7). **Stated**
11. Embedded estimate: the main solution is the element-local update (63)
    with the interface terms $\mathcal C_{e,p}$ dropped and the full
    time-average flux ($k=0,\dots,N$). The embedded solution (65) uses the
    flux truncated at $k=0,\dots,N-1$ (64), "one order of accuracy lower".
    No extra inter-element communication is needed (§5.2, Algorithm 1).
    **Derived** (the order of the estimate is asserted, not proved)
12. The error is the weighted RMS norm of Ranocha et al. (62), normalized
    with $\max\{|u^{n+1}|,|\hat u^{n+1}|\}$, and the step is set by the PID
    controller (61) with limiter $\kappa(x)=1+\tan^{-1}(x-1)$ and
    $k=\min(p,\hat p)+1$. A step is accepted iff the step ratio is at least
    $0.9^2$ and no inadmissible state is detected; otherwise it is redone
    with the new step (§5.1–5.2, Algorithm 3). **Stated** (procedure from
    [37])
13. The exponents $\beta_1=0.6$, $\beta_2=-0.2$, $\beta_3=0$ (those of [37]
    for BS3(2)3$_F$) are used throughout; other parameter sets of [37] were
    "either superior or only slightly different", measured by step counts
    (§5.2). **Shown** (no table)
14. Tolerances affect the step only logarithmically;
    $\mathrm{atol}=\mathrm{rtol}=10^{-6}$ "worked reasonably for all tests
    with shocks", and larger tolerances helped some problems (§5). **Shown**
15. Novelty: "This is the first time error-based time stepping has been
    introduced for a single stage evolution method for solving time
    dependent equations" (§7). **Stated**
16. Mach 2000 jet from a cold start: error-based stepping automatically uses
    an effective $C_{\mathrm{CFL}}\sim10^{-3}$ at start-up, rising to about
    $10^{-1}$, which a CFL-based run would need to program by hand
    (§6.1.1, Fig. 5b, $N=4$, $512^2$ elements). **Shown**
17. Optimal order on curved meshes: rotating Couette flow and isentropic
    vortex on a sine-distorted periodic mesh, $N=3$, $L^2$ errors decay as
    $O(M^{-4})$ in the element count per direction over $16^2$–$256^2$
    elements (§6.2.2–6.2.3, Figs. 10b, 11b). These convergence tests use
    CFL-based stepping. **Shown**
18. Free-stream preservation is verified numerically for $N=6$ at $t=10$ on
    a mesh with curved boundaries and on a non-conforming, everywhere-curved
    refined mesh (§6.2.1, Fig. 9). **Shown**
19. Step counts, error-based against the best constant $C_{\mathrm{CFL}}$
    (the largest without admissibility loss) (§6.3, Table 1):
    forward-facing step 5679021 (CFL) against 7633954 at tolE $=10^{-6}$
    (ratio 0.74) and 5598338 at $5\times10^{-6}$ (ratio 1.01); Mach 3
    cylinder 1601725 against 1057844 (1.51) and 768835 at $5\times10^{-6}$
    (2.08); NACA0012 7530003 against 4842326 (1.55). Blunt body: no
    constant CFL reached $t=10$ without admissibility loss; error-based
    finished in 30527 steps (29766 accepted, 761 rejected). **Shown**
20. The error estimate adds about 4 % to the cost, so step counts measure
    total cost (§6.3). **Shown** (asserted from runs; no timing table, no
    hardware)
21. Theorem 1: if the low- and high-order schemes share the interface flux,
    their element means coincide, and the blended scheme is admissibility
    preserving in means iff the low-order scheme is. If the blended
    interface flux keeps the low-order updates at the adjacent solution
    points admissible, the blended scheme is admissibility preserving in
    means (App. A.3, Thm. 1). **Proved**
22. Flux limiting by the convex combination $F\leftarrow\theta F+(1-\theta)f$,
    with $\theta$ from the concavity of each constraint (Eq. (87), Algorithm
    4), extends to corner points on curved meshes by splitting the subcell
    update into $d$ directional updates with weights summing to one (Eqs.
    (89)–(92)) (App. A.3.2). **Derived**
23. With GLL points and $g_2$ correction functions, $g_R'(\xi_N)=1/w_N$, so
    the interface flux enters the high- and low-order residuals with the
    same coefficient and needs no blending coefficient, unlike the
    Gauss–Legendre case of [4] (Remark 4). **Derived**
24. The subcell first-order finite-volume scheme with the normals of [18] is
    free-stream preserving under the metric identities (App. A.2.2).
    **Proved**
25. AMR savings in elements (adapted against uniform): KHI 13957 against
    262144; DMR up to 7793 against 327680; forward step peak 6700 against
    202752; cylinder peak 85000 against 574464; NACA0012 peak about 4200
    against 186368 (§6.1.2–6.2.6). **Shown**

# Printed slips

- §5.2, p. 17: "we redo the time step if $\widetilde{\Delta t}^{n+1}/\Delta t^n\ge0.9^2$
  or if admissibility is violated". The condition is inverted: §5.1 and
  Algorithm 3 accept iff the ratio is at least $0.9^2$.
- Eqs. (66)–(67): $\Delta t_n=\frac2{N+1}C_{\mathrm{CFL}}\min_{e,p}\big(\frac1{|J_{e,p}|}\sum_i\tilde\lambda^i_{e,p}\big)$
  is proportional to a minimum wave speed per length, a rate, not a time.
  The intended formula is presumably the inverse of the maximum (compare
  (60)). Reader's inference.
- p. 18: "$\{Ja^i\}$ are the contravariant vectors (2)"; Eq. (2) is the
  equation of state, (9)/(10) are meant.
- §6.1.1: "the standard wave speed estimate for time step approximation
  (67)"; (66) is meant.
- §4.2.1: "the refinement levels of those elements only differs by 2",
  against §4.3 and Fig. 3a (one level).
- §4.1.2: "To show that refinement maintains conservation, we sum the
  identity (52)"; the paragraph is about coarsening.
- §4.2.3: "Using the identities (58), the equations (58) become"; the
  identities are (53).
- Eq. (45): index range "$0\le i,j\le N$" for indices $p,q$.
- §5.1: "For $m$ being the degrees of freedom in $u$", but (62) sums to $M$.
- Appendix B, p. 37: "$g_L(-1)=g_R(1)=1$, $g_L(-1)=g_R(1)=0$"; the second
  pair should be $g_L(1)=g_R(-1)=0$.
- App. A.3.2, p. 36: "admissibility in means (Definition 30)"; Definition 5
  is meant. App. A.3.1: "$\{p_k,1\le1\le K\}$" for $1\le k\le K$.
- App. A.2.3, p. 34: threshold "$\mathbb T(N)=a\cdot10^{-c(N+1)^4}$",
  $a=\frac12$, $c=1.8$. Hennemann et al. [18] use the exponent
  $(N+1)^{1/4}$; with $(N+1)^4$ and $N=4$ the threshold would be
  $\frac12\cdot10^{-1125}$.
- §6.2.2, p. 24: the Couette velocity $(-\sin\theta,\cos\theta)$ has unit
  magnitude, inconsistent with Fig. 10a and with the printed pressure,
  which balances a swirl $v_\theta=\frac1{75}(r-\frac{16}r)$ (reader's
  inference).
- §6.2.1 mesh map: the $x$ component contains "$\cos(2\pi\frac{2y-3}3)$"
  with $y$ where $\eta$ is expected.
- §6.1.1: "$u_b=u_a$ if $y\in[-0.05,0.05]$, $u_j$ otherwise"; the jet
  should enter for $y\in[-0.05,0.05]$, so ambient and jet appear swapped.
- §6.2.6: 186368 $=728\cdot4^4$ uniform elements implies four refinement
  levels beyond the 728-element mesh, while base_level 1 and max_level 4
  give three (possible inconsistency).
- Ref. [21] (Al Jahdali et al.) has no venue and no year.

# Notation map

| Babbar & Chandrashekar (2025) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Delta t$, $\Delta t_n$ (also $\Delta t^n$), $\widetilde{\Delta t}_{n+1}$ | $h$, $h_n$, proposed $h_{n+1}$ | |
| $u$, $u^n_{e,p}$ | — | PDE unknown at solution point $p$ of element $e$, page-local |
| $f(u)=(f_1,\dots,f_d)$ | — | physical flux; **collides with the registry right-hand side $f(t,y)$** |
| $N$ | — | polynomial degree of the solution and of the reference map; formal order $N+1$ |
| $\Theta_e$, $\xi$, $\Omega_o=[-1,1]^d$ | — | reference map, coordinates, cell |
| **$J$**, $Ja^i$ | — | metric Jacobian determinant and contravariant metric terms; **$J$ collides with the Jacobian $\partial f/\partial y$** |
| $\tilde u=Ju$, $\tilde f^i$ | — | transformed solution and contravariant flux (tilde = transformed, not time-averaged) |
| $\tilde F$, $\tilde F^\delta_e$ | — | time-average contravariant flux ($k=0,\dots,N$) and its element-local interpolant; **collides with the elementary differential $F(\tau)$** |
| $U$ | — | time-average solution |
| $\widehat F^\delta_e$, $\widehat u^{n+1}_{\mathrm{loc}}$ | $\hat y_{n+1}$ (analogue) | truncated flux ($k=0,\dots,N-1$) and embedded local update |
| $u^{n+1}_{\mathrm{loc}}$ | $y_{n+1}$ (analogue) | element-local main update without interface terms $\mathcal C_{e,p}$ |
| $q$, $\hat q$ | $p$, $\hat p$ | main and embedded orders; **$q$ collides with the stage order** |
| $\tau_a$, $\tau_r$, tolE | $\mathrm{atol}$, $\mathrm{rtol}$ | tolE $=\tau_a=\tau_r$ in §6.3 |
| $w_{n+1}$ | $\mathrm{err}_{n+1}$ | weighted RMS error norm |
| **$\varepsilon_{n+1}=1/w_{n+1}$** | $\mathrm{err}_{n+1}^{-1}$ | inverse error, Ranocha et al. convention; **collides with the stiffness parameter $\varepsilon$** |
| $\beta_1,\beta_2,\beta_3$, $k$ | $\beta_1,\beta_2,\beta_3$, $k$ | agree; $h_{n+1}=\kappa(\varepsilon_{n+1}^{\beta_1/k}\varepsilon_n^{\beta_2/k}\varepsilon_{n-1}^{\beta_3/k})h_n$ |
| $\kappa(x)=1+\tan^{-1}(x-1)$ | — | step-ratio limiter |
| $\breve u$ | — | normalization state of (62): $\widehat u^{n+1}$ here (PETSc), $u^n$ in OrdinaryDiffEq.jl |
| **$M$** | — | degrees of freedom in (62); elements per direction in the convergence plots; **collides with the mass matrix $M$** |
| $C_s$, $\mathrm{CFL}(N)$, $C_{\mathrm{CFL}}$ | — | safety factor, Fourier-optimal CFL of [3], CFL coefficient of (66) and effective CFL (67) |
| $\alpha_e$, $\alpha_{e+1/2}$ | — | blending coefficients; **not Shu–Osher $\alpha_{ij}$** |
| $\mathcal U_{ad}$, $p_k$ | — | admissible set and its concave constraints; **$p_k$ is not the order $p$** |
| $\lambda_{S,i}$, $\sigma(u)$ | — | interface wave speed, spectral radius of the flux Jacobian; **$\sigma$ collides with the tree symmetry** |

# Reference list

The paper prints 55 references in numbered, alphabetical style. All are
merged complete into the [bibliography](/bibliography.md) with `citedby`
babbar-2025. Ref. [3] is [Babbar et al. (2022)](/sources/babbar-2022.md),
printed without volume. Refs. [2] and [4] print a ditto dash for the
preceding entry's authors; [4] prints only "2023" (a preprint). Ref. [10]
has the corporate author CANAERO (5th workshop on high-order CFD methods,
printed 2017) and is `cenaero-2018`. Ref. [21] ("R. A. Jahdali", i.e. Al Jahdali) has no venue and no year; by
title and authors it is the AIAA SciTech 2021 paper `aljahdali-2021`, with a note. Ref. [25] is undated
software and ref. [39] has no volume or pages. Trailing "bibtex: Key"
artefacts are dropped. No DOIs are printed.

# Pages created or updated

Chunk 5 (2026-10-20). This source is cited on:

* [ADER as a time integrator](/methods/ader-time-integration.md)
* [Double Mach reflection](/benchmarks/double-mach-reflection.md)
* [Embedded Runge–Kutta pairs and the FSAL property](/methods/embedded-runge-kutta-pair.md)
* [Flow past a cylinder (Schäfer–Turek)](/benchmarks/flow-past-cylinder.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)
* [Lax–Wendroff flux reconstruction (single-stage Taylor time stepping)](/methods/lax-wendroff-flux-reconstruction.md)
* [Local time stepping](/methods/local-time-stepping.md)
* [Positivity preservation in time integration](/properties/positivity-preservation.md)
* [Step-size control: error-based controllers, PID filters and CFL control](/methods/step-size-control.md)
* [Trixi.jl](/software/trixi-jl.md)
* [Von Neumann (Fourier) stability analysis of fully discrete schemes](/definitions/von-neumann-stability-analysis.md)
