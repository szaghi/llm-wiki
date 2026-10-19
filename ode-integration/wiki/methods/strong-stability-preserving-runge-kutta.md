---
type: Method
title: "Strong-stability-preserving (SSP) Runge–Kutta methods"
description: "A Runge–Kutta method is SSP with coefficient $\\mathcal C$ when it preserves every convex-functional bound that forward Euler preserves for $h\\le h_{\\mathrm{FE}}$, under $h\\le\\mathcal C h_{\\mathrm{FE}}$; the page gives the characterization, order and coefficient barriers, the optimal explicit methods, embedded pairs and the multiderivative and IMEX extensions."
status: established
aliases: [SSP Runge–Kutta, SSPRK, SSPERK, TVD Runge–Kutta, monotonicity-preserving Runge–Kutta, contractivity-preserving Runge–Kutta]
tags: [ssp, runge-kutta, stability, explicit, structure-preserving]
timestamp: 2026-10-20T03:00:00Z
---

# Strong-stability-preserving (SSP) Runge–Kutta methods

A [Runge–Kutta method](/definitions/runge-kutta-method.md) is *strong stability
preserving* (SSP) if it inherits, under a step-size restriction, any bound that the
forward Euler method satisfies for the same right-hand side. The hypothesis is the
**forward Euler condition**: for a convex functional $\lVert\cdot\rVert$ (a norm, a
semi-norm, total variation, or the positivity indicator),

$$\lVert y+hf(y)\rVert\le\lVert y\rVert\qquad\text{for all }y\text{ and }0\le h\le h_{\mathrm{FE}}.$$

The method is SSP with **SSP coefficient** $\mathcal C>0$ if, under this hypothesis,
$\lVert y_{n+1}\rVert\le\lVert y_n\rVert$ whenever $h\le\mathcal Ch_{\mathrm{FE}}$
(Conde, Fekete & Shadid, [Fekete et al. 2022](/sources/fekete-2022.md), §1.1, Eq. (6);
[Gottlieb et al. 2022](/sources/gottlieb-2022.md), §1, Eq. (2)). The property is
nonlinear and independent of any linearization: it holds for every $f$ satisfying the
hypothesis. The effective SSP coefficient $\mathcal C_{\mathrm{eff}}=\mathcal C/s$
normalizes by the stage count (registry convention; none of the sources below uses it).

SSP is a different notion from the [strong stability](/properties/strong-stability.md)
of a method on a linear seminegative problem: see *Relation to strong stability* below.

## Characterization

**Shu–Osher form.** A method written as
$Y_i=\sum_{j<i}\bigl(\alpha_{ij}Y_j+h\beta_{ij}f(Y_j)\bigr)$ (with $Y_1=y_n$,
$\sum_j\alpha_{ij}=1$, all $\alpha_{ij},\beta_{ij}\ge0$) is a convex combination of
forward Euler steps of size $h\beta_{ij}/\alpha_{ij}$, so it is SSP with
$\mathcal C\ge\min_{ij}\alpha_{ij}/\beta_{ij}$ (Gottlieb et al. 2022, §1; Fekete et
al. 2022, §1.1). Fekete et al. call the convex decomposition "a sufficient and
necessary condition"; see *Qualifications*.

**Kraaijevanger's characterization.** With the $(s+1)\times(s+1)$ matrix
$\tilde A=\begin{pmatrix}A&0\\b^\top&0\end{pmatrix}$ (page-local),

$$\mathcal C(A,b)=\sup\Bigl\{r\ge0:\ (I+r\tilde A)^{-1}\text{ exists},\ \tilde A(I+r\tilde A)^{-1}\ge0,\ r\tilde A(I+r\tilde A)^{-1}\mathbf 1\le\mathbf 1\Bigr\},$$

