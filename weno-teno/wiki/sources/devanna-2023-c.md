---
type: Source
title: "De Vanna et al. (2023) — On the coupling between wall-modeled LES and immersed boundary method towards applicative compressible flow simulations"
description: "Couples an equilibrium wall model, imposed through an effective ghost-point viscosity and conductivity, with a sharp-interface ghost-point immersed boundary method in the GPU solver URANOS, switching pointwise between wall-resolved and wall-modelled treatment; validated on channel, pipe, Mach 2 boundary layer and Mach 2.91 compression ramp."
resource: "doi:10.1016/j.compfluid.2023.106058"
source_kind: paper
authors: [De Vanna F., Baldan G., Picano F., Benini E.]
year: 2023
venue: "Comput. Fluids 266:106058"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Computers_amp_Fluids_De_On_the_coupling_between_wall-modeled_LES_and_immersed_bounda.pdf"
tags: [immersed-boundary, turbulence, teno, gpu, software]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

The paper couples an equilibrium [wall-modelled LES](/methods/wall-modeled-les.md)
with a sharp-interface ghost-point
[immersed boundary method](/methods/immersed-boundary-method.md) inside the
GPU finite-difference solver [URANOS](/software/uranos.md), so that walls of
arbitrary shape on Cartesian grids can be run at high Reynolds and Mach
numbers without control of the near-wall resolution. The wall model is the
group's earlier unified wall-resolved/wall-modelled approach: thin
boundary-layer ODEs for the wall-parallel velocity and temperature are
integrated from the wall to an exchange point. The resulting wall stress and
heat flux are imposed by raising the viscosity and conductivity at the ghost
point to effective values, while no-slip and isothermal or adiabatic
conditions stay enforced. For each ghost point a wall-normal probe defines an
image point with bi- or trilinear interpolation. A first-guess friction
velocity from Reichardt's law tests the local inner-scaled spacings against
$\Delta x^+_w<40$, $\Delta y^+_w<5$, $\Delta z^+_w<20$. The wall model is
switched on, pointwise and dynamically, only where the test fails.

Convection uses a sixth-order energy-preserving central scheme of Pirozzoli
([split convective forms](/methods/split-convective-forms.md)), in
[hybrid](/methods/hybrid-weno.md) with [adaptive TENO](/methods/adaptive-teno.md)
(TENO-A5 or TENO-A7) through a modified
[Ducros sensor](/definitions/ducros-shock-sensor.md) with threshold 0.1, plus
sixth-order semi-conservative viscous terms and
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md) stepping (CFL 0.5), on GPUs
with OpenACC and MPI.

The validation represents every wall as an immersed block. In
[turbulent channel flow](/benchmarks/turbulent-channel-flow.md) at bulk Mach
0.1, $\mathrm{Re}_\tau$ 590–20000, the fit $\mathrm{Re}_\tau=0.084\,\mathrm{Re}_b^{0.89}$
compares with 0.079/0.89 from DNS. Pipe flow inside a square block covers
$\mathrm{Re}_\tau$ 500–6000. The Mach 2
[supersonic turbulent boundary layer](/benchmarks/supersonic-turbulent-boundary-layer.md)
reaches $\mathrm{Re}_\tau=2000$. The Mach 2.91, 24° compression ramp of Priebe &
Martín is run on three grids. In the ramp the activation sensor shows that
the separation bubble is treated mostly as wall-resolved, so reversed flow
appears although the equilibrium model cannot produce it. The bubble is
overpredicted, separating about one boundary-layer thickness upstream of the
DNS, and coarse grids show a spurious λ-shock branch. The evidence is
numerical comparison with DNS only.

# Version read

Version of record (Elsevier typeset, open access CC BY, Computers and Fluids
266 (2023) 106058), 19 pages, all read; page 1 matches Crossref (title, four
authors in this order, venue). The suffix `-c` follows the bundle's
publication-order rule among the three De Vanna 2023 sources. Equation, table
and figure numbers on this page are those of this version.

# Key claims

Registry notation (see the notation map): velocity $v$; the source's Ducros
sensor $\theta$ and threshold $\bar\theta$ are $\Psi_{\mathrm D}$ and $\Psi^*$
(page-local, as on the Ducros page); ghost, boundary and image points keep
the subscripts $g$, $b$, $ip$.

