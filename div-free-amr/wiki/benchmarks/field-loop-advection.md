---
type: Benchmark
title: "Field-loop advection"
description: "Passive advection of a weak magnetic loop; the standard detector of divergence-constraint violations and stencil inconsistency in MHD schemes."
status: established
tags: [benchmark, divergence-constraint, mhd, constrained-transport]
timestamp: 2026-10-13T00:00:00Z
---

# Field-loop advection

A weak magnetic field loop (magnetic pressure dynamically negligible) is
advected by a uniform velocity across a periodic domain; the exact
solution is pure translation. Sensitive quantities: preservation of the
loop's shape, decay of magnetic energy, and — the diagnostic that made
the test canonical — spurious growth of field components that should stay
identically zero.

**Origin.** The 2D form was introduced by
[Gardiner & Stone (2005)](/sources/gardiner-stone-2005.md) §3.3.1. A loop
whose out-of-plane vector potential is proportional to the distance
inside the loop radius, measured from the loop's edge (zero outside), with $\beta = 2\cdot10^6$, is advected along the
diagonal of a periodic $2N\times N$ grid, so the field is effectively a
passive scalar. Its first job there was to discriminate the dissipation of
corner-EMF algorithms: an unbiased EMF goes oscillatory and a
Lax–Friedrichs one diffuses. It also exposes missing multidimensional
source terms in the interface states: without them "the field loop
disintegrates in oscillations before completing a fraction of an orbital
period".

## What it detects, per the compiled sources

* **Stencil inconsistency** (the sharpest use): in 3D, a loop confined to
  the $(x,y)$-plane advected with $u_z \ne 0$ grows spurious $B_z$ unless
  the divergence is held **on the same stencil used to construct the
  $B_z$ fluxes**; round-off-constant $B_z$ certifies consistency
  ([Gardiner & Stone (2008)](/sources/gardiner-stone-2008.md), where the
  test motivates the divergence-balanced PPM source terms —
  [exact discrete divergence](/properties/exact-discrete-divergence.md)).
  **The slot those terms fill.** The hydrodynamic template of "PPM
  interface states" is the characteristic tracing of the PPM paper, which
  already corrects its first-guess states with geometric and gravity
  sources inside the tracing. The MHD source terms enter the same slot.
  That paper has no magnetic field, so the divergence-balance requirement
  is entirely post-1984 and MHD-specific
  ([Colella & Woodward (1984)](/sources/colella-woodward-1984.md), §3,
  eqs. 3.3–3.7; [PPM](/methods/ppm.md)).
* **The same distinction in the Athena code paper** ([Stone, Gardiner, Teuben, Hawley & Simon (2008)](/sources/stone-2008.md) §8.4). With the
  loop axis along a grid direction, Athena keeps $B_z = 0$ to round-off.
  With the loop inclined, the axial component is zero only to truncation
  error, matching the rotated-loop result below.
* **Fourth-order CT in 3D** ([Felker & Stone (2018)](/sources/felker-2018.md)). The loop
  is advected along the space diagonal with $\mathbf u = (2,1,2)$, on a $[-1,1]\times[-0.5,0.5]\times[-1,1]$ box with $N = 64$ cells across $x_2$.
  * $B_z$ stays below machine epsilon for two periods.
  * Loop edges are resolved in 4 cells, against 6–8 at second order.
  * The second-order scheme opens a larger reconnection hole and
    overshoots the peak by about 20%, against about 8% at fourth order.
* **A rotated 3D loop measures what CT does not hold**
  ([Mignone & Del Zanna (2021)](/sources/mignone-2021.md)).
  * The loop is rotated about $y$ (rotation angle with tangent 1/2), with $\mathbf u = (1,1,2)$
    on $64\times64\times128$.
  * The field component along the loop axis is then zero only to
    truncation error, not round-off. It ranks EMF schemes: UCT is best,
    CT-Contact and CT-Flux are worse, and arithmetic averaging is worst,
    disrupting the loop at third order.
  * This differs from Felker & Stone's round-off $B_z$. In their geometry
    $B_z$ is the component whose update CT cancels exactly; here the axial
    component mixes all three.
* **Fourth-order CT with point-value reconstruction, MHD and RMHD**
  ([Berta et al. (2024)](/sources/berta-2024.md) §5.4). On a 2D loop at $256\times128$,
  smearing and magnetic-energy decay fall steadily from second to fourth
  order. WENO-Z ([WENO](/methods/weno.md)) is best; MP5 shows small over- and undershoots at the
  loop's head and tail. The choice of Riemann solver matters only
  marginally here.