inequalities componentwise, as recalled by Fekete et al. (2022, §1.1, Thm. 1, Eqs.
(7a)–(7b), from Gottlieb–Ketcheson–Shu, Thm. 3.2). A positive SSP coefficient requires
$A\ge0$ and $b\ge0$ (Fekete et al. 2022, Thm. 2); for an irreducible method Biswas et
al. recall the sharper requirement $A\ge0$, $b>0$ (Kraaijevanger, Thm. 4.2;
[Biswas et al. 2025](/sources/biswas-2025.md), proof of Cor. 2.8).

**Linear SSP coefficient.** On linear problems only the
[stability polynomial](/definitions/stability-function.md) matters, and the relevant
quantity is the *radius of absolute monotonicity* (threshold factor) of $R$: the
largest $r$ such that $R$ and all its derivatives are nonnegative on $(-r,0]$ (Fekete
et al. 2022, §1.1, Def. 4). It can exceed the nonlinear $\mathcal C$, and it can be
positive when $\mathcal C=0$ (Biswas et al. 2025, after Cor. 2.8).

## Barriers

- **Explicit order barrier.** No explicit Runge–Kutta method of order $p\ge5$ has
  $\mathcal C>0$, as recalled by Fekete et al. (2022, §1.1).
- **Implicit methods have bounded $\mathcal C$.** Implicit Runge–Kutta, multistep and
  general linear methods have finite SSP coefficients, "usually bounded by twice the
  number of stages for a Runge–Kutta method"; implicit methods that preserve the
  forward Euler condition for every $h>0$ cannot exist beyond first order (backward
  Euler is the exception at order 1), as recalled by Gottlieb et al. (2022, §1 and App.
  A, restating Gottlieb–Shu–Tadmor). The same barrier for positivity is the
  Bolley–Crouzeix result recalled on
  [positivity preservation](/properties/positivity-preservation.md).
- **Many stages do not bring SSP for free.** Stability polynomials optimized for
  hyperbolic spectra and realized as products of forward Euler steps and two-stage
  submethods have $\mathcal C=\min\alpha_{ij}/\beta_{ij}=0$, because the final row has
  $\alpha_{s+1,s}=0$, $\beta_{s+1,s}=1$; negative $\beta$, used to reduce
  [internal error amplification](/definitions/internal-stability.md), would need
  downwind treatment ([Doehring et al. 2024](/sources/doehring-2024.md), §9.4, Eq.
  (9.14)). On Burgers with a source and on the isentropic vortex their 28–120-stage
  methods need 28–79% of the linearly stable step and increase the total variation,
  while Ketcheson's third-order SSP method with $s=225=n^2$ stages, of similar internal
  amplification, keeps it constant; the authors attribute the reductions to the
  missing SSP property, and leave many-stage SSP methods of this kind open (§10.2,
  Tables 5–6). The optimal second-order disk polynomial
  $\frac{s-1}s(1+\frac z{s-1})^s+\frac1s$ is, by contrast, a composition of forward
  Euler steps and SSP with optimal coefficient, as recalled there (§3.1.2).
- **Partitioned methods.** A partitioned Runge–Kutta method is SSP only if every
  member is, with $h\le\min_q\mathcal C^{\{q\}}h_{\mathrm{FE}}$ over the members'
  coefficients (page-local $\mathcal C^{\{q\}}$), which makes SSP partitioned methods
  "in many cases ineffective" ([Doehring et al. 2025](/sources/doehring-2025.md),
  §2.5, Eq. (2.15)); see
  [paired explicit Runge–Kutta methods](/methods/paired-explicit-runge-kutta.md).
- **Weak stage order.** An explicit method with $A\ge0$, $b\ge0$ has either
  [weak stage order](/definitions/weak-stage-order.md) $q_{\mathrm w}=1$, or $p\le1$
  and $q_{\mathrm w}=\infty$; hence every explicit method with $p\ge2$ and
  $q_{\mathrm w}\ge2$ has $\mathcal C=0$ (Biswas et al. 2025, §2, Thm. 2.7, Cor. 2.8).
  Such methods can still have a positive *linear* SSP coefficient: the families
  (3,2,2), (4,3,2) and (5,3,3) of
  [explicit methods with high weak stage order](/methods/explicit-runge-kutta-high-weak-stage-order.md)
  have linear SSP coefficient 1 (Biswas et al. 2025, §3.1.2–3.1.4). Avoiding
  [order reduction](/definitions/order-reduction.md) this way and preserving
  nonlinear strong stability are therefore mutually exclusive for explicit methods.

