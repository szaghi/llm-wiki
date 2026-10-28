---
type: Source
title: "Huang et al. (2022c) — Applications of wall-models to implicit large eddy simulations in the spectral/hp element method"
description: "Couples an algebraic log-law wall-stress model, imposed as a Neumann condition with a freely chosen matching height, to spectral-vanishing-viscosity implicit LES in Nektar++; turbulent channel flow up to Re_tau=2000 on one coarse high-order mesh gives mean velocity within 5.4% of DNS, with errors in the fluctuations near the matching interface."
resource: "doi:10.1063/5.0117432"
source_kind: paper
authors: [Huang B., Wang R., Wu F., Xu H.]
year: 2022
venue: "Phys. Fluids 34:105129"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Physics_of_Fluids_Huang_Applications_of_wall-models_to_implicit_large_eddy_simulatio.pdf"
tags: [wmles, implicit-les, spectral-vanishing-viscosity, spectral-element, channel-flow]
timestamp: 2026-10-27T21:11:00Z
---

# Summary

Huang et al. (2022c) build a [wall-modelled LES](/methods/wall-modelled-les.md)
on top of spectral-vanishing-viscosity
[implicit LES](/definitions/implicit-les.md) (SVV-iLES) of the incompressible
equations in [Nektar++](/software/nektar-plus-plus.md), a continuous
[spectral/hp element](/methods/spectral-element-method.md) code with a
velocity-correction splitting scheme. The
[spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
(Tadmor, Maday et al., Kirby & Sherwin, the "DG kernel" of Moura et al.) is
the only regularization, a form of
[numerical dissipation](/properties/numerical-dissipation.md); resolving the
inner layer limits SVV-iLES to moderate Reynolds numbers
([grid-point requirements](/results/les-grid-point-requirements.md)). The
[equilibrium wall model](/methods/equilibrium-wall-model.md) samples the
resolved velocity at a freely chosen height $h_{\mathrm{wm}}$ in the log
layer by evaluating the element expansion, solves the
[log law](/definitions/law-of-the-wall.md) ($\kappa=0.41$, $B=5.2$) for
$u_\tau$ by Newton–Raphson and imposes $\tau_w$ as a Neumann condition on the
wall-parallel velocity. The Neumann type is chosen so that no wall-model eddy
viscosity enters the equations; the authors argue that eddy-viscosity fixes
of the SGS side ([log-layer mismatch](/definitions/log-layer-mismatch.md)
corrections) and the Nek5000 framework of Pal et al. ([Nek5000](/software/nek5000.md))
do not carry over to SVV-iLES, and call this the first wall model for
SVV-iLES in a spectral/hp element method.

[Channel flow](/benchmarks/turbulent-channel-flow.md) at $Re_\tau=550$, 950
and 2000 on one $12\times6\times10$ hexahedral mesh with printed "polynomial
order $N_p=7$" and $h_{\mathrm{wm}}=0.224\delta$ gives mean velocity
indistinguishable from DNS at 550 and at most 2% and 5.4% high at 950 and
2000; fluctuations and shear stress show a "parabolic" error near the
interface, attributed to the Neumann condition. Reichardt's law instead of the
log law and a time-averaged matching velocity change little; at similar
resolution a mesh with fewer, higher-order elements beats more, lower-order
ones; the run is up to seven times cheaper than wall-resolved SVV-iLES.
[Non-equilibrium](/methods/nonequilibrium-wall-model.md),
[slip-wall](/methods/slip-wall-model.md) and
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) approaches are reviewed but
not tested.

# Version read

Version of record (Phys. Fluids 34:105129, AIP; submitted 1 August 2022,
accepted 19 September 2022, online 25 October 2022), 15 PDF pages (an AIP
cover and article pages 105129-1 to -14), all read; equation, table and
figure pages also read visually. Page-1 title, four authors and DOI match the
metadata. No identity problem. Numbering on this page is that of this
version.

# Key claims

