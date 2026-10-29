---
type: Method
title: "Inflow turbulence generation"
description: "How a scale-resolving simulation is fed with turbulence at its inflow or in its initial field: recycling–rescaling, precursor planes and stored fluctuation libraries with compressible scaling laws, digital-filter and Fourier-mode synthetic turbulence, forcing, wall blowing and suction, geometric tripping, or laminar inflow by choice, with the recovery each needs and the errors each leaves."
status: established
aliases: [turbulent inflow generation, synthetic inflow turbulence, synthetic turbulence generator, STG, recycling–rescaling inflow, recycling inflow, digital filter inflow, precursor inflow, MDSRFG, random flow generation, turbulence fluctuation library, TFL, rescaling–reintroduction]
tags: [les, dns, boundary-layer, wmles, compressible]
timestamp: 2026-10-29T10:04:00Z
---

# Inflow turbulence generation

A DNS or LES of a spatially developing flow (a boundary layer, a
turbomachinery passage, a jet) needs a time-dependent velocity field on its
inflow plane whose statistics match a turbulent state: the mean profile, the
Reynolds stresses $R_{ij}$, length and time scales and, ideally, the
coherent near-wall structures. The methods differ in
where the fluctuations come from: from the simulation itself
(**recycling–rescaling**, auxiliary or precursor boxes), from a stochastic
construction with prescribed statistics (**synthetic turbulence**: digital
filters, Fourier modes, forcing), or from a disturbance that triggers
transition inside the domain (**blowing and suction**).
[Mo et al. (2023)](/sources/mo-2023.md), §I, sort the methods into four
classes, transition-inducing, recycling–rescaling, synthetic generation and
turbulence libraries (stored precursor fluctuations), each with its own
shortcomings, and state, citing Mullenix et al., that the
transition-inducing route needs at least 50 boundary-layer thicknesses to
reach a developed state. Every method leaves
an adaptation ("induction" or "recovery") region downstream of the inlet in
which the flow is not yet the target state, and the sources measure it.

## Recycling–rescaling

The velocity (and, in compressible flow, temperature and density) on a plane
some distance downstream is rescaled, inner and outer layers separately, to
the target thickness at the inlet and fed back.

- [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) and
  [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) use the
  Lund–Wu–Squires method with the recycling plane at $890\theta_0$ from the
  inlet ($\theta_0$ the inlet momentum thickness) for wall-modelled LES of
  the zero-pressure-gradient layer (see
  [turbulent boundary layers](/benchmarks/turbulent-boundary-layer.md)).
- In compressible DNS: [Cogo et al. (2022)](/sources/cogo-2022.md), §2, use
  the method of Pirozzoli, Bernardini & Grasso with the recycling station at
  $80\delta_{\mathrm{in}}$, "long enough" to decorrelate the recycled eddies;
  [Huang et al. (2022)](/sources/huang-2022.md), §2.3, a modified version of
  Duan et al. with the recycling plane at $52.7\delta_i$;
  [Zhang et al. (2022)](/sources/zhang-2022-b.md), §2, the
  Pirozzoli–Bernardini–Grasso method in [STREAmS](/software/streams.md)
  for six layers from Mach 0.5 to 8, chosen because it is "less noisy
  than a synthetic inflow like the digital filtering method".
- [Maeyama & Kawai (2023)](/sources/maeyama-2023.md), §3, use the
  rescaling–reintroduction of Urbin & Knight, which they cite, with the
  recycle station at $35\delta_0$ ($\delta_0$ about the inlet 99%
  thickness) for a [wall-modelled LES](/methods/wall-modelled-les.md) of a
  Mach 2.28 boundary layer under adverse pressure gradient, judge domain and
  extraction location sufficient by the criteria of Morgan et al. (as cited),
  and check the outcome by $C_f(Re_\theta)$ (Fig. 3).
- An **auxiliary box**: [Helm & Martín (2022)](/sources/helm-2022.md), §II,
  run a separate boundary layer with recycling–rescaling over a long box and
  interpolate its rescaling plane, in time and space, onto the inlet of the
  shock-interaction domain, so that the long rescaling length decorrelates
  the eddies and the incoming state stays fixed over the long records the
  low-frequency shock motion needs. They attribute a slight log-law
  overshoot of their Mach 3 DNS to recycling forcing from a shorter
  rescaling length (§III B).
- **Chained boxes**: [Huang et al. (2022)](/sources/huang-2022.md), §2.3,
  split each DNS into three overlapping streamwise boxes, saving four planes
  of primitive variables of one box (the width of the WENO stencil) as the
  spline-interpolated inflow of the next.
- [Krais et al. (2021)](/sources/krais-2021.md), §7.3, combine
  recycling–rescaling "similar to Lund" with anisotropic linear forcing for
  a zonal LES of a cavity in [FLEXI](/software/flexi.md).
- **A periodic precursor without rescaling**:
  [Steinhausen et al. (2023)](/sources/steinhausen-2023.md) (read in arXiv
  v1), §2.1, run a separate periodic non-reacting
  [channel](/benchmarks/turbulent-channel-flow.md) ($14\times3\times2$
  half-widths, 60 million cells, wall spacing at $y^+=0.24$) and write
  inflow planes every 3 µs for a reacting simulation of flame–wall
  interaction in the same channel; no recovery length is reported.
- **Precursor pipe flows for a burner**: [Zhang et al. (2023)](/sources/zhang-2023-c.md),
  §2, feed the LES of a multi-regime burner flame with inlet turbulence
  from computed fully developed pipe and annular-pipe flows for the jet and
  the outer slot, and prescribe a laminar annular profile for the inner
  slot, whose Reynolds number is much lower.
