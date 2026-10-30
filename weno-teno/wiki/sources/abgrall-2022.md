---
type: Source
title: "Abgrall et al. (2022) — Reinterpretation and extension of entropy correction terms for residual distribution and discontinuous Galerkin schemes: Application to structure preserving discretization"
description: "Recasts Abgrall's entropy correction term as the explicit minimum-norm solution of an equality-constrained quadratic problem, transfers it to SBP–SAT discontinuous Galerkin with a mass-weighted variant, and extends it to entropy inequalities, several constraints, kinetic-energy preservation and fully discrete deferred-correction schemes."
resource: "doi:10.1016/j.jcp.2022.110955"
source_kind: paper
authors: [Abgrall R., Öffner P., Ranocha H.]
year: 2022
venue: "J. Comput. Phys. 453:110955"
local_file: "/home/stefano/papers/mosaic/weno-teno/2022_Crossref_Journal_of_Computational_Physics_Abgrall_Reinterpretation_and_extension_of_entropy_correction_terms_f.pdf"
tags: [entropy-stable, entropy-correction, kinetic-energy-preserving, summation-by-parts, dg, residual-distribution]
timestamp: 2026-10-22T20:00:00Z
---

# Summary

Abgrall (2018) added to each degree of freedom of a residual distribution (RD)
scheme a correction $\alpha(w_\sigma-\bar w)$, proportional to the deviation of
the entropy variables from their element mean, chosen so that the sub-residuals
still sum to the element residual while their entropy-weighted sum equals the
numerical entropy flux. This paper reinterprets that
[entropy correction term](/methods/entropy-correction-term.md) as the explicit,
unique solution of an equality-constrained quadratic minimization: the smallest
correction, in a discrete norm, that keeps local conservation and enforces one
linear entropy constraint (Theorem 2.8, Proposition 2.10). It transfers the
correction to the [summation-by-parts](/operators/summation-by-parts-operator.md)
operator form of nodal [discontinuous Galerkin](/methods/discontinuous-galerkin.md),
where a mass-weighted variant is optimal in the $M$-norm and Abgrall's original
in the identity norm, and generalizes it to an entropy inequality (correct only
an element that produces entropy, Theorem 3.1), to several linear constraints
(a closed-form $2\times2$ system, Theorem 3.2) and to
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md), so
that entropy and kinetic energy are corrected together. Applied to the whole
space–time residual of a deferred-correction RD scheme, the correction gives a
fully discrete entropy-conservative scheme. An appendix casts entropy-stable
$p$-refinement and coarsening as convex optimization problems.

Tests use continuous-Galerkin RD ([solid-body rotation](/benchmarks/solid-body-rotation.md),
a [Burgers-type](/benchmarks/burgers-equation-tests.md) equation, radial
[Sod](/benchmarks/sod-and-lax-shock-tubes.md) and
[Shu–Osher](/benchmarks/shu-osher-problem.md) problems), nodal
[DGSEM](/methods/dgsem.md) and sixth-order SBP finite differences on the
inviscid [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md), with
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md) stepping. The corrections
control the entropy and the kinetic energy but do not keep central schemes
alive: they blow up from negative density or pressure, whereas
[flux differencing](/methods/flux-differencing.md) with
[entropy-conservative and kinetic-energy-preserving fluxes](/methods/entropy-conservative-flux.md)
runs much longer, and a [split form](/methods/split-convective-forms.md) of
Ducros type plus both corrections behaves like flux differencing. The authors
conclude that [entropy stability](/properties/entropy-stability.md) is "not the
holy grail", that [bound preservation](/properties/bound-preservation.md) is
needed alongside it, and that the correction avoids the equation-of-state
algebra of two-point fluxes. [Artificial viscosity](/methods/artificial-viscosity.md)
and modal filtering are cited as alternative routes.

# Version read

arXiv:1908.04556v4 [math.NA], stamped 5 Jan 2022 (title page "January 4,
2022"), the authors' preprint, not the JCP version of record; 39 pages (text,
appendix, references pp. 35–39), all read, display equations visually. The
file prints neither venue nor DOI; page-1 title and authors match Crossref.
Page, equation, section and theorem numbers cited here are those of arXiv v4.

# Key claims

