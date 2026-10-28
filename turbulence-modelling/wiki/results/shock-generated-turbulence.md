---
type: Result
title: "Shock-generated turbulence and turbulent shock jump relations"
description: "A strong shock crossing a medium with order-one density fluctuations generates turbulence whose velocity dispersion scales with shock speed times a pre-shock Atwood number and whose Reynolds stress lowers post-shock pressure and density; conversely, shocks form inside supersonic turbulence and the supersonic Taylor–Green vortex, where they test shock capturing."
status: established
aliases: [shock–inhomogeneity interaction, shock through a non-uniform medium, turbulent Rankine–Hugoniot relations, turbulent jump conditions, shock-driven turbulence, shocklets, shock networks, shock–turbulence interaction, supersonic isothermal turbulence, sonic scale, detonation–turbulence interaction]
tags: [compressible, implicit-les, plasma, astrophysics, dg, numerical-dissipation, combustion]
timestamp: 2026-10-28T02:16:00Z
---

# Shock-generated turbulence and turbulent shock jump relations

When a strong planar shock propagates into a medium whose density varies in
space, the post-shock flow becomes turbulent, a process the source below
scales with linear Richtmyer–Meshkov theory. That source cites the
theory of
shock–turbulence and shock–inhomogeneity interaction (linear interaction
analysis, rapid distortion) as mostly assuming small upstream perturbations and a
single passage of the fluid through one shock front.
[Davidovits et al. (2022)](/sources/davidovits-2022.md) study the regime the
theory excludes: density fluctuations of order one, which break the front
into several shocks. They give scaling laws for the generated velocity
dispersion and turbulent Mach number, and Favre-averaged jump relations in
which the post-shock Reynolds stress lowers the mean post-shock pressure and
density. The application is the controlled generation of compressible
turbulence in laser-driven high-energy-density shock tubes; the paper is
peripheral to closure modelling, and its "model" content is the scaling and
jump relations. The converse process, shocks formed by the turbulence itself,
is the subject of the last section: driven supersonic turbulence and the
supersonic [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md), used
by three further sources as tests of shock-capturing discretizations. A
detonation running into isotropic turbulence and a boundary layer
amplified through a ramp interaction are added there as reacting and
wall-bounded counterparts.

