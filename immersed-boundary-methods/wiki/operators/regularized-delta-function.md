---
type: Operator
title: "Regularized delta function $\\delta_h$"
description: "The smoothed approximation of the Dirac delta that links Lagrangian boundary points to the Eulerian grid in the classical immersed boundary method: a tensor product of one-dimensional kernels $\\varphi$ fixed by moment, even–odd and sum-of-squares conditions, with Peskin's 1972 hat kernel, his 4-point kernel and its cosine approximation, and the 3-point and higher-moment variants."
status: established
symbol: "$\\delta_h$"
aliases: [discrete delta function, smoothed delta function, semidiscrete delta function, Peskin delta function, kernel function]
tags: [immersed-boundary, delta-function, coupling-operator, diffuse-interface]
timestamp: 2026-11-08T18:10:00Z
---

# Regularized delta function $\delta_h$

The [classical immersed boundary method](/methods/classical-immersed-boundary-method.md)
writes the coupling between the immersed structure and the fluid with the
Dirac delta: the force density is $\mathbf f(\mathbf x)=\int\mathbf F(\mathbf s)\,\delta(\mathbf x-\mathbf X(\mathbf s))\,d\mathbf s$
and the boundary velocity is $\partial_t\mathbf X=\int\mathbf u(\mathbf x)\,\delta(\mathbf x-\mathbf X)\,d\mathbf x$.
On a grid the Lagrangian points $\mathbf X_\ell$ do not coincide with grid
points, so $\delta$ is replaced by a function $\delta_h$ of support $O(h)$ that
tends to $\delta$ as $h\to0$ ([Peskin 1972](/sources/peskin-1972.md), §III.B;
[Peskin 2002](/sources/peskin-2002.md), §4). It is used in both directions,
by the [spreading and interpolation operators](/operators/spreading-and-interpolation.md).

## Postulates

[Peskin (2002, §6)](/sources/peskin-2002.md) fixes $\delta_h$ by the following
conditions on the tensor-product form
$\delta_h(\mathbf x)=h^{-d}\prod_{m=1}^{d}\varphi(x_m/h)$:

$$\begin{aligned}
&\varphi \text{ continuous},\qquad \varphi(r)=0 \ \text{for}\ |r|\ge 2,\\
&\sum_{j\ \mathrm{even}}\varphi(r-j)=\sum_{j\ \mathrm{odd}}\varphi(r-j)=\tfrac12 \quad\forall r,\\
&\sum_j (r-j)\,\varphi(r-j)=0 \quad\forall r,\\
&\sum_j \varphi(r-j)^2=C \quad\forall r .
\end{aligned}$$

- Continuity avoids jumps in velocity or force as a marker crosses grid
  lines; the bounded support keeps the cost local.
- The even–odd condition implies the unit sum $\sum_j\varphi(r-j)=1$ and
  gives equal weight to the $2^d$ "chains" of grid points that the
  null space of the central-difference gradient $D_0$ decouples, avoiding
  grid-scale oscillations. Peskin (1972, eq. 3.19) already imposed it on his
  four chains $(i,j)$ even/odd.
- The first moment, with the unit sum, makes interpolation exact for linear
  functions, hence second-order accurate for smooth fields.
- The sum-of-squares condition is the $r_1=r_2$ case of exact translation
  invariance $\sum_j\varphi(r_1-j)\varphi(r_2-j)=\Phi(r_1-r_2)$, which Peskin
  proves incompatible with bounded support; with the Schwarz inequality it
  makes the grid-mediated coupling of two markers strongest when they
  coincide. Its value is $C=3/8$.

## Kernels

