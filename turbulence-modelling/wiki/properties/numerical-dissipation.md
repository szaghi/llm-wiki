---
type: Property
title: "Numerical dissipation in scale-resolving simulation"
description: "Numerical dissipation is the kinetic-energy loss a discretization adds itself; sources show where in wavenumber and in the element it acts, how it is measured, that it competes with or replaces the subgrid model, that RANS-level artificial dissipation spoils hybrid RANS/LES, that it trades against dispersion, and that both too much and too little of it degrade LES."
status: established
aliases: [artificial dissipation, scheme dissipation, upwind dissipation, Riemann-solver dissipation, numerical viscosity]
tags: [numerical-dissipation, implicit-les, les, dg, kinetic-energy-preserving]
timestamp: 2026-10-27T11:01:00Z
---

# Numerical dissipation in scale-resolving simulation

**Numerical dissipation** is the loss of resolved kinetic energy produced
by the discretization itself: upwind or Riemann-solver fluxes, interface
penalties, filters, limiters, hyperviscous derivative stencils and blended
low-order operators. In a scale-resolving simulation it acts on the same
scales as the [subgrid-scale model](/definitions/large-eddy-simulation.md).
It therefore either competes with the model or, in
[implicit LES](/definitions/implicit-les.md), replaces it. A
**low-dissipation** (kinetic-energy-preserving) discretization adds none
from the convective terms, so all dissipation comes from viscosity and the
model ([kinetic-energy preservation](/properties/kinetic-energy-preservation.md)).

## Where it acts in wavenumber

- **Element methods with interface fluxes.** High-order element methods
  have very low dispersion errors over a broad range of scales and
  dissipation that is near zero for well-resolved scales and very high near
  the Nyquist cutoff. The interface dissipation thus acts like a
  high-frequency filter ([Flad & Gassner 2017](/sources/flad-2017.md),
  §1, §3.1, citing earlier DG studies). It is concentrated at the highest
  wavenumbers and lacks the low-wavenumber plateau of the Kraichnan
  [spectral eddy viscosity](/methods/spectral-eddy-viscosity.md), which
  Flad & Gassner propose as the reason DG implicit LES fails when the cutoff
  lies in the inertial range.
