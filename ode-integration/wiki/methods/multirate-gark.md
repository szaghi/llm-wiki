---
type: Method
title: "Multirate GARK methods (MrGARK, compound-fast, multirate backward Euler)"
description: "Multirate GARK methods advance a slow partition with one macro step and a fast partition with m micro steps of the same base method; the page gives the standard and compound-fast forms, their order conditions, the implicit–implicit methods of orders one to four, their stability angles and their cost."
status: established
aliases: [MrGARK, multirate generalized additive Runge–Kutta, compound-fast MrGARK, multirate backward Euler, multirate implicit midpoint, implicit multirate GARK]
tags: [multirate, runge-kutta, implicit, stiff, order-conditions, stability]
timestamp: 2026-10-20T03:00:00Z
---

# Multirate GARK methods (MrGARK, compound-fast, multirate backward Euler)

A multirate GARK (MrGARK) method integrates $y'=f^{\{\mathrm f\}}(y)+f^{\{\mathrm s\}}(y)$
by taking one macro step $H$ with a slow base method and $m$ micro steps
$h=H/m$ with a fast base method, the two coupled through stage-dependent
coefficients. It is a [GARK method](/methods/generalized-additive-runge-kutta.md)
whose fast block repeats the fast base method $m$ times, as recalled by
[Roberts et al. (2021)](/sources/roberts-2021.md) (§2.1, eqs. 2.4–2.5, after
Günther & Sandu). Roberts et al. treat **both** partitions implicitly, develop a
second family, *compound-fast* MrGARK, and build methods of orders one to four.
Throughout this page $\ell=0,\dots,m-1$ indexes the micro steps (registry
notation; the source writes $\lambda=\ell+1=1,\dots,M$ for it, and $M$ for the
ratio $m$; its formulas are shifted accordingly).

## Standard MrGARK

With slow base $(A^{\{\mathrm s,\mathrm s\}},b^{\{\mathrm s\}})$, fast base
$(A^{\{\mathrm f,\mathrm f\}},b^{\{\mathrm f\}})$ and coupling matrices
$A^{\{\mathrm s,\mathrm f,\ell\}}$, $A^{\{\mathrm f,\mathrm s,\ell\}}$
(Roberts et al. 2021, eq. 2.4):

$$\begin{aligned}
Y^{\{\mathrm s\}}_i&=y_n+H\sum_j a^{\{\mathrm s,\mathrm s\}}_{ij}f^{\{\mathrm s\}}\big(Y^{\{\mathrm s\}}_j\big)+h\sum_{\ell=0}^{m-1}\sum_j a^{\{\mathrm s,\mathrm f,\ell\}}_{ij}f^{\{\mathrm f\}}\big(Y^{\{\mathrm f,\ell\}}_j\big),\\
Y^{\{\mathrm f,\ell\}}_i&=\tilde y_{n+\ell/m}+H\sum_j a^{\{\mathrm f,\mathrm s,\ell\}}_{ij}f^{\{\mathrm s\}}\big(Y^{\{\mathrm s\}}_j\big)+h\sum_j a^{\{\mathrm f,\mathrm f\}}_{ij}f^{\{\mathrm f\}}\big(Y^{\{\mathrm f,\ell\}}_j\big),\\
\tilde y_{n+(\ell+1)/m}&=\tilde y_{n+\ell/m}+h\sum_i b^{\{\mathrm f\}}_if^{\{\mathrm f\}}\big(Y^{\{\mathrm f,\ell\}}_i\big),\qquad
y_{n+1}=\tilde y_{n+1}+H\sum_i b^{\{\mathrm s\}}_if^{\{\mathrm s\}}\big(Y^{\{\mathrm s\}}_i\big).
\end{aligned}$$

In GARK form the fast block is block lower triangular with
$\frac1mA^{\{\mathrm f,\mathrm f\}}$ on its diagonal and
$\frac1m\mathbf 1b^{\{\mathrm f\}\top}$ below it, so the full method has
$ms^{\{\mathrm f\}}$ fast and $s^{\{\mathrm s\}}$ slow stages (eq. 2.5). A method is
**telescopic** when the fast and slow base methods are identical, which lets it
nest over more than two rates. It is **decoupled** when implicitness sits only in
the base methods and **coupled** when fast and slow stages are defined implicitly
in terms of each other.

## Compound-fast MrGARK

The compound-fast family first takes a **compound** macro step with the full
right-hand side and the base method $(A,b,c)$, then re-integrates the fast
partition over the $m$ micro steps and discards the fast part of the compound
step (Roberts et al. 2021, eq. 2.6; idea after Rice, Savcenco et al. and Verhoeven
et al.):

