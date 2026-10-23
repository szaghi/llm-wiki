---
type: Source
title: "Ciallella et al. (2023) — Arbitrary High Order WENO Finite Volume Scheme with Flux Globalization for Moving Equilibria Preservation"
description: "Arbitrary-order WENO finite-volume scheme for the shallow-water equations with bathymetry and Manning friction, built on flux globalization: Gauss-quadrature global-flux averages, WENO reconstruction of the global flux and a Roe upwind flux; exact for constant discrete global flux, exactly lake-at-rest preserving, with deferred-correction time stepping."
resource: "doi:10.1007/s10915-023-02280-9"
source_kind: paper
authors: [Ciallella M., Torlo D., Ricchiuto M.]
year: 2023
venue: "J. Sci. Comput. 96:53"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Journal_of_Scientific_Computing_Ciallella_Arbitrary_High_Order_WENO_Finite_Volume_Scheme_with_Flux_Glo.pdf"
tags: [well-balanced, weno, finite-volume, stiff-source]
timestamp: 2026-10-23T23:00:00Z
---

# Summary

Ciallella, Torlo & Ricchiuto build an arbitrarily high-order WENO finite-volume scheme for the
one-dimensional [shallow-water equations](/definitions/shallow-water-equations.md) with
bathymetry and Manning friction, based on [flux globalization](/methods/flux-globalization.md).
The integral of the source is absorbed into the flux, which turns the balance law into a
quasi-conservative system $\partial_tu+\partial_xK=0$. Both components of the global flux $K$,
the discharge and the momentum flux plus the source integral, are then constant at every
steady state. This includes discontinuous (transcritical, shocked) states, for which the
classical Bernoulli invariant fails.

The scheme has three ingredients. (i) Cell averages of the global flux from 4-point
Gauss–Legendre quadrature of WENO-reconstructed states, with the source integral accumulated
cell by cell from zero at the left boundary through a Lagrange interpolant of the source.
(ii) A [WENO-JS](/methods/weno-js-reconstruction.md) reconstruction (WENO3, WENO5) of the
global-flux averages to interface values. (iii) An upwind flux built on the Roe matrix of the
homogeneous system, which returns the constant global flux at equilibrium. Prop. 3.1 proves
that any state with constant global-flux averages is an exact discrete steady state. For still
water, a split source quadrature, WENO weights computed from the free surface and shared by
depth and bottom, and an interface jump of the source integral make the scheme exactly
[well-balanced](/properties/well-balancing.md) (Prop. 3.3). Interface depths come from a
depressed cubic. Time integration is explicit deferred correction.

The tests are lake at rest, a perturbed lake at rest, sub-, super- and transcritical flows over
a bump, perturbed moving states, a step bottom and Manning friction. They show machine-precision
lake-at-rest preservation, design orders 3 and 5 on moving equilibria with errors 2 to 5
orders of magnitude below a standard WENO/Rusanov scheme, and no spurious oscillations at the
transcritical shock and the step. The authors state that the scheme is not exactly
well-balanced for all analytical equilibria.

# Version read

Author manuscript in LaTeX preprint layout, dated "January 4, 2024" on page 1 (PDF created
2024-01-04), 27 pages, no arXiv stamp, journal header or DOI: a post-publication author
version, not the version of record (J. Sci. Comput. 96, article 53, 2023). Title, authors and
affiliations match Crossref. Equation, table and figure numbers are those of this manuscript.

# Key claims

Registry notation with the conventions of the [well-balancing](/properties/well-balancing.md)
page: depth $h$, bottom $b$, free surface $H_{\mathrm s}=h+b$, velocity $v$, discharge $hv$,
gravity $g$. Page-local: Manning coefficient $n_{\mathrm M}$, source integral
$\mathcal S(x,t)=-\int^xS\,d\xi$, global flux $K=(hv,K_2)$ with
$K_2=(hv)^2/h+gh^2/2+\mathcal S$, and $\Upsilon=(hv)^2/(2h^2)+gH_{\mathrm s}$.

