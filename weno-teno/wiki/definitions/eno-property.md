---
type: Definition
title: "ENO property"
description: "A reconstruction has the ENO property when, near a discontinuity, it effectively draws only on candidate stencils that do not cross it, so the solution is captured essentially non-oscillatorily; for weighted schemes this means the weights of discontinuous stencils vanish asymptotically, a condition that a too-large or absolute ε can silently defeat."
status: established
aliases: [ENO-property, essentially non-oscillatory property, ENO condition]
tags: [reconstruction, weno, teno, limiting]
timestamp: 2026-10-30T07:53:00Z
---

# ENO property

Takagi et al. (2022, §1), Fu (2023, §2.3) and Deng (2023, §1) recall that ENO schemes pick, among
the candidate stencils, the one on which the data are smoothest, so that the reconstruction does not
interpolate across a discontinuity. In the founding paper the choice is made point by point by the
smallest divided differences, under the assumption that "for $h$ sufficiently small there are at least
$(r+1)$ points of smoothness between discontinuities"; Harten et al. (1987a, §2, p. 240) add that
where discontinuities interact "there are not enough points to select a stencil of $(r+1)$ points from
the region of smoothness" ([ENO reconstruction](/methods/eno-reconstruction.md)). A weighted
reconstruction has the **ENO property** when it reproduces this behaviour through its weights: the
weight of a candidate stencil that contains a discontinuity tends to zero, while on smooth stencils
the weights tend to the linear ones. Luo & Wu
(2021, §1) state the design principle: "the weights of the discontinuous substencils are designed to
be asymptotically small. This design is why WENO schemes have the ENO property." For the compact
third-order scheme, Deng (2023, §4.3) and Huang et al. (2026, §3.1) write the condition as
$\omega_k\to0$ if and only if stencil $k$ contains a discontinuity.

## Founding statements

Two founding papers state the property as an inequality.

- **Total variation (ENO).** [Harten et al. (1987a)](/sources/harten-1987.md) (Eq. (1.9c)) require
  of the reconstruction $TV(R(\cdot;\bar u))\le TV(u)+O(\Delta x^r)$, and of the scheme
  $TV(\bar u^{n+1})\le TV(u)+O(\Delta x^r)$ (Eq. (1.13b)). It "excludes a Gibbs-like phenomenon but
  allows for the production of spurious oscillations on the level of the truncation error", which
  "may occur only in the smooth part" (§2). The bound for the adaptive interpolant is proved in
  their paper II, not in this one (Eq. (3.5b)), and holds under the separation assumption above. For
  the scalar scheme they conjecture $TV(v^{n+1})\le TV(v^n)+O(\Delta x^{p+1})$, $p>0$, "based on
  heuristic analysis and extensive numerical experimentation" (Eq. (1.22)).
- **Weights (WENO).** [Liu et al. (1994)](/sources/liu-1994.md) (§3.3, Definition 1, Eq. (3.8)) say
  that a weighted reconstruction has the "ENO property" if the normalized weight of a stencil in a
  smooth region is $O(1)$ and that of a stencil in a discontinuous region is at most $O(\Delta x^r)$;
  their weights $\alpha_k=C_k/(\epsilon+\beta_k)^r$ (positive constants $C_k$, page-local) satisfy it with the bound
  $\max(O(\epsilon^r),O(\Delta x^{2r}))$ for $\epsilon=10^{-5}$, provided at least one candidate is
  smooth (Eq. (3.9)). The explicit $\epsilon^r$ term is the mechanism by which a too-large $\epsilon$
  defeats the property (see *How it is lost*).

[Jiang & Shu (1996)](/sources/jiang-1996.md) (§2, Eqs. (2.26)–(2.28)) give the weight of a
non-smooth stencil as $O(\Delta x^{2q})$ (registry $q$, their $p=2$), and add that with more than one
smooth stencil each gets an $O(1)$ weight, so the weights "do not exactly resemble the ENO digital
weights"; next to the jump of their test function they find $\omega\approx\frac17$ and $\frac67$ on the
two smooth stencils (§3, Fig. 1). [Shu (2009a)](/sources/shu-2009.md) (§2.1, p. 86) explains why the
combination stays non-oscillatory even when every substencil contains the jump: for a step in
$(x_i,x_{i+1})$ the large-stencil interpolant and the two candidates whose stencils contain $x_{i+1}$ are monotone on
$[x_i,x_{i+1}]$, and a convex combination of monotone approximations is monotone.

Wang & Don (2022, §3) use an operational diagnosis: point-wise errors that decay monotonically and
exponentially away from the singularity, against Gibbs-type oscillations when the property is lost.

