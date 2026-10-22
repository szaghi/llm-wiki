---
type: Benchmark
title: "Kelvin–Helmholtz instability"
description: "Periodic two-dimensional shear-layer benchmark: Euler variants with sharp, exponentially smoothed and tanh-smoothed layers serve as a visual dissipation gauge, a positivity stress test for high-order DG and a probe of the non-convergence of inviscid shear flow; a smooth guiding-center Vlasov variant serves as a convergence test."
status: established
aliases: [KHI, Kelvin–Helmholtz, shear-layer instability]
tags: [benchmark, low-dissipation, central-scheme, dg, positivity, finite-volume]
timestamp: 2026-10-22T00:00:00Z
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
$(\rho,v_1,v_2,p)$.

**Exponentially smoothed layers.**
[Chertock et al. (2023)](/sources/chertock-2023.md) Ex. 8 and
[Wang et al. (2023)](/sources/wang-2023-b.md) Example 8 print the same
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
$\Delta x=\Delta y=1/1024$ and Wang et al. $1/400$.

**Sharp layers.** [Fu (2021)](/sources/fu-2021.md) §5.6:
$(\rho,v_1)=(2,-0.5)$ for $|y|\le0.25$, $(1,0.5)$ otherwise,
$v_2=0.01\sin(2\pi x)$, $p=2.5$, $\gamma=1.4$, on $[-0.5,0.5]^2$ with
$512\times512$ points, $t=1$.

**Tanh-smoothed layers.**
[Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md)
§5.2.1: on $[-1,1]^2$, with $B=\tanh(15y+7.5)-\tanh(15y-7.5)$ (a
page-local symbol, not the magnetic field),
$\rho=\tfrac12+\tfrac34B$, $p=1$, $v_1=\tfrac12(B-1)$,
$v_2=\tfrac1{10}\sin(2\pi x)$; $\gamma$ not stated in that subsection;
$64\times64$ elements of degree $N=7$, $t=10$, Mach number up to about
0.6.

The three setups differ in density ratio (2, 2, and 4 for the tanh
setup, where $\rho$ runs from $0.5$ to $2$ *(compiler check, not in the
sources)*), shear-layer thickness, perturbation wavenumber ($4\pi$ versus $2\pi$), background
pressure (1.5, 2.5, 1) and final time (4, 1, 10), so results do not
transfer between them.

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

**Visual dissipation gauge.** Wang et al. find that the A-WENO scheme
with the [adaptive-diffusion central-upwind flux](/methods/adaptive-diffusion-central-upwind-flux.md)
forms more pronounced vortex streets and more complex mixing than the
earlier flux (Fig. 8). Chertock et al. find the same for their
[LCD central-upwind scheme](/methods/lcd-central-upwind-scheme.md)
against the earlier [central-upwind scheme](/methods/central-upwind-scheme.md). Fu (2021) finds more small-scale structure with very-high-order
[TENO](/methods/adaptive-teno.md) than with
[WENO-CU6](/methods/weno-cu6.md) (Fig. 10). All three read
"more structure" as "less [numerical dissipation](/definitions/numerical-dissipation.md)".

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

**Positivity of high-order DG.** Rueda-Ramírez et al. report that both
standard and split-form [DGSEM](/methods/dgsem.md) ($N=7$, entropy- and
kinetic-energy-preserving volume flux, Rusanov surface flux) need a
positivity limiter on this case. With
[subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md)
enforcing $\rho\ge0.1\rho^{\mathrm{FV}}$, $p\ge0.1p^{\mathrm{FV}}$, the
peak blending coefficient is about 0.025 for both element-wise and
subcell-wise blending, but the space–time averaged amount of low-order
method is about three orders of magnitude smaller with subcell
blending (element-wise of order $10^{-6}$–$10^{-5}$, subcell-wise of
order $10^{-9}$–$10^{-8}$, read from Fig. 4b at ingestion; the text
says "about three orders of magnitude lower"). The authors note that the
two solutions differ visibly by $t=6.7$ and evolve to "substantially
different solutions" at $t=10$; they do not say which is more accurate.

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

- Chertock et al. print the Cesàro average with upper index $n$ where
  $m$ is meant, and refer to "the adaptive scheme" in the Ex. 8 text,
  a leftover: the paper has no adaptive scheme.
- None of the sources reports an error measure for the compressible
  Euler variants; the only error measurements are for the
  guiding-center variant, whose model, data and convergence behaviour
  differ entirely from the Euler ones.
- Zheng et al. state CFL $=10.2$ for Table 5 in the text and CFL $=1$
  in the table's caption; the paper does not resolve which was used.
  The second-to-last rate 7.22 of the non-split scheme is printed
  without comment.
- Kelvin–Helmholtz roll-up also appears as a secondary feature of other
  benchmarks: on the interface of the [shock–bubble interaction](/benchmarks/shock-bubble-interaction.md),
  where [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) §4.6
  find it sharpens with mesh refinement in 2D and is not captured on
  their 3D mesh, and in the two-material tri-point problem of
  [Li, Duan & Tang (2022)](/sources/li-2022-c.md) Ex. 5.7, resolved by
  the moving-mesh scheme. These are not runs of the benchmark itself.

# Citations

- [Chertock et al. (2023)](/sources/chertock-2023.md) — §5.2, Ex. 8, Fig. 5.9 (arXiv v2).
- [Wang et al. (2023)](/sources/wang-2023-b.md) — §4, Example 8, Fig. 8.
- [Fu (2021)](/sources/fu-2021.md) — §5.6, Fig. 10 (arXiv v1).
- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — §5.2.1, Figs. 4–6 (arXiv v2).
- [Zheng, Cai, Qiu & Qiu (2022)](/sources/zheng-2022.md) — §4.3, Ex. 4.6, Eq. (62), Table 5, Figs. 15–18.
- [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) — §4.6, Figs. 16–18 (roll-up on a shocked bubble only).
- [Li, Duan & Tang (2022)](/sources/li-2022-c.md) — Ex. 5.7 (roll-up in the tri-point problem only; arXiv v1).