## Optimal explicit SSP methods

SSPERK$(s,p)$ denotes the explicit $s$-stage, order-$p$ method with the largest
$\mathcal C$ (Fekete et al. 2022, §2). The families used across the sources:

| Method | $\mathcal C$ | Structure | Source |
|---|---|---|---|
| SSPERK$(s,2)$ (Ruuth–Spiteri; $s=2$ Gottlieb–Shu) | $s-1$ | $a_{ij}=\frac1{s-1}$ for $j<i$, $c_i=\frac{i-1}{s-1}$, $b_j=\frac1s$ | Fekete et al. 2022, §2.1, Table 1 |
| SSPERK$(n^2,3)$, $n\ge2$ (Kraaijevanger; Ketcheson) | $n^2-n=s-\sqrt s$ | entries $\frac1{n(n-1)}$ except a $\frac{n(n-1)}2\times(2n-1)$ block of $\frac1{n(2n-1)}$ | Fekete et al. 2022, §2.2, Eqs. (15)–(16) |
| SSPERK$(4,3)$ (the $n=2$ case) | 2 | $c=(0,\frac12,1,\frac12)$, rows $(\frac12)$, $(\frac12,\frac12)$, $(\frac16,\frac16,\frac16)$, $b=(\frac16,\frac16,\frac16,\frac12)$ | Fekete et al. 2022, §2.2; [Ranocha et al. 2022](/sources/ranocha-2022.md), App. A, Eq. (A.1) |
| SSPERK$(10,4)$ (Ketcheson) | 6 | rows 2–5: $\frac16$ in all previous columns; rows 6–10: $\frac1{15}$ in columns 1–5, $\frac16$ in columns $6,\dots,i-1$; $b=\frac1{10}\mathbf 1$; low-storage | Fekete et al. 2022, §2.3 |

The effective coefficients are $\mathcal C_{\mathrm{eff}}=(s-1)/s$, $1-1/n$ and $0.6$
respectively *(compiler check, not in the sources)*. The three-stage third-order
Shu–Osher method SSPRK(3,3) is the common baseline in the numerical comparisons of
Ranocha et al. (2022, §5) and Biswas et al. (2025, Table 3.2); among the classical
methods compared by Biswas et al., it, RK4 and Dormand–Prince all have
$q_{\mathrm w}=1$. Irksome ships an SSP tableau among its explicit methods
([Farrell et al. 2021](/sources/farrell-2021.md), §3.2).

Linear-stability measures go with these methods. Ranocha et al. report that the
four-stage third-order method has real stability interval 5.15, i.e. 1.29 per
right-hand-side evaluation, the largest scaled value of all pairs they compare, against
0.84 for SSPRK(3,3) and for Bogacki–Shampine 3(2) (Ranocha et al. 2022, Suppl. Table 1).
It can be implemented in three registers (Ranocha et al. 2022, App. A, Eq. (A.2)); see
[low-storage Runge–Kutta methods](/methods/low-storage-runge-kutta.md). On linear
spectra of DG with subcell shock capturing, its stability region loses about 5% of
the admissible CFL number relative to plain DG, against more than 20% for
Bogacki–Shampine 3(2) and the five-stage pair of Ranocha et al.
([Ranocha et al. 2025](/sources/ranocha-2025.md), §4.1, Fig. 3). The second-order
two-stage SSP method of Shu and Osher is the base of the second-order multirate scheme
MRK2 of Constantinescu and Sandu, which [Kang & Constantinescu (2022)](/sources/kang-2022.md)
use and extend to several levels (§2.3, Table 1).

## Embedded pairs and adaptive steps