| kernel | $\varphi(r)$ | support | source |
|---|---|---|---|
| hat (1972) | $\tfrac14\,(2-\lvert r\rvert)$ for $\lvert r\rvert<2$ | $4h$ | [Peskin (1972)](/sources/peskin-1972.md), eq. (3.20), written per direction with the factor $1/16h^2$ in 2-D |
| 4-point (2002) | $\tfrac18\big(3-2\lvert r\rvert+\sqrt{1+4\lvert r\rvert-4r^2}\big)$ for $\lvert r\rvert\le1$; $\tfrac18\big(5-2\lvert r\rvert-\sqrt{-7+12\lvert r\rvert-4r^2}\big)$ for $1\le\lvert r\rvert\le2$ | $4h$ | [Peskin (2002)](/sources/peskin-2002.md), §6 |
| cosine | $\tfrac14\big(1+\cos(\pi r/2)\big)$ for $\lvert r\rvert\le2$ | $4h$ | Peskin (2002, §6): satisfies all postulates except the first moment; used by [LeVeque & Li (1994)](/sources/leveque-1994.md), eq. (1.4) |
| 1-D hat of width $2h$ | $1-\lvert r\rvert$ for $\lvert r\rvert<1$ | $2h$ | LeVeque & Li (1994), eq. (1.3): reproduces $u''=c\,\delta(x-x_\Gamma)$ exactly at grid points in 1-D |
| 3-point | drop the even–odd condition, keep the unit sum | $3h$ | Peskin (2002, §6), for schemes without the $D_0$ null-space problem (e.g. MAC grids, Roma, Peskin and Berger 1999) |
| higher moments | add moment conditions two at a time; 6-point with negative tails | $6h$, … | Peskin (2002, §6), after Stockie (1997) |

The 4-point kernel turns out symmetric and $C^1$ although neither property
was postulated (Peskin 2002, §6). [Goldstein et al. (1993)](/sources/goldstein-1993.md)
spread their feedback force with a narrow Gaussian instead and found the
exact shape "not crucial".

## Qualifications

- With $\delta_h$ the interpolated velocity is only first-order accurate at
  a true interface, where the velocity has a normal-derivative jump
  (Peskin 2002, §6); LeVeque & Li (1994, §5) measure first-order convergence
  for a delta-function source in 2-D
  ([first-order accuracy of regularized-delta forcing](/results/first-order-accuracy-of-regularized-delta-forcing.md)).
- The 1972 hat kernel is the tensor product of hats of half-width $2h$; the
  printed formula is garbled in the text layer of the scan and is read here
  from the chain condition (3.19) and the Fig. 1 caption
  ([Peskin 1972](/sources/peskin-1972.md), Version read).

## Later uses

[Uhlmann (2005)](/sources/uhlmann-2005.md), §3, and [Taira & Colonius (2007)](/sources/taira-2007.md),
§3.2, both use the 3-point kernel of Roma, Peskin and Berger on staggered
grids, where the even–odd decoupling of the central-difference gradient does
not arise. Uhlmann reports second-order interpolation of smooth fields with an
error insensitive to sub-grid shifts of the boundary, and a still smoother
force with the 4-point kernel at higher cost; Taira and Colonius found no
significant differences with other kernels and note that the moment
conditions require a uniform grid near the body.
[Mittal & Iaccarino (2005)](/sources/mittal-2005.md) compare four
distribution functions used in the literature (their Fig. 2b).

## B-spline kernels

[Griffith & Patankar (2020)](/sources/griffith-2020.md) list, besides Peskin's
moment-constrained family, the B-spline kernels built by repeated convolution,
$B_k=B_{k-1}*B_0$, which are $C^k$ piecewise polynomials with support $k+1$
mesh widths; higher discrete moments improve interpolation of smooth fields,
and non-uniform grids need other constructions.

# Citations

- [Peskin (1972)](/sources/peskin-1972.md) — §III.B, eqs. (3.17)–(3.22).
- [Goldstein et al. (1993)](/sources/goldstein-1993.md) — spectral implementation.
- [LeVeque & Li (1994)](/sources/leveque-1994.md) — §1, eqs. (1.3)–(1.5); §5 Example 1.
- [Peskin (2002)](/sources/peskin-2002.md) — §4, §5, §6.
- [Mittal & Iaccarino (2005)](/sources/mittal-2005.md) — continuous-forcing section, Fig. 2.
- [Uhlmann (2005)](/sources/uhlmann-2005.md) — §3, §5.
- [Taira & Colonius (2007)](/sources/taira-2007.md) — §3.2.
- [Griffith & Patankar (2020)](/sources/griffith-2020.md) — discretization.
