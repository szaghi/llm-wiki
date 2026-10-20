---
type: Source
title: "Al Jahdali et al. (2022) — On the performance of relaxation and adaptive explicit Runge–Kutta schemes for high-order compressible flow simulations"
description: "Short note measuring the cost of global and local relaxation with nine explicit Runge–Kutta schemes under CFL-based and error-based step-size control on industrial compressible-flow DG simulations; the secant method is the only robust root finder, and error-controlled high-order relaxation schemes cost about as much as low-order ones."
resource: "doi:10.1016/j.jcp.2022.111333"
source_kind: paper
authors: [Al Jahdali R., Dalcin L., Parsani M.]
year: 2022
venue: "J. Comput. Phys. 464:111333"
local_file: "/home/stefano/papers/mosaic/ode-integration/2021_Crossref_Journal_of_Computational_Physics_Vermeire_Accelerated_implicit-explicit_Runge-Kutta_schemes_for_locall.pdf"
tags: [relaxation, step-size-control, entropy-stability, explicit, cfd, hpc]
timestamp: 2026-10-19T20:00:00Z
---

# Summary

The note is a performance study, not a theory paper. It measures what
[relaxation](/methods/relaxation-runge-kutta.md) costs when it is combined with
adaptive explicit Runge–Kutta methods in large compressible-flow simulations.
The spatial discretization is the hp-adaptive entropy-stable collocated DG
solver SSDC. Relaxation scales the update by $\gamma_n$ so that the fully
discrete scheme is [entropy stable](/properties/entropy-stability.md). In the
global variant $\gamma_n$ is the root of one scalar equation for the total
entropy $\eta$. In the local variant it is the minimum over cells of the roots
of cell-wise equations.

Nine schemes with positive weights are tested. Four use CFL-based control:
ERK(4,2), ERK(8,2) and ERK(5,3), which are stability-optimized for collocated
DG, and the classical RK4. Five use an error-based PID controller with
embedded pairs: BSRK(4,3), the [low-storage](/methods/low-storage-runge-kutta.md)
pairs SSP3(2)4[3S*+] and RK3(2)5F[3S*+], BSRK(8,5) and VRK(9,6)
([step-size control](/methods/step-size-control.md)). Seven scalar root
finders for $\gamma_n$ are compared on compressible homogeneous isotropic
turbulence and on flow past a 3D cylinder. Only the secant method never fails;
Newton and simplified Newton fail most often.

Performance runs cover 600 steps of the Imperial front wing (3.4M hexahedra)
and the NASA Common Research Model (9.1M hexahedra) on 512 cores. All runs are
stable even without relaxation. Global and local relaxation cost about the
same. With CFL control, relaxation leaves the number of function evaluations
almost unchanged, which the authors read as $\gamma_n\approx1$. With error
control it raises them by about 33% on the front wing. Error-controlled
third-order schemes beat the CFL-controlled ERK(5,3), and the fifth- and
sixth-order error-controlled schemes beat the low-order CFL-controlled ones in
most cases. The conclusion: when entropy stability is wanted, high-order
relaxation schemes with an error-based controller cost practically as much as
low-order schemes. The compressible homogeneous isotropic turbulence case
serves only the root-finder comparison; it is a different flow from the
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md), which the note does
not run.

# Version read

The file is the version of record (Elsevier typeset, open access CC BY-NC-ND,
article type "Short note"), 5 pages, with the DOI printed on page 1. **Identity
problem:** the archive filename names a different paper, Vermeire (2021),
"Accelerated implicit-explicit Runge-Kutta schemes for locally stiff systems".
Page 1 of the file is this paper (Al Jahdali, Dalcin, Parsani 2022), and its
title, venue, article number and DOI match Crossref. The Vermeire paper is not
in this file. The bundle law records the defect and the real Vermeire (2021)
file, added later under a full-title filename.

# Key claims

Notation: relaxed update $y^\gamma_{n+1}=y_n+\gamma_nh\sum_ib_if(t_n+c_ih,Y_i)$;
$\eta$ the convex entropy, $\eta_\kappa$ its restriction to cell $\kappa$.

