---
type: Method
title: "KEEP and KEEP-PE schemes"
description: "Second-order central split-form face fluxes for mass, momentum and total energy that preserve kinetic energy and keep entropy nearly conserved (KEEP, Kuya et al.), and the variant whose internal-energy flux also preserves pressure equilibrium (KEEP-PE, Shima et al.); the page gives the flux sets, the discrete energy, pressure and velocity equations they induce, their two-point and multicomponent forms, and the tests."
status: established
aliases: [KEEP scheme, KEEP-PE, KEEP_PE, kinetic energy and entropy preserving scheme, Shima flux, Shima et al. flux]
tags: [kinetic-energy-preserving, central-scheme, finite-difference, turbulence, low-dissipation]
timestamp: 2026-11-17T08:43:12Z
---

# KEEP and KEEP-PE schemes

The **KEEP** (kinetic energy and entropy preserving) schemes of Kuya,
Totani & Kawai and Kuya & Kawai discretize the convective terms of the mass,
momentum and total-energy equations with
[split convective forms](/methods/split-convective-forms.md) written as face
fluxes. Mass, momentum and total energy are conserved exactly, the kinetic
energy is preserved in the sense of
[kinetic energy preservation](/properties/kinetic-energy-preservation.md),
and the total entropy is nearly, though not exactly, conserved, with no
numerical dissipation. **KEEP-PE**, due to
[Shima, Kuya, Tamaki & Kawai (2021)](/sources/shima-2021.md), changes the
internal-energy flux only, so that the scheme is also
[pressure-equilibrium preserving](/properties/pressure-equilibrium-preservation.md):
uniform velocity and pressure with an arbitrary density stay uniform. The
Kuya et al. papers are not ingested; their scheme is recorded here as
Shima et al. print it (§2.2.1, Table 1).

## Face fluxes

On a uniform grid the semi-discretization is
$\frac{d}{dt}u_i=-(\hat f_{i+1/2}-\hat f_{i-1/2})/\Delta x$, with
$\{\!\{a\}\!\}=\tfrac12(a_i+a_{i+1})$ at face $i+1/2$ and the page-local
product mean $(\!(a;b)\!)=\tfrac12(a_ib_{i+1}+a_{i+1}b_i)$. With page-local
names for the parts of the face flux (Shima et al. Tables 1–2, Eq. (17)):

| flux | KEEP | KEEP-PE | KEP (Jameson, Pirozzoli) |
|---|---|---|---|
| mass $f_\rho$ | $\{\!\{\rho\}\!\}\{\!\{v\}\!\}$ | same | same |
| momentum $f_{\rho v}$ | $f_\rho\{\!\{v\}\!\}+\{\!\{p\}\!\}$ | same | same |
| kinetic energy | $f_\rho\,\tfrac12v_iv_{i+1}$ | same | $f_\rho\{\!\{\tfrac12v^2\}\!\}$ |
| internal energy $f_{\rho e}$ | $\{\!\{\rho\}\!\}\{\!\{e\}\!\}\{\!\{v\}\!\}$ | $\{\!\{\rho e\}\!\}\{\!\{v\}\!\}=\dfrac{\{\!\{p\}\!\}\{\!\{v\}\!\}}{\gamma-1}$ | — |
| pressure work | $(\!(p;v)\!)$ | same | — |
| enthalpy | — | — | $\{\!\{\rho\}\!\}\{\!\{e+p/\rho\}\!\}\{\!\{v\}\!\}$ |

The total-energy flux is the sum of the kinetic, internal and pressure-work
rows (KEEP, KEEP-PE) or of the kinetic and enthalpy rows (KEP). KEEP
discretizes the energy equation in the form
$\partial_tE+\partial_x(\tfrac12\rho\lvert v\rvert^2v)+\partial_x(\rho ev)+\partial_x(pv)=0$,
KEP in the enthalpy form (Eqs. (1)–(2), (8)–(11)). In several dimensions the
means carry the face-normal velocity and $\{\!\{p\}\!\}$ enters the normal
momentum component.

- The mass flux is the Kennedy–Gruber–Pirozzoli one ($\zeta=\tfrac12$ on
  [split convective forms](/methods/split-convective-forms.md)). Momentum
  flux $f_\rho\{\!\{v\}\!\}$ and kinetic-energy flux $\tfrac12f_\rho v_iv_{i+1}$
  are the structure that
  [Coppola & Veldman (2023)](/sources/coppola-2023.md) prove necessary and
  sufficient for kinetic-energy preservation of three-point schemes
  (Observation 7) *(compiler check, not in the sources: neither paper
  compares the two)*.
