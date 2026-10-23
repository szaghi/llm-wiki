---
type: Method
title: "Semi-implicit and linearly implicit IMEX Runge–Kutta methods"
description: "Semi-implicit IMEX Runge–Kutta methods write y' = H(y, y) with an explicit and an implicit argument, duplicate the state and apply an IMEX tableau pair to the two copies, so that freezing coefficients at the explicit copy makes every stage solve linear; the page gives the scheme, its tableaux, its all-Mach, MHD and radiation-hydrodynamics uses and its limits."
status: established
aliases: [SI-IMEX, SI-IMEX-RK, LIMEX-RK, linearly implicit IMEX Runge–Kutta, semi-implicit IMEX Runge–Kutta, partitioned-argument IMEX, Boscarino–Filbet–Russo semi-implicit Runge–Kutta, ALIMEX-RK, OPIRK, optimized partially implicit–explicit Runge–Kutta]
tags: [imex, runge-kutta, stiff, linear-algebra, asymptotic-preserving]
timestamp: 2026-10-20T06:18:00Z
---

# Semi-implicit and linearly implicit IMEX Runge–Kutta methods

An [IMEX Runge–Kutta method](/methods/imex-runge-kutta.md) needs an additive split
$f=f^{\mathrm E}+f^{\mathrm I}$. Many stiff terms do not split that way: in all-Mach
gas dynamics the stiff pressure work $\nabla\cdot(\mathsf h\rho u)$ multiplies a nonstiff
enthalpy $\mathsf h$ by a stiff momentum (page-local $\rho$, $u$ and sans-serif $\mathsf h$,
distinct from the step $h$), and in radiation hydrodynamics the stiff absorption term
carries opacities that depend on the hydrodynamic state. The **semi-implicit**
(Boscarino–Filbet–Russo) approach writes the right-hand side with two arguments,

$$y'=\mathcal H(y,y),$$

the first to be treated explicitly and the second implicitly ($\mathcal H$ page-local),
duplicates the state into an explicit copy $y^{\mathrm E}$ and an implicit copy
$y^{\mathrm I}$,

$$y^{\mathrm E\prime}=\mathcal H(y^{\mathrm E},y^{\mathrm I}),\qquad y^{\mathrm I\prime}=\mathcal H(y^{\mathrm E},y^{\mathrm I}),\qquad y^{\mathrm E}(t_0)=y^{\mathrm I}(t_0)=y_0,$$

and applies an IMEX tableau pair to this partitioned system, explicit in
$y^{\mathrm E}$ and implicit in $y^{\mathrm I}$. The exact solution of the doubled
system is $y^{\mathrm E}=y^{\mathrm I}=y$, so any nonlinear interaction between the two
arguments is allowed ([Southworth et al. (2024)](/sources/southworth-2024.md), §2,
Eq. (4); [Orlando et al. (2025b)](/sources/orlando-2025-b.md), §3.3, Eqs. (37)–(39);
[Boscheri & Pareschi (2021)](/sources/boscheri-2021.md), §3.4.1, Eqs. (71)–(72)). When
$\mathcal H$ is affine in its second argument, each stage is a **linear** system with
coefficients frozen at explicit-copy values: the method is *linearly implicit*, and
needs neither Newton nor Picard iterations. Southworth et al. call the class LIMEX-RK,
Orlando et al. SI-IMEX; all sources take the framework from Boscarino, Filbet & Russo.

## The scheme

With an explicit tableau $(A^{\mathrm E},b^{\mathrm E},c^{\mathrm E})$, a diagonally
implicit tableau $(A^{\mathrm I},b^{\mathrm I},c^{\mathrm I})$ and **equal weights**
$b^{\mathrm E}=b^{\mathrm I}=b$, the stages are

$$\begin{aligned}
Y^{\mathrm E}_i&=y_n+h\sum_{j=1}^{i-1}a^{\mathrm E}_{ij}\,\mathcal H\big(Y^{\mathrm E}_j,Y^{\mathrm I}_j\big),\\
Y^{\mathrm I}_i&=y_n+h\sum_{j=1}^{i}a^{\mathrm I}_{ij}\,\mathcal H\big(Y^{\mathrm E}_j,Y^{\mathrm I}_j\big),\\
y_{n+1}&=y_n+h\sum_{i=1}^{s}b_i\,\mathcal H\big(Y^{\mathrm E}_i,Y^{\mathrm I}_i\big)
\end{aligned}$$

