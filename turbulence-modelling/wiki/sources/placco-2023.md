---
type: Source
title: "Placco et al. (2023) — Large-Eddy Simulation of the unsteady supersonic flow around a Mars entry capsule at different angles of attack"
description: "Implicit LES with the GPU finite-difference code STREAmS (fifth-order WENO, ghost-point immersed boundary) of a Mars entry capsule at Mach 2 and four angles of attack, describing wake topology, turbulent kinetic energy, aerodynamic coefficients, lift spectra and a POD low-order model of the fishtail wake mode."
resource: "doi:10.1016/j.ast.2023.108709"
source_kind: paper
authors: [Placco L., Cogo M., Bernardini M., Aboudan A., Ferri F., Picano F.]
year: 2023
venue: "Aerosp. Sci. Technol. 143:108709"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Aerospace_Science_and_Technology_Placco_Large-Eddy_Simulation_of_the_unsteady_supersonic_flow_around.pdf"
tags: [les, implicit-les, compressible, separated-flow, gpu]
timestamp: 2026-10-26T05:09:00Z
---

# Summary

Placco et al. (2023) simulate the supersonic flow around an ExoMars-2022-shaped
Mars entry capsule at $M_\infty=2$, $Re_D=10^6$ ($D=3.8$ m), in an ideal-gas
CO$_2$ atmosphere ($\gamma=1.3$, $Pr=0.72$) at about 9 km altitude, the
condition before parachute deployment, for angles of attack $0^\circ$,
$5^\circ$, $10^\circ$ and $15^\circ$. The paper belongs to planetary-entry
aerodynamics; its tie to this bundle is the simulation approach, not a
modelling contribution.

No explicit subgrid model is used: the authors run an
[implicit LES](/definitions/implicit-les.md), in which the
[numerical dissipation](/properties/numerical-dissipation.md) of the
fifth-order [WENO](/methods/weno-scheme.md) convective discretization acts at
the small scales, a choice they justify by citing implicit LES of turbulent
boundary layers. The solver is the GPU code [STREAmS](/software/streams.md)
(sixth-order central viscous terms, third-order Runge–Kutta), with a
ghost-point-forcing [immersed boundary method](/methods/immersed-boundary-method.md)
for the capsule on a $2048\times672\times672$ rectilinear grid, run on 32 GPUs.
The introduction contrasts this with earlier
[detached-eddy simulations](/methods/detached-eddy-simulation.md) of capsule
wakes, which were confined to the near-body wake and, by the cited account,
disagreed with experiment at the backshell because the
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) model mispredicted
transition after the shoulder separation.

Results are descriptive: bow shock, shoulder expansion fans, a subsonic
recirculation closed by a recompression shock, and a toroidal mean vortex at
$0^\circ$ that merges into a single, smaller eddy as the angle grows. Backshell
turbulent kinetic energy falls with the angle while far-wake fluctuations
grow. The drag coefficient decreases slightly and the lift coefficient rises
to 0.367 at $15^\circ$. The lift spectrum peaks at $St=fD/U_\infty\approx0.2$–$0.3$,
tied to the antisymmetric fishtail (helical) wake mode. A snapshot proper
orthogonal decomposition (POD) of the streamwise velocity at $0^\circ$ and
$5^\circ$ gives a ten-mode low-order model that reproduces the fishtail
motion. There is no comparison with experiment or reference simulations and no
grid-convergence study.

# Version read

Version of record (Elsevier, open access CC BY; received 7 August 2023,
accepted 29 October 2023, online 7 November 2023), 14 pages, all read. Page-1
title, six authors, venue and DOI match the metadata above; no identity
problem. Section, equation, table and reference numbers on this page are those
of this version.

# Key claims

