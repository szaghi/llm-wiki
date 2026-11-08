---
type: Source
title: "Peskin (1972) — Flow patterns around heart valves: a numerical method"
description: "The founding immersed boundary paper: an elastic boundary moving with a viscous incompressible fluid is replaced by a force field on a rectangular mesh, linked to the Lagrangian boundary points by a semidiscrete delta function, with an implicit force computation that removes the instability of explicit forcing; applied to a two-dimensional mitral valve."
resource: "doi:10.1016/0021-9991(72)90065-4"
source_kind: paper
authors: [Peskin C.S.]
year: 1972
venue: "J. Comput. Phys. 10(2):252-271"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/1972_Crossref_Journal_of_Computational_Physics_Peskin_Flow_patterns_around_heart_valves_A_numerical_method.pdf"
tags: [immersed-boundary, fluid-structure-interaction, delta-function, stiffness, incompressible, biofluid]
timestamp: 2026-11-08T17:40:00Z
---

# Summary

Peskin introduces the [immersed boundary method](/definitions/immersed-boundary-method.md)
for boundaries that "move with the fluid and exert forces on the fluid", such
as heart-valve leaflets. The fluid is described on a periodic rectangular
mesh in Eulerian form, the boundary by Lagrangian points; the boundary is
replaced by a force field that is nonzero only within two mesh widths of it,
so the discrete fluid equations are identical at every mesh point
([classical immersed boundary method](/methods/classical-immersed-boundary-method.md)).
Boundary and fluid are linked in both directions by a semidiscrete analogue
of the delta function ([regularized delta function](/operators/regularized-delta-function.md);
[spreading and interpolation](/operators/spreading-and-interpolation.md)).
Explicit force computation is unstable; an implicit predictor of the
configuration with an under-relaxed fixed-point iteration makes the scheme
stable at the same time step. The method is applied to a two-dimensional
natural mitral valve.

# Version read

Version of record, J. Comput. Phys. 10, 252–271 (1972), 20 pages, all read
from the publisher's scan with a text layer. The text layer misreads the
author's name on page 1 ("PISKIN") and garbles several display equations,
notably the delta function (3.20) and the implicit predictor (4.4). The
delta function is read here as the tensor product of hats of half-width $2h$
with factor $1/16h^2$, which is what the chain condition (3.19) and the Fig. 1
caption ("the factor $1/16h^2$ has been omitted") require. The page-1 title,
volume and pages match Crossref.

# Key claims

