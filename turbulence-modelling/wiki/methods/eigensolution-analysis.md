---
type: Method
title: "Eigensolution (dispersion–dissipation) analysis"
description: "Eigensolution analysis inserts Bloch waves into a linear discretization of advection to obtain numerical dispersion and dissipation; the page gives its temporal and spatial, semi- and fully-discrete forms for DG, flux reconstruction, spectral difference, compact differences with boundaries and spline VMS, mode counting, the time-step effects it predicts, and where under-resolved turbulence stops following it."
status: established
aliases: [eigenanalysis, von Neumann analysis, dispersion–dissipation analysis, dispersion–diffusion analysis, spatial eigenanalysis, temporal eigenanalysis, fully-discrete eigenanalysis, semi-discrete eigenanalysis, wave propagation analysis, approximate dispersion relation, ADR]
tags: [numerical-dissipation, dg, flux-reconstruction, implicit-les, dns]
timestamp: 2026-10-29T16:18:00Z
---

# Eigensolution (dispersion–dissipation) analysis

**Eigensolution analysis** (von Neumann analysis in the element setting)
measures how a linear discretization of the advection equation
$\partial_tu+a\,\partial_xu=0$ propagates and damps a plane wave. The
exact solution $e^{\mathrm i(kx-\omega_{\mathrm f}t)}$ has the
dispersion relation $\omega_{\mathrm f}=ak$, real, with no damping. In a
discontinuous element method the unknowns of all elements are written as
a Bloch wave, the element vector $\boldsymbol u_n=e^{\mathrm i(k_hx_n-\omega_{\mathrm f,h}t)}\boldsymbol v$
with $x_n$ the left end of element $n$, which turns the discrete operator
into a small matrix eigenproblem per wave. Its eigenvalues give a
numerical frequency $\omega_{\mathrm f,h}$ for a given $k$ (**temporal**
analysis) or numerical wavenumbers $k_h$ for a given $\omega_{\mathrm f}$
(**spatial** analysis); the real part measures dispersion, the imaginary
part dissipation. In the bundle the analysis is the main tool by which
high-order element methods are judged as
[implicit LES](/definitions/implicit-les.md) discretizations: it locates
where in wavenumber or frequency a scheme dissipates (see
[numerical dissipation](/properties/numerical-dissipation.md)).

Page-local symbols: $k$ the exact wavenumber and $\omega_{\mathrm f}$ the
exact angular frequency (not the specific dissipation rate $\omega$);
$k_h$, $\omega_{\mathrm f,h}$ their numerical, complex counterparts (the
sources' $\tilde\theta$, $\tilde\omega$, or $k^*$, $\omega^*$; the tilde is
not a Favre filter here); $\mathbf H(k_h)$ the semi-discrete operator and
$\mathbf T(k_h,\Delta t)$ the one-step amplification matrix of the
fully-discrete scheme; $\lambda_{\mathrm{up}}$ the upwinding parameter of
the interface flux, 1 for the upwind and 0 for the central flux (as on
[jump-penalty stabilization](/methods/jump-penalty-stabilization.md));
$r_{\Delta t}=\Delta t/\Delta t_{\max}$ the time step normalized by the
critical (CFL-limit) step; $n_{\mathrm{RK}}$ the number of Runge–Kutta
stages; $\omega_{\mathrm c}=\pi/\Delta t$ the temporal Nyquist frequency.
Wavenumbers and frequencies are plotted normalized by the
degree-of-freedom spacing, $kh/(N+1)$ and $\omega_{\mathrm f}h/(N+1)$,
with $h$ the element size and $N$ the polynomial degree.

## The four variants

