---
type: Method
title: "Conservative semi-Lagrangian finite-volume WENO"
description: "A semi-Lagrangian finite-volume scheme updates each cell average as the integral of the old solution over its upstream cell; Zheng et al. reach fourth order in 2-D without dimensional splitting by cubic-curved upstream cells, a WENO-ZQ polynomial reconstruction and Green's-theorem clipping, with mass conservation, positivity and large CFL numbers."
status: established
aliases: [semi-Lagrangian finite volume, SL FV WENO, non-splitting semi-Lagrangian WENO, conservative semi-Lagrangian scheme, SLWENO]
tags: [finite-volume, weno, cweno, positivity, reconstruction]
timestamp: 2026-10-22T12:00:00Z
---

# Conservative semi-Lagrangian finite-volume WENO

A **semi-Lagrangian (SL) finite-volume** scheme for the transport equation
$\partial_tu+\nabla\cdot(vu)=0$, $v=(v_1,v_2)(x,y,t)$, does not integrate fluxes in time. By Reynolds'
transport theorem, the integral of $u$ over the moving image of a cell is constant, so the new cell
average is exactly the average of the old solution over the cell's **upstream** (characteristic-foot)
region (Zheng, Cai, Qiu & Qiu 2022, §2, Eqs. (3)–(5)):

$$\bar u^{n+1}_{i,j}=\frac1{\Delta x\Delta y}\iint_{I^\star_{i,j}}u(x,y,t^n)\,dx\,dy,\qquad I^\star_{i,j}=I_{i,j}(t^n),$$

where $I_{i,j}(t)$ is the image of $I_{i,j}$ under the backward characteristics
$\dot X=v(X,t)$, $X(t^{n+1})\in I_{i,j}$ (page-local $I^\star$, $X$). The update has no CFL
restriction of its own; the time step is set through a CFL number, 10.2 in the tests (§4). The
framework goes back to CSLAM-type remapping (Lauritzen et al.) and the authors' third-order SL DG work
(§1, §2).

## Fourth-order scheme without splitting

Zheng et al. (2022) realize the identity to fourth order in 2-D without dimensional splitting:

- **Cubic-curved upstream cells** (§2.1, App. A). The four Gauss–Lobatto points of each Eulerian edge
  are traced back to $t^n$ by a fourth-order Runge–Kutta solver; each edge of the approximate
  upstream cell is the parametric cubic through the four feet, built as a graph over the chord between
  the end feet after an affine map (Eqs. (6), (A.1)–(A.3)).
- **Reconstruction.** The two-dimensional fourth-order WENO-ZQ of the paper, a CWENO-type
  reconstruction that returns a full $\mathbb P^3$ polynomial per cell from a 13-cell stencil and four
  $\mathbb P^1$ candidates, with the cell average as its constant coefficient (§2.2;
  [CWENO](/methods/cweno.md)). The authors judge WENO-JS unusable here, since SL needs the
  reconstruction "at any spatial position" (§1).
- **Clipping and Green's theorem** (§2.3, App. B). The upstream cell is cut by the Eulerian mesh into
  curved pieces; each piece's integral is turned into line integrals along **outer** segments (pieces
  of the cubic edges) and **inner** segments (pieces of mesh lines), with potentials whose curl is the
  reconstruction of the overlapped cell (Eqs. (17)–(21)). Three-point Gauss–Legendre quadrature per
  segment is exact on inner segments and "of sixth-order accuracy" on the cubic ones (§2.3.2).
  Intersections come from roots of cubics; for near-tangencies and endpoints near a mesh line the
  authors "do not state a standard way to treat them" (App. B.1).
- **Positivity.** A [Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md) on each
  reconstruction, with the cell minimum found exactly by solving $\nabla\tilde u=0$, two quadratics,
  i.e. intersecting conics (Eqs. (22)–(24)). Remark 2.1: unlike the quadrature-point minima of Zhang &
  Shu's survey, the minimum over the whole cell is needed, which the authors attribute to the
  Green's-formula integration.
- **Nonlinear models.** When the velocity depends on the solution (Vlasov–Poisson, guiding-centre
  model, incompressible Euler in vorticity form), the SL step is composed in the fourth-order
  commutator-free Runge–Kutta exponential integrator CF4 of Celledoni, Marthinsen & Owren, each stage
  an SL step with a combination of stage velocity fields (Eq. (53), Table 3).

## Analysis

- **Mass conservation** (Prop. 3.1): with periodic boundaries the total mass is conserved, because
  inner-segment integrals are exact and cancel between neighbouring pieces and the reconstruction
  keeps the cell average (Eq. (25)). Conservation here comes from exact remapping, not from a flux
  form ([local conservation and flux form](/results/local-conservation-flux-form.md)).
