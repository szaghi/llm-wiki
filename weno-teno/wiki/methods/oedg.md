---
type: Method
title: "Oscillation-eliminating discontinuous Galerkin (OEDG)"
description: "OEDG follows every Runge–Kutta stage of a DG scheme with an exactly solved damping step that multiplies each modal coefficient by a solution-dependent exponential factor, scale- and evolution-invariant and conserving cell averages; the page covers OE-HWENO, bound-preserving two-phase OEDG, locally divergence-free OEDG for MHD and the entropy-stable oscillation-free DG relative."
status: established
aliases: [BP-OEDG, OEDG, LDF OEDG, ESOFDG, entropy-stable oscillation-free DG, oscillation-eliminating DG, OE procedure, OE step, OE-HWENO, oscillation-eliminating Hermite WENO]
tags: [dg, limiting, low-dissipation, weno]
timestamp: 2026-10-24T06:02:00Z
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
damped previous stages exactly as unmodified RKDG would, then replaces it by
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

## Locally divergence-free OEDG for ideal MHD

[Liu & Wu (2025)](/sources/liu-2025.md) (arXiv v2) carry OEDG to the 2D ideal MHD
equations on Cartesian meshes with two structure-preserving properties: a
[locally divergence-free](/properties/divergence-free-magnetic-field.md) magnetic field
and provable positivity of the cell averages. The variables are split into
$(\rho,\rho v,B_3,E)$, discretized in a $\mathbb P^N$ modal Legendre space, and
$(B_1,B_2)$, discretized in the Li–Shu space of vector polynomials of degree $N$ with zero
divergence in each cell, of dimension $(N+1)(N+4)/2$ (§2.2). After every SSP-RK3 stage
the OE step of Peng et al. is applied in a form that differs from the system version
above in how coefficients are pooled (§2.4):

- **Component-wise step** for the six non-magnetic variables (Eqs. (16)–(25)): each
  component has its own damping coefficients, applied by a Hadamard product, instead of
  the common maximum over the components of Peng et al. (Eq. (2.17)) and Yan et al.
- **Locally divergence-free step** for $(B_1,B_2)$ (Eqs. (27)–(35)): one coefficient per
  edge, the maximum over $B_1$ and $B_2$, scales whole basis vectors of the
  divergence-free space, so the damped field stays divergence free in each cell
  (Remark 2); the two constant basis vectors are untouched.

The rate is $\delta^m_{ij}=a^{(1)}_{ij}\big(\sigma^m_{i+1/2,j}+\sigma^m_{i-1/2,j}\big)/\Delta x+a^{(2)}_{ij}\big(\sigma^m_{i,j+1/2}+\sigma^m_{i,j-1/2}\big)/\Delta y$,
with $a^{(d)}_{ij}$ the spectral radius at the cell average and, on an $x$-edge,
$$\sigma^m_{i+1/2,j}=\frac{(2m+1)\Delta x^m}{2(2N-1)\,m!}\sum_{\lvert\boldsymbol\alpha\rvert=m}\frac{\frac1{\Delta y}\int_{y_{j-1/2}}^{y_{j+1/2}}\big\lvert[\![\partial^{\boldsymbol\alpha}u_h]\!]_{i+1/2}\big\rvert\,dy}{\lVert u_h-\mathrm{avg}(u_h)\rVert_{L^\infty(\Omega)}}$$
(Eqs. (17)–(19); $\boldsymbol\alpha$ a multi-index and $\partial^{\boldsymbol\alpha}$ the
derivative weighted by the multinomial coefficient $\lvert\boldsymbol\alpha\rvert!/(\alpha_1!\alpha_2!)$,
page-local). For data that vary in $x$ only this is Peng et al.'s 1D coefficient, the
factor $\tfrac12$ moved from the normaliser into the edge term *(compiler check, not in
the sources)*; Peng et al.'s 2D form uses face-averaged jumps by the trapezoidal rule and
the distances $h_{e,K}$. The authors state that the step keeps conservation,
compactness, the optimal order and, "as with the OE technique" of Peng et al., scale and
evolution invariance (Remarks 1–2).

Positivity comes from the cell-average equation, not from the OE step: the
[Godunov–Powell source](/definitions/godunov-powell-source-term.md) is added there only,
split upwind between the two cells of each interface, the flux is a positivity-preserving
HLL flux, and a [Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md) at the
nodes of the [optimal cell-average decomposition](/methods/optimal-cell-average-decomposition.md)
after each OE step supplies the hypotheses of the
[geometric-quasilinearization](/methods/geometric-quasilinearization.md) proof (Thm 1,
§3). With $N=2$ and CFL $0.12$ the 1D sine wave converges at $L^1$ orders
$3.18\to3.01$ (Table 1), and the 2D sine wave at $2.92$, $4.24$, $4.61$, $3.55$, $3.19$
(Table 2), which the authors read as third order. Disabling the OE step makes the MHD
shock–cloud run fail, and removing the source or the limiter gives negative cell-average
pressure; on the Mach 800 and Mach 10000 magnetized jets disabling any of the three makes
"the code immediately fail" (§4.2.4, §4.2.6).

