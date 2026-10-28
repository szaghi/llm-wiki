---
type: Method
title: "One-equation subgrid kinetic-energy models"
description: "Eddy-viscosity LES closures that transport the subgrid kinetic energy and build the viscosity from its square root and the filter width; the sources use the localized dynamic and dynamic k-equation models, a test-filter-free quasi-dynamic variant, Yoshizawa's algebraic estimate as energy target, and the equation in hybrid and astrophysical codes."
status: established
aliases: [k-equation model, one-equation SGS model, subgrid kinetic energy equation model, LDKM, localized dynamic k-equation model, dynamic k-equation model, DKSGS, dk-equation model, Yoshizawa one-equation model, quasi-dynamic SGS kinetic energy equation model, QKM]
tags: [les, sgs-model, eddy-viscosity, compressible, combustion]
timestamp: 2026-10-28T12:25:00Z
---

# One-equation subgrid kinetic-energy models

A **one-equation subgrid kinetic-energy model** closes the
[subgrid stress](/definitions/large-eddy-simulation.md) with an eddy
viscosity whose velocity scale is the square root of the subgrid kinetic
energy $k_{\mathrm{sgs}}=\tfrac12\tau_{ii}$, and obtains $k_{\mathrm{sgs}}$
from its own transport equation instead of from the local resolved strain.
In the compressible (Favre-filtered) form used by most sources,
$\bar\rho k_{\mathrm{sgs}}=\tfrac12\bar\rho(\widetilde{u_iu_i}-\tilde u_i\tilde u_i)$,
so that $\tau_{kk}=2\bar\rho k_{\mathrm{sgs}}$ is a solved quantity, and

$$\tau_{ij}=\tfrac23\bar\rho k_{\mathrm{sgs}}\delta_{ij}-2\mu_t\tilde S^d_{ij},\qquad \mu_t=c_k\,\bar\rho\,\Delta\sqrt{k_{\mathrm{sgs}}},$$

with $c_k$ (registry §11) the viscosity coefficient. The transport equation
is driven by the local subgrid energy flux $\Pi=-\tau_{ij}\tilde S_{ij}$
(registry §3; a gain for $k_{\mathrm{sgs}}$ when the cascade is forward)
and drained by a dissipation modelled as $c_\varepsilon\bar\rho k_{\mathrm{sgs}}^{3/2}/\Delta$
($c_\varepsilon$, registry §11). Because $k_{\mathrm{sgs}}$ is transported, the
model carries history and non-local effects that an algebraic closure such
as the [Smagorinsky model](/methods/smagorinsky-model.md) lacks, at the
price of one more equation and of closures for its unclosed terms.

## Equilibrium limit: Smagorinsky and Yoshizawa forms

If production balances dissipation locally, the transport equation
becomes algebraic. For incompressible flow with the stress above,
$\nu_t\lvert\bar S\rvert^2=c_\varepsilon k_{\mathrm{sgs}}^{3/2}/\Delta$
with $\nu_t=c_k\Delta\sqrt{k_{\mathrm{sgs}}}$ gives

$$k_{\mathrm{sgs}}=\frac{c_k}{c_\varepsilon}\,\Delta^2\lvert\bar S\rvert^2,\qquad \nu_t=\frac{c_k^{3/2}}{c_\varepsilon^{1/2}}\,\Delta^2\lvert\bar S\rvert,$$

that is, the Smagorinsky viscosity with $C_s^2=c_k^{3/2}c_\varepsilon^{-1/2}$
and Yoshizawa's algebraic estimate of the subgrid energy with
$C_I=c_k/c_\varepsilon$ *(compiler check, not in the sources)*. The
sources use both ends of this relation:

- [Abe (2021)](/sources/abe-2021.md) (§IV E, Eqs. 18–20) equates the
  Smagorinsky viscosity with a one-equation viscosity
  $C_{\mathrm{sgs}}f_{\mathrm{sgs}}\sqrt{k_{\mathrm{sgs}}}\Delta$
  ($C_{\mathrm{sgs}}=0.05$) to obtain an algebraic subgrid energy, and
  finds it suppressed on high-aspect-ratio cells, like the Smagorinsky
  viscosity itself (see the [Smagorinsky model](/methods/smagorinsky-model.md));