1. Grid counts scale as $N_{\mathrm{DNS}}\sim\mathrm{Re}^{37/14}$, $N_{\mathrm{WRLES}}\sim\mathrm{Re}^{13/7}$, $N_{\mathrm{WMLES}}\sim\mathrm{Re}$; at $\mathrm{Re}_c\approx10^7$ DNS needs about $10^{18}$ and WRLES about $10^{13}$ points (§1, after Chapman and Choi & Moin). **Stated**
2. The wall model imposes the wall stress and heat flux by augmenting the viscosity and diffusivity at the boundary while keeping no-slip and isothermal/adiabatic conditions, which the authors say has never been done in compressible conditions and only partially in incompressible ones (§1). **Stated**
3. The method switches locally and dynamically between wall-resolved and wall-modelled treatment by the resolution criterion $\Delta x^+_w<40$, $\Delta y^+_w<5$, $\Delta z^+_w<20$ (Eq. 21) (§3.5). **Stated** (criterion); behaviour **Shown** in Fig. 19
4. The ghost-point values are $\mu^{\mathrm{tot}}_g=2\mu_{\mathrm{eff}}-\mu^{\mathrm{tot}}_{ip}$, $\lambda^{\mathrm{tot}}_g=2\lambda_{\mathrm{eff}}-\lambda^{\mathrm{tot}}_{ip}$ with $\mu_{\mathrm{eff}}=(\tau^{\mathrm{WM}}_w/\tau^{\mathrm{WR}}_w)\mu_w$, $\lambda_{\mathrm{eff}}=(q^{\mathrm{WM}}_w/q^{\mathrm{WR}}_w)\lambda_w$ (Eqs. 24–25), and $\mu_{\mathrm{eff}}\to\mu_w$, $\lambda_{\mathrm{eff}}\to\lambda_w$ as the near-wall resolution increases (§3.5). **Stated**
5. The whole algorithm (solver, IBM, wall model) is explicit with compact supports and ports to multi-GPU without special MPI treatment; ray tracing, ghost flagging and interpolation coefficients are computed once at start (§3.6). **Stated**
6. Channel, bulk Mach 0.1, $\mathrm{Re}_\tau$ 590–20000: the fit $\mathrm{Re}_\tau=\alpha_{\mathrm P}\mathrm{Re}_b^{\beta_{\mathrm P}}$ gives $0.084$, $0.89$ against $0.079$, $0.89$ (DNS fit) and $0.09$, $0.88$ (Pope) (Table 2, Fig. 5). **Shown**
7. Channel mean velocity and TKE agree with DNS apart from a "mild log-layer mismatch, typical of WMLES"; above $\mathrm{Re}_\tau=2000$ results are minimally sensitive to resolution (§4.1, Fig. 6). **Shown**
8. $\mathrm{Re}_\tau\approx2\times10^4$ is beyond DNS and WRLES, so this case is compared only with Reichardt's law (§4.1). **Shown**/**Stated**
9. Pipe flow inside an immersed square block, $\mathrm{Re}_\tau$ 500–6000: the friction factor is almost superimposed on DNS and Prandtl's law, slightly high at the lowest $\mathrm{Re}$, attributed to the fully developed thin-layer assumptions of the wall model (§4.2, Fig. 9). **Shown**
10. Pipe mean velocity overlaps DNS; velocity fluctuations are systematically underestimated (§4.2, Fig. 10). **Shown**
11. Mach 2 boundary layer, $\mathrm{Re}_\tau$ 250–2000: $c_f$ slightly overestimated against DNS, less so as $\mathrm{Re}_\tau$ grows; $\mathrm{Re}_\tau=2000$ is "double the maximum available in the literature" and is compared with a power-law fit to the DNS (§4.3, Eq. 32, Fig. 13). **Shown**
12. The digital-filter inflow on Musker's profile gives a fully developed turbulent boundary layer about $10\delta_0$ downstream (§4.3). **Stated**
13. The hybrid of the central scheme and TENO-A7 with threshold 0.1 "increases the simulation's stability without excessively penalizing the natural deployment of the wall turbulence" (§4.3, citing [De Vanna et al. (2023a)](/sources/devanna-2023.md)). **Stated**
14. Compression ramp, $M_\infty=2.91$, 24°, $\mathrm{Re}_\tau\approx320$: separation at $x^*=-4.0,-4.0,-3.2$ and reattachment at $0.56,0.80,0.67$ on the coarse, medium and fine grids (Table 5). **Shown**
15. The wall-model activation sensor (0 resolved, 1 modelled) is active in about half of the samples for $x^*<-10$, near zero in the bubble (minimum at $x^*\approx-3.5$) and steadily 1 on the ramp (§4.4.2, Fig. 19). **Shown**
16. Negative mean wall velocities are recovered although the equilibrium model cannot produce them, because the bubble is treated as wall-resolved (§4.4.2–4.4.3). **Shown**
17. Coarse and medium grids show a λ-shock whose rear branch is non-physical, attributed to laminarizing turbulent viscosity at low resolution, a smeared primary shock and the absence of a pressure-gradient correction in the wall model; it weakens with refinement (§4.4.3, Fig. 18). **Shown** (causes **Stated**)
18. Wall pressure converges to DNS with refinement, with a mild deviation in the initial rise, and recovers the shock–expansion value downstream (§4.4.3, Fig. 20a). **Shown**
19. The bubble is overpredicted, separation about one $\delta$ upstream of DNS, and recovery on the ramp is delayed; equilibrium regions are grid-independent, and a non-equilibrium wall model would be needed in the bubble (§4.4.3). **Shown**
20. The nominal inviscid shock angle of the ramp is $43.58°$ (§4.4). **Stated**; the θ–β–M relation with $M=2.91$, $\gamma=1.4$, $24°$ gives $43.578°$. *(compiler check, not in the sources.)*
21. The modified Ducros sensor is "found peculiarly accurate" in low-resolution WMLES, where ENO-like detection misreads noise as shocklets (§3.2). **Stated**
22. The semi-conservative viscous formulation equals central differences of the same order for uniform properties and gives "strong preservation and accurate telescoping" for variable viscosity; sixth order is used (§3.3). **Stated**