## How weight designs realize it

- **Smoothness indicators.** A stencil crossed by a jump has $\beta_k=O(1)$ against $O(\Delta x^2)$
  for smooth stencils, and the weights of [WENO-JS](/methods/weno-js-reconstruction.md) and
  [WENO-Z](/methods/weno-z.md) decrease with $\beta_k$
  ([smoothness indicators](/definitions/smoothness-indicator.md)).
- **WENO-Z.** [Borges et al. (2008)](/sources/borges-2008.md) (§1, §3, Fig. 3) argue that the
  strategy "should be to augment the influence of the stencil containing the discontinuity as much as
  possible, without destroying the essentially non-oscillatory behavior": next to a jump WENO-Z gives
  the discontinuous stencils weights of about $10^{-4}$ against about $10^{-8}$ for WENO-JS, and the
  solutions stay essentially non-oscillatory.
- **WENO-ZN.** Li et al. (2022b, §3.3(2)) argue that $S_0$ and $S_{r-1}$ cover the global stencil
  without overlap, so any discontinuity falls in one of them; then the adaptive term of the weights is
  small and the ranking by $\beta_k$ takes over. This is a heuristic argument, not a theorem
  ([WENO-ZN](/methods/weno-zn.md)). Li et al. (2022b) leave WENO-Z$\eta$ and the WENO-Z of Don & Borges with
  $\epsilon=\Delta x^m$ out of their comparison because they "cannot keep the ENO property well".
- **WENO-Z+.** Luo & Wu (2021, §2.3) recall that Acker et al. proved the ENO property of WENO-Z+ for
  an $O(1)$ coefficient of the extra term ([WENO-Z+](/methods/weno-z-plus.md)).
- **TENO.** [Fu et al. (2016)](/sources/fu-2016.md) (§3.1.1, Fig. 2) argue that classical WENO
  "fails to guarantee the ENO property" when two close discontinuities cross every equal-width
  candidate of a very-high-order stencil, while the three-point candidate of TENO can still be singled
  out; with the binary cut-off the scheme reaches "arbitrarily high-order accuracy while satisfying the
  ENO property", hence the name targeted ENO (§3.1.4). Fu (2023, §2.3) calls TENO's sharp cut-off an "ENO-like stencil selection": a stencil is
  kept with its linear weight or dropped. It differs from ENO, which keeps only the smoothest stencil
  and cannot recover the full-stencil linear scheme, whereas TENO "tends to rule out the nonsmoothest
  stencil crossed by genuine discontinuities" ([targeted ENO](/methods/targeted-eno.md)).
  Hong, Ye & Ye (2022, §1) say that this ENO-like selection preserves the ENO property at
  arbitrary order; their TENO-M grows the target stencil point by point and stops at the first
  three-point extension that fails a relative-difference test between neighbouring indicators. On unstructured meshes Ji, Liang & Fu (2022, §3.3, Eqs. (24)–(28)) enforce
  the property explicitly in two steps: the large stencil is used alone if it survives the cut-off,
  otherwise the cut-off is repeated among the small stencils and the survivors are averaged with
  equal weights. *(Compiler check, not in the sources: with $K$ small stencils the largest normalized
  measure is at least $1/K>C_T=10^{-6}$, so at least one stencil always survives.)* Ji, Liang & Fu (2023, §3.2.2, Eqs. (29)–(36)) keep the two steps and use
  different cut-offs, $C_T=10^{-7}$ among all candidates and $10^{-5}$ among the small stencils, so that the second step
  "ensures the preservation of ENO property" with stronger nonlinear adaptation at discontinuities.
  Liang, Shyy & Fu's unstructured TENO-E keeps the same two-level structure, with one cut-off for both
  levels and equal weights $1/K$ among the surviving third-order directional stencils
  ([Liang et al. (2025)](/sources/liang-2025.md), §3.3.3, Eqs. (22)–(27)). In the finite-volume
  [converged ENO](/methods/converged-eno.md) scheme of [Liang & Fu (2026)](/sources/liang-2026.md)
  (§3.2.4, Eqs. (25)–(26)) the five-point stencil is used alone if it survives; otherwise the two
  two-point stencils are combined with renormalized linear weights, and a dropped two-point stencil
  is suppressed "such that the ENO property is achieved".
- **Blending with a linear reconstruction.** In the steady-state hybrid WENO-H of Wan & Xia (2022,
  §3.1), the non-smooth-region reconstruction is a blend of a CWENO-type nonlinear and a linear
  polynomial whose weights bound the blended smoothness indicator by twice an amplification factor
  times the nonlinear one; the authors state that the ENO property is kept, without a proof
  ([hybrid schemes](/methods/hybrid-weno.md)).
