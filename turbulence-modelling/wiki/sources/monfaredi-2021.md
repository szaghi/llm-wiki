---
type: Source
title: "Monfaredi et al. (2021) — Unsteady continuous adjoint to URANS coupled with FW-H analogy for aeroacoustic shape optimization"
description: "Unsteady continuous adjoint of a 2D Spalart–Allmaras URANS solver coupled with the permeable frequency-domain Ffowcs Williams–Hawkings analogy, verified against finite differences on a laminar cylinder and the rod–airfoil case, and used to reshape the airfoil for a 30% lower far-field noise objective."
resource: "doi:10.1016/j.compfluid.2021.105136"
source_kind: paper
authors: [Monfaredi M., Trompoukis X., Tsiakas K., Giannakoglou K.]
year: 2021
venue: "Comput. Fluids 230:105136"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2021_Crossref_Computers_amp_Fluids_Monfaredi_Unsteady_continuous_adjoint_to_URANS_coupled_with_FW-H_analo.pdf"
tags: [aeroacoustics, rans, spalart-allmaras, compressible]
timestamp: 2026-10-27T15:50:00Z
---

# Summary

Monfaredi et al. (2021) build a gradient-based aeroacoustic
shape-optimization tool for 2D unsteady compressible flow. The near field
comes from an in-house GPU URANS solver: vertex-centred finite volumes on
unstructured grids, Roe flux with the Van Leer limiter, dual time stepping
and the [Spalart–Allmaras model](/methods/spalart-allmaras-model.md) for
the eddy viscosity of a [Boussinesq](/definitions/boussinesq-hypothesis.md)
stress. The far-field sound comes from the permeable
[Ffowcs Williams–Hawkings analogy](/methods/ffowcs-williams-hawkings-acoustic-analogy.md),
solved in the frequency domain with the 2D convective Green function. The
quadrupole term is dropped, and the time-domain 2D form is avoided because
of its tail effect. The objective is $J=\int|\hat p'(\boldsymbol x_r,f)|\,df$
at a far-field receiver.

The contribution is the unsteady continuous adjoint of this whole chain.
The FW-H integral is differentiated analytically and mapped back to the time
domain through the windowed, mean-subtracted Fourier transform. The
objective then enters the adjoint mean-flow equations only as source terms
on the finite volumes on and next to the FW-H surface; the adjoint SA and
adjoint wall-distance equations are also solved. This extends the authors'
earlier inviscid FW-H adjoint to viscous, turbulent flow.

The FW-H implementation reproduces the analytical field of a monopole in
uniform flow. The adjoint sensitivities agree with central finite
differences for a laminar vortex-shedding [cylinder](/benchmarks/circular-cylinder-wake.md)
($Re=1000$, reference length not stated, $M=0.2$) and for the turbulent rod–airfoil configuration (a
rod one chord upstream of a [NACA 0012](/benchmarks/naca-0012-airfoil.md),
$Re_c=4.8\times10^5$). Earlier rod–airfoil studies mostly used 3D
[LES](/definitions/large-eddy-simulation.md) or DES with FW-H; the
comparison URANS ran [$k$-$\omega$ SST](/methods/k-omega-sst-model.md).
The adjoint field decays outside the optimization window, so the backward
integration is truncated 460 steps after it. A 50-variable free-form
deformation of the airfoil lowers $J$ by 30% in 12 cycles. The main tonal
peak drops by about 3.7 dB, while the mean drag rises and the lift falls.
The URANS baseline overpredicts the shedding Strouhal number (0.24 against
about 0.19 measured).

# Version read

Version of record (Elsevier, Comput. Fluids 230:105136; received 25 August
2020, online 3 September 2021); 14 pages, all read, equations on pp. 2–6
and p. 10 checked visually. Page 1 matches Crossref; no identity problem.

# Key claims

Registry notation; the source's $\omega$ (frequency) is written $f$ here,
and its $\mathrm k=\omega/c_\infty$ is written $k_a$ (see the Notation map).

