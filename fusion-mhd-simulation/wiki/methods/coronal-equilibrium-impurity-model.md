---
type: Method
title: "Coronal-equilibrium impurity model"
description: "Impurity model for MHD codes in which one advected impurity density carries all charge states, whose distribution is set instantaneously to the local ionization–recombination balance at the electron temperature; it supplies radiation, ionization energy, effective charge and electron density to the fluid equations."
status: established
aliases: [coronal equilibrium, CE impurity model, coronal impurity fluid]
tags: [impurities, disruption, mhd, code]
timestamp: 2026-10-16T00:00:00Z
---

# Coronal-equilibrium impurity model

In the coronal-equilibrium (CE) model an impurity species is represented by
a single mass density $\rho_{\mathrm{imp}}$, all of whose charge states are
convected with the main plasma; the distribution over charge states is not
evolved but assumed to be in instantaneous ionization–recombination balance
at the local electron temperature
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.7;
[Hu et al. (2021b)](/sources/hu-2021-b.md), §1). It is the impurity model
that [JOREK](/software/jorek.md) used for massive material injection and
radiative-collapse studies before the
[collisional-radiative model](/methods/collisional-radiative-impurity-model.md)
replaced it ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.2).

## Equations

**Transport.** One continuity equation is added to the fluid model
([Bhole et al. (2023)](/sources/bhole-2023.md), Eq. 5;
[Bandaru et al. (2024)](/sources/bandaru-2024.md), Eq. 2.10):
$$\partial_t\rho_{\mathrm{imp}}+\nabla\cdot(\rho_{\mathrm{imp}}\mathbf v)=\nabla\cdot\big[D_{\parallel,\mathrm{imp}}\nabla_\parallel\rho_{\mathrm{imp}}+D_{\perp,\mathrm{imp}}\nabla_\perp\rho_{\mathrm{imp}}\big]+S_{\rho,\mathrm{imp}},$$
where $S_{\rho,\mathrm{imp}}$ is the injection source (gas or pellet
ablation; see [shattered pellet injection](/definitions/shattered-pellet-injection.md)).
The same source enters the total-density equation, and the total mass
density includes the impurities, $\rho=\rho_i+\rho_{\mathrm{imp}}$
([Bandaru et al. (2024)](/sources/bandaru-2024.md), Eq. 2.1).

**Charge-state closure.** The fraction of impurity ions in charge state
$z$ is a tabulated function of the local plasma,
$n_{\mathrm{imp},z}/n_{\mathrm{imp}}=\mathcal F_z(n_e,T_e)$, taken from ADAS
in [Bhole et al. (2023)](/sources/bhole-2023.md) (Eqs. 11–12, with
$T_e=T/2$ and $n_e\simeq n$ in the single-temperature model) and from
Mosher's coronal tables in
[Bandaru et al. (2024)](/sources/bandaru-2024.md) (§II). The mean charge is
$\langle z\rangle=\sum_z z\,\mathcal F_z$ and the effective charge
$Z_{\mathrm{eff}}=\sum_z z^2\mathcal F_z/\sum_z z\,\mathcal F_z$
([Bhole et al. (2023)](/sources/bhole-2023.md), Eq. 14). Coronal balance
is the stationary limit of the charge-state rate equation written on the
[collisional-radiative page](/methods/collisional-radiative-impurity-model.md):
setting its time derivative to zero gives
$\langle\sigma v\rangle_{\mathrm{ion},z}\,n_{\mathrm{imp},z}=\langle\sigma v\rangle_{\mathrm{rec},z+1}\,n_{\mathrm{imp},z+1}$
for every adjacent pair (compiler's restatement of the definition in
[Hu et al. (2021b)](/sources/hu-2021-b.md), §1).

