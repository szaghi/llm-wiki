---
type: Method
title: "Relaxation Runge–Kutta methods"
description: "Relaxation rescales each Runge–Kutta update by a scalar root γn of one entropy equation so that a convex entropy or invariant is conserved or dissipated at the fully discrete level; placed at tn+γnh it keeps order p, placed at tn+h (IDT) it loses one order. Variants cover IMEX, multirate, ADER, several invariants, FSAL pairs and adjoints."
status: established
aliases: [RRK, relaxation RK, relaxation method, incremental direction technique, IDT, multiple-relaxation Runge–Kutta, MRRK, FSAL-R, R-FSAL, global relaxation, local relaxation]
tags: [runge-kutta, structure-preserving, explicit, imex, multirate, step-size-control, relaxation, entropy-stability]
timestamp: 2026-10-20T16:00:00Z
---

# Relaxation Runge–Kutta methods

A relaxation Runge–Kutta method takes the update of a baseline Runge–Kutta
method and scales it by a scalar **relaxation parameter** $\gamma_n$. The
parameter is chosen at every step so that a convex functional $\eta(y)$ (an
entropy, an energy or an invariant) changes from $y_n$ to the new solution
exactly as the semi-discrete system says it should. Relaxation was introduced
by Ketcheson (2019) and generalized by Ranocha, Lóczi, Ketcheson and coauthors
(2020), as recalled by every source below. With the baseline stage values
$Y_i$ and update $y_{n+1}$,

$$y^{\gamma}_{n+1}=y_n+\gamma_n\,(y_{n+1}-y_n)=y_n+\gamma_n h\sum_{i=1}^sb_if(t_n+c_ih,Y_i)$$

([Kang & Constantinescu (2022)](/sources/kang-2022.md), §2.1;
[Bencomo & Chan (2023)](/sources/bencomo-2023.md), Eq. (11);
[Al Jahdali et al. (2022)](/sources/aljahdali-2022.md), Eq. (1);
[Bleecke & Ranocha (2026)](/sources/bleecke-2026.md), Eq. (7);
[Biswas & Ketcheson (2023)](/sources/biswas-2023-b.md), Eq. (5c)). The
integration continues from $y^{\gamma}_{n+1}$, so in this page $y_n$ always
denotes the previous relaxed solution. $\gamma_n=1$ recovers the baseline
method. The relaxed solution is a point on the secant through $y_n$ and
$y_{n+1}$; the question of **which time it approximates** separates the two
variants below.

## The relaxation equation

Write $d_n=y_{n+1}-y_n$ for the step direction and

$$e_n=h\sum_{i=1}^sb_i\big\langle\eta'(Y_i),f(t_n+c_ih,Y_i)\big\rangle$$

for the quadrature estimate of the entropy production over the step
(page-local symbols $d_n$, $e_n$; Bencomo & Chan write $d_k$, $e_k$). The
relaxation parameter is the nonzero root, closest to one, of

$$r_n(\gamma)=\eta(y_n+\gamma d_n)-\eta(y_n)-\gamma\,e_n=0$$

(Bencomo & Chan (2023), Eq. (12); Kang & Constantinescu (2022), $\theta(\gamma)$
in §2.1). $\gamma=0$ is always a root, which is why the nonzero one is taken;
Bencomo & Chan say "the non-zero root (closest to one)" in §2.2 and "the positive
root near 1 (for $\Delta t$ small enough)" in their appendix.

**Entropy stability.** At the root,
$\eta(y^{\gamma}_{n+1})-\eta(y_n)=\gamma_ne_n$. If the semi-discretization is
entropy dissipative, $\langle\eta'(y),f(y)\rangle\le0$ for all $y$, then
$e_n\le0$ when every $b_i\ge0$, and $\gamma_n>0$ gives
$\eta(y^{\gamma}_{n+1})\le\eta(y_n)$; if it is entropy conservative, $e_n=0$ and
$\eta(y^{\gamma}_{n+1})=\eta(y_n)$ (Kang & Constantinescu (2022), §2.1). This
is why Al Jahdali et al. (2022, §2.1) select only baseline methods with
positive weights. For a conserved invariant the target reduces to
$\eta(y^{\gamma}_{n+1})=\eta(y_n)$, the form written by Bleecke & Ranocha
(2026, §1) and Biswas & Ketcheson (2023, Eq. (6)); the two forms coincide
because $e_n=0$ identically when $\langle\eta'(y),f(y)\rangle=0$ for all $y$
*(compiler check, not in the sources)*. The fully discrete property is the
subject of [entropy stability](/properties/entropy-stability.md).