1. Adjoint methods have a cost independent of the number of design variables (§1). **Stated**
2. Continuous adjoints are rare in aeroacoustic shape optimization although they need less memory than discrete ones; the cited aeroacoustic discrete adjoints all use automatic differentiation (§1). **Stated**
3. The paper extends the inviscid FW-H continuous adjoint of the authors' earlier work to viscous and turbulent flow by differentiating the FW-H analogy fully and solving the adjoint Spalart–Allmaras and adjoint Eikonal equations (§1, §3, §5). **Derived**
4. URANS overpredicts the shedding frequency and the spectral peak levels of the rod–airfoil case but is affordable for studying noise mitigation; per Jacob et al., a 3D URANS practically matches the spanwise-repeated 2D one (§1). **Stated**
5. In 2D the time-domain FW-H integral has a tail effect that requires an infinitely long integration, so the 2D FW-H equation (quadrupole dropped) is solved in the frequency domain with the Green function of Eq. (7) (§2.2). **Stated**
6. The quadrupole term is negligible at the low speeds treated, and dropping it avoids computing and storing a volume term (§2.2). **Stated**
7. The frequency-domain FW-H implementation "exactly" matches the analytical r.m.s. directivity of a monopole in uniform flow at 500 m ($M_\infty=0.6$; FW-H circle of radius 4 m with 150 nodes) (§2.2.1, Fig. 2). **Shown**
8. An objective at a remote receiver changes neither the adjoint boundary conditions nor the sensitivity expression; it enters the adjoint equations only as source terms on the FW-H surface and its neighbouring nodes (§3, Eqs. 31–33). **Derived**
9. Inserting the Hanning-windowed, mean-subtracted Fourier transform (Eq. 23) into the frequency-domain derivative (Eq. 22) gives the time-domain sensitivity Eq. (25) with kernels $\mathcal A_k$, $B$ (Eq. 26) (§3). **Derived**
10. The FW-H line is fixed during optimization, so the derivatives of the Green function, of its gradient and of the surface element with respect to the design variables vanish (§3). **Stated**
11. Laminar cylinder ($D=0.019$ m, $M=0.2$, $Re=1000$): $St=0.24$ and mean $C_D=1.42$, "close to" the 0.234 and 1.56 of the URANS of Cox et al. (§4.1). **Shown**
12. Hybrid URANS+FW-H pressure histories match pure CFD at receivers near the FW-H surface in both cases; the discrepancies at the start and end of the records come from the Hanning window (§4.1, Fig. 4; §4.2, Fig. 9). **Shown**
13. Cylinder: adjoint and central finite-difference sensitivities (108 FFD variables, step $10^{-7}D$) are almost identical for time-averaged lift and drag and satisfactorily close for the noise objective, the residual differences being partly finite-difference round-off that grows with the integration time (§4.1, Fig. 5). **Shown**
14. Rod–airfoil URANS: $St=0.24$, as the 2D URANS of Jacob et al., above the experimental $\approx0.19$; the tonal peak frequency (1728 Hz) is overestimated, the main peak level "adequately close" to experiment, five harmonics identified (§4.2, Fig. 10a). **Shown**
15. Rod–airfoil mean velocity at $x/c=-0.25$ agrees with the 2D URANS of ref. [38] and "seem[s] to outperform" that of Jacob et al.; at $x/c=0.25$ all URANS overpredict the measured profile relative to LES; part of the differences may come from SA here against $k$-$\omega$ SST there (§4.2, Fig. 7). **Shown**
16. The mean $C_p$ on the airfoil pressure side agrees with the 3D LES of the literature, both above experiment; the r.m.s. $C_p$ is slightly better than other 2D URANS (§4.2, Fig. 8). **Shown**
17. OASPL directivity at 1.85 m (100 receivers): the coarse grid (124,000 nodes) gives a quadrupole-like shape, the medium (161,906) and dense (240,000) grids tend to a dipole and nearly coincide, so the medium grid is used; OASPL overprediction is expected of URANS (§4.2, Fig. 10b). **Shown**
18. Outside the optimization window the only contribution to the adjoint equations is the unsteady term, so the adjoint fields decay and are convected towards the inlet backward in time (§4.2, Fig. 12). **Shown**
19. The sensitivities converge within 460 time steps after the end of the window (backward in time), so the adjoint run is truncated at 2490 steps (2030 + 460) without significant gradient error (§4.2, Fig. 13; §5). **Shown**
20. Rod–airfoil adjoint sensitivities (50 design variables) agree with central finite differences (step $10^{-7}c$) at control points 9–14 (§4.2, Fig. 14). **Shown**
21. Steepest descent with constant step $1.5\times10^{-12}$ m²s/Pa reduces $J$ by 30% after 12 cycles, with the largest drop in cycle 1 and convergence by cycle 8 (§4.2, Fig. 15a). **Shown**
22. Optimized airfoil: main PSD peak reduced by about 3.7 dB to 90.7 dB; second harmonic down by about 1.6 dB; third and fifth up by about 1.2 and 3.4 dB; fourth unchanged; the harmonic frequencies unaffected (§4.2, Fig. 16b). **Shown**
23. The optimized OASPL directivity tends to a quadrupole: insignificant reduction between 300° and 60°, amplification from 135° to 195°, considerable reduction elsewhere, largest near 90° (the receiver direction) (§4.2, Fig. 17). **Shown**
24. The optimized shape has worse aerodynamics, $\Delta C_D=0.011$, $\Delta C_L=-0.018$; lift and drag are neither objectives nor constraints (§4.2). **Shown**
25. Comparison with DES or LES and their adjoints is the next step (§5). **Stated**

The objective and its frequency-domain derivative (Eqs. 9, 21), with
$\hat p'=\hat p'_{\mathrm{Re}}+i\hat p'_{\mathrm{Im}}$:

$$J=\int|\hat p'(\boldsymbol x_r,f)|\,df,\qquad \frac{\delta J}{\delta b_i}=\int\frac{1}{|\hat p'|}\Big(\hat p'_{\mathrm{Re}}\frac{\delta\hat p'_{\mathrm{Re}}}{\delta b_i}+\hat p'_{\mathrm{Im}}\frac{\delta\hat p'_{\mathrm{Im}}}{\delta b_i}\Big)df .$$

