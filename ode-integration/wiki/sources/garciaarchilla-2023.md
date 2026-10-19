---
type: Source
title: "García-Archilla & Novo (2023) — Robust error bounds for the Navier–Stokes equations using implicit-explicit second-order BDF method with variable steps"
description: "Proves viscosity-independent second-order error bounds for fixed- and variable-step BDF2 with grad-div stabilized mixed finite elements for Navier–Stokes, with explicit convection (needing a time step bounded by the squared mesh width) or linearly implicit convection (no such restriction), and confirms the restriction in adaptive runs."
resource: "doi:10.1093/imanum/drac058"
source_kind: paper
authors: [García-Archilla B., Novo J.]
year: 2023
venue: "IMA J. Numer. Anal. 43:2892-2933"
local_file: "/home/stefano/papers/mosaic/ode-integration/2022_Crossref_IMA_Journal_of_Numerical_Analysis_García-Archilla_Robust_error_bounds_for_the_NavierStokes_equations_using_imp.pdf"
tags: [linear-multistep, bdf, imex, step-size-control, energy-method, cfd]
timestamp: 2026-10-19T23:00:00Z
---

# Summary

The paper analyses fully discrete approximations of the incompressible
Navier–Stokes equations: inf-sup stable mixed finite elements with
grad-div stabilization in space, and two second-order
[BDF](/methods/backward-differentiation-formula.md) (BDF2) time integrators
with implicit viscous, pressure and grad-div terms, in fixed-step and
variable-step form. In the [IMEX](/methods/imex-linear-multistep-methods.md)
variant the convective term is fully explicit, evaluated at the linear
extrapolation of the last two steps. In the semi-implicit variant it is
linearized, with the extrapolated velocity advecting the new one. Both
need one linear system per step; the first step is IMEX Euler, at no loss
of order.

The main results are error bounds of order $h^2$ in time and optimal order
in space whose constants do not depend on inverse powers of the viscosity,
so they hold at high Reynolds number. For the IMEX method the proof needs
the time step bounded by a constant times $\Delta x^2$, free of the
viscosity, where DeCaria and Schneier needed a bound on $h/(\Delta x\,\nu_{\mathrm v})$.
The semi-implicit method needs no such condition. The variable-step
analysis rests on a perturbed G-norm energy inequality
([G-stability](/properties/g-stability.md)-type) for
[variable-step BDF2](/results/variable-step-bdf2-stability.md), a bound
on the step ratio $r_n$ from a quartic polynomial ($>1.25$ to $>2.61$
depending on a free parameter) and a bound on the total variation of the
ratios. The authors claim the first analysis of variable-step BDF2 for
Navier–Stokes.

The experiments (Matlab, P2/P1) use the variable-order BDF1/BDF2
[step-size control](/methods/step-size-control.md) of Hairer and Wanner,
with the error estimator of the fully implicit BDF applied unchanged to
both schemes, and [linear solves](/methods/implicit-stage-solvers.md) by
iterative refinement with reused factorizations. On a manufactured
solution with viscosity down to $10^{-10}$ the spatial error is
viscosity-independent. At fixed tolerance, the IMEX step count grows under
mesh refinement while the semi-implicit one does not, and on the
[flow past a cylinder](/benchmarks/flow-past-cylinder.md) the IMEX steps
are limited by stability rather than accuracy. The authors read both as
evidence that the $h\lesssim\Delta x^2$ restriction is real.

# Version read

The file is the arXiv preprint arXiv:2112.12446v1 [math.NA], 23 December
2021 (title page dated 24 December 2021), 31 pages, all read; it is not the
version of record, despite the "Crossref" in the archive filename. The
journal version spans 42 pages (2892–2933) and may differ in numbering and
content. It appeared online in 2022 and in the 2023 issue; the slug and
`year` follow the issue. The preprint title writes "Navier-Stokes" and
"second order"; Crossref has "Navier–Stokes" and "second-order", a
typographic difference only. Numbering cited here is that of arXiv v1.

# Key claims

Here $h_n$ is the time step, $\Delta x$ the mesh width, $\nu_{\mathrm v}$
the kinematic viscosity, $\mu_{\mathrm{gd}}$ the grad-div parameter,
$\ell_u$ and $\ell_p$ the velocity and pressure degrees and $e_n$ the
discrete velocity error against a Stokes-type projection.

