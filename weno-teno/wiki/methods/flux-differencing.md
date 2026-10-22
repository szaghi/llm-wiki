---
type: Method
title: "Flux differencing and split-form DG"
description: "Flux differencing replaces the DG volume term D f by a sum of symmetric two-point volume fluxes weighted by 2D; on diagonal-norm SBP (LGL) elements it recovers split forms, inherits entropy conservation or kinetic-energy preservation from the volume flux, admits a local flux form, and costs about N+1 times the flux evaluations of the strong form."
status: established
aliases: [flux-differencing DG, split-form DG, split-form DGSEM, two-point flux volume integral, entropy-conservative DG volume term]
tags: [dg, entropy-stable, kinetic-energy-preserving, numerical-flux, software]
timestamp: 2026-10-21T12:00:00Z
---

# Flux differencing and split-form DG

In a nodal DG element whose derivative matrix $D_d$ is a diagonal-norm
[summation-by-parts operator](/operators/summation-by-parts-operator.md),
**flux differencing** replaces the volume term $\sum_dD_d\mathbf f^{(d)}$ of the
strong form by

$$\mathrm{VOL}_i=\sum_d\sum_m2\,(D_d)_{im}\,f^{\mathrm{vol},(d)}(u_i,u_m).$$

Here $f^{\mathrm{vol},(d)}$ is a symmetric, consistent two-point *volume flux*
in direction $d$: $f^{\mathrm{vol},(d)}(u,u)=f^{(d)}(u)$ and
$f^{\mathrm{vol},(d)}(u_i,u_m)=f^{\mathrm{vol},(d)}(u_m,u_i)$. The scheme is then

$$\frac{d}{dt}\mathbf u+\mathrm{VOL}+M^{-1}\mathcal R^\top B_\partial\Big(\mathbf h-\sum_dN_d\mathcal R\,\mathbf f^{(d)}\Big)=0,$$

with $\mathbf h$ the surface numerical fluxes. This is the form of
[Ranocha et al. (2023)](/sources/ranocha-2023.md), Eq. (2.5), after Gassner,
Winters & Kopriva, with origins they trace to Tadmor, LeFloch–Mercier–Rohde,
Fisher et al., Carpenter et al. and Chen–Shu. The page-local boundary
symbols $\mathcal R$, $B_\partial$, $N_d$ are those of the SBP page.
[Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) call
the same construction the *split form* of the DGSEM (§2.1, Eqs. (2)–(7)).

## Consistency with the standard DGSEM

With the central volume flux $f^{\mathrm{vol}}=\{\!\{f\}\!\}$, flux differencing
reduces to the standard strong form. On a curvilinear element the central
flux is $\{\!\{f\cdot Ja\}\!\}$ (Rueda-Ramírez et al. (2022), Eq. (7)). The
check: $\sum_m2D_{im}\tfrac12(f_i+f_m)=f_i\sum_mD_{im}+(D\mathbf f)_i=(D\mathbf f)_i$,
because the rows of a consistent $D$ sum to zero *(compiler check, not in
the sources)*.

Other volume fluxes give the split forms of finite-difference methods
(Ranocha et al. (2023), §2, citing Gassner–Winters–Kopriva). Rueda-Ramírez
et al. (2022), §2.1, list the properties a suitable volume flux can give:

- kinetic-energy preservation;
- entropy conservation or dissipation (Ismail–Roe, Chandrashekar);
- pressure-equilibrium preservation (Shima et al.);
- several of these together.

The fluxes themselves are on
[entropy-conservative and kinetic-energy-preserving two-point fluxes](/methods/entropy-conservative-flux.md).
The finite-difference split forms they reproduce are on
[split convective forms](/methods/split-convective-forms.md).

## Properties

- **Entropy.** The scheme is entropy-conservative if the volume flux is
  entropy-conservative and the surface flux is entropy-conservative. It is
  entropy-dissipative if the surface flux is entropy-dissipative instead
  (Ranocha et al. (2023), §2, citing Carpenter et al. and Gassner–Winters–Kopriva).
  See [entropy stability](/properties/entropy-stability.md).
