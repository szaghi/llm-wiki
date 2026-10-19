---
type: Method
title: "IMEX and additive Runge–Kutta methods"
description: "Additive Runge–Kutta methods integrate y' = fE + fI with an explicit tableau for the nonstiff part and a diagonally implicit tableau for the stiff part on shared stages; the page gives the scheme, the type I/II/ARS classification, named pairs, GARK and splitting views, SSP, asymptotic-preserving and uniformly accurate variants, solver costs and software practice."
status: established
aliases: [IMEX, ImEx, IMEX-RK, ImEx-ARK, ARK, additive Runge–Kutta, implicit-explicit Runge–Kutta, type I IMEX, type II IMEX, type CK, type ARS, globally stiffly accurate IMEX]
tags: [imex, runge-kutta, stiff, implicit, explicit, asymptotic-preserving]
timestamp: 2026-10-20T01:00:00Z
---

# IMEX and additive Runge–Kutta methods

An implicit–explicit (IMEX) or additive Runge–Kutta (ARK) method integrates
$y'=f^{\mathrm E}(t,y)+f^{\mathrm I}(t,y)$, with $f^{\mathrm E}$ nonstiff and
$f^{\mathrm I}$ stiff, by applying an explicit tableau
$(A^{\mathrm E},b^{\mathrm E},c^{\mathrm E})$ to $f^{\mathrm E}$ and a diagonally
implicit tableau $(A^{\mathrm I},b^{\mathrm I},c^{\mathrm I})$ to $f^{\mathrm I}$, on one
shared set of $s$ stage values. Each stage then needs one implicit solve in
$f^{\mathrm I}$ only, while $f^{\mathrm E}$ is evaluated explicitly. The sources use
IMEX methods as production integrators
([Reynolds et al. 2023](/sources/reynolds-2023.md);
[Gardner et al. 2022](/sources/gardner-2022.md)), as the base of IMEX multirate
methods ([Chinomona & Reynolds 2021](/sources/chinomona-2021.md)), as comparison
baselines ([Roberts et al. 2021](/sources/roberts-2021.md)), as compositions of
Euler steps ([Blanes et al. 2024](/sources/blanes-2024.md)), as the time
discretization of stiff relaxation and kinetic problems
([Gottlieb et al. 2022](/sources/gottlieb-2022.md); [Jin 2022](/sources/jin-2022.md);
[Hu & Shu 2025](/sources/hu-2025.md)), and of low-Mach and all-Mach gas dynamics, MHD
and radiation hydrodynamics ([Orlando & Bonaventura 2025](/sources/orlando-2025.md);
[Orlando et al. 2025b](/sources/orlando-2025-b.md);
[Boscheri & Pareschi 2021](/sources/boscheri-2021.md);
[Birke et al. 2024](/sources/birke-2024.md);
[Boscheri & Thomann 2024](/sources/boscheri-2024.md);
[Southworth et al. 2024](/sources/southworth-2024.md)).

## The scheme

With step $h_n$ and stage values $Y_i$ (Reynolds et al. 2023, eq. 7; Gardner et al.
2022, §2.3; Orlando & Bonaventura 2025, Eqs. (50)–(51); Southworth et al. 2024, Eqs.
(6)–(8)):

$$\begin{aligned}
Y_i&=y_n+h_n\sum_{j=1}^{i-1}a^{\mathrm E}_{ij}f^{\mathrm E}\big(t_n+c^{\mathrm E}_jh_n,Y_j\big)+h_n\sum_{j=1}^{i}a^{\mathrm I}_{ij}f^{\mathrm I}\big(t_n+c^{\mathrm I}_jh_n,Y_j\big),\qquad i=1,\dots,s,\\
y_{n+1}&=y_n+h_n\sum_{i=1}^{s}\Big(b^{\mathrm E}_if^{\mathrm E}\big(t_n+c^{\mathrm E}_ih_n,Y_i\big)+b^{\mathrm I}_if^{\mathrm I}\big(t_n+c^{\mathrm I}_ih_n,Y_i\big)\Big),
\end{aligned}$$

and an embedded solution $\hat y_{n+1}$ uses $\hat b^{\mathrm E}$, $\hat b^{\mathrm I}$
([embedded pairs](/methods/embedded-runge-kutta-pair.md)). $A^{\mathrm E}$ is strictly
lower triangular and $A^{\mathrm I}$ lower triangular, i.e. a
[DIRK](/methods/diagonally-implicit-runge-kutta.md); stage $i$ solves
$Y_i-h_na^{\mathrm I}_{ii}f^{\mathrm I}(t_n+c^{\mathrm I}_ih_n,Y_i)=\text{known data}$.
With a mass matrix, $My'=f^{\mathrm E}+f^{\mathrm I}$ is treated through
$M^{-1}f^{\mathrm E}$ and $M^{-1}f^{\mathrm I}$ with $M$ nonsingular and independent
of $y$ (Reynolds et al. 2023, eqs. 5–6).