$h_{\mathrm{wm}}$ is the matching height (the source's $h$, $y_j$), $\tau_w$
the wall shear stress (also printed $\tau_u$), $\nu_{t,\mathrm{wm}}$ the
mixing-length wall-model eddy viscosity (page-local).

1. SVV-iLES (spectral/hp elements with SVV, no explicit SGS model) is limited to moderate Reynolds numbers by the cost of resolving the inner layer, so a wall-modelled SVV-iLES is needed (abstract, §I). **Stated**
2. This work is "the first to construct the wall model of SVV-iLES based on the spectral/hp element method" (abstract, §I, §IV). **Stated**
3. The Nek5000 wall-modelling framework of Pal et al. (log law, Neumann condition) "is only suitable for conventional iLES, which could not be coupled with iLES based on the spectral vanishing viscosity method" (§I). **Stated**
4. Eddy-viscosity wall-model corrections (Cabot & Moin's dynamic eddy viscosity; Wu & Meyers' modified Smagorinsky coefficient) are "not applicable to the iLES" because no model coefficient can be modified (§I). **Stated**
5. A Neumann condition avoids applying a mixing-length eddy viscosity at the matching interface, and with the velocity-correction scheme the Helmholtz problem keeps a constant viscosity (§I). **Stated**
6. $h_{\mathrm{wm}}$ can be chosen freely inside an element by evaluating the high-order expansion (Eqs. 15–16), as long as it lies in the log layer; the paper uses the top of the first wall-adjacent element, $0.224\delta$ (§II C, §III A). **Stated**
7. Mean velocity: "almost not distinguishable" from DNS at $Re_\tau=550$, at most 2% high at 950 and 5.4% high at 2000 (§III B, Figs. 4a–6a). **Shown**
8. R.m.s. fluctuations and Reynolds shear stress agree with DNS in most of the resolved region but show "a parabolic curve appearing around the interface", attributed to the high wall-normal gradient imposed by the Neumann condition, which the authors say increases the eddy viscosity and the near-wall dissipation, and call common to wall-modelled approaches (§III B, Figs. 4–6 b,c). **Shown** (attribution **Stated**)
9. A Dirichlet condition with eddy-viscosity augmentation "may perform better prediction in the near-wall region" (citing Bae & Lozano-Durán); not tested (§III B). **Stated**
10. Instantaneous spanwise-velocity fields show finer resolved scales as $Re_\tau$ grows on the same mesh, taken as evidence that the wall model "does not jeopardize the capability of a high order polynomial" (§III B, Fig. 3). **Shown** (qualitative)
11. With matching in the log region, Reichardt's law (Eq. 17) and the log law give only slightly different statistics at $Re_\tau=550$, "due to the fact that the interface … is located in the logarithmic region where both of the two laws coincide" (§III C, Fig. 7). **Shown** (reason **Stated**; see Printed slips)
12. A time-averaged matching velocity (exponential moving average, weight 0.01) gives only marginally different results from the instantaneous one, which can therefore be used directly, in agreement with Frère et al. (§III D, Fig. 8). **Shown**
13. At similar resolution ($\Delta x^+\times\Delta y_1^+\times\Delta z^+\approx48$–$49\times20\times29$ at $Re_\tau=550$), mesh 1 ($12\times6\times10$, $N_p=7$) gives better fluctuations and shear stress than mesh 2 ($14\times8\times12$, $N_p=6$), both giving the DNS mean velocity; the conclusion calls this "the p-type refinement shows better agreement" (§III E, Figs. 3, 9, §IV). **Shown**
14. At $Re_\tau=550$ the wall-modelled run improves the computational efficiency "as high as seven times" over wall-resolved SVV-iLES with the same mesh and order in the resolved region (§III A). **Shown** (number only; no timing data)
15. The channel is driven by a constant body force from $f_x\delta/U^2=(Re_\tau/Re_\delta)^2$ (Eq. 18) with $Re_\delta/Re_\tau=2.5\ln Re_\tau+5$ (Eq. 19), giving $f_x=2.42\times10^{-3}$, $2.13\times10^{-3}$, $1.7\times10^{-3}$ (Table I) (§III A). **Stated** (see Printed slips)
16. Each run covers at least 250 flow-through times of transient and more than 45 of averaging (§III A). **Stated**
17. The spacings $\Delta x\simeq0.087\delta$, $\Delta y_1\simeq0.037\delta$, $\Delta z\simeq0.052\delta$ follow the WMLES review of Larsson et al. (2016) (§III A). **Stated**
18. The algebraic equilibrium model is "considerably cheaper" but cannot represent the wall-attached vortices of the inner layer; it suffices for channel flow, while non-equilibrium models need a separate near-wall grid (§I, §II C). **Stated**
19. Limitations: incompressible flow only; adverse pressure gradient, separation and compressible thermal effects, and better near-interface Reynolds stresses, are left open (§IV). **Stated**
20. "Compared with RANS models, LES greatly improves computational accuracy and efficiency" (§I). **Stated**

# Printed slips

- **Eqs. (20) and (22):** printed $\left.\partial u/\partial y\right|_w=\tau_w/(\rho v)$ and "$v_t|_w=0$", with the italic $v$ of the wall-normal velocity ($v|_w=0$ in the same line) in place of a viscosity; elsewhere $\nu$ is printed (Eq. 14, $Re_\delta=U_c\delta/\nu$).
- **Reichardt against log law (§III C):** *(compiler check, not in the sources)* for large $y^+$, Eq. (17) with the printed $D=9.8$, $\kappa=0.41$ tends to $\kappa^{-1}\ln y^++D+\kappa^{-1}\ln\kappa$, an intercept of about 7.63 against $B=5.2$ in Eq. (14); at $y^+\approx123$ (the matching height at $Re_\tau=550$) Eq. (17) gives $u^+\approx19.4$ and Eq. (14) $u^+\approx16.9$, so with the printed constants the two laws do not coincide in the log region, against the explanation of §III C.
- **Eq. (19) against Table I:** *(compiler check, not in the sources)* Eq. (19) gives $Re_\delta=11\,426$, 21 034, 48 005 at $Re_\tau=550$, 950, 2000, while Table I prints 11 180, 20 580, 48 500; the tabulated $f_x$ follow from Eq. (18) with the tabulated $Re_\delta$.
- **"Polynomial order $N_p=7$":** *(compiler check, not in the sources)* the printed spacings equal the element sizes divided by $N_p-1$ ($2\pi\delta/12/6=0.087\delta$, $\pi\delta/10/6=0.052\delta$, $0.224\delta/6=0.037\delta$; mesh 2: $2\pi\delta/14/5$ gives $\Delta x^+=49$ at $Re_\tau=550$), i.e. a polynomial degree $N=N_p-1$.
- **SVV parameters:** the kernel, $\nu_{svv}$ and cut-off used in the runs are not stated (only the Fourier-setting kernel of Eq. 11 and the DG kernel of Moura et al. are described).
- **Mesh comparison:** called "h-type refinement" (§I, §III E) and "p-type refinement" (§IV, abstract) for the same comparison.
- **Reference list:** Ref. 2 prints "G. E. Karniadakis, G. Karniadakis, and S. Sherwin"; Ref. 66 prints "AIAA Paper No. 2002-1206, 2022".

# Notation map

| Huang et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\boldsymbol u=(u,v,w)$ | $\boldsymbol u$ | resolved iLES velocity, no filter symbol; $y$ wall-normal, agree |
| $N_p$ ("polynomial order"), $P$ (Eq. 16) | $N$ | spacings consistent with $N=N_p-1$ (see Printed slips); $P+1$ GLL points per direction in Eq. (16) |
| $N$ (§II B) | (number of Fourier modes) | **collision** with the polynomial degree $N$ |
| $N_x\times N_y\times N_z$ | (element counts) | not grid points |
| $\epsilon$, $\nu_{svv}$, $Q_\epsilon$, $\mathcal Q_N$, $Q^d$, $P_{\rm cut}$ | (SVV strength, effective SVV viscosity, kernels, activation mode) | page-local; see [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md) |
| $h$, $y_j$ | $h_{\mathrm{wm}}$ | matching height; **collision** with the cell size $h$ |
| $\tau_w$, $\tau_u=\rho u_\tau^2$ | $\tau_w$ | |
| $\kappa$, $B$, $A^+$ | $\kappa$, $B$, $A^+$ | 0.41, 5.2; $A^+$ value not printed |
| $D$, $E$, $F$ | (Reichardt constants 9.8, 1/11, 1/3) | page-local |
| $\nu_{t,\rm wm}$ | $\nu_{t,\mathrm{wm}}$ | page-local mixing-length wall-model eddy viscosity |
| $\langle u_\|\rangle$ | (wall-parallel velocity at $h_{\mathrm{wm}}$) | instantaneous by default despite the brackets |
| $\bar u^n$ | (exponential moving time average) | **collision** with the filter overbar |
| $Re_\delta=U_c\delta/\nu$ | (Reynolds number on centreline velocity and half-height) | page-local |
| $Re_\tau$, $\delta$, $u_\tau$, $y^+$, $\Delta x^+$ | $Re_\tau$, $\delta$, $u_\tau$, $y^+$, $\Delta x^+$ | agree; $\Delta y_1^+$ the first-element spacing |
| $f_x$ | $f_1$ | constant streamwise body force per unit mass |
| $l_p$ | (slip length of the Robin condition) | page-local |

# Reference list

69 printed references, numbered (AIP superscript style). The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this slug.
Ref. 5 is the ingested [wang-2013](/sources/wang-2013.md); Ref. 14 (Wang, Wu,
Xu & Sherwin 2021, Phys. Fluids 33:035130) is the bibliography's
`wang-2021-d`; Ref. 24 (Heinz, Mokhtarpoor & Stoellinger 2020, Phys. Fluids
32:065102) is a work distinct from the ingested Heinz (2020) review and is
matched by volume and page. Ref. 2 prints a duplicated author and Ref. 66 a
paper number inconsistent with its year (see Printed slips). No printed
duplicate reference, no unparseable item.

# Pages created or updated

Chunk 11 (2026-10-27). This source is cited on:

- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Log-layer mismatch](/definitions/log-layer-mismatch.md)
- [Equilibrium wall model](/methods/equilibrium-wall-model.md)
- [Non-equilibrium wall models](/methods/nonequilibrium-wall-model.md)
- [Slip-wall models](/methods/slip-wall-model.md)
- [Continuous-Galerkin spectral-element method](/methods/spectral-element-method.md)
- [Spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
- [Nek5000 and NekRS](/software/nek5000.md)
- [Nektar++](/software/nektar-plus-plus.md)
