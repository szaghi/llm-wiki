---
type: Definition
title: "Total variation diminishing (TVD) and slope limiters"
description: "TVD reconstruction limits the interface value of a second-order scheme by a limiter of the slope ratio inside Sweby's region; the page gives the incremental-form TVD conditions for explicit and implicit Euler steps, the limiter formulas of the sources, their normalised-variable reading, the first-order barrier at extrema, and the roles of limiters in WENO, central and DG schemes."
status: established
aliases: [TVD, TVD limiter, flux limiter, slope limiter, MUSCL limiter, minmod]
tags: [limiting, reconstruction, finite-volume, central-scheme]
timestamp: 2026-10-22T20:00:00Z
---

# Total variation diminishing (TVD) and slope limiters

**Total variation diminishing** (TVD) schemes satisfy $TV(u^{n+1})\le TV(u^n)$.
The chunk-1 sources use the property without restating it and impose it
through Sweby's limiter region; the estimate and the incremental-form
conditions behind that region are restated by
[Puppo et al. (2023)](/sources/puppo-2023.md) (§2; next section).
For a second-order reconstruction the TVD constraint is imposed through a
**limiter** $\psi$ of the slope ratio

$$r_i=\frac{\bar u_i-\bar u_{i-1}}{\bar u_{i+1}-\bar u_i},\qquad
u^-_{i+1/2}=\bar u_i+\tfrac12\psi(r_i)\,(\bar u_{i+1}-\bar u_i),$$

with the mirror formula, $\psi(1/r_i)$ and $\bar u_{i-1}-\bar u_i$, for
$u^+_{i-1/2}$ ([Deng (2023)](/sources/deng-2023.md), §4.1, Eqs. (4.1)–(4.2)).
Deng places Sweby's **second-order TVD region** between MinMod and SuperBee
(§4.1, Fig. 2).

## TVD conditions in incremental form, explicit and implicit

[Puppo et al. (2023)](/sources/puppo-2023.md) (§2) revisit the TVD bounds for
$\partial_tu+a\partial_xu=0$, $a>0$, periodic data, to motivate an implicit
high-order scheme ([Quinpi](/methods/quinpi.md)). Write the limited
second-order update in Harten's incremental form, with page-local coefficients
$\mathsf C_i$:

$$\begin{aligned}
\text{explicit:}\quad u^{n+1}_i&=u^n_i-\mathsf C_{i-1}\big(u^n_i-u^n_{i-1}\big),\\
\text{implicit:}\quad u^{n}_i&=u^{n+1}_i+\mathsf C_{i-1}\big(u^{n+1}_i-u^{n+1}_{i-1}\big),
\end{aligned}\qquad
\mathsf C_{i-1}=\frac{a\Delta t}{\Delta x}\Big[1-\tfrac12\Big(\psi(r_{i-1})-\frac{\psi(r_i)}{r_i}\Big)\Big],$$

with the slope ratio $r_i$ and limited slope $\psi(r_i)(u_{i+1}-u_i)$ of this
page. Then (Puppo et al., §2, citing Harten, Sweby and LeVeque):

- the explicit step is TVD iff $\mathsf C_i\ge0$ and $1-\mathsf C_i\ge0$; the
  first condition gives Sweby's region $0\le\psi(r)/r\le2$, $0\le\psi(r)\le2$, the
  second a CFL condition;
- the implicit step is TVD if $\mathsf C_i\ge0$ and $1+\mathsf C_i\ge0$; the first
  condition is the same limiter region and the second always holds, so the
  implicit Euler step with a TVD limiter is TVD for every $\Delta t/\Delta x$;
  the first-order implicit upwind scheme ($\psi\equiv0$) is unconditionally
  TVD by the reverse triangle inequality;
- second-order accuracy needs $\psi(1)=1$ and $\psi$ at least Lipschitz, so
  $\psi$ and $r$ may be computed from any at least first-order approximation of
  $u(x,t^{n+1})$, e.g. a predictor.

In the implicit step the coefficients $\mathsf C_i$ depend on $u^{n+1}$ through
$\psi$ and $r$. Quinpi carries the last item over to its CWENO reconstruction,
whose nonlinear weights it computes from a first-order predictor (§2–§3).

## Limiter formulas

| name | $\psi(r)$ | source |
|---|---|---|
| MinMod | $\max[0,\min(1,r)]$ | Deng, Eq. (4.10) |
| SuperBee | $\max[0,\min(2r,1),\min(2,r)]$ | Deng, Eq. (4.11) |
| van Leer | $(r+\lvert r\rvert)/(1+\lvert r\rvert)$ | Deng, Eq. (4.12) |
| van Albada | $(r^2+r)/(r^2+1)$ | Deng, Eq. (4.13) |
| OSPRE | $1.5(r^2+r)/(r^2+r+1)$ | Deng, Eq. (4.14) |
| Deng's shape-preserving limiter | $(2r+4r^2)/(1+2r+3r^2)$ for $r\ge0$, $0$ otherwise | Deng, Eq. (6.2) |
| SuperBee, parametrized | $\max[0,\min(\beta r,1),\min(r,\beta)]$, $\beta=2$ | Nguyen et al., Eq. (28b) |
| OverBee (Chiapolino, Saurel, Nkonga) | $\max\big[0,\min\big[2,2r,\max[\min(2r,\beta),\min\{(2-\beta)r+2(\beta-1),r\}]\big]\big]$, $1\le\beta\le2$ | Nguyen et al., Eq. (28c) |

