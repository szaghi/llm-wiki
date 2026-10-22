---
type: Property
title: "Divergence-free magnetic field"
description: "The magnetic field of MHD obeys div B = 0; discretizations enforce it exactly, locally, through divergence cleaning or not at all, and Wu and Shu show that bound preservation of high-order MHD schemes requires a discrete divergence-free condition, recovered by a Godunov-symmetrization source term; the page adds locally divergence-free finite-volume reconstruction and constrained transport for unstaggered central schemes."
status: established
aliases: [div B = 0, solenoidal constraint, discrete divergence-free condition, DDF, divergence cleaning, GLM-MHD, constrained transport, CTM, locally divergence-free DG, locally divergence-free reconstruction, Powell source term, Godunov–Powell source term]
tags: [mhd, bound-preserving, positivity, dg, finite-volume]
timestamp: 2026-10-22T12:00:00Z
---

# Divergence-free magnetic field

The ideal MHD equations carry the involution $\nabla\cdot B=0$: it holds for
all time if it holds initially, but the conservative flux form does not
enforce it, and discretizations generally do not preserve any discrete
version of it. The sources of this bundle meet the constraint in five ways:
as a hypothesis that [bound preservation](/properties/bound-preservation.md)
needs ([Wu & Shu (2023)](/sources/wu-2023-b.md)); as a constraint built
into the reconstruction polynomial, cell by cell
([Liu et al. (2021)](/sources/liu-2021.md)); as a quantity controlled by
generalized-Lagrange-multiplier (GLM) divergence cleaning
([Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md);
[Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md));
through constrained transport in an unstaggered central scheme
([Kanbar, Touma & Klingenberg (2022)](/sources/kanbar-2022.md)) and in
finite-difference TENO codes ([Fu (2023)](/sources/fu-2023.md)).

## The Powell source term

Three sources add to the conservative MHD system the non-conservative
Godunov–Powell term, proportional to the divergence,
$$\partial_tu+\nabla\cdot f(u)+(\nabla\cdot B)\,S_B(u)=0,\qquad S_B=(0,\ B,\ v,\ v\cdot B)^\top$$
for the ordering $u=(\rho,\rho v,B,E)$ ($S_B$ page-local): Wu & Shu as the
Godunov symmetrization (§6.2, as recalled from Godunov 1972), Liu et al.
after Powell et al. (Eq. (1)), and Rueda-Ramírez et al. (2021) as the
Powell part $\Upsilon^{\mathrm{MHD}}$ of the resistive GLM-MHD system, whose
coefficient vector $(0,B,v\cdot B,v,0)$ for the ordering
$(\rho,\rho v,E,B,\psi_{\mathrm{GLM}})$ is the same vector, with $\mu_0=1$
(Eqs. (13)–(15)) *(compiler check, not in the sources: the components
agree after reordering)*. Rueda-Ramírez et al. (2021) state that these terms, together
with a GLM term required by Galilean invariance, are needed for the
continuous entropy analysis to hold, and they enter the entropy flux
potential through an extra term proportional to $(v\cdot B)B$ (§2.2,
Eqs. (21)–(22)).

## Divergence and bound preservation

[Wu & Shu (2023)](/sources/wu-2023-b.md) (§6) study multicomponent ideal MHD,
whose admissible set requires $0\le Y_k\le1$, $\rho>0$ and $p>0$ (Eq. (6.4)).
Its [geometric quasilinearization](/methods/geometric-quasilinearization.md)
writes the pressure constraint as
$\varphi(u;v_*,B_*)=u\cdot n_*+\tfrac12\lvert B_*\rvert^2>0$ for all auxiliary
velocities $v_*$ and fields $B_*$ (Eq. (6.5); page-local $\varphi$). With it:

