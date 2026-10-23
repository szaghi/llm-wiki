---
type: Method
title: "Hermite WENO"
description: "Hermite WENO (HWENO) builds WENO candidates from cell averages plus derivative or first-moment data on compact stencils; the page covers moment-based finite-volume HWENO with moment modification, positivity preservation and the OE-HWENO filter, Hermite candidates for spectral-difference limiting, finite-difference HWENO-R, and HWENO as a finite-element sensor."
status: established
aliases: [HWENO, Hermite WENO reconstruction, HWENO-R, HWENO-L, finite-difference HWENO, Zhong–Shu HWENO, moment-based HWENO, multi-resolution HWENO, MR-HWENO, hybrid HWENO, PCP HWENO, HWENO6-M5-I, HTENO, Hermite TENO, OE-HWENO, oscillation-eliminating HWENO]
tags: [weno, reconstruction, finite-volume, dg, compact-scheme]
timestamp: 2026-10-23T23:55:00Z
---

# Hermite WENO

Hermite WENO (HWENO) schemes, "based on the Hermite polynomials", were developed for nonlinear
conservation laws and Hamilton–Jacobi equations (Fu 2023, §1). A candidate polynomial is fitted not
only to cell averages but also to derivative information (derivative averages in the Qiu–Shu schemes,
first moments in the more recent ones, or a neighbour's whole polynomial in element methods), so a
given order needs fewer cells. Fan, Zhang & Qiu (2021, §1) summarize the trade-off: HWENO schemes have
more compact stencils than WENO schemes and higher resolution at the same order, but they are in
practice less robust, and the extra equation for the derivative or moment raises their cost.

## Moment-based HWENO

The finite-volume HWENO of Zhao, Chen & Qiu, used by Fan et al. (2021, §3, Eqs. (3.2)–(3.6)) and by Li,
Shu & Qiu (2022d, §2.1, Eqs. (2.2)–(2.8)), evolves the cell average $\bar u_i$ and the first moment
$\bar u^{(1)}_i=\frac1{\Delta x}\int_{I_i}u\,\frac{x-x_i}{\Delta x}\,dx$ (page-local symbol). Testing
$\partial_tu+\partial_xf=0$ with $1$ and $(x-x_i)/\Delta x$ — the $\mathbb P^1$
[discontinuous Galerkin](/methods/discontinuous-galerkin.md) weak form — gives

$$\frac{d\bar u_i}{dt}=-\frac{\hat f_{i+1/2}-\hat f_{i-1/2}}{\Delta x},\qquad
\frac{d\bar u^{(1)}_i}{dt}=-\frac{\hat f_{i+1/2}+\hat f_{i-1/2}}{2\Delta x}+\frac1{\Delta x^2}\int_{I_i}f(u)\,dx,$$

with the volume integral by the four-point Gauss–Lobatto rule on $x_{i\pm1/2}$,
$x_i\pm\frac{\sqrt5}{10}\Delta x$ (weights $\tfrac1{12},\tfrac5{12},\tfrac5{12},\tfrac1{12}$). Only
point values at these four points are reconstructed; the two boundary values feed the numerical flux.
Li, Shu & Qiu (2022d, §1) contrast this with their earlier multi-resolution HWENO, which evolved derivative
values and reconstructed function and derivative values at cell boundaries. *(Compiler check, not in
the sources: for linear data $\bar u^{(1)}_i=u'\Delta x/12$, so the moment and derivative variables
agree up to a factor only for linear data.)*

## Sixth-order multi-resolution HWENO (HWENO6-M5-I)

Li, Shu & Qiu (2022d, §2) build a sixth-order scheme on three cells in 1-D and $3\times3$ cells in 2-D
("the same size as the general HWENO scheme and more compact than the general WENO scheme of the same
order", Abstract; §4):

- **Hierarchy.** Central polynomials of degree 0, 2, 3, 5: the constant from $\bar u_i$ alone, the
  others from the averages of $I_{i-1},I_i,I_{i+1}$ and zero, one or three first moments (Eq. (2.9)), combined in the multi-resolution manner with linear weights
  $10^{l-1}$ and WENO-Z-type weights; in 2-D the over-determined fits keep the target average exactly
  and the rest in least squares ([multi-resolution WENO](/methods/multi-resolution-weno.md)).
- **Flux.** HLLC with a primitive-variable pressure estimate and pressure-dependent wave-speed
  coefficients, chosen "to better adapt to our high order scheme" (Eqs. (2.5)–(2.7);
  [HLL-family solvers](/methods/hll-riemann-solvers.md)).
- **Troubled cells.** A KXRCF indicator with exponent $(l+1)/3$, $l=5$, on the density, which needs no
  extra reconstruction (Eqs. (2.25), (2.31)–(2.34);
  [troubled-cell indicators](/definitions/troubled-cell-indicator.md)).
- **Moment modification.** In a flagged cell the first moment is replaced by that of the quartic
  fitted to the three neighbouring averages and the two neighbouring moments (Eq. (2.27)),
  $$\bar u^{(1)}_i\leftarrow-\tfrac5{76}\bar u_{i-1}+\tfrac5{76}\bar u_{i+1}-\tfrac{11}{38}\bar u^{(1)}_{i-1}-\tfrac{11}{38}\bar u^{(1)}_{i+1},$$
  and the reconstruction is repeated there (dimension by dimension in 2-D). *(Compiler check, not in the sources: the
  coefficients were recomputed from the quartic's moment conditions; they agree.)* The modified moment
  overwrites the evolved one.
- **Time step.** SSP-RK3 at CFL 0.6 in 1-D and 2-D ([SSP Runge–Kutta](/methods/ssp-runge-kutta.md)).

Remark 1 argues by Taylor expansion that the weights stay at $d_l(1+O(\Delta x^6))$ in smooth regions,
hence sixth order, and that without modification a discontinuity makes the first moment $O(1)$ and
magnifies the low-order layers, smearing the jump, whereas after modification all layers keep weights
near their linear ones, so that resolution "can be increased significantly". With the modification
only in flagged cells, $L^1$ orders at the finest grids are 5.96 (1-D Burgers, $3.95\times10^{-13}$),
6.36 (2-D Burgers), 6.03 (1-D Euler) and 6.49 (2-D Euler); modifying every cell (HWENO6-M5-NI) gives
fifth order, 4.88–5.10, "as expected" (Tables 3.1–3.4;
[Burgers tests](/benchmarks/burgers-equation-tests.md)). The unmodified HWENO6 blows up on the
[double Mach reflection](/benchmarks/double-mach-reflection.md); with the modification the scheme
gives sharper shocks than HWENO6 on the Lax, Shu–Osher, blast-wave, Sedov and
[forward-facing step](/benchmarks/forward-facing-step.md) problems (§3, figure comparisons only).

**Stability history.** Li, Shu & Qiu (2022d, §1) state that the original Qiu–Shu HWENO "is not stable enough"
for the double Mach and forward-step problems, largely because first-derivative values become very
large near discontinuities, and that their own earlier multi-resolution HWENO improved resolution but
not stability, "since the first two layers in the hierarchy do not contain the information of the
first order derivative".

## Positivity-preserving hybrid HWENO for Navier–Stokes

Fan, Zhang & Qiu (2021) make the hybrid moment-based HWENO of Zhao, Chen & Qiu positivity-preserving
for compressible Navier–Stokes (Euler at $\mathrm{Re}=\infty$):

- **Hybrid.** A troubled-cell indicator selects the cells where the nonlinear HWENO reconstruction,
  preceded by a non-oscillatory limiter on the first moment, is used; elsewhere a linear Hermite
  reconstruction (§1, §4; [hybrid schemes](/methods/hybrid-weno.md)).
- **Flux.** A Lax–Friedrichs-type flux of the total (advective minus viscous) flux, whose coefficient
  must exceed $|v|+\frac1{2\rho^2e}\big(\sqrt{\rho^2q_h^2+2\rho^2e|\tau_v-p|^2}+\rho|q_h|\big)$ (page-local
  viscous stress $\tau_v$ and heat flux $q_h$), after Zhang 2017 (Eqs. (3.4)–(3.5)).
- **Theorem 1 (1-D).** With degree-$k$ reconstruction, the forward-Euler cell average stays in
  $G=\{\rho>0,\ \rho e>0\}$ if the interface traces and the Gauss–Lobatto residual state
  $(\bar u_i-\hat{\mathsf w}u^+_{i-1/2}-\hat{\mathsf w}u^-_{i+1/2})/(1-2\hat{\mathsf w})$ lie in $G$,
  under $\frac{\Delta t}{\Delta x}\max_i(\text{coefficient})\le\hat{\mathsf w}=\frac1{n_{\mathrm{GL}}(n_{\mathrm{GL}}-1)}$,
  $n_{\mathrm{GL}}=\lceil(k+3)/2\rceil$ (Eqs. (3.11)–(3.12); page-local $\hat{\mathsf w}$, the end
  Gauss–Lobatto weight, and $n_{\mathrm{GL}}$ the number of Gauss–Lobatto points, the source's $N$). Theorem 2 is the 2-D analogue (Eqs. (3.29)–(3.30)). Both are enforced by a density-then-
  internal-energy [scaling limiter](/methods/zhang-shu-scaling-limiter.md) on point values only
  ([bound preservation](/properties/bound-preservation.md)).
- **Viscous derivatives.** App. A reconstructs $u_x$ with HWENO at the interfaces of flagged stencils
  and linearly elsewhere; in 1-D the three Hermite cubics combine into the quintic's derivative with
  linear weights $\tfrac{11}{459},\tfrac{44}{765},\tfrac{124}{135}$, Jiang–Shu-type weights with
  exponent 2, and indicators summing only derivative orders 2–3 (App. A.1;
  [smoothness indicators](/definitions/smoothness-indicator.md)). *(Compiler check, not in the sources: the three weights
  sum to 1.)*

Results: about fifth order in 1-D and fourth order in 2-D at $\mathrm{Re}=100$ (Table 4.1); the hybrid
scheme of Zhao et al. without positivity preservation blows up on Examples 4.3–4.7 (Euler), which the
new one runs; the positivity-preserving hybrid saves 59.05–89.64 % of the CPU time of the
non-hybrid positivity-preserving HWENO, with troubled-cell fractions 0.97–19.57 % (Table 4.2;
[Sedov blast wave](/benchmarks/sedov-blast-wave.md), [Leblanc shock tube](/benchmarks/leblanc-shock-tube.md),
[double rarefaction](/benchmarks/double-rarefaction-problem.md)). A moment-based HWENO without the
first-moment modification and without positivity limiter is non-oscillatory on the Lax problem at
$\mathrm{Re}=100$ but oscillates and loses stability at higher Re, so the authors conclude that it
"itself is unstable" (Example 4.2, Fig. 4.1). On the Lax problem the positivity limiter is never
triggered: the first-moment limiter alone makes the hybrid scheme "already very stable". The authors
read that limiter as "artificial viscosity": fewer troubled cells at $\mathrm{Re}=1000$ give slightly
sharper fronts than at $\mathrm{Re}=\infty$ (Example 4.2, §5;
[artificial viscosity](/methods/artificial-viscosity.md)).

## Physical-constraint-preserving HWENO for relativistic hydrodynamics

Cai, Qiu & Wu (2024, §§3–4; arXiv v1 read) build the moment-based finite-volume HWENO of Zhao & Qiu, with "artificial
linear weights", for the special-relativistic Euler equations, where the primitive variables must be recovered from the
conserved ones by a root solve ([relativistic hydrodynamics](/definitions/relativistic-hydrodynamics.md)). The moment
equations are those above, with the four-point Gauss–Lobatto rule in the moment equation (Eqs. (3.2)–(3.3)) and a
global Lax–Friedrichs flux (Eq. (3.4); [Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md)).

- **Linear and nonlinear operators** (§3.1.1–3.1.2). A linear operator fits a quintic to the averages and first moments
  of $I_{i-1},I_i,I_{i+1}$ (sixth order in 1-D); e.g.
  $P_0(x_{i+1/2})=\tfrac{13}{108}\bar u_{i-1}+\tfrac7{12}\bar u_i+\tfrac8{27}\bar u_{i+1}+\tfrac{25}{54}\bar u^{(1)}_{i-1}+\tfrac{241}{54}\bar u^{(1)}_i-\tfrac{28}{27}\bar u^{(1)}_{i+1}$.
  The HWENO operator adds two quadratics, on $\{\bar u_{i-1},\bar u_i,\bar u^{(1)}_i\}$ and $\{\bar u_i,\bar u_{i+1},\bar u^{(1)}_i\}$,
  combined with the quintic in the [CWENO](/methods/cweno.md) form $\omega_0\big(P_0-\sum_{n\ge1}d_nP_n\big)/d_0+\sum_{n\ge1}\omega_nP_n$, with
  Jiang–Shu indicators (e.g. $\beta_1=144(\bar u^{(1)}_i)^2+\tfrac{13}3(\bar u_{i-1}-\bar u_i+12\bar u^{(1)}_i)^2$) and
  $$\alpha_n=d_n\Big(1+\frac{\tau^2}{\beta_n^2+\epsilon}\Big),\qquad \tau=\tfrac12\big(|\beta_0-\beta_1|+|\beta_0-\beta_2|\big)$$
  (page-local $\tau$; Eq. (3.8)), which the authors call scale-invariant, crediting Chen & Wu for the idea that such weights
  suppress oscillations in multiscale relativistic flows (Remark 3.2; [scale invariance](/properties/scale-invariance.md)).
  The values of $d_n$, $\epsilon$ and the KXRCF threshold are not printed.
- **Hybrid procedure** (§3.1.3). A KXRCF indicator marks troubled cells
  ([troubled-cell indicators](/definitions/troubled-cell-indicator.md)); there the first moment is modified by the HWENO
  limiter of Zhao & Qiu, with weights $d_n\big(1+\tau_\ell^2\Delta x/(\beta_{\ell,n}^2+\epsilon)\big)$ (page-local), the
  two inner Gauss–Lobatto values are reconstructed component-wise, and the two interface values characteristic-wise with
  the eigenvectors of the Eulderink–Mellema Roe matrix; elsewhere all four values come from the linear operator
  ([hybrid schemes](/methods/hybrid-weno.md)). The eigenvector pairs $(r,l)$ may be rescaled to $(cr,l/c)$, and the
  "matching" choice $c=\sqrt{|l|/|r|}$ removes the "serious oscillations" that unrescaled or "unitized" ($c=|l|$)
  eigenvectors give on an ultra-relativistic 2-D Riemann problem (Remark 3.3, Example 5.7, Fig. 7;
  [characteristic decomposition](/methods/characteristic-decomposition.md)).
- **Physical-constraint limiter** (§3.1.3, Step 3; Lemma 3.2). A two-stage
  [Zhang–Shu scaling](/methods/zhang-shu-scaling-limiter.md), first on the lab-frame density, then on the concave
  constraint function of the admissible set, is applied at all four Gauss–Lobatto points, the inner ones included,
  because the primitive recovery converges only for admissible states (Remark 3.4), together with the interior value
  $\Pi_i=\big(\bar u_i-\tfrac1{12}u^+_{i-1/2}-\tfrac1{12}u^-_{i+1/2}\big)/(1-\tfrac16)$ of the Gauss–Lobatto
  decomposition, both traces taken from cell $i$ (Eq. (3.11)).
- **Theorem 3.1.** With the end Gauss–Lobatto weight $1/(N_{\mathrm{GL}}(N_{\mathrm{GL}}-1))=\tfrac1{12}$
  ($N_{\mathrm{GL}}=4$), the forward-Euler cell average stays in the admissible set if
  $\Delta t\le\tfrac1{12}\Delta x/a$, $a$ the global Lax–Friedrichs speed; SSP Runge–Kutta keeps it by convexity.
  Theorem 4.1 is the 2-D analogue, $\Delta t\le\tfrac1{12}/(a^{(1)}/\Delta x+a^{(2)}/\Delta y)$, and §4.3 adds a step
  restriction for the axisymmetric source term ([bound preservation](/properties/bound-preservation.md),
  [optimal cell-average decomposition](/methods/optimal-cell-average-decomposition.md)).
- **2-D** (§4, Apps. A–B). Three moments per cell, a $3\times3$ stencil, a quartic that matches the nine averages and the
  centre's two first moments exactly and four first moments in least squares (fifth order), and four quadratics on the
  $2\times2$ sub-blocks with $\tau=\tfrac14\sum_n|\beta_0-\beta_n|$.

The pointwise recovery uses Newton–Raphson methods proved convergent and positivity-preserving (§2). The 1-D scheme reaches
sixth order on an ultra-relativistic smooth problem, where the limiter is needed ($L^1$ errors $3.56\times10^{-1}$ to
$1.74\times10^{-9}$ for $N=30$ to 180, orders 6.00, 5.99, 5.97 at $N=120$, 150, 180; Table 4), the 2-D scheme fifth
order (5.35, 5.20, 5.08; Table 5). Without the limiter the code breaks down after one step on the shock-heating problem
with $|v_0|=1-10^{-10}$ and cannot take one step on the demanding shock–vortex test with minimum pressure
$1.7847\times10^{-20}$; with it only two cells are limited in the 1-D Riemann problem, and the axisymmetric jet with
beam speed 0.99 runs (Examples 5.3–5.4, 5.8–5.9; [shock–vortex interaction](/benchmarks/shock-vortex-interaction.md),
[high-Mach jets](/benchmarks/high-mach-astrophysical-jet.md)).

## Oscillation-eliminating HWENO (OE-HWENO)

Fan & Wu (2024; arXiv v1 read) keep the sixth-order moment-based scheme and replace moment limiting by
a filter applied after every Runge–Kutta stage, carrying the [OEDG](/methods/oedg.md) step of Peng, Sun &
Wu from DG to HWENO. They name the uncontrolled growth of the first moments near discontinuities as the
source of oscillations and nonlinear instability, and set their method against two earlier fixes:
moment limiting, which they say keeps "at most fifth-order accuracy for originally sixth-order HWENO
schemes" (citing Zhao, Chen & Qiu, Li, Shu & Qiu, Zhao & Qiu), and the oscillation-free OF-HWENO of Zhao &
Qiu, which adds stiff damping terms with empirical, problem-dependent parameters to the moment equations
and needs modified exponential Runge–Kutta (§1, Remark 1).

- **HWENO operator** (§2.2.1, App. A). On $I_{i-1},I_i,I_{i+1}$: a quintic $p_0$ matching all three averages
  and moments, a cubic $p_1$ matching the three averages and $\bar u^{(1)}_i$, and two linear polynomials
  on $\{\bar u_{i-1},\bar u_i\}$ and $\{\bar u_i,\bar u_{i+1}\}$, combined in two nested [CWENO](/methods/cweno.md)
  levels ($p_0$ with $p_1$, then $p_1$ with the two linears; the
  [multi-resolution](/methods/multi-resolution-weno.md) structure) with arbitrary positive linear weights
  (0.025 for the lowest-degree polynomials in all tests) and Z-type weights
  $d_l\big(1+\tau/(\beta_l+\epsilon)\big)$, $\tau=(\beta_0-\beta_1)^2$ at the top level and
  $\tau=\big(\tfrac12(|\beta_1-\beta_2|+|\beta_1-\beta_3|)\big)^2$ at the lower one (page-local $\tau$; Eq. (A.2);
  [WENO-Z](/methods/weno-z.md)). The value of $\epsilon$ is not printed. The quintic's interface value,
  $p_0(x^-_{i+1/2})=\tfrac{13}{108}\bar u_{i-1}+\tfrac7{12}\bar u_i+\tfrac8{27}\bar u_{i+1}+\tfrac{25}{54}\bar u^{(1)}_{i-1}+\tfrac{241}{54}\bar u^{(1)}_i-\tfrac{28}{27}\bar u^{(1)}_{i+1}$
  (p. 12). *(Compiler check, not in the sources: these are the coefficients of the linear operator printed by
  Cai, Qiu & Wu (2024) above.)*
- **OE step** (§2.2.2, Theorem 1). The modified moments are the solution, after a pseudo-time $\Delta t$,
  of a linear damping problem in the $\mathbb P^1$ test space, with a coefficient frozen at its initial
  data; it is solved exactly: the cell average is unchanged and
  $$\bar u^{(1)}_i\leftarrow\bar u^{(1)}_i\exp\Big(-a\frac{\Delta t}{\Delta x}\hat\sigma_i\Big),\qquad
  \hat\sigma_i=\frac{\sum_{m=0}^1\Delta x^m\big(\lvert[\![\partial_x^mu_h^*]\!]_{i-1/2}\rvert+\lvert[\![\partial_x^mu_h^*]\!]_{i+1/2}\rvert\big)}{\max_j\lvert\bar u_j-u_\Omega\rvert},$$
  $u_\Omega$ the mean of all cell averages, $a$ the global Lax–Friedrichs speed, $u_h^*$ a *linear*
  sixth-order Hermite reconstruction whose jumps are explicit in the averages and moments (Eq. (2.17)),
  e.g. $[\![u_h^*]\!]_{i+1/2}=\tfrac1{108}\big(-13\bar u_{i-1}-31\bar u_i+31\bar u_{i+1}+13\bar u_{i+2}-50\bar u^{(1)}_{i-1}-370\bar u^{(1)}_i-370\bar u^{(1)}_{i+1}-50\bar u^{(1)}_{i+2}\big)$
  ($\hat\sigma_i$, $u_\Omega$, $u_h^*$ page-local; $\hat\sigma_i=0$ when $\max_j|\bar u_j-u_\Omega|=0$). The step
  costs one multiplication per moment and keeps local conservation (Remarks 2–3). For systems the largest
  coefficient over the components damps all of them (Eq. (2.29)); in 2-D both first moments are multiplied by
  $\exp(-a^{(1)}\frac{\Delta t}{\Delta x}\hat\sigma_{i,j}-a^{(2)}\frac{\Delta t}{\Delta y}\tilde\sigma_{i,j})$ (Theorem 8; page-local
  $\tilde\sigma_{i,j}$). *(Compiler check, not in the sources: the jump coefficients of Eq. (2.17) follow from
  the printed one-sided values of the quintic, and those values reproduce constant and linear data.)*
- **Accuracy.** Theorem 2: under $a\Delta t/\Delta x\le C_{\mathrm{cfl}}<1$, for $u\in C^{k+1}$ and periodic
  data, if the moments are $(k+1)$th-order accurate, so are the filtered ones; the proof bounds
  $1-e^{-x}\le x$ and uses the vanishing jumps of the linear Hermite reconstruction on smooth data, in the
  nontrivial case $\max_j|\bar u_j-u_\Omega|\ge C>0$. Theorem 9 is the 2-D version (proof omitted).
- **Invariance** (Theorems 4–7). The OE operator is invariant under affine maps of the data, a
  dimensionless transformation of the stencil data makes the HWENO operator invariant, and the scheme is
  evolution invariant ([scale invariance](/properties/scale-invariance.md)).
- **Bound preservation** (§2.4, Theorem 11). The OE step leaves cell averages unchanged, so the
  forward-Euler bound-preserving analysis is that of the cell-average update. With the 2-D
  [optimal cell-average decomposition](/methods/optimal-cell-average-decomposition.md) of Cui, Ding &
  Wu, the bound-preserving condition is $\Delta t(a^{(1)}/\Delta x+a^{(2)}/\Delta y)\le\varpi$, with
  $\varpi=2-\sqrt{14}/2\approx0.1292$ when $a^{(1)}\Delta y=a^{(2)}\Delta x$, against $\tfrac1{12}$ for the classical
  Zhang–Shu decomposition; it is presented as the first use of the 2-D optimal decomposition for HWENO,
  also valid without OE (Remark 5). A [Zhang–Shu scaling](/methods/zhang-shu-scaling-limiter.md) and the
  Euler positivity limiter enforce the hypotheses (Remark 4; [bound preservation](/properties/bound-preservation.md)).

Results (SSP-RK3 with an OE step after each stage, $C_{\mathrm{cfl}}=0.45$, $\Delta t\propto\Delta x^2$ in the
accuracy tests; §3): $\ell^\infty$ orders 6.10–6.58 on 1-D and 5.38–6.43 on 2-D
[Burgers](/benchmarks/burgers-equation-tests.md) (Table 3.1) and 6.47–6.99 on the 1-D and 2-D Euler
[density wave](/benchmarks/density-wave-advection.md) (Table 3.2), above six, which the authors attribute to
the high-order damping dominating the error, as in OEDG and OF-HWENO. ADR curves with and without OE are
"nearly identical" (Fig. 2.1; [approximate dispersion relation](/definitions/approximate-dispersion-relation.md)).
OE-HWENO resolves the [Woodward–Colella](/benchmarks/woodward-colella-blast-wave.md) problem better than
OF-HWENO; on the 1-D [Sedov](/benchmarks/sedov-blast-wave.md) problem OF-HWENO is sensitive to its parameter
(best of $\{2.5,3.5,5,10\}$ still oscillates) and standard HWENO with the positivity limiter oscillates,
while OE-HWENO with it is "essentially non-oscillatory" (Ex. 6); [double rarefaction](/benchmarks/double-rarefaction-problem.md)
runs without the positivity limiter, and [Leblanc](/benchmarks/leblanc-shock-tube.md),
[double Mach reflection](/benchmarks/double-mach-reflection.md), 2-D Sedov and the Mach 2000
[jet](/benchmarks/high-mach-astrophysical-jet.md) with it, where standard HWENO with the positivity limiter
shows "obvious" non-physical oscillations (Ex. 7–12). No timings are reported.

## Hermite candidates for nodal spectral-difference limiting

Chen & Fu (2024) build a compact limiter for the nodal spectral difference (SD) method at third and
fourth order from Hermite candidates. From the nodal polynomials of the target cell and its two face
neighbours in one direction they compute, by quadrature, cell averages and the cell averages of the
first and second derivatives, $\overline{\partial_xu}_j=\frac1{\Delta x}\int_{I_j}\partial_xu_h\,dx$ and
$\overline{\partial^2_xu}_j$ (page-local), and fit on $I_i$ (§5, Eqs. (36), (51)):

- three quadratics: $p_0$ on the averages of $I_{i-1},I_i$ and $\overline{\partial_xu}_{i-1}$; $p_1$ on the three
  averages; $p_2$ on the averages of $I_i,I_{i+1}$ and $\overline{\partial_xu}_{i+1}$;
- for fourth order, four cubics: on the three averages plus $\overline{\partial_xu}_{i-1}$ or plus
  $\overline{\partial_xu}_{i+1}$, and on two averages plus both derivative averages of the left or of the right
  neighbour.

All candidates have the cell's average, and the limited polynomial is a **direct convex combination**
$\sum_k\omega_kp_k$, against earlier compact HWENO limiters that limit low-order moments one at a time (§1). The
linear weights are fixed by requiring the cell-averaged first derivative to third order and the second
to second order; they depend on the solution-point set, e.g. for the third-order SD points
$-\tfrac{11}{96}d_0+\tfrac5{24}d_1-\tfrac{11}{96}d_2=\tfrac1{24}$ with $d_0=d_2$, giving
$(d_0,d_1,d_2)=(\tfrac8{31},\tfrac{15}{31},\tfrac8{31})$; with the fourth-order SD points the same
three quadratics take $(\tfrac14,\tfrac12,\tfrac14)$, and the four cubics $(\tfrac5{14},\tfrac5{14},\tfrac17,\tfrac17)$
(Eqs. (38)–(54)). *(Compiler check, not in the sources: the three printed conditions give $d_0=d_2=\tfrac8{31}$.)*
The nonlinear weights are Jiang–Shu-type or TENO with an adaptive cut-off; at fourth order all seven
candidates are classified and the quadratics are discarded when any cubic survives (§5.4–5.7;
[adaptive TENO](/methods/adaptive-teno.md), [WENO limiters for DG](/methods/weno-limiter-dg.md)). The limiter
acts dimension by dimension on lines of solution points, characteristic-wise, and leaves cell averages
unchanged (§6–§7, Eq. (75)). On the 2-D Euler density wave, with every cell forced troubled, all limiters
keep the design order, the TENO-A errors about half of the WENO ones (Table 1).

## Finite-difference HWENO without the target-point derivative (HWENO-R)

Finite-difference HWENO (Liu & Qiu; Zhao, Zhang & Qiu; Zhang & Zhao's HWENO-L, as recalled by Fan, Zhao,
Xiong & Qiu 2023, §1) evolves the point values $u_i$ together with $v_i=\partial_xu(x_i)$ through
$\partial_tv+\partial_x\big(f'(u)v\big)=0$, both in [conservative finite-difference](/definitions/conservative-finite-difference-scheme.md)
form with Lax–Friedrichs splitting of $f$ and of $f'(u)v$ (page-local $h_j$ the split derivative
fluxes; Eqs. (2.2)–(2.3)). Fan et al. (2023, §2.1) build **HWENO-R** for the Euler equations by
**dropping the derivative at the target point** from the flux reconstruction:

- the large candidate is the quartic $q_0$ matching the three point fluxes $f^+_{i-1},f^+_i,f^+_{i+1}$ as
  cell averages and the two derivative fluxes $h^+_{i-1},h^+_{i+1}$; the small candidates are the linear
  polynomials on $\{f^+_{i-1},f^+_i\}$ and $\{f^+_i,f^+_{i+1}\}$ (Fig. 2.1(a));
- $q_0(x_{i+1/2})=-\tfrac{23}{120}f^+_{i-1}+\tfrac{19}{30}f^+_i+\tfrac{67}{120}f^+_{i+1}-\Delta x\big(\tfrac3{40}h^+_{i-1}+\tfrac7{40}h^+_{i+1}\big)$
  (sign corrected, see Qualifications), and the derivative flux is the linear value
  $\hat h^+_{i+1/2}=q_0'(x_{i+1/2})=\tfrac1{8\Delta x}(3f^+_{i-1}-16f^+_i+13f^+_{i+1})+\tfrac18h^+_{i-1}-\tfrac38h^+_{i+1}$,
  which "works well without spurious oscillations" (Eq. (2.5));
- the nonlinear combination is the [CWENO](/methods/cweno.md)/WENO-ZQ one with
  $\tau=\big(\tfrac12(|\beta_0-\beta_1|+|\beta_0-\beta_2|)\big)^2$ (page-local), $\epsilon=10^{-10}$ and any
  positive linear weights, recommended $(0.99,0.005,0.005)$; $\tau/(\beta_k+\epsilon)=O(\Delta x^4)$ is
  asserted by Taylor expansion (Step III);
- the derivative unknowns pass through a fifth-order HWENO limiter, a point-value Hermite quartic and two
  linear interpolants with weights $(0.9,0.05,0.05)$, but only in the stage values of SSP-RK3; the
  spatial operator sees the unlimited derivatives (Eqs. (2.6)–(2.7));
- in 2-D the mixed derivative fluxes are fourth-order linear,
  $\tfrac1{12}(-q_{i-1}+7q_i+7q_{i+1}-q_{i+2})$ (page-local $q$), not the third-order split
  reconstruction of earlier schemes (Eq. (2.11)); reconstruction is characteristic-wise for the main
  fluxes and component-wise for the derivative fluxes (Remark 2.2).

HWENO-L also uses $h^+_i$, i.e. $v_i$, in a quintic and a sixth-order reconstruction, but its limiter is fifth
order, so the scheme is fifth order; HWENO-R makes the reconstruction order equal the scheme order
(Remark 2.1). The authors attribute HWENO-L's failures to the unlimited $v_i$: after one step of the 1-D
[Sedov](/benchmarks/sedov-blast-wave.md) problem its density derivative exceeds 4000, against below 20
for HWENO-R, and HWENO-L fails even with a positivity-preserving flux limiter (Example 3.5, Fig. 3.9).
HWENO-R runs the 1-D and 2-D Sedov, [double rarefaction](/benchmarks/double-rarefaction-problem.md) and
[Leblanc](/benchmarks/leblanc-shock-tube.md) problems without positivity limiters; the Mach 2000
[jet](/benchmarks/high-mach-astrophysical-jet.md) and a Mach 10 reflection–diffraction problem need the
parametrized flux limiter of Xiong, Qiu & Xu, active in 0.0146 % and 0.0012 % of cells
([positivity-preserving flux limiter](/methods/positivity-preserving-flux-limiter.md)). It is fifth order
on Burgers, 1-D Euler and a near-vacuum isentropic vortex (Tables 3.1–3.3), more accurate than WENO-ZQ
at equal CPU time (CPU ratios 1.2–1.8, error ratios about 1/5), slightly cheaper than HWENO-L, and on
the [Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md) at $120\times480$ comparable
to WENO-ZQ at $240\times960$ (Example 3.13). Fan et al. (§1) count three points for fifth-order HWENO
against five for WENO.

## HWENO candidates on a finite element mesh

Kuzmin & Vedral (2023, §5, Eq. (11)) outline, "without claiming originality", the Zhong–Shu-type
construction they use. For a cell $K_e$ with finite element polynomial $u_h^e\in\mathbb P^N$ and its
von Neumann neighbours $e'$ (sharing a point, edge or face; at least $d+1$ of them in $d$ dimensions):

- each neighbour polynomial is extended into $K_e$ and its mean corrected,
  $$u^e_{h,l}(x)=u_h^{e'}(x)+\pi_e\big(u_h^e-u_h^{e'}\big),\qquad \pi_ev=\frac1{|K_e|}\int_{K_e}v\,dx,$$
  so that the candidate has the cell's mean and the neighbour's derivatives; the cell's own
  polynomial is the candidate $l=0$ (page-local index $l$, mean operator $\pi_e$);
- the candidates are blended with linear weights that favour the central candidate,
  $\tilde\omega_0=1-m_e\cdot10^{-3}$, $\tilde\omega_l=10^{-3}$ ($m_e$ non-central candidates;
  $\tilde\omega_l=0.2$ for all five candidates in the KPP test), and Jiang–Shu-type nonlinear weights
  $\omega_l\propto\tilde\omega_l/(\epsilon+\beta_l)^2$, $\epsilon=10^{-6}$, with
  $\beta_l=\|u^e_{h,l}\|_e^{\mathsf q}$ a power of the scaled Sobolev seminorm of the candidate
  (page-local sensor exponent $\mathsf q\ge1$, $\mathsf q=1$ by default; not the registry's weight
  exponent $q$)
  ([smoothness indicators](/definitions/smoothness-indicator.md),
  [WENO-JS](/methods/weno-js-reconstruction.md)).

Because the seminorm contains only derivatives, the mean correction does not affect the indicator and
is unnecessary in practice (Remark 3). A smaller central linear weight makes shock detection more
reliable and the stabilization stronger (§5, used in the KPP test). Remark 4 proposes, without
implementing them, additional Hermite candidates from vertex neighbours and Lagrange candidates
interpolated on the convex hull of neighbouring barycentres, generalizing a DG-$\mathbb P^1$
construction of Luo et al. to arbitrary order.

## The simple WENO limiter for DG

The same candidates, the target polynomial and its mean-corrected neighbours, are the simple WENO
limiter of Zhong & Shu and its triangle version by Zhu, Zhong, Shu & Qiu, as recalled by Du, Shu &
Zhong (2022, §1, §3.1), which **overwrites** the DG polynomial of a troubled cell
([WENO limiters for DG](/methods/weno-limiter-dg.md)). Their improvement concerns systems: for each
edge normal $n_l$ of a triangle the original limiter projects all four polynomial vectors (target and
three neighbours) on the characteristic fields of the normal Jacobian at the target average; the new
one projects only the target polynomial $p_0$ and the corrected neighbour across edge $l$, combines
the two per field,

$$p^{\mathrm{new}}_l=\omega_0\,L_lp_0+\omega_1\,L_l\tilde p_l,\qquad \omega_i\propto\frac{d_i}{(\epsilon+\beta_i)^2},$$

maps back with $R_l$, and averages the three directional results with the neighbour areas as weights,
$p^{\mathrm{new}}_0=\sum_lR_lp^{\mathrm{new}}_l|K_l|/\sum_l|K_l|$ (Eqs. (3.1)–(3.8); page-local
$p$, $\tilde p_l$, $L_l$, $R_l$ for the polynomial vectors and the directional eigenvector matrices).
The linear weights are $d_0=0.999$, $d_1=0.001$ on triangles and $0.9995$, $0.0005$ on polygonal meshes
built from point clouds (where the direction is the centre-to-centre vector and $N_j$ neighbours give
$N_j$ two-polynomial combinations instead of one $(N_j+1)$-polynomial one, §3.2, Eq. (3.9)), and
$\epsilon=10^{-6}$; any positive $d_0+d_1=1$ is argued to keep the accuracy, since both candidates are
$(N+1)$th-order in smooth regions (§3.1). The cell average is preserved because each neighbour is
shifted to the target average ([characteristic decomposition](/methods/characteristic-decomposition.md),
[troubled-cell indicators](/definitions/troubled-cell-indicator.md)). Numerically, with the KXRCF
threshold lowered so that up to 91 % of the cells are flagged, both limiters keep the design order
and the error size of unlimited DG for $\mathbb P^1$–$\mathbb P^3$ (Tables 4.1–4.6), the new one
perturbing the error less (e.g. $\mathbb P^1$, $h=2\pi/10$, $L^2$ $2.46\times10^{-2}$ against
$3.87\times10^{-2}$, unlimited $5.63\times10^{-3}$); on shock problems it saves 6–55 % of the CPU time,
most for $\mathbb P^2$ and point clouds, and reduces the spurious Mach stem of the $\mathbb P^2$
[forward-facing step](/benchmarks/forward-facing-step.md) (Tables 4.7–4.18, Fig. 4.9). The authors'
attribution of the sharper resolution to "less information being used for reconstruction in each
direction" is not isolated by any experiment.

Other passages only cite HWENO limiters for RKDG: Du, Shu & Zhong (2022, §1) as earlier
wider-stencil and compact WENO limiters; Yu & Hesthaven (2022, §1) as reducing the stencil, adding that WENO and HWENO
limiters reconstructing whole polynomials are "difficult to extend … to higher order cases (typically
higher than 3rd order) due to the stability issue of extrapolation"; Bai & Li (2022, §3.1.5) use a
simple or Hermite WENO limiter (their refs. [90, 91]) only on their two-phase Shu–Osher problem.

## Use as a sensor, not a limiter

Classical RKDG schemes with WENO or HWENO limiters **overwrite** the solution in troubled cells by the
reconstruction. Kuzmin & Vedral (2023, Remark 2) do not: the reconstruction $u_h^{e,*}$ serves only to
compute a cellwise blending factor

$$\varsigma_e=1-\min\Big\{1,\Big(\frac{\|u_h^e-u_h^{e,*}\|_e}{\|u_h^e\|_e}\Big)^{\mathsf q}\Big\}$$

(page-local; the source writes $\gamma_e$ and $q$; Eq. (9)), which blends a high-order symmetric projection stabilization with low-order
artificial viscosity, so the semi-discrete scheme keeps the structure of a continuous Galerkin method
([WENO-stabilized continuous Galerkin](/methods/weno-stabilized-continuous-galerkin.md),
[artificial viscosity](/methods/artificial-viscosity.md),
[troubled-cell indicators](/definitions/troubled-cell-indicator.md)). They argue that overwriting
DG-WENO schemes "have more in common with finite volume methods". If the finite element solution on
the stencil union is a polynomial of degree $\le N$, every candidate equals it, $\varsigma_e=1$ for any
nonlinear weights, and polynomial solutions are reproduced exactly (Remark 6). The moment modification
of Li, Shu & Qiu (2022d), by contrast, does overwrite the evolved moment in flagged cells.

## Hermite TENO

Fu (2023, §3.10) lists HTENO (Wibisono et al.), a Hermite-polynomial compact variant of
[TENO](/methods/targeted-eno.md); Ye et al. (2022, §1) cite it among the TENO extensions. No formulas
are given in the ingested sources.

## Qualifications

- **Linear weights.** Li, Shu & Qiu (2022d) state in the Abstract and §4 that the linear weights "can be
  any positive numbers as long as their sum equals one", but in §1 that their gap "cannot be too
  large" and in Remark 1 that larger weights on higher-degree polynomials make the scheme less stable;
  "any" holds for smooth-region accuracy only.
- **HWENO-R slips and limits.** Fan et al. (2023, §2.1) print
  $-\Delta x\big(\tfrac3{40}h^+_{i-1}-\tfrac7{40}h^+_{i+1}\big)$ in $q_0(x_{i+1/2})$. *(Compiler check, not in
  the sources: solving the five Hermite conditions gives $+\tfrac7{40}$; for $f=x$ the corrected value
  returns $x_{i+1/2}$, the printed one does not.)* Their printed indicator of the limiter's point-value
  quartic does not equal the Jiang–Shu integral of that quartic
  ([smoothness indicators](/definitions/smoothness-indicator.md)). "Arbitrary" positive linear weights
  coexist with a recommended band $\gamma_0/\gamma_1\in[100,300]$, $d_0/d_1\in[10,30]$ (Example 3.4), and
  "robust without positivity limiters" coexists with negative minimum pressures on coarse meshes of the
  near-vacuum vortex run without limiters (Table 3.3).
- **Heuristic resolution argument.** Remark 1 of Li, Shu & Qiu (2022d) assumes the low-order indicators
  stay $O(\Delta x^2)$ in a cell that contains a discontinuity, and that after modification all
  indicators behave as on smooth data, although the modified moment is built from averages that
  straddle the jump; the resolution gain is supported by figures only. Their claim of "smaller errors
  than multi-resolution WENO under the same meshes" (§4) is not shown in the paper.
- Li, Shu & Qiu (2022d) justify the KXRCF exponent $(l+1)/3$ by asking the indicator to converge "twice
  as fast" in smooth regions as it diverges at discontinuities; Krivodonova et al. use $(k+1)/2$.
- **Order of the positivity CFL under SSP-RK3.** Fan et al. (2021, §3.3) state that Theorems 1–2 hold
  for SSP-RK3 "if the CFL is one third" of the forward-Euler bound; the Shu–Osher RK3 is a convex
  combination of forward-Euler steps of size $\Delta t$, so the convexity argument gives the
  forward-Euler bound itself, not a third of it *(compiler check, not in the sources)*; Wong et al.
  (2021, §5.3) state this for their limiters, the SSP-RK extension being "trivial since SSPRK time
  stepping schemes are convex combinations of Euler forward steps"
  ([SSP Runge–Kutta](/methods/ssp-runge-kutta.md)).
- Fan et al. (2021) print $\rho e=(\gamma-1)(E-\tfrac12m^2/\rho)$ in Eq. (3.7) (the pressure; their
  2-D Eq. (3.25) has no $(\gamma-1)$) and a numerator $\rho e(\hat q^k)-\varepsilon$ in the implemented
  1-D energy limiter, where (3.15) and the 2-D version give $\rho e(\bar P_i)-\varepsilon$; the
  Lax-problem CPU savings quoted in the text (77.68 %, 75.08 %) differ from Table 4.2 (71.20 %,
  69.98 %). The 2-D derivative reconstruction is third order (App. A.2) while the 2-D scheme is
  reported fourth order.
- **Step bound against the tests.** Cai, Qiu & Wu (2024) prove the physical-constraint property under
  $\Delta t\le\tfrac1{12}\Delta x/a$, but run all tests at a "CFL number" of 0.6 without defining it (§5). *(Compiler
  check, not in the sources: if the CFL number is taken relative to $\Delta x/a$, 0.6 exceeds the proved bound by a factor
  7.2.)* Their claim that the hybrid Newton recovery is superior in speed "across all tests" (§5.1) is not borne out by
  their own timings on the third sample set, where the linearly convergent hybrid of Chen & Wu is faster.
- Cai, Qiu & Wu (2024, §3.1.2) state that the weights "remain unchanged" under $(\bar u,\bar u^{(1)})\mapsto\sigma(\bar u,\bar u^{(1)})$
  for any $\sigma\ne0$. *(Compiler check, not in the sources: $\tau^2$ and $\beta_n^2$ both scale as $\sigma^4$, so the
  ratio is invariant only up to $\epsilon$, whose value is not printed.)*
- **What "fifth order" of moment limiting measures.** Fan & Wu (2024, §1, §2.2.2) say that moment
  limiting keeps "at most fifth-order accuracy" for sixth-order HWENO, citing Li, Shu & Qiu (2022d) among
  others; Li, Shu & Qiu report sixth order (5.96–6.49) for HWENO6-M5-I, whose modification acts only in flagged
  cells, and fifth order only when every cell is modified (Tables 3.1–3.4). The two statements are
  compatible: the first concerns the modification when it is active, the second smooth tests where it is not.
- **OE-HWENO slips** (Fan & Wu 2024, arXiv v1). The printed optimal decomposition weight,
  $\big[\tfrac{14}3+\tfrac23\sqrt{78\varkappa^2+46}\cos\big(\tfrac13\arccos\frac{1476\varkappa^2-244}{78\varkappa^2+46}\big)\big]^{-1}$
  with the anisotropy $\varkappa$ of the decomposition, is undefined at $\varkappa=0$, where the arccos argument is $-244/46$.
  *(Compiler check, not in the sources: with the denominator $(78\varkappa^2+46)^{3/2}$ the argument is $-0.782$ and
  the formula gives $0.1291713=2-\sqrt{14}/2$, the value printed on p. 31.)* In Tables 3.1–3.2 the $\ell^2$
  order columns repeat the $\ell^1$ ones digit for digit. *(Compiler check, not in the sources: recomputed from the printed $\ell^2$
  errors they are, e.g., 6.83, 6.53, 6.32, 6.36, 6.47 for 1-D Burgers against the printed 6.83, 6.53, 6.40,
  6.37, 6.54; the $\ell^\infty$ and $\ell^1$ columns agree with their errors.)* The 2-D reconstruction (2.40) is
  printed with $\gamma$ and $\omega$ exchanged relative to the 1-D Eq. (2.13) and App. B.
- Chen & Fu (2024, Eq. (3)) call the SD solution points "the Gauss points", but print
  $X_s=-\tfrac12\cos\big(\tfrac{2s-1}{2N}\pi\big)$ on $[-\tfrac12,\tfrac12]$, Chebyshev–Gauss points *(compiler
  check: for $N=3$ these are $0,\pm\sqrt3/4$, against $0,\pm\sqrt{15}/10$ for Gauss–Legendre)*; the linear
  weights depend on this choice.
- Li et al. (2022b, Eq. (8)) — the WENO-ZN paper — call the rescaled Legendre basis used by Balsara et
  al. for smoothness indicators "Hermite polynomials"; that reconstruction is not Hermite WENO.
- The nonlinear HWENO reconstruction of Kuzmin & Vedral is printed once with a tilde
  ($\tilde u_h^{e,*}$) and referred to without it elsewhere; they are the same object.

# Citations

- [Li, Shu & Qiu (2022d)](/sources/li-2022-d.md) — Abstract; §1; §2.1–2.2, Eqs. (2.2)–(2.34), (2.36)–(2.59), Remarks 1–3; §3, Tables 3.1–3.4, Examples 3.5–3.10; §4.
- [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) — §1; §3, Eqs. (3.2)–(3.33), Theorems 1–2; §4, Tables 4.1–4.2, Fig. 4.1; §5; App. A.
- [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) — §3, Eq. (8); Eq. (9); §5, Eq. (11), Remarks 2–4, 6; §7.4.
- [Fu (2023)](/sources/fu-2023.md) — §1; §3.10.
- [Ye et al. (2022)](/sources/ye-2022.md) — §1.
- [Li et al. (2022b)](/sources/li-2022-b.md) — §2, Eq. (8).
- [Du, Shu & Zhong (2022)](/sources/du-2022.md) — §1; §3.1–3.2, Eqs. (3.1)–(3.9); §4, Tables 4.1–4.18, Fig. 4.9.
- [Yu & Hesthaven (2022)](/sources/yu-2022.md) — §1.
- [Bai & Li (2022)](/sources/bai-2022.md) — §2.6; §3.1.5.
- [Fan, Zhao, Xiong & Qiu (2023)](/sources/fan-2023.md) — §1; §2.1–2.3, Eqs. (2.2)–(2.11), Remarks 2.1–2.4; §3, Tables 3.1–3.4, Examples 3.4–3.13, Fig. 3.9; App.
- [Cai, Qiu & Wu (2024)](/sources/cai-2024.md) — §3.1, Eqs. (3.2)–(3.8), Remarks 3.2–3.4; Lemma 3.2, Theorem 3.1; §4, Theorem 4.1, Apps. A–B; §5, Examples 5.2–5.9, Tables 4–5 (arXiv v1).
- [Fan & Wu (2024)](/sources/fan-2024.md) — §1; §2.1–2.4, Eqs. (2.2)–(2.57), Theorems 1–11, Remarks 1–5; §3, Tables 3.1–3.2, Examples 1–12; App. A–C (arXiv v1).
- [Chen & Fu (2024)](/sources/chen-2024.md) — §1; §2, Eq. (3); §5, Eqs. (36)–(69); §6–§7, Eqs. (70)–(75); §9.1, Table 1.