## Entropy-stable oscillation-free DG for ideal MHD (ESOFDG)

[Liu et al. (2025b)](/sources/liu-2025-b.md) extend their entropy-stable
oscillation-free DG, the OFDG line that OEDG modifies, to ideal MHD on nodal
Legendre–Gauss–Lobatto DG with [flux differencing](/methods/flux-differencing.md), the
Chandrashekar–Klingenberg [entropy-conservative flux](/methods/entropy-conservative-flux.md)
and the Godunov–Powell source (§3.1). The damping stays in the semi-discrete equation,
as in OFDG, as a term $-\sigma^{\mathrm{ES}}_i\big(u_h-\bar u_i\big)$ that acts on the
deviation from the cell mean, all non-mean modes alike, with one scalar coefficient per
cell for all eight components (Eqs. (3.15)–(3.16)):
$$\sigma^{\mathrm{ES}}_i=\frac{a_i}{\mathcal M_i^2}\max_{1\le c\le8}\sum_{\ell=0}^{1}\tfrac12\Delta x^{2\ell}\Big([\![\partial_x^\ell u^{(c)}_h]\!]^2_{i-1/2}+[\![\partial_x^\ell u^{(c)}_h]\!]^2_{i+1/2}\Big),\qquad
\mathcal M_i=\max_c\big\lVert u^{(c)}_h-\overline{u^{(c)}_h}\big\rVert_{L^\infty(I_{i-1}\cup I_i\cup I_{i+1})},$$
zero if $\mathcal M_i\le10^{-12}$ (page-local $\sigma^{\mathrm{ES}}_i$, $\mathcal M_i$; $a_i$
the largest characteristic speed in the cell). Against the OEDG coefficient above it
uses only the jumps of the value and of the first derivative, independently of $N$,
squared jumps over a squared local range in place of absolute jumps over the global
range, and no $(2m+1)/((2N-1)m!)$ factors. The authors present the local wave speed, the
absence of characteristic decomposition, evolution invariance and, through
$\mathcal M_i$, affine invariance as taken from OEDG; the invariances are asserted, not
proved (§3.2). Each forward-Euler stage of TVD-RK3 is split into the explicit DG step and
an implicit damping step solved in closed form, $u_h\leftarrow\frac1{1+\mathsf d_i}u_h+\frac{\mathsf d_i}{1+\mathsf d_i}\bar u_i$
with $\mathsf d_i=2\Delta t\,\sigma^{\mathrm{ES}}_i/\Delta x$ times the stage weight
(page-local $\mathsf d_i$, Eq. (3.21)), a rational rather than exponential factor, which
keeps the CFL number of the undamped scheme; the splitting is at most first order, which
they argue does not pollute accuracy because the coefficient vanishes on smooth solutions,
citing the OEDG proof for linear scalar laws (§3.3). **Theorem 3.2** proves the damped
semi-discrete scheme entropy stable, since the damping term is entropy dissipative by
convexity of $\eta$ and orthogonality of the cell-mean projection, and its local
truncation error $O(\Delta x^N)$ ([entropy stability](/properties/entropy-stability.md)).
The scheme is non-conservative because of the Godunov–Powell term and not provably
positivity preserving (Remarks 3.1–3.2). With $N=2$, $N+3$ Gauss–Lobatto points (more than
collocation needs) and CFL $0.6/(2N+1)$, the density wave converges at order $3.000$ (Table 1);
the rotor and the Balsara–Spicer blast run without a positivity limiter, the Mach 800 and
10000 jets need the Zhang–Shu limiter and CFL $0.2/(2N+1)$ (Ex. 6, 8, 10). The authors
contrast their jets, run with the positivity limiter alone, with Liu & Wu's, which needed
three ingredients (Ex. 10).

## The OE step and COS(DG)

[Cao et al. (2026)](/sources/cao-2026.md), from the same group, recall the OE operator
exactly in their Remark 3 and replace it by the [COS(DG)](/methods/cos-dg.md)
post-processing, which scales all non-mean modes of a cell by one exponential factor
$\exp(-a_i\Delta t\,\sigma^{\mathrm{OS}}_i/\Delta x_i)$ built from distances between the
cell's extrapolated polynomial and its neighbours' (page-local, defined on that page). They
read the OE step as a modal filter whose mode-$l$ exponent is the cumulative sum
$\sum_{m\le l}\sigma^m_i$, and list five differences: mode-dependent against uniform damping,
derivative jumps against derivative-free differences, every Runge–Kutta stage against once
per time step, global against local scale invariance, and a modal formulation against one
that also serves nodal DG (§1, Remark 3). Their statements about OEDG:

