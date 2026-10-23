---
type: Property
title: "Free-stream preservation"
description: "A discretization on curvilinear or moving grids is free-stream preserving when a uniform state stays an exact discrete steady solution, which requires discrete metric identities; the page covers DGSEM and subcell metrics, warped-mesh tests, geometric conservation laws on moving meshes, constant states under divergence-free transport, gradient-based finite differences, and an untested TENO claim."
status: established
aliases: [freestream preservation, free-stream preserving, discrete metric identities, geometric conservation law, GCL, watertight subcell discretization, constant-state preservation]
tags: [dg, finite-difference, limiting, entropy-stable, reconstruction]
timestamp: 2026-10-23T23:00:00Z
---

# Free-stream preservation

On a curvilinear grid the physical fluxes enter the scheme combined with
the metric terms, the Jacobian $J$ and the contravariant metric terms
$Ja^{(n)}$. A scheme is **free-stream preserving** when every constant state
remains an exact discrete steady solution, so that the metric discretization
creates no spurious residual. In the sources the property is secured by
discrete *metric identities*, algebraic conditions on the discrete metric
terms that make the residual of a constant state vanish.

## Nodal DG

In the [DGSEM](/methods/dgsem.md), the metric terms are computed at the LGL
nodes by applying the derivative matrix to the node coordinates
([Ranocha et al. (2023)](/sources/ranocha-2023.md), Eqs. (2.12)–(2.13)).
They enter the curvilinear SBP operator
$D_{d,x}=\tfrac12J^{-1}\sum_n\big(Ja^{(n)}_dD_{n,\xi}+D_{n,\xi}Ja^{(n)}_d\big)$
(Eq. (2.14)). In [flux differencing](/methods/flux-differencing.md) they are
averaged between node pairs in the two-point flux, as
$\{\!\{Ja^{(n)}\}\!\}_{(i,m)}$ (Eq. (2.17);
[Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md),
Eq. (6)). Ranocha et al. reorder the sums into directional volume fluxes.
They note that "the usual care must be taken to ensure free-stream
preservation" when the contravariant vectors are computed, and cite the
literature for it rather than proving it (§2.3).