(Southworth et al. 2024, §2.2, Eq. (9); Orlando et al. 2025b, Eqs. (43)–(44)). Equal
weights make the two copies agree at every step end, $y^{\mathrm E}_{n+1}=y^{\mathrm I}_{n+1}$,
so the doubling of unknowns is "only apparent": one solution is stored and one set of
right-hand-side values $\mathcal H(Y^{\mathrm E}_j,Y^{\mathrm I}_j)$ serves both copies
(Boscheri & Pareschi 2021, §3.4.1; Orlando et al. 2025b, §3.3; Southworth et al. 2024,
Eq. (11)). Stage $i$ first forms $Y^{\mathrm E}_i$ explicitly, then solves
$Y^{\mathrm I}_i-ha^{\mathrm I}_{ii}\mathcal H(Y^{\mathrm E}_i,Y^{\mathrm I}_i)=\text{known data}$
for $Y^{\mathrm I}_i$. If the implicit tableau is
[stiffly accurate](/properties/stiff-accuracy.md), $y_{n+1}=Y^{\mathrm I}_s$
([Boscheri & Thomann (2024)](/sources/boscheri-2024.md), §3.3).

Boscheri & Pareschi (2021, Eqs. (75)–(77)), Boscheri & Thomann (2024, Eqs. (37)–(40))
and [Birke et al. (2024)](/sources/birke-2024.md) (Eqs. (32)–(34)) print the same scheme
with stage derivatives $k_i=\mathcal H(Y^{\mathrm E}_i,Y^{\mathrm I}_i)$, where the
implicit argument appears as "known data $+\,ha^{\mathrm I}_{ii}k_i$"; the two forms are
identical.

**Relation to additive IMEX.** If $\mathcal H(u,v)=f^{\mathrm E}(u)+f^{\mathrm I}(v)$,
the scheme is the additive IMEX method with $b^{\mathrm E}=b^{\mathrm I}$. Southworth et
al. implement the general case as $\mathcal H(y^{\mathrm E},y^{\mathrm I})=f^{\mathrm E}(y^{\mathrm E})+f^{\mathrm I}(y^{\mathrm E},y^{\mathrm I})$,
with $f^{\mathrm I}$ implicit in the second argument only (Eq. (12)). They state that
component-wise (partitioned) and additive partitions are equivalent classes and that the
order conditions are those of partitioned Runge–Kutta methods (§2.1). Additive partitions
must still sum to the original operator: a substitution valid only for the exact flow
(their example: using $\frac{d}{dt}\rho=0$ inside one sub-operator of an operator split)
is not allowed in a Runge–Kutta partition (§3.3, item 2).

**First-order member.** With explicit Euler $(c,A,b)=(0,0,1)$ and implicit Euler
$(1,1,1)$ the scheme is $y_{n+1}=y_n+h\,\mathcal H(y_n,y_{n+1})$ (Southworth et al.
2024, Eqs. (10)–(11); Orlando et al. 2025b, Eq. (46); SP(1,1,1) in Boscheri & Pareschi
2021, Eq. (78)).

## How the stage solve becomes linear

The design work is in the choice of $\mathcal H$, i.e. which factor of each stiff term
is frozen at the explicit copy.

- **All-Mach Navier–Stokes and Euler.** With the Toro–Vázquez-Cendón flux split, the
  convective fluxes are explicit and the pressure gradient implicit; the energy equation
  is semi-implicit: kinetic energy as $\frac{\varepsilon}{2}\frac{(\rho u)^n}{\rho^n}(\rho u)^{n+1}$
  (explicit factor times implicit factor) and the enthalpy flux as $\mathsf h^n(\rho u)^{n+1}$,
  with $\varepsilon\propto\mathrm{Ma}^2$ (Boscheri & Pareschi 2021, §3.1, Eqs. (22)–(26);
  page-local $\mathrm{Ma}$). Substituting the momentum update gives a
  pressure wave equation that is **linear** for an ideal gas (Eq. (29)) and mildly
  nonlinear for a general equation of state, solved there by a nested Newton method
  that converged in at most four iterations to $10^{-10}$ on Redlich–Kwong shock tubes
  (Eqs. (33)–(36), §4.2). Orlando et al. (2025b, §3.3, Eqs. (40)–(42), (50)) use
  $\mathcal H=-\nabla\cdot F_{\mathrm E}-\nabla\cdot F_{\mathrm{SI}}$ with
  $F_{\mathrm{SI}}=(0,\ p_{\mathrm I}/\mathrm{Ma}^2,\ \mathsf h_{\mathrm E}(\rho u)_{\mathrm I})$ and a
  linear elliptic pressure equation per stage. For non-ideal gases they freeze the ratio
  of internal energy to pressure, $(\rho e)_{\mathrm I}\approx\frac{(\rho e)_{\mathrm E}}{p_{\mathrm E}}\,p_{\mathrm I}$
  (Eq. (53)), which keeps the equation linear for any equation of state and is exact for
  the ideal gas; on a low-Mach Kelvin–Helmholtz test with a cubic equation of state it
  saved about 70% CPU time against solving the nonlinear pressure equation, with no
  visible difference (§3.4, §4.5, Fig. 13).