1. The main achievement is that a Navier–Stokes solver on a rectangular domain "can now be applied" to moving immersed boundaries, by replacing the boundary with a force field computed from its configuration (Abstract, §I). **Stated**
2. The problem is closed by five equations for $\mathbf u$, $p$, $\mathbf f$, $\mathbf X$, $\mathbf F$: Navier–Stokes, incompressibility, $\partial_t\mathbf X=\mathbf u(\mathbf X)$, $\mathbf f=\int\mathbf F\,\delta(\mathbf x-\mathbf X)\,ds$ and an elastic law $\mathbf F=\mathcal M(\mathbf X)$; the boundary is massless with fluid on both sides (§II, eqs. 2.1–2.7). **Stated**
3. Only the two interaction equations involve the delta function, which "makes its appearance under an integral sign" in both directions (§II). **Derived**
4. Boundary points must not be snapped to mesh points: an $O(h)$ displacement changes the boundary force by $O(1)$ (§III). **Stated**
5. The semidiscrete delta must give unit discrete integrals, be continuous in the boundary position, and give equal weight to the four parity chains of the central-difference projection, so that the solution stays smooth (§III.B, conditions 1–3, eq. 3.19). **Stated**
6. The implicit position update (3.23) is a contraction if $u_{\max}\Delta t<h/4$ (3.25), which is taken as a necessary accuracy condition for the explicit update (3.21) (§III.B). **Derived**
7. Forces from a link table — cords, rods, links to fixed points, links with variable rest length for muscle — represent membranes, nearly rigid fixed structures and active walls (§III.C). **Stated**
8. Forces computed from the configuration at the start of the step, or from a forward-Euler predictor, are unstable unless $\Delta t$ is "exceedingly small"; the force field is $O(h^{-1})$ (§IV, Fig. 2). **Shown**
9. The implicit choice (4.4), a predictor that includes the displacement produced by the forces themselves, is stable at the same viscosity and time step (§IV, Fig. 5); the fixed point is solved by under-relaxation, with a convergence range of the relaxation factor that shrinks for highly stressed boundaries (§IV–V). **Shown**
10. The fluid solver's conditioning requires $hRe<2$ (3.7), so the physiological $Re\approx2000$ would need about $10^3$ points per direction; the computation uses a hundredfold viscosity, interpreted by similarity as a 0.3 cm valve in blood (§III.A, §V). **Derived**
11. On a $20\times20$ mesh with 2000 steps per heartbeat, one beat takes about 5000 s on a CDC 6600; 30 SOR sweeps per step are needed for the Poisson equation, suggesting fast direct solvers (§V). **Shown**
12. The simulated leaflets "catch" most of the backflow at closure; peak flow lags peak driving force, forward flow continues against an adverse force, and a damped post-closure oscillation appears — features observed in dog mitral valves (§V, Figs. 5–6). **Shown**
13. The method's main strength is "the absence of special conditions imposed along the immersed boundary"; it extends at once to three dimensions but may be too expensive there (§VI). **Stated**

# Notation map

| Peskin (1972) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $R$, $B$ | $\Omega$, $\Gamma$ | periodic rectangle; immersed boundary |
| $\mathbf x(s,t)$, $\mathbf x_k$ | $\mathbf X(s,t)$, $\mathbf X_\ell$ | boundary configuration, Lagrangian points |
| $\mathbf f(s,t)$ | $\mathbf F(s,t)$ | boundary force density (per unit $s$) |
| $\mathbf F(\mathbf x)$ | $\mathbf f(\mathbf x)$ | Eulerian force density |
| $M$ | $\mathcal M$, the elastic law $\mathbf F=\mathcal M(\mathbf X)$ | page-local |
| $P$ | $\mathcal P$ | projection onto divergence-free fields |
| $D_{ij}(\mathbf x_k)$ | $\delta_h(\mathbf x_{\mathbf i}-\mathbf X_\ell)$ | semidiscrete delta |
| $h_B$ | $h_\Gamma$ | Lagrangian spacing |
| $D$, $G$ | $D_0\cdot$, $D_0$ | central divergence and gradient |
| $S$, $R_0$, $R$, $T$ | $k_s$, $\ell_0$, $\ell$, $T$ | link stiffness, rest length, length, tension |
| $\gamma$ | under-relaxation factor, page-local | |
| $R$ (Reynolds number) | $Re$ | **collision** with the domain $R$ |
| $\mathbf x^*$, $\mathbf f^*$ | $\mathbf X^*$, $\mathbf F^*$ | predicted configuration and its force |

# Reference list

Nine printed references, merged complete into the
[bibliography](/bibliography.md) from the Crossref deposited list (ten
entries: the printed ref. 5 combines Buzbee, Golub and Nielson with Hockney).
Ref. 9 (Yellin et al., ASME paper 71-WA/BHF-2) is a conference paper.

# Pages created or updated

Chunk 1 (2026-11-08). This source is cited on:

- [Immersed boundary method](/definitions/immersed-boundary-method.md)
- [Sharp and diffuse interface representations](/definitions/sharp-and-diffuse-interface.md)
- [Regularized delta function](/operators/regularized-delta-function.md)
- [Spreading and interpolation operators](/operators/spreading-and-interpolation.md)
- [Classical (Peskin) immersed boundary method](/methods/classical-immersed-boundary-method.md)