# Printed slips

- Receiver position: §4.2 prints $\vec x_{r1}=(0.31$ m, $0.101$ m$)$, the Fig. 9 caption $(0.31$ m, $0.104$ m$)$.
- Main-peak reduction: "reduced by about 3.7 dB and drops to 90.7 dB" (§4.2) against "a 3.6 dB reduction in the main peak of the PSD" (§5).
- §4.2 calls 3456 Hz "the third harmonic", while the tonal peak is 1728 Hz and the five peaks are called "the first five harmonics"; 3456 Hz is twice 1728 Hz *(compiler check, not in the sources)*.
- $\omega$ is an angular frequency in Eqs. (5) and (7) ($\mathrm k=\omega/c_\infty$, "rad/s" in §2.2.1) but an ordinary frequency in the kernels $e^{-2i\pi\omega t}$ of Eq. (23) and $\cos(2\pi\omega t)$ of Eq. (26).
- Fig. 17 caption "radius $R=1.85$" without unit (m in the text); the monopole test switches to $\rho_0$, $c_0$; after Eq. (21) the receiver is written $\vec x_o$.
- Ref. [30] is printed without volume and with the first author as "Williams JF" (Ffowcs Williams).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $v_k$ | $u_i$ | URANS mean velocity, written without averaging brackets in the source |
| $U=[\rho,\rho v_1,\rho v_2,\rho E]$, $R_n$ | same (conservative variables, residual, page-local) | $E$ per unit mass in the source |
| $\tau_{km}=(\mu+\mu_t)(\partial_mv_k+\partial_kv_m-\tfrac23\delta_{km}\partial_\ell v_\ell)$ | $2(\mu+\mu_t)S^d_{ij}$ | viscous stress $\sigma_{ij}$ plus the Boussinesq stress $-\langle\rho\rangle(R_{ij}-\tfrac23k\delta_{ij})$, no $k$ term |
| $\mu_t$ | $\mu_t$ | from SA |
| $p'$, $\rho'$, $v'_k$ | same | perturbations from the free stream, not Reynolds fluctuations |
| $\omega$ | $f$ (frequency, page-local) | **collision** with the specific dissipation rate $\omega$ and the vorticity $\omega_i$; angular or ordinary (Printed slips) |
| $\mathrm k=\omega/c_\infty$ | $k_a$ (acoustic wavenumber, page-local) | **collision** with $k$ |
| $\hat{(\cdot)}$ | same (Fourier transform in time, page-local) | **collision:** not a test filter |
| $\beta=\sqrt{1-M_\infty^2}$ | $\beta_{\mathrm{PG}}$ (page-local) | **collision** with $\beta(\boldsymbol x)$ and $\beta^*$ |
| $f$, $H(f)$, $\delta(f)$ | $f_{\mathrm s}$ (signed distance from the FW-H surface, page-local) | **collision** with the forcing $f_i$ |
| $Q$, $F_k$, $T_{km}$ | same (FW-H monopole, dipole, quadrupole sources) | $F_k$ includes the stress $\tau_{km}$ above |
| $\hat G$, $H_0^{(2)}$, $\mathcal H(t)$ | same (page-local) | Green function, Hankel function, window |
| $J$, $b_i$, $N$ | same (objective, design variables, page-local) | **collision:** $N$ is not the polynomial degree |
| $\Psi_n$, $\tau^{adj}_{mk}$, $q^{adj}_k$, $S_{\rm FW\text{-}H}$ | same (adjoint variables, stress, heat flux, sources, page-local) | |
| $\mathcal A_k$, $B$, $T_s$, $T_O$ | same (page-local) | sensitivity kernels; simulation and optimization windows |
| $C_d$, $C_l$, $C_p$ | $C_D$, $C_L$, $C_p$ | $C_p$ is also the specific heat in Eq. (20) |
| $C$, $D$ | $c$, $D$ | chord, cylinder (rod) diameter |
| $Re$ | $Re_c$ (rod–airfoil), $Re$ (cylinder, reference length not stated) | |

# Reference list

39 printed references, numbered style ([1]–[39]). The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this slug.
Ref. [11] (the authors' Springer 2021 chapter *An unsteady
aerodynamic/aeroacoustic optimization framework using continuous adjoint*)
is a different work from this paper and is keyed `monfaredi-2021-b`.
Ref. [1] has a corporate author (EU Commission); ref. [30] is printed
"Williams JF, Hawkings DL" without volume (the Ffowcs Williams & Hawkings
1969 paper); ref. [33] is a PhD thesis. No printed duplicates; all items
parsed.

# Pages created or updated

Chunk 9 (2026-10-27). This source is cited on:

- [Circular-cylinder wake](/benchmarks/circular-cylinder-wake.md)
- [NACA 0012 airfoil](/benchmarks/naca-0012-airfoil.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Ffowcs Williams–Hawkings acoustic analogy](/methods/ffowcs-williams-hawkings-acoustic-analogy.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
