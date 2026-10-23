---
type: Method
title: "WLS-ENO reconstruction"
description: "WLS-ENO is a single-stencil finite-volume reconstruction: a weighted least-squares fit whose row weights fall where neighbouring averages jump; Liu et al. make it conservative with a zero-mean basis and locally divergence-free for the magnetic field, and run it in second- and third-order ideal-MHD schemes, with a Zhang–Shu or Barth–Jespersen limiter and an HLL or generalized-Riemann-problem flux."
status: established
aliases: [WLS-ENO, weighted least-squares ENO, conservative WLS-ENO, locally divergence-free WLS-ENO, LDF WLS-ENO]
tags: [reconstruction, finite-volume, mhd, positivity, riemann-solver]
timestamp: 2026-10-23T03:53:00Z
---

# WLS-ENO reconstruction

**WLS-ENO** (Liu & Jiao 2016, as recalled by Liu, Zhang, Li & Shen 2021, §1, §2.3) reconstructs, in a
finite-volume cell $I_i$ with centroid $(x_i,y_i)$, a single polynomial of degree $n$ (page-local) by a
**weighted least-squares** fit to the cell averages of a whole stencil. Unlike
[WENO](/methods/weno-js-reconstruction.md), it has no candidate stencils and no convex combination:
non-oscillation is sought by down-weighting the rows of the fit that come from neighbours across a
jump. The row weight of neighbour $j$ is computed once, directly from the cell averages,

$$W_j=\frac1{(\bar u_j-\bar u_i)^2+\epsilon h_i^2},\qquad \epsilon=10^{-2},\qquad h_i=\sqrt{|I_i|},$$

(page-local $W_j$, $h_i$), so that $W_j=O(h_i^{-2})$ in smooth regions and $O(1)$ across a
discontinuity (§2.3). In the original scheme the cell's own row is included with weight
$\alpha_{\mathrm c}\max_jW_j$ over edge neighbours, $\alpha_{\mathrm c}>1$ ($1.5$; page-local), so the
cell average is matched only in the least-squares sense (Eq. (8)). Liu et al. (§1) contrast it with
Ollivier-Gooch's DD-$L_2$-ENO, which computes the weights from the residual of a first, geometrically
weighted solve and solves again, and with single-stencil $k$-exact and CENO schemes, which need
limiters "which may cause difficulties in convergence". They recall from Liu & Jiao that WLS-ENO
"generally has higher accuracy than the WENO scheme near the discontinuity and is less sensitive to
mesh quality" (§1; not shown in this paper).

## Conservative WLS-ENO

Following Ollivier-Gooch, Liu et al. (2021, §3.1–3.2, Eqs. (9)–(12), (21)–(23)) write the polynomial in
a zero-mean basis, so that its cell average is $\bar u_i$ exactly:

$$u^{\mathrm R}_i=\bar u_i+\sum_{q=1}^n\sum_{p_1+p_2=q}\frac{1}{p_1!\,p_2!}\,
\frac{\partial^qu}{\partial x^{p_1}\partial y^{p_2}}\Big|_i\Big((x-x_i)^{p_1}(y-y_i)^{p_2}-\overline{x^{p_1}y^{p_2}}_i\Big),$$

with $\overline{x^{p_1}y^{p_2}}_i$ the moments of $I_i$ about its centroid (page-local exponents
$p_1,p_2$). Each neighbour gives one equation
$\bar u_j-\bar u_i\approx\sum\frac1{p_1!p_2!}\partial^qu|_i\big(\widehat{x^{p_1}y^{p_2}}_{ij}-\overline{x^{p_1}y^{p_2}}_i\big)$,
with $\widehat{x^{p_1}y^{p_2}}_{ij}$ the moments of $I_j$ about the centroid of $I_i$ (shift formula
Eq. (23)); the weighted system for the $\tfrac{(n+1)(n+2)}2-1$ derivative coefficients is solved in
least squares, with the weights $W_j$ above and no central-cell row. For $n=2$ the truncation error is
$O(h^3)$.