**Quadratic entropy.** For $\eta(y)=\tfrac12\lVert y\rVert^2$ the equation is
quadratic in $\gamma$ and its nonzero root is explicit:

$$\gamma_n=\frac{2h\sum_ib_i\big\langle Y_i-y_n,\,f(t_n+c_ih,Y_i)\big\rangle}{\lVert y_{n+1}-y_n\rVert^2},$$

for a nonstationary step (Kang & Constantinescu (2022), Cor. 2.1.1). Bencomo &
Chan (2023, Eq. (19)) give the same root for a linear skew-symmetric system
$y'=Sy$ as $\gamma_n=-2\langle y_n,d_n\rangle/\lVert d_n\rVert^2$, and
[Gaburro et al. (2023)](/sources/gaburro-2023.md) (Example 4.5, Eq. (42)) the
ADER analogue; the three agree, because
$\langle Y_i,SY_i\rangle=0$ *(compiler check, not in the sources)*. Ketcheson's
original setting is exactly this inner-product-norm case.

## Where the relaxed solution lives: RRK and IDT

* **Relaxation Runge–Kutta (RRK)** assigns $y^{\gamma}_{n+1}$ to the time
  $t_n+\gamma_nh$: the step length becomes $\gamma_nh$ (Kang & Constantinescu
  (2022), §2.1; Bleecke & Ranocha (2026), $t^{n+1}_\gamma=t^n+\gamma\Delta
  t_n$; Gaburro et al. (2023), Eq. (35); Biswas & Ketcheson (2023), Eq. (5c)).
* **The incremental direction technique (IDT)** of Calvo et al. uses the same
  $\gamma_n$ but assigns the result to $t_n+h$ (Kang & Constantinescu (2022),
  Remark 2; Bencomo & Chan (2023), §2.2).

Bencomo & Chan reserve the name "relaxation RK" for the time-adjusted variant
and call the other IDT; the other sources use "relaxation" for the family.

**Accuracy.** If the baseline method has order $p\ge2$, then under technical
assumptions the root exists and is unique for small $h$, with
$\gamma_n=1+O(h^{p-1})$; RRK then has order $p$, while IDT has order $p-1$
(Bleecke & Ranocha (2026), Eq. (3); Biswas & Ketcheson (2023), §2;
Gaburro et al. (2023), §4.2; Bencomo & Chan (2023), §2.2; Kang &
Constantinescu (2022), Remark 2, all recalling Ketcheson (2019) and Ranocha,
Lóczi & Ketcheson (2020)). The numbers show it. On inviscid Burgers with an
entropy-conservative DG flux and $h=7.813\times10^{-5}$, second-order IMEX gives
errors $6.27\times10^{-8}$ (plain), $5.81\times10^{-8}$ (relaxation) and
$8.49\times10^{-6}$ (IDT); IDT converges at order 0.94–1.00 and the third-order
IDT at 2.00–2.01, while relaxation keeps 2.00 and 2.98–3.00 (Kang &
Constantinescu (2022), Tables 2–3). The loss is not always visible at moderate
times: with a multirate method at $t=0.2$ IDT still converged at order 2
because $\lvert\gamma_n-1\rvert$ was about $10^{-5}$ and the error had not yet
accumulated; after the shock ($t=1$) its error was at least 60 times larger
than with relaxation and its order fell to 0.95 (Table 4). See
[Burgers equation](/benchmarks/burgers-equation.md).

How far $\gamma_n$ departs from one tracks the accuracy. For relaxed ADER-DG,
$\gamma_n\approx1.004$–$1.005$ at second order, $1.0005$ at third and
$\approx1.0000$ at fourth order on a smooth advected bump, and up to about 1.2
and 1.35 with a contact discontinuity and the "123" problem (Gaburro et al.
(2023), Figs. 2, 13, 17).

## Solving for the relaxation parameter

The scalar equation is solved once per step, with all stage data fixed.