- **Positivity** (Prop. 3.2): positivity-preserving with the limiter "if the line integrals ... are
  exactly evaluated" ([bound preservation](/properties/bound-preservation.md)).
- **Geometry** (Lemmas 3.3–3.5): for $v\in C^4$ and $\Delta t\sim\Delta x\sim\Delta y$ the exact
  upstream image of an edge deviates from a straight edge by $O(\Delta t)$ in slope and in its higher
  derivatives, so it is a graph over its chord.
- **Truncation** (Prop. 3.6): with exact input averages and $u,v\in C^4$, the one-step error of the
  cell average is $O(h^4)$, $h\sim\Delta x\sim\Delta y\sim\Delta t$ (page-local $h$), from a
  reconstruction error $O(h^4)$, quadrature error $O(h^6)$ and an upstream-cell area error $O(h^6)$;
  the error of the RK4 characteristic feet is called "not dominant" without proof (Remark 3.8).
- **Stability** (Prop. 3.9): with the linear reconstruction ($\tilde u=\mathbb P^3$ part, no weights),
  constant coefficients and periodic boundaries, the scheme is $L^2$ stable for every CFL number; the
  argument reduces the Courant numbers to $[0,1]^2$ and checks the (unprinted) amplification factor
  $\le1$ on 1000 samples per variable (App. C).

## Results

At CFL 10.2 the non-split scheme is compared with the authors' fourth-order dimensionally split SL FV
scheme (§4, Tables 1–5):

- **Constant-coefficient transport** ($u_0=\sin(x+y)$, $T=2$, no time error): fourth order (orders
  7.55, 4.03, 4.00, $L^2$ $3.22\times10^{-9}$ at $320^2$); the split scheme is fifth order
  ($5.43\times10^{-11}$) and "much more efficient" (Table 1, Fig. 6).
- **Swirling deformation** ($T=1.5$): orders 3.47–3.71 from $40^2$ to $1280^2$, then 9.66 and 4.50;
  more accurate than the split scheme up to $640^2$, similar efficiency; fourth order in time for
  both (Table 2, Fig. 7). Discontinuous data stay non-negative (Figs. 9–10).
- **Vlasov–Poisson** (strong Landau damping, $T=2$): orders 3.67–4.68, $2.90\times10^{-8}$ at
  $256^2$, more accurate than split but costlier; mass and $L^1$ norm conserved to about $10^{-13}$
  (Table 4, Figs. 11, 13); two-stream and bump-on-tail runs agree with the literature.
- **Guiding-centre [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)**
  ($T=5$, incompressible drift model, not compressible Euler): the non-split scheme converges at orders
  3.73–7.22 ($8.89\times10^{-11}$ at $512^2$), the split one at **first order** (0.88–0.99), the
  order reduction the paper is built to avoid (Table 5, Fig. 15); energy and enstrophy are conserved
  better by the non-split scheme here and on vortex-patch and shear-flow tests (Figs. 18, 20–21).

## Qualifications

- **Global order.** *(Compiler check, not in the sources:)* a one-step error $O(h^4)$ with
  $\Delta t\sim h$, summed over $O(h^{-1})$ steps, bounds the global error by $O(h^3)$ only; the
  paper claims fourth order without discussing this, so global fourth order rests on the tables, not
  on Prop. 3.6.
- **Stability by sampling.** Prop. 3.9 is a numerical check of a von Neumann condition for the linear
  reconstruction and constant coefficients, labelled a proof by the authors.
- **Observed orders.** The swirling-flow orders below 3.75 over six refinements are reported as
  "Fourth order accuracy is observed"; reference-solution errors give erratic rates elsewhere (7.55,
  4.68, 7.22).
- **Printed slips.** Eq. (53) prints $\tfrac12\Delta t$ in the fourth stage and both output
  exponentials of CF4, where the coefficients of Table 3 require the full step; the Table 5 caption
  says CFL 1 and the text CFL 10.2; the limiter factor is printed $\min\{|\bar u/(\bar u-m)|\}$ without
  the "$,1$" of the Zhang–Shu limiter; the stability appendix uses $\Delta x$ in both Courant numbers;
  the indicator sums of the reconstruction start at order zero (see
  [smoothness indicators](/definitions/smoothness-indicator.md)).
- The scheme is for transport equations with a velocity field; the bundle's compressible systems
  enter only through the incompressible-Euler and kinetic tests.

# Citations

- [Zheng et al. (2022)](/sources/zheng-2022.md) — §1; §2, Eqs. (2)–(24), Remark 2.1; §3, Props. 3.1–3.9, Lemmas 3.3–3.5; §4, Tables 1–5, Figs. 6–21; §5; Apps. A–C.
