---
type: Method
title: "Paired explicit Runge–Kutta (P-ERK) methods"
description: "P-ERK families are explicit Runge–Kutta tableaux with a common stage count, abscissae and weights but different numbers of active stages, assigned per mesh region by local stiffness; one global step gives a multirate effect at second, third and fourth order, with optimized stability polynomials and an embedded stability-limit detector."
status: established
aliases: [P-ERK, PERK, paired-explicit Runge–Kutta, embedded P-ERK, multirate P-ERK, P-ERK2, P-ERK3, P-ERK4]
tags: [runge-kutta, explicit, multirate, stability, order-conditions, step-size-control]
timestamp: 2026-10-19T20:00:00Z
---

# Paired explicit Runge–Kutta (P-ERK) methods

A **paired explicit Runge–Kutta (P-ERK) family** is a set of explicit $s$-stage
tableaux $(A^{\{q\}},b,c)$ that share the abscissae $c$ and the weights $b$ but
differ in the number of **active stages**, the stages whose right-hand side is
actually evaluated (page-local: $e\le s$ the number of active stages of a member,
$e_q$ for member $q$; it is also the degree of the member's stability polynomial). A member
with many active stages has a large region of absolute stability and is assigned
to the stiff part of a method-of-lines system (small cells, fast waves); members
with few active stages are assigned elsewhere and cost less per step. All members
advance with the same global step $h$, so the family acts as a
[partitioned (GARK) Runge–Kutta method](/methods/generalized-additive-runge-kutta.md)
with partition-wise tableaux $A^{\{q\}}$ and common $b$, $c$
([Hedayati Nasab & Vermeire 2022](/sources/hedayatinasab-2022.md), §1, §3;
[Vermeire 2023](/sources/vermeire-2023.md), §1, §3;
[Doehring et al. 2025](/sources/doehring-2025.md), §1–3). The second-order family is
due to Vermeire (2019), as recalled by all three; third order is constructed by
Hedayati Nasab & Vermeire (2022), embedded pairs by Vermeire (2023), and fourth
order by Doehring et al. (2025).

## Butcher structure

All published families use the same sparse archetype. For $i\ge3$ only the first
column and the subdiagonal of $A^{\{q\}}$ are nonzero,

$$Y_i=y_n+h\bigl(a^{\{q\}}_{i,1}f(Y_1)+a^{\{q\}}_{i,i-1}f(Y_{i-1})\bigr),\qquad a^{\{q\}}_{i,1}=c_i-a^{\{q\}}_{i,i-1},$$

with $a_{2,1}=c_2$ and the row-sum condition $A\mathbf 1=c$; $b$ is nonzero only in
its last one or two entries (Hedayati Nasab & Vermeire 2022, §3.1, Eqs. (19)–(25);
Vermeire 2023, §3, Eq. (15); Doehring et al. 2025, §3.2, Eqs. (3.6)–(3.7)).
A member is reduced to $e_q$ active stages by setting the subdiagonal to zero in the
rows $3,\dots,s-e_q+2$ (Hedayati Nasab & Vermeire 2022, Eq. (22); Vermeire 2023,
Eq. (18)). Those stages become $Y_i=y_n+hc_if(Y_1)$, and their right-hand sides are
never used, so only $f(Y_1)$ and $f(Y_{s-e_q+2}),\dots,f(Y_s)$ are evaluated (Eq.
(23)). In isolation such a member is a reducible method; its inactive stages are kept
because the coupled update needs every member to have the same $c$ (Doehring et al.
2025, §3.1). Each stage reads at most two earlier stage derivatives, so the cost per
stage is constant and storage does not grow with $s$: Hedayati Nasab & Vermeire count
three stage derivatives held at once for the third-order family (Eq. (21)), Doehring
et al. call the second- and third-order families two-register schemes (§3.1); see
[low-storage Runge–Kutta methods](/methods/low-storage-runge-kutta.md).

Implementation in a method-of-lines code only restricts the element, interface,
boundary and mortar loops to each partition's index set, interfaces and mortars
belonging to the partition of the smaller element (Doehring et al. 2025, §6.1,
Listings 1–2). Members are assigned by minimum element edge length (Hedayati Nasab &
Vermeire 2022, §5.3–5.4; Vermeire 2023, §6) or by local wave speed (Doehring et al.
2025, §2); the load imbalance of unequal stage counts is handled by multi-constraint
METIS partitioning (Vermeire 2023, §3).

## Coefficients by order

**Second order.** $c_i=\frac{i-1}{2(s-1)}$, so $c_s=\frac12$, and $b=(0,\dots,0,1)$:
the update is $y_{n+1}=y_n+hf(Y_s)$, a midpoint-type step (Vermeire 2023, Eqs.
(16)–(17)). Doehring et al. (2025, Eq. (3.5)) print the $s=6$ example
$c=(0,\frac1{10},\dots,\frac5{10})$, $b=(0,\dots,0,1)$, members with 3 and 6 active
stages.

**Third order** (Hedayati Nasab & Vermeire 2022, §3.1, Eqs. (26)–(29)). Only $c_s$,
$c_{s-1}$, $c_{s-2}$, $a_{s,s-1}$, $a_{s-1,s-2}$, $b_s$, $b_{s-1}$ enter the four
third-order conditions. Fixing $c_s=1$ gives

$$b_{s-1}=\tfrac34,\qquad b_s=\tfrac14,\qquad c_{s-1}=\tfrac13,\qquad c_{s-2}=\frac{2-a_{s,s-1}}{9\,a_{s-1,s-2}}.$$

**Fourth order** (Doehring et al. 2025, §3.2, Eq. (3.9), App. A). With
$b=(0,\dots,0,b_{s-1},b_s)$ the eight fourth-order conditions involve nine
unknowns. All members share the last three subdiagonal entries
$a_{s-2,s-3}$, $a_{s-1,s-2}$, $a_{s,s-1}$, which satisfies the coupling condition by
construction and leaves a one-parameter family:

$$\begin{aligned}
&b_{s-1}=b_s=\tfrac12,\quad c_{s-1}=\tfrac12+\tfrac{\sqrt3}6,\quad c_s=\tfrac12-\tfrac{\sqrt3}6,\quad c_{s-2}=0.479274057836310,\\
&a_{s-2,s-3}=0.114851811257441/c_{s-3},\quad a_{s-1,s-2}=0.648906880894214,\quad a_{s,s-1}=0.0283121635129678,
\end{aligned}$$

with $c_{s-3}$ free; $c_{s-1}$ and $c_s$ are the two Gauss nodes in reverse order.
Since $c_{s-3}=c_1=0$ for $s=4$, a fourth-order P-ERK needs at least five stages,
whereas second- and third-order ones exist with two and three. The stability
polynomial does not depend on $c_{s-3}$; Doehring et al. choose $c_{s-3}=1$, and in
practice $c_i=1$ for $i=2,\dots,s-3$, to reduce [internal error
amplification](/definitions/internal-stability.md) (§3.2, §4.4). Stages 1–2 and
$s-3,\dots,s$ are then common to all members and only stages $3,\dots,s-4$ are truly
partitioned: a "classic–partitioned–classic" method (§3.3, Eq. (3.10)).

## Order, consistency and conservation of the coupled method

For a partitioned method with common $c$ and $b$, the conditions up to order three
reduce to the classical ones, with $b^\top A^{\{q\}}c=\frac16$ required for each
member separately; at order four the per-member conditions
$b^\top c^3=\frac14$, $b^\top CA^{\{q\}}c=\frac18$, $b^\top A^{\{q\}}c^2=\frac1{12}$
($C=\operatorname{diag}(c)$, page-local) are joined by the coupling condition

$$b^\top A^{\{q\}}A^{\{r\}}c=\tfrac1{24}\qquad\text{for all members }q,r$$

(Doehring et al. 2025, §2.1, Eqs. (2.3)–(2.4)). Hedayati Nasab & Vermeire (2022,
§3.2, Eqs. (31)–(39)) use the same reduction to argue that any spatial mix of
third-order members is third order; it is confirmed numerically on the
[isentropic vortex](/benchmarks/isentropic-vortex.md), where all fourteen members
$e=3,\dots,16$ of the 16-stage family and a random spatial mix of them show observed
order 2.98–3.00 (§5.1, Table 2). See the
[order conditions](/results/runge-kutta-order-conditions.md).

Common abscissae are **internal consistency**, $\sum_ja^{\{q\}}_{ij}=c_i$ for all
members, equivalent to stage order one of each member; it prevents spurious
oscillations at partition interfaces (Doehring et al. 2025, §2.3, Eq. (2.13)).
Common weights give conservation of linear invariants for equation-based
partitioning (§2.4, Eq. (2.14)). Doehring et al. confirm both: the combined
three-member fourth-order scheme on an AMR mesh reproduces the density errors of
each standalone member to 4–5 digits (§5.2, Table 2), and conservation errors are
$\mathcal O(10^{-13})$–$\mathcal O(10^{-12})$, round-off level, as for Ketcheson's
SSP$(10,4)$ (§5.3, Table 3). Partition interfaces act like time-dependent internal
boundaries and could cause [order reduction](/definitions/order-reduction.md); none
is observed on their smooth periodic tests, fourth order holding on the isentropic
vortex (until the spatial error dominates) and on the Lotka–Volterra system (§5.2,
§5.4, Table 4, Fig. 6).

## Stability polynomials

The stability polynomial of a member with $e$ active stages has degree $e$. At
second and third order it has $e-p$ free coefficients, which are optimized for the
semi-discrete spectrum by the Ketcheson–Ahmadia bisection over a convex problem; see
[optimal stability polynomials](/methods/optimal-stability-polynomial.md)
(Hedayati Nasab & Vermeire 2022, §3.3; Vermeire 2023, §4). The tableau is then
recovered from the polynomial. At second order the coefficient of $z^j$ is a chain of
subdiagonal entries times one abscissa, so the entries follow sequentially from the
top degree down without a nonlinear solver (Vermeire 2023, §3, Eq. (22)); at third
order the optimal polynomial and the condition on $c_{s-2}$ form a nonlinear system
per member (Hedayati Nasab & Vermeire 2022, §4.2). At fourth order only $e-5=e-p-1$
coefficients are free, because the shared entries fix the $z^5$ coefficient through
the others. Doehring et al. (2025, §4.2, Eqs. (4.7)–(4.8), App. C) make the
polynomial affine in the products $\prod_{i=1}^ja_{e-3-i+1}$ ($j=1,\dots,e-5$; page-local
shorthand $a_k:=a_{k,k-1}$) of subdiagonal entries, so the stability constraint stays a second-order cone
constraint; optimizing the monomial coefficients first and fitting the tableau by
least squares gave "significantly inferior results". The five-stage member has
$P(z)=\sum_{j=0}^4z^j/j!+0.001055026310046423\,z^5$ (Eq. (4.4)). The constrained
polynomials reach about 85% of the unconstrained fourth-order optimal step at $e=6$,
rising to 96.5% at $e=16$ (§4.3, Figs. 1–2).

P-ERK relies on the stable step of an optimized explicit method growing about
linearly with $e$ for hyperbolic spectra: a member with $2e$ evaluations on cells of
size $\Delta x/2$ then allows the same $h$ as one with $e$ evaluations on cells of
size $\Delta x$. For diffusion-dominated spectra, whose radius grows like
$\Delta x^{-2}$, the scaling fails, and [stabilized Chebyshev-type
methods](/methods/stabilized-explicit-runge-kutta.md) are the relevant class
(Doehring et al. 2025, §3.1, Eqs. (3.2)–(3.4)). For third-order members on
flux-reconstruction DG spectra (degrees 0–8), Hedayati Nasab & Vermeire (2022,
§4.2, Table 1, Fig. 2) find the optimal step roughly linear in $e$ and the step per
active stage still increasing at $e=16$ (e.g. degree 4: 0.029895 at $e=3$, 0.046618
at $e=16$). Doehring et al. (2024) build polynomials of degree above 100 by a
root parametrization, with many-stage P-ERK members as the stated target (§1, §11);
families with more than 16 stages were previously limited by the conditioning of
the monomial optimization.

**Linear stability of the coupled scheme** does not follow from that of the members:
the partitioned method has a matrix-valued stability function, and member-wise
absolute stability is only "observed" to suffice (McLachlan, Sun & Tse, as recalled by
Doehring et al. 2025, §2.2, Eq. (2.12)). Doehring et al. check one case directly: a
two-level fourth-order family with 10 and 16 active stages on 1D advection with 2:1
refinement has a fully discrete matrix of spectral radius 1 to machine precision and
runs stably for 7672 steps (§5.1, Fig. 4). See
[linear stability of multirate methods](/definitions/multirate-linear-stability.md).

**Nonlinear stability** is weak. A partitioned SSP method needs every member to be
SSP and has step bound $h\le\min_q\mathcal C^{\{q\}}h_{\mathrm{FE}}$ (page-local
$\mathcal C^{\{q\}}$ for the members' SSP coefficients), which Doehring et al. (2025,
§2.5, Eq. (2.15)) judge "in many cases ineffective"; see
[SSP methods](/methods/strong-stability-preserving-runge-kutta.md). Sharing the final
stages of the members reduces interface oscillations: a second-order family with 8
and 16 active stages whose last 6 stages are shared shows much smaller oscillations
on 1D upwind advection, at the price of an optimal step about 64.3% of the
unconstrained one (App. B, Fig. B.13).

## Embedded P-ERK and stability-limited step control

Vermeire (2023, §3, Eqs. (15)–(20)) adds to each second-order member with $e$ active
stages a **first-order embedded method with $e-1$ active stages**: $\hat b_s=0$,
$\hat b_i=0$ on the inactive stages, $\hat b_1=1-\sum_{i=2}^{s-1}\hat b_i$, leaving
$e-2$ free entries of $\hat b$ next to the $e-2$ free subdiagonal entries. The
embedded polynomial (degree $e-1$, first order) is optimized to have a region of
absolute stability *slightly smaller* than the main one, and $\hat b$ follows from a
triangular linear system. The difference $y_{n+1}-\hat y_{n+1}$ then grows just
before the main method goes unstable, so the pair is a stability-limit detector more
than an accuracy estimator; the main second-order solution advances. The embedded
weights differ between members, so the embedded solution is not conservative, which
Vermeire accepts because it never advances the solution. For flux-reconstruction DG
on 1D advection the embedded/main ratio of maximal stable CFL numbers is about 60% at
few active stages and about 93% at $e=16$ (e.g. degree 1, $e=8$: 1.71 and 1.49;
degree 8, $e=16$: 0.30 and 0.28; §4, Table 1, Fig. 2). For degree 1 the embedded
region coincides with the main region of the member with one fewer active stage.

The [step-size controller](/methods/step-size-control.md) is the PID controller with
Fekete et al.'s gains, in registry form $(\beta_1,\beta_2,\beta_3)=(0.58,-0.21,0.10)$,
a step factor limited to $[0.1,1.2]$, safety factor 0.9 and
$\mathrm{atol}=\mathrm{rtol}=10^{-4}$, values tuned to approach the stability limit
without exceeding it; P, PI and Gustafsson controllers gave more rejections (§5, Eqs.
(29)–(34)). The cited justification is that for high-order spatial discretizations
the stable step introduces little temporal error relative to the spatial error
(§2.2). Error-based control for fourth-order P-ERK is left open by Doehring et al.
(2025, §6), whose runs use constant-CFL control. See also
[embedded pairs](/methods/embedded-runge-kutta-pair.md).

## Performance

| Family | Baseline | Measure | Range | Source |
|---|---|---|---|---|
| third order, $s=16$, members $e\in\{3,4,8,12,16\}$ | classical three-stage RK3 | wall-clock speedup; step ratio | 4.06–4.51; 7.28–8.21 | Hedayati Nasab & Vermeire 2022, Tables 3–5 |
| second order embedded, $s=16$, $e\in\{3,8,16\}$ | Bogacki–Shampine 3(2) | speedup | 4.95–7.11 | Vermeire 2023, Tables 2–4 |
| fourth order, multirate | optimized standalone methods (P-ERK, Niegemann–Diehl–Busch, Toulorge–Desmet, Ranocha et al., Kennedy–Carpenter–Lewis, others) and RK4 | runtime ratio; RHS-evaluation ratio | 1.20–4.77; 1.38–4.52 | Doehring et al. 2025, Tables 5–9 |

The test cases are compressible Navier–Stokes and Euler computations with
high-order flux reconstruction or DGSEM: SD7003 airfoil (laminar and turbulent),
tandem spheres, cylinder, heaving and pitching NACA 0012 on a deforming mesh, stalled
NACA 0020, 3D linearized Euler with variable sound speed ($>10^8$ degrees of
freedom), isentropic vortex on AMR meshes and a coupled Euler/acoustic vortex pair.
Lift and drag agree with the baseline integrators and with the literature (e.g.
SD7003 $C_L=0.3827$, $C_D=0.04995$ at fourth order against 0.3841/0.04990 at second
and 0.3848/0.04910 at third; Doehring et al. 2025, Table 8). Doehring et al. realize
only about half the theoretical speedup, because their DG code is memory-bound and
partitioning loses data locality (§6.2), and they ask that the earlier speedups,
measured against three-stage third-order baselines, be compared with theirs against
RK4 rather than against optimized methods.

## Relation to multirate methods

P-ERK obtains a multirate effect with one global step and partition-dependent stage
counts, without interpolating or extrapolating interface values. Hedayati Nasab &
Vermeire (2022, §1) and Doehring et al. (2025, §1) contrast it with
[multirate GARK](/methods/multirate-gark.md) and local time stepping. Doehring et al.
(2024, §1) state that consistency and conservation "are not trivially satisfied by
other classical multirate methods". The alternatives named for locally stiff
problems are [IMEX](/methods/imex-runge-kutta.md) and accelerated IMEX schemes, which
need implicit solves (Hedayati Nasab & Vermeire 2022, §1; Vermeire 2023, §1).

## Qualifications

- **Equal abscissae at third order.** The construction needs every member to have
  the same $c$, but the formula for $c_{s-2}$ depends on each member's own
  $a_{s,s-1}$ and $a_{s-1,s-2}$, which come from its optimized polynomial;
  Hedayati Nasab & Vermeire (2022) do not say how $c_{s-2}$, $c_{s-3},\dots$ are kept
  equal, and print no coefficients (supplementary material). The observed third order
  of the random mix is the evidence. For $e=3$ the subdiagonal entry $a_{s-1,s-2}$
  is zero and the $c_{s-2}$ formula divides by zero; that member must instead have
  $a_{s,s-1}=2$, not discussed in the paper (reader's observations).
- **Which property comes from which equality.** Hedayati Nasab & Vermeire (2022,
  §3.2) state that equal $b$ and equal $c$ make the schemes "consistent and
  conservative, respectively", which reads as equal weights giving consistency;
  Doehring et al. (2025, §2.3–2.4) and GARK theory tie consistency to equal $c$ and
  conservation to equal $b$. The first is read here as a slip of order.
- **Speedup claims.** Vermeire (2023) states speedups "in excess of 7 … for all
  considered test cases" in the Conclusions; the tables give maxima 7.00, 7.11 and
  6.23. Hedayati Nasab & Vermeire (2022) state "up to four" in the abstract while
  their tables reach 4.51. Doehring et al. (2025, §7) summarize runtime savings as
  "40% to 280%", meaning runtime ratios up to 3.86. All speedups compare at
  stability-limited steps; no work–precision curves are given, and Vermeire (2023)
  compares a second-order method with a third-order pair. Vermeire's NACA 0020
  baseline was run only about $10$ convective times from a P-ERK restart.
- **Printed slips.** Hedayati Nasab & Vermeire (2022) print the free-coefficient sum
  of the optimized polynomial from $j=3$ (Eq. (40); the free coefficients start at
  $j=4$) and step sizes $5\times10^{-2}$ in Table 2 where $5\times10^{-3}$ is meant.
  Doehring et al. (2025) print the fourth order-condition with $c_{s-1}$, $c_s$ where
  $c_{s-2}$, $c_{s-1}$ are meant (Eq. (A.1d)); the values (3.9) satisfy the correct
  form. Vermeire (2023) prints, for degree 1, equal main and embedded CFL numbers at
  $e=15$ and $e=16$ (Table 1), against his statement that the embedded value is always
  smaller; the pattern $\hat\nu_{\max}(e)=\nu_{\max}(e-1)$ he states would give 3.00 and 3.22
  ($\nu_{\max}$, $\hat\nu_{\max}$ the main and embedded maximal stable Courant numbers).
- The P-ERK sources write $\Delta t$ for the step, $e$ (Hedayati Nasab & Vermeire, Vermeire)
  or $E$ (Doehring et al.) for active stages, $S$ or $s$ for stages, and $\gamma_j$ or
  $\alpha_j$ for polynomial coefficients; here $h$, $e$ (page-local),
  $s$ and $\theta_j$.

# Citations

- [Hedayati Nasab & Vermeire (2022)](/sources/hedayatinasab-2022.md) — §1, §3.1 (Eqs. 19–30), §3.2 (Eqs. 31–39), §3.3, §4.2 (Table 1, Fig. 2), §5.1 (Table 2), §5.2–5.4 (Tables 3–6).
- [Vermeire (2023)](/sources/vermeire-2023.md) — §1, §2.2, §3 (Eqs. 15–23), §4 (Table 1, Figs. 1–2), §5 (Eqs. 29–34), §6 (Tables 2–4).
- [Doehring et al. (2025)](/sources/doehring-2025.md) — §2.1–2.5 (Eqs. 2.3–2.15), §3.1–3.3 (Eqs. 3.2–3.10), §4.2–4.4, §5.1–5.4, §6.1–6.5 (Tables 5–9), App. A–C.
- [Doehring et al. (2024)](/sources/doehring-2024.md) — §1, §11 (many-stage polynomials for P-ERK; multirate comparison).
- [Hedayati Nasab et al. (2021)](/sources/hedayatinasab-2021.md) — §1 (P-ERK as consumer of optimized polynomials, previously from 1D spectra only).