1. Earlier work reported 20–35% time-to-solution savings from adaptive time stepping based on the error or on the CFL condition for industrially relevant turbulent flows (§1). **Stated**
2. Relaxation scales the weights by $\gamma_n$: $y^\gamma_{n+1}=y_n+\gamma_nh\sum_ib_if(t_n+c_ih,Y_i)$, and $\gamma_n=1$ recovers the base method (§2, Eq. 1). **Stated** (background)
3. Global relaxation: $\gamma_n$ is a root of one global scalar equation for $\eta$. Local relaxation: $\gamma_n=\min_\kappa\gamma_{n,\kappa}$, the minimum over cells of the roots of local equations for $\eta_\kappa$ (§2). **Stated**
4. Relaxation theory requires positive weights $b_i$, so only such schemes are selected (§2.1). **Stated**
5. CFL-based step: $h_{n+1}=\sigma\,\nu\min_i\Delta x_i/v_i^n$, with safety factor $\sigma=0.95$ and $\nu$ the maximum stable Courant number: ERK(4,2) 4.1471, ERK(8,2) 8.3132, ERK(5,3) 4.8111, ERK(4,4) 2.7852 (§2.1, Eq. 2, Table 1). **Stated**
6. With high-order spatial discretizations of compressible flow, stability, not accuracy, limits the explicit step (§2.1). **Stated**
7. Error-based step: a PID controller with $\mathrm{rtol}=\mathrm{atol}=10^{-6}$; the controller formula and exponents are not printed (§2.1, Eq. 3). **Stated**
8. The scalar relaxation equation is solved in double precision to tolerance $10^{-12}$ (§2.2). **Stated**
9. Among seven root finders, on homogeneous isotropic turbulence (turbulent Mach 0.6, $Re_\lambda=100$, DG degrees 2, 3, 7) and the 3D cylinder (Mach 0.1, three Reynolds numbers), run for 1,000 steps with RK4, only the secant method succeeds in every global and local case (§2.2, Tables 2–3). **Shown**
10. Newton and simplified Newton are the least reliable and fail reproducibly in several cases, even with up to 1,000 iterations (§2.2). **Shown**
11. All simulations of Table 4 are stable without relaxation, although then the fully discrete scheme carries no entropy-stability guarantee (§3). **Shown**
12. Relaxation (global or local) needs more function evaluations than no relaxation, and the two variants need a similar number; hence relaxation raises wall time (§3, Table 4). **Shown**. Table 4 has exceptions: SSP3(2)4[3S*+] on the CRM needs 1,352 evaluations with global relaxation and 1,356 without, and three wall times with relaxation are lower than without.
13. When the evaluation counts with and without relaxation are close, the wall-time difference comes from the scalar solve for $\gamma_n$ (§3). **Stated**
14. At third order the error-controlled schemes are substantially more efficient than the CFL-controlled ERK(5,3). For example, on the front wing without relaxation they need 4,250 evaluations and $1.41\times10^3$ s, against 7,135 evaluations and $2.30\times10^3$ s (§3, Table 4). **Shown**
15. The fifth- and sixth-order error-controlled BSRK(8,5) and VRK(9,6) are faster than the second- and third-order CFL-controlled schemes: $1.4149\times10^3$ s and $1.4116\times10^3$ s against $2.1347\times10^3$ s for ERK(4,2) on the front wing without relaxation (§3, §4, Table 4). **Shown**. It does not hold for every case: on the CRM with relaxation, VRK(9,6) ($1.4170\times10^2$ s global) is slower than ERK(4,2) ($1.4108\times10^2$ s).
16. With CFL control, relaxation leaves the evaluation count almost unchanged (ERK(4,2) on the front wing: 6,624 / 6,636 / 6,628), which "seems to indicate" $\gamma_n$ very close to 1. With error control the count rises, from 4,250 to 5,648 / 5,652 on the front wing, about +33% (§3, Table 4). **Shown** (data); the $\gamma_n\approx1$ reading is **Stated** ($\gamma_n$ is not reported)
17. No trend with the order of the time integrator is observed (§3). **Shown**
18. Relaxation guarantees entropy stability of the fully discrete algorithm (§4). **Stated**
19. If entropy stability is sought, high-order relaxation schemes with an error-based controller cost practically as much as lower-order schemes (§4). **Shown** (from Table 4)
20. RK4, BSRK(4,3) and BSRK(8,5) are work-horses of commercial and national-laboratory compressible-flow solvers (§2.1). **Stated**
21. Wall times are averages of three runs of 600 steps from a fully developed flow on 512 cores of Shaheen XC40 (§3). **Stated**

