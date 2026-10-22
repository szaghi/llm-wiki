---
type: Method
title: "Oscillation-eliminating discontinuous Galerkin (OEDG)"
description: "OEDG follows every Runge–Kutta stage of a standard DG scheme with an exactly solved damping step that multiplies each modal coefficient by a solution-dependent exponential factor; its damping coefficients are scale- and evolution-invariant, it conserves cell averages, and it carries an optimal fully discrete error estimate for linear advection."
status: established
aliases: [OEDG, oscillation-eliminating DG, OE procedure, OE step]
tags: [dg, limiting, low-dissipation]
timestamp: 2026-10-21T12:00:00Z
---

# Oscillation-eliminating discontinuous Galerkin (OEDG)

The OEDG method of [Peng, Sun & Wu (2024)](/sources/peng-2024.md) controls
oscillations of a Runge–Kutta [discontinuous Galerkin](/methods/discontinuous-galerkin.md)
scheme without troubled-cell detection and without characteristic
decomposition. After every stage of the unmodified DG scheme, an
**oscillation-eliminating (OE) step** solves a linear damping ODE in a
pseudo-time over one full time step. With the damping coefficients frozen at
the stage solution and an orthogonal modal basis, that ODE is diagonal and is
solved exactly: each modal coefficient of degree $l\ge1$ is multiplied by an
exponential factor, and the cell average is untouched. The method modifies
the oscillation-free DG (OFDG) method of Lu, Liu and Shu, in which the same
kind of damping is added to the semi-discrete ODE and makes it stiff.

## The scheme

Let $\mathcal L$ denote the DG spatial operator of degree $N$ on cells $I_i$
of width $\Delta x_i$, and let a Runge–Kutta method be written in Shu–Osher
form. OEDG (Eqs. (2.3)–(2.4)) computes each stage $u_h^{n,\ell+1}$ from the
damped previous stages exactly as standard RKDG would, then replaces it by
$u_\sigma^{n,\ell+1}=\mathcal F_{\Delta t}\,u_h^{n,\ell+1}$, with
$\mathcal F_{\Delta t}$ the OE operator (page-local symbols
$u_\sigma$, $\mathcal F_{\Delta t}$). The step applies equally after each step
of a multistep method. The damping is evolved over the full $\Delta t$ at
every stage; matching it to the stage fraction would reduce the damping
(Rem. 2.5).

**OE operator** (1D scalar, Eq. (2.5)). $\mathcal F_{\Delta t}u_h=u_\sigma(\cdot,\Delta t)$,
where $u_\sigma(\cdot,\hat t)$ solves, in pseudo-time $\hat t$, for all test
functions $w\in\mathbb P^N(I_i)$,
$$\frac{d}{d\hat t}\int_{I_i}u_\sigma w\,dx+\sum_{m=0}^{N}\frac{a_i\,\sigma_i^m(u_h)}{\Delta x_i}\int_{I_i}\big(u_\sigma-P^{m-1}u_\sigma\big)w\,dx=0,\qquad u_\sigma(\cdot,0)=u_h,$$
with $a_i=\lvert f'(\bar u_i)\rvert$ the local wave speed at the cell average,
$P^m$ the $L^2$ projection onto piecewise $\mathbb P^m$ and $P^{-1}:=P^0$ the
cell average (page-local $P^m$, $\sigma_i^m$).

**Damping coefficients** (Eq. (2.6)):
$$\sigma_i^m(u_h)=\frac{(2m+1)\,\Delta x_i^m}{(2N-1)\,m!}\;
\frac{\lvert[\![\partial_x^mu_h]\!]_{i-1/2}\rvert+\lvert[\![\partial_x^mu_h]\!]_{i+1/2}\rvert}{2\,\lVert u_h-\mathrm{avg}(u_h)\rVert_{L^\infty(\Omega)}},$$
and $\sigma_i^m=0$ if $u_h$ is constant; $\mathrm{avg}$ is the average over
the whole domain $\Omega$, so the normaliser is one global scalar per OE step,
computed like the time step. The coefficients are dimensionless, which they
must be because $\Delta t\,a_i\sigma_i^m/\Delta x_i$ is the argument of an
exponential (Rem. 2.1). They are small where the solution is smooth and
large near discontinuities.

