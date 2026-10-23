---
type: Method
title: "RBF differential-quadrature finite volumes"
description: "The implicit RBF differential-quadrature finite-volume method (IRBFDQ-FV) of Liu et al. evolves cell-centre point values with a cubic Taylor polynomial whose derivatives come from meshless multiquadric RBF quadrature, so a non-diagonal mass operator makes it implicit; it uses Roe or gas-kinetic fluxes and a PEEB scaling limiter on unstructured grids."
status: established
aliases: [IRBFDQ-FV, RBFDQ-FV, LRBFDQ, local RBF differential quadrature, RBF-based differential quadrature, PEEB limiter, point extrema-based extended bounds limiter]
tags: [finite-volume, reconstruction, limiting, numerical-flux]
timestamp: 2026-10-23T20:00:00Z
---

# RBF differential-quadrature finite volumes

Liu, Shu, Yang, Liu, Liu & Zhang (2023b) extend their radial-basis-function differential-quadrature
finite-volume method (RBFDQ-FV), earlier applied to incompressible flow, to two-dimensional inviscid
and viscous compressible flow on unstructured triangular and quadrilateral grids. They state that
this is its first use for compressible flow (§1).

Each cell carries a cubic Taylor polynomial about its centre, nine derivative coefficients that the
authors call a "fourth-order approximation". The derivatives are not fitted to cell averages, as in
$k$-exact or least-squares reconstruction
([gradient reconstruction on unstructured meshes](/methods/unstructured-gradient-reconstruction.md)).
They come from a meshless differential quadrature on the **cell-centre point values** of neighbouring
cells. RBFs enter only this derivative step, not the candidates of a WENO scheme as in
[RBF-based WENO](/methods/rbf-weno.md).

## Local RBF differential quadrature

At a reference point $X_i$ with $N$ supporting points $X_j$, a derivative is a weighted sum of point
values (page-local symbols: $a^{(p)}_{ij}$ the quadrature weights, $\varphi_k$ the RBFs, $\mathsf G$
the collocation matrix; Liu et al. 2023b, §2.1, Eqs. (1)–(4)):

$$\frac{\partial^pf(X_i)}{\partial x^p}=\sum_{j=1}^Na^{(p)}_{ij}f(X_j),\qquad
a^{(p)}=\mathsf G^{-1}\frac{\partial^p\boldsymbol\varphi}{\partial x^p}(X_i),\qquad \mathsf G_{kj}=\varphi_k(X_j).$$

The weights make the formula exact on the $N$ RBFs. The basis is the multiquadric
$\sqrt{(x-x_j)^2+(y-y_j)^2+c^2}$, normalized by the diameter $D_i$ of the smallest circle that
encloses the supporting points (page-local $c$, $D_i$; Eqs. (5)–(7)). The default shape parameter
$c=30d_{\min}/\sqrt N$ is "based on numerous experiments" ($d_{\min}$ the smallest distance from the
reference to a supporting point, page-local; §2.2). The supporting points are the centres of the von
Neumann neighbourhood of range $l\le3$ (§2.2). The weights depend only on the point positions, so on
a fixed mesh the $9\times N$ weight matrix is computed once (§3.1.1).

## Implicit finite-volume update

The conserved variables are written, in cell $\Omega_i$ (page-local), as

$$u(x,y)=u(x_i,y_i)+\sum_{k=1}^9u^{[k]}_i\,\mathsf C_k(x-x_i,y-y_i)+O(\Delta x^4,\Delta y^4),$$

where the $u^{[k]}_i$ are the nine derivatives $\partial_x,\partial_y,\partial_{xx},\partial_{yy},
\partial_{xy},\partial_{xxx},\partial_{yyy},\partial_{xxy},\partial_{xyy}$ at the centre and the $\mathsf C_k$
the matching Taylor monomials with their factorials (page-local; Eqs. (12)–(13)). Integrating over
the cell gives

$$\int_{\Omega_i}u\,d\Omega=|\Omega_i|\,u(x_i,y_i)+\sum_ku^{[k]}_i\int_{\Omega_i}\mathsf C_k\,d\Omega .$$

The derivatives are linear combinations of neighbouring centre values. Substituting them into the
finite-volume balance therefore couples the time derivatives of the cell and its neighbours through a
non-diagonal mass operator $\mathsf M_i$ (page-local):

