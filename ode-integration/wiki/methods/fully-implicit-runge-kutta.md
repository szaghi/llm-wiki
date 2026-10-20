---
type: Method
title: "Fully implicit collocation Runge–Kutta methods (Gauss, Radau IIA, Lobatto IIIC)"
description: "Runge–Kutta methods with a full Butcher matrix built on Gauss, Radau or Lobatto nodes: Gauss of order $2s$, Radau IIA of order $2s-1$ and Lobatto IIIC of order $2s-2$, with high stage order, A-, L-, B-stability and symplecticity as the family allows; the coupled $sd$-dimensional stage system and its preconditioning decide their cost."
status: established
aliases: [IRK, fully implicit Runge–Kutta, Gauss–Legendre, Radau IIA, Lobatto IIIC, Lobatto IIIA, collocation methods, Radau-Right, ADER-DG ODE solver]
tags: [runge-kutta, implicit, stiff, stability, linear-algebra, geometric-integration, parallel]
timestamp: 2026-10-20T10:00:00Z
---

# Fully implicit collocation Runge–Kutta methods (Gauss, Radau IIA, Lobatto IIIC)

A **fully implicit** [Runge–Kutta method](/definitions/runge-kutta-method.md) has a
Butcher matrix $A$ that is not lower triangular, so all $s$ stages are coupled and
each step solves one system of dimension $sd$ for a problem of dimension $d$
([Farrell et al. 2021](/sources/farrell-2021.md), §2.1). The families used in
practice are built on quadrature nodes: the **collocation** methods Gauss
(Gauss–Legendre nodes), Radau IIA (right Radau nodes, $c_s=1$) and Lobatto IIIA
(Lobatto nodes), and Lobatto IIIC, which shares $b$ and $c$ with Lobatto IIIA but has
a different $A$ and is "not quite standard collocation" (Farrell et al. 2021, §3.2).
Their appeal is order up to $2s$ together with stage order $s$, which avoids the
[order reduction](/definitions/order-reduction.md) of low-stage-order methods, and
A-stability at every order, which linear multistep methods cannot reach beyond 2
([Southworth et al. 2022](/sources/southworth-2022.md), §2.1). The same two
arguments, the stage-order limit on index-2 [DAEs](/definitions/differential-algebraic-equation.md)
and the second Dahlquist barrier for multistep methods, motivate their use for
incompressible flow and MHD ([Abu-Labdeh et al. 2023](/sources/abulabdeh-2023.md), §2,
§3.3) and for fluid–structure interaction ([Taddei et al. 2026](/sources/taddei-2026.md),
§1.1). Their obstacle is the coupled stage system.

## Family properties

| family | order $p$ | stage order $q$ | stability | other |
|---|---|---|---|---|
| Gauss | $2s$ | $s$ | A- and B-stable, not L-stable | symplectic; stability function the $(s,s)$ Padé approximant |
| Radau IIA | $2s-1$ | $s$ | L-stable | $c_s=1$; the one-stage member is backward Euler |
| Lobatto IIIA | — | — | A-stable | collocation; includes Crank–Nicolson |
| Lobatto IIIC | $2s-2$ | $s-1$ (see below) | A-, L- and B-stable | not collocation |

Orders and stage orders are from Southworth et al. (2022, §2.1 and the order labels
of §7) and Farrell et al. (2021, §3.2); [Čaklović et al. (2025)](/sources/caklovic-2025.md)
(§2.1) give the same orders $2\mathsf M-1$ for Radau IIA ("Radau-Right") and $2\mathsf M-2$ for
Lobatto collocation on $\mathsf M$ nodes; stability classes from Farrell et al. (2021,
§3.2), who also note that every listed collocation family is A-stable; the Padé
statement from [Sun et al. (2022)](/sources/sun-2022.md), §1, after Hairer–Wanner
Table IV.5.13. The two-stage Lobatto IIIC tableau is

$$c=\begin{pmatrix}0\\1\end{pmatrix},\qquad A=\begin{pmatrix}\tfrac12&-\tfrac12\\\tfrac12&\tfrac12\end{pmatrix},\qquad b=\begin{pmatrix}\tfrac12\\\tfrac12\end{pmatrix}$$

