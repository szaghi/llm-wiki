---
type: Method
title: "Diagonally implicit Runge–Kutta methods (DIRK, SDIRK, ESDIRK)"
description: "Runge–Kutta methods with lower-triangular Butcher matrix, so each step solves $s$ sequential stage systems of the problem's size; covers the SDIRK, EDIRK, ESDIRK and GEDIRK subclasses, their order and stage-order limits, the tableaux used in the sources, and their cost against fully implicit methods."
status: established
aliases: [DIRK, SDIRK, ESDIRK, EDIRK, GEDIRK, singly diagonally implicit Runge–Kutta]
tags: [runge-kutta, implicit, stiff, stage-order, linear-algebra]
timestamp: 2026-10-20T10:00:00Z
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
| SDIRK3 (Alexander) | $c=(\gamma,\tfrac{1+\gamma}2,1)$, rows $(\gamma)$, $(\tfrac{1-\gamma}2,\gamma)$, $(-\tfrac{3\gamma^2}2+4\gamma-\tfrac14,\ \tfrac{3\gamma^2}2-5\gamma+\tfrac54,\ \gamma)$; $\gamma\approx0.436$, middle root of $6\gamma^3-18\gamma^2+9\gamma-1=0$ | order 3, stiffly accurate; A-stable, hence L-stable | Roberts et al. 2021, App. A; [Puppo et al. 2024](/sources/puppo-2024.md), §4 ($\gamma=0.4358665215$) |
| five-stage SDIRK4 (new) | $\gamma=\tfrac14$, $c=(\tfrac14,1,\tfrac25,\tfrac7{11},1)$, $b$ = last row $(\tfrac{400}{459},-\tfrac{35}{216},-\tfrac{250}{351},\tfrac{1331}{1768},\tfrac14)$ | order 4, L-stable, stiffly accurate, embedded pair | Roberts et al. 2021, App. B |
| Qin–Zhang | $c=(\tfrac14,\tfrac34)$, $A=\begin{pmatrix}\tfrac14&0\\\tfrac12&\tfrac14\end{pmatrix}$, $b=(\tfrac12,\tfrac12)$ | order 2, A-stable, symplectic | Farrell et al. 2021, Eq. (37); [Sun et al. 2022](/sources/sun-2022.md), Ex. 4.3 |
| Kraaijevanger–Spijker | $c=(\tfrac12,\tfrac32)$, $A=\begin{pmatrix}\tfrac12&0\\-\tfrac12&2\end{pmatrix}$, $b=(-\tfrac12,\tfrac32)$ | $R(z)=\frac{1-\frac32z+\frac12z^2}{1-\frac52z+z^2}$; order 1, since $b^\top c=2\neq\tfrac12$ *(compiler check)* | Sun et al. 2022, Ex. 4.4 |
| trapezoidal ESDIRK | $c=(0,1)$, $A=\begin{pmatrix}0&0\\\tfrac12&\tfrac12\end{pmatrix}$, $b=(\tfrac12,\tfrac12)$ | order 2, stiffly accurate | [Gottlieb et al. 2022](/sources/gottlieb-2022.md), §2.4 (from Kennedy–Carpenter) |
| two-stage SDIRK of H-LDIRK2 | $c=(\gamma,1-\gamma)$, $A=\begin{pmatrix}\gamma&0\\1-2\gamma&\gamma\end{pmatrix}$, $b=(\tfrac12,\tfrac12)$, $\gamma=1-1/\sqrt2$ | order 2, L-stable; the Nørsett structure with a different $\gamma$ | [Southworth et al. 2024](/sources/southworth-2024.md), §5.1 |
| DIRK of SA SSP(3,3,2) | $c=(\tfrac14,\tfrac14,1)$, rows $(\tfrac14)$, $(0,\tfrac14)$, $(\tfrac13,\tfrac13,\tfrac13)$ | order 2, stiffly accurate; diagonal $(\tfrac14,\tfrac14,\tfrac13)$, so not singly diagonal | [Boscheri & Pareschi 2021](/sources/boscheri-2021.md), Eq. (79); Southworth et al. 2024, §5.1 |
| four-stage SDIRK of the type-I third-order IMEX pairs | $c=(\gamma,\gamma,\tfrac{1+\gamma}2,1)$, rows $(\gamma)$, $(0,\gamma)$, $(0,\tfrac{1-\gamma}2,\gamma)$, $(0,b_2,b_3,\gamma)$, $\gamma\approx0.4358665215$ (the SDIRK3 value) | order 3, stiffly accurate, invertible $A$ | Boscheri & Pareschi 2021, Eq. (80); [Orlando et al. 2025b](/sources/orlando-2025-b.md), Table 20; Southworth et al. 2024, §5.1 |
| ESDIRK of ARK3(2)4L[2]SA (Kennedy–Carpenter) | $c=(0,2\gamma,\tfrac35,1)$, $\gamma=\tfrac{1767732205903}{4055673282236}\approx0.4358665215$ | order 3, stiffly accurate, $R(\infty)=0$ | [Orlando & Bonaventura 2025](/sources/orlando-2025.md), Table 1; Orlando et al. 2025b, Table 21 |
| SDIRK21 (Kennedy–Carpenter) | $\gamma=1-\tfrac1{\sqrt2}$, $c=(\gamma,1)$, $A=\begin{pmatrix}\gamma&0\\\tfrac1{\sqrt2}&\gamma\end{pmatrix}$, $b=(\tfrac1{\sqrt2},\gamma)$, $\hat b=(\tfrac23,\tfrac13)$ | order 2(1), L-stable, stiffly accurate; all coefficients nonnegative | [Nurkhametova et al. 2026](/sources/nurkhametova-2026.md), §4.2.1 |
| SDIRK32 (Kennedy–Carpenter) | $\gamma=\tfrac9{40}$, $c=(\tfrac9{40},\tfrac7{13},\tfrac{11}{15},1)$, $b$ = last row $(\tfrac{4032}{9943},\tfrac{6929}{15485},-\tfrac{723}{9272},\tfrac9{40})$, $a_{31}<0$ | order 3(2), L-stable, stiffly accurate | Nurkhametova et al. 2026, §4.2.2 |
| SDIRK43 (Kennedy–Carpenter) | $\gamma=\tfrac14$, $c=(\tfrac14,\tfrac9{10},\tfrac23,\tfrac35,1)$, $b$ = last row $(\tfrac{944}{1365},-\tfrac{400}{819},\tfrac{99}{35},-\tfrac{575}{252},\tfrac14)$ | order 4(3), L-stable, stiffly accurate | Nurkhametova et al. 2026, §4.2.3 |
| five-stage SDIRK4 with explicit first stage | $\gamma=\tfrac14$ on stages 2–6, $c=(0,\tfrac14,\tfrac34,\tfrac{11}{20},\tfrac12,1)$ | order 4, stiffly accurate, L-stable | Orlando & Bonaventura 2025, Table 2 (implicit part of the Calvo–de Frutos–Novo pair) |

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