- **First order** (Thm 6.1). Under
  $\Delta t\big(a^{(1)}/\Delta x+a^{(2)}/\Delta y\big)\le1$, the 2D
  Lax–Friedrichs update keeps the species and density constraints and
  satisfies
  $$\varphi(\bar u^{n+1}_{ij};v_*,B_*)>-\Delta t\,(v_*\cdot B_*)\,\mathrm{div}_{ij}\bar B,\qquad
  \mathrm{div}_{ij}\bar B=\frac{\bar B_{1,i+1,j}-\bar B_{1,i-1,j}}{2\Delta x}+\frac{\bar B_{2,i,j+1}-\bar B_{2,i,j-1}}{2\Delta y}.$$
  The update is therefore bound-preserving if the discrete divergence
  vanishes, the **discrete divergence-free (DDF) condition**; since
  $v_*\cdot B_*$ takes either sign, a nonzero divergence leaves the
  right-hand side negative for some auxiliary states.
- **High order** (Thm 6.2, proof omitted by analogy with Wu's 2018
  analysis). For finite-volume or DG cell-average schemes of degree $N\ge1$
  with Gauss-quadrature Lax–Friedrichs fluxes, if the point values at the
  mixed Gauss / Gauss–Lobatto points lie in $G$, then under the CFL bound
  with the first Gauss–Lobatto weight the same estimate holds with
  $\mathrm{div}_{ij}B=\tfrac12\big(\mathrm{div}^-_{ij}B+\mathrm{div}^+_{ij}B\big)$,
  built from the interior ($-$) and exterior ($+$) interface traces.
- **Standard schemes do not preserve the DDF condition** (Rem. 6.3).
  Globally divergence-free DG techniques are incompatible with the local
  [scaling limiter](/methods/zhang-shu-scaling-limiter.md), and a locally
  divergence-free DG basis gives only $\mathrm{div}^-_{ij}B=0$. The
  convex-decomposition analyses of the classical Zhang–Shu framework are
  therefore "inapplicable" to multidimensional MHD.