# Printed slips

- Eq. (10b): the left-hand derivative is printed $dT_{wm}/dn$, the independent variable being $y$ everywhere else.
- §3.5, step 3: "$\tau^*_w=\sqrt{u^*_\tau/\rho_w}$" is dimensionally inverted; the relation used in §4.1 is $u_\tau=\sqrt{\tau_w/\rho_w}$.
- Eq. (27): the 3D wall-parallel speed $\sqrt{(\tilde ut_1+\tilde vt_2+\tilde wt_3)^2}$ is the projection on one tangent only, unlike Eq. (19), which keeps two tangential components.
- Superscript case: $\tau^{wm}_w$, $q^{wm}_w$ (Eq. 23) against $\tau^{\mathrm{WM}}_w$, $q^{\mathrm{WM}}_w$ (Eq. 25); $\theta_{WM}$ against $\theta_{wm}$ (§4.4.2). $\tau^{\mathrm{WR}}_w$ and $q^{\mathrm{WR}}_w$ are not defined.
- Fig. 2 caption repeats the caption of Fig. 1.
- §4.3 calls the four Mach 2 cases "adiabatic" and then speaks of the block enforcing "wall temperature isothermality" ($T_{\mathrm{rat}}=1$ reconciles them).
- Table 1, $\Delta y^+$: for tch2–tch9 the printed values are exactly half the uniform spacing $2.6\,\mathrm{Re}_{\tau,0}/N_y$ (e.g. $2.6\times1000/78/2=16.7$), but for tch1 half the spacing is $9.83$, not the printed 7.6; Table 4 follows the same half-spacing convention, while pipe Table 3 prints the full spacing. *(compiler check, not in the sources.)*
- Table 3, tpi2: $\Delta z^+=2\pi\times1217/96=79.65$ against the printed 79.2. *(compiler check, not in the sources.)*
- §4.4.3 says the bubble spans "up to $x^*\approx1$"; Table 5 gives reattachment at 0.56–0.80.
- $\theta$ denotes both the Ducros sensor and the ramp angle; $\beta$ the adiabatic/isothermal switch (Eq. 18), the exponent of Eq. (28) and the shock angle; $\lambda$ both the conductivity and the pipe friction factor.
- Ref. [63] prints "Shu CW" twice; [82] "Lelef S"; [52] prints given names as surnames ("Michele C, Matteo B").

