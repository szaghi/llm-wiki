---
type: Result
title: "Convergence of volume penalization"
description: "Angot, Bruneau and Fabrie's theorems: as the penalization parameter tends to zero the penalized Navier–Stokes solution converges to the no-slip solution in the fluid and to zero in the body, with an error of order η^{1/4} in the fluid and η^{3/4} in the body for the L2 penalization, a sharper estimate for the H1 penalization, and the body force given by the limit of the penalty term."
status: established
aliases: [penalization error estimate, Angot–Bruneau–Fabrie theorem]
tags: [penalization, convergence, error-estimate, fictitious-domain]
timestamp: 2026-11-08T17:31:00Z
---

# Convergence of volume penalization

Setting: 2-D bounded domain $\Omega$ containing regular obstacles
$\Omega_s=\bigcup_i\Omega_s^i$, incompressible Navier–Stokes in
$\Omega_f=\Omega\setminus\overline{\Omega_s}$ with homogeneous Dirichlet data on
$\Gamma$ and a forcing $\mathbf f_0$ supported in $\Omega_f$;
[volume penalization](/methods/volume-penalization.md) with parameter $\eta$
([Angot et al. 1999](/sources/angot-1999.md), §2–§5).

1. **Convergence ($L^2$ penalization, Theorem 4.1).** As $\eta\to0$,
   $\mathbf u_\eta\to\mathbf u$ (weakly, with strong compactness from a
   fractional-time-derivative estimate), where $\mathbf u|_{\Omega_f}$ is the
   unique weak Navier–Stokes solution and $\mathbf u=\mathbf 0$ in $\Omega_s$. The
   proof uses energy estimates and a trace bound of order $\eta^{1/4}$ on each
   $\partial\Omega_s^i$ (Lemma 4.4). **Proved.**
2. **Error estimate ($L^2$, Theorem 4.2).** For a regular fluid solution,
   $\mathbf u_\eta=\mathbf u+\eta^{1/4}\mathbf v_\eta$ with $\mathbf v_\eta$ bounded, and a
   further factor in the body, which the authors summarize as
   $O(\eta^{3/4})$ in $\Omega_s$ and $O(\eta^{1/4})$ in $\Omega_f$ (§6). **Proved.**
3. **Body force (Theorem 4.3).** Under a compatibility condition on the
   initial data, the weak limit of $\eta^{-1}\chi_s\mathbf u_\eta$ is determined
   uniquely, and testing with a function equal to one on $\Omega_s^i$ gives the
   force on obstacle $i$, hence drag and lift as volume integrals of the penalty
   term. **Proved.**
4. **$H^1$ penalization (Theorem 5.1).** With the time derivative and viscous
   term also penalized, $\mathbf u_\eta=\mathbf u+\eta\tilde{\mathbf u}+$ higher order,
   a sharper estimate than (2). **Proved.**

## Numerical observation

For a grid-aligned square cylinder in a channel at $Re=40$ the measured error
behaves as $O(\eta)$ in the body and about $O(\eta)$ in the fluid until the
discretization error dominates, the threshold falling with $h$; the authors
conclude the $\eta^{1/4}$ estimate "might not be optimal" (§6).

## Qualifications

- The fractional exponents of the estimates are partly lost in the text layer
  of the version read; the values above are those the authors state in the
  numerical section ([Angot et al. 1999](/sources/angot-1999.md), Version read).
- The analysis is two-dimensional, where weak Navier–Stokes solutions are
  unique, and with the obstacle motion imposed through the source term.

# Citations

- [Angot et al. (1999)](/sources/angot-1999.md) — §2–§6, Theorems 4.1–4.3, 5.1, Lemma 4.4.
