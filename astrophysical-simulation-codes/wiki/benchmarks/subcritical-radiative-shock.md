---
type: Benchmark
title: "Subcritical radiative shock"
description: "A steady Mach 3 non-equilibrium radiative shock with a radiative precursor and a Zel'dovich temperature spike, compared with the semi-analytic solution of Lowrie & Edwards (2008); it tests the coupling of gas and radiation across a shock and is sensitive to the closure the reference solution assumes."
status: established
aliases: [sub-critical radiative shock, Lowrie–Edwards radiative shock, non-equilibrium radiative shock, Mach 3 radiative shock]
tags: [benchmark, radiation, verification, reduced-speed-of-light]
timestamp: 2026-10-12T00:00:00Z
---

# Subcritical radiative shock

**Set-up.** A planar shock of upstream Mach number 3 in a gray,
radiating ideal gas with $\gamma = 5/3$. Radiation preheats the upstream
gas (the precursor) without bringing it to the post-shock temperature
(subcritical), and the gas temperature overshoots just behind the shock
(the Zel'dovich spike). The reference is the semi-analytic
non-equilibrium solution of Lowrie & Edwards (2008), which uses the
Eddington approximation $\mathsf P_{\mathrm r} = E_{\mathrm r}\mathsf I/3$
([Skinner & Ostriker (2013)](/sources/skinner-2013.md), §4.3.5;
[Wibking & Krumholz (2022)](/sources/wibking-2022.md), §3.3.3).

**Runs.**

* [Skinner & Ostriker (2013)](/sources/skinner-2013.md), §4.3.5,
  Fig. 22. [Athena](/software/athena.md)'s Hyperion module
  ([M1 radiation transport](/methods/m1-radiation-transport.md), unsplit
  VL with piecewise-linear reconstruction, HLL). Dimensionless set-up:
  opacity 1, ratio of radiation to gas pressure $10^{-4}$, Mach 3;
  $N = 1024$, Dirichlet boundaries; domain set where the temperature
  perturbation falls to $10^{-4}$ of the upstream value; shock frame, with
  the front tracked. With the computed M1 eigenvalues the relative errors
  are 1.7 % in $\rho$, 6.1 % in gas temperature and 7.8 % in radiation
  temperature, with a resolution-independent discrepancy in the
  precursor. With the HLL wave speeds fixed at $\mp\hat c/\sqrt3$ (the
  Eddington values) they are 0.42 %, 0.49 % and 0.42 %. The authors
  attribute the difference to the Eddington approximation in the
  reference solution, not to the reduced speed of light. The Zel'dovich
  spike is captured.
* [Wibking & Krumholz (2022)](/sources/wibking-2022.md), §3.3.3, Fig. 16.
  [Quokka](/software/quokka.md), set-up after Skinner et al. (2019) in
  physical units: opacity $577\,(1\,\mathrm{g\,cm^{-3}}/\rho)$ cm² g⁻¹
  (Planck and Rosseland), $\mu = 1$; upstream
  $\rho = 5.69$ g cm⁻³, $v = 5.19\times10^7$ cm s⁻¹, $T = 2.18\times10^6$ K;
  downstream $\rho = 17.1$ g cm⁻³, $v = 1.73\times10^7$ cm s⁻¹,
  $T = 7.98\times10^6$ K; Eddington closure
  $\mathsf P_{\mathrm r} = E_{\mathrm r}\mathsf I/3$ (not the default
  Levermore closure); $\hat c$ equal to 10 times the upstream speed plus
  sound speed; CFL 0.4; 512 cells on $[0, 0.01575]$ cm with the shock
  initially at 0.0130 cm; run to $t = 10^{-9}$ s. The shock drifts by
  1.5 % of the domain; after correcting the drift the L1 relative error of
  the gas temperature is 0.4 %, "at least as good as" Skinner et al.
  (2019) at the same resolution. Miller–Colella flattening is essential for
  a non-oscillatory Zel'dovich spike. A semi-analytic solver ships with
  the code (footnote 8).

**Comparing the two.** Both match the reference best when the radiation
is closed or bounded with Eddington values: Hyperion keeps the M1 closure
but fixes the HLL wave speeds, while Quokka replaces the closure by the
Eddington tensor. The error measures also differ (Skinner & Ostriker
quote relative errors per variable; Quokka quotes an L1 relative error
after drift correction), as do resolution (1024 against 512 cells) and
units. The 0.49 % and 0.4 % gas-temperature errors are therefore not a
like-for-like comparison. Neither source states a convergence rate.

The Quokka text cites "Figure 11" for the Zel'dovich spike; the figure is
Fig. 16 ([Wibking & Krumholz (2022)](/sources/wibking-2022.md), §3.3.3).

# Citations

1. [Skinner & Ostriker (2013)](/sources/skinner-2013.md), §4.3.5 (arXiv v1).
2. [Wibking & Krumholz (2022)](/sources/wibking-2022.md), §3.3.3 (arXiv v2).
