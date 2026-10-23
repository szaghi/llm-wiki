---
type: Source
title: "Kuzmin et al. (2022) — Bound-preserving Flux Limiting for High-Order Explicit Runge–Kutta Time Discretizations of Hyperbolic Conservation Laws"
description: "Proves a semi-discrete maximum principle for bar-state ODE forms, introduces the global monolithic convex flux limiter with time-step-independent bounds, and limits the stages and final update of non-SSP Runge–Kutta methods, including Euler extrapolation and Butcher's sixth-order scheme, to keep global bounds at full order."
resource: "doi:10.1007/s10915-022-01784-0"
source_kind: paper
authors: [Kuzmin D., Quezada de Luna M., Ketcheson D.I., Grüll J.]
year: 2022
venue: "J. Sci. Comput. 91:21"
local_file: "/home/stefano/papers/mosaic/ode-integration/2022_Crossref_Journal_of_Scientific_Computing_Kuzmin_Bound-preserving_Flux_Limiting_for_High-Order_Explicit_Runge.pdf"
tags: [positivity, ssp, structure-preserving, explicit, hyperbolic-conservation-laws]
timestamp: 2026-10-20T06:18:00Z
---

# Summary

The paper asks how to guarantee a discrete maximum principle (bound
preservation, BP) for high-order finite-volume discretizations of a scalar
conservation law when the time integrator is a general high-order explicit
Runge–Kutta method. That is, beyond the order barriers of
[SSP methods](/methods/strong-stability-preserving-runge-kutta.md): order 4
explicit, order 6 implicit. Theorem 1 gives a sufficient condition for a
semi-discretization to be BP. The system is written as
$u_i'=a_i(u)(g(u)_i-u_i)$, with $g$ mapping a box into itself and
$0\le a_i\le C$. The first-order local Lax–Friedrichs (LLF) scheme in
bar-state form satisfies it. This puts the paper's
[positivity preservation](/properties/positivity-preservation.md) in the
general setting of bounds.

The authors then propose the global monolithic convex (GMC) limiter, the
core of [bound-preserving flux limiting](/methods/bound-preserving-flux-limiting.md).
It follows Zalesak's FCT algorithm but uses bounds that do not depend on the
step. A relaxation parameter $\kappa\ge0$ loosens the bounds at the price
of a tighter forward-Euler step limit $(1+\kappa)h\,\omega_i/|K_i|\le1$. The
limited semi-discretization is BP, so every SSP Runge–Kutta step is BP. For
non-SSP methods the final update is written as the forward-Euler LLF update
plus antidiffusive fluxes, and these are limited with GMC bounds;
intermediate stages are limited the same way with bounds scaled by $c_i$.
Three classes are distinguished: SSP, "internal SSP" (every stage a convex
combination of Euler steps, but not the final weights) and general methods.
Euler [extrapolation methods](/methods/extrapolation-methods.md) of any
order are internal SSP. The paper prints an 11-stage, fifth-order tableau,
ExE-RK5.

Tests use fifth-order WENO with SSPRK(5,4), ExE-RK5 and Butcher's 7-stage
sixth-order method RK76. They cover smooth and discontinuous
[linear advection](/benchmarks/linear-advection-equation.md), the
[Burgers equation](/benchmarks/burgers-equation.md) and the 1-D KPP
problem. Global bounds hold to round-off. With $\kappa=1$ (sometimes
$\kappa\ge2$) the optimal convergence rates are kept. With $\kappa=0$ they
fall to about second or third order, except for RK76 limited only at the
final stage on linear advection.

# Version read

arXiv:2009.01133v2 [math.NA], 11 June 2021 (page footer "June 14, 2021"),
32 pages (main text pp. 1–23, references pp. 23–27, Appendices A and B pp.
28–32), all read. This is the arXiv preprint, not the J. Sci. Comput.
version of record (91:21). Title and authors match the published version;
the corresponding author is Quezada de Luna. The file prints no DOI.
Section, equation and table numbers on this page are those of arXiv v2.
The slug is distinct from the bibliography's `kuzmin-2022-b`, a CMAME paper
by Kuzmin, Hajduk and Rupp.

