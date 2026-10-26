---
type: Result
title: "Compressible MHD turbulence"
description: "In compressible MHD turbulence fluctuations can be Alfvénic, slow or fast magnetosonic, or none of these; a spatio-temporal decomposition finds most power off the linear dispersion branches and few fast modes, and subsonic compressible Hall-MHD runs show little Mach-number dependence of the cascade."
status: established
aliases: [compressible MHD turbulence, MHD wave-mode decomposition, fast modes, slow modes, non-wave fluctuations, compressible Hall MHD turbulence]
tags: [mhd, compressible, plasma, astrophysics, dns]
timestamp: 2026-10-26T05:06:00Z
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
[exact laws](/results/turbulence-exact-laws.md). Both are diagnostics of
simulated turbulence; neither proposes a closure.

Page-local notation: $f_c$ is the compressibility parameter of Gan et al.'s
velocity forcing; $A$, $F$, $S$ denote the Alfvén, fast and slow fractions of
the fluctuation power, and NW the non-wave fraction; $\omega$ is the angular
frequency of a space–time Fourier transform (not the specific dissipation
rate), and $\boldsymbol k$ the wavevector with $k_\parallel=k_x$ along
$\boldsymbol B_0$ and $k_\perp=(k_y^2+k_z^2)^{1/2}$; $l_\parallel$, $\lambda$
are the parallel and perpendicular separations of the structure functions
(the source's $L_\parallel$, $L_\perp$; the reference direction of the
separations is not stated), and $m_a$ the exponent of
$l_\parallel\propto\lambda^{m_a}$.

## Wave-mode content of driven turbulence

**Set-up** (Gan et al. 2022, §2.1, §3). Three isothermal ideal-MHD runs with
ATHENA++ (Stone et al. 2020, as recalled) at $512^3$, uniform density
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

- **Spatial-only** (after Cho & Lazarian 2003 and Yang et al. 2018, as
  recalled): each instantaneous velocity field is projected in Fourier space
  on the Alfvén, fast and slow eigenvector polarizations of linear MHD, so
  every fluctuation is forced into one of the three modes. The authors call
  its physical meaning "a bit unclear" for strong turbulence, where
  nonlinear interactions matter.
- **Spatio-temporal (4D FFT)** (after Svidzinski et al. 2009, as recalled): a
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
  turbulence (Bieber et al. 1996), as recalled (§3, §4).
- **Few fast modes.** In compressibly driven run C the fast fraction drops
  from 0.137 (spatial-only) to 0.024 (4D FFT, the abstract's "∼2%"); with
  incompressible driving it is negligible. Among waves the Alfvén mode
  dominates; run B, with magnetic forcing, has the largest Alfvén fraction
  under both methods. Slow modes cascade further in $k$ than Alfvén and fast
  modes (Fig. 1).
- **Method dependence.** The authors conclude that spatial projection "might
  be too optimistic" about the fraction of fast and compressible modes, and
  that the non-wave component should enter models of particle transport and
  energization (§4). Their spatial-only results with the injection range
  agree with Makwana & Yan (2020), who found fast-mode power up to about 30%
  of the total with highly compressible driving (§1, §3, as recalled).

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
2003, as recalled); compressible driving changes the total to 5/6 and the
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
  component (Ferrand et al. 2020, as recalled; §4, Fig. 4).
- **Compressible terms in the exact law.** The cascade rate of compressible
  MHD contains, besides the flux term, source terms built from the
  dilatation and density increments (Eq. 9); for weakly compressible runs
  (density nearly equal at the two points) the single-point dissipation term
  and the time derivative of the mean total energy are "almost equal", and
  the two-point dissipative and forcing terms, "likely to be
  scale-independent", "still
  have a significant impact on the energy balance" (§2.1, §5.2).

## Qualifications

- **Different regimes.** Gan et al. drive at $M_t\le0.18$ with a strong
  guide field and analyse a statistically steady state; Ferrand et al.
  analyse decay at initial Mach numbers 0.25–0.5 with and without a mean
  field. Neither reaches supersonic turbulence.
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
- **Numerics unreported.** Gan et al. give no Riemann solver,
  reconstruction or dissipation details; the fractions come from $512^3$
  runs analysed over about $10\tau_A$, and the authors note that resolving its low-frequency part
  needs longer times and larger domains (§4).

# Citations

- [Gan et al. (2022)](/sources/gan-2022.md) — §1; §2.1–§2.2; §3, Figs. 1–5; §4.
- [Ferrand et al. (2022)](/sources/ferrand-2022.md) — §2.1, Eq. (9); §3.1, Fig. 1; §4, Fig. 4; §5.2.
- [Schekochihin (2022)](/sources/schekochihin-2022.md) — §5.3, Eq. (5.8) (local-field measurement of anisotropy).
