---
type: Source
title: "Jiang & Shu (1996) — Efficient implementation of weighted ENO schemes"
description: "Recasts weighted ENO in the Shu–Osher finite-difference flux form, shows that the Liu–Osher–Chan indicators give only order r+1, introduces the integral smoothness indicators that make the r=3 scheme fifth order (the scheme later called WENO-JS), and adds pressure–entropy weights, artificial compression, a convergence argument, timings and the standard Euler tests."
resource: "doi:10.1006/jcph.1996.0130"
source_kind: paper
authors: [Jiang G.-S., Shu C.-W.]
year: 1996
venue: "J. Comput. Phys. 126(1):202-228"
local_file: "/home/stefano/papers/mosaic/weno-teno/1996_Crossref_Journal_of_Computational_Physics_Jiang_Efficient_Implementation_of_Weighted_ENO_Schemes.pdf"
tags: [weno, finite-difference, smoothness-indicator, weno-weights, characteristic]
timestamp: 2026-10-30T08:09:00Z
---

# Summary

Jiang & Shu (1996) analyse, modify and test the weighted ENO schemes of
[Liu et al. (1994)](/sources/liu-1994.md), recast in the
[conservative finite-difference](/definitions/conservative-finite-difference-scheme.md) flux
form of [Shu & Osher (1988)](/sources/shu-1988.md): the point values of a split flux are cell
averages of an implicit function $\phi$, and the numerical flux is a convex combination of the $r$
candidate [ENO](/methods/eno-reconstruction.md) fluxes with weights
$\alpha_k=d_k/(\epsilon+\beta_k)^q$, $q=2$, $\epsilon=10^{-6}$.

A truncation-error analysis shows that the weights reach order $2r-1$ if
$\omega_k=d_k+O(\Delta x^{r-1})$, and that Liu et al.'s indicators give only $\omega_k=d_k+O(\Delta x)$,
hence order $r+1$; the higher orders in Liu et al.'s tables are attributed to coarse-grid errors
and to $\epsilon$ dominating the indicators on fine grids. The central contribution is a new
[smoothness indicator](/definitions/smoothness-indicator.md), the sum of scaled squared $L^2$
norms of all derivatives of the candidate polynomial on the cell, which for $r=3$ gives the
$\frac{13}{12}$, $\frac14$ formulas and a fifth-order scheme, the one later literature calls
[WENO-JS](/methods/weno-js-reconstruction.md). The paper states that the new weights are also
fifth order at [critical points](/properties/critical-point-accuracy.md). Weights are
[ENO](/definitions/eno-property.md)-like at discontinuities but not "digital".

For the Euler equations the scheme is applied field by field after
[characteristic decomposition](/methods/characteristic-decomposition.md) with Roe or arithmetic
averages; a cheaper variant takes the weights from pressure and entropy and needs only two
projections, but fails at reflective walls. Yang's [artificial compression](/methods/artificial-compression.md)
sharpens contacts. A convergence result for smooth solutions follows from Strang's theorem,
because the scheme with a smooth splitting such as global
[Lax–Friedrichs](/methods/lax-friedrichs-flux.md) ([flux splitting](/methods/flux-vector-splitting.md))
is infinitely differentiable. Timings on a CRAY C-90 show WENO about twice as fast as ENO.
Time stepping is the third-order TVD [Runge–Kutta](/methods/ssp-runge-kutta.md) scheme or a
non-TVD RK4. The split fluxes are the [monotone](/definitions/monotone-scheme.md) building blocks of
the scheme; [Roe](/methods/roe-riemann-solver.md)-type building blocks are compared with
Lax–Friedrichs ones in operation count and timing.

The Euler tests became standard: [Sod and Lax](/benchmarks/sod-and-lax-shock-tubes.md), a
[shock–entropy wave](/benchmarks/shu-osher-problem.md), the
[blast waves](/benchmarks/woodward-colella-blast-wave.md), a [nozzle](/benchmarks/steady-shock-problems.md),
the [forward step](/benchmarks/forward-facing-step.md), the
[double Mach reflection](/benchmarks/double-mach-reflection.md),
[shock–vortex interaction](/benchmarks/shock-vortex-interaction.md) and a
[cylinder](/benchmarks/flow-past-circular-cylinder.md), plus the scalar
[composite-wave advection](/benchmarks/jiang-shu-composite-advection.md) and
[Buckley–Leverett](/benchmarks/buckley-leverett-problem.md).

