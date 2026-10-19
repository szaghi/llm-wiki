---
type: Source
title: "Han Veiga et al. (2021) — DeC and ADER: Similarities, Differences and a Unified Framework"
description: "Shows that modern ADER and deferred correction are the same iterative collocation scheme with different test functions, proves order min(M+1, K) for ADER, compares the stiff variants IMDeC and IMADER, and computes identical stability regions."
resource: "doi:10.1007/s10915-020-01397-5"
source_kind: paper
authors: [Han Veiga M., Öffner P., Torlo D.]
year: 2021
venue: "J. Sci. Comput. 87:2"
local_file: "/home/stefano/papers/mosaic/ode-integration/2021_Crossref_Journal_of_Scientific_Computing_Han_DeC_and_ADER_Similarities_Differences_and_a_Unified_Framewor.pdf"
tags: [explicit, implicit, stiff, stability, verification]
timestamp: 2026-10-19T12:00:00Z
---

# Summary

The paper relates two iterative, arbitrarily high-order one-step integrators of the hyperbolic-PDE community. The first is modern [ADER](/methods/ader-time-integration.md), the space–time Galerkin "local predictor" of Dumbser and co-workers, as distinct from the historical Taylor/Cauchy–Kovalevskaya/generalized-Riemann-problem ADER. The second is [deferred correction](/methods/deferred-correction.md) (DeC) in Abgrall's two-operator form: a low-order explicit operator $\mathcal L^1$, a high-order implicit collocation operator $\mathcal L^2$, and the iteration $\mathcal L^1(\underline y^{(k)})=\mathcal L^1(\underline y^{(k-1)})-\mathcal L^2(\underline y^{(k-1)})$.

For the method-of-lines system $y'=f(y)$ the authors write ADER as a time-Galerkin fixed-point problem $\mathcal M\underline y=r(\underline y)$ on $\mathsf M+1$ subnodes, solved by Picard iteration. They show that ADER is a DeC scheme with $\mathcal L^2=\mathcal M\underline y-r(\underline y)$ and $\mathcal L^1=\mathcal M\underline y-r(y(t_n))$, and that DeC is an ADER-type scheme whose test functions are characteristic functions instead of the Lagrange basis ([DeC–ADER equivalence](/results/dec-ader-equivalence.md)). From Abgrall's DeC convergence proposition they prove that ADER with $\mathsf M+1$ nodes and $K$ iterations has order $\min(\mathsf M+1,K)$.

For stiff sources they compare IMDeC (linearized implicit source in $\mathcal L^1$, $d\times d$ solves per subnode) with IMADER (Newton-type coupling of the time matrix and the source Jacobian, one $(d\mathsf M)\times(d\mathsf M)$ solve per step). IMADER is costlier and more accurate in their tests. They also write DeC–residual distribution, ADER space–time DG and ADER/DeC–spectral difference in closed form.

Numerically, the [stability regions](/definitions/stability-function.md) of explicit ADER and explicit DeC coincide and do not depend on the node family (equispaced, Gauss–Legendre, Gauss–Lobatto). Convergence studies on scalar and system ODEs, Lotka–Volterra, a stiff linear system, Robertson, and spectral-difference linear advection and Burgers confirm design orders up to about 11. ADER with equispaced or Gauss–Legendre nodes loses order near machine precision. The paper names an [asymptotic-preserving](/definitions/asymptotic-preserving-scheme.md) DeC only through a cited title.

# Version read

arXiv:2002.11764v3 [math.NA], 6 Jan 2021, author typeset; page 1 carries the arXiv stamp and no journal header. Not the JSC version of record. 30 pages (main text pp. 1–27, references pp. 27–30). Title and authors match Crossref. The archive filename gives the first author as "Han"; the printed surname is the compound "Han Veiga". Page, equation and section numbers cited here are those of the arXiv v3. All codes are at the authors' repository (ref. [21]).

# Key claims

Notation: $y'=f(y)$ with $f=-F$ of the source; $h$ step; subnodes $t_{n,m}$, $m=0,\dots,\mathsf M$; $\underline y=(y_{n,0},\dots,y_{n,\mathsf M})$; $\mathcal M$ the ADER time matrix; $K$ iterations (see the notation map).

