---
type: Method
title: "Subgrid velocity enrichment"
description: "Hausmann et al.'s model reconstructs an approximate subgrid velocity field during LES by evolving Fourier modes under the linearized subgrid momentum equation, with an RNG viscosity for the dropped nonlinear term and stochastic forcing towards Yoshizawa's subgrid energy, at about twice the LES cost."
status: established
aliases: [velocity enrichment model, SGS velocity enrichment, subgrid-scale velocity reconstruction, LES-E, enriched LES]
tags: [les, sgs-model, filtering]
timestamp: 2026-10-27T20:40:00Z
---

# Subgrid velocity enrichment

A **subgrid velocity enrichment** model produces, alongside an LES, an
approximate unresolved velocity $u^{<}_i$ that is added to the filtered
velocity, $u_i\approx\bar u_i+u^{<}_i$. It does not replace the closure of
the [subgrid stress](/definitions/large-eddy-simulation.md): the LES runs
with its own subgrid model, and the enrichment is evaluated on the fly for
applications that need the small-scale velocity itself.
[Hausmann et al. (2022)](/sources/hausmann-2022.md) (§I) list dispersed
multiphase flows (multi-particle statistics, clustering, droplet
deformation), dual-scale interface methods, wind-turbine loads, flame-front
location and turbulent mixing. Their model, the subject of this page,
evolves a truncated Fourier series of $u^{<}_i$ under a linearized subgrid
momentum equation; the energy it adds to the subgrid scales is not required
to equal the energy the LES model removes, so the enrichment is
independent of the subgrid stress model (§II A).

## From the exact subgrid equation to the model

Subtracting the filtered from the unfiltered incompressible Navier–Stokes
equations gives the exact subgrid momentum equation (Hausmann et al. 2022,
§II A, Eqs. 7–8; kinematic pressure),

$$\partial_tu^{<}_i+u^{<}_j\partial_ju^{<}_i+\bar u_j\partial_ju^{<}_i+u^{<}_j\partial_j\bar u_i=-\partial_ip^{<}+\nu\partial_j\partial_ju^{<}_i+\partial_j\tau_{ij}+s^{<}_i,$$

with $s^{<}_i$ (page-local) the subgrid part of the momentum source. The
authors name its three advection terms non-linear relaxation
($u^{<}_j\partial_ju^{<}_i$), sweeping ($\bar u_j\partial_ju^{<}_i$) and
straining ($u^{<}_j\partial_j\bar u_i$); without the non-linear term the
equation is that of rapid distortion theory (cited). The model (Eqs. 13–14)
keeps sweeping and straining, replaces the non-linear relaxation by a
spatially uniform wavenumber-dependent viscosity, and replaces the
divergence of the subgrid stress by a stochastic forcing $f_i$:

$$\partial_tu^{<}_i+\bar u_j\partial_ju^{<}_i+u^{<}_j\partial_j\bar u_i=-\partial_ip^{<}+\big(\nu+\nu^{\mathrm{RNG}}_t\big)\partial_j\partial_ju^{<}_i+f_i,\qquad \partial_iu^{<}_i=0 .$$

The viscosity $\nu^{\mathrm{RNG}}_t(k)$ is the renormalization-group form
cited from Canuto & Dubovikov, with constant $C_\nu=2/5$ (page-local); its
printed formula and sign are discussed on the
[spectral eddy viscosity](/methods/spectral-eddy-viscosity.md) page. The
authors cite Laval et al. for the two effects that the viscosity is meant
to compensate: without the non-linear relaxation the subgrid spectrum is
overestimated and the field is too intermittent.

## Fourier representation and update

The subgrid velocity is a truncated Fourier series with time-dependent
vector coefficients (Eq. 12),

$$\boldsymbol u^{<}=\sum_{m=0}^{N_m-1}\Big[\boldsymbol A_m(t)\cos(\boldsymbol k_m\cdot\boldsymbol x)+\boldsymbol B_m(t)\sin(\boldsymbol k_m\cdot\boldsymbol x)\Big],\qquad \boldsymbol k_m\cdot\boldsymbol A_m=\boldsymbol k_m\cdot\boldsymbol B_m=0,$$

with $N_m$ modes of wavevector $\boldsymbol k_m$ ($N_m$, $\boldsymbol k_m$,
$\boldsymbol A_m$, $\boldsymbol B_m$ page-local). This is the representation
of **kinematic simulation**, but there the coefficients are random with a
prescribed spectrum, statistically homogeneous and stationary with unclear
time correlation, whereas here they evolve with the model equation (§II C).
Inserting the series gives an explicit Euler predictor for each mode,
without summation over $m$ (Eqs. 15–16):

$$\frac{A^*_{m,i}-A^n_{m,i}}{\Delta t}+\bar u^n_jk_{m,j}B^n_{m,i}+A^n_{m,j}\partial_j\bar u^n_i=-(\nu+\nu^{\mathrm{RNG}}_t)\lvert\boldsymbol k_m\rvert^2A^n_{m,i}+f_{m,i},$$

