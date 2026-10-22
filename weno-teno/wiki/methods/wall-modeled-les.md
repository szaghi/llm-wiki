---
type: Method
title: "Wall-modelled large-eddy simulation"
description: "Equilibrium wall-modelled LES solves thin-boundary-layer ODEs between the wall and an exchange point and imposes the modelled wall stress and heat flux through an effective wall viscosity and conductivity, keeping no-slip; De Vanna et al. show that shock-capturing dissipation decides whether wall turbulence survives in it, and couple it with immersed boundaries."
status: established
aliases: [WMLES, wall-modeled LES, equilibrium wall-stress model, unified WR/WMLES, IBM+WMLES]
tags: [turbulence, immersed-boundary, numerical-flux, low-dissipation, weno, teno]
timestamp: 2026-10-23T16:00:00Z
---

# Wall-modelled large-eddy simulation

In **wall-resolved LES** (WRLES) the near-wall eddies are resolved by the
grid; in **wall-modelled LES** (WMLES) the first grid points lie in the
logarithmic layer and a model supplies the wall shear stress and heat flux
that the grid cannot resolve. As recalled by
[De Vanna et al. (2023c)](/sources/devanna-2023-c.md)
(§1, after Chapman and Choi & Moin), the number of grid points scales with
the Reynolds number as $\mathrm{Re}^{37/14}$ for DNS, $\mathrm{Re}^{13/7}$ for
WRLES and $\mathrm{Re}$ for WMLES; for $\mathrm{Re}\approx10^7$ a DNS would
need about $10^{18}$ points and a WRLES about $10^{13}$. The three bundle
sources are by one group and use one model, implemented in the
finite-difference GPU solver [URANOS](/software/uranos.md)
([De Vanna et al. (2023b)](/sources/devanna-2023-b.md), §2.3). The bundle
records the method because of what it reveals about the convective
discretization: the numerical dissipation of shock-capturing schemes acts
far more strongly on WMLES than on WRLES
([De Vanna et al. (2023a)](/sources/devanna-2023.md)).

Page-local symbols: $y$ wall distance; $\mu$, $\lambda_{\mathrm c}$
dynamic viscosity and thermal conductivity ($\lambda_{\mathrm c}=c_p\mu/\mathrm{Pr}$);
$c_p$ specific heat at constant pressure; $T$ temperature; $\tau_w$, $q_w$
wall shear stress and heat flux; $u_\tau=\sqrt{\tau_w/\rho_w}$ friction
velocity; $y^+=\rho_wu_\tau y/\mu_w$; subscript $w$ wall values;
$\kappa_{\mathrm{vK}}=0.41$ the von Kármán constant (not the kinetic energy
$\kappa$ of the registry).

## The equilibrium wall-stress model

All three sources use the same thin-boundary-layer equilibrium model,
recalled from the group's earlier work (De Vanna et al. (2023a), §2.2,
Eq. (4); De Vanna et al. (2023b), §2.3, Eq. (7); De Vanna et al. (2023c),
§2.4, Eqs. (10)–(11)). On a separate one-dimensional grid along the wall
normal, from $y=0$ to an exchange height $h_{\mathrm{wm}}$ (page-local), it
solves for the wall-parallel velocity $U_{\mathrm{wm}}$ and temperature
$T_{\mathrm{wm}}$:

$$\begin{aligned}
&\frac{d}{dy}\Big[(\mu_{\mathrm{wm}}+\mu_{t})\frac{dU_{\mathrm{wm}}}{dy}\Big]=0,\\
&\frac{d}{dy}\Big[c_p\Big(\frac{\mu_{\mathrm{wm}}}{\mathrm{Pr}}+\frac{\mu_{t}}{\mathrm{Pr}_t}\Big)\frac{dT_{\mathrm{wm}}}{dy}\Big]=-\frac{d}{dy}\Big[(\mu_{\mathrm{wm}}+\mu_{t})U_{\mathrm{wm}}\frac{dU_{\mathrm{wm}}}{dy}\Big],
\end{aligned}$$

