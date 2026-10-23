---
type: Definition
title: "Thermal quench"
description: "The thermal quench is the disruption phase in which the plasma loses most of its thermal energy, by parallel transport along stochastic field lines opened by MHD modes (external kinks, resistive-wall tearing modes, the 1/1 kink or tearing cascades after injection), by impurity radiation, or both; its duration (0.1 ms in NSTX, about 20 ms predicted for unmitigated ITER VDEs, 75–125 ms proposed for ITER locked-mode disruptions) is sensitive to parallel heat conduction, impurity atomic model, boundary conditions and numerical stabilization."
status: established
aliases: [TQ, radiative collapse, thermal collapse]
tags: [disruption, impurities, mhd, tokamak]
timestamp: 2026-10-16T18:38:00Z
---

# Thermal quench

The **thermal quench (TQ)** is the phase of a
[disruption](/definitions/disruption.md) in which the thermal energy
$W_{\mathrm{th}}$ collapses on a time short compared with the subsequent
current quench. In the nonlinear-MHD literature of this bundle two loss
channels produce it, often together:

- **Stochastic parallel transport.** MHD modes overlap, the field becomes
  stochastic, field lines connect the core to the wall, and heat is lost
  along them at the rate set by $\kappa_\parallel$.
- **Radiative collapse.** Injected impurities radiate ($P_{\mathrm{rad}}$)
  and absorb ionization energy, cooling the plasma from the outside in.

A TQ is therefore classified by its trigger: an MHD-triggered TQ in an
unmitigated disruption or a [hot VDE](/definitions/vertical-displacement-event.md),
and an injection-triggered TQ in a mitigated disruption
([shattered pellet and massive material injection](/definitions/shattered-pellet-injection.md),
[massive gas injection](/definitions/massive-gas-injection.md)).

## MHD-triggered TQ

In the 3D NSTX hot-VDE benchmark the plasma drifts into the wall, the edge
safety factor falls, and when $q_{95}\approx2$ low-$n$ external kinks
(2/1, 4/2, 6/3) grow from the edge, create an ergodic layer, open core
regions to the wall and produce filamentary pressure structures; the TQ
follows in all three codes ([Artola et al. (2021)](/sources/artola-2021.md),
§4.1.2–4.1.3, Figs. 6–7). Its duration is 0.14 ms (JOREK), 0.24 ms (M3D-C1)
and 0.20 ms (NIMROD), consistent with the ≈0.2 ms loss of core confinement
in NSTX disruptions (same source, §4.1.3; also
[Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §4.8). Once the 3D
instability sets in, the decay rate of $W_{\mathrm{th}}$ is dominated by the
3D dynamics, not by the (raised) perpendicular diffusivities
([Artola et al. (2021)](/sources/artola-2021.md), §4.1.1).

The TQ time depends sublinearly on parallel conduction: multiplying
$\kappa_\parallel$ by 10 shortens the JOREK TQ from 0.14 to 0.043 ms, a
factor ≈3, while the peak wall forces stay similar
([Artola et al. (2021)](/sources/artola-2021.md), §4.3.2, Fig. 13).

**Locked-mode TQ by a resistive-wall tearing mode.** In DIII-D shot 154576
the TQ lasts ≈2.5 ms, about half the 5 ms wall time, and in JET pulse 81540
≈1.5 ms, 0.3 of the wall time
([Strauss et al. (2022)](/sources/strauss-2022.md), §I, Fig. 1). Strauss et
al. attribute it to a (2,1)
[resistive-wall tearing mode](/definitions/resistive-wall-tearing-mode.md),
stable with an ideal wall: nonlinear [M3D](/software/m3d.md) runs give a
complete TQ by parallel transport along the stochastized field, with
$\tau_{\mathrm{TQ}}\approx3.4/\gamma$, tracking the parallel transport time
$a^2/(\kappa_\parallel b_n^2)$ ($b_n$ the normalized normal field
perturbation at the wall), and $\tau_{\mathrm{TQ}}\approx\tau_w/2$ at the
experimental wall Lundquist number (§III, Eq. 6, Fig. 4b). The TQ time is
then set by the mode growth, hence by $\tau_w$, rather than by
$\kappa_\parallel$ alone. A small drop of pressure from internal modes
before the TQ resembles the minor precursor disruptions in JET and DIII-D
(§III, interpretation).

For ITER, unmitigated VDE simulations predict a significantly longer TQ, "in
the range of 20 ms" ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.1).
In dedicated ASDEX Upgrade VDE experiments, JOREK reproduces the onset point
of the TQ during the vertical motion; the timing is strongly affected by the
SOL heat transport, controlled by the temperature below which the
$T$-dependence of $\kappa_\parallel$ is cropped (same source, §3.1, Fig. 5).
Ports in a 3D volumetric wall advance the TQ of a 3D hot VDE (≈12 ms
against ≈12.5 ms, read from the figure) and move it to a larger $q_{95}$
([Isernia et al. (2023)](/sources/isernia-2023.md), §VI, Fig. 10).

## Injection-triggered TQ

**Tearing cascade.** In JOREK deuterium massive-gas-injection simulations
of JET, the cold front reaches $q=2$, destabilizes a large 2/1 tearing mode
(boosted by helical cooling inside the island), which flattens $j_\phi$
there and steepens it further in; the steep gradient destabilizes 3/2 and
then 4/3 modes, and the combined modes make the field globally stochastic
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6.2.1, Figs. 54–55). See
[tearing mode](/definitions/tearing-mode.md).

