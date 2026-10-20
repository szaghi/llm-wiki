---
type: Source
title: "Micalizzi & Torlo (2024) — A New Efficient Explicit Deferred Correction Framework: Analysis and Applications to Hyperbolic PDEs and Adaptivity"
description: "Makes explicit deferred correction cheaper by starting from two subtimenodes and adding one per iteration through interpolation of the solution or of the right-hand side, gives the Butcher tableaux and stage counts of the new families, proves that bDeC-type methods of order K have the Taylor stability polynomial, and adds an order-adaptive variant and mass-matrix-free continuous Galerkin applications."
resource: "doi:10.1007/s42967-023-00294-6"
source_kind: paper
authors: [Micalizzi L., Torlo D.]
year: 2024
venue: "Commun. Appl. Math. Comput. 6:1629-1664"
local_file: "/home/stefano/papers/mosaic/ode-integration/2023_Crossref_Communications_on_Applied_Mathematics_and_Computation_Micalizzi_A_New_Efficient_Explicit_Deferred_Correction_Framework_Analy.pdf"
tags: [deferred-correction, explicit, runge-kutta, stability, method-of-lines]
timestamp: 2026-10-20T10:00:00Z
---

# Summary

The paper starts from explicit [deferred correction](/methods/deferred-correction.md) (DeC)
in Abgrall's two-operator form: a low-order explicit operator $\mathcal L^1$, a high-order
implicit operator $\mathcal L^2$, and $K$ iterations each gaining one order. Standard DeC
uses all $\mathsf M+1$ subnodes $t_{n,m}$ from the first iteration on, although iteration $k$
is only $k$-th order accurate. The authors start with the two subnodes $t_n$, $t_{n+1}$ and
add one per iteration, linking iterations by Lagrange interpolation, so that the node count
follows the order reached. This "ladder" idea had been used in implicit SDC but, they say,
never analysed for explicit DeC.

Two families result for the one-parameter αDeC family ($\alpha=0$: bDeC, integration over
$[t_{n,0},t_{n,m}]$; $\alpha=1$: sDeC, over $[t_{n,m-1},t_{n,m}]$, equivalent to the
Dutt–Greengard–Rokhlin spectral DeC): αDeCu interpolates the solution between iterations,
αDeCdu the right-hand side. The paper writes all variants as explicit Runge–Kutta tableaux
and counts their stages. The theoretical speed-ups reach 1.835 (bDeCdu, order 13,
equispaced nodes). Theorem 6.1 shows that every bDeC, bDeCu and bDeCdu method of order $K$
has the [stability polynomial](/definitions/stability-function.md) $\sum_{j=0}^Kz^j/j!$,
whatever the subnodes. Theorem 6.2 shows that αDeCu and αDeCdu coincide on linear problems.

Two applications follow. Abgrall's mass-matrix-free DeC for continuous Galerkin
discretizations of hyperbolic PDEs gets an interpolated variant. An order-adaptive DeC keeps
adding subnodes until the endpoint value stops changing, a fixed-step alternative to
[step-size control](/methods/step-size-control.md). The tests are two ODEs, the 1D
[linear advection equation](/benchmarks/linear-advection-equation.md) with several
continuous finite elements, and a 2D shallow-water vortex. The new bDeC variants dominate the
error-versus-CPU-time Pareto front, with measured speed-ups of about 2 (ODE, order 9) and up
to about 1.8 (PDE). The supplement shows that Abgrall's continuous Galerkin DeC is only
second order with cubic Bernstein and Lagrange elements on unsteady problems unless many more
iterations are run. The paper cites [DeC–ADER equivalence](/results/dec-ader-equivalence.md)
and [ADER](/methods/ader-time-integration.md) for future work, and the structure-preserving
DeC variants ([positivity](/properties/positivity-preservation.md), relaxation) and the
[SSP](/methods/strong-stability-preserving-runge-kutta.md) origin of bDeC only in passing.

# Version read

