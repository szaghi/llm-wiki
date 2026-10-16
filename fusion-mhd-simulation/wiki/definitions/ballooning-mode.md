---
type: Definition
title: "Ballooning mode"
description: "Pressure-driven, high-n MHD instability localized on the outboard (bad-curvature) side of flux surfaces, whose ideal growth rate rises with n without bound in the absence of stabilizing flows, with its resistive and peeling-ballooning variants in tokamak pedestals; the standard linear verification case of edge and stellarator MHD codes."
status: established
aliases: [ideal ballooning mode, IBM, resistive ballooning mode, drift-ballooning mode, peeling-ballooning mode]
tags: [ballooning, mhd, pedestal, edge, verification, stellarator, tokamak]
timestamp: 2026-10-16T12:00:00Z
---

# Ballooning mode

A ballooning mode is a pressure-driven MHD instability with high toroidal
mode number $n$. It is elongated along $\mathbf B$ and narrow across it, and
its amplitude peaks on the outboard side of the flux surfaces, where the
field-line curvature is unfavourable. A ballooning eigenfunction is a
superposition of many poloidal harmonics, each peaking at its own rational
surface $q=m/n$. In the $n=20$ ideal ballooning mode (IBM) of
[Jiang et al. (2024)](/sources/jiang-2024.md) (§IX A, Fig. 17) the harmonics
run from $m=64$ to $m=103$. In the $n=20$ IBM of
[Seto et al. (2023)](/sources/seto-2023.md) (§4, Fig. 4) they run from $m=33$
to $m=51$, around a resonant $q=41/20$. In the second case the mode is even in
radius about the peak of the pressure gradient and even about the outboard
midplane.

**Unbounded growth with $n$.** Without equilibrium flows, the ideal growth
rate increases monotonically with $n$ and diverges as $n\to\infty$.
[Nikulsin et al. (2022)](/sources/nikulsin-2022.md) (§VII) state this from
tokamak theory and check it in W7-A: runs that included $n=15$ and $n=20$
still had the highest-$n$ mode growing fastest. Diamagnetic drifts are the
usual cut-off.

- In the drift-ballooning model of Jiang et al. (2024, §IX B, Fig. 23), ion
  and electron diamagnetic terms give the mode a real frequency $\omega$
  that rises almost linearly with $n$. They stabilize high $n$: $\gamma$
  peaks near $n\approx6$, at about $0.083\,v_A/R_0$, and falls to about
  $0.02\,v_A/R_0$ by $n=16$.
- In the four-field two-fluid drift-wave resistive ballooning model (DWRBM)
  of Seto et al. (2023, §5.1, Fig. 5b), the cbm18_dens4 spectrum peaks at
  $n=32$, with $\gamma\tau_A=7.86\times10^{-2}$. Modes with $n\le10$ and
  $n\ge53$ are stable.

**Second stability.** At fixed $n$, the ideal growth rate is non-monotonic in
the pressure. In the Jiang et al. (2024, §IX A, Fig. 18) scan from 0.4% to 2%
of the normalized peak pressure (the paper's "$\beta$"), $\gamma$ peaks near
0.7–0.8% and then falls. This is the access to the second stability region.

**Edge relevance.** Coupled to the current-driven peeling mode, the ballooning
mode sets the onset of type-I
[edge-localized modes](/definitions/edge-localized-mode.md)
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §5.1). The
three-field linear peeling–ballooning model of Seto et al. (2023, §4,
Eqs. 21–27) is the minimal set. It contains vorticity, the parallel vector
potential and pressure, with the curvature term as the drive.

## Resistive and peeling–ballooning variants

**Resistivity destabilizes ideally stable pedestals.** The ASDEX Upgrade EDA
H-mode #36330 lies just inside the ideal $n\approx15$ ballooning boundary of
MISHKA, yet at realistic resistivity [JOREK](/software/jorek.md) finds it
unstable to resistive peeling–ballooning modes for $n=5$–11, most strongly
$n=6$–9 ([Cathey et al. (2023)](/sources/cathey-2023.md), §2.1, §3.1, Figs. 2,
5). The growth rate peaks at about $2.7\times10^4$ s$^{-1}$ for $n=7$–8
(figure reading). The mode peaks at $\psi_N=0.983$, almost exactly at the
maximum of $\partial T_e/\partial R$ ($\psi_N=0.980$), not at the maxima of
$\nabla p_e$ (0.977) or $\nabla n_e$ (0.995); its dominant poloidal
harmonics $m=35$–56 are resonant near $q=6$ (§3.2, Fig. 6). Earlier
resistive studies, cited there, move the ballooning boundary to lower
pressure gradients (stated).