1. Fixed-step IMEX BDF2 (Eq. 20) satisfies $\lVert e_{n+1}\rVert_0^2+\sum_{j=2}^{n+1}\nu_{\mathrm v}h\lVert\nabla e_j\rVert_0^2+\mu_{\mathrm{gd}}\sum_{j=2}^{n+1}h\lVert\nabla\cdot e_j\rVert_0^2\le e^{8(\kappa+1)+2T\max_jM^j}\big((C_0^2+TC_3^2)h^4+T(C_1^2\Delta x^{2\ell_u}+C_2^2\Delta x^{2\ell_p+2})\big)$ for $\Delta x<\Delta x_0$, under the condition $64c_{\mathrm{inv}}^2\lVert u\rVert^2_{L^\infty(L^\infty)}h/\Delta x^2\le\kappa/T$ (Eq. 44) and $h\big(4(\kappa+1)/T+M^j\big)\le\frac12$ (Eq. 45); no constant depends on $\nu_{\mathrm v}^{-1}$ (Thm. 1, Eqs. 44–46). **Proved**
2. Fixed-step semi-implicit BDF2 (Eq. 22) satisfies the same bound with $\kappa=0$ under only a viscosity-independent smallness condition on $h$, with no condition linking $h$ and $\Delta x$ (Thm. 2). **Proved**
3. Hence $\max_n\lVert u_h^n-u^n\rVert_0=O(h^2+\Delta x^{\ell_u}+\Delta x^{\ell_p+1})$, second order in time; Taylor–Hood elements give order $\ell_u$ in space (Remarks 4 and 6). **Proved**
4. With variable steps, ratio bounds $r_{\min}\le r_n\le r_{\max}$ (Eq. 19), $r_{\max}\le r^*_{\max}(a)$ (Eq. 84) and $\sum_{n=2}^{N-1}(\lvert r_{n-1}-1\rvert+\lvert r_n-1\rvert)\le\Lambda$ (Eq. 85), the IMEX method satisfies a bound of the same form on $G_{n+1}$ plus the dissipation sums, with $h=\max_nh_n$, under a condition $h_n/\Delta x^2\le$ const involving $r_{\min}$ and $r_{\max}$ (Eq. 86) and a smallness condition (Eq. 87) (Thm. 3, Eqs. 86–89). **Proved**
5. The variable-step semi-implicit method satisfies the same bound under Eq. 87 alone (Thm. 4). **Proved**
6. Lemma 7: $h_n(\mathcal De_{n+1},e_{n+1})\ge G_{n+1}-G_n+\frac{r_n}{2(1+r_n)}\lVert e_{n+1}-\hat e_n\rVert_0^2-\frac{K_0}{r_{\min}}(1+r_{\max})^2(\lvert r_{n-1}-1\rvert+\lvert r_n-1\rvert)G_n$, with $G_n=\frac{r_{n-1}}{2(1+r_{n-1})}\lVert e_n\rVert_0^2+\frac14\lVert 2e_n-e_{n-1}\rVert_0^2$ and $K_0\le75/14$ (Lemma 7, Eqs. 69–70). **Proved**
7. $G_n\ge\frac{0.07}{1+r_{\max}}r_{n-1}(\lVert e_{n-1}\rVert_0^2+\lVert e_n\rVert_0^2)$, from the smallest eigenvalue of a $2\times2$ matrix bounded below by $0.14x$ on $[0,1/2]$ (Eqs. 80–81, Fig. 1). **Proved** (the eigenvalue bound is checked graphically)
8. The quartic of Eq. 83 has one positive root $r^*_{\max}(a)$, increasing in the free parameter $a\in[1,10]$, with $r^*_{\max}>1.25$, $2.12$, $2.61$ for $a=1,5,10$; larger $a$ allows larger step increases but enlarges the error constant (Eqs. 83–84, 99, Remark 5). **Derived**
9. The term $2\lVert\hat u_h^n\rVert_\infty c_{\mathrm{inv}}\Delta x^{-1}\lVert e_{n+1}-\hat e_n\rVert_0\lVert e_{n+1}\rVert_0$ from the explicit convection is the sole origin of the $h\lesssim\Delta x^2$ condition; it is absent for the semi-implicit treatment (Lemmas 3–4, Remark 2). **Proved**
10. The IMEX condition bounds $h/\Delta x^2$, stronger than the usual $h/\Delta x$ but better than DeCaria and Schneier's bound on $h/(\Delta x\,\nu_{\mathrm v})$, so the method runs at high Reynolds number without reducing the step (§1, Remark 3, §5). **Stated**
11. A condition bounding $h/(\Delta x\,\nu_{\mathrm v})$ with a weaker norm of $u$ could be obtained as in DeCaria–Schneier; it is left aside because it is not robust in $\nu_{\mathrm v}$ (Remark 3). **Stated**
12. The constant $\kappa$ of the step condition enters the error bound as $\exp(8(\kappa+1))$ (fixed step) or $\exp(\kappa\sigma(1+r_{\max})/0.07)$ (variable step) (Remarks 3 and 5). **Derived**
13. No earlier error analysis of variable-step BDF2 for Navier–Stokes exists; variable-step BDF2 was analysed for linear and semilinear parabolic, monotone-potential and Cahn–Hilliard problems (§§1, 5). **Stated**
14. Manufactured solution (P2/P1, $\mu_{\mathrm{gd}}=0.05$, $T=4$): the velocity error decays as $O(\Delta x^2)$ independently of the viscosity for $\nu_{\mathrm v}=10^{-6},10^{-8},10^{-10}$, whose curves coincide; for $\nu_{\mathrm v}=10^{-2}$ the slope is close to 4 (supraconvergence) (§4.1, Fig. 2). **Shown**
15. Adaptive steps at $\nu_{\mathrm v}=10^{-6}$, $\mathrm{rtol}=10^{-5}$: step lengths between about 0.001 and 0.005 after start-up, with very few rejections (§4.1, Fig. 3). **Shown**
16. The number of LU factorizations is at worst "hardly more than 5%" of the number of steps and barely grows as the mesh and tolerance decrease (§4.1, Fig. 4). **Shown**
17. At fixed $\mathrm{rtol}=10^{-4}$ the IMEX step count roughly doubles from $\Delta x=1/24$ to $1/48$ and triples from $1/48$ to $1/96$ for the three smallest viscosities, "approaching the factor 4 predicted by" Eq. 86; the semi-implicit count stays roughly constant (§4.1, Fig. 5). **Shown**
18. Flow past a cylinder ($\nu_{\mathrm v}=10^{-3}$, $\mu_{\mathrm{gd}}=0.01$, 27168 velocity and 3480 pressure dofs): at $\mathrm{rtol}=10^{-4},10^{-6},10^{-8}$ the IMEX method takes 11221, 21187 and 93671 steps, the semi-implicit 4384, 19885 and 92086; factorizations number 67, 53, 92 and 72, 84, 89 (§4.2). **Shown**
19. On the cylinder the IMEX step sizes at $\mathrm{rtol}=10^{-4}$ and $10^{-6}$ coincide on $t\in[1.7,3.7]$ and are smaller than the semi-implicit ones: the step is limited by Eq. 86, not by accuracy (§4.2, Fig. 8). **Shown**
20. Cylinder accuracy (IMEX, $\mathrm{rtol}=10^{-4}$): times of maximum drag and lift within relative error 0.0006; maximum drag and lift within 0.012 and 0.043 of the references 2.950921575 and 0.47795; pressure difference at $t=8$ within 0.002 of $-0.1116$ (§4.2, Fig. 9). **Shown**
21. The semi-implicit method costs "not much" more than the IMEX one and has no step restriction (§4.2, §5). **Shown**

