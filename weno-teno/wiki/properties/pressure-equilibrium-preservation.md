---
type: Property
title: "Pressure-equilibrium preservation"
description: "A discretization is pressure-equilibrium preserving when initial data with constant velocity and pressure keep them constant; the page gives the discrete conditions for split-form central schemes and two-point fluxes, the schemes and algebraic fluxes that meet them, the incompatibility with a KEP internal-energy splitting, and the multicomponent and multiphase interface-equilibrium constructions."
status: established
aliases: [PEP, pressure equilibrium preserving, KEEP-PE, interface equilibrium, preservation of constant velocity and pressure, compatibility condition, FC/PE scheme]
tags: [kinetic-energy-preserving, finite-difference, central-scheme, multiphase, turbulence]
timestamp: 2026-10-23T23:00:00Z
---

# Pressure-equilibrium preservation

For the Euler equations, data with uniform velocity $v$ and pressure $p$
and arbitrary density (a contact or entropy wave) is advected unchanged:
$v$ and $p$ stay constant for all time. A semi-discretization is
**pressure-equilibrium preserving** (PEP) when it keeps a constant $v$ and
$p$ constant whenever they are constant initially
([De Michele & Coppola (2023a)](/sources/demichele-2023.md), §4.2.2). The
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

## Two-point fluxes: conditions and the AEC family

[De Michele & Coppola (2023b)](/sources/demichele-2023-b.md) state the
two-point form of the conditions, after Ranocha: for $v\equiv v_0$ and
$p\equiv p_0$ constant, the momentum flux must be $f_\rho v_0$ plus a
constant depending only on $v_0,p_0$, and the convective internal-energy
flux $f_{\rho e}$ must be a constant depending only on
$v_0,p_0$ (§4; arXiv v2; page-local $f_\rho$ the mass flux,
$f_{\rho e}$ the convective internal-energy flux,
$N_{\mathrm T}$ the truncation order). Their table of KEP fluxes
(arithmetic, geometric and harmonic means; details on
[entropy-conservative fluxes](/methods/entropy-conservative-flux.md)):

