# #30 Route 2 (PARKED): CT/staggered B at the 2:1 AMR seam — activates only if a workload needs it

state: open | opened: 2026-07-06T20:19:38Z | closed: - | author: szaghi
url: https://github.com/szaghi/adam/issues/30

## Route 2 (PARKED): CT/staggered B at the 2:1 AMR seam — activates only if a workload needs it

**Status: PARKED.** Do not implement speculatively. This issue activates ONLY if a production workload exceeds the `[IO].seam_divB_tol` guard-rail (issue #29) on a run where the O(h^p) seam div(B) floor actually corrupts the physics.

### Why parked

Issue #29 established (with five fix classes ruled out) that PRISM's collocated high-order **FD** path has **no local div(B) fix** at a 2:1 AMR seam — the mimetic `div_h(curl_h)≡0` identity breaks at the resolution jump (Ranocha commutation), and no value-transfer restores operator commutation (the R∘P≠I wall). The resolution adopted is **accept-truncation**: the seam source is O(h^p) refinement-convergent, unbounded only in t at fixed h, and monitored by the `seam_divB_tol` guard-rail.

Route 2 is the **only remaining route to an exact seam div(B) bound**, but it is a large structural change against PRISM's collocated-FD core design, so it is not justified unless a real workload demands it.

### What Route 2 would entail (if activated)

Re-collocate B to a **constrained-transport (CT) / staggered** representation **at the seam** (interior stays collocated-FD):
- B on faces, EMF (E) on edges, so `∂/∂t(div B) = -div(curl E) = 0` by discrete Stokes/telescoping — cell-by-cell, regardless of resolution.
- This is the finite-VOLUME flux-telescoping mechanism where a proven discrete-divergence bound exists (**Mishra & Svärd**, the conservative induction form). PRISM's **reflux / flux-register** machinery (issues #23/#28, Berger-Colella `∮F·n` telescoping across the 2:1 seam) is the FV substrate this would build on — reflux already telescopes fluxes to register parity; Route 2 makes that telescoping carry the div-bound for B.
- Requires: a face/edge B/E representation at seam cells, a collocated↔staggered transfer at the FD/CT boundary, and the Balsara-type div-free prolongation for the 2:1 restriction/prolongation.

### Activation trigger

Open/prioritize this issue when: a production AMR run trips `[IO].seam_divB_error` (or the warn-only monitor shows the floor corrupting a physics observable) AND the mitigations are insufficient — refining h is too costly, shortening the run defeats the science, and the GLM delay (`hyperbolic` + `[physics].c_r`, ~5.5× margin) doesn't buy enough runway.

### References

- Root-cause + fix-class scoreboard: issue #29, and the CLAUDE.md PRISM gotcha "2:1 AMR seam injects an O(h^p) div(B) source".
- SOTA: Mishra-Svärd (conservative-induction div-bound), Balsara 2001/2004 (div-free AMR prolongation), Tóth-Roe 2002 (collocated non-locality), Ranocha 2019 (the commutation obstruction).


