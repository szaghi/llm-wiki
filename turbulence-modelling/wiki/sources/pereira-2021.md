---
type: Source
title: "Pereira et al. (2021) — Modeling and simulation of transitional Rayleigh–Taylor flow with partially averaged Navier–Stokes equations"
description: "Applies variable-density PANS with the scale-aware BHR linear eddy-viscosity closure to transitional Rayleigh–Taylor mixing at Atwood number 0.5, compares three strategies for the resolution parameters, and finds that RANS overpredicts mixing while PANS with f_k at most 0.35 reproduces the no-closure reference."
resource: "doi:10.1063/5.0067552"
source_kind: paper
authors: [Pereira F.S., Grinstein F.F., Israel D.M., Rauenzahn R., Girimaji S.S.]
year: 2021
venue: "Phys. Fluids 33:115118"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2021_Crossref_Physics_of_Fluids_Pereira_Modeling_and_simulation_of_transitional_RayleighTaylor_flow.pdf"
tags: [pans, hybrid-rans-les, rans, transition, a-priori-a-posteriori]
timestamp: 2026-10-25T19:45:00Z
---

# Summary

Pereira et al. (2021) apply the variable-density
[partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md)
(PANS) model with the scale-aware BHR-LEVM closure (Besnard–Harlow–Rauenzahn
linear eddy-viscosity model), proposed in their companion paper (Pereira et
al., Phys. Rev. Fluids 6:084602, ref. [66]), to
[Rayleigh–Taylor mixing](/benchmarks/rayleigh-taylor-mixing.md) at Atwood
number $At=0.5$ and maximum Reynolds number about 500. The flow is
transient and transitional: a laminar linear regime, mushroom-shaped
bubbles and spikes, Kelvin–Helmholtz-driven onset of turbulence, then
turbulent mixing, with turbulent kinetic energy produced by both shear and
buoyancy. The unresolved stress is a
[Boussinesq](/definitions/boussinesq-hypothesis.md) form; the closure adds
transport equations for an unresolved length scale, the mass-flux velocity
$a_i$ and the density–specific-volume correlation $b$.

The LANL finite-volume code xRAGE (HLLC, parabolic reconstruction, low-Mach
correction, Heun time stepping, no artificial viscosity) runs five physical
resolutions on a $256^2\times768$ grid, $f_k=0$ (no closure, the reference),
0.25, 0.35, 0.50 and 1 (RANS). Three strategies fix the other resolution
parameters: S1 ($f_\varepsilon=f_a=f_b=1$), S2 ($f_a=\sqrt{f_k}$) and S3
($f_a\approx f_k/2$, $f_b=f_k$, from
[a priori](/definitions/a-priori-and-a-posteriori-testing.md) filtering of
DNS of [isotropic](/benchmarks/homogeneous-isotropic-turbulence.md) and
homogeneous variable-density turbulence).

RANS overpredicts the mixing (growth rate 0.043 against 0.025, which matches
the DNS of Livescu et al.) and disturbs even the laminar linear regime. S1
and S2 converge to the reference as $f_k$ decreases, S2 already at
$f_k\le0.35$. S3, built from fully developed turbulence, does not converge
and produces a nonphysical overshoot of $b_u$, so the a priori guidance fails
a posteriori in a transitional flow. The minimum physical resolution is set
by the need to resolve the bubbles and spikes that trigger turbulence, as
in the authors' PANS study of the transitional
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md). An effective
viscosity $\nu+\nu_t+\nu_n$, with $\nu_n$ the
[numerical](/properties/numerical-dissipation.md) part (not computed),
measures how far the closure lowers the effective Reynolds number. The
paper places PANS among [hybrid RANS/LES](/definitions/hybrid-rans-les.md)
methods, cites [implicit LES](/definitions/implicit-les.md) and
[DNS](/definitions/direct-numerical-simulation.md) results for the same
flow, and contrasts it with [LES](/definitions/large-eddy-simulation.md).

# Version read