* Al Jahdali et al. (2022, §2.2, Tables 2–3) compared seven root finders
  (bisection, Brent, Newton, secant, simplified Newton, TOMS 748 in two
  variants) for global and local relaxation on compressible isotropic
  turbulence and a 3D cylinder, 1,000 steps each with the classical
  fourth-order method, tolerance $10^{-12}$: only the secant method succeeded
  in every case; Newton and simplified Newton failed most often, even with up
  to 1,000 iterations.
* Bencomo & Chan (2023, §3) use bisection; Bleecke & Ranocha (2026, §3) the
  Alefeld–Potra–Shi Algorithm 748; Kang & Constantinescu (2022, §2.1) list
  Brent, Levenberg–Marquardt or Newton; Gaburro et al. (2023, Eq. (37)) use
  scalar Newton with $\mathrm dr_n/\mathrm d\gamma$ in closed form.

**Global and local relaxation.** For a spatially discretized problem the
entropy is a sum over cells. *Global* relaxation solves one equation for the
total entropy; *local* relaxation solves one per cell and takes the
minimum of the cell roots (Al Jahdali et al. (2022), §2, citing Ranocha et
al. 2020 for both). The two cost the same number of right-hand-side
evaluations in their tests (Table 4).

## Variants

### Additive (IMEX) methods

For an [IMEX method](/methods/imex-runge-kutta.md), relaxation scales the
combined update,
$y^{\gamma}_{n+1}=y_n+\gamma_nh\sum_i\big(b^{\mathrm E}_if^{\mathrm E}(Y_i)+b^{\mathrm I}_if^{\mathrm I}(Y_i)\big)$,
with the production estimate built from the same weighted sum (Kang &
Constantinescu (2022), Eqs. (12)–(14), Prop. 2.1). When
$b^{\mathrm E}\ne b^{\mathrm I}$, the proof needs each part entropy stable on its
own, $\langle\eta'(y),f^{\mathrm E}(y)\rangle\le0$ and
$\langle\eta'(y),f^{\mathrm I}(y)\rangle\le0$; when the weights coincide only the
sum has to be (Cor. 2.1.1). Biswas & Ketcheson (2023, §6) relax the
Kennedy–Carpenter ARK3(2)4L[2]SA and ARK4(3)6L[2]SA methods for the energy of a
stiff KdV semi-discretization.

### Multirate methods

Kang & Constantinescu (2022, §2.3, Props. 2.2–2.3) relax the second-order
multirate partitioned method MRK2 of Constantinescu and Sandu with **one
global** $\gamma_n$ shared by all zones and refinement levels; the
production estimate sums over zones, level blocks, substeps and stages. The
entropy guarantee then holds only at the synchronization time of the coarsest
level, not inside stages or substeps, so the authors recommend
entropy-stable rather than entropy-conservative fluxes for deep nesting; with
an entropy-stable flux the relaxed method ran stably on 10 nested levels
(§3.3, Fig. 16). See [multirate GARK](/methods/multirate-gark.md).

### ADER

Gaburro et al. (2023, §4.2) apply relaxation to one
[ADER](/methods/ader-time-integration.md) predictor–corrector step: the
increment $u^{n+1}_h-u^n_h$ is scaled by $\gamma_n$, the time advanced by
$\gamma_nh$, and the production estimate is the time quadrature of the spatial
entropy balance evaluated on the predictor (Eqs. (33)–(34)), not a sum over
Runge–Kutta stages. Dropping the upwind dissipation terms from that target
forces exact entropy conservation in time.

### Several invariants (MRRK)

To conserve $\kappa$ invariants $\eta_1,\dots,\eta_\kappa$ (page-local count
$\kappa$), Biswas & Ketcheson (2023, §3, Eqs. (9)–(11)) take $\kappa$ linearly
independent methods sharing $A$, with weights $b^{(1)},\dots,b^{(\kappa)}$
(page-local), directions $d^{(k)}_n=h\sum_jb^{(k)}_jf(t_n+c_jh,Y_j)$, and

$$y^{\gamma}_{n+1}=y_{n+1}+\sum_{k=1}^{\kappa}\gamma_{n,k}\,d^{(k)}_n\quad\text{at }t_n+\Big(1+\sum_k\gamma_{n,k}\Big)h,$$