[Pazner (2021)](/sources/pazner-2021.md) states the condition and proves
its effect. With $G$ the diagonal matrix of nodal Jacobians and $GJ^{-1}$
the nodal metric terms (Pazner's notation, page-local), the discrete metric
identity of Kopriva, as the author recalls it, is
$\sum_iD_{i}\,(GJ^{-1})_{ij}=0$ for every $j$, with $D_i$ the
tensor-product weighted derivative in direction $i$ (Eq. (22)).

- **Strong form.** Under the identity, the strong-form DGSEM gives
  $\frac{d}{dt}u=0$ for every spatially constant flux (Prop. 3).
- **Weak form.** The weak form is in general not free-stream preserving,
  for example on curved meshes. Pazner therefore takes the strong form as
  the high-order target of Pazner's limiter (§2.4.2).

[Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) show where the
identity enters the entropy analysis on 3D curvilinear hexahedra. The
element entropy balance of the split-form DGSEM contains a residual equal
to the entropy flux potential contracted with the discrete divergence of
the metric terms. It vanishes when the discrete metric identities hold,
e.g. for metrics computed as a discrete curl (App. C.1, Lemma 4,
Eq. (145)). Free-stream preservation is therefore a prerequisite of their
entropy conservation and stability proofs, as they state after Hennemann
et al. (§6.1).

## Subcell metric identities

The [subcell finite-volume](/methods/subcell-finite-volume-limiting.md)
scheme that is blended with the DGSEM needs its own normals. Without them,
it would neither be watertight nor preserve free streams on high-order
curved elements. Rueda-Ramírez et al. (2022) recall the normals of Hennemann
et al., derived from the subcell flux form of the DGSEM (§2.2, Eq. (14)). In
the first direction, on grid line $j$, they read

$$n_{(i,i+1)j}=(Ja^{(1)})_{0j}+\sum_{l=0}^{i}\sum_{m=0}^{N}Q_{lm}(Ja^{(1)})_{mj},$$

with $Q=MD$ the SBP matrix, and similarly in the second direction. These
unnormalized subcell-interface normals (page-local symbol $n_{(a,b)}$) give
free-stream preservation and satisfy the discrete subcell metric identities

$$\frac{n_{(i-1,i)j}-n_{(i,i+1)j}}{\mathsf w_i}+\frac{n_{i(j-1,j)}-n_{i(j,j+1)}}{\mathsf w_j}=0 .$$

The source obtains these identities by evaluating a constant state in the
subcell scheme (Eq. (15)). Rueda-Ramírez et al. (2021) give the 3D form of
the same normals and use them for the non-conservative GLM-MHD terms as
well (App. C.2, Eq. (150)). The normals are symmetric. On element
boundaries they reduce to the surface-scaled normals, pointing along the
reference coordinates rather than outward. They make the subcell
finite-volume scheme watertight, and its entropy-balance residual vanishes
under the DG metric identities (Lemma 5): inserting (150) turns the
residual into the discrete divergence of the metric terms, Eq. (145). The
normals and their watertightness are taken from Hennemann et al.
The finite-volume flux through each subcell face is
$\lVert n_{(a,b)}\rVert\,h\big(u_a,u_b;n_{(a,b)}/\lVert n_{(a,b)}\rVert\big)$
(Eq. (13)). For a constant state, consistency of $h$ reduces the residual
to $f(u)$ dotted into the left-hand side of the identity. The residual
therefore vanishes exactly when the identity holds *(compiler check, not in
the sources)*.

**Pazner's corrected metrics.** Pazner (2021) builds a low-order
scheme from the sparse first-order operator $\widehat Q$
([summation-by-parts operator](/operators/summation-by-parts-operator.md)).
That operator cannot differentiate the metric terms exactly, so the metric
identities fail for it, and with them free-stream preservation (§3). Pazner
perturbs the metric terms, $\widehat{GJ^{-1}}=GJ^{-1}+C$ with page-local
correction $C$, so that the sparse weak form reproduces the boundary normals
for a constant state (Eq. (25)). This is an underdetermined linear system,
Eqs. (26)–(27). Its operator has the constants as null space, so it is
solvable when the right-hand side sums to zero. The sum vanishes by (P1),
the SBP column sums and the metric identity (22) (Eq. (28)). Pazner takes
the minimum-norm solution from a singular-value decomposition precomputed
on the reference element, and the perturbation is $O(h)$ entrywise. The
corrected low-order scheme is conservative and constant-preserving
(Prop. 4). For variable-velocity advection the same correction must also
enforce a discrete divergence-free condition on the velocity,
$\sum_j\hat c_{ij}\cdot\beta_j=0$ (page-local velocity $\beta_j$ at node
$j$); the procedure for this is not given (§3.3).

**Proposition 2** (Rueda-Ramírez et al. (2022), §3, Eqs. (35)–(36)). In
Pazner's sparse invariant-domain-preserving DG method, the modified metric
terms must satisfy a conservation condition, $\sum_{j\in N(i)}\hat c_{ij}=0$
over the low-order stencil (page-local graph coefficients $\hat c$). With
$\hat c$ built from the Hennemann et al. normals, that sum is
$\tfrac12\mathsf w_i\mathsf w_j$ times the left-hand side of the subcell metric
identity. The Hennemann et al. normals are therefore exact analytic
solutions of Pazner's condition, and the singular-value-decomposition
minimisation Pazner used to find the modified metrics is unnecessary.
The authors present this as a simplification of Pazner's construction, not
a correction.

## Evidence on warped meshes

Rueda-Ramírez et al. (2021) test the blended DGSEM–subcell scheme on a
heavily warped 3D mesh of $10^3$ elements, geometry degree 4, with a
uniform GLM-MHD state ($\rho=1$, $v=(0.1,-0.2,0.3)$, $p=1$, $B=(1,1,1)$).
The blending coefficient $\alpha$ is drawn at random per element and per
Runge–Kutta stage; $N=4$, CFL 0.1, $t=1$ (§6.1, Eqs. (91)–(94)). The
$L^2$ norm of $\partial_tu$ is $10^{-13}$–$10^{-12}$ at $t=0$. At $t=1$ the
deviation is about $10^{-13}$ with the entropy-conservative surface flux
and $10^{-14}$–$10^{-15}$ with the entropy-stable and TVD-ES fluxes
(Table 1; [TeCNO schemes](/methods/tecno-scheme.md)). Free streams are
kept for random element-wise blends; the subcell metrics (150) and the
discrete metric identities are the ingredients of the proofs in App. C.

## Mixed degrees and finite-volume subcells

[Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) test a hybrid
that couples three things on one curved mesh: Gauss-node
[DGSEM](/methods/dgsem.md) elements of different degrees, joined at faces
by interpolation to the higher degree and modal truncation back, and
elements switched to a finite-volume scheme on $N_{\mathrm{FV}}^d$
equidistant subcells (page-local $N_{\mathrm{FV}}$ per direction;
[h- and hp-adaptation](/methods/hp-adaptation.md)). The subcell metric
terms are the subcell integral means of the DG metric fields,

$$J^{\mathrm{FV}}=\frac{\int_eJ\,d\xi}{\int_ed\xi},\qquad (Ja^{(d)})^{\mathrm{FV}}=\frac{\int_eJa^{(d)}\,d\xi}{\int_ed\xi},$$

for each subcell $e$ (page-local), i.e. the DG-to-subcell transfer
operator applied to the DG metrics (§4.1, Eqs. (19)–(21)). The paper
states no discrete metric identity for these terms; the evidence is a
test (§8.1). A constant state $u=(1,1,1,1,1)$ on a periodic cube distorted
by $x\mapsto x+0.1\sin x_1\sin x_2\sin x_3$, with geometry degree 2, one
half covered by a checkerboard of $N=2$ and $N=7$ DG elements and the
other half by finite-volume elements with $N_{\mathrm{FV}}=15$, is run to
$t=0.5$ (165 steps). The $L^2$ errors of the five conserved variables are
$7.79\times10^{-16}$ to $3.37\times10^{-15}$ and the $L^\infty$ errors
$6.35\times10^{-14}$ to $2.89\times10^{-13}$ (Eq. (39), Table 1), from
which the authors conclude free-stream preservation on curved meshes.
The test covers DG/DG faces of different degrees and DG/FV faces at
once; it does not separate them.

## Moving meshes: geometric conservation laws

On a mesh that moves in time, a uniform state must also survive the mesh
motion. [Duan & Tang (2022)](/sources/duan-2022.md) and
[Li, Duan & Tang (2022)](/sources/li-2022-c.md) write the law in
time-dependent curvilinear coordinates together with the volume
conservation law (VCL), $\partial_\tau J+\sum_k\partial_{\xi_k}(J\partial_t\xi_k)=0$,
and the surface conservation laws (SCLs),
$\sum_k\partial_{\xi_k}(J\partial_{x_j}\xi_k)=0$ (Duan & Tang, Eq. (2.9); Li,
Duan & Tang, Eq. (2.3); [adaptive moving mesh](/methods/adaptive-moving-mesh.md)).
As Duan & Tang recall, these identities make constant states exact
solutions of the transformed equations (§2). Discretely, in both papers:

- the SCL metric terms are written in conservative cross-product form with
  the same central difference, of order $2n_{\mathrm o}$ (page-local, as
  on [flux differencing](/methods/flux-differencing.md)), as the
  entropy-conservative flux, which gives the discrete SCLs (Li, Duan &
  Tang, Eq. (3.9); Duan & Tang, Eq. (3.17));
- the time metric is computed from the mesh velocity as
  $J\partial_t\xi_k=-\sum_j\dot x_j\,J\partial_{x_j}\xi_k$, which gives the
  semi-discrete VCL (Li, Duan & Tang, Eq. (3.10); Duan & Tang, Eq. (3.18)),
  page-local computational coordinates $\xi_k$ and computational time
  $\tau$.

Li, Duan & Tang state that the fully discrete scheme with SSP-RK3 then
preserves free streams, proved by Duan & Tang (Remark 3.1). As recalled
from Visbal & Gaitonde, violating free-stream preservation "causes large
errors and instabilities" for high-order schemes (§3.2).

**The proof** (Duan & Tang (2022), §3.3, Prop. 3.2). The proof for the
high-order finite-difference case, which Li, Duan & Tang defer to "Duan &
Tang", is in this paper:

1. *Discrete SCLs.* The metrics are written in divergence
   (cross-product) form, e.g.
   $J\partial_{x_1}\xi_1=\partial_{\xi_3}(x_3\,\partial_{\xi_2}x_2)-\partial_{\xi_2}(x_3\,\partial_{\xi_3}x_2)$,
   and every derivative is replaced by the same central operator
   $\delta_k a_i=\tfrac12\sum_nc_n(a_{i+n\mathbf e_k}-a_{i-n\mathbf e_k})$
   (page-local coefficients $c_n$, those of the entropy-conservative flux
   combination; [flux differencing](/methods/flux-differencing.md)). The
   discrete SCLs then hold exactly, because the directional operators
   commute, $\delta_j\delta_k=\delta_k\delta_j$ (Eqs. (3.15)–(3.17), after the
   conservative metric method of Thomas & Lombard). In 2D the metrics
   reduce to central differences of the node coordinates (App. B); in 1D
   the SCL holds automatically (App. A).
2. *Discrete VCL.* The temporal metrics are
   $J\partial_t\xi_k=-\sum_j\dot x_j\,J\partial_{x_j}\xi_k$ at the nodes, and
   $J$ is advanced by the same flux combination applied to the averaged
   temporal metrics (Eqs. (3.5), (3.8), (3.18)).
3. *Forward Euler.* With $u^n_i=u_0$ everywhere, the update gives
   $J^{n+1}_i=J^n_i-\sum_k\frac{\Delta t}{\Delta\xi_k}\,\delta_k[J\partial_t\xi_k]$
   and $(Ju)^{n+1}_i=J^{n+1}_iu_0$, so the state stays $u_0$; explicit
   SSP Runge–Kutta methods are convex combinations of forward-Euler steps,
   which extends the result (Prop. 3.2).
4. *Entropy-stable dissipation.* The dissipation of their TeCNO-type flux
   acts on jumps of reconstructed entropy variables and vanishes for a
   constant state, so the entropy-stable scheme preserves free streams too
   (Remark 4.1; [TeCNO schemes](/methods/tecno-scheme.md)).

Discrete GCLs are also needed for the discrete entropy conservation of the
moving-mesh scheme (Duan & Tang, Remark 2.1, Thm. 3.2;
[entropy stability](/properties/entropy-stability.md)). Neither paper
prints a free-stream test; the property is proved, and the accuracy tests
on moving meshes reach the design orders (Duan & Tang, Exs. 6.1, 6.7).

**Appending the GCL as a conserved equation.**
[Ramani & Shkoller (2023)](/sources/ramani-2023.md) take a third route in
their finite-difference WENO arbitrary-Lagrangian–Eulerian scheme on
meshes moved by smooth adaptive meshing
([adaptive moving mesh](/methods/adaptive-moving-mesh.md); arXiv v2). They
append the geometric conservation law $\partial_tJ-\partial_{\xi_j}(\text{cofactor}\cdot\partial_t\mathsf X)=0$
(page-local mesh map $\mathsf X$) to the Euler system as a fifth conserved
equation, discretized with the same fluxes, and evolve $J$ with it instead
of recomputing it from the determinant (§6.1.3, Eqs. (44)–(46)). The
cofactor metrics are fourth-order central differences of $\mathsf X$, and
every interface velocity is the fourth-order linear average
$(-\mathsf b_{i-1}+7\mathsf b_i+7\mathsf b_{i+1}-\mathsf b_{i+2})/12$ of a quantity $\mathsf b$ (page-local); for a constant
state the scheme is then linear in the data, which is their argument for
free-stream preservation (§6.2.1, Eqs. (49)–(51)). On a mesh oscillating
as $\mathsf X_1=\xi_1+0.4\sin(3\pi t/T)\sin(\tfrac{3\pi}8(\xi_2+8))$ and
$\mathsf X_2=\xi_2+0.8\sin(3\pi t/T)\sin(\tfrac{3\pi}8(\xi_1+8))$ on
$[-8,8]^2$, $50\times50$, uniform data stay uniform to
$\lVert\rho-1\rVert_{L^\infty}=9.10\times10^{-14}$ at $T=80$ (Eq. (52)). The
authors take the GCL as equivalent to free-stream preservation for their
system (§6.1.3) and state that "many standard schemes (including WENO)
fail to preserve the free-stream" on dynamic adaptive meshes (§6.1.3);
the sources above instead distinguish the GCL from the discrete metric
identities that a nonlinear reconstruction can break.

## Constant states under variable-velocity transport

A related property holds on Cartesian grids for
$\partial_tu+\nabla\cdot(v\,u)=0$ with a given divergence-free velocity
field $v$: a constant $u$ is an exact solution, and a
scheme preserves it only if its discrete velocity is discretely
divergence-free. Pazner (2021) notes this for the corrected low-order
scheme above (§3.3). [Calhoun, Chudzik & Helzel (2023)](/sources/calhoun-2023.md)
prove it for the third-order Cartesian [Active Flux](/methods/active-flux.md)
method (§4.2–4.3; arXiv v2):

- for solid-body rotation, with exact characteristics, the flux of a
  constant through an $x$-edge depends only on $y$ and through a $y$-edge
  only on $x$, so the flux differences cancel (Remark 4.1);
- for a time-dependent swirl, the velocity at each edge midpoint is the
  centred difference of the stream function between the two ends of the
  edge, and the flux freezes the velocity at the edge midpoint; the update of a constant then reduces to
  differences of the stream function at the four cell corners that cancel
  exactly (Thm. 4.2, Eqs. (25)–(28));
- on adaptively refined grids with global time stepping the coarse flux at
  a coarse–fine edge equals the mean of the two fine fluxes, and the
  property survives (Cor. 4.3);
- with subcycling the intermediate-time fine fluxes are not balanced by
  coarse fluxes: constant data on levels 3–4 have error $10^{-13}$ at
  $t=1$ against about $10^{-16}$ without subcycling (§4.3).

The mechanism is a discrete stream function, not a metric identity; the
role it plays, a discrete divergence-free condition, is the one of the
surface conservation laws on curvilinear grids *(compiler check, not in
the sources)*.

## Gradient-based finite differences on curvilinear and deforming grids

[Chandravamsi et al. (2023)](/sources/chandravamsi-2023.md) give a recipe
for the gradient-based reconstruction schemes MEG6 and MIG4
([gradient-based reconstruction](/methods/gradient-based-reconstruction.md))
on 3D multi-block, static and deforming curvilinear grids, a
cell-centred conservative finite-difference setting in which interface
states are reconstructed in characteristic variables, limited and fed to
HLLC (§3, §5.1). Page-local: $\xi,\eta,\zeta$ the computational
coordinates with unit spacing, $\hat\xi_x=\xi_x/J$ etc. the
Jacobian-scaled metrics (their $J$ is the inverse of the registry's $J$:
$1/J$ is the cell-volume measure), $x'_i$, $x''_i$ the first and second
derivatives of the scheme's gradient operator (explicit sixth-order for
MEG6, fourth-order compact for MIG4). The recipe (§7, Eqs. (36)–(38)):

