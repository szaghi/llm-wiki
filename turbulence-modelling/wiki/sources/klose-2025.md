---
type: Source
title: "Klose et al. (2025) — The Unsteady Shock–Boundary Layer Interaction in a Compressor Cascade—Part II: High-Fidelity Simulation"
description: "Implicit LES with a split-form DGSEM and subcell finite-volume shock capturing of the transonic TEAMAero compressor cascade, studying low-frequency shock buffet: span and resolution sensitivity, URANS (SST with γ-Re_θ) deficiencies, and an SBLI mechanism from space–time diagrams and SPOD."
resource: "doi:10.1115/1.4067097"
source_kind: paper
authors: [Klose B.F., Morsbach C., Bergmann M., Munoz Lopez E.J., Hergt A., Kügeler E.]
year: 2025
venue: "J. Turbomach. 147:091002"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2025_Crossref_Journal_of_Turbomachinery_Klose_The_Unsteady_ShockBoundary_Layer_Interaction_in_a_Compressor.pdf"
tags: [implicit-les, dg, shock-capturing, turbomachinery, transition, rans]
timestamp: 2026-10-26T20:47:00Z
---

# Summary

Klose et al. (2025) simulate the Transonic Cascade TEAMAero (TCTA), a linear
transonic [compressor cascade](/benchmarks/compressor-cascade.md) measured at
DLR, at its aerodynamic design point: inlet Mach number $M=1.21$, chord
Reynolds number $Re_c=1.35\times10^6$, inlet flow angle $145.7°$. A normal
shock stands at mid-chord on the suction side and oscillates at low frequency
(buffet) over a laminar, transitional boundary layer and its shock-induced
[separation bubble](/definitions/laminar-separation-bubble.md), a case of
[shock–boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md).

The scale-resolving runs are an [implicit LES](/definitions/implicit-les.md)
with the DG solver of DLR's [TRACE](/software/trace.md): a nodal
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md) on
Legendre–Gauss–Lobatto nodes with $N=3$, Chandrashekar's entropy-conserving
split form with its matching Riemann solver (see
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md)),
BR1 viscous fluxes, explicit third-order Runge–Kutta, and the
[subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md)
of Hennemann et al. driven by the dilatation–vorticity sensor of Fernandez et
al. The low-fidelity comparison is a second-order finite-volume URANS with the
[$k$-$\omega$ SST model](/methods/k-omega-sst-model.md) (Kato–Launder
production) and the Langtry–Menter $\gamma$-$Re_\theta$
[transition model](/methods/local-correlation-based-transition-model.md).

On a coarse grid, spans of 5, 10 and 20% chord leave the buffet frequency
($St=0.163$–$0.165$) and the mean shock position nearly unchanged, while the
maximum oscillation amplitude falls (0.278, 0.172, 0.158) and the separation
bubble shrinks. A refined 10%-span LES (375M degrees of freedom) differs
mainly downstream of the shock, matches the measured isentropic Mach number
slightly better, and has a larger amplitude (0.231). The URANS captures the
frequency (0.161) but places the shock upstream, with less than half the
LES20 amplitude and a mostly laminar suction side. All simulations give
$St\approx0.16$ against about 0.14 measured. The authors "assume" that the
[numerical dissipation](/properties/numerical-dissipation.md) of URANS and,
to a lesser extent, of the coarse LES damps the structures that drive the
larger oscillations. Snapshots,
space–time pressure diagrams and spectral proper orthogonal decomposition
(SPOD) show velocity perturbations travelling upstream through the subsonic
boundary layer as the bubble grows, producing oblique compression waves at
the buffet harmonics, driven by shocklets from the pressure side.

# Version read

ASME Accepted Manuscript (accepted-manuscript repository cover sheet, CC BY,
line-numbered layout, manuscript number TURBO-24-1138, dated 29 October 2024;
version of record online 7 November 2024), 13 PDF pages (cover sheet, 10
manuscript pages, 2 pages of figure and table lists), all read; Table 1,
Eq. 1, Table 2 and Figs. 2, 8–9 were checked visually. The manuscript prints
"Part 2" and a plain hyphen in "Shock-Boundary"; Crossref has "Part II" and an
en dash. Same work (the cover sheet carries the DOI). Locations are by
section, equation, table and figure.

# Key claims

