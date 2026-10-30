---
type: Method
title: "Central WENO (CWENO)"
description: "Central WENO schemes subtract weighted low-order candidates from one central high-order polynomial and recombine them nonlinearly, so the linear weights may be any positive numbers summing to one and the result is a full polynomial on the cell; the page gives CWENO3, unstructured CWENO, WENO-ZQ and its scale-invariant form on triangles, CWENOZ as a DG limiter, predictor-based weights and costs."
status: established
aliases: [CWENO, central WENO, CWENOZ, compact central WENO, CWENO3, WENO-ZQ, unstructured CWENO, CWENO implicit, ALW-MR-WENO, adaptive linear weights]
tags: [weno, cweno, reconstruction, finite-volume]
timestamp: 2026-10-30T08:44:00Z
---

# Central WENO (CWENO)

Central WENO schemes (Levy, Puppo & Russo, with later work by Cravero, Semplice, Coco, Russo and
Visconti, as recalled by Balsara et al. 2024, §I, Fu 2021, §1, Deng 2023, §1 and Puppo et al. 2023,
§3.1) are WENO reconstructions in which the candidate set contains polynomials of **unequal degree**:
one high-order "optimal" polynomial $P_{\mathrm{opt}}$ on a central stencil carrying the design order,
and lower-degree polynomials $P_k$, $k\ge1$, on smaller stencils for shock capturing (page-local
symbols). The central candidate is defined by subtraction,

$$P_0=\frac1{d_0}\Big(P_{\mathrm{opt}}-\sum_{k\ge1}d_kP_k\Big),\qquad
P_{\mathrm{rec}}=\sum_{k\ge0}\omega_kP_k,$$

so that $P_{\mathrm{rec}}=P_{\mathrm{opt}}$ when $\omega_k=d_k$ (Puppo et al. 2023, Eqs. (7), (11);
Tsoutsanis et al. 2021, Eqs. (29)–(31); Zheng et al. 2022, Eq. (15)). Because the identity holds for
any $d_k$, "the optimal linear weights can be arbitrary positive numbers provided that the sum equals
one" (Fu 2021, §1; Fu 2023, §1; Zheng et al. 2022, §2.2). Deng (2023, §1) gives the consequence: the
linear weights do not depend on the stencil geometry, so CWENO extends more easily to non-uniform
grids. And because the output is a polynomial on the whole cell, not a value at one point, it can be
evaluated anywhere: uniform accuracy within the cell is the CWENO hallmark (Puppo et al. 2023, §3.1),
and Zheng et al. (2022, §1, §2.2) need exactly that for semi-Lagrangian remapping, for which they
judge [WENO-JS](/methods/weno-js-reconstruction.md), giving values "only at specific positions",
unsuitable.

## Third-order CWENO (CWENO3)

Puppo, Semplice & Visconti (2023, §3.1, Eqs. (5)–(13)) recall the Levy–Puppo–Russo scheme on the
three-cell stencil of a finite-volume scheme, with $X=x-x_i$ (page-local):

- $P_{\mathrm L}=\bar u_i+\frac{\bar u_i-\bar u_{i-1}}{\Delta x}X$, $P_{\mathrm R}=\bar u_i+\frac{\bar u_{i+1}-\bar u_i}{\Delta x}X$;
- $P_{\mathrm{opt}}=\mathsf a+\mathsf bX+\mathsf cX^2$ with
  $\mathsf a=\frac{-\bar u_{i+1}+26\bar u_i-\bar u_{i-1}}{24}$,
  $\mathsf b=\frac{\bar u_{i+1}-\bar u_{i-1}}{2\Delta x}$,
  $\mathsf c=\frac{\bar u_{i+1}-2\bar u_i+\bar u_{i-1}}{2\Delta x^2}$ (page-local coefficients);
- $P_0=(P_{\mathrm{opt}}-d_{\mathrm L}P_{\mathrm L}-d_{\mathrm R}P_{\mathrm R})/d_0$, $d_0+d_{\mathrm L}+d_{\mathrm R}=1$,
  $d_k\in(0,1)$;
- Jiang–Shu indicators $\beta_{\mathrm L}=(\bar u_i-\bar u_{i-1})^2$,
  $\beta_{\mathrm R}=(\bar u_{i+1}-\bar u_i)^2$, $\beta_0$ computed from the coefficients of
  $P_{\mathrm{opt}}$ ([smoothness indicators](/definitions/smoothness-indicator.md));