with turbulent Prandtl number $\mathrm{Pr}_t=0.9$ and the mixing-length
eddy viscosity $\mu_t=\kappa_{\mathrm{vK}}\rho_{\mathrm{wm}}u_\tau yD$,
$\rho_{\mathrm{wm}}=p_{\mathrm{LES}}/(RT_{\mathrm{wm}})$, van Driest damping
$D=[1-\exp(-y^*/A^+)]^2$, $A^+=17$, and the semi-local wall distance
$y^*=y\sqrt{\rho_{\mathrm{wm}}\tau_{w,\mathrm{wm}}}/\mu_{\mathrm{wm}}$
(page-local $R$ the gas constant). At $y=h_{\mathrm{wm}}$ the model is matched
to the LES: $U_{\mathrm{wm}}$ to the wall-parallel LES velocity,
$T_{\mathrm{wm}}$ and the pressure to the LES values. The outputs are
$\tau_{w,\mathrm{wm}}=(\mu\,dU_{\mathrm{wm}}/dy)_{y=0}$ and
$q_{w,\mathrm{wm}}=(\lambda_{\mathrm c}\,dT_{\mathrm{wm}}/dy)_{y=0}$
(De Vanna et al. (2023a), Eq. (5); (2023c), Eq. (23)). The model contains no
pressure-gradient term and cannot produce reversed flow
((2023c), §4.4.3).

## Imposing the modelled stress: effective wall viscosity

The coupling, the group's "unified WR/WMLES" approach, does not replace the
no-slip condition by a slip or Neumann condition. It raises the viscosity
and conductivity at the wall so that the resolved velocity and temperature
gradients reproduce the modelled flux (De Vanna et al. (2023a), Eqs. (6)–(8);
(2023c), Eqs. (24)–(25)):

$$\mu_{\mathrm{eff}}=\frac{\tau_{w,\mathrm{wm}}}{\tau_w^{\mathrm{LES}}}\,\mu_w,\qquad
\lambda_{\mathrm{eff}}=\frac{q_{w,\mathrm{wm}}}{q_w^{\mathrm{LES}}}\,\lambda_{\mathrm{c},w},$$

with $\tau_w^{\mathrm{LES}}$, $q_w^{\mathrm{LES}}$ the stress and heat flux
that the resolved field gives at the wall. The difference
$\mu_{\mathrm{eff}}-\mu_w$ is the missing subgrid-scale viscosity at the wall.
No-slip and isothermal or adiabatic conditions stay imposed. When the wall
is resolved the ratios tend to 1, $\mu_{\mathrm{eff}}\to\mu_w$, and the method
falls back to WRLES ((2023a), §2.2; (2023c), §3.5 step 9). De Vanna et al.
(2023c) state that imposing the wall stress this way "has never been
addressed" in compressible conditions and only partially in incompressible
ones (§1); the earlier compressible instance they build on is their own.
They contrast it with slip-velocity, log-law-extrapolation and partial-slip
treatments of other authors, which modify the velocity condition (§1).

## Coupling with immersed boundaries

De Vanna et al. (2023c) carry the model to walls of arbitrary shape on
Cartesian grids with a sharp-interface ghost-point
[immersed-boundary method](/methods/immersed-boundary-method.md). For each
ghost point a wall-normal probe defines an image point in the fluid, where
the flow variables are bilinearly (2D) or trilinearly (3D) interpolated.
The algorithm (§3.5, steps 1–9):

1. interpolate velocity, viscosity and conductivity at the image point;
2. take the wall-parallel speed there and a first-guess friction velocity
   from Reichardt's law, iterated (Eq. (20));
3. form the local inner-scaled spacings; if
   $\Delta x^+_w<40$, $\Delta y^+_w<5$, $\Delta z^+_w<20$ (Eq. (21), taken
   from the literature) the wall is resolved, and the ghost
   viscosity is extrapolated laminarly, $\mu_g=2\mu_w-\mu_{\mathrm{ip}}$
   (page-local $g$ ghost, ip image point; Eq. (22));
4. otherwise solve the wall model between the wall and an interface point
   along the normal and set $\mu_g=2\mu_{\mathrm{eff}}-\mu_{\mathrm{ip}}$, and
   likewise for the conductivity (Eq. (24)).

The switch is pointwise and re-evaluated in time, so WRLES and WMLES
coexist on one wall; a binary activation sensor records which is active.
On the Mach 2.91, 24° compression ramp the sensor is about 0.5 for
$x^*<-10$, close to zero inside the separation bubble and 1 on the ramp
(Fig. 19). Because the bubble is treated as wall-resolved, negative mean
wall velocities appear although the equilibrium model cannot produce them
(§4.4.2–4.4.3). The whole algorithm is explicit with compact supports; the
geometric preprocessing (ray tracing, flagging, interpolation weights) is
done once, and the method runs on multiple GPUs without special MPI
treatment (§3.6).

## Interaction with the convective scheme

