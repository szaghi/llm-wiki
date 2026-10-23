---
type: Definition
title: "Normalised-variable diagram"
description: "The normalised-variable diagram plots the normalised interface value of a three-cell compact reconstruction against the normalised cell average; Deng's unified version (UND), extended to non-uniform grids, adds the accuracy point, the third-order line, diffusion and anti-diffusion regions, a CFL-dependent CBC-TVD region and ENO and high-resolution regions, on which TVD, NVD, WENO3, THINC, ROUND and learned schemes are compared."
status: established
aliases: [NVD, normalized variable diagram, unified normalised-variable diagram, UND]
tags: [reconstruction, finite-volume, limiting, weno, low-dissipation]
timestamp: 2026-10-23T15:11:00Z
---

# Normalised-variable diagram

For a finite-volume reconstruction of the left state $u^-_{i+1/2}$ from the
three cell averages $\bar u_{i-1},\bar u_i,\bar u_{i+1}$ (a compact three-cell
stencil), the **normalised cell average** and **normalised face value** are

$$\tilde u_i=\frac{\bar u_i-\bar u_{i-1}}{\bar u_{i+1}-\bar u_{i-1}},\qquad
\tilde u_{i+1/2}=\frac{u^-_{i+1/2}-\bar u_{i-1}}{\bar u_{i+1}-\bar u_{i-1}}$$

([Deng (2023)](/sources/deng-2023.md), §2.2, Definitions 1–2;
[Huang et al. (2026)](/sources/huang-2026.md), §2.2, Eqs. (2.6)–(2.7)); the
right state at $x_{i-1/2}$ is normalised by mirror symmetry. A reconstruction is
**normalisable** when $\tilde u_{i+1/2}$ is a function of $\tilde u_i$ alone,
$\tilde u_{i+1/2}=\mathcal R(\tilde u_i)$ (page-local symbol for the
normalised operator; Deng, Definitions 4–6). The **normalised-variable diagram**
is the graph of $\mathcal R$. It goes back to Leonard's NVD and Gaskell and Lau's
convection boundedness criterion (CBC), as recalled by Deng, who generalizes it
into the **Unified Normalised-variable Diagram (UND)**
([Deng (2023)](/sources/deng-2023.md), §5, Fig. 9).

## Linear operators and the accuracy point

Every consistent linear three-cell operator is normalisable, with
$\mathcal R(\tilde u)=\mu_1\tilde u+\mu_0$ (Deng, Eq. (3.7); $\mu_0$,
$\mu_1$ page-local, not WENO weights). The named operators are
([Deng (2023)](/sources/deng-2023.md), Eqs. (3.1)–(3.6);
[Huang et al. (2026)](/sources/huang-2026.md), Eqs. (2.9)–(2.13)):

| operator | reconstruction $u^-_{i+1/2}$ | $\mathcal R(\tilde u)$ |
|---|---|---|
| UW1, first-order upwind | $\bar u_i$ | $\tilde u$ |
| DW, first-order downwind | $\bar u_{i+1}$ | $1$ |
| UW2, second-order upwind | $\tfrac32\bar u_i-\tfrac12\bar u_{i-1}$ | $\tfrac32\tilde u$ |
| CD2, second-order central | $\tfrac12\bar u_i+\tfrac12\bar u_{i+1}$ | $\tfrac12\tilde u+\tfrac12$ |
| P3, third-order | $-\tfrac16\bar u_{i-1}+\tfrac56\bar u_i+\tfrac13\bar u_{i+1}$ | $\tfrac56\tilde u+\tfrac13$ |

P3 is the linear scheme of third-order WENO, $P3=\tfrac13UW2+\tfrac23CD2$.
Huang et al. print UW1 as $\bar u_{i-1}$; the normalised form $\tilde u$ they give
belongs to $\bar u_i$.

**Results** ([Deng (2023)](/sources/deng-2023.md), §§2–3):

