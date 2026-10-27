---
type: Method
title: "Method of manufactured solutions"
description: "The method of manufactured solutions verifies a flow solver by choosing an analytic solution, adding the residual it leaves in the governing equations as a source term, and measuring the observed order of accuracy; this page gives the manufactured solutions used for Euler, RANS and GPU DG codes and what they verify."
status: established
aliases: [MMS, manufactured solution, manufactured solutions, code verification by manufactured solutions]
tags: [verification, dg, rans, software]
timestamp: 2026-10-26T20:44:00Z
---

# Method of manufactured solutions

The **method of manufactured solutions (MMS)** verifies the implementation
of a discretization: an analytic field is chosen, substituted into the
governing equations, and the residual it leaves is added to the equations as
a source term, so that the chosen field is the exact solution of the forced
problem ([Wang & Roy 2023](/sources/wang-2023.md), §4.1.1, citing Roache
and Oberkampf & Roy). Solving the forced problem on a sequence of
grids and comparing with the exact field gives the discretization error
and its **observed order of accuracy**, to be checked against the design
order: $N+1$ for an element method of polynomial degree $N$ in the solution
variable, as in the sources below. The manufactured field need not be
physical; it must be smooth and exercise every term of the operator under
test. In this bundle MMS appears as the code-verification step of
high-order DG solvers for the Euler, RANS and compressible Navier–Stokes
equations, before the turbulent test cases.

Page-local symbols: $A$, $a$ amplitude and advection speed of a travelling
manufactured wave; $\boldsymbol q_h$ the discrete conserved-variable
vector, $\boldsymbol q^{\mathrm{ex}}$ the exact solution, $I^h$ the projection
on the discrete space, $\boldsymbol e_h$ the discretization error and
$\boldsymbol e_h^{\mathrm{est}}$ its estimate, $\tau_h$ the truncation error
(the source's $\mathbf u_h$, $\tilde{\mathbf u}$, $\varepsilon_h$,
$\bar\varepsilon_h$, $\tau_h$, renamed because $\boldsymbol u$ is the
velocity, the tilde the Favre filter, $\varepsilon$ the dissipation rate and
the overbar the LES filter; $\tau_h$ is not a stress);
$\ell_{\mathrm{HDG}}$ the length scale of the HDG stabilization
$\tau_{\mathrm{HDG}}=Re/\ell_{\mathrm{HDG}}$ (the source's $\ell$ and $\tau$,
renamed because $\tau$ is the SGS stress of the registry).

## Manufactured solutions in the sources

**Sinusoidal Euler solution.** Wang & Roy (2023, §4.1.1, Eqs. 18–21,
Table 2) use the two-dimensional sinusoidal form of Roy et al. for the
steady Euler equations,
$$\begin{aligned}
\rho&=\rho_0+\rho_x\sin(a_{\rho x}\pi x)+\rho_y\cos(a_{\rho y}\pi y),\\
u&=u_0+u_x\sin(a_{ux}\pi x)+u_y\cos(a_{uy}\pi y),\\
v&=v_0+v_x\cos(a_{vx}\pi x)+v_y\sin(a_{vy}\pi y),\\
p&=p_0+p_x\cos(a_{px}\pi x)+p_y\sin(a_{py}\pi y),
\end{aligned}$$
with dimensional coefficients ($\rho_0=1$ kg/m³, $u_0=v_0=200$ m/s,
$p_0=10^5$ Pa, perturbation amplitudes of 5–50% of these, wavenumber
factors $a$ between 0.5 and 2; Table 2) that make the flow mixed subsonic
and supersonic. They also build an exact Euler solution for a
Kármán–Trefftz airfoil from the potential-flow velocity at constant density,
which satisfies continuity and momentum exactly, and add a small source
term to the energy equation, "much in the same way that one creates a
manufactured solution" (§4.2.2). The Ringleb flow, an exact
smooth Euler solution with curved walls, serves the same purpose without a
source term (§4.1.2).

**RANS boundary-layer solution.** [Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md),
§5.1, verify their hybridizable DG solver of the $k$-$\omega$ RANS equations
with the manufactured solution of Eça, Hoekstra & Vaz, which mimics a
turbulent boundary layer and is valid for code verification at $Re=10^6$
to $10^9$, on the rectangle $x\in[0.1,1]$, $y\in[0,0.25]$ with a no-slip
wall at $y=0$ (Dirichlet velocity on the left, Neumann conditions on top and
right, Vinokur stretching in $y$). The mean-flow equations are solved with
the analytical eddy viscosity, and the $k$ and $\omega$ equations
separately (see [Wilcox $k$-$\omega$ model](/methods/k-omega-model.md)).

**Travelling wave for compressible Navier–Stokes.** [Kurz et al. (2025)](/sources/kurz-2025.md),
§5.1, Eq. (24), verify the GPU solver [GALÆXI](/software/galaexi.md) with
$$\rho=2+A\sin\big(2\pi(x+y+z-at)\big),\qquad E=\big(2+A\sin(2\pi(x+y+z-at))\big)^2,$$
and the velocity printed with the same form as $\rho$, $A=0.1$, $a=1$, on
the periodic cube $[-1,1]^3$, with source terms from Gassner et al.
(cited by the source), run to $t=1$ with a time step small enough not to affect
the error.

## What the tests show