De Vanna et al. (2023a) compare six convective discretizations in 69 cases
of spatially developing supersonic boundary layers
([supersonic turbulent boundary layer](/benchmarks/supersonic-turbulent-boundary-layer.md)):
a sixth-order fully split central energy-preserving (EP) scheme of
Pirozzoli ([split convective forms](/methods/split-convective-forms.md),
[kinetic energy preservation](/properties/kinetic-energy-preservation.md)),
[WENO-Z](/methods/weno-z.md) of orders 3, 5 and 7 with $\epsilon=10^{-12}$,
[TENO5](/methods/targeted-eno.md) with $C_T=10^{-7}$ and
[TENO-A5](/methods/adaptive-teno.md) with $C_T$ between $10^{-10}$ and
$10^{-7}$ (§3.1). The shock-capturing schemes run pure or in a
[hybrid](/methods/hybrid-weno.md) with the EP scheme, switched by a
modified [Ducros sensor](/definitions/ducros-shock-sensor.md)
$\Psi_{\mathrm D}$ above a threshold
$\Psi^*\in\{0,0.1,0.2,0.4\}$, $\Psi^*=0$ being
pure WENO/TENO (§3.2, Eq. (9)).

- **WRLES** ($M_\infty=2$, statistics at $\mathrm{Re}_\tau=250$). Upwinding
  lowers the wall friction, raises the log-layer velocity and the peak of
  turbulent kinetic energy; the error shrinks as the WENO order rises and
  with TENO, and the EP scheme fits the DNS (§4.2, Figs. 1–2).
- **WMLES, pure shock capturing** ($M_\infty=2$, statistics at
  $\mathrm{Re}_\tau=900$, three grids). On the coarse grid pure WENO/TENO do
  not sustain wall turbulence; on the medium grid all but WENO-Z3 give
  reasonable friction with damped turbulence; on the fine grid they
  overestimate friction. WENO-Z3 is wrong on every grid, and no
  WENO/TENO variant collapses on the EP solution (§4.3.1, Fig. 5).
- **WMLES, hybrid.** $\Psi^*=0.1$ already brings friction and
  profiles near the DNS on the medium and fine grids; on the coarse grid it
  widens the $\mathrm{Re}_\tau$ range and gives a decreasing friction curve,
  but not a fully turbulent one (§4.3.1, Fig. 5). At $\Psi^*=0.4$ all
  shock-capturing variants give identical curves, since the EP scheme
  covers most of the flow. A mild drag reduction and overestimated
  fluctuations remain relative to pure EP (§4.3.3, Figs. 7–8).
- **Hypersonic WMLES** ($M_\infty=5.86$, cold wall). The pure EP scheme
  diverges because of shocklets; $\Psi^*=0.2$ is the largest
  stable threshold, and the authors recommend $\Psi^*\simeq0.2$
  as an upper bound for hypersonic regimes (§4.4, §6).
- **Cost** (13 Intel KNL nodes, Joliot-Curie). Wall time per iteration
  relative to pure EP is 0.90–1.00 for the hybrids and 0.95–1.32 for the
  pure schemes, the maximum for TENO-A5 on the fine grid (Table 2).
- **Subgrid model.** Smagorinsky, whose eddy viscosity does not vanish at
  the wall, deviates; WALE, Sigma and the Mixed Time Scale model give
  similar results (Appendix, Fig. 10).

They explain the stronger effect in WMLES (§5): there the Reynolds
stresses reach the wall stress only through the wall model, which sees
only the instantaneous velocity and temperature at the exchange point, so
upwind dissipation that damps the resolved fluctuations can remove wall
turbulence altogether. They also state that in low-resolution WMLES shock
sensors read turbulent fluctuations and grid noise as shocklets and
activate the shock-capturing scheme in smooth regions (§3.2, §4.3.3).
De Vanna et al. (2023c) cite this study for their choice of a hybrid
EP–TENO-A scheme with $\Psi^*=0.1$ (§4.3).

## Validation

