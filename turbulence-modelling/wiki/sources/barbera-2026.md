---
type: Source
title: "Barbera et al. (2026) — Mesh adaptation for DNS and LES of turbulent flows: Application to isotropic and anisotropic meshes"
description: "Builds a priori mesh-size criteria for DNS (a cell Reynolds number on a subgrid velocity estimated from the velocity Hessian) and LES (a resolved-scale-range target from a Kolmogorov-spectrum model, bounded by a mean-flow criterion), extends them to anisotropic metrics and applies them to a forced round jet, pipe flow and the PRECCINSTA burner."
resource: "doi:10.1016/j.compfluid.2026.107273"
source_kind: paper
authors: [Barbera R., Berthelon T., Balarac G., Letournel R., Ghigliotti G.]
year: 2026
venue: "Comput. Fluids 320:107273"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2026_Crossref_Computers_amp_Fluids_Barbera_Mesh_adaptation_for_DNS_and_LES_of_turbulent_flows_Applicati.pdf"
tags: [mesh-adaptation, grid-requirements, les, dns, sgs-model]
timestamp: 2026-10-29T10:04:00Z
---

# Summary

Barbera et al. (2026) ask how to define, a priori and automatically, a mesh
adequate for [DNS](/definitions/direct-numerical-simulation.md) or
[LES](/definitions/large-eddy-simulation.md) of a turbulent flow. The DNS
check $\Delta/\eta=\mathcal O(1)$ is a posteriori, and the authors' earlier
LES criteria (a mean-flow Hessian criterion plus a resolved-to-subgrid
energy ratio) fail in an anisotropic framework where the flow is
transitional: the turbulence criterion becomes inactive and the mean-flow
Hessian alone allows elements too large along directions of weak mean
variation. The paper combines three criteria. A DNS criterion estimates a
subgrid velocity $u^{<}$ from the box-filtered second-order Taylor expansion
of the instantaneous velocity and targets a cell Reynolds number
$Re^u_\Delta=\Delta u^{<}/\nu$. A scale-separation criterion assumes a
Kolmogorov spectrum between the filter and Kolmogorov scales, estimates
the subgrid shares of kinetic energy and dissipation on the current mesh
with Deardorff's algebraic relations (the constants of
[one-equation subgrid models](/methods/subgrid-kinetic-energy-equation-model.md))
and the eddy viscosity of the [σ model](/methods/sigma-model.md), and
returns the filter width that achieves a target $L/\Delta_c$. A mean-flow
criterion of Lam et al. bounds the size. LES is thus a local relaxation of
DNS where an inertial range exists, bounded by a RANS-like mean-flow
resolution; earlier anisotropic adaptation for
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) is reviewed. All criteria
are extended to anisotropic metric tensors.

The criteria drive the automatic mesh-convergence loop of YALES2 with MMG3D
remeshing ([mesh adaptation](/methods/mesh-adaptation.md)). On a forced
[round jet](/benchmarks/turbulent-round-jet.md) at $Re=4000$,
$Re^u_\Delta=0.125$ gives $\Delta/\eta\approx1.5$ and less than 5% subgrid
dissipation, and LES with $L/\Delta_c$ from 5 to 25 spans very-large-eddy to
quasi-DNS meshes; anisotropic meshes need 2–3 times fewer elements. A pipe
at $Re_D=5300$ is compared with Wu & Moin's DNS, and the non-reacting
PRECCINSTA burner with Meier et al.'s experiments, with 143,961,671 against
276,472,835 elements and 99,332 against 231,961 CPU hours for the
anisotropic and isotropic loops. The link $L/\Delta=10\Rightarrow$ 80%
resolved energy, which the authors state, ties the criterion to Pope's
([grid-point requirements](/results/les-grid-point-requirements.md)); no
value of the Kolmogorov constant is printed.
"Implicit filtering" in the paper means that the filter width of the
σ-model LES is set by the local mesh, not a simulation without subgrid
model (abstract).

# Version read

Version of record (Elsevier; received 7 February 2026, revised 13 April
2026, accepted 28 August 2026, online 4 September 2026), 15 pages, all
read; pp. 2, 3 and 7 checked visually where the text layer garbles the
equations. Page 1 matches the Crossref metadata; no identity issue.
Equation, figure, table and section numbers are those of this version.

# Key claims

