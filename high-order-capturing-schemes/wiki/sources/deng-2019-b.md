---
type: Source
title: "Deng, Boivin & Xiao (2019) — A new formulation for two-wave Riemann solver accurate at contact interfaces"
description: "Introduces HLL-BVD: the HLL flux keeps its two-wave fan and wave speeds, but the state-difference part of its dissipation is evaluated with the face density pair of smallest jump, chosen by boundary variation diminishing between MUSCL and THINC (tanh) profiles; at second order it resolves contacts more sharply than HLL and, in most tests, HLLC, without the odd–even decoupling, Sedov axis oscillations and kinked Mach stem HLLC shows; robustness is observed, not proved."
resource: "doi:10.1063/1.5083888"
source_kind: paper
authors: [Deng X., Boivin P., Xiao F.]
year: 2019
venue: "Phys. Fluids 31:046102"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2019-PhysFluids-Deng-10106315083888.pdf"
tags: [riemann-solver, shock-instability, contact-discontinuity, low-dissipation]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

HLL is robust at strong shocks but smears contacts, and solvers that
resolve the contact (HLLC, HLLEM) show shock instabilities. The paper
proposes **HLL-BVD**, which restores the contact inside HLL's
dissipation instead of adding a contact wave. The HLL flux is split into
a central part and a dissipation term, and the density jump in the
state-difference part of that term is identified as what smears contacts
(§II B). Each cell carries a MUSCL polynomial and a THINC (hyperbolic
tangent) jump profile of density. At each face a BVD (boundary variation
diminishing) selection picks the left/right density pair with the
smallest jump, and only that density enters the state-difference
dissipation (§II D). The wave speeds and the two-wave fan are unchanged.
All tests are second order (MUSCL). Every robustness claim rests on
tests; nothing is proved. Merged into the
[Riemann-solver](/methods/approximate-riemann-solvers.md),
[shock-instability cures](/methods/shock-instability-cures.md),
[HLLEM](/methods/hllem-riemann-solver.md),
[low-Mach flux](/methods/low-mach-number-fluxes.md),
[stationary normal shock](/benchmarks/stationary-normal-shock.md) and
[Quirk test](/benchmarks/quirk-odd-even-test.md) pages.

# Key claims

1. **The HLL dissipation smears contacts** (§II B, eqs. 7–11). With
   Davis's wave speeds (eq. 9),
   $S_L = \min(v_n^- - c^-,\ v_n^+ - c^+)$ and
   $S_R = \max(v_n^- + c^-,\ v_n^+ + c^+)$, the HLL flux is written as
   $\tfrac12\left(f(u^-) + f(u^+)\right) + \mathbf d^{\mathrm{HLL}}$ with
   $$\mathbf d^{\mathrm{HLL}} = \frac{S_R + S_L}{2(S_R - S_L)}\left(f(u^-) - f(u^+)\right) - \frac{S_L S_R}{S_R - S_L}\left(u^- - u^+\right).$$
   This is the subsonic branch $S_L \le 0 \le S_R$, which the paper writes
   without the restriction. A density jump makes $u$ vary between $S_L$
   and $S_R$, which the paper says causes the excess dissipation (citing
   Mandal & Panwar).
2. **Earlier routes, as reviewed** (§II C). Mandal & Panwar replace the
   density jumps in the state-difference term by pressure jumps under a
   local isentropy assumption, which "may not always hold" (eqs. 12–13).
   HLLEM adds to HLL an anti-diffusive term with a factor in $[0, 1]$ and
   an eigenstructure matrix, and reduces to HLL when the factor is 0
   (eq. 14). HLLC and HLLEM "share similar shock instability problems",
   attributed to transverse perturbations; this agrees with Pandolfi &
   D'Ambrosio that solvers treating the contact explicitly show
   carbuncles.
3. **THINC profile** (§II D, eq. 15). In cell $I_i$ the density is a tanh
   jump between $\min(\bar\rho_{i-1}, \bar\rho_{i+1})$ and
   $\max(\bar\rho_{i-1}, \bar\rho_{i+1})$, oriented by the sign of
   $\bar\rho_{i+1} - \bar\rho_{i-1}$, with its position fixed by the cell
   average. The steepness is 1.6 in every test; 1.4–2.0 give "good or
   acceptable results", smaller values are more diffusive and larger ones
   tend "to introduce extra anti-diffusion effect". The closed form of
   the jump position is not given, nor a guard for a cell average outside
   the neighbour range.
4. **BVD selection per face** (eq. 16). The face density pair is the one
   of smallest $\vert\rho^- - \rho^+\vert$ among the four combinations of
   MUSCL and THINC values from the left and from the right. This is a
   per-face choice, not the per-cell choice of the original BVD, and the
   paper does not discuss the difference.
5. **New dissipation** (eq. 17). The flux-difference part of
   $\mathbf d^{\mathrm{HLL}}$ is unchanged. In the state-difference part
   the selected densities replace $\rho$ in all four components (mass,
   both momenta, energy). The paper does not say which density enters
   $f(u^\mp)$ and the wave speeds, nor whether the velocity and pressure in
   eq. 17 are the MUSCL values.
