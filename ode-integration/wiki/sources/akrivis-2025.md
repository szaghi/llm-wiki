---
type: Source
title: "Akrivis et al. (2025) — Runge–Kutta Physics Informed Neural Networks: Formulation and Analysis"
description: "Defines PINNs whose time-discrete loss is the residual of a collocation Runge–Kutta or Galerkin time scheme, proves their stability and convergence for linear parabolic problems, and proves variable-step discrete maximal L2 regularity by energy techniques for cG, dG, Gauss, Radau IIA, Lobatto IIIA and all algebraically stable Runge–Kutta methods."
resource: "doi:10.1007/s00211-025-01501-7"
source_kind: paper
authors: [Akrivis G., Makridakis C.G., Smaragdakis C.]
year: 2025
venue: "Numer. Math. 157:1975-2016"
local_file: "/home/stefano/papers/mosaic/ode-integration/2025_Crossref_Numerische_Mathematik_Akrivis_RungeKutta_physics_informed_neural_networks_formulation_and.pdf"
tags: [runge-kutta, implicit, energy-method, stability, parabolic]
timestamp: 2026-10-20T16:00:00Z
---

# Summary

The paper defines Runge–Kutta physics-informed neural networks (RK-PINNs), a
family of [learned time integrators](/methods/learned-time-integrators.md).
The PINN residual loss is discretized in time not by random sampling but by
the pointwise form of a collocation Runge–Kutta or Galerkin time-stepping
method; spatial integrals may still be sampled (Sobol points). For
$y'=Ly+g$ with $-L$ coercive and self-adjoint, a network $v$ is interpolated in
time at auxiliary nodes into a continuous piecewise polynomial $\hat v$ of
degree $s$, and the loss is the squared residual
$\lVert\hat v_t-I_{s-1}L\hat v-I_{s-1}g\rVert^2$ integrated over $(0,T)$, plus an
$H^1$ initial term. Here $I_{s-1}$ interpolates at the $s$ collocation nodes. A
version with abstract projections covers
[collocation Runge–Kutta](/methods/fully-implicit-runge-kutta.md), continuous
Galerkin cG($s$) and discontinuous Galerkin dG($s-1$).

For linear parabolic problems the authors prove stability of the discrete loss
(equi-coercivity in the Γ-convergence sense) and convergence of the discrete
minimizers in $L^2(0,T;H^1)$, assuming the networks approximate smooth
functions. Stability rests on a discrete maximal $L^2$ regularity estimate.

Section 4, of independent interest for time integration, proves
[discrete maximal regularity](/results/discrete-maximal-regularity.md) in Hilbert
space by the [energy technique](/methods/runge-kutta-energy-method.md), for
**arbitrary variable steps**: an abstract theorem for methods of a pointwise
form under a one-sided condition, then cG, dG, Gauss (with equality) and
Radau IIA; Lobatto IIIA, through a new equivalence of its interpolant with a
modified cG($s-1$) method (claimed first estimates for this
[A-stable](/properties/a-stability.md) but not B-stable family); and all
algebraically stable Runge–Kutta methods. Kovács, Li & Lubich (2016) had the
$L^p$ results in UMD Banach spaces for constant steps only. Experiments
compare three-stage Gauss, Lobatto IIIA and Radau IIA RK-PINNs with uniform
time sampling on the two-dimensional [heat equation](/benchmarks/heat-equation.md)
(smooth and discontinuous data) and a wave equation. The RK-PINNs have smaller
misfit and conserve heat and energy better; for discontinuous data Gauss and
Lobatto oscillate near $t=0$ while Radau smooths, as the underlying schemes
do. The evidence is graphical; no convergence rates are reported.

# Version read

The file is the arXiv preprint arXiv:2412.20575v2 (18 January 2025), 35 pages
(text 1–31, references 31–35), all read, with visual checks of pp. 23, 25 and
28–31; it is not the Numer. Math. typeset (42 journal pages). Title and
authors on page 1 match Crossref, whose title is in sentence case. Numbering
cited here is that of arXiv v2. Not to be confused with the ingested
[Akrivis et al. (2021)](/sources/akrivis-2021.md) and
[Akrivis et al. (2024)](/sources/akrivis-2024.md).

# Key claims