(Farrell et al. 2021, Eq. (35)). Its $Ac=(-\frac12,\frac12)^\top\neq c^2/2$, so it
satisfies $C(1)$ but not $C(2)$: stage order $1=s-1$ *(compiler check, not in the
sources)*. [Irksome](/software/irksome.md) generates Gauss, Radau IIA and Lobatto
IIIA of any order from quadrature nodes supplied by FIAT, with $A$ and $b$ obtained
by numerical integration, plus Lobatto IIIC of general order (Farrell et al. 2021,
§3.2).

Further properties recalled by the sources:

- An A-stable irreducible method with invertible $A$ (DIRK, Gauss, Radau IIA,
  Lobatto IIIC) has all eigenvalues of $A$ in the open right half-plane (Southworth
  et al. 2022, §2.2, Assumption 1, after Hairer–Wanner); this is what makes the
  stage system solvable by backward-Euler-like blocks.
- Fully implicit methods can be symplectic at any order, unlike DIRK methods
  (Southworth et al. 2022, §2.1; but see the qualification on
  [DIRK methods](/methods/diagonally-implicit-runge-kutta.md)); Gauss methods preserve quadratic invariants,
  while cubic invariants need "very strong conditions" (Farrell et al. 2021, §4.4.2,
  citing Iserles–Zanna). See [symplecticity](/properties/symplecticity.md).
- For $y'=Ly$ with $L$ seminegative and possibly non-normal, Sun et al. (2022,
  Thms. 5.1–5.2) prove a discrete energy identity for every $(s,s)$ diagonal Padé
  approximant, hence for Gauss methods: the energy decay is a truncation of the
  exact one with the same weights, giving unconditional strong stability and
  energy-dissipation error $\mathcal O(h^{2s})$ globally; see
  [unconditional strong stability of diagonal Padé schemes](/results/diagonal-pade-strong-stability.md).
- Gauss methods attain the [weak-stage-order barrier](/results/weak-stage-order-barriers.md)
  for general Runge–Kutta methods sharply, with weak stage order $s$
  ([Biswas et al. 2024](/sources/biswas-2024.md), Ex. 7.4).
- For Radau IIA, $A^{-1}$ has $\lfloor s/2\rfloor$ complex-conjugate eigenvalue pairs
  plus one real eigenvalue for odd $s$, so a diagonalization of $A^{-1}$ leaves
  $\lceil s/2\rceil$ independent blocks ([Munch et al. 2024](/sources/munch-2024.md),
  §2, recalling Butcher).
- *(Compiler remark, not in the sources.)* For Gauss methods the eigenvalues of $A^{-1}$
  are the roots of the Padé denominator, $3\pm\sqrt3\,\mathrm i$ for $s=2$ and the values
  tabulated for $s\le4$ by [Song & Eisenträger (2022)](/sources/song-2022.md) (Eqs. (71),
  (76), (82)), who factor the $(m,m)$ Padé approximant in their
  [Padé time integration](/methods/pade-time-integration.md) of linear structural dynamics
  without mentioning Gauss methods; on linear constant-coefficient problems that scheme's
  homogeneous propagator is that of $m$-stage Gauss.
- **Stability functions as Padé approximants.** [Jin et al. (2025)](/sources/jin-2025.md)
  (Table 4.1) classify the stability functions of 2-, 3- and 4-stage Lobatto IIIC (orders 2, 4,
  6) as the $(0,2)$, $(1,3)$, $(2,4)$ Padé approximants and that of 3-stage Radau IIA (order 5) as
  the $(2,3)$ one, all L-stable. Two-stage Lobatto IIIC has $R(z)=2/(z^2-2z+2)$, translated
  from their variable $-z$ (§3.3). The 3-stage Lobatto IIIC function changes sign on the
  negative real axis, which excludes it from their Parareal robustness theorem (Remark 3.7).
  These methods are their fine [Parareal](/methods/parareal.md) propagators, because a fine
  method with $\lvert R(-\infty)\rvert=1$ (Crank–Nicolson, Gauss) needs a bounded spectrum and
  many fine steps per slice (§2.1, Remark 3.1).
- Radau IIA is [stiffly accurate](/properties/stiff-accuracy.md), $a_{sj}=b_j$ and
  $c_s=1$, so $y_{n+1}=Y_s$ and the update step can be dropped; with invertible $A$ the
  stage derivatives of a kinematic variable can be eliminated through $A^{-1}\otimes I$
  (Taddei et al. 2026, §3.1, Eqs. (15), (18)).
