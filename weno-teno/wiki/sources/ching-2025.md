---
type: Source
title: "Ching et al. (2025) — Positivity-preserving and entropy-bounded discontinuous Galerkin method for the chemically reacting, compressible Navier-Stokes equations"
description: "Extends a positivity-preserving, entropy-bounded DG method to multicomponent reacting Navier–Stokes flow: a Lax–Friedrichs-type penalty applied to the viscous flux alone with a separate HLLC inviscid flux, a split cell-average update with the entropy bound on the convective half only, curved elements and a gradient fix for zero concentrations."
resource: "doi:10.1016/j.jcp.2025.113746"
source_kind: paper
authors: [Ching E.J., Johnson R.F., Burrows S., Higgs J., Kercher A.D.]
year: 2025
venue: "J. Comput. Phys. 525:113746"
local_file: "/home/stefano/papers/mosaic/weno-teno/2025_Crossref_Journal_of_Computational_Physics_Ching_Positivity-preserving_and_entropy-bounded_discontinuous_Gale.pdf"
tags: [dg, positivity, bound-preserving, reacting-flows, navier-stokes, limiting]
timestamp: 2026-10-23T15:20:00Z
---

# Summary

The paper extends the authors' fully conservative, positivity-preserving and
entropy-bounded [discontinuous Galerkin](/methods/discontinuous-galerkin.md)
method for the reacting
[multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)
(their Parts I and II of 2024) to the multicomponent, chemically reacting,
compressible Navier–Stokes equations. The gases are thermally perfect (NASA
polynomials), with mixture-averaged species diffusion, Wilke viscosity and
Mathur conductivity. Strang
[operator splitting](/methods/operator-splitting.md) separates transport, advanced
by [SSP Runge–Kutta](/methods/ssp-runge-kutta.md), from the stiff chemistry, which
is unchanged from the inviscid papers. Only the transport step is analysed.

The core ingredient is Zhang's Lax–Friedrichs-type
[positivity-preserving viscous flux](/methods/positivity-preserving-navier-stokes-flux.md),
with penalty $\tfrac12a^\nu(u^+-u^-)$. Unlike Zhang and Du & Yang, the
paper applies it to the **viscous flux alone** and keeps a separate inviscid flux
(HLLC). Lemma 1 gives the multicomponent bound on $a^\nu$. The
forward-Euler cell-average update is split into a convective and a viscous half,
each with a doubled step. The convective half stays in an entropy-bounded set
(earlier work), the viscous half in the positivity set (Theorems 6 and 8, in 1D
and on curved multi-D elements with general positive quadrature, through an
[optimal cell-average decomposition](/methods/optimal-cell-average-decomposition.md)
of Lv–Ihme type). The minimum-entropy bound of
[entropy stability](/properties/entropy-stability.md) is enforced only on the
convective half, because the minimum entropy principle fails for Navier–Stokes
with heat conduction. Four sequential
[Zhang–Shu scalings](/methods/zhang-shu-scaling-limiter.md) (density, species,
temperature, entropy) enforce [bound preservation](/properties/bound-preservation.md)
at the nodes. The Johnson–Kercher modified flux interpolation, which limits
spurious pressure oscillations
([pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)),
adds one time-step condition. The default viscous flux is
[BR2](/methods/bassi-rebay-viscous-discretization.md); the Lax–Friedrichs-type
flux is a fallback after one step halving. At zero species concentration no
finite $a^\nu$ suffices, and a gradient scaling fixes it.

The tests are a 1D thermal-bubble advection–diffusion
([material-interface advection](/benchmarks/material-interface-advection.md)), a
1D H$_2$/O$_2$ premixed flame against Cantera, a 1D viscous N$_2$/He shock tube
(a multicomponent relative of the [Sod tube](/benchmarks/sod-and-lax-shock-tubes.md)),
a 2D viscous H$_2$–O$_2$–Ar
[detonation](/benchmarks/shock-induced-combustion.md) and a 3D reacting
[shock–mixing-layer interaction](/benchmarks/shock-mixing-layer-interaction.md).

# Version read

The archive file is the version of record (Elsevier typeset, J. Comput. Phys.
525:113746; received 28 June 2024, online 15 January 2025), 37 pages, all read:
§§1–6, Appendices A–B and references. Page 1 prints title, authors, venue and DOI
matching Crossref; there is no identity problem. The text extraction drops
calligraphic letters; the derivation after Eq. (4.17) was checked against the
extracted equation layout.

