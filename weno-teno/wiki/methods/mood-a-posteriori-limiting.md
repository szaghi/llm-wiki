---
type: Method
title: "MOOD a posteriori limiting"
description: "MOOD-type limiting computes a candidate high-order update, checks it for admissibility (positivity, NaN, maximum principle), and recomputes only flagged cells with a robust low-order scheme; the page records a kinetic scheme, deferred correction, a posteriori subcell limiters of ADER-DG and unstructured DG, artificial-viscosity recomputation, PAD and NAD used a priori, and the a priori contrast."
status: established
aliases: [MOOD, multi-dimensional optimal order detection, a posteriori limiting, a posteriori stabilization, a posteriori subcell limiting, APLSC, a posteriori local subcell correction]
tags: [limiting, positivity, bound-preserving, finite-difference, dg]
timestamp: 2026-10-23T20:29:00Z
---

# MOOD a posteriori limiting

MOOD (multi-dimensional optimal order detection) reverses the order of
a priori non-oscillatory limiting. Instead of deciding before the
step where the high-order scheme must be limited, it computes a
candidate update $\tilde u^{n+1}$ with the unlimited high-order scheme,
tests the candidate cell by cell against admissibility criteria, and
recomputes the update only in the cells that fail, with a lower-order
scheme that is robust there; the high-order result is kept everywhere
else. Two sources of this bundle that apply it use only physical
admissibility (positivity of density and pressure, finite values) as
criterion, and fall back directly to first order; a third uses the
classical MOOD criteria, physical and numerical admissibility, but before
the step rather than after it; and the ADER-DG sources recompute flagged
cells on a subcell grid with a second-order finite-volume scheme, after
physical, numerical and (in one of them) shock criteria; Vilar & Abgrall
replace, after the same criteria, only the fluxes on the faces of troubled
subcells inside a DG cell.
[Abgrall & Nassajian Mojarrad (2024)](/sources/abgrall-2024.md) present
their version as inspired by two earlier a posteriori methods (their
refs. [14] and [25], §3.2.2).

## Detection and recomputation in a kinetic scheme

Abgrall & Nassajian Mojarrad (2024) (§3.2.2) use MOOD as one of two
stabilizations of their arbitrarily high-order, explicit
[discrete kinetic relaxation scheme](/methods/discrete-kinetic-relaxation-scheme.md),
the other being a flux limiter blending first- and high-order
differences (§3.2.1). From the kinetic state at $t^n$:

1. compute the candidate update with the full-order method (fourth
   order in space and time in their tests);
2. at every grid point recover $(\tilde\rho,\tilde v,\tilde p)$ from the
   projected kinetic state and flag the point if $\tilde\rho\le0$,
   $\tilde p\le0$, or any component is NaN (tested as $x\ne x$);
3. flag a quadrilateral if any of its four vertices is flagged;
4. on flagged quadrilaterals, recompute for every sub-time step the four
   vertex residuals with the first-order scheme.

The recomputation is local because the update of each grid point is
written as the sum of four residuals, one from each quadrilateral sharing
it, and the four residuals of one quadrilateral sum to an approximation
of the flux through its boundary (Eqs. (15)–(16)); this guarantees local
conservation when some quadrilaterals use first-order residuals and their
neighbours high-order ones ([local conservation](/results/local-conservation-flux-form.md)).
No local-extremum detection (as in their ref. [14]) and no
discrimination of smooth extrema (as in their ref. [25]) are used
(§3.2.2). The first-order
scheme "amounts to global Lax–Friedrichs" ([Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md)).
Applying the procedure at each cycle of the
[deferred-correction](/methods/deferred-correction.md) iteration would
make the scheme domain-invariant preserving, they state; in the tests it
is applied once per time step, not per cycle.

**Evidence** (§5.2). On a radial Sod problem ($[-1,1]^2$, $200^2$ points,
CFL 1, $T=0.16$) MOOD never activates the first-order scheme, so the
results are fourth order everywhere, with over- and undershoots at the
shock; the flux limiter removes the overshoot and reduces the undershoot
(Figs. 8–9; [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)).
On a radial shock with pressure ratio 1000 ($[-1.5,1.5]^2$, $200^2$,
$T=0.025$) MOOD is required; the flagged first-order elements are few and
localized around the discontinuities (Fig. 10). The authors give no
CPU cost of the recomputation.

