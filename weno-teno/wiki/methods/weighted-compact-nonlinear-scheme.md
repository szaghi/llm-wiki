---
type: Method
title: "Weighted compact nonlinear schemes (WCNS)"
description: "WCNS are finite-difference shock-capturing schemes in three steps — nonlinear node-to-interface interpolation, a two-point flux at the interfaces, and high-order interface-to-node flux differencing; the page records the explicit WCNS-IS with its eighth-order hybrid differencing and positivity limiters, TENO-weighted members including the 5th- to 11th-order WCNS-T without compact step, the relation to A-WENO, and an open disagreement on conservation."
status: established
aliases: [WCNS, WCNS-Z, WCNS-JS, TCNS, targeted compact nonlinear scheme, WCNS-T, HWCNS, WCNS-IS, PP-WCNS-IS, explicit WCNS]
tags: [compact-scheme, finite-difference, weno, teno, numerical-flux, multiphase]
timestamp: 2026-10-22T20:00:00Z
---

# Weighted compact nonlinear schemes (WCNS)

The **weighted compact nonlinear scheme** of Deng and Zhang (as recalled by Fu 2023, §3.7, and Wong et
al. 2021, §4) is a finite-difference scheme built in three steps:

1. a nonlinear (WENO-weighted) **interpolation** of the variables from the nodes $x_i$ to the
   interfaces ("midpoints") $x_{i+1/2}$, giving $u^\pm_{i+1/2}$;
2. evaluation of an **interface flux** $h(u^-_{i+1/2},u^+_{i+1/2})$, e.g. a Riemann solver;
3. high-order **interface-to-node differencing** of the interface fluxes, compact (spatially
   implicit) in the original scheme, explicit in later ones, to obtain $\partial_xf$ at the nodes.

It shares steps 1 and 2 with the [alternative WENO formulation](/methods/alternative-weno.md), which
reaches high order by explicit even-derivative corrections instead; Ye et al. (2022, §1) state that
AFWENO "is similar to WCNS and is equivalent to the HWCNS scheme under specific parameters" (HWCNS is
cited to a Deng et al. conference paper). For [AFTENO](/methods/afteno.md), Ye et al. (§1, §5) credit
this interpolation-plus-flux structure with the freedom to use any monotone or Riemann-solver flux and
to interpolate conserved, primitive or characteristic variables. Wong et al. (2021, §4.3) make the
same point against flux-split FD-WENO, which they say "degenerates to only second order" with a
Riemann solver, whereas "a WCNS can still maintain high order".

## Explicit WCNS with hybrid differencing (WCNS-IS)

Wong, Angel, Barad & Kiris (2021, §4) build a fifth-order explicit WCNS for the five-equation
two-phase model ([five-equation model](/definitions/five-equation-model.md)).

**Differencing.** Following Nonomura & Fujii's observation that explicit schemes are more efficient,
they use Deng's explicit hybrid cell-midpoint and cell-node scheme (HCS; §4.1, Eq. (77)), with
midpoint fluxes $\tilde f_{i\pm1/2}$ from step 2 and nodal fluxes $f_j=f(u_j)$:

$$\partial_xf\big|_i\approx\frac1{\Delta x}\Big[\Psi\big(\tilde f_{i+1/2}-\tilde f_{i-1/2}\big)-\tfrac{175\Psi-192}{256}\big(f_{i+1}-f_{i-1}\big)+\tfrac{35\Psi-48}{320}\big(f_{i+2}-f_{i-2}\big)-\tfrac{45\Psi-64}{3840}\big(f_{i+3}-f_{i-3}\big)\Big],$$

($\Psi$ the HCS parameter, page-local). With $\Psi=256/175$ the linear scheme is eighth order, leading
error $-\tfrac1{40320}\partial_x^9f\,\Delta x^8$ (Eqs. (78)–(79)), although the family is called
"sixth order". Rewritten in flux-difference form, after Subramaniam, Wong & Lele, it has the implied
interface flux (Eq. (80))

$$\hat f_{i+1/2}=\Psi\tilde f_{i+1/2}-\big(\tfrac{75\Psi}{128}-\tfrac{37}{60}\big)(f_i+f_{i+1})+\big(\tfrac{25\Psi}{256}-\tfrac2{15}\big)(f_{i-1}+f_{i+2})-\big(\tfrac{3\Psi}{256}-\tfrac1{60}\big)(f_{i-2}+f_{i+3}).$$

