---
type: Definition
title: "Sawtooth crash and Kadomtsev reconnection"
description: "The periodic collapse of the core temperature inside an inversion radius, explained in the Kadomtsev model by complete reconnection driven by the (1,1) internal kink once a q = 1 (ι = 1) surface exists; simulated in tokamaks and, with M3D-C1, in full W7-X geometry, where purely resistive reconnection gives crashes about ten times slower than measured."
status: established
aliases: [sawtooth, sawteeth, sawtooth-like crash, Kadomtsev model, Kadomtsev reconnection, inversion radius]
tags: [kink, tearing, mhd, tokamak, stellarator]
timestamp: 2026-10-16T12:00:00Z
---

# Sawtooth crash and Kadomtsev reconnection

A sawtooth crash is a fast collapse of the core electron temperature that
flattens the profile inside an **inversion radius** $r_{\rm inv}$ (page-local
symbol): the temperature falls inside $r_{\rm inv}$ and rises outside it.
In the **Kadomtsev model** the crash is magnetic reconnection driven by the
$m/n=1/1$ [internal kink](/definitions/resistive-internal-kink.md), present
when $q<1$ somewhere ($\iota>1$ in stellarator notation). The $1/1$ island
grows at the $q=1$ surface, expels the original hot core and finally replaces
it, leaving a flattened profile
([Zhou et al. (2023)](/sources/zhou-2023.md), §I, §IV;
[Zhang et al. (2021)](/sources/zhang-2021.md), §1, which connects the
resistive kink to sawteeth and Kadomtsev reconnection without calling its own
nonlinear kink crash a sawtooth). The model predicts the reconnected state by
pairing flux surfaces of equal helical flux; the same construction, applied to
two resonant surfaces, predicts the relaxation region of the
[double tearing mode](/definitions/double-tearing-mode.md)
([Nardon et al. (2023b)](/sources/nardon-2023-b.md), §II, attributing the
generalization to Maget et al. 2007).

**Limits of the model.** Purely resistive reconnection cannot account for the
fast crashes observed; two-fluid or plasmoid-mediated reconnection (see
[plasmoid instability](/definitions/plasmoid-instability.md)) may be needed
(Zhou et al. 2023, §IV, citing tokamak sawtooth simulations). At high $\beta$
the Kadomtsev picture "seem[s] elusive", and Wesson's quasi-interchange model
"might be more applicable" (§I, citing Wesson and Jardin et al. 2020). After
a crash, a saturated helical $(1,1)$ core can replace the cycle; that
behaviour is [magnetic flux pumping](/definitions/magnetic-flux-pumping.md).

## Sawtooth-like crashes in W7-X (M3D-C1)

W7-X shows sawtooth-like core crashes under electron cyclotron current drive
(ECCD). Zhou et al. (2023) simulate them with the stellarator version of
[M3D-C1](/software/m3d-c1.md): single-fluid visco-resistive MHD in SI, constant
density, and the ECCD as a fixed toroidal source current in Ohm's law, peaked
at $r/a\approx0.15$ (§II–III, Fig. 1). The rotational-transform profile, from a
1D current-diffusion model, has a near-axis hump with maximum about 1.2, so
two $\iota=1$ surfaces exist, at about $r/a\approx0.08$ and $0.33$ by figure
reading (Fig. 2). The VMEC equilibrium is made self-consistent with the
dissipative model by a VMEC → one-period M3D-C1 → VMEC → M3D-C1 sequence
(§III; see [VMEC](/software/vmec.md)).

* **Two successive $(1,1)$ kinks.** The inner one reconnects at the inner
  resonance and lowers the core $T_e$ only from 5 to about 4.8 keV
  ($t\approx1.2$–2 ms); the authors speculate that it corresponds to the
  precursors sometimes observed before "type-A" crashes. The outer one grows a
  $(1,1)$ island at the outer resonance that expels and overtakes the core,
  "signatures of Kadomtsev's sawtooth model"; $T_e$ falls below 2.5 keV
  ($t\approx2$–3 ms) (§IV, Figs. 3–5).
* **Agreement with experiment.** The crash amplitude, about 50%, and
  $r_{\rm inv}/a\approx0.4$ are consistent with typical medium "type-A"
  crashes (experimental values quoted from Zanini et al. 2020, not
  overplotted) (§IV, Fig. 6).
* **Disagreement.** The simulated crash takes $\gtrsim1$ ms against
  $\lesssim100\,\mu$s measured, attributed to purely resistive reconnection
  with enhanced viscosity (§IV).
* **Variants.** A temperature-dependent $\eta$ gives a slower, smaller crash
  (about 40% by figure reading) with $r_{\rm inv}/a\approx0.45$ (Fig. 8).
  Removing the $(1,1)$ seed changes nothing; an $\iota=5/6$ resonance near the
  axis has no noticeable effect, so the small "type-B" crashes linked to it
  elsewhere are not reproduced (§IV).

The interpretation that type-A crashes are $(1,1)$-kink reconnection agrees
with Aleynikova et al. 2021, whose 1D model also generated the input $\iota$
profile, so the agreement is not independent in its input (§V). Suzuki et al.
2021 found core crashes driven instead by high-$n$ ballooning modes coupling
to low $n$, with different $\iota$ profiles and mid-radius ECCD (§I).

## Sawteeth in tokamak simulations of the sources

* **As NTM seeds.** A $1/1$ sawtooth crash coupling to existing $4/3$ and $3/2$
  islands seeds $2/1$ [neoclassical tearing modes](/definitions/neoclassical-tearing-mode.md)
  in DIII-D (Bardóczi et al. 2021, cited by
  [Howell et al. (2022)](/sources/howell-2022.md), §I). NIMROD NTM studies
  raise $q_0$ above 1 to remove the internal kink and sawteeth (§III A), as do
  linear M3D-C1 resistive-wall studies ([Strauss et al. (2022)](/sources/strauss-2022.md),
  §II).
* **Benchmarks of the nonlinear kink crash.** CLT and M3D-C1 reproduce a
  nonlinear $1/1$ resistive-kink crash with qualitatively identical
  post-crash oscillations ([Zhang et al. (2021)](/sources/zhang-2021.md),
  §3.2; details on [resistive internal kink](/definitions/resistive-internal-kink.md)).
* **After a runaway-beam loss.** In the M3D-C1 DIII-D runaway-termination
  case, $q_0$ drops from 1.10 to 1.0 and a $(1,1)$ kink flattens the residual
  runaway core; a persisting $n=1$ keeps $q_0\approx1$ inside
  $\sqrt{\psi_N}\approx0.4$ with sawtooth-like flattening
  ([Liu et al. (2021)](/sources/liu-2021.md), §5.3–5.4, Figs. 12, 16).

## Contradictions

None open. The W7-X mechanism contrast with Suzuki et al. 2021 (not ingested)
is conditioned on different $\iota$ and ECCD profiles.

# Citations

- [Zhou et al. (2023)](/sources/zhou-2023.md) — §§I–V, Figs. 1–8.
- [Zhang et al. (2021)](/sources/zhang-2021.md) — §1, §3.2.
- [Nardon et al. (2023b)](/sources/nardon-2023-b.md) — §II (generalized Kadomtsev construction).
- [Howell et al. (2022)](/sources/howell-2022.md) — §I, §III A.
- [Strauss et al. (2022)](/sources/strauss-2022.md) — §II.
- [Liu et al. (2021)](/sources/liu-2021.md) — §5.3–5.4.
