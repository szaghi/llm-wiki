---
type: Method
title: "Hybrid compact-WENO schemes"
description: "Pirozzoli's conservative scheme: a fifth-order compact upwind flux (tridiagonal) in smooth regions, switched to WENO5 or WENO7 near discontinuities detected by density differences; spectral-like resolution with shock capturing, cheaper than WENO."
status: established
aliases: [hybrid compact-WENO, compact upwind WENO, H5, H7]
tags: [compact-scheme, hybrid, turbulence, spectral-resolution]
timestamp: 2026-10-08T00:00:00Z
---

# Hybrid compact-WENO schemes

**Compact flux** ([Pirozzoli (2002)](/sources/pirozzoli-2002.md), §2).
The conservative-flux problem
([conservative finite difference](/methods/conservative-finite-difference.md))
is posed with an implicit (compact) interface reconstruction on a narrow
stencil; with one point on each side in both the implicit and explicit
parts the only fifth-order member of the family needs a tridiagonal,
diagonally dominant solve (Thomas algorithm). The flux is not local in
the data, but the Lax–Wendroff theorem still holds (Carpenter, Gottlieb
and Shu, cited). Its transfer function resolves waves at three points per
wavelength ($\xi \le 2$) and confines dissipation to high wavenumbers,
better than explicit WENO5/WENO7 and the fourth- and sixth-order Padé
schemes ([modified wavenumber](/definitions/modified-wavenumber.md)).
Fourth-order explicit boundary closures keep global fifth order and
stabilize the semi-discrete operator (eigenvalue study); with the
non-TVD RK4 the stable Courant range is narrower than for linear WENO5
and WENO7. The coefficients are given in the paper but are not legible
in the copy read.

**Switch.** The WENO flux is used at $x_{i+1/2}$ and its two neighbours
where the undivided density difference exceeds a threshold $\vartheta$;
inside each smooth segment the compact system is then decoupled from
the other side of the discontinuity. $\vartheta = 0$ is pure WENO7;
larger $\vartheta$ lowers the error but lets Gibbs oscillations appear,
a trade-off to set per problem (0.1 for Burgers, 0.8 for the
shock–entropy and shock–vorticity tests). Indicators for systems use
density only; two Lax–Friedrichs splittings are compared (per-field
"low-dissipation" and global "high-dissipation", the latter 15 % cheaper).

**Results.** The order of the capturing part matters: H7 beats H5,
though H5 already beats WENO5 and WENO7 on Shu–Osher at 200 points;
shock–vorticity (Mach 8) and 3D shock–isotropic-turbulence interaction
where the hybrids give grid-independent statistics and an energy cutoff
at three points per wavelength (good for DNS, not for MILES).

**Context.** [Martín et al. (2006)](/sources/martin-2006.md),
[Hu, Wang & Adams (2010)](/sources/hu-2010.md) and
[Balsara, Garain & Shu (2016)](/sources/balsara-2016.md) cite hybrid
schemes as the alternative they avoid: a discontinuity detector is
needed, which is problem dependent, and Hu et al. add that hybrids of a
linear high-order scheme and a nonlinear one can become unstable when
discontinuities are only a few points apart.

# Citations

1. [Pirozzoli (2002)](/sources/pirozzoli-2002.md), §§1–6.
2. [Martín et al. (2006)](/sources/martin-2006.md), §1.
3. [Hu, Wang & Adams (2010)](/sources/hu-2010.md), §1.
4. [Balsara, Garain & Shu (2016)](/sources/balsara-2016.md), §1.
