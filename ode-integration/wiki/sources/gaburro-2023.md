---
type: Source
title: "Gaburro et al. (2023) — High order entropy preserving ADER-DG schemes"
description: "Builds a fully discrete entropy-conservative or entropy-dissipative ADER-DG scheme on unstructured triangles by combining Abgrall's cell-wise entropy-correction term in space with relaxation of the ADER predictor–corrector step in time, and shows design order and total entropy matched to machine precision on advection, shallow-water and Euler tests."
resource: "doi:10.1016/j.amc.2022.127644"
source_kind: paper
authors: [Gaburro E., Öffner P., Ricchiuto M., Torlo D.]
year: 2023
venue: "Appl. Math. Comput. 440:127644"
local_file: "/home/stefano/papers/mosaic/ode-integration/2023_Crossref_Applied_Mathematics_and_Computation_Gaburro_High_order_entropy_preserving_ADER-DG_schemes.pdf"
tags: [ader, relaxation, entropy-stability, structure-preserving, hyperbolic-conservation-laws]
timestamp: 2026-10-20T06:18:00Z
---

# Summary

The paper builds what the authors call the first provably fully discrete
entropy-preserving ADER-DG scheme for multidimensional hyperbolic
conservation laws $\partial_tu+\operatorname{div}F(u)=0$ on unstructured
triangular meshes. The base scheme is modern
[ADER as a time integrator](/methods/ader-time-integration.md) in its
explicit space–time finite-element reading: a cell-local Galerkin predictor
solved by Picard iterations, then a corrector that updates the modal DG
coefficients with a time quadrature $\{\beta_s\}_{s=0}^S$ of the fluxes
evaluated on the predictor. ADER-DG is not a method-of-lines scheme; cells
communicate only in the corrector.

Two ingredients make the scheme entropy preserving. In space, Abgrall's
entropy-correction term $\alpha^s_{\Omega_i}\int_{\Omega_i}\nabla\psi\,A_0\nabla v_h$
is added to the corrector at each quadrature node, with a cell-wise scalar
chosen so that the central part of the flux plus the correction produces
exactly the numerical entropy flux across the cell boundary; the upwind
part of the flux leaves an entropy-dissipative remainder. In time, the
paper applies [relaxation](/methods/relaxation-runge-kutta.md) to the ADER
step: the increment $y_{n+1}-y_n$ is scaled by $\gamma_n$, time advances by
$\gamma_nh$, and $\gamma_n$ is the nontrivial root of a scalar equation
that matches the new total entropy to the quadrature of the spatial entropy
balance. Dropping the dissipative remainder from the target gives exact
conservation. For quadratic entropy $\gamma_n$ is explicit; otherwise a
scalar Newton iteration is used. Existence of $\gamma_n$,
$\gamma_n=1+O(h^{p-1})$ and preservation of order $p$ are imported from the
relaxation theory for Runge–Kutta and multistep methods, not proved for
ADER.

The tests use P1–P3 (orders 2–4) on 2D linear advection, a shallow-water
moving vortex, the Euler [isentropic vortex](/benchmarks/isentropic-vortex.md),
a smoothed moving contact and the 2D "123" problem. They show near-design
order, total entropy error at $10^{-12}$–$10^{-16}$ for the relaxed scheme
against $10^{-3}$–$10^{-8}$ entropy loss for plain ADER-DG — the
[entropy stability](/properties/entropy-stability.md) of the fully discrete
scheme — and $\gamma_n$ close to 1, closer at higher order and up to about
1.35 for discontinuous data. No limiter is used, so strong shocks are out
of scope.

# Version read

arXiv:2206.03889v1 [math.NA], 8 June 2022, a 24-page preprint (main text
pp. 1–21, references pp. 21–24), not the Appl. Math. Comput. version of
record. Page 1 prints the title "High order entropy preserving ADER
scheme" (singular, without "-DG"); the published title is "High order
entropy preserving ADER-DG schemes", and the content may have been revised
after review (not checked). Authors and their order agree with the
published version. The archive filename names the journal version; the
DOI is not printed in the file. Equation, table, figure and remark numbers
on this page are those of arXiv v1.

# Key claims

Registry notation: $h$ step, $y_n$ the discrete solution at $t_n$ (the DG
coefficients), $\gamma_n$ relaxation parameter, $\eta$ the convex entropy,
$p$ order. PDE-level symbols ($u$, $F$, $v$, $A_0$, $\beta_s$, $F^s_i$,
$D^s_i$, $E^s_i$) are the source's and are kept page-locally; $\mathcal E$
denotes the total entropy $\int_\Omega\eta(u)\,dx$ on this page only.

