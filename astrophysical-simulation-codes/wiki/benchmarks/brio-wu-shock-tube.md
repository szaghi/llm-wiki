---
type: Benchmark
title: "Brio–Wu MHD shock tube"
description: "The one-dimensional MHD Riemann problem of Brio and Wu with normal field 0.75 and adiabatic index 2, whose fast rarefactions, compound wave, contact and slow shock test MHD Riemann solvers and the variables in which states are reconstructed."
status: established
aliases: [Brio-Wu, Brio and Wu shock tube]
tags: [benchmark, mhd, riemann-solver, verification]
timestamp: 2026-10-13T00:00:00Z
---

# Brio–Wu MHD shock tube

**Set-up.** A 1D MHD Riemann problem with normal field $B_x = 0.75$ and
$\gamma = 2$ (Brio & Wu 1988). The left and right states are tabulated in
[Stone et al. (2008)](/sources/stone-2008.md), Table 2, and reproduced
from the original under Later uses (batch 9). Solutions are compared with high-resolution reference runs.

**Runs.**

* [Stone et al. (2008)](/sources/stone-2008.md), §8.2, Fig. 13. PLM, Roe,
  CTU, $t = 0.08$, reference solution with $10^4$ points. Shocks and
  contacts are captured in 2–3 zones. PPM gives small velocity
  oscillations, and the authors write that "our TVD limiters could be
  improved". The resolution is printed inconsistently: 800 zones in the
  text, 400 in the Fig. 13 caption.
* [Stone et al. (2020)](/sources/stone-2020.md), §3.3.3, Fig. 15.
  $N = 256$, HLLD, characteristic reconstruction, $t = 0.1$, reference
  with $N = 8192$. Reconstruction in primitive
  variables gives significant oscillations behind the right-moving fast
  rarefaction, so characteristic reconstruction is needed; RK3+PPM gives a
  slightly sharper rarefaction head and foot.

The two sources print different output times (0.08 and 0.1).

**What it shows.** Both sources use it to examine oscillations next to
MHD waves: [Stone et al. (2008)](/sources/stone-2008.md) attribute residual
PPM oscillations to the limiters, and
[Stone et al. (2020)](/sources/stone-2020.md) show that the choice of
reconstruction variables decides whether they appear. No error norms are
reported. See also [approximate Riemann solvers](/methods/approximate-riemann-solvers.md).

## Later uses (batch 3)

* [Stone et al. (2026)](/sources/stone-2026.md), §3.2, Fig. 3 (right);
  [AthenaK](/software/athenak.md), on a CPU. 200 cells, RK2+PLM against
  RK3+PPM4, reference with 2000 cells (RK3+PPM4); reconstruction in
  primitive variables, since characteristic reconstruction is not
  implemented in AthenaK (§3). The two runs are similar, with "small
  amplitude ringing near the compound wave at x = 0" that characteristic
  reconstruction would reduce. Output time not printed (the plot shows
  $-0.15 < x < 0.25$).
* [Lesur et al. (2023)](/sources/lesur-2023.md), §4.2, Fig. 6;
  [IDEFIX](/software/idefix.md). A **variant with $\gamma = 5/3$**, with an
  "initial condition identical to Mignone et al. (2007)"; the states are
  not printed, and Fig. 6 shows $B_x = 0.75$. Roe, PLM (primitive
  variables), RK2, 500 points, against a [PLUTO](/software/pluto.md) 4.3 Roe run with 8000
  points: "excellent agreement", with a "small amplitude oscillation of the
  post-shock velocity that is typical of the primitive variable
  reconstruction". 1D, so the EMF reconstruction is not exercised. Visual
  only.
* [Caddy & Schneider (2024)](/sources/caddy-2024.md), §3.1.4, Table 2,
  Fig. 6; [Cholla](/software/cholla.md). The standard set-up, $\gamma = 2$,
  $B_x = 0.75$, $t = 0.1$; run in 3D on a $1\times1\times1$ domain with
  $512\times16\times16$ cells along each axis and in both orientations,
  with "identical results"; VL+CT, HLLD. PPM (Felker & Stone 2018) gives
  "oscillations in the solution when limiting in either the primitive or
  characteristic variables", PLM gives none; this PPM "significantly
  reduces oscillations" compared with the PPM of Stone et al. (2008).
  Visual only, no reference-solution overlay.

