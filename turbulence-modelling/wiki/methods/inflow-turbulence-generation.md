---
type: Method
title: "Inflow turbulence generation"
description: "How a scale-resolving simulation is fed with turbulence at its inflow or in its initial field: recycling–rescaling and precursor planes, digital-filter and Fourier-mode synthetic turbulence built from prescribed statistics (also from a RANS solution), forcing, wall blowing and suction, or laminar inflow by choice, with the recovery each needs and the errors each leaves."
status: established
aliases: [turbulent inflow generation, synthetic inflow turbulence, synthetic turbulence generator, STG, recycling–rescaling inflow, recycling inflow, digital filter inflow, precursor inflow, MDSRFG, random flow generation]
tags: [les, dns, boundary-layer, wmles, compressible]
timestamp: 2026-10-26T15:53:00Z
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
transition inside the domain (**blowing and suction**). Every method leaves
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
  Duan et al. with the recycling plane at $52.7\delta_i$.
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

## Synthetic turbulence

A stochastic field with prescribed one-point statistics and length scales is
superimposed on the mean inflow.

- **Digital filters.** [Hoy & Bermejo-Moreno (2022)](/sources/hoy-2022.md),
  §2–3, use the digital filter of Klein, Sadiki & Janicka with the extensions
  of Xie & Castro and of Touber & Sandham for the boundary layer of a
  wall-modelled shock interaction; [Huang et al. (2022)](/sources/huang-2022.md)
  use a digital filter (Dhamankar et al.; Huang & Duan) as the alternative
  to recycling in their recovery study below.
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

## Qualifications

- The sources measure recovery differently (momentum-integral balance in
  Huang et al.; match of a measured momentum-thickness growth and of the
  free-stream decay in Morsbach et al.), so their recovery lengths are not comparable;
  Mukha et al. give no length for their "inflow adaptation".
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
- Inflow generation is a boundary condition, not a closure, but it sets
  the state that the closure is tested on; the benchmarks where it matters
  are [turbulent boundary layers](/benchmarks/turbulent-boundary-layer.md)
  and [shock–turbulent boundary layer interactions](/benchmarks/shock-turbulent-boundary-layer-interaction.md).

# Citations

- [Huang et al. (2022)](/sources/huang-2022.md) — §2.3, Fig. 1; §3.1, Eq. (3.1), Table 3, Fig. 2; §6(i).
- [Cogo et al. (2022)](/sources/cogo-2022.md) — §2 (recycling–rescaling set-up).
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