**Electron density and pressure.** The impurities add $\langle z\rangle$
free electrons per ion. [Bandaru et al. (2024)](/sources/bandaru-2024.md)
(§II) write the electron density in mass units as
$m_in_e=\rho+\beta_{\mathrm{imp}}\rho_{\mathrm{imp}}$ with
$\beta_{\mathrm{imp}}=\frac{m_i}{m_{\mathrm{imp}}}\langle z\rangle-1$;
[Bhole et al. (2023)](/sources/bhole-2023.md) (Eq. 12) write the total
pressure as $p=(\rho+\alpha_{\mathrm{imp}}\rho_{\mathrm{imp}})T/m_i$ with
$\alpha_{\mathrm{imp}}=\frac{m_i}{m_{\mathrm{imp}}}\frac{\langle z\rangle+1}{Z+1}-1$
(normalized units; $m_i$ shown here for clarity). For $Z=1$ and $T_e=T_i=T/2$
both are the same particle count: electrons plus ions of the main species
and of the impurity (compiler's check).

**Energy.** The pressure equation loses the radiated power
$P_{\mathrm{rad}}=n_en_{\mathrm{imp}}L_{\mathrm{rad}}(T_e)$, where
$L_{\mathrm{rad}}$ is the coronal radiation function
([Bhole et al. (2023)](/sources/bhole-2023.md), source $S_p$, p. 8;
[Bandaru et al. (2024)](/sources/bandaru-2024.md), Eq. 2.8). Because the
charge distribution jumps instantaneously with $T_e$, a cooling plasma
would recombine instantly and release spurious recombination radiation.
Both JOREK papers avoid this by treating the ionization energy as a
potential energy that is advected with the impurities
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.7;
[Bhole et al. (2023)](/sources/bhole-2023.md), Eq. 13):
$$\partial_t p+\dots=-(\Gamma-1)\Big[\partial_t\big(n_{\mathrm{imp}}\bar\varepsilon_{\mathrm{ion}}\big)+\nabla\cdot\big(n_{\mathrm{imp}}\bar\varepsilon_{\mathrm{ion}}\mathbf v\big)\Big]+\dots,\qquad
\bar\varepsilon_{\mathrm{ion}}=\sum_z\mathcal F_z\sum_{k=0}^{z-1}\varepsilon_{\mathrm{ion},k},$$
where $\varepsilon_{\mathrm{ion},k}$ is the energy needed to ionize state
$k$ to $k+1$. Bhole et al. absorb this term into an extended pressure
$p+(\Gamma-1)\rho_{\mathrm{imp}}\bar\varepsilon_{\mathrm{ion}}/m_{\mathrm{imp}}$
in their conservative variable vector (Eq. 15).

**Resistivity.** The radiation-cooled plasma becomes resistive through a
Spitzer resistivity with the Hirshman $Z_{\mathrm{eff}}$ correction
([Bandaru et al. (2024)](/sources/bandaru-2024.md), §III.A;
[Hu et al. (2021b)](/sources/hu-2021-b.md), Eq. 7):
$$\eta=\eta_{\mathrm{Sp}}(T_e)\,Z_{\mathrm{eff}}\,\frac{1+1.198Z_{\mathrm{eff}}+0.222Z_{\mathrm{eff}}^2}{1+2.966Z_{\mathrm{eff}}+0.753Z_{\mathrm{eff}}^2},\qquad \eta_{\mathrm{Sp}}\propto T_e^{-3/2}.$$
The JOREK–DINA runaway-electron benchmark uses the simpler
$\eta=\eta_{\mathrm{Sp}}Z_{\mathrm{eff}}$
([Bandaru et al. (2024)](/sources/bandaru-2024.md), §IV.A).

## Implementations in the sources

- **JOREK reduced MHD**: one extra variable, all charge states convected
  with the main plasma, used for MMI and radiative-collapse runs
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.7). A simpler
  option prescribes a constant background radiation rate.
- **JOREK full MHD**: the model is extended to the
  [visco-resistive full MHD model](/methods/visco-resistive-mhd-model.md),
  single fluid and single temperature, for neon and argon SPI in a JET-like
  plasma, together with VMS and
  [shock-capturing stabilization](/methods/shock-capturing-artificial-viscosity.md)
  ([Bhole et al. (2023)](/sources/bhole-2023.md), §2, §4). A two-temperature
  variant puts the ionization term in the electron pressure equation
  (Eqs. 6–7) but is not used in that paper's tests.