1. use the conservative metrics of Thomas & Lombard,
   $\hat\xi_x=(y_\eta z)_\zeta-(y_\zeta z)_\eta$ and cyclic forms (Eq. (10));
2. compute every metric derivative with the scheme's own interface
   interpolation in its *linear* form, no limiter and the average of the
   left and right states, e.g.
   $x_{i+1/2}=\tfrac12\big[x_i+\tfrac12x'_i+\tfrac1{12}x''_i+x_{i+1}-\tfrac12x'_{i+1}+\tfrac1{12}x''_{i+1}\big]$
   and $(x_\xi)_i=x_{i+1/2}-x_{i-1/2}$;
3. interpolate the metrics to the interfaces with the same averaged
   formula, treating $\xi_x/J$ as a single quantity.

The three discrete metric identities
$\partial_\xi\hat\xi_x+\partial_\eta\hat\eta_x+\partial_\zeta\hat\zeta_x=0$ (and
in $y$, $z$; Eq. (39)) then hold. For MEG6 the derivative of $y_\xi z$ is an
11-point central stencil,
$\frac1{2880}\big[2282(y_{i+1}-y_{i-1})-546(y_{i+2}-y_{i-2})+89(y_{i+3}-y_{i-3})-3(y_{i+4}-y_{i-4})-(y_{i+5}-y_{i-5})\big]z_i$
(Eq. (41)), and the cancellation of the full sum (Eq. (43)) is carried out
in a supplementary Mathematica notebook; the paper prints the proof for
MEG6 and states that MIG4 follows the same steps. The authors add that
any other metric interpolation fails the identities for this scheme
(§7). The construction builds on Nonomura et al., who showed, as recalled,
that the Visbal–Gaitonde procedure does not preserve free streams for
WENO because of the nonlinear reconstruction (§1, §7). The 11-point
stencil coefficients follow from the sixth-order explicit gradient, the
second-derivative formula and the averaged interface value
*(compiler check, not in the sources)*.

