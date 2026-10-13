---
type: Method
title: "HLL Riemann solver and wave-speed estimates"
description: "Harten, Lax and van Leer's two-wave approximate Riemann solver: one constant star state between the speeds S_L and S_R, its flux in three-branch, clipped and central (dissipation) forms, the wave-speed estimates that complete it (Davis, Roe-average, the two forms called Einfeldt's, pressure-based), Rusanov and Lax–Friedrichs as its symmetric special cases, its contact and shear diffusion, what is and is not proved about its positivity, its robustness at strong shocks, and HLL-BVD."
status: established
aliases: [HLL, HLLE, HLL flux, Harten–Lax–van Leer solver, two-wave Riemann solver, Davis wave speeds, Einfeldt wave speeds]
tags: [riemann-solver, numerical-flux, positivity, shock-instability, contact-discontinuity]
timestamp: 2026-10-13T00:00:00Z
---

# HLL Riemann solver and wave-speed estimates

Harten, Lax and van Leer obtain the interface flux directly from an
assumed wave pattern: two waves of speeds $S_L \le S_R$ separating three
constant states. Given $S_L$ and $S_R$, the integral form of the
conservation law fixes the flux in closed form. The solver became
practical once Davis and Einfeldt supplied ways to compute the speeds
([Toro (1997)](/sources/toro-1997.md), Ch. 10 introduction, §10.3). The
overview of all interface fluxes used in this bundle is the
[approximate Riemann solvers](/methods/approximate-riemann-solvers.md) page;
the three-wave extension is the [HLLC Riemann solver](/methods/hllc-riemann-solver.md).

## The two-wave model and its flux

The star state is the integral average of the Riemann fan between $S_L$
and $S_R$,
$$u^{\mathrm{HLL}}_* = \frac{S_R u^+ - S_L u^- + f(u^-) - f(u^+)}{S_R - S_L},$$
and the flux follows from the Rankine–Hugoniot conditions across either
wave, $f(u^-) + S_L(u^{\mathrm{HLL}}_* - u^-) = f(u^+) + S_R(u^{\mathrm{HLL}}_* - u^+)$,
not from $f(u^{\mathrm{HLL}}_*)$
([Toro (1997)](/sources/toro-1997.md), §§10.2–10.3, eqs. 10.13, 10.17–10.21):
$$\hat f^{\mathrm{HLL}} = \begin{cases} f(u^-), & 0 \le S_L,\\ \dfrac{S_R f(u^-) - S_L f(u^+) + S_L S_R (u^+ - u^-)}{S_R - S_L}, & S_L \le 0 \le S_R,\\ f(u^+), & 0 \ge S_R.\end{cases}$$
Two equivalent one-line forms circulate in the shock-instability papers:
* *Clipped speeds.* With $S_L^- = \min(S_L, 0)$ and $S_R^+ = \max(S_R, 0)$
  the middle formula covers all three branches
  ([Xie et al. (2021)](/sources/xie-2021.md), eq. 12;
  [Dumbser & Balsara (2016)](/sources/dumbser-2016.md), eq. 5).
* *Central flux plus dissipation.* $\hat f^{\mathrm{HLL}} = \tfrac12\left(f(u^-) + f(u^+)\right) + \mathbf d^{\mathrm{HLL}}$,
  where on the subsonic branch
  $$\mathbf d^{\mathrm{HLL}} = \frac{S_R + S_L}{2(S_R - S_L)}\left(f(u^-) - f(u^+)\right) - \frac{S_L S_R}{S_R - S_L}\left(u^- - u^+\right)$$
  ([Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md), eqs. 7–11).
  Simon & Mandal write the coefficients as
  $(\vert S_R\vert - \vert S_L\vert)/(2(S_R - S_L))$ on the flux jump and
  $(\vert S_L\vert S_R - \vert S_R\vert S_L)/(2(S_R - S_L))$ on the state
  jump, which holds on every branch; their shock-instability cure edits only
  these numerators ([Simon & Mandal (2019)](/sources/simon-2019.md), eqs. 14–15, 17–18).

