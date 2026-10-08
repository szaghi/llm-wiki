# #21 Seam divergence control for cell-centered PRISM — experiment-gated successor to #13

state: closed | opened: 2026-07-02T08:06:49Z | closed: 2026-07-03T07:28:28Z | author: szaghi
url: https://github.com/szaghi/adam/issues/21

> **Provenance.** This issue rebases the open remainder of #13 ("Coarse-fine interface machinery") onto corrected premises. #13 delivered its conservation scope (Phase A reflux + the §7.5 intra-realm AMR path, M0–M4) and is closed as complete-for-scope / superseded-for-the-rest. Its design history — the reformulation, the α/β cadence, the M-milestone log, Appendix H — stays there; **this issue does not restate it**. What migrates here: the divergence question (ex-Phase B), the ghost-fill question (ex-Phase C), the FNL firewall check (ex-M5), and the deferred carve-outs.
>
> **Ground truth for the premises:** `sources/papers_20260702_telescoping_cellcentered_seam.md` — a source-verified SOTA review (25/25 claims adversarially confirmed, 2026-07-02) of telescoping conservation and divergence control at 2:1 AMR jumps for collocated cell-centered FD/FV schemes.

---

## 1. Corrected premises (what changed since #13 was written)

#13 §2.1 rested on: *"cell-centered storage + interface machinery can preserve ∇·B = 0 across AMR jumps — yes, demonstrated by Flash-X Spark, BATSRUS cell-centered mode, Athena++ FluxCorrection."* The 2026-07-02 verification pass **falsifies the operative half of that claim**:

1. **Athena++'s telescoping FluxCorrection covers the cell-centered *conserved hydro* variables; its B is staggered CT** (Stone et al. 2020, ApJS 249:4) — i.e. the ∇·B guarantee there comes from the mechanism PRISM explicitly excludes.
2. **The genuinely cell-centered production MHD codes (PLUTO, Mignone FD-GLM, Freret–Groth CENO) do not achieve machine-zero seam div-B.** Their SOTA is GLM/Dedner divergence *cleaning*: the induction update stays in flux form (so reflux applies to the B rows like any conserved row), and div-B errors are **transported and damped — never zeroed** (Mignone, Tzeferacos & Bodo 2010, JCP 229, arXiv:1001.2832; Mignone & Tzeferacos 2010, JCP 229:2117).
3. **Telescoping conservation at the 2:1 jump is imposed, never emergent** — by Berger–Colella reflux (AMReX, Chombo, PLUTO Eqs. 48–49) or same-step flux replacement (Athena++). For cell-centered **FD** it is achievable *only* for flux-form schemes conformed at **flux points**, with a δF end-of-coarse-step correction (Wang et al. 2025, arXiv:2511.08335) — and enforcing it **caps global conservation-error convergence at 2nd order** ("any means to preserve the conservation will reduce the schemes to no more than second order").
4. **No published treatment makes a non-flux-form centered FD scheme telescope at a seam.** All surveyed constructions presuppose flux form. This is an absence of construction, not an impossibility theorem — none was found.
5. **Even ghost-fill interpolation needs an explicit conservation constraint to preserve order** (McCorquodale & Colella 2011 + Guzik: Σ fine = 2³ × coarse via constrained least-squares) — consistent with our own negative result that unconstrained linear prolongation made the seam leak *worse*.
6. A register-free alternative exists at medium confidence: **Freret–Groth heterogeneous blocks** (J. Sci. Comput. 79:176, 2019) — ghost cells stored at the neighbor's *native* resolution (hanging nodes), both sides evaluate the same face flux, "no need for an additional correction." Single-group, discrete proof deferred to a prior reference.

**Consequences:**
- #13 §4 (shared edge-E / `adam_edge_register_object`) stays dead — retired twice, now also premise-dead.
- #13's Phase-B acceptance — *pointwise ∇·B ≤ 1e-13 at seam cells* — is **retired as unsatisfiable under the cell-centered constraint**, not silently dropped. No surveyed method meets it without staggering.
- The correct acceptance frame is the field's: **seam div-B is a truncation-order quantity, verified by convergence under refinement and controlled by cleaning** — *unless* the gate experiment (§4, E0) shows the current leak is not truncation but a consistency defect, in which case flux-form seam machinery (premise 3) is the remedy.

## 2. What this issue inherits as verified fact (do-not-relearn list)

