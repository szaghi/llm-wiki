---
type: Property
title: "Entropy conservation and entropy stability"
description: "A discretization is entropy conservative when its convective terms reproduce the vanishing global entropy production of smooth inviscid flow, and entropy stable when entropy can only be dissipated; this page gives the two-point fluxes that achieve it, its dependence on the equation of state, and its measured effect in turbulence simulations."
status: established
aliases: [EC, entropy-conservative scheme, entropy-conserving flux, entropy-stable discretization, entropy stability, Ismail–Roe flux, Chandrashekar flux, EC-TP scheme, nonlinear stability]
tags: [entropy-stable, kinetic-energy-preserving, compressible, dg, dns, numerical-dissipation]
timestamp: 2026-10-26T16:22:00Z
---

# Entropy conservation and entropy stability

For smooth, inviscid and adiabatic flow the compressible Euler equations
neither create nor destroy the entropy density $\rho s$: its convective
term integrates to zero over a periodic domain. A semi-discretization is
**entropy conservative (EC)** when its convective terms reproduce this
global balance at the discrete level, and **entropy stable** when, with
dissipative fluxes added, the discrete (mathematical) entropy can only
decrease. Entropy, like the kinetic energy of
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md)
(KEP), is an **induced variable**: it is not evolved by the scheme, and its
discrete evolution follows from the discretization of mass, momentum and
energy ([Aiello et al. 2026](/sources/aiello-2026.md), §3.1, Eqs. 4–5).
Unlike kinetic energy, the thermodynamic entropy is a strict (convex)
entropy of the Euler system, which is why entropy stability is the stronger
nonlinear-stability statement of the two
([Mateo-Gabín et al. 2022](/sources/mateogabin-2022.md), §2.3).

Page-local notation: $e$ the specific internal energy and $s$ the specific
entropy; $\mathcal E(Q)$ a convex mathematical entropy of the conservative
variables $Q$ and $W=\partial\mathcal E/\partial Q$ its entropy variables;
for a node-indexed one-dimensional scheme, $\mathcal F_{\rho\phi}$ the
convective numerical flux of $\rho\phi$ at the face $i+\tfrac12$,
$\{\!\{\phi\}\!\}=\tfrac12(\phi_i+\phi_{i+1})$ the registry's arithmetic
mean, and $\phi^{\ln}=(\phi_{i+1}-\phi_i)/(\ln\phi_{i+1}-\ln\phi_i)$ the
logarithmic mean.

## Definitions in the sources

**Global and local conservation of an induced variable.** Aiello et al.
(2026, §3.1) split the Eulerian terms of each conserved quantity $\rho\phi$
($\phi=1,u_i,E/\rho$) into a convective and a pressure part. The
continuous identities $\int_\Omega\mathcal C_{\rho k}\,dV=0$ for the
kinetic energy and $\int_\Omega\mathcal C_{\rho s}\,dV=0$ for the entropy
(Eqs. 4–5; page-local $\mathcal C_{\rho\phi}$ the convective term) define,
when a scheme reproduces them, a **globally KEP** and a **globally EC**
scheme. A scheme is *locally* conservative when the induced convective term
is a difference of face fluxes; local implies global by telescoping, and,
as recalled by the authors from Coppola & Veldman, the converse holds for a
wide class of finite-difference discretizations (§3.1). Higher-order
versions are linear combinations of two-point fluxes on wider stencils
(§3.1).

**Entropy variables and dissipative fluxes.** Mateo-Gabín et al. (2022,
§2, Eqs. 19–24) write dissipative fluxes as $\mathcal B\nabla W$ with
$\mathcal B$ symmetric positive semi-definite, which then dissipate
$\mathcal E$ at the rate $(\nabla W)^{\mathsf T}\mathcal B\nabla W\ge0$;
for the thermodynamic entropy $\mathcal E=-\rho s/(\gamma-1)$ with
$s=\ln p-\gamma\ln\rho$. This is the construction behind the entropy-stable
artificial viscosity and
[spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md) of
the [DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md) (see
also [artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)).
The kinetic energy has entropy variables too, but its balance contains the
pressure work, which cannot be bounded, so kinetic-energy "stability" is
weaker (§2.3; see
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md)).

## Two-point fluxes

