# #29 Seam div(B) fix E1: matched-stencil single-valued seam ghost fill (successor to #13/#21)

state: closed | opened: 2026-07-05T11:51:29Z | closed: 2026-07-06T20:19:53Z | author: szaghi
url: https://github.com/szaghi/adam/issues/29

## Context — the diagnosis (successor to #13, #21)

Closed #13/#21 established that PRISM's cell-centered high-order scheme keeps `div(B)=0` to machine precision on uniform grids (matched `FD1_CC` div/curl pair, `div_h(curl_h)≡0` by operator commutation) but injects a **truncation-order div(B) source at the 2:1 AMR seam**. A dedicated characterization + literature + symbolic session (2026-07-05) pinned the root cause and a fix direction:

- **Empirical (S1/S2):** on the source-free `rmf-amr-fd-pulse` case, seam `max|div(B)|` runs away **6.9 → 1002 over 100 steps at fixed h** (control = 0.0), dt-independent (physical-time, not a CFL instability), and **survives tricubic (q=4/q=6) ghost fill**. GLM hyperbolic cleaning (which is only half of Dedner — the parabolic damping term is absent, a separate defect) suppresses ~5.5× but does not bound it.
- **Scheme-universal:** flipping the pulse case to `fv_centered` reproduces the identical runaway to 4–5 significant figures (FV ≡ FD; reflux active on FV does nothing for div(B) — conservation ≠ solenoidality).
- **Root cause (symbolic, SymPy on exact `FD1_CC`):** NOT variable-coefficient non-commutation (an earlier hypothesis, falsified — each seam cell can be individually consistent AND commuting). The true cause is **inter-cell operator mismatch across the 2:1 jump**: the seam cell and its coarse neighbor differentiate with different stencils, so `div_h(curl_h)` telescoping fails. It telescopes for field degree ≤ 2s and appears at degree 2s+1 (the truncation order). A **single-valued interface operator** (both sides use the same operator at the shared face) drives the residual to **exactly zero** symbolically.

Full analysis, papers, and reproducible symbolic scripts are in the working tree (`untracked/seam-divfree-rootcause-and-hybrid-2026-07-05.md`, `untracked/seam-symbolic-checks/`, `untracked/sota-seam-2026-07-04-papers/`).

## This issue — E1 (the cheapest fix experiment)

Replace the pointwise-accurate tricubic seam ghost fill with a **matched-stencil `SEAM_FILL_MATCHED` regime** that constructs the fine-side ghosts so the fine `curl_h`/`div_h` stencils see the same single-valued interface derivative the coarse side does — restoring `div_h(curl_h)` telescoping at the seam. No new field, no staggering, no CT.

