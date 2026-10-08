---
type: Method
title: "Lax–Wendroff (Taylor) single-step time discretization"
description: "Single-stage, single-step time stepping that expands the solution or the time-averaged flux in a Taylor series and converts time derivatives to space derivatives by the Cauchy–Kowalewski procedure — the alternative to SSP Runge–Kutta for capturing schemes, attractive for AMR and storage."
status: established
aliases: [Lax-Wendroff time discretization, Cauchy-Kowalewski procedure, Taylor method, PIF-WENO, single-step method]
tags: [time-discretization, lax-wendroff, single-step, amr]
timestamp: 2026-10-08T00:00:00Z
---

# Lax–Wendroff (Taylor) single-step time discretization

**Idea.** Instead of the method of lines with
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md), expand in time and use
the PDE (the Cauchy–Kowalewski procedure) to replace each time
derivative by space derivatives, giving a fully discrete one-step
scheme. In the original ENO paper the "solution in the small" is
obtained this way ([Harten et al. (1987)](/sources/harten-1987.md), §4).
Shu notes the approach is compact and one-step but algebraically heavy
in multi-D and hard to analyze ([Shu (1998)](/sources/shu-1998.md), §4.2.3).

**Why single-step.** On AMR grids, multistage Runge–Kutta needs
consistent ghost values at intermediate stages, and simple time
interpolation loses high order. Single-stage single-step methods need
fewer synchronizations and allow local time stepping. The families
named are ADER, Lax–Wendroff FD-WENO, Lax–Wendroff DG and space–time
schemes, and before 2016 only ADER had been applied to MHD
([Christlieb et al. (2016)](/sources/christlieb-2016.md), §1). They save
storage only if the time derivatives are not stored.

**Picard integral formulation (PIF-WENO)** ([Christlieb et al. (2016)](/sources/christlieb-2016.md), §3).
Integrate in time exactly:
$u^{n+1}_i = u^n_i - \frac{\Delta t}{h}\left(\hat{\mathcal{F}}_{i+1/2} - \hat{\mathcal{F}}_{i-1/2}\right)$
(per direction), with $\hat{\mathcal{F}}$ obtained by classical FD-WENO
reconstruction applied to the time-averaged fluxes $\mathcal{F}^n_i$
rather than to the frozen $f(u^n_i)$. $\mathcal{F}^n_i$ is a third-order
Taylor expansion in time with Cauchy–Kowalewski substitution. Expanding
the flux rather than the solution is what admits a
[positivity flux limiter](/methods/positivity-preserving-flux-limiter.md);
one WENO reconstruction per step replaces the three of an RK3 solver.

**Scope of "FD cannot do ADER".** [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §7.4,
state that FD schemes, lacking a volumetric reconstruction, "cannot
indeed draw on ADER approaches", and that ADER gives FV about a factor
of two over SSP-RK. This concerns ADER's space–time predictor; it
does not exclude FD single-step schemes of Lax–Wendroff/Taylor type such
as PIF-WENO, which in Christlieb et al.'s taxonomy are a separate family.

# Citations

1. [Harten et al. (1987)](/sources/harten-1987.md), §4.
2. [Shu (1998)](/sources/shu-1998.md), §4.2.3.
3. [Christlieb et al. (2016)](/sources/christlieb-2016.md), §§1, 3, 4, 7.
4. [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §7.4.