$$\begin{aligned}
Y_i&=y_n+H\sum_j a_{ij}f(Y_j),\\
Y^{\{\mathrm f,\ell\}}_i&=\tilde y_{n+\ell/m}+h\sum_j a_{ij}f^{\{\mathrm f\}}\big(Y^{\{\mathrm f,\ell\}}_j\big)+H\sum_j a^{\{\mathrm f,\mathrm s,\ell\}}_{ij}f^{\{\mathrm s\}}(Y_j),\\
y_{n+1}&=\tilde y_{n+1}+H\sum_i b_if^{\{\mathrm s\}}(Y_i),
\end{aligned}$$

with $\tilde y$ advanced by the weights $b$. The method is telescopic, coupled
only in the compound step and decoupled in the micro steps; the coefficients
$A^{\{\mathrm f,\mathrm s,\ell\}}$ act as interpolation weights for the slow
tendencies. An embedded estimate on the compound step can choose the fast
components adaptively.

**Theorem (fourth-order conditions; Roberts et al. 2021, Thm. 2.1).** An
internally consistent compound-fast MrGARK method has order four if and only if
$(A,b,c)$ has order four and, for the sums over $\ell=0,\dots,m-1$,

$$\begin{aligned}
&mA^{\{\mathrm f,\mathrm s,\ell\}}\mathbf 1=\ell\,\mathbf 1+c, &&\text{(internal consistency)}\\
&\textstyle\sum_\ell b^\top A^{\{\mathrm f,\mathrm s,\ell\}}c=\frac m6, &&\text{(order 3)}\\
&\textstyle\sum_\ell\ell\,b^\top A^{\{\mathrm f,\mathrm s,\ell\}}c+\sum_\ell b^\top\operatorname{diag}(c)A^{\{\mathrm f,\mathrm s,\ell\}}c=\frac{m^2}8,\\
&\textstyle\sum_\ell b^\top A^{\{\mathrm f,\mathrm s,\ell\}}c^2=\frac m{12},\\
&\textstyle\sum_\ell b^\top AA^{\{\mathrm f,\mathrm s,\ell\}}c+\sum_\ell(m-1-\ell)\,b^\top A^{\{\mathrm f,\mathrm s,\ell\}}c=\frac{m^2}{24},\\
&\textstyle\sum_\ell b^\top A^{\{\mathrm f,\mathrm s,\ell\}}Ac=\frac m{24}.
\end{aligned}$$

The proof specializes the GARK conditions 3a–4j; several of them reduce to
base-method conditions. Order is preserved when the interpolant behind
$A^{\{\mathrm f,\mathrm s,\ell\}}$ is accurate enough, a sufficient condition only.

**Scalar stability with $s\times s$ matrices (Roberts et al. 2021, §3.4).** With
$R_{\rm int}(z)=(I-zA)^{-1}\mathbf 1$ (page-local, the internal stability
vector), $z=z^{\{\mathrm f\}}+z^{\{\mathrm s\}}$ and $R$ the stability function of
$(A,b)$, the scalar multirate stability function is

$$R_{\mathrm{mr}}=R\Big(\tfrac{z^{\{\mathrm f\}}}m\Big)^{m}+z^{\{\mathrm s\}}b^\top R_{\rm int}(z)+\frac{z^{\{\mathrm s\}}z^{\{\mathrm f\}}}{m}\,b^\top\Big(I-\tfrac{z^{\{\mathrm f\}}}mA\Big)^{-1}\sum_{\ell=0}^{m-1}R\Big(\tfrac{z^{\{\mathrm f\}}}m\Big)^{m-1-\ell}A^{\{\mathrm f,\mathrm s,\ell\}}R_{\rm int}(z).$$

If $A$ is invertible, $R_{\mathrm{mr}}\to R(-\infty)^m$ as
$z^{\{\mathrm f\}}\to-\infty$. The **stiff-slow damping condition**
$A^{\{\mathrm f,\mathrm s,\ell\}}A^{-1}\mathbf 1=\mathbf 1$ for every $\ell$ (eq. 3.18)
gives $R_{\mathrm{mr}}\to R(-\infty)$ as $z^{\{\mathrm s\}}\to-\infty$. With an
[L-stable](/properties/a-stability.md) base and (3.18) both limits vanish, the
scalar L-type behaviour defined on
[linear stability of multirate methods](/definitions/multirate-linear-stability.md).

## Methods constructed

All methods below are from Roberts et al. (2021, §5 and Apps. A–B), are
telescopic and are SDIRK-based.

