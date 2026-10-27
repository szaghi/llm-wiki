---
type: Definition
title: "Bulk viscosity"
description: "The bulk (volume) viscosity multiplies the velocity divergence in the Newtonian stress and damps only compressive motion; the page gathers its kinetic-theory origin, its role in the dissipation budget, its explicit use in compressible MHD turbulence, where it removes a compressible-mode bottleneck, and artificial bulk viscosity for shock capturing."
status: established
aliases: [volume viscosity, dilatational viscosity, second viscosity, bulk viscous Reynolds number, viscous Prandtl number, Stokes hypothesis]
tags: [compressible, dns, implicit-les, numerical-dissipation, mhd]
timestamp: 2026-10-27T05:46:00Z
---

# Bulk viscosity

The **bulk viscosity** $\mu_b$ (page-local; kinematic $\nu_b=\mu_b/\rho$) is the
coefficient of the isotropic, divergence-proportional part of the Newtonian
viscous stress,

$$\sigma_{ij}=2\mu S^d_{ij}+\mu_b\,S_{kk}\,\delta_{ij},\qquad S_{kk}=\nabla\cdot\boldsymbol u .$$

The registry's viscous stress $\sigma_{ij}=2\mu S^d_{ij}$ is the special case
$\mu_b=0$, the **Stokes hypothesis**. The bulk viscosity acts only on compressive
(dilatational) motion: it does no work on a solenoidal velocity field. It is
related to the "second viscosity coefficient" $\lambda_{\mathrm v}$
(page-local; not the Taylor microscale $\lambda$) by
$\mu_b=\lambda_{\mathrm v}+\tfrac23\mu$, as stated by
[Beattie et al. (2025)](/sources/beattie-2025.md), footnote 2, who vary
$\nu_b$ at fixed $\nu$, "equivalent to changing $\lambda$ for fixed
$\nu_{\rm shear}$". The sources use it in three ways: as a physical property
of molecular gases, as an inherent property of a kinetic discretization, and
as an artificial dissipation for shocks.

Page-local symbols: $\mu_b$, $\nu_b$ as above; $\lambda_{\mathrm v}$ the
second viscosity; $Re_{\mathrm{bulk}}$ and $P_\nu$ the bulk Reynolds number
and viscous Prandtl number defined below; $\boldsymbol u_{\mathrm c}$,
$\boldsymbol u_{\mathrm s}$ the compressive (curl-free) and solenoidal
(divergence-free) parts of the velocity in a Helmholtz decomposition, and
$E_{\mathrm c}(k)$, $E_{\mathrm s}(k)$ their spectra; $\ell_0$, $t_0$ the
driving scale and the turbulent correlation time $\ell_0/u_{\mathrm{rms}}$ of
a forced box.

## Physical origin

**Monatomic gases** have $\mu_b=0$ (Beattie et al. 2025, §1, citing Tisza
1942). **Polyatomic gases** have a bulk viscosity set by the
relaxation of their rotational and vibrational degrees of freedom: Beattie
et al. (2025, §2.1, Eqs. 12–15, citing the Chapman–Enskog expansion of
Tisza, Cramer and Sharma & Kumar) write it as proportional to
$(\gamma-1)^2$, to the heat capacities of the internal modes, to the
equilibrium pressure and to the relaxation times, valid for sound
frequencies below the inverse relaxation times. Their §1 adds, citing Pan &
Johnsen and Sharma & Kumar, that for diatomic or triatomic gases out of equilibrium it "can vary between tens and
thousands of times larger than the shear viscosity". Their own
order-of-magnitude estimates for the interstellar medium (§2.1, App. B,
Eqs. B1–B2), each from a single rotational transition and Parker's
collision-number model:

| Gas | Temperature | Rotational relaxation time | $\nu_b/\nu$ |
|---|---|---|---|
| H$_2$, shock-heated, $n\approx10^3$ cm$^{-3}$ | $\approx10^3$ K | $\approx2.3\times10^8$ s ($\approx7.4$ yr) | $\approx30$ |
| CO, ambient | $\approx10$ K | $\approx7.1\times10^6$ s ($\approx3$ months) | $\approx1$ |

