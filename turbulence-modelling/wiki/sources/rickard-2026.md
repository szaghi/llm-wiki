---
type: Source
title: "Rickard & Kasbaoui (2026) — Modelling the wall slip in large eddy simulations with immersed boundaries"
description: "Extends volume-filtering immersed boundaries to wall-modelled LES: with a truncated, non-rescaled filter the only unclosed wall quantity is the filtered velocity at the wall, the wall slip; a priori filtering of channel DNS at Re_tau 5200 calibrates a Van Driest slip model and a slip-length model from exact commutation identities."
resource: "doi:10.1017/jfm.2026.11788"
source_kind: paper
authors: [Rickard M.Z., Kasbaoui M.H.]
year: 2026
venue: "J. Fluid Mech. 1039:A17"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2026_Crossref_Journal_of_Fluid_Mechanics_Rickard_Modelling_the_wall_slip_in_large_eddy_simulations_with_immer.pdf"
tags: [les, wall-model, wmles, immersed-boundary, filtering, a-priori-a-posteriori]
timestamp: 2026-10-27T15:51:00Z
---

# Summary

Rickard & Kasbaoui (2026) extend the volume-filtering
[immersed boundary method](/methods/immersed-boundary-method.md) of Dave,
Herrmann & Kasbaoui (2023) from its DNS limit to
[wall-modelled LES](/methods/wall-modelled-les.md), which they call
immersed boundary-modelled LES (IBMLES). The incompressible equations are
convolved with a compact, symmetric, unit-integral kernel $G$ of support
$\Delta_f$ that is truncated by the fluid indicator and not rescaled near
walls. The deficit is carried by a fluid volume fraction $\varphi_f$
($=1/2$ at a planar wall), and filtered fields extend $\Delta_f/2$ into the
solid. Exact commutation identities turn the wall terms into an
immersed-boundary body force; with the subgrid stress $\tau_{ij}$
they leave a closed residual viscous stress. The only unclosed wall
quantity is the filtered velocity at the wall, the wall slip, so modelling
it is a wall model. This is the [LES](/definitions/large-eddy-simulation.md)
filtering framework of the paper, set against wall-resolved LES with
refined filters and the truncated-and-rescaled filter of Bose & Moin (2014).

An [a priori](/definitions/a-priori-and-a-posteriori-testing.md) analysis
filters the Lee & Moser [DNS](/definitions/direct-numerical-simulation.md)
of [turbulent channel flow](/benchmarks/turbulent-channel-flow.md) at
$Re_\tau=5200$ with $\Delta_f^+=50$ to 300. The mean streamwise slip is large
($6.93u_\tau$ at $\Delta_f^+=50$, $13.5u_\tau$ at 300) and grows
logarithmically; wall-normal and spanwise slips are negligible. Two
closures follow. A Van Driest slip model filters the Van Driest profile of
the [law of the wall](/definitions/law-of-the-wall.md) ($\kappa=0.41$,
$A^+=26$) and fits it explicitly for $\Delta_f^+\ge100$. A slip-length model
derives the Bose & Moin form from the exact commutation identity rather
than from a Taylor argument; its gradient ratio is fitted as a power law
of $\Delta_f^+$. Four kernels change the results only slightly. A dynamic
slip-length procedure from the Germano identity of the
[dynamic procedure](/methods/dynamic-procedure.md) is proposed but not
tested, and existing subgrid closures such as dynamic
[Smagorinsky](/methods/smagorinsky-model.md) are expected to apply to
$\tau_{ij}$. No a posteriori simulation is run. The introduction recalls
the [grid-point requirements](/results/les-grid-point-requirements.md) of
DNS, wall-resolved and wall-modelled LES.

# Version read

Version of record (J. Fluid Mech. 1039:A17, Open Access, CC-BY 4.0),
33 pages, all read; equation pages checked visually because the text layer
garbles the mathematics. Page 1 matches Crossref (title, authors, volume,
article number, DOI). Equation, section, figure and table numbers on this
page are those of the version of record.

