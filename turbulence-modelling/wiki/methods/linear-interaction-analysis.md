---
type: Method
title: "Linear interaction analysis of shock–turbulence interaction"
description: "Linear interaction analysis superposes weak vortical, entropic and acoustic upstream modes, linearizes the Rankine–Hugoniot conditions about a mean normal shock and integrates the post-shock amplitudes over isotropic orientations, giving turbulent-kinetic-energy and Reynolds-stress amplification factors that, for solenoidal isotropic upstream turbulence, depend only on the shock Mach number and the gas."
status: established
aliases: [LIA, linear interaction approximation, Ribner–Moore–Chang theory, Kovasznay decomposition, Kovasznay modes, shock-LIA]
tags: [compressible, hypersonic, dns, les, shock-turbulence-interaction]
timestamp: 2026-10-29T05:11:00Z
---

# Linear interaction analysis of shock–turbulence interaction

Linear interaction analysis (LIA) predicts how a normal shock changes the
turbulence it crosses by treating the upstream turbulence as a
superposition of infinitesimal, statistically independent Fourier waves,
solving the linearized Euler equations behind a shock that each wave
slightly corrugates, and summing the far-field post-shock responses over an
isotropic distribution of wave orientations.
[Cuadra et al. (2025)](/sources/cuadra-2025.md), whose review of the
canonical shock–turbulence interaction is the source of this page, place
the theory in the line of Ribner, Moore and Chang (§I, §II A) and extend
it, in their own earlier work and in new results, to multi-component air
in thermochemical equilibrium at hypersonic Mach numbers (§II B–C). The
output is the amplification factor $\mathrm{AF}_k$ (registry §11) of the
turbulent kinetic energy, and of the streamwise and transverse Reynolds
stresses, as functions of the pre-shock Mach number and the gas. The
configuration and the numerical evidence LIA is compared with are on
[shock-generated turbulence](/results/shock-generated-turbulence.md).

**Page notation** (page-local): $x$ is the shock-normal direction,
subscripts 1 and 2 denote pre- and post-shock states, $M_1=u_1/c_1$ and
$M_2=u_2/c_2$ the Mach numbers relative to the shock, and
$\mathcal R=\rho_2/\rho_1$, $\mathcal P=P_2/P_1$, $\mathcal T=T_2/T_1$ the
mean density, pressure and temperature jumps (the source writes calligraphic
Mach numbers); $\beta_c=c_2/c_1$ is the sound-speed ratio (not the SST
$\beta^*$); $\epsilon_{\mathrm w}\ll1$ the amplitude of one upstream wave,
with $\epsilon_{\mathrm r}$, $\epsilon_{\mathrm e}$, $\epsilon_{\mathrm a}$
its rotational, entropic and acoustic parts (the source's $\varepsilon$,
which is not the dissipation rate); $\theta_k$ the angle of the wavevector
to the shock normal; hats are dimensionless post-shock amplitudes (not the
test filter). $\mathrm{AF}_{11}$ and $\mathrm{AF}_{22}$ are the
amplification factors of $R_{11}$ and $R_{22}$ (the source writes them
$R_{11}$, $R_{22}$ in its figures), $\mathrm{AF}_k$ that of
$k=\tfrac12R_{ii}$.

## Assumptions

- **Kovasznay decomposition.** For small fluctuations ($M_t\ll1$, first
  order), compressible turbulence is a linear superposition of vortical
  (solenoidal), entropic and acoustic modes; any mode hitting a shock
  generates all three downstream, and this linear independence is what LIA
  rests on (Cuadra et al., §I, §II A 1).
- **Weak, inviscid waves.** Each upstream wave has infinite Reynolds number
  and only first-order amplitude; the problem is reduced to two dimensions
  by rotating about the shock normal, the spanwise velocity crossing the
  shock unaltered by conservation of tangential momentum (§II A, Eqs. 7–14).
- **Validity conditions** stated by the authors (§I, p. 4; §II C): upstream
  Mach-number variations small compared with the mean Mach number, and a
  residence time across the shock and its non-equilibrium region small
  compared with the turbulence time scale, i.e. a thermochemical relaxation
  length $\ell_T$ much smaller than the upstream integral scale $\ell$
  (page-local symbols). The LIA cut-off removes the smallest eddies (§I).
  Rapid distortion theory has also been applied to the interaction, under
  "even more restrictive" assumptions (§I).

