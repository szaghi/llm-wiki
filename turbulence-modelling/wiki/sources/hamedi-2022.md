---
type: Source
title: "Hamedi & Vermeire (2022) — Optimized Filters for Stabilizing High-Order Large Eddy Simulation"
description: "Modal filtering as the sole stabilization of under-resolved flux-reconstruction LES: a time-step-normalized filter operator whose cumulative strength is independent of the time step, and exponential-filter parameters optimized over more than 14,000 inviscid Taylor–Green runs, validated on isentropic vortex, Taylor–Green, channel and stalled-airfoil cases."
resource: "doi:10.1016/j.compfluid.2021.105301"
source_kind: paper
authors: [Hamedi M., Vermeire B.C.]
year: 2022
venue: "Comput. Fluids 237:105301"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Computers_amp_Fluids_Hamedi_Optimized_Filters_for_Stabilizing_High-Order_Large_Eddy_Simu.pdf"
tags: [flux-reconstruction, filtering, implicit-les, numerical-dissipation, high-order]
timestamp: 2026-10-27T15:53:00Z
---

# Summary

Hamedi & Vermeire (2022) stabilize under-resolved high-order
[flux reconstruction](/methods/flux-reconstruction.md) against
aliasing-driven non-linear instability with
[explicit modal filtering](/methods/explicit-modal-filtering.md), which
costs far less than de-aliasing, limiters or
[artificial viscosity](/methods/artificial-viscosity-shock-capturing.md)
(the latter needs a sensor), and which earlier work (Park et al. 2017)
found harmful to accuracy. The scheme run is the FR variant whose Radau
correction functions recover nodal DG (see the
[DGSEM page](/methods/discontinuous-galerkin-spectral-element-method.md)),
with the Rusanov flux; FR also recovers the
[spectral difference method](/methods/spectral-difference-method.md), and
[entropy-stable](/properties/entropy-conservation.md) schemes are mentioned
as a costlier alternative.

Two contributions. First, a time-step-independent filter: the diagonal modal
filter matrix $\Lambda$ is raised to the power $1/n$ with
$n=T_{\mathrm{char}}/\Delta t$, so that applying the normalized filter every
step has the cumulative effect of applying $\Lambda$ once per characteristic
time. Second, the parameters of an exponential filter (cut-off degree,
damping, order) are optimized by bisection over more than 14,000 inviscid
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) runs on a $16^3$
degree-of-freedom mesh, $N=3$–5, $M=0.1$–0.5: the weakest filter that keeps
pressure and density physical to $20T_{\mathrm{char}}$ is chosen, damping the
high modes as much as possible and leaving the low modes unchanged. The
optimum order is always 16.

The filters preserve the super-accurate convergence on the isentropic
vortex, slightly raise the [numerical dissipation](/properties/numerical-dissipation.md)
of the Taylor–Green vortex at $Re=1600$ on linear and curved meshes (curved
Jacobians being a geometric aliasing source, see the
[geometric conservation law](/properties/geometric-conservation-law.md)),
stabilize an otherwise unstable $N=5$ [channel](/benchmarks/turbulent-channel-flow.md)
at $Re_\tau=395$ with 3/8 of the DNS resolution, and leave lift, drag and
pressure on a stalled NACA 0020 at $Re=20\,000$ nearly unchanged. The
unfiltered runs are called [implicit LES](/definitions/implicit-les.md), the
filtered ones "LES"; the filter is the only model. The authors warn that
the parameters are tied to the DG-recovering correction function and the
Rusanov flux.

# Version read

Version of record (Comput. Fluids 237 (2022) 105301; received 19 January
2021, available online 14 January 2022), 28 pages, all read; pp. 6–8 also
read visually because the text layer drops the calligraphic degree symbol.
Page-1 title, authors and DOI match the metadata. No identity problem. The
solver is not named. Numbering on this page is that of this version.

# Key claims

