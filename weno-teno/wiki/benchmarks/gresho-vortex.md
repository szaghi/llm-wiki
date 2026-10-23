---
type: Benchmark
title: "Gresho vortex"
description: "Two-dimensional vortex in exact equilibrium between a piecewise-linear azimuthal velocity and its pressure field, advected through or held in a periodic square; used to test whether a compressible scheme's dissipation stays bounded as the Mach number goes to zero, for semi-implicit all-Mach schemes and learned WENO weights, and as a stationary-state test of Active Flux."
status: established
aliases: [Gresho–Chan vortex, triangular vortex, low-Mach Gresho vortex]
tags: [benchmark, low-dissipation, asymptotic-preserving, machine-learning]
timestamp: 2026-10-23T11:06:00Z
---

# Gresho vortex

The Gresho vortex is a stationary solution of the incompressible and of
the compressible Euler equations: an azimuthal velocity $v_\theta(r)$
that rises linearly to a peak at $r=R/2$ and falls linearly to zero at
$r=R$, held in equilibrium by a pressure field with
$\partial_rp=\rho v_\theta^2/r$, at uniform density. Put on a uniform
stream in a periodic square, the exact solution is the initial vortex
translated. At low Mach number the pressure variation is of the order
of the Mach number squared, and an upwind scheme whose numerical
viscosity scales with the sound speed smears the vortex; the test thus
measures whether a scheme's dissipation is uniform in the Mach number.
Here $r$ is the distance to the vortex centre ($(0.5,0.5)$, or the
origin in Chudzik et al.) and
$v_\theta$ the azimuthal velocity (page-local).

## Data

Boscarino et al. and Bezgin et al. place the vortex of radius $R=0.4$ at the centre of the
periodic unit square with $\rho=1$ and a background pressure of 1, and
print the velocity profile
$$
v_\theta(r)=V\cdot\begin{cases}2r/R,&0\le r<R/2,\\ 2(1-r/R),&R/2\le r<R,\\ 0,&r\ge R,\end{cases}
$$
superposed on a uniform stream in $x$, with the matching pressure
$$
p=1+P\cdot\begin{cases}2(r/R)^2+2-\ln16,&0\le r<R/2,\\ 2(r/R)^2-8r/R+4\ln(r/R)+6,&R/2\le r<R,\\ 0,&r\ge R.\end{cases}
$$
The sources differ in how the Mach number enters (page-local $V$
and $P$ are the velocity and pressure scales):

- [Boscarino et al. (2022)](/sources/boscarino-2022.md) Ex. 5.5 (arXiv
  v2) solve the Euler equations in an all-Mach scaling with a
  parameter $\varepsilon$ that multiplies the pressure gradient as
  $1/\varepsilon^2$ (page-local; the Mach-number scale): $V=1$,
  $P=\varepsilon^2$, background stream $0.1$ in $x$, $c_\infty=\sqrt\gamma$,
  $\varepsilon=10^{-1},10^{-2},10^{-6}$, $\gamma=1.4$. One period is
  $T=\pi R$, and they run up to two periods.
- [Bezgin et al. (2022)](/sources/bezgin-2022.md) §4.5 solve the
  unscaled Euler equations with $V=P^{1/2}=u_0=M_0c_0$, $c_0=\sqrt{\gamma p_0/\rho_0}$,
  $M_0=0.01$, background stream $u_0$ in $x$, $\gamma=1.4$, on
  $96\times96$ cells to $t=1/u_0=84.515$.

- [Chudzik et al. (2024)](/sources/chudzik-2024.md) Ex. 7.2 hold the
  vortex at rest at the centre of the periodic square
  $[-0.75,0.75]^2$, with $\rho=1$, $V=1$, $R=0.4$ (their velocity
  $5r$ for $r\le0.2$, $2-5r$ for $0.2<r\le0.4$) and the printed pressure
  $5+\tfrac{25}2r^2$, $9-4\ln0.2+\tfrac{25}2r^2-20r+4\ln r$ and $3+4\ln2$
  on the three ranges, with $\gamma=1.4$; $64^2$ cells, CFL $\le0.275$,
  $t=3$, no limiter.

Chudzik et al.'s pressure is the profile above with $P=1$ and
background pressure $3+4\ln2\approx5.77$ in place of 1: with $R=0.4$,
$2(r/R)^2=\tfrac{25}2r^2$ and $3+4\ln2+2-\ln16=5$, and the middle branch
gives $3+4\ln2+6-4\ln0.4=9-4\ln0.2$. The larger background pressure sets
the peak Mach number to about $1/\sqrt{1.4\times5.5}\approx0.36$, so their
run is a moderate-Mach stationarity test, not a low-Mach one, and $t=3$
is about 2.4 rotation periods $\pi R/V$ *(compiler check, not in the
sources)*.

