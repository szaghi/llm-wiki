---
type: Source
title: "Zampa & Dumbser (2025) — An asymptotic-preserving and exactly mass-conservative semi-implicit scheme for weakly compressible flows based on compatible finite elements"
description: "Semi-implicit compatible finite-element scheme for weakly compressible isentropic flow, with H(div) momentum, discontinuous density and pressure, hybridization and an a posteriori MOOD artificial viscosity; mass is conserved cell by cell and the scheme is proved to reduce to an H(div) incompressible Navier–Stokes scheme at zero Mach number."
resource: "doi:10.1016/j.jcp.2024.113551"
source_kind: paper
authors: [Zampa E., Dumbser M.]
year: 2025
venue: "J. Comput. Phys. 521:113551"
local_file: "/home/stefano/papers/mosaic/weno-teno/2025_Crossref_Journal_of_Computational_Physics_Zampa_An_asymptotic-preserving_and_exactly_mass-conservative_semi-.pdf"
tags: [asymptotic-preserving, semi-implicit, all-mach, finite-element, mood, artificial-viscosity]
timestamp: 2026-10-23T19:58:00Z
---

# Summary

Zampa & Dumbser (2025) build a semi-implicit finite-element method for weakly
compressible isentropic flow and its incompressible limit. The unknowns are density,
momentum and a specific entropy carried by a non-conservative transport equation in
place of the energy. Space uses compatible finite elements: momentum in the
Raviart–Thomas space $\mathrm{RT}_N$, density and pressure in discontinuous
$\mathrm d\mathbb P^N$, and a "momentum vorticity" in continuous Lagrange elements of
degree $N+1$ (Nédélec in 3D). Because $\nabla\cdot\mathrm{RT}_N=\mathrm d\mathbb P^N$,
the density update is exactly the divergence of the discrete momentum, so mass is
conserved cell by cell (Theorem 3.1).

Time stepping is a first-order splitting. Momentum convection, by a
[DG](/methods/discontinuous-galerkin.md) step with a Ducros-type
[split flux](/methods/split-convective-forms.md) plus Rusanov dissipation, and entropy
transport, by a [path-conservative](/methods/path-conservative-scheme.md) DG step, are
explicit. Pressure, viscous terms and the density–pressure coupling are implicit,
solved by a Newton iteration on the equation of state, so the CFL condition involves
only the flow speed ([semi-implicit all-Mach schemes](/methods/semi-implicit-all-mach-scheme.md)).
The vorticity decouples into one SPD system. Hybridization of the RT space removes the
ill-conditioning of the pressure Schur complement as $c^2\to\infty$, and every linear
system solved is symmetric definite.

Shocks are handled by an a posteriori
[MOOD](/methods/mood-a-posteriori-limiting.md)-type
[artificial viscosity](/methods/artificial-viscosity.md): a candidate solution is
checked against a relaxed discrete maximum principle on Voronoi neighbours, troubled
cells get a viscosity $\tfrac12h\,s_{\max}$, and the step is recomputed. Theorem 3.2
proves [asymptotic preservation](/properties/asymptotic-preservation.md): with
constant density and $1/c^2=0$ the Newton iteration converges in one step to a new
H(div) vorticity–velocity–pressure scheme for incompressible Navier–Stokes. Tests are
the [isentropic vortex](/benchmarks/isentropic-vortex.md), an acoustic pulse, a
circular [explosion](/benchmarks/explosion-and-implosion-problems.md), low-Mach
[Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md), the
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md), a double shear layer, the
[lid-driven cavity](/benchmarks/lid-driven-cavity.md), a backward-facing step and
[cylinder flow](/benchmarks/flow-past-circular-cylinder.md). The method touches the
bundle through its limiter, its fluxes and its low-Mach property; it has no
reconstruction content.

# Version read

The archive file is arXiv:2407.10163v1 [math.NA], 14 July 2024 (manuscript dated
12 July 2024), 29 pages, all read; pp. 4–7 and 9–11 checked on the page images. It is
the preprint of the J. Comput. Phys. paper, not the version of record; changes made
in review are not visible. Title and authors match the Crossref record. Every page
carries the running header "Well-balanced hybrid FV/FE for inc.MHD — Submitted to
...", left over from another manuscript; the identity of the paper is not in doubt.
Every claim, equation and number on this page is that of arXiv v1.

