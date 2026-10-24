---
type: Benchmark
title: "Kelvin–Helmholtz instability"
description: "Periodic shear-layer benchmark: Euler variants with sharp and smoothed layers serve as a visual dissipation gauge, a robustness test for high-order and entropy-corrected DG and a probe of non-convergence; low-Mach and MHD variants check all-Mach schemes and entropy-stable MHD DG; relativistic MHD runs measure growth rates; Vlasov and viscous variants serve as convergence tests."
status: established
aliases: [KHI, Kelvin–Helmholtz, shear-layer instability]
tags: [benchmark, low-dissipation, central-scheme, dg, positivity, finite-volume]
timestamp: 2026-10-24T06:00:00Z
---

# Kelvin–Helmholtz instability

A periodic box of ideal gas holds a dense central strip moving in one
direction and a light outer stream moving in the other; a small
transverse velocity perturbation seeds the Kelvin–Helmholtz instability
of the two shear layers, which roll up into vortices and, without
physical viscosity, cascade to ever smaller scales. Because the
inviscid problem has no grid-converged solution, the benchmark does not
measure an error: it measures how much small-scale structure a scheme
lets develop on a given grid, and, for high-order element methods,
whether it stays positive under strong under-resolution. A different
model, the guiding-center Vlasov equation, carries a smooth version of
the same instability whose solution does converge, and is used as an
accuracy test.

## Variants

Three compressible-Euler setups appear in the sources, all periodic, in
$(\rho,v_1,v_2,p)$, plus a low-Mach variant run at the incompressible
limit of an all-Mach scheme.

**Exponentially smoothed layers.**
[Chertock et al. (2023)](/sources/chertock-2023.md) Ex. 8 and
[Wang et al. (2023b)](/sources/wang-2023-b.md) Example 8 print the same
data on $[-0.5,0.5]^2$ with $L=0.00625$:

$$
(\rho,v_1)=\begin{cases}
\big(1,\ -0.5+0.5e^{(y+0.25)/L}\big), & y<-0.25,\\
\big(2,\ 0.5-0.5e^{(-y-0.25)/L}\big), & -0.25\le y<0,\\
\big(2,\ 0.5-0.5e^{(y-0.25)/L}\big), & 0\le y<0.25,\\
\big(1,\ -0.5+0.5e^{(0.25-y)/L}\big), & y\ge0.25,
\end{cases}
\qquad v_2=0.01\sin(4\pi x),\quad p\equiv1.5,
$$

$\gamma=1.4$, snapshots at $t=1$, $2.5$, $4$. Chertock et al. use
$\Delta x=\Delta y=1/1024$ and Wang et al. (2023b) $1/400$.

**Sharp layers.** [Fu (2021)](/sources/fu-2021.md) §5.6:
$(\rho,v_1)=(2,-0.5)$ for $|y|\le0.25$, $(1,0.5)$ otherwise,
$v_2=0.01\sin(2\pi x)$, $p=2.5$, $\gamma=1.4$, on $[-0.5,0.5]^2$ with
$512\times512$ points, $t=1$.
[Ji, Liang & Fu (2022)](/sources/ji-2022.md) §5.7 print the same data
(single mode, $\gamma=1.4$, $t=1$) and run them on triangular meshes
with $h\approx1/500$ (577,416 elements, §5.10).
[Hu, Yuan & Zhao (2022)](/sources/hu-2022.md) §5.6, Eq. (5.8), also
print the same state, $(2,-0.5,0.01\sin(2\pi x),2.5)$ for $|y|\le0.25$
and $(1,0.5,0.01\sin(2\pi x),2.5)$ otherwise, but run it to $t=2$ on
$1000\times1000$ cells at CFL 0.5, with a second-order MUSCL scheme.
[Zhong et al. (2023)](/sources/zhong-2023.md) Ex. 12 print the same
two states on $[0,1]^2$ with the strip $0.25\le y\le0.75$,
$(\rho,v_1,p)=(2,0.5,2.5)$ inside and $(1,-0.5,2.5)$ outside, and a
perturbation localized at the two layers,
$v_2=0.1\sin(4\pi x)\big[e^{-(y-0.25)^2/(2\sigma^2)}+e^{-(y-0.75)^2/(2\sigma^2)}\big]$
with $\sigma=0.05/\sqrt2$ (page-local width), on $600\times600$ cells
to $t=0.8$; boundary conditions are not printed.
[Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) §5.1.5 use the
same strip and pressure on $[-0.5,0.5]^2$ with the velocities reversed,
$(\rho,v_1,v_2,p)=(2,0.5,0,2.5)$ for $|y|\le0.25$ and $(1,-0.5,0,2.5)$
otherwise, $\gamma=1.4$, and no seeded perturbation: the instability
grows from round-off. They run flux reconstruction of degree $N=4$ on
$100^2$, $200^2$, $400^2$ and $800^2$ elements to $t=2$; the boundary
conditions are not stated.

