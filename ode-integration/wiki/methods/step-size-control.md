---
type: Method
title: "Step-size control: error-based controllers, PID filters and CFL control"
description: "Adaptive time stepping: a scaled norm of the embedded local-error estimate decides acceptance and an I, PI, PID or Gustafsson controller sets the next step; the page covers controller stability and tuning, error- versus CFL-based control, temporal-spatial error balancing, control with relaxation, stabilized, Taylor, positivity-adapted and SDC methods, multirate, cost-based and multistep control."
status: established
aliases: [adaptive time stepping, balanced adaptive time stepping, space–time error balancing, error control, PID controller, PI controller, digital-filter step-size controller, Gustafsson controller, CFL-based step size control, step size control stability, stability-limit detection, H-M controller, multirate step-size control, cost-based step-size control, LASA, adaptive SDC, Delta t-adaptivity, Delta t-k-adaptivity, p-adaptive deferred correction, order adaptivity]
tags: [step-size-control, explicit, runge-kutta, software]
timestamp: 2026-10-20T16:00:00Z
---

# Step-size control: error-based controllers, PID filters and CFL control

**Error-based step-size control** computes, after each step, a scaled local-error estimate
$\mathrm{err}_n$ (usually from an [embedded pair](/methods/embedded-runge-kutta-pair.md),
$y_{n+1}-\hat y_{n+1}$), accepts the step iff $\mathrm{err}_n\le1$, and chooses the next step
$h_{n+1}$ from the current and past estimates with a **controller**. **CFL-based control**
instead sets $h_n$ from a Courant number $\nu$ and the current wave speeds. The sources agree
that a time integrator is the triple *(main method, error estimator, controller)*, not the main
method alone (Ranocha et al. 2022, §8; Fekete et al. 2022, §3); pair and controller must be
designed together for stability-limited semidiscretizations
([Ranocha et al. 2025](/sources/ranocha-2025.md), §2.4), and with the main method fixed the
choice of the estimator alone changes the number of accepted steps by up to a factor of about
1.85 ([Belardo et al. 2026](/sources/belardo-2026.md), Tables 2–3; section *Choice of the error
estimator* below).

## Error norm and acceptance

The sources use a componentwise tolerance $\mathrm{atol}_i+\mathrm{rtol}\,|y_i|$ and either a
weighted root-mean-square or a max norm:

$$\mathrm{err}_n=\lVert y_{n+1}-\hat y_{n+1}\rVert_{\mathrm{WRMS}}
=\Bigl(\frac1d\sum_{i=1}^d\Bigl(\frac{y_{n+1,i}-\hat y_{n+1,i}}{\mathrm{atol}_i+\mathrm{rtol}\,\max\{|y_{n+1,i}|,|\hat y_{n+1,i}|\}}\Bigr)^2\Bigr)^{1/2},$$

as in [Ranocha et al. (2022)](/sources/ranocha-2022.md) (§2.2, Eq. (2.7)). Conventions differ
in the scale:

- Ranocha et al. scale by $\max\{|y_{n+1,i}|,|\hat y_{n+1,i}|\}$ and argue that the WRMS norm
  decouples the time-integration parameters from the spatial discretization and weighs degrees
  of freedom on different refinement levels equally, unlike a quadrature-based norm (§2.2).
- [Fekete et al. (2022)](/sources/fekete-2022.md) use the max norm with scale
  $\mathrm{atol}+\mathrm{rtol}\max(|y_n|,|y_{n+1}|)$ (§3.1, Eq. (17)).
- [Reynolds et al. (2023)](/sources/reynolds-2023.md) ([ARKODE](/software/arkode.md)) use WRMS
  weights $(\mathrm{rtol}\,|y_{n,i}|+\mathrm{atol}_i)^{-1}$ built from the solution at the start
  of the step, multiply the estimate by a bias factor larger than one to account for the
  unknown error constant, and add residual weights for equation-unit quantities when the mass
  matrix is not the identity (§3.1–3.2, Eqs. (12)–(14), (17)).
- [Gardner et al. (2022)](/sources/gardner-2022.md) give the SUNDIALS WRMS norm and its
  many-vector form, which needs one global reduction instead of one per subvector (§4.2,
  Algorithm 1).
- Ranocha et al. (2025) document two implementations of the same WRMS norm over all degrees
  of freedom (§2.3, Eq. (2.7)). The scale is $\mathrm{atol}+\mathrm{rtol}\max\{|y_{n+1,i}|,|\tilde y_i|\}$
  with $\tilde y=y_n$ in OrdinaryDiffEq.jl and $\tilde y=\hat y_{n+1}$ in PETSc ($\tilde y$
  page-local), and the norm is floored at about $2.2\times10^{-16}$ (OrdinaryDiffEq.jl) or
  $10^{-10}$ (PETSc). The PETSc variant is the scale written by Ranocha et al. (2022). See
  [DifferentialEquations.jl](/software/differentialequations-jl.md) and
  [PETSc TS](/software/petsc-ts.md).
- [Vermeire (2023)](/sources/vermeire-2023.md) uses the max norm with the scale of Fekete et
  al., $\mathrm{atol}+\mathrm{rtol}\max(|y_n|,|y_{n+1}|)$ (§5, Eqs. (29)–(31), (34)), and
  Belardo et al. (2026) the same scale for a scalar problem (§4).

## Controllers

With $k=\min(p,\hat p)+1$, the PID controller in the form of Ranocha et al. (Eq. (2.6)),
written in registry notation, is

$$h_{n+1}=h_n\,\mathrm{err}_n^{-\beta_1/k}\,\mathrm{err}_{n-1}^{-\beta_2/k}\,\mathrm{err}_{n-2}^{-\beta_3/k}.$$

$\beta=(1,0,0)$ is the deadbeat **I controller**, $\beta_3=0$ a **PI controller**. Ranocha et al.
call the I controller "in some sense optimal in the asymptotic regime" (§6.1); Reynolds et al.
call it the "standard" method of most public solvers (§3.2). Parameter values reported by the
sources, translated to this sign convention:

| Controller | $(\beta_1,\beta_2,\beta_3)$ | Source |
|---|---|---|
| I | $(1,0,0)$ | Fekete et al. (2022), Eq. (20); Ranocha et al. (2022) §6.1 |
| PI | $(0.8,-0.31,0)$ | Fekete et al. (2022), Eq. (21) |
| PID | $(0.58,-0.21,0.10)$ | Fekete et al. (2022), Eq. (22) |
| PI42 / PI33 / PI34 | $(0.60,-0.20,0)$ / $(0.66,-0.33,0)$ / $(0.70,-0.40,0)$ | Ranocha et al. (2022), Table 1 |
| PID of Kennedy–Carpenter | $(0.49,-0.34,0.10)$ | Ranocha et al. (2022), §2.2 |
| PID of Fekete et al., reused | $(0.58,-0.21,0.10)$ | Vermeire (2023), Eq. (33) |
| PI42 of Ranocha et al., reused | $(0.6,-0.2,0)$ | [Babbar & Chandrashekar (2025)](/sources/babbar-2025.md), §5.2 |
| per-pair controllers of Ranocha et al. (2022), reused | Table 11 below | Ranocha et al. (2025), Tables 1–6 |

Fekete et al. also use Gustafsson's explicit (predictive) controller with gains 0.367 and 0.268,
an I step on the first step and an error floor $\mathrm{err}>10^{-10}$ (Eq. (23)).
ARKODE offers PID (its default), PI, I, explicit and implicit Gustafsson controllers, an "ImEx"
Gustafsson controller that takes the smaller of the two, and user-supplied controllers; its
default parameters were tuned by "an exhaustive genetic optimization" over dozens of test
problems, including most of the Bari "Test Set for IVP Solvers", but the controller formulas
and values are not printed (Reynolds et al. 2023, §3.2).

**Exponent denominator.** Ranocha et al. use $k=\min(p,\hat p)+1$, usually $k=p$ under local
extrapolation (§2.2), and Ranocha et al. (2025) keep this choice, which equals the main order
for their pairs (§2.3); Fekete et al. print $p$ without saying whether the main or the embedded
order is meant (§3.1), and so does Vermeire (2023, Eq. (33)), where the main order is 2 and the
embedded order 1, a factor of two in the exponents; ARKODE uses the embedding order by default
and the main order on request (Reynolds et al. §3.2).