- **Designed hyperviscosity.** The implicit
  [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
  of [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md)
  (§5.1, §5.3) puts the dissipation near $k_c$ by construction. It is
  strongly anisotropic, largest along the mesh axes and smallest along the
  diagonals; the authors argue that this is an asset, because the
  convective differentiation errors are also largest along the axes.
- **Discretization order at fixed degrees of freedom.** Going from a
  second- to a fourth-order flux-reconstruction scheme at equal degrees of
  freedom improves partially-averaged Navier–Stokes far more than
  under-resolved DNS. [Dzanic et al. (2022)](/sources/dzanic-2022.md)
  (§3.2, §4) attribute this to the lower numerical dissipation of the
  high-order scheme, which lets the small resolved scales respond to the
  model. At low order the shedding and Kelvin–Helmholtz peak frequencies of
  the cylinder at $Re_D=3900$ are overpredicted by about 10% and 6%
  (Fig. 11).

- **Filtered artificial viscosity versus Riemann-solver dissipation.**
  [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md) (§5.2,
  Figs. 2–3) compare, by von Neumann (eigensolution) analysis of 1D
  advection–diffusion with DG at $N=7$ and an upwind flux, the dissipation
  of an artificial viscosity filtered by a modal
  [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
  kernel $(i/N)^{P}$ with that of the interface flux. The exponent $P$
  matters most at low wavenumbers, where the filtered viscosity supplies
  almost all the dissipation; at the other wavenumbers it is smaller than
  the Riemann-solver dissipation.

- **DG as an ILES discretization.** [Ferrer et al. (2023)](/sources/ferrer-2023.md)
  (§3.3, §4.1) state, citing earlier studies, that DG dissipation and
  dispersion errors are confined to high wavenumbers, so that numerical
  dissipation acts "primarily on under-resolved scales". In their
  [HORSES3D](/software/horses3d.md) code the Riemann solver is the
  main source (central, Lax–Friedrichs, Rusanov, Roe, low-dissipation
  Roe, Roe–Pike and matrix-dissipation fluxes are offered), and an
  interior-penalty parameter raised above its coercivity minimum is an
  alternative one; "for large enough Reynolds numbers" a turbulence model
  is added "for additional dissipation". The same concentration is what
  Flad & Gassner (above) blame for the failure of coarse DG ILES; see
  [implicit LES](/definitions/implicit-les.md).

- **Interface jump penalties in DG.** [Kou et al. (2023)](/sources/kou-2023.md)
  (§2.1, §3, App. A, Figs. 1–4, Table 1) add to a modal DG scheme a
  penalty on the solution jump or on the gradient jump across element faces
  ([jump-penalty stabilization](/methods/jump-penalty-stabilization.md))
  and study it by temporal eigensolution analysis of linear advection. With
  an upwind flux at $N=3$, a positive solution penalty lowers the
  dissipation at medium wavenumbers and raises it at high ones, without
  instability for any positive value; a slightly negative gradient
  penalty gives less dissipation at medium wavenumbers, and below about
  $-10^{-3}$ it makes the scheme unstable. Their stated preference is a
  scheme "with less dissipation at low to medium wavenumbers, and with more
  dissipation at high wavenumbers" (§3). The solution penalty
  drives DG towards continuous Galerkin as it grows, and with a central
  flux a solution penalty of 0.5 reproduces the upwind scheme (both
  recovered from earlier work). Both penalties are symmetric positive
  semi-definite face terms (§2.2), "completely decoupled from the time
  discretization" (§1, citing Moura et al.).
- **Upwind jump term near walls.** In an exactly divergence-free hybrid
  mixed finite-element method used as implicit LES, [Lederer et al. (2023)](/sources/lederer-2023.md)
  (§3.2–3.3, Figs. 2–3, 10) identify the upwind term on the tangential
  velocity jump as "the main source of stability" in under-resolved flow,
  and show with a jump indicator that the jumps, hence the dissipation, are
  largest near walls and, on the periodic hill, near the separation point:
  more near-wall dissipation than stability needs. Their
  [HOPU method](/methods/high-order-projection-based-upwind-method.md)
  applies the upwind penalty only to the part of the jump orthogonal to
  facet polynomials of degree $l$, treating the low-order jump with a
  central flux; all upwinding vanishes as $h\to0$. In channel flow at
  $Re_\tau=392.24$ this improves the $N=3$ mean velocity and the spectrum
  at $y^+=5$ (§4.1, Figs. 4, 6, Table 2).
  In a later version of the method, with a Chorin-type projection in time
  and indicator thresholds $\{0.1,0.2,0.3,0.4\}$ updated every tenth step,
  [Lederer et al. (2026)](/sources/lederer-2026.md) (§3.1–3.2, §4, Table 2,
  Figs. 4, 7–9) apply it to the transitional
  [Eppler 387 airfoil](/benchmarks/eppler-387-airfoil.md) at $Re=10^5$
  ($\alpha=10^\circ$) and $3\times10^5$ ($\alpha=4^\circ$) with $N=3$. They
  recall, citing Moura et al., that DG upwind dissipation acts on the
  high-order part of the solution (§3.1). Restricting the upwinding leaves
  the pressure distribution, lift, drag and separation bubble essentially
  unchanged ($C_L=1.274$ against 1.271, $C_D=0.0432$ against 0.0436 on the
  coarsest mesh at $Re=10^5$), and reduces the overprediction of the mean
  velocity and turbulent kinetic energy in the turbulent boundary layer for
  $y^+>10$, most on the coarsest mesh. The authors call the HOPU profiles
  "under-dissipative" and state that the laminar disturbances leading to
  transition are "not significantly affected" by it (§4.2, §5).
- **Upwind DG dissipation called insufficient.** [Ranjbar et al. (2026)](/sources/ranjbar-2026.md)
  (§I) state that the Riemann-solver dissipation of DG makes it more robust
  than continuous Galerkin but "remains insufficient for under-resolved
  turbulent flow simulations". In their DGSEM ([HORSES3D](/software/horses3d.md),
  low-dissipation Roe flux) the unmodelled coarse runs over-predict the
  turbulent kinetic energy of decaying isotropic turbulence, which they
  attribute to the missing subgrid dissipation (§III.A, Fig. 3), over-predict
  the r.m.s. velocities of channel flow at $Re_\tau=395$ (§III.C, Fig. 15)
  and are unstable in that channel without filtering (§III.D.2). Their
  remedy, [explicit modal filtering](/methods/explicit-modal-filtering.md),
  adds dissipation to the highest modal groups only in elements whose
  local Kolmogorov length is below the mesh spacing, with a cut-off that
  falls where strain and rotation are strong; its action vanishes as the
  flow relaminarizes (§III.D.4, Fig. 18) and costs 1–2.5% of wall time
  (§III.D.3).
- **Order, recalled for DG.** [Zhao et al. (2023b)](/sources/zhao-2023-b.md)
  (§1) recall that raising the DG order increases the dissipation at the
  largest wavenumbers while narrowing the range where it acts.

- **Riemann solvers and solution filters in flux reconstruction.**
  [Wang (2024)](/sources/wang-2024-b.md) recalls Rusanov as a central flux
  plus scalar dissipation (the largest local wave speed) and Roe as a
  central flux plus matrix dissipation (§2.2). In flux-reconstruction
  implicit LES of turbine cascades the most dissipative flux, Rusanov, is
  the most robust on no-slip walls and is used there throughout, with HLLC
  or Roe inside (§2.4.2, a numerical experiment stated without figures).
  HLLC is more robust than Roe: on the LS89 vane it is stable with less
  filtering (Tables 7–8), which the author relates to Roe's known weakness
  near vacuum states (Toro, cited); when both are stable the mean
  results are nearly identical, but their pressure spectra downstream of
  the T106C trailing edge differ at high frequencies for a reason the
  author leaves open (§4.2, Fig. 6; §4.3.2). The heat transfer coefficient
  depends more on the threshold of the local modal filter than on the
  Riemann solver (§4.3.2, Fig. 17). The entropy filter of Dzanic &
  Witherden (cited) stabilizes without tuning but resolves trailing-edge
  pressure waves less sharply, decays faster at high frequency and costs
  about 15% more per iteration than the local modal filter (§4.3.2,
  §4.4.3, Figs. 15–16); the author's run is less dissipative at high
  frequency than an implicit-time-stepping CPR run of Jia et al. (cited), which the author attributes, as a possibility, to that code's
  limiter. See [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
  and [subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md).
- **Flux-reconstruction correction parameter.** [Brillon & Nadarajah (2026)](/sources/brillon-2026.md)
  (§3.1.5, Fig. 14, Table 5) recall that the correction operator of
  energy-stable flux reconstruction acts as a linear filter on the
  residual, and find in under-resolved Taylor–Green runs ($N=5$, $96^3$
  degrees of freedom) that the dissipation peaks order as $c_+>c_{HU}>c_{SD}>c_{DG}$
  ("added dissipation associated with larger c values"; $c_{DG}$, $c_{SD}$
  and $c_{HU}$ recover DG, spectral difference and Huynh's scheme, $c_+$ is
  the largest stable value), with similar spectra.
  The largest value raises the stable CFL number from 0.26 to 0.36, against
  0.14 for over-integrated strong DG. See [flux reconstruction](/methods/flux-reconstruction.md).
- **Filters induced by central derivatives and interpolation.**
  [Caban et al. (2026)](/sources/caban-2026.md) (§3.2.1, Eqs. 24–29) write
  a discrete derivative as the exact one convolved with a
  [discretization-induced filter](/definitions/discretization-consistent-closure.md)
  $\mathcal F_h$, with transfer function $\hat{\mathcal F}^{(r)}_h(k)$ for the
  $r$-th derivative (superscript page-local), the ratio of the discrete to
  the exact derivative. For the semi-discrete advection–diffusion equation
  with central (compact) differences, each Fourier mode obeys
  $$\frac{d\phi_k}{dt}+ia\,\hat{\mathcal F}^{(1)}_h(k)\,k\,\phi_k=-\nu\,\hat{\mathcal F}^{(2)}_h(k)\,k^2\phi_k$$
  ($a$ the advection speed, page-local; Eq. 26), so the first-derivative
  filter changes only the phase speed, and the second-derivative filter
  gives a numerical viscosity $\nu\hat{\mathcal F}^{(2)}_h\le\nu$, slower
  damping of the small scales (Eq. 27). They recall that global spectral
  analysis including the time integration can give an effective viscosity
  above $\nu$ in some wavenumber ranges (§3.2.1). On a half-staggered grid
  the two interpolations to the pressure nodes and back act as the square
  of the interpolation filter (Eqs. 34–35), a dissipative filter whose
  effect is largest when the interpolation order is comparable to the
  derivative order (§4.1, Fig. 5). See [implicit LES](/definitions/implicit-les.md).

- **Vortex-dominated fluid–structure interaction.** [Liu et al. (2022b)](/sources/liu-2022-g.md)
  (§1) motivate high-order
  [flux reconstruction](/methods/flux-reconstruction.md) for
  vortex-induced vibration by its sensitivity to numerical dissipation and
  dispersion, and note that the low dissipation of high-order methods
  makes the fluid–structure coupling harder to stabilize for light bodies;
  their test flows are laminar.

## Dissipation against dispersion: upwind and central schemes

[Wang et al. (2024)](/sources/wang-2024.md) compare, for the
turbulent-kinetic-energy budget, a second-order central convective scheme
in the Kennedy–Gruber–Pirozzoli split form (KGP2,
[kinetic-energy preserving](/properties/kinetic-energy-preservation.md),
no numerical dissipation) with a sixth-order linear upwind reconstruction
(OPT6, the linear part of an optimized scheme of Li et al. with free
parameters $a=0$, $b=0.001$, page-local, and a Roe flux; see
[low-dissipation low-dispersion schemes](/methods/low-dissipation-low-dispersion-scheme.md)),
in compressible LES with the [WALE](/methods/wale-model.md) model.

- **Resolving power** (approximate dispersion relation of Pirozzoli, as
  recalled; §2.5, Table 1). KGP2 needs 14 points per wavelength for
  dispersion and 2 for dissipation (resolved $k_{\max}\Delta x=0.48$ and
  $\pi$); OPT6 needs 4 and 6 ($k_{\max}\Delta x=1.65$ and 1.15), the
  tolerance being unprinted.
- **Inviscid Taylor–Green vortex with time reversal** ($30^3$; flow reversed
  at $t=20L/V_0$, run to $40L/V_0$; §3.1, Fig. 2): KGP2 keeps the kinetic
  energy constant and returns to the initial field; OPT6, third-order MUSCL
  and fifth-order WENO decay monotonically, MUSCL most.
- **Channel** at $Re_\tau=180$, $M_b=0.2$ ($128\times66\times128$, §3.2,
  Figs. 3–4): mean velocity alike; OPT6 is closer to DNS near the
  Reynolds-shear-stress peak and in the budget terms, "especially for the
  dissipation term".
- **Periodic hill** at $Re_h=10\,595$ (grids $48^3$ to
  $196\times128\times186$, §3.3, Table 2, Figs. 5–6): first-order
  statistics are grid-insensitive, second-order ones and budget terms are
  not; OPT6 agrees with the reference "even in $48^3$ grids", especially in
  the budget balance, while KGP2 converges with refinement (separation at
  $x/h=0.26$, 0.24, 0.20, 0.20 from coarsest to finest, against 0.20 from
  DNS). A significant budget imbalance is used as a sign of insufficient
  resolution.

The authors recommend high-order upwind schemes for budget analysis
(§5). They recall (§1) that Mohan Rai & Moin found a high-order upwind
scheme better for turbulent flows, while Mittal & Moin and Park et al.
preferred central schemes; their recommendation agrees with the former.
The two schemes differ in formal order (second against sixth) as well as
in dissipation, and the paper tests no high-order kinetic-energy-preserving
central scheme (§2.3–2.4, §3). The authors credit OPT6's advantage to its
"good" dispersion and dissipation against KGP2's "perfect" dissipation but
"poor" dispersion (Table 1, §5). The recommendation sits beside the
statement of Goc et al. (2021, §2.3, below) that numerical dissipation is
"extremely detrimental" for coarse LES; it is not recorded as a
contradiction, because Goc et al. state a design rationale (citing Mittal
& Moin) without testing it, and Wang et al. attribute their result to
dispersion, not to the added dissipation.

For shock-capturing WENO schemes, [Luo & Wu (2021)](/sources/luo-2021-b.md)
(§4, Figs. 4–7) separate the linear dissipation of the underlying upwind
scheme from a nonlinear dissipation of the weighting: a weight of the
less-smooth substencil below its ideal value adds dissipation, one above
it removes some, so a nonlinear scheme can be less dissipative than its
linear scheme. Approximate-dispersion-relation analysis shows that pushed
too far this gives negative dissipation, which amplifies smooth waves
(§3.1, Fig. 1; §5.2.3, Fig. 11). See [WENO schemes](/methods/weno-scheme.md).

[Kim et al. (2024)](/sources/kim-2024.md) (§2.1, §4.2.1, Fig. 9) use a
central scheme in their cylinder LES: second-order central differences on a
staggered mesh that conserve kinetic energy and "do not exhibit numerical
dissipation" (citing Mittal & Moin), so that all dissipation comes from the
subgrid model. The scheme produces spurious oscillations near the front
stagnation region, a dispersive error, which a QUICK upwind scheme confined
to $x/D<-0.25$ removes without changing the wake at $Re_D=3900$; they note
that a hybrid scheme may be needed at much higher Reynolds number.

The summary of the first High-Order CFD Workshop by
[Wang et al. (2013)](/sources/wang-2013.md) frames the same trade at the
level of scheme families. First- and second-order methods "strongly
dissipate unsteady vortices" (§1), and DG schemes are "dissipative but
[have] particularly good dispersive accuracy" (§5.6). On the
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at $Re=1600$
the error of a twelfth-order central finite-difference scheme is
comparable with that of a formally fourth-order dispersion-relation-preserving
scheme, while the standard fourth-order scheme's error is much higher,
which "seems to indicate that the dispersion error already dominates"
(§5.6, Figs. 25–27). Of the workshop's three error measures, the
difference between $-dE_k/dt$ and the enstrophy-based dissipation
needs no reference solution and would vanish for a truly
[kinetic-energy-preserving](/properties/kinetic-energy-preservation.md)
method such as skew-symmetric central differences, which in practice add
dissipation through dealiasing filters (§5.6).

**Dissipation and vortex preservation in rotor wakes.** Two rotorcraft
sources measure scheme dissipation by how far a tip vortex survives on
the [Caradonna–Tung rotor](/benchmarks/caradonna-tung-rotor.md) in hover.

- **WENO variants in URANS.** [Han et al. (2022)](/sources/han-2022-c.md)
  (§4, Figs. 12, 17–24) compare third-order MUSCL, fifth-order WENO-JS
  and their Gauss–Kriging WENO-K, whose lower dissipation over a range of
  wavenumbers is reproduced from their earlier paper (Fig. 12), on an
  overset grid of 18.1 million cells with the
  [Spalart–Allmaras model](/methods/spalart-allmaras-model.md). The tip
  vortex is resolved to a wake age of $900^\circ$ against $630^\circ$ and
  $150^\circ$ at tip Mach number 0.439, and to $1000^\circ$ against $720^\circ$
  and $250^\circ$ at 0.877; the thrust-coefficient errors are 0.9%, 1.5% and
  3.5% (subsonic) and 3.0%, 5.1% and 8.2% (transonic), at 4.1% extra cost
  per revolution for WENO-K over WENO-JS. For the shocks WENO-K is "only
  slightly better" than WENO-JS (§4.2). See [WENO schemes](/methods/weno-scheme.md).
- **High-order finite volume in DDES.** [Sugaya & Imamura (2021)](/sources/sugaya-2021.md)
  (§4.5, Tables 6–7, Figs. 18–19) run the same rotor at tip Mach 0.439 by
  delayed detached-eddy simulation on moving Cartesian grids of 75 and 149
  million cells, with MUSCL or their fourth-order scheme. Thrust
  coefficient and figure of merit change little with grid and scheme
  (thrust coefficient $C_{\mathrm{Th}}$ 0.00514–0.00521, page-local), but the high-order scheme resolves finer wake
  vortices and secondary braid structures: "the numerical scheme greatly
  affects the prediction of the wake structure". It costs 99 h against
  63 h for MUSCL for the same revolutions (Table 6). See
  [immersed boundary methods](/methods/immersed-boundary-method.md).

**Bandwidth-optimized WENO.** [Kumar & Ghosh (2022)](/sources/kumar-2022-b.md)
(§1, §3.1, Tables 1–2) state that fifth-order WENO-JS is robust "but too
dissipative for turbulent flows", and test bandwidth-optimized WENO with a
total-variation limiter whose threshold sets how much of the domain uses
the nonlinear weights. Raising the threshold from 3 to 10 resolves more
small-scale structure in inviscid problems, structures they call "purely
numerical-viscosity effects"; the three-point variant is unstable in double
Mach reflection at threshold 7 and the four-point one at 5, and TENO8 is
unstable there "due to its less dissipative nature near the shocks"
(§3.1.6); less dissipative schemes lose the symmetry of the Rayleigh–Taylor
instability, as Fu et al. (cited) found (§3.1.7). The chosen variant costs
1.045 times WENO-JS per point and step against 2.9 for TENO8 (Table 1),
and runs a supersonic channel DNS (centreline Mach 1.49, $Re_\tau=240$)
and a shock train (§3.2). The review of compressible multiphase numerics
by [Maltsev et al. (2022)](/sources/maltsev-2022.md) (§IV, Table I) states,
citing Johnsen et al. and Pirozzoli, that WENO-JS dissipates
turbulent fluctuations at the higher resolvable wavenumbers and degrades
spectral properties through its upwind-biased nonlinear reconstruction;
it lists the low-dissipation variants (WENO-Z, WENO-M, bandwidth-optimized,
WCNS, MDCD-WENO with free dissipation and dispersion parameters) and the
interface-sharpening and anti-diffusion techniques that counter the
numerical smearing of material interfaces, which, like contacts, lack
characteristic steepening (§IV).

## Dissipation of RANS-type schemes in hybrid RANS/LES

[Carlsson et al. (2023)](/sources/carlsson-2023.md) quantify the
artificial dissipation of a second-order node-based finite-volume scheme
(Kok's energy-preserving central flux plus Jameson–Schmidt–Turkel matrix
dissipation) in hybrid RANS/LES. The fourth-difference coefficient
$\kappa^{(4)}$ (page-local, the global scaling of the background
dissipation) controls it (§2.2.1, §2.3, Fig. 1).

- **Values.** Typical RANS values $\kappa^{(4)}=1/128$–$1/64$ "will
  severely dissipate resolved turbulence"; earlier LES of decaying grid
  turbulence and channel flow indicate $1/512$ to $1/1024$ for
  scale-resolving simulation (§2.2.1). The conclusion gives "1/512 or
  smaller" (§5).
- **Decaying isotropic turbulence.** Against the Comte-Bellot–Corrsin
  experiment on $32^3$, $64^3$ and $128^3$ grids, the reference scheme
  ($\kappa^{(4)}=1/128$, no gradient extrapolation) decays the spectrum too
  steeply at high wavenumbers on all three grids, whereas the
  [low-dissipation low-dispersion scheme](/methods/low-dissipation-low-dispersion-scheme.md)
  with $\kappa^{(4)}=1/512$ or $1/1024$ matches it without recalibrating
  what the authors call the standard DES constants (SA 0.65, SST
  $k$-$\varepsilon$ branch 0.61), 1/512 being slightly more dissipative (§4.2, Fig. 3). In
  this flow "numerical dissipation of the convection term dominates" the
  decay (§5).
- **Log-layer mismatch.** In IDDES of channel flow at $Re_\tau=395$, 2400
  and 18 000 the reference scheme gives a significant
  [log-layer mismatch](/definitions/log-layer-mismatch.md) at all
  Reynolds numbers, correct in the RANS region and failing "as soon as the
  model switches to LES due to adding to much numerical dissipation"; the
  low-dissipation schemes leave only a small mismatch at the RANS–LES
  interface (§4.3, Fig. 4).
- **Shear-layer onset.** In delayed DES of a supersonic base flow with the
  shear-layer-adapted length scale, the formation of resolved structures in
  the initial shear layer is governed mainly by the numerical dissipation
  and the grid. The reference scheme strongly delays them; the
  low-dissipation scheme on the coarsest grid (1.82 million cells) has
  small-scale content comparable to the reference scheme on the finest
  (8.51 million). On the two finer grids it moves reattachment from
  $x/R\approx3.0$ (reference scheme) to about 2.7, against the experimental
  2.67 ($R$ the base radius), but does not improve the base pressure
  (§4.4, Figs. 9–10). See
  [detached-eddy simulation](/methods/detached-eddy-simulation.md).

The authors add that "some amount of numerical dissipation is often
needed" for convergence (§2.3). In their conclusion they credit a
vorticity-weighted (Ducros-type) shock sensor with better shear stress and
grey-area mitigation than the Jameson pressure sensor (§5); in the
base-flow discussion they attribute the faster transition of the separated
shear layer jointly to "the reduction in numerical dissipation from the
shock capturing sensor" and "the reduced overall dissipation" (§4.4).

**Central/upwind flux blending in transitional DDES.**
[Möller et al. (2024)](/sources/moller-2024.md) (§II.C, Eq. 26; §III.B.3,
Figs. 19–22) run transitional delayed
[DES](/methods/detached-eddy-simulation.md) of the V103
[compressor cascade](/benchmarks/compressor-cascade.md) at $Re=138\,500$ in
the second-order finite-volume code [TRACE](/software/trace.md). The
convective flux blends a central and a Roe upwind flux, with a fraction
$\sigma_b$ of upwind flux (page-local):

$$F=(1-\sigma_b)F_{\mathrm{central}}+\sigma_bF_{\mathrm{upwind}}.$$

The dynamic blending of Travin et al. (cited), designed for a clear
RANS/LES distinction, goes almost fully upwind ($\sigma_b\approx1$) in the
boundary layers on both blade sides. It damps the resolved scales there.
With synthetic inflow turbulence, constant blending gives:

- 0% (pure central): oscillations, and the suction-side laminar
  separation is suppressed;
- 25% (the value of Yin & Durbin): the synthetic scales are damped, bypass
  transition is delayed and the separation bubble is overpredicted;
- 5%: the best agreement with DNS in skin friction on both sides.

Without synthetic turbulence, varying the blending changes little. The
authors take this as evidence of the interdependence between resolved
inflow scales and numerical dissipation (§III.B.3). They caution that 5%
is "another adjustable parameter" that may need re-tuning for other
cases or meshes.
With it, bypass transition relies on resolved scales, so the model "acts
more like an LES model" (pp. 25–26).

Two further sources scale the upwind part of the convective flux by a
sensor, so that $\sigma_b$ (the upwind fraction above) is small in the
LES region and near one in the RANS region:

- **Adaptive-dissipation Roe scheme and the DES constant.**
  [Wang et al. (2021)](/sources/wang-2021-l.md) (App. A, Eqs. A.1–A.2)
  multiply the Roe dissipation by $\sigma_b=\tanh(A^3)$ (the source's
  $\phi$, with $\phi_{\max}=1$), where $A$ depends on the ratio of
  $C_{DES}\Delta$ to a turbulent length scale and on a vorticity-to-strain
  function, giving low dissipation in LES regions and stability in RANS
  regions, after Xiao et al. and Ducros et al. (cited). Calibrating
  their Reynolds-stress-model IDDES on decaying isotropic turbulence
  (Comte-Bellot–Corrsin, $64^3$) with this scheme gives $C_{DES}=0.3$ for
  the SSG branch and 0.5 for the LRR branch, below the values 0.630
  and 0.805 that their equilibrium analysis gives (ratios 0.48 and 0.62
  *(compiler check, not in the sources)*); the authors attribute
  the gap to numerical dissipation and conclude that the theoretical value
  "only provides a reference" (§2.3, §3.1, Fig. 1). Since $C_{DES}$ also
  enters the sensor, it changes the numerical dissipation too (App. B). See
  [detached-eddy simulation](/methods/detached-eddy-simulation.md).
- **Blending factor as a resolution indicator.** In SST-based DES of a
  transonic turbine cascade with tip clearance, [Yang & Ma (2022)](/sources/yang-2022-b.md)
  (§2.3, §3.1–3.2, Eq. 6, Figs. 4, 7) blend bounded central differencing
  with a second-order upwind scheme. They use the field of $\sigma_b$, near
  zero in the tip-leakage vortex and the wake and near one at walls and in
  irrotational regions, instead of a grid-convergence study to judge that
  the vortex is resolved in LES mode, and attribute the longer persistence
  of the resolved wake vortices, against URANS, to lower numerical
  dissipation. See [turbine cascade](/benchmarks/turbine-cascade.md).
- **Default scalar dissipation and transition models.** [Batther & Lee (2022)](/sources/batther-2022.md)
  (§3.1.2, §5) run delayed DES of a pitching airfoil with transition
  models in OVERFLOW with a fifth-order central scheme and scalar
  dissipation at the code's default smoothing parameters, and name the
  influence of the numerics on the transition-model predictions as an
  open question; they do not measure it (see
  [dynamic stall](/definitions/dynamic-stall.md)).

## Where it acts in the element

[Beck & Kurz (2023)](/sources/beck-2023.md) (§V A–C) contrast two DG-based
operators. DG dissipation enters only through the face fluxes, so it is
concentrated at element faces. The finite-volume subcell operator of the
hybrid [DG/FV scheme](/methods/subcell-finite-volume-shock-capturing.md),
whose subcells are sized by the LGL weights, dissipates most at the element
centre (Fig. 4; stated by the authors as an explanation, not tested). The no-model reward in forced HIT decreases as the degree $N$ grows from 3
to 8, which the authors relate to the localization of the numerical
dissipation at the element faces as $N$ grows. Pure DG ($\alpha=0$) is under-dissipative and pure FV ($\alpha=1$)
over-dissipative; an RL-chosen blend matches the DNS spectrum (Fig. 12). The
trained element-wise Smagorinsky coefficient peaks at the element centre and
vanishes at the faces, which the authors read as homogenizing the total
dissipation (Fig. 11).

## Measuring it

- **Energy budget.** [Cao et al. (2022)](/sources/cao-2022.md) (§3.1,
  Fig. 5) estimate the numerical dissipation of a high-order gas-kinetic
  scheme in the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
  ($Re=1600$, $M_0=0.1$) as the residual of the volume-averaged
  kinetic-energy budget, with $E_k$ the volume-averaged kinetic energy per
  unit reference density and $\varepsilon_1$, $\varepsilon_2$,
  $\varepsilon_3$, $\varepsilon_{\mathrm{num}}$ page-local:
  $$\varepsilon_{\mathrm{num}}=-\frac{dE_k}{dt}-(\varepsilon_1+\varepsilon_2+\varepsilon_3),$$
  where $\varepsilon_1=\tfrac{2\mu}{\rho_0\lvert\Omega\rvert}\int_\Omega S^d_{ij}S^d_{ij}\,dV$
  is the solenoidal (deviatoric) part, $\varepsilon_2=\tfrac{\mu_b}{\rho_0\lvert\Omega\rvert}\int_\Omega(\nabla\cdot\boldsymbol u)^2dV$
  the bulk-viscosity part with the scheme's inherent bulk viscosity
  $\mu_b=\tfrac{2n}{3(n+3)}\mu$ ($n=2$ internal degrees of freedom for a
  diatomic gas, page-local), and $\varepsilon_3=-\tfrac1{\rho_0\lvert\Omega\rvert}\int_\Omega p\,\nabla\cdot\boldsymbol u\,dV$
  the pressure–dilatation. The resolved part is computed with sixth-order
  central differences. $\varepsilon_{\mathrm{num}}$ decreases with grid
  refinement from $128^3$ to $1024^3$ and is significant on the coarse
  grids, where $\varepsilon_1+\varepsilon_2+\varepsilon_3$ is well below the
  decay rate. The authors read the agreement of the decay rate with the
  reference as support for [implicit LES](/definitions/implicit-les.md).
- **Subdomain energy budget with the model terms.** [Saini et al. (2023)](/sources/saini-2023.md)
  (§2.2–2.3, Eqs. 2–12) extend the budget-residual method of Schranner et
  al. (cited) to LES with an explicit model. The resolved-energy
  budget is integrated over an arbitrary subdomain, with the rate of
  change, viscous, subgrid (or SVV) dissipation and the surface fluxes,
  and the residual of its discrete form is minus the numerical dissipation
  rate. Equivalent viscosities follow as $\nu$ times the ratio of each
  dissipation to the viscous one (Eq. 11). Rules: budget terms computed at
  least at the solver's order; subdomains large enough for the residual to
  be dissipative (of the size of the main geometric features) and away
  from laminar regions; time derivative by central differences over the
  solver time step. Validated on the Taylor–Green vortex at $Re=3000$
  against Castiglioni & Domaradzki (cited) (§4, Figs. 5–6), it is
  then applied to a second-order finite-volume code with
  [WALE](/methods/wale-model.md) and a fifth-order continuous-Galerkin
  code with [SVV](/methods/spectral-vanishing-viscosity.md) (results under
  "Interaction with the subgrid model"). The residual also contains
  dispersive errors; it is slightly negative in the laminar phase of the
  vortex for the high-order runs and judged unreliable in a jet-stream
  subdomain (standard error about 20%) (§5.1–5.2).
- **The same budget for gas-kinetic ILES.** [Zhao et al. (2023a)](/sources/zhao-2023.md)
  (§5.1, Eqs. 22–23, Fig. 7) apply the budget of Cao et al. above to the
  Taylor–Green vortex at $Re=1600$ on $256^3$ cells with fifth- and
  seventh-order, non-compact and compact
  [gas-kinetic](/methods/high-order-gas-kinetic-scheme.md) reconstructions:
  higher order and the compact stencil reduce the numerical dissipation,
  and "the 5th-order scheme for ILES is still over-dissipative".
- **Decay of an exact solution.** For the lattice Boltzmann Hall-MHD
  scheme of [Foldes et al. (2023)](/sources/foldes-2023.md) (§4.3,
  Eqs. 4.7–4.9, Figs. 6–9), the damping of an exact circularly polarized
  wave gives an effective viscosity $\nu+\nu_{\mathrm{num}}$
  ($\nu_{\mathrm{num}}$ page-local); the ratio $\nu_{\mathrm{num}}/\nu$ is
  "only a small percentage", decreases as $N_x^{-2}$ with the grid points
  per direction, and does not depend on $\nu$ or the Mach number. On the
  3D Orszag–Tang problem at $512^3$ the moment-based collision operator
  over-damps the kinetic-energy spectrum at high wavenumbers against a
  pseudo-spectral code, recovered at $768^3$, while the BGK magnetic
  scheme matches it (§4.4, Fig. 11). See
  [lattice Boltzmann methods](/methods/lattice-boltzmann-method.md).
- **Numerical Reynolds number.** [Seta & Federrath (2022)](/sources/seta-2022.md)
  (§2.4) take from earlier work (McKee et al. 2020, App. C) that the
  numerical Reynolds numbers of their finite-volume MHD code are
  approximately $2n_g^{4/3}$ for $n_g$ grid points per direction (about
  8000 at $n_g=512$), and choose explicit $Re=Rm=2000$ so that "the
  explicit diffusion is always significantly higher and at larger scales
  than the numerical diffusion".
- **Resolution doubling.** [Davidovits et al. (2022)](/sources/davidovits-2022.md)
  (§II A) restrict their analysis of shock-generated turbulence, computed
  with artificial viscosity and no physical viscosity, to large-scale
  averages "least influenced" by numerical dissipation (citing Kitsionas et
  al.), and rerun a subset of 2D cases at double resolution: the scalings
  of the averages do not change, and in one example case the averages
  change by 0.6% to 2.9%.
- **Dissipation rate against enstrophy.** For the compressible
  Taylor–Green vortex at $Re=1600$, $M=0.1$, [Brillon & Nadarajah (2026)](/sources/brillon-2026.md)
  (§2.5, Eqs. 37, 45, 96–100, 105; §3.1.1, Figs. 2–4) take the numerical
  dissipation as the difference between the decay rate $-dE_k/dt$ and the
  enstrophy-based viscous dissipation, and the ratio of the two as an
  effective viscosity, $-dE_k/dt=\nu_{\mathrm{eff}}\langle\omega_i\omega_i\rangle$
  (the same definition as Reddy et al. below). In their
  dissipation-free nonlinearly stable flux-reconstruction DNS ($256^3$
  degrees of freedom) $\nu_{\mathrm{eff}}$ stays within 4.5% of $\nu$. The
  pressure–dilatation term, obtained as the residual of the
  kinetic-energy budget, agrees with the literature; computed pointwise it
  oscillates spuriously, much less with collocated flux nodes, and upwind
  (Roe, L2Roe or Lax–Friedrichs) interface dissipation nearly removes the
  oscillations (§3.1.7, Figs. 17–18), as Flad & Gassner (below) found.
  Roe and L2Roe dissipation lower the peak enstrophy; added Lax–Friedrichs
  dissipation raises it above the projected DNS, a behaviour the authors
  call "anti-dissipative" (§3.1.7, Fig. 17).
- **Effective Reynolds number of a decaying exact solution.**
  [Caban et al. (2026)](/sources/caban-2026.md) (§5.1, Eq. 42, Figs. 10–11)
  fit the energy decay of the laminar three-dimensional Taylor–Green
  solution at $Re=1600$ on $64^3$ with the analytical decay at an effective
  Reynolds number $Re_{\mathrm{eff}}$ (page-local). With sixth-order compact
  derivatives and spectral interpolation $Re_{\mathrm{eff}}/Re\approx1$: the
  derivative-induced filtering "does not decrease the effective Reynolds
  number". Dissipative compact interpolation and explicit
  regularization filtering lower it markedly, fourth-order interpolation
  to several times below $Re$.
- **Effective viscosity.** [Pereira et al. (2021)](/sources/pereira-2021.md)
  (§IV.3.1, Eqs. 22–23) include a numerical viscosity $\nu_n$ in the
  effective viscosity $\nu+\nu_t+\nu_n$ that sets an effective Reynolds
  number, but leave it out of their plots because it is not computed.

## Scheme design against excess dissipation

**Selective filters of central schemes.** Volpiani (2024, §2.2.2, §4,
Table 1) measures the dissipation of relaxation filters of central finite
differences by the kinetic energy kept in the inviscid Taylor–Green
vortex ($64^3$, $t=5$): 0.176, 0.903, 0.963, 0.978, 0.983 for filters of
3 to 11 points, and 0.978, 0.985, 0.986 for three optimized 11-point
filters, the newest of which minimizes the squared damping over
$0.2\le kh\le1.3$ at formal sixth order; the 2004 optimized filter, of
lower formal order, is "more dissipative for long waves" (§4). The same
filter as the only dissipation of a viscous run predicts the
kinetic-energy dissipation rate well on all grids while the
enstrophy-based rate is under-predicted on coarse ones, which the author
reads as the numerics carrying the energy drain (§5). Per 100 iterations per processor the
filtered divergence form costs 78.9 s, the split forms 115.9–298.9 s
(Table 1).

Several sources state how their scheme limits dissipation, without
measuring it:

- [Huang et al. (2022)](/sources/huang-2022.md) (§2.2) use for compressible
  boundary-layer DNS a seventh-order WENO scheme "optimized by means of
  limiters" to reduce numerical dissipation and, for the high-Reynolds
  Mach 2.5 case, an eighth-order split convective central scheme of
  Pirozzoli, "about twice as fast as the conventional WENO method".
- [Hoy & Bermejo-Moreno (2022)](/sources/hoy-2022.md) (§3) combine an
  essentially non-oscillatory scheme near shocks with a centred scheme
  elsewhere, switched by a sensor based on dilatation, enstrophy and sound
  speed (no formula printed).
- Cao et al. (2022, §2.1, Remark 1) use linear WENO weights for smooth
  low-speed flows "to avoid the numerical dissipation from artificially
  created interface discontinuity", and WENO-Z with characteristic
  variables only for the compressible isotropic turbulence with shocklets.
- [Alauzet et al. (2022)](/sources/alauzet-2022.md) (§4.1.1) use a
  multi-slope MUSCL "β-scheme" that blends centred and upwind gradients for
  low dissipation, and note that the limiter choice "directly affects the
  numerical dissipation". In their RANS of NASA Rotor 37, globally refined
  structured meshes dissipate the induced tip vortex while adapted meshes
  keep it (Figs. 42–43), which they attribute to resolution.
- [Gillyns et al. (2022)](/sources/gillyns-2022.md) (§2) cite small
  dispersion and minimal dissipation as advantages of the spectral element
  code Nek5000; [Mozaffari et al. (2022)](/sources/mozaffari-2022.md)
  (§5.1) blend 20% second-order upwind into central convection for their
  delayed DES.
- [Basile et al. (2023)](/sources/basile-2023.md) (§1) state that pure
  p-adaptation of DG needs very high polynomial degrees, which can cause
  instabilities from aliasing "or too little numerical dissipation"; their
  DG uses a Roe flux with a Harten-type entropy fix (§2.1).
- [Helm & Martín (2022)](/sources/helm-2022.md) (§II) use a fourth-order
  bandwidth-optimized WENO scheme with absolute and relative limiters "to
  reduce WENO dissipation" and filtering of the candidate-stencil weights
  near the wall. They recall that Wu & Martín "demonstrated that excess numerical
  dissipation can prevent" the wall-pressure plateau of a separated
  shock/boundary-layer interaction, and take the agreement of their Mach 3
  ramp pressure with the reference as "assurance" that their LES does not
  suffer from it (§III C, Fig. 8); see [shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md).
- [Dang et al. (2022)](/sources/dang-2022.md) (§1, §2.2.3) write the DNS code
  [OpenCFD-SCU](/software/opencfd-scu.md) with a three-way hybrid scheme
  switched by a modified Jameson pressure sensor: seventh-order upwind
  where the sensor is below a first threshold (usually 0.02),
  seventh-order WENO up to a second (usually 0.1), fifth-order WENO
  above. "More than 90%" of the points use the low-dissipation upwind
  scheme. They state that seventh-order WENO alone is still too
  dissipative for good DNS data, and that flows above Mach 6 usually need
  a dissipative scheme for robustness at strong shocks. See
  [WENO schemes](/methods/weno-scheme.md).
- [Placco et al. (2023)](/sources/placco-2023.md) (§2) rely on the
  dissipation of fifth-order WENO as the only small-scale dissipation of
  their capsule-wake simulation ([implicit LES](/definitions/implicit-les.md)),
  and recall that low-dissipation schemes represent the recirculation of
  capsule wakes better in earlier DES studies (§1).
- [Delassaux et al. (2023)](/sources/delassaux-2023.md) (§4.2) choose for
  hybrid RANS/LES of a car in a commercial finite-volume code the bounded
  central-differencing scheme, a blend of central, second-order and
  first-order upwind: second-order upwind "would annihilate the turbulent
  structures" and pure central differencing "can be unstable or produce
  nonphysical wiggles", so the bounded scheme, "slightly more dissipative"
  than central, is "the optimal choice". They advise a CFL number of at
  most 5 in the LES region, and recall from their Ahmed-body study that
  above 10 the slant separation is missed or massively overpredicted (§5).
- [Moratilla-Vega et al. (2024)](/sources/moratillavega-2024.md) (§2.1,
  §4.3–4.4, Eq. 6, Figs. 12–13, 18) use a second-order Roe-type flux whose
  upwind term is scaled by a smoothing parameter between 0.3 and 1, lowered
  in the jet's source region and raised near the boundaries to absorb
  outgoing waves. The LES dissipates high-frequency acoustic waves within a
  few jet diameters, which they relate to the 22 points per wavelength a
  second-order scheme needs against 5 for their fifth-order DG acoustic
  solver (values recalled from earlier work); hence the separate high-order
  acoustic step.
- [Bernades et al. (2023)](/sources/bernades-2023.md) (§1, footnote 1;
  §4.1, Fig. 1) distinguish numerical dissipation, an undesired behaviour
  of the method, from artificial dissipation, added deliberately, and
  require both to be absent from schemes for transcritical turbulence; in
  their density-wave tests the upwind and hybrid schemes dissipate the
  wave, while their [kinetic-energy- and pressure-equilibrium-preserving](/properties/pressure-equilibrium-preservation.md)
  scheme adds none (its total-energy error is dissipative at
  $O(h^2)$, §4.2).
- [Slaughter et al. (2023)](/sources/slaughter-2023.md) (§3–3.1) take all
  the small-scale dissipation of their spectral/hp implicit LES from
  gradient-jump penalisation and spanwise SVV, "a pure characteristic of
  the numerical scheme", and relay that SVV at lower polynomial order can
  be overly diffusive.
- [Morsbach et al. (2024)](/sources/morsbach-2024.md) (§2) let the Roe
  interface flux of a kinetic-energy-preserving split-form DGSEM ($N=5$)
  carry the subgrid dissipation of their turbine-cascade implicit LES,
  citing the dispersion and dissipation analyses of DG (Gassner & Kopriva;
  Moura et al., cited).
- [Cai et al. (2022)](/sources/cai-2022.md) (§II.A, Eqs. 7, 9) use a
  hybrid recursive regularized lattice Boltzmann collision, because plain
  BGK is unstable at high Reynolds number; it adds a hyper-viscous term
  depending on the fourth derivative of the velocity and on a parameter
  "chosen as close to unity as possible" (no value printed). See
  [immersed boundary methods](/methods/immersed-boundary-method.md).
- In a plasma-turbulence fluid code, [Coelho et al. (2022)](/sources/coelho-2022.md)
  (p. 4) add explicit perpendicular and parallel diffusion terms "to improve
  the numerical stability", and state, without showing it, that they give
  "significantly lower perpendicular transport than turbulence".
- In the stabilized finite-element LES of [Prakash et al. (2022)](/sources/prakash-2022.md)
  (§III.B.1), the authors state from experiments not shown that the
  SUPG/PSPG/grad-div stabilization dissipates "significantly" less than any
  of their explicit SGS models; their no-model run of forced isotropic
  turbulence at $\nu=10^{-12}$ piles energy up at the highest wavenumbers
  (Fig. 4).
- In the stabilized continuous-Galerkin implicit LES of
  [Prieto Saavedra et al. (2024)](/sources/prietosaavedra-2024.md) (§3.1,
  Eq. 10; §4.2) the SUPG/PSPG term, a parameter times the strong momentum
  residual, is the only added dissipation, with the transient parameter
  $$\tau_u=\Big[\Big(\frac1{\Delta t}\Big)^2+\Big(\frac{2\lvert\boldsymbol u\rvert}{h}\Big)^2+9\Big(\frac{4\nu}{h^2}\Big)^2\Big]^{-1/2}$$
  ($\tau_u$ page-local; $h$ the diameter of the sphere of the cell volume,
  used for both the convective and the diffusive size). Its dissipation
  therefore shrinks with the time step: on a coarse mesh of the
  [periodic hill](/benchmarks/periodic-hill.md) at $Re_h=5600$, lowering
  $\Delta t$ from 0.1 to 0.0125 lengthens the recirculation from $x/h=4.73$
  to 5.37 (experiment 4.83) and degrades the Reynolds stresses; on the
  fine mesh, where the residual is small, the time step matters little
  (Table 5). The authors relate this to earlier stabilized-method studies
  (cited). See [implicit LES](/definitions/implicit-les.md).
- [Ruan et al. (2023)](/sources/ruan-2023.md) (§2) simulate solar-flare
  MHD turbulence with the HLL flux and a third-order limiter on the
  coarser adaptive levels, and the second-order van Leer limiter on the
  finer levels in the low atmosphere and flaring regions, with no subgrid
  model; the paper does not discuss the numerical dissipation of this
  combination or the resolution dependence of its turbulent energy.

## Interaction with the subgrid model

- **Detrimental excess.** [Goc et al. (2021)](/sources/goc-2021.md)
  (§2.3) state that low-dissipation discretization is essential and that
  numerical dissipation is "extremely detrimental" for coarse LES (Mittal &
  Moin 1997, cited); many unsteady solvers inherit dissipative RANS
  discretizations. Their aircraft LES use charLES, with entropy- and
  kinetic-energy-preserving fluxes, and Alya, with an energy-conserving
  Galerkin convective form and no upwinding. [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md)
  (§II.B) describe charLES as kinetic-energy conserving and approximately
  entropy preserving, "thereby limiting the amount of numerical
  dissipation".
- **Masking the model.** On de-aliased DG with Roe fluxes, adding
  Smagorinsky or VMS Smagorinsky does not improve coarse DHIT, which the
  authors attribute to the interaction of the artificial dissipation with
  the SGS viscosity. On a dissipation-free split-form baseline, which in
  their argument separates stability from model dissipation, Smagorinsky
  works (Flad & Gassner 2017, §1, §4). Of the three
  ways Flad & Gassner add small-scale damping (§5), only the low-dissipation
  L2Roe flux damps the pressure–dilatation oscillations left by the
  kinetic-energy-preserving scheme. It does so by scaling the interface
  velocity jump by the local Mach number, so that it dissipates density and
  pressure fluctuations without affecting the momentum dissipation. A BR2
  penalty reduces them somewhat, and the modal cusp viscosity leaves them
  unchanged (§5.1, Fig. 10).
- **Errors that look like a model.** With the Smagorinsky model at
  $\Delta x=\Delta$, differentiation errors dominate and the spectral eddy
  viscosity drops near the mesh cutoff, a numerical signature (Vicente Cruz
  & Lamballais 2023, §6.3). Numerical convergence needs $\Delta x=\Delta/5$.
  The authors propose the criterion that the effective transfer function at
  the mesh cutoff should be at most about 0.1.
- **Automatic compensation.** In a mixed Smagorinsky + SVV model, lowering
  $C_s$ from 0.18 to 0 shifts the dominant dissipation to the SVV term, which
  compensates the missing explicit dissipation; Vicente Cruz & Lamballais
  (2023, §6.5) relate this to the "convenient conspiracy" of Oran & Boris.
- **Numerics dominate even beside an explicit model.** With the subdomain
  budget above, [Saini et al. (2023)](/sources/saini-2023.md) (§5, Figs.
  7–16; Abstract) find numerical dissipation 60–90% of the non-viscous
  (model plus numerical) dissipation in both a second-order finite-volume
  LES with WALE and a fifth-order continuous-Galerkin LES with SVV:
  - Taylor–Green vortex at $Re=1600$: 65–75% for the second-order runs
    and 85–95% for the high-order ones; the second-order $64^3$ run reaches
    a non-viscous to viscous dissipation ratio near 4, a much lower
    effective Reynolds number, against at most 1.2 for $16^3$ elements of
    degree 4;
  - combustor port flow ($Re=2.25\times10^4$): numerical dissipation is
    4–12 times the WALE dissipation and 1.3–6 times the SVV dissipation in
    the turbulent subdomains; between 16 and 48 million points, 85% of the
    change of the normalized non-viscous dissipation comes from the
    numerics; this ratio is 10–23 (16 million points, second order), 8–15
    (48 million) and 2.5–7 (8.4 million, high order);
  - the numerical dissipation follows the instantaneous flow more than the
    model dissipation does.
  They conclude that the accuracy-per-cost gain of the high-order solver
  comes mainly from its lower numerical dissipation, and that the result
  "challenges the usual assumption in LES practice that all or most of the
  required subgrid dissipation is imparted by the SGS model", in line with
  Ghosal (cited). Goc et al. (above) call numerical dissipation
  "extremely detrimental" for coarse LES.
- **Explicit model on top of an implicit one.** Lederer et al. (2023, §4.1,
  §6) find that a WALE-based variational multiscale model added to DG-type
  implicit LES does not help and, on the coarsest grids, slightly harms;
  [Kou et al. (2023)](/sources/kou-2023.md) (§4.2, Fig. 12) find interface
  penalties "clearly superior" to Smagorinsky and Vreman models adapted to
  DG on the Taylor–Green vortex. Flad & Gassner (above) likewise report
  that Smagorinsky added to de-aliased DG with Roe fluxes does not improve
  coarse decaying isotropic turbulence.
- **Learning around the numerics.** [Kurz et al. (2023)](/sources/kurz-2023.md)
  (§1, §4.2) note that implicit modelling interprets numerical dissipation
  as a turbulence model, and train a Smagorinsky coefficient inside the DG
  solver so that the closure adapts to the discretization's own
  dissipation; their no-model DG LES piles energy up at high wavenumbers
  in forced isotropic turbulence ($N=5$, 7). See
  [discretization-consistent closure](/definitions/discretization-consistent-closure.md).
- **Model dissipation far above scheme dissipation at high order.**
  [Duan & Wang (2024)](/sources/duan-2024.md) (§5.1, Figs. 5–6) find in
  flux-reconstruction LES of the inviscid Taylor–Green vortex ($16^3$
  elements, $N=4$) that the subgrid dissipation of the Smagorinsky, WALE
  and Vreman models is much larger than the Riemann-solver dissipation of
  the scheme, with every filter width. They argue that subgrid models were
  calibrated on second-order schemes and high-order schemes carry less
  dissipation, and recalibrate the filter width rather than the constant
  (§3; see [Vreman model](/methods/vreman-model.md)). They recall that all
  high-order schemes show some high-wavenumber pile-up of energy in a
  broadband Burgers test, central finite differences the most (§1, Fig. 1,
  from an earlier comparison), and that stabilization by solution limiting
  in wall-modelled LES of channel flow at $Re_\tau=5200$ makes the wall
  friction depend on the amount of limiting, too little over-predicting it
  and too much under-predicting it (§1, Fig. 2), which they call ad hoc.
- **Negligible by construction.** [Domaradzki (2024)](/sources/domaradzki-2024.md)
  (§3.3) tests the [autonomous eddy-viscosity model](/methods/autonomous-eddy-viscosity-model.md)
  in a de-aliased pseudo-spectral code,
  stating that its numerical dissipation is negligible so that the
  observed effects are those of the model, and warns that in many
  finite-difference and finite-volume methods the numerical dissipation is
  comparable to the model dissipation, the ratio that the budget of Saini
  et al. above measures. [Wang et al. (2023c)](/sources/wang-2023-c.md)
  (§II.A) filter explicitly with a filter-to-grid ratio of 2, in a
  pseudo-spectral code, "to ensure that the influence of the numerical
  errors is much less compared to that of the SGS model".
- **Scheme dissipation as the reason explicit models lose.**
  [Zhao et al. (2021)](/sources/zhao-2021-c.md) (Abstract, §IV, §VI,
  Apps. A–B) find gas-kinetic implicit LES of channel flow better than
  four explicit eddy-viscosity models (see
  [implicit LES](/definitions/implicit-les.md)) and explain it by the
  high-order scheme's numerical dissipation already sufficing as subgrid
  dissipation: an explicit model over-dissipates, lowers the wall velocity
  gradient and $u_\tau$, and degrades the profiles. They measure no
  dissipation. Two further statements are theirs: the modified interface
  flux needed at $Re_\tau=395$ (an upwind kinetic part for the
  non-equilibrium initial state, "flux 2") is "a little" more dissipative
  than the smooth-flow flux, which works at 180 because the central
  character of the scheme keeps dissipation small (§IV, App. A), and
  "when the grids are refined, the numerical dissipation decreases"
  (App. B). See [high-order gas-kinetic schemes](/methods/high-order-gas-kinetic-scheme.md).
- **Scheme dissipation inside a learned-model test.** In the pseudospectral
  LES of [Li et al. (2021)](/sources/li-2021.md) (§II A, §III C) a
  "high-order dissipative numerical method" taken from Xie et al. (2020,
  cited) mimics the kinetic-energy flux to small scales at high
  wavenumbers, in DNS and LES alike. Their learned tensor model has a
  small eddy-viscosity term (see [gradient model](/methods/gradient-model.md)),
  and the no-model LES at $128^3$ "deviates strongly" near the cutoff;
  the paper does not separate the dissipation of the numerics from that of
  the model.
- **Uncounted dissipation.** The upwinding-based energy-transfer model iSGET
  of [Haering et al. (2022)](/sources/haering-2022.md) (App. C, §V D)
  works in their hybrid model, but its numerical dissipation is not counted
  in their resolution-adequacy parameter, an inconsistency the authors
  acknowledge.

- **Kinetic-energy- and entropy-preserving baseline for model testing.**
  [Maejima & Kawai (2025)](/sources/maejima-2025.md) (§4) choose a
  second-order non-dissipative central scheme of this kind "so that SGS
  dissipation is not contaminated by numerical dissipation" (citing Asada
  et al.). They need it to read a learned model's backscatter from the
  Reynolds-stress budgets (see
  [energy backscatter](/definitions/energy-backscatter.md)).
- **Spectral elements called dissipation-free.** [Reddy et al. (2026)](/sources/reddy-2026.md)
  (§1) call a continuous spectral-element discretization "ideal" for
  comparing subgrid models "due to the lack of inherent numerical
  dissipation present". They do not measure it. In the Taylor–Green vortex
  they define an effective viscosity from the kinetic-energy dissipation
  rate and the enstrophy, $\varepsilon=\nu_{\mathrm{eff}}\langle\omega_i\omega_i\rangle$
  ($\nu_{\mathrm{eff}}$ page-local). It includes subgrid and numerical
  dissipation together (§7.1).

  [Mukha et al. (2025)](/sources/mukha-2025.md) (§II.B, §III.C) find the
  continuous-Galerkin [Nek5000](/software/nek5000.md) discretization not
  benign in coarse wall-modelled LES:
  - velocity derivatives jump across element boundaries, which produces
    spikes in the subgrid viscosity, "just numerical artifacts";
  - global momentum is not conserved;
  - the explicit subgrid model doubles as the stabilizer, and higher
    near-wall model dissipation reduces the artifacts. A modal relaxation
    filter alone "does not introduce enough damping".

  They call continuity of velocity derivatives "a missing component in the
  current WMLES methodology". See
  [spectral-element method](/methods/spectral-element-method.md) and
  [wall-modelled LES](/methods/wall-modelled-les.md).

- **Eddy viscosity not recommended on a dissipation-free high-order scheme.**
  With nonlinearly stable flux reconstruction ($N=5$, $96^3$ degrees of
  freedom), [Brillon & Nadarajah (2026)](/sources/brillon-2026.md)
  (§3.1.8, Figs. 19–20) add Smagorinsky, shear-improved, high-pass-filtered
  and dynamic Smagorinsky models to the under-resolved Taylor–Green vortex.
  They raise the dissipation rate marginally, lower the peak enstrophy and
  dissipate energy at wavenumbers where the baseline already has a
  deficit, so the models are "not recommended for the LES of transitional
  turbulent free-shear flows using NSFR". On strong-form DG without
  over-integration, which is unstable at $N=5$, a high-pass-filtered model
  restores stability but not accuracy: "a stable scheme without any
  de-aliasing can lead to inaccuracies".
  [Lederer et al. (2026)](/sources/lederer-2026.md) (§3) likewise exclude
  explicit subgrid models from their transitional-airfoil runs, citing
  "their inferior performance compared to ILES in a DG framework for
  wall-bounded flow problems".
- **Numerical filters as the model.** In LES of the transitional
  Taylor–Green vortex at $Re=1600$ on $64^3$ with a half-staggered compact
  scheme, [Caban et al. (2026)](/sources/caban-2026.md) (§5.3–5.4,
  Tables 4–9) find:
  - with spectral (non-dissipative) interpolation and no explicit filter,
    the no-model run is unstable near $t=3.5$, and the Smagorinsky and
    Vreman models with $\Delta=2h$ are unstable too; with $\Delta=4h$
    they are stable but inaccurate (§5.3.1, Fig. 18);
  - dissipative compact interpolation, or an explicit regularization
    filter, stabilizes the runs with sixth- and tenth-order derivatives;
    without a model these act as implicit LES and give the smallest
    kinetic-energy error ($2.23\times10^{-2}$), about half that of the best
    eddy-viscosity run; eddy viscosity added to these filters is stable
    but too dissipative (Table 4, Figs. 19–20). With second-order
    derivatives the regularized no-model run is unstable, which the
    authors attribute to the second-derivative filter damping the viscous
    dissipation (§5.3.1);
  - lowering the interpolation order from tenth to fourth raises the error
    by an order of magnitude for implicit LES and about fivefold with the
    eddy-viscosity models (Table 4);
  - the approximate deconvolution model "requires some level of numerical
    dissipation", in line with the relaxation term of Stolz and Adams
    (cited) (§5.4.2, §6).
  The authors restrict the interpolation results to staggered and
  half-staggered algorithms (§6). See
  [scale-similarity models](/methods/scale-similarity-model.md) and
  [implicit LES](/definitions/implicit-les.md).
- **The numerics shape what a learned model meets.** [Wu & Lele (2026)](/sources/wu-2026.md)
  (§1, §3.2.2, §5–6, Tables 3–4) state that the LES filter is "a product of
  both the grid and the numerical method" and test the same neural-network
  subgrid models in a Fourier-spectral solver with two-thirds dealiasing
  and in a sixth-order compact solver without it. A network trained on
  box-filtered data alone is under-dissipative in both, with high-wavenumber
  pile-up (sum spectral error 18.87 and 32.58); training on several filter
  shapes, including one that mimics the dealiasing, removes most of it.
  See [neural-network subgrid models](/methods/neural-network-sgs-model.md).

## Shock capturing and dissipation in compressible turbulence

Four sources measure what shock capturing does to the turbulent scales,
in decaying and driven compressible turbulence and in a transonic
cascade.

- **Seven schemes on the supersonic Taylor–Green vortex.**
  [Chapelier et al. (2024)](/sources/chapelier-2024.md) (§III–V, Figs. 5–8)
  compare seven codes at $Re=1600$, $M_0=1.25$ at $64^3$ to $512^3$
  degrees of freedom. They read the solenoidal dissipation (vorticity
  based) as a small-scale measure and the dilatational dissipation as a
  shock-sharpness measure. Its oscillations in time signal Gibbs
  oscillations.
  - **Riemann-flux codes.** Modal DG, spectral difference and TENO
    under-estimate the early kinetic energy at $64^3$. The authors
    attribute this to the dissipation of their Riemann-based interface
    fluxes.
  - **Second order.** The second-order code (H3AMR) under-estimates the
    kinetic energy at $64^3$, which the authors attribute to the excess
    numerical dissipation typical of second-order upwind schemes.
  - **Dissipation-free central schemes.** They are accurate to
    $t\approx12$, then pile energy up at the cutoff.
  - **Shock-capturing families.** Localized artificial diffusivity gives
    thick, oscillation-free shocks and the lowest dilatational dissipation.
    Local switching to a low-order scheme gives sharp but oscillating
    shocks on coarse grids, except TENO, which is sharp and
    oscillation-free at all resolutions. A high-order filter without shock
    capturing gives the strongest oscillations.
  - **Small scales.** DG, spectral difference and DGSEM capture the small
    scales well on coarse grids, as do high-order finite differences with
    high-order filtering. Finite differences with local switching and TENO
    "yield more small-scale dissipation" (§V).
  - **The authors' synthesis.** Shock capturing has "a low impact" on the
    turbulent scales overall (§V).
  - **Shock sharpening.** The first dilatational-dissipation peak is not
    converged even at $2048^3$, because shocks sharpen until molecular
    viscosity resolves them (§II.C).

  See [artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md),
  [subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md)
  and [WENO schemes](/methods/weno-scheme.md).
- **DG against finite volume in supersonic driven turbulence.**
  [Cernetic et al. (2024)](/sources/cernetic-2024.md) (§3.1, §5–7) find
  that a modal DG scheme with a von Neumann–Richtmyer viscosity at internal
  Gauss points extends the resolved range over second-order finite volume.
  - **Subsonic against supersonic.** The extension is large in subsonic
    driven turbulence and "nearly disappears" in supersonic turbulence.
    Below the sonic scale at $M=3.2$ it returns: DG at $512^3$ is "nearly
    as good as" finite volume at $1024^3$.
  - **Entropy at shocks.** The authors note that DG has no sub-cell entropy
    source at shocks, unlike finite volume, whose cell averaging produces
    entropy at every step. This is advantageous for advection and an
    impediment at shocks, hence the artificial viscosity.
  - **Bottleneck.** The lower dissipation of DG also gives a more
    pronounced [bottleneck](/definitions/bottleneck-effect.md).
  - **Cost.** With many shocks, their cost model expects orders 2–3 to be
    the "sweet spot" (§7).
- **Locality of the DG/finite-volume blending.** In the GPU code
  [GALÆXI](/software/galaexi.md), [Kurz et al. (2025)](/sources/kurz-2025.md)
  (§2.3, §5.2, §6.3) report two results.
  - **Supersonic Taylor–Green vortex.** With the same maximum blending
    factor at all resolutions, the solenoidal dissipation converges to the
    reference of Chapelier et al. at $512^3$ degrees of freedom.
  - **Rotor 37 cascade.** The finite-volume part is active only near the
    leading-edge shock, with blending factor $\alpha$ between 0.1 and 0.7,
    which keeps the scheme high order elsewhere.
- **Shock buffet damped by dissipation.** In implicit LES and URANS of a
  transonic compressor cascade, [Klose et al. (2025)](/sources/klose-2025.md)
  (§5–6, Table 2) find a maximum shock-oscillation amplitude of 0.072
  chords with URANS; 0.278, 0.172 and 0.158 with coarse LES at spans of 5,
  10 and 20% of the chord; and 0.231 with the refined LES at 10% span. The authors "assume that
  the increased numerical dissipation of the URANS and, to a lesser extent,
  the coarser LES, damps out flow structures that are driving the larger
  shock oscillations". In the coarse LES the shocklets appear more diffused
  "given the increased numerical dissipation" (§7.1).

Further sources keep the shock-capturing dissipation away from the
turbulent scales by design:

- **Shock capturing kept out of an under-resolved boundary layer.**
  [Gao et al. (2022)](/sources/gao-2022.md) (§1, §3.2) argue that
  shock-capturing dissipation spoils the turbulence: the finite-volume
  subcells of their DGSEM are more dissipative than DG in smooth regions,
  and a pressure-jump indicator on the instantaneous field flags large
  parts of the under-resolved turbulent boundary layer. Evaluating it on a
  spanwise-averaged field confines the subcells to the shocks (see
  [shock sensor](/definitions/shock-sensor.md) and
  [subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md)).
  At equal degrees of freedom their DG ($N=4$) is closer to the converged
  laminar interaction than second-order finite volume, and reaches the
  converged separation length with 182,000 degrees of freedom against
  409,500, at 7680 against 10,368 CPU-minutes (§4.1–4.2).
- **Sensor-switched artificial dissipation as the closure.** In the
  supersonic-jet [implicit LES](/definitions/implicit-les.md) of
  [Ahn et al. (2023)](/sources/ahn-2023.md) (§III, Eqs. 1–6) a modified
  Jameson second/fourth-difference dissipation, scaled by a Ducros-type
  dilatation sensor and applied once per time step at the end of the first
  Runge–Kutta stage, is both the shock capturing and the only subgrid
  dissipation; the authors read the rapid drop of their shear-layer
  spectra at high Strouhal number as the "maximum resolving performance"
  of grid and scheme (§IV C 1, Fig. 12).
- **Upwind background dissipation and quadratic invariants.**
  [Liang & Fu (2024)](/sources/liang-2024.md) (§1, §3.2) state that the
  dissipation of the background upwind linear scheme prevents classical
  WENO/TENO schemes from conserving quadratic invariants such as kinetic
  energy. Their TENO-S scheme uses a non-dissipative,
  [kinetic-energy-preserving](/properties/kinetic-energy-preservation.md)
  split-form flux in smooth cells and TENO only in troubled cells, flagged
  by an eight-point indicator. The TENO background scheme is optimized for
  dispersion with a small dissipation coefficient (0.01, so that the
  approximate dispersion relation holds), and its cutoff is adapted
  between $10^{-10}$ and $10^{-7}$ by a discontinuity-strength measure
  (§3.3, Eqs. 43–49). In the inviscid Taylor–Green vortex ($64^3$, to
  $t=100$) TENO-S conserves the kinetic energy while WENO-CU6, TENO6 and
  TENO8 dissipate it and smear the small vortices after $t\approx5$
  (§4.10, Figs. 17–18). [Li & Fu (2024)](/sources/li-2024-c.md) (§3.2.1,
  Eq. 47) adapt the same cutoff between $10^{-10}$ (high-wavenumber
  fluctuations) and $10^{-5}$ (discontinuities) in multiphase TENO schemes.
- **Dissipation at discontinuities.** [Takagi et al. (2022)](/sources/takagi-2022.md)
  (§1–2) note that TENO keeps the spectral properties of its linear scheme
  up to intermediate wavenumbers but that its stencil selection is
  dissipative at genuine discontinuities, and replace it there by the THINC
  jump reconstruction, which with steepness $\beta_{\mathrm{TH}}=1.6$
  (page-local) is anti-diffusive (positive
  imaginary part of the modified wavenumber in some ranges) and therefore
  unsuited to smooth scales; their hybrid preserves the kinetic energy of
  the inviscid Taylor–Green vortex ($64^3$) better than WENO5-Z and TENO5
  (§4.10, Fig. 21). Li & Fu (2024, §1, §4) use THINC against interface
  smearing in two-phase flow, with a first-order a posteriori fallback that
  stays below 0.04% of the cells in their hardest case (§4.8).
- **Limiters for discontinuous Galerkin.** [Huang & Fu (2024)](/sources/huang-2024.md)
  (§1, §6) and [Huang et al. (2025)](/sources/huang-2025.md) (§1, §3.2.1,
  §5) replace WENO-type limiters of third-order modal Runge–Kutta DG, which
  "may substantially smear the small-scale flow structures", by TENO and
  TENO–THINC limiters. In Huang et al. (2025) the limiter's cutoff
  ($10^{-5}$) directly sets the added dissipation, chosen "as a balance of
  the good numerical robustness and the low dissipation property", at
  172.08 s against 163.07 s for the WENO limiter on Lax's problem
  (Table 4). Both papers test inviscid problems only, and attribute the
  symmetry breaking of their
  two-dimensional Riemann and Rayleigh–Taylor solutions to dissipation too
  low to damp round-off (Huang & Fu 2024, §6.6; Huang et al. 2025, §5.7).

## Dissipation of compressible modes

When the only physical viscosity is shear viscosity, the compressible
(dilatational) velocity modes are damped by the scheme.
[Beattie et al. (2025)](/sources/beattie-2025.md) (§1, §6, App. D, §9.1)
show this in trans-sonic MHD turbulence with the finite-volume code FLASH
(MUSCL–Hancock, five-wave Riemann solver):

- without [bulk viscosity](/definitions/bulk-viscosity.md), compressible-mode
  decay is "governed completely by numerical dissipation", set by the flux
  discretization, the number of waves in the Riemann solver and the
  resolution;
- the compressible modes pile up at high wavenumbers in a
  [bottleneck](/definitions/bottleneck-effect.md);
- the run never converges in those modes, so that a nominal DNS is an
  [implicit LES](/definitions/implicit-les.md) for them.

An explicit bulk viscosity about ten times the shear viscosity removes the
pile-up and gives convergence at $512^3$.

[Cao et al. (2024)](/sources/cao-2024.md) (§1) rely on the scheme's
dissipation as the model in a gas-kinetic iLES: the "built-in numerical
dissipation acts as the subgrid-scale (SGS) dissipation". The paper gives
no measure of it.

## Too little dissipation

A scheme that conserves kinetic energy exactly and has no model does not
stay accurate:

- truncated-Euler and no-model runs thermalize towards a $k^2$
  equipartition spectrum. During the Taylor–Green breakdown the no-model LES
  overestimates the total dissipation: "a subdissipative operator leads
  eventually to an overdissipative behaviour" (Vicente Cruz & Lamballais
  2023, §6.2, Figs. 4–7);
