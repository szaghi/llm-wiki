---
type: Result
title: "Electron temperature hole and the stochastic barrier at q = 1 after SPI"
description: "In JOREK simulations of neon-deuterium SPI into ITER L-mode, transient electron temperature holes form along field lines through the fragment plume because Braginskii parallel conduction collapses in the cold radiating cloud, raising local resistivity and the MHD response; and a transport barrier of the stochastic field just outside q = 1 confines the core during the early thermal quench until edge modes grow."
status: established
aliases: [temperature hole, Te hole, cold spot along field lines, stochastic transport barrier, q=1 barrier, KAM barrier]
tags: [disruption, impurities, mhd, kink, tokamak]
timestamp: 2026-10-16T20:00:00Z
---

# Electron temperature hole and the stochastic barrier at q = 1 after SPI

**Statement.** Two features of the early mitigated
[thermal quench](/definitions/thermal-quench.md) appear in 3D JOREK
reduced-MHD simulations of neon–deuterium
[shattered pellet injection](/definitions/shattered-pellet-injection.md)
into an ITER 15 MA L-mode with two temperatures and a
[collisional-radiative impurity model](/methods/collisional-radiative-impurity-model.md)
([Hu et al. (2023)](/sources/hu-2023.md)):

1. **Electron temperature holes:** transient, localized $T_e$ minima along
   the field lines that cross the fragment plume, which survive parallel
   conduction because the conductivity collapses where the plasma is cold
   (§3.2, Figs. 11–12).
2. **A stochastic transport barrier just outside $q=1$:** after the 1/1
   kink has relaxed the core, field lines inside $q=1$ stay confined for
   2000 toroidal turns although they are stochastic, until edge modes grow
   (§3.3, Figs. 13–15).

The equilibrium has a large $q<1$ region ($q=1$ at normalized flux 0.3)
and the fragments reach $q=1$ before the edge radiative collapse (§2.2,
§3.2); both features belong to that ordering.

## 1. Electron temperature holes

**Mechanism.** Strong local radiation in the dense, cold plume removes
electron energy faster than parallel conduction can refill it, because the
Braginskii conductivity $\kappa_\parallel\propto T_e^{5/2}$ collapses in the
cold region. The hole is a dark spot in $\log_{10}T_e$ at the plume
($R\simeq7.75$ m, $Z\simeq0.65$ m at 1.26 ms in the 500 m/s case), with
$T_e$ falling from ≈1 keV to very low values along the traced field line
and $n_e$ reaching ∼$10^{21}$ m$^{-3}$; it disappears once the fragments
have passed ([Hu et al. (2023)](/sources/hu-2023.md), §3.2, Figs. 11–12).

**Control experiment.** With $\kappa_\parallel$ held at its Braginskii value
for 500 eV, the hole does not form (§3.2, Fig. 11b), the MHD response is
weaker, good flux surfaces survive outside $q=1$ at 2.39 ms, and the rise of
radiated power is delayed (§4.4, Figs. 21–22).

**Validity of collisional conduction.** The line density needed for a
collisional electron to cross the hole, about $2\times10^{21}$ m$^{-2}$,
is comparable with $\int n_e\,dl\simeq2.4\times10^{21}$ m$^{-2}$ across the
hole's half-width, so transport into the hole is "barely collisional"
(§3.2, Eq. 20, an order-of-magnitude estimate). The Braginskii closure is
therefore at the edge of its validity there.

**Consequences.**

- The hole raises the resistivity along its field lines, enhances current
  expulsion from them and so the helical current perturbation and the MHD
  amplitude; the Braginskii runs have stronger MHD than the
  constant-$\kappa_\parallel$ runs (§3.2, §4.4, Fig. 21).
- The hole lowers the $T_e$ that a "local" ablation law sees and cuts
  ablation; this motivates evaluating ablation on flux-surface-averaged
  $T_e$, $n_e$ ([pellet ablation models](/methods/pellet-ablation-models.md);
  §3.2, §4.1).