**Tanh-smoothed layers.**
[Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md)
§5.2.1: on $[-1,1]^2$, with $\mathcal B=\tanh(15y+7.5)-\tanh(15y-7.5)$ (a
page-local symbol, not the magnetic field),
$\rho=\tfrac12+\tfrac34\mathcal B$, $p=1$, $v_1=\tfrac12(\mathcal B-1)$,
$v_2=\tfrac1{10}\sin(2\pi x)$; $\gamma$ not stated in that subsection;
$64\times64$ elements of degree $N=7$, $t=10$, Mach number up to about
0.6. [Rueda-Ramírez et al. (2024)](/sources/ruedaramirez-2024.md) §3.2,
Eq. (49) (arXiv v1) rerun the same data, mesh, degree and final time at
CFL 0.9, again without stating $\gamma$ in the subsection.
[Lin & Chan (2024)](/sources/lin-2024.md) §4.3 run the same data on
$80\times80$ elements of degree $N=3$ to $T=10$, boundary conditions not
printed.
[Alberti et al. (2025)](/sources/alberti-2025.md) §3.1.2, Eq. (54),
following Chan et al., print the same layer profile,
$f=\tfrac12[\tanh(15y+7.5)-\tanh(15y-7.5)]=\tfrac12\mathcal B$, with
$v_1=f-\tfrac12$, $v_2=\tfrac1{10}\sin(2\pi x)$, $p=1$ on the doubly
periodic $[-1,1]^2$, but a density $\rho=\rho_1+f(\rho_2-\rho_1)$,
$\rho_1=1$, at Atwood number $(\rho_2-\rho_1)/(\rho_1+\rho_2)=0.75$,
i.e. $\rho_2=7$ and $\rho=1+3\mathcal B$, against $\rho=\tfrac12+\tfrac34\mathcal B$
(density ratio 4) of the runs above *(compiler check, not in the
sources)*. They run it to $t=14$ with modal DG of degree $N=4$–7 on quadrilateral $2^4\times2^4$ and $2^5\times2^5$ grids
and on triangular grids made from the same subdivisions, with the
entropy-stable Godunov flux, CFL $2.5\times10^{-2}$ and no limiter, as a
robustness test.

**Viscous smooth layers with a passive dye.**
[Cernetic et al. (2023)](/sources/cernetic-2023.md) §6 (arXiv v2) run
the Navier–Stokes variant of Lecoanet et al. (2016), whose solution
converges: on the periodic box of width 1 and height 2,
$\rho=1+\frac{\Delta\rho}{\rho_0}\frac12\big[\tanh\frac{y-y_1}a-\tanh\frac{y-y_2}a\big]$,
$v_1=u_{\mathrm f}\big[\tanh\frac{y-y_1}a-\tanh\frac{y-y_2}a-1\big]$,
$v_2=A\sin(2\pi x)\big[e^{-(y-y_1)^2/\sigma^2}+e^{-(y-y_2)^2/\sigma^2}\big]$,
and a dye $c=\frac12\big[\tanh\frac{y-y_2}a-\tanh\frac{y-y_1}a+2\big]$,
with $u_{\mathrm f}=1$, $a=0.05$, $y_1=0.5$, $y_2=1.5$, $A=0.01$,
$\sigma=0.2$, $p_0=10$ (Mach about 0.25) and $\Delta\rho/\rho_0=0$
(all page-local); $\mathrm{Re}=10^5$ with kinematic viscosity, thermal
and dye diffusivity $2u_{\mathrm f}/\mathrm{Re}=2\times10^{-5}$, and
$\mathrm{Re}=10^6$ also run. The metrics are the dye entropy and the
$L_2$ dye difference against the published DEDALUS spectral reference.

[Stone et al. (2026)](/sources/stone-2026.md) §4.1 take the same
Lecoanet et al. initial condition, printed as $P_0=10$, shear velocity
1, "width of shear profile" $\sigma=0.2$ and $a=0.01$ (their symbols,
page-local), on $[-0.5,0.5]\times[-1,1]$ with $512\times1024$ cells, the
LLF solver, PLM and RK2, without stating a viscosity, to compare a
passive contaminant advected by the fluid with $10^7$ Lagrangian Monte
Carlo tracer particles in [AthenaK](/software/athenak.md) at $t=2$ and
$3$ (Fig. 18). The tracers follow the mass flow and recover the
statistics of the fluid more accurately but are more diffusive than the
fluid evolution, an extra diffusivity that they call a consequence of
the probabilistic update, an effective random walk, which more
particles cannot reduce. Cernetic et al.'s $\sigma=0.2$ is the width of
the Gaussian of the velocity perturbation and their $a=0.05$ the
shear-layer thickness, so the two papers' labels of the same data
differ.

The three setups differ in density ratio (2, 2, and 4 for the tanh
setup, where $\rho$ runs from $0.5$ to $2$ *(compiler check, not in the
sources)*), shear-layer thickness, perturbation wavenumber ($4\pi$ versus $2\pi$, and $4\pi$ on the unit
box of Zhong et al.) and amplitude, background
pressure (1.5, 2.5, 1) and final time (4, 1, 2 or 0.8, 10), so results do not
transfer between them; Dzanic & Witherden also leave the perturbation
to round-off where the other sources seed it.

