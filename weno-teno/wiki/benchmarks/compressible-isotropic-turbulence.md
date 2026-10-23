---
type: Benchmark
title: "Compressible isotropic turbulence"
description: "Triply periodic turbulence box. In the decaying form a random solenoidal velocity field of prescribed spectrum and turbulent Mach number 0.07–0.6 decays, and the histories of kinetic energy, turbulent Mach number, density fluctuations, enstrophy and dilatation measure numerical dissipation on under-resolved turbulence with eddy shocklets; driven subsonic hydrodynamic and MHD variants compare inertial ranges across scheme orders."
status: established
aliases: [decaying compressible isotropic turbulence, decaying isotropic turbulence, compressible homogeneous isotropic turbulence, compressible HIT, decaying HIT, forced compressible turbulence, driven subsonic turbulence]
tags: [benchmark, turbulence, low-dissipation, teno]
timestamp: 2026-10-23T23:55:00Z
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

## Qualifications

- The four sources use different spectra, Mach and Reynolds numbers and
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
