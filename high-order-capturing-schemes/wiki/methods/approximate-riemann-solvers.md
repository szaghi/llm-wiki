---
type: Method
title: "Approximate Riemann solvers as building blocks of capturing schemes"
description: "The interface fluxes used by capturing schemes in this corpus: Lax–Friedrichs/Rusanov, Roe with the Harten–Hyman entropy fix, Osher, the approximate-state solvers (PVRS, TRRS, TSRS, adaptive), HLL and HLLC (with positivity-preserving wave speeds), HLL-BVD, HLLI/LLFI, the Riemann-solver-free MUSTA flux, the MHD solvers of Brio–Wu (Roe-type) and Dai–Woodward (nonlinear), and multidimensional HLL/LLF solvers for edge electric fields."
status: established
aliases: [Riemann solver, HLL, MUSTA, FORCE, HLLI, Rusanov flux, HLL-BVD, Roe-type MHD solver]
tags: [riemann-solver, numerical-flux, finite-volume, positivity]
timestamp: 2026-10-13T00:00:00Z
---

# Approximate Riemann solvers as building blocks

A capturing scheme evaluates $\hat f(u^-_{i+1/2}, u^+_{i+1/2})$ at each
interface. At first order this is a [monotone flux](/definitions/monotone-flux.md)
or an E-flux; at high order its choice still sets contact and shear
resolution and robustness. Finite-volume WENO and
[AFD-WENO](/methods/alternative-finite-difference-weno.md) accept any
solver. Classical FD-WENO needs a smooth flux splitting and so is
restricted to Lax–Friedrichs or Roe-type fluxes
([Balsara et al. (2025)](/sources/balsara-2025.md), §I).
HLL, its wave-speed estimates and its Rusanov and Lax–Friedrichs special
cases are gathered on the [HLL Riemann solver](/methods/hll-riemann-solver.md) page.

* **Lax–Friedrichs / Rusanov / LLF**: centred average plus dissipation
  $\alpha$. It is robust and positivity-preserving for Euler under
  $\nu \le 1$ ([positivity preservation](/properties/positivity-preserving.md)),
  but it does not open the Riemann fan, so contacts smear.
  Titarev and Toro's WENO-HLLC and WENO-MUSTA are about twice as
  accurate on the same mesh as the Rusanov-based FV-WENO of Shi, Hu and
  Shu ([Titarev & Toro (2004)](/sources/titarev-2004.md), §5.1–5.2).
* **HLLC** (Toro, Spruce & Speares): a three-wave model with speeds
  $S_L \le S_M \le S_R$ and two star states. It contains all waves of the
  Euler Riemann fan, uses no linearization, and works for low density
  and sonic points without fixes ([Titarev & Toro (2004)](/sources/titarev-2004.md), §4.1).
  With the wave speeds of Batten et al. it resolves isolated shocks and
  contacts exactly. The star states stay in $\mathcal{G}$, so the
  first-order scheme is positivity-preserving under
  $\Delta t\,\Vert\vert\mathbf v\vert + c\Vert_\infty/h \le 1$
  ([Guo, Xiong & Shi (2014)](/sources/guo-2014.md), §2.4, Remark 1). Being
  less dissipative, it can leave oscillations in velocity and internal
  energy near vacuum, where Lax–Friedrichs is cleaner (Examples 6, 8).
* **MUSTA** (Toro): opens the Riemann fan numerically by evolving the
  two-cell data with a first-order predictor flux — FORCE, whose
  viscosity is half the Lax–Friedrichs one — for $k$ stages
  ($k = 2$–$3$ approaches the exact Godunov flux; $k = 2$ is used). It
  needs no eigenstructure, so it suits systems whose characteristic
  information is unknown, at a cost comparable to approximate Riemann
  solvers. HLLC resolves slip lines better than MUSTA in the
  [double Mach reflection](/benchmarks/double-mach-reflection.md)
  ([Titarev & Toro (2004)](/sources/titarev-2004.md), §§4.2, 5.3).
* **Roe** for MHD shock tubes and **HLLC** for Euler in GP-WENO
  ([Reyes et al. (2018)](/sources/reyes-2018.md), §5).
* **HLLI / LLFI** (Dumbser–Balsara): HLL-type solvers that resolve
  intermediate (linearly degenerate) waves, used throughout AFD-WENO.
  A solver that keeps stationary contacts makes the whole AFD scheme do
  so, which helps well-balancing ([Balsara et al. (2025)](/sources/balsara-2025.md), §II).
