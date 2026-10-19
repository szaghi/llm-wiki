---
type: Method
title: "Diagonally implicit Runge–Kutta methods (DIRK, SDIRK, ESDIRK)"
description: "Runge–Kutta methods with lower-triangular Butcher matrix, so each step solves $s$ sequential stage systems of the problem's size; covers the SDIRK, EDIRK, ESDIRK and GEDIRK subclasses, their order and stage-order limits, the tableaux used in the sources, and their cost against fully implicit methods."
status: established
aliases: [DIRK, SDIRK, ESDIRK, EDIRK, GEDIRK, singly diagonally implicit Runge–Kutta]
tags: [runge-kutta, implicit, stiff, stage-order, linear-algebra]
timestamp: 2026-10-19T12:00:00Z
---

# Diagonally implicit Runge–Kutta methods (DIRK, SDIRK, ESDIRK)

A [Runge–Kutta method](/definitions/runge-kutta-method.md) $(A,b,c)$ is
**diagonally implicit** when $a_{ij}=0$ for $j>i$ and some $a_{ii}\neq0$. Its
stages are then computed one after another,

$$Y_i-h\,a_{ii}\,f(t_n+c_ih,Y_i)=y_n+h\sum_{j<i}a_{ij}f(t_n+c_jh,Y_j),\qquad i=1,\dots,s,$$

so a step costs $s$ nonlinear systems of the dimension $d$ of the problem instead
of one coupled system of dimension $sd$
([Farrell et al. 2021](/sources/farrell-2021.md), §2.1;
[Gardner et al. 2022](/sources/gardner-2022.md), §2.5;
[Biswas et al. 2023](/sources/biswas-2023.md), §2). This is the reason DIRK methods
are the default implicit Runge–Kutta family in practice, and their weakness is the
low [stage order](/definitions/stage-order.md) the triangular structure allows.

## Subclasses

Let $\gamma$ denote a common diagonal entry, page-local (as in the Rosenbrock
family). The sources use:

- **SDIRK** (singly diagonally implicit): all $a_{ii}=\gamma$, so every stage
  system has the same matrix $I-h\gamma J$ in a Newton iteration
  ([Biswas et al. 2024](/sources/biswas-2024.md), §2.1).
- **EDIRK**: $a_{11}=0$, an explicit first stage (Biswas et al. 2024, §2.1;
  Biswas et al. 2023, §8). **ESDIRK**: an EDIRK whose other diagonal entries are
  equal ([Southworth et al. 2022](/sources/southworth-2022.md), §2.1).
- **GEDIRK** (generalized EDIRK, introduced by Biswas et al. 2024, Def. 2.1): a
  DIRK in which the first stage with $c_\ell=0$ has $a_{\ell\ell}=0$. Explicit
  methods are GEDIRKs.
- Biswas et al. (2023, 2024) allow distinct diagonal entries; their
  [high-weak-stage-order schemes](/methods/dirk-high-weak-stage-order.md) need
  $a_{11}\neq a_{22}$ and so are not SDIRK.

## Order and stage-order limits

- **Stage order.** An irreducible DIRK has stage order at most 2, and at most 1
  if $A$ is nonsingular (Biswas et al. 2023, Thm. 2.2, recalled from Ketcheson et
  al. 2020). Southworth et al. (2022, §2.1) state the same as $q=1$ for DIRK and
  $q=2$ for ESDIRK with one explicit stage. Biswas et al. (2024, Ex. 7.3) recover
  both bounds from their Lemma 3.13 with $\dim\mathcal K_q=0$ (stage order $q$ makes
  every residual $\tau^{(k)}$, $k\le q$, vanish).
- **Classical order.** $p\le s+1$ (Biswas et al. 2023, §4, recalling Hairer–Wanner
  Thm. IV.4.18), the $q_{\mathrm w}=0$ case of the DIRK
  [weak-stage-order barrier](/results/weak-stage-order-barriers.md); the bound
  comes from the real poles of the
  [stability function](/definitions/stability-function.md) (Nørsett–Wolfbrandt,
  $p\le\deg N+1$; Biswas et al. 2024, Thm. 3.7). Southworth et al. (2022, §2.1)
  put the practical maximum at $p=s$ or $s+1$ "with reasonable stability
  properties".
- **Weak stage order.** Unlike stage order, [weak stage order](/definitions/weak-stage-order.md)
  is not capped at 2: DIRK schemes with $q_{\mathrm w}=4$ and 5 exist
  ([DIRK schemes with high weak stage order](/methods/dirk-high-weak-stage-order.md)),
  within the DIRK barrier
  $\lfloor q_{\mathrm w}/2\rfloor+p\le s+1-\delta_{\mathrm{SA}}$ for non-GEDIRKs
  ($\delta_{\mathrm{SA}}=1$ for stiffly accurate methods with invertible $A$,
  page-local).
- **Symplecticity.** Southworth et al. (2022, §2.1) state that symplectic DIRK
  methods are limited to fourth order and that the known ones above second order
  have negative diagonal entries; see Qualifications.

