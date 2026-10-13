---
type: Result
title: "EHT GRMHD code comparison"
description: "Nine GRMHD codes run one weakly magnetized torus around a spinning black hole at three resolutions; their horizon fluxes agree better as resolution rises (time-averaged accretion rate max/min from 3.9 to 1.77, non-monotone with 8.6 at N = 128; normalized magnetic flux from 17.4 to 2.8), and the residual differences are traced to MRI resolution, polar boundaries, outer-boundary placement, floors and PPM versus PLM, not to a preferred code."
status: established
aliases: [EHT code comparison, Event Horizon Telescope GRMHD code comparison, Porth et al. code comparison, GRMHD code comparison project]
tags: [mhd, relativity, benchmark, verification, constrained-transport, riemann-solver, time-integration]
timestamp: 2026-10-12T00:00:00Z
---

# EHT GRMHD code comparison

The Event Horizon Telescope (EHT) code comparison runs nine
general-relativistic MHD codes on one problem, the
[magnetized Fishbone–Moncrief torus](/benchmarks/magnetized-torus-accretion.md)
in its SANE state, and compares common diagnostics
([Porth et al. (2019)](/sources/porth-2019.md)). Grids, boundaries and
floors are left to each group, so the comparison measures each code "as
typically used" (§4). The result: "the community of GRMHD codes is mature,
capable, and consistent on these test problems" (abstract); once
resolution standards are met, "we can find no preference favoring one
solution against the other" (§6.5). The comparison informed the EHT M87
simulation library, built with iharm3D, KORAL, H-AMR and BHAC (43
simulations).

## The codes

"All apply overall 2nd order conservative schemes and preserve the
divergence of the magnetic field to machine precision. All except iharm3D
applied the piecewise-parabolic-method (PPM)" (§6). They differ in the
order of time integration, the Riemann solver and the discretization of
the induction equation. Low-resolution configurations (Table 1, §4.1;
spacings are proper cell widths in units of $r_{\mathrm g}$ at radius
$12r_{\mathrm g}$ in the midplane, eq. 10; radial domains in $r_{\mathrm g}$):

| Code | Time integrator | Riemann solver | Reconstruction | Induction scheme | Spacing (radial, meridional, azimuthal) | Radial domain | Polar domain |
|---|---|---|---|---|---|---|---|
| [Athena++](/software/athena-plus-plus.md) | VL2 (van Leer 2006), 2nd order | HLL | PPM | upwind CT (Gardiner & Stone 2005) | 0.506, 0.393, 0.788 | 1.152–50 | 0–π |
| BHAC | two-step predictor–corrector, 2nd order | LLF | PPM | UCT (Del Zanna et al. 2007) | 0.402, 0.295, 0.788 | 1.185–3333 | 0–π |
| BHAC Cartesian | 2nd order | LLF | PPM | UCT (Del Zanna et al. 2007) | Cartesian AMR, 0.176, 0.163, 0.163 | §4.1.2 | — |
| Cosmos++ | 5-stage SSPRK, 3rd order (Spiteri & Ruuth 2002) | HLL | PPM | staggered CT (Fragile et al. 2012) | 0.508, 0.375, 0.788 | 1.25–354 | 0.070–3.072 |
| ECHO | IMEX-SSP (Pareschi & Russo 2005), effectively RK3 | HLL | PPM | UCT (Del Zanna et al. 2007) | 0.460, 0.382, 0.752 | 1.048–2500 | 0.060–3.082 |
| [H-AMR](/software/h-amr.md) | 2nd order | HLL | PPM | UCT (Gardiner & Stone 2005) | 0.523, 0.379, 0.785 | 1.169–500 | 0–π |
| HARM-Noble | RK2 | LLF ("LF" in §4.1.6) | PPM | Flux-CT (Tóth 2000; Noble et al. 2009) with PPM edge EMFs | 0.578, 0.182, 0.784 | 1.090–80 | 0.053–3.088 |
| iharm3D | predictor–corrector, method of lines, 2nd order | LLF | PLM (MC limiter) | Flux-CT (Tóth 2000) | 0.519, 0.118, 0.788 | 1.073–50 | 0–π |
| IllinoisGRMHD | RK4 | HLL | PPM | vector-potential PPM + Flux-CT (Tóth 2000; Etienne et al. 2010, 2012) | Cartesian AMR, 0.246, 0.228, 0.229 | §4.1.8 | — |
| KORAL | 2nd order | LLF | PPM | Flux-CT (Tóth 2000) | 0.478, 0.266, 0.785 | 1.15–50 | 0–π |

