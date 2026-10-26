---
type: Method
title: "Jump-penalty stabilization of high-order methods"
description: "Jump-penalty stabilization adds to a high-order element method face terms that penalize the jump of the solution or of its gradient across element interfaces; it acts as localized numerical diffusion and serves as the implicit subgrid dissipation of DG and spectral/hp implicit LES of under-resolved turbulence."
status: established
aliases: [jump penalty, solution jump penalty, gradient jump penalty, gradient-jump penalisation, GJP, continuous interior penalty, edge stabilization, interior penalty stabilization]
tags: [dg, implicit-les, numerical-dissipation, spectral-element]
timestamp: 2026-10-26T07:42:00Z
---

# Jump-penalty stabilization of high-order methods

**Jump-penalty stabilization** adds to the semi-discrete form of a
high-order element method a term, integrated over the element faces, that
penalizes either the **jump of the solution** across the face (the
*solution jump penalty*, an interior-penalty term with an enlarged
parameter) or the **jump of its gradient** (the *gradient jump penalty*,
GJP, which comes from the continuous interior penalty or edge stabilization
of Burman and co-workers) ([Kou et al. 2023](/sources/kou-2023.md),
Abstract, §1). Both terms are symmetric and positive semi-definite, require
no change of the underlying scheme and are independent of the time
discretization (§1, §2.2, citing Moura et al.). In under-resolved turbulence
the jumps grow where the flow is not resolved, so the penalty acts as
localized numerical diffusion: Kou et al. state that it "acts as an
implicit subgrid model and stabilizes under-resolved turbulent simulations",
and [Slaughter et al. (2023)](/sources/slaughter-2023.md), §3, call such
stabilisations "somewhat analogous to a sub-grid scale model" whose
dissipation is "a pure characteristic of the numerical scheme" (see
[implicit LES](/definitions/implicit-les.md) and
[numerical dissipation](/properties/numerical-dissipation.md)).

Page-local symbols: $\tau_s$ and $\tau_g$ the solution and gradient penalty
parameters (Kou et al.'s symbols, kept because other pages cite them; not
related to the SGS stress $\tau_{ij}$); $\sigma_{\mathrm{IP}}$ the
three-dimensional penalty coefficient (Kou et al.'s $\sigma$); $a$ the
advection speed and $\nu$ the diffusivity of the scalar model problem; $N_e$
the number of elements of a one-dimensional mesh (Kou et al.'s $N$; $N$ is
the polynomial degree here, their $P$); $\phi_i$ the basis functions;
$\{\!\{\cdot\}\!\}$ and $[\![\cdot]\!]$ the face average and jump.

## Formulation

**One-dimensional advection–diffusion** (Kou et al. 2023, §2.1, Eqs. 7–14),
modal Legendre DG of degree $N$ on elements of size $h$. The gradient
penalty adds to the right-hand side of the equation for mode $i$ of element
$n$
$$\tau_g\,|a|\,h^2\Big[\frac{\partial\phi_i}{\partial x}(+1)\,G_{n,n+1}-\frac{\partial\phi_i}{\partial x}(-1)\,G_{n-1,n}\Big],\qquad G_{n,n+1}=\frac{\partial u_{n+1}}{\partial x}\Big|_{-1}-\frac{\partial u_n}{\partial x}\Big|_{+1},$$
and the solution penalty
$$\tau_s\,|a|\Big[\phi_i(+1)\,U_{n,n+1}-\phi_i(-1)\,U_{n-1,n}\Big],\qquad U_{n,n+1}=u_{n+1}(-1)-u_n(+1)$$
(page-local face jumps $G$, $U$, evaluated at the reference end points
$\pm1$). Both are scaled by the advection speed; Kou et al. note that a
scaling by the Péclet number $ah/\nu$ is an alternative. Combined with an
upwind flux, positive penalties increase the damping that upwinding already
provides and negative ones decrease it; large negative values make the
scheme unstable, "effectively adding anti-diffusion" (§2.1).

**Compressible Navier–Stokes in [HORSES3D](/software/horses3d.md)** (§2.2,
Eqs. 15–25). The DGSEM uses a Roe flux and the symmetric interior penalty
(SIP) viscous flux $F^{v*}\cdot\boldsymbol n=\{\!\{F^v\}\!\}\cdot\boldsymbol n+\sigma_{\mathrm{IP}}[\![\boldsymbol q]\!]$,
with no over-integration. The SIP penalty *is* the three-dimensional
solution jump penalty; it acts on a selected subset $\tilde{\boldsymbol q}=\Lambda\boldsymbol q$
of the conservative variables ($\Lambda$ page-local: momentum only for the
low-Mach Taylor–Green vortex, all five equations for the compressible
Kelvin–Helmholtz case) and is added explicitly as
$$\frac{\sigma_{\mathrm{IP}}}{Re}\int_{\partial\Omega_n}[\![\tilde{\boldsymbol q}]\!]\,\phi_i\,ds,\qquad \sigma_{\mathrm{IP}}=\tau_sRe.$$
The gradient penalty, in the general form of Moura et al., is
$$\frac{\sigma_{\mathrm{IP}}h^2}{Re}\int_{\partial\Omega_n}[\![\nabla\tilde{\boldsymbol q}]\!]\,\nabla\phi_i\cdot\boldsymbol n\,ds,$$
with $h$ the face-averaged grid size and physical (not reference)
gradients, so curved elements need the metric terms. The global penalty
matrices, with entries $\frac{\sigma_{\mathrm{IP}}}{Re}\int_\Gamma[\![\phi_j]\!][\![\phi_i]\!]$
and $\frac{\sigma_{\mathrm{IP}}h^2}{Re}\int_\Gamma[\![\nabla\phi_j]\!][\![\nabla\phi_i]\!]\cdot\boldsymbol n$
over the faces $\Gamma$, are stated to be "symmetric and positive
semi-definite and therefore provide dissipation of energy" (§2.2; no proof
given, reference to Ferrer).