# Version read

Author preprint, not the typeset JCP version: a title page numbered "i" and 39 numbered pages
(40 PDF pages), LaTeX typesetting, with no report number, date or journal header (the PDF's
embedded metadata, not its content, give 13 January 1997). All 40 pages read; the text layer
loses minus signs and Greek letters, so every equation was transcribed from the page images.
Title and authors match the published version (J. Comput. Phys. 126:202–228, 1996), whose
metadata head this page; section, equation, table and figure numbers cited are the preprint's.
Label in this bundle: Jiang & Shu (1996).

# Key claims

Registry notation: grid index $i$ (source $j$), $\Delta x$ (source $h$ or $\Delta x$), candidate
flux $\hat f^{(k)}_{i+1/2}$ (source $q^r_k$), linear weights $d_k$ (source "optimal weights"
$C^r_k$), smoothness indicator $\beta_k$ (source $IS_k$), weight exponent $q$ (source $p$),
Lax–Friedrichs constant $a$ (source $\alpha$), vortex strength $\mathcal E$ (source $\epsilon$),
eigenvectors $L$, $R$ (source $\mathbf l_s$, $\mathbf r_s$), velocity $v$ and pressure $p$
(source $u$ or $q$, and $P$). Page-local: $\phi$ the implicit flux function (source $h$, as on the
[conservative finite-difference](/definitions/conservative-finite-difference-scheme.md) page),
$f^{(l)}$ the $l$th derivative of $f(u(x))$ at $x_i$.