## With deferred correction and residual distribution

[Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) use MOOD
(their ref. [12]) as the positivity enforcement of a fourth-order
deferred-correction residual-distribution scheme, DeC(4,4) with cubic
Bernstein elements, on the radial Sod problem with
[entropy correction terms](/methods/entropy-correction-term.md); with it
the computation works (§4.1, Fig. 5). The paper does not describe the
detection criteria or the fallback scheme.

## A posteriori subcell finite-volume limiting of ADER-DG

[Gaburro et al. (2024)](/sources/gaburro-2024.md) (§3.4, arXiv v1) recall
the a posteriori subcell finite-volume limiter of Dumbser and Loubère for
modal ADER-[DG](/methods/discontinuous-galerkin.md) on polygonal meshes
and add a third detection criterion to it. After the unlimited candidate
DG update:

1. **Projection.** Each polygon is split into its barycentric triangles,
   each of them into $N^2$ sub-triangles; the candidate is projected onto
   their averages (Eq. 35).
2. **Detection.** A subcell is troubled if (i) $\rho$ or $p$ falls below
   $10^{-12}$, or (ii) it violates a relaxed discrete maximum principle
   over the neighbour subcells with margin
   $\max\big(\delta_0,\ 10^{-3}(\max-\min)\big)$, $\delta_0=10^{-4}$
   (Eqs. 36–37), or (iii), new, a shock sensor fires (see below).
3. **Recomputation.** Troubled subcells are recomputed with a
   second-order MUSCL–Hancock scheme ("equivalent to a second order
   ADER-FV scheme"; [MUSCL–Hancock](/methods/muscl-hancock.md)) whose slopes are
   chosen among candidates by an ENO rule that minimizes $S_x^2+S_y^2$
   variable by variable (page-local slopes $S_x$, $S_y$; Eq. 38); a DG
   polynomial whose subcell integrals match the new averages is then
   rebuilt (Eqs. 40–41, projection times reconstruction equal to the
   identity).
4. **Safeguards.** A cell troubled in two consecutive steps keeps its
   stored subcell averages instead of a re-projection; the troubled flag
   is extended to the direct neighbours, and no correction is applied to
   the fluxes between limited and unlimited cells.

The relaxed maximum principle of step 2(ii) is the same as Maltsev et
al.'s strict numerical-admissibility criterion below ($10^{-4}$ floor,
$10^{-3}$ relative margin); Maltsev et al. apply it before the step,
Gaburro et al. after it.

The new criterion (iii) and the corrector it selects are the paper's
contribution (§4.4). The DG scheme evolves primitive variables, which
avoids pressure oscillations at material interfaces but gives wrong
shock speeds. A subcell is "shock-triggered" when an undivided-divergence
sensor attributed to Balsara is negative,
$$\sigma_{i,\alpha}=\frac{\widetilde{\nabla\cdot v}\big|_{i,\alpha}+m_1h_{i,\alpha}c_{\min}}{m_1h_{i,\alpha}c_{\min}}<0,$$
with $\widetilde{\nabla\cdot v}$ the face sum of $(v^-+v^+)\cdot n$
weighted by face length and scaled by $h_{i,\alpha}/|\tau_{i,\alpha}|$,
$h_{i,\alpha}=\sqrt{|\tau_{i,\alpha}|}$ for subcell $\tau_{i,\alpha}$, and
$c_{\min}$ the smallest sound speed over its faces (Eqs. 65–66; page-local
$\sigma_{i,\alpha}$, $m_1$, $c_{\min}$). The constant $m_1\in[1,15]$ is 1
for single-gas Euler and 15 for multi-material flows. Shock-triggered
subcells are recomputed in **conservative** variables with the Rusanov
flux ([Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md); Eq. 67) and
converted back; the other troubled subcells (positivity or maximum-principle
failures, e.g. at material interfaces) are recomputed in primitive variables
with path-conservative fluctuations
([path-conservative schemes](/methods/path-conservative-scheme.md)). The
conservative correction removes the local conservation defect where the
scheme needs it, so the authors' modified
[Lax–Wendroff theorem](/results/lax-wendroff-theorem.md) applies; their
Prop. 4 shows that a face-data mismatch of order $h^{1+\beta}$, $\beta>0$,
between limited and unlimited cells keeps the scheme quasi-conservative,
which is their justification for extending the flag to neighbours
instead of correcting the fluxes of unflagged cells.

