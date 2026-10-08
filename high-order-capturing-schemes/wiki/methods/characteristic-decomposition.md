---
type: Method
title: "Local characteristic decomposition"
description: "Applying scalar ENO/WENO/MP reconstruction to the characteristic variables of a Jacobian frozen at each interface or cell; needed for robustness at high order, at the cost of most of the floating-point work."
status: established
aliases: [characteristic-wise reconstruction, field-by-field decomposition]
tags: [systems, eigenvectors, reconstruction]
timestamp: 2026-10-08T00:00:00Z
---

# Local characteristic decomposition

**Why.** Scalar ENO reconstruction is non-oscillatory only if
discontinuities are separated by at least $r+1$ smooth points. In a
system, discontinuities of different families collide (and a Riemann
problem emits them from one point), so component-by-component
reconstruction can oscillate near interactions. For a linear system the
characteristic variables are decoupled scalar advections whose
discontinuities never collide; Harten et al. therefore reconstruct in
locally defined characteristic variables
([Harten et al. (1987)](/sources/harten-1987.md), §5).

**How** ([Shu (1998)](/sources/shu-1998.md), Procedures 2.8–2.10).
At each $x_{i+1/2}$, take an average state (arithmetic mean, or a Roe
average satisfying $f(u_{i+1}) - f(u_i) = f'(\hat u)(u_{i+1} - u_i)$),
compute $R$, $L$, $\Lambda$ there, project the stencil data
$w^{(p)}_j = \ell^{(p)} u_j$ (and $\ell^{(p)} f(u_j)$ for flux
schemes), apply the scalar procedure in each field (the Roe speed
becomes $\lambda^{(p)}$; the LLF speed becomes per field), and project
back with $r^{(p)}$. In multi-D the decomposition is one-dimensional,
normal to the face. [Suresh & Huynh (1997)](/sources/suresh-1997.md)
freeze the eigenvectors at the cell centre over the five-point stencil
instead. [Colella & Woodward (1984)](/sources/colella-1984.md) use the
characteristic structure differently: to trace domain-of-dependence
states for the Riemann problem ([PPM](/methods/ppm.md)).

**Evidence.**
* Lax's shock tube is much noisier with component-wise fourth-order ENO
  than Sod's; characteristic reconstruction removes most of the noise
  ([Harten et al. (1987)](/sources/harten-1987.md), Figs. 11–15;
  [Lax shock tube](/benchmarks/lax-shock-tube.md)).
* Component-wise versions are adequate at second and sometimes third
  order; for demanding problems or high order the characteristic
  version is required ([Shu (1998)](/sources/shu-1998.md), §2.3.5).
  [Jiang & Shu (1996)](/sources/jiang-1996.md) call Sod's and especially
  Lax's problem tough tests for non-characteristic schemes of order three
  or more.

**Cost and shortcuts.**
* The projections account for most of the floating-point work of ENO and
  WENO ([Jiang & Shu (1996)](/sources/jiang-1996.md), §4;
  [Shu & Osher (1989)](/sources/shu-1989.md), §IV). Since the only
  nonlinearity of WENO is in the weights, Jiang and Shu compute the
  weights from pressure (genuinely nonlinear fields) and entropy
  (linearly degenerate fields) and keep the rest linear, needing only
  two projections: about twice as fast, adequate without strong shocks,
  but failing at reflecting walls — the mirrored ghost values have the
  same pressure and entropy, so the jump in normal velocity is invisible
  to the weights (double Mach reflection, forward step, 2D
  shock–entropy-wave interaction).
* Restricting the decomposition to transition regions is suggested but
  not pursued ([Shu & Osher (1989)](/sources/shu-1989.md);
  [Suresh & Huynh (1997)](/sources/suresh-1997.md), since MP5 leaves
  smooth monotone data unchanged and then equals the conservative-
  variable formula).
* Central schemes avoid it entirely; for systems,
  [Levy, Puppo & Russo (1999)](/sources/levy-1999.md) find one *global*
  smoothness indicator shared by all components (each component's
  indicator scaled by its $L^2$ norm) better and cheaper than
  component-wise indicators, and a density-only indicator slightly
  better still on Euler ([central WENO](/methods/central-weno.md)).
* [Balsara & Shu (2000)](/sources/balsara-2000.md) build the flux
  components per characteristic field and choose the building block per
  field (LLF for linearly degenerate, RF for genuinely nonlinear).

**Later uses (batch 2).** Roe-averaged characteristic decomposition with
Lax–Friedrichs (global or per-field) splitting is the default of the
batch-2 schemes ([Borges et al. (2008)](/sources/borges-2008.md);
[Hu, Wang & Adams (2010)](/sources/hu-2010.md); [Fu, Hu & Adams (2016)](/sources/fu-2016.md);
[Zhu & Qiu (2016)](/sources/zhu-2016.md); [Balsara, Garain & Shu (2016)](/sources/balsara-2016.md)).
[Pirozzoli (2002)](/sources/pirozzoli-2002.md) computes the hybrid switch
and the WENO indicators from density only, and compares per-field and
global Lax–Friedrichs splittings (the global one 15 % cheaper, more
dissipative).

**Later uses (batch 3).** FV-WENO in 3D always reconstructs in local
characteristic variables, found necessary in some cases despite the
cost ([Titarev & Toro (2004)](/sources/titarev-2004.md), §3.4). In
compact-reconstruction WENO the projection, with Roe-average
eigenvectors that differ per interface, turns the scalar tridiagonal
solve into a $3\times3$ block-tridiagonal one. Conservative-variable
reconstruction is cheaper and adequate for smooth flows
([Guo, Xiong & Shi (2014)](/sources/guo-2014.md), §§2.3, 3). FD WENO with
positivity limiting uses Roe-matrix eigenvectors at each interface
([Zhang & Shu (2012)](/sources/zhang-2012.md), §3.1). A global rather
than local Lax–Friedrichs speed in the splitting further reduces
spurious oscillations for MHD ([Christlieb et al. (2016)](/sources/christlieb-2016.md), §6.2).
AFD-WENO projects each cell's neighbours onto that cell's eigenvectors
for the interpolation. For the interface derivatives, componentwise
interpolation works as well as projection
([Balsara et al. (2025)](/sources/balsara-2025.md), §V). For relativistic
MHD only primitive variables, projected on primitive-variable
eigenvectors, discriminate speeds close to that of light
([Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §8). GP-WENO
also reconstructs in characteristic variables
([Reyes et al. (2018)](/sources/reyes-2018.md), §5).

# Citations

1. [Harten et al. (1987)](/sources/harten-1987.md), §§5–7.
2. [Shu & Osher (1989)](/sources/shu-1989.md), §IV.
3. [Shu (1998)](/sources/shu-1998.md), §§2.3.5, 3.3.4.
4. [Jiang & Shu (1996)](/sources/jiang-1996.md), §§4, 8.
5. [Suresh & Huynh (1997)](/sources/suresh-1997.md), §3.
6. [Levy, Puppo & Russo (1999)](/sources/levy-1999.md), §5.2.
7. [Balsara & Shu (2000)](/sources/balsara-2000.md), §II.
8. [Colella & Woodward (1984)](/sources/colella-1984.md), §3.
9. [Pirozzoli (2002)](/sources/pirozzoli-2002.md), §4.
10. [Borges et al. (2008)](/sources/borges-2008.md), §5.2.
11. [Fu, Hu & Adams (2016)](/sources/fu-2016.md), §5.
12. [Titarev & Toro (2004)](/sources/titarev-2004.md), §3.4.
13. [Guo, Xiong & Shi (2014)](/sources/guo-2014.md), §§2.3, 3.
14. [Zhang & Shu (2012)](/sources/zhang-2012.md), §3.1.
15. [Christlieb et al. (2016)](/sources/christlieb-2016.md), §6.2.
16. [Balsara, Bhoriya, Shu & Kumar (2025)](/sources/balsara-2025.md), §V.
17. [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §8.
18. [Reyes et al. (2018)](/sources/reyes-2018.md), §5.
