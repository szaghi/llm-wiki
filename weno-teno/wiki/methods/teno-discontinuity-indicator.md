---
type: Method
title: "TENO-based discontinuity indicator"
description: "A troubled-cell flag built from the TENO scale separation: equal three-point stencils spanning the flux stencil, γ_k=(β_k+ε)^{-6}, and a cell is troubled when some normalized χ_k falls below a threshold; Fu's original drives a fifth-order-upwind/TENO6 hybrid, later variants drive TENO-S and TENO-type DG and spectral-difference limiters."
status: established
aliases: [TENO-based troubled-cell indicator, TENO discontinuity indicator, TENO-type indicator, TENO-type troubled-cell indicator, hybrid TENO indicator]
tags: [teno, limiting, finite-difference, dg, low-dissipation]
timestamp: 2026-11-17T08:52:09Z
---

# TENO-based discontinuity indicator

[TENO](/methods/targeted-eno.md) decides, stencil by stencil, whether a candidate is crossed by a
discontinuity: its cut-off flag $\delta_k$ is 0 when the normalized measure $\chi_k$ falls below
$C_T$. [Fu (2019b)](/sources/fu-2019-b.md) turns the same test into a cell flag: "one computational
cell $i$ is identified to be a troubled cell if there exists at least one candidate stencil, which is
judged as 'nonsmooth' by the ENO-like stencil selection strategy" (§4.2). Because TENO judges a scale
smooth when it restores the spectral property of its linear scheme exactly, Fu presents the
threshold as a cut-off in wavenumber, which "takes effects in wavespace rendering its high
generality", unlike thresholds "typically defined in physical space" (Abstract, §1, §4). The flag
selects between a cheap linear flux and a characteristic-wise TENO flux in
[hybrid schemes](/methods/hybrid-weno.md), and, in later papers, the cells a DG or
spectral-difference limiter acts on ([troubled-cell indicators](/definitions/troubled-cell-indicator.md)).

Notation (registry §10): $\mathrm{Flag}_i\in\{0,1\}$ is the flag of cell
$i$, **1 = troubled**, the opposite convention to $\delta_k$ (1 = kept); $\mathrm{Flag}_x$,
$\mathrm{Flag}_y$ the flags of a dimension-by-dimension evaluation. $u$ is the examined variable
(density or total energy, a component of the conserved variables), $\hat f^{\mathrm{lin}}_{i+1/2}$
the flux of the linear branch of a hybrid.

## Definition (Fu 2019b)

**Stencils.** "Different from the candidate stencil arrangement in Fig. 1", i.e. TENO6's candidates
of incremental width, Fu uses four **equal** three-point stencils (§4.1, Fig. 3), in the registry's
order, most upwind first, which Fig. 3 already follows:
$S_0=\{i-2,i-1,i\}$, $S_1=\{i-1,i,i+1\}$, $S_2=\{i,i+1,i+2\}$, $S_3=\{i+1,i+2,i+3\}$. Their union is
$\{x_{i-2},\dots,x_{i+3}\}$, the six-point stencil of the flux at $x_{i+1/2}$. The fourth stencil has
width 3 "rather than 4" to cut the cost, and no candidate flux is computed (§4.1).

**Indicators.** Each $\beta_k$ is the Jiang–Shu
[smoothness indicator](/definitions/smoothness-indicator.md) over the target cell $I_i$; for $S_3$,
which does not contain $x_i$, it is the integral over $I_i$ of the quadratic of $S_3$ extrapolated
there (Eq. (4.1)):

$$\beta_0=\tfrac14(u_{i-2}-4u_{i-1}+3u_i)^2+\tfrac{13}{12}(u_{i-2}-2u_{i-1}+u_i)^2,\qquad
\beta_1=\tfrac14(u_{i-1}-u_{i+1})^2+\tfrac{13}{12}(u_{i-1}-2u_i+u_{i+1})^2,$$
$$\beta_2=\tfrac14(3u_i-4u_{i+1}+u_{i+2})^2+\tfrac{13}{12}(u_i-2u_{i+1}+u_{i+2})^2,\qquad
\beta_3=\tfrac13\big[u_{i+1}(22u_{i+1}-73u_{i+2}+29u_{i+3})+u_{i+2}(61u_{i+2}-49u_{i+3})+10u_{i+3}^2\big].$$

