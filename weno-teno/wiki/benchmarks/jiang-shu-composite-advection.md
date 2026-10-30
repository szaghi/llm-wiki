---
type: Benchmark
title: "Jiang–Shu composite-wave advection"
description: "Linear advection of Jiang and Shu's four-wave profile, a smooth narrow Gaussian, a square wave, a triangle and a half ellipse, over one to a thousand periods; it tests at once the resolution of smooth peaks, the absence of oscillations at jumps and kinks, symmetry and long-time dissipation of nonlinear reconstructions, mostly by eye, once by L1 errors."
status: established
aliases: [Jiang–Shu multi-wave test, multi-wave advection, multiple-wave advection, composite wave, Shu linear advection test, Gaussian–square–triangle–ellipse test]
tags: [benchmark, weno, teno, reconstruction, low-dissipation]
timestamp: 2026-10-30T07:59:00Z
---

# Jiang–Shu composite-wave advection

The scalar linear advection equation $\partial_tu+\partial_xu=0$ on a
periodic interval carries its initial data unchanged, so after any
whole number of periods the exact solution is the initial profile. The
composite profile of [Jiang & Shu (1996)](/sources/jiang-1996.md) (§8.1
Ex. 1), to whom the later sources attribute it, puts four
waves of different regularity side by side on $[-1,1]$: a narrow smooth
Gaussian, a square wave (two jumps), a triangle (kinks and a sharp
peak) and a half ellipse (a smooth top with infinite slope at its
feet). One run thus shows whether a reconstruction clips a smooth peak,
oscillates at a jump, smears a kink, keeps the profile symmetric and,
over many periods, how much it dissipates and distorts the waves. Most
sources judge it by eye; [Borges et al. (2008)](/sources/borges-2008.md)
print $L_1$ errors and orders (Table 4).

## Data

With page-local $G(x,\beta_{\mathrm G},z)=e^{-\beta_{\mathrm G}(x-z)^2}$ and
$F(x,\alpha_{\mathrm F},a)=\sqrt{\max\big(1-\alpha_{\mathrm F}^2(x-a)^2,0\big)}$,
the form printed by Jiang & Shu (§8.1 Ex. 1), Borges et al. (Eq. (44)),
[Li et al. (2022b)](/sources/li-2022-b.md) §4.2,
[Abgrall et al. (2026)](/sources/abgrall-2026.md) Ex. 1 and
[Cao et al. (2026)](/sources/cao-2026.md) Ex. 6.5 is

$$
u_0(x)=\begin{cases}
\tfrac16\big[G(x,\beta_{\mathrm G},z-\delta_{\mathrm G})+G(x,\beta_{\mathrm G},z+\delta_{\mathrm G})+4G(x,\beta_{\mathrm G},z)\big], & -0.8\le x\le-0.6,\\
1, & -0.4\le x\le-0.2,\\
1-\lvert10(x-0.1)\rvert, & 0\le x\le0.2,\\
\tfrac16\big[F(x,\alpha_{\mathrm F},a-\delta_{\mathrm G})+F(x,\alpha_{\mathrm F},a+\delta_{\mathrm G})+4F(x,\alpha_{\mathrm F},a)\big], & 0.4\le x\le0.6,\\
0, & \text{otherwise},
\end{cases}
$$