- **Ideal MHD.** Birke et al. (2024, §3.1, Eqs. (22)–(25)) split the flux into an explicit
  convective part (all transport and magnetic terms, gravity) and an implicit pressure
  part, freeze $\mathsf h^n$ and write the kinetic energy semi-implicitly: one linear elliptic
  pressure equation per implicit stage, solved by GMRES to $10^{-12}$, with no fixed-point
  iteration. Boscheri & Thomann (2024, §3.1–3.5) split three ways (convective, pressure,
  magnetic), linearize $\lVert B\rVert^2\approx B^n\cdot B^{n+1}$ and
  $(\rho E+p)u\approx(\rho E^n+p^n)u^{n+1}$ (page-local magnetic field $B$, specific total
  energy $E$, pressure $p$), and obtain two **decoupled** linear systems
  solved in sequence by GMRES to about $10^{-14}$: a vector system for the magnetic
  potential, then a scalar elliptic system for the total energy (Eqs. (56), (60)).
- **Radiation hydrodynamics.** Southworth et al. (2024, §3.3, Eqs. (25)–(27)) freeze
  opacities, diffusion coefficient and heat capacity at the explicit copy and keep
  radiation energy and temperature implicit. The $T^4$ emission term stays nonlinear in
  the temperature, so their stage solves are "inexact linear and nonlinear" (§5.2). They
  also derive a temperature evolution equation from $\mathrm de_i=c_v\,\mathrm dT$
  (Eqs. (20)–(24)) so that the implicit solve does not pass through a tabulated equation
  of state.

## Tableaux used

Let $\gamma$ denote the diagonal entry of the implicit tableau (page-local, as on
[DIRK methods](/methods/diagonally-implicit-runge-kutta.md)). Triplets follow the
Pareschi–Russo convention (implicit stages, explicit stages, order) unless stated.

| Name in the source | Explicit tableau | Implicit tableau | Properties | Used by |
|---|---|---|---|---|
| SP(1,1,1) | forward Euler | backward Euler | order 1 | Boscheri & Pareschi 2021, Eq. (78) |
| LSDIRK2(2,2,2) | $c^{\mathrm E}=(0,\frac1{2\gamma})$, $a^{\mathrm E}_{21}=\frac1{2\gamma}$ | $c^{\mathrm I}=(\gamma,1)$, rows $(\gamma)$, $(1-\gamma,\gamma)$; $\gamma=1-\frac1{\sqrt2}$ | $b=(1-\gamma,\gamma)$; order 2; implicit part the L-stable stiffly accurate SDIRK2 | Birke et al. 2024, Table 1; Boscheri & Thomann 2024, Eq. (39) |
| H-LDIRK2(2,2,2) | $c^{\mathrm E}=(0,1)$, $a^{\mathrm E}_{21}=1$ | $c^{\mathrm I}=(\gamma,1-\gamma)$, rows $(\gamma)$, $(1-2\gamma,\gamma)$; $\gamma=1-\frac1{\sqrt2}$ | $b=(\frac12,\frac12)$; order 2 | Southworth et al. 2024, §5.1 |
| SA SSP(3,3,2) = SSP-LDIRK2(3,3,2) | $c^{\mathrm E}=(0,\frac12,1)$, rows $(\frac12)$, $(\frac12,\frac12)$ | $c^{\mathrm I}=(\frac14,\frac14,1)$, rows $(\frac14)$, $(0,\frac14)$, $(\frac13,\frac13,\frac13)$ | $b=\frac13\mathbf 1$; order 2; implicit stiffly accurate | Boscheri & Pareschi 2021, Eq. (79); Southworth et al. 2024, §5.1 |
| SSP-LDIRK3(3,3,2) | SSPRK(3,3): $c^{\mathrm E}=(0,1,\frac12)$, rows $(1)$, $(\frac14,\frac14)$ | rows $(\gamma)$, $(1-2\gamma,\gamma)$, $(\frac12-\gamma,0,\gamma)$; $\gamma=1-\frac1{\sqrt2}$ | $b=(\frac16,\frac16,\frac23)$; formally order 2 | Southworth et al. 2024, §5.1 (reference solutions) |
| SSP3(4,3,3) | SSPRK(3,3) after a zero first stage | $c^{\mathrm I}=(\alpha_0,0,1,\frac12)$, $\alpha_0=0.241694$ | order 3; implicit **not** stiffly accurate | Boscheri & Pareschi 2021, Eq. (81), high Mach only |
| SA DIRK(3,4,3); IMEX-RK(4,3,3) type I; I-IMEX(3,4,3) | see below | $c^{\mathrm I}=(\gamma,\gamma,\frac{1+\gamma}2,1)$, rows $(\gamma)$, $(0,\gamma)$, $(0,\frac{1-\gamma}2,\gamma)$, $(0,b_2,b_3,\gamma)$ | order 3; type I, stiffly accurate | Boscheri & Pareschi 2021, Eq. (80); Orlando et al. 2025b, Table 20; Southworth et al. 2024, §5.1 |

