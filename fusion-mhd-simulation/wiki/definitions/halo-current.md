---
type: Definition
title: "Halo current"
description: "The halo current is the current that flows partly in the scrape-off layer and closes through conducting structures in contact with it; its poloidal magnitude (halo fraction), toroidal peaking factor and 3D filamentary structure set the largest wall forces of VDEs, and its modelling depends on sheath and ion-saturation-current boundary conditions and on how the MHD code lets current cross into the wall."
status: established
aliases: [halo currents, halo fraction, toroidal peaking factor, TPF, SOL current]
tags: [disruption, vde, wall, edge, free-boundary]
timestamp: 2026-10-16T16:51:00Z
---

# Halo current

The **halo current** is "the current that flows partly in the plasma SOL,
closing its path via conducting structures in contact with the SOL"
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6.3). It appears when a
[vertical displacement event](/definitions/vertical-displacement-event.md)
or a current quench pushes current into open field lines that end on the
wall. The registry symbol $I_{\mathrm{halo}}$ denotes its poloidal part
unless a page states otherwise; the poloidal part closes through the wall
and loads it with $\mathbf J\times\mathbf B$ forces
([wall forces](/definitions/wall-forces.md)).

## Measures

- **Halo fraction.** The poloidal halo current crossing the wall,
  normalized to the pre-disruption current:
  $$\frac{I_{\mathrm{halo}}}{I_p(0)}=\frac{1}{I_p(0)}\int_{\mathrm{wall}}\frac{|\mathbf J\cdot\mathbf n|}{2}\,dS,$$
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6.3, Fig. 62 caption).
  The factor $1/2$ counts each poloidal current path once, since it crosses
  the wall surface twice (the compiler's reading; the source prints only the
  formula).
- **Toroidal peaking factor $\mathrm{TPF}$.** The toroidal maximum of the
  poloidal halo current over its toroidal mean,
  $$\mathrm{TPF}\equiv\frac{\max_\phi\Big(\frac12\oint_\phi|\mathbf J\cdot\mathbf n|\,R\,dl\Big)}{I_{\mathrm{halo}}/2\pi},$$
  with $dl$ the poloidal length element of the wall contour at fixed $\phi$
  ([Artola et al. (2022)](/sources/artola-2022.md), §4.1, Eq. 8). The
  numerator is the halo current per radian crossing the wall at $\phi$, with
  the same factor $\frac12$ as the halo-fraction formula above. Hoelzl et al.
  (2021, §6.2.4) give the same max-over-mean definition for the radiated
  power ([radiation asymmetry](/definitions/radiation-asymmetry.md)).
- **Design metric.** The product of halo fraction
  ($\mathrm{HF}=I_{\mathrm{halo}}/I_p(0)$) and $\mathrm{TPF}$ sets
  the ITER electromagnetic-load category: category I requires
  $\mathrm{HF}\times\mathrm{TPF}<0.15$, against an experimental maximum of
  0.75 in the ITPA database (as cited by
  [Artola et al. (2022)](/sources/artola-2022.md), §4.1, §4.4, from Lehnen
  et al. 2015 and Eidietis et al. 2015).
- **Toroidal halo current.** The toroidal current in the open-field-line
  region; in the 3D NSTX benchmark it reaches ≈0.4 MA (JOREK) and ≈0.35 MA
  (M3D-C1) late in the TQ, while NIMROD lacked the post-processing to
  separate open and closed field lines
  ([Artola et al. (2021)](/sources/artola-2021.md), §4.1.1, Fig. 2).

## Physics results

**Dependence on the current-quench time.** Axisymmetric JOREK scans of an
ITER 15 MA upward VDE (fixed halo temperature and width) give a halo fraction
of ≈10% when the current quench is much faster than the wall time $\tau_w$
and up to ≈50% when it is much slower, the latter similar to the maximum
values of DINA. Mitigated ITER disruptions, with CQ times of 50–150 ms
against $\tau_w=0.5$ s, should have 10–20%, so the disruption mitigation
system "could be used to reduce the halo current electromagnetic loads by
more than a factor 2 with respect to their maximum possible value"
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6.3, Fig. 62).

