---
type: Method
title: "Step-size control: error-based controllers, PID filters and CFL control"
description: "Adaptive time stepping: a scaled norm of the embedded local-error estimate decides acceptance, and an I, PI, PID or Gustafsson controller sets the next step; step-size-control stability, controller tuning per pair, and error-based versus CFL-based control for stability-limited CFD."
status: established
aliases: [adaptive time stepping, error control, PID controller, PI controller, digital-filter step-size controller, Gustafsson controller, CFL-based step size control, step size control stability]
tags: [step-size-control, explicit, runge-kutta, software]
timestamp: 2026-10-19T00:00:00Z
---

# Step-size control: error-based controllers, PID filters and CFL control

**Error-based step-size control** computes, after each step, a scaled local-error estimate
$\mathrm{err}_n$ (usually from an [embedded pair](/methods/embedded-runge-kutta-pair.md),
$y_{n+1}-\hat y_{n+1}$), accepts the step iff $\mathrm{err}_n\le1$, and chooses the next step
$h_{n+1}$ from the current and past estimates with a **controller**. **CFL-based control**
instead sets $h_n$ from a Courant number $\nu$ and the current wave speeds. The sources agree
that a time integrator is the triple *(main method, error estimator, controller)*, not the main
method alone (Ranocha et al. 2022, §8; Fekete et al. 2022, §3).

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

Fekete et al. also use Gustafsson's explicit (predictive) controller with gains 0.367 and 0.268,
an I step on the first step and an error floor $\mathrm{err}>10^{-10}$ (Eq. (23)).
ARKODE offers PID (its default), PI, I, explicit and implicit Gustafsson controllers, an "ImEx"
Gustafsson controller that takes the smaller of the two, and user-supplied controllers; its
default parameters were tuned by "an exhaustive genetic optimization" over dozens of test
problems, including most of the Bari "Test Set for IVP Solvers", but the controller formulas
and values are not printed (Reynolds et al. 2023, §3.2).

**Exponent denominator.** Ranocha et al. use $k=\min(p,\hat p)+1$, usually $k=p$ under local
extrapolation (§2.2); Fekete et al. print $p$ without saying whether the main or the embedded
order is meant (§3.1); ARKODE uses the embedding order by default and the main order on request
(Reynolds et al. §3.2).

**Limiters and rejections.** All three implementations bound the step ratio, with different
rules:

- Fekete et al. apply a safety factor 0.9 and bound the ratio to $[0.1,5]$; after a rejection
  the upper bound drops to 0.9, a change made to stop an observed infinite loop (Eqs. (18)–(19)).
- Ranocha et al. mention the smooth limiter $1+\arctan(x-1)$ of Söderlind and Wang. They accept a
  step iff the controller's factor is at least $0.9^2=0.81$, and retry otherwise with the PID
  step. A step whose solution leaves physical bounds (negative density or pressure) is rejected
  and retried with $h$ divided by 4 (§2.2).
- ARKODE inherits the CVODE heuristics: growth and decay bounds, a reduction after repeated
  error failures or after a failed implicit solve, and $h_{\min}\le h\le h_{\max}$ (Reynolds et
  al. §3.2).

**Initial step.** Fekete et al. and Ranocha et al. both use the Hairer–Nørsett–Wanner starting
procedure; for PDEs Fekete et al. take the minimum of that step and the CFL step (§3.1; §2).

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

## Related practice

- **Multirate.** ARKODE's multirate module adapts only the fast time scale; multirate temporal
  adaptivity is called an open research question (Reynolds et al. 2023, §2.3).
- **Coupling to nonlinear solves.** SUNDIALS ties the default nonlinear stopping test to the
  subsequent local error test, so that nonlinear iteration errors do not interfere with error
  control (Gardner et al. 2022, §6); see [implicit stage solvers](/methods/implicit-stage-solvers.md).
- **Estimator failure.** A degenerate estimator defeats any controller: for $y'=\cos t$ the
  Rodas5 main and embedded errors coincide (Steinebach 2023, §1;
  [Rosenbrock–Wanner methods](/methods/rosenbrock-wanner-method.md)).

## Qualifications

- **Rankings of controllers differ between sources.** Fekete et al. find PID best, Reynolds et
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
  not demonstrated (§8).

# Citations

- [Fekete et al. (2022)](/sources/fekete-2022.md) — §3.1 (Eqs. (17)–(23), starting step, work measure), §3.1.1 (Figs. 9–10), §3.2.2.
- [Ranocha et al. (2022)](/sources/ranocha-2022.md) — §2.2 (Eqs. (2.6)–(2.7), Table 1), §3 (Eqs. (3.1)–(3.2), Figs. 2–3), §4 (Eq. (4.2), Table 2, Fig. 4), §5.4, §5.5, §6.1 (Fig. 6, Table 11), §7 (Tables 8–10), §8.
- [Reynolds et al. (2023)](/sources/reynolds-2023.md) — §2.3, §3.1–3.2 (Eqs. (12)–(17)), §5.1.1 (Fig. 2).
- [Gardner et al. (2022)](/sources/gardner-2022.md) — §2.1, §4.2 (Algorithm 1), §6.
- [Steinebach (2023)](/sources/steinebach-2023.md) — §1 (Rodas5 estimator failure on $y'=\cos t$).