**Moving grids.** With analytic grid velocities, temporal metrics from
the chain rule, $\xi_t=-(x_t\xi_x+y_t\xi_y+z_t\xi_z)$, and the
geometric-conservation form $(1/J)_t=-\big[(\xi_t)_\xi+(\eta_t)_\eta+(\zeta_t)_\zeta\big]$,
recomputed every step, the schemes are free-stream preserving on deforming
grids (§4.2, Eqs. (11)–(14)). The last relation plays the role of the volume
conservation law of the moving-mesh section below *(compiler check, not in
the sources)*.

**Evidence** (§8; non-FP = non-conservative metrics with fourth-order
central derivatives, App. D):

| test | grid | FP metrics | non-FP metrics |
|---|---|---|---|
| uniform flow, $M=0.5$, $t=10$ | $20^3$, sinusoidal | $L_2(v_2,v_3)$ from $3.1\times10^{-16}$ to $1.3\times10^{-14}$ | $8.2$–$8.6\times10^{-3}$ |
| same | $20^3$, randomized by 20 % | same range | 0.121–0.386 |
| uniform flow on a deforming sinusoidal grid | $32^3$ | $2.3$–$3.2\times10^{-15}$ | $2.88$–$2.93\times10^{-3}$ |
| [isentropic vortex](/benchmarks/isentropic-vortex.md), one period | $64^2$, centre randomized, included angle up to about 160° | vortex and swirl profile kept | unphysical after one period |
| [double Mach reflection](/benchmarks/double-mach-reflection.md) | $768\times256$, centre randomized by up to 50 %, angle about 200° | unaffected by the distortion | rough patches, smaller for MIG4 |