**Exact solution** (Eqs. (2.9)–(2.12)). In a scaled Legendre basis
$\phi^{(l)}_i$, $u_\sigma=\sum_{l=0}^{N}u^{(l)}_i(\hat t)\,\phi^{(l)}_i$ and
$u_\sigma-P^{m-1}u_\sigma=\sum_{l\ge\max(m,1)}u^{(l)}_i\phi^{(l)}_i$, so each
mode obeys a scalar linear ODE and
$$u^{(l)}_i(\Delta t)=\exp\Big(-\frac{a_i\Delta t}{\Delta x_i}\sum_{m=0}^{l}\sigma_i^m\Big)\,u^{(l)}_i(0),\qquad l=1,\dots,N,\qquad u^{(0)}_i\ \text{unchanged}.$$
Mode $l$ is damped by the cumulative sum over $m\le l$, so higher modes are
damped more: the OE step is an exponential modal filter with
solution-dependent strength, which links damping to spectral viscosity and
filtering ([artificial viscosity](/methods/artificial-viscosity.md)). Its
cost is a few scalar multiplications per mode.

**Systems** (Eq. (2.17)). The same ODE acts on the vector of conservative
variables, with $a_i$ the spectral radius of $A(\bar u_i)$ and one common
coefficient $\sigma_i^m=\max_c\sigma_i^m(u_h^{(c)})$ over the components $c$
(page-local); there is no [characteristic decomposition](/methods/characteristic-decomposition.md).

**Multi-D** (Eqs. (3.8)–(3.12)). The rate becomes
$\delta_K^m=\sum_{e\in\partial K}a_e\,\sigma^m_{e,K}/h_{e,K}$, with $a_e$ the
normal spectral radius at $\bar u_K$, $h_{e,K}=\sup_{x\in K}\mathrm{dist}(x,e)$,
and $\sigma^m_{e,K}$ built from face-averaged jumps of all derivatives of
order $m$ (trapezoidal rule in 2D; page-local symbols, $\delta_K^m$ not the
TENO flag $\delta_k$). All modes of total
degree $l$ share one factor $e^{-\Delta t\sum_{m\le l}\delta_K^m}$. On
rectangles the 2D method reduces exactly to the 1D one for quasi-1D problems
(Rem. 3.1).

## Properties

- **Conservation**: the cell average is unchanged (Rem. 2.2).
- **Stability**: the elementwise $L^2$ norm does not increase (Rem. 2.3), and
  OEDG runs at the normal CFL condition even where the damping is very stiff
  near strong shocks (§5; $\Delta t=C\Delta x/a$ with $C=1/(2N+1)$ in 1D).
- **[Scale invariance](/properties/scale-invariance.md)** (Thm 2.6):
  $\sigma_i^m(\lambda u_h+\mu)=\sigma_i^m(u_h)$ for $\lambda\neq0$, hence
  $\mathcal F_{\Delta t}(\lambda u_h+\mu)=\lambda\mathcal F_{\Delta t}u_h+\mu$
  ($\lambda$, $\mu$ page-local scalars). With homogeneous flux and numerical
  flux the whole scheme is homogeneous (Thm 2.7).
- **Evolution invariance** (Thm 2.10): for $\partial_tu+\lambda\,\partial_xf(u)=0$,
  $\lambda>0$, on a fixed mesh at the same CFL number, the discrete solution
  after $n$ steps does not depend on $\lambda$. This holds because $a_i$
  scales with $\lambda$.
- **Contrast with OFDG.** The OFDG coefficient (Eq. (2.13), as recalled)
  $\frac{2(2m+1)h^m}{(2N-1)m!}\big([\![\partial_x^mu_h]\!]_{i-1/2}^2+[\![\partial_x^mu_h]\!]_{i+1/2}^2\big)^{1/2}$,
  $h=\max_i\Delta x_i$, scales like $\lvert\lambda\rvert$ under $u_h\mapsto\lambda u_h$
  and carries no wave speed, so OFDG smears large-amplitude or slow-wave
  problems and leaves oscillations in small-amplitude or fast-wave ones
  (Rem. 2.8). The new coefficient inserted in OFDG would give OFDG the same
  invariances (Rem. 2.11, not shown numerically).
- Without scale-invariant coefficients the result of a damping applied in
  characteristic variables would depend on the arbitrary scaling of the
  eigenvectors, and characteristic decomposition can destroy scale
  invariance (Rem. 2.12).

## Error estimate