- **Precursor isotropic turbulence through the inlet of a moving frame**:
  [Iwata et al. (2023)](/sources/iwata-2023.md), §II C, Eq. (1), run a
  detonation in a detonation-fixed frame (inlet velocity equal to the
  detonation speed plus the fluctuations) and take the fluctuations from a
  decaying compressible [isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
  in a periodic 1.92 mm cube on the same 4 µm grid, initialized with the
  spectrum $E(k)=16\sqrt{2/\pi}\,(u'^2/k_e)(k/k_e)^4\exp[-2(k/k_e)^2]$ (the
  form used by Coulon et al. 2023, below) and run until the
  velocity-derivative skewness lies between $-0.6$ and $-0.4$, giving
  $Re_\lambda=240$ and $M_t=0.30$ at the inlet (Table I); see
  [direct numerical simulation](/definitions/direct-numerical-simulation.md).
- **Stored precursor planes reused cyclically**:
  [Mukha et al. (2025)](/sources/mukha-2025.md) (read in arXiv v1), §IV.A,
  feed wall-modelled LES of a zero-pressure-gradient boundary layer in
  [Nek5000](/software/nek5000.md) with inflow planes from a SIMSON DNS at
  $Re_\theta=790$, interpolated onto the coarser meshes in space and cubically
  in time; the stored record spans about $450\,\delta_{99}/U_0$ ($U_0$ the
  free-stream velocity, page-local) and is reused cyclically. The shape
  factor agrees with the references "after inflow adaptation"; four
  elements per inlet $\delta_{99}$ in the spanwise direction are already
  wall-resolved resolution (about $10\delta_\nu$), so the wall-modelled
  meshes must be coarsened downstream (§IV.A–B, Figs. 12–13; see
  [wall-modelled LES](/methods/wall-modelled-les.md)).

- **A concurrent precursor for an atmospheric boundary layer**:
  [Zhang et al. (2022e)](/sources/zhang-2022-i.md), §II A–B, feed their
  wall-modelled LES of wind-turbine wakes over hills from a precursor run
  concurrently (the method of Stevens, Graham & Meneveau, which they cite),
  a neutral boundary layer driven by a constant pressure gradient
  $u_\tau^2/H_{\mathrm{dom}}$ ($H_{\mathrm{dom}}$ the domain height, page-local) without viscous
  term. They take the linear profile of the total (resolved plus subgrid)
  shear stress, $1-y/H_{\mathrm{dom}}$ in units of $u_\tau^2$, as the evidence of
  statistical stationarity, and match the mean velocity, the three
  velocity variances and the shear stress of the wind-tunnel inflow
  (Eq. 13, Fig. 3); see [actuator line and disk models](/methods/actuator-line-model.md).
- **A separate flat-plate precursor for a separating flow**:
  [Zhou & Bae (2024)](/sources/zhou-2024-b.md), §2.3, Fig. 3, feed their
  wall-modelled LES of the [Gaussian bump](/benchmarks/gaussian-bump.md)
  from a flat-plate LES with the rescale-and-recycle method of Lund et al.
  (domain $0.09L\times0.15L\times0.08L$, $L$ the bump length, isotropic
  cells of $2.19\times10^{-4}L$, equilibrium stress-balance wall model,
  dynamic Smagorinsky model; 100 flow-through times of transient and 150
  of collection). The plane extracted $0.025L$ upstream of the precursor
  exit has $Re_\tau\approx620$, $\delta_{99}/L=0.0061$ and
  $Re_\theta\approx1074$, against about 1035 in the reference simulation of
  Uzun & Malik, which used a different inflow method; the mean velocity
  follows $u^+=\ln(y^+)/0.41+5.2$. Data above $y/L=0.15$ are set to the
  free stream. A second precursor run with the anisotropic
  minimum-dissipation model ($Re_\theta\approx1126$, $Re_\tau\approx630$)
  changes the bump-flow velocity profiles negligibly (App. A, Fig. A.21).
- **A periodic precursor channel coupled one-to-one**:
  [De Cosmo et al. (2025)](/sources/decosmo-2025.md), §3.4, feed an
  implicit LES of a channel with a two-Gaussian bump on one wall (the
  Banchetti et al. geometry, $12h\times2h\times4h$) from a flat periodic
  channel run alongside, through a one-to-one matching interface with the
  same $y$–$z$ mesh, bulk Reynolds number and time step; the mean wall
  quantities on the bump are on
  [turbulent channel flow](/benchmarks/turbulent-channel-flow.md).
- **The method in historical perspective**:
  [Kim & Leonard (2024)](/sources/kim-2024-b.md), §4.6, record that the
  recycling method of Lund et al. (1998), or a variant of it, "has since
  been used commonly" as a turbulent inflow condition, with an advective
  outflow condition (Lowery & Reynolds) "allowing turbulence to leave the
  computation softly"; in the first spatial mixing-layer simulations the
  inlet forcing ranged from inviscid shear-layer eigenfunctions to random
  perturbations, to shorten the development length (§4.2). Before spatial
  inflows, Spalart's boundary-layer DNS used streamwise-periodic conditions
  with a multiscale procedure approximating the local effects of
  streamwise growth, valid only for mildly growing layers (§3.5); see
  [direct numerical simulation](/definitions/direct-numerical-simulation.md).

## Turbulence fluctuation libraries for compressible boundary layers

A **turbulence fluctuation library** stores a time series of velocity
planes from a precursor DNS and, at the inflow of the target simulation,
adds the rescaled fluctuations to a mean profile.
[Mo et al. (2023)](/sources/mo-2023.md) build one in the finite-difference
code ACANS (seventh-order WENO-Z, fourth-order central viscous fluxes,
third-order Runge–Kutta; §II A) from a Mach 2.25 flat-plate DNS with
blowing–suction transition: 65,536 planes at the DNS step of 5 ns at a
station with $\delta=2.08$ mm and $Re_\tau\approx770$, a span of about 4.4
$\delta/u_\tau$, storing velocity only, with $u_\tau$ and the mean density
profile (§III A, Table IV). Mean profiles at the target come from a
[Spalart–Allmaras](/methods/spalart-allmaras-model.md) RANS. Page-local
symbols: subscripts $w$, $e$, $r$ for wall, edge and recovery values;
$s_{\mathrm{RA}}=1.16$ is the Reynolds analogy factor (registry §11).

**Velocity** (Eqs. 15–17, generalizing Martin 2007 as cited): the
density-scaled fluctuation $\sqrt{\langle\rho\rangle/\rho_w}\,u_i'/u_\tau$
is the same in library and target at equal scaled position, the spanwise
coordinate scaled by $\delta_\nu$, the wall-normal one by $\delta_\nu$ in
the inner layer and by $\delta$ in the outer layer, the two blended by a
tanh function between $0.2\delta$ and $0.5\delta$ (an application of
[Morkovin's hypothesis](/definitions/morkovin-hypothesis.md); Mo et al.
cite Duan et al. for its validity below Mach 12 and above a
wall-to-recovery temperature ratio of 0.12).

**Thermodynamics.** Martin's laws, from the strong Reynolds analogy,
$$\frac{T'}{\langle T\rangle}\approx-(\gamma-1)M^2\frac{u'}{\langle u\rangle},\qquad \frac{\rho'}{\langle\rho\rangle}=-\frac{T'}{\langle T\rangle}$$
(Eqs. 18–19), assume $Pr=1$, negligible total-temperature fluctuation and
an adiabatic wall. Mo et al. (§IV A) replace them by the instantaneous
form of Gaviglio's analogy due to Yu & Xu (as cited),
$T'\approx(\partial\langle T\rangle/\partial\langle u\rangle)\,u'$, with the
derivative taken from the generalized Reynolds analogy of Zhang et al.
(as cited, Eqs. 11–13),
$$\frac{\langle T\rangle}{T_e}=\frac{T_w}{T_e}+\frac{T_r-T_w}{T_e}\,f\Big(\frac{\langle u\rangle}{u_e}\Big)+\frac{T_e-T_r}{T_e}\Big(\frac{\langle u\rangle}{u_e}\Big)^2,\qquad f(q)=(1-s_{\mathrm{RA}}Pr)\,q^2+s_{\mathrm{RA}}Pr\,q,$$
with $Pr=0.72$ (printed form of the derivative in Qualifications), and by a
density law from the equation of state that keeps the $\rho'T'$
correlation and drops only $p'$ (Eqs. 24–25),
$$\frac{\rho'}{\langle\rho\rangle}=-\frac{T'/\langle T\rangle}{1+T'/\langle T\rangle},$$
of which Eq. (19) is the linearization; it keeps $\rho'/\langle\rho\rangle>-1$,
so the density stays positive whenever $T'/\langle T\rangle>-1$. At the
Mach 7.25 inflow Eq. (19) gives $\rho'/\langle\rho\rangle<-1$ near
$y/\delta=0.8$, a negative density (Fig. 10c), and Martin's remedy of
multiplying the analogy by a factor below 0.8 distorts the positive tail of
the density PDF (§IV B).

**Tests** (§III C, §IV B–C; recovery distance $L_r$ defined from the
inlet to the peak of the averaged $C_f$ that follows its initial drop):

- a Mach 2.9 adiabatic layer (Ringuette et al. experiment, inflow
  $Re_\tau=340$) with Martin's thermodynamic laws recovers in
  $L_r\approx10\delta_{\mathrm{in}}$ ($\delta_{\mathrm{in}}$ the inflow
  thickness, page-local) and matches the measured $C_f$, mean velocity and
  streamwise fluctuation (Table II, Figs. 7–8);
- a Mach 7.25 cold-wall layer ($T_w=562$ K, Williams et al. experiment,
  inflow $Re_\tau=155$) with the new laws runs stably and matches the
  measured $C_f$, van Driest velocity and Morkovin-scaled fluctuations; the
  total-temperature fluctuation reaches about 10%, the RMS ratio of the
  two sides of Eq. (18) is about 0.8 over most of the layer, that of the new
  law about 1, and the $\rho'T'$ term exceeds the density and temperature
  fluctuations at $y^+=100$ while $\lvert p'/\langle p\rangle\rvert<0.2$
  with high probability (Figs. 11–17);
- the recovery there is $L_r\approx24\delta_{\mathrm{in}}$ with the
  $Re_\tau=770$ library and about $11\delta_{\mathrm{in}}$ with libraries at
  $Re_\tau=350$ and 186, built by lowering the free-stream density of the
  precursor (Fig. 19). The authors locate the cause in the mapping: the
  spanwise coordinate is scaled by $\delta_\nu$ everywhere but the
  wall-normal one by $\delta$ in the outer layer, and since
  $Re_\tau=\delta/\delta_\nu$, the two stretchings agree only for matched
  $Re_\tau$; otherwise outer-layer structures are distorted in span (mass-flux
  autocorrelations at $y/\delta=0.3$, Figs. 21–22), the outer stresses decay
  one $\delta$ downstream and $C_f$ drops (Fig. 23). They recommend a library
  at a friction Reynolds number close to the target (§V).

## Synthetic turbulence

A stochastic field with prescribed one-point statistics and length scales is
superimposed on the mean inflow.

- **Digital filters.** [Hoy & Bermejo-Moreno (2022)](/sources/hoy-2022.md),
  §2–3, use the digital filter of Klein, Sadiki & Janicka with the extensions
  of Xie & Castro and of Touber & Sandham for the boundary layer of a
  wall-modelled shock interaction; [Huang et al. (2022)](/sources/huang-2022.md)
  use a digital filter (Dhamankar et al.; Huang & Duan) as the alternative
  to recycling in their recovery study below.
  [Idelsohn et al. (2024)](/sources/idelsohn-2024.md), §2.10.5, impose a
  flat-plate boundary-layer profile with digital-filter fluctuations (Klein
  et al., as cited) ten step heights upstream of a
  [backward-facing step](/benchmarks/backward-facing-step.md) at
  $Re_h=5000$ on a 142,000-cell mesh, for their
  [pseudo-DNS](/methods/pseudo-direct-numerical-simulation.md) and a
  one-equation LES.
- **The filter coefficients.** [Shi & Yan (2023)](/sources/shi-2023.md),
  §II.C, Eqs. (19)–(26), print the implementation of Touber & Sandham's
  form of the filter (as cited) for a flux-reconstruction implicit LES:
  zero-mean unit-variance random numbers are filtered with
  $b_k=\tilde b_k/(\sum_j\tilde b_j^2)^{1/2}$, $\tilde b_k=\exp(-\pi k/n)$,
  $n$ the integral length in grid units and the stencil half-width at least
  $2n$, which reproduces an exponential correlation
  $\exp(-\pi x/(2I_x))$ ($I_x$ the integral length, page-local), "not the
  same as the two-point correlation in the wall-bounded turbulence, but
  still a valid approximation"; the inflow plane is split into three
  wall-normal zones of uniform spacing for the two-dimensional filter, and
  the streamwise correlation is replaced by a temporal one,
  $v^{\mathrm{new}}=v^{\mathrm{old}}\exp(-\pi\Delta t/(2\tau_I))+v\sqrt{1-\exp(-\pi\Delta t/\tau_I)}$,
  $\tau_I=I_x/U$ (page-local). The paper does not state how the filtered
  signals become velocity fluctuations (no prescribed stress profiles are
  printed).
  [Kokkinakis et al. (2023)](/sources/kokkinakis-2023.md), §III B, use the
  filter of Klein et al. developed by Touber & Sandham (as cited), filtered
  in two dimensions only for speed, for an implicit LES of a shock/boundary-layer
  interaction over a flexible panel, with an inlet thickness of about 4.7 mm
  estimated from laminar and turbulent growth correlations.
- **Digital filters for shock interactions.** Three sources feed
  supersonic shock/boundary-layer interactions with the filter of Klein,
  Sadiki & Janicka, each with its own mean state:
  [De Vanna et al. (2022)](/sources/devanna-2022.md), §4.1, in the
  low-storage form of Kempf et al., superposed on a mean profile, with the
  initial field from a van Driest-transformed Musker profile, for a
  wall-modelled LES of the Mach 2.28 oblique interaction at inflow
  $Re_\tau=700$;
  [Yu et al. (2022)](/sources/yu-2022-e.md), §2.1, with a Musker mean
  velocity and the mean temperature and temperature fluctuations from the
  generalized Reynolds analogy of Zhang et al. (2014), for a DNS of the
  same interaction at $Re_\tau=201$ on the reference plane (the DNS that
  [Yu et al. (2023)](/sources/yu-2023.md), §2, reuse for post-shock
  recovery); and
  [Tonicello et al. (2022)](/sources/tonicello-2022.md), §2.1, in a form
  generalized to their spectral-difference discretization, with mean
  profiles from closed-form relations built on the van Driest-transformed
  velocity, the correlation tensor extrapolated from the boundary-layer
  DNS of Pirozzoli & Bernardini, and density and temperature fluctuations
  from the strong Reynolds analogy (see
  [Morkovin's hypothesis](/definitions/morkovin-hypothesis.md)), for a DNS
  of a Mach 2.91 compression/expansion ramp.
  [Yu et al. (2023b)](/sources/yu-2023-b.md), §II, use the same
  combination as Yu et al. (2022) (filter of Klein et al., Musker mean
  velocity, mean temperature from the generalized Reynolds analogy) for a
  DNS of Mach 5 oblique shock interactions over a cold wall
  ($T_w=0.75T_r$, $T_r$ the recovery temperature), but prescribe no
  temperature or density fluctuations, for numerical stability; the
  incoming layer is compared at $30\delta_{\mathrm{in}}$ from the inlet
  ($Re_\theta\approx2087$; $\delta_{\mathrm{in}}$ the inflow thickness)
  with the Mach 2 DNS of Pirozzoli & Bernardini at $Re_\tau\approx200$.
  Recovery is in the next
  section; the interactions are on
  [shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md).
- **Fourier modes.** [Morsbach et al. (2024)](/sources/morsbach-2024.md),
  §2 and §3.3, feed the synthetic turbulence generator of Shur et al.
  (randomized Fourier modes) with spanwise profiles of the six Reynolds-stress
  components and one integral length scale, superimpose the fluctuations on
  the mean state of a Riemann boundary condition, and impose the state weakly
  through a central flux on the DG inflow faces. The profiles come from the
  $Re_\theta=670$ boundary-layer DNS of Schlatter & Örlü rescaled to the
  operating point (Eqs. 5–11): velocity and stresses in wall units, and a
  length scale $L_T=(k^+)^{3/2}/\varepsilon^+$ converted to physical units,
  joined to a free-stream length scale by $L_T=\max(L_{T,\mathrm{BL}},L_{T,\mathrm{free}})$,
  with the measured free-stream anisotropy and the stress tensor rotated from
  streamline-aligned to Cartesian axes. [Carlsson et al. (2023)](/sources/carlsson-2023.md)
  use the same generator only to seed fluctuations in a channel for one
  convective time. [Möller et al. (2024)](/sources/moller-2024.md) (read in
  the accepted manuscript), §II.E, §III.A, use it in the TRACE
  implementation they attribute to Morsbach & Franke, for detached-eddy
  simulation of a compressor cascade: a bulk state (velocity, density, static
  pressure) extracted from a RANS precursor feeds the generator, the inflow
  turbulence intensity is 3.25%, and the inlet specific dissipation rate
  is set as $\omega=\sqrt k/(\beta^*l_t)$ (Eq. 28; $l_t$
  page-local inlet length scale), with $l_t=0.055$ axial chords against
  $0.003$ in the runs without the generator, chosen to give "a comparable
  inlet turbulent dissipation rate".
- **Fourier modes with a model spectrum, into a jet flame.**
  [Coulon et al. (2023)](/sources/coulon-2023.md), §2.2, Eqs. (2)–(3),
  inject synthetic isotropic turbulence into the central jet of a premixed
  slot burner through a characteristic (NSCBC) inlet: a sum of $N=200$
  random Fourier modes in the manner of Kraichnan, with random amplitudes,
  wavevectors and frequencies sampled to reproduce the Passot–Pouquet
  spectrum
  $$E(k)=16\frac{u'^2}{k_e}\sqrt{\frac2\pi}\Big(\frac{k}{k_e}\Big)^4\exp\Big[-2\Big(\frac{k}{k_e}\Big)^2\Big],$$
  with $u'$ the fluctuation intensity and $k_e$ the most energetic
  wavenumber (page-local; the integral length is $\sqrt{2\pi}/k_e$). The
  intensity is a tenth of the bulk velocity (2.5 m/s against 25 m/s) and
  the integral length a quarter of the jet width (2.1 mm), identical for
  the three fuels of the comparison, which places all three flames at
  one point of the combustion regime diagram.
  [Kumar et al. (2023)](/sources/kumar-2023.md), §3.2, impose turbulence
  in the initial field and feed it continuously at the hard inlet of a
  lean methane slot-burner DNS, "by specifying a turbulent length scale and
  RMS velocity fluctuations and by prescribing a turbulent energy
  spectrum", without printing the generator. They state that the shear
  turbulence of the jet has no time to develop because the flame adds
  viscous dissipation, so the flames are controlled by the injected
  turbulence; the supporting spectral analysis is in supplementary
  material not in the file read. See
  [direct numerical simulation](/definitions/direct-numerical-simulation.md).
- **Steady Fourier modes through a radiation boundary condition.**
  [Gao et al. (2025)](/sources/gao-2025.md), §III.B, Eqs. (21)–(22),
  Table IV, App., feed a slip-wall WMLES in a high-order aeroacoustic
  finite-difference solver with a "simplified Fourier mode synthesis":
  the three outer-layer modes of Sandham et al. (as cited) with their time
  dependence $\sin(\omega_jt)$ removed, so that the fluctuations are
  steady and spanwise-periodic, and injected as source terms in the Tam &
  Dong radiation condition at the inlet, the time invariance being chosen
  to minimize spurious noise. With page-local amplitudes $c_{1j}$, $c_{2j}$,
  peak heights $y_{p,j}$, spanwise wavenumbers $\kappa_{z,j}$, phases
  $\varphi_{z,j}$ and Gaussian constants $a_{\mathrm G}$, $b_{\mathrm G}$
  ($j=1,2,3$),
  $$\begin{aligned}
  u'&=\sum_jc_{1j}\Big[\frac{y}{y_{p,j}}e^{-y/y_{p,j}}+a_{\mathrm G}y^2e^{-b_{\mathrm G}y^2}\Big]\cos(\kappa_{z,j}z+\varphi_{z,j}),\\
  v'&=\sum_jc_{2j}\Big[\frac{y}{y_{p,j}}e^{-y/y_{p,j}}+a_{\mathrm G}y^2e^{-b_{\mathrm G}y^2}\Big]\cos(\kappa_{z,j}z+\varphi_{z,j}),\\
  w'&=-\sum_jc_{2j}\Big[\Big(1-\frac{y}{y_{p,j}}\Big)\frac{e^{-(y/y_{p,j})^2}}{y_{p,j}}+2a_{\mathrm G}\big(y-b_{\mathrm G}y^3\big)e^{-b_{\mathrm G}y^2}\Big]\frac{\sin(\kappa_{z,j}z+\varphi_{z,j})}{\kappa_{z,j}},
  \end{aligned}$$
  with $c_{1j}=0.24U_0$, $c_{2j}=-0.1U_0$ ($U_0$ the free-stream velocity),
  $y_{p,2}=0.1\delta$ and $y_{p,j}$, $\kappa_{z,j}$ in the ratios 1.33,
  1, 0.67, $\kappa_{z,2}=2\pi/(7\Delta z\times1.33)$ from the smallest
  wavelength the dispersion-relation-preserving scheme resolves,
  $a_{\mathrm G}=3$, $b_{\mathrm G}=6$, phases 0, 0.1, 0.15 (Table IV). On a
  Mach 0.15 flat plate ($\delta_0=4$ mm, $Re_{\delta_0}=1.4\times10^4$,
  inlet mean profile $(y/\delta_0)^{1/6}$, $967\times76\times91$ points,
  sample point of the wall model at $y^+=44.1$) the flow becomes fully
  turbulent after $20\delta_0$, the wall-pressure spectra become
  self-similar by $20\delta$ to $30\delta$, and at $35\delta_0$
  ($Re_\theta=1924$, $Re_\tau=674$) the mean velocity and the stresses
  agree with Spalart's DNS for $y>0.2\delta$ (§III.B.2, Table VI,
  Figs. 13–17); the wall-pressure spectrum there is 8.6 dB above Goody's
  model and the rms wall pressure about 3.8 times a correlation the
  authors cite, which they attribute to fluctuations transmitted through
  the wall-model sample point and to the grid (Figs. 18–19; see
  [slip-wall models](/methods/slip-wall-model.md) and
  [turbulent boundary layers](/benchmarks/turbulent-boundary-layer.md)).
  They call the field rigorously divergence-free; with the printed forms,
  $\partial_yv'+\partial_zw'$ cancels in the Gaussian terms but not in the
  first terms, which carry $e^{-y/y_{p,j}}$ in $v'$ and
  $e^{-(y/y_{p,j})^2}$ in $w'$ *(compiler check, not in the sources)*.
  Their survey (§I.C) lists recycling, Fourier, digital-filter, synthetic
  eddy, volume-forcing and divergence-free synthetic-eddy methods, and
  states that the low-noise generator of Shur et al. still needs a
  first-cell $y^+\approx1$.
- **Digital-filter perturbations as an initial field.**
  [Wang et al. (2022)](/sources/wang-2022-j.md), §V, perturb the initial
  tanh profile of a weakly compressible
  [temporal mixing layer](/benchmarks/temporal-mixing-layer.md) ($M=0.2$,
  $Re=2000$) with a digital-filter field of width $\Delta_d$ (page-local)
  of 8 to 64 DNS spacings, and find that every LES (filter width eight DNS
  spacings) agrees better with the filtered DNS when $\Delta_d$ is 16 rather
  than 8 spacings: the initial perturbation scales must exceed the LES
  filter width, so that filtering the initial condition does not remove
  them (Figs. 8–13, Conclusions).
- **Fourier modes from a RANS solution, as an initial field.**
  [Bouhafid et al. (2024)](/sources/bouhafid-2024.md), §2.1, initialize a
  temporal LES of an aircraft wake (a periodic box built by extruding a
  cross-flow slice of a RANS solution) with the modified discretizing and
  synthesizing random flow generation (MDSRFG) of Castro & Paz, a sum of
  random Fourier modes, divergence-free and correlated in space and time,
  that reproduces prescribed one-dimensional spectra. The series is
  normalized and then transformed, cell by cell, with the eigenvectors of
  the local RANS Reynolds-stress tensor (the random-flow-generation
  transformation of Smirnov et al.) so that its stresses match the RANS
  ones; the energy follows a Pao spectrum between the jet radius and the
  smallest cell, and fluctuations are added only in the engine jets. The
  rescaled field is no longer divergence-free, which the authors accept
  because it is an initial and not an inflow condition. On a test of Huang
  et al. (von Kármán spectrum) the generated spectrum agrees very well with
  the target before scaling, and the scaling changes the levels but not the
  shape (Fig. 2). Atmospheric turbulence is generated by the same method
  without scaling, on $k^{-5/3}$ spectra with an anisotropy factor between
  horizontal and vertical components (§4.1.1).
- **Random cosine modes as an isotropic initial field.**
  [De Cosmo et al. (2025)](/sources/decosmo-2025.md), §3.2, Eq. (15),
  initialize decaying [isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
  matching the Comte-Bellot–Corrsin experiment with the generator of
  Saad et al. that they cite: $\boldsymbol u=2\sum_mq_m\cos(k_m\hat{\boldsymbol k}_m\cdot\boldsymbol x+\psi_m)\hat{\boldsymbol\sigma}_m$
  over 5000 modes, with amplitudes $q_m$ from the target spectrum at the
  bin wavenumbers $k_m$, random unit wavevectors $\hat{\boldsymbol k}_m$,
  directions $\hat{\boldsymbol\sigma}_m$ normal to them and random phases
  $\psi_m$ (all page-local); the authors state that the field is
  divergence-free, and it is evaluated at cell centres, with uniform temperature and pressure chosen
  for the target Reynolds number (an initial condition, not an inflow).
- **Synthetic eddies plus forcing.** [Gao et al. (2022)](/sources/gao-2022.md),
  §1, §5.2, feed the Mach 2 boundary layer of a DG
  [implicit LES](/definitions/implicit-les.md) of an oblique
  [shock/boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
  in [FLEXI](/software/flexi.md) with the synthetic eddy method (SEM) of
  Jarrin et al. in the reformulation of Roidl, Meinke & Schröder that they
  cite: randomly placed coherent structures with prescribed time and length
  scales and shapes, with three wall-normal virtual boxes for the different
  eddy sizes, and compressibility taken into account "by enforcing the
  strong Reynolds analogy" (see [Morkovin's
  hypothesis](/definitions/morkovin-hypothesis.md)). The SEM acts on the
  lower part of the inflow plane, and anisotropic linear forcing (de Laage
  de Meux et al.) in a zone from $5\delta_r$ to $10\delta_r$ ($\delta_r$
  the boundary-layer thickness at the reference station, registry §11)
  shortens the recovery further at a cost of 5–10% in performance. No
  formula of either is printed. The authors choose the SEM because random
  superposition creates no spurious inflow correlations; they state,
  citing Morgan et al., that the recycling–rescaling of Lund et al.
  introduces extra frequencies that contaminate the separation-induced
  unsteadiness, and, citing Pamiès et al. and Roidl et al., that SEMs
  recover faster than digital filters.
  [Gao et al. (2023)](/sources/gao-2023.md), §5.1, use the same
  combination for the same Mach 2 interaction over an elastic panel, the
  forcing zone at $7\delta_r$–$11\delta_r$ streamwise and
  $0.1\delta_r$–$1.2\delta_r$ wall-normal, and find the van Driest II
  skin friction and the shape factor close to DNS and to the correlation
  quickly after the forcing zone (Fig. 19).
- **Synthetic eddies from a RANS precursor, with the strong Reynolds
  analogy.** [Wei et al. (2023)](/sources/wei-2023.md), §II D, Eqs.
  (21)–(24), print their implementation of the synthetic eddy method of
  Jarrin et al. (cited) for a wall-resolved LES of supersonic hydrogen film
  cooling (Mach 2.44 main stream, inlet boundary layer of 10 mm). $N$ eddies
  at positions $\boldsymbol x^k$ carry intensities
  $c^k_i=a_{ij}\xi^k_j$, with $\xi^k_j$ standard normal random numbers and
  $a_{ij}$ the Cholesky factor of the Reynolds stress $R_{ij}$ of a
  [$k$-$\omega$ SST](/methods/k-omega-sst-model.md) precursor (after Lund
  et al.), and
  $$\boldsymbol u=\langle\boldsymbol u\rangle+\frac{1}{\sqrt N}\sum_{k=1}^N\boldsymbol c^k\,f_\sigma(\boldsymbol x-\boldsymbol x^k),$$
  with $\langle\boldsymbol u\rangle$ the precursor mean and $f_\sigma$ the
  eddy shape function of Jarrin's thesis ($N$, $\boldsymbol x^k$,
  $\boldsymbol c^k$, $\xi^k_j$, $a_{ij}$, $f_\sigma$ page-local; $N$ is not
  the polynomial degree here). Temperature fluctuations follow the strong
  Reynolds analogy, $T'/\langle T\rangle=-(\gamma-1)M^2u'/\langle u\rangle$
  (see [Morkovin's hypothesis](/definitions/morkovin-hypothesis.md)), and
  density fluctuations are tied to them (printed form under
  Qualifications). The hydrogen film inlet is laminar, with a 1/7
  power-law profile. The authors state that the method was devised for
  transition problems at RANS–LES interfaces and recovers physical
  structures quickly; its recovery is in the next section.
- **Synthetic eddies as a volume source in a high-order code.**
  [Witherden et al. (2025)](/sources/witherden-2025.md), §3.8, describe
  the turbulence-generation plugin of [PyFR](/software/pyfr.md) v2.0.3: the
  synthetic eddy method of the works they cite, injected through a source
  term with specified intensity and length scale; the eddy characteristics are generated from a single 32-bit seed by a
  device-side permuted congruential generator, and the eddy intersections
  of each element are pre-computed, so that the cost scales with the number
  of eddies crossing an element rather than with the total injected. No
  verification of the generated statistics is printed in the paper.
- **Learned generators.** The review of
  [Fang et al. (2026)](/sources/fang-2026.md)
  cites a machine-learning inflow generator built on an MLP and an
  autoencoder (Fukami et al.) and a transformer-based generator for
  spatially developing boundary layers trained on DNS over
  $Re_\theta=661.5$–$1502.0$, reported with "less than 5% error" in
  turbulence intensity and energy spectrum (Yousif et al.) (§3.3.1, §3.4,
  Table 3); no recovery length is quoted.
- **Forcing.** [Krais et al. (2021)](/sources/krais-2021.md), §7.3,
  generate inflow turbulence by anisotropic linear forcing (de Laage de Meux
  et al.), combined with recycling–rescaling, for a zonal LES with low
  spurious noise.

**What synthetic turbulence does after injection.**
[Morsbach et al. (2024)](/sources/morsbach-2024.md), §3.3, Figs. 4–5,
find the injected turbulence two-component at the inlet, returning toward
isotropy downstream; the integral length scale, measured by frozen
turbulence, drops quickly to about half the specified value, as in their
earlier tests of the generator on decaying isotropic turbulence; the spectra
show an $f^{-5/3}$ range. Matching the measured decay of free-stream
turbulence would need a length scale of the order of the cascade pitch, so
they reduce it and rescale the stresses to match the turbulence intensity at
the blade leading edge, accepting a steeper decay.

**Synthetic inflow in a hybrid RANS/LES.** [Möller et al. (2024)](/sources/moller-2024.md)
show that in [detached-eddy simulation](/methods/detached-eddy-simulation.md)
of the transitional V103 [compressor cascade](/benchmarks/compressor-cascade.md)
the inflow decides which mode carries the free-stream turbulence (§III.B,
Figs. 11–22):

- **Without the generator**, the modelled free-stream turbulence intensity
  drops unphysically ahead of the leading edge, unlike DNS, LES and RANS:
  the shielding function is 1 in the free stream and, with a small subgrid
  length scale, "spuriously" switches on LES-mode destruction there
  (§III.B.1, Figs. 11–12). Pressure-side bypass transition is then carried
  by modelled turbulence and follows RANS with a transition model.
- **With the generator**, the total free-stream intensity agrees with DNS
  (slight over-prediction of modelled plus resolved energy), the
  suction-side separation bubble closes slightly earlier, closer to DNS, and
  bypass transition is carried by resolved scales, slightly delayed against
  LES; the skin friction on the pressure side barely changes, because the
  shielding function enforces RANS mode near the wall (§III.B.2,
  Figs. 13–18).
- **Numerical dissipation interacts.** The dynamic central/upwind flux
  blending of Travin et al. damps the injected scales; a constant upwind
  fraction of 25% still damps them and over-predicts the bubble, 0%
  oscillates and suppresses it, 5% agrees best with DNS (§III.B.3,
  Fig. 19). Varying the blending without the generator changes little,
  which the authors take as evidence of "the interdependence between
  resolved inflow scales and numerical dissipation" (p. 25). They also
  question whether shielding is needed at all once resolved inflow
  turbulence is supplied (§III.B.2). The transitional DDES itself is on
  [local-correlation-based transition models](/methods/local-correlation-based-transition-model.md).

[Bouhafid et al. (2024)](/sources/bouhafid-2024.md) show what the
synthetic field is for, on two wake cases. On a NACA 0012 wing with an
engine jet, the temporal LES without synthetic fluctuations does not roll
the jet up around the vortex; with them it agrees qualitatively with the
wind-tunnel experiment and much better in temperature, and resembles a
zonal detached-eddy simulation on 89 million cells at far lower cost (no
timings given) (§3.2, Figs. 4–6). On the NASA Common Research Model with
engines, the wake turbulence carried over from the RANS triggers a
short-wave instability of the horizontal-tail vortices consistent with the
optimal-perturbation analysis of Fabre et al. (§4.3.1). The alternative
"analytic" initialization, a Lamb–Oseen vortex pair with uniform jets and
uncorrelated Gaussian noise in each cell, gives a similar descent and
lifespan of the primary vortices but no short-wave instability, because
spatially uncorrelated noise does not excite short-wave modes, a much less
turbulent secondary wake, and a plume about three times more diluted at the
end of the dissipation phase (§4.3.3, Figs. 18, 21–23). See
[mesh adaptation](/methods/mesh-adaptation.md) for the RANS precursor and
[Reynolds-stress model](/methods/reynolds-stress-model.md) for the stresses
it supplies.

## Recovery length

[Huang et al. (2022)](/sources/huang-2022.md), §3.1, Table 3, define the
induction length $\Delta x_{\mathrm{ind}}$ as the distance from the inlet to
where the momentum-integral relation $C_f=2\,d\theta/dx$ first holds to
5%, after Wenzel et al. For recycling inflow it grows with Mach number,
from $20\delta_i$ at Mach 2.5 (adiabatic wall) to $80\delta_i$ at Mach 14
($\delta_i$ the inflow thickness); in units of the eddy-turnover length
$U_\infty\delta_i/u_{\tau,i}$ it is 1 to 3, and the effective turnover
length of Sillero et al. collapses the cases to 1–2. The digital filter
needs $15$ to $20\delta_i$ more (40 against 20 at Mach 2.5, 85 against 70 at
Mach 10.9). At the end of the digital-filter induction region the two
inflows still differ by 6.2% in the van Driest velocity of the wake region
and 1.8% in the streamwise stress, falling to 1.5% and 1.0% at
$Re_\tau=774$, while near the wall they agree almost at once: the outer
layer recovers more slowly than the near-wall region (Fig. 2).

[Morsbach et al. (2024)](/sources/morsbach-2024.md), §3.3, Fig. 3, handle
the adaptation by a precursor: a finite-length channel LES with parallel end
walls (83,790 elements, $N=5$) reproduces the clean-tunnel inflow and fixes
the inlet distance at which the end-wall boundary layer meets the measured
momentum-thickness growth, and the RANS inflows of the comparison are tuned
to reproduce the LES decay of free-stream turbulence. They specify the
inflow by total pressure, as is turbomachinery practice, which makes the
near-wall velocity a result of the simulated static pressure and requires a
chosen centre-line Mach number (0.362) that may need iteration.


[Gao et al. (2022)](/sources/gao-2022.md), §5.2–5.3, Figs. 16–17 and 24,
judge recovery by validation instead of a criterion: at $11\delta_r$, one
reference thickness after the forcing zone, the van Driest transformed
mean velocity and the density-scaled Reynolds stresses match the DNS of
Wenzel et al. that they cite, the van Driest II transformed skin friction
"quickly approaches" that DNS and the incompressible correlation
$0.024Re_\theta^{-0.25}$ (in transformed variables) after the forcing
zone, and the wall-pressure spectra of the interaction show no extra
low-frequency content from the SEM, with the interaction peak at
$St\approx0.03$ based on the interaction length.

Three sources state adaptation distances for the digital filter
and the library. [Kokkinakis et al. (2023)](/sources/kokkinakis-2023.md),
§III B, state, citing earlier work, that the digital filter needs about
$5\delta_0$ for the velocity autocorrelation to approach zero, and place
the shock generator about $21.1\delta_0$ from the inlet. In
[Shi & Yan (2023)](/sources/shi-2023.md), §IV.B, the inlet at
$x/\delta=-18.4$ generates weak compression waves from the mismatch with a
true turbulent state, and the layer becomes a true turbulent boundary
layer at around $x/\delta=-8$ (the source's $x^*$), about $10\delta$
downstream of the inlet
*(compiler check, not in the sources)*. Mo et al. (2023) define
$L_r$ by the $C_f$ peak and find 10 to 24 inflow thicknesses, governed by
the Reynolds-number mismatch of the library (section above).

[Tonicello et al. (2022)](/sources/tonicello-2022.md), §2.1, place the
digital-filter inlet $12\delta$ upstream of the reference station
($\delta$ the reference 99% thickness), citing recovery distances in the
literature from about $\tfrac23\delta$ (Adler et al.) to $15\delta$ (Morgan
et al.). At the reference station the computed layer has $Re_\theta=2873$,
$\delta^+=355$ and $C_f\times10^3=2.17$ against the target 2900, 340 and
2.16, with the van Driest velocity and Reynolds stresses compared with DNS
(Table 3, Fig. 5). [Yu et al. (2022)](/sources/yu-2022-e.md) validate
their incoming layer on a reference plane $15\delta_i$ from the inlet
($\delta_i$ the inflow thickness) against the Mach 2 DNS of Pirozzoli &
Bernardini at $Re_\tau\approx200$ (§2, Fig. 2), and
[De Vanna et al. (2022)](/sources/devanna-2022.md) theirs at
$Re_\tau=840$ against the same DNS (§4.3, Figs. 3–4); neither states a
recovery length.

[Wei et al. (2023)](/sources/wei-2023.md), §III B, Fig. 9, measure the
recovery of their synthetic-eddy inflow on a separate 100 mm inlet section
($1.52\times10^6$ cells, the grid and conditions of the inert film-cooling
case): physical turbulence statistics need a development region of about
50 mm, and the skin friction reaches the van Driest II value at
$x/\delta_{\mathrm t}=7$ ($\delta_{\mathrm t}$ the inlet thickness,
page-local), with a trend similar to the recycling–rescaling LES of Liu et
al. that they cite; the van Driest velocity at $x/\delta_{\mathrm t}=7$
and 14 and the Reynolds stresses at 7 are compared with supersonic
boundary-layer experiments. They attribute part of a difference between
two of their combustion cases to the different turbulence states that the
two RANS precursors supply (§IV D).

## Triggering transition instead

[Dang et al. (2022)](/sources/dang-2022.md), §5.1, generate the Mach 2.9
boundary layer upstream of a compression ramp by blowing and suction on the
wall between 350 and 200 mm upstream of the corner, instead of the
recycling of the reference DNS of Martín et al., and validate the van
Driest-transformed mean velocity against it.
[Zhang et al. (2022c)](/sources/zhang-2022-g.md), §II B, trip the Mach 6
boundary layer of a DNS of a swept compression ramp in the same code
family ([OpenCFD-SCU](/software/opencfd-scu.md)) from a laminar inlet
profile about 3.9 mm thick by a wall disturbance between 370 and 350 mm
upstream of the corner, stimulating bypass transition; they check the
incoming layer against the van Driest law (log-law intercept 5.7, higher than
incompressible, which they attribute to the wall temperature) and against compressibility-scaled
fluctuations of published boundary layers (§II C, Fig. 6). The forcing
leaves narrow-band peaks in the wall-pressure spectra of the interaction,
which they state do not affect their low-frequency analysis (§III C).
[Tang et al. (2024)](/sources/tang-2024.md), §2.2–2.3, Eqs. (2.2)–(2.3),
print the blowing and suction of Pirozzoli et al. (2004), which they cite,
for a Mach 5 DNS of a 30° compression ramp over a cold wall in the same
code family: a wall-normal velocity $A_{\mathrm{bs}}U_\infty$ ($A_{\mathrm{bs}}=0.2$,
page-local) between $x=-440$ and $-410$ mm (corner at $x=0$), shaped by a
streamwise sine bump of zero mean mass flux, a sum of three spanwise sine
modes and five temporal harmonics with weights $0.8^{n-1}$ and random
phases, at a fundamental frequency $0.32U_\infty/\delta_{\mathrm d}$
($\delta_{\mathrm d}$ the laminar thickness at the disturbance) or
$1.24U_\infty/\delta$; the laminar inlet profile and the initial field come
from a two-dimensional auxiliary laminar run. Transition is complete near
$x=-250$ mm and the boundary layer fully developed from $x=-150$ mm, ahead
of the reference station at $x=-60$ mm ($\delta=10.6$ mm, $Re_\theta=4652$,
$Re_\tau=700$, Table 1).

**Inlet disturbances on a laminar profile.**
[Wang et al. (2024c)](/sources/wang-2024-j.md), §II, trigger transition
in a wall-resolved LES of a Mach 2 flat-plate boundary layer
($Re_{\delta_0}\approx13{,}500$ on the inflow thickness $\delta_0$,
page-local) with the inlet disturbances of Sandham et al. extended to
supersonic flow by Li & Coleman, as cited (details not printed); they
divide the flow into transition ($x/\delta_0<10$), development
($10<x/\delta_0<20$) and a fully developed stage beyond $x/\delta_0=20$,
and take statistics at $x/\delta_0=25$ (§III C, Figs. 5–6). The
scale-adaptive comparison run on that flow is on
[scale-adaptive simulation](/methods/scale-adaptive-simulation.md).
[Kimmel et al. (2025)](/sources/kimmel-2025.md), §III.A, start the
boundary layer of an implicit LES of a Mach 4, $24^\circ$ compression ramp
from a 1 mm parabolic velocity profile with random velocity perturbations
between $-2\%$ and $+2\%$ of $U_\infty$, "allowing the natural formation
of a turbulent boundary layer downstream", which is 8 mm thick ahead of
the corner; no recycling or synthetic turbulence is used, and the
accuracy of the developed layer is delegated to the authors' conference
paper ([shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)).

**Forced laminar shear layers at a jet inflow.**
[Rahatgaonkar & Ghosh (2025)](/sources/rahatgaonkar-2025.md), §II C,
Eq. (10), start their LES of compressible round jets at
$Re=5\times10^5$ (on the diameter) with no nozzle in the domain, from a
hyperbolic-tangent velocity profile of momentum thickness
$\theta_0=0.05r_0$ ($r_0$ the inflow jet radius, page-local), excited by
the vortex-ring forcing of Bogey et al. that they cite, the added
fluctuation reaching at most 3.3% of the centreline velocity, with
characteristic inflow conditions. They attribute part of their
overprediction of the near-field noise of the $M_j=0.9$ jet, by at most
1.5 dB against the measurements of Bogey et al., to the inflow momentum
thickness, of order $10^{-2}r_0$ in the LES against $10^{-3}r_0$ in
experiments (§III A, Fig. 8). See
[turbulent round jet](/benchmarks/turbulent-round-jet.md).

**Counter-flow body-force tripping.** [Kang & Lee (2024)](/sources/kang-2024.md),
§II.B, Eq. (15), trip a laminar Blasius inflow of thickness
$\delta_{\mathrm{in}}=2.5$ mm with the body force of Mullenix et al. and
Poggie (cited) for a DNS of the Mach 2.9, 24° compression ramp. A force
$f_i$ (registry §1), with its work added to the energy equation, points
almost against the flow (at 179° to $x$) and has the magnitude
$$f=\frac{2D_{\mathrm c}}{\pi l_xl_yl_z}\sin^2\!\Big(\pi\frac{z-z_{\mathrm c}}{l_z}\Big)\exp\Big[-\Big(\frac{x-x_{\mathrm c}}{l_x}\Big)^2-\Big(\frac{y-y_{\mathrm c}}{l_y}\Big)^2\Big],$$
with $D_{\mathrm c}=0.055$, centre $2.5\delta_{\mathrm{in}}$ downstream of
the inlet at $y_{\mathrm c}=0.25\delta_{\mathrm{in}}$, widths
$(l_x,l_y,l_z)=(0.17,0.01,0.5)\delta_{\mathrm{in}}$ (all page-local). It
sheds hairpin-like vortices that break down into a "forest of hairpin
vortices" (Fig. 8). At the reference station the layer has $Re_\theta=2400$
and $C_f=0.00227$ against 2400 and 0.00225 in the experiment of Bookey et
al. (Table I); the van Driest velocity follows the viscous and
logarithmic laws (Fig. 4b), the density-scaled intensities agree with
incompressible and compressible DNS (Fig. 5), spanwise autocorrelations at $y^+=50$ and
$y/\delta=0.5$ vanish within half a thickness, and the spectra at $y^+=50$
follow $k^{-5/3}$ with "no spurious length scales" from the trip (§III,
Figs. 4–8). The interaction is on
[shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md).

**Geometric tripping inside a nozzle.** [Ahn et al. (2023)](/sources/ahn-2023.md),
§III and §IV A–B, Figs. 3–10, impose a laminar inflow (total pressure and
temperature, zero turbulence intensity) on twin square supersonic nozzles
($M_j=1.36$, $Re=8.85\times10^5$ on an equivalent diameter) and disturb the
nozzle boundary layer with a small step of height $0.02h_n$ ($h_n$ the exit
height, registry §11) mid-way along the converging section, following the
$0.01D$ step that Langenais et al., whom the authors cite, used in a round
jet. The step sits in the converging rather than the diverging part
to avoid a shock at the artificial geometry, and the larger height is
justified by the lower wall slope of their convergent. The implicit LES
(MILES with Jameson-type artificial dissipation, see
[implicit LES](/definitions/implicit-les.md)) has no wall model, with a
first cell of $h_n/320$ giving $y^+$ of 10 to 20 inside the nozzle, which
"is insufficient to resolve the viscous sub-layer but allows us to convect
forced velocity fluctuations". The vortical structures shed by the step
are convected along the convergent, stretched and weakened through the
throat and divergent section, and the exit turbulence intensity reaches
about 0.06, streamwise-dominated, against the 0.04 reported by Langenais
et al. Compared with the untripped run (145 against 150 million points),
tripping brings the length of the supersonic region, the centre-line
velocity decay and the turbulent kinetic energy of the initial shear
layers closer to PIV; both runs over-predict the shock-cell strength, and
the untripped one over-predicts the near-lip turbulent kinetic energy more.
The authors state that tripping "has not been done for coupled twin jets"
before (§I); the far-field noise of the tripped run is on the
[Ffowcs Williams–Hawkings analogy](/methods/ffowcs-williams-hawkings-acoustic-analogy.md).

## Choosing no inflow turbulence

Three turbomachinery and jet sources inject no inflow turbulence, two of
them with a stated reason.
[François et al. (2022)](/sources/francois-2022.md), §3.2.1, compute the
region upstream of the [ACAT1 fan](/benchmarks/acat1-fan-stage.md) in URANS
because the measured inflow turbulence is about 0.3% and fan noise from it
is negligible against rotor–stator interaction noise; the
[ACAT1](/benchmarks/acat1-fan-stage.md) LES of
[Lewis et al. (2023)](/sources/lewis-2023.md), §3.2.2, likewise injects no
turbulence at the inlet. [Moratilla-Vega et al. (2024)](/sources/moratillavega-2024.md),
§3, run a subsonic round-jet LES with laminar inflow and no wall model,
expecting the nozzle contraction to relaminarize the boundary layer and
stating that synthetic inflow turbulence without experimental
characterization "can generate spurious noise"; they then attribute a 3–4 dB
over-prediction of the far-field spectrum at $0.7<St<1.4$ "possibly" to the
laminar inlet (§4.3).

A hybrid RANS/LES avoids the problem by construction.
[Husson et al. (2024)](/sources/husson-2024.md), §1, contrast wall-modelled
LES, in which "by construction, the near-wall flow events responsible for
turbulence generation are no longer resolved, [so] turbulent inflow
conditions must be specified", and which in lattice Boltzmann solvers
"still raises open questions about how to generate turbulent
fluctuations", with hybrid RANS/LES, where the outer layer of attached
boundary layers is also modelled in RANS, "thus no fluctuations have to be
generated". Their zonal [detached-eddy simulation](/methods/detached-eddy-simulation.md)
in a [lattice Boltzmann](/methods/lattice-boltzmann-method.md) solver is
built to keep attached layers in RANS; see
[hybrid RANS/LES](/definitions/hybrid-rans-les.md).

The opposite case: [Morsbach et al. (2024)](/sources/morsbach-2024.md), §1,
cite earlier simulations of the same turbine cascade with laminar
end-wall boundary layers and no free-stream turbulence (Rasquin et al.;
Iyer et al.), which reached "no satisfactory agreement" with the experiment, and
attribute their own agreement to the turbulent inflow. They also show that
the RANS practice of shrinking the inflow length scale to fix a laminar
separation bubble gives the right loss for the wrong reason (§4.1, see
[local-correlation-based transition models](/methods/local-correlation-based-transition-model.md)).

A laminar inlet chosen for reproducibility.
[Wang & Xu (2024)](/sources/wang-2024-h.md), §2.3, App. B, run a DNS of a
reacting supersonic boundary layer (Mach 2.33 vitiated air over a sonic
hydrogen film, loosely after the Burrows–Kurkov combustor) from a laminar
wall-jet inlet: a Poiseuille hydrogen stream of height $h_0=4$ mm under a
compressible Blasius main stream, separated by an "infinitely thin"
no-slip interface. They state that in the Burrows–Kurkov set-up the inlet
turbulent state is unknown and that key results such as the flame
anchoring position "are reported to be highly sensitive to the thickness
of the inlet turbulent boundary layer" (citing Edwards et al., Liu et al.
and [Wei et al. 2023](/sources/wei-2023.md), above), so that the various
inflow generators used can lead to different results; a laminar inlet
avoids this, "enhance[s] the reproducibility", and needs no precursor.
They compensate the slower mixing by a thinner main-stream layer and a
higher main-stream temperature (1700 K). Transition comes in two stages: a
mixing-layer instability for $0<x/h_0<7.6$, which leaves $C_f$ unchanged,
then a boundary-layer instability that raises it (§4.1, Figs. 6–7); the
statistics stations at $x/h_0=100$–150 have $Re_\tau\approx1050$ in the
reacting case (Table 2) and are
compared with the canonical adiabatic Mach 2 layer at $Re_\tau=1000$ (see
[turbulent boundary layers](/benchmarks/turbulent-boundary-layer.md)).

## Inflow turbulence as a physical parameter, and at RANS–LES interfaces

In turbomachinery the inflow turbulence is not only a boundary condition
to be matched but a parameter the blade responds to. The review of
[Sandberg & Michelassi (2022)](/sources/sandberg-2022.md), §3.2.1 and
§3.3.3.2, cites highly resolved LES of a high-pressure-turbine nozzle
fed synthetically generated inflow turbulence at intensities of 6%–20% of
the inlet velocity and length scales of 5%–20% of the chord (Pichler et
al. 2017b), in which the boundary layer was strongly sensitive to the
incoming turbulence through different transition routes and larger length
scales gave an earlier rise and a higher overall level of heat transfer on
suction and pressure sides (Fig. 4a); and DNS and LES of a vane with inflow
intensities of 6.5%–20% and integral lengths of 4.8%–20.1% of the axial
chord (Zhao & Sandberg 2020a), in which the competition of inflow intensity
and stabilizing pressure gradient decides the path to transition while the
integral length sets the scale of the leading-edge streaks (Fig. 5). The
review adds, from Verma et al. (2019), that the hot-streak migration
induced on a transonic vane by the large-scale fluctuations of a reacting,
swirling combustor is captured only by a fully coupled combustor–turbine
LES, not by a segregated one (§3.2.1). See
[turbine cascade](/benchmarks/turbine-cascade.md).

In zonal [hybrid RANS/LES](/definitions/hybrid-rans-les.md) the same
problem appears inside the domain, at the RANS-to-LES interface. The
review of [Heinz (2020)](/sources/heinz-2020.md), §1, states that
"empirical approaches for adding fluctuations in RANS-LES transition
regions have been suggested, but such methods introduce other
inconsistencies", the argument it uses for consistent single-equation
hybrids such as
[continuous eddy simulation](/methods/continuous-eddy-simulation.md); on
the [NASA wall-mounted hump](/benchmarks/nasa-wall-mounted-hump.md) it
cites two zonal DES variants that differ in the synthetic-turbulence
generator at the interface, next to a non-zonal one, among the results it
compiles (§5.2).

## Qualifications

- The sources measure recovery differently (momentum-integral balance in
  Huang et al.; match of a measured momentum-thickness growth and of the
  free-stream decay in Morsbach et al.; integral parameters at one station
  in Tonicello et al.); Mukha et al. give no length for their "inflow
  adaptation".
- Zhang et al. prefer recycling as "less noisy" than the digital filter;
  Huang et al. measure a longer induction length (distance to equilibrium)
  for the digital filter. Zhang et al. print no induction length, and Huang
  et al. no noise measure.
- [Möller et al. (2024)](/sources/moller-2024.md) find the 5% upwind
  fraction best but call it a tunable parameter likely to depend on case and
  mesh; their inflow length scales with and without the generator differ
  because the two inlet conditions define $\omega$ differently (§III.A).
- [Morsbach et al. (2024)](/sources/morsbach-2024.md) write $z$ for the
  end-wall normal and keep the momentum-thickness data confidential (fit
  only).
- [Bouhafid et al. (2024)](/sources/bouhafid-2024.md) use the generator
  for an initial field, not an inflow, and do not define the normalizing
  wavenumber $k_0$ of their mode phases (Eq. 2.1). Their abstract states
  that "atmospheric turbulence intensity and stratification both accelerate
  the vortex decay", while §4.3.1 finds that atmospheric turbulence
  intensity "does not seem to significantly impact the vortex pair
  lifespan".
- Zhang et al. (2022c) describe their trip as a "multi-frequency sine wave
  disturbance" (§II B) and later as an "upstream blowing and suction
  disturbance" (§III C); its amplitude and frequencies are not printed.
- Coulon et al. (2023) state that $u'$, the integral length and the
  turbulent Reynolds number are "the same" for the three flames (§3),
  while their Table 1 prints turbulent Reynolds numbers of 355, 313 and
  271.
- **Printed forms in Mo et al. (2023).** Differentiating their Eq. (11)
  with Eq. (12) gives
  $\partial\langle T\rangle/\partial\langle u\rangle=(T_r-T_w)\big[2(1-s_{\mathrm{RA}}Pr)\langle u\rangle/u_e^2+s_{\mathrm{RA}}Pr/u_e\big]+2(T_e-T_r)\langle u\rangle/u_e^2$;
  the printed Eq. (22) lacks the term $(T_r-T_w)s_{\mathrm{RA}}Pr/u_e$, and
  Eq. (23) and the ratio of Eq. (27) inherit it *(compiler check, not in
  the sources)*. The cover page of the file announces a published erratum
  that the file does not contain. Eq. (23) carries $+2$ where the
  denominator of Eq. (27) carries $-2$. The recovery of the same Mach 7.25
  run is printed as $24\delta_{\mathrm{in}}$ (§IV B) and $22.7\delta_{\mathrm{in}}$
  (§IV C); the library thickness as 2.08 mm (§III A, Table IV) and 2.06 mm
  (§III C); the precursor wall as isothermal at 322 K (§II B) and
  adiabatic (§III B). All three libraries come from one Mach 2.25
  precursor and are tested on one Mach 7.25 target, and the $C_f$-peak
  criterion differs from the criteria of Huang et al. (2022) and the
  other sources above.
- **Shi & Yan (2023)** print the flat-plate length as
  $L_{x,1}=117.76$ mm with "$L^*_{x,1}=52.3$"; $117.76/6.4=18.4$, the
  inlet position in reference thicknesses, while 52.3 is the value of the
  earlier set-up of Tong et al. they quote next ($335/6.4$) *(compiler
  check, not in the sources)*.
- **Printed forms in Wei et al. (2023).** The sum of their Eq. (21) runs
  over $i$ while the summand carries $k$. The $(2,2)$ entry of the
  Cholesky factor (Eq. 23) is printed $\sqrt{R_{xx}-a_{21}^2}$; with
  $aa^{\mathsf T}=R$ the entry must satisfy $a_{21}^2+a_{22}^2=R_{yy}$,
  and the $(3,3)$ entry of the same matrix uses the matching diagonal
  *(compiler check, not in the sources)*. Eq. (24) prints
  $\rho'/\langle\rho\rangle=+T'/\langle T\rangle$ (overbars in the
  source); linearizing their own equation of state (Eq. 8) at fixed
  composition and $p'=0$ gives $\rho'/\langle\rho\rangle=-T'/\langle T\rangle$
  *(compiler check, not in the sources)*; the condition $p'=0$ is not
  stated by the authors.
- The trip of Kang & Lee (2024), the blowing and suction of Tang et al.
  (2024) and the laminar wall jet of Wang & Xu (2024) report no recovery
  length in the sense of Huang et al. (2022); they validate the incoming
  layer at one or more stations instead.
- The benchmarks on which the sources of this page test their inflows
  are [turbulent boundary layers](/benchmarks/turbulent-boundary-layer.md)
  and [shock–turbulent boundary layer interactions](/benchmarks/shock-turbulent-boundary-layer-interaction.md).

# Citations

- [Huang et al. (2022)](/sources/huang-2022.md) — §2.3, Fig. 1; §3.1, Eq. (3.1), Table 3, Fig. 2; §6(i).
- [Cogo et al. (2022)](/sources/cogo-2022.md) — §2 (recycling–rescaling set-up).
- [Zhang et al. (2022)](/sources/zhang-2022-b.md) — §2 (recycling–rescaling preferred to digital filtering, Mach 0.5–8).
- [De Vanna et al. (2022)](/sources/devanna-2022.md) — §4.1 (low-storage digital filter, Musker initial field); §4.3, Figs. 3–4.
- [Yu et al. (2022)](/sources/yu-2022-e.md) — §2.1 (digital filter, Musker profile, generalized Reynolds analogy); §2, Fig. 2.
- [Tonicello et al. (2022)](/sources/tonicello-2022.md) — §2.1, Tables 1 and 3, Fig. 5 (generalized digital filter with strong-Reynolds-analogy thermodynamics, $12\delta$ development length).
- [Helm & Martín (2022)](/sources/helm-2022.md) — §II, Fig. 1; §III B.
- [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) — Methods p. 14 (preprint v1).
- [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) — §4.3.
- [Krais et al. (2021)](/sources/krais-2021.md) — §7.3.
- [Hoy & Bermejo-Moreno (2022)](/sources/hoy-2022.md) — §2–3.
- [Morsbach et al. (2024)](/sources/morsbach-2024.md) — §1; §2; §3.1–3.3, Eqs. (5)–(14), Figs. 3–5; §4.1.
- [Carlsson et al. (2023)](/sources/carlsson-2023.md) — §4.3 (channel initialization with the generator of Shur et al.).
- [Dang et al. (2022)](/sources/dang-2022.md) — §5.1.
- [François et al. (2022)](/sources/francois-2022.md) — §3.2.1.
- [Lewis et al. (2023)](/sources/lewis-2023.md) — §3.2.2.
- [Moratilla-Vega et al. (2024)](/sources/moratillavega-2024.md) — §3; §4.3.
- [Bouhafid et al. (2024)](/sources/bouhafid-2024.md) — §2.1, Eqs. (2.1)–(2.4), Figs. 1–2; §3.2, Figs. 4–6; §4.1.1; §4.3.1; §4.3.3, Figs. 18, 21–23.
- [Steinhausen et al. (2023)](/sources/steinhausen-2023.md) — §2.1.
- [Möller et al. (2024)](/sources/moller-2024.md) — §II.E; §III.A, Eq. (28); §III.B.1–III.B.3, Figs. 11–22 (Shur et al. generator fed from a RANS precursor in DDES of a compressor cascade).
- [Mukha et al. (2025)](/sources/mukha-2025.md) — §IV.A–B, Figs. 12–13 (stored DNS inflow planes reused cyclically).
- [Gao et al. (2022)](/sources/gao-2022.md) — §1; §5.2, Figs. 15–17; §5.3.2, Fig. 24 (reformulated synthetic eddy method with anisotropic linear forcing for a Mach 2 shock/boundary-layer interaction).
- [Ahn et al. (2023)](/sources/ahn-2023.md) — §I; §III, Fig. 3; §IV A–B, Figs. 4–10 (geometric step tripping of a laminar nozzle boundary layer in implicit LES of twin supersonic jets).
- [Husson et al. (2024)](/sources/husson-2024.md) — §1 (inflow turbulence as a burden of wall-modelled LES that hybrid RANS/LES avoids).
- [Sandberg & Michelassi (2022)](/sources/sandberg-2022.md) — §3.2.1, Fig. 4a (cited inflow-turbulence sensitivity of turbine heat transfer; coupled combustor–turbine LES); §3.3.3.2, Fig. 5 (inflow intensity and length scale in vane transition).
- [Heinz (2020)](/sources/heinz-2020.md) — §1 (fluctuations added at RANS–LES interfaces); §5.2 (zonal DES with synthetic-turbulence generators on the hump, cited).
- [Zhang et al. (2022e)](/sources/zhang-2022-i.md) — §II A–B, Eq. (13), Fig. 3 (concurrent precursor for a pressure-gradient-driven neutral boundary layer).
- [Idelsohn et al. (2024)](/sources/idelsohn-2024.md) — §2.10.5 (digital-filter inflow of a backward-facing step).
- [Coulon et al. (2023)](/sources/coulon-2023.md) — §2.2, Eqs. (2)–(3), Table 1 (Kraichnan-type Fourier modes with a Passot–Pouquet spectrum through an NSCBC inlet); §3.
- [Wang et al. (2022)](/sources/wang-2022-j.md) — §V, Figs. 8–13 (digital-filter initial perturbations of a temporal mixing layer, perturbation scale against LES filter width); Conclusions.
- [Mo et al. (2023)](/sources/mo-2023.md) — §I (four classes of inflow methods); §II A–B (ACANS, Mach 2.25 precursor); §III A–C, Eqs. (14)–(19), Tables I–II, IV, Figs. 5–8 (library, velocity and strong-Reynolds-analogy scalings, Mach 2.9 test); §IV A, Eqs. (20)–(25) (new temperature and density laws); §IV B–C, Eqs. (26)–(28), Figs. 10–23 (Mach 7.25 tests, friction-Reynolds-number matching); §V.
- [Maeyama & Kawai (2023)](/sources/maeyama-2023.md) — §3, Fig. 3 (rescaling–reintroduction at $35\delta_0$).
- [Shi & Yan (2023)](/sources/shi-2023.md) — §II.C, Eqs. (19)–(26) (digital-filter coefficients, temporal correlation); §IV.A–B (inlet position and adaptation).
- [Kokkinakis et al. (2023)](/sources/kokkinakis-2023.md) — §III B (two-dimensional digital filter, inlet thickness, $5\delta_0$ adaptation).
- [Gao et al. (2023)](/sources/gao-2023.md) — §5.1–5.2, Fig. 19 (synthetic eddies with anisotropic linear forcing over an elastic panel).
- [Yu et al. (2023)](/sources/yu-2023.md) — §2 (reuse of the digital-filter DNS of Yu et al. 2022).
- [Iwata et al. (2023)](/sources/iwata-2023.md) — §II C, Eq. (1), Table I (precursor decaying isotropic turbulence through the inlet of a detonation-fixed frame).
- [Kumar et al. (2023)](/sources/kumar-2023.md) — §3.2 (prescribed inlet turbulence of a slot-burner DNS).
- [Zhang et al. (2023)](/sources/zhang-2023-c.md) — §2 (precursor pipe and annular-pipe inflows).
- [Zhang et al. (2022c)](/sources/zhang-2022-g.md) — §II B–C, Fig. 6 (laminar inlet and wall disturbance at Mach 6, incoming-layer check); §III C (spectral peaks of the trip).
- [Zhou & Bae (2024)](/sources/zhou-2024-b.md) — §2.3, Fig. 3 (Lund recycling precursor for the Gaussian bump); App. A, Fig. A.21 (inflow insensitivity).
- [Kim & Leonard (2024)](/sources/kim-2024-b.md) — §3.5 (multiscale streamwise-periodic boundary layer); §4.2 (inlet forcing of spatial mixing layers, advective outflow); §4.6 (Lund recycling in common use).
- [Yu et al. (2023b)](/sources/yu-2023-b.md) — §II (digital filter with Musker mean and generalized Reynolds analogy, no thermodynamic fluctuations, Mach 5).
- [Wei et al. (2023)](/sources/wei-2023.md) — §II D, Eqs. (21)–(24) (synthetic eddy method with RANS Cholesky factor and strong Reynolds analogy); §III B, Fig. 9 (recovery); §IV D (precursor dependence).
- [Tang et al. (2024)](/sources/tang-2024.md) — §2.2–2.3, Eqs. (2.2)–(2.3), Table 1 (blowing and suction, transition and development stations).
- [Kang & Lee (2024)](/sources/kang-2024.md) — §II.B, Eq. (15) (counter-flow body-force trip); §III, Figs. 5–8, Table I (incoming-layer validation).
- [Wang & Xu (2024)](/sources/wang-2024-h.md) — §2.3, App. B (laminar wall-jet inlet and its rationale); §4.1, Figs. 6–7 (two-stage transition).
- [De Cosmo et al. (2025)](/sources/decosmo-2025.md) — §3.2, Eq. (15) (random cosine modes for an isotropic initial field); §3.4 (periodic precursor channel coupled one-to-one to a bump channel).
- [Witherden et al. (2025)](/sources/witherden-2025.md) — §3.8 (synthetic-eddy source-term plugin of PyFR, seeding and cost).
- [Fang et al. (2026)](/sources/fang-2026.md) — §3.3.1, §3.4, Table 3 (machine-learning inflow generators, cited).
- [Wang et al. (2024c)](/sources/wang-2024-j.md) — §II (Sandham / Li–Coleman inlet disturbances); §III C, Figs. 5–6 (transition, development and developed stages).
- [Kimmel et al. (2025)](/sources/kimmel-2025.md) — §III.A (laminar parabolic inflow with ±2% random perturbations).
- [Gao et al. (2025)](/sources/gao-2025.md) — §I.C (survey of generators); §III.B, Eqs. (21)–(23), Table IV, App., Eq. (A1) (steady Fourier modes in a radiation boundary condition); §III.B.2, Tables V–VI, Figs. 13–19 (flat-plate development and wall pressure).
- [Rahatgaonkar & Ghosh (2025)](/sources/rahatgaonkar-2025.md) — §II C, Eq. (10) (tanh jet inflow with vortex-ring forcing); §III A, Fig. 8 (inflow momentum thickness and near-field noise).
