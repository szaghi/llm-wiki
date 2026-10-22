---
type: Benchmark
title: "Sod and Lax shock tubes"
description: "The two most often run one-dimensional Euler Riemann problems with exact solutions, Sod's mild tube and Lax's stronger one, run by most sources as the first check of shock and contact capturing; records each source's placement, grid and final time, the printed variants and the multicomponent, stiffened-gas and relaxation relatives."
status: established
aliases: [Sod problem, Sod shock tube, Lax problem, Lax shock tube, Riemann problem of Lax, Lax–Harden problem]
tags: [benchmark, weno, teno, riemann-solver]
timestamp: 2026-10-22T18:00:00Z
---

# Sod and Lax shock tubes

Both are one-dimensional Riemann problems of the Euler equations with
$\gamma=1.4$: two constant states separated by a diaphragm at the
middle of the tube. Each has an exact solution containing a shock and
a contact discontinuity, so the benchmark checks whether a scheme
captures both sharply and without oscillation, before harder problems
are attempted. Lax's data start with a moving left state;
[Huang et al. (2026)](/sources/huang-2026.md) §6.3 describe the problem
as testing a strong shock and contact.

## Sod

$(\rho,v,p)=(1,0,1)$ on the left half of $[0,1]$ and $(0.125,0,0.1)$ on
the right half.

| Source | Grid | Final time | Notes |
|---|---|---|---|
| [Fu (2021)](/sources/fu-2021.md) §5.3 | 96 points | 0.2 | exact Riemann reference; [TENO-AA](/methods/adaptive-teno.md) |
| [Takagi et al. (2022)](/sources/takagi-2022.md) §4.3 | 100 | 0.2 | exact reference; [TENO-THINC](/methods/teno-thinc.md) |
| [Ye et al. (2022)](/sources/ye-2022.md) §4.3, Eq. (43) | 200 | 0.2 | mirrored: $(0.125,0,0.1)$ on the left, $(1,0,1)$ on the right; [AFTENO](/methods/afteno.md) |
| [Deng (2023)](/sources/deng-2023.md) App. A.4 | 200 cells | 0.25 | [ROUND](/methods/round-scheme.md), NewWENO |
| [Abgrall & Barsukow (2023)](/sources/abgrall-2023.md) §3.5.3, §5.6 | 100 | 0.1 | [Active Flux](/methods/active-flux.md); states and $\gamma$ not printed |
| [Pazner (2021)](/sources/pazner-2021.md) §5.2.1 | 256 DOFs, $N=0,1,3,7$ ($N=7$ on 32 elements) | 0.18 | on $[-\tfrac12,\tfrac12]$; sparse IDP DG with subcell [convex limiting](/methods/convex-limiting.md) |
| [Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md) §IV.A | 8 space–time quadrilaterals | 0.2 | on $(-0.5,0.5)$; [MDG+ICE shock tracking](/methods/implicit-shock-tracking.md), $\mathbb P^1$–$\mathbb P^3$ |
| [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) §4.2, Eq. (41) | 200 points | 0.2 | on $[-0.5,0.5]$ (from Fig. 3), $\Delta t=5\times10^{-4}$; ninth-order central scheme with adaptive [artificial dissipation](/methods/artificial-viscosity.md) |
| [Bezgin et al. (2022)](/sources/bezgin-2022.md) §4.2, Eq. (29) | 200 | 0.2 | finite-volume [WENO3-NN](/methods/learned-weno-weights.md), LLF, characteristic, TVD-RK3 at CFL 0.6 |
| [Hiejima (2022)](/sources/hiejima-2022.md) §3.1, Eq. (26) | 101 points ($101\times21\times21$) | 0.2 | on $[-0.5,0.5]$; [WCNS](/methods/weighted-compact-nonlinear-scheme.md) of interpolation order 5–11, AUSMDV |
| [Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) §5.2.1 | $\mathbb P_3$ on 50 and $\mathbb P_9$ on 20 elements (200 DOFs); $N=20$–$160$ for $\mathbb P_2$–$\mathbb P_7$ | 0.2 | [artificial viscosity](/methods/artificial-viscosity.md) from the temporal residual, $c_\mu=5$ (arXiv v2) |
| [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) §5.1.1 | $\mathbb P_3$, $\mathbb P_5$ at about 200 DOFs; $N=40$–$640$ ($L^1$), $20$–$320$ ($L^2$), and $M=100$–$1600$ DOFs, $\mathbb P_2$–$\mathbb P_7$ | 0.2 | flux reconstruction with [entropy filtering](/methods/entropy-filtering.md) (arXiv v3) |
| [Yu & Hesthaven (2022)](/sources/yu-2022.md) §5.3.1 | 100 elements | 0.2 | nodal DG with ANN-predicted artificial viscosity |
| [Sousa & Scalo (2022)](/sources/sousa-2022.md) §5.1 | grid study (grids not printed in the text) | 0.2 | diaphragm at $x=0$; Dirichlet left, Neumann right; compact central scheme with [quasi-spectral viscosity](/methods/quasi-spectral-viscosity.md) vs localized artificial diffusion; $\gamma$ not printed (arXiv v2) |