* **Multidimensional HLL / LLF** solvers at mesh edges, for the
  electric field of the induction equation; they reduce to the 1D
  solver for one-dimensional variation
  ([constrained transport](/methods/constrained-transport.md);
  [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §3).

In 3D FV-WENO the flux integral over a face is approximated by a tensor
Gauss rule, so a Riemann solve is needed at each face Gauss point
([finite-volume reconstruction](/methods/finite-volume-reconstruction.md);
[Titarev & Toro (2004)](/sources/titarev-2004.md), §2).

**In one-step schemes (batch 4).**
* *Space–time averaged fluxes.* Freezing the HLL signal speeds at the
  face's space–time barycentre makes the flux linear in the
  predictor's states and fluxes, which are then averaged exactly
  instead of solving Riemann problems at every quadrature point
  ([Balsara et al. (2009)](/sources/balsara-2009.md), §4.1; [ADER](/methods/ader.md)).
* *Linearized vs HLL for MHD.* In the decay of torsional Alfvén waves,
  a linearized MHD Riemann solver is much less dissipative than HLL.
  The gap narrows as the order rises, because better reconstruction
  shrinks the interface jumps, so cheaper solvers become acceptable at
  high order ([Balsara et al. (2009)](/sources/balsara-2009.md), §7.2).
* *Rusanov and Osher-type fluxes* (the path-integral flux of Dumbser and
  Toro, evaluated with Gauss–Legendre quadrature) serve the ADER-WENO
  and ADER-DG schemes on adaptive meshes ([Dumbser et al. (2013)](/sources/dumbser-2013.md), §2.1; [Dumbser et al. (2014)](/sources/dumbser-2014.md), §2.3;
  [Zanotti et al. (2015)](/sources/zanotti-2015.md), §3.2).
* *Linear systems* use the exact Riemann solver,
  $\tfrac12\left(A + \vert A\vert\right)u^- + \tfrac12\left(A - \vert A\vert\right)u^+$,
  with $A$ the Jacobian along the face normal and
  $\vert A\vert = R\vert\Lambda\vert L$
  ([Dumbser & Käser (2007)](/sources/dumbser-2007.md), eqs. 30–31).

**Later uses (batch 6).**
* *Relativistic MHD.* HLLC (Mignone–Bodo; Kim–Balsara, modified so that
  both star states share the normal velocity and total pressure) and
  HLLEM (Dumbser–Balsara), which keeps isolated contacts and Alfvén
  discontinuities without iteration. Relativistic HLLD is expensive and
  brittle. Positivity proofs exist only for first-order 1D schemes: for
  the HLL/HLLEM class on Euler flow (Einfeldt; Einfeldt et al.; qualified
  for HLLEM in the batch-16 block), for HLLC
  on 1D Euler and 1D MHD; none exist for Roe- or Osher-type solvers, and
  none for a subluminal RMHD solver
  ([Balsara & Kim (2016)](/sources/balsara-2016-b.md), §§1, 4.1, Appendix B).
* *Multidimensional solvers with sub-structure.* At a vertex, four states
  bound a strongly interacting state by $[S_L, S_R]\times[S_D, S_U]$.
  Keeping linear variation of the entropy and Alfvén waves inside it
  reduces dissipation, and without it the solver is the multidimensional
  HLL ([Balsara & Kim (2016)](/sources/balsara-2016-b.md), §4.2;
  [constrained transport](/methods/constrained-transport.md)). An LLF
  version at vertices upwinds a scalar potential, with dissipation
  $\frac{|v_d|}{2h_d}$ times a second difference in each direction
  ([Balsara et al. (2023)](/sources/balsara-2023.md), §§2.5, 3.4;
  [curl-preserving reconstruction](/methods/curl-preserving-reconstruction.md)).
* *HLLD and GFORCE* serve fourth-order finite volume for MHD and RMHD, with
  upwind-CT coefficients for each. On field-loop advection the solver
  choice matters only marginally ([Berta et al. (2024)](/sources/berta-2024.md), §§3.3, 5.4, Appendix B).
* *Accuracy versus dissipation at second order.* On the MHD vortex, Roe
  and HLLE errors are comparable, but HLLE is more dissipative on decaying
  Alfvén waves. HLLE also costs less as the number of species grows, and is
  carbuncle-free ([Balsara (2004)](/sources/balsara-2004.md), §§3.4, 6, 7.1).

**Later uses (batch 7).**
* *A Roe-type TVD solver for MHD* ([Ryu & Jones (1995)](/sources/ryu-1995.md), §2.3). Harten's
  second-order TVD scheme on the renormalized MHD eigensystem with
  arithmetic interface states, a per-family entropy fix (parameter 0.1,
  0.2, 0.1, 0 for the fast, Alfvén, slow and entropy families) and
  steepening of the Alfvén families. A nonlinear MHD Riemann solver with
  exact rarefactions, replacing Dai and Woodward's "rarefaction shocks",
  serves as reference (§3).
* *Entropy-conservative and entropy-stable fluxes for GLM-MHD*
  ([Derigs et al. (2018)](/sources/derigs-2018.md), §§4.2–4.5). $\hat f^{\mathrm{EC}}$ from arithmetic and
  logarithmic means, then $\hat f^{\mathrm{ES}}$ by adding Lax–Friedrichs,
  local Lax–Friedrichs or matrix dissipation in entropy variables. Roe's
  solver shows an entropy glitch in the sonic rarefaction of Toro's
  modified Sod problem and of a modified Brio–Wu problem; the ES flux does
  not (§5.7).
* *HLLI* adds to HLL a linear sub-structure for chosen intermediate
  families with weight
  $\delta_p = 1 - \min(\lambda^{(p)}, 0)/S_L - \max(\lambda^{(p)}, 0)/S_R$; it is
  "complete" when all are included, and HLLD lacks the slow waves
  ([Balsara (2017)](/sources/balsara-2017-d.md), Apps. D–E).
* *Solver quality against order.* On torsional Alfvén-wave decay, HLL with
  a multidimensional solver without sub-structure dissipates about 6 times
  more than HLLI with sub-structure at second order, 3 times more at
  third, and "almost negligible" more at fourth ([Balsara (2017)](/sources/balsara-2017-d.md), §IX.5).
* *An exact face solve of the cleaning subsystem* before a seven-wave Roe
  solver ([Mignone & Tzeferacos (2010)](/sources/mignone-2010-b.md), §3.2;
  [hyperbolic divergence cleaning](/methods/hyperbolic-divergence-cleaning.md)).

**Later uses (batch 8).**
* *HLLEM has its own page* ([HLLEM (HLLI) Riemann solver](/methods/hllem-riemann-solver.md)).
  [Dumbser & Balsara (2016)](/sources/dumbser-2016.md) are the primary source of the HLLI weight $\delta_p$
  quoted above. They name the solver HLLEM throughout and offer "HLLI"
  only as an alternative name (abstract, §4). "LLFI" does not occur in
  that paper, so the bullet "HLLI / LLFI (Dumbser–Balsara)" rests on
  [Balsara et al. (2025)](/sources/balsara-2025.md) for LLFI. The paper
  asserts, but does not prove, that HLLEM inherits the positivity of HLL,
  for general (conservative and non-conservative) hyperbolic systems.
  Balsara & Kim state that Einfeldt et al. proved positivity for the
  HLL/HLLEM class for 1D first-order schemes on Euler flow
  ([Balsara & Kim (2016)](/sources/balsara-2016-b.md), §1) (HLLE only,
  per the batch-16 block below).
* *Complete solvers and shock instability.* HLLC is HLL plus an
  anti-diffusive term, $\hat f^{\mathrm{HLL}} + S_L(u^{\mathrm{HLLC}}_{*L} - u^{\mathrm{HLL}}_*)$
  for $S_L \le 0 \le S_M$ ([Simon & Mandal (2019)](/sources/simon-2019.md), eq. 13). Solvers that resolve the
  contact and shear waves (Godunov, Roe, HLLC, HLLEM) are prone to the
  carbuncle, odd–even decoupling and kinked Mach stems at strong
  grid-aligned shocks ([Simon & Mandal (2019)](/sources/simon-2019.md); [Simon & Mandal (2019b)](/sources/simon-2019-b.md); [Xie et al. (2021)](/sources/xie-2021.md), §6;
  [numerical shock instability](/definitions/numerical-shock-instability.md), [cures for numerical shock instability](/methods/shock-instability-cures.md)).
* *Wave-speed estimates.* What Xie et al. call Einfeldt's speeds are
  $S_L = \min(v_n^- - c^-,\ v_n - c)$ and $S_R = \max(v_n^+ + c^+,\ v_n + c)$,
  the second argument at the Roe state; they give the exact speed of an
  isolated shock. Toro prints a different formula under Einfeldt's name
  (batch-12 bullet "Two formulas called Einfeldt's" below). Davis's are
  $S_L = \min(v_n^- - c^-,\ v_n^+ - c^+)$ and $S_R = \max(v_n^- + c^-,\ v_n^+ + c^+)$.
  They are more diffusive and "useful for suppressing possible post-shock
  oscillations" ([Xie et al. (2021)](/sources/xie-2021.md), eqs. 10–11, §5).
* *Source waves inside the solver* (shallow water with a bed slope). The
  augmented Roe solver adds the source as a stationary wave. It is
  complete and well balanced, but it develops carbuncles. HLLS is HLL plus
  the same stationary wave and ignores the contact. It is free of
  carbuncles and smears shear waves ([Navas-Montilla & Murillo (2019)](/sources/navasmontilla-2019.md), §§3, 4.2.1;
  [well-balanced schemes](/properties/well-balanced.md)).
* *Flux families beyond Godunov type.* For first-order AUSM-family and
  flux-vector-splitting fluxes, Kitamura & Shima rank robustness at
  shocks. Roe is vulnerable, AUSM+-up, LDFSS and SLAU sit in the middle,
  and van Leer, AUSMPW+, RoeM2 and SLAU2 are "almost (but not perfectly)
  free" ([Kitamura & Shima (2019)](/sources/kitamura-2019.md), §§II.B, III.E).
* *Low Mach.* Roe's dissipation in the momentum equations scales like
  $1/\mathrm{Ma}$, so it swamps the flux as the Mach number falls.
  Rescaling only the dissipation cures it
  ([Miczek et al. (2015)](/sources/miczek-2015.md); [Edelmann et al. (2021)](/sources/edelmann-2021.md), §3.2;
  [low-Mach-number fluxes](/methods/low-mach-number-fluxes.md)).

**Later uses (batch 11).**
* *The original Roe-type MHD solver* ([Brio & Wu (1988)](/sources/brio-1988.md), §§IV.1, VII).
  An exact Roe matrix for $\gamma = 2$ and, for general $\gamma$, the
  Jacobian at an arithmetic-mean state; the averaging, its loss of the
  exact jump property, the comparison of the two versions on the
  [Brio–Wu shock tube](/benchmarks/brio-wu-shock-tube.md) and the
  renormalized eigenvectors are on the
  [characteristic decomposition](/methods/characteristic-decomposition.md)
  page. The second-order scheme costs about 10 times the floating-point
  operations of Lax–Wendroff per point and step, yet with 200 points it
  gives "a reasonable result" where Lax–Wendroff needs 800, and is then
  the more efficient.
* *A nonlinear MHD Riemann solver* ([Dai & Woodward (1994)](/sources/dai-1994.md), §§4–6).
  A seven-wave solver in Lagrangian mass coordinates, meant to supply
  interface fluxes to a PPM-type Godunov scheme. Every wave is treated as
  a discontinuity: fast and slow shocks, two rotational discontinuities
  and a contact. Rarefactions become "rarefaction shocks" that obey the
  jump conditions with an entropy decrease, so the solver is exact only
  when no rarefaction is present and applies to weak rarefactions.
  Closed formulas give the shock speed from the post-shock transverse
  field, and a cubic gives the field jump from the shock speed. A Newton
  iteration on three transverse-field values and the common field
  orientation closes the fan at the contact. The initial guess blends a
  linear Riemann-invariant solver with a one-strong-wave guess; a
  relaxation factor handles several strong waves; where the solver
  fails, the code takes the average of the left and right states for the
  flux. Intermediate shocks are excluded by construction. One Newton
  iteration is "enough to obtain sufficiently accurate fluxes in an
  actual code even for very strong MHD shocks", and the unoptimized
  solver does 348,143 Riemann problems per second on a Cray-C90. These
  are the "rarefaction shocks" that Ryu & Jones replace by exact
  rarefactions (batch-7 bullet above).
* *HLL-BVD: HLL accurate at contacts* ([Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md), §II).
  With Davis's speeds and $S_L \le 0 \le S_R$,
  $$\mathbf d^{\mathrm{HLL}} = \frac{S_R + S_L}{2(S_R - S_L)}\left(f(u^-) - f(u^+)\right) - \frac{S_L S_R}{S_R - S_L}\left(u^- - u^+\right),$$
  and the paper identifies the density jump in the second,
  state-difference term as what smears contacts. Each cell carries a
  MUSCL polynomial and a THINC (tanh) jump profile of density, with
  steepness 1.6 in every test. At each face a BVD (boundary variation
  diminishing) selection takes, among the four combinations of the two
  profiles from left and right, the density pair with the smallest jump,
  and only that density enters the state-difference term (eqs. 15–17).
  The wave speeds and the two-wave fan are unchanged. The paper does not
  say which density enters $f(u^\mp)$ and the wave speeds. It is second
  order (MUSCL) only, with no convergence study. In tests HLL-BVD
  resolves contacts more sharply than HLL and, in most tests, HLLC, and
  it shows none of HLLC's odd–even decoupling, Sedov axis oscillations or
  kinked Mach stem (§§III F–H;
  [cures for numerical shock instability](/methods/shock-instability-cures.md)).
  The robustness is observed, not proved; HLL's positivity and entropy
  properties are restated for HLL but not claimed for HLL-BVD. The paper
  also reviews Mandal & Panwar's HLL fix, which replaces the density
  jumps of the state-difference term by pressure jumps under a local
  isentropy assumption that "may not always hold" (§II C).
* *HLLI is a family.* Balsara & Nkonga derive a second HLLI with a
  first-moment (Galerkin) constraint, a shifted mean flux and different
  weights; they find both versions "work equally well" and give the first
  comparison of HLLI dissipation with Roe's (at most 23.2 % above it in
  the cases shown, zero for a stationary wave)
  ([Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §2;
  [HLLEM (HLLI)](/methods/hllem-riemann-solver.md)). Their 2D analogue is
  on the [multidimensional Riemann solvers](/methods/multidimensional-riemann-solvers.md) page.
* *Primary source of the solver-quality factors.* The 6 times and 3 times
  factors of the batch-7 bullet "Solver quality against order" come from
  [Balsara & Nkonga (2017)](/sources/balsara-2017-b.md) (§5.5, Fig. 7),
  with the same set-up ($120^2$, $t = 129$); the review repeats them. A
  relativistic MHD repeat gives the same ordering, without factors (§5.7).
* *Bearing on the HLLE contradiction below:* Deng, Boivin & Xiao's HLL
  runs are recorded in the entry as batch-11 evidence.

**Later uses (batch 12).**
* *Own pages.* The exact solver and HLLC now have pages with their
  formulas: [exact Riemann solver](/methods/exact-riemann-solver.md) and
  [HLLC Riemann solver](/methods/hllc-riemann-solver.md). The source is
  Toro's textbook, which runs every solver below through first-order
  Godunov on one set of 1D tests (100 cells, Courant number 0.9)
  ([Toro (1997)](/sources/toro-1997.md), Tables 4.1, 6.2).
* *Approximate-state solvers* (Ch. 9). They approximate $p_*$ and
  $v_{n*}$ in closed form and then use the exact wave relations.
  * PVRS linearizes the primitive-variable equations about arithmetic
    means (eqs. 9.19–9.21):
    $p_{\mathrm{PV}} = \tfrac12(p^- + p^+) - \tfrac18(v_n^+ - v_n^-)(\rho^- + \rho^+)(c^- + c^+)$,
    $v_{n*} = \tfrac12(v_n^- + v_n^+) + \dfrac{2(p^- - p^+)}{(\rho^- + \rho^+)(c^- + c^+)}$,
    $\rho_{*L} = \rho^- + (v_n^- - v_{n*})\dfrac{\rho^- + \rho^+}{c^- + c^+}$ and
    $\rho_{*R} = \rho^+ + (v_{n*} - v_n^+)\dfrac{\rho^- + \rho^+}{c^- + c^+}$.
    It is exact for an isolated contact or shear wave whatever the
    averages. A variant uses the acoustic impedances $\rho^\mp c^\mp$ at
    the feet of the characteristics (eq. 9.28).
  * TRRS is exact when both nonlinear waves are rarefactions, which
    $f^{\mathrm p}(\min(p^-, p^+)) \ge 0$ detects a priori (eq. 9.39).
    TSRS takes $p_{\mathrm{TS}}$ with $g^{\mathrm{TS}}_{L,R}$ evaluated at
    $\max(0, p_{\mathrm{PV}})$ (eq. 9.45; the initial guess of the exact
    solver floors at $\mathrm{TOL}$ instead, eq. 4.48) and
    $v_{n*} = \tfrac12(v_n^- + v_n^+) + \tfrac12\left[(p_* - p^+)g^{\mathrm{TS}}_R - (p_* - p^-)g^{\mathrm{TS}}_L\right]$
    (eqs. 9.42–9.45). Direct quadratic two-shock formulas are rejected:
    non-unique and complex roots "can occur very often" (p. 283).
  * The adaptive scheme uses PVRS when $\max(p^-, p^+)/\min(p^-, p^+) < Q_{\mathrm{user}}$
    and $p_{\mathrm{PV}}$ lies between $p^-$ and $p^+$, otherwise TRRS if
    $p_{\mathrm{PV}} \le \min(p^-, p^+)$ and TSRS if not (eqs.
    9.46–9.49). With $Q_{\mathrm{user}} = 2$, "over 90% of all Riemann
    problems are handled by the cheap linearised Riemann solver"
    (p. 285), and the non-iterative PVRS–TRRS–TSRS scheme "is
    recommended for practical applications" (p. 286). PVRS alone shows
    slight oscillations behind the right shock of the shock-collision
    test, a sign it "may not be robust enough" (p. 287).
* *Roe's flux, as printed* (Ch. 11, eqs. 11.27–11.29). With
  $\lambda^{(p)}$, $\ell^{(p)}$, $r^{(p)}$ at the Roe state and the wave
  strengths $\ell^{(p)}(u^+ - u^-)$,
  $$\hat f = f(u^-) + \sum_{\lambda^{(p)} \le 0}\lambda^{(p)}\,\ell^{(p)}(u^+ - u^-)\,r^{(p)} = f(u^+) - \sum_{\lambda^{(p)} \ge 0}\lambda^{(p)}\,\ell^{(p)}(u^+ - u^-)\,r^{(p)} = \tfrac12\left(f(u^-) + f(u^+)\right) - \tfrac12\sum_p\vert\lambda^{(p)}\vert\,\ell^{(p)}(u^+ - u^-)\,r^{(p)},$$
  so the Roe matrix itself is never formed. The Roe–Pike route computes
  the strengths directly from primitive jumps, e.g.
  $\frac{1}{2c_{\mathrm{Roe}}^2}\left[(p^+ - p^-) \mp \rho_{\mathrm{Roe}} c_{\mathrm{Roe}}\,(v_n^+ - v_n^-)\right]$ for the
  acoustic families and $(\rho^+ - \rho^-) - (p^+ - p^-)/c_{\mathrm{Roe}}^2$ for the
  entropy wave, with $\rho_{\mathrm{Roe}} = \sqrt{\rho^-\rho^+}$, $\sqrt\rho$-weighted
  velocities and enthalpy, and $c_{\mathrm{Roe}}$ from them; the averages are "identical
  to the Roe averages obtained by the original Roe method" (eqs. 11.113,
  11.118, p. 333).