**Related interior-penalty fluxes.** The interior-penalty parameter as an
implicit-LES dissipation source is also one of the three options that
[Ferrer et al. (2023)](/sources/ferrer-2023.md), §4.1, list for HORSES3D
(see [DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md)).
In a RANS context [Zhao et al. (2023b)](/sources/zhao-2023-b.md), §3.1,
Eq. (3-9), use an interior-penalty viscous flux whose penalty
$C_{\mathrm{IP}}N^2/h_f$ (page-local constant and face scale; the source
writes the polynomial order $p$) multiplies a jump-based lifting quantity,
the viscous flux evaluated with the interface jump in place of the gradient,
which avoids forming the Jacobian of the viscous flux. The
[high-order projection-based upwind method](/methods/high-order-projection-based-upwind-method.md)
of [Lederer et al. (2023)](/sources/lederer-2023.md) works on the other jump
term, the upwind penalty of the convective flux, and restricts it to the
high-order part of the velocity jump.

## Eigenanalysis and parameter choice

Kou et al. (2023, §3, App. A, App. C) perform a temporal eigensolution (von
Neumann) analysis of linear advection with the penalties, Gauss–Legendre
quadrature, $N=2,3,4$, and central or upwind flux, plotting dispersion and
dissipation against $kh/(N+1)$. Their design criterion, recalled from Moura
et al., is better dispersion at medium–high wavenumbers and more
dissipation at high wavenumbers. Findings:

- with upwind flux and $N=3$, a small **negative** $\tau_g$ reduces the
  dissipation at medium wavenumbers, a positive $\tau_g$ is too dissipative
  there, and $\tau_g<-1\times10^{-3}$ makes the dissipation positive, i.e.
  unstable (Figs. 1, 3);
- a positive $\tau_s$ reduces dissipation at medium wavenumbers and raises
  it at high wavenumbers, never destabilizes, and from the dissipation curve
  "should be as large as possible" (Figs. 2, 4); below $\tau_s=-0.5$
  anti-diffusion appears;
- as $\tau_s$ grows the DG eigenvalues split into a set converging to the
  continuous Galerkin ones and a strongly dissipative set, as recalled from
  earlier work, and the DG–CG difference in an advection test decays as
  $\tau_s^{-0.5}$ (§3, App. B);
- with a central flux, $\tau_s=0.5$ reproduces the dispersion and
  dissipation of the upwind flux, a known equivalence that the analysis
  recovers (App. C.1).

Representative parameters (Table 1, Table C.2):

| flux | $\tau_g$ at $N=2,3,4$ | $\tau_s$ |
|---|---|---|
| upwind | $-3\times10^{-3}$, $-1\times10^{-3}$, $-4\times10^{-4}$ | 0.25 |
| central | $1.2\times10^{-2}$, $4\times10^{-3}$, $2\times10^{-3}$ | 0.75 |

The magnitude of the gradient penalty falls as $N$ rises; the solution
penalty does not change with $N$.

## Turbulence tests

- **Forced Burgers turbulence** ($N_e=400$, $N=3$, Roe flux, white-in-time
  forcing up to 80 modes; §4.1, App. D): both penalties extend the resolved
  wavenumber range beyond the 1% rule of the unpenalized scheme; too large
  penalties keep excess energy at high wavenumbers and lose the $-2$
  slope; optimal values $\tau_g=-8\times10^{-4}$, $\tau_s=1.5$. The
  gradient penalty is "slightly better", keeping the $-2$ slope to higher
  wavenumbers. At $N=2$ and 4 both still improve standard DG, less so as
  $N$ grows; with a central flux, standard DG blows up and the penalties
  stabilize it.
