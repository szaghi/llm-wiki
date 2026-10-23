---
type: Source
title: "Trojak & Dzanic (2024) — Positivity-preserving discontinuous spectral element methods for compressible multi-species flows"
description: "Extends the adaptive entropy filter to the conservative multi-species Euler and Navier–Stokes equations in nodal DG/FR: positivity of density, pressure and every partial density always, the mixture minimum-entropy constraint only where a parameter-free pressure-jump sensor detects a shock, with PyFR tests up to 3D turbulence."
resource: "doi:10.1016/j.compfluid.2024.106343"
source_kind: paper
authors: [Trojak W., Dzanic T.]
year: 2024
venue: "Comput. Fluids 280:106343"
local_file: "/home/stefano/papers/mosaic/weno-teno/2024_Crossref_Computers_amp_Fluids_Trojak_Positivity-preserving_discontinuous_spectral_element_methods.pdf"
tags: [dg, flux-reconstruction, positivity, multiphase, entropy-stable, gpu]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

The paper extends the adaptive [entropy filter](/methods/entropy-filtering.md)
of Dzanic & Witherden (2022) from single-species gas dynamics to the
conservative [multicomponent Euler](/definitions/multicomponent-euler-equations.md)
and Navier–Stokes equations in thermal equilibrium. The discretization is nodal
DG, recovered through [flux reconstruction](/methods/flux-reconstruction.md)
in [PyFR](/software/pyfr.md). The filter is an element-wise exponential modal
filter whose strength is the smallest that makes all nodal values satisfy a
set of convex constraints: positivity of the mixture density, the pressure
and every partial density ([bound preservation](/properties/bound-preservation.md)),
and a local minimum principle for the mixture entropy of Gouasmi et al. (2020).

The central finding is that enforcing the entropy constraint everywhere (the
"naive" extension) over-dissipates at species interfaces. There, a smooth
mixture density can be made of discontinuous partial densities whose entropy
field is numerically ill behaved. The remedy is a parameter-free switch that
drops the entropy constraint in an element unless a pressure-jump sensor,
modelled on the Krivodonova et al. (2004) interface-jump indicator
([troubled-cell indicators](/definitions/troubled-cell-indicator.md)),
reaches 1. The positivity constraints stay on, so positivity does not depend
on the switch. Other ingredients are a clipped, exponentiated entropy
functional for robustness near zero species density, a mesh scale defined by
the element's surface area, and the inviscid/viscous split of Dzanic &
Witherden for Navier–Stokes.