*(Compiler check, not in the sources: $\beta_3$ equals
$\sum_{j=1}^2\Delta x^{2j-1}\int_{I_i}(p^{(j)})^2dx$ exactly for the quadratic $p$ whose cell averages
on $I_{i+1},I_{i+2},I_{i+3}$ are $u_{i+1},u_{i+2},u_{i+3}$; over its own centre cell $I_{i+2}$ the same
quadratic gives the classical form
$\tfrac13(4u_{i+1}^2-13u_{i+1}u_{i+2}+5u_{i+1}u_{i+3}+13u_{i+2}^2-13u_{i+2}u_{i+3}+4u_{i+3}^2)$.)*

**Measure and flag** (Eqs. (4.2)–(4.4)):

$$\gamma_k=\frac1{(\beta_k+\epsilon)^q},\qquad\chi_k=\frac{\gamma_k}{\sum_{l=0}^3\gamma_l},\qquad
\mathrm{Flag}_i=\begin{cases}0,&\chi_k>C_T\ \text{for all }k\in\{0,\dots,3\},\\1,&\text{otherwise},\end{cases}$$

with $q=6$, $C_T=5\times10^{-4}$, and $\epsilon=10^{-4}$ in 1D and $10^{-3}$ in multi-D. The measure
drops the constant $C$ and the global indicator $\tau_K$ of the TENO scheme "to simplify the
scale-separation computation"; the full TENO measure "is also applicable but with more complexity"
(§4.2). A large $q$ "is preferred for strong scale separation", unlike WENO, which keeps $q$ small to
reduce dissipation (§4.2).

**Variables and dimensions** (§5, Algorithm 1; §6). The indicator reads, in physical space, density
and total energy in 1D and density alone in 2D "if not mentioned otherwise", dimension by dimension:
$\mathrm{Flag}_x$ selects the $x$-fluxes and $\mathrm{Flag}_y$ the $y$-fluxes. The flag of cell $i$
decides the flux at $x_{i+1/2}$. Fu notes that a shock not aligned with the grid "may be only
detected as a discontinuity in one dimension", and that "if deemed necessary" the criterion can be
redefined as $\mathrm{Flag}=\max(\mathrm{Flag}_x,\mathrm{Flag}_y)$ for both directions; "in this paper,
numerical simulations demonstrate that the current implementation can generate oscillation-free
solutions", so the runs keep the two flags separate (Figs. 18–28).

*(Compiler check, not in the sources: on sampled sine data of unit amplitude, over 360 phases, the
flag with $\epsilon=10^{-4}$ first fires at the reduced wavenumber $\vartheta\approx0.644$, about ten
points per wavelength, and at 0.645 with $\epsilon=10^{-3}$; $C_T=5\times10^{-3}$ and $5\times10^{-5}$
move it to 0.49 and 0.77. Because $\epsilon$ is an absolute regularization added to a quantity
quadratic in the data, the flag is not [scale-invariant](/properties/scale-invariance.md): a single
step in otherwise constant data is flagged only if its height exceeds about $5.4\times10^{-3}$
($\epsilon=10^{-4}$) or $1.7\times10^{-2}$ ($\epsilon=10^{-3}$) in the units of the examined
variable.)* Fu (2023, §3.4) describes $\epsilon$ as "also" functioning "as a cut-off on the stencil
smoothness"; Fu (2019b) does not discuss it.

## The hybrid it drives (Fu 2019b)

Where $\mathrm{Flag}_i=0$ the flux is "the fifth-order Lax-Friedrichs scheme without characteristic
decomposition" (§5, Eq. (5.1)), applied component-wise to the conserved variables,

$$\hat f^{\mathrm{lin}}_{i+1/2}=\tfrac1{60}\big(f_{i-2}-8f_{i-1}+37f_i+37f_{i+1}-8f_{i+2}+f_{i+3}\big)-\tfrac a{60}\big(u_{i+3}-5u_{i+2}+10u_{i+1}-10u_i+5u_{i-1}-u_{i-2}\big),$$

