---
type: Benchmark
title: "Colliding acoustic pulses"
description: "Klein's low-Mach test of two acoustic pulses that collide on a periodic domain; the sources run it with implicit and IMEX integrators at acoustic Courant numbers above one to check how well large steps resolve acoustics, and find the pulses captured at moderate Courant numbers but damped at very large ones."
status: established
aliases: [Klein's colliding pulses, two colliding acoustic pulses, Klein test I]
tags: [verification, imex, implicit, asymptotic-preserving, stiff]
timestamp: 2026-10-20T06:18:00Z
---

# Colliding acoustic pulses

Klein's colliding-pulse problem (1995, as recalled by both sources) is a
one-dimensional weakly compressible flow of an ideal gas with ratio of specific heats
$\gamma=1.4$ (page-local). On $[-L,L]$ with $L=2/\varepsilon$, periodic, the
data are, in page-local density, velocity and pressure,

$$\begin{aligned}
\rho&=0.955+\tfrac{\varepsilon}2\,2\,\big(1-\cos\tfrac{2\pi x}L\big),\\
u&=-\operatorname{sgn}(x)\,\tfrac12\,2\sqrt\gamma\,\big(1-\cos\tfrac{2\pi x}L\big),\\
p&=1+\tfrac{\varepsilon}2\,2\gamma\,\big(1-\cos\tfrac{2\pi x}L\big),
\end{aligned}$$

with $\varepsilon$ the low-Mach parameter of the scaled Euler equations
([Puppo et al. (2024)](/sources/puppo-2024.md), §4.2.2;
[Orlando & Bonaventura (2025)](/sources/orlando-2025.md), §5.2). The velocity
perturbation launches two pressure pulses that run toward each other, superpose at
the centre and separate again; at $t\approx0.815$ and $1.63$ the profiles are compared.
The acoustic waves are faster than the flow by a factor of order $1/\varepsilon$, so a
step chosen for the material speed has an acoustic Courant number far above one. The
test asks whether the implicit or IMEX treatment of the acoustics still resolves the
pulses at such steps.

## Configurations in the sources

| Source | $\varepsilon$ | Space | Time integrator | Steps |
|---|---|---|---|---|
| Orlando & Bonaventura (2025), §5.2 | $1/11$ | DG, degree 2, 55 elements | third-order Kennedy–Carpenter IMEX, ideal gas and stiffened gas | $h=1.63\times10^{-2}$, $3.26\times10^{-2}$, $8.15\times10^{-2}$ (acoustic Courant number about 0.56, 1.16, 2.9) |
| Puppo et al. (2024), §4.2.2 | $1/11$, $10^{-4}$ | third-order CWENOZ finite volumes, 440 cells | [Quinpi](/methods/quinpi.md) without time limiting, Alexander's SDIRK3 | Courant number 6.78; $h/\Delta x=0.423$ and $5.59\times10^{-4}$ |

## What it shows

* **Acoustics captured at moderate Courant numbers.** The IMEX scheme agrees with an
  SSPRK(3,3) reference (880 elements, acoustic Courant number about 0.14) at all three
  steps; larger steps hit the stability limit of the explicit part (Orlando &
  Bonaventura 2025, §5.2, Figs. 1–2). Puppo et al. (2024, Fig. 7) compare the implicit
  pressure profiles with an explicit CWENOZ run at both $\varepsilon$, graphically only,
  with no error numbers.
* **Damping at very large acoustic Courant numbers.** With a stiffened-gas equation of
  state ($\gamma=4.4$, $\pi_\infty=6.8\times10^3$, page-local) at the same step, the acoustic Courant
  number is about 80: the IMEX scheme stays stable but the pressure pulses are
  "completely damped"; a step 80 times smaller resolves them without oscillations
  (Orlando & Bonaventura 2025, Fig. 4). An L-stable implicit treatment damps waves it
  does not resolve, so this is the expected behaviour *(compiler remark, not in the
  sources)*; see
  [asymptotic-preserving schemes](/definitions/asymptotic-preserving-scheme.md) and
  [IMEX Runge–Kutta](/methods/imex-runge-kutta.md).

## Qualifications

* **Two meanings of $\varepsilon$.** Orlando & Bonaventura call $1/11$ the Mach number $M$;
  Puppo et al. scale the pressure term by $1/\varepsilon^2$ and state
  $\mathrm{Ma}=\varepsilon/\sqrt\gamma$. The initial data agree in both.
* Puppo et al. (2024) do not claim the asymptotic-preserving property for Quinpi; the test
  shows stability and qualitative agreement only (§4.2).
* **Printed step sizes.** The Fig. 7 caption of Puppo et al. (2024) gives implicit and
  explicit steps (4.23 and 0.624 for $\varepsilon=1/11$) that do not match the stated
  $h/\Delta x=0.423$ with $\Delta x=2L/440=0.1$ (which gives $0.0423$); a step of 4.23 would
  exceed both output times *(compiler check, not in the source)*.
* Orlando & Bonaventura's third-order pair is of type II and, by their own §3.1, only
  weakly asymptotic preserving with ill-prepared pressure data such as these; the paper
  does not comment (see [IMEX Runge–Kutta](/methods/imex-runge-kutta.md), Qualifications).

# Citations

- [Puppo et al. (2024)](/sources/puppo-2024.md) — §4.2, §4.2.2, Fig. 7.
- [Orlando & Bonaventura (2025)](/sources/orlando-2025.md) — §3.1, §5.2, Figs. 1–2 and 4.