The source writes $u'+Au=f$ with $A$ coercive and self-adjoint; below this is
$y'=Ly+g$ with $-L=A$, $\lVert v\rVert_L=\lVert(-L)^{1/2}v\rVert$, steps
$h_n=t_{n+1}-t_n$, $s$ stages, stage values $Y_{n,i}$ at $t_{n,i}=t_n+c_ih_n$, and
$y_h$ the continuous piecewise-polynomial (collocation, Galerkin or
reconstructed) solution, page-local.

1. RK-PINN principle: the discrete loss is designed in a time-discrete framework and incorporates a Runge–Kutta or time-Galerkin discretization "in a carefully structured manner", so the methods "inherit the stability properties" of the underlying scheme (Abstract, §1, §2.4). **Stated** (supported by claims 6–17 and the experiments)
2. Earlier work showed that the backward-Euler time-discrete PINN loss (Eq. 14) gives stable and convergent approximations while the explicit-Euler analogue (Eq. 16) does not without a CFL-type condition (§2.3, §1). **Stated**; explicit Runge–Kutta losses are deliberately not computed.
3. The backward-Euler loss equals $\lVert\hat v_t-L\bar v-g\rVert^2_{L^2(0,T;L^2)}+\lvert\hat v(0)-y_0\rvert^2_{H^1}$ with $\hat v$ the piecewise-linear and $\bar v$ the piecewise-constant reconstruction (Eq. 19); this form is what generalizes to high order (§2.3). **Derived**
4. Collocation methods with $a_{ij}=\int_0^{c_i}\ell_j$, $b_i=\int_0^1\ell_i$ have [stage order](/definitions/stage-order.md) $s$, are equivalent to the continuous collocation polynomial at the nodes and stages, and have the pointwise form $y_h'=I_{s-1}Ly_h+I_{s-1}g$ on each step (Eqs. 22–24, 87–90). **Stated** (classical)
5. The losses $G_{RK}$ (Eq. 26) and $G_k$ (Eq. 28), with abstract projections $\Pi_{s-1}$, $\tilde\Pi_{s-1}$ onto discontinuous piecewise polynomials of degree $s-1$, define the RK-PINN and generalized RK-PINN methods (Eqs. 27, 29) (§2.4.2–2.4.3). **Derived** (definition)
6. Proposition 2: if the maximal regularity estimate (37) holds, a bounded loss $G_k(v)\le C$ bounds $\lVert\bar v\rVert_{L^2(H^2)}+\lVert\hat v'\rVert_{L^2(L^2)}$ uniformly (stability property [S1]) (§3.1.1). **Proved**
7. Lemma 3 (liminf inequality): if the quadrature of $\Pi_{s-1}$ integrates the continuous piecewise polynomials of degree $s$ exactly (Eq. 41) and $v_\ell\to\tilde v$ in $L^2(H^1)$, then $G(\tilde v)\le\liminf G_\ell(v_\ell)$ (§3.2). **Proved**
8. Lemma 4 (limsup inequality): if the time interpolation is Lagrange interpolation at $s+1$ points including both endpoints (Eq. 49), every sufficiently regular $w$ has a recovery sequence $w_\ell$ in the network spaces with $G(w)=\lim G_\ell(w_\ell)$ (§3.2). **Proved** (under the approximability assumptions 33–34)
9. Theorem 7: minimizers $v_\ell$ of $G_\ell$ satisfy $\hat v_\ell\to y$ in $L^2(0,T;H^1(\Omega))$ for the whole sequence, for convex Lipschitz $\Omega$ and maximal step $\to0$ (§3.2, via Aubin–Lions). **Proved**
10. Theorem 8: any method of the pointwise form $y_h'-\Pi_{s-1}Ly_h=\tilde\Pi_{s-1}g$ (Eq. 66) whose projection satisfies $-\int_{t_n}^{t_{n+1}}(y_h',\Pi_{s-1}Ly_h)\,dt\ge\frac12\big(\lVert y_h(t_{n+1})\rVert_L^2-\lVert y_h(t_n)\rVert_L^2\big)$ (Eq. 67) satisfies $\lVert y_h(t_m)\rVert_L^2+\lVert y_h'\rVert^2_{L^2(0,t_m;H)}+\lVert\Pi_{s-1}Ly_h\rVert^2_{L^2(0,t_m;H)}\le\lVert y_h(0)\rVert_L^2+\lVert\tilde\Pi_{s-1}g\rVert^2_{L^2(0,t_m;H)}$ (Eq. 68) for arbitrary partitions (§4.2). **Proved**
11. Proposition 9: cG($s$) satisfies (67) with equality, hence the discrete maximal regularity identity (74), in which the $L^2$ projection restricted to degree $s$ is interpolation at the $s$ Gauss points (Eq. 73), and the bound (76) with $\lVert g\rVert$ on the right (§4.3.1). **Proved**
12. Proposition 10: dG($s-1$), through the Makridakis–Nochetto reconstruction at Radau nodes, satisfies (67) and hence (84)–(85) (§4.3.2). **Proved**
13. Propositions 11–12: Gauss and Radau IIA collocation satisfy discrete maximal regularity (91), equivalently in nodal form $\lVert y_m\rVert_L^2+\sum_nh_n\sum_ib_i\lVert y_h'(t_{n,i})\rVert^2+\sum_nh_n\sum_ib_i\lVert LY_{n,i}\rVert^2\le\lVert y_0\rVert_L^2+\sum_nh_n\sum_ib_i\lVert g(t_{n,i})\rVert^2$ (92), with **equality for Gauss** (§4.4.1). **Proved**
14. Lobatto IIIA: the degree-$(s-1)$ interpolant of the Lobatto IIIA collocation solution solves a modified cG($s-1$) method with forcing $I_{s-1}g$ (Eq. 95), a connection presented as new (§4.4.2). **Proved**
15. Proposition 13: Lobatto IIIA satisfies the identity (99) and bound (100), "the first maximal regularity estimates in the literature" for this A-stable, not B-stable class with singular coefficient matrix (§1, §4.4.2). **Proved** (priority **Stated**)
16. Remark 14: for the trapezoidal rule (Lobatto IIIA, $s=2$) the estimate holds as an **equality** for arbitrary partitions, $\lVert y_m\rVert_L^2+\sum_nh_n\big\lVert\frac{y_{n+1}-y_n}{h_n}\big\rVert^2+\sum_nh_n\big\lVert\frac{Ly_{n+1}+Ly_n}2\big\rVert^2=\lVert y_0\rVert_L^2+\sum_nh_n\big\lVert\frac{g(t_{n+1})+g(t_n)}2\big\rVert^2$ (Eq. 101); Kovács, Li & Lubich (2016, Thm 3.2) prove only an inequality, for constant steps (but for any $p\in(1,\infty)$ and UMD spaces) (Remark 15). **Derived** / comparison **Stated**
17. Every algebraically stable Runge–Kutta method (equivalent to B-stable for distinct nodes, as stated) satisfies the nodal estimate of claim 13 as an inequality, for variable steps (Eq. 111); the proof applies $(-L)^{1/2}$ to the stage equations and uses positive semidefiniteness of $\operatorname{diag}(b)A+A^\top\operatorname{diag}(b)-bb^\top$ (§4.4.3, Eqs. 105–110). **Proved**
18. The Section 4 estimates hold for variable steps, generalizing Kovács, Li & Lubich (2016), where constant steps were "a key assumption", and give energy-based proofs of their Hilbert-space results (Abstract, §1, §4). **Proved** (estimates) / **Stated** (comparison)
19. Setup: three-stage Gauss, Lobatto IIIA ($c=(0,\tfrac12,1)$) and Radau IIA; auxiliary nodes $(0,\tfrac14,\tfrac12,1)$ for Gauss and Lobatto and $(0,\frac{4-\sqrt6}{10},\frac{4+\sqrt6}{10},1)$ for Radau; uniform sampling gets four times as many time points; DGM network, 4 hidden layers of 20 units, Adam with rate $3\cdot10^{-4}$, 20,000 (heat) or 100,000 (wave) epochs, 40 time nodes, 256 Sobol points per epoch (§5.4). **Stated**
20. Heat equation, smooth initial datum: the RK-PINN misfit at the final time is visibly smaller than with uniform sampling (Fig. 1); total heat stays near 0.0095–0.0103 for the RK schemes while uniform sampling drifts from about 0.0105 to about 0.0078 (Fig. 2, values read off the plot) (§5.4.1). **Shown**
21. Heat equation, discontinuous initial datum: the RK schemes again beat uniform sampling in misfit (Fig. 3) and heat conservation (about 0.033–0.036 against a decay from about 0.038 to 0.024, Fig. 4, read off the plot) (§5.4.2). **Shown**
22. Smoothing: for discontinuous data the Gauss and Lobatto RK-PINNs oscillate close to $t=0$ (slices at $x=0.6$, $t=0.002$ and $0.008$) while Radau IIA smooths fully, "as expected" from the smoothing behaviour of the underlying schemes (Luskin–Rannacher, Thomée) (§5.4.2, Fig. 5). **Shown**
23. Wave equation: Gauss and Lobatto conserve energy best (about 0.45 to 0.43 over 40 steps), Radau IIA decays more (0.44 to 0.40), uniform sampling most (0.44 to 0.36) (Fig. 7, read off the plot); misfit against an 8-term separation-of-variables solution in Fig. 6 (§5.4.3). **Shown**
24. Because only time is meshed, the approach is "particularly well-suited for high-dimensional evolution problems" (§1, §2.3). **Stated** (no high-dimensional test)
25. The convergence theory for hyperbolic (wave) problems "remains to be developed"; the wave equation is treated as a first-order system (§1). **Stated**

