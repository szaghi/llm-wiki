---
type: Benchmark
title: "Gresho vortex"
description: "Two-dimensional vortex in exact equilibrium between a piecewise-linear azimuthal velocity and its pressure field, advected through or held in a periodic square; tests whether a compressible scheme's dissipation stays bounded as the Mach number goes to zero (semi-implicit and IMEX all-Mach schemes, low-Mach HLLC corrections, learned WENO weights) and whether Active Flux keeps the stationary state."
status: established
aliases: [Gresho–Chan vortex, triangular vortex, low-Mach Gresho vortex]
tags: [benchmark, low-dissipation, asymptotic-preserving, machine-learning]
timestamp: 2026-10-24T06:00:00Z
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
origin in Chudzik et al. and Wilfong et al.) and
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

- [Allegrini & Vignal (2025)](/sources/allegrini-2025.md) §4.5 (HAL
  manuscript) hold the vortex at rest in the unit square $[0,1]^2$
  (boundary conditions not stated):
  $v_\theta=5r$, $2-5r$ and $0$ on $r<0.2$, $0.2\le r<0.4$, $r\ge0.4$,
  $\rho=1$, pressure $p_0+12.5r^2$, $p_0+12.5r^2+4\big(1-5r-\ln0.2+\ln r\big)$
  and $p_0-2+4\ln2$, with $p_0=\rho/(\gamma M_p^2)$ for the Mach numbers
  $M_p=10^{-1},10^{-2},10^{-3}$; one turn, $t=0.4\pi$, on $40^2$ and
  $80^2$.
- [Barsukow et al. (2026)](/sources/barsukow-2026.md) §5.3 (arXiv v2)
  use the same profile at rest in the periodic $[0,1]^2$ with $\gamma=1.4$,
  $M=0.1$ and pressure $\tfrac1{\gamma M^2}-\tfrac12+\tfrac{(5r)^2}2$,
  $\tfrac1{\gamma M^2}-\tfrac12+4\ln(5r)+4-20r+\tfrac{(5r)^2}2$ and
  $\tfrac1{\gamma M^2}-\tfrac12+4\ln2-2$ on the three ranges, to $t=1$
  on $51^2$ cells.
- [Wilfong et al. (2026)](/sources/wilfong-2026.md) §4.2.4 write the
  vortex with its peak at $r=R$ and its edge at $r=2R$:
  $v_\theta=u_{\mathrm r}\{r/R;\ 2-r/R;\ 0\}$ on $[0,R)$, $[R,2R]$,
  $[2R,\infty)$ and
  $p=p_{\mathrm r}+\rho_{\mathrm r}u_{\mathrm r}^2\{\tfrac12(r/R)^2;\ \tfrac12(r/R)^2+4(1-r/R+\ln(r/R));\ -2+4\ln2\}$,
  with $u_{\mathrm r}=2\pi RM_{\mathrm r}$ and the reference time
  $t_{\mathrm r}=2\pi R/u_{\mathrm r}=1/M_{\mathrm r}$ ($u_{\mathrm r}$,
  $p_{\mathrm r}$, $\rho_{\mathrm r}$, $M_{\mathrm r}$ page-local
  reference scales), run to $t/t_{\mathrm r}=1$ at
  $M_{\mathrm r}=10^{-1},10^{-2},10^{-3},10^{-4}$. They define the Mach
  number as printed by
  $M_{\mathrm r}=u_{\mathrm r}/\sqrt{\gamma p_{\mathrm r}/\rho_{\mathrm r}+u_{\mathrm r}^2/2}$;
  domain and grid are not given.

All three are the profile above with $V=1$ (Allegrini & Vignal, Barsukow
et al.) or $V=u_{\mathrm r}$ and $R$ doubled (Wilfong et al.), $P=\rho V^2$ and
a background pressure set by the Mach number: the three printed
pressures are continuous at the peak and at the edge and satisfy
$\partial_rp=\rho v_\theta^2/r$ *(compiler check, not in the sources)*.
Allegrini & Vignal's $t=0.4\pi$ is one rotation period $\pi R/V$ of the
core.

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