# Key claims

Registry notation. Page-local: $u=(\rho v,\rho e_{\mathrm t},C_1,\dots,C_{n_s})$
the state, with $\mathsf C_k$ the molar concentrations, $W_k$ the molar masses and $\rho=\sum_kW_k\mathsf C_k$;
$e^*=e-e_0$ the internal energy shifted by its value at $T=0$; $f^{\mathrm c}$,
$f^\nu$ the convective and viscous fluxes, $f^\nu_{\mathsf C_k}$ their
species components; $a^\nu_*$ the sufficient bound on $a^\nu$,
$a^\nu_T$ its temperature part; $\varpi_q,\varpi_L,\varpi_R$ the weights of
the cell-average decomposition; $\Delta t^*=2\Delta t$; $s_{\mathrm b}$ the local entropy
bound; $\theta_\nabla\in[0,1]$ the gradient-scaling factor; $V_i$ the corrected
diffusion velocity.

1. Conventional viscous fluxes (BR2, SIPG) do not guarantee positivity: the step that keeps it can be arbitrarily small. Zhang's Lax–Friedrichs-type viscous flux comes with a strictly positive bound on the step (§1). **Stated**
2. In multicomponent flow the diffusive operator acts directly on the species equations, so the viscous flux "can indeed be largely responsible for negative concentrations"; in monocomponent flow the mass equation has no diffusion (§1). **Stated**
3. Clipping negative concentrations "violates mass conservation and may pollute the solution with errors". In the 1D premixed flame, $N=1$ with clipping overpredicts the velocity and the OH and H$_2$O$_2$ mass fractions relative to Cantera; the proposed formulation agrees "much more closely" (§1, §5.2, Figs. 5.2–5.3). **Shown**
4. Operator splitting is limited to second order unless backward-in-time or complex-time substeps are allowed; the cited exponential schemes need "well-prepared" initial conditions (§1). **Stated** (cited)
5. Lemma 1: for $u\in G$ with all $\mathsf C_k>0$, $u\pm f^\nu\cdot n/a^\nu\in G$ for any unit $n$ if $a^\nu>a^\nu_*=\max\{\max_i\lvert f^\nu_{\mathsf C_k}\cdot n\rvert/\mathsf C_k,\ a^\nu_T\}$, where $a^\nu_T$ is the largest root of a quadratic in $\rho^2e^*$, Eq. (4.5). The condition is stated as sufficient (§4.1, Eqs. (4.4)–(4.8)). **Proved**
6. At $\mathsf C_k=0$ with $f^\nu_{\mathsf C_k}\cdot n\ne0$ no finite $a^\nu$ keeps $\mathsf C_k\pm f^\nu_{\mathsf C_k}\cdot n/a^\nu\ge0$, because the species molar flux is not proportional to $\mathsf C_k$ (Remark 2). With the definitions substituted the species bound is $\max_i\lvert V_i\cdot n\rvert$, which can blow up as $\mathsf C_k\to0$ (Remark 3, Eq. (4.10)). **Derived**
7. Without species diffusion the bound reduces to Zhang's monocomponent one (Remark 3). **Stated**
8. Combining the convective and diffusive fluxes, as Zhang and Du & Yang do, gives a different constraint on $a^\nu$. Separating them is what allows enforcing entropy only on the convective part and using HLLC (Remark 5, §1). **Stated**
9. In 1D with $N=0$, the viscous half-update is a convex combination under $\frac{\Delta t^*}{2\Delta x}\max_K(a^\nu_{K_L}+a^\nu_{K_R})\le1$ for any positive coefficients, even with zero concentrations (§4.2.1, Eq. (4.16)). **Proved**
10. Theorem 6 (1D, $N\ge1$): if the nodal and exterior states lie in $G$, the viscous half of the cell average lies in $G$ under $\Delta t^*/\Delta x\le\min\{\varpi_L/a^\nu_{K_L},\varpi_R/a^\nu_{K_R}\}$, with the bounds (4.24)–(4.25) on $a^\nu$ and $\varpi_L,\varpi_R>0$, $\varpi_q\ge0$ (4.22) (§4.2.2, Eq. (4.23)). **Proved**
11. The convective half stays in the entropy-bounded set under $\Delta t^*a/\Delta x\le\tfrac12\min\{\varpi_L,\varpi_R\}$ (4.21) in 1D, and under (4.36) in multi-D (§4.2.2, §4.4.3, from Parts I–II). **Stated** (proof in earlier work)
12. Theorem 8 (multi-D, curved elements, general positive quadrature): the viscous half lies in $G$ under $\Delta t^*/\lvert K\rvert\le\min_{f,l}\varpi_{f,l}/(a^\nu_{f,l}\,\mathsf w^\partial_{f,l})$, with $a^\nu_{f,l}$ above the bound at both traces (§4.4.3, Eqs. (4.39)–(4.40); $\mathsf w^\partial_{f,l}$ the surface weight times the surface Jacobian). **Proved**
13. With the modified flux interpolation, nodal sets containing the endpoints need no change in 1D; in multi-D an extra time-step condition through Lemma 14 is needed (§4.2.3, §4.4.4). **Derived**
14. Boundary conditions with penalty $\tfrac12a^\nu(u^+-u_\partial)$, $u_\partial\in G$, keep the viscous half admissible under (4.39) and the modified bound (4.44) (§4.5, App. A). **Derived**
15. On non-constant geometric Jacobians the Lax–Friedrichs-type viscous flux is "significantly more straightforward" than invariant-region-preserving inviscid fluxes: it satisfies positivity algebraically, whereas those rely on a Riemann problem (Remark 10). **Stated**
16. The constraints (4.36) and (4.39) are sufficient, not necessary. The adaptive procedure (BR2, then one halving of $\Delta t$, then the Lax–Friedrichs-type viscous flux) needs a smaller step or a flux switch in "typically no more than ten percent of time steps" (§4.6). **Stated** (from the authors' runs)
17. Gradient scaling by $\theta_\nabla$, Eqs. (4.46)–(4.50), guarantees non-negative species cell averages with $a^\nu$ set from $a^\nu_T$ alone, and the coefficient need not be recomputed, since the species bound scales by $\theta_\nabla$ (§4.7, Remark 13). **Derived**
18. A projection onto $N=0$ (density limiter with zero scaling) always restores non-negative concentrations, "foolproof but low-fidelity" (Remark 12). **Derived**
19. Gradient limiting is "extremely rare": it is applied only at the first time step of both Lax–Friedrichs 2D detonation runs, where otherwise $\Delta t$ "would need to be halved approximately thirty times" (§4.7, §5.4). **Shown**
20. Thermal bubble: optimal order $N+1$ for $N=1,2,3$ with both BR2 and the Lax–Friedrichs-type flux at fixed CFL 0.1, except on the coarse $N=1$ grids. Both limiters activate on $h$ and $h/2$ for every $N$; on $h/4$ with $N=1$ only the positivity limiter does (§5.1, Fig. 5.1). **Shown**
21. Viscous multicomponent shock tube: the entropy limiter damps large-scale pressure, temperature and entropy instabilities "significantly better" than the positivity limiter alone, whose instabilities are much larger than in monocomponent, calorically perfect shock tubes (§5.3, Figs. 5.5–5.6). **Shown**
22. Artificial viscosity alone, without limiters, gives negative concentrations and other instabilities (§5.3). **Stated** (results not shown)
23. In the 1D shock tube the Lax–Friedrichs-type flux gives a noticeably smaller temperature overshoot at the shock than BR2 (§5.3, Fig. 5.6). **Shown**
24. 2D detonation: BR2 on the $64h$ and $8h$ meshes resembles the Lax–Friedrichs-type solutions "but with much smaller nonphysical instabilities"; the Lax–Friedrichs-type $64h$ run has a large temperature undershoot near the walls (§5.4, Figs. 5.7–5.9). **Shown**
25. Curved quadratic elements give a stable solution "extremely similar" to the linear-mesh one (§5.4, Fig. 5.11). **Shown**
26. Without the entropy limiter the minimum entropy and temperature "oscillate considerably"; before $t=50$ μs the temperature approaches zero and the nonlinear solver of the reaction step stalls. With it the minimum entropy is roughly constant and the temperature stays near 300 K (§5.4, Fig. 5.12). **Shown**
27. The minimum entropy principle does not hold for Navier–Stokes unless the thermal diffusivity is zero (monocomponent, calorically perfect, cited); the authors "do not expect the conclusion to change" for multicomponent thermally perfect gases (§1). **Stated**
28. The residual-based artificial-viscosity term (3.10) vanishes on piecewise constants, so it does not change the cell averages (§3). **Derived**

The paper's admissible set is $G=\{\rho>0,\ \rho e^*>0,\ \mathsf C_k\ge0\}$ (Eq. (4.3)). The
entropy-bounded set is assumed convex even where the entropy constraint is not concave
($\mathsf C_k=0$); the paper states this and defends it by the lack of "discernible negative
effects" (§4).

# Printed slips

- **Remark 3, $b$:** printed $b=\rho\,q\cdot n+\rho\sum_iW_iC_ih_iV_i\cdot n$. *(Compiler check, not in the sources:)* substituting the viscous flux (2.6), whose energy component carries $-q_k$, into $b=\rho f^\nu_{\rho e_{\mathrm t}}\cdot n-\rho v\cdot(f^\nu_{\rho v}\cdot n)$ gives $b=\rho\sum_iW_iC_ih_iV_i\cdot n-\rho\,q\cdot n$ (the stress-work terms cancel by symmetry of $\tau$). Only $\lvert b\rvert$ enters the bound, so the monocomponent limit is unaffected.
- **§4.2.2, after Eq. (4.17):** the last line reads "$\sum_qw_qy_\kappa(x_q)-\theta_Ly_\kappa(x_L)+\theta_Ry_\kappa(x_R)$"; the preceding line has $-\theta_L\sum\cdots-\theta_R\sum\cdots$, so the last sign must be $-\theta_R$.
- **Appendix B, proof of Lemma 14:** $y-\alpha^{-1}\Delta y$ is expanded as "$(\rho v-\alpha\Delta(\rho v),\ \rho e_t-\alpha\Delta(\rho e_t),\ C_1-\alpha\Delta C_1,\dots)$", with $\alpha$ for $\alpha^{-1}$.
- **Appendix B, Eq. (B.3):** printed $\alpha^2Z(y-\alpha^{-1}\Delta y)=\rho^2u\,\alpha^2-\mathsf b\alpha+\mathsf g$. *(Compiler check, not in the sources:)* with $Z=\rho\,\rho e_{\mathrm t}-\tfrac12\lvert\rho v\rvert^2-\rho^2e_0$ (4.7) and $\mathsf b$, $\mathsf g$, $\mathsf M$ as defined after (B.2), the expansion is $\rho^2e^*\alpha^2+\mathsf b\alpha+\mathsf g$, the sign consistent with the root $\alpha_T=(-\mathsf b+\sqrt{\mathsf b^2-4\rho^2e^*\mathsf g})/(2\rho^2e^*)$ of (B.2). (B.2)–(B.3) also write $\rho^2u$ (unshifted internal energy) where (4.7) gives $\rho^2u^*$.
- **Lemma 14, end of proof:** the quantity named $\alpha_T$ in (B.1)–(B.2) is called $\alpha_0$.
- **§5.5, Eq. (5.6):** the temperature profile is printed "$\tfrac12\big((T_F+Y_O)+(T_F-T_O)\tanh(\cdots)\big)$"; the mass-fraction and velocity lines of the same equation have the form $\tfrac12\big((\cdot_F+\cdot_O)+(\cdot_F-\cdot_O)\tanh\big)$, so $T_F+T_O$ is meant.
- **§4.3:** the density-limiter threshold is $\varepsilon$ in the text and $\epsilon$ in the scaling factor.
- **App. A.3–A.4:** the state vector is printed "$C_i^+,\dots,C^+_{n_s}$"; A.5 sums over $j$ a summand indexed by $k$.
- Typo: "operating splitting" (§1).

# Notation map

| Ching et al. (2025) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $y=(\rho v,\rho e_t,C_1,\dots,C_{n_s})$ | $u$ | species carried as molar concentrations $\mathsf C_k$ (page-local, as on [multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)), not partial densities |
| $u$, $u_0$, $u^*=u-u_0$ | $e$, $e_0$, $e^*$ | **collision**: the source's $u$ is the specific internal energy, not the state; velocity is $v$ in both |
| $e_t$ | $E/\rho$ | specific total energy |
| $W_i$, $X_i$, $Y_i$ | $W_k$, mole fraction, $Y_k$ | §10 symbols |
| $s$, $s_b$, $\chi_\sigma=\rho s-\rho\sigma$ | $s$ (mixture), $s_{\mathrm b}$, $\chi_\sigma$ (page-local) | physical specific entropy bounded from below, not the mathematical entropy $\eta$ |
| $\mathcal G$, $\mathcal G_\sigma$, $\mathcal G_{s_b}$ | $G$, entropy-bounded sets (page-local) | positivity set and its entropy-constrained subsets |
| $\mathcal F=\mathcal F^c-\mathcal F^v$ | $f^{\mathrm c}-f^\nu$ (page-local) | convective minus viscous flux |
| $\mathcal F^{c\dagger}$ | $h$ (HLLC) | inviscid numerical flux |
| $\delta^v=\tfrac\beta2(y^+-y^-)$ | $\tfrac12a^\nu(u^+-u^-)$ | **collision**: $\beta$ is not a smoothness indicator; viscous-only coefficient, unlike the total-flux coefficient of Zhang and Du & Yang |
| $\beta^*$, $\beta_T$ | $a^\nu_*$, $a^\nu_T$ (page-local) | sufficient bound and its temperature part |
| $\lambda$ | $a$ | maximum wave speed |
| $p$ | $N$ | DG degree; **$p$ is the pressure in the registry** |
| $P$ | $p$ | pressure |
| $\kappa$, $\kappa_L$, $\kappa_R$, $\kappa^{(f)}$, $h$ | $K$ and its neighbours, $\Delta x$ | **collision**: $\kappa$ is the kinetic energy, $h$ the numerical flux in the registry |
| $\theta_q,\theta_L,\theta_R,\theta_{f,l}$ | $\varpi_q,\varpi_L,\varpi_R,\varpi_{f,l}$ (page-local) | cell-average decomposition weights; **$\theta$ is the Zhang–Shu factor in the registry** |
| $\omega^{(1)},\dots,\omega^{(4)}$ | $\theta$ | Zhang–Shu scalings of density, species, temperature, entropy |
| $\omega$ (§4.7) | $\theta_\nabla$ (page-local) | gradient scaling |
| $\omega_i$ (§2) | $\Omega_k$ | production rates; **the paper uses $\omega$ for three things** |
| $\nu^\partial_{f,l}$ | $\mathsf w^\partial_{f,l}$ (page-local) | surface weight times surface Jacobian; **not the CFL number $\nu$** |
| $\Delta t^*=2\Delta t$ | kept | step of each half-update |
| $j$ | $n$ (time level) | not a cell index |
| $\mu$, $\lambda_T$, $\tau$, $q$ | viscosity, conductivity, stress, heat flux | **$q$ is the weight exponent in the registry** |
| CFL $=\Delta t(2p+1)(\lvert v\rvert+c)/h$ | $\nu$ with factor $2N+1$ | DG-scaled CFL number |

# Reference list

The paper prints 60 references, numbered [1]–[60], merged complete into the
[bibliography](/bibliography.md) with `citedby` including `ching-2025`. Ref. [17]
(Du & Yang, JCP 469:111548) is the ingested [Du & Yang (2022)](/sources/du-2022-b.md)
and ref. [25] (Dzanic & Witherden, JCP 468:111501) the ingested
[Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md); both are keyed to those
Source pages. Ref. [50] (Trojak & Dzanic, arXiv:2308.02426) is the preprint of the
ingested [Trojak & Dzanic (2024)](/sources/trojak-2024.md) and stays a distinct
entry, as does ref. [46] (Wu, arXiv 2021). Refs. [43] (ICASE report, 1996) and [44]
(AIAA J., 1998) are the report and journal versions of Atkins & Shu's quadrature-free
DG and are kept as two entries. Refs. [10], [11] and [24] print article numbers
without volumes; [1] prints only a title, a DOI and the year; [57] has no title;
[28], [29], [37], [43] and [59] are reports or manuals. No item is unparseable.

# Pages created or updated

Chunk 9 (2026-10-23). This source is cited on:

* [Bassi–Rebay viscous discretizations (BR1, BR2)](/methods/bassi-rebay-viscous-discretization.md)
* [Bound preservation](/properties/bound-preservation.md)
* [Discontinuous Galerkin method](/methods/discontinuous-galerkin.md)
* [Entropy stability](/properties/entropy-stability.md)
* [Material-interface advection tests](/benchmarks/material-interface-advection.md)
* [Multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)
* [Optimal cell-average decomposition](/methods/optimal-cell-average-decomposition.md)
* [Positivity-preserving numerical fluxes for Navier–Stokes](/methods/positivity-preserving-navier-stokes-flux.md)
* [Pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)
* [Shock-induced combustion and detonation](/benchmarks/shock-induced-combustion.md)
* [Shock–mixing-layer interaction](/benchmarks/shock-mixing-layer-interaction.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md)
