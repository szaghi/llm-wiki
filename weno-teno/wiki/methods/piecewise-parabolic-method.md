---
type: Method
title: "Piecewise parabolic method (PPM)"
description: "The piecewise parabolic method reconstructs face values from cell averages with limited parabolas. In this bundle it is a reconstruction option of two GPU finite-volume codes, applied to primitive variables in two limiter families; the page records its observed orders on linear waves, its dissipation and its loss of convergence on MHD waves."
status: established
aliases: [PPM, piecewise parabolic method, PPM4, PPMX, extremum-preserving PPM, Colella–Woodward PPM]
tags: [reconstruction, finite-volume, limiting, mhd, software]
timestamp: 2026-10-24T05:41:00Z
---

# Piecewise parabolic method (PPM)

The **piecewise parabolic method** (Colella & Woodward 1984, as recalled by both sources) is a
finite-volume reconstruction. From the cell averages $\bar u_i$ it builds, as its name says, a
limited parabolic profile in each cell, and the profile supplies the interface states
$u^\mp_{i+1/2}$ of a Godunov-type flux. In this bundle PPM appears only as a reconstruction
option of two performance-portable codes,
[IDEFIX](/software/idefix.md) ([Lesur et al. (2023)](/sources/lesur-2023.md)) and
[AthenaK](/software/athenak.md) ([Stone et al. (2026)](/sources/stone-2026.md)). Both apply it to
primitive variables inside a reconstruct–solve–average (or reconstruct–solve–advance)
finite-volume scheme. Neither paper prints its formulas, so this page records the variants as
named and what the two codes measure with them.

## Variants

Two limiter families appear, and the label "4" in PPM4 is a name, not an order.

- **Original Colella–Woodward limiters.** AthenaK's "PPM4" is PPM with the limiters of
  Colella & Woodward (1984) (§3).
- **Extremum-preserving limiters.** IDEFIX offers "extremum-preserving PPM", citing Colella &
  Woodward (1984) and Colella & Sekora (2008) and calling it "4th order accurate on regularly
  spaced grids". The code is nevertheless "at most globally second order" (Lesur et al., §2.3,
  footnote 1). AthenaK's "PPMX" is PPM with the extremum-preserving limiters of McCorquodale et al.
  (2015) (Stone et al., §3).

**Variables.** Both codes reconstruct primitive variables without
[characteristic decomposition](/methods/characteristic-decomposition.md). IDEFIX reconstructs
$(\rho,v,B,p)$, a choice said to keep "the basic physical constraints (density and pressure
positivity for instance)", with no proof given (§2.3). AthenaK has no characteristic
reconstruction, "largely because of the complexity of the implementation for general relativistic
flows" (§3). In IDEFIX's orbital advection the reconstruction can be PPM or linear (§4.3).

The other options of the two codes are piecewise-constant and piecewise-linear reconstruction
(van Leer-limited in IDEFIX, PLM in AthenaK; see [MUSCL–Hancock](/methods/muscl-hancock.md)),
Čada and Torrilhon's LimO3 in IDEFIX, and [WENO-Z](/methods/weno-z.md) in AthenaK. The Riemann
solvers run from Rusanov ([Lax–Friedrichs](/methods/lax-friedrichs-flux.md)) through the
[HLL family](/methods/hll-riemann-solvers.md) to [Roe](/methods/roe-riemann-solver.md).

## Observed order on linear waves

"Order" here is the observed $L_1$ convergence rate of a whole scheme on a smooth linear wave.

- **Hydrodynamic waves (AthenaK).** On 1D entropy and sound waves over one period, RK3 with
  PPMX converges at fourth order, as does RK3 with WENO-Z, "until nonlinear effects or round-off
  dominate". RK3 with PPM4 and RK2 with PLM converge at second order. The results are stated to be
  identical to the corresponding figure of the original Athena paper (Stone et al., §3.1, Fig. 1;
  [linear acoustics tests](/benchmarks/linear-acoustics-tests.md)).