In the last two rows $\beta$ is the limiter's parameter (page-local, as below).
[Nguyen et al. (2022)](/sources/nguyen-2022.md) print SuperBee in a form that equals Deng's for
$\beta=2$, and van Leer as in the table (Eq. (28a)). *(compiler check, not in the sources: the
OverBee formula gives $\psi(1)=\beta$, so for $\beta>1$ it violates the second-order condition
$\psi(1)=1$ of Puppo et al. above; the $\beta$ used is not printed.)* Nguyen et al. apply OverBee to the volume fractions and van Leer to the other
primitive variables of their multiphase model, in the MUSCL $\kappa_{\mathrm M}$-scheme with $\kappa_{\mathrm M}=1/3$ ([MUSCL](/methods/muscl-hancock.md))
(Eqs. (26)–(27)); OverBee and SuperBee keep a water–air interface about three cells thick, van
Leer lets it grow beyond ten cells at Mach 0.001 with the Rusanov flux (§2.3, §3.1, Figs. 1–4),
and OverBee is retained after the shock–helium-bubble comparison for its better interface
thickness and smoothness (§3.4, Fig. 17). In the source of the OverBee limiter, as reported by
Nguyen et al., it is switched on only by an interface indicator.

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
[Kanbar et al. (2022)](/sources/kanbar-2022.md) (§3, Eq. (8)) use the
three-argument form of the MC limiter for the undivided slope,

$$\mathrm{minmod}\Big(\beta(\bar u_i-\bar u_{i-1}),\ \tfrac12(\bar u_{i+1}-\bar u_{i-1}),\ \beta(\bar u_{i+1}-\bar u_i)\Big),\qquad 1<\beta<2,$$

