---
type: Method
title: "Subcell finite-volume shock capturing for DG"
description: "Troubled DG elements are recomputed as (N+1)^3 finite-volume subcells with the same degrees of freedom, either switched by an indicator or blended convexly with the DG operator; the blending factor has also been controlled by reinforcement learning as an implicit subgrid model."
status: established
aliases: [hybrid DG/FV, DG/FV subcell scheme, finite-volume subcell limiting, DG/FV blending, RL-Blend]
tags: [dg, numerical-dissipation, implicit-les, reinforcement-learning, compressible]
timestamp: 2026-10-25T13:42:00Z
---

# Subcell finite-volume shock capturing for DG

**Subcell finite-volume (FV) shock capturing** stabilizes a
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md) near
discontinuities by reinterpreting a troubled element of degree $N$ as
$(N+1)^d$ FV subcells carrying the same number of degrees of freedom, advanced
with a robust low-order (first- or second-order TVD) FV scheme. Two variants
appear in the sources: the **switching** scheme of the FLEXI group, in which an
element is either DG or FV ([Krais et al. 2021](/sources/krais-2021.md)), and
the **convex blending** of DG and FV operators of Hennemann et al., which
[Beck & Kurz (2023)](/sources/beck-2023.md) reinterpret as an implicit
subgrid-scale model.

## Switching hybrid DG/FV (FLEXI)

Krais et al. (2021, §2.2.3, §4, §5.7) describe the group's scheme:

- **Subcells.** In reference space the element is cut into $N+1$ equispaced
  subcells per direction of width $h_{\mathrm{sub}}=2/(N+1)$ (page-local), so
  $h_{FV}=h_{DG}/(N+1)$ in physical space; data structures and the number of
  degrees of freedom are shared with DG, which balances the cost per element.
- **Conservative transfer.** The subcell means are the integrals of the DG
  polynomial over each subcell, evaluated with $N+1$ quadrature nodes
  $\xi^k_\lambda$ mapped into subcell $k$:
  $$U^{FV}_k=\sum_{i=0}^{N}\Big(\frac12\sum_{\lambda=0}^{N}w_\lambda\,\ell_i(\xi^k_\lambda)\Big)U_i,\qquad U^{FV}=V_{DG\to FV}\,U,$$
  and the backward transfer uses $V_{FV\to DG}=V_{DG\to FV}^{-1}$ (Eqs. 57–63).
- **FV operator.** A block-structured FV update on the subcells, with the
  subcell Jacobian integrated by the midpoint rule (Eq. 64); second order by
  TVD-limited reconstruction of primitive variables. At DG/FV interfaces the
  DG face data are converted to FV points by the face version of
  $V_{DG\to FV}$, the flux is computed pointwise and transferred back (§4.2).
- **Indicator and hysteresis.** A priori troubled-cell indicators of
  Persson–Peraire, Jameson–Schmidt–Turkel or Ducros type are evaluated at the
  start of each step; an element switches to FV above an upper threshold and
  back to DG below a lower one. The two-threshold band prevents back-and-forth
  switching and reduces sensitivity to the user value; the authors state that
  "numerical studies have shown" this without data (§4.3). A posteriori
  (MOOD-like) indicators are mentioned as the alternative.
- **Time step.** The FV subcells obey
  $\Delta t\le\mathrm{CFL}\,c^{c}_{RK}(0)\,h_{FV}/\lambda^c$ (Eq. 67, factor as on
  the DGSEM page), a weaker restriction than the DG one, so the DG step governs.

**Demonstrations.** In a stationary $M=1.5$ shock interacting with a vortex
(Euler, $200\times100$ cells, fifth order, entropy-conserving Chandrashekar flux
in DG cells, JST-type pressure indicator) the FV subcells stay confined to the
shock, no spurious waves are emitted and the vortex survives past the shock
because DG is used downstream (Krais et al. 2021, §7.2, Fig. 25); 2D Riemann
problems are shown in Fig. 9.

**Cost.** In strong-scaling tests with half the domain DG and half FV, the
hybrid operator performs about 15–20% worse than pure DG and shows weaker or no
super-linear speed-up, attributed to the extra memory of the FV operator (FV
metrics, inner-face geometry, subcell distances) (§5.8). FV cells send twice the
DG data at partition boundaries (cell mean plus slope) and the slope
computation overlaps the volume integral to hide communication (§5.7).

## Convex DG/FV blending as an implicit closure

In the scheme of Hennemann et al. (as recalled by Beck & Kurz 2023, §III C,
Eq. 16), originally a provably entropy-stable subcell shock capturing for
split-form DG, each element evolves by a convex combination
$$\frac{\partial U}{\partial t}=(1-\alpha)R_{DG}(U)+\alpha R_{FV}(U),\qquad\alpha\in[0,1],$$
with $\alpha=0$ pure DG and $\alpha=1$ a compatible low-order TVD FV scheme on
subcells whose widths equal the LGL quadrature weights $w_i$ (Fig. 4). The
scheme is conservative and consistent, and elements can be blended
independently because the face fluxes coincide for DG and FV.

Beck & Kurz (2023, §III C, §V C) set $\alpha$ per element with a
[reinforcement-learning](/methods/reinforcement-learning-closure.md) policy
("RL-Blend", actions mapped to $\alpha\in[0,0.5]$) and use it as an
[implicit LES](/definitions/implicit-les.md) model, which they state had "not
been interpreted as a possible implicit SGS model alternative yet". In forced
[isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md) at 36
degrees of freedom per direction and $N=5$, pure DG is under-dissipative, pure
FV over-dissipative, and the learned blending matches the DNS spectrum closely
(Fig. 12); its rewards are comparable to those of the learned explicit
Smagorinsky closures. The authors explain the success by the location of the
dissipation: FV dissipation is concentrated at the element centre, where the LGL
subcells are largest, the inverse of DG dissipation at the faces, so blending
can homogenize the total (§V C); the explanation is stated, and the
dissipation distribution is not measured. The agent lowers $\alpha$ for $N=3$ and raises its mean for $N=5$
(Figs. 13–14). See [discretization-consistent closure](/definitions/discretization-consistent-closure.md)
and [numerical dissipation](/properties/numerical-dissipation.md).

## Convention difference

The two variants place the subcells differently: equispaced subcells of width
$2/(N+1)$ in reference space (Krais et al. 2021, Eq. 59) against subcells sized
by the LGL weights (Beck & Kurz 2023, Fig. 4). The difference is part of the
schemes, not a disagreement.

## Qualifications

- Krais et al. (2021) print two statements on the hybrid cost: "almost no
  additional computational cost compared to pure DG" (§2.2.3, §4.1) and "about
  15–20% worse than for the pure DG method" (§5.8, measured). The measured
  value is the quantitative one.
- Krais et al. (2021, Eq. 64) print the flux at face $i+\tfrac12$ with arguments
  $(U^{FV-},U^{FV-})$ while the three other faces carry $(U^{FV-},U^{FV+})$.
- Beck & Kurz (2023, Eq. 17) admit $0\le\alpha\le1$ but map the RL action to
  $[0,0.5]$ (Table I).

# Citations

- [Krais et al. (2021)](/sources/krais-2021.md) — §2.2.3; §4.1–4.4, Eqs. (56)–(67), Figs. 14–16; §5.7–5.8, Figs. 19–20; §7.2, Fig. 25.
- [Beck & Kurz (2023)](/sources/beck-2023.md) — §III C, Eqs. (16)–(17), Figs. 4–5; §V C, Figs. 8, 12–14; Table I.