- **MHD waves (AthenaK).** RK3 with PPMX (or WENO-Z) converges at fourth order for the slow and
  Alfvén waves, but the fast wave converges only at second order "even in one dimension". PPM4 and
  PLM give second order for all waves. The authors state that this reproduces the Athena++ paper;
  no cause for the fast-wave rate is given (§3.2, Fig. 3).
- **MHD waves (IDEFIX).** With HLLD, LimO3 and PPM (with RK3) have lower errors than linear
  reconstruction, but PPM stops converging at high resolution. The effect is strongest for the
  slow mode, whose error levels off at about $10^{-2}$. The authors report the same lack of
  convergence with HLL and in Athena++ with primitive reconstruction, and conclude that "the LimO3
  scheme should be preferred" because it converges at second order at every resolution tested
  (Lesur et al., §4.2, Fig. 8). In a Hall-dominated shock they state, without showing it, that
  second order is "strictly" recovered with LimO3 or PPM (§4.2, Fig. 15).

## Dissipation and use in the tests

- **Least diffusive option of a second-order code.** In IDEFIX's
  [double Mach reflection](/benchmarks/double-mach-reflection.md) at $1920\times480$, LimO3 and
  PPM, "the least diffusive schemes in IDEFIX", give a more vigorous jet with incipient
  Kelvin–Helmholtz rolls (§4.1, Fig. 3;
  [numerical dissipation](/definitions/numerical-dissipation.md)). On the
  [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md), RK3 with PPM and the Roe solver is the
  most accurate combination at a given resolution (§4.2, Figs. 10–11).
- **Primitive-variable ringing.** AthenaK's [Brio–Wu tube](/benchmarks/brio-wu-shock-tube.md)
  compares RK2 with PLM against RK3 with PPM4 on 200 cells, with a 2000-cell RK3 + PPM4 reference.
  Primitive reconstruction leaves small-amplitude ringing near the compound wave, which
  characteristic reconstruction "would significantly reduce", as the authors recall from the
  Athena++ paper (§3.2, Fig. 3). IDEFIX reports a small post-shock velocity oscillation in the same
  test, "typical of the primitive variable reconstruction" (Lesur et al., §4.2, Fig. 6).
- **Production runs.** AthenaK uses RK3 with PPM4, HLLC and its first-order flux-correction
  fallback for a supernova blast in a turbulent multiphase interstellar medium on $2048^3$ cells
  (§3.1, Fig. 2). It uses PPM4 with a third-order IMEX integrator for driven two-fluid
  (ion–neutral) turbulence on $1200^3$ cells (§3.4, Fig. 8).

## Qualifications

- No formula, limiter or face-value stencil of PPM is printed in either source, so the two
  extremum-preserving variants (Colella–Sekora in IDEFIX, McCorquodale et al. in AthenaK) cannot be
  compared from the bundle. "4th order" in IDEFIX refers to the reconstruction alone, and AthenaK's
  fourth order is an observed rate with RK3 on 1D linear waves.
- **Two codes, two MHD convergence behaviours.** On linear MHD waves IDEFIX's extremum-preserving
  PPM levels off, most strongly for the slow mode, while AthenaK's PPMX converges at fourth order
  for the slow and Alfvén waves. Lesur et al. add that Athena++ with primitive reconstruction shows
  the same loss, and Stone et al. state that their rates reproduce the Athena++ paper. Not recorded
  as a contradiction: the limiters differ, Lesur et al. do not say which Athena++ reconstruction or
  resolution range they mean, and neither paper runs the other's variant. A run of both PPM variants
  in one code on the same MHD wave up to the resolutions of IDEFIX's plateau would decide it.

# Citations

- [Lesur et al. (2023)](/sources/lesur-2023.md) — §2.3 (footnote 1), §4.1 (Fig. 3), §4.2 (Figs. 6, 8, 10–11, 15), §4.3: extremum-preserving PPM in IDEFIX, loss of convergence on MHD waves, dissipation.
- [Stone et al. (2026)](/sources/stone-2026.md) — §3, §3.1 (Figs. 1–2), §3.2 (Fig. 3), §3.4 (Fig. 8): PPM4 and PPMX in AthenaK, observed orders on hydro and MHD linear waves, use in production runs.
