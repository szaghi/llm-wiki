---
type: Method
title: "Artificial viscosity and spectral viscosity"
description: "Artificial viscosity adds solution-dependent dissipation instead of overwriting the solution; the page covers the high-order Jameson–Schmidt–Turkel blend, graph viscosity, Laplacian DG viscosities driven by a time-reversibility defect, a learned modal decay or a time-evolved SPH-type switch, residual-based finite-element viscosity, spectral and quasi-spectral eddy viscosities, C-function viscosity on moving meshes, and modal damping read as dissipation."
status: established
aliases: [artificial diffusion, artificial diffusivity, artificial dissipation, nonlinear stabilization, spectral viscosity, spectral vanishing viscosity, SVV, modal filtering, damping, JST-type dissipation, Jameson–Schmidt–Turkel dissipation, graph viscosity, time-reversibility viscosity, TR viscosity, local artificial diffusivity, LAD, residual-based viscosity, RV, residual viscosity, time-dependent artificial viscosity, viscosity switch]
tags: [limiting, dg, low-dissipation, finite-difference, weno, machine-learning]
timestamp: 2026-10-23T11:06:00Z
---

# Artificial viscosity and spectral viscosity

Artificial viscosity suppresses spurious oscillations by adding a
dissipative term whose strength depends on the solution, rather than by
replacing the solution in troubled cells as limiters do. In the sources of
this bundle it appears in six forms: a **blend of low- and high-order
dissipation** switched by a shock sensor, in finite-difference central
schemes ([Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md)) and in
continuous finite elements ([Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md));
a first-order **graph viscosity** that makes a low-order scheme
invariant-domain preserving ([Pazner (2021)](/sources/pazner-2021.md));
a **Laplacian viscosity for DG and flux reconstruction** whose magnitude
comes from an indicator, a time-reversibility defect
([Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md)), a learned
modal decay rate ([Yu & Hesthaven (2022)](/sources/yu-2022.md)) or a
viscosity field evolved in time by sources and decay
([Cernetic et al. (2023)](/sources/cernetic-2023.md)), and its
continuous-finite-element counterpart driven by a normalized PDE residual
([Dao & Nazarov (2022)](/sources/dao-2022.md));
**spectral and quasi-spectral eddy viscosities** that act on the highest
resolved wavenumbers ([Sousa & Scalo (2022)](/sources/sousa-2022.md));
a **damping of the modal coefficients** of a DG solution, which is the
high-order dissipation of spectral-viscosity and filtering methods
([Peng, Sun & Wu (2024)](/sources/peng-2024.md)); and **solution
filtering** read as a dissipation operator ([Edoh (2022)](/sources/edoh-2022.md)).
The JST-type, finite element, quasi-spectral and modal forms are evaluated
in every cell; the first two need a
[shock sensor](/definitions/troubled-cell-indicator.md) only to set the
weight of the low-order part. A further form, a space–time smooth
viscosity scaled by C-functions on moving meshes, is that of
[Ramani & Shkoller (2023)](/sources/ramani-2023.md).

## High-order Jameson–Schmidt–Turkel dissipation (finite differences)

**Odd-order schemes as central plus dissipation.**
[Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) (§3, Eqs.
(20)–(28)) start from the Lerat–Corre family of odd-order schemes, as
recalled: with $\Delta^mu_{i+1/2}$ the $m$-th undivided difference centred
at the interface (registry §10, here centred at $x_{i+1/2}$) and
$\mu f_{i+1/2}=\tfrac12(f_i+f_{i+1})$ (page-local), the interface flux
$$\hat f_{i+1/2}=\Big[\Big(1-\sum_{p=0}^{P}a_p\Delta^{2+2p}\Big)\mu f\Big]_{i+1/2}+\frac{a_P}{2}\,\lvert Q\rvert\,\Delta^{2P+3}u_{i+1/2}$$
(signs as the explicit members (25)–(28) print them; $P$, $a_p$, $Q$
page-local, $Q$ not the SBP matrix of the registry) is of order $2P+3$ on $2(P+2)+1$ points, with
$a_0=\tfrac16$, $a_1=-\tfrac1{30}$, $a_2=\tfrac1{140}$, $a_3=-\tfrac1{630}$.
It is a central difference of order $2(P+2)$ of the flux derivative plus an
artificial viscosity of order $2P+3$, whose leading truncation error is an
even derivative, $\frac{a_P}{2}\Delta x^{2P+3}\partial_x^{2(P+2)}u$, and
therefore dissipative (Eq. (24)); the dispersion error is exactly that of
the central scheme. $Q$ is a dissipation matrix: Roe's $\lvert A\rvert$, or
the spectral radius $a$ (Rusanov). The authors take the scalar $a$ to avoid
the non-unique and costly extension of Roe averaging to real and
multi-species gases (Eq. (29)).

**The adaptive blend** (§3, Eqs. (30)–(35)). The scheme adds a
second-order dissipation switched by the sensor $\Xi_i$ (page-local) of the
[troubled-cell indicator](/definitions/troubled-cell-indicator.md) page
(Ducros × Jameson × Bhagatwala–Lele), in Jameson–Schmidt–Turkel form:
$$\mathcal D_{i+1/2}=a_{i+1/2}\Big[\varepsilon_2\,\Delta^1u+(-1)^{P+1}\varepsilon_{2(P+2)}\,\Delta^{2P+3}u\Big]_{i+1/2},\qquad
\varepsilon_{2,i+1/2}=k_2\max(\Xi_i,\Xi_{i+1}),\quad
\varepsilon_{2(P+2),i+1/2}=\max\big(0,\ k_{2(P+2)}-k_\varepsilon\,\varepsilon_{2,i+1/2}\big)$$
($\mathcal D$, $\varepsilon_2$, $\varepsilon_{2(P+2)}$, $k_2$,
$k_{2(P+2)}$, $k_\varepsilon$ page-local; the source's JST notation
$\varepsilon^{(2)}$, $\varepsilon^{(4)}$). Where the sensor is on, the
second-order term grows and the high-order one is switched off; with
$k_2=0$ and $k_{2(P+2)}=\lvert a_P\rvert/2$ the odd-order upwind scheme is
recovered. The production scheme is the ninth-order member, $P=3$:
$$\mathcal D=a\big[\varepsilon_2\Delta^1u+\varepsilon_{10}\Delta^9u\big],\qquad \varepsilon_{10}=\max\big(0,\ k_{10}-\tfrac1{105}\varepsilon_2\big),$$
with $k_2=1$ and $k_{10}=1/1260$, the upwind value $\lvert a_3\rvert/2$, by
default, and $k_2=2$, $k_{10}=1/630$ on the shock tubes. The design aim is a
truncation error dominated by dissipation, which limits both spurious
oscillations and the activation of the low-order term (§1).

**Evidence** (§4–§5). The ninth-order dissipation acts only above a
reduced wavenumber $\vartheta\approx0.35\pi$, fewer than six points per
wavelength, and leaves larger scales almost untouched (Fig. 1;
[numerical dissipation](/definitions/numerical-dissipation.md)). On the
[isentropic vortex](/benchmarks/isentropic-vortex.md) ninth order appears
only when the CFL number is below about 0.0125, because the third-order
Runge–Kutta error dominates otherwise (§4.1). On the compressible
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) (Re 1600,
$M=0.1$–1, $64^3$–$1024^3$) the scheme behaves as an implicit LES without
energy pile-up, and the order of the dissipation matters more than that of
the convective flux: third-order dissipation with up to tenth-order
convective fluxes gives nearly identical results, while ninth-order
dissipation on $64^3$ is close to third order on $256^3$ (§5.2, Fig. 11).

