---
type: Method
title: "Subcell finite-volume shock capturing for DG"
description: "Troubled DG elements are recomputed as (N+1)^3 finite-volume subcells with the same degrees of freedom, switched by an indicator or blended convexly with the DG operator (the blend also learned as an implicit subgrid model); indicator-switched modal and entropy filters are the alternative that keeps the polynomial."
status: established
aliases: [hybrid DG/FV, DG/FV subcell scheme, finite-volume subcell limiting, DG/FV blending, RL-Blend, local modal filter, LMF, entropy filter]
tags: [shock-capturing, dg, numerical-dissipation, implicit-les, reinforcement-learning, compressible, flux-reconstruction]
timestamp: 2026-10-27T10:59:00Z
---

# Subcell finite-volume shock capturing for DG

**Subcell finite-volume (FV) shock capturing** stabilizes a
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md) near
discontinuities by reinterpreting a troubled element of degree $N$ as
$(N+1)^d$ FV subcells carrying the same number of degrees of freedom, advanced
with a robust low-order (first- or second-order TVD) FV scheme. Two variants
appear in the sources: the **switching** scheme of the FLEXI group, in which an
element is either DG or FV ([Krais et al. 2021](/sources/krais-2021.md)), and
the **convex blending** of DG and FV operators of Hennemann et al., which
[Beck & Kurz (2023)](/sources/beck-2023.md) reinterpret as an implicit
subgrid-scale model.

## Switching hybrid DG/FV (FLEXI)

Krais et al. (2021, §2.2.3, §4, §5.7) describe the group's scheme:

- **Subcells.** In reference space the element is cut into $N+1$ equispaced
  subcells per direction of width $h_{\mathrm{sub}}=2/(N+1)$ (page-local), so
  $h_{FV}=h_{DG}/(N+1)$ in physical space; data structures and the number of
  degrees of freedom are shared with DG, which balances the cost per element.
- **Conservative transfer.** The subcell means are the integrals of the DG
  polynomial over each subcell, evaluated with $N+1$ quadrature nodes
  $\xi^k_\lambda$ mapped into subcell $k$:
  $$U^{FV}_k=\sum_{i=0}^{N}\Big(\frac12\sum_{\lambda=0}^{N}w_\lambda\,\ell_i(\xi^k_\lambda)\Big)U_i,\qquad U^{FV}=V_{DG\to FV}\,U,$$
  and the backward transfer uses $V_{FV\to DG}=V_{DG\to FV}^{-1}$ (Eqs. 57–63).
- **FV operator.** A block-structured FV update on the subcells, with the
  subcell Jacobian integrated by the midpoint rule (Eq. 64); second order by
  TVD-limited reconstruction of primitive variables. At DG/FV interfaces the
  DG face data are converted to FV points by the face version of
  $V_{DG\to FV}$, the flux is computed pointwise and transferred back (§4.2).
- **Indicator and hysteresis.** A priori troubled-cell indicators of
  Persson–Peraire, Jameson–Schmidt–Turkel or Ducros type are evaluated at the
  start of each step; an element switches to FV above an upper threshold and
  back to DG below a lower one. The two-threshold band prevents back-and-forth
  switching and reduces sensitivity to the user value; the authors state that
  "numerical studies have shown" this without data (§4.3). A posteriori
  (MOOD-like) indicators are mentioned as the alternative.
- **Time step.** The FV subcells obey
  $\Delta t\le\mathrm{CFL}\,c^{c}_{RK}(0)\,h_{FV}/\lambda^c$ (Eq. 67, factor as on
  the DGSEM page), a weaker restriction than the DG one, so the DG step governs.

**Demonstrations.** In a stationary $M=1.5$ shock interacting with a vortex
(Euler, $200\times100$ cells, fifth order, entropy-conserving Chandrashekar flux
in DG cells, JST-type pressure indicator) the FV subcells stay confined to the
shock, no spurious waves are emitted and the vortex survives past the shock
because DG is used downstream (Krais et al. 2021, §7.2, Fig. 25); 2D Riemann
problems are shown in Fig. 9.