arXiv:2210.02976v4 [math.NA], 26 May 2023 (cover date 30 May 2023), "Main document submitted
to Communications on Applied Mathematics and Computation": the submitted manuscript, not the
version of record. 72 PDF pages, all read: a 35-page main document (with Appendix A and 38
references) and a 37-page supplementary material with its own page numbering and a 7-item
reference list. Page-1 title and authors match Crossref up to capitalization (page 1:
"A new efficient explicit Deferred Correction framework: analysis and applications to
hyperbolic PDEs and adaptivity"). The filename's 2023 is the online year; the published
issue is 2024. Section, equation, table and figure numbers cited here are those of arXiv v4;
"Supp." refers to the supplement.

# Key claims

Notation: subnodes $t_{n,m}=t_n+c_mh$, $m=0,\dots,\mathsf M$, $c_0=0$, $c_{\mathsf M}=1$;
$Y^{(k)}_m$ the subnode value after iteration $k$, $K$ iterations;
$\omega_{mr}=\int_0^{c_m}\ell_r(\vartheta)\,d\vartheta$ the integration weights;
$\kappa_1$, $\kappa_2$ the constants of the DeC theorem; $s$ the stage count of the
Runge–Kutta form.

1. DeC accuracy theorem: if $\mathcal L^2$ has a unique zero $\mathbf Y^*$, $\mathcal L^1$
   is coercive with constant $\kappa_1$ and $\mathcal L^1-\mathcal L^2$ is Lipschitz with
   constant $\kappa_2h$, then
   $\lVert\mathbf Y^{(K)}-\mathbf Y^*\rVert\le(h\kappa_2/\kappa_1)^K\lVert\mathbf Y^{(0)}-\mathbf Y^*\rVert$,
   and the iteration converges from any start if $h\kappa_2/\kappa_1<1$. (Thm. 2.1, Eqs.
   (1)–(5); Supp. Thm. 1.1) **Proved** (recalled from Abgrall 2017, proof given)
2. If $\mathbf Y^*$ has order $p$ and $\mathbf Y^{(0)}$ is first-order accurate, the
   optimal iteration count is $K=p$; more iterations are wasted. (§2) **Derived**
3. bDeC operators: $\mathcal L^2(\mathbf Y)=0$ has order $\mathsf M+1$ on equispaced subnodes
   and is an implicit Runge–Kutta method with $\mathsf M$ stages; on Gauss–Lobatto subnodes
   it is Lobatto IIIA. (§3.1; Supp. Props. 2.1–2.2) **Proved** (order); **Stated** (Lobatto
   IIIA)
4. bDeC constants: $\kappa_1=1$ and
   $\kappa_2=L_f\max_m\sum_{r=1}^{\mathsf M}\lvert\omega_{mr}\rvert$, $L_f$ the
   Lipschitz constant of $f$. (§3.1; Supp. Remark 2.1) **Proved**
5. Optimal parameters for order $p$: $K=p$ iterations with $\mathsf M=p-1$ on equispaced
   subnodes, and $\mathsf M=\lceil p/2\rceil$ on Gauss–Lobatto subnodes (so $K=2\mathsf M$
   when $p$ is even). (§3.1, p. 6) **Stated**
6. sDeC is equivalent to the Dutt–Greengard–Rokhlin spectral DeC in residual and
   error-function form, with explicit-Euler corrections; bDeC has an analogous residual
   form. (App. A.1–A.2, Eqs. (71)–(72)) **Proved** (by direct computation)
7. The sDeC iterate is an $O(h^{k+1})$ perturbation of the bDeC iterate. (Supp. Prop. 2.4)
   **Proved**
8. αDeC, $\alpha\in[0,1]$, is the convex combination of the bDeC and sDeC updates, after
   Ketcheson & bin Waheed; in matrix form
   $\mathbf Y^{(k)}=\mathbf Y^{(0)}+h(\Theta-\alpha\Gamma)f(\mathbf Y^{(k-1)})+h\alpha\Gamma f(\mathbf Y^{(k)})$
   with $\Theta$ full and $\Gamma$ strictly lower triangular. (§3.3, Eqs. (16)–(20))
   **Derived**
9. αDeCu and αDeCdu start with 2 subnodes, interpolate (solution or right-hand side) to
   $k+2$ equispaced subnodes after iteration $k$, reach $\mathsf M+1$ subnodes after
   $\mathsf M$ iterations, and end with one iteration without interpolation. They reach the
   order $\mathsf M+1$ of αDeC with $\mathsf M+1$ equispaced subnodes. (§4.1–4.2, Eqs.
   (21)–(29), Fig. 2) **Derived** (accuracy argued, not proved)
10. On Gauss–Lobatto subnodes the interpolation must happen in the first iterations: $k+1$
    such nodes give order $2k$ for $\mathcal L^2$ but only order $k+1$ for the interpolant.
    (§4.3) **Stated**
11. Stage counts: αDeC $s=\mathsf MK$; bDeC $s=\mathsf M(K-1)+1$; bDeCu
    $s=\mathsf M(K-1)+1-(\mathsf M-1)(\mathsf M-2)/2$; αDeCdu $s=\mathsf MK-\mathsf M(\mathsf M-1)/2$;
    bDeCdu $s=\mathsf M(K-1)+1-\mathsf M(\mathsf M-1)/2$; αDeCu with $\alpha\ne0$ has the
    stage count of αDeC. (§5.1–5.3) **Derived**
12. Theoretical speed-ups (stage ratios) at order 13: equispaced ($\mathsf M=12$) αDeCdu
    1.733 (156→90), bDeCu 1.611 (145→90), bDeCdu 1.835 (145→79); Gauss–Lobatto
    ($\mathsf M=7$) αDeCdu 1.300 (91→70), bDeCu 1.214 (85→70), bDeCdu 1.328 (85→64).
    (Tables 5–6) **Derived**
13. For αDeCu with $\alpha\ne0$ about half the stages are cheap interpolations, so the stage
    count overstates the cost. (Remark 5.1) **Stated**
14. Theorem 6.1: every bDeC, bDeCu and bDeCdu method of order $K$ has stability function
    $R(z)=\sum_{j=0}^Kz^j/j!$, independent of the subnodes; the Butcher matrix is block
    strictly lower triangular with $K$ block rows, so $A^K=0$. (§6, Eq. (44)) **Proved**
15. Theorem 6.2: for fixed order, subnodes and $\alpha$, αDeCu and αDeCdu are equivalent on
    linear systems, since interpolation commutes with a linear right-hand side. (§6, Eqs.
    (46)–(48)) **Proved**
16. Stability regions for orders 3–13 are identical for bDeC, bDeCu and bDeCdu on any
    subnodes; sDeC and sDeCu = sDeCdu are plotted separately for equispaced and
    Gauss–Lobatto subnodes. (Fig. 3) **Shown**
17. Abgrall's continuous Galerkin DeC uses forward Euler with first-order mass lumping
    $C_i=\int_\Omega\varphi_i$ in $\mathcal L^1$, so it is explicit and needs no mass-matrix
    inversion; it is well posed iff $C_i\ne0$ (false for quadratic Lagrange elements on
    triangles, true for Bernstein elements) and is not a Runge–Kutta method, because
    $\mathcal L^1$ and $\mathcal L^2$ carry different mass matrices. (§7.2, Remark 7.1)
    **Stated**; the operator properties **Proved** in Supp. §3 under a Poincaré-type
    Assumption 3.8 and a smoothness Assumption 3.9, with $h\le C\Delta x$.
18. Order-adaptive DeC: αDeCu and αDeCdu keep adding subnodes until
    $\lVert y^{(k)}_{n+1}-y^{(k-1)}_{n+1}\rVert/\lVert y^{(k)}_{n+1}\rVert\le\varepsilon_{\rm tol}$;
    with $\varepsilon_{\rm tol}=10^{-8}$ the error is about constant in $h$, and the mean
    iteration count falls with $h$ (from about 13 at $h\approx10^{-0.5}$ to about 5 at
    $h\approx10^{-1.75}$ for equispaced bDeCu). (§8, Eq. (60); Figs. 4–6, 8–9) **Shown**
19. Linear $2\times2$ system: orders 3–9 attained; bDeC, bDeCu and bDeCdu give the same
    error; sDeCu and sDeCdu errors are slightly larger than sDeC; the bDeC Pareto front
    consists only of new methods; measured bDeCdu speed-up about 2 at order 9 (equispaced)
    and close to 4/3 (Gauss–Lobatto). (§9.1.1, Figs. 4, 5, 7) **Shown**
20. Forced damped oscillator (linear but non-autonomous, so Thms. 6.1–6.2 do not make the
    methods coincide): similar errors, the new methods slightly less accurate at fixed $h$;
    for equispaced bDeC they nearly halve the run time at high order; sDeCdu beats sDeC from
    order 6 (equispaced), sDeCu is always worse than sDeCdu. (§9.1.2, Figs. 8–10) **Shown**
21. 1D linear advection, CFL 0.1, CIP stabilization: bDeC and bDeCu errors are essentially
    identical for quadratic and cubic Bernstein, Lagrange and Gauss–Lobatto Lagrange
    elements; the formal order is recovered except with cubic Bernstein and cubic Lagrange
    elements (second order only, for both); bDeCu speed-ups reach about 1.8, larger than for
    ODEs because the PDE cost is dominated by new stages. (§9.2.1, Figs. 11–12, Remark 9.1)
    **Shown**
22. Abgrall's continuous Galerkin DeC with cubic Bernstein (B3), cubic Lagrange (P3) and
    quartic Bernstein (B4) elements is second order on unsteady problems with the optimal
    iteration count; the formal order needs 10 (P3), 80 (B3) or 320 (B4) iterations. CFL
    0.1, 0.01, 0.001 do not change this, and higher-derivative CIP lowers the errors but not
    the order. The loss is absent on steady problems and with mass-lumpable Gauss–Lobatto or
    cubature elements; the authors suspect that Assumption 3.8 fails. (Remark 9.1; Supp.
    §3.2, Figs. S1–S3) **Shown**; the cause **Stated** as a conjecture
23. 2D shallow-water vortex: new and original bDeC errors coincide; formal orders are
    recovered for quadratic Bernstein and quadratic and cubic cubature elements; the
    measured speed-up 1.25 for quadratic Bernstein equals the theoretical 5/4 obtained by not
    counting interpolated stages. (§9.2.2, Figs. 12–13) **Shown**
24. The speed-ups of the Fortran code (Bernstein elements) are much higher than those of the
    Python code (cubature elements). (§9.2.2) **Stated**

*(Reader checks, not in the source.)* The paper calls iterate $k$ "$O(\Delta t^{k+1})$
accurate", meaning its local error, so iteration $k$ is order $k$; with the bundle's
convention the final order is $\min(K,\mathsf M+1)$ on equispaced subnodes. The measured
speed-up exceeds the stage-count prediction (about 2 against $65/37\approx1.757$ for
equispaced bDeCdu9) and falls short of it at order 3 (about 1.0 against 1.25), unexplained
beyond Remark 5.1. Theorem 6.1 gives bDeC-type methods the stability polynomial of any
$K$-stage order-$K$ explicit method: their extra stages buy no linear stability, while the
sDeC regions differ.

# Printed slips

- References [31] and [32] are the same work, Öffner & Torlo, Appl. Numer. Math. 153:15–34
  (2020), printed twice ([32] with the abbreviated journal); [31] is cited in §1, [32] in
  §2 and §3.1.
- Thm. 2.1 assumes "$\exists\,\alpha_1\ge0$", but (4) and (5a) divide by $\alpha_1$; it must
  be positive (Supp. Prop. 3.10 writes $\alpha_1>0$).
- §9.1.2, after (62): "with $m,k,\Omega>0$, $r,F,\psi\ge0$"; $\psi$ is the phase of the
  particular solution defined later, the problem's phase is $\varphi$ (Supp. (162) writes
  "$r,F\ge0$ with $\varphi\in[0,2\pi[$").