**Conventions differ in the sources.** Hu & Shu (2025), Boscheri & Pareschi (2021),
Southworth et al. (2024) and Orlando et al. (2025b) put the tilde on the explicit tableau;
Orlando & Bonaventura (2025) put it on the implicit one; Birke et al. (2024) hat the
explicit one. This page writes superscripts E and I throughout. Names of the form
$(s,\sigma,p)$ give implicit stages, explicit stages and order in the Pareschi–Russo
convention; Ascher–Ruuth–Spiteri names count the implicit stages without the explicit
first one.

**Shared or distinct abscissae.** ARKODE requires the two tables to share $s$ but
allows $c^{\mathrm E}\ne c^{\mathrm I}$, which some SSP IMEX methods need
(Reynolds et al. 2023, §2.2). The base IMEX-ARK of an
[IMEX-MRI-GARK](/methods/imex-mri-gark.md) method must instead be internally
consistent, $c^{\mathrm E}=c^{\mathrm I}$, have an explicit first stage and be
stiffly accurate, a form obtained by padding (Chinomona & Reynolds 2021, §2.1). Hu & Shu
(2025, Thms. 4.3, 5.1) also assume $c^{\mathrm E}=c^{\mathrm I}$ for their uniform-accuracy
proofs, while the type-I pairs of the semi-implicit literature have
$c^{\mathrm E}_1=0\neq c^{\mathrm I}_1$.

## Type I, type II and type ARS

The AP literature classifies a pair by the structure of $A^{\mathrm I}$
(Orlando & Bonaventura 2025, Def. 3.1; Orlando et al. 2025b, Def. 3.1; Hu & Shu 2025,
Eq. (2.9)):

- **type I** (Boscarino–Pareschi–Russo's "type A"): $A^{\mathrm I}$ invertible;
- **type II** ("type CK", after Carpenter–Kennedy):
  $A^{\mathrm I}=\begin{pmatrix}0&0\\ \hat a&\hat A\end{pmatrix}$ with
  $\hat A\in\mathbb R^{(s-1)\times(s-1)}$ invertible ($\hat a$, $\hat A$ page-local), i.e.
  an explicit first implicit stage, as in ESDIRK methods;
- **type ARS**: type II with $\hat a=0$ and $b^{\mathrm I}_1=0$, so the implicit method
  reduces to $s-1$ stages.

A pair is *implicitly stiffly accurate* (ISA) if $a^{\mathrm I}_{sj}=b^{\mathrm I}_j$ and
*globally stiffly accurate* (GSA) if in addition $a^{\mathrm E}_{sj}=b^{\mathrm E}_j$, which
gives $Y_s=y_{n+1}$ (Hu & Shu 2025, footnote 1; see
[stiff accuracy](/properties/stiff-accuracy.md)). Type II allows simplifying assumptions
that ease the order conditions; type I suits the analysis because $A^{\mathrm I}$ is
invertible (Orlando et al. 2025b, §3.1). For a stiffly accurate type-I implicit part with
A-stability, L-stability follows; for a stiffly accurate type-II one it needs the extra
condition

$$R_\infty=\hat e^\top\hat A^{-1}\hat a=0,$$

$\hat e$ the last unit vector of $\mathbb R^{s-1}$, while a stiffly accurate type-ARS part
is L-stable (Orlando & Bonaventura 2025, Eq. (68); Orlando et al. 2025b, Eq. (32); both
citing Boscarino–Russo). Hu & Shu's "condition (A)", that the null vector of $A^{\mathrm I}$
has zero last component, is equivalent to $\hat e^\top\hat A^{-1}\hat a=0$ (Remark 4.2), the
same expression *(compiler observation that the two conditions coincide)*.
The classification decides AP behaviour: in the low-Mach analysis of Orlando &
Bonaventura (2025, Thm. 3.4, §3.1), type I and type ARS are **strongly AP** (any initial
data) and type II non-ARS only **weakly AP** (well-prepared initial pressure). Orlando et
al. (2025b, §4.1–4.4) find type I more robust at low Mach in their semi-implicit
formulation, but only type II stable on a test with time-dependent boundary data.

## Structural views

- **As a GARK method.** An ARK method is the
  [GARK method](/methods/generalized-additive-runge-kutta.md) with
  $A^{\{\mathrm I,\mathrm E\}}=A^{\{\mathrm E,\mathrm E\}}=A^{\mathrm E}$ and
  $A^{\{\mathrm E,\mathrm I\}}=A^{\{\mathrm I,\mathrm I\}}=A^{\mathrm I}$ (Chinomona &
  Reynolds 2021, §2.1, citing Sandu & Günther). Its order conditions are those of
  the two tables plus the coupling conditions in which both tableaux appear along
  one tree.
- **As a composition of Euler steps.** The one-step IMEX Euler method of Ascher
  et al. is the composition of an explicit Euler step on $f^{\mathrm E}$ and an
  implicit Euler step on $f^{\mathrm I}$, and many second-order IMEX schemes have the
  symmetric form implicit half step ∘ explicit step ∘ explicit half step (Blanes
  et al. 2024, §6.1, eq. 6.14). The IMEX trapezoidal Runge–Kutta method is Strang
  splitting of a doubled system (eqs. 6.18–6.21); without restarting the
  auxiliary variable it is symmetric and can be extrapolated. A splitting variant
  of IMEX Crank–Nicolson leapfrog with an explicit midpoint step halves the implicit
  work (eq. 6.17). See [operator splitting](/methods/operator-splitting.md).
- **Linearly implicit use.** When $f^{\mathrm I}$ is linear in $y$, ARKODE performs
  one Newton iteration per implicit stage (Reynolds et al. 2023, §2.2).
- **Semi-implicit (partitioned-argument) form.** When the stiff term is not additively
  separable, the state is duplicated, $y'=\mathcal H(y^{\mathrm E},y^{\mathrm I})$, and an
  IMEX pair with $b^{\mathrm E}=b^{\mathrm I}$ is applied to the two copies; freezing
  coefficients at the explicit copy makes every stage linear. The additive method is the
  case $\mathcal H(u,v)=f^{\mathrm E}(u)+f^{\mathrm I}(v)$. See
  [semi-implicit IMEX Runge–Kutta](/methods/semi-implicit-imex-runge-kutta.md).
- **Stability with a split operator.** For $y'=(L_{\mathrm I}+L_{\mathrm E})y$ (page-local
  matrices) the standard IMEX linear-stability analysis assumes the two parts
  simultaneously diagonalizable, as recalled by
  [Conte et al. (2024)](/sources/conte-2024.md) (§1, §4); they carry the
  generalized-eigenvalue and field-of-values technique of Rosales et al. for unconditional
  stability of IMEX multistep methods over to [TASE](/methods/tase-operators.md)
  Runge–Kutta methods with an inexact Jacobian.