**Evidence** (§5, $N=1$–$3$, CFL 0.1 for the first ten steps and 0.5
afterwards). On a circular Sod explosion the primitive-variable scheme
run everywhere, shocks included, gives a wrong shock speed, and the
shock-triggered conservative correction restores it (Fig. 3;
[explosion and implosion problems](/benchmarks/explosion-and-implosion-problems.md)).
On the Lax tube the conservative limiter activates "exactly where the
shock wave is located" (Fig. 2). On the two-dimensional shock–helium-bubble
interaction a second-order conservative ENO finite-volume scheme on
$h=1/750$ emits spurious pressure waves from the interface, while the
$N=2$ scheme on $h=1/150$ shows none; the limiter is active at both the
interface and the shock, and the conservative form is used only in the
shock-triggered cells (Figs. 8–9;
[shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)).

[Ciallella et al. (2024)](/sources/ciallella-2024.md) (§3.4, Remark 1,
§5.3.2, arXiv v1) use the same a posteriori limiter, after Gaburro and
Dumbser (2021), in modal ADER-DG on triangles: troubled cells are
recomputed with a second-order MUSCL–Hancock TVD scheme on $(2N+1)^d$
sub-triangles, so the DG time step
$\Delta t<\mathrm{CFL}\,h_{\min}/\big((2N+1)a\big)$
(Eq. 14; $h_{\min}$ the smallest mesh size, page-local) already satisfies the subcell condition with $N=0$. Troubled
cells on a curved wall use a corrected wall flux instead of their
high-order boundary reconstruction, which the authors call at most third
order; on a shock–cylinder interaction on an embedded mesh the only
residual disturbances lie in these limiter-flagged boundary cells (§6.3,
Fig. 9).

## A posteriori local subcell correction of DG

[Vilar & Abgrall (2024)](/sources/vilar-2024.md) (§3, HAL preprint v1)
correct a modal DG scheme on 2D unstructured and polygonal grids inside
the cell, at the level of subcell fluxes, rather than replacing the cell
polynomial. The DG scheme of degree $N$ is first written exactly as a
finite-volume scheme on $n_N=(N+1)(N+2)/2$ subcell means with
reconstructed fluxes $\hat F_{mp}$ on the interior subcell faces
([DG–subcell finite-volume equivalence](/results/dg-subcell-finite-volume-equivalence.md);
page-local $n_N$, $\bar u_m$, $\hat F_{mp}$). Each forward-Euler stage of
SSP-RK3 then follows the MOOD loop (§3.3):

1. compute the DG candidate and project it onto submeans $\bar u_m$;
2. **detect** troubled subcells with a physical admissibility detector
   (maximum principle for scalar laws, positive density and internal
   energy for Euler, NaN) and a numerical one, the relaxed discrete
   maximum principle on submeans with margin
   $\max\big(10^{-4},\ 10^{-3}(\max-\min)\big)$ over a neighbourhood that is
   cell-wise (all subcells of the cell and its face neighbours) for linear
   problems and subcell-wise (face and node neighbour subcells) for
   nonlinear ones; for Euler the numerical check uses the total energy only
   (Eqs. (3.3), (4.3), (4.6), §4.3);
3. **relax** the numerical check at smooth extrema with a vertex-based
   test on linearized derivatives, after Kuzmin's hierarchical slope
   limiter, applied at subcell level in all tests (Eqs. (3.4)–(3.6),
   Remark 6);
4. **correct**: on every face of a troubled subcell replace $\hat F_{mp}$ by
   a first-order finite-volume flux (global Lax–Friedrichs) between the two
   submeans, recompute only the troubled subcells and their face
   neighbours, map back to moments with $P^{-1}$ and iterate the detection.

The correction is conservative at subcell level by construction, and with
a first-order fallback it enforces the maximum principle or positivity,
provided the initial data are set from subcell integrals and not by nodal
interpolation or $L^2$ projection (Remark 8;
[bound preservation](/properties/bound-preservation.md)). The authors
state, "up to our knowledge", that it is the only technique on fully
unstructured grids that modifies the scheme locally at subcell level
without affecting the rest of the cell, and contrast it with subcell
limiters that discard the whole DG polynomial of a troubled cell, "a
waste of information" (§1, §3;
[subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md)).
Second-order TVD or WENO fallback fluxes are possible but not used here
(Remark 7).

