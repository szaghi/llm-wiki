---
type: Source
title: "Kumar et al. (2023) — Acceleration of turbulent combustion DNS via principal component transport"
description: "Replaces energy and species transport in a DNS of a lean premixed methane–air slot Bunsen flame by four transported principal components closed with small neural networks trained on a 2D species DNS, with a semi-implicit pressure update; the 3D surrogate reproduces the species DNS at 73 times lower cost."
resource: "doi:10.1016/j.combustflame.2023.112903"
source_kind: paper
authors: [Kumar A., Rieth M., Owoyele O., Chen J.H., Echekki T.]
year: 2023
venue: "Combust. Flame 255:112903"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Combustion_and_Flame_Kumar_Acceleration_of_turbulent_combustion_DNS_via_principal_compo.pdf"
tags: [combustion, dns, data-driven, neural-network]
timestamp: 2026-10-28T01:52:00Z
---

# Summary

Kumar et al. (2023) accelerate the [direct numerical simulation](/definitions/direct-numerical-simulation.md)
of turbulent premixed combustion by transporting, instead of the energy
and the 16 species of a skeletal methane–air mechanism, a few principal
components (PCs) of the thermochemical state ("surrogate PC DNS"). PCA of
the temperature and seven representative species, sampled from a 2D
species DNS, gives eight PCs of which four carry more than 99% of the
variance. The PC source terms and diffusion coefficients, and $\mu$,
$\gamma$, $T$ and the mixture molecular weight, are regressed on the PCs
with small neural networks trained by Levenberg–Marquardt (regression of
thermochemistry, not of a subgrid stress: contrast the
[neural-network SGS models](/methods/neural-network-sgs-model.md)); a
further network recovers non-transported species such as HO$_2$. A
semi-implicit pressure update from the equation of state, linearized
with the networks' Jacobians, removes the acoustic time-step limit: the
step grows from 5 ns to 60 ns. The method is a competitor of the
chemistry-reduction and tabulation strategies of
[flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md),
and the authors argue that 1D laminar flames are inadequate training
data for turbulent conditions.

The code is S3D (eighth-order explicit differencing, a tenth-order filter
applied periodically, see [numerical dissipation](/properties/numerical-dissipation.md);
fourth-order Runge–Kutta), the case a lean ($\phi_{\mathrm{eq}}=0.7$)
slot-burner Bunsen flame after Sankaran et al. (2015), with turbulence
fed at the inlet from a prescribed length scale, rms and spectrum
([inflow turbulence generation](/methods/inflow-turbulence-generation.md)).
Trained only on the 2D species DNS (an [a priori](/definitions/a-priori-and-a-posteriori-testing.md)
step), the coupled 3D surrogate reproduces the species DNS in
instantaneous fields, mean progress variable, centreline turbulence
intensity and dissipation, conditional means, strain rate and curvature.
The cost per flow-through time falls from 18674.4 to 256.9 CPU hours
(73 times) and the memory by 5.5 times; two further PC-only cases at a
lower jet velocity stay within the composition space of the 2D training
data.

# Version read

Version of record (Combust. Flame 255:112903, Elsevier; received 21 Feb
2023, accepted 7 Jun 2023, online 14 Jun 2023), 16 pages, all read;
Eqs. (9), (14)–(19) and (23) checked visually. Page-1 title, authors and
DOI match the metadata; no identity problem. Numbering on this page is
that of this version.

# Key claims

The source's slot width $h$ is the registry's $h_n$; its turbulence
intensity $u'=\sqrt{(u_x'^2+u_y'^2+u_z'^2)/3}$ is written
$u'_{\mathrm{rms}}$ here; its laminar flame speed $S_L$ is $s_{\mathrm L}$;
its dissipation $\epsilon=\langle\sigma_{ij}\partial_ju_i'\rangle/\langle\rho\rangle$
is $\varepsilon$ (Eq. 23, overbar a time and span average). The PC
vector is $\boldsymbol\psi_{\mathrm{PC}}=\mathbf Q^T\boldsymbol\Phi_{\mathrm{tc}}$,
with $\boldsymbol\Phi_{\mathrm{tc}}$ the thermochemical vector and
$\mathbf Q$ the PCA eigenvector matrix (Eq. 8); PC sources
$\dot{\boldsymbol\omega}_\psi=\mathbf Q^T\dot{\boldsymbol\omega}_{\Phi}$
(Eq. 10) and diffusion matrix $\mathbf D_\psi=\mathbf Q^T\mathbf D_\Phi\mathbf Q$
(Eq. 11), diagonalized by a constant rotation of the PCs.

