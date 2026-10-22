---
type: Definition
title: "ENO property"
description: "A reconstruction has the ENO property when, near a discontinuity, it effectively draws only on candidate stencils that do not cross it, so the solution is captured essentially non-oscillatorily; for weighted schemes this means the weights of discontinuous stencils vanish asymptotically, a condition that a too-large or absolute ε can silently defeat."
status: established
aliases: [ENO-property, essentially non-oscillatory property, ENO condition]
tags: [reconstruction, weno, teno, limiting]
timestamp: 2026-10-22T12:00:00Z
---

# ENO property

ENO schemes (Harten et al., as recalled by Takagi et al. 2022, §1, Fu 2023, §2.3 and Deng 2023, §1)
pick, among the candidate stencils, the one on which the data are smoothest, so the reconstruction
never interpolates across a discontinuity. A weighted reconstruction has the **ENO property** when it
reproduces this behaviour through its weights: the weight of a candidate stencil that contains a
discontinuity tends to zero, while on smooth stencils the weights tend to the linear ones. Luo & Wu
(2021, §1) state the design principle: "the weights of the discontinuous substencils are designed to
be asymptotically small. This design is why WENO schemes have the ENO property." For the compact
third-order scheme, Deng (2023, §4.3) and Huang et al. (2026, §3.1) write the condition as
$\omega_k\to0$ if and only if stencil $k$ contains a discontinuity.

The property is not a sharp mathematical statement in the bundle's sources. Wang & Don (2022, §3)
use an operational diagnosis: point-wise errors that decay monotonically and exponentially away from
the singularity, against Gibbs-type oscillations when the property is lost.

## How weight designs realize it

- **Smoothness indicators.** A stencil crossed by a jump has $\beta_k=O(1)$ against $O(\Delta x^2)$
  for smooth stencils, and the weights of [WENO-JS](/methods/weno-js-reconstruction.md) and
  [WENO-Z](/methods/weno-z.md) decrease with $\beta_k$
  ([smoothness indicators](/definitions/smoothness-indicator.md)).
- **WENO-ZN.** Li et al. (2022, §3.3(2)) argue that $S_0$ and $S_{r-1}$ cover the global stencil
  without overlap, so any discontinuity falls in one of them; then the adaptive term of the weights is
  small and the ranking by $\beta_k$ takes over. This is a heuristic argument, not a theorem
  ([WENO-ZN](/methods/weno-zn.md)). Li et al. leave WENO-Z$\eta$ and the WENO-Z of Don & Borges with
  $\epsilon=\Delta x^m$ out of their comparison because they "cannot keep the ENO property well".
- **WENO-Z+.** Luo & Wu (2021, §2.3) recall that Acker et al. proved the ENO property of WENO-Z+ for
  an $O(1)$ coefficient of the extra term ([WENO-Z+](/methods/weno-z-plus.md)).
- **TENO.** Fu (2023, §2.3) calls TENO's sharp cut-off an "ENO-like stencil selection": a stencil is
  kept with its linear weight or dropped. It differs from ENO, which keeps only the smoothest stencil
  and cannot recover the full-stencil linear scheme, whereas TENO "tends to rule out the nonsmoothest
  stencil crossed by genuine discontinuities" ([targeted ENO](/methods/targeted-eno.md)).
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
  [learned WENO weights](/methods/learned-weno-weights.md)).

## How it is lost

The weights distinguish stencils only if $\beta_k$ dominates $\epsilon$. Wang & Don (2022, §3.2.1)
give the mechanism: for data $\sigma f+\mu$ (page-local constants) with $\sigma=10^{-7}$, $\mu=1$ and
$\epsilon=10^{-12}$, $\beta_k=O(\sigma^2)=O(10^{-14})$ is swamped by $\epsilon$ (scaled by the
scale-invariant descaler, which is $\approx|\mu|$), the weights become independent of $k$, and the
scheme reverts to the linear upwind scheme, with visible Gibbs oscillations in linear advection and
in a blast-wave problem with background pressure. Their conclusion (§3.2.2): the ENO property of a
non-affine-invariant WENO scheme can be violated when $|\sigma|\ll|\mu|$. The remedy is a relative
sensitivity parameter ([affine-invariant WENO](/methods/affine-invariant-weno.md),
[scale invariance](/properties/scale-invariance.md)).

## Beyond weights

Deng (2023, §5 IV) holds that "classical ENO constraints are not enough to ensure that reconstruction
operators can achieve the ENO property or obtain the optimal accuracy", and adds an "ENO region" to
the unified [normalised-variable diagram](/definitions/normalised-variable-diagram.md) as a
supplementary constraint on the normalized reconstruction where $\tilde u_i<0$ or $\tilde u_i>1$.
Fu (2021, Abstract; §5.7) obtains positivity and the ENO property in extreme simulations only "with
the assistant of a positivity-preserving flux limiter", i.e. the reconstruction alone is not claimed
to deliver them.

# Citations

- [Li et al. (2022)](/sources/li-2022-b.md) — §3.3(2); §4.1.
- [Wang & Don (2022)](/sources/wang-2022-b.md) — §3.2.1–3.2.2, Figs. 4–6.
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §1; §2.3.
- [Deng (2023)](/sources/deng-2023.md) — §1; §4.3; §5 IV.
- [Huang et al. (2026)](/sources/huang-2026.md) — §3.1; §3.2, Eq. (3.11).
- [Fu (2023)](/sources/fu-2023.md) — §2.3.
- [Fu (2021)](/sources/fu-2021.md) — Abstract; §5.7.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §1.
- [Liu et al. (2021)](/sources/liu-2021.md) — Abstract; §2.3; §3.1; §4; §5.