($\alpha_0$ is page-local.) In the last row $\gamma=0.4358665215\ldots$ is the middle root
of $6\gamma^3-18\gamma^2+9\gamma-1=0$, and $b=(0,b_2,b_3,\gamma)$ with
$b_2\approx1.2084966492$, $b_3\approx-0.6443631707$: the weights and diagonal of the
[ARS(3,4,3)](/methods/imex-runge-kutta.md) pair, but with an implicit first stage
($a^{\mathrm I}_{11}=\gamma$), which makes $A^{\mathrm I}$ invertible and the implicit
part L-stable through stiff accuracy *(compiler check: $1-b^\top(A^{\mathrm I})^{-1}\mathbf 1=0$)*.
Southworth et al. print the explicit companion of I-IMEX(3,4,3) (from Boscarino 2023) to
10 digits: $c^{\mathrm E}=(0,\gamma,\frac{1+\gamma}2,1)$, rows $(\gamma)$,
$(1.243893189,-0.5259599287)$, $(0.6304125582,0.7865807402,-0.4169932983)$; with it the pair
satisfies all order-3 conditions, coupling conditions included *(compiler check, not in
the source)*. Note $c^{\mathrm E}\neq c^{\mathrm I}$ in the first stage.

## Requirements and limits

- **Equal weights.** All sources require $b^{\mathrm E}=b^{\mathrm I}$ (Boscheri &
  Pareschi 2021, §3.4.1; Orlando et al. 2025b, §3.3; Southworth et al. 2024, §2.2).
- **Autonomy and distinct abscissae.** The most effective schemes Southworth et al. found
  have $c^{\mathrm E}\neq c^{\mathrm I}$; for non-autonomous problems they treat time as an
  auxiliary variable to avoid doubling the stage storage (§2.2). Orlando et al. (2025b,
  §4.4) find the type-I third-order scheme ($c^{\mathrm E}\ne c^{\mathrm I}$) unstable in
  the semi-implicit form on an open tube with time-dependent Dirichlet data, which makes
  the system non-autonomous and leaves the theory of the semi-implicit method (stated for
  periodic or no-flux boundaries); the type-II scheme runs at a quarter of the step that
  the Picard-iterated IMEX method tolerates.
- **Implicit-tableau type.** On a low-Mach Taylor–Green vortex the semi-implicit method
  with the type-II third-order scheme is stable only down to $\mathrm{Ma}=10^{-3}$, with
  the type-I scheme down to $10^{-4}$; Orlando et al. (2025b, §4.1–4.2, Tables 2–4, 9)
  conclude that type I is more robust at low Mach, consistent with earlier all-Mach work
  they cite. The open-tube test above reverses the ranking, so the ranking is
  test-dependent. The type classification is on
  [IMEX Runge–Kutta methods](/methods/imex-runge-kutta.md).
- **Against Picard-iterated IMEX.** Orlando et al. (2025b) compare the semi-implicit method
  with an IMEX method whose implicit enthalpy is resolved by a Picard iteration on the same
  DG discretization. The semi-implicit method is generally cheaper in wall-clock time, the
  gap shrinking to about 5% at $\mathrm{Ma}=10^{-3}$ because one Picard iteration suffices
  at low Mach (1, 3, 5 iterations for tolerances $10^{-4},10^{-6},10^{-10}$ at
  $\mathrm{Ma}=10^{-1}$; Table 16); the Picard IMEX method tolerates about twice the step
  and is "globally more robust" with large density or pressure variations and
  time-dependent boundaries (§4.2, §4.4, Fig. 6). With a common step on the open tube the
  semi-implicit method saves about 37% CPU time (§4.4).
- **Accuracy across Mach numbers.** Both approaches are asymptotic preserving and
  asymptotically accurate "in the range of low Mach accuracy established by the spatial
  discretization": third order up to $\mathrm{Ma}=10^{-3}$, error saturation at
  $10^{-4}$, attributed mainly to DG on quadrilaterals (Orlando et al. 2025b, §4.2, §5,
  Tables 8–15). Boscheri & Pareschi (2021, Table 2) report finite-volume orders
  2.87–2.99 for momentum with SA DIRK(3,4,3) for $\varepsilon\in[10^{-6},10^{-1}]$ on a
  stationary [isentropic vortex](/benchmarks/isentropic-vortex.md).

## Asymptotic preservation and step size

