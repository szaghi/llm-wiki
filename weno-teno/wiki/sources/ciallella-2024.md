---
type: Source
title: "Ciallella et al. (2024) — Very high order treatment of embedded curved boundaries in compressible flows: ADER discontinuous Galerkin with a space-time Reconstruction for Off-site data"
description: "Transfers the Reconstruction for Off-site Data (ROD) boundary treatment to modal ADER-DG on triangles, in a space-only and a space-time variant whose constrained least-squares system has the identity as normal matrix, recovering high order on linear conformal and fully embedded meshes of curved domains."
resource: "doi:10.1016/j.camwa.2024.08.028"
source_kind: paper
authors: [Ciallella M., Clain S., Gaburro E., Ricchiuto M.]
year: 2024
venue: "Comput. Math. Appl. 175:1-18"
local_file: "/home/stefano/papers/mosaic/weno-teno/2024_Crossref_Computers_amp_Mathematics_with_Applications_Ciallella_Very_high_order_treatment_of_embedded_curved_boundaries_in_c.pdf"
tags: [dg, immersed-boundary, unstructured-mesh, very-high-order, space-time]
timestamp: 2026-10-23T23:45:00Z
---

# Summary

The paper treats boundary conditions on curved boundaries for the 2D Euler
equations, when the true boundary is approximated either by a conformal
straight-sided triangulation or by a fully embedded triangulation whose
surrogate boundary is detached from it (an
[embedded-boundary](/methods/immersed-boundary-method.md) setting). With naive
ghost-state conditions, [DG](/methods/discontinuous-galerkin.md) is at best
second order on the conformal linear mesh and first order in boundary
consistency on the embedded one, whatever the degree. The authors transfer the
Reconstruction for Off-site Data (ROD) of Costa, Clain et al. from finite
volumes to modal [ADER](/methods/ader-scheme.md)-DG on triangles. In ROD-DG,
for each boundary element and each sub-time node of the ADER corrector, a
monomial polynomial is fitted in weighted least squares to the predictor at
the element's own quadrature points. Linear Robin constraints
$\alpha_\Gamma\varphi+\beta_\Gamma\partial_n\varphi=g$ are imposed at the
projections of the boundary quadrature points onto the true boundary, and the
saddle-point system is solved with Lagrange multipliers. In ROD-ADER-DG, the
main contribution, the fit is written in the coefficients of the space-time
ADER predictor itself: the normal matrix becomes the identity, and one
constrained solve per space-time boundary element replaces one per sub-time
node.

Curved slip walls use the conditions of Chertock, Coco, Kurganov & Russo,
recast as the mixed set $v_n=0$, $\partial_nS=0$, $\partial_nH=0$,
$\partial_nv_t-\kappa_{\mathrm c}v_t=0$. These are linear in
$(v_n,S,H,v_t)$ and reached through a space-time $L^2$ projection, with the
true normal from a level set. Troubled boundary cells of the a posteriori
subcell finite-volume limiter use a Krivodonova–Berger-type corrected wall
flux. A [manufactured solution](/definitions/method-of-manufactured-solutions.md)
on a trefoil-like domain shows uncorrected DG at order 2 and both ROD variants
at high order with near-identical errors; the space-time variant is reported
about 10 % cheaper at $N=3$. The
[supersonic vortex between concentric arcs](/benchmarks/supersonic-vortex-between-arcs.md)
gives order about $N$ with curved slip walls, against less than 2 uncorrected.
A Mach 1.3 shock–cylinder interaction at $N=3$ shows smoother contours with
ROD on conformal and embedded meshes.

# Version read

arXiv 2312.07170v1 [math.NA], 12 Dec 2023, footer "Preprint submitted to
Elsevier, December 13, 2023": not the version of record (the published article
is 18 pages). It has 28 pages. Title and authors match page 1. Equation,
table and section numbers are those of arXiv v1.

# Key claims

