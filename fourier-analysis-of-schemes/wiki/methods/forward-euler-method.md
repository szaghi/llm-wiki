---
type: Method
title: "Forward Euler method"
description: "The one-step recurrence y^{n+1} = y^n + Delta t F(t^n, y^n) from the forward difference; on the decay equation dy/dt = -y it multiplies the solution by G = 1 - Delta t per step, and the source states |G| < 1, i.e. 0 < Delta t < 2, as a necessary condition for non-divergence that does not ensure accuracy, with oscillation for Delta t > 1 and divergence for Delta t > 2."
status: established
aliases: [Euler method, explicit Euler method, Euler forward difference method]
tags: [time-integration, stability, finite-difference]
timestamp: 2026-10-13T00:00:00Z
---

# Forward Euler method

For $\mathrm dy/\mathrm dt = F(t,y)$, replacing the derivative by the forward
difference $D_+$ in time ([one-sided differences](/operators/one-sided-differences.md))
gives
$$y^{n+1} = y^n + \Delta t\,F(t^n, y^n)$$
([Riley et al. (2006)](/sources/riley-2006.md), eqs. 27.62–27.63, 27.72).
The source calls it "the Euler method" (p. 1021). The forward step "would give
exact results if $y$ were a linear function" of $t$ over the step (p. 1025).

## Stability statement on the decay equation

For the [exponential-decay test equation](/benchmarks/exponential-decay-test-equation.md)
$\mathrm dy/\mathrm dt = -y$, $y(0) = 1$, the recurrence is (eq. 27.63)
$$y^{n+1} = (1 - \Delta t)\,y^n,$$
a scalar recurrence $y^{n+1} = G\,y^n$ with $G = 1 - \Delta t$ (the source's
$\lambda$). Printed claims (§27.6.1, p. 1021, table 27.10):

1. "to maintain anything like a reasonable accuracy only very small steps ...
   can be used";
2. for $\Delta t > 1$ "the calculated solution oscillates (when it should be
   monotonic)", and for $\Delta t > 2$ "it diverges";
3. "a necessary condition for non-divergence is" $\lvert G\rvert < 1$, i.e.
   $0 < \Delta t < 2$, "though in no way does this ensure accuracy".

**Scope.** The statement is made for this one linear test equation and this
recurrence. The source gives no general stability theory, no amplification
factor of a mode, and no extension to other $F$. It attributes the
inaccuracy partly to the forward difference, which is "a closer approximation" to the
derivative at $t^n + \Delta t/2$ than at $t^n$ (p. 1021), and its
summary names two difficulties: "(i) insufficiently precise approximations to
the derivatives and (ii) inherent instability due to rounding errors"
(pp. 1022–1023).

## Compiler's notes (hypothesis)

These are the compiler's own readings of the printed material, not claims of
the source.

* **Strict versus non-strict bound.** For $\Delta t = 2$, $G = -1$ and the
  recurrence gives $y^n = (-1)^n$, which neither decays nor diverges. Table
  27.10 prints exactly this column ($\pm1$). Non-divergence therefore needs
  only $\lvert G\rvert \le 1$, i.e. $0 < \Delta t \le 2$. The printed strict
  inequality $\lvert G\rvert < 1$ is the condition for the numerical solution
  to decay, as the exact one does.
* **Table 27.10 rows.** For $\Delta t = 1.5$, $2$ and $3$ the printed entries
  equal $(1-\Delta t)^n$ at $n = 1, 2, \dots, 6$. These are the values after
  $n$ steps, at $t = n\Delta t$, not at the tabulated $t = 0.5n$. For
  $\Delta t \le 0.5$ the rows are at the tabulated $t$.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §27.6.1 (eqs. 27.61–27.63, table 27.10, pp. 1020–1023), §27.6.3 (eq. 27.72, p. 1025).
