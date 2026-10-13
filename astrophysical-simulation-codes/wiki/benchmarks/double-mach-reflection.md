---
type: Benchmark
title: "Double Mach reflection"
description: "The Woodward–Colella problem of a Mach 10 shock reflecting at 30 degrees in a gamma = 1.4 gas; used qualitatively to compare reconstructions, carbuncle fixes, and AMR against uniform grids."
status: established
aliases: [DMR, Woodward–Colella double Mach reflection]
tags: [benchmark, hydro, verification, amr]
timestamp: 2026-10-13T00:00:00Z
---

# Double Mach reflection

**Set-up.** After Woodward & Colella (1984): a Mach 10 shock at 30° in a
$\gamma = 1.4$ gas, on a rectangular domain. Stone et al. (2008) defer the
set-up to Woodward & Colella; Bryan et al. (2014) print it (below). There
is no exact solution; results are compared with Woodward & Colella's
figures and between schemes or grids.

**Runs.**

* [Stone et al. (2008)](/sources/stone-2008.md), §8.3, Fig. 16. Set-up
  deferred to Woodward & Colella; $t = 0.2$. PLM and PPM at
  $260\times80$ and $520\times160$, Roe with the H-correction (to reduce
  post-shock noise), CTU. PPM is slightly less diffusive. Compared with
  Woodward & Colella Fig. 4 and with ZEUS (Stone & Norman 1992a,
  Figs. 15–16).
* [Bryan et al. (2014)](/sources/bryan-2014.md), §11.2.4, Fig. 7.
  $960\times240$ cells on $[0, 4]\times[0, 1]$, pre-shock $\rho = 1.4$ and
  $e = 2.5/1.4$, shock at 30° starting at $x = 1/6$, to $t = 0.205$; PPM
  with diffusion, flattening and steepening. Qualitative comparison with
  Woodward & Colella Fig. 9.
* [Stone et al. (2020)](/sources/stone-2020.md), §3.4.2, Fig. 20.
  Characteristic reconstruction, HLLE (to avoid the carbuncle). Uniform
  $h = 1/120$ against [AMR](/methods/adaptive-mesh-refinement.md) on a
  root grid of $h = 1/30$ with 2 levels and $6\times6$ blocks, refining
  where a normalized second-derivative (curvature) indicator exceeds 0.01
  and derefining below 0.005 (eq. 25). The AMR solution is
  indistinguishable from the uniform one. Decomposed into $6^2$ blocks, the
  uniform and AMR runs take 279 and 63.2 CPU s (a factor 4.4); into
  $12^2$ blocks, 127 and 31.8 s; the uniform grid as a single block takes
  42.8 s. The CFL number is not printed.

**What it shows.** Sensitivity to reconstruction (PPM slightly less
diffusive than PLM) and to the carbuncle, which both [Athena](/software/athena.md) papers
suppress, by the H-correction ([Stone et al. (2008)](/sources/stone-2008.md))
or by the HLLE solver ([Stone et al. (2020)](/sources/stone-2020.md)); see
[approximate Riemann solvers](/methods/approximate-riemann-solvers.md).
With AMR it exposes the cost of block decomposition: small blocks slow
the uniform grid from 42.8 s (one block) to 279 s ($6^2$ blocks), and
the AMR gain must be read against the same block size
([Stone et al. (2020)](/sources/stone-2020.md), §3.4.2). All
comparisons are qualitative.

## Later uses (batch 3)

* [Lesur et al. (2023)](/sources/lesur-2023.md), §4.1, Fig. 3;
  [IDEFIX](/software/idefix.md). Initial conditions deferred to the 1984
  Colella–Woodward work (cited in that author order); $1920\times480$,
  $t = 0.2$, several combinations of reconstruction, Riemann solver and
  integrator. LimO3 and PPM give a more vigorous jet and the onset of
  Kelvin–Helmholtz rolls. Visual comparison with Stone et al. (2008),
  Fig. 16, and Mignone et al. (2007), Fig. 2.

This agrees with the reading above that PPM is less diffusive than PLM
on this test, adds LimO3 to the less diffusive side, and uses about 3.7
times as many cells per direction as the larger Stone et al. (2008) run
(1920 against 520 along $x$). It remains qualitative.

## Later uses (batch 8)

* **Unsplit against split in the CTU paper.** [Colella (1990)](/sources/colella-1990.md), §5, Figs. 8–10, runs a Mach 10 shock on a 30° wall at $400\times100$ zones, $h = 1/120$, the wall starting 20 mesh lengths from the lower left corner, $t = 0.2$ ("the finest grid results" of Woodward & Colella). His unsplit CTU and operator-split results with the same parameters are "essentially identical". The transverse choice of his eq. 2.13 gives "considerably lower resolution in the jet along the wall" (pp. 197–198). The Courant number is not printed. The mesh implies a $3.33\times0.83$ domain (inferred, not printed).

## Later uses (batch 9)

### The set-up in its primary source