6. **Robustness claim** (abstract, §§II D, IV). Since the wave structure
   is not modified, "the robustness of original HLL has been preserved",
   and the method is "free from carbuncle instability for strong shock".
   This rests on the tests of §§III F–H. HLL's entropy satisfaction,
   exact isolated-shock resolution and positivity are restated for HLL
   (§I) but not claimed for HLL-BVD.
7. **Hybrid cures criticized** (§I). Switching parameters "usually have
   some arbitrariness" that may lead to failures, and hybridization "may
   break the strict Rankine–Hugoniot jump conditions", smearing contacts.
8. **Setting** (§§II A, III). Finite volume, eq. 3; MUSCL reconstruction,
   so at most second order; $\gamma = 1.4$ and CFL 0.4 unless noted. The
   time integrator, the MUSCL limiter and the reconstruction variables are
   not stated. No convergence study, error norms or timings.

# Tests

All compare HLL, HLLC and HLL-BVD, with MUSCL; comparisons are visual.

| § | Test | Set-up as printed | Findings |
|---|---|---|---|
| III A | Isolated contact | $[0,1]$, $(\rho, v_x, p) = (1.4, 0.1, 1)$ for $x \le 0.5$, $(1, 0.1, 1)$ otherwise (eq. 18), $\mathrm{Ma} = 0.1$, 100 cells, $t = 2$; repeated at $\mathrm{Ma} = 10^{-5}$ (velocity and end time not printed) | HLL most diffusive, HLLC "still poorly" sharp, HLL-BVD sharp. At $\mathrm{Ma} = 10^{-5}$ HLL smears the contact completely, HLLC slightly, HLL-BVD not (Fig. 2) |
| III B | [Sod](/benchmarks/sod-shock-tube.md) | standard states (eq. 19), 100 cells, $t = 0.25$ | all similar; contact "slightly thinner" with HLL-BVD |
| III C | [Lax](/benchmarks/lax-shock-tube.md) | standard states (eq. 20), 100 cells; end time not printed | "almost identical" except a "slightly" less diffused contact |
| III C 1 | "Strong Lax problem" | $(1, -19.59745, 1000)$ for $x \le 0.8$, $(1, -19.59745, 0.01)$ otherwise (eq. 21), $t = 0.012$ | a stationary contact: HLLC resolves it best but "produces the largest overshoot values across the shock"; HLL-BVD much sharper than HLL, no overshoot. Not Lax's problem despite the name |
| III D | Slowly moving shock | 1000 cells, $t = 1.5$ (eq. 22, states swapped as printed, see Citations) | HLLC oscillates most behind the shock; HLL-BVD is "clearly" the most stable ([slowly moving shock anomaly](/definitions/slowly-moving-shock-anomaly.md)) |
| III E | [2D Riemann problems](/benchmarks/two-dimensional-riemann-problems.md) | two four-contact configurations with full printed states (eqs. 23–24), $[-0.5, 0.5]^2$, $600^2$; end time and boundaries not printed | HLL-BVD best at contacts and shear; HLL misses the Kelvin–Helmholtz roll-up |
| III F | "Odd–even perturbation problem" | stationary Mach 20 shock, 51×26 cells, perturbed shock column (eq. 25), CFL 0.5, $10^4$ and $4\times10^4$ steps | odd–even decoupling "clearly visible" with HLLC; HLL and HLL-BVD clean ([stationary normal shock](/benchmarks/stationary-normal-shock.md)) |
| III G | [Sedov blast](/benchmarks/sedov-blast-wave.md) | $[-1.1, 1.1]^2$, $160^2$, ambient $p = 10^{-6}$, $\epsilon_0 = 0.244816$ in the centre cell, $t = 1$ | HLLC shows carbuncle-type oscillations along the axes and the largest radial error; HLL and HLL-BVD stable |
| III H | [Double Mach reflection](/benchmarks/double-mach-reflection.md) | Mach 10, 60° shock on $[0, 3.2]\times[0, 1]$, $t = 0.2$; grid and most boundaries not printed | HLLC kinks the Mach stem; HLL and HLL-BVD do not; HLL-BVD resolves the slip-line roll-up with less diffusion than HLL |
| III I | Rayleigh–Taylor | $[0, 0.25]\times[0, 1]$, $60\times240$, $\gamma = 5/3$, $t = 1.95$ (eq. 27) | HLL most diffusive; HLLC and HLL-BVD close, HLL-BVD sharper |

# Notation map