**Semi-discrete temporal analysis.** With a flux reconstruction (FR)
scheme for unit-speed advection, the interface fluxes couple each element
to its two neighbours, and the Bloch ansatz gives
$$\frac{\mathrm d\boldsymbol u}{\mathrm dt}=\mathbf H(k_h)\boldsymbol u,\qquad
\mathbf H(k_h)=-2\big(\mathbf C^-e^{-\mathrm ik_h}+\mathbf C^0+\mathbf C^+e^{\mathrm ik_h}\big),$$
with coupling matrices $\mathbf C^-$, $\mathbf C^0$, $\mathbf C^+$ built
from the differentiation matrix, the derivatives of the correction
functions and the boundary values of the Lagrange basis (element size 1;
[Tonicello et al. 2023](/sources/tonicello-2023.md), §2.1, Eqs. 4–11).
Discontinuous Galerkin and spectral difference differ only through these
matrices, since both are recovered from FR by the choice of the
correction functions. The temporal eigenproblem
$-\mathrm i\omega_{\mathrm f,h}\boldsymbol u=\mathbf H(k_h)\boldsymbol u$
(Eq. 12) is the one that [Kou et al. (2023)](/sources/kou-2023.md), §3,
App. A, solve for modal DG with interface jump penalties, plotting
dispersion and dissipation against $kh/(N+1)$ for $N=2,3,4$, and that
[Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md), §5.2, solve for
advection–diffusion with DG at $N=7$ and a filtered artificial viscosity.

**Fully-discrete temporal analysis.** An explicit Runge–Kutta step
multiplies the Bloch vector by a polynomial in $\mathbf H\Delta t$,
$\boldsymbol u^{t+\Delta t}=\mathbf T(k_h,\Delta t)\boldsymbol u^t$,
$\mathbf T=\sum_m\beta_m(\mathbf H\Delta t)^m/m!$ with the scheme's
coefficients $\beta_m$ (page-local), and the eigenproblem becomes
$e^{-\mathrm i\omega_{\mathrm f,h}\Delta t}\boldsymbol u=\mathbf T\boldsymbol u$;
it is stable if the spectral radius of $\mathbf T$ stays below one for all
$k_h$ in $[-\pi(N+1)/h,\pi(N+1)/h]$, and it reduces to the semi-discrete
problem as $\Delta t\to0$. Tonicello et al. (2023, §2.1, Eqs. 13–16) state
this form after Vermeire & Vincent, whose results their own framework
reproduces (§3, §4.2; not displayed).

