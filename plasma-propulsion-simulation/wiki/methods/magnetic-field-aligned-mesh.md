---
type: Method
title: "Magnetic-field-aligned meshes"
description: "Meshes built from magnetic field lines and their orthogonal family, on which the parallel and perpendicular derivatives of the electron fluid equations are computed directly, removing the numerical diffusion that the strong mobility anisotropy produces on cylindrical meshes; used by HALL2De and HYPHEN, with known boundary and 3D limitations."
status: established
aliases: [MFAM, field-aligned mesh, magnetically aligned mesh, magnetic-field-aligned mesh]
tags: [numerics, fluid, hybrid, hall-thruster, anomalous-transport]
timestamp: 2026-10-14T00:00:00Z
---

# Magnetic-field-aligned meshes

## The problem it solves

In the [electron fluid model](/methods/electron-fluid-model.md) the mobility
along $\mathbf B$ exceeds the mobility across it by a factor of order
$\Omega_e^2$ (with anomalous transport, $\Omega_e$ times its effective,
anomalous-corrected value), "say $O(10^5)$ in conventional HETs"
([Ahedo (2023)](/sources/ahedo-2023.md), eqs. 33–35). On a cylindrical
$(z,r)$ mesh the parallel and perpendicular gradients of the
[thermalized potential](/definitions/thermalized-potential.md) are assembled
from $z$ and $r$ derivatives, and small errors in those make the parallel
gradient spuriously large against the perpendicular gradient divided by the
square of the effective Hall parameter. Ahedo calls this error
**numerical diffusion** (eq. 36). In $r$–$z$ components the current-continuity
equation becomes a strongly anisotropic five-point elliptic problem whose flux
is a sum of large terms of opposite sign, so numerical error can dominate the
cross-field transport ([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md),
§2.2, eqs. 20a,b, after Hagelaar 2016).

## Construction

* One mesh family follows the magnetic lines; the other is the orthogonal
  family ([Ahedo (2023)](/sources/ahedo-2023.md), §3, Fig. 1a).
* In an axisymmetric field the lines are the level sets of a magnetic stream
  function whose axial derivative is $rB_r$ and whose radial derivative is
  $-rB_z$; the second coordinate is orthogonal to it
  ([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), eqs. 21–22,
  after Mikellides & Katz 2012).
* A topology with a zero-field point can be handled with four monotonic
  regions ([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §2.2,
  after Garrigues et al. 2003). The HYPHEN mesh of a magnetically shielded
  Hall thruster has such a singular null-field point inside the channel
  ([Ahedo (2023)](/sources/ahedo-2023.md), Fig. 1a).
* The parallel and perpendicular derivatives are then computed directly, and
  the elliptic problem loses the cross-diffusion error; the mesh "removes the
  problem" ([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §2.2,
  after Mikellides & Katz 2012; [Ahedo (2023)](/sources/ahedo-2023.md),
  eq. 36).

## Codes

* HALL2De (JPL) and [HYPHEN](/software/hyphen.md) (UC3M) use field-aligned
  meshes ([Ahedo (2023)](/sources/ahedo-2023.md), §3, refs. 30, 36, 38).
* 2D field-aligned calculations confirm that the potential is thermalized
  except in the near plume close to the cathode
  ([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §2.2, after
  Mikellides & Katz 2012).

## Limitations (stated)

* Cells are very irregular, and the mesh boundaries are in general not
  magnetically aligned ([Ahedo (2023)](/sources/ahedo-2023.md), §3,
  ref. 39).
* Weighted-least-squares derivative algorithms on such meshes "lead to
  numerical diffusion and large errors" in the parallel current at the
  channel boundaries ([Ahedo (2023)](/sources/ahedo-2023.md), §3, refs. 40,
  41).
* The construction is impractical in 3D and inapplicable when the magnetic
  field is induced and time dependent. The 3D plume code
  [EP2PLUS](/methods/hybrid-pic-fluid-model.md) therefore uses a Cartesian mesh and is
  reliable only for effective Hall parameters up to 50–100
  ([Ahedo (2023)](/sources/ahedo-2023.md), §3, eqs. 68–72, ref. 87).
* No discretization formulas, mesh sizes or time steps are given in either
  source.

# Citations

1. [Ahedo (2023)](/sources/ahedo-2023.md), §3, eqs. 33–36, 68–72, Fig. 1a.
2. [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §2.2, eqs. 20–22.
