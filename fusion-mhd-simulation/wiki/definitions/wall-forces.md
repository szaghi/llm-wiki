---
type: Definition
title: "Electromagnetic wall forces (vertical and sideways)"
description: "The electromagnetic wall force is the integral of the Lorentz force over the conducting structures, computed as a Maxwell-stress surface integral; its vertical component is set mainly by the axisymmetric VDE and current quench and, when the current quench is much faster than the wall time, peaks on the wall time after the plasma current has vanished; its horizontal (sideways) component is set by low-n kinks and 3D halo currents, and its toroidal rotation matters for resonance with the vessel."
status: established
aliases: [wall force, vertical force, sideways force, horizontal force, asymmetric VDE force]
tags: [disruption, vde, wall, free-boundary]
timestamp: 2026-10-16T23:59:30Z
---

# Electromagnetic wall forces (vertical and sideways)

The **electromagnetic wall force** $\mathbf F_w$ is the total Lorentz force
on the conducting structures surrounding the plasma. During
[VDEs](/definitions/vertical-displacement-event.md) and current quenches it
is carried by eddy currents induced in the wall and by
[halo currents](/definitions/halo-current.md) that close through it.

## Definition and computation

$$\mathbf F_w\equiv\int_{\mathrm{wall}}\mathbf J\times\mathbf B\,dV=\frac{1}{\mu_0}\oint_{\mathrm{wall}^+}\Big[(\mathbf B\cdot\mathbf n)\,\mathbf B-\frac{B^2}{2}\,\mathbf n\Big]dS,$$

where $\mathrm{wall}^+$ is a closed toroidal surface enclosing the wall and
$\mathbf n$ its outward normal; JOREK and NIMROD evaluate the surface form
(after Pustovitov, Rubinacci & Villone 2017), M3D-C1 the volume integral
over its meshed vessel ([Artola et al. (2021)](/sources/artola-2021.md),
§4.1.4, Eq. 8). The components are the vertical force $F_{w,z}$ and the
horizontal (sideways) force $F_{w,h}=\sqrt{F_{w,x}^2+F_{w,y}^2}$ with
toroidal phase $\arctan(F_{w,y}/F_{w,x})$ (same source, Fig. 8).
[Artola et al. (2022)](/sources/artola-2022.md) (§1, Eq. 1) print the same
identity with the $1/\mu_0$ on the volume integral instead of the surface
integral, which is dimensionally inconsistent as printed; the form above is
the consistent one. Since the surface integral needs the field to have
penetrated the wall, $\mathbf F_w\approx0$ for times short compared with
$\tau_w$ (same section).

**Halo–eddy decomposition.** When no current crosses the wall surface
($\mathbf J\cdot\mathbf n=0$, the situation of JOREK reduced MHD coupled to
STARWALL), the force of the eddy currents in the wall is the difference of
the Maxwell-stress integrals just outside and just inside the wall,

$$\mathbf F_{w,\mathrm{eddy}}=\mathbf F_w-\mathbf F_{w,\mathrm{halo}}=\oint_{\mathrm{wall}^+}\mathbf f\,dS-\oint_{\mathrm{wall}^-}\mathbf f\,dS,\qquad \mathbf f\equiv\frac{1}{\mu_0}\Big[(\mathbf B\cdot\mathbf n)\,\mathbf B-\frac{B^2}{2}\,\mathbf n\Big],$$

and the remainder is the force of the halo currents, which close at the
plasma-domain boundary ([Artola et al. (2021)](/sources/artola-2021.md),
§4.3.1, Eq. 9; the inner surface $\mathrm{wall}^-$ is not defined
explicitly in the source). JOREK treats the wall source and sink of the halo
current with the Zakharov–Atanasiu formalism as a post-processor for wall
forces ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.9).

## Vertical force

$F_{w,z}$ is "already significant before the onset of the instabilities",
i.e. dominated by the axisymmetric drift ([Artola et al. (2021)](/sources/artola-2021.md),
§4.1.4). In the NSTX 3D VDE its peak is ≈28–29 kN in all three codes, in
"excellent agreement" (§5, Fig. 8). In the JOREK decomposition, halo and
eddy contributions are similar before the TQ; after it, the core-current
decay induces halo current, the halo part grows from ≈−10 to ≈−30 kN and
the eddy part decreases from ≈−10 to ≈+2 kN, so the maximum force is due
to halo currents (§4.3.1, Fig. 12).

