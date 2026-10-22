---
type: Method
title: "Gradient reconstruction on unstructured meshes"
description: "Cell-centred finite volumes on unstructured meshes reconstruct a cell gradient, or a higher-degree polynomial, from neighbouring averages; this page records the Green–Gauss and least-squares gradient families, the vertex-based averaged gradient (VWLSQ) with iterative boundary treatment, face-gradient decoupling, a WENO-type weighting replacing the limiter, and the constrained least-squares polynomials of high-order WENO and TENO."
status: established
aliases: [constrained least-squares reconstruction, VWLSQ, VWLSQ-ITER, vertex-based weighted least squares, node-averaging Green–Gauss, NAGG, WLSQ, least-squares gradient, nonlinear weighting strategy, NW]
tags: [finite-volume, reconstruction, limiting, weno]
timestamp: 2026-10-23T08:00:00Z
---

# Gradient reconstruction on unstructured meshes

A second-order cell-centred finite-volume scheme on an unstructured mesh reconstructs, in each cell
$i$, a linear function from the cell value $u_i$ and a reconstructed gradient $\nabla u_i$, and
evaluates the face states as

$$u_k=u_i+\theta_i\,\nabla u_i\cdot\Delta r_{ik},$$

with $\Delta r_{ik}$ the vector from the cell centroid to the centroid of face $k$ and
$\theta_i\in[0,1]$ a slope-limiter coefficient (page-local symbols; $\theta_i$ scales the linear
part as the factor of a [Zhang–Shu limiter](/methods/zhang-shu-scaling-limiter.md) does)
([Chen, Zhang, Liu & Chen (2022)](/sources/chen-2022.md), §2, Eq. (8)). The same gradients enter the
viscous fluxes through face gradients. Chen et al. reconstruct primitive variables, with an HLLC flux
for shock-free and van Leer flux-vector splitting for shocked problems, and LU-SGS (steady) or
four-stage Runge–Kutta (unsteady) stepping (§2). "Order" on this page follows the paper: a gradient
that is exact for linear data ("linearly exact") is first-order accurate, and the scheme is second
order.

## Families of gradient

Chen et al. (2022, §3.1, §4.1) compare, as recalled background:

- **Node-averaging Green–Gauss (NAGG)**: Green–Gauss on the cell faces with vertex values averaged
  from the surrounding cells by inverse-distance (IDW) or pseudo-Laplacian (PLW) weights; linearly
  exact only on regular grids. Cell-averaging Green–Gauss (CAGG) is mentioned as more robust on
  regular high-aspect-ratio grids but less accurate, and not shown.
- **Cell-based weighted least squares (WLSQ($n$))**, weights $1/L^n$ with $L$ the centre distance,
  on the face-neighbour stencil (WLSQ-F) or the vertex-neighbour stencil (WLSQ-V); both use the
  vertex stencil in boundary cells, since there are no ghost cells. On a Cartesian grid WLSQ-F is the
  second-order central difference (Eq. (C.5)).
- **Vertex-based least-squares averaged gradient (VWLSQ)**, the authors' method (recalled from their
  earlier papers, §3.2): at each vertex $a$, a weighted least-squares fit of a linear function
  through the centre values of the $N_c$ surrounding cells,
  $$\min_{u_a,\nabla u_a}\ \sum_{i=1}^{N_c}w_i\big(u_i-u_a-\nabla u_a\cdot\Delta r_{ai}\big)^2,\qquad w_i=L_{ai}^{-n},$$
  with the vertex value $u_a$ among the unknowns ($d+1$ unknowns in $d$ dimensions; the normal matrix
  depends on geometry and weights only), then the cell gradient as a convex combination of its $N_v$
  vertex gradients,
  $$\nabla u_i=\sum_{a=1}^{N_v}d_a\nabla u_a,\qquad d_a=\frac{L_{ai}^{-m}}{\sum_lL_{li}^{-m}}$$
  (page-local $a$, $L_{ai}$ the vertex-to-centre distance, $n$, $m$; Eqs. (10)–(16)). The method is
  named VWLSQ($n$-$m$); the tests use VWLSQ(1-0), inverse-distance fit and equal vertex weights.
