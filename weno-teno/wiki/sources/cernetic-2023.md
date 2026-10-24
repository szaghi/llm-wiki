---
type: Source
title: "Cernetic et al. (2023) — High-order discontinuous Galerkin hydrodynamics with sub-cell shock capturing on GPUs"
description: "TENET-GPU, a modal DG code for the compressible Euler and Navier–Stokes equations on Cartesian meshes in C++/CUDA, with viscous interface fluxes by local L2 recovery and limiter-free shock capturing by a time-evolved, SPH-style artificial-viscosity field; shock widths scale as h/p and GPU nodes run about 8 times faster than CPU nodes."
resource: "doi:10.1093/mnras/stad1043"
source_kind: paper
authors: [Cernetic M., Springel V., Guillet T., Pakmor R.]
year: 2023
venue: "Mon. Not. R. Astron. Soc. 522:982-1008"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Monthly_Notices_of_the_Royal_Astronomical_Society_Cernetic_High-order_discontinuous_Galerkin_hydrodynamics_with_sub-cel.pdf"
tags: [dg, artificial-viscosity, gpu, software, turbulence, troubled-cell]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

The paper presents the GPU version of [TENET](/software/tenet.md), a
[discontinuous Galerkin](/methods/discontinuous-galerkin.md) code for the
compressible Euler and Navier–Stokes equations on uniform Cartesian meshes. It
is written from scratch in MPI-parallel C++/CUDA. The basis is modal:
orthonormal tensor-product Legendre polynomials truncated at total degree $N$,
with order $N+1$, Gauss quadrature with $N+1$ points per direction, a simplified
HLLC interface flux and SSP Runge–Kutta stepping up to five stages and fourth
order. There are two methodological contributions. Viscous interface fluxes
come from a local recovery: the two cell polynomials next to a face are
$L^2$-projected onto one polynomial of degree $N+1$ on a box that straddles the
face, in the manner of van Leer & Nomura. This replaces BR1 lifting, which the
authors found costly and not robust. Shocks are captured without slope limiting
by [artificial viscosity](/methods/artificial-viscosity.md) driven by a
dimensionless field $\alpha_{\mathrm{AV}}$, carried as an extra DG field and
evolved by a source–sink equation modelled on SPH viscosity switches. Its
sources are a compression term and a "wiggles" term, the growth rate of the
Persson–Peraire modal sensor ([troubled-cell indicators](/definitions/troubled-cell-indicator.md)),
balanced by decay on the time $f_\tau\Delta x/((N+1)c)$. A positivity limiter at all volume
and surface quadrature points is kept only as a last line of defence.

The evidence is numerical. Shocks are captured inside one cell, with a width
proportional to $\Delta x/(N+1)$. The [isentropic vortex](/benchmarks/isentropic-vortex.md)
and a Gaussian diffusion test converge at design order in $\Delta x$ and
exponentially in $N$. In the [Woodward–Colella blast waves](/benchmarks/woodward-colella-blast-wave.md),
equal degrees of freedom give equal quality, and an eighth-order WENO is more
accurate per degree of freedom. Top-hat advection
([material-interface advection tests](/benchmarks/material-interface-advection.md))
shows error growth slowing with order. On the viscous
[Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md) test of Lecoanet
et al., 64 cells at order 4 match ATHENA at 2048 cells. In driven subsonic
turbulence, physical viscosity is needed for a resolution-independent
bottleneck, and higher order beats more cells. On A100 GPUs, a node runs
about 8 times faster than a CPU node, and one GPU about 80 times faster than
one CPU core.

# Version read