Abgrall & Barsukow run Sod with three Active Flux variants: sixth order
at CFL 0.25 (Fig. 19); a fifth-order point setup with a third-order
evolution operator at CFL 0.5 (Fig. 24); and seventh order at CFL 0.01
on a periodic tube with discontinuities at $x=1/3$ and $x=2/3$ (Fig. 28),
which doubles the problem so that periodic boundaries can be used.
Pazner, Luo et al., Hiejima and Sousa & Scalo place the diaphragm at
$x=0$ (of a tube centred on the origin, for the first three), a shift
of the $[0,1]$ placement. Sousa & Scalo also run a "mirrored Sod" tube
on the periodic interval $[-1,1]$, with $(1,0,1)$ for $|x|<0.5$ and
$(0.125,0,0.1)$ elsewhere, to $t=0.2$ with a Fourier pseudo-spectral
method on 64 to 512 points, used to calibrate their model constants
(App. A); like Abgrall & Barsukow's doubled tube, it makes the problem
periodic.

## Lax

$(\rho,v,p)=(0.445,\ 0.698,\ 3.528)$ on the left and $(0.5,\ 0,\ 0.571)$
on the right. Three placements coexist: $[0,1]$, its shift
$[-\tfrac12,\tfrac12]$, and $[-5,5]$.

| Source | Domain | Grid | Final time | Notes |
|---|---|---|---|---|
| [Fu (2021)](/sources/fu-2021.md) §5.3 | $[0,1]$ | 96 | 0.14 | right pressure printed $0.5710$ |
| [Takagi et al. (2022)](/sources/takagi-2022.md) §4.3 | $[0,1]$ | 100 | 0.14 | same |
| [Deng (2023)](/sources/deng-2023.md) App. A.5 | $[0,1]$ | 200 cells | 0.16 | |
| [Huang et al. (2026)](/sources/huang-2026.md) §6.3 | $[0,1]$ | 200 cells | 0.15 (text) / 0.16 (Fig. 8) | ROUND, LD-ROUND, [WENO3-NN](/methods/learned-weno-weights.md) |
| [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) Ex. 3.5 | $[-0.5,0.5]$ | 200 cells | 0.16 | moment-based [multi-resolution HWENO](/methods/hermite-weno.md); troubled cells shown in the $x$–$t$ plane |
| [Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md) §IV.B | $(-0.5,0.5)$ | 8 space–time quadrilaterals | 0.15 | printed $(0.445,\ 0.698876404,\ 3.52773)$; called the "Lax–Harden" problem |
| [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) §4.2 | $[-0.5,0.5]$ | 200 | 0.13 | $\Delta t=10^{-3}$ |
| [Li et al. (2022)](/sources/li-2022-b.md) §4.3.1, Eq. (39) | $[-5,5]$ | 200 | 1.3 | zero-gradient BCs, CFL 0.5; reference fifth-order WENO-Z with 4000 points |
| [Luo & Wu (2021)](/sources/luo-2021-b.md) §5.2.4, Eq. (16) | $[-5,5]$ | 101 | 1.3 | CFL 0.5 |
| [Peng, Sun & Wu (2024)](/sources/peng-2024.md) Ex. 5.6 | $[-5,5]$ | 256 cells | 1.3 | outflow; data scaled by $\lambda\in\{1,0.01,100\}$ |
| [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) Ex. 4.2, Eq. (4.1) | $[-5,5]$ (figures) | 200 cells | 1.3 | positivity-preserving hybrid [HWENO](/methods/hermite-weno.md), Navier–Stokes at $\mathrm{Re}\in\{100,1000,10^4,\infty\}$ |
| [Wang & Don (2022)](/sources/wang-2022-b.md) §3.2.3 | specifications deferred to an earlier paper | | | affine-invariant weights, data scaled |
| [Bezgin et al. (2022)](/sources/bezgin-2022.md) §4.2, Eq. (30) | $[0,1]$ | 200 | 0.14 | right pressure printed $0.5710$ |
| [Hiejima (2022)](/sources/hiejima-2022.md) §3.2, Eq. (27) | $[-0.5,0.5]$ | 101 | 0.14 | right pressure printed $0.5710$ |
| [Yu & Hesthaven (2022)](/sources/yu-2022.md) §5.3.1 | $[0,1]$ (stated for Sod) | 100 elements | 0.13 | |

