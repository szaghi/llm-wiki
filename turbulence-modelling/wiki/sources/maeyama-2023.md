---
type: Source
title: "Maeyama & Kawai (2023) — Near-wall numerical coherent structures and turbulence generation in wall-modelled large-eddy simulation"
description: "Wall-stress-modelled LES and new DNS of a Mach-2.28 flat-plate boundary layer up to Re_tau 14 000: below the matching height the LES holds coherent but non-physically wide streak–vortex pairs whose width is set by the SGS eddy viscosity, and it misses the Reynolds-number growth of the outer spectral peak."
resource: "doi:10.1017/jfm.2023.575"
source_kind: paper
authors: [Maeyama H., Kawai S.]
year: 2023
venue: "J. Fluid Mech. 969:A29"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Journal_of_Fluid_Mechanics_Maeyama_Near-wall_numerical_coherent_structures_and_turbulence_gener.pdf"
tags: [wmles, wall-model, les, dns, compressible, boundary-layer]
timestamp: 2026-10-28T02:14:00Z
---

# Summary

Maeyama & Kawai (2023) ask how near-wall turbulence is generated and
sustained in [wall-modelled LES](/methods/wall-modelled-les.md) of the
wall-stress type, where the grid does not resolve the viscous-scaled streaks
and quasi-streamwise vortices below the matching height $h_{\mathrm{wm}}$.
The inner-layer total shear-stress balance of Kawai & Larsson (2012)
explains the statistics, but not the structures.
[Hybrid RANS/LES](/definitions/hybrid-rans-les.md) and
[slip-wall models](/methods/slip-wall-model.md) are set aside.

The test case is a zero-pressure-gradient [boundary layer](/benchmarks/turbulent-boundary-layer.md)
at $M_\infty=2.28$, computed with sixth-order compact differences, an
eighth-order low-pass filter, the selective mixed-scale SGS model and the
Kawai–Larsson [equilibrium wall model](/methods/equilibrium-wall-model.md)
matched at the tenth grid point, which avoids
[log-layer mismatch](/definitions/log-layer-mismatch.md). New
[DNS](/definitions/direct-numerical-simulation.md) at
$Re_\tau\approx700$, 1250 and 2300 (up to 5.6 billion points, database
released) is the reference. The WMLES (about 12 million points) runs at
those three $Re_\tau$ and at 4100, 7800 and 14 000. Inflow comes from
rescaling–reintroduction ([inflow generation](/methods/inflow-turbulence-generation.md)).
The authors quote the Choi & Moin [grid estimates](/results/les-grid-point-requirements.md).

Above $h_{\mathrm{wm}}$, the [van Driest](/definitions/compressible-velocity-transformation.md)
velocity, the Reynolds shear stress and the TKE budget match the DNS.
Quadrant analysis and a three-dimensional conditional average of intense
Q2–Q4 pairs at $y^+\approx15$ show that the near-wall region of the WMLES
holds coherent streak-like pairs with a vortex between them. These
"numerical coherent structures" span about 8 grid points per spanwise
wavelength and, as $Re_\tau$ grows, are "non-physically elongated" in
span relative to the DNS. Their width collapses only
in a new semi-local scaling that adds the SGS eddy viscosity to the
molecular one: SGS diffusion sets the scale. The collapse also holds on
other grids, with the [kinetic-energy-preserving](/properties/kinetic-energy-preservation.md)
KEEP scheme, and with the [Smagorinsky model](/methods/smagorinsky-model.md).
SGS dissipation dominates filter dissipation
([numerical dissipation](/properties/numerical-dissipation.md)).

The WMLES does not reproduce the Reynolds-number growth of the outer peak
of the streamwise spectrum. A spanwise cut-off at $\lambda_z/\delta=0.7$
puts the deficit in the nominally resolved large scales. The authors
speculate that the outer peak needs inner–outer interaction with
near-wall turbulence. They place $h_{\mathrm{wm}}$ in the log region, whose
eddies scale with $y$ ([attached eddies](/definitions/attached-eddy-hypothesis.md)).
The paper sits within [large-eddy simulation](/definitions/large-eddy-simulation.md)
of wall turbulence.

