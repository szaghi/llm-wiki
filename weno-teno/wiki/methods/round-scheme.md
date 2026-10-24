---
type: Method
title: "ROUND schemes"
description: "ROUND schemes are three-cell compact finite-volume reconstructions written directly as functions of the normalised cell average, hence scale-invariant, with dissipation, TVD and ENO behaviour placed by construction; the page gives the dissipative, low-dissipative, fine-tuned, learned-weight-inspired and non-uniform-grid forms, their DG-subcell use, cost, evidence and order caveat."
status: established
aliases: [ROUND, LD-ROUND, Reconstruction Operator on Unified Normalised-variable Diagram, low-dissipative ROUND]
tags: [reconstruction, finite-volume, low-dissipation, limiting, round-scheme]
timestamp: 2026-10-24T05:57:00Z
---

# ROUND schemes

A **ROUND scheme** prescribes the normalised face value of a three-cell compact
reconstruction as an explicit function of the normalised cell average,
$\tilde u_{i+1/2}=\mathcal R(\tilde u_i)$, with
$\tilde u_i=(\bar u_i-\bar u_{i-1})/(\bar u_{i+1}-\bar u_{i-1})$, and recovers
$u^-_{i+1/2}=\bar u_{i-1}+(\bar u_{i+1}-\bar u_{i-1})\,\mathcal R(\tilde u_i)$
([Deng (2023)](/sources/deng-2023.md), §7; [Huang et al. (2026)](/sources/huang-2026.md),
§4). The curve is drawn on the unified
[normalised-variable diagram](/definitions/normalised-variable-diagram.md) (UND),
where accuracy (the point $(1/2,3/4)$ and the third-order line P3,
$\tfrac13+\tfrac56\tilde u$), dissipation (below P3) and anti-dissipation (above),
the CBC-TVD region and the ENO region are visible, so these properties are chosen
by construction. Being normalisable, every ROUND scheme is scale-invariant
(Deng, Proposition 2; see [scale invariance](/properties/scale-invariance.md)).
The building blocks are UW2 ($\tfrac32\tilde u$), CD2 ($\tfrac12\tilde u+\tfrac12$),
P3 and UW1 ($\tilde u$). Below, $\varphi_k$ are page-local blending functions of
$\tilde u$ (Deng writes $\omega_k$ for them; they are not smoothness-based weights)
and their parameters are written as numbers.

## Precursor: scale-invariant WENO3

[Deng (2023)](/sources/deng-2023.md) (§6.2, Eqs. (6.3)–(6.6), Proposition 6)
first makes WENO3 normalisable by letting its weight depend on $\tilde u_i$ only:
$u^-_{i+1/2}=\omega_0\,\mathrm{UW2}+(1-\omega_0)\,\mathrm{CD2}$ with

$$\omega_0=\frac13+\frac23\frac{1}{\big(1+25\tilde u_i^{2}\big)^2}-\frac13\frac{1}{\big(1+25(1-\tilde u_i)^{2}\big)^2},$$

the parameter 25 being the largest that keeps the curve inside the CBC-TVD region
on $0<\tilde u<1$. Its scale-invariance error stays at round-off for scaling
factors from $10^{-19}$ to $10^{19}$, unlike WENO-JS3, WENO-Z3 and WENO-P3 (Fig. 13).

## Dissipative ROUND (Deng 2023, §7.1)

- **Piecewise linear** (Eq. (7.1), as Fig. 16(a) shows):
  $\min(-\tfrac12\tilde u,\ \text{P3})$ for $\tilde u\le0$;
  $\min\big(\tfrac52\tilde u,\ \text{P3},\ \tfrac9{10}+\tfrac1{10}\tilde u\big)$ on $(0,1]$;
  $\min\big(\tfrac65\tilde u-\tfrac15,\ \text{P3}\big)$ for $\tilde u>1$.
- **Two blending functions** (Eq. (7.2)):
  $\mathcal R=(1-\varphi_0)\big[(1-\varphi_1)\,\text{P3}+\varphi_1\,\text{UW2}\big]+\varphi_0\,\text{CD2}$,
  $\varphi_0=(1+7.8(\tilde u-1)^2)^{-6}$, $\varphi_1=(1+12\tilde u^2)^{-4}$.
- **One blending function** (Eq. (7.3)): P3 blended with Deng's shape-preserving
  TVD curve $(2\tilde u+\tilde u^3)/(1+2\tilde u^2)$ (see
  [TVD](/definitions/total-variation-diminishing.md)) by
  $\varphi_0=(1+11\tilde u^2(\tilde u-1)^2)^{-4}$.

