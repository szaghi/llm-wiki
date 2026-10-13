---
type: Source
title: "Irsalinda, Bakar, Harun, Idris & Surono (2026) — A dynamic mesh refinement in Physic-Informed Neural Networks for handling Stiff Partial Differential Equations"
description: "Residual-driven adaptive resampling of PINN collocation points (Aug-MR PINN), called mesh refinement but outside the bundle's AMR sense, with no divergence content; its comparison table does not match its own result tables, its baselines get smaller point budgets, its convergence lemma assumes its conclusion, and it reports losses but no errors or costs."
resource: "doi:10.1016/j.aej.2025.11.041"
source_kind: paper
authors: [Irsalinda N., Bakar M.A., Harun F.N., Idris R., Surono S.]
year: 2026
venue: "Alex. Eng. J. 134:1–20"
local_file: "/home/stefano/papers/mosaic/div-free-amr/2026-AlexEngJ-Irsalinda-101016jaej202511041.pdf"
tags: [pinn, adaptive-sampling]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper proposes "Augmented Mesh Refinement PINN" (Aug-MR PINN):
**adaptive resampling of the collocation points** of a physics-informed
neural network. "Mesh refinement" here does **not** mean mesh refinement
in the bundle's sense. There are no cells, faces, levels, nesting,
refinement ratio, transfer operators or conservation constraints. The
network is a global function of space and time, so "refinement" only
changes where the loss is sampled. The paper has **no divergence-constraint
content**: no $\nabla\cdot B$ or $\nabla\cdot u$ constraint is posed or
discussed. (The azimuthal velocity of its flow-mixing test, eq. 30, is
solenoidal; the paper never mentions or uses this.)

It is recorded as out of scope for the bundle's concept pages. Its
"AMR" vocabulary relates to [block-structured AMR](/definitions/block-structured-amr.md)
by name only. The one shared idea, flagging by an indicator, loosely
mirrors error-estimation flagging; here the indicator is a PINN residual and
the flagged objects are sample points. The AMReX citation
([Zhang et al. (2019)](/sources/zhang-2019.md), ref. 19) serves only as a
generic definition of AMR in the introduction. The paper's "Adam" is the
stochastic optimizer, not the [ADAM](/software/adam.md) code.

# Key claims

1. **Point sets** (§4, Defs. 1–2, Fig. 3, Algorithm 1). A coarse "training
   domain" $\Omega_t$ of collocation points is enriched from a denser
   "dummy domain" $\Omega_d$ restricted to "stiff regions". Defs. 1–2 set
   both as uniform lattices on $[0,1]^2$. The tests run on $[-1,1]$,
   $[0,1]$ and $[-4,4]^2$, and §3 says points are "randomly distributed
   within the domain", so the definitions do not describe the tested
   point sets.
2. **Indicators** (§4, eqs. 18–20). Gradient magnitude, curvature and the
   PDE residual are listed. Only the residual is used (§5.1). Eq. 20
   writes the residual in reaction–diffusion form with the coefficients
   undefined; it matches none of the test PDEs.
3. **Refinement rules** (Assumption 2, §§5.1–5.2). A threshold rule
   (residual above $\tau$) and a percentile rule (keep the $p$-th
   percentile of lowest-residual points; the rest are enriched from
   $\Omega_d$ in their "local neighborhoods"). Tested: $p \in \{70, 80, 90\}$;
   $\tau$ from 0.5 to 0.0001 (Burgers), $10^{-3}$ to $10^{-5}$ (telegraph),
   $5\times10^{-7}$ to $5\times10^{-6}$ (flow mixing); pools of 10,000 or
   20,000 points; an update every 100 Adam iterations.
   **Replace or add.** Assumption 2 and §6.1 say points are replaced. The
   tables ("Last Point" grows from 5,000 to 23,000 and from 2,500 to
   147,546), §5.2 ("supplemented with an additional 30%") and the
   future-work remark ("replacing rather than adding training points")
   show they are added. The lemma (claim 5) is stated for a procedure
   other than the one tested.
4. **Set-up** (§3, §5.4). Tanh networks, Adam at learning rate 0.001,
   unweighted loss $MSE_0 + MSE_b + MSE_{\mathcal F}$. Burgers 4×20 with
   5,000 points; telegraph 4×20 with 2,500; flow mixing 5×50 with 2,500.
   Iteration counts differ between tables and text (flow mixing: 500 in
   Tables 6–7, 200 in §5.4). TensorFlow is named; there is no code or data
   availability statement.
