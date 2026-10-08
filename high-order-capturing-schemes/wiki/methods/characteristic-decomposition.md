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

**Later uses (batch 4).**
* *Troubled-cell detection* in RKDG uses a characteristic TVB detector.
  The componentwise one is cheaper but flags far too many good cells,
  and the WENO limiter's reconstruction is always characteristic ([Qiu & Shu (2005)](/sources/qiu-2005.md), §2).
* *Modal FV reconstruction.* 1D moments are reconstructed in
  characteristic variables, cross moments in conserved variables to save
  cost. For the most stringent problems the 1D moments are built both
  ways and the smaller is kept, after Dumbser and Käser, which
  stabilizes without hurting order ([Balsara et al. (2009)](/sources/balsara-2009.md), §4.2).
* *Componentwise* WENO suffices for linear systems ([Dumbser & Käser (2007)](/sources/dumbser-2007.md), §3.1). The
  third-order ADER-WENO AMR runs of the Orszag–Tang vortex use
  componentwise reconstruction ([Dumbser et al. (2013)](/sources/dumbser-2013.md), §4), while the AMR-DG Riemann
  problems and explosions use characteristic reconstruction ([Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.1).
* *Boundaries.* Characteristic decomposition with Roe-averaged
  eigenvectors at each flux point precedes Lax–Friedrichs splitting in
  energy-stable WENO; the order holds although the Roe average is only
  second-order accurate ([Fisher et al. (2011)](/sources/fisher-2011.md), §6.3). At inflow boundaries, the
  incoming characteristic variables take the boundary data while the
  outgoing ones are extrapolated ([Lu et al. (2016)](/sources/lu-2016.md), §§2.3–2.5;
  [inverse Lax–Wendroff](/methods/inverse-lax-wendroff.md)).

**Later uses (batch 5).**
* *MHD eigenvectors.* Fifth-order FD-WENO for ideal MHD uses Brio–Wu
  normalized eigenvectors, which stay complete and nonsingular where the
  fast, Alfvén and slow speeds coincide. The degeneracy tests are relaxed
  by a threshold of about $10^{-12}$. The interface state is the
  arithmetic mean, which differs little from a Roe average for
  time-dependent problems (a single Roe state exists only for
  $\gamma = 2$). In 2D a seven-wave system (normal-field equation
  dropped) and Powell's eight-wave system give the same flux except in
  the normal-field component, and the eight-wave one adds diffusion there
  ([Jiang & Wu (1999)](/sources/jiang-1999.md), §2.3).
* *Boundary case selection.* At a boundary whose normal velocity changes
  sign, the signs of the characteristic speeds decide how many conditions
  are imposed. The missing conserved component is recovered from the
  extrapolated outgoing characteristic variables, dividing only by
  eigenvector entries, never by an eigenvalue
  ([Lu et al. (2021)](/sources/lu-2021.md), §§2.2–2.3;
  [inverse Lax–Wendroff](/methods/inverse-lax-wendroff.md)).
* *Interfaces.* At a fluid–structure interface the outgoing characteristics
  of both media, plus the interface conditions, close one local linear
  system ([Liu et al. (2025)](/sources/liu-2025.md), §3.2).
* *Avoided by design.* A fifth-order FD scheme for block-adaptive
  curvilinear grids interpolates primitive variables with an MP5 limiter
  instead, to stay equation-agnostic and cheap
  ([Chen, Tóth & Gombosi (2016)](/sources/chen-2016.md), §1;
  [monotonicity-preserving limiting](/methods/monotonicity-preserving-limiter.md)).

**Later uses (batch 6).**
* *Arithmetic means of primitive variables* for the MHD interface state,
  with Barth's entropy-variable scaling of the eigenvectors. Global and
  local Lax–Friedrichs speeds made no significant difference in SSP-RK
  FD-WENO with CT ([Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md), §4, Remarks 1–3).
  That qualifies the 2016 statement above, made for a different
  (single-step) scheme.
* *GLM-MHD.* The nine-wave system splits into a constant-coefficient
  $2\times2$ part, reconstructed grid-wide with no local projection, and
  the usual $7\times7$ MHD eigensystem
  ([Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md), §3.1;
  [hyperbolic divergence cleaning](/methods/hyperbolic-divergence-cleaning.md)).
* *Isothermal MHD* has six waves and no entropy mode; HOW-MHD uses
  Ryu–Jones (adiabatic) and Kim et al. (isothermal) eigenvectors
  ([Seo & Ryu (2023)](/sources/seo-2023.md), §2.2).
* *Second-order MHD slopes* can be limited per characteristic family,
  with WENO optimal weights biased by wave direction, because MHD "seem[s]
  to require more limiting than the corresponding hydrodynamic" case
  ([Balsara (2004)](/sources/balsara-2004.md), §§3.3–3.4).
* *Relativistic MHD.* Reconstructing the four-velocity resolves speeds
  that bunch near 1: $v_x = 0.999$ and 0.9999 differ by 0.0009, while
  the four-velocity components are 22.344 and 70.704 ([Balsara & Kim (2016)](/sources/balsara-2016-b.md), §2).

**In the reviews (batch 6).** Componentwise reconstruction "usually"
suffices up to third order, and characteristic reconstruction is better
at higher order, at greater cost ([Shu (2009)](/sources/shu-2009.md), §3.5.3). It is satisfactory for
smooth or weak-shock problems but "could lead to spurious oscillations"
for strong shocks and for several discontinuities from one initial jump.
The interface state is the Roe average, or the arithmetic mean where no
Roe average exists ([Shu (2020)](/sources/shu-2020.md), §4.1).

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
19. [Qiu & Shu (2005)](/sources/qiu-2005.md), §2.
20. [Balsara et al. (2009)](/sources/balsara-2009.md), §4.2.
21. [Dumbser & Käser (2007)](/sources/dumbser-2007.md), §3.1.
22. [Dumbser et al. (2013)](/sources/dumbser-2013.md), §4.
23. [Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.1.
24. [Fisher et al. (2011)](/sources/fisher-2011.md), §6.3 and Appendix B.
25. [Lu et al. (2016)](/sources/lu-2016.md), §§2.3–2.5.
26. [Jiang & Wu (1999)](/sources/jiang-1999.md), §2.3.
27. [Lu et al. (2021)](/sources/lu-2021.md), §§2.2–2.3.
28. [Liu et al. (2025)](/sources/liu-2025.md), §3.2.
29. [Chen, Tóth & Gombosi (2016)](/sources/chen-2016.md), §1.
30. [Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md), §4 (arXiv v2).
31. [Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md), §3.1 (arXiv v2).
32. [Seo & Ryu (2023)](/sources/seo-2023.md), §2.2.
33. [Balsara (2004)](/sources/balsara-2004.md), §§3.3–3.4.
34. [Balsara & Kim (2016)](/sources/balsara-2016-b.md), §2.
35. [Shu (2009)](/sources/shu-2009.md), §3.5.3.
36. [Shu (2020)](/sources/shu-2020.md), §4.1.