- [Hausmann et al. (2022)](/sources/hausmann-2022.md) (§II F, Eq. 28) take
  the algebraic form as the target energy of their
  [subgrid velocity enrichment](/methods/subgrid-velocity-enrichment.md):
  $k_{\mathrm{sgs}}=C_I\Delta^2\lvert\bar S\rvert^2$ (the paper's
  $C_I\Delta^22\tilde S_{ij}\tilde S_{ij}$) with $C_I=0.0826$, which they call
  the originally proposed value of Yoshizawa (cited), $\Delta$ the cell
  size. In forced isotropic turbulence ($Re_\lambda=75$, DNS $256^3$
  filtered with a spectrally sharp filter to the $32^3$ LES cutoff) the
  estimate "lies within a ten percent margin" of the filtered-DNS subgrid
  energy; the comparison is stated numerically, not plotted. Averaging the
  estimate over several cells makes its PDF more Gaussian, so they evaluate
  it in one cell (§II D, §II F, Fig. 3). They note that $C_I$ can be made
  dynamic after Moin et al. (cited);
- the same isotropic form, $\tau_{kk}=2C_I\bar\rho\Delta^2\lvert\tilde S\rvert^2$,
  is the Yoshizawa trace added to compressible Smagorinsky models (see the
  [Smagorinsky model](/methods/smagorinsky-model.md) and the
  [dynamic procedure](/methods/dynamic-procedure.md)).

## Localized dynamic $k$-equation model

[Fureby & Nilsson (2023)](/sources/fureby-2023.md) (§3.2) close their
finite-rate-chemistry LES of a cavity-stabilized dual-mode ramjet with the
localized dynamic $k$-equation model (LDKM) of Kim & Menon (cited), in the
form

$$\partial_t(\bar\rho k_{\mathrm{sgs}})+\partial_j(\bar\rho k_{\mathrm{sgs}}\tilde u_j)=-\tau_{ij}\tilde S_{ij}+\partial_j\big(\mu_t\,\partial_jk_{\mathrm{sgs}}\big)-c_\varepsilon\frac{\bar\rho k_{\mathrm{sgs}}^{3/2}}{\Delta},$$

with $\mu_t=c_k\bar\rho\Delta\sqrt{k_{\mathrm{sgs}}}$ and the stress of the
lead paragraph (translated from the paper's tensor notation, in which the
full density-weighted stress enters the momentum equation as its negative
divergence). The coefficients $c_k$ and $c_\varepsilon$ are "dynamically
evaluated from scale similarity"; neither the procedure nor values are
printed. The subgrid scalar and energy fluxes are gradient-diffusion
closures with $Pr_t\approx0.7$ and a turbulent Schmidt number of about 0.85.
The authors choose LDKM over Smagorinsky,
[WALE](/methods/wale-model.md) and hyperviscosity because, citing their own
earlier comparison, it "performs better than many other subgrid models
with respect to turbulent boundary layers, mixing and shock-boundary layer
interactions", and they call LDKM with the partially-stirred-reactor
combustion closure "a reliable combination, capable of matching the more
advanced and expensive models" (§3.2, §6, both self-cited). They also note
that extending subgrid models from incompressible to compressible reacting
flow by dimensional arguments "can be disputed but in the absence of better
alternatives this constitutes today's standards" (§3.2). The paper studies
combustion, not the closure: the only turbulence-related check is the
resolved fraction of turbulent kinetic energy, 90%, 94% and 96% on grids of
7.3, 24.6 and 57.8 million cells (§6.2; see
[grid-point requirements](/results/les-grid-point-requirements.md)).

The same Kim–Menon dynamic $k$-equation subgrid model (DKSGS) is the "LES"
against which [Idelsohn et al. (2024)](/sources/idelsohn-2024.md) (§2.10)
measure their [pseudo-direct numerical simulation](/methods/pseudo-direct-numerical-simulation.md)
on the same coarse meshes; its formula is not printed there. The
reported LES results are ($h_s$ the step height, page-local):