# Printed slips

- §1: "we add grad-did stabilization".
- Eq. 19 is stated for "$n=0,1,\dots,N-1$", but $\omega_n$ is defined only for $n\ge1$ (p. 6); Eqs. 104–105 nevertheless use $\omega_0$.
- p. 18: $\Delta t=\max_{1\le n\le N}\Delta t_n$, while $\Delta t_n$ is defined for $n=0,\dots,N-1$.
- Proof of Lemma 2, $n=0$: "$S_0\le(1+\gamma_0)^{-1}(c_0+B)$"; it should be $(1-\gamma_0)^{-1}=1+\sigma_0\gamma_0$.
- p. 8: "foruth"; the sentence "with the third and foruth terms replaced" should name the third term only.
- Fig. 2 caption: "Continuous lines correspond to method ((20) and continuous lines to method (22)"; the second should be "discontinuous".
- Eq. 113: unbalanced parenthesis in the first velocity component, "$8\sin^2(\pi x)(2y(1-y)(1-2y)$", and a literal "sin(2 ∗ πx)" in the second.
- Eqs. 65–66 and after 107: "$\|\hat s^n_h\|\le(7/2)\|u\|_{L^\infty(L^\infty)}$" omits the $\infty$ subscript.
- The abstract calls the velocity degree $r$, the body $k$.
- §4.1: measured growth factors of about 2 and 3 are described as "approaching the factor 4 predicted by" (86), an interpretation rather than a match.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Delta t_n=t_{n+1}-t_n$ | $h_n$ | $\Delta t=\max_n\Delta t_n$ (variable) or $T/N$ (fixed), written $h$ |
| $h$ | $\Delta x$ | mesh size; **collision** with the registry step $h$ |
| $\omega_n=\Delta t_n/\Delta t_{n-1}$ | $r_n$ | agree after renaming |
| $\gamma$, $\Gamma$ | $r_{\min}$, $r_{\max}$ | ratio bounds (Eq. 19); $\gamma_j$ also appears unrelated in the Gronwall lemmas |
| $\Gamma^*(\alpha)$, $\alpha\in[1,10]$ | $r^*_{\max}(a)$, $a$ | admissible ratio bound and its free parameter; **collision** with the multistep $\alpha_j$ |
| $\Lambda$ | $\Lambda$ | total variation bound of the ratios |
| $\nu$ | $\nu_{\mathrm v}$ | kinematic viscosity; **collision** with the Courant number $\nu$ |
| $\mu$ | $\mu_{\mathrm{gd}}$ | grad-div parameter; **collision** with the multipliers $\mu_j$ |
| $k$, $l$ | $\ell_u$, $\ell_p$ | velocity and pressure degrees; **collision**: $k$ is the registry step count |
| $u$, $p$ | $u$, $p$ | velocity and pressure (PDE variables); **collision**: $p$ is the order |
| $e_h^n=s_h^n-u_h^n$ | $e_n$ | discrete error against the Stokes projection $s_h$ |
| $Du^n$, $\hat u^n=u^n+\omega_nDu^n$ | —, $\hat u^n$ | backward difference and linear extrapolation to $t_{n+1}$ |
| $\mathcal Du^n$ | $\mathcal D$ | variable-step BDF2 difference; fixed step $\frac32u^n-2u^{n-1}+\frac12u^{n-2}$ |
| $G_n$ | $G_n$ | energy functional quadratic in $(e_n,e_{n-1})$, a variable-step G-norm; distinct from the matrix $G$ |
| $c_{\mathrm{inv}}$, $\kappa$ | $c_{\mathrm{inv}}$, $\kappa$ | inverse-inequality constant and free step-condition constant |
| $K_0$ | $K_0$ | Lemma 7 constant, not an iteration count |
| $M^k$, $N^k$, $L_h^n$, $f_n$, $m_k$, $\sigma$, $\sigma_n$, $C_n$ | — | Gronwall and theorem constants ($\sigma>1$ fixed in Thm. 3); $M$ **collides** with the mass matrix, $\sigma$ with the generating polynomial $\sigma(\zeta)$ |
| $\mathrm{EST}_n$, $\mathrm{TOL}_n$, $TOL_r$ | $\mathrm{err}_n=\mathrm{EST}_n/\mathrm{TOL}_n$, $\mathrm{rtol}$ | accept iff $\mathrm{EST}_n\le\mathrm{TOL}_n$; controller $h_n^{\mathrm{new}}=0.9h_n(\mathrm{TOL}_n/\mathrm{EST}_n)^{1/(k+1)}$ with $k$ the BDF order |
| "IMEX" | — | in this paper only the fully explicit convection; the linearized variant is "semi-implicit" |

