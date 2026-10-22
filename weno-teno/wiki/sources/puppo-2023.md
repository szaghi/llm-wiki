---
type: Source
title: "Puppo et al. (2023) — Quinpi: Integrating Conservation Laws with CWENO Implicit Methods"
description: "Third-order implicit finite-volume framework (Quinpi) for 1D scalar conservation laws: CWENO3 weights frozen from a first-order implicit predictor make the reconstruction linear, a DIRK3 corrector, CWENO-type blending in time with the predictor, and a conservative flux correction; third order on Burgers at time steps of one and ten cell widths."
resource: "doi:10.1007/s42967-021-00171-0"
source_kind: paper
authors: [Puppo G., Semplice M., Visconti G.]
year: 2023
venue: "Commun. Appl. Math. Comput. 5:343-369"
local_file: "/home/stefano/papers/mosaic/weno-teno/2022_Crossref_Communications_on_Applied_Mathematics_and_Computation_Puppo_Quinpi_Integrating_Conservation_Laws_with_CWENO_Implicit_Met.pdf"
tags: [cweno, finite-volume, limiting, tvd, implicit-time-stepping]
timestamp: 2026-10-22T12:00:00Z
---

# Summary

The paper proposes [Quinpi](/methods/quinpi.md) ("CWENO implicit"), a framework
for high-order *implicit* finite-volume integration of hyperbolic conservation
laws. It targets stiff problems, where the explicit CFL limit set by the fastest
waves is too restrictive. Following Arbogast et al., a high-order implicit scheme
has three sources of nonlinearity: the flux, the nonlinear weights of the space
reconstruction, and the limiting in time that a high-order Runge–Kutta step
needs. Quinpi removes the second and controls the third.

Section 2 revisits [TVD](/definitions/total-variation-diminishing.md) bounds. The
implicit upwind scheme is TVD for every time step, and the implicit Euler step
with a limited piecewise-linear reconstruction is TVD for every $\Delta t/\Delta x$
under the same limiter conditions as the explicit step. The limiter can be
computed from any first-order approximation of $u(x,t^{n+1})$.

The third-order scheme Q3P1 has three parts. (i) A first-order predictor: a
composite backward Euler with piecewise-constant data, one substep per DIRK
abscissa. (ii) A corrector D3P1: Alexander's three-stage, third-order L-stable
DIRK with third-order [CWENO](/methods/cweno.md) reconstruction. Its Jiang–Shu
[smoothness indicators](/definitions/smoothness-indicator.md) are evaluated on
the predictor, so the interface values are linear in the unknowns and the stage
systems are nonlinear only through the flux. (iii) A CWENO-type blending in time
of the D3P1 and predictor solutions, driven by a space-time smoothness
indicator. The blend is not conservative, so a correction redistributes the mass
defect at each interface. This restores a flux form
([local conservation](/results/local-conservation-flux-form.md)), and without it
the shock lands in the wrong place, as the
[Lax–Wendroff theorem](/results/lax-wendroff-theorem.md) predicts. The global
[Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md) is used throughout.

The tests are 1D and scalar only. On the
[Burgers equation](/benchmarks/burgers-equation-tests.md) the scheme converges at
third order up to $\Delta t=50\Delta x$. Further tests are linear transport of
discontinuous data, shock formation and interaction, and the
[Buckley–Leverett problem](/benchmarks/buckley-leverett-problem.md). The cost per
step is 2.5–6 times that of explicit [SSP-RK3](/methods/ssp-runge-kutta.md). The
authors call the work preliminary: systems, multi-D problems and higher orders
are left open.

# Version read