- **Global scale invariance only.** Because the normaliser
  $\lVert u_h-\mathrm{avg}(u_h)\rVert_{L^\infty(\Omega)}$ is one domain-wide range, OEDG "may
  fail to fully suppress oscillations when small and large-scale jumps coexist" (§2.1,
  Fig. 2); on a multi-scale Lax problem with two tubes of very different amplitude OEDG
  shows undershoots in the small-scale part that COS(DG) suppresses (Ex. 6.8, Fig. 9).
  Peng et al. themselves proposed a locally scale-invariant coefficient and left it unused
  for want of a mesh-independent constant (Rem. 2.9; see Qualifications); COS(DG) uses a local
  normaliser with one fixed constant per degree, chosen empirically (see its page).
- **Entropy stability** is "not guaranteed for the OEDG method", whereas the COS step
  provably does not increase any convex entropy in a cell (§1; Thm 2.4 of Cao et al.;
  [entropy stability](/properties/entropy-stability.md)).
- **Cost.** On the Woodward–Colella and Shu–Osher problems with 400 cells, single-core
  Python, the OE step takes 35.3–40.6 % of the OEDG run time, against 15.6–18.8 % for the
  COS step and 6.3–10.4 % for local COS (Table 3).
- **OFDG**, the semi-discrete precursor, is recalled as stiff at strong discontinuities,
  needing modified exponential Runge–Kutta methods, and as prone to smearing or persistent
  oscillations when scales or wave speeds vary widely, the latter citing Peng et al. (§1).

## Qualifications

- **No bound preservation in the original method.** Peng et al.'s OEDG is not claimed bound-preserving, and no
  positivity limiter is mentioned for the Mach 2000 jet and double Mach
  runs; in this corpus TENO-AA, TENO-THINC and affine-invariant WENO need a
  positivity-preserving flux limiter on the Mach 2000 jet
  ([bound preservation](/properties/bound-preservation.md)). Yan et al. (2024)
  obtain bound preservation by adding a scaling limiter, not from the OE step (above).
  Liu & Wu (2025) likewise obtain positivity from the cell-average update, the
  Godunov–Powell source and a scaling limiter (above).
- **Pooling across components.** Peng et al. and Yan et al. damp all components of a
  system with one coefficient, the maximum over the components, which Yan et al.'s
  linearity invariance needs; Liu & Wu (2025) damp the non-magnetic components with
  their own coefficients and pool only $B_1$, $B_2$. Their paper states scale and
  evolution invariance but not linearity invariance. Component-wise factors still keep
  an identity in which one component is an affine function of another, such as
  $\rho v=v_0\rho$ at uniform velocity, because each coefficient is affine invariant, but
  not a general identity $\Lambda u_h\equiv c$ that couples several components, for which
  Yan et al.'s proof needs a common factor *(compiler check, not in the sources)*. The
  two are design variants; no source compares them on the same problem.
- **Orders read as "third".** Liu & Wu's 2D sine-wave orders $4.24$, $4.61$, $3.55$
  (Table 2) and Liu et al. (2025b)'s circularly polarized Alfvén-wave orders
  $3.622$, $5.065$, $3.910$, $3.086$, $2.897$ in $L^1$ (Table 2) are called third order
  and "the optimal order" by the authors; the finest pairs are $3.19$ and $2.897$, the
  latter below $N+1=3$. Theorem 3.2 of Liu et al. (2025b) proves only truncation error
  $O(\Delta x^N)$.
- Liu et al. (2025b) state the entropy-stable flux condition (Eq. (3.13)) for the
  entropy-conservative flux instead of the interface flux, for which it is trivially
  satisfied; their proof of Theorem 3.2 uses the condition for the interface flux.
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
- [Liu & Wu (2025)](/sources/liu-2025.md) — arXiv v2: §1; §2.2–2.4, Eqs. (5)–(35), Remarks 1–2; §3.2–3.5; §4.1–4.2, Tables 1–2.
- [Liu et al. (2025b)](/sources/liu-2025-b.md) — §3.1–3.3, Eqs. (3.11)–(3.21), Thm 3.2, Remarks 3.1–3.2; §4, Tables 1–2, Ex. 6, 8, 10.
- [Cao et al. (2026)](/sources/cao-2026.md) — §1; §2.1, Fig. 2; Remark 3; Thm 2.4; Ex. 6.8, Fig. 9; Table 3.
