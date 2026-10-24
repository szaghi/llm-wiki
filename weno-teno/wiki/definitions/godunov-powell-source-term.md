---
type: Definition
title: "Godunov–Powell source term"
description: "The non-conservative term proportional to div B that Godunov and Powell add to ideal MHD: it makes the system symmetrizable by the entropy variables and lets bound-preserving and entropy-stable schemes tolerate divergence errors. The page gives the term, its entropy structure, its interface-jump discretizations and its cost in conservation."
status: established
aliases: [Powell source term, Godunov source term, eight-wave source, Godunov symmetrization source, symmetrizable MHD, Godunov–Powell modified system, upwind discrete Godunov–Powell source]
tags: [mhd, entropy-stable, positivity, dg, finite-volume]
timestamp: 2026-10-23T20:43:00Z
---

# Godunov–Powell source term

Ideal MHD in conservative form, $\partial_tu+\nabla\cdot f(u)=0$ with
$u=(\rho,\rho v,B,E)$, carries the involution $\nabla\cdot B=0$ but does
not use it. The **Godunov–Powell modified system** adds a term proportional
to the divergence,
$$\partial_tu+\nabla\cdot f(u)=-(\nabla\cdot B)\,S_B(u),\qquad S_B(u)=(0,\ B,\ v,\ v\cdot B)^\top,$$
in the ordering $(\rho,\rho v,B,E)$ ($S_B$ page-local, as on the
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
page; in the ordering $(\rho,\rho v,E,B)$ the vector reads
$(0,B,v\cdot B,v)$). The two systems coincide when $\nabla\cdot B=0$, and
the modified one differs from the conservative one only through divergence
errors. [Ding & Wu (2024a)](/sources/ding-2024.md) (§1, Eq. (3)),
[Liu & Wu (2025)](/sources/liu-2025.md) (§3, Eq. (37)) and
[Liu et al. (2025b)](/sources/liu-2025-b.md) (§2, Eq. (2.7)) write this
form and attribute it to Godunov (symmetrization) and Powell (eight-wave
schemes); [Wu & Shu (2023)](/sources/wu-2023-b.md) (§6.2) call it the
Godunov symmetrization, [Liu et al. (2021)](/sources/liu-2021.md) (Eq. (1))
cite Powell et al., and [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md)
carry the same vector as the Powell part of resistive GLM-MHD (§2.2,
Eqs. (13)–(15)). The term is load-bearing in two ways: it is what makes the
thermodynamic entropy a symmetrizer, and it is what lets a
bound-preserving proof absorb a nonzero discrete divergence.

## Entropy structure

With the registry entropy $\eta=-\rho s/(\gamma-1)$, $s=\ln(p\rho^{-\gamma})$,
the entropy variables of ideal MHD are
$$w=\eta'(u)^\top=\Big(\frac{\gamma-s}{\gamma-1}-\frac{\rho\lvert v\rvert^2}{2p},\ \frac{\rho v}{p},\ \frac{\rho B}{p},\ -\frac{\rho}{p}\Big)^\top$$
(Liu et al. 2025b, §2, written with $\beta=\rho/(2p)$; Liu et al. 2025c,
§2, in the ordering with $E$ before $B$). The conservative system "can
hardly be symmetrized" (Liu et al. 2025b, §2): Godunov's observation, as
recalled by [Liu et al. (2025c)](/sources/liu-2025-c.md) (§2), is that ideal
MHD with the divergence constraint is not symmetrizable. The source vector
is the gradient in $w$ of a function homogeneous of degree one,
$$S_B=\phi_{\mathrm G}'(w),\qquad \phi_{\mathrm G}(w)=-\frac{w_2w_5+w_3w_6+w_4w_7}{w_8}=\frac{\rho\,(v\cdot B)}{p},\qquad w\cdot\phi_{\mathrm G}'(w)=\phi_{\mathrm G}(w)$$
($\phi_{\mathrm G}$ page-local; the sources' $\phi(\mathbf V)=2\beta\,\mathbf u\cdot\mathbf B$;
Liu et al. 2025b, Eq. (2.9); Liu et al. 2025c, Eq. (7)). With it the
modified system takes the symmetric form
$\varphi''(w)\partial_tw+\sum_d\big(\psi_d''(w)-\phi_{\mathrm G}''(w)^\top B_d\big)\partial_{x_d}w=0$,
first matrix symmetric positive definite, second symmetric (Liu et al.
2025b, §2; $\varphi=\rho+\rho\lvert B\rvert^2/(2p)$ the entropy potential and
$\psi_d=\rho v_d+\rho v_d\lvert B\rvert^2/(2p)$ the potential flux in their
convention, which includes the term $\phi_{\mathrm G}B_d$). Liu et al. (2025c)
also print the entropy balance of the physical entropy, which carries
$(\gamma-1)\,\rho(v\cdot B)\,(\nabla\cdot B)/p$ (§2).