- Degree-$p$ discontinuous Galerkin in time with $(p+1)$-point Radau quadrature is
  equivalent to Radau IIA collocation, so solvers for these methods also solve DG in
  time on fixed slabs (Southworth et al. 2022, Remark 1).
- **ADER-DG as an implicit Runge–Kutta method.** The ODE solver of
  [Popov (2024)](/sources/popov-2024.md), an ADER scheme with a local DG predictor of degree
  $\mathsf M$ (the source's $N$) on the $\mathsf M+1$ Gauss–Legendre nodes, is an
  $(\mathsf M+1)$-stage implicit Runge–Kutta method with $A=B$, the predictor matrix of
  [ADER time integration](/methods/ader-time-integration.md) (DG stiffness matrix inverse times
  the diagonal mass matrix), Gauss weights $b$ and Gauss nodes $c$; Popov uses this form for
  the stability function (§1.1–1.2, Eqs. (11)–(15)). He shows numerically that it is
  A-stable for $\mathsf M\le60$ (plotted stability regions) and that $R$ has numerator degree
  $\mathsf M$ over denominator degree $\mathsf M+1$ for $\mathsf M\le80$ (rank computation),
  whence his "L1-stable"; he observes order $2\mathsf M+1$ at the nodes (§1.2, §2.1). Both are
  numerical evidence for finitely many degrees, not proofs, and the paper does not relate the
  scheme to known methods. *(Compiler remark, not in the source:* for linear autonomous
  problems the nodal quadrature of $f$ is exact, so the scheme is then upwind DG in time of
  degree $\mathsf M$, whose stability function is the $(\mathsf M,\mathsf M+1)$ Padé
  approximant, that of $(\mathsf M+1)$-stage Radau IIA, consistent with the DG–Radau
  equivalence above; the ADER page records a numerical check of this for $\mathsf M\le12$.)
- **Dense output.** Inside the step the collocation polynomial is accurate to order $\mathsf M$
  only, against up to $2\mathsf M$ at the step end ([Saupe et al. (2025)](/sources/saupe-2025.md),
  §2.1, after Hairer–Nørsett–Wanner); see [dense output](/methods/dense-output.md).

## The stage system

For a linearized problem $My'=Ly+\dots$ (mass matrix $M$), the stage equations in
the stage-derivative unknowns of Farrell et al. and Southworth et al. have matrix

$$I_s\otimes M-h\,A\otimes L$$

(Farrell et al. 2021, Eq. (31), for the heat equation; Southworth et al. 2022,
Eq. (4), where each block row carries its own stage linearization $L_i$ in the
nonlinear case). For DIRK methods it is block lower triangular; here it is full.
Two strategies appear:

- **Block-diagonal preconditioning** (Mardal–Nilssen–Staff):
  $\mathrm{diag}(M-h\,a_{ii}L)_{i=1}^s$, $s$ independent backward-Euler-like
  solves, each approximated by one algebraic-multigrid cycle inside GMRES (Farrell
  et al. 2021, §2.3, Eq. (32), Listing 2).
- **Real Schur form of $A^{-1}$** (Southworth et al. 2022, §2.2–5, building on Part
  I of their work and on the RADAU code): factor
  $(A^{-1}\otimes M-h\,\mathrm{diag}(L_i))(A\otimes I)$, reduce $A^{-1}$ to real
  Schur form, and solve by block back substitution through $1\times1$ blocks
  $\xi M-hL$ and $2\times2$ blocks for each complex pair $\xi\pm i\omega$ of
  eigenvalues of $A^{-1}$ ($\xi,\omega$ page-local, $\xi>0$ by A-stability). Each
  $2\times2$ block is preconditioned with a block-triangular operator whose Schur
  complement is approximated by $\vartheta_*M-hL$, $\vartheta_*=\xi+\omega^2/\xi$ (page-local); the
  preconditioned Schur complement then has condition number at most
  $1+\omega^2/(2\xi^2)$ when the two stage linearizations coincide (Cor. 1, tight)
  and at most $2+\omega^2/\xi^2$ when they differ, provided the scaled
  linearizations satisfy $\langle hM^{-1}L_1w,\,hM^{-1}L_2w\rangle\ge0$ for all $w$
  (Thm. 2). The tight bounds range from
  1.00 to 3.44 for Gauss, Radau IIA and Lobatto IIIC with 2–5 stages (Table 1).

For saddle-point DAEs the system keeps its block structure: Abu-Labdeh et al. (2023,
§3.1, Eq. (3)) write the Taylor–Hood Stokes stage system as
$I_s\otimes\begin{bmatrix}M&0\\0&0\end{bmatrix}+h\,A\otimes\begin{bmatrix}K&B\\B^\top&0\end{bmatrix}$
(page-local stiffness $K$ and discrete gradient $B$), and Munch et al. (2024, §2, Eq. (1))
multiply the heat-equation system by $A^{-1}\otimes I$ to get
$A^{-1}\otimes M+h\,I_s\otimes K$. Three further strategies appear:

- **Monolithic multigrid with stage-coupled Vanka patches** (Abu-Labdeh et al. 2023,
  §4): one geometric V-cycle on the whole stage system, interpolating each stage
  separately ($I_s\otimes P$, page-local $P$) and relaxing on vertex patches that contain
  all stage copies, so that no Schur complement, which "may depend on properties of the
  specific IRK scheme", has to be approximated.
- **Stage-parallel diagonalization** (Munch et al. 2024, §2–6): either Butcher's exact
  complex diagonalization of $A^{-1}$ with $\lceil s/2\rceil$ complex blocks, or the
  Axelsson–Neytcheva preconditioner that replaces $A^{-1}$ by the lower-triangular factor
  of its LU decomposition, whose real eigendecomposition gives $s$ real blocks
  $\tilde\lambda_iM+hK$ ($\tilde\lambda_i$ page-local); the blocks are solved concurrently on
  process subgroups.
- **All-stage Newton with static condensation** (Taddei et al. 2026, §3.2): the coupled
  nonlinear stage system of a fluid–structure problem is condensed onto the interface
  unknowns, with no stage decoupling.

Details, including the Newton-like approximations of the stage Jacobian, are on
[solving the stage equations](/methods/implicit-stage-solvers.md).

## Iterative and parallel-in-time solution of the collocation step

The collocation step $Y=y_n\mathbf 1+hQf(Y)$, $Q=A$, can also be solved by a preconditioned
fixed-point iteration instead of Newton on the coupled system. Spectral deferred correction
(SDC) sweeps $Y^{(k+1)}-hQ_\Delta f(Y^{(k+1)})=y_n\mathbf 1+h(Q-Q_\Delta)f(Y^{(k)})$ with a cheap
$Q_\Delta$, so that $K$ sweeps solve $K\mathsf M$ systems of size $d$ instead of one system of size
$\mathsf Md$ (Saupe et al. 2025, §2.1, Eq. (12); Čaklović et al. 2025, §2.1). Classical SDC with
lower-triangular $Q_\Delta$ is an iterated implicit Runge–Kutta method of van der Houwen &
Sommeijer, and a diagonal $Q_\Delta$ makes the node solves of each sweep parallel; after $K$ sweeps
the order is $\min(K,p)$, as recalled by Čaklović et al. (§1, §3.1). See
[diagonal SDC](/methods/parallel-sdc.md) and [deferred correction](/methods/deferred-correction.md).
Čaklović et al. (2025, §1.1) recall that stage-parallel diagonalization and GMRES-preconditioned
approaches "struggle to outperform sequential time-stepping" for large problems, in line with
Munch et al.'s finding that stage parallelism pays off only near the strong-scaling limit
(below). [Gander & Palitta (2024)](/sources/gander-2024.md) (§7) state, citing Kressner–Massei–Zhu,
that all-at-once Runge–Kutta discretizations have a circulant-plus-low-rank structure to which
their [ParaDiag](/methods/paradiag.md) solver applies; they show it only for backward Euler and
BDF.

## Cost and accuracy in the sources

- **Heat equation, block-diagonal AMG** ($128\times128$ $Q_2$ mesh, $h=0.078125$):
  Radau IIA with 2 stages costs about 3 backward-Euler solves per step, with 3
  stages about 5; Richardson extrapolation of backward Euler needs 3 solves for
  order 2 and 7 for order 3, so the authors call Radau IIA "a clear win" (Farrell et
  al. 2021, §4.2, Fig. 3).
- **Against SDIRK** (preconditioner applications per step): Gauss of order 4 needs
  36, 244, 161 and 75 against 59, 481, 365 and 177 for SDIRK4 on the Euler vortex,
  NACA0012 at Re 40 000, and the double shear layer at Re 10 and 25 000; Gauss of
  order 10 needs 333 against 365 for SDIRK4 on the double shear layer (Southworth et
  al. 2022, Tables 3, 5–7). Lobatto IIIC is "significantly more expensive" than
  Gauss there.
- **Observed orders.** Euler vortex, degree-4 DG: Gauss 2/4/6 → 2.07/4.07/5.99,
  Radau 3/5/7 → 2.90/4.91/6.28, Lobatto IIIC 2/4/6 → 1.88/3.67/5.83 (Southworth et
  al. 2022, Table 2). Double shear layer at Re 100: Gauss 4/6/8 → 3.99/6.61/6.63,
  Radau 5/7/9 → 4.94/6.91/1.96, the last rates limited by the nonlinear tolerance
  (Table 8).
- **Order reduction.** On a manufactured heat solution two-stage Gauss falls to
  order 2, two-stage Radau IIA reduces in $L^2$ only, three-stage Radau IIA keeps
  full accuracy (Farrell et al. 2021, §4.1, Figs. 1–2).
- **Energy behaviour on the linear wave equation** ($E(10)/E(0)$ for
  $h=0.1,0.5,1$): Gauss with 1 and 2 stages conserve $E$ to machine precision;
  Lobatto IIIC(2) gives $3.79\times10^{-1}$, $9.75\times10^{-18}$, $1.17\times10^{-20}$;
  Lobatto IIIC(3) $9.99\times10^{-1}$, $5.19\times10^{-2}$, $3.65\times10^{-9}$;
  Radau IIA(1) $1.50\times10^{-8}$, $3.40\times10^{-16}$, $6.79\times10^{-14}$;
  Radau IIA(2) $9.00\times10^{-1}$, $7.10\times10^{-4}$, $3.77\times10^{-7}$
  (Farrell et al. 2021, Table 1). Radau and Lobatto damping is a weakness for wave
  problems.
- **Invariants.** On the BBM solitary wave Gauss with 1 and 2 stages preserves the
  linear and quadratic invariants to $\mathcal O(10^{-15})$, while the cubic one
  drifts to $0.9948969$ and $0.9999990$ of its initial value (Farrell et al. 2021,
  Table 2).
- **Navier–Stokes cylinder benchmark** (Re 100): two-stage Radau IIA with
  Scott–Vogelius elements matches reference drag and lift with about 0.57 of the
  degrees of freedom and twice the step of a Crank–Nicolson reference (Farrell et
  al. 2021, §4.4.1). With Taylor–Hood elements and $h=1/400$, two- and three-stage
  Radau IIA and Lobatto IIIC give maximum drag 2.95 and lift 0.48 at every refinement
  level (up to 46.6M unknowns on 640 cores), while three-stage Gauss gives "highly
  oscillatory" drag and lift even with a tighter tolerance; Abu-Labdeh et al. (2023,
  §5.2, Table 6, Fig. 4) hypothesize that the lack of L-stability leaves stiff modes
  with $R(z)\approx-1$ undamped. See [flow past a cylinder](/benchmarks/flow-past-cylinder.md).
