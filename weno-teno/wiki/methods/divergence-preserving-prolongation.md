---
type: Method
title: "Divergence-preserving prolongation and reconstruction for AMR"
description: "Prolongation of a face-collocated vector field with a divergence constraint onto newly refined zones of an adaptive mesh, so that every fine zone satisfies the constraint to round-off; the page gives Balsara et al.'s analytically exact fourth-order reconstruction, the WENO-ADP face interpolation with its least-squares touch-up (WENO-ADPT), the counts of the constrained problem, and the verification."
status: established
aliases: [divergence-free prolongation, divergence-preserving prolongation, constraint-preserving prolongation, WENO-ADP, WENO-ADPT, almost divergence-preserving WENO, divergence-preserving reconstruction, divergence-free reconstruction]
tags: [mhd, weno, reconstruction, finite-volume]
timestamp: 2026-10-24T06:00:00Z
---

# Divergence-preserving prolongation and reconstruction for AMR

On a block-structured [adaptive mesh](/methods/adaptive-mesh-refinement.md),
**prolongation** transfers the solution from a coarse zone to the fine
zones that replace it. For a vector field whose normal components live
on zone faces and obey a divergence constraint, the transfer must also
satisfy the constraint on every new fine zone, or the
[constrained-transport](/properties/divergence-free-magnetic-field.md)
update that follows inherits a divergence error it cannot remove.
[Balsara, Samantaray & Subramanian (2023)](/sources/balsara-2023.md)
treat the magnetic induction of MHD, $\nabla\cdot B=0$, and the electric
displacement of electrodynamics, $\nabla\cdot D=\rho_{\mathrm q}$, with
one formalism; Balsara (2001) solved the problem at second order (as
recalled). The page writes the constrained field as $D$ and its source
as $\rho_{\mathrm q}$ ($D$, $\rho_{\mathrm q}$ page-local; $B$ is the case
$\rho_{\mathrm q}=0$).

## The problem

Fine faces that overlie a coarse face keep the coarse facial data, so
the normal component stays continuous across coarse faces; only the new
internal fine faces are free (§1). A coarse zone that abuts an existing
fine mesh must also retain all moments of the abutting fine faces: their
means at second order, and, when the fine scheme is high order, a mean
and two linear moments on each of the four fine faces, twelve values on
a coarse face (§1–§2, Fig. 2). The constraint is written for
area-integrated face fluxes and volume-integrated charges, so the
constructions below hold unchanged for non-uniform subdivisions and
curved zone boundaries, provided the fluxes are computed accurately
(§4; stated).

## Analytically exact fourth-order reconstruction

Balsara et al. (§2, Eqs. (2)–(10); Supplement B) build, inside each coarse
zone of the reference cube $[-\frac12,\frac12]^3$, three polynomials for
$D_1,D_2,D_3$ in a basis of Legendre-polynomial products
($1$, $x$, $x^2-\frac1{12}$, $x^3-\frac{3x}{20}$,
$x^4-\frac{3x^2}{14}+\frac3{560}$) that

- match all facial moments of the six faces, twelve per face (Eqs. (2)–(4):
  the ten moments of a fourth-order facial reconstruction plus two extra
  ones, needed to hold the mean and two linear moments of four fine
  faces);
- satisfy $\nabla\cdot D=\rho_{\mathrm q}$ at all orders of the polynomial
  expansion, with the fourth-order charge polynomial obtained by
  finite-volume WENO from zone averages (Eq. (6)); this needs terms
  borrowed from fifth and sixth order;
- minimize the quadratic energy of the field.

The zone's own faces do not fix some cross coefficients; a WENO step over
the facial values of the neighbouring zones in the normal direction sets
them, and the rest follow from a stack of explicit formulas. The facial
moments of a coarse face are recovered from the four abutting fine faces
by inverting a $12\times12$ system, printed in closed form (Eq. (7)). The
earlier constraint-preserving formulation of Balsara et al. (2018) "was not
general enough" for this problem, because it cannot carry twelve facial
moments (§2). Going analytically beyond fourth order is "very
challenging" (§1, §10). The coefficient stack (Supplement B) and the
finite-volume WENO with perfect-square indicators (Supplement A) are not
in the article's PDF, so the method cannot be reproduced from the
article alone.

## WENO-ADP: face-matching WENO interpolation