# Key claims

Registry notation: momentum $\rho v$ (source $\mathbf m$), velocity $v$, sound speed
$c$, $\gamma$, Mach number $M$, $\Delta t$, $\mathbb P^N$. Page-local: $N$ the
polynomial label of the spaces ($\Sigma_{N+1}$, $\mathrm{RT}_N$, $\mathrm d\mathbb P^N$;
source $r$); $\mathsf S$ the specific entropy of the equation of state
$p=\rho^\gamma e^{\mathsf S/c_v}$ ($\mathsf S=c_vs$); $\mathfrak w=\epsilon_{\mathrm m}\nabla\times(\rho v)$
the momentum vorticity; $\epsilon_\rho$, $\epsilon_{\mathrm m}$, $\epsilon_{\mathsf S}$
the viscosities of the regularized system; $h$ the mesh size; $s_{\max}$ the
dissipation speed; $\delta_T$, $\delta_{\mathrm 0,T}$, $\eta_{\mathrm r}$ the
limiter's relaxation and parameters; $p_0$ the background pressure of the
Taylor–Green test.

1. Momentum in $\mathrm{RT}_N$ and density in $\mathrm d\mathbb P^N$, with $\nabla\cdot\mathrm{RT}_N=\mathrm d\mathbb P^N$, make the density update $\rho_h^{n+1}=\rho_h^n-\Delta t\,\nabla\cdot(\rho v)_h^{n+1}$ hold pointwise: mass is conserved on every element, and momentum globally, when the normal momentum and the tangential $\mathfrak w_h$ vanish on $\partial\Omega$ and $\epsilon_\rho=0$ (Thm 3.1, Eqs. (13)–(14)). **Proved**
2. With $\epsilon_\rho\ne0$ global mass is still conserved if $\nabla\rho\cdot n=0$ on $\partial\Omega$ (Thm 3.1, proof). **Proved**
3. The splitting makes the CFL condition depend only on the flow speed, not on the sound speed; the time step is $\Delta t=C_{\mathrm{CFL}}h/((2N+1)\max(\lVert v\rVert_\infty,1))$ with default $C_{\mathrm{CFL}}=0.25$ (Abstract, §1, §3.1, §4). **Stated**
4. The vorticity equation (16) decouples from the momentum–pressure system when $\nabla\times z_h$ is an admissible momentum test function (outflow and nonstandard slip conditions); its matrix is SPD (§3.2.5). **Derived**
5. For Dirichlet conditions the inclusion $\nabla\times\Sigma_{N+1}\subset\mathring{\mathrm{RT}}_N$ fails, which the authors name as the source of the suboptimal convergence of vorticity and pressure shown by Arnold, Falk and Gopalakrishnan; they impose the normal condition with a boundary multiplier and close the underdetermined system (19) with the boundary pressure data or its previous value (Remarks 3.2–3.3). **Stated**
6. The non-hybridized pressure Schur complement $M+S+D^\top(M^p_{c^2})^{-1}D$ is SPD but becomes ill-conditioned as $c^2\to\infty$, because the weighted pressure mass matrix $M^p_{c^2}\to0$ (§3.2.5). **Stated**
7. After hybridization the local solver stays invertible as $c^2\to\infty$, and the condensed multiplier matrix $\tilde BCL^{-1}C^\top\tilde B^\top$ is symmetric negative definite (Lemma 3.1). **Proved**
8. Hybridizing the vorticity system (16) is possible but brings no significant advantage, since it is already SPD (Remark 3.6). **Stated**
9. Asymptotic preservation: if $\rho_h^n=\rho$ is constant, $1/(c^2)^{n+1,0}=0$ and $\epsilon_{\mathrm m}=\mu/\rho$ with constant $\mu$, the Newton iteration (11) converges in one iteration and its solution solves the incompressible scheme (24) (Thm 3.2). **Proved**
10. The incompressible limit scheme (24) is new as a combination (rotational viscous form, compatible spaces, semi-implicit time stepping, hybridization) and is close to the MEEVC scheme of Palha & Gerritsma and to the HDG scheme of Lehrenfeld & Schöberl (§1, §3.5). **Stated**
11. The DG convective term coincides with that of Guzmán et al.; conforming alternatives (Lamb identity, skew-symmetric form) have no upwinding and need implicit, nonsymmetric time stepping, while DG upwinding is stable with explicit stepping (§3.5). **Stated**
12. The compared H(div) schemes treat convection implicitly with nonsymmetric systems, except Lehrenfeld & Schöberl (pseudo-implicit) and Fu (fully explicit, unsuitable for low Reynolds numbers) (§3.5). **Stated**
13. The time discretization with the dissipative flux is not energy conserving; the dissipation is remarkably small and helps against oscillations from under-resolved scales (§3.5, §4.5). **Shown**
14. Because the energy equation is replaced by a non-conservative entropy equation, shocks are not expected to be correct at large shock Mach numbers; the method is restricted to weakly compressible isentropic flow with Mach number from zero to about one (§3.2.2). **Stated**
15. The midpoint rule for the path integral (8) of the entropy flux suffices "to preserve the accuracy and correctness of the scheme" (§3.2.2). **Stated**
16. Isentropic vortex, $N=0,1,2$: observed $L^2$ order $N+1$ for density, velocity and pressure; for $N=2$ on the finest mesh ($N_x=120$) $L^2(\rho_h)=5.2539\times10^{-6}$, order 3.20 (Tables 1–3). **Shown**
17. Taylor–Green vortex at low Mach ($N=0,1,2$, $p_0=10^7$, $C_{\mathrm{CFL}}=0.5$): velocity and pressure converge at order $N+1$; for $N=2$, $N_x=120$: $L^2(v_h)=7.8322\times10^{-6}$ (order 3.00), $L^2(p_h)=3.4815\times10^{-6}$ (order 2.86) (Tables 5–7). **Shown**
18. The $L^\infty$ errors of $\nabla\cdot v_h$ and of $\rho_h$ decrease as $M^2$ (order 2.00) from $M=1.20\times10^{-2}$ to about $M=10^{-6}$; at the smallest $M$ the divergence order drops to 1.87 and 0.92 as the error reaches round-off, about $10^{-13}$ (Table 4). **Shown**
19. Inviscid Taylor–Green to $t=10$ ($N=2$): energy dissipation "less than $\approx2\cdot10^{-6}$ per time unit"; momentum and incompressibility errors of the order of $M^2$ (§4.5, Fig. 6). **Shown**
20. Circular explosion ($N=2$, $120\times120$): the artificial viscosity is active only near discontinuities, with no spurious oscillations (§4.3, Figs. 3–4). **Shown**
21. Lid-driven cavity at $\mu=0.01$ and $0.001$ on $40\times40$: excellent and good agreement with Ghia et al. (§4.7, Figs. 8–9). **Shown**
22. Backward-facing step at $\mathrm{Re}=44$–$400$: recirculation length compared qualitatively with Armaly et al. and two numerical references (§4.8, Fig. 10). **Shown**
23. Cylinder flow: the Strouhal number against $\mathrm{Re}$ agrees with Tavelli & Dumbser, Williamson & Brown and the universal Strouhal curve, with fewer elements (9168) than the references (§4.9, Fig. 11). **Shown**
24. The method is "one of the first works that uses a posteriori limiting in the context of compatible finite element exterior calculus" (§1). **Stated**
25. The scheme is first order in time because of the splitting; higher order by IMEX Runge–Kutta is "easily achieved" (§3.1, §5). **Stated**