**Elementary controller.** Belardo et al. (2026, §4) use "the controller of the ode23tx
textbook code", printed as $h_{n+1}=h_n\min\bigl(5,\,0.8(\mathrm{rtol}/\mathrm{err}_n)^{1/3}\bigr)$
with acceptance iff $\mathrm{err}_n\le1$, for the third-order Bogacki–Shampine pair (see
Qualifications).

**Limiters and rejections.** All three implementations bound the step ratio, with different
rules:

- Fekete et al. apply a safety factor 0.9 and bound the ratio to $[0.1,5]$; after a rejection
  the upper bound drops to 0.9, a change made to stop an observed infinite loop (Eqs. (18)–(19)).
- Ranocha et al. mention the smooth limiter $1+\arctan(x-1)$ of Söderlind and Wang. They accept a
  step iff the controller's factor is at least $0.9^2=0.81$, and retry otherwise with the PID
  step. A step whose solution leaves physical bounds (negative density or pressure) is rejected
  and retried with $h$ divided by 4 (§2.2). Ranocha et al. (2025) make the arctan limiter the
  default and state the acceptance rule as a test on the *limited* factor, not on the current
  estimate alone, which Söderlind argues avoids unnecessary rejections; they start the
  recursion with unit past estimates and clip the last step to the final time, snapping a time
  within 100 units in the last place onto it in OrdinaryDiffEq.jl (§2.3, Eqs. (2.6)–(2.7),
  Algorithm 2).
- Vermeire (2023) bounds the step ratio to $[0.1,1.2]$ with safety factor 0.9 (Eq. (32)); the
  small growth bound serves the stability-limit tracking described below.
- ARKODE inherits the CVODE heuristics: growth and decay bounds, a reduction after repeated
  error failures or after a failed implicit solve, and $h_{\min}\le h\le h_{\max}$ (Reynolds et
  al. §3.2).

**Initial step.** Fekete et al. and Ranocha et al. both use the Hairer–Nørsett–Wanner starting
procedure; for PDEs Fekete et al. take the minimum of that step and the CFL step (§3.1; §2).
Ranocha et al. (2025) keep it, but for a Mach 2000 astrophysical jet the automatic guess was
insufficient and they set $h_0\approx10^{-12}$ by hand (§2.3, §5.2).

## Step-size-control stability

When the step is limited by stability rather than accuracy, $z=h\lambda$ sits on the boundary of
the main method's stability region and the asymptotic theory of controllers no longer applies.
Ranocha et al. (2022, §4), following Hall, Higham and Hairer–Wanner, apply the pair and
controller to $y'=\lambda y$: $y_{n+1}=R(h_n\lambda)y_n$, the estimate is
$E(h_n\lambda)y_n$ with $E$ the difference of the embedded and main stability polynomials
(page-local), and the PID recursion in logarithmic variables has fixed points on the stability
boundary. The fixed point is stable iff the spectral radius of