## Low- and high-order dissipation operators (continuous finite elements)

[Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) (§3) stabilize the
Galerkin form of a scalar law with cellwise forms $s_h^e(u_h,w_h)$ added to
the weak form. Let $\mu_e$ denote the cellwise viscosity coefficient
(page-local; the source writes $\nu_e$, which the registry reserves for the
CFL number), $a_e=\lVert f'(u_h)\rVert_{L^\infty(K_e)}$ the local maximum wave
speed, $h_e$ the cell diameter and $N$ the polynomial degree.

- **Low order** (Eq. (4)): $s_h^{e,L}(u_h,w_h)=\mu_e\int_{K_e}\nabla w_h\cdot\nabla u_h\,dx$,
  $\mu_e=a_eh_e/(2N)$. Isotropic first-order viscosity with an
  $O(h^{1/2})$ consistency error (§3, §6).
- **High order, variational multiscale** (Eq. (5)):
  $\mu_e\int_{K_e}\nabla w_h\cdot(\nabla u_h-g_h)\,dx$, with $g_h$ a continuous
  ($L^2$-projected) approximation of $\nabla u_h$; consistency error
  $O(h^{N+1/2})$. It is equivalent in 1D to a consistent SUPG method (as
  recalled from Lohmann et al.), but it is not symmetric and "may produce
  entropy".
- **High order, symmetric projection form** (Eq. (7)):
  $\mu_e\int_{K_e}(\nabla w_h-g_h(w_h))\cdot(\nabla u_h-g_h(u_h))\,dx$, coercive
  and therefore truly dissipative; a local-projection stabilization.

**Nonlinear blending (JST design in finite elements).** The CG-WENO method
of [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) blends the two with a
cellwise factor $\varsigma_e\in[0,1]$ (page-local; the source writes
$\gamma_e$) (Eq. (8)):
$$s_h^e(u_h,w_h)=\omega_{\mathrm H}\,\varsigma_e\,\mu_e\int_{K_e}(\nabla w_h-\pi_h\nabla w_h)\cdot(\nabla u_h-\pi_h\nabla u_h)\,dx+(1-\varsigma_e)\,\mu_e\int_{K_e}\nabla w_h\cdot\nabla u_h\,dx,$$
with $\pi_h$ the $L^2$ projection of gradients and $\omega_{\mathrm H}\in[0,1]$
a scaling of the high-order part (page-local; 1 in all experiments).
$\varsigma_e=1$ in smooth cells (high-order dissipation only), $\varsigma_e\to0$
in troubled cells (low-order viscosity). The factor is the WENO-deviation
sensor defined on the [troubled-cell indicator](/definitions/troubled-cell-indicator.md)
page; the reconstruction is used only to compute it and never overwrites the
finite element solution, so the semi-discrete scheme keeps the structure of a
continuous Galerkin method (Rem. 2). The authors present the scheme as a
multidimensional, high-order finite element analogue of the
Jameson–Schmidt–Turkel blend of second- and fourth-difference dissipation,
and argue that a nonlinear artificial-diffusion structure is easier to
analyse than DG-WENO schemes that manipulate derivatives directly (§3, §8).
The full method is on
[dissipation-based WENO stabilization](/methods/weno-stabilized-continuous-galerkin.md).
Sciacovelli et al. also call their finite-difference scheme above a JST
form: both sources keep a high-order dissipation everywhere and trade it,
through a sensor, for a first-order one at shocks.

**Consistency** (§6, labelled "preliminary" by the authors). For steady
advection–reaction, the stabilization has, in the worst case, an $O(h^{1/2})$
consistency error; for $u\in C^{N+1}$ and exponent 2 in the sensor,
$\sqrt{s_h(I_hu;I_hu,I_hu)}=O(h^{N+1/2})$, which the authors call optimal for
general meshes. Polynomials of degree $\le N$ are reproduced exactly
(Rem. 6). An a priori estimate follows under an assumed, unverified
Lipschitz-type condition.

## Graph viscosity (first-order, invariant-domain preserving)

The low-order scheme of [convex limiting](/methods/convex-limiting.md) is an
algebraic artificial viscosity. [Pazner (2021)](/sources/pazner-2021.md)
(§3.1, Eqs. (32)–(35), after Guermond and Popov) adds to a nodal
discretization with coefficients $c_{ij}$ the viscosity
$$d_{ij}=\max\big\{a_{\max}(u_i,u_j,n_{ij})\lVert c_{ij}\rVert,\ a_{\max}(u_j,u_i,n_{ji})\lVert c_{ji}\rVert\big\},\qquad d_{ii}=-\sum_{j\ne i}d_{ij},$$
with $n_{ij}=c_{ij}/\lVert c_{ij}\rVert$ and $a_{\max}$ an upper bound of the
maximum wave speed of the Riemann problem (page-local $c_{ij}$, $d_{ij}$,
$a_{\max}$), which makes the forward-Euler update a convex combination of
bar states. Every connection of the stencil adds viscosity, so on the
dense DGSEM operator, which couples each node to $O(N)$ others, the
low-order method grows more diffusive with $N$ at fixed degrees of
freedom; on a sparsified operator with an $O(1)$ stencil it does not
($N=3,7,15,31$ on 128 degrees of freedom, §3.4, Fig. 1). The modal
smoothness indicator Pazner uses to relax the limiter bounds is taken from
Persson and Peraire's shock-capturing work (§4.4).
[Lin, Chan & Tomas (2023)](/sources/lin-2023.md) use the same graph
viscosity on a sparse low-order SBP operator for the Navier–Stokes
equations, with Zhang's viscous positivity coefficient in place of the
wave-speed bound (§5, Eqs. 16–18;
[positivity-preserving Navier–Stokes fluxes](/methods/positivity-preserving-navier-stokes-flux.md)).

## Laplacian viscosity for DG and flux reconstruction

The sources add to the conservation law a parabolic term,
$\partial_tu+\nabla\cdot f(u)=\nabla\cdot(\mu\nabla u)$, discretized with the
DG machinery of second-order terms, and differ in how they set the
elementwise viscosity.

