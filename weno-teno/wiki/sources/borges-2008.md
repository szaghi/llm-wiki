---
type: Source
title: "Borges et al. (2008) — An improved weighted essentially non-oscillatory scheme for hyperbolic conservation laws"
description: "Introduces WENO-Z: fifth-order finite-difference WENO weights built with the global smoothness indicator τ5=|β0−β2|, analyses their order at critical points (fourth at a first-order critical point, fifth with q=2), and attributes the gain over WENO-JS on shock problems to larger weights on discontinuous stencils, at lower cost than mapped WENO."
resource: "doi:10.1016/j.jcp.2007.11.038"
source_kind: paper
authors: [Borges R., Carmona M., Costa B., Don W.S.]
year: 2008
venue: "J. Comput. Phys. 227(6):3191-3211"
local_file: "/home/stefano/papers/mosaic/weno-teno/2008_Crossref_Journal_of_Computational_Physics_Borges_An_improved_weighted_essentially_non-oscillatory_scheme_for.pdf"
tags: [weno, weno-z, weno-weights, smoothness-indicator, critical-points]
timestamp: 2026-10-30T08:43:00Z
---

# Summary

Borges et al. (2008) introduce [WENO-Z](/methods/weno-z.md), a change of the nonlinear weights
of the fifth-order finite-difference [WENO-JS](/methods/weno-js-reconstruction.md) scheme of
[Jiang & Shu (1996)](/sources/jiang-1996.md) on the
[conservative finite-difference](/definitions/conservative-finite-difference-scheme.md) flux form.
Candidate stencils, linear weights and Jiang–Shu [smoothness indicators](/definitions/smoothness-indicator.md)
are kept; a global indicator on the five-point stencil, $\tau_5=\lvert\beta_0-\beta_2\rvert$, is
$O(\Delta x^5)$ in smooth regions, and the weights become
$\alpha_k=d_k\big(1+(\tau_5/(\beta_k+\epsilon))^q\big)$, with $q=1$ in all experiments and
$\epsilon=10^{-40}$.

Recalling the necessary and sufficient conditions of Henrick, Aslam & Powers for fifth order,
the authors show that WENO-Z meets the sufficient condition $\omega_k-d_k=O(\Delta x^3)$ away
from [critical points](/properties/critical-point-accuracy.md), and analyse its order at a
critical point of order $n_{\mathrm{cp}}$: fifth for $n_{\mathrm{cp}}=0$, fourth for $n_{\mathrm{cp}}=1$ (WENO-JS: third), second for
$n_{\mathrm{cp}}\ge2$; $q=2$ restores fifth order at $n_{\mathrm{cp}}=1$. The [mapped WENO](/methods/mapped-weno.md) of
Henrick et al. serves as the comparator.

The central interpretive claim is that WENO-M and WENO-Z improve on WENO-JS for shock problems
not through their order at critical points but through the larger weights they give stencils
crossing a discontinuity, i.e. less [numerical dissipation](/definitions/numerical-dissipation.md):
about $10^{-4}$ for WENO-Z against $10^{-8}$ for WENO-JS. Raising $q$ raises the critical-point
order but adds dissipation.

The tests use characteristic-wise ([characteristic decomposition](/methods/characteristic-decomposition.md))
[Lax–Friedrichs](/methods/lax-friedrichs-flux.md) splitting and third-order TVD
[Runge–Kutta](/methods/ssp-runge-kutta.md) time stepping: the
[composite-wave advection](/benchmarks/jiang-shu-composite-advection.md),
[Sod and Lax](/benchmarks/sod-and-lax-shock-tubes.md), the
[123 problem](/benchmarks/double-rarefaction-problem.md), the
[Shu–Osher problem](/benchmarks/shu-osher-problem.md), the
[blast waves](/benchmarks/woodward-colella-blast-wave.md), a Mach 3
[shock–vortex interaction](/benchmarks/shock-vortex-interaction.md) and a Xe/Ar
[Richtmyer–Meshkov instability](/benchmarks/richtmyer-meshkov-instability.md). WENO-Z matches or
slightly sharpens WENO-M and beats WENO-JS, and runs about 25% faster than WENO-M in the same code.

# Version read

Version of record (J. Comput. Phys. 227:3191–3211), 21 pages, all read: text extraction plus
visual reading of pp. 3193–3209 (equations, Tables 1–5, test data). Received 22 September 2007,
revised 15 November 2007, accepted 21 November 2007, online 8 December 2007. The DOI is printed
on page 1; page 1 matches the Crossref record. No identity problem. Label in this bundle:
Borges et al. (2008).