**Semi-discrete spatial analysis.** For inflow–outflow problems a real
frequency is imposed and the wavenumbers solved for:
$\det\big(\mathbf H(k_h)+\mathrm i\omega_{\mathrm f}\mathbf I\big)=0$, a
polynomial in $z=e^{\mathrm ik_h}$ (Eq. 17). The imaginary part of $k_h$
is the spatial damping rate, $u\propto e^{-\mathrm{Im}(k_h)x}$, so a
transmitted wave is stable for $\mathrm{Im}(k_h)>0$ and a reflected one
for $\mathrm{Im}(k_h)<0$; negative damping of a transmitted wave is
anti-dissipation, a convective instability (Eq. 23). Tonicello et al.
(§1) cite the earlier semi-discrete spatial analyses of Hu & Atkins,
Mengaldo et al., Moura et al. and Tonicello et al. (2021); the
[spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
kernel of Moura et al. is calibrated by spatial eigenanalysis, as cited
on that page.

**Fully-discrete spatial analysis** (Tonicello et al. 2023, §2.2,
Eq. 18), which the authors call the first of its kind for high-order
methods:
$$\det\big(\mathbf T(k_h,\Delta t)-e^{-\mathrm i\omega_{\mathrm f}\Delta t}\mathbf I\big)=0 .$$
For explicit Euler it is $\det\big((1-e^{-\mathrm i\omega_{\mathrm f}\Delta t})\mathbf I-2\Delta t(\mathbf C^-z^{-1}+\mathbf C^0+\mathbf C^+z)\big)=0$,
which tends to the semi-discrete form as $1-e^{-\mathrm i\omega_{\mathrm f}\Delta t}\to\mathrm i\omega_{\mathrm f}\Delta t$
(Eqs. 19–21). Each further Runge–Kutta stage raises the degree of the
polynomial in $z$ and adds roots (Eq. 22 for the two-stage scheme).

## Physical and spurious modes

The matrix eigenproblem has more eigenvalues than the one physical
relation:

- **Spatial, fully discrete.** With an upwind flux the number of
  transmitted modes equals the number of Runge–Kutta stages (2 for RK22,
  3 for RK33, 5 for the five-stage fourth-order RK45 of Carpenter &
  Kennedy), all transmitted; with a non-upwind flux there are twice as
  many, half of them reflected. The **physical mode** is the one anchored
  at the origin of the dissipation plot, with vanishing dissipation for
  well-resolved waves; the others are spurious (Tonicello et al. 2023, §3,
  Figs. 2, 4–5, 31–32).
- **Temporal, with a central flux.** Kou et al. (2023, App. C.1,
  Fig. C.17), after Asthana & Jameson, find that the physical mode of
  modal DG has a negative wave speed for $kh/(N+1)>1.57$, while a spurious
  mode carries the energy beyond about 1.1; their gradient-jump penalty
  acts on that spurious mode, adding upwinding and dissipation.
- **Temporal, with a penalty.** As a solution-jump penalty grows, the DG
  eigenvalues split into a set converging to the continuous-Galerkin
  eigenvalues and a set of large real part, pure dissipation (Kou et al.
  2023, §3, recovering a cited result).

## What the analysis predicts

**Where the dissipation sits.** The sources use the plots to choose
parameters and to compare schemes. Kou et al. (2023, §3, Figs. 1–4,
Table 1) select jump-penalty
values that improve dispersion at medium–high wavenumbers and move
dissipation to high wavenumbers (values and stability limits on
[jump-penalty stabilization](/methods/jump-penalty-stabilization.md));
with a central flux, a solution penalty of 0.5 reproduces the upwind
curves (App. C.1). Mateo-Gabín et al. (2022, §5.2, Figs. 2–3) find that
the exponent of a filtered artificial viscosity acts mainly at low
wavenumbers, where the filtered viscosity supplies almost all the
dissipation, and that elsewhere the interface flux dominates. Tonicello
et al. (2023, §3, Fig. 7, App. Figs. 29–30) find FR-DG spatially less
dissipative than FR-SD, with a more restrictive CFL limit; see
[spectral difference method](/methods/spectral-difference-method.md) and
[flux reconstruction](/methods/flux-reconstruction.md). Nearly centred
fluxes (Tonicello et al.'s interface parameter 0.49 in Fig. 9, i.e.
$\lambda_{\mathrm{up}}=0.02$ by the mapping in the Qualifications) show
"dissipative bubbles", dissipation concentrated in some frequency ranges
with others almost undamped, which "might potentially lead to undesirable
non-smooth features in simulations with broadband energy content" (§3).

**What the time step does** (Tonicello et al. 2023, §3–4.1):

- The spatial eigencurves become **periodic in frequency**, with period
  $2\omega_{\mathrm c}$, the spurious curves being shifted replications of
  the physical one, a periodicity the authors say had not been noted
  because $\omega_{\mathrm c}\to\infty$ as $\Delta t\to0$ (Fig. 2).
  $\omega_{\mathrm c}h/(N+1)$ is the counterpart of the wavenumber limit
  $kh/(N+1)=\pi$ of temporal analysis, but the observed limit for an
  $n_{\mathrm{RK}}$-stage scheme is $n_{\mathrm{RK}}\omega_{\mathrm c}/2$,
  "as if multiple single-stage time steps of size $\delta t=2\Delta t/R$
  had been employed" ($R=n_{\mathrm{RK}}$), the physical mode being
  symmetric about it (Figs. 4–5).
- With an upwind flux, a larger $r_{\Delta t}$ raises the dissipation at
  low frequencies and lowers it at high frequencies until, at
  $r_{\Delta t}=1$, the physical mode touches zero dissipation and
  anti-dissipation (convective instability) follows; the largest
  frequencies cause the CFL instability (§3, Figs. 2–6; §4.1). For a
  second-order FR-SD scheme with RK22 the spurious transmitted mode,
  infinitely damped as $r_{\Delta t}\to0$, approaches the physical-mode
  dissipation as $r_{\Delta t}\to1$.
- **Convergence order.** For fifth-order FR-SD ($N=4$) with RK33 the
  spatial superconvergence of order $2N+1=9$ falls to fourth order at small
  wavenumbers and frequencies, is kept in an intermediate range, and
  smaller time steps extend that range (Eqs. 24–25, Fig. 8).
- Explicit Euler is anti-dissipative at low frequency for $N=4$ FR-SD
  (Fig. 1); the predicted switch from dissipation to growth near
  $\Delta t\approx1.0\times10^{-4}$ for $h=0.01$ is seen in simulations at
  $\Delta t=9.825\times10^{-5}$, $9.925\times10^{-5}$ and
  $1.0925\times10^{-4}$ (§4.1, Figs. 16–17).

**Linear tests confirm it.** On 1D advection with an oscillating inlet
(100 elements, fifth-order SD, RK33 and RK45, nearly centred flux) the
trends of dissipation against $r_{\Delta t}$ are those predicted (§4.1,
Figs. 10–15), and on an inlet–outlet isentropic vortex (sixth- and
eighth-order SD, RK33) time steps near the CFL limit reduce the
convergence rate to that of the time integrator, with spurious entropy
oscillations only very close to the limit, "in agreement with" Vermeire et
al. (§4.2.1, Figs. 23–24).

## Where it stops predicting: under-resolved turbulence

The analysis is linear. Tonicello et al. (2023, §4.3) test its time-step
prediction on two under-resolved, implicit-LES-like flows run with the
improved spectral difference method and a Roe flux: the inviscid
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at $M=0.1$
($32^3$ elements, sixth order, RK3) and a two-dimensional inviscid duct
flow with an oscillating inlet and a mesh coarsening. In the Taylor–Green
vortex the numerical dissipation, measured as the kinetic-energy decay
rate minus the pressure–dilatation work, is "almost indistinguishable" for
$r_{\Delta t}=0.5$, 0.9 and 0.95: "the gradual decrease of numerical
dissipation observed in the theoretical framework does not manifest"
(Fig. 25). In the duct all runs below about $r_{\Delta t}=0.95$ behave
alike (Fig. 28). They conclude that in under-resolved flows spatial errors
dominate and overshadow the time-integration effect, that the time step
"plays a more relevant role in highly accurate simulations such as DNS",
and that the linear theory "is not always representative of more complex
nonlinear dynamics" (abstract, §4.3.2, §5); for
[DNS](/definitions/direct-numerical-simulation.md)-like flows only the
well-resolved range of the eigencurves is informative, for LES the
high-wavenumber and high-frequency range (§3).

The jump-penalty values that Kou et al. (2023) select by eigenanalysis
are not the ones they use in turbulence: their Taylor–Green penalties are
larger than those of the Burgers test, which they attribute to the $1/Re$
scaling of the penalty (§4.2).

## Advection–diffusion with a stabilized model: time-first against space-first VMS

[Sun et al. (2026)](/sources/sun-2026.md), §5, App. B, apply a fully
discrete Fourier analysis to the one-dimensional advection–diffusion
equation $\partial_tu+a\,\partial_xu-\nu\,\partial_x^2u=0$ (periodic,
uniform mesh) discretized by $C^1$ quadratic B-splines, a five-point
stencil, with a residual-based
[variational-multiscale](/methods/variational-multiscale-method.md) model.
A mode $e^{\sigma t+\mathrm ikx}$ has the exact damping $\nu k^2$ and
frequency $-ak$; the scheme's one-step amplification factor
$\zeta^h=e^{\sigma^h\Delta t}$ gives the numerical damping
$-\mathrm{Re}(\ln\zeta^h)/\Delta t$ and frequency
$\mathrm{Im}(\ln\zeta^h)/\Delta t$, plotted against $k\Delta x$ for
Courant number $a^*=a\Delta t/\Delta x$ and diffusion number
$\nu^*=\nu\Delta t/\Delta x^2$ (page-local $\sigma$, $\zeta^h$, $a^*$,
$\nu^*$, the source's $\nu$, $\kappa^*$). Three schemes are compared:

- **RK($s,p$)-VMS**, time first (Rothe method): each explicit Runge–Kutta
  stage is a steady problem whose fine scale is a mesh-independent
  multiple $\tau^*\in(0,1)$ (page-local) of the stage residual;
- **VMS-RK($s,p$)**, space first: the residual-based VMS
  semi-discretization with the classical stabilization parameter
  $\big[(2/\Delta t)^2+(2a/\Delta x)^2+9(4\nu/\Delta x^2)^2\big]^{-1/2}$
  (Eq. 5.5), then Runge–Kutta;
- the IMEX scheme of Le & Moin (Wray's RK3 with stage-wise Crank–Nicolson
  for diffusion), written VMS-RK(3,3)-CN.

Findings (§5.2–5.3, Tables 2–3, Figs. 1–5): both VMS variants have
temporal order $p$; the time-first variant has leading spatial errors
$O(\Delta x^4)$ in damping and $O(\Delta x^6)$ in frequency plus mixed
$\Delta x^2\Delta t$-type terms, while in the space-first variant the
stabilization parameter enters the mixed terms, so that when
$\Delta x\ll\Delta t$ in advection-dominated conditions its spatial
accuracy drops to third order in damping and fourth in frequency. The
time-first variant's stability region extends further along $a^*$
(convection-dominated), the space-first one is "more amenable to
diffusion-dominated regimes"; decreasing $\tau^*$ widens the region along
$a^*$, and except at $\tau^*=0.9$ raising the Runge–Kutta order widens it
too. At high wavenumbers and large $a^*$ the time-first variant has the
smaller damping and frequency errors. The implicit viscous treatment of
the IMEX scheme enlarges stability at large $\nu^*$ (both explicit
third-order variants are unstable for $\nu^*\gtrsim0.6$), at second-order
temporal accuracy only. The authors add (Remark 4) that in Kolmogorov
units the convective step limit, not the diffusive one, controls at high
Reynolds number, so implicit diffusion "does not significantly enlarge the
time step". The amplification factors of each variant are printed in
closed form (Tables B.1–B.2).

## Finite differences: modified wavenumber and the complete-scheme spectrum

For a finite-difference scheme on a periodic mesh the Bloch ansatz
reduces to a single Fourier mode, and the semi-discrete temporal analysis
is the **modified wavenumber**: the scheme replaces $\mathrm ik$ by
$\mathrm ik'$, so that $\omega_{\mathrm f,h}=ak'$ for advection at speed
$a$ ($k'$ page-local, as on
[compact finite-difference schemes](/methods/compact-finite-difference-scheme.md)).
[Lele (1992)](/sources/lele-1992.md), §3.1, builds the comparison of
compact schemes on it: a central scheme has a real $k'$, hence no
dissipation and a phase speed $k'/k$, and the fraction of the
representable wavenumbers in which $|k'-k|/k$ stays below a tolerance
(the resolving efficiency) ranks schemes independently of the number of
points; the figures and the spectral-like schemes it produces are on the
compact-scheme page. Lele places this measure as "analogous to, but more
general than" the intervals-per-wavelength comparisons of Swartz &
Wendroff and of Kreiss & Oliger, which sense only the longest waves
(§1).

**Boundaries need the whole operator.** A one-sided boundary closure has
a complex $k'$, its real part the dispersive and its imaginary part the
dissipative error, but Lele (1992, §4.1) calls this Fourier analysis of a
boundary scheme heuristic, and the sign of the imaginary part of many
compact closures, opposite to that of explicit one-sided formulas, no
ground for concluding instability. The stability test is instead the
eigenvalue problem of the complete semi-discrete scheme (§4.5,
Eqs. 4.5.1–4.5.4): for $\partial_tu+a\,\partial_xu=0$ on $[0,1]$ with
$u(0,t)=0$ and the scheme written as
$\mathbf A\,\mathrm d\boldsymbol u/\mathrm dt=-(a/h)\mathbf B\boldsymbol u$
($\mathbf A$, $\mathbf B$ the banded left- and right-side matrices,
interior and boundary rows included; page-local), normal modes
$e^{\sigma t}\boldsymbol v$ ($\sigma$ a complex growth rate, page-local)
satisfy
$$-\frac{\sigma h}{a}\,\mathbf A\boldsymbol v=\mathbf B\boldsymbol v,$$
and stability requires every eigenvalue in the left half-plane.
Lele's results, for $N$ up to 200 points ($N$ the number of points here,
not a polynomial degree; Figs. 9–10):

- with the tridiagonal fourth-order interior family and conservative or
  non-conservative compact closures, or explicit ones, all eigenvalues
  are stable, and the least-damped one approaches the imaginary axis like
  $N^{-3}$, the rate that Lele (§4.5) cites Warming & Beam as
  predicting for a second-order interior;
- the exception is the Padé interior with a second-order compact closure
  built to have no dissipative error at $kh=\pi$: one eigenvalue moves
  towards the origin more slowly than $N^{-1}$, "consistent with the
  $\log N/N$ approach" predicted by Warming & Beam, while other interior
  members with the same closure do not; no eigenvalue is unstable;
- with the interior fixed, a more accurate boundary closure shifts the
  spectrum towards more negative real parts, which Lele gives as "a
  caution against associating the eigenvalue spectrum with the overall
  performance (accuracy)" of a scheme.

The maximum of $k'h$ (and of the second-derivative counterpart) over
$[0,\pi]$ fixes the explicit Runge–Kutta time step on a periodic domain
(§4.6); the printed maxima grow in the order of the schemes' resolving
efficiencies, and Lele notes that spectral schemes have the most severe
restriction; the numbers are on the compact-scheme page.

## A nonlinear relative: the approximate dispersion relation

Eigensolution analysis needs a linear scheme. For the nonlinear weighted
interpolations of shock-capturing finite differences, [Wu et al. (2024b)](/sources/wu-2024-b.md),
§IV.A, Fig. 4, use the approximate dispersion relation (ADR) of Pirozzoli
(2006, as they cite it), which plots the real part (dispersion) and the
imaginary part (dissipation) of the modified wavenumber of the nonlinear
scheme. They compare the fifth-order [weighted compact nonlinear scheme](/methods/weighted-compact-nonlinear-scheme.md)
with linear, Jiang–Shu, Z-type, TENO-type, smooth-cutoff TENO-type and
adaptive smooth-cutoff weights: the TENO-type weights keep the properties
of the linear scheme over a wide wavenumber range, the smooth cutoff has
"slight influences" on them, and the adaptive variant approaches the
linear scheme. No values are tabulated; the scheme's behaviour in scale-resolving runs is on
[numerical dissipation](/properties/numerical-dissipation.md) and
[self-adaptive turbulence eddy simulation](/methods/self-adaptive-turbulence-eddy-simulation.md).

**Where neither applies.** [Tsoutsanis & Nogueira (2025)](/sources/tsoutsanis-2025.md),
§1, §4.1, citing Pirozzoli and Ruano et al., state that
approximate-dispersion-relation analysis is limited to linear schemes,
or one dimension without nonlinear interactions, and that their extension
to unstructured meshes "leads to results that are not understandable and
therefore of unclear value at present"; for nonlinear CWENOZ
reconstructions on mixed-element meshes they adjust dissipation and
dispersion cell by cell from a measured energy ratio instead (see
[numerical dissipation](/properties/numerical-dissipation.md) and
[WENO](/methods/weno-scheme.md)).

## Qualifications

- **Conventions differ.** Kou et al. (2023) and the temporal analyses
  plot dissipation as the imaginary part of $\omega_{\mathrm f,h}$, with
  positive values unstable; Tonicello et al.'s spatial analysis plots the
  imaginary part of $k_h$, positive stable for transmitted waves. Kou et
  al.'s upwinding parameter is 1 for upwind and 0 for central; Tonicello
  et al.'s interface parameter is 0 for upwind and 0.5 for central, which
  is $\lambda_{\mathrm{up}}=1-2\alpha_{\mathrm T}$ with $\alpha_{\mathrm T}$
  their parameter (registry §11) *(compiler check, not in the sources: their
  interface value $(1-\alpha_{\mathrm T})u_{\mathrm L}+\alpha_{\mathrm T}u_{\mathrm R}$
  equals $\tfrac12(1+\lambda_{\mathrm{up}})u_{\mathrm L}+\tfrac12(1-\lambda_{\mathrm{up}})u_{\mathrm R}$)*.
  Tonicello et al. call $N$ "the order of the solution polynomial" but use
  it as the degree ("5th order" is $N=4$).
- **Evidence.** The predictions are linear and one-dimensional.
  Tonicello et al. (2023) test them in under-resolved flow on one
  Taylor–Green vortex and one 2D duct flow, both with spectral difference
  and explicit Runge–Kutta near the CFL limit; no implicit time
  integration is tested. The abstract's expectation that the
  predictions "hold (even if partially)" in DNS of turbulence is not
  tested by a turbulent DNS in the paper.
- **Wording on explicit Euler.** Tonicello et al.'s Fig. 1 caption calls
  RK11 "convectively unstable for pure advection", the text "only
  marginally stable for pure advection" (§3, §4.1), while their runs show
  spatial growth.
- **Printed slips (Tonicello et al. 2023).** *(compiler check, not in
  the sources)* Inserting their interface fluxes (Eq. 9) into their matrix
  form (Eq. 7), or reading their unnumbered equation before Eq. (10), the
  coefficient of the left
  correction-function term is $(1-\alpha_{\mathrm T})e^{-\mathrm ik_h}\boldsymbol r^{\mathsf T}+(\alpha_{\mathrm T}-1)\boldsymbol l^{\mathsf T}$,
  so $\mathbf C^0$ carries $+(\alpha_{\mathrm T}-1)\mathbf g_L\boldsymbol l^{\mathsf T}$,
  whereas Eq. (10) prints $-(\alpha_{\mathrm T}-1)\mathbf g_L\boldsymbol l^{\mathsf T}$
  ($\boldsymbol l$, $\boldsymbol r$, $\mathbf g_L$ the basis values at the
  element ends and the correction-function derivatives; page-local);
  $\mathbf C^-$ and $\mathbf C^+$ follow as printed. The
  captions of Figs. 17, 18 and 20 assign the frequencies $\omega_0=0.1$,
  $\omega_1=1.3$ and $\omega_1=1.2$ in a way that does not match the text,
  which puts the switch test at the second frequency ($\omega_1=1.3$) and
  the 1000-element runs at the lowest one ($\omega_0=0.1$). Eq. (27)
  prints the Taylor–Green pressure amplitude $\rho_0U_0/16$, which for a
  pressure must be $\rho_0U_0^2/16$ *(compiler check, not in the
  sources)*, numerically the same since $U_0=1$.

# Citations

- [Lele (1992)](/sources/lele-1992.md) — §1, §3.1, Eqs. (3.1.3)–(3.1.7) (modified wavenumber, phase speed, resolving efficiency); §4.1 (complex modified wavenumber of boundary closures, heuristic); §4.5, Eqs. (4.5.1)–(4.5.4), Figs. 9–10 (eigenvalues of the complete semi-discrete scheme, $N^{-3}$ approach, the slow eigenvalue, boundary accuracy against spectrum); §4.6 (time-step limits).
- [Tonicello et al. (2023)](/sources/tonicello-2023.md) — abstract; §1; §2.1–2.2, Eqs. (4)–(25) (FR Bloch analysis, semi- and fully-discrete temporal and spatial eigenproblems, mode counting, error measures); §3, Figs. 1–9, App. Figs. 29–32 (periodicity, effective Nyquist frequency, time-step effects, FR-DG against FR-SD, dissipative bubbles); §4.1, Figs. 10–21; §4.2.1, Figs. 23–24; §4.3, Eq. (28), Figs. 25, 28; §5.
- [Kou et al. (2023)](/sources/kou-2023.md) — §3, App. A, App. C.1, Table 1, Table C.2, Figs. 1–4, C.17–C.18 (temporal eigensolution analysis of jump-penalized DG, spurious mode with central flux, CG limit); §4.2, §5 (penalties in the Taylor–Green vortex).
- [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md) — §5.2, Figs. 2–3 (von Neumann analysis of filtered artificial viscosity against Riemann-solver dissipation).
- [Wu et al. (2024b)](/sources/wu-2024-b.md) — §IV.A, Fig. 4 (approximate dispersion relation of fifth-order WCNS with linear, JS, Z, TENO-type and smooth-cutoff weights).
- [Sun et al. (2026)](/sources/sun-2026.md) — §5.1–§5.3, Eqs. (5.2)–(5.8), Tables 2–3, Figs. 1–5, App. B, Tables B.1–B.2 (Fourier analysis of time-first and space-first VMS and Le–Moin IMEX with $C^1$ quadratic B-splines; Remark 4).
- [Tsoutsanis & Nogueira (2025)](/sources/tsoutsanis-2025.md) — §1, §4.1 (limits of eigen-type and ADR analyses for nonlinear unstructured schemes, as cited).