* **EMF-assembly dissipation**: magnetic-energy decay differentiates
  Riemann-solver and EMF-averaging choices
  ([Fromang et al. (2006)](/sources/fromang-2006.md), Roe vs
  Lax–Friedrichs; [Balsara (2004)](/sources/balsara-2004.md) test suite).
* **Constraint machinery on unstructured/hybrid meshes**: 2D and 3D loop
  advection validates the exactly divergence-free hybrid schemes of
  [Zampa (2024)](/sources/zampa-2024.md).
* **High-order cleaning, uniform grid**
  ([Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-tzeferacos-bodo-2010.md)).
  * 2D on $128\times64$, and 3D on $128\times128\times256$ with
    $\mathbf u = (1,1,2)$ and the loop rotated about one axis.
  * Fifth-order schemes are visibly less diffusive than third-order ones in
    both shape and magnetic-energy decay.
  * The divergence error depends on the damping parameter in an
    order-dependent way. See [GLM](/methods/glm-divergence-cleaning.md).
* **A cleaning scheme across 2:1 seams** ([Zaghi (2026)](/sources/zaghi-2026.md),
  hypothesis). Collocated WENO MHD with
  [GLM](/methods/glm-divergence-cleaning.md), with a $u_z$ component so that
  $\partial_t B_z$ measures the divergence error.
  * The generated $\langle|B_z|\rangle$ stays at the cleaning level and
    decreases under refinement.
  * Magnetic energy retained at 64/128 cells: 0.872/0.937 with flux
    splitting, 0.887/0.944 with HLLD on characteristic variables.
  * On a 2:1 grid, the compiler's reading of the captured histories: the
    seam divergence peaks when the loop crosses the seam
    ($9.75\cdot10^{-4}$ at $t \approx 0.38$, 64²), not at the first step as
    the code's docs state. It then decays about 3×, to the uniform-grid
    interior level, by $t = 1$.
  * In a scheme without an exact invariant the test therefore reads the
    seam as one more truncation source, not as a distinct defect.

**High-order FD-WENO with high-order CT** ([Seo & Ryu (2023)](/sources/seo-2023.md)). In 2D, with the
loop crossing the domain 20 times at $256\times128$, the CT order is
visible. The second-order CT distorts the loop, while CT4 and CT6 keep it
circular. At $t = 20$ and $N = 128$, about 96% of the magnetic energy is
retained with the high-order CT, against about 95% with the second-order
one, with a larger gap at coarser grids. A nearly grid-aligned loop
($\tan\theta = 1/100$) shows few-percent oscillations along $y$ that do not
grow. In 3D the tilted cylindrical loop erodes at its core and rim with the
second-order CT only.

The test's virtue is that it is *trivial physics with unforgiving
algebra*: any constraint-consistent error channel — wrong stencil, biased
EMF, transfer-operator leakage — shows up as structure the exact solution
forbids.

# Citations

1. [Gardiner & Stone (2008)](/sources/gardiner-stone-2008.md), §1, §6.
2. [Fromang et al. (2006)](/sources/fromang-2006.md), §3.
3. [Balsara (2004)](/sources/balsara-2004.md), §7.
4. [Zampa (2024)](/sources/zampa-2024.md), §4.6.4.
5. [Zaghi (2026)](/sources/zaghi-2026.md): FLUME `verification.md` (MV-9, "MHD on weno-riemann" table); captured field-loop div(B) histories.
6. [Gardiner & Stone (2005)](/sources/gardiner-stone-2005.md), §§3.1, 3.3.1, 5.1.
7. [Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-tzeferacos-bodo-2010.md), §4.4, Figs. A.8–A.11.
8. [Felker & Stone (2018)](/sources/felker-2018.md), §5.3, Figs. 12–14.
9. [Mignone & Del Zanna (2021)](/sources/mignone-2021.md), §6.1, Figs. 2–7.
10. [Berta et al. (2024)](/sources/berta-2024.md), §5.4, Figs. 6–7.
11. [Seo & Ryu (2023)](/sources/seo-2023.md), §3.3, Figs. 4–7.
12. [Stone, Gardiner, Teuben, Hawley & Simon (2008)](/sources/stone-2008.md), §8.4, Fig. 34.
13. [Colella & Woodward (1984)](/sources/colella-woodward-1984.md), §3.