Registry notation: $N$ is the DG degree (the source's $M$), $N_{\mathrm b}$
the number of spatial monomial coefficients (the source's $N$), $v_n$, $v_t$
the normal and tangential velocity, $\kappa_{\mathrm c}$ the boundary
curvature, $S=p\rho^{-\gamma}$ the source's entropy and $H$ the specific total
enthalpy (see the notation map).

1. On a linear conformal mesh of a curved boundary, the classical ghost-state DG boundary treatment is at best second-order accurate; on fully embedded meshes boundary consistency drops to first order without special treatment (§4, Fig. 1). **Stated** (conformal case **Shown**, Table 2)
2. The curvature-corrected wall conditions of Wang & Sun and Krivodonova & Berger recover third and sometimes fourth order in 2D but exist only for slip walls and only in 2D (§1). **Stated**
3. ROD replaces the polynomial of each boundary cell by a constrained least-squares reconstruction embedding the boundary condition; in its finite-volume form the stencil has $s\approx1.5N_{\mathrm b}$ neighbour cells found by a search algorithm (§1, Remark 3). **Stated**
4. In DG the reconstruction uses only the element's own high-order polynomial sampled at quadrature points, with no neighbour search (§5.1). **Derived**
5. Space-only ROD needs one constrained solve per boundary element at every sub-time node of the time integrator (ADER corrector nodes or Runge–Kutta stages) (§5.2, Fig. 3a). **Stated**
6. In the space-time modal basis of the ADER predictor the cost becomes $\hat{\mathcal J}(\eta)=\tfrac12[\eta-\hat q]^2$, so the normal matrix is the identity and one constrained system (Eq. 33) is solved per space-time boundary element (§5.2, Eqs. 30–33). **Derived**
7. System (33) is "slightly larger" than (29) but more diagonally dominant and solved only once; the total number of reconstructed modes is much lower than for several independent reconstructions, and the number of constraints needed for consistency is halved (Remark 4). **Stated** (no counts given; see Printed slips)
8. At $N=2$ the space-only ROD inverts a local $9\times9$ matrix each time, at $N=3$ a $14\times14$ one (§7). **Stated**
9. The slip-wall conditions on the true boundary are $v_n=0$ (16), $\partial_np=-\rho v_t^2\kappa_{\mathrm c}$ (18), $\partial_n\rho=c^{-2}\partial_np$ for an adiabatic wall (19) and $\partial_nv_t=\kappa_{\mathrm c}v_t$ for irrotational flow (20), after Chertock et al. (§4.2). **Derived**
10. The same conditions can be imposed as the mixed system $v_n=0$, $\partial_nS=0$, $\partial_nH=0$, $\partial_nv_t-\kappa_{\mathrm c}v_t=0$ (21), linear in $(v_n,S,H,v_t)$ (Remark 2). **Stated** ("straightforward to deduce"; with $\partial_nS=0$ and $v=v_t\tau$, $\partial_nH=\rho^{-1}\partial_np+v_t\partial_nv_t$, so given (20), $\partial_nH=0$ is equivalent to (18) *(compiler check, not in the sources)*)
11. For space-time ROD in the variables $(v_n,S,H,v_t)$, their modal coefficients come from a space-time $L^2$ projection (Eq. 34), which needs the normal and tangent inside the element, available because the boundary is a level set (§5.3.1, Remark 5). **Derived**
12. The corrected wall flux (36) used in troubled boundary cells is at most third-order accurate for general geometries on conformal linear meshes, which suffices for troubled cells (§5.3.2). **Stated**
13. The time step is $\Delta t<\nu\,h_{\min}/((2N+1)a)$ (Eq. 14) with $\nu<1/d$ for DG on unstructured meshes; troubled cells need no smaller step, since each troubled triangle is split into exactly $(2N+1)^d$ sub-triangles and (14) holds there with $N=0$ (Remark 1). **Stated**
14. Manufactured solution, uncorrected DG on conformal linear meshes: second order for $N=1,2,3$ alike (finest-level rates 2.00–2.01 in all variables; at $N=3$ the finest $\rho$ error is $2.6792\times10^{-5}$) (§6.1, Table 2). **Shown**
15. ROD-DG on conformal linear meshes: rates 2.02–2.17 at $N=1$, 2.61–2.99 at $N=2$, 4.10–4.67 at $N=3$, with finest $\rho$ error $1.5035\times10^{-10}$ at $N=3$ (Table 4). **Shown**
16. ROD-ADER-DG on conformal linear meshes gives errors very close to ROD-DG: finest $\rho$ error $1.4723\times10^{-10}$ and rates 4.07–4.43 at $N=3$, rates 2.60–2.97 at $N=2$ (Table 6). **Shown**
17. On fully embedded meshes both variants converge non-monotonically (e.g. ROD-ADER-DG at $N=3$, $\rho$ rates 3.76, 4.17, 1.53, 4.47), which the authors call typical of embedded methods, since the surrogate boundary approaches the true one depending on how it cuts the background mesh (§6.1, Tables 5, 7). **Shown**
18. "In all cases, the expected convergence of $M+1$ is achieved" (§6.1). **Stated** (the $N=2$ conformal rates are 2.6–2.99; see Printed slips)
19. The space-time formulation gives similar results at a cost about 10 % lower at $N=3$, "remarkable given that the ROD reconstruction only influences the boundary cells" (§6.1). **Shown** (no timings, hardware or mesh given)
20. Supersonic vortex, uncorrected (Dirichlet inner arc, classical slip outer arc): rates below 2 (about 1.5 at $N=1,2$, about 1.1–1.25 at $N=3$), errors that **increase** with degree on a given mesh, and an $N=3$ run on the coarsest mesh that stops before the final time (§6.2, Table 9). **Shown**
21. Reflecting boundary conditions on linear meshes give severe spurious errors that grow with the polynomial degree (§6.2). **Stated**
22. With ROD-ADER-DG and slip walls the observed order is $N$ rather than $N+1$, because the Neumann and Robin conditions use polynomial derivatives; the errors are still several orders of magnitude below the uncorrected ones, and each degree increase lowers the error by at least one order of magnitude (§6.2, Table 10). **Shown** (finest-level rates 2.04–2.11 at $N=1$, 2.07–2.09 at $N=2$, 2.40–2.57 at $N=3$)
23. The lost order could be recovered by building degree-$N$ derivative polynomials from neighbour information for Neumann and Robin cells; not pursued (§6.2). **Stated**
24. Shock–cylinder interaction at $N=3$ on a conformal mesh: naive reflecting conditions produce spurious disturbances that start at the boundary and propagate, while ROD gives much smoother iso-contours near and away from the wall (§6.3, Fig. 8). **Shown** (qualitative)
25. On a fully embedded mesh with ROD the density contours are globally very similar to the conformal ROD run; residual disturbances occur only in boundary cells flagged by the limiter, where the less accurate flux (36) is used (§6.3, Fig. 9). **Shown** (qualitative)
26. Further constraints in the optimization (mass conservation, positivity, entropy) may improve accuracy, conditioning and limiter activation in boundary cells (§7). **Stated**

# Printed slips

- Eq. (38), supersonic-vortex density, is printed $\rho=\rho_i\big(1+\frac{\gamma+1}{2}M_i^2(1-(r_i/r)^2)\big)^{1/(\gamma-1)}$. From the paper's Eq. (39) ($\lvert v\rvert=c_iM_i/r$, $p=\rho^\gamma/\gamma$, hence $c^2=\rho^{\gamma-1}$ and $c_i=1$ for $\rho_i=1$) and Bernoulli's relation $c^2/(\gamma-1)+\lvert v\rvert^2/2=\mathrm{const}$ for the steady irrotational flow, $\rho^{\gamma-1}=1+\frac{\gamma-1}{2}M_i^2\big(1-(r_i/r)^2\big)$: the factor is $(\gamma-1)/2$. At $r_o=1.384$, $M_i=2.25$, $\gamma=1.4$ this gives $\rho\approx2.68$, against $\approx30.1$ from the printed form *(compiler check, not in the sources)*.
- Table 5 (ROD-DG, embedded meshes): the printed orders do not follow from the printed errors and the Table 3 mesh sizes. For $\rho$, $\log(e_{k-1}/e_k)/\log(h_{k-1}/h_k)$ gives 2.42, 1.50, 0.73, 2.50 at $N=1$ (printed 2.26, 1.64, 0.74, 2.26), 4.51, 2.36, 1.97, 3.80 at $N=2$ (printed 4.21, 2.57, 2.00, 3.44) and 4.69, 3.24, 1.72, 4.80 at $N=3$ (printed 4.38, 3.52, 1.74, 4.34); the grid counts in place of $h$ do not reproduce them either. Table 7 is reproduced from the same $h$ to within about 0.04 (ROD-ADER-DG at $N=3$: 3.75, 4.13, 1.55, 4.48 against 3.76, 4.17, 1.53, 4.47) *(compiler check, not in the sources)*.
- §6.1 and the captions of Tables 4 and 6 say the expected order $M+1$ is achieved "in all cases", but the $N=2$ conformal rates are 2.61–2.99 (Table 4) and 2.60–2.97 (Table 6), below 3 at every level. §6.2 says the slip-wall order is $M$ rather than $M+1$, while Table 10 gives 2.04–2.11 at $N=1$ (that is $N+1$) and a decreasing 2.40–2.57 at $N=3$ (below $N$).
- Remark 4 calls system (33) "slightly larger" than (29). The space-time unknowns number $(N+1)(N+2)(N+3)/6$ (10 at $N=2$, 20 at $N=3$) against $N_{\mathrm b}=(N+1)(N+2)/2$ (6, 10), about twice as many; the $9\times9$ and $14\times14$ matrices of §7 equal $N_{\mathrm b}$ plus $N+1$ constraints, a constraint count the paper does not state *(compiler check, not in the sources)*.
- Eq. (24) puts the weight inside the square, $\frac12\sum_q[w_q\mathcal P_M\eta-w_q\bar{\mathcal U}_q]^2$, whose normal equations carry $w_q^2$, while Eq. (25) prints $w_q$ *(compiler check, not in the sources)*.
- Eq. (12) runs $\ell=0,\dots,\mathcal L(M,d+1)$ while Eq. (11) sums to $\mathcal Q-1$ with $\mathcal Q=\mathcal L(M,d+1)$.
- The third-order statement for the flux (36) is cited to [15] (finite-volume ROD for steady convection–diffusion), although the flux itself is attributed to [13] (Krivodonova & Berger).
- §5.1 writes "$w_q:=w(d_q,\delta,\gamma)$", then "$w(D_q,\delta,\gamma)$", and reuses $\gamma$ (ratio of specific heats) as the weight exponent; it calls a degree-$M$ reconstruction "of order $M$".
- The roadmap at the end of §1 skips Section 4. The manufactured and vortex tests print no final time or steady-state criterion and no CFL number; the shock–cylinder test prints no mesh sizes, initial shock position or outer boundary conditions.

# Notation map

| Ciallella et al. (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathcal U$, $\mathcal F$, $\mathcal S$ | $u$, $f$, $S(u)$ | conserved variables, flux, source of the manufactured solution |
| $\mathbf u$ | $v$ | velocity |
| $\rho E$, $E$, $e$, $H$, $h$ | $E$, kept, $e$, $H$, kept | **the source's $E$ is specific total energy**; $h$ (specific enthalpy) is not the numerical flux |
| $M$ | $N$ | DG degree; **$M$ is also the elemental mass matrix in Eqs. (9)–(10) and the inner Mach number $M_i$** |
| $N$ | $N_{\mathrm b}$ | number of spatial coefficients $(N+1)(N+2)/2$; **$N$ is the degree in the registry** |
| $\mathcal U_h^-$, $\mathcal U_h^+$ | $u^-$, $u^+$ | interior and neighbour traces |
| $\hat{\mathcal F}$, $s_{max}$ | $h^{\mathrm{LF}}$, $a$ | Rusanov flux and maximum spectral radius |
| $\lambda_{max}$, $\mathrm{CFL}$, $h_{min}$ | $a$, $\nu$, kept | Eq. (14) |
| $q_h$, $\hat q_\ell$, $\theta_\ell$, $\mathcal Q$ | kept | ADER predictor, its coefficients, space-time Taylor basis, number of space-time modes; **$\theta$ is the Zhang–Shu factor in the registry** |
| $\alpha_i$, $\omega_i$ | kept, $\mathsf w_i$ | time-quadrature nodes and weights |
| $\mathbf n$, $\boldsymbol\tau$, $\tilde{\mathbf n}$ | kept | true-boundary normal and tangent, discrete-boundary normal; **$\tilde n$ is the observed order in the tables** |
| $u_n$, $u_\tau$ | $v_n$, $v_t$ | normal and tangential velocity (page-local, as on the immersed-boundary page) |
| $k$ | $\kappa_{\mathrm c}$ | boundary curvature (registry §10) |
| $S=p\rho^{-\gamma}$ | kept | entropy function, $=e^{s}$ with the registry's $s$; **collides with the source $S(u)$** |
| $\phi$ | kept | signed-distance level set |
| $\varphi$, $\mathcal P_M$, $\eta$, $\mathbf m$ | kept | ROD polynomial, monomial row vector, coefficients, barycentre; **$\eta$ is the entropy in the registry** |
| $w_q$, $\delta$, $D_q$, $\gamma$ (weight) | kept | least-squares weight, sensitivity factor, distance, exponent; **$\gamma$ collides with the ratio of specific heats** |
| $\mathcal A$, $b$, $\mathcal C$, $\varrho$, $\lambda$, $p$ | kept | normal matrix, right side, constraint matrix and data, multipliers, number of constraints; **$\lambda$ is not an eigenvalue, $p$ not the pressure** |
| $\alpha_\Gamma$, $\beta_\Gamma$, $g_\Gamma$ | kept | Robin coefficients and data; **$\alpha$ is not a weight or the blending coefficient** |

# Reference list

52 printed references, numbered Elsevier style, all parsed and merged
complete into the [bibliography](/bibliography.md) with `citedby`
`ciallella-2024`. Refs. [6] (Loseille & Rochery) and [7] (Couplet, Reberol &
Remacle) print no year and no venue name, only an AIAA URL in an "arXiv:"
field and a DOI; they are keyed with the citing year (`loseille-2024`,
`couplet-2024`) and a note. Ref. [12] prints no pages, ref. [21] no volume;
ref. [25] is an arXiv preprint; ref. [35] carries the reprint year 2012. Ref.
[14] (Ciallella, Gaburro, Lorini & Ricchiuto, Appl. Math. Comput. 441:127698,
2023) is a different work from the ingested `ciallella-2023` and is merged
under a distinct key. No printed duplicates were found.

# Pages created or updated

Chunk 7 (2026-10-23). This source is cited on:

* [ADER schemes](/methods/ader-scheme.md)
* [Discontinuous Galerkin method](/methods/discontinuous-galerkin.md)
* [Immersed-boundary and cut-cell methods](/methods/immersed-boundary-method.md)
* [Method of manufactured solutions](/definitions/method-of-manufactured-solutions.md)
* [MOOD a posteriori limiting](/methods/mood-a-posteriori-limiting.md)
* [Subcell finite-volume limiting for DG](/methods/subcell-finite-volume-limiting.md)
* [Supersonic vortex between concentric arcs](/benchmarks/supersonic-vortex-between-arcs.md)