| case | coarse mesh | DKSGS LES | reference | locator |
|---|---|---|---|---|
| decaying isotropic turbulence, Reynolds number on the r.m.s. velocity about 60 and 500 | $32^3$ down to $4^3$ | accurate at $32^3$, departs from DNS as the mesh coarsens | DNS $256^3$ | §2.10.3, Fig. 12 |
| [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) | $32^3$ | under-predicts the energy decay | DNS $512^3$ | §2.10.4, Fig. 13 |
| [backward-facing step](/benchmarks/backward-facing-step.md), $Re_h=5000$ | 142 000 cells | $x_R=5.1h_s$ | DNS $6.1h_s$, experiment $(6\pm0.15)h_s$ | §2.10.5, Fig. 16 |
| [square cylinder](/benchmarks/square-cylinder-flow.md), $Re=22\,000$ | about 2 million cells | $St=0.115$, mean $C_D=2.701$, $L_r=1.404$ | DNS 0.132, 2.18, 1.04 | §2.10.6, Table 2 |

Idelsohn et al. read these as a limitation of LES on coarse meshes; the
comparison is a single coarse-mesh LES per case. In their particle-laden
examples the LES comparator is static Smagorinsky instead (§3.2).

### Dynamic $k$-equation model in supersonic film-cooling LES

[Wei et al. (2023)](/sources/wei-2023.md) (§II B, Eqs. 9–15) close their
wall-resolved LES of supersonic hydrogen film cooling (Burrows–Kurkov
configuration, Mach 2.44, in the OpenFOAM-based solver scramjetFoam; see
[OpenFOAM](/software/openfoam.md)) with the same model family: Yoshizawa's
one-equation model with the dynamic procedure of Kim & Menon and Germano
et al. (all cited),

$$\partial_t(\bar\rho k_{\mathrm{sgs}})+\partial_i(\bar\rho\tilde u_ik_{\mathrm{sgs}})=-\tau_{ij}\partial_j\tilde u_i-c_\varepsilon\frac{\bar\rho k_{\mathrm{sgs}}^{3/2}}{\Delta}+\partial_j\big(\bar\rho\nu_t\,\partial_jk_{\mathrm{sgs}}\big),\qquad \nu_t=c_k\sqrt{k_{\mathrm{sgs}}}\,\Delta,$$

with the deviatoric stress closed by $-2\bar\rho\nu_t\tilde S^d_{ij}$,
$\Delta=(\Delta_x\Delta_y\Delta_z)^{1/3}$ the implicit (grid) filter width,
and $c_k$, $c_\varepsilon$ computed dynamically (no values printed). The
paper's $\tau^{sgs}_{ij}=\overline{\rho u_iu_j}-\bar\rho\tilde u_i\tilde u_j$
carries the density, as the compressible registry form does. The subgrid
heat and species fluxes are gradient-diffusion closures with constant
subgrid turbulent Prandtl and Schmidt numbers 0.85 and 0.7, and the
subgrid viscous-work flux is neglected. The authors choose the model
because it "accounts for history effects" and depends little on model
parameters; they report that 99.5% of the cells resolve more than 80% of
the turbulent kinetic energy (§III B, Fig. 6). Their a posteriori
analysis of the resolved turbulent Prandtl and Schmidt numbers, which vary
between 0 and 2 although the subgrid values are constant, is on
[turbulent Prandtl number](/definitions/turbulent-prandtl-number.md).

## Dynamic and quasi-dynamic compressible variants

