---
type: Definition
title: "Total variation diminishing (TVD) and slope limiters"
description: "TVD reconstruction limits the interface value of a second-order scheme by a limiter function of the slope ratio inside Sweby's region; this page collects the limiter formulas of the chunk-1 sources (MinMod, generalized minmod, SuperBee, van Leer, van Albada, OSPRE, MC, Deng's shape-preserving limiter), their normalised-variable reading, and the roles limiters play inside WENO, central-upwind and DG schemes."
status: established
aliases: [TVD, TVD limiter, flux limiter, slope limiter, MUSCL limiter, minmod]
tags: [limiting, reconstruction, finite-volume, central-scheme]
timestamp: 2026-10-21T12:00:00Z
---

# Total variation diminishing (TVD) and slope limiters

**Total variation diminishing** (TVD) schemes are used by the chunk-1 sources
without a restated definition: none of them prints the total-variation
estimate, and all of them impose the property through Sweby's limiter region.
For a second-order reconstruction the TVD constraint is imposed through a
**limiter** $\psi$ of the slope ratio

$$r_i=\frac{\bar u_i-\bar u_{i-1}}{\bar u_{i+1}-\bar u_i},\qquad
u^-_{i+1/2}=\bar u_i+\tfrac12\psi(r_i)\,(\bar u_{i+1}-\bar u_i),$$

with the mirror formula, $\psi(1/r_i)$ and $\bar u_{i-1}-\bar u_i$, for
$u^+_{i-1/2}$ ([Deng (2023)](/sources/deng-2023.md), §4.1, Eqs. (4.1)–(4.2)).
Deng places Sweby's **second-order TVD region** between MinMod and SuperBee
(§4.1, Fig. 2).

## Limiter formulas

| name | $\psi(r)$ | source |
|---|---|---|
| MinMod | $\max[0,\min(1,r)]$ | Deng, Eq. (4.10) |
| SuperBee | $\max[0,\min(2r,1),\min(2,r)]$ | Deng, Eq. (4.11) |
| van Leer | $(r+\lvert r\rvert)/(1+\lvert r\rvert)$ | Deng, Eq. (4.12) |
| van Albada | $(r^2+r)/(r^2+1)$ | Deng, Eq. (4.13) |
| OSPRE | $1.5(r^2+r)/(r^2+r+1)$ | Deng, Eq. (4.14) |
| Deng's shape-preserving limiter | $(2r+4r^2)/(1+2r+3r^2)$ for $r\ge0$, $0$ otherwise | Deng, Eq. (6.2) |

**Symmetric limiters** satisfy $\psi(r)/r=\psi(1/r)$; they can be written as
slope limiters, $u^\mp=\bar u_i\pm\tfrac12\tilde\psi(1/r_i)\,s_i$ with the central
difference $s_i=\tfrac12(\bar u_{i+1}-\bar u_{i-1})$ (MUSCL–Hancock form; Deng,
Eqs. (4.6)–(4.7), $\tilde\psi$ page-local for the slope-form limiter).

**Two-argument slope limiters.** With $\delta^+=\bar u_{i+1}-\bar u_i$ and
$\delta^-=\bar u_i-\bar u_{i-1}$ (page-local),
[Balsara et al. (2024)](/sources/balsara-2024.md) (App. D, Eqs. (D.9)–(D.10)) use

$$\begin{aligned}
\mathrm{MC}_\beta(\delta^+,\delta^-)&=\tfrac12\big(\mathrm{sgn}\,\delta^++\mathrm{sgn}\,\delta^-\big)\min\big(\lvert\delta^++\delta^-\rvert/2,\ \beta\lvert\delta^+\rvert,\ \beta\lvert\delta^-\rvert\big),\quad1\le\beta\le2,\\
\mathrm{vA}_\varepsilon(\delta^+,\delta^-)&=\frac{\big((\delta^-)^2+\varepsilon\big)\delta^++\big((\delta^+)^2+\varepsilon\big)\delta^-}{(\delta^+)^2+(\delta^-)^2+2\varepsilon},
\end{aligned}$$

($\beta$ and $\varepsilon$ here are the limiter's own parameters, not a
smoothness indicator and not the WENO regularization), and recommend van Albada
for implicit problems because it is continuous in the slopes.
*(Compiler check, not in the sources: with $\varepsilon=0$, $\mathrm{vA}$ is the
undivided slope $\delta^+\psi(r_i)$ of the van Albada limiter of the table, since
$\tfrac12\delta^+\psi(r_i)=\tfrac12\delta^+\delta^-(\delta^++\delta^-)/((\delta^+)^2+(\delta^-)^2)$.)*

The **generalized minmod** limiter with factor 2,

$$(u_x)_i=\mathrm{minmod}\Big(2\frac{\bar u_i-\bar u_{i-1}}{\Delta x},\ \frac{\bar u_{i+1}-\bar u_{i-1}}{2\Delta x},\ 2\frac{\bar u_{i+1}-\bar u_i}{\Delta x}\Big),$$

with $\mathrm{minmod}(z_1,z_2,\dots)=\min_jz_j$ if all $z_j>0$, $\max_jz_j$ if all
$z_j<0$, $0$ otherwise, is the reconstruction of the second-order
central-upwind schemes ([Chertock et al. (2023)](/sources/chertock-2023.md),
§2.1, Eqs. (2.5)–(2.7)). The same minmod function enters the
anti-diffusion correction of the CURH flux
([Wang et al. (2023)](/sources/wang-2023-b.md), §3, Eq. (5)).