1. A WENO scheme built from $r$-point ENO stencils reaches order $2r-1$ in the optimal case, the convex combination then approximating the $(2r-1)$th-order "upstream central scheme" (§1; §2, (2.9)–(2.14)). **Derived**
2. A sufficient condition for order $2r-1$ is $\omega_k=d_k+O(\Delta x^{r-1})$ (2.14); it holds if $\beta_k=D(1+O(\Delta x^{r-1}))$ with $D$ nonzero and independent of $k$ (2.17) (§2). **Derived**
3. With Liu et al.'s indicators (2.18), $\beta_k=(f'\Delta x)^2(1+O(\Delta x))$ in smooth regions (2.21), hence $\omega_k=d_k+O(\Delta x)$ (2.22) and order $r+1$ in smooth monotone regions ("This result was proven in [9] using a different approach"); for $r=3$ the second-order terms differ between stencils (2.23)–(2.25), so Liu et al.'s $r=3$ scheme "is only 3rd order accurate" at critical points (§2). **Derived**
4. Liu et al.'s apparent super-convergence is "superficial": larger errors on coarse grids (10 to 80 points per wave) and, on fine grids, $\beta_k$ smaller than $\epsilon$ pushing the weights to $d_k$ (§1; §2 p. 7; Tables 3–4). **Derived / Shown**
5. At a discontinuity a non-smooth stencil gets $\omega_l=O(\Delta x^{2q})$ (2.28); with more than one smooth stencil each gets an $O(1)$ weight, so the weights "do not exactly resemble the ENO digital weights" (§2, pp. 7–8). **Derived**
6. $q=2$ "is adequate to obtain essentially non-oscillatory approximations at least for $r=2,3$", although Liu et al. suggested $q=r$; $q=2$ is used in all tests, and "in our later tests, we will take $\epsilon=10^{-6}$" (§2, pp. 6, 8). **Stated** (test choice)
7. New indicator $\beta_k=\sum_{l=1}^{r-1}\int_{x_{i-1/2}}^{x_{i+1/2}}\Delta x^{2l-1}\big(\tfrac{d^l}{dx^l}p_k(x)\big)^2dx$ (3.1), $p_k$ the candidate interpolation polynomial: for $r=2$ it coincides with (2.18); for $r=3$ it gives $\beta_0=\frac{13}{12}(f_{i-2}-2f_{i-1}+f_i)^2+\frac14(f_{i-2}-4f_{i-1}+3f_i)^2$, $\beta_1=\frac{13}{12}(f_{i-1}-2f_i+f_{i+1})^2+\frac14(f_{i-1}-f_{i+1})^2$, $\beta_2=\frac{13}{12}(f_i-2f_{i+1}+f_{i+2})^2+\frac14(3f_i-4f_{i+1}+f_{i+2})^2$ (3.2)–(3.4), and $\beta_k=(f'\Delta x)^2(1+O(\Delta x^2))$ when $f'\ne0$ (3.8), so (2.17) holds and the scheme is fifth order (§3). **Derived**
8. At critical points ($f'=0$) the paper prints $\beta_k=\frac{13}{12}(f''\Delta x^2)^2(1+O(\Delta x^2))$, $k=0,1,2$ (3.9), "which implies that the weights resulting from the measurement (3.1) are also 5th order accurate at critical points" (§3, p. 9). **Derived** (see Printed slips)
9. On $f_i=\sin2\pi x_i$ for $x\le\frac12$ and $1-\sin2\pi x_i$ beyond, $\Delta x=\frac1{40}$, Liu et al.'s weights are "far less optimal" near the critical points $x=\frac14,\frac34$; near the jump both indicators give the discontinuous stencil almost zero weight, and just left of it $\omega_0\approx\frac17$, $\omega_1\approx\frac67$ (§3, (3.10), Fig. 1). **Shown**
10. Linear advection on $[-1,1]$, $t=1$, $u_0=\sin(\pi x)$: WENO-RF-5 reaches about fifth order from about 40 points ($L_\infty$ $1.35\times10^{-9}$, $L_1$ $6.79\times10^{-10}$ at $N=320$, orders 5.03 and 5.00); WENO-RF-4 (Liu et al.'s $r=3$) is more accurate at $N=10$ ($1.31\times10^{-2}$ against $2.98\times10^{-2}$) but reaches only orders 3.86 ($L_\infty$) and 4.65 ($L_1$) at $N=320$; the linear CENTRAL-5 gives $1.53\times10^{-10}$ and $9.73\times10^{-11}$; $\Delta t\sim\Delta x^{5/4}$ so that RK4 is effectively fifth order (Table 3). **Shown**
11. With $u_0=\sin^4(\pi x)$ the orders settle later: WENO-RF-5 5.48 ($L_\infty$) and 5.30 ($L_1$) at $N=640$ ($9.79\times10^{-8}$, $1.57\times10^{-8}$); WENO-RF-4 3.81 and 5.00 ($1.51\times10^{-6}$, $9.57\times10^{-8}$) (Table 4). **Shown**
12. For the Euler equations, pressure for the genuinely nonlinear fields and entropy for the linearly degenerate ones can replace the projected values in the weights, "at least for problems without strong shocks and reflective waves"; by linearity of the candidate fluxes this needs only two projections and two inverse projections (4.6) (§4). **Derived / Shown**
13. The pressure–entropy scheme WENO-LF-5-PS with Liu et al.'s indicators "does not perform well at shocks" (§4, p. 13). **Stated** (tests not shown)
14. With a smooth flux splitting (global Lax–Friedrichs) the WENO operator is infinitely differentiable (6.1); its first variation is $-\frac{f'(u_i)}{\Delta x}\big(D^{2r-2}+(-1)^{r-1}\tau_r\Delta_+^{2r-1}u_{i-r}\big)$ with $\tau_r=\frac{(r-1)!^2}{(2r-1)!}$ (6.3), whose spectrum lies in the left half plane (6.4) (§6). **Derived**
15. Theorem 6.1: for scalar laws with sufficiently smooth solution and flux, WENO with a smooth flux splitting and an $n$th-order Runge–Kutta method, $n\ge\max(r,3)$, converges with error $O(\Delta x^r)$ at a suitable CFL number (§6). **Proved** (via Strang's Theorem I; short argument)
16. Linear-stability CFL numbers: $r=2$: 1.625 (RK3), 1.745 (RK4); $r=3$: 1.434 (RK3), 1.731 (RK4) (Table 5). **Stated** (computed; method not shown)
17. Timings ($10^{4-d}$ iterations, RK4, CRAY C-90, 1D/2D/3D): ENO-LF-4 16.67/122.52/171.42 s, WENO-LF-4 7.44/63.93/76.79, WENO-LF-5 7.45/60.84/78.89, WENO-LF-5-PS 6.29/37.67/43.47, second order 1.75/13.13/15.48 (Table 6); the text says WENO-LF-4 and -5 are "at least twice as fast as ENO-LF-4" on the CRAY and WENO-LF-5-PS 2.5, 3.2 and 3.9 times as fast (§7). **Shown** (see Printed slips)
18. All WENO schemes run at about 500 MFlops on the CRAY C-90, "50% of the peak speed"; WENO-LF-5 557/503/442 MFlops in 1D/2D/3D against ENO-LF-4 223/219/190 (Table 7). **Shown**
19. The operation count per point and stage of characteristic fourth- and fifth-order ENO with Lax–Friedrichs building blocks is 3 to 4 times that of the second-order scheme, and about 1.5 times with the Roe building block (§7). **Shown**
20. Yang's artificial compression raises the operation count by 40% (1D) and 65% (2D) with the Roe building block and by 65% and 100% with Lax–Friedrichs (§7, Table 7). **Shown**
21. Composite-wave advection (200 points, $t=8$): WENO-Roe-4 and -5 beat ENO-Roe-4 on all four waves; WENO-Roe-4 is better at acute turns, WENO-Roe-5 for the square wave and obtuse turns, and WENO-Roe-5-A best everywhere (CFL 0.2; at CFL 0.4 a compression constant of 40 gives similar results) (§8.1 Ex. 1, Fig. 2). **Shown**
22. The shocks of WENO are in principle as sharp as those of the base ENO, but the tests show WENO-3 comparable to ENO-3 rather than ENO-2, and WENO-5 comparable to ENO-4 (Buckley–Leverett) (§8.1 Ex. 2, Fig. 3). **Shown**
23. The Sod and Lax problems "are tough test cases for non-characteristic based schemes of order at least three"; WENO-RF-5 is better than WENO-LF-5-PS, which is better than WENO-RF-3; WENO-LF-5-A is best at contacts (§8.2 Ex. 1, Fig. 4). **Shown**
24. 1D shock–entropy wave: at 800 points WENO-LF-4 is best and WENO-LF-5 second; at 1200 points WENO-LF-5 is as accurate as WENO-LF-4 and more accurate "on finer grids"; a second-order scheme on 2000 points is clearly worse (§8.2 Ex. 2, Figs. 5–6). **Shown**
25. Steady quasi-1D nozzle: WENO-Roe-4 and -5 converge with 34 points, residual to $10^{-7}$; "WENO has its advantage for steady state calculations", attributed to the smoothness of the WENO flux (§1; §8.2 Ex. 4, Fig. 8). **Shown**
26. WENO-LF-5-PS fails on the forward step and the double Mach reflection; at a reflective flat wall pressure and entropy are symmetric and cannot indicate jumps in the normal velocity, giving unstable weights and negative density (§8.3 Ex. 2–3, Remark p. 34). **Shown / Derived**
27. 2D shock–entropy wave: unmodified ENO-LF-4/-5 lose accuracy, WENO-LF-4/-5 "work nicely without any modification"; with the threshold modification (8.2) both perform better, and WENO-LF-4 "becomes 5th order accurate in smooth regions" (§8.3 Ex. 4, Fig. 14). **Shown / Stated**
28. Conclusions: with the new indicator, WENO from $r$-point ENO stencils is of order $2r-1$ in smooth regions "at least for $r=2,3$"; at discontinuities all WENO schemes are $r$th-order accurate; Liu et al.'s fourth-order scheme is slightly more accurate than WENO-5 on coarse grids (20 points or fewer per wavelength) and less accurate on finer ones (§9). **Stated**

Setting: global Lax–Friedrichs splitting $f^\pm=\frac12(f\pm au)$ with $a=\max\lvert f'(u)\rvert$
over the whole range (2.5), or Roe splitting with entropy fix (RF, details referred to ref. [15], Shu & Osher);
stencils $S_k=\{x_{i+k-r+1},\dots,x_{i+k}\}$, $S_0$ the most upwind; linear weights
$d=(\frac13,\frac23)$ for $r=2$ and $(\frac1{10},\frac6{10},\frac3{10})$ for $r=3$ (Table 2); candidate
coefficients in Table 1. Names WENO-X-Y: splitting X (LF, Roe, RF), order Y "in $L^1$ sense";
"-PS" pressure–entropy weights, "-A" artificial compression, "WENO2" threshold-modified weights
($\omega_k=d_k$ if some $\beta_l<\frac12$, (8.2)). The name "WENO-JS" is not used. Artificial
compression (5.1)–(5.4) follows Yang in point-value form with a minmod-limited correction and
constant 33, applied to the contact fields only. Time stepping: TVD RK3 (1.3) and the classical
non-TVD RK4 (1.4), which "can be made TVD by an increase of operation counts".

# Printed slips

- **(3.5)–(3.7)** (p. 9): the printed expansions
  $\beta_{0,2}=\frac{13}{12}(f''\Delta x^2)^2+\frac14(2f'\Delta x-\frac23f'''\Delta x^3)^2+O(\Delta x^6)$ and
  $\beta_1=\frac{13}{12}(f''\Delta x^2)^2+\frac14(2f'\Delta x+\frac13f'''\Delta x^3)^2+O(\Delta x^6)$ carry no
  $\Delta x^5$ term. [Borges et al. (2008)](/sources/borges-2008.md) (Eqs. (12)–(14)) print the same
  indicators with the term $\mp(\frac{13}6f''f'''-\frac12f'f^{(4)})\Delta x^5$ in $\beta_{0,2}$ and none in
  $\beta_1$. *(Compiler check, not in the sources: a symbolic Taylor expansion of (3.2)–(3.4) about $x_i$
  reproduces Borges et al.'s coefficients; at $f'=0$ it gives
  $\beta_{0,2}=\frac{13}{12}f''^2\Delta x^4\big(1\mp2\frac{f'''}{f''}\Delta x+O(\Delta x^2)\big)$, a relative
  $O(\Delta x)$ term against the $O(\Delta x^2)$ of (3.9), so that this expansion does not meet the
  sufficient condition (2.14) for $r=3$; $\epsilon$ ignored.)* (3.8), for $f'\ne0$, is unaffected. The
  disagreement on the order at critical points is recorded on
  [critical-point accuracy](/properties/critical-point-accuracy.md).
- (2.26), p. 7: "for a smooth stencil $S_k$, $IS_k=O(h^{2p})$", while (2.21) and (3.8) give
  $O(h^2)$, from which (2.28) $\omega_l=O(h^{2p})$ follows.
- Below (2.18), p. 6: "$f[j,l]=f[j+1,l-1]-f[j,l-1]$, $k=1,\dots,r-1$" (range variable $k$ for $l$).
- §4, p. 13: the smooth Euler test is said to be "the same example used in Section 6"; it is in
  Section 7, (7.1)–(7.4). §8.2 Ex. 2, p. 23: "our accuracy test in section 4"; the accuracy tests are
  in Section 3.
- §8.3 Ex. 5, p. 35: "A stationary Mach 1.1 shock … Its left state is
  $(\rho,u,v,P)=(1,\sqrt\gamma,0,1)$". *(Compiler check, not in the sources: with $\rho=p=1$,
  $c=\sqrt{\gamma p/\rho}=\sqrt\gamma$, so this state has Mach number 1.)* Recorded as printed.
- §7, p. 16 against Table 6 *(compiler check, not in the sources: ratios of the printed times)*:
  "at least twice as fast as ENO-LF-4 on the CRAY C-90", but 2D WENO-LF-4 gives
  $122.52/63.93=1.92$; "WENO-LF-5-PS is 1.5 to 2.2 times as fast as ENO-LF-4 on the SUN Sparc10
  and on the SGI Indigo2", but SGI 1D gives $66.21/58.14=1.14$ and Sparc 1D
  $311.22/215.95=1.44$; WENO-LF-4 and -5 "a bit faster than ENO-LF-4 on the SUN Sparc10", but the
  1D times 317.55 and 319.02 exceed 311.22. Table 6 uses $N=40$ in 3D on the Sparc10 and $N=60$
  on the other machines.
- References [11] (Roe) and [17] (Sod) are both printed "J. Comput. Phys., v27, 1978, pp. 1-31".
- The Sod and Lax data use $q$ for the velocity (p. 19), $u$ elsewhere.

# Notation map

| Jiang & Shu | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $j$, $h=\Delta x$ | $i$, $\Delta x$ | **collision**: $h$ is also the implicit function |
| $h(x)$, $h_{j+1/2}$ | $\phi$ (local) | implicit function whose cell averages are $f$; **collision** with the two-point flux $h$ |
| $q^r_k$, $a^r_{k,l}$ | $\hat f^{(k)}_{i+1/2}$, candidate coefficients | Table 1 |
| $q^{2r-1}_{r-1}$ | linear $(2r-1)$th-order flux | "upstream central scheme"; CENTRAL-5 in Tables 3–4 |
| $C^r_k$ | $d_k$ | "optimal weights" |
| $IS_k$ | $\beta_k$ | |
| $p$ | $q$ | $q=2$ |
| $\epsilon$ | $\epsilon$ | $10^{-6}$; also an entropy-wave amplitude and the vortex strength $\mathcal E$ |
| $\alpha$ | $a$ (splitting), $\alpha_k$ (weights) | also Yang's constant, the threshold of (8.2) and a vortex decay rate |
| $\mathbf l_s$, $\mathbf r_s$, $A_{j+1/2}$ | rows of $L$, columns of $R$, $A$ at $x_{i+1/2}$ | Roe or arithmetic average |
| $r$ | $r$ | WENO order $2r-1$ |
| $u$, $q$, $P$, $S=\ln(P/\rho^\gamma)$ | $v$, $v$, $p$, $s$ | |
| $\tau_r$, $D^{2r-2}$, $\Delta_+^{2r-1}$ | local | first-variation analysis (§6) |

# Reference list

The paper prints 21 references, numbered [1]–[21] in alphabetical order. The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` including `jiang-1996`. [5],
[9] and [14] are [Harten et al. (1987a)](/sources/harten-1987.md),
[Liu et al. (1994)](/sources/liu-1994.md) and [Shu & Osher (1988)](/sources/shu-1988.md). [8]
(Liu & Lax, "Positive schemes …") is printed as a preprint "submitted to CFD Review" with no
year and is kept as a preprint entry. [6] is Jiang's PhD thesis (Brown, 1995). [11] and [17] are
printed with identical volume and pages and are recorded as printed; [12] prints the second author
"Meiberg". No item is unparseable.

# Pages created or updated

Chunk 12 (2026-10-30). This source is cited on:

* [Accuracy at critical points](/properties/critical-point-accuracy.md)
* [Artificial compression](/methods/artificial-compression.md)
* [Buckley–Leverett problem](/benchmarks/buckley-leverett-problem.md)
* [Characteristic decomposition](/methods/characteristic-decomposition.md)
* [Conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
* [Double Mach reflection](/benchmarks/double-mach-reflection.md)
* [ENO property](/definitions/eno-property.md)
* [ENO reconstruction (essentially non-oscillatory schemes)](/methods/eno-reconstruction.md)
* [Flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
* [Flux vector splitting](/methods/flux-vector-splitting.md)
* [Jiang–Shu composite-wave advection](/benchmarks/jiang-shu-composite-advection.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [Mach 3 forward-facing step](/benchmarks/forward-facing-step.md)
* [Monotone schemes and monotone numerical fluxes](/definitions/monotone-scheme.md)
* [Roe approximate Riemann solver](/methods/roe-riemann-solver.md)
* [Shock–vortex interaction](/benchmarks/shock-vortex-interaction.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Steady shock problems](/benchmarks/steady-shock-problems.md)
* [WENO-JS reconstruction](/methods/weno-js-reconstruction.md)
* [Woodward–Colella interacting blast waves](/benchmarks/woodward-colella-blast-wave.md)