**Low-Mach (incompressible-limit) variant.**
[Boscarino, Qiu, Russo & Xiong (2022)](/sources/boscarino-2022.md)
Ex. 5.6 run their semi-implicit all-Mach scheme at global Mach number
$\varepsilon=10^{-6}$ with $\rho=p=1$ initially (here $\varepsilon$ is
the paper's Mach-number scaling, page-local). Their Kelvin–Helmholtz
case is $v_1=\cos y$, $v_2=0.03\sin(0.5x)$ on the periodic box
$[0,4\pi]\times[0,2\pi]$ (the box of the guiding-center variant
below), $T=40$, $256\times128$ points; a companion double shear layer
on $[0,2\pi]^2$ has $v_1=\tanh((y-\pi/2)/\delta_s)$ for $y\le\pi$ and
$\tanh((3\pi/2-y)/\delta_s)$ for $y>\pi$, $v_2=\delta\cos x$, $T=6$,
$256^2$, where the layer thickness $\delta_s$ (printed $\rho$) and the
amplitude $\delta$ are not given (page-local symbols). Both are smooth
shear flows; no density contrast is involved.

**Magnetized low-Mach variant.** [Chen, Wu & Xiong (2023)](/sources/chen-2023-b.md)
Ex. 5.9 (arXiv v1) extend the same semi-implicit all-Mach framework to
ideal MHD with constrained transport and run a magnetized
Kelvin–Helmholtz instability at $\varepsilon=10^{-6}$ on
$[0,2]\times[-0.5,0.5]$, $256\times128$ points, $\gamma=1.4$, $T=0.8$:
$(\rho,v_1,v_2,v_3,B_1,B_2,B_3,p)=(\gamma,\,1-2\eta(y),\,0.1\sin2\pi x,\,0,\,0.1,\,0,\,0,\,1)$,
vector potential $\mathsf A_3=0.1y$ (page-local, as on the Source page), with the layer profile $\eta=1$ on
$[-7/32,7/32]$, $\eta=\tfrac12(1+\sin(16\pi(y+1/4)))$ on
$[-9/32,-7/32]$, $\eta=\tfrac12(1-\sin(16\pi(y-1/4)))$ on $[7/32,9/32]$
and $0$ otherwise (page-local $\eta$); periodic for the conserved
variables, first-order extrapolation for $\mathsf A_3$. They print the velocity
as $1-2\eta(x)$ while $\eta$ is defined as a function of $y$.

**Low-Mach variant with a density contrast, and low-Mach double shear
layers.** [Zampa & Dumbser (2025)](/sources/zampa-2025.md) §4.4 (arXiv
v1) run, on the periodic $[-1,1]^2$ with a $120\times120$ unstructured
triangular mesh and polynomials of degree 1,
$\rho=1-\tfrac14\tanh\big(25(\lvert y\rvert-\tfrac12)\big)$,
$p=10^4/\gamma$, $v_1=-\tfrac12\tanh\big(25(\lvert y\rvert-\tfrac12)\big)$,
$v_2=\tfrac1{100}\sin(2\pi x)\cos(2\pi y)$, density shown at $t=2$, 3,
4, 5 (Fig. 5). With $\rho\approx1$ the sound speed is about 100, so the
shear speed $\tfrac12$ is a Mach number of about $5\times10^{-3}$
*(compiler check, not in the sources)*; the authors state that the
non-constant density puts the test outside their asymptotic-preserving
theory. Their §4.6 runs the double shear layer of Bell, Colella & Glaz on
the same box mapped to $\hat x=(x+1)/2$, $\hat y=(y+1)/2$:
$\rho=1$, $p=10^4/\gamma$, $v_1=\tanh(30(\hat y-0.25))$ for
$\hat y\le0.5$ and $\tanh(30(0.75-\hat y))$ above, $v_2=0.05\sin(2\pi\hat x)$,
viscosity $\mu=2\times10^{-4}$, 120 elements per side, $\Delta t=10^{-4}$,
vorticity at $t=0.8$, 1.6, 2.4, 3.6 (Fig. 7).
[Allegrini & Vignal (2025)](/sources/allegrini-2025.md) §4 (HAL
manuscript) run the same layer inviscid on the periodic $[0,1]^2$,
$\rho=p=1$, $v_1=\tanh(30(y-0.25))$ for $y<0.5$ and $\tanh(30(0.75-y))$
otherwise, $v_2=0.05\sin(2\pi x)$, to $t=1.2$ on $128^2$, with their
rescaling parameter $\varepsilon$ (the squared Mach-number scale,
$M^2=\varepsilon/\gamma$, page-local) decreased to $10^{-6}$ (Fig. 16).

**Ideal-MHD shear layers.** [Liu et al. (2025b)](/sources/liu-2025-b.md)
Ex. 7, after Yee & Sjögreen, run $(0,1)\times(-1,1)$, periodic, $\gamma=1.4$:
$\rho=1$, $v_1=5\big(\tanh(20(y+0.5))-\tanh(20(y-0.5))-1\big)$,
$v_2=0.25\sin(2\pi x)\big(e^{-100(y+0.5)^2}-e^{-100(y-0.5)^2}\big)$,
$v_3=0$, $p=50$, printed $B=(0,0,0)$, to $t=0.5$ on $256\times512$ (Fig.
8). [Liu et al. (2025c)](/sources/liu-2025-c.md) Ex. 5.4 take the MHD
setup of Mignone, Tzeferacos & Bodo, which they do not reprint, with
reflective walls (implied by their statement on entropy for reflective
walls), on $256\times512$ to $t=5$, 12 and 20, and plot the ratio of the
poloidal field $\sqrt{B_1^2+B_2^2}$ to the toroidal field $B_3$ and the
normalized poloidal magnetic energy; the linear growth lasts to $t\approx5$
and tearing-mode reconnection sets in from $t\approx8$ (see
[tearing-mode instability](/benchmarks/tearing-mode-instability.md)).

**Visco-resistive MHD variant.** [Dematté et al. (2024)](/sources/dematte-2024.md)
§4.3.2 run a magnetized shear layer on $[0,2]\times[-1,1]$, $1024^2$
cells, to $t=4$, with $\gamma=5/3$: $\rho_0=1$, $p_0=3/5$,
$v_1=-\tfrac12U_0\tanh\big((\lvert y\rvert-0.5)/a_{\mathrm l}\big)$,
$v_2=\delta_v\sin(2\pi x)\sin(\pi\lvert y\rvert)$, $v_3=0$, and a field
that rotates across the layer, $B=(b_0,0,0)$ for
$\tfrac12+a_{\mathrm l}<\lvert y\rvert\le1$,
$(b_0\sin\chi,0,b_0\cos\chi)$ for $\tfrac12-a_{\mathrm l}<\lvert y\rvert\le\tfrac12+a_{\mathrm l}$
and $(0,0,b_0)$ for $\lvert y\rvert\le\tfrac12-a_{\mathrm l}$, with
$\chi=\tfrac\pi2\,(y-0.5+a_{\mathrm l})/(2a_{\mathrm l})$; $a_{\mathrm l}=1/25$,
$U_0=1$, $\delta_v=0.01$, $b_0=0.07/\sqrt{4\pi}$, viscosity and
resistivity $10^{-3}$, no heat conduction (all page-local). An ideal
rerun (zero viscosity and resistivity) measures the changes of the
magnetic helicity $\tfrac12\int\mathsf A\cdot B$ and of the cross
helicity $\tfrac12\int v\cdot B$ ($\mathsf A$ the vector potential) and
the magnetic divergence, against an explicit Godunov scheme with
staggered constrained transport.

**Viscous high-Atwood variant.** Alberti et al. (2025) §3.2.2 rerun
their setup as a Navier–Stokes problem at Atwood number 0.99
($\rho_2/\rho_1=199$) on the $2^4\times2^4$ quadrilateral grid, degree
3, CFL $5\times10^{-3}$, to $t=10/\sqrt\gamma$, with the dynamic
viscosity $\sqrt\gamma\,\mathrm{Re}^{-1}$ in the light fluid and
$\sqrt\gamma\,\mathrm{Re}^{-1}\rho_2^{-\beta_\mu}$ in the heavy one
($\beta_\mu$ page-local, their $\beta$): $\mathrm{Re}=100$ with
$\beta_\mu=3/4$, so the heavy fluid's viscosity is about
$199^{-0.75}\approx0.02$ of the light one's *(compiler check, not in
the sources)*, and $\beta_\mu=0$ with $\mathrm{Re}$ up to 500.

