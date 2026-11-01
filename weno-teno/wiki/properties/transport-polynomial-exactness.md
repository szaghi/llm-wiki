---
type: Property
title: "Transport polynomial exactness"
description: "A moving-mesh scheme is TPE(k) when, for linear advection of a degree-k polynomial, its fully discrete solution equals the projection of the exact translated solution; TPE(0) is free-stream preservation, and Cai et al. prove TPE(2) for a rezoning moving-mesh finite-volume scheme under arbitrary mesh motion via evolved geometric moments."
status: hypothesis
aliases: [TPE, TPE(k), TPE(2), transport polynomial exactness of order k, evolved geometric moments, EGM, EGMs, higher-order geometric conservation law, quadratic polynomial preservation]
tags: [moving-mesh, finite-volume, reconstruction, weno, hybrid-scheme, free-stream-preservation]
timestamp: 2026-11-01T18:56:00Z
---

# Transport polynomial exactness

**Transport polynomial exactness of order $k$**, TPE($k$), is an exactness
criterion for schemes on moving meshes introduced by
[Cai, Cheng, Wu & Qiu (2026)](/sources/cai-2026.md) (Def. 2.1; arXiv v1,
no journal version). Let $\mathsf v\in\mathbb R^d$ be a constant advection
velocity (page-local; not the registry's wave speed $a$), so that the linear
system $\partial_tu+\mathsf v\cdot\nabla u=0$, $u\in\mathbb R^m$, has the
exact solution $u(t,x)=u_0(x-\mathsf vt)$. Let $(\mathbb P^k)^m$ be the
vector polynomials $p(x)=\sum_{\lvert\alpha\rvert\le k}c_\alpha x^\alpha$,
$c_\alpha\in\mathbb R^m$, of total degree at most $k$ ($k$ page-local, the
degree; a scheme of design order $k+1$). A scheme for a conservation law is
**TPE($k$)** if, whenever the law reduces to this linear advection with
$u_0\in(\mathbb P^k)^m$, the fully discrete solution coincides with the
projection of the exact solution onto the discrete space at every discrete
time. For finite volumes the projection is the vector of exact cell averages.
TPE($0$) is [free-stream preservation](/properties/free-stream-preservation.md).

The authors call the criterion "mesh-motion-independent", "verifiable" and
"a sharp diagnostic for assessing whether a moving-mesh method truly
delivers its nominal high-order accuracy" (§1.3–1.4). Nonlinear ingredients
(limiters, nonlinear reconstructions) may break it; the requirement is that
the *linear baseline* of a degree-$k$ scheme be TPE($k$) (§2.1).

## Why the geometric conservation law is not enough

On a moving mesh the classical geometric conservation law (GCL) makes the
numerically evolved cell volume consistent with the mesh motion, and with
it constant states are preserved: in Cai et al.'s words, TPE($0$) "is
precisely the property enforced by the classical GCL" (§1.3; for the
discrete GCLs of moving-mesh finite differences see
[free-stream preservation](/properties/free-stream-preservation.md) and
[adaptive moving mesh](/methods/adaptive-moving-mesh.md)). A finite-volume
reconstruction of order $k+1$ on a cell $I_{i,j}$ needs, besides the volume,
the geometric moments (page-local)

$$\mathfrak M_{s,r,i,j}=\int_{I_{i,j}}x^sy^r\,dx\,dy,\qquad s+r\le k,$$

because fitting $p=\sum_{s+r\le k}c_{s,r}x^sy^r$ to the cell integrals
$\mathfrak V_{i,j}=\int_{I_{i,j}}u\,dx\,dy$ (page-local) of a stencil means
solving $\sum_{s,r}c_{s,r}\mathfrak M_{s,r,i,j}=\mathfrak V_{i,j}$
(Eqs. (3.2)–(3.3)). On a moving mesh the $\mathfrak V_{i,j}$ are evolved
numerically and carry discretization errors, while conventional remaps
"typically" compute the moments exactly from the cell geometry (bilinear map and
$3\times3$ Gauss–Lobatto rule, Eqs. (3.4)–(3.6)). Coupling "inexact"
$\mathfrak V$ with "exact" $\mathfrak M$ is a mismatch that, according to
Cai et al., "degrades accuracy and can preclude convergence"; the classical
GCL removes it only for the zeroth moment (§3.1.1).