| Deng, Boivin & Xiao (2019) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf U$, $\mathbf F(\mathbf U)$, $\overline{\mathbf U}_i$ | $u$, $f(u)$, $\bar u_i$ | |
| $\mathbf F_{i\pm1/2}$, $\Delta x$ | $\hat f_{i\pm1/2}$, $h$ | |
| subscripts $L$, $R$ at a face | superscripts $-$, $+$ | $\mathbf F_L = f(u^-)$ |
| $u$, $v$ (velocity) | $v_x$, $v_y$; $v_n$ normal to a face | |
| $S_L$, $S_R$ | $S_L$, $S_R$ | Davis estimates |
| $\mathbf U^*$, $\mathbf F^*$ | $u^{\mathrm{HLL}}_*$, $\hat f^{\mathrm{HLL}}$ | subsonic branch |
| $\varepsilon_{hll}$ | $\mathbf d^{\mathrm{HLL}}$ | equal for $S_L \le 0 \le S_R$ |
| $\varepsilon_1$, $\varepsilon_2$, $\varepsilon_{new}$ | (words: flux-difference part, state-difference part, HLL-BVD dissipation) | |
| $\phi$, $M(\mathbf U)$ (HLLEM) | $\delta_p$ and $\sum_{p\in\mathcal I}\delta_p r^{(p)}\ell^{(p)}$ | $\phi_i$ and $M$ are taken in the registry |
| $\beta$, $\theta$, $\tilde x_i$, $\tilde\rho_i(x)$ (THINC) | (words: steepness, jump orientation, jump position, profile) | collide with $\beta_k$, $\theta$ |
| $\rho^P_{L/R}$, $\rho^T_{L/R}$ | (words: MUSCL and THINC face densities) | |
| $\bar c$ (eq. 13) | (words: mean sound speed) | the overbar is the cell average in the registry |
| Ma | $\mathrm{Ma}$ | |
| $\lambda$ (eq. 25) | (words: perturbation weight) | collides with $\lambda^{(p)}$ |
| $\tau$ (Rayleigh–Taylor amplitude) | (words) | collides with $\tau$ |

# Pages created or updated

* Updated [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md) (HLL-BVD; bearing on the HLLE contradiction), [HLLEM (HLLI) Riemann solver](/methods/hllem-riemann-solver.md), [Cures for numerical shock instability](/methods/shock-instability-cures.md), [Low-Mach-number numerical fluxes](/methods/low-mach-number-fluxes.md), [Stationary normal shock test](/benchmarks/stationary-normal-shock.md), [Quirk's odd–even decoupling test](/benchmarks/quirk-odd-even-test.md).
* Also cited on [HLLC Riemann solver](/methods/hllc-riemann-solver.md) (created in batch 12).
* Merged at the 2026-10-13 deep lint: updated [Sod shock tube](/benchmarks/sod-shock-tube.md), [Lax shock tube](/benchmarks/lax-shock-tube.md) (and the "strong Lax problem"), [Two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md), [Sedov point-blast wave](/benchmarks/sedov-blast-wave.md) (full-domain centred variant), [Double Mach reflection](/benchmarks/double-mach-reflection.md), [Numerical shock instability](/definitions/numerical-shock-instability.md) and [Slowly moving shock anomaly](/definitions/slowly-moving-shock-anomaly.md).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2019-PhysFluids-Deng-10106315083888.pdf`.
   * **Version.** The publisher's typeset PDF (AIP; cover page plus 12
     article pages). Submitted 1 December 2018, accepted 21 March 2019,
     published online 11 April 2019.
   * **Identity.** doi:10.1063/1.5083888, printed on page 1 and checked on
     Crossref: Phys. Fluids 31(4):046102, issue dated April 2019, authors
     Deng, Boivin, Xiao. Slug `deng-2019-b`, since the bare `deng-2019` is a
     different work (Deng F. et al., Phys. Fluids 31:056106).
   * **How it was read.** Text extraction, all sections; equations read
     from the page images.
   * **Recorded as printed.**
     * Eq. 22 prints $(1, -3.44, 1)$ for $x \le 0.5$ and
       $(3.86, -0.81, 10.33)$ otherwise. The text puts the post-shock
       state on the left and Fig. 7 shows $\rho \approx 3.86$, $p \approx 10.33$
       left of the shock, so the printed states are swapped. In the text's
       orientation the Rankine–Hugoniot speed is about 0.109, which fits
       the shock moving from 0.5 to about 0.66 by $t = 1.5$ (reader's
       check).
     * §III I says "the HLL and HLL-BVD produce very similar prediction",
       while the Fig. 15 caption says HLLC and HLL-BVD are "practically
       indistinguishable"; it also puts the interface "at $y = 0.0$",
       while eq. 27 puts the density jump at $y = 0.5$.
     * The figures label nondimensional data with units (kg/m³, MPa, s).
   * **Reference list:** 54 printed entries, matching Crossref's count; 54
     bibliography entries. Godunov is printed Mat. Sb. 89:271, the
     new-series number of 47:271, and merged into `godunov-1959`.
     Rusanov's NRC translation (printed 1962) is merged into
     `rusanov-1961`. Harten, Lax & van Leer is `harten-1983-d`. Ref. 48
     (Phys. Fluids 30:106110) is `zhang-2018-b`, a different work from
     `zhang-2018`. Quirk's Springer reprint is kept as `quirk-1997` and
     Sedov's CRC edition as `sedov-1993`. Ref. 45 is `deng-2019-c`.