**Cost.** In strong-scaling tests with half the domain DG and half FV, the
hybrid operator performs about 15–20% worse than pure DG and shows weaker or no
super-linear speed-up, attributed to the extra memory of the FV operator (FV
metrics, inner-face geometry, subcell distances) (§5.8). FV cells send twice the
DG data at partition boundaries (cell mean plus slope) and the slope
computation overlaps the volume integral to hide communication (§5.7).

## Convex DG/FV blending as an implicit closure

In the scheme of Hennemann et al. (as recalled by Beck & Kurz 2023, §III C,
Eq. 16), originally a provably entropy-stable subcell shock capturing for
split-form DG, each element evolves by a convex combination
$$\frac{\partial U}{\partial t}=(1-\alpha)R_{DG}(U)+\alpha R_{FV}(U),\qquad\alpha\in[0,1],$$
with $\alpha=0$ pure DG and $\alpha=1$ a compatible low-order TVD FV scheme on
subcells whose widths equal the LGL quadrature weights $w_i$ (Fig. 4). The
scheme is conservative and consistent, and elements can be blended
independently because the face fluxes coincide for DG and FV.

Beck & Kurz (2023, §III C, §V C) set $\alpha$ per element with a
[reinforcement-learning](/methods/reinforcement-learning-closure.md) policy
("RL-Blend", actions mapped to $\alpha\in[0,0.5]$) and use it as an
[implicit LES](/definitions/implicit-les.md) model, which they state had "not
been interpreted as a possible implicit SGS model alternative yet". In forced
[isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md) at 36
degrees of freedom per direction and $N=5$, pure DG is under-dissipative, pure
FV over-dissipative, and the learned blending matches the DNS spectrum closely
(Fig. 12); its rewards are comparable to those of the learned explicit
Smagorinsky closures. The authors explain the success by the location of the
dissipation: FV dissipation is concentrated at the element centre, where the LGL
subcells are largest, the inverse of DG dissipation at the faces, so blending
can homogenize the total (§V C); the explanation is stated, and the
dissipation distribution is not measured. The agent lowers $\alpha$ for $N=3$ and raises its mean for $N=5$
(Figs. 13–14). See [discretization-consistent closure](/definitions/discretization-consistent-closure.md)
and [numerical dissipation](/properties/numerical-dissipation.md).

## Alternatives that keep the polynomial

Not every DG code uses subcells. [HORSES3D](/software/horses3d.md) captures
shocks with an entropy-stable artificial viscosity filtered by a spectral
vanishing viscosity kernel and switched by an element-wise density-gradient
sensor $\int_{\mathrm{el}}\mathcal J|\nabla_\xi\rho|^2$ (page-local
$\mathcal J$ the Jacobian of the element map, $\nabla_\xi$ the
reference-space gradient), which adds
unfiltered dissipation in troubled elements; a Mach 3 forward-facing step on
3653 elements with $N=7$ is shown ([Ferrer et al. 2023](/sources/ferrer-2023.md),
§4.4, Eqs. 15–19, Fig. 9, from the work of
[Mateo-Gabín et al. 2022](/sources/mateogabin-2022.md), who contrast it
with order-lowering subcell approaches; see the
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md) page).
In the authors' comparison table of high-order codes (Ferrer et al. 2023,
§2, Table 1), shock capturing is ticked for both HORSES3D and Flexi/Fluxo.

## Indicator-switched modal and entropy filters

A third family keeps the polynomial and damps it instead.
[Wang (2024)](/sources/wang-2024-b.md) stabilizes implicit LES of
turbomachinery with the [flux-reconstruction](/methods/flux-reconstruction.md)
solver ATHOS, whose correction functions recover nodal DG on LGL points, by
two solution filters applied after every Runge–Kutta stage (§2.3, App. A,
Algorithm 1). Page-local symbols: $\vartheta_m\in[0,1]$ the normalized index
of Legendre mode $m$, $\vartheta_c$ the filter cutoff, $\alpha_f$ the filter
strength and $s_f$ its order (the source's $\eta$, $\eta_c$, $\alpha$, $s$,
renamed to avoid the Kolmogorov length and the blending factor); $s_e$ the
Persson–Peraire indicator of an element and $s_0$ its activation threshold;
$\mathcal S=\rho\ln(p\rho^{-\gamma})$ the entropy function and
$\epsilon_{\mathcal S}$ its tolerance.

