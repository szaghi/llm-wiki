---
type: Method
title: "HLLEM (HLLI) Riemann solver"
description: "HLL with a linear sub-structure along chosen intermediate characteristic fields, which subtracts an anti-diffusive term from the HLL flux: Einfeldt's Euler solver, generalized by Dumbser and Balsara to any conservative or path-conservative system with a diagonal anti-diffusion matrix (alias HLLI); it keeps stationary contacts, shear and Alfvén waves, and is shock-unstable unless cured."
status: established
aliases: [HLLEM, HLLI, HLLEM-NC, Einfeldt HLLEM, anti-diffusive HLL]
tags: [riemann-solver, numerical-flux, well-balanced, shock-instability, hllem]
timestamp: 2026-10-13T00:00:00Z
---

# HLLEM (HLLI) Riemann solver

HLL replaces the Riemann fan by one constant state $u^{\mathrm{HLL}}_*$
between $S_L$ and $S_R$, which smears every intermediate wave. HLLEM
lets the state vary linearly inside the fan along chosen intermediate
families $p \in \mathcal I$. This leaves $u^{\mathrm{HLL}}_*$ unchanged
for a conservation law and subtracts an anti-diffusive term from the HLL
flux ([Dumbser & Balsara (2016)](/sources/dumbser-2016.md), §2.2, eqs. 26–30):
$$\hat f^{\mathrm{HLLEM}} = \frac{S_R^+ f(u^-) - S_L^- f(u^+)}{S_R^+ - S_L^-} + \frac{S_L^- S_R^+}{S_R^+ - S_L^-}\left(u^+ - u^-\right) - \frac{S_L^- S_R^+}{S_R^+ - S_L^-}\sum_{p\in\mathcal I}\delta_p\, r^{(p)}\,\ell^{(p)}\left(u^+ - u^-\right),$$
$$\delta_p = 1 - \frac{\min(\lambda^{(p)}, 0)}{S_L^-} - \frac{\max(\lambda^{(p)}, 0)}{S_R^+}, \qquad 0 < \delta_p \le 1.$$
The speeds are clipped at zero (eq. 5): $S_L^-$ is the smallest of 0 and
the eigenvalues at $u^-$ and at the mean state $\tfrac12(u^- + u^+)$, and
$S_R^+$ the largest of 0 and those at $u^+$ and at the mean state.
The eigenvectors and eigenvalues of the intermediate fields are evaluated
once per face, at the mean state or at a Roe average. Since
$S_L^- S_R^+ \le 0$, the last term lowers the HLL dissipation on the chosen
fields. The underlying two-wave solver is on the [HLL Riemann solver](/methods/hll-riemann-solver.md) page.
* **Where $\delta_p$ comes from.** Write the flux as
  $\tfrac12(f(u^-) + f(u^+)) - \tfrac12\Theta_{i+1/2}(u^+ - u^-)$.
  Einfeldt's stability condition, that the eigenvalues of $\Theta_{i+1/2}$
  bound $\vert\lambda^{(p)}\vert$ at the Roe state, gives $\delta_p$ as an
  upper bound. At the bound the intermediate fields get Roe-like upwind
  dissipation $\vert\lambda^{(p)}\vert$ (App. B). For the single Euler
  contact $\delta_p$ reduces to Einfeldt's
  $(S_R - S_L)/(S_R - S_L + 2\vert v_n\vert)$ when the speeds are
  symmetric about the contact, $S_L + S_R = 2v_n$. Xie et al. reach the same
  bound from the contact stability condition, so $\delta_p$ cannot simply
  be raised further ([Xie et al. (2021)](/sources/xie-2021.md), eqs. 43–44).
* **Einfeldt's Euler form**, as used in the shock-instability papers.
  The intermediate families are the contact and the shear wave, with
  $\delta_p = c/(c + \vert v_n\vert)$ at the Roe state and Einfeldt's
  speeds $S_L = \min(v_n^- - c^-,\ v_n - c)$ and
  $S_R = \max(v_n^+ + c^+,\ v_n + c)$, the second argument at the Roe
  state, clipped at zero in the flux (Simon & Mandal write the 0 into
  the same minimum and maximum) ([Simon & Mandal (2019b)](/sources/simon-2019-b.md), eqs. 9, 13–17;
  [Xie et al. (2021)](/sources/xie-2021.md), eqs. 10, 13–20). With
  $S_{L,R} = v_n \mp c$ at the Roe state, the two expressions for
  $\delta_p$ coincide, and HLLEM is identical to Roe's solver
  ([Xie et al. (2021)](/sources/xie-2021.md), §3.3.1).