The $[-5,5]$ placement at $t=1.3$ corresponds to the $[0,1]$ placement
at $t=0.13$ under the scaling $x\mapsto(x+5)/10$, $t\mapsto t/10$
*(compiler check, not in the sources)*; Sciacovelli et al. stop at
exactly that time, whereas the other $[0,1]$ and $[-\tfrac12,\tfrac12]$
runs stop later, at $0.14$ to $0.16$, so the families compare slightly
different wave positions.

Luo et al.'s digits are those of the conserved state
$(\rho,\rho v,E)=(0.445,\ 0.311,\ 8.928)$ converted with $\gamma=1.4$:
$0.311/0.445=0.698876$ and $0.4\,(8.928-\tfrac12\cdot0.311\cdot0.698876)=3.52773$;
the other sources print the same state rounded *(compiler check, not in
the sources)*.

## Findings across sources

**Contact resolution separates the schemes.** On Sod all schemes agree
with the exact solution, and differences lie at the contact: AFTENO best
and AFWENO-Z better than AFWENO-JS (Ye et al., Fig. 3); TENO-THINC
shocks as sharp as WENO5-Z and TENO5, contacts better resolved (Takagi
et al., Figs. 4–5, also for Lax). Pazner finds that at a fixed 256
degrees of freedom a higher polynomial degree on a coarser mesh
resolves the discontinuities somewhat better, especially the contact,
with $N=3$ and $N=7$ largely indistinguishable (Fig. 7). Sciacovelli et
al. attribute the smearing of their contact to the high-order
dissipation alone, since their shock sensor switches the low-order
term off at the contact, where the pressure is constant (§4.2, Fig. 3).
On Lax, WENO-ZN reduces the dissipation near the shock (Li et al.,
Fig. 4); WENO-Z+M improves shock and contact markedly over WENO-Z and
WENO-Z+, is less oscillatory than WENO-IS-I, while ninth-order WENO-Z9
is less dissipative but more oscillatory (Luo & Wu, Fig. 12). Deng finds
NewWENO less dissipative than WENO-P on both tubes (Fig. 15). Li, Shu &
Qiu report that modifying the first moment in troubled cells gives
"much better resolutions and sharper shock transitions" than the
unmodified sixth-order HWENO on Lax and on their five other shock tests
(Ex. 3.5, Fig. 3.3, comment p. 31).

**Three-point and very-high-order reconstructions.** Bezgin et al.'s
learned three-point WENO3-NN has a lower $L_1$ error than fifth-order
WENO5-JS on both tubes, with $L_1=L_1^\rho+L_1^v+L_1^p$: on Sod
$1.035\times10^{-2}$ (WENO3-NN2) against $1.106\times10^{-2}$ (WENO5-JS)
and $1.636\times10^{-2}$ (WENO3-JS), on Lax $2.416\times10^{-2}$ against
$2.590\times10^{-2}$ and $3.949\times10^{-2}$; WENO5-Z is best on both
(App. A.6, Table 4). On Lax WENO3-NN2 shows a slight velocity overshoot,
as WENO5-JS does (§4.2, Fig. 9). Hiejima finds that his WCNS with
Jiang–Shu weights suppresses oscillations at the Sod shock "even for
the eleventh-order accuracy", whereas the TENO-type weights give a
slight undershoot at the shock and a slight overshoot at the contact
that grow with the order (§3.1, Fig. 2). On Lax the two weightings
differ little, the TENO-type one being slightly better at the contact;
every run overshoots in velocity near $x=-0.25$, a point where the
solution is continuous but not differentiable, and with the cut-off
$C_T=10^{-7}$ the plateau between shock and contact oscillates, which
Hiejima states without a figure (§3.2, Fig. 3).

