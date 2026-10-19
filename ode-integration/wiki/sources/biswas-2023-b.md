---
type: Source
title: "Biswas & Ketcheson (2023) — Multiple-Relaxation Runge Kutta Methods for Conservative Dynamical Systems"
description: "Generalizes relaxation to several invariants: multiple-relaxation Runge–Kutta methods combine embedded weight vectors sharing one stage matrix, prove existence of the relaxation parameters and order recovery at a shifted time, and give linear error growth on rigid-body, Lotka–Volterra, Kepler and IMEX KdV tests."
resource: "doi:10.1007/s10915-023-02312-4"
source_kind: paper
authors: [Biswas A., Ketcheson D.I.]
year: 2023
venue: "J. Sci. Comput. 97:4"
local_file: "/home/stefano/papers/mosaic/ode-integration/2023_Crossref_Journal_of_Scientific_Computing_Biswas_Multiple-Relaxation_Runge_Kutta_Methods_for_Conservative_Dyn.pdf"
tags: [relaxation, structure-preserving, geometric-integration, embedded-pair, imex]
timestamp: 2026-10-19T20:00:00Z
---

# Summary

Single [relaxation](/methods/relaxation-runge-kutta.md) enforces conservation
of one functional $\eta$ by scaling the Runge–Kutta update with $\gamma_n$ and
reading the result at $t_n+\gamma_nh$. The paper extends it to $\kappa$
invariants $\eta=(\eta_1,\dots,\eta_\kappa)$. The multiple-relaxation
Runge–Kutta (MRRK) method takes $\kappa$ embedded methods that share the stage
matrix $A$, with weights $b^{(1)},\dots,b^{(\kappa)}$, and forms the directions
$d_k=\sum_jb^{(k)}_jf(t_n+c_jh,Y_j)$. It sets
$y^\gamma_{n+1}=y_{n+1}+h\sum_k\gamma_{n,k}d_k$, where $y_{n+1}$ is the first
method's solution. The $\kappa$ parameters solve the system
$\eta(y^\gamma_{n+1})=\eta(y_n)$, and the result is read at
$t_n+(1+\Gamma_n)h$ with $\Gamma_n=\sum_k\gamma_{n,k}$. No extra
right-hand-side evaluations are needed. The method resembles the directional
projection method of Calvo et al. but needs one fewer embedded method, at the
price of a modified step time.

Lemma 4.1 proves, by the implicit function theorem, that a unique set of
parameters with $\gamma_{n,k}=O(h^{p-1})$ exists for small $h$ when a leading
$\kappa\times\kappa$ matrix is nonsingular. Theorem 4.2 shows order $p-1$ at
$t_n+h$ and order $p$ at the shifted time.

The tests cover rigid-body rotation (two quadratic invariants), a
bi-Hamiltonian 3D Lotka–Volterra system (two Casimirs), the
[Kepler problem](/benchmarks/kepler-problem.md) with three invariants, and a
perturbed Kepler problem. MRRK conserves all invariants to rounding and turns
quadratic long-time error growth into linear growth. Section 6 combines
relaxation with Kennedy–Carpenter additive [IMEX](/methods/imex-runge-kutta.md)
methods on a mass- and energy-conserving Fourier semi-discretization of KdV,
which the authors claim is the first such combination. Energy relaxation
gives linear error growth for one soliton, intermediate growth for two, and
still quadratic (though smaller) growth for three. So mass and energy
conservation do not guarantee linear growth for multi-soliton data
([entropy stability and conservation](/properties/entropy-stability.md)).
Enforcing the Whitham invariant as well, which the semi-discretization does
not conserve, reduces its drift but not to rounding.

# Version read

The file is the arXiv preprint arXiv:2302.05235v1 [math.NA] (10 Feb 2023),
24 pages, in journal-submission format. It is not the version of record and
prints no DOI. Title and authors match Crossref (page 1 prints the title in
upper case). Numbering on this page is that of arXiv v1. The slug carries the
suffix `-b` because biswas-2023 is an earlier ingested paper of the same year.

# Key claims