**Generalization (Dumbser & Balsara).** The paper's contributions:
* **Non-conservative systems.** For systems with non-conservative
  products, the HLL state follows from a path integral along the two
  segments $u^- \to u^{\mathrm{HLL}}_* \to u^+$. This makes
  $u^{\mathrm{HLL}}_*$ implicit, and a Picard or quasi-Newton iteration
  finds it "very rapidly". The resulting path-conservative solver is
  called HLLEM-NC. For conservation laws no iteration is needed (§2.1,
  eqs. 8–20).
* **Flattener.** A factor between 0 (HLL) and 1 (HLLEM) multiplies the
  anti-diffusive term. Where eigenvalues coincide and the eigenvectors are
  incomplete, the term is dropped, "a very crude procedure" (§2.2).
* **Completeness.** Including every intermediate field, genuinely
  nonlinear ones too, makes the solver complete. The paper does this for
  MHD and relativistic MHD (with the slow waves), and for Euler, where the
  two linearly degenerate fields are the only intermediate ones (§2.3).
* **Name.** The paper calls the solver HLLEM throughout. It "could
  alternatively be called the HLLI Riemann solver", "I" for the
  intermediate fields (abstract, §4). The batch-7 description of HLLI
  ([Balsara (2017)](/sources/balsara-2017-d.md), Apps. D–E) gives exactly
  this $\delta_p$, so this paper is its primary source. The LLF-based
  sibling "LLFI" does not occur in this paper; the bundle has it from
  [Balsara et al. (2025)](/sources/balsara-2025.md).
* **Claimed properties.** It needs no entropy fix and shows no sonic
  glitch in Toro's modified Sod problem. It "naturally inherits the
  positivity properties and the entropy enforcement" of HLL, but this is
  asserted, not proved, and asserted for general conservative and
  non-conservative systems (abstract, §§1, 3.6.1). Balsara & Kim state
  that Einfeldt et al. proved positivity for the HLL/HLLEM class
  applied to one-dimensional first-order schemes for Euler flow
  ([Balsara & Kim (2016)](/sources/balsara-2016-b.md), §1) (HLLE only,
  per the batch-16 block below). It costs one
  eigen-decomposition per face. The authors say it outperforms the
  Dumbser–Osher–Toro solver "by a wide margin" at similar quality, but
  report no timings (§4).
* **Tests.** All tests are 1D and second-order TVD (minmod,
  MUSCL–Hancock type). They cover shallow water, two-layer shallow water,
  debris flow, Baer–Nunziato, ideal MHD with GLM, Euler with an ideal or a
  real-gas equation of state, nonlinear elasticity and relativistic MHD.
  HLLEM keeps stationary contacts, Alfvén and elastic contact waves that
  HLL smears at second order (§§3.5–3.7). The Baer–Nunziato problems
  needed a flattener of 0.97 (§3.4.2). High order appears in one
  sentence: freezing the speeds and the viscosity matrix per face would
  allow a quadrature-free [ADER](/methods/ader.md)-WENO formulation (§4).
* **Well-balancing.** At lake-at-rest data, $\lambda^{(p)} = 0$ gives
  $\delta_p = 1$, and the fluctuations vanish for any bottom topography.
  The non-conservative scheme is therefore exactly well balanced for
  shallow water (§3.1.1; [well-balanced schemes](/properties/well-balanced.md)).

**Shock instability.** Resolving the contact and shear waves makes HLLEM
unstable at strong grid-aligned shocks. On faces transverse to a
perturbed normal shock, its anti-diffusion cancels the HLL damping of
density and normal velocity. It produces odd–even decoupling, kinked Mach
stems and the blunt-body carbuncle
([Simon & Mandal (2019b)](/sources/simon-2019-b.md), §§5, 7;
[Xie et al. (2021)](/sources/xie-2021.md), §§3, 6;
[numerical shock instability](/definitions/numerical-shock-instability.md)).
For the remedies (selective wave modification, anti-diffusion control,
entropy control), see [cures for numerical shock instability](/methods/shock-instability-cures.md).

**Uses in this bundle.** HLLEM for relativistic MHD
([Balsara & Kim (2016)](/sources/balsara-2016-b.md)), HLLI with
sub-structure in multidimensional solvers ([Balsara (2017)](/sources/balsara-2017-d.md)),
and HLLI/LLFI in [alternative finite-difference WENO](/methods/alternative-finite-difference-weno.md)
([Balsara et al. (2025)](/sources/balsara-2025.md)); see the
[Riemann-solver page](/methods/approximate-riemann-solvers.md).