**Element methods: localization and convergence rate.** For Sod at
200 DOFs, Dzanic, Trojak & Witherden find the artificial viscosity of
the density localized at the shock, with minimal dissipation at the
rarefaction and the contact (§5.2.1, Fig. 4). The $L^1$ density error
converges at first order, rates 0.92, 1.02, 0.87, 0.95, 0.99, 0.85 for
$\mathbb P_2$–$\mathbb P_7$ on 20 to 160 elements, with a marginally lower error at higher order
for fixed DOFs (Table 1). Dzanic & Witherden's entropy filter gives the
same first order, $L^1$ rates 0.91, 0.94, 0.93, 0.92, 0.87, 0.86 and
$L^2$ rates 1.05, 0.98, 1.01, 1.01, 0.98, 1.03 against $N$ (Tables 1–2);
at fixed DOFs the lower order gives a marginally lower error, which
they attribute to more elements and hence a more localized filter
(Tables 3–4, Fig. 2), with minimal smearing of the contact. The two
fixed-DOF trends are opposite but marginal, and belong to two different
shock-capturing devices. Yu & Hesthaven
report spurious oscillations suppressed on both tubes with 100
elements (§5.3.1, Figs. 7–8).

**Explicit viscosity for a central scheme.** Sousa & Scalo find their
quasi-spectral viscosity and localized artificial diffusion both
converge under refinement on Sod, the former giving slightly sharper
discontinuities on equal grids; localized artificial diffusion needs an
explicit Padé filter ($\alpha=0.495$), the quasi-spectral viscosity does
not, although an optional filter ($\alpha=0.499$) attenuates residual
high-wavenumber oscillations (§5.1, Fig. 4).

**Shock tracking instead of capturing.** Luo, Absillis & Nourgaliev fit
the shock and the contact as true discontinuities of a space–time mesh
of eight quadrilaterals, six of them degenerate at the diaphragm, and
place the rarefaction head and tail "virtually exactly" with
$\mathbb P^2$ and $\mathbb P^3$ (Figs. 8–11). Their $L^2$ density error
falls, from $\mathbb P^1$ to $\mathbb P^3$, as
$\log_{10}\|\rho-\rho_{\mathrm e}\|=-2.82,\ -4.36,\ -5.67$ on Sod
(slopes 8.75 and 10.48 against $\log_{10}(1/\sqrt{\mathrm{DOFs}})$) and
$-3.38,\ -4.54,\ -5.59$ on Lax (slopes 6.59 and 8.44), which they call
exponential $p$-convergence (Table 1 and the second Table 1); no
shock-capturing scheme is run for comparison. See
[implicit shock tracking](/methods/implicit-shock-tracking.md).

**Robustness of Hermite WENO at high Reynolds number.** Fan, Zhang &
Qiu run the Lax tube for the compressible Navier–Stokes equations. A
non-hybrid HWENO built on the first two moments, without moment
limiter or positivity limiter, is non-oscillatory at $\mathrm{Re}=100$
but oscillates and loses stability at larger $\mathrm{Re}$ and for
Euler (Fig. 4.1). Their positivity-preserving hybrid HWENO is
non-oscillatory, flags 2.43 % ($\mathrm{Re}=1000$) and 2.68 %
($\mathrm{Re}=\infty$) of the cells as troubled, and never triggers its
positivity limiter, so they attribute the stability on this problem to
the first-moment limiter; a small velocity dent is a numerical artifact
also seen in an earlier finite-volume WENO (Fig. 4.2, Table 4.2).

**Scale invariance.** Scaling the Lax data by a factor $\lambda$
(page-local symbol) exposes schemes
whose weights depend on the magnitude of the data: OEDG is exactly
scale-invariant, whereas the earlier OFDG smears at $\lambda=100$,
oscillates at $\lambda=0.01$ and undershoots near the shock even at
$\lambda=1$ (Peng et al., Fig. 3). Wang & Don find affine-invariant Z-
and D-type weights essentially identical and non-oscillatory on Lax and
the [123 problem](/benchmarks/double-rarefaction-problem.md) (Fig. 7).
Deng recalls, from an earlier study, that
WENO-Z with $\epsilon=10^{-12}$ and WENO-JS with $\epsilon=10^{-6}$
oscillate on Sod scaled by $\lambda=10^{-7}$ (§1). See [scale invariance](/properties/scale-invariance.md).

## Relatives of the two tubes

