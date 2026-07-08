---
type: Source
title: "Derigs, Winters, Gassner, Walch & Bohm (2018) — Ideal GLM-MHD: about the entropy consistent nine-wave magnetic field divergence diminishing ideal magnetohydrodynamics equations"
description: "Unifies Powell terms and GLM cleaning into a nine-wave, Galilean-invariant, entropy-consistent system; shows some common cleaning extensions violate the second law; entropy-stable fluxes in FLASH."
resource: "doi:10.1016/j.jcp.2018.03.002"
source_kind: paper
authors: [Derigs D., Winters A.R., Gassner G.J., Walch S., Bohm M.]
year: 2018
venue: "J. Comput. Phys. 364:420-467 (arXiv:1711.06269)"
local_file: "~/papers/mosaic/div-free-amr/2018-JCP-Derigs-101016jjcp201803002.pdf"
tags: [glm, eight-wave, entropy, divergence-constraint, mhd, amr]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

Derives the **ideal GLM-MHD system**: starting from compressible Euler and
coupling magnetic fields *while explicitly allowing*
$\nabla\cdot\mathbf{B}\ne 0$, the Powell/Godunov non-conservative terms
emerge as **physically essential** — the classical ideal MHD model is
"invalid for regions where $\nabla\cdot\mathbf{B}\ne 0$" because it
assumes the constraint holds pointwise. Adding GLM cleaning yields a
**nine-wave**, symmetrizable, Galilean-invariant system consistent with
the second law of thermodynamics — and, a sharp byproduct, "**not all of
the commonly used divergence cleaning extensions … are thermodynamically
consistent**." An entropy-stable finite-volume/high-order discretization
is derived in implementable detail and deployed in the AMR code FLASH,
compared against FLASH's unsplit staggered CT solver.

# Key claims

1. **Powell terms rehabilitated by physics**: the non-conservative terms
   are not a numerical trick but what the Lorentz force requires when
   divergence errors exist — without them, discrete solutions "may
   describe the wrong physics" wherever the constraint is not pointwise
   exact. (This sharpens, from thermodynamics, the trade recorded at
   [eight-wave](/methods/eight-wave.md).)
2. **Entropy as the referee among GLM variants**: the cleaning coupling
   must be built so the combined system has an entropy pair — some
   standard GLM extensions fail this and can inject entropy-inconsistent
   dynamics; the ideal GLM-MHD construction passes by design
   ([GLM cleaning](/methods/glm-divergence-cleaning.md)).
3. **Nine waves, Galilean invariant**: eight MHD waves plus the cleaning
   wave in one hyperbolic, symmetrizable system with entropy-stable
   numerical fluxes — the constraint-control and nonlinear-stability
   agendas merged rather than layered.

# Notation map

| Derigs et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| ideal GLM-MHD, $\psi$ | GLM system with $\psi_h$ | nine-wave |
| non-conservative Powell terms | eight-wave source terms | thermodynamically derived |
| entropy pair, ES fluxes | — | nonlinear stability layer |

# Pages created or updated

* Updated [GLM divergence cleaning](/methods/glm-divergence-cleaning.md) (entropy-consistent nine-wave form; inconsistency of some variants).
* Updated [Eight-wave formulation](/methods/eight-wave.md) (thermodynamic rederivation of the source terms).

# Citations

1. `~/papers/mosaic/div-free-amr/2018-JCP-Derigs-101016jjcp201803002.pdf` (doi:10.1016/j.jcp.2018.03.002) — text extraction, 48 pp.
