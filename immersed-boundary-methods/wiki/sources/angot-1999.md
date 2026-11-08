---
type: Source
title: "Angot, Bruneau & Fabrie (1999) — A penalization method to take into account obstacles in incompressible viscous flows"
description: "Convergence theorems and error estimates for volume penalization of obstacles in the incompressible Navier–Stokes equations: an L2 penalization (Darcy law in the body) and an H1 penalization (Brinkman law), with the body force recovered from the penalty term, verified on a square cylinder in a channel."
resource: "doi:10.1007/s002110050401"
source_kind: paper
authors: [Angot P., Bruneau C.-H., Fabrie P.]
year: 1999
venue: "Numer. Math. 81(4):497-520"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/1999_Crossref_Numerische_Mathematik_Angot_A_penalization_method_to_take_into_account_obstacles_in_inco.pdf"
tags: [penalization, fictitious-domain, convergence, error-estimate, incompressible]
timestamp: 2026-11-08T17:50:00Z
---

# Summary

Angot, Bruneau and Fabrie give the mathematical justification of
[volume penalization](/methods/volume-penalization.md): the Navier–Stokes
equations are solved in the whole domain with a penalty term
$\eta^{-1}\chi_s\mathbf u$ (an $L^2$ penalization, Darcy law in the body) or with
the whole linear part penalized (an $H^1$ penalization, Brinkman law). They
prove convergence to the no-slip solution as $\eta\to0$, with error
estimates, and show that the penalty term yields the body force
([convergence of volume penalization](/results/convergence-of-volume-penalization.md)).
A square cylinder in a channel confirms the analysis, with an observed error
better than the estimate.

# Version read

Version of record, Numer. Math. 81, 497–520 (1999), 24 pages, all read. The
text layer loses most fractional exponents of the estimates (they print as
"η 4", "η 2"); the exponents recorded here are those the authors state in
words in §6, "O(η^{3/4}) in Ω_s and O(η^{1/4}) in Ω_f", and the $H^1$ estimate
is recorded only as sharper. Page-1 title and authors match Crossref.

# Key claims

1. Peskin-type surface forcing (time integral plus velocity penalty at surface points) "has to be extended to the volume of the body to give correct physical solutions at high Reynolds numbers"; Arquis and Caltagirone (1984) penalized the volume of a porous body in a Brinkman model (§1). **Stated** (cited)
2. In the $L^2$ penalization the first-order correction obeys a Darcy law in the obstacles, which therefore behave as porous media (Remark 3.1). **Derived**
3. In the $H^1$ penalization it obeys a Brinkman equation with a stress-Neumann condition (Remark 3.2). **Derived**
4. Theorem 4.1: the penalized solutions converge, as $\eta\to0$, to a limit vanishing in $\Omega_s$ whose restriction to $\Omega_f$ is the unique weak Navier–Stokes solution (2-D). **Proved**
5. Lemma 4.4: the trace of $\mathbf u_\eta$ on each obstacle boundary is $O(\eta^{1/4})$ in $L^2(0,t;L^2(\Sigma^i))$. **Proved**
6. Theorem 4.2: error estimate $\mathbf u_\eta=\mathbf u+\eta^{1/4}\mathbf v_\eta$, i.e. $O(\eta^{1/4})$ in the fluid and $O(\eta^{3/4})$ in the body. **Proved**
7. Theorem 4.3: under a compatibility condition, the weak limit of $\eta^{-1}\chi_s\mathbf u_\eta$ is unique and gives the force on each obstacle, so drag and lift are volume integrals over the body. **Proved**
8. Theorem 5.1: for the $H^1$ penalization $\mathbf u_\eta=\mathbf u+\eta\tilde{\mathbf u}+$ higher order. **Proved**
9. Square cylinder in a channel ($320\times80$, $\Gamma$ on grid lines), $Re=40$: error $O(\eta)$ in the body and about $O(\eta)$ in the fluid until the discretization error dominates; the estimate of Theorem 4.2 "might not be optimal" (§6, Table 1). **Shown**
10. At $Re=80$ a large $\eta$ delays convection and underestimates the Strouhal number; at $\eta=10^{-8}$ penalized and Dirichlet solutions are indistinguishable; the pressure is continuous through the obstacle (§6, Table 2, Figs. 3–5). **Shown**
11. The $H^1$ penalization gives no practical improvement, because the discretized penalized viscous term changes the effective body volume (§6). **Shown**
12. Since $\eta$ can be taken as small as necessary, the penalty error is always negligible compared with the approximation error (§7). **Stated**

# Notation map

| Angot et al. (1999) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Omega_f$, $\Omega_s=\bigcup\Omega_s^i$, $\Sigma_s^i$ | $\Omega_f$, $\Omega_s$, $\Gamma$ | |
| $1_{\Omega_s}$ | $\chi_s$ | body mask |
| $\eta$ | $\eta$ | agree |
| $\sigma(\mathbf u,p)$ | $\boldsymbol\Sigma$ | stress tensor; registry reserves $\sigma$ for source strength |
| $\mathbf f$ | $\mathbf f_0$ | external force; $\mathbf f$ is the immersed-boundary force density in the registry |
| $\mathbf n_s^i$ (pointing into $\Omega_s^i$) | $-\mathbf n$ | registry normal points out of the body |

# Reference list

16 printed references, merged complete into the [bibliography](/bibliography.md)
from the printed list (Crossref deposits none). Refs. 3 and 10 are printed
as submitted, ref. 5 as to appear.

# Pages created or updated

Chunk 1 (2026-11-08). This source is cited on:

- [Flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
- [Immersed boundary method](/definitions/immersed-boundary-method.md)
- [Sharp and diffuse interface representations](/definitions/sharp-and-diffuse-interface.md)
- [Feedback forcing](/methods/feedback-forcing.md)
- [Volume penalization](/methods/volume-penalization.md)
- [Convergence of volume penalization](/results/convergence-of-volume-penalization.md)