1. Writing the shallow-water equations with bathymetry and friction as $\partial_tu+\partial_xK(u,x)=0$, $\mathcal S=g\int^x\big(h\,\partial_\xi b+n_{\mathrm M}^2h^{-7/3}\lvert hv\rvert hv\big)d\xi$, makes both components of $K$ equilibrium variables (§2.1, Eqs. (3)–(4)). **Stated**
2. Steady states are characterized in general by $hv\equiv q_0$ and $K_2\equiv K_0$ (Eq. (7)); lake at rest (5) and constant energy (6) are special cases. The smooth frictionless reduction $\Upsilon\equiv\Upsilon_0$ fails when bathymetry or depth is discontinuous, while (7) "is always true" (§2.2, Eqs. (8)–(9)). **Derived**
3. The simple averaging of $\mathcal S$ used by Cheng et al. "is not enough to reach more than second order of accuracy" (§3, p. 5). **Stated**
4. The upwind flux is $\hat f_{i+1/2}=(L^{-1}\Lambda^+L)_{i+1/2}K^-_{i+1/2}+(L^{-1}\Lambda^-L)_{i+1/2}K^+_{i+1/2}$, with $L$ the left eigenvectors of the Roe-averaged Jacobian of the homogeneous system and $\Lambda^\pm$ diagonal 0/1 selectors of the eigenvalue signs (Eqs. (12)–(14)). Other solvers such as Rusanov are admissible if their dissipation vanishes at steady states, e.g. through cutoff functions (§3, p. 5). **Stated**
5. Prop. 3.1 (global flux property): if the global-flux averages equal a constant $K_0$ in every cell, the cell averages are a steady state of the semi-discrete scheme (11) with WENO reconstruction of $K$ (§3.2, p. 7). **Proved** (all candidate polynomials reproduce constants, and (12) then returns $K_0$)
6. The discrete steady states are not necessarily the analytical equilibria; at equilibrium the scheme acts like a nonlinear multistep ODE method, and no explicit ODE-solver analogy (as the Lobatto IIIA equivalence of Gauss–Lobatto DGSEM) was found (Remark 3.2). **Stated**
7. Prop. 3.3 (lake at rest): with the bathymetric source quadrature (35) and the jump (38), the global-flux WENO scheme is exactly well-balanced for the lake at rest (§3.3, proof in App. B, Eqs. (60)–(63)). **Proved**
8. Including the jump of $\mathcal S$ in the global flux does not affect the moving-equilibrium property of Prop. 3.1 (Remark 3.4). **Stated**
9. The interface jump of $\mathcal S$ is "similar to classical strategies used in well-balanced path conservative methods" with a linear path (§3.3, p. 9). **Stated**
10. The interface depth is recovered from the reconstructed $hv$, $K_2$, $\mathcal S$ by solving a depressed cubic. A positive root exists only if $(hv)^4<8(K_2-\mathcal S)^3/(27g)$ (Eq. (56)); otherwise $h=H_{\mathrm s}-b$ from the reconstructed free surface (57). For $hv\ne0$ the three roots (58)–(59) are one negative and two positive (sub- and supercritical), and the one closer to (57) is chosen (App. A). **Derived**
11. Deferred correction with $K_{\mathrm{DeC}}$ iterations has order $\min(K_{\mathrm{DeC}},\text{order of the high-order operator})$; equispaced sub-nodes give order $M_{\mathrm{DeC}}+1$, Gauss–Lobatto $2M_{\mathrm{DeC}}$ (Lobatto IIIA). Order 5 needs $K_{\mathrm{DeC}}=5$ with $M_{\mathrm{DeC}}=4$ equispaced or $3$ Gauss–Lobatto nodes (§4, pp. 10–11). **Stated**
12. All runs use CFL 0.5. The comparison scheme is standard WENO finite volumes with the Rusanov flux and Gauss–Legendre source quadrature from the analytical bottom; a "GF non-WB" variant (global flux without the lake-at-rest treatment) is also run. Still-water well-balanced methods are not compared, because earlier work found that they do not perform better on moving equilibria (§5, p. 11). **Stated**
13. Lake at rest (Table 1): GF-WENO3 and GF-WENO5 WB keep the solution to machine precision ($L^2$ errors about $10^{-13}$ in $h$ and $10^{-15}$–$10^{-14}$ in $hv$ for $N_e=25$–$800$). The non-WB errors decay with the reconstruction order, with final estimated orders 3.58/3.67 (WENO3) and 5.01/5.06 (WENO5) in $h$/$hv$ (§5.1). **Shown**
14. Perturbed lake at rest ($\alpha=10^{-4}$, $N_e=150$): standard WENO5 makes a discretization error larger than the perturbation, while GF-WENO5 WB reproduces it; WENO5 needs about $N_e=800$ to match GF at $N_e=150$ (§5.2, Figs. 4–6). **Shown**
15. On supercritical and subcritical flows over the smooth bump all schemes reach third and fifth order, but the global-flux formulation lowers the errors by 2 to 5 orders of magnitude, most of all in the WB variant (§5.3, Figs. 7–8). **Shown**
16. GF-WB costs about twice the classical scheme on a fixed mesh; for errors $10^4$ times smaller at fifth order, the classical scheme needs about 20 times more computing time for equal error (§5.3, p. 15). **Derived**. *(compiler check, not in the sources)*: a mesh factor $10^{4/5}\approx6.3$ with cost $\propto N_e^2$ gives about 40, halved by the factor 2: about 20, consistent.
17. GF-WENO5 keeps $hv$ and $K_2$ constant "up to $\sim10^{-9}$" in the moving-equilibrium tests, also with friction (§5.3, p. 15; §5.6). **Shown**
18. Transcritical flow with a shock: WENO5 produces spurious oscillations at the shock that propagate through the domain; GF-WENO5 has none and recovers the solution on both sides; $\Upsilon$ jumps at the shock (§5.3, Fig. 11). **Shown**
19. Perturbed sub- and supercritical states ($\alpha=10^{-3}$, $10^{-4}$): GF-WENO5 is accurate on $N_e=100$; WENO5 needs a much finer mesh ($N_e=800$ shown) (§5.4, Figs. 12–15). **Shown**
20. Step bathymetry (54): in the subcritical case GF-WENO5 has no oscillations and errors of order $10^{-10}$, while WENO5 oscillates strongly after the discontinuities. In the supercritical case GF-WENO5 keeps the global fluxes constant to machine precision, while WENO5 oscillates and misses the outflow state (§5.5, Figs. 16–17). **Shown**
21. With Manning friction $n_{\mathrm M}=0.05$ both schemes are consistent, but WENO5 has strong spurious oscillations where the bathymetry acts most; GF-WENO5 keeps the global-flux variables to about $10^{-9}$ (§5.6, Figs. 18–19). **Shown**
22. Perturbed friction states: the supercritical friction case is the only one in which the classical WENO reaches the steady state (residuals to machine precision), "probably" because friction stabilizes; in the subcritical friction case classical WENO5 does not reach it (§5.7, Figs. 20–21). **Shown**

