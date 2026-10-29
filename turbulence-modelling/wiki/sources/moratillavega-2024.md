---
type: Source
title: "Moratilla-Vega et al. (2024) — Installed Jet Noise Analysis Using a Coupled LES/APE High-Order Method"
description: "Couples a second-order σ-model LES of a cold Mach 0.75 round jet, isolated and below a flat plate, one-way and in memory to a fifth-order DG solver of the acoustic perturbation equations; far-field spectra match experiment within 1–2 dB below St 0.7, and the plate changes the jet's sources little but scatters and reflects their noise."
resource: "doi:10.1007/s10494-023-00468-5"
source_kind: paper
authors: [Moratilla-Vega M.A., Xia H., Page G.J.]
year: 2024
venue: "Flow Turbul. Combust. 113:667–693"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Flow_Turbulence_and_Combustion_Moratilla-Vega_Installed_Jet_Noise_Analysis_Using_a_Coupled_LESAPE_High-Ord.pdf"
tags: [les, aeroacoustics, numerical-dissipation, dg]
timestamp: 2026-10-28T07:08:00Z
---

# Summary

Moratilla-Vega et al. (2024) apply a two-step hybrid computational
aeroacoustics method to installed jet noise. A cold, single-stream round jet
(acoustic Mach number 0.75, $Re\approx7\times10^5$ on the nozzle diameter
$D_j$) runs isolated and below a flat plate whose trailing edge lies $4D_j$
downstream of the nozzle exit and $1D_j$ from the jet axis, after the ISVR
experiments of Lawrence. The flow step is a compressible
[large-eddy simulation](/definitions/large-eddy-simulation.md) with the
[σ subgrid model](/methods/sigma-model.md) of Nicoud et al. (2011). It uses a second-order cell-vertex
finite-volume code with a Roe-type flux whose upwind dissipation is scaled by a
smoothing parameter of 0.3–1. The parameter is lowered in the source region
and raised near the boundaries, where the dissipation damps outgoing waves.
No inflow turbulence is imposed: the authors argue that the nozzle contraction
relaminarizes the boundary layer and that uncharacterized synthetic turbulence
"can generate spurious noise" ([inflow turbulence generation](/methods/inflow-turbulence-generation.md)).

The acoustic step solves the acoustic perturbation equations (APE-4,
Ewert & Schröder 2003) with the Lamb-vector perturbation as the only source,
on a fifth-order discontinuous Galerkin spectral/hp solver of Nektar++
([DG family](/methods/discontinuous-galerkin-spectral-element-method.md)).
The sources pass from the LES to the acoustic solver in memory through the
CWIPI coupling library. The plate barely changes the jet (velocity-decay
constants 7.5 and 7.4). The far-field spectra at 90° lie within 1–2 dB of
the experiment for $0.05<St<0.7$ and overpredict by 3–4 dB up to
the cut-off, which the authors attribute possibly to the laminar inflow. The
installed-minus-isolated spectra show a 4–8 dB low-frequency increase from
jet–surface interaction and a high-frequency increase of about 2 dB on the
unshielded side from reflection. The unshielded-side directivity follows the
$\sin^2(\theta/2)$ edge-scattering law. Filtered near fields show that the
[numerical dissipation](/properties/numerical-dissipation.md) of the
second-order LES removes high-frequency waves within a few diameters, whereas
the high-order acoustic solver propagates them. The Lamb-vector sources hardly
change with the plate, so the authors propose that the LES of the isolated jet
could suffice, with the plate entering only the acoustic step.

# Version read

Version of record (Springer, open access CC BY 4.0; received 28 November
2022, accepted 30 July 2023, online 17 August 2023), 27 pages (pp.
667–693), all read; the equations of pp. 669–670 were checked visually. Page
1 matches the metadata. The archive filename carries the online year 2023;
the issue year is 2024.

# Key claims

