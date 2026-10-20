---
type: Benchmark
title: "Van der Pol oscillator"
description: "The relaxation oscillator y1' = y2, y2' = mu (1 - y1^2) y2 - y1, from non-stiff to very stiff as mu grows; the sources use it to test step-size controllers, including adaptive SDC, to compare additive polynomial and IMEX methods across stiffness, and to show that weak stage order and deferred correction lose their design orders on it."
status: established
aliases: [Van der Pol equation, van der Pol problem, VDPOL]
tags: [stiff, verification, order-reduction, step-size-control]
timestamp: 2026-10-20T16:00:00Z
---

# Van der Pol oscillator

The **Van der Pol oscillator** is the two-component system

$$y_1'=y_2,\qquad y_2'=\mu\,(1-y_1^2)\,y_2-y_1,$$

with the parameter $\mu>0$ (page-local). The nonlinear damping
$-\mu(y_1^2-1)y_2$ is negative for $\lvert y_1\rvert<1$ and positive outside, so
every solution approaches a limit cycle. For large $\mu$ the cycle alternates slow
phases, where the problem is stiff, with fast transitions, so a single run mixes
regimes where accuracy and stability limit the step. It is a standard stiff nonlinear
test that lies outside the linear theory behind most remedies for
[order reduction](/definitions/order-reduction.md).

## Parameter sets in the sources

| source | $\mu$ | $y(0)$ | $t$ | use |
|---|---|---|---|---|
| [Koyaguerebo-Imé & Bourgault (2022)](/sources/koyaguerebo-2022.md), §6.6, Eq. (6.6) | 1000 | $(2,0)$ | $[0,3000]$ | fixed-step convergence of deferred correction against BDF and Scilab solvers |
| [Biswas et al. (2023)](/sources/biswas-2023.md), §7.3 | 500 | $(2,0)$ | $[0,10]$ | fixed-step convergence of DIRK methods with high weak stage order |
| [Fekete et al. (2022)](/sources/fekete-2022.md), §3.1.1, Eq. (24) | 10 | $(2,-0.6654321)$ | $[0,2]$ | adaptive step-size controllers with explicit SSP pairs |
| [Saupe et al. (2025)](/sources/saupe-2025.md), §3.1, Eqs. (19)–(20) | 1000 | $(1.1,0)$ | $[0,20]$ (one fast transition) | adaptive and parallel SDC against fixed steps and ESDIRK5(3) |
| [Buvoli & Southworth (2023)](/sources/buvoli-2023.md), §6.2, Eq. (6.1) | $\varepsilon\in[10^{-8},1]$ (singularly perturbed form, below) | $y_1(0)=2$, $y_2(0)$ on the slow manifold | $[0,0.5]$ | order and stability of additive polynomial (FIMEX) methods against IMEX Runge–Kutta |

Buvoli & Southworth (2023) take the singularly perturbed form
$y_2'=\big((1-y_1^2)y_2-y_1\big)/\varepsilon$, citing Hairer and Wanner, with
$y_2(0)=-\tfrac23+\tfrac{10}{81}\varepsilon-\tfrac{292}{2187}\varepsilon^2-\tfrac{1814}{19683}\varepsilon^3$,
which starts the solution near the slow manifold. It is the form above with
$\varepsilon=1/\mu^2$ after the change of variables $t\mapsto t/\mu$, $y_2\mapsto\mu y_2$
*(compiler check, not in the source)*.
Fekete et al. write the second equation as $y_2'=\varepsilon^{-1}(1-y_1^2)y_2-y_1$
with $\varepsilon=0.1$, i.e. $\mu=1/\varepsilon=10$, after Iserles. Koyaguerebo-Imé &
Bourgault note that the problem was proposed with $\mu=5$ on $[0,1]$ by
Enright–Hull–Lindberg and that their stiff version follows a suggestion of
Shampine; along their solution $y_1\in[-2,2.000073]$, $y_2\in[-1323.04,1231.35]$, and
the Jacobian eigenvalues lie in $[-3000.29,1123.17]\times[-1158.48,1158.48]$ of the
complex plane (§6.6).

## Results

**Weak stage order does not help.** Biswas et al. (2023, §7.3, Fig. 12) apply their
L-stable DIRK-(7,4,4) and DIRK-(12,5,5), with weak stage order 4 and 5, and
reference schemes with weak stage order 1, at steps from $0.5$ to about
$2.44\times10^{-4}$, solving the stages by Newton to machine precision against an RK4
reference with $h=10^{-6}$. High weak stage order "does not suffice to remove order
reduction" in the stiff regime $10^{-2}<h<10^{-1}$. They present the problem as the
counterexample that limits their remedy to linear problems; see
[DIRK methods with high weak stage order](/methods/dirk-high-weak-stage-order.md) and
[weak stage order](/definitions/weak-stage-order.md).

**Deferred correction: low levels fail, high levels recover.** Koyaguerebo-Imé &
Bourgault (2022, Table 6.6) run their [deferred-correction](/methods/deferred-correction.md)
schemes DC2–DC10 with steps $3.75\times10^{-5}$ to $1.875\times10^{-6}$ against a DC8
reference at $h=1.875\times10^{-6}$:

- DC2 and DC4 show order 0 (errors of order 1 in $y_1$ and $10^3$ in $y_2$) down to
  $h=7.5\times10^{-6}$ and remain inaccurate at $1.875\times10^{-6}$;
