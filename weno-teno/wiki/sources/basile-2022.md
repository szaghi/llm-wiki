---
type: Source
title: "Basile et al. (2022) — Unstructured h- and hp-adaptive strategies for discontinuous Galerkin methods based on a posteriori error estimation for compressible flows"
description: "Isotropic metric-based h- and hp-adaptation for modal DG on unstructured and hybrid meshes: a combined modal-energy and interface-jump error estimator, a modal-decay smoothness indicator for the h/p choice, a size law with degree-dependent rates and a dof-growth-controlled target error, tested on steady laminar and RANS subsonic flows."
resource: "doi:10.1016/j.compfluid.2021.105245"
source_kind: paper
authors: [Basile F., Chapelier J.-B., de la Llave Plata M., Laraufie R., Frey P.]
year: 2022
venue: "Comput. Fluids 233:105245"
local_file: "/home/stefano/papers/mosaic/weno-teno/2022_Crossref_Computers_amp_Fluids_Basile_Unstructured_h-_and_hp-adaptive_strategies_for_discontinuous.pdf"
tags: [dg, amr]
timestamp: 2026-10-22T12:00:00Z
---

# Summary

The paper builds an isotropic, metric-based
[h- and hp-adaptation](/methods/hp-adaptation.md) loop for a modal
[discontinuous Galerkin](/methods/discontinuous-galerkin.md) discretization of
steady compressible laminar Navier–Stokes and RANS (Spalart–Allmaras) flows on
unstructured simplicial and hybrid prism–tetrahedron meshes. It is implemented in
the Airbus–ONERA–DLR solver CODA, and the open-source remesher MMG builds each new
mesh from a nodal size map. The DG scheme is background, not a contribution of the paper: an orthonormal
hierarchical modal basis, a Roe flux with a Harten-type entropy fix, BR1 viscous
terms, and backward Euler with matrix-free GMRES.

Three ingredients drive the loop. (i) An element error estimator $\mathsf E_K$
sums two min–max-normalized indicators of the momentum magnitude: the "small scale
energy density", the volume-normalized $L^2$ energy of the highest-degree modes,
and a face-averaged interface-jump indicator. The estimators keep their physical
dimension and are applied to every degree, including $N=1$. (ii) A smoothness
indicator after Mavriplis: the decay rate $\varrho$ of a least-squares
fit $\hat a^{(\ell)}\simeq Ce^{-\varrho\ell}$ of the per-degree norms of
the modal coefficients. $\varrho>1$ selects p-enrichment, otherwise
h-refinement, and $N=1$ elements always count as smooth. This is a modal-decay
measure of the same family as the modal [troubled-cell indicators](/definitions/troubled-cell-indicator.md).
It grows with smoothness, the opposite sense of the WENO
[smoothness indicator](/definitions/smoothness-indicator.md) $\beta_k$. (iii) A
size law $h^*=h(\mathsf E^*/\mathsf E)^{1/\mathsf r}$ with $\mathsf r=N+1$
(smooth) or $1$ (non-smooth), a refinement cap of 2 per step, and a target error
$\mathsf E^*$ found by bisection so that the predicted number of degrees of
freedom grows by a fixed factor $\mathsf g$ per step.

The tests are a 2D NACA0012 at $M_\infty=0.5$, $\mathrm{Re}=5000$, a 3D sphere at
$\mathrm{Re}=200$, a 3D delta wing at $M=0.3$, $\mathrm{Re}=4000$, and a 3D RANS
subsonic jet from the PPRIME nozzle. The adapted series beat the finest uniform
meshes in about four steps, and hp converges fastest in the first steps. For the
jet, DG-hp with 7–15 M degrees of freedom agrees better with LES and experiment
than a 48 M-element second-order structured finite-volume RANS. No case has
shocks; the authors defer shock-dominated flows and state that they would need a
different indicator.

# Version read

Author manuscript in the Elsevier preprint template, footer "Preprint submitted to
Elsevier, September 21, 2021", not the Computers & Fluids version of record. It has
58 pages: text to p. 48, references on pp. 49–58. It was read from text
extraction; the figures are image-only, and their captions and legends were read.
Page 1 prints "hp- adaptive" with a space and a final period; title and authors
otherwise match Crossref. The manuscript prints no DOI. Equation, section and
figure numbers are those of this manuscript.

# Key claims