* *Harten–Hyman entropy fix, as printed* (§11.4.2, eqs. 11.119–11.134).
  For the first family, if $v_n^- - c^- < 0 < v_{n*} - c_{*L}$ (a
  transonic left rarefaction), the Roe jump is split by an intermediate
  state and
  $$\hat f = f(u^-) + (v_n^- - c^-)\,\frac{(v_{n*} - c_{*L}) - \lambda^{(1)}}{(v_{n*} - c_{*L}) - (v_n^- - c^-)}\;\ell^{(1)}(u^+ - u^-)\,r^{(1)}.$$
  For the last family $m$, if $v_{n*} + c_{*R} < 0 < v_n^+ + c^+$,
  $$\hat f = f(u^+) - (v_n^+ + c^+)\,\frac{\lambda^{(m)} - (v_{n*} + c_{*R})}{(v_n^+ + c^+) - (v_{n*} + c_{*R})}\;\ell^{(m)}(u^+ - u^-)\,r^{(m)}.$$
  The star values come from the Roe intermediate states, from PVRS, TRRS
  or TSRS, or from the adaptive scheme ("even better", p. 339); PVRS and
  Roe-linearized star speeds "may fail in the vicinity of low density
  flow". On the modified Sod problem, Roe without the fix computes an
  entropy-violating jump inside the sonic rarefaction (Fig. 11.4; the
  glitch of the batch-7 bullet); with it the result is "almost
  indistinguishable" from exact Godunov (Fig. 11.5;
  [Sod shock tube](/benchmarks/sod-shock-tube.md)).