Boscheri & Pareschi (2021, §3.1) show formally, for the first-order semi-discrete
scheme, that the leading-order discrete equations give the incompressibility constraint
$\nabla\cdot u^{n+1}_{(0)}=O(h)$ with an $\varepsilon$-independent constant (Eqs. (37)–(47)),
and they rely on a stiffly accurate implicit tableau for high order: "in the stiff limit
only (80) can be used in order to be consistent with the limit model" (§3.4.1). Boscheri &
Thomann (2024, §3.2–3.3) transfer an AP proof for $\mathrm{Ma}\to0$ at unit Alfvén Mach
number from a related scheme and call stiff accuracy "crucial for assuring asymptotic
consistency and accuracy"; Birke et al. (2024) claim the AP property in the abstract
without analysis. See [asymptotic-preserving schemes](/definitions/asymptotic-preserving-scheme.md).

The payoff is a step limited by the material speed. Boscheri & Pareschi (2021, Eqs. (20),
(27)) replace the acoustic restriction $h=O(\sqrt\varepsilon)$ by
$h\le\nu\,\Delta x/\max\lvert u\rvert$. Boscheri & Thomann (2024, §4.1, §4.7, Figs. 1, 12)
run steps up to about $10^3$ times the explicit magnetosonic step on an MHD vortex and up
to $10^4$ times on a magnetized Kelvin–Helmholtz flow at $\mathrm{Ma}=10^{-4}$; Birke et
al. (2024, §4.7, Figs. 4–5) find kinetic-energy dissipation independent of
$\mathrm{Ma}_{\max}\in[10^{-5},10^{-1}]$ on a gravitational vortex. Birke et al. (2024,
Thm. 1) prove that their well-balanced semi-implicit scheme keeps a discrete
magnetohydrostatic equilibrium to machine precision; the pressure solve then needs zero
GMRES iterations (Tables 3–5).

## A three-tableau variant and operator splitting

Southworth et al. (2024, §2.3, Eqs. (13)–(17)) add a third, explicit tableau
$(\hat A,\hat b,\hat c)$ (page-local) for the implicit operator inside the explicit copy
(ALIMEX-RK). With first-order tableaux it gives the step "explicit step on
$f^{\mathrm E}$, then linearize $f^{\mathrm I}$ about the explicit update and solve", and
on the rad-hydro partition it reproduces the production first-order Lie–Trotter split
exactly once the temperature after the hydrodynamic step is replaced by its first-order
Runge–Kutta approximation (Eq. (30), §3.3.2). The split "cannot be exactly posed as a
standard ODE integrator" because it evaluates the temperature inconsistently between the
two sub-steps. The authors see no benefit of the three-tableau form over two tableaux. On
radiative shocks at Mach 1.2, 3 and 45, the two-stage and higher LIMEX methods reach
second order (third order in two cases) and errors 3–5 orders of magnitude below the
operator split at the hydrodynamic CFL step, for 2–4 times its cost; LIMEX-Euler and
Lie–Trotter are equally accurate (Abstract, §5.2, Figs. 7–10). See
[operator splitting](/methods/operator-splitting.md).

## Semi-implicit methods as nonlinearly partitioned Runge–Kutta methods

