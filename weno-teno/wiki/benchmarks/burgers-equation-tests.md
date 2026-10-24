---
type: Benchmark
title: "Burgers equation tests"
description: "The inviscid Burgers equation as test bed: 1D to 3D sine data for accuracy before the shock and shock capturing after, energy and entropy tests of split forms, discontinuous data, a slow shock across a block interface, Burgers balance laws with source terms, 2D Riemann data, and gamma = 3 Euler data reducing to Burgers; setups, breaking times, orders."
status: established
aliases: [Burgers equation, inviscid Burgers test, Burgers sine wave, two-dimensional Burgers Riemann problem]
tags: [benchmark, weno, cweno, dg]
timestamp: 2026-10-24T06:00:00Z
---

# Burgers equation tests

The inviscid Burgers equation $\partial_tu+\partial_x(u^2/2)=0$, and its
two-dimensional form $\partial_tu+\partial_x(u^2/2)+\partial_y(u^2/2)=0$,
is the simplest genuinely nonlinear conservation law. Smooth data
steepen and form a shock at the breaking time
$t_{\mathrm b}=-1/\min_xu_0'(x)$ (page-local symbol), so a single
initial profile serves two tests: an accuracy test at $t<t_{\mathrm b}$,
where the exact solution follows from characteristics, and a
shock-capturing test at $t>t_{\mathrm b}$. The sources also use
discontinuous data, a slow shock across a block interface, balance laws
with a source term, a two-dimensional Riemann problem, and Euler data
that reduce exactly to Burgers.

## Sine data: accuracy and shock formation

| Source | Data | Domain | Accuracy time | Shock time |
|---|---|---|---|---|
| [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) Ex. 3.1 | $u_0=0.5+\sin(\pi x)$ | $[0,2]$, periodic | $0.5/\pi$, 10–320 cells | $1.5/\pi$, 200 cells |
| [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) Ex. 3.2 | $u_0=0.5+\sin(\pi(x+y)/2)$ | $[0,4]^2$, periodic | $0.5/\pi$, $10^2$–$320^2$ | $1.5/\pi$, $200^2$, cut along $x=y$ |
| [Fan, Zhao, Xiong & Qiu (2023)](/sources/fan-2023.md) Ex. 3.1 | $u_0=0.5+\sin(\pi x)$; 2D $u_0=0.5+\sin(\pi(x+y)/2)$ | $[0,2]$; $[0,4]^2$, periodic | $0.5/\pi$, 10–320 cells; $10^2$–$320^2$ | — |
| [Puppo, Semplice & Visconti (2023)](/sources/puppo-2023.md) §4.1, §4.3.1 | $u_0=0.5-0.25\sin(\pi x)$ | $[0,2]$, periodic | $1$, $\Delta t=h,10h,50h$ | $2$, 256 cells, $\Delta t=3h,5h$ |
| [Cicchino, Nadarajah & Del Rey Fernández (2022)](/sources/cicchino-2022.md) §4.1 | $u_0=\sin(\pi x)+0.01$ | $[0,2]$, periodic | — | $3$, 8 elements, $N=4,5$, RK4, $\Delta t=10^{-4}$ |
| [Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) §5.1.1 | $u_0=\sin(2\pi x)+2$ | $[0,1]$, periodic | — | $0.5$, $\mathbb P^4$ on 15 and $\mathbb P^{14}$ on 5 elements |
| [Yu & Hesthaven (2022)](/sources/yu-2022.md) §5.2 | $u_0=\sin(2\pi x)$, flux printed $u^2$ | $[0,1]$ | — | $0.3$, 80 elements |
| [Sousa & Scalo (2022)](/sources/sousa-2022.md) §2.3 | $u_0=1+\tfrac12\sin(\pi x)$ | $[-1,1]$, periodic | — | $1$, Fourier pseudo-spectral, 128 points, RK4 |
| [Zhong et al. (2023)](/sources/zhong-2023.md) Ex. 5 | $u_0=0.5+\sin(\pi x)$ | $[0,2]$, periodic | $0.15$, 20–320 cells | $0.5$, 20 and 40 cells, reference WENO-JS on 10000 |
| [Calhoun, Chudzik & Helzel (2023)](/sources/calhoun-2023.md) §4.4 | $u_0=\sin(2\pi x)\sin(2\pi y)+0.1$, 2D flux $(u^2/2,u^2/2)$ | $[0,1]^2$, boundary conditions not stated | $0.05$, AMR | $0.2$, $0.6$, $1.0$, AMR levels 3–5 |
| [Qin et al. (2023)](/sources/qin-2023.md) §3.2 | $u_0=0.25+0.5\sin(\pi x)$ | $[-1,1]$, periodic, boundary closures kept active | $0.3$, 40–640 points | $4$, $7.9$, $8.1$, 200 points |
| [Kolluru et al. (2024)](/sources/kolluru-2024.md) §3.1–3.2 | IC0 $u_0=\sin(2\pi x)$; IC1 $u_0=\sin(2\pi x-\pi/2)$ | $[0,1]$, periodic | $0.07$, $N_x=39$–$7995$ | $0.2$, $2.0$ (IC0), $0.17$ (IC1); Fourier, RK4 |
| [Lin & Zhu (2024)](/sources/lin-2024-b.md) Case 3.1 | $u_0=0.5+\sin(\pi(x+y)/2)$ | $[-2,2]^2$, periodic, triangles | $0.5/\pi$, 58–14848 cells | — |
| [Zhang & Zhu (2024)](/sources/zhang-2024-c.md) Ex. 3.1–3.2 | $u_0=0.5+\sin(\pi x)$; 2D $u_0=0.5+\sin(\pi(x+y)/2)$ | $[0,2]$; $[0,4]^2$, periodic | $0.5/\pi$, 100–200 points or cells; $100^2$–$200^2$ | — |
| [Fan et al. (2025a)](/sources/fan-2025.md) Ex. 3.1, 3.3 | $u_0=0.5+\sin(\pi x)$; 2D $u_0=0.5+\sin(\pi(x+y)/2)$ | $(0,2)$; $(0,4)^2$, periodic | $0.5/\pi$, 40–240 cells; $40^2$–$240^2$ | — |
| [Danis et al. (2025)](/sources/danis-2025.md) §5.2 | $u_0=0.5+0.5\sin(2\pi(x+y+z))$, 3D flux $(u^2/2,u^2/2,u^2/2)$ | $[0,1]^3$, periodic | $1/(12\pi)$, up to $320^3$, $\Delta t=h^{5/3}$ | — |
| [Vilar & Abgrall (2024)](/sources/vilar-2024.md) §3.4, §4.2.1 | $u_0=\sin(2\pi(x+y))$, 2D flux $(u^2/2,u^2/2)$ | $[0,1]^2$, periodic, triangles | — | $0.5$, $\mathbb P^5$ on 576 and $\mathbb P^3$ on 242 triangles |
| [Duan, Barsukow & Klingenberg (2025)](/sources/duan-2025.md) Ex. 5.5 | $u_0=0.5+\sin(2\pi(x+y))$, 2D flux $(u^2/2,u^2/2)$ | $[0,1]^2$, periodic | — | $0.3$, $100\times100$, generalized Active Flux with LLF flux vector splitting |
| [Cao et al. (2026)](/sources/cao-2026.md) Ex. 6.1, Ex. 6.12 | $u_0=\sin x+0.5$; 2D $u_0=0.5+\sin(\pi(x+y)/2)$ | $[0,2\pi]$; $[-2,2]^2$, periodic | $0.6$; $\mathbb P^1$ 1280–10240, $\mathbb P^2$ 320–2560, $\mathbb P^3$ 160–1280 cells | 2D: $1.5/\pi$, $160\times80$, third order, cut along the diagonal cells |
| [Liu et al. (2026)](/sources/liu-2026.md) §5.1.1, §5.1.4 | $u_0=A\sin x+B$ (training family); 2D $u_0=A\sin(2\pi x+x_0)\cos(2\pi y+y_0)+B$ ($A$, $B$, $x_0$, $y_0$ page-local, random) | $[0,2\pi]$; $[0,1]^2$, periodic | training data on $[0,0.1]$ (1D) | test to $T=3$ (1D), $T=1.6$ (2D) |