* *Roe fails at low density.* "The Roe method, as described, does
  actually fail" on the 123 problem, and Einfeldt et al.'s modification
  is needed (p. 340); Einfeldt et al. "showed that in fact this anomaly
  afflicts all linearised Riemann solvers" (p. 313;
  [double rarefaction](/benchmarks/double-rarefaction.md)).
* *Osher's solver: the ordering matters* (§12.3, eqs. 12.94–12.96).
  O-ordering (Osher's original) gives unrealistically large intersection
  pressures in strong rarefactions and fails on the 123 problem. Its
  intersection pressure is undefined, and the scheme fails, when
  $c^- + c^+ + \tfrac{\gamma-1}{2}(v_n^+ - v_n^-) \le 0$, which two
  colliding streams with strong shocks reach. P-ordering runs both but
  shows "spurious oscillations … near the shocks" of the colliding
  streams (p. 373). With O-ordering the slowly moving shock of the
  collision test has no post-shock oscillations, "a distinguishing
  property of the Osher approach" (§12.4;
  [slowly moving shock anomaly](/definitions/slowly-moving-shock-anomaly.md)).
* *Rusanov and Lax–Friedrichs are HLL cases* (eqs. 10.42–10.45). With
  $S_L = -S$, $S_R = S$ the HLL flux becomes
  $\tfrac12\left(f(u^-) + f(u^+)\right) - \tfrac12 S(u^+ - u^-)$; Davis's
  $S = \max(\vert v_n^- - c^-\vert, \vert v_n^+ - c^+\vert, \vert v_n^- + c^-\vert, \vert v_n^+ + c^+\vert)$
  gives Rusanov, and $S = h/\Delta t$ gives Lax–Friedrichs. First-order
  Lax–Friedrichs pairs odd and even cell values and spreads a shock over
  about 8 cells (§6.4.2).
