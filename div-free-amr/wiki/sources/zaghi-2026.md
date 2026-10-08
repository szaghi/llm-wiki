---
type: Source
title: "Zaghi (2026) — ADAM verification record: seam divergence in collocated AMR solvers"
description: "Verification docs and seam-divergence research threads of the ADAM code: exact interior divergence lost at 2:1 seams, a point-value restriction bound, five failed local fixes, and GLM's limits."
resource: "https://github.com/szaghi/adam (commit d99e61f012efd7a6eebda6b13b433c2da64e3a79; issues #21, #29, #30, #31)"
source_kind: code
authors: [Zaghi S.]
year: 2026
venue: "ADAM repository: documentation and issue tracker"
local_file: "~/llm-wiki/div-free-amr/raw/docs/zaghi-2026/"
tags: [amr, coarse-fine-interface, divergence-constraint, glm, collocation, ghost-fill, verification]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

The verification record of ADAM, a GPU-oriented block-AMR library with two
solvers that matter here ([software page](/software/adam.md)):

* **PRISM** (Maxwell). Collocated, centered high-order finite differences
  that evolve $B_h$ through a curl. Its curl and divergence share one
  antisymmetric derivative primitive, so
  $D_h^{\mathrm{c}} C_h^{\mathrm{c}} = 0$ holds identically on uniform grids.
* **FLUME** (MHD). WENO finite differences in flux-divergence form, with GLM
  or EGLM cleaning. It holds no discrete divergence exactly anywhere.

The record is the author's own working log, the docs plus the issue threads.
Its central result concerns PRISM's 2:1 seams. There the exact interior
identity breaks and the seam injects a divergence source. The source
converges under refinement but grows in time at fixed resolution. Five
classes of local fix were ruled out with evidence, and the issue was
resolved as **accept-truncation** with a run-time guard-rail. A staggered
seam is parked as the only exact route.

Every claim compiled from this source carries `status: hypothesis`
(bundle law: claims from the human's own notes).

# Scope of the read

Captured verbatim to `raw/docs/zaghi-2026/` on 2026-10-08:

* **Docs** at commit `d99e61f0`:
  * `docs/applications/flume/{index,numerics,models,verification}.md`
  * `docs/applications/prism/verification.md`
  * `docs/tests/prism-regression.md`
  * `docs/guide/{forest,forest-cookbook}.md`
  * the oracle `src/tests/flume/verification/mhd/divb-peak/divb_peak_oracle.py`.
* **Issue threads, full, with comments:** #21 (seam divergence control,
  2026-07-02/03), #29 (fix-class survey, closed accept-truncation), #30
  (Route 2, parked), #31 (inter-realm 1:1 seam leak).
* **Run data:** FLUME div(B) histories (columns
  `it time max_divb l1_divb seam_max_divb`) of the divb-peak AMR run, the
  field-loop AMR runs at 32/64 and the uniform field-loop runs at 64/128,
  plus the divb-peak input.

Not read, so not captured: #13, the predecessor thread (149 KB). #21
restates the parts of #13 that this record relies on. The internal SOTA
review that #21 names (`sources/papers_20260702_telescoping_cellcentered_seam.md`)
is not part of the capture. The issue comments are signed as generated with
an AI assistant on the author's account; they are the author's record.

# Key claims

