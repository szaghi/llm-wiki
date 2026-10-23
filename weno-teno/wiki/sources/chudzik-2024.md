---
type: Source
title: "Chudzik et al. (2024) — Active Flux Methods for Hyperbolic Systems Using the Method of Bicharacteristics"
description: "Third-order Cartesian Active Flux methods whose point values are updated by bicharacteristic (evolution-Galerkin) operators: Maxwell via two acoustic systems, EG2 acoustics with a proved order and eigenvalue stability limits, the first unsplit linearised-Euler Active Flux, and a nonlinear Euler extension with iterated local linearisation."
resource: "doi:10.1007/s10915-024-02462-z"
source_kind: paper
authors: [Chudzik E., Helzel C., Lukáčová-Medvid’ová M.]
year: 2024
venue: "J. Sci. Comput. 99:16"
local_file: "/home/stefano/papers/mosaic/weno-teno/2024_Crossref_Journal_of_Scientific_Computing_Chudzik_Active_Flux_Methods_for_Hyperbolic_Systems_Using_the_Method.pdf"
tags: [active-flux, finite-volume, euler-equations, compressible-flow]
timestamp: 2026-10-23T23:55:00Z
---

# Summary

The paper builds third-order, fully discrete [Active Flux](/methods/active-flux.md)
methods on two-dimensional Cartesian grids in which the point values on the
cell boundary (corners and edge midpoints) are evolved by approximate
multidimensional evolution operators derived with the method of
bicharacteristics, the evolution-Galerkin (EG) operators of
Lukáčová-Medvid’ová, Morton and Warnecke, instead of the exact evolution
formulas that exist only for acoustics. Cell averages are updated by finite
volumes with Simpson-rule fluxes in space and time; point values and averages
define a globally continuous biquadratic reconstruction.

Four steps. (i) The source-free 2D Maxwell equations decouple, after a
scaling, into two acoustic systems, so an Active Flux method with the exact
acoustic operator is obtained, with a claimed third order and exact discrete
divergence constraints (Theorem 3.1); the paper's own convergence table shows
lower orders in some components. (ii) The third-order EG2 operator for
acoustics, which integrates only over the base circle of the bicharacteristic
cone, gives a provably third-order method (Theorem 4.1); eigenvalue
computations of the one-step matrix give stability for $\nu\le0.279$ (EG2) and
$\nu\le0.154$ (EG4), instability of EG1 and EG3, and $\nu\le0.5$ for the exact
operators. On a new non-irrotational test EG2 is third order in all
components, while the Eymann–Roe operator is second order in velocity and the
exact operator shows a time-dependent velocity order loss. (iii) The EG2
operator of the linearised Euler equations gives what the authors call the
first unsplit Active Flux method for that system, third order on
[density-wave advection](/benchmarks/density-wave-advection.md) and a smooth
two-pulse problem. (iv) For the nonlinear Euler equations, conservative cell
averages are updated by finite volumes and primitive point values by EG2 with
a local linearisation iterated at each point; the order is close to three on a
smooth travelling vortex. The [Gresho vortex](/benchmarks/gresho-vortex.md) and
a [2D Riemann problem](/benchmarks/two-dimensional-riemann-problems.md) are run
without limiters. The implementation lives in
[ForestClaw](/software/forestclaw.md), which allows adaptive refinement.

# Version read

Version of record (Springer typeset, open access CC BY 4.0, J. Sci. Comput.
(2024) 99:16), 39 pages, all read, appendix A on pp. 36–38. Page 1 matches
Crossref (title, three authors, venue, DOI). Equation, table and example
numbers cited here are those of this version.

# Key claims

Registry notation (see the notation map): the source's CFL number is $\nu$,
its acoustic velocity $\mathbf u=(u,v)$ is $v=(v_1,v_2)$, its cell average
$Q^n_i$ is $\bar u^n_i$, its frozen linearisation state carries primes as in the
source.