The Sod data recur, unchanged or nearly so, in models other than the
single-gas Euler equations.

- **Gas mixtures.** Sciacovelli et al. run both tubes for a single
  species and for an N$_2$ (79 %)–O$_2$ (21 %) mixture and find the two
  solutions superposed (§4.2, Fig. 3). [Renac (2021)](/sources/renac-2021.md)
  §7.2 calls "RP1" a Sod-like problem of the
  [two-component Euler equations](/definitions/multicomponent-euler-equations.md):
  $(Y_1,\rho,v,p)=(0.5,1,0,1)$ and $(0.5,0.125,0,0.1)$, with
  $Y_1$ the mass fraction of component 1, $\gamma_1=1.5$, $\gamma_2=1.3$,
  unit heat capacities, $t=0.2$, entropy-stable DGSEM with $N=3$ on 100
  cells; shocks and contacts are well captured (Figs. 3–4).
- **Stiffened gas and three dimensions.** [Li, Duan & Tang (2022)](/sources/li-2022-c.md)
  run a quasi-two-dimensional [stiffened-gas](/definitions/stiffened-gas-equation-of-state.md)
  tube, $(\rho,v_1,v_2,p)=(1,0,0,1)$ and $(0.75,0,0,0.05)$ with
  stiffening pressure 1 and $\gamma=3$, on $100\times5$ cells to
  $t=0.15$, where their [adaptive moving mesh](/methods/adaptive-moving-mesh.md)
  with multi-resolution WENO beats the uniform mesh with three times as
  many cells near the rarefaction head and the contact (Ex. 5.2,
  Fig. 5.3). Their Ex. 5.6 is a spherical Sod problem, the Sod states
  inside and outside the sphere $r<0.5$ in $[0,1]^3$, $t=0.2$, with a
  second-order TVD solution of the one-dimensional spherical equations
  on 8000 cells as reference: the moving mesh with $100^3$ cells gives
  results comparable to a uniform $200^3$ mesh at 37.2 % of its CPU time
  (Table 5.2).
- **Relaxation and gravity.** [Arun, Krishnan & Samantaray (2022)](/sources/arun-2022.md)
  §5.1 solve the barotropic Euler equations with gravity ($\phi(x)=x$)
  and stiff friction relaxation for the Sod densities
  $(\rho,v)=(1,0)$, $(0.125,0)$ on $[0,1]$ to $t=0.2$, CFL 0.45, $\gamma$
  not printed. In the compressible regime the solution converges under
  refinement (100 and 1000 cells, Fig. 1); in the stiff regime it
  matches a first-order porous-medium solver in the parabolic scaling
  and a first-order upwind transport solver in the hyperbolic one
  (Fig. 2). See [asymptotic preservation](/properties/asymptotic-preservation.md).
- **Two-fluid and multispecies tubes.** [Nguyen et al. (2022)](/sources/nguyen-2022.md)
  §3.2 run the Sod states as a gas–gas two-fluid tube, the left gas
  with $\gamma=1.4$ and the right one with $\gamma=1.667$, interface at
  $x=0.5$ of $[0,1]$, on 100 to 800 cells to $t=0.2$ at CFL 0.9 against
  the exact solution; they report no spurious oscillation in pressure,
  density or velocity, and grid convergence (Figs. 6–9). A
  hydrogen–oxygen–argon tube of molar ratio 2:1:7, with
  $(T,v,p)=(400\ \mathrm K,0,8000\ \mathrm{Pa})$ on the left and
  $(1200\ \mathrm K,0,80000\ \mathrm{Pa})$ on the right, to
  $t=40\,\mu$s, is run without reactions by two sources:
  [Peng, Atkins & Deiterding (2022)](/sources/peng-2022.md) §3.2 on a
  $100\times50$ mm tube with the diaphragm at $x=50$ mm, slip walls and
  three levels of [adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)
  down to 0.25 mm, whose results on several meshes agree with two
  earlier computations (Fig. 6); and
  [Du & Yang (2022)](/sources/du-2022-b.md) Ex. 6.3 on a 10 cm domain
  with bound-preserving LDG, $k=2$, 400 cells and a 5000-cell
  reference, whose code blows up without the bound-preserving limiter
  (Fig. 6.3). Du & Yang also run a He/N$_2$ tube, $(T,v,p,Y_1,Y_2)=(300\
  \mathrm K,0,10\ \mathrm{atm},1,0)$ for $x\le0.4$ m and $(300\ \mathrm
  K,0,1\ \mathrm{atm},0,1)$ beyond, on 1000 cells to $t=300\,\mu$s, where
  without the limiter $Y_2$ turns negative within $0.5085\,\mu$s and the
  code blows up (Ex. 6.2, Figs. 6.1–6.2). See
  [multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)
  and [bound preservation](/properties/bound-preservation.md).