- DC6 and DC8 reach orders of about 6 to 7.6 (DC6 at $h=1.875\times10^{-6}$:
  $2.5\times10^{-7}$ in $y_1$);
- DC10 is accurate (about $3\times10^{-7}$ in $y_1$ at the finest step) but its
  order "is not observed".

Scilab's adaptive BDF solver reaches $2.16\times10^{-6}$ in $y_1$; its adaptive RKF45
$3.54\times10^{-2}$. The authors read the table as evidence that the correction
strategy works even though DC2 and DC4 "would require much smaller time steps".

**Step-size control.** Fekete et al. (2022, §3.1.1, Fig. 9) compare I, PI, PID and
Gustafsson controllers on the mildly stiff case with an SSP(2,2) pair at tolerance
$10^{-4}$: the PID controller takes 753 steps with 17 rejections against 1982 steps
with 495 rejections for the I controller. The table is on
[step-size control](/methods/step-size-control.md).

**Adaptive SDC.** Saupe et al. (2025) solve one fast transition with spectral deferred correction,
Newton for the implicit sweeps and a reference from scipy's Dormand–Prince 5(4) at tolerances
near machine precision. With a maximal local error of about $10^{-5}$ during the transition, fixed
step sizes need about 70 times the Newton iterations of their two step-size-adaptive strategies
(§4.1, Fig. 6); smaller $\mu$ gave similar but weaker trends (not shown). Pipelined block
Gauss–Seidel SDC on four processes gave a "good speedup" in measured wall time, with no number
printed, and at least one parallel adaptive SDC
variant beat the embedded pair ESDIRK5(3) in wall time (§4.1–4.2, Figs. 9–10). See
[step-size control](/methods/step-size-control.md) and [diagonal SDC](/methods/parallel-sdc.md).

**Additive polynomial methods across the stiffness range.** Buvoli & Southworth (2023, §6.2,
Figs. 6, SM2–SM4) split the problem in two ways: semi-implicit (first component explicit,
second implicit) and linearly implicit ($J_ny$ implicit, $f(y)-J_ny$ explicit, with the exact
Jacobian). With 30 logarithmically spaced steps $h\in[10^{-4},0.25]$, Newton to $10^{-12}$ and
an ode15s reference, their FIMEX-Radau and FIMEX-Radau* methods (Radau IIA implicit part,
explicit part extrapolated from the previous step; $q=3,4,5$ nodes and $\kappa=0,1,2$
order-raising iterations) are stable over the whole step range with both splittings, while
every IMEX Runge–Kutta method they tested needed substantially smaller steps to be stable with
the linearly implicit splitting. For small $\varepsilon$ each iteration raises the observed
order by about one; with the semi-implicit splitting the $\kappa=2$ methods show markedly
reduced rates for $\varepsilon\in[10^{-4},10^{-2}]$ while staying the most accurate, and the
fitted rates fall below nominal because of mild order reduction at $h\ge0.1$, where fewer than
five steps are taken. FIMEX-Radau*(5,0) with the linearly implicit splitting is stable but does
not converge at large steps; one iteration fixes it. See
[polynomial time integrators](/methods/polynomial-time-integrators.md),
[IMEX Runge–Kutta](/methods/imex-runge-kutta.md) and
[order reduction](/definitions/order-reduction.md).

## Qualifications

- The two fixed-step studies disagree in emphasis, not in fact: both find that
  remedies proved for linear problems or for one-sided Lipschitz problems do not
  deliver their design order at practical steps on this problem. One reason is
  visible in the eigenvalue range reported by Koyaguerebo-Imé & Bourgault: Jacobian
  eigenvalues with real part up to $1123$ mean a large positive one-sided Lipschitz
  constant during the fast transitions, where the stiffness-independent bounds of
  [B-convergence](/definitions/b-convergence.md) give no useful step range
  *(compiler check, not in the sources)*.
- Buvoli & Southworth (2023) conclude that high-degree polynomials "trivially" give high stage
  order and prevent order reduction on stiff problems (§7); their own Van der Pol rates are
  reduced for intermediate $\varepsilon$ with the semi-implicit splitting, so the observation
  joins the two fixed-step studies above rather than contradicting them. They were read as
  arXiv v2 with the SIAM supplement.
- Biswas et al. (2023) state the stiff regime from Fig. 12 only; no error table is
  given.
- Saupe et al. (2025) give mutually inconsistent time references: the Fig. 2 caption says only
  the shaded transition "at $t\approx800$" is solved, while §3.1 and Fig. 6 solve $t\in[0,20]$ from
  $y_1(0)=1.1$, and the Fig. 6 caption puts the next transition "at around $t=600$", where Fig. 2
  shows transitions near 800 and 1600 (recorded on the Source page).

# Citations

- [Koyaguerebo-Imé & Bourgault (2022)](/sources/koyaguerebo-2022.md) — §6.6 (Eq. (6.6), Table 6.6); §6.7.
- [Biswas et al. (2023)](/sources/biswas-2023.md) — §7.3 (Fig. 12); §8.
- [Fekete et al. (2022)](/sources/fekete-2022.md) — §3.1.1 (Eq. (24), Fig. 9).
- [Saupe et al. (2025)](/sources/saupe-2025.md) — arXiv v2: §3.1 (Eqs. (19)–(20), Fig. 2), §4.1 (Figs. 6, 9), §4.2 (Fig. 10).
- [Buvoli & Southworth (2023)](/sources/buvoli-2023.md) — §6.2 (Eq. (6.1), Fig. 6), §7; Supplement Figs. SM2–SM4.