Registry §11 symbols: $R_k$, $R_\varepsilon$, $\Delta_c$, $\Delta_I$,
$Re^u_\Delta$, $u^{<}$, as defined below. Page-local symbols: $\mathsf H(\cdot)$ the Hessian; $\mathsf D$ the
second-order moment of a control volume and $c_1$ its constant ($\mathsf D=c_1\Delta^2\mathsf I$
for a sphere of radius $\Delta$); $u^{<}$ the characteristic subgrid
velocity and $\langle u\rangle^{<}$ its mean-flow analogue;
$Re^u_\Delta=\Delta u^{<}/\nu$ and $Re^{\langle u\rangle}_\Delta=\Delta\langle u\rangle^{<}/(\nu+\nu_t)$
the instantaneous and mean cell Reynolds numbers; $\Delta_{\mathrm{DNS}}$,
$\Delta_{\langle u\rangle}$, $\Delta_c$, $\Delta_I$ the DNS, mean-flow,
filter and current mesh sizes; $R_k=K_{\mathrm{sgs}}/K$,
$R_\varepsilon=\varepsilon_{\mathrm{sgs}}/\varepsilon$ the subgrid shares
(superscripts $I$ current, $T$ target); $C_{\mathrm K}$ the Kolmogorov
constant; $L=K^{3/2}/\varepsilon$; $\mathsf M$ an SPD metric,
$\cap$ and $\cup$ metric intersection and union; $T_0$ the averaging
window.

