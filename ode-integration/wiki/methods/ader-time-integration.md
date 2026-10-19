---
type: Method
title: "ADER as a time integrator"
description: "Modern ADER read as an ODE integrator: a Galerkin-in-time predictor on one step, a fixed-point problem with a time iteration matrix, solved by K Picard iterations of order min(M+1, K); it differs from historical Taylor–Cauchy–Kovalevskaya ADER and has a Newton-type implicit variant for stiff sources."
status: established
aliases: [ADER, modern ADER, ADER predictor, local space–time Galerkin predictor, space–time DG predictor, IMADER, implicit ADER, locally implicit ADER-DG]
tags: [ader, deferred-correction, explicit, implicit, stiff]
timestamp: 2026-10-20T05:00:00Z
---

# ADER as a time integrator

ADER ("arbitrary derivative") schemes reach arbitrary order in one step for hyperbolic
PDEs. Two different constructions carry the name.
[Han Veiga et al. (2021)](/sources/hanveiga-2021.md) (§2) set them apart and analyse the
modern one as a time integrator for the semi-discrete system $y'=f(y)$:

- **Historical ADER** (Titarev & Toro; Toro & Titarev, as recalled in §2.1) Taylor-expands
  the interface state in time and replaces the time derivatives by space derivatives
  (Cauchy–Kovalevskaya). It obtains the space derivatives from linearized generalized
  Riemann problems, then integrates the flux in time by Gauss quadrature (eqs. (15)–(17)).
  This is a space-time-coupled flux construction, not a separable time integrator.
- **Modern ADER** (Dumbser et al.; Zanotti et al.) computes a local, element-wise
  "predictor": a polynomial-in-time solution on $[t_n,t_{n+1}]$ from a Galerkin weak form in
  time, solved by fixed-point iteration. After the method-of-lines reduction this is a
  one-step ODE method. Han Veiga et al. prove it is a
  [deferred-correction](/methods/deferred-correction.md) scheme (see
  [equivalence of DeC and ADER](/results/dec-ader-equivalence.md)).

The bundle treats modern ADER here. Han Veiga et al. justify reading it as a time
integrator by the structure of ADER space–time DG. The space–time matrix factorizes into
a spatial mass matrix and a temporal part, so changing the spatial discretization changes
only the spatial factor: "That is why we can consider ADER to be a time integration method"
(Remark 4.8).