- *Lemma 1.* With no critical point in the stencil,
  $\tilde u_i=\tfrac12-\frac{u''(x_c)\Delta x}{4u'(x_c)}+O(\Delta x^2)$, so smooth
  monotone data sit near $\tilde u=1/2$.
- *Lemma 2 and Proposition 1.* At a first-order critical point
  $x_c=x_{i-1/2}+\delta\Delta x$ ($\delta\ne1/2$, page-local),
  $\tilde u_i=\delta/(2\delta-1)+O(\Delta x)$; on a fine enough mesh a critical
  point in $I_i$ gives $\tilde u_i<0$ or $\tilde u_i>1$, one in $I_{i-1}$ gives
  $0<\tilde u_i<1/2$, one in $I_{i+1}$ gives $1/2<\tilde u_i<1$.
  *(Compiler check, not in the sources: $\delta/(2\delta-1)$ maps
  $\delta\in(-1,0)$ onto $(0,1/3)$ and $\delta\in(1,2)$ onto $(2/3,1)$, so the
  printed bounds $1/2$ are valid but not sharp.)*
- *Proposition 2.* A normalisable scheme is scale-invariant,
  $u^-_{i+1/2}[\lambda\bar u]=\lambda\,u^-_{i+1/2}[\bar u]$ for $\lambda\ne0$
  (see [scale invariance](/properties/scale-invariance.md)).
- *Proposition 3.* A linear operator is at least second order iff its line passes
  through the **accuracy point** $(1/2,3/4)$.
- *Proposition 4.* It is uniformly third order iff $\mu_0=1/3$,
  $\mu_1=5/6$ (the P3 line). Hence QUICK ($\mu_0=3/8$, $\mu_1=3/4$) is
  not uniformly third order for cell-average data.
- *Proposition 5.* For a second-order linear operator the leading error is
  $4(\tfrac13-\mu_0)(\tfrac12-\tilde u_i)u'(x_c)\Delta x+O(\Delta x^3)$: the
  operator is diffusive for $\mu_0>1/3,\tilde u>1/2$ or
  $\mu_0<1/3,\tilde u<1/2$, and anti-diffusive otherwise. The dissipation sign
  therefore depends on the solution as well as on the coefficients
  (Remark 3.1); see [numerical dissipation](/definitions/numerical-dissipation.md).

## The unified diagram (UND)

[Deng (2023)](/sources/deng-2023.md) (§5, Fig. 9) induces, from the results
above and the schemes recast in §§3–4, five elements; the paper states them, it
does not prove them as a whole:

1. the accuracy point $(1/2,3/4)$ and the P3 line;
2. a **diffusion** region below P3 and an **anti-diffusion** region above it;
3. a **CBC-TVD region** on $0\le\tilde u\le1$, bounded above by DW
   ($\mathcal R=1$), on the right by UW1 ($\mathcal R=\tilde u$) and on the left by
   the line $\mathcal R=k\tilde u$ (page-local slope $k$); $k=2$ is the classical
   TVD region, and "a safe choice for the CFL number is CFL $<1/k$";
4. an **ENO region**, for $\tilde u>1$ (between UW1 and DW) and for $\tilde u<0$
   (between P3, $\mathcal R=0$ and UW1), a "supplementary constraint" because
   "classical ENO constraints are not enough" for the ENO property or optimal
   accuracy;
5. a **high-resolution region**, in three parts bounded by P3 and the lines
   UW2, DW, $\mathcal R=0$, $\tilde u=0$ and $\mathcal R=\tilde u$; in the part
   bounded by UW2, P3 and DW the resolution gain comes from anti-diffusion,
   controlled by the distance to P3, at the price of possible oscillations.

The UND applies to conservative, primitive or characteristic variables, and to
split fluxes in a conservative finite-difference scheme (Deng, §8).
[Huang et al. (2026)](/sources/huang-2026.md) (§3.4) use the left boundary
$k=2.5$, i.e. CBC for CFL $\le0.4$ (citing Deng et al. 2025).
*(Compiler check, not in the sources: inserting $\psi=2r$ and $\psi=2$ into the
normalised flux-limiter form of
[TVD limiters](/definitions/total-variation-diminishing.md),
$\mathcal R=\tilde u+\tfrac12\psi\big(\tilde u/(1-\tilde u)\big)(1-\tilde u)$,
gives $\mathcal R=2\tilde u$ and $\mathcal R=1$: the $k=2$ and DW boundaries are
Sweby's bounds $\psi\le2r$ and $\psi\le2$.)*

## Non-uniform grids

[Deng, Jiang & Yan (2025)](/sources/deng-2025.md) (§2.2–2.3) extend the diagram to three
cells of arbitrary widths; write $h_-=\Delta x_{i-1}$, $h_0=\Delta x_i$, $h_+=\Delta x_{i+1}$
(page-local) and $H=h_-+h_0+h_+$. The normalised variables are unchanged; the linear
operators become, in normalised form (Eqs. (2.13)–(2.15)),

$$\mathrm{UW}:\ \frac{h_-+2h_0}{h_-+h_0}\tilde u,\qquad
\mathrm{CD}:\ \frac{h_+}{h_0+h_+}\tilde u+\frac{h_0}{h_0+h_+},\qquad
\mathrm P:\ \mu_1^{\mathrm P}\tilde u+\mu_0^{\mathrm P},$$

$$\mu_0^{\mathrm P}=\frac{h_0(h_-+h_0)}{(h_0+h_+)H},\qquad
\mu_1^{\mathrm P}=\frac{h_+\big(h_-^2+3h_-h_0+3h_0^2+h_-h_++2h_0h_+\big)}{(h_-+h_0)(h_0+h_+)H},$$

P being the quadratic reconstruction from the three averages (page-local $\mu^{\mathrm P}_0$,
$\mu^{\mathrm P}_1$). The results generalize Propositions 3–5 above:

- *Proposition 1.* A linear operator $\mu_1\tilde u+\mu_0$ is at least second order iff its line
  passes through the **accuracy point**
  $\big(\theta_{\mathrm A},\tfrac{h_-+2h_0}{h_-+2h_0+h_+}\big)$,
  $\theta_{\mathrm A}=\tfrac{h_-+h_0}{h_-+2h_0+h_+}$ (page-local), through which UW, CD and P all pass
  (Eq. (2.18)).
- *Proposition 2.* It is uniformly third order iff $(\mu_0,\mu_1)=(\mu_0^{\mathrm P},\mu_1^{\mathrm P})$.
- *Proposition 3* (Eq. (2.22)). A second-order operator is diffusive if $\mu_0>\mu_0^{\mathrm P}$ and
  $\tilde u>\theta_{\mathrm A}$, or $\mu_0<\mu_0^{\mathrm P}$ and $\tilde u<\theta_{\mathrm A}$, and
  anti-diffusive in the two mixed cases, assuming no critical point in the stencil.

On a uniform grid these reduce to UW2, CD2, P3, the point $(1/2,3/4)$ and Deng's Proposition 5
(Remark 2.1). The non-uniform UND (Fig. 1(a)) keeps the elements listed above: accuracy point and
P line, diffusion and anti-diffusion regions, an ENO region on $0\le\tilde u\le1$ bounded by
first-order downwind ($\mathcal R=1$), first-order upwind ($\mathcal R=\tilde u$) and a line
$\mathcal R=k\tilde u$ with "CFL $<1/k$" called a safe choice, and high-resolution regions
outside $[0,1]$; no formula is printed for the latter. The ROUND operator drawn on it is on the
[ROUND](/methods/round-scheme.md) page.
*(Compiler check, not in the sources: on the cells $[-h_-,0]$, $[0,h_0]$, $[h_0,h_0+h_+]$, the
normalised forms, the common point, Propositions 1–2 and the sign rule of Proposition 3 were
recomputed by Taylor expansion and agree; P errs on a cubic by $h_0h_+(h_-+h_0)u'''/24$.)*

## Schemes on the diagram

- **TVD limiters.** MinMod and SuperBee bound Sweby's second-order TVD region;
  symmetric limiters (van Leer, van Albada, OSPRE) are dissipative for
  $\tilde u<1/2$ and anti-dissipative for $\tilde u>1/2$ and cannot be third
  order; SuperBee is anti-dissipative for $\tilde u$ between about 0.3 and 0.8;
  MinMod is always dissipative (Deng, §4.1). See
  [TVD](/definitions/total-variation-diminishing.md).
- **NVD schemes.** CUBISTA and TOPUS do not fully retrieve P3 on $0<\tilde u<1$
  and stay below the $k=2.5$ line; SMART is meant for implicit stepping; all
  revert to UW1 outside $[0,1]$, which smears critical points (Deng, §4.2).
- **WENO3.** WENO-JS3, WENO-Z3 and WENO-P3 are not normalisable; plotted under
  $\bar u_{i-1}=0$, $\bar u_{i+1}=1$ (a special case Deng calls "not a perfect
  approach"), WENO-JS3 is close to MinMod and WENO-P closer to P3; the third-order
  WENO-P+ leaves the CBC region for its parameter equal to 1 (Deng, §§4.3–4.4).
  A weight depending on $\tilde u_i$ alone makes WENO normalisable and
  scale-invariant (Proposition 6, §6.2).
- **THINC** has the closed normalised form
  $\mathcal R=\dfrac{\sinh\beta_{\mathrm T}+\cosh\beta_{\mathrm T}-e^{\beta_{\mathrm T}(1-2\tilde u)}}{2\sinh\beta_{\mathrm T}}$
  on $0<\tilde u<1$ and $\tilde u$ otherwise (Deng, Eq. (4.33)); see
  [THINC](/methods/thinc-reconstruction.md).
- **ROUND schemes** are designed directly as curves on the UND
  ([ROUND schemes](/methods/round-scheme.md)).
- **A learned scheme.** Sampled on the diagram, the neural-network weights of
  WENO3-NN recover UW2 near $\tilde u=0$, P3 near $1/2$ and CD2 near $1$, stay
  below $2.5\tilde u$ on $(0,1)$, and for $\tilde u<0$ (critical point inside
  cell $i$) leave UW2 and bend toward CD2
  ([Huang et al. (2026)](/sources/huang-2026.md), §3.4, Fig. 2); see
  [learned WENO weights](/methods/learned-weno-weights.md). The network's
  candidates are UW2 and CD2 with linear weights $d_0=1/3$, $d_1=2/3$, i.e. P3
  as the linear limit, in the original paper
  ([Bezgin, Schmidt & Adams (2022)](/sources/bezgin-2022.md), §2, Eqs. (6)–(10)),
  which does not use the diagram.

## Qualifications

- The diagram describes a scheme completely only if it is normalisable. For
  non-normalisable schemes (classical WENO3, WENO3-NN) the plotted curve is one
  section through a two-parameter family, obtained by fixing
  $\bar u_{i-1}=0$, $\bar u_{i+1}=1$; Huang et al. explicitly *assume* the
  network's scale independence when sampling it. Bezgin et al. (2022, §3.2,
  Eqs. (14)–(15)) build that independence in: the network sees only the absolute
  first and second differences of the three averages divided by
  $\max(\lvert\bar u_i-\bar u_{i-1}\rvert,\lvert\bar u_{i+1}-\bar u_i\rvert,\epsilon)$,
  which are invariant under adding a constant and, up to $\epsilon$, under scaling.
  *(Compiler check, not in the sources: the four inputs depend only on the ratio
  $(\bar u_{i+1}-\bar u_i)/(\bar u_i-\bar u_{i-1})=1/\tilde u_i-1$, so up to
  $\epsilon$ the WENO3-NN weights are functions of $\tilde u_i$ alone and, by
  Deng's Proposition 6, the scheme is normalisable; the section Huang et al.
  plot is then the whole scheme.)*
- **Printed slips in the non-uniform proofs.** Deng, Jiang & Yan (2025) print
  $\frac{u''}{u'}=\frac{3(2h_0+h_-h_0+h_+h_0)^2}{(h_-+h_0)(h_-+h_+)H}\big(\theta_{\mathrm A}-\tilde u\big)$
  (Eq. (2.24), in registry and page-local notation), whose numerator mixes lengths and squared
  lengths, and an error prefactor $\tfrac16(\mu_0^{\mathrm P}-\mu_0)h^2$ in Eq. (2.23).
  *(Compiler check, not in the sources: the expansion gives
  $\frac{u''}{u'}=\frac{3(h_-+2h_0+h_+)^2}{(h_-+h_0)(h_0+h_+)H}(\theta_{\mathrm A}-\tilde u)$, $4/\Delta x$ on a
  uniform grid like the printed one, and an error coefficient of $u''$ proportional to
  $(\mu_0^{\mathrm P}-\mu_0)(h_0+h_+)H/6$; both prefactors are positive, so Proposition 3 is
  unaffected.)* The first-order brackets of the expansions also carry slips: Eq. (2.20)
  prints $\mu_0\big(1+\tfrac{h_+}{h_0}+\tfrac{h_-}{h_0}\big)$ and Eq. (2.21) prints the factor
  $\tfrac{h_-}{h_+}$, where the expansion gives $\mu_0\big(2+\tfrac{h_+}{h_0}+\tfrac{h_-}{h_0}\big)$ (the
  $2\mu_0$ of (2.21)) and $\tfrac{h_-}{h_0}$ *(compiler check, not in the sources)*; the
  second-order condition and Propositions 1–2 agree with the compiler check above.
- The CBC–CFL link ($k\leftrightarrow$ CFL $<1/k$) is stated, not derived, in both
  sources; Deng also reports, after Giuliani and Krivodonova, that the TVD bound
  CFL $<0.5$ is "overly stringent" with high-order SSP Runge–Kutta stepping.
- "Order" on the diagram is the formal truncation order of the face value from
  cell averages; neither source tabulates observed orders for Deng's schemes,
  and Huang et al.'s Table 3 gives $L_1$ orders 2.4–2.6 for the compact schemes
  it tests.

# Citations

- [Deng (2023)](/sources/deng-2023.md) — §§2–5, Definitions 1–8, Lemmas 1–2, Propositions 1–6, Table 1, Figs. 2–9, Eqs. (3.1)–(4.33).
- [Huang et al. (2026)](/sources/huang-2026.md) — §2.2, Eqs. (2.6)–(2.13); §3.4, Fig. 2.
- [Bezgin, Schmidt & Adams (2022)](/sources/bezgin-2022.md) — §2, Eqs. (6)–(10); §3.2, Eqs. (14)–(15).
- [Deng, Jiang & Yan (2025)](/sources/deng-2025.md) — §2.2–2.3, Eqs. (2.13)–(2.25), Propositions 1–3, Remark 2.1, Fig. 1.