Optimal SSP methods are usually run at a fixed CFL-limited step. Fekete et al. (2022)
construct [embedded pairs](/methods/embedded-runge-kutta-pair.md) that share $A$ with
the SSP method (no extra stage) and advance with the SSP solution (local
extrapolation). Design targets: embedded order $p-1$; non-defective (violating every
order-$p$ condition, otherwise the error estimate degenerates); rational coefficients;
and, if possible, an embedded SSP coefficient equal to $\mathcal C$ (§2, Eqs.
(9)–(11)). Results:

- SSPERK$(s,2)$: $\tilde b_1=[\frac1{s-1},\dots,\frac1{s-1},0]$ and
  $\tilde b_2=[\frac{s+1}{s^2},\frac1s,\dots,\frac1s,\frac{s-1}{s^2}]$, both with
  embedded SSP coefficient $s-1$; $\tilde b_2$ is preferred (§2.1).
- SSPERK$(4,3)$: $\tilde b_2=\frac14\mathbf 1$ supersedes the earlier
  $[\frac13,\frac13,\frac13,0]$ by a larger stability region; for SSPERK$(n^2,3)$,
  $n\ge3$, $\tilde b=\frac1{n^2}\mathbf 1$, and no embedding with SSP coefficient
  $n^2-n$ was found (§2.2).
- SSPERK$(10,4)$: no non-defective embedding exists, because one fourth-order
  condition, $b^\top(\frac{c^3}{3!}-\frac{Ac^2}{2!})=0$, holds for every weight vector
  on this $A$; eight rational third-order embeddings are listed, none with SSP
  coefficient 6 (§2.3).

With a PID controller these pairs reach the requested tolerance where classical
second-order pairs do not, cost 30–40% more than Bogacki–Shampine 3(2) at third order,
and beat Dormand–Prince 5(4) on hyperbolic problems for $\mathrm{tol}\ge10^{-4}$ at
fourth order (Fekete et al. 2022, §3.2.2). Ranocha et al. (2022, §5.5.2, Table 4) find
the four-stage third-order pair with $\hat b=\frac14\mathbf 1$ about 50% cheaper than
SSPRK(3,3) or Bogacki–Shampine 3(2) at loose and medium tolerances on the
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md), nearly 50% faster than
Bogacki–Shampine 3(2) on the NASA juncture flow and the most efficient method on the
Imperial Front Wing at spatial degree 2 (§7.2–7.3, Tables 8–9), but its cost grows
sharply at tight tolerances. In a later study of error-based control for
compressible DG, the same pair with the Conde–Fekete–Shadid embedding is usually the
most efficient of four pairs for low-Mach, positivity-critical and strongly
shock-captured problems: 16% fewer right-hand-side evaluations than the five-stage
pair of Ranocha et al. on the Orszag–Tang vortex, and the fewest on both
Kelvin–Helmholtz tests (5478 and 6618 evaluations), one of which cannot be run with
CFL-based control at all; because its coefficients are optimized for $\mathcal C$
and not for the truncation error, it enters the accuracy-limited regime at looser
tolerances than the others (Ranocha et al. 2025, §3, §4.2, §6, §8, Tables 1, 4–5). Step-size control is on [step-size control](/methods/step-size-control.md).

## Beyond Runge–Kutta: downwind, multiderivative, IMEX

- **Downwind operators.** With a downwind approximation $\tilde f$ satisfying
  $\lVert y-h\tilde f(y)\rVert\le\lVert y\rVert$ for $h\le h_{\mathrm{FE}}$, Ketcheson
  built unconditionally SSP implicit methods of order 2, as recalled by Gottlieb et al.
  (2022, §1, Eq. (3)).
- **Two-derivative methods.** Explicit SSP two-derivative methods use a second
  derivative condition $\lVert y+h^2\dot f(y)\rVert\le\lVert y\rVert$ or a Taylor
  series condition $\lVert y+hf(y)+\frac12h^2\dot f(y)\rVert\le\lVert y\rVert$, as
  recalled by Gottlieb et al. (2022, §1, Eqs. (4)–(5)); under either, no implicit
  two-derivative method of order 2 is unconditionally SSP (App. A). Under their new
  *backward derivative condition* Gottlieb et al. obtain unconditionally SSP implicit
  methods of orders 2, 3 and 4; see
  [multiderivative Runge–Kutta methods](/methods/multiderivative-runge-kutta.md).