**Local modal filter (LMF).** The exponential modal filter of Hesthaven and
Warburton, $\mathcal V\Lambda\mathcal V^{-1}$ with
$$\Lambda_{mm}=\begin{cases}1,&\vartheta_m<\vartheta_c,\\ \exp\!\Big[-\alpha_f\Big(\dfrac{\vartheta_m-\vartheta_c}{1-\vartheta_c}\Big)^{s_f}\Big],&\vartheta_c<\vartheta_m<1,\end{cases}$$
(Eqs. 17–18; $\alpha_f=36$, printed as $-\log_{10}$ of double-precision machine
epsilon; it equals $-\ln$ of it *(compiler check, not in the sources)*, and $s_f=6$ throughout, §4.2; the cutoff value used is not printed)
is applied only in elements whose density smoothness indicator
$$s_e=\log_{10}\frac{(\rho-\rho_{N-1},\,\rho-\rho_{N-1})_e}{(\rho,\rho)_e}$$
(Eq. 19, $\rho_{N-1}$ the truncation of the density to degree $N-1$, the
$L_2$ inner product over the element) satisfies $s_e\ge s_0$. The Persson–Peraire
indicator is one of the a priori indicators listed for the FLEXI switching
scheme above; here it switches a filter instead of subcells. The only
tuning parameter is $s_0$. Starting from the
Li–Wang classification centred at $-C_0\ln N$ with $C_0=4$ (after Klöckner
et al.) and ramp width 4, the author finds that the lower edge filters too
many elements and the upper edge does not stabilize, and recommends
$s_0\in[-3.7,-2.7]$ for $N=2$ and $[-5.3,-4.3]$ for $N=3$, a ramp of width
about 1 below the centre (Table 2b), summarized in the conclusions as
$s_0\in[-(N+2),-(N+1)]$ (§5). A posteriori maps of $s_e$ in both turbines
place the wake and transitional regions in that range, with only a tiny
fraction of elements filtered (§4.4, Figs. 18–20). A single $s_0$ can be
kept while the order is raised, since the threshold of the higher order is
conservative for lower orders (§4.4.1).

**Entropy filter (EF)** of Dzanic and Witherden, as implemented by Wang
(2024, §2.3, Eqs. 20–22): a second-order modal filter
$\Lambda_{mm}=e^{-\alpha_f\vartheta_m^2}$ whose strength $\alpha_f$ is found
per element so that the discrete minimum entropy principle
$$\mathcal S\big(U(\boldsymbol x,t+\Delta t)\big)\ge\min\mathcal S\big(U(\boldsymbol x,t)\big)-\epsilon_{\mathcal S}$$
and positivity $\rho\ge\rho_{\min}$, $p\ge p_{\min}$ hold, the minimum
taken over the element and its immediate neighbours (the domain of influence
for CFL below one); $\epsilon_{\mathcal S}=10^{-4}$,
$\rho_{\min}=p_{\min}=10^{-8}$, and $\alpha_f=0$ means no filtering.

**Comparison** (Wang 2024, §4):

- **Smooth flow.** On the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
  at $Re=1600$ and $5000$ ($64^3$ elements, $N=3$, HLLC, $s_0=-4$) the LMF
  run and the unfiltered run give the same dissipation rate and spectra, both
  in excellent agreement with DNS; the filter costs about 5.5% (overhead of
  computing $s_e$) (§4.1, Figs. 2–3). The author notes that the filter is
  then essentially never activated.
- **T106C low-pressure turbine** (exit $Re=80{,}000$, Mach 0.65; 122 904
  hexahedra, $N=3$, 7 865 856 degrees of freedom per equation;
  $\Delta y^+\approx0.5$ after division by $N+1$, $\Delta x^+\approx20$,
  $\Delta z^+\approx6$): with $s_0=-4.0$ both HLLC and Roe are stable, and
  the isentropic Mach number agrees with the experiment of Michálek et al.
  and with a CPR $N=3$ reference; the filter has negligible effect on it
  (§4.2, Table 4, Fig. 8). The smooth upstream flow has $s_e<-7$, so a
  threshold below $-7$ filters essentially everything (§4.2, Fig. 18).