For $u_0=0.5+\sin(\pi x)$, $t_{\mathrm b}=1/\pi$ (stated by Zhong et
al.); along the diagonal the
two-dimensional data have the same breaking time (the data of Li, Shu
& Qiu, also run by Fan et al. (2023) and Fan et al. (2025a), by Zhang &
Zhu and, on $[-2,2]^2$, by Lin & Zhu); Danis et al. call their final
time "well before the breaking time": along $\xi=x+y+z$ their equation
is $\partial_tu+3u\,\partial_\xi u=0$ with $\max\lvert\partial_\xi u_0\rvert=\pi$,
so $t_{\mathrm b}=1/(3\pi)$ and $1/(12\pi)$ is a quarter of it; for
Vilar & Abgrall's data, $\partial_tu+2u\,\partial_\xi u=0$ along
$\xi=x+y$ gives $t_{\mathrm b}=1/(4\pi)\approx0.08$, and the two shocks form
on the lines $x+y=0.5$ and $x+y=1.5$ where $u_0$ decreases through zero,
the stationary shocks the authors state *(compiler check, not in the
sources)*; Duan, Barsukow & Klingenberg's data have the same slope
$2\pi$ along $\xi=x+y$, so $t_{\mathrm b}=1/(4\pi)\approx0.08$ and their
$t=0.3$ is a shock-capturing time *(compiler check, not in the
sources)*; for $u_0=\sin(2\pi x)$, Kolluru et al. state
$t_{\mathrm b}=1/(2\pi)\simeq0.159$, the shock forming at $x=0.5$; for Calhoun et al.'s two-dimensional
data, whose characteristics carry the Jacobian
$1+t\,(\partial_xu_0+\partial_yu_0)$ and
$\partial_xu_0+\partial_yu_0=2\pi\sin(2\pi(x+y))$,
$t_{\mathrm b}=1/(2\pi)\approx0.16$ *(compiler check, not in the
sources)*; for
$u_0=0.5-0.25\sin(\pi x)$, $t_{\mathrm b}=4/\pi\approx1.27$ *(compiler
check, not in the sources)*. The accuracy times thus lie before and
the shock times after breaking. Likewise $t_{\mathrm b}=1/\pi$ for
Cicchino et al., $1/(2\pi)\approx0.16$ for Dzanic et al., $2/\pi\approx0.64$
for Sousa & Scalo and for Qin et al. (who print $t=2/\pi$ themselves), and, with Yu & Hesthaven's flux $u^2$ (characteristic
speed $2u$), $1/(4\pi)\approx0.08$ *(compiler check, not in the
sources)*: all five run past breaking. For Cao et al.'s
$u_0=\sin x+0.5$, $t_{\mathrm b}=1$, so $t=0.6$ is an accuracy time,
and their 2D data are Li, Shu & Qiu's on a shifted square, with
$t_{\mathrm b}=1/\pi$ along the diagonal *(compiler check, not in the
sources)*.

**Orders.** Li, Shu & Qiu's sixth-order moment-based
[multi-resolution HWENO](/methods/hermite-weno.md), with the first
moments modified only in cells flagged by their indicator (M5-I),
reaches $L^1$ error $3.95\times10^{-13}$ at 320 cells (order 5.96) in
1D and $6.83\times10^{-12}$ at $320^2$ (order 6.36) in 2D; modifying the
moments in every cell (M5-NI) drops the order to five, as they expect
(4.97 and 4.88; Tables 3.1–3.2). Fan, Zhao, Xiong & Qiu's fifth-order finite-difference
[Hermite WENO](/methods/hermite-weno.md) with restricted derivatives
(HWENO-R) gives $L^1$ errors $3.69\times10^{-10}$ at 320 cells and
$3.64\times10^{-10}$ at $320^2$, against $3.24\times10^{-10}$ and
$3.20\times10^{-10}$ for HWENO-L and $2.12\times10^{-9}$ and
$2.10\times10^{-9}$ for WENO-ZQ (Table 3.1). On meshes of at least 160
cells HWENO-R costs about 1.2 times the CPU time of WENO-ZQ (1.45 in
2D) for an error about 5.3 times smaller, so it is the more efficient at
equal error (Fig. 3.1). Its observed 1D orders oscillate, 2.98, 4.61,
6.99, 6.15, 5.32, which the authors explain only qualitatively
(Remark 3.1); $\log_2(1.32\times10^{-4}/1.04\times10^{-6})=6.99$
reproduces the printed order at 80 cells *(compiler check, not in the
sources)*. Back to Li, Shu & Qiu: on the shocked data the unmodified and
modified schemes both match the exact solution with "not much
difference" (Figs. 3.1–3.2). Puppo et al.'s time-limited implicit
[Quinpi](/methods/quinpi.md) scheme Q3P1 converges at third order even
at time steps of 10 and 50 cell widths: $L^1$ errors
$3.66\times10^{-7}$ ($\Delta t=h$, 2560 cells), $1.29\times10^{-7}$
($\Delta t=10h$, 5120 cells) and $1.41\times10^{-5}$ ($\Delta t=50h$,
5120 cells), with finest-grid rates 2.99, 2.99 and 2.79 (Table 1);
implicit Euler is first order and the unlimited DIRK–CWENO scheme D3P1
third order on the same data (Fig. 1). After the shock forms, Q3P1 is
slightly more diffusive than D3P1 but much less than implicit Euler,
and at $\Delta t=5h$ it reduces D3P1's oscillations (Figs. 4–5).