- **Weighted least squares.** [WLS-ENO](/methods/wls-eno.md) has no candidate stencils: a single
  least-squares fit on the whole stencil weights each neighbour row by
  $W_j=1/\big((\bar u_j-\bar u_i)^2+\epsilon h_i^2\big)$ (page-local $W_j$, $h_i$ the square root of
  the cell area; $\epsilon=10^{-2}$), which is $O(h_i^{-2})$ on smooth data and $O(1)$ across a jump
  (Liu, Zhang, Li & Shen 2021, §2.3, recalling Liu & Jiao). Liu et al. state that their
  locally divergence-free variant "retains ENO property" (§3.1, §5) and use no limiter other than a
  positivity limiter in any test (Abstract, §4). No proof or measurement of the property is given;
  *(compiler check, not in the sources: the weights reduce a row across a jump by a factor $O(h_i^2)$
  relative to smooth rows, they do not remove it)*.
- **Learned weights.** WENO3-NN appends an "ENO layer" that zeroes network weights below
  $2\times10^{-4}$ and renormalizes (Huang et al. 2026, Eq. (3.11);
  [learned WENO weights](/methods/learned-weno-weights.md)). Bezgin, Schmidt & Adams (2022, §3.2,
  Eq. (16); App. A.4), who introduced it, give the reason: a softmax output layer saturates and cannot
  return an essentially zero weight, so the network alone lets oscillations through; for a single jump
  the trained network still gives the discontinuous stencil a weight "of around $10^{-4}$" (Eq. (A.1),
  Fig. 21), which sets the cut-off at $2\times10^{-4}$. The layer is applied at test time only, is
  "similar" to the TENO cut-off, and acts only near discontinuities (A.4). Nogueira et al. (2024, §3.1, Eq. (15))
  carry the device over to their five-point WENO5-NN: network weights at or below $4\times10^{-7}$ are zeroed and
  the rest renormalized, a threshold set "following the same procedure" as Bezgin et al.; the layer is not used in
  training and "restores the ENO property", preventing small non-zero weights on discontinuous stencils (stated, no
  ablation shown). Their indicator inputs are normalized by their maximum, and near machine-zero plateaus the normalized
  input "may correspond with a non-smooth situation", so a curvature-based plateau detector bypasses the network and sets $\omega_k=d_k$
  there (§3.1).

## How it is lost