## Evolved geometric moments

The remedy is to evolve every moment the reconstruction needs by its own
Reynolds-transport equation, discretized exactly as the conserved
variables are. With $v_{\mathrm g}$ the mesh velocity (page-local, as on
[conservative remapping](/methods/conservative-remapping.md)) and $n$ the
outward unit normal,

$$\frac{d\mathfrak M_{s,r,i,j}}{d\tau_{\mathrm p}}=\int_{\partial I_{i,j}(\tau_{\mathrm p})}x^sy^r\,(v_{\mathrm g}\cdot n)\,dS ,$$

with $\tau_{\mathrm p}$ the (pseudo-)time of the mesh motion (page-local)
(Eq. (3.7)). Its boundary-flux structure mirrors that of the moving-cell
conservation law of the remap. Cai et al. discretize it with the same
three-point Gauss–Lobatto rule on every edge $l_e$ (page-local edge index
$e=1,\dots,4$, points $x_{e,g}$, weights $\mathsf w_g=\tfrac16,\tfrac23,\tfrac16$)
that the conserved variables use (Eq. (3.9)):

$$\frac{d\widetilde{\mathfrak M}_{s,r,i,j}}{d\tau_{\mathrm p}}=\sum_{e=1}^4\lvert l_e\rvert\sum_{g=1}^3\mathsf w_g\,x^s_{e,g}y^r_{e,g}\,(v_{\mathrm g}\cdot n_e)_{e,g}=:\mathcal L^{\mathfrak M_{s,r}}_{i,j},$$

and advance it with the same Runge–Kutta method. The results
$\widetilde{\mathfrak M}_{s,r,i,j}$ are the **evolved geometric moments**
(EGMs). $\widetilde{\mathfrak M}_{0,0}$ is the classical GCL; the higher
EGMs "extend geometric compatibility to higher degrees" (§3.1.1). The EGMs
replace the exact moments everywhere in the reconstruction, including the
centroid and the scaling of the normalized basis (Remark 3.5, Eqs.
(3.23)–(3.24)); no reference-to-physical map or Jacobian is evaluated, and
the authors call the scheme "mapping- and Jacobian-free" (§1.4).

**Adapted $k$-exactness** (Def. 3.1, a modification of Barth's
$k$-exactness). A reconstruction is $k$-exact if, on a fixed geometry,
whenever the stencil averages are generated by a polynomial through the
EGMs, $\bar u_{i,j}=\widetilde{\mathfrak M}_{0,0,i,j}^{-1}\sum_{s+r\le k}c_{s,r}\widetilde{\mathfrak M}_{s,r,i,j}$,
the reconstruction returns that polynomial (Eq. (3.12)). The cell integral
of the polynomial is thus *approximated* by the EGMs (Remark 3.2). If every
average in the domain comes from one quadratic and the reconstruction is
2-exact, the interior and exterior traces at every edge point agree and
equal $p(x_{e,g})$ (Eq. (3.13)).

## The TPE(2) proof for a rezoning moving-mesh scheme

Cai et al. build a two-dimensional finite-volume scheme on quadrilaterals
in the rezoning moving-mesh framework (physical evolution on a fixed mesh,
rezoning, remapping; see [adaptive moving mesh](/methods/adaptive-moving-mesh.md)
and [conservative remapping](/methods/conservative-remapping.md)), with a
[hybrid WENO](/methods/hybrid-weno.md) reconstruction that is the optimal
least-squares quadratic in cells not flagged by the KXRCF
[troubled-cell indicator](/definitions/troubled-cell-indicator.md) and
Zhu & Qiu's third-order WENO in flagged cells (§3.4, Eq. (3.22)), the
[Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md) and
[SSP-RK3](/methods/ssp-runge-kutta.md). The proof is a chain:

1. **Linear relation** (Lemma 3.3). With a 2-exact reconstruction and
   $\bar u_{i,j}=\widetilde{\mathfrak M}^{-1}_{0,0,i,j}\sum_{s+r\le2}c_{s,r}\widetilde{\mathfrak M}_{s,r,i,j}$
   in every cell, the remap operator of the conserved integrals is the
   same combination of the moment operators,
   $\mathcal L^{\mathfrak V}_{i,j}=\sum_{s+r\le2}c_{s,r}\mathcal L^{\mathfrak M_{s,r}}_{i,j}$:
   equal traces cancel the Lax–Friedrichs dissipation, and the remap flux
   $-u\,(v_{\mathrm g}\cdot n)$ evaluated on $p$ is the moment flux.
2. **Remap, forward Euler** (Thm. 4.3). If
   $\mathfrak V^\ell_{i,j}=\sum c_{s,r}\widetilde{\mathfrak M}^\ell_{s,r,i,j}$
   at one pseudo-time level, the same holds at the next, for any mesh
   motion and any pseudo-time step. The updated averages are those of $p$
   "in the sense of EGM-based integration".
3. **Remap, SSP-RK3** (Prop. 4.4). SSP-RK3 is a convex combination of
   forward-Euler steps, so the remap operator is TPE(2) "regardless of the
   prescribed mesh motion, mesh quality, or the pseudo-time step size".
   Remark 4.5 extends this to TPE($k$) with a $k$-exact reconstruction "and
   any SSP time discretization".
4. **Physical evolution** (Prop. 4.1). On a fixed mesh with
   $u_0\in(\mathbb P^2)^m$ the semi-discrete scheme is spatially exact,
   because three-point Gauss–Lobatto integrates cubics exactly; and since
   the third power of the exact operator annihilates quadratics, the SSP-RK3
   stability polynomial $1+z+z^2/2+z^3/6$ applied to it equals the exact
   evolution $e^{\Delta t\mathcal L}$. The new averages are those of
   $p(x-\mathsf v_1\Delta t,y-\mathsf v_2\Delta t)$, for any $\Delta t$
   (Prop. 4.1); with a 3-exact reconstruction the evolution is TPE(3)
   (Remark 4.2).
5. **Full scheme** (Thm. 4.6). The composition is TPE(2) for any
   $\Delta t$ and any pseudo-time step.

**Geometric consistency** (Thm. 4.7). Step 4 uses exact moments, step 2
EGMs; they coincide. For a quadrilateral whose vertices move linearly in
$\tau_{\mathrm p}$, the exact moment $\mathfrak M_{s,r}(\tau_{\mathrm p})$
is a polynomial of degree at most $s+r+2$ (Lemma 4.8: on each edge the
position and $v_{\mathrm g}\cdot n^*$, with the scaled normal $n^*$, are
affine in $\tau_{\mathrm p}$ and in the edge parameter). For $s+r\le2$ the
three-point edge rule gives $d\mathfrak M_{s,r}/d\tau_{\mathrm p}$ exactly
(Lemma 4.9, integrand of degree at most 3 in the edge parameter). For a
pure quadrature problem $u'=f(\tau_{\mathrm p})$, SSP-RK3 with stage
geometries at $\tau_{\mathrm p}$, $\tau_{\mathrm p}+\Delta\tau_{\mathrm p}$
and $\tau_{\mathrm p}+\tfrac12\Delta\tau_{\mathrm p}$ is Simpson's rule
(Lemma 4.10):

$$u^{\ell+1}-u^\ell=\frac{\Delta\tau_{\mathrm p}}6\Big[f(\tau^\ell_{\mathrm p})+4f\big(\tau^\ell_{\mathrm p}+\tfrac12\Delta\tau_{\mathrm p}\big)+f(\tau^\ell_{\mathrm p}+\Delta\tau_{\mathrm p})\Big].$$