- **JOREK runaway-electron extension**: CE impurities with a single
  $\rho_{\mathrm{imp}}$ provide the free and bound electron densities that
  enter the partially screened avalanche source of the
  [runaway-electron fluid model](/methods/runaway-electron-fluid-model.md)
  ([Bandaru et al. (2024)](/sources/bandaru-2024.md), §II). In the DINA
  benchmark, DINA tracks charge states and a "DINA-C" run mimics coronal
  equilibrium ([ITER runaway-electron benchmarks](/benchmarks/iter-runaway-electron-benchmarks.md)).

## Accuracy and limits

- Massive injection deposits impurities on time scales comparable to the
  ionization equilibration time, so CE is inaccurate early in the
  injection; it "tends to underestimate the line radiation contribution
  from the weakly ionized states"
  ([Hu et al. (2021b)](/sources/hu-2021-b.md), §1).
- Within JOREK, on the DIII-D argon case with Spitzer-like resistivity and
  one temperature, the CE run starts with *larger* ionization cooling (the
  distribution jumps to equilibrium), but its combined cooling rises more
  slowly; the non-equilibrium run reaches the balance of cooling and Ohmic
  heating at $t\approx0.7$ ms, the CE run "only does so very late"; peak
  cooling powers are comparable ([Hu et al. (2021b)](/sources/hu-2021-b.md),
  §4, Fig. 2). With two temperatures the CE run is "better behaved" and
  reaches balance only slightly later (Fig. 3).
- Imposing the CE distribution on the particle representation ("CE
  particle") reproduces the CE fluid run apart from a late delay, which
  validates the particle representation against the fluid one rather than
  the CE assumption itself ([Hu et al. (2021b)](/sources/hu-2021-b.md), §4,
  Fig. 6).
- Hoelzl et al. (2021, §2.7) state that the assumption "may lead, at least
  in certain cases, to an underestimation of energy dissipation by
  impurities".
- The impurity-pellet deposition source converges with the toroidal source
  width only for deuterium, not necessarily for impurities, whose radiated
  power scales inversely with that width
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.8).

## Contradictions

**CE thermal-collapse delay: size and attribution** — Open.
[Hoelzl et al. (2021)](/sources/hoelzl-2021.md) (§2.7) report that in the
axisymmetric impurity benchmark of Lyons et al. (2019) JOREK "with its
coronal equilibrium model predicts a roughly two times slower thermal
collapse than M3D-C1 and NIMROD", and attribute the gap to the CE
assumption, since those codes track every charge state.
[Hu et al. (2021b)](/sources/hu-2021-b.md) (§4, Fig. 2; §6; App. A) confirm
the direction inside JOREK (CE delays the cooling–Ohmic balance) but give no
factor. With non-equilibrium charge states, JOREK and NIMROD then agree to
within a 0.15 ms delay of the argon cooling peak, and Hu et al. attribute the
residual differences to the atomic data (open-ADAS versus KPRAD-fitted ADPAK),
not to the charge-state model. An argon rerun with a different ADAS
line-radiation data set (labelled "1942" in the paper, against the 1989 set
of the main runs) gives "much better" agreement with NIMROD. The two papers do not contradict each other on
the sign of the effect. They leave open how much of the factor 2 is due to
the CE assumption and how much to the atomic-data set used by the CE run.
That set is not stated in Hoelzl et al. (2021). A CE run and a
non-equilibrium run with identical atomic data, compared with M3D-C1 and
NIMROD on the same case, would settle it. See the
[DIII-D gas-injection benchmark](/benchmarks/diii-d-mgi-impurity-benchmark.md).

# Citations

- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — §2.7, §2.8, §2.15.
- [Bhole et al. (2023)](/sources/bhole-2023.md) — §2, Eqs. 5, 11–15; §4.
- [Bandaru et al. (2024)](/sources/bandaru-2024.md) — §II, Eqs. 2.1, 2.7–2.10; §III.A; §IV.A.
- [Hu et al. (2021b)](/sources/hu-2021-b.md) — §1, §4, Figs. 2–3, 6; Eq. 7.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) — §3.2.
