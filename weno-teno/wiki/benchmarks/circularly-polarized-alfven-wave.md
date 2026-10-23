---
type: Benchmark
title: "Circularly polarized Alfvén wave"
description: "Smooth exact travelling-wave solution of ideal (and relativistic) MHD in which the transverse velocity and magnetic field rotate along the propagation direction at constant density and pressure; advected over one period in 1D or along a rotated direction in 2D, it serves as a convergence-order test of MHD schemes, from fifth-order WENO to one-step second-order GRP finite volumes."
status: established
aliases: [Alfvén wave test, circularly polarised Alfvén wave, rotated Alfvén wave, large-amplitude Alfvén wave]
tags: [benchmark, mhd, relativistic]
timestamp: 2026-10-23T20:00:00Z
---

# Circularly polarized Alfvén wave

In ideal MHD a circularly polarized Alfvén wave of any amplitude is an
exact smooth solution: density and pressure are uniform, the normal
magnetic field $B_1$ is constant, and the transverse velocity and field
rotate along the propagation direction,
$v_\perp\propto-B_\perp$, so the wave translates rigidly at the Alfvén
speed. With periodic boundaries it returns to its initial state after
one period, which makes it an accuracy test of MHD schemes: the error
against the initial (or translated) data measures the order in space
and time. In 2D the wave is rotated to an oblique direction, which
also tests the treatment of $\nabla\cdot B$; in special relativity a
large-amplitude version of the same wave is an exact solution of
relativistic MHD.

## Data

**Non-relativistic, [Chen, Wu & Xiong (2023)](/sources/chen-2023-b.md).**
Ex. 5.1 on $[0,1]$, periodic:
$(\rho,v_1,v_2,v_3,B_1,B_2,B_3,p)=(1,0,0.1\sin2\pi x,0.1\cos2\pi x,1,0.1\sin2\pi x,0.1\cos2\pi x,0.1)$,
exact solution $u(x,t)=u(x+t,0)$, $\gamma=5/3$, $T=1$, sonic Mach
parameter $\varepsilon=1$. The time step
$\Delta t=\nu\,\Delta x^{5/3}/\max(\lvert v_1\rvert+\hat c_f)$ ($\hat c_f$
their capped fast speed, $\nu=0.25$) makes the error of their
third-order time integrator of order $\Delta x^5$ *(compiler check, not in the sources)*. Ex. 5.4 rotates the same wave to the direction
$(-\cos\theta,-\sin\theta)$, $\theta=\pi/4$, on
$[0,1/\cos\theta]\times[0,1/\sin\theta]$ with $\Delta t$ scaled by
$\Delta x^{5/3}$ and $\Delta y^{5/3}$.

**Non-relativistic, rotated, [Liu, Feng & Wang (2023a)](/sources/liu-2023.md).**
§4.2 on $[0,1/\cos\theta]\times[0,1/\sin\theta]$, $\theta=\pi/4$,
periodic: with the page-local phase $\ell=x\cos\theta+y\sin\theta$,
$\rho=1$, parallel velocity $0$, perpendicular velocity
$0.1\sin(2\pi\ell)$, $v_3=0.1\cos(2\pi\ell)$, parallel field $1$,
perpendicular field equal to the perpendicular velocity, $B_3=v_3$,
$p=0.1$, $\gamma=5/3$, Alfvén speed 1, $t=2$, CFL 0.2, meshes $16^2$ to
$256^2$. The reference is "the exact solution at $t=2$, which is the
initial value", and the error is that of the reconstructed polynomial
(their Eq. (84)).

**Relativistic, [López-Miralles, Martí & Perucho (2023)](/sources/lopezmiralles-2023.md).**
§4.1.1, Eqs. 44–47: $v_2=-A\cos\!\big(\tfrac{2\pi}{\lambda}(x-v_at)\big)$,
$v_3=-A\sin(\cdot)$, $B_1=B_0$, $B_2=-B_0v_2/v_a$, $B_3=-B_0v_3/v_a$,
with
$v_a=\pm\sqrt{B_0^2(1-A^2)/\big(\rho_0h_0+B_0^2(1-A^2)\big)}$, $\rho_0=1$,
specific enthalpy $h_0=5$ ($\gamma=4/3$), $B_0=1$,
$A=\sqrt{2/(7+3\sqrt5)}\approx0.38197$ (page-local amplitude $A$, Alfvén
speed $v_a$ and wavelength $\lambda$); domain $[0,2\pi]$, $N=8$–$512$,
one period $T=\lambda/v_a$; $L_1$ error of $v_3$ against the initial
data.

## Runs and findings

