---
type: Method
title: "High-order projection-based upwind (HOPU) method"
description: "HOPU restricts the upwind penalty of a high-order discontinuous convective form to the part of the velocity jump that a facet projection of order l cannot represent, with l chosen facet by facet from a jump indicator; in implicit LES it removes excess near-wall dissipation in channel, hill and transitional airfoil flow without altering transition."
status: established
aliases: [HOPU, high-order projection-based upwinding, adaptive HOPU, projection-based upwind stabilization]
tags: [implicit-les, numerical-dissipation, dg, boundary-layer, transition]
timestamp: 2026-10-27T15:50:00Z
---

# High-order projection-based upwind (HOPU) method

The **high-order projection-based upwind (HOPU)** method of
[Lederer et al. (2023)](/sources/lederer-2023.md) is a modification of the
upwind stabilization of a discontinuous (DG-type) convective form, designed
for [implicit LES](/definitions/implicit-les.md) of under-resolved
wall-bounded turbulence. In such a scheme the upwind penalty on the
velocity jump across element faces is "recognized" as the main source of
stability (§3.2, citing a dispersion–diffusion analysis of DG), but it
penalizes the whole resolved range. HOPU applies the penalty only to the
component of the jump orthogonal to facet polynomials of degree $l$, so that
the low-order content of the jump is convected with a central flux and the
[numerical dissipation](/properties/numerical-dissipation.md) is confined to
high-order jump content, "in the spirit of" the variational multiscale
method (§3.3). An adaptive variant chooses $l$ facet by facet from a jump
indicator. The authors interpret it as "a wall model approach for standard
DG ILES" (§6); as defined in §3.3 it prescribes no wall stress and uses
no matching height, unlike the methods of
[wall-modelled LES](/methods/wall-modelled-les.md).
[Lederer et al. (2026)](/sources/lederer-2026.md) carry the method over
to transitional flow on the [Eppler 387 airfoil](/benchmarks/eppler-387-airfoil.md)
with a new, projection-type time integration of the host scheme, and
cite its lineage: a projection-based upwind method "was first introduced
as a DG stabilization method for hyperbolic systems" and later established
for diffusion equations in mixed form (§1, citing earlier work).
They place HOPU beside the
[jump-penalty stabilization](/methods/jump-penalty-stabilization.md) of
under-resolved DG turbulence, which "ha[s] sparked interest" (§1).