The two-wave model is exact only for $2\times2$ systems (one-dimensional
shallow water). For the Euler equations it lumps the contact and shear
waves into the single star state ([Toro (1997)](/sources/toro-1997.md), p. 293).

**Convergence and entropy, as reported.** Harten, Lax and van Leer showed
that the Godunov-type scheme with this flux, if it converges, converges to
a weak solution, and proved that the limit is the entropy solution; the
result covers any approximate solver consistent with the integral form of
the conservation laws ([Toro (1997)](/sources/toro-1997.md), §10.3, p. 298).
Xie et al. likewise list HLLE among the Godunov-type schemes that satisfy a
discrete entropy condition ([Xie et al. (2021)](/sources/xie-2021.md), §1).
Both are secondhand: the 1983 paper is not in the corpus.

## Wave-speed estimates

The flux is determined only once $S_L$ and $S_R$ are; the estimates are
meant as bounds on the slowest and fastest signal speeds of the Riemann
problem ([Toro (1997)](/sources/toro-1997.md), §10.5). As printed:
* **Davis, direct** (eqs. 10.37–10.38): $S_L = v_n^- - c^-$,
  $S_R = v_n^+ + c^+$; or the data-only min/max
  $S_L = \min(v_n^- - c^-,\ v_n^+ - c^+)$, $S_R = \max(v_n^- + c^-,\ v_n^+ + c^+)$.
  Xie et al. call the min/max form "simpler and more diffusive" than
  Einfeldt's and useful against post-shock oscillations
  ([Xie et al. (2021)](/sources/xie-2021.md), eq. 11, §5); Deng, Boivin & Xiao
  use it throughout ([Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md), eq. 9).
* **Roe-average eigenvalues**, credited by Toro to both Davis and Einfeldt
  (eqs. 10.39–10.41): $S_L = v_{n,\mathrm{Roe}} - c_{\mathrm{Roe}}$,
  $S_R = v_{n,\mathrm{Roe}} + c_{\mathrm{Roe}}$, with $\sqrt\rho$-weighted
  velocity and total enthalpy. With these speeds HLLEM becomes identical
  to Roe's scheme ([Xie et al. (2021)](/sources/xie-2021.md), §3.3.1;
  [HLLEM](/methods/hllem-riemann-solver.md)).
* **Einfeldt, two forms under one name.**
  * The min/max form $S_L = \min(v_n^- - c^-,\ v_{n,\mathrm{Roe}} - c_{\mathrm{Roe}})$,
    $S_R = \max(v_n^+ + c^+,\ v_{n,\mathrm{Roe}} + c_{\mathrm{Roe}})$, proposed
    "concerning the stability and positivity preserving property"; it
    returns the exact speed of an isolated shock
    ([Xie et al. (2021)](/sources/xie-2021.md), eq. 10). Simon & Mandal write
    the 0 into the same minimum and maximum, and call HLL with these speeds
    HLLE ([Simon & Mandal (2019)](/sources/simon-2019.md), §4.1, eq. 9;
    [Simon & Mandal (2019b)](/sources/simon-2019-b.md), eq. 9).
  * Toro's form (eqs. 10.46–10.48): a mean normal velocity minus and plus
    $\bar c_{\mathrm E}$, with
    $\bar c_{\mathrm E}^2 = \dfrac{\sqrt{\rho^-}\,(c^-)^2 + \sqrt{\rho^+}\,(c^+)^2}{\sqrt{\rho^-} + \sqrt{\rho^+}} + \dfrac12\,\dfrac{\sqrt{\rho^-\rho^+}}{(\sqrt{\rho^-} + \sqrt{\rho^+})^2}\,(v_n^+ - v_n^-)^2$;
    "reported to lead to effective and robust schemes". The naming clash
    is recorded on the [approximate Riemann solvers](/methods/approximate-riemann-solvers.md)
    page (batch-12 bullet "Two formulas called Einfeldt's").