1. The classical DNS check $\Delta/\eta=\mathcal O(1)$ is a posteriori and gives no constructive way to design a DNS mesh a priori or during a simulation (§1). **Stated**
2. Embedding the earlier LES criteria of Bénard et al. and Grenouilloux et al. in an anisotropic framework fails in transitional or non-fully-turbulent regions: the turbulence criterion becomes inactive and the mean-flow Hessian allows excessively large elements along weak-gradient directions (§1, citing Barbera et al. 2025). **Stated**
3. The box-filtered second-order Taylor expansion gives $u^{<}\approx\frac12\|\mathsf H(\boldsymbol u):\mathsf D\|_2$, and for a sphere of radius $\Delta$, $u^{<}\approx\frac12c_1\Delta^2\|\nabla^2\boldsymbol u\|_2$ with $c_1=1/4$ (2-D) or $1/5$ (3-D) (§2.1, Eqs. 1–4). **Derived**
4. $Re^u_\Delta$ is read by analogy with the Kolmogorov-scale Reynolds number of order one; for $Re^u_\Delta<\mathcal O(1)$ diffusion prevents motion below $\Delta$ and $u^{<}$ vanishes, "as expected in DNS" (§2.1, Eq. 5). **Stated**
5. The DNS size $\Delta^{\mathrm{inst}}_{\mathrm{DNS}}=(2\nu Re^u_\Delta/(c_1\|\nabla^2\boldsymbol u\|_2))^{1/3}$ is averaged over $T_0$ by an inverse root mean square (Eqs. 6–7); linear averaging gives similar results, and the inverse r.m.s. is chosen for consistency with the anisotropic case (§2.1, §3). **Derived / Stated**
6. The DNS criterion extends to the instantaneous velocity the mean-velocity criterion of Lam et al. (§2.1, Eqs. 8–9). **Stated**
7. Under a Kolmogorov spectrum $E(k)=C_{\mathrm K}\varepsilon^{2/3}k^{-5/3}$ between $k_c=2\pi/\Delta_c$ and $k_\eta=2\pi/\eta$, $R_k=\frac32C_{\mathrm K}((k_cL)^{-2/3}-(k_\eta L)^{-2/3})$ and $R_\varepsilon=1-(k_cL)^{4/3}/(k_\eta L)^{4/3}$, which give $(k_\eta L)^{-2/3}=2R_k\sqrt{1-R_\varepsilon}/[3C_{\mathrm K}(1-\sqrt{1-R_\varepsilon})]$ (§2.2, Eqs. 10–14). **Derived**
8. The subgrid shares on the current mesh use $K_{\mathrm{sgs}}=\nu_t^2/(c_k^2\Delta_I^2)$ with $c_k=0.1$ and $\varepsilon_{\mathrm{sgs}}=c_\varepsilon K_{\mathrm{sgs}}^{3/2}/\Delta_I$ with $c_\varepsilon=0.85$, $\nu_t$ from the σ model, and the resolved parts $\frac12\langle\bar u_i'\bar u_i'\rangle$ and $2\nu\langle\bar S'_{ij}\bar S'_{ij}\rangle$ (§2.2, Eqs. 15–18). **Stated**
9. The filter width achieving a target share is $\Delta_c=(R^T_k/R^I_k)^{3/2}\Delta_I$, assuming an eddy viscosity scaling with the 4/3 power of the filter width (§2.2, Eq. 19). **Derived**
10. Targeting $L/\Delta=10$ with $\eta\to0$ gives $R^T_k\approx0.2$, Pope's 80% resolved-energy criterion in the infinite-Reynolds limit, so the method is "an extension of Pope's criterion to finite Reynolds numbers" (§2.2). **Stated** (no value of $C_{\mathrm K}$ is printed)
11. Where the target $L/\Delta_c$ gives $\Delta_c<\Delta_{\mathrm{DNS}}$, scale separation is not achievable and DNS should be performed there (§2.2–2.3, Fig. 1). **Stated**
12. The LES size is $\Delta=\min\{\Delta_{\langle u\rangle};\max\{\Delta_{\mathrm{DNS}};\Delta_c\}\}$ (Eq. 20), a compromise between the RANS strategy (controlled by $\Delta_{\langle u\rangle}$ only) and the DNS strategy (controlled by $\Delta_{\mathrm{DNS}}$ only) (§2.3). **Stated**
13. Adaptation stops when the total number of cells varies by less than 10%, empirically sufficient, typically after 2 or 3 steps (§3, App. A). **Shown**
14. Round-jet DNS with $Re^u_\Delta$ from 0.05 to 0.5: final meshes from 920,442,715 ($Re^u_\Delta=0.05$) to 75,093,339 elements ($Re^u_\Delta=0.5$); mean and r.m.s. axial velocity at $x/D=1$, 5, 10 agree for all values; at $Re^u_\Delta=0.5$ the $x/D=10$ spectrum shows weak high-frequency ripples, attributed to under-resolved dissipative scales and the implicit filtering of the finite-volume method (§3.1, Figs. 2–4). **Shown**
15. With $Re^u_\Delta=0.125$, $\Delta/\eta\approx1.5$ in the fully turbulent region and the subgrid part of the dissipation is below 5%; $\Delta/\eta$ is roughly constant there, so $Re^u_\Delta$ scales the mesh to the Kolmogorov scale a priori (§3.1, Fig. 5). **Shown**
16. Along $y/D=0.5$, $z/D=0$ the mesh size decreases after $x/D>2$ (secondary instabilities) and increases after $x/D>7$ (fully turbulent state, decreasing dissipation) (§3.1, Fig. 5). **Shown**
17. Jet LES with $Re^u_\Delta=Re^{\langle u\rangle}_\Delta=0.125$ and $L/\Delta_c=5$–25: the transition region and the turbulent/non-turbulent interface are meshed by the DNS criterion whatever $L/\Delta_c$; $L/\Delta_c$ acts after the potential core; element count grows with $L/\Delta_c$ from VLES to quasi-DNS; mean and r.m.s. agree with DNS even at small $L/\Delta_c$, spectra for $L/\Delta_c>20$ (§3.2, Figs. 7–9). **Shown**
18. The filter-width criterion stays isotropic in the anisotropic extension because turbulence is nearly isotropic at those scales; only the Hessian-based criteria become anisotropic (§4.1). **Stated**
19. Only the magnitude of $\mathsf D$ is fixed by a target $u^{<}_T$; its shape is free through any SPD $\mathsf N$, chosen as $(\sum_i|\mathsf H(u_i)|)^{-1}$ to minimize the element count (§4.1, Eq. 23). **Derived**
20. Instantaneous DNS metrics are averaged log-Euclidean, $\mathsf M_{\mathrm{DNS}}=\exp(T_0^{-1}\int_{T_0}\log\mathsf M^{\mathrm{inst}}_{\mathrm{DNS}}\,dt)$, and the LES metric is $\mathsf M_{\mathrm{LES}}=\mathsf M_{\langle u\rangle}\cap(\mathsf M_{\mathrm{DNS}}\cup\mathsf M_c)$ with $\mathsf M_c=\Delta_c^{-2}\mathsf I$ (§4.1–4.2, Eqs. 24, 26). **Derived**
21. Anisotropic jet LES gives statistics very similar to the isotropic LES; anisotropy develops mainly in transition regions, the fully turbulent region stays isotropic, and the element count falls by a factor between 2 and 3 (§5.1, Figs. 8, 10, 11). **Shown**
22. Pipe LES ($Re_D=5300$, $L/\Delta_c=2$–16): the near-wall region behaves as a transition region, meshed by the DNS criterion and insensitive to $L/\Delta_c$, with aspect ratios up to about 25; elements from 5,083,181 ($L/\Delta_c=2$) to 18,645,837 ($L/\Delta_c=16$); mean velocity in very close agreement with Wu & Moin's DNS for all meshes; r.m.s. values decrease away from the wall as the filter grows (§5.2, Figs. 12–13). **Shown**
23. PRECCINSTA cold flow ($Re^u_\Delta=Re^{\langle u\rangle}_\Delta=0.5$, $L/\Delta_c=10$): mean and r.m.s. axial velocity agree with Meier et al.; isotropic and anisotropic results are "essentially identical"; final meshes 143,961,671 (anisotropic) and 276,472,835 elements (isotropic); loop cost 99,332 against 231,961 CPU hours (§6, Figs. 14–15). **Shown**
24. The slight discrepancy near the swirler exit is generally attributed in the literature to experimental uncertainties and slight inflow asymmetries (§6). **Stated**
25. After convergence the estimated $L$ and $\eta$ at a fully turbulent probe are similar for $L/\Delta_c=5$, 10, 15: $L/\Delta_c$ changes the resolved/subgrid partition without altering total energy and dissipation; it is a robust control parameter, not an accurate integral-scale estimate (App. A, Fig. A.20). **Shown**
26. Pipe parametric study ($0.125\le Re^u_\Delta\le2$, $2\le L/\Delta_c\le16$): decreasing $Re^u_\Delta$ monotonically reduces mean and r.m.s. errors, the mean flow being weakly sensitive up to $Re^u_\Delta\approx0.5$; r.m.s. errors improve with $L/\Delta_c$ and plateau with the element count at quasi-DNS (App. B, Figs. B.21–B.22). **Shown**
27. "It has been shown that $Re^u_\Delta=0.125$ is the target value to achieve rigorous DNS if only this criterion is considered" (App. B). **Stated**
28. The r.m.s. "error" against DNS combines mean-field discretization error, subgrid modelling error and the filtered-out fraction, so it is not strictly an error (App. B). **Stated**