arXiv 2208.11131v2 [astro-ph.IM], 4 May 2023, in MNRAS preprint style
("Accepted 2023 April 04. Received 2023 April 01; in original form 2022 August
23"): the accepted manuscript, paginated 1–27, not the typeset version of
record (pp. 982–1008). It has 27 pages. Title and authors match page 1 (the
preprint capitalises "Discontinuous Galerkin"). Section, equation, figure and
table numbers are those of this version.

# Key claims

Registry notation: $N$ is the DG polynomial degree, so the source's order $p$
is $N+1$. $u=(\rho,\rho v,E)$ are the conserved variables, $e$ the specific
internal energy, $c$ the sound speed. $\Delta x$ is the cell edge length (the source's $h$).
$\alpha_{\mathrm{AV}}$, $\tau_{\mathrm{AV}}$ and $S^{\mathrm{PP}}_K$ are the
artificial-viscosity field, its decay time and the Persson–Peraire sensor,
and $\mu$ is the viscosity, as on the
[artificial-viscosity](/methods/artificial-viscosity.md) page (page-local,
see the notation map).

1. DG reaches arbitrarily high order without enlarging the coupling stencil, since cells interact only through face fluxes, whereas high-order finite-volume reconstruction needs ever deeper stencils (§1). **Stated**
2. The basis is orthonormal tensor-product Legendre polynomials truncated at total degree $N$, with $(N+1)(N+2)(N+3)/6$ functions per cell in 3D, $(N+1)(N+2)/2$ in 2D and $N+1$ in 1D (§2.3, Eqs. 17–18). **Stated**
3. Gauss quadrature uses $N+1$ points per direction, more than the $(N+1)/2$ needed for polynomial integrands, because the flux integrands are rational functions of the state (§2.4). **Stated**
4. The time step is $\Delta t_{\max}=f_{\mathrm{CFL}}\Delta x/[2(N+1)(c_{\max}+\lvert v\rvert_{\max})]$, with $f_{\mathrm{CFL}}=0.5$ (0.3 for "the shock tube, Sedov blast wave and double blast wave"); with at most a five-stage fourth-order SSP Runge–Kutta method, no time-error dominance was seen for $N+1>4$, which the authors attribute to the low Courant factor (§2.5, Eq. 23). **Shown**
5. BR1 lifting (Bassi & Rebay 1997) was implemented first and abandoned: it triples the work for the auxiliary gradient in 3D, has robustness problems when the initial data have large jumps, and "does not converge rapidly at high order either" (§3.1). **Stated**
6. Interface gradients for the viscous flux come from an $L^2$ projection of the two cell polynomials onto one polynomial of degree $N+1$ in the normal direction, on a box $K^\star$ covering a fraction $f$ of each cell; the projection is a precomputable sparse linear map, and exchanging left and right partial sums makes communication cost the same as averaging (§3.2, Eqs. 29–35). **Derived**
7. With $f=3/4$ and piecewise-constant states the recovered gradient is $(u^+-u^-)n/\Delta x$ (Eq. 36); $f=3/4$ gives the expected diffusion orders for $N\le2$, and $f=1$ is needed for $N>2$ (§3.2). **Derived** (Eq. 36); **Shown** (orders)
8. A Gaussian dye-pulse diffusion test converges as $L_1\propto N_x^{-(N+1)}$ for the first five orders, and exponentially in order at 8 cells up to tenth order (§5.2, Fig. 6). **Shown**
9. Slope limiters that discard high-order coefficients defeat high-order DG in problems with many shocks; shocks in high-order DG "still await a compelling and reasonably simple solution" (§1, §4.1). **Stated**
10. The Persson–Peraire sensor $S^{\mathrm{PP}}_K$ is evaluated on the density. Persson & Peraire predict $S^{\mathrm{PP}}_K\sim1/(N+1)^4$ in oscillatory cells, but the authors measure approximately $S^{\mathrm{PP}}_K\sim1/(N+1)^2$ in troubled cells (§4.1, Eqs. 41–42). **Shown** (as a reported measurement; no figure)
11. Viscosity is triggered by a physical compression sensor rather than by an oscillation threshold, because with the latter "some damage must have already happened before the fix is applied" (§4.1). **Stated**
12. The field obeys $\partial_t\alpha_{\mathrm{AV}}=f_v\max(0,-\nabla\cdot v)+f_w\max\big(0,\tfrac{d\ln S^{\mathrm{PP}}_K}{dt}\big)-\alpha_{\mathrm{AV}}/\tau_{\mathrm{AV}}$, the wiggle term acting only for $S^{\mathrm{PP}}_K>S_{\mathrm{on}}$, with $\tau_{\mathrm{AV}}=f_\tau\Delta x/((N+1)c)$; it is expanded in the DG basis and deliberately **not advected**, so it lags behind moving discontinuities (§4.1, Eqs. 43–45). **Stated**
13. The applied viscosity is $\mu=\alpha_{\mathrm{AV}}c\,\Delta x/(N+1)$, acting as Laplacian diffusion of all conserved variables, with the cap $\alpha_{\mathrm{AV}}\le1$ keeping the explicit diffusion within the von Neumann limit for the Courant-limited step (§4.1, Eq. 46). **Stated**
14. A shock at $\Delta x=1/21$, $\gamma=5/3$, labelled $p=9$, is captured within a fraction of a cell with negligible ringing (Fig. 3); the 20 %–80 % shock width scales as $\Delta x/p$ for $p\ge2$, and $p=1$ is broader (Fig. 4; source labels $p$, whose reading as order or degree is ambiguous, see Printed slips). The authors call reliable sub-cell shock capturing in DG "a nagging problem for decades", now solved (§4.1). **Shown**
15. The default parameters $f_v=2.5$, $f_\tau=0.5$, $f_w=0.2$, $S_{\mathrm{on}}=10^{-4}$ and a global viscous-flux factor 1 do not depend on the order (§4.1, §5.3). **Stated**
16. Positivity limiter: with $\rho_{\mathrm{bot}}=10^{-6}\bar\rho$, all higher-order coefficients of all fields are scaled by $(\bar\rho-\rho_{\mathrm{bot}})/(\bar\rho-\rho_{\min})$, $\rho_{\min}$ taken over volume and surface quadrature points; for pressure a factor 0.5 is applied repeatedly until the floor holds. It never triggers on smooth problems and acts only in the first steps of discontinuous initial data (§4.2, Eq. 47). **Shown** (as reported usage)
17. Isentropic vortex ($[-5,5]^2$, strength 5, $\gamma=1.4$, $t=10$): $L_1\propto N_x^{-(N+1)}$ for $N+1=1,\dots,8$, with fitted orders slightly above design except at first order; the error falls exponentially in $N$ at fixed $N_x$, down to a floor of $\sim10^{-11}$ set by the periodic box edge (§5.1, Fig. 5). **Shown** (the printed profiles, with specific internal energy $1-\frac{25}{8\gamma\pi^2}e^{1-r^2}$, are an exact steady solution whose ambient density is $(\gamma-1)^{1/(\gamma-1)}\approx0.10$, not 1 *(compiler check, not in the sources)*)
18. Woodward–Colella blast waves with 100 cells: the profile improves with order at fixed cell count, and the degree-7, 100-cell run matches the degree-1, 400-cell run of equal degrees of freedom; Krivodonova's moment limiter is "marginally better" at low order; an eighth-order WENO with 400 cells (Zhao et al. 2017) is closer to the reference with half the degrees of freedom of the degree-7, 100-cell run (§5.3, Figs. 7–8). **Shown**
19. Real discontinuities converge only at first order, and high-order DG gives no "magic solution" for them: shocks are as accurate as with a second-order method at equal degrees of freedom (§5.3). **Stated** (interpretation of Figs. 7–8)
20. Top-hat advection (64 cells, 100 box crossings): $L_1\propto t^{s}$ with fitted slopes $s=0.427,0.335,0.172,0.056,0.054,0.049,0.048,0.046,0.039,0.028$ for degrees $N=0,\dots,9$; degree 0 loses the profile after about 10 crossings (§5.4, Fig. 10). **Shown**
21. Lowering $S_{\mathrm{on}}$ to $10^{-6}$ damps the ringing at the top-hat discontinuities at the cost of a slightly wider front (§5.4, Fig. 9). **Shown**
22. Viscous Kelvin–Helmholtz (Lecoanet et al. 2016, $\mathrm{Re}=10^5$, no density jump): the dye entropy agrees with the DEDALUS reference already at 64 cells and order 4 (256 degrees of freedom per dimension); under-resolved mesh runs over-mix, against the under-mixing of Tricco's (2019) SPH (§6.2, Fig. 13). **Shown**
23. The $L_2$ dye error at 64 cells and order 4 equals ATHENA with 2048 cells, and SPH at 2048 particles per dimension is "orders of magnitude" worse; the error at $t=4$ falls exponentially in order, and among equal-degree-of-freedom runs (64 cells order 8, 128 order 4, 256 order 2) the highest order has the lowest error (§6.3, Figs. 14–15). **Shown**
24. Inviscid driven turbulence shows a bottleneck bump whose shape is set by the numerics; more cells or higher order only shift it to smaller scales (§7.2.1, Fig. 18). **Shown**
25. With physical viscosity the bump becomes resolution-independent (a DNS). At equal degrees of freedom $64^3$ cells at order 4 reproduce the converged $128^3$ order-3 spectrum while $128^3$ at order 2 does not; on 16 A100s the wall-clock times are 0.9 h ($128^3$, order 2), 3.9 h ($128^3$, order 3) and 1.8 h ($64^3$, order 4), "about 2x faster" at high order for the same converged result (§7.2.2, Fig. 19). **Shown**
26. Memory: $(3+d+f_t)N_x^dn_{\mathrm b}$ doubles, with $n_{\mathrm b}$ the basis size and $f_t$ the Runge–Kutta storage factor; one 40 GB A100 holds $128^3$ cells at degree 9 (37.81 GB), and a $2048^3$ run at degree 1 needs at least 52 such GPUs (§8.3, Eq. 62, Table 1). **Derived** (Table 1 follows from Eq. 62 when its $p$ is the degree: $8\cdot128^3\cdot4\cdot8$ B = 512 MiB at degree 1, $11\cdot128^3\cdot220\cdot8$ B = 37.81 GiB at degree 9 *(compiler check, not in the sources)*)
27. Weak scaling from 1 to 64 A100 GPUs ($128^3\to512^3$, degrees 0–5) is good, with losses at large sizes from the slab decomposition and inter-node communication; it improves at higher order (§9.1, Fig. 20). **Shown**
28. Strong scaling at $256^3$ (1–16 A100s; 1–256 Xeon-6138 cores): the CPU runs degrade from 16 to 32 cores because one 20-core socket saturates its memory bandwidth (checked with STREAM) and because one-cell-wide slabs communicate heavily (§9.2, Fig. 21). **Shown**
29. The node-level GPU speedup (4 A100s against 40 Xeon-6138 cores) peaks at "just over 8x", and one GPU is about 80 times one CPU core, close to the ratio of nominal double-precision peak performances (§9.3, Fig. 22). **Shown**
30. The GPU code is "the first" astrophysical GPU code that can carry out DG calculations of the full Navier–Stokes equations at order 10 and beyond (§10). **Stated**
31. Results are binary-identical under changes of the slab count, by fixing the summation order of left and right fluxes at the periodic wrap-around; races are avoided without locks by red–black checkerboard processing (§8.2). **Stated**

# Printed slips

- Order and degree are mixed. §2.3 defines "$p=n+1$ … the order of our DG scheme", but §5.3 says "Recall that the order of the method is $p+1$", and Figs. 6, 7, 9, 10, 13, 15, 18, 20 and Table 1 label curves by degree. The text says "order $p=2$, $p=4$, or $p=8$", against $p=1,3,7$ in Fig. 7. Fig. 11 has "order $p=5$" against "Expansion order $p=6$" in the text for the same run, Fig. 14 "orders $p=1$ to $p=4$" against "$p=2$ to $p=5$", and Fig. 13 "64 cells and $p=3$" against "64 cells and order $p=4$". §8.3 has "quadratic order $p=1$".
- The text's shock is "$\mathcal M=3$" (p. 9), the Fig. 3 and Fig. 4 captions say $\mathcal M=4$; the caption's "orange line" is the text's "red line".
- §4.1 gives "$f_v\sim1.0$" and an onset "$10^{-4}/p^2$", against the stated defaults $f_v=2.5$ and $S_{\mathrm{on}}=10^{-4}$; the global viscous-flux factor is also named $\alpha$.
- Eq. (42): the numerator sum starts at $l=N_{p-1}$, which includes a coefficient that Eq. (41) keeps in $\hat u$; it should start at $N_{p-1}+1$.
- Eq. (9) carries $\delta_{l,k}$ for indices $l,m$; Eq. (17) text has "orders $l_{z,y,z}$".
- Eq. (20) prints the prefactors $1/4$ (volume) and $1/8$ (surface), explained as $1/\lvert K\rvert$ after the change of variables of Eq. (15). With $\lvert K\rvert=\Delta x^3$, volume element $(\Delta x/2)^3$, surface element $(\Delta x/2)^2$ and the factor $2/\Delta x$ of the gradient, both terms carry $1/(4\Delta x)$ for Gauss weights on $[-1,1]$, and $\Delta x$ is absent from Eq. (20) *(compiler check, not in the sources)*.
- Eq. (35) prints the prefactor $1/(2f)$. From Eq. (32) with $\lvert K^\star\rvert=2f\Delta x$ in the normal direction and $dx=f\Delta x\,dx^\star$, the prefactor is $1/2$; only $1/2$ reproduces Eq. (36) at $f=3/4$ and $N=0$, where $1/(2f)$ gives $\tfrac43(u^+-u^-)/\Delta x$ *(compiler check, not in the sources)*. The sum stops at $m_x=l_x$, which is exact for $f=1$ but drops nonzero terms for $f=3/4$, e.g. $A^-_{1,0}=\sqrt3/4$. Eq. (34) gives $A^+$ the argument $P_m(2fx+1)$ of $A^-$, where the right cell's local coordinate is $2fx-1$ *(compiler check, not in the sources)*.
- Eq. (39) prints $\Pi=\nu\rho\big(\nabla v+\nabla v^{\mathrm T}+\tfrac23\nabla\cdot v\big)$, with no identity tensor and a plus sign. With the identity understood, its trace is $4\nu\rho\nabla\cdot v$, so it is not the trace-free shear stress the text describes; that needs $-\tfrac23(\nabla\cdot v)\mathbb I$ *(compiler check, not in the sources)*.
- Eq. (40) prints the right side $\nabla(\eta\rho\nabla c)$ without the divergence; Eq. (4) prints the energy flux $(\rho e+p)v$, while Eq. (2) defines $e$ as the total energy density, so $(e+p)v$ is meant.
- §2.5: "scaling the time-step size as $h^{r/4}$" (source $h$), with $r$ undefined; the $f_{\mathrm{CFL}}=0.3$ remark names shock-tube and Sedov tests that the paper does not show.
- §6.3 gives the ATHENA comparison "at a resolution of 1024 cells", then "as good as ATHENA with 2048 cells"; Fig. 14 says 2048.
- The DEDALUS reference resolution is printed "3096 × 6144" (§6.1, §6.3, Fig. 12) for a $1\times2$ domain, whose aspect ratio gives 3072 for 6144 *(compiler check, not in the sources)*.
- §5.4 says Fig. 9 shows the profile "at $t=1.0$ when 10 cells per dimension are used, for different DG expansion orders"; the caption has 64 cells at $t=1.0$ for the orders and 10 cells at $t=0.01$ for degree 9 only.
- Fig. 19 caption: "$128^2|p=3$" for $128^3$. §9.3: "the speedup … is modest for order $p=2$ … At $p=2,3$ we reach the highest node-level speedup". Fig. 20 caption mentions "$N_c=400$", not among the listed sizes.
- Typos: "Discontinuois", "conversation of mass", "oscillatory senor", "bottlenect", "intertial", "Ahmdahl's law", "string discontinuities".

# Notation map

| Cernetic et al. (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $n$ | $N$ | polynomial degree |
| $p=n+1$ | $N+1$ | order; **often used for the degree in figures and §§5–9** |
| $N$, $N^{dD}(n)$ | $n_{\mathrm b}$ | number of basis functions per cell; **$N$ is the degree in the registry** |
| $\boldsymbol u=(\rho,\rho\boldsymbol v,e)$ | $u=(\rho,\rho v,E)$ | conserved variables |
| $u$ | $e$ | specific internal energy; **collides with the state** |
| $e$ | $E$ | total energy per unit volume; **$e$ is the specific internal energy in the registry** |
| $c_s$ | $c$ | sound speed |
| $\boldsymbol u^-$, $\boldsymbol u^+$ | $u^-$, $u^+$ | inner and outer (neighbour) traces, relative to the outward normal, not left and right |
| $\boldsymbol F^\star$, $\boldsymbol f^\star_\alpha$ | $h$ | numerical (HLLC) flux; the direction index $\alpha$ is $d$ |
| $K$, $h$ | $K$, $\Delta x$ | cell and its edge length |
| $\boldsymbol w^K_l$, $P_l$, $\phi^K_l$ | kept | modal coefficients, Legendre polynomials with $\int_{-1}^1P_l^2=2$, basis; **$\boldsymbol w$ is not the entropy variable** |
| $n_g$, $g_j$ | $N+1$, kept | Gauss points per direction and weights |
| $N_c$, $N_{\mathrm{grid}}$, $N_{\mathrm{cells}}$ | $N_x$ | cells per dimension |
| $\varepsilon$, $\epsilon$ | $\mu$ (page-local) | diffusion coefficient; **$\epsilon$ is the WENO regularization in the registry** |
| $\alpha(\boldsymbol x,t)$ | $\alpha_{\mathrm{AV}}$ (page-local) | artificial-viscosity strength; **$\alpha$ is the DG–FV blending coefficient in the registry** |
| $f_v$, $f_w$, $f_\tau$, $\tau$, $S_{\mathrm{onset}}$ | $f_v$, $f_w$, $f_\tau$, $\tau_{\mathrm{AV}}$, $S_{\mathrm{on}}$ (page-local) | source, wiggle and decay coefficients, decay time, wiggle threshold |
| $S^K$ | $S^{\mathrm{PP}}_K$ (page-local) | Persson–Peraire modal sensor; **$S$ is also the dye entropy (Eq. 56) and the BR1 auxiliary gradient** |
| $K^\star$, $f$, $\psi^{K^\star}_l$, $\boldsymbol q^{K^\star}_l$, $\tilde{\boldsymbol u}$, $A^\pm_{m,l}$ | kept | recovery box, overlap fraction, recovery basis and coefficients, recovered polynomial, overlap integrals; **$f$ is reused as the positivity scaling factor and collides with the flux** |
| $\boldsymbol\Pi$, $\nu$, $\chi$, $\eta$ | kept | viscous stress, kinematic viscosity, thermal diffusivity, dye diffusivity; **$\nu$ is the CFL number and $\eta$ the entropy in the registry** |
| $\rho_{\mathrm{bottom}}$, $p_{\mathrm{bottom}}$ | $\rho_{\mathrm{bot}}$, $p_{\mathrm{bot}}$ | positivity floors |

# Reference list

67 printed references in author–year MNRAS style, alphabetical, all parsed
and merged complete into the [bibliography](/bibliography.md) with `citedby`
`cernetic-2023`. Persson & Peraire (2006) is printed book-like ("AIAA Inc.,
Reston, VA", with its DOI) and entered as a conference paper; van Leer &
Nomura (2005) is printed with a DOI; Markert, Gassner & Walch (2021) print a
DOI only; Federrath et al. (2016) is an arXiv e-print. Schmidt et al. 2006a/b
are keyed `schmidt-2006` and `schmidt-2006-b` in printed order. No printed
duplicates were found.

# Pages created or updated

Chunk 7 (2026-10-23), cited further in chunks 8–11 (2026-10-23/24). This source is cited on:

* [Artificial viscosity and spectral viscosity](/methods/artificial-viscosity.md)
* [Bassi–Rebay viscous discretizations (BR1, BR2)](/methods/bassi-rebay-viscous-discretization.md)
* [Discontinuous Galerkin method](/methods/discontinuous-galerkin.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)
* [Material-interface advection tests](/benchmarks/material-interface-advection.md)
* [Subcell finite-volume limiting for DG](/methods/subcell-finite-volume-limiting.md)
* [TENET](/software/tenet.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
* [Woodward–Colella interacting blast waves](/benchmarks/woodward-colella-blast-wave.md)
* [Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md)
