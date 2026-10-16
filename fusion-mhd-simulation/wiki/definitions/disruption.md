---
type: Definition
title: "Disruption: phases, current quench and current spike"
description: "A disruption is the rapid loss of thermal energy and then of plasma current of a tokamak discharge; it proceeds through a trigger phase, a thermal quench, a transient plasma-current spike and a current quench, and its consequences (heat loads, electromagnetic wall forces, runaway-electron beams) are what nonlinear MHD codes are asked to predict and mitigate."
status: established
aliases: [major disruption, current quench, CQ, plasma current spike, Ip spike, disruption mitigation]
tags: [disruption, mhd, tokamak, runaway-electrons, wall, impurities]
timestamp: 2026-10-16T12:00:00Z
---

# Disruption: phases, current quench and current spike

A **disruption** is the sudden termination of a tokamak discharge: the
plasma loses its thermal energy in a [thermal quench](/definitions/thermal-quench.md)
and then its current $I_p$ in a current quench. Major disruptions "pose a
severe risk for large fusion devices as they can produce excessive
electro-magnetic forces, heat loads, and in-depth material damage by beams
of relativistic electrons" ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3).
For ITER, unmitigated disruptions are "considered intolerable above modest
values (by ITER standards) of the plasma current and thermal energy"
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6), so disruption
mitigation is the "last line of defense" once control and avoidance have
failed ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3).

## Phases

The simulation literature of this bundle divides a disruption into the
following phases; each has its own page where it carries a load-bearing
definition.

1. **Pre-disruption and trigger.** Tearing-mode growth and locking to the
   wall, impurity-radiation-driven island growth near the density limit, and
   error-field or RMP penetration ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6.1);
   beta-limit disruptions in which a dominant $n=1$ internal kink evolves
   into a disruptive state ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.1);
   loss of vertical position control, which starts a
   [vertical displacement event](/definitions/vertical-displacement-event.md).
   In ITER "major disruptions will unavoidably lead to the loss of plasma
   control" and therefore to a VDE ([Artola et al. (2021)](/sources/artola-2021.md), §1).
   In mitigated disruptions the trigger is the injected material itself
   ([shattered pellet and massive material injection](/definitions/shattered-pellet-injection.md)).
   For locked-mode disruptions, [Strauss et al. (2022)](/sources/strauss-2022.md)
   (§I, §IV) argue that the locked mode is a precursor, not the instability
   that ends the discharge: the mode amplitude often does not grow before
   the TQ, and the TQ is produced by a
   [resistive-wall tearing mode](/definitions/resistive-wall-tearing-mode.md)
   once the $q=2$ surface lies close enough to the wall (≈0.65 of the wall
   radius in a step-current model, consistent with a DIII-D database
   boundary). A localized impurity deposition on $q=2$ can itself trigger a
   2/1 tearing mode in a tearing-stable equilibrium by reversing the
   resistive-interchange drive, above a threshold impurity density, and the
   classical criterion "local radiation above Ohmic heating" does not
   explain that threshold ([Zeng et al. (2023)](/sources/zeng-2023.md), §3,
   §5; see [radiation-triggered tearing](/results/radiation-triggered-tearing.md)).
2. **Thermal quench (TQ).** Loss of $W_{\mathrm{th}}$ by stochastic
   parallel transport and/or radiation; see
   [thermal quench](/definitions/thermal-quench.md).
3. **Current spike.** A transient rise of $I_p$ at the end of the TQ (below).
4. **Current quench (CQ).** The decay of $I_p$ in the cold, highly
   resistive post-TQ plasma. The changing current induces eddy currents in
   the wall and [halo currents](/definitions/halo-current.md) in the
   scrape-off layer, which together set the
   [electromagnetic wall forces](/definitions/wall-forces.md).
5. **Runaway-electron (RE) beam.** The parallel electric field of the CQ
   accelerates [runaway electrons](/definitions/runaway-electrons.md); in
   ITER the avalanche can convert most of the current into an RE plateau
   (≈10 MA of an initial 15 MA in the JOREK–DINA benchmark,
   [Bandaru et al. (2024)](/sources/bandaru-2024.md), §IV.B).

## Current quench