- **VKI LS89 vane** (MUR129, exit $Re=1.13\times10^6$, heat transfer; 6.6
  to 31.3 million degrees of freedom, Table 6): at $N=3$ HLLC is stable with
  $s_0=-4.0$ and $-4.3$, Roe only with $-4.3$; at $N=2$ HLLC is stable with
  $-3.3$ and $-3.7$, Roe only with $-3.7$ (Tables 7–8). The heat-transfer
  coefficient in the turbulent region depends more on $s_0$ than on the
  Riemann solver; the transition location does not depend on $s_0$
  (Fig. 17).
- **EF against LMF.** EF stabilizes LS89 "without any tuning parameters",
  but resolves the trailing-edge pressure waves less sharply and decays
  faster at high frequency in the pressure spectrum than LMF with
  $s_0=-4.0$, consistent with Gao et al. as cited; it filters more elements
  (with small $\alpha_f$ in most) and costs about 15% more per iteration
  than LMF, which is also simpler to implement (§4.3.2, §4.4.2–4.4.3,
  Figs. 15–16, 19, 21). Its heat-transfer prediction lies between those of
  the two LMF thresholds (Fig. 17).

The cascades are on [turbine cascades](/benchmarks/turbine-cascade.md). The
author connects solution filtering to
[spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md) in
finite differences, as cited from Lamballais et al., and leaves the FR
analogue to future work (§2.3, §5); filtering adds to the
[numerical dissipation](/properties/numerical-dissipation.md) that
[implicit LES](/definitions/implicit-les.md) relies on (§2.3).

## Applications in compressible turbulence

**Switching FV subcells in a code comparison.** In the supersonic
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) comparison of
[Chapelier et al. (2024)](/sources/chapelier-2024.md) ($Re=1600$,
$M_0=1.25$, $64^3$ to $512^3$ degrees of freedom), [FLEXI](/software/flexi.md)
runs a fourth-order DGSEM ($N=3$) whose troubled elements are projected onto
element-local subcells solved with a second-order TVD finite-volume scheme
and a generalized minmod limiter, the indicator being the exponential decay
rate of the modal coefficients of the **pressure** (§III.B.f). It gives the
sharpest shocks of the seven solvers and matches the reference Mach profile
at $256^3$, but oscillates on the coarser grids (§IV.B, Fig. 8); its
dilatational dissipation is high and oscillates on the low resolutions,
which the authors attribute to the switching between DG and FV per element
(§IV.A, Fig. 6). Its kinetic energy at $64^3$ is closer to the
central-difference codes than to the other Riemann-flux codes, which they
attribute to the subcell capturing rather than artificial diffusivity, and
its solenoidal dissipation is among the highest on all grids. In the
authors' classification, local switching to lower-order schemes gives
"sharp but oscillating shocks" on coarse grids (§V; see
[artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)
for the comparison).

**Switching FV subcells in a shock/turbulent-boundary-layer interaction.**
[Gao et al. (2022)](/sources/gao-2022.md) run the FLEXI switching scheme
of Sonntag & Munz (troubled element of degree $N$ replaced by $(N+1)^3$
equidistant second-order TVD subcells) as an implicit LES of an oblique
shock reflecting on a Mach 2 turbulent boundary layer ($N=6$, about 93
million degrees of freedom on 16,384 cores, $Re_{\theta_0}=1628$). Three
ingredients are specific to the turbulent interaction:

- **Indicator on a filtered field.** The Jameson pressure indicator,
  evaluated on the instantaneous field, flags much of the under-resolved
  turbulent boundary layer and fills it with dissipative subcells, and
  Ducros-type indicators miss shocks inside the boundary layer or flag too
  many cells; evaluating the Jameson indicator on the spanwise-averaged
  pressure confines the subcells to the shocks, including inside the
  boundary layer (§3.2, Figs. 2, 7). The construction and its limits
  (quasi-two-dimensional configurations) are on
  [shock sensors](/definitions/shock-sensor.md).