The H$_2$ relaxation time follows from the printed collision number 174,
viscosity $1.8\times10^{-5}$ Pa s and pressure $1.38\times10^{-11}$ Pa:
$174\times1.8\times10^{-5}/1.38\times10^{-11}=2.3\times10^8$ s *(compiler
check, not in the sources)*. The authors caution that the shock-heated gas
cools quickly.

**Kinetic schemes carry one.** The BGK model behind the
[high-order gas-kinetic scheme](/methods/high-order-gas-kinetic-scheme.md)
has an inherent bulk viscosity $\mu_b=\frac{2K_{\mathrm{int}}}{3(K_{\mathrm{int}}+3)}\mu$
with $K_{\mathrm{int}}$ internal degrees of freedom ($K_{\mathrm{int}}=2$ for a
diatomic gas), as stated, with a citation, by
[Cao et al. (2022)](/sources/cao-2022.md), §3.1, and by
[Zhao et al. (2023a)](/sources/zhao-2023.md), §5.1; for a
diatomic gas $\mu_b=\tfrac4{15}\mu$ *(compiler check, not in the sources)*.
The weakly compressible
[lattice Boltzmann](/methods/lattice-boltzmann-method.md) MHD scheme of
[Foldes et al. (2023)](/sources/foldes-2023.md) likewise carries a bulk
viscosity in its viscous stress, written with the second-viscosity form
(§2.2, Eq. 2.12).

## Bulk viscosity in the dissipation budget

For uniform viscosity in a periodic box, the volume-integrated dissipation of
the Stokes stress splits into an enstrophy part and a dilatational part,
$\int2\mu S^d_{ij}S^d_{ij}\,dV=\int\mu\,\omega_i\omega_i\,dV+\tfrac43\int\mu(\nabla\cdot\boldsymbol u)^2dV$,
and a bulk viscosity adds $\int\mu_b(\nabla\cdot\boldsymbol u)^2dV$ to the
second *(compiler check, not in the sources)*. The sources use both pieces:

- [Cao et al. (2022)](/sources/cao-2022.md), §3.1, and
  [Zhao et al. (2023a)](/sources/zhao-2023.md), §5.1, Eqs. (22)–(23), keep
  the bulk term $\varepsilon_2=\frac{\mu_b}{\rho_0|\Omega|}\int(\nabla\cdot\boldsymbol u)^2dV$
  with the scheme's inherent $\mu_b$ when they estimate numerical
  dissipation as the residual of the kinetic-energy budget; in the nearly
  incompressible [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
  it is negligible (Cao et al. 2022, Fig. 5). See
  [numerical dissipation](/properties/numerical-dissipation.md).
- The dilatational dissipation $\varepsilon_d$ with the factor $\tfrac43\mu$
  used for compressible [isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
  (Cao et al. 2022, §3.4) and for the supersonic Taylor–Green vortex by
  [Chapelier et al. (2024)](/sources/chapelier-2024.md), §II.C, Eq. (11), is
  the dilatational part of the shear-viscous (Stokes) dissipation, not a
  bulk-viscous term.
- [Brillon & Nadarajah (2026)](/sources/brillon-2026.md) (read in arXiv
  v1) state the Stokes hypothesis explicitly, second viscosity coefficient
  $\lambda_{\mathrm v}=-\tfrac23\mu$ (§2.1, Eq. 3), i.e. $\mu_b=0$. Their
  kinetic-energy budget of the compressible
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) therefore has
  only two terms, the pressure dilatation $\langle p\,\nabla\cdot\boldsymbol u\rangle$
  and the viscous dissipation of the deviatoric strain,
  $\tfrac{2}{Re_\infty}\langle\mu S^d_{ij}S^d_{ij}\rangle$ in their
  non-dimensional form (Eq. 37). They obtain an "observed" pressure
  dilatation as the residual of the measured energy decay rate minus the
  viscous term (Eq. 105), which agrees with published DNS, while the
  pressure dilatation computed node by node oscillates spuriously; a
  collocated scheme reduces and Riemann-solver (upwind) dissipation removes
  the oscillations (§3.1.1, §3.1.7, Figs. 3–4, 17–18); see
  [numerical dissipation](/properties/numerical-dissipation.md).
- [Volpiani (2024)](/sources/volpiani-2024.md), §3.2, Eq. (25), writes the
  "theoretical" dissipation rate of the compressible
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) as the sum of
  three volume averages: the deviatoric-strain term
  $\frac{2\mu}{\rho_0|\Omega|}\int S^d_{ij}S^d_{ij}\,dV$, the bulk term
  $\frac{\mu_b}{\rho_0|\Omega|}\int(\nabla\cdot\boldsymbol u)^2dV$ and the
  pressure-dilatation term $-\frac{1}{\rho_0|\Omega|}\int p\,\nabla\cdot\boldsymbol u\,dV$,
  with $\mu_b$ "the bulk viscosity; the viscosities are related via the
  Stokes' hypothesis". The solver's viscous stress is the Stokes form
  $2\mu S_{ij}-\tfrac23\mu S_{kk}\delta_{ij}$ (§2.1, Eq. 2), so in the
  computations the bulk term is zero *(compiler check, not in the
  sources)*; the case is run at $M=0.085$, where the author also uses the
  incompressible enstrophy relation (Eq. 24) as a second estimate. Its
  bulk term has the form of the $\varepsilon_2$ of Cao et al. (2022) and
  Zhao et al. (2023a) above, with the physical rather than a
  scheme-inherent $\mu_b$.