## 2. The stochastic barrier at q = 1

**Sequence.** Vanguard fragments crossing $q=1$ destabilize the 1/1
resistive kink; flux displacement and a "cold bubble" relax $T_e$ inside
$q=1$ (§3.1, Figs. 3–4; see
[resistive internal kink](/definitions/resistive-internal-kink.md)). The
field inside $q=1$ becomes stochastic, but field lines traced from there do
not reach the edge in 2000 toroidal turns (Fig. 13a,d). The authors
attribute the barrier to the stiff 1/1 eigenfunction, which vanishes
outside $q=1$, together with weak 2/1 and 3/1 edge modes, so that "some
good KAM surfaces … might survive" (§3.3; the KAM reading is an
interpretation, the confinement is shown).

**Breakdown.** In the 200 m/s case the barrier breaks at $t\approx6$ ms,
when edge $n=1,2$ modes grow in a second MHD peak; mixing then reaches the
whole volume and the connection length to the wall is ∼$10^4$ m (Figs. 13c,f,
14–15). By then 2/3 of the initial thermal energy has been radiated (§5;
§3.1 gives an ≈80% radiated fraction of the 25 MJ lost, a different ratio,
as the source note records). The 500 m/s case is expected to behave the
same way but "may take on the order of 10ms" (§3.3, stated).

**Diagnostics.** Poincaré plots and connection lengths from tracing over
2000 turns; 300 tracers per launch point followed for 500 turns, with the
mean and variance of $\sqrt{\psi_N}$ (§2.2, Figs. 13–15).

**Corroboration.** The JOREK review reports the same barrier ("transient
transport barrier of stochastic field lines outside $q=1$ in early TQ") as
a result of ITER Ne–D SPI simulations
([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.2, Fig. 8); it
summarizes this work. An earlier coronal-equilibrium study of argon SPI in
a JET-like plasma found the related delay between core $T_e$ collapse and
core impurity mixing: field lines from the edge needed more than 50
toroidal turns to reach the core at TQ onset, and core mixing lagged the
temperature collapse by more than 100 µs
([Hu et al. (2021)](/sources/hu-2021.md), §3, Figs. 8, 10). A later JOREK
study of neon–deuterium SPI in ASDEX Upgrade applies a 50 eV floor to the
Spitzer–Härm parallel diffusivity $\chi_\parallel$ "to help deal with low
temperature regions such as temperature holes"; whether the floor acts on
the temperature in the formula or on the diffusivity itself is ambiguous as
printed ([Tang et al. (2025)](/sources/tang-2025.md), §3.1). The floor is a
modelling response to the hole, not a further observation of it, and it
makes the parallel conduction differ from the Braginskii closure of Hu et
al. (2023) exactly where the hole forms.

## Significance

The barrier delays full stochastization and the loss of the hot core,
which bears on hot-tail runaway seed formation and loss (§1, §3.3, §5, as
motivation); the temperature hole makes the MHD response depend on the
parallel-conduction closure, which most SPI studies treat as a fixed
modelling choice.

## Limits of the evidence

One code, one equilibrium, one model family (reduced MHD, which "tends to
underestimate" the 1/1 instability, §2.2), $n=0$–11, a toroidally elongated
source (0.3–0.5 rad), and no comparison with experiment or with another
code (Hu et al. 2023). Without SPI no significant 1/1 growth occurs on the
timescale of interest (§2.2).

## Citations

- [Hu et al. (2023)](/sources/hu-2023.md), §2.2, §3.1–3.3, §4.1, §4.4, §5, Eq. 20, Figs. 3–4, 11–15, 21–22.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.2, Fig. 8.
- [Hu et al. (2021)](/sources/hu-2021.md), §3, Figs. 8, 10.
- [Tang et al. (2025)](/sources/tang-2025.md), §3.1.