- **Positivity.** The positivity-preserving limiter of Zhang & Shu is added
  "to stabilise the switching between DG and FV subcells" caused by
  unsteady shocks inside the boundary layer; the authors state, without a
  test, that it keeps DG stable "without losing high-order accuracy"
  (§3.2; no formula printed).
- **Cost.** The hybrid run has a performance index (wall time times cores
  per degree of freedom, time step and Runge–Kutta stage) of about
  1.84 µs against 1.55 µs for the shock-free boundary layer, 18.7% more,
  within the 15–20% hybrid overhead that Krais et al. report above,
  filtering included (§5.3.1, Eq. 19).

In the laminar shock/boundary-layer interaction of Katzer (Mach 2,
$Re_{x}=3\times10^5$ at the impingement point, pressure ratio 1.4), DG with
$N=4$ on 182,000 degrees of freedom reaches the converged separation length
that a second-order finite-volume scheme needs 409,500 degrees of freedom
for, both 5.87% longer than Katzer's original, under-resolved prediction;
at about 355 degrees of freedom per core the DG/FV run takes 7680
CPU-minutes against 10,368 for the finite-volume one (§4.1–4.2,
Figs. 9, 13). The turbulent interaction (separation at $16.7\delta_r$
against $17.6\delta_r$ in the reference LES of Morgan et al., reattachment
$19.5\delta_r$ against $19.3\delta_r$, $\delta_r$ the boundary-layer
thickness at a reference station) is on
[shock/boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md).

**Convex blending on GPUs.** The GPU code [GALÆXI](/software/galaexi.md)
keeps the Hennemann blending with an a priori indicator,
$\partial_tU=(1-\alpha)R_{DG}+\alpha R_{FV}$, blending only the element
interiors because the outer face fluxes of DG and FV coincide
([Kurz et al. 2025](/sources/kurz-2025.md), §2.3, Eq. 21). In the supersonic
Taylor–Green vortex ($N=7$, $64^3$ to $512^3$ degrees of freedom) the
maximum $\alpha$ is the same at all resolutions and the solenoidal
dissipation converges to that of Chapelier et al.'s reference (§5.2,
Fig. 11); in a wall-resolved LES of a [NASA Rotor 37](/benchmarks/nasa-rotor-37.md)
mid-span cascade ($N=5$, $2.6\times10^8$ degrees of freedom) $\alpha$ is
active only near the leading-edge shock, with values 0.1 to 0.7 (§6.3,
Fig. 13). Kurz et al. recall (§2.3, citing Beck & Kurz) that the blending
"has also been demonstrated to yield a sensible turbulence model if tuned
correctly" (see above).

**Convex blending with a dilatation–vorticity sensor.** [Klose et al.
(2025)](/sources/klose-2025.md), §2, Eq. (1), write the same blend as
$\partial_t\boldsymbol q+\alpha R^{FV}+(1-\alpha)R^{DG}=0$ with a
**first-order** FV residual, in DLR's TRACE DGSEM ($N=3$, entropy-conserving
Chandrashekar split form, BR1, implicit LES; see [TRACE](/software/trace.md)),
and select troubled elements with the dilatation–vorticity sensor of
Fernandez et al., with time and space relaxation factors 0.7 (formula not
printed). It carries implicit LES of a transonic
[compressor cascade](/benchmarks/compressor-cascade.md) at inlet Mach 1.21
and $Re=1.35\times10^6$, whose suction-side normal shock oscillates at low
frequency (see
[shock/boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)).

**An alternative that keeps the polynomial.**
[Cernetic et al. (2024)](/sources/cernetic-2024.md), §3.1, capture shocks in
modal DG up to high order with a von Neumann–Richtmyer viscous pressure at
the internal quadrature points instead of subcells; see
[artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md).

