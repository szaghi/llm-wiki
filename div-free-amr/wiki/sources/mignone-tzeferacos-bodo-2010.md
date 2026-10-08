---
type: Source
title: "Mignone, Tzeferacos & Bodo (2010) — High-order conservative finite difference GLM-MHD schemes for cell-centered MHD"
description: "Third- and fifth-order point-value finite-difference MHD with GLM cleaning (WENO+3, LimO3, WENO-Z, MP5) in PLUTO; upwinds the (B_n, psi) subsystem separately and finds the optimal damping order-dependent."
resource: "doi:10.1016/j.jcp.2010.04.013"
source_kind: paper
authors: [Mignone A., Tzeferacos P., Bodo G.]
year: 2010
venue: "J. Comput. Phys. 229(17):5896-5920 (arXiv:1001.2832)"
local_file: "~/papers/mosaic/div-free-amr/2010-JCP-Mignone-101016jjcp201004013.pdf"
tags: [glm, high-order, finite-difference, weno, collocation, production-code, mhd]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

Takes [GLM divergence cleaning](/methods/glm-divergence-cleaning.md) to
third and fifth order. The scheme is a conservative finite-difference
method on point values, in the Shu–Osher flux-primitive form, on uniform
Cartesian grids. All variables, $B$ included, are collocated at zone
centers. Four 1D interface reconstructions are compared inside PLUTO, with
global Lax–Friedrichs splitting on local characteristic fields and
third-order SSP-RK:
* WENO+3 (Yamaleev–Carpenter weights);
* LimO3 (Čada–Torrilhon);
* WENO-Z;
* MP5.

The argument for the route: the scheme avoids the elliptic step, avoids
staggered fields, and avoids the multidimensional reconstruction that
held-class schemes need above second order
([divergence-free reconstruction](/methods/divergence-free-reconstruction.md)).
The authors cite the second-order comparison of
[Mignone & Tzeferacos (2010)](/sources/mignone-tzeferacos-2010.md) as
evidence that GLM matches CT in accuracy.

The file read is the arXiv v2 preprint. Volume, issue and pages were
verified on Crossref.

# Key claims

1. **Split treatment of the cleaning subsystem** (§3.1, eqs. 21–24). $B_n$
   and $\psi$ obey a constant-coefficient $2\times2$ system with speeds
   $\pm c_h$, decoupled from the other seven waves. Its characteristic
   variables $\tfrac12(\psi \mp c_h B_n)$ need no local projection and are
   reconstructed grid-wide with the same operator $R$. The interface $B_n$
   and $\psi$ follow, and $B_n$ then enters the 7-wave solve as a constant.
   That makes 16 reconstructions per direction: 2 for the cleaning pair and
   14 for the remaining families.
2. **Cleaning speed and damping** (eqs. 8–9). $c_h$ is the grid-maximal
   fast speed. The source step is integrated analytically,
   $\psi \leftarrow \psi\,\exp(-\alpha_p c_h \Delta t/\Delta h)$ with
   $\alpha_p = \Delta h\, c_h/c_p^2$, and the authors recommend
   $\alpha_p \in [0,1]$. In 1D the GLM correction is switched off.
3. **Divergence monitor** (eq. 43). $\nabla\cdot B$ is the flux-form
   difference of the interface $B_n$ produced by eq. 24, which is a
   scheme-dependent quantity.
4. **Measured divergence** (§§4.2–4.4, Table 2, Figs. A.7, A.11–A.12).
   * Rotated shock tubes: errors $\lesssim 10^{-2}$, bounded with
     resolution, saturating for $\alpha_p \gtrsim 0.4$ in 2D and 3D.
   * Field loop: fifth-order schemes are best for $\alpha_p \gtrsim 0.4$,
     third-order for $\alpha_p \lesssim 0.2$.
   * Vortex: the error falls with resolution, below $10^{-8}$ at $128^3$
     for the fifth-order schemes.
   * Orszag–Tang: the error peaks at discontinuities.
   * Neither AMR nor a long-time fixed-$h$ divergence history is reported.
5. **Accuracy and cost** (§§4.1, 4.3, 5).
   * Design order is met on smooth problems: 3 or 5 on the 1D and 3D
     Alfvén waves and on the 2D and 3D vortex.
   * After about 100 Alfvén periods at $\tan\alpha = 6$, fifth-order
     schemes keep about 94% of the amplitude. Third-order schemes keep
     about 20% and second-order TVD with MC about 3%.
   * At discontinuities the gain from third to fifth order is only a
     factor 1.5–2.
   * Fifth-order schemes cost 1.25–1.5 times as much as third-order ones,
     which the authors present as a net gain at equal accuracy.
6. **New benchmark**: a 3D extension of the Balsara magnetized vortex
   (§4.3.2).
7. **Record inconsistencies.**
   * Ref. [39], the CTU-GLM paper, is given as "ApJS 229 (2010)". It is
     J. Comput. Phys. 229.
   * Colella–Sekora is listed as volume "277"; the volume is 227.
   * The text notes a misprint in [39]'s final time for the 3D shock tube.

# Notation map

| Mignone, Tzeferacos & Bodo (2010) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\psi$ | $\psi_h$ | GLM multiplier, collocated |
| $c_h$, $c_p$ | $c_h$, $c_p$ | same |
| $\alpha_p = \Delta h\,c_h/c_p^2$ | (no registry symbol) | damping parameter |
| $B_{x,i+1/2}$ (eq. 24) | interface value of collocated $B_h$ | reconstructed, not a stored face field |
| eq. (43) $\nabla\cdot B$ | not a registry operator | differences reconstructed interface values; closest is a face-difference applied to non-stored data |
| $R(\cdot)$ | reconstruction operator | **not** the restriction $R$ of the registry |
| $\mathcal{L}(U)$ | semi-discrete residual | |

# Pages created or updated

* Updated [GLM divergence cleaning](/methods/glm-divergence-cleaning.md): a high-order finite-difference section, and the origin of the $(B_n,\psi_h)$ upwinding behind the Zaghi (2026) observation.
* Updated [Divergence-free reconstruction](/methods/divergence-free-reconstruction.md): the controlled-class alternative.
* Updated [Rotated shock tube](/benchmarks/rotated-shock-tube.md): the 45° 2D and 3D high-order cleaning results.
* Updated [Field-loop advection](/benchmarks/field-loop-advection.md): the 2D and 3D high-order cleaning runs.

# Citations

1. `~/papers/mosaic/div-free-amr/2010-JCP-Mignone-101016jjcp201004013.pdf` (doi:10.1016/j.jcp.2010.04.013): text extraction, all pages, including the reference list (54 entries).