1. No provable high-order entropy-conservative or entropy-dissipative ADER
   method existed before; this is the first provable fully discrete
   entropy-preserving ADER-DG scheme (Abstract, §1). **Stated**
2. ADER-DG is not a method-of-lines scheme but a local predictor–corrector
   with one inter-element communication per step, in the corrector, which
   gives efficiency advantages over RK-DG (§3.1, citing Balsara et al. [5]).
   **Stated** (not measured)
3. The predictor (Eq. 11) is solved cell by cell by discrete Picard
   iterations (Eq. 12); the resulting ADER-DG scheme is an explicit
   space–time finite-element method (§3.2.1–3.2.2). **Stated**
4. The coefficient $\alpha^s_{\Omega_i}$ of Eq. 22 makes the central-flux
   part plus the correction equal the numerical entropy flux
   $\int_{\partial\Omega_i}\mathcal G\cdot n$ in each cell at each node
   (Eq. 21). Since $D^s_i$ always decreases entropy, the quadrature estimate
   of the entropy production is bounded by
   $-h\sum_s\beta_s\int_{\partial\Omega}G\cdot n\,dS$ (§4.1). **Derived**
5. When $E^s_i<\varepsilon^s:=\bar h^N\max_iE^s_i$ the code sets
   $\alpha^s_{\Omega_i}=0$ (Remark 4.1, Eq. 23); in the relaxation equation
   such cells use $\int_{\partial\Omega_i}G(v^s)\cdot n\,dS$ instead, so the
   global balance (Eq. 36) still holds exactly (Remark 4.3). **Derived**
6. For $N=0$ (finite volumes) the correction terms vanish and the framework
   does not apply; the face-jump correction
   $\mathcal F^{co}=\mathcal F-\alpha_fA_0[\![v]\!]$ is entropy conservative
   for $\alpha_f=\alpha_0$ (Eq. 28) and semi-discretely entropy stable for
   $\alpha_f>\alpha_0$ (Remark 4.2, Eqs. 24–28). **Stated** (not used further)
7. Relaxed ADER-DG: $y^{\gamma}_{n+1}=y_n+\gamma_n(y_{n+1}-y_n)$ at time
   $t_n+\gamma_nh$, with $\gamma_n$ the nontrivial root of
   $R(\gamma_n)=\mathcal E(y_n+\gamma_n(y_{n+1}-y_n))-\mathcal E(y_n)+\gamma_nh\sum_s\beta_s\sum_i(F^s_i+\alpha^s_{\Omega_i}E^s_i+D^s_i)$
   (Eq. 34); removing $D^s_i$ gives exact entropy conservation in time
   (§4.2, Eqs. 29–35). **Derived**
8. By Ranocha, Lóczi & Ketcheson [47], for a base method of order $p\ge2$
   a unique $\gamma_n>0$ exists for small $h$, $\gamma_n=1+O(h^{p-1})$, and
   the relaxed solution has order $p$ (§4.2). **Stated** (by citation; the
   hypotheses of [47] are not verified for ADER-DG)
9. For quadratic entropy $\eta=\langle u,u\rangle/2$, $\gamma_n$ is
   explicit (Eq. 42) and close to one (Example 4.5); for general entropies a
   scalar Newton iteration on $R$ uses the derivative of Eq. 37 (Remark 4.4).
   **Derived**
10. Travelling bump (linear advection), $t_f=3$: P1/P2/P3+Rel give observed
    $L^2$ orders 1.78/1.82/1.84, 2.77/2.91/2.94 and 3.47/3.79/3.97; the text
    says "order of accuracy N+1" (Table 1). **Shown**
11. Travelling bump, $t_f=15$, about 71k DOFs: plain ADER-DG loses entropy
    ($10^{-4}$ for P1 to $10^{-6}$ for P3), the relaxed schemes hold the
    entropy error at $10^{-12}$–$10^{-16}$ (Fig. 1); $\gamma_n\approx$
    1.004–1.005 (P1), 1.0005 (P2), 1.0000 (P3) (Fig. 2). **Shown**