- **Stokes, Gauss against Radau and Lobatto** (Abu-Labdeh et al. 2023, §5.1,
  Tables 1–2; time step halved with each mesh refinement): two-stage velocity errors
  at the finest level $5.6\times10^{-4}$ (Gauss), $5.0\times10^{-8}$ (Radau IIA),
  $6.3\times10^{-5}$ (Lobatto IIIC); velocity rates 2.5, 3.0–3.1, 2.0; Gauss pressure
  rates near 1 or negative. The authors do not explain the Gauss errors.
- **Against L-stable DIRKs** (Abu-Labdeh et al. 2023, §5.1, Table 4): the two-stage
  Pareschi–Russo and three-stage Alexander SDIRKs "outperform" their stage-order-1
  guarantees, but three-stage Alexander needs a finer level to match two-stage Radau IIA,
  which gets there in about 60 % of the wall time on one eighth of the cores.
- **Fluid–structure interaction** (Taddei et al. 2026, §5): Radau IIA with $s=2,3,4$
  shows fitted rates 2.1, 2.4 and 3.5 against the formal 3, 5, 7, which the authors
  attribute to the DAE structure and to the spatial, ALE and interface-coupling errors
  (§5.1.1, Table 1); on the Turek–Hron FSI3 benchmark two-stage Radau IIA keeps a bounded
  total energy over long times where BDF2 with undamped [Newmark](/methods/newmark-method.md)
  is unstable, and drag and lift statistics agree across $s=2,3,4$ and $h=0.01,0.02$
  (§5.2.1, Table 2). No timings are reported.