**Stencils.** In the $m$-ring notation of Liu & Jiao (cells sharing an edge form the 1/2-ring, cells
sharing a vertex the 1-ring), the stencil should be balanced around the cell with about 1.5–2 times as
many cells as unknown coefficients; larger stencils "seem to be more stable". On Cartesian grids Liu et
al. use the 1/2-ring (4 cells) for $n=1$ and the 1-ring (8 cells) for $n=2$ (§3.3.1).

**Solver.** The least-squares problems can become ill-conditioned under refinement; they are solved by
truncated SVD (LAPACK DGESVD), discarding singular values below $\sigma_1\times10^{-10}$ by default
(§3.3.2).

## Locally divergence-free magnetic field

Componentwise reconstruction does not make $\partial_xB^{\mathrm R}_1+\partial_yB^{\mathrm R}_2$ vanish
inside the cell. Liu et al. (2021, §3.1, Eqs. (13)–(20)) impose it exactly:

1. reconstruct $B_2$ by conservative WLS-ENO;
2. fix the coefficients of $B_1$ that appear in $\partial_xB_1$ by matching coefficients of
   $\partial_xB_1^{\mathrm R}=-\partial_yB_2^{\mathrm R}$; for $n=2$:
   $\partial_xB_1|_i=-\partial_yB_2|_i$, $\partial^2_xB_1|_i=-\partial_x\partial_yB_2|_i$,
   $\partial_x\partial_yB_1|_i=-\partial^2_yB_2|_i$ (the system printed as Eq. (17));
3. fit the remaining, pure-$y$ coefficients of $B_1$ by a reduced weighted least-squares problem
   (Eq. (18));
4. repeat with the roles of $B_1$ and $B_2$ exchanged and average the two results (Eqs. (19)–(20)).

Both rounds are divergence-free and conservative, hence so is their average. For degree $n$ the
coefficient-matching system has size $\tfrac{n(n+1)}2$, is upper triangular with diagonal entries
$1/\big((p_1-1)!\,p_2!\big)$ and therefore uniquely solvable; the remaining fit has $n$ unknowns
(§3.2, Eqs. (24)–(26)). One-round reconstructions gave "slightly higher" errors in the constrained
component; the averaged one removes the bias and is "slightly stable[r]" (§3.1). Only $B_1$, $B_2$ are
constrained, in 2-D ([divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)).

## In a positivity-preserving MHD scheme

Liu et al. (2021, §2, §3.3) embed the reconstruction in the positivity-preserving finite-volume
framework of Wu & Shu for ideal MHD with the Godunov–Powell term
$-(\nabla\cdot B)\,\Phi_{\mathrm P}(u)$, $\Phi_{\mathrm P}=(0,B,v,v\cdot B)$ (page-local):
[HLL](/methods/hll-riemann-solvers.md) fluxes at $N_g$ Gauss points per edge ($N_g=n$), the Powell term
upwinded with the HLL speeds, a [Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md) on
density and pressure at Gauss⊗Gauss–Lobatto points with floor $\min\{10^{-13},\bar u_i\}$ (Eqs.
(36)–(38)), and SSP-RK2 ($n=1$) or SSP-RK3 ($n=2$) ([bound preservation](/properties/bound-preservation.md),
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md)). Because the reconstruction is locally divergence-free,
the cell-interior part of the discrete divergence in the Powell term equals the cell integral of
$\nabla\cdot B^{\mathrm R}_i$, which vanishes when the edge quadrature is exact; in floating point it
does not, and keeping it "may lead to a failed simulation", so the code drops it and keeps only the
normal-jump part (Eqs. (32)–(35)). No limiter other than the positivity limiter is used.

## Results