1. Surrogate PC DNS with four transported PCs, closed by networks trained on a 2D species DNS, reproduces instantaneous profiles and statistics of turbulence, flame topology and flame–turbulence interaction of a 3D species DNS of a lean premixed methane–air slot Bunsen flame (Abstract, §3.6, §4). **Shown**
2. The leading four of the eight PCs (from $T$ and seven representative species) exceed 99% of the cumulative variance, the retention criterion (§3.3–3.4, Fig. 3). **Shown**
3. PC3 and PC4 carry the H$_2$ and H contributions, together about 2% of the variance, but are "essential for capturing curvature and differential diffusion effects" (§3.4, Fig. 4). **Stated**
4. PC1 is dominated by reactants, products, temperature and CO; PC2 by CO, CO$_2$, temperature and O$_2$ (§3.4, Fig. 4). **Shown**
5. The 3D surrogate solves 8 equations (continuity, three momentum, four PCs) against 21 for species DNS (continuity, three momentum, energy, 16 species) (§3.3). **Stated**
6. Cost per flow-through time (Cori-Haswell): 3D species DNS 18674.4 CPU h and 1382.4 GB against 256.9 CPU h and 252.0 GB for the PC DNS, speed-up 73 and memory saving 5.5; in 2D 87.1 CPU h, 58.2 GB against 2.3 CPU h, 23.7 GB, speed-up 38 and saving 2.5 (Table 3, §3.3). **Shown**
7. The parametric PC cases B2 and B3 cost 384.2 CPU h each (flow-through time 0.6 ms), about 48 times less than the 3D species DNS (§3.3, Table 3). **Shown**
8. The 3D species DNS costs more than 200 times the 2D training DNS, and the 3D PC DNS about three times it: building the closure from a 2D DNS adds no significant overhead (§3.3). **Shown**
9. Per time step the surrogate is about 1.5 times faster in evaluating source terms and diffusion coefficients (shallow networks); a further factor 4.2 comes from the lower spatial resolution, mainly through the cost of derivatives (§3.3). **Shown**
10. The Ren–Goldin chemical time scale $\tau_{\mathrm{ch}}=\min_kY_k/(|\dot\omega_k|/\rho)$ (Eq. 20, scaling constant 1) is 1.5 ns in species DNS and 18 ns in PC DNS, so an order of magnitude larger chemistry step is expected (§3.3). **Shown**
11. Acoustic limits are about 10 ns (species) and 20 ns (PC); the semi-implicit pressure update raises the PC limit to about 60 ns; steps used 5 ns and 60 ns, against 2 ns in Sankaran et al. (§2.2, §3.2–3.3, Tables 1–2). **Shown**
12. The semi-implicit pressure evaluation (Eqs. 12–18: $\rho$, $T$ and $W_{\mathrm{mix}}$ Taylor-expanded to the next step with the network Jacobians $\mathrm dT/\mathrm d\boldsymbol\psi_{\mathrm{PC}}$, $\mathrm dW_{\mathrm{mix}}/\mathrm d\boldsymbol\psi_{\mathrm{PC}}$ and backward differences of the previous step) "eliminates stringent CFL restrictions imposed by the acoustic waves" and "does not impact the predictive capabilities" (§2.2). **Stated** (no run isolates it)
13. The finest structure is the HCO profile, about 560 μm thick (1% of peak, 1D flame) in species DNS; the thinnest PC (PC3) is about 800 μm; the 40 μm and 65 μm grids give about 14 and 12 points across them (§3.2–3.3). **Shown**
14. In the 3D species DNS 99% of the turbulent kinetic energy spectrum lies at scales above 120 μm (§3.3). **Stated**
15. Sankaran et al. used 20 μm but found 40 μm adequate (§3.2). **Stated** (cited)
16. Training data from 1D laminar flames do not reproduce turbulent states; stacked snapshots of a 2D species DNS (wrinkling, flame–flame interaction, pockets, local extinction, strong curvature) span the composition space of the 3D DNS (§3.1, §3.4, Fig. 2). **Shown**
17. The 2D training data, transients included, span all states accessed by the 3D PC cases B1–B3 despite different inlet and turbulence conditions (§3.7, Fig. 13, PC1–PC2 projection). **Shown**
18. Mean absolute errors of instantaneous species (Eqs. 21–22) are comparable in 2D and 3D, normalized values from $5.4\times10^{-3}$ (CH$_4$, 2D) to $8.8\times10^{-2}$ (OH, 3D) (§3.5, Table 4). **Shown**
19. The non-representative HO$_2$, recovered from the PCs by a post-processing network, is "a stringent test" and is reproduced in 2D and 3D (§3.5–3.6, Figs. 6, 8). **Shown**
20. Larger source-term networks fit the training data better but are "very sensitive to input fluctuations"; the $[4\ 15\ 10\ 4]$ architecture reaches correlation coefficients of at least 99.9% (§3.4). **Shown** (correlation) / **Stated** (robustness)
21. Second-order optimizers (Levenberg–Marquardt) are a better choice than first-order ones (gradient descent, Adam) for this regression (§3.4). **Stated** (cited)
22. $u'_{\mathrm{rms}}$ and $\varepsilon$ along the centreline decay downstream alike in the species and PC DNS despite the grid difference; the mean progress-variable field and its $c=0.65$ iso-contour agree (§3.6, Figs. 9–10). **Shown**
23. Conditional means of CH$_4$ and CO on $c$ at $x=5$ mm agree; H$_2$ and HO$_2$ differ slightly on the reactant side (§3.6, Fig. 11). **Shown**
24. The tangential strain rate is constant up to some $c$ and then drops sharply, the curvature magnitude decreases monotonically with $c$, and the PC DNS reproduces both (§3.6, Fig. 12). **Shown**
25. Lower jet velocity (B2, B3) shortens the flame; higher turbulence intensity (B2 against B3) shortens it further through tip pinch-off and broadens the mean $c$ iso-contours; the strain-rate peak is largest in B1 and smallest in B3 (§3.7, Figs. 14–16). **Shown**
26. The peak conditional mean of $|\nabla c|$ at $x=5$ mm is lowest for B1, with B2 and B3 similar, consistent with Sankaran et al.'s finding that the peak decreases (thickening increases) with turbulence intensity, B1 having the highest local intensity there (§3.7, Fig. 17). **Shown**
27. The results "can be obtained in a single day on a 10-core CPU machine", whereas species DNS "would take more than two and a half months" (§4). **Stated**; *(compiler check, not in the sources)* $256.9/10\approx26$ h and $18674.4/10\approx1867$ h $\approx78$ days, consistent with Table 3.
28. Choosing the training data and the representative species is "largely domain expert dependent"; complex fuels need more automated strategies (§2.2, §4). **Stated**