# Version read

Version of record (J. Fluid Mech. 969:A29, Cambridge University Press, open
access; received 28 November 2022, accepted 7 July 2023), 44 pages, all
read; the equations of §2, §4.3, §5.4 and Appendix D and figure 2 were
checked visually. Page 1 matches the published identity. The bundle's
[maeyama-2022](/sources/maeyama-2022.md) is a plasma-turbulence paper by
other authors, a different work. Numbering on this page is that of this
version.

# Key claims

The source's overbar (Reynolds average) is written $\langle\cdot\rangle$ and
its tilde (Favre average) $\langle\cdot\rangle_\rho$, with $u_i''$ the Favre
fluctuation. Its SGS eddy viscosity $\nu_{t,sgs}$ is $\nu_t$ and its
wall-model eddy viscosity $\mu_{t,wm}$ is $\mu^w_{\mathrm{sgs}}$. Page-local
symbols: $\delta^{*,\mathrm{sgs}}_\nu$ the SGS-augmented semi-local viscous
length; $l_z$ the near-wall spanwise length scale, with $l_z^+$, $l_z^*$,
$l_z^{*,\mathrm{sgs}}$ its three scalings; $H_{\mathrm q}$ the hyperbolic-hole
parameter of quadrant analysis (the source's $H$).

1. Below the matching height the WMLES holds near-wall coherent structures (Q2–Q4 pairs: low- and high-speed streaks alternating in span with a streamwise vortex between them), although the grid does not resolve near-wall eddies; the region is "not composed of disordered random structures, but streak-like coherent structures" (§5.3, figs. 14–16). **Shown**
2. These structures are "non-physically elongated" in span relative to the DNS as $Re_\tau$ grows; at $Re_\tau\approx700$ they resemble the DNS because that WMLES grid is close to DNS resolution (§5.1, §5.3, figs. 8–10, 14, 15). **Shown**
3. The spanwise distance between the Q2 and Q4 centres in the WMLES is "approximately 4 grid points for all Reynolds numbers, i.e. approximately 8 grid points in one spanwise wavelength $\lambda_z$" (§5.3). **Shown**
4. The spanwise premultiplied spectra at $y^+\approx15$ peak at $\lambda_z^+\approx100$ in the DNS (consistent with Smith & Metzler 1983) and collapse in wall units; the WMLES spectra do not scale with $\delta_\nu$ but peak at about the same $\lambda_z/\delta$ (fig. 10a,b). **Shown**
5. With the semi-local scaling including the SGS eddy viscosity, $\delta^{*,\mathrm{sgs}}_\nu=(\nu+\nu_t)/u_\tau^*=(\mu+\mu_t)/(\langle\rho\rangle u_\tau^*)$, $u_\tau^*=\sqrt{\tau_w/\langle\rho\rangle}$ (Eq. 5.5, local $\langle\rho\rangle$ and $\mu$ at height $y$), the near-wall spanwise length $l_z^{*,\mathrm{sgs}}$ of the WMLES collapses over $Re_\tau\approx700$–14 000 to the order of the DNS value $l_z^+\sim O(100)$; in wall units ($l_z^+$) or in the semi-local scaling of Coleman et al. (1995) ($l_z^*$, Eq. 5.4) it grows almost linearly with $Re_\tau$ (§5.4, fig. 17b). **Shown**
6. Hence "the diffusion introduced by the SGS eddy viscosity dominantly determines the spanwise length scale of the numerical turbulence structures in the WMLES"; the collapse holds on other grids (App. C, fig. 28) and with other schemes and SGS models (App. D, fig. 32), and the SGS-model dissipation dominates the low-pass-filter dissipation (App. D) (§5.4). **Shown**
7. Near-wall turbulence generation in the WMLES is "maintained by the numerically elongated near-wall coherent structures", presented as "suggested" within the self-sustaining-process picture (§5.3, §7). **Stated** (interpretation of shown data)
8. The WMLES near-wall structures are not elongated in the streamwise direction relative to the spanwise one, unlike the DNS (fig. 15); the authors read this as support for Jiménez (2022), that long streaks are "not necessarily required for the self-sustaining process" (§5.3). **Shown** / interpretation
9. The van Driest mean velocity $\langle u\rangle^+_{vD}$ and the Reynolds shear stress match the DNS above $h_{\mathrm{wm}}$ at $Re_\tau\approx700$, 1250 and 2300 (fig. 4); the total shear stress (Reynolds, molecular and SGS) stays about $\langle\tau_w\rangle$ even below $h_{\mathrm{wm}}$, with oscillations (fig. 5, §4.1). **Shown**
10. Quadrant analysis: the WMLES captures the dominance of Q2 (ejections) over Q4, even near the wall; Q2 and Q4 are under-predicted above $h_{\mathrm{wm}}$ at $Re_\tau\approx1250$ and 2300, and the DNS Q2 peak at $y^+\approx40$ is missed even at $Re_\tau\approx700$, while the total $\langle\rho\rangle\langle u''v''\rangle_\rho$ is right because of the shear-stress balance (§4.2, fig. 6). **Shown**
11. The TKE-budget terms match the DNS above $h_{\mathrm{wm}}$; the production peak at $y^+\approx12$ is largely captured at $Re_\tau\approx700$ and hardly at 2300 (first point at $y_1^+\approx16$); the DNS premultiplied production $y^+P_k$ has a Reynolds-number-independent peak at $y^+\approx15$ and a log-region plateau; the WMLES misses the near-wall peak, but at 1250 and 2300 "the second point off the wall shows a peak" (§4.3, fig. 7). **Shown**
12. With $H_{\mathrm q}=1.75$ at $y^+\approx15$ ($Re_\tau\approx2300$), "approximately 55 %" of the total Reynolds shear stress lies outside the hole while those events occupy less than 10 % of the time, in both DNS and WMLES; Q2 and Q4 each carry "approximately 30 %–40 %" (§5.2.1, fig. 12). **Shown**
13. The WMLES does not reproduce the appearance or growth of the outer peak of the premultiplied spanwise spectrum of $u''$ with $Re_\tau$, up to $Re_\tau\approx14\,000$ (§6.1, figs. 19, 20, 26; App. B). **Shown**
14. The streamwise normal stress departs from the DNS above $h_{\mathrm{wm}}$ ($y/\delta\gtrsim0.085$) at $Re_\tau\approx1250$ and 2300, while the spanwise and wall-normal stresses agree at all $Re_\tau$; the WMLES $\langle\rho\rangle\langle u''u''\rangle_\rho$ is nearly the same at every $Re_\tau$ against $y/\delta$ (§6.1, fig. 18). **Shown**
15. A spanwise cut-off at $\lambda_z/\delta=0.7$ shows that the WMLES reproduces the small-scale part and misses the Reynolds-number growth of the large-scale part ($\lambda_z/\delta>0.7$): the outer-peak deficit is a failure on order-$\delta$ fluctuations that the WMLES grid is designed to resolve (§6.2, fig. 22). **Shown**
16. Instantaneous fields at $y/\delta\approx0.15$ show "no noticeable difference" between WMLES and DNS, in contrast to $y^+\approx15$ (§6.1, fig. 21). **Shown** (qualitative)
17. The authors speculate that the outer peak originates in interaction with the inner peak and "does not appear alone without resolving or correctly reflecting the near-wall turbulence structures", "just speculation as of now" (§6.2, §7). **Stated**
18. Against Mizuno & Jiménez (2013), who concluded that log-layer structures do not depend on seeding from the wall, the deterioration of the log-region streamwise stress "indicates that the turbulence dynamics of the near-wall inner layer has some influence on the large-scale eddy dynamics in the logarithmic region" (§6.2). **Stated** (inferred from shown data)
19. On a wall-parallel grid $\sqrt2$ times finer ($\delta/\Delta x=\delta/\Delta z=37.8$) "the indication of the appearance of the outer peak" is seen and the log-layer streamwise stress rises mainly through its large-scale part; the authors expect "the outer peak will appear more clearly as increasing the grid resolution towards that used in the WRLES" (App. C, figs. 29b, 30). **Shown** (the extrapolation **Stated**)
20. Halving the wall-normal resolution ($N_y=71$, about 30 points in $\delta$) "has little effect" on the near-wall structures and spectra (App. C, figs. 27e,f, 29c). **Shown**
21. The near-wall structures depend on the wall-parallel resolution: their length scales shrink as the grid is refined (App. C, fig. 27). **Shown**
22. The outer peak does not appear with KEEP (with or without the low-pass filter) or with the Smagorinsky model either (App. D, fig. 33). **Shown**
23. The Choi & Moin (2012) estimates are quoted: $N_{\mathrm{DNS}}\sim Re^{37/14}$, $N_{\mathrm{WRLES}}\sim Re^{13/7}$, $N_{\mathrm{WMLES}}\sim Re$ (§1). **Stated** (cited)
24. The total shear-stress balance $\langle\tau_w\rangle\approx\langle\mu\,\mathrm du/\mathrm dy\rangle+\langle\mu_t\,\mathrm du/\mathrm dy\rangle-\langle\rho\rangle\langle u''v''\rangle_\rho$ (Eq. 4.2, from Kawai & Larsson 2012, thin-layer and equilibrium approximations) explains WMLES accuracy for the mean velocity and the Reynolds shear stress; it does not extend to the normal stresses (§4.1, §6.1). **Derived** (cited)
25. The DNS agrees with the incompressible DNS of Schlatter & Örlü (2010) at $Re_\tau\approx700$ and 1250 for mean velocity, Reynolds stresses and TKE budget, with "slight differences" (App. A, figs. 23, 24). **Shown**
26. Bose & Park (2018) had called the WMLES predictability of the outer peak "highly questionable"; the authors claim to be the first to address it and the first to characterize WMLES near-wall structures in three dimensions (§1, §6.1). **Stated** (novelty claim)

Method details (§2): SGS model is the selective mixed-scale model of
Lenormand, Sagaut & Ta Phuoc (2000), $\nu_t=C_m|\bar S|^{1/2}(q_c^2)^{1/4}\Delta^{3/2}$
(Eq. 2.8 with $\alpha=0.5$, $C_m=0.06$, $q_c^2$ the test-field kinetic energy
of a three-point test filter, selection function with $\theta_0=20^\circ$,
$n=2$), $\Delta$ the cube root of the cell volume times an anisotropy factor
(Eqs. 2.9–2.11); the wall model solves the momentum and energy ODEs
(2.17)–(2.18) with a mixing-length eddy viscosity with van Driest damping,
$\kappa=0.41$, $A^+=17$, $Pr_{t,\mathrm{wm}}=0.9$, on 39 points; the
Smagorinsky runs of App. D use $C_s=0.1$ without damping. Matching heights
$h^+_{\mathrm{wm}}\approx54$, 101, 191, 357, 677 and 1287 for the six
$Re_\tau$.

# Printed slips

- **§3, domain:** the text prints "[40.0, 6.0, 10.0] × δ0 in the streamwise (x), wall-normal (y) and spanwise (z) directions", while fig. 2 labels the wall-normal extent $10\delta_0$ and the spanwise extent $6\delta_0$. *(compiler check, not in the sources)* The fig. 15 caption gives a wall spacing of $0.05\delta_0$ in $x$ and $z$; with $N_z=121$ that spacing needs $L_z=6\delta_0$, and $40\delta_0/800=0.05\delta_0$ matches the tabulated $\Delta x^+=\Delta z^+$ of the WMLES.
- **Table 1, DNS1 and DNS3:** for the WMLES rows and DNS2 the printed $\delta/\Delta x$ equals $Re_\tau/\Delta x^+$ to rounding (e.g. $2204/80.9=27.2$). *(compiler check, not in the sources)* For DNS1, $715/9.5=75.3$ and $715/4.8=149$ against the printed 77 and 154; for DNS3, $2407/10.0=241$ and $2407/5.0=481$ against the printed 250 and 500.
- **§5.2.1:** "the hole parameter h = 1.75", lowercase, where Eq. (5.1) and the rest of the paper use $H$; "the frequency of occurrence outside the hall" for "hole".
- **§2.3:** "The wall boundary conditions at y = y0 for (2.17) and (2.18)", with $y_0$ undefined; the ODEs are stated to be solved between $y=0$ and $y=h_{\mathrm{wm}}$.
- **Eq. (2.6):** the bulk term $[\beta-\tfrac23(\mu+\mu_t)]S_{kk}$ is printed without $\delta_{ij}$.
- **Eq. (D1):** $\nu_{t,sgs}=(C_s\Delta)^2\tilde S$, without the modulus bars of $|\tilde S|$ defined at Eq. (2.8).

# Notation map

| Maeyama & Kawai | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar\phi$, $\phi'$ | $\langle\phi\rangle$, $\phi'$ | **collision:** the overbar is a Reynolds (time and span) average, not the LES filter |
| $\tilde\phi=\overline{\rho\phi}/\bar\rho$, $\phi''$ | $\langle\phi\rangle_\rho$, $\phi''$ | Favre average; in the LES equations of §2 the tilde is the Favre filter (agrees) |
| $\hat\phi$ | (conditionally averaged quantity, §5.3) | **collision:** also the three-point test filter of Eq. (2.13), which agrees with the registry hat |
| $-\bar\rho\widetilde{u''v''}$, $\bar\rho\widetilde{u_i''u_i''}$ | $-\langle\rho\rangle\langle u''v''\rangle_\rho$, $\langle\rho\rangle R_{ii}$ (Favre form) | positive convention |
| $\tilde k=\tfrac12\widetilde{u_i''u_i''}$ | $k$ | $k$ in Eq. (2.4) is the resolved kinetic energy $\tfrac12u_iu_i$ |
| $\tau_{ij}$ | $\sigma_{ij}$ plus the modelled stress $2\mu_tS^d_{ij}$ | **collision** with the registry SGS stress $\tau_{ij}$ |
| $\nu_{t,sgs}$, $\mu_{t,sgs}$, $\mu_t$ | $\nu_t$, $\mu_t$ | SGS eddy viscosity |
| $\mu_{t,wm}$ | $\mu^w_{\mathrm{sgs}}$ | wall-model eddy viscosity (registry §11) |
| $\lvert\tilde S\rvert=(2\tilde S_{ij}\tilde S_{ij})^{1/2}$ | $\lvert\bar S\rvert$ | agrees (factor two) |
| $C_m$, $\alpha$, $q_c^2$, $\theta$, $\theta_0$, $n$ | (selective mixed-scale model constants and variables) | page-local; $\theta$ is a vorticity angle, not the momentum thickness |
| $C_s$ | $C_s$ | agrees (App. D, 0.1) |
| $\Delta$, $C_w$ | $\Delta$, (anisotropy factor) | $C_w$ is not the WALE constant |
| $h_{wm}$, $U_\parallel$ | $h_{\mathrm{wm}}$, (wall-parallel velocity of the wall model) | $h_{\mathrm{wm}}=y_{10}$ |
| $\kappa$, $A^+$, $Pr_{t,wm}$ | $\kappa$, $A^+$, (wall-model $Pr_t$) | agree |
| $u_\tau$, $\delta_\nu$, $y^+$ | $u_\tau$, $\delta_\nu$, $y^+$ | agree (wall density and viscosity) |
| $u_\tau^*$, $\delta_\nu^*$ | $u_\tau^*$, (semi-local viscous length) | registry $(\cdot)^*$ semi-local scaling (Coleman et al. 1995); agrees |
| $\delta_\nu^{*,sgs}$ | $\delta^{*,\mathrm{sgs}}_\nu$ | page-local, the paper's new scaling (Eq. 5.5) |
| $l_z^+$, $l_z^*$, $l_z^{*,sgs}$ | (near-wall spanwise length scale in three scalings) | page-local |
| $H$ | $H_{\mathrm q}$ | hyperbolic-hole parameter; **collision** with the shape factor $H$ |
| Q1–Q4 | (quadrants of $(u'',v'')$) | Q2 ejection, Q4 sweep |
| $C, P, T_d, T_p, D_v, D_d, M, \Pi_d$ | (convection), $\langle\rho\rangle P_k$, (turbulent and pressure transport, viscous diffusion), $\langle\rho\rangle\varepsilon$, (mass flux), $\Pi^{\mathrm t}_{\mathrm{pd}}$ | TKE-budget terms (Kawai 2019); **collision:** $M$ is not the Mach number |
| $\delta$, $\delta_0$ | $\delta_{99}$ at $x=30\delta_0$, (reference length, about the inlet $\delta_{99}$) | $\delta\approx1.5\delta_0$ |
| $\bar u_{vD}$ | (van Driest transformed velocity) | Eq. (4.1) |
| $k_z$, $\lambda_z$, $\Phi_{u''u''}$, $R_{u''u''}$ | (spanwise wavenumber, wavelength, spectrum, two-point correlation) | **collision:** $k_z$ is not the kinetic energy |
| $\beta$ | $\mu_b$ | bulk viscosity, set to zero; **collision** with the field-inversion $\beta$ |
| $N_{DNS}$, $N_{WRLES}$, $N_{WMLES}$ | (grid-point counts) | not the polynomial degree $N$ |

# Reference list

87 printed references, author–year (JFM) style, alphabetical. The list is
merged complete into the [bibliography](/bibliography.md) with `citedby`
this slug; the work itself was already in the bibliography as a cited entry
(cited by [maejima-2025](/sources/maejima-2025.md)) and becomes the
ingested entry. Same-author same-year works take suffixes in printed order
(Marusic et al. 2010a, 2010b). The cited Bose & Park (2018), Kuya, Totani &
Kawai (2018) and Lozano-Durán, Bose & Moin (2022) are the ingested
[bose-2018](/sources/bose-2018.md), [kuya-2018](/sources/kuya-2018.md) and
[lozanoduran-2022](/sources/lozanoduran-2022.md). Recorded as printed: Park
& Moin (2014) as "Phys. Fluids 26 (1), 37–48" (venue compared at merge with
the existing entry), Larsson et al. (2016) as "Mech. Engng Rev. 3 (1),
15–00418", Jiménez (2018) without a page or article number. No printed
duplicate, no unparseable item.

# Pages created or updated

Chunk 12 (2026-10-28). This source is cited on:

- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [Attached-eddy hypothesis](/definitions/attached-eddy-hypothesis.md)
- [Compressible velocity transformations](/definitions/compressible-velocity-transformation.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Log-layer mismatch](/definitions/log-layer-mismatch.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [Equilibrium wall model](/methods/equilibrium-wall-model.md)
- [Inflow turbulence generation](/methods/inflow-turbulence-generation.md)
- [Slip-wall models](/methods/slip-wall-model.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