- **IMEX.** For $f=f^{\mathrm E}+f^{\mathrm I}$, ordinary
  [IMEX Runge–Kutta](/methods/imex-runge-kutta.md) methods do not remove the step
  restriction caused by $f^{\mathrm I}$ for general convex functionals (Gottlieb et
  al. 2022, §3, recalling Higueras and Conde et al.); the multiderivative IMEX methods
  of the same paper are SSP for $h\le rh_{\mathrm{FE}}$ with $r$ the SSP coefficient of
  the explicit part alone (Thm. 2).

## SSP explicit parts in IMEX and low-Mach practice

- **Explicit parts of IMEX pairs.** Several IMEX pairs pair an SSP explicit method with an
  L-stable or stiffly accurate implicit one: SSP-LDIRK2(3,3,2) (SSP second-order explicit
  part), SSP-LDIRK3(3,3,2) and SSP3(4,3,3) (SSPRK(3,3) explicit part), used for radiation
  hydrodynamics and for high-Mach flows
  ([Southworth et al. 2024](/sources/southworth-2024.md), §5.1;
  [Boscheri & Pareschi 2021](/sources/boscheri-2021.md), §3.4.1, Eqs. (79), (81)); the
  tableaux are on [semi-implicit IMEX Runge–Kutta](/methods/semi-implicit-imex-runge-kutta.md).
  No SSP coefficient of a pair is stated in these sources, and the step restriction of the
  stiff part is not lifted (see *Beyond Runge–Kutta* above). Southworth et al. also compare
  with an operator split whose hydrodynamics uses third-order TVD Runge–Kutta (§5).
- **Implicit high order is not $L^\infty$-stable.** Boscheri & Pareschi (2021, §3.6) state
  that high-order implicit schemes "are not $L^\infty$ stable but only $L^2$ stable", so
  their semi-implicit scheme can produce bounded over- and undershoots at strong shocks when
  the explicit CFL condition is violated, which they control with an a-priori flattener that
  blends a first-order and the high-order solution. [Orlando & Bonaventura (2025)](/sources/orlando-2025.md)
  (§3) recall that implicit methods of order above one cannot be unconditionally TVD and that
  this holds for IMEX methods too. Both are consequences of the unconditional-SSP barrier
  above.
- **Explicit relaxation splitting.** [Toh et al. (2026)](/sources/toh-2026.md) (§3) use
  SSP-RK2 (Heun) for the explicit fluxes of extended MHD with an implicit relaxation step at
  every sub-stage, and suggest the Shu–Osher SSPRK(3,3) as a replacement; the coupling to the
  split relaxation step limits the scheme to first order in time in the stiff regime (§3.5;
  see [operator splitting](/methods/operator-splitting.md)).
- **When forward Euler is unstable.** [Kemm (2024)](/sources/kemm-2024.md) (§3.1–3.2) argues
  that SSP theory, for Runge–Kutta and for multistep methods, "hinges on the stability of the
  explicit Euler scheme" and is therefore "not applicable" to low-Mach finite-volume
  solvers whose acoustic dissipation scales with the flow speed: their semi-discrete spectra
  approach the imaginary axis, where forward Euler is unstable. Among explicit methods with
  the minimal number of stages only the third- and fourth-order ones have stability regions
  containing the required hull (§3.3, Fig. 2); in his tests with a nonlinear limiter
  third-order Adams–Bashforth outperforms a three-stage third-order Runge–Kutta method, which
  he attributes to the forward Euler first stage of every explicit Runge–Kutta step. See
  [linear multistep methods](/methods/linear-multistep-method.md).
- **Reference solutions.** SSPRK(3,3) provides the explicit reference runs of Orlando &
  Bonaventura (2025, §5.2–5.3) and Orlando et al. (2025b, §4.3) for low-Mach IMEX tests.

## SSPRK(3,3) as a building block of coupled and asynchronous schemes