In the four-stage SDIRK row, $b_2\approx1.2084966492$ and $b_3\approx-0.6443631707$ are the
weights of ARS(3,4,3); the last two rows are the implicit parts of IMEX pairs, with an
explicit first stage padding the five-stage SDIRK4 in the last row, whose implicit rows
coincide with the five-stage L-stable SDIRK4 of Hairer and Wanner *(compiler
identification, not in the sources)*. Boscheri & Pareschi (2021,
Eq. (80)) print the four-stage SDIRK with a slip in $a_{44}$, and Orlando et al. (2025b,
Table 20) pair it with an explicit companion that fails a third-order condition; see
[semi-implicit IMEX Runge–Kutta](/methods/semi-implicit-imex-runge-kutta.md).
Puppo et al. (2024, Eq. (26)) print the corrector stage of Quinpi as
$U^{(k)}+\frac{a_{kk}h}{\Delta x}\Delta\hat F^{(k)}-U^{(k-1)}=0$, the composite backward Euler
form; consistency with their DIRK (15a) requires $-y_n$ plus the earlier stage fluxes in place
of $-U^{(k-1)}$ *(compiler check of Eqs. (15a) and (26))*.

## DIRK parts of IMEX pairs

In an [IMEX pair](/methods/imex-runge-kutta.md) the implicit tableau is a DIRK, and its
structure decides the asymptotic behaviour on stiff relaxation:

- **Explicit first stage or not.** An EDIRK/ESDIRK implicit part makes the pair "type II"
  (type CK); with $a_{i1}=0$ and $b_1=0$ it is "type ARS", effectively an $(s-1)$-stage DIRK;
  an implicit first stage makes it "type I" ([Orlando & Bonaventura 2025](/sources/orlando-2025.md),
  Def. 3.1; [Hu & Shu 2025](/sources/hu-2025.md), Eq. (2.9)). For type II, stiff accuracy
  plus A-stability does not give L-stability; the extra condition is on
  [stiff accuracy](/properties/stiff-accuracy.md). Southworth et al. (2024, §5.1) choose only
  pairs whose DIRK has no explicit stage, for asymptotic-preservation reasons whose stated
  form is disputed on [asymptotic-preserving scheme](/definitions/asymptotic-preserving-scheme.md).
- **Positive diagonal.** The uniform-accuracy proof of Hu & Shu (2025, Lemma 4.6) bounds
  $(I+\frac h\varepsilon A^{\mathrm I})^{-1}$ through the diagonal $1+\frac h\varepsilon a_{ii}$,
  which needs $a_{ii}>0$ on the implicit stages (a hypothesis left implicit there).
- **Linear stages.** In semi-implicit low-Mach and MHD schemes each DIRK stage is a linear
  elliptic solve, e.g. one pressure equation or two decoupled systems per stage
  ([Boscheri & Thomann 2024](/sources/boscheri-2024.md), §3.3–3.5, with the two-stage SDIRK2,
  $\gamma=1-1/\sqrt2$, of the first table row as implicit part).

## DIRKs as bases of structure-preserving and parallel schemes