Unreported anomaly: on the front wing all five error-controlled schemes, with
4 to 9 stages, print identical evaluation counts (4,250 without, 5,648 global,
5,652 local relaxation). The counts are also hard to reconcile with "600 time
steps" (ERK(8,2) on the CRM prints 1,000 evaluations).

# Printed slips

- Table 4 header "WTC [s]" against the text's "wall-clock time (WCT)" (p. 4).
- §2.2: "We solve the two problems by using six different configurations", but Table 3 (cylinder) has three; the six refer to Table 2 only.
- §2.1 cites BSRK(4,3) to refs [13, 9], neither of which is the original Bogacki–Shampine paper (which is not in the reference list).
- CRM angle of attack printed "$AoA = 2.75^0$" (superscript zero for the degree sign).
- "throughly tested" (§2.1), "homogenous" (§4); §3 "This seems to indicate that with the current CFL-based controller leads to a time step …" is ungrammatical.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u^n$, $u(t)$ | $y_n$, $y(t)$ | |
| $\Delta t$, $\Delta t_{n+1}$ | $h$, $h_{n+1}$ | |
| $y_i$ | $Y_i$ | stage values (agrees up to case) |
| $A$, $b$, $c$ | $A$, $b$, $c$ | agrees |
| $\tilde\gamma_n$, $\tilde\gamma_{n,\kappa}$ | $\gamma_n$, $\gamma_{n,\kappa}$ | relaxation parameter (global; cell-local, page-local) |
| $u^{n+1}_{\tilde\gamma}$ | $y^\gamma_{n+1}$ | relaxed update; the note does not state whether time advances by $\gamma_nh$ or $h$ |
| $\eta$, $\eta_\kappa$ | $\eta$, $\eta_\kappa$ | entropy; cell-local part page-local |
| $\mathrm{CFL_d}$ | $\nu$ | desired (maximum stable) Courant number |
| $\sigma$ | same (page-local) | safety factor 0.95 |
| $\beta$ | $\beta_1,\beta_2,\beta_3$ | PID coefficient vector; values not printed |
| $\mathtt{atol}$, $\mathtt{rtol}$ | $\mathrm{atol}$, $\mathrm{rtol}$ | |
| $err^{n+1}$ | $\mathrm{err}_{n+1}$ | |
| $\varepsilon$ | same (page-local) | **collision**: root-finder tolerance $10^{-12}$, not the registry stiffness parameter |
| $p$ | same (page-local) | **collision**: DG polynomial degree, not the classical order |
| ERK($s$,$p$) etc. | same | (stages, order) |

# Reference list

The note prints 16 references in numbered style ([1]–[16]). The list is merged
complete into the [bibliography](/bibliography.md), with `citedby` this slug.
Ref. [1] (Al Jahdali et al., Comput. Math. Appl. 118, 2022) shares this
source's author and year but is a different work; it takes the suffixed key
`aljahdali-2022-b` so that it is not mistaken for this ingested source.
Ref. [13] (Ranocha et al., Commun. Appl. Math. Comput., printed with the
online year 2021 and no volume or pages) is the ingested
[Ranocha et al. (2022)](/sources/ranocha-2022.md) and is merged into its
entry.
Incomplete items: [1] has no pages, and [11] (Persson chapter) prints no book
title or editors. [15] prints DOI 10.2514/6.2019-3725 with "AIAA SciTech 2019
Forum"; the venue is unverified. No printed duplicates.

# Pages created or updated

Chunk 2 (2026-10-19). This source is cited on:

* [Embedded Runge–Kutta pairs and the FSAL property](/methods/embedded-runge-kutta-pair.md)
* [Entropy stability and conservation of the fully discrete scheme](/properties/entropy-stability.md)
* [Fully discrete cell entropy inequality of third-order Runge–Kutta DG](/results/fully-discrete-cell-entropy-inequality.md)
* [Low-storage Runge–Kutta methods](/methods/low-storage-runge-kutta.md)
* [Relaxation Runge–Kutta methods](/methods/relaxation-runge-kutta.md)
* [Step-size control: error-based controllers, PID filters and CFL control](/methods/step-size-control.md)