- **Stage parallelism** (Munch et al. 2024, §4–7): on a 3D heat equation, solving the
  decoupled blocks concurrently pays off only near the strong-scaling limit, below
  about $10^4$ unknowns per process, with speedup bounded by $s$; far from it the
  stage-parallel variant loses about 13–20 %.
- **Against parallel SDC.** Under a cost model, diagonal SDC on 4 Radau IIA nodes beats the
  L-stable ESDIRK4(3)6L[2]SA on the Lorenz system and on Allen–Cahn, and on Allen–Cahn also in
  measured MPI wall time (Čaklović et al. 2025, §4.2, §4.4). On each of four stiff problems at least
  one adaptive parallel SDC variant beat the order-5 embedded pair used there (ESDIRK5(3) on van
  der Pol and the quench problem, ARK5(4) on Schrödinger and Allen–Cahn) in measured wall time;
  ARK5(4) was faster on Schrödinger at low accuracy (Saupe et al. 2025, §4.2, Fig. 10).
- **Very high order: ADER-DG.** In 500-digit arithmetic Popov (2024, §2.1) observes nodal
  orders $2\mathsf M+1$ up to $\mathsf M=60$ (121.01) and order $\mathsf M+1$ for the in-step
  polynomial on non-stiff problems. On the stiff flame problem $y'=y^2-y^3$, $y(0)=\delta$
  (page-local), the fitted nodal orders saturate near 8 for $\delta=10^{-4}$ and near 4 for
  $\delta=10^{-5}$, where degree 1 places the front too late; the same artefact is stated, not
  shown, for scipy's Radau IIA (§2.2, Table 7, Fig. 11). Per Newton iteration the scheme
  assembles an $(\mathsf M+1)d$-dimensional Jacobian system, like an $s$-stage method's $sd$
  system; Picard iteration diverges on the stiff problem at large steps (§2.2–2.3). In CPU time
  its mpmath implementation is slower than scipy's explicit pairs and Radau IIA(5) at comparable
  order but reaches errors they cannot (§2.3, Fig. 12; hardware not stated).