**Toroidal peaking.** In 3D JOREK runs of the same ITER VDE in the fast-CQ
limit, the $\mathrm{TPF}$, given by an $n=1$ kink, stays below ≈1.15 and
hardly depends on the CQ time, whereas experiments reach values of 4; the
runs use CQ times below 50 ms, which ITER does not allow, and are presented
for physical interest only ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md),
§6.3, Fig. 63). In ASDEX Upgrade hot-VDE simulations, the time traces of
$I_p$, $I_{\mathrm{halo}}$ and $\mathrm{TPF}$ match the experiment "for
appropriate values" of the SOL heat-transport parameter
([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.1, Fig. 5): the match
is conditional on a tuned boundary parameter.

**Mitigated ITER current quenches in 3D.** JOREK–STARWALL runs of two ITER
15 MA post-TQ states at realistic Lundquist number, with CQ times of 47 and
45.5 ms ([Artola et al. (2022)](/sources/artola-2022.md), §4.1–4.2, §4.4):

| | case 1 | case 2 |
|---|---|---|
| max poloidal halo fraction | 8.7% | 16.6% |
| max $\mathrm{TPF}$ (halo fraction at that time) | 1.2 (2%) | 1.7 (5.7%) |
| max $\mathrm{HF}\times\mathrm{TPF}$ | 0.09 | 0.17 |
| max toroidal halo current | 4.1 MA | 8.4 MA |

Case 2 lies "slightly above the level for category I". The halo fractions
agree with the 10–20% that Hoelzl et al. (2021, §6.3) predict for 50–150 ms
CQs. The $\mathrm{TPF}$ of 1.7 exceeds the ≲1.15 of the fast-CQ ITER VDE
runs above; the scenarios differ (mitigated CQ from a tearing-unstable
post-TQ state against a VDE with an $n=1$ kink), so the values are recorded
side by side, not as a contradiction. The scrape-off-layer temperature rises
to 10–15 eV from the 1 eV boundary value, "consistent with experimental
temperature measurements" (§4.4, Fig. 8). The authors caution that if a
cold halo limited the halo current, current would be re-induced in the
core, slowing the $I_p$ decay against the vertical motion and lowering
$q_{95}$, which could raise halo asymmetries; they call for SOL models with
Ohmic heating, radiation, neutrals and sheath conditions (§4.4, stated).

**3D structure.** In the NSTX 3D VDE, the wall normal current during the
thermal quench shows filamentary structures with strong $n=3$ content,
strong enough near the limiter point to reverse the sign of the $n=0$
normal current; at peak horizontal force the structure is dominantly $n=1$
([Artola et al. (2021)](/sources/artola-2021.md), §4.1.5, Fig. 9). The
peak wall forces of that case come from halo currents, not eddy currents
(§4.3.1, Fig. 12).

**Mitigated disruptions.** After massive impurity injection the plasma
inside and outside the separatrix has comparable temperatures, a large part
of $I_p$ flows in the SOL, and because $q_{95}$ rises these SOL currents are
mostly toroidal; the poloidal halo current therefore stays moderate even
though the SOL current is large, and the halo pattern broadens in both
simulations and experiments ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md),
§3.3, Fig. 10; see
[vertical-force mitigation](/results/vertical-force-mitigation.md)).
In a JOREK hot VDE of EU-DEMO mitigated by neon, a large fraction of the
current is likewise induced in the halo region outside the last closed flux
surface, so the current centroid stagnates near the midplane and the
vertical force saturates at $F_{w,z}\approx13$ MN; with runaway electrons
the authors read $I_p-I_{\mathrm{RE}}$ as the *toroidal* halo current
([Vannini et al. (2025)](/sources/vannini-2025.md), §4, Fig. 3, p. 7; an
interpretation of the traces, stated). That quantity is the toroidal part,
not the poloidal $I_{\mathrm{halo}}$ of the measures above.

