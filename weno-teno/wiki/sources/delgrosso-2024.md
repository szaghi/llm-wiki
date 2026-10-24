---
type: Source
title: "Del Grosso et al. (2024) — A well-balanced, positive, entropy-stable, and multi-dimensional-aware finite volume scheme for 2D shallow-water equations with unstructured grids"
description: "Cell-centred finite-volume scheme for 2D shallow water on polygonal grids whose subface fluxes come from a Lagrangian simple Riemann solver closed by a nodal velocity solver: node-wise conservative, positive, entropy-stable and lake-at-rest preserving, with a second-order extension and no carbuncle where the two-point version shows it."
resource: "doi:10.1016/j.jcp.2024.112829"
source_kind: paper
authors: [Del Grosso A., Castro M.J., Chan A., Gallice G., Loubère R., Maire P.-H.]
year: 2024
venue: "J. Comput. Phys. 503:112829"
local_file: "/home/stefano/papers/mosaic/weno-teno/2024_Crossref_Journal_of_Computational_Physics_Del_A_well-balanced_positive_entropy-stable_and_multi-dimensiona.pdf"
tags: [shallow-water, well-balanced, entropy-stable, positivity, unstructured-mesh, carbuncle]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

The paper builds a first-order cell-centred finite-volume scheme for the 2D
[shallow-water equations](/definitions/shallow-water-equations.md) with bottom
topography on general polygonal grids (quadrangles and triangles), and a
second-order extension with limited least-squares slopes and a two-stage
Runge–Kutta step. The core is a "simple" approximate Riemann solver (three
waves, four states) derived in Lagrangian mass coordinates normal to each
subface, after Gallice's theory for balance laws, and mapped back to Eulerian
coordinates. [Well-balancing](/properties/well-balancing.md) is built into the
solver: the interface source term $g\,\tfrac{h_l+h_r}{2}(b_r-b_l)$ makes the
intermediate normal velocity vanish for a lake-at-rest pair of states.

The multidimensional ingredient is a nodal solver taken from cell-centred
Lagrangian hydrodynamics: the intermediate normal velocity of every subface
meeting at a node is the projection of one nodal velocity, fixed by a
node-based consistency condition, a $2\times2$ linear system per node. Each
subface flux then depends on all cells around the node, and conservation
holds node-wise rather than by flux cancellation across each face. When the
nodal projection equals the face Godunov velocity, a classical face-based
"two-point" scheme ([HLLC-like](/methods/hll-riemann-solvers.md)) is recovered.
The first-order multi-point scheme is shown to be
[positive](/properties/bound-preservation.md) under an explicit time-step
condition, [entropy-stable](/properties/entropy-stability.md) (total energy
non-increasing) under wave-speed lower bounds, and exactly lake-at-rest
preserving.

Tests: first and second order on a smooth subsonic flow; round-off
preservation of a lake at rest over three mounds and the decay of a small
perturbation (the 2D analogue of the [flow over a bump](/benchmarks/flow-over-a-bump.md));
symmetric radial [dam breaks](/benchmarks/dam-break-problem.md) on flat and
curved bottoms; an oblique hydraulic jump; a four-quadrant Riemann problem over
discontinuous topography. On colliding flow, a Quirk-type odd–even decoupling
test and supercritical flow past a cylinder, the two-point scheme develops the
[carbuncle](/definitions/carbuncle-phenomenon.md) and the multi-point scheme
does not; the two-point scheme is slightly less diffusive.

# Version read

HAL preprint hal-04177987v1 ("Preprint submitted on 7 Aug 2023"; footer
"Preprint submitted to Journal of Computational Physics, July 13, 2023"), not
the version of record: 42 PDF pages (HAL cover plus 41 numbered pages, text
pp. 1–38, references pp. 38–41), all read. Title and authors match Crossref;
the preprint prints no DOI, which comes from Crossref. Equation, section and
page numbers cited here are those of the preprint.

# Key claims

Registry notation (see the notation map): the source's bottom $B$ is $b$, its
free-surface level $\eta$ is $H_{\mathrm s}$, its velocity $\mathbf u=(u,v)$ is
$v=(v_1,v_2)$, its normal velocity $u_n$ is $v_n$.

