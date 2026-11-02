---
type: Result
title: "Interpolation order and overlap requirements"
description: "Chesshire and Henshaw's lemmas on the width of inter-grid interpolation needed to keep a composite-grid discretization at its design order: width at least 2s+1 when the overlap shrinks with h, s+1 when it stays fixed, generalized to sp+1 and sp/2+1, and confirmed in 1-D, 2-D Poisson, fourth-order Navier–Stokes and Maxwell, sixth-order compact and finite-volume elliptic, advective and Navier–Stokes tests."
status: established
aliases: [interpolation width rule, interpolation order lemma, Chesshire–Henshaw interpolation lemma, q >= 2s+1 rule, overlap requirement]
tags: [interpolation, high-order, composite-grid, finite-difference, overset-grid]
timestamp: 2026-11-02T14:53:00Z
---

# Interpolation order and overlap requirements

On a composite overlapping grid the receptor equations
$u^k_{\mathbf i}=\sum_{\mathbf j\in\mathcal S_{\mathbf i}}\alpha_{\mathbf j}u^{k'}_{\mathbf j}$
are part of the discrete boundary-value problem, so their truncation error
enters the solution error. [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md)
(§5.3, Lemmas I and II) determine how wide the
[interpolation](/methods/inter-grid-interpolation.md) formula must be for the
composite solution to keep the order of the interior discretization. The
answer depends on how the overlap $d$, the distance between the innermost
receptors of the two grids (see [fringe points and overlap width](/definitions/fringe-point.md)),
scales with the spacing $h$: when $d\propto h$, a second-order solution of an
equation of order $2s$ needs interpolation of width $q\ge 2s+1$. When $d$ stays
bounded away from zero, $q\ge s+1$ is enough. Interpolation is therefore not a
boundary condition of lower importance: it must be carried out to full
accuracy.

## Setting and translation

Chesshire & Henshaw write $2p$ for the order of the differential equation and
$2r$ for the order of the discretization. In this bundle these are $2s$ and $p$
([notation](/notation.md) §3). Interpolation of width $q$ (a $q$-point Lagrange
formula, degree $q-1$) has error $O(h^q)$ and is called order $q$. This is
Chesshire & Henshaw's own convention, "$p$ points give $p$th order", so linear
interpolation is second order (§5.2–5.3). The CMPGRD parameter `iw` is $q$.

**Model problem** (§5.3, Eq. (5.4)). On $[a,b]$,
$$\frac{\partial^{2s}u}{\partial x^{2s}}=F(x),\qquad \frac{\partial^{j}u}{\partial x^{j}}(a)=L_j,\quad \frac{\partial^{j}u}{\partial x^{j}}(b)=R_j,\qquad j=0,\dots,s-1,$$
is discretized on two overlapping uniform grids $G_1$ (spacing $h_1$, starting
at $a$) and $G_2$ (spacing $h_2$, ending at $b$) by $(D_+D_-)^s$ at interior
points. On each grid, the $s$ innermost points are receptors interpolated from
the other grid with a $q$-point formula. Let $x_1,\dots,x_s$ denote the receptors
of $G_1$ and $x_{s+1},\dots,x_{2s}$ those of $G_2$ (page-local labels). The
overlap is $d=x_s-x_{2s}>0$, the distance between the innermost receptors. The
interpolation system becomes singular when a receptor of $G_1$ coincides with
one of $G_2$.

**Error equations.** Each grid's error $e^k$ satisfies the same discrete
equations, with $O(h_k^2)$ forcing in the interior and boundary equations and
$O(h_{k'}^q)$ forcing in the interpolation equations. The authors split the
error into two problems and *assume* that the one with zero interpolation
truncation error is well posed. Henshaw's thesis proved this only for $s=1$
(as recalled by Chesshire & Henshaw, §5.3). The interpolation-driven part
then behaves like the continuous problem $\partial^{2s}e^k/\partial x^{2s}=0$ with
homogeneous boundary data. Its solutions are (Eq. (5.6))
$$e^1(x)=\sum_{m=1}^{s}c^1_m(x-a)^{s+m-1},\qquad e^2(x)=\sum_{m=1}^{s}c^2_m(b-x)^{s+m-1},$$
with page-local coefficients $c^k_m$. The $2s$ interpolation equations form a
linear system $\mathsf A\mathbf c=O(h^q)$, $h=\max(h_1,h_2)$. Its determinant
is a Vandermonde-type product of the receptor separations $x_i-x_j$, and
Cramer's rule bounds $\mathbf c$ by counting how many of those factors are
$O(h)$ (Eqs. (5.7)–(5.8)).

## Statements

**Lemma I** (p. 33). If $d\ge ch$, then every factor $x_i-x_j$ is $O(h)$. The
denominator of Cramer's rule has $\binom{2s}{2}$ such factors and the numerator
$\binom{2s-1}{2}$, so $c^k_m=O(h^{q-2s+1})$. The error is second order provided
$$q\ \ge\ 2s+1 .$$

**Lemma II** (p. 34). If $d\ge c$ independently of $h$, only same-grid
separations are $O(h)$. The denominator then has $2\binom{s}{2}$ such factors
and the numerator $\binom{s}{2}+\binom{s-1}{2}$. The difference is $s-1$, so
$c^k_m=O(h^{q-s+1})$, and second order requires
$$q\ \ge\ s+1 .$$

**Generalization to order $p$** (summary, p. 29, and Remark 1, p. 34). The
authors argue that solving an equation of order $2s$ to order $p$ is
equivalent, for this counting, to solving an equation of order $sp$ to second
order. They then state:
$$q=sp+1\quad(d\propto h),\qquad q=\tfrac{sp}{2}+1\quad(d=O(1)),$$
with $\tfrac{sp}{2}$ receptor lines on each grid. The total geometric overlap of
the two grids is then $d+\tfrac{sp}{2}(h_1+h_2)$. For second-order elliptic
equations ($s=1$) this gives the rules: a second-order scheme needs
quadratic ($q=3$) interpolation when the overlap shrinks with $h$, and linear
($q=2$) interpolation suffices when the overlap stays larger than a constant.
Chesshire & Henshaw credit this corollary to Henshaw's thesis (p. 29). A
fourth-order scheme ($p=4$) needs $q=5$ with two receptor lines.

**Interpolation is an essential boundary condition** (Remark 3, p. 34). Lower
order is enough for non-essential boundary conditions, such as the outgoing
characteristic conditions treated by Kreiss and by Gustafsson (as recalled by
Chesshire & Henshaw). Interpolation equations are essential conditions and must
be as accurate as the theory demands.

**Degenerate case** (Remark 2). When $h_1=h_2=d$ the receptors coincide with
grid points of the other grid. A one-point formula is then exact, consistent
with the single-grid limit.

## Numerical confirmation

*1-D model problem* (Tables I–II, pp. 35–36): $(D_+D_-)^s v=f$ on $[0,1]$ with
$u=\sin\pi x+\cos\pi x+\sin2\pi x+\cos2\pi x$, grids $(N_1,N_2)=(10,10),(15,15),\dots,(130,130)$,
and observed rate $\sigma$ from a least-squares fit:

| overlap | $q$ | $\sigma$ ($s=1$) | $\sigma$ ($s=2$) |
|---|---|---|---|
| $d=0.5h$ | $2s$ | 1.0 | 0.79 |
| $d=0.5h$ | $2s+1$ | 2.1 | 2.0 |
| $d=0.5$ | $s$ | 0.38 | 1.3 |
| $d=0.5$ | $s+1$ | 1.9 | 2.1 |

*2-D Poisson equation* (§5.5, Tables III–IV, p. 41): $\nabla^2u=f$ with
$u=\cos2\pi x\cos2\pi y$, on an annular boundary grid over a Cartesian grid
(Fig. 16), with four resolutions of 1, 1.5, 2 and 2.5 times the coarse point
count per direction. A second-order scheme gives $\sigma=0.98$ with $q=2$ and
$\sigma=2.1$ with $q=3$. A fourth-order scheme gives $\sigma=3.2$ with $q=4$ and
$\sigma=4.2$ with $q=5$. The authors conclude that "a $3\times3$ interpolation
stencil … is required for second-order accuracy and a $5\times5$ … for
fourth-order accuracy". One order less of interpolation loses one order of
convergence. The authors read these tests against the $d\propto h$ rule,
having noted that the overlap is typically a constant times $h$ and shrinks
under refinement (p. 29).

*Fourth-order incompressible Navier–Stokes.* [Henshaw (1994)](/sources/henshaw-1994.md)
(§4.1, §5.1) chooses the interpolation order by this criterion. A fourth-order
discretization ($p=4$) of the second-order momentum and pressure equations
($s=1$) uses quartic ($q=5$) Lagrange interpolation on a $5\times5\times5$
stencil, with two lines of receptors. That is exactly $q=sp+1$ with $\tfrac{sp}{2}=2$
lines. The measured rates are fourth order on overlapping grids: on the
overlapping circle, $\sigma=4.0$ (velocity), 4.0 (pressure) and 4.3
(divergence) (Table III). On the two-patch spherical shell, $\sigma=4.0$, 4.2
and 4.2 (Table VII). See
[incompressible flow on overlapping grids](/methods/incompressible-flow-on-overset-grids.md).

*Fourth-order Maxwell.* [Henshaw (2006)](/sources/henshaw-2006-b.md) (§4)
states the rule as width $q=p+1$ for a $p$th-order approximation of the
second-order wave equation, "following" Chesshire & Henshaw; this is
$q=sp+1$ with $s=1$. With $q=5$ the twilight-zone rates are 3.93–4.40 on a
2-D cylinder in a channel and 4.11–4.26 on a 3-D sphere in a box, and 3.85–3.88
in PEC-sphere and dielectric-cylinder scattering (Tables 1–4). See
[Maxwell's equations on overlapping grids](/methods/maxwell-equations-on-overset-grids.md).

*Second-order finite volumes, elliptic versus hyperbolic.*
[Sharma et al. (2021)](/sources/sharma-2021.md) (§3.1) restate the rules for
a second-order discretization: with constant fringe gap, linear interpolation
suffices for first- and second-order PDEs; with a gap proportional to $h$,
linear suffices for a first-order PDE but at least quadratic is needed for a
second-order one. They test them with a node-centred finite-volume code on
two overlapping Cartesian meshes, $h=0.2$ to $0.025$ (§4.1):
- diffusion (manufactured solution) with fringe gap $d=3h$: linear ($q=2$)
  Lagrange interpolation degrades second order, quadratic ($q=3$) keeps it,
  and cubic adds nothing (Fig. 10); with a constant gap linear keeps second
  order (Fig. 11) — Lemmas I and II with $s=1$;
- the same with radial-basis-function interpolation: polynomial augmentation
  of degree 2 keeps second order, degree 1 does not (Fig. 13);
- linear advection: linear interpolation keeps second order and higher order
  changes little (Fig. 15);
- advection–diffusion at Péclet numbers about 3, 30 and 300: high Péclet
  behaves like advection, and as it approaches 1 higher-order interpolation
  is needed (Fig. 16);
- a decaying Taylor vortex in the incompressible Navier–Stokes solver with
  linear interpolation keeps second order at cell Reynolds number about 400
  and loses it at about 1 (§4.3.1, Fig. 25). The authors "strongly recommend"
  higher-order interpolation for incompressible flow, since the pressure
  equation is elliptic; the observed orders are shown only in figures.

*High-order compact scheme, hyperbolic.* [Sherer & Scott (2005)](/sources/sherer-2005.md)
(§5.2, Fig. 16a) convect an inviscid vortex across a curvilinear overset
system with a hole, using a sixth-order compact scheme. The orders printed
on the figure are 2.01 with second-order interpolation, 5.33 with sixth-order
interpolation, 6.36 with direct injection between coincident grids and 7.47
on a single grid: the interpolation order caps the global order. They recall
(§1) that Delfs showed linear interpolation eventually corrupts a high-order
solution, and that Chesshire & Henshaw showed it cannot keep high-order
global accuracy.

*Second-order finite-volume Chimera transfer.* [Picard et al. (2021)](/sources/picard-2021.md)
(§4.1, Table 1) advect a sine wave through a non-coincident patch with a
second-order intersection-volume interpolation: the observed orders of the
Chimera run (2.026, 2.108 at the two finest pairs) track the single-grid ones
(2.022, 2.119). Their §1 states that interpolation errors can be compensated
by interpolating at higher order than the scheme.

## Qualifications

- **Scope.** The proof is one-dimensional, elliptic, and second-order in the
  discretization. It rests on the well-posedness assumption, which was proved
  only for $s=1$. The extension to order $p$ rests on the equivalence argument
  of Remark 1, which the authors give as a heuristic. The 2-D and 3-D evidence
  is numerical (above).
- **Hyperbolic and engineering practice.** The Chimera sources use linear
  ($q=2$) interpolation with second-order flow solvers and a fixed number of
  overlap points, so $d\propto h$. These are the Taylor formula of
  [Benek et al. (1983)](/sources/benek-1983.md) (Eq. (1)), the trilinear
  interpolation of [Benek et al. (1985)](/sources/benek-1985.md) (p. 324), and
  the trilinear inversion of [Rogers et al. (2003)](/sources/rogers-2003.md).
  None of these papers measures the resulting order, and Chesshire &
  Henshaw derive Lemma I for an elliptic model problem only. [Lee & Baeder (2003)](/sources/lee-2003.md)
  accept low-order 4- or 2-point stencils next to walls as unavoidable (p. 11).
  Benek et al. (1983) give only the qualitative overlap rule that the
  interpolation stencil must lie in the donor grid and that the overlap must
  be large enough for its boundaries to have little influence (p. 375).
  As recalled by [Chan (2009)](/sources/chan-2009.md) (§7), Meakin showed
  that trilinear fringe interpolation keeps the formal accuracy "provided the
  flow solution is smoothly resolved by all participant grids in the
  overlapped zones". The statement, as recalled, does not say for which
  scheme order it holds; Sherer & Scott's measured 2.01 (above) shows that
  linear interpolation does not keep the accuracy of a sixth-order solver.
- **First-order (hyperbolic) equations.** The lemmas are proved for
  equations of even order $2s$. Sharma et al. (2021) attribute to Chesshire &
  Henshaw the rule that linear interpolation suffices for a first-order PDE
  with $d\propto h$. Setting $2s=1$ formally in $q\ge2s+1$ gives $q\ge2$,
  consistent with that rule and with the advection tests of Sharma et al. and
  Picard et al. *(compiler check, not in the sources)*; it is not a proved
  case of the lemma.
- **Overlap scaling in practice.** Sharma et al. (Fig. 4) note that implicit
  hole cutting by cell counts, as in TIOGA, makes the fringe gap shrink with
  $h$, so the $d\propto h$ rule applies unless the gap is fixed by hand.
- **"Interpolation width equals discretization width."** Chesshire & Henshaw
  summarize the $d\propto h$ rule this way (p. 29). A centred order-$p$
  approximation of the $2s$-th derivative uses $2s+p-1$ points per direction.
  This equals $q=sp+1$ when $s=1$ or $p=2$, but for $s=2$, $p=4$ it gives 7
  against $q=9$ *(compiler check, not in the sources)*.
- **Counting check of the generalization** *(compiler check, not in the
  sources)*. Keeping the factor counts of Lemmas I and II but requiring
  $c^k_m=O(h^p)$ instead of $O(h^2)$ gives $q\ge2s+p-1$ when $d\propto h$ and
  $q\ge s+p-1$ when $d=O(1)$. The first bound is the centred stencil width
  above, which is the paper's verbal summary; it agrees with the printed
  $q=sp+1$ only when $s=1$ or $p=2$. The second agrees with the printed
  $q=sp/2+1$ only when $s=2$ or $p=2$: for $s=1$, $p=4$ it asks for $q=4$
  where the printed rule gives 3. The tested cases ($p=2$; $s=1$, $p=4$ with
  the $d\propto h$ rule) do not separate the two forms, since both give the
  same $q$ there.
- **Printed slips in Chesshire & Henshaw** (do not affect the lemmas):
  - The determinant (5.7) and Cramer quotient (5.8) are printed as products
    $\prod_{i}\prod_{j\ne i}(x_i-x_j)$. These count every pair twice and
    contradict the paper's own degree argument and factor counts. The single
    product over $i<j$ is meant.
  - The cross-distance formula on p. 34 prints
    $d+(s-i)h_1+(j-s-1)h_2$, which does not reduce to $d$ for the innermost
    pair. The form consistent with Fig. 14 is $d+(s-i)h_1+(2s-j)h_2$.
  - The 1-D grid $G_2$ is printed as $x^2_i=b-(i-1)h_2$. Fig. 14 and the
    boundary equations require $x^2_i=b-(N_2-i)h_2$.
  - The caption and header of Table I read $d=0.5$, but the text assigns
    Table I to $d=0.5h$.
  - Table IV's fourth-order, $q=4$ errors are non-monotone
    ($0.00023$ then $0.00048$). This is data, not a slip.

# Citations

- [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) — §5.2 (order convention), §5.3 (model problem, Eqs. (5.4)–(5.8), Lemmas I–II, Remarks 1–3, Tables I–II), §5.5 (Fig. 16, Tables III–IV).
- [Henshaw (1994)](/sources/henshaw-1994.md) — §4.1 (quartic interpolation per Chesshire & Henshaw), §5.1–5.2 (Tables III, VII).
- [Benek et al. (1983)](/sources/benek-1983.md) — p. 374, Eq. (1); p. 375 (qualitative overlap rule).
- [Benek et al. (1985)](/sources/benek-1985.md) — p. 324 (trilinear interpolation).
- [Lee & Baeder (2003)](/sources/lee-2003.md) — p. 11 (low-order stencils near walls).
- [Rogers et al. (2003)](/sources/rogers-2003.md) — "Boundary Point Interpolation" (trilinear inversion).
- [Sherer & Scott (2005)](/sources/sherer-2005.md) — §1 (Delfs, Chesshire & Henshaw as recalled), §5.2, Fig. 16a.
- [Henshaw (2006)](/sources/henshaw-2006-b.md) — §4 ($q=p+1$), §10 (Tables 1–4).
- [Chan (2009)](/sources/chan-2009.md) — §7 (Meakin's result as recalled).
- [Sharma et al. (2021)](/sources/sharma-2021.md) — §3.1, Fig. 4, §4.1 (Figs. 10–16), §4.3.1 (Fig. 25).
- [Picard et al. (2021)](/sources/picard-2021.md) — §1, §4.1, Table 1.