## Named methods in the sources

- **Kennedy–Carpenter ARK methods**, the ARKODE defaults: ARK3(2)4L[2]SA,
  ARK4(3)6L[2]SA and ARK5(4)8L[2]SA, of orders 3, 4, 5 with embeddings 2, 3, 4,
  and ARK4(3)7L[2]SA1 (Reynolds et al. 2023, §2.2). The ESDIRK part of
  ARK5(4)8L[2]SA is ARKODE's default fifth-order DIRK, used for reference
  solutions. ARK3(2)4L[2]SA, with diagonal $\gamma=\frac{1767732205903}{4055673282236}\approx0.4358665215$
  and $c^{\mathrm I}_2=2\gamma$, is type II, stiffly accurate and has $R_\infty=0$; it is the
  third-order scheme of Orlando & Bonaventura (2025, Table 1) and the IMEX-RK(3,3,3) of
  Orlando et al. (2025b, Table 21). Orlando et al. also use a seven-stage type-II
  fourth-order Kennedy–Carpenter (2019) pair with $\gamma=\frac{247}{2000}$, their
  IMEX-RK(6,6,4) (Table 23).
- **ARS(3,4,3)** of Ascher, Ruuth & Spiteri, printed to 40 digits by Chinomona &
  Reynolds (2021, §4.1): with $\gamma_{\mathrm{ARS}}=0.4358665215\ldots$ and
  $\alpha_{\mathrm{ARS}}=0.5529291480\ldots$ (page-local names; the source writes $\eta$,
  $\alpha$), the implicit table is
  $c=(0,\gamma_{\mathrm{ARS}},\tfrac{1+\gamma_{\mathrm{ARS}}}2,1)$ with rows $(0)$,
  $(0,\gamma_{\mathrm{ARS}})$, $(0,\tfrac{1-\gamma_{\mathrm{ARS}}}2,\gamma_{\mathrm{ARS}})$,
  $(0,b_2,b_3,\gamma_{\mathrm{ARS}})$, where $b_2=-\tfrac32\gamma_{\mathrm{ARS}}^2+4\gamma_{\mathrm{ARS}}-\tfrac14$ and
  $b_3=\tfrac32\gamma_{\mathrm{ARS}}^2-5\gamma_{\mathrm{ARS}}+\tfrac54$; both tables share
  $b=(0,b_2,b_3,\gamma_{\mathrm{ARS}})$. It is the base of IMEX-MRI-GARK3a/3b. The
  type-I pairs SA DIRK(3,4,3), IMEX-RK(4,3,3) and I-IMEX(3,4,3) keep these weights and
  diagonal but make the first stage implicit ($a^{\mathrm I}_{11}=\gamma_{\mathrm{ARS}}$);
  they are tabulated on [semi-implicit IMEX Runge–Kutta](/methods/semi-implicit-imex-runge-kutta.md).
