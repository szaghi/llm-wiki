---
type: Definition
title: "Method of manufactured solutions"
description: "Code verification by a chosen smooth solution whose source term is added to the solver, the observed order being compared with the design order; the sources apply it to a full solver on mapped adaptive meshes, a steady shock-capturing solver, curved-boundary conditions on unfitted meshes, a semi-discrete operator and a gradient reconstruction."
status: established
aliases: [MMS, manufactured solution, manufactured solutions, order-of-accuracy verification]
tags: [benchmark, finite-volume, finite-difference, dg, immersed-boundary]
timestamp: 2026-10-23T23:45:00Z
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

## Five uses in the sources

The sources apply the idea at five levels of a solver.

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

**Boundary treatment on curved, unfitted meshes.**
[Ciallella et al. (2024)](/sources/ciallella-2024.md) §6.1 use the same
steady field as Wan & Xia, $\rho=1+0.2\sin(x+y)$, $v=(1,1)$,
$p=1+0.2\sin(x+y)$, with the same source
$(0.4,0.6,0.6,1.8)\cos(x+y)$ and $\gamma=1.4$, but to measure the
consistency of boundary conditions rather than of the interior scheme. The
exact solution is imposed as Dirichlet data on a curved trefoil-like
boundary $r=1+\frac1{10}\sin(3\theta)$ (Eq. 37), which the mesh does not
fit: either a conformal triangulation with straight boundary edges (levels
0–3, mesh size $h=1.54\times10^{-1}$ to $1.93\times10^{-2}$, page-local, Table 1) or a fully
embedded triangulation of $[-1.5,1.5]^2$ whose surrogate boundary is
detached from the true one ($5\times5$ to $35\times35$, Table 3). Modal
ADER-[DG](/methods/discontinuous-galerkin.md) of degree $N=1$–$3$ with
naive boundary conditions stays at second order for every degree on the
conformal meshes (finest rates 2.00–2.01; $N=3$ density error
$2.6792\times10^{-5}$ at level 3, Table 2). With the constrained
least-squares boundary reconstruction ROD (reconstruction for off-site
data) the same meshes give rates 2.61–2.99 for $N=2$ and 4.10–4.67 for
$N=3$ (finest density error $1.5035\times10^{-10}$, Table 4); its
space–time ADER variant gives nearly the same errors (Table 6). On the
embedded meshes the rates oscillate between levels, which the authors
attribute to how the surrogate boundary cuts the background mesh
(Tables 5, 7). Here the test isolates a boundary closure
([immersed and cut-cell boundaries](/methods/immersed-boundary-method.md)):
the interior scheme is the same in all runs, and only the boundary
treatment changes. Final time, steady-state criterion and CFL number are
not printed.

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

## What the five uses verify

Peng et al. march a solution in time, with boundary conditions
and coarse–fine transfer in the loop, and measure a solution error;
Wan & Xia march to a steady state and measure the converged solution
error. Ciallella et al. hold the interior scheme fixed and vary only
the boundary closure, so their observed order is that of the boundary
treatment on a non-fitted geometry.
Browne et al. evaluate the discrete right-hand side once, against
"exact" derivatives that are themselves a sixth-order central difference
of the exact fluxes (Eq. A.3). Chen et al. evaluate a gradient from
exact cell values and solve no equation (§6.2). The four observed
orders therefore refer to an unsteady solution, a steady solution, a
boundary closure, an operator and a reconstruction respectively *(compiler check, not in the sources)*.

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
- Ciallella et al. write that "in all cases, the expected convergence of
  $M+1$ is achieved" (§6.1; their $M$ is the registry's $N$), while their
  $N=2$ rates on conformal meshes stay below 3 at every level (2.61–2.99
  in Table 4, 2.60–2.97 in Table 6) and the $N=3$ rates exceed 4. The
  order columns of their Table 5 (embedded meshes, ROD-DG) are not
  reproduced from the printed errors and the mesh sizes of Table 3,
  whereas those of Table 7 are (to about $\pm0.03$) *(compiler check, not
  in the sources)*.
- Chen et al. call their profile a manufactured solution, although no
  source term is added and no equation is solved (§6.2).

# Citations

- [Peng, Atkins & Deiterding (2022)](/sources/peng-2022.md) — §3.1, Eq. (35), Figs. 4–5, Table A (accepted manuscript).
- [Wan & Xia (2022)](/sources/wan-2022.md) — Ex. 4.2, Table 4.1; Ex. 4.14, Table 4.3.
- [Ciallella et al. (2024)](/sources/ciallella-2024.md) — §6.1, Eq. (37), Tables 1–7 (arXiv v1).
- [Browne et al. (2022)](/sources/browne-2022.md) — Appendix A, Eqs. (A.1)–(A.3), Tables A.1–A.2, Fig. A.30.
- [Chen et al. (2022)](/sources/chen-2022.md) — §6.2, Eq. (31), Figs. 11–12.