Registry notation: the source's entropy pair $(U,F^j)$ is $(\eta,F_\eta^{(j)})$,
its surface flux $f^{\mathrm{num},j}$ is $h$, its DG degree $p$ is $N$, its
$\varrho$ is $\rho$ and $E_{kin}$ is $\kappa$; the DG correction vector
$\mathfrak r_i$, the RD correction $r^K_\sigma$, the amplitude $\alpha$ and the
entropy defect $\mathcal E$ are page-local (written $\mathfrak r_m$,
$\alpha_{\mathrm c}$ and $\Delta_\eta$ on the concept pages).

1. Abgrall's correction (Eqs. 12–13) added to every sub-residual makes the RD scheme locally conservative and entropy conservative, with $\alpha=0$ when $w$ is constant in the element (Thm. 2.1, Eqs. 14–15). **Proved**
2. The correction is "universally applicable": no restriction on grid, distribution of degrees of freedom or scheme (DG, CG, SUPG, FR); only the error behaviour of $\mathcal E$, controlled by quadrature, matters (§2.1, p. 7). **Stated**
3. Entropy-dissipative variants follow by adding jump or streamline diffusion to the correction (§2.1, p. 7). **Stated**
4. Correcting the whole space–time deferred-correction bracket (Eq. 19), not only the spatial residual, gives a fully discrete entropy-conservative RD scheme; correcting the spatial residual alone gives a semidiscretely entropy-conservative one (Remark 2.2), presented as the first fully discrete one of its kind (abstract). **Derived** (fully discrete conservation shown numerically, Figs. 3–4, 6)
5. In the SBP–SAT DG setting with diagonal $M$, the correction (26) enforces local conservation (23) and entropy conservation (24); if the denominator of $\alpha$ vanishes, the solution is constant in the element by Cauchy–Schwarz (§2.2, p. 11). **Derived**
6. Conservation (23) and entropy conservation (24) can contradict each other only for a solution constant in the element; with Tadmor entropy-conservative surface fluxes (Eqs. 27–28) they do not, since the DG scheme then reduces to an entropy-conservative finite-volume scheme (Remarks 2.5, 2.7, Eq. 29). **Proved**
7. Theorem 2.8: for $\mathcal E\ne0$ and non-constant $w$, (26) is the unique solution of $\min\tfrac12\lVert\mathfrak r\rVert_M^2$ subject to $1^\top M\mathfrak r_i=0$ and $w_i^\top M\mathfrak r_i=\mathcal E$ (Eq. 30), by the KKT system. **Proved**
8. Proposition 2.10: Abgrall's original (12) is the unique optimal correction in the identity norm (Eq. 31); its pointwise form (33) is optimal in the $M$-norm and the integral form (34) of (26) in the $M^{-1}$-norm; the two are related by $r^K_\sigma\simeq M\mathfrak r_i$ (Eq. 32) with opposite sign conventions (§2.2, p. 13). **Proved**
9. Both corrections are explicit: no optimization solver is needed, and the mass-weighted variant costs the same as Abgrall's (p. 14). **Stated**
10. Single-block finite differences and Fourier collocation are one-element RD/DG schemes, so corrections give only global conservation and a global entropy inequality, which do not imply convergence to the entropy solution: for Burgers on $[0,3]$ with $u_0=-1$ on $(1,2)$ and $+1$ elsewhere, the central scheme and its corrected version keep a stationary non-entropic solution because $\mathcal E=0$ (Example 2.12). **Derived**
11. Theorem 3.1: with the inequality constraint $w_i^\top M\mathfrak r_i\le\mathcal E$ (Eq. 35) the unique solution is $\mathfrak r=0$ if $\mathcal E>0$ and (26) if $\mathcal E\le0$: an element already entropy dissipative is left alone. **Proved**
12. Theorem 3.2: with two linear constraints ($\mathcal E$ and a second $\widetilde{\mathcal E}$) the unique minimum-$M$-norm correction is $\mathfrak r_i=\alpha\big(w_i-\frac{1^\top Mw_i}{1^\top M1}1\big)+\tilde\alpha\big(\tilde w_i-\frac{1^\top M\tilde w_i}{1^\top M1}1\big)$, with $(\alpha,\tilde\alpha)$ from an explicit $2\times2$ linear system (Eq. 37). **Proved**
13. Several entropies cannot in general be conserved together through DG surface fluxes, since for a scalar law and a fixed entropy the entropy-conservative flux is uniquely $[\![\psi]\!]/[\![w]\!]$; Osher's E-schemes satisfy all entropy inequalities but are at most first order (Remark 3.3). **Stated**
14. The kinetic-energy correction (Eq. 42) enforces the kinetic-energy balance (41) and local conservation and is the unique $M$-norm optimal correction (Prop. 3.5); with kinetic-energy-preserving surface fluxes (40) the two constraints do not contradict in a finite-volume setting (Remark 3.4). **Proved** (by reference to Thm. 2.8)
15. Entropy and kinetic energy can be corrected simultaneously through Theorem 3.2 with $\eta=-\rho s/(\gamma-1)$ (Remark 3.6). **Derived**
16. Entropy conservation or dissipation "is not the holy grail": a bad baseline scheme behaves badly even when forced to be entropy conservative or dissipative (§4, pp. 18–19; App. A.2). **Shown**
17. Rotation test (43), fourth-order Bernstein CG, SSPRK(5,4), CFL 0.4, 3582 triangles: the two weightings (12) and (34) give energy changes and $L_\infty$ errors that agree to eight to ten significant digits ($L_\infty$ $1.5323772081\times10^{-4}$ against $1.5323772103\times10^{-4}$) (§4.1, Table 1). **Shown**
18. Burgers-type test (44), third-order CG, SSPRK(3,3), CFL 0.1: entropy differences at $t=0.2$ are $1.68193\times10^{-15}$ (12) and $1.68224\times10^{-15}$ (34); the two weightings do not differ significantly for smooth solutions (§4.1). **Shown**
19. Radial Sod, DeC(2,2), B1, CFL 0.25: uncorrected CG with jump stabilization breaks down at $t\approx0.16$, the semidiscretely corrected scheme runs to $t=0.25$, and the two corrections are indistinguishable without zoom (Figs. 1–2). **Shown**
20. With wall boundaries and the fully discrete correction, the more dissipative psi baseline behaves better than Galerkin, which gives non-flat plateaus; semidiscrete and fully discrete Galerkin differ slightly near shocks; with MOOD positivity enforcement DeC(4,4), B3 works (Figs. 3–5). **Shown**
21. Taylor–Green vortex, nodal DG on LGL nodes, $N=5$, $16\times16$ elements, SSPRK(10,4): central DG blows up at $t\approx3.8$; the kinetic-energy correction removes the kinetic-energy growth before blow-up, the entropy correction keeps the entropy nearly constant, and correcting both with weighting (12) delays blow-up to $t\approx4.3$; flux-differencing DG stays stable until $t\approx35$ (§4.2.2, Fig. 7). **Shown**
22. The Ducros et al. split form (neither entropy stable nor kinetic-energy preserving) plus both corrections behaves like flux differencing with Ranocha's flux: entropy conserved, no blow-up up to $t=30$; the surface flux has no major influence once the corrections are applied (§4.2.2, Fig. 8). **Shown**
23. The blow-up of corrected classical DG is caused by negative nodal densities or pressures, after which neither the entropy variables nor the correction exist; splitting the volume terms prevents it (§4.2.2, p. 25; §6). **Shown**
24. Convergence test, $N=4$, $t=6$: central and corrected schemes have no significant error difference; at low resolution the mass-weighted correction (34) gives lower errors than (12); observed orders up to 6.38 exceed $N+1=5$, attributed possibly to nodal superconvergence (§4.3, Table 2). **Shown**
25. Entropy-conservative two-point fluxes built from Tadmor's condition (45) rely on calorically perfect gas structure; for temperature-dependent or tabulated $c_v$ the algebra is case-dependent, which the correction approach avoids (§5). **Stated**
26. Entropy-stable refinement (47) and coarsening (50) are convex problems with unique solutions; interpolation and $L^2$ projection produce spurious entropy ($3.566\times10^{-3}$ for refinement, $9.749\times10^{-2}$ and $7.767\times10^{-2}$ for coarsening), the optimized transfers do not, up to tolerance ($-3.980\times10^{-8}$, $2.497\times10^{-8}$, $-3.429\times10^{-7}$) (App. A.1, Fig. 9). **Shown**
27. Linear advection, nodal DG, 16 elements, $N=4$, closed Newton–Cotes (Boole) quadrature, SSPRK(10,4): the entropy change falls by $10^4$ when $\Delta t$ falls by 10, yet the solutions are highly oscillatory (App. A.2, Fig. 10). **Shown**
28. Sixth-order SBP finite differences, $100^2$ nodes, $\Delta t=\Delta x/8$, $t\in[0,30]$: the central scheme blows up at $t\approx23.50$, the kinetic-energy correction at about the same time, the entropy correction at $t\approx24.82$ and both at $t\approx25.46$; flux differencing with Pirozzoli's or Ranocha's flux survives the interval, and Ranocha's flux and the corrected central scheme conserve entropy nearly to machine accuracy (App. A.3, Fig. 11). **Shown**

