---
type: Benchmark
title: "Self-gravitating polytrope"
description: "A 3D polytropic star, in equilibrium or perturbed into collapse, on a Cartesian grid with Poisson self-gravity; it exposes energy errors of non-conservative gravity coupling (spurious heating, loss of spherical symmetry, a central hole) and anomalous forces of gravitational stress-tensor discretizations in a light atmosphere."
status: established
aliases: [polytrope test, polytropic star, collapsing polytrope, polytrope with atmosphere]
tags: [benchmark, self-gravity, conservation, verification]
timestamp: 2026-10-12T00:00:00Z
---

# Self-gravitating polytrope

**Set-up.** A polytropic sphere sits at the centre of a periodic or
isolated Cartesian box, surrounded by a low-density background, with
self-gravity from a Poisson solve. In equilibrium any motion is an error;
perturbed, it collapses or oscillates. Both sources use it to compare a
[conservative self-gravity](/methods/conservative-self-gravity.md)
coupling with non-conservative source terms.

**Variants.**
* *Collapse of a polytrope of index 3 with $\gamma = 1.36$*
  ([Jiang et al. (2013)](/sources/jiang-2013.md), §4.2, Figs. 6–8).
  Units $4\pi G = 1$, central density 1, central pressure
  $8.09\times10^{-5}$, background density 0.005, diameter 0.16 (20% of
  the box), $256^3$ cells, periodic, FFT gravity, Athena with HLLC at
  Courant number 0.8. The central pressure is lowered to 0.93 of
  equilibrium; a homologous estimate gives a collapse to about 0.4 of the
  radius. The conservative and non-conservative runs agree until $t = 15$.
  Afterwards the non-conservative energy source reaches a much higher
  peak central density, loses spherical symmetry by $t = 460$, more so by
  680, and forms a central low-density hole by 900; the conservative run
  stays near-periodic and spherical. Both use the conservative momentum
  flux, so the difference is the energy coupling. For small oscillations
  of a $\gamma = 5/3$ polytrope the two algorithms are "very similar" (§6;
  no figure).
* *Equilibrium $\gamma = 2$ polytrope with a light atmosphere*
  ([Mullen et al. (2021)](/sources/mullen-2021.md), §4.3, Figs. 5–8).
  Atmosphere mass $10^{-2}$ of the body, $80^3$ cells, about 10 cells per
  radius, Athena++. The older gravitational stress-tensor flux destroys
  the atmosphere with a fourfold azimuthal pattern, its initial
  $(\nabla\times\mathbf g)_z$ reaching about $\pm0.1$; the source-term
  scheme and the new tensor keep the equilibrium and are curl-free to
  round-off. With white noise of $10^{-4}$ times the surface potential added
  to $\Phi$,
  only the source-term scheme shows no spurious velocities. A
  non-conservative cell-centred energy source heats the polytrope
  steadily, so that its central density drops by about 30% after 100 time
  units of radius over escape speed, while the conservative scheme
  settles.

**What it shows.** In both, energy errors of a non-conservative coupling
change the dynamics of a self-gravitating star (collapse depth and
symmetry in Jiang et al.; secular heating and expansion in Mullen et al.),
and neither reports an error norm or a convergence rate for this test.
Stars with a realistic equation of state are run as the
[hydrostatic white dwarf](/benchmarks/hydrostatic-white-dwarf.md).

# Citations

1. [Jiang et al. (2013)](/sources/jiang-2013.md), §§4.2, 6, Figs. 6–8
   (arXiv v2).
2. [Mullen et al. (2021)](/sources/mullen-2021.md), §4.3, Figs. 5–8.