* *Two formulas called "Einfeldt's".* The batch-8 bullet "Wave-speed
  estimates" quoted Xie et al.'s min/max form as Einfeldt's speeds
  without qualification (attributed to Xie et al. at the 2026-10-13 deep
  lint).
  Toro prints a different formula under Einfeldt's name, a mean velocity
  plus and minus a $\sqrt\rho$-weighted sound speed augmented by a
  velocity-jump term, and credits the plain Roe-average eigenvalues
  $v_n \mp c$ to "Davis and Einfeldt" (eqs. 10.39–10.48;
  [HLLC Riemann solver](/methods/hllc-riemann-solver.md) for both
  formulas). Both forms circulate under the name, so the batch-8 quote
  is one of them, not the only one. Toro's Davis min/max estimate
  (eq. 10.38) agrees with the batch-8 quote.
* *HLLC at low density*, against the bullet at the top: Toro finds that
  HLLC does not fail on the 123 problem but is less accurate in velocity
  and internal energy than the exact and approximate-state solvers
  (§10.8, Fig. 10.6), which fits both Titarev & Toro's statement that it works for low
  density and Guo et al.'s oscillations near vacuum.
* *HLL for a non-conservative two-fluid model*
  ([Yeom & Chang (2010)](/sources/yeom-2010.md), §3.2, eqs. 37–51). An
  eight-equation gas–droplet model with non-conservative
  interfacial-pressure terms. The face flux is HLL; the interface gas
  volume fraction that multiplies the non-conservative terms is weighted
  with the same coefficients, $S_R/(S_R - S_L)$ on the left value and
  $-S_L/(S_R - S_L)$ on the right, which suppresses "artificial source
  and sink" (after Saurel & Abgrall). The wave speeds are either the
  "simple" estimate, the minimum and maximum over both phases of
  $v_n \mp c$, or Nguyen et al.'s effective sound speeds of the mixture;
  Nguyen's is called more accurate and the simple one more robust;
  Nguyen's is used except for solid copper particles. Second order comes from Toro's
  weighted-average-flux (WAF) method in TVD form with the MINBEE limiter;
  the WAF chapter of the book was not read, so WAF has no page.

**Later uses (batch 14).** *Roe's solver at the source*
([Roe (1981)](/sources/roe-1981.md); no separate Roe page, by user
decision).
* *Linearized Riemann problem and Property U* (p. 359). Each Riemann
  problem is replaced by the exact solution of a linear problem with a
  constant matrix of $u^-$ and $u^+$, the Roe matrix, which must (i) map
  states linearly to fluxes, (ii) tend to $A(u)$ as $u^-$ and $u^+$ tend to
  $u$, (iii) map $u^- - u^+$ exactly to $f(u^-) - f(u^+)$ for any pair, and
  (iv) have linearly independent eigenvectors. The source prints four
  conditions, not three, and requires no real eigenvalues of the matrix
  itself. "Property U" stands for "uniform validity across
  discontinuities" (p. 360). Condition (iii) suffices for conservation;
  (iii) with (iv) is "necessary and sufficient" for the scheme to
  "recognize" a shock: if the flux jump is a shock speed times the state
  jump, that speed is an eigenvalue, the jump lies on one eigenvector, and
  the Riemann solution is exact (pp. 359–360). The Jacobian at the
  arithmetic-mean state, and the mean of the two Jacobians, fail (iii) in
  general (p. 359). *Compiler reading:* HLLEM is identical to Roe's solver
  when evaluated at the Roe state ([HLLEM (HLLI)](/methods/hllem-riemann-solver.md)),
  so an HLLEM evaluated at a mean state does not inherit (iii).