**Relativistic resistive MHD variant.** [Mignone et al. (2024)](/sources/mignone-2024.md)
§4.6, Eqs. (68)–(69), after their second-order Paper I: a
three-dimensional double shear layer of relativistic MHD with shear
velocity $\tfrac12$, layer thickness $a_{\mathrm s}=0.01$ (page-local)
and profile in $\phi_{\mathrm s}=(\lvert y\rvert-\tfrac12)/a_{\mathrm s}$,
seeded by a perturbation of amplitude 0.1 with random phases localized
by $e^{-\phi_{\mathrm s}^2a_{\mathrm s}^2/0.1^2}$, a magnetic field with
poloidal and toroidal magnetization parameters $0.01$ and $1$, and
resistivity $\eta_{\mathrm m}=10^{-5}$, on $[-\tfrac12,\tfrac12]\times[-1,1]\times[-\tfrac12,\tfrac12]$
with $N_x\times2N_x\times N_x$ zones, $N_x=128,256$, to $t=30$, in [PLUTO](/software/pluto.md) with
the MHLLC solver and SSP(4,3,3) IMEX stepping with a linear fallback at
discontinuities.

**Guiding-center Vlasov variant.**
[Zheng, Cai, Qiu & Qiu (2022)](/sources/zheng-2022.md) Ex. 4.6 solve
the guiding-center model, a scalar density $\rho$ transported by the
drift velocity of its own electrostatic field: with $\Phi_{\mathrm e}$
the potential, $-\Delta\Phi_{\mathrm e}=\rho$, and
$E=-\nabla\Phi_{\mathrm e}$, the drift is
$E^\perp=(-\partial_y\Phi_{\mathrm e},\partial_x\Phi_{\mathrm e})=(E_2,-E_1)$
(Eq. 60) and $\partial_t\rho+\nabla\cdot(E^\perp\rho)=0$
(page-local symbols; the drift field is divergence-free, so the flow is
incompressible). The data are
$\rho(x,y,0)=\sin y+0.015\cos(x/2)$ on the periodic box
$[0,4\pi]\times[0,2\pi]$, a shear layer with a long-wave
perturbation; accuracy at $T=5$, contours at $T=40$. The model
conserves mass, energy and enstrophy, which serve as diagnostics.

## Findings across sources

