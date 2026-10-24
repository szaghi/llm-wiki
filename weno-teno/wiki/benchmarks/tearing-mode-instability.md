---
type: Benchmark
title: "Tearing-mode instability"
description: "Resistive or numerically resistive instability of a Harris-type current sheet in (relativistic) MHD: a small perturbation grows into magnetic islands and plasmoids; its growth rate, compared with tearing theory, measures the effective dissipation of a high-order scheme, here resistive relativistic MHD at fourth order and ideal relativistic MHD at high magnetization."
status: established
aliases: [tearing mode, tearing instability, ideal tearing mode, Harris current sheet, Harris sheet, plasmoid instability]
tags: [benchmark, mhd, relativistic, low-dissipation]
timestamp: 2026-10-24T05:58:00Z
---

# Tearing-mode instability

A current sheet, in which the magnetic field reverses across a thin
layer, is unstable to the tearing mode: a perturbation of wavenumber
along the sheet reconnects field lines and grows into chains of
magnetic islands (O-points) separated by X-points, and in thin sheets
into plasmoids. The growth rate depends on the resistivity through the
Lundquist number. As a benchmark the test is run either with a
physical resistivity, where the measured growth rate converges to the
theoretical one as the grid is refined, or without one, where the
scheme's own numerical resistivity sets the rate. Both uses make it a
direct probe of [numerical dissipation](/definitions/numerical-dissipation.md)
in MHD.

Page-local symbols: $a$ the half-thickness of the sheet, $L$ a length
along it, $\eta_{\mathrm m}$ the magnetic resistivity (not the entropy
$\eta$), $v_{\mathrm A}$ the Alfvén speed, $S=Lv_{\mathrm A}/\eta_{\mathrm m}$
and $S^*=av_{\mathrm A}/\eta_{\mathrm m}$ the Lundquist numbers on $L$ and
on $a$, $k_y$ the perturbation wavenumber along the sheet, and
$\omega_{\mathrm{TM}}$ the growth rate (not the WENO weights
$\omega_k$), and $\mathcal E$ the electric field (not the total energy
$E$). Units are those of the sources: $c=1$, no $4\pi$.

## Theory used by the sources

[Komissarov & Phillips (2024)](/sources/komissarov-2024.md) §5.4
(arXiv v3), Eqs. (103)–(112), recall the classical resistive results of
Furth, Killeen & Rosenbluth (1963) for the fastest-growing mode,

$$
k_ya\approx1.4\,S^{*-1/4},\qquad
\omega_{\mathrm{TM}}\frac{a}{v_{\mathrm A}}\approx0.63\,S^{*-1/2},
$$

and the aspect ratios at which a sheet fragments: Sweet–Parker
$a/L\simeq S^{-1/2}$ and Pucci–Velli $a/L=S^{-1/3}$.

[Mignone et al. (2024)](/sources/mignone-2024.md) §4.5, following Del
Zanna et al. (2016), run the **ideal tearing** regime, in which the
sheet thickness is tied to the Lundquist number, $a=S^{-1/3}L$
(their Eq. 64). They state that for large $S$ the growth rate becomes
$\omega_{\mathrm{TM}}\simeq0.6\,v_{\mathrm A}/L$, independent of the
resistivity, "commonly referred to as ideal tearing", and print the
fastest wavenumber $k_{\max}=1.4S^{1/6}=14$ with growth rate
$\simeq0.3$. With this thickness $S^*=S^{2/3}$, so Furth's relations
give $k_y=1.4\,S^{1/6}/L$ and $\omega_{\mathrm{TM}}=0.63\,v_{\mathrm A}/L$,
which is $0.315$ for $v_{\mathrm A}=0.5$, $L=1$ *(compiler check, not in
the sources)*.

## Setups

**Force-free Harris sheet, resistive relativistic MHD.** Mignone et
al. (2024) §4.5, Eqs. (63)–(67):