$$\mathsf M_i\,\frac{\partial u}{\partial t}=-\mathsf R_i,$$

with $\mathsf R_i$ the flux sum over the faces, two Gauss points per face (Eqs. (11), (14)–(17)). "The
presence of $\mathsf M_i$ suggests the implicitness of the proposed method", hence the name IRBFDQ-FV.

Time stepping (§3.2, Eqs. (26)–(35)):
- **Steady problems.** LU-SGS with $\mathsf M$ replaced by its diagonal term, at CFL 2000.
- **Unsteady problems.** A four-stage ESDIRK scheme with dual time stepping in each implicit stage
  and inner LU-SGS iterations, at pseudo-CFL 5. The full $\mathsf M$ is kept in the unsteady residual
  "to keep temporal accuracy" and replaced by its diagonal only in the iteration operator.

## Fluxes

- **Inviscid flux.** A Roe scheme, chosen "due to its simplicity and good positivity property for
  problems with strong shock wave and expansion wave" (§1). The cited form is the shock-stable Roe
  scheme of Kim et al. ([Roe solver](/methods/roe-riemann-solver.md)).
- **Viscous flux.** The discrete gas-kinetic flux solver DGKFS evaluates the convective and viscous
  fluxes together from a D2Q4 discrete-velocity model (§3.1.2, Eqs. (18)–(25);
  [gas-kinetic schemes](/methods/gas-kinetic-scheme.md)). Four particles on a circle of radius
  $\sqrt{2(\gamma-1)e}$ around the local velocity carry the equilibrium $g_d=\rho/(2\pi)$. Their
  states at the foot of the characteristics are interpolated, upwind, from the cubic polynomials of the
  two cells. The interface flux blends the equilibrium flux and the discrete-particle flux with the
  dimensionless collision time $\mu/(p\,\delta_t)$, where $\delta_t$ is a streaming step (page-local).
  The authors call it simpler and cheaper than Maxwellian-based gas-kinetic schemes. They state that
  it avoids the separate viscous treatment of DG and spectral-volume methods, "still an open problem"
  (§1).

## The PEEB limiter

Shocks are handled by a "point extrema-based extended bounds" (PEEB) limiter (Liu et al. 2023b, §4,
Eqs. (36)–(41)). It scales the whole high-order part of the polynomial by one factor, the way the
[Zhang–Shu limiter](/methods/zhang-shu-scaling-limiter.md) does, but towards the centre point value:

1. **Cell extrema.** Evaluate the primitive variables $(\rho,v_1,v_2,p)$ of the reconstructed
   polynomial at all Gauss points, vertices and the centre of the cell. Record their extrema.
2. **Extended bounds.** Take the extrema of these cell extrema over the vertex neighbours, relaxed by
   a tolerance $\kappa_{\mathrm P}(h)=O(h^{1.5})$ about the centre value (page-local
   $\kappa_{\mathrm P}$). The value used is $100h^{1.5}$, chosen "based on extensive numerical tests".
3. **Limiting factor.** For each variable, the ratio of the bound excursion to the polynomial's
   excursion, passed through $\min\{\cdot/1.1,1\}$. The scalar factor $\theta_i\in[0,1]$ is the minimum
   over the four variables and the two bounds.
4. **Scaling.** Multiply all nine derivative terms by $\theta_i$, the registry's Zhang–Shu factor, here acting about the centre value rather than the cell average. The scaling is applied to the
   conserved variables "for mass conservation at the discrete level".

The bounds use the neighbours' polynomial extrema, not their centre values as in Barth–Jespersen-type
limiters, and are relaxed. The introduction calls PEEB a "positivity preserved limiting procedure"
(§1); the paper gives no proof and no positivity-stressing test
([bound preservation](/properties/bound-preservation.md)). On the smooth vortex the limiter changes the
errors "only slightly" (§5.1.2, Fig. 5).

## Evidence

All results are numerical (Liu et al. 2023b, §5; one PC at 2.30 GHz):

