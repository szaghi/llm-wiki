---
type: Definition
title: "Method of manufactured solutions"
description: "Code verification by a chosen smooth solution: the equations applied to it give a source term, the source is added to the solver, and the observed error order is compared with the design order; the sources apply it to a full solver on mapped adaptive meshes, to a steady-state shock-capturing solver, to a semi-discrete operator and to a gradient reconstruction."
status: established
aliases: [MMS, manufactured solution, manufactured solutions, order-of-accuracy verification]
tags: [benchmark, finite-volume, finite-difference]
timestamp: 2026-10-23T08:00:00Z
---

# Method of manufactured solutions

The method of manufactured solutions verifies that a code solves its
equations at the order it was designed for. Instead of looking for a
problem with a known exact solution, one chooses a smooth field
$u_{\mathrm m}(x,t)$ (page-local symbol), applies the continuous
operator to it, and adds the residual as a source term, so that
$u_{\mathrm m}$ solves

$$
\partial_tu+\nabla\cdot f(u)=S_{\mathrm m},\qquad
S_{\mathrm m}=\partial_tu_{\mathrm m}+\nabla\cdot f(u_{\mathrm m})
$$

exactly. The modified code is run on a sequence of meshes and the
observed order $\log\big(\lVert e_1\rVert/\lVert e_2\rVert\big)/\log(h_1/h_2)$ of
the error $e=u_h-u_{\mathrm m}$ is compared with the design order. The
chosen field need not be physical, only smooth and exercising every term
of the operator; the method tests the implementation, not the model.
Peng et al. introduce it as a method "used in many published studies to
verify CFD codes and test the accuracy of the scheme", citing two
references, and Chen et al. cite Roache.

## Four uses in the sources

The sources apply the idea at four levels of a solver.

**Whole solver on mapped adaptive meshes.**
[Peng, Atkins & Deiterding (2022)](/sources/peng-2022.md) §3.1 verify
their finite-volume solver on mapped curvilinear meshes with
[block-structured refinement](/methods/adaptive-mesh-refinement.md)
([AMROC](/software/amroc.md)). They replace the chemical source of the
reacting multispecies Euler equations by analytical sources built from
fields of the form

$$
\Psi(x,y)=\Psi_0+\Psi_x\,f_{s,x}(a_{\Psi x}\pi x)+\Psi_y\,f_{s,y}(a_{\Psi y}\pi y)
$$

for $\rho Y_{\mathrm O_2}$, $\rho Y_{\mathrm N_2}$, $v_1$, $v_2$ and $T$,
with $f_s$ sines or cosines and the constants of their Table A
(e.g. $v_1=800+60\sin(1.5\pi x)+30\sin(0.75\pi y)$ m/s,
$T=1000+100\cos(\pi x)+75\cos(0.5\pi y)$ K), a supersonic flow; a
constant ratio of specific heats is assumed to simplify the source
(Eq. 35; page-local symbols, the source's $\phi$ renamed $\Psi$ to keep
$\phi_k$ for volume fractions). The fields are run on stretched, skewed
and distorted mapped meshes with three statically refined levels
(dynamic refinement is switched off so that cells can be compared
with the analytical values, which also exercises the coarse–fine
transfer), base meshes $12^2$ to $96^2$, CFL 0.1, Dirichlet inflow and
extrapolated supersonic outflow, and the $L^2$ errors of $\rho$,
$Y_{\mathrm O_2}$, $\rho v_1$ and $E$ are compared at $t=0.02$ s with a
second-order slope (Figs. 4–5). The authors conclude second order "when
simulating the smoothly varying flow field on a hierarchically refined
mapped mesh"; they print no observed orders, and the conclusion rests on
the decrease of the errors in the figure.

**Steady solver driven to a converged residual.**
[Wan & Xia (2022)](/sources/wan-2022.md) verify their steady-state
[hybrid WENO](/methods/hybrid-weno.md) finite-difference scheme (WENO-H)
on steady Euler equations with a source term, marched in pseudo-time
with SSP-RK3. In 2D (Ex. 4.2) the source is
$(0.4,0.6,0.6,1.8)\cos(x+y)$ for the exact solution
$\rho=1+0.2\sin(x+y)$, $v_1=v_2=1$, $p=1+0.2\sin(x+y)$ on $[0,2\pi]^2$
with exact boundary values, run to $T=120$ on $20^2$ to $70^2$ points;
the $L^1$ error falls from $1.86\times10^{-3}$ to $3.69\times10^{-6}$ at
observed orders 4.94–4.99 (Table 4.1). In 3D (Ex. 4.14) the source is
$(0.6,0.8,0.8,0.8,3)\cos(x+y+z)$ for $\rho=p=1+0.2\sin(x+y+z)$,
$v=(1,1,1)$, CFL 0.6, $T=40$, $20^3$ to $70^3$; the $L^1$ error falls from
$3.90\times10^{-3}$ to $7.06\times10^{-6}$ at orders 5.01–5.07
(Table 4.3). With $\gamma=1.4$ the 2D source is exactly
$\nabla\cdot f(u_{\mathrm m})$ for this field *(compiler check, not in
the sources)*. The errors of WENO-H and of the linear fifth-order
upwind scheme are identical to all printed digits in both tables, so
the hybrid's smoothness detector selects the linear scheme everywhere
and the test verifies the linear scheme and the steady-state marching,
not the nonlinear branch *(compiler check, not in the sources)*.