**Damping of compressive modes.** With constant coefficients the viscous force
is $\partial_j\sigma_{ij}/\rho=\nu\nabla^2u_i+(\tfrac13\nu+\nu_b)\partial_i(\nabla\cdot\boldsymbol u)$,
so in Fourier space solenoidal modes decay at the rate $\nu k^2$ and
compressive modes at $(\tfrac43\nu+\nu_b)k^2$ *(compiler check, not in the
sources)*. [Beattie et al. (2025)](/sources/beattie-2025.md) derive the same
decoupling of the two families in the Stokes limit (low Reynolds and Mach
numbers; §6.2, Eqs. 56–57, App. E), with the compressive coefficient printed
as $\nu+\nu_b$ (see Qualifications). The bulk viscosity is therefore the one
molecular coefficient that sets the dissipation scale of the compressive
modes separately from that of the solenoidal ones.

## Explicit bulk viscosity in compressible turbulence

[Beattie et al. (2025)](/sources/beattie-2025.md) (read in arXiv v4) add an
explicit $\nu_b$ to forced, isothermal, visco-resistive MHD at trans-sonic
turbulent Mach number $M_t\approx1$, in a modified FLASH finite-volume code
(second-order MUSCL–Hancock, five-wave approximate Riemann solver) (§4,
App. F).

**Dimensionless numbers** (§2.2, Eqs. 22–30). Non-dimensionalizing the
momentum equation puts $1/Re$ on the deviatoric term and $1/Re_{\mathrm{bulk}}$
on the bulk term, with real-space definitions on the driving scale,

$$Re=\frac{u_{\mathrm{rms}}\ell_0}{\nu},\qquad Re_{\mathrm{bulk}}=\frac{u_{\mathrm{rms}}\ell_0}{\nu_b},\qquad P_\nu=\frac{\nu}{\nu_b}=\frac{Re_{\mathrm{bulk}}}{Re},$$

$P_\nu$ being the authors' **viscous Prandtl number**, ordered by analogy with
$Pm$; $P_\nu=\infty$ is the Stokes hypothesis, and with $Pm=1$ the bulk
magnetic Prandtl number $\nu_b/\eta_m$ equals $P_\nu^{-1}$ (Eqs. 29–30).
Footnote 3 notes that Reynolds numbers built on $2\pi/k_0$ are larger by
$2\pi$.

