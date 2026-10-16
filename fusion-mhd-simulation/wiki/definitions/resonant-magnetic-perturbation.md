---
type: Definition
title: "Resonant magnetic perturbations and plasma response"
description: "Small non-axisymmetric fields applied by external or in-vessel coils whose harmonics resonate with edge rational surfaces q = m/n; the plasma response (screening, kink-peeling amplification, island penetration) decides whether they mitigate or suppress ELMs, and nonlinear MHD codes model them through a ramped vacuum boundary field or self-consistent coils."
status: established
aliases: [RMP, RMPs, magnetic perturbation, MP, plasma response, RMP ELM suppression, ELM mitigation by RMP, density pump-out]
tags: [elm, pedestal, edge, tokamak, mhd, extended-mhd, free-boundary, wall, tearing]
timestamp: 2026-10-16T12:00:00Z
---

# Resonant magnetic perturbations and plasma response

A resonant magnetic perturbation (RMP) is a small non-axisymmetric field
produced by coils outside the plasma. Each toroidal harmonic $n$ of the coil
field contains poloidal harmonics $m$, and those with $q=m/n$ at an edge
rational surface are resonant there. Because the edge-resonant $m$ are high,
the perturbation of a harmonic decays from the coils roughly as a power
$m$ of the distance, so at fixed coil current the edge ergodization falls as
$n$ rises ([Becoulet et al. (2022)](/sources/becoulet-2022.md), §4, Fig. 8;
the decay law is stated, the energies are shown). In vacuum the resonant
harmonics would open islands and an ergodic edge layer and split the
separatrix into lobes. The plasma does not respond as vacuum. Its rotation
and currents screen the resonant field, while the external kink-peeling
response can amplify it. This response, not the vacuum field, is what the
nonlinear simulations of this bundle compute
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §5;
[Becoulet et al. (2022)](/sources/becoulet-2022.md), §1).

RMPs are used to mitigate or suppress
[edge-localized modes](/definitions/edge-localized-mode.md). Applied as a
short transient, a magnetic perturbation is also used to seed islands
(below). An unwanted static perturbation of the same kind is an error field,
whose penetration is a disruption precursor
([disruption](/definitions/disruption.md)).

## How codes impose an RMP

- **Ramped vacuum boundary field.** JOREK prescribes a precomputed vacuum
  perturbation of $\psi$ on the computational boundary and ramps it up
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.4). In the ITER
  study of [Becoulet et al. (2022)](/sources/becoulet-2022.md) (§2) the vacuum
  field of the $3\times9$ in-vessel coils is computed by the ERGOS code and
  imposed at the boundary, which follows the ITER wall. It is ramped over a
  few ms to avoid transient unphysical currents in the vacuum region, before
  the non-axisymmetric harmonics other than the RMP are seeded. No STARWALL
  coupling is used there: the model is fixed-boundary.
- **Self-consistent coils.** Through [STARWALL](/software/starwall.md) the
  coils become part of a free-boundary vacuum response
  ([resistive-wall coupling](/methods/resistive-wall-coupling.md);
  [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.4, §2.9). This
  free-boundary model "was shown to recover experimental flux surface
  corrugation accurately" ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md),
  §2.2).
- **Coil currents and phasing.** In the ITER model, coil $k=1,\dots,9$ of a
  row at toroidal centre angle $\phi_k$ (degrees, $40^\circ$ apart) carries
  $$I_k=I_{\mathrm C}\cos\!\big[-n(\phi_k-\phi_{\mathrm{row}})\,\pi/180\big],$$
  with $I_{\mathrm C}$ the peak current and $\phi_{\mathrm{row}}$ the phase of the row
  ([Becoulet et al. (2022)](/sources/becoulet-2022.md), §2; page-local
  symbols, orientation of $\phi$ not stated). The relative phases of the
  upper, middle and lower rows are taken from the linear code
  [MARS-F](/software/mars-f.md), converted to the ERGOS angle convention
  (Table 1; the compiler re-derived every converted entry on the Source
  page).