- **Accuracy.** For general symmetric volume fluxes the scheme keeps the
  order of accuracy of the derivative operator (Ranocha et al. (2023), §2,
  citing Chen–Shu and Ranocha). This is the route to high order with
  kinetic-energy-preserving fluxes *(compiler check, not in the sources:
  neither source relates the two results)*. It sidesteps the second-order barrier
  that [Coppola & Veldman (2023)](/sources/coppola-2023.md) prove for
  single product-form face fluxes, since the volume term is a sum of
  two-point fluxes over the element
  ([kinetic energy preservation](/properties/kinetic-energy-preservation.md)).
- **Local conservation.** Rueda-Ramírez et al. (2022), Eqs. (8)–(11), write
  the whole DGSEM, surface terms included, as inter-node flux differences.
  In the first direction, with unit Jacobian for brevity, the scheme reads
  $\mathsf w_i\frac{d}{dt}u_i=\hat f^{\mathrm{DG}}_{(i-1,i)}-\hat f^{\mathrm{DG}}_{(i,i+1)}$.
  The outer fluxes $\hat f^{\mathrm{DG}}_{(-1,0)}$ and $\hat f^{\mathrm{DG}}_{(N,N+1)}$
  are the surface numerical fluxes. The inner ones follow recursively from
  the volume terms, $\hat f^{\mathrm{DG}}_{(0,1)}=-F^{\mathrm{vol}}_0$ and
  $\hat f^{\mathrm{DG}}_{(i,i+1)}=\hat f^{\mathrm{DG}}_{(i-1,i)}-F^{\mathrm{vol}}_i$
  for $i=1,\dots,N-1$, with page-local $F^{\mathrm{vol}}_i=-\sum_mS_{im}f^{\mathrm{vol}}(u_i,u_m)$ and
  $S=2Q-B$. The authors note that these fluxes differ slightly from Fisher &
  Carpenter's because the surface terms are transformed too (§2.1). The flux
  form gives subelement-wise conservation in the
  [Lax–Wendroff](/results/lax-wendroff-theorem.md) sense. It is what allows
  [subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md)
  to blend DG and finite-volume fluxes at each subcell interface.

## Efficient evaluation

Ranocha et al. (2023) collect the implementation identities and measure
each one in [Trixi.jl](/software/trixi-jl.md) and [FLUXO](/software/fluxo.md).

1. **Absorbing the surface correction.** With
   $\widetilde D_d=2D_d-M^{-1}\mathcal R^\top B_\partial N_d\mathcal R$ and
   diagonal $M$ and boundary operator, consistency of $f^{\mathrm{vol}}$
   cancels the $-N_d\mathcal R\mathbf f^{(d)}$ term. The scheme becomes
   $\frac{d}{dt}\mathbf u+\sum_d\sum_m(\widetilde D_d)_{im}f^{\mathrm{vol},(d)}(u_i,u_m)+M^{-1}\mathcal R^\top B_\partial\mathbf h=0$,
   the flux-differencing analogue of the weak form, with no pointwise flux
   evaluation at surface nodes (§2.1, Eqs. (2.7)–(2.10)).
2. **Skew-symmetry.** $M\widetilde D_d$ is skew-symmetric (Eq. (2.11)), so
   $(\widetilde D_d)_{ii}=0$. With symmetric fluxes only the pairs $i<m$ are
   evaluated, which "saves more than half" of the volume-flux evaluations
   (§2.2). In 1D, $M\widetilde D=2Q-B=S$, the split-form matrix of
   Rueda-Ramírez et al. (2022) *(compiler check, not in the sources)*.
3. **Curvilinear elements.** The curvilinear SBP operator gives
   $(D_d)_{im}=J_i^{-1}\sum_n\{\!\{Ja^{(n)}_d\}\!\}_{im}(D_{n,\xi})_{im}$, with the
   metric terms averaged between nodes $i$ and $m$ (Eq. (2.17)). Rueda-Ramírez
   et al. (2022), Eq. (6), use the same averaged metrics in the contravariant
   two-point flux. Reordering the sums turns the volume term into one
   *directional* volume flux per reference direction $n$, taken along the
   averaged contravariant vector $\{\!\{Ja^{(n)}\}\!\}_{im}$. This keeps the
   sparsity of the tensor-product operators, which the Cartesian-flux form
   (2.18) loses (§2.3, Eq. (2.19)).
4. **Directional fluxes.** Directional fluxes should be coded directly
   rather than through rotation to the first coordinate direction (§4.2,
   Table 2). Free-stream preservation on curved meshes still needs the usual
   care with the metric terms (§2.3;
   [free-stream preservation](/properties/free-stream-preservation.md)).