Low stage order is what exposes DIRK methods to
[order reduction](/definitions/order-reduction.md) on stiff problems: Biswas et al.
(2023, §6) use the $q_{\mathrm w}=1$ schemes DIRK-(5,4,1) (Hairer–Wanner, Table
IV.6.5, A-stable, stiffly accurate) and DIRK-(5,5,1) (Kennedy–Carpenter 2016,
Table 24, A-stable, not stiffly accurate) as reference cases that lose order.

## Tableaux used in the sources

| method | tableau | properties | source |
|---|---|---|---|
| SDIRK2 (Alexander) | $c=(\gamma,1)$, $A=\begin{pmatrix}\gamma&0\\1-\gamma&\gamma\end{pmatrix}$, $b=(1-\gamma,\gamma)$, $\hat b=(\tfrac35,\tfrac25)$, $\gamma=1-1/\sqrt2$ | order 2, L-stable, stiffly accurate | [Roberts et al. 2021](/sources/roberts-2021.md), Eq. (5.4) |
| two-stage order-3 SDIRK (Nørsett) | $c=(\gamma,1-\gamma)$, $A=\begin{pmatrix}\gamma&0\\1-2\gamma&\gamma\end{pmatrix}$, $b=(\tfrac12,\tfrac12)$, $\gamma=(3+\sqrt3)/6$ | order 3, algebraically stable | Roberts et al. 2021, Eq. (5.8) |
| SDIRK3 (Alexander) | $c=(\gamma,\tfrac{1+\gamma}2,1)$, rows $(\gamma)$, $(\tfrac{1-\gamma}2,\gamma)$, $(-\tfrac{3\gamma^2}2+4\gamma-\tfrac14,\ \tfrac{3\gamma^2}2-5\gamma+\tfrac54,\ \gamma)$; $\gamma\approx0.436$, middle root of $6\gamma^3-18\gamma^2+9\gamma-1=0$ | order 3, stiffly accurate | Roberts et al. 2021, App. A |
| five-stage SDIRK4 (new) | $\gamma=\tfrac14$, $c=(\tfrac14,1,\tfrac25,\tfrac7{11},1)$, $b$ = last row $(\tfrac{400}{459},-\tfrac{35}{216},-\tfrac{250}{351},\tfrac{1331}{1768},\tfrac14)$ | order 4, L-stable, stiffly accurate, embedded pair | Roberts et al. 2021, App. B |
| Qin–Zhang | $c=(\tfrac14,\tfrac34)$, $A=\begin{pmatrix}\tfrac14&0\\\tfrac12&\tfrac14\end{pmatrix}$, $b=(\tfrac12,\tfrac12)$ | order 2, A-stable, symplectic | Farrell et al. 2021, Eq. (37); [Sun et al. 2022](/sources/sun-2022.md), Ex. 4.3 |
| Kraaijevanger–Spijker | $c=(\tfrac12,\tfrac32)$, $A=\begin{pmatrix}\tfrac12&0\\-\tfrac12&2\end{pmatrix}$, $b=(-\tfrac12,\tfrac32)$ | $R(z)=\frac{1-\frac32z+\frac12z^2}{1-\frac52z+z^2}$; order 1, since $b^\top c=2\neq\tfrac12$ *(compiler check)* | Sun et al. 2022, Ex. 4.4 |
| trapezoidal ESDIRK | $c=(0,1)$, $A=\begin{pmatrix}0&0\\\tfrac12&\tfrac12\end{pmatrix}$, $b=(\tfrac12,\tfrac12)$ | order 2, stiffly accurate | [Gottlieb et al. 2022](/sources/gottlieb-2022.md), §2.4 (from Kennedy–Carpenter) |

The Qin–Zhang tableau is two implicit-midpoint steps of size $h/2$
*(compiler check, not in the sources)*. Its stability function is
$R(z)=(1+\tfrac z2+\tfrac{z^2}{16})/(1-\tfrac z2+\tfrac{z^2}{16})$, a symmetric
rational function different from the (2,2) Padé approximant, and Sun et al. (2022,
Ex. 4.3) derive the discrete energy law
$\lVert y_{n+1}\rVert^2-\lVert y_n\rVert^2=-h\,[\![w_n]\!]^2-\tfrac1{16}h^3[\![Lw_n]\!]^2$
for $y'=Ly$ with $L$ seminegative ($[\![\cdot]\!]$ the dissipation seminorm and
$w_n=(I-\tfrac h2L+\tfrac{h^2}{16}L^2)^{-1}y_n$, both page-local). For the
Kraaijevanger–Spijker method they obtain an identity with all terms
non-positive, hence unconditional strong stability (Ex. 4.4); see
[strong stability](/properties/strong-stability.md). Farrell et al. (2021, Table 1)
find the Qin–Zhang method conserves the energy of the linear wave equation exactly,
like Gauss–Legendre.