| Method | Coupling | Order | Stability (scalar) |
|---|---|---|---|
| Coupled multirate backward Euler (5.2) | one coupled stage, internally inconsistent | 1 | L- and algebraically stable for all $m$ |
| Decoupled multirate backward Euler (5.3) | decoupled, internally inconsistent | 1; no second-order coupling error for even $m$ | L- and algebraically stable for all $m$ |
| Coupled multirate midpoint ($m$ odd) | coupled | 2 | algebraically stable, symmetric, symplectic |
| Decoupled multirate midpoint ($m$ even) | decoupled | 2 | algebraically stable, symmetric, symplectic |
| Lightly coupled SDIRK2 MrGARK (5.5) | internally consistent, stiffly accurate in both partitions | 2 | L(69.2°) at $m=2$, not L(0°) by $m=6$ |
| Kværnø–Rentrop-type SDIRK2 MrGARK (5.6) | first micro step computed with the macro step | 2 | same stability function as (5.5) |
| Compound-fast SDIRK2 (5.7) | compound-fast, (3.18) | 2 | L(α), α ≈ 83.0°–84.6° |
| Compound-fast SDIRK3 (A.2) | compound-fast | 3 | L(α), α ≈ 86.8°–88.6° |
| Compound-fast SDIRK4 (B.2) | compound-fast, new base | 4 | L(α), α ≈ 81.2°–81.7° |

Details:

- **Multirate backward Euler.** In the coupled version (5.2)
  $A^{\{\mathrm f,\mathrm s,\ell\}}=0$ for $\ell<m/2-1$ and $1$ otherwise,
  $A^{\{\mathrm s,\mathrm f,\ell\}}=1$ for $\ell\le(m-1)/2$ and $0$ otherwise. The
  decoupled version (5.3) uses $\ell\le m/2-1$ in both rules; it is subcycled
  Strang splitting with every sub-flow replaced by one backward Euler step
  (see [operator splitting](/methods/operator-splitting.md)). The authors state
  the stability claims without printed proofs.
- **Multirate midpoint.** Both versions keep the algebraic stability, symmetry and
  [symplecticity](/properties/symplecticity.md) of the implicit midpoint rule;
  only odd powers appear in their error expansion, which makes them bases for
  multirate extrapolation.
- **SDIRK2 base** (5.4), after Alexander: $c=(\gamma,1)$,
  $A=\begin{bmatrix}\gamma&0\\1-\gamma&\gamma\end{bmatrix}$, $b=(1-\gamma,\gamma)$,
  embedded $\hat b=(\tfrac35,\tfrac25)$, $\gamma=1-1/\sqrt2$; L-stable, order 2.
  Any internally consistent standard MrGARK method on this base needs at least
  one coupled stage, and stiff accuracy in both partitions determines the lightly
  coupled method (5.5) uniquely. The authors "cannot recommend" (5.5) and (5.6) as
  general-purpose methods.
- **Compound-fast SDIRK2** (5.7) follows from (3.18) and internal consistency;
  its $2\times2$ coupling is a rational function of $\gamma$, $\ell$ and $m$.
- **Compound-fast SDIRK3** uses Alexander's 3-stage stiffly accurate SDIRK with
  $\gamma\approx0.44$, the middle root of $6\gamma^3-18\gamma^2+9\gamma-1=0$.
- **Compound-fast SDIRK4** uses a new 5-stage L-stable stiffly accurate SDIRK with
  $\gamma=\tfrac14$, $c=(\tfrac14,1,\tfrac25,\tfrac7{11},1)$, derived together with
  its coupling so that the coefficients stay bounded in $\ell$ and $m$ (B.1).
- **Design rules for orders 3–4** (§5.3): compound-fast form, stiff accuracy, an
  L-stable base, condition (3.18), internal consistency, and coupling
  coefficients bounded in $\ell$ and $m$ to avoid cancellation at large $m$. A
  Kværnø–Rentrop coupling on Nørsett's algebraically stable 2-stage order-3 base
  gave coefficients unbounded in $m$, and no A(0°)-stable solution was found.

The L($\alpha$) angles of the compound-fast methods (Table 5.1):

| Method | $m=2$ | $m=3$ | $m=4$ | $m=8$ | $m=16$ | $m=32$ |
|---|---|---|---|---|---|---|
| SDIRK2 (5.7) | 84.6° | 83.5° | 83.2° | 83.0° | 83.0° | 83.0° |
| SDIRK3 (A.2) | 88.6° | 87.8° | 87.3° | 86.9° | 86.8° | 86.8° |
| SDIRK4 (B.2) | 81.7° | 81.2° | 81.2° | 81.2° | 81.2° | 81.2° |