- **ARS(2,3,2), ARS(3,4,3), ARK4(3)6L[2]SA** are the IMEX baselines of Roberts et
  al. (2021, §6.2).
- **ARS(2,2,2)**: $c=(0,\gamma,1)$, explicit rows $(\gamma)$, $(\delta,1-\delta)$,
  $b^{\mathrm E}=(\delta,1-\delta,0)$; implicit rows $(0)$, $(0,\gamma)$,
  $(0,1-\gamma,\gamma)$, $b^{\mathrm I}=(0,1-\gamma,\gamma)$; $\gamma=1-\frac{\sqrt2}2$,
  $\delta=1-\frac1{2\gamma}$ (page-local $\delta$); type ARS, GSA (Hu & Shu 2025, App. 7.2).
- **ARS(4,4,3)**: $c=(0,\frac12,\frac23,\frac12,1)$, implicit diagonal $\frac12$,
  $b^{\mathrm E}=(\frac14,\frac74,\frac34,-\frac74,0)$, $b^{\mathrm I}=(0,\frac32,-\frac32,\frac12,\frac12)$;
  GSA, third order but only uniformly second order on relaxation systems (Hu & Shu 2025,
  App. 7.2, §6).
- **BHR(5,5,3)\***: the Boscarino–Russo pair BHR(5,5,3) with $c_4=1.5$ instead of
  $\approx2.3402$; type CK, ISA, not GSA, $\gamma\approx0.435866521508460$,
  $c=(0,2\gamma,2\gamma,1.5,1)$, $b^{\mathrm E}=b^{\mathrm I}$; the only pair proved
  uniformly third order by Hu & Shu (2025, App. 7.2, Thm. 5.1).
