---
type: Source
title: "Huang & Fu (2024) — A new troubled cell indicator and a new limiter based on TENO schemes for RKDG methods"
description: "Transplants TENO's sharp cut-off into RKDG: a compact three-cell troubled-cell indicator with fixed parameters, and a TENO-weighted compact Hermite-type limiter for third-order DG in one and two dimensions, compared with KXRCF and a compact WENO limiter on Euler benchmarks."
resource: "doi:10.1016/j.cma.2024.116795"
source_kind: paper
authors: [Huang H., Fu L.]
year: 2024
venue: "Comput. Methods Appl. Mech. Eng. 421:116795"
local_file: "/home/stefano/papers/mosaic/weno-teno/2024_Crossref_Computer_Methods_in_Applied_Mechanics_and_Engineering_Huang_A_new_troubled_cell_indicator_and_a_new_limiter_based_on_TEN.pdf"
tags: [dg, teno, limiting, troubled-cell, smoothness-indicator, low-dissipation]
timestamp: 2026-10-23T23:45:00Z
---

# Summary

The paper attacks two weaknesses of limited Runge–Kutta
[discontinuous Galerkin](/methods/discontinuous-galerkin.md) (RKDG) methods. The
classical [troubled-cell indicators](/definitions/troubled-cell-indicator.md), TVB
minmod with its parameter $M$ and the KXRCF indicator, are said to need
case-dependent tuning. The compact [WENO limiters](/methods/weno-limiter-dg.md), in
particular the simple compact limiter of Zhu, Qiu & Zhu (2020), are said to be
dissipative. Both new ingredients take the stencil selection of
[TENO](/methods/targeted-eno.md): a candidate is kept with its linear weight or
dropped entirely, by a sharp cut-off $C_T$ on normalized
[smoothness measures](/definitions/smoothness-indicator.md).

The indicator works on three cells. It computes the Jiang–Shu-type indicator
$\beta_n$ of each cell's own DG polynomial on $I_{i-1}$, $I_i$, $I_{i+1}$, forms
$\gamma_n=(\beta_n+\epsilon_1)^{-6}$ with $\epsilon_1=10^{-3}$, and flags cell $i$
if its own normalized measure $\chi_i<C_T=10^{-4}$. It is a compact version of
Fu's TENO discontinuity indicator for finite differences, and it is applied
direction by direction in 2D.

The limiter is built for $P^2$ (third-order) RKDG and keeps the cell average. In 1D
it rebuilds the first and second modes from three compact Hermite-type candidates
each, with linear weights from a larger target polynomial ($\tfrac{11}{38}$,
$\tfrac{11}{38}$, $\tfrac8{19}$ and $\tfrac{45}{154}$, $\tfrac{45}{154}$,
$\tfrac{32}{77}$). The TENO weights carry a bias $t=10$ toward the central stencil.
In 2D it uses eight $P^2$ candidates on the $3\times3$ block, with minimum-norm
linear weights.

All evidence is numerical, on third-order DG with SSP-RK3, CFL 0.15 and the Rusanov
flux:

* density-wave accuracy tests in 1D and 2D: third order, and the indicator flags no
  cell;
* the Sod and Lax tubes, the Woodward–Colella blast waves and the Shu–Osher problem;
* the double Mach reflection and 2D Riemann configuration 3.

In the authors' visual comparisons the new limiter is less dissipative than the
compact WENO limiter, and the new indicator flags cells more selectively than KXRCF. The paper proves nothing and
reports no timings.

# Version read

Version of record (Elsevier typeset), 24 pages: received 2 November 2023, accepted 20
January 2024, online 25 January 2024. Title, authors, venue and DOI on page 1 match
Crossref. Equation, table and section numbers are those of this version.

# Key claims

Registry notation. $N$ is the DG degree ($N=2$ throughout), $u^{(l)}_i$ the $l$-th
modal coefficient on $I_i$ in the scaled Legendre basis $v^{(i)}_l$ (local), with
$u^{(0)}_i=\bar u_i$. The source's $\varepsilon$ is written $\epsilon$, and its
nonlinear weights $w_n$ are written $\omega_n$.