5. **"Convergence guarantee"** (§6.2, Lemma 1, Corollary 1). Lemma 1 bounds
   the expected residual loss on the enriched set by $(1-\mu)$ times the
   old loss minus $\eta$ times the mean squared bad-set residual. The
   four-line argument assumes per-phase multiplicative loss descent
   (Assumption 3), which is the conclusion, and never relates the loss on
   the new point set to that on the old one. $\eta$ is never constructed.
   Assumption 2.3 bounds the residuals of refinement points from *below*,
   which works against a decrease. **This is not a proof**; the claim is
   at most a hypothesis. Corollary 1 recommends $\tau \approx 10^{-3}$,
   while the flow-mixing runs used $\tau \sim 10^{-6}$.
6. **Headline claims** (abstract, §§5.3–5.5, §7). Lower loss than PINN,
   R-PINN, X-PINN and "AMR-FEM"; threshold "more efficient" than
   percentile; "enhances computational efficiency". The paper's own data
   do not support them (next section).

## Unsupported or contradicted claims

* **Table 8 does not match Tables 2–7.** Burgers, Aug-MR (70%), 3.616e−04,
  appears in no table. Burgers "0.00001", 1.643e−05, is Table 3's
  *validation* loss for $\tau = 10^{-4}$; the Burgers runs never used
  $\tau = 10^{-5}$. Telegraph 70%, 5.120e−04, is the validation loss of the
  10,000-point row of Table 4; the better 20,000-point row (2.318e−05) is
  not reported. Telegraph "0.00001", 6.990e−04, is the validation loss for
  $\tau = 10^{-4}$ in Table 5 (the $\tau = 10^{-5}$ value is 3.159e−04).
  Flow mixing, 5.289e−05 and 1.799e−05, appear in neither Table 6 nor
  Table 7, whose losses are $O(10^{-6})$–$O(10^{-7})$. Table 8 mixes
  training and validation losses, mislabels thresholds and contains
  untraceable numbers.
* **Unequal budgets.** Baselines keep 5,000 or 2,500 points; Aug-MR ends
  with up to 23,000 (Burgers), 147,546 (telegraph) or 32,500 (flow mixing).
  "Consistency in key parameters" (§5.4) holds only for the initial points.
  With 200–600 Adam iterations the baselines are unconverged (a PINN
  Burgers loss of 1.584e−01). The comparison measures sample budget and
  training length, not the refinement criterion.
* **Loss is not error.** Apart from flow-mixing absolute-error plots
  (Fig. 13) and qualitative contours, no error against a reference is
  reported: no $L^2$ or relative error, no convergence study in point
  count. For the telegraph equation "the exact solution is unknown"
  (§5.2), yet the AMR-FEM solution is said to show "numerical dissipation
  and phase errors" (§5.5). The "Absolute Residual" figures (Figs. 14, 16)
  show PDE residuals, while §5.4 defines "Absolute Residual Error" as
  observed minus predicted.
* **AMR-FEM is unspecified.** No element, indicator, mesh size,
  integrator, software or definition of its "loss value" (Table 9). A loss
  of 3.046e+00 for smooth linear advection of a tanh profile points to a
  broken or unstabilized baseline. The superiority claim over AMR-FEM is
  unsupported.
* **"Threshold beats percentile" fails for the telegraph equation.**
  Threshold losses (Table 5) are 2.6e−03 to 4.4e−03 against 3.212e−04 for
  the percentile rule (Table 4, 20,000 points, 70%). The two tables also
  use different boundary-point and iteration counts (300 and 500 against
  75 and 600). Table 8 itself picks the percentile run as best there.
* **No cost data.** No wall-clock, epoch or FLOP figures anywhere; the
  efficiency claims rest on nothing. The authors concede that refinement
  "inevitably extends computational time" (§§5.3, 6.1, 7).
* **"Stiff" is asserted, not shown.** No eigenvalue or timescale ratio is
  computed. Flow mixing is linear advection with a smooth field; Burgers at
  $\nu = 0.01/\pi$ is a steep-front problem, not stiff in the paper's own
  §2 (Jacobian-eigenvalue) sense.
* **Single runs.** No seeds, repetitions or variances are reported.

# Tests

| § | Problem | Set-up | Best result (as printed) |
|---|---|---|---|
| 5.1 | Viscous Burgers, $\nu = 0.01/\pi$, $x \in [-1,1]$, $u(x,0) = -\sin\pi x$ | 5,000 points, 100 boundary points; Table 2 percentile (300 iter.), Table 3 threshold (200 iter.) | percentile: loss 1.766e−04 (val 6.250e−05), $p = 70$, 20k pool, 23,000 points; threshold: $\tau = 10^{-4}$, loss 1.212e−04 (val 1.643e−05), 19,015 points |
| 5.2 | Damped telegraph equation, Neumann BC | 2,500 points; Table 4: 75 boundary points, 600 iter.; Table 5: 300 and 500 | percentile: 3.212e−04 (val 2.318e−05), 74,500 points; threshold: 2.607e−03 (val 3.159e−04) at $\tau = 10^{-5}$, 147,546 points. **The equation's constants are never given and there is no reference solution.** |
| 5.3 | Rotational flow mixing (linear advection) on $[-4,4]^2$, exact tanh solution | 2,500 points, 50 boundary points, 500 iter. | percentile: 2.12e−6 (val 2.46e−7); threshold: 2.63e−6 (val 2.45e−7) at $\tau = 5\times10^{-7}$ |
| 5.4–5.5 | PINN, R-PINN, X-PINN, "AMR-FEM" | AMR-FEM not specified | Tables 8–9; see above |

