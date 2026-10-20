---
type: Source
title: "Sayyari & Yamaleev (2026) — Implicit dual time-stepping positivity-preserving entropy-stable schemes for the compressible Navier–Stokes equations"
description: "Solves each BDF1 or BDF2 step of a high-order entropy-stable spectral-collocation Navier–Stokes solver by explicit pseudotime iteration with the BDF term taken at the new pseudo-level, which makes every iterate provably density- and internal-energy-positive with no physical-step limit and a pseudotime bound above forward Euler's."
resource: "doi:10.1016/j.cam.2026.117735"
source_kind: paper
authors: [Sayyari M., Yamaleev N.K.]
year: 2026
venue: "J. Comput. Appl. Math. 487:117735"
local_file: "/home/stefano/papers/mosaic/ode-integration/2026_Crossref_Journal_of_Computational_and_Applied_Mathematics_Sayyari_Implicit_dual_time-stepping_positivity-preserving_entropy-st.pdf"
tags: [positivity, entropy-stability, bdf, implicit-stage-solvers, dual-time-stepping, cfd]
timestamp: 2026-10-20T14:00:00Z
---

# Summary

The authors' earlier high-order positivity-preserving entropy-stable
spectral-collocation schemes for the 3D compressible Navier–Stokes
equations were explicit in time. This paper makes them implicit in
physical time with [BDF1 and BDF2](/methods/backward-differentiation-formula.md).
The nonlinear system of each physical step is solved by **dual time
stepping**: a pseudotime derivative is added and the system is marched to
steady state in pseudotime with a forward-Euler update
([stage solvers](/methods/implicit-stage-solvers.md)). The key choice is to
take the new-level unknown of the BDF term at the *new* pseudotime level,
while the spatial residual stays explicit. The pseudotime update then
becomes a forward-Euler step applied to a modified state and scaled by a
factor $C^\tau\in(0,1)$. The positivity proofs of the explicit baseline
therefore carry over.

Theorem 1 gives a pseudotime bound for density positivity under BDF1. The
bound is *larger* than that of explicit forward Euler, because the BDF term
subtracts $\rho^n/(h\rho^k)$ from the denominator. Internal-energy
positivity reduces to a quadratic in $\Delta\tau$ with positive intercept,
so a positive admissible $\Delta\tau$ always exists. Element-wise convex
[flux limiting](/methods/bound-preserving-flux-limiting.md) between the
first-order positivity-preserving scheme and the high-order entropy-stable
scheme gives high order in space. Fully discrete
[entropy stability](/properties/entropy-stability.md) is argued for BDF1,
conditional on a converged pseudotime residual.
[Positivity](/properties/positivity-preservation.md) holds at every
pseudotime iterate with no constraint on the physical step $h$. An explicit
CFL-type bound remains on $\Delta\tau$.

Tests: a 3D viscous shock (BDF2, second order on the finest grid);
shock/boundary-layer interaction at Mach 2.15 and 6.85, where steady-state
convergence is up to about twice as fast as explicit forward Euler; a
hypersonic cylinder at Mach 17.6; and a supersonic
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at Mach 2 and 10.
In the Mach-10 Taylor–Green case BDF2 takes physical steps on average 20
times larger than SSPRK3 and saves about 30% wall-clock time. Pseudotime
step choice is governed by the positivity and CFL bounds, not by
[error-based step-size control](/methods/step-size-control.md).

# Version read

The file is the arXiv preprint 2504.11333v3 [math.NA], dated 23 Mar 2026,
35 pages; it is not the journal typeset and does not print the DOI. Page-1
title and authors match Crossref, whose title is truncated. No identity
problem. Theorem, equation and table numbers below are those of the arXiv
version.

# Key claims

Notation: $y'=f(y)$ is the semi-discrete system (the source's residual
$R$; $f_1$ first-order, $f_P$ high-order); $h$ the physical step,
$\Delta\tau$ the pseudotime step, $y^{(k)}$ the $k$-th pseudotime iterate
of step $n$; $\rho$ density, $\rho e$ internal energy per volume, $J$ the
metric Jacobian.