$$\mathcal J(z)=\begin{pmatrix}
1&\frac{zR'(z)}{R(z)}&0&0&0&0\\
-\frac{\beta_1}{k}&1-\frac{\beta_1}{k}\frac{zE'(z)}{E(z)}&-\frac{\beta_2}{k}&-\frac{\beta_2}{k}\frac{zE'(z)}{E(z)}&-\frac{\beta_3}{k}&-\frac{\beta_3}{k}\frac{zE'(z)}{E(z)}\\
1&0&0&0&0&0\\
0&1&0&0&0&0\\
0&0&1&0&0&0\\
0&0&0&1&0&0
\end{pmatrix}$$

is below one ($\mathcal J$ page-local; Eq. (4.2)). A controller designed for one pair can fail
for another: PI34, designed by Gustafsson for DP5(4)6F, is step-size-control unstable for
BS5(4)7F near the negative real axis (spectral radius up to about 2.2). On linear advection at
tolerance $10^{-5}$ it costs 5015 right-hand-side evaluations with 132 rejections, against 4119
with none for the optimized $(0.28,-0.23,0)$ (§4, Table 2, Fig. 4). For some pairs no PID controller they tested was stable, e.g. SSPRK(10,4) with an embedded method
of Conde, Fekete and Shadid (§5; see the qualification on the
[embedded-pair page](/methods/embedded-runge-kutta-pair.md)).

Ranocha et al. contest the earlier Kennedy–Carpenter–Lewis advice that controller instability
"is probably best accomplished by reducing step sizes": optimizing the controller is more
robust and efficient (§8).

## Tuning controllers per pair

Ranocha et al. search $\beta_1\in[0.1,1]$, $\beta_2\in[-0.4,-0.05]$, $\beta_3\in[0,0.1]$ in
steps of 0.01, restricted a priori to step-size-control-stable parameters (computed with
NodePy). The objective is the number of right-hand-side evaluations on three Euler problems
(Taylor–Green vortex, isentropic vortex, a source-term problem) for tolerances
$10^{-8}$–$10^{-1}$, and the final choice is made by judgement (§5.4, §6.1). Findings:

- good controllers are within about 5% of the best, and no controller is optimal everywhere
  (§5.4);
- in the accuracy-limited regime (isentropic vortex) larger $\beta_1$ and $\beta_2$ near zero,
  i.e. close to the I controller, perform best; near the stability boundary more damping and a
  smaller $\beta_1$ do (Fig. 6).

Recommended controllers (Table 11, excerpt):

| Pair | $(\beta_1,\beta_2,\beta_3)$ |
|---|---|
| BS3(2)3F | $(0.60,-0.20,0.00)$ |
| BS5(4)7F | $(0.28,-0.23,0.00)$ |
| DP5(4)6F | $(0.70,-0.40,0.00)$ |
| T5(4)6F | $(0.57,-0.24,0.04)$ |
| SSP3(2)4[3S\*$_+$] | $(0.55,-0.27,0.05)$ |
| RK3(2)5F[3S\*$_+$] | $(0.70,-0.23,0.00)$ |
| RK4(3)9F[3S\*$_+$] | $(0.38,-0.18,0.01)$ |
| RK5(4)10F[3S\*$_+$] | $(0.45,-0.13,0.00)$ |

## Empirical comparisons of controllers

- Fekete et al. (2022), Van der Pol with $\varepsilon=0.1$, tolerance $10^{-4}$, SSPRK(2,2) pair
  (§3.1.1, Fig. 9):

  | Controller | steps | rejected | mean accepted step |
  |---|---|---|---|
  | I | 1982 | 495 | $1.91\times10^{-3}$ |
  | PI | 1270 | 210 | $2.71\times10^{-3}$ |
  | PID | 753 | 17 | $3.94\times10^{-3}$ |
  | Gustafsson | 795 | 38 | $3.84\times10^{-3}$ |

  PID "performed significantly better" in the vast majority of their tests, and they use it
  afterwards.
- Reynolds et al. (2023), advection–reaction [Brusselator](/benchmarks/brusselator.md) with
  explicit pairs of orders 2–5 (§5.1.1, Fig. 2): the I controller is often least efficient
  (13–50% rejected steps), PI and Gustafsson are often most efficient (under 7% rejected), and
  PID falls between PI and I.
- Ranocha et al. (2022): for BS3(2)3F all classical controllers of their Table 1 perform
  reasonably, PI42 slightly best; for DP5(4)6F an optimized controller is not significantly
  better than PI34 (§5.5.1).

## Error-based versus CFL-based control

CFL control sets $h_n=\nu\min_i\Delta x_i/v_{\max,i}$, with $v_{\max,i}$ the local maximal wave
speed (page-local), normalized so that a real stability interval of length 2 corresponds to
$\nu=1$ (Ranocha et al. 2022, §3, Eqs. (3.1)–(3.2)). Its cost is linearly sensitive to $\nu$
and to the mesh, and $\nu$ must be tuned per method and grid. Ranocha et al. (2022) compare
the two:

- **Linear advection** (§3, Figs. 2–3). A PI controller automatically settles at the maximal
  stable step, $\nu=2.1$, for tolerances $10^{-5}$–$10^{-3}$, matching the best hand-tuned
  CFL run. On a curvilinear grid the stable CFL number could be doubled, which error control
  finds without tuning.
- **Industrial flows** (§7, Tables 8–10). Error control at tolerance $10^{-8}$ costs about half
  of CFL control with $\nu=1$: on the NASA juncture flow ($4.09\times10^7$ degrees of freedom),
  BS3(2)3F needs 1786 against 3598 evaluations and 586 s against 1172 s. On the Imperial Front
  Wing at $p=1$, CFL control with $\nu=1$ crashed for SSP3(2)4[3S\*$_+$]; $\nu=0.85$ ran a few
  percent cheaper than error control, which needed no tuning.
- **Recommendation** (§8). Tolerance $\approx10^{-8}$ for applied CFD, where the step is almost
  always stability-limited. Error-based control moves the choice of critical parameters from
  the spatial-discretization developer to the time-integrator developer.

[Al Jahdali et al. (2022)](/sources/aljahdali-2022.md), from the same group, set the CFL step
as $h_{n+1}=0.95\,\nu_{\max}\min_i\Delta x_i/v_{\max,i}$ with $\nu_{\max}$ the largest stable
Courant number of each method (4.1471, 8.3132, 4.8111 and 2.7852 for their ERK(4,2), ERK(8,2),
ERK(5,3) and the classical RK4) and compare it with PID control at
$\mathrm{rtol}=\mathrm{atol}=10^{-6}$ over 600 steps of two industrial flows (§2.1, Eqs. (2)–(3),
Tables 1, 4). At third order, error control costs 4250 right-hand-side evaluations on the
Imperial Front Wing against 7135 for CFL-controlled ERK(5,3) (1.41e3 s against 2.30e3 s), and
the fifth- and sixth-order error-controlled pairs BSRK(8,5) and VRK(9,6) run faster than the
second-order CFL-controlled schemes (1.41e3 s against 2.13e3 s) (§3, Table 4).

[Ranocha et al. (2025)](/sources/ranocha-2025.md) extend the comparison to six situations
in which CFL control needs hand tuning, with the pairs and controllers of Ranocha et al. (2022)
in two code bases (Trixi.jl with OrdinaryDiffEq.jl, and SSDC on PETSc TS):

- **Mesh change** (§3, Fig. 2; [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)). The
  CFL factor affects cost linearly, the tolerance only roughly logarithmically; a range of
  tolerances spanning up to five orders of magnitude reaches the cost of the best hand-tuned
  CFL factor. The optimal factor grows by 55% (BS3(2)3F) to 74% (SSP3(2)4[3S\*$_+$]) from a
  Cartesian to a curved mesh, while the good tolerance range is unchanged.
- **Shock capturing** (§4, Table 1). DG/finite-volume subcell blending moves eigenvalues near
  the negative real axis outside the stability region, which lowers the linearly stable CFL
  number by more than 20% for BS3(2)3F and RDPK3(2)5F but by about 5% for SSP3(2)4[3S\*$_+$].
  On the Orszag–Tang vortex error control saves 13%, 11% and 6% of the evaluations of tuned
  CFL control for these three pairs.
- **Cold starts** (§5, Tables 2–3). Error control produces an initial transient of about 100
  small steps automatically. CFL control crashes in the first steps of a double Mach reflection
  even at $\nu=0.01$, would need $\nu\approx10^{-9}$ at the start of a Mach 2000 jet, and needs
  initial factors 9–32% below the asymptotic ones on a delta wing and on the NASA Common Research
  Model. On a second Common Research Model mesh, the CFL target of the first mesh fails for all
  three pairs, because the asymptotic CFL number of the new mesh is about three times smaller;
  error control runs all three to the end.
- **Change of variables** (§6, Tables 4–5). For entropy-projected Gauss DG on a
  Kelvin–Helmholtz instability, error control is "usually around 5%" cheaper than tuned CFL
  control at Atwood number 3/7. At 0.7 the evolved variables lose positivity around $t\approx3$
  even with $\nu=0.05$ for SSP3(2)4[3S\*$_+$], so CFL control is not possible, while error
  control works directly.
- **New equations** (§7). For shallow water–Exner sediment transport, whose wave speeds are
  roots of a cubic, error control needs no eigenvalue estimate; a loose bound would add
  excessive diffusion.

Their pair recommendation: SSP3(2)4[3S\*$_+$] for lower-Mach flows and for problems with
positivity issues or strong shock capturing, otherwise RDPK3(2)5F (more robust) or RDPK4(3)9F
(more efficient at strict tolerances), with BS3(2)3F a good general-purpose choice (§8).

**A single-stage method.** [Babbar & Chandrashekar (2025)](/sources/babbar-2025.md) bring the
same controller to Lax–Wendroff flux reconstruction, a one-step Taylor-type scheme with no
Runge–Kutta stages (see [Lax–Wendroff flux reconstruction](/methods/lax-wendroff-flux-reconstruction.md)).
The embedded solution drops the highest Taylor term of the time-averaged flux, "one order of
accuracy lower", and both solutions are element-local updates without the interface terms, so
the estimate needs no extra communication and adds about 4 % to the cost (§5.2, Eqs. (63)–(65),
Algorithm 1; §6.3). They use the WRMS norm with the PETSc scale, the PI42 parameters, the arctan
limiter and the $0.81$ acceptance rule, and redo a step when the solution leaves the admissible
set (§5.1–5.2, Algorithm 3); they claim the first error-based stepping for a single-stage
evolution method (§7). Against the best constant CFL factor that ran without admissibility
failure, at $\mathrm{atol}=\mathrm{rtol}=10^{-6}$ or $5\times10^{-6}$ (Table 1):

| problem | CFL steps | error-controlled steps |
|---|---|---|
| forward-facing step | 5,679,021 | 7,633,954 ($10^{-6}$); 5,598,338 ($5\times10^{-6}$) |
| Mach 3 flow past a cylinder | 1,601,725 | 1,057,844; 768,835 |
| NACA0012 | 7,530,003 | 4,842,326 ($10^{-6}$) |
| blunt body | no constant CFL ran to $t=10$ | 30,527 (761 rejected) |

On a cold-started Mach 2000 jet the controller used an effective Courant number of about
$10^{-3}$ at start-up that rose to about $10^{-1}$, a ramp that CFL control would have to be
programmed by hand (§6.1.1, Fig. 5b).

## Balancing the temporal against the spatial error

[Pan et al. (2022)](/sources/pan-2022.md) drop the user's temporal tolerance altogether. For
an implicit ESDIRK step of a high-order DG discretization of compressible Navier–Stokes they
write the one-step error, to leading order, as three terms (§2.1.5, Eqs. (24)–(28)):

$$\text{local error}\approx E_t+h\,\bar E_s+h\,\bar E_{\mathrm{it}},$$

the local temporal error $E_t$, $h$ times the $b$-weighted stage average $\bar E_s$ of the
spatial truncation error, and $h$ times the $b$-weighted average $\bar E_{\mathrm{it}}$ of the
Newton iteration error (page-local symbols). Since the largest term dominates, shrinking
another far below it buys nothing. The step is the largest one with

$$\lVert E_t\rVert=\beta_{\mathrm s}\,h\,\lVert\bar E_s\rVert,\qquad \beta_{\mathrm s}<1$$

(Eq. (29); page-local $\beta_{\mathrm s}$, the source's $\beta$, distinct from the PID
exponents), so the total error stays dominated by the spatial one. The three ingredients:

- **Temporal estimate**: an embedded ESDIRK solution one order *higher* than the advanced
  one, from Kværnø's stiffly accurate pairs 2(3), 3(4), 4(5), with no local extrapolation
  (Eq. (15)); the authors claim it is more accurate than the usual lower-order estimate and
  needs no problem-dependent calibration (§2.4). See
  [embedded pairs](/methods/embedded-runge-kutta-pair.md).
- **Spatial estimate**: the DG operator at polynomial degree $P+1$ minus that at degree $P$,
  applied to the end-of-step solution (Eq. (30); page-local $P$), about 1.5 operator
  evaluations, against more than 10 for one implicit stage (§2.4).
- **Iteration error**: the Newton tolerance is $0.1$ times the temporal estimate (Eq. (37));
  see [implicit stage solvers](/methods/implicit-stage-solvers.md).

Because the target itself scales with $h$, the elementary controller has exponent $1/p$, not
$1/(p+1)$, for main order $p$: $h_{n+1}=h_n\bigl(\beta_{\mathrm s}h_n\lVert\bar E_s\rVert/\lVert E_t\rVert\bigr)^{1/p}$
(Eqs. (31)–(32)). It is applied per element and per conserved variable, with a floor
$10^{-12}$ times the root-mean-square of each variable added to numerator and denominator
(the numerator carries an extra factor $1.5^p$ so that quiescent elements let the step
grow), aggregated over elements by a temporal-error-weighted mean and over variables by
the minimum (Eqs. (33)–(36)). A global $L^2$ norm, they argue, can be dominated by one
variable or by large structures and give a step too large for the small ones (§2.2). No
accept/reject test is described.

Results (§3; Nektar++):

- **Isentropic vortex**, degree 6, ESDIRK3: the adaptive step keeps the temporal error below
  the spatial one on every mesh, so the total error converges at the spatial rate, whereas
  Courant number 10 is temporal-error dominated, 0.2 wastes work and 1.0 switches from
  spatial to temporal dominance under refinement (Figs. 3–4); the adaptive run is near the
  most efficient fixed-Courant run at every error level and up to ten times cheaper than a
  naive choice (Fig. 5); ESDIRK2, 3 and 4 give almost the same total error (Fig. 6). With a
  tolerance-based controller the temporal error would be independent of the mesh, the
  authors note (§3.1.2).
- **Steady flat-plate boundary layer**: unchanged parameters converge almost as fast as a
  Courant ramp growing by 2 per step and faster than one growing by 1.5 (§3.2, Figs. 9–10);
  dedicated steady-state accelerators remain faster.
- **Taylor–Green vortex** at $\mathrm{Re}=1600$: $\beta_{\mathrm s}=0.01$ matches $h=0.1$ for
  1.27 times its CPU time; they use $0.01$ for implicit LES, where the spatial truncation error
  acts as the subgrid model, and $0.1$ otherwise (§3.3, Table 3).
- **Cylinder at $\mathrm{Re}=3900$**: averaged adaptive steps 0.027, 0.043, 0.127 for ESDIRK2,
  3, 4 against a fixed DIRK2 step 0.010 (Courant about 40), with CPU-time ratios 1.09, 1.36,
  1.53: higher order takes larger steps but costs more (§3.4, Table 2).
- Across all tests the CPU time is 0.96–1.27 times that of hand-tuned fixed or ramped Courant
  settings, with no per-case tuning (Table 4).

The authors concede that per-step balancing does not guarantee a spatially dominated global
error and that the accuracy-based step does not guarantee stability (§4). Compared with the
tolerance-based controllers on this page, the free parameter moves from $\mathrm{tol}$ to
$\beta_{\mathrm s}$, which they still set per regime (0.1 or 0.01) *(compiler remark, not in the
source)*. Vermeire
(2023) rests stability-limited stepping on the related claim that the maximal stable step
"often introduces little temporal error relative to the error introduced by the spatial
discretization" (next section).

## Error control as a stability-limit detector

Vermeire (2023) uses an embedded pair not to estimate accuracy but to find the stability limit
of [paired explicit Runge–Kutta](/methods/paired-explicit-runge-kutta.md) methods. The embedded
first-order method has a region of absolute stability slightly smaller than the second-order
main method, so its solution diverges from the main one just before the main method becomes
unstable (§3–4; see [embedded pairs](/methods/embedded-runge-kutta-pair.md)). With the PID
gains of Fekete et al., tolerances $10^{-4}$, step ratio bounds $[0.1,1.2]$ and safety 0.9, the
controller drives the step towards, without exceeding, the stability limit; P, PI and explicit
Gustafsson controllers were also tried and gave more rejected steps (no counts printed). The
Bogacki–Shampine pair with Fekete et al.'s coefficients and tolerances $10^{-3}$ also ran
close to its stability limit (§5). The justification is that, for high-order spatial
discretizations of advection–diffusion, the maximal stable step "often introduces little
temporal error relative to the error introduced by the spatial discretization" (§2.2, cited,
not shown). Against the Bogacki–Shampine pair the adaptive paired methods are 4.95–7.11 times
cheaper on compressible Navier–Stokes flows (§6, Tables 2–4).

## Choice of the error estimator

Belardo et al. (2026, §4) fix the third-order Bogacki–Shampine method and vary only its
second-order estimator within the two-parameter family of embeddings that share its stages
(see [embedded pairs](/methods/embedded-runge-kutta-pair.md)), keeping the distance of
$\hat b$ from $b$ equal to that of the standard embedding. On the stiff scalar problem
$y'=-a(y-\cos t)$, $y(0)=a^2/(a^2+1)$, $t\in[0,10]$, a
[Prothero–Robinson-type](/benchmarks/prothero-robinson-problem.md) test, with
$\mathrm{rtol}=10^{-6}$, $\mathrm{atol}=10^{-9}$ (Tables 2–3):

| Estimator | accepted steps, $a=50$ | final error, $a=50$ | accepted steps, $a=200$ | final error, $a=200$ |
|---|---|---|---|---|
| standard | 906 | $3.31\times10^{-6}$ | 1874 | $1.30\times10^{-6}$ |
| best tested | 804 | $3.21\times10^{-6}$ | 1709 | $1.29\times10^{-6}$ |
| other directions | 977–1488 | $5.5\times10^{-7}$–$2.3\times10^{-6}$ | 1302–2492 | $4.6\times10^{-7}$–$3.1\times10^{-6}$ |

The best estimator cuts accepted steps by 11% and 9% at no loss of final accuracy, but it is a
different member of the family at each stiffness, and it was selected on the same problem on
which it is evaluated. The estimator with the largest real stability interval does not minimize
the step count. Rejected steps and function evaluations are not reported.

## Step-size control with relaxation

[Relaxation Runge–Kutta methods](/methods/relaxation-runge-kutta.md) replace $y_{n+1}$ by
$y^{\gamma}_{n+1}=y_n+\gamma_n(y_{n+1}-y_n)$ at time $t_n+\gamma_nh$, which interacts with the
controller in two ways.

- **Cost.** With error control, relaxation raised the number of evaluations on the Imperial
  Front Wing from 4250 to 5648 (global) or 5652 (local relaxation), about 33%; with CFL control
  it was almost unchanged (e.g. 6624, 6636, 6628 for ERK(4,2)). Al Jahdali et al. (2022, §3,
  Table 4) read this as a sign that the CFL step is already close to the entropy-stable step
  ($\gamma_n\approx1$), without reporting $\gamma_n$.
- **FSAL pairs.** Relaxing after acceptance, as OrdinaryDiffEq.jl and SUNDIALS do, makes the
  first stage of the next step $f(y^{\gamma}_{n+1})$ instead of the FSAL value, one extra
  evaluation per step. [Bleecke & Ranocha (2026)](/sources/bleecke-2026.md) remove it in two
  ways (§2): **FSAL-R** keeps error control on the unrelaxed pair and relaxes accepted steps
  only, approximating the next first stage by linear interpolation along the relaxation
  secant; **R-FSAL** relaxes *before* the error estimate and compares the relaxed main solution
  with a relaxed embedded solution, both read at $t_n+\gamma_nh$. Both keep the local orders of
  main and embedded method (Theorems 1–2) and, on the
  [BBM equation](/benchmarks/benjamin-bona-mahony-equation.md), reach the accuracy of the naive
  combination at the cost of the unrelaxed method (§3, Fig. 1). FSAL-R preserves the structure
  of existing libraries; R-FSAL is preferred for dissipative problems (§4). Step-size-control
  stability with relaxation is deferred to a companion report (§3). Details are on the
  [embedded-pair page](/methods/embedded-runge-kutta-pair.md).

## Stabilized methods

For Runge–Kutta–Chebyshev-type [stabilized methods](/methods/stabilized-explicit-runge-kutta.md)
the controller also chooses the stage count. [Faleichik & Moisa (2026)](/sources/faleichik-2026.md)
take the step-size selection of the RKC code of Sommeijer, Shampine and Verwer and pick the
number of stages $s$ from an estimate of the spectral radius by a fitted formula,
$s\approx-0.831+1.855\,\rho^{0.534}$ with $\rho$ the spectral-radius estimate (page-local; the
source does not say whether it includes the factor $h$;
§4, Eq. (21)). The stage $Y_{s-1}$ of their method is a first-order solution at $t_n+h$, but its
error constant depends on $s$ and would need normalization to avoid rejections when $s$
changes; they use instead the Taylor-type estimate
$\mathrm{err}=\tfrac1{10}\bigl(y_n-y_{n+1}+hf(t_{n+1},y_{n+1})\bigr)$ for a leading local error
$\tfrac1{10}h^2y''$ (§4, Eqs. (22)–(23); see Qualifications).

## Multistep methods

For [linear multistep methods](/methods/linear-multistep-method.md) the controller also chooses
the order. Every change of step changes the coefficients, and stability constrains the sequence
of step ratios $r_n=h_n/h_{n-1}$, not only each step.

**Error estimate from divided differences.** Here $p$ is the current order; for BDF and for the
methods of Glandon et al. it equals the step number $k$ of the
[registry](/notation.md). Both multistep sources estimate the local error of
the order-$p$ method from the divided difference of order $p+1$ through the new and $p+1$ past
values, scaled by an error constant.

- [Glandon et al. (2022)](/sources/glandon-2022.md) (Def. 7.1) multiply that divided difference by
  $(p+1)!\,C\,h_n^{p+1}$, with $C$ (page-local) the method's error constant on the current grid.
  The estimate may slightly overestimate the local error.
- [García-Archilla & Novo (2023)](/sources/garciaarchilla-2023.md) (§4) take the BDF estimate of
  Hairer–Wanner §III.5, the divided difference scaled by the products of the step lengths.

**Controller and order.**

- García-Archilla & Novo use a mixed tolerance $\mathrm{TOL}_n=\mathrm{TOL}_r\big(\max\{\lVert y_{n+1}\rVert,\lVert y_n\rVert\}+0.001\big)$,
  reject when the estimate exceeds it, and set $h_{\mathrm{new}}=0.9\,h_n(\mathrm{TOL}_n/\mathrm{EST}_n)^{1/(p+1)}$,
  with $\mathrm{EST}_n$ the estimate and $p$ the current BDF order (Eq. (110); $\mathrm{TOL}_r$,
  $\mathrm{EST}_n$ page-local). This is the I controller above with a safety factor and no printed
  ratio limiter. They start with BDF1 at $h_0=h_1=\sqrt{\mathrm{TOL}_r}/100$ and switch to BDF2
  once its estimates are smaller than BDF1's; in practice at most eight to ten BDF1 steps were
  taken.
- Glandon et al. compute $h_{\mathrm{opt}}=h_n\lVert e\rVert^{-1/(p+1)}$ for orders $p-1$, $p$
  and $p+1$ and select among them, after Hairer–Nørsett–Wanner (Eq. (7.1); $e$ page-local). They
  let the step grow only after $p$ successful steps at the current size, because explicit
  step-ratio bounds are not available for general multistep methods (Remark 7.3).

**Restarts.** A multistep integrator restarts at first order and loses its error history after
every reset. Inside a multirate method this forced Reynolds et al. to cap CVODE's step growth
after the first internal step at 10 instead of $10^4$ (Reynolds et al. 2023, §5.1.3; see
[CVODE](/software/cvode.md)).

**Step-ratio constraints from stability theory.** For variable-step BDF2 the parabolic energy
estimate of [Akrivis et al. (2024)](/sources/akrivis-2024.md) is proved for every ratio at most
$r^\star\approx1.9398$, and its constant grows with the accumulated decreases of the ratio
sequence (Thm. 1.1, §1.1). A controller that caps growth at about 1.94 and avoids oscillating
ratios therefore stays within the theorem; the bound is sufficient, not shown necessary
*(compiler inference; the source gives no controller advice)*.
Graded meshes $t_i=(i/N)^a$ with $a>1$ (page-local) satisfy the cap except at finitely many
steps. Zero-stability alone allows ratios up to $1+\sqrt2$. García-Archilla & Novo's
Navier–Stokes theory needs a ratio cap and bounded total variation of the ratios (Thms. 3–4).
Their own controller enforces neither, and no check is reported, so the theory does not formally
cover their runs (§4, Fig. 8). See
[variable-step BDF2 stability](/results/variable-step-bdf2-stability.md) and
[zero-stability](/definitions/zero-stability.md).

**Estimator reuse and stability limits.** García-Archilla & Novo use the estimator of the fully
implicit BDF also for BDF2 with explicit or linearized convection. They state this without
justification ("nevertheless, it was used"; §4). On the
[flow past a cylinder](/benchmarks/flow-past-cylinder.md), the IMEX steps at two tolerances
coincide on $t\in[1.7,3.7]$: the CFL-type condition of explicit convection, not accuracy, limits
them (Fig. 8). This is the multistep counterpart of the stability-limited regime discussed
above; see [IMEX linear multistep methods](/methods/imex-linear-multistep-methods.md).

**Linear solves.** Each BDF step of García-Archilla & Novo solves one linear system by iterative
refinement with a factorization from an earlier step, refactorizing after five iterations without
convergence. Factorizations numbered at most about 5% of the steps on the manufactured test, and 53–92
for 4,384–93,671 steps on the cylinder (§4.1–§4.2; see
[implicit stage solvers](/methods/implicit-stage-solvers.md)).

## Multirate step-size control

A [multirate infinitesimal](/methods/multirate-infinitesimal-methods.md) method has two step
parameters, the macro step $H_n$ and the integer multirate ratio $m_n$ (micro step
$H_n/m_n$). [Fish & Reynolds (2023)](/sources/fish-2023.md) control both at once ("H-M
controllers"), arguing that adapting only $H$ at fixed $m$, or only the micro step at fixed $H$,
wastes work or loses accuracy (§1). They bound the total error by a slow error (method error with
exactly solved stages) plus a fast error (inner-solver error),
$e_n\le e^{\{\mathrm s\}}_n+e^{\{\mathrm f\}}_n$ (page-local unscaled error norms), and model

$$e^{\{\mathrm s\}}_{n+1}=\varphi^{\{\mathrm s\}}_nH_n^{p^{\{\mathrm s\}}},\qquad e^{\{\mathrm f\}}_{n+1}=\varphi^{\{\mathrm f\}}_n\Big(\frac{H_n}{m_n}\Big)^{p^{\{\mathrm f\}}}H_n$$

(§2, eq. 2.1), with $p^{\{\mathrm s\}}$, $p^{\{\mathrm f\}}$ the global orders of the slow and fast
**embeddings** and $\varphi^{\{\cdot\}}_n$ unknown principal error functions (page-local symbols,
not the exponential $\phi_k$). The tolerance is split, $\mathrm{tol}=\mathrm{tol}^{\{\mathrm s\}}+\mathrm{tol}^{\{\mathrm f\}}$
(equal halves in all their runs). Approximating $\log\varphi$ by a piecewise-constant or
piecewise-linear model with an observer, after Gustafsson, gives two derived controllers; with
$q^{\{\cdot\}}_n=\mathrm{tol}^{\{\cdot\}}/e^{\{\cdot\}}_n$ the "oversolve" factors and observer gains
$\kappa_1,\kappa_2$ (page-local), the **Constant-Constant** controller is

$$H_{n+1}=H_n\big(q^{\{\mathrm s\}}_{n+1}\big)^{\kappa_1/p^{\{\mathrm s\}}},\qquad m_{n+1}=m_n\big(q^{\{\mathrm s\}}_{n+1}\big)^{\frac{(p^{\{\mathrm f\}}+1)\kappa_1}{p^{\{\mathrm s\}}p^{\{\mathrm f\}}}}\big(q^{\{\mathrm f\}}_{n+1}\big)^{-\kappa_2/p^{\{\mathrm f\}}}$$

(§2.2.1, eq. 2.9), whose $H$ part is an I controller with gain $\kappa_1/p^{\{\mathrm s\}}$; $m$ is
treated as real in the derivation and rounded up. The **Linear-Linear** controller uses two past
steps and errors (eqs. 2.10–2.11); **PIMR** and **PIDMR** are heuristic multirate analogues of
the PI and PID controllers (eqs. 2.13, 2.15). Quadratic and higher models were "bimodal" and
omitted (§2.3).

**Fast-error estimates** (§3), all with an embedded inner pair: Full-Step runs the whole step a
second time with the embedded inner method (doubling slow evaluations); Stage-Aggregate solves
each stage with both inner methods; Local-Accumulation-Stage-Aggregate (LASA) sums the inner
embedded local-error estimates along each stage and aggregates over stages by mean or max, with no
extra evaluations. The slow error comes from the standard MRI-GARK embedding.

**Results** (seven ODE problems, four MRI-GARK methods, three tolerances; costs relative to a
brute-force step-local optimum, §4): LASA-mean is the cheapest strategy with mean error deviation
$\log_{10}(e/\mathrm{tol})=-0.08$ and is recommended; tuned gains for Constant-Constant are
$\kappa_1=0.42$, $\kappa_2=0.44$ (eq. 4.5). The four multirate controllers differ by at most 20 %
(slow) and 16 % (fast) in cost, and all beat single-rate I, PI, PID and Gustafsson controllers run
at fixed $m=10$: mean fast cost deviation 5.7–6.6 against 10.4 for PID and 123.9 for I (Fig. 7).
Constant-Constant is recommended for simple problems. On a 1D stiff reaction–diffusion
[Brusselator](/benchmarks/brusselator.md) not used in tuning, the controllers keep $m=1$ until
reaction stiffness appears at $t\approx0.9$ and then raise it (Fig. 8). [Fish et al.
(2024)](/sources/fish-2024.md) (§6.2.2) use Constant-Constant with LASA-mean to run their
[IMEX-MRI-SR](/methods/imex-mri-sr.md) methods adaptively; some runs fail by oscillating between
accepted and rejected steps.

## Cost-based control for iterative integrators

Error-based controllers pick the largest step meeting the tolerance, assuming the cost of a step
does not depend on its size. [Deka & Einkemmer (2022)](/sources/deka-2022.md) (§1, §2.4) point out
that this fails for implicit and exponential integrators with iterative inner solvers, whose cost
per step grows nonlinearly with $h$ (Krylov bases, Leja interpolation degree). The controller of
Einkemmer (2018), as recalled there, minimizes the cost per unit time $c_n=\tau_n/h_n$ ($\tau_n$
the runtime of step $n$; page-local) by gradient descent in logarithmic variables:

$$\Delta_n=\frac{\ln c_n-\ln c_{n-1}}{\ln h_n-\ln h_{n-1}},\qquad \sigma_n=\exp\big(-\alpha_{\mathrm c}\tanh(\beta_{\mathrm c}\Delta_n)\big),\qquad h_{n+1}=h_n\times\begin{cases}\lambda_{\mathrm c},&1\le\sigma_n<\lambda_{\mathrm c},\\ \delta_{\mathrm c},&\delta_{\mathrm c}\le\sigma_n<1,\\ \sigma_n,&\text{otherwise,}\end{cases}$$

with $\alpha_{\mathrm c}=0.65241444$, $\beta_{\mathrm c}=0.26862269$, $\lambda_{\mathrm c}=1.37412002$,
$\delta_{\mathrm c}=0.64446017$ (page-local names), and the step taken is the minimum of this proposal
and the traditional I-controller step $h_n(\mathrm{tol}/e_n)^{1/(p+1)}$. With Leja-based
[exponential Rosenbrock](/methods/exponential-integrators.md) EXPRB43 on resistive MHD it is cheaper
than the traditional controller in most configurations, gives a roughly linear relation between
cost and tolerance, and rescues Krylov runs that fail to finish at lenient tolerances with the
traditional controller (§4.2, §5.2; [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)).
It is not designed for explicit methods, whose cost per step is independent of $h$ (§4.3).

## Adaptive spectral deferred correction

[Saupe et al. (2025)](/sources/saupe-2025.md) transfer embedded-pair control to spectral deferred
correction (SDC), whose sweeps raise the order by one each up to the collocation order (see
[deferred correction](/methods/deferred-correction.md)). Earlier adaptive SDC either doubled and
halved the step (Dutt, Greengard and Rokhlin) or used problem-specific quantities (§1). Both new
estimates feed the elementary controller $h_{n+1}=0.9\,h_n\,\mathrm{err}_n^{-1/k}$, with
$\mathrm{err}_n$ the estimate divided by the tolerance, local extrapolation and
reject-and-recompute when $\mathrm{err}_n>1$ (§2.2, Eqs. (14)–(15)):

- **$\Delta t$-adaptivity** (Algorithm 1). A fixed number $K$ of sweeps; the increment between
  sweeps $K$ and $K-1$ estimates the local error of the order-$(K-1)$ iterate, so $k=K$. It needs a
  sweep that gains exactly one order (implicit Euler) and exact inner solves.
- **$\Delta t$-$k$-adaptivity** (Algorithm 2). Sweep until the collocation residual falls below a
  tolerance set a few orders below the error tolerance; then compare the value at node
  $\mathsf M-1$ with the degree-$(\mathsf M-1)$ interpolant through the other nodes and $t_n$, an order
  $\mathsf M-1$ approximation built from the collocation polynomial (see
  [dense output](/methods/dense-output.md)), so $k=\mathsf M$ (Eqs. (16)–(18)). The step may grow by
  at most a factor 4; divergence (residual above $10^9$, growing, or 16 sweeps) divides the step
  by 4. This chooses both the step and the number of sweeps, and allows inexact inner solves.
- **Restarts** reuse the rejected step's collocation polynomial, evaluated at the new nodes, as
  initial guess; it cut iterations but changed total cost little, because restarts were rare
  (§2.2, §4.1).
- **$k$-adaptivity**, fixed step and sweeping to a residual tolerance, is inferior: the
  iteration count is a coarse integer control, and the residual measures the distance to the
  collocation solution, not the truncation error (§2.2).

On the stiff [van der Pol oscillator](/benchmarks/van-der-pol-oscillator.md) ($\mu=1000$) fixed
steps need about 70 times the Newton iterations of the adaptive strategies (§4.1, Fig. 6), and
adaptivity helps on all four problems tested. The global error follows tolerance
proportionality $e\propto\mathrm{tol}^{\,q/(p+1)}$, with $q$ the order advanced and $p$ the
order estimated: $\mathrm{tol}^1$ for $\Delta t$-adaptivity and $\mathrm{tol}^{5/4}$ for
$\Delta t$-$k$-adaptivity, except for $\Delta t$-adaptivity on the quench problem, whose error
depends on how the runaway transition is resolved (§4.1, Fig. 8).

**Parallel-in-time variants.** In pipelined block Gauss–Seidel SDC one step size serves a whole
block; the increment then estimates the error accumulated in the block, which the controller
treats as a local error, and a rejected block restarts from its first failing step, a heuristic
that "performed consistently better" than restarting the block (§2.3). Christlieb et al. found
the increment a poor estimate for RIDC because local errors of different steps accumulate;
Saupe et al. argue that fixed-size blocks with one step size avoid this (§5). Diagonal SDC is
run with $\Delta t$-$k$-adaptivity; see [diagonal SDC](/methods/parallel-sdc.md) and
[parallel-in-time integration](/methods/parallel-in-time-integration.md). At least one parallel
adaptive SDC variant beat the embedded order-5 pairs ESDIRK5(3) and ARK5(4) in wall time on every
problem (§4.2, Fig. 10). [Čaklović et al. (2025)](/sources/caklovic-2025.md) (§4) compare their
diagonal SDC variants at fixed steps only.

## Positivity and the error estimate

When a step is modified after the fact to restore positivity, the error estimate must account
for the modification:

- **Adapted weights.** [Nüßlein et al. (2021)](/sources/nusslein-2021.md) replace the weights $b$
  of a step whose solution has negative entries by the nearest $\tilde b$, in the $\ell^1$ sense,
  that gives a nonnegative solution and satisfies the order conditions to a reduced order, found
  by a linear program (§3; see [positivity preservation](/properties/positivity-preservation.md)).
  The error estimate becomes $\mathrm{err}\approx\mathrm{err}_T+\delta$, with $\mathrm{err}_T$ the
  standard embedded estimate and $\delta=\lVert hF(\tilde b-b)\rVert$ the change caused by the
  adaptation ($F$ the matrix of stage derivatives, page-local); a step is rejected when $\delta$
  exceeds its own tolerance or the linear program is infeasible down to the lowest allowed order
  (§4.2, Eqs. (4.1)–(4.2), Algorithm 1). With a PI controller at tolerance $0.01$ on an
  advection–diffusion–production–destruction problem, 72 of 264 steps were adapted, $\delta$ was
  of the size of $\mathrm{err}_T$, and mass was conserved to round-off; on the
  [stratospheric reaction problem](/benchmarks/stratospheric-reaction-problem.md), 249 steps with 2
  rejections (§5.3–5.4).
- **Post-processing correctors.** [Nurkhametova et al. (2026)](/sources/nurkhametova-2026.md)
  estimate the error from the uncorrected SDIRK predictor, so the controller does not see their
  Patankar correction, or more conservatively add the size of the correction (Remarks 3.20–3.21).
  Enforcing positivity by rejecting steps with negative components and halving $h$ instead made the
  step size collapse to the minimum in stiff regimes (Fig. 8).

## Related practice

- **Multirate.** ARKODE's multirate module adapts only the fast time scale; multirate temporal
  adaptivity is called an open research question (Reynolds et al. 2023, §2.3). Fish & Reynolds
  (2023), published the same year, give multirate controllers for $H$ and
  $m$; see *Multirate step-size control* above. Loffeld et al. (2024, §7), running ARKODE's
  multirate methods at fixed steps, list adaptivity as work in progress.
- **Coupling to nonlinear solves.** SUNDIALS ties the default nonlinear stopping test to the
  subsequent local error test, so that nonlinear iteration errors do not interfere with error
  control (Gardner et al. 2022, §6); see [implicit stage solvers](/methods/implicit-stage-solvers.md).
- **Order instead of step.** The p-adaptive deferred correction of
  [Micalizzi & Torlo (2024)](/sources/micalizzi-2024.md) keeps the step fixed and adds subnodes and
  iterations until the relative change of the step-end value between successive iterations falls
  below a tolerance (Eq. (60)). With tolerance $10^{-8}$ the error stays roughly constant in $h$ and
  the mean number of iterations falls as $h$ decreases, from about 13 to about 5 (§8, Figs. 6,
  8–9). It adapts the order, not the step; see [deferred correction](/methods/deferred-correction.md).
- **Implicit Runge–Kutta for DAEs.** [Kirby & MacLachlan (2025)](/sources/kirby-2025.md) (§5)
  list adaptive time stepping for implicit Runge–Kutta DAEs as future work for
  [Irksome](/software/irksome.md).
- **Pseudo-time steps from positivity.** In the dual time stepping of
  [Sayyari & Yamaleev (2026)](/sources/sayyari-2026.md) the pseudo-step is set by density
  and internal-energy positivity bounds and a CFL condition, enforced only when a
  pseudo-iterate falls below user thresholds, while the physical step of the steady runs is
  set by hand, fixed or ramped down (§8, §8.2, Table 2); see [implicit stage solvers](/methods/implicit-stage-solvers.md).
- **Estimator failure.** A degenerate estimator defeats any controller: for $y'=\cos t$ the
  Rodas5 main and embedded errors coincide (Steinebach 2023, §1;
  [Rosenbrock–Wanner methods](/methods/rosenbrock-wanner-method.md)).

## Qualifications

- **Rankings of controllers differ between sources.** Fekete et al. find PID best (as does
  Vermeire (2023, §5) for stability-limit tracking, by rejected steps, without numbers), Reynolds et
  al. find PI and Gustafsson best with PID in between, and Ranocha et al. find the best
  parameters pair- and problem-dependent. The claims rest on different test sets, pairs and gain
  values, so they are not incompatible; Ranocha et al.'s step-size-control-stability analysis is
  the stated mechanism for pair dependence. Reynolds et al. keep PID as ARKODE's default
  although their own test favours PI.
- Fekete et al. attribute their controller defaults to "SUNDIALS/CVODE". [CVODE](/software/cvode.md)
  is the variable-order BDF/Adams package (Gardner et al. 2022, §2.1); the SUNDIALS package that
  offers I, PI, PID and Gustafsson controllers is ARKODE (Reynolds et al. 2023, §3.2). The
  attribution is likely loose, but Reynolds et al. do not print ARKODE's gains, so the values
  cannot be checked from the ingested sources.
- Reynolds et al. write $\lVert y_n-y(t_n)\rVert=Ch_n^{q+1}+O(h_n^{q+2})$ "assuming exact initial
  conditions for the step" and call $q$ a "global order"; the expression is the local error of
  a method of global order $q$ (§3.2, Eq. (15)).
- The superiority of error-based control is shown for dissipative (upwind) DG semidiscretizations
  at Mach 0.036–2.5; Ranocha et al. note that low Mach numbers stress the negative real axis and
  that other spectra behave differently (§5.5.4, §8). Robustness for "cold startup" is stated,
  not demonstrated, by Ranocha et al. (2022, §8); Ranocha et al. (2025, §5) demonstrate it on
  four cold-start problems.
- **Limits of error-based control.** Ranocha et al. (2025, §8) concede that it carries no hard
  guarantee: it cannot in general be proven to respect the CFL bounds under which
  invariant-domain-preserving methods are robust, and adaptive mesh refinement or positivity
  limiters applied as callbacks after a step are not seen by the error estimator. Their
  evidence, like that of Al Jahdali et al. (2022) and Vermeire (2023), is numerical.
- Al Jahdali et al. (2022, Table 4) report *identical* evaluation counts on the Imperial Front
  Wing (4250 without, 5648 and 5652 with relaxation) for five error-controlled pairs with 4 to
  9 stages and different controllers, which the paper does not comment on; their claim that
  the high-order error-controlled pairs beat the low-order CFL-controlled schemes fails for some
  relaxed runs on the Common Research Model (e.g. VRK(9,6) 141.7 s against ERK(4,2) 140.8 s).
- Vermeire (2023) leaves the exponent normalizer of Eq. (33) undefined, and its claimed
  speedups "in excess of 7 … for all considered test cases" exceed its own tables (largest
  values 7.00, 7.11 and 6.23 on the three flows).
- Belardo et al. (2026) print the ode23tx-type controller with $\mathrm{rtol}/\mathrm{err}_n$
  although their $\mathrm{err}_n$ is already divided by the tolerance. As printed, the step
  stays constant when $\mathrm{err}_n=0.8^3\,\mathrm{rtol}$, far below the acceptance threshold
  $\mathrm{err}_n\le1$, so the formula is either misprinted or very conservative; either way it
  shifts the absolute step counts of their tables, not the comparison between estimators run
  with the same controller *(compiler check, not in the sources)*.
- Faleichik & Moisa (2026) print the error estimate as $\tfrac1{10}(y_n-y_{n+1}+f(t_{n+1},y_{n+1}))$,
  without the factor $h$ on $f$; with $h$ restored, $y_n-y_{n+1}+hf(t_{n+1},y_{n+1})=\tfrac12h^2y''+O(h^3)$,
  so the printed constant gives $\tfrac1{20}h^2y''$ rather than the $\tfrac1{10}h^2y''$ of their
  Eq. (22) *(compiler check, not in the sources; arXiv v1 read)*.

- Fish & Reynolds (2023, §4.7) compare their multirate controllers with single-rate ones run at
  fixed $m=10$ and with the slow error only, whose parameters are not printed, so the cost gap
  partly measures the missing adaptivity of $m$; their "optimal" baseline is a step-local greedy
  search (App. A). Their conclusions call the advantage over PID "slight", while the fast cost of
  PID is 58 % above the worst multirate controller (§4.7). On the 1D Brusselator all controllers
  over-solve by two to four orders of magnitude (Fig. 9).
- **Tolerance exponent $5/4$ and the node count.** Saupe et al. (2025, §4.1, Fig. 8) obtain the
  $\Delta t$-$k$ exponent $q/(p+1)=5/4$ from order $q=5$ and $p+1=\mathsf M$, which requires
  $\mathsf M=4$. The paper never states $\mathsf M$ or the node type of its runs; its diagonal-SDC runs
  use three processes, one per node, which suggests $\mathsf M=3$, and Radau IIA with $\mathsf M=3$ has
  order $2\mathsf M-1=5$, which would give $5/3$ *(compiler remark, not in the source)*. The same paper
  writes that Gauss–Legendre, Lobatto and Radau nodes reach "up to order $2\mathsf M$"; only Gauss
  nodes do, Radau IIA reaching $2\mathsf M-1$ and Lobatto $2\mathsf M-2$ (see
  [fully implicit Runge–Kutta methods](/methods/fully-implicit-runge-kutta.md)).
- **Printed controller of Saupe et al.** Algorithm 2 prints the update as
  $\max\bigl(4,\,0.9\,\mathrm{err}_n^{-1/\mathsf M}\bigr)h_n$, which would grow the step by at least a
  factor 4 every time; the text describes 4 as a cap on growth, which needs $\min$ (recorded on the
  Source page).
- Babbar & Chandrashekar (2025) state that the other controller parameter sets of Ranocha et
  al. were "either superior or only slightly different" without a table, give no hardware, and
  report step counts, not times; at the stricter tolerance error control took more steps than the
  best CFL factor on the forward-facing step (Table 1). The embedded order is that of the
  truncated Taylor flux, not a proved local-error order.
- Nüßlein et al. (2021) find adaptation less efficient than a smaller step for cheap explicit
  problems, with an unoptimized implementation and no timings (§5.1).
- Pan et al. (2022) justify the floor term $1.5^p$ times the floor by guaranteed growth "by
  at least 1.5 times"; the ratio inside the root of Eq. (33) is at least $1.5^p$ only when
  $\beta_{\mathrm s}h\lVert\bar E_s\rVert\ge1.5^p\lVert E_t\rVert$, and tends to $1.5^p$ where
  both estimates are far below the floor, so growth by 1.5 is approached in quiescent elements
  but not guaranteed *(compiler check of Eq. (33), not in the source)*. They
  give two different motivations for the floor (rounding error in §2.2, truncation error in
  §3.5). The elementwise steps are aggregated into one global step, which is not
  [local time stepping](/methods/local-time-stepping.md).
- Deka & Einkemmer (2022) give no hardware for their timings, and Krylov runs that do not finish
  "within a reasonable amount of time" are excluded from their speedup factors.

# Citations

- [Fekete et al. (2022)](/sources/fekete-2022.md) — §3.1 (Eqs. (17)–(23), starting step, work measure), §3.1.1 (Figs. 9–10), §3.2.2.
- [Ranocha et al. (2022)](/sources/ranocha-2022.md) — §2.2 (Eqs. (2.6)–(2.7), Table 1), §3 (Eqs. (3.1)–(3.2), Figs. 2–3), §4 (Eq. (4.2), Table 2, Fig. 4), §5.4, §5.5, §6.1 (Fig. 6, Table 11), §7 (Tables 8–10), §8.
- [Reynolds et al. (2023)](/sources/reynolds-2023.md) — §2.3, §3.1–3.2 (Eqs. (12)–(17)), §5.1.1 (Fig. 2).
- [Gardner et al. (2022)](/sources/gardner-2022.md) — §2.1, §4.2 (Algorithm 1), §6.
- [Steinebach (2023)](/sources/steinebach-2023.md) — §1 (Rodas5 estimator failure on $y'=\cos t$).
- [Ranocha et al. (2025)](/sources/ranocha-2025.md) — §2.3 (Eqs. (2.6)–(2.7), Algorithm 2, limiter, acceptance rule, OrdinaryDiffEq.jl and PETSc variants), §2.4, §3 (Fig. 2), §4 (Fig. 3, Table 1), §5 (Tables 2–3), §6 (Tables 4–5), §7, §8.
- [Al Jahdali et al. (2022)](/sources/aljahdali-2022.md) — §2.1 (Eqs. (2)–(3), Table 1), §3 (Table 4).
- [Vermeire (2023)](/sources/vermeire-2023.md) — §2.2, §3–4, §5 (Eqs. (29)–(34)), §6 (Tables 2–4).
- [Belardo et al. (2026)](/sources/belardo-2026.md) — §4 (Eq. (3), controller, Tables 2–3).
- [Bleecke & Ranocha (2026)](/sources/bleecke-2026.md) — §1 (naive relaxation with FSAL and PID control), §2.1–2.2 (FSAL-R, R-FSAL, Theorems 1–2), §3 (Fig. 1), §4.
- [Faleichik & Moisa (2026)](/sources/faleichik-2026.md) — §4 (Eqs. (21)–(23)).
- [Glandon et al. (2022)](/sources/glandon-2022.md) — §7 (Eqs. (7.1)–(7.5), Def. 7.1, Remarks 7.2–7.3).
- [García-Archilla & Novo (2023)](/sources/garciaarchilla-2023.md) — §4 (Eqs. (110)–(112), Figs. 3–5, 8), Thms. 3–4.
- [Akrivis et al. (2024)](/sources/akrivis-2024.md) — §1.1, §1.3, Thm. 1.1.
- [Fish & Reynolds (2023)](/sources/fish-2023.md) — §1, §2 (eqs. 2.1–2.15), §3, §4 (eqs. 4.1–4.8, Figs. 4–9), §5.
- [Fish et al. (2024)](/sources/fish-2024.md) — §6.2.2 (Fig. 7).
- [Deka & Einkemmer (2022)](/sources/deka-2022.md) — §1, §2.4, §4.2–4.3, §5.2.
- [Loffeld et al. (2024)](/sources/loffeld-2024.md) — §7.
- [Saupe et al. (2025)](/sources/saupe-2025.md) — arXiv v2: §1, §2.2 (Eqs. (14)–(18), Algorithms 1–2), §2.3, §4.1 (Figs. 6, 8), §4.2 (Fig. 10), §5.
- [Babbar & Chandrashekar (2025)](/sources/babbar-2025.md) — arXiv v4: §5.1–5.2 (Eqs. (61)–(65), Algorithms 1, 3), §6.1.1 (Fig. 5b), §6.3 (Table 1), §7.
- [Nüßlein et al. (2021)](/sources/nusslein-2021.md) — arXiv v2: §3, §4.2 (Eqs. (4.1)–(4.2), Algorithm 1), §5.1, §5.3–5.4.
- [Nurkhametova et al. (2026)](/sources/nurkhametova-2026.md) — CSL-TR-26-1: Remarks 3.20–3.21, Fig. 8.
- [Micalizzi & Torlo (2024)](/sources/micalizzi-2024.md) — arXiv v4: §8 (Eq. (60), Figs. 6, 8–9).
- [Čaklović et al. (2025)](/sources/caklovic-2025.md) — arXiv v2: §4.
- [Pan et al. (2022)](/sources/pan-2022.md) — §2.1.2 (Eq. (15)), §2.1.5 (Eqs. (24)–(28)), §2.2 (Eqs. (29)–(36)), §2.3 (Eq. (37)), §2.4, §3.1–3.4 (Figs. 3–16, Tables 2–4), §4.
- [Kirby & MacLachlan (2025)](/sources/kirby-2025.md) — §5 (future work).
- [Sayyari & Yamaleev (2026)](/sources/sayyari-2026.md) — arXiv v3: §8, §8.2 (Table 2).