# Key claims

Registry notation: $h$ is the step (source $\Delta t$), $s$ the number of
stages (source $M$), $Y_i$ the stage values (source $y^{(m)}$),
$A=(a_{ij})$, $b$, $c$ the Butcher coefficients (source $a_{ms}$, $b_m$,
$c_m$), $\mathcal C$ the SSP coefficient (source $\mu$), $h_{\mathrm{FE}}$
the forward-Euler step bound (source $\Delta t_{FE}$), and $f$ the
semi-discrete right-hand side (source $F$). Page-local: cell averages
$u_i$, cell volume $|K_i|$, $\omega_i=\sum_j|S_{ij}|\lambda^{\max}_{ij}$ (source $d_i$), bar states
$\bar u_i$, the relaxation parameter $\kappa$ (source $\gamma$) and the bounds $\mathcal Q_i^\pm$ (source $Q_i^\pm$), as on [bound-preserving flux limiting](/methods/bound-preserving-flux-limiting.md).

1. Methods that enforce local bounds with limiters can be at most second
   order accurate; imposing global bounds does not in general degrade the
   rates for smooth solutions (§1, citing [47]). **Stated**
2. Requiring SSP imposes an order barrier of 4 on explicit and of 6 on
   implicit Runge–Kutta methods; only backward Euler is SSP for arbitrarily
   large steps (§1, §3.1.1, citing [13]). **Stated**
3. Theorem 1 (semi-discrete maximum principle): if
   $u_i'=a_i(u)(g(u)_i-u_i)$, $u\in G\Rightarrow g(u)\in G$ for the box
   $G=[\alpha,\beta]^{N_h}$, $0\le a_i(u)\le C$ on $G$, and a unique global
   solution exists, then $u(t)\in G$ for all $t\ge0$ (§2.1, Eqs. (9)–(12)).
   The authors call it "to our knowledge, the first theoretical result of
   this kind" (§1). **Proved** (via Nagumo's lemma and a lemma of Horváth)
4. Corollary 1: the first-order LLF scheme (7) is BP with respect to global
   bounds if $\lambda^{\max}_{ij}$ is uniformly bounded on $G$ (§2.1). **Proved**
5. The LLF scheme is local extremum diminishing, because the bar states
   satisfy $\min\{u_i,u_j\}\le\bar u^L_{ij}\le\max\{u_i,u_j\}$ (Eq. (6), Def.
   3). **Derived**
6. A flux-corrected semi-discretization (14) that satisfies the constraints
   (17) with $\kappa>0$ is BP: it has the form of Theorem 1 with
   $a_i=(1+\kappa)\omega_i/|K_i|$ and $g_i\in[u_i^{\min},u_i^{\max}]$ (Eq. (18)).
   **Proved** (by reduction to Thm. 1)
7. Larger $\kappa$ relaxes the bounds $\mathcal Q_i^\pm$ (Eq. (20)) and improves
   accuracy, but the forward-Euler BP condition for LMC or GMC limiting,
   $(1+\kappa)h\,\omega_i/|K_i|\le1$ (Eq. (28)), becomes more restrictive (§3).
   **Proved** (convex-combination argument)
8. The GMC limiter (Eqs. (24)–(26)) has Zalesak's FCT structure, but its
   bounds do not depend on $h$; the discrete maximum principle holds for
   every SSP Runge–Kutta method (§2.2, §3). **Proved** (forward-Euler step)
   and **Stated** (SSP extension via [13])
9. FCT bounds (29)/(30) depend on $h$ and on the low-order predictor, so the
   nonlinear scheme has no semi-discrete or steady-state counterpart
   (Remark 4). GMC factors do not depend on $h$ and do not inhibit
   convergence to steady states (Remark 6). **Stated**
10. Classical FCT is restricted to second order in time; [42] first combined
    FCT with high-order Runge–Kutta (§3.2). **Stated**
11. Space-time GMC limiting of the final Runge–Kutta update (Eq. (40) with
    the bounds (20)) gives a fully discrete scheme that is BP for steps
    satisfying (28) and conserves mass, because the correction factors are
    symmetric and the fluxes antisymmetric (§3.2, Remark 5). **Proved**