[Qi et al. (2022)](/sources/qi-2022-b.md) (§3.1, Eqs. 3.1–3.7) solve the
exact compressible $k_{\mathrm{sgs}}$ equation of Chai & Mahesh (cited),
whose right-hand side contains the subgrid flux, a turbulent diffusion, a
solenoidal and a dilatational dissipation and a subgrid pressure
dilatation, and model each term separately rather than lumping them into
one production and one dissipation, which they criticise in earlier
$k$-equation models (§1). The Chai–Mahesh dynamic $k$-equation model
("dk-equation", every term with a coefficient from the Germano identity)
is one of their baselines. Their own quasi-dynamic model (QKM) closes every
term with the leading term of the series expansion of a filtered product,
$\overline{fg}-\bar f\bar g\approx C_0\Delta_k^2\partial_k\bar f\partial_k\bar g$,
whose single coefficient follows from the transported energy,
$C_0=2k_{\mathrm{sgs}}/(\Delta_l^2\partial_l\tilde u_k\partial_l\tilde u_k)$,
without a test filter; the Smagorinsky coefficient of the deviatoric
stress is fixed by matching the anisotropic part of the subgrid flux, and
the isotropic part of the stress is $2\bar\rho k_{\mathrm{sgs}}$ instead of
Yoshizawa's model (Eqs. 3.11–3.26). The construction, the a priori and
a posteriori evidence and the costs are on the
[dynamic procedure](/methods/dynamic-procedure.md) and
[gradient model](/methods/gradient-model.md) pages. In compressible channel
flow at $M=1.5$ (DNS $Re_\tau=220$) the dk-equation model gives
$Re_\tau=215$, 210 and 208 on three successively coarser grids and QKM
220, 221 and 218 (Tables 2–4); per step QKM costs about as much as the
dk-equation model ($7.22\times10^{-2}$ s against $7.38\times10^{-2}$ s on 112
CPUs, Table 5).

## Other uses (inline)

- **Hybrid RANS/LES.** [Tang et al. (2022)](/sources/tang-2022.md)
  (§2.1, Eqs. 1–9) run Yoshizawa's one-equation model (as cited) in the LES
  region of a zonal [hybrid RANS/LES](/definitions/hybrid-rans-les.md) of
  scramjet combustion, with viscosity constant 0.02075 and dissipation
  constant 1.0, recast as a transport equation for $\nu_t$ and blended with
  the [Spalart–Allmaras](/methods/spalart-allmaras-model.md) equation near
  walls (see [large-eddy simulation](/definitions/large-eddy-simulation.md)).
- **Reynolds-stress-based DES.** In the LES branch of the Reynolds-stress
  IDDES of [Li et al. (2022)](/sources/li-2022-k.md) (§II C, Eqs. 4–9) the
  isotropic dissipation $\tfrac23\delta_{ij}k^{3/2}/(C_{\mathrm{DES}}\Delta)$
  of the modelled stresses, $k$ the modelled kinetic energy, plays the role
  of the $c_\varepsilon$ sink; under
  equilibrium the branch is "Smagorinsky-like", with
  $C_{\mathrm{DES}}=C_kC_s$ ($C_k$ page-local there, fixed by the
  length-scale equation), which they make dynamic (see
  [detached-eddy simulation](/methods/detached-eddy-simulation.md) and the
  [dynamic procedure](/methods/dynamic-procedure.md)).
- **Astrophysical codes.** In [RAMSES](/software/ramses.md), as used by
  [Liu et al. (2022)](/sources/liu-2022.md) (§2.3), a transport
  equation for the subgrid turbulent kinetic energy (production by resolved
  shear, a cascade sink) sets the star-formation efficiency and the
  velocity dispersion that drives the
  [subgrid turbulent dynamo model](/methods/subgrid-turbulent-dynamo-model.md);
  its equation is not printed in that source.

- **Origin, as told in a history of LES.** [Kim & Leonard (2024)](/sources/kim-2024-b.md)
  (§2.5) credit Schumann (1975, cited) with extending subgrid modelling to
  anisotropic grids and adding a transport equation for the subgrid
  turbulent energy, in LES of plane channels and annuli with up to 65 000
  grid volumes and special wall boundary conditions instead of no-slip;
  no equation is printed.
- **Detonation-engine LES.** [Vignat et al. (2024)](/sources/vignat-2024.md)
  (§3.3, Table 1) list one-equation eddy-viscosity and one-equation
  turbulent-kinetic-energy closures (the latter in
  [ANSYS Fluent](/software/ansys-fluent.md)) among the subgrid treatments
  of earlier LES of the same rotating detonation rocket engine; their own
  LES uses the [Vreman model](/methods/vreman-model.md).
