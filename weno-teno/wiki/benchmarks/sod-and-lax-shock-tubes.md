---
type: Benchmark
title: "Sod and Lax shock tubes"
description: "The two most often run one-dimensional Euler Riemann problems with exact solutions, Sod's mild tube and Lax's stronger one, run by most sources as the first check of shock and contact capturing; records each source's placement, grid and final time, the printed variants and the multicomponent, stiffened-gas and relaxation relatives."
status: established
aliases: [Sod problem, Sod shock tube, Lax problem, Lax shock tube, Riemann problem of Lax, Lax–Harden problem]
tags: [benchmark, weno, teno, riemann-solver]
timestamp: 2026-10-22T00:00:00Z
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

Abgrall & Barsukow run Sod with three Active Flux variants: sixth order
at CFL 0.25 (Fig. 19); a fifth-order point setup with a third-order
evolution operator at CFL 0.5 (Fig. 24); and seventh order at CFL 0.01
on a periodic tube with discontinuities at $x=1/3$ and $x=2/3$ (Fig. 28),
which doubles the problem so that periodic boundaries can be used.
Pazner and Luo et al. place the diaphragm at $x=0$ of a tube centred
on the origin, a shift of the $[0,1]$ placement.

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
- **Gas–liquid tube.** [Wong et al. (2021)](/sources/wong-2021.md) §6.3
  run a water–air "Sod" problem with pressure ratio $10^9/10^5$; it
  belongs with the [gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md).

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
- Li, Shu & Qiu do not print $\gamma$ for the Lax problem, and Arun et
  al. not for their tube.

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