- $\alpha_k=d_k/(\epsilon+\beta_k)^q$ with $\epsilon=\Delta x^2$ and $q=2$, "always", following
  earlier CWENO papers (their refs. [9, 10, 27]).

If $d_k-\omega_k=O(\Delta x)$ the reconstruction is third order in the whole cell (Eq. (12)). The
values of $d_0,d_{\mathrm L},d_{\mathrm R}$ used in their tests are not stated.

**Predictor-based weights.** For implicit time stepping Puppo et al. (2023, §3.1, §3.3.2, Eq. (21))
compute the indicators, and hence the weights, on a first-order predictor instead of the unknown
solution. The boundary values then become linear functions of the cell averages with grid-varying
coefficients, $u^-_{i+1/2}=\sum_{\ell=-1}^1W^-_{i,\ell}\bar u_{i+\ell}$ (page-local $W$), so a DIRK
stage is nonlinear only through the flux, and linear for a linear law. This is the space reconstruction
of [Quinpi](/methods/quinpi.md), which also uses the CWENO template "in time" to blend a third-order
DIRK solution with the first-order predictor.

## Unstructured CWENO

Tsoutsanis, Adebayo, Merino, Arjona & Skote (2021, §3.2), after Tsoutsanis & Dumbser and Dumbser et
al., build arbitrary-order CWENO on mixed-element meshes:

- every polynomial is a constrained least-squares fit in a reference space (affine map of a
  decomposed tetrahedron or triangle), in a zero-mean Legendre basis that keeps the cell average
  exactly; the pseudo-inverse is precomputed once (Eqs. (18)–(28));
- the central stencil has $M=2K$ cells, $K$ the number of polynomial coefficients, built by a
  stencil-based compact algorithm; the small stencils are "Type3" directional stencils, one per
  element face, carrying **linear** ($r=1$) polynomials, whatever the central order (§3.2.1);
- $\alpha_s=d_s/(\epsilon+\beta_s)^q$ with $\epsilon=10^{-6}$ and $q=4$ (Eq. (32)), with
  multi-dimensional indicators written as precomputed quadratic forms (Eqs. (33)–(35));
- linear weights from an arbitrary non-normalized central weight $d_0'$ (page-local):
  $d_0=1-1/d_0'$, $d_s=(1-d_0)/(s_t-1)$ for the $s_t-1$ directional stencils (Eqs. (36)–(37)); the
  value of $d_0'$ is not given.

The gain over unstructured WENO, whose directional stencils carry the full order, comes from the low
degree and small size of the directional stencils (§1). On a multi-species advection test on triangles
CWENO and WENO have almost identical errors at orders 3–6 (e.g. 3rd order, 80 edges per side,
$L^\infty$ $2.487\times10^{-5}$ against $2.473\times10^{-5}$) and design orders (CWENO6 5.77/5.88),
and CWENO is said to need "approximately 60–80%" of the WENO time (§4.1, Table 1). At an isolated
material interface on a coarse mixed mesh CWENO3 is "significantly less oscillatory" than WENO3, which
the authors attribute to the more compact directional stencils (§4.2, Fig. 2), and on a gas–liquid
Riemann problem CWENO5 is less oscillatory than WENO3 (§4.3;
[gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md)). Reconstruction in
primitive variables is needed to keep pressure and velocity free of oscillations at interfaces with
variable $\gamma$ (§4.2, Figs. 3–4; [five-equation model](/definitions/five-equation-model.md),
[shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)).

**CWENOZ as a DG limiter.** Maltsev, Yuan, Jenkins, Skote & Tsoutsanis (2023, §2.2.2, Eqs. (18)–(28))
use the unstructured CWENOZ of Tsoutsanis & Dumbser (as they recall it) inside a hybrid
discontinuous Galerkin–finite-volume scheme in [UCNS3D](/software/ucns3d.md):

- the polynomials are least-squares fits in **physical space**, without the reference-space map of
  the authors' earlier work, in the same volume-normalized Taylor basis as the modal DG solution,
  with central stencils of $M=2K$ cells and a pre-stored pseudo-inverse (§2.2.1;
  [gradient reconstruction on unstructured meshes](/methods/unstructured-gradient-reconstruction.md));