1. The flow at the TCTA design point ($Re_c=1.35\times10^6$, $M=1.21$) is computed with a high-order DGSEM with finite-volume subcell shock capturing as an implicit LES over several buffet cycles (Abstract, §1, §3). **Stated**
2. The LES uses $N=3$ ("4th order accurate") on a coarse grid of 47 319 elements per $x$-$y$ plane (span study) and a refined grid of 108 564 elements per plane (final LES) (§3). **Stated**
3. Table 1: LES5, LES10, LES20 have 54.6, 109.0, 218.0M degrees of freedom on 4096, 8192, 16 384 MPI ranks at 15 583, 30 933, 77 950 CPU-hours per convective time $t_c$; LES10-HR has 375.2M on 16 384 ranks at 152 850 CPU-hours per $t_c$; URANS 0.12M on 1024 ranks at 74.6. Averaging windows 60.0, 40.0, 40.0, 75.0, 50 $t_c$; time steps $\Delta t/t_c=11.2\times10^{-6}$ (coarse LES), $7.5\times10^{-6}$ (LES10-HR), $27.9\times10^{-6}$ (URANS) (Table 1). **Stated**
4. Arc-length-averaged cell sizes in wall units divided by $N$: coarse $\Delta x^+\approx39.7$–$41.2$, $\Delta y^+\approx1.96$–$2.03$, $\Delta z^+\approx30.2$–$31.4$; LES10-HR 25.5, 1.39, 21.4. Excluding leading and trailing edges the maxima are 65, 2.5, 40 (coarse) and 35, 2, 25 (refined); "the resolution is deemed sufficient for LES" (§3, Fig. 2, Table 1). **Stated**
5. No inflow turbulence is prescribed: the measured level is below 1% and "the effects are assumed to be minor at most" (§3). **Stated**
6. The suction-side boundary layer is laminar up to the shock at mid-chord; planar shocklets travel upstream in the passage and intermittently transition the laminar pressure-side boundary layer through an adverse pressure gradient (§4, Fig. 3). **Shown**
7. The time-averaged flow has a slender separation bubble under the shock and a large recirculation zone extending to the trailing edge, "indicating an open separation bubble" (§4, Fig. 4). **Shown**
8. Span study: buffet frequency $St$ = 0.165, 0.164, 0.163 and mean shock location 0.537, 0.531, 0.528 (chord fractions) for LES5, LES10, LES20, while the maximum amplitude (0.278, 0.172, 0.158) and its standard deviation (0.065, 0.054, 0.046) decrease with span (§5, Table 2, Fig. 5c). **Shown**
9. LES5 has lower isentropic Mach number upstream of the shock, higher downstream, a larger trailing-edge separation and more blockage; LES10 and LES20 differ only in separation, reattachment and transition of the upstream bubble and converge for $x_c/c>0.7$; the bubble shrinks as the span grows. The deviations are within the confidence intervals and longer runs are needed (§5, Figs. 5–6). **Shown**
10. This partly agrees with Touber & Sandham (2009) (taller bubbles in narrower domains), but the buffet frequency "appears to be less dependent on the bubble size"; their $St_{\mathrm{sep}}=fL_{\mathrm{sep}}/U_{\mathrm{ref}}\approx0.03$ gives $L_{\mathrm{sep}}/c\approx0.18$, within the observed $0.12\le L_{\mathrm{sep}}/c\le0.22$ (§5). **Shown**/**Derived**
11. LES10-HR against LES10: minor differences confined to the separated region downstream of the shock ($x_c/c>0.6$), where LES10-HR has a slightly higher isentropic Mach number and matches the experiment better (§6, Fig. 7a). **Shown**
12. URANS deviates from LES for $x_c/c>0.3$, misses the plateau at $0.3<x_c/c<0.4$, predicts an earlier shock, under-predicts the pressure-side isentropic Mach number up to $x_c/c\approx0.6$ and predicts a mainly laminar flow with much lower $C_f$, whereas the LES is driven by intermittent turbulence (§6, Fig. 7). **Shown**
13. Both LES show an earlier drop of suction-side $C_f$ at $x_c/c\approx0.2$, driven by intermittent boundary-layer thickening that produces an oblique shock; the URANS suction side stays unperturbed up to $x_c/c=0.3$ (§6, Fig. 7b). **Shown**
14. All simulations give $St\approx0.16$, which "slightly overestimates the experimental values of approximately 0.14" (§6, Table 2, Fig. 7c, §8). **Shown**
15. URANS needs $\Delta t/t_c=2.8\times10^{-5}$ "because the shock oscillation magnitude and frequency are otherwise not correctly predicted" (§6). **Stated** (no larger-step run shown)
16. URANS mean shock location 0.504 and amplitude 0.072, less than half that of LES20 (0.158); the LES10-HR amplitude (0.231) exceeds LES10 (0.172) (§6, Table 2). **Shown**
17. The authors "assume that the increased numerical dissipation of the URANS and, to a lesser extent, the coarser LES, damps out flow structures that are driving the larger shock oscillations in the LES10-HR"; the coarse solutions "should be considered under-resolved" (§6). **Stated**
18. The measured amplitude 0.13 "agrees very well with the LES20 case", although a high-resolution LES20 "would presumably show larger deviations as well"; a possible cause of the simulation–experiment differences is the wind-tunnel span of $1.68c$, which allows spanwise modulation of the shock (§6). **Stated**
19. One buffet period is about $6.3\,t_c$. The cycle: most-forward shock; adverse pressure gradient separates and reattaches the boundary layer; upstream-travelling disturbances in the subsonic boundary layer thicken it and produce an intermittent oblique compression wave; the shock moves downstream, the separation fails to reattach; shocklets transition the pressure side; the separated region grows and the flow above turns locally supersonic; the separation point creeps upstream, the compression wave lowers the downstream Mach number; the shock is pushed upstream and the recirculating fluid is shed as a large vortex (§7.1, Figs. 8–9). **Shown** (qualitative)
20. "The underlying SBLI mechanics are identical for the two LES" (LES10-HR, LES20); LES10-HR has a larger separated region, and the waves and shocklets of LES20 "appear more diffused, given the increased numerical dissipation in this case" (§7.1). **Shown**
21. Space–time pressure diagrams: in the subsonic region ($x_c/c>0.6$) pressure waves travel both ways, the thin negative-slope streaks being shocklets; in the supersonic region ($0.1<x_c/c<0.5$) only downstream propagation, except thin lines that are the oblique compression waves, which appear driven by the shocklets (§7.2, Fig. 10). **Shown**
22. Near the wall ($0.003c$) the sonic line is dominated by a high-frequency oscillation driven by the boundary layer and oblique shocks, with secondary spectral peaks at $ft_c=0.32$ and $0.48$ (§7.2, Figs. 11–12). **Shown**
23. SPOD (velocity fluctuations, kinetic-energy norm with uniform weights, 1008 snapshots over 75 $t_c$, 7 blocks of 250 with 50% overlap, Hamming window) gives a distinct dominant mode at $ft_c=0.16$, well separated from the second mode, and further peaks at the harmonics 0.32, 0.48, 0.64 (§7.3, Eqs. 2–5, Fig. 13). **Shown**
24. The 0.16 mode is the streamwise back-and-forth motion of the shock in $u'$, with a sign reversal under the shock attributed to strong oblique waves; the 0.48 and 0.64 modes are the oblique compression wave as a vertical displacement in $v'$ (§7.3, Fig. 14). **Shown**
25. Mechanism: as the shock reaches its most downstream position the bubble grows and forces velocity perturbations upstream through the subsonic boundary layer; bubble fluctuations at higher frequencies, with upstream-travelling shocklets, cause the oblique compression waves (§7.3, §8). **Shown** (interpretation)
26. Conclusion: "a very good match with the experimental campaign … with a near exact match of the isentropic Mach number and a close agreement of the shock oscillation frequency" (§8). **Shown**

The shock-capturing blend (Eq. 1), with $\boldsymbol q$ the conserved variables and $\boldsymbol R$ the inviscid residual operators:
$$\frac{\partial\boldsymbol q}{\partial t}+\alpha\,\boldsymbol R^{\mathrm{FV}}(\boldsymbol q)+(1-\alpha)\,\boldsymbol R^{\mathrm{DG}}(\boldsymbol q)=0,\qquad\alpha\in[0,1],$$
$\alpha$ set by the shock indicator; the time and space relaxation factors of the sensor are both 0.7 (§2). **Stated**

# Printed slips

- §5: "upstream of the shock (0 > $x_c/c$ 0.4)", a malformed inequality.
- §6: "($x_c/c$ <,0.3)", a stray comma.
- §2: "Bassy-Rebay-1 (BR1) scheme [40]"; reference [40] prints "Bassi, F. and Rebay, S.".
- Nomenclature: $t$ is defined both as "pitch length [m]" and as "time [s]"; $N$ is the polynomial order (§2) and the SPOD state dimension (Eqs. 2–4).
- Table 1 footnote writes $t_c=c/U_{\mathrm{in}}$, §3 writes $t_c=c/U_{\mathrm{ref}}=c/\lVert\boldsymbol u_{\mathrm{in}}\rVert_2$ (same meaning, different symbol).
- Title "Part 2" on the manuscript, "Part II" in the published metadata.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathrm{Ma}$, $\mathrm{Ma_{in}}$ | $M$ | inlet Mach number at the measurement plane MP1 |
| $\mathrm{Ma_{is}}$ | (isentropic surface Mach number) | |
| $\mathrm{Re}$, $\mathrm{Re_{in}}$ | $Re_c$ | chord-based, inlet reference |
| $St=ft_c$ | $St$ | chord-based; $St_{\mathrm{sep}}$ uses $L_{\mathrm{sep}}$ |
| $N$ | $N$ | polynomial degree; **collision:** also the SPOD state dimension (Eqs. 2–4) |
| $\alpha$ | $\alpha$ | DG/FV blending factor, $\alpha=1$ pure FV, agrees |
| $\mathbf q$, $\mathbf R^{\mathrm{DG}}$, $\mathbf R^{\mathrm{FV}}$ | (conserved variables, inviscid residuals) | |
| $\xi$, $\eta$, $\zeta$ | $x$, $y$, $z$ (wall-tangent, wall-normal, spanwise) | **collision:** $\xi$ is the reference coordinate and $\eta$ the Kolmogorov length in the registry |
| $\Delta\xi^+$, $\Delta\eta^+$, $\Delta\zeta^+$ | $\Delta x^+$, $\Delta y^+$, $\Delta z^+$ divided by $N$ | overbar = arc-length average along the blade surface |
| $\overline{x_s/c}$ | $\langle x_s\rangle/c$ | **collision:** overbar is a time average, not an LES filter |
| $t$ | (pitch, 0.065 m) and time | **collision** printed in the nomenclature |
| $c$, $t_c=c/U_{\mathrm{ref}}$ | (chord 0.1 m, convective time) | |
| $\beta_{\mathrm{in}}$, $\beta_{\mathrm{st}}$ | (inlet flow angle, stagger angle) | **collision:** not the field-inversion $\beta$ |
| $x_c$, $s$ | (chord-aligned coordinate, surface arc length) | |
| $\Delta_{\max}(x_s/c)$, $\mathrm{std}(x_s/c)$ | (maximum amplitude and standard deviation of the shock position) | **collision:** $\Delta$ is not a filter width |
| $L_z$, $L_{\mathrm{sep}}$ | (span of the domain, separation length) | |
| $C_f$ | $C_f$ | |
| $Q=(\lVert\boldsymbol\Omega\rVert^2-\lVert\mathbf S\rVert^2)/2$ | Q-criterion with $\Omega_{ij}$, $S_{ij}$ | norms not specified in the source |
| $u'$, $v'$, $w'$ | $u'$, $v'$, $w'$ | fluctuations about the time mean |
| $\mathbf X$, $\tilde{\mathbf X}$, $\tilde{\mathbf C}$, $\mathbf W$, $\boldsymbol\Phi$, $\boldsymbol\Lambda$, $N_{\mathrm{blk}}$, $N_{\mathrm{fft}}$ | (SPOD snapshot matrix, Fourier blocks, cross-spectral matrix, weights, modes, eigenvalues, block and frequency counts) | Schmidt & Colonius notation, page-local; **collision:** $\boldsymbol\Lambda$ is not the slip-length tensor of the wall-model pages |

# Reference list

51 printed references, numbered style, titles printed, DOIs only for some
conference papers. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Reference [51]
(Morsbach et al. 2024, "Modal analysis of high-fidelity simulations in
turbomachinery") is a different work from the ingested Morsbach et al. (2024)
and takes the key `morsbach-2024-b`; [42] (Fernandez et al. 2018) and [51] print no venue,
[31] prints no publisher or pages, [26] is a web page. No printed duplicates.

# Pages created or updated

Chunk 6 (2026-10-26), cited further in chunk 7. This source is cited on:

- [Compressor cascades](/benchmarks/compressor-cascade.md)
- [Shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Laminar separation bubble](/definitions/laminar-separation-bubble.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [Local-correlation-based transition models](/methods/local-correlation-based-transition-model.md)
- [Subcell finite-volume shock capturing for DG](/methods/subcell-finite-volume-shock-capturing.md)
- [Entropy conservation and entropy stability](/properties/entropy-conservation.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [TRACE](/software/trace.md)