All three lie in the dissipative region; they are less dissipative than existing
second-order shock-capturing schemes on sine advection, non-oscillatory, better
at critical points than WENO-P, with "no remarkable difference" between them
(Figs. 17–23).

## Low-dissipative ROUND (Deng 2023, §7.2)

These deliberately add anti-dissipation: parts of the curve lie above P3, so that
positive and negative second-order error terms partly cancel over a cell
(Remark 7.2, contrasted with [BVD](/definitions/boundary-variation-diminishing.md),
which minimizes the boundary jump). Eq. (7.4):

$$\mathcal R=\begin{cases}
\text{P3}\cdot\varphi_0,&\tilde u\le0,\\
\min\big(\text{P3}\,\varphi_1+2.5\tilde u\,(1-\varphi_1),\ 2.5\tilde u\big),&0<\tilde u\le\tfrac12,\\
\min\big(\text{P3}\,\varphi_2+(0.05\tilde u+0.95)(1-\varphi_2),\ 0.05\tilde u+0.95\big),&\tfrac12<\tilde u\le1,\\
\text{P3}\,(1-\varphi_3)+\tilde u\,\varphi_3,&\tilde u>1,
\end{cases}$$

$\varphi_0=1-(1+5\tilde u^2)^{-4}$, $\varphi_1=(1+300(\tilde u-\tfrac12)^4)^{-2}$,
$\varphi_2=(1+800(\tilde u-\tfrac12)^4)^{-2}$, $\varphi_3=(1+20(\tilde u-1)^2)^{-2}$.
Larger parameters in $\varphi_1,\varphi_2$ give more anti-dissipation, larger
ones in $\varphi_0,\varphi_3$ retrieve P3; the values are "already large" and
larger ones "are not recommended" (Remark 7.3). Eq. (7.5) adds two positive
polynomial bumps on $(0.05,0.47)$ and $(0.55,0.97)$ to P3, and Eq. (7.6) is a
piecewise blend with six parameters. Their spectral property is "close to the
linear third-order scheme" (Fig. 28).

**Fine-tuned TVD ROUND** (§7.3, Eq. (7.7)): a curve fully in the TVD region,
following P3 around $\tilde u\in[0.4,0.6]$, with slope-2 and
$0.15\tilde u+0.85$ upper bounds on the two sides; it is less dissipative and more
shape-preserving than van Leer on 2D rotation (Fig. 37).

## ROUND and LD-ROUND after WENO3-NN (Huang et al. 2026, §4)

Learning from the [WENO3-NN](/methods/learned-weno-weights.md) diagram, which
bends toward CD2 for $\tilde u<0$, Huang et al. propose (Eq. (4.1))

$$\mathcal R=\begin{cases}
\max\big\{\min\{\text{CD2},\ -\tfrac32\tilde u-\tfrac95\},\ \text{UW2}\big\},&\tilde u\le0,\\
\min\big\{\tfrac52\tilde u,\ \text{P3},\ \tfrac3{50}\tilde u+\tfrac{47}{50}\big\},&0<\tilde u\le1,\\
\text{CD2},&\tilde u>1,
\end{cases}$$

*(compiler check, not in the sources: the breakpoints are UW2 on $[-0.6,0]$, the connector on
$[-1.15,-0.6]$, CD2 below $-1.15$; $\tfrac52\tilde u$ on $(0,0.2]$, P3 on
$[0.2,91/116]$, the near-1 line on $[91/116,1]$)*, with a larger central share for
$\tilde u<0$ than WENO3-NN itself, "motivated by numerical experiments" not shown.
**LD-ROUND** (Eqs. (4.2)–(4.3)) keeps the $\tilde u\le0$ and $\tilde u>1$ branches
and on $(0,\tfrac12]$ and $(\tfrac12,1]$ blends P3 with the upper bounding lines
$\tfrac52\tilde u$ and $\tfrac3{50}\tilde u+\tfrac{47}{50}$ by
$\varphi_1=(1+180(\tilde u-\tfrac12)^4)^{-2}$, $\varphi_2=(1+600(\tilde u-\tfrac12)^4)^{-2}$,
which equal 1 at $\tilde u=1/2$ (P3 recovered) and fall off away from it,
producing controlled anti-dissipation; larger parameters risk "excessive
anti-dissipation errors and potentially ... numerical instability" (§4.2).