- **Derivatives.** On $\sin(\pi x)\sin(\pi y)$ over five triangular meshes ($h=1/10$ to $1/60$), the
  quadrature gives gradient and Laplacian errors below those of least-squares finite differences
  (LSFD) and $k$-exact reconstruction. The fitted $L_2$ slopes printed in the legend of Fig. 2 are:

  | method | gradient | Laplacian |
  |---|---|---|
  | LRBFDQ, $c=2$ | 3.667 | 2.848 |
  | LRBFDQ, $c=3$ | 3.668 | 3.069 |
  | LSFD | 3.201 | 2.303 |
  | $k$-exact | 3.172 | 2.207 |

  The text gives the theoretical orders as 3 and 2 (§5.1.1).
- **[Isentropic vortex](/benchmarks/isentropic-vortex.md)** on four uniform triangular meshes ($t=2$).
  IRBFDQ-FV, LSFD-FV and $k$-exact FV all reach fourth order in $L_\infty$ and $L_1$. IRBFDQ-FV is the
  most accurate and needs the least CPU time for a given error (§5.1.2, Figs. 3–4; numbers only in the
  figures).
- **Shocks.**
  - On the [Shu–Osher problem](/benchmarks/shu-osher-problem.md) on triangles ($h=1/40$) the smooth
    extrema are kept, where the second-order scheme is diffusive (§5.2).
  - On the Mach 3 [forward-facing step](/benchmarks/forward-facing-step.md) (108,543 triangles,
    $t=4$) the [Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md) roll-up of the contact
    discontinuity appears, which the second-order scheme misses (§5.3).
- **Viscous flows.**
  - NACA0012 at $M=0.8$, $\mathrm{Re}=500$, $10°$ on 5788 triangles: $C_d=0.28926$, $C_l=0.47809$.
    The second-order scheme gives 0.30955 and 0.50802 on the same mesh and 0.29658 and 0.47861 on
    12287 cells (§5.4, Table 1).
  - [Viscous shock tube](/benchmarks/viscous-shock-tube.md) at $\mathrm{Re}=200$: primary-vortex
    height 0.166 at $h=1/500$, against 0.161 at second order; the references give 0.165–0.168
    (§5.5, Table 2).
  - Blasius boundary layer at $\mathrm{Re}=10^5$ on cells of aspect ratio up to 443.6. The implicit
    scheme at CFL 2000 converges faster than four-stage Runge–Kutta at CFL 2 (§5.6).
  - Hypersonic cylinder at $M=8.03$, $\mathrm{Re}=1.835\times10^5$, isothermal wall: no carbuncle.
    Wall pressure and heat flux agree with Wieting's experiment, the heat flux better than at second
    order (§5.7; [flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md),
    [carbuncle phenomenon](/definitions/carbuncle-phenomenon.md)).

## Qualifications

- The fourth-order convergence test is inviscid, with the Roe flux. The DGKFS is stated to be locally
  second order in $\delta_t$ without affecting "the overall accuracy" (§3.1.2), but no viscous
  convergence test is shown.
- The positivity of the Roe flux and of PEEB is asserted, not demonstrated.
- The Laplacian slopes 2.848 and 3.069 and the gradient slopes 3.667 and 3.668 exceed the stated
  theoretical orders 2 and 3. The text says they "agree well with this analytical trend".
- *(Compiler check, not in the sources.)* Eq. (7) divides the normalized weights by $D_i$ for every
  derivative order $p$. With the normalized coordinate $(x-x_i)/D_i$ of Eq. (6), the chain rule gives
  $D_i^{-p}$; this is either a printed slip or an unstated convention.
- Printed inconsistencies:
  - the tolerance is $\kappa(h)$ in §4 but "$\alpha=100h^{1.5}$" in §5.2;
  - §5 announces "four classic benchmark cases" and presents six;
  - the boundary-layer mesh has a maximum aspect ratio of 443.6 but printed minimum sizes
    $\Delta x_{\min}=0.08$, $\Delta y_{\min}=0.05$, a ratio of 1.6 *(compiler check, not in the sources)*;
  - the shape parameter is $c=30d_{\min}/\sqrt N$ by default but "$c=2$ and $c=3$" in §5.1.1, without
    saying whether these are normalized values.

# Citations

- [Liu et al. (2023b)](/sources/liu-2023-b.md) — §1; §2, Eqs. (1)–(7); §3.1, Eqs. (8)–(25); §3.2, Eqs. (26)–(35); §4, Eqs. (36)–(41); §5, Tables 1–2, Figs. 2–18.