Notation: $Y_j$ stage values; $b^{(k)}$ the weights of the $k$-th embedded
method, $p_k$ its order, $p=p_1$; $d_k$ the directions above; $D_n=[d_1|\dots|d_\kappa]$;
$\gamma_{n,k}$ the MRRK parameters (near 0; for $\kappa=1$, $\gamma_{n,1}$ equals
$\gamma_n-1$ of single relaxation).

1. All Runge–Kutta methods preserve linear invariants; only symplectic ones preserve quadratic invariants, and these are fully implicit; no Runge–Kutta method preserves all polynomial invariants of degree $\ge3$ (§1). **Stated**
2. Oblique projection (Dekker–Verwer modification, Calvo et al. directional projection, relaxation) keeps linear invariants while enforcing nonlinear ones, unlike orthogonal projection (§1). **Stated**
3. For an order-$p$ base method, single relaxation has a solution $\gamma_n=1+O(h^{p-1})$ under restrictions, and RRK has order $p$ at $t_n+\gamma_nh$ (§2, Eqs. 5c–6). **Stated** (prior work)
4. MRRK with $\kappa$ linearly independent embedded methods and update (11), with the parameters solving $\eta(y^\gamma_{n+1})=\eta(y_n)$, conserves $\kappa$ invariants; for $\kappa=1$ it reduces to relaxation, with the update based at $y_{n+1}$ rather than $y_n$ (§3, Eqs. 9–11). **Derived** (definition)
5. MRRK needs one fewer embedded method than directional projection for the same number of invariants but adjusts the step time (§3, §5). **Stated**
6. Lemma 4.1: if $(A,b^{(1)})$ has order $p\ge2$, $y_n=y(t_n)$, and $\eta'(y_{n+1})D_n=B_nh+O(h^2)$ with $B_n$ nonsingular, then there is $h^*>0$ such that for all $h\in[0,h^*]$ a unique parameter set satisfies (10)–(11), with $\gamma_{n,k}=O(h^{p-1})$ (§4, Eqs. 12–18). **Proved**
7. Theorem 4.2: with orders $p\ge2$ and $p_k\ge1$, and assuming $\gamma_{n,k}=O(h^{p-1})$, MRRK has order $p-1$ read at $t_n+h$ and order $p$ read at $t_n+(1+\Gamma_n)h$ (§4, Eqs. 19–21). **Proved**
8. Basing the update at $y_{n+1}$ instead of $y_n$ gives better robustness in finding the parameters (§5). **Shown** (asserted from experience, no figure)
9. Some methods need smaller steps for the parameters to exist at every step (§5). **Shown** (asserted)
10. Directional projection was also run and gave results comparable to MRRK (§5). **Stated** (no data)
11. Rigid body, $t_f=5$: SSPRK(2,2), Heun(3,3), RK(4,4), DP(7,5) and their MRRK versions converge, the MRRK versions above their theoretical orders (§5.1, Fig. 1). **Shown**
12. Rigid body up to $t=1000$: MRRK versions of Heun(3,3) ($h=0.04$), Fehlberg(6,4) and DP(7,5) ($h=0.1$) conserve both quadratic invariants to rounding; their error grows linearly, the baselines' quadratically (§5.1, Figs. 2–3). **Shown**
13. Lotka–Volterra on $[0,400]$: MRRK versions of Heun(3,3), RK(4,4) and Fehlberg(6,5) conserve both Casimirs; all methods keep periodicity; MRRK error grows linearly and ends below the quadratically growing baseline error (§5.2, Figs. 4–5). **Shown**
14. Kepler with three invariants ($H$, $L$ and the squared Laplace–Runge–Lenz vector), $e=0.5$, $t\le200$: MRRK conserves all three almost to machine precision, the baselines to about four digits; error growth is linear against quadratic (§5.3.1, Figs. 6–7). **Shown**
15. Perturbed Kepler ($\mu=0.005$, $e=0.6$): MRRK conserves $H$ and $L$ and reproduces the precessing orbit; the third-order baseline gets the orbit wrong; higher-order baselines look right but their error grows quadratically to saturation, MRRK's linearly (§5.3.2, Figs. 8–10). **Shown**
16. For the 1-soliton KdV solution, conservative methods give linear and nonconservative ones quadratic error growth; for interacting solitons there is no theory (§6). **Stated** (prior work)
17. The split-form Fourier semi-discretization conserves discrete mass and energy to rounding for any $\Delta x$, the Whitham invariant only to truncation error; it is stiff ($\lVert D_3\rVert=O(\Delta x^{-3})$), so $D_3$ is treated implicitly (§6). **Stated**
18. 1-soliton KdV ($N=512$, $t\in[0,20]$): energy relaxation reduces the maximum energy change from $5.38\times10^{-2}$ (ARK3) and $1.05\times10^{-2}$ (ARK4) to $1.33\times10^{-15}$ and $1.55\times10^{-15}$, and the Whitham-invariant change from $2.11\times10^{-1}$ and $4.21\times10^{-2}$ to $6.56\times10^{-4}$ and $9.84\times10^{-5}$; error growth is linear with relaxation, quadratic without (§6.1.1, Table 1, Fig. 11). **Shown**
19. 2-soliton KdV: the two relaxation methods differ, one sublinear, one between linear and quadratic at long times; both are far more accurate than the baselines; all show an error dip during the interaction (§6.1.2, Fig. 12). **Shown**
20. 3-soliton KdV: relaxation still gives quadratic error growth with smaller errors; total energy is conserved but the energy of individual solitons drifts linearly, giving quadratic phase errors. The authors cannot explain why the 2-soliton case differs. Mass and energy conservation do not guarantee linear error growth for multi-soliton data (§6.1.3, Fig. 13, §7). **Shown**
21. The smallest achievable maximum drift of the discrete Whitham invariant for the exact solution is about $10^{-11}$ on the 2- and 3-soliton grids (§6.2). **Shown**
22. Relaxation can try to restore through the time discretization a conservation law lost in the semi-discretization, but no existence guarantee holds, and `fsolve` often returns parameters accurate to well below double precision (§6.2.1). **Shown**
23. Enforcing energy and the Whitham invariant ($h=0.01$): invariant errors improve but not to rounding; accuracy can stagnate or degrade at short times but improves at long times, with roughly linear growth and strong jitter (§6.2.2, Figs. 14–17). **Shown**
24. "We also demonstrate for the first time the application of relaxation in combination with additive (ImEx) RK methods for stiff problems" (§7). **Stated** (priority claim; *compiler note, not in the source:* [Kang & Constantinescu (2022)](/sources/kang-2022.md) already applied relaxation to additive IMEX methods, recorded as a qualification on the [relaxation](/methods/relaxation-runge-kutta.md) page)
25. Ideally all methods of an embedded set have the same order; the paper uses existing methods of different orders and leaves equal-order sets to future work (§2.1). **Stated**
26. Future work: nonlinear Schrödinger, linear multistep methods, several dissipated or mixed functionals (§7). **Stated**

