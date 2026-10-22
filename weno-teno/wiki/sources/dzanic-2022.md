---
type: Source
title: "Dzanic et al. (2022) — Utilizing time-reversibility for shock capturing in nonlinear hyperbolic conservation laws"
description: "Artificial-viscosity shock capturing whose indicator is the defect of a forward step followed by a time-reversed step: a vector-valued viscosity, one per conserved component, that needs no entropy pair and is O(h) at shocks, tested in nodal DG/flux reconstruction (PyFR) on Euler and MHD problems."
resource: "doi:10.1016/j.compfluid.2022.105652"
source_kind: paper
authors: [Dzanic T., Trojak W., Witherden F.D.]
year: 2022
venue: "Comput. Fluids 247:105652"
local_file: "/home/stefano/papers/mosaic/weno-teno/2022_Crossref_Computers_amp_Fluids_Dzanic_Utilizing_time-reversibility_for_shock_capturing_in_nonlinea.pdf"
tags: [artificial-viscosity, troubled-cell, dg, limiting, mhd]
timestamp: 2026-10-22T20:00:00Z
---

# Summary

The paper proposes an [artificial-viscosity](/methods/artificial-viscosity.md) method whose
[shock indicator](/definitions/troubled-cell-indicator.md) rests on time reversibility.
Entropy solutions are invariant under $t\to-t$ only where they are smooth: across a shock the
entropy admissibility condition makes them irreversible (the motivation of
[entropy stability](/properties/entropy-stability.md), after Dafermos). The method takes one
forward explicit Euler step with an upwind-biased divergence, then one step of $-\Delta t$
with a downwind-biased divergence (upwind for reversed time). The component-wise defect
$d_{\mathrm{TR}}(u^n)=\lvert u^\dagger-u^n\rvert$ between the reversed and the original state drives the
viscosity $\mu_{\mathrm{TR}}=c_\mu h^2d_{\mathrm{TR}}/(\Delta t\,\Delta_\Omega u^n)$, normalized by the
global range of each component. The time-reversibility (TR) viscosity is vector-valued (one
entry per conserved component), needs no extra equation and no entropy pair, and has one
tunable constant $c_\mu$.

A first-order analysis (forward Euler, upwind flux, step data) gives $\mu_{\mathrm{TR}}\to
c_\mu a\Delta x$ as $\Delta t\to0$ for linear advection and for Burgers' equation, with $a$
the advection or shock speed. With $c_\mu=1/2$ this is the viscosity that turns a central
scheme into first-order upwind, a statement on
[numerical dissipation](/definitions/numerical-dissipation.md).

The method runs in [PyFR](/software/pyfr.md): nodal
[discontinuous Galerkin](/methods/discontinuous-galerkin.md) recovered by
[flux reconstruction](/methods/flux-reconstruction.md), a
[Rusanov flux](/methods/lax-friedrichs-flux.md) whose dissipative part is negated for the
downwind divergence, BR1 viscous fluxes and explicit RK4. The viscosity is constant per
element and capped by $\mu_{\max}=c_{\max}\hat a h_{\max}$. Tests: the
[Burgers](/benchmarks/burgers-equation-tests.md) sine wave at $\mathbb P^{14}$, the
[KPP rotating wave](/benchmarks/kpp-rotating-wave.md), [Sod](/benchmarks/sod-and-lax-shock-tubes.md)
(first-order $L^1$ convergence at $\mathbb P^2$–$\mathbb P^7$),
[Shu–Osher](/benchmarks/shu-osher-problem.md), the
[isentropic vortex](/benchmarks/isentropic-vortex.md) (order $N+1$ or better), a new
partially-confined explosion, the inviscid ONERA M6 wing, the
[MHD rotor](/benchmarks/mhd-blast-wave.md) and the
[Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md), the last two with a Powell source for
the [divergence constraint](/properties/divergence-free-magnetic-field.md). Discontinuities
are resolved within 2–5 solution points.

