---
type: Result
title: "Divergence source at collocated 2:1 seams"
description: "A collocated scheme with exact interior divergence loses it at 2:1 seams: the seam injects a source that converges in h but grows in t at fixed h, and no local fix was found."
status: hypothesis
aliases: [seam div(B) source, accept-truncation]
tags: [amr, coarse-fine-interface, divergence-constraint, collocation, ghost-fill]
timestamp: 2026-10-08T00:00:00Z
---

# Divergence source at collocated 2:1 seams

**Setting.** Take a collocated scheme whose discrete curl and divergence are
built from one shared antisymmetric derivative primitive. On a uniform
tensor-product grid the derivatives commute, and a field evolved through
the curl, $\partial_t B_h = -C_h^{\mathrm{c}} E_h$, keeps
$$D_h^{\mathrm{c}} C_h^{\mathrm{c}} = 0$$
identically ([notation](/notation.md)). This is the exact-algebraic class of
[exact discrete divergence](/properties/exact-discrete-divergence.md), and
it is reached here without staggering.

**Claim** ([Zaghi (2026)](/sources/zaghi-2026.md), a high-order
centered-FD Maxwell solver; `status: hypothesis`). At a 2:1 coarse–fine
seam the identity fails. The coarse side differences with $H$, the fine side
with $h$, so the composite operator is no longer a tensor product and the
commutation breaks. The seam then injects a divergence source on a skin a
few cells wide. Its behavior:

* **convergent in $h$.** With a ghost fill $\Gamma$ of value accuracy
  $O(h^q)$, the seam-skin curl errs at $O(h^{q-1})$ and the divergence
  production rate is $O(h^{q-2})$. Tricubic fill ($q = 4$) gives a
  production rate converging at exactly $p_{\mathrm{obs}} = 2$ on step-1
  ladders, and $p_{\mathrm{obs}} = 1.15$, $1.62$ for matched-time maxima
  (16/32/64, sixth-order interior). The solution on the skin drops to third
  order;
* **unbounded in $t$ at fixed $h$.** On a source-free pulse,
  $\max|D_h^{\mathrm{c}} B_h|$ goes from 6.9 to 1002 in 100 steps. The growth
  is independent of $\Delta t$, so it is not a CFL instability;
* **a constraint violation, not an energy instability.** The field energy
  stays flat (−3%) while the divergence grows 145×;
* **scheme-universal.** The finite-volume version reproduces it to 4–5
  significant figures. [Refluxing](/methods/refluxing.md) has no effect on
  it.

## What does not remove it

Five fix classes were ruled out with evidence:

| Class | Idea | Outcome |
|---|---|---|
| matched ghost values | build fine ghosts so both sides see one interface derivative | no improvement (the construction was one-dimensional in the normal direction) |
| single-valued flux values | enforce one $B$-flux at the seam | null: coarse and fine fluxes already agree to 0.24%, so the defect is the **operator**, not the values |
| matched-difference seam operator | a dedicated seam stencil pair making $D_h^{\mathrm{c}} C_h^{\mathrm{c}}$ telescope to order 6 across the jump | **eigenvalue-unstable** ($6.2\cdot10^{18}$ by step 100) |
| full GLM (Dedner, with parabolic damping) | transport and damp the error | never bounds it; see [GLM](/methods/glm-divergence-cleaning.md) `## Contradictions` |
| SBP + weak SAT | energy-stable interface coupling | analysis only: it bounds the energy, which is already bounded, and not the divergence |

Two lessons stand out. First, **telescoping exactness and time stability are
independent conditions**: the one construction that restores the divergence
structure across the jump loses stability. That is the instability that
non-SBP interface treatments are known for
([SBP-preserving interpolation](/operators/sbp-preserving-interpolation.md)).
Second, restriction-compatible ghost fills cannot rescue the order
([point-value restriction bound](/results/point-value-restriction-compatibility.md)).

The record resolves the problem as **accept-truncation**: a run-time monitor
on the seam divergence, plus GLM as a delay (about 5.5× margin) rather than
a cure. The only route to an exact seam bound it names is parked: switch to
staggered face/edge storage at the seam, with discrete Stokes telescoping
([staggered grid](/definitions/staggered-grid.md)).

## Relation to the compiled corpus

* It is evidence, not proof, for the cell-collocated row of the
  [transfer locality limits](/results/transfer-operator-locality-limits.md)
  ("not found / not found"). The record's own judgment, "no local
  collocated-FD fix exists", is an induction over five failed classes, not
  a theorem.
* **The constraint class decides what a seam does.** In a scheme that holds
  no divergence exactly anywhere (WENO flux-divergence form with GLM, in the
  same record), the seam error sits at the interior truncation level and is
  described as bounded on short runs. In the exact-interior scheme the seam
  is the *only* defect, and it grows. The two verdicts do not contradict
  each other. *Compiler hypothesis:* upwind dissipation damps the
  grid-oscillation modes in which the centered scheme's seam source grows.
  This is untested: no long-horizon, fixed-$h$, source-free seam test exists
  for the upwind scheme.

* **The interior identity is published; its seam behavior is not.**
  [Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md)
  hold $D_h^{\mathrm{c}} C_h^{\mathrm{c}} = 0$ at fourth order on uniform
  grids and defer AMR to future work. In this corpus no published
  collocated scheme with exact divergence has been run across a 2:1 seam.
  This result therefore stands on the record alone.

## Revisions in the record

* An earlier close-out called the post-fix seam divergence "bounded, not
  secular", measured over 4–19 steps. A 100-step run on the same instrument
  then showed the secular growth above. The later, longer measurement is
  the record's final position.
* Two early diagnoses were retracted after better instruments existed:
  * a "first-order divergent" seam ($p_{\mathrm{obs}} \approx -1$), in fact
    caused by a ghost layer that was never refreshed and by a source term
    whose divergence scales like $h^{-2}$;
  * a seam-excited grid-oscillation instability at a 1:1 seam, in fact
    stale stage-buffer ghosts
    ([time coupling](/properties/exact-discrete-divergence.md)).
* The lesson is about instruments: an order study of a seam divergence
  needs a source-free, divergence-free initial state and matched physical
  times.

# Citations

1. [Zaghi (2026)](/sources/zaghi-2026.md): issue #21 (error chain, E0–E2, N3–N5), #29 (fix classes, the 100-step horizon, the energy diagnostic, resolution), #30 (Route 2), #31 (1:1 seam); `forest.md` §"The 2:1 seam is not div-free".
2. [Tóth & Roe (2002)](/sources/toth-roe-2002.md): the cell-collocated locality assertion this result bears on.
3. [Mattsson & Carpenter (2010)](/sources/mattsson-carpenter-2010.md): the SBP interface framework whose absence explains the matched-operator instability.
4. [Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md), §§3, 6, 8.