- §9.1.1: bDeC, bDeCu and bDeCdu have the same error "since they coincide on linear
  problems, as shown in Theorem 6.1"; Theorem 6.1 is about the stability function only.
- §9.1.1: the speed-up is "the ratio between the computational times required by the bDeCdu
  and the bDeC method", which would be below 1; the plotted values (Fig. 7) are bDeC over
  bDeCdu.
- Supp. §4, case 3 of (167): "$\lambda_{1,2}=\alpha\pm i\omega$, complex and conjugate with
  negative real part"; by (167) the real part is $-\alpha/2$, as (168) uses.
- Ref. [24] (Liu, Shu & Zhang 2008, J. Comput. Math. 26(5):633–656) prints the same page
  range as [19] (Huang, Jia & Minion, J. Comput. Phys. 214(2):633–656, 2006); recorded as
  printed, unverified.

# Notation map

| Micalizzi & Torlo | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\frac{d}{dt}u=G(t,u)$, $u\in\mathbb R^Q$ | $y'=f(t,y)$, $y\in\mathbb R^d$ | **source $Q$ is the dimension, not the registry collocation matrix** |
| $L$ | $L_f$ | Lipschitz constant of $G$; **the registry $L$ is the linear operator** |
| $\Delta t$; $\Delta$ | $h$; $h$ (ODE) or $\Delta x$ (CG) | DeC parameter of Thm. 2.1 |
| $h$ | $\Delta x$ | mesh size |
| $t^m$, $m=0..M$ | $t_{n,m}$, $m=0,\dots,\mathsf M$ | subnodes; $M$ subintervals |
| $M$ | $\mathsf M$ | **not the registry mass matrix** |
| $P$ (iterations, order) | $K$ (iterations), $p$ (order) | DeC($P$) has order $P$ |
| $p$ (iteration index) | $k$ | superscript $(k)$ |
| $u^{m,(p)}$, $\underline u^{(p)}$, $U^{(p)}$ | $Y^{(k)}_m$, $\mathbf Y^{(k)}$ | capital $U$ includes $u^0=y_n$ |
| $\psi^\ell$ | $\ell_r$ | Lagrange basis on the subnodes |
| $\theta^m_\ell$, $\Theta$ | $\omega_{mr}$, $\Theta$ | big-interval weights, as on the DeC page |
| $\delta^m_\ell$ | $\omega^{\mathrm s}_{mr}$ | small-interval weights, as on the DeC page |
| $\beta^m$ | $c_m$ | node fractions |
| $\gamma^m$, $\Gamma$ | $c_m-c_{m-1}$, $\Gamma$ | **$\Gamma$ is not the MRI-GARK $\Gamma^{(k)}$** |
| $\alpha$ | $\alpha$ | αDeC parameter; **not the Shu–Osher or Rosenbrock $\alpha$** |
| $\alpha_1$, $\alpha_2$ | $\kappa_1$, $\kappa_2$ | coercivity and Lipschitz constants, as on the DeC page |
| $\mathcal L^1_\Delta$, $\mathcal L^2_\Delta$ | $\mathcal L^1$, $\mathcal L^2$ | |
| $H^{(p)}$, $U^{*(p)}$, $G^{*(p)}$ | kept | interpolation matrix; interpolated solution and right-hand side |
| $W^{(p)}$, $X^{(p)}$, $Y^{(p)}$ | kept, page-local | Butcher-tableau blocks; **$Y^{(p)}$ is not a stage value** |
| $A$, $b$, $c$, $S$; $y^s$ | $A$, $b$, $c$, $s$; $Y_i$ | zero-based stage values |
| $R(z)$, $z=\lambda\Delta t$ | $R(z)$, $z=h\lambda$ | region printed with strict $\lvert R\rvert<1$ |
| $\varepsilon$ | $\varepsilon_{\rm tol}$ | adaptivity tolerance; **not the registry stiffness $\varepsilon$** |
| $\varphi_i$, $C_i$, $\phi_i$, $ST_i$ | kept | finite-element basis, lumped mass, space residual, stabilization |