* **Pressure-based** (Toro, Spruce & Speares; eqs. 10.49–10.56): estimate
  the star pressure $p_*$ first, then $S_L = v_n^- - c^-q^{\mathrm w}_L$,
  $S_R = v_n^+ + c^+q^{\mathrm w}_R$, with $q^{\mathrm w}_L = 1$ for a
  left rarefaction ($p_* \le p^-$) and
  $q^{\mathrm w}_L = \left[1 + \frac{\gamma+1}{2\gamma}(p_*/p^- - 1)\right]^{1/2}$
  for a left shock, and $q^{\mathrm w}_R$ likewise with $p^+$. The speed is then that of the rarefaction head or of the
  shock for the estimated pressure. $p_*$ comes from PVRS, TRRS, TSRS or,
  "in computational practice", the adaptive hybrid (p. 305;
  [exact Riemann solver](/methods/exact-riemann-solver.md)).
* **Eigenvalues at the mean state.** Dumbser & Balsara take $S_L^-$ as
  the smallest of 0 and the eigenvalues at $u^-$ and at
  $\tfrac12(u^- + u^+)$, and $S_R^+$ symmetrically
  ([Dumbser & Balsara (2016)](/sources/dumbser-2016.md), eq. 5).
* **Other systems.** For a gas–droplet two-fluid model, a "simple"
  estimate (extremes of $v_n \mp c$ over both phases) is called the more
  robust and Nguyen et al.'s mixture sound speeds the more accurate
  ([Yeom & Chang (2010)](/sources/yeom-2010.md), §3.2).
* **Frozen speeds in one-step schemes.** Freezing $S_L$, $S_R$ at the
  space–time barycentre of a face makes the flux linear in the predictor's
  states and fluxes, so it can be averaged exactly
  ([Balsara et al. (2009)](/sources/balsara-2009.md), §4.1; [ADER](/methods/ader.md)).

## Rusanov and Lax–Friedrichs as special cases

With $S_L = -S$, $S_R = S$ the flux is
$\tfrac12\left(f(u^-) + f(u^+)\right) - \tfrac12 S(u^+ - u^-)$
([Toro (1997)](/sources/toro-1997.md), eqs. 10.42–10.45):
* Davis's $S = \max(\vert v_n^- - c^-\vert, \vert v_n^+ - c^+\vert, \vert v_n^- + c^-\vert, \vert v_n^+ + c^+\vert)$
  gives the Rusanov (local Lax–Friedrichs) flux, whose $S$ is the registry's
  $\alpha_{i+1/2}$;
* $S = h/\Delta t$ (the largest speed at Courant number 1) gives the
  Lax–Friedrichs flux.

Their cost is the cost of dissipating every wave at the fastest speed.
First-order Lax–Friedrichs pairs odd and even cell values and spreads a
shock over about 8 cells ([Toro (1997)](/sources/toro-1997.md), §6.4.2).
In Sod's 1978 comparison Rusanov's scheme smears the contact over 14–16
zones and the shock over 6–8, "extremely diffusive"
([Sod (1978)](/sources/sod-1978.md)). At high order, WENO-HLLC and
WENO-MUSTA are about twice as accurate on the same mesh as Rusanov-based
FV-WENO ([Titarev & Toro (2004)](/sources/titarev-2004.md), §§5.1–5.2).
Classical FD-WENO needs a smooth flux splitting, which restricts it to
Lax–Friedrichs or Roe-type fluxes
([Balsara et al. (2025)](/sources/balsara-2025.md), §I).

## Contact and shear diffusion

* **The defect.** For the Euler equations HLL smears contacts, shear
  waves and material interfaces, which "is unacceptable" when they are
  stationary ([Toro (1997)](/sources/toro-1997.md), p. 293). For a passive
  scalar it is more diffusive than Godunov's flux whenever the flow is
  subsonic (§10.7, eq. 10.62; the weights are on the
  [HLLEM](/methods/hllem-riemann-solver.md) page), and on an isolated
  stationary contact it smears the jump over the whole domain by $t = 2$
  at 100 cells (Fig. 10.9; set-up on the [HLLC](/methods/hllc-riemann-solver.md) page).
