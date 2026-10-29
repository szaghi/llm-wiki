---
type: Property
title: "Pressure-equilibrium preservation"
description: "A scheme is pressure-equilibrium preserving when uniform pressure and velocity stay uniform under density variations; for a general equation of state, evolving total or internal energy makes this exact only with a discrete chain rule (second order at best), while evolving pressure makes it exact at the price of total-energy conservation."
status: established
aliases: [PEP, pressure equilibrium preserving scheme, KGP-Pt, KGP-PT scheme, pressure-equilibrium-preserving split form, CDHD, central differential flux with high-order dissipation, primitive-variable hybrid scheme]
tags: [pressure-equilibrium, kinetic-energy-preserving, compressible, real-gas, numerical-dissipation, dns]
timestamp: 2026-10-29T07:42:00Z
---

# Pressure-equilibrium preservation

A semi-discretization of the compressible Euler or Navier–Stokes equations is
**pressure-equilibrium preserving (PEP)** when it has "the property of
maintaining constant pressure when both pressure and velocity are initially
uniform", whatever the density field ([Bernades et al. 2023](/sources/bernades-2023.md),
§1, §3.1.2). The continuous equations have it: a density wave advected at
uniform $u$ and $p$ changes neither. A discretization that lacks it creates
spurious pressure oscillations at density interfaces, which in
[DNS](/definitions/direct-numerical-simulation.md) and LES of real-gas
(transcritical) turbulence contaminate the velocity and can make the run
diverge. Bernades et al. treat PEP as a companion of
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md)
(KEP): KEP depends only on the discretization of the continuity and momentum
equations, PEP on the choice of the energy variable and its discretization
(§3.1.2).

