---
type: Software
title: "MARS-F"
description: "Linear resistive MHD plasma-response and stability code used as the linear reference of nonlinear codes: it optimizes RMP coil phasing by the X-point displacement criterion, matches JOREK's early-phase displacement in ITER, and supplies the linear (2,1) resistive-kink structure against which M3D-C1 runaway-electron runs are checked; it handles 3D active coils but only thin, axisymmetric passive conductors."
status: established
aliases: [MARS F, MARS-F code]
tags: [code, mhd, tokamak, verification, elm, free-boundary, wall, kink]
timestamp: 2026-10-16T12:00:00Z
---

# MARS-F

MARS-F is a linear MHD code for the response of a toroidal plasma to
external fields and for its linear stability. The sources of this bundle
describe it as "linear resistive MHD" plasma-response code
([Becoulet et al. (2022)](/sources/becoulet-2022.md), §1–2) and use it in
three roles: optimizing the phasing of resonant-magnetic-perturbation coils,
supplying linear mode structures against which nonlinear codes are
compared, and as a benchmark partner of [CLT](/software/clt.md). None of
the sources describes its equations, discretization or time scheme. Its
relation to the MARS eigenvalue code, from which
[HYMAGYC](/software/hymagyc.md) derives (see
[linear MHD eigenvalue codes](/methods/linear-mhd-eigenvalue-codes.md)), is
not stated in these sources.

## Uses in the cited sources

**RMP coil phasing for ITER.** For each ITER scenario and toroidal mode
number, the relative phases of the upper, middle and lower rows of the
$3\times9$ in-vessel coils are set to the MARS-F optimum, the phasing that
maximizes the linear-response normal displacement near the X-point at
$\psi_N\approx0.99$; the phases are converted to the ERGOS angle convention
and the ERGOS vacuum field is then imposed on JOREK. ERGOS and MARS-F were
benchmarked in vacuum (not shown) ([Becoulet et al. (2022)](/sources/becoulet-2022.md),
§2, Table 1). The underlying criterion, that the linear-response X-point
displacement predicts ELM suppression better than vacuum island overlap, is
attributed to Liu et al. (2016) (§1, §6); see
[resonant magnetic perturbations](/definitions/resonant-magnetic-perturbation.md).

**Linear against nonlinear displacement.** In the ITER 12.5 MA case MARS-F
gives about 7 mm at 60 kAt with optimum phasing, and the same displacement
at about 80 kAt with non-optimum phasing, by linear scaling of a 30 kAt
computation. [JOREK](/software/jorek.md) gives about 6 and 8 mm in its early
single-harmonic phase, "very similar", and about 60 mm once nonlinear
coupling sets in, which is stated without a figure (Becoulet et al. 2022,
§6, Figs. 17–18).

**Linear reference for the runaway-electron kink.**
[Liu et al. (2021)](/sources/liu-2021.md) compare the linear $(2,1)$
resistive kink of their [M3D-C1](/software/m3d-c1.md) runaway-electron model
in DIII-D shot 177040 with MARS-F results (Liu Y.Q. et al. 2019, as cited):
the dominance of $m=2$ and the localization of the normal displacement at
$q=2$ are "in agreement" (§5.2, Figs. 7–8), and §6 speaks of good agreement
"including the growth rate and mode structure". No MARS-F curve or number
is shown, so the growth-rate agreement is stated, not shown.

**Benchmark partner of CLT.** CLT was benchmarked against MARS-F on the
linear plasma response to RMPs before the CLT–M3D-C1 benchmark
([Zhang et al. (2021)](/sources/zhang-2021.md), §2; no numbers given).

## Conductors

MARS-F treats 3D active coils but only axisymmetric passive structures, and
only as thin conductors, like CASTOR3D and VALEN
([Isernia et al. (2023)](/sources/isernia-2023.md), §I); see
[resistive-wall coupling](/methods/resistive-wall-coupling.md).

## Limitations

- Linear: it cannot follow the nonlinear multi-harmonic phase, where the
  ITER X-point displacement grows about tenfold beyond the linear value
  (Becoulet et al. 2022, §6).
- The sources give no quantitative MARS-F result that a reader can check
  against a figure, apart from the 7 mm displacement.

## Contradictions

None open.

# Citations

- [Becoulet et al. (2022)](/sources/becoulet-2022.md) — §1, §2, §6, Table 1, Figs. 17–18.
- [Liu et al. (2021)](/sources/liu-2021.md) — §1, §5.2, §6, Figs. 7–8.
- [Zhang et al. (2021)](/sources/zhang-2021.md) — §2.
- [Isernia et al. (2023)](/sources/isernia-2023.md) — §I.