Compared with Deng's Eq. (7.1), the Part-2 ROUND differs on $\tilde u\le0$ (a
switch to CD2 instead of the $-\tfrac12\tilde u$/P3 branch), near $\tilde u=1$
($\tfrac3{50}\tilde u+\tfrac{47}{50}$ instead of $\tfrac9{10}+\tfrac1{10}\tilde u$)
and for $\tilde u>1$ (CD2 instead of $\min(\tfrac65\tilde u-\tfrac15,\text{P3})$).

## Non-uniform grids and DG subcells (Deng, Jiang & Yan 2025)

[Deng, Jiang & Yan (2025)](/sources/deng-2025.md) (§2) carry ROUND to a three-cell stencil
of arbitrary widths $\Delta x_{i-1},\Delta x_i,\Delta x_{i+1}$ (page-local width of cell $I_i$;
$h_-,h_0,h_+$ on the normalised-variable-diagram page),
with the same normalised variables. The building blocks become (Eqs. (2.13)–(2.15))

$$\mathrm{UW}=\frac{\Delta x_{i-1}+2\Delta x_i}{\Delta x_{i-1}+\Delta x_i}\tilde u,\qquad
\mathrm{CD}=\frac{\Delta x_{i+1}}{\Delta x_i+\Delta x_{i+1}}\tilde u+\frac{\Delta x_i}{\Delta x_i+\Delta x_{i+1}},$$

and the third-order line P of slope $\mu_1^{\mathrm P}$ and intercept $\mu_0^{\mathrm P}$ given on the
[normalised-variable diagram](/definitions/normalised-variable-diagram.md), all three passing
through a grid-dependent accuracy point. The non-uniform ROUND operator is piecewise linear
(Eq. (2.26)):

$$\mathcal R(\tilde u)=\begin{cases}
\min\big(-\tfrac14\tilde u,\ \mathrm P\big),&\tilde u\le0,\\
\min\Big(\tfrac32\,\mathrm{UW},\ \mathrm P,\ \tfrac25\dfrac{\Delta x_{i+1}}{\Delta x_i+\Delta x_{i+1}}(\tilde u-1)+1\Big),&0<\tilde u\le1,\\
\min\big(\mathrm P,\ \tfrac65(\tilde u-1)+1\big),&\tilde u>1,
\end{cases}$$

with the four constants $\tfrac14,\tfrac32,\tfrac25,\tfrac65$ (the source's $\beta_1,\dots,\beta_4$,
not smoothness indicators) used in every test. Larger first, second and fourth constants use
the third-order line more, with more risk of oscillation; a smaller third one moves the
curve toward first-order downwind, with the same risk. The curve recovers P away from
$\tilde u\approx0,1$ and lies entirely in the dissipative region for $0<\tilde u<1$; an
anti-dissipative variant is said to be possible (§2.4). On a uniform grid the blocks reduce to
UW2, CD2 and P3 (Remark 2.1). The authors stress that, unlike non-uniform WENO, ROUND needs no
smoothness indicators, and call it cheaper on that ground (§1, §5; no timings).

**Use as a DG subcell scheme** (§3). The non-uniform cells are the subcells of a modal
Legendre [DG](/methods/discontinuous-galerkin.md) element, sized by the Gauss–Legendre weights
and carrying the Gauss-point values, which are interpreted as subcell averages without exact
averaging; a mass-matrix projection maps the subcell data back to modes. A troubled-element
indicator built on a relaxed [BVD](/definitions/boundary-variation-diminishing.md) criterion
switches whole elements to the ROUND finite-volume scheme (hard switching; DG/FV-ROUND;
[subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md)). ROUND is
[scale-invariant](/properties/scale-invariance.md), but DG/FV-ROUND is not, because the indicator
threshold is dimensional (§3.3).

**Evidence** (§4). On a rotating passive scalar on $200\times200$ cells, uniform or with the
widths of the subcells of $50\times50$ fourth-order elements, ROUND is far less dissipative
than TVD limiters and keeps the shapes on the strongly non-uniform grid, where the van Leer
limiter distorts them even on the uniform grid; along one line it is less dissipative than
uniform-grid WENO5-JS, which overshoots (Figs. 5–7). As a subcell scheme it gives $L^2$
density orders 2.69, 3.40, 3.41, 2.65 at third order on the isentropic vortex, and 2.13–2.60
when 5 % of the elements are forced troubled at random (Tables 1–2), and keeps conservation
to round-off (Table 3). Shock tests (blast waves, Shu–Osher and Titarev–Toro, Lax, two 2D
Riemann problems, double Mach reflection, a viscous shock tube, a type IV shock–shock
interaction) are compared visually with published DG subcell results; an OpenFOAM
implementation on unstructured meshes is given in App. A.

