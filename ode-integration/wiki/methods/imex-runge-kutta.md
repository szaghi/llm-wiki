---
type: Method
title: "IMEX and additive Runge–Kutta methods"
description: "Additive Runge–Kutta methods integrate y' = fE + fI with an explicit tableau for the nonstiff part and a diagonally implicit one for the stiff part on shared stages: the scheme, type I/II/ARS classes, order conditions, named, optimal-efficiency and accelerated pairs, GARK views, SSP, invariant-domain-preserving and asymptotic-preserving variants, and solver practice."
status: established
aliases: [IMEX, ImEx, IMEX-RK, ImEx-ARK, ARK, additive Runge–Kutta, implicit-explicit Runge–Kutta, type I IMEX, type II IMEX, type CK, type ARS, globally stiffly accurate IMEX, AIMEX, accelerated IMEX, IMEX3,2]
tags: [imex, runge-kutta, stiff, implicit, explicit, asymptotic-preserving]
timestamp: 2026-10-29T18:13:00Z
---

# IMEX and additive Runge–Kutta methods

An implicit–explicit (IMEX) or additive Runge–Kutta (ARK) method integrates
$y'=f^{\mathrm E}(t,y)+f^{\mathrm I}(t,y)$, with $f^{\mathrm E}$ nonstiff and
$f^{\mathrm I}$ stiff, by applying an explicit tableau
$(A^{\mathrm E},b^{\mathrm E},c^{\mathrm E})$ to $f^{\mathrm E}$ and a diagonally
implicit tableau $(A^{\mathrm I},b^{\mathrm I},c^{\mathrm I})$ to $f^{\mathrm I}$, on one
shared set of $s$ stage values. Each stage then needs one implicit solve in
$f^{\mathrm I}$ only, while $f^{\mathrm E}$ is evaluated explicitly. Two founding papers
construct named families of pairs:
[Ascher et al. (1997)](/sources/ascher-1997.md) build the ARS pairs for
convection–diffusion, with convection explicit and diffusion implicit, motivated by the
step-size restrictions of IMEX multistep schemes (§1), and
[Kennedy & Carpenter (2003)](/sources/kennedy-2003.md) analyse $N$-additive methods in
general and build the
[ARK3(2)4L[2]SA, ARK4(3)6L[2]SA and ARK5(4)8L[2]SA pairs](/methods/kennedy-carpenter-ark-methods.md)
for convection–diffusion–reaction systems with stiff chemistry (§1–6). The sources use
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
[Southworth et al. 2024](/sources/southworth-2024.md)). Further uses: many-stage pairs that
accelerate locally stiff, mesh-induced problems
([Vermeire & Hedayati Nasab 2021](/sources/vermeire-2021.md)), the high-order update of an
invariant-domain-preserving limiter ([Ern & Guermond 2023](/sources/ern-2023.md)), and
baselines for fully implicit–explicit polynomial methods
([Buvoli & Southworth 2023](/sources/buvoli-2023.md)).

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
of $y$ (Reynolds et al. 2023, eqs. 5–6). Kennedy & Carpenter (2003, §2.1, Eqs. (2)–(4))
write the general $N$-additive form $y'=\sum_{\nu=1}^Nf^{[\nu]}(y)$ with one tableau per term
on shared stage values ($[\nu]$ page-local), and use $N=2$, an explicit method plus an
[ESDIRK](/methods/diagonally-implicit-runge-kutta.md), for their pairs (§3).

**The Ascher–Ruuth–Spiteri form.** Ascher et al. (1997, §2, Eqs. (2.1a–e)) couple an
$s$-stage DIRK for $f^{\mathrm I}$ with an $(s+1)$-stage explicit method for
$f^{\mathrm E}$. The DIRK is padded with a zero first row and column, so that the two tableaux
share the abscissae $c=(0,c_1,\dots,c_s)$ of the padded form, which "simplifies significantly
the form of the order conditions … due to coupling" (§2). Each step evaluates
$f^{\mathrm E}(y_n)$, then for $i=1,\dots,s$ solves one implicit stage in $f^{\mathrm I}$
alone and evaluates $f^{\mathrm E}$ at the new stage. They single out two sub-families:

1. explicit weights equal to the padded implicit weights (so the explicit first weight is 0),
   giving $y_{n+1}=y_n+h\sum_{j=1}^sb_j\big(f^{\mathrm I}(Y_j)+f^{\mathrm E}(Y_j)\big)$ over the
   $s$ implicit stages (Eq. (2.2));
2. the last explicit weight zero and both weight vectors equal to the last rows of their
   tableaux (Eq. (2.3)), "implying that the implicit scheme is stiffly accurate and
   $c_s=1$", so that $y_{n+1}$ is the last stage (Eq. (2.4)), "useful for very stiff
   problems".

With the Jacobian of $f^{\mathrm I}$ frozen at $t_n$, the stage matrix
$I-ha^{\mathrm I}_{ii}J^{\mathrm I}$ is the same for all stages iff the diagonal is constant;
the search allowed varying diagonals, but every recommended pair is SDIRK-based "since there
were sufficient excess degrees of freedom" (§2).

**Conventions differ in the sources.** Hu & Shu (2025), Boscheri & Pareschi (2021),
Southworth et al. (2024) and Orlando et al. (2025b) put the tilde on the explicit tableau;
Orlando & Bonaventura (2025) put it on the implicit one; Birke et al. (2024) hat the
explicit one; Vermeire & Hedayati Nasab (2021) hat the implicit one, and Ern & Guermond
(2023) write superscripts e and i. Ascher et al. (1997) call the explicit part $f$ and the
implicit part $g$, put the hat on the explicit tableau and the tilde on the padded implicit
one (§2); Kennedy & Carpenter (2003) write superscripts $[E]$ and $[I]$. This page writes
superscripts E and I throughout. Names of the form
$(s,\sigma,p)$ give implicit stages, explicit stages and order in the Pareschi–Russo
convention; Ascher–Ruuth–Spiteri names count the implicit stages without the explicit
first one. In Ascher et al. (1997, §2, p. 155) $\sigma$ is the number of explicit stages
evaluated: $\sigma=s+1$ in sub-family 1 and $\sigma=s$ in sub-family 2, where the
last explicit stage is not needed, so (2,2,2) and (4,4,3) count $\sigma=s$ although their
explicit tableaux are printed with $s+1$ rows. Kennedy & Carpenter (2003, §3) name their
pairs ARK$p(\hat p)s$S[$q$]X: orders of the main and embedded methods, stages, a stability
label, the stage order of the implicit part and other properties (see
[Kennedy–Carpenter ARK methods](/methods/kennedy-carpenter-ark-methods.md)). Two further labels occur: IMEX$s,p$ (explicit stages, order) in Vermeire &
Hedayati Nasab (2021, §2.1), and IMEX$(s,p;c_{\mathrm{eff}})$ with an efficiency ratio as
third entry in Ern & Guermond (2023, §4), which clashes with the Ascher–Ruuth–Spiteri
triple.

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

