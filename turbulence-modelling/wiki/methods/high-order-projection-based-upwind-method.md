---
type: Method
title: "High-order projection-based upwind (HOPU) method"
description: "HOPU restricts the upwind penalty of a high-order discontinuous convective form to the part of the velocity jump that a facet projection of order l cannot represent, with l chosen facet by facet from a jump indicator; in implicit LES of channel and periodic-hill flow it removes excess near-wall numerical dissipation."
status: established
aliases: [HOPU, high-order projection-based upwinding, adaptive HOPU, projection-based upwind stabilization]
tags: [implicit-les, numerical-dissipation, dg, boundary-layer]
timestamp: 2026-10-26T07:42:00Z
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
component of the jump orthogonal to facet polynomials of order $l$, so that
the low-order content of the jump is convected with a central flux and the
[numerical dissipation](/properties/numerical-dissipation.md) is confined to
high-order jump content, "in the spirit of" the variational multiscale
method (§3.3). An adaptive variant chooses $l$ facet by facet from a jump
indicator. The authors interpret it as "a wall model approach for standard
DG ILES" (§6); as defined in §3.3 it prescribes no wall stress and uses
no matching height, unlike the methods of
[wall-modelled LES](/methods/wall-modelled-les.md).

Page-local notation (Lederer et al. 2023, translated): $N$ the polynomial
order of the velocity (the source's $k$); $l$, $0\le l\le N$, the order of
the facet projection; $\mathcal P^l$ the facet-wise $L^2$ projection onto
tangential vector polynomials of order $l$ (the source's $\Pi^l_{\hat V}$,
renamed because $\Pi$ is the SGS flux); $\boldsymbol u_h$ the discrete
velocity; $[\![\cdot]\!]$ the face jump and $\{\!\{\cdot\}\!\}$ the registry's
face average (the source's $\langle\cdot\rangle$, renamed because the bracket
is the registry's Reynolds average); $r_J$ the jump indicator and $r_{J,i}$ its
thresholds (the source's $\eta$, $\eta_i$, renamed because $\eta$ is the
Kolmogorov length).

## Baseline discretization

The host scheme is the **mass-conserving mixed-stress (MCS)** method of
Gopalakrishnan, Lederer and Schöberl for incompressible flow, as recalled by
Lederer et al. (2023, §2.2): an $H(\mathrm{div})$-conforming
Raviart–Thomas velocity of order $N$ with piecewise-polynomial pressure of
order $N$, so that the discrete velocity is exactly divergence free
($\nabla\cdot V_h=Q_h$, Eq. 5); a trace-free stress of order $N+1$ whose
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

## The HOPU convective form

HOPU replaces the jump in the upwind term by its high-order remainder
(§3.3):
$$c^{\mathrm{HOPU}}_h(\boldsymbol u_h,\boldsymbol u_h,\boldsymbol v_h)=\sum_T\int_T(\nabla\boldsymbol u_h\,\boldsymbol u_h)\cdot\boldsymbol v_h\,dx+\sum_F\int_F\Big(-(\boldsymbol u_h\cdot\boldsymbol n)[\![\boldsymbol u_h]\!]\cdot\{\!\{\boldsymbol v_h\}\!\}+\tfrac12(\boldsymbol u_h\cdot\boldsymbol n)\,(I-\mathcal P^l)[\![\boldsymbol u_h]\!]\cdot[\![\boldsymbol v_h]\!]\Big)ds.$$
The limits are $l=0$, nearly standard upwinding ("the lowest order part is
of no relevance"), and $l=N$, no upwinding, i.e. central convection. As
$h\to0$ the jumps vanish and so does the effect of upwinding and of HOPU
(§3.3).

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

## Comparison with no-model and VMS implicit LES

Lederer et al. compare three approaches on the same MCS discretization:
**no-model implicit LES** (the upwind form above), a **projection-based
three-scale variational multiscale (VMS)** model in which the
[WALE](/methods/wale-model.md) eddy viscosity ($C_w=0.5$,
$\Delta=(\Delta x\Delta y\Delta z)^{1/3}/(N+1)$) acts only on the strain
minus its $L^2$ projection onto element-wise polynomials of order $m$
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

## Qualifications

- No analysis of the HOPU form (energy stability, consistency) is given;
  the central treatment of the low-order jump content removes its upwind
  dissipation without a stability proof. Evidence is two flows at one
  Reynolds number each.
- **Printed slips (arXiv v1).** The upwind term of Eq. (9) and of the HOPU
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
- The version read is the arXiv v1 preprint; the published article may
  differ.

# Citations

- [Lederer et al. (2023)](/sources/lederer-2023.md) — arXiv v1: §1.1 (MCS dissipation); §2.2, Eqs. (2)–(9) (MCS method, upwind convective form, IMEX, quadrature); §3.1, Eqs. (10)–(14) (projection-based VMS with WALE); §3.2 (no-model implicit LES); §3.3, Figs. 2–3 (HOPU, jump indicator, adaptive order); §4, §4.1, Tables 1–2, Figs. 1, 4–6 (channel, wall-stress identity); §5, §5.1, Table 3, Figs. 7–10 (periodic hill); §6.
