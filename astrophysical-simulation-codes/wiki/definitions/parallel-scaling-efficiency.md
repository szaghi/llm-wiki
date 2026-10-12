---
type: Definition
title: "Parallel scaling efficiency"
description: "Weak-scaling efficiency (fixed work per processing unit) and strong-scaling efficiency (fixed total work) as the code papers define them, with the baselines each source uses — one core, one GPU, one node, several nodes or the smallest run that fits — on which every quoted percentage depends."
status: established
aliases: [parallel efficiency, weak scaling, strong scaling, weak-scaling efficiency, strong-scaling efficiency, doubling efficiency]
tags: [performance, scaling, gpu]
timestamp: 2026-10-12T00:00:00Z
---

# Parallel scaling efficiency

**Weak scaling** keeps the work per processing unit (core, GPU, GCD or node)
fixed while the number of units grows; its efficiency is the time per step
of the baseline run divided by the time per step of the larger run, or
equivalently the throughput per unit of the larger run divided by that of the
baseline. **Strong scaling** keeps the total problem fixed; its efficiency is
the measured speed-up over the baseline divided by the ratio of unit counts.
Ideal is 1 (100%) in both. Printed forms:
* GAMER: strong efficiency = (time at the smallest node count / time at the
  current count) / (current count / smallest count); weak efficiency = time
  at the smallest count / time at the current count
  ([Zhang et al. (2018)](/sources/zhang-2018.md), §5.2).
* gPLUTO: weak efficiency = wall time on one node / wall time on the larger
  node count; strong efficiency = measured speed-up over
  ideal within each group of runs
  ([Rossazza et al. (2026)](/sources/rossazza-2026.md), §4.1).
* AthenaK: weak efficiency = per-device performance / single-device
  performance ([Stone et al. (2026)](/sources/stone-2026.md), §5.2).

GAMER also defines a **doubling efficiency**, the time ratio when halving the
node count minus one: 57% at $10^3$ nodes, where its strong efficiency is 70%
([Zhang et al. (2018)](/sources/zhang-2018.md), §5.2).

A quoted percentage is meaningless without its **baseline**: an efficiency
relative to one node already absorbs the intra-node loss that an efficiency
relative to one GPU would show.

## Baselines and results in the sources

