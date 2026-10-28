---
type: Property
title: "Entropy conservation and entropy stability"
description: "A discretization is entropy conservative when its convective terms reproduce the vanishing global entropy production of smooth inviscid flow, and entropy stable when entropy can only be dissipated; this page gives the two-point fluxes that achieve it, its dependence on the equation of state, its extension to the Spalart–Allmaras RANS equation, and its measured effect in turbulence simulations."
status: established
aliases: [EC, entropy-conservative scheme, entropy-conserving flux, entropy-stable discretization, entropy stability, Ismail–Roe flux, Chandrashekar flux, EC-TP scheme, nonlinear stability, entropy-stable RANS]
tags: [entropy-stable, kinetic-energy-preserving, compressible, dg, dns, numerical-dissipation]
timestamp: 2026-10-27T21:10:00Z
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
is a difference of face fluxes; local implies global by telescoping, and
the authors cite Coppola & Veldman for the converse, which holds for a
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

## Entropy through consistent energy fluxes (KEEP)

[Kuya et al. (2018)](/sources/kuya-2018.md) reach entropy conservation by
another route than an entropy-conservative two-point flux: they solve no
entropy equation and make the discrete energy fluxes consistent with the
continuous energy relations. From the Gibbs relation $T\,ds=de-(p/\rho^2)\,d\rho$
(citing Subbareddy & Candler) they write (§1.2, Eq. 6)
$$\frac{\partial\rho s}{\partial t}+\frac{\partial\rho su_j}{\partial x_j}=\frac1T\Big[\Big(sT-e-\frac p\rho\Big)\Big(\frac{\partial\rho}{\partial t}+\frac{\partial\rho u_j}{\partial x_j}\Big)+\frac{\partial\rho e}{\partial t}+\frac{\partial\rho eu_j}{\partial x_j}+p\frac{\partial u_j}{\partial x_j}\Big],$$
so that total entropy is preserved in a periodic domain whenever the mass
equation and the internal-energy equation
$\partial_t(\rho e)+\partial_j(\rho eu_j)+p\,\partial_ju_j=0$ hold (Eq. 7).
A scheme that evolves total energy satisfies the internal-energy equation
implicitly only if its kinetic-energy, internal-energy and
pressure-diffusion fluxes are consistent with the mass and momentum fluxes
(the three Analytical Relations; the fluxes of their QC$_C$ scheme are on
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md)).
Each inconsistency leaves a spurious source in the implicit internal-energy
equation: with a kinetic-energy flux that differs from the consistent one
by $\Delta_j$ (page-local) the entropy equation acquires
$\frac1T\,\partial\Delta_j/\partial x_j$ (§4.2, Eqs. 59–62), which is a flux
divergence, and so harmless to total entropy, only at uniform temperature
(Eq. 63), and the same holds for an inconsistent internal-energy flux
(§4.3, Eqs. 64–65). A divergence-form pressure-diffusion flux evaluates the
dilatation implicitly from cells $m\pm1$ (§4.4, Eq. 66), and the enthalpy
fluxes of Jameson and Pirozzoli split into a consistent internal-energy flux
plus a pressure diffusion written as $\partial(\rho u_j\,p/\rho)/\partial x_j$,
which lets density variations into the pressure-diffusion term (§4.5,
Eqs. 67–71); the authors find it "apparently very challenging to formulate
consistent enthalpy numerical fluxes". In their inviscid Taylor–Green and
isotropic-turbulence tests every inconsistent QC variant, including the
Jameson–Pirozzoli scheme, shows entropy reduction and growing density and
temperature fluctuations, while QC$_C$ keeps the total entropy (§5.2–5.3,
Figs. 1–11).

This is the KEEP scheme of the comparison table below, which Aiello et al.
(2026) class as approximately, not exactly, EC for a calorically perfect
gas. Kuya et al.'s own long run at $M_0=0.4$ shows a "negligibly small"
entropy reduction, which they attribute to the non-conservative
pressure-dilatation term (§5.2, Fig. 4); they state that it
"nominally satisfies" kinetic-energy and entropy conservation in the
semi-discrete sense (App. C).