- dissipation-free split-form DG is stable for severely under-resolved
  DHIT and gives a $k^2$ spectrum near the cutoff (Flad & Gassner 2017, §3,
  Fig. 4);
- high-order under-resolved DNS of the periodic hill shows spurious
  oscillations in second-order statistics, attributed by Dzanic et al.
  (2022, §3.1, Fig. 5) to aliasing and absent when an eddy viscosity is
  added;
- in the discretize-first LES of [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md)
  (§5.1.2, §5.2.4), the under-resolved second-order central scheme
  produces grainy high-wavenumber oscillations. The no-closure LES has too
  much energy at high wavenumbers; Smagorinsky corrects this, and the
  learned closure is trained to predict the oscillations as part of the
  discrete commutator error, instead of removing them by explicit
  filtering.

Dissipation-free schemes that are stable by construction behave
differently:

- nonlinearly stable (entropy-stable split-form) flux reconstruction runs
  the Taylor–Green vortex at $Re=1600$ down to $24^3$ degrees of freedom
  with no upwinding, over-integration or model, while strong-form DG
  without over-integration fails in transition (Brillon & Nadarajah 2026,
  §3.1.2–3.1.3, Figs. 8, 11). With a split form it costs about half the CPU
  time of over-integrated strong DG for $N=5$ to 12 (Fig. 12);