- KEEP's internal-energy flux is the cubic split of $\rho$, $e$ and $v$;
  KEEP-PE's is the quadratic split of $\rho e$ and $v$, the names
  [Jain & Moin (2022)](/sources/jain-2022.md) use for these face fluxes
  (§3.1). "The whole idea ... is not to split the internal energy ($\rho e$)",
  so that it reduces to the pressure (Shima et al. §2.2.3).
- In pointwise (finite-difference) form the KEEP-PE internal-energy term is
  $\partial_x(\rho ev)\simeq\tfrac12\big(\delta(\rho ev)/\delta x+v\,\delta(\rho e)/\delta x+\rho e\,\delta v/\delta x\big)$,
  $\delta$ a discrete derivative (Eq. (20)): the blend $\chi=\tfrac12$ of
  De Michele & Coppola's pressure-equilibrium condition on the
  internal-energy convective term
  ([pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)).

## Induced equations

**Energy split.** The pressure-work flux obeys the discrete product rule

$$(\!(p;v)\!)_{i+1/2}-(\!(p;v)\!)_{i-1/2}=\tfrac12p_i(v_{i+1}-v_{i-1})+\tfrac12v_i(p_{i+1}-p_{i-1}),$$

so the discrete total-energy equation of KEEP or KEEP-PE is the sum of the
kinetic-energy equation induced by mass and momentum, with pressure term
$v_i(p_{i+1}-p_{i-1})/(2\Delta x)$, and the internal-energy equation
(Shima et al. Eqs. (12)–(13), the product rule credited to Kuya et al.)

$$\frac{d}{dt}(\rho e)_i+\frac{(f_{\rho e})_{i+1/2}-(f_{\rho e})_{i-1/2}}{\Delta x}+p_i\frac{v_{i+1}-v_{i-1}}{2\Delta x}=0 .$$

For KEEP, whose $f_{\rho e}=f_\rho\{\!\{e\}\!\}$, this is the
Kennedy–Gruber–Pirozzoli discretization of the internal-energy equation, as
[De Michele & Coppola (2023a)](/sources/demichele-2023.md) also find for
exact time integration (§4.2.1); its convective part is of the
kinetic-energy-preserving type for $e$. De Michele & Coppola show that no
pressure-equilibrium-preserving internal-energy splitting is of that type
(§4.2.2), so KEEP-PE gives it up. The KEP enthalpy flux decomposes as the
KEEP internal-energy flux plus $\{\!\{\rho\}\!\}\{\!\{p/\rho\}\!\}\{\!\{v\}\!\}$,
whose pressure part does not split by the product rule (Shima et al.
Eq. (16)).

**Pressure.** With $\rho e=p/(\gamma-1)$, at $v\equiv v_0$, $p\equiv p_0$ and
any density, the KEEP pressure rate is

$$\frac{dp_i}{dt}=-\frac{v_0p_0}2\Big[\frac1{\rho_i}\frac{\rho_{i+1}-\rho_{i-1}}{2\Delta x}+\rho_i\frac{\rho_{i+1}^{-1}-\rho_{i-1}^{-1}}{2\Delta x}\Big]=-\frac{v_0p_0\,(\rho_{i+1}-\rho_{i-1})(\rho_{i+1}\rho_{i-1}-\rho_i^2)}{4\Delta x\,\rho_{i-1}\rho_i\rho_{i+1}}$$

(Shima et al. Eqs. (14)–(15); the factored form is a *compiler check, not
in the sources*). It is generically nonzero; its Taylor expansion is
$-\tfrac12v_0p_0\Delta x^2(\ln\rho)'(\ln\rho)''+O(\Delta x^4)$, so the error is
second order in smooth regions and vanishes where $\ln\rho$ is locally linear
on the grid *(compiler check, not in the sources)*. KEP contains the same
internal-energy part and fails as well. The KEEP-PE rate is
$-\big[(\{\!\{p\}\!\}\{\!\{v\}\!\})_{i+1/2}-(\{\!\{p\}\!\}\{\!\{v\}\!\})_{i-1/2}\big]/\Delta x-(\gamma-1)p_i(v_{i+1}-v_{i-1})/(2\Delta x)$,
which vanishes identically at $v_0$, $p_0$ (Eqs. (18)–(19)).

**Velocity.** All three schemes share the mass, momentum and pressure
fluxes, so the velocity rate induced by momentum minus $v_i$ times mass
vanishes for each at $v_0$, $p_0$ (Eqs. (21)–(23)). KEEP and KEP lose
velocity equilibrium only through their pressure error, which enters
through the pressure-gradient term and then perturbs the density through
the mass equation (§2.2.4, §3.1).

