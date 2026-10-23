---
type: Definition
title: "Boundary variation diminishing (BVD)"
description: "BVD is the selection principle that, in each cell, picks among candidate reconstructions (polynomial WENO or TENO versus THINC) the one that minimizes the jump of reconstructed values at cell interfaces, and so the dissipation term of the Riemann flux; this page records how the sources define, use and contrast it, including an interface-wise variant inside a Riemann-solver dissipation term."
status: established
aliases: [BVD, BVD principle, boundary variation diminishing algorithm]
tags: [reconstruction, low-dissipation, interface-capturing, finite-volume, riemann-solver]
timestamp: 2026-10-23T23:55:00Z
---

# Boundary variation diminishing (BVD)

**Boundary variation diminishing** (BVD), introduced by Sun, Inaba and Xiao
(2016) as recalled by the sources, is a parameter-free rule for hybridizing
reconstructions in a Godunov-type finite-volume scheme: each cell carries two
(or more) candidate reconstructions, typically a polynomial one (linear, WENO or
TENO) and a [THINC](/methods/thinc-reconstruction.md) one, and the candidate
selected is the one that minimizes the jump $[\![u]\!]_{i+1/2}=u^+_{i+1/2}-u^-_{i+1/2}$
of the reconstructed values at the cell boundaries
([Takagi et al. (2022)](/sources/takagi-2022.md), §1;
[Fu (2023)](/sources/fu-2023.md), §3.6).

## Why the interface jump

The chunk-1 sources write the finite-volume flux in the unified form

$$\hat f_{i+1/2}=\tfrac12\big(f(u^-_{i+1/2})+f(u^+_{i+1/2})\big)-\tfrac12\lvert\tilde a_{i+1/2}\rvert\big(u^+_{i+1/2}-u^-_{i+1/2}\big),$$

where $\tilde a_{i+1/2}$ is an averaged signal speed fixed by the Riemann solver
(Roe, Rusanov, HLL, HLLC) ([Fu (2023)](/sources/fu-2023.md), §3.6, Eq. (29),
printed with the symbol $\tilde\partial_{i+1/2}$; the same form in
[Huang et al. (2026)](/sources/huang-2026.md), §2.1, Eq. (2.5), which prints the
jump with the wrong sign). The upwind dissipation of the flux is proportional to
the interface jump, so the candidate with the smaller jump is the less
dissipative one; [Deng (2023)](/sources/deng-2023.md) (Remark 7.2) accordingly
describes BVD as minimizing "the absolute dissipation error at a cell boundary".
*(Compiler check, not in the sources: the proportionality is read off the
printed flux form; the sources do not state a theorem on it.)*

[Wakimura et al. (2024)](/sources/wakimura-2024.md) (§3.2.1, Eq. (26)) give the
same rationale on the scalar model $f=au$: the Riemann flux is
$\tfrac12\big(f(u^-)+f(u^+)\big)-\tfrac{\lvert a\rvert}2(u^+-u^-)$, the boundary
variation is $\lvert u^+-u^-\rvert$, and the BVD principle is that it "should be
diminished" to reduce numerical dissipation.

## The minimum-total-boundary-variation selection

Wakimura et al. (§3.2.4, Eqs. (35)–(36)) print the cell-wise selection they take from
Deng et al. (2018) for two candidates A and B in each cell. For a candidate
$\Xi\in\{\mathrm A,\mathrm B\}$ of cell $i$, the total boundary variation is minimized over
the choices $X,Y\in\{\mathrm A,\mathrm B\}$ of the neighbours (page-local symbols):

$$\mathrm{mTBV}^\Xi_i=\min_{X,Y\in\{\mathrm A,\mathrm B\}}\Big(\big\lvert u^{X,-}_{i-1/2}-u^{\Xi,+}_{i-1/2}\big\rvert+\big\lvert u^{\Xi,-}_{i+1/2}-u^{Y,+}_{i+1/2}\big\rvert\Big),$$