**SPI regimes.** For shattered pellets the pre-TQ dynamics depend on the
ordering of the shard transit time and the resistive current-decay time in
the cooled region ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6.2.1).
Fast shards cause helical cooling at low-order rational surfaces and, for
$q_0<1$, excite the 1/1 internal kink when they reach $q=1$ (JET deuterium
SPI). Slow shards let the current profile contract, tearing modes cascade
from edge to core, and the TQ is usually triggered when shards reach $q=2$
(ASDEX Upgrade deuterium SPI, and any impurity SPI). Predictive ITER
neon–deuterium SPI shows the opposite ordering of edge and core: shards can
reach the core before the edge radiative collapse, and a transport barrier
of the stochastic field outside $q=1$ can persist in the early TQ until the
edge collapses ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.2,
Fig. 8). In full-MHD neon SPI into a JET-like plasma the core temperature
drops from ≈3.5 keV to below 1 keV between 2 and 3 ms after injection,
with ergodization by 3/1 and 2/1 and later 1/1 structures as fragments
cross $q=2$ ([Bhole et al. (2023)](/sources/bhole-2023.md), §4.3.1,
Figs. 13–14).

**Two-stage TQ in ASDEX Upgrade H-mode SPI.** In JOREK reduced-MHD
neon-doped deuterium SPI into AUG discharge #40355
([Tang et al. (2025)](/sources/tang-2025.md), §3.2, Figs. 5–12):

- *First stage.* About half of $W_{\mathrm{th}}$ is lost within roughly
  0.1–0.15 ms of fragment arrival, "mainly due to the convective and
  conductive transport caused by the magnetic field line stochastization at
  the edge". Vanguard fragments at $q=3$ induce 3/1 islands, the pedestal
  degrades, an outward heat flux makes the following fragments ablate
  suddenly, and a large 2/1 island at $q=2$ "triggers the global reconnection
  event, resulting in full stochastisation". The stage is nearly independent
  of the neon fraction and radiates little (≈0–27% radiation fraction at
  1 ms for 0.12–10% Ne). Faster and smaller fragments radiate more in it
  (§3.4–3.5), so the paper's §4 statement that the stage is "virtually
  independent of injection parameters" overstates (recorded on the Source
  page).
- *Second stage.* Radiation dominates (80–97% of the energy lost in the
  window), and a 1/1 mode ends it with a core collapse below 10 eV, aligned
  with a second magnetic-energy and radiation peak; higher neon makes it
  earlier and stronger. Pure deuterium injection has no second stage.
- *Durations.* Pre-TQ plus TQ lasts about 1 ms at 10% Ne and 3–5 ms at 0.12%
  Ne. AUG pre-TQ durations converge to 3–5 ms at ≥1% Ne and range from a few
  to about 70 ms without neon (Fig. 26), so the simulated durations are short
  at high neon against the converged value and, by the authors' reading
  ("especially with a low neon fraction"), at low neon against the longer
  low-neon experiments; the TQ ends,
  by the paper's definition, at $W_{\mathrm{th}}\approx100$ kJ (§3.5,
  Figs. 25–26).

The $q=2$ trigger of the first stage agrees with the review's statement that
slow shards in AUG deuterium SPI trigger the TQ when they reach $q=2$
(Hoelzl et al. 2021, §6.2.1).