*(Compiler check: the stages give $u^{(2)}=u^\ell+\tfrac{\Delta\tau_{\mathrm p}}4(f_0+f_1)$
and $u^{\ell+1}=u^\ell+\tfrac{\Delta\tau_{\mathrm p}}6(f_0+f_1)+\tfrac{2\Delta\tau_{\mathrm p}}3f_{1/2}$,
which is the formula.)* Simpson's rule is exact for cubics, and the
derivative of a moment with $s+r\le2$ is at most cubic, so
$\widetilde{\mathfrak M}^{\ell+1}_{s,r,i,j}=\mathfrak M_{s,r,i,j}(\tau^{\ell+1}_{\mathrm p})$:
the authors call it a "fourth-order superconvergence" of SSP-RK3 (§4.4).
No geometric refreshing or source-term correction is needed, which they
reject because it "compromise[s] conservation" (§4.4). Ketcheson's
ten-stage fourth-order SSP method lacks this superconvergence and reaches
the same exactness at higher cost (Remark 4.11).

**Consequence for the pseudo-time step.** Because the remap is exact on
quadratics for any $\Delta\tau_{\mathrm p}$, only stability limits it, and
the number of pseudo-time levels per physical step is $N_\ell=O(1)$ under
a bounded but discontinuous mesh velocity, against $O(\Delta x^{-1})$ for
remaps that need a Lipschitz mesh velocity (§4.5; details on
[conservative remapping](/methods/conservative-remapping.md)).

## Evidence

**Polynomial advection on random meshes** (§5.1, Table 1).
$\partial_tu+\partial_xu+\partial_yu=0$ on $[0,1]^2$, $40\times40$ cells,
exact boundary values at every Runge–Kutta stage, random rezoning of
amplitude $C_r=0.5$ (page-local) plus a drift $(-0.6,-0.8)$, $t=0.1$; 20
random quadratic, linear and constant initial data each, coefficients
uniform in $(-5,5)$. Maximum $L^1$ errors:

| initial data | TPE(2), $O(1)$ levels | GCL only, $O(1)$ levels | exact moments, $O(1)$ levels | exact moments, resolution-dependent levels |
|---|---|---|---|---|
| quadratic | $7.13\times10^{-15}$ | $1.88\times10^{-4}$ | $1.37\times10^{-2}$ | $1.11\times10^{-2}$ |
| linear | $6.30\times10^{-15}$ | $1.06\times10^{-4}$ | $1.10\times10^{-2}$ | $8.82\times10^{-3}$ |
| constant | $4.93\times10^{-15}$ | $5.00\times10^{-15}$ | $5.85\times10^{-3}$ | $4.80\times10^{-3}$ |

"GCL only" uses the evolved volume and exact higher moments; "exact
moments" computes all moments from the geometry, as Gu et al. do
([conservative remapping](/methods/conservative-remapping.md)); average
$N_\ell=1.9$ for the first three columns and $2.1$ for the last. The GCL-only
scheme is exact for constants and not for linear or quadratic data, which
the authors take as confirmation that "while the classical GCL suffices for
free-stream preservation, it is insufficient to guarantee TPE($k$) for
$k\ge1$" (§5.1). The exact-moment schemes fail even for constants.

**Euler equations on random meshes** (§5.2, Table 2). For the smooth
[density wave](/benchmarks/density-wave-advection.md)
$\rho=1+0.2\sin(2\pi(x+y))$ on $80^2$ to $320^2$ randomly rezoned cells,
the TPE(2) scheme with $N_\ell=2$ keeps $L^1$ orders 2.93–2.98 while the
measured Lipschitz constant of the mesh velocity grows from 1874.9 to
8443.5; the GCL-only scheme loses order in $L^\infty$ (1.06, $-0.00$,
$-0.55$ on the middle meshes) and the exact-moment scheme with two levels
does not converge ($L^1$ about $1.5$–$1.7\times10^{-3}$ on every mesh).
Cost figures are on [conservative remapping](/methods/conservative-remapping.md).

## Qualifications

- **Single source, unrefereed.** The definition, the theorems and the
  tests come from one arXiv preprint with no journal version as of
  2026-11-01; the page carries `status: hypothesis` for that reason, not
  because the authors present anything as conjectural.