# Printed slips

- **Table 4 (Heun(3,3)), p. 21:** $b^{(1)}$ is printed $(1/4,0,1/4)$, which sums to 1/2; Heun's third-order weights are $(1/4,0,3/4)$.
- **Table 6 against §5:** §5 calls Fehlberg(6,4) a fourth-order method with third-order embedded methods, but the Table 6 caption makes $b^{(1)}$ (the RKF45 weights $16/135,\dots$) fifth order with a fourth-order $b^{(2)}$; which vector is the baseline is ambiguous.
- Tables 6–7: entries $0.000000000000003$ and $0.000000000000009$ where the structure of $A$ implies an exact 0 (rounding residue).
- Figs. 11–17 label the fourth-order IMEX method "ARK4(3)4L[2]SA"; the method used is ARK4(3)6L[2]SA. Figs. 2 and 6 write "DP5(7,5)" for DP(7,5).
- §5.2: "$\lambda,\mu,\nu>0$", but the chosen values are $\lambda=0$, $\nu=-1$.
- §3 requires every embedded method to have order at least 2, while Theorem 4.2 needs only $p_k\ge1$ and the SSPRK(2,2) set uses a first-order $b^{(2)}$.
- Theorem 4.2 proof: "$\Gamma=O(\Delta^{p-1})$" twice (missing $t$); Lemma 4.1 Eq. (14) has a stray subscript, "$G_i(u(t_n))$".
- Eq. (36), p. 18: the Simpson sum $\sum_{j=2}^{N-1}(4U_j^3+2U_{j+1}^3)$ with end terms $U_1$, $U_{N+1}$ does not reproduce the alternating composite-Simpson weights.
- Ref. [13] prints "E. Haier" for Hairer. The text credits the RK4 modification to "Dekker and Verwer [9]", but [9] is printed as a single-author K. Dekker monograph.
- Typos: "generealized" (Thm. 4.2), "Bi-Hamitonian" (§5.2), "Kortweg-de Vries" (§6).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u$, $\dot u=f(t,u)$, $u\in\mathbb R^m$ | $y$, $y'=f(t,y)$, $y\in\mathbb R^d$ | |
| $\Delta t$, $u^n$ | $h$, $y_n$ | |
| $A$, $\vec b$, $\vec c$, $\vec e$ | $A$, $b$, $c$, $\mathbf 1$ | $c=A\mathbf 1$ assumed |
| $g_i$ | $Y_i$ | stage values; **collision**: the source's $g(\Delta t,\vec\gamma)$ in Lemma 4.1 is a residual function |
| $\ell$ | $\kappa$ (page-local) | number of invariants; **collision**: registry $\ell$ is the micro-step index; $\kappa$ as on the [relaxation](/methods/relaxation-runge-kutta.md) page |
| $\vec b^k$, $p_k$ | $b^{(k)}$, $p_k$ | weights of the $k$-th embedded method (page-local); superscript is an index, not a power |
| $G_1$; $G=(G_1,\dots,G_\ell)^T$ | $\eta$; $\eta=(\eta_1,\dots,\eta_\kappa)$ | invariants |
| $\gamma$ | $\gamma_n$ | single relaxation parameter, near 1 |
| $\vec\gamma=(\gamma_1,\dots,\gamma_\ell)$, $\Gamma$ | $\gamma_{n,k}$, $\Gamma_n$ | MRRK parameters, near 0 (page-local); different normalization from $\gamma_n$ |
| $u^{n+1}_{\vec\gamma}$, $t^{n+1}_{\vec\gamma}$ | $y^\gamma_{n+1}$, $t_n+(1+\Gamma_n)h$ | relaxed solution and time |
| $d^n_k$, $D^n$ | $d_k$, $D_n$ | directions (page-local) |
| $B(u^n)$ | $B_n$ | leading $\kappa\times\kappa$ matrix of Lemma 4.1 (page-local); not the simplifying assumption $B(\xi)$ |
| $\Delta t^*$ | $h^*$ | step bound of Lemma 4.1 |
| $q$, $p$ (Kepler) | same (page-local) | **collision**: $p$ is also the order |
| $A=\lVert V\rVert^2$ (Kepler) | same (page-local) | **collision** with the Butcher matrix |
| $a,b,c,\lambda,\mu,\nu$ (Lotka–Volterra) | same (page-local) | **collisions** with Butcher symbols, the eigenvalue and the Courant number |
| $\eta_0,\eta_1,\eta_2$ (KdV) | same (page-local) | discrete mass, energy (no factor 1/2), Whitham invariant; $\eta_1$ is not the first component of the invariant vector above |
| $D_1$, $D_3$ | same | Fourier differentiation matrices |

# Reference list

The preprint prints 26 references in numbered style ([1]–[26], alphabetical).
The list is merged complete into the [bibliography](/bibliography.md), with
`citedby` this slug. [2] is the authors' code repository (GitHub, 2023); its
author-year coincides with the ingested biswas-2023, so it takes the
suffixed key `biswas-2023-f`. [11] is the NASA technical report TR R-315, [9] a CWI monograph, and [22]
and [26] arXiv preprints, kept as their own entries. [13] prints "E. Haier"
and is entered under Hairer. [14] prints "K. Heun et al.". Three Ranocha 2020
works ([20], [21], [23]) are matched to the bibliography by title and venue.
No printed duplicates.

# Pages created or updated

Chunk 2 (2026-10-19). This source is cited on:

* [Entropy stability and conservation of the fully discrete scheme](/properties/entropy-stability.md)
* [IMEX and additive Runge–Kutta methods](/methods/imex-runge-kutta.md)
* [Kepler problem](/benchmarks/kepler-problem.md)
* [Relaxation Runge–Kutta methods](/methods/relaxation-runge-kutta.md)
* [Symplecticity and quadratic-invariant preservation](/properties/symplecticity.md)
