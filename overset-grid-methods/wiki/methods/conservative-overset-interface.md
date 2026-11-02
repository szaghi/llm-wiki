---
type: Method
title: "Conservative overset interface"
description: "Why interpolation-coupled overset grids are not globally conservative, the conditions for conservation over an overlap, Wang's interface that cuts the minor grid's boundary into the major grid as a patched interface carrying Riemann fluxes (mass imbalance 6e-6 % against 0.38 %), Picard et al.'s intersection-weighted transfer with conservation defects up to 0.635 %, and when conservation matters."
status: established
aliases: [conservative Chimera, COC, fully conservative interface algorithm, zonal interface generation, ZIG, conservative overset coupling, interpolation-free overset coupling]
tags: [conservation, overset-grid, chimera, finite-volume, shock-capturing, hole-cutting]
timestamp: 2026-11-02T14:53:00Z
---

# Conservative overset interface

An overset grid coupled by [inter-grid interpolation](/methods/inter-grid-interpolation.md)
is conservative on each component grid but not over the composite. Each
component discretizes $\partial_t\mathbf q+\nabla\cdot\mathbf F(\mathbf q)=\mathbf 0$
in conservation form. At receptors, however, values are interpolated rather
than updated by fluxes, and the two grids hold two different solutions in the
overlap $\Omega_{kk'}$. [Wang (1995)](/sources/wang-1995.md) calls such a
scheme "zonally conservative" but "nonconservative globally" (§1). A
*conservative overset interface* restores global conservation. Wang's version
converts the overlap into a patched interface: the boundary of the minor grid
becomes a cut through the major grid, and the two grids exchange fluxes
through it instead of interpolated values.

## The problem as the founding sources state it

- [Benek et al. (1983)](/sources/benek-1983.md) (p. 374) flag "the loss of
  conservation form" of their Taylor interpolation as a possible deficiency
  "if differences are taken across shocks". On the SKF 1.1 airfoil at
  $M_\infty=0.76$, $\alpha=2.5^\circ$, the shock crossing the overlap boundary
  shows mismatch and "hash", which "indicates that the nonconservative
  interpolations are likely to be at fault", "still under study"
  (pp. 376–377, Figs. 13–14). The authors list conservative interpolation
  among the remedies to examine.
- [Benek et al. (1985)](/sources/benek-1985.md) (p. 324) recall that Rai
  developed a conservative interface for *patched* grids, and that Berger
  generalized it to overlapping 2-D grids at the price of irregular difference
  stencils. They expect these to be "even more irregular" in 3-D and keep
  non-conservative trilinear interpolation, conceding possible trouble at
  shock–grid-boundary interactions.
- [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) (§6.4, pp. 49–52,
  §7) state that neither their discretization nor their interpolation is
  conservative. Their position: "if the computed solution is smoothly
  represented on the grid then the question of conservation is not crucial".
  They concede that conservation matters when a shock is not resolved, cite
  Berger for conservation at interpolation faces, and leave a systematic study
  to future work. In their Mach 2, $Re=50$ impulsively started cylinder, the
  viscous bow shock "has some difficulty crossing the interpolation boundary"
  on the coarsest grid. It is well represented on the two finer grids
  (Fig. 19a).

## Conservation conditions for two overlapping zones

[Wang (1995)](/sources/wang-1995.md) (§2) considers a cell-centred finite-volume
discretization on two overlapping zones: the major grid $G_{k'}$ (Wang's $A$)
and the minor grid $G_k$ ($B$), with overlap $\Omega_{kk'}$ ($O$). The part of
the minor grid's boundary that lies inside the major grid is
$\Gamma_{k\mid k'}$ (Wang's $\Gamma_{BO}$), and $\Gamma_{k'\mid k}$ likewise.
Each zone is conservative by itself (Eqs. (6)–(7)):
$$\sum_{c\in G_k}\lvert V_c\rvert\,\partial_t\mathbf q_c=-\sum_{f\subset\partial\Omega_k}\mathbf F_fS_f .$$
Global conservation over $\Omega_k\cup\Omega_{k'}$ (Eq. (9)) then holds if and
only if two conditions are met:

1. **Uniqueness in the overlap** (Eq. (8)). Both grids give the same rate of
   change of the conserved quantities in $\Omega_{kk'}$:
   $\sum_{c\in G_k,\,c\subset\Omega_{kk'}}\lvert V_c\rvert\,\partial_t\mathbf q^k_c=\sum_{c\in G_{k'},\,c\subset\Omega_{kk'}}\lvert V_c\rvert\,\partial_t\mathbf q^{k'}_c$.
2. **Flux balance of the overlap** (Eq. (10)). This rate equals the net flux
   through the overlap's own boundary $\Gamma_{k\mid k'}\cup\Gamma_{k'\mid k}$:
   $\sum_{c\subset\Omega_{kk'}}\lvert V_c\rvert\,\partial_t\mathbf q_c=-\sum_{f\subset\Gamma_{k\mid k'}\cup\Gamma_{k'\mid k}}\mathbf F_fS_f$,
   with $\mathbf n_f$ outward from $\Omega_{kk'}$.

Wang writes the sign through the orientation, as a sum over
"$-\Gamma_{AO}-\Gamma_{BO}$". For two *patched* zones, the necessary and
sufficient condition reduces to equal and opposite fluxes through the common
boundary (Eq. (11)).

Enforcing (8) and (10) together on a general overlap requires two new internal
boundaries, $\Gamma_{k'\mid k}$ inside $G_k$ and $\Gamma_{k\mid k'}$ inside
$G_{k'}$. Wang judges this "extremely difficult, if not impossible" (§3). As
recalled by Wang:
- Moon & Liou enforced only condition (8), in 2-D, which "was not sufficient
  to guarantee conservation". The 3-D extension "is almost impossible to
  implement".
- Berger gave another conservation condition, whose "implementation is
  unknown".

## Wang's algorithm: overlapped to patched

Wang's way out (§3, Fig. 2) is to use the single boundary $\Gamma_{k\mid k'}$
as a patch boundary between the minor grid $G_k$ and the major grid with the
overlap removed. Conservation then reduces to Eq. (11) along
$\Gamma_{k\mid k'}$, the solution in the overlap is unique, and no
interpolation between zones is needed. There are three steps.

**1. Zonal interface generation (ZIG)** (§3.1, Fig. 3). In 2-D,
$\Gamma_{k\mid k'}$ is the polyline of the minor grid's boundary faces. ZIG
intersects it with the faces of the major grid:
- faces of $G_{k'}$ that it cuts are *cut faces*;
- the boundary segments of $G_k$, split at the cut faces, become *smallest
  faces*.

Major-grid cells are then classified as:
- *cut cells*, crossed by $\Gamma_{k\mid k'}$;
- *normal cells*, outside the minor grid, updated as usual;
- *hole cells*, inside the minor grid, excluded from the computation.

ZIG also computes the area vectors of all smallest and cut faces and the
volumes of the cut cells. This is an explicit
[hole cutting](/methods/hole-cutting.md) whose hole boundary is exactly the
minor grid's boundary, with exact geometric clipping of the major-grid cells.

**2. Fluxes on the smallest faces** (§3.2). For each smallest face, left and
right states are reconstructed from the adjacent major-grid cut cell and
minor-grid cell, and the flux is Roe's approximate Riemann flux,
$\mathbf F_f=\mathbf F(\mathbf q^L_f,\mathbf q^R_f,\mathbf n_f)$ (Eq. (13)),
matching the interior scheme. Two reconstructions are offered:
- *cell-wise constant* states, which give a first-order interface;
- *cell-wise linear* states from a least-squares gradient over neighbouring
  cells (Eq. (12), primitive variables, evaluated at the face centre), which
  give a second-order interface.

**3. Update** (§3.3, Eq. (14), Fig. 4). A minor-grid boundary face receives
the sum of the fluxes of its smallest faces. A major-grid cut cell $(i,j)$
combines its four regular face fluxes, each weighted by the retained fraction
$W_f\in[0,1]$, with the smallest-face fluxes inside it:
$$\sum_{f\subset\partial V_c}\mathbf F_fS_f=\big(\mathbf F S W\big)_{i+\frac12,j}-\big(\mathbf F S W\big)_{i-\frac12,j}+\big(\mathbf F S W\big)_{i,j+\frac12}-\big(\mathbf F S W\big)_{i,j-\frac12}+\sum_{\text{smallest faces}}\mathbf F_fS_f .$$
The regular face fluxes are computed through the full face, in the direction
of increasing index. In Fig. 4 the line 1–2 cuts the cell, and the weights
are $\lvert 1d\rvert/\lvert ad\rvert$, $\lvert 2c\rvert/\lvert bc\rvert$, 1 and
0. With these area weights, every cut cell "can be cast in the same form no
matter what shapes" it takes. The conserved variables of the cut cell are
updated with its clipped volume from ZIG.

Wang states that conserving the fluxes on each smallest face "in the local
sense" guarantees global conservation (§3.1). The
interface matches the interior accuracy when its reconstruction order equals
the interior one (§6). Freestream preservation, which requires correct
smallest-face and cut-face area vectors, was the debugging criterion and held
in every case (§5).

## Evidence

Wang (§5) implements the interface in the cell-centred finite-volume code
CFD-FASTRAN: MUSCL with minmod in primitive variables, Roe flux-difference
splitting, implicit backward Euler with point-Jacobi inner iterations. The
comparator is the "original Chimera" implemented in NASA Langley's CFL3D,
which has the same spatial discretization but a diagonalized implicit
operator. Wang argues that this difference "should disappear at steady
state". All tests are 2-D Euler.

- **Transonic channel with a 10% bump**, $M_{\mathrm{in}}=0.675$ (§5.1,
  Table I). Mass imbalance between inflow and outflow:

  | grid | code | imbalance |
  |---|---|---|
  | single zone | CFD-FASTRAN | $4\times10^{-6}$ % |
  | two zones | conservative interface | $6\times10^{-6}$ % |
  | two zones | original Chimera | 0.38 % |

  Wang calls the Chimera imbalance "about five orders larger". The $C_p$ of
  both methods agrees fairly well with a fine single-zone reference. The
  second-order interface gives smoother transitions than the first-order one
  (Fig. 9). The conservative scheme converges to machine zero, while the
  Chimera stalls after several orders of residual reduction. Wang hedges the
  attribution: the nonconservative interface "may have contributed" (§5.1,
  Fig. 10).
- **Slow moving shock** (§5.2, Figs. 11–13). Pre-shock state $\rho=1.4$,
  $p=1$, $u=3$; post-shock $\rho=5.38064$, $p=10.2286$, $u=0.791673$; shock
  speed 0.015. The domain is a wavy-walled channel with a rectangular minor
  grid. The original Chimera develops instabilities that dissipate the shock
  until it disappears. The conservative interface passes it through without
  difficulty. As recalled by Wang, Part-Enander & Sjögreen had shown the same
  contrast.
- **Three-element airfoil** (§5.3), $M_\infty=0.2$, $\alpha=0.2^\circ$,
  computed inviscid. Slat $85\times7$, main $209\times79$, flap $136\times9$.
  $C_p$ agrees "generally fairly good" with the Valarezo et al. experiment.
  The main-grid residual stalls after about 1500 iterations; Wang attributes
  this to leading-edge separation in the inviscid model. See
  [multi-element airfoils](/benchmarks/multi-element-airfoil.md).
- **Shock diffraction by a cylinder**, $M=1.5$ (§5.4, Figs. 19–20). Shocks and
  slip lines cross the interface freely. Agreement with an experimental
  shadowgraph is qualitative.
- **Cost** (§6). In 2-D, ZIG costs about one flow-solver step and runs once
  for fixed grids. Wang expects it to be much more expensive in 3-D. The
  per-iteration smallest-face fluxes add less than 5% of CPU time. No
  hardware is stated.

## Intersection-weighted transfer without flux matching

[Picard et al. (2021)](/sources/picard-2021.md) (§3.2.4, Eqs. (14)–(15))
take a third route in a cell-centred finite-volume Chimera method: they keep
the overlap, cut no hole, and fill the receptor ("ghost") cells of each grid
with conservative variables averaged over the geometric intersections with
the donor grid's cells. Their starting point is a *local conservation
hypothesis*: the integral of the conserved variables over a receptor cell
$V_c$ of $G_k$ equals the integral of the donor solution over the part of
$V_c$ covered by $G_{k'}$. With the limited piecewise-linear reconstruction
of each donor cell $V_{c'}$ evaluated at the barycentre $\mathbf x_{cc'}$ of
$V_c\cap V_{c'}$ (page-local), the transfer reads
$$\mathbf q_c=\sum_{c'\in G_{k'}}\frac{\lvert V_c\cap V_{c'}\rvert}{\lvert V_c\rvert}\Big(\mathbf q_{c'}+\Phi_{c'}\,\nabla\mathbf q_{c'}\cdot(\mathbf x_{cc'}-\mathbf x_{c'})\Big),$$
with $\Phi_{c'}\in[0,1]$ the slope limiter (page-local) and least-squares
gradients of the conserved variables. The weights are intersection-volume
fractions, so the formula needs no structured index space; the authors call
it second-order accurate "without any constraint on meshes" (§3.2.4), and
their 1-D advection test keeps the order of the single grid (see
[inter-grid interpolation](/methods/inter-grid-interpolation.md)). The method
is admittedly *not* globally conservative, because it transfers states, not
fluxes: "the only conservative Chimera approach is based on flux
interpolation" (§3.2.4, citing [Wang (1995)](/sources/wang-1995.md), Wang's
1998 moving-grid extension and Pärt-Enander & Sjögreen (1994), the last two
not ingested here). The limiter
extension that keeps the reconstruction bounded at intersection barycentres
is on [shock capturing on overlapping grids](/methods/shock-capturing-on-overset-grids.md).

**Measured conservation defect.** Picard et al. (§4.2, Tables 3–4) place a
stationary Mach-1.5 shock on the patch boundary, the patch holding only the
post-shock state, and report the relative change of total mass, momentum and
energy, $\varepsilon_{\mathrm c}$, after $tu_L/L=100$ (pre-shock velocity $u_L$,
domain length $L$). With coincident grid interfaces (ghost layers abutting
exactly) and equal cell sizes the defect equals that of the single grid to all
printed digits. With non-coincident interfaces it is a few tenths of a
percent:

| interfaces | patch/substrate cell ratio | mass | momentum | energy |
|---|---|---|---|---|
| single grid / coincident | 1 | $5.97\times10^{-4}$ % | $2.45\times10^{-3}$ % | $4.46\times10^{-3}$ % |
| non-coincident | 1 | 0.434 % | 0.635 % | 0.465 % |
| non-coincident | 2–16 | 0.115–0.599 % | | |

The authors summarize the non-coincident defect as "about 0.6 %" and below
1 % for every cell ratio, and the loss on the post-shock density jump as at
most 0.35 % of the exact post-shock state, "acceptable for industrial
applications" (§4.2, Fig. 11b). For comparison, Wang's original-Chimera mass
imbalance on the bump channel was 0.38 % (above); the two tests differ in
geometry, scheme and measure, so the numbers are not a like-for-like
comparison.

## Positions on when conservation matters

The founding sources agree on the observations and differ in emphasis:
- Benek et al. (1983) attribute the shock mismatch they see to
  nonconservative interpolation, provisionally.
- Chesshire & Henshaw (1990) hold that conservation is not crucial for
  resolved solutions.
- Wang (1995) states the opposite case for discontinuities. Conservation
  errors, "although formally of truncation-error order", can exceed a
  first-order error in smooth regions and "can potentially result in shock
  waves with incorrect jump conditions or wrong locations even if the
  numerical scheme itself is of high-order in accuracy" (§5).
- Wang also grants that the nonconservative Chimera "can capture a strong
  steady shock wave probably because it is zonally conservative" (§6).

Later sources state the same conditional position:
- Chan (2009) recalls that the early concern that non-conservative fringe
  interpolation degrades accuracy "was resolved by Meakin, who showed that
  formal solution accuracy is maintained using the commonly adopted
  tri-linear interpolation scheme at the fringe points provided the flow
  solution is smoothly resolved by all participant grids in the overlapped
  zones" ([Chan (2009)](/sources/chan-2009.md), §7).
- Sharma et al. (2021) state that interpolating the solution does not
  guarantee global conservation, but that the lack of conservation does not
  degrade the solution if the overlap is away from shocks and
  discontinuities; incompressible schemes preclude shocks, although mass
  conservation may matter for the pressure-correction step. They declare
  conservative interpolation out of scope
  ([Sharma et al. (2021)](/sources/sharma-2021.md), §1).
- Picard et al. (2021) accept a measured conservation defect of tenths of a
  percent for a shock on the patch boundary (above), and Henshaw &
  Schwendeman (2006) and Banks et al. (2016) compute shocked flows on
  overlapping grids without discussing conservation at the overlap
  ([Henshaw & Schwendeman (2006)](/sources/henshaw-2006.md),
  [Banks et al. (2016)](/sources/banks-2016.md); see
  [shock capturing on overlapping grids](/methods/shock-capturing-on-overset-grids.md)).

No contradiction is recorded: each source limits its own claim.
Chesshire & Henshaw restrict theirs to smoothly represented solutions and
concede the unresolved shock; Benek et al.'s attribution and Wang's
explanation of the steady-shock capture are both hedged ("likely",
"probably").

## Other effects of nonconservative coupling

[Henshaw (1994)](/sources/henshaw-1994.md) (§4.4) notes that in the
fourth-order incompressible scheme the (nonconservative) interpolation conditions act as a
source of discrete divergence. Divergence damping is used to control it (see
[incompressible flow on overlapping grids](/methods/incompressible-flow-on-overset-grids.md)).

## Qualifications

- **Two meanings of "conservative overset".** Wang's interface removes the
  overlap on the major-grid side (hole cells) and keeps a single solution
  there. Other methods keep the overlap and make the interpolation itself
  conservative. Berger's method is one, recalled by Benek et al. (1985),
  Chesshire & Henshaw (1990) and Wang (1995); none of the sources ingested here
  describes its formulas. Both families belong on this page, attributed. Picard et al.'s
  intersection-weighted transfer (above) is a third kind: it keeps the
  overlap and transfers states, and its authors call it not conservative.
- **"Only flux interpolation is conservative."** Picard et al. (§3.2.4)
  state that the only conservative Chimera approach is based on flux
  interpolation, and cite Wang (1995) as one of the three works behind the
  statement. In their usage, then, "flux interpolation" covers Wang's
  patched interface, which computes Riemann fluxes on the minor grid's
  boundary rather than transferring states; the two sources do not conflict.
- **Unaddressed issues.** Wang does not analyse the accuracy of the cut-cell
  geometry, the time-step restriction of small cut cells, or the stability of
  the cut-cell update.
- **Comparison caveat.** The comparison is between two codes with different
  implicit operators. Wang argues that this difference "should disappear at
  steady state" and attributes the stall of the original Chimera to the
  interface only in part ("may have contributed").
- **Printed slips in Wang (1995):**
  - Eq. (9) is printed without the minus sign that Eqs. (4)–(7) carry. Only
    with $-\sum_{\Gamma_G}$ does Eq. (10) follow as printed *(compiler check,
    not in the sources)*.
  - Eq. (16) prints the reconstruction interval as
    $\xi_{i-1/2}\le\xi\le\xi_{i-1/2}$; the upper bound is $\xi_{i+1/2}$.
  - Eq. (25) is introduced as a linearization "up to second order" but
    contains only first-order terms.
  - Eq. (29) prints "$0_{\max}$" for $\theta_{\max}$.
  - Table I prints the conservative scheme's imbalance as $6\times10^{-6}$ %,
    while the printed rates, $\lvert269.47414-269.47412\rvert/269.47414$, give
    $7.4\times10^{-6}$ % *(compiler check, not in the sources)*.
- **Slow-moving-shock states.** The printed states satisfy the
  Rankine–Hugoniot mass and momentum relations in the shock frame to four
  digits, and the energy relation if $\gamma=1.4$, which Wang does not state
  *(compiler check, not in the sources)*.

# Citations

- [Wang (1995)](/sources/wang-1995.md) — §1 (zonal vs global conservation), §2 Eqs. (6)–(11), §3 (Fig. 2, Moon & Liou and Berger as recalled), §3.1–3.3 (ZIG, Eqs. (12)–(14), Figs. 3–4), §4 (flow solver), §5.1–5.4 (Table I, Figs. 9–20), §6 (cost, conclusions).
- [Benek et al. (1983)](/sources/benek-1983.md) — p. 374 (loss of conservation form), pp. 376–377 (SKF 1.1, Figs. 13–14).
- [Benek et al. (1985)](/sources/benek-1985.md) — p. 324 (Rai and Berger as recalled; choice of trilinear interpolation).
- [Chesshire & Henshaw (1990)](/sources/chesshire-1990.md) — §6.4 pp. 49–52, Fig. 19a, §7.
- [Henshaw (1994)](/sources/henshaw-1994.md) — §4.4.
- [Picard et al. (2021)](/sources/picard-2021.md) — §3.2.4 (Eqs. (14)–(15), non-conservation), §4.2 (Tables 3–4, Fig. 11b).
- [Chan (2009)](/sources/chan-2009.md) — §7 (Meakin's result as recalled).
- [Sharma et al. (2021)](/sources/sharma-2021.md) — §1.
- [Henshaw & Schwendeman (2006)](/sources/henshaw-2006.md) — §4.2 (semi-conservative scheme).
- [Banks et al. (2016)](/sources/banks-2016.md) — §4.2.
