---
type: Definition
title: "Carbuncle phenomenon"
description: "The carbuncle is a numerical instability that low-dissipation approximate Riemann solvers such as HLLC and Roe can develop near strong shocks; the sources avoid it with HLL at strong shocks or with van Leer flux-vector splitting, one attributes kinked Mach stems to the reconstruction, and a shock-fitting moving DG method shows none."
status: established
aliases: [carbuncle problem, carbuncle instability, shock instability of low-dissipation Riemann solvers]
tags: [riemann-solver, numerical-flux, benchmark]
timestamp: 2026-10-22T20:00:00Z
---

# Carbuncle phenomenon

The **carbuncle phenomenon** is the numerical instability that some approximate Riemann
solvers develop in the vicinity of strong shock waves. In the sources of this bundle it is
identified by the solvers that exhibit it and by the remedy, not by a mechanism:
[Fu (2023)](/sources/fu-2023.md) (§3.6) states that "the HLLC and Roe solvers may induce
carbuncle problem in proximity to strong shockwaves with low numerical dissipation whereas
the HLL solver is free from carbuncle problem but featuring substantially larger
dissipation", and concludes that "there is no unique Riemann solver capable of handling all
Mach numbers". [Huang et al. (2026)](/sources/huang-2026.md) (§6.7) likewise state that "the
HLLC solver is known to exhibit numerical instabilities in the presence of strong shock
waves".

The defining trade-off is therefore between the resolution that a low-dissipation solver
gives to contacts and shear layers and the robustness that the more dissipative HLL solver
gives at strong shocks ([HLL-family solvers](/methods/hll-riemann-solvers.md),
[numerical dissipation](/definitions/numerical-dissipation.md)).

## Remedies used in the sources

- **Solver switching by smoothness.** The low-dissipation finite-volume TENO recalled by
  [Fu (2023)](/sources/fu-2023.md) (§3.6, Eq. (30)) uses a low-dissipation flux (HLLC, or the
  central flux for turbulence) where both full reconstruction stencils are flagged smooth by
  the TENO cut-off and the HLL flux otherwise, "to avoid the carbuncle problem while the HLLC
  flux [is] imposed for smooth flows to resolve the fine-scale structures"
  ([targeted ENO](/methods/targeted-eno.md)).
- **HLL for the strong-shock test case.** [Huang et al. (2026)](/sources/huang-2026.md)
  (§6.7) run their compact-stencil reconstructions with HLLC by default but switch to HLL for
  the Mach-10 [double Mach reflection](/benchmarks/double-mach-reflection.md) "to mitigate
  the carbuncle phenomenon".

- **HLL–HLLC hybrid switched by a shock sensor.** [Bai & Li (2022)](/sources/bai-2022.md)
  (§2.4, Eqs. (16)–(20)) replace the Lax–Friedrichs flux of an earlier DG cut-cell code by the
  HLLC–HLL solver of Kim et al. "to reduce the numerical dissipation" and "to avoid the shock
  instability which may meet in the vicinity of strong shock". The star states are blended,
  $\hat u^*_K=f\,u^*_K+(1-f)\,u^{\mathrm{HLL}}$, $K=L,R$, so $f=1$ is HLLC and $f=0$ HLL; $f$ is set
  by the pressure-jump indicator $f_p$ of the
  [Rankine–Hugoniot](/definitions/rankine-hugoniot-condition.md) page and the face-normal Mach
  numbers: "when the indicator function is equal to 1", $f=f_p$ if $M_L,M_R$ are both above or
  both below 1 and $f=0$ otherwise (Eq. (19)); $f$ where the indicator is 0 is not stated.
  *(compiler check, not in the sources: the Mach numbers are those of the face-normal
  velocities in the mesh frame (§2.4), so across a stationary shock aligned with the face the
  upstream one exceeds 1 and the downstream one is below 1, the "otherwise" branch applies and
  the face gets HLL, as the stated aim requires; at a detected moving shock both Mach numbers
  can lie on one side of 1, and Eq. (19) as printed then gives $f=f_p=1$, i.e. HLLC.)*
- **Flux-vector splitting.** [Chen et al. (2022)](/sources/chen-2022.md) (§2) compute all
  shocked cases with van Leer flux-vector splitting because it is "robust in shock-capturing
  computations", so that "we are able to exclude the numerical shock instabilities caused by
  numerical fluxes", citing the matrix stability analysis of the carbuncle by Dumbser,
  Moschetta and Gressier; HLLC is reserved for shock-free runs.
- **HLL for relativistic jets.** [Chen & Wu (2022)](/sources/chen-2022-b.md) (Ex. 4.12) report
  "no carbuncle" in their third-order finite-volume WENO run of an axisymmetric relativistic
  jet with the HLL flux on triangles, relativistic Mach number about 41.95
  ([high-Mach jets](/benchmarks/high-mach-astrophysical-jet.md)).
- **Fitting the shock instead of capturing it.** In the moving discontinuous
  Galerkin method MDG+ICE of [Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md)
  the bow shock is a mesh face located by the weakly enforced interface
  ([Rankine–Hugoniot](/definitions/rankine-hugoniot-condition.md)) condition,
  and the interior flux is the plain central average, with no Riemann solver.
  On the steady Mach 8 (315 elements) and Mach 15 (497 elements) flows past a
  half cylinder, computed with linear elements, the authors observe "no shock
  instabilities or carbuncle phenomenon" (§IV.E, Fig. 28). The evidence is the
  figure alone; no shock-capturing comparison is run. See
  [implicit shock tracking](/methods/implicit-shock-tracking.md).

## The reconstruction matters too

With the flux held fixed, [Chen et al. (2022)](/sources/chen-2022.md) (§6.5, Fig. 22) find
"kinked Mach stems" in the Mach-10 [double Mach reflection](/benchmarks/double-mach-reflection.md)
on 576,910 triangles for the cell-based weighted-least-squares gradients with the MLP-pw slope
limiter, "especially significant" with the common-vertex stencil, citing for the kinked stem
Kim et al.'s paper on cures for the shock instability of the Roe scheme. Their vertex-based
gradient with nonlinear weights, on the same common-vertex stencil and with the same van Leer
flux, shows "no numerical abnormality". Since the flux is the same in all runs, the abnormality
is ascribed to the reconstruction and limiter (see
[unstructured gradient reconstruction](/methods/unstructured-gradient-reconstruction.md)). The
paper does not call the kinked stem a carbuncle.

## Qualifications

- None of the sources describes the carbuncle's form or its mechanism; this page records
  only what they state. Fu (2023) cites a dedicated reference for it and, among its references,
  a rotated-hybrid carbuncle-free Riemann solver (Nishikawa & Kitamura), which the review
  mis-cites as the Rusanov solver (§3.6).
- Luo, Absillis & Nourgaliev's Fig. 28 caption gives Mach 8 and 18, the text Mach 8 and 15;
  the page follows the text.

# Citations

- [Fu (2023)](/sources/fu-2023.md) — §3.6 (Eq. (30), Fig. 9).
- [Huang et al. (2026)](/sources/huang-2026.md) — §6.7 (Fig. 12).
- [Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md) — §3.3, §IV.E (Fig. 28; author manuscript).
- [Bai & Li (2022)](/sources/bai-2022.md) — §2.4 (Eqs. (16)–(20)).
- [Chen et al. (2022)](/sources/chen-2022.md) — §2, §6.5 (Fig. 22).
- [Chen & Wu (2022)](/sources/chen-2022-b.md) — Ex. 4.12 (Fig. 18) (arXiv v1).
