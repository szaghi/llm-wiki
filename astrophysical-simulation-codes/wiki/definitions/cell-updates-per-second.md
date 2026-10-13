---
type: Definition
title: "Cell-update throughput"
description: "The throughput metric of grid codes — cells advanced by one full time step per wall-clock second (cell updates, zone-cycles), or its inverse, the grind time — whose value depends on what counts as one update and on the normalization (per core, socket, GPU, GCD or node), precision, scheme and problem size, which the sources state unevenly."
status: established
aliases: [cell updates per second, zone-cycles per second, zone updates per second, Mzone-cycles/s, Mzcps, cell-updates-per-device-second, grind time, time per point per iteration]
tags: [performance, gpu, benchmark]
timestamp: 2026-10-12T00:00:00Z
---

# Cell-update throughput

**Cell-update throughput** is the number of cells advanced by one time step
per second of wall-clock time: the number of cells times the number of steps,
divided by the elapsed time, optionally divided by the number of hardware
units. The sources name it "cell updates per second"
([Stone et al. (2008)](/sources/stone-2008.md), §7;
[Zhang et al. (2018)](/sources/zhang-2018.md), §5.2;
[Caddy & Schneider (2024)](/sources/caddy-2024.md), §3.2), "zone-cycles per
second" ([Stone et al. (2020)](/sources/stone-2020.md), §3.6;
[Shankar et al. (2023)](/sources/shankar-2023.md), §V A),
"cell-updates-per-device-second" ([Stone et al. (2026)](/sources/stone-2026.md),
§5.1), "Mzones/GPU/s" ([Wibking & Krumholz (2022)](/sources/wibking-2022.md),
§4) or "cells updated per second per node"
([Rossazza et al. (2026)](/sources/rossazza-2026.md), §4.1). Its inverse, time
per cell per step, is the **grind time**.

Two definitions are printed explicitly:
* GRaM-X: zone-cycles per second = iterations × cells / wall time, per GPU
  divided by the number of GPUs; "a single zone-cycle ... includes all
  intermediate steps for RK2/RK4", so one update is one full multistage step
  ([Shankar et al. (2023)](/sources/shankar-2023.md), §V A).
* gPLUTO: grid points × time steps / (execution time × nodes)
  ([Rossazza et al. (2026)](/sources/rossazza-2026.md), §4.1). Quokka divides
  total cell updates by GPUs and wall seconds
  ([Wibking & Krumholz (2022)](/sources/wibking-2022.md), §4).

The other sources do not say whether a multistage step counts once; a
throughput is comparable across codes only when the counting rule,
normalization unit, precision, scheme, problem size per unit and hardware all
match.

## Normalizations in use