Further DIRK tableaux appear as building blocks: the implicit table of the IMEX
pair ARS(3,4,3), an SDIRK with explicit first stage and $\gamma\approx0.4359$
([Chinomona and Reynolds 2021](/sources/chinomona-2021.md), §4.1; see
[IMEX Runge–Kutta methods](/methods/imex-runge-kutta.md)); fast-scale DIRKs of
Conde et al. and Cash in multirate methods (Chinomona and Reynolds 2021, §5.2);
and SDIRK bases of [multirate GARK methods](/methods/multirate-gark.md) (Roberts et
al. 2021, §5).

## Solving the stage systems

Because $A$ is lower triangular, the coupled stage system
$(I\otimes M-hA\otimes J)$ of a linear problem is block lower triangular; Farrell
et al. (2021, §2.3, §4.3) solve it with a multiplicative field-split
preconditioner, which is block forward substitution and exact in one iteration
when each diagonal block is solved exactly, so their software
[Irksome](/software/irksome.md) needs no special code for DIRK methods. ARKODE
poses each stage as the root-finding problem
$Y_i-h\,a_{ii}f^{\mathrm I}(t_n+c_ih,Y_i)-a_i=0$ with known data $a_i$ and solves
it with a modified or inexact Newton iteration (Gardner et al. 2022, §2.5, §6); see
[implicit stage solvers](/methods/implicit-stage-solvers.md). For SDIRK methods one
Jacobian factorization serves all stages; Roberts et al. (2021, §4) exploit this
per micro- and macro-step in multirate settings.

## Cost against other implicit families

- **Against fully implicit methods.** Southworth et al. (2022, Tables 3, 5–7) count
  preconditioner applications per step for SDIRK of orders 1–4 against
  [Gauss, Radau IIA and Lobatto IIIC](/methods/fully-implicit-runge-kutta.md) with
  their block preconditioner. Fourth-order Gauss needs 36 vs 59 (Euler vortex), 244
  vs 481 (NACA0012), 161 vs 365 and 75 vs 177 (double shear layer, two Reynolds
  numbers) applications of SDIRK4; tenth-order Gauss costs slightly less than SDIRK4
  on the double shear layer. Farrell et al. (2021, §1) recall Pazner and Persson's
  finding that preconditioned Radau IIA beats DIRK methods of comparable order for
  compressible Navier–Stokes.
- **Against BDF.** On a $4096^2$ heat equation with default tolerances, CVODE's
  variable-order BDF needs 84 steps and 8.8 s, ARKODE's default third-order DIRK
  148 steps and 67.3 s (Gardner et al. 2022, Table 5); the authors attribute this to
  one nonlinear solve per BDF step and order adaptivity, and the comparison is
  specific to that problem (see [CVODE](/software/cvode.md), [ARKODE](/software/arkode.md)).
- **Positivity.** On $y'=-10y^2$, $y(0)=10$, the second- and third-order
  Kennedy–Carpenter DIRK methods lose positivity for $h>1/50$ and $h>1/75$, while
  the implicit multiderivative SSP methods of Gottlieb et al. (2022, §2.4, Fig. 1)
  stay positive for all tested $h$.

## Qualifications

- Southworth et al.'s bound "symplectic DIRK methods are limited to at most 4th
  order" (2022, §2.1, citing a technical report) needs extra hypotheses. A
  composition of implicit-midpoint steps of sizes $\gamma_jh$ is a DIRK method, it
  is symplectic, and the triple-jump recursion reaches any even order
  *(compiler check, not in the sources)*; [Blanes et al. (2024)](/sources/blanes-2024.md),
  §2.1, give that recursion for any time-symmetric second-order basic method, of
  which implicit midpoint is one. Such compositions have negative step fractions
  for order $\ge3$, consistent with the negative diagonal entries Southworth et al.
  mention; see [composition methods](/methods/composition-methods.md).
- "Maximum order $s$ or $s+1$ with reasonable stability" (Southworth et al. 2022)
  is a qualified practical statement, not a theorem; the theorem is $p\le s+1$.

# Citations

- [Biswas et al. (2023)](/sources/biswas-2023.md) — §2 Thm. 2.2; §4; §6 reference schemes; §8.
- [Biswas et al. (2024)](/sources/biswas-2024.md) — §2.1, Def. 2.1; Thms. 3.2, 3.7; Ex. 7.3.
- [Farrell et al. (2021)](/sources/farrell-2021.md) — §1; §2.1, §2.3 Eq. (33); §4.3 Eq. (37), Table 1, Listing 3.
- [Southworth et al. (2022)](/sources/southworth-2022.md) — §2.1; Tables 3, 5–7.
- [Roberts et al. (2021)](/sources/roberts-2021.md) — §4; §5 Eqs. (5.4), (5.8); Apps. A–B.
- [Gardner et al. (2022)](/sources/gardner-2022.md) — §2.3, §2.5; §5.1 Table 5; §6.
- [Gottlieb et al. (2022)](/sources/gottlieb-2022.md) — §2.4, Fig. 1.
- [Sun et al. (2022)](/sources/sun-2022.md) — Exs. 4.3–4.4.
- [Chinomona and Reynolds (2021)](/sources/chinomona-2021.md) — §4.1; §5.2.
- [Blanes et al. (2024)](/sources/blanes-2024.md) — §2.1.
