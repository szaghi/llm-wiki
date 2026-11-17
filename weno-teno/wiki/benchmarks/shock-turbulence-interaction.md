---
type: Benchmark
title: "Shock–turbulence interaction"
description: "Isotropic turbulence convected through a stationary normal shock in a box periodic in the transverse directions; the growth of Reynolds stresses, vorticity variances and turbulent kinetic energy across the shock is compared with linear interaction analysis and DNS, testing whether shock-capturing dissipation leaves the turbulence intact before and through the shock."
status: established
aliases: [shock/turbulence interaction, shock/isotropic-turbulence interaction, canonical shock–turbulence interaction, shock–isotropic turbulence interaction, STI]
tags: [benchmark, turbulence, central-scheme, low-dissipation]
timestamp: 2026-11-17T08:43:44Z
---

# Shock–turbulence interaction

Isotropic turbulence is carried by a uniform supersonic stream through a
normal shock held at rest in the computational frame. The box is
periodic in the two transverse directions and the turbulence enters at
the inflow. The shock is corrugated by the turbulence, and the
turbulence is amplified across it: the streamwise and transverse
Reynolds stresses and the transverse vorticity variance grow, the
streamwise vorticity variance stays nearly unchanged, and the flow
becomes axisymmetric. The references are linear interaction analysis
(LIA, after Ribner) and the DNS of Lee, Lele & Moin, as recalled by
[Ducros et al. (1999)](/sources/ducros-1999.md) (§1, §4.3). A scheme
passes when the incoming turbulence decays before the shock as
homogeneous turbulence would and the jumps across the shock match LIA
and DNS. The test isolates the conflict of every shock-capturing scheme:
enough dissipation in the shock to capture it, as little as possible
elsewhere (§1). Page-local symbols: upstream shock Mach number $M_1$,
turbulent Mach number $M_t$, reference length and speed $L_{\mathrm{ref}}$
and $U_{\mathrm{ref}}$, Reynolds stresses $\mathsf R_{ij}$ (Favre averages,
index 1 streamwise; the registry's $R$ is the eigenvector matrix),
captured-shock width $\lambda_{\mathrm{sh}}$, LES cut-off length
$\Delta_c$, and the size $L_{uvw}$ of the smallest resolved energetic
eddies, upstream mean speed $U_1$ and sound speed $c_1$, and turbulence
kinetic energy $q$.

This is a three-dimensional turbulence test. The one-dimensional
[Shu–Osher problem](/benchmarks/shu-osher-problem.md), which
[Zhang & Zhu (2024)](/sources/zhang-2024-c.md) call "the standard
shock/turbulence problem", is a model
problem of a shock running into an entropy wave, not this benchmark; the
two-dimensional single-vortex version is
[shock–vortex interaction](/benchmarks/shock-vortex-interaction.md).

## Setup of Ducros et al. (1999)

§4.3.1, Figs. 12–13, Table III. The domain is
$(L_x,L_y,L_z)=(2,1,1)L_{\mathrm{ref}}$, mean flow along $x$, periodic in
$y$ and $z$, with the shock at rest near $x=1$ (all runs are in the
shock frame, the shock initially at $x=L_x/2$, §4.2). The mean Mach
number is 1.2 upstream (Fig. 12) and, read from Fig. 15, about 0.84
downstream *(compiler
check, not in the sources: the normal-shock value for $M_1=1.2$,
$\gamma=1.4$, is 0.842)*. The inflow turbulence is not synthesized from
a prescribed spectrum but taken from the LES fields of their decaying
runs ([compressible isotropic turbulence](/benchmarks/compressible-isotropic-turbulence.md))
through Taylor's hypothesis, as Mahesh et al. did; the inlet turbulent
Mach number is about 0.075 and the intensity $\sqrt q/U_1\approx0.06$,
for which the authors consider Taylor's hypothesis valid. The flow is
inviscid (infinite Reynolds number) with the filtered-structure-function
subgrid model on in every run. The scheme is a second-order
skew-symmetric central finite-volume scheme with four-stage Runge–Kutta
time stepping and scalar Jameson–Schmidt–Turkel dissipation
([artificial viscosity](/methods/artificial-viscosity.md)), $k_2=1.5$,
either classical ($k_4=0.02$, Jameson's pressure sensor
$\varphi_{\mathrm J}$) or with $k_4=0$ and $\varphi_{\mathrm J}$
multiplied by the dilatation ratio $\Phi_{\mathrm D}$ of the
[Ducros sensor](/definitions/ducros-shock-sensor.md).

| Run | Grid | Mesh in $x$ | $k_4$ | Sensor |
|---|---|---|---|---|
| ST-1 | $64\times32\times32$ | isotropic, $\Delta x=L_{\mathrm{ref}}/32$ | 0.02 | $\varphi_{\mathrm J}$ |
| ST-2 | $64\times32\times32$ | isotropic | 0 | $\varphi_{\mathrm J}\Phi_{\mathrm D}$ |
| ST-3 | $262\times32\times32$ | refined smoothly to $\Delta x\approx\tfrac18L_{\mathrm{ref}}/32$ just before the shock and kept fine to the outflow | 0.02 | $\varphi_{\mathrm J}$ |
| ST-4 | $262\times32\times32$ | as ST-3 | 0 | $\varphi_{\mathrm J}\Phi_{\mathrm D}$ |
| ST-5 | $156\times32\times32$ | refined only around the shock | 0 | $\varphi_{\mathrm J}\Phi_{\mathrm D}$ |

The smallest resolved energetic scale of the incoming turbulence is
$L_{uvw}=L_{\mathrm{ref}}/16$. Statistics are averages over $y$, $z$ and
time (Eq. (26)), with Reynolds and Favre fluctuations (Eq. (27)) and
$\mathsf R_{ij}$ the Favre-averaged Reynolds stress (Eq. (28)); sampling
covers $12L_{\mathrm{ref}}/U_{\mathrm{ref}}$ (ST-1, 2, 5) or
$5L_{\mathrm{ref}}/U_{\mathrm{ref}}$ (ST-3, 4).

## Data

Growth of the Reynolds stresses between the pre-shock region and
$x\approx1.4$, about one integral length downstream (Table IV):

| Quantity (post/pre shock) | DNS, Lee et al. (1993) | LIA | ST-2 | ST-4 | ST-5 |
|---|---|---|---|---|---|
| $\mathsf R_{11}$ | 19 % | 34 % | 25 % | 37 % | 41 % |
| $\mathsf R_{22}$ | 4.4 % | 10 % | 0 % | 6 % | 6 % |

The DNS and LIA values are read by the authors from Figs. 5 and 4 of Lee,
Lele & Moin (1993). The transverse vorticity variance grows by 85 %
(ST-4) and 80 % (ST-5), against 60–80 % in the DNS of Lee, Lele & Moin
(1997), depending on the turbulent Reynolds number, and about 80 % from
LIA (§4.3.4).

## What the test exposes

- **Dissipation away from the shock.** With Jameson's pressure sensor
  alone (ST-1, ST-3) the incoming turbulence decays spuriously before it
  reaches the shock, in kinetic energy and in vorticity; with the Ducros
  factor (ST-2, ST-4) the pre-shock decay matches homogeneous decay
  through Taylor's hypothesis, independently of the streamwise
  resolution. The turbulent Mach number falls from 0.075 at the inlet to
  0.061 (ST-1, ST-3) or 0.068 (ST-2, ST-4) just ahead of the shock
  (§4.3.3, Figs. 16–17, 19–20). In the dissipation budget away from the
  shock, the subgrid dissipation dominates, but the classical
  second-order term can be "non-negligible (around 10%)"; with the Ducros
  factor it becomes negligible (ST-2 and ST-5). Inside the shock the numerical dissipation
  dominates the subgrid dissipation, so the subgrid model matters little
  there "at least for the numerical scheme used here" (§4.4, Fig. 24).
- **Dissipation inside the shock: scale separation.** The second-order
  term captures the shock in about three cells, so on the coarse grid
  $\lambda_{\mathrm{sh}}\approx\Delta_c\approx L_{\mathrm{ref}}/16\sim L_{uvw}$
  (ST-2). When the smallest resolved energetic eddies are as small as the
  captured shock, the shock-capturing dissipation damps them: smaller
  growth of the kinetic energy, of $\mathsf R_{ii}$ and of the transverse
  vorticity, and a spurious drop of the streamwise vorticity variance,
  which LIA and DNS predict nearly unchanged and which ST-1, 3, 4, 5 keep
  (§4.3.4, §5). On the refined grid $\lambda_{\mathrm{sh}}\approx3\Delta x\approx3L_{\mathrm{ref}}/256$
  separates the two scales (ST-4); ST-1 escapes the problem only because
  its pre-shock dissipation has already removed the small energetic
  scales. With refinement, $\mathsf R_{22}$ peaks ahead of the minimum of
  $\mathsf R_{11}$, as in the DNS (ST-4, ST-5), which the coarse grid does
  not reproduce (Fig. 18). The authors propose local (automatic) mesh
  refinement at the shock, or pre-filtering the resolved field to a
  cut-off larger than the shock width (§5).
- **Refinement side effect.** Refining the mesh well upstream of the
  shock lets the infinite-Reynolds-number turbulence cascade from the
  cut-off $k_{c1}\approx32/L_{\mathrm{ref}}$ into the new scales up to
  $k_{c2}\approx8\cdot32/L_{\mathrm{ref}}$, which raises both vorticity
  components far from the shock independently of it (ST-3, ST-4);
  refining only just before and around the shock (ST-5) avoids it
  (§4.3.4, §5).
- **Mean flow.** The mean variables follow modified Rankine–Hugoniot
  jumps (after Lele), with slight over- and undershoots behind the shock
  before relaxing to the laminar values, more pronounced on the refined
  grid (§4.3.2, Figs. 14–15).

## Earlier and later computations, as recalled

- **DNS by local shock capturing.** Ducros et al. (§1) recall DNS of the
  problem at upstream Mach numbers 1.05–2, turbulent Mach numbers
  0.05–0.102 and Taylor Reynolds numbers 6–20 with sixth-order compact
  schemes, and up to $M_1=3$ with a sixth-order ENO scheme applied only
  shock-normal and in a zone covering about 10 % of the domain around the
  known shock (Lee, Lele & Moin 1997; Mahesh et al.), possible only
  because the shock position and direction are known a priori.
  [Pirozzoli (2011a)](/sources/pirozzoli-2011.md) (§3.2) recalls the same
  hybrid of a sixth-order compact and a sixth-order ENO scheme, with ENO
  over 12 points upstream and 12 downstream of the mean shock.
- **Later DNS.** Pirozzoli (2011a, §5) names Larsson & Lele (2009) as
  revisiting the problem at high resolution with a hybrid central/WENO
  scheme with convective splitting, and attributes the slow grid
  convergence of "apparently simple" shock/turbulence calculations to
  the first-order accuracy of shock capturing downstream of shocks
  (§3.5; [order of accuracy behind shocks](/results/order-of-accuracy-behind-shocks.md)).
  The review adds that spurious post-shock oscillations, strongest behind slowly
  moving shocks, may spoil shock/turbulence predictions (Johnsen et al.
  2010, as recalled), and lists a study of their effect as an open issue
  (§6, Future Issue 1).
- **Sensors.** Pirozzoli (2011a, §6) finds that the Ducros sensor "was
  found to perform reasonably well in many shock/turbulence interaction
  problems, particularly with some minor case-by-case modification and
  tuning of the threshold value"
  ([troubled-cell indicators](/definitions/troubled-cell-indicator.md),
  [hybrid schemes](/methods/hybrid-weno.md)).

## Qualifications

- The conclusions come from a second-order scheme; the authors state
  that they "may be modified when using higher order numerical schemes"
  (§6). Only one Mach number (1.2) and one inflow turbulence are run in
  three dimensions.
- The runs are at infinite Reynolds number, so the comparison with
  viscous DNS is qualitative; the authors attribute their larger
  amplification to the missing molecular viscosity and the reduced
  numerical dissipation (§4.3.3, §6).
- The text attributes the LIA estimates to its reference [54] (M. J. Lee,
  Kim & Moin, a homogeneous-shear paper), while the note to Table IV takes
  them from Fig. 4 of [7] (Lee, Lele & Moin 1993); [54] is most likely
  misnumbered *(compiler check, not in the sources)*. §4.4 is titled "A Posteriori Test on the Modified Sensor",
  while the abstract, §1 and §5 call the same analysis a priori.
- Pirozzoli (2011a, §3.2, §5) classes Ducros et al.'s LES as "a
  characteristic-based nonlinear filtering scheme". In the original the
  dissipation is the scalar (spectral-radius) Jameson–Schmidt–Turkel
  term inside the numerical flux, "although we keep a scalar dissipation
  model" (§3, Eqs. (8)–(13)). The two descriptions are recorded side by
  side.
- *(Compiler check, not in the sources: the inlet values $M_t\approx0.075$
  and $\sqrt q/U_1\approx0.06$ have the ratio 1.25, close to $M_1=1.2$,
  consistent with the definition $M_t=\sqrt q/c$ of §2, $q$ the turbulence
  kinetic energy, so $M_t/(\sqrt q/U_1)=U_1/c_1=M_1$.)*

# Citations

- [Ducros et al. (1999)](/sources/ducros-1999.md) — §1; §2; §3, Eqs. (8)–(13); §4.2; §4.3, Eqs. (26)–(28), Tables III–IV, Figs. 12–20; §4.4, Figs. 21–24; §5; §6.
- [Pirozzoli (2011a)](/sources/pirozzoli-2011.md) — §3.2; §3.5; §5; §6, Future Issue 1.
- [Zhang & Zhu (2024)](/sources/zhang-2024-c.md) — Ex. 3.8 (the name "standard shock/turbulence problem" for the 1D problem).