**Polynomial limiting instead of subcells (modal RKDG).**
[Huang et al. (2025)](/sources/huang-2025.md), §1, recall the hybrid DG/FV
subcell route (Balsara et al. 2007, Sonntag & Munz 2014, and Jiang et al.
2021 with a boundary-variation-diminishing THINC reconstruction on the
subcells, as cited) and stay instead with the classical indicator–limiter
route of Runge–Kutta DG, as do [Huang & Fu (2024)](/sources/huang-2024.md):
a troubled-cell indicator flags cells, and a limiter rebuilds the
higher modal coefficients of the flagged cells from compact neighbour
stencils, keeping the cell average. Both use
third-order modal DG ($N=2$) on uniform Cartesian grids and inviscid
tests only; the TENO-based indicator is on
[shock sensors](/definitions/shock-sensor.md), the TENO and TENO-THINC
limiters on [WENO](/methods/weno-scheme.md). No source of this bundle
compares the two routes on the same flow.

## A posteriori subcell correction in multi-material DG

A third variant is named in a multi-material context. In their
review of diffuse-interface methods for compressible multi-material flow,
[Maltsev et al. (2022)](/sources/maltsev-2022.md), §IV C, cite the a
posteriori subcell finite-volume limiting of Dumbser et al. and Dumbser &
Loubère (named, not described), and its use by Cheng, Zhang & Liu in a DG scheme for
a $\gamma$-based two-medium model with an HLL flux; that DG scheme reduces
at degree $N=0$ to a quasi-conservative finite-volume scheme and keeps
uniform pressure and velocity at isolated material interfaces. They also
review the $P_NP_M$ reconstructed DG, which spans the range between finite
volumes ($N=0$) and DG ($M=N$) by reconstruction instead of by subcells
(§III C; see the
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md) page),
and conclude that DG for diffuse-interface models is still mostly
restricted to reduced five-equation models on structured meshes (§V).
None of these is a turbulence application.

## Convention difference

The two variants place the subcells differently: equispaced subcells of width
$2/(N+1)$ in reference space (Krais et al. 2021, Eq. 59) against subcells sized
by the LGL weights (Beck & Kurz 2023, Fig. 4). The difference is part of the
schemes, not a disagreement. The FV operator is second order in the
switching scheme of FLEXI (Krais et al. 2021; Chapelier et al. 2024) and
first order in the blend of Klose et al. (2025); Klose et al. put the
operators on the left-hand side, Beck & Kurz (2023) and Kurz et al. (2025)
on the right.

## Qualifications

- Krais et al. (2021) print two statements on the hybrid cost: "almost no
  additional computational cost compared to pure DG" (§2.2.3, §4.1) and "about
  15–20% worse than for the pure DG method" (§5.8, measured). The measured
  value is the quantitative one.
- Krais et al. (2021, Eq. 64) print the flux at face $i+\tfrac12$ with arguments
  $(U^{FV-},U^{FV-})$ while the three other faces carry $(U^{FV-},U^{FV+})$.
- Beck & Kurz (2023, Eq. 17) admit $0\le\alpha\le1$ but map the RL action to
  $[0,0.5]$ (Table I).
- **Printed slips (Wang 2024, arXiv v2).** Table 2a prints the upper Li–Wang
  edge for $N=2$ as $2.77$, against $-2.7+4=1.3$ from its own centre and ramp
  width (the $N=3$ row, $-8.3$, $-4.3$, $-0.3$, is consistent); the centres
  $-2.7$ and $-4.3$ are truncations of $-4\ln2\approx-2.77$ and
  $-4\ln3\approx-4.39$ *(compiler check, not in the sources)*. The
  recommended ranges of Table 2b ($[-3.7,-2.7]$, $[-5.3,-4.3]$) and the
  conclusions' $[-(N+2),-(N+1)]$ ($[-4,-3]$, $[-5,-4]$) overlap but differ.
  Eq. (19) prints the numerator inner product with a single argument;
  Eq. (18) leaves $\vartheta_m=\vartheta_c$ and $\vartheta_m=1$ uncovered
  and defines the mode index as $i/(N_p-1)$ with $N_p$ called "the maximum
  order of the polynomial"; §4.4.1 prints the $N=3$ range as "[-5.5:4]".
  The entropy filter is attributed in the text to ref. [31], a different
  Dzanic et al. preprint; the filter paper is ref. [42].
