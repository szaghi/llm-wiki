---
type: Method
title: "ADER as a time integrator"
description: "Modern ADER read as an ODE integrator: a Galerkin-in-time predictor on one step, a fixed-point problem with a time iteration matrix, solved by K Picard iterations of order min(M+1, K) or to convergence, when the Gauss–Legendre variant is a fully implicit Runge–Kutta method of nodal order 2M+1; it differs from historical Taylor–Cauchy–Kovalevskaya ADER."
status: established
aliases: [ADER, modern ADER, ADER predictor, local space–time Galerkin predictor, space–time DG predictor, IMADER, implicit ADER, locally implicit ADER-DG, ADER-DG with local DG predictor, ADER-DG ODE solver]
tags: [ader, deferred-correction, explicit, implicit, stiff]
timestamp: 2026-10-20T16:00:00Z
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
  [Lax–Wendroff flux reconstruction](/methods/lax-wendroff-flux-reconstruction.md) keeps
  this Taylor route for flux reconstruction and replaces the exact flux derivatives by
  Jacobian-free finite differences in time; [Babbar et al. (2022)](/sources/babbar-2022.md)
  (§1) and [Babbar & Chandrashekar (2025)](/sources/babbar-2025.md) (§1) cite ADER as the
  other route to single-stage high-order schemes, and
  [Chouchoulis et al. (2022)](/sources/chouchoulis-2022.md) (§1) as the main family of
  high-order Lax–Wendroff-type methods.
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
(Remark 4.8). Popov (2024) takes the reading literally and runs implicit ADER-DG on ODEs
(below). [Micalizzi & Torlo (2024)](/sources/micalizzi-2024.md) (Conclusions) plan to carry
the subnode interpolation of their efficient [DeC](/methods/deferred-correction.md) over to
ADER, which the equivalence makes natural.

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

The entries check by hand *(compiler check, not in the source)*.

## Implicit ADER-DG as a stand-alone ODE solver

