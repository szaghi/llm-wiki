---
type: Definition
title: "Magnetic flux pumping"
description: "A saturated (1,1) helical core mode whose dynamo redistributes current so as to clamp the central safety factor at about 1, replacing the sawtooth cycle; found in JOREK for sufficiently peaked pressure (1/1 quasi-interchange), quantified for the ASDEX Upgrade hybrid scenario at a slow negative dynamo of a few mV/m, and seen in M3D-C1 simulations of W7-X after an ECCD-driven crash."
status: established
aliases: [flux pumping, saturated (1,1) core, sawtooth-free helical core, hybrid scenario]
tags: [kink, mhd, full-mhd, tokamak, stellarator]
timestamp: 2026-10-16T18:00:00Z
---

# Magnetic flux pumping

Magnetic flux pumping is the redistribution of current by a saturated,
non-crashing $(1,1)$ helical core mode that keeps the central safety factor
$q_0$ at about 1: at or slightly above 1 in the summary of
[Hoelzl et al. (2024)](/sources/hoelzl-2024.md) (§4.4), at about 0.99 in
the first quantitative study of an experimental discharge
([Zhang et al. (2025)](/sources/zhang-2025.md), §3.4; see *Contradictions*).
Where current drive or peaking would push $q_0$ well below 1 and start a
[sawtooth](/definitions/sawtooth-crash.md) cycle, the mode instead removes
the excess central current continuously, so the plasma stays sawtooth-free.
Zhang et al. (2025, §1) define it as "a self-regulating process of toroidal
magnetized plasma under external drives, where the anomalous redistribution
of current density and pressure sustains a shear-free $q$-profile
($q_0\simeq1$) in the plasma core". The tokamak hybrid scenario, a
sawtooth-free regime with broad, shear-free core $q$ and current profiles and
a large non-inductive current fraction, relies on it (§1, stated).

The mechanism is the [MHD dynamo](/definitions/mhd-dynamo.md): the
correlated velocity and field fluctuations of the helical mode produce an
axisymmetric electric field that opposes the current drive ("negative
dynamo"). A second, smaller contribution comes from the flattening of $T_e$
and hence of $\eta$ in the core (Zhang et al. 2025, §1, §2.2, after Krebs et
al. 2017 as cited).

## Sources

* **JOREK review (tokamak).** A $1/1$ quasi-interchange mode keeps $q_0\ge1$
  if the pressure is peaked enough, which prevents sawteeth and thereby
  removes a seed of
  [neoclassical tearing modes](/definitions/neoclassical-tearing-mode.md).
  An analytical quasi-linear expression for the normalized current
  redistribution has been derived and a reduced model is in development
  ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §4.4, refs. [82, 83];
  stated in the review, details in the cited works).
* **JOREK, ASDEX Upgrade hybrid discharge #36663.** Full two-temperature
  [visco-resistive MHD](/methods/visco-resistive-mhd-model.md) with
  experimental parameters over the resistive time: Spitzer
  $\eta_0=2.41\times10^{-9}$ Ω m, Lundquist number $2.8\times10^8$, magnetic
  Prandtl number 1400 and Hartmann number $7.9\times10^6$, all built on a
  length of 0.1 m; 700 ms in 3D and up to 1.8 s in 2D
  ([Zhang et al. (2025)](/sources/zhang-2025.md), §2.4, Table 1). Details
  below.
* **M3D-C1 (W7-X).** After the ECCD-driven outer $(1,1)$ crash, a saturated
  $(1,1)$ helical core forms and "the plasma does not tend to restore the
  initial equilibrium", so the crash cycle does not repeat
  ([Zhou et al. (2023)](/sources/zhou-2023.md), §IV, Fig. 7). The authors relate
  the structure to flux pumping and note that such post-crash saturated
  $(1,1)$ structures are "fairly common in tokamak simulations" and sensitive
  to transport parameters (their refs. [10–13]). The structure is robust to a
  temperature-dependent resistivity (Fig. 8) but does not form if the ECCD is
  switched off during the crash (not shown). The authors suggest that an
  ECCD model following the evolving field could recover cyclic behaviour.

## The ASDEX Upgrade case (Zhang et al. 2025)