- **Provable stability.** Kurz et al. (2025, §1) count "provable stability
  near shocks" among GALÆXI's distinguishing features, from the
  entropy-stable construction of Hennemann et al.; their runs use the
  Pirozzoli kinetic-energy-preserving split flux, which Ferrer et al. (2023, §3.3)
  list as a split form distinct from the entropy-conserving ones, and the
  paper does not state that the proof covers this configuration.
- **Printed saving (Gao et al. 2022, §4.2).** The DG/FV run is said to
  take "around 35% less" CPU time than the finite-volume one; from the
  printed 7680 and 10,368 CPU-minutes it takes 25.9% less, and 35% is how
  much more the finite-volume run takes *(compiler check, not in the
  sources)*. The laminar comparison uses the classic Jameson indicator on
  a two-dimensional case and says nothing about the subcells' share of the
  cost.
- Chapelier et al. (2024) attribute the oscillations of FLEXI's dilatational
  dissipation to DG/FV switching without a run that isolates it; Klose et
  al. (2025) do not show the distribution of $\alpha$.

# Citations

- [Krais et al. (2021)](/sources/krais-2021.md) — §2.2.3; §4.1–4.4, Eqs. (56)–(67), Figs. 14–16; §5.7–5.8, Figs. 19–20; §7.2, Fig. 25.
- [Beck & Kurz (2023)](/sources/beck-2023.md) — §III C, Eqs. (16)–(17), Figs. 4–5; §V C, Figs. 8, 12–14; Table I.
- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — §2, Table 1; §4.4, Eqs. (15)–(19), Fig. 9 (SVV-filtered artificial viscosity instead of subcells).
- [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md) — §1, §6.3 (filtered artificial viscosity against order-lowering approaches).
- [Wang (2024)](/sources/wang-2024-b.md) — arXiv v2: §2.3, Eqs. (17)–(22), Tables 1–2, App. A (local modal filter, Persson–Peraire indicator, entropy filter); §4.1, Figs. 2–3; §4.2, Tables 3–4, Fig. 8; §4.3, Tables 5–8, Figs. 13–17; §4.4, Figs. 18–21; §5.
- [Chapelier et al. (2024)](/sources/chapelier-2024.md) — HAL hal-04582857v1: §III.B.f, h (FLEXI FV subcells, pressure modal-decay indicator); §IV.A–B, Figs. 5–8 (energy, dissipation, shock profiles); §V.
- [Kurz et al. (2025)](/sources/kurz-2025.md) — arXiv 2404.12703v2: §1; §2.3, Eq. (21) (Hennemann blending in GALÆXI); §5.2, Fig. 11 (supersonic Taylor–Green vortex); §6.3, Fig. 13 (Rotor 37 cascade, $\alpha$ near the shock).
- [Klose et al. (2025)](/sources/klose-2025.md) — ASME accepted manuscript: §2, Eq. (1) (blending with first-order FV, dilatation–vorticity sensor); §3.
- [Cernetic et al. (2024)](/sources/cernetic-2024.md) — arXiv 2401.06841v2: §3.1 (artificial viscosity instead of subcells).
- [Gao et al. (2022)](/sources/gao-2022.md) — §3.2, Figs. 1–2, 5–7 (Sonntag–Munz subcells, filtered indicator, positivity-preserving limiter); §4.1–4.2, Figs. 9, 13 (laminar interaction, DG against FV cost); §5.3.1, Eq. (19) (performance index of the hybrid).
- [Huang et al. (2025)](/sources/huang-2025.md) — §1 (subcell approaches recalled; polynomial limiting chosen).
- [Huang & Fu (2024)](/sources/huang-2024.md) — §1, §4 (indicator–limiter route of RKDG).
- [Maltsev et al. (2022)](/sources/maltsev-2022.md) — §III C, §IV C, §V (a posteriori subcell limiting and reconstructed DG in multi-material DG, cited).