- the directional "Type3" stencils carry linear polynomials, as in Tsoutsanis et al. (2021);
- the weights are of WENO-Z type,
  $$\alpha_s=d_s\Big(1+\frac{\tau}{\epsilon+\beta_s}\Big),\qquad
  \tau=\Big(\frac{1}{s_t-1}\sum_{s\ge1}|\beta_s-\beta_0|\Big)^{b},\qquad b=4,\ \epsilon=10^{-14}$$
  (page-local $\tau$, $b$; their central index 1 written 0 here), with indicators that are quadratic
  forms in the coefficients with a precomputed oscillation-indicator matrix;
- the central weight follows the same rule as above, $d_0=1-1/d_0'$, with $d_0'=10^7$; the authors
  state, citing Tsoutsanis & Dumbser, that any $d_0'>10^3$ gives the design order and that CWENOZ,
  unlike CWENO, is insensitive to the magnitude of the central weight (§2.2.2, §2.4).

In troubled cells the CWENOZ coefficients overwrite the higher DG modes, with the cell average kept
and the same order as the DG polynomial (DG($\mathbb P^N$)–FV(CWENOZ$(N+1)$)). On the isentropic vortex
pure CWENOZ of the same degree reaches the design order only on finer meshes than DG: on quadrilaterals
at $\mathbb P^4$ the $L^2$ error falls from $7.64\times10^{-2}$ to $7.20\times10^{-4}$ over 8 to 64 edges,
against $2.97\times10^{-4}$ to $1.14\times10^{-9}$ for DG (Table 1). With every cell forced to the
finite-volume branch the hybrid keeps the design order on smooth advection (3.01, 4.04, 4.99 for
$\mathbb P^2$–$\mathbb P^4$; Table B.4) ([WENO limiters for DG](/methods/weno-limiter-dg.md),
[troubled-cell indicators](/definitions/troubled-cell-indicator.md)). *(Compiler check, not in the
sources: the ratio $\tau/(\epsilon+\beta_s)$ is of degree $2b-2=6$ in the data, so these weights depend
strongly on its amplitude; see the homogeneity count on [WENO-Z](/methods/weno-z.md).)* Ji, Liang & Fu
(2022) use $d_0'=10^4$ and Jiang–Shu-type weights in the same code family (below).

## WENO-ZQ

WENO-ZQ (Zhu & Qiu) is the CWENO combination with WENO-Z-type weights. Zheng, Cai, Qiu & Qiu (2022,
§2.2, Eqs. (8)–(16)) build a new two-dimensional, cell-average, fourth-order version:

- $P_{\mathrm{opt}}$: a polynomial in a 13-dimensional orthogonal (Legendre-type) space matched to all
  13 cell averages of a diamond stencil, then projected onto $\mathbb P^3$;
- four $\mathbb P^1$ polynomials on the L-shaped triples
  $\{I_{i,j-1},I_{i-1,j},I_{i,j}\}$, $\{I_{i,j-1},I_{i,j},I_{i+1,j}\}$,
  $\{I_{i-1,j},I_{i,j},I_{i,j+1}\}$, $\{I_{i,j},I_{i+1,j},I_{i,j+1}\}$;
- $\tau=\big(\tfrac14\sum_{k=1}^4|\beta_0-\beta_k|\big)^2$ (page-local),
  $\alpha_k=d_k\big(1+\tau/(\beta_k+\epsilon)\big)$, $\epsilon=10^{-14}$, with $d_0=0.8$ and
  $d_{1,\dots,4}=0.05$ ([WENO-Z](/methods/weno-z.md));
- the constant coefficient of the result is the cell average, so the reconstruction is conservative
  (Eq. (16)).

The reconstruction "automatically decays to a lower order polynomial reconstruction" at
discontinuities, "a similar spirit with p-adaptive DG methods" (§1). It is the reconstruction of their
[semi-Lagrangian finite-volume scheme](/methods/semi-lagrangian-finite-volume.md), followed by a
[Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md) whose cell minimum is found
exactly.