**Identification by rotation velocity.** Following Morales et al. (2016, as
cited), the poloidal velocity of an ideal ballooning mode is the
$E\times B$ velocity plus the poloidal projection of the parallel flow plus
half the poloidal ion diamagnetic velocity, while a resistive ballooning
mode moves without the diamagnetic term. The simulated EDA mode moves at
about $-15$ km/s in the laboratory frame (electron diamagnetic direction)
and matches the resistive expression best, which is the basis of the
identification (Cathey et al. 2023, §3.2, Fig. 7). Becoulet et al. (2022,
§3, attributed) name two-fluid diamagnetic effects and toroidal rotation as
the most important factors in the observed rotation of ballooning modes
before ELM crashes ([Becoulet et al. (2022)](/sources/becoulet-2022.md)).

**Resistivity and flows in a JT-60SA pedestal.**
[Cathey et al. (2024)](/sources/cathey-2024.md) (§4, Figs. 8–11) run single-$n$
linear JOREK simulations of the 4.6 MA, 2.26 T scenario 4-1, on top of
established diamagnetic and $E\times B$ flows and a Mach-1 parallel flow
set at the targets. Growth rates in $10^3$ s$^{-1}$, read from the figures:

| $n$ | 1 | 3 | 6 | 9 | 13 | 17 | 21 | 25 | 30 |
|---|---|---|---|---|---|---|---|---|---|
| about $10\eta_{\mathrm{real}}$, with flows | 4 | 13 | 18 | 22 | 25.5 | 26.5 | 20 | 11 | 4 |
| $\eta_{\mathrm{real}}$, with flows | – | 3.3 | 8 | 8 | – | – | – | – | – |
| $\eta_{\mathrm{real}}$, no flows | – | – | – | 8 | 12 | 14 | 16 | 17 | 17 |

Here $\eta_{\mathrm{real}}$ is Spitzer resistivity with neoclassical
corrections at $Z_{\mathrm{eff}}=2.5$. At realistic resistivity only $n=3$
("mostly peeling"), 6 and 9 (coupled peeling–ballooning) are unstable. The
flows stabilize the high-$n$ modes, whose zero-flow growth rate rises
monotonically to $n=30$ (and is up to about four times larger at
$10\eta_{\mathrm{real}}$), in agreement with the unbounded-growth statement
above and with diamagnetic drifts as the cut-off. They also destabilize the
low-$n$ modes: $n=3$ and 6 at realistic resistivity, and $n=1$ at high
resistivity, are unstable only with flows, which the authors attribute to
$E\times B$ shear, after Xu et al. and Chen et al. (2017, as cited).
Without flows the $n=9$ structure is "much more ballooning", with the
high-field side almost unperturbed (Fig. 11). JT-60SA is said to be harder
than AUG because of its size and higher Lundquist number (§4.1, stated).
In the AUG small-ELM and EDA cases, the ideal boundary from MISHKA
overestimates the dominant $n$ because ideal analysis neglects this flow
stabilization (Cathey et al. 2024, §2.3, §3.4, stated).

**Parity in nonlinear peeling–ballooning ELMs.** In NIMROD runs of DIII-D
ELMs, ballooning-parity modes $n=10$–14 localized on the low-field side grow
linearly; the peeling-parity $n=1$ and 2 currents surround the device and
dominate on the high-field side; and the nonlinear $n=12$ current spreads
poloidally well beyond its linear structure
([Ebrahimi & Bhattacharjee (2023)](/sources/ebrahimi-2023.md), p. 2, p. 4,
Figs. 2a, 4).