(Table 2, Figs. 8–10.) Conservative metrics computed with the fourth-order
central scheme instead of the scheme's own interpolation also fail
(§8.1.1). A stationary vortex on a deforming $32^3$ grid stays intact over
eight deformation cycles, and a viscous double shear layer on a deforming
$360^2$ grid matches a stationary run in kinetic energy and enstrophy
(§8.2.2–8.2.3, Figs. 11–12). The metric arrays are 71 of the 117 arrays the
GPU version stores, about 60 % of its memory (§9.4).

## Finite-difference reconstruction schemes

[Ye et al. (2022)](/sources/ye-2022.md) argue that [AFTENO](/methods/afteno.md)
has an advantage over flux-splitting TENO. Because it interpolates states
and evaluates a two-point flux plus derivative corrections, they claim it
keeps free streams better (§1, §4.2, §5). They also say the extra cost of
the interpolation-based flux, about three times TENO5, buys this property.
The paper contains no curvilinear-grid test, so the claim is untested in
the source.

## Qualifications

- **Who proves what.** Ranocha et al. (2023) and Rueda-Ramírez et al.
  (2022) cite free-stream preservation from the literature for the DGSEM
  and the subcell normals. Ye et al. (2022) assert it without a test.
  Pazner (2021) proves it for the strong-form DGSEM and for the author's corrected
  low-order scheme (Props. 3–4), and Rueda-Ramírez et al. (2021) prove
  that the curvilinear entropy-balance residuals vanish under the metric
  identities and show free-stream preservation numerically. Li, Duan &
  Tang (2022) cite the proof for moving meshes; Duan & Tang (2022) give it
  (Prop. 3.2), and Mossier et al. (2022) show it numerically for
  mixed-degree DG with finite-volume subcells, without a proof. Ramani &
  Shkoller (2023) argue it from linearity and test it on a moving mesh;
  Calhoun et al. (2023) prove constant-state preservation for their
  variable-velocity Active Flux schemes (Thm. 4.2, Cor. 4.3).