12. "Internal SSP" methods satisfy the stage conditions (36) but possibly
    not the weight conditions (37). They include all SSP methods and the
    Euler-based extrapolation methods, which "can be constructed to have
    any desired order of accuracy". Their final update is not BP and must be
    limited (§3.1.2). **Stated**
13. Intermediate stages of a general Runge–Kutta method are in general not
    BP even for the LLF scheme; they can be limited with GMC bounds
    multiplied by $c_i$ (§3.1, §3.3). **Derived**
14. Table 2 (WENO5 semi-discretization of $\partial_x(u^2/2)$ for
    $u=\exp(-100(x-0.5)^2)$): WENO converges at order about 6.0 ($L^1$ error
    5.36e-14 at $N_h=1600$); WENO-GMC with $\kappa=0$ converges at order
    3.00 (1.63e-08 at 1600); with $\kappa=0.5$ and $\kappa=1$ the errors
    equal the unlimited ones (§5.1). **Shown**
15. Linear advection, smooth data (Table 3, $t=1$, $h=0.4\Delta x/(1+\kappa)$):
    all GMC schemes reach the optimal rates for $\kappa=1$. With $\kappa=0$
    only RK76-GMC (final-stage limiting only) keeps full accuracy (E1 =
    1.32e-10, EOC 5.00 at $N_h=1600$). SSP54-GMC drops to EOC 2.69,
    ExE-RK5-GMC to 2.66 and Sw-RK76-GMC to 2.70. The baseline schemes
    undershoot on coarse meshes ($\delta=-2.00\times10^{-5}$ at $N_h=25$)
    (§5.2). **Shown**