The two founding papers use no "type" terminology. Ascher et al. (1997, §2) pad every DIRK
with a zero first row and column, which has the type-ARS structure *(compiler check, not in the
sources: the padded first column and first implicit weight are zero)*, and classify their pairs by
the sub-families 1 and 2 above; in sub-family 2 the explicit first weight need not vanish
((2,2,2) has $b^{\mathrm E}_1=\delta\neq0$, §2.6). Kennedy & Carpenter (2003, §3) pair an
explicit method with an ESDIRK whose first stage is explicit and whose second row is
$(\gamma,\gamma)$, i.e. a nonzero first column, the structure the AP literature calls type II
or type CK *(compiler check, not in the sources: $a^{\mathrm I}_{1j}=0$, $a^{\mathrm I}_{21}=\gamma\neq0$)*.

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

- **As a partitioned or splitting method.** Ascher et al. (1997, §1, Eq. (1.3)) write the
  pair as a partitioned Runge–Kutta method for $y=v+w$, $v'=f^{\mathrm E}(v+w)$,
  $w'=f^{\mathrm I}(v+w)$, where $v$ and $w$ need not be known individually, and add that IMEX
  Runge–Kutta schemes "can also be seen as a particular class of splitting methods".
- **Hamiltonian use.** For a separable Hamiltonian with $f^{\mathrm E}=(H_p,0)^\top$ and
  $f^{\mathrm I}=(0,-H_q)^\top$, the IMEX midpoint pair (1,2,2) below is explicit, "can also be
  shown to be symplectic", and is identical to the leap-frog/Verlet scheme, which Ascher et al.
  (1997, §2.3, Example 2) derive; see [symplecticity](/properties/symplecticity.md).
- **As a GARK method.** An ARK method is the
  [GARK method](/methods/generalized-additive-runge-kutta.md) with
  $A^{\{\mathrm I,\mathrm E\}}=A^{\{\mathrm E,\mathrm E\}}=A^{\mathrm E}$ and
  $A^{\{\mathrm E,\mathrm I\}}=A^{\{\mathrm I,\mathrm I\}}=A^{\mathrm I}$ (Chinomona &
  Reynolds 2021, §2.1, citing Sandu & Günther). Its order conditions are those of
  the two tables plus the coupling conditions in which both tableaux appear along
  one tree. Kennedy & Carpenter (2003, §2.1.1, App. A), after Araújo, Murua and
  Sanz-Serna, state them with $N$-coloured trees and count the order conditions of an
  $N$-additive method at each order through the generating function of their Eq. (6).
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
- **As an NPRK method.** A
  [nonlinearly partitioned Runge–Kutta method](/methods/nonlinearly-partitioned-runge-kutta.md)
  applied to an additive partition $F(u,v)=f^{\mathrm I}(u)+f^{\mathrm E}(v)$ is the
  additive method built from its two underlying tableaux, with shared abscissae
  ([Buvoli & Southworth (2025)](/sources/buvoli-2025.md), §4.1, Eq. (4.5)). Their IMEX
  members are diagonally implicit in the first argument and explicit in the second
  (Table 4.1). On the partitioned Dahlquist problem an NPRK method has the additive
  two-variable stability function $R(z_1,z_2)$; Buvoli & Southworth call an IMEX method
  A-stable (L-stable) "in the stiff $z_1$ limit" when
  $\lim_{\lvert z_1\rvert\to\infty}\lvert R(z_1,z_2)\rvert\le1$ ($=0$), and add stability
  in the coupled stiff limit, where the explicit argument is a bounded fraction as stiff as
  the implicit one (§4.5, Eqs. (4.18), (4.22)–(4.27)); details on
  [stability function](/definitions/stability-function.md). In their Burgers tests
  with a conservative partition, which puts stiffness in the explicit argument, only the
  methods stable in the coupled stiff limit survive large steps (§7.1, Fig. 7.1).
- **No fully implicit implicit part.** Buvoli & Southworth (2023, §1) state that IMEX
  Runge–Kutta methods cannot be built on fully implicit implicit tableaux, "since the
  explicit stages would be nonlinearly coupled to the fully implicit stages". Their
  [FIMEX polynomial methods](/methods/polynomial-time-integrators.md) obtain a Radau IIA
  implicit part by integrating, for the explicit part, an interpolant of the previous
  step's derivatives instead of explicit stages; written as an additive general linear
  method they have $3(s+1)$ inputs and $s+1$ stages (supplement SM4).
- **Stability with a split operator.** For $y'=(L_{\mathrm I}+L_{\mathrm E})y$ (page-local
  matrices) the standard IMEX linear-stability analysis assumes the two parts
  simultaneously diagonalizable, as recalled by
  [Conte et al. (2024)](/sources/conte-2024.md) (§1, §4); they carry the
  generalized-eigenvalue and field-of-values technique of Rosales et al. for unconditional
  stability of IMEX multistep methods over to [TASE](/methods/tase-operators.md)
  Runge–Kutta methods with an inexact Jacobian.

## Order conditions with shared weights and abscissae

When $b^{\mathrm E}=b^{\mathrm I}=b$ and $c^{\mathrm E}=c^{\mathrm I}=c$ with
$A^{\mathrm E}\mathbf 1=A^{\mathrm I}\mathbf 1=c$, the additive order conditions shrink.
Ern & Guermond (2023, §4.1, Eqs. (64)–(70)), after Pareschi–Russo and Kennedy–Carpenter,
list them up to order 4 (products of vectors componentwise):

- order 2: $b^\top\mathbf 1=1$, $b^\top c=\tfrac12$;
- order 3: $b^\top c^2=\tfrac13$, $b^\top A^{\mathrm E}c=b^\top A^{\mathrm I}c=\tfrac16$;
- order 4: $b^\top c^3=\tfrac14$, $b^\top A^{\mathrm X}c^2=\tfrac1{12}$,
  $b^\top(A^{\mathrm X})^2c=\tfrac1{24}$, $b^\top\bigl(c\,A^{\mathrm X}c\bigr)=\tfrac18$ for
  $\mathrm X\in\{\mathrm E,\mathrm I\}$, and the two coupling conditions
  $b^\top A^{\mathrm E}A^{\mathrm I}c=b^\top A^{\mathrm I}A^{\mathrm E}c=\tfrac1{24}$.