Akrivis et al. state (§4.4.3) that, the nodes being pairwise distinct,
B-stability is equivalent to algebraic stability (105), and they write the
stage increments through the collocation polynomial, $h_ny_h'(t_{n,i})$
(Eqs. 86, 90). For a method that is not of collocation type, $y_h'(t_{n,i})$
in (111) is to be read as $LY_{n,i}+g(t_{n,i})$; the proof uses only the stage
equations, so the estimate holds with that reading *(compiler check, not in
the sources)*.

# Printed slips

- Eq. (118): the sum over $i$ evaluates at $\tilde t_{nj}$ instead of $\tilde t_{ni}$ (as in Eq. 117), and its minus sign contradicts the residual $\hat u_t+I_{q-1}L\hat u$ of Eqs. (116)–(117).
- Theorem 7 refers to "the energy functionals defined in (31) and (14)", where (14) is the backward-Euler loss; Eq. (60) takes an infimum over an undefined "$W_\ell$"; Eq. (51) keeps the backward-Euler label "$G_{IE,\ell}$".
- Lemma 4 refers to itself ("can be represented as (49); see (49)"); §3.1 and Proposition 2 cite "(3.1)" for the loss defined in Eq. (28).
- Eq. (62) prints one $L^2(H^2)$ term twice with different accents.
- §4.2: "$J_n:=(t_n,t_{n+1}]$, $n=0,\dots,N$" (should end at $N-1$); §4.4.2: "since $c_0=0$" for $c_1=0$; Eq. (109): "$k(f(t_{ni}),AU_{ni})$" for $k_n$.
- Remark 15: "Lobatto IIA" for Lobatto IIIA; Remark 16: "it $\tilde U$ is available" for "if".
- Figs. 1 and 3 label panels "t = 2" for problems posed on $[0,1]$, and do not state the reference solution of the heat-equation misfit; captions of Figs. 3, 4 and 6 speak of "iterative schemes".
- Typos: "auxiliary modes" (§5.4), "colocation" (§5.2), "form the Neumann" (§5.4.1).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u$, $u_0$ | $y$, $y_0$ | solution and initial datum |
| $L$ (§§2–3), $A$ (§§4–5); $u'+Au=f$ | $-L$; $y'=Ly+g$ | coercive self-adjoint operator; **$A$ collides** with the Butcher matrix; the forcing $f$ is written $g$ (**collision** with the right-hand side $f$) |
| $\lvert A^{1/2}v\rvert$ | $\lVert v\rVert_L=\lVert(-L)^{1/2}v\rVert$ (page-local, as on the result pages) | energy norm |
| $(\cdot,\cdot)$, $\lvert\cdot\rvert$ | $\langle\cdot,\cdot\rangle$, $\lVert\cdot\rVert$ | Hilbert space $H$ |
| $k_n=t_{n+1}-t_n$, $k$ | $h_n$, $h$ | variable steps; **$k$ collides** with the multistep step count |
| $J_n=(t_n,t_{n+1}]$ | — | step interval; distinct from the Jacobian $J$ |
| $q$ | $s$ | number of stages and nodes; **collides** with the stage order $q$ (here stage order $=s$) |
| $c_i$, $t_{ni}$ | $c_i$, $t_{n,i}=t_n+c_ih_n$ | collocation nodes and stage times |
| $a_{ij}$, $b_i$, $\mathcal O=(a_{ij})$ | $a_{ij}$, $b_i$, $A$ | Butcher coefficients and matrix |
| $M=(m_{ij})$ | $\operatorname{diag}(b)A+A^\top\operatorname{diag}(b)-bb^\top$ | algebraic-stability matrix; **$M$ collides** with the mass matrix |
| $U_n$, $U_{ni}$ | $y_n$, $Y_{n,i}$ | step and stage values |
| $\hat U$ | $y_h$ (page-local) | continuous piecewise-polynomial solution; **$\hat U$ would collide** with the embedded solution $\hat y$ |
| $\bar U=\Pi_{q-1}\hat U$, $\tilde U=I_{q-1}\hat U$ | $\Pi_{s-1}y_h$, $I_{s-1}y_h$ | discontinuous interpolant; continuous interpolant (Lobatto IIIA) |
| $\ell_i$, $\tilde c_j$, $\tilde t_{nj}$, $\tilde\ell_{ni}$ | — | Lagrange basis at the nodes; auxiliary nodes and basis for interpolating the network |
| $I_{q-1}$, $\hat I_q$, $\hat\Pi_q$, $\Pi_{q-1}$, $\tilde\Pi_{q-1}$, $P_{q-1}$, $I_{G,q-1}$ | $I_{s-1}$, $\hat I_s$, $\hat\Pi_s$, $\Pi_{s-1}$, $\tilde\Pi_{s-1}$, $P_{s-1}$, $I_{G,s-1}$ (page-local) | interpolation and projection operators; **$P$ collides** with the stability polynomial |
| cG($q$), dG($q-1$) | cG($s$), dG($s-1$) | continuous and discontinuous Galerkin time stepping; dG($s-1$) matches $s$-stage Radau IIA at the nodes |
| $E$, $G$, $G_{k,IE}$, $G_{k,EE}$, $G_{RK}$, $G_k$, $G_\ell$ | — | continuous and discrete PINN losses; **$G$ collides** with the G-norm matrix |
| $V_{\mathcal N}$, $V_\ell$, $\theta$, $\beta_\ell$ | — | network spaces, parameters, approximation rates |
| $\varphi_j=-k_n\hat U'(t_{nj})$ | $-h_ny_h'(t_{n,j})$ | stage increments of the algebraic-stability proof; **$\varphi$ collides** with the exact flow |
| $\zeta$ | — | time-discrete residual |
| MR | — | maximal regularity |