* *Construction* (pp. 361–363, eqs. 6–17). A valid matrix always exists
  as the Jacobian integrated along the straight path between the states,
  but has no closed form in general; building a rational one from the
  identities $[\![ab]\!] = \{\!\{a\}\!\}[\![b]\!] + \{\!\{b\}\!\}[\![a]\!]$
  and $[\![1/a]\!] = -[\![a]\!]/(a^-a^+)$ is "far from unique". For the
  Euler equations Roe instead uses the parameter vector
  $\sqrt\rho\,(1, v_x, v_y, v_z, (E+p)/\rho)^{\mathsf T}$: every component of
  $u$ and of the three fluxes is quadratic in it, so both the state jump
  and the flux jump are matrices linear in its arithmetic means times its
  jump, and the Roe matrix is their quotient. That a parameter vector
  "has so far worked each time that it has been tried" (p. 362) is a
  report of experience, not a theorem, consistent with Brio and Wu
  finding no Roe matrix for MHD at general $\gamma$
  ([characteristic decomposition](/methods/characteristic-decomposition.md)).
* *The averages* (pp. 364–365, eqs. 18–21). The eigenstructure is that of
  $A$ at $v_{x,\mathrm{Roe}} = (\sqrt{\rho^-}v_x^- + \sqrt{\rho^+}v_x^+)/(\sqrt{\rho^-} + \sqrt{\rho^+})$,
  likewise $v_y$, $v_z$ and the total specific enthalpy $(E+p)/\rho$, with
  $c_{\mathrm{Roe}}^2 = (\gamma-1)\left[\left((E+p)/\rho\right)_{\mathrm{Roe}} - \tfrac12\vert\mathbf v_{\mathrm{Roe}}\vert^2\right]$;
  the eigenvalues are $v_{x,\mathrm{Roe}} \mp c_{\mathrm{Roe}}$ and the
  triple $v_{x,\mathrm{Roe}}$, the eigenvectors and wave strengths are
  printed in closed form (eqs. 20, 22), and the eigenvector determinant,
  $2c_{\mathrm{Roe}}^3/(\gamma-1)$, is "never small unless the Mach number is
  very large". The 1981 paper prints **no averaged density**: the
  $\rho_{\mathrm{Roe}} = \sqrt{\rho^-\rho^+}$ of the batch-12 bullet
  "Roe's flux, as printed" comes from Toro's Roe–Pike route (and, for MHD
  at $\gamma = 2$, from Brio and Wu), and is not needed by Roe's
  eigenstructure.
* *The flux, as first printed* (p. 370). The first-order scheme splits
  $f(u^+) - f(u^-) = \sum_p\lambda^{(p)}\,\ell^{(p)}(u^+ - u^-)\,r^{(p)}$
  into its $\lambda^{(p)} < 0$ part, sent to the left cell, and its
  $\lambda^{(p)} > 0$ part, sent to the right. This is equivalent to the
  first two of Toro's three forms in the batch-12 bullet; the central form
  is not in the 1981 paper. The intended use is a "mechanism" (Roe's 7th
  ICNMFD paper) that carries any linear-advection scheme over to systems,
  reportedly with accuracy kept "at least to third order" (p. 359,
  unpublished results).
* *Entropy, in Roe's words* (pp. 359, 370–371). The approximation "suffers
  the theoretical disadvantage of not having a naturally constructed
  entropy condition". When a wave is in fact a fan spanning the interface,
  and in the extreme case of equal fluxes from unequal states, both parts
  vanish and nothing breaks up "the unrealistic discontinuity". The cure
  offered is empirical, an artificial equal and opposite contribution in
  each interval containing a sonic point, with no formula, no parameter and
  "a fuller theoretical justification" still to come; users "would be
  advised to employ either an empirical device … or some form of
  artificial viscosity". The sonic glitches of the batch-7 and batch-12
  bullets are this predicted defect; the Harten–Hyman fix quoted above is
  later work, not Roe's.
* *Cost against the exact solver* (pp. 368–370, Table I). On Sod's problem,
  35 steps at $\Delta t/h = 0.411$, first-order upwind through the
  approximate solver differs from Godunov with the exact solver by at most
  0.0003 in density, and takes 1.09 s against 2.02 s of CPU time
  ([Sod shock tube](/benchmarks/sod-shock-tube.md)). The approximate
  density fan is "not very close" to the exact one, but the areas under
  the two curves are identical (Fig. 1).
* *Multi-D caveat* (p. 360). Under operator splitting the solver works
  while shocks are grid-aligned; oblique shocks cause problems
  "particularly severe as the solution attempts to reach a steady state",
  since "neither of the split operators, by itself, recognizes the oblique
  shock as being in equilibrium". This is a steady-state convergence
  remark; the paper says nothing about the carbuncle or odd–even
  decoupling, which rest on the batch-8 sources above.