**Multi-resolution WENO with fewer stencils.** Two schemes of the
Zhu group, both compared with the
[multi-resolution WENO](/methods/multi-resolution-weno.md) of Zhu & Shu
on the same data, run the smooth sine. Lin & Zhu's finite-volume
ALW-MR-WENO on triangles, which keeps only a one-cell and one large
stencil, reaches finest-mesh $L^1$ errors $4.90\times10^{-5}$ (third
order), $1.36\times10^{-6}$ (fourth) and $1.63\times10^{-7}$ (fifth),
identical to MR-WENO; the fifth-order $L^1$ orders are 2.17, 5.02,
4.98, 4.88 and the fourth-order ones 3.02, 3.61, 3.97, 4.41, the
finest-mesh $L^\infty$ orders 2.75, 3.95 and 4.82 (Case 3.1, Table 3.2,
CFL 0.6, third-order TVD Runge–Kutta). Zhang & Zhu's ghost
multi-resolution GMR-WENO, built on one central stencil, gives at third
order, 200 points, $L^1$ error $1.27\times10^{-5}$ and $L^\infty$ error
$2.37\times10^{-4}$, against $2.25\times10^{-5}$ and $4.61\times10^{-4}$ for
MR-WENO3; at fifth and seventh order the $L^1$ errors are identical to
MR-WENO's to the printed digits ($2.27\times10^{-8}$ for both fifth-order
finite-difference schemes at 200 points) (Ex. 3.1, Table 3.2). Their
third-order $L^\infty$ orders on Burgers are 2.25–3.37; they take
$\Delta t\sim(\Delta x)^{\nu/3}$ for a scheme of order $\nu$ to keep the
third-order Runge–Kutta error below the spatial one, and GMR-WENO
reaches a given error in less CPU time (Figs. 3.1–3.4).

**Hermite WENO with unified stencils.** Fan et al. (2025a) run the same
sine data with their fifth-order moment-based
[Hermite WENO](/methods/hermite-weno.md) HWENO-U, which obtains the
point values and the high-order modification of the first moment from
one reconstruction on one set of stencils (CFL 0.6, a modified SSP-RK3).
HWENO-U, HWENO-M (two stencil sets) and WENO-ZQ are all fifth order,
and so are HWENO-U's first moments (Tables 1–2, 4–5); at 240 cells the
$L^1$ errors are $6.97\times10^{-10}$, $7.58\times10^{-10}$ and
$8.95\times10^{-9}$. On meshes of at least 200 cells HWENO-U costs 1.516
times the CPU time of WENO-ZQ for an $L^1$ error 12.800 times smaller,
HWENO-M 2.319 times for 11.777 times smaller; in 2D the ratios are
1.312 and $1/59.905$ for HWENO-U, 1.601 and $1/75.842$ for HWENO-M
(§3.1).

**Tensor-train WENO.** Danis et al. solve the three-dimensional data with
fifth-order finite-difference WENO-JS in
[tensor-train format](/methods/tensor-train-weno.md), with the
truncation tolerance set by their dynamic rule with $C_\varepsilon=10$
(page-local: the problem-dependent constant of that rule). The
tensor-train and full-tensor errors nearly coincide, $9.01\times10^{-10}$
against $9.03\times10^{-10}$ at $320^3$ with order 4.96 (§5.2, Table 2;
arXiv v1).

**Symmetric smoothness indicators.** Zhong et al.'s fifth-order
finite-volume IMWENO-P, whose smoothness indicators satisfy their
mirror-symmetry condition (see
[smoothness indicator](/definitions/smoothness-indicator.md)), reaches
fifth order on the smooth data with $L_1$ error $3.30\times10^{-9}$ at
320 cells, against $1.63\times10^{-8}$ for
[WENO-JS](/methods/weno-js-reconstruction.md) (Table 6; SSP-RK3, global
Lax–Friedrichs flux, CFL number $(\Delta x)^{2/3}$); the shocked solutions at $t=0.5$ on 20 and 40 cells are
compared with the WENO-JS reference (Fig. 3).