and the same for $\boldsymbol B_m$ with $-\bar u^n_jk_{m,j}A^n_{m,i}$ and a
forcing $g_{m,i}$; a spectral projection then removes the component along
$\boldsymbol k_m$,
$\boldsymbol A^{n+1}_m=\boldsymbol A^*_m-\boldsymbol k_m(\boldsymbol k_m\cdot\boldsymbol A^*_m)/\lvert\boldsymbol k_m\rvert^2$
(Eqs. 17–18), derived in the appendix from a spectral pressure Poisson
equation. Without a non-linear term the modes do not exchange information,
so the cost is linear in $N_m$ and the update parallelizes over
wavenumbers without communication (§II C, §II D).

**Forcing.** The forcing directions are random on the unit sphere and
correlated in time by an Ornstein–Uhlenbeck-like recursion,
$\boldsymbol V^n_m=a_m\boldsymbol V^{n-1}_m+\sqrt{1-a_m^2}\,\boldsymbol V_{m,0}$
with $a_m=\exp(-\Delta t\,\omega_{E,m})$ and
$\omega_{E,m}=\sqrt{\lvert\boldsymbol k_m\rvert^3E(\lvert\boldsymbol k_m\rvert)}$
the eddy-turnover rate of the mode (Eqs. 19–22; $\boldsymbol V_m$, $a_m$,
$\omega_{E,m}$ page-local), with independent directions for $f$ and $g$.
These directions are not divergence-free, like the divergence of the
subgrid stress whose role they take; the ideal direction, that of
$\partial_j\tau_{ij}$, is not available (§II C). The magnitude drives the
subgrid energy of the modes,
$k^{\mathrm{act}}_{\mathrm{sgs}}=\tfrac14\sum_m(\lvert\boldsymbol A_m\rvert^2+\lvert\boldsymbol B_m\rvert^2)$,
towards a target $k^{\mathrm{tgt}}_{\mathrm{sgs}}$ (both page-local) with a
relaxation factor $(\sqrt{k^{\mathrm{tgt}}_{\mathrm{sgs}}}-\sqrt{k^{\mathrm{act}}_{\mathrm{sgs}}})/(\Delta t\sqrt{k^{\mathrm{tgt}}_{\mathrm{sgs}}})$
and an inertial-range shape $\lvert\boldsymbol k_m\rvert^{-5/6}$ (Eqs.
24–27). The target is Yoshizawa's algebraic estimate
$k^{\mathrm{tgt}}_{\mathrm{sgs}}=C_I\Delta^2\lvert\bar S\rvert^2$ with
$C_I=0.0826$ (Eq. 28; see
[one-equation subgrid kinetic-energy models](/methods/subgrid-kinetic-energy-equation-model.md)
for its relation to transported $k_{\mathrm{sgs}}$ and for the other value
of $C_I$ in the bundle). The mode spectrum is
$E(\lvert\boldsymbol k_m\rvert)=(\lvert\boldsymbol A_m\rvert^2+\lvert\boldsymbol B_m\rvert^2)/(4\Delta k_m)$
(Eq. 23).

## Inhomogeneous flows: sub-domains

To represent inhomogeneous statistics, a distinct set of coefficients is
evolved on each cell of a structured grid of **sub-domains** coarser than
the LES grid (§II D, Eqs. 29–30). The LES velocity and velocity gradient in
the predictor are sub-domain averages, and extra terms with the spatial
derivatives of the coefficients appear; the target energy is taken at one
cell, the sub-domain centre, because averaging Gaussianizes its PDF
(Fig. 3). The algorithm per LES step is: LES step, sub-domain averages and
energy target; independent explicit mode updates per sub-domain; evaluation
of $\bar u_i+u^{<}_i$ where needed (Fig. 1). Only the averaging changes on
unstructured LES grids. An optional sigmoid interpolation between
sub-domains with a tangential correction velocity, chosen per mode to
minimize its magnitude, makes the field continuous and divergence-free
except where four sub-domains meet (§II E, Eqs. 31–37, Fig. 2); the results
of the paper are computed **without** it, and the PDFs of the second
invariant with and without it almost coincide (Fig. 11).

## Results

Both tests use a second-order finite-volume LES against the authors' own
DNS (§III):