- **Radial Sod in two dimensions.** [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md)
  §4 (arXiv v4) run $(\rho,v_1,v_2,p)=(1,0,0,1)$ for $r\le0.5$ and
  $(0.125,0,0,0.1)$ for $0.5<r\le1$, CFL 0.25, $t=0.25$, with
  deferred-correction residual distribution on triangles. The
  uncorrected continuous-Galerkin scheme with jump stabilization breaks
  down at $t\approx0.16$; with their
  [entropy correction term](/methods/entropy-correction-term.md) it runs
  to $t=0.25$, the two correction variants being indistinguishable
  without zoom (Figs. 1–2). The three-dimensional spherical version of
  Li, Duan & Tang is listed above.
- **Relativistic tubes.** [Chen & Wu (2022)](/sources/chen-2022-b.md)
  Exs. 4.2–4.5 (arXiv v1) run quasi-one-dimensional
  [relativistic](/definitions/relativistic-hydrodynamics.md) Riemann
  problems on thin strips of triangles: $(\rho,v_1,v_2,p)=(1,-0.6,0,10)$
  against $(10,0.5,0,20)$ (two rarefactions and a contact, $t=0.4$);
  $(1,0,0,10^4)$ against $(1,0,0,10^{-8})$ ($t=0.45$, a thin shell between
  shock and contact; without the physical-constraint-preserving limiter
  the run fails within a few steps); and $(10^2,0,0,10^4)$ against
  $(10^2,0,0,10^2)$, rerun with $\rho$ and $p$ scaled by $10^{-2}$ and
  $10^{-4}$. On the scaled problem their scale-invariant weights keep
  $\rho^{(\zeta)}_h-\zeta\rho_h$ (with $\zeta$ the page-local scaling
  factor) at $O(10^{-12})$–$O(10^{-13})$, whereas the original Zhu–Qiu
  weights give $O(10^{-1})$ and $O(10^{-2})$ and overshoot (Ex. 4.4,
  Figs. 6–8), the relativistic counterpart of the Lax scaling test
  above.
- **Gas–liquid tubes.** [Wong et al. (2021)](/sources/wong-2021.md) §6.3
  run a water–air "Sod" problem with pressure ratio $10^9/10^5$;
  [Nguyen et al. (2022)](/sources/nguyen-2022.md) §3.2 an air–water tube
  with the same ratio; [Bai & Li (2022)](/sources/bai-2022.md) §3.1
  air–helium and water–air tubes with a sharp-interface DG method. They
  belong with the [gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md).

## Qualifications

- Luo & Wu print the left Lax pressure as $0.3528$ (Eq. (16)), where
  Fu (2021), Takagi et al., Li et al., Deng, Huang et al., Peng et
  al., Li, Shu & Qiu, Fan et al. and Sciacovelli et al. print $3.528$;
  the paper's text does not show which value was run.
- Huang et al. give $t=0.15$ in the text and $t=0.16$ in the caption of
  Fig. 8.
- Wang & Don's figure of the unscaled tubes includes the Lax problem,
  although their §3.2.3 text list omits it.
- Li et al. compute the Lax reference with fifth-order WENO-Z, the
  other references of the paper with seventh order.
- Fan et al. print both Lax states on "$x\in[0,5)$" and "$x\in[0,5]$"
  (Eq. (4.1)); their figures show $[-5,5]$, so the left state belongs on
  $[-5,0)$. Their text gives CPU savings of the hybrid scheme of 77.68 %
  and 75.08 % "as shown in Table 4.2", whose entries are 71.20 %
  ($\mathrm{Re}=1000$) and 69.98 % ($\mathrm{Re}=\infty$).
- Luo, Absillis & Nourgaliev write "profiles at $t=0.2$" for the Lax
  problem, whose space–time domain ends at $t=0.15$, the time in their
  figure captions.
- Li, Shu & Qiu do not print $\gamma$ for the Lax problem, Arun et
  al. not for their tube, Sousa & Scalo not for Sod.