Thm 4.1: for linear advection $\partial_tu+b\cdot\nabla u=0$ with
constant velocity and upwind flux, on quasi-uniform 1D meshes and 2D
Cartesian meshes, with an explicit $r_{\mathrm{RK}}$-stage Runge–Kutta method of order $r_{\mathrm{RK}}$
for which RKDG is stable in the sense of Assumption 4.5, $N>d/2$,
$r_{\mathrm{RK}}>d/2+1$, a smooth solution, $\lVert u_h-\mathrm{avg}(u_h)\rVert_{L^\infty}\ge C>0$
at every stage, and initial error $O(\Delta x^{N+1})$,
$$\max_{n}\lVert u_\sigma^n-u(\cdot,t^n)\rVert_{L^2}\le C\big(\Delta x^{N+1}+\Delta t^{r_{\mathrm{RK}}}\big)$$
($b$, $r_{\mathrm{RK}}$, $d$ page-local; the source writes $\beta$ and $r$). The proof writes OEDG as linear RKDG plus a
nonlinear source, validates an a priori $L^\infty$ bound by induction
(Lemma 4.10), and bounds the OE perturbation (Lemma 4.14). The restrictions
$N>d/2$, $r_{\mathrm{RK}}>d/2+1$ are technical; optimal rates are observed with lower $N$
and $r_{\mathrm{RK}}$ (Rem. 4.4). The authors call this possibly the first generic fully
discrete error estimate for nonlinear DG schemes with an automatic
oscillation control.

## Numerical evidence

With SSP-RK3 and local Lax–Friedrichs fluxes on discontinuous problems,
$(N+1)$th-order RK on smooth ones (§5):

- Optimal order $N+1$ in $L^1$, $L^2$, $L^\infty$ for 1D and 2D advection,
  Burgers and 1D Euler, approached from above on coarse meshes, where the
  damping dominates the error (Tables 1–6). Cell averages and downwind point
  values superconverge at order $N+2$ (e.g. 2.99, 4.02, 5.00 for $N=1,2,3$),
  proved for semi-discrete OFDG but not for fully discrete OEDG.
- On coarse meshes OEDG errors exceed plain RKDG errors (at $N_x=128$,
  $N=2$: $1.08\times10^{-5}$ against $2.25\times10^{-6}$); at $N_x=2048$ they
  nearly agree ($6.23\times10^{-10}$ against $5.48\times10^{-10}$).
- Scale and evolution invariance hold to the plotting accuracy for advection
  scaled by $\lambda\in\{0.01,1,100\}$, for LWR traffic in three unit
  systems, and for the Lax and [Shu–Osher](/benchmarks/shu-osher-problem.md)
  problems; OFDG smears at $\lambda=100$ and oscillates at $\lambda=0.01$
  (Figs. 1–3, 5).
- On the [Woodward–Colella blast waves](/benchmarks/woodward-colella-blast-wave.md)
  OEDG works with or without characteristic decomposition; OFDG without it
  smears much (Fig. 4).
- Steady residuals reach machine-epsilon levels for a shock reflection and
  for supersonic flow past two plates (Figs. 8–9).
- [Double Mach reflection](/benchmarks/double-mach-reflection.md) ($N=3$,
  $\Delta x=1/240$), [shock–vortex interaction](/benchmarks/shock-vortex-interaction.md),
  [two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md)
  and the [Mach 2000 jet](/benchmarks/high-mach-astrophysical-jet.md)
  ($320\times160$, $N=2$) run without nonphysical oscillations (Ex.
  5.15–5.18).

## Qualifications

- **No bound preservation.** OEDG is not claimed bound-preserving, and no
  positivity limiter is mentioned for the Mach 2000 jet and double Mach
  runs; in this corpus TENO-AA, TENO-THINC and affine-invariant WENO need a
  positivity-preserving flux limiter on the Mach 2000 jet
  ([bound preservation](/properties/bound-preservation.md)).
- **Global coupling.** The normaliser $\lVert u_h-\mathrm{avg}(u_h)\rVert_{L^\infty(\Omega)}$
  makes the damping strength depend on the global range of the solution.
  A locally scale-invariant variant (Eq. (2.14)) is proposed but not used,
  because no unified mesh-independent constant for it has been found
  (Rem. 2.9).
- **Fixed constants.** The coefficient carries fixed constants; "no
  problem-specific parameters" means no constants tuned per problem.
- **Internal inconsistency.** Ex. 5.15 says the OFDG damping grows to
  "$\lambda^2$ times its original magnitudes" at $\lambda=100$, while
  Rem. 2.8 gives a factor $\lvert\lambda\rvert$ (arXiv v1).
- Read in arXiv v1; numbering may differ in the Mathematics of Computation
  version.

# Citations

- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) — arXiv v1: §1 (Eqs. (1.2)–(1.4)); §2 (Eqs. (2.3)–(2.17); Rems. 2.1–2.12; Thms 2.6, 2.7, 2.10); §3 (Eqs. (3.8)–(3.12), Rem. 3.1); §4 (Thm 4.1, Assumption 4.5, Lemmas 4.10, 4.14, Rem. 4.4); §5 (Ex. 5.1–5.18, Tables 1–6, Figs. 1–14).