The angles drop by less than 2° as $m$ grows and then stabilize, "just a few
degrees short of scalar L-stability".

## Cost of the stage solves

Assuming direct solves dominate (Roberts et al. 2021, §4.1–4.2), decoupled
DIRK-based methods cost $\mathcal O(\mathbf sd^3)$ per macro step ($\mathbf s$ the
total number of GARK stages), reduced to
$\mathcal O(md^3)$ by reusing the slow factorization per macro step and the fast
one per micro step; compound-fast methods cost $\mathcal O(md^3)$, or
$\mathcal O(d^3+m(d^{\{\mathrm f\}})^3)$ for component-partitioned systems with
$d^{\{\mathrm f\}}$ fast components. The micro steps need only the fast Jacobian,
the compound step's dense output supplies stage predictors, and its
fast-variable tolerances can be loosened. Stage reducibility turns coupled stages
into one system with matrix $I-h\gamma J^{\{\mathrm f\}}-H\gamma J^{\{\mathrm s\}}$,
which Roberts et al. argue (without measurement) is better conditioned than
$I-H\gamma J$ when $m$ matches the stiffness ratio
([implicit stage solvers](/methods/implicit-stage-solvers.md)).

## Numerical evidence

- **CUSP reaction–diffusion** (diffusion slow, reaction fast, $m=2,4,6$): the
  observed orders match the nominal ones for decoupled midpoint and compound-fast
  SDIRK2/3; SDIRK4 converges "slightly higher than the nominal order", and for a
  fixed number of macro steps the error decreases as $m$ grows (§6.1, Fig. 6.1).
- **500-inverter MOSFET chain** ($\Gamma=100$, $t\in[0,120]$, serial C code): at
  orders 2 and 3 compound-fast MrGARK ($m=14$ and $m=10$) reaches a given accuracy
  "four to six times faster" than single-rate SDIRK and is slightly more efficient
  than the IMEX baselines ARS(2,3,2), ARS(3,4,3) and ARK4(3)6L[2]SA; at order 4
  ($m=6$) multirate and IMEX are similar and about 3× faster than single-rate
  SDIRK4 (§6.2, Fig. 6.2). The largest stable step of compound-fast equals that of
  implicit single rate ($7.1\times10^{-2}$, $5.2\times10^{-2}$, $6.0\times10^{-2}$
  at orders 2–4), while IMEX has an explicit-like limit ($3.2$–$5.2\times10^{-3}$)
  (Table 6.1).

## Explicit multirate partitioned RK with buffer zones (MRK2)

A simpler, explicit multirate family is the second-order multirate
partitioned Runge–Kutta method MRK2 of Constantinescu and Sandu, used by
[Kang & Constantinescu (2022)](/sources/kang-2022.md) (§2.3, Table 1, Eq. (16))
for geometric stiffness on locally refined meshes. The domain is split into a
fast zone (fine elements), a fast buffer, a slow buffer and a slow zone, each
integrated with its own explicit tableau on four shared global stages:

* fast zone and fast buffer: two half-steps of Heun's method,
  $c=(0,\tfrac12,\tfrac12,1)$, $b=(\tfrac14,\tfrac14,\tfrac14,\tfrac14)$;
* slow buffer: $c=(0,1,0,1)$, $a_{21}=1$, $a_{43}=1$, $b=(\tfrac14,\tfrac14,\tfrac14,\tfrac14)$;
* slow zone: one Heun step, $a_{21}=1$, $a_{41}=1$, $b=(\tfrac12,0,0,\tfrac12)$.

The base method is the two-stage SSP method of Shu and Osher (see
[SSP RK](/methods/strong-stability-preserving-runge-kutta.md)). Written this
way (one global step $H$, stages shared by all zones) it is a component-partitioned Runge–Kutta method, and hence a
[GARK method](/methods/generalized-additive-runge-kutta.md) with one partition
per zone *(compiler observation, not in the source)*. Kang & Constantinescu
generalize it to any number of 2:1 refinement levels: elements are grouped
into level blocks of fast zone, fast buffer and slow buffer; a block of level
$k\ge1$ (page-local) takes $2^{k-1}$ substeps of length $2^{1-k}H$, with $H$
the global step; an activation table over $2^{k_{\max}+1}$ global stages, with
$k_{\max}$ the finest level (page-local), says which blocks are active at each stage; and a balancing
algorithm keeps neighbouring level jumps at most one (Eqs. (20)–(21),
Algorithms 1–2, Fig. 2).