where $u^{\Xi,+}_{i-1/2}$ and $u^{\Xi,-}_{i+1/2}$ are the two face values of cell $i$
with candidate $\Xi$ and $u^{X,-}_{i-1/2}$, $u^{Y,+}_{i+1/2}$ those of the neighbours.
Cell $i$ takes A if $\mathrm{mTBV}^{\mathrm A}_i<\mathrm{mTBV}^{\mathrm B}_i$ and B
otherwise, so ties go to B. In MUSCL-THINC-BVD, A is MUSCL with the van Leer limiter
and B is [THINC](/methods/thinc-reconstruction.md) with $\beta_{\mathrm T}=1.6$; in
Adaptive THINC-BVD, A is THINC with $\beta_{\mathrm T}=1.1$ and B THINC with $1.6$.
This answers, for these two schemes, the gap noted under Qualifications: the comparison
uses both faces of the cell and all four neighbour combinations.

## Uses in the sources

- **BVD with TENO.** BVD-TENO5-THINC, the BVD selection between TENO5 and THINC,
  performs better than BVD-WENOZ-THINC (as recalled by
  [Fu (2023)](/sources/fu-2023.md), §3.6); the floating-point treatment that
  restores mirror symmetry for TENO5 has been carried over to BVD schemes
  (§3.8; see [symmetry preservation](/properties/symmetry-preservation.md)).
- **An alternative switch: TENO flags.** [Takagi et al. (2022)](/sources/takagi-2022.md)
  (§1, §3) present [TENO-THINC](/methods/teno-thinc.md) as an alternative to
  BVD: instead of comparing interface jumps of the two candidates, the THINC
  candidate is invoked where the binary stencil flags $\delta_k$ of TENO5 display
  the pattern of a cell containing a discontinuity. Both rules are free of tunable
  parameters; Takagi et al. work in finite difference (on split point
  fluxes), whereas BVD is recalled as a finite-volume rule.
- **Interface-wise BVD inside a Riemann solver.** [Hu, Yuan & Zhao (2022)](/sources/hu-2022.md)
  (§4.2, Eqs. (4.7)–(4.9)) write their shock-stable HLLEM flux as a central part plus a
  dissipation term, $\hat f_{i+1/2}=\tfrac12\big(f(u^-_{i+1/2})+f(u^+_{i+1/2})\big)+D_{i+1/2}$
  (page-local $D_{i+1/2}$), and compute the density *inside $D_{i+1/2}$ only* from the
  combination of MUSCL (P) and THINC (T) interface values with the smallest jump,
  $$\lvert\rho^+-\rho^-\rvert=\min\big(\lvert\rho^{\mathrm T,+}-\rho^{\mathrm T,-}\rvert,\ \lvert\rho^{\mathrm P,+}-\rho^{\mathrm P,-}\rvert,\ \lvert\rho^{\mathrm T,+}-\rho^{\mathrm P,-}\rvert,\ \lvert\rho^{\mathrm P,+}-\rho^{\mathrm T,-}\rvert\big),$$
  an interface-wise selection over all four left/right pairs for one variable, not the
  cell-wise selection recalled above. Whether the central part uses these values is not
  stated. The resulting RHLLEM-LD solver resolves contacts and interfaces more sharply than the
  solvers it is compared with (HLLE and HLLEM on the isolated contact) on an isolated
  contact, the blast wave, Titarev–Toro, Richtmyer–Meshkov and Kelvin–Helmholtz tests at
  second order (§5, Figs. 5.1–5.6), and the
  BVD step does not change the robustness of the solver at strong shocks: HLLEM with BVD
  alone stays unstable on the stationary inclined shock, the shock-stable version stays
  stable (Fig. 5.7, §5.7; see [carbuncle phenomenon](/definitions/carbuncle-phenomenon.md),
  [HLL-family solvers](/methods/hll-riemann-solvers.md)).