*(Compiler check, not in the sources: the HCS is exact on polynomials of degree 8, its degree-9
error is $-\tfrac{1}{40320}\partial_x^9f\,\Delta x^8$, and the difference of the implied fluxes
reproduces the bracket above.)* The same formula reconstructs the interface advection velocity, so
that the non-conservative volume-fraction term uses the same differencing as the flux (Eqs. (81)–(82)).

**Interpolation.** An incremental-stencil WENO interpolation adapted from the finite-volume WENO-IS
of Wang, Xiang & Hu (§4.3, Eqs. (84)–(101)): four candidates on $\{i,i+1\}$, $\{i-1,i\}$,
$\{i,i+1,i+2\}$, $\{i-2,i-1,i\}$, with linear weights $\tfrac{15}{32},\tfrac5{32},\tfrac5{16},\tfrac1{16}$
that combine them into the fifth-order interpolant
$\tfrac1{128}(3u_{i-2}-20u_{i-1}+90u_i+60u_{i+1}-5u_{i+2})$, WENO-Z-type weights with the TENO
reference indicator, and an extra indicator on $\{i-1,i,i+1\}$ for the two-point stencils
([smoothness indicators](/definitions/smoothness-indicator.md), [WENO-Z](/methods/weno-z.md),
[targeted ENO](/methods/targeted-eno.md)). *(Compiler check: the four candidates with these weights
give exactly the printed interpolant.)* It is applied to primitive variables projected on
characteristic fields of the primitive system (App. A), with HLLC midpoint fluxes
([HLL-family solvers](/methods/hll-riemann-solvers.md)). Appendix B proves fifth order for a scalar
law with $f'>0$ away from critical points, under the sufficient condition $\omega_k-d_k=O(\Delta x^4)$
([accuracy at critical points](/properties/critical-point-accuracy.md)).

**Positivity and boundedness (PP-WCNS-IS).** Two limiter stages blend with first-order quantities:
an interpolation limiter blends the midpoint states with the node state, successively for partial
densities, volume fraction and $\rho e-\bar p_\infty$ (page-local mixture stiffening pressure); a flux
limiter blends the implied flux with the first-order HLLC flux in the same three stages, with a common
blending factor for the two sides of an interface (§5, Algorithms 1–6). The first-order HLLC scheme is
proved positivity- and boundedness-preserving under CFL $\le0.5$, which the SSP-RK3 extension keeps
(§3.3, §5.3) ([bound preservation](/properties/bound-preservation.md),
[positivity-preserving flux limiter](/methods/positivity-preserving-flux-limiter.md)). Because both
limiters act on the implied fluxes, the update stays in flux-difference form and is "discretely
conservative for all conservative equations" of the model (Abstract, §5.2).

**Results.** Fifth order on 2-D volume-fraction advection ($L_2$ from $3.136\times10^{-5}$ at $8^2$ to
$1.714\times10^{-13}$ at $256^2$, orders 4.85–4.97 beyond the first refinement; Table 4); sharp,
oscillation-free interfaces on 1-D advection, gas–liquid shock tube and multi-material Sedov problems;
the unlimited WCNS-IS fails (imaginary sound speed) on a Mach 10 shock/water-column interaction that
PP-WCNS-IS runs (§6.6); a Mach 100 water jet, multiphase version of the Mach 2000 jet (§6.7;
[shock–water column](/benchmarks/shock-water-column.md),
[high-Mach jets](/benchmarks/high-mach-astrophysical-jet.md),
[Sedov blast wave](/benchmarks/sedov-blast-wave.md)).

## Very high-order interpolation with TENO stencils (WCNS-T, WCNS-JS)

Hiejima (2022) builds explicit WCNS-type schemes for the 3-D Euler equations at interpolation orders
5, 7, 9 and 11. Steps 1 and 2 are as above; step 3 is absent: the flux derivative is
$(\hat f_{i+1/2}-\hat f_{i-1/2})/\Delta x$ with AUSMDV interface fluxes, and "the WCNS does not include
a compact procedure for calculating the flux derivative" (§2.2, Eq. (5); the paper says nothing about
conservation). Primitive variables $(\rho,v,p)$ are interpolated componentwise, with no
characteristic projection, and the time integrator is the four-step fourth-order Runge–Kutta of
Jameson, Schmidt & Turkel at CFL 0.8 (§2.2).