**Visual dissipation gauge.** Wang et al. (2023b) find that the A-WENO scheme
with the [adaptive-diffusion central-upwind flux](/methods/adaptive-diffusion-central-upwind-flux.md)
forms more pronounced vortex streets and more complex mixing than the
earlier flux (Fig. 8). Chertock et al. find the same for their
[LCD central-upwind scheme](/methods/lcd-central-upwind-scheme.md)
against the earlier [central-upwind scheme](/methods/central-upwind-scheme.md). Fu (2021) finds more small-scale structure with very-high-order
[TENO](/methods/adaptive-teno.md) than with
[WENO-CU6](/methods/weno-cu6.md) (Fig. 10). All three read
"more structure" as "less [numerical dissipation](/definitions/numerical-dissipation.md)".
Ji, Liang & Fu (2022) read the sharp-layer case the same way on unstructured
triangles: finite-volume TENO3 is much more dissipative than the
higher-order [unstructured TENO](/methods/targeted-eno.md) schemes, and
TENO5/6 resolve more than [CWENO](/methods/cweno.md)5/6 (Figs. 18–20);
the text says TENO5/6 do better "in terms of preserving the kinetic
energy", but the figures show density only. The case also serves as
their cost benchmark: the normalised reconstruction time per element
and iteration grows from $1.32\times10^{-6}$ s (TENO3) to
$2.20\times10^{-6}$ s (TENO6), "roughly 65%" (Table 7).
Zhong et al. find that all six fifth-order finite-volume WENO schemes
they compare capture the small vortical structures and the
filamentation, with the largest degree of filamentation for their
IMWENO-P, whose smoothness indicators are mirror-symmetric (Fig. 14);
see [smoothness indicator](/definitions/smoothness-indicator.md).
Hu et al. use the case to compare [HLL-type solvers](/methods/hll-riemann-solvers.md)
inside one second-order scheme: their RHLLEM-LD solver gives the
sharpest interfaces and more filamentation, and is the only one of the
compared solvers (HLLE, HLLEM, HLLC, RHLLEM-LD) that retains the
symmetry of the roll-up (Fig. 5.6). Here the dissipation gauge ranks
Riemann solvers, not reconstructions.

**A converged viscous reference.** On the Lecoanet variant Cernetic et
al.'s modal DG with artificial viscosity matches the DEDALUS dye entropy
already at 64 cells per unit length and fourth order, 256 degrees of
freedom per dimension; under-resolved mesh runs over-mix, while the SPH
results of Tricco (2019) they cite under-mix (§6.2, Fig. 13). Their
$L_2$ dye error at 64 cells and fourth order equals that of the ATHENA
finite-volume code on 2048 cells, the SPH error is "orders of magnitude
larger", and among equal-degree-of-freedom runs (64 cells with $p=8$,
128 with $p=4$, 256 with $p=2$ in their labelling) the highest order has the lowest error,
which falls exponentially with the order at $t=4$ (§6.3, Figs. 14–15;
see [discontinuous Galerkin](/methods/discontinuous-galerkin.md)).

**Non-convergence and Cesàro averages.** Chertock et al. state that
numerical solutions of this problem do not converge under mesh
refinement and that the limit is a dissipative weak solution, which
Cesàro averages over a sequence of meshes approximate in $L^q$,
$1\le q<\infty$ (citing Feireisl, Lukáčová-Medviďová, Mizerová & She).
They average densities on meshes $1/2^5$ to $1/2^m$, $m=8,9,10$, and
find that the averages of the new and the old scheme differ, which they
interpret as non-uniqueness of the limit depending on the numerical
diffusion (Fig. 5.9). The interpretation rests on visual comparison.
It also qualifies the first finding: if the limit depends on the
scheme, more small-scale structure on one grid is not by itself
evidence of accuracy.

**Positivity of high-order DG.** Rueda-Ramírez et al. (2022) report that both
standard and split-form [DGSEM](/methods/dgsem.md) ($N=7$, entropy- and
kinetic-energy-preserving volume flux, Rusanov surface flux) need a
positivity limiter on this case. With
[subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md)
enforcing $\rho\ge0.1\rho^{\mathrm{FV}}$, $p\ge0.1p^{\mathrm{FV}}$, the
peak blending coefficient is about 0.025 for both element-wise and
subcell-wise blending, but the space–time averaged amount of low-order
method is "about three orders of magnitude lower" with subcell
blending (Fig. 4b). The authors note that the
two solutions differ visibly by $t=6.7$ and evolve to "substantially
different solutions" at $t=10$; they do not say which is more accurate.

Rueda-Ramírez et al. (2024) compare their monolithic
[convex limiting](/methods/convex-limiting.md) of LGL-DGSEM, which limits
at the semi-discrete level, with the predictor–corrector FCT/IDP
subcell limiting of the 2022 paper. With strict positivity bounds
(MCL) and with the 2022 heuristic bounds $\rho\ge0.1\rho^{\mathrm{FV}}$,
$p\ge0.1p^{\mathrm{FV}}$ (FCT/IDP) both reach $t=10$ with "remarkably
similar looking results"; FCT/IDP needs the positive threshold, "as
otherwise some nodes might get an invalid vacuum state" (§3.2, Fig. 1).
With local bounds (MCL on density, velocity and specific total energy;
FCT/IDP on density and a minimum of the modified specific entropy) the
two again agree, and local bounds add more dissipation than global ones
(Fig. 2); the mean limiting factors are plotted in Fig. 3.

[Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) take a
different route to positivity: their
[entropy filter](/methods/entropy-filtering.md), implemented in
[PyFR](/software/pyfr.md), damps the modes of each element that
violates positivity of $\rho$ and $p$ or a local minimum entropy
principle, with no low-order blending. On the unseeded sharp-layer
setup they report a resolved roll-up, no spurious oscillations and
pressure waves that are not over-dissipated, on meshes of $100^2$ to
$800^2$ elements (Fig. 5); the evidence is visual, as for the other Euler variants.

**Entropy limiting and the choice of high-order scheme.** Lin & Chan
(2024) run the tanh setup with [DGSEM](/methods/dgsem.md) limited by a
relaxed positivity constraint plus their semi-discrete cell entropy
inequality (subcell limiting factors from a linear program); the run is
robust and resolves fine-scale features. Applying the same limiting to
entropy-stable DG gives visibly different turbulent structures, from
which they conclude that the choice of the high-order scheme matters
(§4.3, Figs. 4–5); like Rueda-Ramírez et al. (2022), they do not say which is
closer to a converged solution.

**Helicity of a semi-implicit MHD scheme.** Dematté et al. show their
[semi-implicit all-Mach scheme](/methods/semi-implicit-all-mach-scheme.md)
on the visco-resistive run in Fig. 15. In the ideal rerun its magnetic-
and cross-helicity conservation errors are comparable to those of the
explicit second-order divergence-free Godunov scheme, and the authors
state that no standard ideal-MHD scheme conserves these quantities exactly (§4.3.2,
Fig. 16). See [divergence-free magnetic field](/properties/divergence-free-magnetic-field.md).

**Divergence at the incompressible limit.** Boscarino et al. report
vorticity comparable to the isentropic all-Mach results of their earlier
scheme, and an $L^\infty$ error of $\nabla\cdot v$ (measured with
zero-viscosity fifth-order WENO and with fourth-order central
differences) that grows in time and jumps when the fine structures are
no longer resolved (Fig. 5.7). They state that, for incompressible or
weakly compressible flows without initial discontinuities, high-order
linear reconstruction "would perform better than WENO reconstructions in
preserving the divergence and in resolving solution structures"; the
divergence comparison is shown, the resolution claim is not shown
separately. See [asymptotic preservation](/properties/asymptotic-preservation.md)
for the scheme's low-Mach limit. Chen, Wu & Xiong compare the
vorticity and the ratio of local to sonic Mach number of the
magnetized run qualitatively with the hydrodynamic results of Boscarino
et al. and with Leidi et al., "comparable", and present this as the
numerical check of the asymptotic-preserving property of their MHD
scheme (Fig. 5.7); the vorticity is computed with fourth-order central
differences.

**Low-Mach shear layers of compatible finite elements and IMEX finite
volumes.** Zampa & Dumbser compare their low-Mach Kelvin–Helmholtz and
double-shear-layer results with the literature only qualitatively
(Figs. 5, 7). Allegrini & Vignal measure the density error against 1 at
$\varepsilon=10^{-3}$: $9.18\times10^{-3}$ on $128^2$ and
$5.13\times10^{-3}$ on $256^2$, which they describe as "of order
$\varepsilon$"; the printed errors are 5 to 9 times $\varepsilon$ and
fall by a factor 1.8 under refinement *(compiler check, not in the
sources)*.

**Entropy stability and the magnetic field.** Liu et al. (2025c) run
their globally divergence-free entropy-stable nodal DG at $N=2,3,4$
(their face degree $k=1,2,3$) without any limiter; the total entropy does not increase and the
divergence norm stays at machine level for $N=3$ (Figs. 7–9). Liu et
al. (2025b) describe "growth of the magnetic field … amplified by the
vortical flow" with their entropy-stable oscillation-free DG and plot
the magnetic pressure in $[1,21]$ (Fig. 8). With the printed initial
field $B=0$ the ideal induction equation $\partial_tB=\nabla\times(v\times B)$
keeps $B\equiv0$, so the printed data cannot produce that figure and
the initial field as printed is incomplete *(compiler check, not in the
sources)*.

**Entropy correction and BR2 projection in modal DG.** Alberti et al.
(2025) use the inviscid case to compare their entropy-projection DG
(STD) with five discrete entropy-balance (DEEB) corrections: every DEEB
variant completes more runs than STD, the variants they label a and b
are the more robust on triangles, and on the fine triangular grids,
they state, all DEEB variants complete up to degree 3 while STD fails
above degree 1 (Fig. 4; see
[entropy projection](/methods/entropy-projection.md)). The DEEB variants
cost 1.2–1.5 times STD on $2^5\times2^5$ for degrees 3–7, on two
cluster nodes of two Intel Xeon E5-2620 v4 each, 32 MPI processes
(Table 2). In the viscous runs only their entropy-projected
[BR2](/methods/bassi-rebay-viscous-discretization.md) discretization
$\Pi_{\mathrm{BR2}}$ reaches the final time at $\mathrm{Re}=100$,
$\beta_\mu=3/4$, and produces the least entropy in the common time
window; it fails for a penalty $\eta_F<2$ (page-local, the BR2 penalty).
With $\beta_\mu=0$ all schemes complete for $\mathrm{Re}<500$, at
$\mathrm{Re}=500$ only $\Pi_{\mathrm{BR2}}$, with the penalty threshold
$\eta_F=4$ (Figs. 9–12). $\Pi_{\mathrm{BR2}}$ costs 1.34, 1.42, 1.52,
1.58 and 1.62 times BR2 for degrees 3–7, an overhead that the authors
say "tends to hinder its applicability in production-grade solvers"
(Table 4, §4). They also note that a globally increasing entropy does
not guarantee a consistent entropy evolution in each element (§3.2.2).