# Key claims

Registry notation: weight exponent $q$ (source $p$ for WENO-JS, $q$ for WENO-Z), critical-point
order $n_{\mathrm{cp}}$ ($n_{\mathrm{cp}}=0$ a non-critical point), Taylor coefficients $\mathsf a_k$ of the
candidate errors (source $A_k$, as on the critical-point page), velocity $v$ and pressure $p$
(source $U$, $u$, $P$), vortex strength $\mathcal E$ (source $\Gamma$). Page-local: $\beta^z_k$ the
normalised WENO-Z indicators, $s$, $s_1$, $s_2$ the orders of the scheme, of
$\sum_k\mathsf a_k(\omega^+_k-\omega^-_k)$ and of $\omega_k-d_k$, $f^{(l)}_i$ the derivatives of $f$
at $x_i$.

1. WENO-Z modifies only the weights of fifth-order WENO-JS, building from the existing $\beta_k$ a higher-order indicator $\tau_5=\lvert\beta_0-\beta_2\rvert$ (Abstract; §3, Eq. (25)). **Stated** (definition)
2. The truncation error of $\tau_5$ is printed as $\frac{13}3\lvert f''_if'''_i\rvert\Delta x^5+O(\Delta x^6)$ (Eq. (26)), "straightforward" from Eqs. (12)–(14). **Derived** (see Printed slips)
3. If $S^5$ holds no discontinuity, $\tau_5=O(\Delta x^5)\ll\beta_k$; if the solution is continuous on some $S_k$ but not on $S^5$, $\beta_k\ll\tau_5$ for those $k$; $\tau_5\le\max_k\beta_k$ (§3). **Stated**
4. Away from critical points, with $\epsilon=0$, $1+\tau_5/\beta_k=1+O(\Delta x^3)$ and $\omega_k=d_k+O(\Delta x^3)$, the sufficient condition (23), hence formal fifth order (§3, Eq. (29)). **Derived**
5. Necessary and sufficient conditions for fifth order, recalled from Henrick et al. and re-derived in Eqs. (15)–(19): $\sum_k(\omega^\pm_k-d_k)=O(\Delta x^6)$ (always true by normalisation), $\sum_k\mathsf a_k(\omega^+_k-\omega^-_k)=O(\Delta x^3)$, $\omega^\pm_k-d_k=O(\Delta x^2)$; sufficient: $\omega^\pm_k-d_k=O(\Delta x^3)$ (§2, Eqs. (20)–(23)). **Derived**
6. WENO-JS weights: since $\beta_k=D(1+O(\Delta x^2))$ at smooth non-critical points, $\omega_k=d_k+O(\Delta x^2)$, so condition (21) must also hold, which "can be easily confirmed with any symbolic calculation"; at a first-order critical point $\omega_k=d_k+O(\Delta x)$ and the scheme is third order; if $f''$ also vanishes, second order (§2, after Henrick et al.). **Stated**
7. The deficiency of WENO-JS at critical points was hidden by $\epsilon=10^{-6}$, which dominates $\beta_k$ in the denominators (§2, Remark 2, §4, after Henrick et al.). **Stated**
8. The mapping of Henrick et al. does not raise the order when $f''$ also vanishes at the critical point: $\beta_k=D(1+O(1))$, $\omega_k=d_k+O(1)$, second order as for WENO-JS (§2, after Eq. (24)). **Derived**
9. Remark 1: the authors "do not credit" the improvements of WENO-M on shock problems to its higher order at critical points, "but to the smaller dissipation that results from the assignment of larger weights to discontinuous stencils", "distinctly from" Henrick et al. (§2). **Stated** (supported by §§3–5)
10. With a discontinuity in $S_2$ only, $\beta^z_k/\beta^z_2=(\beta_k/\beta_2)(\beta_2+\tau_5)/(\beta_k+\tau_5)\ge\beta_k/\beta_2$ for $k=0,1$, so the discontinuous stencil gains relative weight compared with WENO-JS (§3, Eq. (31)). **Derived**
11. Near the jump of the piecewise-sine data (30), WENO-JS gives discontinuous stencils weights "around $10^{-8}$", WENO-M a small increase, and WENO-Z "a more substantial increase to $10^{-4}$" ($\epsilon=10^{-6}$ for JS, $10^{-40}$ for M and Z) (§3, Fig. 3). **Shown**
12. $\tau_5$ is comparable to one of the $\beta_k$ only on stencils containing the discontinuity (§3, Fig. 2(b), $\epsilon=10^{-40}$). **Shown**
13. The order of WENO-Z is $s=\min(5,s_1+2,s_2+3)$ (§4, Eqs. (32)–(34)). **Derived**
14. At a critical point of order $n_{\mathrm{cp}}$, $\beta_k=O(\Delta x^{2(n_{\mathrm{cp}}+1)})$, and $\tau_5=O(\Delta x^5)$ if $n_{\mathrm{cp}}\le1$, $O(\Delta x^{2(n_{\mathrm{cp}}+1)})$ otherwise; hence $s_2=3,1,0$ for $n_{\mathrm{cp}}=0,1,\ge2$ (§4, Eqs. (37)–(38)). **Derived**
15. A symbolic algebra program gives $s_1=6,2,0,0$ for $n_{\mathrm{cp}}=0,1,2,\ge2$, hence $s=5,4,2,2$: WENO-Z is fourth order at a first-order critical point, WENO-JS third (§4, Tables 1–2). **Derived** (symbolic computation, not shown)
16. With $q=2$ in Eq. (42), fifth order is reached at $n_{\mathrm{cp}}=1$ (§4). **Derived** / **Shown** (Table 3)
17. Table 3 ($L^\infty$ error at $x=0$ of the reconstruction of $f(x)=x^3+\cos x$, $\epsilon=10^{-40}$, 64-digit Matlab variable precision, $\Delta x$ from $10^{-3}$ to $6.25\times10^{-5}$): WENO-JS orders 2.95, 2.97, 2.98, 2.99; WENO-Z $q=1$ 3.93, 3.96, 3.98, 3.99; WENO-Z $q=2$ 4.80, 4.91, 4.96, 4.98; extended precision was "necessary because of the roundoff error in the standard double precision due to the very small values of $\Delta x$" (§4). **Shown**
18. Increasing $q$ brings the scheme closer to the central scheme in smooth regions but, at discontinuities, lowers the relative weight of the discontinuous substencil, "making the scheme more dissipative" (§4, after Eq. (42)). **Stated** (qualitative argument)
19. Fourth order at critical points does not keep WENO-Z ($q=1$) from matching WENO-M on shock problems; "the larger weights attributed to discontinuous stencils … is the essential improvement of these schemes with respect to WENO-JS" (§4). **Shown** (Fig. 2, §5)
20. $q=1$ and $q=2$ show "the same order of convergence at discontinuous solutions", so only $q=1$ is presented (§5). **Stated** (no data shown)
21. Composite-wave advection, $t=8$: $L_1$ errors at $N=1600$ are $9.93\times10^{-3}$ (WENO-JS), $7.73\times10^{-3}$ (WENO-Z) and $8.06\times10^{-3}$ (WENO-M), all orders about 1; WENO-Z is "quantitatively and qualitatively equivalent to WENO-M" (§5.1, Table 4, Figs. 4–5). **Shown**
22. Sod, Lax and 123 problems with $N=200$: WENO-Z and WENO-M are more accurate than WENO-JS "due to their lesser dissipativity" (§5.2.1, Fig. 6). **Shown**
23. Shu–Osher problem ($k=5$, $N=200,300$; $k=10$, $N=510$): WENO-M and WENO-Z capture more fine-scale structure than WENO-JS and converge faster (§5.2.2, Figs. 7–8). **Shown**
24. Blast waves ($N=400,800$): WENO-Z gives a sharper peak near $x=0.78$ and resolves the structure at $x=0.86$ and the contact near $x=0.8$ better than WENO-M (§5.2.3, Figs. 9–10). **Shown**
25. CPU time per Runge–Kutta step, shock–vortex: $400^2$: WENO-JS 1.47 s, WENO-Z 1.39 s, WENO-M 1.87 s; $800^2$: 6.54, 6.15, 8.27 s (Table 5); Richtmyer–Meshkov $800^2$: 6.46, 6.07, 8.13 s (Table 6); WENO-Z "is the most efficient scheme and about 25% faster than the WENO-M scheme, since WENO-Z does not make use of any mapping"; one code on an AMD Opteron 250, same subroutines and compiler options, only the weight routine differing (§5, §5.3.1). **Shown** *(Compiler check, not in the sources: WENO-Z/WENO-M time ratios $1.39/1.87=0.743$, $6.15/8.27=0.744$, $6.07/8.13=0.747$.)*
26. On the Richtmyer–Meshkov problem WENO-Z is "equivalent" to WENO-M at $800^2$ (§5.3.2, Fig. 13). **Shown**
27. Conclusions: WENO-Z gives the accuracy of WENO-M at smaller cost; its convergence rate at critical points "is intermediary between" WENO-JS and WENO-M; extension to higher order is "currently underway" (§6). **Stated**

Setting: point values on $x_i=i\Delta x$, implicit flux function of Shu & Osher, candidates
$\hat f^k_{i+1/2}=h_{i+1/2}+\mathsf a_k\Delta x^3+O(\Delta x^4)$ (Eq. (6)); WENO-JS weights
$\alpha_k=d_k/(\beta_k+\epsilon)^q$, $q=2$, $\epsilon=10^{-6}$ ("commonly suggested", kept for WENO-JS
"to compare with the classical scheme at its best"); $\beta_k$ by Eq. (8) with expansions (12)–(14)
that carry the $\Delta x^5$ terms $\mp(\frac{13}6f''_if'''_i-\frac12f'_if''''_i)$; normalised
indicators $\beta^z_k=(\beta_k+\epsilon)/(\beta_k+\tau_5+\epsilon)$ (27); mapping of Henrick et al.
$g_k(\omega)=\omega(d_k+d_k^2-3d_k\omega+\omega^2)/(d_k^2+\omega(1-2d_k))$ (24); TVD RK3 (43) at CFL 0.4
with $\Delta t$ bounded by $\Delta x^{5/3}$; Roe eigenvectors and the first-order Lax–Friedrichs
flux as building block for Euler (§5.2). The shock–vortex test is a Mach 3 shock with the Kopriva
vortex ($\mathcal E=0.25$, radii 0.2 and 1, $t=1$, inflow/outflow in $x$, periodic in $y$); the
Sod tube is placed on $[-5,5]$ with the low-pressure state on the left (Eq. (48)).

# Printed slips

- **Lax left state** (§5.2.1, Eq. (49)): printed $(\rho,u,p)=(0.445,0.698,0.3528)$; the other sources on the [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md) page, among them Harten et al. (1987a), Liu et al. (1994), Jiang & Shu (1996) and Fu et al. (2016), print the left pressure $3.528$. The text does not show which value was run.
- **Linear weights against stencil labelling** (§2): $d_0=\frac3{10}$, $d_1=\frac35$, $d_2=\frac1{10}$
  are printed while Fig. 1 and Eqs. (9)–(11) place $S_0=\{x_{i-2},x_{i-1},x_i\}$ upwind of
  $x_{i+1/2}$; Jiang & Shu (1996, Table 2) give $(\frac1{10},\frac6{10},\frac3{10})$ with $S_0$ the
  most upwind. The printed values fit instead Eq. (5), $\hat f^k_{i+1/2}=\sum_jc_{kj}f_{i-k+j}$ with
  $k$ the "left-shift parameter", under which $k=0$ is $\{x_i,x_{i+1},x_{i+2}\}$. $\tau_5$ is
  symmetric in $\beta_0$, $\beta_2$ and unaffected.
- **Eq. (26)**: from the paper's Eqs. (12) and (14),
  $\beta_0-\beta_2=-2\big(\frac{13}6f''_if'''_i-\frac12f'_if''''_i\big)\Delta x^5+O(\Delta x^6)$, i.e.
  $\tau_5=\big\lvert\frac{13}3f''_if'''_i-f'_if''''_i\big\rvert\Delta x^5+O(\Delta x^6)$ *(compiler
  check, not in the sources: difference of (12) and (14))*; the printed
  $\frac{13}3\lvert f''_if'''_i\rvert\Delta x^5$ omits the $f'_if''''_i$ term. $\tau_5=O(\Delta x^5)$
  is unaffected.
- Eq. (3) prints $\frac{du_i}{dt}=\frac1{\Delta x}(h_{i+1/2}-h_{i-1/2})$ without the minus sign of
  Eq. (2).
- **Table 1**: the column "$\ge2$" prints $O(\Delta x^{12(n_{cp})})$, while the column $n_{cp}=2$
  prints $O(\Delta x^{36})$ for both rows; Tables 1–2 carry both a "2" and a "$\ge2$" column.
- **Table 3**: the first WENO-JS error is printed $0.16\mathrm e{-10}$ at $\Delta x=10^{-3}$, followed
  by $2.09\mathrm e{-10}$ with order 2.95. *(Compiler check, not in the sources:
  $\log_2(1.6\times10^{-9}/2.09\times10^{-10})=2.94$, so $0.16\mathrm e{-8}$ fits the printed order.)*
- Eq. (42) repeats the middle expression $d_k/\beta^z_k$, which equals
  $d_k\big(1+(\tau_5/(\beta_k+\epsilon))^q\big)$ only for $q=1$.
- §2 calls the three-point candidate $\hat f^k$ "the third degree polynomial".
- Eq. (35) defines $n_{cp}$ "for a critical point of order $n_{cp}\ge1$", while Tables 1–2 and
  Eq. (38) use $n_{cp}=0$ for non-critical points.
- Richtmyer–Meshkov data: $A_t=0.54$ with $\rho_{\mathrm{Xe}}=2.90\times10^{-3}$ and
  $\rho_{\mathrm{Ar}}=0.89\times10^{-3}$ g/cm³. *(Compiler check, not in the sources:
  $(2.90-0.89)/(2.90+0.89)=0.530$.)*
- §3 says the new weights satisfy "the necessary and sufficient conditions (22)", while Eq. (29)
  shows the sufficient condition (23).
- Notation drift: superscripts $z$ and $Z$; "$\beta^k_z$" in the text before Eq. (27). References:
  [4] "Approximation Riemann solvers", [7] "Collela".

# Notation map

| Borges et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $S^5$, $S_0,S_1,S_2$ | $S^5$, $S_k$ | Fig. 1 labelling, $S_0$ leftmost; Eq. (5) uses the opposite one |
| $\hat f^k$, $c_{kj}$ | $\hat f^{(k)}_{i+1/2}$, candidate coefficients | |
| $h(x)$, $h_{i\pm1/2}$ | implicit flux function | **collision** with the two-point flux $h$ |
| $d_k$, $\alpha_k$, $\omega_k$, $\beta_k$, $\epsilon$ | agree | $\epsilon=10^{-6}$ (JS), $10^{-40}$ (M, Z) |
| $p$ | $q$ | WENO-JS exponent 2 |
| $q$ | $q$ | WENO-Z exponent, 1 in all tests |
| $\tau_5$ | $\tau_5$ | agree |
| $\alpha^z_k$, $\omega^z_k$, $\omega^M_k$ | $\alpha_k$, $\omega_k$ of WENO-Z and mapped WENO | |
| $\beta^z_k$ | local | normalised indicators |
| $g_k(\omega)$ | $g(\omega)$ | mapping of mapped WENO |
| $A_k$, $B^\pm$ | $\mathsf a_k$, local | |
| $n_{cp}$ | $n_{\mathrm{cp}}$ | critical-point order, as on the critical-point page |
| $s$, $s_1$, $s_2$, $\Omega^\pm$, $N^\pm$, $D^\pm$, $F^\pm_k$ | local | order analysis of §4 |
| $Q$, $U$, $P$ | $u$, $v$, $p$ | **collision** of $U$/$u$ with the conserved variables |
| $\Gamma$, $r_0$, $r_1$, $M_s$ | $\mathcal E$, local radii, $M$ | shock–vortex |
| $\alpha$, $\beta$, $\delta$ in Eqs. (44), (57)–(58) | local | composite profile and diffuse-interface shape; **collision** with $\alpha_k$, $\beta_k$ |

# Reference list

The paper prints 8 references, numbered [1]–[8]. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` including `borges-2008`. [2] is
[Jiang & Shu (1996)](/sources/jiang-1996.md); Shu & Osher's 1988 paper is
[Shu & Osher (1988)](/sources/shu-1988.md), distinct from its 1989 part II. [8] (Kopriva, in Lee &
Schultz (eds.), Computational Acoustics, vol. 2, 1988) prints no publisher or pages; [4] (Roe)
prints only the first page; [4] and [7] carry the spellings noted above. No item is unparseable.

# Pages created or updated

Chunk 12 (2026-10-30). This source is cited on:

* [Accuracy at critical points](/properties/critical-point-accuracy.md)
* [Characteristic decomposition](/methods/characteristic-decomposition.md)
* [Conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
* [Double rarefaction (123) problem](/benchmarks/double-rarefaction-problem.md)
* [ENO property](/definitions/eno-property.md)
* [Jiang–Shu composite-wave advection](/benchmarks/jiang-shu-composite-advection.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [Mapped WENO](/methods/mapped-weno.md)
* [Numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
* [Richtmyer–Meshkov instability](/benchmarks/richtmyer-meshkov-instability.md)
* [Shock–vortex interaction](/benchmarks/shock-vortex-interaction.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [WENO-JS reconstruction](/methods/weno-js-reconstruction.md)
* [WENO-Z weights](/methods/weno-z.md)
* [Woodward–Colella interacting blast waves](/benchmarks/woodward-colella-blast-wave.md)