## Plasma response: what the simulations show

1. **Screening, mitigation, suppression.** JOREK simulations show screening
   of the vacuum field by the plasma response, then ELM mitigation and then
   suppression, with locking of modes to the RMP field. Nonlinear mode
   coupling is essential ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md),
   §5, KSTAR $n=2$ among the cases).
2. **A minimum model.** Becoulet et al. (2022, §1) name the minimum model that
   reproduces experiments: nonlinear and multi-harmonic, with realistic
   X-point and SOL geometry, realistic coil geometry and spectrum, toroidal
   rotation, two-fluid diamagnetic effects and neoclassical poloidal
   friction. They call the external kink-peeling response "an important
   factor for ELM suppression". This is stated from earlier AUG and KSTAR
   validation, not re-tested in that paper.
3. **ITER suppression threshold.** In the ITER 15 MA, 5.3 T H-mode with
   $n=3$ RMPs, ELM crashes are suppressed for peak coil currents above about
   45 kAt. The abstract and conclusions give 45–60 kAt, against a coil limit
   of 90 kAt. Above the threshold the RMP harmonic and its side harmonics
   $n=6,9$ dominate and the remaining harmonics stay small. Below it the RMP
   "usually" lowers growth rates but an ELM crash still follows
   ([Becoulet et al. (2022)](/sources/becoulet-2022.md), §4, Fig. 5). This is
   the primary source of the review statement that ITER suppression lies
   within the coil-current design limits
   ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §2.2).
4. **Spectrum of the suppressed state.** At 60 kAt, $n=2$, 3 and 4 RMPs all
   avoid crashes in the 15 MA case. The side harmonics $n\cdot k$ couple most
   strongly; the other harmonics are driven nonlinearly and saturate,
   "providing edge MHD turbulence instead of ELM crashes", at a higher level
   for $n=2$ and 4 than for $n=3$. Energy transport falls slightly with $n$;
   density transport, convective through the $E\times B$ flow, hardly
   changes (Becoulet et al. 2022, §4, Figs. 7–10). In the 12.5 MA case
   ($n=3$, 60 kAt) density transport exceeds energy transport, as in many
   RMP experiments (§5).
5. **Locking of a QH-like mode.** In the 10 MA ITER case the naturally
   saturated $n=3$ mode locks to the static $n=3$ RMP after a few ms, later
   at lower amplitude: about 12 ms at 40 kAt and 25 ms at 20 kAt, read from
   Fig. 11 (Becoulet et al. 2022, §5).
6. **Islands and pump-out.** An island forms at the pedestal top in
   ELM-suppressed ASDEX Upgrade plasmas (an experimental paper still
   submitted when reviewed). Adding electron polarization drift and
   neoclassical toroidal viscosity recovers the KSTAR density pump-out, by
   stepwise growth of the $5/1$ and $6/1$ islands, and island-mediated mode
   coupling reproduces suppression in KSTAR
   ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §2.2, Fig. 3; see
   [tearing mode](/definitions/tearing-mode.md)). Radial tungsten transport
   rises substantially at high enough coil current (§2.2).
7. **Penetration hysteresis.** RMP seeding of tearing modes shows
   hysteresis: penetration above about 2 kA, expulsion below 1.5 kA
   ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6).

## The X-point displacement criterion

Becoulet et al. (2022, §1, §6) adopt, after Liu et al. (2016, as cited), the
criterion that the maximum perpendicular displacement of the flux surfaces
near the X-point, computed with the linear plasma response, predicts
suppression better than the vacuum island-overlap (Chirikov) criterion. The
coil phasing is chosen to maximize this displacement at $\psi_N\approx0.99$.
The displacement is diagnosed in JOREK from the electron temperature
perturbation divided by the equilibrium temperature gradient (as printed it
is a displacement in flux; a factor $|\nabla\psi|$ is implied for the values
in mm). Results for the 12.5 MA case (§6, Figs. 17–18):