| Solver and test | Grids and degrees | Observed result | Source |
|---|---|---|---|
| Modal DG, steady Euler, sinusoidal MMS | primal orders 2, 3, 4 (degrees $N=1$–3); grids from $32\times32$ | primal solutions at design order; error estimates at their expected orders (below) | Wang & Roy (2023), §4.1.1, Figs. 2–6 |
| HDG, RANS MMS at $Re=10^7$, $N=3$ triangles | 10, 13, 21, 28 cells per direction, first-cell $y^+$ 0.77 to 0.18 | velocity error $1.69\times10^{-4}$ to $2.70\times10^{-6}$, rates 4.62, 3.79, 3.82 ($\approx N+1$); pressure rates 2.84, 2.94, 2.97 ($\approx N$); $k$ and $\omega$ equations also optimal | Elzaabalawy et al. (2023), §5.1, Table 1 |
| GALÆXI, DGSEM, travelling wave | $N=2$ to 9, 1 to $64^3$ elements | design order of the density $L_2$ error for standard DG on Gauss nodes and split-form DG on Gauss–Lobatto nodes | Kurz et al. (2025), §5.1, Fig. 9 |

Elzaabalawy et al. (2023, §5.1, Figs. 4–6) also use the manufactured
solution to **calibrate** a free parameter: with
$\tau_{\mathrm{HDG}}=Re/\ell_{\mathrm{HDG}}$, the error is smallest at
$\ell_{\mathrm{HDG}}\approx10^2$ for $Re=10^5$, $10^7$ and $10^9$, which they
take as support for a stabilization proportional to $Re$; the turbulent
cases then use $\tau_{\mathrm{HDG}}=Re/200$ ($Re/100$ in the MMS runs).

## From code verification to error estimation

Manufactured solutions make the exact discretization error available, which
Wang & Roy (2023) use to test **error transport equations** for a modal DG
discretization (see [mesh adaptation](/methods/mesh-adaptation.md), where
error estimates drive adaptation). With $\boldsymbol e_h=\boldsymbol q_h-I^h\boldsymbol q^{\mathrm{ex}}$
the error of the discrete solution against the projected exact one, and
$\tau_h$ the residual of the discrete operator evaluated at the projected
exact solution (the truncation error, Eq. 11), the nonlinear error transport
equation is the discrete equation minus its value at the projected exact
solution, with $-\tau_h$ as source (Eq. 12); linearizing about the discrete
solution gives the linearized version (Eq. 13). Writing their order triplet
in orders of accuracy (the source's $p$ is the order, polynomial degree
$p-1$): for a primal solution of order $N+1$, an error-equation solution of
the same order, and a truncation-error estimate of order $r$ (page-local,
reconstructed from neighbouring elements), the corrected error is
$O(h^{\min(2N+2,r)})$ for the nonlinear equation and the linearization adds
an $O(h^{2N+2})$ term (Eqs. 15–16, derivation cited to Banks et al.; smooth
solution and smoothly varying grid metrics). On the sinusoidal MMS (§4.1.1,
Figs. 3–5) and on Ringleb flow (§4.1.2) the nonlinear equation with the
exact truncation error gives a corrected error at round-off level, the
linearized one shows order $2N+2$, and with an estimated truncation error
both reach order $r$ only after their "iterative correction"; for degree 3
(order 4) they use $r=6$ instead of 8, which is "strongly affected by
round-off". On non-smooth problems (an expansion fan with a corner
singularity, the Kármán–Trefftz airfoil) the primal order falls to one and
the estimated truncation error is the bottleneck (§4.2, §5).

## Qualifications

- *(Compiler check, not in the sources.)* When the error-equation solution
  has the order of the primal solution and the exact truncation error is
  used, the nonlinear error transport equation of Wang & Roy is satisfied
  identically by $\boldsymbol e_h^{\mathrm{est}}=\boldsymbol q_h-I^h\boldsymbol q^{\mathrm{ex}}$, since the
  discrete operator at $\boldsymbol q_h-\boldsymbol e_h^{\mathrm{est}}=I^h\boldsymbol q^{\mathrm{ex}}$
  returns $\tau_h$ by definition; the round-off-level corrected error of
  their Figs. 3–5 is therefore expected by construction, and the paper
  reports it as an observation.
- The manufactured solutions verify the discretization, not the turbulence
  model. Elzaabalawy et al. solve the RANS MMS with a prescribed eddy
  viscosity and the turbulence equations separately; in their turbulent
  channel the rates of all variables stay near $N+1$ from 30 to 150 cells
  across the channel and then degrade because of the wall singularity of
  $\omega$, which makes the global rate "first-order accurate at most", a
  property they recall for second-order finite volumes too (§5.2.1,
  Table 2); an algebraic mixing-length model, without that singularity,
  recovers order $N+1$ (Eqs. 93–94, Fig. 16). The MMS order does not carry
  over to the singular problem.
- Kurz et al. show only the density error, and Wang & Roy state no hardware
  for the costs of their error equations (Table 1).
- Wang & Roy print "discretion error" for discretization error (§3.1) and
  list Oberkampf & Roy's book twice in their references ([17] and [24]).

# Citations

- [Wang & Roy (2023)](/sources/wang-2023.md) — Journal Pre-proof: §3.1, Eqs. (11)–(16) (error transport equations, expected orders); §4.1.1, Eqs. (18)–(21), Table 2, Figs. 2–6 (sinusoidal Euler MMS, round-off and order results); §4.1.2 (Ringleb flow); §4.2, §5 (non-smooth problems, Kármán–Trefftz airfoil with energy source term).
- [Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md) — §5.1, Table 1, Figs. 4–6 (Eça–Hoekstra–Vaz RANS manufactured solution, observed orders, stabilization calibration); §5.2.1, Table 2, Eqs. (93)–(94), Fig. 16 (rates degraded by the $\omega$ wall singularity).
- [Kurz et al. (2025)](/sources/kurz-2025.md) — §5.1, Eq. (24), Fig. 9 (travelling-wave manufactured solution, design order for $N=2$–9).
