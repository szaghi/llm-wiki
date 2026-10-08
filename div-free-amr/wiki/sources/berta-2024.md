---
type: Source
title: "Berta, Mignone, Bugli & Mattia (2024) — A 4th-order accurate finite volume method for ideal classical and special relativistic MHD based on pointwise reconstructions"
description: "Fourth-order FV-CT for MHD and RMHD in PLUTO: point-value MP5/WENO-Z reconstruction (one Riemann solve per face), the Mignone-Del Zanna UCT composition formula at fourth order, and a discontinuity-detector order-reduction fallback."
resource: "doi:10.1016/j.jcp.2023.112701"
source_kind: paper
authors: [Berta V., Mignone A., Bugli M., Mattia G.]
year: 2024
venue: "J. Comput. Phys. 499:112701 (arXiv:2310.11831)"
local_file: "~/papers/mosaic/div-free-amr/2024-JCP-Berta-101016jjcp2023112701.pdf"
tags: [constrained-transport, upwind-emf, high-order, finite-volume, relativistic-mhd, production-code, mhd]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

This is the PLUTO implementation of a fourth-order finite-volume
constrained-transport scheme for classical and special-relativistic MHD.
It sits on the same McCorquodale–Colella fourth-order FV base as
[Felker & Stone (2018)](/sources/felker-2018.md), with three changes:
* **Point-value reconstruction.** MP5 and WENO-Z are reformulated to
  interpolate interface states from cell-centre *point* values. There is
  one Riemann solve per face.
* **The EMF.** It is built with the composition formula of
  [Mignone & Del Zanna (2021)](/sources/mignone-2021.md) at fourth order:
  UCT-HLLD for MHD, and UCT-GFORCE extended here to RMHD.
* **A fallback.** A discontinuity detector reduces the order locally.

The face averages of $B_h$ are evolved by discrete Stokes, so
$D_h^{\mathrm{f}}B_h = 0$ holds to machine precision
([notation](/notation.md); [UCT](/methods/upwind-constrained-transport.md)).
Grids are uniform Cartesian.

The file read is the arXiv v4 preprint. The published JCP version was
identified on Crossref by title.

# Key claims

1. **Point-value pipeline** (§3).
   * Cell averages are converted to point values by a Laplacian correction
     to fourth order, and face averages likewise by transverse Laplacians.
   * The cell-centre $B$ is interpolated from face-centre point values,
     following Felker & Stone.
   * Primitive or characteristic point values are then reconstructed with
     MP5 or WENO-Z. The point-value optimal weights differ, e.g.
     $(1/16, 5/8, 5/16)$ for WENO-Z.
   * Point fluxes are face-averaged by a Simpson-like rule. Unlike Felker &
     Stone, no Riemann problem on face-averaged states is needed.
   * Time stepping is eSSPRK(5,4).
2. **Order reduction** (§3.4).
   * Near discontinuities the Laplacian point-value recovery can produce
     unphysical states. A flag $\theta_c$ switches off the correction and
     the flux quadrature, and drops reconstruction to WENO3 or linear.
   * There are two detectors: Jameson's compact pressure sensor, and a new
     ratio of odd- to even-derivative contributions that needs one more
     ghost layer.
   * The authors call the fallback essential on the blast (C2) and on the
     cloud–shock problem.
3. **UCT at fourth order** (§4). The edge EMF is the Mignone–Del Zanna
   formula on reconstructed transverse velocities and staggered fields,
   then line-averaged to fourth order. Point-value reconstruction needs 3
   rather than 4 transverse ghost layers for the EMF. Appendix B corrects
   typos in the coefficient formulas of the 2021 paper (e.g. its eq. 51).
4. **Accuracy and efficiency** (§§5.2–5.3).
   * Fourth order on the MHD iso-density vortex, a new RMHD iso-enthalpy
     vortex, and 2D and 3D CP Alfvén waves.
   * Numerical Alfvén-wave decay scales as $N^{-5}$, against $N^{-3}$ at
     second order.
   * The cost model gives $512^3$ second-order accuracy at about $34^3$,
     roughly $1.2\cdot10^4$ times cheaper. The cost per cell is about
     4.3 times (MHD) and 3.7 times (RMHD) that of second order.
5. **Robustness** (§§5.4–5.8). The field loop, a current sheet with
   $A = \beta = 0.1$, Orszag–Tang (MHD and RMHD, with O-points at low
   dissipation), 3D blasts and a 3D cloud–shock all run.
   * The energy correction is required for the Balsara–Spicer case and the
     RMHD blast.
   * Felker & Stone's blast at three times their magnetization is the
     strongest the scheme runs without it.
6. **Scope** (§6). AMR and non-Cartesian grids are left to companion
   papers. A parallel run needs one communication per Runge–Kutta stage.

# Notation map

| Berta et al. (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\hat B_{x_f}$ etc. (face averages) | $B_h \in V_h^2$ | primary field data |
| $\bar E_{z_e}$ (edge average) | $E_h \in V_h^1$ | |
| $\langle Q\rangle_c$, $Q_c$ | cell average, point value | |
| $\Delta$, $\Delta^\perp$ | Laplacian and transverse Laplacian | no registry symbol |
| $a^{L,R}$, $d^{L,R}$ | UCT flux and diffusion coefficients | as in Mignone & Del Zanna (2021) |
| $\theta_c$, $\eta_c$ | order-reduction flag and detector | |

# Pages created or updated

* Updated [Upwind constrained transport](/methods/upwind-constrained-transport.md): a second fourth-order FV realization, with point values.
* Updated [Positivity–divergence coupling](/results/positivity-divergence-coupling.md): the energy correction is still needed at fourth order.
* Updated [Field-loop advection](/benchmarks/field-loop-advection.md): MHD and RMHD loops at second to fourth order.

# Citations

1. `~/papers/mosaic/div-free-amr/2024-JCP-Berta-101016jjcp2023112701.pdf` (doi:10.1016/j.jcp.2023.112701): text extraction, all pages including Appendices A–B and the reference list (85 entries).
