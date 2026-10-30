---
type: Source
title: "Harten (1983) — High resolution schemes for hyperbolic conservation laws"
description: "Defines total variation nonincreasing (TVNI, later TVD) schemes, proves monotone ⇒ TVNI ⇒ monotonicity preserving and a sufficient incremental-form condition, and builds a five-point second-order TVNI scheme by applying a first-order scheme to a minmod-limited modified flux, extended to systems by characteristic fields and tested on Euler problems."
resource: "doi:10.1016/0021-9991(83)90136-5"
source_kind: paper
authors: [Harten A.]
year: 1983
venue: "J. Comput. Phys. 49:357-393"
local_file: "/home/stefano/papers/mosaic/weno-teno/1983_Crossref_Journal_of_Computational_Physics_Harten_High_resolution_schemes_for_hyperbolic_conservation_laws.pdf"
tags: [finite-difference, tvd, limiting, numerical-flux, characteristic, artificial-viscosity]
timestamp: 2026-10-30T08:09:00Z
---

# Summary

Harten (1983a) constructs explicit, second-order, five-point schemes in
conservation form for hyperbolic conservation laws that are **total variation
nonincreasing (TVNI)** in the scalar case, the property later called TVD
([TVD and slope limiters](/definitions/total-variation-diminishing.md)); the
word "TVD" is not printed. Section 2 defines TVNI, monotonicity-preserving and
[monotone schemes](/definitions/monotone-scheme.md), proves monotone ⇒ TVNI ⇒
monotonicity preserving (Theorem 2.1), recalls that monotone and linear
monotonicity-preserving schemes are at most first order, and gives a
**sufficient** condition for TVNI in incremental form (Lemma 2.2).