* **Where it sits.** In the central form it is the density jump in the
  state-difference term of $\mathbf d^{\mathrm{HLL}}$
  ([Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md), §II B).
* **Observed in 2D.** On a first-order supersonic shear flow ($10\times10$
  cells, CFL 1.0, 1000 iterations) HLLE gives "a very diffused density
  profile" where HLLC and its cured variants keep the contact
  ([Simon & Mandal (2019)](/sources/simon-2019.md), §9.8). Xie et al. find
  HLLE smearing the shear of a flat-plate boundary layer and of Elling's
  physical carbuncle ([Xie et al. (2021)](/sources/xie-2021.md), §§6.5–6.6).
  Kitamura & Shima class HLLE with van Leer's and Hänel's splittings as
  very robust at shocks but "too diffusive at contact discontinuity or
  boundary-layer" ([Kitamura & Shima (2019)](/sources/kitamura-2019.md), §II.B).
* **Less of a defect at high order.** Better reconstruction shrinks the
  interface jumps, so HLLE's extra dissipation shrinks with it. With
  $r = 2$ WENO slopes at second order, HLLE and Roe errors on the MHD
  vortex are "entirely comparable"; in 1D Roe resolves noticeably better
  at that reconstruction, and the gap narrows with blended WENO. HLLE's
  cost grows only linearly with the number of species
  ([Balsara (2004)](/sources/balsara-2004.md), §§2, 3.4, 6, Table 3). On
  torsional Alfvén-wave decay, HLL with a multidimensional solver without
  sub-structure dissipates about 6 times more than HLLI at second order,
  3 times at third, and almost the same at fourth
  ([Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §5.5).
* **Sonic points.** "Correct handling of sonic flow is a distinctive
  feature of HLL-type Riemann solvers": no entropy fix is needed at a
  sonic rarefaction ([Toro (1997)](/sources/toro-1997.md), §10.8, p. 308).
* **Repairs.** A second star state ([HLLC](/methods/hllc-riemann-solver.md)),
  a linear sub-structure along the intermediate fields
  ([HLLEM/HLLI](/methods/hllem-riemann-solver.md)), or a smaller density
  jump in the dissipation (HLL-BVD, below). Mandal & Panwar's earlier fix
  replaces the density jumps by pressure jumps under a local isentropy
  assumption that "may not always hold"
  ([Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md), §II C).

## Positivity: what is proved, and for what

* **Proved in the corpus: Lax–Friedrichs only.** For the 1D Euler
  equations the first-order Lax–Friedrichs scheme with
  $\alpha = \Vert\vert\mathbf v\vert + c\Vert_\infty$ keeps cell averages in
  $\mathcal{G}$ under $\Delta t\,\alpha/h \le 1$, because the update is a
  convex combination of $u$ and $u \pm f(u)/\alpha$, both admissible;
  Perthame and Shu had $\tfrac12$
  ([Zhang & Shu (2010)](/sources/zhang-2010.md), Remark 2.4;
  [positivity preservation](/properties/positivity-preserving.md)).
* **Cited, not proved here: HLL and HLLE.** Zhang & Shu list the HLL flux
  among the positivity-preserving first-order fluxes, citing Harten, Lax
  and van Leer ([Zhang & Shu (2010)](/sources/zhang-2010.md), §1).
  Simon & Mandal state that HLL with Einfeldt's speeds is "both positivity
  preserving and entropy satisfying" ([Simon & Mandal (2019)](/sources/simon-2019.md), §4.1),
  and Deng, Boivin & Xiao restate positivity for HLL
  ([Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md), §I). The scope
  given by Balsara & Kim is narrower: Einfeldt et al. proved positivity
  for the HLL/HLLEM class applied to one-dimensional first-order schemes
  for Euler flow, and no proof exists for Roe- or Osher-type solvers
  ([Balsara & Kim (2016)](/sources/balsara-2016-b.md), §1). Einfeldt et al.
  (1991) is not in the corpus, so every HLL positivity claim in this bundle
  rests on citation.
* **MHD.** A first-order scheme with HLL or LLF face fluxes "will indeed be
  PCP, as was first proved by Gurski" ([Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §5.1);
  whether the first-order Lax–Friedrichs MHD scheme is provably positive is
  an open entry under `Contradictions` on the
  [positivity page](/properties/positivity-preserving.md).
* **Not inherited automatically.** HLLEM's claim to inherit HLL's
  positivity is asserted, not proved ([HLLEM](/methods/hllem-riemann-solver.md)),
  and HLL-BVD does not claim it (below).

## Robustness at strong shocks

* **The case for.** HLL's shock stability is attributed to its
  dissipation of the linear waves, as a corollary of the Gressier–Moschetta
  conjecture that exact contact resolution and shock stability exclude each
  other ([Simon & Mandal (2019)](/sources/simon-2019.md), §4.1;
  [Simon & Mandal (2019b)](/sources/simon-2019-b.md), §4). In the
  saw-tooth analysis across a perturbed normal shock HLLE damps density,
  normal velocity and pressure alike by $1 - 2\nu_y$, where HLLEM leaves
  density and normal velocity undamped
  ([Simon & Mandal (2019b)](/sources/simon-2019-b.md), §5). Balsara calls
  HLLE "free of the carbuncle instability", citing Pandolfi & D'Ambrosio
  ([Balsara (2004)](/sources/balsara-2004.md), §6). In shallow water the
  two-wave HLLS solver stays free of carbuncles where the complete
  augmented Roe solver does not, at the price of shear diffusion
  ([Navas-Montilla & Murillo (2019)](/sources/navasmontilla-2019.md), §4.2.1).
  At second order, HLL with Davis's speeds is clean on a perturbed Mach 20
  shock, a Sedov blast and the double Mach reflection, where HLLC is not
  ([Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md), §§III F–H).
* **The case against.** HLLE with Einfeldt's speeds captures a steady
  shock with one interior point and is as unstable as HLLEM on the 1D
  steady shock for sub-cell positions 0–0.3, the one-dimensional carbuncle
  ([Xie et al. (2021)](/sources/xie-2021.md), §3.1.2, Table 1;
  [stationary normal shock](/benchmarks/stationary-normal-shock.md)).
  Kitamura & Shima hold that "any flux functions … can generate
  carbuncles" ([Kitamura & Shima (2019)](/sources/kitamura-2019.md), §I).
* **Status.** The disagreement is the open entry "Is HLLE carbuncle-free?"
  under `Contradictions` on the
  [approximate Riemann solvers](/methods/approximate-riemann-solvers.md)
  page, which records each side's evidence and scope; it is not restated
  here. See also [numerical shock instability](/definitions/numerical-shock-instability.md).
* **HLL as the robust partner.** Hybrid (Roe–HLLE, HLLC–HLL) and rotated
  solvers fall back on HLL(E) near shocks
  ([Simon & Mandal (2019)](/sources/simon-2019.md), §1), and trade shear
  resolution for stability: Quirk's Roe–HLLE hybrid smears Elling's
  physical carbuncle ([Xie et al. (2021)](/sources/xie-2021.md), §6.6). Selective
  wave modification instead widens the HLL speeds only inside the
  dissipation of HLLC or HLLEM
  ([cures for numerical shock instability](/methods/shock-instability-cures.md)).

## HLL-BVD

Deng, Boivin & Xiao keep the two-wave fan and Davis's speeds and change
only the density in the state-difference term of $\mathbf d^{\mathrm{HLL}}$:
each cell carries a MUSCL and a THINC (tanh) density profile, and a BVD
selection takes, at each face, the left/right pair with the smallest jump
([Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md), §II D, eqs. 15–17).
At second order it resolves contacts more sharply than HLL and, in most
tests, HLLC, without HLLC's odd–even decoupling, Sedov axis oscillations
or kinked Mach stem (§§III A–H). The robustness is observed, not proved;
HLL's entropy, isolated-shock and positivity properties are restated for
HLL but not claimed for HLL-BVD. The full description, with what the
paper leaves unspecified, is on the
[approximate Riemann solvers](/methods/approximate-riemann-solvers.md)
page (batch-11 bullet "HLL-BVD").

## HLL as a building block

* *Non-conservative systems.* Integrating along the two segments
  $u^- \to u^{\mathrm{HLL}}_* \to u^+$ gives a path-conservative HLL state,
  implicit and found by Picard or quasi-Newton iteration
  ([Dumbser & Balsara (2016)](/sources/dumbser-2016.md), §2.1). In a
  two-fluid model the interface volume fraction multiplying the
  non-conservative terms is weighted with the HLL coefficients
  $S_R/(S_R - S_L)$ and $-S_L/(S_R - S_L)$
  ([Yeom & Chang (2010)](/sources/yeom-2010.md), §3.2).
* *Sub-structure.* HLLEM/HLLI adds a linear variation along chosen
  intermediate fields and reduces to HLL when the anti-diffusion is off
  ([HLLEM](/methods/hllem-riemann-solver.md)). Balsara & Nkonga's
  first-moment HLLI tends to HLL when one speed is much smaller in
  magnitude than the other ([Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §2).
* *Multidimensional HLL* at edges and vertices, for the induction
  equation; the 2D HLLI analogue reduces to it at zero slopes
  ([multidimensional Riemann solvers](/methods/multidimensional-riemann-solvers.md);
  [Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §3;
  [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §3).
* *In production schemes.* HLLE with SSP-RK3 in fifth-order block AMR
  ([Chen, Tóth & Gombosi (2016)](/sources/chen-2016.md)); HLL among the face
  fluxes of fourth-order FV for MHD ([Berta et al. (2024)](/sources/berta-2024.md), §§3.2–3.3).

# Citations

1. [Toro (1997)](/sources/toro-1997.md), Ch. 10 introduction, §§6.4.2, 10.2–10.3, 10.5, 10.7–10.8.
2. [Xie et al. (2021)](/sources/xie-2021.md), §§1, 3, 5–6, eqs. 10–12 (arXiv v3).
3. [Dumbser & Balsara (2016)](/sources/dumbser-2016.md), §2.1, eq. 5.
4. [Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md), §§I–II, III A–H.
5. [Simon & Mandal (2019)](/sources/simon-2019.md), §§1, 4.1, 5, 9.8, eqs. 9, 14–18.
6. [Simon & Mandal (2019b)](/sources/simon-2019-b.md), §§4–5, eq. 9.
7. [Kitamura & Shima (2019)](/sources/kitamura-2019.md), §§I, II.B.
8. [Balsara et al. (2009)](/sources/balsara-2009.md), §4.1.
9. [Yeom & Chang (2010)](/sources/yeom-2010.md), §3.2.
10. [Sod (1978)](/sources/sod-1978.md).
11. [Titarev & Toro (2004)](/sources/titarev-2004.md), §§5.1–5.2.
12. [Balsara, Bhoriya, Shu & Kumar (2025)](/sources/balsara-2025.md), §I.
13. [Balsara (2004)](/sources/balsara-2004.md), §§2, 3.4, 6, Table 3.
14. [Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §§2, 3, 5.5.
15. [Zhang & Shu (2010)](/sources/zhang-2010.md), §1, Remark 2.4.
16. [Balsara & Kim (2016)](/sources/balsara-2016-b.md), §1.
17. [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §§3, 5.1.
18. [Navas-Montilla & Murillo (2019)](/sources/navasmontilla-2019.md), §4.2.1.
19. [Chen, Tóth & Gombosi (2016)](/sources/chen-2016.md).
20. [Berta et al. (2024)](/sources/berta-2024.md), §§3.2–3.3 (arXiv v4).