1. A two-step hybrid method is used: the LES produces the noise sources and the APE propagate them to the far field, with one-way coupling (§2, §2.3). **Stated**
2. The LES uses the σ model, $\mu_t=(C_\sigma\Delta)^2\mathcal D_\sigma$, $\mathcal D_\sigma=\varsigma_3(\varsigma_1-\varsigma_2)(\varsigma_2-\varsigma_3)/\varsigma_1^2$ with $\varsigma_1\ge\varsigma_2\ge\varsigma_3\ge0$ the singular values of the resolved velocity-gradient tensor; neither $C_\sigma$ nor $\Delta$ is printed (§2.1, Eqs. 4–5). **Stated**
3. The LES flux is a second-order Roe-type scheme, $F_{ij}=\tfrac12[F(Q_i)+F(Q_j)]-\tfrac12\epsilon|A_{ij}|[L_j(Q)-L_i(Q)]$ with $L$ a pseudo-Laplacian; $\epsilon$ ranges 0.3–1 in this study, smaller in the near-field source region and larger near boundaries to limit reflections; time integration is a four-stage Runge–Kutta scheme (§2.1, Eq. 6). **Stated**
4. APE-4 rather than APE-2 is used "since the case considered is a compressible flow problem" (§2.2). **Stated**
5. In isothermal flows with strong vortical motion the vortex-sound source $-(\boldsymbol\omega\times\boldsymbol u)'$ is "several orders of magnitude greater than the other terms combined" (citing Gröschel et al. 2008), so only this source is kept (§2.2). **Stated** (cited)
6. The APE are solved by Nektar++'s AcousticSolver, a DG spectral/hp method with a Gauss–Lobatto–Legendre basis of degree 5, a Lax–Friedrichs flux, an absorbing layer and classical RK4 (§2.2, Eq. 11). **Stated**
7. The LES–APE data exchange runs in memory through a shared MPI communicator with the CWIPI library, without file-system I/O (§2.3). **Stated**
8. Neither inflow turbulence nor a wall model is used: the nozzle contraction is "expected to cause the boundary layer to relaminarize", and synthetic inflow turbulence without experimental characterization "can generate spurious noise" (§3). **Stated**
9. LES grids: $547\times234\times121$ (isolated, "approximately 18,200,000" elements) and $547\times227\times121$ (installed, "about 16,500,000"); finest cell $7.874\times10^{-3}D_j$ axially ($\Delta x^+=220$) and $1.41\times10^{-3}D_j$ radially ($\Delta r^+=40$); $\Delta t=10^{-7}$ s (§3, Table 1). **Stated**
10. 121 azimuthal points suffice on the basis of a grid study (121 against 193 points) in Moratilla-Vega et al. (2020) (§3). **Stated**
11. Acoustic grids: about $10^6$ elements, finest element $0.117D_j$, degree 5, 216 M solution points; the time step follows $CFL=1/(2N+1)$ (Bauer et al. 2011), $\Delta t=3\times10^{-7}$ s (§3, Eq. 12, Table 1). **Stated**
12. Statistics: 100 $t^*$ of transient and 100 $t^*$ of averaging in the LES, then 50 $t^*$ of transient and 100 $t^*$ of signal in the coupled run ($t^*=tU_j/D_j$); 100 $t^*$ is argued sufficient for the reliable band, although 400–1000 $t^*$ are "typically considered necessary" in the jet-noise literature (§3). **Stated**
13. The highest reliable frequency follows the 1% dispersion–diffusion rule of Moura et al. (2015), $St_{\max}=c_\infty D_j|kh|_{1\%}/(2\pi hU_j)$ with $|kh|_{1\%}=8.071$ for degree 5, printed as $St_{\max}\approx1.4$ (§3, Eq. 13). **Stated** (see Printed slips)
14. Second-order methods need 22 points per wavelength (Bailly & Juvé 2000), the fifth-order DG only 5 (Moura et al. 2015) (§4.4). **Stated** (cited)
15. The plate has a marginal effect on the jet: a slight deflection toward the plate, a slightly longer potential core, velocity-decay constants $B_u=7.5$ (isolated) and 7.4 (installed), peak $u'_{\mathrm{rms}}/U_j\approx0.13$ at $x/D_j=8$ and 10, in good agreement with the hot-wire data of de Almeida et al. (2017) (§4.2, Eq. 14, Figs. 7–8). **Shown**
16. The shear-layer widths coincide up to $x/D_j\approx3$, the installed one is slightly wider for $3<x/D_j<4$, and they grow in parallel after the trailing edge (§4.2, Eq. 15, Figs. 9–10). **Shown**
17. Far-field 1/3-octave spectra at $\theta=90^\circ$ lie within 1–2 dB of Lawrence (2014) for $0.05<St<0.7$ in both cases and overpredict by 3–4 dB for $0.7<St\lesssim1.4$, "possibly caused by the laminar inlet conditions" (§4.3, Fig. 14). **Shown**
18. Installed minus isolated spectra at 90°: the same 4–8 dB increase up to $St=0.5$ on both sides (jet–surface interaction); beyond it about 2 dB on the unshielded side (jet–surface reflection), while the shielded side keeps decreasing and turns negative after $St\approx0.7$ (§4.3, Fig. 15). **Shown**
19. The unshielded-side $\Delta$OASPL follows the $\sin^2(\theta/2)$ law of Ffowcs Williams & Hall (1970) up to $\theta=110^\circ$; on the shielded side only the simulation follows it, up to 90°, and the reliability of the shielded-side measurements is questioned after Lawrence (2014) (§4.3, Fig. 16). **Shown**
20. The numerical dissipation of the second-order LES erases high-frequency waves within a few diameters, while the high-order APE solver carries them to the far field (§4.3, §4.4, Figs. 12, 13, 18). **Shown**
21. Frequency-filtered near fields: at $St=0.2$ waves generated at the trailing edge reach every observer angle; at $St=1$ the unshielded directivity of the installed jet points upstream (§4.4, Figs. 17–18). **Shown**
22. The plate changes the Lamb-vector sources little; the differences, at $y/D_j=0.93$ near $x/D_j=3$, sit where the sources are much weaker; the plate acts on propagation (scattering, reflection) rather than generation (§4.5, §5, Figs. 19–20). **Shown**
23. For this configuration the LES could simulate the isolated jet only, with the plate included only in the acoustic step (§4.5, §5). **Stated** (not tested)