**The remedy: a discretized Godunov-symmetrization source** (§6.2). The
symmetrizable form above is discretized by a source built only from the
jumps of the normal magnetic field at the interface Gauss points
(Eq. (6.22)). With a locally divergence-free DG basis, $\mathrm{div}_{ij}B$
reduces to those jumps (Eq. (6.19)), the source cancels the offending term,
and the scheme is provably bound-preserving under $(1+\varepsilon_B)\nu\le\varpi$
(Thm 6.4), where $\nu=\Delta t(a^{(1)}/\Delta x+a^{(2)}/\Delta y)$ is the 2D
CFL number of this page, $\varpi=\mathsf w^{\mathrm{GL}}_0$ the first
Gauss–Lobatto weight (the source writes $\lambda$ and $\widehat\omega_1$) and $\varepsilon_B$ a
correction proportional to the normal-field jumps divided by the wave speeds
(page-local; the source's $\varepsilon$). The CFL penalty vanishes when the
normal field is continuous.

**Evidence** (§7). A third-order locally divergence-free DG method with the
source term, a locally divergence-free WENO limiter in KXRCF-flagged cells,
the scaling limiter and SSP-RK3 at CFL 0.15 keeps the admissible set
throughout a two-species MHD blast ($400^2$ cells, $t=0.01$, Fig. 5), and
computes a two-species MHD jet with inflow speed 800 and
$B=(0,\sqrt{4000},0)$ (Fig. 6). On the jet the run "fails quickly" without
any one of the three ingredients — scaling limiter, locally divergence-free
basis, source term — even with the WENO limiter; this is stated, no failure
figure is shown.

## Locally divergence-free reconstruction (finite volumes)

[Liu et al. (2021)](/sources/liu-2021.md) (§3.1–§3.3) carry the
locally divergence-free idea from DG bases to finite-volume reconstruction.
Their [WLS-ENO](/methods/wls-eno.md) polynomials $B^{\mathrm R}_1$,
$B^{\mathrm R}_2$ of degree $k$ in each cell are constrained so that
$\partial_xB^{\mathrm R}_1+\partial_yB^{\mathrm R}_2\equiv0$ in the cell
(Eqs. (15)–(16); $B^{\mathrm R}$ page-local):

1. $B^{\mathrm R}_2$ is reconstructed by the conservative weighted least
   squares, with its cell average imposed exactly;
2. the coefficients of $B^{\mathrm R}_1$ that appear in
   $\partial_xB^{\mathrm R}_1$ follow from matching the monomial
   coefficients of the identity, a square upper-triangular system with
   diagonal $1/((p_1-1)!\,p_2!)$ and therefore a unique solution for every
   degree (Eqs. (17), (24)–(26));
3. the remaining coefficients of $B^{\mathrm R}_1$ (pure $y$-derivatives)
   come from a reduced weighted least-squares fit (Eq. (18));
4. the procedure is repeated with the roles of the two components swapped
   and the two results averaged (Eqs. (19)–(20)), which removes the bias of
   the one-sided version, slightly larger errors in $B_1$ than in $B_2$
   (stated, no data). Both rounds are divergence-free in the cell and
   conservative, so the average is too.

**Discrete divergence.** The Powell term is discretized upwind with the
HLL wave speeds, after Wu & Shu (2019, as recalled; Eqs. (3), (32)). The
resulting discrete divergence splits into an interior term, the integral of
$\nabla\cdot B^{\mathrm R}$ over the cell, which vanishes for a locally
divergence-free reconstruction when the edge quadrature is exact
($2N_g-1\ge k$, $N_g$ Gauss points per edge, Eq. (34)), and a term of
normal-field jumps across the edges (Eqs. (33), (35)). The same reduction
to normal-field jumps is what Wu & Shu's DG analysis uses (Eq. (6.19)).
Because the interior term is not zero in floating point and "may lead to a
failed simulation", the code omits it and evaluates only the jump term,
which is also the divergence diagnostic (§3.3.3); the remaining jumps are
"globally controlled by the Godunov–Powell source term". On the rotor the
divergence norm is "controlled below $10^{-3}$" for linear and quadratic
reconstruction at $200^2$ cells and for linear at $600^2$ (§4.3, Fig. 12). The authors stress
that local is not global: a globally divergence-free scheme would also make
the normal component continuous, so that the Powell term vanishes (§5).

## Constrained transport

**Unstaggered central scheme.** [Kanbar, Touma & Klingenberg (2022)](/sources/kanbar-2022.md)
(§4, Eqs. (18)–(21)) correct the magnetic field of their
[unstaggered central scheme](/methods/unstaggered-central-scheme.md) at the
end of each step, after Touma's constrained-transport method (CTM). With
$\Omega=-v_1B_2+v_2B_1$ (page-local) the 2D induction equation is
$\partial_t(B_1,B_2)-\partial_x(0,\Omega)+\partial_y(\Omega,0)=0$; the field
on the dual (staggered) nodes is re-updated with centred differences of
$\Omega^{n+1/2}$, the time average of $\Omega$ at the dual node, and averaged
back to the primary nodes. If the centred divergence
$$\nabla\cdot B^n_{i,j}=\frac{B^n_{1,i+1,j}-B^n_{1,i-1,j}}{2\Delta x}+\frac{B^n_{2,i,j+1}-B^n_{2,i,j-1}}{2\Delta y}$$
vanishes at every primary node, the divergence on the dual nodes is the
average of four such values and vanishes, and so does the divergence at the
primary nodes after averaging back (Eqs. (20)–(21); the substitution is
sketched, not written out). This is the same centred, $2\Delta$-wide
discrete divergence that appears in Wu & Shu's Thm 6.1 above *(compiler
check, not in the sources: the two printed formulas coincide)*. Numerically
(§5): on a four-state MHD Riemann problem ($400^2$, $t=0.8$) the divergence
is of order $10^{-14}$ with CTM and of order one without, with visually
alike densities (Figs. 4–5); in a magnetized stratified atmosphere it is
clearly nonzero without CTM and zero "up to machine precision" with it
(Figs. 10–11); CTM adds "a small smearing out effect" on the Brio–Wu tube
(Fig. 3). The authors apply CTM "whenever needed" and give no criterion
(§6).

**TENO-A with unstaggered constrained transport.**
[Fu (2023)](/sources/fu-2023.md) reviews TENO-A for MHD with unstaggered
constrained transport (§5.3, recalled from earlier work): in 1D the cost of
TENO5-A is similar to WENO5-JS and WENO5-Z, and even the eight-point TENO8-A
adds a "negligible" cost; Orszag–Tang results at $200^2$ are compared with a
WENO5-JS reference at $512^2$ (Fig. 19). The review gives no formulas for
the transport step.