### Cost

On tensor-product LGL elements of degree $N$ in $d$ dimensions, the strong
form needs $d(N+1)^d$ flux evaluations per element, and flux differencing
needs $O(d(N+1)^{d+1})$. Both need $O(d(N+1)^{d+1})$ floating-point
operations without the fluxes (Ranocha et al. (2023), §2, Table 1).

The authors measure cost by the performance index PID, the wall-clock time
of one evaluation of the semi-discretization divided by the number of DG
nodes (Def. 4.1). It counts one node as one degree of freedom, not node
times variable. Their findings:

- **Against overintegration.** Overintegration interpolates to a higher
  degree, applies the weak form there and projects back. In 3D with the
  Shima et al. flux, flux differencing is cheaper than any overintegration
  for $3\le N\le5$. With the entropy-conservative flux it lies between
  overintegration to degree $N+1$ and $N+2$ for $N\in\{3,4\}$ (§5, Fig. 2).
  In 3D at $N\le3$, the most relevant case for CFD, flux differencing can be
  faster than overintegration with one extra node per direction (§5, §9).
- **Robustness.** Ranocha et al. state, citing earlier work, that flux
  differencing stays stable where overintegration fails, and that
  overintegration costs about a factor two in explicit time step (§5).
- **SIMD.** With an array-of-structures-of-arrays layout, precomputed
  primitive variables and logarithms, and explicit vectorization, the volume
  terms reach vectorization ratios of 98.36–99.26 % and 20.69–29.09 % of the
  FMA peak at $N=3$ on an Intel Core i7-8700K (§8, Table 3). The total
  speed-up is 20 % to 3× in 2D and 30 % to 3× in 3D (Figs. 10–11).
- **Best timings.** The best 3D PIDs at $N=3$ are
  $2.6\times10^{-8}$ s (Cartesian) and $4.3\times10^{-8}$ s (curved,
  unstructured) with the Shima et al. flux, and $4.2\times10^{-8}$ s and
  $6.5\times10^{-8}$ s with the Ranocha entropy-conservative flux (§9).

## Gauss-node variant

On Legendre–Gauss nodes the volume nodes exclude the boundary. Entropy
stability then requires the hybridized SBP operator and an *entropy
projection*: the surface states are computed from the interpolated entropy
variables, $\tilde u=u(\mathcal Rw(\mathbf u))$ (Ranocha et al. (2023), §6,
Eqs. (6.1)–(6.3)).

- **Run-time breakdown.** Flux differencing takes 66–91 % of the run time in
  2D and 65–89 % in 3D. The entropy projection takes 4–14 % (Fig. 3).
- **Cost relative to LGL.** The Gauss scheme is 1.5× to 5× more expensive
  than LGL-DGSEM, with the gap closing at high order in 3D (Fig. 4).
- **Self-correction.** An earlier estimate by Chan and co-workers, that a
  degree-$N$ Gauss scheme costs about as much as a degree-$(N+1)$ LGL
  scheme, "was optimistic" because it ignored the projection, face
  interpolation and lifting (§6, footnote 4). J. Chan is an author of both
  papers.

## Qualifications

- The cost figures are single-core CPU measurements on the compressible
  Euler equations. MPI and non-conservative terms are deferred to other work
  (Ranocha et al. (2023), §9).
- Ranocha et al.'s §4.2 prose ranges for the flux microbenchmarks do not
  match their Table 2 throughout *(compiler check, not in the sources:
  ratios computed from the printed timings)*. The text says the Cartesian flux is 5–20 %
  faster than the directional one, but the table gives +27 % for the Shima
  flux in 3D and a faster directional HLL flux in 3D. The text puts the
  precomputed rotated flux up to 2× slower, but the table's largest ratio is
  1.55. The table is the measurement.

# Citations

- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — §2 Eq. (2.5) and Table 1, §2.1–2.3 Eqs. (2.7)–(2.19), §4.2 Table 2, §5 Fig. 2, §6 Eqs. (6.1)–(6.3) Figs. 3–4, §8 Table 3, §9.
- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — §2.1 Eqs. (2)–(11).
- [Coppola & Veldman (2023)](/sources/coppola-2023.md) — §6.1 Observation 9.