**Two spectral regimes** (§3.1, Fig. 1, Eqs. 31–32). For $P_\nu<1$ a
*sub-bulk-viscous range* between the bulk and the shear dissipation scales
has $E_{\mathrm s}\gg E_{\mathrm c}$; for $P_\nu>1$ a *sub-shear-viscous
range* has $E_{\mathrm c}\gg E_{\mathrm s}$, and "all" supersonic
simulations without explicit bulk viscosity "ought to be" in it. The sketch
assumes a $k^{-5/3}$ solenoidal and a $k^{-2}$ compressive spectrum.

**Runs** (§4.3, Table 1): $Re=Rm=1000$, $Pm=1$,
$P_\nu\in\{\infty,1,0.1,0.01,0.001\}$ ($Re_{\mathrm{bulk}}=\infty$ to 1),
$128^3$ to $1024^3$ cells, Ornstein–Uhlenbeck forcing at $\ell_0=L/2$ with a
2:1 solenoidal-to-compressive ratio, run to $100t_0$.

**Findings:**

- **Integral quantities are insensitive** until the bulk-viscous decay time
  reaches $t_0$: the saturated magnetic-to-kinetic energy ratio stays
  $\approx0.15$ and the kinematic growth rate of magnetic energy is
  $1.42$–$1.48\,t_0^{-1}$ at $512^3$ for $P_\nu=\infty$, 1 and 0.1, and
  $1.46$ at $P_\nu=0.01$, dropping to $1.28$ only at $P_\nu=0.001$ (§5,
  Table 1). See [small-scale dynamo](/results/small-scale-dynamo.md).
- **Compressive energy fraction.** $\langle E_{\mathrm c}\rangle/\langle E_{\mathrm{kin}}\rangle$
  falls from about $10^{-1}$ ($P_\nu=\infty$) to about $10^{-3}$
  ($P_\nu=0.001$), roughly as $P_\nu$ for $P_\nu<1$ (Eq. 54, Fig. 6).
- **A compressive-mode bottleneck.** For $P_\nu=\infty$ and 1, compressive
  power piles up at high wavenumber, $E_{\mathrm c}/E_{\mathrm s}$ rising from
  about $10^{-1}$ at large scales to about $10^2$ at small scales; for
  $P_\nu\le0.1$ the pile-up "completely disappear[s]" (§6.1–6.2, Fig. 9). See
  [bottleneck effect](/definitions/bottleneck-effect.md).
- **Coupling.** Low $P_\nu$ also suppresses high-wavenumber solenoidal and
  magnetic modes, which the authors attribute not to the viscous operators,
  which decouple the modes, but to a high-wavenumber coupling between them
  (§6.2); the magnetic field becomes larger-scale (§7). See
  [compressible MHD turbulence](/results/compressible-mhd-turbulence.md).

**"DNS" without bulk viscosity.** The authors' methodological claim (§9.1):
without explicit $\nu_b$ the compressive modes have "an unresolved
dissipation scale", "turning what is usually considered a direct numerical
simulation (DNS) into an implicit large eddy simulation for the compressible
modes"; "if one wants to do a compressible DNS where all viscous scales are
resolved, one needs to use both $\nu_{\rm bulk}$ and $\nu_{\rm shear}$, with
$\mathrm P\nu\sim1$, otherwise the grid controls the dissipation of the
compressible modes". Their resolution study (App. D, Figs. D1–D4) supports
it within their set-up: integral statistics converge by $256^3$; $P_\nu=0.1$
is "converged on all scales at $512^3$"; at $P_\nu=1$ the shear dissipation
scale is resolved between $256^3$ and $512^3$ but the bulk one not even at
$1024^3$; at $P_\nu=\infty$ the ratio $E_{\mathrm c}/E_{\mathrm s}$ at high
wavenumber is expected to "grow unbounded" with resolution, "which exactly
what one expects for an ILES". See
[direct numerical simulation](/definitions/direct-numerical-simulation.md)
and [implicit LES](/definitions/implicit-les.md).