1. All previously published high-order positivity-preserving methods for compressible Navier–Stokes are explicit in time and hence CFL-limited; this paper's implicit dual time-stepping scheme is provably positivity-preserving and entropy-stable (§1). **Stated**
2. Nonlinear implicit solvers do not preserve positivity at each iteration, so implicit schemes solved by standard nonlinear solvers are not provably positivity-preserving (§1). **Stated**
3. BDF1 dual time stepping with forward-Euler pseudotime and the BDF unknown at level $k+1$ gives $y^{(k+1)}=\frac{h}{h+\Delta\tau}y^{(k)}+\frac{\Delta\tau}{h+\Delta\tau}y_n+\frac{h\Delta\tau}{h+\Delta\tau}f_1(y^{(k)})=C_1^\tau\bigl(y^{(k,n)}+\Delta\tau f_1(y^{(k)})\bigr)$ with $C_1^\tau=h/(h+\Delta\tau)$ and $y^{(k,n)}=y^{(k)}+\frac{\Delta\tau}{h}y_n$ (§4, Eqs. 10–13). **Derived**
4. Taking the BDF unknown at the current level $k$ instead gives a density bound on $\Delta\tau$ stricter than that of explicit Euler in physical time, so that variant is discarded (§4, Remark 1). **Stated** (no derivation shown)
5. Theorem 1: with the first-order density flux (15) and dissipation coefficients $\mathscr D^\pm\ge\lvert\hat{\bar m}^\pm\rvert/(2\rho^\pm_A)$, BDF1 dual time stepping keeps the density positive if $\Delta\tau<\min 1/\bigl(\frac2J\sum_d\frac{\mathscr D^+_d+\mathscr D^-_d}{\Delta\bar\xi_d}-\frac1h\frac{\rho_n}{\rho^{(k)}}\bigr)=\Delta\tau_1^\rho$, with no constraint when the denominator is $\le0$ (§5.1, Eq. 16). **Proved**
6. The density bound of dual time stepping exceeds the explicit forward-Euler bound $\Delta\tau^\rho_{\mathrm{FE}}$ because of the subtracted term $\rho_n/(h\rho^{(k)})$ (§1, §5.1, §8.2.1, §9). **Proved** for BDF1 (from Eq. 16); for BDF2 see claim 12
7. Internal-energy positivity for BDF1 reduces to $(\rho e)^{(k+1)}\rho^{(k+1)}/(C_1^\tau)^2=A(\Delta\tau/J)^2+B\,\Delta\tau/J+C>0$ with $C=(\rho e)^{(k)}\rho^{(k)}>0$ for an admissible iterate, so a positive bound on $\Delta\tau$ always exists; the identity holds for any spatial discretization (§5.2, Eqs. 18–19). **Derived** (proof deferred to the authors' earlier paper)
8. High-order viscous terms can make the internal-energy constraint very stiff at under-resolved features; earlier velocity and temperature limiters remove this stiffness independently of the time scheme (§5.2, Remark 2). **Stated**
9. The first-order BDF1 dual time-stepping scheme is entropy-stable in the fully discrete sense, because BDF1 is unconditionally entropy-stable (Tadmor) and all spatial terms dissipate entropy, provided the pseudotime residual is driven below a suitable norm of the BDF1 entropy dissipation (§5). **Stated**
10. The flux-limited scheme $y^{(k+1)}(\theta_f)=C_1^\tau\bigl[y^{(k,n)}+\Delta\tau\bigl(\theta_ff_P+(1-\theta_f)f_1\bigr)(y^{(k)})\bigr]$, $0\le\theta_f\le1$ per element, is positivity-preserving (using $0<C_1^\tau<1$) and entropy-stable as a convex combination of entropy-stable schemes (§6.2, Eq. 22). **Stated** (proof by reference)
11. The high-order summation-by-parts scheme with BDF1 dual time stepping is conservative and entropy-stable but not positivity-preserving in general (§6.1, Eq. 21). **Stated**
12. BDF2 dual time stepping: $y^{(k+1)}=C_2^\tau\bigl(y^{(k,n)}+\Delta\tau f(y^{(k)})\bigr)$ with $C_2^\tau=2h/(2h+3\Delta\tau)$ and $y^{(k,n)}=y^{(k)}+\frac{2\Delta\tau}{h}y_n-\frac{\Delta\tau}{2h}y_{n-1}$; density stays positive if $\Delta\tau<\min1/\bigl(\frac2J\sum_d\frac{\mathscr D_d^++\mathscr D_d^-}{\Delta\bar\xi_d}-(\frac2h\frac{\rho_n}{\rho^{(k)}}-\frac1{2h}\frac{\rho_{n-1}}{\rho^{(k)}})\bigr)=\Delta\tau_2^\rho$ (§7, Eqs. 23–25, §7.1). **Derived** (by the argument of Theorem 1; constant step only)
13. BDF2 internal-energy positivity reduces to a quadratic (26) with positive intercept, so some $\Delta\tau\in(0,\Delta\tau_2^\rho]$ keeps both density and internal energy positive (§7.2). **Derived**
14. The method extends to higher multistep schemes, but BDF3 and above are not A-stable and are not considered (§7, Remark 3). **Stated**
15. 3D viscous shock (Mach 2.5, $Re=10$), BDF2, degree 4, grids $3^3$ to $24^3$ with $h=0.32$ to $0.04$: $L^1$ errors $3.67\times10^{-4}$ to $3.44\times10^{-6}$ (rates 1.77, 2.87, 2.10), second order on the finest grid, temporal error dominant (§8.1, Table 1). **Shown**
16. Shock/boundary-layer interaction at Mach 2.15 (BDF1, degree 4): wall pressure and skin friction match explicit forward Euler and a degree-6 DG reference; the dual scheme reaches the same steady state without over-dissipating (§8.2.1, Fig. 1). **Shown**
17. In the same case, with $h$ near $\Delta\tau^\rho_{\mathrm{FE}}$ the convergence slope equals forward Euler's, although $\Delta\tau_1^\rho$ is "orders of magnitude higher"; with $\Delta\tau=3\Delta\tau^\rho_{\mathrm{FE}}$ convergence is "nearly a factor of 2" faster; raising $h$ far above $10\Delta\tau^\rho_{\mathrm{FE}}$ slows convergence because the previous physical level is a poor initial guess (§8.2.1, Fig. 2, Table 2). **Shown**
18. At Mach 6.85 BDF1 matches forward Euler but converges at a similar rate, because $\Delta\tau$ is bound by the temperature-positivity constraint, which "is sharp and cannot be relaxed" (§8.2.2, Figs. 3–4). **Shown**
19. Hypersonic cylinder (Mach 17.605, $Re=376{,}930$): the time-averaged pressure coefficient is practically identical to a fourth-order HDG reference; skin friction differs by under 10% on the coarsest grid; BDF dual time stepping and SSPRK3 give no appreciable difference (§8.3, Figs. 5–6). **Shown**
20. Taylor–Green vortex at Mach 2, $Re=400$, BDF2, $h=10^{-3}$: kinetic energy agrees with a $512^3$ WENO reference; time-averaged solenoidal dissipation 0.0067 ($32^3$) and 0.0069 ($64^3$) against 0.0054–0.0063 for the reference at $128^3$–$512^3$ (§8.4.1, Table 3, Fig. 7). **Shown**
21. Taylor–Green vortex at Mach 10: BDF2 and SSPRK3 at degree 6, $64^3$ give nearly identical kinetic energy and dilatational dissipation; BDF2 is slightly more dissipative in line profiles, explained by its physical step being on average 20 times larger (§8.4.2, Figs. 8–9). **Shown**
22. In that case BDF2 dual time stepping gives a nearly 30% wall-clock speed-up over SSPRK3 (§8.4.2). **Shown** (hardware not stated)
23. The schemes remain bound by explicit stability conditions in pseudotime; positivity-preserving nonlinear solvers are needed to exploit unconditional stability fully (§9). **Stated**

Caveats. Positivity of every iterate does not by itself prove positivity of
the converged BDF solution (a limit of positive iterates is only
nonnegative), nor convergence of the pseudotime iteration. In claim 12 the
subtracted term is positive only when $4\rho_n>\rho_{n-1}$ *(compiler check)*,
so the "bound larger than forward Euler" statement of §1 and §9 is not
guaranteed for BDF2; the paper does not discuss this. No entropy-stability
statement is made for BDF2, although the title's "entropy-stable" covers it.

# Printed slips

- Proof of Theorem 1 (pp. 12–13): "$2\rho^+_{j,A}$", "$2\rho^-_{j,A}$" with index $j$ for $i_d$; the summed inequality uses "$\sum_{l=1}^3$" over a summand indexed by $d$ and asserts "$>0$" before the step condition is introduced.
- Eq. 19: the last term of $A$ is printed $\frac{1}{\Delta t^2}(\rho_1^n(\rho E)_1^n-\|\mathbf m_1^n\|^2)$. Expanding $\rho(\rho E)-\frac12\lVert m\rVert^2$ at the new iterate gives $-\frac12\lVert m_n\rVert^2$ *(compiler check)*. The BDF2 analogue in §7.2 likewise lacks the $\frac12$.
- §5.2 and §7.2 print "$(\rho E)^{k+1}=(\rho e)^{k+1}\rho^{k+1}+(m^{k+1})^2/(2\rho^{k+1})$", dimensionally inconsistent; the identity holds only after multiplying by $\rho$.
- §8: $\epsilon_{rel}=\frac{\|u^{m+1}-u^k\|}{\|u^1-u^0\|}\frac{\Delta\tau_0}{\Delta\tau}$ mixes the indices $m$ and $k$.
- Fig. 1 legend "BDFI-152"; Fig. 6 caption lists a "15, 216" element grid against the text's 15,776, and calls the 55,216-element run BDF1 although §8.3 says BDF2.
- §4 says pseudotime is discretized "with an explicit SSP scheme", but only forward Euler is used.
- Typos: "Consequentially", "formular", "peudotime", "Setions", "CWorld Scientific" (ref. [17]); ref. [33] has a garbled author list.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Delta t$, $\Delta t_n$ | $h$, $h_n$ | physical step |
| $\hat u=[J]u$, $\hat u^n$ | $y_n$ | Jacobian-weighted conservative state |
| $R_1$, $R_p$, $R^k$ | $f_1$, $f_P$, $f(y^{(k)})$ | spatial residual (first-order, high-order, blended) |
| $\tau$, $\Delta\tau$ | same (page-local) | pseudotime and its step; **collision** with a tree $\tau$ |
| $k$ | $(k)$ superscript (page-local) | pseudotime iteration index; **collision** with the multistep $k$ |
| $\hat u^{k,n}$, $C_1^\tau$, $C_2^\tau$ | $y^{(k,n)}$, same (page-local) | modified state and scaling factor, both in the update $y^{(k+1)}=C^\tau(y^{(k,n)}+\Delta\tau f)$ |
| $\theta_f$ | same (page-local) | element flux limiter in $[0,1]$; **collision** with the polynomial coefficients $\theta_j$ |
| $\mathscr D^\pm$, $\hat{\bar m}^\pm$, $\Delta\bar\xi$, $J$ | same (page-local) | density-flux dissipation, mass flux, flux-point spacing, metric Jacobian; **collision**: $J$ is not the Jacobian of $f$ |
| $\Delta\tau_1^\rho$, $\Delta\tau_2^\rho$, $\Delta\tau^\rho_{\mathrm{FE}}$ | same (page-local) | density bounds (BDF1, BDF2, forward Euler) |
| $S=-\rho s$ | $\eta(y)$ | convex mathematical entropy |
| $p$ | $P$ (page-local) | spatial polynomial degree; **collision** with the order $p$ and, in §8, the pressure |
| $P$, $D$, $Q$, $B$ | same (page-local) | summation-by-parts matrices; **collision** with the stability polynomial $P$ |
| BDF1, BDF2 | BDF$k$, $k=1,2$ | constant-step formulas |

# Reference list

The paper prints 36 references in numbered style ([1]–[36]). The list is
merged complete into the [bibliography](/bibliography.md), with `citedby`
this slug. DOIs are printed only for [4], [11], [13], [16], [30] and [35].
Ref. [33] has a garbled author list, recorded as printed, and no pages;
[19] has no publisher; [28] is a NASA TM and [34] a workshop case
description. No printed duplicates.

# Pages created or updated

Chunk 6 (2026-10-20). This source is cited on:

* [Backward differentiation formulas (BDF)](/methods/backward-differentiation-formula.md)
* [Bound-preserving flux limiting of Runge–Kutta stages and updates](/methods/bound-preserving-flux-limiting.md)
* [Entropy stability and conservation of the fully discrete scheme](/properties/entropy-stability.md)
* [Positivity preservation in time integration](/properties/positivity-preservation.md)
* [Solving the stage equations of implicit Runge–Kutta methods](/methods/implicit-stage-solvers.md)
* [Step-size control: error-based controllers, PID filters and CFL control](/methods/step-size-control.md)
* [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