The CQ time is defined from the 80% and 20% crossings of the
pre-disruption current, extrapolated to the full decay:
$(t_{20\%}-t_{80\%})/0.6$ ([Artola et al. (2022)](/sources/artola-2022.md),
§4.1, after the ITPA database of Eidietis et al. 2015).

The CQ time relative to the wall time $\tau_w$ controls how the current
lost by the plasma is shared between the wall and the halo region. In
axisymmetric JOREK scans of an ITER 15 MA upward VDE the halo-current
fraction is ≈10% for a CQ much faster than $\tau_w$ and up to ≈50% for a
CQ much slower than $\tau_w$; mitigated ITER disruptions target CQ times of
50–150 ms against $\tau_w=0.5$ s, which gives a predicted halo fraction of
10–20% ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6.3, Fig. 62).
CQ times below 50 ms are not allowed in ITER because of eddy-current limits
on the blanket modules (same section). Predictive ITER simulations at
realistic post-TQ parameters show continuous MHD activity throughout the CQ
and reduced global wall forces in mitigated cases
([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.3); the mechanism of
the vertical-force reduction is the subject of
[vertical-force mitigation by massive material injection](/results/vertical-force-mitigation.md).

The primary study behind that summary is
[Artola et al. (2022)](/sources/artola-2022.md): 3D JOREK–STARWALL
simulations of two ITER 15 MA post-TQ states ($T_e\approx15$–30 eV on
axis) at Spitzer resistivity and parallel conduction, $n=0$–10, continued
past the CQ to ≈1.5 s. Several tearing modes grow at 2–3 ms$^{-1}$,
saturate and ergodize the field, after which core surfaces re-form (§4.1,
Figs. 3–5). The CQ times are 47 and 45.5 ms; because they are an order of
magnitude below $\tau_w\approx500$ ms, $q_{95}$ stays at 3–4, no 1/1 mode
appears and the horizontal force stays at noise level (§4.1–4.2, §5). The
two cases drift in opposite vertical directions, the downward one after a
large drop of $l_i(3)$ (0.26 in 3.3 ms) (§4.2). The source calls 45.5–47 ms
"close to the envisaged minimum CQ time" of 50 ms, while Hoelzl et al.
(2021, §6.3) state that CQs below 50 ms are not allowed in ITER: the
simulated cases sit just below the permitted range, which is a scope
remark on the cases, not a disagreement. Forces and halo currents of these
runs are on [wall forces](/definitions/wall-forces.md) and
[halo current](/definitions/halo-current.md).

The energy budget of the radiative CQ is set by Ohmic heating against
radiation: in axisymmetric JOREK gas-injection runs, the thermal energy is
mostly depleted by the time cooling and Ohmic power balance, after which
Ohmic conversion of magnetic energy feeds the radiation
([Hu et al. (2021b)](/sources/hu-2021-b.md), §5, Fig. 9). A model without
Ohmic heating cannot follow the CQ: the full-MHD shattered-pellet runs of
[Bhole et al. (2023)](/sources/bhole-2023.md) (§4.3.1, §5) stop after the
TQ for that reason.

Artificially raised resistivity, common for numerical reasons, shortens the
resistive current-decay time (which scales as $\mu_0$ times the square of
the relevant length over $\eta$) and so distorts both the CQ and the
pre-TQ dynamics of injection; present JOREK runs use realistic resistivity
at low $T_e$ with a cut-off above a threshold temperature
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6.2.1).

## Current spike

The $I_p$ spike is "a robust experimental observation associated to the TQ,
but a difficult one to reproduce quantitatively with 3D non-linear MHD
simulations"; earlier simulated spikes were much smaller than measured ones
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6.2.2). JOREK argon
massive-gas-injection simulations of JET pulse 85943, run with
realistically low resistivity, give a spike of the experimental magnitude
(same section, Fig. 57). The spike is observed in mitigated and unmitigated
disruptions alike ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3).

Further simulation evidence:

- Full-MHD neon SPI into a JET-like plasma reproduces a small $I_p$ spike
  at the end of the TQ ($I_p$ ≈2.0 → 1.88 MA over the TQ) when the
  shock-capturing coefficient is moderate; an over-diffusive stabilization
  setting removes both the TQ and the spike
  ([Bhole et al. (2023)](/sources/bhole-2023.md), §4.3.1–4.3.2, Figs. 14, 19).