**Fifth order with constrained transport.** Chen, Wu & Xiong's
semi-implicit [IMEX](/methods/imex-runge-kutta.md) fifth-order
finite-difference WENO scheme with constrained transport gives $L^1$
errors of $\rho v_2$ from $6.24\times10^{-4}$ ($N=10$) to
$6.27\times10^{-10}$ ($N=160$), orders 4.94, 4.99, 5.00, 5.00
(Table 5.1). In 2D the momentum converges at fifth order ($\rho v_1$:
$1.54\times10^{-3}$ on $8^2$ to $1.84\times10^{-9}$ on $128^2$, orders
4.75–5.00), but $B_1$ only at about fourth order (3.87, 4.33, 4.23,
4.13), because $B=\nabla\times\mathsf A$ is formed from the vector potential $\mathsf A$ (page-local) by
fourth-order central differences (Table 5.3; see
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)).

**Second order of a one-step GRP scheme.** Liu, Feng & Wang compare
three second-order finite-volume schemes with the same locally
divergence-free [WLS-ENO](/methods/wls-eno.md) reconstruction: their
one-step HLL [generalized Riemann problem](/methods/generalized-riemann-problem.md)
flux (HLL-GRP), a forward-Euler HLL scheme (FE) and a two-stage SSP-RK2
HLL scheme (RK2) (Table 1, $L^1$ errors of $v_1$):

- HLL-GRP: $1.7210\times10^{-2}$ on $16^2$ to $5.5446\times10^{-5}$ on
  $256^2$, orders 2.1125, 1.9463, 2.3627, 1.8565;
- RK2: orders 2.0953, 1.9895, 2.4408, 2.3915, error
  $3.6834\times10^{-5}$ on $256^2$;
- FE: orders falling to 1.0034 on $256^2$.

The authors state that HLL-GRP "achieves the expected convergence
order" with errors close to RK2. At $256^2$ on 64 cores (Tianhe-1A, two
six-core Xeon X5670 per node) the wall times are 714.77 s (FE),
4202.02 s (HLL-GRP) and 1681.45 s (RK2), which the authors ascribe to the
truncated-SVD least-squares solves of the GRP star-state gradient: the
one-step scheme costs 2.50 times the two-stage one
*(compiler check, not in the sources)*.

**Order of reconstruction and time stepping in relativistic MHD.**
López-Miralles et al. run their RMHD code with HLL, HLLC, HLLD and a
Jacobian-free [polynomial viscosity matrix](/methods/polynomial-viscosity-matrix-solver.md)
solver (PVM-int-8) and with several reconstructions (Tables 1–4,
Fig. 1):

- first order with Godunov's method (HLL, order 0.916 at $N=256\to512$);
  second order with piecewise-linear limiters (MC 2.024, van Leer 2.094
  with HLL at the finest pair), MinMod giving the largest errors;
- third order with [MP](/methods/monotonicity-preserving-limiter.md)3
  and three-stage Runge–Kutta (HLLD 2.998, PVM-int-8 2.999);
- MP5 with the three-stage Runge–Kutta still third order (HLLD 3.005)
  but with errors almost two orders lower ($4.284\times10^{-9}$ against
  $3.224\times10^{-7}$ at $N=512$);
- MP5 with a five-step fourth-order SSP Runge–Kutta: orders 4.83–5.05,
  error $9.006\times10^{-12}$ at $N=512$ (HLLD).

HLLC reproduces the earlier results of Martí (2015), HLLD behaves like
HLLC on this smooth solution, and the PVM-int-8 errors are very close to
HLLC's.

**Other sources.** [Liu et al. (2021)](/sources/liu-2021.md) use a
smooth Alfvén wave as the order test of their
[WLS-ENO](/methods/wls-eno.md) MHD scheme (orders about 2 and 3).

## Qualifications

- López-Miralles et al. observe fifth order with a fourth-order time
  integrator at CFL 0.3 and do not comment on it. Their text says the runs use $N=16$–$512$,
  their tables start at $N=8$.
- Chen, Wu & Xiong scale $\Delta t$ with $\Delta x^{5/3}$ to observe the
  spatial order; their third-order IMEX scheme is not tested at
  $\Delta t\propto\Delta x$ on this case.
- Liu, Feng & Wang's HLL-GRP orders oscillate between 1.86 and 2.36,
  and at $256^2$ the HLL-GRP error is 1.5 times that of RK2
  *(compiler check, not in the sources)*; the paper does not discuss
  the drop to 1.86 at the finest pair.
- Chen, Wu & Xiong and López-Miralles et al. are read as arXiv v1
  preprints; Liu, Feng & Wang as the version of record.

# Citations

- [Chen, Wu & Xiong (2023)](/sources/chen-2023-b.md) — Exs. 5.1, 5.4, Tables 5.1, 5.3 (arXiv v1).
- [López-Miralles, Martí & Perucho (2023)](/sources/lopezmiralles-2023.md) — §4.1.1, Eqs. 44–47, Tables 1–4, Fig. 1 (arXiv v1).
- [Liu et al. (2021)](/sources/liu-2021.md) — §4.1, Table 1.
- [Liu, Feng & Wang (2023a)](/sources/liu-2023.md) — §4.2, Table 1.