**Time-reversibility (TR) viscosity.**
[Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) (§2, Eqs.
(2)–(7)) take the componentwise defect $d_{\mathrm{TR}}$ of a forward
upwind Euler step followed by a backward downwind one (defined on the
[troubled-cell indicator](/definitions/troubled-cell-indicator.md) page),
and set a **vector** viscosity, one value per conserved component
(page-local $\mu_{\mathrm{TR}}$, $c_\mu$, $\Delta_\Omega u$),
$$\mu_{\mathrm{TR}}=c_\mu\,\frac{h^2\,d_{\mathrm{TR}}(u^n)}{\Delta t\,\Delta_\Omega u^n},\qquad \Delta_\Omega u^n=\max_\Omega u-\min_\Omega u\ \text{ over }[t^n,t^{n+1}],$$
componentwise, with $h$ the local mesh scale ($h^d$ the element volume). A
first-order analysis on step data (forward Euler, upwind flux, uniform grid,
§3) gives for linear advection with speed $a>0$ a defect
$\nu(1-\nu)\lvert[\![u]\!]\rvert$ on both sides of the jump, hence
$$\mu_{\mathrm{TR}}=c_\mu\big(a\Delta x-a^2\Delta t\big)\ \to\ c_\mu\,a\,\Delta x\quad(\Delta t\to0)$$
(Eqs. (18)–(20); *compiler check, not in the sources: substituting the two
steps into the step data*). With $c_\mu=\tfrac12$ this is the "monotone"
viscosity, with which a second-order central scheme becomes first-order
upwind. For Burgers' equation with $u^-,u^+>0$ the limit is
$c_\mu\lvert\tfrac12(u^-+u^+)\rvert\Delta x$, the shock speed times $c_\mu\Delta x$
(Eq. (30)). The viscosity is elementwise constant and capped by
$\mu_{\max}=c_{\max}\hat a\,h_{\max}$, $c_{\max}\approx100$, $\hat a$ an a
priori maximum wave speed, only to keep transients from limiting the
explicit step (Eq. (40); page-local); in 1D, with implicit viscous terms,
results were identical with and without the cap. The method is
implemented in PyFR ([PyFR](/software/pyfr.md);
[flux reconstruction](/methods/flux-reconstruction.md) recovering nodal DG,
Rusanov flux with Davis wave speeds, BR1, RK4), with one forward Euler pair
per stage (§4). The paper relates it to Guermond et al.'s entropy
viscosity: both rest on entropy production, but TR viscosity needs no
entropy residual and no entropy pair (§2).

Evidence (§5): on [Burgers](/benchmarks/burgers-equation-tests.md), $N=14$
on 5 elements resolves the shock over 4–5 solution points like $N=4$ on 15
elements; on [Sod](/benchmarks/sod-and-lax-shock-tubes.md) the $L^1$ rates
are about one for $N=2$–7 (Table 1); on the
[isentropic vortex](/benchmarks/isentropic-vortex.md) the $L^2$ rates are
3.30–8.74 for $N=2$–7, at least $N+1$, and the largest viscosity
components fall from about $10^{-7}$ to $10^{-9}$ when the mesh is halved
($N=7$; Table 2, §5.2.3); on the
[KPP rotating wave](/benchmarks/kpp-rotating-wave.md) ($N=9$),
[Shu–Osher](/benchmarks/shu-osher-problem.md), an MHD rotor and the
[Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) discontinuities are
resolved within 2–5 solution points; on Orszag–Tang the density and
magnetic-field viscosities differ visibly, which the authors read as the
benefit of a vector viscosity (Fig. 13). $c_\mu$ ranges from 1 to 8 between
problems and is kept fixed under refinement and order changes (§4.2).

**Learned modal-decay viscosity.** [Yu & Hesthaven (2022)](/sources/yu-2022.md)
(§2, §4.1, Eqs. (2.1)–(2.23), (4.3)–(4.5)) set the element viscosity
(registry §10 $\mu_e$) from the decay exponent $\mathfrak a_K$ of the
modal coefficients, estimated by a neural network (troubled-cell indicator
page):
$$\mu_e=\mu_{\max}\begin{cases}1,&\mathfrak a_K<1,\\1-\tfrac12(\mathfrak a_K-1),&1\le\mathfrak a_K\le3,\\0,&\mathfrak a_K>3,\end{cases}\qquad
\mu_{\max}=c_{\max}\frac{\mathcal H}{N}\max_{x\in K}\lvert f'(u_h)\rvert,$$
with $c_{\max}=0.5$ (page-local) and the length scale $\mathcal H=h$ if
$\mathfrak a_K<\mathfrak a_0$ or $h<\tilde{\mathcal H}$, and
$\mathcal H=\tilde{\mathcal H}=\max_e[\![u]\!]_e$, the largest jump across
the element's edges, otherwise; $\mathfrak a_0=2$ by default and 2.5 on the
forward step and the jet (page-local $\mathcal H$, $\tilde{\mathcal H}$,
$\mathfrak a_0$). The jump-based scale is meant to tell spurious
oscillations from physical fluctuations. The same viscosity acts on all
components, computed from the density for Euler, and is made continuous by
averaging it at the nodes of a quadratic Lagrange basis (Remarks 1–2). The
viscous term uses an LDG-type auxiliary gradient with central fluxes, and
the explicit step obeys
$\Delta t\sim\nu/(aN^2/h+\mu_eN^4/h^2)$, which the authors call a stringent
restriction (Eq. (2.23)). On smooth tests the viscosity acts only on the
coarsest grids, after which the errors equal those of the inviscid scheme
(Tables 2–3); shocks from Burgers to the double Mach reflection, the
forward step on unstructured triangles and the
[high-Mach jet](/benchmarks/high-mach-astrophysical-jet.md) (inflow speed
800) are captured without oscillation, but $N=2$ fails on the jet from
insufficient dissipation (§5.4.6).

**Time-evolved viscosity field (SPH-type switch).**
[Cernetic et al. (2023)](/sources/cernetic-2023.md) (§4.1, Eqs. 43–46,
accepted manuscript) carry the strength of the viscosity as an extra
field $\alpha_{\mathrm{AV}}(x,t)$ of their modal DG code
[TENET](/software/tenet.md) (page-local; not the registry's blending
$\alpha$), expanded in the DG basis and evolved, after the viscosity
switches of smoothed-particle hydrodynamics (Morris & Monaghan, Cullen &
Dehnen), by
$$\partial_t\alpha_{\mathrm{AV}}=f_v\max(0,-\nabla\cdot v)+f_w\max\Big(0,\frac{d\ln S^{\mathrm{PP}}_K}{dt}\Big)-\frac{\alpha_{\mathrm{AV}}}{\tau_{\mathrm{AV}}},\qquad
\tau_{\mathrm{AV}}=f_\tau\frac{\Delta x}{(N+1)\,c},\qquad
\mu=\alpha_{\mathrm{AV}}\,c\,\frac{\Delta x}{N+1},$$
with the second source active only while the Persson–Peraire sensor
$S^{\mathrm{PP}}_K$ exceeds an onset value $S_{\mathrm{on}}$ (page-local
$f_v$, $f_w$, $f_\tau$, $\tau_{\mathrm{AV}}$, $S_{\mathrm{on}}$; the source
writes $h$ for $\Delta x$ and $p$ for the order $N+1$). The viscosity $\mu$
diffuses all conserved variables, $\nabla\cdot(\mu\nabla u)$, and is
capped by $\alpha_{\mathrm{AV}}\le1$ to stay within the explicit diffusion
limit at the Courant-limited step. The compression source fires at
shocks; the sensor-rate source targets oscillations ahead of shocks and
at moving contacts, which it alone sees
([troubled-cell indicator](/definitions/troubled-cell-indicator.md)). The
field is deliberately not advected: it lags behind moving discontinuities,
and advecting it at high order would itself need limiting. Defaults
$f_v=2.5$, $f_\tau=0.5$, $f_w=0.2$, $S_{\mathrm{on}}=10^{-4}$ and a global
scaling 1.0 are used for every order; no slope limiter is used, only a
positivity limiter as a last line of defence
([Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md)).

