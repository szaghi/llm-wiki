---
type: Method
title: "Characteristic decomposition"
description: "Local characteristic decomposition projects stencil data onto the eigenvectors of the flux Jacobian at an interface state, reconstructs each field separately and projects back; WENO, TENO and central-upwind schemes use it against oscillations, multiphase sources project primitive variables at material interfaces, entropy-stable schemes scale the eigenvectors, and some schemes do without it."
status: established
aliases: [local characteristic decomposition, LCD, characteristic-wise reconstruction, characteristic projection, reconstruction in characteristic variables, primitive-variable reconstruction]
tags: [characteristic, reconstruction, weno, teno, central-scheme, multiphase]
timestamp: 2026-10-23T15:15:00Z
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
cases), [Li et al. (2022b)](/sources/li-2022-b.md) ("global Lax–Friedrichs flux splitting with
local characteristic fields", with Eq. (38)), [Luo & Wu (2021)](/sources/luo-2021-b.md) (§5),
[Takagi et al. (2022)](/sources/takagi-2022.md) (§4, where THINC is applied per characteristic
component and per split-flux direction), [Wang & Don (2022)](/sources/wang-2022-b.md)
(§3.3, well-balanced shallow-water WENO) and
[Wang et al. (2021)](/sources/wang-2021.md) (§3.1, Remark 1, for their
[multi-resolution WENO](/methods/multi-resolution-weno.md)).
[Wang et al. (2023b)](/sources/wang-2023-b.md) apply it to the WENO-Z *interpolation* of
point values in [A-WENO](/methods/alternative-weno.md) (§2). [Browne et al. (2022)](/sources/browne-2022.md) use the
finite-difference algorithm with Rusanov splitting for fifth-order WENO on disturbance fluxes,
the characteristic transform being applied "to improve the shock capturing characteristics"
(§2.2); [Bezgin et al. (2022)](/sources/bezgin-2022.md) use the finite-volume algorithm with the
local Lax–Friedrichs flux for their learned three-point WENO (§2, §4).
The TENO papers of [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) (§4) and
[Liang et al. (2022)](/sources/liang-2022.md) (§3–4) use the finite-difference algorithm with
Roe averages and Rusanov splitting (global or local not stated);
[Hong et al. (2022)](/sources/hong-2022.md) reconstruct in characteristic variables with a Roe
flux by default for their TENO-M schemes (§2, §5);
[Jeong et al. (2022)](/sources/jeong-2022.md) (§5) use it for the 1D Euler tests of their
RBF-based WENO, with eigenvalues $v-c$, $v$, $v+c$, and treat 2D dimension by dimension.
[Wan & Xia (2022)](/sources/wan-2022.md) (§2, Eqs. (2.7)–(2.9)) state the averaged state as a
Roe average satisfying $f(u_{i+1})-f(u_i)=A(u_{i+1/2})(u_{i+1}-u_i)$, split each field with its
own maximum $\max_j\lvert\lambda_l(u_j)\rvert$ over the stencil, and in most tests use instead
the global $\max(\lvert v\rvert+c)$ per direction. [Li et al. (2023a)](/sources/li-2023.md)
(Eqs. (30)–(33)) project the conservative variables with Roe-averaged $L_{i+1/2}$, $R_{i+1/2}$
for the six-point interpolation of their [A-WENO](/methods/alternative-weno.md).
[Fan et al. (2022)](/sources/fan-2022.md) (§3) project, with the eigenvectors of the Roe matrix
of $u_i$ and $u_{i+1}$, not the Lax–Friedrichs split fluxes but the split auxiliary variables of
their positivity-preserving Navier–Stokes splitting
([positivity-preserving Navier–Stokes fluxes](/methods/positivity-preserving-navier-stokes-flux.md));
they print the factorization as $A=L\Lambda R$, where $A=R\Lambda L$ is meant.

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
  [Chu et al. (2025b)](/sources/chu-2025-b.md) (§3–§4, Apps. A–B) do the same for the
  flux-globalized LCD-PCCU scheme, with the matrix $A+\mathcal C$ (their $\partial F/\partial U-B$,
  the product written on the right-hand side as $B\,\partial_xU$) at an average of primitive-type
  quantities, and print closed forms.
  For the $\gamma$-based two-fluid system with stiffened gas the eigenvalues are $v-c$, $v$ (three
  times in 1D, four in 2D), $v+c$, with $c=\sqrt{\gamma(p+p_\infty)/\rho}$ from averaged $\gamma$,
  $p$, $p_\infty$, $\rho$; for the thermal rotating shallow-water system they are $v\mp\sqrt{bh}$ and
  $v$ (twice), $b$ the buoyancy and $h$ the depth (page-local). Unlike Chu et al. (2022) they
  apply the projection only in the numerical flux, through the field-wise coefficients, and
  reconstruct conservative (or equilibrium) variables (Remark 2.2; see [LCD central-upwind scheme](/methods/lcd-central-upwind-scheme.md)).
- **Arithmetic mean of conservative averages.** In the adaptive
  [low-dissipation central-upwind schemes](/methods/low-dissipation-central-upwind-scheme.md)
  of [Chu et al. (2025a)](/sources/chu-2025.md) (§2.1, App. A) $R_{i+1/2}$ diagonalizes
  $A\big(\tfrac12(\bar u_i+\bar u_{i+1})\big)$, and the four averages $\bar u_{i-1},\dots,\bar u_{i+2}$
  are projected with it before the SBM-limited piecewise-linear reconstruction; the stated
  purpose is to reduce the oscillations of the compressive and overcompressive limiters near
  shocks and contacts (§1). The Euler matrices are taken from Chertock et al. (2023).
- **Several directions per cell on unstructured meshes.** On triangles,
  [Chen & Wu (2022)](/sources/chen-2022-b.md) (§3.2.2, Eq. (38)) project the stencil averages onto
  the eigenvectors of the normal Jacobian for each of the three edge normals of the target cell,
  evaluated at the cell average through the recovered primitive state, reconstruct in each
  frame, project back, and average the three polynomials with weights $\lvert K_j\rvert$, the
  areas of the three neighbours in the paper's notation for cell areas (§2.2). The resulting
  operator stays homogeneous of degree one, $R_h(\sigma u)=\sigma R_h(u)$ for $\sigma>0$, because the
  eigenvector matrices are invariant under $u\mapsto\sigma u$ (Lemma 3.2;
  [scale invariance](/properties/scale-invariance.md)).
- **Scaling of the eigenvectors.** A right eigenvector $\mathsf r$ (column of $R$) and its
  left eigenvector $\mathsf l$ (row of $L$) can be rescaled to $(\mu_{\mathrm r}\mathsf r,\mathsf l/\mu_{\mathrm r})$
  for any $\mu_{\mathrm r}\neq0$ ($\mathsf r$, $\mathsf l$, $\mu_{\mathrm r}$ page-local) without
  changing $RL=I$. [Cai, Qiu & Wu (2024)](/sources/cai-2024.md) (Remark 3.3) compare, for
  relativistic hydrodynamics, no rescaling, "unitization" $\mu_{\mathrm r}=\lvert\mathsf l\rvert$,
  which can make $\lvert\mu_{\mathrm r}\mathsf r\rvert$ huge, and "matching"
  $\mu_{\mathrm r}=\sqrt{\lvert\mathsf l\rvert/\lvert\mathsf r\rvert}$, which equalizes the two
  norms. On their second 2D relativistic Riemann problem ($400^2$) the unrescaled and unitized
  eigenvectors give "serious oscillations", matching does not (Ex. 5.7, Fig. 7). Their
  eigenvectors are those of the Roe matrix of Eulderink and Mellema, evaluated from the
  primitive variables recovered by their provably convergent Newton iterations; only the
  interface points of troubled cells are reconstructed characteristic-wise, the inner
  quadrature points and the non-troubled cells componentwise (§3.1.3, Step 2;
  [Hermite WENO](/methods/hermite-weno.md),
  [relativistic hydrodynamics](/definitions/relativistic-hydrodynamics.md)). The scaling is the
  same freedom that [Peng et al. (2024)](/sources/peng-2024.md) invoke against
  characteristic-wise damping (below): Cai et al. show that it changes the numerical solution,
  Peng et al. that it changes scale invariance.
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
- **Direction by direction in a nodal limiter.** In the compact TENO/WENO limiter for the
  nodal [spectral difference method](/methods/spectral-difference-method.md) of
  [Chen & Fu (2024)](/sources/chen-2024.md) (§6, Eqs. (70)–(72), after Qiu and Shu), the
  Jacobian is frozen at the cell average of the target cell, $A_i=R_i\Lambda_iL_i$ (page-local
  $\Lambda_i$), and the cell averages of the target cell and its two face neighbours and the
  cell-averaged first derivatives of the neighbours are projected by $L_i$; each characteristic
  component is limited and the result is mapped back by $R_i$. In 2D the limiter runs along lines
  of solution points, with the characteristic direction that of the sweep ($x$ or $y$), and the
  nodal values from the two sweeps are averaged (§7, Algorithm 1, Eq. (73)). Their fourth-order
  candidates also use cell-averaged second derivatives of the neighbours (Eq. (51)), whose
  characteristic projection Eq. (71) does not list.
- **Only where a detector fires.** The hybrid MDAD scheme of [Li et al. (2022a)](/sources/li-2022.md)
  (§3.4) decomposes only at interfaces flagged non-smooth by its shock detector, with $R$ from
  the simple average of the two neighbouring states, splits by global Lax–Friedrichs in
  characteristic space and runs a second detection on each split characteristic flux, which
  chooses between the linear scheme and the nonlinear one field by field; elsewhere the
  reconstruction is componentwise. For the Taylor–Green vortex they switch to local
  characteristic Lax–Friedrichs splitting because, citing earlier work, the global one is too
  dissipative (§4.4;
  [hybrid central-WENO schemes](/methods/hybrid-weno.md)).
  The TENO-S scheme of [Liang & Fu (2024b)](/sources/liang-2024-b.md) (§3.2, Algorithm 1)
  goes further: its eight-point discontinuity indicator is evaluated on the conserved
  variables in physical space, and only in flagged cells are the eight point values and
  fluxes $u_{i-3},\dots,u_{i+4}$ projected with Roe-average $L_{i+1/2}$, split field by field
  with Rusanov (Lax–Friedrichs) splitting at the field's maximum speed, reconstructed by
  eight-point TENO and projected back with $R_{i+1/2}$; smooth cells take a kinetic-energy-preserving
  [split-form](/methods/split-convective-forms.md) central flux in physical variables, which
  the authors call "significantly more efficient" than characteristic-space ENO-like
  reconstruction (§2.3). They report that more than 90 % of the cells of the double Mach
  reflection take the split-form branch (§4.6; no count shown), and replace Rusanov by Roe
  splitting with entropy fix "to obtain a stable result" on the interacting blast waves (§4.4).
- **Eigenvectors of another system.** In the semi-implicit all-Mach scheme of
  [Boscarino et al. (2022)](/sources/boscarino-2022.md) (§3.3.1) only the explicit
  (material-wave) flux is reconstructed characteristic-wise, with the local eigenvectors of the
  full Euler system **at Mach number one**, not of the split flux; the implicit acoustic flux is
  reconstructed componentwise ([semi-implicit all-Mach schemes](/methods/semi-implicit-all-mach-scheme.md)).
- **Eigenvectors at Mach number one, MHD.** [Chen, Wu & Xiong (2023)](/sources/chen-2023-b.md)
  (§3.3) do the same for ideal MHD at sonic Mach number $\varepsilon$: the explicit
  convective–magnetic flux is reconstructed characteristic-wise at the arithmetic-mean state
  $\tfrac12(u_i+u_{i+1})$, with global Lax–Friedrichs splitting of each field, and the
  eigenvectors are those of the MHD system with $\varepsilon=1$, because for small $\varepsilon$ the
  true ones "will make such a spectral characteristic decomposition to be unstable"; the
  authors give no analysis and state that this "works well from our numerical results". The
  other two flux parts are reconstructed componentwise
  ([semi-implicit all-Mach schemes](/methods/semi-implicit-all-mach-scheme.md)).
- **Values and gradients together.** In the gradient-based finite-difference schemes the
  interface state is built from point values and cell-centre derivatives, and both are
  projected with the same frozen matrix, which the linearity of the projection allows.
  [Chamarthi (2023a)](/sources/chamarthi-2023.md) (§3.3, Eqs. (62)–(64)) project the primitive
  values and gradients on $i-2,\dots,i+3$ with $L_{i+1/2}$ from arithmetic or Roe averages,
  apply the [gradient-based reconstruction](/methods/gradient-based-reconstruction.md) and the
  [MP limiter](/methods/monotonicity-preserving-limiter.md) in characteristic space and project
  back; characteristic projection is recommended "for cleanest results", but the paper does not
  say per test which variables were used, except for one 2D Riemann problem run "using
  primitive variables" (Fig. 10). [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) (§2.3)
  call shock capturing in characteristic variables "essential" and project the variables of
  choice (conservative or primitive) together with their gradients. [Chandravamsi et al. (2023)](/sources/chandravamsi-2023.md)
  (§5.1 Step 2, App. A) project the primitive variables $(\rho,v,p)$ and their first and
  second derivatives with the eigenvectors of the quasilinear primitive-variable matrix in the
  direction of the interface metrics, on generalized curvilinear meshes.
- **Characteristic flux splitting in a finite-volume code.** [JAX-Fluids](/software/jax-fluids.md)
  ([Bezgin et al. (2023)](/sources/bezgin-2023.md), §3.3) offers two routes: reconstruction of
  primitive or conservative cell averages, optionally in characteristic space, followed by an
  approximate Riemann solver; or the finite-difference recipe above applied to cell averages
  with one-point face quadrature, with a Roe or arithmetic face state, componentwise local
  Lax–Friedrichs or Roe splitting of the characteristic fluxes, WENO on the split fluxes and
  back-projection.
- **Point values inside a finite-volume scheme.** The fourth-order finite-volume MHD scheme of
  [Berta et al. (2024)](/sources/berta-2024.md) reconstructs interface point values from
  cell-centre point values with pointwise WENO-Z or MP5, "in primitive or characteristic
  variables" (§3.2; §4, step 7); their 3D rotated MHD shock tube uses WENO-Z in characteristic
  variables and the relativistic one MP5 in primitive variables (§5.1). The detector of
  their order-reduction fallback uses primitive variables, which "has shown to yield a more
  robust identification method" (§3.4).
- **Main fluxes only.** The finite-difference Hermite WENO of [Fan et al. (2023)](/sources/fan-2023.md)
  (§2, Remark 2.2) reconstructs the fluxes of the conservation law in local characteristic
  directions and the fluxes of its derivative equations componentwise
  ([Hermite WENO](/methods/hermite-weno.md)).
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

The most direct evidence is that of [Boscarino et al. (2022)](/sources/boscarino-2022.md)
(Ex. 5.4, Figs. 5.4–5.5): on two [2D Riemann problems](/benchmarks/two-dimensional-riemann-problems.md)
($400^2$, Mach number one) the scheme with characteristic-wise WENO on the explicit flux is
closest to the reference with no obvious oscillations, while componentwise WENO everywhere,
with or without the pressure splitting, shows "clear oscillations" in the middle region; the
authors conclude on "the importance of characteristic reconstructions". [Ji et al. (2022)](/sources/ji-2022.md)
(§2.3) recommend characteristic variables as "generally believed" to suppress oscillations
better than primitive or conservative ones, yet state for their shock tubes that conservative
variables are reconstructed "due to the simplicity".
[Hong et al. (2022)](/sources/hong-2022.md) (§6) note that their timings include flux splitting
and characteristic decomposition, whose cost is the same for every reconstruction, so the saving
of TENO-M over TENO in the reconstruction alone is "much higher" than the totals show (not
measured).

The cost is measured on a GPU by [Bezgin et al. (2023)](/sources/bezgin-2023.md) (§6, Table 3):
on a Taylor–Green vortex on one RTX A6000, characteristic Roe flux splitting with WENO5
("ROE") costs about 300 ns per cell and time step in single precision against about 25 ns for
primitive-variable WENO5 with HLLC, "roughly an order of magnitude" more, which they attribute
to the eigenvector and eigenvalue computation. They also attribute, after Qiu and Shu, the
slight oscillations of the primitive-variable HLLC setup on the Sod and Lax tubes to
reconstruction in physical space (§3.3, §5.1.2, Figs. 9–10); no characteristic-space run of the
same Godunov setup is shown.

**The field speeds matter beyond oscillations.** For steady Euler problems
[Wan & Xia (2022)](/sources/wan-2022.md) (Ex. 4.4, Figs. 4.4–4.6) find that on the shock
reflection ($120\times30$) only their WENO-H residue falls to about $10^{-12}$ with the global speed
$\max(\lvert v\rvert+c)$, whereas with per-field speeds $\max\lvert v-c\rvert$, $\max\lvert v\rvert$
(twice), $\max\lvert v\rvert+c$ all three schemes tested converge to that level
([Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md)).

[Wang & Don (2022)](/sources/wang-2022-b.md) (§3.3) use the linearity of the projection: an
[affine-invariant WENO](/methods/affine-invariant-weno.md) operator stays affine invariant in
characteristic variables, so the shallow-water still-water state is preserved without
further linearization ([well-balancing](/properties/well-balancing.md)).
[Li et al. (2023a)](/sources/li-2023.md) (§4.2, Thm. 5) make the same argument for the Euler
equations with gravity: at a hydrostatic equilibrium the Roe-averaged velocity vanishes and the
characteristic variables are $(\lambda_{\mathrm e}p_{\mathrm e},\ \rho_{\mathrm e}-2\lambda_{\mathrm e}p_{\mathrm e},\ \lambda_{\mathrm e}p_{\mathrm e})$
with $\lambda_{\mathrm e}=(2\hat c^2_{i+1/2})^{-1}$ (page-local; $\rho_{\mathrm e}$, $p_{\mathrm e}$ the
equilibrium density and pressure), multiples of the equilibrium pressure, so a scale-invariant
interpolation in characteristic variables reproduces the equilibrium exactly; they call this
"the crucial novel idea".

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

[Lesur et al. (2023)](/sources/lesur-2023.md) (§2.3) reconstruct the primitive variables
$(\rho,v,B,p)$ in IDEFIX, avoiding characteristic decomposition "while keeping the basic
physical constraints (density and pressure positivity for instance)" (no proof given), and
attribute a small post-shock velocity oscillation in the [Brio–Wu shock tube](/benchmarks/brio-wu-shock-tube.md)
to that choice (§4.2, Fig. 6; [IDEFIX](/software/idefix.md)).

## Qualifications

- Chertock et al. evaluate the field speeds at the reconstructed states while $R$
  diagonalizes the Jacobian at a third state; for nonlinear systems the per-field quantities
  are therefore an approximation, not an exact diagonalization.
- Chu et al. (2025b), App. A, print for the 1D two-fluid system an $R_{i+1/2}$ and an
  $R^{-1}_{i+1/2}$ that are not inverse to each other. *(compiler check, not in the sources:
  symbolically, the printed $R$ diagonalizes the printed matrix (A.1),
  $(\text{A.1})\,R=R\,\mathrm{diag}(v-c,v,v,v,v+c)$, but the printed inverse gives $R^{-1}R=\mathrm{diag}(1,1,1,-1,1)$;
  flipping the sign of entry (4,5) of $R^{-1}$, or taking column 4 of $R$ as $(0,0,0,1,-p)^\top$
  as in their 2D matrix, restores $R^{-1}R=I$. Their 2D $R^{-1}$ prints five rows of six; with the
  row $(0,0,0,0,0,-1/p)$ inserted as the fifth, $R^{-1}R=I$. The printed (A.1) equals
  $\partial f/\partial u$ plus $\mathrm{diag}(0,0,0,v,v)$, which matches the advection
  $\partial_t\Gamma=-v\partial_x\Gamma$ of their Eq. (5.2), so the printed
  $B=\mathrm{diag}(0,0,0,0,v,v)$ of §5.1 has the wrong sign.)* The thermal shallow-water
  matrices of App. B invert and diagonalize exactly *(same check)*.
- [Fu (2023)](/sources/fu-2023.md) calls the splitting with a global per-field maximum speed
  "Rusanov"; most of the literature calls it global Lax–Friedrichs (naming convention, see
  [Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md)).

# Citations

- [Fu (2023)](/sources/fu-2023.md) — §3.4 (Algorithm 1, hybrid TENO, Eqs. (21)–(24)), §3.6 (Algorithm 2).
- [Chertock et al. (2023)](/sources/chertock-2023.md) — §2.1 (Eqs. (2.5)–(2.8)), §3, Apps. A–B (arXiv v2).
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §VI (pointwise algorithm, steps 2–3).
- [Fu (2021)](/sources/fu-2021.md) — §5.
- [Li et al. (2022b)](/sources/li-2022-b.md) — Eq. (38) and the numerical set-up.
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §5.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §4, §4.11.
- [Wang & Don (2022)](/sources/wang-2022-b.md) — §3.3.
- [Wang et al. (2023b)](/sources/wang-2023-b.md) — §2.
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
- [Boscarino et al. (2022)](/sources/boscarino-2022.md) — §3.3.1, Ex. 5.4 (Figs. 5.4–5.5) (arXiv v2).
- [Fan et al. (2022)](/sources/fan-2022.md) — §3.
- [Fan et al. (2023)](/sources/fan-2023.md) — §2, Remark 2.2.
- [Hong et al. (2022)](/sources/hong-2022.md) — §5, §6.
- [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) — §4.
- [Liang et al. (2022)](/sources/liang-2022.md) — §3, §4.
- [Jeong et al. (2022)](/sources/jeong-2022.md) — §5.
- [Ji et al. (2022)](/sources/ji-2022.md) — §2.3, §5.
- [Lesur et al. (2023)](/sources/lesur-2023.md) — §2.3, §4.2 (Fig. 6).
- [Li et al. (2022a)](/sources/li-2022.md) — §3.4, §4.4.
- [Li et al. (2023a)](/sources/li-2023.md) — Eqs. (30)–(33), §4.2 (Thm. 5).
- [Wan & Xia (2022)](/sources/wan-2022.md) — §2 (Eqs. (2.7)–(2.9)), Ex. 4.4.
- [Chen, Wu & Xiong (2023)](/sources/chen-2023-b.md) — §3.3 (arXiv v1).
- [Chamarthi (2023a)](/sources/chamarthi-2023.md) — §3.3 (Eqs. (62)–(64)), Fig. 10 (arXiv v2).
- [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) — §2.3 (arXiv v1).
- [Chandravamsi et al. (2023)](/sources/chandravamsi-2023.md) — §5.1, App. A (arXiv v1).
- [Bezgin et al. (2023)](/sources/bezgin-2023.md) — §3.3, §5.1.2, §6 (Table 3) (arXiv v1).
- [Berta et al. (2024)](/sources/berta-2024.md) — §3.2, §3.4, §4 (step 7), §5.1 (arXiv v4).
- [Cai, Qiu & Wu (2024)](/sources/cai-2024.md) — §3.1.3 (Step 2), Remark 3.3, Ex. 5.7 (Fig. 7) (arXiv v1).
- [Liang & Fu (2024b)](/sources/liang-2024-b.md) — §2.3, §3.2 (Algorithm 1), §4.4, §4.6.
- [Chen & Fu (2024)](/sources/chen-2024.md) — §6 (Eqs. (70)–(72)), §7 (Algorithm 1, Eq. (73)), Eq. (51).
- [Chu et al. (2025a)](/sources/chu-2025.md) — §1, §2.1 (Eqs. (2.4)–(2.5)), App. A (arXiv v1).
- [Chu et al. (2025b)](/sources/chu-2025-b.md) — Remark 2.2, §3–§4, §5.1 (Eq. (5.2)), Apps. A–B.