# Key claims

Page-local symbols: $G_1$ the one-dimensional kernel factor
($G=G_1(x)G_1(y)G_1(z)$); $\Delta_f$ the kernel support width (the source's
$\delta_f$); $\varphi_f$ the fluid volume fraction and $\varphi_{f,w}$ its wall
value (the source's $\alpha_f$, $\alpha_{f,w}$); $\Sigma$ the surface density $\iint_{S_w}G\,dS$; $\boldsymbol F_{\mathrm{IB}}$
the immersed-boundary body force; $R^\mu_{ij}$ the residual viscous stress;
$\boldsymbol u_{\mathrm{slip}}=\bar{\boldsymbol u}|_w-\boldsymbol u_w$ the
wall slip; $\boldsymbol\ell$ the slip lengths; $\boldsymbol\Lambda$ the ratio
of the mean filtered wall gradient to the mean gradient of the filtered
velocity (the source's $\boldsymbol\lambda$); $a_0,b_0,n_0$ and $a_1,n_1$
the fit constants.

1. Volume filtering with a truncated, non-rescaled kernel and a volume fraction $\varphi_f$ removes the commutation errors of wall-resolved and wall-modelled LES with variable filters, and turns boundary conditions into volumetric forcing, which gives an immersed boundary method directly (§2.1). **Stated** (identities derived in Dave et al. 2023, which the paper recalls as Eqs. 2.8–2.13)
2. The volume-filtered momentum equation (2.22) contains two unclosed terms, $\tau_{ij}$ and $\boldsymbol F_{\mathrm{IB}}$; the residual viscous stress $R^\mu_{ij}$ (2.17)/(2.18) is closed but non-trivial (§2.2). **Derived**
3. $\boldsymbol F_{\mathrm{IB}}$ is approximated to $O(\Delta_f^2)$ by the surface integral (2.24) and is non-zero only in a band of width $\Delta_f$ around the interface for a compact kernel (§2.2). **Derived**
4. The wall stress relates to the wall slip through (2.25), so the slip is the only unclosed term and modelling it is equivalent to specifying a wall model (§2.3). **Derived** (following Dave et al. 2023)
5. No-slip ($\boldsymbol u_{\mathrm{slip}}=0$) holds only in the "DNS limit" $\Delta_f^+<1$ (§2.3). **Stated**
6. At the wall $R^\mu_{ij}$ is linear in $\boldsymbol u_{\mathrm{slip}}$ (2.27), hence significant whenever the slip is, i.e. at $\Delta_f^+=O(100)$ (§2.3). **Derived**
7. For a planar wall $\varphi_{f,w}=1/2$ for any symmetric kernel and filter size, and $\Sigma_w=O(1/\Delta_f)$ (§2.3, Fig. 4). **Derived / Shown**
8. Away from the wall ($y\gtrsim\Delta_f$) the mean filtered velocity collapses onto the DNS profile with a log region for $y^+>\Delta_f^+$; near the wall the filtered profiles lose the viscous sublayer and buffer layer (§3.2, Fig. 5). **Shown**
9. Mean streamwise slip $\langle u_{\mathrm{slip}}\rangle/u_\tau=6.93$ at $\Delta_f^+=50$ and $13.5$ at $\Delta_f^+=300$, growing logarithmically with $\Delta_f^+$; mean spanwise and wall-normal slips are negligible (§3.2, Fig. 6). **Shown**
10. The streamwise slip r.m.s. is $\approx1.5u_\tau$ at all filter sizes, the wall-normal $\approx0.02u_\tau$ and the spanwise $\approx0.3u_\tau$; the fluctuations plateau for $\Delta_f^+\ge100$ (§3.2, Fig. 6). **Shown**
11. The slip field carries near-wall high- and low-speed streaks at $\Delta_f^+=50$ and outer-layer large-scale structures at $\Delta_f^+=300$ (§3.2, Fig. 7, a $5000\times2500$ wall-unit patch). **Shown**
12. Filtered r.m.s. fluctuations decrease with $\Delta_f$; they agree best with DNS near the centreline and worst near the wall (§3.2, Fig. 8). **Shown**
13. The averaged streamwise balance (3.3) (Appendix A) gives a linear total stress $\tau_w(1-y/\delta)$ for $\Delta_f/2\ll y\ll2\delta-\Delta_f/2$ (3.4); near the wall the profile is rounded over a width $\propto\Delta_f$, the $G_1$ terms coming from $\boldsymbol F_{\mathrm{IB}}$ (§3.3, Fig. 9). **Derived / Shown**
14. The subgrid stress resembles the unfiltered viscous stress (largest at the wall); its normalized peak grows from 0.24 at $\Delta_f^+=50$ to 0.57 at $\Delta_f^+=300$. The filtered Reynolds stress decreases with $\Delta_f$ and its peak moves towards the centreline (§3.3, Fig. 10). **Shown**
15. The residual viscous stress is larger than the filtered viscous stress at every filter size tested, though of comparable magnitude; it has compact support on $[-\Delta_f/2,\Delta_f/2]$, while the filtered viscous stress has a long tail (§3.3, Fig. 10). **Shown**
16. The Van Driest slip model (4.2) agrees with the filtered-DNS mean slip for $\Delta_f^+=50$–300 ("excellent agreement") (§4.1, Fig. 11a). **Shown**
17. The explicit approximation (4.5) differs from the exact Van Driest slip by less than 1 % for $\Delta_f^+\ge100$ and diverges as $\Delta_f^+\to0$ (§4.1, Fig. 11b). **Shown**
18. A slip-length relation of the Bose & Moin form follows from the exact commutation identity (2.11): $\boldsymbol\ell=\varphi_{f,w}(\boldsymbol\Lambda-1)/(\partial\varphi_f/\partial n)|_w$ (4.13), valid for planar, curved (curvature resolved by $\Delta_f$), static and moving walls (§4.2). **Derived**
19. $\boldsymbol\Lambda\to(1,1,1)$ and $\boldsymbol\ell\to0$ as $\Delta_f\to0$ (4.24): the model recovers no-slip, the DNS limit (§4.2, §7). **Derived**
20. Fitted slopes of the joint PDFs of the filtered wall gradient and the gradient of the filtered velocity give $\Lambda_x=1+0.251\,\Delta_f^{+\,0.5385}$ (4.26) and $\ell_x^+=0.0798\,\Delta_f^{+\,1.5385}$ (4.27) for the cosine kernel; the PDF peak at $\Delta_f^+=50$ lies near $(0.2,0.6)$ (§4.2, Figs. 12–13). **Shown**
21. $\Lambda_y=\Lambda_z=1$ (4.25) reproduces the negligible wall-normal and spanwise slip of the channel (§4.2). **Stated** (model choice from §3)
22. The kernel (cosine, triangle, parabolic, triweight) causes only small differences: cosine and parabolic nearly coincide, triangle and triweight give slightly lower slip; stress profiles at $\Delta_f^+=300$ differ by less than 1 % (§5, Figs. 15–16, Tables 1–2). **Shown**
23. Across kernels $a_0=0.81\pm0.21$, $b_0=-67.5\pm4.5$, $n_0=0.92\pm0.03$ for the Van Driest fit and $a_1=0.30\pm0.06$, $n_1=0.53\pm0.02$ for the slip length; roughly $\Lambda_x\approx1+0.3\,\Delta_f^{+0.5}$ and $\ell_x^+\approx0.08\,\Delta_f^{+1.5}$ (§5, §7). **Shown**
24. A dynamic slip-length procedure (6.9)/(7.4) follows from the Germano identity with the $n_1$ scaling between filter levels, $\hat\ell_{t_1}=(\hat\Delta_f/\Delta_f)^{n_1+1}\ell_{t_1}$; it is solved explicitly (positive root), not by least squares, with one slip length per direction, and is not evaluated (§6). **Derived**
25. Existing subgrid models (e.g. dynamic Smagorinsky) are expected to apply to $\tau_{ij}$ in IBMLES (abstract, §7). **Stated**
26. The $Re_\tau$ dependence of $\boldsymbol\Lambda$ is expected to be secondary to the $\Delta_f^+$ dependence but cannot be determined from one $Re_\tau$; the models are not expected to hold for rough, moving or deforming, or strongly separated flows (§4.2, §7). **Stated**
27. Cost scalings cited from Choi & Moin (2012): grid points $\sim Re^{37/14}$ (DNS), $Re^{13/7}$ (wall-resolved LES), linear in $Re$ (wall-modelled LES); from Piomelli (2014): for $Re>O(10^5)$ more than 90 % of the points resolve less than 10 % of the domain; channel DNS frontier $Re_\tau\approx12\,000$ (Pirozzoli 2024) (§1). **Stated**
28. Immersed boundaries on non-uniform grids introduce spurious stress oscillations that can corrupt the near-wall turbulent viscosity; Verzicco (2023) suggests immersed-boundary LES may be possible only on uniform grids with immersed-boundary-adapted wall models (§1). **Stated**

# Printed slips

- **Eq. (2.18):** the third term is printed $(2/3)(\nabla\alpha\cdot\overline{\boldsymbol u}_f)\boldsymbol I$, without the subscript $f$ used elsewhere.
- **Eq. (2.25):** the bracket multiplied by $\rho_f\alpha_{f,w}/\Sigma_w$ adds $\frac{d}{dt}(\boldsymbol u_w+\boldsymbol u_{slip})$ to $\nabla\cdot(\overline{\boldsymbol\tau}^R_f+\boldsymbol R_\mu-\boldsymbol\tau_{sfs})$. *(Compiler check, not in the sources: the first is an acceleration, $\nabla\cdot\boldsymbol\tau_{sfs}$ is an acceleration because the subgrid stress is kinematic, but $\nabla\cdot(\overline{\boldsymbol\tau}^R_f+\boldsymbol R_\mu)$ is a force per unit volume; the terms agree only with a factor $1/\rho_f$ on the dynamic stresses, which elsewhere in the paper carry $\rho_f\boldsymbol\tau_{sfs}$.)*
- **Fig. 6 caption:** "Streamwise slip velocity fluctuations are approximately 10 % or less of mean slip values", while the text gives r.m.s. $\approx1.5u_\tau$ and mean $6.93u_\tau$ at $\Delta_f^+=50$. *(Compiler check, not in the sources: $1.5/6.93\approx22\%$ at $\Delta_f^+=50$ and $1.5/13.5\approx11\%$ at $\Delta_f^+=300$.)*
- **§4.1 against Fig. 11(b), Eqs. (5.4), (7.1):** the text says approximation (4.5) "provides accurate results for filter sizes $\delta^+_f\geqslant50$", while the figure and the summary equations state validity for $\Delta_f^+\ge100$. *(Compiler check, not in the sources: Eq. (4.5) with $\varphi_{f,w}=1/2$, $\kappa=0.41$ and the natural logarithm gives $6.32$ at $\Delta_f^+=50$, against the filtered-DNS $6.93$, and $13.53$ at $\Delta_f^+=300$, against $13.5$.)*
- **Typos:** "elongated and titled upwards" (§4.2, for tilted); a missing semicolon in "Lozano-Durán et al. 2022 Mani & Dorgan 2023" (§1).
- **Table 1 caption:** writes $(1/\alpha_w)$ for $(1/\alpha_{f,w})$ and lists the kernels in an order (cosine, triweight, triangle, parabolic) different from the rows (cosine, triangle, parabolic, triweight).
- **Citations:** in-text "Hoyas, Oberlack & Laux 2022" names three of the five authors of the listed reference; the reference "M., GERMANO, R., MOREAU & W., RODI 2002" has inverted names, and its co-authors coincide with the volume editors.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\boldsymbol u_f$, $p$, $\rho_f$, $\mu_f$, $\nu$ | $\boldsymbol u$, $p$, $\rho$, $\mu$, $\nu$ | incompressible; subscript $f$ = fluid phase |
| $\overline{\boldsymbol u}_f$, $\alpha_f\overline{\boldsymbol u}_f=\overline{\mathbb I_f\boldsymbol u_f}$ | $\bar{\boldsymbol u}$ | volume (phase-weighted) LES filter |
| $\mathcal G$, $\mathcal G_1$ | $G$, $G_1$ (page-local) | compact, symmetric, unit-integral kernel |
| $\delta_f$, $\delta_f^+$ | $\Delta_f$, $\Delta_f^+$ (page-local) | kernel support width, the LES filter width of this framework; **collision:** $\delta$ is the channel half-height |
| $\widehat{\cdot}$, $\widehat\delta_f$, $\delta_R$ | $\hat\cdot$, $\hat\Delta_f$, $\hat\Delta_f/\Delta_f$ | test filter |
| $\alpha_f$, $\alpha_{f,w}$, $\mathbb I_f$ | $\varphi_f$, $\varphi_{f,w}$ (page-local), $\mathbb I_f$ (fluid indicator) | **collision:** $\alpha_f$ is the registry's modal-filter strength (§11), $\alpha$ the DG/FV blending factor |
| $\Sigma$, $S_w$, $\boldsymbol n$, $\boldsymbol u_w$ | (page-local) | surface density; walls; solid-to-fluid normal; wall velocity |
| $\boldsymbol\tau_{sfs}$ | $\tau_{ij}$ | kinematic, full (not deviatoric), positive trace; enters as $-\rho\tau_{ij}$ |
| $\boldsymbol T_{sfs}$ | (test-level stress of the Germano identity) | |
| $\overline{\boldsymbol\tau}_f^R$, $\boldsymbol R_\mu$ | (resolved stress), $R^\mu_{ij}$ (page-local) | **collision:** $R_{ij}$ is the Reynolds stress |
| $\boldsymbol F_{IB}$ | $\boldsymbol F_{\mathrm{IB}}$ (page-local) | |
| $\boldsymbol u_{slip}$, $\boldsymbol\ell$ | $\boldsymbol u_{\mathrm{slip}}$, $\boldsymbol\ell$ (page-local) | wall slip, slip lengths |
| $\boldsymbol\lambda$ | $\boldsymbol\Lambda$ (page-local) | gradient ratio; **collision:** $\lambda$ is the Taylor microscale |
| $\langle\cdot\rangle$, $\overline u_f'$ | $\langle\cdot\rangle$, $\bar u'$ | average over snapshots, $x$, $z$ and channel halves; fluctuation of the filtered field |
| $h$ | $\delta$ | channel half-height; **collision:** $h$ is the cell size |
| $u_\tau$, $\delta_\nu$, $Re_\tau$, $\tau_w$ | same | $Re_\tau=5200$ |
| $\kappa=0.41$, $A^+=26$ | $\kappa$, $A^+$ | Van Driest profile |
| $a_0,b_0,n_0$; $a_1,n_1$ | (page-local) | fit constants (Tables 1–2) |

# Reference list

57 printed references, author–year style (JFM), alphabetical, without
DOIs. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Goc et al.
(2021) and Lozano-Durán, Bose & Moin (2022) are the ingested sources of
those keys. The Germano (2002) entry is printed with mangled names and is
recorded as printed with a note; two CTR Annual Research Briefs carry URLs;
Larsson et al. (2016) prints the article number "15-00418". No printed
duplicates and no same-key pairs within the list.

# Pages created or updated

Chunk 7 (2026-10-26), cited further in chunk 10. This source is cited on:

- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Immersed boundary methods](/methods/immersed-boundary-method.md)
- [Slip-wall models](/methods/slip-wall-model.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