## Entropy conservation depends on the equation of state

Aiello et al. (2026, §3.2) separate the two properties. With the
second-order flux family (Eq. 7)
$$\mathcal F_\rho=\hat\rho\,\{\!\{u\}\!\},\qquad \mathcal F_{\rho u}=\mathcal F_\rho\{\!\{u\}\!\}+\{\!\{p\}\!\},\qquad \mathcal F_{\rho E}=\mathcal F_\rho\frac{u_iu_{i+1}}{2}+\mathcal F_{\rho e}+\tfrac12\big(u_ip_{i+1}+u_{i+1}p_i\big),$$
($\hat\rho$ a consistent face density, page-local) the scheme is KEP for
any internal-energy flux $\mathcal F_{\rho e}$, because KEP needs only
$\mathcal F_{\rho u}=\mathcal F_\rho\{\!\{u\}\!\}$ in the convective
momentum flux (the authors cite Jameson and Veldman). The face density and
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
  the Gibbs free energy (the authors cite Aiello et al. 2025); the resulting
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
to spoil the kinetic-energy balance in isotropic turbulence (the authors
cite their companion paper and Gassner et al.; §4). KEEP has later been
made entropy preserving to machine precision by Taylor expansions (the
authors cite Tamaki et al. and Kawai & Kawai; §3.2).

## Extension to RANS: the Spalart–Allmaras equation

[Lodares et al. (2022)](/sources/lodares-2022.md) extend the entropy
analysis from the Navier–Stokes equations to the compressible RANS
equations closed by the
[Spalart–Allmaras model](/methods/spalart-allmaras-model.md), whose
working variable $\rho\tilde\nu$ is a sixth conserved component; to the
authors' knowledge no earlier work had derived entropy-stable DGSEM schemes
for RANS systems (§1). Page-local: $[\![\phi]\!]=\phi_R-\phi_L$ the jump
across a face; $P_{\tilde\nu}$, $D_{\tilde\nu}$ the production and
destruction of the SA equation; $\nu_{\mathrm{SA}}$ its diffusion
coefficient ($\nu+\tilde\nu$ for $\tilde\nu\ge0$; the source's
$\hat\sigma$); $\boldsymbol Q$ the conserved state; $\sigma$, $c_{b2}$ the
SA constants (2/3 and 0.622).

**The SA entropy.** The mathematical entropy of the Navier–Stokes part
(either the kinetic energy or the thermodynamic entropy
$-\rho s/(\gamma-1)$) is augmented by an SA "energy" (§3.2, Eqs. 38–39)
$$\mathcal E_{\mathrm{SA}}=\tfrac12\rho\tilde\nu^2,\qquad \boldsymbol W_{\mathrm{SA}}=\frac{\partial\mathcal E_{\mathrm{SA}}}{\partial\boldsymbol Q}=\big(-\tfrac12\tilde\nu^2,0,0,0,0,\tilde\nu\big).$$
Because $\boldsymbol W_{\mathrm{SA}}$ vanishes in the momentum and energy entries and the
Navier–Stokes entropy variables vanish in the sixth, the contraction of
state, inviscid and viscous fluxes splits into the known Navier–Stokes part
and an independent SA part, and "no modification of the NSE part will be
required" (§3.2, Eqs. 39–43). The continuous SA dissipation is (Eq. 49)
$$\mathcal D_{\mathrm{SA}}=\int\rho\tilde\nu(D_{\tilde\nu}-P_{\tilde\nu})\,d\boldsymbol x+\int\frac{\rho}{\sigma}\big(\nu_{\mathrm{SA}}-c_{b2}\tilde\nu\big)\lvert\nabla\tilde\nu\rvert^2\,d\boldsymbol x\ \ge\ \int\rho\tilde\nu(D_{\tilde\nu}-P_{\tilde\nu})\,d\boldsymbol x,$$
(integrals over the domain) provided $c_{b2}\le1$ and
$\nu_{\mathrm{SA}}\ge0$. The total
entropy can therefore grow only where production exceeds destruction; "if
the destruction of turbulent viscosity leads over the production, the
system will be fully–stable" (§3.2, Eq. 50). For $\tilde\nu<0$ the
authors use a variant of the negative SA model with
$P_{\tilde\nu}-D_{\tilde\nu}=c_{b1}(1-c_{t3})\lvert\Omega\rvert\tilde\nu+c_{w1}(\tilde\nu/d)^2\ge0$,
which makes $\tilde\nu(D_{\tilde\nu}-P_{\tilde\nu})\ge0$, and they clip the
diffusion coefficient to $\nu_{\mathrm{SA}}=\max(\nu+f_n\tilde\nu,0)$ ($f_n$ the
diffusion function of the negative model) to keep
it non-negative (§2, Eqs. 16–17). The proof also needs non-negative
viscosity and heat conductivity after the turbulent increments (§3.1).