- **BVD in a two-phase model with phase change.** Wakimura et al. (2024) apply the two
  selections above to the six-equation model of Pelanti and Shyue with infinite-rate
  pressure, temperature and Gibbs relaxation
  ([five- and six-equation models](/definitions/five-equation-model.md)). Reconstruction
  acts on $(\phi_1,\phi_1\rho_1,\phi_2\rho_2,v,p)$, and the BVD switch only on the volume
  fraction and the two partial densities; velocity and pressure always take MUSCL (or THINC
  with $1.1$) (§3.2.4). For a 1D cavitation tube with rarefactions at $\lvert v\rvert=500$
  m/s, THINC with $1.6$ is admissible in the selection only where $\nabla\cdot v<0$, "to
  address the strong rarefaction waves" (§4.1). The BVD schemes capture contacts in about
  3–4 cells, give more developed Richtmyer–Meshkov structures and resolve vapour bubbles
  created by phase change on $200\times200$ cells, where MUSCL needs $400^2$ or $800^2$
  (stated) (§§4.2–4.4; [gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md),
  [Richtmyer–Meshkov instability](/benchmarks/richtmyer-meshkov-instability.md)). On the
  1D cavitation tube MUSCL-THINC-BVD differs from MUSCL by at most $1.49\times10^{-6}$ in
  mass fraction at $\lvert v\rvert=2$ m/s and $6.00\times10^{-5}$ at $500$ m/s, and Adaptive
  THINC-BVD "appropriately selects" THINC with $1.1$ at smooth rarefaction waves (§4.1). Their Appendix A orders the floating-point
  operations so that the BVD scheme keeps mirror symmetry
  ([symmetry preservation](/properties/symmetry-preservation.md)).
- **A volume-fraction switch instead.** [Zhang et al. (2024a)](/sources/zhang-2024.md)
  (§3.3) cite symmetry-preserving BVD but switch their WENO–THINC multiphase hybrid by a
  volume-fraction test, not by boundary variation (see [THINC](/methods/thinc-reconstruction.md)).
- **A contrast: ROUND.** [Deng (2023)](/sources/deng-2023.md) (Remark 7.2)
  sets BVD against the low-dissipative [ROUND schemes](/methods/round-scheme.md),
  which do not minimize the boundary jump but the *overall* error in a cell, by
  admitting both positive and negative second-order (diffusive and anti-diffusive)
  error terms on the [normalised-variable diagram](/definitions/normalised-variable-diagram.md).

## Qualifications

- The original algorithm of Sun, Inaba and Xiao (2016) is still known here only
  from recollections. Wakimura et al. (2024) print in full the
  minimum-total-boundary-variation selection of Deng et al. (2018) for two
  candidates, which they use; whether it coincides with the 2016 rule, and how
  selections with more than two candidates or several stages work, no ingested
  source states. Hu et al. (2022) give a complete formula for their own
  interface-wise, density-only variant, which is a different rule.
- Wakimura et al.'s $\nabla\cdot v<0$ condition on the steep THINC candidate is
  introduced "to address the strong rarefaction waves" of one test, and no run without
  it is shown (§4.1). Their statement that schemes above third
  order "may introduce spurious oscillation error due to the reconstruction of
  primitive variables" (§1), the reason for their second-order candidates, is given
  without evidence.
- Hu et al. do not give the THINC formula, its steepness or the MUSCL limiter
  used in their BVD candidates.
- "Parameter-free" refers to the selection; the THINC candidate carries its
  steepness $\beta_{\mathrm T}$ (1.6 at discontinuities in the cited BVD
  variants, see [THINC](/methods/thinc-reconstruction.md)).

# Citations

- [Takagi et al. (2022)](/sources/takagi-2022.md) — §1: BVD recalled; §3: TENO-flag switch as alternative.
- [Fu (2023)](/sources/fu-2023.md) — §3.6, Eq. (29): unified flux, BVD-TENO5-THINC; §3.8: symmetry for BVD.
- [Deng (2023)](/sources/deng-2023.md) — Remark 7.2: BVD versus ROUND.
- [Huang et al. (2026)](/sources/huang-2026.md) — §2.1, Eq. (2.5): unified flux form.
- [Hu, Yuan & Zhao (2022)](/sources/hu-2022.md) — §4.2, Eqs. (4.7)–(4.9); §5, Figs. 5.1–5.7: interface-wise BVD of density in the HLLEM dissipation term.
- [Wakimura et al. (2024)](/sources/wakimura-2024.md) — §1; §3.2.1, Eq. (26); §3.2.4, Eqs. (35)–(36); §§4.1–4.4; Appendix A: canonical-flux rationale, minimum-total-boundary-variation selection, BVD in a six-equation model with phase change.
- [Zhang et al. (2024a)](/sources/zhang-2024.md) — §3.3: volume-fraction switch in place of BVD.
