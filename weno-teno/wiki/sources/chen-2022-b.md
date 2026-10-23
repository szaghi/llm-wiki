---
type: Source
title: "Chen & Wu (2022) — A physical-constraint-preserving finite volume WENO method for special relativistic hydrodynamics on unstructured meshes"
description: "Third-order finite-volume WENO scheme on triangles for special relativistic hydrodynamics, proved physical-constraint-preserving through geometric quasilinearization and an HLL flux, with scale-invariant Zhu–Qiu weights that make the scheme homogeneous and three provably convergent pressure-recovery root finders."
resource: "doi:10.1016/j.jcp.2022.111398"
source_kind: paper
authors: [Chen Y., Wu K.]
year: 2022
venue: "J. Comput. Phys. 466:111398"
local_file: "/home/stefano/papers/mosaic/weno-teno/2022_Crossref_Journal_of_Computational_Physics_Chen_A_physical-constraint-preserving_finite_volume_WENO_method_f.pdf"
tags: [bound-preserving, relativistic, finite-volume, weno, scale-invariance, cweno]
timestamp: 2026-10-22T20:00:00Z
---

# Summary

The paper builds a third-order finite-volume WENO scheme for the
two-dimensional [special relativistic hydrodynamics](/definitions/relativistic-hydrodynamics.md)
(RHD) equations with the ideal equation of state on unstructured triangular
meshes, and proves it physical-constraint-preserving (PCP): cell averages stay in
the admissible set $G=\{\rho>0,\ p>0,\ \lvert v\rvert<1\}$, a case of
[bound preservation](/properties/bound-preservation.md) made hard by the
primitive variables and fluxes being implicit functions of the conserved ones.

The ingredients are (i) the Zhu–Qiu big-plus-small reconstruction on triangles,
a [CWENO](/methods/cweno.md)-type combination of one quadratic and four linear
polynomials, applied in [characteristic variables](/methods/characteristic-decomposition.md)
along each of the three edge normals and averaged; (ii) a two-step
[Zhang–Shu-type scaling limiter](/methods/zhang-shu-scaling-limiter.md)
(density, then the concave function $E-\sqrt{D^2+\lvert m\rvert^2}$) that evaluates
only the edge Gauss points plus one interior remainder defined through the
Zhang–Xia–Shu triangle quadrature, a [cell-average decomposition](/methods/optimal-cell-average-decomposition.md);
(iii) bisection, fixed-point and hybrid pressure-recovery root finders, all
provably convergent; (iv) the [HLL flux](/methods/hll-riemann-solvers.md), proved
PCP through the linear form of $G$ given by
[geometric quasilinearization](/methods/geometric-quasilinearization.md), with
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md) extending the result in time.

The second contribution is a [scale-invariant](/properties/scale-invariance.md)
modification of the Zhu–Qiu weights, a [WENO-Z](/methods/weno-z.md)-type form
whose original version mixes powers of the
[smoothness indicators](/definitions/smoothness-indicator.md): with the new
weights the whole one-step operator is homogeneous of degree one, as the exact
RHD evolution is. Twelve examples support the theory: third order on relativistic
[isentropic vortices](/benchmarks/isentropic-vortex.md) down to pressure
$1.78\times10^{-20}$; quasi-one-dimensional and scaled Riemann problems, where the
original weights oscillate and break homogeneity; [two-dimensional Riemann
problems](/benchmarks/two-dimensional-riemann-problems.md),
[double Mach reflection](/benchmarks/double-mach-reflection.md),
[forward-facing steps](/benchmarks/forward-facing-step.md) with inflow speed up to
$0.999$, [shock–vortex interaction](/benchmarks/shock-vortex-interaction.md),
[shock diffraction](/benchmarks/shock-diffraction.md) and an axisymmetric
[relativistic jet](/benchmarks/high-mach-astrophysical-jet.md) without
[carbuncle](/definitions/carbuncle-phenomenon.md). The references to
[DG](/methods/discontinuous-galerkin.md) PCP schemes and to
[multi-resolution WENO](/methods/multi-resolution-weno.md) are background.

# Version read

arXiv 2207.09385v1 [math.NA], 19 July 2022 (pdfTeX preprint, not the version of
record), 56 pages, all read; pp. 13–14, 18, 25–27, 30 and 41–42 checked visually.
Page 1 matches Crossref in title and authors; the preprint prints no DOI.
Section, equation, figure and table numbers cited here are those of the arXiv v1
and may differ from the journal article.