# Version read

arXiv 2110.03653v2 [math.NA], 18 Apr 2022, Elsevier preprint template ("Preprint submitted to
Elsevier"): not the version of record, and the file prints no volume or article number, which
come from Crossref. 20 pages, all read; equations on pp. 4, 5, 15 and 16 checked visually.
Page 1 prints the title in title case and the third author as "F. D. Witherden" (Crossref:
"Witherden F."); page 1 is followed for the initials. Section, equation, table and figure
numbers are those of the arXiv v2.

# Key claims

Registry notation (see the notation map): conserved state $u$, TR defect
$d_{\mathrm{TR}}$ and viscosity $\mu_{\mathrm{TR}}$ (vector), advection or wave speed $a$, polynomial degree $N$, CFL number
$\nu=a\Delta t/\Delta x$.

1. Where an entropy functional satisfies a conservation equation the system is invariant under $t\to-t$; near a shock the entropy admissibility criterion makes the solution time-irreversible (§2, citing Dafermos). **Stated**
2. The TR defect $d_{\mathrm{TR}}(u^n)=\lvert u^\dagger-u^n\rvert$ (Eq. 5) is a component-wise irreversibility indicator that tends to zero in smooth regions, where it scales with the approximation error $O(h^{p_{\mathrm s}}\Delta t^{r_{\mathrm{RK}}+1})$, $p_{\mathrm s}$ and $r_{\mathrm{RK}}$ the spatial and temporal orders (§2). **Stated** (scaling posited, not derived for general orders)
3. Near a shock the defect scales as $O(h^{-1}\Delta t)$, so the viscosity of Eq. (6) is $O(h)$ (§2, "shown in Section 3"). **Derived** (for first-order upwind with forward Euler only, Eqs. 18 and 27)
4. TR viscosity $\mu_{\mathrm{TR}}=c_\mu h^2d_{\mathrm{TR}}(u^n)/(\Delta t\,\Delta_\Omega u^n)$, with $\Delta_\Omega u^n=\max_\Omega u-\min_\Omega u$ over $[t^n,t^{n+1}]$, component-wise (Eqs. 6–7). **Stated** (definition)
5. Linear advection ($a>0$), first-order upwind with forward Euler, step data with jump $\delta u=u_L-u_R>0$: the defect is the same on both sides of the jump, $d_{\mathrm{TR}}(u_1)=d_{\mathrm{TR}}(u_2)=(1-\nu)\nu\lvert\delta u\rvert$ (Eq. 18). **Derived** *(compiler check, not in the sources: $u_2^{n+1}=u_R+\nu\delta u$, $u_1^\dagger=u_L-\nu(1-\nu)\delta u$, $u_2^\dagger=u_R+\nu(1-\nu)\delta u$.)*
6. Hence $\mu_{\mathrm{TR}}=c_\mu(a\Delta x-a^2\Delta t)$ (Eq. 19) and $\lim_{\Delta t\to0}\mu_{\mathrm{TR}}=c_\mu a\Delta x$ (Eq. 20); with $c_\mu=1/2$ this is the "monotone" viscosity with which a second-order central scheme plus viscous dissipation recovers first-order upwind exactly (§3.1). **Derived**
7. Burgers' equation with $u_L,u_R>0$: the defect is symmetric, $d_{\mathrm{TR}}(u_2)=d_{\mathrm{TR}}(u_1)$ (Eq. 28), and $\lim_{\Delta t\to0}\mu_{\mathrm{TR}}=c_\mu\lvert\tfrac12(u_L+u_R)\rvert\Delta x$, the shock speed times $c_\mu\Delta x$ (Eq. 30). **Derived** (see Printed slips for Eqs. 27 and 29; the limit is unaffected)
8. Similar conclusions hold for a Rusanov-type upwind flux, "with significantly more algebraic complexity" (§3.2). **Stated**
9. The method needs no additional governing equation, applies to systems without a known entropy–entropy-flux pair, is independent of mesh and order, and has one tunable parameter $c_\mu$ (Abstract, §§1, 2, 6). **Stated**
10. The main novelty is a vector-valued viscosity, one per component, useful when some components are discontinuous and others are not, at no extra cost (Abstract, §§1, 2; Orszag–Tang, Fig. 13). **Shown**
11. The acceptable range of $c_\mu$ is "on the order of 1-10"; it was tuned per problem and kept fixed under changes of resolution or order: Burgers 1, KPP 6, Sod 5, Shu–Osher 5, vortex 6, explosion 6, ONERA M6 8, rotor 2, Orszag–Tang 3 (§§4.2, 5). **Shown**
12. A global cap $\mu_{\max}=c_{\max}\hat a h_{\max}$, $c_{\max}\approx100$, computed once before the run, only keeps TR-viscosity transients from limiting the explicit time step; in 1D (implicit viscous terms) results were identical with and without it (§4.2, Eq. 40). **Shown** (1D only)
13. Burgers, $u_0=\sin(2\pi x)+2$, $t=0.5$, $c_\mu=1$: with $\mathbb P^{14}$ on 5 elements the shock spans 4–5 solution points without spurious oscillations, a width similar to $\mathbb P^4$ on 15 elements; "the proposed approach does not suffer with increasing approximation order" (§5.1.1, Fig. 1). **Shown**
14. KPP rotating wave, $\mathbb P^9$, $32^2$ elements, $c_\mu=6$, $t=1$: the expected composite wave structure with sub-element resolution and no oscillations; the viscosity is localized and "roughly proportional to the magnitude of the discontinuity"; qualitative convergence on $16^2$–$64^2$ (§5.1.2, Figs. 2–3). **Shown**
15. Sod, 200 degrees of freedom ($\mathbb P^3$ on 50 elements, $\mathbb P^9$ on 20), $c_\mu=5$, $t=0.2$: good agreement, with the density viscosity localized at the shock and minimal at the rarefaction and contact (§5.2.1, Fig. 4). **Shown**
16. Sod $L^1$ density error on 20–160 elements converges at first order, rates 0.92, 1.02, 0.87, 0.95, 0.99, 0.85 for $\mathbb P^2$–$\mathbb P^7$; at fixed degrees of freedom a higher order gives a marginally lower error (Table 1). **Shown**
17. Shu–Osher, $\mathbb P^4$, 100 elements, $c_\mu=5$, $t=1.8$: good agreement with a resolved exact-Godunov reference; the indicator separates the shocks from the oscillatory density field, roughly in proportion to shock strength (§5.2.2, Fig. 5). **Shown**
18. Isentropic vortex, $c_\mu=6$, one convective period: the $L^2$ density convergence rate "met or exceeded" $N+1$: 3.30, 4.93, 5.53, 7.44, 7.79, 8.74 for $\mathbb P^2$–$\mathbb P^7$ (Table 2). **Shown**
19. For $\mathbb P^7$ on the vortex the maximum viscosity components fall from $[2.6\times10^{-8},8.6\times10^{-8},7.4\times10^{-8},4.7\times10^{-7}]$ at $N_x=20$ to $[8.1\times10^{-11},1.7\times10^{-10},1.4\times10^{-10},1.1\times10^{-9}]$ at $N_x=40$, consistent with the viscosity tending to the approximation error (§5.2.3). **Shown**
20. Partially-confined explosion (new; radial Sod inside a partial ring), $\mathbb P^4$, $c_\mu=6$: shocks resolved with minimal oscillation and without over-dissipating the Richtmyer–Meshkov-type vortices; the finer mesh improves small scales without retuning $c_\mu$ (§5.2.4, Fig. 7). **Shown**
21. ONERA M6 (inviscid, $M_\infty=0.8395$, incidence $3.06^\circ$), $\mathbb P^4$, $c_\mu=8$: the lambda shock is captured within a few solution points, and $C_p$ at 65% span agrees satisfactorily with the (viscous) experiment of Schmitt & Charpin (§5.2.5, Fig. 9). **Shown**
22. MHD rotor, $c_\mu=2$, $t=0.15$, $\mathbb P^4$ on $128^2$ and $\mathbb P^9$ on $64^2$: effectively non-oscillatory profiles, discontinuities over 2–3 solution points, no deterioration with order (§5.3.1, Figs. 10–11). **Shown**
23. Orszag–Tang, $\mathbb P^7$ on $32^2$ and $64^2$, $c_\mu=3$, $t=0.48$: density and magnetic viscosity fields are "particularly distinct", reflecting separate hydrodynamic and magnetic shocks; the pressure cut at $y/L=0.3125$ agrees well with Jiang & Wu on $64^2$ and is over-diffused on $32^2$ (§5.3.2, Figs. 12–14). **Shown**
24. The approach applies to any shock-capturing method that needs an indicator, not only to artificial viscosity (§2). **Stated**
25. Future work: mixed hyperbolic–parabolic systems and non-parabolic viscous regularizations (§6). **Stated**

# Printed slips

- Eq. (18), second line of $\mathcal D(u_2)$: "$+c\frac{\Delta t}{\Delta x}(u^{n+1}_3-u^{n+1}_2)$" uses an undefined $c$ in place of $\lambda$ (twice); the result is correct.
- Eq. (23), first line: "$u_0^{n+1}=u_0^{n+1}$"; by analogy with Eq. (15) it should read $u_0^{n+1}=u_0^n$.
- Eq. (27) prints $\mathcal D(u_1)=\big\lvert k\big(\zeta-2ku_2^n\zeta+k^2\zeta^2\big)\big\rvert$ with $k=\Delta t/(2\Delta x)$ and $\zeta=u_L^2-u_R^2$; the last term should carry a minus sign. Eq. (29) moreover replaces $k$ by $\Delta t/\Delta x$ inside the bars. Neither affects the limit of Eq. (30). *(compiler check, not in the sources: $u_2^{n+1}=u_R+k\zeta$, $u_1^{n+1}=u_L$ and the downwind flux give $u_1^*-u_L=k\big((u_2^{n+1})^2-u_L^2\big)=k(-\zeta+2ku_R\zeta+k^2\zeta^2)$, so $\mathcal D(u_1)=k\lvert\zeta-2ku_R\zeta-k^2\zeta^2\rvert$.)*
- Eq. (30): the middle expression prints "$c\,\lvert\ldots\rvert$" without the subscript $\mu$.
- §5.2.1: "the convergence of the entropy filtering approach for discontinuous solutions"; the method of the paper is the TR viscosity.
- §5.3.2: the Orszag–Tang density contours are said to be "shown in Fig. 7"; they are in Fig. 12 (Fig. 7 is the explosion).
- §5.2.4: the domain is printed "$\Omega=[-1,1]$" for a 2D problem, while the Fig. 6 caption says "$[0,1]^2$".
- §5.3.1: "$r=\sqrt{x^2+y^2}$" on $[0,1]^2$, while the rotor velocity is centred at $(0.5,0.5)$.
- §5.3: the magnetic pressure is defined as "$P_b=1/2(\gamma-1)\mathbf B\cdot\mathbf B$", while the flux (Eq. 47) uses $\tfrac12\mathbf B\cdot\mathbf B$; the factor is not explained.
- Eq. (48) and the rotor set-up write the velocity as $\mathbf u$, which is the conserved state elsewhere (velocity $\mathbf v$).
- Page 1 labels both affiliations "a"; "consistent with assumption that" (§5.2.3).

# Notation map

| Dzanic et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf u$, $\mathbf F(\mathbf u)$ | $u$, $f^{(d)}(u)$ | conserved state and inviscid flux; **$\mathbf u$ is also the velocity in Eq. 48 and §5.3.1** |
| $\mathbf v$ | $v$ | velocity (§§5.2–5.3); also the FR auxiliary gradient in §4.1 |
| $\nabla\cdot\mathbf F^+$, $\nabla\cdot\mathbf F^-$ | kept | upwind- and downwind-biased discrete divergences; **not the Lax–Friedrichs split fluxes $f^\pm$** |
| $\mathbf u^*$, $\mathcal D$ | $u^\dagger$, $d_{\mathrm{TR}}$ (page-local) | reversed state, TR defect |
| $\boldsymbol\mu$, $\mu_\rho$ | $\mu_{\mathrm{TR}}$, $\mu_{\mathrm{TR},\rho}$ | vector artificial viscosity and its density entry; **$\mu$ is the affine translation in registry §10** |
| $\Delta\mathbf u^n$ | $\Delta_\Omega u^n$ (page-local) | global range of each component over $[t^n,t^{n+1}]$ |
| $c_\mu$, $c_{\max}$, $\hat\lambda$, $h_{\max}$ | $c_\mu$, $c_{\max}$, $\hat a$, $h_{\max}$ | TR constant, cap constant, a-priori maximum wave speed, largest mesh size |
| $h$, $h_k$ | kept | local mesh scale, $h_k^d=\lvert\Omega_k\rvert$; $h=\Delta x$ in §3 |
| $\lambda$ | $a$ | advection speed (§3.1), shock speed (Eq. 30), maximum wave speed |
| $\lambda\Delta t/\Delta x$ | $\nu$ | CFL number |
| $p$, $q$ (orders), $\mathbb P_p$ | $p_{\mathrm s}$ (page-local), $r_{\mathrm{RK}}$ (registry §10), $\mathbb P^N$ | spatial and temporal orders; polynomial degree, design order $N+1$; **$q$ is the weight exponent in the registry** |
| $N$ | $N_x$ | number of elements (§5); number of solution nodes in §4.1 |
| $M$ | kept | interface flux points (§4.1) and total degrees of freedom (Eq. 44) |
| $\mathbf p^{\partial\Omega+}$, $\mathbf p^{\partial\Omega-}$ | traces of own and neighbouring element | **"+" is the element of interest, opposite to the registry's $u^+_{i+1/2}$ (right state)** |
| $\mathbf h_i$ | kept | FR correction functions in $RT_p$ |
| $\delta u=u_L-u_R$, $\zeta=u_L^2-u_R^2$ | kept | jump magnitudes of the first-order analysis |
| $P$, $P_b$, $\mathbf B$ | $p$, kept, $B$ | pressure, "magnetic pressure", magnetic field |

# Reference list

36 printed references in numbered style ([1]–[36]), all parsed and merged complete into the
[bibliography](/bibliography.md) with `citedby` `dzanic-2022`. DOIs are printed for all but
[32] (AGARD AR 138, a technical report). [13] (Dafermos) is a book chapter; [14] prints the
page range "107–107"; [1] keeps Hopf's printed equation in the title. No printed duplicates.

# Pages created or updated

Chunk 3 (2026-10-22). This source is cited on:

* [Artificial viscosity and spectral viscosity](/methods/artificial-viscosity.md)
* [Burgers equation tests](/benchmarks/burgers-equation-tests.md)
* [Discontinuous Galerkin method](/methods/discontinuous-galerkin.md)
* [Divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
* [Entropy stability](/properties/entropy-stability.md)
* [Flux reconstruction and energy-stable FR](/methods/flux-reconstruction.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [KPP rotating wave](/benchmarks/kpp-rotating-wave.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [MHD blast wave and rotor](/benchmarks/mhd-blast-wave.md)
* [Numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
* [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md)
* [PyFR](/software/pyfr.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