| Source | Kind | Baseline | Result as printed | Hardware, precision |
|---|---|---|---|---|
| [Athena](/software/athena.md) ([Stone et al. (2008)](/sources/stone-2008.md), §7) | weak | not stated on the page | "above 85%" to 20,000 processors ($32^3$ or $64^3$ per processor) | Cray XT-3 |
| [Castro](/software/castro.md) ([Almgren et al. (2010)](/sources/almgren-2010.md), §7.4) | weak | not stated (range 8–64,000 processors) | "scales excellently" to 64,000 (one $64^3$ grid each); Poisson gravity to 13,824 | jaguarpf |
| [Enzo](/software/enzo.md) ([Bryan et al. (2014)](/sources/bryan-2014.md), §12.2.2) | weak | 8 tasks | 20% drop in cell updates per task to 4,096 tasks, 40% to 13,824 | Cray XT4 |
| [GAMER](/software/gamer.md) ([Zhang et al. (2018)](/sources/zhang-2018.md), §5.2) | strong; weak (replicated problem) | smallest run: 64 nodes (strong), range 1–4096 nodes (weak) | 70% strong and 57% doubling at $10^3$ nodes; 70% weak at $10^3$ nodes, 85% at 512 | Blue Waters K20X nodes, single precision |
| [Athena++](/software/athena-plus-plus.md) ([Stone et al. (2020)](/sources/stone-2020.md), §3.6) | weak | 8 nodes | 97% (hydro) and 95% (MHD) at 250 nodes; 86% and 84% at 2048 KNL nodes | Cray XC50; Oakforest-PACS |
| Athena++ multigrid ([Tomida & Stone (2023)](/sources/tomida-2023.md), §4.1.2) | weak | 2 nodes | 89.6%, 73.2%, 45.7% at 200 nodes for $128^3$, $64^3$, $32^3$ blocks (one FMG sweep) | not stated on the page |
| [STREAmS](/software/streams.md) ([Bernardini et al. (2021)](/sources/bernardini-2021.md), §4.3) | weak; strong | 1 GPU | weak about 97% at 1024 GPUs (asynchronous); strong above 90% at 8 GPUs, 70% at 16 | Marconi100 V100, precision not stated |
| [Quokka](/software/quokka.md) ([Wibking & Krumholz (2022)](/sources/wibking-2022.md), Tables 1–3, 5) | weak; strong with AMR | **4 GPUs** (one node) | weak 82.76% (PPM), 75.84% (PLM), 76.19% (radiation) at 256 GPUs; AMR strong 52.69% at 32 GPUs | Gadi V100, precision not stated |
| [IDEFIX](/software/idefix.md) ([Lesur et al. (2023)](/sources/lesur-2023.md), §5, Fig. 18) | weak | 1 node | above 80% to 1024 CPU nodes (131,072 cores); above 80% to 512 V100; above 95% to 1024 MI250X | double |
| [GRaM-X](/software/gram-x.md) ([Shankar et al. (2023)](/sources/shankar-2023.md), Tables II–III) | weak; strong | **1 node (6 GPUs)**; 8 nodes | weak 0.40 and 0.49 at 2304 nodes; strong 0.19 at 1000 nodes | Summit V100, FP64 implied |
| [ADAM](/software/adam.md) ([Zaghi et al. (2023)](/sources/zaghi-2023.md), §3.2, Table 1) | strong; weak by grind time | 1 GPU | near ideal to 8 GPUs ("even superlinear"), close to 90% at 16, below 60% at 32 (AMR update excluded) | Marconi100 V100, precision not stated |
| [Cholla](/software/cholla.md) ([Caddy & Schneider (2024)](/sources/caddy-2024.md), §3.2) | weak; strong | 1 GCD (weak); not stated (strong) | weak 82.2% (text and caption) or 80% (summary) at 74,088 GCDs; strong 80% at 32 GPUs, 67.2% at 64 | Frontier MI250X GCDs, double |
| [AthenaK](/software/athenak.md) ([Stone et al. (2026)](/sources/stone-2026.md), §5.2) | weak | 1 device | "roughly 70%" at 4096 A100; 80% at 65,536 MI250X GCDs; AMR weak scaling "nearly perfect" to 4096 GCDs | Perlmutter, Frontier; precision not stated |
| [gPLUTO](/software/gpluto.md) ([Rossazza et al. (2026)](/sources/rossazza-2026.md), §4.1–§4.2) | weak; strong | 1 node; first run of each group | Orszag–Tang weak 88% at 512 Leonardo nodes; strong group averages 0.90 and 0.89 | H100 and A100 nodes, double |

## What the sources show about baselines

* **Intra-node loss hidden by a node baseline.** Quokka loses about 40% of
  per-GPU throughput from 1 to 4 GPUs (113.34 to 70.68 Mzones/s), then sets
  4 GPUs to 100% ([Wibking & Krumholz (2022)](/sources/wibking-2022.md),
  Table 1). GRaM-X's one-node per-GPU rate ($0.154\times10^8$) is already below
  its single-GPU rate ($0.26\times10^8$) for the same set-up, so its 40%
  relative to one node would be lower relative to one GPU
  ([Shankar et al. (2023)](/sources/shankar-2023.md), §V A–§V B). Athena++
  quotes its KNL weak scaling relative to 8 nodes
  ([Stone et al. (2020)](/sources/stone-2020.md), §3.6).