- **Calvo–de Frutos–Novo fourth-order pair**: six stages,
  $c=(0,\frac14,\frac34,\frac{11}{20},\frac12,1)$, type ARS with an implicit SDIRK of
  diagonal $\frac14$ on stages 2–6, stiffly accurate, hence L-stable (Orlando & Bonaventura
  2025, Table 2; Orlando et al. 2025b, Table 22, "IMEX-RK(5,5,4)"). Its implicit part is the
  five-stage L-stable SDIRK4 of Hairer–Wanner padded with an explicit first stage
  *(reader's identification, recorded on the Source pages)*.
- **IMEX-RK(2,2,2) of Giraldo, Kelly & Constantinescu** as printed by Orlando et al.
  (2025b, Table 19): $c=(0,2-\sqrt2,1)$ for both tables, explicit rows $(2-\sqrt2)$,
  $(\frac12,\frac12)$; implicit rows $(0)$, $(1-\frac{\sqrt2}2,1-\frac{\sqrt2}2)$,
  $(\frac{\sqrt2}4,\frac{\sqrt2}4,1-\frac{\sqrt2}2)$; $b^{\mathrm E}=b^{\mathrm I}$ equal to
  the last implicit row; type II, stiffly accurate.
- **Pairs used in semi-implicit form** (LSDIRK2(2,2,2), H-LDIRK2(2,2,2), SA SSP(3,3,2) =
  SSP-LDIRK2(3,3,2), SSP-LDIRK3(3,3,2), SSP3(4,3,3), the type-I third-order pairs) are
  tabulated on [semi-implicit IMEX Runge–Kutta](/methods/semi-implicit-imex-runge-kutta.md).

## Strong stability and positivity

For a general convex functional, standard IMEX Runge–Kutta methods do not remove
the step restriction coming from the stiff operator (Gottlieb et al. 2022, §3,
citing earlier work). Gottlieb et al. lift it by adding the second
derivative $\dot f^{\mathrm I}=f^{\mathrm I\prime}f^{\mathrm I}$ on the implicit diagonal,
an IMEX [multiderivative](/methods/multiderivative-runge-kutta.md) method:

$$Y_i=y_n+h\sum_{j<i}a^{\mathrm E}_{ij}f^{\mathrm E}(Y_j)+h\sum_{j\le i}a^{\mathrm I}_{ij}f^{\mathrm I}(Y_j)+h^2\sum_{j\le i}\dot a_{ij}\dot f^{\mathrm I}(Y_j),\qquad y_{n+1}=Y_s.$$

**Theorem (Gottlieb et al. 2022, Thm. 2).** Assume forward-Euler conditions on
$f^{\mathrm E}$ (step $h_{\mathrm{FE}}$) and on $f^{\mathrm I}$, and the *backward
derivative condition* $\lVert y-h^2\dot f^{\mathrm I}(y)\rVert\le\lVert y\rVert$ for
$h^2\le\dot\kappa\,h_{\mathrm{FE}}^2$ ($\dot\kappa>0$, page-local). If the method has a
Shu–Osher form with non-negative convex-combination and explicit coefficients,
non-negative diagonal coefficients on $f^{\mathrm I}$ and **non-positive** diagonal
coefficients on $\dot f^{\mathrm I}$, then $\lVert y_{n+1}\rVert\le\lVert y_n\rVert$ for
$h\le\mathcal C h_{\mathrm{FE}}$, with $\mathcal C$ the
[SSP coefficient](/methods/strong-stability-preserving-runge-kutta.md) of the explicit
part, independently of $f^{\mathrm I}$.

Gottlieb et al. derive the 22 order conditions of this three-tableau class up to
order 3 (§3.2) and give a 3-stage second-order method with $\mathcal C=1$ (explicit
part Heun/SSPRK(2,2), against $\mathcal C=0.8125$ for an earlier method of Hu, Shu
& Zhang: a 23% larger step) and a 6-stage third-order method with
$\mathcal C=0.904402174130635$ (§3.3). For stiff kinetic systems with the
structural property $\dot Q=-C\,Q$ they prove positivity for $h\le\mathcal C h_{\mathrm{FE}}$
uniformly in $\varepsilon$ (Prop. 1); see
[positivity preservation](/properties/positivity-preservation.md).

Implicit methods of order above one cannot be unconditionally TVD, and Orlando &
Bonaventura (2025, §3) recall that this holds for IMEX methods too; their low-Mach schemes
are therefore not claimed to be $L^\infty$-stable. In radiation hydrodynamics most
third-order IMEX pairs tested by Southworth et al. (2024, §5.1) were unstable, which they
attribute to negative temperatures produced at shocks; only I-IMEX(3,4,3) was robust.

## Relaxation and entropy stability

[Relaxation](/methods/relaxation-runge-kutta.md) extends to IMEX methods by
scaling the combined update,
$y^{\gamma}_{n+1}=y_n+\gamma_nh\sum_i\big(b^{\mathrm E}_if^{\mathrm E}(Y_i)+b^{\mathrm I}_if^{\mathrm I}(Y_i)\big)$,
with $\gamma_n$ the root of the scalar entropy equation built from the same
weighted sum ([Kang & Constantinescu (2022)](/sources/kang-2022.md), §2.2,
Eqs. (12)–(14)). **Prop. 2.1:** if the explicit and implicit parts are each
entropy conservative or stable, the relaxed IMEX method is entropy conservative
or stable (the argument also uses nonnegative weights and $\gamma_n>0$, which
the proposition leaves implicit); for $\eta=\tfrac12\lVert y\rVert^2$,
$\gamma_n=2h\sum_i\big\langle b^{\mathrm E}_if^{\mathrm E}(Y_i)+b^{\mathrm I}_if^{\mathrm I}(Y_i),\,Y_i-y_n\big\rangle/\lVert y_{n+1}-y_n\rVert^2$.
When $b^{\mathrm E}=b^{\mathrm I}$, only the sum $f^{\mathrm E}+f^{\mathrm I}$ has to
be entropy stable (Cor. 2.1.1). See
[entropy stability](/properties/entropy-stability.md).

* **Linearized-flux splitting.** Kang & Constantinescu take
  $f^{\mathrm I}(y)=J(\tilde y)\,y$ with $J(\tilde y)$ the Jacobian of the full
  right-hand side at a reference state $\tilde y$ ($y_n$ or the stage value;
  for Burgers the element mean at $t_n$)
  and $f^{\mathrm E}=f-f^{\mathrm I}$, so each stage needs one linear solve
  (Remark 3, Eq. (11); page-local $\tilde y$). Note their convention: $f$
  explicit, $g$ implicit, tilde on the implicit tableau.
* **Evidence** on [Burgers](/benchmarks/burgers-equation.md) with
  Kennedy–Carpenter ARK methods: relaxed ARK2/ARK3 keep orders 2.00 and
  2.98–3.00 with errors "slightly lower" than plain ARK, while IDT drops one
  order (Tables 2–3). With an entropy-conservative flux, plain ARK loses
  energy slightly, which the authors attribute to IMEX acting as a
  high-frequency filter, while explicit RK2 gains energy; ARK2 also removes
  Gibbs oscillations "dramatically" compared with RK2, the relaxed variants
  less so (Figs. 5–6). Mass is conserved to $O(10^{-14})$ by all IMEX variants
  (Fig. 9).
* **Stiff dispersive problems.** [Biswas & Ketcheson (2023)](/sources/biswas-2023-b.md)
  (§6) relax ARK3(2)4L[2]SA and ARK4(3)6L[2]SA for the energy of a Fourier
  split-form KdV semi-discretization, with the stiff third-derivative term
  implicit. On one soliton the maximum energy change falls from
  $5.38\times10^{-2}$ and $1.05\times10^{-2}$ to about $1.4\times10^{-15}$,
  and the error grows linearly instead of quadratically (Table 1, Fig. 11).
  They present this as the first combination of relaxation with IMEX methods;
  Kang & Constantinescu's earlier work above does not bear the claim out (see
  the Qualifications of the relaxation page).