**Modified Tadmor condition.** An entropy-conservative two-point flux for
the 1D modified system must satisfy
$$[\![w]\!]\cdot f^{\mathrm{ec}}+[\![\phi_{\mathrm G}]\!]\,\{\!\{B_1\}\!\}=[\![\psi]\!]$$
(Liu et al. 2025b, Def. 3.1, Eq. (3.12), with their $\psi$ above), and an
entropy-stable flux the same with $\le$ (Def. 3.2). The
Chandrashekar–Klingenberg flux with logarithmic means of $\rho$ and
$\rho/(2p)$ satisfies it (Liu et al. 2025b, §3.1; Liu et al. 2025c,
App. A.1; [logarithmic mean](/operators/logarithmic-mean.md),
[entropy-conservative flux](/methods/entropy-conservative-flux.md)).
Liu et al. (2025c) print the condition as
$[\![w]\!]\cdot f^{\mathrm{ec}}=[\![\psi]\!]-[\![\phi_{\mathrm G}]\!]\,\{\!\{B_1\}\!\}$
(Def. 2, Eq. (9)), with the potential defined in their §2, for a
symmetrizable system, as $\psi=w\cdot f-F_\eta$, without the term
$\phi_{\mathrm G}B_1$ that Liu et al. (2025b) include; the two papers thus
define the potential differently, and the page does not reconcile them. Rueda-Ramírez et al. (2021)
state that the Powell terms, with a GLM term required by Galilean
invariance, are needed for the continuous entropy analysis of GLM-MHD
(§2.2); [Dzanic & Witherden (2023)](/sources/dzanic-2023.md) state, after
Wu & Shu, that only the Powell-modified system is symmetrizable and
Galilean invariant for a field that is not exactly solenoidal (§2.3).

**Relativistic analogues.** For special relativistic MHD the symmetrizing
source has a different vector: [Duan & Tang (2022)](/sources/duan-2022.md)
use $-\Phi'(w)^\top\sum_d\partial_{x_d}B_d$ with $\Phi=\rho W(v\cdot B)/p$,
and [Ding & Wu (2024b)](/sources/ding-2024-b.md) the vector
$\big(0,(1-\lvert v\rvert^2)B+(v\cdot B)v,v,v\cdot B\big)$ in the ordering
$(D,m,B,E)$; both are on the
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
page ([relativistic hydrodynamics](/definitions/relativistic-hydrodynamics.md)).

## Why the term matters for bound preservation