arXiv preprint arXiv:2108.06423v2 [physics.flu-dyn], 19 October 2021, 22
pages, all read (equations on pp. 4–6 and 18 checked visually); not the
typeset version of record. Some sentences are printed in blue (revision
marks, e.g. pp. 6 and 18). The DOI is not printed on the arXiv copy. The
arXiv title capitalises and hyphenates differently ("Modeling and
Simulation of Transitional Rayleigh-Taylor Flow with Partially-Averaged
Navier-Stokes Equations"); authors and order match the published version.
Section, equation and figure numbers on this page are those of the arXiv v2.

# Key claims

1. PANS BHR-LEVM predicts the spatio-temporal development of the transitional Rayleigh–Taylor flow at $At=0.5$, $Re_{\max}\approx500$ with results comparable to LES/DNS at much lower physical resolution, "by resolving only a fraction of the turbulent spectrum"; with S2 this requires $f_k\le0.35$ (Abstract; §V). **Shown**
2. The reference ($f_k=0$) gives an averaged growth rate of the mixing-layer half-width $\alpha_b\approx0.025$, "matching the value obtained in the DNS study of Livescu et al. [56]" (§IV.2, Table II). **Shown**
3. RANS ($f_k=1$) gives $\alpha_b=0.043$ against 0.025; the mixing-layer height $h$ is initially thinner, overpredicted in the late nonlinear regime and poorly predicted after $t\approx2$ (§IV.2, Table II, Fig. 8). **Shown**
4. The RANS closure has "a meaningful impact on the flow dynamics in the linear regime", where the flow is laminar and the turbulent stresses should be negligible (§IV.2). **Shown**
5. With S1 the accuracy improves monotonically as $f_k$ decreases and $f_k=0.25$ agrees well with the reference; discrepancies at $t>20$ are attributed to $f_a=1$ (§IV.2, Fig. 8a). **Shown** (attribution **Stated**)
6. S2 gives the smallest comparison errors; at $f_k=0.25$, $\alpha_b=0.024$ against 0.025; $f_k=0.35$ with S2 gives smaller comparison errors than $f_k=0.25$ with S1 (§IV.2, Fig. 8b, Table II). **Shown**
7. S3 has large comparison errors and does not converge to the reference as $f_k$ decreases; with $f_k<0.50$ it had robustness issues "requiring a CFL number not exceeding 0.5", which grew with grid refinement (§IV.2). **Shown**
8. RANS gives linear mixture-fraction profiles (a higher global mixing rate), while $f_k=0$ and $f_k=0.25$ with S2 give nonlinear profiles in close agreement (§IV.2, Fig. 9). **Shown**
9. Molecular mixing parameter: the reference has $\theta\approx0.26$ at $t=0$, rising sharply for $t\le5$ and reaching about 0.8 at $t\approx25$; RANS reaches 0.95 before $t=5$ and tends to one (§IV.2, Fig. 10). **Shown**
10. The effective viscosity $\nu_e=\nu+\nu_t+\nu_n$ (Eq. 23) and the effective Reynolds number $Re_e=V_oL_o/\nu_e$ (Eq. 22) are "crucial to the simulation of problems highly dependent on Re and flow regime" (§IV.3.1). **Stated** (citing [67, 92, 93])
11. At $t=25$ the maximum planar-averaged $\nu_e/\nu$ (excluding $\nu_n$) falls from 20,737 at $f_k=1$ to 1376 (S1) and 408 (S2) at $f_k=0.25$; with S3 it grows strongly after $t\approx3$ for $f_k<0.50$ (§IV.3.1, Fig. 11). **Shown**
12. In RANS, $\nu_e/\nu$ grows at $t=20$ from about 1 to $10^4$ across the mixing layer; in RANS and at $f_k=0.25$ with S2 the peak lies on the light-fluid side, moving further into it as $f_k$ decreases (§IV.3.1, Fig. 12). **Shown**
13. With $f_\varepsilon=1$ the prescribed ratio of unresolved to RANS eddy viscosity is $f_{\nu}=f_k^2$ (Eq. 24); the effective ratio $\nu_t/(\nu_t)_{f_k=1}$ (Eq. 25) does not match it, because the flow is transient and sensitive to memory effects (§IV.3.1, Fig. 13). **Derived** (Eq. 24) / **Shown** (mismatch). From $\nu_t=c_\mu\ell_u\sqrt{k_u}$ and $f_\ell=f_k^{3/2}/f_\varepsilon$, $\nu_t/\nu_{t,\mathrm{RANS}}=f_k^2/f_\varepsilon$ *(compiler check, not in the sources)*.
14. The RANS $a_{2u}$ peaks on the heavy-fluid side and grows in time, against DNS (Livescu et al. [32, 56]) and the $f_k=0$ run, but consistently with Banerjee et al. [63] using a simplified BHR-LEVM; decreasing $f_k$ with S2 moves the peak to the light side (§IV.3.2, Fig. 14). **Shown**
15. The RANS $b_u$ grows to nearly 0.5 at $t=20$, its maximum moves to the heavy side, and it is overpredicted (§IV.3.2, Fig. 14). **Shown**
16. With S3, $b_u$ shows "a steep overproduction" at $t=2.5$ that later affects $a_{iu}$ and $k_u$; the cause is choosing $f_a$, $f_b$ for high-intensity turbulence at early stages, which makes S3 "physically inconsistent" (§IV.3.2). **Shown** (cause **Stated**)
17. Dynamic strategies for the resolution parameters may be needed to set $f_a$ and $f_b$ consistently at different flow stages (§IV.3.2, §V). **Stated**
18. Shear-to-total production ratio at $x_2=0$: shear and buoyancy contribute similarly at first; the peak grows from 0.51 ($f_k=1$) to 0.88 ($f_k=0.25$, S2) and occurs later; at $t=25$ the ratio is 0.02 and 0.30 (§IV.3.3, Fig. 15). **Shown**
19. Coherent structures at $t=2.5$ are indistinguishable from the reference for $f_k\le0.35$ (S2); larger $f_k$ dissipates them, i.e. low-resolution runs overpredict the unresolved stresses (§IV.3.4, Fig. 16). **Shown**
20. The spikes and bubbles that lead to the onset of turbulence must be resolved and set the minimum physical resolution ($f_k\le0.35$ with S2), "reiterat[ing] the findings of Pereira et al. [43, 65, 92, 93]" (§IV.3.4, §V). **Shown** / **Stated**
21. Resolved spectra at $x_2=0$: for $f_k\le0.35$ an inertial range exists up to $t=20$; decreasing $f_k$ lengthens it without much effect on the energy-containing scales; only $f_k=0$ resolves viscous scales; $f_k>0.35$ lowers the energy at all wavenumbers (§IV.3.5, Fig. 17). **Shown**
22. From a priori filtering of forced-isotropic DNS, $f_\varepsilon=1$ "is adequate for practical computations, i.e., $f_k\ge0.20$" (§III, Fig. 4a; results of [66]). **Shown** (in [66], reproduced here)
23. Grid study at $f_k=0$: $128^2\times384$ and $256^2\times768$ give negligible differences in $h$ until $t\approx15$ and small ones afterwards; $256^2\times768$ and $512^2\times1536$ (CFL 0.8) give nearly identical $h$; $64^2\times192$ cannot predict the shape of $h(t)$ (App. B, Fig. 18). **Shown**
24. Survey: experimental $\alpha_b$ values are much larger than simulated ones; DNS varies little while ILES spans a broad range, attributed (besides initial conditions) to assumptions such as inviscid fluid or one- and two-dimensional flow (§I, Fig. 1). **Shown** (survey) / **Stated** (attribution)

## Closure as printed, in registry notation

The unresolved stress (Eq. 5) is printed with the negative sign convention,
$\tau^1(V_i,V_j)=2\nu_u\{S_{ij}\}-\tfrac23k_u\delta_{ij}$; in the registry's
positive-trace form it is $\tau_{ij}=\tfrac23k_u\delta_{ij}-2\nu_t\tilde S_{ij}$,
with $\nu_t=c_\mu\ell_u\sqrt{k_u}$ (Eq. 6; $\ell_u$ the source's $S_u$) and $\tilde S_{ij}$ the Favre-filtered
strain. Six transport equations (Eqs. 7–10) carry $k_u$, the length scale
$\ell_u$, the three components of $a_i=\overline{\rho'u_i'}/\bar\rho$ and
$b=-\overline{\rho'(1/\rho)'}$ (Eqs. 11–12), with shear production
$-\bar\rho\,\tau^1\partial_j\tilde u_i$ as printed and buoyancy production
$a_j\partial_j\bar p$ (Eqs. 17–18). The resolution parameters are
$f_\phi=\phi_u/\phi$ for $k$, $\varepsilon$, $a_i$, $b$, and $f_S=f_k^{3/2}/f_\varepsilon$
(Eqs. 19–21). No coefficient values are printed; they are deferred to [66].

# Printed slips

- **CFL limit.** §II sets the maximum instantaneous CFL "equal to 0.5" for all runs, while §IV.2 says the S3 runs with $f_k<0.50$ had robustness issues "requiring a CFL number not exceeding 0.5", and App. B runs the finest grid at CFL 0.8. Which CFL each run used is unclear.
- **Monotonicity against Table II.** §IV.2 states that with S1 "the accuracy of the simulations improves monotonically with $f_k$" and that $f_k=0.35$ with S2 gives smaller errors than $f_k=0.25$ with S1 (both judged on $h(t)$, Fig. 8). Table II prints for S1 $\alpha_b=0.027$, 0.012, 0.016 at $f_k=0.50$, 0.35, 0.25, and 0.015 for S2 at $f_k=0.35$, against the reference 0.025.
- **Name of $\alpha_b$.** §I calls it the "growth rate of the lower interface", Fig. 1 caption and App. A the growth rate of the "mixing-layer half-width", while $h$ in Eq. A7 is the full 5%–95% height. If $h=\alpha\,At\,g\,t^2$, Eq. A9, $\alpha_b=\dot h^2/(4ghAt)$, returns $\alpha$, the coefficient of the full height *(compiler check, not in the sources)*.
- **Sign of the shear production.** Eq. 17 prints $\mathcal P_{s_u}=-\langle\rho\rangle\tau^1(V_i,V_j)\,\partial\{V_i\}/\partial x_j$ with $\tau^1=2\nu_u\{S_{ij}\}-\tfrac23k_u\delta_{ij}$ (Eq. 5). With that sign the eddy-viscosity part of the production, $-2\bar\rho\nu_t\tilde S_{ij}\tilde S_{ij}$, is negative; the registry form $-\bar\rho\big(\tfrac23k_u\delta_{ij}-2\nu_t\tilde S_{ij}\big)\partial_j\tilde u_i$ is positive, so either Eq. 5 or Eq. 17 carries a sign slip *(compiler check, not in the sources)*.
- **Index order.** §IV.3.2 prints "$a_{ui}$" once, $a_{iu}$ elsewhere.
- **Undefined symbol.** §IV.3.5 "At later times, $t\ge20$, $k_r$ starts decaying": $k_r$ is not defined; the spectrum is $E_r(k)$ in the Fig. 17 caption and $E(k_r)$ in App. A.
- **Reference list.** [31] "International Journal of Herat and Mass Transfer"; [36] first author "Konnikakis" while [55] prints "Kokkinakis" with the same initials and co-authors; [49] "Physical D: Nonlinear Phenomenon"; [55] "International Journal of Heat and Fluids Flow"; [60] authors "B. Basara and Z. P. S. Girimaji" and [64] "R. M. R. J. R. Ristorcelli" (garbled author lists); [5] "Usar Minor"; [80] Reynolds, Phil. Trans. R. Soc. London 186:123, printed with the year 1985; [81] no page.

# Notation map

| Pereira et al. (2021) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\langle\Phi\rangle$, $\phi$ | $\bar\Phi$ (PANS filter), $\Phi-\bar\Phi$ | **collision:** the source's angle brackets are the resolved (filtered) part, not a Reynolds average; they reduce to the Reynolds average only at $f_k=1$ (Eq. 15) |
| $\{\Phi\}=\langle\rho\Phi\rangle/\langle\rho\rangle$, $\phi^*$ | $\tilde\Phi$, $\Phi-\tilde\Phi$ | density-weighted resolved part; reduces to the Favre average at $f_k=1$ (Eq. 16) |
| overbar (Eq. 15; App. A) | $\langle\cdot\rangle$ | Reynolds average in Eq. 15; $x_1$–$x_3$ planar average in App. A |
| $V_i$ | $u_i$ | velocity; $x_2$ is the vertical (gravity) direction |
| $\{S_{ij}\}$ | $\tilde S_{ij}$ | resolved strain, not defined explicitly |
| $\tau^1(V_i,V_j)$ | $-\tau_{ij}$ | **sign:** printed with the negative convention, trace $-2k_u$ |
| $\nu_u$ | $\nu_t$ | unresolved eddy viscosity, as on the PANS page |
| $\nu_n$, $\nu_e$, $Re_e$ | (numerical viscosity, effective viscosity, effective Reynolds number) | page-local |
| $k_u$, $k_t$; $\varepsilon_u$, $\varepsilon_t$ | $k_u$, $k$; $\varepsilon_u$, $\varepsilon$ | unresolved and total |
| $S_u$, $S_t$ | $\ell_u$, (total length scale) | unresolved and total dissipation length scale, as on the PANS page; **collision:** not a strain rate |
| $f_k$, $f_\varepsilon$, $f_{a_i}$ ($f_a$), $f_b$, $f_S$ | $f_k$, $f_\varepsilon$, $f_a$, $f_b$, $f_\ell$ (page-local on the PANS page) | |
| $f_{\nu_u}$ | (unresolved-to-RANS eddy-viscosity ratio) | |
| $a_{i_u}$, $b_u$ | $a_i$, $b$ (page-local on the PANS page) | unresolved mass-flux velocity, density–specific-volume correlation |
| $\mathcal P_{s_u}$, $\mathcal P_{b_u}$, $\mathcal E_u$ | (shear and buoyancy production of $k_u$, $\bar\rho\varepsilon_u$) | |
| $c_\mu$, $c_2^*$, $c_1$, $c_4$, $c_{a_1}$, $c_b$, $\sigma_k$, $\sigma_S$, $\sigma_a$, $\sigma_b$ | model constants | values not printed |
| $At$, $\rho_h$, $\rho_l$ | (Atwood number, heavy and light densities) | |
| $h$, $\alpha_b$, $\theta$, $\overline\chi_1$ | (mixing-layer height, growth rate, molecular mixing parameter, mixture fraction) | **collision:** $\theta$ is not the momentum thickness; $h$ is not the element size |
| $Re=\dot hh/\nu$ | $Re$ | based on the mixing-layer height and its growth rate |
| $E_r(k)$ | $E(k)$ | resolved spectrum |
| $\lambda_2$ | (Jeong–Hussain vortex criterion) | not the Taylor microscale |

# Reference list

98 printed references in numbered style, in order of first citation, all
merged complete into the [bibliography](/bibliography.md) with `citedby`
this slug. Pre-publication items keep their own entries (ref. [43],
submitted, arXiv:2103.09899; [57], in preparation; [98], to be submitted).
Ref. [26] (Pereira, Eça, Vaz & Girimaji 2021, Arch. Comput. Methods Eng.)
and four further 2021 works of the same first author (refs. [43], [48], [65],
[66]) are different works whose printed-order key would collide with this
slug, so they carry suffixed keys and the bare key `pereira-2021` denotes
this source. The garbled author lists of refs. [60] and [64] and the year
1985 of ref. [80] are recorded as printed (see Printed slips). ASME V&V
20-2009 is a corporate entry. No printed duplicates.

# Pages created or updated

Chunk 2 (2026-10-25), cited further in chunk 15. This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Rayleigh–Taylor mixing](/benchmarks/rayleigh-taylor-mixing.md)
- [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Vortex identification criteria](/definitions/vortex-identification-criterion.md)
- [Partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