**In finite differences.** Wan & Xia (2022, §2.3, Eqs. (2.24)–(2.30)) write the fifth-order
finite-difference WENO-ZQ, which they rename CWENOZ following Cravero, Semplice & Visconti, on the
point fluxes read as cell averages: the quartic $P_{\mathrm{opt}}$ on five cells, linear polynomials on
$\{I_{i-1},I_i\}$ and $\{I_i,I_{i+1}\}$, $(d_0,d_1,d_2)=(0.98,0.01,0.01)$,
$\tau=\big(\tfrac12(|\beta_0-\beta_1|+|\beta_0-\beta_2|)\big)^2$ (page-local) and
$\alpha_k=d_k\big(1+\tau/(\epsilon+\beta_k)\big)$, combined as above. Fan, Zhang & Qiu (2022, §5) use the
same WENO-ZQ5 with the same linear weights as one of three reconstructions of their positivity-preserving
Navier–Stokes scheme: it is less dissipative than WENO-JS5 and JS7 on the double rarefaction and the
Mach 10 reflection–diffraction problem and more oscillatory on the Leblanc problem, "possibly due to its
wider stencil" (Examples 5.2, 5.4, 5.8; [Leblanc shock tube](/benchmarks/leblanc-shock-tube.md)). The
finite-difference Hermite WENO of Fan, Zhao, Xiong & Qiu (2023) takes its weight form, which permits
arbitrary positive linear weights, from WENO-ZQ and uses it as comparator
([Hermite WENO](/methods/hermite-weno.md)).

**Steady states.** Wan & Xia (2022, §1) recall that Zhu & Shu's CWENO and multi-resolution steady
schemes converge much better than classical WENO, but "some oscillations may appear near
discontinuities because the schemes perform similarly to a linear scheme". In their tests CWENOZ
stalls on a shock reflection with the global Lax–Friedrichs speed (all schemes converge with
per-field speeds) and on fine-grid square columns, where enlarging the Lax–Friedrichs speed by 10 %
restores convergence, and it goes to negative pressure on a 3-D plate, which the linear weights
$(0.8,0.1,0.1)$ cure (Examples 4.4, 4.12–4.13, 4.15). Their WENO-H uses the CWENOZ stencils with $(0.8,0.1,0.1)$
and a modified weight in its non-smooth region ([hybrid schemes](/methods/hybrid-weno.md)).

**On triangles, with scale-invariant weights.** Chen & Wu (2022, §3.2.1) use the third-order
Zhu–Qiu reconstruction on unstructured triangles in a bound-preserving finite-volume scheme for
special-relativistic hydrodynamics ([relativistic hydrodynamics](/definitions/relativistic-hydrodynamics.md)):

- $P_{\mathrm{opt}}$ is a quadratic fitted by least squares on a 10-cell stencil (the target, its
  three face neighbours and two further neighbours of each), the $P_\ell$, $\ell=1,\dots,4$, are
  linear polynomials on a central and three sectorial 4-cell stencils, all in a zero-mean basis, and
  the combination is the CWENO one above (Eq. (28)), with $d_0=0.96$, $d_{1,\dots,4}=0.01$;
