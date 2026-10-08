---
type: Benchmark
title: "Cylindrical and spherical explosion problem"
description: "A Sod-type state jump on a circle or sphere in [-1, 1]^d (inside ρ = p = 1, outside ρ = 0.125, p = 0.1, γ = 1.4), compared with a 1D radial reference solution with geometric sources: tests symmetry preservation for shocks, contacts and rarefactions not aligned with the grid."
status: established
aliases: [explosion problem, cylindrical explosion, spherical explosion, multidimensional Sod problem]
tags: [benchmark, euler, 2d, 3d, riemann-problem]
timestamp: 2026-10-08T00:00:00Z
---

# Cylindrical and spherical explosion problem

**Setup** (Toro's test, as used in [Dumbser et al. (2013)](/sources/dumbser-2013.md), §4;
[Dumbser et al. (2014)](/sources/dumbser-2014.md), §5.8;
[Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.1.6). The domain is
$\Omega = [-1, 1]^d$ with $\gamma = 1.4$. The state is constant inside
and outside a circle ($d = 2$) or sphere ($d = 3$):
$(\rho, \mathbf v, p) = (1, \mathbf 0, 1)$ inside and
$(0.125, \mathbf 0, 0.1)$ outside. The papers use radius 0.4 to
$t = 0.25$ (2013) and radius 0.5 to $t = 0.2$ (2014, 2015). The radial
symmetry gives a 1D reference solution: the Euler equations in the
radial coordinate with geometric source terms, solved on a very fine
1D mesh (10,000 points with a TVD scheme in 2013). Shock, contact and
rarefaction head are not aligned with the grid, which tests whether a
scheme keeps the symmetry.

## Results in this corpus

* **ADER-WENO on AMR** ([Dumbser et al. (2013)](/sources/dumbser-2013.md), §4).
  * 2D, fourth order, $34^2$ base grid, $r_{\mathrm{AMR}} = 3$, two levels
    (equivalent $306^2$). It matches the uniform fine grid and the 1D
    reference, takes 4 instead of 14 minutes, and ends with 28,036 cells.
  * 3D, third order, Osher-type flux, $34^3$ base grid (equivalent
    $306^3$, about $2.9\times10^7$ cells). It ends with about
    $9.1\times10^6$ cells and runs 7.5 hours on 8 cores.
* **ADER-DG $K = 9$ with subcell limiting**, 3D
  ([Dumbser et al. (2014)](/sources/dumbser-2014.md), §5.8).
  * On $25^3$ cells, about 12 cells across $0 \le x \le 1$, the shock
    and the contact are each resolved within one cell.
  * On $100^3$ cells, $10^{10}$ space–time degrees of freedom per step
    on 8000 cores, it agrees with the reference. The limiter acts only
    in cells crossed by the outgoing waves.
* **ADER-DG with subcell limiting and AMR**
  ([Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.1.6).
  * 2D, $K = 9$, $50^2$ base grid, $r_{\mathrm{AMR}} = 3$, two levels.
    It coincides with the reference and with the uniform fine grid.
  * 3D, on a $13^3$ base grid, $K = 3$ in the text but $K = 5$ in the
    caption of Fig. 11. The limiter is active only at the shock, the
    contact and the rarefaction head.

# Citations

1. [Dumbser et al. (2013)](/sources/dumbser-2013.md), §4 (Table 3).
2. [Dumbser et al. (2014)](/sources/dumbser-2014.md), §5.8.
3. [Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.1.6.