**Page notation** (page-local unless in the registry): $x$ is the
shock-normal direction (the shock moves toward $-x$), $y$, $z$ the
transverse directions over which flow statistics are homogeneous;
$\langle\cdot\rangle$ is the volume-weighted average over a thin transverse
slab and $\langle\cdot\rangle_\rho$ the Favre average; subscripts 0 and 1
denote pre- and post-shock states and $[\![f]\!]=f_1-f_0$ the jump;
$U_s$ is the mean shock speed, $M_s=U_s/c_0$ the shock Mach number on the
pre-shock sound speed $c_0$, and $\mathcal M_s$ the shock speed over the mean
post-shock sound speed $c_1$; $\sigma_\rho/\langle\rho\rangle$ is the pre-shock
standard deviation of density over its mean; $\sigma_v$ is the total
velocity dispersion, $\sigma_v^2=\sum_i\langle u_i'^2\rangle$; $r_v$ is the
radius of the low-density voids that make up the pre-shock medium (in
micrometres); $n_d$ the number of space dimensions (not the registry's wall distance $d$). The Reynolds stress is the
kinematic Favre stress $R_{ij}=\langle\rho u_i''u_j''\rangle/\langle\rho\rangle$
(positive trace, the registry's Favre form divided by the mean density),
$R_{ii}$ its trace, and $\Theta=R_{xx}/R_{yy}$ its anisotropy (axisymmetric,
$R_{yy}=R_{zz}$). Quantities "in the analysis region" are averaged a second
time, with the same weighting, over a window behind the shock.

## Set-up

[Davidovits et al. (2022)](/sources/davidovits-2022.md), §II, Fig. 1,
App. A–B, simulate an idealized indirect-drive shock tube with the
arbitrary-Lagrangian–Eulerian radiation-hydrodynamics code HYDRA. Radiation
launches the shock through an ablator and a dense pusher and is switched off
once the shock is in the working material, an ideal monatomic gas
($\gamma=5/3$) of mean density about 0.05 g/cm³ with no viscosity or
thermal conduction and artificial viscosity at shocks. The pre-shock medium
is a uniform background with circular (2D) or spherical (3D) voids on a
randomly perturbed close-packed lattice, and in the highest-variance cases
dense beads between them. The 2D suite spans

- $M_s\sim12$, 15, 18, 20, 37 (pre-shock sound speed about 2.4 km/s);
- $\sigma_\rho/\langle\rho\rangle\sim0.38$, 1.05, 1.9;
- $r_v\approx23$, 45, 90 µm,

on grids of about $846\times512$ or $1694\times1024$ cells over
$3.8\times2.048$ mm; six 3D runs at $M_s=18$ and 37, $r_v=90$ and 120 µm,
use up to about $657\times400\times400$ cells. The shock decays as it
travels about 2.5 mm, much more than the void size, and statistics are taken
in a 0.2 mm window about 0.1 mm behind the end of the shock transition.
Doubling the resolution in each direction changes the analysis-region
averages by 0.6% to 2.9% for one representative case (§II A).

The authors state that the runs "should not be regarded as direct numerical
simulation", being "in the spirit of
[implicit large eddy simulations](/definitions/implicit-les.md)", and they
analyse only large-scale averages, which they expect to be least influenced
by [numerical dissipation](/properties/numerical-dissipation.md) (§II A).

## Velocity dispersion: a Richtmyer–Meshkov scaling

[Davidovits et al. (2022)](/sources/davidovits-2022.md), §III, cite
earlier work on young supernova remnants (Inoue et al.) that found the
post-shock velocity dispersion "reasonably predicted by the result of linear
analysis of the Richtmyer-Meshkov instability". Adapting that result to a
continuous density field, the authors (§III, Fig. 4) define a pre-shock
average Atwood number
$$A_\sigma=\frac{\sigma_\rho/\langle\rho\rangle}{1+\sigma_\rho/\langle\rho\rangle}$$
(registry §11; it is not the two-fluid Atwood number of
[Rayleigh–Taylor mixing](/benchmarks/rayleigh-taylor-mixing.md)) and find
$\sigma_v\propto A_\sigma U_s$. The void size also matters. By a dimensional argument
(energy injection $dE/dt\sim v^3/l$ at a comparable rate, forcing scale
$l\propto r_v$) they hypothesize $\sigma_v\propto r_v^{1/3}$ and fit, in the
analysis region of the 2D runs,
$$\sigma_v=0.52\left(\frac{r_v}{45}\right)^{1/3}A_\sigma U_s \qquad\text{(Eq. 2)},$$
the coefficient 0.52 "chosen to approximately fit the data" and dependent on
set-up choices such as the window position. The 3D runs follow the same
scalings with a coefficient of about 0.6, which the authors cannot firmly
attribute to geometry rather than statistical variation; Inoue et al., with
an isotropic $k^{-5/3}$ density spectrum peaked at the box size, found a
coefficient of 1 (§III, §IV). The shock speed for a given drive is
relatively insensitive to $r_v$, and the scatter grows with $r_v$ because
fewer voids fall in the averaging window (§III). The post-shock velocity
fluctuation magnitude in a 3D run has a probability distribution close to
the Maxwell–Boltzmann form $P(v')\propto v'^2\exp(-3v'^2/2\sigma_v^2)$, the
distribution the authors recall from Federrath for fully developed turbulence
even at high Mach number, and the transverse velocity spectra peak at the
mode number of the void diameter (Fig. 3).

## Saturation of the turbulent Mach number

With the turbulent Mach number defined as $M_t=\sigma_v/c_1$, the velocity
dispersion over the mean post-shock sound speed (volume-weighted, which
equals the mean local Mach number only for isothermal fluctuations), the same
fit gives
$$M_t=0.52\left(\frac{r_v}{45}\right)^{1/3}A_\sigma\,\mathcal M_s\qquad\text{(Eq. 3)}.$$
For an unperturbed normal shock the Rankine–Hugoniot relations, which
the authors cite, give
$$\mathcal M_s=\frac{(\gamma+1)M_s^2}{\sqrt{(2\gamma M_s^2-\gamma+1)\big((\gamma-1)M_s^2+2\big)}}\;\xrightarrow{M_s\to\infty}\;\frac{\gamma+1}{\sqrt{2\gamma(\gamma-1)}},$$
which is $4/\sqrt5\approx1.79$ for $\gamma=5/3$. A stronger drive therefore
raises $\sigma_v$ but hardly $M_t$: "a rapidly diminishing return to driving
with higher-Mach shocks" for the turbulent Mach number. The constraint relaxes
as $\gamma\to1$, and simulations with a tabular carbon equation of state,
whose compression exceeds the $\gamma=5/3$ limit of 4, suggest a lower
effective $\gamma$ once the material ionizes (§III, §IV, Fig. 5).

## Favre-averaged jump relations with Reynolds stress

Following the turbulent jump conditions of Lele and the post-shock
definitions of Larsson et al., which
[Davidovits et al. (2022)](/sources/davidovits-2022.md), §III, cite, the broken-up
transition is treated as one average normal shock, steady in its own frame.
With no pre-shock turbulence, the triple correlation and the
temperature–velocity correlation dropped, and $u$ the shock-normal velocity,
$$\begin{aligned}
[\![\langle\rho\rangle\langle u\rangle_\rho]\!]&=0,\\
[\![\langle\rho\rangle\langle u\rangle_\rho^2+\langle p\rangle+\langle\rho\rangle R_{xx}]\!]&=0,\\
\Big[\!\Big[\tfrac12\langle\rho\rangle\langle u\rangle_\rho^3+\tfrac{\gamma}{\gamma-1}\langle p\rangle\langle u\rangle_\rho+\langle\rho\rangle\langle u\rangle_\rho\big(R_{xx}+\tfrac12R_{ii}\big)\Big]\!\Big]&\approx0,
\end{aligned}$$
with $R_{ii}=R_{xx}\big(1+(n_d-1)/\Theta\big)$ (Eqs. 5–7). Neglecting the
pre-shock pressure, taking the post-shock $R_{xx}$ and $\Theta$ as given and
expanding to first order in $R_{xx}/U_s^2$, the post-shock density and
pressure relative to the unperturbed shock (subscript $1,0$) are
$$\begin{aligned}
\frac{\langle\rho\rangle_1}{\langle\rho\rangle_{1,0}}&\approx1-\frac{2\Theta(3-\gamma)-2(n_d-1)(\gamma-1)}{4\Theta}\,\frac{\gamma+1}{\gamma-1}\,\frac{R_{xx}}{U_s^2},\\
\frac{\langle p\rangle_1}{\langle p\rangle_{1,0}}&\approx1+\frac{(n_d-1)(\gamma-1)^2+\Theta(1-6\gamma+\gamma^2)}{4\Theta}\,\frac{\gamma+1}{\gamma-1}\,\frac{R_{xx}}{U_s^2},
\end{aligned}$$
(Eqs. 8–9), which for $\gamma=5/3$ become
$$\frac{\langle\rho\rangle_1}{\langle\rho\rangle_{1,0}}\approx1-\frac83\Big(1-\frac{n_d-1}{2\Theta}\Big)\frac{R_{xx}}{U_s^2},\qquad
\frac{\langle p\rangle_1}{\langle p\rangle_{1,0}}\approx1-\frac89\Big(7-\frac{n_d-1}{2\Theta}\Big)\frac{R_{xx}}{U_s^2}$$
(Eqs. 10–11). Solving the three jump conditions above to first order
reproduces Eqs. (8)–(9), and Eqs. (10)–(11) follow from them at
$\gamma=5/3$ *(compiler check, not in the sources)*.

**What the simulations show.** The pressure relation is relatively
insensitive to the anisotropy (for $\Theta\gtrsim1$) and to the
dimensionality, the density relation more sensitive; the simulated
post-shock pressures collapse on one line even ignoring $n_d$ and $\Theta$,
agree "fair[ly]" with Eq. (11) plotted for $n_d=3$, $\Theta=1$, and fall to
less than half the unperturbed value at the largest $R_{xx}/U_s^2$ (§III,
Figs. 7–8). The unperturbed runs have analysis-region density jumps of about
3.3 to 3.8, below the strong-shock limit 4 (Fig. 8). The mean post-shock
temperature clusters by drive strength and shows no discernible dependence
on the turbulence intensity (Fig. 6). The anisotropy grows with
$R_{xx}/U_s^2$, with trend lines $\Theta\sim1+13(R_{xx}/U_s^2-1/40)$ in 2D
and $\Theta\sim1+26R_{xx}/U_s^2$ in 3D; the factor two between the slopes
follows from $R_{ii}=R_{xx}(1+(n_d-1)/\Theta)$ if the trace is the same in 2D
and 3D (Fig. 9). The fit of Eq. (2) also describes the density-weighted
dispersion $\sqrt{R_{ii}}$, so that, with a model for $\Theta$, the jump
relations can be closed from pre-shock quantities alone (§III). Moving the
window downstream lowers the anisotropy toward isotropy, as in wind-tunnel
shock–turbulence experiments (not shown).

## The converse: shocks formed inside compressible turbulence

When the turbulence itself is supersonic, or becomes so locally, it builds
its own shocks; nothing is imposed from outside. Three sources of the bundle
use such flows to test discretizations, one more offers decaying data and
another uses decaying data as an implicit-LES test, and a shock train in a
channel and a compression/expansion ramp give wall-bounded counterparts
with imposed shocks.
Page-local symbols here: $l_s$ and $L_{\mathrm{inj}}$ the sonic and injection
scales, $v(l)$ the velocity increment at separation $l$ from the
second-order structure function; $\varepsilon_s$ and $\varepsilon_d$
(registry §11) the solenoidal (enstrophy) and dilatational dissipation of
the Stokes stress.

**Driven supersonic isothermal turbulence.**
[Cernetic et al. (2024)](/sources/cernetic-2024.md) (read in arXiv v2) drive
isothermal turbulence (solenoidal Ornstein–Uhlenbeck forcing at half the box)
at rms Mach numbers 0.1 to 12.8, doubling each step, in which the flow is "a
network of interacting shocks", with a GPU modal discontinuous Galerkin code
(Legendre basis of total degree $N$, HLLC flux; not the nodal
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md)) and a
second-order finite-volume baseline, with no explicit viscosity or subgrid
model (§4–§6, Table 1):

- **Cascade transition.** All schemes reproduce the change from
  $E(k)\propto k^{-5/3}$ (subsonic) to $k^{-2}$ (supersonic); at $256^3$ the
  structure-function slopes of $v(l)$ fitted over $0.1<l<0.25$ are 0.32 for
  the most subsonic and 0.47 for the most supersonic run, against expected
  $1/3$ and $1/2$ (§5, Figs. 5–6). Density PDFs are close to log-normal,
  widen strongly with Mach number and are nearly identical for all schemes
  at $256^3$ (Fig. 7).
- **The sonic scale.** With $v(l)\propto l^{1/2}$ from injection, the scale
  where the increment equals the sound speed is $l_s=L_{\mathrm{inj}}/M^2$
  (Eq. 22), about ten times below injection at Mach 3.2. At $1024^3$ and
  Mach 3.2, DG with $N=1$ (second order) shows $v(l)\propto l^{0.49}$ down
  to a sudden change to $l^{0.43}$, identified as the sonic point, and a
  spectrum going from $k^{-2}$ towards $k^{-5/3}$ with the intersection of the
  two fits "reasonably close" to it; the finite-volume run at $1024^3$
  washes it out, DG at $512^3$ "does nearly as well as" finite volumes at
  $1024^3$, and finite volumes at $512^3$ show no sonic point (§6,
  Figs. 8, 10–11).
- **High order and shocks.** DG extends the resolved spectral range in the
  subsonic runs, but in the supersonic ones the gain "nearly disappears"
  (§5). A cost model (cost $\propto N_x^4N^8$ to a fixed time in 3D, with
  $N_x$ cells per direction) and an error model for a planar shock lead the
  authors to a "sweet spot" of second- or third-order DG ($N=1$ or 2) once
  many shocks are present (§7, Eqs. 33–35; Conclusions). Stability at
  Mach 12.8 needs a von Neumann–Richtmyer viscous pressure applied only at
  interior quadrature points and a projection of primitive variables
  before extrapolation to faces (§3); the total dissipation at a shock is
  "fixed by the conservation laws", the viscosity coefficient only setting
  its sharpness and post-shock oscillations (§3.1). See
  [artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)
  and [homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md).

**The supersonic Taylor–Green vortex.**
[Chapelier et al. (2024)](/sources/chapelier-2024.md) (HAL accepted
manuscript) compare seven high-order codes on the Taylor–Green vortex at
$Re=1600$ and reference Mach number 1.25, which develops "transition,
decaying turbulence, strong shocks and shock–turbulence interaction" from a
smooth analytic initial field (§I). The closest physical flow, they state,
is compressible isotropic turbulence with shocklets (§I). On the reference
sixth-order TENO runs from $64^3$ to $2048^3$ (§II.C, Figs. 2–4):

- the kinetic energy converges by $128^3$, $\varepsilon_s$ needs $512^3$;
- $\varepsilon_d$ has two peaks, the first linked to shocks with little
  vortex interaction, the second to the onset of shock–turbulence
  interaction; the first is **not mesh-converged even at $2048^3$**, because
  the shocks keep sharpening until molecular viscosity smooths them, while
  the second converges faster;
- the $2048^3$ run cost about 1.96 million core hours (57,600 cores, 34 h).

Across codes (§IV, Figs. 5–8): artificial-diffusion schemes give smooth but
thick shocks and the lowest $\varepsilon_d$; local switching to lower-order
schemes gives sharp shocks that oscillate on coarse grids, except TENO,
sharp and oscillation-free at all resolutions; filtering without shock
capturing gives the largest oscillations. The authors conclude that shock
capturing has "a low impact" on the turbulent scales overall (§V), while
noting that the "strong shock capturing strategy" of the spectral-difference
code SD3D "is probably hindering" small-scale development on finer grids
(§IV.A). See [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md),
[subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md)
and [WENO schemes](/methods/weno-scheme.md).

[Kurz et al. (2025)](/sources/kurz-2025.md) (read in arXiv v2) use the same
case to validate the GPU code [GALÆXI](/software/galaexi.md): with DG/finite-volume
subcell blending at the same maximum blending factor on all grids and $N=7$,
GALÆXI and [FLEXI](/software/flexi.md) give identical $\varepsilon_s(t)$,
"almost identical" to the Chapelier et al. reference at $512^3$ degrees of
freedom (§5.2, Fig. 11).

**Shocklets in decaying compressible turbulence.** In decaying isotropic
turbulence at turbulent Mach numbers 0.8 to 1.6,
[Cao et al. (2022)](/sources/cao-2022.md), §3.4, Fig. 15, find shocklets
(dilatation below $-3$ times its rms) as long narrow ribbons next to
block-like expansion regions (detail on
[homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)).
[Deng et al. (2022)](/sources/deng-2022.md), §4.15, run the decaying
case "with eddy shocklets" of Johnsen et al. only as an implicit-LES test
of the velocity spectrum, with no shocklet statistics (recorded on
[homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md));
their shock tests are inviscid.

**Turbulence amplified through a shock train.** A wall-bounded counterpart,
with the shocks imposed by back pressure rather than formed by the
turbulence, is the shock train that
[Kumar & Ghosh (2022)](/sources/kumar-2022-b.md), §3.2.3, compute in a
plane isolator channel ($4\pi h\times2h\times4\pi h/3$, $h$ the half-width,
$192\times128\times151$ points, isothermal walls) fed by a concurrently
run periodic channel at centreline Mach 1.5 and $Re_\tau=247$, with an
outlet pressure nearly twice the inlet pressure, using a three-point
bandwidth-optimized [WENO scheme](/methods/weno-scheme.md) with a relative
total-variation limiter and no model. The shock train extends to
$x/L_x=0.3$ ($L_x$ the channel length) and its shocks are not always
symmetric about the centreline. Along the centreline the streamwise
Reynolds stress, normalized by the inlet wall shear stress, jumps in the
compression regions and drops in the expansions, grows gradually in the
mixing region up to $x/L_x=0.78$ and then declines, staying above its
inlet value at the outlet; the other normal stresses follow with smaller
magnitudes (Fig. 36). Near the shocks the boundary layers thicken and
separate, and near-wall sweep–ejection activity intensifies (Figs. 30–32).
The evidence is qualitative: there is no reference data for the shock
train beyond a qualitative match of centreline density and pressure with
an earlier pipe-flow LES that the authors cite, and the paper reports
neither the wall-unit resolution nor the averaging time. The
"one-dimensional shock–turbulence interaction" of the same paper is the
inviscid Shu–Osher shock/entropy-wave problem, not turbulence (§3.1). See
also [shock/turbulent boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
and [turbulent channel flow](/benchmarks/turbulent-channel-flow.md).

**Turbulence through the shocks of a compression/expansion ramp.**
[Tonicello et al. (2022)](/sources/tonicello-2022.md) run a DNS of a Mach
2.91 boundary layer ($Re_\theta=2900$) over a 24° compression ramp
followed by an expansion corner, in a spectral-difference code at $N=5$
with an artificial bulk viscosity that regularizes the shocks, which stay
under-resolved: the authors restrict the term DNS to the scales of the
turbulence (§2.2; see
[bulk viscosity](/definitions/bulk-viscosity.md) and
[shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)).
Downstream of the interaction the spectra keep an inertial range that is
longer than upstream, with no energy accumulation near the grid Nyquist
wavenumber (§3.2, Figs. 7–8). Conditioned on a local Mach number above
one, the density PDF downstream extends to larger values while the
pressure PDFs are insensitive to the sonic condition, which the authors
attribute partly to shocklets (§3.2, Fig. 11). Their a priori analysis of
the subgrid energy transfer finds compression associated with forward
transfer and expansion with backscatter, also in the mean near the
expansion corner (§4, Figs. 14, 23–24; detail on
[energy backscatter](/definitions/energy-backscatter.md) and
[pressure dilatation](/definitions/pressure-dilatation.md)). The subgrid
Mach number $M_{\mathrm{sgs}}=\sqrt{2\bar\rho k_{\mathrm{sgs}}/(3\gamma\bar p)}$
(page-local, Eq. 4.14) reaches about 0.32 in the Favre mean and about 0.42
in the fields filtered at $4h$ and $8h$ ($h$ the DNS resolution), above
the value of about 0.3 beyond which they expect non-negligible
compressibility; larger $M_{\mathrm{sgs}}$ goes with stronger forward
transfer in the mean and with both directions in the filtered fields
(§4.2, Figs. 20–22, 25–26).

**Implicit LES for shock–turbulence problems.**
[Cheng et al. (2023)](/sources/cheng-2023-b.md), §1, argue, citing Garnier
et al., that explicit subgrid models are "not suited to shock-vortex and
shock-turbulence problems", because they cannot represent the energy
exchange among the acoustic, entropy and vorticity modes and usually fail
to capture the conversion of kinetic into internal energy across shocks,
and they leave the subgrid scales to the numerical dissipation of a
shock-capturing scheme (see [implicit LES](/definitions/implicit-les.md)).
Their tests of the shock–vortex coupling are inviscid: a vortex
($M_v=0.9$, page-local vortex Mach number) crossing a standing Mach 1.5
shock splits into two parts, which their low-dissipation ROUND
reconstructions resolve better than the van Leer and MUSCL limiters, and a
shock crossing an oblique entropy wave, whose high-frequency post-shock
waves the limiters damp (§3.3–3.4, Figs. 4–5); their one turbulent
validation is a transonic deep cavity without a shock–turbulence
interaction (§3.6). See [numerical dissipation](/properties/numerical-dissipation.md).

**A reacting shock meeting isotropic turbulence.**
[Iwata et al. (2023)](/sources/iwata-2023.md) run a DNS of a cellular
detonation propagating into isotropic turbulence, with a 19-step hydrogen
mechanism, in two stoichiometric hydrogen–oxygen–argon mixtures of the
same cell width (1.92 mm) but different cell regularity (§II). The
inflow turbulence comes from a decaying
[isotropic-turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
precursor at $Re_\lambda=240$ and turbulent Mach number 0.30, fed in
around the detonation speed in a detonation-fixed frame; the code uses
fifth-order WENO, HLLC switched to Lax–Friedrichs near shocks by a
pressure sensor, and a 4 µm grid of $1200\times480\times480$ cells, with
$k_{\max}\eta=2.31$ and 4.25 for the two mixtures ($k_{\max}$ page-local,
the largest resolved wavenumber) (§II B–C, Table I). Findings on the
shock–turbulence side (§IV A–C):

- behind the shock the Taylor microscales are about 25 µm along the
  propagation direction and 50 µm across it in all cases, an anisotropy
  the authors attribute to shock compression, as in inert
  shock–turbulence interaction (Fig. 9);
- the post-shock turbulent velocity scale, about 480 and 670 m/s for the
  two mixtures, is comparable to the post-shock mean velocity and comes
  mainly from the detonation itself (slip lines behind the triple points):
  the contribution of the incoming turbulence is "quite minor" (Fig. 10);
- turbulent fluxes of hydrogen and enthalpy along the propagation
  direction exceed molecular transport by two orders of magnitude or more
  (Figs. 11–12);
- the incoming turbulence broadens the distribution of the local shock
  Mach number; in the less diluted, irregular mixture this raises the
  share of high post-shock temperatures and shortens the mean induction
  length from 0.321 to 0.295 mm, which ZND solutions started from the DNS
  post-shock states reproduce qualitatively; the authors name "creation of
  different shock strength" the main effect of turbulence and expect the
  turbulent Mach number to be an important indicator (Figs. 14–15, §V).

The mean detonation speed stays at 0.98 and 0.95 of the Chapman–Jouguet
value with or without turbulence (§III C, Table I). The reaction proceeds
faster with turbulence in the irregular mixture and unchanged in the
regular one, against the delay that Jin et al. found with one-step
chemistry, as Iwata et al. cite them (§III D). The detonation-structure
results are on the Source page.

**Amplification over a compression ramp.** In the wall-bounded
interaction of a Mach 2.9 boundary layer with a 24° ramp,
[Shi & Yan (2023)](/sources/shi-2023.md) find the turbulent kinetic
energy amplified 3.34 times and the spanwise normal stress 4.23 times,
the streamwise stress peaking upstream of the others, and attribute the
amplification near separation to deceleration by the separation shock
rather than to shear (§IV.C, Table IV); detail on
[shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md).

**Not this mechanism: turbulence behind a perforated plate.** In the
shock tube of [Chambers et al. (2022)](/sources/chambers-2022.md) a leading
shock of Mach 2 to 3 passes through a perforated plate, and the choked jets
it forms generate nominally isotropic turbulence ahead of an accelerating
hydrogen–air flame (§II A–B); the turbulence comes from the post-shock
jets, not from the shock–inhomogeneity interaction of the first sections.
The flow measurements and the combustion results are on the Source page.

Unlike the shock-tube runs of the first sections, none of the turbulence-generated
flows has a single mean shock, so the Favre-averaged jump relations do not apply to them; their
shocks are the dissipative structures of the turbulence, and the sources
judge discretizations by how they resolve or smear them.

## Qualifications

- The $r_v^{1/3}$ dependence is the authors' dimensional hypothesis, fitted
  over voids of 23 to 120 µm; they note that "it is possible there is some
  alternate explanation", that the coefficient $0.52(r_v/45)^{1/3}$ must have
  a maximum by momentum and energy conservation, and that the scaling must
  saturate at or before the domain size (§III, §IV). The original linear
  Richtmyer–Meshkov result fits better with a post-shock Atwood number; the
  pre-shock $A_\sigma$ is chosen for prediction (§IV).
- All evidence is numerical: fits to one simulation suite without DNS or
  experimental reference, with comparison only against the unperturbed runs.
  The same paper estimates that equipartition would give post-shock magnetic
  fields of about 10 to 100 T, without claiming such fields would be present
  (§IV).
- [Davidovits et al. (2022)](/sources/davidovits-2022.md) were read in arXiv
  v1. The Fig. 6 caption lists drive strengths $M_s\sim14$, 16, 20, 22, 37
  and 3D runs at $M_s\sim20$ and 37, while Table I and §II A give 12, 15,
  18, 20, 37 and the 3D runs at 18 and 37. Table I lists a 3D case with
  $\sigma_\rho/\langle\rho\rangle=1.07$ that App. A describes as about 1.03,
  and the main 3D cases as 0.9 against about 0.87 in App. A (labelled
  approximate). The abstract calls $\sigma_\rho/\langle\rho\rangle$ a
  "normalized variance" although it is a normalized standard deviation, and
  §II B calls the transverse directions "shock-normal".
- The turbulent Mach number here is the volume-weighted dispersion over the
  mean post-shock sound speed, which the authors note equals the mean local
  Mach number only for isothermal fluctuations (§III). Other sources define
  it differently, e.g. $M_t=\sqrt3\,u_{\mathrm{rms}}/c_0$ on the initial
  sound speed in the compressible decaying runs of
  [Cao et al. (2022)](/sources/cao-2022.md) (Notation map) on
  [homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md);
  values from the two definitions are not compared by any source.
  [Iwata et al. (2023)](/sources/iwata-2023.md) give their inflow
  turbulence a turbulent Mach number of 0.30 without printing its
  definition (Table I).
- [Iwata et al. (2023)](/sources/iwata-2023.md) print a ZND induction
  length of 124 µm (§IV A) and mean DNS induction lengths of 0.321 and
  0.295 mm, the DNS one measured from the shock to the half-reacted
  hydrogen iso-surface (§IV C); the two are defined differently and the
  paper does not compare them. They state the resolution of the incoming
  turbulence by the $k_{\max}\eta$ criterion and of the reaction zone by
  the half-reaction length, "resolved by 30 grids" (§II C); the shocks are
  captured by the WENO scheme.

- **Printed slips in the shock-network sources.** Cernetic et al. (2024)
  state that doubling the Mach number needs a tripled driving strength
  $E_{\mathrm{inj}}$, while their Eq. (32), $M\propto E_{\mathrm{inj}}^{1/3}$,
  gives a factor $2^3=8$ *(compiler check, not in the sources)*; their
  Eq. (35) prints a coefficient 315 where the printed ingredients of the
  cost model (their Eq. 33, which they reproduce exactly, and the first line
  of Eq. 35) give 351 *(compiler check, not in the sources)*; the leading
  order $N_x^4N^8$ is unaffected.
  Chapelier et al. (2024) print the equation of state without $\rho$ in the
  kinetic term and $Re=\rho_0U_0/\mu_0$ without a length (§II.A–B); the
  Fig. 8 legend names a "TENO6 512" reference where the text uses the
  $2048^3$ run.
- Kumar & Ghosh (2022) give the periodic channel as centreline Mach
  1.49 and $Re_\tau=240$ (Table 4, §3.2.2) and the inflow channel of the
  shock train, on the same domain and grid, as Mach 1.5 and
  $Re_\tau=247$ (§3.2.3), without saying whether these are the same run.

# Citations

- [Davidovits et al. (2022)](/sources/davidovits-2022.md) — §I; §II A–B, Eq. (1), Table I, Fig. 1; §III, Eqs. (2)–(11), Figs. 3–9; §IV; App. A–B.
- [Cernetic et al. (2024)](/sources/cernetic-2024.md) — §3.1, Eqs. (14)–(16); §3.2; §4.1–4.2, Eqs. (22), (26)–(32); §5, Figs. 5–7; §6, Figs. 8, 10–11; §7, Eqs. (33)–(35); Conclusions (shock networks in driven supersonic isothermal turbulence, sonic scale, DG against finite volumes).
- [Chapelier et al. (2024)](/sources/chapelier-2024.md) — §I; §II.A–C, Eqs. (5)–(11), Figs. 2–4; §IV.A–B, Figs. 5–8; §V (supersonic Taylor–Green vortex, non-converged first dilatational peak, shock-capturing comparison).
- [Kurz et al. (2025)](/sources/kurz-2025.md) — §5.2, Fig. 11 (supersonic Taylor–Green vortex as GALÆXI validation).
- [Cao et al. (2022)](/sources/cao-2022.md) — §3.4, Fig. 15 (shocklets in decaying compressible isotropic turbulence).
- [Kumar & Ghosh (2022)](/sources/kumar-2022-b.md) — §3.1 (Shu–Osher problem labelled shock–turbulence interaction); §3.2.2, Table 4; §3.2.3, Figs. 30–36 (shock-train DNS in an isolator channel, Reynolds-stress amplification).
- [Deng et al. (2022)](/sources/deng-2022.md) — §4.15, Eq. (40), Figs. 23–25 (decaying compressible isotropic turbulence with eddy shocklets as an implicit-LES test).
- [Tonicello et al. (2022)](/sources/tonicello-2022.md) — §2.2; §3.2, Figs. 7–8, 11 (spectra and Mach-conditioned PDFs downstream of a compression/expansion ramp); §4.1–4.2, Eq. (4.14), Figs. 14, 20–26 (compression, expansion and subgrid Mach number in the energy transfer).
- [Cheng et al. (2023)](/sources/cheng-2023-b.md) — §1; §3.3–3.4, Figs. 4–5 (implicit LES framing; inviscid shock–vortex and shock–entropy-wave tests).
- [Chambers et al. (2022)](/sources/chambers-2022.md) — §II A–B (perforated-plate turbulence behind a shock; a different mechanism, passing mention).
- [Iwata et al. (2023)](/sources/iwata-2023.md) — §II A–C, Eq. 1, Table I; §III C–D; §IV A–C, Figs. 9–15; §V (detonation–turbulence interaction DNS).
- [Shi & Yan (2023)](/sources/shi-2023.md) — §IV.C, Table IV, Figs. 23–32 (turbulence amplification through a ramp interaction).