Page-local symbols: $\Lambda$ the diagonal modal filter matrix,
$\Lambda^*=\Lambda^{1/n}$ its time-step-normalized form, $V$ the
Vandermonde matrix; $\vartheta^{\mathrm t}_m$ the total degree of a modal basis function
(sum of the exponents of its highest monomial; the source's $\eta$; an
integer, distinct from the normalized index $\vartheta_m$ of registry §11, as
on [explicit modal filtering](/methods/explicit-modal-filtering.md)), $\vartheta^{\mathrm t}_c$ and $\vartheta^{\mathrm t}_{\max}$ the cut-off and maximum
degree; $\alpha_f$, $s_f$ the damping and order of the exponential filter
(the source's $\alpha$, $s$); $\Lambda_{M}$ the filter optimized at
Taylor–Green Mach number $M$ (the source's $\Lambda_{Mach=M}$, called a
filter "strength"); $\mathcal Z$ the volume-averaged enstrophy (the
source's $\varepsilon$).

1. Finite-volume methods typically reach about 3% of peak FLOP/s on modern accelerators, a motivation for high-order unstructured methods (§1, citing earlier work). **Stated**
2. De-aliasing and limiters are relatively costly; artificial dissipation competes with filtering on cost but needs a sensor; filtering has typically negligible cost, but Park et al. found it can harm accuracy (§1). **Stated**
3. In ILES the FR numerical dissipation acts as a built-in SGS model together with high-order time stepping; the Riemann-solver dissipation is "responsible for reducing or eliminating a pile-up of kinetic energy in high-frequency modes" (§1, §2.1). **Stated**
4. The filters are optimized for the Rusanov flux and the DG-recovering (Radau) correction function; they "may not be optimal for different Riemann solvers" and "would not be generally suitable for other correction functions" (§2.1, §3.4). **Stated**
5. A fixed modal filter applied every step has a cumulative strength over a fixed interval that depends on $\Delta t$; with $\Lambda^*=\Lambda^{1/n}$, $n=T_{\mathrm{char}}/\Delta t$, $F^*=V\Lambda^*V^{-1}$ (Eqs. 28–30), $n$ applications of $F^*$ are "analogous to" one application of $F=V\Lambda V^{-1}$ per $T_{\mathrm{char}}$, so the observed strength is the same for any $\Delta t$ (§3.2). **Derived** (by construction for a diagonal $\Lambda$)
6. The time-step independence holds when the time integration is of high enough order and $\Delta t$ is not near the stability limit, so that the spatial operator governs the behaviour; otherwise the optimization could give different parameters (§3.2). **Stated**
7. The filter function must be smoother than the solution to limit its effect on the convergence rate, hence the exponential filter: $\sigma=1$ for $\vartheta^{\mathrm t}_m\le\vartheta^{\mathrm t}_c$, $\exp\{-\alpha_f[(\vartheta^{\mathrm t}_m-\vartheta^{\mathrm t}_c)/(\vartheta^{\mathrm t}_{\max}-\vartheta^{\mathrm t}_c)]^{s_f}\}$ up to $\vartheta^{\mathrm t}_{\max}$ (§3.3, Eq. 32). **Stated**
8. The filter function moves towards higher degrees when $s_f$ or $\vartheta^{\mathrm t}_c$ increase and when $\alpha_f$ decreases (§3.3, Fig. 6). **Shown**
9. The optimization used more than 14,000 runs: inviscid Taylor–Green vortex, $16^3$ degrees of freedom, $N=3,4,5$, $s_f\in\{2,4,8,16\}$, $M=0.1$–0.5; stability means pressure and density stay non-negative and real to $20T_{\mathrm{char}}$, $T_{\mathrm{char}}=L/U_0$ (§3.4, Algorithms 1–4). **Shown**
10. The optimum filters all have $s_f=16$; $\vartheta^{\mathrm t}_c=5$ for $N=3$; $\vartheta^{\mathrm t}_c=7$ for $N=4$ ($\Lambda_{0.1}$–$\Lambda_{0.4}$) and 6 ($\Lambda_{0.5}$); $\vartheta^{\mathrm t}_c=8$ for $N=5$ ($\Lambda_{0.1}$, $\Lambda_{0.2}$) and 6 ($\Lambda_{0.3}$–$\Lambda_{0.5}$); $\alpha_f$ ranges from about $2.2\times10^5$ to about $1.9\times10^{14}$ (Tables 4–6). **Shown**
11. The optimum filters split the spectrum "in general" at about 2/3, tending to 1/2 as $N$ grows, "similar to the 2/3 rule of dealiasing" (§3.4). **Stated**
12. Working hypothesis: filtering only the highest modes can preserve high-order accuracy, because those modes carry most of the aliasing error (§3.4). **Stated**
13. On the 2-D isentropic vortex the observed order (density $L_2$ error) is almost identical with and without the filter, both super-accurate: 7.626557 / 7.626587 ($N=3$), 9.104274 / 9.108797 ($N=4$), 10.426575 / 10.633066 ($N=5$) (§4.1, Table 1). **Shown**
14. Taylor–Green vortex at $Re=1600$ (linear mesh, $64^3$ degrees of freedom): filtered runs dissipate kinetic energy slightly faster, more with stronger filters, with the trend reversing later; the kinetic energy is "always less than the DNS results except for $N=3$" (§4.2, Figs. 9–10). **Shown**
15. The enstrophy-based dissipation $2\mu\mathcal Z/\rho$ is slightly under-predicted by the filtered runs, as the filter removes the enstrophy-dominated small scales (§4.2, Fig. 11). **Shown**
16. Stronger filters reduce the high-wavenumber energy at $20T_{\mathrm{char}}$ and enlarge the Q-criterion structures (§4.2, Figs. 12–13). **Shown**
17. The filters "slightly increase the amount of numerical dissipation for all polynomial degrees", while "the overall accuracy at each polynomial degree and for all filtering strengths is not impacted significantly" (§4.2). **Shown**
18. On a fully non-linear (sinusoidally perturbed, curved) Taylor–Green mesh the results are similar to the linear mesh (§4.3, Figs. 15–18). **Shown**
19. In the channel at $Re_\tau=395$ with 3/8 of the DNS degrees of freedom, $N=3$ and 4 are stable unfiltered; $N=5$ needs $\Lambda_{0.5}$ (§5.1). **Shown**
20. Filtering reduces the velocity spectra only at the higher modes, "as by design"; mean velocity and Reynolds stresses agree with DNS, "no loss in accuracy is seen" (§5.1, Figs. 20–25). **Shown**
21. At $N=3$ the filtered channel gives more accurate near-wall fluctuation intensities for $10<y^+<40$; the streamwise peak is at $y^+\approx12$ with and without the filter (§5.1, Fig. 25a). **Shown**
22. NACA 0020 at incidence 20 (unit not printed), $M=0.2$, $Re=20\,000$: time-averaged $C_L$/$C_D$ are 0.64/0.35 (DNS of Rosti et al.), 0.639/0.353 (unfiltered ILES) and 0.651/0.357 (filtered); the mean $C_p$ distributions are nearly identical (§5.2, Table 3, Fig. 30). **Shown**
23. The filtered airfoil run damps spurious small-scale structures while keeping the large ones (§5.2, Fig. 28). **Shown** (qualitative)
24. The filter "stabilizes otherwise unstable simulations, while maintaining good agreement with non-filtered stable solutions"; higher Reynolds numbers, other correction functions and other schemes are future work (§6). **Stated**

# Printed slips

- **Algorithm 1 (p. 7):** the unstable branch prints the update
  "$\eta_c=\eta_{max}-1$", while the stated purpose is that "the highest
  possible $\eta_c$ is found" by lowering it.
- **Eq. (32) with §3.4:** the search starts from $\eta_c=\eta_{max}$, where
  the middle branch of Eq. (32) has the denominator $\eta_{max}-\eta_c=0$.
- **Eq. (44):** the Rusanov flux is printed
  $\frac{\hat n_L}{2}\cdot(f^{inv}_L+f^{inv}_R)+\frac s2(u_L+u_R)$, the
  dissipative term a sum of the states rather than their jump; with
  $u_L=u_R$ it does not reduce to the physical flux.
- **Eq. (43):** the left-hand side is $\|\rho(t)\|^2$ while the right-hand
  side carries the square root; the integration window $[-2,2]^2$ is
  narrower than the domain.
- **Fig. 8:** the abscissa is labelled $\eta_{max}$ for a plot of $\sigma$
  against $\eta$.
- **Airfoil run length:** §5.2 gives 100 convective times with statistics
  over the final 80; the Fig. 28 caption reads "after $200T_{char}$".
- **References:** [42] has no volume ("AIAA J 2017;2186–97"); [34] prints
  "501, Rockefeller Institute Press New York; 1959, p. 504"; [39] prints
  "VonNeumann John".

# Notation map

| Hamedi & Vermeire | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathcal P$ | $N$ | polynomial degree; order $N+1$ |
| $N_p$, $N_e$ | (solution points per element, number of elements) | |
| $u^\delta$, $f^{\delta D}$, $f^R$, $g_L$, $g_R$ | (discrete solution, discontinuous flux, common flux, correction functions) | $f^R$ is $f^*$ in the registry |
| $\xi$, $J$ | $\xi$, $\mathcal J$ | reference coordinate, Jacobian determinant |
| $\hat u_i^\delta$, $\psi_i$, $V$ | (modal coefficients, orthonormal basis, Vandermonde matrix) | **collision:** the hat is not a test filter |
| $\Lambda$, $\Lambda^*$, $F$, $F^*$ | (page-local filter matrices and operators) | |
| $\eta$, $\eta_c$, $\eta_{max}$, $\eta^*$ | $\vartheta^{\mathrm t}_m$, $\vartheta^{\mathrm t}_c$, $\vartheta^{\mathrm t}_{\max}$, $\vartheta^{\mathrm t}_m/\vartheta^{\mathrm t}_{\max}$ | **collision:** $\eta$ is the Kolmogorov length in the registry |
| $\alpha$, $s$ (filter) | $\alpha_f$, $s_f$ | **collisions:** $\alpha$ also names the lifting coefficients, the angle of attack and the channel stretching factor; $s$ also the Rusanov wave speed |
| $\sigma(\eta)$ | (filter function) | not the $\sigma$ SGS model |
| $T_{char}=L/U_0$, $n$ | (characteristic time, steps per $T_{\mathrm{char}}$) | |
| $E_k$, $\epsilon(E_k)$ | (volume-averaged kinetic energy, $-dE_k/dt$) | |
| $\varepsilon$, $\epsilon(\varepsilon)$ | $\mathcal Z$ (page-local), $2\mu\mathcal Z/\rho$ | **collision:** the source's $\varepsilon$ is the enstrophy, not the dissipation |
| $Ma$, $\gamma$ | $M$, $\gamma$ | |
| $Re_b$, $Re_\tau$, $\delta$, $u_\tau$, $\Delta x^+$ | same | channel half-width $\delta$ |
| $C_L$, $C_D$, $C_p$ | same | |

# Reference list

68 printed references, numbered style. The list is merged complete into
the [bibliography](/bibliography.md) with `citedby` this slug. Same-author
same-year works take suffixes in printed order (Cockburn 1989, Vermeire
2016 and 2017, Pereira 2020). Ref. [29] (Wang Z.J. et al. 2013, Int. J.
Numer. Methods Fluids 72:811) is the ingested [wang-2013](/sources/wang-2013.md). Ref. [62] is an arXiv preprint kept as its own entry. Defects:
[42] no volume, [34] odd pagination, [59] no venue, [1] no report number.
No printed duplicates.

# Pages created or updated

Chunk 10 (2026-10-27). This source is cited on:

- [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Explicit modal filtering as an LES closure](/methods/explicit-modal-filtering.md)
- [Flux reconstruction](/methods/flux-reconstruction.md)
- [Spectral difference method](/methods/spectral-difference-method.md)
- [Entropy conservation and entropy stability](/properties/entropy-conservation.md)
- [Geometric conservation law and free-stream preservation](/properties/geometric-conservation-law.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