**Reference solutions.** [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md)
compare their GLM-MHD DG results on the
[Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) with the
second-order constrained-transport code Athena at $1024^2$ and $2048^2$
(§6.2, Figs. 9–10).

## Divergence cleaning (GLM-MHD)

GLM-MHD adds a field $\psi_{\mathrm{GLM}}$ that transports divergence
errors away at a cleaning speed $c_h$; $\nabla\cdot B=0$ is not enforced
exactly. Both GLM sources recompute $c_h$ every step as the largest value
compatible with the CFL condition
([Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md), §6;
[Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md), §5.3, Eqs.
(51)–(52)). They differ in the form of the equations:

- Rueda-Ramírez et al. (2021) keep the **non-conservative** Powell and GLM
  terms, which the entropy analysis needs, discretize them with two-point
  volume and surface terms in the DGSEM and by central differences of
  interface means in the subcell finite volumes, and prove entropy
  stability of the element-wise blend (§3; see
  [subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md)).
- Rueda-Ramírez et al. (2022) solve the **conservative** form, although the
  non-conservative form is needed to prove entropy stability, because the
  conservative form fits their subcell-wise limiting framework (§5.3). On
  the Orszag–Tang vortex ($N=3$, $256^2$ elements, $t=1$) subcell-wise
  density limiting with second-order subcell finite volumes limits less and
  develops more turbulent structure than with first-order ones (§5.3.1).

The two choices are compatible *(compiler remark, not in the sources)*: the
earlier paper shows that element-wise blending can carry the
non-conservative terms with an entropy proof, the later one trades them
for subcell-wise blending, for which the entropy proof is "still missing"
(Rueda-Ramírez et al. 2022, §4 item (2)).

## Qualifications

- The Godunov-symmetrization source is non-conservative; Wu & Shu do not
  discuss the resulting conservation error. The source vanishes only where
  the normal field is continuous.
- The extension of Thm 6.4 to SSP time stepping requires the point-value
  hypothesis and the locally divergence-free property at every stage; it is
  stated without a stage-wise argument (§6.2).
- arXiv v1 of Wu & Shu prints the jump coefficient of $\varepsilon_B$ with
  $(\rho^\pm)^{1/2}$ where a Cauchy–Schwarz and AM–GM bound of Eq. (6.21)
  gives $(\rho^\pm)^{-1/2}$ *(compiler check, not in the sources; worked out
  on [geometric quasilinearization](/methods/geometric-quasilinearization.md))*;
  the version of record should decide.
- Liu et al. place their scheme in Wu & Shu's provably positivity-preserving
  framework, but the implemented scheme drops the interior divergence term
  and the paper prints no CFL number, so the guarantee is not established
  for the code; a degree-2 run of the Mach 800 jet fails with negative
  pressure unless the SVD truncation of the least-squares solve is loosened
  (§3.3.3, §4.5).
- Kanbar et al.'s CTM preserves the centred discrete divergence at the
  nodes, not a face-centred divergence *(compiler remark, not in the
  sources)*, and only in the steps where it is applied; it is applied "whenever needed" without a stated criterion.

# Citations

- [Wu & Shu (2023)](/sources/wu-2023-b.md) — arXiv v1: §6 (Eqs. (6.3)–(6.5), (6.17)–(6.22); Thms 6.1, 6.2, 6.4; Rem. 6.3); §7 (Ex. 7.1–7.2, Figs. 5–6).
- [Liu et al. (2021)](/sources/liu-2021.md) — Eq. (1); §3.1–§3.2 (Eqs. (15)–(26)); §3.3.3 (Eqs. (32)–(35)); §4.3 (Fig. 12); §4.5; §5.
- [Kanbar, Touma & Klingenberg (2022)](/sources/kanbar-2022.md) — arXiv v1: §4 (Eqs. (18)–(21)); §5.1–§5.2, §5.5 (Figs. 3–5, 10–11); §6.
- [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) — arXiv v1: §2.2 (Eqs. (13)–(15), (21)–(22)); §3; §6; §6.2 (Figs. 9–10).
- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — arXiv v2: §5.3 (Eqs. (51)–(52)); §5.3.1 (Figs. 10–11).
- [Fu (2023)](/sources/fu-2023.md) — §5.3, Fig. 19.