*(Compiler check, not in the sources:)* the second moment per unit volume
of a ball of radius $\Delta$ is $\Delta^2/5$ per direction (of a disk
$\Delta^2/4$), as Eq. (4) prints; eliminating $k_cL$ through
$(k_cL)^{-2/3}=(1-R_\varepsilon)^{-1/2}(k_\eta L)^{-2/3}$ from Eqs. (12)–(13)
reproduces Eq. (14); with $\nu_t\propto\Delta^{4/3}$, Eq. (15) gives
$K_{\mathrm{sgs}}\propto\Delta^{2/3}$ and hence Eq. (19).

# Printed slips

- **§4.1 and Eq. (25):** the paper defines $\mathbb D=c_1\mathbb M^{-1}$ (isotropic limit $\mathbb M=\Delta^{-2}\mathbb I$, $\mathbb D=c_1\Delta^2\mathbb I$), then prints $\mathbb M^{inst}_{DNS}=\frac1{c_1}\mathbb D^{-1}$ and $\mathbb M_{\langle u\rangle}=\frac1{c_1}\mathbb D^{-1}_{\langle u\rangle}$. *(Compiler check, not in the sources: the definition gives $\mathbb M=c_1\mathbb D^{-1}$; with $\frac1{c_1}\mathbb D^{-1}$ the isotropic limit is $c_1^{-2}\Delta^{-2}\mathbb I$.)*
- **Eq. (9) against Eq. (8):** Eq. (8) defines $Re^{\langle u\rangle}_\Delta$ with $\nu+\nu_T$ in the denominator, Eq. (9) prints $\Delta_{\langle u\rangle}=(2\nu Re^{\langle u\rangle}_\Delta/(c_1\|\nabla^2\langle\vec u\rangle\|_2))^{1/3}$ with $\nu$ alone, while the anisotropic target of §4.1 uses $\nu+\nu_T$. *(Compiler check, not in the sources: solving Eq. (8) with $\langle u\rangle^<=\frac12c_1\Delta^2\|\nabla^2\langle\vec u\rangle\|_2$ gives $2(\nu+\nu_T)$ in the numerator.)*
- **§2.2:** "Deardoff's model [24]"; ref. [24] is Deardorff J.W.
- **§5:** "the developed anisotropic mes adaptation strategy".
- **Fig. A.16 caption:** "for different values of $L/\Delta$", where the text uses $L/\Delta_c$.
- **References:** refs. [17] and [43] print no venue or year; ref. [38] prints "173, 2018, p. 133–9" without venue; refs. [32] and [33] print no page or article number; the booktitle of ref. [45] is garbled.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\vec u$, $u_i$ | $\boldsymbol u$, $u_i$ | incompressible |
| $\bar{\vec u}$ (Eq. 2) | $\bar{\boldsymbol u}$ | box filter over the control volume; also the resolved LES field |
| $u^<$, $\langle u\rangle^<$ | $u^{<}$ (registry §11), $\langle u\rangle^{<}$ (page-local; both magnitudes) | unresolved part as in the registry, here a scalar estimate |
| $\langle\cdot\rangle$ | $\langle\cdot\rangle$ | time average |
| $\bar u_i'$, $\bar S'_{ij}$ | $\bar u_i'$, $\bar S'_{ij}$ | resolved fluctuations |
| $\langle e\rangle$, $e_{sgs}$ | $K$, $K_{\mathrm{sgs}}$ | **the source keeps $k$ for the wavenumber** |
| $\langle\epsilon\rangle$, $\epsilon_{sgs}$ | $\varepsilon$, $\varepsilon_{\mathrm{sgs}}$ | $\epsilon$ is also the forcing amplitude of Eq. (22) |
| $R_e$, $R_\epsilon$ | $R_k$, $R_\varepsilon$ (registry §11) | scalar ratios, not the Reynolds stress $R_{ij}$ |
| $C$ | $C_{\mathrm K}$ (page-local) | Kolmogorov constant, no value printed |
| $C_m=0.1$, $C_\epsilon=0.85$ | $c_k$, $c_\varepsilon$ | one-equation subgrid constants |
| $\nu_{sgs}$, $\nu_T$ | $\nu_t$ | subgrid (σ model) and RANS or LES eddy viscosity |
| $\Delta$ | $\Delta$ | **radius of the equivalent sphere**, not the cube root of the cell volume |
| $\eta$, $k_\eta=2\pi/\eta$, $k_c=2\pi/\Delta_c$ | $\eta$, $k_\eta$, $k_c$ | $2\pi$ over the length |
| $L=\langle e\rangle^{3/2}/\langle\epsilon\rangle$ | $L$ | $L$ is also the pipe length $7.5D$ in §5.2 |
| $\mathbb H$, $\mathbb D$, $\mathbb N$, $\mathbb M$ | $\mathsf H$, $\mathsf D$, $\mathsf N$, $\mathsf M$ (page-local) | $\mathsf M$ not the Mach number $M$ |
| $\lambda_i$ (metric eigenvalues) | (page-local) | **collision** with the Taylor microscale |
| $Re=(U_{in}-U_{co})R/\nu$, $Re_D=U_bD/\nu$ | $Re$ (jet, on the radius), $Re_D$ | |
| $St_R$, $\theta$ | $St$ (forcing), $\theta$ (inlet momentum thickness) | |

# Reference list

52 printed references, numbered Elsevier style. The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this
slug. Ref. [20] (Mozaffari et al. 2022) is the ingested
[mozaffari-2022](/sources/mozaffari-2022.md). Refs. [17] (Park et al.) and
[43] (Kamenetskiy et al.) print no venue or year and are keyed with the
citing year and a note; ref. [38] has no venue; ref. [45] has a garbled
booktitle; ref. [21] is the authors' AIAA SciTech 2025 paper. No item is
unparseable.

# Pages created or updated

Chunk 15 (2026-10-28). This source is cited on:

- [Turbulent round jets](/benchmarks/turbulent-round-jet.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Mesh adaptation for turbulent-flow simulation](/methods/mesh-adaptation.md)
- [Sigma model](/methods/sigma-model.md)
- [One-equation subgrid kinetic-energy models](/methods/subgrid-kinetic-energy-equation-model.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