**Strong-cooling limit: argon SPI at q = 2.** In reduced-MHD argon SPI into
a JET-like L-mode (pulse 85943 template, $q_0=0.98$), the $n=0$ current
contraction follows the cooling front and forms a current sheet on it; 3/1
and 2/1 modes grow as the front crosses $q=3$ and $q=2$ (2/1 from 1.72 ms),
the 2/1 drives a 3/2 core mode nonlinearly (1.90 ms) and the field becomes
globally stochastic, giving the TQ at ≈2.00 ms when the fragments reach
$q=2$ ([Hu et al. (2021)](/sources/hu-2021.md), §3, Figs. 5–7), in
qualitative agreement with JET SPI observations. The authors order two
destabilization mechanisms by cooling strength: axisymmetric current
contraction, on the time $\propto a^2/\eta$, dominates under strong
cooling; helical cooling at each rational surface, on the time
$\propto\delta l^2/\eta$ with $\delta l$ the cooled width, dominates under
the mild dilution cooling of deuterium SPI (§3, §6, attributed reasoning).
The core $T_e$ collapses more than 100 µs before the impurities mix into
the core: at TQ onset edge field lines need more than 50 toroidal turns to
connect to the core, and fast parallel conduction outruns parallel
convection of the material (§3, Figs. 8, 10). The resulting hollow density
is unfavourable for runaway-electron suppression (stated).

**Large q < 1 region: TQ at q = 1.** In ITER L-mode targets with a broad
$q\approx1$ core (7.5 MA, weakly reversed shear; and 15 MA with $q=1$ at
normalized flux 0.3) the TQ, or core relaxation, is triggered when the
vanguard fragments enter $q=1$ and destabilize the 1/1 kink, whose O-point
coincides with the fragments ([Hu et al. (2021)](/sources/hu-2021.md),
§4.1, Figs. 13–14; [Hu et al. (2023)](/sources/hu-2023.md), §3.1, Figs. 3–4).
The 2/1 and 3/1 islands are too narrow to couple to core modes because of
the strong edge shear (Hu et al. 2021, §4.1). The kink convects material
deposited on or inside $q=1$ into the core, so mixed hydrogen–neon pellets,
which penetrate deeper, give better core neon penetration than pure neon
(same section). In the 15 MA case the axisymmetric current contraction
plays a "minimal role", the region behind the front stays at $O(100)$ eV,
and the fragments reach the core before the edge radiative collapse,
especially at 500 m/s (Hu et al. 2023, §3.1–3.2); the TQ is gradual and
multi-stage, with a stochastic transport barrier outside $q=1$ that breaks
only when edge modes grow at ≈6 ms in the 200 m/s case (§3.3; see
[electron temperature hole and the q = 1 barrier](/results/electron-temperature-hole.md)).
Slower injection gives stronger radiative cooling and a larger MHD
amplitude at the same penetration (§3.1–3.2). At ≈4.85 ms the thermal loss
exceeds the radiated energy by 6 MJ, and by ≈6.4 ms 25 of 36 MJ are lost
(§3.1, Fig. 5).

**ITER H-mode dual SPI.** TQ times (90% → 20% of $W_{\mathrm{th}}$) of
2.0 ms in a 370 MJ baseline H-mode and 4.2–4.4 ms in a 190 MJ degraded
H-mode; in the baseline case with 1%-neon pellets
[plasmoid drift](/definitions/plasmoid-drift.md) collapses the pedestal and
loses more than 100 MJ before the fragments penetrate, with a radiated
fraction of 49.4% against 86–90% in the degraded H-mode with 5%-neon pellets
([Hu et al. (2024)](/sources/hu-2024.md), §3, Table 2, Fig. 7). The
radiation asymmetry of these quenches and its wall load are on
[radiation asymmetry](/definitions/radiation-asymmetry.md).

**Multi-valve gas injection in SPARC.** In NIMROD 90/10 D$_2$/neon MGI
([massive gas injection](/definitions/massive-gas-injection.md)), a
pre-TQ of about 2 ms (2.5 ms at high resolution) radiates 5–15 GW; the TQ
flash peaks at 40–55 GW at low resolution and about 70 GW with a narrower,
more deuterium-rich source, and the radiated energy fraction exceeds 95%
([Izzo et al. (2025)](/sources/izzo-2025.md), §II C–D, §IV, Figs. 4–5).
The equilibrium has $q_{\min}=1.05$ and no $q=1$ surface, yet a large 1/1
mode develops during the TQ and pulls neon from the edge inward; the
radiation peaks at the very start of that mixing (§II D, Fig. 7; see
[resistive internal kink](/definitions/resistive-internal-kink.md)). A
closed-circuit [runaway-electron mitigation coil](/definitions/runaway-electron-mitigation-coil.md)
seeds the $n=1$ and makes the TQ earlier (§III B). Raising the mass density
of the region between limiter and vessel forestalls the 1/1 mode; higher-$n$
modes then collapse the mid-radius temperature first and the TQ radiation
shows two peaks (§III C, Fig. 9b–c).