with $a=0.5$, $z=-0.7$, $\delta_{\mathrm G}=0.005$, $\alpha_{\mathrm F}=10$ and
$\beta_{\mathrm G}=\ln2/(36\delta_{\mathrm G}^2)$ (page-local symbols; the
sources' $\beta$, $\alpha$, $\delta$ or $\theta$). The Gaussian and the
ellipse are each averaged with Simpson weights over three centres
$\delta_{\mathrm G}$ apart. With these constants $\beta_{\mathrm G}=\ln2/0.0009$,
so a single Gaussian falls to half its peak at
$\lvert x-z\rvert=0.03$, and the ellipse has half-width $1/\alpha_{\mathrm F}=0.1$
*(compiler check, not in the sources)*. Jiang & Shu and Borges et al.
print the constant as $\log2/(36\delta^2)$ without a base; the natural
logarithm of this page is the reading of Yajaman et al., who print
$\ln2$ (below).

| Source | Domain | Grid | Time | Time stepping | Schemes compared |
|---|---|---|---|---|---|
| [Jiang & Shu (1996)](/sources/jiang-1996.md) §8.1 Ex. 1 | $(-1,1)$, periodic | 200 | $t=8$ (4 periods) | RK-3, CFL 0.4 (0.2 for WENO-Roe-5-A) | fourth- and fifth-order finite-difference WENO with Roe building block (WENO-Roe-4, WENO-Roe-5) and with Yang's artificial compression (WENO-Roe-5-A), against ENO-Roe-4 |
| [Borges et al. (2008)](/sources/borges-2008.md) §5.1, Eq. (44) | $[-1,1]$, periodic | 50–1600 (Table 4); figures at 200 and 400 | $t=8$ | third-order TVD Runge–Kutta | [WENO-Z](/methods/weno-z.md) against [mapped WENO](/methods/mapped-weno.md) (WENO-M) and [WENO-JS](/methods/weno-js-reconstruction.md) |
| [Li et al. (2022b)](/sources/li-2022-b.md) §4.2, Eqs. (34)–(36) | $[-1,1]$, periodic | 200 | $t=10$ (5 periods) | — | seventh-order [WENO-ZN](/methods/weno-zn.md) against WENO7-Z and other seventh-order schemes |
| [Takagi et al. (2022)](/sources/takagi-2022.md) §4.2, Eqs. (24)–(26) | $[0,2]$ | 200; 400 | $t=200$; $t=2000$ | SSP-RK3; five-stage fourth-order SSP-RK | [TENO-THINC](/methods/teno-thinc.md), TENO5, WENO5-Z |
| [Huang et al. (2023b)](/sources/huang-2023-b.md) §4.2, Eqs. (38)–(40) | $[0,2]$, profile shifted by 1 | 200 | $t=2$; $t=18$ | SSP-RK3, CFL 0.4 | [adaptive-dissipation TENO](/methods/adaptive-teno.md), TENO5-A, TENO5, WENO5-Z |
| [Wang & Don (2022)](/sources/wang-2022-b.md) §3.2.1 | $[-1,1)$, periodic | 200 | $t=2$ | TVD-RK3, CFL 0.45 | [affine-invariant WENO-Z](/methods/affine-invariant-weno.md) against scale-invariant WENO-Z, on scaled and translated data |
| [Abgrall et al. (2026)](/sources/abgrall-2026.md) Ex. 1 | $[-1,1]$, periodic | 400 | $t=2$ (1 period) | SSP-RK3, CFL 0.2 | bound-preserving [PAMPA](/methods/pampa-scheme.md), strict and relaxed bounds |
| [Yajaman, Toro & Demattè (2025)](/sources/yajaman-2025.md) §6, Eq. (56) | $[-1,1]$, periodic | 200 | $t=2000$ (1000 periods) | ADER, CFL 0.9 | [AENO-C](/methods/aeno-reconstruction.md) against WENO, orders 5–10 |
| [Cao et al. (2026)](/sources/cao-2026.md) Ex. 6.5 | $[-1,1]$, periodic | 256 cells | $t=6$ (3 periods) | SSP-RK3 | global [COS(DG)](/methods/cos-dg.md), $\mathbb P^1$–$\mathbb P^3$ |

Takagi et al. print the domain $[0,2]$ with the Jiang–Shu constants;
Huang et al. (2023b) print the pieces explicitly as functions of $x-1$
on $[0.2,0.4)$, $[0.6,0.8]$, $[1.0,1.2]$ and $[1.4,1.6)$, the same profile
moved by one unit. Wang & Don do not print the formula of their
"multi-wave" profile, so its identity with the Jiang–Shu data is not
established by the paper; they advect $\sigma u_0+\mu$ with
$\sigma=10^{-7}$ and $\mu\in\{0,1\}$ (the affine-map symbols of the
registry) and $\epsilon=10^{-12}$.

Yajaman et al. print a single Gaussian
$\exp\big(-\ln2\,(x+0.7)^2/0.0009\big)$ and a single half ellipse
$\big(1-100(x-0.5)^2\big)^{1/2}$, without the three-point averages; the
constants are the same ($0.0009=36\delta_{\mathrm G}^2$, $100=\alpha_{\mathrm F}^2$)
*(compiler check, not in the sources)*. Their 1000 periods at CFL 0.9
on 200 cells take $2000/(0.9\times0.01)\approx222{,}222.2$ steps, printed
as 222,223 *(compiler check, not in the sources)*.

## Findings

**The original comparison.** Jiang & Shu find both WENO-Roe-4 and
WENO-Roe-5 better than ENO-Roe-4 on all four waves; WENO-Roe-4 is the
better of the two at acute turns of the profile ("spike-like peaks"),
WENO-Roe-5 on the square wave and at obtuse turns, and with
[artificial compression](/methods/artificial-compression.md)
WENO-Roe-5-A is best on every wave. They lower its CFL number to 0.2;
at 0.4 a compression parameter of 40 gives similar results (Fig. 2).

**Errors under refinement.** Borges et al. print $L_1$ errors from 50
to 1600 points: at 1600, $9.93\times10^{-3}$ for WENO-JS,
$7.73\times10^{-3}$ for WENO-Z and $8.06\times10^{-3}$ for WENO-M, all
three converging at about first order, and WENO-Z "quantitatively and qualitatively equivalent to
WENO-M" (Table 4, Figs. 4–5).

**Square wave and symmetry at seventh order.** Li et al. (2022b) find
WENO7-ZN the best of the seventh-order schemes, "especially" on the
square wave and the half ellipse, while WENO7-Z gives a visibly
asymmetric solution near the square wave (Fig. 3); see
[WENO-Z](/methods/weno-z.md).

**Sharpening the square wave over long times.** Takagi et al.'s
TENO-THINC, which replaces the TENO reconstruction by a THINC jump
profile in cells judged discontinuous, keeps the square wave markedly
better than WENO5-Z and TENO5 at $t=200$ and at $t=2000$, while the
Gaussian, triangle and half ellipse are similar to TENO5 (Figs. 2–3).

**Long-time oscillations of adaptive TENO.** In Huang et al. (2023b) at
$t=2$ TENO5-A and their scale-sensor scheme are indistinguishable, and
both capture the Gaussian and the triangle more sharply than WENO5-Z
and TENO5 (Fig. 4). At $t=18$ TENO5-A shows "obvious oscillations even
in the smooth regions", while the new scheme keeps the overall shape and
the square wave sharp (Fig. 5).

**The ENO property under an affine map.** On Wang & Don's translated
data of amplitude $10^{-7}$, the scale-invariant WENO-Z reverts to its
linear scheme, because the regularization $\epsilon$ swamps smoothness
indicators of order $10^{-14}$, and shows Gibbs oscillations; the
affine-invariant WENO-Z is non-oscillatory, with pointwise errors
identical for $\mu=0$ and $\mu=1$ (Figs. 4–5); see
[scale invariance](/properties/scale-invariance.md).

**Bounds without oscillations.** Abgrall et al.'s bound-preserving
PAMPA scheme, which evolves cell averages and point values with blended
low- and high-order fluxes and residuals, stays within $[0,1]$ with
strict bounds and within $[-0.001,1.001]$ with relaxed ones, and is
non-oscillatory after one period on 400 cells (Fig. 1). The relaxed
bounds matter for accuracy: on smooth advection, strict global bounds
lower the $L^\infty$ rate to about 1.8, and relaxed ones restore third
order (their Ex. 1, Tables 1–2).

**A thousand periods at orders up to ten.** Yajaman et al. find that
ADER with AENO-C keeps the shape of all four waves without overshoots
at every order from 5 to 10, while WENO is prone to spurious
oscillations near the discontinuities and sharp gradients (Fig. 11).
They also report occasional undershoots of AENO-C near discontinuities,
for instance at order 6, which they attribute to the reconstruction
keeping too much information from the centred stencil, call not
spurious oscillations, and see decrease with resolution (§5.2, §9).

**A post-processed DG.** Cao et al. (2026) run the profile with global
COS(DG), which blends each cell polynomial with its cell average once
per time step through a coefficient driven by the jumps to the two
neighbours, at $\mathbb P^1$, $\mathbb P^2$ and $\mathbb P^3$: higher
degrees give sharper resolution, and spurious oscillations are, in
their words, fully suppressed (Fig. 5). The same paper advects two
other piecewise-smooth profiles on 256 cells, one on $[-1,1]$ to $t=8$
and one on $[0,1]$ to $t=1.1$, with the same verdict (Exs. 6.3–6.4,
Figs. 3–4).

**A static detection test.** [Liang & Fu (2026)](/sources/liang-2026.md)
§3.3 use the profile without advecting it: shifted to $[0,2]$ as in
Huang et al. (2023b) (Gaussian on $[0.2,0.4)$, square wave on
$[0.6,0.8]$, triangle $1-\lvert10(x-1.1)\rvert$ on $[1.0,1.2]$, half
ellipse on $[1.4,1.6)$, same constants), sampled on $N=400$ points, it is
the fourth of four static functions on which they show that their
discontinuity-detecting variable, the minimum over the three stencil
pairs of a normalized agreement between the TENO smoothness indicators
$\beta_k$, taking values in $(0,1]$, flags the jumps and the non-smooth
regions (Fig. 3). The variable drives the mesh adaptation of their
finite-volume [converged ENO](/methods/converged-eno.md) scheme with
multiresolution [adaptive mesh refinement](/methods/adaptive-mesh-refinement.md):
a block is refined below 0.3 and coarsened above 0.7.

## Qualifications

- Apart from Borges et al.'s $L_1$ errors, the findings are visual
  comparisons of plotted profiles (Liang & Fu's use is a static plot of
  the detector); no other source reports an error norm, a convergence
  rate or a measure of dissipation on this test, and the grids, times
  and stepping differ between sources, so results are not comparable
  across papers.
- Li et al. (2022b) print $F(x,\alpha,a)=\sqrt{\max(1-\alpha^2(x-\alpha)^2,0)}$,
  with $\alpha$ in place of $a$ inside the square; the form with $a$, as
  printed by Abgrall et al. and Huang et al. (2023b), is the one that
  centres the ellipse at $x=0.5$.
- Yajaman et al.'s Fig. 11 caption calls the test "the Shu linear
  advection test", while their §6 attributes it to Jiang and Shu.
- Jiang & Shu print the domain as $-1<x<1$; their fourth- and
  fifth-order scheme names count the order in the $L^1$ sense.
- Takagi et al. do not state the boundary condition.

# Citations

- [Jiang & Shu (1996)](/sources/jiang-1996.md) — §8.1, Ex. 1, Fig. 2 (author preprint).
- [Borges et al. (2008)](/sources/borges-2008.md) — §5.1, Eq. (44), Table 4, Figs. 4–5.
- [Li et al. (2022b)](/sources/li-2022-b.md) — §4.2, Eqs. (34)–(36), Fig. 3.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §4.2, Eqs. (24)–(26), Figs. 2–3.
- [Huang et al. (2023b)](/sources/huang-2023-b.md) — §4.2, Eqs. (38)–(40), Figs. 4–5.
- [Wang & Don (2022)](/sources/wang-2022-b.md) — §3.2.1, Figs. 4–5.
- [Abgrall et al. (2026)](/sources/abgrall-2026.md) — §4, Ex. 1, Tables 1–2, Fig. 1.
- [Yajaman, Toro & Demattè (2025)](/sources/yajaman-2025.md) — §5.2, §6, §9, Eq. (56), Fig. 11.
- [Liang & Fu (2026)](/sources/liang-2026.md) — §3.3, Eqs. (27)–(28), Fig. 3.
- [Cao et al. (2026)](/sources/cao-2026.md) — Exs. 6.3–6.5, Figs. 3–5.
