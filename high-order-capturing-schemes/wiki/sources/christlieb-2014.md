---
type: Source
title: "Christlieb, Rossmanith & Tang (2014) — Finite difference weighted essentially non-oscillatory schemes with constrained transport for ideal magnetohydrodynamics"
description: "The original unstaggered constrained-transport FD-WENO scheme for 2D and 3D ideal MHD: Jiang–Wu FD-WENO for the MHD state, Hamilton–Jacobi WENO for the Weyl-gauge vector potential with a gated artificial resistivity in 3D, a fourth-order central curl in every stage of a 10-stage SSP-RK4 at CFL 3, and exact total-energy conservation; fourth order on Alfvén waves and Orszag–Tang stable to t = 30."
resource: "doi:10.1016/j.jcp.2014.03.001"
source_kind: paper
authors: [Christlieb A.J., Rossmanith J.A., Tang Q.]
year: 2014
venue: "J. Comput. Phys. 268:302-325"
local_file: "~/papers/mosaic/high-order-capturing-schemes/2014-JCP-Christlieb-101016jjcp201403001.pdf"
tags: [mhd, constrained-transport, weno, finite-difference, divergence-free]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

The predecessor of [Christlieb et al. (2016)](/sources/christlieb-2016.md),
following the Helzel–Rossmanith–Taetz framework. Merged into the
[constrained transport](/methods/constrained-transport.md) page (now its
primary source for the unstaggered design), the SSP, characteristic and
conservative-FD pages, and the Alfvén-wave, oblique shock-tube,
Orszag–Tang, shock–cloud and Brio–Wu benchmarks.

# Key claims

1. **Divergence approaches** (§1): eight-wave, projection, cleaning, CT;
   Tóth showed staggering is unnecessary, and unstaggered CT eases AMR.
2. **Potential equation** (§2.2, eqs. 2.15–2.26): Weyl gauge; weakly
   hyperbolic in 3D, which Helzel et al. call an artifact of freezing the
   velocity; a scalar strongly hyperbolic equation in 2D.
3. **CT step** (§3, eqs. 3.3–3.7): in every Runge–Kutta stage, overwrite
   the predicted field with the curl of the potential. Only the
   energy-conserving option is used; positivity limiters are left for later.
4. **Time** (§3, Algorithm 1): Ketcheson's SSP-RK(10,4), essentially
   non-oscillatory with WENO5 up to CFL 3.07, run at 3.0; non-SSP RK4 needs
   0.8.
5. **Base scheme** (§4): Jiang–Wu FD-WENO with arithmetic means of
   primitives, Barth's eigenvector scaling, and global Lax–Friedrichs per
   field; local splitting gave "no significant differences".
6. **Hamilton–Jacobi WENO** (§5): WENO on differences of the potential,
   which controls oscillations in the field (§5.1, Fig. 1); in 3D a gated
   resistivity of size $O(h^6)$ in smooth regions, $\nu \in [0.02, 0.2]$,
   0.1 in the runs (eqs. 5.19–5.24).
7. **Curl and order** (§6): fourth-order central differences whose
   divergence vanishes exactly; overall fourth order; Claim 6.1 (global
   conservation of the field), proof omitted.
8. **Tests** (§7): smooth Alfvén waves (fourth order, 2D and 3D); rotated
   shock tube with Helzel–Rossmanith states; Orszag–Tang to $t = 30$ (the
   base scheme fails at about $t = 4.0$); 2D, 2.5D and 3D shock–cloud.

# Notation map

| Christlieb et al. (2014) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $q$, $\mathbf u$ | $u$, $\mathbf v$ | the paper's $\mathbf u$ is velocity |
| $\mathcal E$ (energy) | $E$ | registry $\boldsymbol{\mathcal E}$ is the electric field |
| $\mathbf A$, $\psi$ | $\mathbf A$, $\psi$ | |
| $\mathcal H(Q_A, u)$ | (words) | registry $\mathcal H$ is the Shu–Osher flux function |
| $\varepsilon^1$, $\nu$, $\gamma^1$ (resistivity) | (words), $\nu$ on concept pages as "resistivity coefficient" | collide with $\varepsilon$, $\nu$, $\gamma$ |
| $D^x$ | fourth-order central difference | |
| $g^\pm_j$, $\alpha^{(m)}$ | $f^\pm$, $\alpha$ | |

# Pages created or updated

* Updated [Brio–Wu MHD shock tube](/benchmarks/brio-wu-shock-tube.md).
* Created [Circularly polarized (torsional) Alfvén waves](/benchmarks/circularly-polarized-alfven-wave.md).
* Updated [Conservative finite-difference (flux) formulation](/methods/conservative-finite-difference.md).
* Updated [Constrained transport for high-order capturing schemes (MHD)](/methods/constrained-transport.md).
* Created [Grid-oblique MHD shock tubes](/benchmarks/oblique-mhd-shock-tubes.md).
* Updated [Local characteristic decomposition](/methods/characteristic-decomposition.md).
* Updated [Orszag–Tang vortex (2D MHD)](/benchmarks/orszag-tang-vortex.md).
* Updated [Shock–cloud interaction (MHD and relativistic MHD)](/benchmarks/shock-cloud-interaction.md).
* Updated [TVD / strong-stability-preserving Runge–Kutta methods](/methods/ssp-runge-kutta.md).
* Updated [Notation registry](/notation.md): batch-6 registry extensions.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2014-JCP-Christlieb-101016jjcp201403001.pdf` (arXiv:1309.3344v2, 4 March 2014, an author preprint, most likely the revised manuscript, not the version of record; published as J. Comput. Phys. 268:302–325 (July 2014), doi:10.1016/j.jcp.2014.03.001, checked on Crossref): text extraction, all sections; pp. 6, 9, 11, 16, 18, 19 and 36 read from the page images. Preprint typos: eq. 4.7 lacks the minus sign, eq. 2.23 has $n^2$ for $n^3$. The CFL-number definition is not stated. Reference list: 47 entries.