## Modelling

**Boundary conditions.** The halo current is limited by the sheath:
without a boundary condition that caps the current density at the ion
saturation current, large currents are induced in regions of very low
density. With a complete set of sheath conditions, a neutral fluid and
Spitzer resistivity and conduction, JOREK runs give "the first … fully
self-consistent evolution of halo currents"
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6.3). In COMPASS the
ion saturation current governs the poloidal extent of the halo region
([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.1, Fig. 6). See
[sheath boundary conditions](/methods/sheath-boundary-conditions.md).

**Crossing into the wall.** How the code lets current pass from plasma to
conductor determines what "halo current" means numerically.

- In JOREK reduced MHD the boundary condition $\Phi=$ const makes the
  domain boundary a poloidal ideal conductor, so $\mathbf J\cdot\mathbf n=0$
  at the STARWALL wall: halo currents close in the plasma domain, only eddy
  currents flow in the wall, and halo and eddy forces separate cleanly
  ([Artola et al. (2021)](/sources/artola-2021.md), §4.1.6, §4.3.1). JOREK
  treats the source/sink currents in the wall by the Zakharov–Atanasiu
  formalism as a post-processor for wall forces; implicit coupling of the
  wall potential is not implemented ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.9).
  The same boundary condition removes the toroidal asymmetry of $I_p$
  ([reduced-MHD current asymmetry](/results/reduced-mhd-current-asymmetry.md)).
- JOREK–CARIDDI represents the plasma by an equivalent solenoidal surface
  current on the domain boundary, which cannot describe currents crossing
  the boundary; halo currents need plasma-facing electrodes and correction
  terms not yet implemented ([Isernia et al. (2023)](/sources/isernia-2023.md),
  §II.B–C, §VII). Halo coupling is ongoing work
  ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3).
- In M3D-C1 and NIMROD the poloidal electric field at the boundary is
  finite, so current enters and leaves the plasma domain
  ([Artola et al. (2021)](/sources/artola-2021.md), §4.1.6); see
  [resistive-wall coupling](/methods/resistive-wall-coupling.md).
- NIMROD runs of SPARC gas injection give the region between limiter and
  vessel enhanced resistivity (and optionally mass density) through a tanh
  transition, but keep plasma-like parameters in the divertor regions out
  to the domain boundary, so open-field-line (halo) currents can reach the
  boundary there ([Izzo et al. (2025)](/sources/izzo-2025.md), §III A, C;
  passing remark, no halo-current values given).

**Suppression in idealized runs.** In the ITER runaway-electron VDE
benchmark, halo currents are deliberately suppressed during the artificial
cooling by raising the parallel conductivity, which avoids SOL energy
accumulation and keeps the SOL resistivity high
([Bandaru et al. (2024)](/sources/bandaru-2024.md), §IV.A). The paper
states that the halo current "can be seen to be negligible in all cases"
but also that it drops "to negligible values in the lower vessel
resistivity cases", which implies a non-negligible value at nominal vessel
resistivity late in the VDE (§IV.B, Fig. 9b): an internal tension of the
source.

## Citations

- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.9, §6.2.4, §6.3.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3, §3.1, §3.3.
- [Artola et al. (2021)](/sources/artola-2021.md), §4.1.1, §4.1.5–4.1.6, §4.3.1.
- [Isernia et al. (2023)](/sources/isernia-2023.md), §II, §VII.
- [Bandaru et al. (2024)](/sources/bandaru-2024.md), §IV.
- [Artola et al. (2022)](/sources/artola-2022.md), §4.1–4.2, §4.4, Eq. 8.
- [Vannini et al. (2025)](/sources/vannini-2025.md), §4, Fig. 3.
- [Izzo et al. (2025)](/sources/izzo-2025.md), §III A, C.
