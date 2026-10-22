---
type: Method
title: "Central WENO (CWENO)"
description: "Central WENO schemes subtract weighted low-order candidates from one central high-order polynomial and recombine them nonlinearly, so the linear weights may be any positive numbers summing to one and the result is a full polynomial on the cell; the page gives CWENO3, unstructured CWENO, WENO-ZQ in 2-D and its scale-invariant form on triangles, predictor-based weights, and costs."
status: established
aliases: [CWENO, central WENO, compact central WENO, CWENO3, WENO-ZQ, unstructured CWENO, CWENO implicit]
tags: [weno, cweno, reconstruction, finite-volume]
timestamp: 2026-10-22T20:00:00Z
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

## Position in the WENO family

- **Stability before accuracy.** Balsara et al. (2024, §I) place CWENO in a trend of scheme design
  that "has also begun to emphasize stability": CWENO schemes "emphasize the central, and most stable,
  stencil over and above all the other stencils". Fu (2023, §1) groups CWENO with WENO-AO and
  WENO-ZQ as alternatives "which emphasize more on numerical stability by introducing the
  unequal-size candidate stencils and the tailored weighting strategy".
- **Descendants.** [WENO-AO](/methods/weno-ao.md) hybridizes a large central stencil with an $r=3$
  WENO; WENO-ZQ, in Balsara et al.'s description (2024, §I), hybridizes a central stencil with an
  extrema-clipping van Albada limiter, and they claim for WENO-AO, against WENO-ZQ, that it preserves
  local extrema; Zheng et al. (2022) describe it instead by the lower-order polynomials above; [multi-resolution WENO](/methods/multi-resolution-weno.md) nests
  the subtraction level by level. The fifth-order multi-resolution scheme of Wang et al. (2021, Step 6,
  Eq. (3.21)) assembles its interface value "as in" WENO-ZQ, i.e. by this CWENO combination, with
  any positive linear weights.
- **Third order.** Deng (2023, §1) recalls third-order compact CWENO schemes and judges that their
  performance "is usually dependent on parameters in an ad hoc way"; his answer is the
  [ROUND](/methods/round-scheme.md) family.
- **Unstructured meshes.** Balsara et al. (2024, §I) recall extensions by Friedrichs, Käser & Iske and
  Dumbser & Käser; Tsoutsanis et al. (2021) is such an extension in the bundle.

## Relation to TENO

TENO also uses candidate stencils of unequal width, but it keeps or discards each stencil with a sharp
cut-off and renormalized linear weights; its incremental stencils make the linear combination "always
work" on uniform and non-uniform Cartesian meshes because each stencil contains the evaluation point,
whereas negative or non-existent linear weights appear on unstructured meshes (Fu 2023, §2.5;
[targeted ENO](/methods/targeted-eno.md)). The CWENO subtraction avoids the existence question
altogether, since the linear weights are free. Fu (2021, §1) cites CWENO, WENO-AO and WENO-ZQ as the
cognate unequal-stencil approaches when he introduces TENO-AA
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

# Citations

- [Puppo et al. (2023)](/sources/puppo-2023.md) — §3.1, Eqs. (5)–(13); §3.3.2, Eq. (21); §3.3.3.
- [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) — §1; §3.2, Eqs. (18)–(37); §4.1, Table 1; §4.2, Figs. 2–4; §4.3, Fig. 5.
- [Zheng et al. (2022)](/sources/zheng-2022.md) — §1; §2.2, Eqs. (8)–(16), Fig. 3.
- [Wang et al. (2021)](/sources/wang-2021.md) — §1; §3.1.1, Step 6, Eq. (3.21).
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §I.
- [Deng (2023)](/sources/deng-2023.md) — §1.
- [Fu (2023)](/sources/fu-2023.md) — §1; §2.5.
- [Fu (2021)](/sources/fu-2021.md) — §1.
- [Chen & Wu (2022)](/sources/chen-2022-b.md) — §1; §3.2, Eqs. (28)–(38), Lemmas 3.1–3.2, Remark 3.3; §4, Examples 4.1, 4.4–4.5, Tables 1–2, Figs. 6–9.
