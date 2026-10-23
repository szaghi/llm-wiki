---
type: Benchmark
title: "Lid-driven cavity"
description: "Viscous flow in a square cavity driven by its sliding top wall, run by compressible schemes at low Mach number against steady centreline profiles, in a magnetized visco-resistive variant, and with a lid accelerated through Mach 2 and back, to test viscous accuracy and all-Mach robustness."
status: established
aliases: [lid-driven cavity flow, driven cavity, MHD lid-driven cavity, accelerating-lid cavity]
tags: [benchmark, mhd, asymptotic-preserving, finite-volume]
timestamp: 2026-10-23T11:06:00Z
---

# Lid-driven cavity

The lid-driven cavity is a closed square box of viscous fluid whose top wall slides
tangentially while the other three walls are fixed no-slip walls. The moving lid drags the
fluid into a primary recirculating vortex, with secondary corner vortices whose size grows
with the Reynolds number $\mathrm{Re}$ built on the lid speed and the side of the box; at
moderate $\mathrm{Re}$ the flow reaches a steady state, and the velocity profiles along the
vertical and horizontal centrelines are the quantities compared. The problem has no inflow,
outflow or shock, so it isolates the viscous discretization and the wall boundary
conditions. Compressible schemes run it at low Mach number, where it also tests whether the
scheme stays accurate when the acoustic speed is much larger than the flow speed. Here
$v_{\mathrm{lid}}$ is the lid velocity and $\mu$ the dynamic viscosity (page-local).

## Setups

| Source | Variant | Data as printed | Grid, run |
|---|---|---|---|
| [Zhao et al. (2023)](/sources/zhao-2023.md) §4.9 | hydrodynamic, steady | unit square; lid $U_0=1$, $T_0=1$, $M=0.15$, $\mathrm{Re}=1000$; isothermal no-slip walls | $33\times33\times2$ triangles, stretching 1.2, minimum $h\approx0.0052$ |
| [Dematté et al. (2024)](/sources/dematte-2024.md) §4.3.3 | visco-resistive MHD, steady | $[-0.5,0.5]^2$; $\rho=1$, $v=0$, $p=10^5$; lid $v_{\mathrm{lid}}=\tanh\big(\hat\beta(0.5-x)\big)+\tanh\big(\hat\beta(0.5+x)\big)-1$, $\hat\beta=40$; $B_0=(B_{x,0},0,0)$, $B_{x,0}=0.5$ and $1.0$ | $512^2$, CFL 0.4 on the velocity, steady by $t=20$ |
| Dematté et al. §4.4 (new) | visco-resistive MHD, unsteady all-Mach | $[-0.5,0.5]^2$; $\rho=2$, $v=0$, $p=10$; $B=(0,0,0.1/\sqrt{4\pi})$ for $r\le0.1$, $0$ outside; lid $v_{\mathrm{lid}}=4A(x_{\mathrm{norm}}-x_{\mathrm{norm}}^2)$, $A=u_{\max}e^{-(t-t_{\mathrm{peak}})^2/(2s_t^2)}$, $u_{\max}=6$, $t_{\mathrm{peak}}=10$, $s_t^2=5$; $\mu=0.02$, thermal conductivity $1.0$ | $512^2$, no-slip walls, MUSCL–Hancock; snapshots $t=3.2$, $7.2$, $10$, $20$ |

In Dematté et al.'s accelerating-lid case $r$ is the distance from the cavity centre,
$x_{\mathrm{norm}}$ is their normalized lid coordinate and $s_t$ (page-local) is the width of
the Gaussian pulse of the lid speed. Their default is an ideal gas with $\gamma=5/3$ (§4).

**Boundary conditions of the MHD variant.** Dematté et al. impose Neumann conditions on
$\rho$ and $p$ and perfectly conducting walls, $B\cdot n=B_0\cdot n$ and $\mathcal E\times n=0$ for the
electric field $\mathcal E$ (page-local, as on the other pages citing Dematté et al.), which they realize as Neumann conditions on the tangential
field; in the staggered constrained-transport variant the corner electric field on the
boundary is set to zero (§4.3.3).

**Mach numbers** *(compiler check, not in the sources)*. In the steady MHD cavity the sound
speed is $\sqrt{\gamma p/\rho}=\sqrt{(5/3)\times10^5}\approx408$, so the unit lid speed gives
$M\approx2.4\times10^{-3}$. In the accelerating-lid case the sound speed is
$\sqrt{(5/3)\times10/2}\approx2.89$ and the peak lid speed $u_{\max}=6$ gives $M\approx2.1$,
consistent with the authors' "$M\simeq2$" at $t=10$.

## Findings

**Gas-kinetic compact scheme.** Zhao et al. use the cavity at $\mathrm{Re}=1000$ to show the
viscous accuracy of their compact [gas-kinetic scheme](/methods/gas-kinetic-scheme.md) on a
coarse stretched triangular mesh in a nearly incompressible regime: the centreline $U$ and
$V$ profiles are compared with "reference solutions" whose source is not named in the text
(§4.9, Figs. 15–16, arXiv v1).

**Semi-implicit MHD at very low Mach number.** Dematté et al.'s
[semi-implicit all-Mach scheme](/methods/semi-implicit-all-mach-scheme.md) treats the pressure
and magnetic terms implicitly, so its time step is set by the flow speed alone. On the
magnetized cavity with CFL 0.4 on the velocity, the steady solutions for $B_{x,0}=0.5$ and
$1.0$ agree "very well" with the hybrid finite-volume/finite-element reference of Fambri et
al. that they cite (§4.3.3, Figs. 17–18). The magnetic field is advanced by
[constrained transport](/methods/constrained-transport.md), whose wall treatment is the one
described above; the paper's divergence measurements
([divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)) are made on
other tests.

**Through Mach 2 and back.** The accelerating-lid cavity is Dematté et al.'s own test: the
lid speed rises as a Gaussian pulse, so that the flow passes from very low Mach number
($t=3.2$) through $M\simeq2$ ($t=10$) back to low Mach number and a nearly steady state
($t=20$), with a magnetized disc at the centre. There is no reference solution; the authors
judge the results "satisfactory based on physical intuition" (§4.4, Figs. 19–20).

**Hydrodynamic cavity at higher Reynolds number.** [Bezgin et al. (2023)](/sources/bezgin-2023.md)
run the cavity at $\mathrm{Re}=5000$ on $500^2$ cells with the HLLC flux in
[JAX-Fluids](/software/jax-fluids.md); the centreline velocities agree with those of Ghia et
al. (§5.1.3, Fig. 11).

## Qualifications

- Dematté et al. do not print the viscosity and resistivity (or the Reynolds and magnetic
  Reynolds numbers) of the steady MHD cavity in §4.3.3.
- In §4.4 Dematté et al. call the coefficient $1.0$ a "heat-capacity", whereas their §3.4
  defines it as the thermal conductivity; the table above follows §3.4.
- Zhao et al.'s lid-driven cavity is in the arXiv v1 read; the published version may differ.
- None of the sources gives an error norm: the comparisons are of profiles (Zhao et al.,
  Dematté et al. §4.3.3) or qualitative (§4.4).

# Citations

- [Zhao et al. (2023)](/sources/zhao-2023.md) — §4.9, Figs. 15–16 (arXiv v1).
- [Dematté et al. (2024)](/sources/dematte-2024.md) — §3.4, §4 (defaults), §4.3.3, §4.4, Figs. 17–20.
- [Bezgin et al. (2023)](/sources/bezgin-2023.md) — §5.1.3, Fig. 11.