**Growth rates at fourth order in relativistic MHD.** Mignone et al.
(2024) measure growth rates of about 2.94 and 2.14 with the
second-order scheme of Paper I (low and high resolution) and about 2.17
and 2.31 with their fourth-order finite-volume scheme; the fourth-order
run at $N_x=128$ "already outperforms" the second-order one at twice the
resolution, and resolves the large-scale modes better, as the density
spectra $P(k_x)$ at $t=15$ show (Figs. 7–8).

**Convergence and operator splitting on the guiding-center variant.**
Zheng et al. compare their non-split
[conservative semi-Lagrangian finite-volume WENO](/methods/semi-lagrangian-finite-volume.md)
scheme with a dimensionally split fourth-order semi-Lagrangian WENO
scheme of the same group. Against reference solutions at $T=5$, the
non-split scheme converges at fourth order ($L^2$ error from
$3.49\times10^{-3}$ on $16^2$ to $8.89\times10^{-11}$ on $512^2$, rates
3.73, 4.66, 4.49, 7.22, 5.14), while the split scheme converges at
first order (rates 0.88–0.99, $9.03\times10^{-4}$ on $512^2$); at fixed
mesh $128^2$ the temporal order is four for the non-split scheme and one
for the split one (Table 5, Fig. 15). At $T=40$ the non-split scheme at
CFL 1 and 10.2 matches published solutions, while the split scheme
matches them at CFL 0.1 and deviates "significantly" at CFL 1
(Figs. 16–17). Energy and enstrophy deviations are smaller with the
non-split scheme; mass is conserved to about $10^{-13}$ by both
(Fig. 18). Here, unlike the Euler variants, the instability is a smooth,
convergent flow, and the benchmark measures an error.

## Qualifications

- Liu et al. (2025b)'s Ex. 7 is not reproducible from the paper: the
  initial magnetic field is printed as zero (see above). Liu et al.
  (2025c) give no initial data for their MHD run.
- Zampa & Dumbser and Allegrini & Vignal are read as arXiv v1 and the
  HAL manuscript.
- Chertock et al. print the Cesàro average with upper index $n$ in
  place of the $m$ of their text, and refer to "the adaptive scheme" in the Ex. 8 text,
  a leftover: the paper has no adaptive scheme.
- None of the sources reports an error measure for the compressible
  Euler or MHD variants; the only error measurements are for the
  guiding-center variant, whose model, data and convergence behaviour
  differ entirely from the Euler ones, and for Cernetic et al.'s viscous
  Navier–Stokes variant against a spectral reference.
- Cernetic et al. print the DEDALUS resolution as $3096\times6144$ for a
  domain of aspect ratio 1:2, and the ATHENA resolution as 1024 cells in
  one sentence of §6.3 and 2048 cells in the next and in Fig. 14; they
  also alternate between degree and order for their "$p$" in captions and
  text (the orders above follow the text).
- Zheng et al. state CFL $=10.2$ for Table 5 in the text and CFL $=1$
  in the table's caption; the paper does not resolve which was used.
  The second-to-last rate 7.22 of the non-split scheme is printed
  without comment.
- Alberti et al. (2025) caption their CPU-time Table 2 "KHI, $A=0.33$",
  degrees 3–7, and their viscous Table 4 "$A=0.95$", while the text runs
  the inviscid robustness tests at Atwood number 0.75 (degrees 4–7)
  and the viscous ones at 0.99.
- Mignone et al. (2024) print the density of Eq. (68) with $\rho_h$ in
  both terms and give no density values, nor the $p$ and $\sigma$ that
  enter their magnetic field (where $\sigma$ is also $1/\eta_{\mathrm m}$); and their
  text says that higher resolution or accuracy gives "a gradual
  reduction of the growth rate", while their fourth-order rates rise
  from about 2.17 to 2.31 with resolution.
- Kelvin–Helmholtz roll-up also appears as a secondary feature of other
  benchmarks: on the interface of the [shock–bubble interaction](/benchmarks/shock-bubble-interaction.md),
  where [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) §4.6
  find it sharpens with mesh refinement in 2D and is not captured on
  their 3D mesh, and where [Yan, Abgrall & Wu (2024)](/sources/yan-2024.md)
  Ex. 4.11 see it on the shocked helium bubble of their OEDG runs;
  along the shear layers of the second two-dimensional Riemann problem
  of [Deng, Jiang & Yan (2025)](/sources/deng-2025.md) §4.4 (see
  [two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md));
  and in the two-material tri-point problem of
  [Li, Duan & Tang (2022c)](/sources/li-2022-c.md) Ex. 5.7, resolved by
  the moving-mesh scheme. These are not runs of the benchmark itself.