$$
B=B_0\Big(\tanh\frac{x}{a}\,\hat e_y+\operatorname{sech}\frac{x}{a}\,\hat e_z\Big),\qquad
\mathcal E=0,\qquad v=0,
$$

uniform $\rho$ and $p$, perturbed with relative amplitude $10^{-4}$
through the vector potential
$\mathcal A_z=-B_0\big[a\log\cosh(x/a)-\tfrac{10^{-4}}{k_y}\sin(k_yy)\operatorname{sech}(x/a)\big]$.
Parameters: $L=B_0=1$, magnetization $B_0^2/\rho_0=1$ and plasma beta
$2p_0/B_0^2=1$, hence $\rho_0=1$, $p_0=0.5$, $v_{\mathrm A}=0.5$;
$S=10^6$, $a=0.01$, $\eta_{\mathrm m}=5\times10^{-7}$; $k_y=12$,
shifted from $k_{\max}=14$ by compressibility, with expected growth
rate $\omega_{\mathrm{TM}}\simeq0.27$. Domain $x\in[-0.2,0.2]$ with
outflow boundaries, $y\in[0,0.523598]$ periodic (one wavelength
$2\pi/12$), grids $N_x\times N_x/4$ with $N_x=256,\dots,2048$, $t=20$,
$\gamma=4/3$, IMEX SSP3(4,3,3). The growth rate is read from
$\tfrac12\log\int B_x^2\,dS$ (their Eq. 67). The printed parameters are
consistent: $v_{\mathrm A}=B_0/\sqrt{\rho_0+4p_0+B_0^2}=1/\sqrt4=0.5$ and
$\eta_{\mathrm m}=v_{\mathrm A}L/S=5\times10^{-7}$ *(compiler check, not in
the sources)*.

**Harris sheet at high magnetization, ideal relativistic MHD.**
Komissarov & Phillips (2024) §5.4: $B_1=B_0\tanh(y/a)$ with pressure
balance, $\rho_0=p_0=1$, $B_0=500$, $a=0.01$, magnetization
$\lvert B\rvert^2/w_{\mathrm h}=5\times10^4$ ($w_{\mathrm h}$ the relativistic enthalpy
density, page-local); domain $(-1,1)^2$ with $400^2$ points, periodic
in $x$, zero-gradient in $y$, $\gamma=4/3$. The perturbation is
$B_2=\sum_{j=1}^{20}A_j\sin(\pi jx/L+2\pi r_j)$ with $A_j=10^{-5}B_0$
and random phases $r_j$ ($A_j$, $r_j$ page-local); a single-mode run uses
$B_2=10^{-4}\sin6\pi x$. No physical resistivity is present: the
sheet tears through the numerical resistivity of their third-order
finite-difference scheme with
[force-free splitting](/methods/force-free-splitting-rmhd.md), HLL
fluxes and [GLM cleaning](/methods/glm-divergence-cleaning.md); the DER
step (the central-interpolation flux divergence of Del Zanna et al.
2007) "had to be switched off" for this test to avoid conversion
failures at shocks (§5.4.2). With
$w_{\mathrm h}=\rho_0+4p_0=5$ the magnetization is $500^2/5=5\times10^4$
*(compiler check, not in the sources)*.

Komissarov & Phillips §4.2 also run a one-dimensional Harris sheet
($B_2=B_0\tanh(x/a)$, $p=p_0+\tfrac12B_0^2(1-\tanh^2(x/a))$, $\rho=1$,
$B_0=500$, $p_0=1$, $a=0.02$, $(-5,5)$ with 500 points, to $t=5$), not
for tearing but to measure the heating of the sheet and the energy
non-conservation of the split scheme for several values of its
energy-transfer threshold (Table 2).

## Results

**Growth rate against order.** Mignone et al. (2024) Table 1 print the
measured $\omega_{\mathrm{TM}}$:

| Grid | $256\times64$ | $512\times128$ | $1024\times256$ | $2048\times512$ |
|---|---|---|---|---|
| second order (their earlier scheme) | 1.19 | 0.89 | 0.58 | 0.38 |
| fourth order | 0.75 | 0.44 | 0.30 | 0.27 |

The fourth-order scheme reaches the expected 0.27 and "requires
approximately half of the resolution (or less)" of the second-order
one for the same rate.

**Linear phase from numerical resistivity.** Komissarov & Phillips
§5.4.1 measure $\omega_{\mathrm{TM}}\approx2.7$, $2.0$ and $1.7$ in
successive unit time intervals and infer, from Furth's growth-rate
relation, $320<S^*<480$; the corresponding fastest wavelength,
$0.25<\lambda<0.36$ ($\lambda$ page-local), matches the observed $0.33$ (six plasmoids along
the sheet). They model the numerical resistivity of their scheme as
$\eta_{\mathrm{num}}=A_\eta L_B(\Delta x/\Delta t)(\Delta x/L_B)^3$, with
$L_B$ the length scale of the field and $A_\eta\approx0.031$ calibrated
on a decaying Alfvén wave (§4.3, Eq. 91; page-local symbols), and with
$A_\eta=0.034$ estimate $\eta_{\mathrm{num}}\approx10^{-4}$ in the
sheet.

**Nonlinear plasmoid phase.** In the plasmoid-dominated phase to
$t=10$ the global reconnection rate, from the growth of the energy, is
about $0.04$, and the inflow speed near an X-point is about $0.05$,
"only slightly below" the rate of about $0.1$ they call universal
(§5.4.2, Figs. 16–19). The authors call their study "the first"
more-or-less systematic one of plasmoid-dominated reconnection with
ideal relativistic MHD codes (§6). Their error estimate for the
unsplit "standard" mode, the relative field error times magnetization
over $W^2$, reaches about 20 near the tearing sheets (§5.6), a value
above 1, for which they predict conversion failures of that mode.

**Related.** On the [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md),
[Berta et al. (2024)](/sources/berta-2024.md) use the magnetic island
that forms in the central current sheet as a qualitative measure of
dissipation, recalling that tearing develops on ideal time scales only
if the numerical dissipation is low enough.

## Qualifications

- The two sources measure different things: Mignone et al. converge a
  physically resistive growth rate to a reference value; Komissarov &
  Phillips have no physical resistivity and use tearing theory to
  infer the effective Lundquist number of their scheme.
- Komissarov & Phillips print the length scale entering
  $\eta_{\mathrm{num}}$ as $L_B=\tfrac{a}{\sqrt2}\cosh\tfrac{x}{a}$ for a
  sheet that varies in $y$, and "at $x=a$, $L\approx0.009$"; the
  printed formula at one sheet half-thickness gives
  $0.01\cosh1/\sqrt2\approx0.0109$ *(compiler check, not in the
  sources)*. Their $\eta_{\mathrm{num}}\approx10^{-4}$ follows from the
  printed $0.009$. The values of $a$ behind $320<S^*<480$ are not
  stated.
- For the one-dimensional sheet Komissarov & Phillips print the
  asymptotic magnetization as $54500$; with the same $B_0=500$,
  $\rho_0=p_0=1$ their §5.4 prints $5\times10^4$, which $w_{\mathrm h}=\rho+4p=5$
  reproduces *(compiler check, not in the sources)*.
- Mignone et al.'s text calls the second-order data "dotted lines",
  their Fig. 6 caption "dashed"; the table values are unaffected.

# Citations

- [Komissarov & Phillips (2024)](/sources/komissarov-2024.md) — §4.2, §4.3 Eq. (91), §5.4, §5.6, Eqs. (103)–(112), Table 2, Figs. 16–19 (arXiv v3).
- [Mignone et al. (2024)](/sources/mignone-2024.md) — §4.5, Eqs. (63)–(67), Table 1, Fig. 6.
- [Berta et al. (2024)](/sources/berta-2024.md) — §5.6, Figs. 9–10 (arXiv v4).