- [Kuya et al. (2018)](/sources/kuya-2018.md) (§5, Figs. 1–11) run
  non-dissipative second-order central split-form schemes on the inviscid
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) ($64^3$,
  $M_0=0.05$ and 0.4) and inviscid decaying isotropic turbulence ($32^3$,
  $M_{t0}=0.07$ and 0.3) with no added dissipation. Every variant with a
  divergence-form mass flux and quadratic-split momentum (DQ type) blows
  up, the consistent one included; of the quadratic–cubic (QC) variants
  only the one whose energy fluxes are consistent with the discrete
  kinetic- and internal-energy relations keeps total entropy and bounded
  density and temperature fluctuations. The inconsistent variants,
  including those of Jameson and Pirozzoli, reduce entropy and let the
  thermodynamic fluctuations grow. That the consistent DQ variant is
  unstable while the consistent QC one is not, the authors suggest "could
  partly be explained by the reduction of aliasing errors" of cubic split
  forms (§5.3; see
  [kinetic-energy preservation](/properties/kinetic-energy-preservation.md)
  and [entropy conservation](/properties/entropy-conservation.md)). Time
  integration matters too: third-order TVD Runge–Kutta, and the classical
  fourth-order one at CFL about 1, produce entropy (App. C);
- in DNS of compressible channel flow of a thermally perfect gas at bulk
  Mach numbers 3 to 5, run fully central after a WENO transient,
  [Aiello et al. (2026)](/sources/aiello-2026.md) (§3.3, §4.2, Fig. 3,
  Table 3) find that two schemes that conserve entropy discretely for this
  gas stay statistically stationary, while two kinetic-energy-preserving
  schemes that do not overpredict the thermodynamic fluctuations, which
  then drift; no shock capturing was needed with the entropy-conserving
  schemes. They add that coupling the other schemes to WENO-type
  hybridization may mitigate the problem "at the price" of dissipation
  (§4.2). See [entropy conservation](/properties/entropy-conservation.md);