**Discrete construction.** On Gauss–Lobatto DGSEM with the
summation-by-parts property and discrete metric identities (curvilinear
hexahedra), any Navier–Stokes two-point flux of the form
$(\widehat{\rho U},\widehat{\rho U}\{\!\{U\}\!\}+\hat P,\dots,\widehat{\rho UH})$
extends to SA by the sixth component $\widehat{\rho U}\{\!\{\tilde\nu\}\!\}$,
which satisfies Tadmor's jump condition for $\mathcal E_{\mathrm{SA}}$ for **any**
momentum average $\widehat{\rho U}$, through
$2[\![\tilde\nu]\!]\{\!\{\tilde\nu\}\!\}=[\![\tilde\nu^2]\!]$ (§4.3, Eq. 68;
§5.1.2, Eqs. 87–89). With $\widehat{\rho U}=\{\!\{\rho\}\!\}\{\!\{U\}\!\}$
(Pirozzoli) the scheme is kinetic-energy preserving, with
$\rho^{\ln}\{\!\{U\}\!\}$ (Chandrashekar) entropy conserving. The SA
interface flux
$F^{*}_{6}=F^{*}_{1}\{\!\{\tilde\nu\}\!\}-\tfrac12\lambda_\nu\lvert F^{*}_{1}\rvert[\![\tilde\nu]\!]$
($F^*_1$ the mass flux; $\lambda_\nu=0$ central, $\lambda_\nu=1$ upwind,
the default) produces the interface entropy
$\tfrac12\lambda_\nu\lvert(\rho U_n)^*\rvert[\![\tilde\nu]\!]^2\ge0$ (§4.4,
Eq. 74; §5.2.1, Eq. 107); BR1 viscous fluxes leave no interior boundary
term (Eq. 108); and adiabatic free- and no-slip walls built from a mirrored
ghost state with $-\rho\tilde\nu$ are entropy stable (§4.5.1, §5.2.2,
Eqs. 75–77, 110–115). Inflow and outflow boundaries "can increase and/or
decrease the entropy" and are not covered (§4.5). Two configurations
result: Pirozzoli split form with Lax–Friedrichs (kinetic energy, with the
pressure-work term of the KEP page) and Chandrashekar split form with
matrix dissipation (thermodynamic entropy), whose semi-discrete entropy
laws mirror the continuous one (§5.3, Eqs. 116–118).

**Evidence.** On a periodic random initial condition (viscosity and heat conductivity $10^{-8}$,
$N=10$, $10^3$ elements, central fluxes, $\tilde\nu$ random in
$[-0.5,0.5]$) the standard DGSEM diverges while the Chandrashekar and
Pirozzoli forms stay stable with zero entropy remainder (§7.2, Figs. 5–6).
A [manufactured solution](/methods/method-of-manufactured-solutions.md)
gives spectral convergence for all three forms (§7.1), and the NASA
flat plate and [NACA 0012](/benchmarks/naca-0012-airfoil.md) RANS cases run
with the Pirozzoli form on the coarsest TMR grids (§7.3–7.4; numbers on
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md) and the
benchmark page). The authors suggest that the approach can serve other
RANS models and a [detached-eddy simulation](/methods/detached-eddy-simulation.md)
coupling entropy-stable RANS near walls with entropy-stable LES (§1, §8).

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

