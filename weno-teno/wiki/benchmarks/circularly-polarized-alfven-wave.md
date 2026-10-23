---
type: Benchmark
title: "Circularly polarized Alfvén wave"
description: "Smooth exact travelling-wave solution of ideal and relativistic MHD whose transverse velocity and magnetic field rotate along the propagation direction at constant density and pressure; advected one period in 1D or along a rotated direction in 2D and 3D, it tests the convergence order of MHD schemes, from fifth-order WENO to second-order GRP finite volumes and bound-preserving central DG."
status: established
aliases: [Alfvén wave test, circularly polarised Alfvén wave, rotated Alfvén wave, large-amplitude Alfvén wave]
tags: [benchmark, mhd, relativistic]
timestamp: 2026-10-23T11:06:00Z
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

**Non-relativistic and relativistic, 2D and 3D, [Berta et al. (2024)](/sources/berta-2024.md).**
§5.3, Eqs. (47)–(49), after Mignone (MHD) and Del Zanna (RMHD) as they
cite them. With the page-local phase $\varphi_{\mathrm A}=k_wx-\omega t$
(wavenumber $k_w$, angular frequency $\omega$) and amplitude
$\eta_{\mathrm A}$ (page-local), the 1D MHD profile is
$v=(0,\ \eta_{\mathrm A}\sin\varphi_{\mathrm A},\ \eta_{\mathrm A}\cos\varphi_{\mathrm A})$,
$B=(c_a\sqrt\rho,\ \sqrt\rho\,\eta_{\mathrm A}\sin\varphi_{\mathrm A},\ \sqrt\rho\,\eta_{\mathrm A}\cos\varphi_{\mathrm A})$,
with $c_a=\omega/k_w=1$, $\eta_{\mathrm A}=0.1$, $\rho=1$, $p=2$,
$\gamma=5/3$. The relativistic profile is
$v=(0,\ -c_A\eta_{\mathrm A}\cos\varphi_{\mathrm A},\ -c_A\eta_{\mathrm A}\sin\varphi_{\mathrm A})$,
$B=(B_0,\ B_0\eta_{\mathrm A}\cos\varphi_{\mathrm A},\ B_0\eta_{\mathrm A}\sin\varphi_{\mathrm A})$,
with $B_0=1$, $\eta_{\mathrm A}=1$, $\gamma=4/3$ and the relativistic Alfvén
speed $c_A$ of their Eq. (49). The wave is rotated by $45^\circ$ about
the $y$ axis in 2D and by a further $45^\circ$ about the $z$ axis in 3D,
on the unit square or cube, periodic; one period; $N_x=8$ to $512$;
CFL 0.4 (2D) and 0.3 (3D); $L^1$ error of $B_2$ between final and
initial profiles.

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

**Relativistic at $0.99c$, [Ding & Wu (2024)](/sources/ding-2024-b.md).**
Example 5.1, with the equation of state they label TM,
$h=\tfrac{5p}{2\rho}+\sqrt{1+\tfrac94(p/\rho)^2}$. In 1D on $[0,1]$,
periodic: $\rho=1$, $p=0.01$, $v_1=0$,
$v_2=0.99\sin\big(2\pi(x+t/\kappa_{\mathrm A})\big)$,
$v_3=0.99\cos(\cdot)$, $B_1=1$, $B_2=\kappa_{\mathrm A}v_2$,
$B_3=\kappa_{\mathrm A}v_3$, with $\kappa_{\mathrm A}=\sqrt{1+\rho hW^2}$
(page-local), so the wave moves at speed $1/\kappa_{\mathrm A}$ and
$W\approx7.09$ *(compiler check, not in the sources)*; $t=1$, error of $v_2$. In 2D the same wave propagates at
$45^\circ$ on the periodic $[0,\sqrt2]^2$ with phase
$x\cos\alpha+y\sin\alpha$, $\alpha=\pi/4$, and constant field
$(\cos\alpha,\sin\alpha)$ added to $\kappa_{\mathrm A}(v_1,v_2)$; $t=1$, error
of $B_2$. They take the 1D setup from Wu & Tang and describe the 2D one
as that of Wu & Shu with a lower pressure.

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

**Fourth order, cost and dissipation of pointwise finite volumes.**
Berta et al.'s fourth-order constrained-transport finite-volume scheme
(pointwise [MP5](/methods/monotonicity-preserving-limiter.md) or
pointwise [WENO-Z](/methods/weno-z.md) interface values, Laplacian
point/average conversions, SSPRK(5,4)) reaches $O_{L_1}=4.00$ at
$N_x=512$ in every configuration, and its MP5 and WENO-Z errors are
almost identical (Table 2; WENO-Z shown):

| $\varepsilon_1(B_2)$ | $N_x=8$ | 64 | 512 |
|---|---|---|---|
| MHD, 2D | 3.02E-03 | 5.08E-07 | 1.21E-10 |
| MHD, 3D | 3.83E-03 | 7.57E-07 | 1.82E-10 |
| RMHD, 2D | 2.60E-02 | 4.33E-06 | 1.04E-09 |
| RMHD, 3D | 3.48E-02 | 6.45E-06 | 1.58E-09 |