# Printed slips

- p. 6, proof of Thm. 2.1: "$\sum_\sigma\alpha(w_\sigma-\bar w)=\alpha\sum_\sigma w_\sigma-\sum_\sigma\bar w=0$" drops the factor $\alpha$ on the second sum.
- p. 7, deferred correction: "there are $K$ corrections $k=0,\dots,M$" while the loop runs $k=1,\dots,K$; "$U^{n,r,(k)}$ is the $k$-th correction of the $r$-th substep" while the substeps are indexed by $l$; $K$ also denotes the element.
- p. 11, Remark 2.5: "such as in Example 2.5"; there is no Example 2.5.
- p. 12, Remark 2.7: "drop the EC constraint (23)"; (23) is the conservation constraint, the entropy constraint is (24). Thm. 2.8: "the the minimization problem".
- p. 19, Eq. (43): the "linear rotation equation" $\partial_tu+\partial_x(2\pi yu)+\partial_y(2\pi xu)=0$ has velocity $(2\pi y,2\pi x)$, whose streamlines are the hyperbolas $x^2-y^2=\text{const}$, not circles; a rotation needs opposite signs. *(compiler check, not in the sources: $\frac d{dt}(x^2-y^2)=0$ along the printed field.)*
- p. 20 and Table 1: "$\int U^2_{corr}(t)-\int U^2_0$" for the entropy $U=u^2/2$.
- p. 23, radial Shu–Osher: post-shock velocity printed $\sqrt{2.629\varrho_0}\,x/r$. The printed density 3.857143 and pressure $10.\bar3$ are the Rankine–Hugoniot states of a Mach 3 shock into $(\rho,p)=(1,1)$, $\gamma=1.4$, whose gas speed is $\frac{2c_0}{\gamma+1}(M-1/M)=2.62937$; the printed expression evaluates to 3.184. *(compiler check, not in the sources.)*
- pp. 24, 26, 31: the LGL quadrature is cited as "[11, Eq. 25.4.32]" in the text and "[11, Eq. 25.4.14]" in the Fig. 8 caption, the number App. A.2 uses for Boole's rule. Fig. 7 caption truncated ("with a Taylor-Green").
- p. 27, Table 2 caption: "initial condition (4.3)"; 4.3 is a section, not an equation.
- p. 27, §5: "$\varepsilon$ the specific heat" where $\varepsilon=c_vT$ is the specific internal energy; "$\mathcal R$ being Avogadro's number" where the gas constant is meant.
- p. 28, §6: "correction terms (given in (12) and (33), respectively)"; (33) is the pointwise rewrite of (12), and §4 compares (12) with (34).
- p. 31, App. A.1: "$\gamma$ has to be chosen with minimal absolute value"; the multiplier of (48)–(49) is $\lambda$.
- Ref. [4]: "Comp. Fluids 19.1-3 (2017)", the volume of the 1991 ref. [2]; no pages.