| Source | Unit of normalization | Value(s) as printed | Hardware | Precision | Problem and scheme |
|---|---|---|---|---|---|
| [Athena](/software/athena.md) ([Stone et al. (2008)](/sources/stone-2008.md), Table 1) | one CPU (per CPU second) | $85.9\times10^3$ (Roe) and $97.6\times10^3$ (HLLD), adiabatic MHD | 2.2 GHz Opteron | not stated on the page | 3D, $128^3$ |
| [Athena++](/software/athena-plus-plus.md) ([Stone et al. (2020)](/sources/stone-2020.md), §3.6.1) | one core | 2.924 million zone-cycles/s; full-node per-core about 2× lower | Skylake 6148 | not stated on the page | 3D MHD, HLLD + PLM, VL2, $64^3$ block |
| [Castro](/software/castro.md) ([Almgren et al. (2010)](/sources/almgren-2010.md), §7.4) | one core, as grind time | 24.8 µs per cell per step per core at 64,000 processors | jaguarpf | not stated on the page | weak scaling, no gravity |
| [Enzo](/software/enzo.md) ([Bryan et al. (2014)](/sources/bryan-2014.md), §12.2.2) | one MPI task | relative only: 20% drop from 8 to 4,096 tasks | Cray XT4 | not stated on the page | $128^3$ per task |
| [GAMER](/software/gamer.md) ([Zhang et al. (2018)](/sources/zhang-2018.md), §5.2) | one GPU; whole machine | $1.2\times10^8$ (single), $5.5\times10^7$ (double) per GPU; $5\times10^{10}$ at 4096 nodes | P100; Blue Waters K20X nodes | stated | VL + PLM + Roe uniform; CTU + PPM + Roe AMR (single) |
| [AthenaK](/software/athenak.md) ([Stone et al. (2026)](/sources/stone-2026.md), Tables 1–2) | one device (CPU socket or GPU) | hydro/MHD, in millions: A100 614/298, H100 677/290, Grace Hopper 1077/565, MI250 405/190, 32-core Xeon 63/33 | as listed | not stated | 3D linear wave, $512\times256\times256$ with $128^3$ blocks on GPUs; solver options not stated |
| [IDEFIX](/software/idefix.md) ([Lesur et al. (2023)](/sources/lesur-2023.md), Table 4) | one node | 484 Mcell/s (4 V100), 1240 Mcell/s (4 MI250X), 25.0 (2× Cascade Lake), 41.3 (2× EPYC Rome) | Jean Zay, Adastra, Irene | double | 3D Orszag–Tang, HLLD + PLM + RK2; $256^3$ per GPU, $32^3$ per core |
| [Cholla](/software/cholla.md) ([Caddy & Schneider (2024)](/sources/caddy-2024.md), §3.2) | one GPU or GCD | $2.36\times10^8$ per MI250X GCD (text; caption $2.04\times10^8$); $2.59\times10^8$ A100, $1.60\times10^8$ V100 | Frontier; NVIDIA systems not described | double for Frontier; not stated for NVIDIA | slow wave, $459^3$ per GCD, PLMC + HLLD, VL+CT |
| [Quokka](/software/quokka.md) ([Wibking & Krumholz (2022)](/sources/wibking-2022.md), Tables 1–4) | one GPU | 113.34 (V100, PPM), 157.75 (V100, PLM), 254.05 (A100) Mzones/s; radiation hydrodynamics 22.55 (V100), 39.04 (A100), counting one hydro step with its radiation substeps as one update | Gadi V100 nodes; one 4-A100 node | not stated | 3D periodic Sedov (hydro), radiation-driven shell (radiation hydrodynamics); $256^3$ per GPU in the A100 runs |
| [GRaM-X](/software/gram-x.md) ([Shankar et al. (2023)](/sources/shankar-2023.md), §V A) | one GPU | $0.47\times10^8$ (ideal gas, static spacetime, RK2), $0.26\times10^8$ (tabulated EOS, RK4), $0.062\times10^8$ (dynamical spacetime) | Summit V100 | FP64 implied, not stated | unigrid, WENO5, $240^3$ or $168^3$ per GPU |
| [gPLUTO](/software/gpluto.md) ([Rossazza et al. (2026)](/sources/rossazza-2026.md), Fig. 6) | one node | not printed; read from the plot: about $1.5\times10^8$ (4 H100), $1.1\times10^8$ (4 A100), $1.2\times10^7$ (112 CPU cores) | MareNostrum 5, Leonardo, MeluXina | double | 3D Orszag–Tang, WENOZ + HLLD + RK3, CT |
| [ADAM](/software/adam.md) ([Zaghi et al. (2023)](/sources/zaghi-2023.md), Table 1) | one GPU, as grind time | 0.16–0.49, labelled seconds but numerically seconds per iteration per million cells per GPU | Marconi100 V100 | not stated | shock diffraction by a sphere, WENO + SSP-RK3, AMR (update time excluded) |
| [STREAmS](/software/streams.md) ([Bernardini et al. (2021)](/sources/bernardini-2021.md), Table 3) | one GPU, as grind time | 9.6 ns per point per iteration (ZEFR 28.3); 350 bytes per point (ZEFR 2060) | GPU not stated | not stated | channel flow, fourth-order central flux |

## Pitfalls the sources record

* **What counts as one update.** Quokka's radiation-hydrodynamics rate
  counts one hydrodynamic step together with its radiation substeps (10 in
  the benchmark) as one zone update
  ([Wibking & Krumholz (2022)](/sources/wibking-2022.md), §4.1).

* **Device versus GCD.** AthenaK's Table 1 says "AMD MI250" without saying
  whether one GCD or the two-GCD module is meant, while its Frontier scaling
  counts single GCDs as "GPUs" ([Stone et al. (2026)](/sources/stone-2026.md),
  §5.1–§5.2). IDEFIX counts one two-GCD MI250X module as one "GPU" (1024 GPUs on 256
  nodes with four MI250X per node), so its 1240 Mcell/s per node is about
  155 Mcell/s per GCD ([Lesur et al. (2023)](/sources/lesur-2023.md),
  abstract, Table 3, Table 4). Cholla runs one GCD per
  rank and calls each GCD "a single GPU"
  ([Caddy & Schneider (2024)](/sources/caddy-2024.md), §3.2).
* **Per node hides the node.** Cholla compares itself with the Parthenon/AthenaPK
  numbers of Grete et al. (2023), which are per node and hydro, not MHD (its
  footnote 8), so the comparison is
  not like-for-like ([Caddy & Schneider (2024)](/sources/caddy-2024.md),
  §3.2). Quokka states that its radiation-hydrodynamics rate on GPUs,
  normalized per CPU core of the node, is "comparable to or better than"
  Athena++ hydrodynamics on CPUs, with no Athena++ number printed
  ([Wibking & Krumholz (2022)](/sources/wibking-2022.md), §4.1).
* **Mislabelled axes and inconsistent values.** AthenaK's scaling figures
  label total performance "Mzcps" over $10^8$–$10^{12}$, consistent with
  cell updates per second rather than millions
  ([Stone et al. (2026)](/sources/stone-2026.md), Figs. 21–22). Cholla prints
  two single-GCD throughputs ($2.36\times10^8$ in the text, $2.04\times10^8$
  in the Fig. 13 caption) ([Caddy & Schneider (2024)](/sources/caddy-2024.md),
  §3.2). ADAM's grind time is labelled in seconds
  ([Zaghi et al. (2023)](/sources/zaghi-2023.md), Table 1).