* **Linear invariants across partitions.** Southworth et al. (2024, §4.3) note that
  conserving a linear invariant is harder for IMEX methods when the parts of the operator
  are evaluated at different stage vectors, and prove discrete total-energy conservation
  for their semi-implicit (LIMEX) methods under a flux-consistency condition.

## Asymptotic-preserving IMEX schemes

For $y'=T(y)+\frac1\varepsilon Q(y)$ with relaxation term $Q$ ($T$, $Q$ page-local),
an IMEX scheme with $Q$ implicit is
[asymptotic preserving](/definitions/asymptotic-preserving-scheme.md) when its
$\varepsilon\to0$ limit at fixed $h$ is a consistent scheme for the limit system.

- Gottlieb et al. (2022, Prop. 1) prove the AP property of their IMEX
  multiderivative methods when every stage carries $Q$ or $\dot Q$
  ($a^{\mathrm I}_{ii}+\lvert\dot a_{ii}\rvert>0$): the limit is the explicit part applied
  to the limit system, with the order of the explicit part. They call their
  schemes "type A" and globally stiffly accurate in the Boscarino–Pareschi–Russo
  classification (Remark 2), although $A^{\mathrm I}$ alone is singular for both
  methods; the classification is extended to the pair $(A^{\mathrm I},\dot A)$.
- Hu & Shu (2025, App. 7.3, Thm. 7.4) show formally for hyperbolic relaxation, with initial
  data in equilibrium to $O(\varepsilon)$, that a type-CK ISA pair is AP with the full order
  in the limit (asymptotically accurate) if it is GSA, as ARS(2,2,2) and ARS(4,4,3) are, or
  if it satisfies condition (A) plus one (order 2) or two (order 3) conditions on
  $b^{\mathrm E}-A^{\mathrm E}_{s\cdot}$; BHR(5,5,3)\* is AP without being GSA.
- Orlando & Bonaventura (2025, §3, Thms. 3.4, 3.7) prove formally that the semi-implicit
  low-Mach Euler scheme (continuity, momentum convection and kinetic-energy flux explicit;
  pressure gradient and enthalpy flux implicit; Eq. (53)) is AP for the single-scale and
  two-scale low-Mach limits for a general equation of state, with stage and update local
  errors $O(h^2)$; type I and ARS strongly, type II weakly. Momentum and energy are coupled
  implicitly into a nonlinear Helmholtz equation for the pressure solved by fixed-point
  iteration. The explicit subsystem is pressureless gas dynamics, only weakly hyperbolic
  (App. A).
- **AP is not asymptotic accuracy.** Orlando & Bonaventura (2025, §3.1) separate AP from
  asymptotic accuracy (order kept as $\mathrm{Ma}\to0$), state that "it is quite
  established that L-stability is necessary to guarantee asymptotic accuracy", and use
  only L-stable implicit parts. Hu & Shu (2025) go further and prove uniform accuracy in
  $\varepsilon$, including the intermediate regime, for a class of pairs; see
  [uniform accuracy of IMEX schemes](/results/uniform-accuracy-relaxation-systems.md).
- Boscheri & Pareschi (2021, §3.4.1) and Boscheri & Thomann (2024, §3.3) call a stiffly
  accurate implicit part "crucial for assuring asymptotic consistency and accuracy" and use
  only such pairs in the stiff limit; the semi-implicit forms are on
  [semi-implicit IMEX Runge–Kutta](/methods/semi-implicit-imex-runge-kutta.md).
- Southworth et al. (2024, §5.1) attribute to Pareschi & Russo a proof that AP IMEX
  schemes for stiff relaxation must have no explicit stage in the implicit method, and
  choose their pairs accordingly. Hu & Shu (2025, App. 7.3) call the type-ARS pairs
  ARS(2,2,2) and ARS(4,4,3) AP for hyperbolic relaxation, which contradicts the statement as
  printed; Orlando & Bonaventura (2025) find type-ARS pairs strongly AP in the low-Mach
  limit. The contradiction is recorded on
  [asymptotic-preserving scheme](/definitions/asymptotic-preserving-scheme.md).