In mitigated disruptions the vertical force falls because broad,
predominantly toroidal SOL currents decouple the current centroid from the
axis motion ([vertical-force mitigation](/results/vertical-force-mitigation.md);
[Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.3). Predictive ITER
current-quench simulations at realistic post-TQ parameters show reduced
global wall forces with mitigation (same section;
[Artola et al. (2022)](/sources/artola-2022.md), the primary study, below).

**Current-moment estimate.** The vertical force follows the vertical
current moment, $F_{w,z}\propto I_p\,\Delta Z_{\mathrm c}$, with
$Z_{\mathrm c}=\int j_\phi Z\,dR\,dZ/I_p$ the current centroid and
$\Delta Z_{\mathrm c}$ its displacement ($Z_{\mathrm c}$ registry §11;
[Vannini et al. (2025)](/sources/vannini-2025.md), §4, Eq. 2, after Gruber
et al. 1993). In a 2D EU-DEMO VDE mitigated by neon the moment and the force
saturate at about 13 MN without runaways; with a 13 MA runaway beam they keep
growing, to about 43 MA m and 60 MN at 570 ms. In 3D the beam termination
"slightly reduces" the force (§4–5, Figs. 3, 6; values read from the
figures). See [vertical-force mitigation](/results/vertical-force-mitigation.md).

### Vertical force after the current quench (fast-CQ limit)

3D JOREK–STARWALL simulations of two ITER 15 MA mitigated current quenches
($\tau_{\mathrm{CQ}}$ 47 and 45.5 ms, vessel L/R time ≈500 ms) continued to
≈1.5 s find that $F_{w,z}$ is small during the CQ (about −1 to −1.5 MN in
case 1, read from Fig. 4c) and peaks at 11–14 MN some 300–400 ms after $I_p$
has vanished, i.e. on the wall time ([Artola et al. (2022)](/sources/artola-2022.md),
§4.3, §5, Fig. 9; the abstract quotes 13 MN, case 2 rounded). The authors
attribute it to diffusion of the net toroidal wall current along the
contour of the up-down asymmetric vessel and its interaction with the
poloidal-field-coil field: the maximum force and the final inner-vessel
current distribution are "roughly identical" for the upward and the
downward case (§4.3, Fig. 10). The peak is a factor ≈6 below the ≈80 MN of
the "broadly accepted" earlier estimates (Sugihara 2007, Clauser 2019, as
cited). The force "would in principle not arise" in an up-down symmetric
plasma and vessel, which the authors propose as a DEMO design criterion
(inference, not simulated). They note that 3D simulations "are typically
not continued after the plasma current vanishes" and that the effect "has
been largely ignored in the literature", while time traces of Albanese et
al. 2015 with volumetric walls and the COMPASS-U study of Yanovskiy et al.
2021 show it (§1, §4.3). Blanket modules, electrically insulated from each
other, are omitted on the argument that toroidal current cannot circulate
through them (§2). The halo contribution can
be controlled through the current-quench time: in ITER the predicted halo
fraction of 10–20% for 50–150 ms CQs means the halo loads can be more than
halved relative to their maximum ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6.3).

## Sideways force

3D MHD instabilities during VDEs localize the loads and produce a net
sideways force; this force can rotate toroidally, and when the rotation
frequency resonates with natural frequencies of the vessel the loads on the
vessel and supports become large ([Artola et al. (2021)](/sources/artola-2021.md),
§1, citing Schioler 2011 and Gerasimov 2014). The horizontal force appears
once $q_a$ falls below about 2 and low-$n$ external kinks grow (§1, §4.1.2).

In the NSTX 3D VDE ([NSTX VDE benchmarks](/benchmarks/nstx-vde-benchmarks.md)):

- $F_{w,h}$ correlates with the $n=1$ magnetic energy $W_{\mathrm{mag}}^{(1)}$:
  two peaks of one match two peaks of the other in JOREK
  ([Artola et al. (2021)](/sources/artola-2021.md), §4.1.4).
- The force makes less than one toroidal turn after the TQ in all codes;
  NIMROD shows no rotation, JOREK and M3D-C1 some rotation between the
  $n=1$ peaks (same section).
- The sideways force is governed by the halo currents (mainly $F_{w,y}$),
  and the eddy-current force opposes it and reduces the total (§4.3.1,
  Fig. 12).
