---
type: Method
title: "Contact-discontinuity sharpening (subcell resolution, artificial compression, steepening)"
description: "Techniques that counter the progressive smearing of linearly degenerate discontinuities in capturing schemes: Harten's subcell resolution, Harten–Yang artificial compression, and PPM contact steepening; applied only to contacts, never to shocks."
status: established
aliases: [artificial compression, ACM, subcell resolution, contact steepener]
tags: [contact-discontinuity, steepening, eno, weno]
timestamp: 2026-10-08T00:00:00Z
---

# Contact-discontinuity sharpening

**The problem.** Shocks self-sharpen because characteristics converge
into them; contacts (linearly degenerate fields) have parallel
characteristics, so numerical smearing accumulates and the
discontinuity widens progressively with time. Harten gives a rate that
depends on the order $k$; higher orders smear less, but still
significantly at long times ([Shu (1998)](/sources/shu-1998.md), §4.1.1;
the rate's exponent is illegible in the text layer of the copy read and
is not reproduced here).
ENO and WENO smear contacts alike
([Jiang & Shu (1996)](/sources/jiang-1996.md);
[Liu, Osher & Chan (1994)](/sources/liu-1994.md)).

**Subcell resolution** (Harten). In the cell containing the
discontinuity the reconstruction is inaccurate (only its average is
useful). Extend the neighbours' polynomials into the cell and place the
discontinuity where the cell average is preserved; under general
conditions there is a single root. [Shu & Osher (1989)](/sources/shu-1989.md)
translate it to the flux framework with RK stepping (Algorithm 3.1),
simpler and theoretically less accurate than Harten's but numerically
close; a naive 2D generalization failed. It must not be applied to
shocks (risk of entropy-violating expansion shocks) and is hard in 2D
([Shu (1998)](/sources/shu-1998.md), §4.1.1).

**Artificial compression** (Harten; Yang's slope modification). Add to
the reconstruction a steepening term that increases the slope near a
discontinuity, bounded by minmod constraints so that monotonicity (TVD
or ENO property) is preserved for any compression parameter
([Shu & Osher (1989)](/sources/shu-1989.md), Algorithm 3.2, parameter
2–5; [Jiang & Shu (1996)](/sources/jiang-1996.md) use Yang's 33 with
WENO). It works in 1D and 2D and is applied only in linearly degenerate
fields for Euler. Costs: 40–65 % more operations with Roe building
blocks, 65–100 % with Lax–Friedrichs
([Jiang & Shu (1996)](/sources/jiang-1996.md), §7).
[Balsara & Shu (2000)](/sources/balsara-2000.md) write the slope modifier
as the product of a discontinuity detector and a balance factor (fixed
at 4.3) and find that higher orders need *less* compression — maximal
coefficient 20 for $r = 3, 4$, 15 for $r = 5, 6$, none for $r = 7$ — and
that schemes with $r \ge 5$ carry a contact over about seven zones
without degradation, so they may not need it; it does not degrade the
convergence order on smooth data (Table IX).

**PPM steepening** ([Colella & Woodward (1984)](/sources/colella-1984.md)):
discontinuity detection replaces edge values in cells judged inside a
contact with values from the limited linear profiles of the neighbours
([PPM](/methods/ppm.md)). On long-time advection it squares off smooth
pulses and, lacking a balance factor, makes them asymmetric
([Balsara & Shu (2000)](/sources/balsara-2000.md), Fig. 1d).

# Citations

1. [Shu & Osher (1989)](/sources/shu-1989.md), §III.
2. [Jiang & Shu (1996)](/sources/jiang-1996.md), §§1, 5, 7.
3. [Shu (1998)](/sources/shu-1998.md), §§4.1.1–4.1.2.
4. [Balsara & Shu (2000)](/sources/balsara-2000.md), §§V–VI.a.
5. [Colella & Woodward (1984)](/sources/colella-1984.md), §1.
6. [Liu, Osher & Chan (1994)](/sources/liu-1994.md), §4.