1. The explicit modern ADER method (as in Zanotti et al.) is a special interpretation of deferred correction (Dutt et al., in Abgrall's form). (Abstract, §4.1–4.2, Conclusion 4.2) **Derived**
2. Modern ADER for $y'=f(y)$ on $[t_n,t_{n+1}]$ reduces to the fixed-point problem $\mathcal M\underline y=r(\underline y)$ (Eq. 12), which is "nothing more than a classical collocation method … or a high order implicit RK method"; its order "depends on the used quadrature rule", and its solution is stated to be "$(M+1)$th order accurate in time". (§2, Eqs. 9–13) **Stated**
3. ADER fits the DeC iteration with $\mathcal L^2(\underline y)=\mathcal M\underline y-r(\underline y)$ and $\mathcal L^1(\underline y)=\mathcal M\underline y-r(y(t_n))$ (Eq. 24); the DeC update then collapses exactly to the ADER Picard iteration $\mathcal M\underline y^{(k+1)}=r(\underline y^{(k)})$. (§4.1) **Derived**
4. The $\mathcal L^1$ operator for ADER is "not really unique"; choice (24) makes $\mathcal L^1-\mathcal L^2$ Lipschitz. An equivalent normalized pair is $\mathcal L^1(\underline y)=\underline y-\mathcal M^{-1}r(y(t_n))$, $\mathcal L^2(\underline y)=\underline y-\mathcal M^{-1}r(\underline y)$ (Eqs. 25/30). (§4.1, Remark 4.1) **Stated**
5. Row $m$ of DeC's $\mathcal L^2$ is a weak form in time with test function $\psi_m=\chi_{[t_{n,0},t_{n,m}]}$ (Eqs. 26–29); DeC and ADER differ "just in the choice of the test functions" and hence in the iteration matrix; DeC cannot integrate by parts in time because its test functions are discontinuous. (§4.2, Conclusion 4.2) **Derived**
6. The ADER $\mathcal L^1$ is coercive with constant $C_0=1$ (for equal initial data). (Proposition 4.3) **Proved** (the proof cites definition (24), but the identity holds for (30); see printed slips)
7. $\mathcal L^1-\mathcal L^2$ for ADER is Lipschitz with constant $C_A=h\beta$, $\beta=C_{\mathcal M}C_r$ independent of $h$, using bounded basis functions and weights, Lipschitz $f$ and an $h$-independent bound on $\lVert\mathcal M^{-1}\rVert$. (Proposition 4.4, Eqs. 31–33) **Proved**
8. Main theorem: ADER–DeC with operators (30) in the DeC algorithm (23) has order of accuracy $\min(\mathsf M+1,K)$, each iteration gaining one order: $\lVert\underline y^{(K)}-\underline y^{\mathrm{ex}}\rVert\le C^*(h^{\mathsf M+1}+(\beta h)^K)$. (Theorem 4.5) **Proved** (DeC contraction argument; extends Jackson's finite-iteration result for linear homogeneous systems)
9. Explicit DeC (Abgrall form) needs $K=\mathsf M+1$ iterations, "as many iterations as the desired order of accuracy". (§3, after Eq. 23) **Stated**
10. DeC convergence proposition (Abgrall): if $\mathcal L^1$ is coercive with constant $\gamma_1$, $\mathcal L^1-\mathcal L^2$ is Lipschitz with constant $\gamma_2\Delta$, and $\mathcal L^2(\underline y^*)=0$ has a unique solution, then for $\eta=\frac{\gamma_2}{\gamma_1}\Delta<1$ the error after $k$ iterations is at most $\eta^k\lVert\underline y^{(0)}-\underline y^*\rVert$. (Proposition 3.1; proofs in cited works) **Stated** (background)
11. For equidistant, Gauss–Lobatto and Gauss–Legendre nodes the ADER matrix $\mathcal M$ has full rank and is invertible. (Remark 4.6) **Stated** (no proof)
12. A higher-order method than explicit Euler in $\mathcal L^1$ speeds up the iteration but can lower accuracy because the error loses smoothness; any DeC method can be interpreted as a Runge–Kutta scheme. (Remark 3.2) **Stated**
13. IMDeC puts the linearized stiff source into $\mathcal L^1$ (Eq. 39) and inverts a $d\times d$ matrix $I-\beta_mhJ^{\mathrm I}(y(t_n))$ per subnode, $\beta_m=(t_{n,m}-t_{n,0})/h$; IMADER couples the time matrix with the source Jacobian and inverts a $(d\mathsf M)\times(d\mathsf M)$ matrix per step. (§4.4, Eqs. 40–47) **Derived**
14. IMADER is more accurate than IMDeC on the stiff tests; the heuristic is that in explicit schemes most $\mathcal L^1$ terms cancel, while IMDeC treats them in a "very simplified first order manner", and "IMADER is closer to a pure implicit scheme than IMDeC". (§4.4, §5.3, Figs. 9–10) **Shown** (qualitative, plots only, no error numbers) and **Stated** (heuristic)
15. The stability regions $\{z:\lvert R(z)\rvert<1\}$ of explicit ADER and explicit (simplified) DeC on $y'=\lambda y$ coincide for the orders shown (labels $p=1,\dots,5$; text says 2 to 5), do not depend on the node family, and grow with order; claimed as the first A-stability study of ADER. (§5.1, Fig. 2) **Shown** (one step with $h=1$ on an equispaced grid of $\lambda$)
16. An analytic A-stability study "is not feasible since it leads to solving polynomial inequalities of degree $p(p+1)$". (§5.1) **Stated**
17. CFL bounds cannot be derived directly from the ODE stability analysis because they depend on the spatial discretization; von Neumann and energy (entropy) stability are left to future work. (§5.1) **Stated**
18. Scalar linear ODE ($\lambda=10$, $t\in[0,0.1]$): all variants converge with design order at low orders; ADER with equispaced nodes fails to reach the right order at the highest orders (suspected cause: higher condition number of the equispaced $\mathcal M$); DeC is "not affected … because it does not require a mass matrix"; equispaced weights become negative from ninth order on; ADER with Gauss–Legendre nodes shows "strange behavior at high orders and high resolutions", attributed to the extrapolation to $t_{n+1}$; the ADER/DeC difference with Gauss–Lobatto nodes is negligible. (§5.2.1, Fig. 3, orders 2–11) **Shown**
19. Nonlinear scalar ODE, linear three-species system and Lotka–Volterra: design rates for all node families with minor differences (Figs. 4–6); long Lotka–Volterra runs ($t\in[0,100]$, $h=1$ and $0.5$, orders 3 and 5, Gauss–Lobatto) show no large ADER–DeC differences, higher orders being more accurate (Figs. 7–8). (§5.2) **Shown**
20. Stiff linear system (71), $T=10$, $h=1$, fourth order: IMDeC and IMADER track the exact solution; explicit ADER (and explicit DeC, not plotted) fail. (§5.3, Fig. 9) **Shown**
21. Robertson problem (75), third order, 30 steps with $h_n=2h_{n-1}$: only the implicit methods converge to the exact solution, IMADER more precisely than IMDeC; the explicit methods fail early with wide oscillations. (§5.3, Fig. 10) **Shown**
22. PDE tests (spectral difference in space, $h=\frac{C}{\mathsf M+1}\frac{\Delta x}{\lvert v_{\max}\rvert}$, $C=0.5$): ADER and DeC reach the design orders 3–9 for linear advection at $T=1$ and Burgers at $t=0.05$, with no noticeable node-family dependence above the round-off floor ($\approx10^{-12}$–$10^{-13}$). (§5.3.1, Figs. 11–14) **Shown**
23. For Burgers, ADER was "more stable" when the final update used the flux integral rather than the predictor reconstruction $\phi(1)^\top\underline y^{(k+1)}$; no significant difference for linear advection. (§5.3.1) **Shown** (qualitative statement only)
24. ADER-DG with the generalized Riemann problem solved only in the final step is local during the iterations (easy parallelization) and "can keep up or be even more effective than traditional RKDG". (Remark 4.7) **Stated**
25. In ADER space–time DG the space–time matrix factorizes into a spatial and a temporal part; changing the space discretization changes only the spatial part, so the time-integration structure is unchanged: "That is why we can consider ADER to be a time integration method." (Remark 4.8) **Derived**
26. DeC's advantage for continuous finite elements: it avoids inverting the global mass matrix by mass lumping in $\mathcal L^1$; residual distribution with the method of lines destroys high order, which DeC–RD (Eq. 49) avoids. (§3, §4.5.1) **Stated**
27. Explicit Runge–Kutta is hard to extend to very high order because there is "no automatic procedure to generate the Butcher tableau"; DeC and ADER give arbitrary order without order-condition checks. (§1, Remark 3.2) **Stated**
28. The order loss of ADER with equispaced and Gauss–Legendre nodes near machine precision at very high order remains unexplained (conditioning of $\mathcal M$ or interpolation suspected). (§6) **Stated** (open question)

*(Compiler check, not in the sources.)* The collocation solution of $\mathcal L^2=0$ has order $2\mathsf M$ on Gauss–Lobatto and $2\mathsf M+2$ on Gauss–Legendre nodes, so the paper's "$\mathsf M+1$" is a lower bound, not the sharp order; Theorem 4.5 does not distinguish local from global error; and the "A-stability" of §5 is a computation of bounded stability regions of explicit methods, which are not A-stable.

# Printed slips

- Sign of $F$: the ODE is written $\alpha'+F(\alpha)=0$ (Eqs. 4, 14) and ADER's $r$ uses $-\Delta tF$ consistently, but DeC's $\mathcal L^2$ (Eqs. 18–19) "$\alpha^M-\alpha^0-\Delta t\sum\theta^M_rF(\alpha^r)$" and $\mathcal L^1$ (Eq. 20) correspond to $\alpha'=+F$; IMDeC (Eq. 38) reverts to "$+\beta^m\Delta t(F(\alpha^0)+S(\alpha^m))$"; §5.3 sets $S$ equal to the right-hand side (Eq. 74, and "$S(y)=F(y)$" for Robertson), again opposite to Eq. (37).
- Eq. (11): index range "$m=0,\dots,M+1$" for $M$.
- Example 2.1: $r(\alpha)$ printed with "$F(\alpha(t^1))w_1$; $F(\alpha(t^2))w_2$" while nodes and weights are indexed 0, 1.
- Eq. (21) (and Props. 3.1, 4.4): "$\underline\alpha:=(\alpha^0,\dots,\alpha^M)\in\mathbb R^{M\times I}$" for $M+1$ states.
- Proposition 4.3 proof: "from the definition (24) we have $\|\mathcal L^1(\alpha)-\mathcal L^1(d)\|=\|\alpha-d\|$" — with (24) the difference is $M(\alpha-d)$; the identity holds for (30).
- Eq. (34): "$\le C_0\|\mathcal L^1(\alpha^{(k)})-\mathcal L^1(\alpha^*)\|$" — coercivity gives $1/C_0$; harmless since $C_0=1$.
- The Lipschitz constant $\beta$ (C.2, Prop. 4.4) reuses the symbol of the subnode fractions $\beta^m$ (Eq. 20).
- Eq. (42): "$\mathcal L^2(\underline\alpha^{(k+1)})$" for $\mathcal L^2(\underline\alpha^{(k)})$ (Eqs. 41 and 47 have $(k)$).
- Eq. (28): integrand "$\chi_{[t^0,t^m]}(t)\phi_m(t)$" inside $\sum_rF(\alpha^r)$ for $\phi_r$ (Eq. 26 has $\phi_r$); the unnumbered iteration after Eq. (29) also has $\phi_m$.
- Text at Eq. (44): "Newton–Rapshon".
- Eq. (65): the ADER-SD matrix includes "$-\Delta t\,w_s\phi'_q(t_s)$" while the ODE matrix (Eq. 10) on $[0,1]$ is $\Delta t$-free; the scaling convention switches between §2 and §4.5.3.
- Eq. (68), DeC-SD: "$u^{s,(k+1)}=u^{s,(k)}-\Delta t\sum_q\theta^s_q\partial_xf(u^{q,(k)})$" — the DeC algorithm (23) starts from $u(t^n)$, not from the previous iterate; as printed it is not the DeC iteration.
- §5.1: region printed "$\mathcal S:=\{z\in\mathbb C:\phi(z)<1\}$" without modulus; $\phi$ reused for the stability function; Fig. 2 axes "Re(a)/Im(a)", order labels $p=1\dots5$ against "2 to 5" in the text; the panel descriptions do not match the legends.
- §5.3: "final time of T = 10" while the Fig. 9 axis spans 0–5.
- §5.2.1 attributes the Gauss–Legendre anomaly to an extrapolation "only necessary when using nodes that do not include the boundaries", while Example 2.1 and §4.5.3 use Gauss–Legendre throughout.
- References: [41] "M. H. Veiga" against "M. Han Veiga" elsewhere; [20] and [42] are the same book (Hairer & Wanner, *Solving ODEs II*) with authors in different order; [4] "E. l. Meledo" against [5] "E. l. Mélédo".

# Notation map

| Han Veiga et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\alpha(t)\in\mathbb R^I$ | $y(t)\in\mathbb R^d$ | semi-discrete state; $I\to d$ |
| $\partial_t\alpha+F(\alpha)=0$ | $y'=f(y)$, $f=-F$ | **sign: the source's $F$ is minus the right-hand side**, and §3 uses the opposite sign (slips) |
| $S$ in $\alpha'+F+S=0$ | $f^{\mathrm I}=-S$ | stiff part; $J^{\mathrm I}=\partial f^{\mathrm I}/\partial y$ |
| $\Delta t$, $T^n=[t^n,t^{n+1}]$ | $h$, $[t_n,t_{n+1}]$ | |
| $M$ (polynomial degree; $M+1$ nodes) | $\mathsf M$ | sans-serif subnode count |
| $\underline{\underline M}$ | $\mathcal M$ | **ADER time "mass matrix", in fact the iteration matrix; the registry's $M$ is the mass matrix of $My'=f$** |
| $t^m=t^{n,m}$, $\alpha^m$ | $t_{n,m}$, $y_{n,m}$ | $t_{n,0}=t_n$, $t_{n,\mathsf M}=t_{n+1}$ |
| $k$, $K$ | $k$, $K$ | correction (Picard) iterations |
| $\phi_m(t)$ | $\phi_m(t)$ | Lagrange time basis; **not the registry $\phi_k$ functions**, and §5.1 reuses $\phi$ for the stability function |
| $\phi(z)$ (§5.1) | $R(z)$ | stability function |
| $\theta^m_r$, $\beta^m$ | kept, $\beta_m$ | DeC weights; subnode fraction |
| $\beta$, $C_A$, $C_0$, $C_r$, $C_M$ | kept | Lipschitz and coercivity constants; **$\beta$ collides with $\beta^m$** |
| $\gamma_1,\gamma_2,\eta$ | kept | constants of Abgrall's proposition; not the tree density |
| $\mathcal L^1$, $\mathcal L^2$ | kept | low- and high-order DeC operators |
| $\alpha^*$, $\alpha^{ex}$ | $\underline y^*$, $\underline y^{\mathrm{ex}}$ | |
| $\lambda$, $z$ | $\lambda$, $z=h\lambda$ | |
| m (figure labels), $p$ (Fig. 2) | $p$ | order of accuracy, not a node index |
| EQ, GL, GLB | equispaced, Gauss–Legendre, Gauss–Lobatto | |

# Reference list

43 printed references, numbered [1]–[43], alphabetical by first author. The list is merged complete into the [bibliography](/bibliography.md) with `citedby` hanveiga-2021. Printed duplicate: [20] and [42] are the same Hairer–Wanner book printed twice with authors in different order; they are folded into one entry (`hairer-1996`), so the list gives 42 entries. [21] is a software repository and [41] a preprint without venue (`@misc`); [6] is "accepted" and [4] an arXiv preprint, kept as their own entries. [8] prints no publisher. No unparseable item.

# Pages created or updated

Chunk 1 (2026-10-19). This source is cited on:

* [A-, L-, A(α)- and algebraic stability](/properties/a-stability.md)
* [ADER as a time integrator](/methods/ader-time-integration.md)
* [Asymptotic-preserving scheme](/definitions/asymptotic-preserving-scheme.md)
* [Deferred correction (DeC)](/methods/deferred-correction.md)
* [Equivalence of DeC and ADER](/results/dec-ader-equivalence.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)