**Flow shear as a stabilizer.** NIMROD needs the reconstructed pedestal flow
shear to keep peeling–ballooning modes stable in a DIII-D ITER-baseline
equilibrium ([Howell et al. (2022)](/sources/howell-2022.md), §III A,
stated). Ramasamy et al. (2024, §4.5) list the neglected ambipolar
$E\times B$ shear among the limits of their stellarator runs and expect it
to stabilize high-$n$ and worsen low-$n$ modes, by analogy with edge
harmonic oscillations ([Ramasamy et al. (2024)](/sources/ramasamy-2024.md));
the JT-60SA scan above shows that pattern.

**Ballooning modes beside other instabilities.**
- In the circular, weak-shear tokamak equilibria used for $n=3$ infernal
  modes, $n>3$ ballooning modes are also unstable. With drift-kinetic
  thermal ions in MEGA, the $n=18$ ballooning growth rate rises while the
  $n=3$ rate falls until the two are comparable, but $n=18$ saturates lower
  and its effect on $n=3$ "appears to be small"; in MHD the $n=3$ mode
  saturates first ([Sato et al. (2024)](/sources/sato-2024.md), §3.2.2,
  Fig. 14b, qualitative).
- In W7-AS, the low-$n$ MHD activity at intermediate $\beta$ is resistive in
  the JOREK3D simulations: tenfold resistivity destroys confinement, lower
  resistivity confines the activity to the edge, and the dominant $(2,1)$
  mode seen in the experiment appears only at artificially high resistivity
  (Ramasamy et al. 2024, §4.2, §4.4; see [JOREK3D](/software/jorek3d.md)).

## Verification results

| Case | Codes | Agreement | Source |
|---|---|---|---|
| cbm18_dens8, IBM, $n=20$ | BOUT++ 2D and 1D field solvers vs earlier BOUT++ and ELITE | $\gamma\tau_A=0.244$ (2D), 0.246 (1D), 0.245 (BOUT++), 0.239 (ELITE) | Seto et al. (2023), §4, Fig. 3 |
| CBM18, $n=20$ | JOREK reduced and full MHD | growth-rate error converges at 5th order (reduced) and 3rd order (full) | Hoelzl et al. (2021), §4.1, Fig. 14 |
| Circular, aspect ratio 3.3, $q_{95}=3$, resistive | JOREK vs BOUT++ | within 4%, with and without diamagnetic effects | Hoelzl et al. (2021), §4.5, Fig. 21 |
| JET-like X-point peeling–ballooning | JOREK reduced vs full MHD | within 5%, largest gap at high $n$ | Hoelzl et al. (2021), §4.5, Fig. 22 |
| VMEC equilibrium, $R_0=2.763$ m, $a=1$ m, $n=4$–20, pressure scan | GMEC_I vs MAS | $<4\%$ in $\gamma$ | Jiang et al. (2024), §IX A, Fig. 18 |
| Same, with diamagnetic drift, $n=4$–16 | GMEC_I vs MAS | $<1\%$ in $\omega$, $<20\%$ in $\gamma$ | Jiang et al. (2024), §IX B, Fig. 23 |
| W7-A, $\beta=0.11\%$ and $0.21\%$, $n=0,5,10$ | JOREK3D vs CASTOR3D | max 6.4%; the other three cases $<3\%$ | Nikulsin et al. (2022), §VII, Fig. 12 |

The cbm18 case is detailed on
[cbm18 ideal-ballooning benchmark](/benchmarks/cbm18-ballooning-benchmark.md).
Hoelzl et al. (2021, §4.5) also validate the rotation of ballooning modes
against analytic linear theory.

## Numerical requirements specific to ballooning modes

- **Flute ordering of the field solver.** In the field-aligned codes, the
  vorticity–potential inversion is often made one-dimensional by dropping
  parallel derivatives. Seto et al. (2023, §4, Fig. 3) measure the resulting
  error on the IBM: about 1% at $n=20$ and about 36% at $n=5$, with the
  flute-ordered solver higher. They read this as the $O(1/n)$ correction of
  ballooning theory (Connor, Hastie and Taylor). See
  [hybrid 2D/1D field solver](/methods/hybrid-2d-1d-field-solver.md).