[Wu & Shu (2023)](/sources/wu-2023-b.md) (§6) show by
[geometric quasilinearization](/methods/geometric-quasilinearization.md)
that the pressure constraint of a conservative cell-average update is
violated, for some auxiliary states, by a term
$-\Delta t\,(v_*\cdot B_*)\,\mathrm{div}_{ij}B$, so that
[bound preservation](/properties/bound-preservation.md) needs a discrete
divergence-free condition that standard schemes do not keep. Ding & Wu
(2024a) recall (§1) that exact smooth solutions of the conservative system
can lose positivity when $\nabla\cdot B=0$ is slightly violated, while
those of the modified system are always positivity-preserving (from Wu &
Shu's earlier work, as recalled). Liu & Wu (2025) restate it as: adding the
source "removes the effect of divergence errors" on positivity (§3). In
every proof below, the discretized source produces a divergence term of
opposite sign to the flux's, and the two cancel once the in-cell part of
the field is divergence-free.

## Discretizations

All the discretizations in the bundle drop or cancel the cell-interior
divergence and keep only the **jumps of the normal field** across
interfaces, which a field that is divergence-free inside each cell leaves
as the whole discrete divergence. Let $[\![B_1]\!]^\mu_{i+1/2}$ be the jump
of $B_1$ at the face quadrature point $\mu$ (page-local index $\mu$, face
weights $\mathsf w_\mu$ normalized to sum one).

| Source | Scheme | Interface source | Where added |
|---|---|---|---|
| [Wu & Shu (2023)](/sources/wu-2023-b.md) §6.2, Eq. (6.22) | locally divergence-free DG, multicomponent MHD | normal-field jumps at the interface Gauss points | cell averages, CFL penalty $\varepsilon_B$ proportional to the jumps |
| [Liu et al. (2021)](/sources/liu-2021.md) §3.3.3, Eqs. (32)–(35) | finite-volume [WLS-ENO](/methods/wls-eno.md), locally divergence-free | HLL-upwind split of the jumps (after Wu & Shu 2019, as recalled); interior term omitted in the code | cell averages |
| [Liu, Feng & Wang (2023a)](/sources/liu-2023.md) §3.2.2, Eqs. (67)–(70) | one-step HLL [generalized Riemann problem](/methods/generalized-riemann-problem.md) | the same jumps, evaluated at $t^n+\Delta t/2$ | cell averages; the edge Riemann problem is posed without the source |
| [Ding & Wu (2024a)](/sources/ding-2024.md) Eq. (12) | finite-volume WENO with a discretely divergence-free projection | $\tfrac12[\![B_1]\!]^\mu S_B(\{\!\{u\}\!\}^\mu)$ on each face, central | cell averages |
| [Liu & Wu (2025)](/sources/liu-2025.md) §3.2, Eqs. (45)–(49) | locally divergence-free [OEDG](/methods/oedg.md) | wave-speed-weighted split of the jump, $S_B$ of each cell's own trace | cell averages only |
| [Liu et al. (2025b)](/sources/liu-2025-b.md) §3.1, Eqs. (3.2), (3.10)–(3.11) | nodal entropy-stable DG | half jump at each face, plus the volume term $\sum_lD_{il}B_1^l\,S_B^i$ | every node |
| [Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) §5.3, Eq. (48); [Dzanic & Witherden (2023)](/sources/dzanic-2023.md) §2.3, Eqs. (17)–(19) | flux reconstruction, nodal DG | corrected (global) divergence with centred common interface values | every solution point |

**Central jump source** (Ding & Wu 2024a, Eq. (12)):
$$S_{ij}=-\frac1{\Delta x}\sum_\mu\mathsf w_\mu\Big(\tfrac12[\![B_1]\!]^\mu_{i+1/2}S_B(\{\!\{u\}\!\}^\mu_{i+1/2})+\tfrac12[\![B_1]\!]^\mu_{i-1/2}S_B(\{\!\{u\}\!\}^\mu_{i-1/2})\Big)-\frac1{\Delta y}\big(\cdots\big)_y,$$
with $\{\!\{u\}\!\}$ the mean of the two traces. The interior divergence is
absent because their discretely divergence-free condition makes it zero;
the authors call the form new and its CFL condition milder than Wu & Shu's
(§2.1; no side-by-side constant).

**Upwind jump source** (Liu & Wu 2025, Eqs. (45)–(47)). At the face
$x_{i+1/2}$, with the HLL speeds $s^-\le0\le s^+$ of the face flux, the
jump is split into the part charged to the left cell and the part charged
to the right one,
$$\mathscr B^-_{i+1/2}=\frac{-s^-}{s^+-s^-}[\![B_1]\!]_{i+1/2},\qquad \mathscr B^+_{i+1/2}=\frac{s^+}{s^+-s^-}[\![B_1]\!]_{i+1/2},\qquad \mathscr B^-+\mathscr B^+=[\![B_1]\!]$$
($\mathscr B^\pm$ page-local, the sources' $\mathscr B^\pm_1$ written in
registry speeds *(compiler check, not in the sources: the printed weights
are $\pm V^\pm/(V^+-V^-)$ with $V^\mp$ the clipped HLL speeds)*), and the
cell average of $I_i$ receives
$-\frac1{\Delta x}\sum_\mu\mathsf w_\mu\big[\mathscr B^-_{i+1/2}S_B(u^-_{i+1/2})+\mathscr B^+_{i-1/2}S_B(u^+_{i-1/2})\big]$
plus the $y$ analogue. If all waves go left ($s^+=0$) the whole jump is
charged to the left cell; if all go right, to the right one (Fig. 2). They
derive the form from the weak divergence of a locally divergence-free
field, concentrated on an interface strip of vanishing width (Eqs.
(48)–(49), Fig. 1), and add it only to the cell-average equations,
because weak positivity involves only the averages; the higher moments
evolve with the unmodified scheme (§1, §3.2).

**Nodal entropy-stable form** (Liu et al. 2025b, §3.1). The
non-conservative product is discretized as in DG for Hamilton–Jacobi
equations (after Cheng and Shu, as recalled): a volume term
$\big(\sum_lD_{il}B_1^l\big)S_B(u^i)$ at each Gauss–Lobatto node $i$ and an
interface correction $\tfrac12S_B(u^\mp)[\![B_1]\!]$ at the two end nodes
(Eqs. (3.2), (3.10)); with an entropy-conservative volume flux of the
modified Tadmor condition and an entropy-stable interface flux, the
scheme is entropy stable (Thm 3.1, recalled from their earlier nodal
scheme), and stays so with their oscillation-damping term (Thm 3.2,
[entropy stability](/properties/entropy-stability.md)).

## Bound-preserving proofs with the source

- **Liu & Wu (2025), Theorem 1** (§3.6). For locally divergence-free OEDG
  with a positivity-preserving HLL flux (Wu–Shu speed bounds), if the
  limited solution is admissible at the nodes of a cell-average
  decomposition, the cell averages stay in $G$ under the CFL condition
  (66), whose denominators add $\lvert\mathscr B^\mp\rvert/\sqrt{\rho^\mp}$ to
  the wave speeds. In the proof the $v_*\cdot B_*$ terms of the flux sum
  to $-\Delta t\,(v_*\cdot B_*)$ times the Gauss-quadrature divergence of the
  limited field, which equals the cell integral of $\nabla\cdot B$ and
  vanishes for a locally divergence-free field; the jump terms of the flux
  cancel against those of the source through the upwind split. With the
  [optimal cell-average decomposition](/methods/optimal-cell-average-decomposition.md)
  for $\mathbb P^2$ and $\mathbb P^3$ the bound is
  $\Delta t\le\Delta x\Delta y/\max\{6a^{(1)}\Delta y+2a^{(2)}\Delta x,\ 6a^{(2)}\Delta x+2a^{(1)}\Delta y\}$
  (Corollary 2), against $\Delta t\,(a^{(1)}/\Delta x+a^{(2)}/\Delta y)\le1/(N_{\mathrm{GL}}(N_{\mathrm{GL}}-1))$
  for the Zhang–Shu decomposition (Corollary 1, $N_{\mathrm{GL}}=\lceil(N+3)/2\rceil$).
  They state that their two-state inequalities simplify and improve Wu &
  Shu's general-mesh estimates on Cartesian meshes (§1, Remark 3).
- **Ding & Wu (2024a), Theorem 2.1.** With the central source, the
  divergence remainder of the proof is
  $\Delta t\,(v_*\cdot B_*)\big(\tfrac12\widehat{[\![B]\!]}_{ij}-\nabla_h\cdot\{\!\{B\}\!\}_{ij}\big)=-\Delta t\,(v_*\cdot B_*)\nabla_h\cdot B_{ij}$,
  which their projection makes zero (§3.2).
- **Wu & Shu (2023), Thm 6.4**, with the CFL penalty $\varepsilon_B$, and
  **Ding & Wu (2024b)** for central DG on overlapping meshes; details on
  [divergence-free magnetic field](/properties/divergence-free-magnetic-field.md).

**Evidence that the source is needed.** Liu & Wu (2025) report that on
the shock–cloud interaction removing the source gives negative cell-average
pressure, and that on Mach 800 and Mach 10000 magnetized jets disabling the
upwind source, the oscillation-eliminating step or the limiter makes "the
code immediately fail" (§4.2.4, §4.2.6; stated, no failure figure). Wu &
Shu (2023) state the same for their two-species jet (§7), and Ding & Wu
(2024b) for Mach 50 relativistic jets (Ex. 5.9)
([high-Mach jets](/benchmarks/high-mach-astrophysical-jet.md)). Liu et al.
(2025b) run the same Mach 800 and Mach 10000 jets with their nodal
entropy-stable scheme, the source in the nodal form above and only the
Zhang–Shu limiter, at CFL $0.2/(2N+1)$, and read the contrast with Liu &
Wu as evidence of robustness (Ex. 10); their scheme is not locally
divergence-free and its positivity is not proved (Remark 3.1).

## Cost: conservation

The source is non-conservative in every component where $S_B$ is nonzero:
momentum, magnetic field and energy: Liu et al. (2025c) state that schemes
of the modified system that do not keep the divergence-free property "can
ensure the mass conservation but may fail to conserve other quantities,
including the momentum, total energy, and magnetic field" (§3). Liu et al. (2025b) state that their scheme is non-conservative
because of the Godunov term and that a DG method at once conservative,
globally divergence-free, entropy stable and positivity-preserving
"remains open" (Remark 3.2). Liu et al. (2025c) argue against
entropy-stable schemes of the modified system (§1, §3): since they do not
satisfy the divergence constraint discretely, they are "inherently
nonconservative", which "can lead to numerical instability and nonphysical
features". Their alternative discretizes the **conservative** form with
a nodal field that is divergence-free at every Gauss–Lobatto node and
normal-continuous across faces (Def. 4, Eqs. (11)–(12)); under these two
conditions the contributions of $\phi_{\mathrm G}$ cancel exactly (the face
terms by continuity, the volume terms by the nodal divergence) and the
conservative scheme is entropy conservative in each element and entropy
stable globally (Thm 1, App. B). The field is supplied by
[constrained transport](/methods/constrained-transport.md) of face
polynomials and a least-squares reconstruction; the energy correction
that keeps the pressure unchanged after the reconstruction costs local
energy conservation (Remarks 1–2, §4.2). Dzanic & Witherden (2023) recall, after Tóth, that
the non-conservative form can be inaccurate near discontinuities (§2.3,
not tested).

## Qualifications

- The upwind and central jump forms are not compared on the same scheme
  in any source; Ding & Wu's "milder CFL" and Liu & Wu's "notably
  improved" CFL are each relative to Wu & Shu's earlier estimates.
- Liu & Wu (2025) print the split as an "un-wind" discretization
  (§3.2, a typo for upwind) and refer at the end of Remark 3 to "our above
  PP CFL condition (2)", where (2) is the divergence constraint; the
  intended condition is that of Corollary 2.
- Liu et al. (2021) evaluate only the jump term because the interior term
  is not zero in floating point; with it omitted, Wu & Shu's guarantee is
  not established for their code (see
  [divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)).
- The conservation error of the source is not quantified by any source of
  the bundle.

# Citations

- [Liu & Wu (2025)](/sources/liu-2025.md) — arXiv v2: §1; §3, Eqs. (36)–(37); §3.1, Eqs. (38)–(44); §3.2, Eqs. (45)–(49), Figs. 1–2; §3.6, Theorem 1, Lemmas 1–4, Eq. (66); Corollaries 1–2, Remark 3; §4.2.4, §4.2.6.
- [Liu et al. (2025b)](/sources/liu-2025-b.md) — §2, Eqs. (2.7)–(2.9); §3.1, Eqs. (3.2), (3.10)–(3.14), Defs. 3.1–3.2, Thm 3.1; §3.2, Thm 3.2; Remarks 3.1–3.2; Ex. 10.
- [Liu et al. (2025c)](/sources/liu-2025-c.md) — §1; §2, Eqs. (6)–(7); §3, Def. 2, Eq. (9); §3.1, Def. 4, Eqs. (11)–(12), Thm 1; App. A.1, App. B.
- [Ding & Wu (2024a)](/sources/ding-2024.md) — arXiv v1: §1; §2.1, Eqs. (3), (6)–(16), Thm 2.1; §3.2.
- [Wu & Shu (2023)](/sources/wu-2023-b.md) — arXiv v1: §6.2, Eqs. (6.17)–(6.22), Thm 6.4; §7.
- [Liu et al. (2021)](/sources/liu-2021.md) — Eq. (1); §3.3.3, Eqs. (32)–(35).
- [Liu, Feng & Wang (2023a)](/sources/liu-2023.md) — §3.1.3; §3.2.2, Eqs. (67)–(70).
- [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) — arXiv v1: §2.2, Eqs. (13)–(15), (21)–(22).
- [Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) — arXiv v2: §5.3, Eq. (48).
- [Dzanic & Witherden (2023)](/sources/dzanic-2023.md) — arXiv v2: §2.3, Eqs. (17)–(19).
- [Duan & Tang (2022)](/sources/duan-2022.md) — arXiv v1: §2, Eqs. (2.4)–(2.5).
- [Ding & Wu (2024b)](/sources/ding-2024-b.md) — Eq. (7); §4.4, Thm 4.1; Ex. 5.9.
