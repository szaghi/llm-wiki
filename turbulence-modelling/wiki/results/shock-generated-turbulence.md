---
type: Result
title: "Shock-generated turbulence and turbulent shock jump relations"
description: "A strong shock crossing a medium with order-one density fluctuations generates turbulence whose velocity dispersion scales with shock speed times a pre-shock Atwood number, whose turbulent Mach number saturates for strong shocks, and whose Reynolds stress lowers the post-shock pressure and density through Favre-averaged jump relations."
status: established
aliases: [shock–inhomogeneity interaction, shock through a non-uniform medium, turbulent Rankine–Hugoniot relations, turbulent jump conditions, shock-driven turbulence]
tags: [compressible, implicit-les, plasma, astrophysics]
timestamp: 2026-10-25T20:39:00Z
---

# Shock-generated turbulence and turbulent shock jump relations

When a strong planar shock propagates into a medium whose density varies in
space, the post-shock flow becomes turbulent, a process the source below
scales with linear Richtmyer–Meshkov theory. As recalled by that source,
most theory of
shock–turbulence and shock–inhomogeneity interaction (linear interaction
analysis, rapid distortion) assumes small upstream perturbations and a
single passage of the fluid through one shock front.
[Davidovits et al. (2022)](/sources/davidovits-2022.md) study the regime the
theory excludes: density fluctuations of order one, which break the front
into several shocks. They give scaling laws for the generated velocity
dispersion and turbulent Mach number, and Favre-averaged jump relations in
which the post-shock Reynolds stress lowers the mean post-shock pressure and
density. The application is the controlled generation of compressible
turbulence in laser-driven high-energy-density shock tubes; the paper is
peripheral to closure modelling, and its "model" content is the scaling and
jump relations.

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

As recalled by [Davidovits et al. (2022)](/sources/davidovits-2022.md),
§III, earlier work on young supernova remnants (Inoue et al.) found the
post-shock velocity dispersion "reasonably predicted by the result of linear
analysis of the Richtmyer-Meshkov instability". Adapting that result to a
continuous density field, the authors (§III, Fig. 4) define a pre-shock
average Atwood number
$$A_\sigma=\frac{\sigma_\rho/\langle\rho\rangle}{1+\sigma_\rho/\langle\rho\rangle}$$
(page-local; it is not the two-fluid Atwood number of
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
For an unperturbed normal shock the Rankine–Hugoniot relations give, as
recalled by the authors,
$$\mathcal M_s=\frac{(\gamma+1)M_s^2}{\sqrt{(2\gamma M_s^2-\gamma+1)\big((\gamma-1)M_s^2+2\big)}}\;\xrightarrow{M_s\to\infty}\;\frac{\gamma+1}{\sqrt{2\gamma(\gamma-1)}},$$
which is $4/\sqrt5\approx1.79$ for $\gamma=5/3$. A stronger drive therefore
raises $\sigma_v$ but hardly $M_t$: "a rapidly diminishing return to driving
with higher-Mach shocks" for the turbulent Mach number. The constraint relaxes
as $\gamma\to1$, and simulations with a tabular carbon equation of state,
whose compression exceeds the $\gamma=5/3$ limit of 4, suggest a lower
effective $\gamma$ once the material ionizes (§III, §IV, Fig. 5).

## Favre-averaged jump relations with Reynolds stress

Following the turbulent jump conditions of Lele and the post-shock
definitions of Larsson et al., as recalled by
[Davidovits et al. (2022)](/sources/davidovits-2022.md), §III, the broken-up
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

# Citations

- [Davidovits et al. (2022)](/sources/davidovits-2022.md) — §I; §II A–B, Eq. (1), Table I, Fig. 1; §III, Eqs. (2)–(11), Figs. 3–9; §IV; App. A–B.