The tableau of SSPRK(3,3) is $c=(0,1,\tfrac12)$, $a_{21}=1$,
$a_{31}=a_{32}=\tfrac14$, $b=(\tfrac16,\tfrac16,\tfrac23)$
([Unfer (2021)](/sources/unfer-2021.md), Eq. (106)). Three sources use it
inside a larger time-stepping construction; in none of them is the SSP property of the
whole scheme proved.

- **Positivity inside a splitting.** [Liu & Zhang (2023)](/sources/liu-2023.md) (§2.1,
  §3.1, Eq. (5)) advance the Euler half-steps of a Strang splitting of compressible
  Navier–Stokes with SSPRK(3,3) in Shu–Osher form and a Zhang–Shu positivity limiter at
  every stage: positivity of density and internal energy follows from the convex
  combination of forward Euler steps, each positive under the Gauss–Lobatto CFL bound
  $\frac{h}{\Delta x}\max\lvert\text{wave speed}\rvert\le\frac12\hat\omega$ with
  page-local Gauss–Lobatto weight factor $\hat\omega$ (Eq. (17), cited). This is the
  forward-Euler argument of this page applied to the positivity functional; the viscous
  half of the splitting is implicit and first order, so the full scheme is at most first
  order in time (§1.4) and no temporal convergence is reported. See
  [positivity preservation](/properties/positivity-preservation.md) and
  [operator splitting](/methods/operator-splitting.md).