With shared $b$ and $c$ every tree of order at most 4 contributes one of these conditions,
so the list is complete; only the chain tree $b^\top A^{\mathrm X}A^{\mathrm Y}c$ couples
the two tableaux *(compiler check, not in the sources)*. In particular a pair with shared
$b$, $c$ and $b^\top c=\frac12$ is second order with no coupling condition, which covers the
accelerated pairs below.

Kennedy & Carpenter (2003, §2.1.2, Tables 1–4) count the coupling conditions. Without
$b^{\mathrm E}=b^{\mathrm I}$ or $c^{\mathrm E}=c^{\mathrm I}$, $N$ methods couple without
coupling error only to first order; with one of the two, to second order; with both, any
number of third-order methods with the same number of stages couple without coupling error.
With both simplifications a 2-additive method has 2, 13, 63 and 272 coupling conditions at
orders 4, 5, 6 and 7 (Table 4), in agreement with the two order-4 coupling conditions above.
An $N$-additive method has at most $Ns(s+1)$ independent coefficients (§2.1.2).

## Named methods in the sources

- **Kennedy–Carpenter ARK methods**, the ARKODE defaults: ARK3(2)4L[2]SA,
  ARK4(3)6L[2]SA and ARK5(4)8L[2]SA, of orders 3, 4, 5 with embeddings 2, 3, 4,
  and ARK4(3)7L[2]SA1 (Reynolds et al. 2023, §2.2). The first three are constructed in
  Kennedy & Carpenter (2003, §4–6, App. D), with shared $b$, $\hat b$, $c$, an L-stable,
  stiffly accurate, stage-order-2 ESDIRK and error-free coupling to full order; ARK4(3)7L[2]SA1
  is not in that paper. Coefficients, design conditions and tests are on
  [Kennedy–Carpenter ARK methods](/methods/kennedy-carpenter-ark-methods.md). The ESDIRK part of
  ARK5(4)8L[2]SA is ARKODE's default fifth-order DIRK, used for reference
  solutions. ARK3(2)4L[2]SA, with diagonal $\gamma=\frac{1767732205903}{4055673282236}\approx0.4358665215$
  and $c^{\mathrm I}_2=2\gamma$, is type II, stiffly accurate and has $R_\infty=0$; it is the
  third-order scheme of Orlando & Bonaventura (2025, Table 1) and the IMEX-RK(3,3,3) of
  Orlando et al. (2025b, Table 21), which both attribute to Kennedy and Carpenter (the match
  with ARK3(2)4L[2]SA by its diagonal and abscissae is a *compiler check, not in
  the sources*). Kennedy & Carpenter (2003, App. D) print for ARK3(2)4L[2]SA the same
  $\gamma$, $c=(0,2\gamma,\frac35,1)$ and $a^{\mathrm I}_{32}=-\frac{640167445237}{6845629431997}$,
  with the minus sign (see Qualifications). Orlando et al. also use a seven-stage type-II
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
  $b=(0,b_2,b_3,\gamma_{\mathrm{ARS}})$. It is the base of IMEX-MRI-GARK3a/3b.
  Ascher et al. (1997, §2.7) give the same implicit table, with $\gamma_{\mathrm{ARS}}$ the middle
  root of $6x^3-18x^2+9x-1=0$ and the same weight formulas, and the explicit table as a
  two-parameter family with free $a^{\mathrm E}_{42}$, $a^{\mathrm E}_{43}$ (padded indices),
  $$\begin{aligned}
  a^{\mathrm E}_{31}&=\bigl(1-\tfrac92\gamma+\tfrac32\gamma^2\bigr)a^{\mathrm E}_{42}+\bigl(\tfrac{11}4-\tfrac{21}2\gamma+\tfrac{15}4\gamma^2\bigr)a^{\mathrm E}_{43}-\tfrac72+13\gamma-\tfrac92\gamma^2,\\
  a^{\mathrm E}_{32}&=\bigl(-1+\tfrac92\gamma-\tfrac32\gamma^2\bigr)a^{\mathrm E}_{42}+\bigl(-\tfrac{11}4+\tfrac{21}2\gamma-\tfrac{15}4\gamma^2\bigr)a^{\mathrm E}_{43}+4-\tfrac{25}2\gamma+\tfrac92\gamma^2,\\
  a^{\mathrm E}_{41}&=1-a^{\mathrm E}_{42}-a^{\mathrm E}_{43},
  \end{aligned}$$
  with $\gamma=\gamma_{\mathrm{ARS}}$, the two free entries chosen so that the explicit
  stability polynomial matches the exponential to fourth order, "the same (desirable)
  stability region as all four-stage, fourth-order ERK schemes". They print
  $a^{\mathrm E}_{42}=a^{\mathrm E}_{43}=0.5529291479$, $a^{\mathrm E}_{31}=0.3212788860$,
  $a^{\mathrm E}_{32}=0.3966543747$, $a^{\mathrm E}_{41}=-0.105858296$; Chinomona & Reynolds
  print $\alpha_{\mathrm{ARS}}=0.5529291480\ldots$ to 40 digits. The pair is in sub-family 1
  ($b^{\mathrm E}=b^{\mathrm I}$) and third order. The
  type-I pairs SA DIRK(3,4,3), IMEX-RK(4,3,3) and I-IMEX(3,4,3) keep these weights and
  diagonal but make the first stage implicit ($a^{\mathrm I}_{11}=\gamma_{\mathrm{ARS}}$);
  they are tabulated on [semi-implicit IMEX Runge–Kutta](/methods/semi-implicit-imex-runge-kutta.md).
- **ARS(2,3,2), ARS(3,4,3), ARK4(3)6L[2]SA** are the IMEX baselines of Roberts et
  al. (2021, §6.2).