- **Candidates.** For interpolation order $K$ on the full stencil of $K$ points
  $i-\tfrac{K-1}2,\dots,i+\tfrac{K-1}2$ ($K=2r-1$ in the source's order parameter $r$), $K-2$
  substencils: the central $\{i-1,i,i+1\}$ and the pairs $\{i,\dots,i+s+1\}$, $\{i-s-1,\dots,i\}$,
  $s=1,\dots,\tfrac{K-3}2$,
  the "pyramid" taken from the original TENO (§2.3, Fig. 1; see
  [targeted ENO](/methods/targeted-eno.md)). Each candidate is a Taylor expansion about $x_i$ with
  the derivatives replaced by one-sided or central differences on the substencil (Eqs. (6)–(12),
  coefficients in Tables 1, 3, 5); the seventh-order case is written out with its truncation terms
  (Eqs. (19)–(24)). *(Compiler check, not in the sources: with the derivative orders each substencil
  supports, a candidate equals the Lagrange interpolant of the substencil at $x_{i+1/2}$.)*
- **Linear weights** (Tables 2, 4, 6), for the order central, downwind, upwind, …: $K=7$:
  $(\tfrac{35}{64},\tfrac{35}{128},\tfrac7{128},\tfrac7{64},\tfrac1{64})$; $K=9$:
  $(\tfrac{525}{1024},\tfrac{525}{2048},\tfrac{105}{2048},\tfrac{63}{512},\tfrac9{512},\tfrac9{256},\tfrac1{256})$;
  $K=11$: $(\tfrac{8085}{16384},\tfrac{8085}{32768},\tfrac{1617}{32768},\tfrac{2079}{16384},\tfrac{297}{16384},\tfrac{99}{2048},\tfrac{11}{2048},\tfrac{11}{1024},\tfrac1{1024})$;
  the right state uses the mirrored weights. $K=5$ "is consistent with" Deng & Zhang's fifth-order
  WCNS. *(Compiler check, not in the sources: the $K=7$ set combines the five candidates into the
  seven-point interpolant at $x_{i+1/2}$ exactly; for $K=5$ the weights are
  $(\tfrac58,\tfrac5{16},\tfrac1{16})$, the fifth-order interpolation weights printed by Chu et al. 2022
  on the [alternative WENO](/methods/alternative-weno.md) page in the upwind-first order.)* The
  nonlinear value is written $u^{\mathrm{opt}}_{i+1/2}+\sum_k(\omega_k-d_k)u^{(k)}_{i+1/2}$, with
  $u^{\mathrm{opt}}_{i+1/2}$ the optimal linear interpolation (page-local; Eq. (25)).
- **Indicators.** The Deng–Zhang form, unweighted squares of the difference derivatives on each
  substencil (Eq. (14); [smoothness indicators](/definitions/smoothness-indicator.md)).
- **WCNS-JS:** $\alpha_k=d_k/(\epsilon+\beta_k)^2$, $\epsilon=10^{-40}$ (Eq. (15);
  [WENO-JS](/methods/weno-js-reconstruction.md)). **WCNS-T:** $\gamma_k=1/(\epsilon+\beta_k)^6$, no
  constant and no global indicator, normalized $\chi_k$, cut-off $C_T=10^{-5}$ on every candidate,
  $\omega_k=d_k\delta_k/\sum_ld_l\delta_l$ (Eqs. (16)–(18)).
- **Positivity fallback.** In double Mach reflection, where an interpolated $\rho$ or $p$ is
  negative a first-order interpolation is used instead (§3.4, after Kamiya et al.); which variables
  and sides is not stated ([bound preservation](/properties/bound-preservation.md)).

**Evidence** (qualitative; no convergence test; Hiejima 2022, §3, App.): on Sod and Lax at 101 points
WCNS-JS is oscillation-free at every order and WCNS-T shows slight under- and overshoots growing with
order; all schemes overshoot the Lax velocity where the solution is "continuous but not
differentiable" ([Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)). On the
[Shu–Osher problem](/benchmarks/shu-osher-problem.md) (201 and 401 points) WCNS-JS shows "no
difference based on the accuracy" and misses the small waves, which the author attributes to the
dissipation of the Jiang–Shu weights; WCNS-T resolves them, its 11th order equal to its 9th. On
[double Mach reflection](/benchmarks/double-mach-reflection.md) at $1024\times256\times5$ WCNS-JS shows no
Kelvin–Helmholtz roll-up of the slip line at any order, WCNS-T increasingly more with order up to the
9th; at 11th order the wavy structures vanish, "probably caused by the first-order interpolation" of
the fallback; at $2048\times512\times5$ the small scales grow with order up to the 11th (Figs. 7–9). In
Pirozzoli's [approximate dispersion relation](/definitions/approximate-dispersion-relation.md), WCNS-T
is better than WCNS-JS but "not so different", and orders 5 to 11 nearly coincide (Fig. A.1), which the
author reads as an open question of the weight formulation. The conclusion: high order works "on the
premise that a suitable grid resolution is being satisfied", and $q$ and $C_T$ need tuning, as in
[adaptive TENO](/methods/adaptive-teno.md) (§4).

## Members recalled in the sources

- **WCNS-JS and WCNS-Z**: interpolation weighted with Jiang–Shu or WENO-Z weights; WCNS-Z beats
  WCNS-JS (Fu 2023, §3.7).
- **TCNS** (targeted compact nonlinear schemes): WCNS with the [TENO](/methods/targeted-eno.md)
  weighting (incremental stencils, sharp cut-off). TCNS "clearly beat" WCNS-Z; TCNS6 is better than
  seventh- and ninth-order WCNS-Z on the Shu–Osher problem, and TCNS is insensitive to the definition of
  the global indicator $\tau_K$, which mainly affects cost; a TCNS with adaptive dissipation exists
  (Fu 2023, §3.7, §4.1; [adaptive TENO](/methods/adaptive-teno.md)).
- **WCNS-T** (Hiejima): fifth-, seventh-, ninth- and eleventh-order WCNS with TENO weighting (Fu 2023,
  §3.7; also cited by Ye et al., §1); described in the section above.
- **Further members** recalled by Hiejima (2022, §1, §2.3): Nonomura & Fujii's robust explicit
  formulation with ninth-order interpolation, Yan et al.'s seventh-order scheme with Y-type weights
  on the fifth-order stencil, the compact high-resolution interpolation of Subramaniam, Wong & Lele
  (lower dispersion error), and the TCNS of Zhang, Zhang & Xu, TENO stencil selection in fifth-order
  WCNS for optimal linear interpolation in smooth regions; and his own earlier interpolation on
  uniform substencils, which "requires strong suppression of numerical oscillations".
- **Learned variants**: WCNS3-NN and WCNS3-MR-NN, to which Huang et al. (2026, §7) claim their
  diagram-fitting method applies ([learned WENO weights](/methods/learned-weno-weights.md)).
- **Earlier multiphase use**: Wong & Lele applied WCNS to the five-equation model for mixtures of ideal
  gases only (as recalled by Wong et al. 2021, §1).

## Stated weaknesses and neighbours

- Fu (2023, §3.7) names "the lack of conservation" as "the main flaw of WCNS family schemes", although
  their "spectral property is typically better than the WENO counterpart"; see Contradictions.
- Hiejima (2022, §1) states, without citation or test, that WCNS can use any numerical flux, is
  "easy to apply … to general coordinates, in contrast to the WENO scheme", and "slightly outperforms
  the WENO scheme with the same order of accuracy" in resolution, but "is less robust than the WENO
  because the results of the former can sometimes blow up, i.e., the interpolated pressure or density
  becomes negative"; and that "almost all methods with multipoint interpolation above the seventh
  order of accuracy cause spurious oscillations near strong discontinuities".
- **CRWENO** (Ghosh and Baeder, as recalled by Fu 2023, §3.7): compact reconstruction WENO, with lower
  dissipation than WENO at low and moderate wavenumbers and higher dissipation at aliased wavenumbers;
  a TENO variant exists.
- **Cost against finite volumes.** Wong et al. (2021, §4.3), citing Sebastian & Shu, state that
  explicit FD-WENO and WCNS are "four times cheaper in 2D and nine times cheaper in 3D" than
  finite-volume WENO, because they avoid multi-dimensional reconstruction; the factor is relayed, and
  the paper prints no timing for it.

## Qualifications

- The equivalence of AFWENO and HWCNS is relayed from a cited conference paper, not derived in an
  ingested source.
- Wong et al. (2021) read is the arXiv v1 preprint; the value of $\epsilon$ in the WCNS-IS weights is
  not printed.
- Wong et al.'s statement about Riemann solvers in FD-WENO does not cover the alternative
  formulation; see the Qualifications of [alternative WENO](/methods/alternative-weno.md).
- **Order of Hiejima's schemes.** The orders 5 to 11 are interpolation orders. *(Compiler check, not
  in the sources: with no step 3, the plain difference of exact interface fluxes is
  $\partial_xf(x_i)+\tfrac{\Delta x^2}{24}\partial_x^3f(x_i)+O(\Delta x^4)$, so the spatial operator is
  formally second order for point values, the limit Wang et al. 2023 state for an uncorrected
  two-point flux in finite differences; see
  [conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md).)*
  The paper shows no convergence test that could confirm or refute the higher order.