# Printed slips

- Eq. (36), sign of $\bar S_i$: by the splitting (32), $S=-gH_{\mathrm s}\partial_xb+g\partial_x(b^2/2)$, but (36) prints $\bar S_i=\frac1{\Delta x}\big[+g\int H_{\mathrm s}\partial_xb\,dx-g\big((b^-_{i+1/2})^2/2-(b^+_{i-1/2})^2/2\big)\big]$. *(compiler check, not in the sources)*: with (37), $\mathcal S^-_{i+1/2}=\mathcal S^+_{i-1/2}-\Delta x\bar S_i$, the printed (36) gives the opposite sign to (35), (40) and the underbraced term of (62c), which all have $\mathcal S^-_{i+1/2}-\mathcal S^+_{i-1/2}=+g\int H_{\mathrm s}\partial_xb\,dx-g[\dots]$. The printed (36) is $-\bar S_i$.
- Eqs. (62e) and (63): $b^+_{i-1/2}$ is printed where $b^+_{i+1/2}$ follows from substituting (62c) into (62d), and (63) prints $b^-_{i-1/2}$ where (38) at $H_{\mathrm s}=\text{const}$ gives $b^-_{i+1/2}$. The definition (38) and Prop. 3.3 are unaffected.
- Eqs. (39)–(40): the friction term inside the bracket carries a factor $g$ that the outer $g$ multiplies again, giving $g^2n_{\mathrm M}^2\lvert hv\rvert hv/h^{7/3}$ against $g\,n_{\mathrm M}^2\lvert hv\rvert hv/h^{7/3}$ in (2) and (4).
- P. 5: "exploiting the relation $\partial_xR\equiv S$", while (4) defines $R:=-\int^xS$, so $\partial_xR=-S$; (18) uses the latter.
- Eq. (26): the integration cell is $i-r+j+m$ while the right-hand side is $u_{i-j+m}$; these agree only for $r=2j$.
- Eq. (39): $(b_{i,\theta})^2$ with the free index $\theta$, where (35) has $(\tilde b_{i,q})^2$.
- Table 1: the estimated orders are computed with $N_e-1$ in place of $N_e$. *(compiler check, not in the sources)*: e.g. GF-WENO3 non-WB $h$, $25\to50$: $\log(e_1/e_2)/\log2=2.74$ against the printed 2.67; using $N_e-1$ reproduces all six printed values of that column (2.67, 3.62, 3.69, 3.53, 3.53, 3.58), inconsistent with $N_e$ uniform cells of width $25/N_e$.
- §5.1: "the error decay for the non-WB simulations matches the order of the reconstruction for both GF-WENO3 and GF-WENO5", while the GF-WENO3 orders settle at 3.5–3.7.
- Figs. 7–8: axis label $(x_\ell-x_r)/N_e$, which is negative.
- §5.4: "perturbation (48)", while (48) defines only the bump function; the perturbation is the $\alpha$ term of (47).

# Notation map