**Later uses (batch 11).**
* *"HLLI" names a family, not one solver* ([Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §§2.1–2.3).
  They re-derive a 1D HLLI in which the fan state is linear in the
  similarity variable scaled to the fan, and impose the first-moment
  (Galerkin) constraint as well as the zeroth. The mean state stays
  $u^{\mathrm{HLL}}_*$, but the mean flux is the HLL flux plus
  $(S_R - S_L)/6$ times the slope of the fan state (eq. 2.7), with slope
  $\sum_{p\in\mathcal I}2\delta_p\,\ell^{(p)}(u^+ - u^-)\,r^{(p)}$ (eq. 2.8).
  The flux is (eq. 2.9c, checked on the page image)
  $$\hat f = \hat f^{\mathrm{HLL}} - \frac12\sum_{p\in\mathcal I}2\delta_p\left[\frac{S_R + S_L}{S_R - S_L}\,\lambda^{(p)} - \frac{S_R - S_L}{3}\right]r^{(p)}\,\ell^{(p)}\left(u^+ - u^-\right),$$
  with the weight (eq. 2.11)
  $$\delta_p = \min\left(\frac{S_R\min(\lambda^{(p)}, 0) + S_L\max(\lambda^{(p)}, 0) - S_RS_L}{(S_R - S_L)^2/3 - \lambda^{(p)}(S_R + S_L)},\ -\frac{3S_RS_L}{(S_R - S_L)^2}\right)$$
  when the denominator is positive, and $\delta_p$ equal to the cap
  $-3S_RS_L/(S_R - S_L)^2$ otherwise. The first argument makes the
  viscosity eigenvalues "minimally match or exceed" Roe's, which is the
  same principle as Einfeldt's bound above. The cap keeps stationary
  linearly degenerate waves exact and is "not mandated by mathematics".
  In the subsonic case it is positive, with maximum 3/4 at $S_R = -S_L$;
  when one speed is much smaller in magnitude than the other, $\delta_p \to 0$ and the
  flux tends to HLL.
* *Two HLLI weights.* The authors call the Dumbser–Balsara solver
  "HLLI-type". Its weight is the $\delta_p$ at the top of this page
  (their eq. 2.13); it omits the first-moment constraint, gives a fan flux
  quadratic in the similarity variable and leaves the mean flux at HLL.
  The paper says that weight allows larger values than eq. 2.11. The cost
  is almost the same, since the eigenvectors dominate it, and "in
  practice, both work equally well" (§2.3). So the alias "HLLI" in this
  page's title, and the range $0 < \delta_p \le 1$ above, belong to the
  Dumbser–Balsara weight; in Balsara's later papers "HLLI" can mean
  either. In the 2D analogue the paper notes that the factors "can be
  greater than unity" (§3;
  [multidimensional Riemann solvers](/methods/multidimensional-riemann-solvers.md)).
* *Dissipation against Roe* (§2.2, Fig. 1). With $S_R - S_L = 1$ and one
  subsonic intermediate wave, the dissipation of the Galerkin HLLI is at
  most 23.2 % above Roe's $\vert\lambda^{(p)}\vert$, at
  $(S_L, S_R) = (-0.9, 0.1)$, and 17.6 % at $(-0.2, 0.8)$. It equals Roe's
  at $(-0.7, 0.3)$ and $(-0.5, 0.5)$, and practically at $(-0.01, 0.99)$.
  It is zero for a stationary wave. The paper's summary "within ten to
  twenty percent … under all circumstances" is exceeded by its own
  23.2 % case, recorded as printed.
* *Positivity, again a procedure* (§§2.1, 2.4). The HLL state plus and
  minus half the slope is checked and the slope reduced if needed; at zero
  slope the flux is HLL. Sub-structure is also skipped where the HLL
  density or pressure is "substantially" outside the range of the input
  states, with no threshold given. This matches the "asserted, not
  proved" status above.
* *Shock instability, from outside the HLLI line.* Deng, Boivin & Xiao
  quote HLLEM as HLL plus an anti-diffusive term with a factor in
  $[0, 1]$ and an eigenstructure matrix, reducing to HLL at 0, and state
  that HLLC and HLLEM "share similar shock instability problems". They
  do not run HLLEM ([Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md), §II C).