- **Smooth Alfvén wave** ($t=2$, $16^2$–$256^2$): $L_1$ orders of $v_1$ 2.09, 1.99, 2.43, 2.38 for $n=1$
  and 2.88, 3.00, 2.82, 3.02 for $n=2$; $L_1(v_1)$ at $256^2$ is $3.78\times10^{-5}$ and
  $1.59\times10^{-6}$, at 580.81 s and 6450.53 s on 64 cores; below an error of about $10^{-3.6}$ the
  third-order scheme is cheaper for equal error (§4.1, Table 1, Fig. 4).
- **[Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md)** ($200^2$, $t=3$): sharp shocks; relative
  total-energy deviation within $10^{-5}$ for $n=2$ (§4.2).
- **Rotor** ($t=0.295$): no negative pressure and no distortion of the central Mach contours, which
  earlier work attributes to divergence errors; divergence norm below $10^{-3}$ (§4.3).
- **[MHD blast wave](/benchmarks/mhd-blast-wave.md)** (ambient plasma beta $2.51\times10^{-4}$,
  $200^2$): no negative pressure; density "significantly smoother" than in three cited works (§4.4).
- **Mach 800 dense jet** (plasma beta $10^{-4}$, $200\times300$): positive for $n=1$; for $n=2$ the
  pressure turns negative at $t=4.45\times10^{-4}$ with the default SVD threshold and the run succeeds
  with $\sigma_1\times10^{-6}$, the failure being "possibly attributed to ill-conditioned matrix"
  (§4.5; [high-Mach jets](/benchmarks/high-mach-astrophysical-jet.md)).

## With a generalized-Riemann-problem flux

Liu, Feng & Wang (2023a, §3.1) reuse the locally divergence-free WLS-ENO at second order ($n=1$, four
face neighbours, the row weights above with $\epsilon=10^{-2}$, truncated SVD with threshold
$\sigma_1\times10^{-10}$) in a one-step finite-volume scheme for ideal MHD whose flux is the HLL
approximate solver of the generalized Riemann problem, applied edge by edge after rotation to the edge
normal ([generalized Riemann problem](/methods/generalized-riemann-problem.md),
[HLL-family solvers](/methods/hll-riemann-solvers.md)). Three differences from Liu et al. (2021):

- **Primitive variables.** The reconstruction acts on $(\rho,v,B,p)$; the conservative gradients that the
  generalized Riemann problem needs are assembled at each edge midpoint by the product and chain rules
  (Eqs. (30)–(40)).
- **One constraint round.** $\partial_xB_1|_i=-\partial_yB_2|_i$ is imposed after reconstructing $B_2$, and
  $\partial_yB_1$ comes from a one-unknown weighted fit (Eqs. (23)–(24)). Constraining $\partial_yB_2$ instead,
  or both and averaging, "didn't make much difference" (no data shown); Liu et al. (2021) report a
  slight advantage for the average.
- **Limiter.** Instead of the Zhang–Shu scaling, a Barth–Jespersen limiter on density and pressure bounds
  their values at the edge midpoints by the extrema of the neighbouring averages, which the authors call
  a "PP limiter" (Eqs. (25)–(29)). The CFL condition of Wu & Shu is applied "without making a rigorous
  proof" of positivity (§2.2) ([bound preservation](/properties/bound-preservation.md)).

The smooth [Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md) at CFL 0.2 converges at $L_1$
orders 2.11, 1.95, 2.36, 1.86 with the generalized-Riemann-problem flux and 2.10, 1.99, 2.44, 2.39 with
SSP-RK2 and the HLL flux; the $L_1(v_1)$ errors at $256^2$ are $5.54\times10^{-5}$ and
$3.68\times10^{-5}$, at 4202 s and 1681 s on 64 cores, the cost of the one-step scheme attributed to its
SVD solves (§4.2, Table 1). No run on Brio–Wu, Orszag–Tang to $t=100$, the rotor or 2-D and 3-D blast
waves produced negative density or pressure (§4–5;
[Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md), [MHD blast wave](/benchmarks/mhd-blast-wave.md),
[Brio–Wu shock tube](/benchmarks/brio-wu-shock-tube.md)). *(Compiler check, not in the sources: the SSP-RK2
errors are close to the $3.78\times10^{-5}$ of the $n=1$ scheme of Liu et al. (2021) at the same mesh,
whose limiter and time step rule differ.)*

