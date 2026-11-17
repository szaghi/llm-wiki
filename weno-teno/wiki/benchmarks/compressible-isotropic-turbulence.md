---
type: Benchmark
title: "Compressible isotropic turbulence"
description: "Triply periodic turbulence box. Decaying runs (turbulent Mach number 0.07–1.0, uniform and AMR grids) measure numerical dissipation and robustness on under-resolved turbulence with eddy shocklets through kinetic-energy, Mach-number, density-fluctuation, enstrophy and dilatation histories; driven hydrodynamic and MHD variants compare inertial ranges across orders and demonstrate GPU-scale runs."
status: established
aliases: [decaying compressible isotropic turbulence, decaying isotropic turbulence, compressible homogeneous isotropic turbulence, compressible HIT, decaying HIT, forced compressible turbulence, driven subsonic turbulence]
tags: [benchmark, turbulence, low-dissipation, teno]
timestamp: 2026-11-17T08:43:44Z
---

# Compressible isotropic turbulence

In its decaying form the flow fills a triply periodic cube $[0,2\pi]^3$. At $t=0$ the
velocity is a random solenoidal field with a prescribed energy spectrum
peaked at a wavenumber $k_0$, density and temperature are uniform (or
consistent with a prescribed pressure field), and the turbulence decays
without forcing. It is set by the initial turbulent Mach number
$M_{t,0}$ ($\sqrt3\,u_{\mathrm{rms},0}/c$ in Hong, Ye & Ye's definition) and Taylor-scale Reynolds number
$\mathrm{Re}_{\lambda,0}$ ($u_{\mathrm{rms}}$ the rms velocity component,
page-local). At $M_{t,0}\gtrsim0.5$ the field develops eddy shocklets,
so a scheme must capture them without damping the small scales. The
quantities compared with a DNS or spectral reference are the decay of
kinetic energy and of $M_t$, the rms density fluctuation
$\rho_{\mathrm{rms}}$, enstrophy, dilatation variance and the energy
spectrum, against a time normalized by an eddy-turnover time $\tau$
(defined per source). A forced form, driven from rest in a unit box and
compared by its inertial range, is recorded below under *Forced subsonic
turbulence*.

## Data

| Source | Initial spectrum | Cases | Grid and reference |
|---|---|---|---|
| [Hong, Ye & Ye (2022)](/sources/hong-2022.md) §5.8 | as in their ref. [33] | $M_{t,0}=0.5$, $\mathrm{Re}_{\lambda,0}=72$ | $128^3$; tenth-order compact finite differences on the same grid |
| [Bezgin et al. (2023)](/sources/bezgin-2023.md) §5.1.4 | $E(k)=Ak^4\exp(-2k^2/k_0^2)$ (Eq. 34) | Spyropoulos & Blaisdell cases 1–3, $M_t=0.2,0.4,0.6$, $\mathrm{Re}_T=2742$ | DNS reference; HLLC on $128^3$; LES on $32^3$; $\tau=\lambda_f/u'\approx0.85$ |
| [Bielawski et al. (2023)](/sources/bielawski-2023.md) App. A | $E(k)=\frac{16}{3}\sqrt{\frac2\pi}\,M_{t,0}^2c^2\,\frac{k^4}{k_0^5}\exp\!\big(-2(k/k_0)^2\big)$, $k_0=4$ (Eq. A.1) | A.1: $M_{t,0}=0.3$, $\mathrm{Re}_{\lambda,0}=30$; A.2: $M_{t,0}=0.6$, $\mathrm{Re}_{\lambda,0}=100$ | structured $64^3$ and skewed tetrahedral (32 edges per direction, maximum skewness 0.425); spectral data of Honein & Moin (A.1) and Johnsen et al. (A.2) |
| [Jain & Moin (2022)](/sources/jain-2022.md) §4.2, §5 | Honein (2005) | inviscid two-phase, $M_{t,0}=0.07$, density ratio 10; droplet-laden, $\mathrm{Re}_\lambda\approx75$, $M_{t,0}=0.07$ | $32^3$ to $t/\tau=20$; $256^3$ in $[0,\pi/2]^3$ with 1000 droplets |
| [Wang et al. (2026)](/sources/wang-2026.md) §6.4.3 | $E(k)\sim k^4\exp(-2(k/k_0)^2)$, $k_0=4$; $p_0=101325$ Pa, $T_0=300$ K, $\rho_0=1.1768$ kg m$^{-3}$, viscosity $\propto T^{3/4}$ | validation $M_{t,0}=0.6$, $\mathrm{Re}_{\lambda,0}=100$ to $t/\tau=4$; AMR runs $M_{t,0}=1.0$ | uniform $64^3$ against a $256^3$ run spectrally filtered to $64^3$ and Johnsen et al.; two-level AMR on a $64^3$ base |
| [Ducros et al. (1999)](/sources/ducros-1999.md) §4.1, Table I | THI: solenoidal, energy peaked at $k_0L_{\mathrm{ref}}=3$, uniform density and temperature; CBC: the Comte-Bellot–Corrsin spectrum at $tU_0/M=42$ | THI-1 to THI-6 inviscid, $M_t\approx0.13$ falling to 0.03 at $t\approx10t^*$ (THI-4); CBC-1 to CBC-3, $M_t=0.26$ | $32^3$, periodic box; reference: LES with the filtered-structure-function model and no artificial dissipation (THI-1, CBC-1), and the CBC experiment |
| [Pirozzoli (2010)](/sources/pirozzoli-2010.md) §3.1, Eq. (18) | $E(k)=A(k/k_0)^4\exp[-2(k/k_0)^2]$, $k_0=6$; zero initial temperature and density fluctuations | inviscid, $M_{t,0}=0.07$ (to $t/\tau\approx60$) and $0.3$ (to $t/\tau\approx270$), $M_t=u_{\mathrm{rms}}/\bar c$ | $32^3$ in $(2\pi)^3$, SSP-RK3 at CFL 1; at $0.07$ the dealiased spectral solution of Honein & Moin |
| [Pirozzoli (2011a)](/sources/pirozzoli-2011.md) §2.5, Fig. 1 | $E(k)\sim(k/k_0)^4\exp[-2(k/k_0)^2]$, $k_0=6$; zero initial temperature and density fluctuations | inviscid, $M_{t,0}=0.07$ (to $t/\tau=40$) and $0.3$ (to $t/\tau=80$) | $32^3$, SSP-RK3; at $0.07$ the dealiased spectral solution of Honein & Moin |
| [Fu et al. (2019d)](/sources/fu-2019-d.md) §V.G, Eqs. (48)–(49) | $E(k)\sim k^4\exp(-2(k/k_0)^2)$, $k_0=4$; $\rho_0=u_{\mathrm{rms},0}=T_0=1$, $\gamma=1.4$, $\mathrm{Pr}=0.7$, viscosity $\propto T^{0.75}$ | $M_{t,0}=\sqrt3\,u_{\mathrm{rms},0}/\langle c\rangle=0.6$, $\mathrm{Re}_{\lambda,0}=100$, $\lambda_0=0.5$, to $t/\tau=4$ with $\tau=\lambda_0/u_{\mathrm{rms},0}$ | $64^3$ and $128^3$; filtered DNS and DNS of Johnsen et al. (2010) |

In Bezgin et al. $\lambda_f$ and $u'$ are the longitudinal Taylor scale
and rms velocity of the cited setup. Jain & Moin's two-phase runs place a
slab of a lighter fluid ($\rho=0.1$ against 1) in the box, or 1000
initially spherical droplets of diameter about twice the Taylor scale
with droplet-to-carrier density ratios 1, 10, 100, 1000 and rms Weber
number 1.

## Runs and findings

**Numerical dissipation of reconstructions.** Hong, Ye & Ye compare
their efficiency-improved [TENO](/methods/targeted-eno.md) variants with
WENO schemes: TENO6 and TENO-M6 predict $M_t$ and $\rho_{\mathrm{rms}}$
much better than WENO-JS and are slightly less dissipative than
[WENO-CU6](/methods/weno-cu6.md); TENO8, TENO-M8 and WENO9 are similar
and less dissipative than WENO7 (Fig. 16). For TENO-A, as recorded on
[adaptive TENO](/methods/adaptive-teno.md),
[Fu (2023)](/sources/fu-2023.md) (§4.2) reports agreement with filtered
DNS on $64^3$.

**TENO-A against WENO-CU6 (the original runs).** In the paper that
introduced TENO5-A and TENO6-A, [Fu et al. (2019d)](/sources/fu-2019-d.md)
(§V.G, Figs. 11–14) find both "significantly better" than WENO-CU6 on
$64^3$ and in agreement with the filtered DNS for the velocity, density,
dilatation, vorticity and temperature fluctuations. Against the
localized-artificial-diffusivity scheme LAD-D2-0 of Kawai et al. (2010),
compared across papers, they predict the dilatation better and
slightly underestimate the vorticity. At $t/\tau=4$ the TENO6-A spectra
match the DNS over the resolved range; TENO5-A is as good below
wavenumber 24 and slightly more dissipative above, and neither piles
energy up at high wavenumbers. On $128^3$ both spectra agree with the
DNS.

**Dilatation-weighted JST dissipation in LES.** [Ducros et al. (1999)](/sources/ducros-1999.md)
(§4.1, Figs. 1–8) test the second-order Jameson–Schmidt–Turkel
dissipation of [artificial viscosity](/methods/artificial-viscosity.md)
in LES of decaying turbulence. With the filtered-structure-function
model, the kinetic energy of THI-1 to THI-4 decays as $t^{-1.4}$ after the
enstrophy peak $t^*$, a result the authors find insensitive to the
kind of dissipation. Second- plus fourth-order dissipation ($k_2=1.5$,
$k_4=0.02$, Jameson's pressure sensor; THI-2) is "clearly too
dissipative": the energy near the cut-off falls by more than a decade.
Without the fourth-order term (THI-3) the second-order term still
perturbs the subgrid model, chiefly at early times, when the energy at
the cut-off and hence the model dissipation are nearly zero. With the
pressure sensor multiplied by the dilatation ratio $\Phi_{\mathrm D}$ of
the [Ducros sensor](/definitions/ducros-shock-sensor.md) (THI-4) the run
"gives the same results" as the LES without artificial dissipation. The
skew-symmetric central scheme with neither model nor dissipation (THI-5)
diverges, and the sensor-weighted second-order dissipation without a model
(THI-6) only prevents divergence, leaving a $k^2$ equipartition
spectrum. On the Comte-Bellot–Corrsin field at $M_t=0.26$ the LES
without dissipation is within about 20 % of the experimental energy at
$t/t_0=4.07$; the dilatation-weighted dissipation stays close to it and
classical JST does not; the larger gap than at $M_t\approx0.13$ is
attributed to the higher turbulent Mach number (Figs. 7–8). The
decaying-turbulence LES fields then feed, through Taylor's hypothesis,
the inflow of their
[shock–turbulence interaction](/benchmarks/shock-turbulence-interaction.md)
runs (§4.3).

**Split central schemes at zero viscosity.** On the inviscid
Honein–Moin box, [Pirozzoli (2010)](/sources/pirozzoli-2010.md) (§3.1,
Figs. 2–3) runs the locally conservative
[split forms](/methods/split-convective-forms.md) of Feiereisen
(C-FE-SF), Blaisdell (C-BL-SF) and Kennedy–Gruber (C-KG-SF) at orders 2
to 10 (the fluxes of the
[conservative split derivative](/operators/conservative-split-derivative.md)).
Central differencing of the divergence form diverges within one eddy
turnover time at every order. At $M_{t,0}=0.07$ all split schemes keep
the kinetic energy (C-FE-SF and C-KG-SF within 0.6 %), but the rms
density drifts upward over long times without diverging, more at higher
order, whereas second order has the largest energy error and the
smallest density growth; the reference levels off at
$\rho'/(\rho_0M_{t,0}^2)\approx0.35$. At $M_{t,0}=0.3$ C-FE-SF diverges
within a few turnover times at every order and the text reports
divergence for the Blaisdell form as well, while C-KG-SF runs to
$t/\tau\approx270$ at every order, its fourth-order version tending to a
nearly statistically steady state. The review
[Pirozzoli (2011a)](/sources/pirozzoli-2011.md) (§2.5, Fig. 1; §3.5)
repeats the test with a wider set: the divergence-form central schemes
D2 and D6 diverge in less than one turnover time with growing kinetic
energy and falling entropy; seventh-order upwinding (D7) avoids
divergence but dissipates most of the kinetic energy within 10 turnover
times, and seventh-order WENO (W7) is "substantially poorer", that is
more dissipative, than D7; at $M_{t,0}=0.07$ the sixth-order Blaisdell
(S6) and Kennedy–Gruber (K6) split forms conserve kinetic energy and
entropy but let the density fluctuations grow, Tadmor's second-order
entropy-conserving scheme (T2) has larger long-time errors without
diverging, and the sixth-order entropy-consistent scheme of Honein &
Moin (H6) reproduces the inviscid limit; at $M_{t,0}=0.3$ every scheme
fails at large times except K6 and T2.

**Riemann solvers and implicit LES.** In Bezgin et al.'s
[JAX-Fluids](/software/jax-fluids.md), HLLC on $128^3$ recovers the DNS
$\rho_{\mathrm{rms}}(t)$; on $32^3$ the adaptive local deconvolution
method (ALDM) agrees with the DNS and plain HLLC does not (Fig. 12).

**Central against upwind fluxes, structured against skewed meshes.**
Bielawski et al. verify the convective schemes of their GPU OpenFOAM
solver. At $M_{t,0}=0.3$ the skew-symmetric central scheme on the
structured mesh tracks the spectral solution; HLLC is closer to it than
AUSMDV, which "adds additional numerical dissipation even at the
turbulent Mach number of 0.3"; the unstructured mesh deviates more and
piles energy up at small scales (Figs. A.13–A.14). At $M_{t,0}=0.6$ both
shock-capturing fluxes are much more dissipative than the central scheme
in enstrophy and dilatation, the HLLC–AUSMDV gap narrows, and mesh
skewness matters little compared with the flux (Figs. A.15–A.16). They
suggest a hybrid central/HLLC flux (see [HLL Riemann solvers](/methods/hll-riemann-solvers.md),
[hybrid schemes](/methods/hybrid-weno.md)).

**Split forms for two-phase flow.** In Jain & Moin's inviscid two-phase
box at density ratio 10, only their quadratic-split internal-energy flux
stays stable; the cubic-split forms diverge (Fig. 8; see
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md)
and [five-equation model](/definitions/five-equation-model.md)). In the
droplet-laden case the droplets enhance the early kinetic-energy decay,
more so with denser droplets, in qualitative agreement with Dodd &
Ferrante's incompressible results (§5, Figs. 9–10).

**High-order AMR at $M_{t,0}=1$.** Wang et al. (2026) first check
their single-level fifth-order WENO-JS solver on the uniform $64^3$ grid
at $M_{t,0}=0.6$: it agrees with the filtered $256^3$ reference and with
Johnsen et al.'s results, slightly more dissipative in the dilatational
kinetic energy (Fig. 19). They then run $M_{t,0}=1.0$ on a two-level
[AMR](/methods/adaptive-mesh-refinement.md) grid refined where the
dilatation falls below a user threshold whose value is not given, and
compare three inter-level transfers. Pure fifth/sixth-order WENO
interpolation gives the highest resolution but terminates at $t\approx3.4\tau$, during
the coarsening of shocklet regions, when one-sided restriction stencils
steepen the shocklets and corrupt the coarse values; second-order
conservative Berger–Colella transfers are the most dissipative; and
AMR-HybridWENO, which switches to the conservative linear transfer in
cells flagged by a Roe-averaged Lax wave-speed criterion and a
pressure-curvature sensor, runs through, its dissipation converging
towards that of WENO interpolation (Figs. 21–22). The test is their
evidence that non-conservative transfers break down when a
discontinuity is refined or coarsened abruptly (their scenario III,
§5.1).

## Forced subsonic turbulence

[Teissier et al. (2024)](/sources/teissier-2024.md) (§4.3, arXiv v2)
drive the turbulence instead of letting it decay, to compare the
inertial ranges of their finite-volume schemes S2 to S10 (orders 2 to
10, with the
[cell-average to point-value conversion](/operators/cell-average-point-value-conversion.md)
at faces and [constrained transport](/methods/constrained-transport.md)
for the magnetic field). The box is $[0,1]^3$, periodic, with $\rho_0=1$,
$\gamma=5/3$, $v=0$ and sound speed 1 at $t=0$. A stochastic
Ornstein–Uhlenbeck forcing acts on the wavenumbers $1\le\lvert k\rvert<3$
as an acceleration, $\partial_t(\rho v)=\rho f$ for a forcing field $f$
(page-local), with kinetic-energy injection rate $10^{-4}$ and zero
physical viscosity, so all dissipation is numerical. In the MHD runs an
electromotive forcing at $4\le\lvert k\rvert<5$ injects magnetic energy
at the same rate; it is placed at smaller scales to avoid a build-up of
cross-helicity, and the mean velocity generated by the driver is removed
at every forcing call because the magnetic field breaks Galilean
invariance (§3.5.4, §4.3.3).

**Heating and the energy sink.** Because the finite-volume form
conserves total energy, every unit of kinetic and magnetic energy the
scheme dissipates becomes heat: without a sink the temperature rises and
the rms Mach number falls. The authors' estimates (78)–(81) match an S4
run on $32^3$ with an equilibrium kinetic energy $1.64\times10^{-3}$, and
an energy sink with coefficient calibrated from the injection rate and
the initial velocity scale keeps the temperature constant (§4.3.1,
Eqs. (78)–(82), Fig. 12).

**Order against resolution.** In the hydrodynamic runs S10 on $64^3$
shows a level of detail similar to S2 on $256^3$, and its inertial range
in the velocity spectrum lies between those of S2 and S4 on $256^3$
(§4.3.2, Figs. 13–14, with the Kolmogorov $k^{-5/3}$ slope for
reference). In the MHD runs the power-law range of the velocity and
magnetic spectra grows with the order, but the gain from S8 to S10 is
smaller than the gains from S2 to S4, S4 to S6 and S6 to S8 (§4.3.3,
Fig. 15). The authors restrict their efficiency claims to smooth
subsonic flows; for supersonic flows they suggest, without testing,
flattening and positivity preservation (§1, §5). The same schemes'
dissipation on a smooth vortex is recorded on
[numerical dissipation](/definitions/numerical-dissipation.md).

## Driven turbulence at GPU scale

[Stone et al. (2026)](/sources/stone-2026.md) use driven turbulence to
demonstrate the scale of [AthenaK](/software/athenak.md), without a
reference or a scheme comparison: isothermal ideal-MHD turbulence on
$10{,}240^3$ cells in $256^3$ MeshBlocks on 65,536 GPUs of Frontier,
with [WENO-Z](/methods/weno-z.md), RK2 and HLLD, solenoidal real-space
driving at the largest scales, sonic Mach number $0.5$, Alfvén Mach
number 2 and $\delta B/\bar B\approx3$, over four eddy turnover times
(§3.2, Fig. 4); two-fluid ion–neutral turbulence on $1200^3$ with
PPM, IMEX3, ionization fraction 0.1 and drag coefficient $10^6$,
reaching sonic Mach number about 10 and Alfvén Mach number about 1
(§3.4, Fig. 8); and test particles in MHD turbulence on $1280^3$ (§4.2,
Fig. 19). See [piecewise parabolic method](/methods/piecewise-parabolic-method.md).

## Qualifications

- The decaying-turbulence sources use different spectra, Mach and Reynolds numbers and
  references, so their results are not comparable with each other; the
  Spyropoulos–Blaisdell and Johnsen et al. setups are taken from the
  cited works and not restated in full.
- Hong, Ye & Ye's definition of the Taylor scale and the normalization of
  $\rho_{\mathrm{rms}}$ in their Fig. 16 are not legible in the text read.
- Bielawski et al. are read as the accepted manuscript; their text
  assigns the $M_{t,0}=0.6$ spectrum to Fig. A.14, which shows the
  $M_{t,0}=0.3$ spectrum (the $M_{t,0}=0.6$ one is Fig. A.16).
- Bezgin et al. are read as arXiv v1; their reference for the Taylor
  scale and dissipation is a garbled entry (ref. [80]).
- Jain & Moin's comparison with Dodd & Ferrante is qualitative; their
  runs are shock-free ($M_{t,0}=0.07$).
- Wang et al. (2026) print the eddy-turnover time as
  $\tau=k_0/u_{\mathrm{rms},0}$ and do not give the dilatation threshold
  of their refinement criterion.
- Stone et al. (2026) print the driving spectrum as "$1\le2\pi
  k/L_{\mathrm{box}}\le3$, peaking at $2\pi k=2L_{\mathrm{box}}$", which
  is dimensionally inconsistent if $k$ is a wavenumber *(compiler check,
  not in the sources)*; and their §4.2 refers to "the $4096^3$
  turbulence simulation described in Section 3.2 and Figure 4", which
  describe a $10{,}240^3$ run.
- Ducros et al. (1999) print the enstrophy-peak time and its two
  theoretical estimates as "$t\approx15U_{\mathrm{ref}}/L_{\mathrm{ref}}$" and
  "28 and $19U_{\mathrm{ref}}/L_{\mathrm{ref}}$", with the units inverted
  against the $L_{\mathrm{ref}}/U_{\mathrm{ref}}$ used elsewhere (§4.1). Their
  runs are LES: the reference is their own LES without artificial
  dissipation, not a DNS.
- Pirozzoli (2010) and Pirozzoli (2011a) print the total kinetic energy
  as $\int\rho u^2\,dV$, without the factor ½, which is immaterial for the
  normalized histories they plot. Pirozzoli (2010) defines
  $M_t=u_{\mathrm{rms}}/\bar c$ without saying whether $u_{\mathrm{rms}}$ is a
  component or the magnitude, and the §3.1 text says that the Blaisdell
  form "leads to divergence" at $M_{t,0}=0.3$ while Fig. 3a shows its
  fourth-order run lasting to $t/\tau\approx245$, against 30–70 for the
  other orders. The two papers run the same setup over different
  horizons and scheme sets; the review's runs are not those of 2010.
- Fu et al. (2019d)'s comparison with LAD-D2-0 and other WENO schemes is
  across papers (their refs. [37], [13]).
- Teissier et al.'s forced runs are not decaying turbulence and use a
  different box, $[0,1]^3$, and forcing; they are recorded here as the
  same flow class, not as a comparable data point. Their Fig. 12 caption
  assigns panel (b) to the sound speed and (c) to the rms Mach number,
  while the panel axis labels show the reverse; the text follows the
  caption. They are read as arXiv v2, which carries an earlier title and
  two of the three authors.

# Citations

- [Hong, Ye & Ye (2022)](/sources/hong-2022.md) — §5.8, Fig. 16.
- [Bezgin et al. (2023)](/sources/bezgin-2023.md) — §5.1.4, Eq. 34, Fig. 12 (arXiv v1).
- [Bielawski et al. (2023)](/sources/bielawski-2023.md) — App. A, Eq. A.1, Figs. A.13–A.16 (accepted manuscript).
- [Jain & Moin (2022)](/sources/jain-2022.md) — §4.2, §5, Figs. 8–10.
- [Fu (2023)](/sources/fu-2023.md) — §4.2 (TENO-A, as recorded on the adaptive-TENO page).
- [Teissier et al. (2024)](/sources/teissier-2024.md) — §1, §3.5.4, §4.3, Eqs. (78)–(82), Figs. 12–15, §5 (arXiv v2).
- [Wang et al. (2026)](/sources/wang-2026.md) — §5.1, §6.4.3, Figs. 19–22.
- [Stone et al. (2026)](/sources/stone-2026.md) — §3.2, §3.4, §4.2, Figs. 4, 8, 19.
- [Ducros et al. (1999)](/sources/ducros-1999.md) — §4.1, Table I, Figs. 1–8.
- [Pirozzoli (2010)](/sources/pirozzoli-2010.md) — §3.1, Eq. (18), Figs. 2–3.
- [Pirozzoli (2011a)](/sources/pirozzoli-2011.md) — §2.5, Fig. 1; §3.5.
- [Fu et al. (2019d)](/sources/fu-2019-d.md) — §V.G, Eqs. (48)–(49), Figs. 11–14.