| test | source | result |
|---|---|---|
| channel, $M_b=0.1$, $\mathrm{Re}_\tau$ 590–20000, walls as immersed blocks | 2023c §4.1, Tables 1–2 | fit $\mathrm{Re}_\tau=0.084\,\mathrm{Re}_b^{0.89}$ against $0.079\,\mathrm{Re}_b^{0.89}$ (DNS fit) and $0.09\,\mathrm{Re}_b^{0.88}$ (Pope); a "mild log-layer mismatch, typical of WMLES" |
| channel, $\mathrm{Re}_\tau=5200$, $160\times128\times80$, walls on the domain boundary | 2023b §5.1, Fig. 7 | agrees with DNS away from the wall |
| pipe in an immersed square block, $\mathrm{Re}_\tau$ 500–6000 | 2023c §4.2, Figs. 9–10 | friction factor on DNS and the Prandtl law, slightly high at the lowest Re; velocity fluctuations underestimated |
| Mach 2 boundary layer on an immersed block, $\mathrm{Re}_\tau$ 250–2000 | 2023c §4.3, Fig. 13 | $C_f$ slightly overestimated, less so as $\mathrm{Re}_\tau$ grows |
| Mach 5.86 boundary layer, $\mathrm{Re}_\tau=1200$, TENO-A5 | 2023b §5.2, Fig. 10 | mean velocity and temperature agree with DNS, deviations in the inner-layer turbulent kinetic energy |
| Mach 2.91, 24° compression ramp, three grids | 2023c §4.4, Table 5 | separation at $x^*=-4.0,-4.0,-3.2$, reattachment at $0.56,0.80,0.67$; bubble overpredicted, separation about one boundary-layer thickness upstream of the DNS; a spurious $\lambda$-shock branch on the coarse and medium grids |

## Qualifications

- **Equilibrium model.** The model has no pressure-gradient or
  non-equilibrium terms. De Vanna et al. (2023c) attribute the
  overpredicted ramp bubble and part of the $\lambda$-shock artefact to
  this, and state that a non-equilibrium model would be needed in the
  bubble (§4.4.3).
- **Thresholds are sensor-specific.** The recommended
  $\Psi^*\simeq0.2$ belongs to the modified, non-squared,
  compression-only Ducros sensor of these papers, with regularization
  $\epsilon_{\mathrm D}=(v_\infty/\delta_0)^2$ (De Vanna et al. (2023a),
  Eq. (9)). Where $\nabla\cdot v<0$ and with the same
  $\epsilon_{\mathrm D}$, $\Psi_{\mathrm D}=\sqrt{\Phi_{\mathrm D}}$ for the
  classical squared ratio $\Phi_{\mathrm D}$ of the
  [Ducros page](/definitions/ducros-shock-sensor.md), so $\Psi^*=0.2$ is the
  threshold $0.04$ on $\Phi_{\mathrm D}$ *(compiler check, not in the
  sources)*.
- **Explanatory text versus data.** De Vanna et al. (2023a) write that
  numerical viscosity "freezes the Reynolds stress", that by momentum
  conservation "the average wall velocity gradient must increase", and
  call the result a drag reduction (§5, §6), while their §4.2 reports the
  wall friction *under*estimated in WRLES. With $\tau_w=\mu_w(\partial
  v_1/\partial y)_w$, a larger mean wall velocity gradient is a larger wall
  stress, so the mechanism as worded has the sign opposite to the reported
  friction *(compiler check, not in the sources)*.
- **Printed inconsistencies.** De Vanna et al. (2023a) print
  $\Delta x^+=90$ for the Mach 5.86 grid of 1400 streamwise points (Table 4,
  §4.4). Assuming the domain length $90\delta_0$ of §4.1 also holds at Mach
  5.86, $\mathrm{Re}_\tau=1200$ gives $90\cdot1200/1400\approx77.1$, and 90
  would need 1200 points; the same rule reproduces every other printed
  streamwise spacing of Tables 1–3 ($90\cdot250/768=29.3$,
  $90\cdot900/960=84.4$) *(compiler check, not in the sources)*. De Vanna et al. (2023c) print the first-guess friction
  velocity as $\tau^*_w=\sqrt{u^*_\tau/\rho_w}$ (§3.5 step 3), dimensionally
  inverted; their own §4.1 uses $u_\tau=\sqrt{\tau_w/\rho_w}$.
- **One group.** All validation is by the authors of the method against
  DNS; there is no independent comparison with other wall models in the
  bundle.

# Citations

- [De Vanna et al. (2023a)](/sources/devanna-2023.md) — §1, §2.2 Eqs. (4)–(8), §3.1–3.2 Eq. (9), §4.2 Figs. 1–2, §4.3 Table 2 Figs. 5–8, §4.4 Fig. 9, §5, §6, Appendix Fig. 10.
- [De Vanna et al. (2023b)](/sources/devanna-2023-b.md) — §2.3 Eq. (7), §5.1 Fig. 7, §5.2 Fig. 10.
- [De Vanna et al. (2023c)](/sources/devanna-2023-c.md) — §1, §2.4 Eqs. (10)–(12), §3.5 Eqs. (19)–(25), §3.6, §4.1–4.4 Tables 1–5 Figs. 5–20.