- Dzanic & Witherden's $L^2$ errors are smaller than their $L^1$ errors
  throughout (e.g. $1.21\times10^{-3}$ against $6.87\times10^{-3}$ at
  $M=100$, $\mathbb P_2$, Tables 3–4), while their printed definitions
  (Eq. (28)), $\frac1M\sum\lvert e_i\rvert$ and
  $\sqrt{\frac1M\sum e_i^2}$ over the same points, satisfy
  $L^2\ge L^1$ by the power-mean inequality *(compiler check, not in the
  sources)*. The $L^2$ norm computed differs from the printed one, or the
  labels are swapped; the rates are unaffected.
- Du & Yang print the H$_2$/O$_2$/Ar diaphragm at $x=0.5$ cm of a 10 cm
  domain, Peng et al. at the middle of their 100 mm tube.

# Citations

- [Fu (2021)](/sources/fu-2021.md) — §5.3 (arXiv v1).
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §4.3, Figs. 4–5.
- [Ye et al. (2022)](/sources/ye-2022.md) — §4.3, Eq. (43), Fig. 3.
- [Deng (2023)](/sources/deng-2023.md) — §1; App. A.4–A.5, Fig. 15.
- [Abgrall & Barsukow (2023)](/sources/abgrall-2023.md) — §3.5.3 and §5.6, Figs. 19, 24, 28 (author preprint).
- [Huang et al. (2026)](/sources/huang-2026.md) — §6.3, Fig. 8.
- [Li et al. (2022)](/sources/li-2022-b.md) — §4.3.1, Eq. (39), Fig. 4.
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §5.2.4, Eq. (16), Fig. 12.
- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) — Ex. 5.6, Fig. 3 (arXiv v1).
- [Wang & Don (2022)](/sources/wang-2022-b.md) — §3.2.3, Fig. 7.
- [Pazner (2021)](/sources/pazner-2021.md) — §5.2.1, Fig. 7 (arXiv v1).
- [Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md) — §IV.A–IV.B, Figs. 8–17, both tables captioned "Table 1" (author manuscript).
- [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) — §4.2, Eq. (41), Fig. 3 (arXiv v1).
- [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) — Ex. 3.5, Fig. 3.3; comment p. 31 (arXiv v1).
- [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) — Ex. 4.2, Eq. (4.1), Figs. 4.1–4.2, Table 4.2.
- [Renac (2021)](/sources/renac-2021.md) — §7.2, RP1, Figs. 3–4 (arXiv v3).
- [Li, Duan & Tang (2022)](/sources/li-2022-c.md) — Ex. 5.2, Fig. 5.3; Ex. 5.6, Table 5.2 (arXiv v1).
- [Arun, Krishnan & Samantaray (2022)](/sources/arun-2022.md) — §5.1, Eq. (5.2), Figs. 1–2 (arXiv v1).
- [Wong et al. (2021)](/sources/wong-2021.md) — §6.3, Table 6 (arXiv v1).
- [Bezgin et al. (2022)](/sources/bezgin-2022.md) — §4.2, Eqs. (29)–(30), Figs. 8–9; App. A.6, Table 4.
- [Hiejima (2022)](/sources/hiejima-2022.md) — §§3.1–3.2, Eqs. (26)–(27), Figs. 2–3.
- [Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) — §5.2.1, Table 1, Fig. 4 (arXiv v2).
- [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) — §5.1.1, Eq. (28), Tables 1–4, Fig. 2 (arXiv v3).
- [Yu & Hesthaven (2022)](/sources/yu-2022.md) — §5.3.1, Figs. 7–8.
- [Sousa & Scalo (2022)](/sources/sousa-2022.md) — §5.1, Fig. 4; App. A, Figs. A.21–A.22 (arXiv v2).
- [Nguyen et al. (2022)](/sources/nguyen-2022.md) — §3.2, Figs. 6–10.
- [Peng, Atkins & Deiterding (2022)](/sources/peng-2022.md) — §3.2, Fig. 6 (accepted manuscript).
- [Du & Yang (2022)](/sources/du-2022-b.md) — Exs. 6.2–6.3, Figs. 6.1–6.3.
- [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) — §4, Figs. 1–5 (arXiv v4).
- [Chen & Wu (2022)](/sources/chen-2022-b.md) — Exs. 4.2–4.5, Figs. 4–9 (arXiv v1).
- [Bai & Li (2022)](/sources/bai-2022.md) — §3.1.1–3.1.2, Figs. 8–9.