* **Superlinear strong scaling.** ADAM's speed-ups from 1 to 8 GPUs exceed
  the GPU ratio ([Zaghi et al. (2023)](/sources/zaghi-2023.md), §3.2). In
  AthenaK's AMR weak scaling, a MeshBlock that grows with the device count
  gives super-linear curves, while fixed $32^3$ blocks give "nearly perfect
  weak scaling" ([Stone et al. (2026)](/sources/stone-2026.md), §5.2, Fig. 22).
* **Decomposition geometry.** GRaM-X reaches about 98% weak efficiency on an
  elongated $1{,}399{,}680\times240\times240$ grid on 972 nodes, against 0.39
  for the cubic grid at the same node count ([Shankar et al. (2023)](/sources/shankar-2023.md),
  §V B).
* **Machine state.** AthenaK attributes a dip on Perlmutter at small node
  counts to production-mode network load
  ([Stone et al. (2026)](/sources/stone-2026.md), §5.2).
* **Strong-scaling indicator.** Neko argues that the strong-scaling limit is
  where arithmetic and communication times are equal, communication being
  dominated by allreduce latency, and that the right indicator is the work
  per process divided by memory bandwidth, not the work per process alone
  ([Jansson et al. (2024)](/sources/jansson-2024.md), §10). Neko reports wall
  time per step against core count without an efficiency figure (§9).

## Printed inconsistencies

Several sources print efficiencies that their own data do not reproduce;
each is recorded on its Source page:
* Cholla: 82.2% in text and caption, 80% in the summary; the text's per-GCD
  throughputs give about 80%; its "at most a ≈ 55% drop" is a loose
  bound beside the measured 67.2% at 64 GPUs ([Caddy & Schneider (2024)](/sources/caddy-2024.md), §3.2,
  §5).
* AthenaK: "roughly 70% on 4096 GPUs" while the plotted A100 curves end near
  $10^3$ GPUs at about 0.63–0.68 ([Stone et al. (2026)](/sources/stone-2026.md),
  Fig. 21).
* gPLUTO: the Alfvén-wave strong-scaling averages (0.97, 0.93) are not
  reproducible from Table 5 by the rule that reproduces Table 4
  ([Rossazza et al. (2026)](/sources/rossazza-2026.md), §4.2).
* STREAmS: the per-GPU axis of the strong-scaling figure is a factor 10 off
  the stated mesh ([Bernardini et al. (2021)](/sources/bernardini-2021.md),
  Fig. 13).

# Citations

1. [Stone et al. (2008)](/sources/stone-2008.md), §7.
2. [Almgren et al. (2010)](/sources/almgren-2010.md), §7.4.
3. [Bryan et al. (2014)](/sources/bryan-2014.md), §12.2.2.
4. [Zhang, Schive & Chiueh (2018)](/sources/zhang-2018.md), §5.2.
5. [Stone et al. (2020)](/sources/stone-2020.md), §3.6.
6. [Tomida & Stone (2023)](/sources/tomida-2023.md), §4.1.2.
7. [Bernardini et al. (2021)](/sources/bernardini-2021.md), §4.3, Fig. 13.
8. [Wibking & Krumholz (2022)](/sources/wibking-2022.md), §4, Tables 1–3, 5
   (arXiv v2).
9. [Lesur et al. (2023)](/sources/lesur-2023.md), §5, Fig. 18.
10. [Shankar et al. (2023)](/sources/shankar-2023.md), §V, Tables II–III
    (arXiv v2).
11. [Zaghi et al. (2023)](/sources/zaghi-2023.md), §3.2, Table 1.
12. [Caddy & Schneider (2024)](/sources/caddy-2024.md), §3.2, §5.
13. [Jansson et al. (2024)](/sources/jansson-2024.md), §§9–10 (arXiv
    preprint 2021).
14. [Stone et al. (2026)](/sources/stone-2026.md), §5.2, Figs. 21–22 (arXiv
    v1).
15. [Rossazza et al. (2026)](/sources/rossazza-2026.md), §§4.1–4.2,
    Tables 4–5 (arXiv v1).
