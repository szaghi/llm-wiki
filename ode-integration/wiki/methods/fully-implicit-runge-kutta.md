---
type: Method
title: "Fully implicit collocation Runge–Kutta methods (Gauss, Radau IIA, Lobatto IIIC)"
description: "Runge–Kutta methods with a full Butcher matrix built on Gauss, Radau or Lobatto nodes: Gauss of order $2s$, Radau IIA of order $2s-1$ and Lobatto IIIC of order $2s-2$, with high stage order, A-, L-, B-stability and symplecticity as the family allows; the coupled $sd$-dimensional stage system and its preconditioning decide their cost."
status: established
aliases: [IRK, fully implicit Runge–Kutta, Gauss–Legendre, Radau IIA, Lobatto IIIC, Lobatto IIIA, collocation methods]
tags: [runge-kutta, implicit, stiff, stability, linear-algebra, geometric-integration]
timestamp: 2026-10-19T12:00:00Z
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
([Southworth et al. 2022](/sources/southworth-2022.md), §2.1). Their obstacle is
the coupled stage system.

## Family properties

| family | order $p$ | stage order $q$ | stability | other |
|---|---|---|---|---|
| Gauss | $2s$ | $s$ | A- and B-stable, not L-stable | symplectic; stability function the $(s,s)$ Padé approximant |
| Radau IIA | $2s-1$ | $s$ | L-stable | $c_s=1$; the one-stage member is backward Euler |
| Lobatto IIIA | — | — | A-stable | collocation; includes Crank–Nicolson |
| Lobatto IIIC | $2s-2$ | $s-1$ (see below) | A-, L- and B-stable | not collocation |

Orders and stage orders are from Southworth et al. (2022, §2.1 and the order labels
of §7) and Farrell et al. (2021, §3.2); stability classes from Farrell et al. (2021,
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
- Degree-$p$ discontinuous Galerkin in time with $(p+1)$-point Radau quadrature is
  equivalent to Radau IIA collocation, so solvers for these methods also solve DG in
  time on fixed slabs (Southworth et al. 2022, Remark 1).

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

Details, including the Newton-like approximations of the stage Jacobian, are on
[solving the stage equations](/methods/implicit-stage-solvers.md).

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
  al. 2021, §4.4.1).

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
- Southworth et al. (2022) state in the abstract that fourth-order Gauss needs
  "roughly half" the preconditioner applications of SDIRK; the ratios are 0.42–0.61,
  and they compare equal order at equal step, not equal accuracy. Their Table 2
  includes rates visibly below nominal for Lobatto IIIC (1.13 and 3.53 at coarse
  steps) under "the expected rates of convergence are observed".
- The real Schur and condition-number results assume the field of values of the
  linearization lies in the closed left half-plane (Southworth et al. 2022,
  Assumption 2), stronger than eigenvalue stability for non-normal operators.

# Citations

- [Farrell et al. (2021)](/sources/farrell-2021.md) — §1; §2.1, §2.3 Eqs. (31)–(32); §3.2 Eq. (35); §4.1–4.4 Figs. 1–3, Tables 1–2.
- [Southworth et al. (2022)](/sources/southworth-2022.md) — §2.1–2.2, Assumptions 1–2, Remark 1; §3–5 Cor. 1, Thm. 2, Table 1; §7 Tables 2–8.
- [Sun et al. (2022)](/sources/sun-2022.md) — §1; Thms. 5.1–5.2, Remark 5.6.
- [Biswas et al. (2024)](/sources/biswas-2024.md) — Ex. 7.4.