12. Rotating bump: expected orders (Table 2, final-row P1 1.91, P2 3.19,
    P3 3.70); plain ADER-DG entropy error grows in time, relaxed stays at
    machine precision (Fig. 3); $\gamma_n\approx$ 1.08–1.12 (P1), 1.01
    (P2), 1.00 (P3) (Fig. 4). **Shown**
13. Shallow-water $C^6$ moving vortex, $t_f=1$: orders P1 2.07/2.04/2.02,
    P2 2.89/2.91/2.93, P3 4.10/4.07/4.05 (Table 3); accuracy "is not
    modified by the entropy correction and relaxation" (§5.2.1). **Shown**
    (the plain ADER-DG table is not printed)
14. Shallow-water vortex: plain ADER-DG dissipates entropy, more at lower
    order; relaxed schemes conserve it to machine precision (Fig. 6); for P1
    $\gamma_n=1+O(10^{-1})$, much closer to 1 at higher order (Fig. 7).
    **Shown**
15. Euler isentropic vortex, $t_f=1$: orders P1 2.03/2.02/2.01,
    P2 2.68/2.71/2.74, P3 4.35/4.20/4.06 (Table 4); classical and relaxed
    errors very close; relaxed total entropy at machine precision (Fig. 9);
    $\gamma_n\lesssim1.02$ (Fig. 10). **Shown**
16. Smoothed moving contact, no limiter: small overshoots; classical
    schemes lose entropy at nearly the same rate for all orders, relaxed
    schemes match the exact total entropy to machine precision; $\gamma_n$
    reaches about 1.2 (Figs. 11–13). **Shown**
17. 2D "123" problem, $t_f=0.15$: no visible difference in density
    (Fig. 14); relaxed schemes match the reference entropy (Eq. 62) to
    machine precision (Fig. 16); $\gamma_n$ reaches about 1.35 for P1
    (Fig. 17). **Shown**
18. Relaxation "is able to guarantee a zero entropy production also during
    the time discretization for the entropy conservative terms", and the
    scheme "outperforms the classical ADER-DG" in exactly preserving total
    entropy where physics does (§6). **Stated**
19. The scheme starts from unlimited ADER-DG; shocks need a limiter inside
    the split spatial discretization, and a $P_NP_M$ extension is in
    preparation (§6, Remarks 3.1 and 4.2). **Stated**

*(Compiler note, not in the source.)* Claim 8 is a hypothesis for ADER:
the relaxation target is a quadrature of the spatial entropy production on
the predictor, not on the stages of the step being relaxed, so the
hypotheses of [47] do not apply directly. The conservative variant (target
without $D^s_i$) forces exact entropy conservation even where the upwind
flux dissipates entropy, unlike the dissipation-matching practice of
Ranocha et al. [48]; which variant each test uses is not stated, and the
machine-precision match to the exact entropy implies the conservative one.

# Printed slips

- Table 2, P1+Rel, last row: $\Delta x$ printed "3.43E-3"; the sequence
  4.53E-2, 4.06E-2, 3.71E-2 and the printed order 1.91 require 3.43E-2.
- Table 2, P2+Rel, first row: error printed "8.09E-5"; the next row
  (6.16E-6) with the printed order 2.69 implies about 8.09E-6.
- Tables 1 and 2 (scalar advection) label the error "L2(h − hex)"; the
  variable is $u$ (copied from the shallow-water table).
- Eq. 36 lacks the factor $\gamma^n\Delta t$ before the sum (compare
  Eqs. 31–33) and writes $\beta^s$ for $\beta_s$.
- Eq. 21 ranges over "$s=1,\dots,S$", while every sum runs over
  $s=0,\dots,S$.
- §5.3: "The Hessian of the flux is" introduces Eq. 56, which is
  $\partial_uv$, the Hessian of the entropy.
- Fig. 5 caption says "profile of the density ρ" for the shallow-water
  test (the variable is the depth $h$) and "DG scheme of order 2" while the
  text says P2 (order 3).
- Fig. 15 caption says "DG scheme of order 3" and the text a "P3" scheme on
  a mesh of 5130 elements, which is the P2 mesh of that section.
- Travelling bump: the $\gamma$ figure is said to use $t_f=15$, but the
  time axis of Fig. 2 ends near 6.3.
- Remark 4.3 writes "$\alpha_{\Omega_i}=0$" and "$\varepsilon$" without the
  superscript $s$.
- Eq. 9 prints the index range "$\ell=0,\dots,\mathcal Q$"; Eq. 8 sums to
  $\mathcal Q-1$.