Registry notation: the source's polynomial degree $p$ becomes the DG degree $N$;
its error estimator $\epsilon_K$, decay rate $\sigma$, per-degree coefficient norm
$a^{(q)}$, imposed rate $m$ and growth factor $f_r$ become $\mathsf E_K$, $\varrho$,
$\hat a^{(\ell)}$, $\mathsf r$ and $\mathsf g$, as on the
[hp-adaptation](/methods/hp-adaptation.md) page (see the Notation map).

1. Combining a spectral-decay (high-mode) estimator with an interface-jump estimator is motivated by earlier findings: jump estimators are reliable for any $N$, while spectral-decay estimators are reliable only at high $N$ and vary strongly from cell to cell (§4.1, citing Colombo et al. and Bassi et al.). **Stated**
2. Dimensional estimators on the momentum magnitude, with energy dimensions $[\rho v^2]$, work better than estimators normalized by the total modal energy or the solution norm, especially in recirculation zones, where a small momentum biases the normalized ones (§4.1, following Naddei and the authors' earlier work). **Stated** (no comparative figure in this paper)
3. The combined estimator is applied to every degree, including $N=1$, where the modal part is "not always optimal" but the coupled estimator "still performs well" (§4.1). **Stated**; **Shown** only indirectly by the $N=1$ h-adaptive series
4. The h/p decision uses Mavriplis' 1D spectral-decay criterion with threshold $\varrho=1$, extended to multi-D by taking the $L^2$ norm of all modal coefficients of total degree $\ell$ (37). The degree-0 coefficient is excluded from the fit because the element mean "can severely bias the decay rate" (§4.2). **Stated**
5. The smoothness indicator therefore exists only for $N\ge2$; $N=1$ elements are "fictitiously marked as smooth" and always p-enriched (§4.2, §4.4). **Stated** (design choice)
6. The imposed local convergence rate is $\mathsf r=1$ near discontinuities and $\mathsf r=N+1$ in smooth regions, from the DG $L^2$ error rate $O(h^{N+1})$ ((38)–(39)). **Stated**
7. Classical fixed-fraction marking performs poorly with magnitude-dependent sizing, because the gap between maximum and mean error leads to localized refinement and an early stall. A target error controlled by the growth of the number of degrees of freedom and found by bisection, (49), is proposed instead (§4.5). **Stated** (no figure of the classical variant)
8. In hp mode, nodal averages of $\mathsf E_K$, $N_K$ and $\varrho$ use only the elements not marked for p-enrichment (Fig. 1). This prevents excessive h-refinement in p-refined zones and keeps the constant-$C$ assumption of (45) valid (§4.4). **Stated**
9. On hybrid meshes the boundary-layer prisms (and, for the nozzle, the internal tetrahedra) are frozen during remeshing but can still be p-enriched; in frozen regions an element is p-enriched whenever $\mathsf E_K>\mathsf E^*$, with no smoothness condition (§4.6, §6.1). **Stated**
10. NACA0012 ($\mathrm{Re}=5000$): for every h-adaptive series ($N=1,2,3$), four adaptation steps reach a lower drag error than the finest uniform mesh of the same degree. hp reaches a lower error than the finest uniform $N=3$ mesh in four steps, with fewer degrees of freedom than any h-adaptive series (§5.1, Figs. 3–4). **Shown**
11. NACA0012: for the $N=2$ and $N=3$ h-adaptive series and for hp, the final drag and lift errors are "around two orders of magnitude" below uniform refinement (§5.1). **Shown**
12. Reference values: $C_D=0.0556622$ (friction 0.0328013, pressure 0.0228610) and $C_L=0.0199830$ (Table 1), against Swanson et al.'s $C_D=0.055980$ and $C_L=0.0184635$. The $C_L$ gap is attributed to the revised NACA0012 definition used here rather than the exact formula (§5.1). **Shown**/**Stated**
13. Refinement-factor study, $\mathsf g\in\{1.2,1.3,1.4,1.5,1.6,1.75,2\}$: all values converge the integral errors; a smaller $\mathsf g$ needs fewer degrees of freedom but more steps and gives oscillating errors. $\mathsf g=1.5$ is the chosen trade-off (§5.1, Fig. 7). **Shown**
14. Sphere ($\mathrm{Re}=200$): reference $C_D=0.77815623$, against 0.7771 (Rueda et al.), 0.7567 (Fadlun et al.) and 0.7683 (Fornberg) (Table 2). $N=1$ h-adaptation needs about 10 times fewer degrees of freedom than uniform $N=1$; hp converges slightly faster than the $N=2$ and $N=3$ h-adaptive series in the first steps (§5.2, Fig. 9). **Shown**
15. Raising the degree progressively from $N=1$ during adaptation makes the implicit high-order solver more robust on stiff problems (§5.2, §6.2). **Stated** (no failure of the non-progressive alternative is shown)
16. No CPU-cost comparison of hp against high-order h-adaptation is given, because a fair one would need load balancing and optimized implicit schemes (§5.2). **Stated**
17. Delta wing ($\mathrm{Re}=4000$): reference $C_D=0.165617$, $C_L=0.34716$ (extrapolated from uniform $N=3$; Table 3), against Hartmann's 0.1658/0.347 and Ceze's 0.16578/0.34771. $N=1$ h-adaptation matches the finest uniform $N=1$ error with about 90 % ($C_D$) and 50 % ($C_L$) fewer degrees of freedom. hp is fastest at first and then coincides with the $N=2$ series; the $N=3$ series is slightly worse below an error of $10^{-3}$ (§5.3, Figs. 11–12). **Shown**
18. Delta wing, hp: the elements around the geometric singularity stay at $N=2$ for several steps, because the indicator marks the zone non-smooth, and switch to $N=3$ as it is resolved (§5.3, Figs. 13–14). **Shown**
19. PPRIME jet (RANS): from about 1.5 M degrees of freedom at $N=1$, five steps with $\mathsf g=1.5$ reach 10 M; the last three iterations (6.9, 10.1 and 14.4 M) "practically collapse", which shows mesh convergence (§6.2, Figs. 16–18). **Shown**
20. DG-hp RANS agrees better with LES and experiment than a 48 M-element second-order structured finite-volume RANS, with 15–20 % of its degrees of freedom (7, 10 and 15 M against 48 M). Both RANS runs underpredict the centreline velocity for $x/D\ge5$, the short potential core typical of RANS (§6.2, Figs. 17–18; §7). **Shown**
21. For the jet, a smaller $\mathsf g$ (1.5 against 2) concentrates elements in the potential-core cone and lowers the profile errors faster per degree of freedom, but needs more steps (§6.2, Figs. 19–20). **Shown**

# Printed slips

- Eq. (43): "$p^*_{K,i+1}=\max(p_{K,i}+1,p_{max})$" would send every p-marked element to $p_{max}$; the text ("increased by one", capped at $p_{max}$) and Algorithm 2 ("$p^*_{K,i+1}=p_{K,i}+1$") imply $\min$.
- Eq. (16) defines $d_q=\{l\mid\phi_l\in P^q_K\setminus P^{q-1}_K\}$ (degree exactly $q$), but pp. 10 and 19 describe it as the basis functions "of total degree at most q".
- Eq. (37) prints the range "$\forall q\in(1,p_K)$", an open interval; $q=1,\dots,p_K$ is meant.
- Eq. (22): "$[[u_u]]$" for $[[u_h]]$.
- §4.3: "where $h^*_{K,i}$ is the characteristic size of the element K", while (39) uses the unstarred $h_K$; the MMG input metric is printed $(h^*_{n,i})^{-2}I$ where $h^*_{n,i+1}$ is meant.
- The single global target error is written $\epsilon^*_{i+1}$ ((39)–(40), (49)), $\epsilon^*_{K,i+1}$ ((44), (46)) and $\epsilon^*_{n,i+1}$ (§4.5).
- After (49): "where $N_{i+1}$ is the number of dofs wanted", while the equation contains $N^*_{i+1}$ and $N_i$.
- Eq. (50) prints $\|u-u_{ref}\|_{L^2}/\|u_{ref}\|_{L^2}=\int_l(u_R-u_{ref})^2dx/\int_lu_{ref}^2dx$, a ratio of squared norms; $u_R$ is undefined.
- §5.2 and §5.3 put the coefficients on the right and their errors on the left, while the captions of Figs. 9, 11 and 12 say the opposite.
- §5.1 refers the remesher's gradation to "section 3.1"; it is defined in §3.2. §6.2 refers to the NACA0012 "figure 7 in section 5.2"; it is in §5.1. §3.2 writes the final mesh "$T_{K+1}$" for $T_{K,i+1}$.
- Degree-of-freedom counts: the text gives "6.9, 10.1 and 14.4 million dofs", the legends "RANS adapt 14.5M", and the conclusion "using only 7 million dofs".
- Table 1 against the text: the text calls the $C_L$ differences "small". *(Compiler check, not in the sources)*: $0.0199830$ against $0.0184635$ is an 8.2 % difference.
- Refs. [58], [75], [85], [87] carry a BibTeX residue "note = Accessed: 2010-09-30".
- Typos: "adaptative", "developped", "readlily", "hauds", "aifoil", "reasearch", "adatation", "entrainement", "lenghts".

# Notation map

| Basile et al. 2022 | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $p$, $p_K$, $p_{min}$, $p_{max}$ | $N$, $N_K$, $N_{\min}$, $N_{\max}$ | DG degree; **collision** with the pressure $p$ |
| $N_p$ | $N_p(N)$ (local) | modal degrees of freedom per element |
| $u=(\rho,\rho v^T,\rho E)^T$ | $u=(\rho,\rho v,E)$ | $\rho\tilde\nu$ appended for RANS |
| $F_c$, $F_v$ | $f$, $f_v$ (local) | convective and viscous fluxes |
| $h_c(u^+,u^-,n)$ | $h$ | Roe flux with Harten-type entropy fix |
| $\{\{u\}\}$, $[[u]]=u^+\otimes n-u^-\otimes n$ | $\{\!\{u\}\!\}$, normal jump (local) | the source's jump carries the normal and its own sign convention |
| $\phi^l_K$, $u^l_K$, $d_q$ | same (local) | orthonormal modal basis, coefficients, index set of degree $q$ |
| $u_{h,p}$, $u_{h,p-1}$ | $u_h$, its truncation to $\mathbb P^{N-1}$ | |
| $\epsilon_{SSED,K}$, $\epsilon_{JUMP,K}$, $\epsilon_K$, $\epsilon^*$ | $\mathsf E_{\mathrm{SSED},K}$, $\mathsf E_{\mathrm{JUMP},K}$, $\mathsf E_K$, $\mathsf E^*$ (local) | error estimators and target error; never the WENO $\epsilon$ |
| $a^{(q)}$ | $\hat a^{(\ell)}$ (local) | per-degree norm of the modal coefficients; **collision** with $a$ and $q$ |
| $\sigma$, $\sigma_K$, $\sigma_n$ | $\varrho$, $\varrho_K$ (local) | modal decay rate, larger is smoother; **collision** with the affine $\sigma$, the SA constant and the BR1 gradient $\sigma=\nabla u$; not $\beta_k$ |
| $m$, $m_K$, $m_n$ | $\mathsf r$, $\mathsf r_K$ (local) | imposed convergence rate, $N+1$ or 1; **collision** with the number of equations $m$ |
| $k$ | Sobolev index (local) | |
| $h_K$, $h_n$, $h^*$ | same (local) | element, nodal and prescribed sizes; **collision** with the two-point flux $h$ |
| $\mathcal M$, $\Lambda$, $R$, $\lambda_i$, $D$ | same (local) | metric tensor, its eigen-decomposition and density; **collision** with $R$, $\lambda_l$ and the differentiation matrix $D$ |
| $r_h$, $f_r$ | $r_h$, $\mathsf g$ (local) | per-step refinement cap (2) and growth factor of the degrees of freedom (1.5) |
| $T_{K,i}$; $T_{h,i}$, $T_{p,i}$, $T_{=,i}$ | same (local) | mesh at step $i$; h-marked, p-marked and unmarked sets |
| $M_\infty$, $Re$, $Pr$ | $M$, $\mathrm{Re}$, $\mathrm{Pr}$ | |

# Reference list

The paper prints 90 references, numbered [1]–[90]. The list is merged complete into
the [bibliography](/bibliography.md), with `citedby` including `basile-2022`. [5]
is a book whose title the citing style splits. [9], [40], [74], [81] and [90] lack
a full venue, and [90] ends with "et al.". [58], [75], [76], [85] and [87] are web
pages with printed URLs and access dates; the ones without an author are keyed by
their host name and the citing year. [53] (Harten and Hyman 1983) is the citation
for the entropy fix. Naddei 2019 has two works, [63] (J. Comput. Phys.) and [80]
(PhD thesis). No DOIs are printed. No printed duplicates were found and no item is
unparseable.

# Pages created or updated

Chunk 2 (2026-10-22), cited further in chunks 3–11 (2026-10-22/24). This source is cited on:

* [Bassi–Rebay viscous discretizations (BR1, BR2)](/methods/bassi-rebay-viscous-discretization.md)
* [Discontinuous Galerkin method](/methods/discontinuous-galerkin.md)
* [h- and hp-adaptation for DG](/methods/hp-adaptation.md)
* [Roe approximate Riemann solver](/methods/roe-riemann-solver.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
