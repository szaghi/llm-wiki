---
type: Source
title: "Friedrich, Winters, Del Rey Fernández, Gassner, Parsani & Carpenter (2018) — An entropy stable h/p non-conforming discontinuous Galerkin method with the summation-by-parts property"
description: "Proves the standard mortar coupling loses entropy stability for nonlinear systems at h/p nonconforming interfaces, and modifies it to restore provable stability at unchanged parallel cost."
resource: "doi:10.1007/s10915-018-0733-7"
source_kind: paper
authors: [Friedrich L., Winters A.R., Del Rey Fernández D.C., Gassner G.J., Parsani M., Carpenter M.H.]
year: 2018
venue: "J. Sci. Comput. 77:689-725 (arXiv:1712.10234)"
local_file: "/home/stefano/papers/mosaic/div-free-amr/2018-JSC-Friedrich-101007s10915-018-0733-7.pdf"
tags: [dg, sbp, entropy, nonconforming, coarse-fine-interface, stability]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

Entropy-stable DG spectral elements on **h/p nonconforming rectangular
meshes** (hanging nodes and/or per-element polynomial order): collocation
at Legendre–Gauss–Lobatto nodes makes the DG derivative/mass pair an
[SBP](/definitions/summation-by-parts.md) operator, so continuous entropy
analysis transfers discretely. The paper's pivotal finding is negative:
**"the standard mortar approach … does not guarantee entropy stability for
non-linear problems, which can lead to instabilities."** The remedy is a
precisely specified modification of the mortar coupling that restores
provable entropy conservation/stability at h/p interfaces, with parallel
scaling unaffected; high-order accuracy and entropy behavior verified
numerically.

# Key claims

1. **Linear-safe is not nonlinear-safe**: the mortar projection —
   accuracy- and energy-adequate for linear problems — fails the *entropy*
   (nonlinear) stability test at nonconforming interfaces; interface
   machinery certified for $L_2$ energy does not automatically extend to
   nonlinear invariants.
2. **The fix is in the coupling, not the elements**: conforming
   entropy-stable DGSEM and nonconforming mortars are individually mature;
   the contribution is the marriage — modified interface fluxes such that
   the entropy estimate telescopes across hanging nodes.
3. **SBP as the transfer vehicle**: the LGL derivative/mass structure is
   what allows discrete mimicry of the continuous entropy proofs — the
   generalized-SBP umbrella
   ([Del Rey Fernández et al. (2014)](/sources/delreyfernandez-2014.md))
   again carrying an interface result.

# Notation map

| Friedrich et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| mortar projections at h/p interfaces | interface transfer machinery (cf. $I_{C2F}, I_{F2C}$) | DG-side counterpart |
| LGL-collocated DGSEM | generalized SBP member | derivative/mass = SBP pair |
| entropy pair, two-point fluxes | nonlinear stability layer | |

# Pages created or updated

* Updated [SBP-preserving interpolation](/operators/sbp-preserving-interpolation.md) (nonlinear caveat: energy-stable coupling need not be entropy-stable; mortar modification).

# Citations

1. `~/papers/mosaic/div-free-amr/2018-JSC-Friedrich-101007s10915-018-0733-7.pdf` (doi:10.1007/s10915-018-0733-7) — text extraction, 37 pp.
