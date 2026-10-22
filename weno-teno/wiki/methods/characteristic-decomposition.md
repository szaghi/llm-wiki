---
type: Method
title: "Characteristic decomposition"
description: "Local characteristic decomposition projects stencil data onto the eigenvectors of the flux Jacobian at an interface state, reconstructs each field separately and projects back; WENO, TENO and central-upwind schemes use it against oscillations, multiphase sources project primitive variables at material interfaces, entropy-stable schemes scale the eigenvectors, and some schemes do without it."
status: established
aliases: [local characteristic decomposition, LCD, characteristic-wise reconstruction, characteristic projection, reconstruction in characteristic variables, primitive-variable reconstruction]
tags: [characteristic, reconstruction, weno, teno, central-scheme, multiphase]
timestamp: 2026-10-22T20:00:00Z
---

# Characteristic decomposition

For a system $\partial_tu+\partial_xf(u)=0$, $u\in\mathbb R^m$, a nonlinear reconstruction
applied component by component to the conserved variables couples the fields at a
discontinuity and produces oscillations. Local characteristic decomposition freezes the
Jacobian at an interface: with $R_{i+1/2}$, $L_{i+1/2}=R_{i+1/2}^{-1}$ the right- and
left-eigenvector matrices of $A$ at an average of the two neighbouring states, every datum of
the stencil is projected, $\zeta_k=L_{i+1/2}u_k$ (page-local symbol), the scalar
reconstruction is applied to each of the $m$ fields, and the result is projected back with
$R_{i+1/2}$. The same matrix is used for all stencil points of one interface, so the
projection is linear and exactly invertible.

## Finite-difference and finite-volume algorithms

[Fu (2023)](/sources/fu-2023.md) gives both algorithms for TENO (§3.4 Algorithm 1, §3.6
Algorithm 2), and they are the ones used, with WENO in place of TENO, across the
finite-difference papers of this bundle.

- **Finite difference** (Algorithm 1): at $x_{i+1/2}$, with Roe-average eigenvectors, project
  the point values and point fluxes of the $K$-point stencil,
  $\zeta_k=L_{i+1/2}u_k$, $g_k=L_{i+1/2}f(u_k)$ (page-local $g_k$); split each field by
  [Lax–Friedrichs](/methods/lax-friedrichs-flux.md),
  $g^{(l)\pm}=\tfrac12\big(g^{(l)}\pm a^{(l)}\zeta^{(l)}\big)$, with $a^{(l)}$ the maximum
  $l$-th characteristic speed over the whole domain; reconstruct $\hat g^{(l)\pm}_{i+1/2}$;
  sum, and return $\hat f_{i+1/2}=R_{i+1/2}\hat g_{i+1/2}$.
- **Finite volume** (Algorithm 2): project the cell averages with Roe-average eigenvectors,
  reconstruct $u^\mp_{i+1/2}$ in characteristic space, project back, then call a Riemann
  solver; conservative variables are reconstructed in characteristic space "towards better
  oscillation suppressing".