- **Iterative boundary treatment (VWLSQ-ITER).** At boundary vertices the boundary-face values join
  the fit, $u_{bf}\approx u_a+\nabla u_a\cdot\Delta r_{a,bf}$; since they are unknown, face values and
  gradients are iterated with the boundary conditions imposed at each pass (Eq. (17); App. B,
  Algorithm 1: tolerance $10^{-5}$ viscous and $10^{-8}$ inviscid, at most 10 passes).

On $x^2e^y$ over regular, irregular and perturbed triangles, the NAGG methods lose linear exactness
of the cell gradient on perturbed grids, in the interior and at the boundary, whereas WLSQ and
VWLSQ-ITER stay linearly exact, VWLSQ with the smaller interior errors (§6.1, Figs. 3–4). At boundary
faces all NAGG and WLSQ variants, which extrapolate boundary values to first order, lose linear
exactness, and VWLSQ-ITER keeps it (Figs. 8–10); on aspect-ratio-1000 perturbed triangles with a
manufactured boundary-layer profile (from Sun, Darmofal & Haimes; only the gradient is evaluated, no
equation is solved) VWLSQ-ITER has the lowest wall-normal gradient errors (§6.2, Figs. 11–12;
[method of manufactured solutions](/definitions/method-of-manufactured-solutions.md)).

## Face gradients and decoupling

Viscous fluxes need gradients at faces. The average of the two adjacent cell gradients, the "A"
methods of Chen et al., can be corrected along the centre-to-centre direction (Crumpton, Moinier &
Giles; the "B" methods),
$$\nabla u_k=\overline{\nabla u}_k-\Big(\overline{\nabla u}_k\cdot l_{ij}-\frac{u_j-u_i}{|x_j-x_i|}\Big)l_{ij},$$
with $l_{ij}$ the unit vector between the centres (page-local; Eqs. (18)–(21)). Chen et al. (§4.2,
Eqs. (22)–(23)) instead average the VWLSQ gradients of the face's own vertices (in 2-D the two end
points, weights $\tfrac12$), reusing the vertex gradients of the convective reconstruction; on
Cartesian grids this is a trapezoidal rule. Face gradients always use the linear weights, even when
the nonlinear weighting below is active (§5).

Appendix C works the $x$-diffusion term of a cell on a uniform Cartesian grid. Averaged NAGG
gradients give a contribution without $u_{i\pm1,j}$ (Eq. (C.3)); averaged WLSQ-F (central)
gradients give
$\frac1{4\Delta x}\big(u_{i+2,j}-2u_{i,j}+u_{i-2,j}\big)$ (Eq. (C.6)), the wide Laplacian, independent
of all immediate neighbours, which produces checkerboard wiggles; the VWLSQ face gradient gives a
compact $3\times3$ stencil (Eq. (C.8)) with no decoupling. WLSQ-V is said to decouple like NAGG
("straightforward to prove", not shown). *(Compiler check, not in the sources: (C.6) follows from
averaging the central gradients $(u_{i+1}-u_{i-1})/(2\Delta x)$ of neighbouring cells, as printed.)*

## Nonlinear weighting instead of a slope limiter

For shocks, Chen et al. (2022, §5, Eqs. (24)–(27)) replace the limiter ($\theta_i=1$ throughout) by a
"WENO-type" nonlinear weighting strategy (NW) in two parts:

1. **Solution-dependent fit.** The least-squares weights become
   $\tilde w_i=w_i/\big((p_a-p_i)^2+\epsilon\big)$, with $p_a$ the inverse-distance vertex pressure
   and $p_i$ the cell pressure; pressure alone is the discontinuity detector, so the normal matrix is
   shared by all variables, though it must be rebuilt every step at every vertex. The authors relate
   it to the solution-dependent least squares of Mandal et al. ([WLS-ENO](/methods/wls-eno.md) is the
   high-order relative).
2. **Nonlinear vertex combination**, direction by direction:
   $$\partial_xu_i=\sum_a\omega^x_a\,\partial_xu_a,\qquad \omega^x_a=\frac{d_a/(\epsilon+\beta^x_a)^2}{\sum_ld_l/(\epsilon+\beta^x_l)^2},\qquad \beta^x_a=(\partial_xu_a)^2|K_i|,$$
   and the same in $y$, with $|K_i|$ the cell area (page-local $\beta^x_a$). This is the
   [WENO-JS](/methods/weno-js-reconstruction.md) form with exponent 2 applied to gradients of a
   second-order scheme, not to candidate polynomials of a high-order one; $\beta^x_a$ scales as
   $h^2|\nabla u|^2$ like a Jiang–Shu indicator ([smoothness indicators](/definitions/smoothness-indicator.md)).