with $y_{n+1}$ the solution of the first method and the $\gamma_{n,k}$ solving
the $\kappa\times\kappa$ system $\eta_k(y^{\gamma}_{n+1})=\eta_k(y_n)$. The
parameters are near zero, not near one: for $\kappa=1$, $\gamma_{n,1}$
corresponds to $\gamma_n-1$ *(compiler check, not in the sources:
$y_n+\gamma_n(y_{n+1}-y_n)=y_{n+1}+(\gamma_n-1)d^{(1)}_n$)*. No extra
right-hand-side evaluation is needed.

* **Lemma 4.1.** If $(A,b^{(1)})$ has order $p\ge2$, $y_n=y(t_n)$, and the
  $\kappa\times\kappa$ leading matrix of $\eta'(y_{n+1})^\top[d^{(1)}_n|\dots|d^{(\kappa)}_n]$,
  which is $O(h)$, is non-singular, then for small $h$ a unique solution exists
  with $\gamma_{n,k}=O(h^{p-1})$ (proof by the implicit function theorem).
* **Theorem 4.2.** With orders $p\ge2$ for the first method and $\ge1$ for the
  others, MRRK has order $p-1$ read at $t_n+h$ and order $p$ read at the
  relaxed time.

On the free rigid body, a bi-Hamiltonian Lotka–Volterra system and the
[Kepler problem](/benchmarks/kepler-problem.md) (three invariants), MRRK keeps
every invariant to round-off and its error grows linearly, against quadratic
growth for the baselines (§5, Figs. 1–10). Biswas & Ketcheson construct new
embedded weight vectors for SSPRK(2,2), SSPRK(3,3), Heun(3,3), the classical
RK4, RKF45 and DOPRI5 (App. A). They found the update based at $y_{n+1}$ more
robust than one based at $y_n$, and that some baselines need smaller steps for
a solution to exist at every step (§5).

MRRK is a variant of the directional projection of Calvo et al. (2006), which
also uses embedded methods but keeps the step time: MRRK needs one embedded
method fewer for the same number of invariants (§3), and the two gave
comparable results (no data shown, §5). Relaxation and directional projection
are both **oblique projections**, which keep linear invariants while enforcing
nonlinear ones, unlike orthogonal projection (§1).

### FSAL pairs and step-size control

An [FSAL embedded pair](/methods/embedded-runge-kutta-pair.md) reuses
$f(y_{n+1})$ as the first stage of the next step. Relaxation breaks the reuse,
because the next step starts from $y^{\gamma}_{n+1}$; the "naive" combination
used in OrdinaryDiffEq.jl and SUNDIALS costs one extra right-hand-side
evaluation per step (Bleecke & Ranocha (2026), §1). Two fixes use the linear
structure of the update:

* **FSAL-R** (control first, then relax): replace $f(y^{\gamma}_{n+1})$ by
  $f(y_n)+\gamma_n\big(f(y_{n+1})-f(y_n)\big)$. Lemma 1: for $g\in C^2$,
  $g(y^{\gamma}_{n+1})=g(y_n)+\gamma_n\big(g(y_{n+1})-g(y_n)\big)+O(h^{p+1})$,
  from $\gamma_n=1+O(h^{p-1})$. Theorem 1: the main and embedded local errors
  keep orders $O(h^{p+1})$ and $O(h^p)$ (§2.1, Eqs. (8)–(14)).
* **R-FSAL** (relax first, then estimate): compute $f(y^{\gamma}_{n+1})$, use
  $f(y_n)+\gamma_n^{-1}\big(f(y^{\gamma}_{n+1})-f(y_n)\big)$ in place of
  $f(y_{n+1})$ in the embedded solution, relax the embedded solution with the
  same $\gamma_n$ and compare both at the relaxed time (Lemma 2, Eq. (17),
  Theorem 2). Rejected steps then also pay the root solve, since relaxation precedes the
  estimate *(compiler remark, not in the sources)*.

On the [BBM equation](/benchmarks/benjamin-bona-mahony-equation.md) with BS3
and DP5, both reach the accuracy of the naive scheme at the baseline's
evaluation count, "roughly 25%" more accurate than the baseline at equal work
(§3, Fig. 1). FSAL-R keeps the core structure of software libraries and is
recommended for general use; R-FSAL is preferred for dissipative problems,
where the entropy estimates relaxation needs cannot be used directly with
FSAL-R (§4). Relaxation is available in recent ARKODE (footnote 1; see
[ARKODE](/software/arkode.md)). See also
[step-size control](/methods/step-size-control.md).