**IMEX all-Mach finite volumes.** Allegrini & Vignal's second-order
"L2 AP" scheme (ARS(2,2,2) in time, MUSCL in space, the
Toro–Vázquez flux splitting with an implicit pressure and enthalpy
flux; see [semi-implicit all-Mach scheme](/methods/semi-implicit-all-mach-scheme.md)
and [flux vector splitting](/methods/flux-vector-splitting.md)) keeps the
local Mach distribution independent of $M_p$ from $10^{-1}$ to $10^{-3}$
on $80^2$ and shows no pressure oscillations even at $M_p=10^{-3}$. The
kinetic-energy loss over one turn is also independent of $M_p$ and comes
"mostly" from the space limiter: the ratio of final to initial kinetic
energy is 0.9825 without and 0.92 with the minmod limiter on $40^2$
(Figs. 13–14).

**Low-Mach corrections of HLLC.** Wilfong et al. use the vortex to test
two low-Mach corrections of the [HLLC](/methods/hll-riemann-solvers.md)
solver in [MFC](/software/mfc.md) 5.0: Thornber et al.'s modification of
the interface velocities by $z=\min\big(\max(\lvert v^-\rvert/c^-,\lvert v^+\rvert/c^+),1\big)$
(page-local; $v^\mp$, $c^\mp$ the left and right interface states, the paper's L and R), and Chen et al.'s anti-dissipation pressure correction,
which adds $(z-1)$ times a pressure-difference term to the star-state
fluxes. Standard HLLC loses accuracy as $M_{\mathrm r}$ falls, the
low-Mach defect of Godunov-type solvers that they cite from Guillard &
Viozat, while with both
corrections HLLC preserves the flow field "to visual accuracy for all tested Mach numbers"
down to $10^{-4}$ (Fig. 14, plots of $M/M_{\mathrm r}$).

**Arbitrary-order Active Flux.** Barsukow et al. run their generalized
[Active Flux](/methods/active-flux.md) method of orders 3 to 7 (SSP-RK3,
the maximal CFL numbers of their Table 3, except 0.085 instead of
0.088 at order 7) and plot the radial
profile of the cell-averaged momentum magnitude; higher orders stay
closer to the exact profile (Figs. 14–15). No error is measured.

The sources reach their low-Mach behaviour by different means: a
semi-implicit or IMEX treatment of the acoustic part (Boscarino et al.,
Allegrini & Vignal), a modified Riemann solver (Wilfong et al.), a
lower-dissipation explicit reconstruction (Bezgin et al.).

## Qualifications

- Boscarino et al. print the middle pressure branch as
  $2(r/R)^2-4\big(2r/R+\ln(r/R)\big)+6$. That branch is discontinuous at
  $r=R/2$ (it gives $2.5+\ln16$ against $2.5-\ln16$ from the inner
  branch) and does not satisfy the radial balance; the form above, with
  $+4\ln(r/R)$, is the one Bezgin et al. print and the one that
  integrates $v_\theta^2/r$ *(compiler check, not in the sources)*.
- No source reports an error norm; Boscarino et al. and Bezgin et al.
  judge by contours and, in Boscarino et al., by the kinetic-energy
  history, Chudzik et al. by the density range and contours, Allegrini &
  Vignal by the Mach distribution and a kinetic-energy ratio, Wilfong et
  al. and Barsukow et al. by plots.
- Barsukow et al. print the velocity as $\frac{5r}{r}(-y-0.5,\ x-0.5)^\top$
  (and likewise on $0.2\le r<0.4$); the azimuthal direction about
  $(0.5,0.5)$ is $(-(y-0.5),\ x-0.5)/r$, so the first component should
  read $0.5-y$ *(compiler check, not in the sources)*.
- Wilfong et al.'s Mach number includes $u_{\mathrm r}^2/2$ under the
  square root, so it is not the ratio of $u_{\mathrm r}$ to the sound
  speed; at $M_{\mathrm r}\le10^{-1}$ the difference is below 1 %
  *(compiler check, not in the sources)*.

# Citations

- [Boscarino et al. (2022)](/sources/boscarino-2022.md) — Ex. 5.5, Eqs. (5.9)–(5.11), Fig. 5.6 (arXiv v2).
- [Bezgin et al. (2022)](/sources/bezgin-2022.md) — §4.5, Eqs. (34)–(36), Fig. 13.
- [Chudzik et al. (2024)](/sources/chudzik-2024.md) — §5.3, Ex. 5.2, 6.4, 7.2, Figs. 8–10, 17, 20–21.
- [Allegrini & Vignal (2025)](/sources/allegrini-2025.md) — §4.5, Figs. 13–14 (HAL manuscript).
- [Barsukow et al. (2026)](/sources/barsukow-2026.md) — §5.3, Table 3, Figs. 14–15 (arXiv v2).
- [Wilfong et al. (2026)](/sources/wilfong-2026.md) — §4.2.4, Fig. 14.