**Boundary closures.** Qin et al. run the sine with their fifth-order
multi-resolution [WCNS](/methods/weighted-compact-nonlinear-scheme.md)
and one-sided nonlinear [boundary closures](/methods/shock-capturing-boundary-closure.md)
used at the ends of a periodic domain, with global Lax–Friedrichs
splitting. At $t=0.3$ the $L_2$ order is 5.16 and the $L_\infty$ order
4.97 at 640 points; their scaled smoothness indicators (scaling
parameter $\lambda_{\mathrm s}=2$, the shared page-local symbol of Qin et al.'s scaling)
give larger errors than $\lambda_{\mathrm s}=1$ on coarse grids ($L_2$
$6.92\times10^{-5}$ against $4.37\times10^{-5}$ at 40 points) and the
same from 160 points (Table 11). After breaking, the shock reaches $x=0$
at $t=4$ and crosses the periodic boundary between $t=7.9$ and $8.1$
with correct profile and location (Fig. 3); the shock moves at speed
$0.25$, and its positions $0$, $\approx0.975$ and $\approx-0.975$ at the
three times follow from the characteristic through $x=1$ *(compiler
check, not in the sources)*.

**Shock capturing in element methods.** Dzanic, Trojak & Witherden
use the shocked sine to show that their residual-based
[artificial viscosity](/methods/artificial-viscosity.md) with $c_\mu=1$
resolves the shock over 4–5 solution points without spurious
oscillations at $\mathbb P^{14}$ on 5 elements, at a width similar to
$\mathbb P^4$ on 15 elements, with the viscosity localized at the shock:
"the proposed approach does not suffer with increasing approximation
order" (§5.1.1, Fig. 1). Yu & Hesthaven capture the discontinuity
without spurious oscillations on 80 elements with ANN-predicted
viscosity, whose peak decreases with the degree; a slight asymmetry of
the viscosity is attributed to the randomness of the training samples
(§5.2, Figs. 5–6).

**A posteriori subcell correction.** Vilar & Abgrall use the
two-dimensional data, with its two stationary shocks, to compare two
versions of their a posteriori local subcell correction of
$\mathbb P^5$ DG on 576 triangles ([MOOD-type limiting](/methods/mood-a-posteriori-limiting.md),
recast through the [DG–subcell finite-volume equivalence](/results/dg-subcell-finite-volume-equivalence.md)).
The new version blends the first-order and reconstructed subcell fluxes
with coefficients $1,\tfrac34,\tfrac12,\tfrac14$ decreasing with the
distance from a troubled subcell. It corrects 14% of the subcells on
average against 10% for the original, but needs 1.46 correction
iterations on average (at most 3) against 2.86 (at most 6), and runs in
2 min 15 s against 2 min 22 s, hardware not stated (§3.4, Figs. 6–9).
Uncorrected sixth-order DG oscillates at the shocks (Fig. 28); the
corrected scheme captures them at sixth order on 576 cells and at fourth
order on 242 cells with four subcell subdivisions (§4.2.1, Figs.
29–32; HAL preprint).

**Spectral make-up of added dissipation.** Sousa & Scalo filter the
shocked sine with a sharp spectral filter and compute the exact
sub-filter flux from the characteristic solution: its energy spectrum
spans all resolved wavenumbers with a plateau and a cusp near the
cut-off, the shape of the Kraichnan and Chollet–Lesieur turbulence
spectra, here produced by shock formation (§2.3, Fig. 1b). A
posteriori, dynamic Smagorinsky dissipates uniformly across the
spectrum, over-damps large scales, under-damps near the cut-off and
lets oscillations pile up, and spectral vanishing viscosity with an
inviscid low range under-damps low wavenumbers; their
[quasi-spectral viscosity](/methods/quasi-spectral-viscosity.md), tuned
on this test, matches the exact spectrum best (Fig. 1).

**Spectral relaxation.** Kolluru et al. add to a Fourier
pseudo-spectral method a relaxation of the solution, at rate $1/\tau$,
towards its convolution with a positive kernel (spectral relaxation, SR,
or its time-discontinuous projection form, SP), with exponents
$(\alpha_{\mathrm{SR}},\gamma_{\mathrm{SR}})$ (page-local; their $(\alpha,\gamma)$) that set how $\tau$ and the
kernel width scale with $N$; see
[artificial and spectral viscosity](/methods/artificial-viscosity.md).
On IC0 without dealiasing, the Fejér–Korovkin kernel with
$(\alpha_{\mathrm{SR}},\gamma_{\mathrm{SR}})=(0.7,0.99)$, the optimum of a parameter search over
$t\in[0,9.9]$, removes the "tygers" (localized oscillatory structures that the
truncated pseudo-spectral Burgers solution develops in smooth regions
away from the shock) and is monotone at the shock; its smooth-data order
at $t=0.07$ is about 1.28 ($L^1$) and 1.27 ($L^2$), after the shock about
0.9 and 0.78, with $L^1$ errors at $N_x=7995$ of $5.8\times10^{-6}$,
$4.6\times10^{-4}$ and $6.5\times10^{-5}$ at $t=0.07$, $0.2$ and $2$
(Table 1). Their heuristic scaling of the relaxation term gives an
order $N^{-(2\gamma_{\mathrm{SR}}-\alpha_{\mathrm{SR}})}$, i.e. $2-\alpha_{\mathrm{SR}}$ for $\gamma_{\mathrm{SR}}\simeq1$, and
their Fig. 4 shows orders falling from about 1.95 at $\alpha_{\mathrm{SR}}=0$ to about
1.05 at $\alpha_{\mathrm{SR}}=0.9$, which the authors take as confirming the
heuristic (§3.1). The de la Vallée-Poussin kernel with $(0.89,0.9)$
converges spectrally before the shock, $L^1$ errors from
$1.2\times10^{-5}$ at $N_x=39$ to $2.8\times10^{-13}$ at 205 (orders 6.82,
9.89, 15.28, then round-off), but after the shock its $L^2$ order is
only about 0.5 ($t=0.2$) and 0.44 ($t=2$) against about 0.8 for
Fejér–Korovkin, at equal $L^1$ order (about 0.95; Table 2). The authors
attribute the better shock convergence of the low-order kernel to its
monotonicity and maximum principle, and conclude that "high-order
approximations as the sole criterion for designing accurate numerical
schemes can be misleading" (§3.1). Spectral vanishing viscosity with
$\epsilon=N^{-1}$, $M=2\sqrt N$ (their parameters) keeps small Gibbs-like
oscillations at the shock (Fig. 7). On IC1 the plain Fejér–Korovkin run
with $(0.97,0.98)$ blows up and needs $(1.18,0.99)$ (orders about 0.80 in
$L^1$, 0.40 in $L^2$ after the shock; Table 3); with 2/3 dealiasing
$(0.97,0.98)$ is stable, with $L^1$ orders about 0.99 at $t=0.07$ and
0.95 at $t=2$ (Table 4). Dealiasing makes the plain pseudo-spectral
method worse for IC0 and better for IC1, from which the authors
conclude that the growth of aliasing errors depends on the initial data
(§3.2, Fig. 10).

**Oscillation-suppressing DG.** Cao et al. (2026) reach the optimal
order $N+1$ with $\mathbb P^N$ [COS(DG)](/methods/cos-dg.md) on the 1D
sine, e.g. $L^1$ error $1.37\times10^{-11}$ at rate 3.96 for
$\mathbb P^3$ on 1280 cells (Table 1), the post-processing being applied
once per time step and shown to perturb an $(N+1)$-th order DG solution
by $O(h^{N+1})$ (their Thm. 2.1). On the shocked 2D data with third
order on $160\times80$ cells, after the comparison of DG limiters whose
codes they reuse, COS(DG) gives the sharpest non-oscillatory profile
along the diagonal, the other limiters being more dissipative near the
shocks or overshooting (Ex. 6.12, Fig. 13).

**Learning a flux from Burgers data.** Liu et al. (2026) (arXiv v1)
train a neural entropy-stable flux, together with a learned convex
entropy, on PyClaw trajectories of the 1D sine family with
$A\sim U[0.75,1.25]$ and $B\sim U[-0.25,0.25]$ (200 trajectories, 512 points, $\Delta t=0.005$, 20
steps), so the training window $[0,0.1]$ ends before any shock forms.
On the test datum $A=1.05609$, $B=0.1997$ the learned model
forms the shock at about $t=1$ and predicts to $T=3$; with noise of
relative level $\xi$ ($\xi$ page-local) added to the data, the shock
structure survives for $\xi\le0.5$, against $\xi\le1$ for the authors'
earlier flux network inside a fixed Kurganov–Tadmor scheme, which they
attribute to learning the entropy (§5.2.1, Fig. 5.1); a discrete
entropy remainder stays non-positive over 101 further initial data
(Fig. 5.3). The test datum breaks at $t_{\mathrm b}=1/A\approx0.95$
*(compiler check, not in the sources)*. On the 2D family (5
trajectories of $100\times100$ points, $\Delta t=0.001$, test to
$T=1.6$) the prediction stays accurate at $\xi=1$, with more numerical
diffusion than expected, which they attribute to the difficulty of
learning the maximum local wave speed (§5.2.4, Figs. 5.10–5.11).

**Active Flux on adaptive grids.** Calhoun, Chudzik & Helzel run the
two-dimensional sine data with their Cartesian
[Active Flux](/methods/active-flux.md) method in ForestClaw
([adaptive mesh refinement](/methods/adaptive-mesh-refinement.md) with
subcycling and a conservative fix at coarse–fine interfaces). The
point values are evolved by a fixed-point iteration of the implicit
characteristic relation $u(x,y,t)=u_0(x-ut,\,y-ut)$, each iteration
gaining one order, two iterations from a first-order guess giving the
third order of the biquadratic reconstruction (§2.2). At $t=0.05$, with
refinement fixed along the diagonal and CFL at most 0.5, they state
third order, with the result "not shown here". At $t=0.2$, $0.6$ and
$1.0$ on levels 3–5, unlimited Active Flux shows unphysical oscillations
along the curve where the characteristic speed changes sign; the
bound-preserving limiter of their earlier work, applied where the
refinement criterion flags steep gradients, avoids them (Fig. 12).

## Space–time Burgers: accelerating shock and shock merger

[Huang & Zahr (2022)](/sources/huang-2022.md) (arXiv v2) solve
Burgers' equation as a steady problem in the space–time slab with their
high-order [implicit shock tracking](/methods/implicit-shock-tracking.md)
method, which moves the mesh so that element faces fit the
discontinuity:

- *Accelerating shock* (§6.2.1, iburg-acc): $(z,t)\in(-0.2,1)\times(0,1.2)$,
  inflow value $\mu_1=4$ at $z=-0.2$, $\mu_2=3$. The exact solution
  (79) is $u=\mu_1$ left of the shock and $u=\mu_2(z-1)/(1+\mu_2t)$
  right of it, and the shock path (80) starts at $z=0$ and accelerates.
  On 72 right triangles whose hypotenuses cross the shock, with
  solution and mesh degrees $p=q=1,2,3$ (page-local; the registry's
  $N$ for the solution degree), the discontinuity is mostly tracked after 20 iterations;
  re-initializing oscillatory elements is needed for $p=3$, without
  which the solver stalls (Figs. 17–19). Under refinement (Table 2) the
  solution error $E_\phi$ along $z=0.8$ decreases with segment slopes
  5.88, 3.92, 2.88 for $p=2$ and 6.60, 5.21, 3.73 for $p=3$, and the
  shock-position error $E_{z_s}$ with slopes of at least $p+1$ except
  the first $p=1$ segment (1.09).
- *Shock formation and merger* (§6.2.2, iburg-form): $(z,t)\in(-1,1)\times(0,1)$,
  $u_0=1.2\exp(-(z+0.5)^2/0.025)-\exp(-(z-0.5)^2/0.025)$, Dirichlet
  data $u_0(\pm1)$, 400 right triangles, $p=q=2,3$. Two shocks form and
  merge in a space–time triple point that the method tracks from a mesh
  carrying no knowledge of them; where the formation is under-resolved
  the steep continuous profile is represented by a growing
  discontinuity (Figs. 21–22).

The printed exact solution satisfies Burgers' equation
($u_t+uu_z=0$ for $u=\mu_2(z-1)/(1+\mu_2t)$), and with
$s=\sqrt{1+\mu_2t}$ the path $z_s=1+(\mu_1/\mu_2)s(s-1)-s$ starts at
$z_s(0)=0$ and moves at the Rankine–Hugoniot speed
$\tfrac12\big(\mu_1+\mu_2(z_s-1)/(1+\mu_2t)\big)$ *(compiler check,
not in the sources)*.

[Naudet & Zahr (2024)](/sources/naudet-2024.md) (§5.1) run the same
problems with the space-time version of the method, in which the
space-time domain is cut into $S$ slabs solved one after another
(HOIST):

- *Accelerating shock leaving the domain* (§5.1.1): $z\in(-0.2,1)$,
  $t\in(0,1)$, $\mu_1=4$, $\mu_2=3$, the exact solution (48) and shock
  path (49) of the problem above. On 192 quadratic ($p=q=2$) space-time
  simplices split into $S=1,2,4,8$ slabs of initial heights $1.2$, $0.6$,
  $0.3$, $0.15$ (the heights are then optimized; $1.2$ is the time interval
  of Huang & Zahr, longer than the $(0,1)$ printed here), with 100
  iterations per slab, "as more slabs are added, the
  residuals converge more rapidly and to deeper tolerances" (Fig. 9). A
  translating top boundary of the slab places the exit of the shock
  through $z=1$ exactly; with shock boundary conditions ($S=5$, 6 spatial
  elements, 24 space-time elements in the first slab) the method
  "eliminates over half of the space-time elements" (Figs. 10–11).
  Their path (49), $(\mu_1/\mu_2+1)(1-s)+\mu_1t$, equals Huang & Zahr's
  $(s-1)(4s-3)/3$ for these $\mu$ and reaches $z=1$ at $s=7/4$, i.e.
  $t=11/16\approx0.69$, in the fifth slab for $S=8$, as they state
  *(compiler check, not in the sources)*.
- *Shock formation and merger* (§5.1.2): the Gaussian data above on
  $(-1,1)\times(0,1)$, one slab, 96 quadratic triangles; eight rounds of
  adaptive refinement give 207 triangles that resolve the formation
  point and agree with a highly refined second-order finite-volume
  solution at $t=0.1$ (Figs. 12–13).
- *Curved shock in two dimensions* (§5.1.3, data from Huang & Zahr's
  method-of-lines paper): flux $\tfrac12u^2(1,0)$ on $(-1,1)^2$,
  $t\in(0,1.5)$,
  $u_0=\tfrac43(x+0.75)\big(0.5-2(y^2-0.25)\big)$ on
  $(-1,0)\times(-0.5,0.5)$ and $0$ elsewhere; three slabs, 32 spatial
  triangles extruded to 448 quadratic tetrahedra in the first slab. The
  initially straight shock curves and is captured by the curved
  elements (Fig. 14).

## Energy and entropy tests

Burgers' equation with the square entropy $\eta=u^2/2$ serves as the
scalar test of discrete energy (entropy) conservation in the sources below.
[Cicchino, Nadarajah & Del Rey Fernández (2022)](/sources/cicchino-2022.md)
§4 (arXiv v1) split the volume term as
$\tfrac23\partial_x(u^2/2)+\tfrac13u\partial_xu$ in energy-stable
[flux reconstruction](/methods/flux-reconstruction.md) and run the
shocked sine above on Gauss–Lobatto nodes (collocated), on $N+1$ Gauss
nodes (uncollocated) and on $N+3$ Gauss nodes (overintegrated), with
an energy-conservative or a local Lax–Friedrichs interface flux. With
their split form, in which the flux-reconstruction filter also acts on
the non-conservative volume term, the energy is conserved to
$O(10^{-12})$ with the conservative flux and decreases monotonically
with Lax–Friedrichs, for $c_{\mathrm{DG}}$, $c_+$ and $c=10^4$ (their
correction parameters); the conservative DG scheme and the classical
split forms, filtered on the surface only, do neither, except Huynh's
lumped-Lobatto $g_2$ scheme (Tables 1–3). A manufactured solution
$u=\cos(\pi(x-t))$ with source term
$\pi\sin(\pi(x-t))\big(1-\cos(\pi(x-t))\big)$ to $t=1$ gives orders
near $N+1$ for $N=4$ and about 5.7 for $c_+$ at $N=5$ (Tables 4–7). See
[split convective forms](/methods/split-convective-forms.md) and
[entropy stability](/properties/entropy-stability.md).

[Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) (arXiv v4)
use two Burgers-type tests of their
[entropy correction term](/methods/entropy-correction-term.md):

- Example 2.12, $\partial_tu+\partial_x(u^2/2)=0$ on periodic $[0,3]$
  with $u_0=-1$ on $(1,2)$ and $+1$ elsewhere, whose entropy solution
  has a stationary shock at $x=1$ and a rarefaction at $x=2$. Central
  finite-difference and Fourier collocation schemes, with or without
  the correction, keep the initial data stationary, so a global entropy
  equality does not make a scheme converge to the entropy solution (no
  numbers given). The shock at $x=1$ is stationary because the
  Rankine–Hugoniot speed is $\tfrac12(1+(-1))=0$, and the jump at $x=2$
  from $-1$ to $+1$ is an expansion shock in the initial data
  *(compiler check, not in the sources)*.
- §4.1, a two-dimensional Burgers-type equation
  $\partial_tu+\partial_x(\cos u)+\partial_yu=0$ on the unit disk with
  $u_0=\exp(-40(x^2+y^2))$, outflow, to $t=0.2$ before shock formation,
  third-order continuous Galerkin residual distribution, SSPRK(3,3),
  CFL 0.1. The non-polynomial flux makes the quadrature inexact. The
  entropy changes at $t=0.2$ are $1.6819\times10^{-15}$ and
  $1.6822\times10^{-15}$ for the two weightings of the correction, so
  the weighting makes no significant difference on smooth data.

## Discontinuous data and interacting shocks

[Puppo et al.](/sources/puppo-2023.md) §4.3.2–4.3.3 run, on periodic
$[-1,1]$:

- the top hat $u_0=1$ on $|x|\le0.25$, $0$ otherwise, to $t=0.5$ on 400
  cells with $\Delta t=3h,5h$, which develops a rarefaction and a moving
  shock (Fig. 6). Without their conservative correction Q3P1 loses mass
  and misplaces the shock; with it mass is conserved at all times and
  the shock is correctly placed (Fig. 7). An explicit first-order
  predictor, even at each Runge–Kutta abscissa, does not prevent
  spurious oscillations at $\Delta t=5h$ (Fig. 8);
- $u_0=0.2-\sin(\pi x)+\sin(2\pi x)$ on 256 cells with $\Delta t=5h$,
  shown at $t=1/(2\pi)$ (shock formation), $0.6$ (before the shocks
  interact) and $1$ (after): Q3P1 is non-oscillatory and sharper than
  implicit Euler (Fig. 9).

[Abgrall et al. (2026)](/sources/abgrall-2026.md) Ex. 2 call
$u_0=2$ on $\lvert x\rvert\le0.2$, $-1$ otherwise, on periodic
$[-1,1]$ the "self-steepening shock" and run it to $t=0.5$ on 200 cells
with their bound-preserving [PAMPA scheme](/methods/pampa-scheme.md)
(SSP-RK3, CFL 0.2), with strict bounds $[-1,2]$ and relaxed bounds
$[-1.003,2.003]$. Without the bound-preserving blending the point values
develop a spike; with either set of bounds there is none (Fig. 2). The
results are "obtained without sonic point transition that is described
in" Duan, Barsukow & Klingenberg's generalized Active Flux (below), which needs
flux vector splitting at sonic points, and the authors state that their
scheme does not exhibit the transonic issues of that work (§1). The jump
at $x=-0.2$ from $-1$ to $2$ opens a transonic rarefaction through the
sonic value $u=0$, and the jump at $x=0.2$ from $2$ to $-1$ is a shock of
speed $\tfrac12(2-1)=\tfrac12$ *(compiler check, not in the sources)*.

[Duan, Barsukow & Klingenberg (2025)](/sources/duan-2025.md) Ex. 5.1
(arXiv v3) run the same data to the same time on the same 200 cells, at
CFL 0.2, as the test that exposes the stagnation of the point-value
update of the generalized [Active Flux](/methods/active-flux.md) method
when it uses Jacobian splitting: at the jump from $2$ to $-1$ the two
upwind derivatives vanish, both point values stay frozen and the cell
average grows linearly in time, a spike (§2.1, Fig. 3). Updating the
point values by [flux vector splitting](/methods/flux-vector-splitting.md)
(local Lax–Friedrichs or upwind splitting) takes information from the
neighbours and removes the spike; their bound-preserving limiting alone,
added to the Jacobian splitting, does not (Fig. 3). Abgrall et al.'s
PAMPA result above is the same experiment run with a different scheme.
On the two-dimensional sine data of the table their limiters are active
only near the shocks (Ex. 5.5, Fig. 8).

[de Romémont et al. (2026)](/sources/deromemont-2026.md) §6.1 take the
composite data of Ray & Hesthaven on $[0,1]$: $u_0=1.5$ on
$3/8\le x\le3.5/8$ and on $4/8<x\le4.5/8$, $0.5$ on $3.5/8<x<4/8$, $1$ on
$4.5/8<x\le5/8$, and $\tfrac12\sin(8\pi x)$ elsewhere, to $t=0.39$. Their
second-order MUSCL finite-volume scheme with
[learned slopes](/methods/learned-weno-weights.md) (a convolutional
network predicts three-point slope coefficients inside the van Albada
limiter; Rusanov flux, explicit Euler, Courant number $0.01$) on 256
cells has smaller and narrower error spikes at the discontinuities than
the same scheme with standard slopes on the same grid, against a
1024-cell reference (Figs. 5–6); unlike their Euler tests, no error gain
is printed for this case. The test is not in their training set, which
holds randomized sine waves partly multiplied by a rectangle function
(App. B).

**Slow shock across a block interface.** [Qin et al.](/sources/qin-2023.md)
§3.2 start from $u_0=1.02$ for $x<0.1$ and $u_0=-1$ otherwise, a shock
of speed $0.01$, on $[0,1]$ split at $x=0.5$ into two blocks of 160 and
80 points (a 2:1 jump of grid spacing). The shock crosses the interface
"with invisible oscillation and phase lag" at $t=40$ and $80$ (Fig. 4);
they cite Pärt-Enander & Sjögreen and Sebastian & Shu for the
stagnation and oscillation of slow shocks at non-conservative
interfaces. A two-dimensional Euler version (shock speed $0.015$) is
recorded on [shock-capturing boundary closures](/methods/shock-capturing-boundary-closure.md).

## Burgers balance laws

[Yajaman, Toro & Demattè (2025)](/sources/yajaman-2025.md) §7.1 test
their [AENO-C reconstruction](/methods/aeno-reconstruction.md) inside
[ADER](/methods/ader-scheme.md) finite volumes on two Burgers balance
laws:

- $\partial_tu+\partial_x(u^2/2)=\beta_{\mathrm B}u^2$ with
  $\beta_{\mathrm B}=-2$ (page-local; their $\beta$), $u_0=\sin(2\pi x)$ on
  periodic $[-1,1]$, to $t=0.05$ before the shock, CFL 0.95. The exact
  solution follows from characteristics,
  $u=u_0(x_0)/\big(1-\beta_{\mathrm B}tu_0(x_0)\big)$ with
  $x=x_0-\ln\big(1-\beta_{\mathrm B}tu_0(x_0)\big)/\beta_{\mathrm B}$
  (Eqs. 58–59): along $dx/dt=u$ the source gives $du/dt=\beta_{\mathrm B}u^2$,
  whose solution integrates to that $x$ *(compiler check, not in the
  sources)*. ADER with AENO-C reaches the expected order at essentially
  every order from 2 to 10 in all norms (Table 3).
- $\partial_tu+\partial_x(u^2/2)=e^{-u}$ with $u=e^{-2(x-1/5)^2}$ for
  $x<0$ and $u=\tfrac14e^{-2(x+1/5)^2}$ for $x>0$, transmissive
  boundaries, a generalized Riemann problem whose shock accelerates;
  ninth-order ADER with AENO-C on 800 cells at CFL 0.95 reproduces the
  $x$–$t$ picture of Demattè et al.'s earlier computation, as the authors
  state from a qualitative comparison; the final time is not printed
  (Fig. 12).

The authors argue that ENO-type reconstructions give a closed-form
polynomial that can be evaluated anywhere in the cell, an advantage over
WENO for the space–time Gaussian quadrature of source terms, because
WENO's linear weights at generic Gauss points are not trivial to
obtain (§7.1).

## Two-dimensional Riemann problem

[Pazner (2021)](/sources/pazner-2021.md) §5.5 solves
$\partial_tu+\nabla\cdot(\tfrac12u^2(1,1))=0$ on $[0,1]^2$ with quadrant
values $-1$ ($x>0.5$, $y>0.5$), $-0.2$ ($x\le0.5$, $y>0.5$), $0.5$
($x\le0.5$, $y\le0.5$) and $0.8$ ($x>0.5$, $y\le0.5$), the exact solution
imposed on the boundary, to $t=0.5$. With $120^2$ degrees of freedom as
$N=2$, $5$, $11$ on $40^2$, $20^2$, $10^2$ elements, and a reference with
$N=1$ on $512^2$ elements, Pazner's subcell
[convex-limited](/methods/convex-limiting.md) DG resolves the solution
well even on the coarsest mesh and captures discontinuities that are
not aligned with element boundaries (Fig. 11). The same quadrant values
and final time are run by [Peng, Sun & Wu (2024)](/sources/peng-2024.md)
Ex. 5.11 on $256^2$ cells, recorded with the Euler configurations on
[two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md).

## Euler data that reduce to Burgers

For $\gamma=3$ the isentropic data $p=\rho^\gamma$, $v=\sqrt\gamma\,\rho$
make the sound speed $c=\sqrt{\gamma p/\rho}=\sqrt3\,\rho$ equal to $v$.
The Riemann invariant $v-c$ is then identically zero, and the other,
$v+c=2\sqrt3\,\rho$, is transported at its own speed $v+c$, so it obeys
Burgers' equation *(compiler check, not in the sources)*. The sources
use this to obtain exact smooth Euler solutions:

- [Zheng, Shu & Qiu (2021)](/sources/zheng-2021.md) Ex. 1: $\gamma=3$,
  $\rho=(1+0.2\sin x)/(2\sqrt\gamma)$, $v=\sqrt\gamma\rho$, $p=\rho^\gamma$
  on periodic $[0,2\pi]$; $2\sqrt\gamma\rho$ solves Burgers with data
  $1+0.2\sin x$, smooth until $t=5$, and the run stops at $t=3$. An
  artificial material interface between identical fluids starts at
  $x=\pi$ with their full interface algorithm active; the density
  converges at fifth order, $L^1$ error $1.05\times10^{-5}$ at 80 points to
  $1.07\times10^{-8}$ at 320 (order 5.14; Table 2). Ex. 8 is the 2D
  analogue, $\rho=(1+0.2\sin((x+y)/2))/\sqrt{2\gamma}$,
  $v_1=v_2=\sqrt{\gamma/2}\,\rho$ on $[0,4\pi]^2$ with an artificial
  circular interface, $t=3$: $9.57\times10^{-6}$ at $80^2$ to
  $1.24\times10^{-8}$ at $320^2$ (order 5.06; Table 4).
- [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) Ex. 3.3–3.4 use the
  same data with the factors printed as $2\sqrt3$ and $\sqrt6$, which
  equal $2\sqrt\gamma$ and $\sqrt{2\gamma}$ only for $\gamma=3$, a value they
  do not state *(compiler check, not in the sources)*; exact solution taken from their
  earlier paper; $t=3$. M5-I reaches $1.69\times10^{-12}$ at 320 cells
  (order 6.03) and $4.67\times10^{-11}$ at $320^2$ (6.49), M5-NI again
  about fifth order (Tables 3.3–3.4).

The breaking time of $1+0.2\sin x$ is $1/0.2=5$ *(compiler check, not
in the sources)*, matching Zheng et al.'s statement.

[Wang et al. (2026)](/sources/wang-2026.md) §6.2 use the general-$\gamma$
version of the construction, a simple wave: on periodic $[0,1]$,
$\gamma=1.4$, $v=\tfrac2{\gamma+1}V(x)$ with
$V(x)=\sin(2\pi x)/(2\pi t_{\mathrm s})$,
$\rho=\rho_\infty\big[1+\tfrac{\gamma-1}2\tfrac{v}{c_\infty}\big]^{2/(\gamma-1)}$,
$p=p_\infty\big[1+\tfrac{\gamma-1}2\tfrac{v}{c_\infty}\big]^{2\gamma/(\gamma-1)}$,
$\rho_\infty=0.1$, $p_\infty=1$, $c_\infty=\sqrt{\gamma p_\infty/\rho_\infty}$,
shock formation at $t_{\mathrm s}=1$ ($t_{\mathrm s}$, $V$ and the
far-field sound speed $c_\infty$, their $a_\infty$, page-local), run to $4t_{\mathrm s}$; they call it the
"acoustic wave problem" (isentropic Euler–Burgers coupling). With
$c=c_\infty+\tfrac{\gamma-1}2v$ the invariant $v-2c/(\gamma-1)$ is
constant and $v+c=c_\infty+V$ is transported at its own speed, so it
obeys Burgers' equation and breaks at $t_{\mathrm s}$ *(compiler check,
not in the sources)*. On a two-level AMR grid (base $N=64$, ratio 2,
seven coarse–fine interfaces, reference uniform $N=512$) the periodic
shock crosses the interfaces repeatedly: WENO and hybrid WENO inter-level
interpolation keep the shock in the right place when flux correction
is applied, while WENO interpolation without flux correction shows
significant artifacts (Fig. 10; see
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)). On
the same problem their $L_1(\rho)=0.001590$ and
$L_\infty(\rho)=0.003035$ do not change over the tested thresholds of
their troubled-cell indicator, the maximum share of troubled cells
going from 5.6338 % to 0 % (Table 4).

