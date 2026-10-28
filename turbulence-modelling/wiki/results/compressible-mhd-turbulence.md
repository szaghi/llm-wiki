---
type: Result
title: "Compressible MHD turbulence"
description: "Compressible MHD turbulence carries Alfvénic, slow, fast and non-wave fluctuations: most power lies off the dispersion branches, subsonic Hall-MHD cascades depend little on Mach number, trans-sonic compressive modes need bulk viscosity, a flare simulation shows Kelvin–Helmholtz-driven Alfvénic turbulence, and a nearly incompressible expansion yields a moment-transport closure for solar-wind turbulence."
status: established
aliases: [compressible MHD turbulence, MHD wave-mode decomposition, fast modes, slow modes, non-wave fluctuations, compressible Hall MHD turbulence, weakly compressible MHD, solar-flare turbulence, flare plasma turbulence, compressive-mode bottleneck, Helmholtz-decomposed spectra, nearly incompressible MHD, NI MHD, solar-wind turbulence transport model, turbulence transport model]
tags: [mhd, compressible, plasma, astrophysics, dns]
timestamp: 2026-10-28T07:08:00Z
---

# Compressible MHD turbulence

When the plasma is compressible, MHD turbulence carries — besides the
Alfvénic fluctuations that [reduced MHD](/definitions/reduced-mhd.md)
retains — slow and fast magnetosonic fluctuations and density and
internal-energy fluctuations, which exchange energy with the kinetic and
magnetic parts. Two questions about it appear in the bundle: how much of the
fluctuation power actually behaves as each linear wave mode, studied by
[Gan et al. (2022)](/sources/gan-2022.md) on driven runs, and whether the
energy cascade of compressible Hall MHD depends on the Mach number, studied
by [Ferrand et al. (2022)](/sources/ferrand-2022.md) on decaying runs through
[exact laws](/results/turbulence-exact-laws.md). A third, what dissipates the
compressive velocity modes, is studied by
[Beattie et al. (2025)](/sources/beattie-2025.md) with an explicit
[bulk viscosity](/definitions/bulk-viscosity.md). These are diagnostics of
simulated turbulence and propose no closure. A fourth strand is a
closure: the nearly incompressible MHD expansion in the turbulent Mach
number and the moment-transport model that [Adhikari et al.
(2023)](/sources/adhikari-2023.md) derive from it for the high-beta outer
heliosphere and test against spacecraft data.

Page-local notation: $f_c$ is the compressibility parameter of Gan et al.'s
velocity forcing; $A$, $F$, $S$ denote the Alfvén, fast and slow fractions of
the fluctuation power, and NW the non-wave fraction; $\omega$ is the angular
frequency of a space–time Fourier transform (not the specific dissipation
rate), and $\boldsymbol k$ the wavevector with $k_\parallel=k_x$ along
$\boldsymbol B_0$ and $k_\perp=(k_y^2+k_z^2)^{1/2}$; $l_\parallel$, $\lambda$
are the parallel and perpendicular separations of the structure functions
(the source's $L_\parallel$, $L_\perp$; the reference direction of the
separations is not stated), and $m_a$ the exponent of
$l_\parallel\propto\lambda^{m_a}$ (registry §11).

## Wave-mode content of driven turbulence

**Set-up** (Gan et al. 2022, §2.1, §3). Three isothermal ideal-MHD runs with
ATHENA++ (the authors cite Stone et al. 2020) at $512^3$, uniform density
$\rho_0=1$, guide field $\boldsymbol B_0=(8,0,0)$ and $v_A=8$, plasma beta
$\beta_p=8\pi p/B^2=0.4$, driven at $0<|\boldsymbol k|\le2$ by an
Ornstein–Uhlenbeck process with correlation time $0.5\tau_A$
($\tau_A=L_0/v_A$, $L_0$ the box length along $\boldsymbol B_0$). The
velocity forcing amplitude parallel to $\boldsymbol B_0$ is
$|\boldsymbol A_\parallel|=|\boldsymbol A_\perp|f_c/(1-f_c)$, so $f_c=0$ and
1 are the incompressible and fully compressible limits (page-local
amplitudes). Run A: velocity forcing, $f_c=0$, box $(2\pi)^3$; run B:
velocity and magnetic forcing, $f_c=0$, box $8\pi\times2\pi\times2\pi$; run
C: velocity forcing with $f_c=0.9$. The turbulent Mach number is
$M_t=0.12$–$0.18$. The equations solved are the ideal MHD equations
(§2.1); no explicit viscosity or resistivity and no Riemann solver or
reconstruction are stated (see [numerical
dissipation](/properties/numerical-dissipation.md)).

**Two decompositions** (§2.2):