- **Chandravamsi et al.'s proof.** The metric-identity cancellation is
  shown symbolically, partly in a supplementary notebook, for MEG6 only;
  for MIG4 it is asserted (§7). The first lines of their Eqs. (41)–(42)
  print the two interface values summed where Eq. (37) and the final
  lines of the same equations take their difference; Eqs. (17)–(18) of
  the gradient operators likewise print sums inside the brackets where
  differences are meant, as the exactness of the printed coefficients on
  linear data shows *(compiler check, not in the sources)*.
- **Strong and weak forms.** Pazner's statement that the weak form (14)
  "will not in general" preserve constants ("e.g. curved meshes", §2.4.2)
  is not a conflict with the strong–weak equivalence of Ranocha et al.
  (2023), Eq. (2.6), but a difference in how the face normals enter. Ranocha
  et al. derive (2.6) from the SBP property (2.2), whose boundary operator
  $\mathcal R^\top B_\partial N_d\mathcal R$ already carries the normals.
  Pazner's strong form (15) carries the face normals separately, in
  $\hat F_e-F_e\cdot n$, next to the volume metric terms $GJ^{-1}$. *(Compiler
  check, not in the sources: by the SBP column sums the two discrete forms
  differ by the boundary values of the contravariant flux against
  $F_e\cdot n$; they coincide when the face normals equal the volume metric
  terms at the boundary nodes and differ when the normals are computed
  otherwise.)*
