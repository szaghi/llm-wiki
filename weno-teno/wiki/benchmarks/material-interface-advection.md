---
type: Benchmark
title: "Material-interface advection tests"
description: "Uniform-velocity, uniform-pressure advection of material interfaces between gases or between gas and liquid, in 1D and 2D with up to five materials, and of a single-gas contact over many crossings, with pure translation as exact solution; it checks that multi-component and multi-phase schemes keep pressure and velocity in equilibrium, conserve mass and keep interfaces thin; a diffusing variant tests convergence."
status: established
aliases: [interface advection, advection of a material interface, interface translation test, water disk advection, smooth interface advection]
tags: [benchmark, multiphase, interface-capturing, finite-volume]
timestamp: 2026-10-23T15:17:00Z
---

# Material-interface advection tests

A material interface between two fluids of different density and
equation of state is carried by a uniform velocity at uniform pressure,
in most of the sources on a periodic domain. The exact solution is the initial data
translated, with pressure and velocity unchanged everywhere. The test
therefore isolates the one defect it is designed to expose: a
conservative scheme whose ratio of specific heats, or whose
stiffened-gas constant, jumps across the interface generates spurious
pressure and velocity oscillations there, even when the interface is
smooth. The sources use it to verify
[pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)
to round-off, conservation of mass and energy, and, for
interface-capturing schemes, that the interface keeps its thickness and
shape after one or more periods.

## Variants

