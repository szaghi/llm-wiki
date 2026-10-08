# #31 Inter-realm 1:1 mirror seam leaks div(B) on source-free pulse (same-resolution, refinement-divergent — distinct from #29)

state: closed | opened: 2026-07-07T06:38:15Z | closed: 2026-07-07T08:22:29Z | author: szaghi
url: https://github.com/szaghi/adam/issues/31

## Inter-realm 1:1 mirror seam leaks div(B) on a source-free y-pulse (same-resolution seam, refinement-divergent — a distinct defect from #29)

### Summary

The **inter-realm 1:1 mirror seam** (two same-resolution realms glued by `coupling = mirror`) injects a large `div(B)` source on a source-free electromagnetic pulse — **93 at step 1 → ~1600 at step 100** — even though the seam is same-resolution, grid-aligned, and the copy machinery is exact. This is a **different defect from #29** (the intra-realm 2:1-jump seam): #29 is truncation-convergent and fundamental; this one is refinement-**divergent** and should be machine-zero (a same-resolution mirror copy must be div-free-neutral — and it IS, for constant fields). Likely **fixable**.

### Reproducer

New case `src/tests/prism/regression/rmf-2realm-fd-pulse/` (this session): the source-free `rmf-amr-fd-pulse` physics (gaussian +y pulse, J=0, nv=9, fd_centered order 6, ni=16 x-domain) split at x=0 into two same-resolution realms (ni=8 each) glued by a mirror seam. `-np 1`, `it_max=100`, `divergence_history_save=1`.

```
inter-realm 1:1 (this case):   div(B) = 93.4 (s1) -> ~1600 (s100),  div(D) = 0.0
intra-block  1:1 (single realm ni=16 uniform, same physics):  div(B) = 0.0
intra-realm  2:1 (rmf-amr-fd-pulse marker-active, #29):        div(B) = 6.9 (s1) -> 1002 (s100)
```

The inter-realm 1:1 seam leaks **13x more at step 1** than an actual 2:1 resolution jump.

### Characterization (5 diagnostics — decisive)