**Without helical modes the core peaks.** In 2D ($n=0$) runs the
off-axis-peaked non-inductive current source (NBI, ECCD and a fixed
bootstrap part, heavily smoothed) raises the maximum $j_\phi$ by about 30%
and drives $q_0$ from 1.04 down to 0.79 at $\sqrt{\psi_N}=0.1$, unsaturated;
with 100 times the resistivity $q_0$ saturates at about 0.75. The saturated
2D range over the three source shapes tested is $q_0\approx0.6$–0.75 and
$j_{\max}\approx3.2$–4 MA/m² (§3.1, §5, §6.1, Figs. 4–5, 9d). This
contradicts the observed sawtooth-free phase.

**Linear and early nonlinear phase.** In 3D ($n\le4$) an $n=1$, $m=1$
quasi-interchange grows at $\gamma=19.46$ ms$^{-1}$; its flow is a core-wide
convection cell, unlike the internal kink, whose flow peaks at $q=1$
(§3.2, Fig. 6; see [interchange modes](/definitions/interchange-mode.md)). At
saturation $q_0$ drops by 0.03 in 0.1 ms and then oscillates around 1.013 at
5.8 kHz for a few ms, driven by a "fast dynamo" of up to 1.5 V/m that
alternates sign at the same frequency (§3.3, Fig. 7). The authors read this
as self-regulation that removes small equilibrium errors, so manual
fine-tuning of profiles "is not necessary" (§3.3, stated).

**Quasi-stationary clamped state.** $q_0$ falls from 1.04 to about 1 within
100 ms and saturates at about 0.99 over $\sqrt{\psi_N}<0.3$ after 200 ms;
the core $j_\phi$ stays at about 2.5 MA/m², near its initial 2.4, against more
than 3 MA/m² in 2D, and the core pressure gradient "almost vanishes"
(§3.4, Figs. 8–10). The slow dynamo that holds this state is negative in the
core and three orders of magnitude below the fast one. The flow is a few m/s
near $q=1$, comparable to the estimate for DIII-D #164661 and not
measurable in AUG (§3.4, Fig. 11).

**Field-electric balance.** The flux-surface-averaged toroidal induction
equation, differenced between the 3D and 2D runs, splits the electric-field
deficit of $-1.6$ mV/m into a net dynamo contribution ($-0.3$, $-1.35$ and
$-1.6$ mV/m at 90, 205 and 505 ms) and resistivity flattening (about 0,
$-0.25$ and $-0.3$ mV/m) (§4.1, Eq. 8, Fig. 13). The decomposition and the
parallel projection are on [MHD dynamo](/definitions/mhd-dynamo.md). At
505 ms the flux-surface-averaged current-diffusion equation shows "excellent
cancellation" between the current drive and the dynamo diffusion, while at
90 ms the drive still slightly exceeds it (§4.3, Eq. 12, Fig. 16).

**Mode structure.** The saturated core holds two twisted $1/1$ flux tubes:
the original axis keeps a local $q_0\approx1.04$ (topology unchanged, read as
the ideal quasi-interchange), and a new island-like tube has a local
$q_0\approx0.97$ (read as the resistive $1/1$ tearing component); the flow
concentrates at the X-point under the new tube, "suggesting an incomplete
magnetic reconnection" (§3.4, Fig. 12, §6.1; local $q$ traced about the
helical axis). The mode is "a combination of the 1/1 ideal quasi-interchange
mode and the 1/1 resistive tearing mode" (§6.1; see
[tearing mode](/definitions/tearing-mode.md)).

**Robustness and parameter dependence.**
* Off-axis and on-axis sources at the experimental strength (about
  2.70 MA/m²) also stay sawtooth-free in 3D, with $q_0$ near 1 and a dynamo
  that follows the source shape; on-axis ECCD is therefore compatible with
  sawtooth suppression, and these runs agree better with the reconstructed
  profiles (§5, Figs. 17–19).
* Toroidal truncation $n\le1$ "cannot correctly capture the flux pumping";
  $n\le2$ and $n\le4$ differ by about 1% in saturated $q_0$ and $j_\phi$
  (§2.4, not plotted).
* Raising $\eta$ and $\nu$ (lowering the Hartmann number) gives periodic
  sawtooth-like oscillations with $q_0$ between 0.95 and 1.0 at a Hartmann
  number of about $10^5$, then a quasi-stationary $1/1$
  [resistive internal kink](/definitions/resistive-internal-kink.md) with
  $q_0\sim0.7$ near $10^4$ (§6.2, not shown; the text says "increase" where
  the printed values decrease, recorded on the Source page). Viscosity is a
  free parameter that "may significantly influence … the success or failure
  of flux pumping" (§6.2, stated).