Users of the finite-difference algorithm with Lax–Friedrichs splitting (the averaged state is
listed below): [Fu (2021)](/sources/fu-2021.md) (§5; Rusanov splitting, LLF for extreme
cases), [Li et al. (2022)](/sources/li-2022-b.md) ("global Lax–Friedrichs flux splitting with
local characteristic fields", with Eq. (38)), [Luo & Wu (2021)](/sources/luo-2021-b.md) (§5),
[Takagi et al. (2022)](/sources/takagi-2022.md) (§4, where THINC is applied per characteristic
component and per split-flux direction), [Wang & Don (2022)](/sources/wang-2022-b.md)
(§3.3, well-balanced shallow-water WENO) and
[Wang et al. (2021)](/sources/wang-2021.md) (§3.1, Remark 1, for their
[multi-resolution WENO](/methods/multi-resolution-weno.md)).
[Wang et al. (2023)](/sources/wang-2023-b.md) apply it to the WENO-Z *interpolation* of
point values in [A-WENO](/methods/alternative-weno.md) (§2). [Browne et al. (2022)](/sources/browne-2022.md) use the
finite-difference algorithm with Rusanov splitting for fifth-order WENO on disturbance fluxes,
the characteristic transform being applied "to improve the shock capturing characteristics"
(§2.2); [Bezgin et al. (2022)](/sources/bezgin-2022.md) use the finite-volume algorithm with the
local Lax–Friedrichs flux for their learned three-point WENO (§2, §4).

## Variants of the frozen state and of where the projection acts

- **Averaged state.** Roe averages in [Fu (2023)](/sources/fu-2023.md),
  [Fu (2021)](/sources/fu-2021.md), [Luo & Wu (2021)](/sources/luo-2021-b.md),
  [Takagi et al. (2022)](/sources/takagi-2022.md) and [Wang & Don (2022)](/sources/wang-2022-b.md);
  an arithmetic average of primitive variables (with $E$ and $H$ derived from it) in
  [Chertock et al. (2023)](/sources/chertock-2023.md) (Apps. A–B), which state that
  $\hat u_{i+1/2}=\tfrac12(\bar u_i+\bar u_{i+1})$ "or another type of average" may be used
  (§2.1).
- **Per zone instead of per interface.** [Balsara et al. (2024)](/sources/balsara-2024.md)
  reconstruct once per zone, in the characteristic variables of zone $i$, obtaining both
  $u^-_{i+1/2}$ and $u^+_{i-1/2}$ from one projection (§VI, steps 2–3); this is what lets
  their [fluctuation-form scheme](/methods/fluctuation-form-fd-weno.md) use one
  reconstruction per zone instead of two.
- **Non-conservative systems.** [Chu et al. (2022)](/sources/chu-2022.md) (Remarks 6.2–6.3)
  project with the eigenvectors of $A(\hat u_{i+1/2})+\mathcal C(\hat u_{i+1/2})$ (in this
  bundle's sign; their $A-B$), the quasilinear matrix of the two-layer shallow-water system
  including its non-conservative products, at Roe averages of the layer depths and velocities;
  $R$ and $L$ are computed numerically and applied to the six values $u_{i-2},\dots,u_{i+3}$ of
  the fifth-order WENO-Z interpolation. They recall that componentwise WENO-Z interpolation may
  oscillate (Remark 3.1) and credit the decomposition with "substantially less oscillatory
  behavior" than an earlier second-order central-upwind computation (§7.2, Ex. 7;
  [path-conservative schemes](/methods/path-conservative-scheme.md)).
- **Several directions per cell on unstructured meshes.** On triangles,
  [Chen & Wu (2022)](/sources/chen-2022-b.md) (§3.2.2, Eq. (38)) project the stencil averages onto
  the eigenvectors of the normal Jacobian for each of the three edge normals of the target cell,
  evaluated at the cell average through the recovered primitive state, reconstruct in each
  frame, project back, and average the three polynomials with weights $\lvert K_j\rvert$, the
  areas of the three neighbours in the paper's notation for cell areas (§2.2). The resulting
  operator stays homogeneous of degree one, $R_h(\sigma u)=\sigma R_h(u)$ for $\sigma>0$, because the
  eigenvector matrices are invariant under $u\mapsto\sigma u$ (Lemma 3.2;
  [scale invariance](/properties/scale-invariance.md)).
- **Fewer projections in a DG limiter.** In the simple WENO limiter for DG on triangles,
  [Du, Shu & Zhong (2022)](/sources/du-2022.md) (§3.1, Eqs. (3.1)–(3.8)) use, for each edge
  normal $\mathbf n_l$, the Jacobian $A_l=n_{l,x}\partial f/\partial u+n_{l,y}\partial g/\partial u$ at the
  target-cell average, and project **two** polynomial vectors — the target cell's and the
  neighbour's across edge $l$, shifted to the target average — instead of all four as in the
  original limiter of Zhu, Zhong, Shu and Qiu; the directional results are averaged with weights
  $\lvert K_l\rvert$, the neighbour areas. On polygonal meshes from point clouds the count drops from
  $N_j+1$ (the number of neighbours plus one) to two, with the direction taken from cell centre to
  neighbour centre (§3.2). Accuracy is kept under heavy over-flagging, and CPU time falls by
  about 6–55 % on shocked problems (§4, Tables 4.7–4.10, 4.17–4.18); the sharper double-Mach stem
  is attributed by the authors to "less information being used for reconstruction in each
  direction", a cause not isolated by their runs. See
  [WENO limiters for DG](/methods/weno-limiter-dg.md).
- **In the numerical diffusion, not only in the reconstruction.**
  [Chertock et al. (2023)](/sources/chertock-2023.md) use the projection also to give each
  field its own central-upwind diffusion, the
  [LCD central-upwind scheme](/methods/lcd-central-upwind-scheme.md) (§3).
- **Entropy-scaled eigenvectors in the dissipation.** In the entropy-stable
  moving-mesh finite-difference scheme of [Li, Duan & Tang (2022)](/sources/li-2022-c.md)
  (§3.4, Eqs. (3.21)–(3.22)) the dissipation acts on jumps of the reconstructed
  scaled entropy variables, with right-eigenvector matrices scaled so that
  $\partial u/\partial w=RR^\top$ ($w$ the entropy variables). They print these
  matrices for the single- and two-component Euler equations with the
  [stiffened-gas equation of state](/definitions/stiffened-gas-equation-of-state.md),
  evaluated at interface averages built from logarithmic means, and rotate the
  directional flux to the face normal. [Duan & Tang (2022)](/sources/duan-2022.md) (§4,
  Eq. (4.1)) use the same construction for relativistic (magneto)hydrodynamics on moving
  curvilinear meshes: fifth-order Jiang–Shu WENO acts on the rotated, scaled entropy variables
  $R^\top T\,w$ ($T$ the page-local rotation to the face normal), and the dissipation matrix is a
  scalar maximal speed times $T^{-1}R$, a Rusanov-type magnitude rather than a field-by-field
  $\lvert\Lambda\rvert$. See [TeCNO schemes](/methods/tecno-scheme.md)
  and [entropy-conservative fluxes](/methods/entropy-conservative-flux.md).

For the Euler equations, [Chertock et al. (2023)](/sources/chertock-2023.md) (App. A) print,
at the averaged state with velocity $v$, sound speed $c$ and enthalpy $H$,

$$R_{i+1/2}=\begin{pmatrix}1&1&1\\ v-c&v&v+c\\ H-vc&\tfrac12v^2&H+vc\end{pmatrix},$$

and its inverse with $2H-v^2=2c^2/(\gamma-1)$; App. B gives the 2D version.

## Primitive variables at material interfaces

At a material interface the density and the equation-of-state parameters jump
while velocity and pressure are continuous. The multiphase sources agree that
reconstructing **conservative** variables there makes velocity and pressure
oscillate, and that the projection must therefore act on primitive variables:

- [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) (§2.2, §4.1, §5.5) let
  [MFC](/software/mfc.md) reconstruct primitive, conservative or characteristic
  variables, with primitive as the default; recalling Coralic & Colonius, they
  state that conservative reconstruction at an advected air–water interface
  gives spurious oscillations and "even negative pressures", primitive
  reconstruction none to round-off.
- [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) (§3.3, §4.2, Figs. 3–4)
  show on an isolated interface with a $\gamma$ jump that conservative
  reconstruction oscillates and primitive reconstruction keeps pressure and
  velocity errors close to machine precision; they then state, citing
  Johnsen–Colonius and others, that reconstruction "in conservative or
  characteristic variables" suffers from such oscillations. Characteristic
  variables are not tested in the paper.
- [Wong et al. (2021)](/sources/wong-2021.md) (App. A) and
  [Zheng et al. (2021)](/sources/zheng-2021.md) (§2.2, §3.1.3) do both: they
  project the **primitive** variables onto the characteristic fields of the
  quasilinear primitive system and interpolate there.

For the Euler equations in primitive variables $u_{\mathrm p}=(\rho,v,p)$
(page-local), the quasilinear system $\partial_tu_{\mathrm p}+A_{\mathrm p}\partial_xu_{\mathrm p}=0$
has (Zheng et al., §2.2)

$$A_{\mathrm p}=\begin{pmatrix}v&\rho&0\\0&v&1/\rho\\0&\rho c^2&v\end{pmatrix},\quad
R=\begin{pmatrix}1&1&1\\-c/\rho&0&c/\rho\\c^2&0&c^2\end{pmatrix},\quad
L=\begin{pmatrix}0&-\rho/(2c)&1/(2c^2)\\1&0&-1/c^2\\0&\rho/(2c)&1/(2c^2)\end{pmatrix},$$

with eigenvalues $v-c$, $v$, $v+c$. *(compiler check, not in the sources: the
three columns of $R$ are eigenvectors of $A_{\mathrm p}$ for $v-c$, $v$, $v+c$.)*
Zheng et al. add that characteristic decomposition has "a reduced effect at the
interface", whose characteristic structure is unclear because two fluids lie on
its two sides (§1); their interface is sharp and each fluid keeps its own nodal
values. For the five-equation diffuse-interface model with primitive variables
$(\phi_1\rho_1,\phi_2\rho_2,v_1,v_2,p,\phi_1)$ ($\phi_k$ the volume fractions,
registry §10), Wong et al. give $A_{\mathrm p}$ with eigenvalues
$v-c$, $v$ (four times), $v+c$, and evaluate $R$ at arithmetic averages of the
partial densities, the mixture density and the sound speed (App. A, Eq. (A.4)).
See [five- and six-equation models](/definitions/five-equation-model.md).

## Why it is used, and what it costs

[Chertock et al. (2023)](/sources/chertock-2023.md) (§2.1) state that the minmod limiter
applied to conservative variables "typically leads to large oscillations", which is why it is
applied to characteristic variables. [Fu (2023)](/sources/fu-2023.md) (§3.4) makes the cost
explicit: the hybrid TENO uses the optimal linear scheme **without** characteristic
decomposition wherever the TENO indicator flags smoothness and reports an overall efficiency
gain "by a factor of four" ([hybrid central-WENO schemes](/methods/hybrid-weno.md)).

[Wang & Don (2022)](/sources/wang-2022-b.md) (§3.3) use the linearity of the projection: an
[affine-invariant WENO](/methods/affine-invariant-weno.md) operator stays affine invariant in
characteristic variables, so the shallow-water still-water state is preserved without
further linearization ([well-balancing](/properties/well-balancing.md)).

## Methods that need none

The [unstaggered central scheme](/methods/unstaggered-central-scheme.md) of
[Kanbar et al. (2022)](/sources/kanbar-2022.md) limits its slopes componentwise
on the conserved deviation from a known steady state (§3, Eq. (8)); being Riemann-solver free, it has no
interface eigensystem to project on.

[Peng et al. (2024)](/sources/peng-2024.md) apply the [OEDG](/methods/oedg.md) damping to
the conservative variables with one coefficient (the maximum over components), without
characteristic decomposition (§2, Eq. (2.17)). They argue (Remark 2.12) that eigenvectors are
defined only up to scaling, so a damping coefficient that is not
[scale invariant](/properties/scale-invariance.md) depends on that arbitrary choice when
applied in characteristic variables, and a characteristic decomposition can destroy scale
invariance. On the [Woodward–Colella blast waves](/benchmarks/woodward-colella-blast-wave.md)
(640 cells) OEDG works with or without it, while the earlier OFDG without it "smears much"
(Ex. 5.7, Fig. 4).

## Qualifications

- Chertock et al. evaluate the field speeds at the reconstructed states while $R$
  diagonalizes the Jacobian at a third state; for nonlinear systems the per-field quantities
  are therefore an approximation, not an exact diagonalization.
- [Fu (2023)](/sources/fu-2023.md) calls the splitting with a global per-field maximum speed
  "Rusanov"; most of the literature calls it global Lax–Friedrichs (naming convention, see
  [Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md)).

# Citations

- [Fu (2023)](/sources/fu-2023.md) — §3.4 (Algorithm 1, hybrid TENO, Eqs. (21)–(24)), §3.6 (Algorithm 2).
- [Chertock et al. (2023)](/sources/chertock-2023.md) — §2.1 (Eqs. (2.5)–(2.8)), §3, Apps. A–B (arXiv v2).
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §VI (pointwise algorithm, steps 2–3).
- [Fu (2021)](/sources/fu-2021.md) — §5.
- [Li et al. (2022)](/sources/li-2022-b.md) — Eq. (38) and the numerical set-up.
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §5.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §4, §4.11.
- [Wang & Don (2022)](/sources/wang-2022-b.md) — §3.3.
- [Wang et al. (2023)](/sources/wang-2023-b.md) — §2.
- [Peng et al. (2024)](/sources/peng-2024.md) — §2 (Eq. (2.17), Remark 2.12), Ex. 5.7.
- [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) — §2.2, §4.1, §5.5 (arXiv v1).
- [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) — §3.3, §4.2 (Figs. 3–4).
- [Wong et al. (2021)](/sources/wong-2021.md) — §4.2, App. A (arXiv v1).
- [Zheng et al. (2021)](/sources/zheng-2021.md) — §1, §2.2, §3.1.3.
- [Wang et al. (2021)](/sources/wang-2021.md) — §3.1, Remark 1.
- [Li, Duan & Tang (2022)](/sources/li-2022-c.md) — §3.4, Eqs. (3.21)–(3.22) (arXiv v1).
- [Kanbar et al. (2022)](/sources/kanbar-2022.md) — §3, Eq. (8) (arXiv v1).
- [Browne et al. (2022)](/sources/browne-2022.md) — §2.2.
- [Bezgin et al. (2022)](/sources/bezgin-2022.md) — §2, §4.
- [Chu et al. (2022)](/sources/chu-2022.md) — Remarks 3.1, 6.2–6.3, §7.2 (Ex. 7).
- [Chen & Wu (2022)](/sources/chen-2022-b.md) — §3.2.2 (Eq. (38), Lemma 3.2), App. A (arXiv v1).
- [Du, Shu & Zhong (2022)](/sources/du-2022.md) — §3.1–3.2 (Eqs. (3.1)–(3.9)), §4.
- [Duan & Tang (2022)](/sources/duan-2022.md) — §4 (Eq. (4.1)) (arXiv v1).