| diagnostic | result | rules out / in |
|---|---|---|
| uniform CONSTANT field (B_x/B_y/B_z const) | div(B) = **0.0 exact** | **rules out** a copy/plumbing bug — the seam transports constant data perfectly |
| pulse (y-varying B) | 93 -> 1600 | leak needs **tangential** field structure |
| refinement ni 8 -> 16 (matched physical time) | 865 -> **1721 (grows)** | **rules out truncation** (would shrink); ~1/Δx amplification |
| div(D) | 0.0 throughout | source-free clean; div(B)-specific (same asymmetry as #29) |
| cadence α (end-of-step) vs β (stage-coincident) | 93 both | **rules out** stale-ghost timing |

**Signature:** a fixed-size inconsistency in the **tangential-derivative ghost cells** the curl reads at seam-adjacent cells — invisible to constant fields, amplified by 1/Δx. NOT truncation, NOT a copy bug, NOT cadence.

### What is confirmed clean

- Inter-realm fill = `fill_seam_from_peer_forest` **pure copy** (`adam_prism_cpu_object.F90:1211`) — not tricubic, verified.
- Ghost slab is `ngc`-deep with full tangential range (`ghost_slab_extents`, `adam_forest_object.F90:1362`, the "defect-B fix").

So the seam-normal copy depth and values are correct; the defect is in the **tangential** ghost values (or the seam-corner where the x-seam meets the y-Neumann BC crown / BC_SEAM override) that the curl's tangential stencil consumes.

### Likely fixable

Unlike #29 (fundamental, no local FD fix), a same-resolution mirror seam SHOULD be machine-zero — and is, for constant fields. This is a bug in the tangential seam-ghost handling, not a fundamental obstruction. Root-cause in progress (field dump at the seam + z-pulse-vs-y-pulse corner discriminator to isolate corner vs edge).



---
## comment by szaghi at 2026-07-07T06:45:27Z
url: https://github.com/szaghi/adam/issues/31#issuecomment-4900932996

## Root-caused: tangential-CORNER seam ghosts resolve to invalid/wrapped peer cells (not the tangential BC)

### The discriminator that cracked it

Rotating the pulse orientation isolated the mechanism:

| pulse | sets fields | seam-normal (x) deriv term | leaks |
|---|---|---|---|
| +y | Bx(y), Dz(y) | dBx/dx in div(B) | **div(B) = 1407** |
| +z | Dx(z), By(z) | dDx/dx in div(D) | **div(D) = 3.73** |

The leak is always in the **seam-normal (x) derivative of the NORMAL field component** (Bx for +y, Dx for +z). That component is x-**constant**, so `dBx/dx` must be 0 — the seam is injecting a spurious x-variation in the normal component.

### The bug (seam-map dump)

Instrumenting `fill_seam_from_peer_forest` to print the seam-map rows showed the **corner/edge ghosts** — where the x-seam ghost also lies in a tangential (y or z) ghost region — get send-side tangential indices that are **out of the peer interior and/or periodically wrapped**:

```
recv(j,k)=(0,17) <- send(j,k)=(16, 1)   # k: recv 17 -> send 1  (periodic wrap, k mod 16)
recv(j,k)=(0,-1) <- send(j,k)=(16,15)   # k: recv -1 -> send 15 (periodic wrap)
recv(j,k)=(0, 0) <- send(j,k)=(16,16)   # send j=16, but peer nj=8 -> reads a peer GHOST/OOB cell
```

`send j=16` while the peer has `nj=8` (interior 1..8) — it reads a peer ghost/out-of-bounds cell as the source. And `recv k=17 -> send k=1` is a **periodic wraparound** on a **Neumann-BC** tangential direction.

### Root cause

`build_inter_realm_ghost_cell_map` (`adam_forest_object.F90:934-1037`) resolves each seam-face ghost — including the **full tangential ghost slab** `[1-ngc..n+ngc]` (the `ghost_slab_extents` "defect-B fix" that widened the tangential range) — to a peer cell by **global-coordinate matching**. For a tangential-**corner** ghost the global coordinate is *outside* the domain tangentially, so the match wraps/clamps to an invalid peer cell instead of recognizing that this ghost belongs to the **tangential physical BC** (Neumann here), not the seam.

- Constant field hides it (all tangential values equal → wrap reads the same value).
- y-varying field exposes it as spurious `dBx/dx`.
- Refinement amplifies it (1/Δx on a fixed-size corner inconsistency) — matches the measured refinement-divergence.

### The fix (clear)

A seam-face ghost that also lies in a tangential-BC ghost region (`j` or `k` outside `[1,n]`) must **not** be seam-filled from a wrapped/OOB peer cell. It must defer to the tangential BC (or the tangential neighbor if that direction is itself a seam/periodic). I.e. the seam ghost fill should cover only the tangential-**interior** strip of the seam face (`j∈[1,nj], k∈[1,nk]`); the corner/edge ghosts belong to the tangential BC. The **intra-block** ghost exchange handles the same corner correctly (div(B)=0 in the single-realm case) — mirror that behavior.

### Reproducer / future regression

`src/tests/prism/regression/rmf-2realm-fd-pulse/` reproduces it (ni=8, it_max=100, -np1). The uniform-field variant (`type = uniform_field`, constant B) is the clean baseline (div=0). Once fixed, this case asserts inter-realm 1:1 div(B) ≤ round-off — the GREEN regression.


---
## comment by szaghi at 2026-07-07T06:59:18Z
url: https://github.com/szaghi/adam/issues/31#issuecomment-4901029498

## Update: initial root-cause was WRONG — corner-ghost fix ineffective; deeper diagnosis needed

The tangential-corner theory in the previous comment is **falsified**. Correcting the record:

- **The "send j=16 / periodic k-wrap" reading was a misparse.** This case has `nj=nk=16` (only `ni` is split to 8), so `j=16` is a valid *interior* peer cell, not a wraparound. Instrumenting `find_peer_cell` found **zero** out-of-range index matches — its bounds guards are correct.
- **A corner-skip fix** (skip seam ghosts whose tangential index is in the ghost region, in `populate_seam_ghost_cells` + `count_seam_ghost_cells`) was implemented and **did not change div(B)** (still 93→1600). Reverted. So corner/edge ghosts are not the source.

What the deeper diagnosis established (all verified):

- **Seam ghost VALUES are exact.** In `fill_seam_from_peer_forest`, the copied peer `Bx` matches self's adjacent interior `Bx` to `diff = 0.0` at every first-layer seam cell. The copy is perfect.
- **The IC is div-free.** `max div(B) at t0 after update_ghost = 0.0`. The leak develops during **evolution**, not from the IC or the static fill.
- **Cadence α vs β: both leak 93.** Not stale-ghost timing.
- **New lead:** the peer realm's `Bx` acquires a small **x-variation** near the seam during evolution (peer i=1: 1.252e-2 vs i=2: 1.254e-2) that must not exist for an x-constant `Bx(y)` pulse. Within a single realm the field stays x-constant (single-realm ni=16 is div-free). So the two-realm system develops spurious x-structure dynamically — a **coupled-evolution** effect at the seam, not a static ghost-fill bug.

**Status:** the defect is real and well-characterized (refinement-divergent, needs tangential field structure, seam values exact, IC clean, evolution-developing), but the precise line-level mechanism is **not yet found**. Reproducer `src/tests/prism/regression/rmf-2realm-fd-pulse/` stands. Candidate next probes: fill only one realm's seam and see if the leak is one-sided; disable the curl's seam-normal term at seam cells; diff the exact order-6 curl-stencil inputs at a seam cell between the single-realm (div-free) and two-realm (leaking) runs.


---
## comment by szaghi at 2026-07-07T07:16:49Z
url: https://github.com/szaghi/adam/issues/31#issuecomment-4901159838

## Re-classified: it's a grid-oscillation (ker D*) instability excited by the seam — a SIBLING of #29, not a quick fix

After deeper probing, the earlier "likely fixable local bug" framing is **wrong** — I over-claimed. The real mechanism:

**The field is div-free in the deep interior.** Excluding the `s1=3` stencil band from each seam edge (leaving the deep-interior cells) gives `div(B) = 2.8e-13` (round-off). The leak lives *only* in the s1-band at the seam skin.

**It is not a diagnostic/ghost-staleness artifact.** Re-filling the inter-realm seam right before the divergence diagnostic did not reduce it; removing the post-step `update_ghost` made it worse. The seam-skin `div(B)` is a real field feature.

**The smoking gun** — dumping `Bx` along x at the seam skin (an x-constant field, should be flat): the seam-coupled realm develops a **±1-cell grid oscillation**:
```
Bx(i=-2..4) = 5.8749 / 5.8787 / 5.8766 / 5.8766 / 5.8787 / 5.8749   (seam-coupled realm)
Bx(i=-2..4) = 5.8760 / 5.8760 / 5.8760 / 5.8760 / 5.8760 / 5.8760   (single-realm, flat)
```
A symmetric sawtooth (~0.06% amplitude) — precisely the **`ker D*` grid-oscillation mode** from Ranocha 2019 (the discretely-div-free-but-not-a-discrete-curl null mode). The seam coupling excites it; `div(B)` then amplifies it by `1/Δx` (explaining the refinement-divergence).

**This is the same mechanism class as #29** (the 2:1-jump seam div(B)). Both are the collocated `ker D*` grid-oscillation mode getting excited where the mimetic `div_h(curl_h)=0` commutation is perturbed at a seam — #29 by a resolution jump, #31 by the inter-realm ghost-swap coupling at matched resolution.

**Fix outlook (revised, honest):** likely not a quick local fix. #29's analogous instability had no local FD fix (→ accept-truncation). #31 may need the same SBP-compatible seam treatment, a grid-oscillation filter (Ranocha Eq. 55 F-projection) at the seam, or a seam-coupling reformulation that doesn't perturb the operator commutation. Verified NOT a value/fill/index bug — the seam copy is exact, the map indices are correct, the IC is div-free.

Downgrading the "fixable" expectation; treating #31 as a sibling of #29. Reproducer `rmf-2realm-fd-pulse` stands.


---
## comment by szaghi at 2026-07-07T07:50:07Z
url: https://github.com/szaghi/adam/issues/31#issuecomment-4901409629

## FIXED — it was the inter-realm machinery, exactly as suspected. Two defects, both resolved.

You were right on both counts: a 1:1 inter-realm seam must be identical to a 1:1 intra-realm block interface (proven div-free), and it is now. The "Ranocha instability" conclusion was wrong — I retract it. Two distinct inter-realm-machinery defects:

### Defect 1 (evolution): α cadence leaves the seam unfilled during RK substages

With `coupling_cadence = end_of_step` (α, the default), `fill_seam_from_peer_forest` runs only ONCE per step (Phase 5). During RK substages 2..N the residual's stage buffer `q_rk(:,...,k)` has **unfilled (zero) inter-realm seam ghosts** — the curl reads them and the field genuinely evolves wrong at the seam skin (a ±1-cell oscillation grows).

Measured (dumping the -x seam ghost inside the residual): `-xghost = 0.0, 0.0, 0.0` while `interior = 6.44` — the seam ghosts are simply not there in the stage buffer.

**Fix:** `coupling_cadence = stage_coincident` (β) fills the seam every substage → the field is seam-coherent at every stage → div-free. This is the physically correct cadence for a same-resolution, same-timestep 1:1 seam (α's end-of-step lag is a Berger-Oliger AMR-subcycling convention, not div-preserving for a 1:1 mirror seam).

### Defect 2 (diagnostic): the div(B) diagnostic doesn't refill the inter-realm seam

`post_step_forest`'s div(B) diagnostic uses `self%update_ghost`, which fills intra-realm ghosts + BCs but NOT the inter-realm seam. The div stencil then reads stale seam ghosts at the seam skin → spurious div(B), even when the field is div-free.

**Fix:** re-establish the inter-realm seam from peers on the committed `q` before the divergence diagnostic (15 lines in `adam_prism_cpu_object.F90`, guarded by `present(realm)` so non-forest cases are untouched).

### Result

With β cadence + the diagnostic fix, the inter-realm 1:1 pulse is **div(B) = div(D) = 0.0 to machine precision, all 100 steps** — identical to the intra-realm 1:1 case. Verified:
- Firewall: single-realm `rmf-amr-fd-pulse` (2:1 AMR) bit-identical to golden (12.650036).
- No regression: `rmf-2realm` (α coil case) byte-identical.

The reproducer `rmf-2realm-fd-pulse` (now β) becomes the GREEN regression. Closing after the fix lands.

### Note for α

α cadence still leaks (it's a genuine evolution error for a 1:1 div-constrained seam, not fixable by the diagnostic). If α must be div-preserving for some AMR-subcycling use case, that's a separate, harder item — but for 1:1 mirror seams β is correct and required.


---
## comment by szaghi at 2026-07-07T08:22:28Z
url: https://github.com/szaghi/adam/issues/31#issuecomment-4901665101

## Resolved — fixed on both backends (b710690a CPU, 3cbecc7b FNL)

The inter-realm 1:1 mirror seam is now exactly div-free (div(B) = div(D) = 0 to machine precision), identical to the intra-realm 1:1 case — as it must be. Two defects, both fixed on CPU and FNL:

1. **Evolution / cadence:** with `coupling_cadence = end_of_step` (α, the default), the seam is filled only once per step, so during RK substages 2..N the residual reads unfilled (zero) inter-realm seam ghosts. Fix: `stage_coincident` (β) fills the seam every substage — the physically correct cadence for a same-resolution, same-timestep 1:1 seam. (The reproducer `rmf-2realm-fd-pulse` ships with β.)
2. **Diagnostic:** `post_step_forest`'s div(B) diagnostic used `self%update_ghost`, which doesn't refill the inter-realm seam → the div stencil read stale seam ghosts. Fix: re-fill the seam from peers before the divergence diagnostic (present(realm)-guarded).

Verified: inter-realm 1:1 pulse (β) div(B)=0 on both backends; firewall — single-realm rmf-amr-fd-pulse bit-identical to golden (12.650036); no regression on rmf-2realm (α coil). New GREEN regression: `rmf-2realm-fd-pulse`.

**Remaining caveat (not blocking closure):** α cadence still leaks on a div-constrained 1:1 seam — a genuine evolution error (per-step, not per-substage, coupling), not a diagnostic artifact. For 1:1 mirror seams β is correct and required. Making α div-preserving for an AMR-subcycling use case is a separate, harder item; if that becomes needed it warrants its own issue.

Closing.