- with kinetic-energy-preserving split forms and no filter or model,
  [Volpiani (2024)](/sources/volpiani-2024.md) (§4–5, Figs. 5, 11–13)
  finds the inviscid Taylor–Green vortex conserving kinetic energy
  (normalized energy 0.998–0.999 at $t=5$ on $64^3$) but the viscous one
  at $Re=1600$ "extremely noisy" on $64^3$ and $128^3$: aliased energy
  builds up at high wavenumber for every split form, consistent with
  aliasing beyond two thirds of the maximum wavenumber (as recalled from
  Johnsen et al.), and contaminates the low wavenumbers. An eddy viscosity
  does not remove it; a weak relaxation filter does (see
  [explicit modal filtering](/methods/explicit-modal-filtering.md));
- in a primitive-variable scheme for transcritical real-gas flow,
  [Xu et al. (2026)](/sources/xu-2026.md) (§3.5, §4.3, §5.1.4, Fig. 5) add
  an upwind dissipation scaled by the fifth-order interface jump, formally
  $O(\Delta x^4)$; without it the central update blows up in a 1D advection
  test.

At the other end, high-order RANS loses the stabilization that large
numerical dissipation gives low-order schemes at the wall and the
boundary-layer edge. [Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md)
(§1, §5.3–5.4, §7) state this for a hybridizable DG discretization of
$k$-$\omega$ models ($N=3$), see oscillations of $k$ and $\omega$ at the
boundary-layer edge and in an airfoil wake, and attribute part of a 2%
skin-friction overprediction on the flat plate to the leading-edge
singularity and the lower numerical dissipation of the finer leading-edge
mesh. They also expect the low
dissipation to make local-correlation transition modelling feasible on
coarser meshes. See [$k$-$\omega$ models](/methods/k-omega-model.md).
[Huang et al. (2022b)](/sources/huang-2022-d.md) (§2.4.1, Fig. 4) quantify
the trade in a fourth-order finite-volume RANS solver with variational
reconstruction: its leading dissipation is of order $(kh)^8$ ($O(h^7)$
in the modified wavenumber), and an unconstrained optimization of the
reconstruction weights, with a leading coefficient
$3.23\times10^{-3}$ against $2.24\times10^{-2}$ for the constrained one
(about seven times smaller, *compiler check, not in the sources*), gives schemes "not robust" in practice.
On the 30P-30N high-lift configuration the fourth-order scheme carries
the slat wake of high turbulent viscosity to the outlet, which the
second-order scheme dissipates quickly; on the NACA 0012 at $15^\circ$ the
second-order scheme predicts a trailing-edge separation absent at fourth
order (§3.2–3.3, Fig. 35; see
[NACA 0012 airfoil](/benchmarks/naca-0012-airfoil.md)).
[Lodares et al. (2022)](/sources/lodares-2022.md) (§4.4, §5.3) add all
dissipation of their entropy-stable Spalart–Allmaras DGSEM through the
interface fluxes: Lax–Friedrichs or matrix dissipation for the
Navier–Stokes part and an upwinding toggle for the Spalart–Allmaras
variable, all switched off for the entropy-conserving central variants
(see [entropy conservation](/properties/entropy-conservation.md)).