- **[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)** ($Re=1600$,
  $M=0.1$, $32^3$ elements, $N=3$, momentum penalized; §4.2): unpenalized DG
  diverges, which the authors relate to aliasing following Gassner et al.
  For low penalties the kinetic-energy dissipation rate has a spurious
  second peak at $t/t_c=11$; it disappears for $\tau_s>1.9$, at the price of
  a first peak higher than DNS, and for $\tau_g>6.3\times10^{-4}$, the
  largest $\tau_g$ recovering the peak magnitude but oscillating later
  (Fig. 10). Both penalties are "clearly superior" to
  [Smagorinsky](/methods/smagorinsky-model.md) and
  [Vreman](/methods/vreman-model.md) models adapted to DG, which give a
  lower dissipation peak, more dissipation before $t/t_c=8$ and significant
  dissipation at mid wavenumbers (Fig. 12; model constants and filter width
  not given). The optimal penalties are "the highest tested", which eases
  the choice but "can lead to CFL-type restrictions" (§5).
- **Kelvin–Helmholtz instability** (2D, $Re=10^4$, $M=0.5$, $64^2$ elements,
  $N=3$, all equations penalized; §4.3): unpenalized DG diverges at
  $t/t_c\simeq4$; the solution penalty $\tau_s=0.01$ completes the run and
  matches a $128^2$-element, $N=5$ reference until $t/t_c=5$; the gradient
  penalty diverged for every value tried, of either sign. DG with and
  without entropy-stable formulations is stated (citing earlier work) to
  diverge on this case.
- **Wall-resolved implicit LES of a multi-element wing** (Slaughter et al.
  2023, §3.1): in the Fourier spectral/hp element solver of
  [Nektar++](/software/nektar-plus-plus.md), with spectral/hp elements in
  the plane and Fourier modes in the span, the in-plane
  discretization (orders 6/5 for velocity/pressure) is stabilized by the GJP
  of Moura et al., the spanwise direction by
  [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md).
  As relayed by the authors from Moura et al., SVV at low polynomial order
  "can be overly diffusive" and GJP "has out-performed the SVV approach on
  canonical cases but has yet to be applied to more complex geometries";
  Slaughter et al. apply it to the three-element
  [Imperial front wing](/benchmarks/imperial-front-wing.md) in ground
  effect at $Re=2.2\times10^5$, which resolves
  [laminar separation bubbles](/definitions/laminar-separation-bubble.md)
  on the suction sides. No penalty value, formula or scaling is printed,
  and no comparison with an unstabilized or SVV-only run is shown.

## Qualifications

- Evidence is numerical (eigenanalysis and simulations); no stability or
  consistency theorem is proved in either source.
- **Sign of the gradient penalty.** The one-dimensional analysis and the
  Burgers test favour a negative $\tau_g$ with an upwind flux, whereas in
  the Taylor–Green vortex positive values above $6.3\times10^{-4}$ remove
  the spurious peak; Kou et al. (§4.2) explain the larger magnitude by the
  $1/Re$ scaling but do not comment on the change of sign. With
  $\sigma_{\mathrm{IP}}=\tau_sRe$ the coefficient $\sigma_{\mathrm{IP}}/Re$
  of the face integral equals $\tau_s$ and does not depend on $Re$
  *(compiler check, not in the sources)*.
- Kou et al. (§5) write that both penalties "enhance dissipation at high
  wavenumbers", while §3 states that with the recommended negative $\tau_g$
  the high-wavenumber dissipation is "similar (or lower)" than standard
  upwinding.
- **Printed slips (Kou et al.).** After Eq. (25) the gradient penalty is
  parametrized as "$\sigma=\tau_sRe$", where $\tau_g$ is the gradient
  parameter elsewhere; the refined Burgers case $N_e=819$, $N=4$ is printed
  with 4096 degrees of freedom, against $819\times5=4095$ *(compiler check,
  not in the sources)*.
- The version of Slaughter et al. read is the Research Square preprint
  (v1); the superiority of GJP over SVV is relayed from Moura et al., not
  tested in that paper.

# Citations

- [Kou et al. (2023)](/sources/kou-2023.md) — Abstract; §1 (origins, properties); §2.1, Eqs. (1)–(14) (one-dimensional penalties); §2.2, Eqs. (15)–(25) (HORSES3D, SIP, $Re$ scaling, penalized variables); §3, App. A, App. C, Table 1, Table C.2, Figs. 1–4 (eigenanalysis, representative parameters); §4.1, App. D, Figs. 6–8 (Burgers); §4.2, Figs. 10–12 (Taylor–Green vortex, explicit models); §4.3, Figs. 13–15 (Kelvin–Helmholtz); App. B; §5.
- [Slaughter et al. (2023)](/sources/slaughter-2023.md) — Research Square preprint v1: §3 (implicit LES, stabilisation as subgrid analogue); §3.1 (GJP in the plane, SVV in the span, Nektar++).
- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — §4.1 (interior-penalty parameter as an implicit-LES dissipation source).
- [Zhao et al. (2023b)](/sources/zhao-2023-b.md) — §3.1, Eqs. (3-1)–(3-9) (interior-penalty viscous flux with jump-based lifting quantity).
- [Lederer et al. (2023)](/sources/lederer-2023.md) — §3.3 (projection of the upwind jump penalty).