Page-local notation (Lederer et al. 2023 and 2026, translated): $N$ the polynomial
degree of the velocity (the source's $k$); $l$, $0\le l\le N$, the degree of
the facet projection; $\mathcal P^l$ the facet-wise $L^2$ projection onto
tangential vector polynomials of degree $l$ (the source's $\Pi^l_{\hat V}$,
renamed because $\Pi$ is the SGS flux); $\boldsymbol u_h$ the discrete
velocity; $[\![\cdot]\!]$ the face jump and $\{\!\{\cdot\}\!\}$ the registry's
face average (the source's $\langle\cdot\rangle$, renamed because the bracket
is the registry's Reynolds average); $r_J$ the jump indicator and $r_{J,i}$ its
thresholds (the source's $\eta$, $\eta_i$, renamed because $\eta$ is the
Kolmogorov length).

## Baseline discretization

The host scheme is the **mass-conserving mixed-stress (MCS)** method of
Gopalakrishnan, Lederer and Schöberl for incompressible flow, as
Lederer et al. (2023, §2.2) describe it: an $H(\mathrm{div})$-conforming
Raviart–Thomas velocity of degree $N$ with piecewise-polynomial pressure of
degree $N$, so that the discrete velocity is exactly divergence free
($\nabla\cdot V_h=Q_h$, Eq. 5); a trace-free stress of degree $N+1$ whose
normal–tangential continuity is imposed by a hybrid facet unknown that
approximates the tangential velocity; and weakly imposed stress symmetry.
The authors state that MCS needs less numerical dissipation for the
inf-sup stability of the Stokes part than an interior-penalty hybrid DG
method (§1.1). The convective form (Eq. 9) is the DG upwind form of
Lehrenfeld & Schöberl,
$$c_h(\boldsymbol u_h,\boldsymbol u_h,\boldsymbol v_h)=\sum_T\int_T(\nabla\boldsymbol u_h\,\boldsymbol u_h)\cdot\boldsymbol v_h\,dx+\sum_F\int_F\Big(-(\boldsymbol u_h\cdot\boldsymbol n)[\![\boldsymbol u_h]\!]\cdot\{\!\{\boldsymbol v_h\}\!\}+\tfrac12(\boldsymbol u_h\cdot\boldsymbol n)[\![\boldsymbol u_h]\!]\cdot[\![\boldsymbol v_h]\!]\Big)ds,$$
as printed (see Qualifications for the absolute value); the last term is the
upwind stabilization, and dropping it gives a central flux. Since the
velocity is normal-continuous, only its tangential components jump. Time
integration is the IMEX Runge–Kutta scheme ARS(2,2,2) with explicit
convection and implicit Stokes part, so a single matrix factorization
serves the whole run (§2.2). Implementation: NGSolve/Netgen.

**Projection-type time integration (Lederer et al. 2026).** For larger
Reynolds numbers Lederer et al. (2026, §2.3, Eqs. 10–14) replace the IMEX
scheme by a Chorin-type splitting of the same MCS discretization, written
to first order in time:

1. an implicit Stokes-like step without the incompressibility constraint,
   with explicit convection, for an intermediate velocity
   $\boldsymbol u_h^*$ (page-local); static condensation of the stress and
   skew unknowns leaves a symmetric positive-definite system in the
   element and facet velocities, solved by preconditioned conjugate
   gradients with an element-wise BDDC preconditioner whose primal
   constraints are dropped when $\nu\Delta t\ll1$, which makes it "purely
   local" (stated, with no scaling data);
2. a projection onto exactly divergence-free velocities through a
   hybridized mixed Poisson problem in a normal-discontinuous
   Raviart–Thomas space with a facet pressure, whose condensed
   symmetric positive-definite matrix is solved with PETSc's algebraic
   multigrid (GAMG); it returns the part $\boldsymbol g_h$ (page-local;
   the source's $\tilde{\boldsymbol u}_h$) of $\boldsymbol u_h^*$ that
   carries its divergence, so that the update is pointwise divergence free
   (Eq. 12; see Qualifications for its printed form).

They also state that exact quadrature of all bilinear forms "is crucial for
maintaining the stability of the method, especially in turbulent flow
regimes" (§2.2), and that the hybrid MCS variant with non-homogeneous
Dirichlet data used at the airfoil inlet is new (§2.2). The upwind
convective form is printed there with the absolute value,
$\tfrac12|\boldsymbol u_h\cdot\boldsymbol n|[\![\boldsymbol u_h]\!]\cdot[\![\boldsymbol v_h]\!]$
(Eq. 9), with the inlet jump taken against the prescribed inflow velocity.

## The HOPU convective form

HOPU replaces the jump in the upwind term by its high-order remainder
(§3.3):
$$c^{\mathrm{HOPU}}_h(\boldsymbol u_h,\boldsymbol u_h,\boldsymbol v_h)=\sum_T\int_T(\nabla\boldsymbol u_h\,\boldsymbol u_h)\cdot\boldsymbol v_h\,dx+\sum_F\int_F\Big(-(\boldsymbol u_h\cdot\boldsymbol n)[\![\boldsymbol u_h]\!]\cdot\{\!\{\boldsymbol v_h\}\!\}+\tfrac12(\boldsymbol u_h\cdot\boldsymbol n)\,(I-\mathcal P^l)[\![\boldsymbol u_h]\!]\cdot[\![\boldsymbol v_h]\!]\Big)ds.$$
The limits are $l=0$, nearly standard upwinding ("the lowest order part is
of no relevance"), and $l=N$, no upwinding, i.e. central convection. As
$h\to0$ the jumps vanish and so does the effect of upwinding and of HOPU
(§3.3).

Lederer et al. (2026, §3.2, Eqs. 15–16) print the HOPU form with
$\tfrac12|\boldsymbol u_h\cdot\boldsymbol n|\,(I-\mathcal P^l)[\![\boldsymbol u_h]\!]\cdot(I-\mathcal P^l)[\![\boldsymbol v_h]\!]$
as the last term, the projection acting on both the trial and the test
jump, and state the limits more sharply: $l=N$ makes $\mathcal P^l$ the
identity, "no upwinding occurs" and convection is central at all scales;
$0\le l<N$ removes the stabilization of the lower-order part; and the
standard upwind form is recovered when $\mathcal P^l$ is the zero
operator. The two prints coincide when the weight
$|\boldsymbol u_h\cdot\boldsymbol n|$ is constant on the facet, because
$I-\mathcal P^l$ is then an orthogonal projection under the weighted facet
integral; for a weight that varies along the facet they differ in general
*(compiler check, not in the sources)*. Lederer et al. (2026, §3.2) refer
to the 2023 paper for stability and implementation.

**Why near the wall.** In highly under-resolved runs the velocity jumps are
larger near the wall than in the outer flow, giving near-wall upwind
dissipation that is "not needed for stability" (§3.3, Figs. 2–3, 10).
Two ways to exploit this are named: a two-zone choice (HOPU near the wall,
standard upwinding outside), which works in a channel but is hard to set up
in complex geometry, and the **adaptive local order**.

**Adaptive HOPU.** On each facet the indicator
$$r_J=\frac{\int_F|(I-\mathcal P^l)[\![\boldsymbol u_h]\!]|\,ds}{\int_F|\{\!\{\boldsymbol u_h\}\!\}|\,ds}$$
(the "high order average absolute value jump") is compared with thresholds
$0=r_{J,0}<r_{J,1}<\dots<r_{J,N+1}=1$, and the local order is $l=i$ when
$r_{J,i}<r_J\le r_{J,i+1}$, recomputed after every time step. Thresholds
used: $\{0.025,0.05,0.1\}$ for $N=3$; $\{0.005,0.015,0.03,0.07,0.12,0.2\}$ for
$N=6$ (§3.3, §4.1). On the coarse periodic-hill mesh without HOPU the
indicator is high near the lower wall and downstream of the hill, with its
peak next to the separation point (§5.1, Fig. 10).

**Adaptive HOPU, second version.** Lederer et al. (2026, §3.2, §4) run the
same indicator with a different bracketing and different settings:
thresholds $r_{J,-1}=0<r_{J,0}<r_{J,1}<\dots<r_{J,N+1}=1$, local order
$l=i$ for $r_{J,i}<r_J\le r_{J,i+1}$ when $i\ge0$, and **reversion to
standard upwinding** when $r_J<r_{J,0}$; thresholds
$\{0.1,0.2,0.3,0.4\}$ for $N=3$; the local order recomputed every tenth
time step. These are settings of two versions of the method, not
competing claims. On the transitional airfoil the velocity jumps are
"significantly larger in the turbulent wall-bounded regions compared to
the laminar and outer regions" (§4, Fig. 3), the same observation as in
the channel and hill; the plotted mode of the local order on the coarsest
mesh has a legend listing only $l=0$ and $l=1$ (Fig. 3).

## Comparison with no-model and VMS implicit LES

Lederer et al. compare three approaches on the same MCS discretization:
**no-model implicit LES** (the upwind form above), a **projection-based
three-scale variational multiscale (VMS)** model in which the
[WALE](/methods/wale-model.md) eddy viscosity ($C_w=0.5$,
$\Delta=(\Delta x\Delta y\Delta z)^{1/3}/(N+1)$) acts only on the strain
minus its $L^2$ projection onto element-wise polynomials of degree $m$
(Eqs. 10–14; $m=1$ for $N=3$, $m=3$ for $N=6$), and **adaptive HOPU**.

**Turbulent channel flow** at $Re_\tau=392.24$ (§4; DNS of Moser, Kim &
Mansour; $N_e^3$ stretched hexahedra with $N_e$ elements per direction,
page-local; $\Delta t=0.001$; see
[turbulent channel flow](/benchmarks/turbulent-channel-flow.md)). The MCS
method needs no flow-rate controller: testing the momentum equation with a
constant velocity shows that a constant forcing fixes the mean wall stress
exactly (§4). Results (Table 2, Figs. 1, 4–6):

| $N_e/N$ | 6/3 | 12/3 | 16/3 |
|---|---|---|---|
| globally coupled DOF ($10^3$) | 43.2 | 331.0 | 775.7 |
| wall-element height in wall units over $N+1$ | 11.8 | 4.3 | 3.0 |
| bulk-$Re$ error, no model | 13.4% | 3.1% | 1.1% |
| bulk-$Re$ error, VMS | 16.3% | 4.7% | 2.7% |
| bulk-$Re$ error, adaptive HOPU | 0.7% | 1.0% | 0.6% |

The authors call the bulk-$Re$ error "only a rough" estimate. For $N=3$
adaptive HOPU "significantly" improves the mean velocity, especially at
$N_e=6$, resolving the buffer region and improving the log and outer
regions; Reynolds stresses change little except a slight near-wall
improvement; at $y^+=5$ HOPU removes excessive damping and gives "a much
better prediction of the high wave number range" of the spectrum. For $N=6$
($N_e=4,6,8$) HOPU makes no remarkable difference, and $N=6$ is better
overall than $N=3$ at roughly equal degrees of freedom. VMS matches no-model
LES on the finer meshes, where its eddy viscosity vanishes, and is slightly
worse on the coarsest ($N_e=6/N=3$, $N_e=4/N=6$), damping more and
under-resolving the buffer layer.

**[Periodic hill](/benchmarks/periodic-hill.md)** at $Re_h=2800$ (§5; DNS of
Balakumar & Ilhwan; $N=3$; $12\times8\times6$ and $24\times16\times12$
elements): all approaches reproduce the mean streamwise velocity
reasonably; on the coarse mesh HOPU improves the wall-normal velocity at
$x=3$, 5 and 8 hill heights (reattachment region) and gives "significantly better"
$\langle v'v'\rangle$ and $\langle u'v'\rangle$ than no-model LES, while VMS
gives "slight to no improvement" (Figs. 8–9).

The authors conclude that the WALE-VMS model is not fundamentally different
from no model and that its added dissipation "can harm the implicit
dissipation mechanism"; whether the jump indicator is the best criterion
for HOPU is left open (§6).

## Transitional airfoil flow

Lederer et al. (2026, §3) leave explicit subgrid models out "due to their
inferior performance compared to ILES in a DG framework for wall-bounded
flow problems", citing the 2023 comparison above and a further DG study,
and compare no-model implicit LES (standard upwinding) with adaptive HOPU
on the [Eppler 387 airfoil](/benchmarks/eppler-387-airfoil.md) (§4,
Tables 1–2), against the NASA wind-tunnel data of McGhee et al. as cited:

- two cases, $Re_c=10^5$ at $10^\circ$ incidence and $Re_c=3\times10^5$ at
  $4^\circ$, both with laminar separation and turbulent reattachment on
  the suction side (see
  [laminar separation bubble](/definitions/laminar-separation-bubble.md));
- extruded curved hexahedral meshes of 2352, 7200 and 14400 elements
  (m1–m3), first-element height $2.6$, $1.6$ and $1.2\times10^{-3}$ chords,
  $N=3$, span $0.1$ chord, no free-stream turbulence; HOPU run on m1 and
  m2 only; m3 is taken as grid-independent because the $L^2$ difference of
  the mean pressure coefficient between consecutive meshes falls below
  0.01 there.

| case | run | $C_L$ | $C_D$ | separation $x/c$ | reattachment $x/c$ |
|---|---|---|---|---|---|
| $Re_c=10^5$, $10^\circ$ | experiment | 1.200 | 0.0413 | – | – |
| | ILES m1 / HOPU m1 | 1.274 / 1.271 | 0.0432 / 0.0436 | 0.007 / 0.007 | 0.010 / 0.010 |
| | ILES m2 / HOPU m2 | 1.268 / 1.266 | 0.0421 / 0.0425 | 0.008 / 0.008 | 0.016 / 0.016 |
| | ILES m3 | 1.259 | 0.0411 | 0.010 | 0.027 |
| $Re_c=3\times10^5$, $4^\circ$ | experiment | 0.792 | 0.0109 | 0.40 | 0.58 |
| | ILES m1 / HOPU m1 | 0.767 / 0.767 | 0.0116 / 0.0116 | 0.498 / 0.499 | 0.517 / 0.517 |
| | ILES m2 / HOPU m2 | 0.763 / 0.763 | 0.0113 / 0.0113 | 0.498 / 0.498 | 0.515 / 0.515 |
| | ILES m3 | 0.759 | 0.0113 | 0.467 | 0.560 |

Findings, as the authors state them:

- HOPU leaves pressure, lift, drag and the separation bubble essentially
  unchanged, which they call "crucial" because HOPU aims at the turbulent
  part "without affecting key quantities" (§4.1); the boundary-layer
  thicknesses and shape factor also differ negligibly (§4.2, Fig. 10).
- In the turbulent boundary layer, for $y^+>10$, HOPU over-predicts the
  mean tangential velocity, the turbulent kinetic energy and the Reynolds
  shear stress less than standard upwinding; the gain is largest at
  $Re_c=10^5$, where "the HOPU m1 case performs almost as well as the ILES
  m3 in terms of velocity profiles", which they attribute to the larger
  extent of turbulent flow (§4.2, Figs. 7–9). They describe HOPU's profiles
  as "under-dissipative" because it penalizes only part of the tangential
  velocity, as in the 2023 channel.
- The finest mesh predicts transition close to experiment, read as an
  advantage of the low-dissipation MCS scheme; the authors infer that the
  laminar disturbances leading to transition "are not significantly
  affected" by the refined stabilization, so that HOPU improves the
  turbulent part "regardless of the transition mechanism" (§5); the
  evidence for this is the two cases above.

No timings or parallel-scaling data are reported for the projection
solver (§2.3, §5).

## Qualifications

- No analysis of the HOPU form (energy stability, consistency) is given;
  the central treatment of the low-order jump content removes its upwind
  dissipation without a stability proof. Evidence is two flows at one
  Reynolds number each in the 2023 paper and one airfoil at two
  conditions in the 2026 paper, with no quantitative error metric for the
  boundary-layer profiles.
- **Versions of the adaptive rule.** The 2023 and 2026 papers differ in
  threshold bracketing, threshold values, the explicit reversion to
  standard upwinding below the lowest threshold, the update interval of the
  local order, and the time integration of the host scheme (IMEX against
  projection); the 2026 paper presents these as its settings, not as
  corrections of the 2023 ones.
- The 2026 paper's lift values lie above experiment at $Re_c=10^5$ (1.259
  to 1.274 against 1.200) and below it at $Re_c=3\times10^5$ (0.759 to 0.767
  against 0.792), and the computed separation at $Re_c=3\times10^5$ lies
  downstream of the measured one, which the authors note (§4.1); they
  summarize the coefficients as matching the experiment closely.
- **Printed slips (Lederer et al. 2026, arXiv v1).** Eq. (5) prints the
  stress term with $1/\nu$ where Eq. (2a) and the text after it have
  $1/(2\nu)$. The update Eq. (12) is printed as
  $\boldsymbol u_h^{n+1}=\boldsymbol u_h^n+\Delta t(\boldsymbol u_h^*-\boldsymbol g_h)$;
  since $\boldsymbol u_h^*$ and $\boldsymbol g_h$ are velocities, the
  dimensionally consistent divergence-free update is
  $\boldsymbol u_h^{n+1}=\boldsymbol u_h^*-\boldsymbol g_h$ *(compiler
  check, not in the sources)*. The averaging interval is given in
  "characteristic time lengths ($U_\infty/c$)", an inverse time
  *(compiler check, not in the sources)*. The text refers to "the last
  integral in (15)", which stands on the line numbered (16).
- **Printed slips (Lederer et al. 2023, arXiv v1).** The upwind term of Eq. (9) and of the HOPU
  form is printed with $(\boldsymbol u_h\cdot\boldsymbol n)$, not
  $|\boldsymbol u_h\cdot\boldsymbol n|$; a term described as dissipative
  upwinding needs the absolute value *(compiler check, not in the
  sources)*. §2.2 asks for $N$ Gauss points per direction for the stress
  mass form, whose integrand has degree $2N+2$ and needs $N+2$ points for
  exactness *(compiler check, not in the sources)*. Table 3 prints for the
  hill the same coupled-DOF counts as for the $N_e=6$ and 12 channels,
  although the hill meshes have 576 and 4608 elements against 216 and 1728
  *(compiler check, not in the sources)*.
- The VMS system matrix is recomputed only after a fixed interval, stated
  to have "negligible impact" (§3.1; interval and evidence not given).
- The 2026 paper prints the absolute value $|\boldsymbol u_h\cdot\boldsymbol n|$
  in both the upwind and the HOPU term (Eqs. 9, 16), the form that the
  compiler check on the 2023 print calls for, and states exact quadrature
  of all bilinear forms (§2.2).
- The versions read of both papers are arXiv v1 preprints (the 2026 one of
  August 2024); the published articles may differ.

# Citations

- [Lederer et al. (2023)](/sources/lederer-2023.md) — arXiv v1: §1.1 (MCS dissipation); §2.2, Eqs. (2)–(9) (MCS method, upwind convective form, IMEX, quadrature); §3.1, Eqs. (10)–(14) (projection-based VMS with WALE); §3.2 (no-model implicit LES); §3.3, Figs. 2–3 (HOPU, jump indicator, adaptive order); §4, §4.1, Tables 1–2, Figs. 1, 4–6 (channel, wall-stress identity); §5, §5.1, Table 3, Figs. 7–10 (periodic hill); §6.
- [Lederer et al. (2026)](/sources/lederer-2026.md) — arXiv 2408.06698v1: §1 (lineage, jump penalties); §2.2, Eqs. (2)–(9) (hybrid MCS, exact quadrature, upwind form with absolute value); §2.3, Eqs. (10)–(14), Fig. 1 (projection splitting, BDDC, GAMG); §3–3.2, Eqs. (15)–(16), Fig. 3 (no explicit model, HOPU form, adaptive rule and settings); §4, Tables 1–2, Fig. 4 (Eppler 387 cases, meshes, coefficients); §4.2, Figs. 7–10 (boundary-layer statistics); §5.
