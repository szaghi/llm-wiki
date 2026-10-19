---
type: Method
title: "Newmark method"
description: "The Newmark family integrates second-order structural dynamics with two parameters; its constant-average-acceleration member is second order, unconditionally stable and free of numerical damping, equals the first Padé scheme, and is the baseline that high-order Padé and Radau IIA integrators are measured against."
status: established
aliases: [Newmark-β, Newmark scheme, constant average acceleration method, average acceleration method, trapezoidal rule (structural dynamics)]
tags: [implicit, stability, verification]
timestamp: 2026-10-20T05:00:00Z
---

# Newmark method

The **Newmark method** advances the second-order semi-discrete equations of structural
dynamics $M\ddot u+C\dot u+Ku=f(t)$ (page-local: $u$ displacement, $C$ damping, $K$
stiffness, $f$ load; $M$ the registry's mass matrix) with displacement, velocity and
acceleration as unknowns and two parameters $\beta_{\mathrm N}$, $\gamma_{\mathrm N}$
(page-local, renamed because $\beta_j$ and $\gamma$ carry registry meanings). In its
standard form, which only Pulicani et al. print, in predictor–corrector form (see below),

$$\begin{aligned}
u_{n+1}&=u_n+h\dot u_n+h^2\big[(\tfrac12-\beta_{\mathrm N})\ddot u_n+\beta_{\mathrm N}\ddot u_{n+1}\big],\\
\dot u_{n+1}&=\dot u_n+h\big[(1-\gamma_{\mathrm N})\ddot u_n+\gamma_{\mathrm N}\ddot u_{n+1}\big],
\end{aligned}$$

with the equation of motion imposed at $t_{n+1}$ *(compiler statement of the standard
form; the other sources print only the member below)*. The member
$\beta_{\mathrm N}=\tfrac14$, $\gamma_{\mathrm N}=\tfrac12$, the **constant average
acceleration** method, is called the "trapezoidal rule" by
[Song & Eisenträger (2022)](/sources/song-2022.md) (§2.4.1), who write it in step-local
time $\theta$ ($t=t_n+\theta h$, primes $=d/d\theta$) as

$$u'_{n+1}=u'_n+\tfrac12u''_n+\tfrac12u''_{n+1},\qquad u_{n+1}=u_n+u'_n+\tfrac14u''_n+\tfrac14u''_{n+1}$$

(Eqs. (62a)–(62b), shifted to $t_n\to t_{n+1}$).

## Stability and damping

[Taddei et al. (2026)](/sources/taddei-2026.md) quote the unconditional-stability
condition $2\beta_{\mathrm N}\ge\gamma_{\mathrm N}\ge\tfrac12$ (§5.2.1). The undamped
choice $\beta_{\mathrm N}=\tfrac14$, $\gamma_{\mathrm N}=\tfrac12$ adds no numerical
dissipation; the damped choice $\beta_{\mathrm N}=\tfrac13$, $\gamma_{\mathrm N}=\tfrac35$
dissipates high frequencies (§5.2.1). They recall that standard Newmark "can be
numerically unstable" for geometrically nonlinear structures, and that dissipative
alternatives (Bossak, generalized-α, ESDIRK) damp spurious high frequencies at the risk
of over-attenuating physically relevant structural dynamics (§1.1, citing the FSI
literature).

## Equivalence with the first Padé scheme

Song & Eisenträger (2022, §2.4.1, Eqs. (58)–(69)) prove that the average-acceleration
method with the load averaged as $\tfrac12(f_n+f_{n+1})$ is algebraically identical to
the $m=1$ member of their [Padé time integration](/methods/pade-time-integration.md),
whose step is

$$(4M+2hC+h^2K)(u'_{n+1}+u'_n)=4h^2\bar f+8Mu'_n-4h^2Ku_n,\qquad u_{n+1}=u_n+\tfrac12(u'_{n+1}+u'_n),$$

with $\bar f$ the step-averaged load (Eqs. (60)–(61)). The proof writes Newmark's
effective equation at both ends of the step, averages them and eliminates the average
acceleration (Eqs. (64)–(69)). Numerically the two give identical errors on a 2D rod and
on Lamb's problem (Figs. 7, 14). Written as a first-order system, the method on a linear
problem is the trapezoidal rule, whose stability function is the $(1,1)$ Padé
approximant, that of the one-stage Gauss method
([fully implicit Runge–Kutta methods](/methods/fully-implicit-runge-kutta.md)), so it
is A-stable and not L-stable *(compiler remark, not in the sources)*.

## As a baseline

**High-order linear dynamics** (Song & Eisenträger 2022, §3). Newmark, HHT-α
($\alpha=-0.05$, the ABAQUS/Standard default), generalized-α ($\rho_\infty=0.8$) and the
two-sub-step Bathe method (trapezoidal then three-point backward Euler, about twice the
cost per step) are all second order. Over 10,000 periods of an undamped oscillator,
second-order methods need $h<T/85$ ($T$ the period, page-local) for 1 % amplitude error,
against $h=T/2$ for the eighth-order Padé scheme; at $h=T/2$ the period elongation is
61.7 % for HHT-α and 30.7 % for Bathe, the best second-order method (Fig. 3). All methods
are very accurate for $h/T<0.01$ (§3.2.3). For 1 % $L_2$ error on a 2D rod Newmark needs
$h=8.4\times10^{-5}$ s, the fourth-, sixth- and eighth-order Padé schemes 17, 49 and 90
times larger steps (§3.3.2); on a 3D mountain model Newmark at the Nyquist step misses
the reference and needs a step 50 times smaller (§3.5).

**Fluid–structure interaction** (Taddei et al. 2026). BDF2 for the incompressible fluid
with Newmark for the structure is common practice and second order overall (§1.1). On the
Turek–Hron FSI3 benchmark the undamped combination ($\beta_{\mathrm N}=\tfrac14$,
$\gamma_{\mathrm N}=\tfrac12$) is unstable, with growing force amplitudes and total
energy; the damped one is stable but its total energy settles lower (about 2.675 against
about 2.69 for two-stage Radau IIA), which the authors read as "IRK schemes are less
dissipative than damped BDF-Newmark methods" (§5.2.1, Figs. 9–11). A reduced-order model
advanced with BDF2–Newmark is unstable "irrespective of numerical (Newmark) damping",
while the same model advanced with Radau IIA stays stable (§5.2.2, Fig. 17). See
[backward differentiation formulas](/methods/backward-differentiation-formula.md) and
[fully implicit Runge–Kutta methods](/methods/fully-implicit-runge-kutta.md).

## In multi-time-step coupling

[Pulicani et al. (2026)](/sources/pulicani-2026.md) (§3.4, Eqs. 22–26) write the undamped
member in predictor–corrector form for $M\ddot u+Ku=f$: predictors
$u^{\mathrm p}_{n+1}=u_n+h\dot u_n+(\tfrac12-\beta_{\mathrm N})h^2\ddot u_n$,
$\dot u^{\mathrm p}_{n+1}=\dot u_n+(1-\gamma_{\mathrm N})h\ddot u_n$, the acceleration from
$(M+\beta_{\mathrm N}h^2K)\ddot u_{n+1}=f_{n+1}-Ku^{\mathrm p}_{n+1}$, and correctors with weights
$\beta_{\mathrm N}h^2$ and $\gamma_{\mathrm N}h$ (page-local superscript p). The effective mass
$M+\beta_{\mathrm N}h^2K$ is constant, so they factor it once. They call the member
"unconditionally stable, second-order accurate, and without numerical dissipation". In their
fluid–structure scheme the structure takes one Newmark step per $m$ explicit fluid steps and a
Lagrange multiplier on the interface velocity couples the two; they recall that energy-method
results of structural dynamics guarantee stability of such multi-time-step schemes, for any
Newmark schemes with their own steps, only when velocity, not displacement, continuity is
imposed (§1). The structure converges at order 2.001 in the coupled piston–rod test (§5.3); see
[local time stepping](/methods/local-time-stepping.md).

## Qualifications

- Taddei et al. print no Newmark or BDF2 formulas; their stability claims rest on two
  test cases. Their Fig. 10 shows the unstable run only on $t\in[43,45]$, where the
  growth they describe is not visible.
- Radau IIA is L-stable and thus itself damps the highest frequencies; the comparison
  with damped Newmark is by total-energy level only.
- The equivalence of Song & Eisenträger holds for linear constant-coefficient problems
  and the step-averaged load.

# Citations

- [Song & Eisenträger (2022)](/sources/song-2022.md) — §1; §2.4.1 Eqs. (58)–(69); §3.1–3.5 Figs. 2–3, 7, 14, 19.
- [Taddei et al. (2026)](/sources/taddei-2026.md) — §1.1; §5.2.1 Figs. 9–11; §5.2.2 Fig. 17.
- [Pulicani et al. (2026)](/sources/pulicani-2026.md) — §1, §3.4 (Eqs. 22–26), §4.4, §5.3 (Fig. 12).