- In the 3D NSTX hot-VDE benchmark $I_p$ rises transiently during the
  stochastic TQ, to ≈0.59 MA in JOREK and ≈0.565–0.57 MA in M3D-C1 and
  NIMROD from an equilibrium value of 0.574 MA (values read from Figs. 2,
  10 and 11 of [Artola et al. (2021)](/sources/artola-2021.md), not stated
  in the text).
- Reduced-MHD argon SPI into a JET-like plasma gives a spike during the TQ,
  $I_p$ ≈1.93 → ≈2.12 MA (read from Fig. 4 of
  [Hu et al. (2021)](/sources/hu-2021.md); no number in the text). Before
  the TQ, the stochastic field stops the contraction of the $n=0$ current
  sheet that follows the cooling front, because the nonlinear
  $\mathbf v\times\mathbf B$ term acts as a hyper-resistivity on the $n=0$
  current (§3, Fig. 5d).
- In the 3D ITER current-quench runs of
  [Artola et al. (2022)](/sources/artola-2022.md) the spike appears in the
  CQ, after saturation of a dominant 2/1 mode, with a rise of halo current;
  the MHD flattening of $j_\phi$ and $T_e$ extends beyond the last closed
  flux surface, and the authors propose that scrape-off-layer currents "may
  be playing a important role" in the spike (§4.2, §5, Figs. 6–8).
- A 4/1 double tearing mode in a JET runaway-beam-like plasma (no runaways
  modelled) produces a spike of about +30% with $l_i(3)$ falling to ≈0.58 of
  its initial value, an almost complete flattening of $j_\phi/B$ at nearly
  constant magnetic helicity, driven by overlapping islands plus a
  macroscopic 4/1 flow that stirs the plasma; this occurs only for
  normalized resistivities $5\times10^{-7}$ to $3\times10^{-6}$ (Spitzer at
  47–13 eV) ([Nardon et al. (2023b)](/sources/nardon-2023-b.md), §III–IV,
  Figs. 4–5; spike and $l_i$ ratios read from the figure). In that model
  helicity is dissipated only resistively (App. A). See
  [double tearing mode](/definitions/double-tearing-mode.md).
- M3D-C1 simulations of the final runaway loss of DIII-D shot 177040 give a
  small spike as the lost runaway current is replaced by Ohmic current and
  current flattening in the stochastic region lowers $l_i$; it is "smaller
  compared to that in experiment", which the authors attribute to fast
  reconnection that a Lundquist number of ≈$10^3$ does not capture
  ([Liu et al. (2021)](/sources/liu-2021.md), §5.3, §6, Fig. 12).

**Mechanism.** By Boozer's theory the spike is a relaxation of the current
profile at approximately conserved magnetic helicity, driven by field-line
stochastization; in a mean-field picture it is a hyper-resistivity $\eta_h$
in the poloidal-flux equation, of a magnitude tied to the field-line
stochastic diffusivity. Axisymmetric JOREK runs with an ad-hoc $\eta_h$ of
Boozer's magnitude reproduce the 3D runs
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6.2.2). A complete
relaxation at conserved helicity would give a far larger spike than
measured; JOREK runs conserve helicity well but show the stochasticity
decaying, from the core outward, before the current profile has flattened,
which points to incomplete relaxation rather than helicity dissipation
(same section). [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) (§3.4,
Fig. 11) refine the picture: the relaxation is driven partly by shear
Alfvén waves in the stochastic field, which restore a constant $j_\parallel/B$
along field lines (Boozer's mechanism), and partly by a macroscopic
$\mathbf E\times\mathbf B$ flow that mixes the core and also carries
impurities inward.

## Mitigation strategy

The ITER disruption mitigation system, based on SPI, pursues four goals
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6): radiate most of the
thermal energy uniformly; avoid an RE beam by raising the electron density;
make an RE beam that forms anyway terminate benignly by injecting into it;
and control the $I_p$ decay rate through the impurity content to limit
electromagnetic loads. Each goal maps onto a phase above and onto a set of
model extensions of the MHD codes: impurity models
([coronal equilibrium](/methods/coronal-equilibrium-impurity-model.md),
[collisional-radiative](/methods/collisional-radiative-impurity-model.md)),
the [runaway-electron fluid model](/methods/runaway-electron-fluid-model.md)
and [resistive-wall coupling](/methods/resistive-wall-coupling.md).