Limiter details (§3.3, Eqs. (21)–(23)). A cell $T$ is troubled if the candidate
variable $W$ leaves $[\min_{\mathcal N(T)}W-\delta_T,\ \max_{\mathcal N(T)}W+\delta_T]$
over the Voronoi neighbourhood $\mathcal N(T)$, with
$\delta_T=\max\big(\delta_{\mathrm 0,T},\eta_{\mathrm r}(\max_{\mathcal N(T)}W-\min_{\mathcal N(T)}W)\big)$,
$\delta_{\mathrm 0,T}=10^{-4}$, $\eta_{\mathrm r}=10^{-3}$. The viscosity is
$\tfrac12h\,s_{\max}$ on troubled cells and a small floor elsewhere; it is applied
first to the entropy ($W=\mathsf S$), then to density and momentum ($W=\rho$).

# Printed slips

- Thm 3.1, Eq. (13): printed $\int_T\rho_h^{n+1}=\int_T\rho_h^n+\Delta t\int_{\partial T}\mathbf m_h^{n+1}\cdot\mathbf n\,dS$. *(Compiler check, not in the sources: integrating the stated pointwise update $\rho_h^{n+1}=\rho_h^n-\Delta t\,\nabla\cdot\mathbf m_h^{n+1}$ over $T$ gives a minus sign before $\Delta t$.)*
- Eq. (9): printed $(\mathbf m_h^*,\mathbf v_h)=(\mathbf m_h^n,\mathbf v_h)-\Delta t(\mathcal F_{\mathbf m},\nabla_h\mathbf v_h)+\langle\widehat{\mathcal F}_{\mathbf m}\mathbf n,\mathbf v_h\rangle_{\partial\mathcal T_h}$. *(Compiler check, not in the sources: elementwise integration by parts of $\mathbf m^*=\mathbf m^n-\Delta t\,\nabla\cdot\mathcal F_{\mathbf m}$ gives $(\mathbf m_h^*,\mathbf v_h)=(\mathbf m_h^n,\mathbf v_h)+\Delta t(\mathcal F_{\mathbf m},\nabla_h\mathbf v_h)-\Delta t\langle\widehat{\mathcal F}_{\mathbf m}\mathbf n,\mathbf v_h\rangle_{\partial\mathcal T_h}$: both signs differ and the facet term lacks $\Delta t$.)*
- Table 4: the $p_0$ column prints $5\cdot10^9$ in rows 6 and 7. *(Compiler check, not in the sources: the text states the sequence $p_0\in\{5\cdot10^3,5\cdot10^4,\dots,5\cdot10^{12}\}$, ten values for ten rows, and the Mach column falls by $\sqrt{10}$ per row ($3.78\cdot10^{-5}$ then $1.20\cdot10^{-5}$), so row 6 is $5\cdot10^8$.)* The last column is headed "O($p_h$)" but reports the order of $L^\infty(\rho_h)$.
- §4.5: the conservation test prints "$p_0=1e-7$", while the other runs use $p_0=10^7$ and the text speaks of errors of the order of the squared Mach number, which needs a large $p_0$.
- §3.2.1: "Here ζ is a user-defined parameter. In this work we choose η = 40": the penalty is $\zeta$ in the formula and $\eta$ in the value; $\eta$ is reused in Eq. (22) with value $10^{-3}$.
- Lemma 3.1 prints "$\widetilde BCE^{-1}C^T\widetilde B^T$" ($E$ for $L$); its proof writes $\vec\lambda$ for $\vec\xi$, $C$ for $C^T$, "$-\vec m\cdot(\widetilde M^{\mathbf m}+S)\vec v$" and "and and".
- Thm 3.2 concludes $\boldsymbol\omega_h^n=\boldsymbol\omega_h^{n+1,1}$; Eq. (24) needs $\boldsymbol\omega_h^{n+1}$. The tangential boundary term is $\langle\mathbf n\times\overline{\mathbf m},\mathbf z_h\rangle$ in (11c) and $\langle\overline{\mathbf u}_h\times\mathbf n,\mathbf z_h\rangle$ in (24a), of opposite sign, although the proof says (11c) "is (24a) multiplied by ρ".
- Eq. (23) says "if (22) is violated"; the criterion is Eq. (21), and Eq. (21) prints $t^n$ for both the candidate value and the bounds.
- Tables 1–3 call the test "Shu vortex", §4.1 the "isentropic vortex proposed by Hu and Shu [73]", where [73] is Hu & Shu's WENO paper for MHD. §2.2 refers to "the system (1)" for the viscous limit, which is system (2). Citation lists repeat [42] in §3.1 and §5. Typos: "sidem", "Netwon", "possibile", "swhon", "exibit suprious", "subpotimal", "incompressilibity", "polynomaials".
- References: [20] and [22] are the same work (Clain, Diot & Loubère 2011), as are [50] and [75] (Toro 2009) and [30] and [78] (Klein et al.; [78] without year or pages); [21] is printed with volume 64 of J. Comput. Phys.; [43] with volume "4201"; [29] has no year, volume or pages; "Michel-Dansac" and "Michael-Dansac" in [41] and [46].