The viscous term needs interface gradients. Bassi–Rebay's BR1 lifting
was implemented first and abandoned: it triples the cost of the gradient
solve in 3D, gives large in-cell derivatives for initial data with large
jumps, and "does not converge rapidly at high order either" (§3.1). In
its place the two cell polynomials adjacent to a face are
$L^2$-projected onto one polynomial of degree $N+1$ in the normal
direction on a domain straddling the face over a fraction $f$ of each
cell, $f=\tfrac34$ for $N\le2$ and 1 for $N>2$, in the manner of van Leer
and Nomura's recovery; the interface value and gradient are taken from
it (Eqs. 29–36). For piecewise-constant data and $f=\tfrac34$ the
recovered gradient is $(u^+-u^-)/\Delta x$ along the normal (Eq. 36).
The projection is a fixed sparse map, and the two sides exchange partial
sums, so the communication costs the same as an average.

Evidence (§4–§7, Figs. 3–15): a Mach 4 shock (captions; "$\mathcal M=3$"
in the text) at $\Delta x=1/21$ and the highest order shown is captured
within a fraction of a cell with negligible ringing, and the 20–80% width
of the density jump falls in proportion to $1/p$ in units of $\Delta x$
for $p\ge2$, $p$ the label of Fig. 4. On the
[isentropic vortex](/benchmarks/isentropic-vortex.md) the $L^1$ error
converges at the design order for orders 1–8 and exponentially in the
order at fixed cells; on a periodic Gaussian diffusion test the recovery
flux converges at the design order for five orders and exponentially up
to tenth order. On the [Woodward–Colella blast waves](/benchmarks/woodward-colella-blast-wave.md)
with 100 cells the degree-7 run matches the degree-1 run on 400 cells,
which has the same degrees of freedom; an eighth-order WENO on 400 cells
(Zhao et al. 2017) is closer to the reference with half the degrees of
freedom of the degree-7 run, which the authors concede; they state that
real discontinuities converge only at first order in resolution. On
top-hat advection over 100 box crossings with 64 cells the fitted growth
exponent $s$ of $L^1\propto t^s$ (page-local) falls from 0.427 (degree 0) to 0.028
(degree 9) (Fig. 10); lowering $S_{\mathrm{on}}$ to $10^{-6}$ damps the
ringing at the top-hat edges at the cost of a slightly wider front
(Fig. 9). On the viscous [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)
of Lecoanet et al. the $L^2$ dye error at 64 cells and order 4 equals
that of ATHENA at 2048 cells (§6.3, Fig. 14).

## Viscosity set by a Helmholtz equation and a homotopy (HDG, steady flows)