Lineages (§3): Athena++ is a rewrite of Athena with GRMHD in arbitrary
stationary spacetimes; BHAC is the GRMHD module of MPI-AMRVAC with
oct-tree block AMR; Cosmos++ is object-oriented C++ on unstructured meshes;
ECHO uses high-order finite-difference reconstruction; H-AMR is a GPU
rewrite of HARM; HARM-Noble and iharm3D descend from HARM; IllinoisGRMHD
is a vector-potential Cartesian AMR code in the Einstein Toolkit; KORAL is
HARM-like with optional M1 radiation. Two runs are Cartesian (BHAC
Cartesian and IllinoisGRMHD). See
[constrained transport](/methods/constrained-transport.md),
[approximate Riemann solvers](/methods/approximate-riemann-solvers.md) and
[primitive-variable recovery](/methods/primitive-variable-recovery.md)
for the scheme families.

## What is compared

Horizon fluxes of mass ($\dot M$), magnetic flux normalized by
$\sqrt{\dot M}$, angular momentum and energy, as time series and averages
over $5000$–$10^4$ $r_{\mathrm g}/c$ (eqs. 13–16, Figs. 2–4, Table 2);
disk-averaged radial profiles (Figs. 6–8); time- and azimuth-averaged maps
(Figs. 9–12); the jet boundary at unit magnetization (Fig. 13); scale
height (Fig. 15); an optically thin synchrotron emission proxy, its power
spectrum and RMS–flux relation (Figs. 16–18); the Maxwell-stress parameter
(Fig. 19); disk radius (Figs. 20, 22); and MRI quality factors, the
wavelength of the fastest-growing MRI mode divided by the cell width in
each direction (eqs. 25–26, Figs. 21, 23) (§5.1).

## Agreement versus resolution

Max/min across codes of the time averages (Table 2):

| Quantity | $N = 96$ | $N = 128$ | $N = 192$ |
|---|---|---|---|
| accretion rate $\langle\dot M\rangle$ | 3.903 | 8.604 | 1.772 |
| normalized horizon magnetic flux | 17.408 | 12.24 | 2.777 |
| specific angular-momentum flux | 1.823 | 1.201 | 1.121 |
| normalized energy flux | 7.096 | 4.631 | 1.405 |

At high resolution the angular-momentum and energy fluxes differ by 12 %
and 40 % (§5.2); the mean accretion rate spread is about 1.7 (§6). All runs
are SANE, with normalized flux about 0.5–6, below the maximum of about 15
(§5.2).

* **Resolution measure** (§5.2, Fig. 5, §6.1). Ordering runs by the proper
  meridional cell spacing, not by the cell count, organizes the data: the
  spread in accretion rate and horizon flux collapses below a critical
  spacing. The iharm3D run with 96 meridional cells is finer at the
  midplane than BHAC and KORAL with 192.
* **MRI quality factors** (§5.6–§5.7, §6.1). Disk-averaged values (radial,
  meridional, azimuthal) are about (2.9, 3, 14) at $N = 96$, (3, 3.8, 17)
  at 128, (7.3, 7.9, 19.7) at 192, (21.3, 24.5, 40.9) for BHAC at 384 and at
  least (120, 100, 190) for H-AMR at 1056 meridional cells (85–100 cells
  per scale height). Only the highest standard resolution keeps the MRI
  turbulence alive to $10^4$ $r_{\mathrm g}/c$.
* **Convergence** (§5.6, §6.1). Disk radius converges above 192 meridional
  cells; the disk Maxwell-stress parameter and the inverse plasma beta keep
  rising weakly up to about $1024^3$ (the latter by about 3 from lowest to
  highest resolution, Fig. 22). "Convergence in the strict sense cannot be
  achieved for ideal MHD simulations of turbulence" (§1, §6.1). The stress
  parameter rises with resolution in these global runs, opposite to local
  shearing boxes (§5.6.1).
* **Persisting differences at $N = 192$.** Peak density still differs by
  about 3 (§6.2); the jet boundary at $50r_{\mathrm g}$ lies at a polar
  angle of 10°–15° with a spread of about 5° (Fig. 13, §6.3).