The evidence is numerical: a near-vacuum two-species
[density wave](/benchmarks/density-wave-advection.md) converging at order
$N+1$ with and without the switch; a two-species
[isentropic vortex](/benchmarks/isentropic-vortex.md) with flow reversal; the
Quirk–Karni shock tube; a helium–air
[shock–bubble interaction](/benchmarks/shock-bubble-interaction.md) on
unstructured triangles; a two-species [triple-point problem](/benchmarks/triple-point-problem.md)
at $2800\times1200$, $N=3$; a 3D viscous
[Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md);
and a two-species [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
at $\mathrm{Re}=1600$. Runs used up to 40 NVIDIA V100 GPUs.

# Version read

arXiv preprint arXiv:2308.02426v1 [physics.flu-dyn], 4 August 2023
("Preprint submitted to Elsevier"), 22 pages, all read; pp. 3, 4, 6–8, 10 and
17–20 were checked visually. It is not the version of record (C&F
280:106343). Page 1 matches Crossref in title and authors. Equation, table and
section numbers cited here are those of arXiv v1.

# Key claims

Registry notation: species index $i\to k$, partial density
$\alpha_i\rho_i\to\rho Y_k$, velocity $\mathbf V\to v$, pressure $P\to p$,
polynomial degree $p\to N$, constraints $\Gamma_k\to g_k$, filter strength
$\zeta\to\zeta_{\mathrm F}$ (as on the entropy-filtering page). The mixture
entropy $\sigma$ (physical sign, minimum principle) is written
$s_{\mathrm{mix}}$, the switching function $S_i$ of element $i$ is written $\mathcal S_K$ for element $K$
(both page-local).

1. The straightforward extension, enforcing $g_4=s_{\mathrm{mix}}-s_{\mathrm{mix},\min}$ everywhere, gives "exceedingly deficient approximations, particularly around species interfaces" (§3.1; §5.1.2, Figs. 1–2, 4). **Shown**
2. The cause is attributed to species interfaces, where even a smooth mixture density may consist of discontinuous species densities that, through Eqs. (9)–(10), give numerically ill-behaved entropy fields; dissipation is then added where little stabilization is needed (§3.1). **Stated**
3. The switch sets $g_4=s_{\mathrm{mix}}-s_{\mathrm{mix},\min}$ if $\mathcal S\ge1$ and $0$ otherwise (Eq. (25)), "inspired by the work of Gao et al." (§3.1). **Stated** (definition)
4. The physical constraints are enforced regardless of $\mathcal S$, so positivity preservation is independent of the switch, whose only purpose is accuracy at species interfaces (§3.1). **Stated** (by construction)
5. The switch is the pressure jump integrated over $\partial\Omega_i$, normalized by $h^{N+1}\lVert p^-\rVert_\infty\lvert\partial\Omega_i\rvert$ (Eq. (27)), on the grounds that the interface jump is at least $O(h^{N+1})$ for smooth solutions and $O(h)$ at discontinuities (§3.2, Eq. (26)). **Stated** (cited to Krivodonova et al.)
6. The pressure sensor separates contact discontinuities and species interfaces, across which the pressure is continuous, from shocks, and it is parameter-free (§3.2). **Stated**
7. A filter strength satisfying the constraints exists, given nodal DG, SSP explicit time stepping and a positivity-preserving entropy-stable Riemann solver, because the DG element mean is equivalent to a first-order Godunov update (§3.1). **Stated** (cited)
8. For Navier–Stokes the hyperbolic substep (Eq. (29)) obeys the local discrete minimum entropy principle, so the filter is applied after it; the viscous increment is added explicitly (Eq. (30)), followed by a positivity-only filter that is "very rare[ly]" needed (§3.3). **Stated** (cited)
9. Without the split, enforcing the entropy constraints on the full hyperbolic–parabolic system does not harm positivity, because a stable root-bracketing method converges to the maximal filter strength when no solution exists (§3.3). **Stated**
10. The modified entropy $s^*_{\mathrm{mix}}=\exp\big[\sum_kc_{v,k}\rho Y_k\log\big(\max(\epsilon_{\mathrm{tol}},\rho Y_k)^{1-\gamma_k}T\big)\big]$ (Eq. (33)) "significantly improved" robustness and accuracy and, "as the exponential function is strictly convex", retains the local minimum entropy principle (§4). **Stated**. A minimum principle survives a transformation $g$ when $g$ is increasing: $s(x_0)\ge\min s$ implies $g(s(x_0))\ge\min g(s)$. The exponential is increasing, so the conclusion holds, but convexity is not the operative property. And since the prefactor $\rho Y_k$ is not clipped, $s^*_{\mathrm{mix}}$ equals $\exp(s_{\mathrm{mix}})$ only when every $\rho Y_k\ge\epsilon_{\mathrm{tol}}$ *(compiler check, not in the sources)*.
11. HLLC "was found to yield notably better results than approaches such as that of Rusanov" as interface flux (§4). **Stated** (no data shown)
12. Results "were not particularly sensitive to how the mesh scale was computed" (§4, after Eq. (35)). **Stated** (no data shown)
13. The filter strength is found with the Illinois method (at most 20 iterations, tolerance $10^{-8}$). With the structured filter matrices of Dzanic & Witherden the filter is "only a small portion of the total compute time"; runs used up to 40 NVIDIA V100 GPUs (§4). **Stated** (no timings)
14. The tolerance $\epsilon_{\mathrm{tol}}=10^{-5}$ (unless stated) enters as $\rho-\epsilon_{\mathrm{tol}}$, $p-\epsilon_{\mathrm{tol}}$, $s_{\mathrm{mix}}-s_{\mathrm{mix},\min}+\epsilon_{\mathrm{tol}}$; for the species it is added to the initial partial densities (§4, Eqs. (31)–(32)). **Stated** (setting)
15. Near-vacuum density wave, $L^\infty$ density error at $t=1$, with the switch: rates 2.28 ($N=1$), 3.16 ($N=2$), 3.93 ($N=3$), 5.17 ($N=4$), 6.61 ($N=5$); "high-order (i.e., $p+1$) convergence was observed even at smooth extrema" (§5.1.1, Table 1). **Shown**
16. With the switch disabled (entropy constraints everywhere) the rates are 2.28, 3.16, 3.93, 5.22, 6.47 and the errors "nearly identical", so the scheme stays high order with the entropy constraints active (§5.1.1, Table 2). **Shown**
17. Two-species isentropic vortex, $N=4$, $t=T=20$ and after reversal $t=2T=40$: with the switch the roll-up is well resolved at $40^2$ elements and converges qualitatively towards $80^2$. Without it, "predictions at $N=80^2$ without the entropy switch were on the order of the much less resolved $N=20^2$ simulation that did utilise the entropy switch" (§5.1.2, Figs. 1–4). **Shown**
18. Quirk–Karni shock tube, $N=3$, $t=0.35$: convergence to a first-order Godunov reference on $5\cdot10^4$ elements, "excellent agreement at $N=200$"; the pressure-equilibrium oscillations of conservative schemes in $0.4<x<0.7$ "were not visually noticeable" (§5.1.3, Fig. 5). **Shown**
19. The pressure oscillations of conservative multi-species formulations are expected to shrink with resolution ([pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)) (§5.1.3). **Stated** (cited)
20. Helium–air shock–bubble, $N=3$ on unstructured triangles: "very good agreement" with Kundu's ninth-order upwind finite-difference solution at roughly equal solution-point spacing, at $t=0.25$ and $0.39$ (§5.1.4, Fig. 9). **Shown** (schlieren, qualitative)
21. Triple-point problem, $N=3$, $2800\times1200$: the Kelvin–Helmholtz roll-up is well resolved and "compare[s] favourably" with Kolev & Rieben (§5.1.5, Fig. 11). **Shown** (qualitative, no side-by-side figure)
22. Rayleigh–Taylor, $N=3$, $32\times32\times64$: the kinetic-energy peak grows as $\mu$ decreases ($10^{-4}$, $5\cdot10^{-5}$, $10^{-5}$) on the same mesh, which "indicates that the dissipation in the flow is primarily introduced through the physical viscosity, not the numerical stabilisation approach" (§5.2.1, Fig. 12). **Shown**
23. Taylor–Green vortex, $N=3$, $32^3$ and $40^3$: two-species runs slightly underpredict the enstrophy with respect to single-species runs, the difference shrinks with resolution, and the smooth initial interface (case B) underpredicts more than the sharp one (case C) (§5.2.2, Fig. 14). **Shown**
24. The extra dissipation of case B "may be linked to aliasing errors associated with the nonlinear description of the interface", since entropy constraints mitigate aliasing (§5.2.2). **Stated** (hypothesis)
25. Conservative multi-species formulations cannot preserve pressure equilibrium across species interfaces but predict shock speeds correctly, and are therefore "critical" at high Mach number (§1). **Stated** (cited)

# Printed slips

- Table 4 and §5.1.4, helium–air shock–bubble. The text calls the state with subscript $l$ the post-shock air, normalized to unit density and pressure, and the state $r$ the pre-shock air from Rankine–Hugoniot. But Table 4 gives L: $\rho=1$, $u=0$, $p=1$ and R: $\rho=1.37636$, $u=-0.55957$, $p=1.5698$, and the bubble is in equilibrium at $p=1$, so L is the quiescent (pre-shock) air and the labels in the text are swapped. A $M=1.22$ shock into the L state gives $\rho=1.37667$, $p=1.56956$, $\lvert u\rvert=0.39476$ with $\gamma=1.3986$, and $\rho=1.37636$, $p=1.5698$, $\lvert u\rvert=0.39473$ with $\gamma=1.4$. The printed density and pressure match $\gamma=1.4$, not the tabulated 1.3986, and the printed $u_R=-0.55957$ matches neither *(compiler check, not in the sources)*. Table 3 (Quirk–Karni) gives the consistent $u=0.3948$ for the same jump.
- Eq. (41e), Taylor–Green pressure: printed $p=p_0+\frac1{16}(\cos2x+\cos2y)(\cos(2z+2))$. For the velocity of Eqs. (41b–d), $\nabla^2p=-\partial_iv_j\partial_jv_i$ is satisfied by $\frac1{16}(\cos2x+\cos2y)(\cos2z+2)$ and not by the printed form *(compiler check, not in the sources)*; the other sources of the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) page print $\cos2z+2$.
- Eq. (34) against Eq. (27): the discrete sensor drops the absolute value of the integrated jump, so a negative jump never triggers it. It also sums over the solution-node set $S$ while the jump exists only at the interface nodes $I$ (§2.3), and $A=\sum_{j\in S}w_j$ "is the surface area of $\partial\Omega_i$".
- Eq. (25): the "else" branch sets the constraint to $0$, while the constraints must be strictly positive (Eqs. (17), (21)); the intent ("neglecting" the constraint) is clear from the text.
- Eq. (5): the viscous column is printed without a divergence, the stress $\bar\mu(\nabla\mathbf V+\nabla\mathbf V^T)-\bar\mu\frac23\nabla\cdot\mathbf V$ without an identity tensor, and the energy row omits the $-\frac23\bar\mu(\nabla\cdot\mathbf V)\mathbf V$ work term that the momentum stress implies.
- Eq. (37a) indexes the species $i\in\{1,2\}$; the paper elsewhere uses $0,\dots,n-1$, including in the same test ($c_{p,0}$, $c_{p,1}$, plots of $\alpha_0\rho_0$).
- Eq. (38): $L$ in the Rayleigh–Taylor perturbation is not defined in §5.2.1.
- Eq. (10) names $\sigma$ the partial-density-weighted sum that Eq. (8) calls $\rho\sigma$; §2.2 calls $R$ "the universal gas constant" though it carries a species index; $\sigma=500$ is reused as the Gaussian width in Eq. (36a).
- §2.3: "partitioned into $N$ elements … $\Omega=\bigcup_{N_e}\Omega_k$" ($N$ against $N_e$).
- Table 2, $N=3$: the printed rate 3.93 against 3.92 from a least-squares fit of $\log_2$ error on $\log_2N_e$ over the printed errors; all other printed rates of Tables 1–2 are reproduced by that fit *(compiler check, not in the sources)*.
- §5.1.4: "average edge lengths of $h/R=50$, 100, and 200" for the coarse, medium and fine meshes; resolution increasing with the number indicates $R/h$.

