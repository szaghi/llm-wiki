---
type: Benchmark
title: "Double Mach reflection"
description: "The Woodward–Colella problem of a Mach 10 shock reflecting at 30 degrees in a gamma = 1.4 gas; used qualitatively to compare reconstructions, carbuncle fixes, and AMR against uniform grids."
status: established
aliases: [DMR, Woodward–Colella double Mach reflection]
tags: [benchmark, hydro, verification, amr]
timestamp: 2026-10-12T00:00:00Z
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

# Citations

1. [Stone et al. (2008)](/sources/stone-2008.md), §8.3.
2. [Bryan et al. (2014)](/sources/bryan-2014.md), §11.2.4 (arXiv v1).
3. [Stone et al. (2020)](/sources/stone-2020.md), §3.4.2.
4. [Lesur et al. (2023)](/sources/lesur-2023.md), §4.1 (arXiv v1).