**Radiative collapse.** In axisymmetric JOREK argon and neon gas injection
into DIII-D, the collapse proceeds from the inside out with a hollow $T_e$
and a thin current and temperature halo, followed by re-concentration of
the current near a new axis ([Hu et al. (2021b)](/sources/hu-2021-b.md),
§6.2, Figs. 15–16). Idealized benchmarks impose the TQ instead of computing
it: [Bandaru et al. (2024)](/sources/bandaru-2024.md) (§III.A) cool the
plasma by a prescribed exponential with 1 ms time constant to ≈100 eV in
the core before letting radiation, Ohmic heating and ionization take over;
$T_e$ then settles at 6–9 eV and drops to ≈1 eV once runaway electrons carry
the current (§III.B). The EU-DEMO runaway study of
[Vannini et al. (2025)](/sources/vannini-2025.md) (§4) imposes an
*artificial thermal quench* of about 4 ms: neon is ramped up uniformly, the
thermal diffusivities are raised by hand and Ohmic heating is switched off
until $T_e\approx10$ eV, and a large hyper-resistivity flattens $j$ to mimic
the current spike; all parameters are then restored.

## Sensitivities

- **Impurity atomic model.** Coronal equilibrium underestimates the line
  radiation of weakly ionized states early in an injection. Compared with
  the collisional-radiative model, it delays the balance of cooling and
  Ohmic power ([Hu et al. (2021b)](/sources/hu-2021-b.md), §1, §4, Fig. 2).
  In the axisymmetric DIII-D benchmark of
  [the DIII-D gas-injection impurity benchmark](/benchmarks/diii-d-mgi-impurity-benchmark.md),
  JOREK's coronal-equilibrium model gives a collapse ≈2× slower than the
  charge-state-resolved M3D-C1 and NIMROD ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.7);
  with the collisional-radiative model JOREK agrees with NIMROD in shape and
  peak of the cooling power, with the argon peak 0.15 ms later
  ([Hu et al. (2021b)](/sources/hu-2021-b.md), §6.1, Fig. 11). The two
  observations point the same way. See
  [coronal-equilibrium](/methods/coronal-equilibrium-impurity-model.md) and
  [collisional-radiative](/methods/collisional-radiative-impurity-model.md)
  impurity models.
- **Temperature model.** A two-temperature model cools electrons faster
  than a single-temperature model, more markedly for neon
  ([Hu et al. (2021b)](/sources/hu-2021-b.md), §5, Figs. 7–8). In 3D ITER
  SPI, $|T_e-T_i|$ reaches ≈2 keV in the core during the TQ: electrons are
  flattened by parallel conduction while $T_i$ still shows the kink, so a
  single-temperature model lets ions heat electrons artificially and
  overestimates ablation ([Hu et al. (2021)](/sources/hu-2021.md), §4.2,
  Fig. 15; the ablation consequence is stated, not tested).
- **Parallel-conduction closure.** Braginskii $\kappa_\parallel\propto T_e^{5/2}$
  lets electron temperature holes form in the fragment plume, which raise
  the MHD response; a constant $\kappa_\parallel$ (the 500 eV value)
  suppresses them, weakens the MHD and delays the rise of radiated power
  ([Hu et al. (2023)](/sources/hu-2023.md), §3.2, §4.4, Figs. 11, 21–22).
  [Tang et al. (2025)](/sources/tang-2025.md) (§4) attribute their
  too-short pre-TQ and too-abrupt first stage in AUG to "overestimation of
  the parallel thermal conduction", through stronger cooling, higher $\eta$
  and stronger resistive MHD, and through excessive losses in stochastic
  regions (stated, not tested); their Spitzer–Härm $\chi_\parallel$ carries a
  50 eV floor against temperature holes (§3.1). For NIMROD MGI,
  [Izzo et al. (2025)](/sources/izzo-2025.md) (§IV) state that a constant
  $\kappa_\parallel$ overestimates transport in cold regions against a
  $T^{5/2}$ closure, which tends to underpredict radiation peaking and
  overestimate the conducted wall energy.
- **Viscosity.** Quoted from a NIMROD JET SPI study (McClenaghan et al.
  2023, not ingested): reducing the viscosity from 2000 to 500 m²/s shortens
  the TQ only from 2.9 to 2.6 ms ([Hu et al. (2024)](/sources/hu-2024.md),
  §5), used there to argue a weak viscosity sensitivity across codes.
  [Izzo et al. (2025)](/sources/izzo-2025.md) (§IV) rank their high
  viscosity, $\nu=500$ m²/s, among their most significant approximations,
  because a lower one would likely mix impurities faster and give less
  peaked radiation. The two statements concern different figures of merit
  (TQ duration against impurity mixing and peaking), so they qualify each
  other rather than conflict.