- **ARS(2,3,2)**, the "IMEX3,2" of Vermeire & Hedayati Nasab (2021, Eqs. (19)–(22)):
  implicit part as in ARS(2,2,2) below (the L-stable, stiffly accurate two-stage SDIRK with
  $\gamma=1-\frac1{\sqrt2}$, padded with an explicit first stage), explicit rows $(\gamma)$,
  $(1-a^{\mathrm E}_{32},a^{\mathrm E}_{32})$ and $b^{\mathrm E}=b^{\mathrm I}=(0,1-\gamma,\gamma)$.
  The commonly used $a^{\mathrm E}_{32}=1+\frac{2\sqrt2}3$ (after Persson) is Ern & Guermond's
  $\delta=-\frac23\sqrt2$ in the rows $(\gamma)$, $(\delta,1-\delta)$ (2023, Eq. (78)); the
  explicit stability polynomial is $1+z+\frac{z^2}2+a^{\mathrm E}_{32}\gamma^2z^3$ *(compiler
  checks, not in the sources)*. Ascher et al. (1997, §2.5) print the explicit rows $(\gamma)$,
  $(\delta,1-\delta)$ with $\delta=-2\sqrt2/3$, chosen "to match the terms of the exponential
  in the stability function up to third order", which gives the stability region of a
  three-stage third-order explicit method; the pair is second order, sub-family 1.
- **ARS(2,2,2)**: $c=(0,\gamma,1)$, explicit rows $(\gamma)$, $(\delta,1-\delta)$,
  $b^{\mathrm E}=(\delta,1-\delta,0)$; implicit rows $(0)$, $(0,\gamma)$,
  $(0,1-\gamma,\gamma)$, $b^{\mathrm I}=(0,1-\gamma,\gamma)$; $\gamma=1-\frac{\sqrt2}2$,
  $\delta=1-\frac1{2\gamma}$ (page-local $\delta$); type ARS, GSA (Hu & Shu 2025, App. 7.2).
  The same coefficients are printed by Ascher et al. (1997, §2.6), as a sub-family-2 pair of
  second order.
- **ARS(4,4,3)**: $c=(0,\frac12,\frac23,\frac12,1)$, implicit diagonal $\frac12$,
  $b^{\mathrm E}=(\frac14,\frac74,\frac34,-\frac74,0)$, $b^{\mathrm I}=(0,\frac32,-\frac32,\frac12,\frac12)$;
  GSA, third order but only uniformly second order on relaxation systems (Hu & Shu 2025,
  App. 7.2, §6).
  The full tableau, printed by [Tan et al. (2022)](/sources/tan-2022.md) (Eq. (2.17)) and
  [Tan et al. (2025)](/sources/tan-2025.md) (Eq. (3.5)): explicit rows $(\frac12)$,
  $(\frac{11}{18},\frac1{18})$, $(\frac56,-\frac56,\frac12)$, $(\frac14,\frac74,\frac34,-\frac74)$;
  implicit rows $(0)$, $(0,\frac12)$, $(0,\frac16,\frac12)$, $(0,-\frac12,\frac12,\frac12)$,
  $(0,\frac32,-\frac32,\frac12,\frac12)$; both weight vectors equal the last rows, so
  $y_{n+1}$ is the last stage, and with a constant linear implicit operator all four implicit
  stages solve with the same matrix $I-\frac h2L$. Neither paper names the pair:
  Tan et al. (2022) take it from Wang, Zhang, Wang & Shu (2020) and Tan et al. (2025) call it
  "a third order IMEX Runge-Kutta method introduced in" Ascher, Ruuth & Spiteri; its
  identification as ARS(4,4,3) rests on an entry-by-entry comparison with Hu & Shu's
  ARS(4,4,3) data in the previous item *(compiler check)*. Ascher et al. (1997, §2.8) print
  the same explicit and implicit rows, entry by entry, as their (4,4,3) pair; they fix the
  free choices $c_1=\frac12$, $c_3=\frac12$, $b_4=\frac12$ (unpadded implicit indices) and
  $a^{\mathrm E}_{43}=\frac12$, choose a diagonal "close to that of the four-stage,
  fourth-order, L-stable DIRK", and report that "no pair consisting of a three-stage, L-stable
  DIRK and a four-stage ERK satisfying (2.3) with a combined third-order accuracy could be
  found". Tan et al. use it as the integrator of the
  [explicit–implicit–null method](/methods/explicit-implicit-null-method.md), with an
  order asserted, not verified, in time.
- **The other Ascher–Ruuth–Spiteri pairs** (Ascher et al. 1997, §2.1–2.4; padded tableaux,
  shared $c$):
  - (1,1,1), forward–backward Euler: $y_{n+1}=y_n+h\big(f^{\mathrm E}(y_n)+f^{\mathrm I}(y_{n+1})\big)$,
    "the linear one-step IMEX" scheme, sub-family 2;
  - (1,2,1): $Y_1=y_n+hf^{\mathrm I}(Y_1)+hf^{\mathrm E}(y_n)$,
    $y_{n+1}=y_n+h\big(f^{\mathrm I}(Y_1)+f^{\mathrm E}(Y_1)\big)$, one extra explicit evaluation,
    sub-family 1;
  - (1,2,2), implicit–explicit midpoint: $c=(0,\frac12)$, explicit midpoint for
    $f^{\mathrm E}$ and implicit midpoint for $f^{\mathrm I}$, second order "because the two
    schemes … are each second-order accurate and" the abscissae agree; it "performs usually
    comparably to the unreasonably popular CNAB" and has better symmetry properties; its implicit
    part has no attenuation at infinity;
  - (2,3,3): implicit part the two-stage third-order DIRK with
    $\gamma=\frac{3+\sqrt3}6$, rows $(\gamma)$, $(1-2\gamma,\gamma)$, $b=(\frac12,\frac12)$, "the
    two-stage, third-order DIRK scheme with the best damping properties", with
    $R(-\infty)=1-\sqrt3\approx-0.7321$; explicit rows $(\gamma)$, $(\gamma-1,2(1-\gamma))$,
    $b^{\mathrm E}=(0,\frac12,\frac12)$; third order, sub-family 1.
- **BHR(5,5,3)\***: the Boscarino–Russo pair BHR(5,5,3) with $c_4=1.5$ instead of
  $\approx2.3402$; type CK, ISA, not GSA, $\gamma\approx0.435866521508460$,
  $c=(0,2\gamma,2\gamma,1.5,1)$, $b^{\mathrm E}=b^{\mathrm I}$; the only pair proved
  uniformly third order by Hu & Shu (2025, App. 7.2, Thm. 5.1).
- **Calvo–de Frutos–Novo fourth-order pair**: six stages,
  $c=(0,\frac14,\frac34,\frac{11}{20},\frac12,1)$, type ARS with an implicit SDIRK of
  diagonal $\frac14$ on stages 2–6, stiffly accurate, hence L-stable (Orlando & Bonaventura
  2025, Table 2; Orlando et al. 2025b, Table 22, "IMEX-RK(5,5,4)"). Its implicit part is the
  five-stage L-stable SDIRK4 of Hairer–Wanner padded with an explicit first stage, as
  [Ern & Guermond (2023)](/sources/ern-2023.md) (§4.4.2) state.