## The single-wave problem

A vortical wave of amplitude $\epsilon_{\mathrm w}$ and wavevector
$(k\cos\theta_k,k\sin\theta_k,0)$ displaces the shock by $\xi_s(y,t)$
(page-local), small against the transverse wavelength. With the post-shock
fluctuations scaled by $\epsilon_{\mathrm r}$ and the post-shock mean
state (Eqs. 15–16), the linearized Rankine–Hugoniot conditions at the mean
shock are (Eq. 19, dimensionless time $\tau$ and shock displacement
$\hat\xi_s$, page-local):
$$\begin{aligned}
\frac{\partial\hat\xi_s}{\partial\tau}&=\frac{\mathcal R(1-\Gamma_{\mathrm H})}{2M_2(\mathcal R-1)}\hat p_{2s}-\hat u_{1s},&
\hat u_{2s}&=\frac{1+\Gamma_{\mathrm H}}{2M_2}\hat p_{2s}+\hat u_{1s},\\
\hat v_{2s}&=\hat v_{1s}-M_2(\mathcal R-1)\frac{\partial\hat\xi_s}{\partial\hat y},&
\hat\rho_{2s}&=\frac{\Gamma_{\mathrm H}}{M_2^2}\hat p_{2s},
\end{aligned}$$
with subscripts $1s$, $2s$ immediately up- and downstream of the shock and
$\Gamma_{\mathrm H}$ (page-local, the source's $\Gamma$) the normalized
inverse slope of the Hugoniot curve,
$$\Gamma_{\mathrm H}=-\left(\frac{P_2-P_1}{1/\rho_1-1/\rho_2}\right)\frac{\mathrm d(1/\rho_2)}{\mathrm dP_2}=\gamma\frac{M_1^2}{\mathcal R^2}\left(\frac{\partial\mathcal P}{\partial\mathcal R}\right)^{-1}\qquad\text{(Eq. 18)},$$
which equals $M_1^{-2}$ for a calorically perfect ideal gas in equilibrium
(after Eq. 18). The linearized Euler equations behind the shock combine
into a periodic wave equation for the pressure, solved by normal-mode
analysis with the corrugated-shock boundary condition; the post-shock
response consists of a rotational and an acoustic part, oscillating at the
shock frequency $\mathcal RM_2/\tan\theta_k$, whose far-field amplitudes
are taken for $M_2\tau\gg1$ (Eq. 20).

## Amplification of the turbulent kinetic energy

For isotropic upstream turbulence the wave amplitudes follow the energy
spectrum and the orientations are weighted by the solid angle, which
gives the upstream variances $1/3$, $1/6$ and $1/2$ (in units of
$\epsilon_{\mathrm w}^2c_2^2$) for $u$, $v$ and $w$ in the rotated frame
(Eq. 21). The kinetic-energy amplification is then (Eqs. 22–25)
$$\mathrm{AF}_k=\frac{\langle u_2'^2\rangle+\langle v_2'^2\rangle+\langle w_2'^2\rangle}{\langle u_1'^2\rangle+\langle v_1'^2\rangle+\langle w_1'^2\rangle}=\frac12\left[\int_0^{\pi/2}\big(\hat u^2+\hat v^2\big)\sin^3\theta_k\,\mathrm d\theta_k+1\right],$$
split into an acoustic part integrated over the propagating range of the
frequency variable ($\zeta\ge1$, page-local) and a rotational part, each
weighted by the density
$$\mathrm P(\zeta)=\frac32\,\frac{M_2^4\mathcal R^4\sqrt{1-M_2^2}}{\big[M_2^2\mathcal R^2+\zeta^2(1-M_2^2)\big]^{5/2}},\qquad\int_0^\infty\mathrm P(\zeta)\,\mathrm d\zeta=1 .$$
The entropic mode carries no kinetic energy in the inviscid linear limit,
and the acoustic waves with $\zeta<1$ decay exponentially and must be
added in the near field (§II A). For isotropic upstream turbulence, the
authors state, LIA makes $\mathrm{AF}_k$ independent of the shape of
$E(k)$, of $Re_\lambda$ and of $M_t$: the only parameters are $M_1$ and the
gas compressibility through $\gamma$ (§I, p. 4). Two derived ratios follow
(Eqs. 32–33): the turbulence-intensity ratio
$\mathcal I_2/\mathcal I_1=\mathrm{AF}_k^{1/2}\mathcal R$ and the
integral-scale Reynolds-number ratio
$\mathrm{AF}_k^{1/2}\mathcal T^{-0.7}\sqrt{(2\mathcal R^2+1)/3}$
($\mathcal I$ the integral-scale velocity fluctuation over the mean velocity,
page-local); the source does not print the viscosity law behind the
exponent $0.7$.

## Upstream entropic and acoustic content

Cuadra et al. (§II B 2) write the linearized Rankine–Hugoniot conditions
with upstream velocity, density and pressure disturbances (Eq. 28),
introducing two further slope parameters,
$$\Gamma_{\mathrm H}=u_2^2\left.\frac{\partial\rho_2}{\partial P_2}\right|_{P_1,\rho_1},\qquad
\Gamma_\rho=\frac{\Gamma_{\mathrm H}}{u_1^2}\left.\frac{\partial P_2}{\partial\rho_1}\right|_{P_1,\rho_2},\qquad
\Gamma_p=\Gamma_{\mathrm H}\left.\frac{\partial P_2}{\partial P_1}\right|_{\rho_1,\rho_2}\qquad\text{(Eq. 29)},$$
($\Gamma_\rho$, $\Gamma_p$ page-local) with $\Gamma_\rho=-\mathcal R^{-1}$
and $\Gamma_p=\mathcal PM_1^{-2}$ for a calorically perfect gas. In the
post-shock velocity the upstream velocity enters with a prefactor
$1/\beta_c$, which decays like $M_1^{-1}$, the upstream pressure like
$M_1^{-2}$, while the prefactor of the upstream density rises to order
one (Eq. 31, Fig. 4b): as $M_1\to\infty$ only density disturbances,
entropic or acoustic, can still substantially affect the shock (Eq. 28).
Upstream density disturbances are non-negligible when
$$\frac{\delta\rho_1}{\rho_1}\sim\frac{c_1}{c_2}\,\frac{2}{M_2\mathcal R(1+\Gamma_\rho)}\,\frac{\delta u_1}{c_1}\qquad\text{(Eq. 30)};$$
for $\gamma=1.4$ and $M_1=5$ a density disturbance about one order of
magnitude smaller than $\delta u_1/c_1$ already matters, and the threshold
falls with shock strength (Fig. 4b). Density disturbances can also be
introduced by numerical forcing of the upstream turbulence, as the authors
cite Petersen & Livescu (§II B 2).

Two upstream mixtures are parametrized (Eqs. 34–37):

- **vortical–entropic**, by a correlation $\chi_{\mathrm e}$ (page-local,
  the source's $\chi$) between entropic density and rotational velocity
  fluctuations, normalized either directly or with an extra $1/M_1$; the
  authors state that their sign convention is opposite to that of Mahesh et
  al. and Quadros et al. because of a different reference frame (p. 12);
- **vortical–acoustic**, by the upstream dilatational-to-solenoidal
  kinetic-energy ratio $\eta_{\mathrm a}\sim\epsilon_{\mathrm a}^2/\epsilon_{\mathrm r}^2$
  (page-local, the source's $\eta$; not the Kolmogorov length), with
  $$\mathrm{AF}_k=\frac{\mathrm{AF}^{\mathrm r}_k+\eta_{\mathrm a}\mathrm{AF}^{\mathrm a}_k}{1+\eta_{\mathrm a}}\qquad\text{(Eq. 37)}.$$

## Results for air at hypersonic Mach numbers

The authors compute the Rankine–Hugoniot curve and the three slope
parameters of air in thermochemical equilibrium with the Combustion
Toolbox (26 species, NASA nine-coefficient polynomials valid to 20 000 K,
compared with NASA CEA), for $T_1=300$ K, $P_1=1$ atm, $M_1$ from 1 to
about 40–60, against a thermochemically frozen reference (§II B 2–3,
Figs. 3–8):

- equilibrium chemistry gives a much higher compression ratio than frozen
  gas; neglecting ionization lowers the maximum compression ratio from 6
  to 4, and ionization matters for $M_1\ge30$ (Fig. 3);
- for purely vortical upstream turbulence $\mathrm{AF}_k(M_1)$ is
  non-monotonic, with two peaks in the O$_2$ and N$_2$ dissociation ranges;
  the acoustic part is negligible in hypersonic conditions, and the
  amplification is governed by the endothermic rise of the compression
  ratio and by the Hugoniot slope (Fig. 5);
- $\mathcal I_2/\mathcal I_1$ is 1.5 times the frozen value at $M_1=10$ and
  reaches its maximum, about twice the frozen value of about 8, near
  $M_1\simeq26$, at the turning point of the Hugoniot curve
  ($\Gamma_{\mathrm H}=0$, $\mathcal T\simeq42$, $\mathcal R\simeq12$)
  (Fig. 6a);
- small entropic correlations matter: at $M_1=10$ and
  $\chi_{\mathrm e}=-0.5M_1^{-1}=-0.05$, $\mathrm{AF}_k$ is 29% above the
  solenoidal case, while endothermic effects add only 8.6% over the
  calorically perfect approximation (Fig. 7);
- acoustic content can raise or lower the downstream kinetic energy:
  $\mathrm{AF}^{\mathrm a}_k$ crosses unity at $M_1=1.11$ and $2.35$, where
  $\mathrm{AF}_k$ is independent of $\eta_{\mathrm a}$ (from Huete et al.,
  as the authors cite them), and in the hypersonic range the acoustic
  contribution grows as $M_1^2$ (Fig. 8);
- hence compressible upstream fluctuations "cannot be neglected a priori"
  in the hypersonic regime even below 10% compressibility, while
  thermochemistry has only a secondary effect on $\mathrm{AF}_k$ for the
  vortical and vortical–entropic cases (§II B 3c).

**Flight altitude** (§II C, Fig. 9). Over 0–30 km of the International
Standard Atmosphere, endothermic effects raise $\mathrm{AF}_k$ over the
whole Mach range, with stronger peaks at higher altitude. To check the
condition $\ell\gg\ell_T$ the authors compute $\ell_T$ at $M_1=10$ by
one-dimensional DNS with the HTR solver (Park two-temperature model,
five-species air, 1200 points, CFL about 0.1): it grows from about
$10^{-4}$ m at sea level to about $10^{-2}$ m at 30 km, so LIA becomes less
likely to apply with altitude. They cite DNS by Kerkar & Ghosh in which
reactions in the non-equilibrium region amplify mainly the streamwise
velocity, "as opposed to the laterally dominating turbulence predicted by
LIA" (p. 14). A vibrational Damköhler number, the viscous-dissipation
thickness over the vibrational-relaxation thickness, separates the frozen
($\gamma=\gamma(T_1)$), coupled and equilibrium post-shock limits, the
coupled case needing direct numerical solution (§II B 1).

## Against direct numerical simulation

Cuadra et al. compile the DNS of the canonical interaction (Table I;
$M_1\in[1.1,6]$, $M_t\in[0.02,0.691]$, $Re_\lambda\in[9,74]$) and compare
them with LIA (§III B, Figs. 10–12; detail on
[shock-generated turbulence](/results/shock-generated-turbulence.md)):

- for solenoidal upstream turbulence LIA has $\mathrm{AF}_{11}$ dominant up
  to $M_1\sim2$ and $\mathrm{AF}_{22}>\mathrm{AF}_{11}$ above, with the
  transverse amplification peaking near $M_1\sim10$, about 15% above its
  frozen value;
- at $M_1=5$ LIA gives about 42% ($\mathrm{AF}_{11}$) and 16%
  ($\mathrm{AF}_{22}$) more amplification for $\eta_{\mathrm a}=0.05$ and
  about 80% and 31% for $\eta_{\mathrm a}=0.1$, relative to the solenoidal
  $\gamma=1.4$ case;
- **the anisotropy is reversed**: LIA predicts $\mathrm{AF}_{22}>\mathrm{AF}_{11}$
  where DNS gives $\mathrm{AF}_{11}>\mathrm{AF}_{22}$, DNS exceeding LIA in
  $\mathrm{AF}_{11}$ for $M_1\gtrsim2.5$; with endothermic effects LIA
  lowers $\mathrm{AF}_{11}$ and raises $\mathrm{AF}_{22}$ while DNS raises
  both. The authors ascribe this to LIA's idealized conservation of
  tangential velocity across a thin non-equilibrium zone and to acoustic
  energy transfer in the streamwise direction (§III B); LIA, they state
  in §III A 2, fails to capture the post-shock anisotropy, which comes from
  further growth of the streamwise stress by pressure transport;
- the total $\mathrm{AF}_k=(\mathrm{AF}_{11}+2\mathrm{AF}_{22})/3$ from DNS
  is much closer to LIA than the components, and approaches it for
  $M_t\ll1$ and $Re_\lambda\to\infty$ (Fig. 12).

LIA and DNS agree that the post-shock Kolmogorov scale grows for
$M_1<1.65$ and shrinks above (§III A 2). The historical disagreement on
Reynolds-stress amplification is attributed to where the post-shock
values are taken and to viscous decay: DNS values are extrapolated back
to the mean shock position, and as the ratio of laminar shock thickness to
Kolmogorov length goes to zero the DNS amplifications of the Reynolds
stresses and of the vorticity variance converge to LIA (§IV A 4). LIA has
also been used to generate shock-processed inflow states ("shock-LIA") at
higher $Re_\lambda$ than DNS reaches, and to improve RANS models, as the
authors cite (§IV A 4).

## Qualifications

- **Calorically perfect jumps as printed.** Cuadra et al. print
  $\mathcal R=[(\gamma+1)M_1^2+\gamma-1]/[(\gamma-1)M_1^2+2]$ together
  with $\mathcal P=(2\gamma M_1^2-\gamma+1)/(\gamma+1)$ and
  $M_2=M_1/\sqrt{\mathcal R\mathcal P}$ (Eq. 17). The printed $\mathcal R$
  gives $\mathcal R=2\gamma/(\gamma+1)$ at $M_1=1$, where the printed
  $\mathcal P$ gives 1; and with
  $\mathcal R=(\gamma+1)M_1^2/[(\gamma-1)M_1^2+2]$ and the printed
  $\mathcal P$, Eq. (18) yields exactly $\Gamma_{\mathrm H}=M_1^{-2}$, the
  value the authors state after Eqs. (18) and (29), whereas the printed
  numerator does not *(compiler check, not in the sources)*. The
  strong-shock limit $(\gamma+1)/(\gamma-1)$ is the same for both.
- Eq. (5) prints the spectrum tensor as
  $(2\pi)^{-2}\int R_{ij}(\boldsymbol r)e^{-\boldsymbol k\cdot\boldsymbol r}\mathrm d^3r$,
  with no imaginary unit in the exponent.
- The source uses one symbol for two similarity parameters,
  $M_t/[Re_\lambda^{1/2}(M_1-1)]$ (p. 7, after Donzis) and $M_t/(M_1-1)$
  (p. 16, the wrinkled-to-broken criterion); the authors argue that the
  temperature dependence of $\gamma$ prevents reducing the hypersonic
  problem to the first alone (p. 7).
- The turbulent Mach number is $M_t=\sqrt{R_{kk}}/\tilde c=\sqrt3\,u_{\mathrm{rms}}/\tilde c$
  on the Favre-averaged sound speed (Eq. 1); LIA uses Reynolds averages and
  the compiled DNS Favre averages (§III B).
- All new results are linear-theory computations by the authors' own
  framework. The limit of the theory is also stated by
  [Davidovits et al. (2022)](/sources/davidovits-2022.md), §I: most
  theories of shock–turbulence interaction hold formally only for small
  upstream perturbations and a single passage of material through the
  shock, which their order-one density fluctuations violate (the shock
  front breaks into several fronts; see
  [shock-generated turbulence](/results/shock-generated-turbulence.md)).

# Citations

- [Cuadra et al. (2025)](/sources/cuadra-2025.md) — §I, Eqs. (1)–(6); §II A, Eqs. (7)–(25), Fig. 2; §II B 1–3, Eqs. (26)–(37), Figs. 3–8; §II C, Fig. 9; §III A 2; §III B, Table I, Figs. 10–12; §IV A 4.
- [Davidovits et al. (2022)](/sources/davidovits-2022.md) — §I (small-perturbation, single-passage assumptions of linear theories; passing mention).