## Qualifications

- Li, Shu & Qiu caption the Burgers figures "density" and call the
  unknown $\mu$, the letter of the velocity in their Euler examples.
- Their M5-I orders 8.85 and 8.72 at 40 and 80 cells (Table 3.1)
  exceed the design order six and are not commented on.
- Puppo et al.'s Table 1 prints a rate on the first row of each
  sub-table, against a coarser grid that is not listed; their Fig. 7
  caption gives $t=5$ for a test that ends at $t=0.5$.
- Cicchino et al. write that "all schemes yield the expected
  convergence rates" of $N+1$ (their "$p+1$"), while their split form with $c_+$ at
  $N=5$ gives 5.70–5.76 (Tables 5, 7); they define $c_+$ as the value at
  which an order is about to be lost, which explains the rates but not
  the sentence.
- Yu & Hesthaven print the flux as $f=u^2$, not $u^2/2$, a scaling that
  doubles the wave speeds against the other sources.
- Huang & Zahr print the initial condition (78) as
  $\mu_1H(-z)-\mu_2H(z)$, a constant right state $-3$, which would move
  the shock at the constant speed $(4-3)/2=1/2$; their exact solution
  (79) and shock path (80), consistent with each other, start instead
  from $\mu_2(z-1)$ for $z>0$ *(compiler check, not in the sources)*.
  Their Table 2 caption says the slopes "tend to at least the optimal
  rate ($p+1$)", while the final $E_\phi$ slopes for $p=2,3$ are 2.88
  and 3.73; the printed slopes agree with the printed errors and mesh
  sizes ($\ln(6.36/0.866)/\ln(3.63/1.81)=2.87$) *(compiler check, not
  in the sources)*.