# Printed slips

- **Tables 1–2, §3.2:** the 2D domain is printed $21.6h\times12h$ (Table 1) and the 3D domain $21.4h\times12h\times3.5h$ (Table 2), while §3.2 says the 3D configuration is the 2D one "uniformly extended in the spanwise z-direction".
- **Table 2, §3.2:** the PC DNS spacing is printed 65 μm (species DNS 40 μm), uniform and the same in all directions, on $N_z=70$ points (species $N_z=105$). *(compiler check, not in the sources)* With $L_z=3.5h=4.2$ mm and the printed uniform spanwise spacing, $L_z/N_z$ gives 40 μm for 105 points and 60 μm for 70 points.
- **§3.6:** $u'$ and $\epsilon$ are "averaged over the same time window as Fig. 7", but Fig. 7 shows instantaneous iso-surfaces at $t=0.1$ ms; the time-averaged fields are those of Fig. 9 (0.15 ms).
- **§3.6:** "Figure 7 compares 2D iso-surfaces of the progress variable", while the Fig. 7 caption reads "(3D DNS) Comparisons of instantaneous iso-surfaces".
- **Eqs. (8)–(9):** the PCs are written $\psi$ in Eq. (8) and $\Psi_k$ in Eq. (9).
- **References:** ref. [27] prints the page range "97–413"; ref. [7] begins its title "Ta multi-timescale".
- **Typos:** "showd" (§3.5), "Levenberg-Marquadt" (§3.4), "instantanenous" (Table 4 caption), "a constant time step of 2 ns in used" (§3.2), "$D_{\psi_k}$ $\dot\omega_{\psi_k}$ are" (after Eq. 9, "and" missing).

