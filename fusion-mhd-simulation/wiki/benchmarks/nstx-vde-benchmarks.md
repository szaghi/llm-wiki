---
type: Benchmark
title: "NSTX VDE benchmarks of JOREK, M3D-C1 and NIMROD (axisymmetric and 3D)"
description: "Code-to-code benchmark of a vertical displacement event of an NSTX plasma in a rectangular resistive wall: an axisymmetric case (Krebs et al. 2020) and its 3D continuation, a hot VDE in which low-n external kinks drive a thermal quench and sideways wall forces; the codes agree on kink onset, thermal-quench duration and vertical force and differ on the toroidal asymmetry of the plasma current."
status: established
aliases: [NSTX VDE benchmark, 3D VDE benchmark, Krebs 2020 VDE benchmark]
tags: [benchmark, verification, vde, disruption, wall, free-boundary]
timestamp: 2026-10-16T23:59:30Z
---

# NSTX VDE benchmarks of JOREK, M3D-C1 and NIMROD (axisymmetric and 3D)

The benchmark compares three nonlinear codes with very different
models and wall treatments on one
[VDE](/definitions/vertical-displacement-event.md):
[JOREK](/software/jorek.md) (ansatz-based [reduced MHD](/methods/reduced-mhd.md),
thin wall via [STARWALL](/software/starwall.md), un-meshed vacuum),
[M3D-C1](/software/m3d-c1.md) (full single-fluid MHD, thick wall, meshed
vacuum) and [NIMROD](/software/nimrod.md) (full MHD, thin wall, meshed
vacuum) ([Artola et al. (2021)](/sources/artola-2021.md), Table 1; wall
models on [resistive-wall coupling](/methods/resistive-wall-coupling.md)).
It has two stages.

## Axisymmetric stage (Krebs et al. 2020)

The parent benchmark, Krebs et al. 2020 (Phys. Plasmas 27:022505, not
ingested), is an NSTX-like axisymmetric VDE. As summarized by
[Hoelzl et al. (2021)](/sources/hoelzl-2021.md) (§4.8, Fig. 26b), the three
codes show excellent agreement on the growth rate, the motion of the
magnetic axis, the plasma and wall currents and the spatial structure of
the halo current. [Artola et al. (2021)](/sources/artola-2021.md) (§4.1.1)
report that the 2D phase of the 3D benchmark agrees as well as this case,
and that each code's time axis must be shifted to synchronize the onset,
because different numerical perturbations start the VDE at different times
even when the growth rates agree.

## 3D stage (Artola et al. 2021)

**Equilibrium.** NSTX discharge 139536 at 309 ms (EFIT):
$I_p=5.74\times10^5$ A, $\beta_N=3.83\%$, $\beta_p=0.532$, $l_i(3)=0.698$,
$q_0=2.04$, $q_{95}=7.32$, plasma volume 11.9 m³, magnetic axis at $R_0=1.07$ m,
$W_{\mathrm{th}}=7.61\times10^4$ J; temperature
$T_e=T_i=946\,\mathrm{eV}\,(p/p_{\mathrm{axis}})^{0.6}$; the equilibrium file
and coil data are supplementary material
([Artola et al. (2021)](/sources/artola-2021.md), §3, Fig. 1).

**Wall.** Rectangle with corners at $R=0.24$ and $1.6$ m, $Z=\pm1.4$ m,
$d_w=0.015$ m, $\eta_w=3\times10^{-5}$ Ω m (thin-wall codes use $\eta_w/d_w$).

**Physics parameters (Table 2).** No loop voltage, Ohmic heating, radiation
or sources; deuterium, $T_e/T_i=1$; resistivity ten times Spitzer; viscosity
$5.16\times10^{-7}$ kg m$^{-1}$ s$^{-1}$. The 2D phase uses
$D_\perp=D_\parallel=1.54$ m²/s and $\kappa_\perp=10^{-5}\kappa_\parallel$;
the 3D phase raises the diffusivities ($D=40$ m²/s, $\kappa$ by ≈150) to
avoid high-$n$ edge modes, since the target is low-$n$ wall forces.
Dirichlet $\rho$ and $T$ at the wall ($T_e=14.6$ eV,
$n_e=2.2\times10^{18}$ m$^{-3}$); $\mathbf v=0$ in M3D-C1 and NIMROD,
$\mathbf v\cdot\mathbf n=0$, $v_\parallel=0$ and zero toroidal vorticity in JOREK.