# Notation map

| Abgrall et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u$, $f^j$ | $u$, $f^{(j)}$ | agree |
| $U$, $F^j$ | $\eta$, $F^{(j)}_\eta$ | convex entropy and entropy flux; mathematical sign |
| $w=\partial_uU$ | $w$ | agrees |
| $\psi^j=w\cdot f^j-F^j$ | $\psi$ | agrees |
| $S=-\varrho s$, $v=\nabla_uS$, $g$ (§5) | $(\gamma-1)\eta$, $w$, $F_\eta$ | §5 switches notation and scaling; **$v$ is the velocity in the registry** |
| $f^{\mathrm{num},j}$, $F^{\mathrm{num},j}$ | $h$, kept | surface flux and numerical entropy flux |
| $f^{\mathrm{vol},j}$ | $f^{\mathrm{vol}}$ | agrees |
| $M$, $D_j$, $B$ | $M$, $D$, $B$ | SBP property $MD_j+D_j^\top M=R^\top BN_jR$ generalizes $Q+Q^\top=B$ |
| $R$, $N_j$ | kept | restriction to the boundary and normal multiplication; **$R$ is the eigenvector matrix and $N$ the DG degree in the registry** |
| $p$ (DG), $k$ (RD) | $N$ | polynomial degree; **$p$ also the pressure** |
| $K$, $\sigma$, $\#K$ | $K$, kept | element, degree of freedom, their number; **$K$ also counts DeC corrections** |
| $\Phi^K$, $\Phi^K_\sigma$, $r^K_\sigma$, $\mathfrak r_i$ | kept, $\mathfrak r_m$ for component $m$ | RD residuals, RD correction, DG correction (opposite sign conventions) |
| $\alpha$, $\tilde\alpha$, $\mathcal E$, $\widetilde{\mathcal E}$ | $\alpha_{\mathrm c}$, $\tilde\alpha_{\mathrm c}$, $\Delta_\eta$, $\tilde\Delta$ (page-local) | correction amplitudes and defects, written so on [entropy correction terms](/methods/entropy-correction-term.md); **$\alpha$ is the DG–FV blending coefficient in the registry and $\mathcal E$ the vortex strength** |
| $\varrho$, $v$, $p$, $\gamma$ | $\rho$, $v$, $p$, $\gamma$ | |
| $e$, $\epsilon$ ($\varepsilon$ in §5) | $E/\rho$, $e$ | **the source's $e$ is the specific total energy, the registry's $e$ the specific internal energy** |
| $E_{kin}=\tfrac12\varrho v^2$ | $\kappa$ | kinetic energy per unit volume |
| $\{\!\{\cdot\}\!\}$, $[\![\cdot]\!]$ | same | agree |
| $M$ (DeC), $\beta_l$, $\theta^l_r$, $\mathcal L^1$, $\mathcal L^2$ | kept | DeC subintervals and operators; **$M$ collides with the mass matrix, $\mathcal L$ with the semi-discrete operator** |
| $I_{f\leftarrow c}$, $M^f$, $M^c$ | kept | fine/coarse transfer and mass operators |

