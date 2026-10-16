---
type: Method
title: "Sheath (Bohm) boundary conditions"
description: "Boundary conditions for MHD codes where field lines intersect a material wall: the plasma leaves at the sound speed (Bohm criterion), the energy flux is a sheath transmission factor times the convected thermal energy, density has no diffusive flux, and the electric potential and current are prescribed, optionally limited by the ion saturation current."
status: established
aliases: [Bohm boundary condition, sheath BC, Bohm–Chodura condition, sheath heat transmission]
tags: [edge, divertor, wall, mhd, numerics]
timestamp: 2026-10-16T00:00:00Z
---

# Sheath (Bohm) boundary conditions

Where the computational boundary is a flux surface, MHD codes fix the
fields (Dirichlet). Where field lines cross the boundary, as on divertor
targets and on a limiting wall, the boundary stands for a Debye sheath that
the fluid model does not resolve, and the conditions express the sheath's
effect on the flow and the energy flux
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.3.2;
[Bhole et al. (2023)](/sources/bhole-2023.md), p. 9;
[Korving et al. (2023)](/sources/korving-2023.md), §V E). They are what
makes [JOREK](/software/jorek.md) usable for SOL, divertor and
[halo-current](/definitions/halo-current.md) studies
([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.1).

## Flow: the Bohm criterion

The plasma enters the sheath at (at least) the sound speed $c_s$:

- in reduced MHD the parallel velocity is set to $v_\parallel=c_s$ at the
  wall ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.3.2; the
  "magnetized Bohm sheath" condition of
  [Korving et al. (2023)](/sources/korving-2023.md), §V E);
- in full MHD the normal velocity is prescribed,
  $\mathbf v\cdot\mathbf n=\pm\sqrt{\Gamma T}$ in normalized units with $T$ the
  total temperature ([Bhole et al. (2023)](/sources/bhole-2023.md), p. 9,
  "Mach-1").

The JOREK outlook lists outflows with Mach numbers larger than one as a
planned refinement ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md),
§2.15).

## Energy: the sheath transmission factor

The energy flux through the sheath is a transmission factor
$\delta_{\mathrm{sh}}$ times the convected thermal energy. For each species
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), Eqs. 40–42),
$$\mathbf q_i\cdot\mathbf n=\delta_{\mathrm{sh},i}\,n_iT_i\,\mathbf v\cdot\mathbf n,\qquad \mathbf q_e\cdot\mathbf n=\delta_{\mathrm{sh},e}\,n_eT_e\,\mathbf v\cdot\mathbf n,$$
with $\delta_{\mathrm{sh},i}\sim2$–3 and $\delta_{\mathrm{sh},e}\sim5$–6;
a single-temperature model uses $\delta_{\mathrm{sh}}\sim7$–8 for the total.
JOREK imposes this as a natural boundary condition on the conductive flux
in the weak form of the temperature equation,
$$\mathsf K\nabla T\cdot\mathbf n=-(c_{\mathrm b}-1)\,n\,T\,\mathbf v\cdot\mathbf n,$$
with $c_{\mathrm b,e}=(\Gamma-1)(\delta_{\mathrm{sh},e}-1)$,
$c_{\mathrm b,i}=(\Gamma-1)(\delta_{\mathrm{sh},i}-\Gamma-1)$ and, for one
temperature, $c_{\mathrm b}=(\Gamma-1)(\delta_{\mathrm{sh}}/2-\Gamma/2-1)$
(as printed; JOREK absorbs $\Gamma-1$ into the conductivity tensor
$\mathsf K=\kappa_\parallel\mathbf b\mathbf b+\kappa_\perp(\mathsf I-\mathbf b\mathbf b)$,
and $n$ stands for the mass density in JOREK units).

The full-MHD form of [Bhole et al. (2023)](/sources/bhole-2023.md) (p. 9)
writes the total energy balance explicitly,
$$\Big(\tfrac12\rho v^2+\tfrac{\Gamma}{\Gamma-1}\rho T\Big)\mathbf v\cdot\mathbf n-\mathsf K\nabla T\cdot\mathbf n=\delta_{\mathrm{sh}}\,\rho T\,\mathbf v\cdot\mathbf n,\qquad \delta_{\mathrm{sh}}\approx7\text{–}8,$$
in normalized units, with the impurity contribution to the conductivity
included in $\mathsf K$. The resulting target fluxes scale as $\rho T^{1/2}$ for
particles and $\delta_{\mathrm{sh}}\rho T^{3/2}$ for heat, which is how Korving et
al. read the ITER target profiles ([Korving et al. (2023)](/sources/korving-2023.md),
§VI B–C).

## Other variables

- **Density**: no Dirichlet condition; the boundary term of the diffusion
  operator is dropped, so $\mathsf D\nabla\rho\cdot\mathbf n=0$ and the
  particle flux is purely convective
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.3.2); Neumann
  conditions in [Korving et al. (2023)](/sources/korving-2023.md) (§V E).
- **Flux, current, potential, vorticity**: $\psi$, $j$, $u$ and $\varpi$
  stay fixed at the sheath boundary in reduced MHD
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.3.2). Korving et al.
  set $u=\varpi=0$, i.e. a grounded wall $\Phi=0$ (§V E). This choice
  suppresses the toroidal asymmetry of the plasma current in VDEs
  ([reduced-MHD current asymmetry](/results/reduced-mhd-current-asymmetry.md)).
- **Ion saturation current**: the current density through the boundary can
  optionally be limited to the ion saturation current
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.3.2). In COMPASS
  VDE simulations this limit governs the poloidal extent of the halo
  region ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.1, Fig. 6).
- **Free boundary**: the Dirichlet conditions on $\psi$ and $j$ are
  replaced by the vacuum response of
  [resistive-wall coupling](/methods/resistive-wall-coupling.md), while the
  sheath conditions on the flow and energy remain
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.3.2).
- **Neutrals**: recycling and sputtering at the same boundaries feed the
  [fluid](/methods/fluid-neutral-models.md) and
  [kinetic](/methods/kinetic-neutral-model.md) neutral models.

## Sensitivity

In ASDEX Upgrade hot-VDE validation, the simulated $I_p$, halo current and
toroidal peaking factor match the experiment only "for appropriate values"
of the temperature below which the temperature dependence of
$\kappa_\parallel$ is cut off in the SOL; the boundary treatment "strongly"
affects the evolution ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md),
§3.1, Fig. 5). Sheath conditions had been added to the JOREK full MHD model
"recently" as of 2021 ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.12).

# Citations

- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — §2.3.2, Eqs. 40–42; §2.12; §2.15.
- [Bhole et al. (2023)](/sources/bhole-2023.md) — p. 9.
- [Korving et al. (2023)](/sources/korving-2023.md) — §V E, §VI B–C.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) — §3.1, Figs. 5–6.
