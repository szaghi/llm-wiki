---
type: Property
title: "Pressure-equilibrium preservation"
description: "A discretization is pressure-equilibrium preserving when initial data with constant velocity and pressure keep them constant; the page gives De Michele and Coppola's two discrete conditions for split-form central schemes, the energy-equation splittings that meet them, the incompatibility with a KEP internal-energy splitting, the Shima and Ranocha fluxes, and the two-phase interface-equilibrium condition."
status: established
aliases: [PEP, pressure equilibrium preserving, KEEP-PE, interface equilibrium, preservation of constant velocity and pressure]
tags: [kinetic-energy-preserving, finite-difference, central-scheme, multiphase, turbulence]
timestamp: 2026-10-23T16:00:00Z
---

# Pressure-equilibrium preservation

For the Euler equations, data with uniform velocity $v$ and pressure $p$
and arbitrary density (a contact or entropy wave) is advected unchanged:
$v$ and $p$ stay constant for all time. A semi-discretization is
**pressure-equilibrium preserving** (PEP) when it keeps a constant $v$ and
$p$ constant whenever they are constant initially
([De Michele & Coppola (2023)](/sources/demichele-2023.md), §4.2.2). The
property is stated for shock-free central discretizations, where nothing
damps a spurious pressure perturbation created at a density jump.

## Setting