- Jin (2022, §5.1) reviews the first-order IMEX scheme of
  [BGK penalization](/methods/bgk-penalization.md), whose implicit BGK term is
  inverted explicitly through conservation, and (p. 457) the Boscarino–Pareschi–Russo
  reformulation of the diffusive limit that turns the limiting scheme into an
  implicit diffusion discretization with $h=\mathcal O(\Delta x)$ instead of
  $\mathcal O(\Delta x^2)$. He points to high-order IMEX schemes for hyperbolic
  relaxation (Pareschi & Russo; Dumbser et al.) and to a uniform-accuracy proof
  for IMEX-BDF (Hu & Shu) (§6.1), and to an all-speed low-Mach splitting with the
  stiff pressure gradient implicit (§6.5).
- Order reduction in the intermediate regime $\varepsilon\sim h$ is observed by
  Gottlieb et al. (2022, Remark 4, §3.5) and, for ARS(4,4,3), by Hu & Shu (2025, §6,
  Fig. 1); Orlando & Bonaventura (2025, §5.1, Table 5) attribute part of a loss of the
  $O(\mathrm{Ma}^2)$ density scaling of their fourth-order pair below $\mathrm{Ma}=10^{-4}$
  to order reduction. See [order reduction](/definitions/order-reduction.md).
- **Operator splitting instead of IMEX.** [Toh et al. (2026)](/sources/toh-2026.md) (§3,
  §3.5) treat the stiff relaxation of extended MHD with an explicit SSP-RK2 step and a
  first-order implicit relaxation step at every sub-stage, which is AP but only first order
  in time in the stiff regime; they name IMEX as the route to higher order (§5). See
  [operator splitting](/methods/operator-splitting.md).

## Cost and solver practice

- **Evaluation counts.** $f^{\mathrm E}$ is evaluated once per stage, $f^{\mathrm I}$
  once per nonlinear iteration, so an expensive nonstiff term favours IMEX over a
  fully implicit DIRK (Reynolds et al. 2023, §5.1.2, Table 1). On a
  [Brusselator](/benchmarks/brusselator.md) with $10^{-4}$/$10^{-9}$ tolerances, the
  maximum-order implicit predictor reduces all integrator statistics by at least
  32% against the trivial one for DIRK and for IMEX with implicit reactions; with
  explicit reactions and one Newton iteration the cutoff predictor gains up to 20%
  ([dense output](/methods/dense-output.md),
  [implicit stage solvers](/methods/implicit-stage-solvers.md)).
- **Task-local nonlinear solves.** When the implicit part is pointwise local (e.g.
  reactions), a custom nonlinear solver can solve each MPI task's block
  independently. On a stiff advection–reaction Brusselator with ARKODE's default
  third-order IMEX method it is 4.2–7.9× faster than a global Newton–GMRES solve
  on 40–10,240 MPI tasks (Gardner et al. 2022, §6.1, Fig. 3).
- **Picard iteration for the low-Mach pressure.** Orlando et al. (2025b, §3.2, Tables
  16–17) solve the nonlinear Helmholtz equation of the IMEX low-Mach scheme by a Picard
  iteration with lagged enthalpy rather than Newton: 1, 3, 5 iterations at
  $\mathrm{Ma}=10^{-1}$ for tolerances $10^{-4},10^{-6},10^{-10}$, one iteration at
  $\mathrm{Ma}=10^{-4}$, with first-order convergence (observed rate about 1).
- **Step-size limits.** IMEX keeps an explicit-like step restriction from the
  explicit part: on the 500-inverter chain its largest stable step is
  $3.2$–$5.2\times10^{-3}$ against $5.2$–$7.1\times10^{-2}$ for implicit single-rate
  and compound-fast multirate methods (Roberts et al. 2021, Table 6.1). At orders
  2–3 compound-fast [multirate GARK](/methods/multirate-gark.md) is slightly more
  efficient than the IMEX baselines; at order 4 they are similar. In low-Mach flow the
  restriction is on the material speed only: Orlando & Bonaventura (2025, §5.2–5.5) run at
  acoustic Courant numbers up to about 19,300 (open tube, stiffened gas), where an explicit
  scheme "would require a time step around 65000 times smaller".
- **IMEX versus multirate at scale.** In a 3D reacting-flow weak-scaling test the
  IMEX ARK4(3)7L[2]SA1 run is far slower than an explicit-MIS multirate run,
  because every rank-local linear solve inside each Newton iteration triggers a
  global synchronization (Reynolds et al. 2023, §5.2;
  [multirate infinitesimal methods](/methods/multirate-infinitesimal-methods.md)).

## Qualifications

- Blanes et al. (2024, §6.2, §6.4) note that splitting methods with real positive
  coefficients are limited to order 2 on parabolic problems; this barrier concerns
  splittings of exact sub-flows, not additive Runge–Kutta methods, for which
  higher orders are routine (the Kennedy–Carpenter methods above reach order 5).
