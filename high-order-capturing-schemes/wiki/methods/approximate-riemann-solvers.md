---
type: Method
title: "Approximate Riemann solvers as building blocks of capturing schemes"
description: "The interface fluxes used by FV and alternative-FD WENO schemes in this corpus: Lax–Friedrichs/Rusanov, Roe, HLL and HLLC (with positivity-preserving wave speeds), HLLI/LLFI, the Riemann-solver-free MUSTA flux, and multidimensional HLL/LLF solvers for edge electric fields."
status: established
aliases: [Riemann solver, HLLC, HLL, MUSTA, FORCE, HLLI, Rusanov flux, HLL-BVD, Roe-type MHD solver]
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
  brittle. Positivity proofs exist only for first-order 1D HLL, HLLEM and
  HLLC, and none for a subluminal RMHD solver
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
  asserts, but does not prove, that HLLEM inherits the positivity of HLL.
* *Complete solvers and shock instability.* HLLC is HLL plus an
  anti-diffusive term, $\hat f^{\mathrm{HLL}} + S_L(u^{\mathrm{HLLC}}_{*L} - u^{\mathrm{HLL}}_*)$
  for $S_L \le 0 \le S_M$ ([Simon & Mandal (2019)](/sources/simon-2019.md), eq. 13). Solvers that resolve the
  contact and shear waves (Godunov, Roe, HLLC, HLLEM) are prone to the
  carbuncle, odd–even decoupling and kinked Mach stems at strong
  grid-aligned shocks ([Simon & Mandal (2019)](/sources/simon-2019.md); [Simon & Mandal (2019b)](/sources/simon-2019-b.md); [Xie et al. (2021)](/sources/xie-2021.md), §6;
  [numerical shock instability](/definitions/numerical-shock-instability.md), [cures for numerical shock instability](/methods/shock-instability-cures.md)).
* *Wave-speed estimates.* Einfeldt's are $S_L = \min(v_n^- - c^-,\ v_n - c)$
  and $S_R = \max(v_n^+ + c^+,\ v_n + c)$, the second argument at the Roe
  state; they give the exact speed of an isolated shock. Davis's are
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
  For $\gamma = 2$ an exact Roe matrix is the Jacobian at an averaged
  state: Roe-averaged velocities and total enthalpy, the geometric-mean
  density, and a $\sqrt\rho$-weighted tangential field (eqs. 26, 28–30).
  For general $\gamma$ the authors could not solve the averaging problem
  ("we are not able to solve it analytically") and use the Jacobian at
  the arithmetic mean of density, velocity, field and total pressure.
  That state keeps the eigenvalues real but does not satisfy
  $f(u_{i+1}) - f(u_i) = A\,(u_{i+1} - u_i)$, so stationary
  discontinuities are no longer exact steady solutions; averaging the
  energy instead "may lead to a negative averaged pressure". On the
  [Brio–Wu shock tube](/benchmarks/brio-wu-shock-tube.md) the two
  versions agree to 4 significant digits in the constant states and to 2
  in the transitions. The second-order scheme costs about 10 times the
  floating-point operations of Lax–Wendroff per point and step, yet with
  200 points it gives "a reasonable result" where Lax–Wendroff needs 800,
  and is then the more efficient. Its renormalized eigenvectors are on
  the [characteristic decomposition](/methods/characteristic-decomposition.md) page.
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
    al.'s (51×26 cells with a sub-cell intermediate column at
    $\lambda = 0.2$, 0.4, against 50×25 with a sub-cell intermediate
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