- **Forced isotropic turbulence** ([isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md),
  $Re_\lambda=75$; DNS $256^3$; LES $32^3$ with
  [Smagorinsky](/methods/smagorinsky-model.md) $C_s=0.1$; standard
  enrichment $8^3$ sub-domains of $4^3$ LES cells, $N_m=100$, $C_\nu=0.4$).
  The subgrid spectrum computed from the coefficients coincides well with
  the DNS beyond the LES cutoff, so LES plus enrichment recovers the whole
  DNS range; a discrete Fourier transform of the sampled, discontinuous
  field would add spurious content (§IV A, Fig. 8). The PDFs of
  longitudinal and transverse velocity gradients become much wider than
  those of the LES, close to the DNS except in the extreme tails, but the
  skewness of the longitudinal-gradient PDF is not reproduced (Fig. 9). The
  PDF of the second invariant $Q_A$ (registry symbol, here of the enriched
  field) widens towards the DNS but stays less skewed (Fig. 10). The
  authors explain the non-Gaussian gradients, despite Gaussian forcing, by
  the non-Gaussian energy target across sub-domains and by the
  intermittency that sweeping and straining produce (§IV A). Writing
  $Q_A=-\tfrac12\partial_i\partial_j(u_iu_j)$ and splitting
  $u_iu_j=\bar u_i\bar u_j+(\bar u_iu^{<}_j+u^{<}_i\bar u_j)+u^{<}_iu^{<}_j$,
  the non-local cross terms are represented by the model and the
  $u^{<}_iu^{<}_j$ part is not; improving $Q_A$ would need the non-linear
  relaxation and a modified forcing (Eqs. 53–54).
- **Sensitivity** (Fig. 10). The $Q_A$ PDFs almost coincide for $8^3$,
  $16^3$ and $32^3$ sub-domains (the number matters only in inhomogeneous
  flows), show no trend for $N_m\ge100$ (200 and 400 tested) and change
  little when $C_\nu$ is varied by a factor of 16 (0.1 to 1.6). Multiplying
  the energy target by 1.5 and 2.0 widens the tails without changing the
  shape, so the conclusion that tuning parameters are insignificant does
  not extend to the energy level.
- **Cost** (Table III, per reference time, hardware not stated): LES
  $32\times10^3$ s, LES with enrichment $69\times10^3$ s, DNS
  $340\times10^6$ s. The enrichment about doubles the LES cost; the
  authors call the DNS "approximately four orders of magnitude" costlier,
  a ratio of about $4.9\times10^3$ *(compiler check, not in the sources)*.
- **Sinusoidally forced periodic shear flow** ($Re_{\mathrm{shear}}=3115$
  on the forcing velocity and box size; DNS $128^3$; LES $16^3$ with the
  [Vreman model](/methods/vreman-model.md); sub-domains equal to the LES
  cells). The generated subgrid velocity is inhomogeneous, with correlation
  extrema located as in the DNS, and anisotropic, with a non-zero shear
  correlation of DNS-like trend and the other off-diagonal correlations
  zero, stepwise across sub-domains (§IV B, Fig. 12b). It does not correct
  the LES's over-predicted mean velocity amplitude, because the subgrid
  energy is small (Figs. 6, 12a).

Wall-bounded flows are outside the scope of the paper (§III).

## Relation to other reconstructions

Hausmann et al. (§I) set their model against other ways of supplying the
subgrid velocity: fractal interpolation of Scotti & Meneveau, which "does
not incorporate important physical properties of turbulence"; kinematic
simulation, with a spatially constant spectrum and unclear time evolution;
the deconvolution and estimation methods of Domaradzki and of Park et al.,
the latter with no length scales below the LES cutoff; the spectrally
enriched model of Bassenne et al., which projects on a DNS-like grid at a
cost "of the order of a DNS"; the
[variational multiscale method](/methods/variational-multiscale-method.md)
and multilevel methods, with a large overhead; and the Gabor-mode
enrichment of Ghate & Lele, which needs mode quenching for long times (all
cited). Deconvolution of the resolved field towards the subgrid scales is
the subject of the [scale-similarity models](/methods/scale-similarity-model.md);
the enrichment instead integrates its own equation.

## Qualifications

- **Printed slips in the carrier LES and diagnostics.** Hausmann et al.
  print the combined viscous and subgrid flux of their LES equation
  (Eq. 39) with a factor $\tfrac12$ in front of
  $(\nu+\nu_t)(\partial_j\bar u_i+\partial_i\bar u_j)$, which halves both
  terms relative to their own Eqs. (5) and (9) *(compiler check, not in the
  sources)*; and they print Eq. (54) without the factor $-\tfrac12$ that
  follows from their Eq. (53) and incompressibility, as written above
  *(compiler check, not in the sources)*. The printed RNG viscosity
  (Eq. 11) is non-positive as written, against the text (see
  [spectral eddy viscosity](/methods/spectral-eddy-viscosity.md)). They
  call $\sqrt{\lvert\boldsymbol k_m\rvert^3E}$ an "eddy-turnover time"
  while it has the dimension of an inverse time and is used as a rate in
  the exponent *(compiler check, not in the sources)*.
- **Evidence.** The insensitivity to the tuning parameters rests on
  $Q_A$ PDFs in isotropic turbulence; the shear-flow test shows qualitative
  inhomogeneity and anisotropy, not a quantitative match.

# Citations

- [Hausmann et al. (2022)](/sources/hausmann-2022.md) — §I; §II A–F, Eqs. (7)–(37), Figs. 1–3; Appendix, Eqs. (A1)–(A13); §III; §IV A, Figs. 8–11, Table III; §IV B, Figs. 6, 12; Eqs. (39), (53)–(54).