# Notation map

| Zampa & Dumbser (arXiv v1) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf m$, $\mathbf u=\mathbf m/\rho$ | $\rho v$, $v$ | |
| $S$, $p=\rho^\gamma e^{S/c_v}$ | $\mathsf S=c_vs$ (local) | **collision** with $S(u)$, $S_k$ and the source's div-div matrix $S$ |
| $c^2=\partial p/\partial\rho$ | $c^2$ | isentropic |
| $r$; $\Sigma_{r+1}$, $\mathrm{RT}_r$, $\mathrm d\mathcal P_r$ | $N$; $\Sigma_{N+1}$, $\mathrm{RT}_N$, $\mathrm d\mathbb P^N$ (local) | **collision** of $r$ with the WENO stencil size; order $N+1$ |
| $\boldsymbol\omega=\epsilon_{\mathbf m}\nabla\times\mathbf m$ | $\mathfrak w$ (local) | **collision** with $\omega_k$ |
| $\epsilon_\rho$, $\epsilon_{\mathbf m}$, $\epsilon_S$ | $\epsilon_\rho$, $\epsilon_{\mathrm m}$, $\epsilon_{\mathsf S}$ (local) | viscosities, not the weight regularization $\epsilon$ |
| $\{\{\cdot\}\}$, $[\![\cdot]\!]$ | $\{\!\{\cdot\}\!\}$, signed jump | the source's jump is $\pm(\hat v^+-\hat v^-)$, zero on boundary facets |
| $s_{\max}$ | $s_{\max}$ (local) | $2\max\lvert v\cdot n\rvert$ in §3.2.2, the full-system wave speed in §3.3 |
| $\Psi(s)$ | path in $(\rho,\rho v)$ | segment path |
| $\delta_T$, $\delta_0$, $\eta$ | $\delta_T$, $\delta_{\mathrm 0,T}$, $\eta_{\mathrm r}$ (local) | **collision** of $\eta$ with the entropy and of $\delta_0$ with the TENO flag |
| $\zeta$ | $\zeta_{\mathrm{IP}}$ (local) | **collision** with the characteristic variables $\zeta$ |
| $M_N$ | mesh with $N_x$ intervals per side | |
| $M$ | Mach number $M$ | also the source's mass matrices $M$, $M^p_{c^2}$ |