- **IMEX-RK(2,2,2) of Giraldo, Kelly & Constantinescu** as printed by Orlando et al.
  (2025b, Table 19): $c=(0,2-\sqrt2,1)$ for both tables, explicit rows $(2-\sqrt2)$,
  $(\frac12,\frac12)$; implicit rows $(0)$, $(1-\frac{\sqrt2}2,1-\frac{\sqrt2}2)$,
  $(\frac{\sqrt2}4,\frac{\sqrt2}4,1-\frac{\sqrt2}2)$; $b^{\mathrm E}=b^{\mathrm I}$ equal to
  the last implicit row; type II, stiffly accurate.
- **Optimal-efficiency pairs of Ern & Guermond (2023, §4.3–4.4)**, with equidistributed
  abscissae $c_l=(l-1)/s$, singly diagonal EDIRK implicit parts and the order conditions
  above, solved in Julia to tolerances $10^{-15}$–$4\times10^{-16}$:
  - IMEX(3,3;1): Heun's third-order explicit method, $c=(0,\frac13,\frac23)$,
    $b=(\frac14,0,\frac34)$, with a new EDIRK of diagonal $\gamma=\frac12+\frac1{2\sqrt3}\approx0.78867$;
    the second L-stability condition has no solution, so the implicit part is only
    A-stable, with $R(-\infty)=1-\sqrt3$ (Eq. (81));
  - IMEX(4,3;1): $b=(0,\frac23,-\frac13,\frac23)$, L-stable ESDIRK with diagonal
    $0.4358665215084591$; the explicit part is called the only four-stage third-order
    method with equidistributed abscissae that is fourth order on linear problems
    (Eq. (82), asserted);
  - IMEX(5,4;1): L-stable ESDIRK with diagonal $0.57281606248213512$ (Eq. (83));
  - IMEX(6,4;1): L-stable ESDIRK with diagonal $0.2780538411364528$, fifth-order linear
    conditions imposed and $b_4=0.47$ fixed so that the explicit part is dissipative near
    the origin (Eq. (84)).

  Several weights and Butcher entries are negative, which their limiting allows. The
  pairs are designed for [invariant-domain-preserving time stepping](/methods/invariant-domain-preserving-time-stepping.md),
  where the admissible step grows with the efficiency ratio
  $c_{\mathrm{eff}}=1/(s\,\Delta c^{\max})$, $\Delta c^{\max}$ the largest gap between an
  abscissa and its nearest smaller one, $c_{s+1}=1$ included; $c_{\mathrm{eff}}=1$ exactly
  for equidistributed abscissae (§3.3, Eq. (63)). Ern & Guermond also write Strang
  splitting with explicit and implicit midpoint steps as a five-stage IMEX scheme with one
  implicit substep (Remark 4.1), and review Heun with Crank–Nicolson, explicit with
  implicit midpoint, ARS(2,3,2), the Crouzeix–Nørsett two-stage ESDIRK with an ARS explicit
  part, and the Calvo–de Frutos–Novo pair (§4.2–4.4).
- **Pairs used in semi-implicit form** (LSDIRK2(2,2,2), H-LDIRK2(2,2,2), SA SSP(3,3,2) =
  SSP-LDIRK2(3,3,2), SSP-LDIRK3(3,3,2), SSP3(4,3,3), the type-I third-order pairs) are
  tabulated on [semi-implicit IMEX Runge–Kutta](/methods/semi-implicit-imex-runge-kutta.md).

## Accelerated IMEX schemes for locally stiff meshes

[Vermeire & Hedayati Nasab (2021)](/sources/vermeire-2021.md) split by **element**, not by
operator: the few elements whose small size makes the semi-discretization stiff
(refinement, boundary layers) are integrated implicitly, the rest explicitly (§1). Their
cost model (§2.2, Eqs. (16)–(18)) counts per step $e$ explicit and $\hat e$ implicit stage
evaluations on $n$ explicit and $\hat n$ implicit elements (page-local), with wall times
$\mathsf c\ll\hat{\mathsf c}$ per element and evaluation (page-local sans-serif, distinct from
the abscissae). With implicit fraction $\eta_{\mathrm{imp}}=\hat n/(n+\hat n)$ (page-local,
not the entropy) the cost per unit time and element is
$[(1-\eta_{\mathrm{imp}})e\,\mathsf c+\eta_{\mathrm{imp}}\hat e\,\hat{\mathsf c}]/h\approx\eta_{\mathrm{imp}}\hat e\,\hat{\mathsf c}/h$:
the implicit solves dominate the cost while the explicit stability limit sets $h$. More
explicit stages that enlarge the stability region, at fixed $\hat e$, therefore pay off as
long as the implicit solver cost does not grow faster than $h$, which they note it tends to
do.

**AIMEX$s$,2** (§3.1, Eqs. (23)–(29)) starts from ARS(2,3,2) and inserts $s-3$ stages
between the second and the last:

- **implicit tableau**: the inserted rows have only $a^{\mathrm I}_{i2}=c_i$, i.e. they
  extrapolate with the stage-2 derivative and need no solve; the last row is
  $(0,1-\gamma,0,\dots,0,\gamma)=b^{\mathrm I}$. Only stages 2 and $s$ are implicit, for any
  $s$, and the implicit part reproduces the original two-stage SDIRK exactly;
- **explicit tableau**: row $i\ge4$ has only $a^{\mathrm E}_{i1}=c_i-a^{\mathrm E}_{i,i-1}$ and
  $a^{\mathrm E}_{i,i-1}$, so three stage derivatives are stored whatever $s$ (low storage),
  and $b^{\mathrm E}=b^{\mathrm I}$, $c^{\mathrm E}=c^{\mathrm I}$, with inserted abscissae
  equidistant between $\gamma$ and 1 (Eq. (26));
- the $s-2$ free entries $a^{\mathrm E}_{32},a^{\mathrm E}_{43},\dots,a^{\mathrm E}_{s,s-1}$ match
  the $s-2$ free coefficients $\theta_3,\dots,\theta_s$ of a second-order explicit
  stability polynomial and follow from it sequentially. For $s=4$ (Eqs. (32)–(34)),
  $$P(z)=1+z+\tfrac12z^2+\tfrac{\gamma+\gamma^2}2a^{\mathrm E}_{43}z^3+\gamma^2a^{\mathrm E}_{32}a^{\mathrm E}_{43}z^4,$$
  so $a^{\mathrm E}_{43}=2\theta_3/(\gamma+\gamma^2)$ and $a^{\mathrm E}_{32}=\theta_4/(\gamma^2a^{\mathrm E}_{43})$;
  the $z^2$ coefficient $2\gamma-\gamma^2$ equals $\frac12$ for $\gamma=1-\frac1{\sqrt2}$
  (App. 1). The polynomial was re-derived from the tableau *(compiler check)*.