**Key de-risking (symbolic, verified):** the matched single-valued seam derivative is **full interior order** — s=2→order 4, **s=3→order 6** (the pulse case's `fdv_order=6`). The R∘P≤2 wall does NOT bite; matching costs zero accuracy. The concrete s=3 ghost formula is derived (`untracked/seam-symbolic-checks/matched_ghost_s3.py`): fine ghost = degree-2s interpolant through {fine interior 0..−s} ∪ {coarse centers +1.5,+3.5,+5.5}, partition-of-unity and linear-exact verified.

### Plan (full detail: `untracked/plan-issue13-E1-matched-seam-2026-07-05.md`)

- **C1** — add `SEAM_FILL_MATCHED=3` regime + evaluator (formula-pending error_stop guard) + meta bits for seam-normal direction, in `adam_seam_interpolation_library.F90`; INI `case('matched')`; maps thread seam-normal into `seam_meta_pack`. Default stays tricubic; **7 goldens must be bit-identical** (matched fires only on `one_or_eight==4` intra-realm AMR seam rows).
- **C2** — dispatch branch in `interp_seam_ghost` (`adam_field_object.F90:889` local + `:1004` MPI) + FNL twin (`adam_fnl_field_kernels.F90:220`, clean error_stop refusal — CPU-first); thread `s`, `nrm`.
- **C3** — drop the s=3 `SEAM_W_MATCHED` table in (flips RED→GREEN).
- **C4** — `--horizon` RED+GREEN leg on `rmf-amr-fd-pulse/check.sh`.

### RED / GREEN oracle
- **RED (measured):** tricubic, 100-step horizon → 6.9→1002, control 0.0.
- **GREEN:** matched fill → `max_{step≤100}|div(B)| ≤ B_CAP` (~20) AND non-acceleration (`|div(B)|(100) ≤ 1.5·|div(B)|(50)`; RED is 28×), control still 0.0, div(D) structural zero preserved. FD **and** FV should both improve (scheme-universal).

### Biggest risk (pre-C3 gate)
**Ghost-overwrite ordering (R2):** verified that within a stage `update_ghost → curl` lets the fine seam curl see the matched ghosts. OPEN: whether the div source is dominated by the *next*-stage ghost re-exchange (mechanism iii) rather than the stencil mismatch the matched fill fixes. A **freeze-ghost experiment is a pre-C3 gate** — if ordering dominates, E1 bounds nothing regardless of ghost values, and that outcome escalates to E2.

### Decision gate
- **GREEN** → diagnosis proven in-code, cheapest fix landed; promote matched → default candidate, port FNL twin.
- **RED** → single-valued fill at ghost-construction is insufficient → escalate to **E2 (auxiliary single-valued face-EMF, `plan-issue13-E2-*.md`)** and, if the collocated-div consistency trap bites, **E3 (SBP lift/projection, `plan-issue13-E3-*.md`)**.

### Constraints
User commits only; pragma inventory per commit; WSL one-test-at-a-time; judge by the div(B) history numbers (state dump), never a derived diagnostic; firewall = the 7 regression goldens + AMR seam check.sh's + #28 register-parity leg.

🤖 Generated with [Claude Code](https://claude.com/claude-code)


---
## comment by szaghi at 2026-07-06T12:55:31Z
url: https://github.com/szaghi/adam/issues/29#issuecomment-4893025780

## Update: fix direction settled after E1/E2 dead-ended — E3 (matched-resolution seam OPERATOR) proven, C1 landed

### E1 and E2 both RED — and E2 reframed the whole problem
- **E1 (matched ghost VALUES):** implemented, firewall-green plumbing, but RED. Even after re-deriving the weights for PRISM's true 2:1 geometry, div(B) stayed ~q=2 (worse than tricubic early) — the fill was 1D-normal-only; the tangential dimension was 0th-order. Reverted.
- **E2 (single-valued flux VALUES, FV path):** implemented, fires correctly, but NULL — div(B) unchanged. **The decisive diagnostic: the coarse and fine seam B-fluxes ALREADY AGREE to 0.24%** (`|coarse_B|`≈2.94e9, `|fine−coarse|`≈6.95e6), yet div(B) still runs away 1000×. Reverted.

**⇒ THE REFRAME: the div(B) source is NOT a value disagreement.** Neither ghost VALUES (E1) nor flux VALUES (E2) — both already near-single-valued. It is a discrete **OPERATOR / stencil-resolution mismatch**: the coarse side differences with Δx, the fine side with Δx/2, and that breaks the `div_h(curl_h)=0` telescoping regardless of value agreement. Confirms Ranocha 2019 (identity dies where tensor-product structure breaks) + the symbolic root-cause analysis, now at the pipeline level. Both E1/E2 aimed at values; the defect is the operator.

### E3 — matched-resolution collocated seam operator (grilled, then executed)
5 grilled decisions: matched-resolution collocated operator (not staggered lift/projection); narrow seam-band; strongest-achievable compatibility; FD-centered first; hardest go/no-go gate.

**Symbolic proof (T1.0/T1.1), verified, scripts in `untracked/seam-symbolic-checks/`:**
- **A matched seam operator EXISTS at full order 6, exact inter-cell telescoping, well-conditioned (L1=2.49), genuinely distinct from the interior operator** (not a tautology — verified 3 ways).
- No separate curl partner needed (div & curl share the FD1_CC primitive → one matched operator per side).
- **Full 3D div(curl) telescopes to the scheme's order 6** — the seam is no longer a lower-order defect. Machine-zero (all orders) is impossible for finite collocated stencils (Ranocha); order-6-clean matching the interior's own order is the strongest achievable, and achieved.
- **T1.1b correction (caught before Fortran):** the coarse samples the normal operator reads are at coarse tangential resolution → naively they collapse telescoping to order 1 (the E1-class trap). FIX (validated): tangentially interpolate the coarse samples to the fine seam line (9-pt order-6 Lagrange). With that, full 3D telescopes to order 6, realizably.

**The standalone-Python gate was relaxed** (3 model attempts didn't converge — a faithful 2:1 Maxwell model ≈ rebuilding PRISM; each failed its own control-reproduces-runaway validation). Since the telescoping is verified on the REAL FD1_CC operators (not a proxy) and PRISM already has a validated runaway oracle, **PRISM's 100-step horizon on `rmf-amr-fd-pulse` is the acceptance test.**

### C1 landed (staged; user commits)
`compute_derivative1_fd_seam` + weight tables (`FD1_SEAM_FINE` L1=2.49, `FD1_SEAM_COARSE` L1=7.60, `FD_SEAM_TANG` tangential interp) added to `adam_fdv_operators_library.F90`. Builds clean, non-disturbing (not yet called). +1 `!$acc routine seq` for the eventual FNL port.

### Remaining: C2/C3 (focused next work)
Wire the operators into `compute_residuals_fd_centered` at seam cells — a 3D tensor gather (7 normal-matched × 9×9 tangential-interp per seam cell, both fine and coarse sides) + seam-cell identification + cross-block coarse-donor addressing. Then the `rmf-amr-fd-pulse` 100-step horizon is the real test. **The math is proven; C2/C3 is mechanical engineering, no research risk.** The one quantified open risk is the coarse-side operator's L1=7.60 conditioning — the real pipeline settles it.

**This is the first affirmative fix after E1/E2 both dead-ended** — the div(B) source is preventable (order-clean seam), not merely bounded. Fallback if C2/C3 or conditioning surprises: fix-class E (complete PRISM's half-implemented Dedner GLM with the missing parabolic damping term — bounds rather than prevents).

---
## comment by szaghi at 2026-07-06T19:37:30Z
url: https://github.com/szaghi/adam/issues/29#issuecomment-4896889589

## Status update (2026-07-06): E3 CLOSED (unstable), E CLOSED (can't bound), A reframed by a decisive diagnostic → Route 1

The previous comment ("E3 proven, C1 landed") is now **superseded**. E3 was pushed to completion and closed with evidence; fix-class E was implemented and closed; a decisive diagnostic then reframed the standing route. Full detail below. Dead code trimmed; two commits landed (`3cd0541d`, `94df72ee`).

### E3 (matched-resolution seam OPERATOR) — CLOSED: eigenvalue-unstable

The T1.0/T1.1 symbolic proof (`div_h(curl_h)` telescopes to order 6 across the jump) was correct, but **telescoping-exactness ≠ time-stability**. Built the full pair (fine-side `FD1_SEAM_FINE` + coarse-side `FD1_SEAM_COARSE`) and measured the `rmf-amr-fd-pulse` 100-step horizon:

| config | div(B) @s25 | div(B) @s100 |
|---|---|---|
| baseline (RED witness) | 72.8 | 1002 |
| fine-side operator only | 19.0 | 3156 |
| **both operators (the matched pair)** | **8.2e4** | **6.2e18** |

The fine-side alone gave the *first seam intervention with real signal* (73→19 at s25 — E1/E2 were null/worse), but neither bounds, and the pair **diverges catastrophically**. This is the **non-SBP interface instability** that Mattsson-Carpenter 2010 and Ranocha 2019 predict: a matched-difference stencil + ghost fill is eigenvalue-unstable regardless of telescoping. Root mechanism (Ranocha Remark 2.8): `div_h(curl_h)=0` holds only under operator commutativity `D_iD_j=D_jD_i`, which the 2:1 seam (different Δx each side) destroys by construction; the residual lives in the grid-oscillation subspace `ker D*`, O(h^p)/step, accumulating in t. **E3-as-difference-operator is evidence-closed.**

### E (complete the half-Dedner GLM) — CLOSED: correct, but can't bound a persistent source

PRISM's `divergence_correction=hyperbolic` shipped only the **hyperbolic half** of Dedner 2002 — the parabolic **damping** term was absent (`dq(ψ) = -c_h²·div(B)` with no `-(c_h²/c_p²)·ψ`). Implemented it on all 8 psi/phi transport lines + added a tunable `[physics].c_r` (default 0.18). Swept the damping strength on the hyperbolic+CT=B pulse horizon:

| c_r (damping ∝ 1/c_r) | div(B) @s100 |
|---|---|
| 0.05 (strongest) | 858 |
| 0.18 (Dedner nominal) | 644 |
| 0.6 | 384 |
| 5.0 (≈ pure hyperbolic) | 212 |

**Monotonic: weaker damping is better, asymptoting to half-GLM — and it NEVER bounds** (5→212 still runs away). Over-strong damping kills the useful hyperbolic transport; in the weak limit the full GLM cannot bound a **persistent localized source** (Koley-Mishra-Risebro-Svärd 2011) — the seam re-injects each step faster than GLM removes. **E fails to bound.** But the parabolic term is a genuine missing piece of PRISM's GLM, now correct and available — committed as a standalone improvement (`94df72ee`), NOT as the seam fix.

### THE DECISIVE DIAGNOSTIC — the runaway is a CONSTRAINT violation, not an energy instability

Before planning fix-class A (SBP+SAT), measured `energy_history` vs `divergence_history` on the SAME baseline run:

| step | B_energy [J] | div(B) |
|---|---|---|
| 1 | 10155 | 6.9 |
| 50 | 10155 | 36 |
| 100 | 9831 | 1002 |

**‖B‖ is FLAT (−3%) while div(B) runs away 145×.** The state energy is already bounded; **div(B) is what diverges.** This is decisive because a 5-paper SBP-SAT extraction (Mattsson-Carpenter, Almquist-Wang-Werpers, Cheng, Koley, Ranocha) confirms **SBP+SAT provably bounds ‖state‖, NOT div(B)** — Koley 2011 p.14 says so verbatim ("we were unable to obtain such a divergence bound"). So plain SBP+SAT would be **necessary-but-insufficient** — it bounds the invariant that is *already fine*. Caught at PLAN time, zero Fortran wasted (the E3 premise-check lesson applied).

### Standing route: fix-class A, Route 1 — conservative-curl SBP + Mishra-Svärd divergence bound

The only PROVEN discrete-divergence bound in the citation graph is **Mishra-Svärd** (conservative induction form, with a real discrete curl). The fix is **structural** (the conservative-curl structure carries the div bound), not penalty-tuning. Favorable alignment: **PRISM is already Route-1-shaped** — it uses the curl form `dq(B)=-curl_h(D)` with the mimetic FD1_CC pair (machine-zero div(B) in the uniform interior). The seam is where that conservative-curl SBP structure must be extended across the 2:1 jump so the discrete div bound survives. Plan is derivation-first and gated (TA.0 portability check → TA.1 crux lemma → TA.2 standalone-model div-bound gate → Fortran only if green). Honest terminal fallbacks if A also fails: Route 2 (staggered/CT at the seam) or accept-truncation (document the O(h^p) seam floor, cap AMR run length).

### Dead-code trim (both landed)

- `3cd0541d` `revert(lib/fdv)`: removed the E3 matched-difference seam operators (`compute_derivative1_fd_seam`, tangential-interp evaluators, `FD1_SEAM_*`/`FD_SEAM_TANG` — all zero live callers). FDV library now byte-identical to pre-C1. Prototype archived locally.
- `94df72ee` `feat(prism)`: the Dedner parabolic damping + `[physics].c_r` (the E result — a real GLM completion, kept on its own merits).
- Audit confirmed the codebase is otherwise clean: the earlier failed experiments (induction-flux-share, edge-register) were already properly retired; high-order ghost interpolation, reflux, and the mimetic pair are all live and untouched.

### Fix-class scoreboard (all ruled out with evidence except A)

- **E1** (matched ghost VALUES) — RED (tangential-1D-only).
- **E2** (single-valued flux VALUES) — NULL (fluxes already agree 0.24% → reframed to OPERATOR).
- **E3** (matched-difference OPERATOR) — CLOSED (eigenvalue-unstable, 1e18).
- **E** (full Dedner GLM) — CLOSED (can't bound a persistent source).
- **A / Route 1** (conservative-curl SBP + Mishra-Svärd div-bound) — the standing target, planned & gated.

Given the arc, consider renaming/retitling this issue from "fix E1" to the broader "Seam div(B) at 2:1 AMR: fix-class survey → SBP conservative-curl (Route 1)".


---
## comment by szaghi at 2026-07-06T20:19:53Z
url: https://github.com/szaghi/adam/issues/29#issuecomment-4897259779

## RESOLVED: accept-truncation. No local collocated-FD fix exists; guard-rail landed; Route 2 parked.

After five fix classes ruled out with evidence, the 2:1 AMR seam div(B) investigation is resolved as **accept-truncation**. Summary of the terminal and the shipped deliverable.

### Root cause (settled)

PRISM keeps `div(B)=0` to machine precision on uniform grids because `curl_h` and `div_h` share the antisymmetric `FD1_CC` primitive → `div_h(curl_h)≡0` by operator commutation (mimetic identity, Ranocha 2019 Remark 2.8). The 2:1 seam breaks commutation (coarse Δx vs fine Δx/2 → composite is not a tensor product), injecting an **O(h^p) div(B) source in the grid-oscillation subspace `ker D*`**. It is refinement-convergent (`p_obs ≈ +1.15 → +2`) but **unbounded in t at fixed h** (6.9 → 1002 / 100 steps), dt-independent, scheme-universal (FD ≡ FV), and a **constraint violation, not an energy instability** (‖B‖ stays flat while div(B) runs away 145×).

### Fix-class scoreboard (all ruled out)

| Class | Approach | Verdict |
|---|---|---|
| E1 | matched ghost VALUES | RED (1D-normal-only, q=2) |
| E2 | single-valued flux VALUES | NULL (fluxes agree 0.24% → source is the OPERATOR, not values) |
| E3 | matched-difference seam OPERATOR | CLOSED — eigenvalue-**unstable** (both-op horizon → 1e18); non-SBP, Mattsson-Carpenter/Ranocha predict it; telescoping-exactness ≠ time-stability |
| E | full Dedner GLM (parabolic damping) | CLOSED — implemented + tunable `c_r`, but GLM can't bound a persistent source (Koley 2011); c_r sweep 0.05→5.0 all run away |
| A | SBP-norm-compatible seam + weak SAT | CLOSED (analysis + grill) — SBP bounds ‖B‖ (already fine), NOT div(B); a value-transfer can't restore operator commutation across the jump (the R∘P≠I wall, #21) |

The A analysis included a decisive diagnostic (‖B‖ flat while div(B) diverges → SBP+SAT targets the wrong invariant) and a full design grill (G1–G10) that concluded the FD path has no local fix and no flux fallback (reflux is FV-only; the FD `dq(B)=-curl_h(D)` is pure point-curl).

### Shipped: accept-truncation + guard-rail

- **Guard-rail** (`[IO].seam_divB_tol`, default off; `[IO].seam_divB_error`, warn-vs-fatal): a run-time monitor in `save_divergence_history` that fires when seam `max|div(B)|` exceeds tolerance on AMR runs — turning the otherwise-**silent** growth into a visible signal. Reuses the existing per-step `divergence_history`; zero added computation. Verified: disabled-default is bit-identical to the golden; warn-only fires each step past tolerance; fatal mode `error_stop`s cleanly.
- **Documentation**: CLAUDE.md PRISM gotcha with the scoreboard + safe-usage.
- **Mitigation** (delay, not cure): `divergence_correction=hyperbolic` + tune `[physics].c_r` buys ~5.5× margin (the now-complete Dedner GLM, committed separately).

### Route 2 parked

**Route 2** (CT/staggered B at the seam — the only route to an *exact* bound, via Mishra-Svärd conservative-flux telescoping + PRISM's existing reflux) is a large structural change against the collocated-FD design and is **parked** in #30. It activates only if a production workload trips the guard-rail and the mitigations are insufficient.

Closing #29 as resolved (accept-truncation).


---
## comment by szaghi at 2026-07-07T08:22:46Z
url: https://github.com/szaghi/adam/issues/29#issuecomment-4901667705

## Note: FNL backend parity for the GLM work landed (3cbecc7b)

#29 remains resolved as accept-truncation. Recording a follow-up for completeness: the Dedner GLM parabolic-damping term (fix-class E, added to the CPU backend in 94df72ee) was CPU-only — the FNL residual kernel had the hyperbolic transport term without the damping term and never received `c_r`. That gap is now closed (3cbecc7b): the damping term is ported to all 8 psi/phi sites of the FNL device kernel and `c_r` is threaded through, verified cross-backend-identical (FNL c_r sweep matches CPU to printed digits). So the full-Dedner GLM — the delay-not-cure mitigation offered alongside accept-truncation — is now available on both CPU and FNL. No change to the #29 resolution.

