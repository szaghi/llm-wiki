---
type: Software
title: "H-AMR"
description: "GPU-accelerated GRMHD code rewritten from HARM, hybrid CUDA–OpenMP–MPI, with AMR and locally adaptive time stepping; in the EHT code comparison it ran second-order PPM with HLL and upwind constrained transport, static azimuthal de-refinement near the pole and drift-frame floors, and its throughput is quoted as 0.85e8 zone-cycles/s on one V100 and 3–5e8 zone-cycles/s per GPU including the time-stepping speed-up."
status: established
aliases: [H-AMR, HAMR]
tags: [software, mhd, relativity, gpu, cuda, amr, constrained-transport, riemann-solver, performance]
timestamp: 2026-10-12T00:00:00Z
---

# H-AMR

H-AMR is a general-relativistic MHD code: a rewrite of HARM and HARM-PI
for GPUs, "hybrid CUDA-OpenMP-MPI", with adaptive mesh refinement and
"locally adaptive timestepping (LAT)"
([Porth et al. (2019)](/sources/porth-2019.md), §3, §4.1.5). Its code
paper is Liska et al. (2022, ApJS 263:26), which this bundle has not
ingested. Everything below is what two ingested sources state about it.
No repository URL or licence is printed in either.

## Solvers

In its [EHT code comparison](/results/eht-grmhd-code-comparison.md)
configuration ([Porth et al. (2019)](/sources/porth-2019.md), Table 1,
§4.1.5):
* second-order time integration; HLL fluxes (see
  [approximate Riemann solvers](/methods/approximate-riemann-solvers.md));
  PPM reconstruction;
* staggered upwind [constrained transport](/methods/constrained-transport.md)
  after Gardiner & Stone (2005), the same family as
  [Athena++](/software/athena-plus-plus.md) (App. A);
* entropy advected as a backup for
  [primitive-variable recovery](/methods/primitive-variable-recovery.md)
  (§4.1).

## Mesh and time stepping

* **Locally adaptive time stepping.** LAT decouples temporal from spatial
  refinement levels and is stated to be "superior to the 'standard'
  hierarchical timestepping ... giving much greater speedups on logarithmic
  spaced spherical grids" (§3). No algorithm is given in this source.
* **Polar de-refinement** (§4.1.5). Up to 5 levels of static de-refinement
  in azimuth near the pole: 64, 128, 256, 512 and 1024 azimuthal cells in
  the polar bands 0–3.75°, 3.75–7.5°, 7.5–15°, 15–30° and 30–90°.
* **Comparison grid** (Table 1): radial domain $1.169$–$500\,r_{\mathrm g}$,
  full polar range; proper cell widths 0.523, 0.379 and 0.785
  $r_{\mathrm g}$ (radial, meridional, azimuthal) at $12r_{\mathrm g}$ in
  the midplane at the lowest resolution. The very-high-resolution run has
  $1608\times1056\times1024$ cells with 5 azimuthal de-refinement levels
  (Table 2, §5.7), run on Blue Waters (acknowledgments).

## Floors

A density floor equal to the larger of the squared fluid-frame field
strength divided by 20 and $10^{-5}$ times the radius (in $r_{\mathrm g}$)
to the power $-3/2$, and an internal-energy floor equal to the larger of
that squared field strength divided by 750 and $3.33\times10^{-8}$ times
the radius to the power $-5/2$; mass is inserted in the drift frame, which
avoids the velocity runaway of fluid-frame injection and the drag of
injection in the frame of zero-angular-momentum observers (§4.1.5). See
[density and pressure floors](/methods/numerical-floors.md).

## Performance

* "We typically use 3 − 4 levels of local adaptive timestepping to speed up
  the code by an additional factor 3 − 5 to 3 − 5 × 10⁸
  zone-cycles/s/GPU" ([Porth et al. (2019)](/sources/porth-2019.md),
  §4.1.5, quoting Chatterjee et al. 2019). No GPU model, precision or
  problem size is given; the figure includes the LAT speed-up.
* "∼ 0.85 × 10⁸ zone-cycles/s for a similar physics setup" on one Summit
  V100, as quoted by the GRaM-X paper, which calls its own $0.47\times10^8$
  "comparable"; H-AMR's set-up is not specified
  ([Shankar et al. (2023)](/sources/shankar-2023.md), §V A).
* [AthenaK](/software/athenak.md)'s 120 Mzone-cycles/s for GRMHD on one A100
  is called "comparable to" H-AMR (Liska et al. 2022), with no H-AMR number
  printed ([Stone et al. (2026)](/sources/stone-2026.md), §5.1, Table 2).

The two figures are not comparable: the $3$–$5\times10^8$ figure is quoted
by Porth et al. from Chatterjee et al. (2019) with no hardware stated, the
$0.85\times10^8$ figure is a 2022 V100 measurement, and neither source
states whether it includes the LAT speed-up. See
[cell-update throughput](/definitions/cell-updates-per-second.md).

## Verification

* **[Magnetized Fishbone–Moncrief torus](/benchmarks/magnetized-torus-accretion.md)**
  at all three standard resolutions and at the very high resolution, whose
  disk-averaged MRI quality factors are at least 120, 100 and 190 (radial,
  meridional, azimuthal), with 85–100 cells per scale height; its field
  profiles are the reference the standard runs match (§5.3, §5.7).
* **PPM versus PLM** (App. A, Table 3, Fig. 23). With PLM (MC limiter,
  parameter 1.5), H-AMR's time-averaged accretion rate falls well below its
  PPM value even at $192^3$ (the paper's range for H-AMR and Athena++ is
  "a factor of two to almost six"); the meridional MRI quality factor stays
  below 10 and decays, and the disk shrinks even at 192 meridional cells
  (§5.6.2, Fig. 20).

## Use

H-AMR is one of the four codes of the EHT M87 simulation library, with
iharm3D, KORAL and BHAC
([Porth et al. (2019)](/sources/porth-2019.md), §6.5).

# Citations

1. [Porth et al. (2019)](/sources/porth-2019.md), §3, §4.1, §4.1.5, §5.3, §5.6.2, §5.7, §6, Tables 1–3, Figs. 20, 23, App. A, acknowledgments (arXiv v2).
2. [Shankar et al. (2023)](/sources/shankar-2023.md), §V A (arXiv v2).
3. [Stone et al. (2026)](/sources/stone-2026.md), §5.1, Table 2 (arXiv v1).