- **Nonlinear switch.** The TPE(2) proof needs the reconstruction to be
  2-exact on the data. Cai et al. state that the KXRCF indicator
  "automatically yields" no flagged cell for quadratic data (§3.4); this is
  asserted, not proved, and Table 1 is the evidence.
- **EGM sense versus Definition 2.1.** Theorem 4.3 and Proposition 4.4 give
  exactness "in the sense of EGM-based integration"; it is the projection of
  Definition 2.1 only because Theorem 4.7 makes the EGMs equal the exact
  moments, and Theorem 4.7 is proved for $s+r\le2$ with SSP-RK3 and the
  three-point edge rule. *(Compiler check, not in the sources: for $s+r=3$
  the exact moment has degree 5 in $\tau_{\mathrm p}$ and its derivative
  degree 4; Simpson's rule is not exact for quartics,
  $\tfrac16\big(0+4\cdot\tfrac1{16}+1\big)=\tfrac5{24}\ne\tfrac15=\int_0^1\tau^4\,d\tau$,
  and the edge integrand has degree 4 in the edge parameter, beyond the
  cubic exactness of three-point Gauss–Lobatto. Remark 4.5's TPE($k$) for
  $k\ge3$ with "any SSP time discretization" therefore holds in the EGM
  sense but not, without further conditions, in the sense of Definition 2.1.
  Conversely, the forward-Euler argument of Theorem 4.3 uses only that each
  Runge–Kutta stage is a combination of earlier stages with coefficients
  summing to one plus forward-Euler increments, so the EGM-sense exactness
  does not need the SSP property.)*
- **Scope of the theory.** Two-dimensional convex quadrilaterals with
  counterclockwise, pairwise distinct vertices at every pseudo-time
  (Assumption 3.4), straight edges and vertices moving linearly in
  pseudo-time (Eq. (3.17)); curved cells are not covered. Lemma 4.8 is
  stated with "degree $s+r+2$" and proved as "at most $s+r+2$".
- **"Superconvergence".** The word refers to SSP-RK3 integrating a
  cubic-in-time right-hand side exactly because its stage times are those
  of Simpson's rule; it is not a statement about SSP-RK3 for general ODEs.
- **Relation to discrete-GCL proofs.** Duan & Tang's free-stream proof for
  moving-mesh finite differences has the same structure as Theorem 4.3 and
  Proposition 4.4, a forward-Euler step that preserves the constant state
  followed by the convex-combination argument for SSP Runge–Kutta
  ([free-stream preservation](/properties/free-stream-preservation.md),
  Duan & Tang (2022), Prop. 3.2); Cai et al. carry it from the constant to
  the quadratic by adding the higher moments *(compiler check, not in the
  sources)*.
- **Challenge to the prevailing view.** Cai et al. state that the work
  "challenges the prevailing assumption that high-order accuracy in ALE
  methods necessitates mesh-velocity smoothness" (§6). The sources of this
  bundle that require that smoothness ([Gu et al. (2023)](/sources/gu-2023.md),
  §2.2) use exact moments, which is the case Cai et al. show to fail without
  many pseudo-time levels; the two claims concern different discretizations
  and do not contradict each other.

# Citations

- [Cai, Cheng, Wu & Qiu (2026)](/sources/cai-2026.md) — §1.2–1.4; §2.1 Def. 2.1; §3.1 Eqs. (3.1)–(3.18), Def. 3.1, Remark 3.2, Lemma 3.3; §3.4 Eq. (3.22), Remarks 3.5–3.6; §4.1–4.5 Prop. 4.1, Remark 4.2, Thm. 4.3, Prop. 4.4, Remark 4.5, Thm. 4.6, Thm. 4.7, Lemmas 4.8–4.10, Remark 4.11; §5.1–5.2 Tables 1–2; §6 (arXiv v1).
- [Duan & Tang (2022)](/sources/duan-2022.md) — §3.3 Prop. 3.2 (forward-Euler and SSP structure of the free-stream proof, compared).
- [Gu, Li, Cheng & Shu (2023)](/sources/gu-2023.md) — §2.2 (mesh-velocity regularity of the exact-moment remap).