- **Numbering.** Rueda-Ramírez et al. (2022) cite Pazner's sparsified
  matrix as Pazner's Eq. (34) and the conservation condition as Eq. (35). In the
  arXiv v1 of Pazner (2021) read here they are Eq. (23) and the first item
  of Prop. 5. The difference is one of versions.

# Citations

- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — §2.1 Eq. (6), §2.2 Eqs. (13)–(15), §3 Prop. 2 Eqs. (35)–(36).
- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — §2.3 Eqs. (2.12)–(2.19).
- [Ye et al. (2022)](/sources/ye-2022.md) — §1, §4.2, §5.
- [Pazner (2021)](/sources/pazner-2021.md) — §2.4 Eq. (22) Prop. 3, §3.1 Eqs. (25)–(29) Props. 4–5, §3.3 (arXiv v1).
- [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) — §6.1 Eqs. (91)–(94) Table 1, App. C Lemmas 4–5 Eqs. (145), (150) (arXiv v1).
- [Li, Duan & Tang (2022)](/sources/li-2022-c.md) — §2 Eq. (2.3), §3.2 Eqs. (3.9)–(3.10), Remark 3.1 (arXiv v1).
- [Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) — §4.1 Eqs. (19)–(21), §8.1 Eq. (39), Table 1.
- [Duan & Tang (2022)](/sources/duan-2022.md) — §2 Eq. (2.9), Remark 2.1, §3.3 Eqs. (3.5), (3.8), (3.15)–(3.18), Prop. 3.2, Thm. 3.2, Remark 4.1, App. A–B, Exs. 6.1, 6.7 (arXiv v1).
- [Chandravamsi et al. (2023)](/sources/chandravamsi-2023.md) — §1, §3, §4.2 Eqs. (10)–(14), §5.1, §7 Eqs. (36)–(44), §8.1–8.2 Table 2 Figs. 8–12, §9.4, App. D (arXiv v1).
- [Ramani & Shkoller (2023)](/sources/ramani-2023.md) — §6.1.3 Eqs. (44)–(46), §6.2.1 Eqs. (49)–(52) (arXiv v2).
- [Calhoun, Chudzik & Helzel (2023)](/sources/calhoun-2023.md) — §4.2–4.3, Remark 4.1, Thm. 4.2, Cor. 4.3, Eqs. (25)–(28) (arXiv v2).