**Landed infrastructure (#13, on develop):** `adam_flux_register_object` as forest value component; α/β `coupling_cadence` (#16/#18); intra-realm AMR seam registration + 2:1 restriction + applied end-of-step reflux (M0–M4: `9975c50f`, `17b66028`, `b3eb6fc5`, `b7ae1ed3`, `c12d5fc5`); deterministic `AMR_GEO` primitive-box marker; oracles `rmf-amr` (fv, structural) and `rmf-amr-fd` (fd, div-B — **currently untracked**, must be committed); regression suite rmf / rmf-2realm / rmf-2realm-asymK / rmf-2realm-stagesync with CPU+FNL goldens.

**Verified findings:**
- Reflux now applies correctly (the SSP-RK `ark`-unallocated silent no-op is fixed, M4) and **does not move centered-FD seam div(B)** — bit-identical on/off (1.96e-8 both). Conservation and divergence are different defects requiring different mechanisms.
- The FD-path uniform-grid identity `div_h(curl_h) ≡ 0` (matched `FD1_CC` stencil pair) holds to round-off: control run (no seam) div(B) = 2.0e-19. The seam breaks it: 4.6e-7 at step 5, growing every step (3.7e-9 → 3.7e-6 over 10 steps).
- The leak is **fine-side only**, a ~2-cell skin on the seam-facing face; the coarse side (1/8-restricted ghosts) is clean. div(D) leaks *more* than div(B) (6.2e-8 vs 3.7e-9 at it=1) — coil-source coupling not yet isolated.
- One-sided (no-ghost-reach) seam div(B) is ~3× smaller than centered but still far above round-off (3.9e-9 vs 1.1e-8) — the leak is not purely a diagnostic-stencil artifact.

**Anti-patterns (do not retry):**
- Prolongation tuning: geometry-exact linear coarse→fine ghost-D prolongation made div(B) **worse** (1.7e-5 vs 3.7e-6 @ step 10). Matches the literature (unconstrained interpolation loses conservation/order).
- Post-stage `flx_f` write-back: a no-op once `dq` is formed (retired M4).
- Mean canonical `½(Fc+Ffs)`: the conservative restriction is the **fine-side** sum (Olivares §4.2.1).
- Unresolved and inherited: the **q(B) double-correction** question (reflux and any induction-share both target q(B); recommended row-partition is unverified) — only meaningful if the machinery path (§5) is taken.

## 3. Goals (redefined)

- **G1 — seam conservation (cell-centered, flux-form paths):** delivered for the intra-realm FV path by #13 M0–M4. Residual open items here: the closed-domain ∮F·n integration oracle (needs a bespoke closed-domain case; `rmf-amr` has Neumann BCs + coils), and — *gated, optional* — a Wang-style flux-point δF treatment for the FD path if E0 takes the machinery fork.
- **G2 — seam divergence control:** seam max|div(B)| (and div(D)) **converges under refinement at a defensible order and is bounded under cleaning**. Acceptance is a convergence ratio + a long-run boundedness check, not a pointwise 1e-13.

## 4. E0 — the gate experiment: convergence under refinement (RUN FIRST)

*Everything downstream forks on this measurement. No mechanism code before it.*

**Protocol** (on `rmf-amr-fd`, CPU, optimized `prism-cpu-gnu`):
1. Re-apply the 4-line optional `divergence_history_save` INI parse in `adam_io_object%load_from_file` (it was in the 2026-06-30 working tree, never committed, since lost; the case INI already sets `divergence_history_save = 1`).
2. Run the marker-ON case at base resolutions h, h/2, h/4 (e.g. 16³ → 32³ → 64³ per-block or equivalent block-count scaling — keep the AMR box, coils, and domain fixed), to a **fixed physical time** (not fixed step count; dt scales with CFL).
3. Record seam max|div(B)| and max|div(D)| at that time, centered *and* one-sided diagnostics; control (marker OFF) alongside at each resolution.
4. Fit observed order p_obs from the ratios.

**Fork criterion:**
- **p_obs ≳ 1 (clean convergence)** → the leak is ordinary truncation from the seam's lower-order ghost coupling → take **Path T** (§5-T). The "conservation violation" framing was wrong for div-B; the fix is acceptance redefinition + cleaning verification.
- **p_obs ≈ 0 or negative (stall/divergence)** → genuine consistency defect at the seam → take **Path M** (§5-M).

**E1 — cheap supporting isolations** (any order, same builds): coils-off run (isolates the J-source contribution to div(D)); long-run growth (does div(B) saturate or grow unbounded — stability vs offset); seam relocated to a quiescent region (field-gradient dependence).

## 5. Post-gate paths

### Path T — truncation accepted (expected per the literature)
- **T1.** Rewrite `rmf-amr-fd/check.sh` acceptance: convergence-ratio assertion (p_obs within tolerance of expected) + boundedness over N steps. Retire the 1e-13 assertion with a comment pointing at the premise correction.
- **T2.** Verify cleaning across the seam: run with `divergence_correction = hyperbolic` (PRISM's GLM) on the AMR case — confirm the cleaning wave crosses the 2:1 jump sanely, phi/psi rows participate in reflux like any conserved row, and seam div-B is damped, not amplified. (Watch the #11 nv/CT input-combination trap when enabling correction.)
- **T3.** Commit `rmf-amr-fd` + the IO parse; document the redefined acceptance in the regression README.

### Path M — machinery (only if E0 stalls)
- **M-A.** Mechanism decision, now premise-grounded: (i) Wang-2025 flux-point conforming + δF for the FD path (makes the FD seam conservative; does **not** zero div-B; accepts the 2nd-order conservation cap), vs (ii) Freret–Groth native-resolution ghosts (removes the mismatch at the source; heavy ghost-machinery restructuring; subsumes much of ex-Phase C). Decide on paper against PRISM's ghost/maps architecture before coding.
- **M-B.** Resolve the q(B) double-correction/row-partition question on the live seam (now testable).
- **M-C.** FNL firewall after every shared-code milestone (see §6).

## 6. Migrated open items (from #13)

| Item | Was | Status here |
|---|---|---|
| FNL firewall verification | #13 M5 | **First action after any shared-code edit**: `fobis build --mode prism-fnl-nvf --varset local_nvf` + the 4 FNL goldens. Still never run for the M0–M4 commits — do it once at issue start. |
| High-order conservative ghost-fill | #13 Phase C | Deferred until a non-conforming-resolution case exists — but note Path M(ii) and the McCorquodale–Colella constrained-interpolation requirement now define what "high-order ghost-fill" must satisfy (conservation-constrained, not plain WENO interp). |
| Closed-domain ∮F·n integration oracle | #13 §7 unchecked box | Needs a bespoke closed-domain AMR case (periodic/reflective, no coils). Low priority; restriction arithmetic is unit-pinned. |
| Disjoint-rank MPI carve-out | #13 §3.7 | Deferred, unchanged. |
| Inter-realm `coupling = interpolate` | #13 §5/§7.5.9 | Deferred behind the intra-realm oracle, unchanged. |
| FNL intra-realm AMR port | #13 §7.5.9 | Its own epic, unchanged. |

## 7. Open research questions (inherited from the SOTA review)

1. Is Wang-2025's 2nd-order conservation-error cap fundamental for collocated FD, or implementation-specific?
2. What is the discrete proof behind Freret–Groth's register-free "automatic" conservation across hanging-node faces?
3. Does any construction make genuinely non-flux-form centered FD telescope at a seam?
4. What div-B bound do Flash-X/Spark and BATSRUS cell-centered mode actually achieve at seams (do they reflux GLM ψ + induction fluxes)? — named in #13's premise but never directly sourced.

## 8. Acceptance criteria

- [x] **E0 executed and its fork recorded in this issue** (the single most important box).
- [x] E1 isolations run (coils-off = the pulse oracle E1a, long-run growth E1b/E1b′; quiescent-seam relocation dropped by grilled decision D5 — the pulse position is free).
- [x] FNL firewall green for the M0–M4 commits (migrated M5) and after every shared-code change here.
- [x] Path T: convergence-ratio + boundedness acceptance in `check.sh`; cleaning-across-seam verified; `rmf-amr-fd` + IO parse committed. **OR** Path M: mechanism decision documented on paper; row-partition verified on the live seam; seam treatment implemented CPU-first with FNL firewall.
- [x] The 1e-13 pointwise seam ∇·B criterion is explicitly retired in this issue and in any test that carried it.

## 9. References

- SOTA review (verified, 2026-07-02): `sources/papers_20260702_telescoping_cellcentered_seam.md`
- Wang, Zeng, Deiterding, Yang, Liang (2025), arXiv:2511.08335 — cell-centered FD AMR: flux-point conforming, δF correction, hybrid ghost-fill, 2nd-order conservation cap.
- Mignone, Tzeferacos & Bodo (2010), JCP 229 (arXiv:1001.2832); Mignone & Tzeferacos (2010), JCP 229:2117 (arXiv:0911.3410) — cell-centered conservative FD/FV GLM-MHD.
- Mignone et al. (2012), ApJS 198:7 — PLUTO-AMR refluxing (Eqs. 48–49) + GLM.
- Stone, Tomida, White & Felker (2020), ApJS 249:4 — Athena++ flux replacement (hydro rows; B is staggered CT).
- McCorquodale & Colella (2011), CAMCoS 6(1) + Guzik dissertation — 4th-order FV AMR, constrained ghost interpolation, mapped-grid metric telescoping.
- Freret, Ivan, De Sterck & Groth (2019), J. Sci. Comput. 79:176 — register-free heterogeneous-block CENO.
- Berger & Colella (1989), JCP 82:64 — the reflux origin.
- Predecessor: #13 (design history, Phase A, §7.5 M-log, Appendix H); siblings #16, #18 (closed).



---
## comment by szaghi at 2026-07-02T14:00:17Z
url: https://github.com/szaghi/adam/issues/21#issuecomment-4866562568

# Implementation plan v1 — #21 seam divergence control (E0-gated)

**Date:** 2026-07-02 · **Base:** develop `ab07444c` · **Scope:** issue #21 §§3–5 (E0/E1/E2 + Path T; Path M as decision procedure per D1)
**Method:** designed via structured grilling; ten decisions locked (D1–D10, §0). Every milestone has an executable acceptance check. No mechanism code before the E0 fork is recorded.

## 0. Decision record

| # | Decision |
|---|---|
| D1 | Gate-first plan. E0/E1 + Path T fully elaborated; **Path M = decision-procedure milestone only** (implementation milestones arrive as a plan amendment after the fork). |
| D2 | E0 ladder: **ni = 16/32/64** (cells-per-block; tree topology, 36-block layout, seam geometry bit-identical across rungs), `it_max = 5/10/20` (dt ∝ h exactly — constant c, fixed CFL ⇒ matched final physical time), marker ON + OFF per rung, `mpirun -np 1`, optimized `prism-cpu-gnu`. 4th rung only as ambiguity contingency. |
| D3 | Minimal pre-gate instrumentation: **only** the 4-line optional `divergence_history_save` parse. Per-block and one-sided probes are contingency instruments, built only if the fork is ambiguous. |
| D4 | Fork on p_obs of seam max\|div(B)\| at matched time: **≥ 0.8 on both ratios → Path T**; **< 0.3 on either, or negative/non-monotone → Path M**; 0.3–0.8 → contingency battery, re-decide. div(B) gates; div(D) reported. Tiebreaker: growth-in-time at fixed h (saturating vs unbounded). |
| D5 | E1a = **gaussian-pulse, zero-coil case** (source-free: with J=0 both div(D) and div(B) are exactly conserved — a two-invariant oracle). E1b = long-run growth. Quiescent-seam relocation dropped (pulse position is free). E0 stays on `rmf-amr-fd`. |
| D6 | Strict serial pre-gate: **P0 FNL firewall → P1 parse + inertness + commit → E0**. |
| D7 | Path-T `check.sh`: default = control ≤ 1e-13 AND seam value pinned to the E0 baseline (golden-style, catches moves in either direction); `--convergence` flag = on-demand 2-rung 16/32 mini-ladder asserting p_obs ≥ 0.8. |
| D8 | E2 (cleaning across the seam) is **fork-independent**, runs immediately after the fork is recorded. |
| D9 | Closed-domain ∮F·n oracle **parked** in #21 backlog. Affordance noted: an `fv_centered` variant of the pulse case is its natural host (but see the `BC_PERIODIC` caveat, §5). |
| D10 | I post #21 comments directly via `gh` (plan = first comment; body untouched except acceptance boxes). Git commits remain user-only. |

## 1. Environment (host `adam`, WSL — correctness only, never benchmarks)

```bash
# CPU/GNU:
export PATH=/opt/openmpi/bin/5.0.10/gnu/15.2.0/bin:$PATH
# FNL/NVF (Lmod modules are host-locked to quark — do not `module load`):
export NVHPC=/opt/nvidia/hpc_sdk/Linux_x86_64/26.1
export PATH=$NVHPC/compilers/bin:$NVHPC/comm_libs/mpi/bin:$PATH
# WSL MPI knobs for FNL runs: UCX_TLS=^cma UCX_RNDV_THRESH=inf OMPI_MCA_coll_hcoll_enable=0 UCX_MEMTYPE_CACHE=n
```
Debug-mode CPU tests: stable gfortran or optimized mode only (gfortran-16-exp `-fcheck=bounds` false abort, reproducer committed).

## 2. Milestones

### P0 — FNL firewall (ex-M5; overdue for the five M0–M4 shared-code commits)

- `fobis build --mode prism-fnl-nvf --varset local_nvf`
- `src/tests/prism/regression/run-fnl-local.sh` → the 4 FNL goldens (rmf, rmf-2realm, rmf-2realm-asymK, rmf-2realm-stagesync).
- **Acceptance:** build exit 0, PASS 4/4. Report to #21.
- **Contingency:** compile break in shared code → fixing it preempts everything (it bounds the blast radius of M0–M4). FNL-only golden drift → bisect against `c12d5fc5` before proceeding; the five M0–M4 commits are the suspects.

### P1 — IO parse + oracle commit

- Re-apply the 4-line optional `divergence_history_save` parse in `adam_io_object%load_from_file` (after the `residuals_save` parse; soft-parse, no `error_stop` — absent key keeps default 10). NOTE: the lib file, NOT the dead `adam_prism_io_object.F90`.
- Inertness: build `prism-cpu-gnu`; `run.sh cpu --no-build` → 4/4 PASS; `rmf-amr/check.sh` PASS.
- Purge scratch (`work-*`) from `rmf-amr-fd/`; stage `input.ini` + `check.sh` + the parse; hand over the semantic commit message; **user commits**.
- **Acceptance:** committed; all existing goldens untouched.

### E0 — the gate: convergence under refinement

**Runs** (6 = 3 rungs × ON/OFF): ni=nj=nk ∈ {16, 32, 64}; `it_max` ∈ {5, 10, 20}; CFL 0.5; marker ON and OFF; `-np 1`; optimized build.
**Ladder-variant INI** (work-dir copies, never committed): `divergence_history_save = 1`; `it_save`/`restart_save` huge; `save_residual_fields`/`save_divergence_fields` = false (the history file is the only needed output — no multi-GB h5 dumps at 64³).
**Protocol checks:** confirm from logs that dt halves per rung (record actual t_final; must match across rungs to round-off); confirm `blocks_number = 36/8` (ON/OFF) at every rung; confirm nb capacity ≥ 36 at ni=64 (init fails loudly if the 0.4-budget can't hold 36 large blocks — fallback ladder 12/24/48).
**Measure:** divergence-history cols 4 (div D) and 5 (div B) at final step, all 6 runs.
**Compute:** p_obs₁ = log₂(E₁₆/E₃₂), p_obs₂ = log₂(E₃₂/E₆₄) for seam max|div(B)|; same for div(D) (reported, not gating). Controls must stay ≤ 1e-13 at every rung (else the matched-stencil identity itself broke — stop, investigate).
**Fork:** per D4. Ambiguous band → contingency battery: one-sided seam div probe, per-block probe (session-2 recipes), 4th rung (ni=128 if memory allows, else 48), pulse-case mini-ladder (E1a exists by then).
**Deliverable:** E0 report comment on #21 — raw 6-run table, p_obs, fork declaration. **This comment is the plan's pivot; nothing downstream starts before it is posted.**

*Analytic caution recorded (not a prediction):* piecewise-constant injection ⇒ O(h) ghost-value error ⇒ O(1) local `curl_h` error ⇒ potentially O(1/h) local `div_h(curl_h)` at the skin unless stencil symmetry cancels. p_obs anywhere in [−1, 6] is a legitimate outcome; the criterion handles all of them.

### E1a — pulse case: the source-free two-invariant oracle

- New case `src/tests/prism/regression/rmf-amr-fd-pulse/`: copy of `rmf-amr-fd` with `[initial_conditions] type = gaussian_pulse` (+ `B0/k0/r0/sigma/pulse_direction` — schema donor: `src/tests/prism/cpu/plane_wave/gaussian_pulse/input.ini`), **coils_number all 0**, same grid/AMR box/Neumann BCs.
- Pulse spec: `pulse_direction = +x`, `r0` in the refined half (x < 0), σ sized so the pulse (i) straddles/crosses the x=0 seam within `it_max`, (ii) never reaches a domain boundary during the run (**Neumann kept — `BC_PERIODIC` is "(reserved)" in `adam_parameters.f90`; do not bet on it**).
- **Assertions:** marker OFF → div(D) AND div(B) ≤ 1e-13 (with J=0, both are exactly conserved: d/dt div D = −div J = 0). Marker ON → measure both; div(D) vs div(B) at the seam quantifies, by subtraction against rmf-amr-fd, what the coil J-source contributed to session-2's div(D) > div(B) anomaly.
- `check.sh` in the D7 shape from day one. Case is goldenless (run.sh skips it), exercised via check.sh — same policy as rmf-amr.
- **Acceptance:** control run round-off in both invariants; seam numbers recorded in #21.

### E1b — long-run growth (fork tiebreaker + E2 baseline)

- `rmf-amr-fd`, ni=16, marker ON, `it_max = 200`, `divergence_history_save = 1`.
- **Deliverable:** growth curve classification — saturating / linear / superlinear — posted with the E0 report. Doubles as the uncleaned baseline for E2.

### ⟂ FORK RECORDED IN #21 ⟂

### E2 — cleaning across the seam (fork-independent, runs on either path)

- `rmf-amr-fd` + `divergence_correction = hyperbolic` (safe with `constrained_transport = no` per the #11 table; follow `physics%nv_cl` for the nv change — do NOT hand-set nv=9).
- Runs: ni=16, marker ON + OFF, `it_max = 200` (matched to E1b).
- **Assertions:** stable (no NaN/blowup); seam div(B)(t) with cleaning ≤ the E1b uncleaned baseline at matched steps; no amplification signature (cleaning wave crossing the 2:1 jump must damp, not reflect-and-grow).
- Instability or amplification here is a **production-relevant finding for #21 in its own right**, whichever path E0 chose.

### Path T (only if fork = T)

- **T1** — `rmf-amr-fd/check.sh` rewritten to D7: default = control ≤ 1e-13 + seam step-5 value within rtol (proposed 5%) of the E0 ni=16 baseline; `--convergence` = 2-rung 16/32, assert p_obs ≥ 0.8. Same shape applied to `rmf-amr-fd-pulse/check.sh`.
- **T2** — acceptance documentation: E2 result folded in; the 1e-13 pointwise criterion explicitly retired in the regression README with a pointer to #21 §1 (premise correction).
- **T3** — close-out: #21 acceptance boxes ticked, final comment; commits staged for user.

### Path M (only if fork = M) — decision procedure, no code (D1)

- **M-A** — paper-first mechanism comparison, published as a design note + #21 comment:
  - Candidates: (i) Wang-2025 flux-point conforming + δF end-of-step correction (FD path); (ii) Freret–Groth native-resolution ghosts (subsumes much of Phase C); (iii) conservation-constrained ghost interpolation (McCorquodale–Colella constraint: Σ fine = 2³ × coarse) as the cheaper middle; (iv) cleaning-only fallback (accept E2's bound, document).
  - Criteria: fit to `adam_maps_object`/ghost-slab architecture; FD+FV coverage; **FNL portability of any new ghost machinery** (§7.5.9 walls); expected seam order; resolution of the inherited q(B) double-correction question; implementation cost.
- **M-B** — plan amendment v2 with implementation milestones, grilled the same way as this plan. Only then code.

## 3. Standing constraints (apply to every milestone)

1. FNL firewall (P0 commands) re-run after **every** shared-code change (`adam_io_object`, residuals, maps, register).
2. User commits only; I stage + hand over semantic messages, then stop.
3. I post #21 comments directly (D10); the #21 body is never edited except acceptance checkboxes.
4. WSL numbers are correctness data, never performance data; `-np 1` for all E-runs.
5. Ladder/E-run INI variants live in work dirs only; committed case INIs stay canonical.

## 4. Risk register

| Risk | Mitigation |
|---|---|
| ni=16 rung pre-asymptotic → misleading first ratio | Fork gates on BOTH ratios; 4th-rung contingency (D2/D4) |
| nb capacity < 36 at ni=64 (0.4-budget sizing) | Loud init failure; fallback ladder 12/24/48 (still dyadic) |
| `BC_PERIODIC` reserved/unimplemented | Avoided by design: Neumann + interior pulse (E1a) |
| Cleaning + AMR seam never co-exercised (E2 novel) | E2 has explicit instability assertion; a failure is a reportable finding, not a plan break |
| FNL firewall reveals M0–M4 breakage | P0 runs first (D6); bisect window is exactly 5 commits |
| Contingency probes re-introduce session-2 throwaway churn | Probes are named, scripted from the handoff recipes, and deleted in the same milestone that uses them |

## 5. Parked (in #21 backlog, not this plan)

- Closed-domain ∮F·n oracle — natural host: `fv_centered` variant of `rmf-amr-fd-pulse`; **blocked-ish on `BC_PERIODIC` being implemented** (currently "(reserved)"), or on a reflective closed-box alternative.
- Phase C ghost-fill; disjoint-rank carve-out; inter-realm `coupling = interpolate`; FNL intra-realm AMR port — unchanged from #21 §6.


---
## comment by szaghi at 2026-07-02T14:22:44Z
url: https://github.com/szaghi/adam/issues/21#issuecomment-4866787625

## P0 — FNL firewall: FAIL caught, root-caused; one fix staged, one decision open

**Verdict:** the firewall did exactly its job. At develop HEAD `ab07444c` the FNL backend was **broken** — all 4 goldens FAIL with realm residuals blowing up to 1e43–1e46 — while **CPU passes 4/4** at the same HEAD. Root cause is not #13/#21 seam machinery: the M0–M4 shared-code commits are exonerated.

### Finding 1 — coil ramp envelope clamp removed → FNL blow-up (FIXED, staged)

Commit `9e2f2529` ("fWL on fnl") dropped the clamp on the coil-current ramp envelope in `adam_prism_fnl_object.F90`:

```fortran
- s = 1._R8P ; if (td > 0._R8P) s = time_s / td ; s = max(0._R8P, min(1._R8P, s))
+ s = 1._R8P ; if (td > 0._R8P) s = time_s / td
```

With the rmf-family `time_delay = 1.0E-19`, `s = time_s/td ≈ 3e8` and the quintic envelope `g = 10s³−15s⁴+6s⁵ ≈ 1e43` — matching the observed residual magnitudes exactly. The CPU side kept its clamp (`adam_prism_cpu_object.F90:490`), which is why CPU goldens survive. Any case with a small-but-nonzero `time_delay` blows up on FNL; the clamp is load-bearing, its removal cannot be intended.

**Fix (working tree, staged):** clamp restored, one line. After rebuild: residual files match golden on all 4 cases (rtol=1e-6), D/B field digests match.

### Finding 2 — coil-stamp resequencing changes the saved J snapshot (OPEN DECISION)

After the clamp fix, exactly **6 digest discrepancies per case remain, confined to Jx/Jy/Jz** at the step-5/step-10 snapshots (e.g. rmf `Jy` min −40.43 vs golden −32.35; Jx/Jz deltas 0.003–0.2%). All D/B rows and all residuals match golden.

Cause: `9e2f2529` also **resequenced the FNL pipeline** — per-stage `compute_coils_current(q_rk(s), gamm)` moved from the SSP stage loop into `update_ghost` (so the coil stamp now lands *after* ghost exchange + BC instead of before), `apply_fwl_correction` moved from per-residual to end-of-step. The J rows are imposed data, so *where* they are stamped relative to BC changes their saved snapshot without moving the D/B dynamics (which is golden-identical within tolerance).

This looks intentional (part of the fWL-correction design), but it has two consequences to decide on:
1. The 4 FNL goldens no longer match intended behavior → **rebaseline** them, or **revert the resequencing** and keep the goldens. Needs @feden96's confirmation of intent.
2. CPU and FNL now stamp J at different pipeline points → the backends disagree on the saved J snapshot for identical inputs. If the resequencing is the desired design, the CPU backend should follow (and CPU goldens rebaseline too); if not, FNL should revert. Cross-backend divergence in pipeline order is worth closing either way.

### Status vs plan

- P0 acceptance ("build exit 0 + PASS 4/4") is **not met** pending the Finding-2 decision; build is clean and the blow-up is fixed.
- The CPU path — everything P1/E0 needs — is verified green at HEAD (PASS 4/4). Per the plan's contingency, the seam-work suspects are cleared; the FNL breakage is orthogonal to #21's CPU-first milestones.

**Artifacts:** clamp fix staged (commit message handed over); full logs in session scratchpad; CPU regression PASS 4/4, FNL post-fix: residuals PASS ×4, field digests FAIL on J rows only.


---
## comment by szaghi at 2026-07-02T14:46:40Z
url: https://github.com/szaghi/adam/issues/21#issuecomment-4867029208

## P0 — CLOSED: FNL firewall green (PASS 4/4)

Finding 2 is resolved by **surgical revert of the coil-stamp resequencing**, per the maintainer's clarification: fWL is an experimental, CPU-first feature whose FNL port is incomplete — its resequencing of the *coil* pipeline on FNL was scaffolding, not considered design. The revert restores the pre-`9e2f2529` coil-call ordering and **keeps every fWL-gated call exactly where the fWL work placed it** (all `C > 0`-gated, inert for the golden suite):

- `integrate_rk_ssp_dev`: per-stage `compute_coils_current(q_rk(s), gamm(s))` restored (was commented out);
- `update_ghost`: the appended `compute_coils_current` block removed (routine back to its prior shape);
- untouched: end-of-step `apply_fwl_correction`, IC-time fWL/coil calls, and the commented fWL call in `compute_residuals_dev` — experimental placement, free to evolve.

**Verification at merged HEAD + clamp fix + revert:**
- FNL: **PASS 4/4** (rmf, rmf-2realm, rmf-2realm-asymK, rmf-2realm-stagesync) — residuals and full field digests, zero rebaselines.
- CPU: PASS 4/4 (unchanged).
- CPU/FNL coil-stamp pipeline parity restored.

**P0 acceptance met.** The two firewall findings and their fixes: (1) coil ramp envelope clamp restored (blow-up, committed); (2) coil-stamp ordering reverted (J-snapshot drift, staged). Both were collateral edits to core coil machinery inside experimental fWL work — the regression suite never exercised fWL itself (`C = 0` everywhere).

**Process note for the fWL thread:** any edit that leaves the `C > 0` gate — coil call sites, `update_ghost`, integrator loops — is core-pipeline change and needs the golden suite on both backends before landing on develop. A feature branch for the FNL fWL port avoids this class of breakage entirely.

Next: **P1** (re-apply the `divergence_history_save` parse, inertness check, commit the `rmf-amr-fd` oracle), then **E0**.


---
## comment by szaghi at 2026-07-02T15:15:41Z
url: https://github.com/szaghi/adam/issues/21#issuecomment-4867319882

## E0 — the gate experiment: seam div(B) DIVERGES under refinement (p_obs ≈ −1) → FORK = PATH M

*(P1 landed first: the `divergence_history_save` optional key + the `rmf-amr-fd` oracle are committed; CPU 4/4, FNL 4/4, rmf-amr check green; the oracle reproduces the session-2 numbers bit-for-bit — control `2.046674E-19`, seam `4.614231E-07` at step 5.)*

### Protocol executed as planned

6 runs: ni = 16/32/64 cells-per-block × {marker ON, OFF}, it_max = 5/10/20, CFL 0.5, `-np 1`, optimized `prism-cpu-gnu`, per-step divergence history, no field dumps. Tree topology bit-identical across rungs (36 blocks ON / 8 OFF at every rung). dt ∝ h held exactly; all three ON rungs end at the identical physical time **t = 7.81790792913750e-12** (dt set by the fine level), all three OFF rungs at 1.5636e-11. Controls: max|div(B)| ≤ 2.0e-17 at every rung — the matched-stencil identity is intact without a seam, at all resolutions.

### The measurement

Seam max|div(B)| at matched physical time:

| rung | h ratio | seam max\|div(B)\| | ratio E(h)/E(h/2) | p_obs |
|---|---|---|---|---|
| 16³ | 1 | 4.61423e-07 | — | — |
| 32³ | 1/2 | 9.15026e-07 | 0.5043 | **−0.988** |
| 64³ | 1/4 | 1.76759e-06 | 0.5177 | **−0.950** |

Seam max|div(D)| (reported, not gating): 3.652e-07 → 6.477e-07 → 1.272e-06 → p_obs = −0.83, −0.97.

**The seam divergence error grows as E ∝ 1/h — first-order DIVERGENCE under refinement, clean and monotone on both ratios and on both fields.**

### Fork decision (per plan v1 D4)

p_obs < 0.3 on both ratios (strongly negative) → **PATH M — machinery**. The ambiguity band was not entered; no contingency instruments needed.

This kills Path T definitively: the leak is **not** truncation — no acceptance redefinition can bless an error that doubles every refinement. It is a genuine **consistency defect of the seam operator**: the measured p = −1 is exactly the analytic prediction for 0th-order injection ghosts feeding `curl_h` — an O(h) ghost-value error becomes an O(1) local curl error through the 1/h of the derivative stencil, and an O(1/h) local `div_h(curl_h)` residual through the second. The refinement study confirms that mechanism quantitatively.

Growth-in-time tiebreaker (informational): at fixed h the seam div(B) grows superlinearly (~t³ over the observed window, no saturation within 20 steps); E1b (200 steps) will characterize saturation vs unbounded growth.

### Secondary finding — the control div(D) floor is the coil J-source, not the seam

Control (no seam) max|div(D)| ≈ 3.4–3.7e-10 at ALL rungs — h-independent, far above round-off, while control div(B) is 1e-18. This is the numerical `div J` of the coil source (d/dt div D = −div J), a fixed source-consistency floor unrelated to the seam. It validates gating the fork on div(B) only, and predicts the E1a pulse case (J = 0) drives BOTH control divergences to round-off — the two-invariant oracle.

### Next (per plan)

- **E1a** — `rmf-amr-fd-pulse` (gaussian-pulse IC, zero coils): source-free seam oracle; also quantifies the coil contribution to the seam div(D) excess by subtraction.
- **E1b** — 200-step growth run at 16³ (saturating vs unbounded), doubling as the E2 baseline.
- **E2** — cleaning across the seam (`divergence_correction = hyperbolic`): the production-relevant question is now sharper — can GLM damping hold a **1/h-growing** seam source bounded?
- **M-A** — the Path-M mechanism decision note (Wang-2025 flux-point δF vs Freret–Groth native-resolution ghosts vs conservation-constrained ghost interpolation), written on paper against PRISM's ghost/maps architecture, then plan amendment v2. The E0 mechanism confirmation (injection ghosts are the defect) is a direct input: any candidate must replace or bypass the 0th-order injection feeding the seam-adjacent curl stencils.

Raw 6-run histories in the session scratchpad; ladder script reproducible from the committed case INI via the documented sed transforms.


---
## comment by szaghi at 2026-07-02T16:02:18Z
url: https://github.com/szaghi/adam/issues/21#issuecomment-4867742766

## E1a + E1b — two-invariant oracle built and run; long-run growth superlinear (~t^2.5)

*(Session note: the previous session died to a WSL OOM mid-E1a — during the 36-block `allocate_cpu` of the seam run. Recovered with no loss; all E1a/E1b runs below re-executed cleanly. Heavy HDF5 work-dir artifacts are deleted after each run from now on — only the divergence histories are kept.)*

### E1a — `rmf-amr-fd-pulse` (source-free, zero coils; case + `check.sh` staged, commit pending)

Gaussian pulse `+y` (transverse to the x=0 seam normal — load-bearing, see the INI header), sigma=0.01, B0=10, k0=0, same 36/8-block 2:1 seam as `rmf-amr-fd`, it_max=5, `-np 1`.

| run | max\|div(D)\| | max\|div(B)\| |
|---|---|---|
| control (marker off, 8 blk) | **0.0 exact** | **0.0 exact** |
| seam ON (36 blk) | **0.0 exact** | **2.497e+02 (s1) → 3.367e+02 (s5)** |

Three results, each sharper than the D5 design anticipated:

1. **The control conserves both invariants *exactly*, not to 1e-13.** The transverse plane pulse has every divergence term identically zero term-by-term (D=Dz(y), B=Bx(y)), and the update preserves that in exact FP. The oracle is stronger than round-off.
2. **It also retires E0's secondary:** the control div(D) floor of ~3.5e-10 in `rmf-amr-fd` was coil J-source consistency, as conjectured — with J=0 it vanishes identically.
3. **The seam leak is B-only and immediate.** div(D) stays exactly 0 across the seam (structural for this pulse orientation: div(D)=dDz/dz and no z-variation ever develops), while div(B)=dBx/dx sees the y-staircased injection ghosts from step 1 — the IC overlaps the seam, so there is no grow-from-zero transient as in the coil case. Magnitude O(10²) on O(10) fields at h=1.875e-3: the O(1/h) scaling E0 measured, now on a source-free state.

`check.sh` is in the D7 fail-before shape: control asserts ≤1e-13 on **both** invariants (PASS), seam asserts the Path-M acceptance (FAILs by design until the seam machinery lands).

### E1b — `rmf-amr-fd`, marker ON, it_max=200 (work-dir variant)

Seam max|div(B)| growth at fixed h (ni=16), matched to E0 conditions:

| step | 1 | 20 | 40 | 100 | 200 |
|---|---|---|---|---|---|
| max\|div(B)\| | 3.7e-9 | 2.8e-5 | 2.0e-4 | 2.0e-3 | 1.08e-2 |

**Classification: superlinear, ~t^2.4–2.8 over the window, no saturation** (E0's early ~t³, mildly decelerating; log-slope from s100→s200 is 2.4). The leak is secular, not equilibrating — this is the uncleaned baseline E2 must beat. div(D) plateaus at ~7.9e-5 (coil-source floor at this amplitude, per E1a item 2).

### E2 spec correction (before running it — one plan deviation + one latent bug found)

The plan's E2 parenthetical says `divergence_correction = hyperbolic` is "safe with `constrained_transport = no`". Reading `adam_prism_physics_object%initialize` (`src/app/prism/common/adam_prism_physics_object.F90:329-385`):

1. **CT=no + hyperbolic is a cleaning no-op**, not a cleaning configuration. The `DIV_CORR_VAR_HYPER` branch dispatches on the CT_D/CT_B flags (D-only / B-only / D+B) **with no else**: CT=no leaves `nv_cl=0` and the cleaning eigen-structure pointers null. The CT flags are what select *which field gets GLM cleaning*; `divergence_correction` selects the method.
2. **Latent #11-class bug in that combo:** `var_Jx/var_Jy/var_Jz` have no declaration initializer and are assigned only inside the three CT branches — under `hyperbolic` + `CT=no` they are **undefined** when later used to index J in the state vector. Memory-safe per the #11 names-vs-allocation table, but undefined-variable UB nonetheless. Filing under #11's umbrella; trivially fixed by giving the if-chain an else that mirrors the `default` branch (7/8/9).

**Corrected E2 config** (donor: `src/tests/prism/fnl/rmf/RMF/RMF_nom_divB/input.ini`): `constrained_transport = B`, `divergence_correction = hyperbolic`, `chi = 1.0` in `[physics]` → `nv_cl=1`, physics nv=10. No INI `nv` edit needed: PRISM ignores `[field] nv` and passes `nv=self%physics%nv` (`adam_prism_common_object.F90:206`) — the plan's "follow `physics%nv_cl`" clause is satisfied automatically. Runs stay as planned: ON+OFF, it_max=200 matched to E1b.

**E2 is deferred to the next session** — the WSL box is under memory pressure again (two host-side warnings during E1b); one 200-step pair at a time from here on.


---
## comment by szaghi at 2026-07-02T16:50:44Z
url: https://github.com/szaghi/adam/issues/21#issuecomment-4868219206

## E2 — cleaning across the seam: AMPLIFICATION confirmed; cleaned run crosses the uncleaned baseline at ~step 120 and ends 3.1× worse

Config per the corrected spec (previous comment): `constrained_transport = B` + `divergence_correction = hyperbolic` + `chi = 1.0` (donor `RMF_nom_divB`; physics nv=10 via `nv_cl=1`). Runs: `rmf-amr-fd`, ni=16, marker ON + OFF, it_max=200 matched to E1b, `-np 1`, work-dir INIs only. Both runs stable to step 200 — exit 0, no NaN/blowup.

### Control (marker OFF, cleaning ON, 8 blocks)

max|div(B)| = **7.6e-15** at step 200 — round-off. GLM cleaning is benign on the seamless grid; whatever follows is the cleaning × seam interaction, not the cleaning itself. div(D) ends at 1.8e-8 (the coil J-source consistency floor integrated over 200 steps; D is untouched by B-cleaning, as expected).

### Seam ON (36 blocks): cleaned vs the E1b uncleaned baseline, matched steps

| step | E1b uncleaned div(B) | E2 cleaned div(B) | cleaned/uncleaned |
|---|---|---|---|
| 20  | 2.83e-5 | 2.14e-5 | 0.76 |
| 60  | 5.66e-4 | 2.41e-4 | 0.43 |
| 100 | 2.02e-3 | 9.15e-4 | **0.45** |
| 120 | 3.13e-3 | 3.04e-3 | 0.97 — crossover |
| 160 | 6.25e-3 | 1.35e-2 | 2.17 |
| 200 | 1.08e-2 | 3.35e-2 | **3.10** |

Two regimes:

1. **Early (≲ step 100):** cleaning does its job — the seam-injected div(B) is transported/damped and the running max sits at ~0.4–0.5× the uncleaned baseline.
2. **Late (≳ step 120):** amplification. Per-20-step growth factors of the cleaned run: ×2.3, ×1.9, ×1.65, ×1.50 — decaying but every one of them far above the uncleaned baseline's (~×1.2). Local log-slope over s120→s200 is p ≈ 4.7 vs the uncleaned ~2.4. The GLM wave that the seam source continuously pumps does not damp across the 2:1 jump — it is re-scattered by the same non-conforming stencils that create the source, and the psi field builds up faster than the transport removes it.

### Consequences for #21

- **The plan's E2 assertion "cleaned ≤ uncleaned at matched steps" FAILS** from step ~120 on. Per the plan, this is a production-relevant finding in its own right: enabling hyperbolic cleaning on a seam-bearing PRISM run is a net *liability* beyond short horizons at this chi.
- **M-A candidate (iv), the cleaning-only fallback, is dead.** It cannot "accept E2's bound" — there is no bound; cleaning inverts sign of benefit mid-run. The M-A comparison reduces to the three structural candidates (Wang δF flux-point, Freret–Groth native-resolution ghosts, conservation-constrained interpolation).
- Caveat recorded: single chi (=1.0) tested. A chi sweep could shift the crossover but cannot fix the mechanism — the source is secular (E1b: ~t^2.5 uncleaned) and h-divergent (E0: p ≈ −1), so any linear transport-damping race is eventually lost.

*(Operational note: E-runs are now executed strictly one at a time on the WSL box — its fill-the-node pre-allocation is by design; overlapping runs were what triggered the OOM crashes.)*

**Next per plan: M-A — paper-first mechanism comparison among the three surviving candidates, posted as a design note; then plan amendment v2 (grilled) before any code.**


---
## comment by szaghi at 2026-07-02T17:03:04Z
url: https://github.com/szaghi/adam/issues/21#issuecomment-4868382865

## M-A — mechanism decision (paper-first): constrained ghost interpolation selected; Freret–Groth held as fallback; Wang δF rejected as mis-targeted

**Inputs:** E0 (p_obs ≈ −1), E1a (source-free two-invariant oracle), E1b (~t^2.4–2.8 secular), E2 (cleaning amplifies ×3.1 by s200), the verified SOTA review (`sources/papers_20260702_telescoping_cellcentered_seam.md`), and a code-level map of the seam machinery (file:line below). Per D1/plan-§M-A this is a decision procedure — no code until the M-B amendment is grilled.

### 0. The diagnosis that orders the comparison

The seam ghost fill is a **single-donor, 0th-order injection**: one coarse value replicated into all 8 fine ghost cells (`adam_field_object.F90:882-892`; map fan-out `adam_maps_object.F90:1044-1062`, hardcoded `do n=1,8` with the *same* `(i_send,j_send,k_send)`). The 6th-order curl then reads **3 layers** of those ghosts (`fdv_half_stencil = fdv_order/2`, `adam_realm_object.F90:371`; `compute_curl_fd_centered`, `adam_fdv_operators_library.F90:653`).

The error chain is then forced: ghost-value error **O(h^q)** → curl error at the seam skin **O(h^(q−1))** → div(B) production rate **O(h^(q−2))**. Injection is q=1, predicting **p = −1**. E0 measured **p_obs = −0.99/−0.95**. The prediction also post-dicts the anti-pattern: *unconstrained* linear prolongation raised nominal q but broke the sum property injection trivially satisfies (Σ over 8 fine ghosts = 8 × coarse), and made div(B) worse (1.7e-5 vs 3.7e-6 @ s10) — exactly the Guzik/McCorquodale–Colella finding that the interpolant **must be conservation-constrained to keep its order**.

So the defect lives in the **ghost-fill (accuracy) lane**, not the **reflux (conservation) lane** — the two are decoupled concerns (Wang 2025, point 1), and M4 already proved reflux is div-inert here (bit-identical div(B) on/off). A mechanism is judged first by whether it raises q.

### 1. Candidates against the plan's criteria

| Criterion | (i) Wang-2025 flux-point + δF | (ii) Freret–Groth native-res ghosts | (iii) MC–Guzik constrained interpolation |
|---|---|---|---|
| Attacks the measured defect (q) | **No** — targets conservation; ghost-fill explicitly left to (hybrid) interpolation | Yes — removes the resolution mismatch at source | **Yes — directly**: q = 3–4 ⇒ predicted p_obs ≈ +1/+2 |
| Fit to `adam_maps_object`/ghost-slab | Poor: requires recasting the centered FD path in flux form + flux-point storage + a δF register the FD path doesn't feed (`adam_prism_cpu_object.F90:2997`) | Poor: heterogeneous ghost storage breaks the uniform 5D `q(nv,1−ngc:…,nb)` slab; non-uniform stencil spacing at exactly the seam-adjacent cells | **Good**: slabs unchanged; extension = multi-donor footprint + weight table in the comm map (today one `(i,j,k)_send` per ghost, `adam_maps_object.F90:137-162`; 2:1 loops at `:940,:1003,:1050` widen) |
| FD+FV coverage | FD only (FV reflux already landed, M0–M4) | FV-native (CENO); FD fit unproven — curl stencils would straddle a 2h/h spacing change | Both — the fill is upstream of every stencil |
| FNL portability (§7.5.9 walls) | New device flux-point + δF kernels; FNL reflux twin doesn't even exist yet (`adam_prism_fnl_object.F90:2367` no-op) | Heaviest: full device ghost-machinery rewrite, irregular data | **Contained**: kernel stays a gather-with-weights, same shape as `update_ghost_local_gpu` (`adam_fnl_field_kernels.F90:186`); weights host-generated at init — the `declare create` + `update device` pattern already validated on nvfortran 26.1 (FDV Phase 0) |
| Expected seam div order | Unchanged by construction (div-B "transported and damped, never zeroed"; conservation-error cap at 2nd order) | Truncation-order of the scheme at the seam (claimed; discrete proof deferred — SOTA open question Q2, MEDIUM confidence) | O(h^(q−2)) production ⇒ **p_obs ≈ +1 (cubic) / +2 (quartic)** — meets G2's convergence acceptance; NOT machine zero, by premise |
| q(B) double-correction (M-B) | **Forces it immediately** (δF targets q rows incl. B, on top of reflux) | Dissolves it (register-free) | **Leaves it parked** — no new q corrections; reflux untouched |
| Cost | High: touches the numerical core; forfeits the matched-stencil `div_h(curl_h) ≡ 0` identity that is the FD path's foundation | Very high: data-structure epic across CPU+FNL | **Low–moderate**: maps extension + init-time weight generator + two fill kernels, CPU-first |

### 2. Decision

**Select (iii) — conservation-constrained ghost interpolation** (McCorquodale–Colella/Guzik constrained least-squares, adapted from 4th-order FV cell averages to our cell-centered point values), coarse→fine direction only; the fine→coarse 8-cell restriction (`one_or_eight=8`) is already clean (E-series: coarse side at round-off).

- **Reject (i)** as mis-targeted: it solves a problem we don't currently have (FD-path telescoping conservation) at the cost of the identity that keeps the seamless grid at round-off, and it explicitly does not move div-B. Retain the δF idea only if FD-path conservation ever becomes its own requirement.
- **Hold (ii)** as the escalation path if the constrained fill stalls in E0′ (below), and as the natural long-term frame for the FV SOTA ladder — its premise risk (single-group, proof deferred) and CPU+FNL restructuring cost are not justified while an architecture-compatible candidate with a quantitative prediction is untested.
- The cleaning-only fallback (iv) was already killed by E2.

**Design constraints carried into M-B (non-negotiable):**
1. The interpolant must satisfy the discrete sum constraint (Σ 8 fine ghosts = 8 × coarse donor) — the property injection trivially has and unconstrained linear lost. For point values this is the 2:1 trapezoid/midpoint-consistency analogue of MC's ⟨U⟩ constraint; exact form to be fixed in M-B.
2. Footprint must serve **3 ghost layers** (fdv_order 6); donor availability at block corners/edges (coarse donor's own ghosts) must be resolved in the maps pass, not the kernel.
3. Weights generated host-side at init into a table; kernels stay branch-free gathers (FNL wall).
4. The seam-OFF path must be bit-identical to today (firewall: 4 CPU + 4 FNL goldens + `rmf-amr` untouched).

### 3. Pre-registered verification (mechanism firewall, before/after)

| Oracle | Today (injection) | Acceptance with constrained fill |
|---|---|---|
| E0′ ladder 16/32/64, matched t | p_obs = −0.99/−0.95 | **p_obs ≥ +1 on both ratios** (gate; stall → escalate to (ii)) |
| E1a pulse, control | exactly 0.0 both invariants | unchanged (no seam ⇒ path untouched) |
| E1a pulse, seam ON | div(B) 3.4e2 @ s5, div(D) ≡ 0 | div(B) drops by ~h² factor at ni=16 and converges in ladder; **div(D) must stay exactly 0** (tangential interpolation of Dz(y) creates no z-variation — a free structural check) |
| E1b 200-step growth | ~t^2.4–2.8 secular | re-classify; bounded or reduced-order growth |
| E2 cleaning, chi=1.0 | crossover s~120, ×3.1 @ s200 | **no crossover** — cleaned ≤ uncleaned at all matched steps (the h^q source should now lose the race to transport-damping) |
| Goldens | CPU 4/4, FNL 4/4, rmf-amr | bit-identical (no seam in any of them… except rmf-amr: structural PASS unchanged) |

### 4. Next

**M-B:** plan amendment v2 — implementation milestones for the constrained fill (maps-layout extension, weight generator + its unit test, CPU kernels, FNL port, firewall cadence), grilled decision-by-decision before any code, per the process rule already on this issue.


---
## comment by szaghi at 2026-07-02T17:30:58Z
url: https://github.com/szaghi/adam/issues/21#issuecomment-4868711291

**Maintainer directive on M-A candidate (i):** Wang-2025 flux-point + δF is rejected for the present div(B) work but **parked, not dead** — a fully conservative FD scheme is a plausible future requirement for PRISM in its own right. When/if that requirement materializes, δF is the published construction (accepting the 2nd-order conservation-error cap), to be layered *alongside* the seam ghost-fill mechanism, not instead of it. Filed in the #21 backlog next to the closed-domain ∮F·n oracle, which would be its natural acceptance test.

---
## comment by szaghi at 2026-07-02T18:37:05Z
url: https://github.com/szaghi/adam/issues/21#issuecomment-4869368919

## Plan amendment v2 — M-B: constrained coarse→fine ghost interpolation (grilled, 8 decisions locked)

**Scope:** implementation plan for the M-A mechanism (constrained ghost interpolation, issuecomment-4868382865). Designed via structured grilling 2026-07-02; decisions G1–G8 below are locked. Supersedes nothing in plan v1 except the Path-M placeholder; all standing constraints (FNL firewall per shared-code change, user-only commits, WSL one-test-at-a-time, work-dir-only INI variants) carry over unchanged.

### 0. Locked decisions

| # | Decision | Resolution |
|---|---|---|
| G1 | Constraint discipline | **Switchable A/B, default constrained.** Two weight regimes, same kernel: constrained (exact round-trip R∘P = I — the mean of the 8 interpolated fine-ghost values equals the coarse donor value exactly, weights projected in closed form) and plain tensor-product. The FV Σ⟨U⟩ constraint's point-value analogue is R∘P = I against the *existing* 8-cell-mean restriction (`one_or_eight=8`, `adam_field_object.F90:885-892`). The A/B decides whether the Guzik constraint is load-bearing for point values — either answer is a finding. |
| G2 | Order | **Tricubic, q = 4** (4³ footprint): predicts seam div(B) p_obs ≈ +2, two orders above the E0′ gate — unambiguous PASS/FAIL. Triquadratic rejected (predicts +1, exactly at the gate: no margin). |
| G3 | Corners/edges | **Shift the footprint inward, keep q = 4** (off-center anchor, 1D-decomposed shifted weight sets; shift state resolved per row at maps-build). Donors are **real cells of the donor block, always** — never the donor's own ghosts (kills the two-phase fill-ordering dependency before it exists). Normal direction is one-sided into the coarse interior by construction. Quadratic fallback retained only as a maps-build assertion safety valve (must never fire; firing is a bug). |
| G4 | Map layout | **Extend rows in place, new flag value.** `one_or_eight`: 1 = copy, 8 = restrict, **4 = interpolate**; plus one packed-int metadata column (sub-position octant + 3 tangential shift states). One row per fine ghost, unchanged sort/pack plumbing; the `do n=1,8` fan-out (`adam_maps_object.F90:1044-1062`) computes the metadata at build. The 4³ gather is implicit around the anchor; weights come from 1D tables composed w = wx·wy·wz in the kernel (branch-free). |
| G5 | MPI side | **Pack-side, donor rank.** Buffer layout and unpack identical to today (precedent: the pack-side 2:1 restriction, `adam_field_object.F90:946-954`). Preserves the FNL device-buffer surface (issue #12) for the eventual port. |
| G6 | Scope + switch | **Uniform across all schemes and all `update_ghost` callers** (the defect is geometric, not scheme-specific). Tri-valued INI key `[amr] seam_ghost_fill = injection | interpolate-unconstrained | interpolate-constrained`, **default constrained**, resolved at maps-build. `injection` is first-class rollback and the E0′ baseline arm. No committed golden has a cross-level seam, so the default touches nothing checked in. |
| G7 | FNL | **Maps mirror only** (mechanical column bump in the host→device copy, `adam_fnl_maps_object.F90:107-139` — unavoidable, the array shape changes); **fill kernel deferred** to the FNL intra-realm-AMR epic with an explicit parity-debt comment at `adam_fnl_field_kernels.F90:186`. FNL cannot run a seam today (reflux no-op at `adam_prism_fnl_object.F90:2367`); no dead device code. |
| G8 | E0′ sequencing | **Gate-first.** (1) Injection bit-identity rerun (one rung + control) — must reproduce E0 numbers **bit-for-bit**, else stop: the refactor changed behavior. (2) Constrained + unconstrained ladders (ni = 16/32/64, matched t, `-np 1`, serial). (3) Gate: constrained p_obs ≥ +1 on both ratios. PASS → E1a′/E1b′/E2′; FAIL → stop, escalate to Freret–Groth per M-A with the A/B slopes as the diagnosis. ≈ 8 runs to the gate. |

### 1. Milestones (each = firewalled, separately staged user commit)

- **N0 — weight tables + unit test.** New module (`src/lib/common/`, e.g. `adam_seam_interpolation_library`): 1D tricubic coefficient vectors (centered + shifted anchor states × 2 sub-positions), the constrained-projection variants, the quadratic safety set; all `parameter` constants (host; device mirroring deferred per G7). Standalone fobos test mode asserting: exact reproduction of polynomials up to degree 3 (all shift states, all sub-positions); R∘P = I exact for the constrained set; partition of unity (constants reproduced ⇒ the E1a div(D) ≡ 0 invariant survives interpolation structurally).
- **N1 — maps extension.** Flag-4 rows + metadata column in the fan-out; shift-state computation; the G3 assertion; FNL maps-mirror column bump; grep-audit for hardcoded column-count literals. Acceptance: firewall green (CPU 4/4 + FNL build + FNL 4/4), `rmf-amr` structural green, and — with key = `injection` — the map change is a provable no-op (bit-identity vs E0, first leg of G8).
- **N2 — CPU fill kernels + INI key.** Flag-4 branch in `update_ghost_local` (`adam_field_object.F90:882`) and the MPI pack path (`:946`); `[amr] seam_ghost_fill` parse. Acceptance: firewall + injection bit-identity again; both interpolation arms smoke-clean on `rmf-amr-fd` ni=16 (no NaN, seam div(B) moves in the right direction).
- **N3 — E0′ gate** per G8. Deliverable: ladder table + p_obs fits + A/B verdict posted here; fork recorded.
- **N4 — post-gate battery** (PASS only): E1a′ (pulse: control must stay exactly 0.0/0.0; seam div(D) must stay exactly 0 — structural, per N0's partition-of-unity check; div(B) re-laddered), E1b′ (growth reclassification), E2′ (chi=1.0: **no crossover** — cleaned ≤ uncleaned at all matched steps). `check.sh` for `rmf-amr-fd` + pulse rewritten to the D7/T1 shape: control ≤ 1e-13, seam value pinned to the new baseline, `--convergence` 2-rung flag; the 1e-13 pointwise seam criterion formally retired in the regression README (#21 acceptance box).
- **N5 — close-out staging.** Semantic commit messages handed over per milestone (user commits, as always); #21 boxes ticked; parity-debt + Wang-parked pointers verified in place.

### 2. Predictions this plan is accountable to

| Quantity | Injection (today) | Predicted, constrained tricubic |
|---|---|---|
| Ghost accuracy q | 1 | 4 |
| Seam div(B) ladder slope p_obs | −0.99/−0.95 (E0) | **≈ +2** (gate ≥ +1) |
| E1a seam div(D) | exactly 0 | **exactly 0** (partition of unity) |
| E1b growth | ~t^2.4–2.8 secular | bounded or reduced-order |
| E2 cleaning | crossover s≈120, ×3.1 @ s200 | **no crossover** |

### 3. Risk register

1. **Transplant conjecture wrong** (point-value R∘P = I not the operative constraint) → caught at N3 by the A/B; escalation path pre-decided (Freret–Groth), diagnosis data already in hand.
2. **Map-shape ripple** — any code holding column-count literals for `inter_realm_ghost_cell` (CPU or FNL copy) → N1 grep-audit + firewall.
3. **Corner assertion fires** (unshiftable footprint) → by construction impossible for ni ≥ 4; if it fires, the maps pass has a bug — fix, don't fallback.
4. **WSL memory** — all E-runs strictly serial, work-dir INIs save-trimmed, artifacts deleted per run (standing).

**Next action:** N0.


---
## comment by szaghi at 2026-07-02T18:46:42Z
url: https://github.com/szaghi/adam/issues/21#issuecomment-4869444520

**N0 checkpoint — G1 amended (grilled): the point-value transplant of the Guzik constraint is provably order-destroying.**

Two-line proof: any interpolant P that reproduces quadratics fills the 8 fine octant ghosts of a coarse cell with the exact values of f = x² (all H²/16 at offsets ±H/4), whose 8-cell mean is H²/16 ≠ 0 = f(anchor). Hence exact R∘P = I (R = the existing `one_or_eight=8` mean) is incompatible with reproduction of quadratics: **restriction-compatibility caps ghost accuracy at q = 2 for point values.** Guzik's FV constraint survives high order only because integral additivity makes exact polynomials satisfy it automatically — cell averages carry the invariant, point values don't. The grilled G1 combination (constrained AND tricubic) is unbuildable; the switchable-arm structure absorbs the correction:

- **Arm B (new DEFAULT): plain tricubic q=4** — 1D weights e.g. [−7,105,35,−5]/128 (η=+1/4, centered). Prediction: p_obs ≈ +2.
- **Arm A (diagnostic): maximal-order restriction-compatible fill, q=2** — unique symmetric 3-node pair [−1,8,1]/8 / [1,8,−1]/8 (exact R∘P=I for arbitrary data, linear-exact). Prediction: p_obs ≈ 0. Value: if tricubic also fails the E0′ gate, the two failure slopes separate order-vs-compatibility before the Freret–Groth escalation.
- INI key values renamed accordingly: `seam_ghost_fill = injection | restriction-compatible | tricubic` (default `tricubic`).

The N0 unit test encodes the theorem executably: it asserts the compatible arm's R∘P=I to round-off on **random** data, and asserts the tricubic mean defect on f=x² equals H²/16 **exactly** (expected, not a failure).

---
## comment by szaghi at 2026-07-02T20:10:28Z
url: https://github.com/szaghi/adam/issues/21#issuecomment-4870076986

## N3 / E0′ — gate verdict: mechanism VALIDATED (p_obs = +1.1/+1.4 on the clean instrument); remaining blocker is an infrastructure defect (unrefreshed 3rd ghost layer), NOT the interpolant. No Freret–Groth escalation.

All runs: `rmf-amr-fd` / `rmf-amr-fd-pulse`, marker ON, `-np 1`, matched physical time t = 7.8179e-12 (it_max = 5/10/20 at ni = 16/32/64, dt ∝ h via fixed CFL), work-dir INIs, strictly serial. Injection bit-identity leg: N2 already proved bit-identical histories+residuals vs the E0 baseline at ni=16 — the refactor is behavior-clean.

### 1. First result: the coil case is NOT a valid convergence instrument

The tricubic and compatible ladders on `rmf-amr-fd` both came out at **p ≈ −1 — identical to injection** (tricubic 1.514e-7 / 3.029e-7 / 6.486e-7). But the step-1 rows expose the confound:

- **Step-1 seam div(B) converges at p = +2.0, exact to four digits, for BOTH arms** (tricubic 1.213e-9 / 3.032e-10 / 7.580e-11 — ratios 4.0000, 4.0001). The instantaneous seam production obeys the design arithmetic.
- The matched-time max is growth-dominated, and the growth driver is the **coil filament**: div(J) of the stamped line current scales ~h⁻² in the history (3.2e-5 / 1.38e-4 / 5.3e-4), so seam-adjacent field amplitudes and gradients are themselves h-divergent. The matched-time criterion on this case measures fill-error × coil-field-divergence — the plan's own "analytic caution" (p_obs ∈ [−1,6] all legitimate) materialized. **Consequence: E0's original p ≈ −1 on this case carries the same contamination; the D5 pulse case is the gate instrument from here on.**

### 2. Second result: the true remaining defect is the never-refreshed 3rd fine ghost layer

Found statically in N1 and now confirmed dynamically: `ijk_mmd_ghost` (portion<0) allots the coarse→fine exchange only `ngc/2 = 1` coarse donor layer → **2 of the 3 fine ghost layers are refreshed; layer 3 is never touched after IC** (it keeps its t=0 value — matching the session-2 "2-cell skin" observation). The 6th-order curl (half-stencil 3) reads that stale layer every step, at every seam, under every fill regime.

Discriminator on the pulse case (`fdv_order = 4` confines the curl to the two refreshed layers):

| pulse case, tricubic | ni=16 | ni=32 | ni=64 | p_obs |
|---|---|---|---|---|
| fdv_order = 6 (reads stale layer 3) | 96.78 | 183.15 | — | **−0.92 diverges** |
| fdv_order = 4 (refreshed layers only) | 10.154 | 4.726 | 1.747 | **+1.10, +1.44 CONVERGES** |

(The earlier o4 test on the coil case had NOT shown this — the filament contamination masked it. The pulse case unmasks it cleanly.)

### 3. The gate, on the clean instrument (pulse, o4, matched t)

| arm | ni=16 | ni=32 | ni=64 | p_obs |
|---|---|---|---|---|
| injection (q=1) | 228.87 | 228.25 | — | ≈ 0 (flat) |
| restriction-compatible (q=2) | 126.08 | 118.48 | — | ≈ +0.1 |
| **tricubic (q=4)** | **10.154** | **4.726** | **1.747** | **+1.10, +1.44** |

- **GATE: PASS for tricubic** — p_obs ≥ +1 on both ratios, slope steepening toward the predicted +2 as sub-leading terms die; magnitude 130× below injection at ni=64; growth-in-time flattens with refinement (×1.54 over 4 steps at 16 → ×1.03 over 19 steps at 64): bounded, not secular.
- **G1 A/B answered:** the exact-R∘P=I arm (q=2) buys a constant (~2×) but **zero slope** — order is load-bearing, the point-value Guzik-constraint transplant is not (consistent with the incompatibility theorem posted at N0). The constraint question is closed.
- **Pre-registered E1a invariant held in every interpolated run:** pulse div(D) stays at round-off (≤ 1e-13) under tricubic and compatible fill — partition of unity preserves the structural zero, as the N0 unit test predicted.

### 4. Fork decision

**No Freret–Groth escalation.** G8's escalate-on-FAIL presumed the interpolant was the failing element; the battery instead localized the failure to a pre-existing exchange defect that ANY ghost-fill mechanism (including F-G native-resolution ghosts) sits on top of. The M-A mechanism is validated at its own job.

**Proposed next milestone — N3.5 (donor-range widening, needs sign-off before code):** extend the coarse→fine donor range from `ngc/2` to `(ngc+1)/2` coarse layers in `ijk_mmd_ghost` (portion<0), with fine-index clipping in the three map builders (count + fill, local / MPI-recv / MPI-send in lockstep — the extra coarse layer produces 2 fine indices of which only ghost-layer-3 is in range; the 4th must be clipped, breaking the rigid ×8 row arithmetic). Then re-run this gate at `fdv_order = 6`; acceptance = tricubic p_obs ≥ +1 on both pulse ratios at o6. Risk: the clipping touches the send/recv buffer-count lockstep — exactly the kind of change the injection bit-identity leg exists to police (2-layer rows must stay bit-identical; only new layer-3 rows may appear).

*Housekeeping: seam div(B) magnitudes on the pulse case are O(10)–O(100) on |B|=10 fields because div carries 1/h units at h = 1.875e-4÷4.7e-5 — the CONVERGENCE RATIO is the metric, per G2/plan-G2's redefined acceptance. The N4 check.sh rewrite should pin ratios, not magnitudes.*


---
## comment by szaghi at 2026-07-03T04:23:37Z
url: https://github.com/szaghi/adam/issues/21#issuecomment-4872571017

## N3.5 — stale-layer fix landed: GATE PASSED AT PRODUCTION ORDER 6 (p_obs = +1.15 / +1.62)

**The fix.** `ijk_mmd_ghost` (portion<0) now allots `(ngc+1)/2` coarse donor layers instead of `ngc/2` — the floor-instead-of-ceil that left fine ghost layer `ngc` permanently stale for odd `ngc`. The widened range emits one out-of-slab fine octant per donor pair; all three map builders (local, MPI-recv, MPI-send) clip it with the identical predicate on the identical walk order. Because the send rows are built in the receiver's frame (same `ijk_mmd_ghost` call — single source), the sender evaluates the receiver's fine index and skips the same octants: **buffer positions stay in lockstep with no shipped-and-discarded values.** A design fact that de-risked everything: per-fec buffer allotments were always `grid%weight_neighbor` = the FULL fine ghost slab (face `ngc·nj·nk`), so the old packing *underfilled* its allotment and the fixed packing fills it exactly — MPI message lengths and buffer sizes are unchanged by construction.

### The re-gate (pulse case, fdv_order = 6 — the production configuration, tricubic, matched t)

| | ni=16 | ni=32 | ni=64 | p_obs |
|---|---|---|---|---|
| before N3.5 | 96.78 | 183.15 | — | −0.92 (diverging) |
| **after N3.5** | **12.650** | **5.700** | **1.852** | **+1.15, +1.62 — PASS** |

Both ratios above the +1 gate, steepening toward the predicted +2; growth-in-time flattens with refinement (×1.8 over 4 steps at ni=16 → ×1.03 over 19 steps at ni=64 — bounded, not secular); pulse div(D) at round-off in every run (the structural invariant, held throughout).

### Verification battery (all green)

- **No-seam bit-identity:** CPU goldens 4/4 at digest level — same-level and fine→coarse paths untouched.
- **MPI lockstep:** `rmf-amr-fd` at `-np 2` reproduces the `-np 1` seam div(B) history **bit-for-bit** — the clipped send/recv walk is provably symmetric. (Observation, pre-existing: the divergence-history writer reports rank-local values — the blocks column shows 18 vs 36 and the div(J)/div(D) maxima differ when their argmax cells live off rank 0. Worth a small issue; diagnostic-only.)
- `rmf-amr` structural PASS; FNL build + goldens 4/4 (flag-4 guard untouched).
- New coil-case baselines (default tricubic, layer 3 now live): seam div(B) @s5 = 1.5558e-7; **coil-case div(D) at step 1 improved ~500×** (3.90e-8 → 7.64e-11) — the stale layer was feeding div(D) as well.

### Status of the #21 goal after N3.5

G2 ("seam div(B) converges under refinement at a defensible order and is bounded") is now **empirically met on the source-free oracle at the production discretization**: p_obs ≥ +1 on both ratios, bounded growth. Remaining to close the N-ladder: **N4** — rewrite `rmf-amr-fd/check.sh` + `rmf-amr-fd-pulse/check.sh` to the redefined acceptance (control ≤ 1e-13; seam value pinned to the new baselines; `--convergence` 2-rung ratio assertion; the 1e-13 pointwise seam criterion formally retired in the regression README) — and **N5** close-out. E1b′/E2′ re-runs (does cleaning now behave, with the source at h²?) are the natural post-N4 checks.


---
## comment by szaghi at 2026-07-03T06:51:33Z
url: https://github.com/szaghi/adam/issues/21#issuecomment-4873432558

## N4 — acceptance rewritten to the redefined frame; E1b′/E2′ re-run: cleaning no longer crosses over

**check.sh rewrites (staged, with the pulse case itself — it was still untracked):**
- `rmf-amr-fd/check.sh`: control ≤ 1e-13 + seam max|div(B)| pinned to **1.555802e-7 ± 5%** (N3.5 baseline, tricubic default). No convergence assertion here — per N3 the coil filament (div(J) ~ h⁻²) invalidates this case as an order instrument; the header says so.
- `rmf-amr-fd-pulse/check.sh`: two-invariant oracle — control ≤ 1e-13 both divergences; **seam div(D) ≤ 1e-13 as a structural invariant** (partition-of-unity fill of the z-invariant pulse); seam div(B) pinned to **1.265004e+1 ± 5%**; `--convergence` runs the 16→32 matched-time ladder and asserts **p_obs ≥ 0.8** (live run: p_obs = 1.150). Both PASS end-to-end; both now clean their own heavy artifacts (WSL/CI disk discipline).
- **README: the 1e-13 pointwise seam criterion is formally retired** in a new "AMR seam cases" section (acceptance table, instrument-validity note, rebaseline-as-golden-refresh rule), pointing at #21 §1.

**E1b′ (200-step growth, tricubic + layer-3 fix, coil case):** still ~t³ secular, s200 = 1.147e-2 ≈ the injection-era 1.081e-2. The seam fix buys the h-scaling (E0′), not the fixed-h late-time growth — that is coil-source-driven, consistent with the N3 contamination finding.

**E2′ (GLM chi=1.0 + tricubic seam vs E1b′, matched steps):** **no crossover** — cleaned/uncleaned = 0.18 (s40), 0.11 (s80), 0.27 (s120), 0.62 (s160), 0.88 (s200). Versus the injection-era E2: crossover at ~s120 and ×3.1 worse at s200. The pre-registered oracle passes; caveat recorded: the margin erodes late as the coil source keeps pumping — a longer horizon or a chi sweep would locate whether a crossover still exists out there, but on the truncation-order seam alone (pulse case) cleaning is not needed for boundedness.

Remaining: **N5 close-out** (acceptance boxes, parity-debt pointers, final staging).

---
## comment by szaghi at 2026-07-03T07:03:19Z
url: https://github.com/szaghi/adam/issues/21#issuecomment-4873556201

## N5 — close-out: the N-ladder is complete; G2 is met; acceptance boxes ticked

**Delivered, commits N0–N4 (`c0202c42` → `22141f0d`):** the tricubic coarse→fine seam ghost fill (`[amr] seam_ghost_fill`, default `tricubic`, with `restriction-compatible` and `injection` as first-class arms), the stale-ghost-layer fix (`ijk_mmd_ghost` ceil-widening + symmetric octant clipping), and the redefined ratio-based acceptance wired into `check.sh` + README. Verified state:

- **G2 met at production order:** pulse-oracle seam div(B) converges at p_obs = +1.15/+1.62 (16/32/64, matched t), bounded in time; asserted continuously by `rmf-amr-fd-pulse/check.sh --convergence` (floor 0.8).
- Seam div(D) on the pulse is a **structural zero** (partition-of-unity), asserted at ≤ 1e-13.
- GLM cleaning across the seam no longer amplifies: no crossover in 200 steps (was: crossover at s120, ×3.1).
- Every no-seam path bit-identical throughout (goldens 4/4+4/4 at each milestone); MPI seam exchange bit-identical to the local path at −np 2.

**On the §8 "Path T OR Path M" box:** the executed path was a hybrid, and honesty demands the record say so. The fork chose **Path M** (E0: consistency defect, not truncation) and M-A selected the interpolation mechanism; but the battery then showed the binding defect was the **exchange infrastructure** (the never-refreshed outermost ghost layer), and once fixed, the seam leak became exactly what **Path T** presumes — ordinary truncation — so Path T's acceptance shape (convergence ratio + boundedness + pinned baselines) is what landed. The Path-M sub-clause "row-partition verified on the live seam" was **not** executed: M-A left the q(B) double-correction question parked as it is only reachable via the flux-form δF path (Wang, parked separately).

**Deferred-items register (nothing silently dropped):**

| item | where it lives |
|---|---|
| FNL port of the interpolation kernels | parity-debt guard + note at `adam_fnl_maps_object.F90` (copy refuses flag-4 maps); belongs to the FNL intra-realm-AMR epic |
| Wang δF / fully conservative FD | parked per maintainer directive (issuecomment-4868711291); trigger = closed-domain ∮F·n oracle on the FD path |
| q(B) double-correction / row-partition | parked with δF (only reachable on that path) |
| Closed-domain ∮F·n oracle | #21 backlog (D9), fv pulse variant is the natural host |
| Divergence-history writer reports rank-local maxima under MPI | observed at N3.5 (−np 2: blocks column 18/36, div(J)/div(D) argmax off-rank); diagnostic-only — deserves a small issue |
| E2′ late-margin erosion | cleaned/uncleaned ratio rises to 0.88 by s200 under the coil's h⁻² source; a chi sweep / longer horizon would map it — production relevance only for long coil-driven AMR runs |
| Quiescent-seam isolation | dropped by grilled decision D5 (pulse position is free); recorded, not forgotten |

**Recommendation:** #21's scope as rebased — seam divergence control for cell-centered PRISM, E-series verdicts, mechanism decision, implementation, redefined acceptance — is delivered and continuously asserted by the committed checks. I recommend **closing #21**, with the deferred-items register above as the pointer for successors. Closure is the maintainer's call.


---
## comment by szaghi at 2026-07-03T07:28:27Z
url: https://github.com/szaghi/adam/issues/21#issuecomment-4873813632

# Closing: seam divergences are now bounded and 2nd-order convergent — a stated, measured, continuously-asserted accuracy contract

This issue rebased the open remainder of #13 onto corrected premises and asked one question: **is the seam div(B) leak of the cell-centered FD path an ordinary truncation effect, or a consistency defect — and in either case, what controls it?** The answer turned out to be richer than either fork anticipated. This comment is the consolidated summary and the record of what the 2:1 seams now cost, exactly.

## What was delivered

Five commits (plus the P0/P1 preludes already logged above):

| commit | content |
|---|---|
| `d4ebad20` | P1: `rmf-amr-fd` div(B) oracle + `divergence_history_save` IO key |
| `c0202c42` | N0: seam-interpolation weight-table library + unit test (incl. the executable incompatibility theorem) |
| `c1ef9e25` | N1: ghost-map metadata columns (octant + shift-clamped anchors), provable no-op |
| `6ce0fffe` | N2: the mechanism — `[amr] seam_ghost_fill = injection \| restriction-compatible \| tricubic` (default `tricubic`), pack-side MPI, FNL flag-4 guard |
| `7fb47980` | N3.5: the stale-ghost-layer fix — `ijk_mmd_ghost` allotted `floor(ngc/2)` coarse donor layers, leaving fine ghost layer `ngc` **never refreshed after IC** for odd `ngc`; now `ceil(ngc/2)` with symmetric octant clipping in all three map builders |
| `22141f0d` | N4: ratio-based acceptance in both `check.sh` + README retirement of the 1e-13 criterion + the committed `rmf-amr-fd-pulse` two-invariant oracle |

**End state, measured on the source-free pulse oracle at the production discretization (fd_centered, order 6, matched physical time):**

| | ni=16 | ni=32 | ni=64 | p_obs |
|---|---|---|---|---|
| seam max\|div(B)\|, before | 96.78 | 183.15 | — | **−0.92 (diverging)** |
| seam max\|div(B)\|, after | 12.650 | 5.700 | 1.852 | **+1.15, +1.62 (converging)** |

Seam div(D) on the pulse is a **structural zero** (≤ 1e-13, partition-of-unity argument, asserted); growth in time flattens with refinement (bounded, not secular); GLM cleaning across the seam no longer amplifies (was: crossover at step ~120, ×3.1 worse at step 200; now: cleaned ≤ uncleaned at every matched step). Every no-seam path stayed bit-identical throughout (CPU+FNL goldens 4/4+4/4 at every milestone), and the MPI seam exchange is bit-identical to the same-rank path at `-np 2`.

This is not a one-off measurement: `rmf-amr-fd-pulse/check.sh --convergence` re-runs the 16→32 matched-time ladder and **asserts p_obs ≥ 0.8 on every invocation** (currently measures +1.15), and both seam cases pin their baselines at ±5% golden-style. The acceptance guards itself.

## The accuracy contract at a 2:1 seam — stated plainly

The interior scheme is 6th-order and its `div_h(curl_h) ≡ 0` identity holds to round-off (controls: 2e-19 on the coil case, exact 0.0 on the pulse). **Neither survives a 2:1 jump, and the delivered mechanism does not pretend otherwise.** What the seams now cost, by construction and by measurement:

1. **The formal 6th order is NOT preserved across the seam.** The tricubic ghost fill carries O(h⁴) value error; one derivative (the curl/gradient stencils reading up to 3 ghost layers) turns that into O(h³): **local solution consistency on the ~3-cell seam skin is 3rd order**, against 6th in the interior. The reduction is confined to a codimension-1 skin, so integral norms degrade more gently than the max-norm — but any max-norm convergence study that straddles a seam will read ~3, not 6, and should expect to.
2. **Seam div(B) is bounded and capped at 2nd-order convergence.** A second difference of the O(h⁴) ghost error gives an O(h²) divergence residual: the cap is p = +2, measured **exactly** (+2.0000, four digits) on step-1 production ladders, and approached from below (+1.15 → +1.62) by the matched-time maxima, which carry pre-asymptotic transients. It is *not* machine zero — consistent with the verified SOTA (no cell-centered method achieves machine-zero seam div(B) without staggered storage) — and it is *not* the old p ≈ −1 divergence, which is dead.
3. **Both caps are properties of the CHOSEN fill order, not fundamental obstructions.** A tri-quintic fill (q = 6, 6³ footprint) would raise the skin to 5th-order solution / 4th-order div(B) at the cost of a wider donor footprint and more shift states — a costed, mechanical extension of the same weight-table + metadata machinery, should a use case ever demand it (see successor issue D below).
4. Distinguish this from Wang-2025's cap: their "conservation enforcement limits conservation-error convergence to 2nd order" concerns **flux telescoping** on the parked δF path — a different quantity that happens to share the number. Nothing delivered here enforces FD-path conservation; the coincidence should not be read as a connection.

## What we learned (the findings that outlive the fix)

1. **The E0 verdict was right for a subtler reason than it knew.** The gate measured p ≈ −1 (a consistency defect, Path M) — but on an instrument later shown to be contaminated: the rmf coil filament has div(J) ~ h⁻², so matched-time seam metrics on `rmf-amr-fd` measure fill-error × source-divergence. **The coil case remains a regression anchor but is not an order instrument; the pulse case is.** (Both `check.sh` headers say so.)
2. **The Guzik conservation constraint does not transplant to point values — provably.** Any interpolant exact on quadratics fills the octants of f = x² with values whose 8-mean ≠ the anchor value, so exact restriction-compatibility R∘P = I caps ghost accuracy at q = 2. The FV constraint survives high order only because cell averages satisfy it via integral additivity. The A/B experiment confirmed the theorem: the compatible arm buys a constant, never a slope — **order is load-bearing; the constraint is not.** Pinned executably in `test_seam_interpolation`.
3. **The binding defect was infrastructure, not interpolation.** With ngc = 3, the coarse→fine exchange refreshed only 2 of 3 fine ghost layers (`floor` vs `ceil`), so the 6th-order curl read one stale layer at every seam, every step, under every fill regime — one bug producing the p ≈ −1 signature no ghost-fill order could fix, and explaining the historical "2-cell skin" observation. A satisfying detail: the per-fec buffer allotments (`weight_neighbor`) were sized for the **full** ghost slab all along — the fix makes the exchange fill its designed allotment, MPI message lengths unchanged by construction.
4. **Mechanism validation needed three instruments**: step-1 ladders (instantaneous production: tricubic p = +2.0000 while the matched-time max still diverged), `fdv_order = 4` (the stale-layer discriminator), and coil-vs-pulse (source contamination). None alone was conclusive; pre-registered oracles and grilled amendments kept the diagnosis honest.
5. **Cleaning is now an option rather than a liability.** With the seam source at truncation order, GLM (chi = 1.0) holds cleaned ≤ uncleaned over the full 200-step coil-case window; the late-window margin erodes (0.88 at s200) under the coil's divergent source — noted, not alarming, irrelevant to source-free regions.

## Successor work — draft plans for the next issues

Nothing below is silently dropped; each item has enough scoping here to open as its own issue by copy-paste.

**Issue A — FNL intra-realm AMR: port the seam machinery to the GPU backend** *(the epic; ex-#13 §7.5.9)*
Current state: FNL cannot run an AMR seam — `apply_reflux_to_stage_forest` is a deliberate no-op, and `maps_fnl_object%copy_cpu_gpu` **refuses** flag-4 maps (guard landed at N2, with the parity-debt note in place).
Draft milestones: (A1) device weight tables via `declare create` + `update device` (the FDV-Phase-0-validated pattern) and the flag-4 gather branch in `update_ghost_local_gpu_dev` + the MPI pack twin — branch-free gather-with-weights, metadata unpacked with the same `ibits` helpers; (A2) remove the copy guard behind a capability flag; (A3) FNL reflux twin for the FV path (write `q_rk_gpu(...,stage)` under `!$acc parallel loop`, plan already sketched at `adam_prism_fnl_object.F90:2381-2389`); (A4) acceptance = pulse oracle on FNL within digest tolerance of CPU + `--convergence` green on FNL + the 4 goldens; every milestone dual-backend firewalled. Risks: nvfortran TBP-dispatch history (the `associate` workaround), device-side integer intrinsics audit.

**Issue B — fully conservative FD path (Wang-2025 δF), parked-not-dead** *(maintainer directive, issuecomment-4868711291)*
Trigger: a demonstrated FD-path conservation defect, measured by the prerequisite deliverable — the **closed-domain ∮F·n oracle** (D9 backlog; natural host = an `fv_centered`/closed-BC variant of the pulse case, no coils). Draft milestones: (B1) the oracle case + check; (B2) if it fails at seams: flux-point interface storage + per-RK-stage scaled accumulation + end-of-coarse-step δF correction, per arXiv:2511.08335; (B3) resolve the **q(B) double-correction / row-partition** question (parked here, only reachable on this path: reflux and δF both target q rows — partition must be decided and verified on the live seam); (B4) accept and document the 2nd-order conservation-error cap. Explicitly orthogonal to the divergence work delivered here — layers alongside the ghost fill, never replaces it.

**Issue C — MPI-correct divergence/energy history writer** *(small, diagnostic-only)*
Defect: the history writer reports rank-local values — at `-np 2` the blocks column shows 18 (rank 0's share of 36) and div(J)/div(D) maxima differ from `-np 1` whenever the argmax cell lives off rank 0 (observed at N3.5; div(B) matched only because its argmax happened to be rank-0-resident). Fix: `MPI_Allreduce(MPI_MAX)` on the divergence maxima (and SUM on energies/blocks) before rank-0 writes. Acceptance: `-np 2` history bit-identical to `-np 1` on all columns for `rmf-amr-fd`; goldens untouched (residuals path already reduces).

**Issue D — optional: tri-quintic seam fill (raise the seam caps)** *(only if a use case demands it)*
Scope: q = 6 weight tables (6³ footprint, more shift states) in the existing library + metadata bit-widths; predicted seam solution skin 5th order, seam div(B) 4th order. The E0′ ladder + `--convergence` machinery measures it for free. Cost driver: block-size floor rises (ni ≥ 6) and corner shift-state count grows; everything else is mechanical.

**Issue E — #11 addendum: `var_Jx/Jy/Jz` undefined under `divergence_correction = hyperbolic` + `constrained_transport = no`** *(latent UB, found during E2 spec work)*
The `DIV_CORR_VAR_HYPER` branch of `prism_physics_object%initialize` dispatches on the CT flags with no else: that combination leaves the J-row indices undefined and the cleaning eigen-pointers null. One-line fix (else-branch mirroring the default 7/8/9 case) + an input-validation error, plus a doc note that CT flags select *which field is cleaned*. Belongs under #11's nv/CT reconciliation umbrella.

**Also recorded:** the E2′ late-margin erosion (chi sweep / longer horizon, production guidance for long coil-driven AMR runs — fold into Issue C's neighborhood or a small study note), and the quiescent-seam isolation dropped by grilled decision D5 (pulse position is free — redundant, not forgotten).

## Closing

The rebased scope of this issue — premise correction, gate experiment, mechanism decision on paper, implementation CPU-first with the dual-backend firewall, redefined acceptance with the 1e-13 criterion formally retired — is delivered, committed, and self-asserting, with the seam accuracy contract now stated explicitly: **6th order interior, 3rd-order solution skin, 2nd-order-convergent bounded divergences at the jumps.** Successor work is scoped above, ready to be opened as issues A–E.

Closed as complete.