- The roll-up of the slip line of the
  [double Mach reflection](/benchmarks/double-mach-reflection.md) is
  read the same way, as a dissipation gauge:
  [Hiejima (2022)](/sources/hiejima-2022.md) §3.4 finds no roll-up with
  Jiang–Shu weights at fifth to eleventh order of a
  [WCNS](/methods/weighted-compact-nonlinear-scheme.md), while with
  [TENO](/methods/targeted-eno.md) weights the roll-up grows from fifth
  to ninth order and vanishes at eleventh order on $1024\times256$,
  which the author attributes to a first-order fallback for negative
  interpolated states;
  Dzanic & Witherden §5.1.4 keep it with their filter;
  [Lesur et al. (2023)](/sources/lesur-2023.md) §4.1 find the beginning
  of Kelvin–Helmholtz rolls on the jet only with the least diffusive
  reconstructions of their second-order code (LimO3, PPM) at
  $1920\times480$ (Fig. 3);
  [Wang et al. (2022a)](/sources/wang-2022.md) §3.4 state that it is
  "generally thought" to depend more on the interior scheme than on the
  [immersed-boundary](/methods/immersed-boundary-method.md) treatment.
  These, too, are not runs of the Kelvin–Helmholtz benchmark.

# Citations

- [Chertock et al. (2023)](/sources/chertock-2023.md) — §5.2, Ex. 8, Fig. 5.9 (arXiv v2).
- [Wang et al. (2023b)](/sources/wang-2023-b.md) — §4, Example 8, Fig. 8.
- [Fu (2021)](/sources/fu-2021.md) — §5.6, Fig. 10 (arXiv v1).
- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — §5.2.1, Figs. 4–6 (arXiv v2).
- [Zheng, Cai, Qiu & Qiu (2022)](/sources/zheng-2022.md) — §4.3, Ex. 4.6, Eq. (62), Table 5, Figs. 15–18.
- [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) — §4.6, Figs. 16–18 (roll-up on a shocked bubble only).
- [Li, Duan & Tang (2022c)](/sources/li-2022-c.md) — Ex. 5.7 (roll-up in the tri-point problem only; arXiv v1).
- [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) — §5.1.5, Fig. 5; §5.1.4 (slip-line roll-up only) (arXiv v3).
- [Ji, Liang & Fu (2022)](/sources/ji-2022.md) — §5.7, Figs. 18–20; §5.10, Table 7 (preprint).
- [Hu, Yuan & Zhao (2022)](/sources/hu-2022.md) — §5.6, Eq. (5.8), Fig. 5.6.
- [Boscarino, Qiu, Russo & Xiong (2022)](/sources/boscarino-2022.md) — Ex. 5.6, Fig. 5.7 (arXiv v2).
- [Lesur et al. (2023)](/sources/lesur-2023.md) — §4.1, Fig. 3 (slip-line roll-up of the double Mach reflection only; arXiv v1).
- [Hiejima (2022)](/sources/hiejima-2022.md) — §3.4, Figs. 7–9 (slip-line roll-up of the double Mach reflection only).
- [Wang et al. (2022a)](/sources/wang-2022.md) — §3.4 (slip-line roll-up only).
- [Chen, Wu & Xiong (2023)](/sources/chen-2023-b.md) — Ex. 5.9, Fig. 5.7 (arXiv v1).
- [Zhong et al. (2023)](/sources/zhong-2023.md) — §4.4, Ex. 12, Fig. 14.
- [Rueda-Ramírez et al. (2024)](/sources/ruedaramirez-2024.md) — §3.2, Eq. (49), Figs. 1–3 (arXiv v1).
- [Cernetic et al. (2023)](/sources/cernetic-2023.md) — §6, Figs. 11–15 (arXiv v2).
- [Lin & Chan (2024)](/sources/lin-2024.md) — §4.3, Figs. 4–5.
- [Dematté et al. (2024)](/sources/dematte-2024.md) — §4.3.2, Figs. 15–16.
- [Alberti et al. (2025)](/sources/alberti-2025.md) — §3.1.2, §3.2.2, Eq. (54), Tables 2 and 4, Figs. 4, 9–12.
- [Mignone et al. (2024)](/sources/mignone-2024.md) — §4.6, Eqs. (68)–(70), Figs. 7–8.
- [Yan, Abgrall & Wu (2024)](/sources/yan-2024.md) — Ex. 4.11 (roll-up on a shocked bubble only).
- [Deng, Jiang & Yan (2025)](/sources/deng-2025.md) — §4.4 (roll-up in a Riemann problem only).
- [Zampa & Dumbser (2025)](/sources/zampa-2025.md) — §4.4, §4.6, Figs. 5, 7 (arXiv v1).
- [Allegrini & Vignal (2025)](/sources/allegrini-2025.md) — §4, Fig. 16 (HAL manuscript).
- [Liu et al. (2025b)](/sources/liu-2025-b.md) — Ex. 7, Fig. 8.
- [Liu et al. (2025c)](/sources/liu-2025-c.md) — Ex. 5.4, Figs. 7–9.
- [Stone et al. (2026)](/sources/stone-2026.md) — §4.1, Fig. 18.