1. Active Flux on Cartesian grids is third order, fully discrete and compact in space and time; point values on the cell boundary and the cell average define a globally continuous piecewise-quadratic reconstruction (§1, §2, Fig. 2). **Stated**
2. For acoustics with the exact operator in the form of Barsukow et al. (Eq. (7)), $\max(c\Delta t/\Delta x,c\Delta t/\Delta y)\le1/2$ keeps the integration disc inside the two adjacent cells, and the authors' earlier paper showed this necessary condition to be sufficient for linear stability (§2.1, Fig. 3). **Stated** (own earlier result)
3. On regular Cartesian grids the Active Flux method with the exact acoustic operator preserves all steady states (stationarity preservation, after Barsukow et al.) (§2.1, §5.3). **Stated**
4. Theorem 3.1: the source-free 2D Maxwell equations decouple into two acoustic systems (Eqs. (12)–(14)); with the exact acoustic solver (7) the Active Flux method is third order and satisfies $\nabla\cdot\mathbf E=0$, $\nabla\cdot B=0$. **Proved** (short proof: order inherited from acoustics; the constraints reduce to preservation of the curl of the acoustic velocity, argued from stationarity preservation; the discrete divergence operator is not specified)
5. Maxwell convergence (Example 3.2, Table 1, $\nu=0.457$, $t=0.1$, $64^2$–$256^2$): $L^1$ orders at $256^2$ are 2.3797 ($E_x$, $E_y$), 2.9862 ($E_z$), 2.7694 ($H_x$, $H_y$), 2.9927 ($H_z$), with the $E_x$, $E_y$ and $H_x$, $H_y$ orders decreasing under refinement (2.5720 → 2.3797, 2.8878 → 2.7694) (§3.1). **Shown** (the authors do not comment on these orders; Theorem 3.1 states third order)
6. The bicharacteristic representation (Eq. (20)) writes the solution at the cone apex as an average over all directions of the characteristic variables at the footpoints plus a mantle integral of the quasi-diagonal source (§4, Eqs. (17)–(20)). **Derived** (background)
7. The trapezoidal rule in time and Butler's trapezoidal integration of the pressure equation along the cone axis turn the exact acoustic representation (21) into the explicit third-order formula (26)–(27); Lemma 4.1, the divergence theorem and the midpoint rule cancel the mantle terms to third order and give the EG2 operator (28), which integrates over the base circle only (§4.1). **Derived**
8. Theorem 4.1: an Active Flux method for 2D acoustics with point values updated by (28) is third order in space and time for sufficiently smooth initial data (§4.1). **Proved** (local $O(\Delta t^3)$ of (28), exact evaluation on the reconstruction, third-order Simpson nodes)
9. The second-order EG1 and EG3 operators give unstable Active Flux methods; the second-order EG4 operator is stable for $\nu\le0.154$ and second order (Remark 4.2, §5.1). **Shown**
10. In a piecewise-constant finite-volume setting EG3 outperformed all other methods, including the third-order EG2 (Remark 4.2, citing earlier work). **Stated**
11. Linear stability (Table 2, $16\times16$ periodic grid): the spectral radius of the one-step matrix is $1.000000000000$ for EG2 up to $\nu=0.279$ and $1.002909442688$ at $\nu=0.28$; for EG4 it is $1.000000000000$ up to $0.154$ and $1.000007260910$ at $0.155$; EG1 and EG3 exceed 1 already at $\nu=0.01$ (§5.1). **Shown**
12. $\lVert A^n\rVert$ of the one-step matrix stays bounded for $n=1,\dots,100$ at $\nu=0.279$ for the irrotational-exact, general-exact and EG2 methods, indicating equal algebraic and geometric multiplicities of the unit-modulus eigenvalues (§5.1, Figs. 5–6). **Shown**
13. The Active Flux methods with the Eymann–Roe operator (4) and the exact operator (7) are stable for $\nu\le0.5$ (§5.1). **Shown** (for (7) first shown in the authors' earlier work)
14. Among the bicharacteristic EG operators, EG2 is "the best candidate" for Active Flux (§5.1). **Shown**
15. Example 5.1 (non-irrotational acoustics, $t=0.1$, $L^1$): EG2 at $\nu=0.267$ gives orders 2.9189 ($p$), 2.9685 ($v_1$), 2.9667 ($v_2$) at 256 (Table 3); Eymann–Roe at $\nu=0.457$ gives 2.9859 ($p$) and 2.0000 ($v_1$, $v_2$); the exact operator gives 2.9871 ($p$) and 2.4377 ($v_1$, $v_2$) (Table 4). **Shown**
16. With the exact operator the velocity order on Example 5.1 is time dependent: between 64 and 128 cells it ranges from 1.9997 ($t=0.4$) to 2.9969 ($t=0.9$), while the pressure order stays near 3 (Table 5); Samani and Roe reported a similar effect (§5.2). **Shown**
17. Stationary vortex (Example 5.2, $t=100$, $128^2$): EG2 does not preserve the steady state exactly but is more accurate than Eymann–Roe; the exact operator preserves the discrete steady state (§5.3, Figs. 8–10). **Shown** (qualitative)
18. Discontinuous acoustic data (Example 5.3, $256^2$, no limiting): discontinuities are "much sharper" than with the first- and second-order EG finite-volume methods; the exact operator is slightly sharper than EG2 (§5.4, Figs. 11–12). **Shown** (qualitative)
19. The EG2 operator of the linearised Euler equations (Eq. (33), from earlier work) gives the first unsplit Active Flux method for that system (§6, Conclusions). **Derived** (operator) / **Stated** (priority)
20. In all linearised-Euler tests the stability limit is the acoustic one, $\nu\le0.279$ with $\nu=\max(\lvert v_1'\rvert+c',\lvert v_2'\rvert+c')\Delta t/\Delta x$ (§6). **Shown** (empirical, no analysis)
21. An exact evolution operator for linearised Euler would need derivatives of the reconstruction across cell interfaces; EG2 needs only integrals along circle segments, evaluated exactly on the reconstruction (Remark 6.1, §6). **Stated**
22. Linearised-Euler density advection (Example 6.2, $\nu=0.275$, $32^2$–$256^2$): $L^1$ order 2.9884 ($v_1'=v_2'=0.5$) and 2.9908 ($v_1'=v_2'=1$) at 256; $p$, $v_1$, $v_2$ constant to machine precision (Table 6). **Shown**
23. Smooth two-pulse linearised-Euler problem (Example 6.3, $t=0.166$, reference $1024^2$, $\nu=0.275$): orders 2.97–2.98 at 256 in all four variables (Table 7). **Shown**
24. Nonlinear Euler: conservative cell averages by finite volumes with the 9-point Simpson flux (38); primitive point values $(\rho,v_1,v_2,p)$ by the EG2 operator (33) linearised locally at each point value and iterated $L+1$ times (Algorithm 1); primitive cell averages recovered to third order from the conservative reconstruction at the cell centre plus Simpson's rule (§7). **Derived** (construction)
25. The method uses the linear characteristic cone and ignores the curvature of characteristics, which Barsukow showed must be accounted for to reach third order for 1D nonlinear systems, so full third order is not expected (§7, Example 7.3). **Stated**
26. Nonlinear density advection (Example 7.1, $L=0$): orders 2.9874 and 2.9880 at 256 (Table 8). **Shown**
27. Smooth travelling vortex (Example 7.3, $t=1$, $\nu\le0.275$, error against the next finer mesh): with $L=0$ the order drops to 2.4349 at 512; with $L=1$ the orders are 2.6454, 2.8899, 2.9320, 2.8234 (Table 9); the iteration improves accuracy, "as previously observed for scalar problems" (§7). **Shown**
28. Gresho vortex at $t=3$ on $64^2$, $\nu\le0.275$: the density (initially 1) stays between 0.999275 and 1.001377, and the circular geometry of $p$ and $\lvert v\rvert$ is well preserved (Example 7.2, Figs. 20–21). **Shown**
29. The pressure polynomial of the Kadioglu–Klein–Minion vortex in its original paper has a wrong coefficient: $-\tfrac{269}{15}r^{30}$, not $-\tfrac{259}{15}r^{30}$ (Example 7.3). **Stated** *(compiler check, not in the sources: with $\mathrm dp/\mathrm dr=\rho v_\theta^2/r$, $v_\theta=1024(1-r)^6r^6$ and $\rho=\rho_c+\tfrac12(1-r^2)^6$, the $\rho_c$ part has degree 24, and the coefficient of $r^{30}$ of $\int\tfrac12(1-r^2)^6(1-r)^{12}r^{11}\,\mathrm dr$, the factor $1024^2$ taken out, is exactly $-\tfrac{269}{15}$, in a polynomial of degree 36; this agrees with the correction if the original normalization takes out $1024^2$, which the compiler has not seen.)*
30. All simulations are run without limiters (§5.4, end of §7). **Stated**

# Printed slips

- Example 6.2: "$\rho'=1$, $u'=v'=0.5$ and $c'=1$ as well as $\rho'=1$,
  $u'=v'=1$ and $c'=1$. These two cases correspond to supersonic flow and
  subsonic flow." *(Compiler check, not in the sources: $\lvert v'\rvert=0.5\sqrt2\approx0.71<c'$
  is subsonic and $\sqrt2\approx1.41>c'$ supersonic, so the printed order is reversed.)*
- §7: the vector printed as the flux $f(U^{n+1/2}_{i+1/2,j})$ has components
  $\rho$, $\rho u$, $\rho v$, $\frac1{\gamma-1}p+\frac12\rho(u^2+v^2)$, the
  conservative state, not the $x$-flux of Eq. (36).
- Example 7.3: the initial data are printed as $\rho(x,y,t)$, "$u(x,y,z)$",
  $v(x,y,t)$, $p(x,y,t)$ for values at $t=0$; the radius is typeset as
  $r=\sqrt{(x-0.5)^2+(y-0.5)^2/R}$ while the text calls it the distance scaled
  by the radius $R$, i.e. $\sqrt{(x-0.5)^2+(y-0.5)^2}/R$.
- Fig. 18 caption: "at times $t = 0.25, 5, 0.75, 1$"; "5" breaks the sequence.
- §2.1, §5.1: "constant vorticity (i.e. irrotational flow)". *(Compiler check,
  not in the sources: constant and zero vorticity are different conditions.)*
- Eq. (27), second line: "$v(Q_1(\theta)\sin^2(\theta)$" lacks a closing
  parenthesis.
- Ref. [19] prints "Lukáčová-Medvid’ová, T." where refs. [21]–[25] print
  "M."; ref. [15] prints the first author "Feyman, R.P." for "The Feynman
  Lectures".
- Typos: "Maxell's equations" (proof of Theorem 3.1), "convergency study"
  (§3.1), "combuted" (Fig. 18), "visable" (§7), "computed on a grids"
  (Example 6.5).

# Notation map

| Chudzik et al. (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $q$, $f(q)$, $g(q)$ | $u$, $f$, $g$ | conserved variables and fluxes |
| $Q^n_i$, $Q^n_{ij}$ | $\bar u^n_i$, $\bar u^n_{ij}$ | cell averages; in §7 conservative |
| $Q^n_{i\pm1/2}$, $Q^{n+1/2}_{i\pm1/2}$, $Q^{n+1}_{i\pm1/2}$ | kept | Active Flux point values, one shared value per interface (no $u^\pm$ states) |
| $U=(\rho,u,v,p)$ | $(\rho,v_1,v_2,p)$ | primitive point values; also the linearised-Euler state of Eq. (31) |
| $q^{rec}$ | kept | continuous (bi)quadratic Active Flux reconstruction |
| $F_{i\pm1/2}$, $F_{i+\frac12,j}$, $G_{i,j+\frac12}$ | $\hat f_{i+1/2}$, $\hat g_{i,j+1/2}$ | Simpson-rule numerical fluxes, weights $1/6$ (1D), $1/36$ (2D) |
| $p$, $\mathbf u=(u,v)$, $c$ | $p$, $v=(v_1,v_2)$, $c$ | acoustic pressure, velocity, sound speed |
| $\rho'$, $u'$, $v'$, $p'$, $c'$ | kept | frozen linearisation state (primes are not perturbations) |
| $\mathbf w$ | kept | **vorticity in §2.1, characteristic variables in §4; $w$ is the entropy-variable vector in the registry** |
| $M_R\{\cdot\}$, $\langle\cdot\rangle_R$ | kept | weighted disc mean ("spherical mean") and disc average, $R=ct$ |
| $A_k$, $A(\mathbf n)$, $R(\mathbf n)$ | $A^{(k)}$, —, $R$ | Jacobians, directional Jacobian, right eigenvectors |
| $B_k=\Lambda_k+B'_k$, $\lambda^k_\ell$ | kept | quasi-diagonalized Jacobians and bicharacteristic speeds; **$B$ collides with the magnetic field** |
| $\mathbf S$, $S(\tilde t,\theta)$ | kept | quasi-diagonal source and mantle integrand; **$S$ is the balance-law source in the registry** |
| $P$, $P'$, $Q_1(\theta)$, $Q_2$, $Q(\theta)$ | kept | cone apex, base centre, base-circle and axis points; **points, not cell averages; $Q$ is also the SBP stiffness matrix** |
| CFL | $\nu$ | $c\Delta t/\Delta x$ (acoustics) or $\max(\lvert v_1'\rvert+c',\lvert v_2'\rvert+c')\Delta t/\Delta x$ |
| $A$ (§5.1) | kept | one-step update matrix on $12m^2$ unknowns; **not the flux Jacobian** |
| $L$, $\ell$ | kept | number of linearisation iterations minus one, iteration index; **$L$ is the left-eigenvector matrix in the registry** |
| $\mathbf E$, $\mathbf H$, $\mathbf D$, $\mathbf B$ | $\mathbf E$, $\mathbf H$, $\mathbf D$, $B$ | Maxwell fields; **$\mathbf E$ collides with the total energy $E$** |
| $\epsilon$, $\mu$ | kept | permittivity and permeability; **$\epsilon$ collides with the weight regularization, $\mu$ with the affine translation** |
| $\phi,u,v$; $\tilde\phi,\tilde u,\tilde v$ | kept | scaled Maxwell fields as acoustic variables (Eq. (12)); **$\phi$ is the gravitational potential on well-balancing pages** |
| EOC | kept | experimental order of convergence, $L^1$ norm |
| $\gamma$ | $\gamma$ | ratio of specific heats, 1.4 ("isotropic exponent") |

# Reference list

33 printed references, numbered style in alphabetical order ([1]–[33]), all
parsed and merged complete into the [bibliography](/bibliography.md) with
`citedby` `chudzik-2024`. Ref. [2] (Abgrall & Barsukow 2023) is the ingested
Abgrall and Barsukow Active Flux paper, and ref. [7] is the ingested Calhoun &
Burstedde ForestClaw paper; refs. [10] and [11] print no year (taken from the
AIAA paper numbers 2011-382 and 2011-3840); ref. [15] prints "Feyman"; ref.
[19] prints the initial "T." for Lukáčová-Medvid’ová. No printed duplicates and
no unparseable items.

# Pages created or updated

Chunk 8 (2026-10-23). This source is cited on:

* [Active Flux](/methods/active-flux.md)
* [Density-wave advection](/benchmarks/density-wave-advection.md)
* [ForestClaw](/software/forestclaw.md)
* [Gresho vortex](/benchmarks/gresho-vortex.md)
* [Two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md)