- **Asynchronous local time stepping.** Unfer (2021, §3.5) builds a third-order
  *asynchronous* Runge–Kutta method ARK3 (the acronym does not mean additive RK here) in
  which every finite-volume cell has its own step. The stage states become parabolic
  extrapolations in time and the conservative states cubic polynomials whose derivatives
  are assembled from face fluxes at three face times; with a global step the scheme
  reverts to SSPRK(3,3) (§3.5.2; with one step size the flux polynomial integrates to the
  weights $\tfrac16,\tfrac16,\tfrac23$, a reader's check recorded on the Source page). A
  formal truncation analysis gives $O(\Delta x^3)$ in smooth regions (§3.5.3). The author
  states: "There is no claim at this point that the SSP property holds for the ARK3
  method"; strong shocks need a fallback to first-order states and per-stage recall of
  cells whose local step dropped (§3.5.2, App. B). On a Mach 10 double Mach reflection
  ARK3 runs 1.98 times faster than synchronous SSPRK(3,3) and shows more slip-line
  roll-ups (§4.5); see [local time stepping](/methods/local-time-stepping.md) and
  [double Mach reflection](/benchmarks/double-mach-reflection.md).
- **Stagewise interface coupling.** [Pulicani et al. (2026)](/sources/pulicani-2026.md)
  (§4.3, Eqs. (54)–(55)) advance an ALE finite-volume fluid with SSPRK(3,3), which they
  state "exhibits a greater stability" than forward Euler with MUSCL, and couple it to an
  implicit [Newmark](/methods/newmark-method.md) structure by solving a Lagrange-multiplier
  interface problem at each of the three stages, with the mid-stage structure velocity
  interpolated linearly. The coupled scheme converges at about second order at fixed CFL
  ($2.087$ in time, $2.064$ in space on a smooth piston problem; $1.41$ for the fluid in a
  coupled piston–rod test), so the third order of the Runge–Kutta method is not observed
  (§5.2–5.3).

## SSP as a proof device beyond Runge–Kutta

The Shu–Osher convex-combination argument transfers any property of a single forward
Euler step to the whole method. [Bassenne et al. (2021)](/sources/bassenne-2021.md)
(§3.1, Lemmas 3.3–3.4, Thm. 3.2) use it for explicit Runge–Kutta methods applied to a
first-order TASE-preconditioned linear problem: one forward Euler step of the
preconditioned problem is the $\theta$-method with $\theta$ equal to the TASE
parameter $\alpha$, unconditionally stable iff $\alpha\ge\frac12$, and a method with
nonnegative Shu–Osher coefficients is then unconditionally stable if
$\alpha\ge\frac12\max\beta_{ij}/\alpha_{ij}$; for linear SSP methods up to order four
this gives $\alpha\ge\frac12$. For four-stage fourth-order methods this uses a linear
SSP realization of the same polynomial, valid for linear constant-coefficient problems
only, since no such method has a nonnegative nonlinear Shu–Osher form (reader's
remark on that source). See [TASE operators](/methods/tase-operators.md).

## Relation to strong stability

SSP assumes the forward Euler condition and then asks nothing of the operator.
[Strong stability](/properties/strong-stability.md) in the sense of Sun and coauthors
asks for $\lVert y_{n+1}\rVert\le\lVert y_n\rVert$ in an inner-product norm for the
linear problem $y'=Ly$ with $\langle Lv,v\rangle\le0$, and makes no forward Euler
assumption. The two meet when $L$ is *coercive*: then forward Euler is contractive for
small $h$, and Gottlieb–Shu–Tadmor showed through the SSP formulation that every linear
Runge–Kutta method is strongly stable, as recalled by
[Sun & Shu (2021)](/sources/sun-2021.md) (§1); Sun, Wei & Wu note that the
truncated-Taylor polynomials of explicit linear Runge–Kutta methods have SSP form
([Sun et al. 2022](/sources/sun-2022.md), §1). For merely seminegative $L$ (a skew
operator from a wave-type semi-discretization, for instance) forward Euler itself
increases the norm, the hypothesis fails for every $h>0$, and SSP and contractivity
arguments "may not be generally applied" (Sun et al. 2022, §1). That regime is handled
by the [energy method](/methods/runge-kutta-energy-method.md).

## Qualifications

- **"Necessary and sufficient."** Fekete et al. (2022, §1.1) call the Shu–Osher convex
  decomposition "a sufficient and necessary condition for the SSP property".
  Necessity holds for the optimal coefficient through the canonical Shu–Osher form
  (the Kraaijevanger characterization above); an arbitrary decomposition can
  underestimate $\mathcal C$.
- **The $2s$ bound.** Gottlieb et al. (2022, §1) attribute the "twice the number of
  stages" bound for implicit SSP Runge–Kutta methods to Ketcheson's downwind paper;
  the reader of that source flags the attribution as unverified, so the bound is
  recorded here as recalled, not as the result of that reference.
- **Unconditional SSP.** Gottlieb et al. (2022, §1) state without qualifier that
  implicit methods preserving the forward Euler condition for every $h$ "cannot
  exist"; their own Appendix A makes clear that the barrier is for order greater than
  one.
- **Embedded SSP coefficient.** Fekete et al. impose SSP conditions on the embedded
  weights, but with local extrapolation the advanced solution is the main method's,
  so the embedded coefficient does not affect the strong stability of $y_{n+1}$; the
  paper does not discuss why it matters.
- **Controllability of SSP pairs.** Ranocha et al. (2022, §5) could not make
  SSPERK$(10,4)$ with the embedded method of Conde, Fekete & Shadid step-size-control
  stable with any PID controller they tested, nor the nine-stage third-order method,
  and they judge the estimator of the four-stage third-order pair unreliable at tight
  tolerances; Fekete et al. (2022, §4) recommend the SSPERK$(10,4)$ pairs
  $\tilde b_1,\tilde b_3,\tilde b_5,\tilde b_8$ on the strength of work-precision tests
  that do not examine step-size-control stability. Which of the eight embeddings
  Ranocha et al. used is not stated, and the test problems differ (WENO
  finite-volume versus entropy-stable spectral elements), so this is recorded as a
  partial disagreement, not a contradiction.
- The SSP coefficients and error measures of the new pairs of Fekete et al. are not
  printed in the version read (arXiv v1); they are deferred to a repository.
- **"Only $L^2$ stable."** Boscheri & Pareschi's (2021, §3.6) statement, attributed to
  Gottlieb, Shu & Tadmor, is sweeping as printed; the SSP theory above gives $L^\infty$ and
  TVD bounds for implicit methods under a step restriction, so it should read "not
  unconditionally". Their explicit-Euler-stage pair SP(1,1,1) is called "stiffly accurate
  and stability preserving" without an SSP coefficient.
- **Kemm's "unstable first stage" thesis.** Kemm's explanation of the Runge–Kutta failures
  is heuristic: the linear stability of a Runge–Kutta step depends only on its stability
  polynomial, his first-order-in-space tests behave as linear theory predicts, and the
  amplification of internal stage perturbations is measured by
  [internal stability](/definitions/internal-stability.md), not by the stability of the
  first stage alone *(reader's remark on that source)*. His claim that SSP theory does not
  apply is correct as a statement about its hypothesis, not a counterexample to it.

# Citations

- [Fekete et al. (2022)](/sources/fekete-2022.md) — §1.1 (Eq. 6, Thms. 1–2, Def. 4, order barrier), §2 (Eqs. 9–11), §2.1–2.3 (SSPERK$(s,2)$, $(n^2,3)$, $(10,4)$ and embeddings), §3.2.2, §4.
- [Gottlieb et al. (2022)](/sources/gottlieb-2022.md) — §1 (Eqs. 2–5, SSP coefficient of implicit methods), §3 and Thm. 2 (IMEX), App. A (unconditional-SSP barrier).
- [Biswas et al. (2025)](/sources/biswas-2025.md) — §2, Thm. 2.7, Cor. 2.8; §3.1.2–3.1.4 (linear SSP coefficient 1); Table 3.2.
- [Ranocha et al. (2022)](/sources/ranocha-2022.md) — §5, §5.5.2, Table 4, §7.2–7.3, App. A (Eqs. A.1–A.2), Suppl. Table 1.
- [Sun & Shu (2021)](/sources/sun-2021.md) — §1 (coercive operators, contractivity).
- [Sun et al. (2022)](/sources/sun-2022.md) — §1 (SSP versus noncoercive problems; Taylor polynomials in SSP form).
- [Farrell et al. (2021)](/sources/farrell-2021.md) — §3.2 (SSP tableau in Irksome).
- [Doehring et al. (2024)](/sources/doehring-2024.md) — §3.1.2, §9.4 (Eq. 9.14), §10.2 (Tables 5–6).
- [Doehring et al. (2025)](/sources/doehring-2025.md) — §2.5 (Eq. 2.15).
- [Ranocha et al. (2025)](/sources/ranocha-2025.md) — §3, §4.1 (Fig. 3), §4.2 (Table 1), §6 (Tables 4–5), §8.
- [Bassenne et al. (2021)](/sources/bassenne-2021.md) — §3.1 (Lemmas 3.3–3.4, Thm. 3.2).
- [Kang & Constantinescu (2022)](/sources/kang-2022.md) — §2.3 (Table 1; MRK2 base method).
- [Kemm (2024)](/sources/kemm-2024.md) — §1, §3.1–3.3 (Figs. 1–2).
- [Boscheri & Pareschi (2021)](/sources/boscheri-2021.md) — §3.4.1 (Eqs. (78)–(81)), §3.6 (Eqs. (104)–(105)); arXiv v1.
- [Toh et al. (2026)](/sources/toh-2026.md) — §3, §3.5.
- [Southworth et al. (2024)](/sources/southworth-2024.md) — §5, §5.1.
- [Orlando & Bonaventura (2025)](/sources/orlando-2025.md) — §3, §5.2–5.3; HAL v2.
- [Orlando et al. (2025b)](/sources/orlando-2025-b.md) — §4.3; arXiv v5.
- [Unfer (2021)](/sources/unfer-2021.md) — §3.5 (Eq. (106)), §3.5.2–3.5.3, App. B, §4.5.
- [Liu & Zhang (2023)](/sources/liu-2023.md) — §1.4, §2.1, §3.1 (Eqs. (5), (17)).
- [Pulicani et al. (2026)](/sources/pulicani-2026.md) — §4.3 (Eqs. (54)–(55)), §5.2–5.3.
