---
type: Method
title: "Volume penalization (Brinkman penalization)"
description: "Fictitious-domain immersed boundary method that solves the flow equations in the whole domain and models the body as a porous medium of vanishing permeability through a penalty term on its volume; the L2 (Darcy) and H1 (Brinkman) penalizations, their convergence as the penalty parameter vanishes, and force computation from the penalty term."
status: established
aliases: [Brinkman penalization, penalization method, L2 penalization, H1 penalization, porous-medium fictitious domain]
tags: [immersed-boundary, penalization, fictitious-domain, continuous-forcing, incompressible]
timestamp: 2026-11-08T18:08:00Z
---

# Volume penalization (Brinkman penalization)

The incompressible Navier–Stokes equations in $\Omega_f$ with no-slip on
$\Gamma$ are replaced by equations on the whole $\Omega=\Omega_f\cup\Omega_s$ with
a penalty term in the body ([Angot et al. 1999](/sources/angot-1999.md), §3).
Two penalizations are analysed.

**$L^2$ penalization** (a damping term on the velocity):

$$\frac{\partial\mathbf u_\eta}{\partial t}+\mathbf u_\eta\cdot\nabla\mathbf u_\eta-\frac{1}{Re}\Delta\mathbf u_\eta+\nabla p_\eta+\frac{1}{\eta}\chi_s\mathbf u_\eta=\mathbf f_0 .$$

The expansion $\mathbf u_\eta=\mathbf u+\eta\tilde{\mathbf u}$ gives $\mathbf u=\mathbf 0$ in
$\Omega_s$ and the Navier–Stokes solution in $\Omega_f$; in the body
$\tilde{\mathbf u}$ obeys a Darcy law with a Neumann pressure condition, so the
obstacle is a porous medium (Remark 3.1).

**$H^1$ penalization** penalizes the whole linear part, time derivative and
viscous term included,
$(1+\eta^{-1}\chi_s)\partial_t\mathbf u_\eta+\dots-\nabla\cdot\big((1+\eta^{-1}\chi_s)\boldsymbol\Sigma(\mathbf u_\eta,p_\eta)\big)+\eta^{-1}\chi_s\mathbf u_\eta$,
and $\tilde{\mathbf u}$ obeys a Brinkman equation in the body with a
stress-Neumann condition (Remark 3.2).

The idea predates the analysis: Arquis and Caltagirone (1984) penalized the
volume of a porous body in a Brinkman model with variable permeability, and
the point forcing of Peskin and of [Goldstein et al. (1993)](/sources/goldstein-1993.md)
"has to be extended to the volume of the body to give correct physical
solutions at high Reynolds numbers" (Angot et al. 1999, §1, citing Peskin 1982).

## Convergence and forces

[Angot et al. (1999)](/sources/angot-1999.md) prove in 2-D that
$\mathbf u_\eta\to\mathbf u$ as $\eta\to0$, with $\mathbf u|_{\Omega_f}$ the unique weak
Navier–Stokes solution and $\mathbf u=\mathbf 0$ in $\Omega_s$, and give error estimates
of order $\eta^{1/4}$ in the fluid for the $L^2$ penalization and a sharper one
for the $H^1$ penalization ([convergence of volume penalization](/results/convergence-of-volume-penalization.md)).
Under a compatibility condition the weak limit of $\eta^{-1}\chi_s\mathbf u_\eta$
is the force density on the obstacle, so drag and lift follow from
integrating the penalty term over the body volume (Theorem 4.3).

## Practice

On a square cylinder in a channel aligned with a $320\times80$ grid, the
penalized solution with $\eta=10^{-8}$ is indistinguishable from the Dirichlet
reference at $Re=40$ and $Re=80$; a large $\eta$ delays convection and
underestimates the Strouhal number; the pressure is continuous through the
obstacle; and the $H^1$ penalization brings no practical gain because the
discretized penalized viscous term effectively changes the body volume
(Angot et al. 1999, §6). Since $\eta$ can be taken as small as needed, the
penalty error is negligible compared with the discretization error (§7).

## Relation to feedback forcing

[Mittal & Iaccarino (2005)](/sources/mittal-2005.md) note that the Brinkman
force $-(\mu/K)\mathbf u$, with permeability $K$ infinite in the fluid and zero in the
solid (dimensionless, $K\leftrightarrow\eta$ and $\chi_s$ marks where $K$ is small), is feedback forcing with $\alpha_f=0$ and $\beta_f=-\mu/K$, subject to the same
stiffness from the large variation of $K$; in practice $K$ is large but finite in
the fluid, small in the solid and smoothed across $\Gamma$, which leaves an error
in the wall velocity. They contrast it with the fictitious-domain method of
Glowinski et al., which treats the solid as a fluid under a rigidity
constraint.

# Citations

- [Goldstein et al. (1993)](/sources/goldstein-1993.md) — introduction (point forcing that Angot et al. contrast).
- [Angot et al. (1999)](/sources/angot-1999.md) — §1, §3–§7.
- [Mittal & Iaccarino (2005)](/sources/mittal-2005.md) — continuous-forcing section (rigid boundaries).