- **Positivity post-processing.** The Patankar predictor–corrector of Nurkhametova et al.
  (2026, §3.3–3.4) takes a stiffly accurate SDIRK step as predictor and replaces the result by
  one linear M-matrix solve built from the clipped stages; its positivity proof needs $b\ge0$,
  and the stage variant also $a_{ij}\ge0$. In the tableaux above only SDIRK21 meets these
  conditions: SDIRK32 has a negative weight and SDIRK43 two *(compiler check of the printed
  tableaux; not discussed in the source)*. Because DIRKs have stage order $q=1$, the proven
  order of the corrected method is $\min(p,q+1)=2$ (Prop. 3.23), although slopes near 3 and 4
  are observed (Tables 4–5). See [modified Patankar methods](/methods/modified-patankar-methods.md).
- **SDC sweeps as DIRKs.** One sweep of spectral deferred correction with a lower-triangular
  preconditioner $Q_\Delta$ costs as much as a DIRK with $s=\mathsf M$ stages, and setting
  $Q_\Delta=Q=A$ for a DIRK Butcher matrix makes the sweep reproduce that DIRK, so a generic SDC
  code runs any DIRK ([Čaklović et al. 2025](/sources/caklovic-2025.md), §2, Remark 2.2). Their
  parallel SDC variants beat ESDIRK4(3)6L[2]SA of Kennedy–Carpenter on the Lorenz system and
  on Allen–Cahn under their cost model (§4.2, §4.4); see
  [deferred correction](/methods/deferred-correction.md).

## Composite backward Euler as a DIRK; DIRKs in flux form

A sequence of backward Euler sub-steps through the abscissae of a DIRK is itself a DIRK.
With sub-steps $\theta_k=c_k-c_{k-1}$ ($c_0=0$, abscissae increasing; page-local
$\theta_k$), the composite backward Euler method has the same $c$, row $k$ of $A$ equal to
$(\theta_1,\dots,\theta_k,0,\dots,0)$ and $b=(\theta_1,\dots,\theta_s)$
([Puppo et al. 2024](/sources/puppo-2024.md), §3.1, Eqs. (19), (22)). For Alexander's
SDIRK3 this gives $\theta=(\gamma,\tfrac{1-\gamma}2,\tfrac{1-\gamma}2)$ (§4). The tableau is
first order and stiffly accurate by construction, since $b$ is its last row *(compiler
remark, not in the sources)*. Puppo et al. run it as a first-order predictor
alongside SDIRK3 so that both share stage times; its stage values fix the nonlinear
reconstruction weights of the third-order stages (see
[Quinpi](/methods/quinpi.md) and [implicit stage solvers](/methods/implicit-stage-solvers.md)).
On a finite-volume semi-discretization they write the DIRK in flux form, each stage value
being $y_n$ minus $h/\Delta x$ times the $a_{ki}$-weighted sum of earlier and current
interface-flux differences (Eqs. (15a)–(15b)). Equal diagonal entries simplify the
Jacobian (§2.2), and the step is set by accuracy on the slow wave of a stiff hyperbolic
system, at Courant numbers of about 7 to 670 in their tests (§4). They note that strictly
increasing abscissae are "not necessary for our construction" (§4).

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
- **Printed slip in Nurkhametova et al. (2026).** The printed embedded weights of SDIRK32,
  $\hat b=(\tfrac{20}{51},-\tfrac{410011317313}{22571052756900},-\tfrac{2075562131}{281561189810},\tfrac{29595333}{2429345900})$,
  sum to about 0.379, so they are mistranscribed; the main weights satisfy the order-3
  conditions *(compiler check of the printed tableau, PDF p. 28)*.
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
- [Boscheri & Pareschi (2021)](/sources/boscheri-2021.md) — §3.4.1 (Eqs. (79)–(80)); arXiv v1.
- [Boscheri & Thomann (2024)](/sources/boscheri-2024.md) — §3.3–3.5 (Eq. (39)); arXiv v1.
- [Hu & Shu (2025)](/sources/hu-2025.md) — Eq. (2.9), Lemma 4.6; arXiv v1.
- [Southworth et al. (2024)](/sources/southworth-2024.md) — §5.1.
- [Orlando & Bonaventura (2025)](/sources/orlando-2025.md) — Def. 3.1, Tables 1–2; HAL v2.
- [Orlando et al. (2025b)](/sources/orlando-2025-b.md) — Tables 20–21; arXiv v5.
- [Puppo et al. (2024)](/sources/puppo-2024.md) — §2.2 (Eqs. (14)–(16)), §3.1 (Eqs. (19)–(24)), Eq. (26), §4 (Alexander SDIRK3).
- [Nurkhametova et al. (2026)](/sources/nurkhametova-2026.md) — §3.3–3.4, Prop. 3.23, §4.2 (SDIRK21, SDIRK32, SDIRK43 tableaux), Tables 4–5.
- [Čaklović et al. (2025)](/sources/caklovic-2025.md) — §2 (Remark 2.2), §3, §4.2, §4.4; arXiv v2.