The polynomials are [optimal stability polynomials](/methods/optimal-stability-polynomial.md)
for the von Neumann spectra of flux-reconstruction DG on linear advection, degrees 1–8,
found by Ketcheson–Ahmadia bisection with CVX (§3.2, §4). With four stages the optimal
explicit step is 2.01, 1.79, 1.80, … , 1.84 times that of ARS(2,3,2) for degrees 1–8
(Table 1); the gain grows about linearly with $s$ and exceeds 5 at $s=10$ (Fig. 1).
Evidence (§5):

- second order on 1D advection with element-size ratio about $2.5\times10^5$, observed
  1.96–2.00 for $s=4,\dots,10$, errors nearly independent of $s$ (Table 2);
- second order on an [isentropic vortex](/benchmarks/isentropic-vortex.md) with an implicit
  refined strip, AIMEX10,2 (Table 3);
- laminar SD7003 airfoil ($\mathrm{Re}=10^4$, Mach 0.2, 6,926 elements): AIMEX10,2 up to
  23 times faster than explicit RK3,3 and at least twice as fast as ARS(2,3,2) for degrees
  1–4, with lift and drag identical to 3–4 digits; beyond an implicit fraction of about 0.2
  the implicit cost grows faster than the step gain (Fig. 6, Table 4);
- an implicit LES of a stalled NACA 0020 with 2.5% implicit elements agrees reasonably with
  DNS (Table 5).

The implicit stages are solved by quasi-Newton with the Jacobian recomputed every 10 or 500
steps and GMRES with additive-Schwarz ILU(0), tolerance $10^{-6}$ (§5.3–5.4). The
construction shares the sparsity "two nonzeros per row, one free entry per stage fixed by
an optimized polynomial" of [paired explicit Runge–Kutta](/methods/paired-explicit-runge-kutta.md)
members, a relation the paper does not draw *(compiler remark)*.

## Add-and-subtract (explicit–implicit–null) use

When the stiff term is nonlinear, an IMEX pair can be applied to a reformulated equation:
add a linear constant-coefficient operator with the same wave-number scaling, treat the
added copy implicitly, and treat the subtracted copy with all nonlinear terms explicitly.
Every implicit stage is then a linear constant-coefficient solve
([Tan et al. (2022)](/sources/tan-2022.md), §1, Eq. (1.4); Tan et al. (2025), §1, §3.4).
For ARS(4,4,3) the stability of this use depends on the size of the added operator
relative to the physical one: Tan et al. (2022, Props. 3.1–3.2) find, by a sampled
Fourier search, unconditional stability for a ratio of at least 0.54 on diffusive,
dispersive and biharmonic models, and Tan et al. (2025, Prop. 3.1) the same 0.54 plus a
convective Courant limit of 1.2 for linearized compressible Navier–Stokes. These are
numerical, hypothesis-grade thresholds, specific to this pair (Remark 3.4 of the 2022
paper). See [explicit–implicit–null method](/methods/explicit-implicit-null-method.md).

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