A relativistic analogue, Balsara's test 1 ($B_x = 0.5$, $\gamma = 2$,
states given in specific internal energy), is run by
[GRaM-X](/software/gram-x.md)
([Shankar et al. (2023)](/sources/shankar-2023.md), §IV A, Table I,
Figs. 2–3): 1600 points, TVD-minmod, HLLE, RK4, CFL 0.8, $t = 0.4$, against
an exact solver; all five waves are captured, maximum Lorentz factor
about 1.458; visual only. Its states differ from Brio–Wu's, so it is a
different problem, not a run of this benchmark.

The output times are now 0.08 (Stone et al. 2008) and 0.1 (Stone et al.
2020, Caddy & Schneider 2024); AthenaK's is not printed. IDEFIX's
$\gamma = 5/3$ run is a variant of the set-up, not a conflict with the
$\gamma = 2$ definition above: the paper states its own initial condition.

Oscillations next to the waves are now reported by four codes, and their
reports **qualify** each other rather than conflict. In primitive
variables, AthenaK (RK2/RK3, PLM and PPM4) and IDEFIX (RK2, PLM) see small
oscillations, as Stone et al. (2020) found for primitive reconstruction in
Athena++. Cholla sees PPM oscillations even with characteristic limiting,
whereas Stone et al. (2020) present characteristic reconstruction as the
cure. The configurations differ, so this is not recorded as a
contradiction: Cholla's PPM runs inside the VL+CT predictor–corrector at
$N = 512$, while the Athena++ run uses the method-of-lines integrators
(RK3 is named) at $N = 256$, and Stone et al. (2020) do not state that their
characteristic RK3+PPM run is free of oscillations, only that it gives a
slightly sharper rarefaction. What the four sources share is that PPM's
behaviour on this test depends on the integrator, the limiter and the
reconstruction variables together.

## Later uses (batch 9)

### The problem in its primary source

[Brio & Wu (1988)](/sources/brio-1988.md), §V, Figs. 2–6, define the
problem as a test of their Roe-type upwind MHD scheme.

* **States** (read at 300 dpi). Left $\rho = 1$, $\mathbf v = 0$, $p = 1$,
  $B_y = 1$; right $\rho = 0.125$, $\mathbf v = 0$, $p = 0.1$, $B_y = -1$;
  $B_x = 0.75$, $\gamma = 2$; $v_z$ and $B_z$ are not printed (coplanar, so
  zero). The hydrodynamic data are "identical to those in Sod's shock tube
  problem" (see [Sod shock tube](/benchmarks/sod-shock-tube.md)). These are
  the states the Set-up above defers to Stone et al. (2008), Table 2. Units
  carry no $4\pi$.
* **Run parameters and output time.** 800 grid points with $h = 1$,
  $\Delta t = 0.2$ (Courant number about 0.8), output after 400 steps, the
  discontinuity at the middle. The paper prints no dimensionless time: the
  output is at $t = 80$ on a domain of length 800, which on a unit domain is
  **$t = 0.1$** (derived at ingestion). The 0.1 of Stone et al. (2020) and
  Caddy & Schneider (2024) matches this derived time; the 0.08 of Stone et
  al. (2008) is a different choice. The original's 800 points agree with
  the 800 zones of Stone et al.'s text, not the 400 of their caption.
* **Wave structure** (Fig. 2). To the left a fast rarefaction and a
  **slow compound wave** (a slow shock with an attached slow rarefaction);
  to the right a contact, a slow shock and a fast rarefaction; checked with
  Riemann invariants and jump conditions. The transverse field changes sign
  across the slow shock of the compound wave, an intermediate shock that
  "all numerical schemes tested" admit (§VI).