# Notation map

| Kumar et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar\rho$, overbar in Eq. (23) | $\langle\rho\rangle$, $\langle\cdot\rangle$ | **collision:** a time and span average in post-processing, not an LES filter |
| $u_x',u_y',u_z'$ | $u',v',w'$ | Reynolds fluctuations |
| $u'$ | $u'_{\mathrm{rms}}$ (page-local) | turbulence intensity; **collision** with the registry fluctuation $\phi'$ |
| $\epsilon$ | $\varepsilon$ | Eq. (23) |
| $\tau_{ji}$ | $\sigma_{ij}$ | molecular viscous stress (Stokes hypothesis), not a Reynolds or subgrid stress |
| $p$, $\rho$, $T$, $\mu$, $\gamma$ | $p$, $\rho$, $T$, $\mu$, $\gamma$ | agree |
| $e_0$ | $E/\rho$ | specific total energy (the registry's $E$ is per unit volume) |
| $h$ (enthalpy) | (mixture enthalpy, page-local $h_t$) | **collision** with the registry cell size $h$ |
| $h$ (geometry) | $h_n$ | slot width, 1.2 mm |
| $\theta=(T,Y_1,\dots,Y_{N-1})$ | $\boldsymbol\Phi_{\mathrm{tc}}$ (page-local) | **collision** with the momentum thickness $\theta$ and the trainable parameters $\boldsymbol\theta$ |
| $\psi$, $\Psi_k$, $N_{PC}$ | $\boldsymbol\psi_{\mathrm{PC}}$ (page-local), $N_{\mathrm{PC}}$ | principal components; **collision** with the $\psi$ of the $k$-$\sqrt kL$ model |
| $Q$ | $\mathbf Q$ (page-local) | PCA eigenvector matrix |
| $N$ (species) | $N_{\mathrm{sp}}$ (page-local) | **collision** with the polynomial degree $N$ |
| $D_k$, $\dot\omega_k$, $Y_k$, $W_{mix}$, $R_u$ | (species diffusivity, source, mass fraction; mixture molecular weight; universal gas constant) | page-local |
| $\tau_{chem}$ | $\tau_{\mathrm{ch}}$ | chemical time scale (registry §11) |
| $S_L$ | $s_{\mathrm L}$ | laminar flame speed; **collision** with the Lundquist number $S_L$ |
| $c$ | $c$ | normalized-temperature progress variable, as on the tabulated-chemistry page |
| $Re_t=u'l_t/\nu$, $l_t$ | (turbulence Reynolds number, length scale) | page-local; $l_t$ not printed |
| $\phi$ | $\phi_{\mathrm{eq}}$ | equivalence ratio |
| $\Delta t$, $\Delta x$ | $\Delta t$, $h$ | time step; grid spacing |
| $L_x,L_y,L_z$, $N_x,N_y,N_z$ | $L_x,L_y,L_z$, $N_x,N_y,N_z$ | domain lengths and grid points |
| $f(s)$, $q$, $s^*$, $\beta$ (Eq. 19) | (grid-stretching function and parameters) | page-local; $\beta$ is not a model constant |

# Reference list

43 printed references, numbered style ([1]–[43]). The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this
slug. Ref. [1] (Pope 1997) is printed with the venue "Combust. Sci. Tech.
1 (1997) 41–63", while the entry of the same title, year and pages
already in the bibliography records Combust. Theory Model.; it is
flagged for a venue check at the merge. Refs. [18] and [19], both Ranade
& Echekki (2019, Combust. Flame), take suffixes in printed order. Ref.
[24] (Zdybał et al., Proc. Combust. Inst.) is printed with a DOI and no
volume or pages; ref. [31] is a book chapter printed without the book
title; ref. [42] is a web document. No printed duplicate, no unparseable
item.

# Pages created or updated

Chunk 12 (2026-10-28). This source is cited on:

- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md)
- [Inflow turbulence generation](/methods/inflow-turbulence-generation.md)
- [Neural-network subgrid-scale models](/methods/neural-network-sgs-model.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