**Entropy stability as a requirement of LES by weak solutions.**
[Svärd (2022)](/sources/svard-2022.md) proposes to replace explicit
subgrid models by numerical approximations of weak entropy solutions of the
compressible Navier–Stokes equations, whose local averages over a fixed
test-function support converge on coarser grids than point values and are
read a posteriori as filtered quantities (§2.3; see
[implicit LES](/definitions/implicit-les.md)). From the a priori estimates
that a theory of weak solutions needs, the author lists five conditions
conjectured necessary, not sufficient (§3): **A** conservation form;
**B** entropy stability, which with a temperature-dependent conductivity
$\kappa_0(1+T^{p_\kappa})\le\kappa_h\le\kappa_1(1+T^{p_\kappa})$
($\kappa_h$ the heat conductivity, $p_\kappa$ an integer, e.g. 2,
$\kappa_0$, $\kappa_1$ constants; page-local, not the von Kármán
constant) bounds $\nabla T$ in $L^2$,
whereas a constant conductivity bounds only $\nabla\ln T$ (Eq. 11);
**C** at least the diffusion of a kinetic-energy-preserving flux, so that
the discrete kinetic- and internal-energy balances hold without velocity
remainders; **D** positive density; **E** a linearly stable (non
anti-diffusive) continuity equation, because physical diffusion controls
velocity and temperature gradients but not density gradients. Citing
earlier work, the author states that entropy-conservative fluxes such as
Ismail–Roe and Chandrashekar violate E and can amplify numerical errors
that "trip unphysical turbulence", and that a scheme that is nonlinearly
but not linearly stable does not blow up, so boundedness alone does not
show that a solution approximates the true one (§3).

The proposed one-dimensional flux (§4, Eqs. 20–23) modifies Chandrashekar's
EC and KEP flux only in the mass flux. With $[\![\phi]\!]=\phi_{i+1}-\phi_i$
the jump, $\beta_{\mathrm C}=1/(2RT)$ the inverse-temperature variable
and $a^\rho$ the mass-flux diffusion coefficient (all page-local),
$$\begin{aligned}
f^\rho&=\{\!\{\rho\}\!\}\{\!\{u\}\!\}-a^\rho[\![\rho]\!],\qquad a^\rho=\tfrac12|\{\!\{u\}\!\}|+\tfrac14|[\![u]\!]|,\\
f^m&=\frac{\{\!\{\rho\}\!\}}{2\{\!\{\beta_{\mathrm C}\}\!\}}+\{\!\{u\}\!\}f^\rho,\qquad
f^E=\Big(\frac{1}{2(\gamma-1)\beta_{\mathrm C}^{\ln}}-\tfrac12\{\!\{u^2\}\!\}\Big)f^\rho+\{\!\{u\}\!\}f^m,
\end{aligned}$$
with first-order viscous and heat fluxes. Because the momentum and energy
fluxes differ from Chandrashekar's (mass flux $\rho^{\ln}\{\!\{u\}\!\}$)
only through $f^\rho$, Tadmor's shuffle condition reduces to
$(f^\rho-\rho^{\ln}\{\!\{u\}\!\})[\![\rho]\!]/\rho^{\ln}\le0$, which holds
since $|\{\!\{\rho\}\!\}-\rho^{\ln}|\le\tfrac12|[\![\rho]\!]|$; the viscous
terms contribute
$\tfrac{8\mu}{3h}\{\!\{\beta_{\mathrm C}\}\!\}[\![u]\!]^2+\tfrac{\kappa_h}{Rh}\tfrac{[\![T]\!]^2}{T_iT_{i+1}}\ge0$
(§4, Eqs. 26–33). Proposition 4.1 states that the scheme satisfies
Conditions A–E; the mass flux is $\{\!\{\rho u\}\!\}-(a^\rho+\tfrac14[\![u]\!])[\![\rho]\!]$
with a non-negative coefficient, a standard artificial diffusion (Eq. 25).