* **Why the compound wave exists** (§VI). With eigenvectors renormalized to
  stay complete where the transverse field vanishes, the derivative of the
  eigenvalue along its eigenvector is proportional to the transverse field
  near its zero, for the fast field if $c_s < c_A$ and the slow field if
  $c_s > c_A$: ideal MHD is **nonconvex**, and shocks with attached
  rarefactions of the same family follow. The rarefaction tail predicted
  from the numerical left state of the slow shock ($\rho = 0.6965$,
  $v_x = 0.5987$, $v_y = -1.583$, $B_y = -0.5341$, $p = 0.5157$) agrees with
  the second-order upwind run (0.6963, 0.5997, −1.578, −0.5341, 0.5133):
  "The agreement is excellent." The "compound wave" in the description of
  this page is this slow compound wave.
* **Schemes compared.** The second-order upwind scheme (Harten's approach,
  artificial compression on the linearly degenerate field) against
  Lax–Wendroff with Lapidus viscosity (undershoot at the rarefaction tail,
  oscillations around the compound wave, contact over 10–15 points),
  Lax–Friedrichs (slow shock over about 20 points; with 20,000 points it
  coincides with the upwind result except at the contact) and FCT at
  Courant number about 0.4 (oscillations in the plateaus, worse at 0.8). For
  $\gamma = 2$ the upwind scheme uses an exact Roe matrix; the
  arithmetic-average variant for general $\gamma$ agrees "up to 4
  significant digits" in constant states. No error norms.
* **Variants in the same paper.** Right $B_y = -0.4$: an "almost
  stationary slow intermediate shock", which Lax–Wendroff could not run
  stably "with any value of artificial viscosity" (no figure). $B_x = 0$
  with a left density printed as 1000: a hydrodynamic Riemann problem in
  total pressure with a Mach 15.5 shock (Fig. 7; the printed density is
  recorded as printed on the Source page).

The original thus supplies the states, the $\gamma = 2$ definition and the
basis for $t = 0.1$; IDEFIX's $\gamma = 5/3$ run remains a variant. The
oscillation reports above concern later schemes and are not addressed by
the original, whose comparison is with central and FCT schemes.

### A γ = 5/3 variant

* [Ryu & Jones (1995)](/sources/ryu-1995.md), §4, Figs. 5a, 6a (test 5a; arXiv preprint). An early **$\gamma = 5/3$ variant**: the Brio–Wu states $(\rho, v_x, v_y, v_z, B_y, B_z, p) = (1, 0, 0, 0, 1, 0, 1)$ left and $(0.125, 0, 0, 0, -1, 0, 0.1)$ right, $B_x = 0.75$, $t = 0.1$, 512 cells, Harten TVD with a Roe-type solver, against a nonlinear MHD Riemann solver (the seventh entry is printed "E" but is the pressure; see the Source page). With 8192 cells (Fig. 6a) the slow compound wave is read as a "2-4" intermediate shock (Alfvénic Mach number $1.03 \to 0.910$) followed by a slow rarefaction, whereas an exact solver that allows rotational discontinuities gives a rotational discontinuity plus a slow shock (§5). Like IDEFIX's run, a variant of the set-up, not a conflict with the $\gamma = 2$ definition.

# Citations

1. [Stone et al. (2008)](/sources/stone-2008.md), §8.2, Table 2.
2. [Stone et al. (2020)](/sources/stone-2020.md), §3.3.3.
3. [Stone et al. (2026)](/sources/stone-2026.md), §3, §3.2 (arXiv v1).
4. [Lesur et al. (2023)](/sources/lesur-2023.md), §4.2 (arXiv v1).
5. [Caddy & Schneider (2024)](/sources/caddy-2024.md), §3.1.4 (arXiv v2).
6. [Shankar et al. (2023)](/sources/shankar-2023.md), §IV A (arXiv v2).
7. [Brio & Wu (1988)](/sources/brio-1988.md), §§V–VII, Figs. 2–10.
8. [Ryu & Jones (1995)](/sources/ryu-1995.md), §§4–5, Figs. 5a, 6a (arXiv preprint).
