---
type: Property
title: "Positivity preservation (invariance of the admissible set)"
description: "A scheme is positivity-preserving if cell averages (or point values) that lie in the admissible set — positive density and pressure — stay there after a step; the high-order route rests on convexity of the set, a positive first-order building block, and SSP time stepping."
status: established
aliases: [positivity-preserving, physical-constraint-preserving, PCP, invariant-domain preserving]
tags: [positivity, euler, mhd, admissible-set]
timestamp: 2026-10-13T00:00:00Z
---

# Positivity preservation

**Definition.** For the Euler equations the admissible set is
$\mathcal{G} = \{u : \rho > 0,\ p = (\gamma-1)(E - \tfrac12\rho\vert\mathbf v\vert^2) > 0\}$. A scheme is positivity-preserving if
$\bar u^n_i \in \mathcal{G}$ for all $i$ implies $\bar u^{n+1}_i \in \mathcal{G}$
([Zhang & Shu (2010)](/sources/zhang-2010.md), §1). The same idea for
general bounds (density, pressure, sub-luminal speed, positive
definite pressure tensors) is called *physical constraint
preservation* (PCP) ([Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §5).
Losing it makes the system non-hyperbolic: the Jacobian's eigenvalues
turn complex, the linearized problem is ill-posed and the code blows
up; replacing negative values by positive ones is neither conservative
nor stable ([Zhang & Shu (2012)](/sources/zhang-2012.md), §1).
Positivity fails in blast waves (low density), high-Mach flows whose
energy is mostly kinetic (low pressure), and also far from vacuum, from
interpolation errors at very strong discontinuities
([Hu, Adams & Shu (2013)](/sources/hu-2013.md), §1).

**The three ingredients** shared by every high-order construction in
this corpus:

1. **Convexity.** $p(u)$ is concave where $\rho > 0$, so by Jensen's
   inequality $\mathcal{G}$ is convex
   ([Zhang & Shu (2010)](/sources/zhang-2010.md), eq. 1.3). For a general
   equation of state with $e > 0 \Leftrightarrow p > 0$ at $\rho \ge 0$,
   the internal energy $\rho e$ is concave and $\mathcal{G}$ stays convex
   ([Zhang & Shu (2012)](/sources/zhang-2012.md), §4.3).
2. **A positive first-order scheme.** The first-order scheme
   $\bar u^{n+1}_i = \bar u^n_i - \frac{\Delta t}{h}\left(\hat f(\bar u_i,\bar u_{i+1}) - \hat f(\bar u_{i-1},\bar u_i)\right)$
   keeps $\mathcal{G}$ under $\nu \le \nu_0$ for the Godunov,
   Lax–Friedrichs, Boltzmann-type and HLL fluxes. For Lax–Friedrichs
   Perthame and Shu proved $\nu_0 = \tfrac12$; Zhang and Shu relax it to
   $\nu_0 = 1$ by writing the update as a convex combination of
   $u$ and $u \pm f(u)/\alpha$, both in $\mathcal{G}$
   ([Zhang & Shu (2010)](/sources/zhang-2010.md), Remark 2.4). HLLC with
   the wave speeds of Batten et al. is positivity-preserving under
   $\nu \le 1$ ([Guo, Xiong & Shi (2014)](/sources/guo-2014.md), §2.4, Remark 1;
   [approximate Riemann solvers](/methods/approximate-riemann-solvers.md)).
3. **SSP time stepping.** An SSP method is a convex combination of
   forward-Euler steps, so positivity of forward Euler carries over
   ([SSP Runge–Kutta](/methods/ssp-runge-kutta.md)); the limiter must be
   applied at every stage.

**The sufficient condition at high order.** A high-order FV or DG
update of cell averages is a convex combination of first-order-type
updates and of interior point values of $\mathcal{P}_i$ at the
Gauss–Lobatto points. Hence $\bar u^{n+1}_i \in \mathcal{G}$ if
$\mathcal{P}_i(\hat x^{(a)}_i) \in \mathcal{G}$ for all $a$ and
$\nu \le \hat w_1\,\nu_0$ ([Zhang & Shu (2010)](/sources/zhang-2010.md),
Theorem 2.1). Two families enforce it: the
[scaling limiter](/methods/positivity-preserving-scaling-limiter.md),
which rescales $\mathcal{P}_i$ about its mean, and the
[flux limiter](/methods/positivity-preserving-flux-limiter.md), which
blends the high-order flux towards a first-order one.

**Accuracy.** Both families are proved not to degrade the order for
smooth solutions bounded away from vacuum: the modification is
$O(h^{K+1})$ ([Zhang & Shu (2010)](/sources/zhang-2010.md), §2.2;
[Hu, Adams & Shu (2013)](/sources/hu-2013.md), §2.3). The proofs need
$\rho$ and $p$ bounded below by a positive constant; near vacuum there is no accuracy claim.
A conservative positivity-preserving scheme is $L^1$-stable
([Zhang & Shu (2012)](/sources/zhang-2012.md), §1).

## MHD

The ingredients carry over except the second one, whose status the
sources state differently (see Contradictions). Christlieb et al.
assume positivity of the first-order Lax–Friedrichs update and accept
a loss of energy conservation where their limiter acts, from the
pressure-preserving energy correction after the constrained-transport
field update ([Christlieb et al. (2016)](/sources/christlieb-2016.md), §§2, 5).
Balsara et al. keep the face-centred field as primal variable; the
first-order scheme can lose PCP in rare cells when face fields are
averaged to cell centres, which they cure first by a conservative
borrowing of thermal energy from neighbours and, failing that, by a
non-conservative energy source
([Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §5.1;
[constrained transport](/methods/constrained-transport.md)).

**A posteriori enforcement (batch 4).** Instead of limiting the
high-order solution to stay in $\mathcal{G}$, MOOD-type schemes check
the candidate solution after the step, physical admissibility first
(e.g. $\rho, p > 0$). Failed cells are recomputed from $t^n$ with a more
robust scheme. For DG this is third-order ADER-WENO on subcells, and
the last resort is a first-order Godunov update "supposed" positive
under its CFL condition ([a posteriori subcell limiting](/methods/a-posteriori-subcell-limiting.md);
[Dumbser et al. (2014)](/sources/dumbser-2014.md), §4.3). The subcell WENO scheme itself may fail positivity for
very complex systems. The proposed remedies are a further MOOD layer or
Balsara's self-adjusting positivity method ([Dumbser et al. (2014)](/sources/dumbser-2014.md), §6).

**MHD, divergence-free reconstruction.** In low-β blast waves (ambient
plasma beta $2.5\times10^{-4}$), fourth-order ADER-WENO keeps the
pressure positive where the strong shock runs oblique to the mesh. The
authors attribute this directly to computing the zone-centred field
from the divergence-free reconstruction ([Balsara et al. (2009)](/sources/balsara-2009.md), §§7.4–7.5;
[constrained transport](/methods/constrained-transport.md)). This is
consistent with the later observation that *simple averaging* of face
fields to cell centres is what costs PCP in rare cells
(Balsara, Bhoriya & Shu above).

**Later uses (batch 6).**
* *Earliest form of the claim.* The same attribution is made at second
  order, ambient plasma beta $2.51\times10^{-4}$. The author claims only
  that the reconstruction "helps overcome some of the problems" and that
  corrective fixes may still be needed at extremely low beta
  ([Balsara (2004)](/sources/balsara-2004.md), §§3.2, 7.3, Conclusion 5;
  [divergence-free reconstruction](/methods/divergence-free-reconstruction.md)).
  The RK-WENO sibling of the ADER paper repeats it at fourth order. No
  paper shows a run without the reconstruction, so the causal claim is
  asserted, not demonstrated ([Balsara (2009b)](/sources/balsara-2009-b.md), §5.3).
* *A provable high-order route.* Ding and Wu prove positivity of the cell
  averages of a finite-volume WENO scheme for MHD, for orders 2 and above,
  under $\Delta t\,(\alpha_x/h_x + \alpha_y/h_y) < \hat w_1$
  (Thm. 2.1, eq. 15). Three ingredients are required.
  * Interface traces that are discretely divergence-free, obtained by a
    projection ([constrained transport](/methods/constrained-transport.md)).
  * An interface discretization of the Godunov–Powell source term.
  * A Zhang–Shu-type scaling of the point values and of one interior
    remainder state. The second step scales the whole state by a ratio,
    using concavity of the internal energy, instead of a quadratic solve
    ([scaling limiter](/methods/positivity-preserving-scaling-limiter.md)).

  The Lax–Friedrichs speeds are enlarged by a term in the jump of the
  normal field. The divergence coupling defeats the usual convex
  decomposition into first-order updates, so the proof uses geometric
  quasilinearization instead. Without the projection or the limiter the
  fifth-order scheme fails on the Orszag–Tang vortex, the blast and the
  magnetized jet ([Ding & Wu (2024)](/sources/ding-2024.md), §§1–4; arXiv v1).
* *Relativistic MHD.* The admissible set adds $|\mathbf v| < 1$.
  Reconstructing the four-velocity guarantees it by construction, but no
  multi-D high-order RMHD corrector guarantees it, and positivity proofs
  exist only for first-order 1D HLL-type solvers
  ([Balsara & Kim (2016)](/sources/balsara-2016-b.md), §§1–2).
* *No limiter at all.* A fifth-order FD-WENO code with high-order CT runs
  the rotor and a 3D blast (ambient beta about 0.02 by the compiler's
  arithmetic) without any positivity treatment
  ([Seo & Ryu (2023)](/sources/seo-2023.md), §§3.6–3.7).

**In the reviews (batch 6).** WENO is usually robust without an extra
limiter, but negative pressure appears in high-speed flows, where the
internal energy is a small difference of large numbers. This is more
likely at higher order, which has less dissipation. For Mach 2000 jets a
third-order WENO scheme "was used successfully" and a fifth-order one
"would fail" (Ha et al., as cited by [Shu (2020)](/sources/shu-2020.md), §9). Shu calls the Zhang–Shu
limiter "very simple and local", most convenient for FV and extended to FD
"under stronger assumptions" ([high-Mach jet](/benchmarks/high-mach-astrophysical-jet.md)).

**Later uses (batch 7).**
* *Viscous flows.* For compressible Navier–Stokes, treating
  $\mathbf f - \mathbf f^{\mathrm v}$ as one flux lets the three ingredients
  carry over unchanged. The first-order building block is a
  Lax–Friedrichs-type viscous flux, the central flux plus
  $\tfrac12\beta^{\mathrm v}_{i+1/2}(u^+ - u^-)$, admissible for
  $\beta^{\mathrm v} > \frac{1}{2\rho^2 e}\left(\sqrt{\rho^2 q_n^2 + 2\rho^2 e\,|\boldsymbol\tau\mathbf n|^2} + \rho|q_n|\right)$,
  $q_n = \mathbf q\cdot\mathbf n$, for any equation of state and any stress
  and heat-flux law ([Zhang (2017)](/sources/zhang-2017.md), §1.5, Lemma 6). Weak-positivity
  theorems hold for FV and DG on rectangles and triangles (Theorems 1–3).
  Two caveats from the same paper: the positivity bound allows
  $\Delta t = O(h)$ for smooth viscous flow while linear stability needs
  $O(\mathrm{Re}\,h^2)$, so errors can grow exponentially with positivity and
  $L^1$ stability intact (Remark 2); and the single-ratio internal-energy
  limiter is "crude", at least second-order inaccurate where the solution
  touches the floor (§4.2;
  [scaling limiter](/methods/positivity-preserving-scaling-limiter.md)).
* *MHD energy accounting.* Without the non-conservative energy term,
  magnetic-energy errors from $\nabla\cdot\mathbf B \ne 0$ are booked as
  internal-energy loss, and "the pressure could easily become negative"
  ([Derigs et al. (2018)](/sources/derigs-2018.md), §2, an argument with no test). Plain GLM omits the
  energy of the cleaning field; on a low-β Alfvén wave its thermal-energy
  error, and CT's with face-averaged cell fields, reach about 30%, while
  EGLM's does not ([Tomida et al. (2026)](/sources/tomida-2026.md), App. B;
  [hyperbolic divergence cleaning](/methods/hyperbolic-divergence-cleaning.md)).
* *Balsara's self-adjusting method*, described in full: a flattener
  narrows extended neighbour bounds at strong shocks, density is rescaled
  Barth-style, and a common factor for all variables comes from a per-node
  quadratic in pressure. It is "designed to save a code from a rare code
  crash", claims no CFL theorem, and does not cure Toro's
  tangential-velocity anomaly. With it a 3D MHD blast at plasma beta
  $1.117\times10^{-4}$ stays positive ([Balsara (2017)](/sources/balsara-2017-d.md), §§VII, IX.4).

**Later uses (batch 9).**
* *Positivity at the end of the step.* Instead of limiting every stage,
  the Runge–Kutta weights can be re-chosen after the stages by a linear
  program that makes $u^{n+1} \ge 0$ and keeps the order conditions up
  to some order. Stages may go negative, the bounds must be linear in
  the weights, and every linear invariant is kept, whereas clipping
  negative values breaks mass conservation ([Nüßlein, Ranocha & Ketcheson (2021)](/sources/nusslein-2021.md); [positivity-preserving adaptive Runge–Kutta](/methods/positivity-preserving-adaptive-runge-kutta.md)).
* *Reject and retry.* Error-controlled DG runs with no limiter reject a
  step that produces negative density or pressure and retry it with
  $\Delta t/4$ ([Ranocha et al. (2022)](/sources/ranocha-2022.md), §2.2); the restart of Zhang (2017) above
  halves the step.
* *Relaxation and limiters.* How a relaxation step, which rescales the
  update by $\gamma^n_{\mathrm R}$, combines with positivity limiters is
  left open ([Ranocha et al. (2020)](/sources/ranocha-2020.md), Conclusions; [relaxation Runge–Kutta](/methods/relaxation-runge-kutta.md)).
* *Why multistep.* SSP multistep methods are recommended with the
  limiter because Runge–Kutta methods with the limiter "can lead to
  order reduction" ([Hadjimichael et al. (2016)](/sources/hadjimichael-2016.md), §1). This is a different reason from
  the unknown stage wave speeds of Zhang & Shu's Remark 2.7; both are
  recorded on [SSP linear multistep methods](/methods/ssp-linear-multistep.md).

**Later uses (batch 10): cut cells and immersed boundaries.**
* Flux redistribution produced mass fractions below 0 and above 1 in a
  reacting 3D run where state redistribution did not
  ([Giuliani et al. (2022)](/sources/giuliani-2022.md), §6.1). State redistribution itself is not monotone and
  its positivity is asserted only qualitatively ([Berger & Giuliani (2021)](/sources/berger-2021.md), §§2–3;
  [state redistribution](/methods/state-redistribution.md)).
* Re-redistribution at an AMR interface gives negative energy and
  pressure when a coarse cut cell there is below a volume fraction of about
  $10^{-4}$ ([Barrio Sanchez et al. (2024)](/sources/barriosanchez-2024.md), §4.1).
* Quadratic interpolation to ghost-cell image points gives negative
  density and pressure behind shocks; the fix was to drop to
  inverse-distance weighting ([Seshadri & De (2020)](/sources/seshadri-2020.md), §4.6; [immersed-boundary methods](/methods/immersed-boundary-method.md)).

**Later uses (batch 16): the first-order building block at its source.**
* *"Positively conservative"* ([Einfeldt et al. (1991)](/sources/einfeldt-1991.md),
  §§1–2, eq. 2.4) is this page's property for first-order Euler schemes:
  density and internal energy "remain positive throughout the
  computational process", with the same admissible set $\mathcal G$.
* *Godunov and HLLE, proved there* (§§2, 4). Both updates are convex
  averages of the states of interface Riemann solutions, exact for
  Godunov and the HLL star state for HLLE, so they stay in the convex
  $\mathcal G$ provided the exact interface solutions contain no vacuum
  and, for HLLE, the wave speeds bound the physical ones (eq. 4.5; the
  bounding property is asserted, not proved). Convexity of $\mathcal G$ is
  stated there, not proved (ingredient 1 above proves it), and no
  time-step condition is stated with the proofs; the runs use
  $\Delta t\max_i(\vert v_{x,i}\vert + c_i)/h \le \tfrac12$. A sharper speed
  choice is proved positive by direct algebra on the star state (eqs.
  4.9–4.10, App.; [HLL](/methods/hll-riemann-solver.md)). This is the
  primary support for the Godunov and HLL entries of ingredient 2; HLLEM
  with nonzero anti-diffusion is only asserted to share it
  ([HLLEM](/methods/hllem-riemann-solver.md)).
* *Linearized solvers cannot be positive* (§3, Propositions 3.1–3.2). For
  symmetric double-rarefaction data, with or without shear, there are
  problems whose exact solution is physical and vacuum-free while every
  linearization yields a negative density or internal energy; at
  $\gamma = 1.4$ the 1D failure starts at Mach number 0.94. The proof
  covers Jacobians at a symmetric average state consistent with the
  ideal-gas relations (reader's reading of eqs. 3.10–3.11). For Roe-type
  solvers this sharpens Balsara & Kim's statement that no positivity
  proof exists for Roe- or Osher-type solvers (batch-6 bullet
  "Relativistic MHD" of the Riemann-solver page) to "positivity is
  impossible" within that scope; Osher-type solvers are not covered
  ([double rarefaction](/benchmarks/double-rarefaction.md);
  [approximate Riemann solvers](/methods/approximate-riemann-solvers.md)).
* *Not in Harten, Lax & van Leer.* That paper only cautions that a scheme
  must keep density and pressure positive (p. 38) and proves no positivity
  ([Harten, Lax & van Leer (1983)](/sources/harten-1983-d.md)).
* *Lax (1954)* proves no positivity for gas dynamics; on one of his Euler
  shock tubes the mesh ratio exceeds the CFL limit in the star state and
  an instability "is indeed beginning to show around the shock front"
  ([Lax (1954)](/sources/lax-1954.md), Ex. 7).

## Contradictions

**Does positivity limiting inside Runge–Kutta stages reduce the order?**
*Open* (recorded at the 2026-10-12 deep lint).
* [Zhang & Shu (2010)](/sources/zhang-2010.md), §2.2, and
  [Hu, Adams & Shu (2013)](/sources/hu-2013.md), §2.3: the limiter's
  modification is $O(h^{K+1})$ for smooth solutions bounded away from
  vacuum, so the order is not degraded.
* *For, by test (added at the 2026-10-13 deep lint).*
  [Zhang & Shu (2012)](/sources/zhang-2012.md), §5, Example 5.1,
  Table 5.1: fifth-order FD WENO with the limiter applied at every stage
  of third-order SSP Runge–Kutta (Remark 3.3) shows fifth order in $L^1$
  on the near-vacuum isentropic vortex (lowest density about
  $7.8 \times 10^{-15}$), refined to $h = 1/64$. The test takes
  $\Delta t = h^{5/3}$ so that the spatial error dominates, and runs to
  $t = 0.01$ only; it does not probe a time-step-dominated regime.
* [Hadjimichael et al. (2016)](/sources/hadjimichael-2016.md), §1: "Use of
  Runge–Kutta methods in conjunction with the limiter can lead to order
  reduction, so linear multistep methods are recommended", citing
  Gottlieb, Ketcheson & Shu (2011) and Zhang & Shu's maximum-principle
  paper, neither ingested; the paper shows no test of it. The
  "Against" side is thus a single secondhand remark without a test in
  the corpus, while the "For" side has two proofs and one convergence
  table.
* The scopes may differ: the proofs bound the per-stage spatial
  modification, while the order-reduction remark concerns the full
  Runge–Kutta step. Ingesting the cited sources, or a convergence test of
  a limited Runge–Kutta step, would settle it.

**Is the first-order Lax–Friedrichs MHD scheme provably positive?**
*Open.*
* [Christlieb et al. (2016)](/sources/christlieb-2016.md), §5, Claim 1:
  for 2D ideal MHD with the global Lax–Friedrichs flux, positivity of
  density and pressure under CFL $\le 0.5$ was *conjectured* by Cheng
  et al. and verified only on many random states, "though not proven";
  their limiter assumes it.
* [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §5.1: a
  first-order zone-centred MHD scheme with HLL or LLF facial fluxes "will
  indeed be PCP, as was first proved by Gurski".
* The scopes may differ (Christlieb: 2D unsplit update with density and pressure
  floors $\epsilon_{\mathcal{G}}$ and a stated CFL; Balsara: no dimension or
  CFL stated). Neither source cites the other's reference on this
  point, and the cited proof (Gurski 2004) is not in the corpus.
  Ingesting it, or a later analysis, would settle the claim.
* *Batch 6 evidence, still not decisive.* [Ding & Wu (2024)](/sources/ding-2024.md),
  §1, report that the Lax–Friedrichs positivity Christlieb et al. assume
  was "later proven rigorously" by Wu (2018). They also report that Cheng
  et al. proved it only in 1D, under assumptions on exact Riemann
  solutions, and only conjectured it in multi-D, as Christlieb et al.
  say. Citing Wu (2018), they add that for the standard MHD system
  positivity of FV and DG schemes is tied to a discrete divergence-free
  condition and can fail if it is violated "even slightly". On that report
  the multi-D statement is conditional, which would explain both the
  "proved" and the "conjectured" claims. This is a secondhand account:
  neither Wu (2018) nor Gurski (2004) is in the corpus, and the entry stays
  open. Wu (2018) is the decisive ingestion target.

# Citations

1. [Zhang & Shu (2010)](/sources/zhang-2010.md), §§1–2.
2. [Zhang & Shu (2012)](/sources/zhang-2012.md), §§1–5 (Example 5.1, Table 5.1).
3. [Hu, Adams & Shu (2013)](/sources/hu-2013.md), §§1–2.
4. [Guo, Xiong & Shi (2014)](/sources/guo-2014.md), §2.4.
5. [Christlieb et al. (2016)](/sources/christlieb-2016.md), §§1, 2, 5.
6. [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §5.
7. [Dumbser et al. (2014)](/sources/dumbser-2014.md), §§4.3, 6.
8. [Balsara et al. (2009)](/sources/balsara-2009.md), §§7.4–7.5.
9. [Balsara (2004)](/sources/balsara-2004.md), §§3.2, 7.3.
10. [Balsara (2009b)](/sources/balsara-2009-b.md), §5.3 (author manuscript).
11. [Ding & Wu (2024)](/sources/ding-2024.md), §§1–4 (arXiv v1).
12. [Balsara & Kim (2016)](/sources/balsara-2016-b.md), §§1–2.
13. [Seo & Ryu (2023)](/sources/seo-2023.md), §§3.6–3.7.
14. [Shu (2020)](/sources/shu-2020.md), §9.
15. [Zhang (2017)](/sources/zhang-2017.md), §§1.5, 4.2, Lemma 6, Theorems 1–3.
16. [Derigs et al. (2018)](/sources/derigs-2018.md), §2.
17. [Tomida et al. (2026)](/sources/tomida-2026.md), App. B.
18. [Balsara (2017)](/sources/balsara-2017-d.md), §§VII, IX.4.
19. [Nüßlein, Ranocha & Ketcheson (2021)](/sources/nusslein-2021.md), §§1–5 (arXiv v2).
20. [Ranocha et al. (2022)](/sources/ranocha-2022.md), §2.2.
21. [Ranocha et al. (2020)](/sources/ranocha-2020.md), Conclusions (arXiv v4).
22. [Hadjimichael et al. (2016)](/sources/hadjimichael-2016.md), §1 (arXiv v2).
23. [Giuliani et al. (2022)](/sources/giuliani-2022.md), §6.1 (arXiv v2).
24. [Berger & Giuliani (2021)](/sources/berger-2021.md), §§2–3 (arXiv v1).
25. [Barrio Sanchez et al. (2024)](/sources/barriosanchez-2024.md), §4.1 (arXiv v1).
26. [Seshadri & De (2020)](/sources/seshadri-2020.md), §4.6 (author manuscript).
27. [Einfeldt et al. (1991)](/sources/einfeldt-1991.md), §§1–4, 6, eqs. 2.4, 4.5–4.10, App.
28. [Harten, Lax & van Leer (1983)](/sources/harten-1983-d.md), §1, p. 38.
29. [Lax (1954)](/sources/lax-1954.md), Ex. 7.