- **Spatial-only** (after Cho & Lazarian 2003 and Yang et al. 2018, whom
  the authors cite): each instantaneous velocity field is projected in Fourier space
  on the Alfvén, fast and slow eigenvector polarizations of linear MHD, so
  every fluctuation is forced into one of the three modes. The authors call
  its physical meaning "a bit unclear" for strong turbulence, where
  nonlinear interactions matter.
- **Spatio-temporal (4D FFT)** (after Svidzinski et al. 2009, whom the authors cite): a
  3D spatial FFT at each of about 100 frames per $\tau_A$ over about
  $10\tau_A$, then a temporal FFT with a Hanning window; power at
  $(\boldsymbol k,\omega)$ is assigned to a mode only if $\omega$ lies within
  ±10% of that mode's linear frequency (tested also at ±3% and ±40%). The
  rest is the **non-wave** component.

**Fractions** (§3, Figs. 2–3), excluding the injection range
$|\boldsymbol k|\le2$ (about 70% of the power in run B) and the degenerate
$(k_\parallel=0,\omega=0)$ component (about 3%):

| Run | spatial-only $A/F/S$ | 4D FFT ±10%: NW$/A/F/S$ |
|---|---|---|
| A ($f_c=0$) | 0.237/0.003/0.760 | 0.792/0.204/$1\times10^{-4}$/0.003 |
| B ($f_c=0$, magnetic forcing) | 0.425/0.007/0.568 | 0.762/0.225/$8\times10^{-7}$/0.013 |
| C ($f_c=0.9$) | 0.210/0.137/0.653 | 0.729/0.238/0.024/0.009 |

At ±40% the non-wave fractions are 0.727, 0.590 and 0.535, at ±3% 0.795,
0.773 and 0.749; "the overall trends do not change" over that range, and
the main conclusions "do not change qualitatively" (§2.2, §3).
With the injection range included, the spatial-only fractions are
0.760/0.223/0.017 (A), 0.628/0.028/0.344 (B) and 0.400/0.206/0.394 (C).

- **Non-wave dominance.** Most of the power lies on none of the three
  dispersion branches and is concentrated at low frequency; the authors
  compare it with the "1/f noise" of Dmitruk & Matthaeus (2007, 2009) and
  with the 80%–20% two-dimensional/slab decomposition of solar-wind
  turbulence that they cite from Bieber et al. (1996) (§3, §4).