- §5.1.1 claims "order of accuracy N+1" for all degrees, whereas P1 gives
  1.78–1.84 (Table 1).
- Symbol clashes: $\gamma$ is both the adiabatic exponent (Eqs. 52–57) and
  the relaxation parameter; $\psi$ is both a test function (§4.1) and the
  entropy potential (Remark 4.2).

# Notation map

| Gaburro et al. (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Delta t$ | $h$ | step size |
| **$h_i$, $\bar h$; $h$ (water depth, §5.2)** | — | **collision with the step $h$**: cell circumradius, mean mesh size, shallow-water depth |
| $u^n_h$, $\hat u^n_\ell$ | $y_n$ | discrete solution (modal DG coefficients) |
| $\Delta u_h=u^{n+1}_h-u^n_h$ | $y_{n+1}-y_n$ | step increment |
| $\gamma^n$ | $\gamma_n$ | relaxation parameter |
| $u^{n+1}_{h,\gamma^n}$, $\tilde t^{n+1}_{\gamma^n}=t^n+\gamma^n\Delta t$ | $y^{\gamma}_{n+1}$, $t_n+\gamma_nh$ | relaxed solution and time |
| **$\gamma$ (§5.3)** | — | **collision with $\gamma_n$**: adiabatic exponent |
| $\eta$, $v=\partial_u\eta$ | $\eta$, $\eta'$ | entropy and entropy variables (agrees) |
| $\mathcal E(u)=\int_\Omega\eta(u)\,dx$ | — | total entropy, page-local |
| $G$, $\mathcal G$ | — | entropy flux and numerical entropy flux; **not the G-norm matrix $G$ nor the coarse propagator $\mathcal G$** |
| $A_0=\partial_vu$ | — | inverse entropy Hessian at the cell average |
| **$\psi$** | — | **collision inside the source**: test function (§4.1) and entropy potential (Remark 4.2); unrelated to the registry one-step map $\psi_h$ |
| **$R(\gamma)$** | — | **collision with the stability function $R(z)$**: relaxation residual |
| $\beta_s$, $s=0,\dots,S$ | — | time-quadrature weights on $[t_n,t_{n+1}]$, summing to 1; **collision with PID exponents $\beta_1,\beta_2,\beta_3$** |
| $q_h$, $q^s_h$ | — | space–time predictor and its value at node $s$ |
| $N$ | — | polynomial degree; P$N$ has order $N+1$ |
| $F^s_i$, $D^s_i$, $E^s_i$, $\alpha^s_{\Omega_i}$ | — | central, dissipative and correction entropy terms; correction coefficient |
| $\alpha_f$, $\alpha_0$ | — | face correction coefficient (Remark 4.2); **collision with Shu–Osher $\alpha_{ij}$** in letter only |
| $a_{LF}$ | — | Rusanov wave speed |

# Reference list

The paper prints 64 references, numbered [1]–[64] in alphabetical order.
All 64 are merged complete into the [bibliography](/bibliography.md) with
`citedby` gaburro-2023. Five arXiv preprints ([2], [35], [36], [38], [54])
are kept as their own entries. Refs. [3] and [4] print no volume; refs.
[18], [29], [41], [52] and [64] are printed in zbMATH style ("vol:pages,
Id/No") and recorded as volume and article number. Ref. [18] prints an
author as "Lucas Fredrich" (probably Friedrich), kept as printed.
Same-author same-year pairs take suffixes: fisher-2013/-b, gaburro-2021/-b,
gassner-2016/-b, manzanero-2020/-b; the two Ranocha 2020 works ([47],
[48]) match the existing entries `ranocha-2020-b` and `ranocha-2020-c`.
Ref. [3] (Abgrall et al., printed 2020 with online-first pages) is the
journal paper keyed `abgrall-2023` by its issue year. No printed
duplicates or unparseable items.

# Pages created or updated

Chunk 2 (2026-10-19). This source is cited on:

* [ADER as a time integrator](/methods/ader-time-integration.md)
* [Entropy stability and conservation of the fully discrete scheme](/properties/entropy-stability.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Lax–Wendroff flux reconstruction (single-stage Taylor time stepping)](/methods/lax-wendroff-flux-reconstruction.md)
* [Linear advection equation](/benchmarks/linear-advection-equation.md)
* [Relaxation Runge–Kutta methods](/methods/relaxation-runge-kutta.md)
