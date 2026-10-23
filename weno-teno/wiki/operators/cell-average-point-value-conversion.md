---
type: Operator
title: "Cell-average to point-value conversion"
description: "Explicit symmetric-stencil formulas that turn line, face or cell averages into centre point values and back to a prescribed even order; with them a finite-volume scheme reconstructs one value per face and evaluates the flux pointwise, and without them it is second order in multi-D."
status: established
symbol: "$\\mathsf C_{2p}$, $\\mathsf C_{2p}^{-1}$"
aliases: [average-to-point transformation, AtoP, PtoA, point-value passage, Laplacian correction, deconvolution of cell averages, McCorquodale–Colella correction]
tags: [finite-volume, mhd, reconstruction]
timestamp: 2026-10-23T11:06:00Z
---

# Cell-average to point-value conversion

Let $\mathsf C_{2p}$ (page-local symbol) map the averages $\bar u$ of a smooth function over cells (or faces,
or edges) of a uniform Cartesian grid to its point value at the centre of one of them, exact for
polynomials up to total degree $2p-1$ and hence of order $2p$, and let $\mathsf C^{-1}_{2p}$ map centre point
values to the average. Both are linear, point-symmetric stencils, so odd derivatives cancel. They are the
discrete inverse pair of the averaging that defines finite-volume unknowns:
$\bar u_i=u_i+\tfrac1{24}\Delta x^2u''_i+\tfrac1{1920}\Delta x^4u^{(4)}_i+O(\Delta x^6)$ in 1-D
(Teissier et al. 2024, Eq. (83); arXiv v2 read). Identifying an average with the centre value is therefore an
$O(\Delta x^2)$ error (Eq. (36)), and, because fluxes are nonlinear,
$\overline{\rho v_1v_2}\ne\overline{\rho v_1}\,\overline{\rho v_2}/\bar\rho$ (Eq. (35)): a finite-volume scheme that
evaluates its flux on averaged states is second order in more than one dimension whatever its
reconstruction order.

## Formulas

Write $\bar u^{\Sigma m}=\bar u_{i+m}+\bar u_{i-m}$ for symmetric sums in 1-D, and, on a face (2-D) or in a cell
(3-D), $\bar u^{\Sigma mn}$, $\bar u^{\Sigma mnl}$ for the sum of the averages at all offsets obtained from
$(m,n)$ or $(m,n,l)$ by permutation and sign change, each counted once (4 or 8 terms in 2-D; 6, 8, 12 or 24
in 3-D) (page-local notation; Teissier et al. 2024, Eqs. (42)–(44), (101)–(105)).

**Fourth order.** In 1-D, $u_i=\tfrac{13}{12}\bar u_i-\tfrac1{24}\bar u^{\Sigma1}$ and
$\bar u_i=\tfrac{11}{12}u_i+\tfrac1{24}u^{\Sigma1}$ (Eqs. (111), (116)); on a face,
$u=\tfrac76\bar u-\tfrac1{24}\bar u^{\Sigma10}$ and $\bar u=\tfrac56u+\tfrac1{24}u^{\Sigma10}$ (Eqs. (38), (46)); in a
cell, $u=\tfrac54\bar u-\tfrac1{24}\bar u^{\Sigma100}$ (Eq. (97)). All three are one formula, the
**Laplacian correction** $u=\bar u-\tfrac1{24}\Delta_{\mathrm u}\bar u$, $\bar u=u+\tfrac1{24}\Delta_{\mathrm u}u$ with the
undivided Laplacian $\Delta_{\mathrm u}$ (page-local) over the directions of the average, which is how Berta et
al. (2024, §3.1, Eqs. (16)–(21), App. A) state the McCorquodale–Colella framework for fourth-order
constrained-transport MHD, including the transverse Laplacian for face averages of the normal magnetic field.
*(Compiler check, not in the sources: $\tfrac54\bar u-\tfrac1{24}\bar u^{\Sigma100}=\bar u-\tfrac1{24}(\bar u^{\Sigma100}-6\bar u)$,
and likewise in 1-D and 2-D; the two sources agree.)*