1. The capsule flow at $M_\infty=2$, $Re_D=10^6$ and angles of attack $0^\circ,5^\circ,10^\circ,15^\circ$ is computed by implicit LES: conventional LES modelling is omitted and "the numerical dissipation given by the numerical discretisation" acts "as artificial viscosity acting at small scales" (§2). **Stated**
2. Implicit LES "has recently been justified when applied to turbulent boundary layers [50,51], showing comparable results to coarse DNS simulations" (§2). **Stated** (cited: Poggie et al. 2015; Ritos et al. 2018)
3. Discretization in STREAmS: fifth-order WENO for the convective terms, sixth-order central finite differences for the viscous terms, third-order explicit Runge–Kutta (Wray) in time (§2). **Stated**
4. The capsule is represented by a ghost-point-forcing immersed boundary method [54,55]: grid nodes are tagged fluid or solid and ghost nodes, filled with values interpolated from the fluid, enforce no-slip and no-penetration (§2). **Stated**
5. Grid $N_x\times N_y\times N_z=2048\times672\times672$ on a $20D\times10D\times10D$ box, clustered in the central region, capsule nose at $(D,0,0)$; 32 GPUs of Marconi100 (§3, Fig. 1). **Stated**
6. Free stream (Table 1): $p_\infty=265.11$ Pa, $T_\infty=223.68$ K, $\rho_\infty=6.22\cdot10^{-3}$ kg/m$^3$, $a_\infty=235.40$ m/s, $\mu_\infty=1.123\cdot10^{-5}$ Pa·s, about 9 km altitude on a simulated entry trajectory [56] (§3). **Stated**
7. The flow has a detached bow shock, shoulder expansion fans, a separated subsonic recirculation (near wake), a recompression shock from merging compression waves, and a supersonic far wake with small subsonic pockets (§4, Figs. 3–4). **Shown**
8. The recirculation region and the wake width at the neck shrink as the angle of attack grows, "similarly as observed in [57]" (§4, Fig. 5). **Shown**
9. At $0^\circ$ the mean flow has a toroidal vortex ring attached to the backshield; at larger angles the flow from the upper shoulder engulfs the lower one, merging them into a single, more contained eddy that shrinks with the angle (§4, Fig. 5). **Shown**
10. The turbulent kinetic energy in the backshield region is highest at $0^\circ$ and decreases in intensity and extent with the angle (§4, Fig. 6). **Shown**
11. In the far wake, fluctuations are stronger at larger angles; the authors attribute this to extra production from the secondary mean-velocity gradient of the tilted, asymmetric wake shear layer, the lower shoulder producing more (§4, Fig. 8). **Shown** (attribution **Stated**)
12. Velocity-deficit profiles are strongest at $x/D=4$ and weaken downstream; symmetric at $0^\circ$, they shift towards negative $z/D$ with a second negative peak at nonzero angles, and their depth generally decreases with the angle (§4, Fig. 7). **Shown**
13. Mean coefficients (Table 3): $C_D=1.5685$, $1.5662$, $1.5562$, $1.5349$ and $C_L=2.8\cdot10^{-8}$, $0.1240$, $0.2458$, $0.3670$ at $0^\circ,5^\circ,10^\circ,15^\circ$; rms values $C_{D,\mathrm{rms}}=2.0\cdot10^{-3}$, $8.6\cdot10^{-4}$, $8.1\cdot10^{-4}$, $9.3\cdot10^{-4}$ and $C_{L,\mathrm{rms}}=2.2\cdot10^{-3}$, $4.8\cdot10^{-4}$, $5.4\cdot10^{-4}$, $5.2\cdot10^{-4}$ (§4). **Shown**
14. Drag decreases slightly with the angle, explained by the smaller cross-section exposed to the flow and the reduced turbulence activity in the recirculation region (§4). **Shown** (explanation **Stated**)
15. The mean pressure coefficient on the backshell is negative everywhere; its maximum on the heat shield follows the stagnation point, the distribution stays symmetric about the $xz$ plane, and at nonzero angles the profiles drop steeply towards negative $z/D$ with a widening plateau on the other side (§4, Figs. 9–10). **Shown**
16. The discrete Fourier transform of $C_L$ shows a dominant content at $St=fD/U_\infty\approx0.2$–$0.3$ (about 30 Hz), drifting to the upper end of the range and losing spectral density as the angle grows (§4, Fig. 11). **Shown**
17. Higher-frequency content at $St\approx0.50$ and $0.75$ appears from $5^\circ$ to $15^\circ$; at $15^\circ$ the spectrum extends beyond $St=1$ (§4). **Shown**
18. The $St=O(10^{-1})$ content is the antisymmetric fishtail wake motion, a helical vortex pattern in three dimensions; $St=O(1)$ components relate to ring vortices from the mixing of the detached shear layers, as in disk wakes [61,62] (§4). **Shown** (presence) / **Stated** (identification, from the literature)
19. The higher frequencies at larger angles are attributed to the contracting recirculation region, which discharges smaller eddies, and to a stronger instability of the tilted shear layer at detachment, with ring vortices inclining and linking [61] (§4). **Stated**
20. Snapshot POD of the streamwise velocity: 130 two-dimensional snapshots on the plane $y/D=0$, spaced by 0.1 in reference time units, at $0^\circ$ and $5^\circ$, over a window matching the approximate period of the force oscillations (§5). **Stated**
21. The first ten POD modes hold "around the 60%" of the fluctuation energy at $0^\circ$ and "around 55%" at $5^\circ$ (§5, Fig. 12). **Shown**
22. The first temporal coefficient at $0^\circ$ is quasi-sinusoidal with one oscillation in the window; modes 1–2 represent the helical vortex structure, modes 5–6 eddies from vortex discharge or linking (§5, Figs. 12–14). **Shown**
23. A ten-mode reconstruction reproduces the fishtail motion and wake direction in both cases; instantaneous and rms profiles agree better at $0^\circ$ and further downstream ($x/D=16$ against 8), and truncation lowers the rms amplitudes (§5, Figs. 15–17). **Shown**
24. POD output can enter aerodynamic databases as a time-dependent supplement to the static models of entry, descent and landing design and of parachute release (§§5–6). **Stated**
25. Earlier DES of capsule wakes [26–29] covered only the near-body wake and disagreed with experiment in the backshell area, attributed to the turbulence model's failure to predict transition after the shoulder separation [29] (§1). **Stated** (cited)