**Explicit time stepping.** At $v\equiv v_0$, $p\equiv p_0$ the KEEP-PE
momentum residual is $v_0$ times the mass residual and the energy residual
$\tfrac12v_0^2$ times it, because $\{\!\{p\}\!\}\{\!\{v\}\!\}$ and $(\!(p;v)\!)$
are constant. Every explicit Runge–Kutta stage therefore keeps
$\rho v=v_0\rho$ and $E=p_0/(\gamma-1)+\tfrac12v_0^2\rho$, hence $v_0$ and $p_0$,
as long as the density stays positive *(compiler check, not in the
sources)*.

## Other forms

- **Two-point (DG) form.** In direction $n$, with $v\cdot n$ in the means,
  $\{\!\{p\}\!\}n$ in the momentum and $\tfrac12f_\rho\,v^-\cdot v^+$ as
  kinetic part, the KEEP-PE set is the "Shima et al. flux" that
  [Ranocha et al. (2023)](/sources/ranocha-2023.md) use as a volume flux of
  [flux-differencing](/methods/flux-differencing.md) DGSEM (§3.2,
  Eq. (3.7); formula on
  [entropy-conservative two-point fluxes](/methods/entropy-conservative-flux.md)).
  They state, citing the literature, that it is kinetic-energy and
  pressure-equilibrium preserving and not entropy conservative. In the
  classification of [De Michele & Coppola (2023b)](/sources/demichele-2023-b.md)
  KEEP-PE is Aρ-Ap and KEEP is Aρ-Ae (Eqs. (3), (15)).
- **Multi-component ideal gases.** The split flux set FC/PE (S) of
  [Fujiwara, Tamaki & Kawai (2023)](/sources/fujiwara-2023.md) keeps
  pressure equilibrium for mixtures and reduces to KEEP-PE for one
  component (§3.4, Table 1;
  [multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)).
- **General equation of state.** The [APEC flux](/methods/apec-scheme.md)
  of [Terashima, Ly & Ihme (2025)](/sources/terashima-2025.md) keeps the
  KEEP mass, momentum, kinetic-energy and pressure-work fluxes and corrects
  only the internal-energy face value (§2.8, Eqs. (35)–(40)).
- **Two-phase flows.** The single-phase part of the
  [Jain & Moin (2022)](/sources/jain-2022.md) scheme is the KEEP-PE set,
  with $\{\!\{\rho e\}\!\}\{\!\{v\}\!\}$ their quadratic split *(compiler check,
  not in the sources)*. They call single-phase schemes of this kind
  "KEEP" and find the KEEP cubic split unstable at density ratio 10, where
  it violates their interface-equilibrium condition (§3.5, §4.1.2).
- **High order.** Shima et al. state that a high-order version "can be
  straightforward" following Kuya & Kawai's high-order KEEP on curvilinear
  grids; it is not built (§2.2.1).

## Evidence

- **Density wave** ([density-wave advection](/benchmarks/density-wave-advection.md)):
  $\rho_0=2+\sin2\pi x$, $v_0=p_0=1$, 41 points on $[0,1]$, RK4 at CFL ≈ 0.1.
  KEEP-PE keeps $v$ and $p$ uniform without dissipation; KEEP and KEP
  develop growing pressure, velocity and density oscillations and diverge
  at $t\approx12.9$ and $t\approx11.1$ (Shima et al. §3.1, Fig. 1). A rerun
  with these settings (41 points with both periodic ends, 40 unknowns)
  diverges at $t=12.89$ (KEEP) and $t=11.16$ (KEP), and
  KEEP-PE holds $\max\lvert p-1\rvert\approx4\times10^{-14}$ to $t=20$
  *(compiler check, not in the sources)*. On their own density wave
  ($\rho_0=1+\exp(\sin2\pi x)$, 61 points) De Michele & Coppola (2023b)
  find Aρ-Ae (KEEP) diverging at $t\approx22$ (§5, Fig. 1).
- **Inviscid Taylor–Green vortex**
  ([Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)), $M_0=0.4$,
  $65^3$ points, time $\hat t=M_0t$ (page-local): KEP loses entropy rapidly
  and blows up at $\hat t\approx120$, while KEEP and KEEP-PE run to
  $\hat t=160$ without dissipation, also at $\Delta x=2\pi/32$. KEEP-PE
  "slightly increases" the total kinetic energy and decreases the total
  entropy relative to KEEP, by about $5\times10^{-3}$ of the normalized
  entropy at $\hat t=160$ as read from Fig. 2b (Shima et al. §3.2, Fig. 2).
  De Michele & Coppola (2023b) likewise find Aρ-Ap and Aρ-Ae conserving
  entropy worse than their harmonic- and geometric-mean fluxes (Fig. 2).