[Buvoli & Southworth (2025)](/sources/buvoli-2025.md) call the semi-implicit class
"to our knowledge the only general class of methods in the literature" that applies
directly to a right-hand side with two arguments (§2.2), and embed it in the
[nonlinearly partitioned Runge–Kutta (NPRK)](/methods/nonlinearly-partitioned-runge-kutta.md)
methods, which evaluate $F(Y_j,Y_k)$ at any pair of stages. Their convention puts the
implicit argument first, so $F(u,v)=\mathcal H(v,u)$ in this page's notation. With
that convention, an $s$-stage semi-implicit method is a $2s$-stage NPRK method whose odd
stages are the explicit copies $Y^{\mathrm E}_i$ and whose even stages are the implicit
copies $Y^{\mathrm I}_i$: the NPRK coefficients are $a_{2i-1,2j,2j-1}=a^{\mathrm E}_{ij}$,
$a_{2i,2j,2j-1}=a^{\mathrm I}_{ij}$ and output weights $b_{2i,2i-1}=b_i$, all others zero
(§4.2, Eq. (4.6); the identification of the odd and even stages with the two copies is
the compiler's reading of that equation). NPRK methods need no alternation of explicit and
implicit stages and reach a given order with fewer stages; the paper's IMEX-NPRK methods
of orders 1–3 use 2–5 stages and 1–4 implicit solves (§4.2, §5.1).

The first-order members coincide: the nonlinearly partitioned Euler step
$y_{n+1}=y_n+hF(y_{n+1},y_n)$ is the first-order member above and the standard
lagged-opacity step of thermal radiation transport (§3, §7.2). On viscous Burgers it
matches implicit and Rosenbrock Euler in accuracy and stability with one linear solve and
no exact Jacobian, while additive IMEX Euler degrades to explicit Euler as the viscosity
goes to zero (§3, Fig. 3.1). They contrast this with
[Rosenbrock methods](/methods/rosenbrock-wanner-method.md), which impose one linearly
implicit treatment on the whole problem (§2.3).

**Comparison on radiation transport.** On a gray thermal-radiation Marshak wave (1000
cells, S8 quadrature), H-LDIRK2(2,2,2) and SSP-LDIRK2(3,3,2) in this page's duplicated
form are stable only at smaller steps, while every second-order NPRK method tested is
stable at much larger steps with comparable accuracy at small steps, and the NPRK methods
with three implicit stages store less than SSP-LDIRK2(3,3,2) (§7.2, Fig. 7.3a). On a
128-cell mesh the implicit–explicit partition reduces every higher-order scheme to first
order, so higher order needs the semi-implicit partition; NPRK2[43]-SiSa converges at
second order even at the largest steps (Fig. 7.3b). No third-order scheme they tried
from the IMEX literature was stable on these problems, and their own third-order
NPRK3[54]-Si mostly fails through negative temperatures (§7.2). Buvoli et al. (2026)
build multirate methods on the same framework, freezing a nonlinear diffusion
coefficient at the explicit argument exactly as here
([Buvoli et al. (2026)](/sources/buvoli-2026.md), §4.1).

## Other routes to linear stage solves

The [explicit–implicit–null method](/methods/explicit-implicit-null-method.md) reaches
linear implicit stages differently: it adds and subtracts a linear constant-coefficient
operator, treats the added copy implicitly and the full nonlinear stiff term explicitly
([Tan et al. (2025)](/sources/tan-2025.md), §1, citing the semi-implicit methods as "the
other" strategy). The implicit matrix then has constant coefficients and can be factored
once, whereas a semi-implicit stage freezes the state-dependent coefficients and changes
its matrix at every stage; in return the null method needs a stabilization coefficient above
a threshold and pays an error that grows with it *(compiler comparison, not in the
sources)*.

## Sequential partitioned updates: the OPIRK schemes

"Implicit" in the semi-implicit literature means a linear solve with frozen coefficients.
[Maurya et al. (2021)](/sources/maurya-2021.md) use the word for something weaker. Their
"optimized partially implicit–explicit Runge–Kutta" (OPIRK) schemes treat linear wave
systems partitioned **by unknown**, such as the 1D linearized Euler equations
$u'=L_1\mathsf p$, $\mathsf p'=L_2u$ (page-local: velocity $u$, pressure $\mathsf p$,
sans-serif to avoid the order $p$, and linear spatial operators $L_1$, $L_2$). The
one-stage scheme OPIRK1 is (§2.1, Eq. (6))

$$u_{n+1}=u_n+hL_1\mathsf p_n,\qquad \mathsf p_{n+1}=\mathsf p_n+h\bigl[(1-\vartheta)L_2u_n+\vartheta L_2u_{n+1}\bigr],$$

with a free weight $\vartheta$ (page-local; the source's $c_1$, not an abscissa). The
"implicit" evaluation $L_2u_{n+1}$ uses a value already computed, so no system is solved:
the scheme is an explicit sequential update in Gauss–Seidel order across the equations,
at the cost of an explicit method. With $\vartheta=1$ it is the forward–backward
(symplectic Euler) step of the partitioned system, $u$ advanced with the old pressure and
$\mathsf p$ with the new velocity *(compiler identification from Eq. (6), not in the
source; see [symplecticity](/properties/symplecticity.md))*. The two-stage OPIRK2 adds a
second sweep with weights $(\vartheta_2,\vartheta_3)$ (page-local) and is called second order
(Eq. (10)); 2D linearized Euler and linearized rotating shallow-water versions advance the
unknowns in a fixed order in the same way (Eqs. (22), (37), (42)).

**Fourier analysis.** With $a=\nu\,\zeta(\kappa\Delta x)$, $\nu$ the Courant number and
$\zeta$ the modified wavenumber of the spatial scheme (page-local), the amplification
factors of OPIRK1 are $1-\frac{\vartheta a^2}2\mp\frac a2\sqrt{\vartheta^2a^2-4}$, and
stability in the wave regime $\vartheta^2a^2<4$ needs $\vartheta\ge1$ (Eq. (8)). The
determinant of the amplification matrix is $1+(1-\vartheta)a^2$, so in that regime
$\lvert g\rvert^2=1+(1-\vartheta)a^2$: neutral for $\vartheta=1$, damped for $\vartheta>1$,
growing for $\vartheta<1$; the formula reproduces the extreme moduli of their Table 1
*(compiler check, not in the source)*. For $\vartheta=1$ the critical Courant number is 2.0
with second-order central differences and 0.91 with the optimized compact scheme OUCS3
(Table 1), i.e. $2/\max\zeta$. OPIRK2 is neutral for $(\vartheta_2,\vartheta_3)=(0.75,1.5)$ and
$(0.5,0.5)$, with critical Courant numbers 1.48/0.68 and 2.00/0.91 for the two spatial
schemes (Table 2). The free weights are fixed by a dispersion-relation-preserving
optimization of the fully discrete scheme, an integral of
$\lvert g-e^{\mathrm i\nu\kappa\Delta x}\rvert^2$ (the source's sign convention) over wavenumbers under integral constraints on
$\lvert g\rvert-1$ and on phase- and group-velocity errors, by grid search at fixed Courant
number (§3, Eqs. (12)–(13); tolerances not printed). See
[von Neumann analysis](/definitions/von-neumann-stability-analysis.md).

**Evidence** (§3–12): at equal $h$ the OPIRK1 errors are below those of classical RK4 on a
1D acoustic pulse ($1.39\times10^{-4}$ against $1.83\times10^{-3}$ at the first output time,
Table 3) and on the CAA cylinder-scattering benchmark ($1.35\times10^{-5}$ against
$2.13\times10^{-5}$, Table 5); wall-clock times are about 13, 32, 95 and 53 s against 32, 91,
250 and 126 s for RK4 on four problems (Table 6). In a Fourier analysis of the linearized
rotating shallow-water equations OPIRK1 is neutral where the semi-implicit atmospheric pair
SIRK3 is slightly unstable (§9, App. A, Fig. 17; see
[IMEX Runge–Kutta methods](/methods/imex-runge-kutta.md)).

**Qualifications.**

- The orders 1 and 2 are asserted by name; no order conditions are written and no
  convergence study is shown. As printed, the third line of Eq. (10),
  $u_{n+1}=\frac12[u_n+u^{(1)}+hL_1\mathsf p_n]$, collapses to $u_{n+1}=u_n+hL_1\mathsf p_n$
  (first order in $u$); the printed amplification matrix and the 2D analogue (42) need the
  stage pressure $\mathsf p^{(1)}$ there (page-local stage values $u^{(1)}$, $\mathsf p^{(1)}$).
- The speedups of Table 6 compare a one-stage first-order scheme with four-stage RK4 at
  apparently equal steps, with no error-against-cost curves and no hardware stated; the
  ratios 2.4–2.8 reflect the stage counts. §13 calls the cost "comparable with explicit
  Runge–Kutta methods of same order".
- On a 1D linearized shallow-water Gaussian (§12.1, Fig. 23) the paper reports that RK4 with
  OUCS3 develops Gibbs oscillations "which result in instability", unlike OPIRK1. The run
  has $h=0.05$ s, $\Delta x=1000$ m and wave speed $\sqrt{gH}\approx31.3$ m/s, i.e.
  $\nu\approx1.6\times10^{-3}$. RK4 is stable on the imaginary axis up to $2\sqrt2$, and the
  periodic OUCS3 symbol peaks at $\zeta\approx2.209$ (at $\kappa\Delta x\approx2.393$, the
  paper's own q-wave limit), so a von Neumann analysis predicts a stable, slightly
  dissipative RK4 up to $\nu\approx1.28$ *(compiler check, not in the source)*. The reported
  growth is therefore not the linear instability of RK4 on the periodic scheme; boundary
  closures, which the paper does not analyse, remain a possible cause.
- The neutral stability of the forward–backward step for $a<2$ follows from the determinant
  above *(compiler check, not in the source)*; the paper presents OPIRK as "a new class"
  without relating it to that step.

## Discrete conservation

Southworth et al. (2024, §4, Eqs. (31)–(37)) prove that LIMEX-Euler with a finite-volume
discretization conserves total energy locally if the numerical fluxes satisfy
$\hat F_E=\hat F_{\rho e_t}+\hat F_{E_r}$ (page-local; local Lax–Friedrichs with a common
viscosity coefficient qualifies) and the radiation-pressure work terms are discretized
identically in the two energy equations, and globally up to boundary fluxes. Since each
stage of a LIMEX-RK method has the form of a scaled LIMEX-Euler step, conservation extends
to every LIMEX-RK method (§4.3). See
[entropy stability and conservation](/properties/entropy-stability.md).

## Qualifications

- **"Only two time scales."** Boscheri & Thomann (2024, §3, p. 7) state that a three-way
  split "is not suitable for the class of IMEX Runge–Kutta methods that allows only the
  splitting according to two time scales" and recast it in the two-argument form. The
  statement holds for the two-tableau IMEX class they cite; additive and
  [GARK](/methods/generalized-additive-runge-kutta.md) methods with more than two
  partitions exist, and Southworth et al. (2024) use a three-tableau variant.
- **Stiff accuracy of LSDIRK2.** Boscheri & Thomann call LSDIRK2 stiffly accurate because
  $b^{\mathrm E}=b^{\mathrm I}$ equals the last row of $A^{\mathrm I}$; the explicit last row
  $(\frac1{2\gamma},0)$ differs from $b$, so the pair is not globally stiffly accurate.
- **Printed tableau of Boscheri & Pareschi (2021), Eq. (80).** The implicit row 4 prints
  $a^{\mathrm I}_{44}=0.416993$ where stiff accuracy and the row sum require
  $\gamma=0.435866$, and the printed explicit rows 3–4 do not sum to their abscissae
  (2.1576 and 1.8340 against 0.7179 and 1). The implicit first row
  ($c^{\mathrm I}_1=a^{\mathrm I}_{11}=\gamma$) looks like a slip, because the name
  promises three implicit stages and ARS(3,4,3) has $a^{\mathrm I}_{11}=0$, but is not one: Orlando et al. (2025b, Table 20) and Southworth et al. (2024, I-IMEX(3,4,3))
  print the same type-I first row, and since $b_1=0$ and $a^{\mathrm I}_{i1}=0$ for $i\ge2$ it
  changes only the stage value passed to the explicit part. The "(3,4,3)" in the names is
  inherited from ARS(3,4,3) and no longer counts the implicit stages. Neither source's
  explicit companion matches the one printed in Eq. (80).
- **Printed tableau of Orlando et al. (2025b), Table 20.** As printed, the explicit
  companion misses the third-order condition $b^\top A^{\mathrm E}c^{\mathrm E}=\frac16$:
  the left side is $0.19885$, $0.0322$ too large, while every other condition of order
  $\le3$, coupling conditions included, holds to about $10^{-12}$ *(compiler check, not in
  the source; recomputed 2026-10-20 from the printed 12-digit coefficients)*. Its fourth
  explicit row, $(-0.733534082749,\ 2.150527381100,\ -0.416993298352)$, differs from
  Southworth et al.'s $(0.6304125582,\ 0.7865807402,\ -0.4169932983)$, with which the pair
  is third order. The paper nevertheless observes third-order convergence with this pair
  (Tables 8–11); the text attributes the table to one reference and the caption to another.
- **Sign slips.** Birke et al. (2024, Eqs. (32)–(34)) and Boscheri & Pareschi (2021,
  Eq. (71)) define $\mathcal H$ with $+\nabla\cdot F$; for $\partial_tq+\nabla\cdot F=0$ the
  flux terms need a minus sign.
- **Evidence.** The temporal orders of LSDIRK2 in the MHD papers are taken from the
  literature; Birke et al. show no temporal convergence test. The AP statements of the MHD
  papers are transferred or asserted, not proved for the schemes used.

# Citations

- [Boscheri & Pareschi (2021)](/sources/boscheri-2021.md) — §3.1 (Eqs. (20)–(47)), §3.4.1 (Eqs. (71)–(81)), §4.1–4.2 (Tables 1–2); arXiv v1.
- [Boscheri & Thomann (2024)](/sources/boscheri-2024.md) — §3, §3.1–3.5 (Eqs. (22)–(62)), §3.3 (Eqs. (37)–(40)), §4.1, §4.7 (Figs. 1, 12); arXiv v1.
- [Birke et al. (2024)](/sources/birke-2024.md) — §3.1 (Eqs. (22)–(26)), §3.3.1 (Eqs. (32)–(35), Table 1), Thm. 1, §4.2–4.7 (Tables 3–5, Figs. 4–5); arXiv v1.
- [Orlando et al. (2025b)](/sources/orlando-2025-b.md) — §3.3 (Eqs. (37)–(50)), §3.4 (Eqs. (51)–(54)), §4.1–4.5 (Tables 2–4, 8–16, Figs. 6, 13), §5, App. A (Table 20); arXiv v5.
- [Southworth et al. (2024)](/sources/southworth-2024.md) — §2–2.3 (Eqs. (4)–(17)), §3.2–3.3 (Eqs. (20)–(30)), §4 (Eqs. (31)–(37)), §5.1–5.3 (Figs. 7–11).
- [Buvoli & Southworth (2025)](/sources/buvoli-2025.md) — §2.2, §2.3, §3 (Fig. 3.1), §4.2 (Eq. (4.6)), §5.1, §7.2 (Fig. 7.3).
- [Buvoli et al. (2026)](/sources/buvoli-2026.md) — §4.1 (frozen-coefficient partition).
- [Tan et al. (2025)](/sources/tan-2025.md) — §1 (semi-implicit methods as the alternative to EIN).
- [Maurya et al. (2021)](/sources/maurya-2021.md) — §2.1–2.2 (Eqs. (5)–(11)), §3 (Eqs. (12)–(13), Tables 1–3), §4.1–4.2 (Eqs. (21)–(26), Table 5), §9–10 (Eqs. (36)–(42)), §12.1 (Fig. 23), §13, Table 6, App. A (Fig. 17).