**Relaxation.** One global relaxation parameter, shared by all zones and
levels, makes the method entropy conservative or stable at the synchronization
time (Props. 2.2–2.3, Eq. (22)); inside stages and substeps entropy is not
controlled, which is why entropy-stable fluxes are recommended for deep
nesting (§3.3, §4). On [Burgers](/benchmarks/burgers-equation.md) with five
refinement levels, plain MRK2 drifts in energy to $O(10^{-1})$ while the
relaxed method holds $O(10^{-13})$ (Fig. 11), and the relaxed method with an
entropy-stable flux runs stably on ten levels (Fig. 16). See
[relaxation Runge–Kutta](/methods/relaxation-runge-kutta.md). Multirate methods
need no linear or nonlinear solves, which the authors find attractive for
parallel computing when no good preconditioner is available (§4).

Printed slips (arXiv v4 read; source's reader checks): Eq. (17) omits the zone
superscript on $b_i$; Algorithm 2 sets its loop flag unconditionally in one
branch and indexes past the end of an array; the level-0 bookkeeping of the
worked example (step $2H$ under the same step label) is unclear.

## Subcycling outside the GARK framework

Two sources subcycle an explicit scheme at a fixed ratio without a coupled tableau, which
places them next to MrGARK rather than inside it; both are on
[local time stepping](/methods/local-time-stepping.md).

- **Overlapping subdomains.** LESAULTS of [Sreejith et al. (2022)](/sources/sreejith-2022.md)
  (§2–4) takes $m$ steps of an unchanged Lax–Wendroff or Taylor–Galerkin scheme in a refined
  subdomain, freezes interface values at $t_n$, and merges overlapping solutions once per macro
  step. Unlike MrGARK there are no coupling coefficients and no interpolation of slow
  tendencies, and the method is not strictly conservative (§5.5). Its introduction lists
  Sandu's MRI-GARK as a fourth-order extension of multirate local time stepping (§1).
- **Partitioned multiphysics.** [Pulicani et al. (2026)](/sources/pulicani-2026.md) subcycle an
  explicit finite-volume fluid $m$ times per implicit Newmark structure step and enforce
  interface velocity continuity by a Lagrange multiplier at each fine step (Gravouil–Combescure
  method). It is an explicit–implicit multirate scheme in the domain-decomposition sense,
  different subdomains with different integrators, not an additive split of one right-hand side
  (§1, §4.4). It stays stable to $m=300$ on a piston–rod problem, where a conventional staggered
  scheme fails beyond $m=5$ (§5.3).

## Qualifications

- The orders of all methods are classical orders on smooth problems; the
  stability results are scalar (and, for the barriers, 2D) linear analyses
  ([barriers](/results/multirate-a-stability-barriers.md)). "Algebraically stable"
  for the decoupled methods does not imply stability on the 2D test problem.
- Roberts et al. write the decoupled-backward-Euler/Strang identity with remainder
  $\mathcal O(H^2)$, looser than the usual third-order local error of Strang
  splitting; the printed remainder is not explained.
- In the arXiv version read, the second row of the slow coupling of (5.5),
  $(1-\gamma,\gamma)$, carries no condition on $\ell$ although the first row does;
  the intended range of $\ell$ is ambiguous as printed.
- Coefficients of the order-3 and order-4 couplings are rational functions or
  polynomials in $\ell$ and $m$ printed on pp. 31–32 of the version read and in the
  authors' supplementary Mathematica notebook.
- The authors conclude that, beyond one-stage bases, they found no standard
  MrGARK method with satisfactory stability, so multirate extrapolation "may be
  the most practical way to achieve high-order" (§7). The order-4 compound-fast
  methods are, to their knowledge, the highest-order methods of this type.

# Citations

- [Roberts et al. (2021)](/sources/roberts-2021.md) — §2 (eqs. 2.4–2.7, Thm. 2.1), §3.4 (eqs. 3.16–3.18), §4, §5 (eqs. 5.2–5.11, Table 5.1), §6 (Figs. 6.1–6.2, Table 6.1), §7, Apps. A–B.
- [Kang & Constantinescu (2022)](/sources/kang-2022.md) — §2.3 (Table 1, Eqs. (16)–(22), Props. 2.2–2.3, Algorithms 1–2, Fig. 2), §3.3 (Figs. 11, 16), §4.
- [Sreejith et al. (2022)](/sources/sreejith-2022.md) — §1, §2–4, §5.5.
- [Pulicani et al. (2026)](/sources/pulicani-2026.md) — §1, §4.4, §5.3.