1. The Eulerian simple Riemann solver derived from its Lagrangian counterpart has ordered wave speeds $\Lambda_l\le\Lambda_0\le\Lambda_r$ whenever the Lagrangian solver keeps positive intermediate specific volumes (§3.6). **Derived**
2. The interface source term $\overline{gh\Delta b}_{lr,f}=g\,\tfrac{h_{rf}+h_{lf}}{2}(b_{rf}-b_{lf})$ (Eq. (34)) makes the Lagrangian solver well-balanced: lake-at-rest states give a zero Godunov normal velocity, hence a zero nodal velocity and unchanged intermediate states (§3.5.1). **Derived**
3. The nodal system $\mathsf M_p\mathbf v_p=\mathbf w_p$ (Eq. (33)) "always admits a unique solution" (§3.4). **Stated** (no proof here; $\mathsf M_p$ is a positive combination of $\mathbf n\otimes\mathbf n$)
4. Positivity of the specific volumes requires lower bounds on the Lagrangian wave speeds, $\lambda_l\ge-(v^\star_n-v_{n,l})/\tau_l$ and $\lambda_r\ge(v^\star_n-v_{n,r})/\tau_r$ (Eq. (35)), combined into Eq. (36); they are implicit in $v^\star_n$ and are checked a posteriori by iteration (§3.5.2, Remark 1). **Derived**
5. The node-based entropy condition (Eq. (37)) holds if the face-wise conditions (38)–(39) hold, which "some algebraic computations" show are met for $\lambda_{lf}\ge\sqrt{gh^\star_{lf}}\,h_{lf}$ and $\lambda_{rf}\ge\sqrt{gh^\star_{rf}}\,h_{rf}$ (Eqs. (42)–(43)); the nodal solver makes the residual vanish (Eq. (41)) (§3.5.3). **Derived** (the algebra for (42)–(43) is not shown)
6. The two-point scheme needs the same wave-speed conditions for positivity and entropy stability (Remark 2). **Stated**
7. The first-order multi-point scheme keeps $h>0$ under $\Delta t\le\min_c\lvert\omega_c\rvert/\sum_p\sum_fl_{pcf}\xi^{\min}_{pcf}$ (Eqs. (50)–(51)), enforced in practice with $\max(\lvert\Lambda_{pcf,L}\rvert,\lvert\Lambda_{pcf,R}\rvert)$ (Eq. (52)) (§4.2). **Derived** (convex-combination argument)
8. Without source term the scheme is conservative; the sufficient node-wise condition (53)/(54) reduces to the node-based consistency (12), which the nodal solver satisfies; conservation is "retrieved around each node", not by face-flux cancellation (§4.3). **Derived** (details referred to Gallice et al. 2022)
9. The scheme satisfies a cell entropy inequality (Eq. (57)) with the subface entropy flux of Eq. (56), and the total entropy is non-increasing up to the source contribution (Eq. (58)) under (42)–(43) and the time-step condition (§4.4). **Derived**
10. The multi-point scheme preserves the lake at rest exactly without further modification (§4.5), through the geometric identity $\sum_p\sum_fl_{pcf}\mathbf n_{pcf}=0$ (Eq. (48)). **Derived**
11. The multi-point subface flux is the two-point averaged flux minus $\tfrac{\lambda_c+\lambda_d}{2}\big(\mathbf v_p\cdot\mathbf n_{pcf}-v^{\mathrm{God}}_{\mathbf n_{pcf}}\big)$ in the normal-momentum component, plus half the interface source (Eq. (47)); the face-based scheme is recovered when $\mathbf v_p\cdot\mathbf n_{pcf}=v^{\mathrm{God}}_{\mathbf n_{pcf}}$, e.g. at a lake at rest (§4.1). **Derived**
12. The second-order extension (limited piecewise-linear reconstruction of $h$, $hv_1$, $hv_2$, $h+b$; two-stage Runge–Kutta) keeps well-balancing, positivity and entropy stability; positivity of the reconstructed depth comes from the minmod or Venkatakrishnan limiter, and well-balancing needs an extra in-cell term (Eq. (60)) (§4.6). **Stated** (no proof for second order)
13. Subsonic smooth test on triangles ($984$ to $62976$ cells, reference $1007616$ cells): first-order $L^1$ orders for $h$ reach 0.92; second-order (no limiter) $L^1$ orders reach 1.97 ($h$), 2.02 ($v_1$), 1.79 ($v_2$) (Tables 1–2). **Shown**
14. The lake at rest over three mounds ($100\times100$ squares, $t=200$ s) is preserved "up to a machine error of order $10^{-15}$" by the first-order multi-point, second-order and two-point schemes (§5.2, Fig. 5). **Shown**
15. A $10^{-3}$ free-surface perturbation of that state leaves the domain; the run stops when residuals fall below $10^{-10}$, at $t\approx55.45$ s (§5.2.1, Fig. 6). **Shown**
16. Radial dam breaks (flat and cosine-bump bottom): the two-point scheme is "slightly less diffusive" than the multi-point one, as already observed for Euler, and second order is much less diffusive than first (§5.3, Figs. 7–10). **Shown**
17. Oblique hydraulic jump: both schemes capture the exact solution ($h=1.5$ m, $v_1=7.9556$ m/s, jump angle 30°); the two-point scheme is slightly less dissipative and second order is sharper (§5.4, Fig. 11). **Shown**
18. Colliding flow ($g=1$, $v_1=\pm30$, $50\times50$ quadrangles, random perturbation of amplitude $10^{-5}$): the two-point scheme produces the carbuncle, the multi-point scheme stays symmetric (§5.6, Fig. 14). **Shown**
19. Odd–even decoupling (Quirk-type moving shock in an $800\times20$ m canal with a bump): the first-order two-point scheme is unstable at $t=20$ s and $30$ s; the first- and second-order multi-point schemes are not (§5.7, Figs. 15–16). **Shown**
20. Flow past a cylinder (Froude 5 inflow, 81272 triangles): carbuncle in the two-point solution, none with the first- or second-order multi-point scheme (§5.8, Fig. 17). **Shown**
21. The carbuncle instability occurs in shallow water, not only in gas dynamics (§1, §§5.6–5.8). **Shown**
22. After Fleischmann et al., the carbuncle has a multidimensional nature, so dimension-by-dimension schemes built on 1D solvers are prone to it and a multi-dimensional-aware scheme "should be insensitive" (§1). **Stated** (a hypothesis attributed to Fleischmann et al.; the paper's carbuncle tests compare only its own two-point and multi-point schemes)
23. Only wet states ($h>0$) are treated; wet–dry fronts are left to future work (§2, §6). **Stated**

# Printed slips

- p. 21, below Eq. (46): "$u^{God}_{\mathbf n_{pcf}}=u^{God,ws}_{\mathbf n_{pcf}}-\overline{gh\Delta B}_{lr,pf}$".
  From Eq. (30) the source term enters divided by $\lambda_l+\lambda_r$,
  $v^{\mathrm{God}}=v^{\mathrm{God,ws}}-\overline{gh\Delta b}_{lr}/(\lambda_l+\lambda_r)$,
  and only this form makes the $+\tfrac12\overline{gh\Delta b}$ term of the third
  line of Eq. (47) follow from the second. *(compiler check, not in the
  sources.)*
- p. 4: the three eigenvalues are all labelled $\lambda^-$:
  "$\lambda^-=\mathbf{ue}-a$, $\lambda^-=\mathbf{ue}$, $\lambda^-=\mathbf{ue}+a$".
- p. 10, Eq. (11): the source-term arguments read "$\mathbf U_{lf},\mathbf U_{Lrf}$"
  (stray "L"); the third listed property of $\mathbf W_{pf,E}$ reads
  "$\mathbf W_{pf,E}(\mathbf U_{lf},\mathbf U_{rf},\dots)=\mathbf U$", incomplete.
- p. 13: the Lagrangian solver fluxes print "$\lambda^{(\mp)}_k(\mathbf V_{k+1}-\mathbf U_k)$",
  mixing $\mathbf V$ and $\mathbf U$.
- Eqs. (45)–(46): the sum runs to $m$, while the number of waves is $J$
  elsewhere.
- §5.4: the profile is taken "along the line y = 40m" in a domain printed as
  $[0,40]\times[0,30]$ m; the abscissa of Fig. 11b–c runs over 0–30 m and the
  vertical axis of Fig. 11a over −20 to 20, so domain, line and axes disagree.
- The colliding-flow test is attributed to "[30]" in §5.6 and to "[31]" in the
  test list of §5.
- p. 33: the perturbation "$\delta(2z-1)$, where z is a random number with
  $z\in[-1,1]$". *(Compiler check, not in the sources: with $z\in[-1,1]$ the
  perturbation ranges over $[-3\delta,\delta]$; $z\in[0,1]$ would give
  $[-\delta,\delta]$.)*