[Popov (2024)](/sources/popov-2024.md) (§1.1, Eqs. (1)–(13)) takes the ADER-DG scheme with
a local DG predictor out of its PDE setting and uses it as a one-step solver for
$y'=f(t,y)$. The predictor is the upwind-in-time Galerkin problem above, with the degree-$\mathsf M$
nodal Lagrange basis on the $\mathsf M+1$ Gauss–Legendre nodes $c_m$ of $[0,1]$ (the
source's degree $N$ is $\mathsf M$) and a nodal (collocated) representation of $f$, which
makes the time mass matrix diagonal with the Gauss weights $w_m$ and removes all
integrals of $f$. The predictor becomes

$$Y_m-h\sum_{r=0}^{\mathsf M}B_{mr}\,f(t_{n,r},Y_r)=y_n,\qquad B=\mathcal D^{-1}\operatorname{diag}(w),\qquad m=0,\dots,\mathsf M,$$

using $\mathcal D^{-1}\big(\ell_m(0)\big)_m=\mathbf 1$ (Eqs. (9)–(12); the source writes
$K$ for $\mathcal D$ and $M$ for the mass matrix). It is solved to convergence by Picard
or Newton iteration, and the step ends with the Gauss quadrature
$y_{n+1}=y_n+h\sum_mw_mf(t_{n,m},Y_m)$ (Eq. (13)). This is the Galerkin system of Han
Veiga et al. with quadrature on the interpolation nodes, multiplied by $\mathcal D^{-1}$
*(compiler check, not in the sources)*. At the converged predictor Popov's quadrature update and the
extrapolation $\sum_m\ell_m(1)Y_m$ of Han Veiga et al. give the same $y_{n+1}$: summing
the rows of $\mathcal D\mathbf Y=\mathbf r(\mathbf Y)$ and using $\sum_m\ell_m\equiv1$ gives
$\sum_l\ell_l(1)Y_l=y_n+h\sum_lw_lf(Y_l)$ *(compiler check, not in the sources)*; after finitely many Picard
iterations the two differ.

The scheme is therefore an $(\mathsf M+1)$-stage
[fully implicit Runge–Kutta method](/methods/fully-implicit-runge-kutta.md) with $A=B$,
$b=w$ and Gauss–Legendre abscissae, a reading Popov uses for the stability function (§1.2,
Eq. (15)). Its row sums satisfy $B\mathbf 1=c$ *(compiler check, numerical, for
$1\le\mathsf M\le12$)*. Further properties (Popov 2024):

- **Two outputs.** The nodal values $y_n$ and a piecewise polynomial "local solution",
  discontinuous at the nodes, which Popov presents as a finite-element representation, not
  a reconstruction (§1.3, Eq. (16)); see [dense output](/methods/dense-output.md). On the
  harmonic oscillator with 96 steps over $[0,100\pi]$ (more than half a period per step)
  in double precision, degree 8 already reaches round-off at the nodes (Fig. 3).
- **Orders.** Expected orders $2\mathsf M+1$ at the nodes and $\mathsf M+1$ for the local
  solution, by analogy with Baccouch's proofs for modal DG (Eq. (20), stated). On six
  non-stiff problems in 500-digit arithmetic the fitted orders match up to $\mathsf M=60$
  (121.01 at the nodes, 61.00 locally, on the oscillator; Tables 1–6), with excursions
  above and below on nonlinear problems.
- **Stiffness.** On the flame problem $y'=y^2-y^3$, $y(0)=\delta$, Newton iteration is
  needed because Picard diverges at large steps; the front is resolved at $\delta=10^{-4}$,
  degree 1 misplaces it at $\delta=10^{-5}$, and the fitted orders saturate near 8
  ($\delta=10^{-4}$) and 4 ($\delta=10^{-5}$) for every degree $\ge3$ (§2.2, Table 7).
- **Cost.** In mpmath Python the solver is slower than scipy's RK23, RK45, DOP853 and
  Radau IIA at comparable order, but from degree 30–35 on it reaches errors that the
  classical methods do not reach on coarse grids (§2.3, Fig. 12; no hardware stated).

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
- **Implicit ADER-DG: A- and L-stability.** For the converged Gauss–Legendre predictor,
  Popov (2024, §1.2, Eq. (15), Figs. 1–2) writes
  $R(z)=\det(I-zB+z\mathbf 1w^\top)/\det(I-zB)$ and concludes A-stability from plotted
  regions of absolute stability for $1\le\mathsf M\le60$, whose complements are bounded
  islands in $\operatorname{Re}z>0$. He concludes L-stability ("more precisely
  L1-stable", meaning $\lvert R(z)\rvert\sim\lvert z\rvert^{-1}$) from a rank computation
  for $\mathsf M\le80$: $\operatorname{rank}(B-\mathbf 1w^\top)=\mathsf M$ and
  $\operatorname{rank}B=\mathsf M+1$, so the numerator has degree $\mathsf M$ and the
  denominator $\mathsf M+1$. Both properties are inferred from plots and rank checks for
  finitely many degrees, not proved. *Compiler check (not in the source):* evaluating this
  $R$ at complex test points in 60-digit arithmetic for $0\le\mathsf M\le12$ reproduces the
  $(\mathsf M,\mathsf M+1)$ subdiagonal Padé approximant of $e^z$ to round-off; that
  approximant is the stability function of the $(\mathsf M+1)$-stage Radau IIA method, as
  [Jin et al. (2025)](/sources/jin-2025.md) (Table 4.1) classify the three-stage case. The first-subdiagonal Padé
  approximants are A-stable, as recalled by [Sun et al. (2022)](/sources/sun-2022.md)
  (§1), and the degree gap gives $R(\infty)=0$, so the identification, if it holds for all
  $\mathsf M$, would make the scheme A- and L-stable at every degree and account for the
  nodal order $2\mathsf M+1$ (the Padé order). The check is numerical and finite; it is
  not a proof.
- **Mild instability at high degree.** Babbar et al. (2022, §8.1.1) observe a mild linear
  instability of Lax–Wendroff and SSP Runge–Kutta flux reconstruction at degree 4 with
  periodic data and state that it "seems to be present" in ADER-DG too; this is not shown.
  Their Radau-corrected LWFR has the same Fourier CFL numbers as ADER-DG (§6, stated).
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
- **Printed slips in Gaburro et al.** (arXiv v1 read; compiler checks of the PDF):
  Table 2 prints $\Delta x=3.43\times10^{-3}$ for $3.43\times10^{-2}$ and an
  error $8.09\times10^{-5}$ where the printed order implies $8.09\times10^{-6}$;
  Eq. (36) omits the factor $\gamma_nh$; the symbol $\gamma$ also denotes the
  adiabatic exponent.
- **Printed slip in Wolf et al. (2022).** The Taylor predictor (Eq. (5)) is printed with
  the sum starting at $j=1$, which drops the zeroth-order term $q(t_i)$.
- **Popov's cost count.** Popov (2024, §2.3) counts "at least $(\mathsf M+1)^2$" evaluations
  of $f$ per Picard iteration and $(\mathsf M+1)^2$ Jacobians per Newton iteration, against
  $s$ for an $s$-stage implicit Runge–Kutta method, and concludes that ADER-DG costs more
  than implicit Runge–Kutta methods. The printed predictor system evaluates $f$ only at the
  $\mathsf M+1$ nodes, so one sweep needs $\mathsf M+1$ evaluations and one Newton step
  $\mathsf M+1$ Jacobians, the implicit Runge–Kutta count with $s=\mathsf M+1$
  *(compiler check of Eq. (11), not in the source)*. The count appears off by a factor
  $\mathsf M+1$, and the scheme is itself an implicit Runge–Kutta method; the defensible cost
  differences are the full stage coupling and iteration to convergence *(compiler remark, not in the sources)*.
- **Popov's labels and fits.** "L1-stable" is not a standard class; read it as L-stable
  with $R(z)=\mathcal O(\lvert z\rvert^{-1})$ (see [A-stability](/properties/a-stability.md)).
  Fitted nodal orders above $2\mathsf M+1$ by up to 3–4 for $\mathsf M\ge25$ on two
  nonlinear problems, which Popov calls "unexpected", come from six-grid fits at errors of
  $10^{-100}$–$10^{-280}$ and are not evidence of superconvergence beyond $2\mathsf M+1$
  *(compiler remark, not in the sources)*. On the flame problem the orders saturate at a common value for all
  degrees, which points to a measurement dominated by the resolution of the layer *(compiler
  remark)*; Popov's statement of agreement "up
  to $N\le3$" does not hold at $N=2$ (7.99 against an expected 5). The abstract's "uniform
  steps" means one formula per step: variable steps are allowed and graded grids are used,
  but there is no step-size control.
- **Printed slips in Popov (2024)** (arXiv v1). Eq. (15) prints
  $R(z)=1+w^\top(I-zB)^{-1}\mathbf 1$ without the factor $z$ in front of $w^\top$; the
  determinant form beside it is correct. Further slips in test-problem data (initial values
  at $t=0$ for a problem on $[1,2]$, a step formula copied from the $2\pi$-periodic cases,
  $(1-t^2)$ for $(1-t)$ in one exact derivative) are recorded on the Source page.
- **Scaling convention.** In the ADER spectral-difference variant (eq. (65)) the iteration
  matrix carries an $h$ that the unit-interval form above does not. The time basis is
  defined there on the physical interval. This is a change of convention between §2 and
  §4.5.3, not a different method.

# Citations

- [Han Veiga et al. (2021)](/sources/hanveiga-2021.md) — §2 (eqs. (2)–(13), Example 2.1); §2.1 (historical ADER, eqs. (15)–(17)); §4.1 and §4.3 (Thm. 4.5, Remark 4.6); §4.4 (eqs. (43)–(47)); §4.5.2 (Remarks 4.7–4.8); §4.5.3; §5.1–5.3 (Figs. 2–14); §6.
- [Gaburro et al. (2023)](/sources/gaburro-2023.md) — §3 (Eqs. (6)–(14), Remark 3.1), §4.1 (Eqs. (15)–(22)), §4.2 (Eqs. (29)–(37), Example 4.5), §5 (Tables 1–4, Figs. 1–17), §6.
- [Wolf et al. (2022)](/sources/wolf-2022.md) — §4.2 (CFL), §4.3 (Eqs. (5)–(8)), §5.2 (Table 2), §6.1 (Fig. 3), §7.3.
- [Popov (2024)](/sources/popov-2024.md) — Introduction; §1.1 (Eqs. (1)–(13)); §1.2 (Eqs. (14)–(15), Figs. 1–2); §1.3 (Eq. (16), Fig. 3); §2.1 (Eq. (20), Tables 1–6); §2.2 (Table 7, Figs. 10–11); §2.3 (Fig. 12).
- [Babbar et al. (2022)](/sources/babbar-2022.md) — §1; §6 (CFL agreement with ADER-DG); §8.1.1 (mild instability).
- [Babbar & Chandrashekar (2025)](/sources/babbar-2025.md) — §1 (ADER as single-stage route).
- [Chouchoulis et al. (2022)](/sources/chouchoulis-2022.md) — §1 (ADER among Lax–Wendroff-type methods).
- [Sun et al. (2022)](/sources/sun-2022.md) — §1 (A-stability of subdiagonal Padé approximants, as recalled).
- [Jin et al. (2025)](/sources/jin-2025.md) — Table 4.1 (Padé classification of Radau IIA).
- [Micalizzi & Torlo (2024)](/sources/micalizzi-2024.md) — Conclusions (interpolation for ADER, planned).