- **Source width.** Toroidally elongated density sources reduce the
  radiation and its peaking; see
  [pellet ablation models](/methods/pellet-ablation-models.md).
- **Numerical stabilization.** Shock capturing lets full-MHD SPI runs pass
  through the TQ with unchanged $W_{\mathrm{th}}$ and $I_p$ traces at moderate
  coefficients, but too strong a setting smears the dynamics, and the
  stronger sensor at low resistivity suppresses the TQ altogether
  ([Bhole et al. (2023)](/sources/bhole-2023.md), §4.3, Figs. 11, 19); see
  [shock-capturing artificial viscosity](/methods/shock-capturing-artificial-viscosity.md).

## Qualifications

**Trigger surface of impurity SPI** (qualification, downgraded from Contradictions by human decision, 2026-10-16). The SPI-regimes
paragraph above, after [Hoelzl et al. (2021)](/sources/hoelzl-2021.md)
(§6.2.1), states that for slow shards the TQ "is usually triggered when
shards reach $q=2$ (ASDEX Upgrade deuterium SPI, and any impurity SPI)".
[Hu et al. (2021)](/sources/hu-2021.md) (§4.1, §6) and
[Hu et al. (2023)](/sources/hu-2023.md) (§3.1, §5) find that neon or
neon–hydrogen SPI into ITER L-mode triggers the TQ at $q=1$ through the 1/1
kink, at 150 m/s as at 500 m/s, and attribute this to the large $q\approx1$
region and the edge shear; Hu et al. (2021) find the $q=2$ trigger in their
JET-like argon case, where there is almost no $q=1$ surface, and Hu et al.
(2023, §5) state that without a large $q=1$ region the 2/1 or 3/2 modes
"would dominate instead". The review cites Hu et al. (2021), so "any
impurity SPI" is best read as "any impurity SPI without a large $q<1$
region". Recorded as a qualification of the review's generalization; it
closes only if the review's statement is shown to be restricted to its
AUG-like profiles. The AUG neon–deuterium runs of
[Tang et al. (2025)](/sources/tang-2025.md) (§3.2), in which a 1/1 mode acts only in the final core collapse, show the
2/1 at $q=2$ triggering the global stochastization, which supports the
reading.

**Duration of the ITER thermal quench** (attributed contrast; qualification,
downgraded from Contradictions by human decision, 2026-10-16).
[Hoelzl et al. (2024)](/sources/hoelzl-2024.md) (§3.1) report JOREK
predictions of ≈20 ms for the TQ of unmitigated ITER VDEs;
[Strauss et al. (2022)](/sources/strauss-2022.md) (§V) project 75–125 ms
(or 70 ms with an $S_{\mathrm{wall}}^{4/9}$ scaling) for ITER locked-mode
disruptions driven by a resistive-wall tearing mode, from the ratio of TQ
time to wall time in DIII-D and JET, and call ITER disruptions "more benign
than previously predicted". The scenarios differ (VDE against locked mode)
and so do the methods (ITER simulations against a two-machine scaling), so
neither statement refutes the other; the projection also depends on an
ITER wall time that is itself contested (see
[disruption](/definitions/disruption.md), Contradictions). A JOREK or M3D
run of an ITER locked-mode case with a resistive wall would test the
scaling.

## Citations

- [Artola et al. (2021)](/sources/artola-2021.md), §4.1.1–4.1.3, §4.3.2.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.7, §4.8, §6.2.1.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.1, §3.2.
- [Bhole et al. (2023)](/sources/bhole-2023.md), §4.3.
- [Hu et al. (2021b)](/sources/hu-2021-b.md), §1, §4–6.
- [Bandaru et al. (2024)](/sources/bandaru-2024.md), §III.
- [Isernia et al. (2023)](/sources/isernia-2023.md), §VI.
- [Strauss et al. (2022)](/sources/strauss-2022.md), §I, §III, §V.
- [Hu et al. (2021)](/sources/hu-2021.md), §3, §4.1–4.2, §6.
- [Hu et al. (2023)](/sources/hu-2023.md), §3.1–3.3, §4.4, §5.
- [Hu et al. (2024)](/sources/hu-2024.md), §3, §5, Table 2.
- [Tang et al. (2025)](/sources/tang-2025.md), §3.1–3.5, §4, Figs. 5–12, 25–26.
- [Izzo et al. (2025)](/sources/izzo-2025.md), §II C–D, §III B–C, §IV.
- [Vannini et al. (2025)](/sources/vannini-2025.md), §4.