Page-local notation (Bernades et al. 2023, translated): $e$ the specific
internal energy and $e_t=e+\tfrac12|\boldsymbol u|^2$ the specific total
energy, so that the registry's total energy per unit volume is $E=\rho e_t$;
$p=p(\rho,e)$ a general equation of state with Jacobians
$p_\rho=(\partial p/\partial\rho)_e$, $p_e=(\partial p/\partial e)_\rho$; $c$
the speed of sound, $c^2=p_\rho+p\,p_e/\rho^2$; $D_x$ the second-order
centred difference matrix (the source's $\delta_x$; it satisfies summation by
parts but not the product rule); $C_{\rho\phi}$ the semi-discrete convective
term of $\rho\phi$; $W_p$ the pressure-work term of the energy equation (the
source's $\Pi_{\rho E}$, renamed because $\Pi$ is the SGS flux); $a_{\mathrm K}$
(with $D_x$, registry §11), $a_e$, $a_p$ the weights the source calls $\xi$, $\chi$, $\eta$ (renamed
because these letters are the registry's reference coordinate, SA ratio and
Kolmogorov length); $p^h_\rho$, $p^h_e$ the discrete Jacobians of a discrete
chain rule (the source's tilded Jacobians, the tilde being the registry's
Favre filter). Bernades et al. write the pressure $P$; it is $p$ here.

## Continuous argument and the induced pressure equation

For a general equation of state, $\partial_tp=p_\rho\partial_t\rho+p_e\partial_te$
turns the energy equation into an equivalent pressure equation (§2.1,
Eqs. 2–4); in one dimension, without viscous terms (§3.1.2, Eq. 15),
$$\partial_tp=-\partial_x(pu)-(\rho c^2-p)\,\partial_xu,$$
so that uniform $u=u_0$, $p=p_0$ (page-local; the source's overbar, which
is the registry's LES filter) give $\partial_tp=0$; the velocity equation (Eq. 14)
likewise gives $\partial_tu=0$. In the semi-discrete setting, under uniform
$u$ every split form of $C_\rho$, $C_{\rho u}$ reduces to
$C_\rho=u_0D_x\rho$, $C_{\rho u}=u_0^2D_x\rho$ (Eq. 16), so the
induced velocity equation keeps $u$ uniform for any split; the question is
the induced pressure equation (Eqs. 17–18).

**Total energy as the variable.** Evolving $\rho e_t$ gives the induced
pressure equation (Eq. 20)
$$\partial_tp=\Big[\frac{p_e}{\rho}e-p_\rho\Big]u_0\,D_x\rho-\frac{p_e}{\rho}\big[C_{\rho e}+W_p\big].$$
Writing the internal-energy convection at uniform velocity as
$C_{\rho e}=a_eu_0D_x(\rho e)+(1-a_e)u_0(eD_x\rho+\rho D_xe)$
(Eq. 21), a term $a_e\ne0$ leaves $D_x(\rho e)$, which cannot be reduced
without a discrete product rule. With $a_e=0$ and a pressure term that
vanishes at equilibrium, the condition becomes (Eq. 22)
$$\partial_tp=-u_0\,(p_\rho D_x\rho+p_eD_xe)\approx-u_0\,D_xp=0,$$
which holds exactly only if the derivative operator satisfies a **discrete
chain rule** $D_xp=p^h_\rho D_x\rho+p^h_eD_xe$ (Eq. 23). Bernades et al.
cite Ranocha: second-order centred differences satisfy such
a chain rule with discrete Jacobians accurate to second order at interior
nodes, and the result "cannot be generalized" to higher-order operators
(§3.1.2).

**Ideal gas.** For an ideal gas the first bracket of Eq. (20) cancels and
PEP reduces to $C_{\rho e}+W_p=0$; Shima et al. achieve it with
$C_{\rho e}=\tfrac12(C^D_{\rho e}+C^u_{\rho e})$ (the PEP-IG scheme, which
Bernades et al. 2023, §3.1.2, cite), where $C^D$ is the divergence
form and $C^u$ the split form that factors the velocity out (Eq. 9).

**Internal energy as the variable.** Evolving $\rho e$ with
$\partial_t(\rho e)=-C_{\rho e}-pD_xu$ (Eq. 24) gives the induced equation
(Eq. 25) $\partial_tp=[\tfrac{p_e}{\rho}e-p_\rho]u_0D_x\rho-\tfrac{p_e}{\rho}C_{\rho e}$:
again a chain rule is needed. Such schemes conserve total energy when the
convection is KEP, $C_{\rho e}$ is locally conservative and the induced
pressure term is an advective form of $D_x(pu)$ (§3.1.2).

**The barrier.** Bernades et al. conclude that "the discrete chain rule
appears to constitute a barrier for the development of PEP methods, at least
for discretizations based on linear finite-differencing schemes"; with total
or internal energy evolved, "the discrete pressure-equilibrium condition can
be fulfilled at most to second-order accuracy" (abstract, §3.1.3). They
liken it to the long-standing difficulty of entropy conservation with
arithmetic-average fluxes, and name finite-volume fluxes with non-linear
averages as a possible remedy, "expected to be cumbersome" for the
Peng–Robinson equation of state (§5, a conjecture).

## The pressure-equation route: KGP-Pt

Evolving the pressure itself (Eq. 26),
$$\partial_tp=-C_{\mathrm{pr}}-(\rho c^2-p)\,D_xu,\qquad C_{\mathrm{pr}}=a_pD_x(pu)+(1-a_p)\,(pD_xu+uD_xp),$$
with $C_{\mathrm{pr}}$ the convective term of the pressure equation (the
source's $C_p$, renamed because $C_p$ is the registry's pressure
coefficient),
gives $\partial_tp=0$ at equilibrium for any $a_p$: PEP is exact. The price
is **total-energy conservation (TEC)**: the induced total-energy equation
(Eqs. 27–28) splits into induced internal, kinetic and pressure parts plus a
spurious term, and is conservative only with both an exact chain rule and a
product rule. The kinetic-energy part is conservative for any KEP scheme, so
the TEC error is "only an incorrect induced internal-energy balance" (§3.1.2).

The scheme Bernades et al. propose, **KGP-Pt**, uses the Kennedy–Gruber–Pirozzoli
(KGP) split for mass and momentum (the member $a_{\mathrm K}=\tfrac12$ of the
locally conservative KEP family on the
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md)
page) and the pressure equation with $a_p=0$. It is PEP and preserves mass,
momentum and kinetic energy globally and locally, but not total energy;
to the authors' knowledge it is new (§3.1.3).

**Properties of the schemes compared** (Table 1; general equation of state,
KGP continuity and momentum in all rows; ○ = only the chain rule needed):

| Scheme | energy variable | TEC | PEP |
|---|---|---|---|
| KGP-Et (KGP split of the total enthalpy) | total energy | yes | no (product and chain rules needed) |
| KGP-Et-CR ($C_{\rho e}=C^\phi_{\rho e}$, $a_p=1$) | total energy | yes | ○ |
| KGP-et-CR ($C_{\rho e}=C^\phi_{\rho e}$) | internal energy | yes | ○ |
| KGP-Pt ($a_p=0$) | pressure | no | yes |
| PEP-IG of Shima et al. | internal energy | yes | no (for a general equation of state) |

The CR class (total energy with $a_e=0$, any split of the kinetic-energy
convection, any pressure-term weight) needs only the chain rule; in the
tests it gave "no practical advantage" (§4.1.2).

## Tests

All tests use second-order centred differences and classical RK4 at
acoustic CFL 0.3, and compare also a divergence form with a fourth-order
compact filter (D+F4), a pressure-based divergence form with filter
(D-Pt+F4), an HLLC double-flux scheme (UB-Df), KGP with double flux (KGP-Df)
and, for the ideal gas, a Ducros-sensor hybrid of KGP and HLLC (H) (§3.2,
Table 2).

- **Ideal-gas density wave** (41 points, $t/t_c=11$; §4.1.1, Fig. 1): only
  the divergence form, PEP-IG and KGP-Pt are free of pressure oscillations;
  KGP-Et is not; the upwind and hybrid schemes damp the density wave, the
  Ducros sensor being "mostly activated by the oscillations".
- **Transcritical nitrogen density wave** (5 MPa, density ratio from
  0.182 to 2.531 of the critical density; §4.1.2, Figs. 2–3): KGP-Et is not
  PEP; PEP-IG is not PEP for a real gas; double flux keeps pressure
  equilibrium only with upwinding (UB-Df), not with KGP; filtering does not
  suppress the oscillations, which are worst across the pseudo-boiling
  line; only D-Pt+F4 and KGP-Pt hold pressure equilibrium. Under refinement
  the total-energy error of KGP-Pt decays on average as $O(h^2)$ and is
  dissipative (total energy decreased in every case), while the PEP error of
  the energy-based schemes is mostly second order.
- **Inviscid transcritical mixing layer** ($256\times128$, $128\times64$,
  $64\times32$; §4.2, Figs. 4–7): KGP-Pt conserves mass and momentum to
  machine accuracy, recovers TEC at $O(h^2)$ over the three grids and shows
  "good conservation" of global entropy although it is not entropy
  preserving; kinetic energy decays slightly, "supposedly as a result of the
  temporal integrator". On $64\times32$, KGP-Et produces noisy pressure that
  contaminates the velocity and diverges shortly after $t/t_c=0.2$, while
  KGP-Pt stays smooth without artificial mechanisms: "the KEP property alone
  is not sufficient to tackle transcritical flows".
- **Transcritical channel DNS** ($Re_\tau=100$ on bottom-wall values,
  $128^3$, isothermal walls at $0.75$ and $1.5$ times the critical
  temperature; §4.3, Figs. 8–10): KGP-Pt and KGP-Et agree to plotting
  accuracy in mean and Favre-fluctuation statistics; the lack of TEC caused
  no deviation. There "pressure oscillations are mitigated by physical
  viscosity and standard KEP schemes can be profitably applied" (§4.3, §5).

## Primitive-variable hybrids for transcritical flow

[Xu et al. (2026)](/sources/xu-2026.md) also evolve the pressure where
the flow is smooth, for inviscid real-gas (Peng–Robinson nitrogen) flow
without turbulence. Their premise (§1) is that conservative schemes
"often generate severe unphysical pressure oscillations" at transcritical
interfaces, while non-conservative formulations (double flux, pressure
evolution) "come at the cost of energy conservation error", which can
misplace shocks; fully conservative PEP schemes (Fujiwara et al., Terashima
et al., and Bernades et al. 2023) are judged "not easily extended to general
transcritical flows", and the DG $L^2$-projection approach of Ching et al.
"can still result in small deviations from pressure equilibrium" (§1; these
are the authors' judgements, not tested). Their scheme is a hybrid (§3):

- in cells flagged by a pressure-ratio sensor built on the
  primitive-variable Riemann solver (threshold 0.05 on the interface
  pressure ratio with a compressive wave speed, Eq. 18), a conservative
  finite-volume update with fifth-order [WENO](/methods/weno-scheme.md)
  reconstruction of the primitive variables and a real-gas Roe flux;
- elsewhere a primitive update of $(\rho,u,p)$, whose third row is the
  pressure equation $\partial_tp+u\,\partial_xp+\rho c^2\partial_xu=0$,
  discretized by the **central differential flux with high-order
  dissipation (CDHD)**: a two-point central difference of the WENO-5
  interface states, multiplied by the quasi-linear matrix at the cell
  average, plus an upwind dissipation built from the path-integral
  fluctuations of the Dumbser–Osher–Toro solver evaluated on the
  high-order interface jump (§3.5, Eqs. 20–23).

By a formal Taylor argument, with $h$ the uniform cell size, the interface
jump is $O(h^5)$, the dissipation term $O(h^4)$ and the central term
$O(h^2)$, so
the scheme is second order in smooth flow, the WENO-5 interface accuracy
not raising the order of the central difference (§4, Eqs. 24–41; the
expansion assumes no eigenvalue sign change along the integration path).
In periodic advection of a transcritical "droplet" (512 points, ten
traversals) the primitive update keeps velocity and pressure uniform, and
the relative total-energy error at the end is about $3.95\times10^{-4}$,
against about 10% for a first-order primitive Dumbser–Osher–Toro scheme
(§5.1.1–5.1.2, Figs. 2–3); the abstract's "two order of magnitude"
reduction "compared to traditional primitive-variable approaches" rests on
that first-order comparator only. Without the dissipation term the central
primitive update develops density and temperature oscillations that "blow
up the simulation quickly" (600 steps at CFL 0.8, §5.1.4, Fig. 5). A
two-dimensional droplet ($151\times151$ cells) keeps its shape and uniform
pressure and velocity (§5.3, Fig. 7, contour plots only).

The trade is the one Bernades et al. (2023) identify for KGP-Pt: exact
pressure equilibrium from evolving the pressure, a total-energy error that
decays with resolution (§5.1.3, Table 1, observed order approaching 2 for
the total energy), and a conservative scheme kept for shocks.

**Pressure-equilibrium-preserving fluxes in turbulence runs.**
[Brillon & Nadarajah (2026)](/sources/brillon-2026.md), §3.1.6, include
Ranocha's modification of the Chandrashekar flux, which is
entropy-conserving, kinetic-energy preserving and PEP, among the two-point
fluxes of their split-form flux reconstruction; on the viscous Taylor–Green
vortex at $M_\infty=0.1$ it is "nearly indistinguishable" from the fluxes
without the PEP property. [Aiello et al. (2026)](/sources/aiello-2026.md),
§3.2 and Table 1, list Ranocha's flux as PEP, exactly
[entropy-conserving](/properties/entropy-conservation.md) for a calorically
perfect gas but not for a thermally perfect one; in their Mach 5 channel
DNS of CO$_2$ it lies between the entropy-conserving and the
non-entropy-conserving schemes (§4.2, Table 3). They also find that the
discretization of the pressure term of the momentum equation matters: the
entropy-conserving scheme of Gouasmi et al., whose pressure term is
$R\{\!\{\rho\}\!\}/\{\!\{1/T\}\!\}$ instead of $\{\!\{p\}\!\}$
($R$ the gas constant, page-local), differs from EC-TP by 5.25% in the
streamwise Reynolds stress (max-norm relative difference) at Mach 5 (§4.2, Table 3), so that "appropriate
thermodynamic coupling in the pressure treatment" is, with entropy
consistency, "essential" (§5).

**Both routes in a GPU DNS solver.** The open-source GPU-resident
solver RHEA-X of [Monteiro et al. (2026)](/sources/monteiro-2026.md),
§2.3.1, Eqs. (21)–(23), carries one scheme of each route next to its KGP
baseline. For ideal gases, the KEEP scheme of Kuya & Kawai with the
pressure-equilibrium-preserving internal-energy flux of Shima et al.
(both cited), whose pressure–velocity part at the face between points $m$
and $m+1$ is printed as
$$I^{\mathrm{pe}}_j=\frac{(p_{m+1}+p_m)(u_{j,m+1}+u_{j,m})}{4(\gamma-1)},$$
($I^{\mathrm{pe}}_j$ page-local, the source's $\tilde I_j$; the tilde is the registry's Favre filter), stated to keep a
uniform pressure invariant and recommended for weakly compressible and
variable-density ideal-gas DNS at low Mach number. For real fluids, the
KGP-Pt pressure equation of Bernades et al. with $a_p=0$ (the source's
$\eta$), with the viscous and conductive source terms of the pressure
equation scaled by a ratio of two thermodynamic coefficients that the
paper does not define (Eq. 22); total energy is not strictly conserved,
"the residual error is dissipative and decays quadratically with grid
refinement", and the scheme is preferred for transcritical and
supercritical flows. The pressure is advanced in lockstep with the
conserved variables and updated first at each Runge–Kutta stage
(Algorithm 1). This real-fluid configuration (Peng–Robinson equation of
state, Chung et al. transport) is the baseline of the performance study;
on CPUs real-fluid thermodynamics adds 82–88% to the run time (§5.1).
The supercritical nitrogen jet they validate with it agrees with Raman
density data (§4.5, Fig. 8).

**Named but not used in an LES comparison.** [Volpiani (2024)](/sources/volpiani-2024.md),
§2.2.3, lists pressure-equilibrium-preserving and entropy-preserving split
forms (Shima et al., De Michele & Coppola, Bernades et al.) among the
alternatives to the three kinetic-energy split forms the paper compares, and does
not treat them. The energy equation is split on the total specific
enthalpy after Pirozzoli, and the Kennedy–Gruber variant (SF3) applies the
quarter weights to mass, momentum and energy, which is the KGP-Et row of
the table above, not pressure-equilibrium preserving even in the
ideal-gas density-wave test of Bernades et al. *(compiler check, not in
the sources)*; the paper's only test, the Taylor–Green vortex at $M=0.085$ with
uniform initial density, does not probe the property (see
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md)).

**The KEEP scheme at a density wave.** The kinetic-energy- and
entropy-preserving scheme of [Kuya et al. (2018)](/sources/kuya-2018.md)
(the KEEP row of the tables on
[entropy conservation](/properties/entropy-conservation.md); its fluxes are
on [kinetic-energy preservation](/properties/kinetic-energy-preservation.md))
evolves total energy with an internal-energy flux
$\{\!\{\rho\}\!\}\{\!\{u\}\!\}\{\!\{p/\rho\}\!\}/(\gamma-1)$ and the
pressure-diffusion flux $\tfrac12(u_mp_{m+1}+u_{m+1}p_m)$ (§3, Eq. 54).
The source makes no pressure-equilibrium claim and its tests start from
uniform density (§5.1). In one dimension with uniform $u_0$ and $p_0$ and an
ideal gas, its fluxes give $\partial_tu=0$ and
$$\partial_tp\big|_m=-\frac{u_0p_0}{h}\Big[\{\!\{\rho\}\!\}\{\!\{1/\rho\}\!\}\Big]_{m-1/2}^{m+1/2},\qquad
\{\!\{\rho\}\!\}\{\!\{1/\rho\}\!\}=\frac{(\rho_m+\rho_{m+1})^2}{4\rho_m\rho_{m+1}}\ge1,$$
which vanishes only where the face values of this ratio agree, so the
scheme is not pressure-equilibrium preserving at a density wave; in the
terms of Bernades et al. its internal-energy convection is not the
$\tfrac12(C^D_{\rho e}+C^u_{\rho e})$ of PEP-IG *(compiler check, not in the
sources)*.

## Remedies in high-order discontinuous schemes (a review)

The review of high-order discontinuous schemes (DG, flux reconstruction,
spectral difference) for multiphase and multicomponent flows of
[Lv & Ekaterinaris (2023)](/sources/lv-2023.md), §4.3, Figs. 3–4,
describes the same failure for material interfaces and contact
discontinuities with variable thermodynamic properties, and four
families of remedies, all from the cited literature:

- **Mechanism.** With constant thermal properties the energy equation
  reduces at an interface to a combination of the mass equations, so
  mechanical equilibrium survives numerical errors; with variable
  properties numerically triggered thermal non-equilibrium changes the
  internal energy and the thermal property, and the pressure oscillates.
  The oscillation is "spurious" where there is no physical diffusion.
- **γ-advection** (Abgrall; extended to WENO by Johnsen & Colonius and to
  DG by de Frahan et al.): an auxiliary advection equation for the ratio
  of specific heats, from which the pressure is evaluated. It fails for
  temperature-dependent properties and diffusion-dominated regimes.
- **Pressure evolution** (Karni; Terashima & Koshi; a DG version for
  turbulent flows) in place of the conservative energy equation, the
  route of KGP-Pt above; it may diverge for shock-containing problems.
- **Double flux**: each element sees an element-wise constant thermal
  property and the Riemann flux is evaluated twice per face, once with
  each side's ratio of specific heats. It preserves mechanical
  equilibrium and applies to general thermodynamic models, but relaxes
  energy conservation, which the authors call acceptable at low Mach
  number (deflagrations) and critical at supersonic conditions, where it
  gives wrong shock speeds; the hybrid of Lv & Ihme reverts to the
  conservative flux where a pressure-jump sensor flags a shock and
  recovers correct detonation speeds. The element-wise constant property
  is, in the authors' words, "a rather intrusive treatment in conflict
  with the core feature of discontinuous schemes", their multiple
  internal degrees of freedom. It has been adopted in the DGSEM.
- **Conservative $L^2$ projection of the equation of state** (Franchina et
  al.): the pressure computed from the equation of state is
  $L^2$-projected onto the DG solution space and used only in the
  convective flux, so the solution energy is unchanged; with artificial
  viscosity it keeps the pressure oscillation within "0.1%~1% relatively"
  for component-dependent heat capacities. Johnson & Kercher extended it
  to thermally perfect multicomponent reacting gases, preserving pressure
  equilibrium at constant temperature and giving bounded, decaying
  oscillations across a temperature jump.

The authors favour the last family as the one compatible with the
element polynomial. Of the limiters, WENO limiters applied blindly
produce pressure oscillations at such interfaces, and the limiter of
de Frahan et al. avoids them by limiting density, momentum, pressure and
the thermal property and rebuilding the energy (§4.2; see
[WENO](/methods/weno-scheme.md)). No turbulence test is part of the
review's evidence for any of the four.

## Qualifications

- The analysis is for second-order centred differences in one dimension;
  the authors state that results "generalize to SBP operators of any order
  unless otherwise indicated", and the chain-rule statement is the
  exception (§3.1).
- The "at most second order" statement concerns schemes that evolve total
  or internal energy for a general equation of state; for the ideal gas
  PEP-IG is exact (§3.1.2). The authors restrict their conclusion that TEC
  may be sacrificed to the regimes tested (§5).
- Time is treated analytically; Runge–Kutta errors are assumed small (§3.1).
- **Double flux in two sources.** Lv & Ekaterinaris (2023, §4.3) report,
  from the cited works, that double flux gives oscillation-free
  solutions; Bernades et al. (2023, §4.1.2) find that double flux keeps
  pressure equilibrium with an upwind (HLLC) flux but not with the KGP
  split; the first statement concerns DG with Riemann fluxes, the second
  centred differences. Xu et al. (2026, §1) judge the
  $L^2$-projection approach (in Ching et al.'s DG form) able to leave
  "small deviations from pressure equilibrium"; Lv & Ekaterinaris report
  a 0.1–1% oscillation level for Franchina et al.'s form.
- **Printed slips.** §4.2 gives the perturbation wavelength as
  $\lambda=1/k=1/3$ m for $k=6$; for $\sin(k\pi x)$ the wavelength is $2/k$,
  which the same section uses in $t_c=2/(k\Delta u)$ *(compiler check, not
  in the sources)*. Eq. (33) with $u_0=25$ m/s and $A_u=3/8$ gives far-field
  velocities 15.625 and 34.375 m/s, a difference of 18.75 m/s, while the
  text states $\Delta u=10$ m/s *(compiler check, not in the sources)*.
  Table 2 gives $N_f=1$ for the F4 filter, whose three coefficients need
  $N_f=2$ in Eq. (29) *(compiler check, not in the sources)*. The PEP-IG row of Table 1 lists a pressure-equation
  entry although that scheme evolves internal energy.
- Xu et al. (2026) is an arXiv preprint (v1) of an inviscid one- and
  two-dimensional study; it has no viscous term and no turbulence. Printed
  slips: §5.1.3 states that "least-squares fits over the three finest
  meshes yield convergence rates of $r=(2.17,2.17,2.21)$", values equal to
  the finest-pair rates of Table 1 (2.1740, 2.1740, 2.2075), whereas a
  least-squares slope over the three finest grids of Table 1 gives about
  2.02, 2.02 and 2.05 *(compiler check, not in the sources)*; §3 calls the
  quasi-linear matrix "the Jacobian of the inviscid flux written in
  primitive variables", which it is not (it is the primitive-variable
  matrix of Eq. 3) *(compiler check, not in the sources)*; the $\pm$
  labels of the interface states in §3.4 and §4.1 are the opposite of
  those of §3.2.

# Citations

- [Xu et al. (2026)](/sources/xu-2026.md) — arXiv 2508.21599v1: §1 (conservative against primitive formulations, prior PEP schemes); §3, §3.4–3.5, Eqs. (18)–(23) (hybrid, PVRS sensor, CDHD); §4, Eqs. (24)–(41) (truncation analysis); §5.1–5.3, Table 1, Figs. 2–7.
- [Brillon & Nadarajah (2026)](/sources/brillon-2026.md) — arXiv 2411.12108v1: §3.1.6, Fig. 16 (Chandrashekar–Ranocha PEP flux on the Taylor–Green vortex).
- [Aiello et al. (2026)](/sources/aiello-2026.md) — §3.2, Table 1 (Ranocha PEP; Gouasmi pressure term); §4.2, Table 3; §5.
- [Kuya et al. (2018)](/sources/kuya-2018.md) — §3, Eq. (54) (KEEP fluxes, from which the compiler check above is derived); §5.1 (uniform initial density in the tests).
- [Volpiani (2024)](/sources/volpiani-2024.md) — §2.2.3, Eqs. (14)–(17) (split forms with enthalpy splitting; PEP schemes named, not treated); §3.2 (Taylor–Green setup).
- [Bernades et al. (2023)](/sources/bernades-2023.md) — §1 (definition, requirements); §2.1, Eqs. (2)–(4) (pressure equation); §3.1, Eqs. (8)–(13) (semi-discrete framework, split forms, KEP family); §3.1.2, Eqs. (14)–(28) (induced pressure and energy equations, chain rule, CR class, KGP-Pt); §3.1.3, Table 1; §3.2, Table 2 (comparison schemes); §4.1, Figs. 1–3; §4.2, Figs. 4–7; §4.3, Figs. 8–10; §5.
- [Lv & Ekaterinaris (2023)](/sources/lv-2023.md) — §4.3, Figs. 3–4 (mechanism of spurious pressure oscillations with variable thermodynamics; γ-advection, pressure evolution, double flux and its hybrid, $L^2$-projected equation of state); §4.2 (interface-consistent WENO limiting; review).
- [Monteiro et al. (2026)](/sources/monteiro-2026.md) — §2.3.1, Eqs. (21)–(23) (KEEP-PEP for ideal gases, KGP-Pt with $a_p=0$ for real fluids in RHEA-X); Algorithm 1; §4.5, Fig. 8; §5.1.