# Notation map

| De Vanna et al. (2023c) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\tilde u_i$; $u,v,w$ | $v$; $v_1,v_2,v_3$ | Favre-filtered velocity; **$u$ is the conserved vector in the registry** |
| $\bar\phi$, $\tilde\phi$ | kept | Reynolds and Favre filters (LES), not cell averages |
| $\mathbf U$, $\mathcal N(\mathbf U)$ | $u$, $\mathcal L(u)$ | conserved variables and spatial operator |
| $\theta$, $\bar\theta$, $\epsilon_0$ | $\Psi_{\mathrm D}$, $\Psi^*$, $\epsilon_{\mathrm D}=\epsilon_0^2$ (page-local on [Ducros shock sensor](/definitions/ducros-shock-sensor.md)) | **$\theta$ is the Zhang–Shu factor and also the ramp angle in the source** |
| $\theta_{WM}$ | kept, page-local | wall-model activation sensor, 0/1 |
| $\mathbf x_g$, $\mathbf x_b$, $\mathbf x_{ip}$, $\mathbf x_{int}$ | kept | ghost, boundary, image and exchange points |
| $\mu_{\mathrm{eff}}$, $\lambda_{\mathrm{eff}}$ | kept, page-local on [wall-modelled LES](/methods/wall-modeled-les.md) | effective wall viscosity and conductivity |
| $\lambda$ | kept | thermal conductivity; also the friction factor (Eq. 29) — **collision in the source** |
| $\alpha$, $\beta$ (Eq. 18b) | kept, page-local | adiabatic/isothermal switch; **collide with $\alpha_k$, $\beta_k$** |
| $\alpha$, $\beta$ (Eq. 28) | $\alpha_{\mathrm P}$, $\beta_{\mathrm P}$ | Pope-type fit constants |
| $\kappa$ | kept as von Kármán constant, page-local | **$\kappa$ is the kinetic energy in the registry** |
| $C_T$ | $C_T$ | adaptive in TENO-A; values not printed |
| CFL, FO | $\nu=0.5$, Fourier number 0.1 | |
| $M_b$, $M_\infty$, $Re_\tau$, $Re_b$ | $M_b$, $M_\infty$, $\mathrm{Re}_\tau$, $\mathrm{Re}_b$ | |

# Reference list

90 printed references in numbered Elsevier style ([1]–[90]), merged complete
into the [bibliography](/bibliography.md) with `citedby` `devanna-2023-c`.
Refs. [46] (URANOS, Comput. Phys. Commun. 287:108717) and [68] (Comput.
Fluids 250:105710) are both De Vanna et al. 2023; by printed order they
would take the suffixes in the reverse of the bundle's slugs, so they are
merged as [De Vanna et al. (2023b)](/sources/devanna-2023-b.md) and
[De Vanna et al. (2023a)](/sources/devanna-2023.md), identified by DOI and
volume:page. DOIs are printed for all items except [50], [78], [81], [87].
Refs. [63], [82] and [52] carry printed author errors (see Printed slips),
kept as printed. No unparseable items and no printed duplicates.

# Pages created or updated

Chunk 5 (2026-10-22), cited further in chunks 6–12 (2026-10-23/30). This source is cited on:

* [Adaptive TENO (TENO-A, TENO-AA)](/methods/adaptive-teno.md)
* [Ducros shock sensor](/definitions/ducros-shock-sensor.md)
* [Immersed-boundary and cut-cell methods](/methods/immersed-boundary-method.md)
* [Supersonic turbulent boundary layer](/benchmarks/supersonic-turbulent-boundary-layer.md)
* [Targeted ENO (TENO)](/methods/targeted-eno.md)
* [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
* [URANOS](/software/uranos.md)
* [Wall-modelled large-eddy simulation](/methods/wall-modeled-les.md)