- Gardner et al. print the abscissa index of the update and of the stage equation
  as $c_j$ inside sums over $i$ (§2.3, §2.5); the formulas above use the intended
  index.
- **Printed tableau of Orlando & Bonaventura (2025), Table 1.** The implicit entry
  $a^{\mathrm I}_{32}$ is printed as $+\frac{640167445237}{6845629431997}$; the row then
  sums to 0.787 instead of $c_3=\frac35$ and $R_\infty\approx0.957$ instead of the stated
  $0$. With a minus sign the row sum is $\frac35$ and $R_\infty\approx0$ *(reader's and
  compiler's check)*, as in the same tableau printed by Orlando et al. (2025b, Table 21).
- **Type II with ill-prepared data.** Orlando & Bonaventura's Table 1 pair is type II
  non-ARS, hence by their own §3.1 only weakly AP, yet their colliding-pulse and
  density-layering tests start from pressure data that are not well prepared; the paper
  does not comment.
- **Naming.** Orlando et al. (2025b, §3.1) define $(s,\sigma,p)$ as the numbers of
  implicit and explicit function evaluations, but their IMEX-RK(3,3,3) has four explicit
  stages and IMEX-RK(6,6,4) seven stages; the names follow neither count consistently.
- **"L-stability is necessary."** Orlando & Bonaventura's statement (§3.1) is attributed to
  Pareschi–Russo without proof; Hu & Shu's uniform-accuracy hypotheses (ISA plus condition
  (A)) imply the same $R_\infty=0$ condition for their pairs, so the two sources agree on
  the schemes they treat *(compiler observation)*.

# Citations

- [Reynolds et al. (2023)](/sources/reynolds-2023.md) — §2.2 (eqs. 5–7), §3.4, §5.1.2 (Table 1), §5.2 (Fig. 3).
- [Gardner et al. (2022)](/sources/gardner-2022.md) — §2.3, §2.5, §6.1 (Fig. 3).
- [Chinomona & Reynolds (2021)](/sources/chinomona-2021.md) — §2.1, §4.1 (ARS(3,4,3)).
- [Roberts et al. (2021)](/sources/roberts-2021.md) — §6.2 (Fig. 6.2, Table 6.1).
- [Gottlieb et al. (2022)](/sources/gottlieb-2022.md) — §3 (Thm. 2, order conditions p. 11, §3.3 methods, Prop. 1, Remarks 2 and 4).
- [Jin (2022)](/sources/jin-2022.md) — §5.1 (eq. 5.2), p. 457 (eqs. 5.37–5.38), §6.1, §6.5.
- [Blanes et al. (2024)](/sources/blanes-2024.md) — §6.1 (eqs. 6.14–6.21), §6.2, §6.4.
- [Kang & Constantinescu (2022)](/sources/kang-2022.md) — §2.2 (Eqs. (10)–(14), Prop. 2.1, Cor. 2.1.1), Remark 3 (Eq. (11)), §3.2 (Tables 2–3, Figs. 5–9).
- [Biswas & Ketcheson (2023)](/sources/biswas-2023-b.md) — §6 (Eq. (34), Table 1, Fig. 11), §7.
- [Hu & Shu (2025)](/sources/hu-2025.md) — §2 (Eqs. (2.6)–(2.9), footnote 1), Remark 4.2, Thms. 4.3, 5.1, §6 (Fig. 1), App. 7.2–7.3 (Thm. 7.4); arXiv v1.
- [Orlando & Bonaventura (2025)](/sources/orlando-2025.md) — §3 (Eqs. (48)–(53), Def. 3.1, Thms. 3.4, 3.7, Eq. (68)), §5 (Tables 1–2, 5), §5.2–5.5, App. A; HAL v2.
- [Orlando et al. (2025b)](/sources/orlando-2025-b.md) — §3.1 (Eqs. (28)–(32), Defs. 3.1–3.2), §3.2 (Tables 16–17), §4.1–4.4, App. A (Tables 19–23); arXiv v5.
- [Southworth et al. (2024)](/sources/southworth-2024.md) — §2.1 (Eqs. (6)–(8)), §4.3, §5.1.
- [Boscheri & Pareschi (2021)](/sources/boscheri-2021.md) — §3.4.1; arXiv v1.
- [Boscheri & Thomann (2024)](/sources/boscheri-2024.md) — §3.3; arXiv v1.
- [Birke et al. (2024)](/sources/birke-2024.md) — §3.3.1 (Table 1); arXiv v1.
- [Conte et al. (2024)](/sources/conte-2024.md) — §1, §4 (split test equation, simultaneous diagonalizability); arXiv v1.
- [Toh et al. (2026)](/sources/toh-2026.md) — §3, §3.5, §5.