**Page-local notation.** Nodes $c_0,\dots,c_{\mathsf M}$ in $[0,1]$ (equispaced,
Gauss–Lobatto or Gauss–Legendre), subnodes $t_{n,m}=t_n+c_mh$, and Lagrange polynomials
$\ell_m$ (a Lagrange basis, unrelated to the registry's multirate micro-step index $\ell$). The predictor is $y(t_n+\vartheta h)\approx\sum_m\ell_m(\vartheta)Y_m$, with
$\mathbf Y=(Y_0,\dots,Y_{\mathsf M})$. The quadrature is
$\{\vartheta_z,w_z\}_{z=0}^{Z}$ on $[0,1]$. $\mathcal D$ is the ADER time iteration
matrix (the source's "mass matrix" $\underline{\underline M}$, renamed because $M$ is
the bundle's mass matrix). $\mathbf r$ is the right-hand-side functional. The source
writes $\partial_t\alpha+F(\alpha)=0$, translated with $f=-F$.

## The predictor as a fixed-point problem

Test the ODE against each basis function $\ell_m$ on the step and integrate by parts in
time, so that the initial value $y_n$ enters weakly ("upwind in time"). With quadrature
this gives (Han Veiga et al. 2021, eqs. (7)–(12); signs translated)

$$\begin{aligned}
\mathcal D_{ml}&=\ell_m(1)\,\ell_l(1)-\sum_{z=0}^{Z}w_z\,\ell_m'(\vartheta_z)\,\ell_l(\vartheta_z),\\
\mathbf r(\mathbf Y)_m&=\ell_m(0)\,y_n+h\sum_{z=0}^{Z}w_z\,\ell_m(\vartheta_z)\,f\Big(\sum_{l}\ell_l(\vartheta_z)Y_l\Big),\\
\mathcal D\,\mathbf Y&=\mathbf r(\mathbf Y).
\end{aligned}$$

$\mathcal D$ does not depend on $h$ on the unit interval. The system is solved by Picard
iteration (eq. (13)):

$$\mathbf Y^{(0)}=(y_n,\dots,y_n),\qquad \mathbf Y^{(k)}=\mathcal D^{-1}\,\mathbf r\big(\mathbf Y^{(k-1)}\big),\quad k=1,\dots,K,$$

and the step ends with $y_{n+1}=\sum_m\ell_m(1)Y_m^{(K)}$. For PDEs, the alternative is a
final flux-integral update $u_{n+1}=u_n-h\,\partial_x\int f$ evaluated with the predictor.
For Burgers this was "more stable", with no difference for linear advection (§5.3.1).
Han Veiga et al. call the converged problem "nothing more than a classical collocation
method … or a high order implicit RK method". After $K$ iterations, ADER with
$\mathsf M+1$ nodes has order $\min(\mathsf M+1,K)$ (Thm. 4.5; proof on the
[equivalence page](/results/dec-ader-equivalence.md)). By Remark 4.6, the matrix
$\mathcal D$ has full rank for equispaced, Gauss–Lobatto and Gauss–Legendre nodes (stated
without proof). Its conditioning is left open.

**Example** (Example 2.1, second order, two Gauss–Legendre nodes
$c_{0,1}=\frac{\sqrt3\mp1}{2\sqrt3}$, $w=(\tfrac12,\tfrac12)$, quadrature on the
interpolation nodes):

$$\mathcal D=\begin{pmatrix}1&\frac{\sqrt3-1}{2}\\-\frac{\sqrt3+1}{2}&1\end{pmatrix},\qquad \mathbf r(\mathbf Y)_m=\ell_m(0)\,y_n+h\,w_m\,f(Y_m).$$

The entries check by hand *(reader and compiler check)*.

## Implicit ADER for stiff sources (IMADER)

For $y'=f^{\mathrm E}(y)+f^{\mathrm I}(y)$ with stiff $f^{\mathrm I}$, the implicit ADER of
Dumbser, Enaux & Toro, recast by Han Veiga et al. (2021, §4.4, eqs. (43)–(47)), adds to the
low-order operator the source Jacobian at $y_n$, weighted by the time basis. This is what a
Newton–Raphson linearization of the predictor gives. The iteration matrix couples
$\mathcal D$ with the Jacobian over all subnodes, so every iteration solves one linear system
of dimension $d$ times the number of nodes (the source prints $(I\times M)\times(I\times M)$,
with $I=d$). The linearly implicit [DeC](/methods/deferred-correction.md) (IMDeC) instead
solves $d\times d$ systems node by node. On the stiff linear system and the Robertson
problem both implicit variants track the reference while explicit ADER fails. IMADER is
visibly more accurate (Figs. 9–10, qualitative). Han Veiga et al. judge IMADER "closer to a
pure implicit scheme than IMDeC" (§4.4).

## ADER-DG as predictor and corrector

In the DG setting used by [Gaburro et al. (2023)](/sources/gaburro-2023.md)
(§3, Eqs. (6)–(14)) the modern scheme has two phases per step:

* a **local predictor** in each space–time cell, a Galerkin problem in a
  modal space–time Taylor basis obtained by integrating by parts in time on the
  cell interior, solved by discrete Picard iteration (Eq. (12); the number of
  iterations is not stated);
* a **global corrector** that updates the DG coefficients with the time
  integrals of the numerical flux and of the volume flux, evaluated on the
  predictor by a time quadrature with nodes $s=0,\dots,S$ and weights
  $\beta_s$ (page-local, summing to one).

Cells exchange data only in the corrector. Gaburro et al. state that ADER-DG
is therefore "not a method-of-lines scheme" and, citing Balsara et al., that
the single communication per step makes it more efficient than RK-DG; the
efficiency is not measured there (§3.1).

**Entropy-preserving ADER-DG.** Gaburro et al. (2023, §4) obtain a provably
entropy-conservative or entropy-dissipative fully discrete ADER-DG scheme,
which they call the first. At each quadrature node they add Abgrall's cell-wise
correction, chosen so that the central part of the flux plus the correction
reproduces the numerical entropy flux of the cell (Eqs. (15)–(22)), and then
apply [relaxation](/methods/relaxation-runge-kutta.md) to the whole step: the
increment is scaled by $\gamma_n$, time advances by $\gamma_nh$, and $\gamma_n$
matches the total entropy to the quadrature of the spatial entropy balance
(Eqs. (29)–(37)); for a quadratic entropy it is explicit (Eq. (42)). Dropping
the upwind terms from the target conserves entropy exactly. On advection,
shallow water and Euler tests with degrees 1–3 the relaxed scheme keeps the
total entropy to $10^{-12}$–$10^{-16}$, while plain ADER-DG dissipates it
(e.g. errors of $10^{-4}$ at degree 1 to $10^{-6}$ at degree 3 on the
travelling bump, Fig. 1), with design orders and, on smooth tests, $\gamma_n$
close to one (up to about 1.2 and 1.35 with a contact discontinuity and the
"123" problem) (Tables 1–4, Figs. 1–17; the Shu vortex is on
[isentropic vortex](/benchmarks/isentropic-vortex.md)). No limiter is used, so
strong shocks are out of scope (§6). See
[entropy stability](/properties/entropy-stability.md).

## Locally implicit predictor for a stiff linear source

For a linear hyperbolic system with a stiff linear source,
$\partial_tq+\sum_j\mathcal A^j\partial_jq=Eq$ (page-local; Biot poroelasticity, where
$E$ is the Darcy friction), [Wolf et al. (2022)](/sources/wolf-2022.md) (§4.3) use the
space–time DG predictor in place of the Cauchy–Kovalevskaya Taylor predictor, which,
they state citing earlier work, "becomes unstable" with a stiff source. The predictor
is the same upwind-in-time Galerkin problem as above, with a Jacobi time basis of the
spatial degree $N$ (page-local) and the source integrated in the space–time weak form
(Eqs. (6)–(8)). Because the source is linear, the predictor is one *linear* system
per element and step, solved directly rather than by Picard iteration. Wolf et al.
call the resulting ADER-DG "locally implicit": the stiff source is integrated
"without a strict time step restriction", while the scheme stays explicit globally,
with no global system, and the step is set by the per-element hyperbolic CFL bound
$h\le\frac{1}{2(2N+1)}\frac{d}{v}$ ($d$ the insphere diameter, $v$ the fastest wave
speed; §4.2, citing earlier work). The stability claim is asserted, not analysed.
The convergence order $N+1$ in space and time is shown for orders 3 to 7 on a 3D
plane wave (§6.1, Fig. 3).

Each element solves a system with $Q\binom{N+3}{3}(N+1)$ unknowns ($Q=13$ fields;
390 at $N=2$, 7,644 at $N=6$, printed $7.64\cdot10^3$). Storing LU factors per element, as in the earlier
approach of de la Puente et al., would take 146 MB per element at $N=5$; the paper's
block back substitution exploits the hierarchical orthogonal basis and the upper
triangular $E$ and cuts the flops by 5.08 to 24.8 times (Table 2). The details are on
[implicit stage solvers](/methods/implicit-stage-solvers.md). Wolf et al. reject the
operator-splitting alternative for this source as not high order; see
[operator splitting](/methods/operator-splitting.md) for the scope of that remark.
The predictor and the clustered
[local time stepping](/methods/local-time-stepping.md) inherited from earlier SeisSol
work together cut the time to solution 6 to 10 times against global time stepping
(§7.3); the LTS algorithm itself is not developed in the paper.

This predictor treats the stiff linear term inside the Galerkin solve, as IMADER does
through its Newton linearization; for a linear source the two coincide in structure,
one linear space–time system per element *(compiler remark, not in the sources)*.

## Stability and accuracy

- **Linear stability.** Han Veiga et al. present the first numerical study of ADER stability
  regions for $y'=\lambda y$ (§5.1, Fig. 2). The regions of explicit ADER coincide with those
  of explicit DeC, do not depend on the node family, and grow with the order. The coincidence
  follows because both are polynomials of degree $K$ in $z=h\lambda$ with order $K$, hence the
  degree-$K$ Taylor polynomial of $e^z$ *(compiler check; see
  [deferred correction](/methods/deferred-correction.md))*. CFL bounds for PDEs depend on the
  spatial discretization and are not derived (§5.1).
- **High-order anomalies.** With equispaced nodes ADER loses its design order at the highest
  orders, presumably because the conditioning of $\mathcal D$ worsens. With Gauss–Legendre
  nodes it shows "strange behavior at high orders and high resolutions", attributed to the
  extrapolation to $t_{n+1}$. Gauss–Lobatto ADER and DeC behave alike. These order losses near
  machine precision remain unexplained (§5.2.1, §6).
- **PDE tests.** With spectral-difference space discretizations, ADER reaches design orders 3
  to 9 on linear advection and Burgers, with no dependence on the node family above round-off
  (§5.3.1).
- **Efficiency claim.** ADER-DG that solves the generalized Riemann problem only in the final
  step keeps the predictor element-local, which eases parallelization. It "can keep up or be
  even more effective than traditional RKDG" (Remark 4.7, citing earlier work, not tested here).

## Qualifications

- **"A-stability".** Han Veiga et al. call the stability-region computation an "A-stability"
  study, but explicit ADER and DeC have bounded regions and are not
  [A-stable](/properties/a-stability.md). The regions are regions of absolute stability. The
  source also prints the region as $\{z:\phi(z)<1\}$, without the modulus.
- **Order of the converged predictor.** The stated order $\mathsf M+1$ is a lower bound.
  The sharp order depends on the nodes. With Gauss–Lobatto or Gauss–Legendre nodes the
  converged collocation problem is of higher order (see
  [deferred correction](/methods/deferred-correction.md), Qualifications) *(compiler note, not in
  the sources)*.
- **Time integrator or not.** Han Veiga et al. read the predictor as a
  one-step method for the semi-discrete system, while Gaburro et al. (2023,
  §3.1) stress that ADER-DG is not a method-of-lines scheme because the
  predictor is element-local and neighbours couple only in the corrector. The
  two are compatible: Han Veiga et al. themselves note the element-local
  predictor (Remark 4.7), and their equivalence results concern the
  predictor iteration, not the inter-element coupling. This is a difference of
  viewpoint, not of claims.
- **Order of relaxed ADER.** Gaburro et al. take existence of $\gamma_n$,
  $\gamma_n=1+O(h^{p-1})$ and order $p$ from Runge–Kutta relaxation theory
  without checking its hypotheses for a predictor–corrector step; for ADER the
  statement is unproved, though the tests show the design orders (e.g. 1.78–1.84
  at second order on one advection test, Table 1).
- **Printed slips in Gaburro et al.** (arXiv v1 read; source's reader checks):
  Table 2 prints $\Delta x=3.43\times10^{-3}$ for $3.43\times10^{-2}$ and an
  error $8.09\times10^{-5}$ where the printed order implies $8.09\times10^{-6}$;
  Eq. (36) omits the factor $\gamma_nh$; the symbol $\gamma$ also denotes the
  adiabatic exponent.
- **Printed slip in Wolf et al. (2022).** The Taylor predictor (Eq. (5)) is printed with
  the sum starting at $j=1$, which drops the zeroth-order term $q(t_i)$.
- **Scaling convention.** In the ADER spectral-difference variant (eq. (65)) the iteration
  matrix carries an $h$ that the unit-interval form above does not. The time basis is
  defined there on the physical interval. This is a change of convention between §2 and
  §4.5.3, not a different method.

# Citations

- [Han Veiga et al. (2021)](/sources/hanveiga-2021.md) — §2 (eqs. (2)–(13), Example 2.1); §2.1 (historical ADER, eqs. (15)–(17)); §4.1 and §4.3 (Thm. 4.5, Remark 4.6); §4.4 (eqs. (43)–(47)); §4.5.2 (Remarks 4.7–4.8); §4.5.3; §5.1–5.3 (Figs. 2–14); §6.
- [Gaburro et al. (2023)](/sources/gaburro-2023.md) — §3 (Eqs. (6)–(14), Remark 3.1), §4.1 (Eqs. (15)–(22)), §4.2 (Eqs. (29)–(37), Example 4.5), §5 (Tables 1–4, Figs. 1–17), §6.
- [Wolf et al. (2022)](/sources/wolf-2022.md) — §4.2 (CFL), §4.3 (Eqs. (5)–(8)), §5.2 (Table 2), §6.1 (Fig. 3), §7.3.