Polynomial de-aliasing (over-integration) and split forms are the two DG
remedies for aliasing. Flad & Gassner (2017, §3.1) find that with classic
Roe dissipation they give almost identical spectra. They conclude that the
failure of coarse DG ILES comes from the Riemann-solver dissipation, not
from the de-aliasing. [Krais et al. (2021)](/sources/krais-2021.md)
(§3.3) list both as stabilizations available in FLEXI. Split-form DG can be
made kinetic-energy-preserving or entropy-conserving by the choice of
two-point flux, with entropy-dissipative surface terms added.

## Numerical diffusion of flames

[Cuenot et al. (2022)](/sources/cuenot-2022.md) (§2–5, Tables 2–3,
Figs. 5–7, 9) measure numerical diffusion through a flame property. In
steady laminar counterflow diffusion flames at high Damköhler number the
consumption speed scales as $\sqrt{a_{\mathrm{cf}}D_{\mathrm m}}$
($a_{\mathrm{cf}}$ the counterflow strain rate, $D_{\mathrm m}$ the
diffusivity; page-local, as on the Source page), so on a coarse grid the
extra diffusion of the scheme raises it. With the first-order upwind
discretization of CANTERA, whose dissipation error the authors give as
$\sin(kh)/(kh)$ ($k$ the wavenumber, $h$ the grid step), at most a factor
$2/\pi$ at the highest discrete wavenumber (§4), the total heat release
of a methane–air flame (two-step chemistry,
$a_{\mathrm{cf}}=100\,\mathrm{s^{-1}}$) deviates from the reference for
flame resolutions $\delta_{\mathrm f}/h\le20$ ($\delta_{\mathrm f}$ the
thermal thickness, page-local) and rises by up to 65% at
$\delta_{\mathrm f}/h=2$ (as printed; see Qualifications). They define
an effective diffusivity ratio $F=D^*_{\mathrm m}/D_{\mathrm m}$ equal to
the square of the heat-release ratio (Eq. 14), with
$F=1.113$, 1.27, 1.505 and 2.575 at resolutions 20, 10, 6 and 2 (Table 2),
and 1.01 to 1.46 for a 14-species methane–oxygen flame at 54 bar
(resolutions 30 to 0.9, Table 3). Dividing all diffusivities by $F$ on the
coarse mesh recovers the reference consumption within 3% (two-step) and
2% (except the mesh with no point near stoichiometry), and about five
points in the reaction zone keep the inner chemical structure (§5). For
LES they propose $F_{\mathrm{LES}}=F_{\mathrm{num}}F_{\mathrm{sgs}}$
(§6; see [thickened flame model](/methods/thickened-flame-model.md)). The
evidence is one-dimensional and laminar.