The weights distinguish stencils only if $\beta_k$ dominates $\epsilon$. Wang & Don (2022, §3.2.1)
give the mechanism: for data $\sigma f+\mu$ (page-local constants) with $\sigma=10^{-7}$, $\mu=1$ and
$\epsilon=10^{-12}$, $\beta_k=O(\sigma^2)=O(10^{-14})$ is swamped by $\epsilon$ (scaled by the
scale-invariant descaler, which is $\approx|\mu|$), the weights become independent of $k$, and the
scheme reverts to the linear upwind scheme, with visible Gibbs oscillations in linear advection and
in a blast-wave problem with background pressure. Their conclusion (§3.2.2): the ENO property of a
non-affine-invariant WENO scheme can be violated when $|\sigma|\ll|\mu|$. The remedy is a relative
sensitivity parameter ([affine-invariant WENO](/methods/affine-invariant-weno.md),
[scale invariance](/properties/scale-invariance.md)). Li, Li, Don & Wang (2023a, §2.5, Fig. 4) separate the two ingredients on the
Lax problem scaled by $\sigma$ (page-local scaling, the source's $\lambda$): with $\sigma=1$ a new
higher-order global indicator alone removes the oscillations of the multi-resolution A-WENO scheme,
with $\sigma=10^{-7}$ it does not, and only the relative $\epsilon$ restores the ENO behaviour: "the
ENO-property of the solution cannot be satisfied by using the new $\tau^*$ alone"
([multi-resolution WENO](/methods/multi-resolution-weno.md)).

**Inside a captured shock.** The property presupposes that some candidate stencil is free of the
discontinuity. [Ren et al. (2025)](/sources/ren-2025.md) (§4.1.3, Table 3, Fig. 20) point out that inside the
numerical structure of a captured shock, whose intermediate cells carry states between the pre- and
post-shock values, every three-point substencil of fifth-order WENO contains the jump, so all weights
stay $O(1)$: for a left state next to a planar Mach 20 normal shock reconstructed with the HLL flux,
the finite-volume [WENO-Z](/methods/weno-z.md) weights are $(\omega_0,\omega_1,\omega_2)=(0.21135,0.62458,0.16407)$,
and the authors say the reconstruction loses the ENO property there. They also find, by
[matrix stability analysis](/methods/matrix-stability-analysis.md), that reconstructing these faces
with the single smoothest quadratic (the ENO choice) is still unstable, whereas a constant
(first-order) reconstruction on the faces next to the shock restores stability (§4.1.3, Figs. 21–22); they conclude
that high-order schemes should degenerate to zeroth-degree polynomials near shocks, and build MR-WENO-SD
on it ([multi-resolution WENO](/methods/multi-resolution-weno.md),
[carbuncle phenomenon](/definitions/carbuncle-phenomenon.md)).

A learned weight function can lose the property in a second way, by construction rather than by
scaling: Bezgin et al. (2022, §3.2, App. A.4, Fig. 21) report that without the ENO layer WENO3-NN
reconstructs negative densities or pressures in the interacting blast waves.

## Beyond weights

Deng (2023, §5 IV) holds that "classical ENO constraints are not enough to ensure that reconstruction
operators can achieve the ENO property or obtain the optimal accuracy", and adds an "ENO region" to
the unified [normalised-variable diagram](/definitions/normalised-variable-diagram.md) as a
supplementary constraint on the normalized reconstruction where $\tilde u_i<0$ or $\tilde u_i>1$.
Fu (2021, Abstract; §5.7) obtains positivity and the ENO property in extreme simulations only "with
the assistant of a positivity-preserving flux limiter", i.e. the reconstruction alone is not claimed
to deliver them.

# Citations

- [Harten et al. (1987a)](/sources/harten-1987.md) — §2, pp. 239–240; Eqs. (1.9c), (1.13b), (1.22), (3.5b).
- [Liu et al. (1994)](/sources/liu-1994.md) — §3.3, Definition 1, Eqs. (3.8)–(3.9).
- [Jiang & Shu (1996)](/sources/jiang-1996.md) — §2, Eqs. (2.26)–(2.28); §3, Fig. 1.
- [Shu (2009a)](/sources/shu-2009.md) — §2.1, p. 86.
- [Borges et al. (2008)](/sources/borges-2008.md) — §1; §3, Fig. 3.
- [Fu et al. (2016)](/sources/fu-2016.md) — §3.1.1, Fig. 2; §3.1.4.
- [Li et al. (2022b)](/sources/li-2022-b.md) — §3.3(2); §4.1.
- [Wang & Don (2022)](/sources/wang-2022-b.md) — §3.2.1–3.2.2, Figs. 4–6.
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §1; §2.3.
- [Deng (2023)](/sources/deng-2023.md) — §1; §4.3; §5 IV.
- [Huang et al. (2026)](/sources/huang-2026.md) — §3.1; §3.2, Eq. (3.11).
- [Fu (2023)](/sources/fu-2023.md) — §2.3.
- [Fu (2021)](/sources/fu-2021.md) — Abstract; §5.7.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §1.
- [Liu et al. (2021)](/sources/liu-2021.md) — Abstract; §2.3; §3.1; §4; §5.
- [Bezgin, Schmidt & Adams (2022)](/sources/bezgin-2022.md) — §3.2, Eq. (16); App. A.4, Eqs. (A.1)–(A.3), Fig. 21.
- [Hong, Ye & Ye (2022)](/sources/hong-2022.md) — §1; §3.2–3.3.
- [Ji, Liang & Fu (2022)](/sources/ji-2022.md) — §3.3, Eqs. (24)–(28); §3.4.
- [Wan & Xia (2022)](/sources/wan-2022.md) — §3.1, Eqs. (3.8)–(3.13).
- [Li, Li, Don & Wang (2023a)](/sources/li-2023.md) — §2.5, Fig. 4.
- [Nogueira et al. (2024)](/sources/nogueira-2024.md) — §3.1, Eqs. (12)–(15).
- [Ji, Liang & Fu (2023)](/sources/ji-2023.md) — §3.2.2, Eqs. (29)–(36).
- [Ren et al. (2025)](/sources/ren-2025.md) — §4.1.3, Table 3: all WENO-Z weights $O(1)$ inside the numerical shock structure; ENO choice still unstable.
- [Liang et al. (2025)](/sources/liang-2025.md) — §3.3.3, Eqs. (22)–(27): two-level unstructured TENO-E selection.
- [Liang & Fu (2026)](/sources/liang-2026.md) — §3.2.4, Eqs. (25)–(26): prioritized CENO reconstruction.