**Phases.** (i) 2D drift: the plasma moves down by ≈1 m in ≈10 ms until it is
limited by the lower wall, typical of experiments (5–20 ms). (ii) 3D phase
from the instant of limitation ($t'=0$).

**Resolution.** JOREK: 22000 Bézier elements, 48000 wall triangles,
$n=0\dots10$. M3D-C1: 17424 vertices per plane, 16 toroidal Hermite
elements. NIMROD: 39000 bicubic elements, $n=0\dots10$, the most dynamic
interval repeated with $n=0\dots21$ (§3).

### Figures of merit and results

| Quantity | JOREK | M3D-C1 | NIMROD |
|---|---|---|---|
| Onset of 3D instability after limitation | 0.85–1.10 ms (all) | | |
| Dominant mode | $n=1$ | $n=1$ ($n=3$ transiently larger) | $n=1$ |
| TQ duration | 0.14 ms | 0.24 ms | 0.20 ms |
| Peak $\lvert F_{w,z}\rvert$ (fig.) | ≈28 kN | ≈28 kN | ≈29 kN |
| Peak $F_{w,h}$ (fig.) | ≈3.4 kN | ≈2.8 kN | ≈2.5 kN |
| Force rotation | some, between $n=1$ peaks | some | none |
| $\Delta I_p/I_p$ | <0.01% | 1–1.4% | 3–4% |
| Toroidal halo current (fig.) | ≈0.4 MA | ≈0.35 MA | not post-processed |

Values marked (fig.) are read from Figs. 2 and 8 of
[Artola et al. (2021)](/sources/artola-2021.md); the others are stated in
§4.1.2–4.1.6. Additional findings (same source):

- Kinks grow when the $q=2$ surface enters the open-field region
  ($q_{95}\approx2$), as 2/1, 4/2, 6/3 external kinks satisfying
  $0<nq_a<m$ (§4.1.2, Eq. 7); see
  [vertical displacement event](/definitions/vertical-displacement-event.md).
- The [thermal quench](/definitions/thermal-quench.md) times agree with the
  ≈0.2 ms of NSTX disruptions (§4.1.3).
- The vertical force is in "excellent agreement"; the horizontal force
  peaks at 2.5–3.5 kN and rotates less than one toroidal turn (§4.1.4, §5;
  [wall forces](/definitions/wall-forces.md)).
- Doubling the toroidal resolution in JOREK and NIMROD leaves $I_p$,
  $W_{\mathrm{th}}$ and the forces nearly unchanged (§4.2, Fig. 11).
- JOREK-only studies decompose the forces into halo and eddy parts (peak
  forces are halo-driven) and scan $\kappa_\parallel$ and viscosity (§4.3).
- The ansatz-based reduced model of JOREK captures the 3D dynamics and wall
  currents "even in the spherical tokamak limit", in contrast to
  reduced models ordered in the aspect ratio (Abstract, §5), with the
  exception of the $I_p$ asymmetry
  ([reduced-MHD current asymmetry](/results/reduced-mhd-current-asymmetry.md)).

Unexplained spreads visible in the figures but not discussed by the source:
the M3D-C1 growth and saturation of $n\ge1$ lag JOREK and NIMROD by
≈0.1–0.2 ms, and the peak $n=1$ magnetic energy differs by a factor ≈2.5
(≈0.2 kJ JOREK, ≈0.37 kJ M3D-C1, ≈0.53 kJ NIMROD; Figs. 3, 5, 8).
The benchmark is used in later JOREK work as the reference 3D VDE
verification of JOREK–STARWALL ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.1).
[Artola et al. (2022)](/sources/artola-2022.md) (§2) rest the validity of
JOREK's reduced model for ITER current-quench wall forces on this
benchmark and its axisymmetric parent.

## Contradictions

**Sideways-force agreement — Open; kept Open by human decision
(2026-10-16).** [Artola et al. (2021)](/sources/artola-2021.md)
(§4.1.4, §5) call the horizontal-force agreement "good … in magnitude" with
maxima of 2.5–3.5 kN; [Hoelzl et al. (2021)](/sources/hoelzl-2021.md)
(§4.8) describe the same benchmark as "reasonable quantitative agreement
with NIMROD showing a factor two smaller force than the other two codes".
The Fig. 8 readings (≈3.4, ≈2.8, ≈2.5 kN) give NIMROD ≈0.74 of JOREK, not
0.5. Tabulated per-code peak values from the published benchmark would
settle it. Recorded also on [wall forces](/definitions/wall-forces.md).

**$I_p$ toroidal asymmetry — Open.** <0.01% (JOREK), 1–1.4% (M3D-C1),
3–4% (NIMROD), against 10–20% in experiments
([Artola et al. (2021)](/sources/artola-2021.md), §4.1.6;
[Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §4.8, pooled as 1–4%). The
JOREK value is explained by its boundary condition; the factor ≈3 between
the full-MHD codes and the gap to experiment are not. Details and the
settling test on [reduced-MHD current asymmetry](/results/reduced-mhd-current-asymmetry.md).

## Citations

- [Artola et al. (2021)](/sources/artola-2021.md), §1–5, Tables 1–2, Figs. 1–13.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §4.8, Figs. 26b, 28–29.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.1.
- [Artola et al. (2022)](/sources/artola-2022.md), §2.