- Naudet & Zahr's Eq. (47) prints the same initial condition
  $\mu_1H(-z)-\mu_2H(z)$ as Huang & Zahr's (78), again inconsistent with
  their exact solution (48) and path (49), which are consistent with each
  other and satisfy the Rankine–Hugoniot speed *(compiler check, not in
  the sources)*; their §5.1.1 calls $x_s$ "the shock speed", whereas
  (48)–(49) use it as the shock position.
- Kolluru et al.'s optimal parameters $\alpha_{\mathrm{SR}}=0.7$ (SR) and $0.65$ (SP)
  lie outside the range $1<\alpha_{\mathrm{SR}}<2$ of the convergence proof they cite;
  they attribute the convergence to initial-data-specific "compensation
  mechanisms" not covered by the theory (§3.2). Their Fig. 4 computes
  orders from $L^\infty$ errors, while the surrounding text and Table 1
  use $L^1$ and $L^2$.
- Lin & Zhu pair their fifth-order scheme with third-order TVD
  Runge–Kutta at CFL 0.6 and report fifth-order rates without saying
  whether $\Delta t$ was reduced in the accuracy test.
- Calhoun et al. print the refinement criterion as
  $(q_{i,j+1}-q_{i,j+1})/(2\Delta y)\ge15$ (their $q$ is $u$), which is
  identically zero, next to the centred
  $(q_{i+1,j}-q_{i-1,j})/(2\Delta x)\ge15$ for $x$, so the $y$-criterion
  read as the centred difference $q_{i,j+1}-q_{i,j-1}$ is the
  non-trivial one; both are printed without absolute values. They are
  read in the arXiv v2 preprint.