The second route (§3) is one-dimensional in each normal direction and
reaches orders 3, 4 and 5. For each transverse facial moment of $D_1$ it
builds the variation in $x_1$ by **interpolating the facial point values**
on the two zone faces and the faces one to three zones out, at
$x=\pm\frac12,\pm\frac32,\pm\frac52,\pm\frac72$ (Fig. 4). With $n_{\mathrm f}$
facial values per candidate stencil ($n_{\mathrm f}=3,4,5$, page-local),
there are $n_{\mathrm f}-1$ candidate stencils, each containing both zone
faces; every candidate polynomial $P_k$ (registry §10) therefore matches
$D_1$ at $x=\pm\frac12$, and so does any convex combination of them, so
the nonlinear hybridization keeps the facial values exactly (§3.1). Each
candidate has the full design order, so the nonlinear weights serve only
non-oscillation, not order enhancement. The highest transverse moments
are interpolated linearly between the two faces; lower moments use the
lower-order WENO-ADP in turn. At third order, for example,
$$P_0(x)=\tfrac1{12}\big(8D^-_0-D^{-2}_0+5D^+_0\big)+\big(D^+_0-D^-_0\big)x+\tfrac12\big(D^{-2}_0-2D^-_0+D^+_0\big)\big(x^2-\tfrac1{12}\big)$$
on the stencil of the two zone faces and the next face on the left
(Eq. (15); page-local $D^\pm_0$ the zone-face means, $D^{-2}_0$ the face
one zone to the left), and the [smoothness indicators](/definitions/smoothness-indicator.md)
are sums of perfect squares in the Legendre coefficients, e.g.
$\beta_k=(p_1)^2+\frac{13}3(p_2)^2$ at third order and
$$\beta_k=\big(p_1+\tfrac{p_3}{10}\big)^2+\tfrac{13}3p_2^2+\tfrac{781}{20}p_3^2$$
at fourth order, with $p_m$ the coefficient of the $m$-th Legendre term
of $P_k$ (Eqs. (17), (23); page-local $p_m$). The coefficients of Eqs.
(15)–(16), (20)–(22) and (26)–(29) and the indicators of Eqs. (17), (23)
and (30) follow from exact interpolation and from the Jiang–Shu integral
$\sum_{l\ge1}\int(d^lP/dx^l)^2$ on the unit interval *(compiler check,
not in the sources)*. The linear weights, the nonlinear weight formula and
its constants are not stated in the main text.

The interpolated field is not divergence-preserving: matching two
opposing faces moment by moment introduces cross terms (two extra terms
at second order, three at third, four at fourth, five at fifth, §3).
The divergence error is observed to converge at one order below the
design order (Tables 4, 6, 8, 10; e.g. fifth-order divergence orders
3.79, 3.75, 4.00, 4.01), hence "almost divergence-preserving"; this is
not proved.

## WENO-ADPT: the least-squares touch-up

The touch-up (§4–§5) keeps the fluxes on fine faces that overlie coarse
faces, takes the WENO-ADP fluxes $\Phi^{\mathrm{FV}}$ on the internal fine
faces as targets, and corrects them to fluxes $\Phi^{\mathrm c}$ that
satisfy the integrated constraint in every fine zone,
$\sum_{\text{faces}}\pm\Phi=\mathcal Q_k$, with $\mathcal Q_k$ the volume
integral of the prolonged charge over fine zone $k$ (page-local $\Phi$,
$\mathcal Q_k$), minimizing $\sum(\Phi^{\mathrm c}-\Phi^{\mathrm{FV}})^2$.

- **Ratio 2, 2D** (Eqs. (31)–(36)): four internal fluxes and four zone
  constraints of which three are independent, since their sum is the
  coarse-zone identity; one free parameter remains, with a closed-form
  least-squares optimum.
- **Ratio 2, 3D** (Eqs. (37)–(42)): twelve internal fluxes, eight fine
  zones and seven independent constraints, hence five free parameters,
  each with a closed-form optimum of denominator 24.