* **Variability** (§5.5, §6.4). The emission-proxy power spectrum has a
  slope of about 2 for all codes and resolutions; the RMS–flux slope is
  1.2–1.6 and converges to about 1.3 with resolution.
* **Cartesian AMR runs** (§5.2–§5.4). They agree qualitatively with the
  spherical runs except in the energy flux (BHAC Cartesian higher,
  IllinoisGRMHD slightly lower). Disk magnetization drops within about
  $10r_{\mathrm g}$, attributed to coarse inner resolution; IllinoisGRMHD
  shows horizontal artefacts in the inverse plasma beta at resolution
  jumps; no pole treatment is needed.
* **Run-to-run variation** (App. B, Table 4). KORAL repeated on two
  machines with different random perturbations differs "typically in the
  low percent regime" (accretion-rate max/min 1.024 / 1.134 / 1.128),
  smaller than the differences between codes.

## Attribution of the differences

* **MRI resolution** (above): unresolved MRI underlies the low-resolution
  spread; BHAC's low- and mid-resolution "mini torus" is judged a numerical
  artefact of unresolved MRI (§5.3).
* **Polar axis** (§4.1, §5.2, §5.4, §6.2). Cut-outs with "soft" reflective
  or outflow boundaries let a truncation-error flux of the radial field
  leave the domain and deplete the funnel magnetization. Cosmos++'s
  horizon flux is "consistently off by a factor of ∼ 4", and medium-resolution
  Cosmos++ and HARM-Noble lose the magnetically dominated funnel;
  zero-flux "hard" boundaries counter this (Shiokawa et al. 2012). Pole
  treatments also set the time step: BHAC's static de-refinement of the
  axis raises it by 16 for the 3-level run, Athena++ de-refines by factors
  of 2 toward the poles, H-AMR de-refines up to 5 levels in azimuth near the
  pole, and iharm3D widens near-axis cells by a coordinate warp (eq. 12).
* **Outer boundary** (§5.3–§5.4). Codes with the outer boundary near the
  torus edge (Athena++, iharm3D, KORAL) form smaller tori, because outflow
  removes mass; Athena++ shows visible kinks.
* **Floors** (§6.3). Funnel plasma parameters "should not be taken at face
  value", but the effect on jet opening angle and profile is minor; see
  [density and pressure floors](/methods/numerical-floors.md).
* **Reconstruction** (App. A, Table 3, Fig. 23). With PLM, H-AMR (MC
  limiter with parameter 1.5) and Athena++ give time-averaged accretion
  rates "a factor of two to almost six" below their PPM runs even at
  $192^3$, and H-AMR's PLM runs keep the meridional quality factor below
  10 and decaying; KORAL (parameter 1.9) is more consistent. "Even when the
  overall order of the scheme is fixed to second order, the PPM method can
  significantly reduce the dissipation". One reason offered for KORAL is
  its cell-centred CT, less dissipative than the upwind CT of H-AMR and
  Athena++ (see [constrained transport](/methods/constrained-transport.md)).

## Qualifications

* **One test problem.** All conclusions concern one SANE torus; the codes
  were not compared on other set-ups in this source.
* **Seeding bug** (footnote 3). HARM-Noble used the same random seed on all
  MPI ranks, so its initial perturbation was azimuthally periodic and its
  runs lack the azimuthal modes 1 to 2, 1 to 5 and 1 to 5 at the three
  resolutions; the symmetry-preserving scheme does not regrow them from round-off.
* **Recorded as printed.** The critical spacing is printed as
  "∆θp = 0.0125 − 0.25" (Fig. 5 caption) and "∆θp ≃ 0.25 − 0.0125M"
  (§6.1); Fig. 5's abscissa and Table 1 point to 0.125–0.25. KORAL's
  accretion rates in Table 4 are 1.6–2.7 times those of Table 2 for the
  same nominal resolutions, unexplained by the paper.
* Later use: [AthenaK](/software/athenak.md) overlays its own SANE torus on
  the $128^3$ data sets of this comparison, visually only
  ([Stone et al. (2026)](/sources/stone-2026.md), §3.6, Fig. 14).

# Citations

1. [Porth et al. (2019)](/sources/porth-2019.md), abstract, §§1, 3–6, Tables 1–4, Figs. 2–23, App. A–B, footnote 3 (arXiv v2).
2. [Stone et al. (2026)](/sources/stone-2026.md), §3.6, Fig. 14 (arXiv v1).
