---
type: Method
title: "Oscillation-eliminating discontinuous Galerkin (OEDG)"
description: "OEDG follows every Runge–Kutta stage of a DG scheme with an exactly solved damping step that multiplies each modal coefficient by a solution-dependent exponential factor, scale-, evolution- and linearity-invariant and conserving cell averages; Fan and Wu carry it to Hermite WENO, Yan, Abgrall and Wu to a bound-preserving five-equation two-phase scheme."
status: established
aliases: [BP-OEDG, OEDG, oscillation-eliminating DG, OE procedure, OE step, OE-HWENO, oscillation-eliminating Hermite WENO]
tags: [dg, limiting, low-dissipation, weno]
timestamp: 2026-10-23T15:08:00Z
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

## Oscillation elimination for Hermite WENO (OE-HWENO)

[Fan & Wu (2024)](/sources/fan-2024.md) carry the OE step from DG to
moment-based finite-volume [Hermite WENO](/methods/hermite-weno.md)
(arXiv v1). HWENO evolves the cell average $\bar u_i$ and the first
normalized moment $\bar u^{(1)}_i$, and the authors identify the
uncontrolled variation of the first moments near discontinuities as the
source of its spurious oscillations and nonlinear instability (§1).
Limiting the moments, they state, caps a sixth-order HWENO scheme at fifth
order, and the oscillation-free OF-HWENO of Zhao & Qiu adds stiff damping
terms with empirical, problem-dependent parameters that need modified
exponential Runge–Kutta integration (§1, Remark 1). The OE step is
applied after every stage of SSP-RK3 (Eq. (2.12)).

**OE step** (§2.2.2, Thm. 1, Eqs. (2.14)–(2.17)). The damping ODE is that
of OEDG with test functions in $\mathbb P^1$, a single coefficient and its
initial data $u^*_h$ given by a *linear* sixth-order Hermite
reconstruction (page-local $u^*_h$, $\hat\sigma_i$). Its exact solution
leaves the cell average unchanged and multiplies the first moment by one
exponential factor,

$$\bar u^{(1)}_i\leftarrow\bar u^{(1)}_i\exp\Big(-\frac{a\Delta t}{\Delta x}\hat\sigma_i\Big),\qquad \hat\sigma_i=\frac{\sum_{m=0}^{1}\Delta x^m\big(\lvert[\![\partial_x^mu^*_h]\!]_{i-1/2}\rvert+\lvert[\![\partial_x^mu^*_h]\!]_{i+1/2}\rvert\big)}{\max_j\lvert\bar u_j-u_\Omega\rvert},$$

with $a$ the global maximum wave speed of the Lax–Friedrichs flux and
$u_\Omega$ the mean of all cell averages ($\hat\sigma_i=0$ for constant
data). The jumps are explicit linear combinations of
$\bar u_{i-1},\dots,\bar u_{i+2}$ and $\bar u^{(1)}_{i-1},\dots,\bar u^{(1)}_{i+2}$
(Eq. (2.17)), so the reconstruction never has to be formed and the step
costs one multiplication per moment (Remark 3). Compared with the OEDG
coefficient above, the printed HWENO coefficient keeps only the jumps of
orders $0$ and $1$, without the factors $(2m+1)/((2N-1)m!)$ and the $\tfrac12$
in the normaliser, and uses the global rather than the local wave speed.
For systems one coefficient, the maximum over the components, damps all
components (Eq. (2.29)); in 2D the factor combines $x$- and $y$-jumps,
$\exp\big(-a^{(1)}\Delta t\hat\sigma^{(1)}_{i,j}/\Delta x-a^{(2)}\Delta t\hat\sigma^{(2)}_{i,j}/\Delta y\big)$,
and multiplies both first moments (Thm. 8, Eqs. (2.44)–(2.46)).

**Properties proved.**

- **Accuracy** (Thm. 2; Thm. 9 in 2D): under $a\Delta t/\Delta x\le C<1$,
  for a $C^{k+1}$ solution with periodic boundaries, $(k+1)$th-order accurate
  moments stay $(k+1)$th-order accurate after the OE step, because the jumps
  of the linear reconstruction of smooth data are $O(\Delta x^{k+1})$; the
  proof assumes $\max_j\lvert\bar u_j-u_\Omega\rvert$ bounded away from zero.
  This is the sixth order that moment limiting loses.
- **[Scale invariance](/properties/scale-invariance.md)** (Thm. 4): the OE
  operator commutes with $u\mapsto\lambda u+c$, $\lambda\ne0$, which the
  bundle calls affine invariance. A stencil-local **dimensionless
  transformation**, subtracting the stencil mean and dividing by the stencil
  range plus machine epsilon $10^{-15}$, makes the HWENO reconstruction
  itself invariant when that epsilon is neglected (Defs. 2–3, Thm. 5); the
  authors present it as applicable to any nonlinear reconstruction, while
  the proof covers HWENO.