16. The SSP54 baseline EOC at $N_h=1600$ is 4.29, against 5.00 for ExE-RK5
    and RK76 (Table 3). **Shown** (that the fourth-order integrator limits
    the rate is a compiler reading, not the paper's)
17. Linear advection with discontinuous and peaked data (59), $N_h=200$,
    $\kappa=1$: baseline $\delta=-4.97\times10^{-6}$ at $t=1$ and
    $-1.32\times10^{-2}$ at $t=100$; GMC $\delta$ of order $-10^{-15}$. GMC
    leaves smooth regions unchanged (Fig. 2). **Shown**
18. Burgers with $u_0=0.5+\sin x$ at the pre-shock time $T=0.5$ (Table 4):
    no flux-limited scheme converges optimally for $\kappa=0$. $\kappa=1$
    restores full accuracy for SSP54-GMC, RK76-GMC and Sw-RK76-GMC;
    ExE-RK5-GMC needs $\kappa\ge2$ (EOC 2.70 at $N_h=800$ with $\kappa=1$)
    (§5.3). **Shown**
19. Burgers after the shock, $T=2$: SSP54-GMC and RK76-GMC coincide with the
    baseline solutions, which already respect the global bounds
    ($\delta=1.64\times10^{-4}$) (Fig. 3). **Shown**
20. 1-D KPP problem: a linear fifth-order reconstruction (64) with RK76 does
    not converge to the entropy solution (E1 about 1.40e-02 at $N_h=1600$,
    EOC 0.040, $\delta=-1.34\times10^{-1}$). No limiter of the paper fixes
    this while the bounds are global and the baseline oscillates strongly.
    WENO5 with RK76 converges (EOC about 0.94) even unlimited; GMC removes
    its small over- and undershoots ($\delta\approx-10^{-14}$) without
    changing the errors (Table 5, Fig. 4). **Shown**
21. Stagewise BP limiting does not degrade the high-order accuracy of the
    baseline, "at least if the bounds are global" and $\kappa>0$ (§4,
    Tables 3–4). **Shown**
22. In practice the low-order and limited methods are positivity preserving
    to machine precision, so $\delta$ can be a tiny negative number and
    simple clipping is acceptable (§5). **Stated**
23. SSP Runge–Kutta applied to the flux-corrected 1-D WENO scheme (B.8) is
    BP under $h\le\mathcal C(1+\kappa)\Delta x/(\lambda_{i+1/2}+\lambda_{i-1/2})$
    (Eq. (B.9)). **Stated** (contradicts Eq. (28); see Printed slips)
24. The same tools apply to high-order finite elements and implicit
    Runge–Kutta methods; convex limiting in space can also enforce
    semi-discrete entropy stability [33, 36, 37]; GMC and LMC are monolithic
    algebraic flux correction schemes, which give well-posed nonlinear
    problems [41] (§6). **Stated**

# Printed slips

- Eq. (B.7b) against Eq. (20): printed
  "$Q_i^+=d_i(u_i^{\max}-\bar u_i^L)+\gamma(u_i^{\max}-u_i^n)$,
  $Q_i^-=d_i(u_i^{\min}-\bar u_i^L)+\gamma d_i(u_i^{\min}-u_i^n)$". The
  $\gamma$-term of $Q_i^+$ lacks the factor $d_i$ (checked visually,
  p. 32).
- Eq. (B.9) against Eq. (28): (B.9) prints
  $\Delta t\le\mu(1+\gamma)\Delta x/(\lambda_{i+1/2}+\lambda_{i-1/2})$, but
  (28) requires the factor $(1+\gamma)$ in the denominator, as in the
  default $\Delta t=0.4\Delta x/(1+\gamma)$ of §5 *(compiler check, not in the
  sources; checked visually, p. 32)*.
- Algorithm 1 (p. 10): the outer loop "for $s=1\to S$" with
  $y^{(m)}:=u^n+\frac{\Delta t}{s}F(u^n)$ creates for $s=1$ an extra stage
  that appears neither in Table 1 (order 2 has the weights $[0,1]$) nor in
  tableau (A.2). The stage counts of Table 1 (2, 4, 7, 11) match a loop
  starting at $s=2$.
- App. A.1 says "The Butcher form of its intermediate stages is as follows"
  but prints Shu–Osher form. It also starts with
  $y^{(1)}=u^n+0.39\ldots\Delta tF(u^n)$, whereas (32) sets $y^{(1)}=u^n$,
  and §4.1.1 omits the evaluation $F(u^n)$ that A.1 uses.
- Eq. (35) writes the optimal SSP methods with 1, 2, 3 or 5 forward-Euler
  predictors as pure sequences of Euler steps, which is not how SSPRK(5,4)
  in App. A.1 is written.
- Corollary 1 (p. 5): "$w\in[u^{\min},u^{\max}]$" for $w_i$.
- §5.1 and §5.3: the wave speed $\lambda_{i+1/2}=\max\{u_i,u_{i+1},\hat u_i^+,\hat u_{i+1}^-\}$
  lacks absolute values, although $u_0=0.5+\sin x$ takes negative values.
- Table 4a: the first row prints EOC "0.00" where the other tables print
  "–".
- Fig. 2 has GMC results "dashed red" and baseline "solid blue"; Fig. 3
  reverses the convention.
- Remarks are numbered from 4; "anfidiffusive" (p. 6).
- Refs. [7], [28] and [35] are listed but never cited in the text.

# Notation map

| Kuzmin et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Delta t$, $t^n$ | $h$, $t_n$ | |
| $F(u)$, $F_i$ | $f(y)$ | semi-discrete right-hand side; **source $F$ is not the elementary differential $F(\tau)$** |
| $u_i$, $u_i^n$ | $y$ components, $y_n$ | cell averages, page-local $u_i$ on this page |
| $M$; $\tilde M$ | $s$; — | number of stages; number of forward-Euler predictors. **Source $M$ collides with the mass matrix** |
| $y_i^{(m)}$ | $Y_m$ | stage values |
| $a_{ms}$, $b_m$, $c_m$ | $a_{ij}$, $b_i$, $c_i$ | Butcher coefficients; $c_m=\sum_s a_{ms}$ used implicitly in (43)–(45) |
| $\mu$ | $\mathcal C$ | SSP coefficient (plain, not effective) |
| $\Delta t_{FE}$ | $h_{\mathrm{FE}}$ | |
| $X(\mu)=(I+\mu A)^{-1}$ | $(I+\mathcal CA)^{-1}$ | used in the SSP and internal-SSP conditions (36)–(37), entrywise inequalities |
| $\nu_i=\Delta t\,a_i$ | — | generalized Courant number of a forward-Euler step |
| **$\gamma$** | $\kappa$ (page-local) | GMC relaxation parameter $\ge0$; renamed because **$\gamma$ collides with the relaxation parameter $\gamma_n$ and the tree density $\gamma(\tau)$** |
| **$\alpha_{ij}$** | — | flux correction factors in $[0,1]$; **collide with Shu–Osher $\alpha_{ij}$** |
| $\alpha$, $\beta$ (Thm. 1) | — | box bounds; also $u^{\min},u^{\max}$ (global), $u_i^{\min},u_i^{\max}$ (local) |
| $K_i$, $\lvert K_i\rvert$, $S_{ij}$, $\lvert S_{ij}\rvert$, $n_{ij}$ | — | cell, volume, face, face area, normal |
| $H$, $H^{FE}_{ij}$, $H^{RK}_{ij}$ | — | Lax–Friedrichs numerical flux; at $u^n$; $\sum_i b_iH^*(\hat Y_i)$ |
| $\lambda_{ij}$, $d_i$ | $\lambda^{\max}_{ij}$, $\omega_i$ (page-local) | wave-speed bound, $\sum_j\lvert S_{ij}\rvert\lambda_{ij}$; **$\lambda$ is not the Dahlquist eigenvalue; $d_i$ collides with the destruction rates $d_{ij}$** |
| $\bar u^L_{ij}$, $\bar u^*_{ij}$ | — | low-order and flux-corrected bar states |
| $F_{ij}$, $F^*_{ij}$, $F^{RK}_{ij}$, $F^{(m)}_{ij}$ | — | raw and limited antidiffusive fluxes |
| $P_i^\pm$, $Q_i^\pm$, $R_i^\pm$ | —, $\mathcal Q_i^\pm$, — | Zalesak sums, bounds, ratios; **$Q$ is not the SDC collocation matrix** |
| $\delta$ | — | minimal distance to the global bounds; $\delta<0$ is a violation |
| "internal SSP" | — | stages BP, final weights possibly not; **unrelated to [internal stability](/definitions/internal-stability.md)** |

# Reference list

The paper prints 47 references in numbered style, roughly alphabetical with
some out-of-order entries (e.g. [5] Boris, [6] Horváth, [19] Anderson).
All are merged complete into the [bibliography](/bibliography.md) with
`citedby` kuzmin-2022. Only [33] prints a DOI (10.1515/jnma-2020-0056, no
volume or pages). Ref. [20] is an arXiv preprint (arXiv:2007.01212). Refs.
[7], [28] and [35] are not cited in the text. The five items printed as
Kuzmin 2020 are resolved by identity, not printed order: [32] is
`kuzmin-2020-c` (CMAME 361), [33] is `kuzmin-2021` (J. Numer. Math. 29,
printed with its online-first year 2020), [35] is `kuzmin-2020-d` (Comput.
Fluids 205), [36] is `kuzmin-2020` (CMAME 372) and [37] is `kuzmin-2020-b`
(Comput. Fluids 213).

# Pages created or updated

Chunk 5 (2026-10-20). This source is cited on:

* [Bound-preserving flux limiting of Runge–Kutta stages and updates](/methods/bound-preserving-flux-limiting.md)
* [Burgers equation](/benchmarks/burgers-equation.md)
* [Extrapolation methods (Richardson extrapolation of a base integrator)](/methods/extrapolation-methods.md)
* [Invariant-domain preserving high-order time stepping (explicit and IMEX)](/methods/invariant-domain-preserving-time-stepping.md)
* [Linear advection equation](/benchmarks/linear-advection-equation.md)
* [Order reduction](/definitions/order-reduction.md)
* [Positivity preservation in time integration](/properties/positivity-preservation.md)
* [Strong-stability-preserving (SSP) Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md)