**Blended correction** (new in this paper, Eq. (3.7)). The corrected flux
is $\theta_{mp}$ times the first-order flux plus $(1-\theta_{mp})\hat F_{mp}$,
with "very naive" weights (page-local $\theta_{mp}$, not the Zhang–Shu
factor): 1 on the faces of the troubled subcell, $3/4$ on the remaining
faces of its face neighbours, $1/2$ on the not-yet-corrected faces of its
node neighbours, and $1/4$ on the remaining faces of the face neighbours of
those (Fig. 4). The 1D version had instead suppressed the remaining
subcell oscillations by also marking, for $N\ge3$, the face neighbours of a
troubled subcell (§3.3–3.4). On 2D Burgers at sixth order ($\mathbb P^5$, 576 triangles) it
corrects 14 % of subcells on average against 10 %, needs 1.46 correction
iterations on average (maximum 3) against 2.86 (maximum 6), runs in 2 min
15 s against 2 min 22 s, and gives a sharper, less oscillatory shock (§3.4,
Figs. 5–9; hardware not stated). An a priori, FCT-type version is announced
([convex limiting](/methods/convex-limiting.md)).

**Evidence** (§4, mostly $\mathbb P^5$ on 100–1054 triangles): smooth
advection keeps sixth order with the correction never active ($L^1$ rates
6.00 and 5.97 at $h=1/10,1/20,1/40$; Table 1); a crenel advected one period
stays in $[8.5\times10^{-6},1]$ against $[-0.06,1.06]$ uncorrected (Fig. 12);
solid-body rotation keeps the global maximum principle (Fig. 22;
[solid-body rotation](/benchmarks/solid-body-rotation.md)); the KPP
problem gives the entropic spiral where uncorrected DG does not (Fig. 33;
[KPP rotating wave](/benchmarks/kpp-rotating-wave.md)); Sedov with the
energy in one subcell and background pressure $10^{-14}$ runs on 271 cells,
where "any scheme lacking positivity-preserving property or a rigorous
stabilization technique would fail" (stated; Figs. 38–39;
[Sedov blast wave](/benchmarks/sedov-blast-wave.md)); and the Mach 3
[forward-facing step](/benchmarks/forward-facing-step.md) runs on 680
cells without corner refinement or scheme modification (Fig. 41). With the
correction active, uniform subdivisions resolve better than non-uniform
ones, which the authors attribute to the numerical detector's dependence on
the subcell aspect ratio (§4.1.1, Figs. 19–21).

## Recomputation with artificial viscosity (compatible finite elements)

[Zampa & Dumbser (2025)](/sources/zampa-2025.md) (§3.3–3.4; arXiv v1)
keep the three MOOD steps but recompute flagged cells with the same
scheme plus a cellwise
[artificial viscosity](/methods/artificial-viscosity.md), instead of a
lower-order scheme. Their scheme is a semi-implicit DG/compatible finite
element method for weakly compressible isentropic flow
([asymptotic preservation](/properties/asymptotic-preservation.md)).

1. **Candidate.** Compute the candidate update with zero numerical
   viscosity.
2. **Detection.** Flag element $T$ when the candidate value $W$ (density
   or entropy) leaves a relaxed discrete maximum principle over the
   Voronoi neighbourhood $\mathcal N(T)$ of $T$ (page-local):
   $$\min_{\mathcal N(T)}W-\delta_T\le W(x)\le\max_{\mathcal N(T)}W+\delta_T,\qquad \delta_T=\max\Big(10^{-4},\ 10^{-3}\big(\max_{\mathcal N(T)}W-\min_{\mathcal N(T)}W\big)\Big).$$
   The criterion follows Tavelli & Dumbser (Eqs. (21)–(22)).
3. **Recomputation.** Set the viscosity to $\tfrac12h\,s_{\max}$ on
   flagged elements, with page-local $h$ the mesh size and $s_{\max}$ an
   estimate of the maximum wave speed. Use a small floor value elsewhere
   (Eq. (23)), and recompute the step.

The entropy transport is computed, checked and recomputed first. The
coupled momentum–pressure–density step follows, checked on the density
(Algorithm, §3.4). The viscosity enters through the interior-penalty,
div–div and curl–curl terms of a regularized system, so the
recomputation needs no subcell grid or second scheme. On a circular
explosion ($120\times120$, degree 2) the viscosity is active only near
the discontinuities, and the authors report no spurious oscillations
(§4.3, Figs. 3–4). They call the method "one of the first works that uses
a posteriori limiting in the context of compatible finite element
exterior calculus" (§1).