* **Problem size per device.** AthenaK's A100 throughput falls from 614 to 126
  million updates per second as MeshBlocks shrink from $128^3$ to $16^3$
  ([Stone et al. (2026)](/sources/stone-2026.md), §5.1); see
  [GPU porting](/methods/gpu-porting.md) for the other sources' thresholds.
* **Physics content.** MHD costs about 2× hydro in AthenaK (Riemann solver and
  CT), and GRaM-X drops about 1.8× from ideal gas with RK2 to a tabulated EOS
  with RK4 — two changes at once
  ([Stone et al. (2026)](/sources/stone-2026.md), Table 2;
  [Shankar et al. (2023)](/sources/shankar-2023.md), §V A).
* **Accuracy-equivalent cost.** STREAmS multiplies its grind time and memory
  per point by the number of points needed for equal error, giving about 10×
  less time and about 20× less memory than the flux-reconstruction code ZEFR
  at matched accuracy, where per point the gap is only about 3× and 6×
  ([Bernardini et al. (2021)](/sources/bernardini-2021.md), §4.4).

## Related metrics

* **Energy per update.** IDEFIX reports cells per kWh from thermal design
  power ([Lesur et al. (2023)](/sources/lesur-2023.md), §5); gPLUTO measures
  energy to solution and defines efficiency as FLOPS per watt without
  reporting FLOP counts ([Rossazza et al. (2026)](/sources/rossazza-2026.md),
  §4.3).
* **Fraction of peak.** Neko reports Tflop/s and percent of double-precision
  peak for one kernel, and time per step for the whole solver
  ([Jansson et al. (2024)](/sources/jansson-2024.md), §6, §9).

## Later uses (batch 4)

| Source | Unit of normalization | Value(s) as printed | Hardware | Precision | Problem and scheme |
|---|---|---|---|---|---|
| [H-AMR](/software/h-amr.md) ([Porth et al. (2019)](/sources/porth-2019.md), §4.1.5, quoting Chatterjee et al. 2019) | one GPU | "3 − 5 × 10⁸ zone-cycles/s/GPU", including a speed-up of 3–5 from 3–4 levels of locally adaptive time stepping | not stated | not stated | not stated |
| [H-AMR](/software/h-amr.md) ([Shankar et al. (2023)](/sources/shankar-2023.md), §V A, quoting Liska et al.) | one GPU | "∼ 0.85 × 10⁸ zone-cycles/s" | Summit V100 | not stated | "a similar physics setup" to GRaM-X's, not specified |

* **Time-step-adaptive speed-ups folded into the rate.** H-AMR's
  $3$–$5\times10^8$ zone-cycles/s per GPU is an *effective* rate: it
  includes the factor 3–5 gained from locally adaptive time stepping, which
  decouples temporal from spatial refinement levels
  ([Porth et al. (2019)](/sources/porth-2019.md), §3, §4.1.5), so it is not
  comparable with rates measured with one global time step. The
  $0.85\times10^8$ figure (one V100, 2022) is not comparable with it
  either: the larger figure is quoted from Chatterjee et al. (2019) with no
  hardware stated, and neither source says whether the smaller one
  includes the speed-up.

# Citations

1. [Stone et al. (2008)](/sources/stone-2008.md), §7, Table 1.
2. [Almgren et al. (2010)](/sources/almgren-2010.md), §7.4.
3. [Bryan et al. (2014)](/sources/bryan-2014.md), §12.2.2.
4. [Zhang, Schive & Chiueh (2018)](/sources/zhang-2018.md), §5.2.
5. [Stone et al. (2020)](/sources/stone-2020.md), §3.6.1.
6. [Bernardini et al. (2021)](/sources/bernardini-2021.md), §4.4, Table 3.
7. [Wibking & Krumholz (2022)](/sources/wibking-2022.md), §4, Tables 1–4
   (arXiv v2).
8. [Lesur et al. (2023)](/sources/lesur-2023.md), §5, Table 4.
9. [Shankar et al. (2023)](/sources/shankar-2023.md), §V A (arXiv v2).
10. [Zaghi et al. (2023)](/sources/zaghi-2023.md), §3.2, Table 1.
11. [Caddy & Schneider (2024)](/sources/caddy-2024.md), §3.2.
12. [Jansson et al. (2024)](/sources/jansson-2024.md), §§6, 9 (arXiv
    preprint 2021).
13. [Stone et al. (2026)](/sources/stone-2026.md), §5, Tables 1–2,
    Figs. 21–22 (arXiv v1).
14. [Rossazza et al. (2026)](/sources/rossazza-2026.md), §§4.1, 4.3, Fig. 6
    (arXiv v1).
15. [Porth et al. (2019)](/sources/porth-2019.md), §3, §4.1.5 (arXiv v2).