- Fan et al. (2025a) print HWENO-M's $L^\infty$ errors and orders at
  $160^2$, $200^2$ and $240^2$ in Table 4 identical to HWENO-U's
  ($7.18\times10^{-8}$, $2.38\times10^{-8}$, $9.52\times10^{-9}$), while
  the $L^1$ errors of the two schemes differ; the paper does not say
  whether the coincidence is real.
- Vilar & Abgrall's Fig. 28 caption gives 576 cells for the uncorrected
  sixth-order solution that the text places on 242 cells; they also
  write that the dimension of $\mathbb P^5$ is 20, whereas their own
  count $(k+1)(k+2)/2$ gives 21 subcells for $k=5$.
- The accuracy tests of Zheng et al. use $\Delta t=O(\Delta x^{5/3})$;
  the other sources' accuracy runs state CFL 0.6 with a reduced time
  step (Li, Shu & Qiu) or prescribed multiples of $h$ (Puppo et al.).

# Citations

- [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) — Ex. 3.1–3.4, Tables 3.1–3.4, Figs. 3.1–3.2 (arXiv v1).
- [Fan, Zhao, Xiong & Qiu (2023)](/sources/fan-2023.md) — Ex. 3.1, Table 3.1, Fig. 3.1, Remark 3.1.
- [Huang & Zahr (2022)](/sources/huang-2022.md) — §6.2.1–6.2.2, Eqs. (78)–(80), Table 2, Figs. 17–22 (arXiv v2).
- [Puppo, Semplice & Visconti (2023)](/sources/puppo-2023.md) — §4.1, §4.3, Table 1, Figs. 1, 4–9 (arXiv v2).
- [Pazner (2021)](/sources/pazner-2021.md) — §5.5, Fig. 11 (arXiv v1).
- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) — Ex. 5.11 (arXiv v1).
- [Zheng, Shu & Qiu (2021)](/sources/zheng-2021.md) — §4, Ex. 1 and Ex. 8, Tables 2 and 4.
- [Cicchino, Nadarajah & Del Rey Fernández (2022)](/sources/cicchino-2022.md) — §4.1–4.2, Tables 1–7 (arXiv v1).
- [Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) — §5.1.1, Fig. 1 (arXiv v2).
- [Yu & Hesthaven (2022)](/sources/yu-2022.md) — §5.2, Figs. 5–6.
- [Sousa & Scalo (2022)](/sources/sousa-2022.md) — §2.3, Fig. 1 (arXiv v2).
- [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) — Example 2.12; §4.1, Eq. (44) (arXiv v4).
- [Qin et al. (2023)](/sources/qin-2023.md) — §3.2, Table 11, Figs. 3–4.
- [Zhong et al. (2023)](/sources/zhong-2023.md) — §4.1, Ex. 5, Table 6, Fig. 3.
- [Calhoun, Chudzik & Helzel (2023)](/sources/calhoun-2023.md) — §2.2, §4.4, Eqs. (7)–(10), (30), Fig. 12 (arXiv v2).
- [Kolluru et al. (2024)](/sources/kolluru-2024.md) — §2.2, §3.1–3.2, Tables 1–4, Figs. 3–4, 7, 10 (arXiv v2).
- [Lin & Zhu (2024)](/sources/lin-2024-b.md) — §3, Case 3.1, Table 3.2.
- [Naudet & Zahr (2024)](/sources/naudet-2024.md) — §5.1.1–5.1.3, Eqs. (46)–(51), Figs. 9–14.
- [Zhang & Zhu (2024)](/sources/zhang-2024-c.md) — §3, Ex. 3.1–3.2, Table 3.2, Figs. 3.1–3.4.
- [Fan et al. (2025a)](/sources/fan-2025.md) — §3.1, Ex. 3.1 and 3.3, Tables 1–2, 4–5.
- [Danis et al. (2025)](/sources/danis-2025.md) — §5.2, Table 2 (arXiv v1).
- [Vilar & Abgrall (2024)](/sources/vilar-2024.md) — §3.4, §4.2.1, Figs. 5–9, 28–32 (HAL preprint).
- [Abgrall et al. (2026)](/sources/abgrall-2026.md) — §1, §4, Ex. 2, Fig. 2.
- [Yajaman, Toro & Demattè (2025)](/sources/yajaman-2025.md) — §7.1, Eqs. (57)–(60), Table 3, Fig. 12.
- [Duan, Barsukow & Klingenberg (2025)](/sources/duan-2025.md) — §2.1, Ex. 5.1, 5.5, Figs. 3, 8 (arXiv v3).
- [de Romémont et al. (2026)](/sources/deromemont-2026.md) — §6, §6.1, App. B, Figs. 5–6.
- [Cao et al. (2026)](/sources/cao-2026.md) — Ex. 6.1, Table 1; Ex. 6.12, Fig. 13; Thm. 2.1.
- [Liu et al. (2026)](/sources/liu-2026.md) — §5.1.1, §5.1.4, §5.2.1, §5.2.4, Figs. 5.1–5.3, 5.10–5.11 (arXiv v1).
- [Wang et al. (2026)](/sources/wang-2026.md) — §6.2, Fig. 10, Table 4.