## PAD and NAD criteria used a priori

[Maltsev et al. (2023)](/sources/maltsev-2023.md) (§2.5, Eqs. 36–37,
Appendix A) take the two detection criteria of MOOD into the
[troubled-cell indicator](/definitions/troubled-cell-indicator.md) of a
hybrid DG–finite-volume scheme on unstructured meshes, which replaces the
higher DG modes of a troubled cell by a same-order CWENOZ reconstruction
([WENO limiters for DG](/methods/weno-limiter-dg.md)):

- **physical admissibility (PAD)**: reject negative or NaN density or
  pressure;
- **numerical admissibility (NAD)**: a relaxed discrete maximum principle,
  $$\min_{y\in V_i}u^n(y)-\delta_{\mathrm N}\le u(x)\le\max_{y\in V_i}u^n(y)+\delta_{\mathrm N},\qquad
  \delta_{\mathrm N}=\max\Big(10^{-4},\ \alpha_{\mathrm N}\big[\max_{V_i}u^n-\min_{V_i}u^n\big]\Big),$$
  with page-local margin $\delta_{\mathrm N}$ and relaxation $\alpha_{\mathrm N}$;
  $\alpha_{\mathrm N}=10^{-3}$ is the strict variant ("MOOD$^O$") and
  $\alpha_{\mathrm N}=10^{-1}$ the relaxed one ("MOOD$^R$"). For the Euler
  equations only density and energy are checked.

They differ from the original MOOD in that the unlimited DG solution is
checked at every Runge–Kutta stage, before the fluxes are computed, and the
neighbour solutions are compared at the same time level; a priori
checking avoids recomputing neighbours, which a posteriori MOOD needs and
which makes it costlier though more robust (§1). Two further choices are
studied. The **bounds** of the NAD come either from the cell and its
direct side neighbours ("limited", L) or from all cells of the
reconstruction stencil ("extended", X), after Tsoutsanis's finding that
extended bounds let a MUSCL limiter reach fourth order while
direct-neighbour bounds activate it in smooth regions (Appendix A). The
**frequency** is either a re-check at every stage or a flag frozen for
the whole step. Their findings:

- extended bounds flag far fewer cells in smooth regions; limited bounds
  over-flag and over-diffuse profiles (§3.2, Figs. 6–7; App. C);
- the strict NAD spuriously flags the smooth vortex core of the
  [isentropic vortex](/benchmarks/isentropic-vortex.md), 26–46 % of cells
  on the coarsest meshes and 0.08–0.16 % on the finest (Table 1, Fig. 4),
  and flags erratically on the Shu–Osher problem (§3.3);
- on square-wave advection MOOD$^O_X$ is the best compromise, DG accuracy
  without oscillations (App. C);
- on [double Mach reflection](/benchmarks/double-mach-reflection.md) only
  the relaxed MOOD$^R$ resolves the slip-stream roll-up; the more
  sensitive indicators flag larger regions (§3.4, Figs. 10–11);
- re-checking at every stage or not makes a negligible difference
  (§3.2, Fig. 7).

A safety check on the reconstruction, positive density and pressure and
relative face-point jumps below 0.8 of the cell value, with a fall-back to
second-order MUSCL or first-order Godunov "as in MOOD", was never
activated in their tests (§2.4, Eq. 34).

## A posteriori against a priori

[Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) take the subcell
resolution $N_{\mathrm{FV}}=2N+1$ of their DG finite-volume subcell
scheme from the "a posteriori FV sub-cell limiting" of Dumbser et al.,
and call their own switching, decided by a modal-decay indicator before
the step and after each Runge–Kutta stage, "a priori" (§1, §4.3, §7.2;
[subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md),
[troubled-cell indicator](/definitions/troubled-cell-indicator.md)). In
the a priori route the indicator decides; in MOOD the candidate solution
itself does, so no smoothness threshold has to be tuned for the
admissibility part, at the cost of computing every step twice in the
flagged cells *(compiler check, not in the sources)*.