In 3D MHD the scheme has smaller errors than Mignone's fifth-order
finite-difference scheme (as they quote its Table 1) below $256^3$; at
$256^3$ the errors are $\varepsilon_1(B_2)\approx3.74\times10^{-9}$
(finite difference) and $2.91\times10^{-9}$ (theirs). From the 3D runs
they fit a cost model: with cost $T=\tau N^{d+1}$ and error
$\varepsilon=CN^{-p_{\mathrm o}}$ ($\tau$, $C$, $p_{\mathrm o}$ page-local: cost per cell
update, error constant, order), equal accuracy at second and fourth order needs
$N_4\sim(C_4/C_2)^{1/4}\sqrt{N_2}$ and
$T_4/T_2=(C_4/C_2)^{(d+1)/4}(\tau_4/\tau_2)/\sqrt{N_2^{d+1}}$; measured
$\tau_4/\tau_2\approx4.3$ and $3.7$, $C_4/C_2\approx5.0$ and $8.7$ (MHD,
RMHD) give $T_4/T_2\sim K/N_2^2$ with $K\approx21$ and $32$, so a smooth
MHD run on $512^3$ at second order is matched at fourth order with
$N_4\approx34$ and a time reduction of about $1.2\times10^4$ (Eqs.
(50)–(52)). The numerical dissipation, measured from the decay rate of
$\big(\iiint B_3^2\big)^{1/2}$, is more than an order of
magnitude below that of the second-order scheme already at $N\sim8$ and
scales as $N^{-5}$ against $N^{-3}$ (Fig. 5); see
[numerical dissipation](/definitions/numerical-dissipation.md).

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

**Third order of bound-preserving central DG.** Ding & Wu's $\mathbb P^2$
central DG scheme for relativistic MHD with SSP-RK3 and CFL 0.25, with
the bound-preserving limiter active (and, in 2D, locally divergence-free
spaces and the symmetrization source), converges at third order
(Tables 1–2):

| | coarsest | finest | $l^1$ orders |
|---|---|---|---|
| 1D, $v_2$ | 6.53e-05 ($N=20$) | 1.96e-09 ($N=640$) | 3.02, 3.00, 3.00, 3.00, 3.00 |
| 2D, $B_2$ | 1.92e-03 ($20^2$) | 3.07e-08 ($640^2$) | 3.93, 3.01, 3.00, 3.00, 3.00 |

The authors conclude that neither the limiter nor the discretized
source terms degrade the accuracy (§5); see
[discontinuous Galerkin](/methods/discontinuous-galerkin.md) and
[bound preservation](/properties/bound-preservation.md).

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
- Berta et al.'s fourth-order scheme uses a fifth-order interface
  interpolation; at $N_x\le64$ their orders lie between 4.01 and 4.34,
  above the design order.
- Ding & Wu's 2D $l^1$ order on the coarsest pair, 3.93, and $l^2$ order
  3.41 lie above three before settling at 3.00 (Table 2).
- Ding & Wu run every test with $\Delta t=0.25\Delta x$ in 1D and
  $\Delta t=0.25/(1/\Delta x+1/\Delta y)$ in 2D, while their
  bound-preserving conditions read $\tau_{\max}\le\tfrac{\varpi}{2}\Delta x$,
  $\varpi=\tfrac16$ for $N=2$ (1D), and
  $\tau_{\max}(\alpha_1/\Delta x+\alpha_2/\Delta y)\le\tfrac{\varpi}{2}=\tfrac18$
  with the Cui–Ding–Wu weight $\varpi=\tfrac14$ (2D), with $\Delta t=\theta_{\mathrm C}\tau_{\max}$,
  $\theta_{\mathrm C}\in(0,1]$ and $\alpha_\ell\ge1$ (page-local, as on
  [discontinuous Galerkin](/methods/discontinuous-galerkin.md)); $\tau_{\max}$ and
  $\theta_{\mathrm C}$ of the runs are not printed. The authors state that the
  theoretical bound is sufficient but not always necessary (§5).
- Chen, Wu & Xiong and López-Miralles et al. are read as arXiv v1
  preprints, Berta et al. as arXiv v4; Liu, Feng & Wang and Ding & Wu
  as versions of record.

# Citations

- [Berta et al. (2024)](/sources/berta-2024.md) — §5.3, Eqs. (47)–(52), Table 2, Fig. 5 (arXiv v4).
- [Chen, Wu & Xiong (2023)](/sources/chen-2023-b.md) — Exs. 5.1, 5.4, Tables 5.1, 5.3 (arXiv v1).
- [López-Miralles, Martí & Perucho (2023)](/sources/lopezmiralles-2023.md) — §4.1.1, Eqs. 44–47, Tables 1–4, Fig. 1 (arXiv v1).
- [Liu et al. (2021)](/sources/liu-2021.md) — §4.1, Table 1.
- [Liu, Feng & Wang (2023a)](/sources/liu-2023.md) — §4.2, Table 1.
- [Ding & Wu (2024)](/sources/ding-2024-b.md) — §5, Example 5.1, Eq. (88), Tables 1–2.