**Semi-discrete operator only.** [Browne et al. (2022)](/sources/browne-2022.md)
Appendix A verify the right-hand side of their nonlinear disturbance
equations, not a time-marched solution: manufactured baseflow and
disturbance fields of trigonometric form
($4+A_p\sin(\alpha_px)\cos(\alpha_py)\sin(\alpha_pz)$ and alike,
Eq. A.1, page-local amplitudes $A_p$ and wavenumbers $\alpha_p$) are inserted in the discrete operator, and the "exact" flux
derivatives are themselves a sixth-order central difference of the exact
fluxes with a small step (Eq. A.3). On three-dimensional block-structured
meshes with spacings 0.1 to 0.0125, the convective operator (fifth-order
[WENO](/methods/weno-js-reconstruction.md) on Rusanov-split fluxes)
converges at observed $L^2$ orders of about 5.8–6.0, and the convective
plus viscous operator (second-order central viscous terms) at about
1.9–2.0 (Tables A.1–A.2, Fig. A.30), "consistent with" the design
orders.

**A reconstruction alone.** [Chen et al. (2022)](/sources/chen-2022.md)
§6.2 use a manufactured boundary-layer profile
$\varphi=1-\exp\big(-y/\sqrt{c\mu x}\big)$, $c=0.59$, $\mu=10^{-8}$
(page-local symbols; after Sun, Darmofal & Haimes), on
$[0.05,1.05]\times[0,0.001]$ with perturbed triangles of aspect ratio
1000, and evaluate only the $y$-gradient that their
[vertex-based reconstruction](/methods/unstructured-gradient-reconstruction.md)
and its competitors compute from exact cell values, with the boundary
values either unknown or given; no equation is solved (Eq. 31,
Figs. 11–12). Their vertex-based least-squares reconstruction with the
iterative boundary treatment gives the lowest boundary-cell and
boundary-face errors in both cases.

## What the four uses verify

Peng et al. march a solution in time, with boundary conditions
and coarse–fine transfer in the loop, and measure a solution error;
Wan & Xia march to a steady state and measure the converged solution
error.
Browne et al. evaluate the discrete right-hand side once, against
"exact" derivatives that are themselves a sixth-order central difference
of the exact fluxes (Eq. A.3). Chen et al. evaluate a gradient from
exact cell values and solve no equation (§6.2). The four observed
orders therefore refer to an unsteady solution, a steady solution, an
operator and a reconstruction respectively *(compiler check, not in the sources)*.

## Qualifications

- Browne et al.'s convective operator is built from fifth-order WENO
  but converges at about sixth order on their smooth fields; the paper
  calls this consistent with the design and does not discuss the extra
  order. At the two finest meshes the $L^\infty$ order of the continuity
  equation falls to 1.672 and 0.971 while the $L^2$ order stays higher,
  and two entries of Table A.2 are negative on the coarse meshes; these
  are not discussed either.
- Peng et al.'s manufactured fields assume a constant ratio of specific
  heats, while their solver models thermally perfect mixtures; the test
  therefore does not exercise the temperature-dependent closure.
- Chen et al. call their profile a manufactured solution, although no
  source term is added and no equation is solved (§6.2).

# Citations

- [Peng, Atkins & Deiterding (2022)](/sources/peng-2022.md) — §3.1, Eq. (35), Figs. 4–5, Table A (accepted manuscript).
- [Wan & Xia (2022)](/sources/wan-2022.md) — Ex. 4.2, Table 4.1; Ex. 4.14, Table 4.3.
- [Browne et al. (2022)](/sources/browne-2022.md) — Appendix A, Eqs. (A.1)–(A.3), Tables A.1–A.2, Fig. A.30.
- [Chen et al. (2022)](/sources/chen-2022.md) — §6.2, Eq. (31), Figs. 11–12.
