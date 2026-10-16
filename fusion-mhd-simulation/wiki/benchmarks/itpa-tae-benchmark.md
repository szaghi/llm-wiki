---
type: Benchmark
title: "ITPA n = 6 TAE benchmark"
description: "Linear multi-code benchmark of an n = 6 toroidal Alfvén eigenmode driven by Maxwellian energetic deuterons in a large-aspect-ratio circular tokamak (Könies et al. 2018), scanned in energetic-particle temperature; JOREK, M3D-C1-K and GMEC each report agreement, with JOREK's growth rates at the low edge and its frequencies below all other codes."
status: established
aliases: [ITPA-TAE, ITPA TAE benchmark, Könies TAE benchmark]
tags: [benchmark, verification, alfven-eigenmode, energetic-particles, hybrid-kinetic]
timestamp: 2026-10-16T00:00:00Z
---

# ITPA n = 6 TAE benchmark

The ITPA TAE benchmark is a linear test of the energetic-particle (EP) drive
of an $n=6$ [TAE](/definitions/toroidal-alfven-eigenmode.md). The case is
defined in Könies et al. (2018), with the setup traced to Könies (2008). The
original paper is not ingested; the case is known here through three hybrid
codes that ran it ([Bogaarts et al. (2022)](/sources/bogaarts-2022.md),
§IV.A; [Liu et al. (2022)](/sources/liu-2022.md), §6.2;
[Liu et al. (2024)](/sources/liu-2024.md), §III C;
[Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §7.2).

## Setup

| item | value | source |
|---|---|---|
| geometry | circular, $R_0=10$ m, $a=1$ m, $B=3$ T | all three |
| bulk plasma | hydrogen, flat $n_i=2\times10^{19}$ m$^{-3}$ | all three |
| safety factor | $q=1.71+0.16(r/a)^2$; $q=1.75$ at $r=0.5a$ | all three |
| bulk pressure | flat, $p=6408$ Pa | [Liu et al. (2022)](/sources/liu-2022.md), §6.2 |
| bulk pressure | $p=7.17\times10^3-6.811\times10^3\psi_{t,N}-3.585\times10^2\psi_{t,N}^2$ Pa | [Liu et al. (2024)](/sources/liu-2024.md), §III C |
| EPs | deuterium, Maxwellian at uniform $T_h$, scanned over 100–800 keV | [Liu et al. (2024)](/sources/liu-2024.md) |
| EP density | $n_h=n_{h0}c_3\exp[-(c_2/c_1)\tanh((\sqrt{\psi_{t,N}}-c_0)/c_2)]$, with $c_0=0.49123$, $c_1=0.298228$, $c_2=0.198739$, $c_3=0.521298$ | [Liu et al. (2022)](/sources/liu-2022.md), Eq. 30; [Liu et al. (2024)](/sources/liu-2024.md) |
| target mode | $n=6$, dominated by $m=10,11$ near $r\approx0.5a$ | all three |

The two Liu papers differ on two inputs:

- **Bulk pressure.** Liu et al. (2022) use a flat profile and Liu et al.
  (2024) a profile.
- **EP density normalization.** Liu et al. (2022) print
  $n_{h0}=1.4431\times10^{17}$ m$^{-3}$ and Liu et al. (2024)
  $1.44131\times10^{17}$ m$^{-3}$.

Neither paper comments on the difference. The second is a printed-digit
discrepancy of 0.1%, below any effect on the results.

## Code runs

- **JOREK** ([Bogaarts et al. (2022)](/sources/bogaarts-2022.md), §IV.A):
  - *Model.* Full MHD with anisotropic CGL pressure coupling and full-$f$,
    full-orbit EPs, so FLR is intrinsic. The run uses 102 × 128 elements,
    $4\times10^7$ markers, an MHD step of $3\tau_A$ and a particle step of
    $2\times10^{-10}$ s.
  - *Convergence.* The growth rate at $T_h=700$ keV is converged within 5%
    over $2\times10^7$–$2\times10^8$ markers and 50–200 particle steps per
    gyro-orbit (Fig. 2).
  - *Earlier runs.* JOREK had run the case before in reduced MHD with
    isotropic pressure coupling and $10^8$ particles. In that earlier run
    JOREK was "the only code in this benchmark using full orbit fast ions"
    ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §7.2, Fig. 68).
- **M3D-C1-K** ([Liu et al. (2022)](/sources/liu-2022.md), §6.2, Fig. 5):
  δf with zero-Larmor-radius (ZLR) or 4-point-gyroaverage (FLR) EPs, and with
  pressure or current coupling. The two couplings give "equal" results.
