---
type: Method
title: "Compact-reconstruction WENO (nonlinear compact schemes)"
description: "Nonlinear compact schemes in which low-order compact (implicit) candidate stencils are combined with WENO weights, so the interface values come from a weight-dependent tridiagonal system: fifth-order upwind compact in smooth regions, third-order compact at discontinuities, without a shock switch."
status: established
aliases: [CRWENO, finite-volume compact-WENO, FVCW, weighted compact scheme]
tags: [compact-scheme, weno, spectral-resolution, finite-volume, positivity]
timestamp: 2026-10-08T00:00:00Z
---

# Compact-reconstruction WENO

**Motivation.** Linear compact schemes have spectral-like resolution on
small stencils but produce Gibbs oscillations at shocks that do not
decay with refinement. [Hybrid compact-WENO](/methods/hybrid-compact-weno.md)
schemes switch to WENO near shocks through an indicator and lose the
compact resolution there. Nonlinear compact schemes instead weight the
compact stencils themselves: Cockburn–Shu (TVB-limited), Deng et al.
(ENO/WENO candidate selection), Jiang et al. (weighted Padé), Zhang et
al. (flux interpolation with WENO weights), and the compact-reconstruction
WENO of Ghosh and Baeder, whose finite-volume form is below
([Guo, Xiong & Shi (2014)](/sources/guo-2014.md), §1).

**Finite-volume construction** ([Guo, Xiong & Shi (2014)](/sources/guo-2014.md), §2.2;
checked on the page images). The fifth-order linear upwind compact
scheme of [Pirozzoli (2002)](/sources/pirozzoli-2002.md) is
$$\tfrac{3}{10}u_{i-1/2} + \tfrac{6}{10}u_{i+1/2} + \tfrac{1}{10}u_{i+3/2} = \tfrac{1}{30}\bar u_{i-1} + \tfrac{19}{30}\bar u_i + \tfrac{10}{30}\bar u_{i+1}.$$
It is split into three third-order compact candidates (pairs of
unknowns on the left, one-sided data on the right):
$$\begin{aligned}
\tfrac23 u_{i-1/2} + \tfrac13 u_{i+1/2} &= \tfrac16\left(\bar u_{i-1} + 5\bar u_i\right),\\
\tfrac13 u_{i-1/2} + \tfrac23 u_{i+1/2} &= \tfrac16\left(5\bar u_i + \bar u_{i+1}\right),\\
\tfrac23 u_{i+1/2} + \tfrac13 u_{i+3/2} &= \tfrac16\left(\bar u_i + 5\bar u_{i+1}\right),
\end{aligned}$$
combined with weights $\omega_0, \omega_1, \omega_2$:
$$\tfrac{2\omega_0 + \omega_1}{3}u_{i-1/2} + \tfrac{\omega_0 + 2(\omega_1 + \omega_2)}{3}u_{i+1/2} + \tfrac13\omega_2\,u_{i+3/2} = \tfrac16\omega_0\bar u_{i-1} + \tfrac{5(\omega_0 + \omega_1) + \omega_2}{6}\bar u_i + \tfrac{\omega_1 + 5\omega_2}{6}\bar u_{i+1},$$
whose solution gives $u^-_{i+1/2}$. The linear weights $d_0, d_1, d_2 = \tfrac{2}{10}, \tfrac{5}{10}, \tfrac{3}{10}$
recover the fifth-order scheme. The nonlinear weights are WENO-Z with
$q = 2$, $\tilde\omega_k = d_k\left(1 + (\tau_5/(\beta_k + \varepsilon))^2\right)$,
$\tau_5 = \vert\beta_2 - \beta_0\vert$, and $\varepsilon = 10^{-13}$, using the
classical Jiang–Shu indicators of the non-compact stencils
([WENO-Z](/methods/weno-z.md); [smoothness indicator](/definitions/smoothness-indicator.md)).
Across a discontinuity the system degenerates to a biased bidiagonal
one and the scheme to third-order compact, which resolves better than
third-order non-compact. $u^+_{i+1/2}$ is the mirror image.

**Systems.** The scalar system is applied per characteristic field,
with eigenvectors at the Roe average of $\bar u_i$, $\bar u_{i+1}$. Since
the left eigenvectors differ between interfaces, the result is a
$3\times3$ block-tridiagonal system per stage, solved by a block chasing
(Thomas) method. Reconstructing conservative variables leaves scalar
tridiagonal systems and is cheaper for smooth flows, but
characteristic reconstruction controls oscillations better at shocks
(§§2.3, 3).

**Cost and resolution** ([Guo, Xiong & Shi (2014)](/sources/guo-2014.md), §3):
despite the implicit solve, the scheme reaches a given $L_1$ error
faster than WENO-JS. On the Lax problem it gives with 60 points
(0.57 s) what WENO-JS gives with 100 (0.55 s). It is sharper than WENO-JS
and WENO-Z on Lax, Sod, Shu–Osher and the blast waves. Positivity is
added with the [scaling limiter](/methods/positivity-preserving-scaling-limiter.md)
and an HLLC flux.

# Citations

1. [Guo, Xiong & Shi (2014)](/sources/guo-2014.md), §§1–3 (eqs. 2.9–2.14 read from the page images).
2. [Pirozzoli (2002)](/sources/pirozzoli-2002.md), §2.