- **Reference LES for an implicit-LES solver.** [De Cosmo et al. (2025)](/sources/decosmo-2025.md)
  (§3.4, Fig. 16) take the Reynolds stresses at $x/h=0$, 3 and 10 of a
  channel with a two-Gaussian bump on the lower wall (the Banchetti et al.
  geometry, as they cite it; see
  [turbulent channel flow](/benchmarks/turbulent-channel-flow.md)) from an
  [OpenFOAM](/software/openfoam.md) LES "with the k-equation SGS model",
  since the DNS provides no fluctuation data; the model's constants are not
  printed. They note that the reference is an incompressible solver with a
  "substantially more sophisticated SGS model" than their
  [implicit LES](/definitions/implicit-les.md), which has none; its
  $\langle v'v'\rangle$ and $\langle w'w'\rangle$ come out slightly lower,
  which they attribute to numerical dissipation from mesh
  non-orthogonality and streamwise non-uniformity.

## Qualifications

- **Two values of Yoshizawa's $C_I$, side by side.** Both sources cite
  Yoshizawa (1986) for the same algebraic form. Hausmann et al. (2022,
  §II F, §III B) print $K=C_I\Delta^2\,2\tilde S_{ij}\tilde S_{ij}$, that is
  $k_{\mathrm{sgs}}=C_I\Delta^2\lvert\bar S\rvert^2$, with $\Delta$ the
  cell size of a uniform grid and $C_I=0.0826$, "the originally proposed
  value of the model constant", also called "the analytical constant".
  [Volpiani (2024)](/sources/volpiani-2024.md) (App. 2, Eq. 28) print
  $\tau_{kk}=2C_I\bar\rho\Delta^2\lvert\tilde S\rvert^2$ with
  $\lvert\tilde S\rvert=(2\tilde S_{ij}\tilde S_{ij})^{1/2}$, $\Delta$ the
  cube root of the cell volume and $C_I=0.0066$, without calling the value
  original; with $\tau_{kk}=2\bar\rho k_{\mathrm{sgs}}$ this is
  $k_{\mathrm{sgs}}=C_I\Delta^2\lvert\tilde S\rvert^2$, and the two
  coefficients differ by a factor of about 12.5 *(compiler check, not in
  the sources)*. Neither source discusses the other value (see the
  [Smagorinsky model](/methods/smagorinsky-model.md) for Volpiani's
  closure).
- **Unstated coefficients.** Fureby & Nilsson (2023) and Idelsohn et al.
  (2024) print no values of $c_k$, $c_\varepsilon$ or of the dynamic
  procedure. Fureby & Nilsson print the subgrid scalar and
  energy fluxes with the molecular $\mu$ divided by turbulent Prandtl and
  Schmidt numbers (§3.2), recorded as printed.

# Citations

- [Fureby & Nilsson (2023)](/sources/fureby-2023.md) — §3.2; §6; §6.2.
- [Wei et al. (2023)](/sources/wei-2023.md) — §II B, Eqs. (9)–(15); §III B, Fig. 6.
- [Kim & Leonard (2024)](/sources/kim-2024-b.md) — §2.5.
- [Vignat et al. (2024)](/sources/vignat-2024.md) — §3.3, Table 1.
- [Idelsohn et al. (2024)](/sources/idelsohn-2024.md) — §2.10.3–2.10.6, Figs. 12, 13, 16, Table 2; §3.2.
- [Hausmann et al. (2022)](/sources/hausmann-2022.md) — §II D, §II F, Eq. (28), Fig. 3.
- [Qi et al. (2022)](/sources/qi-2022-b.md) — §1; §3.1, Eqs. (3.1)–(3.7); §3.2, Eqs. (3.11)–(3.26); §4.1, Tables 2–5.
- [Abe (2021)](/sources/abe-2021.md) — §IV E, Eqs. (18)–(20).
- [Tang et al. (2022)](/sources/tang-2022.md) — §2.1, Eqs. (1)–(9).
- [Li et al. (2022)](/sources/li-2022-k.md) — §II C, Eqs. (4)–(9).
- [Liu et al. (2022)](/sources/liu-2022.md) — §2.3.
- [Volpiani (2024)](/sources/volpiani-2024.md) — App. 2, Eq. (28).
- [De Cosmo et al. (2025)](/sources/decosmo-2025.md) — §3.4, Figs. 14–16 (OpenFOAM k-equation LES as Reynolds-stress reference of the bump channel).