## Grid-size changes

- **Refinement levels.** [Martin-Alvarez et al. (2022)](/sources/martinalvarez-2022.md)
  (§1, §2.1) argue that multi-level adaptive mesh refinement introduces
  numerical viscosity and resistivity at several scales, one per level, so
  that turbulent and magnetic energy is "dissipated significantly more than
  expected for the $\Delta x_{\max}$ employed" and small-scale structure is
  lost when gas moves to coarser levels. In cosmological zoom-in MHD with
  zero physical resistivity (RAMSES, constrained transport), their
  quasi-Eulerian refinement, which covers the galaxy with the finest level,
  gives faster [small-scale dynamo](/results/small-scale-dynamo.md) growth.
  Its growth rates "follow well" the reference scaling
  $\Gamma_E\propto Re^{1/2}\propto h_{\min}^{-1/2}$ drawn in Fig. 7 ($\Gamma_E$ the
  growth rate and $h_{\min}$ the finest cell size, as on the
  [small-scale dynamo](/results/small-scale-dynamo.md) page), the scaling for Kolmogorov turbulence with a
  numerical viscosity proportional to the cell size, whereas mass-based
  refinement follows about $h_{\min}^{-0.3}$ (§3.2, Fig. 7). They
  also state, citing other work, that constrained transport gives lower
  amplification than divergence cleaning because of "the high numerical
  diffusivity introduced by the numerical solver" (§1).
- **Resolution requirement.** With truncation-error dissipation, the
  critical Reynolds number of a turbulent dynamo becomes a grid requirement:
  [Liu et al. (2022)](/sources/liu-2022.md) (§1) estimate at least 30 pc
  for a 1 kpc thick galactic disc and about 3 pc for a 100 pc disc.
- **Fine-to-coarse interfaces.** Mozaffari et al. (2022, §1, Fig. 1, from an
  earlier thesis) show a detached-eddy simulation of decaying turbulence
  crossing a mesh-size doubling: the resolved kinetic energy drops at once,
  the modelled energy, whose dissipation term depends on the cell size,
  decays more slowly, and "the loss of resolved turbulence is never equal
  to the gain in modeled turbulence". They conclude that mesh-size changes
  should be avoided where possible, which motivates their averaged
  [mesh adaptation](/methods/mesh-adaptation.md). The mechanism they name is
  the cell-size-dependent dissipation term of the kinetic-energy equation
  of the [hybrid model](/definitions/hybrid-rans-les.md), which they call an
  "artificial dissipation term".

- **Mesh interfaces in turbomachinery LES.** In a wall-modelled LES of a
  fan stage, [Lewis et al. (2023)](/sources/lewis-2023.md) (§4.4.1,
  Fig. 26) see the rotor wake grow abruptly at the rotor/stator domain
  interface, where the coarser downstream mesh "enhances diffusion"; the
  jump disappears on the refined mesh except at 25% span, outside the
  interstage refinement block.

## Qualifications

- The quantitative statements above come from canonical periodic flows
  (DHIT, forced HIT, Taylor–Green vortex), one bluff body (cylinder at
  $Re_D=3900$) and the periodic hill, each with one scheme family. The
  astrophysical statements do not measure the numerical dissipation of
  their own runs: Martin-Alvarez et al. (2022) assume a numerical viscosity
  proportional to the cell size, Seta & Federrath (2022) take the numerical
  Reynolds number from earlier work, and Liu et al. (2022) give an
  order-of-magnitude estimate.
  [Duraisamy (2021)](/sources/duraisamy-2021.md) (§VII) states that
  disambiguating numerical from modelling errors in LES is hard, especially
  without explicit filtering, and recalls from Lund that even explicit
  filtering may not fully address it.
- Dang et al. (2022, §2.2.3) write that "the higher the values of
  $\theta_1$ and $\theta_2$, the higher is the dissipation of the hybrid
  scheme" ($\theta_1$, $\theta_2$ the two sensor thresholds, page-local).
  By their own switching rule, raising the thresholds sends more points to
  the low-dissipation upwind scheme, which lowers the dissipation
  *(compiler check, not in the sources)*; the rule also assigns the value
  $\theta=\theta_2$ to both WENO branches.
- Saini et al. (2023) print ranges that do not all agree: the abstract
  gives numerics 60–90% of the total, §5.2 gives 56–86% for the high-order
  runs (44% SVV share downstream); for the Taylor–Green vortex the summary
  gives 85–95% numerics for the high-order runs while §5.1 gives an SVV
  share of 10–20% for $8^3$ elements.
- Kou et al. (2023, §5) conclude that "both penalty terms enhance
  dissipation at high wavenumbers", while §3 describes the dissipation of
  the representative negative gradient penalty at high wavenumbers as
  "similar (or lower)" than standard upwind.
- Carlsson et al. (2023) give the scale-resolving range of $\kappa^{(4)}$
  as 1/512 to 1/1024 in §2.2.1 and as "1/512 or smaller" in §5.
- Caban et al. (2026) describe the first-derivative induced filter both as
  "non-dissipative" (§3.2.1) and as "dissipative … without inducing
  numerical diffusion" (abstract; "only dissipative … (not diffusive)",
  §5.1): the words differ, the statement of Eq. (27), that it changes only
  the phase speed, does not. Their effective Reynolds number (Eq. 42) is
  printed with $\log(E_d/E_0)$ although $E_d=E/E_0$ is already normalized;
  the printed numbers are consistent with $\log E_d$ (the energy halves by
  $t=3.772$, $\exp(-6\cdot49\cdot3.772/1600)\approx0.50$) *(compiler check,
  not in the sources)*.
- Brillon & Nadarajah (2026, §2.5) define $\nu_{\mathrm{eff}}<\nu$ as "less
  dissipative than it should be", then write (§3.1.1) that for $t^*>5$ the
  effective viscosity "is greater than 1 at all times except for" one scheme,
  which was therefore "more dissipative than it should be": by their own
  definition that scheme is the less dissipative one.