**Later uses (batch 12).**
* *The defect HLLEM repairs, in Toro's analysis*
  ([Toro (1997)](/sources/toro-1997.md), §10.7, eq. 10.62). For a passive
  scalar advected with the normal velocity $v_n$ (an isolated contact),
  HLL with $S_{L,R} = v_n \mp c$ weights the scalar fluxes of the left and
  right cells by $\tfrac12(1 + c/v_n)$ and $\tfrac12(1 - c/v_n)$ (the
  reciprocal of the signed Mach number $v_n/c$). This is more diffusive than
  Godunov's flux whenever the flow is subsonic, and, as printed, reduces
  to the Lax–Friedrichs flux when that signed Mach number equals
  $v_n\Delta t/h$. The exact,
  HLLC, Roe and Osher solvers instead resolve a stationary contact
  exactly. Toro's 1D (isolated contact) and 2D (single Mach reflection)
  comparisons of HLL against HLLC are stated in full on the
  [HLLC Riemann solver](/methods/hllc-riemann-solver.md) page ("Contacts
  against HLL"). The book has no HLLEM: HLLC restores the contact with a
  second star state, HLLEM with the linear sub-structure above.

**Later uses (batch 16).** *Einfeldt's HLLEM as printed in 1991*
([Einfeldt et al. (1991)](/sources/einfeldt-1991.md), §5, eqs. 5.1–5.10).
* *Origin.* The paper credits HLLEM, and its equivalence with Roe's
  scheme, to Einfeldt (1988), which is not ingested; the 1991 paper
  restates it. Inside the fan the state varies linearly along the contact
  and shear eigenvectors at the Roe state, centred on the mean speed
  $\tfrac12(S_L + S_R)$; the flux is the HLLE flux minus
  $\frac{S_R^+S_L^-}{S_R^+ - S_L^-}\sum_{p\in\mathcal I}\delta_p\,\ell^{(p)}(u^+ - u^-)\,r^{(p)}$
  (5.5b), the form at the top of this page.
* *The weight, a precision of "Einfeldt's Euler form" above.* Eq. 5.6
  prints $\delta_p = c_{\mathrm{Roe}}/\left(c_{\mathrm{Roe}} + \tfrac12\vert S_L + S_R\vert\right)$
  for both families: the sound speed is the Roe one, but the velocity is
  the mean of the two signal speeds, not the Roe velocity. The two
  readings coincide when the speeds are the Roe eigenvalues; with the
  bounding speeds of eq. 4.5 they differ in general. Read with
  $c_{\mathrm{Roe}} = \tfrac12(S_R - S_L)$ and $v_n = \tfrac12(S_L + S_R)$,
  eq. 5.6 is the $(S_R - S_L)/(S_R - S_L + 2\vert v_n\vert)$ quoted above
  (reader's algebra). The 1991 paper does not print the eigenvalue-bound stability
  condition; it says only that $\delta_p$ removes "excess dissipation in
  the linear degenerate fields, subject to the restriction that the
  stability of the HLLE-schemes is to be preserved".
* *Viscosity form* (5.9–5.10). The eigenvalues of $\Theta_{i+1/2}$ are
  $\frac{S_R^+ + S_L^-}{S_R^+ - S_L^-}\lambda^{(p)} - 2\frac{S_R^+S_L^-}{S_R^+ - S_L^-}$
  on the acoustic families and the same with the second term multiplied
  by $1 - \delta_p$ on the contact and shear families ($\lambda^{(p)}$ at
  the Roe state).
* *Roe speeds fail, bounding speeds are claimed to work* (§5, eqs. 5.7–5.8).
  With $S_{L,R}$ the Roe eigenvalues HLLEM is Roe's scheme, and on
  symmetric double-rarefaction data its star density can be negative
  because those speeds "underestimate the physical signal velocities".
  With the speeds of eq. 4.5 the authors state that the scheme "does not
  require an artificial entropy fix and does not suffer under the
  instabilities described in Section 3".
* *Positivity: asserted, also at the source.* No proof is given for
  HLLEM with $\delta_p \ne 0$. On data without shear the intermediate
  wave strengths vanish and HLLEM reduces to HLLE, which is proved
  positive; on the sheared problem the paper runs HLLEM only with the
  shear weight set to zero (§6, Fig. 6.6). The 1991 paper therefore
  supports Balsara & Kim's "HLL/HLLEM class" attribution under
  "Claimed properties" for HLLE only; the HLLEM part may rest on Einfeldt
  (1988) ([HLL](/methods/hll-riemann-solver.md);
  [positivity preservation](/properties/positivity-preserving.md)).

# Citations

1. [Dumbser & Balsara (2016)](/sources/dumbser-2016.md), §§2–4, App. B.
2. [Simon & Mandal (2019b)](/sources/simon-2019-b.md), §§4–7.
3. [Xie et al. (2021)](/sources/xie-2021.md), §§3, 6.
4. [Balsara (2017)](/sources/balsara-2017-d.md), Apps. D–E.
5. [Balsara & Kim (2016)](/sources/balsara-2016-b.md), §§1, 4.1.
6. [Balsara et al. (2025)](/sources/balsara-2025.md), §II.
7. [Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §§2–3.
8. [Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md), §II C.
9. [Toro (1997)](/sources/toro-1997.md), §10.7.
10. [Einfeldt et al. (1991)](/sources/einfeldt-1991.md), §§5–6, eqs. 5.1–5.10.