The same $\epsilon$ is used in both parts: $10^{-3}$ by default, $10^{-5}$ in the smooth accuracy
tests; a larger value is more accurate in smooth regions, a smaller one suppresses oscillations
better, with $10^{-2}$ to $10^{-6}$ the typical range (§5, §6.7). The weighting also replaces the
vectorial limiter of the earlier iterative boundary treatment (App. B). The authors call the scheme
new for second-order finite-volume shock capturing.

**Evidence** (all numerical; Chen et al. 2022, §6):

- *Smooth data.* With $\epsilon=10^{-5}$ NW keeps the gradient accuracy of the linear method on
  $x^2e^y$ (§6.1). On the Euler [isentropic vortex](/benchmarks/isentropic-vortex.md) on triangles
  (HLLC, RK4, $\Delta t=0.002$, $t=2$), density errors of VWLSQ(1-0)-ITER with and without NW are
  $4.02\times10^{-3}$ and $3.29\times10^{-3}$ at $h=0.4$ and both $3.59\times10^{-5}$ at $h=0.05$, last
  order 1.90; NAGG-IDW drops to 0.86 (Table 1).
- *Steady hypersonic cylinder.* At Mach 5 (van Leer, LU-SGS, CFL up to 100) only VWLSQ-ITER with NW
  converges fully on the fine grid, and it alone gives oscillation-free contours and no post-shock
  pressure overshoot on the stagnation line; at Mach 10 it alone converges fully on the coarse grid,
  while VWLSQ-ITER with the MLP-pw limiter (Venkatakrishnan function) diverges (§6.4, Figs. 15–19).
  The NW "limiting coefficient" is active mostly at the shock (Fig. 18).
- *Cost* of one reconstruction on the coarse Mach-5 grid (hardware not stated): NAGG-PLW 6.77 ms,
  WLSQ(1)-F 23.49 ms, WLSQ(1)-V 40.36 ms, VWLSQ(1-0)-ITER with MLP-pw 17.92 ms, with NW 14.84 ms
  (Table 2).
- *Unsteady shocks.* On a Mach-10 [double Mach reflection](/benchmarks/double-mach-reflection.md)
  over a ramp on 576,910 triangles, WLSQ-F and WLSQ-V with MLP-pw give kinked Mach stems, WLSQ-V most;
  VWLSQ-ITER with NW, on the same vertex stencil as WLSQ-V, does not. Since all runs use the same van
  Leer flux, the authors attribute the kinks to reconstruction and limiter rather than to a flux
  instability (§6.5, Fig. 22; [carbuncle phenomenon](/definitions/carbuncle-phenomenon.md)).
- *Viscous.* On a laminar flat plate at $\mathrm{Re}=10^6$ and a cylinder at $\mathrm{Re}=40$ on
  high-aspect-ratio triangles only the VWLSQ variants converge fully (the plate also with WLSQ-F with
  the correction, which however misses the velocity profile and skin friction); cylinder wake length
  2.14 (2.095 with the correction) against 2.13, drag 1.588 (1.591) against 1.48 (§§6.6–6.7, Table 3).

## Beyond second order: constrained least-squares polynomials