- PEP: the Ranocha flux; Gρ-Ge, $f_{\rho e}=\sqrt{\rho_i\rho_{i+1}}\,\overline v\,\sqrt{e_ie_{i+1}}$,
  since $\sqrt{\rho_ie_i\rho_{i+1}e_{i+1}}=p_0/(\gamma-1)$ *(compiler check, not in the sources)*; Aρ-He,
  $f_{\rho e}=\overline\rho\,\overline v\,e_ie_{i+1}/\overline e$; Aρ-Ap, the
  Shima et al. flux $\overline v\,\overline p/(\gamma-1)$ ("exemplary PEP
  scheme"); and every member of their asymptotically entropy-conservative
  hierarchy AEC($N_{\mathrm T}$), for any truncation order $N_{\mathrm T}$, provided the same $N_{\mathrm T}$
  is used in the density and internal-energy expansions (Eq. (14));
- not PEP: Aρ-Ae, $f_{\rho e}=\overline\rho\,\overline v\,\overline e$, which is
  the KEEP scheme of Kuya et al. and the $(\rho e)$ scheme of the table
  above; Aρ-Ge; and the KEEP($N_{\mathrm T}$) expansion of Tamaki et al. at finite $N_{\mathrm T}$
  (§3–§5).

The PEP proof is two lines: at constant $p_0$, $\rho e$ is constant, so the
harmonic mean of $e$ equals $p_0/\big((\gamma-1)\overline\rho\big)$ and the
relative jumps of $e$ and $\rho$ are opposite, which cancels the two
truncated series (Eq. (14)).

Their [density-wave test](/benchmarks/density-wave-advection.md) isolates the property: $\rho_0=1+\exp(\sin2\pi x)$,
$v=p=1$, 61 points, RK4, CFL 0.01 (§5). Aρ-Ae diverges at $t\approx22$,
Aρ-He and Gρ-Ge run to $t=100$, and KEEP(1) shows spurious pressure and
velocity oscillations at $t=30$ (Fig. 1b plots $p-p_0$ on a $10^{-7}$ scale)
where AEC(1) shows none (Fig. 1).
This complements the isentropic-vortex evidence below, in which the non-PEP
$(\rho e)$ scheme never blows up: the vortex has no density variation at
constant pressure, the density wave has nothing else *(compiler check, not
in the sources)*.

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

**Multi-component ideal gases, fully conservative.**
[Fujiwara, Tamaki & Kawai (2023)](/sources/fujiwara-2023.md) treat the
inviscid $N_{\mathrm s}$-species Euler equations in $(\rho Y_k,\rho v,E)$
form (page-local species count $N_{\mathrm s}$, mass fraction $Y_k$,
registry §10), where the ratio of specific heats varies with composition
and conservative schemes produce spurious pressure oscillations even at
smooth interfaces (§1). For an arbitrary equation of state
$\rho e=\rho e(p,\rho Y_k)$ and initial $p_0$, $v_0$ constant, velocity
equilibrium follows from the species equations, and pressure equilibrium
requires (§2.3, Eqs. (5)–(12))

$$\partial_x(\rho e)=\sum_k\Big(\frac{\partial\rho e}{\partial\rho Y_k}\Big)_{p,\rho Y_{j\ne k}}\partial_x(\rho Y_k);$$

for ideal gases, with $\mathsf G=1/(\gamma-1)$ of the mixture
(page-local), this is the advection $\partial_t\mathsf G+v_0\partial_x\mathsf G=0$
of Abgrall's condition (Eq. (15)). In a half-point flux form the discrete
analogue is their **compatibility condition** (Eq. (21)): the difference
of the half-point values of $\rho e$ across node $i$ must equal the
Jacobians $(\partial\rho e/\partial\rho Y_k)$ at $i$ times the differences of
the half-point values of $\rho Y_k$. Imposing a single interface value
(local conservation) and solving the condition for ideal gases gives the
half-point values

$$(\rho Y_k)_{i+1/2}=\tfrac12\big(\mathsf w^-(\rho Y_k)_i+\mathsf w^+(\rho Y_k)_{i+1}\big),\qquad \mathsf G_{i+1/2}=\tfrac12(\mathsf G_i+\mathsf G_{i+1}),$$

with page-local $\mathsf w^+=\frac{\bar W_{i+1}\rho_i}{\rho_{i+1}\bar W_i}=1/\mathsf w^-$ (the
source's $\phi^\pm$ and node index $m$) built from the mixture molar mass
$\bar W$ and the density; $\mathsf w^\pm\to1$ where the composition is
uniform (Eqs. (34)–(49)). Two second-order central
schemes follow (Table 1): **FC/PE (S)**, a split form that reduces to the
KEEP-PE scheme of Shima et al. for one component, and **FC/PE (D)**, a
divergence form that reduces to the standard divergence scheme. Both
solve only the conservation laws, with no extra transport equation, and
preserve equilibrium at the initial state. With a non-uniform velocity
the condition extends to Eq. (55), which only the split form satisfies;
FC/PE (D) therefore keeps equilibrium only for exactly constant velocity,
and round-off disturbances make it diverge (§5, Eqs. (55)–(59);
[split convective forms](/methods/split-convective-forms.md)).

- **Evidence.** On smooth tanh-profiled interfaces advected at constant
  ([material-interface advection](/benchmarks/material-interface-advection.md))
  $v$, $p$ (1D two species, 501 points; 2D three species, $501^2$; 2D with
  a tangential velocity jump; RK4 at convective CFL 0.05), FC/PE (S) keeps
  velocity and pressure equilibrium to about $10^{-13}$ (1D) and $10^{-12}$
  (2D) and conserves mass and energy exactly. FC/PE (D) diverges at
  $t\approx3.8$ and the non-equilibrium divergence scheme at $t\approx6.5$
  (1D) and $5.5$ (2D); Karni's pressure-equation scheme loses energy
  conservation and Abgrall's $\mathsf G$-transport scheme loses species-mass
  conservation (§4, Figs. 2–8).
- **Claims and scope.** The authors state that no previous scheme keeps
  pressure equilibrium while solving only the species-mass, momentum and
  total-energy equations; double-flux methods keep it but overspecify the
  system, with two discrete pressures (§1, §6). The scheme is
  non-dissipative and offered as a baseline: shocks and sharp interfaces
  need added numerical diffusion, left to future work. A stiffened-gas
  extension (arithmetic mean of the extra energy term) is derived but not
  tested (App. B).

The Jain & Moin scheme above solves a diffuse-interface model with a
volume-fraction equation, so it is not a scheme of the
$(\rho Y_k,\rho v,E)$ kind to which Fujiwara et al.'s "first" claim
refers *(compiler check, not in the sources)*.

**Volume-fraction models: consistency requirements.**
[Huang & Johnsen (2023)](/sources/huang-2023.md) add a
[Phase-Field](/methods/phase-field-method.md) flux to
a five-equation-type model to hold interfaces at a fixed thickness
([five-equation model](/definitions/five-equation-model.md)). They prove
that isolated interfaces at interfacial equilibrium in uniform flow are
advected with no phase-density, velocity, pressure or temperature error
(Thm. 2.4) and carry this to the discrete level through two consistency
requirements (§3):

- **Consistent reconstruction of mass and volume fraction** (Def. 1): the
  reconstructed partial density must equal the constant phase density
  times the reconstructed volume fraction. It holds if both are
  reconstructed by the same scheme and that scheme commutes with affine
  maps $g=af+b$, as MUSCL with most TVD limiters does; characteristic
  reconstruction does not, so after a characteristic reconstruction the
  partial densities and volume fraction are reconstructed again from
  primitive variables (§3.1).
- **Consistent Phase-Field fluxes** (Def. 2): the Phase-Field mass flux of
  a phase must equal its constant density times the volume-fraction flux;
  their reduction-consistent flux meets it without computing the phase
  densities (§3.2.1).

With them the Phase-Field step preserves $v$ and $p$ for any explicit
integrator (Thm. 3.1), and temperature equilibrium needs only Def. 1,
which they call weaker than the conditions of Beig & Johnsen (Thm. 5.2,
Remark 5.2.1, Thm. 5.4). A water disk in air advected at density ratio
about 1000 keeps conservation, $v$ and $p$ errors at round-off (§4.3,
Fig. 7). Violating Def. 1 (partial densities by WENO5, volume fraction by
MUSCL) or Def. 2 produces mass spikes near the interface, up to 40 % for
Def. 2, while conservation, boundedness and equilibrium are kept (§5.1,
Figs. 10–12).

**Non-equilibrium (Baer–Nunziato) model.**
[Paula, Adami & Adams (2023)](/sources/paula-2023.md) solve the full
non-equilibrium multiphase model with a
[discrete-equations method](/methods/discrete-equations-method.md), in which
the non-conservative interface terms come from Lagrangian fluxes across the
contact waves of pairwise Riemann problems (§2–4). Under uniform $p$, $v$,
with the criterion of Abgrall, the maximum relative velocity and pressure
errors are $9.4\times10^{-15}$ and $4.7\times10^{-15}$ in 1D (two ideal
gases, 160 cells), $1.1\times10^{-14}$ and $2.3\times10^{-15}$ in 2D with
two materials and $1.2\times10^{-14}$ and $8.4\times10^{-15}$ in 2D with five
materials ($80\times80$) (§7.1, Table 1). A weak shock through a water–air
interface keeps the phasic $p$ and $v$ in equilibrium without relaxation,
because the two-phase Riemann problem enforces mechanical equilibrium, with
small deviations only at the most diffused interface (§7.4.1).

The three multiphase constructions differ in what they solve: Fujiwara et
al. only the species conservation laws, Huang & Johnsen a non-conservative
volume-fraction equation, Paula et al. phasic equations with
non-conservative interface terms. No source compares them on a common
test.

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

- [De Michele & Coppola (2023a)](/sources/demichele-2023.md) — §2.2, §3.1 Eqs. (12)–(16), §3.3 Eqs. (23)–(25), §4.2.1, §4.2.2 Eqs. (45)–(54), Table 2, §5.1 Table 3, §5.2 Fig. 10 (arXiv v1).
- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — §3.2 Eqs. (3.7), (3.10).
- [Jain & Moin (2022)](/sources/jain-2022.md) — §3.3 Lemma 3.1, §4.1.2 (arXiv v1).
- [De Michele & Coppola (2023b)](/sources/demichele-2023-b.md) — §3–§5, Eqs. (3)–(15), Fig. 1 (arXiv v2).
- [Fujiwara, Tamaki & Kawai (2023)](/sources/fujiwara-2023.md) — §1, §2.3 Eqs. (5)–(16), §3 Eqs. (17)–(49), Table 1, §4 Figs. 2–8, §5 Eqs. (55)–(59), §6, App. B.
- [Huang & Johnsen (2023)](/sources/huang-2023.md) — §2.7 Thm. 2.4, §3.1 Def. 1, §3.2 Def. 2, Thm. 3.1, §4.3 Fig. 7, §5.1 Figs. 10–12, §5.2 Thms. 5.2, 5.4.
- [Paula, Adami & Adams (2023)](/sources/paula-2023.md) — §7.1 Table 1, §7.4.1.