1. **Exact interior, broken seam** (#21 §2, #29, `forest.md`). PRISM's
   control runs hold the seam-free divergence at $2.0\cdot10^{-19}$ (coil
   case) and at exactly 0.0 (source-free pulse). A 2:1 seam breaks the
   commutation that makes $D_h^{\mathrm{c}} C_h^{\mathrm{c}} = 0$: the coarse
   side differences with $H$, the fine side with $h$. The result is a
   divergence source on a skin of about 3 cells
   ([seam divergence source](/results/collocated-seam-divergence-source.md)).
2. **Error chain** (#21 M-A, close-out). If the ghost fill $\Gamma$ has
   value error $O(h^q)$, the seam-skin curl has error $O(h^{q-1})$ and the
   divergence production rate is $O(h^{q-2})$. Measured on the pulse case
   (matched physical time, order 6):
   * injection ($q = 1$): $p_{\mathrm{obs}}$ flat ($\approx 0$);
   * restriction-compatible ($q = 2$): $\approx +0.1$;
   * tricubic ($q = 4$), after an infrastructure fix: $+1.15$, $+1.62$
     (12.650 / 5.700 / 1.852 at 16/32/64).
   Step-1 production ladders measure exactly $+2.0000$. The seam-skin
   solution is third order against the sixth-order interior.
3. **Restriction-compatibility bound** (#21 N0). With $R$ the 8-cell mean on
   point values, exact $R P = I$ is incompatible with reproducing
   quadratics, so compatibility caps the ghost order at $q = 2$
   ([Result page](/results/point-value-restriction-compatibility.md)).
   Confirmed by A/B: the compatible arm buys a constant factor and no slope.
4. **A binding defect was infrastructure** (#21 N3, N3.5). With three ghost
   layers, the coarse→fine exchange refreshed only one coarse donor layer
   (a floor where a ceiling was needed), so the outermost fine ghost layer
   was never refreshed after initialization. That stale layer produced a
   refinement-divergent signature ($p_{\mathrm{obs}} \approx -1$) that no
   ghost-fill order could fix. A second confound: in the coil case the
   discrete divergence of the imposed current scales like $h^{-2}$, which
   contaminates it as an order instrument. The source-free pulse case is
   the valid instrument.
5. **Growth in time at fixed $h$, and a revision inside the record.** #21
   closed (2026-07-03) calling the post-fix seam divergence "bounded, not
   secular". That was on 4–19-step windows. #29 then ran the same pulse
   instrument for 100 steps and measured $6.9 \to 1002$. It is
   $\Delta t$-independent (so not a CFL instability), and it survives
   tricubic fill. The record's final position, which `forest.md` adopts, is
   **convergent in $h$, unbounded in $t$ at fixed $h$**. The 100-step
   measurement supersedes the 19-step characterization; #21's sentence is
   left uncorrected in its own thread.
6. **A constraint violation, not an energy instability** (#29). On the
   baseline run the field energy stays flat (10155 → 9831, −3%) while
   $\max|D_h^{\mathrm{c}} B_h|$ grows 145×.
7. **Five fix classes ruled out** (#29):
   * matched ghost values (E1): red;
   * single-valued fluxes (E2): null, because the coarse and fine seam
     $B$-fluxes already agree to 0.24%;
   * a matched-difference seam operator (E3): it achieves order-6
     telescoping of $D_h^{\mathrm{c}} C_h^{\mathrm{c}}$ across the jump and is
     **eigenvalue-unstable** ($8.2\cdot10^{4}$ at step 25,
     $6.2\cdot10^{18}$ at step 100);
   * full Dedner GLM with parabolic damping (E): bounds nothing;
   * SBP + weak SAT (A, analysis only): it bounds energy, which is already
     fine, and not the divergence.
   The resolution is accept-truncation plus a guard-rail monitor.
   Telescoping exactness and time stability are independent conditions.
8. **Scheme universality and reflux** (#21 §2, #29). Flipping the pulse to
   finite volumes reproduces the runaway to 4–5 significant figures with
   reflux active. Reflux is bit-identical on and off for the seam
   divergence: conservation ≠ solenoidality
   ([refluxing](/methods/refluxing.md)).
9. **GLM at a growing seam source** (#21 E2/E2′, #29).
   * With injection fill, hyperbolic cleaning helped early, crossed over at
     about step 120, and ended 3.1× *worse* at step 200.
   * With tricubic fill there is no crossover over 200 steps (coil case;
     cleaned/uncleaned 0.18 → 0.88).
   * On the pulse at 100 steps, full Dedner damping never bounds the source.
     The sweep is monotone, and weaker damping is better: 858 at the
     strongest damping, 212 near pure hyperbolic.
   * #29 cites Koley 2011 for the absence of a discrete divergence bound.
   ([GLM page](/methods/glm-divergence-cleaning.md), `## Contradictions`.)
10. **Time coupling is part of exactness** (#31, `prism-regression.md`). A
    1:1 inter-realm seam is exactly divergence-free (0.0 for 100 steps)
    only when seam ghosts are filled at every Runge–Kutta stage. With
    end-of-step coupling the stage buffers read zero seam ghosts, and the
    divergence leaks ($4.56\cdot10^{2}$ in the negative control). The
    thread retracted two intermediate diagnoses before reaching this one:
    corner-ghost wrap, then a seam-excited grid-oscillation instability.
11. **FLUME (truncation/controlled class)**, from the docs.
    * Seam div(B) is described as "kept bounded" by GLM. MV-12 says it stays
      below the uniform-grid peak; the field-loop text says GLM "removes"
      it.
    * Rotated shock tube: $\delta B_\parallel = 2.79\cdot10^{-3}$ at 63.4°
      against Tóth's $3.7\cdot10^{-3}$.
    * Balsara–Spicer blast ($\beta = 2.5\cdot10^{-4}$, no limiter): the
      mixed GLM motivates EGLM by failing it. Under EGLM the flux-splitting
      scheme still fails at step 3; EGLM with HLLD completes it. No GLM + HLLD
      run is recorded, so the EGLM contribution is not isolated. EGLM's
      energy drifts by 3.0–4.4·10⁻⁴ on Orszag–Tang.
    * With damping, $\int\psi_h$ is not conserved across 2:1 faces.
    * GLM's upwinding damps an exactly static, discretely solenoidal
      diagonal field at fifth order: $8.5\cdot10^{-12}$ at 48 cells,
      $2.7\cdot10^{-13}$ at 96 (VV-5). Without divergence control the field
      stays at round-off.
    * The curl-form resistive flux adds no divergence on a uniform grid
      (VV-6, at round-off). The seam test is deferred.
12. **Seam machinery consistency.** Quadtree and octree reproduce the PRISM
    seam source to every printed digit (12.65004). A 2:1 inter-realm seam
    reproduces the single-realm run bit for bit, seam source included.
13. **Route 2, parked** (#30). The staggered face/edge field at the seam,
    with discrete Stokes telescoping, is named as the only route to an exact
    seam bound. It is not pursued unless a workload trips the guard-rail.

# Compiler analysis of the captured data

These are the compiler's reading of the run histories in `raw/`, not
claims of the source.

* **divb-peak with AMR** (GLM, $c_h = 5$, `glm_alpha = 0.4`, `min-cell`
  damping length). The seam column rises from 0 to $9.99\cdot10^{-3}$
  ($t = 0.05$) and $3.27\cdot10^{-2}$ ($t = 0.10$). It is the global
  maximum from $t \approx 0.35$, peaks at $0.119$ at $t = 0.40$, and ends at
  $7.58\cdot10^{-2}$ at $t = 0.5$. Over the same run the global $L_1$ falls
  from $7.23\cdot10^{-2}$ to $6.56\cdot10^{-3}$. The oracle's seam check
  asserts only three things: zero at step 0, never above the global
  maximum, positive at the end. Nothing in it asserts boundedness or decay.
  The run is too short to separate error arriving at the seam from error
  produced there.
* **Field loop.**
  * AMR runs: the seam maximum peaks at $9.75\cdot10^{-4}$ near
    $t \approx 0.38$ (64²), when the loop crosses the seam, not at the first
    step as the docs state. It ends at $3.48\cdot10^{-4}$ (64²) and
    $3.66\cdot10^{-4}$ (32²) at $t = 1$.
  * Uniform runs: the global maximum near $t = 1$ is $3.72\cdot10^{-4}$
    (64²) and $3.04\cdot10^{-4}$ (128²).
  * So FLUME's seam error sits at the level of its interior truncation
    error.
* **Synthesis.** The FLUME and PRISM seam verdicts ("bounded" and
  "unbounded at fixed $h$") do not contradict each other. They describe
  schemes in different classes of
  [exact discrete divergence](/properties/exact-discrete-divergence.md): in
  PRISM the seam is the only defect in an exact interior; in FLUME it is one
  truncation source among many. *Compiler hypothesis (untested):* FLUME's
  upwind dissipation damps the grid-oscillation modes where PRISM's seam
  source grows. The test that would decide it is a source-free solenoidal
  field crossing a static 2:1 seam, on a 32/64/128 ladder over long
  horizons.

# Unresolved citations

Cited without year or title, so they cannot be keyed without guessing:
"Mishra–Svärd" (the conservative-induction divergence bound, #29/#30),
"Cheng" (SBP–SAT extraction, #29), the Guzik dissertation (#21), and
"Wang 2018" (per-stage RK-weighted reflux, `forest.md`). Two mapped
identifications are compiler judgments:
* "Almquist–Wang–Werpers" is mapped to `almquist-2018`, the only work by
  that author trio in the record.
* `koley-2011` is kept separate; it may be the online-first form of
  `koley-2012`.

# Notation map

| ADAM | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| `div_h`, `compute_divergence_fd_centered` | $D_h^{\mathrm{c}}$ | collocated, sharing the `FD1_CC` primitive |
| `curl_h`, `compute_curl_fd_centered` | $C_h^{\mathrm{c}}$ | same primitive, hence $D_h^{\mathrm{c}} C_h^{\mathrm{c}} = 0$ on uniform grids |
| `div(B)`, `max abs div(B)`, `seam_max_divb` | $\max\lvert D_h B_h\rvert$ (seam-local when stated) | |
| `D` (electric displacement, PRISM) | written out in prose | collides with $D_h$; no registry symbol |
| seam ghost fill (`seam_ghost_fill`, `interp_seam_ghost`) | $\Gamma$, accuracy order $q$ | injection $q=1$, restriction-compatible $q=2$, tricubic $q=4$ |
| `R∘P = I`, `one_or_eight = 8` mean | $R P = I$, $R$ = 8-cell mean | |
| `c_h`, `c_r` / `glm_alpha` | $c_h$, damping via $c_p$ | PRISM `c_r` ∝ inverse damping strength |
| `psi` | $\psi_h$ | |
| `p_obs` | $p_{\mathrm{obs}}$ | |
| `ker D*` grid-oscillation mode | "grid-oscillation subspace" (prose) | after Ranocha 2019; no registry symbol |
| α / β coupling cadence | end-of-step / stage-coincident seam coupling | |

# Pages created or updated

* Created [Divergence source at collocated 2:1 seams](/results/collocated-seam-divergence-source.md).
* Created [Restriction-compatibility bound for point-value prolongation](/results/point-value-restriction-compatibility.md).
* Created [ADAM](/software/adam.md).
* Updated [Locality limits of divergence-preserving transfer](/results/transfer-operator-locality-limits.md): evidence for the cell-collocated row.
* Updated [SBP-preserving interpolation](/operators/sbp-preserving-interpolation.md): partial answer to the open structural question.
* Updated [GLM divergence cleaning](/methods/glm-divergence-cleaning.md): seam behavior, the accuracy cost on solenoidal data, EGLM evidence, `## Contradictions`.
* Updated [Exact discrete divergence](/properties/exact-discrete-divergence.md): the collocated exact instance and time coupling.
* Updated [Refluxing](/methods/refluxing.md): reflux is inert for the seam divergence.
* Updated [Field-loop advection](/benchmarks/field-loop-advection.md): GLM/AMR production evidence.
* Updated [Staggered grid](/definitions/staggered-grid.md): AMR evidence on the `Contradictions` development.
* Extended the [notation registry](/notation.md): $C_h^{\mathrm{c}}$, $R P = I$, $c_h$, $c_p$, $q$, $p_{\mathrm{obs}}$.

# Citations

1. `raw/docs/zaghi-2026/issues/issue-21.md`: body §§1–2, comments E0, E1a/E1b, E2, M-A, N0, N3, N3.5, N4, closing.
2. `raw/docs/zaghi-2026/issues/issue-29.md`: body, the E3 update, the 2026-07-06 status, the resolution.
3. `raw/docs/zaghi-2026/issues/issue-30.md` and `issue-31.md` (all comments).
4. `raw/docs/zaghi-2026/docs/`: `forest.md` §"The 2:1 seam is not div-free", `prism-regression.md`, `prism/verification.md`, FLUME `index.md` (known limitations), `numerics.md` (AMR, EGLM, positivity), `models.md` (GLM, EGLM), `verification.md` (MV-3, MV-8 to MV-12, MV-15, EV-2 to EV-4, VV-5, VV-6).
5. `raw/docs/zaghi-2026/data/`: div(B) histories (compiler analysis above).