[Nguyen et al. (2024)](/sources/nguyen-2024.md) (§2.2–2.5, Eqs. (5)–(17),
arXiv v1) regularize steady compressible Euler and Navier–Stokes problems,
discretized by hybridizable DG with isoparametric elements of degree 4
(degree 3 for their double ramp),
with a Laplacian artificial flux whose shape solves a Helmholtz equation
(their earlier method, after Barter & Darmofal and Ching et al., as
recalled):
$$\nabla\cdot F(u,\nabla u)-\lambda_1\nabla\cdot\big(\mu_{\mathrm h}(\eta_{\mathrm h})\nabla u\big)=0,\qquad
\eta_{\mathrm h}-\lambda_2^2\nabla\cdot\big(\ell^2\nabla\eta_{\mathrm h}\big)=s_{\mathrm h}(u,\nabla u),$$
with $\ell=h_{\min}$ the smallest mesh size, $\eta_{\mathrm h}=0$ on walls,
and the source $s_{\mathrm h}$ a smooth clipping of the shock strength
$-\nabla\cdot v$ to $[0,s_{\max}]$, $s_{\max}=\tfrac12\lVert\nabla\cdot v\rVert_\infty$
from the previous iterate (page-local $F$ the physical flux, $\mu_{\mathrm h}$,
$\eta_{\mathrm h}$, $s_{\mathrm h}$, $\lambda_1$, $\lambda_2$, $\ell$; the
source's $\eta$ is not an entropy). The shape function is a smoothed ramp of
$\bar\eta_{\mathrm h}=\eta_{\mathrm h}/\lVert\eta_{\mathrm h}\rVert_\infty$ above
the threshold $0.2$ (Eq. (8)), and the Helmholtz equation is solved with
continuous Galerkin so that the viscosity field is continuous. The
amplitude $\lambda_1$ and the thickness $\lambda_2\ge1$ are not tuned by
hand: the problem is posed as
$\min\lambda_1\lambda_2$ subject to the discrete equations, $\rho>0$,
$p>0$ and a modal smoothness bound $\sigma(\lambda)\le5\,\sigma(\lambda_0)$,
with $\sigma$ the largest relative $L^1$ defect between a scalar ($\rho$,
$p$ or Mach number) and its degree-$(N-1)$ truncation over the shock
elements (Eqs. (12)–(17)). It is solved by a homotopy that shrinks both
parameters from a conservatively large start and keeps the last iterate
that still satisfies the constraints (§2.4). In this paper the
regularization is coupled to r-adaptation by optimal transport
([adaptive moving mesh](/methods/adaptive-moving-mesh.md)), and the
homotopy runs only on the final adapted mesh. The authors report that the
viscosity shrinks in amplitude and width as the mesh adapts, and that on
a Mach 7 cylinder, a type IV shock–shock interaction ($M_\infty=8.03$) and
a Mach 17.6 viscous cylinder the adapted solutions are sharp and free of
oscillation, with the peak surface pressure and the heat-transfer
coefficient closer to experiment and to the LAURA code than on the initial
mesh (§4.3–4.5; [flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)).
No error norm or convergence rate is given.

## Residual-based viscosity (continuous finite elements, MHD)

[Dao & Nazarov (2022)](/sources/dao-2022.md) stabilize an explicit
continuous Galerkin method with Lagrange $\mathbb P^N$ elements,
$N=1,2,3$, for ideal MHD, whose plain Galerkin form is equivalent to
central differencing and oscillates at shocks (§4). They reject
Galerkin-least-squares stabilization as implicit by construction and
hard to make high order in time, and keep only its viscosity (§1).

**Viscous regularization** (§4.1, Eqs. (4.3)–(4.5)). The added flux is
the resistive-MHD viscous flux (Navier–Stokes stress with dynamic and
bulk viscosity, heat conduction on $T=p/\rho$, resistivity on the
magnetic field) augmented by a mass diffusion $\nu_h\nabla\rho$ (page-local $\nu_h$, not the CFL number) in the
continuity equation, following Guermond and Popov's argument for the
Euler equations that regularizing the mass equation is what keeps
density and internal energy positive and a minimum entropy principle;
with $B=0$ and without the mass term it is the Navier–Stokes flux. The
paper proves none of these properties for MHD and lists positivity,
entropy and Galilean invariance as future work (§6). All coefficients
(mass diffusion, dynamic viscosity, heat conduction, resistivity) are
set equal to one nodal viscosity $\mu_i$; the bulk viscosity used is not
stated.

**The viscosity** (§4.2–4.3, Eqs. (4.6)–(4.10)), with $h_i$ the nodal
value of a mesh function already divided by the degree $N$ (page-local)
and $a_i$ the largest MHD eigenvalue modulus at node $i$ (registry $a$):
$$\mu_i=\min\big(\mu^{\mathrm L}_i,\mu^{\mathrm H}_i\big),\qquad
\mu^{\mathrm L}_i=C_{\max}h_ia_i,\qquad
\mu^{\mathrm H}_i=C_Rh_i^2\widetilde R_i,$$
with $C_{\max}=0.5$, $C_R=1$ (page-local), and $\widetilde R_i$ the
largest, over all conserved components, of the absolute PDE residual
(with a BDF2 time derivative, $L^2$-projected to the nodes and
mass-lumped for $\mathbb P^1$, $\mathbb P^3$) divided by the
normalization $n(q)$ defined on the
[troubled-cell indicator](/definitions/troubled-cell-indicator.md) page
($C_l=0.4$). In 1D the first-order viscosity with $C_{\max}=0.5$ gives
the [Lax–Friedrichs](/methods/lax-friedrichs-flux.md) scheme (stated);
the authors add that a positivity-preserving first-order scheme would
need a sharper wave-speed estimate than the largest eigenvalue (§4.2).
The viscosity is computed at $t^n$ and frozen over the classical RK4
stages; the time step is $0.3\min h/\max a$, with no
parabolic restriction discussed (§4.4). The residual is $O(h^{N+1})$ in
smooth regions and $O(h^{-1})$ at shocks (stated), so the high-order
viscosity vanishes at the design rate where the solution is smooth.

**Evidence** (§5). On smooth MHD vortex and wave tests the RV errors
stay close to the Galerkin errors: $\mathbb P^1$ about second order,
$\mathbb P^3$ $L^1$ rates 3.71–4.24, and $\mathbb P^2$ only second
order, which the authors attribute to a known continuous-Galerkin issue
(Tables 1–2). Brio–Wu, the [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md)
to $t=1$, its 3D extension and the MHD
rotor run without oscillations visible in the figures; the rotor's
minimum pressure is $3.86\times10^{-2}$. Positivity and invariant-domain
preservation are left out of scope (§1, §6). Divergence control is
separate ([divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)).

## Space–time smooth viscosity with C-functions (ALE finite differences)

[Ramani & Shkoller (2023)](/sources/ramani-2023.md) stabilize a
simplified finite-difference WENO scheme for the Euler equations in ALE
form with the C-method of their earlier work, carried here to moving
meshes (§6.2, Appendix A). The advective fluxes reconstruct the conserved
variables by fifth-order WENO at half-points, upwinded on the sign of
the ALE transport velocity, and multiply them by a fourth-order averaged
velocity, without characteristic decomposition or Riemann solver; the
authors call it cheaper and less robust, oscillatory on hard problems,
and in need of the C-method viscosity (Remark 1). Let $\mathsf a^j_i$
denote the cofactors of the mesh map and $\mathcal J$ its Jacobian
(page-local), $C_{\mathrm s}$ the shock C-function and $\tau_{\mathrm c}$
the smoothed contact tangent (page-local). The viscosities are

$$\mathcal D[w;b]=\partial_k\big(\tilde b\,\rho\,C_{\mathrm s}\,\mathsf a^k_i\mathsf a^l_i\,\partial_lw\big),\quad \tilde b=\frac{\lvert\Delta x\rvert^2}{\max C_{\mathrm s}}\,b,\qquad
\mathcal D_\tau[w;\mu_{\mathrm c}]=\partial_k\big(\tilde\mu_{\mathrm c}\,\rho\,\tau^i_{\mathrm c}\tau^j_{\mathrm c}\,\mathsf a^k_i\mathsf a^l_j\,\partial_lw\big)$$

with $\tilde\mu_{\mathrm c}=\lvert\Delta x\rvert^2\mu_{\mathrm c}\big/\big(\max_x\max_i\lvert\tau^i_{\mathrm c}\rvert\big)^2$
(Eqs. 61–63), isotropic for shocks and anisotropic along contacts,
applied to the velocity (with coefficient $b_v$) and to $E/\rho$ (with
$b_E$) (Eq. 65; page-local $b$, $b_v$, $b_E$, $\mu_{\mathrm c}$). The
C-functions are smooth in space and time because they solve
reaction–diffusion equations forced by the solution,
$\partial_tC_{\mathrm s}=\frac{S_{\mathrm c}}{\varepsilon_{\mathrm c}\lvert\Delta x\rvert}(\hat F-C_{\mathrm s})+\kappa_{\mathrm c}S_{\mathrm c}\lvert\Delta x\rvert\Delta C_{\mathrm s}$,
with $\hat F$ the normalized magnitude of the density gradient for the
shock function and the rotated density gradient for the contact tangent
(Eqs. 64–67; page-local $S_{\mathrm c}$, $\varepsilon_{\mathrm c}$,
$\kappa_{\mathrm c}$, whose values are not printed). The coefficients
used are $b_v=0.35$, $b_E=2.5$, $\mu_{\mathrm c}=0$ for the Noh
implosion on uniform grids and $b_v=0.1$, $b_E=0.7$ on the adaptive
grid, and $\mu_{\mathrm c}=7.5\times10^{-4}$, $b_v=b_E=0$ for
Rayleigh–Taylor (§7.1–7.2). The Noh runs show very small wall heating
and preserved radial symmetry, attributed to the viscosity together with
the alignment of the moving mesh with the shock (§7.1.3;
[Noh implosion](/benchmarks/noh-implosion-problem.md),
[adaptive moving mesh](/methods/adaptive-moving-mesh.md)).

## Spectral and quasi-spectral eddy viscosities

[Sousa & Scalo (2022)](/sources/sousa-2022.md) recall Tadmor's spectral
vanishing viscosity (SVV), which adds $\epsilon_{\mathrm{SV}}\partial_x(\mathcal K_{\mathrm{SV}}*\partial_xu)$
with a kernel acting only above an activation wavenumber $\sim k_c^{\beta_{\mathrm{SV}}}$,
$\beta_{\mathrm{SV}}<\tfrac12$, and $\epsilon_{\mathrm{SV}}\ge1/k_c$ (Eqs.
(13)–(16); page-local), and show that it is formally an LES eddy viscosity
for the filtered Burgers equation; on a forming Burgers shock an inviscid
low-wavenumber range makes it under-damp large scales and oscillate (§2.3).
Their [quasi-spectral viscosity](/methods/quasi-spectral-viscosity.md) sets
the magnitude from a filter-residual estimate of the energy at the grid
cutoff and shapes it in wavenumber with filter residuals, on a sixth-order
compact central scheme, and is compared with the local artificial
diffusivity (LAD) of Cook and Kawai–Lele, an artificial shear and bulk
viscosity and conductivity that needs an explicit filter (§5). At $M=5$,
$\gamma=1.15$, LAD oscillates and breaks symmetry where QSV does not
(§5.3).

**Spectral relaxation and spectral purging.**
[Kolluru, Besse & Pandit (2024)](/sources/kolluru-2024.md) (§2–§3, App. A,
arXiv v2) study numerically two alternatives to SVV proposed by Besse (as
recalled, submitted). For a Galerkin-truncated Fourier (or Chebyshev)
pseudospectral solution $u_N$ with truncation wavenumber $N$ (page-local;
not the registry's DG degree), spectral relaxation (SR) adds a BGK-type
term toward a mollified state,
$$\partial_tu_N+\partial_x\big(\mathcal P_N\tfrac12u_N^2\big)=\frac1{\tau_{\mathrm s}}\big(\mathcal K_m*u_N-u_N\big),\qquad m=N^{\gamma_{\mathrm s}},\quad \tau_{\mathrm s}=N^{-\alpha_{\mathrm s}},$$
which damps every Fourier mode at the rate $(1-\hat{\mathcal K}_m(k))/\tau_{\mathrm s}$,
while spectral purging (SP) replaces $u_N$ by $\mathcal K_m*u_N$ at time
intervals $\tau_{\mathrm s}$ (Eqs. (3)–(4); page-local $\mathcal P_N$ the
projection, $\mathcal K_m$ the kernel, $\alpha_{\mathrm s}$, $\gamma_{\mathrm s}$
the exponents). Besse proves $L^2$ convergence to the entropy solution of
inviscid Burgers for positive kernels (Fejér–Korovkin, Jackson,
Jackson–de La Vallée Poussin) with $\alpha_{\mathrm s}/2<\gamma_{\mathrm s}<1$
and $1<\alpha_{\mathrm s}<2$ (as recalled, §3.2). The authors state that SR
and SP get monotonicity and the maximum principle from the positivity of
the kernel, whereas SVV gets them from the structure of its Laplacian
(§1). Their findings, on Burgers' equation with $u_0=\sin2\pi x$ and on 1D
shallow-water and Euler tests:

- the positive Fejér–Korovkin kernel gives monotone, oscillation-free
  shocks with no "tygers" (resonant oscillations born in smooth regions of
  Galerkin-truncated solutions), at observed orders of about
  $2-\alpha_{\mathrm s}$ before the shock and below one after it ($L^1$
  about 0.9, $L^2$ about 0.78; Table 1, Fig. 4), while SVV with
  $\epsilon_{\mathrm{SV}}=N^{-1}$ keeps small oscillations at the shock
  (Fig. 7);
- the non-positive de La Vallée Poussin kernel converges spectrally
  before the shock but keeps bounded oscillations at it, with an $L^2$
  order of about 0.5 after the shock against 0.8 for Fejér–Korovkin
  (Table 2), which the authors read with LeVeque as "the order of
  accuracy is not everything";
- the high-order kernel is needed to keep the entropy waves of the
  [Shu–Osher problem](/benchmarks/shu-osher-problem.md), and it fails on
  the [Woodward–Colella blast waves](/benchmarks/woodward-colella-blast-wave.md)
  with negative density and pressure, where the positive kernel stays
  positive and stable but loses the post-interaction structure (§3.4).

The best parameters for $u_0=\sin2\pi x$ ($\alpha_{\mathrm s}=0.7$ for SR,
0.65 for SP) lie outside the proven range, and every parameter set beyond
Burgers was chosen by visual agreement (§3.2, §4).

## Damping of DG modes as a modal filter

The oscillation-free DG method (Lu, Liu & Shu, as recalled by
[Peng, Sun & Wu (2024)](/sources/peng-2024.md), §1, Eq. (1.2)) adds damping
terms that penalise the deviation of $u_h$ from its lower-order $L^2$
projections, similar in flavour to local projection stabilization. For
discontinuous solutions these terms are very stiff, forcing small explicit
steps or exponential Runge–Kutta integrators. [OEDG](/methods/oedg.md)
splits the damping off and solves it exactly after every stage: with
coefficients frozen at the stage solution and a Legendre basis, the damping
ODE is diagonal and each modal coefficient of degree $l\ge1$ is multiplied by
$$\exp\Big(-\frac{a_i\Delta t}{\Delta x_i}\sum_{m=0}^{l}\sigma_i^m\Big),$$
while the cell average is untouched ($a_i$ the local wave speed at the cell
average, $\sigma_i^m$ dimensionless damping coefficients built from jumps of
the $m$th derivatives; page-local) (Eqs. (2.9)–(2.12)). Higher modes are
damped more, so the damping operator is an exponential **modal filter** with
solution-dependent strength, which links oscillation-free damping to spectral
viscosity and spectral filtering (Rem. 2.3, §1.2). Conservation and the
non-increase of the elementwise $L^2$ norm follow at once (Rems. 2.2–2.3).

[Fan & Wu (2024)](/sources/fan-2024.md) (§2.2.2, Thm 1, Eqs.
(2.14)–(2.17), arXiv v1) carry the same exactly solved damping to
finite-volume [Hermite WENO](/methods/hermite-weno.md), whose unknowns are
the cell average and the first moment of each cell. After every
Runge–Kutta stage the average is kept and the first moment is multiplied
by $\exp\big(-a\frac{\Delta t}{\Delta x}\hat\sigma_i\big)$, with $a$ the
global Lax–Friedrichs speed and $\hat\sigma_i$ the sum of the jumps of the
value and of $\Delta x$ times the first derivative of a linear sixth-order
Hermite reconstruction at the two faces, divided by the global range
$\max_i\lvert\bar u_i-u_\Omega\rvert$, $u_\Omega$ the mean of the cell
averages (page-local $\hat\sigma_i$, $u_\Omega$). The jumps are explicit
linear combinations of the moments of four cells, so the step costs one
multiplication per moment. The authors contrast it with limiting the
moments, which keeps at most fifth order for sixth-order Hermite WENO, and
with adding stiff damping terms to the moment equations, which needs
problem-dependent parameters and exponential Runge–Kutta (§1); they prove
that the step keeps order $k+1$ under $a\Delta t/\Delta x\le C_{\mathrm{cfl}}<1$
(Thm 2) and that it commutes with $u\mapsto\lambda u+c$ (Thm 4;
[scale invariance](/properties/scale-invariance.md)). The approximate
dispersion relation with and without the step is "nearly identical"
(Fig. 2.1).

The same exponential modal filter, with a strength chosen per element as
the smallest one that makes the nodal values positive and above a local
entropy bound, is [entropy filtering](/methods/entropy-filtering.md)
([Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md), §3), which its
authors count, with artificial viscosity, limiting and stencil
modification, among the four classes of shock capturing for discontinuous
spectral element methods (§1).

## Solution filtering read as dissipation

[Edoh (2022)](/sources/edoh-2022.md) (App. B, Eqs. (B.1)–(B.5)) stabilizes
kinetic-energy-preserving central schemes with a temporally consistent
implicit tangent filter of the conservative variables (Eq. (29)), and
analyses it in the semi-discrete limit as an artificial dissipation
$\partial_tu=\mathcal L(u)+\mathcal D_{\mathrm f}u$ with a conservative operator
$\mathcal D_{\mathrm f}\le0$ of even-order differences (page-local; periodic
grid). Filtering the total energy then tends to decrease the global
entropy, filtering the momentum to increase it, and filtering the mass is
indefinite (derived under these assumptions). Momentum-only filtering, which
Edoh calls entropy-stability promoting, gives strict kinetic-energy decay and
entropy growth for all splittings tested, and on the
[isentropic vortex](/benchmarks/isentropic-vortex.md) after 100 vortex
widths minimum densities 0.5677 (divergence form), 0.6663 (Feiereisen),
0.6671 (Kennedy–Gruber) and 0.6981 (Div-rot) against the exact 0.5479
(Figs. B.5–B.6; [split convective forms](/methods/split-convective-forms.md)).

## Limiters read as artificial viscosity

[Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) state that the
non-oscillatory limiter of the first moment in their hybrid Hermite WENO
scheme "simply induces artificial viscosity": at $\mathrm{Re}=1000$ fewer
cells are flagged than at $\mathrm{Re}=\infty$, and the discontinuities are
slightly sharper (Ex. 4.2, §5). The evidence is a qualitative comparison of
the same scheme at two Reynolds numbers. [Fu (2023)](/sources/fu-2023.md)
lists, among hybrid uses of the TENO discontinuity indicator, an adaptive
artificial viscosity for a quintic-spline scheme (§3.4, ref. [183] there);
the review gives no formula.

[Fan, Zhang & Qiu (2022)](/sources/fan-2022.md) frame their
positivity-preserving flux splitting and scaling limiter for
finite-difference WENO as possible sources of artificial viscosity: the
splitting coefficient includes viscous stress and heat flux and the
splitting is nonlinear, so "its artificial-viscosity properties are less
understood" than those of Lax–Friedrichs splitting (§1.3, §3). On a
Mach 10 reflection–diffraction problem they conclude, from contour plots,
that the flux and limiter "do not induce excessive numerical viscosity"
(Ex. 5.8; see [positivity-preserving Navier–Stokes fluxes](/methods/positivity-preserving-navier-stokes-flux.md)).

## Positions against artificial viscosity

- [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) (§1) reject
  artificial-viscosity shock capturing for DG (Persson–Peraire and later
  variants, as recalled) in hyperbolic problems: it lowers performance,
  needs non-physical boundary conditions for the added viscous terms, and
  at strong shocks may need enough viscosity to cut the explicit time step
  significantly. They blend with subcell finite volumes instead
  ([subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md)),
  and note that an earlier entropy-stable DG computation of the Io–plasma
  interaction needed artificial dissipation, which their hybrid scheme does
  without (§6.4).
- [Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md) fit
  discontinuities with the moving mesh and need neither artificial
  viscosity nor limiters nor WENO reconstruction (§I;
  [implicit shock tracking](/methods/implicit-shock-tracking.md)).
  [Huang & Zahr (2022)](/sources/huang-2022.md) give a direct comparison
  on a quasi-1D nozzle: their tracking method at degree 2 on 12 elements
  is "indistinguishable from the exact solution", while the
  Persson–Peraire artificial viscosity needs 50 elements at degree 4 for
  a similar, smeared solution, and converges at a sub-first-order rate
  under refinement, which they attribute to the smoothing of the
  discontinuity and its downstream corruption (§6.3, Table 3, Figs.
  24–26).
- [Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) recall the
  von Neumann–Richtmyer, Persson–Peraire and data-driven (Zeifang & Beck)
  viscosities among DG shock-capturing options and use finite-volume
  subcells instead (§1;
  [subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md)).
- [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) list
  artificial viscosity, with relaxation and implicit methods, as a way to
  turn a semi-discretely entropy-conservative or entropy-dissipative scheme
  into a fully discrete one (Rem. 2.2); they obtain it instead with
  [entropy correction terms](/methods/entropy-correction-term.md) applied to
  the space–time residual.
- [Yu & Hesthaven (2022)](/sources/yu-2022.md) accept the time-step cost
  that Rueda-Ramírez et al. (2021) object to and leave implicit time stepping to
  future work (§2.3); Dzanic, Trojak & Witherden cap the viscosity for the
  same reason (§4.2).
- [Cernetic et al. (2023)](/sources/cernetic-2023.md) take the opposite
  line to Rueda-Ramírez et al. (2021) for astrophysical DG: slope limiters that
  discard high-order coefficients "defeat" high-order DG in problems with
  many shocks, including the limiters of their own predecessor codes, and
  the problem of shocks in high-order DG "still awaits a compelling and
  reasonably simple solution" (§1, §4.1); they also reject
  threshold-triggered viscosity, since the oscillations must already
  exist before it acts (§4.1).
- [Nguyen et al. (2024)](/sources/nguyen-2024.md) choose artificial
  viscosity because limiters "pose implementation difficulties for
  implicit time integration schemes and high-order methods on complex
  geometries" (§1), the reverse of Rueda-Ramírez et al.'s ranking; the
  claim is stated, not measured.
- [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) take the
  opposite line for turbulent flows: a high-order dissipation applied
  everywhere serves as the subgrid regularization of an implicit LES, and
  the low-order part is confined by the sensor (§3, §5).

## Qualifications

- **Printed slips in Sciacovelli et al. (arXiv v1).** The text defines
  $k_\varepsilon=a_0/a_P$, but Eqs. (33)–(35) print the factors
  $\tfrac15$, $\tfrac3{70}$, $\tfrac1{105}$, which equal $\lvert a_P/a_0\rvert$
  *(compiler check, not in the sources: $\tfrac{1/30}{1/6}=\tfrac15$, $\tfrac{1/140}{1/6}=\tfrac3{70}$, $\tfrac{1/630}{1/6}=\tfrac1{105}$)*;
  the equations, not the sentence, are what the scheme uses. Eq. (23)
  prints the dissipation with $-\frac{a_P}{2}$, while the explicit members
  (25)–(28) carry the sign of $+\frac{a_P}{2}$ (e.g. $+\frac1{12}$ for
  $a_0=\frac16$); the page follows the explicit members. The variable
  $\tilde w$ of Eqs. (23)–(29) is not defined.
- Kuzmin & Vedral analyse only the steady linear advection–reaction problem;
  the observed $L^1$ rate on uniform meshes is $N+1$, against the "optimal"
  $N+1/2$ of the general-mesh estimate (§6–§7).
- In their solid-body-rotation test the high-order-only stabilization has a
  smaller $L^1$ error than the blended method (e.g. $1.47\times10^{-2}$
  against $2.68\times10^{-2}$ for $N=1$) but large overshoots; "superior" in
  the paper means bounded and non-oscillatory, not more accurate (§7.3).
- The dissipation-based schemes do not by themselves guarantee bounds;
  Kuzmin & Vedral suggest algebraic flux correction on top when strict
  bounds are required (§7.4; [convex limiting](/methods/convex-limiting.md)).
  Sciacovelli et al. prove no stability or accuracy theorem; their
  evidence is numerical.

- **Cernetic et al.'s parameters and labels.** §4.1 gives "$f_v\sim1.0$"
  and an onset $10^{-4}/p^2$ in the text, but defaults $f_v=2.5$ and
  $10^{-4}$; the global viscous-flux scaling factor is also called
  $\alpha$. The paper defines $p=n+1$ as the order (§2.3) but most
  figures, Table 1 and §5.3 label curves by the degree ("order of the
  method is $p+1$"); the memory formula of Table 1 holds only with $p$
  the degree (accepted manuscript). Their claim that sub-cell shock
  capturing in DG had been "a nagging problem for decades" (§4.1) stands
  next to their own citation of Persson & Peraire's "Sub-Cell Shock
  Capturing for Discontinuous Galerkin Methods".
- **Cernetic et al.'s recovery coefficients.** As printed, Eq. (35) has
  the prefactor $1/(2f)$; with $|K^\star|=2f\Delta x$ the projection gives
  $\tfrac12$, which reproduces their Eq. (36), while $1/(2f)$ would give
  $\tfrac43(u^+-u^-)/\Delta x$ for $f=\tfrac34$. Their sum stops at
  $m_x=l_x$, exact for $f=1$ but not for $f=\tfrac34$ (e.g.
  $\int_{-1}^0\sqrt3(\tfrac32x+1)\,dx=\sqrt3/4\ne0$); and the right-cell
  overlap integral is printed with the argument of the left cell,
  $2fx+1$ instead of $2fx-1$ *(compiler check, not in the sources)*.
  Their viscous stress (Eq. 39) is printed with $+\tfrac23\nabla\cdot v$
  and no identity tensor; with the identity understood its trace is
  $4\nu\rho\nabla\cdot v$ ($\nu$ the source's kinematic viscosity), so it is
  not the trace-free shear stress the text describes *(compiler check, not
  in the sources)*.
- **Tuning.** Dzanic, Trojak & Witherden present TR viscosity as having one
  parameter and being independent of mesh and order (Abstract, §6), yet
  tune $c_\mu$ per problem between 1 and 8 and keep a second constant
  $c_{\max}$ whose influence is checked only in 1D (§4.2, §5). Their
  normalization by the global range of each component makes the viscosity
  at a weak shock depend on a strong jump elsewhere in the domain
  *(compiler check, not in the sources: $\Delta_\Omega u^n$ in Eq. (6) is
  a domain-wide range)*. Yu & Hesthaven tune
  $\mathfrak a_0$ and the edge rule for the forward step and the jet.
- In Yu & Hesthaven's switch (4.5) the length scale is either $h$, a length,
  or $\tilde{\mathcal H}$, a jump of the solution, and the comparison
  $h<\tilde{\mathcal H}$ is dimensionally consistent only for
  non-dimensional variables *(compiler check, not in the sources: units of
  the two branches of Eq. (4.5))*.
- **Nguyen et al.'s printings (arXiv v1).** The shape function (8) is said
  to vanish below the threshold, but at the threshold it equals
  $\tfrac12-\arctan(100)/\pi\approx3.2\times10^{-3}$ and at
  $\bar\eta_{\mathrm h}=0$ about $2.5\times10^{-6}$ *(compiler check, not in
  the sources)*. The homotopy update
  $\lambda_{n,1}=\zeta^{n-1}\lambda_{n-1,1}$ ($\zeta\in(0,1)$, page-local)
  makes no reduction at $n=1$ and a cumulative factor $\zeta^{n(n-1)/2}$
  *(compiler check, not in the sources)*; $\zeta$ and the starting
  $\lambda_{0,1}$ are not printed. The statement that the amount of
  viscosity is "proportional to $\lambda_1\lambda_2$" is not derived.
- **Fan & Wu's damping is normalized globally.** The denominator
  $\max_i\lvert\bar u_i-u_\Omega\rvert$ is a domain-wide range, so the
  damping of a cell depends on data far from it, as for Dzanic, Trojak &
  Witherden's normalization above *(compiler check, not in the sources)*;
  the authors call the update local and non-intrusive (Remark 3).
- Kolluru et al. state the observed order $2\gamma_{\mathrm s}-\alpha_{\mathrm s}$
  from the scaling of the relaxation term, a heuristic that the authors
  support with their Fig. 4, not derived (§3.1).
- Dzanic, Trojak & Witherden's first-order analysis of Burgers prints the
  $\zeta^2$ term of Eqs. (27) and (29) with the wrong sign and drops factors
  of two inside Eq. (29); the limit (30) is unaffected *(compiler check,
  not in the sources: with $k=\Delta t/(2\Delta x)$ the defect is
  $k\lvert\zeta-2ku^+\zeta-k^2\zeta^2\rvert$, $\zeta=(u^-)^2-(u^+)^2$)*.

# Citations

- [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) — arXiv v1: §1; §3 (Eqs. (20)–(35), Fig. 1); §4.1; §5.2 (Fig. 11).
- [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) — arXiv v1: §3 (Eqs. (4)–(8)); Rem. 2; §6 (Eqs. (16)–(18), Rem. 6); §7.3–§7.4; §8.
- [Pazner (2021)](/sources/pazner-2021.md) — arXiv v1: §3.1 (Eqs. (32)–(35)); §3.4 (Fig. 1); §4.4.
- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) — arXiv v1: §1, §1.2 (Eq. (1.2)); §2.2 (Eqs. (2.9)–(2.12)); Rems. 2.2–2.3.
- [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) — Ex. 4.2; §5 (first-moment limiter read as artificial viscosity).
- [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) — arXiv v1: §1; §6.4.
- [Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md) — author manuscript: §I.
- [Fu (2023)](/sources/fu-2023.md) — §3.4 (adaptive artificial viscosity among hybrid TENO uses, named only).
- [Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) — arXiv v2: Abstract; §2 (Eqs. (2)–(7)); §3 (Eqs. (8)–(30)); §4 (Eqs. (31)–(40)); §5 (Tables 1–2, Figs. 1–14); §6.
- [Yu & Hesthaven (2022)](/sources/yu-2022.md) — §2 (Eqs. (2.1)–(2.23)); §4.1 (Eqs. (4.3)–(4.5), Remarks 1–2); §5 (Tables 2–3, §5.4.6).
- [Sousa & Scalo (2022)](/sources/sousa-2022.md) — arXiv v2: §2.2–§2.3 (Eqs. (13)–(16), Fig. 1); §5 (LAD comparison, Figs. 4–11).
- [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) — arXiv v3: §1; §3 (entropy filtering).
- [Edoh (2022)](/sources/edoh-2022.md) — §4 (Eq. (29)); App. B (Eqs. (B.1)–(B.5), Figs. B.5–B.6).
- [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) — arXiv v4: Rem. 2.2.
- [Dao & Nazarov (2022)](/sources/dao-2022.md) — arXiv v1: §1; §4.1–4.4, Eqs. (4.3)–(4.12); §5, Tables 1–2, Figs. 2–7; §6.
- [Fan, Zhang & Qiu (2022)](/sources/fan-2022.md) — §1.3; §3; Ex. 5.8.
- [Huang & Zahr (2022)](/sources/huang-2022.md) — arXiv v2: §6.3, Table 3, Figs. 24–26.
- [Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) — §1.
- [Ramani & Shkoller (2023)](/sources/ramani-2023.md) — arXiv v2: §6.2, Eqs. (47)–(51), Remark 1; Appendix A, Eqs. (60)–(67); §7.1–7.2.
- [Lin, Chan & Tomas (2023)](/sources/lin-2023.md) — arXiv v2: §5, Eqs. (16)–(18) (graph viscosity for Navier–Stokes).
- [Cernetic et al. (2023)](/sources/cernetic-2023.md) — accepted manuscript: §1; §2.3; §3.1–3.2, Eqs. (24)–(36); §4.1, Eqs. (41)–(46), Figs. 3–4; §5.1–5.4, Figs. 5–10; §6.3, Fig. 14.
- [Nguyen et al. (2024)](/sources/nguyen-2024.md) — arXiv v1: §1; §2.2–2.5, Eqs. (5)–(17); §4.3–4.5; §5.
- [Kolluru, Besse & Pandit (2024)](/sources/kolluru-2024.md) — arXiv v2: §1; §2.2–2.3, Eqs. (3)–(4); §3.1–3.4, Tables 1–2, Figs. 4, 7, 16–17; §4; App. A.3.
- [Fan & Wu (2024)](/sources/fan-2024.md) — arXiv v1: §1; §2.2.2, Eqs. (2.14)–(2.17), Thms 1–2, Remarks 2–3; §2.2.4, Thm 4; §2.2.6, Fig. 2.1.