- Hiejima (2022) prints "$c^{(k)}_{2,i+54}$" for $c^{(k)}_{2,i+5}$ in a header of Table 5, and the
  index ranges of Eqs. (11)–(12) and (24) hold only for the widest substencils or for $K=7$. In the
  double Mach reflection the text calls the at-rest state $(1.4,0,0,0,1)$ "post-shock" and imposes it
  at the inflow, while Eq. (29) assigns it to the region ahead of the right-moving shock and the
  compressed state $(8,\dots,116.5)$ to the region behind it; the consistent set-up has the latter as
  the post-shock and inflow state.

## Contradictions

**Conservation of WCNS.** *Open.* [Fu (2023)](/sources/fu-2023.md) (§3.7) states that "the main flaw
of WCNS family schemes is the lack of conservation". [Wong et al. (2021)](/sources/wong-2021.md)
(§4.1, citing Subramaniam, Wong & Lele 2019) state that "any central explicit or compact finite
difference scheme can be rewritten into the flux-difference forms", give the implied interface flux of
their explicit WCNS (Eq. (80)), and call the resulting scheme and its limiters "discretely
conservative for all conservative equations" (Abstract, §5.2). The two statements meet on the compact
form: Fu's sentence closes a passage that describes WCNS as "the WENO-like nonlinear node-to-interface
variable interpolation and the high-order compact scheme for interface-to-node differencing" (Deng &
Zhang 2000), and Wong et al.'s sentence covers "any central explicit or compact" scheme. The conflict is
therefore genuine and is not a difference between an explicit and a compact WCNS. Fu gives no
mechanism and cites no specific scheme in that sentence; Wong et al. derive the implied flux only for
their explicit HCS and relay the compact case from the uningested Subramaniam et al. What would
decide it: a derivation, for the original compact (implicit) interface-to-node differencing with its
boundary closures, of whether a local telescoping interface flux exists, or the identification of the
WCNS variants Fu's statement refers to. *(Compiler check, not in the sources, and not a resolution: Coppola & Veldman 2023,
Lemma A.1, show on the [local conservation](/results/local-conservation-flux-form.md) page that a
globally conservative periodic discretization always factors as a flux difference, which supports Wong
et al. for periodic grids only.)*

# Citations

- [Fu (2023)](/sources/fu-2023.md) — §3.7: three-step WCNS, WCNS-Z, TCNS, WCNS-T, CRWENO, conservation remark; §4.1.
- [Wong et al. (2021)](/sources/wong-2021.md) — Abstract; §1; §3.3; §4.1, Eqs. (73)–(82); §4.2; §4.3, Eqs. (84)–(101); §5, Algorithms 1–6; §6, Table 4; Apps. A–B.
- [Ye et al. (2022)](/sources/ye-2022.md) — §1, §5: AFWENO similar to WCNS, equivalent to HWCNS; WCNS-T cited.
- [Huang et al. (2026)](/sources/huang-2026.md) — §7: WCNS3-NN, WCNS3-MR-NN.
- [Coppola & Veldman (2023)](/sources/coppola-2023.md) — App. A.1, Lemma A.1 (compiler check only).
- [Hiejima (2022)](/sources/hiejima-2022.md) — §1; §2.2, Eq. (5); §§2.3–2.6, Eqs. (6)–(25), Tables 1–6, Fig. 1; §3, Figs. 2–9; §4; App., Fig. A.1: WCNS-T and WCNS-JS at orders 5–11.
