---
type: Definition
title: "Runaway-electron wall loads and sacrificial limiters"
description: "The energy that a terminating runaway-electron beam deposits on plasma-facing components, estimated in MHD workflows by seeding guiding-centre test markers from the fluid runaway density, giving them the magnetic energy converted to the beam and tracing them through the stored 3D fields of the termination; sacrificial limiters shrink the wetted first-wall area but concentrate the load on themselves."
status: established
aliases: [RE wall loads, runaway beam deposition, sacrificial limiter, upper limiter, RE heat load]
tags: [runaway-electrons, disruption, wall, particles, mhd]
timestamp: 2026-10-16T16:51:00Z
---

# Runaway-electron wall loads and sacrificial limiters

When a [runaway-electron](/definitions/runaway-electrons.md) beam is lost to
the wall, its energy, of order tens of MJ in a reactor, is deposited on
whatever plasma-facing surface the lost field lines reach. The wall load is
the deposited energy per unit area and its distribution over the surface.
**Sacrificial limiters** are "discrete plasma-facing components that aim to
absorb most of the load to protect the first wall … in the event of a
catastrophic failure" ([Vannini et al. (2025)](/sources/vannini-2025.md),
§1, after Barrett et al. 2019).

Symbols (registry §11): $W_{\mathrm{RE}}$ the energy channelled to the
runaways, $N_{\mathrm{RE}}$ the total runaway number.

## Fluid-to-marker workflow

Fluid runaway models carry a density but no energy or pitch
([RE fluid model](/methods/runaway-electron-fluid-model.md)), so the load
cannot be read off the MHD run. [Vannini et al. (2025)](/sources/vannini-2025.md)
(§6) close the gap in post-processing:

1. **Energy.** The kinetic energy given to the markers is the magnetic
   energy transferred to the runaways during beam formation,
   $$W_{\mathrm{RE}}=\int\!\!\int J_{\mathrm{RE},\parallel}\,\big(E_\parallel-E_c^{\mathrm{eff}}\big)\,dV\,dt$$
   (Eq. 3; the time limits are not stated). In the EU-DEMO case
   $W_{\mathrm{RE}}\approx35$ MJ.
2. **Seeding.** Marker positions are sampled from $n_{\mathrm{RE}}$ at the
   peak of the runaway current. The weights are equal and sum to
   $N_{\mathrm{RE}}=1.24\times10^{19}$; every marker carries the same energy,
   17.6 MeV, at pitch $\xi=-0.99$ (the compiler checked
   $35\ \mathrm{MJ}/1.24\times10^{19}=17.6$ MeV). The authors call the
   mono-energetic choice a simplification forced by the fluid model.
3. **Tracing.** The JOREK relativistic guiding-centre equations are
   integrated by RK4 through the stored time history of the 3D termination
   fields, as test particles without back-reaction
   ([particle pushers](/methods/particle-pushers.md)). A full-$f$
   particle-in-cell treatment with feedback is the contrast case.
4. **Deposition.** Energy is deposited where a marker crosses the
   triangulated first wall; markers still confined when the beam starts to
   reform are stopped.

The minimum-load curve (the area receiving at least a given energy per
area) is converged in marker number: $10^5$, $10^6$ and $10^7$ markers
overlap (Fig. 13a). It depends moderately on toroidal resolution: $n\le3$
gives a peak of about $1.5\times10^7$ J/m² over a smaller area, against
about $6.5\times10^6$ J/m² for $n\le7$, with $n\le5$ in between
(Fig. 13b, read from the plot).

## EU-DEMO upper limiters

The case is an upward mitigated hot
[VDE](/definitions/vertical-displacement-event.md) of EU-DEMO in which a
13 MA beam forms in 2D and is terminated in 3D by MHD at $q_{95}\approx2.3$,
$I_{\mathrm{RE}}$ falling from 12.3 to 2.8 MA in 1.12 ms
([Vannini et al. (2025)](/sources/vannini-2025.md), §5). Lost markers reach
the upper wall at poloidal angles of about 65°–110° from the magnetic
axis. The design has 8 upper limiters, each about 11.25° wide toroidally,
every 45°, protruding 70 mm from the axisymmetric first wall; variants with
4 × 45°, 8 × 22.5° and 8 × 11.25° were placed at the designed ("current")
and at a shifted ("moved") poloidal position (§6).

| Configuration | first-wall peak (J/m²) | limiter peak (J/m²) | wetted first-wall area (m²) |
|---|---|---|---|
| no limiters | ≈6.5×10⁶ | — | ≈68 |
| current limiters | ≈5–6×10⁶ | ≈5.5×10⁷ | 29–43 |
| moved limiters | ≈4.5–5.5×10⁶ | ≈1–2×10⁸ | 6–16 |

(Figs. 11–12, read from the plots.) Findings:

- **Designed positions miss.** With the limiters where designed, "the
  majority of REs do not hit the ULs": the limiters were positioned for
  charged-particle loads in the thermal quench of a different scenario, and
  the runaway loads are estimated "for the first time" here (§6). The moved
  positions are "purely an exercise", not a design proposal.
- **Shielding against concentration.** Limiters cut the wetted first-wall
  area and slightly lower its peak, but the load on the limiters rises
  sharply. The conclusion says "almost 1 order of magnitude higher than that
  onto the FW in absence of ULs" (§7); the table gives about 8.5× for the
  current and 15–30× for the moved limiters, so the phrase understates the
  moved cases (recorded on the Source page).
- **Toroidal hot spots.** Deposition concentrates on one toroidal side of
  each limiter block (§6, Fig. 10c–d).
- **Lower bounds.** A detailed CAD wall would increase localization and the
  load per area further, as Bergström et al. (2024, cited) show for ITER;
  the energy of the beam that reforms after the first loss is not included
  (§7).

## Other termination footprints

- **DIII-D, M3D-C1.** In the final loss of a DIII-D plateau, more than 95%
  of the runaways reach the lower high-field-side wall within about 0.06 ms,
  with a single toroidal peak ($n=1$ footprint), "similar to the results of
  RE loss simulation in JET using JOREK"
  ([Liu et al. (2021)](/sources/liu-2021.md), §5.3, Fig. 13). The loss
  fraction converges only with at least 16 toroidal planes (Fig. 14a).
- **Benign termination in experiments.** After massive deuterium injection
  into the plateau in JET and DIII-D the wall load is broad enough that no
  appreciable localized heat load is seen
  ([McDevitt & Tang (2023)](/sources/mcdevitt-2023.md), p. 1, attributing
  this to the experiments). The beam-termination physics is on
  [runaway reconstitution after an MHD flush](/results/runaway-reconstitution-after-mhd-flush.md).

## Limits of the method

The marker energy is a single value set by an energy balance, not a
spectrum; the markers do not act back on the fields; the wall is
axisymmetric in the DEMO case; and only the first loss is followed
([Vannini et al. (2025)](/sources/vannini-2025.md), §6–7). The deposited
fraction of the 35 MJ is not given as a number.

## Citations

- [Vannini et al. (2025)](/sources/vannini-2025.md), §1, §5–7, Eq. 3, Figs. 10–13.
- [Liu et al. (2021)](/sources/liu-2021.md), §5.3, Figs. 13–14.
- [McDevitt & Tang (2023)](/sources/mcdevitt-2023.md), p. 1.