## Qualifications

- **Labelling.** Farrell et al. (2021) label methods by stage count (GL($s$),
  RadauIIA($s$)), Southworth et al. (2022) by order ("Gauss 4" is two-stage
  Gauss). The cost and order figures above are quoted in each source's convention
  and translated where stated.
- Farrell et al. (2021, §4.1) say the $H^1$ error of three-stage Lobatto IIIC
  "stays at order three (which is both the stage order and the spatial order in this
  norm)". The stage order of $s$-stage Lobatto IIIC is $s-1$ in the standard
  classification, which their own two-stage tableau illustrates (compiler check
  above), so the observed order 3 is not its stage order. The same paragraph says
  "Gauss-Lobatto" for the Gauss–Legendre method of its Fig. 2a.
- Abu-Labdeh et al. (2023, §2, §5) state that Gauss, Radau IIA and Lobatto IIIC are all
  "fully implicit schemes, with stage order equal to the number of stages", and that
  fully implicit stage order "can be as large as the number of stages". For Lobatto IIIC
  this is the same printed claim as Farrell et al.'s, against the standard value $s-1$,
  which the two-stage tableau above settles (compiler check). Both sources print the
  higher value; no ingested source states $s-1$, which rests on the compiler check. They
  also define stage order as $\min\{q,p\}$ for a stage error $\mathcal O(h^{q+1})$, a
  variant of the usual definition through $C(q)$ (§2).