Section 3 writes three-point schemes with a "coefficient of numerical viscosity"
$Q(\nu)$ ([numerical dissipation](/definitions/numerical-dissipation.md))
and proves TVNI for $\lvert\nu\rvert\le Q(\nu)\le1$. The central idea
([Harten's TVD scheme](/methods/harten-tvd-scheme.md)): apply such a first-order
TVNI scheme to the modified flux $f+\frac{\Delta x}{\Delta t}\mathsf g$, where
$\mathsf g_i$ is a minmod-type limited approximation of the leading viscous term
$\frac12[Q(\nu)-\nu^2]\Delta u$. The result is second order away from
points where $u_x=0$ or $Q(\nu)=\nu^2$ and TVNI under the original CFL
restriction. Section 4 extends the scheme to systems field by field in a local
linearization ([characteristic decomposition](/methods/characteristic-decomposition.md)),
a generalized form of Roe's procedure with Roe's mean-value Jacobian as a special
case ([Roe solver](/methods/roe-riemann-solver.md)); TVNI and convergence are
proved only for constant-coefficient systems. Section 5 compares choices of
$Q$, among them a smoothed $Q$ (Eq. (5.3)) that removes stationary
expansion shocks of schemes with $Q(0)=0$, and $\nu^2+\frac14$, which is
Lax–Wendroff plus linear [artificial viscosity](/methods/artificial-viscosity.md).
Section 6 adds Harten's [artificial compression](/methods/artificial-compression.md)
switch in linearly degenerate fields. Section 1 frames convergence through
bounded variation, entropy consistency and conservation form
([Lax–Wendroff theorem](/results/lax-wendroff-theorem.md)).

Section 8 tests the Euler algorithm with Roe averages (schemes ULT1, $Q=\lvert\nu\rvert$,
and ULT2, $Q=\nu^2+\frac14$) against Roe's first-order scheme, Lax–Wendroff
and Harten's [hybrid scheme](/methods/hybrid-weno.md), on two
[shock-tube Riemann problems](/benchmarks/sod-and-lax-shock-tubes.md),
quasi-one-dimensional nozzle flows with standing shocks
([steady shock problems](/benchmarks/steady-shock-problems.md)) and the
[Mach 3 step](/benchmarks/forward-facing-step.md), in two dimensions with Strang-type
splitting ([operator splitting](/methods/operator-splitting.md)). The comparator
ROE is, in the paper's words, the "first order accurate Godunov-type scheme of
Roe" ([Godunov scheme](/methods/godunov-scheme.md)).

# Version read

Not the journal typeset: the Courant Mathematics and Computing Laboratory
(New York University) Research and Development Report **DOE/ER/03077-175**
(also stamped DE82 015473), dated **March 1982**, prepared under NASA Ames
Interchange NCA2-OR525-101 and DOE contract DE-AC02-76ER03077, in an NTIS/NASA
CASI reproduction scanned in 2010. 69 PDF pages: two disclaimer and stamp pages,
two title pages, contents, abstract, text pp. 1–49, references p. 50, figures
pp. 51–62 and a closing DOE disclaimer (report page $n$ = PDF page $n+6$). Poor
scan: every page with equations was read visually, disputed coefficients on
300-dpi crops; all equations are legible. The report prints the title
"High-Resolution Schemes for Hyperbolic Conservation Laws" and the single
author A. Harten (Tel-Aviv University), matching the Crossref record of the
J. Comput. Phys. paper. Equation, lemma and section numbers on this page are
those of the report; the journal's numbering was not checked.

# Key claims

Registry notation: $u^n_i$ point values, $\hat f_{i+1/2}$ numerical flux,
$\Delta_{i+1/2}u=u_{i+1}-u_i$, entropy pair $(\eta,F_\eta)$, eigenvalues
$\lambda_l$ with right and left eigenvectors $r_l$, $l_l$ (columns of $R$, rows
of $L$), $\nu$ the CFL number. Page-local: $\bar a_{i+1/2}$ the
divided-difference speed, $\nu_{i+1/2}=\bar a_{i+1/2}\Delta t/\Delta x$,
$Q$ the numerical-viscosity function (source $Q$), $\nu_{\max}$ the CFL
bound (source $\mu$), $C^\pm_{i+1/2}$ the incremental coefficients,
$\mathsf g_i$ and $\tilde{\mathsf g}_{i+1/2}$ the limited correction and its
unlimited edge value (source $g$, $\tilde g$), $\delta\nu_{i+1/2}=(\mathsf g_{i+1}-\mathsf g_i)/\Delta_{i+1/2}u$
(source $\gamma$), $\delta^{(l)}_{i+1/2}=l_l\,\Delta_{i+1/2}u$ the wave strengths
(source $\alpha^k$), $\theta_{\mathrm{AC}}$ the artificial-compression switch,
$\varepsilon_{\mathrm H}$ the parameter of (5.3).

1. Convergence of a conservative scheme to the entropy solution follows from (i) total variation bounded uniformly in $t$, $\Delta t$, $\Delta x$, (ii) consistency with the entropy condition for all entropy functions, (iii) uniqueness implied by the entropy condition (§1, citing [2], [9], [10]). **Stated**
2. Adding artificial viscosity can satisfy (i)–(ii), but "viscosity represents an irretrievable loss of information" and degrades resolution (§1). **Stated**
3. Theorem 2.1: a monotone scheme is TVNI, and a TVNI scheme is monotonicity preserving (§2); part (i) through the $\ell_1$ contraction of monotone schemes, part (ii) by contradiction. **Proved**
4. Monotone schemes approximate a viscous modified equation $u_t+f(u)_x=\Delta t[\beta_{\mathrm H}(u)u_x]_x$ with $\beta_{\mathrm H}\ge0$, $\beta_{\mathrm H}\not\equiv0$, and are therefore first order (Eq. (2.7), citing [8]). **Stated**
5. A linear scheme $u^{n+1}_i=\sum_jc_ju^n_{i+j}$ is monotonicity preserving iff all $c_j\ge0$ (citing Godunov [4]); every linear TVNI scheme is therefore monotone and first order, while nonlinear second-order TVNI schemes are not excluded (§2, Eq. (2.8)). **Stated**
6. Lemma 2.2: the scheme $u^{n+1}_i=u_i+C^+_{i+1/2}\Delta_{i+1/2}u-C^-_{i-1/2}\Delta_{i-1/2}u$ is TVNI if $C^-_{i+1/2}\ge0$, $C^+_{i+1/2}\ge0$ and $C^-_{i+1/2}+C^+_{i+1/2}\le1$ (Eqs. (2.9)–(2.10)), a sufficient condition ("sufficient to ensure"), proved from $\Delta_{i+1/2}u^{n+1}=C^-_{i-1/2}\Delta_{i-1/2}u+(1-C^-_{i+1/2}-C^+_{i+1/2})\Delta_{i+1/2}u+C^+_{i+3/2}\Delta_{i+3/2}u$ (2.11). **Proved**
7. Any three-point conservative scheme with a differentiable numerical flux can be written in the form (2.9) by the mean-value theorem (Eq. (2.13)). **Derived**
8. Lemma 3.1: the three-point scheme $\hat f_{i+1/2}=\frac12[f(u_i)+f(u_{i+1})-\frac{\Delta x}{\Delta t}Q(\nu_{i+1/2})\Delta_{i+1/2}u]$ (3.1) is TVNI under $\frac{\Delta t}{\Delta x}\max_i\lvert\bar a_{i+1/2}\rvert\le\nu_{\max}$ if $\lvert\nu\rvert\le Q(\nu)\le1$ for $0\le\lvert\nu\rvert\le\nu_{\max}\le1$ (Eqs. (3.2)–(3.3)). **Proved**
9. Under (3.2) the three-point scheme is only first order; Lax–Wendroff is $Q(\nu)=\nu^2$, which violates (3.2) (Eqs. (3.6)–(3.7)). **Derived**
10. Lemma 3.2: if $Q$ is Lipschitz and $\mathsf g$ satisfies (3.9), the modified flux (3.8) differs from the Lax–Wendroff flux by $O(\Delta x^2)$ (Eq. (3.6b)). **Proved**
11. Lemma 3.3: the minmod-type $\mathsf g_i$ of Eq. (3.11) satisfies (3.9), and $\lvert\delta\nu_{i+1/2}\rvert\le\frac12\lvert Q(\nu_{i+1/2})-\nu_{i+1/2}^2\rvert$ (3.12). **Proved**
12. Lemma 3.4: the five-point second-order scheme (3.8)+(3.11) is TVNI under the CFL restriction (3.3) of the three-point scheme; the proof shows $\lvert\nu^{\mathrm M}_{i+1/2}\rvert\le1-\frac12(\lvert\nu_{i+1/2}\rvert-1)^2\le1$, $\nu^{\mathrm M}=\nu+\delta\nu$. **Proved**
13. Condition (3.6) is necessary, and becomes sufficient for second order only away from points where the sign $s_{i+1/2}$ of $\tilde{\mathsf g}_{i+1/2}$ is discontinuous, i.e. where $Q(\nu)=\nu^2$ or $u_x=0$; there the truncation error may degenerate locally to $O(\Delta x^2)$ (Remark 2, §3). **Derived**
14. In the constant-coefficient scalar case the scheme is convergent although nonlinear (Remark 1, §3). **Derived**
15. Heuristic: the first-order scheme approximates $u_t+[f-\frac{\Delta x}{\Delta t}\mathsf g]_x=0$ to second order, so applying it to $u_t+[f+\frac{\Delta x}{\Delta t}\mathsf g]_x=0$ gives second order for $u_t+f_x=0$ (Eq. (3.16)); $\tilde{\mathsf g}_{i+1/2}$ is replaced by $\mathsf g_i$ to give $\mathsf g$ a bounded derivative (citing [5]). **Derived**
16. Lemma 4.1: the system scheme (4.8) gives $\hat f_{i+1/2}=\hat f^{\mathrm{LW}}_{i+1/2}+O(\Delta x^2)$ for Lipschitz $Q_l$ (Eq. (4.10)). **Proved**
17. Lemma 4.2 and Corollary 4.3: for constant $A$, the system scheme is TVNI in the characteristic total variation $\sum_i\sum_l\lvert\delta^{(l)}_{i+1/2}\rvert$ (4.12) under $\frac{\Delta t}{\Delta x}\max_l\lvert\lambda_l\rvert\le\nu_{\max}=\min_l\nu^{(l)}_{\max}\le1$, convergent for BV data and second-order accurate. **Proved**
18. With Roe's mean-value Jacobian, (4.8) for $m=1$ coincides with the scalar scheme, and if $Q_{l_0}(0)=0$ a stationary discontinuity with $f(u^-)=f(u^+)$ is a stationary solution (§4). **Derived**
19. No estimate of total-variation growth for nonlinear systems is available; convergence in the nonlinear system case is not proved (§4, Remark 3). **Stated**
20. $Q(\nu)=\lvert\nu\rvert$ gives the least dissipative TVNI scheme of the form (3.1), a generalization of Courant–Isaacson–Rees upstream differencing, with the monotonicity property under $\frac{\Delta t}{\Delta x}\max\lvert f'(u)\rvert\le1$ (Lemma 5.1, sketch of proof). **Proved** (sketch)
21. Schemes with $Q(0)=0$ keep stationary jumps, admissible or not, as stationary solutions and may select entropy-violating weak solutions; Eq. (5.3), $Q(\nu)=\nu^2/(4\varepsilon_{\mathrm H})+\varepsilon_{\mathrm H}$ for $\lvert\nu\rvert<2\varepsilon_{\mathrm H}$ and $\lvert\nu\rvert$ otherwise, "with say $\varepsilon=0.05$", prevents this and cannot resolve a stationary shock perfectly; $Q=\nu^2+\frac14$ restricts $\nu_{\max}$ to $\sqrt3/2\approx0.866$ (§5). The argument of $Q$ is the CFL number, not a wave speed, and the paper does not call (5.3) an entropy fix. **Derived**
22. The truncation error of (3.8)+(3.11) is $O(\Delta x^3)$ except possibly where $u_x=0$, independently of $Q$; the author judges (5.3) "the best choice of $Q(x)$" (§5). **Stated**
23. Conjecture: if the base scheme (3.1) is entropy consistent, so is the modified second-order scheme (§5). **Stated** (conjecture)
24. A first-order scheme spreads a contact like $\sqrt n$ after $n$ steps and a $p$-th order scheme like $n^{1/(p+1)}$ (citing [5]); the new scheme is expected to spread contacts like $n^{1/3}$; multiplying $\mathsf g$ by $1+\theta_{\mathrm{AC}}$ (Eq. (6.1)) makes the effective characteristic field slightly convergent so contacts do not spread (§6). **Stated**
25. With (6.1), $\lvert\delta\nu\rvert\le\lvert Q(\nu)-\nu^2\rvert$; the CFL condition is unchanged for $Q=\lvert\nu\rvert$ and for (5.3) with $\varepsilon_{\mathrm H}<1/3$, and tightens to $\max\lvert\nu\rvert\le3/4$ for $Q=\nu^2+\frac14$ (Eqs. (6.3a)–(6.3b)). **Derived**
26. Euler shock tubes: CFL bound $\nu_{\max}=0.95$; ULT2 results "look almost identical" to ULT1; "almost no dependence on the CFL number" (§8 I). **Shown**
27. On the Mach 3 step ($10\times30$ grid, $t=4$, CFL 0.75) ULT1 shows, like the Godunov results of [18], part of the sonic line at the corner turning into an expansion shock (§8 III). **Shown**
28. The scheme is simple to program and needs only slightly more CPU time than Lax–Wendroff with some artificial viscosity (§8; no timings printed). **Stated**

The modified-flux scheme as printed, in registry form ((3.8d), (3.11)):

$$\begin{aligned}
\hat f_{i+1/2}&=\tfrac12\big[f(u_i)+f(u_{i+1})\big]+\tfrac{\Delta x}{2\Delta t}\big[\mathsf g_i+\mathsf g_{i+1}-Q(\nu_{i+1/2}+\delta\nu_{i+1/2})\Delta_{i+1/2}u\big],\\
\mathsf g_i&=s_{i+1/2}\max\big[0,\min\big(\lvert\tilde{\mathsf g}_{i+1/2}\rvert,\tilde{\mathsf g}_{i-1/2}s_{i+1/2}\big)\big],\qquad \tilde{\mathsf g}_{i+1/2}=\tfrac12\big[Q(\nu_{i+1/2})-\nu_{i+1/2}^2\big]\Delta_{i+1/2}u,
\end{aligned}$$

$s_{i+1/2}=\mathrm{sign}(\tilde{\mathsf g}_{i+1/2})$, a minmod of
$\tilde{\mathsf g}_{i\pm1/2}$ (the paper does not use the word "minmod"). The
system version (4.8) applies it to each $\delta^{(l)}_{i+1/2}$ with $r_l$ at a
symmetric average state; the switch (6.1b) is
$\theta^{(l)}_{\mathrm{AC},i}=\lvert\delta^{(l)}_{i+1/2}-\delta^{(l)}_{i-1/2}\rvert/(\lvert\delta^{(l)}_{i+1/2}\rvert+\lvert\delta^{(l)}_{i-1/2}\rvert)$,
used for Euler only in the contact field.

Test setups as printed (§8). Riemann problem I in conservative variables
$(\rho,\rho v,E)$: $(0.445,0.3111,8.928)$ left, $(0.5,0,1.4275)$ right, 140 cells,
100 steps, $\nu_{\max}=0.95$. Riemann problem II: $(1,0,2.5)$ and $(0.125,0,0.25)$,
100 cells, 50 steps, $\nu_{\max}=0.95$, "presented in [16]" (Sod). Neither is
named; domain, diaphragm and final time are not printed. Nozzles: divergent
$A(x)=1.398+0.347\tanh(0.8x-4)$ (supersonic inflow, subsonic outflow) and a
convergent–divergent nozzle (8.7c), figures courtesy of H. C. Yee. Mach 3 duct:
$\rho=1.4$, $p=1$, $c=1$, width 1, length 3, step of height 0.2 at 0.6 from the
entrance, $\Delta x=\Delta y=0.1$, CFL 0.75, $t=4$, corner unrounded, referring
to Woodward and Colella [18].

# Printed slips

Report version; the journal version may differ.

1. Eq. (1.4): the scheme line carries no label "(1.4a)"; only (1.4b) and (1.4c) are printed.
2. Eq. (3.5b) prints $C_{\pm,j+1/2}=\frac12[Q(\bar\nu_{j+1/2})\pm\bar\nu_{j+1/2}]$ (the ± glyph confirmed on a 300-dpi crop). *(Compiler check, not in the sources: from (3.1), $-\frac{\Delta t}{\Delta x}(\hat f_{i+1/2}-f(u_i))=\frac12(Q-\nu)\Delta_{i+1/2}u$ and $-\frac{\Delta t}{\Delta x}(f(u_i)-\hat f_{i-1/2})=-\frac12(Q+\nu)\Delta_{i-1/2}u$, so $C^\pm=\frac12(Q\mp\nu)$.)*
3. Eq. (3.10a) prints $\bar f^M_{j+1/2}=\bar f_{j+1/2}+\frac1\lambda\{g_j+g_{j+1}+[Q(\bar\nu_{j+1})-Q(\bar\nu_{j+1/2}+\gamma_{j+1/2})]\Delta_{j+1/2}v\}$. *(Compiler check, not in the sources: subtracting (3.1a) from (3.8d) gives the factor $\frac1{2\lambda}$ and the argument $\bar\nu_{j+1/2}$ in the first $Q$.)* The following (3.10b) agrees with that difference.
4. Eq. (3.11b) prints the subscript $(\bar\nu_{1+1/2})^2$ for $(\bar\nu_{i+1/2})^2$; the same "1+1/2" appears in $\tilde g$ of (6.1a).
5. Lemma 3.3 proof (p. 17): "(3.13a) and (3.13b) imply", with no (3.13b) labelled; "$\tilde g_j=0$" where the limited $g_j$ is the quantity discussed; the parenthetical "(since $\Delta_{j\pm1/2}=O(\Delta^2)$)" is printed without its argument.
6. Lemma 3.3 proof (p. 18): the last line prints $\lvert\gamma_{j+1/2}\rvert\le\ldots=\lvert Q(\bar\nu_{j+1/2})\rvert-(\bar\nu_{j+1/2})^2\rvert$, without the factor $\frac12$ of (3.11b) and of the statement (3.12).
7. Lemma 3.4 statement (p. 18): "Suppose Q(x) satisfies (3.?)", the label garbled; (3.2) is the condition of Lemma 3.1.
8. Lemma 4.2 proof: "under condition (4.3)", where the CFL condition is (4.13). Corollary 4.3: "second under accurate".
9. Eq. (4.13) and p. 27 print the eigenvalues as $A^k$; elsewhere they are $a^k$.
10. Eq. (6.1b): the denominator is printed $\lvert\alpha^k_{i+1/2}\rvert+\lvert\alpha^k_{i+1-2}\rvert$ (crop-checked); the formula above uses $\lvert\alpha^k_{i-1/2}\rvert$.
11. Eqs. (8.4), (8.5): $\beta^k_{j+1/2}=(\nu^k_{j+1/2})^2$ and $\lvert\nu^k_{j+1/2}\rvert$ are printed without the factor $\alpha^k_{j+1/2}$ that (8.2) and (8.9) carry.
12. The second Riemann data set and the nozzle system are cited as "(8.6c)" (figure captions) and "(8.7a)", labels not printed in the text.
13. §5: "$\beta(u,\lambda)$ vanishes only for $\nu=1$". *(Compiler check, not in the sources: with (5.3), $\beta_{\mathrm H}\propto Q(\nu)-\nu^2=\lvert\nu\rvert-\nu^2$ for $\lvert\nu\rvert\ge2\varepsilon_{\mathrm H}$, which vanishes at $\lvert\nu\rvert=1$, i.e. at $\nu=\pm1$.)*
14. Remark (p. 20): "The schemes that we consider in section 5 all have the monotonicity property"; §5 proves it for $Q=\lvert x\rvert$ only (Lemma 5.1).
15. §2 attributes the $\ell_1$ contraction of monotone schemes to "B. Keyfitz in [8]"; ref. [8] is Harten, Hyman & Lax (1976). §2 cites "[7]" with [6] for second-order monotonicity-preserving schemes; ref. [7] is Harten's report on symmetric forms, and van Leer's scheme is ref. [17].
16. References: "Fluid Syn." in [14]; "parameter vectores" in [15].

# Notation map

| Harten (1983a) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $v^n_j$, index $j$ | $u^n_i$, index $i$ | point values; finite-difference reading of the conservation form (1.4) |
| $\lambda=\Delta t/\Delta x$ | $\Delta t/\Delta x$ | **collision** with the eigenvalues $\lambda_l$ |
| $\Delta_{j+1/2}u$, $\Delta$ | $\Delta_{i+1/2}u=u_{i+1}-u_i$ (local), $\Delta x$ | undivided difference; $O(\Delta^2)$ at fixed $\Delta t/\Delta x$ |
| $\bar f_{j+1/2}$, $\bar f^M$, $\bar f^{LW}$ | $\hat f_{i+1/2}$, modified and Lax–Wendroff fluxes | **collision**: the source's bar marks a numerical flux, the registry's a cell average |
| $(U,F)$, $\bar F$ | $(\eta,F_\eta)$, numerical entropy flux | entropy decreasing: $\eta_t+(F_\eta)_x\le0$ |
| $\bar a_{j+1/2}$ | $\bar a_{i+1/2}$ (local) | divided-difference (scalar Roe) speed |
| $\bar\nu_{j+1/2}=\lambda\bar a_{j+1/2}$ | $\nu_{i+1/2}$ | local CFL number |
| $Q(x)$, $Q^k$ | $Q(\nu)$, $Q_l$ (local) | numerical-viscosity coefficient; **collision** with the SBP matrix $Q$ |
| $\mu$ | $\nu_{\max}$ (local) | CFL bound; **collision** with the affine $\mu$ |
| $C_{\pm,j+1/2}$ | $C^\pm_{i+1/2}$ (local) | incremental coefficients |
| $g_i$, $\tilde g_{i+1/2}$, $s_{i+1/2}$ | $\mathsf g_i$, $\tilde{\mathsf g}_{i+1/2}$, $s_{i+1/2}$ (local) | **collision** with the constraint functions $g_i(u)$ |
| $\gamma_{j+1/2}$ | $\delta\nu_{i+1/2}$ (local) | **collision** with the ratio of specific heats $\gamma$ (kept for the gas) |
| $\beta(u,\lambda)$, $\beta^k_{j+1/2}$ | $\beta_{\mathrm H}$, $\beta^{(l)}_{\mathrm{diss}}$ (local) | modified-equation viscosity; §8 dissipation coefficient; **collision** with the smoothness indicators $\beta_k$ |
| $a^k$ ($A^k$ in (4.13)), $R^k$, $L^k$ | $\lambda_l$, $r_l$, $l_l$ | superscript in §§4–6, subscript ($a_1$, $R_1$) in §7 |
| $S$, $\Lambda$ | $R$, $\mathrm{diag}(\lambda_l)$ | |
| $\alpha^k_{j+1/2}$ | $\delta^{(l)}_{i+1/2}$ (local) | wave strength; **collision** with the weights $\alpha_k$ |
| $w^k$; $w$ in §§7–8 | characteristic variable $l_lu$; $u=(\rho,\rho v,E)$ | |
| $u$ (velocity, §7), $m$ | $v$, $\rho v$ | |
| $\theta^k_i$ | $\theta^{(l)}_{\mathrm{AC},i}$ (local) | **collision** with the Zhang–Shu $\theta$ |
| $\varepsilon$ | $\varepsilon_{\mathrm H}$ (local) | parameter of (5.3); not the weight regularization $\epsilon$ |
| $\hat u$, $\hat c$, $\hat H$ | $\hat v$, $\hat c$, $\hat H$ | Roe averages (7.4) |
| $[b]$ | $[\![b]\!]$ | |
| $V(u,v)$ | symmetric average state (local) | |
| $L$, $L_x$, $L_y$ | $\mathcal S$, $\mathcal S_x$, $\mathcal S_y$ (local) | solution operators; **collision** with the left-eigenvector matrix $L$ |
| TVNI | TVD | |

# Reference list

The report prints 18 references, numbered [1]–[18]; journal articles mostly
without titles. The list is merged complete into the
[bibliography](/bibliography.md), with `citedby` including `harten-1983`.
Several items are printed in pre-publication form and enter as their own
entries: ref. [7] (Harten, ICASE report on symmetric forms, "to appear"), whose
journal version is Harten (1983d); ref. [10] (Harten, Lax & van Leer, ICASE
report, "to appear", no year printed), a work distinct from this source and
from the published Harten, Lax & van Leer (1983); ref. [15] (Roe, J. Comput.
Phys., "to appear"); ref. [13] (Osher, UCLA report 1980). Ref. [9] is Harten &
Lax (SIAM J. Numer. Anal.). Ref. [12] (Liu, J. Math. Anal. Appl. 53) has its
first-page digit partly cut ("?3-88", read as 73-88). Ref. [4] (Godunov) prints
the pages 271-295. No item is unparseable.

# Pages created or updated

Chunk 12 (2026-10-30). This source is cited on:

* [Artificial compression](/methods/artificial-compression.md)
* [Artificial viscosity and spectral viscosity](/methods/artificial-viscosity.md)
* [Characteristic decomposition](/methods/characteristic-decomposition.md)
* [Godunov scheme](/methods/godunov-scheme.md)
* [Harten's high-resolution TVD scheme](/methods/harten-tvd-scheme.md)
* [Hybrid central-WENO schemes](/methods/hybrid-weno.md)
* [Lax–Wendroff theorem](/results/lax-wendroff-theorem.md)
* [Mach 3 forward-facing step](/benchmarks/forward-facing-step.md)
* [Monotone schemes and monotone numerical fluxes](/definitions/monotone-scheme.md)
* [Numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
* [Operator splitting for stiff source terms](/methods/operator-splitting.md)
* [Roe approximate Riemann solver](/methods/roe-riemann-solver.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [Steady shock problems](/benchmarks/steady-shock-problems.md)
* [Total variation diminishing (TVD) and slope limiters](/definitions/total-variation-diminishing.md)