## Cost and evidence

FLOPs per reconstruction: ROUND 11, LD-ROUND 20, WENO3-JS 19, WENO5-JS 55,
WENO3-NN 2139 ([Huang et al. (2026)](/sources/huang-2026.md), Table 2). On sine
advection to $t=20$ (Table 3) LD-ROUND's $L_1$ errors and CPU time are both less
than half of WENO3-NN's on the same grid. All evidence is numerical, mostly visual,
on finite-volume Euler tests (Huang et al. use HLLC, and HLL for double Mach
reflection; Deng does not state the Riemann solver):

- Deng: Sod, Lax, Shu–Osher, blast waves, Leblanc (low-dissipative ROUND "much
  less dissipative and less oscillatory" than WENO-JS5), Lax–Liu Riemann
  configuration 3 on $600\times600$ and double Mach reflection at $\Delta x=1/300$
  ("comparable and even better" than WENO-JS5 on a coarser mesh), and shock
  diffraction over a cylinder in a finite-difference immersed-boundary code, where
  the compact stencil needs fewer ghost nodes (§8, Fig. 38; speed-up stated, not
  timed).
- Huang et al.: Shu–Osher (LD-ROUND best), Riemann configuration 3 (LD-ROUND finer
  than WENO5-JS, symmetry kept), double Mach reflection at $\Delta x=1/400$,
  Rayleigh–Taylor $128\times512$ (ROUND finer than WENO5-JS, LD-ROUND richer than
  WENO5-JS and WENO5-Z), Richtmyer–Meshkov, shock–vortex, an under-expanded
  supersonic planar jet, and a Mach 6 air–helium shock–bubble with a level-set
  sharp interface and multi-resolution (§6).

## Qualifications

- **Order.** Neither paper claims or tabulates observed third order. Huang et al.
  measure $L_1$ orders 2.4–2.6 and $L_\infty$ orders 1.6–1.7 on sine advection
  (Table 3). *(Compiler check, not in the sources: the blending functions are
  fixed functions of $\tilde u$, and smooth monotone data have
  $\tilde u_i=\tfrac12+O(\Delta x)$; for the scale-invariant WENO3 above,
  $\omega_0(\tfrac12)=0.3397$, so $\omega_0-d_0\approx0.0063$ does not vanish
  with $\Delta x$ and, since UW2 and CD2 differ by $O(\Delta x^2)$ in the face
  value, the scheme is formally second order with a small third-order defect,
  not uniformly third order. The same reasoning applies to every ROUND curve that
  departs from P3 in a neighbourhood of $\tilde u=1/2$ of fixed width.)*
- **Order on non-uniform grids.** Deng, Jiang & Yan (2025) also call ROUND "high-order"
  and state no order near $\tilde u\approx0,1$; their DG/FV-ROUND convergence study ends at
  2.65 on the finest mesh (Table 1).
- **Resolution claims** against fifth-order WENO rest on visual comparisons, partly
  on different meshes and partly against figures from other papers.
- **Printed slips** (Deng): the third argument of the middle branch of Eq. (7.1)
  is printed $\tfrac1{10}+\tfrac9{10}\tilde u$, which would never let P3 act and
  would miss the accuracy point; Fig. 16(a) shows $\tfrac9{10}+\tfrac1{10}\tilde u$.
  The blending functions of Eq. (7.7) are printed centred at $\tilde u=1$, which
  would make the curve discontinuous at $1/2$; Fig. 37(a) shows it through
  $(1/2,3/4)$. Huang et al. print the LD-ROUND weights with $k=0,1$ where $k=1,2$
  is used, and state that ROUND "tends toward" CD2 as $\tilde u\to1$, whereas its
  last segment has slope $0.06$ and meets CD2 only at $\tilde u=1$.

# Citations

- [Deng (2023)](/sources/deng-2023.md) — §6.2, Eqs. (6.3)–(6.6), Proposition 6; §7, Eqs. (7.1)–(7.7), Remarks 7.1–7.3, Figs. 13–38; §8.
- [Huang et al. (2026)](/sources/huang-2026.md) — §4, Eqs. (4.1)–(4.3), Figs. 3–4; §5, Table 2, Fig. 5; §6, Table 3, Figs. 6–17.
- [Deng, Jiang & Yan (2025)](/sources/deng-2025.md) — §1; §2, Eqs. (2.10)–(2.26), Remark 2.1; §3.2–3.3; §4, Tables 1–3, Figs. 5–23; §5; App. A.