# Notation map

The paper shares no mathematical object with the registry. The map only
blocks false identifications.

| Irsalinda et al. (2026) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Omega_t$, $\Omega_d$ (point sets) | none | not grid levels $\Omega_h$; no nesting, no $r$, no $P$/$R$ |
| $\Delta x_t$, $\Delta x_d$ (lattice spacings) | none | not $H$/$h$; no fixed ratio |
| $r$ (telegraph constant; radius in eq. 31) | none | collides with the refinement ratio $r$ |
| $R(x;\theta)$ (PINN residual), $R(u)$ (reaction term) | none | collide with the restriction $R$ |
| $D$ (diffusion coefficient, eq. 20) | none | collides with $D_h$ |
| $\tau$ (threshold), $p$ (percentile; also a telegraph constant) | none | paper-local |
| $h_{\min}$, $h_{\max}$ (separation and fill distance) | none | scattered-data notions, not grid spacing $h$ |

# Pages created or updated

None. No concept page is touched: the method is residual-based adaptive
collocation sampling for PINNs, outside the bundle's scope (divergence
constraints and AMR interfaces). It has no cells, transfer operators or
fluxes, so it neither agrees with, extends nor contradicts any AMR page.
It also does not benchmark against the residual-based adaptive sampling
methods it cites (refs. 9, 21), so its named contribution would not earn a
page even in scope.

# Citations

1. `~/papers/mosaic/div-free-amr/2026-AlexEngJ-Irsalinda-101016jaej202511041.pdf`.
   * **Version.** The published version of record, 20 pages, open access
     (CC BY-NC-ND). Received 17 Feb 2025, accepted 23 Nov 2025, online
     4 Dec 2025.
   * **Identity.** doi:10.1016/j.aej.2025.11.041, printed on page 1 and
     checked on Crossref: Alex. Eng. J. 134:1–20, January 2026. Page 1 and
     Crossref list five authors (Irsalinda, Bakar, Harun, Idris, Surono).
     "Physic-Informed" is the printed title's spelling.
   * **How it was read.** Text extraction, all sections. Pages 3, 4, 6, 8,
     14 and 18 were rendered for eqs. 9, 12–17, 25–35, Assumption 2,
     Def. 3 and Lemma 1. Figures 2–18 were not read for numbers.
   * **Printed errors.**
     * Eq. 17 prints $\theta^{l+1} = \theta^{l} + \alpha_l \nabla\mathcal{L}(\theta)$,
       gradient ascent (a sign error).
     * Eq. 14 drops the chain-rule weight factors (illustrative network
       only; the one-hidden-layer, two-neuron network of Fig. 1 is not the
       one used).
     * Eq. 31 prints $v_t = \sec^2(r)\tanh(r)$, singular at $r = \pi/2$
       inside $[-4,4]^2$. The stated $v_{t\max} = 0.385$ equals
       $\max_r \mathrm{sech}^2(r)\tanh(r) = 2/(3\sqrt3) \approx 0.3849$, so
       $\mathrm{sech}^2$ is evidently intended.
     * Eq. 26 prints $v(x,0) = e^{-3(x/0.2 - 1)}$, monotone, not "centered
       around a specific point" as the text says; a missing square cannot
       be confirmed from the paper.
     * Fig. 9's caption says "DMR PINN"; captions and text alternate
       between $\tau = 0.0001$ and $0.00001$ for the same runs; §5.3 cites
       Fig. 9 for results in Fig. 10, and Fig. 12 twice where the second is
       Fig. 13.
   * **Not reproducible from the paper:** the telegraph constants, the
     source of the Burgers "exact solution", the AMR-FEM set-up, how
     $\Omega_d$ points are drawn, whether boundary points are refined, the
     validation set, seeds and repetitions.
   * **Reference list:** 50 entries, merged; no DOIs printed. Wang et al.
     (2023, curriculum learning of PINNs) is `wang-2023-b`, distinct from
     the existing `wang-2023`. AMReX ([Zhang et al. (2019)](/sources/zhang-2019.md))
     and `crank-1947` are existing entries. The list cites the Crank–Nicolson
     paper twice (refs. 37–38, the 1947 original and its 1996 reprint).