The high-order unstructured reconstructions of the bundle generalize the least-squares gradient to a
polynomial of degree $\mathsf r$ (page-local) per stencil. Ji, Liang & Fu (2022, §2.2, Eqs. (4)–(14)),
in the framework of Tsoutsanis and co-workers ([UCNS3D](/software/ucns3d.md)), map each element to a
reference space by an affine map of one of its sub-triangles or sub-tetrahedra, which leaves cell averages
unchanged, and expand the polynomial in a zero-mean basis $\varphi_l-\frac1{|V_0'|}\int_{V_0'}\varphi_l$ over
the target cell (page-local monomials $\varphi_l$, reference volume $V_0'$), so the target average is
matched exactly. Matching the averages of the other $N_s$ stencil cells gives an over-determined system
solved in the least-squares sense through a Householder QR; the matrix is geometric and precomputed, so
each reconstruction is a matrix–vector product. The stencil size is $N_s=2N_k$, $N_k$ the number of
coefficients, "recommended … according to various studies". Large central stencils come from a
"naive cell-based" algorithm and small directional ones from the "Type3" algorithm; the same polynomials
feed unstructured WENO, [CWENO](/methods/cweno.md) and the unstructured TENO of Ji et al.
([targeted ENO](/methods/targeted-eno.md)), and the [CWENO](/methods/cweno.md) page records the same
construction from Tsoutsanis et al. (2021). On a 2-D advection test on triangles the linear schemes of
orders 3 to 6 converge at $L_\infty$/$L_2$ orders 2.92/3.01, 3.61/3.83, 4.93/5.01 and 5.97/5.90 at the
finest pair ($h=1/80\to1/160$; Tables 1–4), the fourth-order one below its design order.

## Relation to limiters

Chen et al. (§1, §5) motivate NW by the limitations of limiters: second-order TVD-type limiters lose
accuracy at smooth critical points, the TVD principle cannot guarantee non-oscillatory results on
unstructured grids (citing Jameson), and several common limiters cannot strictly guarantee
monotonicity ([TVD limiters](/definitions/total-variation-diminishing.md),
[critical-point accuracy](/properties/critical-point-accuracy.md)). They also note that their method
"is not necessary the best choice across different scenarios, as only a limited amount of methods have
been discussed in a few test cases" (§6.4).

## Qualifications

- **Scale dependence.** *(Compiler check, not in the sources: the fit weight
  $(p_a-p_i)^2+\epsilon$ and the combination weight $(\epsilon+\beta^x_a)^2$ use dimensional data
  against a fixed $\epsilon$, the same for every primitive variable, so the weights change with the
  units and the magnitude of the data, the dependence analysed on the
  [scale invariance](/properties/scale-invariance.md) page.)*
- **Rotational invariance.** The direction-by-direction weighting "loses the rotationally invariant
  property"; the authors cite multi-dimensional-limiter work that this is not a particular drawback
  (§5).
- **"WENO-type" without WENO analysis.** No ENO-property or order analysis of the weighting is given.
  The claim of keeping accuracy at smooth critical points rests on the isentropic vortex alone,
  where NW has the larger error on the two coarsest meshes.
- **Cost statement.** §5 says re-solving the vertex systems increases the cost against linear VWLSQ;
  Table 2 shows NW cheaper than VWLSQ-ITER with MLP-pw, which is consistent only if the limiter costs
  more than the re-solve; one grid is reported.
- **Attribution of the viscous results.** NW and linear variants give identical wake lengths and
  drag (Table 3), and NW is inactive in face gradients by §5; the conclusion's link between NW and
  convergence "without specifically concerning the decoupling problem" (§7) is not the mechanism of
  Appendix C, which credits the vertex-based face gradient.
- Table 3 heads both reference values "Experiment" and §6.7 calls the computed drag "close to the
  experimental result"; the drag reference is Visbal's paper, whose title evaluates an implicit
  Navier–Stokes solver, and 1.588 differs from 1.48 by 7 % *(compiler check, not in the sources:
  $1.588/1.48=1.073$)*.
- Ji et al. (2022, Eq. (6)) give $N_k=\frac1{n_d!}\prod_{m=1}^{n_d}(\mathsf r+m)$ coefficients ($n_d$ the dimension,
  page-local), which counts the constant term, while their expansion (Eq. (7)) writes the cell average
  plus $N_k$ non-constant terms; the two differ by one. *(Compiler check, not in the sources: for
  $\mathsf r=1$, $n_d=2$ Eq. (6) gives 3, the number of monomials of degree at most 1.)*

# Citations

- [Chen, Zhang, Liu & Chen (2022)](/sources/chen-2022.md) — §1; §2, Eqs. (1)–(9); §3, Eqs. (10)–(17); §4, Eqs. (18)–(23); §5, Eqs. (24)–(27); §6, Tables 1–3, Figs. 3–27; §7; App. B, Algorithm 1; App. C, Eqs. (C.1)–(C.8).
- [Ji, Liang & Fu (2022)](/sources/ji-2022.md) — §2.2, Eqs. (4)–(14); §3.1; §5.1, Tables 1–4.