**Cost and verification** (App. F). The explicit bulk-viscous flux enters
the momentum flux and, as $\boldsymbol u\cdot\boldsymbol\sigma$, the energy
flux, and adds a diffusive time-step limit
$\Delta t\le\mathrm{CFL}\,\min\big(\tfrac12\Delta x^2/\nu,\ \tfrac12\Delta x^2/\nu_b,\ \tfrac12\Delta x^2/\eta_m\big)$
(Eq. F13); the $P_\nu=0.001$ run was not taken to saturation because of this
cost. Sedov–Taylor blast waves ($288^3$ in 3D, $1024^2$ in 2D) check that the
bulk-viscous damping is isotropic and diffuses $\nabla\cdot\boldsymbol u$,
and space–time spectra follow the damped sound-wave relation
$\omega\approx c_sk-\tfrac i2\nu_bk^2$ (Eqs. F14–F15; $\omega$ page-local
angular frequency, $c_s$ the sound speed).

## Artificial bulk viscosity for shocks

Because it acts only on compression, a bulk-type viscosity is a natural
shock-capturing dissipation (see
[artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)):

- [CharLES](/software/charles.md), in the wall-modelled LES of
  [Griffin et al. (2023)](/sources/griffin-2023.md), §4, adds "an
  artificial bulk viscosity for discontinuities" to its low-dissipation,
  approximately entropy-preserving fluxes.
- In the spectral-difference code SD3DvisP compared by
  [Chapelier et al. (2024)](/sources/chapelier-2024.md), §III.B.e, the
  localized artificial diffusion "acts as a bulk viscosity on the momentum
  equations, and as a thermal diffusivity on the energy equation", with none
  on the mass equation.
- [Cernetic et al. (2024)](/sources/cernetic-2024.md), §3.1, Eq. (15),
  augment their von Neumann–Richtmyer viscous pressure for modal DG with "a
  small additional bulk viscosity contribution" proportional to
  $\rho c_s(h/(N+1))|\nabla\cdot\boldsymbol u|$, which damps post-shock
  oscillations but is "less specific" than the quadratic form and damps
  sound waves if its coefficient is not small; they set it to zero or to
  about a tenth of the quadratic coefficient.

These are numerical devices with coefficients tied to the grid, unlike the
physical $\nu_b$ of Beattie et al., which is constant in space and time.

## Qualifications

- **Printed forms of the stress** (Beattie et al. 2025). Eqs. (11) and (16)
  and App. F use the bulk term $\nu_b(\nabla\cdot\boldsymbol u)\delta_{ij}$,
  while Eq. (47) writes $\boldsymbol\sigma=2\nu_{\rm shear}\mathbb S+\nu_{\rm bulk}\mathbb B$
  with $\mathbb B=\tfrac13(\nabla\cdot\boldsymbol v)\mathbb I$ (Eq. 7), a
  third of that term "using the same definitions as in Section 2.1"; Eq. (23)
  defines $Re_{\mathrm{bulk}}$ with $\mathbb B$ as well. The Stokes-limit
  equation (E1) prints the coefficient of $\nabla(\nabla\cdot\boldsymbol u)$
  as $\tfrac23\nu+\lambda_{\mathrm v}$, i.e. $\nu_b$, and the compressive
  decay coefficient (E5) as $\nu+\nu_b$; for the stress of Eq. (11) the
  coefficient is $\tfrac13\nu+\nu_b$ and the decay coefficient
  $\tfrac43\nu+\nu_b$ *(compiler check, not in the sources)*. Eqs. (56)–(57)
  and (E2) print the dissipative terms with a positive sign. The
  qualitative conclusion, that the viscous operators do not couple the two
  families, is unaffected.
- **Where the two dissipations balance.** Footnote 5 and §6.1 state that the
  bulk and shear dissipation times are equal at $P_\nu\approx1/3$; the paper
  does not derive it. With the decay rates above, the compressive and
  solenoidal rates are never equal for $\nu_b>0$ *(compiler check, not in
  the sources)*.