**Flux differencing.** On Legendre–Gauss–Lobatto nodes the strong-form
DGSEM has the summation-by-parts property, and its volume term can be
replaced by a sum of symmetric, consistent two-point fluxes $f^{\#}$; the
choice of $f^{\#}$ decides whether the split-form scheme is kinetic-energy
preserving or entropy conserving ([Krais et al. 2021](/sources/krais-2021.md),
§3.3, Eqs. 52–54; the formula is on the KEP page). The same split-form
volume term with a Hadamard product, written on the reference element with
Chan's skew-symmetric stiffness operator, is the core of the nonlinearly
stable [flux reconstruction](/methods/flux-reconstruction.md) assessed by
[Brillon & Nadarajah (2026)](/sources/brillon-2026.md), §2.7, Eqs. (71)–(72).

**Ismail–Roe flux.** Brillon & Nadarajah (2026, §2.7.1, Eqs. 73–79) print
the entropy-conserving flux of Ismail & Roe in terms of the parameter vector
$z=\big(\sqrt{\rho/p},\ \sqrt{\rho/p}\,u,\ \sqrt{\rho/p}\,v,\ \sqrt{\rho/p}\,w,\ \sqrt{\rho p}\big)^{\mathsf T}$:
$$\begin{aligned}
f^{\#}_{\mathrm{IR}}&=\big(\hat\rho\hat u,\ \hat\rho\hat u^2+\hat p_1,\ \hat\rho\hat u\hat v,\ \hat\rho\hat u\hat w,\ \hat\rho\hat u\hat h\big)^{\mathsf T},\\
\hat\rho&=\{\!\{z_1\}\!\}\,z_5^{\ln},\quad \hat u=\frac{\{\!\{z_2\}\!\}}{\{\!\{z_1\}\!\}},\quad \hat p_1=\frac{\{\!\{z_5\}\!\}}{\{\!\{z_1\}\!\}},\\
\hat p_2&=\frac{\gamma+1}{2\gamma}\frac{z_5^{\ln}}{z_1^{\ln}}+\frac{\gamma-1}{2\gamma}\hat p_1,\quad \hat h=\frac{\gamma\hat p_2}{\hat\rho(\gamma-1)}+\tfrac12(\hat u^2+\hat v^2+\hat w^2),
\end{aligned}$$
with $\hat v$, $\hat w$ like $\hat u$ (the hatted two-point averages are
page-local, not test-filtered quantities), the logarithmic mean computed by
a numerically stable procedure. The other fluxes they compare are named
but not printed: Kennedy–Gruber (KEP only), Chandrashekar (EC and KEP) and
Chandrashekar as modified by Ranocha (EC, KEP and
[pressure-equilibrium preserving](/properties/pressure-equilibrium-preservation.md))
(§3.1.6).

**The Chandrashekar flux in practice.** Krais et al. (2021, §7.2) use it
in the DG cells of their DG/finite-volume shock-capturing scheme;
[Klose et al. (2025)](/sources/klose-2025.md), §2, use the
entropy-conserving Chandrashekar split form "together with the
corresponding Riemann solver" in the TRACE DGSEM ($N=3$) for an implicit
LES of a transonic compressor cascade, with
[subcell finite-volume blending](/methods/subcell-finite-volume-shock-capturing.md)
at the shocks; [Ranjbar et al. (2026)](/sources/ranjbar-2026.md), §II.A,
run the Taylor–Green vortex and channel flow in
[HORSES3D](/software/horses3d.md) with the split form and the Chandrashekar
averaging, a low-dissipation Roe flux and BR1 or BR2 viscous fluxes.
[HORSES3D](/software/horses3d.md) offers entropy-conserving and Chandrashekar
split forms beside the kinetic-energy-preserving ones
([Ferrer et al. 2023](/sources/ferrer-2023.md), §3.5).

## Entropy conservation depends on the equation of state

Aiello et al. (2026, §3.2) separate the two properties. With the
second-order flux family (Eq. 7)
$$\mathcal F_\rho=\hat\rho\,\{\!\{u\}\!\},\qquad \mathcal F_{\rho u}=\mathcal F_\rho\{\!\{u\}\!\}+\{\!\{p\}\!\},\qquad \mathcal F_{\rho E}=\mathcal F_\rho\frac{u_iu_{i+1}}{2}+\mathcal F_{\rho e}+\tfrac12\big(u_ip_{i+1}+u_{i+1}p_i\big),$$
($\hat\rho$ a consistent face density, page-local) the scheme is KEP for
any internal-energy flux $\mathcal F_{\rho e}$, because KEP needs only
$\mathcal F_{\rho u}=\mathcal F_\rho\{\!\{u\}\!\}$ in the convective
momentum flux (recalled from Jameson and Veldman). The face density and
$\mathcal F_{\rho e}$ remain free, and EC is imposed through them. Two
consequences follow, both stated by the authors:

- **EC is tied to the thermodynamic model.** EC fluxes designed for a
  calorically perfect gas (Chandrashekar, Ranocha, the asymptotic AEC
  family of De Michele & Coppola) lose their EC property for a thermally
  perfect or real gas, but keep KEP, which depends only on the mass and
  momentum discretization (§3.2). This agrees with Bernades et al. (2023,
  §3.1.2) that KEP "depends only" on continuity and momentum.
- **EC for an arbitrary equation of state** follows from discrete
  consistency with the volumetric Gibbs relation
  $\partial_t(\rho e)=T\,\partial_t(\rho s)+g\,\partial_t\rho$, $g=e-Ts+p/\rho$
  the Gibbs free energy (recalled from Aiello et al. 2025); the resulting
  flux is singular at uniform temperature and is regularized by the
  Ismail–Roe procedure or by an asymptotic expansion (§3.2).

**Thermally perfect gas.** For a gas with $p=\rho RT$ but temperature-dependent
specific heats, $c_v(T)=\sum_{m=-\ell}^{r}c_{v,m}T^m$ (NASA Glenn
polynomials; page-local $R$, $c_{v,m}$, $\ell$, $r$), the internal energy
and entropy are integrals of $c_v$, and "entropy variations are no longer
trivially related to temperature" (§2.1). The authors' **EC-TP** flux
(derived in a companion paper, used here; p. 10, Table 1) is
$$\begin{aligned}
\mathcal F_\rho&=\rho^{\ln}\{\!\{u\}\!\},\qquad \mathcal F_{\rho u}=\mathcal F_\rho\{\!\{u\}\!\}+\{\!\{p\}\!\},\\
\mathcal F_{\rho E}&=\mathcal F_\rho\frac{u_iu_{i+1}}{2}+\mathcal F_\rho\Big[e_{\mathrm{ref}}+c_{v,-1}\Big(1-\frac{\{\!\{1/T\}\!\}}{(1/T)^{\ln}}+\{\!\{\ln T\}\!\}\Big)+\frac{c_{v,0}}{(1/T)^{\ln}}+\sum_{m\ne-1,0}\frac{c_{v,m}}{m+1}\,\mathcal T_m\Big]+\tfrac12\big(u_ip_{i+1}+u_{i+1}p_i\big),
\end{aligned}$$
with $e_{\mathrm{ref}}$ a reference energy and $\mathcal T_m$ (page-local)
the generalized two-point averages the source defines for $m\ge1$ and
$m\le-2$; at equal nodal temperatures each $\mathcal T_m$ reduces to
$T^{m+1}$, the power that $\int c_v\,dT$ produces for the coefficient
$c_{v,m}$ *(compiler check, not in the sources)*. It is EC and KEP for the
thermally perfect gas (Table 1).

**Scheme properties compared by Aiello et al. (2026)** (Table 1; thermally
perfect gas):

| Scheme | density flux | pressure term in momentum | KEP | EC |
|---|---|---|---|---|
| EC-TP | $\rho^{\ln}\{\!\{u\}\!\}$ | $\{\!\{p\}\!\}$ | yes | yes |
| AEC$^{(N)}$-TP (asymptotic variant) | series in the density jump | $\{\!\{p\}\!\}$ | yes | asymptotically |
| Gouasmi et al. (2020) | $\rho^{\ln}\{\!\{u\}\!\}$ | $R\{\!\{\rho\}\!\}/\{\!\{1/T\}\!\}$ | yes (the authors' definition) | yes |
| Ranocha (2018) | $\rho^{\ln}\{\!\{u\}\!\}$ | $\{\!\{p\}\!\}$ | yes | no (exact for a calorically perfect gas), PEP |
| KEEP (Kuya et al. 2018) | $\{\!\{\rho\}\!\}\{\!\{u\}\!\}$ | $\{\!\{p\}\!\}$ | yes | no (approximately EC for a calorically perfect gas) |

Gouasmi et al.'s scheme has EC-TP's internal-energy flux and reduces to
Chandrashekar's for a calorically perfect gas; its pressure term is stated
to spoil the kinetic-energy balance in isotropic turbulence (recalled from
Aiello et al.'s companion paper and from Gassner et al.) (§4). KEEP has
later been made entropy preserving to machine precision by Taylor
expansions (recalled, Tamaki et al.; Kawai & Kawai) (§3.2).

## Effect in turbulence simulations

**High-enthalpy channel flow.** Aiello et al. (2026, §4) run
[DNS](/definitions/direct-numerical-simulation.md) of compressible
[channel flow](/benchmarks/turbulent-channel-flow.md) of CO$_2$ as a
thermally perfect gas in [STREAmS](/software/streams.md) (sixth-order central
differences, fully central after a WENO5 transient), at wall-based bulk Mach
numbers 3, 4 and 5 and $Re_\tau\approx470$, 630 and 800. Measured against
EC-TP (no external reference exists), in max-norm relative difference
(Table 3):

| Quantity (case) | KEEP | Gouasmi | Ranocha |
|---|---|---|---|
| transformed mean velocity, Mach 3 / 4 / 5 | 0.23 / 1.05 / 1.98% | 0.57 / 0.23 / 0.78% | — / — / 0.55% |
| streamwise Reynolds stress, Mach 3 / 4 / 5 | 0.60 / 1.59 / 10.98% | 1.38 / 1.21 / 5.25% | — / — / 1.32% |

(Ranocha's scheme was run at Mach 5 only.) The wall-pressure rms in wall
units is 1.97, 2.33, 2.57 with EC-TP and 2.89, 3.23, 3.55 with KEEP. The
non-EC schemes overpredict pressure and density fluctuations, and after a
long stationary period their fluctuations drift, whereas both EC schemes
stay statistically stationary over a run extended by 50% (§4.2, Fig. 3).
Comparing EC-TP with Gouasmi (same convective part, different pressure
term) and with KEEP (same pressure term, non-EC convection), the authors
conclude that EC by convection is "the main factor" of robustness and
necessary but not sufficient for accuracy, the pressure-term treatment
mattering in the buffer layer at high Mach number (§4.2, §5). With the EC
schemes no shock capturing was needed in these shock-free cases; strong
shocks would still require it (§4.2).

**Low-Mach Taylor–Green vortex.** On the viscous
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at $Re=1600$,
$M_\infty=0.1$ and $96^3$ degrees of freedom, Brillon & Nadarajah (2026,
§3.1.6, Fig. 16) find the Ismail–Roe, Kennedy–Gruber, Chandrashekar and
Chandrashekar–Ranocha fluxes "nearly indistinguishable" in spectra,
kinetic energy, dissipation rate, enstrophy and effective viscosity, with
negligible differences in pressure dilatation; Kennedy–Gruber is the
cheapest because it needs no logarithmic mean. The split-form scheme is
stable on every under-resolved grid without upwinding, over-integration or
a subgrid model (§3.1.2), and costs about half the CPU time of an
over-integrated strong-form DG scheme for $N\in[5,12]$ (§3.1.3, Fig. 12).
Two-point fluxes evaluated on uncollocated (Gauss) flux nodes need
entropy-projected variables, which the authors call "key in enabling
entropy stability" there (§2.7).

**Entropy behaviour of a non-EC scheme.** In the real-gas mixing layer of
[Bernades et al. (2023)](/sources/bernades-2023.md), §4.2, the
pressure-equilibrium-preserving KGP-Pt scheme shows "good conservation" of
global entropy although it is not entropy preserving.

## Limits

- **Shocks.** Entropy-conserving split forms are not stable at shocks by
  themselves, because entropy stability rests on positive density, which
  oscillations near shocks can violate; shock capturing must add density
  regularization (Mateo-Gabín et al. 2022, §1). Klose et al. (2025, §2) and
  Krais et al. (2021, §7.2) add finite-volume subcells; Ferrer et al. (2023,
  §4.4) filter an artificial viscous flux so that entropy stability is kept,
  which requires filtering "only one half" of the factorized flux.
- **Non-conforming and adapted meshes.** In HORSES3D the mortar coupling of
  faces between elements of different polynomial degree "does not retain
  entropy stability" (Ferrer et al. 2023, §3.6), and the split forms need
  Gauss–Lobatto nodes (§3.3).
- **Time integration** adds entropy errors, "typically less significant in
  practice" than the spatial ones (Aiello et al. 2026, §3.3); the
  properties on this page are semi-discrete.
- **Real gases.** Bernades et al. (2023, §5) liken their chain-rule barrier
  to pressure-equilibrium preservation to the difficulty of entropy
  conservation with arithmetic-average fluxes, and name non-linear-average
  finite-volume fluxes as a possible remedy, "expected to be cumbersome"
  for the Peng–Robinson equation of state (a conjecture).

## Qualifications

- **Regime of the evidence.** The two turbulence studies point in
  different directions without contradicting each other: Aiello et al.
  (2026) find EC decisive for long-time robustness and thermodynamic
  statistics of a thermally perfect gas at Mach 3–5 without shock capturing,
  while Brillon & Nadarajah (2026) find the choice among EC and KEP fluxes
  immaterial for a calorically perfect gas at $M_\infty=0.1$. The gas
  model, Mach number, discretization (central finite differences against
  flux reconstruction) and flow differ.
- Aiello et al.'s accuracy measure is the difference to EC-TP, so "most
  accurate" for EC-TP rests on the controlled comparison of §4.2, not on
  external reference data (Table 3).
- Aiello et al. (2026) claim the first high-enthalpy channel simulations of
  a thermally perfect gas with exactly EC convective schemes (§5), and
  Brillon & Nadarajah (2026, §1) the first use of a provably
  entropy-conserving and stable high-order flux reconstruction for viscous
  turbulent flow; both are priority statements of the authors.
- Printed slips in Aiello et al. (2026): the sample spacing of the
  statistics is printed "$\Delta t_s=1.5U_b/h$" (§3.3), which has the
  dimension of an inverse time *(compiler check, not in the sources)*; the
  Table 2 caption labels the supersonic cases by $M_b$ while the columns use
  the wall-based bulk Mach number, which §2.1 defines differently.

# Citations

- [Aiello et al. (2026)](/sources/aiello-2026.md) — §2.1 (thermally perfect gas); §3.1, Eqs. (4)–(5) (induced variables, global and local EC and KEP); §3.2, Eq. (7), Table 1, p. 10 (KEP flux family, EC-TP, AEC, Gouasmi, Ranocha, KEEP; EOS dependence; Gibbs relation); §3.3 (time-integration entropy error); §4.1–4.2, Figs. 1–3, Table 3 (channel DNS); §5.
- [Brillon & Nadarajah (2026)](/sources/brillon-2026.md) — arXiv 2411.12108v1: §1; §2.7, Eqs. (71)–(72) (split-form NSFR, entropy-projected variables); §2.7.1, Eqs. (73)–(79) (Ismail–Roe flux); §3.1.2–3.1.3, Fig. 12; §3.1.6, Fig. 16.
- [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md) — §1 (EC split forms not stable at shocks); §2, Eqs. (19)–(24) (entropy variables, dissipative fluxes); §2.3 (kinetic energy not a strict entropy).
- [Krais et al. (2021)](/sources/krais-2021.md) — §3.3, Eqs. (52)–(54) (flux differencing, KEP or EC by choice of $f^{\#}$); §7.2 (Chandrashekar flux with finite-volume subcells).
- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — §3.3, §3.5 (split forms in HORSES3D, Gauss–Lobatto nodes); §3.6 (mortars not entropy stable); §4.4 (entropy-stable filtered artificial viscosity).
- [Klose et al. (2025)](/sources/klose-2025.md) — ASME accepted manuscript: §2 (Chandrashekar entropy-conserving split form with subcell blending in TRACE).
- [Bernades et al. (2023)](/sources/bernades-2023.md) — §3.1.2 (KEP depends on continuity and momentum only); §4.2 (global entropy of KGP-Pt); §5 (analogy with entropy conservation, non-linear averages).
- [Ranjbar et al. (2026)](/sources/ranjbar-2026.md) — arXiv 2512.03315v1: §II.A (split form with Chandrashekar averaging in HORSES3D).