with $\beta=1.5$ in all tests (the source's $\theta$), componentwise on the
conserved deviation $\delta u=u-u_{\mathrm e}$ from a known steady state (and on
$u^n$ and $u_{\mathrm e}$ for the predictor) of their
[unstaggered central scheme](/methods/unstaggered-central-scheme.md); the formula is
written here for $\bar u$.
*(compiler check, not in the sources: this is $\mathrm{MC}_\beta$ above, since
$\tfrac12(\mathrm{sgn}\,\delta^++\mathrm{sgn}\,\delta^-)\min(\cdot)$ equals the
three-argument minmod; the generalized minmod with factor 2 below is the case
$\beta=2$.)* The MFC code offers minmod, MC, OSPRE, SuperBee, Sweby, van Albada
and van Leer as flux limiters ([Bryngelson et al. (2021)](/sources/bryngelson-2021.md),
§4.2.2; no formulas printed).
*(compiler check, not in the sources: with $\varepsilon=0$, $\mathrm{vA}$ is the
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

**Slopes on stretched and mapped meshes.** [Peng et al. (2022)](/sources/peng-2022.md)
(§2.4, Eqs. (15)–(20)) use minmod-limited MUSCL in a MUSCL–Hancock finite-volume scheme on
curvilinear meshes, dividing the cell differences by physical centroid-to-face distances,
$\delta_i=(\bar u_{i+1}-\bar u_i)/(L^-_{i+1}+L^+_i)$, with $L^+_i$ ($L^-_i$) the distance from the
centroid of cell $i$ to its right (left) face (page-local). *(compiler check, not in the sources:
the printed left-face value, with the MUSCL parameter $\omega=0$, is
$\bar u_i-\tfrac12\big(\delta_{i-1}L^-_i+\delta_iL^+_i\big)$, which for linear data
$\delta_{i-1}=\delta_i=b$ gives $\bar u_i-\tfrac12b(L^-_i+L^+_i)$ instead of $\bar u_i-bL^-_i$; the
reconstruction is exact for linear data only where $L^-_i=L^+_i$, whereas the Cartesian form,
Eqs. (15)–(16), is exact. Whether the code does this is not stated.)* See
[MUSCL–Hancock](/methods/muscl-hancock.md).

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
  van Leer in 2D rotation (§6.1, Figs. 10–12). *(compiler check, not in the sources: inserting
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

- **Flux-limited WENO.** "The WENO schemes we utilize are, in general, not TVD",
  which can cause instability "even when the usual CFL criteria are met"; MFC
  therefore optionally blends the first-order (piecewise-constant) Riemann flux
  with the WENO Riemann flux, low-order flux plus $\psi(r_i)$ times the
  difference, where $r_i$ is the slope ratio of the volume fraction taken on
  the upwind side of the contact velocity of the Riemann solver
  ([Bryngelson et al. (2021)](/sources/bryngelson-2021.md), §4.2.2, Eq. (34); the
  blend is described in words). The dissipation is so confined to material
  interfaces where WENO "cannot form a smooth stencil". See
  [hybrid central-WENO schemes](/methods/hybrid-weno.md) and [MFC](/software/mfc.md).
- **The sign property.** In the entropy-stable TVD-ES subcell scheme of
  [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) (§4,
  Eqs. (72)–(81)) the minmod reconstruction of the scaled entropy variables
  makes every reconstructed jump have the sign of the cell-mean jump, which is
  what entropy stability needs; citing Fjordholm, Mishra and Tadmor, they state
  that minmod is the only symmetric TVD limiter with this sign property. The
  reconstruction is done in reference space on the non-uniform Gauss–Lobatto
  subcell grid, and the variant without reconstruction in the element-boundary
  subcells gave the best Orszag–Tang results (§6.2, Fig. 6). See
  [TeCNO schemes](/methods/tecno-scheme.md).

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
- **Replaced by nonlinear weights on unstructured grids.**
  [Chen et al. (2022)](/sources/chen-2022.md) (§1, §5) state that second-order TVD-based
  limiters "typically loss [sic] their designed accuracy at smooth critical points", that the TVD
  principle cannot guarantee the removal of oscillations on unstructured grids (citing
  Jameson), and that several common limiters cannot strictly guarantee monotonicity (citing the
  MLP-pw paper). They replace the slope limiter of a vertex-based least-squares gradient by
  WENO-type weights, $d_j/(\epsilon+SI_j)^2$ with the linear vertex weights $d_j$ (the source's
  $\gamma_j$) and directional indicators $SI_j=(\partial_x\varphi_j)^2\times$ cell area of the
  vertex gradients ($SI_j$, $\varphi_j$ page-local), and report
  that this converges where the MLP-pw limiter with the Venkatakrishnan function stalls or
  diverges on Mach-5 and Mach-10 cylinder flows, at lower cost (14.84 against 17.92 ms per
  reconstruction, §6.4, Table 2). The critical-point claim rests on one smooth test, the
  isentropic vortex, where the nonlinear weights leave the order at about 2 but raise the error on
  the coarse meshes (Table 1). See
  [unstructured gradient reconstruction](/methods/unstructured-gradient-reconstruction.md) and
  [critical-point accuracy](/properties/critical-point-accuracy.md).
- **Bounds called "TVD-like".** The density bounds
  $\min_k\bar\rho_{(ij,k)}\le\rho_{ij}\le\max_k\bar\rho_{(ij,k)}$ of
  [Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md) (§5.2.2,
  Eq. (47)) are local discrete maximum principles over bar states, not
  total-variation estimates, as their printed form shows (see
  [convex limiting](/methods/convex-limiting.md)).

## The first-order barrier at extrema

[Pazner (2021)](/sources/pazner-2021.md) (§4.4) recalls that TVD schemes are
provably at most first-order accurate at smooth extrema, and observes the
analogous loss for the local maximum principle of his flux-corrected DG: with
strictly enforced local bounds the $L^1$ convergence rates on $\sin(2\pi x)$
advection are about one (1.00, 1.04, 1.29 for $p=3,4,5$), while relaxing the
bounds to global ones in cells flagged smooth by a modal indicator restores
4.00, 5.00, 5.86 (§5.1, Table 1; $p$ the source's polynomial degree). See
[convex limiting](/methods/convex-limiting.md) and
[critical-point accuracy](/properties/critical-point-accuracy.md).

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
- [Puppo et al. (2023)](/sources/puppo-2023.md) — §2: explicit and implicit incremental-form TVD conditions (arXiv v2).
- [Kanbar et al. (2022)](/sources/kanbar-2022.md) — §3, Eq. (8): three-argument MC limiter, $\beta=1.5$ (arXiv v1).
- [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) — §4.2.2, Eq. (34): flux-limited WENO in MFC (arXiv v1).
- [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) — §4, Eqs. (72)–(81), §6.2: minmod and the sign property (arXiv v1).
- [Pazner (2021)](/sources/pazner-2021.md) — §4.4, §5.1, Table 1: first-order barrier at extrema (arXiv v1).
- [Nguyen et al. (2022)](/sources/nguyen-2022.md) — §2.3, Eqs. (26)–(28), §3.1, §3.4: SuperBee, OverBee and van Leer in a multiphase MUSCL scheme.
- [Peng et al. (2022)](/sources/peng-2022.md) — §2.4, Eqs. (15)–(20): minmod MUSCL on mapped meshes (accepted manuscript).
- [Chen et al. (2022)](/sources/chen-2022.md) — §1, §5, §6.3–6.4, Tables 1–2: limiters versus nonlinear weights on unstructured grids.