- **GMEC** ([Liu et al. (2024)](/sources/liu-2024.md), §III C, Figs. 12–14):
  - *Model.* Reduced MHD with gyrokinetic δf EPs, ZLR and FLR, on a VMEC
    equilibrium.
  - *At $T_h=400$ keV (ZLR).* $\omega\tau_A=0.279350$ and
    $\gamma\tau_A=0.026743$ ($\tau_A=R_0/v_A$ on axis), with $m=10,11$
    dominant at $\sqrt{\psi_{t,N}}\approx0.5$.
  - *Saturation.* The run saturates after $550\tau_A$ "due to particle
    nonlinearity".
  - *Comparison data.* The other-code curves in Fig. 14 are copied from
    Fig. 5 of Liu et al. (2022), not taken from Könies et al. (2018).

## Results (values read off the figures)

| code | $\gamma$ peak [$10^3$ s$^{-1}$] | $\omega$ [$10^5$ rad/s] | source |
|---|---|---|---|
| JOREK (full orbit) | ≈ 19, near 400 keV | ≈ 3.9–4.08, lowest of all codes | [Bogaarts et al. (2022)](/sources/bogaarts-2022.md), Fig. 3 |
| M3D-C1-K, ZLR | ≈ 42–43, at 400–600 keV | slightly above the FLR curve | [Liu et al. (2022)](/sources/liu-2022.md), Fig. 5 |
| M3D-C1-K, FLR | ≈ 22, near 400 keV | ≈ 4.0–4.25 | [Liu et al. (2022)](/sources/liu-2022.md), Fig. 5 |
| GMEC, ZLR | ≈ 40, near 500–600 keV | close to MEGA | [Liu et al. (2024)](/sources/liu-2024.md), Fig. 14 |
| GMEC, FLR | ≈ 22 | "reasonably close" to MEGA | [Liu et al. (2024)](/sources/liu-2024.md), Fig. 14 |

FLR roughly halves the peak growth rate and lowers the frequency slightly
in both M3D-C1-K and GMEC. In JOREK the dominant resonance is at
$v_{\parallel p}=v_A/3$, in agreement with Könies et al. (2018). At
nonlinear saturation ($T_h=400$ keV, with $n=0$ held fixed) the
resonant-particle density flattens around $r=0.5a$
([Bogaarts et al. (2022)](/sources/bogaarts-2022.md), Figs. 5–6).

## Code-to-code spread

Each paper characterises its agreement differently:

- **JOREK.** Bogaarts et al. (2022, §IV.A, Fig. 3) report "reasonable
  agreement" with the codes that include FLR: CAS3D-K, TAEFL, GYGLES,
  CKA-EUTERPE, MEGA, NOVA-K, LIGKA, EUTERPE, ORB5 and VENUS.
  - Read off Fig. 3, JOREK's $\gamma$ lies at the lower edge of the band for
    $T_h\gtrsim200$ keV: about 15–19 against 18–28 $\times10^3$ s$^{-1}$.
  - Its $\omega$, about 3.9–4.08 $\times10^5$ rad/s, is below every other
    code plotted (about 4.0–4.45).
  - The authors give a reason that blocks a one-to-one comparison. JOREK's
    full-$f$ Maxwellian relaxes, while the other codes switch relaxation off.
    See the [δf method](/methods/delta-f-method.md).
  - [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) (§7.2) summarize the
    earlier JOREK runs as "a good agreement".
- **M3D-C1-K.** Liu et al. (2022, §6.2) report results "close to" the
  gyrokinetic, hybrid and eigenvalue codes. Read off Fig. 5, the ZLR peak
  sits mid-pack, in an inter-code range of about 33–51 $\times10^3$ s$^{-1}$.
  The FLR frequency lies on the lower branch with LIGKA, MEGA and the ORB5
  FLR variant, below GYGLES and HMGC.
- **GMEC.** Liu et al. (2024, §III C) report growth rates close to the other
  codes and to M3D-C1-K.

## Contradictions

None as a source-versus-source disagreement on the same claim. The JOREK
frequency offset is a code-to-code spread. Bogaarts et al. call the
agreement "reasonable", the curves show it, and the paper gives a stated
reason (relaxation of the full-$f$ distribution). Settling the offset needs a
JOREK run with a distribution that is a function of the constants of motion,
or δf codes run without suppressing the relaxation term.

# Citations

- [Bogaarts et al. (2022)](/sources/bogaarts-2022.md): JOREK full-MHD full-orbit runs, convergence, relaxation, spread.
- [Liu et al. (2022)](/sources/liu-2022.md): M3D-C1-K ZLR and FLR runs, setup parameters, the two couplings.
- [Liu et al. (2024)](/sources/liu-2024.md): GMEC runs and setup parameters.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md): earlier JOREK reduced-MHD runs, the only full-orbit code.