- **Ratio $\mathsf r>2$** (§5, Table 1; page-local $\mathsf r$): a
  constrained least-squares problem solved through its KKT matrix. With
  $3(\mathsf r^3-\mathsf r^2)$ new facial variables, $\mathsf r^3-1$
  independent constraints and $2\mathsf r^3-3\mathsf r^2+1$ free
  parameters, the free-to-new ratio is $5/12$, $28/54$, $81/144$ for
  $\mathsf r=2,3,4$ and tends to $2/3$, offered as the reason the touch-up
  can stay close to the WENO-ADP fluxes. With a fixed ratio and uniform
  fine zones the KKT matrix is assembled and inverted once per level,
  leaving a small matrix–vector product per zone (stated).

The closed-form solutions of Eqs. (34), (36) and (40)–(42) follow from
the constraints and the quadratic objective *(compiler check, not in the
sources; one printed symbol slip below)*.

## Verification

On analytic fields (§8, Eqs. (53)–(54)), $D=\nabla\times\mathcal A$ for a
trigonometric vector potential $\mathcal A$ (registry §10, MHD) (divergence-free) and a field with
$\rho_{\mathrm q}=\nabla\cdot D\neq0$ (divergence-preserving), coarse
meshes $8^3$ to $128^3$ (ratio 2) or $6^3$ to $96^3$ (ratio 3), errors
measured on the internal fine faces only:

| Construction | Field error | Fine-zone divergence |
|---|---|---|
| exact fourth order (Table 2) | $L^1$ orders 2.91, 3.87, 4.63, 5.07 | $10^{-12}$ (up to $9.5\times10^{-10}$ at $8^3$) |
| WENO-ADP, fifth order (Table 4) | $L^1$ orders 5.71, 5.53, 5.19, 5.05 | converges at order about 4 |
| WENO-ADPT, fifth order (Table 5) | $L^1$ $4.5\times10^{-2}$ to $1.1\times10^{-8}$, orders 5.66–5.19 | $\le1.4\times10^{-13}$ |
| WENO-ADPT, ratio 3 (Tables 9, 11) | fifth-order $L^1$ orders 6.05–5.29 | $10^{-15}$–$4\times10^{-13}$ |

The touch-up slightly lowers the field error compared with WENO-ADP
(Tables 4–7). At fourth order the exact reconstruction has the smaller
error on very coarse meshes, one reconstruction step against several,
while WENO-ADPT keeps the constraint better, $10^{-15}$–$10^{-14}$
against $10^{-12}$–$10^{-10}$, because the round-off of the long
coefficient stack accumulates (§8.3–8.4). In a time-dependent 2D Maxwell
test with a static refined patch the composite scheme reaches design
orders 2, 3 and 4 and keeps the undivided divergence at
$10^{-14}$–$10^{-12}$ ([adaptive mesh refinement](/methods/adaptive-mesh-refinement.md),
§9).

## Qualifications

- **Smoothness indicators.** Balsara et al. state that finite-volume WENO
  smoothness indicators on Cartesian meshes can be written as sums of
  perfect squares in a Legendre basis, which "has never been documented in
  the literature before" (§1, §6.3, §10); the derivation is in
  Supplement A, which is not in the PDF. They credit the
  finite-difference analogue to Balsara et al. (2016), the
  [WENO-AO](/methods/weno-ao.md) paper, citing it as ref. [6] in §6.3 and
  §10 but as ref. [5] (a 2015 divergence-free MHD paper) in §1.
- **Printed slips.** Eq. (36) prints its last terms as
  "$2\phi_1-\phi_2+\phi_3$"; solving Eqs. (32)–(35) gives
  $2\mathcal Q_1-\mathcal Q_2+\mathcal Q_3$ there *(compiler check, not in
  the sources)*. §4.2 refers to Eq. (30), the fifth-order indicator, for
  the parametrized solution, which is Eq. (40). §3.3 calls the
  fifth-order candidate "cubic"; Eq. (25) is quartic.
- **Unverifiable coefficients.** The fine-face moments of Eq. (7) are not
  defined in the main text; several of its printed coefficients could not
  be reproduced with natural definitions, so they are recorded as
  unverifiable, not as wrong.
- The irregular third-order divergence orders at ratio 3 (Table 8: 2.28,
  1.89, 1.71, 2.23) are not discussed.

# Citations

- [Balsara, Samantaray & Subramanian (2023)](/sources/balsara-2023.md) — §1; §2, Eqs. (1)–(10); §3, Eqs. (11)–(30); §4, Eqs. (31)–(42); §5, Table 1; §6; §8, Eqs. (53)–(54), Tables 2–12; §9; §10.