# Reference list

The main document prints 38 references, numbered [1]–[38] in alphabetical order; the
supplement prints its own 7. The lists are merged complete into the
[bibliography](/bibliography.md) with `citedby` micalizzi-2024, 39 entries for 45 printed
items. Main [31] and [32] are one work (merged as `offner-2020`). Five supplement items
repeat main-list ones (S[1]=[2], S[2]=[3], S[3]=[6], S[6]=[26], S[7]=[27]); S[4] (Larson &
Zahedi 2020) and S[5] (Micalizzi, Ricchiuto & Abgrall, in preparation, 2022) are new
entries. [4], [25] and [35] are arXiv preprints and stay their own entries. [38] prints
"Gerhard Wanner and Ernst Hairer" for *Solving Ordinary Differential Equations II*; it is
the Hairer & Wanner monograph and is merged into `hairer-1996`. [14] prints only an article number. The list
cites the ingested [Han Veiga et al. (2021)](/sources/hanveiga-2021.md) and
[Ciallella et al. (2022)](/sources/ciallella-2022.md).

# Pages created or updated

Chunk 5 (2026-10-20). This source is cited on:

* [ADER as a time integrator](/methods/ader-time-integration.md)
* [Deferred correction (DeC)](/methods/deferred-correction.md)
* [Equivalence of DeC and ADER](/results/dec-ader-equivalence.md)
* [Lax–Wendroff flux reconstruction (single-stage Taylor time stepping)](/methods/lax-wendroff-flux-reconstruction.md)
* [Linear advection equation](/benchmarks/linear-advection-equation.md)
* [Positivity preservation in time integration](/properties/positivity-preservation.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)
* [Step-size control: error-based controllers, PID filters and CFL control](/methods/step-size-control.md)
* [Strong-stability-preserving (SSP) Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md)