- Ten times larger $\kappa_\parallel$ shortens the TQ by a factor ≈3 and
  raises $F_{w,h}$ during the TQ, but the peak force stays similar
  (3.5–4.2 kN across the JOREK variants); a three times smaller viscosity
  has a perceptible effect on the force (§4.3.2, Fig. 13).
- Doubling the toroidal resolution changes neither $I_p$, $W_{\mathrm{th}}$
  nor the forces significantly (§4.2, Fig. 11).

**Fast current quenches.** In the ITER mitigated CQs of
[Artola et al. (2022)](/sources/artola-2022.md), $q_{95}$ stays at 3–4
because $\tau_{\mathrm{CQ}}\ll\tau_w$, no 1/1 mode appears, and
$F_{w,h}$ stays "at the noise level", below 1 MN; it decays completely when
$I_p$ vanishes, which the authors take as confirmation that it is
resolution noise (§4.1–4.3, §5, Figs. 4c, 6c, 9). This agrees with the
statement above that the sideways force needs $q_a$ below about 2. When
the vertical force peaks the plasma current has vanished, so "there is no
electromagnetic source to drive the rotation": in the limit
$\tau_{\mathrm{CQ}}/\tau_w\ll1$ the force is non-rotating and resonance with
the vessel's natural frequencies is "not relevant" (§1, §5; argued from the
timing, the force phase is not plotted). The run cost is "of the order of 5
million core.hours per simulation" (§5).

Accurate prediction of horizontal forces linked to 1/1 kinks requires
coupling the full-MHD model of JOREK to the volumetric wall code and halo
currents through the wall, both ongoing
([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3); see
[resistive-wall coupling](/methods/resistive-wall-coupling.md).

## Contradictions

**Sideways-force agreement in the 3D NSTX VDE benchmark — Open; kept Open
by human decision (2026-10-16).**
[Artola et al. (2021)](/sources/artola-2021.md) (§4.1.4, §5) report that
the horizontal force "shows a good agreement in magnitude" and give the
predicted maxima as 2.5–3.5 kN; the peak values read from their Fig. 8 are
≈3.4 kN (JOREK), ≈2.8 kN (M3D-C1) and ≈2.5 kN (NIMROD).
[Hoelzl et al. (2021)](/sources/hoelzl-2021.md) (§4.8, summarizing the same
benchmark) describe the horizontal force as "in reasonable quantitative
agreement with NIMROD showing a factor two smaller force than the other two
codes". The figure readings give a NIMROD-to-JOREK ratio of ≈0.74, not
0.5, so the two characterizations of one data set disagree; the review may
quote an earlier state of the comparison (its arXiv v3 cites the benchmark paper as
submitted). Tabulated peak values of $F_{w,h}$ per code from the
published version of the benchmark would settle it.

**ITER sideways force in fast current quenches — Open (as stated by one
side).** [Artola et al. (2022)](/sources/artola-2022.md) (§1, §5) find
$F_{w,h}<1$ MN, at noise level, for $\tau_{\mathrm{CQ}}/\tau_w\approx0.1$
at realistic Lundquist number, and compare it with 3D MHD results of
Strauss (2018, as cited; not ingested) of ≈30 MN for
$\tau_{\mathrm{CQ}}/\tau_w\gg1$ and ≈4 MN for $\tau_{\mathrm{CQ}}/\tau_w\ll1$,
and with ≈40 MN extrapolated from JET by Noll's formula or a source/sink
model. Both 3D studies find the force falling with faster CQ, but the
fast-CQ magnitudes differ by more than a factor 4. Artola et al. stress
their realistic Lundquist number and Spitzer conduction; the Strauss
setup (resistivity, wall model) is known here only through this citation.
Only one side is ingested; the entry records the disagreement as Artola et
al. state it. Ingesting Strauss (2018), or a run of either code in the
other's parameter regime, would settle it.

## Citations

- [Artola et al. (2021)](/sources/artola-2021.md), §1, §4.1.4, §4.2, §4.3.1–4.3.2, §5, Eqs. 8–9.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.9, §4.8, §6.3.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3, §3.3.
- [Artola et al. (2022)](/sources/artola-2022.md), §1–2, §4.1–4.3, §5, Eq. 1, Figs. 4, 6, 9–10.
- [Vannini et al. (2025)](/sources/vannini-2025.md), §4–5, Eq. 2, Figs. 3, 6.