**Smooth two-species interfaces, central fluxes.**
[Fujiwara, Tamaki & Kawai (2023)](/sources/fujiwara-2023.md) §4 run
three tests of the
[multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)
with ideal gases, RK4, $\Delta t=10^{-4}$ (printed "CFL number of 0.05"),
on 501 points per direction, $u_0=1$, $p_0=0.9$ (chosen "just for the
visibility of the figures"):

- §4.1, 1D, periodic $[0,1]$: two species, $\gamma=(1.4,1.66)$, molar
  masses $(28,4)$, partial densities
  $\rho Y_1=\tfrac{w_1}{2}\big(1-\tanh(k(r-r_c))\big)$,
  $\rho Y_2=\tfrac{w_2}{2}\big(1+\tanh(k(r-r_c))\big)$ with
  $r=\lvert x-0.5\rvert$, $r_c=0.25$, $(w_1,w_2)=(0.6,0.2)$, $k=20$
  (page-local $w$, $k$, $r_c$, and $Y_k$ the mass fraction of the
  registry); output at $t=1$, $6$, $20$;
- §4.2, 2D, periodic $[0,1]^2$: three species, $\gamma=(1.4,1.66,1.29)$,
  molar masses $(28,4,44)$, circular tanh interfaces about $(0.5,0.5)$
  of radii $(0.3,0.3,0.2)$, amplitudes $(0.4,0.2,0.1)$, $k=15$,
  $u_0=v_0=1$, to $t=5$, five passes;
- §4.3, 2D: the two species of §4.1 with a tangential velocity jump
  $v_0=w_v\tanh(k(r-r_c))$, $w_v=0.5$, to $t=5$.

**Gas–gas interfaces with sharp profiles, discrete-equations method.**
[Paula, Adami & Adams (2023)](/sources/paula-2023.md) §7.1 advect, at
$u=1$, $p=1$, ideal gases with interfaces defined by level-set
functions: in 1D on periodic $[0,1]$ two phases
$\rho_1=1$, $\gamma_1=1.2$ and $\rho_2=2$, $\gamma_2=1.4$, interfaces at
0.25 and 0.75, 160 cells, $t=1$, CFL 0.5; in 2D on the periodic unit
square with $v=(1,0.5)$, a circle of radius 0.25 at the centre filled
with phase 2, or with phases 2–5 split by quadrants, $\gamma_l=1+0.2l$,
$\rho_l=l$ (page-local phase index $l$), $80\times80$ cells, $t=2$ (two
passes in $x$, one in $y$).

**Smooth profiles with and without an interface.** Paula et al. §7.3
advect, on the periodic unit interval with $u=p=1$, $\gamma=1.4$, CFL
0.05 and 128 to 2048 cells to $t=1$, a smooth volume-fraction bump
$\phi_1=0.1+0.8e^{-200(x-0.5)^2}$ and a smooth density bump
$1+5e^{-200(x-0.5)^2}$ in both phases, without and with an interface at
$x=0.5$, as a convergence test.

**Deformation in a vortex.** Paula et al. §7.2 run a Rider–Kothe-type
vortex: a four-material circle of radius 0.15 at $(0.5,0.75)$ of the
unit square in the velocity field
$\cos(\pi t/T)\,\big(-\sin^2(\pi x)\sin(2\pi y),\ \sin^2(\pi y)\sin(2\pi x)\big)$,
$T=4$, $128\times128$ cells, all materials with $p=1$, $\rho=1$,
$\gamma=1.4$, so that the flow reverses and the exact solution at
$t=T$ is the initial data.

**Gas–liquid disk with a density ratio of about 1000.**
[Huang & Johnsen (2023)](/sources/huang-2023.md) §4.3 advect a disk of
radius 0.2 at the centre of the periodic $[-0.5,0.5]^2$ at $(u,v)=(1,1)$,
at an angle of $45^\circ$ to the grid, for one period, $t=1$:
$(\rho_1,\rho_2,u,v,p)=(1.204\times10^{-3},1,1,1,4.819\times10^{-5})$,
air ($\gamma_1=1.4$) and water as a
[stiffened gas](/definitions/stiffened-gas-equation-of-state.md)
($\gamma_2=6.12$, $p_{\infty,2}=3.43\times10^8$ Pa), $100\times100$
cells, CFL 0.2, with their [phase-field](/methods/phase-field-method.md)
regularization at interface-thickness parameter $\eta/\Delta x=1$ (their
$\eta$, page-local).

**Water block and water droplet in air, five-equation model.**
[Zhang et al. (2024a)](/sources/zhang-2024.md) §4.1 advect, at
$v=100$ m s$^{-1}$ and $p=101325$ Pa, a water block on
$0.25\le x<0.75$ of the periodic $[0,1]$ m, with $\rho_1\phi_1=1000$ in
water and $\rho_2\phi_2=1.2$ kg m$^{-3}$ in air ($N_x=128$, $t=0.1$ s, ten
periods), and a water droplet of diameter 0.5 m in the periodic
$[0,1]^2$ m at $(v_1,v_2)=(100,0)$ m s$^{-1}$ on $128^2$ cells for ten
periods. "Pure" states carry volume fraction $1-10^{-8}$ or $10^{-8}$ and
partial densities $10^{-8}$; stiffened-gas water and ideal-gas air of
their Table 1; CFL 0.5 with SSP-RK3 and THINC steepness 1.8. They
compare fifth-order WENO5IS, MUSCL-THINC and their hybrid WENO5IS-THINC,
in which THINC reconstructs only $\phi_1$ and the partial densities in
interface cells.

**A square column of heavy gas, four-equation model.**
[Jiao et al. (2024)](/sources/jiao-2024.md) §4.1 advect a square column
of one ideal gas in another at $u=5$ m/s and $p_0=10^7$ Pa, 300 K, on a
periodic 0.2 m domain with 100 cells, CFL 1.4, for four periods to
$t=0.16$ s: component 1 with $\gamma=5$, $\rho=4.444$ kg m$^{-3}$,
component 2 with $\gamma=1.6$, $\rho=117.647$ kg m$^{-3}$ (Table 4.1),
both isothermal, in a mass-fraction four-equation model. They compare
second-order MUSCL reconstructions of the mass fraction with the six
limiters of their Table 4.2 (Van Albada, Van Leer, MinMod,
Chakravarthy, MC, Koren) against THINC, each followed by their
"thermodynamic-dependent update" of the interface density from the
equation of state.

**Smooth interface in the five-equation (Kapila) model, Abgrall's
test.** [Yan, Abgrall & Wu (2024)](/sources/yan-2024.md) Ex. 4.2 advect,
on periodic $[-0.5,0.5]$ with 200 cells to $t=1$ (one period; reference
on 1000 cells), two fluids with $\gamma_1=5/3$ and $\gamma_2=1.4$ at
$v=1$, $p=1/1.4$: for $\lvert x\rvert<0.25$ the phase densities
$(\rho_1,\rho_2)=(2+0.4\sin(\pi(x+0.5)),\ 1)$ with volume fraction
$\phi_1=1-10^{-10}$, and elsewhere $(1,\ 1-0.4\sin(\pi(x+0.5)))$ with
$\phi_1=10^{-10}$, so that each phase density also varies smoothly in
space. The test checks what they call the Abgrall condition: uniform
velocity and pressure stay uniform.

**Diffusing multicomponent interface.**
[Ching et al. (2025)](/sources/ching-2025.md) §5.1 advect a "thermal
bubble" of hydrogen in oxygen at $v_1=1$ m/s and $p=1$ bar on the
periodic $[-25,25]$ m, $Y_{\mathrm{H_2}}=\tfrac12[1-\tanh(\lvert x\rvert-10)]$,
$Y_{\mathrm{O_2}}=1-Y_{\mathrm{H_2}}$, temperature $T_{\mathrm{K}}=1200-900\tanh(\lvert x\rvert-10)$ K (page-local; $T$ is the period above),
with the multicomponent Navier–Stokes equations (mixture-averaged
species diffusion, thermally perfect gases), no artificial viscosity,
CFL 0.1, on meshes $h=2$ m to $h/8$ with DG degrees 1–3; the "exact"
solution is a degree-3 run on $h/256$, and the $L^2$ error of the
normalized state is taken at $t=5$ s. With diffusion the solution is no
longer a translation, so the test measures convergence, not
equilibrium preservation.

**Single-gas contact over a hundred crossings.**
[Cernetic et al. (2023)](/sources/cernetic-2023.md) §5.4 (arXiv v2) run
the supersonic top-hat of Schaal et al.: in 2D, density 4 inside a
central square of side 0.5 of the unit square and 1 outside, $p=2.5$,
$\gamma=1.4$, $(v_1,v_2)=(100,50)$; the results shown are for the 1D
version with 64 cells, degrees 0 to 9, to $t=1$, i.e. 100 crossings,
and with 10 cells at degree 9 for one crossing. It is a contact in one
gas, so it tests the sub-cell resolution and long-time diffusion of a
discontinuity rather than pressure equilibrium between materials.

## Findings across sources

**Pressure and velocity to round-off.** The sources below report
equilibrium to machine precision for their own schemes (Zhang et al.
(2024a) call their errors "negligible" without a value):

| Source | Scheme | Test | Velocity error | Pressure error |
|---|---|---|---|---|
| Fujiwara et al. | FC/PE (S), second-order central split form | 1D, $t=1$ | $\simeq10^{-13}$ | $\simeq10^{-13}$ |
| Fujiwara et al. | FC/PE (S) | 2D, three species, $t=5$ | $\simeq10^{-12}$ (relative) | $\simeq10^{-12}$ (relative) |
| Paula et al. | RDEMIC with THINC, WENO3, HLLC | 1D, two phases | $9.4\times10^{-15}$ | $4.7\times10^{-15}$ |
| Paula et al. | RDEMIC | 2D, two materials | $1.1\times10^{-14}$ | $2.3\times10^{-15}$ |
| Paula et al. | RDEMIC | 2D, five materials | $1.2\times10^{-14}$ | $8.4\times10^{-15}$ |
| Huang & Johnsen | five-equation-type model with phase field, MUSCL–HLLC | 2D water disk | round-off | round-off |
| Yan, Abgrall & Wu | bound-preserving [OEDG](/methods/oedg.md), $\mathbb P^2$ and $\mathbb P^3$ | 1D Kapila model, $t=1$ | within $\pm1.5\times10^{-12}$ | within $\pm1.5\times10^{-12}$ |

(Fujiwara et al. Figs. 2–3, 7; Paula et al. Table 1; Huang & Johnsen
Fig. 7; Yan et al. Figs. 3–4.) The mechanisms differ. Fujiwara et al. obtain it from a
discrete compatibility condition on the half-point values of a fully
conservative central flux, with no extra transport equation; Paula et
al. from the [discrete-equations method](/methods/discrete-equations-method.md),
whose non-conservative interface terms come from Lagrangian fluxes
across contact waves; Huang & Johnsen from consistency conditions
between the reconstruction and phase-field fluxes of mass and volume
fraction. Yan et al. prove it for their scheme: the semi-discrete DG
scheme with forward Euler keeps uniform velocity and pressure uniform
(Lemma 2.5), and so does the fully discrete OEDG scheme with SSP
Runge–Kutta (Thm 2.6), because the oscillation-eliminating damping is
linearity-invariant, mapping any state on which a linear functional is
constant to such a state (Thm 2.3), and so is their bound-preserving
limiter (Thms 2.13–2.14). In 2D they preserve only the special
condition of a constant velocity vector; with a constant normal and a
jumping tangential velocity across a contact the 2D scheme does not, in
general, preserve the condition, even for a grid-aligned contact
(Remark 3.5).

**What fails without the equilibrium property.** Fujiwara et al.
compare four other schemes on the 1D test: a fully conservative
divergence scheme without pressure equilibrium (NPE) blows up at
$t\approx6.5$ (at $t\approx5.5$ in 2D), their divergence-form variant
FC/PE (D), which satisfies the condition only at the initial uniform
velocity, blows up at $t\approx3.8$, a non-conservative primitive
(Karni-type) scheme loses energy conservation, and an Abgrall-type
scheme transporting $1/(\gamma-1)$ loses species-mass conservation
(Figs. 3–5). On the tangential-velocity-jump test NPE oscillates while
FC/PE (S) keeps pressure in equilibrium and advects $v$ correctly
(Fig. 8). Their §5 analysis with non-uniform velocity explains why only
the split form survives long runs. See
[double-flux methods](/methods/double-flux-method.md) for the
overspecified alternatives they argue against.

Jiao et al. likewise find pressure and velocity at their initial
values after four periods with every reconstruction (Fig. 4.3).

**Interface thickness and shape.** Huang & Johnsen find that, without
the phase-field term, the disk becomes diamond-like from mesh
anisotropy; with it, the interface holds 4–5 cells and the circular
shape (Fig. 6). With a §5.2 temperature extension ($T_0=300$ K) the
temperature error is of the order of an earlier work they cite
(Fig. 13). Paula et al.'s time-averaged THINC keeps the 2D circle,
with triple points distorted and the quadruple point not (§7.1.2);
in the vortex the interface breaks up at maximum deformation and the
topology is restored at $t=T$ with slight deformation (Fig. 11). See
[THINC reconstruction](/methods/thinc-reconstruction.md).

On Zhang et al.'s (2024a) water block and droplet, MUSCL-THINC and
WENO5IS-THINC keep the interface width over ten periods while WENO5IS
alone diffuses it severely; the velocity and pressure errors are
negligible and the interface oscillation-free (§4.1, Figs. 3–4). See
[THINC reconstruction](/methods/thinc-reconstruction.md) and
[hybrid schemes](/methods/hybrid-weno.md).

On Jiao et al.'s square column all MUSCL limiters smear the interface,
Koren's least, and THINC with the thermodynamic update is noticeably
sharper (Fig. 4.2).

**Long-time error growth of high-order DG.** Cernetic et al.'s modal DG
with an evolved artificial-viscosity field captures the top-hat inside
a cell; the $L_1$ error grows in time like $t^{n_{\mathrm t}}$ with
fitted exponents $n_{\mathrm t}=0.427$, 0.335, 0.172, 0.056, 0.054,
0.049, 0.048, 0.046, 0.039, 0.028 for degrees 0 to 9 ($n_{\mathrm t}$
page-local), and degree 0 loses the profile after about 10 crossings
(Fig. 10). Lowering the onset threshold of their oscillation sensor from
$10^{-4}$ to $10^{-6}$ damps the ringing at the discontinuities at the
cost of a slightly wider front (Fig. 9); see
[artificial viscosity](/methods/artificial-viscosity.md).

**Order with diffusion.** Ching et al.'s DG converges at the optimal
order $N+1$ for degrees $N=1$–3 with both the BR2 and the
Lax–Friedrichs-type viscous flux, except on the coarse grids at degree
1 (Fig. 5.1). On meshes $h$ and $h/2$ both their positivity and entropy
limiters activate at every degree, and on $h/4$ at degree 1 only the
positivity limiter, so the limiters act on this smooth problem without
destroying the order (§5.1); see
[positivity-preserving Navier–Stokes flux](/methods/positivity-preserving-navier-stokes-flux.md).

**Order on smooth profiles.** Paula et al. find first order for their
first-order scheme and second order for the "nominally third-order
WENO3", which they call "well-known", with nearly the same density
errors with and without the interface (Fig. 12). The lateral order is
also limited to two because their fluxes are not integrated over cell
faces.

## Qualifications

- The 2D volume errors of Paula et al., $1.1\times10^{-8}$ and
  $3.3\times10^{-9}$, are about $10^6$ times their 1D value
  $5.4\times10^{-15}$ *(compiler check, not in the sources)*; the paper
  does not discuss the difference.
- Fujiwara et al.'s "CFL number of 0.05" matches the convective
  number $u_0\Delta t/\Delta x=1\cdot10^{-4}/0.002$; with the sound
  speed of species 2, $c=\sqrt{1.66\cdot0.9/0.2}\approx2.73$, the acoustic
  number $(u_0+c)\Delta t/\Delta x$ is about 0.19 *(compiler check, not in the sources)*. Their
  §4.3 prints a "periodic region $[0,1]$" for a 2D test and defines no
  $y_c$.
- Huang & Johnsen describe a water disk in air with phase 1 the air,
  but print $\alpha_1=1$ inside the disk and $0$ outside, i.e. a disk of
  phase 1; one of the two is inverted. Their initial data are printed
  without units while the equation-of-state constants are in Pa; their
  temperature constants $C^T_1=701.27$ and $C^T_2=223.37$ J/(kg K) are
  reproduced with $p=101325$ Pa, $\rho_1=1.204$, $\rho_2=1000$ kg m$^{-3}$
  and $T=300$ K, so the printed data are scaled by the water density
  and an unstated pressure scale *(compiler check, not in the
  sources)*.
- Jiao et al. print the gas constants in kJ/(kg K) and the densities in
  kJ/m$^3$ (Table 4.1); the printed $\rho=p_0/(RT)$ values, e.g.
  $10^7/(7500.75\cdot300)=4.444$, hold with $R$ in J/(kg K) and $\rho$
  in kg m$^{-3}$ *(compiler check, not in the sources)*. Their §3.3 and
  Table 4.2 give two different formulas for the MinMod limiter, and they
  do not define the CFL number of 1.4.
- Cernetic et al. say in §5.4 that 10 cells are used for the multi-degree
  comparison at $t=1$, while the Fig. 9 caption gives 64 cells for it
  and 10 cells for the degree-9 run at $t=0.01$.
- Fujiwara et al. restrict their scheme to smooth interfaces without
  shocks and to non-dissipative central fluxes; whether equilibrium
  survives added shock-capturing dissipation is left open.

# Citations

- [Fujiwara, Tamaki & Kawai (2023)](/sources/fujiwara-2023.md) — §4.1–4.3, §5, Eqs. (50)–(52), Figs. 2–8.
- [Paula, Adami & Adams (2023)](/sources/paula-2023.md) — §6, §7.1–7.3, Table 1, Figs. 11–12.
- [Huang & Johnsen (2023)](/sources/huang-2023.md) — §4.3, §5.2, Eq. (50), Figs. 6–7, 13.
- [Jiao et al. (2024)](/sources/jiao-2024.md) — §4.1, Tables 4.1–4.2, Figs. 4.1–4.3.
- [Cernetic et al. (2023)](/sources/cernetic-2023.md) — §5.4, Figs. 9–10 (arXiv v2).
- [Zhang et al. (2024a)](/sources/zhang-2024.md) — §3.3, §4, §4.1, Table 1, Table 2, Figs. 3–4.
- [Yan, Abgrall & Wu (2024)](/sources/yan-2024.md) — Lemma 2.5, Thms 2.3, 2.6, 2.13–2.14, Remark 3.5, Ex. 4.2, Figs. 3–4.
- [Ching et al. (2025)](/sources/ching-2025.md) — §5.1, Eq. (5.1), Fig. 5.1.