- **Evolution invariance** (Thm. 7), for $\partial_tu+\lambda\partial_xf(u)=0$
  at a fixed CFL number, as for OEDG.
- **Bound preservation** (Thm. 11): the forward-Euler cell-average update,
  which the OE step leaves unchanged, is bound-preserving under
  $\Delta t\big(a^{(1)}/\Delta x+a^{(2)}/\Delta y\big)\le\varpi$ with the
  [optimal cell-average decomposition](/methods/optimal-cell-average-decomposition.md)
  of Cui, Ding & Wu, $\varpi=2-\sqrt{14}/2\approx0.1292$ at balanced
  directional speeds against $1/12$ for the classical decomposition, if the
  interface Gauss-point values and the interior part of the decomposition
  are admissible; a Zhang–Shu-type scaling enforces this (Remark 4). The
  authors call it the first use of the 2D optimal decomposition for HWENO
  (Remark 5); see [bound preservation](/properties/bound-preservation.md).

**Evidence** (§3; sixth-order OE-HWENO, SSP-RK3, CFL 0.45, $\Delta t\propto\Delta x^2$
in the accuracy tests). Burgers converges at $\ell^\infty$ orders 6.43,
6.37, 6.58, 6.38, 6.10 in 1D and 5.38–6.43 in 2D (Table 3.1); the Euler
[density wave](/benchmarks/density-wave-advection.md) at 6.93–6.99 in 1D
and 6.47–6.97 in 2D (Table 3.2), above six, which the authors attribute to
the dominance of the damping error, as observed for OEDG. The
[approximate dispersion relation](/definitions/approximate-dispersion-relation.md)
with and without the OE step is "nearly identical" (Fig. 2.1). On the
LWR traffic problem in three unit systems, the Lax tube scaled by
$10^{-7}$, $1$, $10^{7}$ and a 2D Riemann problem scaled by 100, OE-HWENO
results coincide while OF-HWENO smears or oscillates (Figs. 3.1, 3.2, 3.8).
With a positivity-preserving limiter the 1D and 2D
[Sedov](/benchmarks/sedov-blast-wave.md), [Leblanc](/benchmarks/leblanc-shock-tube.md)
and [Mach 2000 jet](/benchmarks/high-mach-astrophysical-jet.md) problems
run; HWENO without the OE step but with the same limiter oscillates on the
Sedov problem and on the jet, and OF-HWENO stays oscillatory on Sedov for
all four of its parameter values tried (Figs. 3.4–3.5, 3.11). The
[double rarefaction](/benchmarks/double-rarefaction-problem.md) problem
runs without the positivity limiter (Ex. 7).

## Bound-preserving OEDG for the five-equation model (BP-OEDG)

[Yan, Abgrall & Wu (2024)](/sources/yan-2024.md) carry OEDG to the Kapila
[five-equation model](/definitions/five-equation-model.md) in 1D and 2D on
Cartesian meshes, with the volume-fraction equation written as conservative
advection plus a non-conservative source, an HLL flux, and a
[Zhang–Shu-type limiter](/methods/zhang-shu-scaling-limiter.md) after the OE step.
The OE step is Peng et al.'s, with $a_i$ the spectral radius of the flux Jacobian
at the cell average and one coefficient per mode, the maximum over the components
(Eqs. (2.19)–(2.20); 2D Eqs. (3.17)–(3.18), with face-averaged jumps of all
derivatives of order $m$ by the trapezoidal rule).

**Linearity invariance** (Thm 2.3). If $\Lambda u_h\equiv c$ in a cell for a
constant matrix $\Lambda$ and vector $c$ (page-local), then
$\Lambda\mathcal F_{\Delta t}u_h\equiv c$. The proof uses that the damping factor of
each mode is a scalar common to all components, so the modes $l\ge1$ of
$\Lambda u_h$, which vanish, stay zero; the factor is common because the
coefficient is the maximum over the components *(compiler check, not in the
sources)*. The authors also
prove the limiter linearity-invariant (Thm 2.13, proof omitted). With uniform
velocity $v_0$ and pressure $p_0$, momentum minus $v_0$ times the partial
densities, and total energy minus kinetic energy minus $p_0\sum_k\phi_k/(\gamma_k-1)$,
are such linear identities, so the OE step and the limiter keep the Abgrall
equilibrium of an isolated material interface (Thms 2.6, 2.14; 2D Thm 3.4 for a
constant velocity vector only, Remark 3.5;
[pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)).
Scale invariance of the OE step gives $(\rho v)_\sigma=v_0\rho_\sigma$ in the same
argument (Remark 2.4, as recalled from Peng et al.).