On a two-dimensional Kelvin–Helmholtz instability ($\mu=\kappa_h=10^{-4}$,
$N^2$ grids, box means of the conserved variables over
$[0.2,0.4]\times[0.5,0.7]$) the box means of the proposed scheme differ by
less than 10% between $N=128$ and 512 (density 2.036, 1.985, 2.000 for
$N=128$, 256, 512), and Chandrashekar's flux with the same viscosity gives
more small-scale roll-ups and a coarse-to-fine density difference of 4.1%
against 1.8% (2.075, 1.975, 1.993), which the author reads as support that
"local stability improves results on coarse meshes" (§5.2, Figs. 3–4,
Tables 1, 3). The Euler version ($\mu=\kappa_h=0$) of the proposed scheme
gives spurious roll-ups, highly grid dependent and "essentially
non-predictive" box means (Table 2). On the Taylor–Green vortex at
$Re=1600$ Chandrashekar's flux gives very similar results, its unstable
continuity equation showing only as a more oscillatory dissipation curve on
$32^3$ (§5.3, Fig. 7).

**Passing mentions.** The centred component of the
blended flux of [van Noordt et al. (2022)](/sources/vannoordt-2022.md), §2.3,
is the fourth-order kinetic-energy- and entropy-preserving scheme of Kuya et
al. and Totani et al. (see [WENO](/methods/weno-scheme.md));
[Hamedi & Vermeire (2022)](/sources/hamedi-2022.md), §1, list
entropy-stable schemes among the remedies for the nonlinear instability of
under-resolved high-order simulation, "generally challenging and
computationally expensive", and use modal filtering instead
([explicit modal filtering](/methods/explicit-modal-filtering.md)).
[Mani & Dorgan (2023)](/sources/mani-2023.md), §4.4, an industrial review
of aerospace CFD, list kinetic-energy-preserving fluxes (Honein & Moin,
Jameson) and a "kinetic energy- and entropy-preserving (KEEP) algorithm",
citing Chandrashekar (2013) and Kuya & Kawai (2020) for it, among the
reduced-dissipation discretizations that scale-resolving simulation
needs, and cite the [CharLES](/software/charles.md) wall-modelled LES of
Goc et al. (2021) with a KEEP scheme, which predicted the maximum lift of
the High-Lift Prediction Workshop configuration (see
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md)).

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
  properties on this page are semi-discrete. Kuya et al. (2018, App. C,
  Figs. 12–17) find that their KEEP scheme produces entropy at CFL
  $\approx1$ and with third-order TVD Runge–Kutta, and run classical RK4 at
  CFL $\approx0.1$, which overlaps CFL $\approx0.01$.
- **Real gases.** Bernades et al. (2023, §5) liken their chain-rule barrier
  to pressure-equilibrium preservation to the difficulty of entropy
  conservation with arithmetic-average fluxes, and name non-linear-average
  finite-volume fluxes as a possible remedy, "expected to be cumbersome"
  for the Peng–Robinson equation of state (a conjecture).

## Qualifications

- **"Entropy stable" with a source term.** In Lodares et al. (2022) the
  bound admits entropy growth wherever SA production exceeds destruction
  (Eq. 50), so the property is stability relative to the source, not
  unconditional decay; the proof covers adiabatic walls and periodic
  boundaries only (§4.5). The paper names its second configuration
  "thermodynamic entropy stable" (§4.6), "entropy conserving schemes with
  the matrix dissipation numerical flux" (§5.3) and "thermodynamic entropy
  conserving" (abstract); with matrix dissipation it is entropy stable.
  Eq. (93) carries the superscript NS on the SA viscous term.

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
- **Local linear stability against entropy conservation.** Svärd (2022)
  holds entropy-conservative fluxes unsuited as stand-alone turbulence
  schemes because their continuity equation is not locally linearly
  stable, and shows it on a two-dimensional Kelvin–Helmholtz box mean;
  Aiello et al. (2026) find entropy-conservative convection decisive for
  robustness in channel DNS, and Brillon & Nadarajah (2026) find EC and
  KEP fluxes equivalent on the Taylor–Green vortex. Svärd adds a mass-flux
  diffusion to an EC flux rather than rejecting it, and on the
  Taylor–Green vortex finds Chandrashekar's flux "very similar"; the
  statements concern different flows, gases and measures, so no
  contradiction is recorded.