### End of the integration interval

Because RRK steps have length $\gamma_nh$, a fixed final time $T$ is not hit
exactly. Bencomo & Chan (2023, §2.2.3, Eq. (24)) take the last step as an IDT
step with the corrected length $T-t_{N-1}$ (page-local $N$ steps), which
depends on all earlier $\gamma_n$. The consequences for derivatives are on
[discrete adjoints](/methods/discrete-adjoint-runge-kutta.md).

## Cost

Al Jahdali et al. (2022, §3, Table 4) ran 600 steps of the Imperial front wing
(3.4M hexahedra) and the NASA Common Research Model (9.1M hexahedra) with an
entropy-stable DG solver on 512 cores. All runs were stable even without
relaxation. With a CFL-based step, relaxation left the number of evaluations
nearly unchanged (e.g. 6,624 without, 6,636 global, 6,628 local for a
second-order method on the front wing), which they read as $\gamma_n\approx1$.
With error-based PID control the count rose by about 33% (4,250 to
5,648/5,652 for the third-order Bogacki–Shampine pair, wall time
$1.41\times10^3$ to $1.83\times10^3$ s). Global and local relaxation cost about
the same. Their conclusion: if entropy stability is wanted, fifth- and
sixth-order relaxation methods with error-based control cost practically the
same as low-order schemes. Bleecke & Ranocha (2026, §1) cite this study for the
extra-evaluation cost that FSAL-R and R-FSAL remove.

## Relation to other methods

* **Superviscosity filter.** The adaptive filter of
  [superviscosity-stabilized RK](/methods/superviscosity-stabilized-runge-kutta.md)
  is modelled on relaxation ([Sun & Shu (2021)](/sources/sun-2021.md), §5);
  both [Sun & Shu (2021)](/sources/sun-2021.md) (§1) and
  [Sun et al. (2022)](/sources/sun-2022.md) (§1) cite relaxation as the
  alternative remedy when an explicit method is not
  [strongly stable](/properties/strong-stability.md).
* **Pseudo-energy-preserving methods** make the energy error small by design
  instead of zero by projection; de León et al. list relaxation among
  the exact alternatives ([pseudo-energy-preserving RK](/methods/pseudo-energy-preserving-runge-kutta.md)).
* **Step-size control.** [Ranocha et al. (2022)](/sources/ranocha-2022.md)
  cite relaxation as the route to fully discrete entropy stability for the
  error-controlled methods they optimize; Bencomo & Chan (2023, §2.2) note that
  RRK resembles adaptive time stepping.
* **Other bases.** Kang & Constantinescu (2022, §1) and Gaburro et al. (2023)
  cite extensions to [deferred correction](/methods/deferred-correction.md);
  Ranocha, Lóczi & Ketcheson (2020) cover multistep methods, as recalled by
  Gaburro et al. (§4.2).

## Qualifications

* **Positive weights.** The dissipation argument needs $b_i\ge0$ and
  $\gamma_n>0$; Kang & Constantinescu (2022) use both in §2.1 but omit them from
  the hypotheses of Prop. 2.1, and do not discuss existence or positivity of
  $\gamma_n$ for their IMEX and multirate methods. For conservation alone the
  weights may be negative: Biswas & Ketcheson (2023) relax RKF45, whose
  fifth-order weights include $-9/50$ (App. A).
* **ADER order.** Gaburro et al. (2023, §4.2) import existence, $\gamma_n=1+O(h^{p-1})$
  and order $p$ from the Runge–Kutta theory without checking its hypotheses
  for a predictor–corrector step whose production target is computed on the
  predictor. For ADER the order statement is unproved; their tests show the
  design order, with second-order rates of 1.78–1.84 on one advection test
  (Table 1).
* **Time placement unstated.** Al Jahdali et al. (2022, Eq. (1)) print only
  the solution update, not whether time advances by $\gamma_nh$ or $h$.
* **MRRK hypotheses.** Biswas & Ketcheson require each embedded method to have
  "order at least 2" in §3 while Theorem 4.2 needs only order 1 for the
  others and their SSPRK(2,2) set uses a first-order second method. The
  non-singularity hypothesis of Lemma 4.1 is not verified for any example.