## The same idea at second order

Chen, Zhang, Liu & Chen (2022, §5, Eq. (24)) use solution-dependent least-squares weights in a
second-order unstructured finite-volume scheme, relating them to the solution-dependent least
squares of Mandal et al. rather than to WLS-ENO: in the fit of a linear function at each mesh vertex
$a$ through the surrounding cell values, the geometric weight $w_i$ of cell $i$ becomes
$w_i/\big((p_a-p_i)^2+\epsilon\big)$, with the vertex and cell pressures as the only detector, so one
matrix serves all variables, and $\epsilon=10^{-3}$ by default
([gradient reconstruction on unstructured meshes](/methods/unstructured-gradient-reconstruction.md)).
The vertex gradients are then combined by WENO-JS-type weights, and no limiter is used. *(Compiler
check, not in the sources: with $\epsilon$ fixed rather than proportional to $h_i^2$ as in WLS-ENO,
the weights tend to the geometric ones in smooth regions as the mesh is refined, and a row across a
jump is reduced by a factor of about $\epsilon/(\Delta p)^2$, independent of $h$, against $O(h_i^2)$
in WLS-ENO; both regularizations use the data in absolute units.)*

## Qualifications

- **ENO property.** "Retains ENO property" (§3.1, §5) is asserted, neither proved nor measured
  ([ENO property](/definitions/eno-property.md)); the weights reduce a row across a jump by a factor
  $O(h_i^2)$ relative to smooth rows, they do not remove it *(compiler check, not in the sources)*.
- **Positivity guarantee.** The framework of Wu & Shu is provably positivity-preserving under its own
  divergence discretization and a CFL condition; the implementation drops the interior divergence term
  and the paper prints no CFL number or time-step rule, and the jet failure shows that positivity is
  not guaranteed in practice. The limiter is applied to a "reconstructed polynomial" of the pressure,
  whose relation to the reconstructed conserved variables is not described.
- **Orders.** The $n=1$ rates 2.43 and 2.38 exceed the design order 2 without comment; the claim that
  higher order is cheaper on the rotor (§4.3) compares $n=2$ at $200^2$ (3731 s) with $n=1$ at $600^2$
  (8788 s) by visual quality only.
- **Printed slips.** The jet domain is printed as $[0,0.5]\times[0,1.5]$ although the nozzle spans
  $-0.05<x<0.05$, and the rotor is printed with periodic boundaries on $[0,1]^2$ without comment; Eq. (17) solves for
  $\partial^2_xB_1|_i$ while the text names $\tfrac12\partial^2_xB_1|_i$; "conservative WLE-ENO" for
  WLS-ENO (§3.2).
- Liu et al. (2023a) state that their scheme attains "the expected convergence order"; the finest-level
  rate 1.86 is below the SSP-RK2 one and the authors do not discuss the drop.
- Locally divergence-free is not globally divergence-free: the normal component stays discontinuous
  across edges, which the Powell term only controls (§3.3.3, §5).

# Citations

- [Liu et al. (2021)](/sources/liu-2021.md) — Abstract; §1; §2, Eqs. (1)–(8); §3.1–3.3, Eqs. (9)–(38); §4, Table 1, Figs. 4–17; §5.
- [Liu et al. (2023a)](/sources/liu-2023.md) — §2.2; §3.1, Eqs. (19)–(40); §3.3; §4, Table 1; §5.
- [Chen, Zhang, Liu & Chen (2022)](/sources/chen-2022.md) — §5, Eq. (24).