# Reference list

The arXiv v1 prints 100 references, numbered [1]–[100], all with titles. The list is
merged complete into the [bibliography](/bibliography.md), with `citedby` including
`zampa-2025`. The printed duplicates [20] = [22], [50] = [75] and [30] = [78] are
recorded once each. Ref. [15] (Zhang, Palha, Gerritsma & Yao 2024, MEEVC) and ref. [85]
(Abgrall, Busto & Dumbser 2023, thermodynamically compatible schemes) would take keys
already used by different works and are keyed apart by venue. Refs. [14], [18] and
[19] are preprints and keep their own entries; [29] is undated. No item is
unparseable.

# Pages created or updated

Chunk 10 (2026-10-23), cited further in chunks 11–12 (2026-10-24/30). This source is cited on:

* [Artificial viscosity and spectral viscosity](/methods/artificial-viscosity.md)
* [Asymptotic preservation](/properties/asymptotic-preservation.md)
* [Discontinuous Galerkin method](/methods/discontinuous-galerkin.md)
* [Flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)
* [Lid-driven cavity](/benchmarks/lid-driven-cavity.md)
* [Linear acoustics tests](/benchmarks/linear-acoustics-tests.md)
* [MOOD a posteriori limiting](/methods/mood-a-posteriori-limiting.md)
* [Path-conservative schemes](/methods/path-conservative-scheme.md)
* [Semi-implicit all-Mach schemes](/methods/semi-implicit-all-mach-scheme.md)
* [Split convective forms](/methods/split-convective-forms.md)
* [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
* [Two-dimensional explosion and implosion problems](/benchmarks/explosion-and-implosion-problems.md)