* **Al Jahdali et al. (2022) data.** On the front wing all five
  error-controlled schemes (4 to 9 stages) report identical evaluation counts
  (4,250 / 5,648 / 5,652), and the counts are hard to reconcile with "600 time
  steps". The claim that relaxation always costs more evaluations has
  exceptions in their Table 4 (e.g. SSP3(2)4[3S*+] on the CRM, 1,352 relaxed
  against 1,356 plain); their conclusion's "almost on par or greater" is the
  accurate wording.
* **Priority claim for IMEX relaxation.** Biswas & Ketcheson (2023, §7,
  arXiv v1 read) state that they "demonstrate for the first time the
  application of relaxation in combination with additive (ImEx) RK methods
  for stiff problems". Kang & Constantinescu had already defined, proved and
  tested relaxation IMEX Runge–Kutta methods (Kennedy–Carpenter ARK methods
  with the implicit part taken for stiffness, on Burgers; Prop. 2.1,
  Cor. 2.1.1, §3.2), in an arXiv preprint of August 2021 and in the
  2022 journal version, and Gaburro et al. (2023, §4.2) cite that work as
  relaxation for IMEX and multirate methods. Biswas & Ketcheson do not cite
  Kang & Constantinescu. The claim is a statement about the literature, not a
  technical result that another source contests, and the publication record
  settles it: the earlier work exists. Their contribution stands as relaxation
  with IMEX methods for a stiff dispersive (KdV) semi-discretization, not as
  the first combination.

* **Printed slips.** Bleecke & Ranocha (2026) write the base point as $u^n$ in
  the introduction and Eq. (11) but $u^n_\gamma$ in Eq. (7) (notational); Kang &
  Constantinescu (2022) print $b_i$ without its zone superscript in Eq. (17)
  and call $\lvert\gamma_n-1\rvert=O(10^{-5})$ "tiny relaxation parameters";
  Biswas & Ketcheson (2023, Table 4) print Heun's third-order weights as
  $(1/4,0,1/4)$ for $(1/4,0,3/4)$.

# Citations

- [Kang & Constantinescu (2022)](/sources/kang-2022.md) — §2.1 (RRK, $\theta(\gamma)$, dissipation argument), Remark 2 (IDT), §2.2 (Eqs. (12)–(14), Prop. 2.1, Cor. 2.1.1), §2.3 (Props. 2.2–2.3), §3 (Tables 2–4, Fig. 16), §4.
- [Bleecke & Ranocha (2026)](/sources/bleecke-2026.md) — §1 (Eqs. (3)–(7), naive FSAL cost, footnote 1), §2.1 (Lemma 1, Theorem 1), §2.2 (Lemma 2, Eq. (17), Theorem 2), §3 (Fig. 1), §4.
- [Bencomo & Chan (2023)](/sources/bencomo-2023.md) — §2.2 (Eqs. (11)–(12), IDT vs RRK, orders), Eq. (19), §2.2.3 (Eq. (24)), §3, appendix.
- [Biswas & Ketcheson (2023)](/sources/biswas-2023-b.md) — §1, §2 (Eqs. (5c)–(6)), §3 (Eqs. (9)–(11)), §4 (Lemma 4.1, Theorem 4.2), §5, §6, §7, App. A.
- [Al Jahdali et al. (2022)](/sources/aljahdali-2022.md) — §2 (Eq. (1), global and local relaxation), §2.1, §2.2 (Tables 2–3), §3 (Table 4), §4.
- [Gaburro et al. (2023)](/sources/gaburro-2023.md) — §4.2 (Eqs. (29)–(37)), Example 4.5 (Eq. (42)), §5 (Table 1, Figs. 2, 13, 17).
- [Sun & Shu (2021)](/sources/sun-2021.md) — §1, §5 (filter modelled on relaxation).
- [Sun et al. (2022)](/sources/sun-2022.md) — §1 (relaxation as remedy).
- [Ranocha et al. (2022)](/sources/ranocha-2022.md) — relaxation cited for fully discrete entropy stability.
- [de León et al. (2025)](/sources/deleon-2025.md) — §1 (relaxation among exact-conservation approaches).