- **Isentropic vortex** ([isentropic vortex](/benchmarks/isentropic-vortex.md)):
  in De Michele & Coppola (2023a)'s robustness study neither the
  KEEP-equivalent $(\rho e)$ scheme nor the KEEP-PE-equivalent
  $(\rho e)_{\mathrm{PEP}}$ scheme blows up by $t=50$ at CFL 0.01, 0.1 or 0.5
  (§5.1, Table 3).
- **Supersonic turbulent boundary layer**
  ([supersonic turbulent boundary layer](/benchmarks/supersonic-turbulent-boundary-layer.md)),
  $M_\infty=2.28$, $\mathrm{Re}_\tau\approx480$: KEEP-PE without numerical
  dissipation agrees with a sixth-order compact DNS with eighth-order
  filtering for mean velocity, Reynolds stresses and the turbulent
  kinetic-energy budget (Shima et al. Appendix, Fig. 3).

## Qualifications

- **Scope of the equilibrium.** Shima et al.'s proof is semi-discrete,
  second order, on a uniform grid, for a single-component ideal gas with
  constant $\gamma$: it needs $\rho e$ linear in $p$. With a variable
  $\gamma$ or a general equation of state the KEEP-PE flux is no longer
  exact, which is where Fujiwara et al. and Terashima et al. take over.
- **"Entropy preserving" means near conservation.** Neither KEEP nor
  KEEP-PE is shown to satisfy Tadmor's condition; KEEP's entropy is "not
  strictly preserved at the discrete level" (§2.1.1), KEEP-PE's internal-energy
  flux "may affect the entropy preservation property" (§2.2.3), and the
  trade-off between pressure equilibrium and entropy seen in the
  Taylor–Green vortex is left "in progress" (§3.2).
- **"Superior numerical stability"** (abstract, §4) rests on the density
  wave, the only test in which KEEP-PE outlives KEEP; in the Taylor–Green
  vortex the two are equally stable. Pressure-equilibrium preservation alone
  does not buy robustness: in De Michele & Coppola (2023a)'s Table 3 the
  pressure-equilibrium-preserving $(\rho e)_{\mathrm{div}}$ scheme blows up
  about as early as plain total energy, while the non-PEP KEEP-equivalent
  scheme never does (§5.1). Jain & Moin find the KEEP cubic split stable in
  the single-phase inviscid Taylor–Green vortex (§4.1.1). The density
  wave, a density variation at constant pressure, is the test the others
  lack, so the results are compatible.
- **"Existing split forms do not maintain pressure equilibrium."** Shima et
  al.'s sentence (§2.2.2) concerns the KEP and KEEP forms they analyse
  ("such as used in the KEP and KEEP schemes"). De Michele & Coppola
  (2023a) list other pressure-equilibrium-preserving split forms, the
  $(\rho E)_{\mathrm{PEP}}$ scheme of Singh & Chandrashekar and their
  $(\rho e)_{\mathrm{div}}$ (§4.2.2), so the sentence is not a general
  impossibility.

# Citations

- [Shima, Kuya, Tamaki & Kawai (2021)](/sources/shima-2021.md) — §2.1–2.2 Eqs. (1)–(23), Tables 1–2, §3, §3.1 Fig. 1, §3.2 Fig. 2, §4, Appendix Fig. 3.
- [De Michele & Coppola (2023a)](/sources/demichele-2023.md) — §4.2.1, §4.2.2, Table 2, §5.1 Table 3 (arXiv v1).
- [De Michele & Coppola (2023b)](/sources/demichele-2023-b.md) — Eqs. (3), (15), §5 Figs. 1–2 (arXiv v2).
- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — §3.2 Eq. (3.7).
- [Coppola & Veldman (2023)](/sources/coppola-2023.md) — §5.2 Observation 7.
- [Fujiwara, Tamaki & Kawai (2023)](/sources/fujiwara-2023.md) — §3.4, Table 1.
- [Terashima, Ly & Ihme (2025)](/sources/terashima-2025.md) — §2.8 Eqs. (35)–(40).
- [Jain & Moin (2022)](/sources/jain-2022.md) — §3.1, §3.5 Eqs. (58)–(62), §4.1.1–4.1.2 (arXiv v1).