| Ciallella et al. 2023 | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u=(h,q)^T$ | $u=(h,hv)$ | conserved variables |
| $h$, $q=hu$, $u$ | $h$, $hv$, $v$ | depth, discharge, velocity; **collision**: $q$ is the weight exponent and $u$ the state |
| $b$, $\eta=h+b$ | $b$, $H_{\mathrm s}$ | bottom and free surface, as on the well-balancing page; **collision**: $\eta$ is the entropy |
| $n$ | $n_{\mathrm M}$ (page-local) | Manning coefficient |
| $F$, $S$ | $f$, $S$ | flux and source |
| $R(x,t)=-\int^xS$ | $\mathcal S$ (page-local) | **collision** with the right-eigenvector matrix $R$; $\mathcal S=-\mathcal G$, the global part $\mathcal G=\int^xS$ of the [flux-globalization](/methods/flux-globalization.md) page |
| $G=(q,K)^T$, $K$ | $K=(hv,K_2)$ (page-local) | global flux, written $K$ as on the path-conservative and A-WENO pages |
| $\Upsilon$, $E$ | $\Upsilon$ | Bernoulli invariant |
| $\Omega_i$, $\Delta x$, $N_x$, $N_e$ | $I_i$, $\Delta x$, number of cells | |
| $\bar U_i$, $\bar G_i$, $\bar F_i$, $\bar R_i$, $\bar S_i$ | $\bar u_i$ and cell averages of $K$, $f$, $\mathcal S$, $S$ | finite volume |
| $\hat H_{i+1/2}$ | $\hat f_{i+1/2}$ | numerical flux |
| $G^L_{i+1/2}$, $G^R_{i+1/2}$; $R^L_{i+1/2}$, $R^R_{i-1/2}$; $b^L$, $b^R$ | $K^-$, $K^+$; $\mathcal S^-_{i+1/2}$, $\mathcal S^+_{i-1/2}$; $b^-$, $b^+$ | $\mathcal S^+_{i-1/2}$ is the cell-$i$ value at its left end |
| $[[R_{i+1/2}]]$ | $[\![\mathcal S]\!]_{i+1/2}$ | jump, registry bracket |
| $L$, $\Lambda^\pm$, $\lambda_i$ | $L$, $\Lambda^\pm$ (page-local), $\lambda_l$ | $\Lambda^\pm$ are 0/1 selectors |
| $J(U^*)$, $h_*$, $u_*$ | Roe-averaged Jacobian $A$, arithmetic depth, Roe velocity | |
| $(x_{i,q},w_q)$, $\ell_\theta$, $r^q_\theta$ | Gauss nodes and weights $\mathsf w$, Lagrange basis $\ell$ | **collision**: index $q$ |
| $p$, $r$ | design order $2r-1$, $r$ | agree with the registry's $r$ |
| $p^{HO}$, $p_m$ | $P_{\mathrm{opt}}$, $P_k$ | high-order and candidate polynomials |
| $d_m(x)$, $\beta_k$, $\alpha_k$, $\omega_m$, $\epsilon$ | $d_k$, $\beta_k$, $\alpha_k$, $\omega_k$, $\epsilon$ | Jiang–Shu, $q=2$, $\epsilon=10^{-6}$; linear weights point-dependent |
| $M$, $K$, $\theta^m_r$, $\beta^m$, $\mathcal L^1$, $\mathcal L^2$ (DeC) | $M_{\mathrm{DeC}}$, $K_{\mathrm{DeC}}$, page-local | **collisions** with the mass matrix $M$, the global flux $K$ and the indicators $\beta_k$ |
| $\alpha$, $\psi$, $r(x)$ | perturbation amplitude and bump (page-local) | not the weights $\alpha_k$ or the entropy potential $\psi$ |
| EOA | estimated order | see Printed slips |

# Reference list

The manuscript prints 67 references, numbered [1]–[67] and sorted alphabetically; none prints a
DOI. The list is merged complete into the [bibliography](/bibliography.md) with `citedby`
including `ciallella-2023`. [2], [24] and [46] are arXiv preprints, kept as their own entries.
[3] (Abgrall & Ricchiuto 2022, book chapter) shares its author–year key with a different
Source page and is re-keyed at the merge. Gómez-Bueno 2021 [33]/[34] take suffixes in printed
order. Garbled items are kept as printed: [26] (Saint-Venant 1871 venue misspelt), [36]
(Hairer–Wanner series and pages), [5] (article number "405(109173)"), [61] (doubled "PhD
thesis") and [44] (no volume). No item is unparseable.

# Pages created or updated

Chunk 6 (2026-10-23), cited further in chunks 7–8 (2026-10-23). This source is cited on:

* [Flux globalization for balance laws](/methods/flux-globalization.md)
* [Path-conservative schemes](/methods/path-conservative-scheme.md)
* [Shallow-water equations](/definitions/shallow-water-equations.md)
* [Shallow-water flow over a bump and lake at rest](/benchmarks/flow-over-a-bump.md)
* [Well-balancing](/properties/well-balancing.md)