# Key claims

Registry notation (see the notation map): the source's adiabatic index $\Gamma$
is $\gamma$, its Lorentz factor $\gamma$ is $W$, its conserved vector $U$ is $u$,
its linear weights $\gamma_\ell$, unnormalized and normalized weights
$\delta_\ell$, $\varpi_\ell$ are $d_\ell$, $\alpha_\ell$, $\omega_\ell$, its
regularization $\varepsilon$ is $\epsilon$, its scaling constant $\zeta$ is
$\sigma$, its spectral radius $\hat\sigma$ is $a$, and its boundary weight
$\tfrac23\hat\omega_1$ is $\varpi$.

1. The admissible set $G$ (Eq. 11) is convex and equals $\{D>0,\ E-\sqrt{D^2+\lvert m\rvert^2}>0\}$, the second function concave (Lemmas 2.1–2.2, recalled from Wu & Tang 2015). **Stated**
2. The fluxes and $E-\sqrt{D^2+\lvert m\rvert^2}$ are homogeneous of degree one in $u$ and the eigenstructure is invariant under $u\mapsto\sigma u$ (Eqs. 13–14); hence $\sigma u\in G$ (Lemma 2.3) and the exact evolution operator is homogeneous, $u(x,t)=\frac1\sigma S_t(\sigma u(x,0))$ (Prop. 2.1). **Proved**
3. The nonlinear weights (32), $\alpha_\ell=d_\ell\big(1+\tau^2/(\beta_\ell+\epsilon)^2\big)$ with $\epsilon=\lvert K_0\rvert\max_{K\in N_0}\lvert\bar u_K\rvert^2$, are scale-invariant, so the reconstruction is homogeneous of degree one (Lemma 3.1). **Proved**
4. The original Zhu–Qiu weights (34), $\alpha_\ell=d_\ell\big(1+\tau^2/(\beta_\ell+\epsilon)\big)$ in this paper's notation, are not scale-invariant even with the scaled $\epsilon$, because $\tau^2$ scales as $\sigma^4$ and $\beta_\ell+\epsilon$ as $\sigma^2$ (Remark 3.3). **Derived**
5. The modified weights keep third order: with $\tau=O(\lvert K\rvert^{3/2})$ and $\beta_\ell=O(\lvert K\rvert)$ (from Zhu & Qiu 2018), $\tau^2/(\beta_\ell+\epsilon)^2=O(\lvert K\rvert)$ and $\omega_\ell=d_\ell(1+O(\lvert K\rvert))$ (Remark 3.3, end of §3.2.1). **Derived**
6. The characteristic WENO operator, which averages the three edge-normal characteristic reconstructions (Eq. 38), is conservative (Eq. 36) and homogeneous (Lemma 3.2). **Proved**
7. The two-step PCP limiter (Eqs. 40–43) keeps the cell average and makes admissible both the edge Gauss-point values and the interior remainder $\big(\bar u_K-\varpi\sum_{j,q}\mathsf w_qu(x^{(jq)})\big)/(1-2\hat\omega_1)$; apart from the safety margins $\le10^{-13}$ it is homogeneous (Prop. 3.1, Eq. 45). **Proved**
8. The limiter uses the concavity of the energy constraint, avoids the quadratic equation of Qin, Shu & Yang and, like a simplified limiter of earlier work, never evaluates the interior quadrature points (Remark 3.5). **Stated**
9. For admissible $u$ the pressure function $\Phi_u(p)$ is strictly increasing on $[0,\infty)$ with $\Phi_u(0)<0$ and $\Phi_u\to+\infty$, so the positive pressure root exists and is unique and the conserved-to-primitive map is a bijection of admissible sets (§3.4, Lemma 3.3). **Proved**
10. Bisection on $(0,p_R^{(0)})$, $p_R^{(0)}=(\gamma-1)\big(E-D\sqrt{1-\lvert m\rvert^2/E^2}\big)$, converges with error $\le p_R^{(0)}/2^{n+1}$ (Alg. 3.1). **Proved**
11. The fixed-point iteration $p^{(n)}=p^{(n-1)}-(\gamma-1)\Phi_u(p^{(n-1)})$ from $p^{(0)}=p_R^{(0)}/2$ stays positive and contracts at rate $\delta=(\gamma-1)\lvert m\rvert^2/E^2<1$ (Alg. 3.2, Eqs. 46–47). **Proved**
12. The hybrid algorithm uses bisection when $\delta\ge\tfrac12$ and the fixed point otherwise, with rate $\min\{\tfrac12,\delta\}$ (Alg. 3.3). **Proved** (from claims 10–11)
13. Newton's method is not convergence-guaranteed: the iterate can turn negative even for admissible $u$ (Remark 3.6, illustrated in Remark 4.1). **Stated**
14. $G$ has the GQL form, linear in $u$: $D>0$ and $E-m\cdot v_*-D\sqrt{1-\lvert v_*\rvert^2}>0$ for all $v_*$ in the unit ball (Lemma 3.4, Eq. 48). **Proved**
15. For admissible $u$: $0<c<\sqrt{\gamma-1}$, $v_n<\lambda_4<1$ and a bound on $v_n/(\lambda_4-v_n)$ (Lemma 3.5, Eqs. 49–51). **Proved**
16. For $\lambda\ge\lambda_4$, $-(n\cdot f(u))\cdot n_*>-\lambda\,u\cdot n_*$ with $n_*=\big(-\sqrt{1-\lvert v_*\rvert^2},-v_*,1\big)^\top$; the proof uses $\gamma\le2$ (Lemma 3.6, Eq. 52). **Proved**
17. The HLL flux satisfies $-\hat f^{\mathrm{HLL}}\cdot n_*\ge-\max_{u\in\{u^\pm\}}a(u;n)\,u^-\cdot n_*$ and the analogous density bound (Lemma 3.7, Eqs. 54–55). **Proved**
18. Main theorem: if the reconstructed and limited polynomial is in the PCP set, the forward-Euler cell average is in $G$ under $\Delta t\,a^{(j)}_K\lvert E^j_K\rvert/\lvert K\rvert\le\varpi=\tfrac23\hat\omega_1$, with $\hat\omega_1=1/(L(L-1))$, $L=\lceil(k+3)/2\rceil$ ($\varpi=1/9$ for the quadratic reconstruction); SSP-RK3 is PCP by convexity (Theorem 3.1, Eq. 57). **Proved**
19. Lax–Friedrichs and HLLC fluxes "also meet the PCP property (22) in this framework" (§3.1). **Stated** (not proved here)
20. The one-step operator is homogeneous, $\frac1\sigma S_h(\sigma u)=S_h(u)$ (Theorem 3.2, safety margins ignored). **Proved**
21. In the axisymmetric extension PCP holds under a two-part time-step bound and a limiter that also enforces admissibility at the interior quadrature points (§3.7, Eqs. 62–63). **Stated** ("one can deduce")
22. Third order on the relativistic isentropic vortex: for boost $0.5\sqrt2$ and $\mathcal E=5$ the $l^1$ and $l^2$ orders reach 2.9971 and 3.0015 on 238592 cells without limiting (Table 1); for $\mathcal E=10.0828$ they reach 3.05 and 3.07 while the limited-cell fraction falls from 1.502% to 0.000% (Table 2). **Shown**
23. On the scaled Riemann problem III ($\sigma=10^{-2},10^{-4}$) the new weights keep $\rho^{(\sigma)}_h-\sigma\rho_h$ at $O(10^{-12})$–$O(10^{-13})$; the Zhu–Qiu weights give $O(10^{-1})$ and $O(10^{-2})$ and overshoot (Example 4.4, Figs. 6–8). **Shown**
24. On the multi-scale four-state problem the Zhu–Qiu weights undershoot at the stationary contact and at the moving contact; the new weights do not (Example 4.5, Fig. 9). **Shown**
25. Without the PCP limiter the code fails on Riemann problem II, the jet, both 2D Riemann problems, the forward-facing steps and the strong vortex and shock–vortex cases (Examples 4.3, 4.6, 4.7, 4.9, 4.10, 4.12). **Shown**
26. On one core of an Intel i7-8700K the hybrid root finder takes 8.7–13.9% of the CPU time, against 15.4–23.0% for Newton, 14.6–17.1% for bisection and 14.0–27.4% for the fixed point; the three provable algorithms never failed (Table 3, Remark 4.1). **Shown**
27. The axisymmetric relativistic jet at relativistic Mach number about 41.95 is captured with no carbuncle (Example 4.12). **Shown**