# Printed slips

- **Eq. (3), pressure coefficient.** Printed $C_P=\frac{2}{\gamma Ma_\infty}\left(\frac{p}{p_\infty}-1\right)$. *(compiler check, not in the sources)* With $C_p=(p-p_\infty)/(\tfrac12\rho_\infty U_\infty^2)$ and $\rho_\infty U_\infty^2=\gamma p_\infty M_\infty^2$ for an ideal gas, $C_p=\frac{2}{\gamma M_\infty^2}\left(\frac{p}{p_\infty}-1\right)$: the square on the Mach number is missing.
- **§4, normalization of $k$.** "$K_\infty$ which corresponds to the specific kinetic energy of the free-stream flow ($K_\infty=0.5\cdot\rho_\infty U_\infty^2$)": the expression carries the density, so it is an energy per unit volume, not a specific one; consistent with Eq. (2), whose $k$ also carries the density.
- **§4, rms of the coefficients.** The text says the rms values show "lower amplitude fluctuations (around one order of magnitude of difference) from the respective average value as the angle-of-attack increases" and that drag and lift both "follow this characteristic behaviour". *(compiler check, not in the sources)* Table 3 gives ratios between $0^\circ$ and the other angles of about 2.2–2.5 for $C_{D,\mathrm{rms}}$ and 4.1–4.6 for $C_{L,\mathrm{rms}}$, and $C_{D,\mathrm{rms}}$ is not monotone ($9.3\cdot10^{-4}$ at $15^\circ$ against $8.1\cdot10^{-4}$ at $10^\circ$). The text does not say between which quantities the order of magnitude is taken.
- **Reference names.** The text cites "Allen [1]" while ref. [1] prints "A. Julien, A. Eggers" (NACA TN-4047); "Campbell [4]" against ref. [4] "J. Cumpbell"; "Micheltree and Gnoffo" (§1) against refs. [17,18] "Mitcheltree"; "Peterson [47]" against the garbled author list of ref. [47] ("J.R. Charbel Farhat").
- **Ref. [62]** prints "J. Fluids Struct. 27 (2015) 064101", while ref. [43] prints "J. Fluids Struct. 27 (2011) 175–192": the same volume with two years.
- **Typos.** "antsymmetric" (§5), "an descent module" (§6), "exchanged forced" (§4), "thewake" (ref. [61]).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho$, $u_i$, $p$, $T$ | $\rho$, $u_i$, $p$, $T$ | agree; no filter symbol is used (implicit LES) |
| $E=c_vT+u_iu_i/2$ | (total energy per unit mass) | **collision:** the registry's $E$ is per unit volume |
| $\lambda=c_p\mu/Pr$ | (thermal conductivity) | **collision:** not the Taylor microscale |
| $\gamma=1.3$, $Pr=0.72$, $\mu$ | $\gamma$, $Pr$, $\mu$ | agree; $\mu$ by a power law with exponent 0.76 |
| $\bar f$ | $\langle f\rangle$ | **collision:** the source's overbar is a time (Reynolds) average, the registry's an LES filter |
| $\tilde f=\overline{\rho f}/\bar\rho$, $f''$ | $\langle f\rangle_\rho$, $f''$ | **collision:** the source's tilde is a Favre average, the registry's a Favre filter |
| $k=\bar\rho\,\widetilde{u_i''u_i''}/2$ | $\tfrac12\langle\rho u_i''u_i''\rangle$ | **differs:** carries the density (energy per unit volume); the registry's $k$ is kinematic |
| $K_\infty=0.5\rho_\infty U_\infty^2$ | (free-stream dynamic pressure) | normalization of $k$ |
| $Re_\infty=\rho_\infty U_\infty D/\mu_\infty$ | $Re_D$ | diameter-based |
| $Ma_\infty$, $M_\infty$ | $M_\infty$ | both spellings printed |
| $P_\infty$, $p_\infty$ | $p_\infty$ | both spellings printed |
| $C_D$, $C_L$, $C_P$ | $C_D$, $C_L$, $C_p$ | reference area not stated |
| $St=fD/U_\infty$ | $St$ | agrees |
| $t_0=D/\sqrt{p_\infty/\rho_\infty}$ | (reference time) | not $D/U_\infty$ |
| $\alpha$, AoA | (angle of attack) | **collision:** the registry's $\alpha$ is the DG/finite-volume blending factor |
| $q$, $\bar q$, $\phi_j$, $a_j(t)$ | (POD variable, its time mean, spatial mode, temporal coefficient; page-local) | Eq. (4), $q-\bar q=\sum_ja_j\phi_j$ |
| $N_x$, $N_y$, $N_z$ | $N_x$, $N_y$, $N_z$ | agree |

# Reference list

65 printed references, numbered style ([1]–[65]). The list is merged complete
into the [bibliography](/bibliography.md) with `citedby` this slug. Ref. [11]
(Li et al. 2022, Tianwen-1 entry module, Astrodynamics 6:39–52) shares the
printed key `li-2022` with the ingested [li-2022](/sources/li-2022.md), a
different work, and is kept as a separate entry, `li-2022-e`. Refs.
[2]–[3] (Chester 1956) and [44], [46] (Boustani 2022) take suffixes in printed
order. Refs. [52], [53] are the STREAmS papers (Bernardini et al. 2021, 2023).
Ref. [40] prints no venue; ref. [56] no page or article number; refs. [1],
[4], [47] and [62] carry the printed defects listed above. No printed
duplicates.

# Pages created or updated

Chunk 3 (2026-10-26). This source is cited on:

- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [Immersed boundary methods](/methods/immersed-boundary-method.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [STREAmS](/software/streams.md)