- the indicators are of Hu–Shu type and the global indicator is
  $\tau=\tfrac14\sum_{\ell=1}^4|\beta_0-\beta_\ell|=O(|K|^{3/2})$, $|K|$ the cell area (Eq. (33);
  the square of this $\tau$ is Zhu & Qiu's $\tau$);
- Zhu & Qiu's weights $\alpha_\ell=d_\ell\big(1+\tau^2/(\beta_\ell+\epsilon)\big)$ (Eq. (34)) are
  replaced by
  $$\alpha_\ell=d_\ell\Big(1+\frac{\tau^2}{(\beta_\ell+\epsilon)^2}\Big),\qquad \epsilon=|K_0|\max_{K\in N_0}\bar u_K^2,$$
  with $N_0$ the large stencil (Eq. (32)). Under $\bar u\mapsto\sigma\bar u$ (the scaling constant of
  [scale invariance](/properties/scale-invariance.md)) $\beta_\ell$, $\tau$ and $\epsilon$ all scale by $\sigma^2$, so the weights are invariant
  and the reconstruction is homogeneous of degree one (Lemma 3.1); in the original weights $\tau^2$
  scales as $\sigma^4$ against $\sigma^2$ (Remark 3.3). Third order is kept because
  $\tau^2/(\beta_\ell+\epsilon)^2=O(|K|)$ (Remark 3.3) ([scale invariance](/properties/scale-invariance.md));
- the reconstruction is done in local characteristic variables for each of the three edge normals
  and the three results are averaged with weights $|K_j|$ (Eq. (38); $|K|$ denotes the cell area, §2.2), then passed to a two-step scaling limiter ([Zhang–Shu limiter](/methods/zhang-shu-scaling-limiter.md),
  [bound preservation](/properties/bound-preservation.md)).

On a Riemann problem scaled by $\sigma=10^{-2}$ and $10^{-4}$ the difference between the scaled and
the unscaled density solutions is $O(10^{-12})$–$O(10^{-13})$ with the new weights and $O(10^{-1})$
and $O(10^{-2})$ with Zhu & Qiu's, which also overshoot (Example 4.4, Figs. 6–8); Zhu & Qiu's weights
also undershoot at the contacts of a multi-scale four-state problem (Example 4.5, Fig. 9). Third order
holds on the relativistic isentropic vortex ($l^1$ order 2.9971 at 238592 cells; Table 1). Chen & Wu
(§1) recall why the big-plus-small construction is used on triangles: Hu–Shu-type linear weights of
equal-order unstructured WENO depend on the quadrature and the topology and can be negative.
*(Compiler check, not in the sources: the Zheng, Cai, Qiu & Qiu weights above have the original
Zhu–Qiu form with an absolute $\epsilon=10^{-14}$, so Chen & Wu's scaling argument applies to them.)*

**Against unstructured TENO.** Ji, Liang & Fu (2022, §2.4) use the unstructured CWENO of the same
code family as comparator: a large central-biased stencil with the target-order polynomial, third-order
(quadratic) directional polynomials, where Tsoutsanis et al. (2021) use linear ones, Jiang–Shu-type weights with exponent 4 and $\epsilon=10^{-14}$, and
$d_0=1-1/d_0'$ with $d_0'=10^4$ for all orders. Larger $d_0'$ ($10^7$, $10^{15}$, values allowed in earlier
work) resolve the Shu–Osher waves better but lose robustness, and double Mach reflection "typically
fails" with too large a value (§5.5, Fig. 11; the failures are not shown). At equal order CWENO is the most
dissipative of the three on double Mach reflection, TENO the least, equal-order unstructured WENO in
between, at the same cost as TENO (e.g. 1.98 against 1.96 μs per element per iteration at fifth order; §5.8, §5.10,
Table 7) ([targeted ENO](/methods/targeted-eno.md), [UCNS3D](/software/ucns3d.md)). They also state
that CWENO is cheaper than equal-order WENO and that its compact small stencils make a smooth candidate
near shocks more likely (§2.4).

Ji, Liang & Fu (2023, §3.1.2, Eqs. (23)–(28)) keep the same comparator for their dual-cut-off TENO of orders 4 to 7:
$\alpha_k=d_k/(\beta_k+\epsilon)^4$, $\epsilon=10^{-14}$, $d_0=1-1/d_0'$ with $d_0'=10^4$ and the remaining weight shared
equally by the directional stencils, and reference-space indicators summed over derivative orders 1 to the degree, without
a mesh-size factor (Eq. (26); [smoothness indicators](/definitions/smoothness-indicator.md)). Their TENO-D uses the same
candidate arrangement, one large central-biased stencil and small directional ones, but returns the large-stencil polynomial
exactly when its stencil passes the cut-off, whereas CWENO recovers it only asymptotically, $\omega_k\approx d_k$ (§3.2.2,
§3.3). They argue that CWENO's smooth weighting activates the nonlinear adaptation "in the low-wavenumber ranges", with
excess dissipation for multiscale flows, and call its choice of $d_k$ "rather ad hoc" against TENO's cut-offs, which
"function in the spectral space" (§3.1.2, §3.3); these are statements, not measurements. At equal order TENO6-D and TENO7-D
resolve the [Shu–Osher](/benchmarks/shu-osher-problem.md) waves "much better" than CWENO6 and CWENO7 and show "much lower
numerical dissipation" on [double Mach reflection](/benchmarks/double-mach-reflection.md) and the
[triple-point problem](/benchmarks/triple-point-problem.md) (§4.4, §4.5, §4.8, figure comparisons). The wall times are
"approximately the same": on Shu–Osher ($h\approx1/20$) 173.12 s and 211.01 s for CWENO6 and CWENO7 against 164.26 s and
196.57 s for TENO6-D and TENO7-D, on double Mach reflection ($h\approx1/125$) 2517.38 s and 3050.80 s against 2694.45 s
and 3126.84 s (Tables 6–7; hardware not stated). *(Compiler check, not in the sources: the TENO-D to CWENO ratios are 0.95
and 0.93 in Table 6, 1.07 and 1.02 in Table 7.)* On the explosion problems and the 3-D spherical explosion TENO-D and
CWENO of equal order agree with the references (§4.3, §4.9;
[explosion and implosion problems](/benchmarks/explosion-and-implosion-problems.md)).

**Two stencils and adaptive linear weights on triangles.** Lin & Zhu (2024) reduce the CWENO combination
on triangular meshes to two central stencils of unequal size: the target cell alone, with the constant
$q_1=\bar u_0$, and one big stencil of at least 6, 10 or 15 cells (8, 12 and 20 listed, extended by edge
neighbours when too few distinct cells remain) carrying a quadratic, cubic or quartic constrained
least-squares fit that keeps the target average exactly, after Hu & Shu (§2, Steps 1.1–1.3, Eqs. (2.5)–(2.7);
page-local $q_1$, $q_\ell$). The high-order polynomial is rewritten "with similar ideas for classical CWENO
schemes" as $p_\ell=q_\ell/d_\ell-(d_1/d_\ell)\,p_1$ with $d_1+d_\ell=1$ (Eqs. (2.8)–(2.10)), weighted by WENO-Z-type
weights $d_k\big(1+\tau/(\epsilon+\beta_k)\big)$, $\tau=|\beta_\ell-\beta_1|^2$, $\epsilon=10^{-10}$, exponent 1 on the
ratio (Eqs. (2.12)–(2.13); [WENO-Z](/methods/weno-z.md)); the indicator $\beta_1$ of the constant is deferred to the
authors' earlier triangular [multi-resolution WENO](/methods/multi-resolution-weno.md). The new element is an *a
posteriori* adaptation of the linear weights inside each cell: the unnormalized high-order weight starts at
$10^8$ (low-order weight 1), and while the tentative reconstruction at a boundary Gauss point deviates from
$\bar u_0$ by more than $\max(\Phi_1,\Phi_2)$, $\Phi_1$ the minimum circumradius of the cell and its edge
neighbours times $\min|\bar u|$ over them and $\Phi_2=\min_j|\bar u_0-\bar u_j|$ ("Condition I", called an
improvement of the KXRCF indicator), the weight is divided by 100 and the weights recomputed, as long as it
exceeds $10^{n_G}$, $n_G=2$ or 3 the Gauss points per edge (Steps 4.3–4.4, Eq. (2.15); page-local $\Phi_1$,
$\Phi_2$, $n_G$; [troubled-cell indicators](/definitions/troubled-cell-indicator.md)). *(Compiler check, not in the
sources: from $10^8$ the sequence $10^6,10^4,10^2$ stops after at most three reductions for $n_G=2$ and 3, so
the normalized high-order linear weight never falls below $100/101$; for any admissible weights the linear
combination returns $q_\ell$ exactly, which is why they are free.)* The schemes (ALW-MR-WENO-3, 4, 5) use the
Lax–Friedrichs flux at Gauss points, characteristic reconstruction for Euler and TVD-RK3 at CFL 0.6. They
reach finest-mesh $L^1$ orders 2.84, 4.41, 4.88 on 2-D [Burgers](/benchmarks/burgers-equation-tests.md) and 3.03,
4.32, 5.10 on the Euler [density wave](/benchmarks/density-wave-advection.md), with errors equal to those of the
multi-resolution WENO on the two finest meshes (Tables 3.2–3.3), and take 0.60–0.96 of its CPU time on the shock
tests, the largest saving at fifth order (Table 3.1; no hardware stated). Results on shock tubes,
[Shu–Osher](/benchmarks/shu-osher-problem.md), [blast waves](/benchmarks/woodward-colella-blast-wave.md),
[Schardin's problem](/benchmarks/shock-diffraction.md), [double Mach reflection](/benchmarks/double-mach-reflection.md),
the [forward-facing step](/benchmarks/forward-facing-step.md) and NACA0012 flows are "comparable" to those of the
multi-resolution scheme by figure. The authors claim "the first time that any high-order WENO schemes with the
application of only two unequal-sized stencils are obtained on triangular meshes" (Abstract). *(Compiler check, not in the
sources: the unstructured CWENO above combines a central stencil with several directional ones, so the claim
rests on the count "only two".)*

## Position in the WENO family

- **Stability before accuracy.** Balsara et al. (2024, §I) place CWENO in a trend of scheme design
  that "has also begun to emphasize stability": CWENO schemes "emphasize the central, and most stable,
  stencil over and above all the other stencils". Balsara, Samantaray & Subramanian (2023, §6.3) recall CWENO and WENO-ZQ as combining
  piecewise-linear small stencils with one large central stencil, against which WENO-AO's third-order
  small stencils "retain the prospect that local extrema could be somewhat represented"; Liang et al.
  (2022, §1) credit CWENO with "stronger numerical robustness". Fu (2023, §1) groups CWENO with WENO-AO and
  WENO-ZQ as alternatives "which emphasize more on numerical stability by introducing the
  unequal-size candidate stencils and the tailored weighting strategy".
- **Descendants.** [WENO-AO](/methods/weno-ao.md) hybridizes a large central stencil with an $r=3$
  WENO; WENO-ZQ, in Balsara et al.'s description (2024, §I), hybridizes a central stencil with an
  extrema-clipping van Albada limiter, and they claim for WENO-AO, against WENO-ZQ, that it preserves
  local extrema; Zheng et al. (2022) describe it instead by the lower-order polynomials above; [multi-resolution WENO](/methods/multi-resolution-weno.md) nests
  the subtraction level by level. The fifth-order multi-resolution scheme of Wang et al. (2021, Step 6,
  Eq. (3.21)) assembles its interface value "as in" WENO-ZQ, i.e. by this CWENO combination, with
  any positive linear weights. Wang, Zhu, Wang & Zhao (2023c, Eqs. (3.17)–(3.18)) state the same
  Levy–Puppo–Russo decomposition for their multi-resolution WCNS interpolation, and Gu, Li, Cheng & Shu
  (2023, §2.4) use the same subtraction, after Zhu & Shu, in a third-order two-level reconstruction on
  moving quadrilaterals, whose linear weights need not change with the cell shapes.
- **Third order.** Deng (2023, §1) recalls third-order compact CWENO schemes and judges that their
  performance "is usually dependent on parameters in an ad hoc way"; Deng's answer is the
  [ROUND](/methods/round-scheme.md) family.
- **Unstructured meshes.** Balsara et al. (2024, §I) recall extensions by Friedrichs, Käser & Iske and
  Dumbser & Käser; Tsoutsanis et al. (2021) is such an extension in the bundle.

## "Central WENO" in Shu's review

[Shu (2009a)](/sources/shu-2009.md) uses the name in an older and partly different sense. In §3.5.5
"central schemes" are finite-volume schemes defined on a **staggered mesh** in the Nessyahu–Tadmor
framework, whose advantage is that "the numerical flux is computed in the smooth part of the
reconstructed function, hence there is no need to use explicitly a monotone flux for the scalar case or
a Riemann solver for the system case"; WENO schemes "based on the central scheme framework" are
those of Levy, Puppo & Russo and of Qiu & Shu (Shu's refs. [92, 93, 94, 131]). Shu reports that this
framework "allows the componentwise WENO reconstruction procedure to be used for less oscillatory
results for third or even fourth order schemes", while "for very high order central WENO schemes,
characteristic WENO reconstruction is still necessary to obtain stable results"
([characteristic decomposition](/methods/characteristic-decomposition.md)). The link with the
construction on this page is the treatment of linear weights (§2.3.3; [negative linear weights](/methods/negative-linear-weights.md)): where accuracy fixes them
uniquely they may be negative, and "if the usual WENO procedure is used without modification,
oscillations and instability may appear"; one remedy is the splitting technique of Shi, Hu & Shu,
used for the central WENO of Qiu & Shu, the other is to lower the accuracy demanded of the linear
combination so that the weights become free, at the cost of "a lower order accuracy than the
'authentic' WENO schemes" with the same large stencil, which is how Levy, Puppo & Russo build their
central WENO (Shu's ref. [92]). Shu also recalls (§2.3.1) the result of Carlini, Ferretti & Russo that the
large-stencil interpolant is a combination of the candidate interpolants with *polynomial*,
position-dependent linear weights, non-negative on the interval common to all candidates. The review
predates the CWENOZ and unstructured variants above.

## Relation to TENO

TENO also uses candidate stencils of unequal width, but it keeps or discards each stencil with a sharp
cut-off and renormalized linear weights; its incremental stencils make the linear combination "always
work" on uniform and non-uniform Cartesian meshes because each stencil contains the evaluation point,
whereas negative or non-existent linear weights appear on unstructured meshes (Fu 2023, §2.5;
[targeted ENO](/methods/targeted-eno.md)). The CWENO subtraction avoids the existence question
altogether, since the linear weights are free. Fu (2021, §1) cites CWENO, WENO-AO and WENO-ZQ as the
cognate unequal-stencil approaches when introducing TENO-AA
([adaptive TENO](/methods/adaptive-teno.md)).

## Qualifications

- **Cost ratio.** The "approximately 60–80%" of Tsoutsanis et al. (2021, §4.1) does not cover their
  own Table 1: the printed CWENO/WENO time ratios range from 0.547 (6th order) to 0.941 (3rd order)
  *(compiler check, not in the sources: ratios of the printed normalized times)*; at 80 edges per side they are 0.84 (3rd),
  0.82 (4th), 0.64 (5th) and 0.62 (6th).
- Tsoutsanis et al. (2021) print the weight numerator as $\lambda_m$ in Eq. (32) while the rest of the
  section indexes by $s$, and their Eq. (23) for $K$ counts the constant coefficient that Eqs.
  (25)–(28) exclude; neither changes the method.
- Tsoutsanis et al. (2021, §4.2) state that reconstruction in conservative or characteristic variables
  oscillates at interfaces with variable $\gamma$, citing earlier work; they test conservative and
  primitive variables only, not characteristic ones
  ([characteristic decomposition](/methods/characteristic-decomposition.md)).
- Zheng et al. (2022, Eq. (12)) print the indicator sums from order zero; see
  [smoothness indicators](/definitions/smoothness-indicator.md). The name WENO-ZQ refers to Zhu and
  Qiu, not to the WENO-Z of Borges et al.
- Puppo et al. (2023, Eq. (7)) print $C(x-x_j^2)$ for $C(x-x_j)^2$ in the central polynomial.
- Maltsev et al. (2023) write "$\lambda_1=10^7$" in the tests for the non-normalized central weight
  $d_0'$ of their Eq. (24), and attribute the two NAD margins of their troubled-cell indicator to
  different references in §2.5 and App. C.

# Citations

- [Puppo et al. (2023)](/sources/puppo-2023.md) — §3.1, Eqs. (5)–(13); §3.3.2, Eq. (21); §3.3.3.
- [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) — §1; §3.2, Eqs. (18)–(37); §4.1, Table 1; §4.2, Figs. 2–4; §4.3, Fig. 5.
- [Zheng et al. (2022)](/sources/zheng-2022.md) — §1; §2.2, Eqs. (8)–(16), Fig. 3.
- [Wang et al. (2021)](/sources/wang-2021.md) — §1; §3.1.1, Step 6, Eq. (3.21).
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §I.
- [Deng (2023)](/sources/deng-2023.md) — §1.
- [Shu (2009a)](/sources/shu-2009.md) — §2.3.1; §2.3.3; §3.5.5: central (staggered) WENO, negative linear weights and the lowered-accuracy remedy, position-dependent linear weights.
- [Fu (2023)](/sources/fu-2023.md) — §1; §2.5.
- [Fu (2021)](/sources/fu-2021.md) — §1.
- [Chen & Wu (2022)](/sources/chen-2022-b.md) — §1; §3.2, Eqs. (28)–(38), Lemmas 3.1–3.2, Remark 3.3; §4, Examples 4.1, 4.4–4.5, Tables 1–2, Figs. 6–9.
- [Wan & Xia (2022)](/sources/wan-2022.md) — §1; §2.3, Eqs. (2.24)–(2.30); §4, Examples 4.4, 4.12–4.13, 4.15.
- [Fan, Zhang & Qiu (2022)](/sources/fan-2022.md) — §5, Examples 5.2, 5.4, 5.8.
- [Ji, Liang & Fu (2022)](/sources/ji-2022.md) — §2.4, Eqs. (18)–(22); §5.5, Fig. 11; §5.8; §5.10, Table 7.
- [Balsara, Samantaray & Subramanian (2023)](/sources/balsara-2023.md) — §6.3.
- [Liang et al. (2022)](/sources/liang-2022.md) — §1.
- [Maltsev et al. (2023)](/sources/maltsev-2023.md) — §2.2, Eqs. (10)–(28); §2.4; §3.1, Table 1; App. B, Table B.4.
- [Wang et al. (2023c)](/sources/wang-2023-c.md) — §3, Eqs. (3.17)–(3.18).
- [Gu et al. (2023)](/sources/gu-2023.md) — §2.4.
- [Ji, Liang & Fu (2023)](/sources/ji-2023.md) — §3.1.2, Eqs. (23)–(28); §3.2.2; §3.3; §4.3–4.5, §4.8–4.9, Tables 6–7.
- [Lin & Zhu (2024)](/sources/lin-2024-b.md) — Abstract; §1; §2, Steps 1–6, Eqs. (2.2)–(2.17); §3, Tables 3.1–3.3, Cases 3.1–3.11.