arXiv:2102.00741v2 [math.NA], stamped 28 Dec 2021, with the title block dated
"December 30, 2021": an author version, not the CAMC version of record. It has 29
pages, all read; pp. 5–6, 8–10, 12–16 and 25 were checked visually. Page 1 prints
the title in sentence case ("integrating conservation laws with CWENO implicit
methods") and the authors in the Crossref order. The archive filename says 2022;
the issue year is 2023. Section, equation, table and figure numbers are those of
the arXiv v2.

# Key claims

Registry notation: the source's $h$, cell index $j$, $\mathcal F$ and $\lambda$
become $\Delta x$, $i$, $\hat f$ and $\Delta t/\Delta x$; DIRK coefficients are
$\mathsf a_{kl},\mathsf b_k,\mathsf c_k$ and the time-blending weights carry the
superscripts $\mathrm L$ (low order) and $\mathrm H$ (high order) (see the
Notation map).

1. The implicit upwind scheme $u_i^n=u_i^{n+1}+\frac{a\Delta t}{\Delta x}(u_i^{n+1}-u_{i-1}^{n+1})$, $a>0$, satisfies $TV(u^{n+1})\le TV(u^n)$ for every $\Delta t/\Delta x$ with periodic boundaries (§2, p. 5). **Derived**
2. For the explicit Euler step with limited piecewise-linear reconstruction, Harten's incremental form gives TVD iff $\mathsf C_i\ge0$ and $1-\mathsf C_i\ge0$. This recovers the Sweby region $0\le\psi(r)/r\le2$, $0\le\psi(r)\le2$, plus a CFL condition for the second inequality (§2, p. 5). **Derived** (background)
3. For the implicit Euler step with the same reconstruction, TVD holds if $\mathsf C_i\ge0$ and $1+\mathsf C_i\ge0$. The first condition gives the explicit limiter restrictions and the second always holds, so the scheme is TVD for every $\Delta t/\Delta x$ (§2, p. 6). **Derived**
4. Second-order accuracy needs $\psi(1)=1$ and a Lipschitz $\psi$. Hence $\psi$ and $r_i$ can be computed from an auxiliary function that is at least a first-order approximation of $u(x,t^{n+1})$ (§2, p. 6). **Derived**
5. When the smoothness indicators are evaluated on a predictor that is at least first-order accurate, the CWENO interface values are linear functions of the cell averages, with grid-dependent coefficients: $u^{-,(k)}_{i+1/2}=\sum_{l=-1}^1W^-_{i,l}\bar u^{(k)}_{i+l}$ (§3.1, p. 9; (21)). **Stated** (by construction)
6. Hence Quinpi is linear in the space reconstruction. For a linear conservation law a time step costs $s$ narrow-banded linear systems; for a nonlinear flux the stage systems are nonlinear only through $f$ (§3.3, p. 11; §3.3.2, p. 13). **Stated** (by construction)
7. The composite backward-Euler predictor over the ordered DIRK abscissae equals a DIRK with tableau (19), $\mathsf a_{kl}=\mathsf b_l=\tilde{\mathsf c}_l-\tilde{\mathsf c}_{l-1}$ for $l\le k$. It gives a first-order, stable, non-oscillatory $u^{\mathrm{IE},n+1}$ and first-order stage values $u^{\mathrm{IE},(k)}$ (§3.3.1, p. 12). **Stated**
8. An implicit predictor costs more than the explicit predictor of Gottlieb, Mullen and Ruuth, but it is stable, gives reliable weights at high Courant numbers, and serves as the low-order solution of the time limiting (§3.3, pp. 11–12). **Stated**; Fig. 8 shows that an explicit first-order predictor gives oscillations at $\Delta t=5\Delta x$. **Shown**
9. D3P1 (DIRK3 plus CWENO3 with predictor weights, no limiting in time) is third order on smooth data but can still oscillate (§3.3.3, p. 13; Figs. 1–3). **Shown**
10. The blending (23), $u_i^{\mathrm B,n+1}=\frac{\omega^{\mathrm H}_i}{d^t_{\mathrm H}}\big(u_i^{\mathrm{D3P1},n+1}-d^t_{\mathrm L}u_i^{\mathrm{IE},n+1}\big)+\omega^{\mathrm L}_iu_i^{\mathrm{IE},n+1}$, returns $u^{\mathrm{D3P1}}$ when $\omega^{\mathrm H}_i=d^t_{\mathrm H}$ and $u^{\mathrm{IE}}$ when $\omega^{\mathrm L}_i=1$ (§3.3.3, p. 14). **Derived**
11. A third-order time-limited solution, blending a first- and a third-order solution, needs $d^t_{\mathrm L}=\Delta t^2$ (citing Semplice and Visconti). The Burgers convergence tests use $d^t_{\mathrm L}=\Delta t^2$, $d^t_{\mathrm H}=1-\Delta t^2$ (§3.3.3, p. 15; §4.1, p. 17). **Stated**
12. The cell-wise blending is not conservative. The interface mass defect (31) is redistributed in proportion to the high-order weights (32), and the resulting Q3P1 scheme is conservative with an explicit interface flux $\hat f^{\mathrm{Q3P1}}_{i+1/2}$ (§3.3.4, pp. 15–16). **Derived**
13. In $\hat f^{\mathrm{Q3P1}}_{i+1/2}$ the high-order flux is weighted by the harmonic mean $\tilde\omega^{\mathrm H}_{i+1/2}=2\omega^{\mathrm H}_i\omega^{\mathrm H}_{i+1}/(\omega^{\mathrm H}_i+\omega^{\mathrm H}_{i+1})$, so it contributes much only when both neighbouring cells are detected smooth; $d^t_{\mathrm L}$ must be infinitesimal (§3.3.4, p. 16). **Derived**
14. On Burgers with $u_0=0.5-0.25\sin\pi x$ at $t=1$, Q3P1 converges at third order in $L^1$ and $L^\infty$. Finest-grid rates are 2.99/2.98 for $\Delta t=\Delta x$ ($N_x=2560$, $L^1$ error $3.66\times10^{-7}$), 2.99/2.98 for $\Delta t=10\Delta x$ ($N_x=5120$, $1.29\times10^{-7}$) and 2.79/2.52 for $\Delta t=50\Delta x$ ($N_x=5120$, $1.41\times10^{-5}$) (§4.1, Table 1). **Shown**
15. At large CFL numbers Q3P1 "reaches smaller errors and faster convergence" than Arbogast et al. (2020) on the same grid (§4.1, p. 17). **Stated** (the numbers of the earlier paper are not reproduced)
16. On the same problem the predictor alone (IE) is first order and D3P1 is third order for $\Delta t=\Delta x,10\Delta x,50\Delta x$ (§4.1, Fig. 1). **Shown**
17. Linear transport of discontinuous data (400 cells, $\Delta t=3\Delta x,5\Delta x$, one period): IE is very diffusive, D3P1 oscillates at the discontinuities, and Q3P1 is much less diffusive than IE and shows no spurious oscillations "even with large CFL number" (§4.2, Fig. 2). **Shown**
18. On the top-hat datum at $\Delta t=5\Delta x$, Q3P1 oscillates less than D3P1 but some oscillation remains; on finer grids "the frequency of the oscillations increases, whereas the amplitude slightly decreases" (§4.2, Fig. 3). **Shown**
19. Burgers shock formation (256 cells, $t=2$): Q3P1 is slightly more diffusive than D3P1 and much less than IE. At $\Delta t=5\Delta x$ it reduces the D3P1 oscillations. DIRK3 with linear CWENO weights and no blending shows very large oscillations even at moderate CFL numbers (§4.3.1, Figs. 4–5). **Shown**
20. Without the conservative correction Q3P1 loses mass and puts the shock in the wrong place; with it mass is conserved at all times and the shock position is correct (§4.3.2, Fig. 7). **Shown**
21. An explicit first-order predictor, even when computed at every DIRK abscissa, does not prevent spurious oscillations at $\Delta t=5\Delta x$ (§4.3.2, Fig. 8). **Shown**
22. Burgers shock interaction ($u_0=0.2-\sin\pi x+\sin2\pi x$, 256 cells, $\Delta t=5\Delta x$): Q3P1 is non-oscillatory and sharper than IE at $t=1/(2\pi)$, $0.6$ and $1$ (§4.3.3, Fig. 9). **Shown**
23. Buckley–Leverett (100 cells, $\Delta t=1.1\Delta x$ and $4.4\Delta x$, $t=0.085$, $\epsilon_t=\Delta t^3$): the schemes are similar at the small CFL number; at the large one Q3P1 avoids the overshoots of D3P1 (§4.4, Fig. 10). **Shown**
24. CPU time per step of Q3P1 over explicit SSP-RK3 (Intel Core i7-6600U, 2.60 GHz): 2.95, 2.82, 2.54, 3.08 for the linear equation with $N_x=200$ to $1600$; 4.48, 4.62, 3.47, 3.97 for Burgers before the shock; 4.65, 4.79, 3.75, 5.96 after it. The implicit scheme pays off when the problem does not require a time step below the explicit limit divided by this ratio (§4.5, Table 2). **Shown**
25. On nonlinear problems Q3P1 needs six Newton solves per step (three predictor and three corrector stages). With smooth data each takes at most 2 iterations, at most 3 after shocks form; for the top hat at most 3 in the first step, fewer once the rarefaction appears (§4.5, Fig. 11). **Shown**
26. On linear equations the scheme is linear in the new-time-level solution, "unlike most, if not all, high order implicit schemes available" (§5, p. 26). **Stated**

# Printed slips

- Eq. (7), p. 8: "$P_{j,0}(x)=\ldots=A+B(x-x_j)+C(x-x_j^2)$": the last term should be $C(x-x_j)^2$, as in (6).
- p. 10, below (16): "$\mathcal F^{(k)}_{j+\frac12}=\mathcal F(u^{-,(k)}_{j+\frac12},u^{+,(k)}_{j-\frac12})$": the second argument should be $u^{+,(k)}_{j+\frac12}$, as in (3), (13), (21).
- Eq. (20), p. 12: the bracket contains $-\frac\alpha2\overline u^{IE,(k)}_{j+1}$ twice; the Lax–Friedrichs term needs one of them to be $-\frac\alpha2\overline u^{IE,(k)}_{j-1}$.
- Eq. (2), p. 2: unbalanced parentheses, "$f(u(x_j+\frac12h,t)-f(u(x_j-\frac12h,t)$".
- §3.3.3, p. 14: "We define $I^3_j$ as contribution of two terms $I^3_j=I^t_j+I^{x,-}_j+I^{x,+}_j$": the sum has three terms.
- §4, p. 17: the predictor initial guess is placed "at $t^{(k)}=t^n+\theta_k\Delta t$", but the stage time is $t^n+\tilde c_k\Delta t$; $\theta_k=\tilde c_k-\tilde c_{k-1}$ is the substep fraction.
- Table 2(a), p. 25, row $N=1600$: "SSP-RK3 0.095, Q3P1 0.0293, ratio 3.08". *(Compiler check, not in the sources)*: $0.0293/0.095=0.31$, while the printed ratio 3.08 needs an SSP-RK3 time of $0.0293/3.08=0.0095$.
- Table 1, p. 18: the first row of each sub-table carries a rate (2.79, 2.36, 2.04), although no coarser grid is listed.
- Fig. 7 caption, p. 22: "at time $t=5$", while the test of §4.3.2 runs to $t=0.5$ and the plot's time axis ends near 0.5.
- §4.4, p. 24: the initial datum (39) is a step on $-0.25\le x\le0.25$, but the domain is the periodic $\Omega=[0,1]$, on which the printed interval does not fit.
- §4.2 calls (36b) "the initial double-step profile"; it is a single top hat.
- §4.5, p. 25: the break-even condition $\Delta t\le C\frac{h}{\lambda_{\max}\lceil r_N\rceil}$ leaves $C$ undefined.
- Symbol reuse: $\lambda$ is the mesh ratio and the DIRK parameter, $\theta$ the limiter ratio and the substep fraction, $C_L$ a CWENO linear weight and the low-order blending weight, $\alpha$ the Lax–Friedrichs speed and Harten's coefficient.

# Notation map

| Puppo et al. 2023 | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $h$ (cell width) | $\Delta x$ | **collision** with the registry two-point flux $h(u^-,u^+)$ |
| $j$ (cell index), $\Omega_j$, $x_j$ | $i$, $I_i$, $x_i$ | |
| $\overline u_j$ | $\bar u_i$ | cell average; the paper is finite volume |
| $u^-_{j+1/2}$, $u^+_{j+1/2}$ | $u^-_{i+1/2}$, $u^+_{i+1/2}$ | "boundary extrapolated data"; agree |
| $\mathcal F(u^-,u^+)$, $\mathcal F_{j+1/2}$ | $h(u^-,u^+)$, $\hat f_{i+1/2}$ | |
| $\alpha=\max_u\lvert f'(u)\rvert$ | $a$ (global) | global Lax–Friedrichs; **collision** with $\alpha_k$ |
| $J(f)$ | $A$ | flux Jacobian |
| $\lambda=\Delta t/h$ | $\Delta t/\Delta x$ | $\nu=a\Delta t/\Delta x$; tests quote $\Delta t=K\Delta x$; **collision** with $\lambda_l$ |
| $\Phi(\theta)$, $\theta_j$, $\sigma_j$ | $\psi(r_i)$, $r_i$, limited slope | §2 only |
| $C_j$, $\alpha_j$ | $\mathsf C_i$, $\alpha_i$ (local) | Harten's incremental coefficient (as on the [TVD](/definitions/total-variation-diminishing.md) page) and its normalized form |
| $C_0$, $C_L$, $C_R$ | $d_0$, $d_{\mathrm L}$, $d_{\mathrm R}$ | CWENO3 linear weights; values used in the tests not printed |
| $P^{(1)}_{j,L}$, $P^{(1)}_{j,R}$, $P^{(2)}_j$, $P_{j,0}$, $P_{j,rec}$ | $P_{\mathrm L}$, $P_{\mathrm R}$, $P_{\mathrm{opt}}$, $P_0$, $P_{\mathrm{rec}}$ (local, as on the [CWENO](/methods/cweno.md) page) | linear candidates, optimal parabola, central polynomial, reconstruction |
| $I_{j,k}$, $I[P]$ | $\beta_k$ | Jiang–Shu indicators; $I_{j,0}$ is computed from the coefficients of $P^{(2)}_j$ |
| $\tilde\omega_{j,k}$, $\omega_{j,k}$ | $\alpha_k$, $\omega_k$ | Jiang–Shu-type weights |
| $\epsilon_x=h^2$ | $\epsilon=\Delta x^2$ | |
| $\tau=2$ (weight exponent) | $q=2$ | **collision** with the registry global indicator $\tau$ |
| $W^\pm_{j,\ell}$ | $W^\pm_{i,l}$ (local) | linear coefficients of the interface values |
| $a_{k\ell}$, $b_k$, $c_k$, $s$ | $\mathsf a_{kl}$, $\mathsf b_k$, $\mathsf c_k$, $s$ | Butcher tableau; **collision** with the wave speed $a$ |
| $\lambda=0.4358665215$ | $\lambda_{\mathrm D}$ (local, as on the [Quinpi](/methods/quinpi.md) page) | Alexander's DIRK3 parameter |
| $\tilde c_k$, $\theta_k=\tilde c_k-\tilde c_{k-1}$ | $\tilde{\mathsf c}_k$, $\Delta\mathsf c_k$ | ordered abscissae and predictor substeps |
| $u^{IE}$, $u^{D3P1}$, $u^B$, $u^{Q3P1}$ | $u^{\mathrm{IE}}$, $u^{\mathrm{D3P1}}$, $u^{\mathrm B}$, $u^{\mathrm{Q3P1}}$ | predictor, corrector, blended and final solutions |
| $P^{(3)}_t$, $P^{(1)}_t$ | same (local) | continuous extensions of DIRK3 and of the predictor |
| $C_L$, $C_H$ (time blending) | $d^t_{\mathrm L}$, $d^t_{\mathrm H}$ (local) | **collision** with the CWENO $C_L$ in the source |
| $\omega^{L,n}_j$, $\omega^{H,n}_j$ | $\omega^{\mathrm L}_i$, $\omega^{\mathrm H}_i$ | |
| $\epsilon_t=\Delta t^\tau$ | $\epsilon_t=\Delta t^2$ | $\Delta t^3$ for Buckley–Leverett |
| $I^3_j$, $I^t_j$, $I^{x,\pm}_j$ | $\beta^{\mathrm{st}}_i$, $\beta^t_i$, $\beta^{x,\pm}_i$ (local) | space-time, time and space parts of the blending indicator |
| $\mu_{j+1/2}$ | $\delta m_{i+1/2}$ (local) | interface mass defect; registry §10 $\mu$ is an affine translation |
| $\tilde\omega^H_{j+1/2}$ | $\tilde\omega^{\mathrm H}_{i+1/2}$ (local) | harmonic mean ("reduced mass") of the high-order weights |
| $N$ | $N_x$ | number of cells |
| $r_N$ | CPU-time ratio | Q3P1 over SSP-RK3 per step |

# Reference list

The paper prints 38 references, numbered [1]–[38] and sorted alphabetically. The
list is merged complete into the [bibliography](/bibliography.md), with `citedby`
including `puppo-2023`. [3] (Arbogast et al., CMAME 368, 2020) prints no page or
article number, [23] (Harten 1984, SIAM J. Numer. Anal. 21) prints no pages, and
[34] (Semplice and Visconti, J. Sci. Comput. 83, 2020) prints the article number
6. No DOIs or arXiv identifiers are printed. No printed duplicates were found and
no item is unparseable.

# Pages created or updated

Chunk 2 (2026-10-22), cited further in chunks 3–4 (2026-10-22/23). This source is cited on:

* [Buckley–Leverett problem](/benchmarks/buckley-leverett-problem.md)
* [Burgers equation tests](/benchmarks/burgers-equation-tests.md)
* [Central WENO (CWENO)](/methods/cweno.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [Lax–Wendroff theorem](/results/lax-wendroff-theorem.md)
* [Local conservation is equivalent to a flux form](/results/local-conservation-flux-form.md)
* [Quinpi — implicit CWENO time stepping](/methods/quinpi.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Total variation diminishing (TVD) and slope limiters](/definitions/total-variation-diminishing.md)