**Invariant-domain preservation by limiting.** Ern & Guermond (2023, §3, Thm. 3.3) make
*every* pair of an explicit method and an EDIRK with shared abscissae, $c_1=0$, $c_j\ge0$,
invariant-domain preserving and conservative. Each stage is computed from its predecessor
stage in incremental form, as a hyperbolic prediction and a parabolic update, each limited
against a low-order forward- or backward-Euler step of size $(c_l-c_{l'})h$; the result
holds for $h\le h^*/\Delta c^{\max}$, $h^*$ the low-order hyperbolic step bound, with no sign
condition on the Butcher coefficients and $2s-1$ quasi-linear solves per step (Remark 3.2).
See [invariant-domain-preserving time stepping](/methods/invariant-domain-preserving-time-stepping.md).

## Linear stability in applications

**Advection–diffusion test equation.** Ascher et al. (1997, §3) analyse their pairs on
$y'=\mathrm i\omega y+\lambda_{\mathrm d}y$ with real $\omega>0$, $\lambda_{\mathrm d}\le0$
(page-local; the paper writes $\beta$, $\alpha$), the imaginary term explicit and the real one
implicit, the [von Neumann](/definitions/von-neumann-stability-analysis.md) reduction of
centred advection–diffusion. With $\xi=h\lambda_{\mathrm d}$ and $\vartheta=h\omega$
(page-local) the step is $y_{n+1}=R\,y_n$; (1,1,1) gives
$R=\frac{1+\mathrm i\vartheta}{1-\xi}$, unstable on the imaginary axis for every
$\vartheta\neq0$, and (1,2,1) gives $\lvert R\rvert^2=1-\vartheta^2+\vartheta^4$ there, stable
iff $\lvert\vartheta\rvert\le1$, a restriction that remains as $\xi\to-\infty$ (§3). Plotting
the largest stable $\vartheta$ against $\lambda_{\mathrm d}/\omega\in[-10^2,-10^{-2}]$ (Figs.
1–2), the sub-family-2 pairs (1,1,1), (2,2,2), (4,4,3) have no step restriction as
$\lambda_{\mathrm d}\to-\infty$, like SBDF, while the sub-family-1 pairs keep one, "typically"
$\vartheta<1$; (3,4,3) suggests "a
potential advantage, in terms of allowable time steps, over a large range of parameter
values".

**Additive stability function.** Kennedy & Carpenter (2003, §2.1.5, §3.1.2, Eqs. (15),
(26)–(31)) use the two-variable function
$R(z_{\mathrm E},z_{\mathrm I})=\det\bigl(I-z_{\mathrm E}A^{\mathrm E}-z_{\mathrm I}A^{\mathrm I}+\mathbf 1(z_{\mathrm E}b^{\mathrm E}+z_{\mathrm I}b^{\mathrm I})^\top\bigr)/\det\bigl(I-z_{\mathrm I}A^{\mathrm I}\bigr)$
($z_{\mathrm E}$, $z_{\mathrm I}$ page-local) and show that, for an explicit method coupled with
an ESDIRK, $R(z_{\mathrm E},-\infty)=0$ for every $z_{\mathrm E}$ needs, besides the two
conditions that make the ESDIRK L-stable, one coupling coefficient of the numerator to vanish.
"Several of the methods given by Ascher et al. and Griepentrog do not account for this and
consequently have $R(z^{[E]},-\infty)$ depending linearly on $z^{[E]}$" (§3.1.2); App. B
lists $R(z_{\mathrm E},-\infty)=-0.732(1+z_{\mathrm E})$ for Ascher (2,3,3) and
$0.106z_{\mathrm E}$ for Ascher (3,4,3). Ascher et al. (1997) do not claim L-stability of the
pairs: they call the DIRK parts of (2,3,2), (2,2,2), (3,4,3), (4,4,3) L-stable and rate the
pairs by the test equation above. Details on
[Kennedy–Carpenter ARK methods](/methods/kennedy-carpenter-ark-methods.md).

**Stiffness leakage.** Kennedy & Carpenter (2003, §8.1) call a pair's stiffness separable
only if the stiff terms do not "stiffen the nonstiff terms", and measure leakage by the
largest stable Courant number as the reaction stiffness grows on a reacting-shock problem. Five
IMEX pairs of Zhong, Yoh and Shen leak catastrophically (largest stable Courant number 0.36–0.57 in
the column headed $\varepsilon=10^0$, 0.0 in the column headed $\varepsilon=10^6$, Table 8), Griepentrog's pairs break under
nonequilibrium data, and the authors point to the internal stability values $-2.464$ and
$-4.909$ of their final stages ([internal stability](/definitions/internal-stability.md); Tables 9–10), and with
nonequilibrium data and exothermic chemistry every additive pair leaks at fixed step while
SBDF2–4 show insignificant leakage (Tables 11, 13).

The sources report pair-dependent stability failures that the scalar
[stability function](/definitions/stability-function.md) of each tableau does not reveal:

- **Upwind DG advection, SIPG diffusion.** With advection explicit and diffusion implicit,
  only the Ascher–Ruuth–Spiteri pairs whose two parts are both stiffly accurate,
  IMEX(1,1,1), (2,2,2) and (4,4,3), were reasonably stable; IMEX(1,2,1) is "very unstable"
  at the forward-Euler advective limit, shown by the eigenvalues of the step matrix
  (Buvoli & Southworth 2023, §6.3.1, Fig. 7). At diffusion coefficient 0.01 and $h=0.01$
  only IMEX(1,1,1) and IMEX(4,4,3) did not diverge (Table 1). The pairs found stable are the
  sub-family-2 pairs that Ascher et al. (1997, §3, Fig. 1) find free of a step restriction in
  the strongly diffusive limit of their test equation.
- **Linearly implicit splitting.** On the stiff [Van der Pol oscillator](/benchmarks/van-der-pol-oscillator.md)
  with $f^{\mathrm I}=J_ny$, $f^{\mathrm E}=f-J_ny$ (exact Jacobian), every IMEX-RK pair tested
  needed much smaller steps to be stable than the FIMEX methods (Buvoli & Southworth 2023,
  §6.2, Fig. SM4).
- **Rotating shallow water.** In a fully discrete Fourier analysis with central differences
  at Courant number 0.2, Coriolis term explicit and gravity waves implicit,
  [Maurya et al. (2021)](/sources/maurya-2021.md) find the atmospheric-modelling pair SIRK3
  (Kar) slightly unstable, and SIL3 (Whitaker–Kar) and the second-order pair of
  Ascher–Ruuth–Spiteri §2.5–2.6 stable (§9, App. A, Fig. 17); see [von Neumann analysis](/definitions/von-neumann-stability-analysis.md).
- **Element-wise splitting.** Vermeire & Hedayati Nasab (2021) design only the explicit
  polynomial on the explicit-region spectrum and do not analyse the coupled scheme at the
  implicit–explicit interface; they see no degradation there in their flow fields (§5.3,
  Fig. 5).

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
  Ern & Guermond (2023, §5.1, Figs. 2–3), on a stiff $2\times2$ system whose limit is an
  index-1 DAE: at $\varepsilon=10^{-6}$ all their third- and fourth-order pairs reduce the
  error of the first component to second order, while the fourth-order ones keep fourth
  order in the second; they place it in the pre-asymptotic range $\varepsilon<h$, after
  Boscarino–Pareschi. It is also observed by
  Gottlieb et al. (2022, Remark 4, §3.5) and, for ARS(4,4,3), by Hu & Shu (2025, §6,
  Fig. 1). Kennedy & Carpenter (2003, §8.3a, Figs. 8–12, Table 15) observe it for every
  additive pair of classical order above 2 on Kaps', Van der Pol and Pareschi–Russo
  problems, worst at $\varepsilon\approx h$, and not for the IMEX-BDF schemes; stage order 2
  of the implicit part does not raise the order of the differential variables. Ascher et al.
  (1997, §1) do not expect their pairs to compete with SBDF when the implicit term is dominant
  and very stiff, since "the effective order of DIRK schemes drops to 1 for very stiff ODEs".
  Orlando & Bonaventura (2025, §5.1, Table 5) attribute part of a loss of the
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
- **Multigrid per stage.** On a 2D viscous Burgers-type system with diffusion implicit and
  one multigrid solve per stage (V(1,1) cycles, residual tolerance 0.003), Ascher et al. (1997,
  §5, Table 1) find that weakly damping pairs need more fine-grid iterations because
  "lingering high-frequency modes necessitate more work on the finest grid": (1,2,2) needs
  3.13–3.68 iterations for viscosity $\ge0.03$ against 2.58–2.81 for (2,2,2). The L-stable
  (4,4,3) needs 4.77–7.84, more than (1,2,2) and (2,3,3) at every printed viscosity
  ([implicit stage solvers](/methods/implicit-stage-solvers.md)).
- **Against multistep IMEX.** On 1D variable-coefficient advection–diffusion (3,4,3) "is more
  accurate and stable in this example than the popular CNAB scheme with one-third the step
  size", and at small viscosity the third-order pairs have errors "always smaller than those
  arising for the two-step IMEX schemes" of Ascher–Ruuth–Wetton "even though twice the time
  step is applied" (Ascher et al. 1997, §4.1, Figs. 4–5). On a reacting-shock problem SBDF3/4
  are slightly more efficient than the Kennedy–Carpenter pairs but have no error control
  (Kennedy & Carpenter 2003, §8.2, §9); see
  [IMEX linear multistep methods](/methods/imex-linear-multistep-methods.md).
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
  $0$. With a minus sign the row sum is $\frac35$ and $R_\infty\approx0$ *(compiler
  check)*, as in the same tableau printed by Orlando et al. (2025b, Table 21) and in the
  ARK3(2)4L[2]SA tableau of Kennedy & Carpenter (2003, App. D).
- **Digits of ARS(3,4,3).** Ascher et al. (1997, §2.7) print
  $a^{\mathrm E}_{42}=a^{\mathrm E}_{43}=0.5529291479$; Chinomona & Reynolds (2021, §4.1) print
  a 40-digit value beginning $0.5529291480$. Both are recorded above.
- **Attributions of the implicit parts.** Ascher et al. (1997, §2.4–2.5, §2.7) take the
  two-stage third-order DIRK from Hairer–Nørsett–Wanner (p. 207) and the stiffly accurate
  two- and three-stage DIRKs from Hairer–Wanner (p. 106); the names attached to these DIRKs on
  [diagonally implicit Runge–Kutta](/methods/diagonally-implicit-runge-kutta.md) come from
  other sources.
- **Type II with ill-prepared data.** Orlando & Bonaventura's Table 1 pair is type II
  non-ARS, hence by their own §3.1 only weakly AP, yet their colliding-pulse and
  density-layering tests start from pressure data that are not well prepared; the paper
  does not comment.
- **Naming.** Orlando et al. (2025b, §3.1) define $(s,\sigma,p)$ as the numbers of
  implicit and explicit function evaluations, but their IMEX-RK(3,3,3) has four explicit
  stages and IMEX-RK(6,6,4) seven stages; the names follow neither count consistently.
- **Accelerated pairs: what is and is not shown.** Vermeire & Hedayati Nasab (2021) give no
  stability analysis of the coupled element-wise scheme (above). On their 1D advection test
  the baseline ARS(2,3,2) is *more* accurate at small steps, e.g. $2.80\times10^{-8}$ against
  $1.03\times10^{-7}$ for AIMEX4,2 at $h=1.25\times10^{-4}$, with unexplained observed orders
  3.55, 2.47, 2.19 (Table 2). Speedups are given only as ratios, without hardware or wall
  times, and as "over 20" or "up to 23" in different places (abstract, §5.3, §6). The
  linear growth of the stable step with $s$ is a gain per step; per explicit evaluation it
  is roughly the step ratio times $3/s$, which matters little only because implicit work
  dominates (Eq. (18)) *(compiler remark)*. Their von Neumann eigenvalues are written for
  $e^{\mathrm i(\theta x-\omega t)}$ but inserted into $P$ without the factor $-\mathrm i$
  (Eqs. (53), (37)); the rotation is presumably done in the computation.
- **Efficiency ratios of the reviewed pairs.** Ern & Guermond (2023) name the reviewed
  pairs IMEX(3,2;0.24), IMEX(3,3;0.26) and IMEX(6,4;0.08). Their own definition
  $c_{\mathrm{eff}}=1/(s\Delta c^{\max})$ gives $1/(3(1-\gamma))\approx0.47$ for ARS(2,3,2)
  ($\Delta c^{\max}=1-\gamma$) and $1/(3\gamma)\approx0.42$ for the Crouzeix–Nørsett pair
  ($\gamma\approx0.78867$); the printed values equal $\Delta c^{\max}/s$ instead *(compiler
  check of Eqs. (63), (78)–(79), HAL draft read)*. The conclusion that the new pairs reach
  $c_{\mathrm{eff}}=1$ and the reviewed ones do not is unaffected.
- **A misnamed "IMEX" class.** The "optimized partially implicit–explicit Runge–Kutta"
  (OPIRK) schemes of Maurya et al. (2021) solve no implicit system; they are sequential
  explicit updates of a partitioned system and are described on
  [semi-implicit IMEX Runge–Kutta](/methods/semi-implicit-imex-runge-kutta.md).
- **"L-stability is necessary."** Orlando & Bonaventura's statement (§3.1) is attributed to
  Pareschi–Russo without proof; Hu & Shu's uniform-accuracy hypotheses (ISA plus condition
  (A)) imply the same $R_\infty=0$ condition for their pairs, so the two sources agree on
  the schemes they treat *(compiler observation)*.

# Citations

- [Ascher et al. (1997)](/sources/ascher-1997.md) — §1 (Eq. (1.3)), §2 (Eqs. (2.1)–(2.4), p. 155 naming), §2.1–2.8 (pairs (1,1,1) to (4,4,3), Example 2), §3 (Eqs. (3.1)–(3.2), Figs. 1–2), §4.1 (Figs. 3–5), §5 (Table 1).
- [Kennedy & Carpenter (2003)](/sources/kennedy-2003.md) — NASA/TM-2001-211038: §1, §2.1 (Eqs. (2)–(6)), §2.1.2 (Tables 1–4), §2.1.5, §3 (naming), §3.1.2 (Eqs. (26)–(31)), §4–6, §8.1 (Tables 8–13), §8.2–8.3 (Figs. 8–12, Table 15), §9, App. B, App. D.
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
- [Tan et al. (2022)](/sources/tan-2022.md) — §1 (Eq. (1.4)), §2.4 (Eqs. (2.16)–(2.17)), §3 (Props. 3.1–3.2, Remark 3.4).
- [Tan et al. (2025)](/sources/tan-2025.md) — §1, §3.4 (Eqs. (3.2)–(3.5)), §3.5 (Prop. 3.1).
- [Buvoli & Southworth (2025)](/sources/buvoli-2025.md) — §4.1 (Eq. (4.5)), Table 4.1, §4.5 (Eqs. (4.18), (4.22)–(4.27)), §7.1 (Fig. 7.1).
- [Vermeire & Hedayati Nasab (2021)](/sources/vermeire-2021.md) — §1, §2.1–2.2 (Eqs. (9)–(18)), §3.1 (Eqs. (19)–(34)), §3.2, §4 (Table 1, Fig. 1), §5.1–5.4 (Tables 2–5, Figs. 5–6), §6.
- [Ern & Guermond (2023)](/sources/ern-2023.md) — HAL draft: §3.3 (Thm. 3.3, Eq. (63), Remark 3.2), §4.1 (Eqs. (64)–(75)), §4.2–4.4 (Eqs. (76)–(84), Remarks 4.1–4.2), §5.1 (Figs. 1–3).
- [Buvoli & Southworth (2023)](/sources/buvoli-2023.md) — arXiv v2: §1, §6.2 (Fig. SM4), §6.3.1 (Fig. 7, Table 1); supplement SM4.
- [Maurya et al. (2021)](/sources/maurya-2021.md) — §9, App. A (Eqs. (50)–(51), Fig. 17).