- Abu-Labdeh et al. (2023) print Table 2 rates that differ slightly from their Table 1
  data for three-stage Gauss (velocity 2.4 against 2.31 recomputed from Table 1 *(compiler check, not in the
  sources)*). Taddei et al. (2026) print $h=0.20,0.10,0.05$ in the caption of Table 1, whose
  header and text use $0.025,0.05,0.10$; at $h=0.10$ their four-stage error exceeds the
  three-stage one, against their text.
- Southworth et al. (2022) state in the abstract that fourth-order Gauss needs
  "roughly half" the preconditioner applications of SDIRK; the ratios are 0.42–0.61,
  and they compare equal order at equal step, not equal accuracy. Their Table 2
  includes rates visibly below nominal for Lobatto IIIC (1.13 and 3.53 at coarse
  steps) under "the expected rates of convergence are observed".
- The real Schur and condition-number results assume the field of values of the
  linearization lies in the closed left half-plane (Southworth et al. 2022,
  Assumption 2), stronger than eigenvalue stability for non-normal operators.
- **"Up to order $2\mathsf M$".** Saupe et al. (2025, §2.1) write that Gauss–Legendre,
  Gauss–Lobatto and Gauss–Radau nodes give superconvergence "up to order $2\mathsf M$" at the step
  end, citing Hairer–Wanner. Only Gauss nodes reach $2\mathsf M$; Radau IIA reaches $2\mathsf M-1$ and
  Lobatto $2\mathsf M-2$, as the family table and Čaklović et al. (2025, §2.1) state. Gauss nodes
  also exclude the step end, which then needs the update $y_n+hb^\top f(Y)$.
- Popov's (2024) A- and L-stability claims rest on plots for $\mathsf M\le60$ and on rank
  computations for $\mathsf M\le80$; no proof is given. His §2.3 count of "at least
  $(N+1)^2$" right-hand-side evaluations per Picard iteration (and as many Jacobians per Newton
  iteration) is inconsistent with his own predictor system, Eq. (11), which evaluates $f$ only
  at the $\mathsf M+1$ nodes, the $s$-stage count with $s=\mathsf M+1$ *(compiler check of
  Eq. (11), not in the sources)*. This weakens his conclusion that the scheme costs more than
  implicit Runge–Kutta methods.

# Citations

- [Farrell et al. (2021)](/sources/farrell-2021.md) — §1; §2.1, §2.3 Eqs. (31)–(32); §3.2 Eq. (35); §4.1–4.4 Figs. 1–3, Tables 1–2.
- [Southworth et al. (2022)](/sources/southworth-2022.md) — §2.1–2.2, Assumptions 1–2, Remark 1; §3–5 Cor. 1, Thm. 2, Table 1; §7 Tables 2–8.
- [Sun et al. (2022)](/sources/sun-2022.md) — §1; Thms. 5.1–5.2, Remark 5.6.
- [Biswas et al. (2024)](/sources/biswas-2024.md) — Ex. 7.4.
- [Abu-Labdeh et al. (2023)](/sources/abulabdeh-2023.md) — §2; §3.1 Eq. (3), §3.3; §4; §5.1–5.2 Tables 1–6, Fig. 4.
- [Munch et al. (2024)](/sources/munch-2024.md) — §2 Eqs. (1)–(3); §4–7.
- [Taddei et al. (2026)](/sources/taddei-2026.md) — §1.1; §3.1 Eqs. (14)–(18); §3.2; §5.1.1 Table 1; §5.2.1 Table 2, Figs. 9–11.
- [Song & Eisenträger (2022)](/sources/song-2022.md) — Eqs. (71), (76), (82) (roots of the Padé denominators).
- [Čaklović et al. (2025)](/sources/caklovic-2025.md) — arXiv v2: §1, §1.1, §2.1, §3.1, §4.2, §4.4.
- [Saupe et al. (2025)](/sources/saupe-2025.md) — arXiv v2: §2.1 (Eq. (12), dense output), §4.2 (Fig. 10).
- [Jin et al. (2025)](/sources/jin-2025.md) — arXiv v2: §2.1, Remark 3.1, §3.3 (Remark 3.7), Table 4.1.
- [Gander & Palitta (2024)](/sources/gander-2024.md) — arXiv v2: §7.
- [Popov (2024)](/sources/popov-2024.md) — arXiv v1: §1.1–1.2 (Eqs. (11)–(15)), §2.1–2.3 (Table 7, Figs. 11–12).