**Sixth to tenth order.** Teissier et al. give every coefficient explicitly, e.g. in 1-D
$$u_i=\tfrac{1067}{960}\bar u_i-\tfrac{29}{480}\bar u^{\Sigma1}+\tfrac3{640}\bar u^{\Sigma2}+O(\Delta x^6),\qquad
\bar u_i=\tfrac{863}{960}u_i+\tfrac{77}{1440}u^{\Sigma1}-\tfrac{17}{5760}u^{\Sigma2}+O(\Delta x^6)$$
(Eqs. (112), (117)), and on a face
$$u=\tfrac{1771}{1440}\bar u-\tfrac{23}{360}\bar u^{\Sigma10}+\tfrac3{640}\bar u^{\Sigma20}+\tfrac1{576}\bar u^{\Sigma11}+O(h^6)$$
($h=\Delta x+\Delta y$; Eq. (39)), up to tenth order in 1-D (Eqs. (111)–(120)), on faces (Eqs. (37)–(41),
(45)–(49)) and in cells (Eqs. (96)–(110)).

**General construction** (App. A). The average of a monomial term is
$$\bar u=\sum_{m_1,m_2,m_3}\frac{\Delta x^{2m_1}\Delta y^{2m_2}\Delta z^{2m_3}\,\partial_x^{2m_1}\partial_y^{2m_2}\partial_z^{2m_3}u}{(2m_1+1)!\,(2m_2+1)!\,(2m_3+1)!\,2^{2(m_1+m_2+m_3)}}$$
(Eq. (92)); order $2p$ needs the even derivatives of total order up to $2(p-1)$, and the unknown coefficients
of the class sums with offsets summing to at most $p-1$ solve a square linear system, there being as many
classes as derivative terms (Eq. (93)); the inverse follows by recursive inversion of the expansion, e.g.
$u_i=\bar u_i-\tfrac1{24}\Delta x^2\partial_x^2\bar u+\tfrac7{5760}\Delta x^4\partial_x^4\bar u+O(\Delta x^6)$ with
$\tfrac7{5760}=(\tfrac1{24})^2-\tfrac1{1920}$ (Eq. (90)). Up to tenth order only classes with $l=n$ or $l=0$ occur in 3-D (App. A.3). *(Compiler check, not in the
sources: the stencils are diamonds, not boxes; the 2-D formulas are not tensor products of the 1-D ones — the tensor product of the fourth-order 1-D formula
has centre weight $\tfrac{169}{144}$ and a corner term $\tfrac1{576}\bar u^{\Sigma11}$, against $\tfrac76$ and no corner
term — because terms of total degree above $2(p-1)$ are dropped. The fourth- and sixth-order 1-D formulas and
the fourth-order face formula were rechecked on monomials.)*

**Fourier symbol.** On $e^{\mathrm ik_wx}$ the cell average multiplies the point value by
$\frac{2\sin(k_w\Delta x/2)}{k_w\Delta x}$ in each averaged direction; Teissier et al. use this factor to set
Fourier initial data and forcing as consistent volume or staggered face averages (Eqs. (55), (76)–(77); printed
form under Qualifications).

## Use in a finite-volume scheme

McCorquodale & Colella and Buchmüller & Helzel, as recalled by Teissier et al. (§1, §3.2.2), turn the
reconstruction into a three-step **passage through point values**: a one-dimensional WENO reconstructs the face
*average* from cell averages; $\mathsf C_{2p}$ on the face turns the reconstructed face averages into face-centre
point values; a Riemann flux is evaluated on these; $\mathsf C^{-1}_{2p}$ turns the point fluxes back into
face-averaged fluxes. Only one reconstructed value per face is needed at any order, with no Gauss quadrature
over the face (§1, §3.7). Teissier et al. build on it dimension-by-dimension constrained-transport solvers
S2–S10 for compressible MHD (WENO of order $2p+1$, Rusanov flux on point values, order-$2p$ face-to-cell
interpolation of the staggered field, multidimensional Rusanov electric field, SSP integrators of matching
order), with viscous and resistive terms from exact averages of derivatives,
$\overline{\partial_xv}_i=(\bar v_{i+1/2}-\bar v_{i-1/2})/\Delta x$ (Eq. (52)), and pointwise cooling and forcing
through cell-average conversions ([constrained transport](/methods/constrained-transport.md),
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md),
[Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md), [SSP Runge–Kutta](/methods/ssp-runge-kutta.md)).