De Michele & Coppola work with collocated central finite differences on a
uniform periodic mesh, derivative $\delta/\delta x$, and write each balance
law $\partial_t(\rho\phi)=-C_{\rho\phi}-P_{\rho\phi}$ with a convective part
$C$ and a pressure part $P$ (page-local); $\mathcal M=C_\rho$ is the
convective term of the mass equation (§2.2, §3.1). Mass and momentum use
the kinetic-energy-preserving family $\mathcal M=\zeta\mathcal M^D+(1-\zeta)\mathcal M^A$,
$C_{\rho v}=\zeta C^F+(1-\zeta)C^C$ of
[split convective forms](/methods/split-convective-forms.md) (their $\xi$ is
the page's $\zeta$; $\zeta=1$ Feiereisen, $\tfrac12$ Kennedy–Gruber–Pirozzoli,
$0$ Coppola et al.). In second-order flux form this is $\mathcal M=[\![m]\!]$,
$C_{\rho v}=[\![\overline v\,m]\!]$, with $\overline a=\tfrac12(a_i+a_{i+1})$,
$[\![g]\!]=(g_{i+1/2}-g_{i-1/2})/\Delta x$ here a flux difference (page-local,
not the registry's interface jump) and face mass flux
$m_{i+1/2}=\zeta\,\overline{\rho v}+(1-\zeta)\tfrac12(\rho_iv_{i+1}+\rho_{i+1}v_i)$
(Eqs. (23)–(25)). All results assume exact time integration.

## The two conditions

The discrete velocity equation induced by mass and momentum is
$\partial_tv=\tfrac v\rho\mathcal M-\tfrac1\rho C_{\rho v}-\tfrac1\rho P_{\rho v}$
(Eq. (46)). With $p$ constant the pressure gradient vanishes, so:

1. **Velocity** (necessary, Eq. (47)): $v\,\mathcal M=C_{\rho v}$ for
   constant $v$. Every kinetic-energy-preserving scheme satisfies it,
   since $C_{\rho v}=[\![\overline v\,m]\!]=v[\![m]\!]$ for constant $v$.
   De Michele & Coppola note that Ranocha derived a similar condition for
   finite volumes.
2. **Pressure** (Eq. (48)): $C_p+P_p=0$ for constant $v$ and $p$, with
   $C_p$, $P_p$ the convective and pressure parts of the discrete pressure
   equation, direct or induced.

How the second condition is met depends on which "energy" equation is
discretized:

- **Pressure equation.** A direct discretization
  $C_p=\chi\,\frac{\delta pv}{\delta x}+(1-\chi)\big(p\frac{\delta v}{\delta x}+v\frac{\delta p}{\delta x}\big)$,
  $P_p=(\gamma-1)p\frac{\delta v}{\delta x}$, with any blending $\chi$
  (page-local), satisfies it (Eqs. (49)–(50)).
- **Internal energy.** Since $p=(\gamma-1)\rho e$, it holds when the
  convective term averages only the divergence and the $v$-advective forms,
  $C_{\rho e}=\chi\,\frac{\delta\rho ve}{\delta x}+(1-\chi)\big(v\frac{\delta\rho e}{\delta x}+\rho e\frac{\delta v}{\delta x}\big)$
  (Eq. (51)). Shima et al. use $\chi=\tfrac12$; $\chi=1$ is the new
  $(\rho e)_{\mathrm{div}}$ form.
- **Total energy.** The condition becomes
  $C_{\rho E}-C_{\rho\kappa}+P_{\rho E}=0$ for constant $v,p$ (Eq. (54)). The
  kinetic part of $C_{\rho E}$ in any of the split forms reduces to the
  induced $C_{\rho\kappa}$ for constant $v$, so what remains is that the
  discretization of $\frac{\gamma}{\gamma-1}\partial_x(pv)$ vanish for
  constant $v$ and $p$. Singh & Chandrashekar obtain this with the
  Kennedy–Gruber–Pirozzoli split for the kinetic part and an average of the
  divergence and advective forms for the pressure part, the $(\rho E)_{\mathrm{PEP}}$
  scheme (§4.2.2).

**PEP and KEP of the energy variable are incompatible.** A
kinetic-energy-preserving treatment of the internal-energy equation, with
flux $\overline e\,m$, makes $\rho e^2$ a conserved quadratic. A splitting
that satisfies Eq. (51) cannot be of that type, so a PEP internal-energy
discretization cannot preserve $\rho e^2$ (§4.2.2). The KEEP scheme of Kuya
et al., equivalent for exact time integration to the KGP internal-energy
scheme, is therefore not PEP (Table 2).

## Which schemes have it

De Michele & Coppola tabulate fifteen second-order schemes, all with KEP
mass and momentum (Table 2). Only three are PEP:

| scheme | convective flux of the energy variable | pressure term | from |
|---|---|---|---|
| $(\rho E)_{\mathrm{PEP}}$ | $\overline{\rho e}\,\overline v+m\,\overline\kappa_{\mathrm s}$ | $[\![\overline v\,\overline p]\!]$ | Singh & Chandrashekar |
| $(\rho e)_{\mathrm{PEP}}$ | $\overline{\rho e}\,\overline v$ | $p\,\delta v/\delta x$ | Shima et al. |
| $(\rho e)_{\mathrm{div}}$ | $\overline{\rho ve}$ | $p\,\delta v/\delta x$ | new |

Here $\kappa_{\mathrm s}=\tfrac12\lvert v\rvert^2$ is the specific kinetic
energy (page-local). The plain total-energy scheme, the Jameson–Pirozzoli
form, the KEP internal-energy scheme, the sound-speed schemes (Kok's and
two new ones), the three total-enthalpy schemes and the three entropy
schemes are not PEP.

In DG, [Ranocha et al. (2023)](/sources/ranocha-2023.md) state, citing the
literature, that the directional Shima et al. flux is kinetic-energy and
pressure-equilibrium preserving but not entropy-conservative, and that the
Ranocha flux is entropy-conservative, kinetic-energy preserving and
pressure-equilibrium preserving (§3.2, Eqs. (3.7), (3.10); formulas on
[entropy-conservative and kinetic-energy-preserving two-point fluxes](/methods/entropy-conservative-flux.md)).
The internal-energy part of the Shima et al. energy flux,
$\{\!\{p\}\!\}\{\!\{v\cdot n\}\!\}/(\gamma-1)$, is for an ideal gas the
$(\rho e)_{\mathrm{PEP}}$ flux $\overline{\rho e}\,\overline v$ of the table
*(compiler check, not in the sources: $\rho e=p/(\gamma-1)$)*.

## Evidence

De Michele & Coppola, 2D [isentropic vortex](/benchmarks/isentropic-vortex.md),
$30\times30$ mesh, fourth-order central derivatives, RK4, to $t=50$ (§5.1,
Table 3), blow-up times at CFL 0.01 / 0.1 / 0.5 ("–": none by $t=50$):

| scheme | blow-up |
|---|---|
| $(\rho E)$ | 26 / 28 / 33 |
| $(\rho E)_{\mathrm{PEP}}$ | 46 / 44 / – |
| $(\rho e)$ (KEP, KEEP-equivalent) | – / – / – |
| $(\rho e)_{\mathrm{PEP}}$ | – / – / – |
| $(\rho e)_{\mathrm{div}}$ | 26 / 26 / 34 |

On the $40\times40$, eighth-order run at CFL 0.01 the blow-up times are
about 19 for $(\rho E)$ and 33 for $(\rho E)_{\mathrm{PEP}}$ (§5.1). In both
runs $(\rho E)_{\mathrm{PEP}}$ outlives $(\rho E)$; in Table 3
$(\rho e)_{\mathrm{div}}$, which is PEP, blows up about as early as plain
$(\rho E)$, and the non-PEP KEP internal-energy scheme $(\rho e)$ never does.
In the inviscid
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at $32^3$ the
temperature and density fluctuations level off for $(\rho e)$,
$(\rho e)_{\mathrm{PEP}}$, the KGP sound-speed scheme and the Feiereisen and
KGP entropy schemes, but not for the Coppola-split entropy scheme, and grow
for every total-energy and total-enthalpy form (§5.2, Fig. 10). Neither
test has a density jump at constant pressure, so the property itself is
not isolated by them *(compiler check, not in the sources)*.

## Material interfaces

For compressible two-phase flows the same requirement, uniform velocity
and pressure staying uniform across an interface, is the *interface
equilibrium* condition of [Jain & Moin (2022)](/sources/jain-2022.md)
(Lemma 3.1): of their internal-energy fluxes only the quadratic split
$\{\!\{\rho e\}\!\}\{\!\{v\}\!\}$ satisfies it, the $(\rho e)_{\mathrm{PEP}}$ form
above, and the two that violate it diverge at density ratio 10 (§4.1.2;
[kinetic energy preservation](/properties/kinetic-energy-preservation.md)).
Related exact-at-rest properties of conservative multicomponent schemes,
which lose equilibrium for moving interfaces, are on
[stationary contact preservation](/properties/stationary-contact-preservation.md)
and [multicomponent Euler equations](/definitions/multicomponent-euler-equations.md).

## Qualifications

- De Michele & Coppola's conditions are for exact time integration and
  periodic uniform meshes; their tests use RK4 and attribute the CFL
  dependence of the blow-up times to RK4 dissipation, an explanation
  stated, not shown (§5.1).
- For exact time integration, which energy equation is discretized
  directly does not matter, only the discrete $C$ and $P$ terms do (§4.2.1),
  and the conditions above are written on those terms.
- The arXiv v1 read prints, in §3.1, "the cases $\xi=0$ and $\xi=1$ give the
  classical Feiereisen form and the newly derived form"; their Eqs.
  (15)–(16), §4.2.5 and Table 2 give $\xi=1$ Feiereisen and $\xi=0$ the
  Coppola et al. form, the convention used here.

# Citations

- [De Michele & Coppola (2023)](/sources/demichele-2023.md) — §2.2, §3.1 Eqs. (12)–(16), §3.3 Eqs. (23)–(25), §4.2.1, §4.2.2 Eqs. (45)–(54), Table 2, §5.1 Table 3, §5.2 Fig. 10 (arXiv v1).
- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — §3.2 Eqs. (3.7), (3.10).
- [Jain & Moin (2022)](/sources/jain-2022.md) — §3.3 Lemma 3.1, §4.1.2 (arXiv v1).
