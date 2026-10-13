---
type: Benchmark
title: "Quirk's odd–even decoupling test"
description: "A Mach 6 shock moving down a long duct whose grid centreline is displaced alternately by a small amount: low-dissipation Riemann solvers let the perturbation grow until the shock profile breaks up (odd–even decoupling); the standard first check of a shock-instability cure, generalized by Kitamura & Shima into a map over shock strength and shock speed."
status: established
aliases: [odd–even decoupling test, Quirk's test, moving-shock instability problem, perturbed duct test]
tags: [benchmark, euler, shock-instability, 2d]
timestamp: 2026-10-13T00:00:00Z
---

# Quirk's odd–even decoupling test

**Set-up.** A rectangular duct of $800\times20$ cells with walls at the
top and bottom. The vertices of the grid centreline are displaced
alternately up and down by $\epsilon_{\mathrm g}$ (in cell sizes). A
$M_s = 6$ shock moves into gas at rest with $\rho = 1.4$, $p = 1$,
$\gamma = 1.4$ ([Xie et al. (2021)](/sources/xie-2021.md), §6.1, eq. 81;
[Simon & Mandal (2019b)](/sources/simon-2019-b.md), §7.1). Kitamura &
Shima give the same shock in normalized form, pre-shock
$(\rho, v_x, v_y, p) = (1, 0, 0, 1/\gamma)$ and post-shock
$(5.2683, 4.8611, 0, 29.881)$. The shock starts on the interface between
cells 25 and 26 ([Kitamura & Shima (2019)](/sources/kitamura-2019.md), §III.D, eqs. 12–13).
* The perturbation size varies:
  * $\epsilon_{\mathrm g} = 10^{-3}$, Quirk's value (Kitamura & Shima;
    Xie et al. use $\pm 0.001$);
  * $10^{-6}$ ([Simon & Mandal (2019)](/sources/simon-2019.md), §9.2;
    [Simon & Mandal (2019b)](/sources/simon-2019-b.md), §7.1).
* The Simon & Mandal papers print the ambient velocity as $v_x = 1.0$ for
  a "stationary fluid", which is recorded as printed. They run until the
  shock reaches $x = 650$.
* Xie et al. report the solution at $t = 25$ and $50$.

**Results.**
* First-order HLLC and HLLEM: the shock profile "deteriorated". Every
  [cure](/methods/shock-instability-cures.md) tested keeps it clean:
  selective wave modification, anti-diffusion control, and Xie et al.'s
  2017 shear-only control (Simon & Mandal 2019, §9.2; 2019b, §7.1).
* Godunov, Roe, HLLEM and HLLC: all destroy the shock, Godunov and HLLC
  less readily than Roe and HLLEM. With the entropy-control term none
  decouples ([Xie et al. (2021)](/sources/xie-2021.md), §6.1, Fig. 14).
* **A single shock speed is not enough.** Kitamura & Shima keep the
  grid but vary the shock Mach number $M_s \in \{1.5, 3, 6, 10\}$ and the
  propagation Mach number $M_{\mathrm{prop}} \in \{0, 0.5, 1, 1.5, 3, 6, 10\}$.
  Quirk's test is the point $(6, 6)$ and the stationary shock is
  $M_{\mathrm{prop}} = 0$. They use eight first-order fluxes, 400 steps
  and CFL 0.4.
  * Roe with an entropy fix forms carbuncles for every $M_{\mathrm{prop}}$
    at $M_s = 10$, and for $M_{\mathrm{prop}} \le 6$ at $M_s = 6$. It
    stays stable at $M_s = 1.5$.
  * AUSM+-up, SLAU and van Leer look stable at $M_s = 6$ but not at
    other points of the map.
  * Slowly moving shocks, $0 < M_{\mathrm{prop}} < 0.44\,M_s$, are the
    most severe ([Kitamura & Shima (2019)](/sources/kitamura-2019.md), §§IV.A–IV.B,
    Figs. 9, 12; [slowly moving shock anomaly](/definitions/slowly-moving-shock-anomaly.md)).
* **Perturbation size.** With $\epsilon_{\mathrm g} = 10^{-6}$ or $0$,
  Roe becomes unstable only for the stationary shocks at $M_s = 6$ and
  $10$. Elsewhere the transverse velocity stays below $10^{-12}$ but
  grows, a "potential carbuncle at a very later stage". Quirk's
  $10^{-3}$ is "a good value to check the occurrence of shock anomalies
  in a realistic time" ([Kitamura & Shima (2019)](/sources/kitamura-2019.md), §IV.C).

Every source runs it at first order, except Xie et al., who use a
second-order Runge–Kutta step and do not state the spatial order. See
[numerical shock instability](/definitions/numerical-shock-instability.md).

**Later uses (batch 11).** Deng, Boivin & Xiao name a test the "odd–even
perturbation problem" and attribute it to Quirk
([Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md), §III F). Its
set-up is different from Quirk's: a stationary Mach 20 shock on
$51\times26$ cells whose intermediate column has a density alternating
from row to row, not a moving Mach 6 shock in a duct with a perturbed
centreline. It is recorded on the
[stationary normal shock](/benchmarks/stationary-normal-shock.md) page;
the attribution is recorded here as printed. Their result (odd–even
decoupling with HLLC, none with HLL and HLL-BVD) bears on the same
instability but is not a run of this test.

# Citations

1. [Simon & Mandal (2019)](/sources/simon-2019.md), §9.2.
2. [Simon & Mandal (2019b)](/sources/simon-2019-b.md), §7.1.
3. [Xie et al. (2021)](/sources/xie-2021.md), §6.1.
4. [Kitamura & Shima (2019)](/sources/kitamura-2019.md), §§III–IV.
5. [Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md), §III F.