- Cuenot et al. (2022) print "+65%" for the coarsest two-step mesh, while
  their Eq. (14) and Table 2 ($F=2.575$) give a heat-release ratio of
  $\sqrt{2.575}=1.605$, +60.5%; they quote the Table 3 values 1.46 and
  1.12 as heat-release ratios, which by Eq. (14) are $F$, the ratios
  being 1.21 and 1.06; and their error relation
  $\varepsilon_{\mathrm{num}}=(F_{\mathrm{num}}^2-1)\dot\Omega_{\mathrm{exact}}$
  ($\dot\Omega$ the consumption rate, page-local) does not follow from
  Eq. (14), which gives the exponent $1/2$ *(compiler check, not in the
  sources)*. The text names M1000 as reference mesh while Table 2 and
  Fig. 6 use M500.
- Kumar & Ghosh (2022, §4) suggest that thresholds of 7–10 "may also show
  better performance" than WENO-CU6, while their §3.1.6 finds the
  three-point scheme unstable at threshold 7 in double Mach reflection.
  They print the WENO-BS linear weights as 1/35, 12/35, 8/35, 4/35
  (Eq. 50), which sum to 25/35 *(compiler check, not in the sources)*.

# Citations

- [Flad & Gassner (2017)](/sources/flad-2017.md) — §1; §3, Fig. 4; §3.1, Figs. 5–6; §4; §5, Figs. 8–9; §5.1, Fig. 10.
- [Beck & Kurz (2023)](/sources/beck-2023.md) — §V A–C, Figs. 4, 8, 11–12.
- [Dzanic et al. (2022)](/sources/dzanic-2022.md) — §3.1, Fig. 5; §3.2, Fig. 11; §4.
- [Goc et al. (2021)](/sources/goc-2021.md) — §2.3.
- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §5.1; §5.3, Fig. 1; §6.2–6.3; §6.5.
- [Krais et al. (2021)](/sources/krais-2021.md) — §3.3, Eqs. (52)–(54).
- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) — §II.B.
- [Haering et al. (2022)](/sources/haering-2022.md) — §V D; App. C.
- [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md) — §5.1.2; §5.2.4.
- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §VII.
- [Cao et al. (2022)](/sources/cao-2022.md) — §2.1, Remark 1; §3.1, Fig. 5.
- [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md) — §5.2, Figs. 2–3.
- [Seta & Federrath (2022)](/sources/seta-2022.md) — §2.4.
- [Pereira et al. (2021)](/sources/pereira-2021.md) — §IV.3.1, Eqs. (22)–(23).
- [Huang et al. (2022)](/sources/huang-2022.md) — §2.2.
- [Hoy & Bermejo-Moreno (2022)](/sources/hoy-2022.md) — §3.
- [Alauzet et al. (2022)](/sources/alauzet-2022.md) — §4.1.1; Figs. 42–43.
- [Gillyns et al. (2022)](/sources/gillyns-2022.md) — §2.
- [Mozaffari et al. (2022)](/sources/mozaffari-2022.md) — §1, Fig. 1; §5.1.
- [Basile et al. (2023)](/sources/basile-2023.md) — §1; §2.1.
- [Prakash et al. (2022)](/sources/prakash-2022.md) — §III.B.1, Fig. 4.
- [Martin-Alvarez et al. (2022)](/sources/martinalvarez-2022.md) — §1; §2.1; §3.2, Fig. 7.
- [Liu et al. (2022)](/sources/liu-2022.md) — §1.
- [Carlsson et al. (2023)](/sources/carlsson-2023.md) — §2.2.1; §2.3, Fig. 1; §4.2, Fig. 3; §4.3, Fig. 4; §4.4, Figs. 9–10; §5.
- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — §3.3; §4.1.
- [Helm & Martín (2022)](/sources/helm-2022.md) — §II; §III C, Fig. 8.
- [Dang et al. (2022)](/sources/dang-2022.md) — §1; §2.2.3.
- [Placco et al. (2023)](/sources/placco-2023.md) — §1; §2.
- [Cai et al. (2022)](/sources/cai-2022.md) — §II.A, Eqs. (7), (9).
- [Coelho et al. (2022)](/sources/coelho-2022.md) — p. 4.
- [Davidovits et al. (2022)](/sources/davidovits-2022.md) — §II A.
- [Kou et al. (2023)](/sources/kou-2023.md) — §1; §2.1–2.2; §3, Figs. 1–4, Table 1; §4.2, Fig. 12; §5; App. A.
- [Lederer et al. (2023)](/sources/lederer-2023.md) — §3.2–3.3, Figs. 2–3, 10; §4.1, Figs. 4, 6, Table 2; §6.
- [Zhao et al. (2023b)](/sources/zhao-2023-b.md) — §1.
- [Saini et al. (2023)](/sources/saini-2023.md) — Abstract; §2.2–2.3, Eqs. (2)–(12); §4, Figs. 5–6; §5.1–5.2, Figs. 7–16; §6.
- [Zhao et al. (2023a)](/sources/zhao-2023.md) — §5.1, Eqs. (22)–(23), Fig. 7.
- [Foldes et al. (2023)](/sources/foldes-2023.md) — §4.3, Eqs. (4.7)–(4.9), Figs. 6–9; §4.4, Fig. 11.
- [Delassaux et al. (2023)](/sources/delassaux-2023.md) — §4.2; §5.
- [Moratilla-Vega et al. (2024)](/sources/moratillavega-2024.md) — §2.1, Eq. (6); §4.3–4.4, Figs. 12–13, 18.
- [Bernades et al. (2023)](/sources/bernades-2023.md) — §1, footnote 1; §4.1, Fig. 1; §4.2.
- [Slaughter et al. (2023)](/sources/slaughter-2023.md) — §3; §3.1.
- [Morsbach et al. (2024)](/sources/morsbach-2024.md) — §2.
- [Kurz et al. (2023)](/sources/kurz-2023.md) — §1; §4.2.
- [Lewis et al. (2023)](/sources/lewis-2023.md) — §4.4.1, Fig. 26.
- [Wang (2024)](/sources/wang-2024-b.md) — §2.2; §2.4.2; §4.2, Fig. 6; §4.3.2, Figs. 15–17, Tables 7–8; §4.4.3.
- [Wang et al. (2024)](/sources/wang-2024.md) — §1; §2.3–2.5, Table 1; §3.1–3.3, Figs. 2–6, Table 2; §5.
- [Kim et al. (2024)](/sources/kim-2024.md) — §2.1; §4.2.1, Fig. 9.
- [Prieto Saavedra et al. (2024)](/sources/prietosaavedra-2024.md) — §3.1, Eqs. (8)–(10); §4.2, Table 5.
- [Ruan et al. (2023)](/sources/ruan-2023.md) — §2.
- [Duan & Wang (2024)](/sources/duan-2024.md) — §1, Figs. 1–2; §3; §5.1, Figs. 5–6.
- [Domaradzki (2024)](/sources/domaradzki-2024.md) — §3.3.
- [Wang et al. (2023c)](/sources/wang-2023-c.md) — §II.A.
- [Möller et al. (2024)](/sources/moller-2024.md) — accepted manuscript: §II.C, Eq. (26); §II.D; §III.B.3, Figs. 19–22.
- [Maejima & Kawai (2025)](/sources/maejima-2025.md) — §4.
- [Reddy et al. (2026)](/sources/reddy-2026.md) — preprint of 4 March 2021: §1; §7.1.
- [Mukha et al. (2025)](/sources/mukha-2025.md) — arXiv v1: §II.B; §III.C, Figs. 6–8; §V.
- [Chapelier et al. (2024)](/sources/chapelier-2024.md) — HAL accepted manuscript: §II.C, Figs. 2–4; §III.A–B; §IV.A–B, Figs. 5–8; §V.
- [Cernetic et al. (2024)](/sources/cernetic-2024.md) — arXiv v2: §3.1; §5, Fig. 5; §6, Figs. 8, 10–11; §7.
- [Kurz et al. (2025)](/sources/kurz-2025.md) — arXiv v2: §2.3, Eq. (21); §5.2, Fig. 11; §6.3, Fig. 13.
- [Klose et al. (2025)](/sources/klose-2025.md) — ASME accepted manuscript: §6, Table 2; §7.1.
- [Beattie et al. (2025)](/sources/beattie-2025.md) — arXiv v4: §1; §6.1–6.2, Fig. 9; §9.1; App. D.
- [Cao et al. (2024)](/sources/cao-2024.md) — arXiv v1: §1.
- [Brillon & Nadarajah (2026)](/sources/brillon-2026.md) — arXiv v1: §2.5, Eqs. (37), (45), (96)–(100), (105); §3.1.1, Figs. 2–4; §3.1.2–3.1.3, Figs. 8, 11–12; §3.1.5, Fig. 14, Table 5; §3.1.7, Figs. 17–18; §3.1.8, Figs. 19–20.
- [Caban et al. (2026)](/sources/caban-2026.md) — §3.2.1, Eqs. (24)–(29); §3.2.2, Eqs. (34)–(35); §4.1, Fig. 5; §5.1, Eq. (42), Figs. 10–11; §5.3.1, Figs. 18–20, Table 4; §5.4.2, Tables 7–9; §6.
- [Lederer et al. (2026)](/sources/lederer-2026.md) — arXiv v1: §3–3.2; §4, Table 2, Figs. 4, 7–9; §5.
- [Ranjbar et al. (2026)](/sources/ranjbar-2026.md) — arXiv v1: §I; §III.A, Fig. 3; §III.C, Fig. 15; §III.D.2–III.D.4, Fig. 18.
- [Wu & Lele (2026)](/sources/wu-2026.md) — arXiv v2: §1; §3.2.2; §5–6, Tables 3–4.
- [Aiello et al. (2026)](/sources/aiello-2026.md) — §3.3; §4.2, Fig. 3, Table 3.
- [Xu et al. (2026)](/sources/xu-2026.md) — arXiv v1: §3.5; §4.3; §5.1.4, Fig. 5.
- [Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md) — §1; §5.3–5.4; §7.
- [Wang et al. (2021)](/sources/wang-2021-l.md) — §2.3; §3.1, Fig. 1; App. A, Eqs. (A.1)–(A.2); App. B.
- [Yang & Ma (2022)](/sources/yang-2022-b.md) — §2.3, Eq. (6); §3.1, Fig. 4; §3.2, Fig. 7.
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §3.1, Fig. 1; §4, Figs. 4–7; §5.2.3, Fig. 11.
- [Gao et al. (2022)](/sources/gao-2022.md) — §1; §3.2; §4.1–4.2.
- [Ahn et al. (2023)](/sources/ahn-2023.md) — §III, Eqs. (1)–(6); §IV C 1, Fig. 12.
- [Liang & Fu (2024)](/sources/liang-2024.md) — §1; §3.2–3.3, Eqs. (43)–(49); §4.10, Figs. 17–18.
- [Li & Fu (2024)](/sources/li-2024-c.md) — §1; §3.2.1, Eq. (47); §4; §4.8.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §1–2; §4.10, Fig. 21.
- [Huang & Fu (2024)](/sources/huang-2024.md) — §1; §6; §6.6.
- [Huang et al. (2025)](/sources/huang-2025.md) — §1; §3.2.1; §5; §5.7; Table 4.
- [Volpiani (2024)](/sources/volpiani-2024.md) — §2.2.2; §4, Table 1, Fig. 5; §5, Figs. 11–13.
- [Huang et al. (2022b)](/sources/huang-2022-d.md) — §2.4.1, Fig. 4; §3.2–3.3, Fig. 35.
- [Lodares et al. (2022)](/sources/lodares-2022.md) — §4.4; §5.3.
- [Batther & Lee (2022)](/sources/batther-2022.md) — §3.1.2; §5.
- [Wang et al. (2013)](/sources/wang-2013.md) — §1; §5.6, Figs. 25–27.
- [Han et al. (2022)](/sources/han-2022-c.md) — §4, Figs. 12, 17–24; §4.2.
- [Sugaya & Imamura (2021)](/sources/sugaya-2021.md) — §4.5, Tables 6–7, Figs. 18–19.
- [Kumar & Ghosh (2022)](/sources/kumar-2022-b.md) — §1; §3.1.3–3.1.7, Tables 1–2; §3.2; §4; Eq. (50).
- [Maltsev et al. (2022)](/sources/maltsev-2022.md) — §IV, Table I.
- [Zhao et al. (2021)](/sources/zhao-2021-c.md) — Abstract; §IV; §VI; Apps. A–B.
- [Li et al. (2021)](/sources/li-2021.md) — §II A; §III C.
- [Kuya et al. (2018)](/sources/kuya-2018.md) — §5, Figs. 1–11; App. C.
- [Cuenot et al. (2022)](/sources/cuenot-2022.md) — §2–6, Eq. (14), Tables 2–3, Figs. 5–7, 9.
- [Liu et al. (2022b)](/sources/liu-2022-g.md) — §1.