**Comparison with experiment and earlier simulations.** The mV/m dynamo
field is "consistent with the experimentally reconstructed electric field
deficit" in AUG and DIII-D, whereas earlier simulations at enhanced
resistivity gave about 0.1 V/m; the authors call this "the first
quantitative result on the flux pumping and dynamo effect in tokamak hybrid
scenarios" (Abstract, §4.1, §6.2). No experimental electric field is plotted
in the paper, so the agreement is in order of magnitude. The 2D and 3D
$q_0$ evolutions are consistent with the "modeled" and "experimental"
curves of Burckhart et al. 2023 (§3.4, as cited).

**Cost.** About 0.5 M core-hours per 3D case on Marconi-Fusion; with
$\tau_R/\tau_A>10^6$ in AUG and ITER and DEMO more than 10 and 40 times
larger, 3D runs for those devices are judged "impractical", which motivates
a surrogate model (§6.2; see [JOREK](/software/jorek.md)).

## Relation to other core dynamics

The sources reach the saturated state from different directions: in JOREK
the mode prevents the first crash; in the W7-X runs it appears after one. In
all of them the controlling ingredients are the central current source (ECCD
in W7-X, the non-inductive source in AUG) and the pressure-driven trigger
(JOREK quasi-interchange). In the AUG case the trigger is pressure-driven
but the saturated core pressure is flat, and the authors credit the flow of
the tearing-like component with sustaining the helical state (Zhang et al.
2025, §3.4); "sufficiently peaked pressure" (Hoelzl et al. 2024) is
therefore a condition for onset, not for the saturated state (compiler's
reading). Both the W7-X and the AUG papers find the saturated $(1,1)$ state
sensitive to transport parameters (Zhou et al. 2023; Zhang et al. 2025,
§6.2). A related observation without the name: after a runaway-beam loss in
DIII-D a persisting $n=1$ keeps $q_0\approx1$ in the core
([Liu et al. (2021)](/sources/liu-2021.md), §5.4, Fig. 16). The internal
kink background is on
[resistive internal kink](/definitions/resistive-internal-kink.md).

## Qualifications

* **Fixed bootstrap part and frozen $F$.** The bootstrap current enters only
  through a fixed, smoothed source profile, the toroidal field function
  $F(\psi)$ is frozen, and $\eta$ acts only on the toroidal component of
  Ohm's law; Hall and diamagnetic terms are omitted (Zhang et al. 2025, §2.2,
  §2.4, §6.2; see [bootstrap current](/definitions/bootstrap-current.md)).
* **Three meanings of "$q_0$".** The source uses $q_0$ for the axis value, for
  $q$ at $\sqrt{\psi_N}=0.1$ (Figs. 7a, 9c) and for the local $q$ of a flux
  tube (Fig. 12); the numbers above carry the location stated in the paper.
* **Superseded note.** The chunk-2 version of this page stated that no source
  quantified the clamped $q_0$ or the pumping rate; Zhang et al. (2025) now do.

## Contradictions

* **Is $q_0$ held at or above 1? — Open.**
  [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) (§4.4) summarize JOREK
  flux pumping as keeping $q_0\ge1$. [Zhang et al. (2025)](/sources/zhang-2025.md),
  the primary JOREK study by an overlapping author list, find the
  axisymmetric $q_0$ saturated at about 0.99 over $\sqrt{\psi_N}<0.3$
  (§3.4, Fig. 9) and a local $q_0\approx0.97$ in the reconnected flux tube,
  with only the original tube at 1.04 (Fig. 12); §6.1 says $q_0$ "first
  decreases slightly below unity". The two statements differ in what "$q_0$"
  measures (axisymmetric, local per tube) and the review is a one-line
  summary of other papers (its refs. [82, 83]); Zhang et al. do not comment
  on the review. A statement from the JOREK group of whether the clamped
  state is meant as $q_0\ge1$ or $q_0\approx1$, with the measure named,
  would settle it.

# Citations

- [Zhang et al. (2025)](/sources/zhang-2025.md) — §§1–6, Eqs. 5–12, Table 1, Figs. 4–19.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) — §4.4.
- [Zhou et al. (2023)](/sources/zhou-2023.md) — §IV, Figs. 7–8.
- [Liu et al. (2021)](/sources/liu-2021.md) — §5.4, Fig. 16 (related observation).