with $a$ the maximum wave speed "over the entire computational domain" (the paper prints the last
term of the central part as $f_{i+2}$; see the Source page). Where $\mathrm{Flag}_i=1$ it is the
TENO6 flux in characteristic variables, with Roe-averaged eigenvectors and Rusanov splitting per
field ([characteristic decomposition](/methods/characteristic-decomposition.md); Algorithm 1).
*(Compiler check, not in the sources: Eq. (5.1) is term by term the fifth-order upwind flux
$\tfrac1{60}(2f^+_{i-2}-13f^+_{i-1}+47f^+_i+27f^+_{i+1}-3f^+_{i+2})$ plus its mirror for $f^-$, with
the global Lax–Friedrichs splitting $f^\pm=\tfrac12(f\pm au)$; the TENO6 of the same paper restores
instead a fourth-order dispersion-optimized linear scheme (§2.2.3), so smooth regions see a different
scheme from TENO6's own linear limit.)* Details, evidence and cost are on
[hybrid schemes](/methods/hybrid-weno.md).

## Variants

- **Eight points, six equal stencils** ([Liang & Fu (2024b)](/sources/liang-2024-b.md), §3.1,
  Eqs. 31–34). For the hybrid TENO-S scheme ([hybrid schemes](/methods/hybrid-weno.md)) six
  three-point stencils of equal size cover $x_{i-3},\dots,x_{i+4}$: the three classical ones,
  $S_0=\{i-1,i,i+1\}$, $S_1=\{i,i+1,i+2\}$, $S_2=\{i-2,i-1,i\}$, and three that do not contain $x_i$,
  $S_3=\{i+1,i+2,i+3\}$, $S_4=\{i-3,i-2,i-1\}$, $S_5=\{i+2,i+3,i+4\}$ (source numbering, TENO's). Each
  $\beta_k$ is the Jiang–Shu integral over the target cell; their $\beta_3$ (Eq. 31) is Fu (2019b)'s
  Eq. (4.1), printed inside absolute-value bars, which are redundant because the form is a sum of
  integrals of squares *(compiler check, not in the sources)*. Then $\gamma_k=1/(\beta_k+\epsilon)^6$,
  $\chi_k=\gamma_k/\sum_l\gamma_l$, and the cell is smooth iff $\chi_k>10^{-6}$ for all six $k$, with
  $\epsilon=10^{-4}$ in 1D and $10^{-2}$ in multi-D. The indicator reads conserved variables in
  physical space, density and total energy in 1D and density alone in multi-D, dimension by dimension,
  without characteristic decomposition. Equal sizes keep it cheap. The authors state that "more than
  90%" of the double-Mach cells take the non-dissipative central flux (§4.6, no count shown) and call
  the indicator "more universal" than physical sensors such as Ducros' (§3.1), without a comparison.
  Against Fu (2019b) it uses six equal stencils instead of four equal ones and a threshold $10^{-6}$
  instead of $5\times10^{-4}$.
- **Compact DG form** ([Huang & Fu (2024)](/sources/huang-2024.md), §4.3, Eqs. 32–35; §5.1). For
  RKDG the candidates are the DG polynomials of $I_{i-1}$, $I_i$, $I_{i+1}$ themselves,
  $\beta_n=\sum_{l=1}^{2}\int_{I_n}\Delta x^{2l-1}\big(\partial_x^lu_h\vert_{I_n}\big)^2dx$,
  $\gamma_n=1/(\beta_n+\epsilon)^q$ with $\epsilon=10^{-3}$, $q=6$, $\chi_n=\gamma_n/\sum_l\gamma_l$, and
  cell $i$ is troubled iff its own $\chi_i<C_T=10^{-4}$; only the target's flag is tested. The authors
  present it as a compact version of Fu (2019b)'s indicator, "which needs four candidate stencils over
  six points". The same constants serve all their tests "without tuning". It drives their
  TENO-weighted limiter ([WENO limiters for DG](/methods/weno-limiter-dg.md)).
  [Huang et al. (2025a)](/sources/huang-2025.md) (§3.1, Eqs. (11)–(14); §4.1, Eq. (26)) reuse it with
  the same constants for their TENO-THINC limiter, evaluated on each local characteristic variable,
  with all three integrals printed over the target cell $I_i$
  ([troubled-cell indicators](/definitions/troubled-cell-indicator.md), Qualifications).
- **Direction-wise spectral-difference form** ([Chen & Fu (2024)](/sources/chen-2024.md), §4.2,
  Eqs. (15)–(20)). The candidates are again the cells' own polynomials on $I_{i-1}$, $I_i$,
  $I_{i+1}$, with Jiang–Shu indicators of all derivatives up to the degree,
  $\gamma_k=1/(\beta_k+\epsilon)^6$, and the cell is smooth only if $\chi_k>C_k$ for **all three** $k$,
  with $\epsilon=10^{-4}$, $C_k=10^{-5}$ in 1D and $\epsilon=10^{-3}$, $C_k=5\times10^{-4}$ in 2D
  (page-local $C_k$), $x$ and $y$ flags independent ([spectral difference method](/methods/spectral-difference-method.md)).
- **Location detectors from TENO5 flags.** Takagi et al. (2022) and Liang et al. (2022) do not
  threshold $\chi_k$ but read patterns of the TENO5 flags $\delta_k$ of neighbouring cells to locate a
  discontinuity for [TENO-THINC](/methods/teno-thinc.md); they are recorded on
  [troubled-cell indicators](/definitions/troubled-cell-indicator.md).

## Uses beyond the original hybrid

Fu (2023, §3.4) lists the reuse of the indicator in steepness-adjustable, minimized-dispersion and
artificial-viscosity hybrids ([targeted ENO](/methods/targeted-eno.md)).
[Li, Chen & Ren (2022a)](/sources/li-2022.md) (§3.2, Eqs. (55)–(57); §4) run Fu's hybrid, TENO-HY, as
a comparator of their [MDCD](/methods/mdcd-scheme.md)-type MDAD-HY, with $\epsilon=10^{-4}$ and
threshold $5\times10^{-4}$, the 1D setting of Fu (2019b).

## Evidence and positions

- **Comparison in the original.** Fu (2019b, §6) set the indicator against the
  [monotonicity-preserving](/methods/monotonicity-preserving-limiter.md) and TVB flags
  ([troubled-cell indicators](/definitions/troubled-cell-indicator.md)) on linear advection, Burgers,
  the [Sod and Lax tubes](/benchmarks/sod-and-lax-shock-tubes.md), the
  [Shu–Osher problem](/benchmarks/shu-osher-problem.md), the
  [blast waves](/benchmarks/woodward-colella-blast-wave.md),
  [2D Riemann configurations 3 and 12](/benchmarks/two-dimensional-riemann-problems.md),
  [double Mach reflection](/benchmarks/double-mach-reflection.md) and a periodic
  [implosion](/benchmarks/explosion-and-implosion-problems.md). The TENO flag and the TVB flag with
  $M_{\mathrm{TVB}}=10$ (page-local TVB constant, as on [troubled-cell indicators](/definitions/troubled-cell-indicator.md)) "perform the best" on linear advection (§6.1); on Burgers the MP flag is best,
  monotone and with fewer flags, the TENO flag marking two more cells at 100 points (§6.2); on the
  shock tubes, Shu–Osher, the Riemann problems and the implosion the TENO flag marks fewer cells than
  the MP flag, and it separates the Shu–Osher entropy waves from the shocklets at 200–800 points, with
  a troubled fraction that falls under refinement (§6.3–6.4, §6.6, §6.8, Figs. 9–11, 20–21, 27, 29).
  The TVB flag depends strongly on $M_{\mathrm{TVB}}\in\{10,100,1000\}$ (Figs. 15, 22–23, 28). More than 98 % of the cells of both Riemann configurations, more than 90 % of
  double Mach reflection and more than 97 % of the implosion take the linear flux (§6.6–6.8).
- **Sensitivity.** On Shu–Osher at 400 points, $\epsilon=10^{-3},10^{-4},10^{-5}$ and
  $C_T=5\times10^{-3},5\times10^{-4},5\times10^{-5}$ give similar flag histories (Figs. 13–14); "both
  the numerical simulation and the spectral analysis reveal that the separating wavenumber does not
  change significantly even when $C_T$ changes by a magnitude of one order" (§6.4).
- **Spectral argument.** The evidence that $C_T$ acts in wavenumber space is Fig. 2, reproduced from
  Fu et al. (2016): the approximate dispersion relation of **five-point** TENO with
  $C_T=10^{-7},\dots,10^{-1}$ ([approximate dispersion relation](/definitions/approximate-dispersion-relation.md)).
  It is not an analysis of this indicator, whose measure has no $\tau_K$, a different $\epsilon$ and
  six points.
- **Against physical sensors.** Fu (2023, §3.4) calls the indicator "more universal" than physical
  sensors such as Ducros' ([Ducros sensor](/definitions/ducros-shock-sensor.md)), because it separates
  non-smooth scales in spectral space; Liang & Fu (2024b, §3.1) repeat the claim. Neither shows a
  comparison.
- **On sine waves.** Li, Chen & Ren (2022a, §3.2, Figs. 9–10) find the flag correct on sine waves only
  below $\vartheta=0.64$, against 2.06 for their modified Ren detector, and normalize the detector
  inputs by $\max(\lvert f_{\max}\rvert,1)$, after which TENO-HY detects "obviously better" on double
  Mach reflection than in Fu's own paper (§4.3.1); TENO-HY and the optimized TENO6 fail on Sedov "even
  with $C_T=0.1$" (§4.2). The measured 0.64 agrees with the compiler check above.

## Qualifications

- **Two-dimensional rule as recalled.** [Huang & Fu (2024)](/sources/huang-2024.md) (§5.1) label a
  cell troubled when it is flagged "in either one or both directions" and state that "this strategy
  has been adopted in [55]", Fu (2019b), "for developing the hybrid TENO scheme". The original names
  $\max(\mathrm{Flag}_x,\mathrm{Flag}_y)$ only as an optional remedy and runs with separate flags
  (§6, Figs. 18–28). Recorded as a recollection that differs from the original, not as a
  contradiction (compiler's ruling, chunk 14).
- **"Fixed set of parameters".** Fu (2019b) states that the algorithm performs better "with a fixed
  set of parameters for all considered benchmarks" (Abstract, §7), while $\epsilon$ is $10^{-4}$ in 1D
  and $10^{-3}$ in multi-D (§4.2), the flux splitting of the TENO6 branch changes to Roe with entropy
  fix on the blast waves (§6.5), and the MP and TVB comparison flags read total energy as well on
  configuration 3 "for numerical robustness" (Figs. 20, 23). Liang & Fu (2024b) and Huang & Fu (2024)
  make the same claim in the same sense: fixed across the authors' tests.
- **Linear branch as recalled.** Fu (2023, §3.4, Eq. (24)) recalls the linear branch as "the optimal
  linear scheme without characteristic decomposition" and the gain as "a factor of four"; the original
  linear branch is the fifth-order upwind flux of Eq. (5.1), not TENO6's optimal linear scheme, and
  the measured gain is 3.2–3.84 (Table 1; [hybrid schemes](/methods/hybrid-weno.md)).
- The threshold $C_T$ of the indicator is not the cut-off of a TENO scheme: TENO6 in the same paper
  uses $C_T=10^{-6}$ (§2.2.3), and the indicator $5\times10^{-4}$.

# Citations

- [Fu (2019b)](/sources/fu-2019-b.md) — Abstract; §1; §4, Eqs. (4.1)–(4.4), Figs. 2–3; §5, Eqs. (5.1)–(5.2), Algorithm 1; §6, Figs. 4–29, Table 1; §7: the original indicator, its hybrid and its tests.
- [Fu (2023)](/sources/fu-2023.md) — §3.4, Eqs. (21)–(24), Fig. 7: recollection, "more universal", reuse.
- [Li, Chen & Ren (2022a)](/sources/li-2022.md) — §3.2, Eqs. (55)–(57), Figs. 9–12; §4.2; §4.3.1: TENO-HY assessed.
- [Liang & Fu (2024b)](/sources/liang-2024-b.md) — §3.1, Eqs. (31)–(34); §4.6: eight-point, six-stencil variant.
- [Huang & Fu (2024)](/sources/huang-2024.md) — §4.3, Eqs. 32–35; §5.1: compact DG variant; two-dimensional rule.
- [Huang et al. (2025a)](/sources/huang-2025.md) — §3.1, Eqs. (11)–(14); §4.1, Eq. (26): reuse in a TENO-THINC DG limiter.
- [Chen & Fu (2024)](/sources/chen-2024.md) — §4.2, Eqs. (15)–(20): spectral-difference variant.