**Later uses (batch 16).** *The framework paper, the low-density paper
and Lax–Friedrichs at the source.*
* *Godunov-type and upstream schemes* ([Harten, Lax & van Leer (1983)](/sources/harten-1983-d.md),
  §§2–3). A scheme is *Godunov-type* when its approximate Riemann
  solution is consistent with the integral forms of the conservation law
  and of the entropy inequality (Theorem 3.1); such a scheme is
  conservative, satisfies a cell entropy inequality, and takes the
  upwind flux when all signal speeds have one sign. An *upstream* scheme
  is conservative, linearizes to Courant–Isaacson–Rees upwinding for
  nearby states, and takes the upwind flux when all signal speeds have one
  sign. The paper sorts the known solvers by their viscosity matrix
  $\Theta_{i+1/2}$: $\vert A\vert$ at the arithmetic mean, the mean of
  $\vert A(u^-)\vert$ and $\vert A(u^+)\vert$ (van Leer, which "somewhat
  smears stationary shocks but … excludes nonphysical discontinuities"),
  Huang's, Roe's, and Osher's path integral (eqs. 2.13–2.23).
* *Roe's entropy failure, the mechanism* (pp. 43, 49). At a stationary
  discontinuity $u^+ - u^-$ is a null vector of the Roe matrix, so the
  dissipation vanishes "whether or not the entropy condition … is
  satisfied"; this is the defect Roe predicted (batch-14 bullet "Entropy,
  in Roe's words"), and the fix cited is Harten & Hyman's. Any perfectly
  resolving conservative scheme can be corrected by subtracting from its
  flux a viscosity that vanishes on admissible shocks (p. 54).
* *A Roe-type matrix always exists when there is an entropy* (Theorem
  2.1, Harten–Lax). For any system with a convex entropy, a matrix with
  the exact jump property, real eigenvalues and a complete set of
  eigenvectors exists: the product of a symmetric matrix and a positive
  definite one, built in entropy variables, similar to a symmetric matrix.
  This is an existence result without a closed form; beside the
  batch-14 bullet "Construction" (Roe's straight-path Jacobian integral),
  it is a construction whose real eigenvalues and complete eigenvectors
  are proved.
* *Osher* (pp. 41–43, 49). Osher's limits satisfy the entropy condition;
  his scheme resolves a stationary contact exactly and needs at least one
  intermediate state for a stationary shock; it "is not of Godunov type in
  the sense of (3.9)", since its path is not a single-valued approximate
  Riemann solution.
* *A two-intermediate-state solver in 1983, not HLLC* (§3B(ii)). Two star
  states separated by a middle speed built from entropy variables, equal
  to the shock or contact speed whenever Rankine–Hugoniot holds, exact for
  an isolated shock or contact of any family, made entropy-satisfying by
  an added viscosity whose constants are not given. Its middle speed,
  star-state closure and viscosity all differ from HLLC's.
* *Flux-vector splitting* (§4(f)). Split fluxes cannot resolve stationary
  discontinuities exactly: van Leer's, like Osher's, gives a stationary
  shock "at best, one intermediate state", and "a contact discontinuity,
  however, will keep on spreading with the use of any split flux scheme".
  Background to the carbuncle entry below, not evidence on it.
* *Every linearization fails at low density* ([Einfeldt et al. (1991)](/sources/einfeldt-1991.md),
  §3, Propositions 3.1–3.2). On symmetric double-rarefaction data with a
  physical, vacuum-free exact solution, every linearized Riemann solution
  produces a negative density or internal energy once the Mach number
  exceeds $\sqrt{2/(\gamma(3-\gamma))}$ (0.94 at $\gamma = 1.4$); with
  shear, "in most cases the failure of linearizations is caused by a shear
  flow" (p. 281). This is Toro's "this anomaly afflicts all
  linearised Riemann solvers" (batch-12 bullet "Roe fails at low
  density"), with the scope of the proof: Jacobians at a symmetric
  average state with the ideal-gas relations (reader's reading). The
  cause, in the authors' words: Roe's signal speeds "underestimate the
  physical signal velocities" (§5).
* *Entropy fixes do not cure it* (§6, Fig. 6.1). On the 1–2–0–3 problem
  ($\rho = 1$, $v_x = \mp2$, $p = 0.4$ at $\gamma = 1.4$, reader's
  conversion) Roe's scheme "explodes after a few time-steps", Roe with the
  Harten–Hyman fix shows "unphysical oscillations", and Roe with Harten's
  1983 fix "also fails after a few time steps"; HLLE with bounding speeds
  runs ([double rarefaction](/benchmarks/double-rarefaction.md)). Toro's
  "Einfeldt et al.'s modification" is this choice of speeds in HLLE or
  HLLEM.
* *Two formulas called "Einfeldt's", partly settled.* The 1991 paper
  prints only the min/max form of the batch-8 bullet (eq. 4.5), a
  Lax–Friedrichs-type member (4.7) and a sharper positive set (4.10).
  Toro's $\bar c_{\mathrm E}$ formula is not in it; Einfeldt (1988), not
  ingested, remains a candidate ([HLL](/methods/hll-riemann-solver.md)).
* *Scope of the "HLL/HLLEM class"* (batch-6 and batch-8 bullets above).
  The 1991 paper proves positivity for HLLE (and Godunov's method), at
  first order for Euler; for HLLEM it asserts, without proof, freedom from
  the low-density failure, and runs its shear test with the shear
  anti-diffusion off. The HLLEM part of Balsara & Kim's attribution, which
  also cites Einfeldt (1988), is not supported by the 1991 paper
  ([HLLEM](/methods/hllem-riemann-solver.md)).
* *Lax–Friedrichs at the source* ([Lax (1954)](/sources/lax-1954.md),
  pp. 163, 177–180). Lax defines the scheme on a staggered lattice, each
  time level using every other point, consistent with the odd–even
  pairing of the batch-12 bullet. His runs show the shock width staying constant while a
  contact spreads like the square root of the number of cycles, and he
  argues that Eulerian contact spreading cannot be prevented without
  moving meshes.

**Later uses (batch 17).** *An Engquist–Osher flux for MHD.* The flux is the physical flux of the left state plus an alternating sum of physical fluxes at the sonic points of each wave's linearly interpolated speed, with eigenvectors frozen at the arithmetic mean of the primitive states. Any split of the flux has its own such flux, so part of it can be differenced as a gradient (eqs. 20–28). Where the fast speed at the mean state is below the jump of the entropy speed, it is replaced by HLLE with $S_R = \max(\lambda_R^+, \lambda_e^+, 0)$ and $S_L = \min(\lambda_L^-, \lambda_e^-, 0)$ (eqs. 29–30). At transonic degeneracies the correction of the two degenerate waves becomes Rusanov dissipation (eq. 33) ([Zachary, Malagoli & Colella (1994)](/sources/zachary-1994.md), §2.3).

## Contradictions

* **Is HLLE carbuncle-free?** *Open* (recorded at batch 8).
  * **For.** [Balsara (2004)](/sources/balsara-2004.md) (§§3.4, 6, 7.1)
    calls HLLE "carbuncle-free" (batch-6 bullet above). Simon & Mandal
    agree that HLL is free of shock instability because it dissipates the
    linear waves ([Simon & Mandal (2019)](/sources/simon-2019.md), §4.1;
    [Simon & Mandal (2019b)](/sources/simon-2019-b.md), §4). In shallow
    water the two-wave HLLS solver stays free of carbuncles where the
    complete augmented Roe solver does not ([Navas-Montilla & Murillo (2019)](/sources/navasmontilla-2019.md), §4.2.1).
  * **Against, Kitamura & Shima.** "Any flux functions including
    flux-vector-splitting (FVS) by Van Leer can generate carbuncles". They
    class the robust group as "almost (but not perfectly) free", citing
    earlier work; they do not run HLLE themselves
    ([Kitamura & Shima (2019)](/sources/kitamura-2019.md), §§I, II.B, III.E).
  * **Against, Xie et al.** On the [stationary normal shock](/benchmarks/stationary-normal-shock.md),
    HLLE with Einfeldt speeds is as unstable as HLLEM for sub-cell shock
    positions 0–0.3 (Table 1), the one-dimensional carbuncle
    ([Xie et al. (2021)](/sources/xie-2021.md), §3.1.2). Their 2D HLLE runs
    (a flat-plate boundary layer, and Elling's vortex filament through a
    Mach 20 shock) show HLLE smearing shear but no spurious carbuncle;
    HLLE is not run on their carbuncle tests (§§6.1–6.6).
  * **Batch 11 evidence, not closing.** [Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md),
    §§III F–H, run HLL with Davis's speeds at second order (MUSCL): no
    odd–even decoupling on a perturbed Mach 20 steady shock, no carbuncle
    in a 2D Sedov blast, no kinked stem in the double Mach reflection
    ("For" side, observed). Their §III F test is the 1.5D twin of Xie et
    al.'s (51×26 cells with a sub-cell intermediate column of
    perturbation weight 0.2 and 0.4, against 50×25 with a sub-cell intermediate
    state); the differences are Davis against Einfeldt speeds, MUSCL
    against first order, Mach 20, and a linear density mix rather than a
    state on the Hugoniot curve.
  * **Status.** Xie et al.'s own data fit a scoped reading: HLLE is
    unstable on the 1D steady shock yet shows no carbuncle in their 2D
    runs. No source states that reading as a claim, and Kitamura &
    Shima's claim is broader. Neither side's evidence uses a high-order
    reconstruction. (Corrected at the batch-8 deep lint: the first version
    said Xie et al. give no 2D HLLE run.)

# Citations

1. [Titarev & Toro (2004)](/sources/titarev-2004.md), §§2, 4, 5.
2. [Guo, Xiong & Shi (2014)](/sources/guo-2014.md), §§2.4, 3.
3. [Reyes et al. (2018)](/sources/reyes-2018.md), §5.
4. [Balsara, Bhoriya, Shu & Kumar (2025)](/sources/balsara-2025.md), §§I–II.
5. [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §3.
6. [Balsara et al. (2009)](/sources/balsara-2009.md), §§4.1, 7.2.
7. [Dumbser et al. (2013)](/sources/dumbser-2013.md), §2.1.
8. [Dumbser et al. (2014)](/sources/dumbser-2014.md), §2.3.
9. [Zanotti et al. (2015)](/sources/zanotti-2015.md), §3.2.
10. [Dumbser & Käser (2007)](/sources/dumbser-2007.md), §3.1.
11. [Balsara & Kim (2016)](/sources/balsara-2016-b.md), §§1, 4, Appendix B.
12. [Balsara et al. (2023)](/sources/balsara-2023.md), §§2.5, 3.4.
13. [Berta et al. (2024)](/sources/berta-2024.md), §§3.3, 5.4, Appendix B (arXiv v4).
14. [Balsara (2004)](/sources/balsara-2004.md), §§3.4, 6, 7.1.
15. [Ryu & Jones (1995)](/sources/ryu-1995.md), §§2.3, 3.
16. [Derigs et al. (2018)](/sources/derigs-2018.md), §§4.2–4.5, 5.7.
17. [Balsara (2017)](/sources/balsara-2017-d.md), §IX.5, Apps. D–E.
18. [Mignone & Tzeferacos (2010)](/sources/mignone-2010-b.md), §3.2.
19. [Dumbser & Balsara (2016)](/sources/dumbser-2016.md), abstract, §§2–4.
20. [Simon & Mandal (2019)](/sources/simon-2019.md), §§4–5, eq. 13.
21. [Simon & Mandal (2019b)](/sources/simon-2019-b.md), §§4–7.
22. [Xie et al. (2021)](/sources/xie-2021.md), eqs. 10–11, §§5–6.
23. [Navas-Montilla & Murillo (2019)](/sources/navasmontilla-2019.md), §§3, 4.2.1.
24. [Kitamura & Shima (2019)](/sources/kitamura-2019.md), §§II.B, III.E.
25. [Miczek et al. (2015)](/sources/miczek-2015.md), §§6–8.
26. [Edelmann et al. (2021)](/sources/edelmann-2021.md), §3.2.
27. [Brio & Wu (1988)](/sources/brio-1988.md), §§IV.1, V, VII.
28. [Dai & Woodward (1994)](/sources/dai-1994.md), §§4–6.
29. [Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md), §§II, III F–H.
30. [Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §§2, 5.5, 5.7.
31. [Toro (1997)](/sources/toro-1997.md), §§6.4.2, 9.3–9.5, 10.5, 10.8, 11.1–11.5, 12.3–12.4.
32. [Yeom & Chang (2010)](/sources/yeom-2010.md), §3.2.
33. [Roe (1981)](/sources/roe-1981.md), pp. 357–371, eqs. 5–22, Table I.
34. [Harten, Lax & van Leer (1983)](/sources/harten-1983-d.md), §§2–4, Theorems 2.1, 3.1.
35. [Einfeldt et al. (1991)](/sources/einfeldt-1991.md), §§3–6, Propositions 3.1–3.2.
36. [Lax (1954)](/sources/lax-1954.md), pp. 163, 177–180.
37. [Zachary, Malagoli & Colella (1994)](/sources/zachary-1994.md), §2.3, eqs. 20–33.