[Strauss et al. (2022)](/sources/strauss-2022.md) (Abstract, §V) argue
that, if locked-mode thermal quenches in ITER last about half a wall time
(75–125 ms), ITER disruptions "may be significantly more benign than
previously predicted" and the mitigation, prediction and runaway-mitigation
requirements could be relaxed; this is an extrapolation of a DIII-D and a
JET ratio, contrasted with the ≈20 ms predicted for unmitigated ITER VDEs on
[thermal quench](/definitions/thermal-quench.md).

## Qualifications

**Current-spike mechanism.** The two JOREK reviews do not disagree, but
they qualify a single-mechanism picture: [Hoelzl et al. (2021)](/sources/hoelzl-2021.md)
(§6.2.2) describe the spike through Boozer's helicity-conserving relaxation
with a mean-field hyper-resistivity; [Hoelzl et al. (2024)](/sources/hoelzl-2024.md)
(§3.4) state that JOREK results "seem quantitatively consistent with
Boozer's theory" but that "the picture is complicated" by the macroscopic
$\mathbf E\times\mathbf B$ mixing flow, which Boozer's shear-Alfvén
relaxation alone does not contain. A quantitative separation of the two
contributions to the spike amplitude, e.g. by suppressing the large-scale
flow in a controlled run, would settle how much of the spike each one
carries.

**Completeness of the relaxation.** [Hoelzl et al. (2021)](/sources/hoelzl-2021.md)
(§6.2.2) find the relaxation in JET MGI runs incomplete: stochasticity
decays from the core outward before the current profile has flattened.
[Nardon et al. (2023b)](/sources/nardon-2023-b.md) (§III–V) find an almost
complete flattening of $j_\phi/B$ at fixed helicity for a double tearing
mode, but only inside a resistivity window, and a gentle or small
relaxation outside it. The cases differ (gas injection into a thermal
plasma against a pressureless model of a runaway-beam plasma), so this is
a qualification: the degree of relaxation depends on resistivity through the
relative growth of secondary modes, not a fixed property of the spike.

## Contradictions

**ITER wall time — Open.** [Hoelzl et al. (2021)](/sources/hoelzl-2021.md)
(§6.3) use $\tau_w=0.5$ s for the halo-fraction scans, and
[Artola et al. (2022)](/sources/artola-2022.md) (§2, §4.3) give a vessel
L/R time of ≈500 ms; [Strauss et al. (2022)](/sources/strauss-2022.md)
(§V) give an ITER wall time of 250 ms, "50 times longer than in JET and
DIII-D", and base the 75–125 ms thermal-quench extrapolation on it. None of
the three defines which wall time it means (the $n=0$ vessel L/R time, the
penetration time of the $n=1$ perturbation, or the cylindrical
$\mu_0r_wd_w/\eta_w$ of the RWTM theory), so the factor 2 may be a
definitional difference; a statement of the definition and the vessel
model behind 250 ms would settle it.

## Citations

- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3, §3.1, §3.3, §3.4.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6, §6.2.1–6.2.2, §6.3.
- [Bhole et al. (2023)](/sources/bhole-2023.md), §4.3.
- [Bandaru et al. (2024)](/sources/bandaru-2024.md), §IV.B.
- [Hu et al. (2021b)](/sources/hu-2021-b.md), §5.
- [Artola et al. (2021)](/sources/artola-2021.md), §1, Figs. 2, 10, 11.
- [Artola et al. (2022)](/sources/artola-2022.md), §2, §4.1–4.3, §5.
- [Strauss et al. (2022)](/sources/strauss-2022.md), Abstract, §I, §IV–V.
- [Zeng et al. (2023)](/sources/zeng-2023.md), §3, §5.
- [Hu et al. (2021)](/sources/hu-2021.md), §3, Figs. 4–5.
- [Nardon et al. (2023b)](/sources/nardon-2023-b.md), §III–V, App. A.
- [Liu et al. (2021)](/sources/liu-2021.md), §5.3, §6.