# Reference list

59 printed references in numbered style ([1]–[59], alphabetical by first
author), all parsed and merged complete into the
[bibliography](/bibliography.md) with `citedby` `abgrall-2022`. DOIs are
printed only for [17], [41], [43], [45] and [48]. [46] and [47] are the same
arXiv manuscript (2009.13139) printed twice, as preprint and as accepted paper,
and are folded into one entry (58 entries for 59 printed items); [4] carries a suspect volume and year
(Comput. Fluids "19.1-3 (2017)"); [53] is a conference talk and [15] the
NIST-JANAF web tables.

# Pages created or updated

Chunk 3 (2026-10-22), cited further in chunks 4–12 (2026-10-22/30). This source is cited on:

* [Artificial viscosity and spectral viscosity](/methods/artificial-viscosity.md)
* [Bound preservation](/properties/bound-preservation.md)
* [Burgers equation tests](/benchmarks/burgers-equation-tests.md)
* [Deferred correction (DeC) time integration](/methods/deferred-correction.md)
* [Discontinuous Galerkin method](/methods/discontinuous-galerkin.md)
* [Discontinuous Galerkin spectral element method (DGSEM)](/methods/dgsem.md)
* [Entropy correction terms](/methods/entropy-correction-term.md)
* [Entropy stability](/properties/entropy-stability.md)
* [Entropy-conservative and kinetic-energy-preserving two-point fluxes](/methods/entropy-conservative-flux.md)
* [Flux differencing and split-form DG](/methods/flux-differencing.md)
* [h- and hp-adaptation for DG](/methods/hp-adaptation.md)
* [Kinetic energy preservation](/properties/kinetic-energy-preservation.md)
* [MOOD a posteriori limiting](/methods/mood-a-posteriori-limiting.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [Solid-body rotation](/benchmarks/solid-body-rotation.md)
* [Split convective forms](/methods/split-convective-forms.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Summation-by-parts operator](/operators/summation-by-parts-operator.md)
* [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