- **Where the bottleneck disappears.** The abstract says it disappears "for
  $\mathrm P\nu\approx1$", while §6.1 shows it at $P_\nu=1$ and its
  disappearance at $P_\nu\le0.1$, adding that it "ought to be
  $\mathrm P\nu\approx1/3$".
- **Microphysics slip.** App. B prints $\gamma=1-R/c_V$; $\gamma=c_P/c_V$
  with $c_P-c_V=R$ gives $\gamma=1+R/c_V=1.403$ for the printed
  $c_V=2.48R$, against the printed $\gamma\approx1.39$ and
  $(\gamma-1)^2\approx0.15$ instead of 0.162 *(compiler check, not in the
  sources)*. App. F (Eqs. F14–F15) divides $\nu_{\rm bulk}$ by $\rho_0$,
  treating it there as a dynamic coefficient.
- **Scope of the DNS claim.** The evidence is one regime: isothermal,
  forced MHD at $M_t\approx1$, $Re=1000$, a five-wave Riemann solver. In
  Beattie et al.'s terms the inherent $\mu_b=\tfrac4{15}\mu$ of the
  gas-kinetic scheme is $P_\nu=15/4=3.75$, the regime $P_\nu>1$
  *(compiler check, not in the sources)*. The registry's $\sigma_{ij}=2\mu S^d_{ij}$ records the Stokes
  hypothesis that these sources adopt.
- **Inconsistent description in Chapelier et al. (2024).** §III.B.h calls
  the SD3DvisP operator "a Laplacian operator impacting all conservative
  variables", which disagrees with the bulk-viscosity-and-thermal-diffusivity
  description of §III.B.e.

# Citations

- [Beattie et al. (2025)](/sources/beattie-2025.md) — §1; §2.1, Eqs. (11)–(15), footnote 2; §2.2, Eqs. (16)–(30), footnotes 3, 5; §3.1, Eqs. (31)–(32), Fig. 1; §4, Table 1; §5, Eq. (54), Fig. 6; §6.1–6.2, Eqs. (56)–(57), Fig. 9; §7; §9.1; App. B, Eqs. (B1)–(B2); App. D, Figs. D1–D4; App. E; App. F, Eqs. (F1)–(F15), Figs. E1–E2, F1.
- [Cao et al. (2022)](/sources/cao-2022.md) — §3.1, Fig. 5 (inherent bulk viscosity of the BGK scheme, bulk term of the energy budget); §3.4 (dilatational dissipation).
- [Zhao et al. (2023a)](/sources/zhao-2023.md) — §5.1, Eqs. (22)–(23) (bulk term of the energy budget).
- [Foldes et al. (2023)](/sources/foldes-2023.md) — §2.2, Eq. (2.12) (bulk viscosity in the lattice Boltzmann MHD stress).
- [Chapelier et al. (2024)](/sources/chapelier-2024.md) — §II.C, Eq. (11); §III.B.e, §III.B.h (artificial bulk viscosity of SD3DvisP).
- [Cernetic et al. (2024)](/sources/cernetic-2024.md) — §3.1, Eq. (15) (bulk-viscosity contribution to the von Neumann–Richtmyer viscous pressure).
- [Griffin et al. (2023)](/sources/griffin-2023.md) — §4 (artificial bulk viscosity in CharLES).
- [Brillon & Nadarajah (2026)](/sources/brillon-2026.md) — arXiv 2411.12108v1: §2.1, Eq. (3) (Stokes hypothesis); §2.5.1, Eq. (37); §3.1.1, Eq. (105), Figs. 3–4; §3.1.7, Figs. 17–18 (pressure dilatation in the kinetic-energy budget).
- [Volpiani (2024)](/sources/volpiani-2024.md) — §2.1, Eq. (2); §3.2, Eqs. (24)–(25) (bulk term in the compressible dissipation budget of the Taylor–Green vortex, Stokes hypothesis).