- **Printed slips (Svärd 2022).** §4 calls the total flux of Eq. (20) "the
  sum of the inviscid and viscous" fluxes, with $f^{V2}=+\tfrac43\mu[\![u]\!]/h$,
  which with the update $(u_i)_t+(f_{i+1/2}-f_{i-1/2})/h=0$ would make the
  viscous term anti-diffusive, whereas Eq. (12) puts the viscous flux on the
  right-hand side and the kinetic-energy derivation uses the difference
  *(compiler check, not in the sources)*; one term of that derivation lacks
  the factor $\mu$. The positivity proof uses
  $a^\rho>\tfrac12|\{\!\{u\}\!\}|$, which becomes an equality when
  $[\![u]\!]=0$, so only the non-strict inequality holds, which still
  suffices for $(\rho_i)_t\ge0$ *(compiler check, not in the sources)*. In
  §5.2, the finest-mesh differences of Chandrashekar's flux to Table 1 are
  "less than 1%", but for the $x$-momentum they are 1.4% (0.215 against
  0.212), and the Euler momentum errors "33% and 42%" are 33.5% and 29.6%
  relative to the Table 1 values (42% only if normalized by the Euler value)
  *(compiler check, not in the sources)*. The abstract announces a
  turbulent Rayleigh–Taylor test that the paper does not run (the third
  test is a Taylor–Green vortex).
- **"KEEP" in Mani & Dorgan (2023).** The review groups under the KEEP
  label Chandrashekar (2013), whose cited title is "Kinetic energy
  preserving and entropy stable finite volume schemes", with Kuya & Kawai
  (2020). The review states no property of its own.
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
- [Kuya et al. (2018)](/sources/kuya-2018.md) — version of record with appended corrigendum: §1.2, Eqs. (6)–(7) (entropy from the Gibbs relation); §4.1–4.5, Eqs. (55)–(71) (spurious entropy from inconsistent kinetic-energy, internal-energy, pressure-diffusion and enthalpy fluxes); §5.2–5.3, Figs. 1–11; App. C, Figs. 12–17 (time step and integrator).
- [Svärd (2022)](/sources/svard-2022.md) — §2.3 (weak solutions, a posteriori averages); §3, Eqs. (10)–(15) (a priori estimates, Conditions A–E, linear instability of EC fluxes); §4, Eqs. (16)–(34), Proposition 4.1 (entropy-stable, KEP-diffusive, positive mass-flux-diffused scheme); §5.2–5.3, Tables 1–3, Figs. 2–4, 7; slips in §4, §5.2 and the abstract.
- [van Noordt et al. (2022)](/sources/vannoordt-2022.md) — §2.3 (KE/EP central component of the blended flux).
- [Hamedi & Vermeire (2022)](/sources/hamedi-2022.md) — §1 (entropy-stable schemes as a costly alternative to filtering).
- [Lodares et al. (2022)](/sources/lodares-2022.md) — §1; §2, Eqs. (13)–(17) (compressible SA, negative variant, clipped diffusion); §3.1–3.2, Eqs. (29)–(50) (SA entropy, split analysis); §4.3–4.5, Eqs. (68)–(77) (two-point flux, interface flux, walls); §5, Eqs. (83)–(118) (semi-discrete entropy laws); §7.1–7.2, Figs. 3–6.
- [Mani & Dorgan (2023)](/sources/mani-2023.md) — §4.4 (KEP and KEEP fluxes for scale-resolving simulation, cited; CharLES KEEP at high lift, cited).