**Bound preservation.** The OE step conserves cell averages, so the
bound-preservation proofs concern the DG update: the volume fraction stays in
$[0,1]$ and the partial densities and internal energy positive under explicit CFL
conditions with the boundary weight $\varpi$ (the first Gauss–Lobatto weight) of
the cell-average decomposition (Thms 2.7, 2.12, 3.6, 3.10;
[bound preservation](/properties/bound-preservation.md),
[geometric quasilinearization](/methods/geometric-quasilinearization.md)), and the
limiter, applied at the Gauss and Gauss–Lobatto points after the OE step, supplies
the point-value hypotheses (Eqs. (2.39)–(2.40)).

**Evidence** (§4; CFL $1/(2N+1)$; RK of order $N+1$ for accuracy, SSP-RK3
otherwise). With a non-vanishing source the $\mathbb P^2$ scheme keeps $L^1$ orders
$3.77$, $3.39$, $3.25$ and $\mathbb P^3$ about $4.5$, while the same OE step with the
earlier second-order averaging of the source (BP-OEDG-AVE) gives $1.69$–$1.84$ and
$1.94$–$1.96$ (Tables 2–3); in 2D $\mathbb P^3$ gives $3.56$, $4.12$, $4.07$ against
$0.91$, $-0.08$, $1.42$ (Tables 5–6). The moving-interface test keeps velocity and
pressure errors within $\pm1.5\times10^{-12}$ (Fig. 4). Thirteen examples, from
the double rarefaction and LeBlanc tubes to shock–bubble interactions, the
Richtmyer–Meshkov instability and a jet of velocity 200 relative to an ambient
sound speed of 1, run with $\mathbb P^2$ and $\mathbb P^3$; the authors state that the
double rarefaction and the jet can stop on negative density or pressure without the
limiter (no figure).

## Qualifications

- **No bound preservation in the original method.** Peng et al.'s OEDG is not claimed bound-preserving, and no
  positivity limiter is mentioned for the Mach 2000 jet and double Mach
  runs; in this corpus TENO-AA, TENO-THINC and affine-invariant WENO need a
  positivity-preserving flux limiter on the Mach 2000 jet
  ([bound preservation](/properties/bound-preservation.md)). Yan et al. (2024)
  obtain bound preservation by adding a scaling limiter, not from the OE step (above).
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
- **OE-HWENO needs a positivity limiter** on the extreme problems (Sedov,
  Leblanc, the Mach 2000 jet), while the OEDG jet run above reports
  none. Both papers run the Mach 2000 jet; neither runs it, or another
  extreme test, with the OE step alone and states the outcome without the
  positivity limiter.
- **Printed slips in Fan & Wu (arXiv v1).** The printed optimal weight of
  the decomposition has $(78\theta^2+46)$ in the denominator of the
  arccos argument, which is then $-244/46\approx-5.30$ at $\theta=0$,
  outside $[-1,1]$; with $(78\theta^2+46)^{3/2}$, the form printed by
  [Ding & Wu (2024b)](/sources/ding-2024-b.md) (Cor. 4.2), it gives
  $0.1291713=2-\sqrt{14}/2$, the value Fan & Wu state *(compiler check,
  not in the sources)*. In Tables 3.1–3.2 the $\ell^2$ orders repeat the
  $\ell^1$ orders digit for digit; from the printed $\ell^2$ errors the 2D
  Burgers orders are 5.45, 6.15, 6.30, 6.40, 6.49, against the printed
  5.57, 6.27, 6.43, 6.31, 6.36 *(compiler check, not in the sources)*. The
  errors still show sixth order.

# Citations

- [Fan & Wu (2024)](/sources/fan-2024.md) — arXiv v1: §1; §2.2 Eqs. (2.12)–(2.17), (2.29), Thms. 1–7, Defs. 1–3, Remarks 1–3; §2.3 Eqs. (2.44)–(2.46), Thms. 8–10; §2.4 Thm. 11, Remarks 4–5; §3 Exs. 1–12, Tables 3.1–3.2, Figs. 2.1, 3.1–3.11.
- [Ding & Wu (2024b)](/sources/ding-2024-b.md) — Cor. 4.2 (form of the optimal weight).
- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) — arXiv v1: §1 (Eqs. (1.2)–(1.4)); §2 (Eqs. (2.3)–(2.17); Rems. 2.1–2.12; Thms 2.6, 2.7, 2.10); §3 (Eqs. (3.8)–(3.12), Rem. 3.1); §4 (Thm 4.1, Assumption 4.5, Lemmas 4.10, 4.14, Rem. 4.4); §5 (Ex. 5.1–5.18, Tables 1–6, Figs. 1–14).
- [Yan, Abgrall & Wu (2024)](/sources/yan-2024.md) — §1; §2.2, Eqs. (2.17)–(2.22), Thms 2.3, 2.6, 2.13–2.14, Remark 2.4; §3, Eqs. (3.17)–(3.18), Thm 3.4, Remark 3.5; §4, Tables 2–3, 5–6, Fig. 4.