## Properties read on the normalised-variable diagram

[Deng (2023)](/sources/deng-2023.md) rewrites the flux-limiter form in the
normalised variable $\tilde u_i$ of the
[normalised-variable diagram](/definitions/normalised-variable-diagram.md),
$\tilde u_{i+1/2}=\tilde u_i+\tfrac12\psi\big(\tilde u_i/(1-\tilde u_i)\big)(1-\tilde u_i)$
(Eq. (4.3), using $r_i=\tilde u_i/(1-\tilde u_i)$), and reads:

- MinMod is always dissipative; SuperBee is anti-dissipative for $\tilde u$
  between about 0.3 and 0.8 (§4.1, Fig. 3);
- the symmetric limiters (van Leer, van Albada, OSPRE) are dissipative for
  $\tilde u<1/2$ and anti-dissipative for $\tilde u>1/2$, "not symmetric in terms
  of numerical dissipation errors", which distorts transported shapes; because the
  third-order line does not satisfy the symmetry condition, a symmetric TVD
  limiter cannot be third order (Remark 4.1);
- Deng's new limiter is tangent to the third-order line at $\tilde u=1/2$ and to
  the left TVD boundary $\tilde u_{i+1/2}=2\tilde u_i$ at $0$, lies in the
  dissipative second-order TVD region, gives lower $L_1$ error than the symmetric
  limiters on sine advection (van Leer is slightly better in $L_\infty$; SuperBee
  "loses the accuracy as the grid is refined"), and preserves shapes better than
  van Leer in 2D rotation (§6.1, Figs. 10–12). *(Compiler check, not in the sources: inserting
  $\psi$ of Eq. (6.2) with $r=\tilde u/(1-\tilde u)$ into Eq. (4.3) reproduces
  Deng's normalised form $(2\tilde u+\tilde u^3)/(1+2\tilde u^2)$ identically
  (symbolic simplification), with value $3/4$ at $1/2$.)*
- The left TVD boundary has slope 2 (CFL 0.5 for the fully discrete scheme);
  Deng makes its slope a CFL-dependent parameter, and, citing Giuliani and
  Krivodonova, calls CFL $<0.5$ "overly stringent" with high-order SSP
  Runge–Kutta stepping (§4.1, §5).

[Chertock et al. (2023)](/sources/chertock-2023.md) (§2.1) report, after their
ref. [26], a classification of limiters into dissipative, compressive and
overcompressive (compressive ones may create kinks, overcompressive ones jumps),
with minmod "the most compressive out of dissipative limiters".

## Roles of limiters in high-order schemes

- **Variable choice.** Minmod applied to conservative variables "typically leads
  to large oscillations", so Chertock et al. apply it to local characteristic
  variables (§2.1; see [characteristic decomposition](/methods/characteristic-decomposition.md)).
  [Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md) (§4 item (4),
  §5.2.3, Fig. 1b) use minmod-limited second-order reconstruction on primitive
  variables inside the subcell finite-volume scheme of a DG method, because it
  keeps positivity; at element-boundary subcells minmod is not defined and the
  scheme falls back to first order. A TVD minmod reconstruction of scaled
  entropy variables, after Fjordholm, Mishra and Tadmor, gives a higher-order
  entropy-stable finite-volume scheme (§2.2; see
  [subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md)).
- **Base polynomial of multi-resolution WENO.** The third-order multi-resolution
  WENO of Zhu and Shu falls to a first-order base polynomial when smoothness is
  lost, and Balsara et al. found it "less than second order" on "somewhat large"
  meshes; their fix replaces that base by an $\mathrm{MC}_\beta$- or van
  Albada-limited linear polynomial ([Balsara et al. (2024)](/sources/balsara-2024.md),
  §VII.a, App. D, Eqs. (D.7)–(D.8); see [WENO-AO](/methods/weno-ao.md)).
- **Bounds called "TVD-like".** The density bounds
  $\min_k\bar\rho_{(ij,k)}\le\rho_{ij}\le\max_k\bar\rho_{(ij,k)}$ of
  [Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md) (§5.2.2,
  Eq. (47)) are local discrete maximum principles over bar states, not
  total-variation estimates, as their printed form shows (see
  [convex limiting](/methods/convex-limiting.md)).

## Qualifications

- Deng's claim that symmetric TVD limiters cannot reach uniform second order in
  smooth regions is relayed from Tang and Li's accuracy tests (Deng, §1); the
  third-order impossibility is Deng's own (Remark 4.1).
- The TVD left boundary of slope 2 is Sweby's; Deng's reading of it as a free
  CFL-dependent slope $k$ is a reinterpretation, not Sweby's statement.

# Citations

- [Deng (2023)](/sources/deng-2023.md) — §1, §4.1, Eqs. (4.1)–(4.15), Remark 4.1, §6.1, Eqs. (6.1)–(6.2), Figs. 2–3, 10–12.
- [Chertock et al. (2023)](/sources/chertock-2023.md) — §2.1, Eqs. (2.5)–(2.7): generalized minmod, limiter classes.
- [Wang et al. (2023)](/sources/wang-2023-b.md) — §3, Eq. (5): minmod in the CURH anti-diffusion term.
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §VII.a, App. D, Eqs. (D.7)–(D.10): MC and van Albada base polynomial.
- [Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md) — §2.2, §4, §5.2: minmod subcell reconstruction, TVD-like bounds.