# Printed slips

- **Smoothing range.** "the value of $\epsilon$ ranges from 0.3 to 1" (§2.1, p. 669) against "$\epsilon\in[0.1,1]$" (p. 670).
- **Probe distance.** "The acoustic signal is recorded along a line at $y/D_j=20$" against "the acoustic probes are located at a distance of $y/D_j=15$" (both p. 675).
- **Lowest reliable frequency.** "the minimum reliable frequency is between St = 0.05 and 0.01" (p. 675, with a sentence repeated verbatim) against "the 0.05−0.1 reliable range obtained with the 100t∗ of signal"; 100 $t^*$ resolves $St=0.01$, and five to ten times that is $0.05$–$0.1$ *(compiler check, not in the sources)*.
- **Azimuthal points.** A grid study "with 121 and 193 azimuthal points", then "The results obtained for the 120 azimuthal point mesh" (p. 673).
- **CFL.** "$CFL=1/(2p+1)$" with $p=5$ "is approximately 0.16" (p. 675); $1/11=0.091$ *(compiler check, not in the sources)*.
- **$St_{\max}$.** Eq. 13 with $|kh|_{1\%}=8.071$, $h=0.117D_j$ and $U_j=0.75c_\infty$ gives 14.6, not the printed "approximately 1.4"; the paper does not state which $h$ it used *(compiler check, not in the sources)*.
- **Element counts.** $547\times234\times121=15{,}487{,}758$ and $547\times227\times121=15{,}024{,}449$, against "approximately 18,200,000" and "about 16,500,000" elements; Table 1 lists the same numbers as cells and as solution points. The acoustic grid $136\times90\times90=1{,}101{,}600$ against "1,000,000" in Table 1 *(compiler check, not in the sources)*.
- **Eq. 16.** "$\hat p(f)=\int_{-\infty}^{\infty}p(t)\exp{-2\pi ft}\,dt$", without the imaginary unit and without the prime of the "Fourier transform of $p'$" named in the text.
- **Heat flux.** "$\tilde q_j=-\lambda\partial_i\tilde T$" (p. 669), index $i$ for $j$.
- **Reflection sentence (§4.3, p. 684).** "This is evidence of the plate blocking in the unshielded side the high-frequency sources generated in the jet plume, and reflecting them towards the shielded side" inverts the sides of the data described (unshielded +2 dB, shielded negative) and of the Conclusion ("causing an increase in high-frequency noise levels for observers below the flat plate").
- **Eq. 15.** "$\frac{\delta}{D_j}=r_{0.95U_j}-r_{0.1U_j}$": the right-hand side is not divided by $D_j$; the text defines the radii by "0.95 and 0.1 the maximum mean velocity", the blanking by $U_j$.
- **Citations and typos.** "Head and Fisher (1976, 1977)" with only the 1976 item listed; "$\theta = 110$" without a degree sign; "Friederichs" (p. 670); "Expermiental" (p. 678). The Conclusion's "within 3–4 dB of the experimental data up to the cut-off frequency" is the worst case of the §4.3 statement (1–2 dB below $St=0.7$).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| overbar (§2.1) | $\bar\phi$ | LES filter, assumed to commute with derivatives |
| overbar (§2.2, APE) | $\langle\phi\rangle$ (time average) | **collision:** the same symbol is a time average in the acoustic equations |
| tilde | $\tilde\phi$ | Favre filter |
| $\mathcal T_{ij}=\bar\rho\tilde u_i\tilde u_j-\overline{\rho u_iu_j}$ | $-\tau_{ij}$ (compressible form $\bar\rho(\widetilde{u_iu_j}-\tilde u_i\tilde u_j)$) | **sign:** the source's SGS stress has negative trace |
| $\tilde\tau_{ij}$ | $\sigma_{ij}$ (resolved viscous stress) | **collision:** not the SGS stress |
| $\mathcal L_j$ | (subgrid energy-flux term, undefined in the source) | |
| $\mu_{SGS}$ | $\mu_t$ | |
| $C_m$, $\Delta$ | $C_\sigma$, $\Delta$ | σ-model constant (registry §11, as on [sigma model](/methods/sigma-model.md)); not printed |
| $\sigma_1\ge\sigma_2\ge\sigma_3$, $\mathcal D_m$ | $\varsigma_1\ge\varsigma_2\ge\varsigma_3$, $\mathcal D_\sigma$ | singular values of the velocity gradient, σ-model operator (registry §11, as on the sigma-model page); **collision:** not the viscous stress $\sigma_{ij}$ |
| $\epsilon$, $L(\cdot)$, $\lvert A_{ij}\rvert$ | (smoothing parameter, pseudo-Laplacian, Roe matrix) | not a dissipation rate |
| $p'$, $\mathbf u'$ | (acoustic pressure and velocity) | **collision:** the prime is an acoustic perturbation about the time average |
| $q_c$, $\mathbf q_m$, $L'$, $L'_r$ | (APE sources, Lamb-vector perturbation, its radial part) | |
| $\boldsymbol\omega$ | $\omega_i$ | vorticity |
| $p$ (§3, Eqs. 12–13) | $N$ | DG polynomial degree (5); **collision** with the pressure |
| $h$ (Eq. 13); $h$ ($h/D_j=1$) | $h$; (plate offset from the jet axis) | **collision:** element size and plate offset |
| $l$ | (plate length downstream of the nozzle exit) | $l/D_j=4$ |
| $\lvert kh\rvert_{1\%}$ | (resolved wavenumber–element-size product at 1% error) | 8.071 for $N=5$ |
| $D_j$, $U_j$, $c_\infty$ | (nozzle diameter, jet velocity, ambient sound speed) | |
| $Ma$ | $M$ | acoustic Mach number $U_j/c_\infty=0.75$ |
| $St$ | $St=fD_j/U_j$ | |
| $t^*$ | $tU_j/D_j$ | |
| $B_u$ | (centreline velocity-decay constant) | |
| $\delta$ (Eq. 15) | (shear-layer width) | **collision:** not a boundary-layer thickness |
| $x^+$, $r^+$ | $\Delta x^+$, $\Delta r^+$ (cell sizes in wall units) | reference location of $u_\tau$ not stated |
| $\theta$ | (azimuthal angle in Fig. 3; polar observer angle in §4.3) | **collision:** not the momentum thickness |

# Reference list

49 printed references, author–year style. The list is merged complete into
the [bibliography](/bibliography.md) with `citedby` this slug. Brès et al.
(2018) and Wang et al. (2020) here are different works from same-key entries
already in the bibliography and are keyed apart. The two Moratilla-Vega 2019
items (a conference paper and a thesis) take suffixes in printed order;
Ffowcs Williams & Hall (1970) is printed as "Williams, J.F., Hall, L." and
keyed by the printed surname. "Head and Fisher (1977)" is cited in the text but
not listed; Refloch et al. (2011), cited for CWIPI, is titled "CEDRE
Software"; the author list of the MPI book by Gropp et al. is printed garbled
and recorded as printed. No printed duplicates.

# Pages created or updated

Chunk 4 (2026-10-26), cited further in chunks 6, 7, 15. This source is cited on:

- [Turbulent round jets](/benchmarks/turbulent-round-jet.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Ffowcs Williams–Hawkings acoustic analogy](/methods/ffowcs-williams-hawkings-acoustic-analogy.md)
- [Inflow turbulence generation](/methods/inflow-turbulence-generation.md)
- [Sigma model](/methods/sigma-model.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Nektar++](/software/nektar-plus-plus.md)