| Phase | Optimum phasing (60 kAt) | Non-optimum phasing (80 kAt) |
|---|---|---|
| MARS-F, linear | about 7 mm | about 7 mm (same displacement at the higher current) |
| JOREK, early single-$n=3$ phase | about 6 mm | about 8 mm |
| JOREK, later multi-harmonic phase | about 60 mm (stated, not shown) | — |

Linear and nonlinear codes agree in the early phase and diverge by an order
of magnitude once nonlinear coupling sets in. The MARS-F figure itself is
plotted at 30 kAt and scaled linearly to 60 kAt.

## Transient magnetic perturbations as an island seed

[Howell et al. (2022)](/sources/howell-2022.md) (§II B, Eqs. 11–12) apply a
1 ms $n=1$ magnetic perturbation with a broad poloidal spectrum at the
[NIMROD](/software/nimrod.md) boundary to seed a $2/1$ neoclassical tearing
mode, as a surrogate for an ELM. The normal field on the boundary is the
coil vacuum field times a compact-support bump envelope times
$e^{i\omega t}$. The modulation follows the linear theory of Fitzpatrick and
Hender (as cited): flow screening is weakest when the applied field is
almost in phase with the rotation of the resonant mode. In shaped geometry
a coil arrangement that would give a pure $m=2$ field in a cylinder gives a
broad poloidal spectrum, so the coil positions were tuned to raise the
$2/1$ component relative to $3/1$ and $4/1$; the $3/1$ and $4/1$ surfaces,
near the boundary, are hardly screened (§II B, §III B, Figs. 1, 5B). The
authors propose scans of the perturbation amplitude as a measure of an
equilibrium's resilience to neoclassical tearing modes (§V).

## Divertor footprints

RMPs split the strike lines into lobes with the $n$-fold symmetry of the
main harmonic. In the ITER 15 MA case the footprints extend about 20 cm
(inner) and 40 cm (outer). After normalizing the computed heat flux to
50 MW into the divertor (an assumed stationary state, about 66% of the
heating radiated), the flux falls from about 5 MW/m² at the strike point to
about 1 MW/m² at the outer baffle–first-wall junction; stationary values
stay within the target, baffle and first-wall design limits, but the
switch-on transient can be much larger
([Becoulet et al. (2022)](/sources/becoulet-2022.md), §7–8, Figs. 19–22).
Kinetic neutrals, recycling and pumping are absent from that model.

## Verification

- CLT and MARS-F were benchmarked on the linear plasma response to RMPs
  earlier ([Zhang et al. (2021)](/sources/zhang-2021.md), §2, cited without
  numbers; see [CLT](/software/clt.md)); M3D-C1 has a cited RMP
  linear-response benchmark as well (same place, no numbers).
- ERGOS and MARS-F were benchmarked in vacuum (Becoulet et al. 2022, §2; not
  shown).
- JOREK closes the energy balance in an ITER 15 MA RMP run with diamagnetic
  flows ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §4.3, Fig. 17).
- No code-to-code nonlinear RMP benchmark appears in the sources.

## Qualifications

- **Resistivity and time span.** The ITER runs use a normalized central
  resistivity about two orders above the realistic value and cover a few
  tens of ms, against an energy confinement time above 3 s; the Alfvénic
  time step of the implicit scheme sets the limit
  ([Becoulet et al. (2022)](/sources/becoulet-2022.md), §2, §7).
- **Version.** The ITER numbers come from the FEC 2020 manuscript; the
  published Nucl. Fusion article is longer and may differ (Source page).
- **Reviews.** Items 1, 6 and 7 come from the two JOREK reviews and rest on
  the cited originals; some were submitted papers or private communications
  when reviewed.

## Contradictions

None open.

# Citations

- [Becoulet et al. (2022)](/sources/becoulet-2022.md) — §§1–8, Table 1, Figs. 5–22.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — §2.4, §2.9, §4.3, §5, §6.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) — §2.2, Fig. 3.
- [Howell et al. (2022)](/sources/howell-2022.md) — §II B, §III B, §V, Eqs. 11–12.
- [Zhang et al. (2021)](/sources/zhang-2021.md) — §2.