The pressure is the radial-equilibrium integral of $v_\theta^2/r$ with
$\rho=1$, continuous at $r=R/2$ (both branches equal $2.5-\ln16$) and
zero at $r=R$, and the period of the rigidly rotating core, angular speed
$2V/R$, is $\pi R/V$ *(compiler check, not in the sources)*. Bezgin et
al.'s final time $1/u_0=84.515$ (with $u_0=0.011832$) is one passage of
the vortex through the unit periodic square, so the exact solution then
coincides with the initial data; it is about 0.8 of a rotation period
$\pi R/u_0\approx106.2$ *(compiler check, not in the sources)*. Boscarino
et al.'s background stream of 0.1 moves the vortex by 0.25 over two
periods $2\pi R\approx2.51$ *(compiler check, not in the sources)*.

## Findings

**Uniformity in the Mach number.** Boscarino et al. run their
fourth-order-space, third-order-time
[semi-implicit all-Mach scheme](/methods/semi-implicit-all-mach-scheme.md)
S4T3 and its second-order counterpart S2T2 on $100^2$ and $200^2$ cells.
Both keep the shape relatively well over two periods, S4T3 a little
better; the averaged kinetic energy of the perturbation,
$\sum_{i,j}[(v_1-0.1)^2+v_2^2]/(N_xN_y)$, is "well maintained", clearly
better with S4T3 on $100^2$, the differences shrinking on $200^2$,
especially for small $\varepsilon$ (Fig. 5.6). A local Mach ratio
$\sqrt{[(v_1-0.1)^2+v_2^2]/(\gamma p/\rho)}$ is also shown. They present
the test as evidence that the dissipation of the scheme does not depend
on $\varepsilon$, in line with its
[asymptotic preservation](/properties/asymptotic-preservation.md);
explicit upwind schemes, whose viscosity scales as $\varepsilon^{-1}$ at
low Mach number, are the background they cite.

**Learned three-point weights.** Bezgin et al. use the vortex at
$M_0=0.01$ for their data-driven [WENO3-NN](/methods/learned-weno-weights.md)
scheme with a local Lax–Friedrichs flux, characteristic reconstruction
and TVD-RK3: WENO3-JS and WENO3-Z strongly deform the vortex, WENO3-NN
only slightly smears it compared with WENO5-JS, and the variant NN1 is
sharper but noisier than NN2 (Fig. 13).

**Active Flux, stationary.** Chudzik et al. run the vortex at rest
with their third-order [Active Flux](/methods/active-flux.md) method for
the nonlinear Euler equations, in which point values are evolved by a
linearized bicharacteristic (EG2) operator. The density, initially 1,
stays between $0.999275$ and $1.001377$ at $t=3$ on $64^2$, and the
circular geometry of the pressure and of $\lvert v\rvert$ is well
preserved (Ex. 7.2, Figs. 20–21). The same velocity field is their
stationary acoustic and linearized-Euler vortex, where the exact
acoustic evolution operator preserves the discrete steady state and EG2
does not exactly but stays close to the exact vorticity profile up to
$t=100$ (Ex. 5.2, 6.4; §5.3).

The first two sources reach their low-Mach behaviour by different means: a
semi-implicit treatment of the acoustic part in Boscarino et al., a
lower-dissipation explicit reconstruction in Bezgin et al.

## Qualifications

- Boscarino et al. print the middle pressure branch as
  $2(r/R)^2-4\big(2r/R+\ln(r/R)\big)+6$. That branch is discontinuous at
  $r=R/2$ (it gives $2.5+\ln16$ against $2.5-\ln16$ from the inner
  branch) and does not satisfy the radial balance; the form above, with
  $+4\ln(r/R)$, is the one Bezgin et al. print and the one that
  integrates $v_\theta^2/r$ *(compiler check, not in the sources)*.
- No source reports an error norm; Boscarino et al. and Bezgin et al.
  judge by contours and, in Boscarino et al., by the kinetic-energy
  history, Chudzik et al. by the density range and contours.

# Citations

- [Boscarino et al. (2022)](/sources/boscarino-2022.md) — Ex. 5.5, Eqs. (5.9)–(5.11), Fig. 5.6 (arXiv v2).
- [Bezgin et al. (2022)](/sources/bezgin-2022.md) — §4.5, Eqs. (34)–(36), Fig. 13.
- [Chudzik et al. (2024)](/sources/chudzik-2024.md) — §5.3, Ex. 5.2, 6.4, 7.2, Figs. 8–10, 17, 20–21.