1. Traditional troubled-cell indicators (TVB minmod, KXRCF) "generally rely on a critical parameter that is dependent on the solution of PDEs and needs tuning in a case-by-case manner". The new indicator "adopts a uniform parameter for different cases", $C_T=10^{-4}$, $\epsilon_1=10^{-3}$, exponent 6 (Abstract, §4.3). **Stated** (the uniform parameters are **Shown** on the paper's tests)
2. For the TVB minmod indicator the number of troubled cells decreases as $M$ grows; too large an $M$ misses genuine troubled cells and can make the computation fail, so $M$ must be chosen per problem (§4.1). **Stated**
3. The new indicator flags cell $i$ iff $\chi_i<C_T$ (Eq. (35)), where $\chi$ normalizes $\gamma_n=(\beta_n+\epsilon_1)^{-6}$ over $n=i-1,i,i+1$ (Eqs. (32)–(34)). It uses only the immediate neighbours, unlike Fu's finite-difference indicator, which needs four candidate stencils and six points (§4.3). **Stated** (construction)
4. In 2D the indicator is applied separately in $x$ and $y$, and a cell flagged in either direction is troubled, as in Fu's hybrid finite-difference TENO (§5.1). **Stated**
5. The 1D limiter for $P^2$ keeps $u^{(0)}_i$ and rebuilds $u^{(1)}_i$ from three quadratic candidates and a quartic target, with linear weights $d_0=d_1=\tfrac{11}{38}$, $d_2=\tfrac8{19}$ (Eqs. (37)–(40)). **Derived** (the weights agree with a recomputation; *compiler check, not in the sources*)
6. $u^{(2)}_i$ is rebuilt from three cubics and a quintic target with $d_0=d_1=\tfrac{45}{154}$, $d_2=\tfrac{32}{77}$ (Eqs. (47)–(49)). **Derived** (the weights agree with a recomputation; *compiler check, not in the sources*)
7. The limiter's weights are $\gamma_n=t_n/(\beta_n+\epsilon_2)^6$ with $t_0=t_1=1$ and $t_2=10$ "to enlarge the chance to choose the central stencil", $\epsilon_2=10^{-10}$, cut-off $C_T=10^{-4}$, and $\omega_n=d_n\delta_n/\sum_ld_l\delta_l$ (Eqs. (42)–(45)). **Stated** (design)
8. The limiter runs only in cells flagged by the new indicator; elsewhere the RKDG scheme is unmodified (§4.4). **Stated**
9. The 2D limiter uses eight $P^2$ candidates on the $3\times3$ block. Four match the averages of a $2\times2$ block plus one $x$- and one $y$-moment; four match six cell averages. Exactness conditions plus a minimum-norm constraint give $d^{(l)}_{1..4}=\tfrac{11}{76}$ and $d^{(l)}_{5..8}=\tfrac2{19}$ for the first-order modes $l=1,2$, and $d^{(l)}_n=\tfrac18$ for the second-order modes $l=3,4,5$ (Eqs. (52)–(58)). **Derived**
10. For the second-order modes the 2D smoothness indicators add first-derivative terms to those of the HWENO limiter "for better robustness" (§5.2 after Eq. (59), §7). **Stated** (no ablation)
11. 1D density wave (Table 1): RKDG with the WENO limiter, with the new limiter and without limiter give identical errors ($L^1$: $3.53\times10^{-7}$, $4.43\times10^{-8}$, $5.55\times10^{-9}$, $6.94\times10^{-10}$ at $N_x=100$–$800$; orders 2.99, 3.00, 3.00), so the new indicator activates no limiter on the smooth solution (§6.1.1). **Shown**
12. With the TVB indicator at $M=1$ forcing limiting in some cells, both limiters converge at third order (Table 2; new limiter $L^1$ $3.02\times10^{-6}$ to $5.58\times10^{-9}$ for $N_x=50$–$400$, orders 3.05, 3.02, 3.01) (§6.1.1). **Shown** (but see Printed slips)
13. KXRCF activation in the accuracy tests is "parameter-dependent", depending on the parameter settings and the mesh, which is why the TVB indicator, which "always labels some troubled cells regardless of its parameter", is used to test the limiter's order (§6.1.1). **Stated**
14. Other indicators such as TVB minmod "may activate limiters in this case [17], because they incorrectly mark cells with smooth extrema as troubled cells" (§6.1.1). **Stated** (cited)
15. 2D density wave (Table 3): the three schemes again give identical errors ($L^1$ $1.22\times10^{-4}$ to $2.46\times10^{-7}$ from $20^2$ to $160^2$; orders 2.98, 2.98, 2.99). With TVB at $M=1$ the new limiter is third order (Table 4: $L^1$ orders 2.79, 2.90, 2.99; $L^\infty$ 3.11, 3.12, 2.92) (§6.1.2). **Shown**
16. Sod and Lax tubes ($N_x=100$): the new indicator flags troubled cells "much more precisely" than KXRCF, and the new limiter is oscillation-free and less dissipative than the WENO limiter (§6.2, Figs. 4–5). **Shown** (visual)
17. Woodward–Colella blast waves ($N_x=400$): both limiters run robustly with the new indicator; the new indicator is more precise than KXRCF and the new limiter "much better" in the zooms (§6.3, Fig. 6). **Shown** (visual)
18. Shu–Osher ($N_x=200$): the new limiter resolves the high-wavenumber fluctuations "substantially better than WENO". The under-resolved fluctuations (about $x=5.6$ to $7.2$) must themselves be flagged; KXRCF misses them and the new indicator does not (§6.4, Fig. 7). **Shown**
19. Double Mach reflection ($1000\times250$, $1500\times375$): the new indicator is "much more precise than the KXRCF indicator with less noise", and the new limiter resolves richer small scales than the WENO limiter in $[2,2.8]\times[0,0.6]$ (§6.5, Figs. 8–11). **Shown** (visual)
20. 2D Riemann configuration 3 ($700^2$, $1000^2$): KXRCF labels "over 50 percent of cells" as troubled and is not plotted. The new limiter shows "much richer small-scale structures" than the WENO limiter. Both solutions are asymmetric, which the authors attribute to low dissipation failing to damp round-off disturbances (§6.6, Figs. 12–15). **Shown** / **Stated** (attribution)
21. Indicator and limiter use compact stencils only and are "straightforward to be implemented into an existing RKDG code"; 3D poses no obvious theoretical barrier, and unstructured meshes are future work (§7). **Stated**
22. TENO schemes (finite difference and finite volume) have "better numerical robustness and lower dissipation properties than WENO schemes" (§1). **Stated** (cited)

# Printed slips

- Eq. (38), fourth line: printed $\int_{I_i}q\,v^{(i)}_1dx=c_1\big(\tfrac{15}{19}(u^{(0)}_{i-1}-u^{(0)}_{i+1})-\tfrac{11}{38}(u^{(1)}_{i-1}+u^{(1)}_{i+1})\big)$. Solving for the quartic that matches the three averages and the first moments of $I_{i\pm1}$ gives $\tfrac{15}{19}(u^{(0)}_{i+1}-u^{(0)}_{i-1})$: the sign of the average term is reversed. A linear $u=(x-x_i)/\Delta x$ has moment $c_1$; the printed line gives $-\tfrac{41}{19}c_1$. The other three lines of (38) and the weights (40), (49) agree with the recomputation *(compiler check, not in the sources)*.
- Table 2, "RKDG with the new limiter", $N_x=50$: the $L^\infty$ error is printed $5.38\times10^{-7}$. That is smaller than the $N_x=100$ value $5.56\times10^{-7}$ and than the same row's $L^1$ error, and it contradicts the printed order 3.27. $\log_2(5.38\times10^{-6}/5.56\times10^{-7})=3.27$, so the value is $5.38\times10^{-6}$ *(compiler check, not in the sources)*.
- Eq. (56) imposes exactness "for $u=v^{(ij)}_1,v^{(ij)}_2,\dots,v^{(ij)}_9$", but Eq. (21) defines only $v_0,\dots,v_5$. Without $v_6$–$v_9$ the derivation of (58) cannot be reproduced from the paper.
- §6.3 credits the blast waves to "Woodward and Colella [63]"; ref. [63] prints only P. Woodward as author.
- §2: "TENO family schemes are firstly proposed in [30–34]". $q$ is both the TENO exponent and the target polynomial $q(x)$ of §4.4.
- References: [56] "withobstacles"; [12] and [29] print no volume; [5] prints "Acta Mech. Sin. 4 (2024)" with no pages.

# Notation map

| Huang & Fu 2024 | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u^L_{i+1/2}$, $u^R_{i+1/2}$ | $u^-_{i+1/2}$, $u^+_{i+1/2}$ | |
| $u^L_{n,i+1/2}$, $n=0,\dots,3$ | candidate values on $S_n$ | **collision**: $S_0$ is the central stencil, $S_1$ downwind, $S_2$ upwind, $S_3$ the 5-point one; the registry's $S_0$ is the most upwind |
| $d_n$ (§2); $d_n$, $d^{(l)}_n$ (§§4–5) | $d_k$ | TENO5 linear weights $\tfrac6{10},\tfrac3{10},\tfrac1{10}$; limiter linear weights |
| $\beta_{n,r}$, $\beta_n$, $\beta^{(l)}_n$ | $\beta_k$ | per stencil (§2), per cell (§4.3), per candidate (§4.4) |
| $\tau_5$, $\tau_K$ | $\tau_5$ | $\lvert\beta_{3,5}-\tfrac16(\beta_{1,3}+\beta_{2,3}+4\beta_{0,3})\rvert$ |
| $\gamma_n$, $\chi_n$, $\delta_n$, $C_T$ | $\gamma_k$, $\chi_k$, $\delta_k$, $C_T$ | agree; Eq. (8) has $C$ and $\tau$, Eqs. (33), (42) do not |
| $\varepsilon$, $\varepsilon_1$, $\varepsilon_2$ | $\epsilon$, $\epsilon_1$, $\epsilon_2$ | $10^{-40}$, $10^{-3}$, $10^{-10}$ |
| $t_n$ | bias (local) | 10 for the central or six-cell stencils |
| $w_n$ | $\omega_n$ | nonlinear weights |
| $q$ | $q$ | exponent 6; **collision**: also the target polynomial $q(x)$ |
| $k$ | $N$ | DG degree |
| $N$ (grid) | $N_x$, $N_x\times N_y$ | **collision** with the DG degree $N$ |
| $v^{(i)}_l$, $v^{(ij)}_l$; $c_l$, $a_l$ | scaled Legendre basis and its norms (local) | **collision**: $v$ is the registry velocity, $c$ the sound speed |
| $u^{(l)}_i$, $u^{(l)}_{ij}$ | modal coefficients (local) | $u^{(0)}_i=\bar u_i$ |
| $M$ | TVB parameter (local) | **collision** with the mass matrix $M$ and the Mach number |
| $I^{KXRCF}_i$, $h$, $\partial I^-_i$ | KXRCF quantity, circumradius, inflow boundary | threshold 1 |
| $u$ (velocity in tests) | $v$ | |

# Reference list

The paper prints 67 references, numbered [1]–[67]. The list is merged complete into
the [bibliography](/bibliography.md) with `citedby` including `huang-2024`.
Same-author same-year works take suffixes in printed order (Cockburn 1989 [8]/[9],
Qiu 2005 [15]/[18], Fu 2019 [33], [34], [35], [46], [50], [55], Fu 2022 [2]/[47]).
[1] (Fu, Karp, Bose, Moin & Urzay, J. Fluid Mech. 909) is a different work from the
ingested source `fu-2021`, and [4] (Bai, Griffin & Fu, AIAA J. 60) a different work
from the source `bai-2022`; both are keyed apart. [5], [12], [29] and [56] are
incomplete as printed (see Printed slips). No item is unparseable.

# Pages created or updated

Chunk 7 (2026-10-23), cited further in chunk 8 (2026-10-23). This source is cited on:

* [Discontinuous Galerkin method](/methods/discontinuous-galerkin.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [Targeted ENO (TENO)](/methods/targeted-eno.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
* [WENO limiters for discontinuous Galerkin](/methods/weno-limiter-dg.md)