# Reference list

The paper prints 52 references in numbered style ([1]–[52]), ordered
alphabetically. The list is merged complete into the
[bibliography](/bibliography.md), with `citedby` this slug. Same-author
same-year pairs are suffixed in printed order (Makridakis 2024 [37], [38]:
`makridakis-2024`, `makridakis-2024-b`; Shin 2020 [45], [46]: `shin-2020`,
`shin-2020-b`). Four items match works already in the bibliography under
suffixed keys (`biswas-2022-b`, `butcher-1996-b`, `chen-2022-c`,
`xu-2020-b`). Ref. [17] is De Giorgi's selected papers (Springer 2013
reprint) and ref. [27] a chapter title within the Hairer–Lubich–Wanner book,
both encoded as books; ref. [15] (Crouzeix, LNEMS 134) is a collection chapter;
ref. [16] prints the C. R. volume as "28.6 (1976)" and ref. [25] as "3.Sér
(1969)", kept as printed. Ref. [30] is Kovács, Li & Lubich (2016), SIAM J.
Numer. Anal. 54:3600–3624. No DOIs are printed. No printed duplicates; all
items parsed.

# Pages created or updated

Chunk 6 (2026-10-20). This source is cited on:

* [A-, L-, A(α)- and algebraic stability](/properties/a-stability.md)
* [Discrete maximal regularity of variable-step Galerkin and Runge–Kutta time stepping](/results/discrete-maximal-regularity.md)
* [Energy method for Runge–Kutta stability](/methods/runge-kutta-energy-method.md)
* [Fully implicit collocation Runge–Kutta methods (Gauss, Radau IIA, Lobatto IIIC)](/methods/fully-implicit-runge-kutta.md)
* [Heat equation](/benchmarks/heat-equation.md)
* [Learned time integrators: neural surrogates and physics-informed Runge–Kutta networks](/methods/learned-time-integrators.md)
* [Stage order](/definitions/stage-order.md)