# Printed slips

- p. 13, after Eq. 30: the basis function is printed $\psi_5=\frac{(y-y_0)^2}{\lvert K_0\rvert}-\frac1{\lvert K_0\rvert^2}\iint_{K_0}(y-x_0)^2\,dx\,dy$; the integrand must be $(y-y_0)^2$ for zero mean.
- Example 4.1: the text (p. 31) gives the errors "at $t=1$", the captions of Tables 1–2 "at $t=0.15$".
- Example 4.1 states no adiabatic index, so the default $\gamma=5/3$ of §4 applies; with it and $\mathcal E=10.0828$ the centre value $1-\alpha e$ of the density formula is $-0.40$ and $\rho$ is undefined, whereas $\gamma=1.4$ gives $\rho_{\min}=7.83\times10^{-15}$ and $p_{\min}=1.78\times10^{-20}$, the printed minima. The strong case must use $\gamma=1.4$ (as Example 4.10 states for its vortex); the mild case is undetermined. *(compiler check, not in the sources: evaluation of the printed initial data at $r=0$ for both values.)*
- Fig. 9 caption reads "Example 4.4"; the figure belongs to Example 4.5.
- Proof of Lemma 3.7 (p. 27): "$-U^\pm\cdot\xi_*>0$"; by Lemma 3.4 it is $u^\pm\cdot n_*>0$, the sign the subsequent inequalities use.
- §3.7, Eq. 60 (p. 30): the axisymmetric source is printed $S=\frac1r(Dv_1,m_1v_1,m_2v_1,m_1)^\top$ for $\partial_tu+\partial_rF_1+\partial_zF_2=S$. Writing $\frac1r\partial_r(rF_1)$ with the pressure gradient kept outside gives $S=-\frac1r(Dv_1,m_1v_1,m_2v_1,m_1)^\top$; the printed form lacks the minus sign. *(compiler check, not in the sources: cylindrical form of the paper's fluxes, Eqs. 4–5.)*
- Wording: "Homogeneousity" (§3.6 heading), "Reconstrucition" (Fig. 1), "spacial" (Remark 3.2), "Dubinar transform" (Remark 3.4, for the rectangle-to-triangle map of Zhang, Xia & Shu).
- Ref. [23] prints the author list "L. E. Kidder, S. E. Field, F. Foucart, and Erik", truncated.

# Notation map

| Chen & Wu (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U=(D,m,E)^\top$ | $u$ | conserved variables; $D=\rho W$, $m=\rho HW^2v$, $E=\rho HW^2-p$ kept |
| $W=(\rho,v,p)^\top$ | kept as primitive vector | **$W$ is the Lorentz factor in the registry** |
| $\gamma$ (Lorentz factor) | $W$ | **collides inside the source with the linear weights $\gamma_\ell$** |
| $\Gamma$ | $\gamma$ | adiabatic index, $\Gamma\in(1,2]$ |
| $H$, $e$, $c_s$ | $H$, $e$, $c$ | specific enthalpy $1+e+p/\rho$; sound speed $\sqrt{\gamma p/(\rho H)}$ |
| $G_u$, $G_u^{(1)}$, $G_u^{(2)}$, $G_w$ | $G$ | admissible set and its equivalent (GQL) forms; primitive set kept |
| $g(U)$ | kept as $E-\sqrt{D^2+\lvert m\rvert^2}$ | concave constraint; **$g$ is the mapped-WENO function and $g_i$ a constraint function in the registry** |
| $v_*$, $\xi_*$ | $v_*$, $n_*$ | free GQL parameter and the normal of the linear constraint $u\cdot n_*>0$ |
| $\Phi_U(p)$, $p_R^{(0)}$, $\delta$ | kept | pressure equation, bisection bracket, fixed-point rate; **$\delta$ collides with the TENO flag $\delta_k$** |
| $K$, $K_0$, $\lvert K\rvert$, $E^j_K$, $n^{(j)}_K$ | kept | triangles, target cell, area, edges, normals; **$K$ is the TENO stencil size in the registry, $E^j_K$ collides with the energy** |
| $\omega_q$, $x^{(jq)}_K$ | $\mathsf w_q$, kept | edge Gauss weights and points |
| $\hat\omega_1$, $\frac23\hat\omega_1$ | kept, $\varpi$ | first Gauss–Lobatto weight; the boundary weight of the cell-average decomposition |
| $k$ | kept | reconstruction degree ($k=2$, third order); **$k$ is the stencil index in the registry** |
| $\phi_2$, $\phi^{(\ell)}_1$ | $P_{\mathrm{opt}}$, $P_\ell$ | quadratic and linear polynomials of the CWENO-type combination |
| $N_0$; $N_1,\dots,N_4$ | $S_0$; kept | large 10-cell stencil, central and three sectorial stencils |
| $\gamma_\ell$ | $d_\ell$ | linear weights $0.96$, $0.01$ |
| $\beta_\ell$ | $\beta_\ell$ | Hu–Shu triangle indicators |
| $\tau=\frac14\sum_\ell\lvert\beta_0-\beta_\ell\rvert$ | $\tau$ | global indicator, unsubscripted on triangles; **this paper's $\tau^2$ is Zhu & Qiu's $\tau$** |
| $\delta_\ell$, $\varpi_\ell$ | $\alpha_\ell$, $\omega_\ell$ | **$\varpi$ is the cell-average-decomposition boundary weight in the registry** |
| $\varepsilon$ (Eq. 32), $\varepsilon$ (Ex. 4.1) | $\epsilon$, $\mathcal E$ | solution-dependent regularization; vortex strength |
| $\theta_D$, $\theta_g$ | $\theta$ | Zhang–Shu scaling factors of the two steps |
| $\lambda^{(1)}_n,\dots,\lambda^{(4)}_n$, $R_n$, $R_n^{-1}$ | $\lambda_1,\dots,\lambda_4$, $R$, $L$ | eigenstructure in direction $n$ |
| $\sigma_l$, $\sigma_r$, $\hat\sigma(U;n)$ | $s^-$, $s^+$, $a(u;n)$ | HLL speeds (bounded by 0) and spectral radius |
| $\zeta$ | $\sigma$ | scaling constant of the homogeneity results |
| $S_t$, $S_h$, $L_K$, $\Pi_h$, $R^k_h$ | kept, $\mathcal L$ | exact and discrete one-step operators, spatial operator, limiter, reconstruction |
| $h$ | kept | boundary edge length labelling meshes |
| $\Theta$ | kept | fraction of limited cells |

# Reference list

73 printed references, numbered [1]–[73] in SIAM style and alphabetical order, all
parsed and merged complete into the [bibliography](/bibliography.md) with
`citedby` `chen-2022-b`. Same-author same-year works take suffixes in printed
order (Dumbser 2007, Wu 2017, 2018 and 2021, Zhang 2010, Zhu 2017 and 2018; [72]
Zhu & Qiu and [73] Zhu & Shu are `zhu-2018` and `zhu-2018-b`). [53] is an arXiv
preprint (arXiv:2111.04722), kept as its own entry; [34] (EASYMESH) is an undated
web page; [54] prints no volume; [23] prints a truncated author list. No printed
duplicates were found.

# Pages created or updated

Chunk 3 (2026-10-22), cited further in chunks 4–8 (2026-10-23). This source is cited on:

* [Bound preservation](/properties/bound-preservation.md)
* [Carbuncle phenomenon](/definitions/carbuncle-phenomenon.md)
* [Central WENO (CWENO)](/methods/cweno.md)
* [Characteristic decomposition](/methods/characteristic-decomposition.md)
* [Double Mach reflection](/benchmarks/double-mach-reflection.md)
* [Geometric quasilinearization (GQL)](/methods/geometric-quasilinearization.md)
* [High-Mach astrophysical jets](/benchmarks/high-mach-astrophysical-jet.md)
* [HLL-family approximate Riemann solvers](/methods/hll-riemann-solvers.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [Mach 3 forward-facing step](/benchmarks/forward-facing-step.md)
* [Multi-resolution WENO](/methods/multi-resolution-weno.md)
* [Optimal cell-average decomposition](/methods/optimal-cell-average-decomposition.md)
* [Scale and affine invariance](/properties/scale-invariance.md)
* [Shock diffraction](/benchmarks/shock-diffraction.md)
* [Shock–vortex interaction](/benchmarks/shock-vortex-interaction.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [Special relativistic hydrodynamics and MHD](/definitions/relativistic-hydrodynamics.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md)
* [WENO-Z weights](/methods/weno-z.md)
* [Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md)