Berta et al. (2024) use the conversion the other way round: cell averages are turned into fourth-order point
values at cell centres, converted to primitive variables pointwise, and reconstructed to interfaces by
point-value interpolation formulas (a pointwise WENO-Z, MP5 or WENO3), with one Riemann problem per
interface and the transverse Laplacian for the flux average (§3.1–3.2, Eq. (30)).

## Evidence

- **Necessity.** On a 3-D MHD vortex advected one period, Teissier et al.'s S8 without the point-value passage
  (S8P) converges at second order, EOC 2.11, 1.97, 1.99, while its energy loss stays close to S8's, which the
  authors read as dispersive rather than dissipative errors (§4.1, Table 2;
  [magnetized vortex](/benchmarks/magnetized-vortex.md)).
- **Design orders.** With the passage, S4, S6, S8, S10 reach EOC 4.46, 6.12, 7.87, 9.74 at $192^3$ (errors
  $7.5\times10^{-5}$, $1.4\times10^{-6}$, $2.1\times10^{-8}$, $5.0\times10^{-10}$), with WENO weights $q=1$,
  $\epsilon=10^{-12}$, since the "typical choice" $q=2$, $\epsilon=10^{-6}$ "leads to a worse convergence for schemes
  of order strictly greater than 4" (Table 2; no table for the latter). Viscous and resistive Fourier-mode
  decay confirms orders 2–10 (§4.2, Fig. 11).
- **Cost.** Per step relative to S2: 1.3, 1.6, 2.2, 5.9 for S4–S10; to a fixed time, 1.3, 2.0, 3.5, 5.3
  ($512^3$, hardware not stated; Table 3). S6 at $96^3$ matches the energy loss of S4 at $192^3$ at about
  1.5 times S4's cost per cell to a fixed time, which the authors count as a gain "of order 10" (§4.1).
- **Near discontinuities.** Berta et al. (2024, §3.4, Eq. (33)) note that the correction "may easily produce
  unphysical values such as negative energies or densities" at discontinuities, and switch it off there with a
  shock flag, falling back to $u=\bar u$ ([troubled-cell indicators](/definitions/troubled-cell-indicator.md));
  Teissier et al. treat smooth subsonic flows only and leave shocks, flattening and positivity to future work
  (§1, §5).

## Qualifications

- The formulas are exact only on polynomial data and unlimited; neither source bounds them near steep
  gradients beyond the switch-off of Berta et al.
- Teissier et al. print every area-average factor in Eqs. (55), (76) and (77) as
  $(e^{\mathrm ik\Delta/2}-e^{\mathrm ik\Delta/2})$, with equal signs, which vanishes identically. *(Compiler check, not in the
  sources: the cell average of $e^{\mathrm ikx}$ over a width $\Delta$ is $(e^{\mathrm ik\Delta/2}-e^{-\mathrm ik\Delta/2})/(\mathrm ik\Delta)$, the
  only consistent reading.)*
- The version read of Teissier et al. is arXiv v2, with a different title and two of the three authors of the
  journal article; locators are those of the preprint.

# Citations

- [Teissier et al. (2024)](/sources/teissier-2024.md) — §1; §3.1–3.7, Eqs. (18)–(65); §4.1–4.2, Tables 2–3, Fig. 11; §5; App. A, Eqs. (83)–(120) (arXiv v2).
- [Berta et al. (2024)](/sources/berta-2024.md) — §3.1–3.2, Eqs. (16)–(30); §3.4, Eq. (33); App. A.