[Woodward & Colella (1984)](/sources/woodward-1984.md), §IVc, §VIc,
Figs. 4, 9–10, print the set-up that the runs above defer to.

* **Geometry.** A Mach 10 shock in air ($\gamma = 1.4$) that "initially
  makes a 60° angle with" the reflecting wall, i.e. with the $x$ axis;
  undisturbed gas $\rho = 1.4$, $p = 1$. Domain $[0,4]\times[0,1]$ (plots
  show $0 \le x \le 3$); the wall runs along the bottom from $x = 1/6$,
  where the shock meets it, and the shock extends to the top. The shock is
  tilted, not the wall, to avoid oblique boundaries.
* **The angle.** The 30° of this page's set-up and of the Bryan et al. and
  Colella (1990) entries is not the angle Woodward & Colella print. With the
  shock at 60° to the wall, the shock normal makes 30° with the wall, which
  is the ramp angle of the equivalent wedge geometry (computed here; the
  paper does not state it). Two descriptions of one configuration, not a
  contradiction.
* **Boundary conditions.** Bottom for $x < 1/6$ and the left boundary:
  post-shock values, which keep the reflected shock attached to the wall.
  Bottom for $x \ge 1/6$: reflecting. Right: zero gradients. Top: values
  set "to describe the exact motion of the initial Mach 10 shock".
* **Output and grids.** $t = 0.2$, on $h = 1/30$, 1/60 and 1/120 (Fig. 9).
  Fig. 4, the figure Stone et al. (2008) compare with, is PPMDE at
  $h = 1/120$ with grid jiggling; its legend gives a Courant number of 0.8
  and $t = 0.200260$ (read from the OCR only). Bryan et al.'s comparison
  figure, Fig. 9, holds all schemes at the three grids; its panels 9f and 9g
  are PPMDE (with Lapidus viscosity 0.1) and PPMLR. Bryan et al.'s
  $t = 0.205$ differs from the original's 0.2.
* **Flow features.** Two Mach stems and two contacts, the second very weak;
  the second Mach shock dies before reaching the first contact; a wall jet
  of dense gas forms. A near-stagnant region between the second Mach shock,
  the reflected shock and the wall makes schemes whose dissipation vanishes
  with the velocity oscillate. Even at $h = 1/120$ the jet is "less than
  five zones wide".
* **Starting error.** The shock is initialized, and imposed on the top
  boundary, as a one-zone jump; this produces an overheated strip about two
  zones wide, visible from the top-right corner to the wall near $x = 2$,
  which "mars" all results. Any comparison with these figures inherits it.
* **Scheme findings.** Godunov leaves the jet unresolved even at 1/120;
  MacCormack gives shocks 2–3 zones wide with oscillations; BBC has no
  oscillations but a poor second Mach shock; ETBFCT shows staircases and a
  wrong Mach-stem shape; MUSCL is best except for noise. PPMDE is more
  efficient than BBC and MacCormack by factors >4.9 and >1.3, PPMLR by
  >4.4 and >1.2, with fewer starting errors and a sharper second Mach
  shock; PPM costs 20 % more than MUSCL (Figs. 9f–g, as printed).

This agrees with the batch-8 reading of [Colella (1990)](/sources/colella-1990.md):
$h = 1/120$ and the wall start at $x = 1/6$ (20 mesh lengths) are the
original's finest grid and position.

**Berger & Colella's resolution claim, checked.** They print (§7, p. 79): "The finest grids in this calculation represent a factor of 4 increase in resolution in each spatial direction over the finest grid calculation in [22]", [22] being [Woodward & Colella (1984)](/sources/woodward-1984.md). Their finest $h = 1/800$ is 6.7 times the original's $h = 1/120$, but the solution is self-similar in $(x/t, y/t)$, so resolution relative to the wave pattern scales as $h/t$: $(1/120)/0.2 \div (1/800)/0.12 = 4.0$ (compiler computation at deep lint #4, using the Fig. 7.1 caption's $t = 0.12$ — the text prints 1.20 — and assuming the same nondimensionalization, which Berger & Colella do not print). The printed factor 4 is consistent; the flag is withdrawn. At $t = 1.20$ the pattern would not fit the $2.0\times0.4$ domain, which supports the caption's value.

# Citations

1. [Stone et al. (2008)](/sources/stone-2008.md), §8.3.
2. [Bryan et al. (2014)](/sources/bryan-2014.md), §11.2.4 (arXiv v1).
3. [Stone et al. (2020)](/sources/stone-2020.md), §3.4.2.
4. [Lesur et al. (2023)](/sources/lesur-2023.md), §4.1 (arXiv v1).
5. [Colella (1990)](/sources/colella-1990.md), §5, Figs. 8–10, pp. 197–198.
6. [Woodward & Colella (1984)](/sources/woodward-1984.md), §§IVc, VIc, Figs. 4, 9–10, p. 136.
7. [Berger & Colella (1989)](/sources/berger-1989.md), §7, Fig. 7.1, p. 79.