- **Twist-shift boundary.** In plain field-aligned coordinates, the integrated
  shear is discontinuous at the twist-shift boundary. This drives a spurious
  instability localized at that boundary, with $\gamma=0.21\,v_A/R_0$ on the
  $n=20$ IBM, against a physical growth rate of $0.087\,v_A/R_0$.
  - Vorticity diffusion suppresses it only when large enough to bias
    $\gamma$ down by 7%.
  - The shifted metric and the "simple shifted metric" remove it without
    bias.

  Source: Jiang et al. (2024), §VIII, Figs. 10–12; see
  [field-aligned coordinates](/methods/field-aligned-coordinates.md).
- **Spectral blocking.** With a truncated toroidal spectrum ($n=0,5,10$),
  the highest retained harmonic is affected. Adding $n=15$ lowers
  JOREK3D's $n=10$ growth rate by 5–6%, while CASTOR3D changes by less than
  0.003%. This accounts for most of the 6.4% gap (Nikulsin et al. 2022, §VII).
- **Reduced MHD.** The finite-$\beta$ failure of ansatz-based
  [reduced MHD](/methods/reduced-mhd.md) concerns the internal kink. Edge
  ballooning modes are largely unaffected. Hoelzl et al. (2021, §2.3.3)
  argue this from a modified Mercier criterion, in which the spurious
  stabilization is negligible when $q\gg1$. See
  [resistive internal kink](/definitions/resistive-internal-kink.md).

## Qualifications

- **Drift-ballooning agreement.** Jiang et al. (2024, §IX B) call the
  GMEC_I–MAS drift-ballooning comparison "agree well" while the $\gamma$
  difference reaches 20%, largest by eye at $n=12$–16. They attribute the
  remaining gaps to MAS neglecting some equilibrium derivatives and using
  Boozer coordinates with FFTs (§IX A). This is a *stated* attribution, not
  a tested one.
- **Systematic offsets.** The JOREK3D growth rates sit systematically above
  CASTOR3D (Nikulsin et al. 2022, Fig. 12). Both BOUT++ solvers sit 2–3%
  above ELITE at $n=20$ (Seto et al. 2023, Fig. 3; the percentages are the
  reader's computation from the printed values).
- **Growth-rate units differ between sources.** Seto et al. normalize by a
  poloidal Alfvén time built on a 3 m reference length and a 2 T reference
  field. Jiang et al. use $v_A/R_0$. Nikulsin et al. and Cathey et al. use
  SI ($\mathrm s^{-1}$).
- **Figure readings.** The JT-60SA and EDA growth rates above are read from
  log or linear plots and carry roughly 10% reading error; Cathey et al.
  (2024) print no numbers and call the resistivities "nominal", "realistic"
  and "anticipated" interchangeably.
- **Single temperature.** The AUG and JT-60SA pedestal runs use $T_e=T_i$
  and no torque source, so the $E	imes B$ and diamagnetic flows that set the
  high-$n$ cut-off are approximate (Cathey et al. 2023, §2.2; 2024, §2.3).

## Contradictions

The low-$n$ overestimate of flute-ordered BOUT++ relative to ELITE and GATO is
recorded on the [cbm18 benchmark page](/benchmarks/cbm18-ballooning-benchmark.md).

# Citations

- [Seto et al. (2023)](/sources/seto-2023.md) — §4, §5.1, Figs. 3–5, Eqs. 21–35.
- [Jiang et al. (2024)](/sources/jiang-2024.md) — §VIII, §IX A–B, Figs. 10–23.
- [Nikulsin et al. (2022)](/sources/nikulsin-2022.md) — §VII, Fig. 12.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — §2.3.3, §4.1, §4.5, §5.1.
- [Cathey et al. (2023)](/sources/cathey-2023.md) — §2.1, §3, Figs. 2, 5–7.
- [Cathey et al. (2024)](/sources/cathey-2024.md) — §2.3, §3.4, §4, Figs. 8–11.
- [Ebrahimi & Bhattacharjee (2023)](/sources/ebrahimi-2023.md) — pp. 2–4, Figs. 2a, 4.
- [Becoulet et al. (2022)](/sources/becoulet-2022.md) — §3.
- [Howell et al. (2022)](/sources/howell-2022.md) — §III A.
- [Ramasamy et al. (2024)](/sources/ramasamy-2024.md) — §4.2, §4.4, §4.5.
- [Sato et al. (2024)](/sources/sato-2024.md) — §3.2.2, Fig. 14b.
