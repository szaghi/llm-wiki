---
type: Method
title: "Positivity-preserving flux limiters (high/low-order flux blending)"
description: "Limit each interface flux towards a first-order positivity-preserving flux, with a blending factor chosen so the forward-Euler update stays admissible: the Hu–Adams–Shu cut-off limiter, the parameterized limiter of Christlieb et al. for MHD, and the PCP hybridization of Balsara et al."
status: established
aliases: [cut-off flux limiter, parametrized flux limiter, PCP flux hybridization, HAS limiter]
tags: [positivity, limiter, mhd]
timestamp: 2026-10-13T00:00:00Z
---

# Positivity-preserving flux limiters

**Idea.** Keep the high-order scheme and limit only those fluxes that
would push a cell out of $\mathcal{G}$:
$$\hat f_{i+1/2} = \theta_{i+1/2}\,\hat f^{\mathrm{HO}}_{i+1/2} + \left(1 - \theta_{i+1/2}\right)\hat f^{\mathrm{LO}}_{i+1/2},\qquad 0 \le \theta_{i+1/2} \le 1,$$
where $\hat f^{\mathrm{LO}}$ is a first-order positivity-preserving flux.
The limited flux is a convex combination of two consistent fluxes, hence
consistent and conservative ([Hu, Adams & Shu (2013)](/sources/hu-2013.md), §2.3).
The root is flux-corrected transport and the maximum-principle-preserving
flux limiters ([Christlieb et al. (2016)](/sources/christlieb-2016.md), §1).

## Hu–Adams–Shu cut-off limiter

Write the forward-Euler update as
$$\bar u^{n+1}_i = \tfrac12\left(\bar u^n_i + \tfrac{2\Delta t}{h}\hat f_{i-1/2}\right) + \tfrac12\left(\bar u^n_i - \tfrac{2\Delta t}{h}\hat f_{i+1/2}\right) = \tfrac12 u^-_i + \tfrac12 u^+_i,$$
so positivity of both halves suffices. The Lax–Friedrichs flux with the
maximal speed makes both halves positive for CFL $\le 1/2$ (eq. 13).
Limiting first for density, then for pressure, each cell proposes a
factor from $(1 - \theta)\,g(u^{\mathrm{LO},\pm}_i) + \theta\, g(u^\pm_i) = \epsilon_{\mathcal{G}}$
($g = \rho$, then $p$), and the interface takes the smaller of its two
cells' factors. The floor is $\epsilon_{\mathcal{G}} = \min\{10^{-13}, g^0_{\min}\}$,
with $g^0_{\min}$ the minimum of $g$ in the initial data
([Hu, Adams & Shu (2013)](/sources/hu-2013.md), §2.2; checked on the
page images).

**Accuracy is shown a posteriori**: under the extra condition
CFL $\le \sigma/2$, for a constant $0 < \sigma < 1$ (eq. 20), the limiter
changes the flux by no more than the high-order flux's own truncation
error (one power of $h$ above the order of the scheme) for smooth
solutions with $g$ bounded below by a positive constant (§2.3). The condition is weaker than the $\hat w_1$
bounds of the [scaling limiter](/methods/positivity-preserving-scaling-limiter.md),
and the limiter applies to any conservative FV or FD scheme. On
advection of $1 + 10^{-6} + \cos 2\pi x$ with WENO5 at the maximal
admissible CFL $0.5$ it is less accurate than the Zhang–Shu limiter;
at $1/12$ it is as accurate, and below that more accurate, since its
error keeps decreasing with $\Delta t$ (§2.4, Fig. 1). In 2D the update
splits into $x$ and $y$ parts with partition weights summing to 1
(equal halves as in Zhang–Shu, or speed-weighted), dimension by dimension (§2.5).
Tested with WENO5 on near-vacuum problems and with WENO-CU6-M1
([central-upwind WENO](/methods/central-upwind-weno.md)) on very strong
discontinuities, which the unlimited scheme cannot compute (§3).

## Christlieb et al.: parameterized limiter for MHD

([Christlieb et al. (2016)](/sources/christlieb-2016.md), §5.) The
low-order flux is the global Lax–Friedrichs flux on the cell values;
its positivity for MHD under CFL $\le 0.5$ is assumed by Christlieb
et al., who call it conjectured and "not proven". Later sources report
proofs that are not in the corpus: Balsara, Bhoriya & Shu (2026, §5.1)
cite Gurski, and Ding & Wu (2024, §1) cite Wu (2018), conditional in
multi-D on a discrete divergence-free condition. The question stays open
([positivity preservation](/properties/positivity-preserving.md),
Contradictions: "Is the first-order Lax–Friedrichs MHD scheme provably
positive?"; [Ding & Wu (2024)](/sources/ding-2024.md), §1).
In 2D each cell's update is affine in four interface factors
$(\theta_L, \theta_R, \theta_D, \theta_U)$, and the admissible sets in
$[0,1]^4$ for density, and for density plus pressure, are convex (density
linear, pressure concave). A box inside the density set is found in
closed form, its vertices are shrunk by bisection to meet the pressure
floor, and each interface takes the minimum of its two cells' factors.
Where the limiter acts, an energy correction keeps the pressure
unchanged across the constrained-transport field update at the cost of
energy conservation; the error stays below 1% in the tests, grows
linearly in time and decreases with resolution (§6.7).

## Balsara et al.: PCP hybridization with divergence-free fields

([Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §5.) A cell
factor $\theta_{i,j,k}$, starting at 1, is lowered iteratively in troubled
cells until all forward-Euler sub-steps of the SSP stage are PCP. Face
fluxes use the minimum over the two adjacent cells, and edge electric
fields the minimum over the four cells around the edge, so the
face-centred magnetic field is limited consistently with the cell
variables. The procedure is time-explicit, and the authors trace it to
Hu et al.

# Citations

1. [Hu, Adams & Shu (2013)](/sources/hu-2013.md), §§2–3 (eqs. 11–21 read from the page images).
2. [Christlieb et al. (2016)](/sources/christlieb-2016.md), §§1, 2, 5, 6.7.
3. [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §§5, 5.1.
4. [Ding & Wu (2024)](/sources/ding-2024.md), §1.