# Notation map

| Trojak & Dzanic (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $n$, $i=0,\dots,n-1$ | $N_{\mathrm s}$, $k$ (page-local) | species count and index (the entropy-filtering page counts $k=1,\dots,N_{\mathrm s}$) |
| $\alpha_i\rho_i$, $\boldsymbol{\alpha\rho}$ | $\rho Y_k$ | partial density; the paper calls $\alpha_i$ a mass fraction but uses only the product; **$\alpha$ collides with $\alpha_k$ and the blending $\alpha$** |
| $\rho$, $\rho\mathbf V$, $E$, $P$, $\rho e$ | $\rho$, $\rho v$, $E$, $p$, $\rho e$ | agrees except letters |
| $\gamma$, $\gamma_i$, $c_{p,i}$, $c_{v,i}$, $R_i$, $T$ | $\gamma$, $\gamma_k$, $c_{p,k}$, $c_{v,k}$, $R_k$, $T$ | mixture $\gamma$ by Eq. (4) |
| $\bar\mu$, $\overline{Pr}$ | $\mu$, $\mathrm{Pr}$ | mass-weighted mixture values |
| $\sigma$, $\rho\sigma$, $\sigma_{\min}$ | $s_{\mathrm{mix}}$, $s_{\mathrm{mix},\min}$ (page-local) | physical sign, minimum principle; **not the registry's convex $\eta$; $\sigma$ is also the Gaussian width and the registry's affine scaling** |
| $\sigma^*$ | $s^*_{\mathrm{mix}}$ | Eq. (33) |
| $\Gamma_1,\dots,\Gamma_4$ | $g_1,\dots,g_4$ | constraint functions; entropy is $\Gamma_3$ in Dzanic & Witherden, $\Gamma_4$ here |
| $\zeta$, $p_i$, $\psi_i$, $\hat{\mathbf u}_i$ | $\zeta_{\mathrm F}$, kept | filter strength, mode order, orthonormal modes; **$\psi$ is the registry's entropy potential** |
| $H(\cdot)$ | kept | filtering operator |
| $p$, $\mathbb P_p$ | $N$, $\mathbb P^N$ | **source $p$ is the degree, registry $p$ the pressure** |
| $S$, $I$ (node sets) | kept | solution and interface nodes |
| $S$, $S_i$ (switch) | $\mathcal S_K$ (page-local) | **$S$ collides with the source term $S(u)$** |
| $\mathbf u^-_i$, $\mathbf u^+_i$ | interior and exterior trace | $-$ = element of interest, not the registry's left/right convention |
| $h$, $A$, $w_j$ | kept | mesh scale (Eq. (35)), surface area, quadrature weight ($\mathsf w_j$ on reference elements) |
| $\epsilon$ | $\epsilon_{\mathrm{tol}}$ | constraint tolerance, not the WENO $\epsilon$ |
| $\overline{\mathbf F}$ | $h(u^-,u^+)$ | HLLC common flux |
| $k$, $\varepsilon$ | $\kappa$ (averaged), kept | volume-averaged kinetic energy; enstrophy-based dissipation rate |
| $N$, $N_e$ (tables) | $N_x$ | elements per direction |

# Reference list

45 printed references in numbered, alphabetical style ([1]–[45]), merged
complete into the [bibliography](/bibliography.md) with `citedby`
`trojak-2024`. Ref. [14] (Dzanic & Witherden, JCP 468:111501) is the
ingested source `dzanic-2022-b`. Ref. [15] is the arXiv preprint of the
ideal-MHD entropy-filtering paper and is kept apart from its published form.
Ref. [13] (Dzanic, Trojak & Witherden, arXiv:2302.13359, printed with a
doubled "arXiv:" prefix) is a different work from the ingested `dzanic-2023`.
Ref. [38] prints only an AIAA video DOI. Ref. [44] is printed "2011" with JCP
229:8917–8934. No printed duplicates; all items parsed.

# Pages created or updated

Chunk 7 (2026-10-23), cited further in chunk 8 (2026-10-23). This source is cited on:

* [Bound preservation](/properties/bound-preservation.md)
* [Density-wave advection](/benchmarks/density-wave-advection.md)
* [Entropy filtering for DG and FR](/methods/entropy-filtering.md)
* [Entropy stability](/properties/entropy-stability.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)
* [Pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)
* [PyFR](/software/pyfr.md)
* [Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md)
* [Shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)
* [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
* [Triple-point problem](/benchmarks/triple-point-problem.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