- **Few fast modes.** In compressibly driven run C the fast fraction drops
  from 0.137 (spatial-only) to 0.024 (4D FFT, the abstract's "∼2%"); with
  incompressible driving it is negligible. Among waves the Alfvén mode
  dominates; run B, with magnetic forcing, has the largest Alfvén fraction
  under both methods. Slow modes cascade further in $k$ than Alfvén and fast
  modes (Fig. 1).
- **Method dependence.** The authors conclude that spatial projection "might
  be too optimistic" about the fraction of fast and compressible modes, and
  that the non-wave component should enter models of particle transport and
  energization (§4). They state that their spatial-only results with the
  injection range agree with Makwana & Yan (2020), whom they cite for
  fast-mode power up to about 30% of the total with highly compressible
  driving (§1, §3).

**Anisotropy** (§3, Figs. 4–5). Contours of second-order velocity structure
functions of the separated components, fitted as $l_\parallel\propto\lambda^{m_a}$:

| Run, method | total or NW | $A$ | $F$ | $S$ |
|---|---|---|---|---|
| B, spatial-only | 2/3 | 2/3 | 1 | 2/3 |
| B, 4D FFT (±3%) | 2/3 | 1 | 1 | 1 |
| C, spatial-only | 5/6 | 2/3 | 4/5 | 2/3 |
| C, 4D FFT | 5/6 | 2/3 | 1 | 1 |

With incompressible driving the spatial-only method reproduces the
Goldreich–Sridhar anisotropy $m_a=2/3$ of [critical
balance](/properties/critical-balance.md) for the total, Alfvén and slow
components and the near-isotropy ($m_a=1$) of fast modes (Cho & Lazarian
2003, which the authors cite); compressible driving changes the total to 5/6 and the
fast component to 4/5. The 4D FFT gives the same or slightly steeper slopes;
the fast slope is 1 in both runs, and the total follows the non-wave slope
because non-wave fluctuations carry most of the power. The authors call the
4D-FFT slow component possibly "too noisy to be accurate" and say that
the slopes, "showing slight variations under different conditions", call
for "additional theoretical and numerical studies" (§3, p. 6).

## Compressible Hall MHD in decay

Ferrand et al. (2022, §3–§4) run freely decaying isothermal compressible
Hall MHD at $1024^3$ (pseudo-spectral, $\nu=\eta_m=3\times10^{-4}$, ion
inertial length $0.02L_0$; equations and runs on [exact
laws](/results/turbulence-exact-laws.md)). Findings that bear on
compressibility:

- **Energy exchange with internal energy.** In Run I (mean field $B_0=2$),
  the sum of kinetic and magnetic energy oscillates in step with the
  internal energy, which the authors attribute to wave-initiated exchanges,
  "as reported in Yang et al. (2021)" (§3.1, Fig. 1).
- **Weak Mach-number dependence.** Raising the initial sonic Mach number from
  0.25 to 0.5 "does not bring significant changes to the total dynamics" of
  the cascade rate, in agreement with Andrés et al. (2018) up to 0.5;
  supersonic flows can develop a dominant compressible, source-like cascade
  component (the authors cite Ferrand et al. 2020; §4, Fig. 4).
- **Compressible terms in the exact law.** The cascade rate of compressible
  MHD contains, besides the flux term, source terms built from the
  dilatation and density increments (Eq. 9); for weakly compressible runs
  (density nearly equal at the two points) the single-point dissipation term
  and the time derivative of the mean total energy are "almost equal", and
  the two-point dissipative and forcing terms, "likely to be
  scale-independent", "still
  have a significant impact on the energy balance" (§2.1, §5.2).

## Weak compressibility as a numerical route

Compressibility can also be a property of the solver rather than of the
physics. [Foldes et al. (2023)](/sources/foldes-2023.md) target
incompressible Hall MHD but solve the **weakly compressible** equations with
a [lattice Boltzmann](/methods/lattice-boltzmann-method.md) scheme: mass and
momentum conservation with the Maxwell stress
$\tfrac12|\boldsymbol B|^2\delta_{ij}-B_iB_j$ in the momentum flux, the
isothermal closure $p=\rho c_s^2$ ($c_s$ the lattice sound speed,
page-local), which they call consistent with density fluctuations of order
$M^2$, and the Hall induction equation in conservative form (§2.2,
Eqs. 2.10–2.14). Points that bear on compressibility:

- **Measured density fluctuations.** On an exact incompressible Hall-MHD
  solution, relative density fluctuations are "typically of order
  $10^{-7}$–$10^{-6}$" and decrease with the Mach number, for
  $M=0.003$–$0.01$ (§4.2, Fig. 5).
- **Acoustic time step.** Because the scheme resolves sound waves, its time
  step in plain MHD is smaller than that of an incompressible pseudo-spectral
  solver by roughly the Mach number (the authors cite Horstmann et al. 2022), so
  the weakly compressible route pays off only in Hall MHD, where whistler
  waves limit both (§5; see [GHOST](/software/ghost.md)).
- **Extension.** An incompressible or weakly compressible formulation is
  "usually justified" for space plasmas (the authors cite Andrés et al. 2022
  and Brodiano et al. 2023); accounting for compressibility explicitly would
  need an additional equation of state and a coupled lattice scheme for
  temperature or density (§7; cf. §2.2).

Ferrand et al. (2022) run compressible Hall MHD at initial sonic Mach
numbers 0.25–0.5 and measure its cascade; Foldes et al. run at Mach
numbers of $6\times10^{-5}$–$2.5\times10^{-2}$ (Tables 1–2, §4.4) to approximate
incompressible dynamics.

## Turbulence generated in a 3D solar-flare simulation

[Ruan et al. (2023)](/sources/ruan-2023.md) study how compressible MHD
turbulence forms, rather than how it cascades. Their setting is a stratified,
reconnection-driven solar flare. The paper uses no turbulence closure and
no subgrid model: the turbulence is what the resistive MHD run resolves.
The paper does not discuss numerical dissipation, and it does not use the
term implicit LES.

**Set-up** (§2). The code is MPI-AMRVAC. It solves resistive MHD with
gravity, field-aligned thermal conduction (with the transition-region
adaptive conduction treatment), optically thin radiative losses and a
static background heating. The box spans $100\times100\times100$ Mm, with
a base grid of $64^3$ and five levels of [mesh
adaptation](/methods/mesh-adaptation.md). This gives an effective $1024^3$,
with smallest cells below 100 km. The flux is HLL, with the third-order
Cada3 limiter on coarse levels and the van Leer limiter on fine levels.
Time integration is three-stage strong-stability-preserving Runge–Kutta.
The initial field is a sheared current sheet of strength 30 G and
half-width 10 Mm (Eqs. 1–3). Reconnection is triggered by a two-stage
anomalous magnetic diffusivity $\eta_m$ (the source's $\eta$), given in
code units with no stated normalization (Eqs. 4–5). The local enhancement
switches on at $t=450$ s and off at $t=480$ s. No Reynolds, Mach or
Lundquist numbers are quoted.

**Diagnostics** (page-local symbols). Turbulence is measured as the
fluctuation of a single snapshot about an average along the line of sight
$x$. It is a spatial decomposition, not an ensemble or time average. With
$n_e$ the electron number density and $u_x$ the line-of-sight velocity,
the nonthermal velocity (Eq. 6) is the $n_e$-weighted standard deviation

$$v_{\mathrm{nth}}=\left[\frac{\int n_e u_x^2\,dx-\left(\int n_e u_x\,dx\right)^2\big/\int n_e\,dx}{\int n_e\,dx}\right]^{1/2}.$$

The turbulent kinetic and magnetic column energies (Eqs. 7–8, page-local
$\mathcal E_u$, $\mathcal E_b$) are printed as

$$\begin{aligned}\mathcal E_u&=\int\rho u_x^2\,dx-\left(\int\rho u_x\,dx\right)^2\Big/\int\rho\,dx,\\ \mathcal E_b&=\int B_x^2\,dx-\left(\int B_x\,dx\right)^2\Big/\int dx.\end{aligned}$$

Only the $x$ components enter. The authors justify this with the
assumption that Alfvénic turbulence develops only perpendicular to the mean
field, and in this view $x$ is perpendicular to the flare loops (§3.5).

**Findings** (§3.2–§3.5; one simulation, compared qualitatively with
spectroscopic observations):

- **Kelvin–Helmholtz generation.** Reconnection downflows collide with the
  flare arcade and form a termination shock and reflected upflows. Vortices
  appear where the vertical velocity jumps by more than 1000 km s$^{-1}$
  over about 2 arcsec. The shear lies in planes perpendicular to the local
  guide field, where tension cannot stabilize it. A growth estimate
  $\sigma_{\mathrm{KH}}=kv_0$ (the source's $\omega$, which the authors cite from Goedbloed
  et al. 2019; with $\sigma_{\mathrm{KH}}$ the page-local growth rate, $k$ the
  inverse of several Mm and $v_0$ the half shear speed, hundreds to 1000 km s$^{-1}$)
  gives growth times of seconds. That is the same order as the vortex
  formation in the run (§3.3). *(Compiler check, not in the sources:
  $1/k=2$–5 Mm and $v_0=300$–1000 km s$^{-1}$ give 2–17 s.)* The
  Rayleigh–Taylor and Richtmyer–Meshkov fingers at the arcade top appear
  later and lie below the region of maximum nonthermal velocity
  (§3.1, §3.3; see [Rayleigh–Taylor mixing](/benchmarks/rayleigh-taylor-mixing.md)).
  The perpendicular-shear mechanism is said to be "missed in 2D settings"
  (§4). Its anisotropy is discussed on [critical
  balance](/properties/critical-balance.md).
- **Magnitude.** The synthetic nonthermal velocity peaks above the loop top,
  near the termination shock, at more than 200 km s$^{-1}$. Gaussian fits
  of synthetic Fe XXIV 255 Å spectra give 245 and 148 km s$^{-1}$ in two
  boxes (§3.2, Fig. 2). The maximum lies where the mean field is below
  25 G (§3.2).
- **Alfvénic character.** Low in the atmosphere, the fluctuations are
  carried down the field rather than generated locally. $B_x$ and $u_x$
  are in antiphase for structures propagating along the field and in phase
  for those propagating against it. Fitted propagation speeds (430 and
  1600 km s$^{-1}$) are close to the local $v_A$. Motions reach about
  10 km s$^{-1}$ at 2 Mm height, where $n_e\sim10^{11}$ cm$^{-3}$ (§3.4,
  Fig. 4). $\mathcal E_u$ and $\mathcal E_b$ have similar magnitude and
  spatial distribution, and $\mathcal E_u$ follows $\mathcal E_b$ in time,
  which the authors call "a feature of Alfvénic motions" (§3.5, Fig. 5).
- **Energy fraction.** The domain-integrated turbulent energy
  $E_{\mathrm{tur}}$ (the sum of $\mathcal E_u$ and $\mathcal E_b$) is about
  10% of $E_{\mathrm{dn}}$, the time-integrated kinetic energy of the
  reconnection downflow across $z=45$ Mm (both page-local). The time-integrated
  transfer exceeds the instantaneous turbulent energy, because turbulent
  energy is continuously transported to the chromosphere and diffused (§3.5, Fig. 5(d);
  the abstract says "more than 10%").

The authors claim that the mechanism holds for any reconnecting flare,
whatever its size, because MHD is scale invariant (§4). The run itself
includes gravity, thermal conduction, radiative losses, an anomalous
resistivity and a finest cell size (§2), and the paper reports no
resolution study.

## Compressive modes and bulk viscosity at trans-sonic Mach number

[Beattie et al. (2025)](/sources/beattie-2025.md) (read in arXiv v4) split
the velocity of forced, isothermal, visco-resistive MHD turbulence without a
mean field ($M_t\approx1$, $Re=Rm=1000$, $Pm=1$, $128^3$–$1024^3$, modified
FLASH; set-up on [small-scale dynamo](/results/small-scale-dynamo.md)) by a
Helmholtz decomposition into a compressive (curl-free) part
$\boldsymbol u_{\mathrm c}$ and a solenoidal (divergence-free) part
$\boldsymbol u_{\mathrm s}$, with kinetic-energy spectra
$E_{\mathrm c}(k)$ and $E_{\mathrm s}(k)$ (registry §11; the source writes
$\parallel$ and $\perp$, which on this page would read as directions
relative to the field), computed by Fourier projection on $\boldsymbol k$
(§4.5, Eq. 49). They vary the bulk viscosity through the viscous Prandtl
number $P_\nu=\nu/\nu_b$ (registry §11, defined on
[bulk viscosity](/definitions/bulk-viscosity.md)), from $\infty$ (no bulk
viscosity) to 0.001. Findings:

- **Spectral slopes.** $E_{\mathrm c}(k)\sim k^{-2}$ (Burgers-like) in the
  runs with low bulk viscosity, not the $k^{-3}$ pseudo-acoustic spectrum
  that Wang et al. (2017) and Sakurai & Ishihara (2023) find, which the
  authors place below $M_t\approx0.4$; $E_{\mathrm s}(k)$ is
  roughly $k^{-5/3}$ over a very truncated range (§6.2, Fig. 9).
- **A compressive-mode bottleneck without bulk viscosity.** For $P_\nu=\infty$
  and 1, compressive power piles up at high $k$: $E_{\mathrm c}/E_{\mathrm s}$
  grows from about $10^{-1}$ at large scales to about $10^2$ at small
  scales, the "sub-shear-viscous range" of their Eq. (32), where
  compressive power exceeds solenoidal power, which disappears for $P_\nu\le0.1$; at the smallest $P_\nu$ the low-$k$
  compressive modes lose "roughly $10^2$ in total power" (§6.1–6.2, Fig. 9).
  See [bottleneck effect](/definitions/bottleneck-effect.md).
- **Compressive energy fraction.** $\langle E_{\mathrm c}\rangle/\langle E_{\mathrm{kin}}\rangle$
  falls from about $10^{-1}$ to about $10^{-3}$ as $P_\nu$ goes from $\infty$
  to 0.001, roughly $\propto P_\nu$ for $P_\nu<1$ (Eq. 54, Fig. 6).
- **Alfvénic character of the compressive modes.** At saturation the
  compressive modes hold 1 to 10 times less energy than the magnetic field
  (sub- to trans-Alfvénic), the solenoidal modes about ten times more
  (§5.1, Fig. 6); for $P_\nu=0.01$ the magnetic-to-compressive spectral ratio
  reaches about $10^3$ at high $k$ (§8, Fig. 13).
- **Coupling between the families.** In the Stokes limit the viscous
  operators act on the two families separately (§6.2, Eqs. 56–57, App. E),
  yet low $P_\nu$ also suppresses high-$k$ solenoidal and magnetic modes; the
  authors attribute the coupling to the reduced compressive energy
  available for small-scale enstrophy production through
  $\boldsymbol\omega(\nabla\cdot\boldsymbol u)$, citing Touber (2019)
  (§6.2).
- **Resolution.** Without explicit bulk viscosity the compressive modes are
  dissipated by the grid and the Riemann solver, so that a shear-viscous
  "DNS" is "an implicit large eddy simulation for the compressible modes"
  (§9.1, App. D); see [bulk viscosity](/definitions/bulk-viscosity.md),
  [implicit LES](/definitions/implicit-les.md) and
  [numerical dissipation](/properties/numerical-dissipation.md).

The authors add that a Braginskii (anisotropic) viscosity contains a
bulk-viscous-type term built on the field direction that would preferentially
damp fast and slow magnetosonic waves (§9.3, stated without simulation).

## Nearly incompressible MHD and a turbulence transport model

**The expansion.** Nearly incompressible (NI) MHD, which [Adhikari et al.
(2023)](/sources/adhikari-2023.md) (§1–§2) cite from Zank & Matthaeus and
Hunana & Zank, expands the fluctuations about a
slowly varying, inhomogeneous background (here the solar wind, with
velocity $\boldsymbol U$, field $\boldsymbol B_{\mathrm{sw}}$, density
$\rho_{\mathrm{sw}}$ and Alfvén velocity $\boldsymbol V_A$, all page-local)
in the turbulent Mach number $M_t\ll1$:

$$\boldsymbol u'=\boldsymbol u^{(0)}+M_t\,\boldsymbol u^{(1)},\quad p'=M_t^2\big(p^{(0)}+p^{(1)}\big),\quad \rho'=M_t\,\rho^{(0)}+M_t^2\rho^{(1)},\quad \boldsymbol B'=\boldsymbol B^{(0)}+M_t\,\boldsymbol B^{(1)}$$

(Eq. 3; superscripts $(0)$ and $(1)$, page-local, mark the leading and
higher orders). Which fluctuations sit at leading order depends on the
plasma beta $\beta_p$. For $\beta_p\ll1$ and $\beta_p\sim1$, Adhikari et al. state, citing
Zank et al. (2017), the leading order is two-dimensional
(structures such as flux ropes and magnetic islands, without the Alfvén
velocity) and the slab (Alfvénic) and compressible magnetosonic parts are
higher-order corrections. For $\beta_p\gg1$ Adhikari et al. derive (§2,
Eqs. 4–6) a leading order that is fully incompressible MHD carrying both
the 2D and the slab component at the same order, so the two "cannot be
distinguished", with the Alfvén velocity present. The leading-order
velocity is not solenoidal in the inhomogeneous background,

$$\nabla\cdot\boldsymbol u^{(0)}=-\frac{1}{\rho_{\mathrm{sw}}}\,\boldsymbol u^{(0)}\cdot\nabla\rho_{\mathrm{sw}},\qquad \nabla\cdot\boldsymbol B^{(0)}=0$$

(Eq. 6), which is why their Elsasser equation (Eq. 7, with
$\boldsymbol Z^\pm=\boldsymbol u\pm\boldsymbol B/\sqrt{\mu_0\rho_{\mathrm{sw}}}$,
$\boldsymbol Z^+$ outward) carries density-gradient terms absent from the
incompressible Elsasser equations of Marsch & Tu and Zhou & Matthaeus they
cite; see [reduced MHD](/definitions/reduced-mhd.md) for the homogeneous,
strong-guide-field limit.

**The moment closure.** Taking moments of the Elsasser equation with the
closures of Zank et al. (2012a) they cite, Adhikari et al. (§2, Eqs. 8–11)
write six transport equations for the Elsasser energies
$\langle|\boldsymbol Z^\pm|^2\rangle$ (no factor $\tfrac12$), the residual
energy $E_D=\langle\boldsymbol Z^+\cdot\boldsymbol Z^-\rangle$ and the
energy-weighted correlation lengths $\ell^\pm$, $\ell_D$ ($E_D$, $\ell^\pm$
registry §11, $\ell_D$ page-local; $\langle\cdot\rangle$ an ensemble average). The Elsasser-energy
equation reads

$$\begin{aligned}
&\partial_t\langle|\boldsymbol Z^\pm|^2\rangle+(\boldsymbol U\mp\boldsymbol V_A)\cdot\nabla\langle|\boldsymbol Z^\pm|^2\rangle+\Big(\tfrac12\nabla\cdot\boldsymbol U\pm\nabla\cdot\boldsymbol V_A\Big)\langle|\boldsymbol Z^\pm|^2\rangle\\
&\quad+\Big(2a_s-\tfrac12\Big)(\nabla\cdot\boldsymbol U)E_D\pm(2b_s-1)(\nabla\cdot\boldsymbol V_A)E_D\mp\frac{b_s}{\rho_{\mathrm{sw}}}(\boldsymbol V_A\cdot\nabla\rho_{\mathrm{sw}})\langle|\boldsymbol Z^\pm|^2\rangle\\
&\quad=-2\alpha_{\mathrm{KT}}\frac{\langle|\boldsymbol Z^\pm|^2\rangle\langle|\boldsymbol Z^\mp|^2\rangle^{1/2}}{\ell^\pm}+2S^\pm,
\end{aligned}$$

and the correlation lengths obey

$$\partial_t\ell^\pm+(\boldsymbol U\mp\boldsymbol V_A)\cdot\nabla\ell^\pm+(\ell_D-2\ell^\pm)\Big[\Big(a_s-\tfrac14\Big)\nabla\cdot\boldsymbol U\pm\Big(b_s-\tfrac12\Big)\nabla\cdot\boldsymbol V_A\Big]\frac{E_D}{\langle|\boldsymbol Z^\pm|^2\rangle}=2\beta_{\mathrm{KT}}\langle|\boldsymbol Z^\mp|^2\rangle^{1/2}-2S^\pm\frac{\beta_{\mathrm{KT}}}{\alpha_{\mathrm{KT}}}\frac{\ell^\pm}{\langle|\boldsymbol Z^\pm|^2\rangle}$$

(Eqs. 8 and 10). Here $\alpha_{\mathrm{KT}}$ is the von Kármán–Taylor
constant of the nonlinear (cascade) term, closed as
$\boldsymbol Z^\mp\cdot\nabla\boldsymbol Z^\pm\simeq\alpha_{\mathrm{KT}}Z^\pm\langle|\boldsymbol Z^\mp|^2\rangle^{1/2}/\ell^\pm$,
$\beta_{\mathrm{KT}}=\alpha_{\mathrm{KT}}/2$ its length-scale counterpart
(after Breech et al. 2008), $a_s=b_s=\tfrac12$ the structural similarity
parameters that give the two-dimensional form of the mixing tensors, and
$S^\pm$ the sources ($\alpha_{\mathrm{KT}}$, $\beta_{\mathrm{KT}}$, $a_s$, $b_s$
registry §11, $S^\pm$ page-local). The correlation
$\langle\boldsymbol Z^\pm\cdot\nabla\rho_{\mathrm{sw}}\rangle$ is set to
zero by assuming isotropic turbulence, which the authors mark as a
departure from Zank et al. (2017). The equations differ from those of
Zank et al. (2012a) because they are derived for
$\nabla\cdot\boldsymbol u\ne0$ (§2, §8). The cascade rate is taken equal to the
dissipation rate, and the turbulent heating
$\alpha_{\mathrm{KT}}m_pn\big[\langle|\boldsymbol Z^+|^2\rangle\langle|\boldsymbol Z^-|^2\rangle^{1/2}/\ell^++\langle|\boldsymbol Z^-|^2\rangle\langle|\boldsymbol Z^+|^2\rangle^{1/2}/\ell^-\big]$
($m_p$ the proton mass, $n$ the wind proton density) heats protons and
electrons in the ratio 60:40 of a three-fluid (proton, electron,
pickup-ion) steady wind (§5, Eqs. 20–34). A density-variance equation
with a nonlinear decay term and shear and pseudosound sources is added
(§4, Eqs. 16–19); the pseudosound source, sound waves excited by
Alfvén waves, is found negligible.

**Calibration and evidence.** In the steady, spherically symmetric
reduction (Eqs. 12–15) the sources are a stream-shear term decaying as
$r^{-2}$ ($r$ the heliocentric distance, page-local), following Zank et
al. (2017) rather than the $r^{-1}$, energy-proportional form of earlier
models they cite, and a pickup-ion source that drives only Alfvénic
fluctuations. The constants are calibrated: $\alpha_{\mathrm{KT}}=0.03$,
chosen so that the turbulent heating is not excessive and the computed
temperatures resemble the observed ones, against 1, 0.8 and 0.128 used in
the earlier works they list; shear strengths 0.3 and 0.7 against about
13 and 1–2 in earlier works; pickup-ion fraction 0.06 (§3, Table 2).
Solved from 1 to 75 au and compared with 27 years of Voyager 2 data, two
of Ulysses and 13 of New Horizons, the model reproduces the Elsasser,
kinetic and magnetic fluctuation energies, the normalized cross-helicity
and residual energy, the Elsasser correlation lengths, the density
variance ($r^{-4.48}$ computed against $r^{-4.71}$ observed) and the
wind and pickup-ion profiles "with some scatter" (§6–§7, Figs. 1–7). The
pickup-ion source flattens the Elsasser energies beyond about 25 au. The
correlation lengths of the residual energy and of the velocity
disagree (computed ones vary, observed ones stay roughly constant), which
the authors attribute to a shear source derived for low-beta models
(§6, Fig. 4). The computed pickup-ion beta exceeds 1 beyond 10 au and
reaches 11.4 at 75 au, while the proton and electron betas stay below 1
(§7, Fig. 6). The comparison concerns one-dimensional steady radial
profiles; the source has no numerical turbulence simulation. Imbalance and
residual energy are on [critical balance](/properties/critical-balance.md).

## Qualifications

- **Different regimes.** Gan et al. drive at $M_t\le0.18$ with a strong
  guide field and analyse a statistically steady state; Ferrand et al.
  analyse decay at initial Mach numbers 0.25–0.5 with and without a mean
  field. Neither reaches supersonic turbulence. Beattie et al. (2025) are
  trans-sonic ($M_t\approx0.90$–$0.96$), without a mean field and with 2:1
  solenoidal-to-compressive forcing. Foldes et al. run at
  $M\le0.025$ only to approximate incompressible dynamics.
- **Reference frame.** Gan et al. define $k_\parallel\simeq k_x$ along
  the guide field $\boldsymbol B_0$ (§3, p. 3) and do not state whether the
  structure-function separations are taken along $\boldsymbol B_0$ or along
  a local field. [Schekochihin (2022)](/sources/schekochihin-2022.md)
  (§5.3, Eq. 5.8), as summarized on [critical
  balance](/properties/critical-balance.md), states that scale-dependent
  anisotropy is visible only when increments are taken along the local
  field.
- **Printed inconsistencies** (Gan et al., arXiv v1). §3 states that the
  total wave fraction from the 4D FFT is "less than ∼25%" and §4 that the
  non-wave component carries "about 75−80%". *(Compiler check, not in the
  sources: the printed ±10% fractions give a wave fraction
  $1-0.729=0.271$ and a non-wave fraction of 0.729 for run C.)* §3 also
  calls the fast fraction "increasing" with compressible driving, while the
  printed spatial-only fractions with the injection range give 0.223 for run
  A and 0.206 for run C; the increase holds from run B (0.028) to run C.
  The set-up prints $v_A=8$ with $B_0=8$, $\rho_0=1$ (no $4\pi$) next to the
  Gaussian $\beta_p=8\pi p/B^2$; the sound speed is not printed.
- **Printed inconsistencies** (Ruan et al. 2023). §3.5, p. 9 calls $E_k$
  (this page's $E_{\mathrm{dn}}$) "the instantaneous turbulence energy".
  The preceding paragraph defines $E_k$ as the time-integrated downflow
  kinetic energy, so the sentence fits only the turbulent energy
  $E_{\mathrm{tur}}$. Eqs. 7–8 print no factor $\tfrac12$, and Eq. 8 prints
  no $1/(8\pi)$, while Fig. 5 gives the energies in erg cm$^{-2}$ and the
  text quotes fields in gauss. The paper does not state the units of
  $B_x$ in Eq. 8, so the printed near-equality of $\mathcal E_u$ and
  $\mathcal E_b$ cannot be converted to a physical equipartition ratio
  from the paper alone.
- **Turbulence as dispersion.** Ruan et al.'s turbulence is a
  line-of-sight velocity dispersion of one snapshot (Eqs. 6–7). For the unresolved mass motions of
  observed flares, the authors note that whether energy cascades occur is
  "impossible to know" from remote observations (§1).
- **Nearly incompressible MHD transport** ([Adhikari et al.
  2023](/sources/adhikari-2023.md)). Table 2 prints the length-scale
  constant as "$\beta$ 0.015", the symbol of the plasma beta; the value is
  $\beta_{\mathrm{KT}}=\alpha_{\mathrm{KT}}/2$ of the text. The
  shear-source strength of the density-variance equation is
  $1.8\times10^{-4}$ in §4 and $1.8\times10^{-5}$ in Table 2. The model
  constants are calibrated to heliospheric profiles: the authors list
  $\alpha_{\mathrm{KT}}=1$, 0.8 and 0.128 and shear strengths of about 13
  and 1–2 in earlier transport models against their 0.03, 0.3 and 0.7
  (§3).
- **Numerics unreported.** Gan et al. give no Riemann solver,
  reconstruction or dissipation details; the fractions come from $512^3$
  runs analysed over about $10\tau_A$, and the authors note that resolving its low-frequency part
  needs longer times and larger domains (§4).

# Citations

- [Gan et al. (2022)](/sources/gan-2022.md) — §1; §2.1–§2.2; §3, Figs. 1–5; §4.
- [Ferrand et al. (2022)](/sources/ferrand-2022.md) — §2.1, Eq. (9); §3.1, Fig. 1; §4, Fig. 4; §5.2.
- [Schekochihin (2022)](/sources/schekochihin-2022.md) — §5.3, Eq. (5.8) (local-field measurement of anisotropy).
- [Foldes et al. (2023)](/sources/foldes-2023.md) — §2.2, Eqs. (2.10)–(2.14); §4.2, Fig. 5; §5; §7 (weakly compressible lattice Boltzmann formulation of Hall MHD, density fluctuations, acoustic time step, compressible extension).
- [Ruan et al. (2023)](/sources/ruan-2023.md) — §1; §2, Eqs. (1)–(5); §3.1–§3.5, Eqs. (6)–(8), Figs. 2–5; §4 (Kelvin–Helmholtz-generated, Alfvénic turbulence in a 3D resistive MHD flare simulation; nonthermal velocity and turbulent energy diagnostics).
- [Beattie et al. (2025)](/sources/beattie-2025.md) — §4.5, Eq. (49); §5.1, Eq. (54), Fig. 6; §6.1–6.2, Eqs. (56)–(57), Fig. 9; §8, Fig. 13; §9.1, §9.3; App. D; App. E (Helmholtz-decomposed spectra, compressive-mode bottleneck and bulk viscosity in trans-sonic MHD turbulence).
- [Adhikari et al. (2023)](/sources/adhikari-2023.md) — §1; §2, Eqs. (3)–(11); §3, Eqs. (12)–(15), Table 2; §4, Eqs. (16)–(19); §5, Eqs. (20)–(34); §6–§8, Figs. 1–7 (nearly incompressible MHD at high plasma beta and its turbulence transport model).