[Berta et al. (2024)](/sources/berta-2024.md) (§3.4, arXiv v4) call the
order reduction of their fourth-order finite-volume MHD scheme a
"fallback" and liken it to that of Núñez-de la Rosa and Munz; the switch
is decided from a discontinuity detector evaluated on the cell averages
at the beginning of the stage, not from a candidate solution, so it is
an a priori switch in the sense of this page
([troubled-cell indicators](/definitions/troubled-cell-indicator.md)).

## Qualifications

- With only positivity and NaN checks, MOOD as used here is a robustness
  fallback, not an oscillation control: Abgrall & Nassajian Mojarrad's
  radial Sod results keep over- and undershoots because no cell is
  flagged (§5.2.2). A [bound-preserving](/properties/bound-preservation.md)
  guarantee requires the first-order fallback itself to be invariant-domain
  preserving and the check to be applied wherever a convex combination is
  formed; the authors state the first part and do not do the second.
- Abgrall & Nassajian Mojarrad print the residual of Eq. (15b) with
  $\Delta y$ multiplying both the $x$- and $y$-direction terms, and
  Eq. (16) with the mesh sizes swapped; the quadrilateral sum that gives
  the boundary flux needs $\Delta y$ on the $x$-part and $\Delta x$ on the
  $y$-part *(compiler check, not in the sources)*.

- The subcell resolution of the a posteriori limiter differs between
  the sources by convention: $N^2$ sub-triangles per barycentric triangle
  of a polygon in Gaburro et al. (§3.4), $(2N+1)^d$ sub-triangles per
  triangle in Ciallella et al. (Remark 1), and $N_{\mathrm{FV}}=2N+1$
  subcells per direction in the a priori scheme of Mossier et al.
- Gaburro et al. state the vanishing-defect hypothesis of their
  Lax–Wendroff proposition as $\sup\lVert\Delta^n_i\rVert=O(1)$ and define
  $O(1)$ in the text as "a quantity vanishing when $h\to0$", i.e. $o(1)$
  (Eqs. 47, 51).
- Zampa & Dumbser's Eq. (21) prints the time level $t^n$ on both the
  tested value and the neighbourhood bounds, and Eq. (23) says "if (22) is
  violated", where (22) defines $\delta_T$ and (21) is the criterion
  (arXiv v1). Their scheme carries the entropy by a non-conservative
  transport equation, and they do not expect shocks to be computed correctly
  at large shock Mach numbers (§3.2.2). Their explosion test has a
  pressure ratio of 10 (§4.3).
- Maltsev et al. attribute the two NAD relaxations to different
  references in §2.5 and in Appendix C. Their observed orders with an
  active indicator, up to 6.89 at $N=4$, are an artefact of the troubled
  fraction falling under refinement, as they state (Appendix B).

# Citations

- [Abgrall & Nassajian Mojarrad (2024)](/sources/abgrall-2024.md) — §2.1, Eqs. (15)–(16); §3.2.1–3.2.2; §5.2.2–5.2.3, Figs. 8–10.
- [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) — arXiv v4: §4.1, Fig. 5.
- [Gaburro et al. (2024)](/sources/gaburro-2024.md) — arXiv v1: §3.4, Eqs. (35)–(41); §4.3.1, Prop. 4; §4.4, Eqs. (65)–(67); §5, Figs. 2–3, 8–9.
- [Ciallella et al. (2024)](/sources/ciallella-2024.md) — arXiv v1: §3.4, Remark 1, Eq. (14); §5.3.2; §6.3, Fig. 9.
- [Berta et al. (2024)](/sources/berta-2024.md) — arXiv v4: §3.4 (a priori "fallback").
- [Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) — §1; §4.3; §7.2 (a priori contrast).
- [Vilar & Abgrall (2024)](/sources/vilar-2024.md) — HAL preprint v1: §1; §3.1–3.4, Eqs. (3.3)–(3.7), Remarks 6–8, Figs. 4–9; §4.1–4.3, Table 1, Figs. 12, 19–22, 33, 38–39, 41.
- [Zampa & Dumbser (2025)](/sources/zampa-2025.md) — arXiv v1: §1; §3.2.2; §3.3 Eqs. (21)–(23); §3.4; §4.3, Figs. 3–4.
- [Maltsev et al. (2023)](/sources/maltsev-2023.md) — §1; §2.4, Eq. (34); §2.5, Eqs. (36)–(37); §3.1–3.4, Table 1, Figs. 4, 6–11; Appendices A–C.