- §5.7: inlet "$u_{in}=13.283$ m²/s", the units of a discharge $hv$, labelled as
  a velocity.
- §4.4, after Eq. (59): "$\mathbf v_p$" where elsewhere $\mathbf u_p$.
- §5.3: "The final solution is plotted at t = 0.69s when the second-order
  accurate schemes are employed", while first-order results are also shown at
  $t=0.69$ s.
- Refs. [4] and [5] are the same work (Bermúdez & Vázquez 1994, Comput. Fluids
  23:1049–1071); ref. [30] prints "K. Friedemann" for F. Kemm.
- Typos: "Fig. 6 … 1t = 1s", "Ventakakrishnan" (§4.6), "encounters for genuine
  multidimensional effects" (abstract), "sensibility".

# Notation map

| Del Grosso et al. (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf U=(h,hu,hv)$, $\mathbb F$, $\mathbf F_1$, $\mathbf F_2$ | $u=(h,hv_1,hv_2)$, $f^{(1)}$, $f^{(2)}$ | conserved variables and fluxes; $\mathbf U_c$ cell averages $\bar u_c$ |
| $\mathbf S$ | $S(u)$ | topography source |
| $h$, $B$, $\eta=h+B$ | $h$, $b$, $H_{\mathrm s}$ | as on [shallow-water equations](/definitions/shallow-water-equations.md); **$B$ is the magnetic field and $\eta$ the entropy in the registry** |
| $\mathbf u=(u,v)$, $u_n$, $u_t$ | $v=(v_1,v_2)$, $v_n$, $v_t$ | velocity and its normal and tangential components |
| $p=\tfrac12gh^2$, $a=\sqrt{gh}$ | kept, $c$ | hydrostatic pressure, gravity-wave speed |
| $E=\varepsilon+\tfrac12\lVert\mathbf u\rVert^2$, $\Sigma=hE$, $\Theta$, $\Phi$ | kept, $\eta$, $F_\eta$, kept | specific total energy; entropy density, entropy flux and source; **$E$ is not the registry's total energy per volume** |
| $\tau=1/h$, $m$ | kept | specific volume and Lagrangian mass coordinate |
| $\mathbf V_n$, $\mathbf G_n$, $\mathbf P_n$ | kept | Lagrangian variables, flux, source |
| $\omega_c$, $\omega_{pc}$, $\omega_p$ | kept | cell, corner subcell, dual cell around node $p$; **$\omega$ collides with $\omega_k$** |
| $l_{pcf}$, $\mathbf n_{pcf}$, $\mathcal{SF}(p)$ | kept | subface length, outward normal, subfaces at node $p$ |
| $\widetilde{\mathbf F}_{pcf}$, $\widetilde{\mathbf F}^\mp_{pf}$ | kept | subface flux with source, left- and right-sided subface fluxes |
| $\mathbf W_{pf,E}$, $\mathbf W_{pf,L}$ | kept | Eulerian and Lagrangian approximate Riemann solvers |
| $\Lambda_l,\Lambda_0,\Lambda_r$ | kept | Eulerian wave speeds; outer ones play the role of $s^-$, $s^+$ |
| $\lambda_l$, $\lambda_r$ | kept | Lagrangian wave speeds (mass fluxes, $\approx a/\tau$); **not eigenvalues $\lambda_l$** |
| $u^\star_n$, $\tilde p_S$, $\tau^\star_S$ | $v^\star_n$, kept | intermediate normal velocity, pressures, specific volumes |
| $u^{God}_n$, $u^{God,ws}$ | $v^{\mathrm{God}}_n$, $v^{\mathrm{God,ws}}$ | Godunov acoustic velocity with and without source (Eq. (30)) |
| $\mathbf u_p$, $\mathsf M_p$, $\mathbf w_p$ | $\mathbf v_p$, $\mathsf M_p$, $\mathbf w_p$ | nodal velocity, nodal matrix and right-hand side; **$\mathbf w_p$ is not the entropy-variable vector** |
| $\overline{gh\Delta B}_{lr,f}$, $\overline{\mathcal M}$, $\mathcal M^C$ | $\overline{gh\Delta b}_{lr,f}$, kept | interface source term, its vector, second-order in-cell correction |
| $\overline{\mathbf F}^{AV}$ | kept | average of left- and right-sided fluxes (Eq. (45)) |
| $\mathcal D_E=\{h>0\}$ | $G$ | admissible set (wet states) |
| $\mathbf e_1$, $\mathbf e_2$ | kept | unit vectors of state space |

# Reference list

66 printed references, numbered style ([1]–[66]) with "(Cited page …)"
back-references, all parsed and merged complete into the
[bibliography](/bibliography.md) with `citedby` `delgrosso-2024`. Refs. [4] and
[5] are a printed duplicate of the same Bermúdez & Vázquez (1994) paper. Ref.
[30] prints the given name "Friedemann" as surname for Kemm's carbuncle paper
(Appl. Math. Comput. 320:596–613); refs. [28] and [31] print "P. Garcia-Navarro F. Alcrudo" and
"F. Kemm G. Bader" and are keyed by the first printed name. Refs. [11], [36], [42], [43] and [52] carry
no pages or article number; ref. [49] (Maire 2011) and ref. [33] (Gallice 2002,
a habilitation) print no venue or institution. No unparseable items.

# Pages created or updated

Chunk 8 (2026-10-23), cited further in chunks 9–10 (2026-10-23). This source is cited on:

* [Bound preservation](/properties/bound-preservation.md)
* [Carbuncle phenomenon](/definitions/carbuncle-phenomenon.md)
* [Dam-break problems](/benchmarks/dam-break-problem.md)
* [Entropy stability](/properties/entropy-stability.md)
* [Flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
* [Shallow-water equations](/definitions/shallow-water-equations.md)
* [Shallow-water flow over a bump and lake at rest](/benchmarks/flow-over-a-bump.md)
* [Well-balancing](/properties/well-balancing.md)