# Reference list

The paper prints 19 references in numbered style ([1]–[19]), ordered
alphabetically. The list is merged complete into the
[bibliography](/bibliography.md), with `citedby` this slug. No DOIs or arXiv
identifiers are printed. Ref. [12] (García-Archilla, John and Novo, CMAME)
is printed "to appear" with no year, volume or pages; it is its own
pre-publication entry `garciaarchilla-2021`, keyed by the year of the
version read. Ref. [19] (Schäfer et al., Vieweg+Teubner 1996) prints no
book title, and [9] prints its page count after the article number. No
printed duplicates; all items parsed.

# Pages created or updated

Chunk 3 (2026-10-19). This source is cited on:

* [Backward differentiation formulas (BDF)](/methods/backward-differentiation-formula.md)
* [Flow past a cylinder (Schäfer–Turek)](/benchmarks/flow-past-cylinder.md)
* [G-stability](/properties/g-stability.md)
* [IMEX linear multistep and IMEX-BDF methods](/methods/imex-linear-multistep-methods.md)
* [Linear multistep methods](/methods/linear-multistep-method.md)
* [Multiplier energy technique for multistep methods (Nevanlinna–Odeh multipliers)](/methods/multiplier-energy-technique.md)
* [Solving the stage equations of implicit Runge–Kutta methods](/methods/implicit-stage-solvers.md)
* [Stability of variable-step BDF2 under step-ratio bounds](/results/variable-step-bdf2-stability.md)
* [Step-size control: error-based controllers, PID filters and CFL control](/methods/step-size-control.md)
