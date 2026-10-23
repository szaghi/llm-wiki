---
type: Method
title: "Lax–Wendroff flux reconstruction (single-stage Taylor time stepping)"
description: "A single-step, single-stage Taylor (Cauchy–Kovalevskaya) time discretization of order N+1 for conservation laws that updates the solution with a Jacobian-free time-averaged flux inside flux reconstruction; its CFL limits come from von Neumann analysis, and a truncated flux series gives it an embedded error estimate for PID step-size control."
status: established
aliases: [LWFR, Lax–Wendroff flux reconstruction, LW-FR, Lax–Wendroff time discretization, approximate Lax–Wendroff procedure, single-stage Taylor time stepping, time-averaged flux, D2 dissipation, error-based time stepping for LWFR]
tags: [lax-wendroff, explicit, stability, step-size-control, ader]
timestamp: 2026-10-20T03:57:00Z
---

# Lax–Wendroff flux reconstruction (single-stage Taylor time stepping)

Lax–Wendroff flux reconstruction (LWFR) advances a hyperbolic conservation law over one
step by a single update with a **time-averaged flux**. That flux is the truncated Taylor
series in time of the physical flux, with time derivatives traded for space derivatives
through the PDE (the Cauchy–Kovalevskaya or Lax–Wendroff procedure)
([Babbar et al. 2022](/sources/babbar-2022.md), §4;
[Babbar & Chandrashekar 2025](/sources/babbar-2025.md), §3.2). Flux reconstruction (FR)
in space is applied to the time-averaged flux instead of the physical flux. With
polynomial degree $N$ in space and $N+1$ Taylor terms the scheme has formal order $N+1$
in space and time, in one stage: there are no Runge–Kutta stages and one inter-element
communication per step. It is not a method-of-lines integrator. The time scheme is a
one-stage Taylor method, the $s=1$ member of the
[multiderivative Runge–Kutta](/methods/multiderivative-runge-kutta.md) family
([Chouchoulis et al. 2022](/sources/chouchoulis-2022.md), Remark 2), evaluated with
element-local derivatives *(compiler remark: Babbar et al. do not use the multiderivative
framing)*.

**Page-local notation.** Scalar law $u_t+g(u)_x=0$ in 1-D ($g$ the physical flux; the
sources write $f$, which the registry reserves for the right-hand side of $y'=f(t,y)$).
$N$ is the polynomial degree, $\Delta x$ the cell width, $h$ the step and $\nu$ the
Courant number (registry symbols; the sources write $\Delta t$ and $\sigma$). $G$ is the
time-averaged flux and $U$ the time-averaged solution. $D$ is the differentiation matrix
on the $N+1$ solution points of a cell. $u^{(m)}=h^m\partial_t^mu$ and
$g^{(m)}=h^m\partial_t^mg$ are scaled time derivatives.

## The single-stage update

Taylor-expand $u(t_{n+1})$ to order $N+1$ and use $\partial_t^mu=-\partial_x\partial_t^{m-1}g(u)$
(Babbar et al. 2022, Eqs. (2)–(5)):

$$u^{n+1}=u^n-h\,\partial_xG+\mathcal O(h^{N+2}),\qquad G=\sum_{m=0}^{N}\frac{h^m}{(m+1)!}\,\partial_t^mg(u),\qquad U=\sum_{m=0}^{N}\frac{h^m}{(m+1)!}\,\partial_t^mu .$$

$G$ is $\frac1h\int_{t_n}^{t_{n+1}}$ of the degree-$N$ Taylor polynomial of $g$ in time,
whence the name (Eq. (4)). The update is the same at every order; only $G$ changes. The
FR step interpolates $G$ at the solution points, corrects the interpolant to continuity
with correction functions (Radau or Huynh's $g_2$) using a numerical flux, and
collocates $\partial_xG$ at the solution points (Eqs. (5), (7)). Conservation of the cell
mean follows from quadrature exactness (§4.1). On curvilinear meshes the same update acts
on contravariant fluxes, $u^{n+1}=u^n-\frac hJ\nabla_\xi\cdot G$ with $J$ the metric
Jacobian (page-local), and Babbar & Chandrashekar (2025, §3.3) prove free-stream
preservation under the discrete metric identities that FR and DG need, which in 2-D hold
when the reference map has degree at most $N$.

With Radau correction on Gauss–Legendre points LWFR equals a direct flux reconstruction
Lax–Wendroff scheme on $N+3$ points (proved, Babbar et al. 2022, App. C) and is identical
to Lax–Wendroff DG; its CFL numbers then agree with those of
[ADER-DG](/methods/ader-time-integration.md) (§6, stated). The limiter is applied once per
step instead of once per Runge–Kutta stage (§7).

## The approximate Lax–Wendroff procedure (Jacobian-free)

Exact flux derivatives need $g'$, $g''$, … and grow intractable with the order; the exact
chain-rule version of Lou et al. is called tedious and more expensive (Babbar et al. 2022,
§1). LWFR instead uses the **approximate Lax–Wendroff procedure** of Zorío, Baeza & Mulet
(as recalled, §4.4): centred finite differences in time of $g$ evaluated at
Taylor-extrapolated states, each $u^{(m)}=-\frac h{\Delta x}Dg^{(m-1)}$ computed from the
previous flux derivative. For $N=1$ and $N=2$ (Eqs. in §4.4.1–4.4.2):

$$\begin{aligned}
N=1:\quad G&=g+\tfrac12g^{(1)},\qquad g^{(1)}=\tfrac12\big[g(u+u^{(1)})-g(u-u^{(1)})\big],\\
N=2:\quad G&=g+\tfrac12g^{(1)}+\tfrac16g^{(2)},\qquad g^{(2)}=g\big(u+u^{(1)}+\tfrac12u^{(2)}\big)-2g(u)+g\big(u-u^{(1)}+\tfrac12u^{(2)}\big).
\end{aligned}$$

$N=3,4$ use five-point centred differences; $\partial_t^mg$ must be approximated to
$\mathcal O(h^{N+1-m})$, which the authors assert ("it can be shown") rather than prove.
Only flux evaluations are needed.

[Chouchoulis et al. (2022)](/sources/chouchoulis-2022.md) use the same device, in the
compact approximate Taylor (CAT) form of Carrillo & Parés, inside multistage
multiderivative schemes; their Jacobian-free MDRKCAT family, its consistency theorem and
critical CFL numbers are on the [multiderivative page](/methods/multiderivative-runge-kutta.md).
Two of their findings bear on single-stage Taylor schemes. The original CAT method is a
Taylor method of order $2\mathsf p$ ($\mathsf p$ the stencil half-width, page-local),
reduces to high-order Lax–Wendroff for linear problems and is linearly stable up to CFL 1,
as recalled from Carrillo & Parés (§5). Yet CAT-$\mathsf p$ with $\mathsf p=4,5,6$
diverges on smooth Burgers data at $\nu=0.5$ "well before shocks are formed", in regions
of large $\lvert u_0'\rvert$; the multistage MDRKCAT schemes do not (§6.1, Fig. 2).

## Dissipation and face fluxes

Babbar et al. (2022, §5) place their contribution in the numerical flux at faces:

- **D1** takes the dissipative jump of a Rusanov-type flux from $u^n$ (as in
  Qiu–Dumbser–Shu); **D2** takes it from the time-averaged solution $U$. D2 is exactly
  upwind for constant linear advection, D1 is not, and D2 costs nothing extra because $U$
  is accumulated during the procedure (Remark 1).
- **AE** (average, then extrapolate) takes face values of $G$ from the interior
  interpolant; **EA** (extrapolate, then average) applies the approximate procedure at the
  faces to extrapolated states. AE loses half an order, about $\mathcal O(\Delta x^{N+1/2})$,
  at odd $N$ on Burgers near sonic points and on variable-coefficient advection, for a
  reason "not known at present"; EA is optimal at all $N$ (§8.2–8.3). The two coincide
  for GLL solution points and for constant-coefficient advection (Remark 3).

The recommended combination is Radau correction, Gauss–Legendre points, EA and D2 (§13).
Inflow boundary data enter as the time average $\frac1h\int_{t_n}^{t_{n+1}}g(u_b(t))\,dt$
by $(N+1)$-point Gauss quadrature, which avoids stage boundary values; Runge–Kutta at its
own CFL shows slightly larger errors at $N=3,4$ with Dirichlet inflow, which the authors
attribute to the treatment of stage boundary data (Remark 4, Fig. 6b; see
[boundary conditions for Runge–Kutta stages](/methods/runge-kutta-stage-boundary-treatment.md)).

## Linear stability: Fourier CFL numbers

The CFL limits come from a [von Neumann analysis](/definitions/von-neumann-stability-analysis.md)
of the fully discrete scheme, not from a stability region. For $g(u)=au$, D2 and
Courant number $\nu=ah/\Delta x$, the cell update is
$u^{n+1}_e=-\nu A_{-1}u^n_{e-1}+(I-\nu A_0)u^n_e$ with $A_{-1}=b_LV_R^\top T$,
$A_0=DT-b_LV_L^\top T$ and $T=\sum_{m=0}^N\frac{(-\nu D)^m}{(m+1)!}$ ($b_L$ the left
correction derivatives, $V_L$, $V_R$ the boundary interpolation vectors, page-local;
Eq. (11)). The amplification matrix is
$H(\nu,\kappa)=I-\nu A_0-\nu A_{-1}e^{-\mathrm i\kappa}$ ($\kappa$ the dimensionless
wavenumber, page-local), and the CFL number is the largest
$\nu$ with $\max_\kappa\rho(H)\le1$, found by sampling $\kappa\in[0,2\pi]$ (§6). Table 1:

| correction, dissipation | $N=1$ | $N=2$ | $N=3$ | $N=4$ |
|---|---|---|---|---|
| Radau, D1 | 0.226 | 0.117 | 0.072 | 0.049 |
| Radau, D2 | 0.333 | 0.170 | 0.103 | 0.069 |
| $g_2$, D1 | 0.465 | 0.204 | 0.116 | 0.060 |
| $g_2$, D2 | 1.000 | 0.333 | 0.170 | 0.103 |

D2 raises the limit by factors 1.41–2.15 (ratios of the printed values). The numbers are sharp: linear advection blows up
slightly above them (§6). In 2-D the stable set is $\lvert\nu_1\rvert+\lvert\nu_2\rvert\le$
CFL except at $N=1$ (Radau D2: 0.259, 0.166, 0.101, 0.067), because the face fluxes do not
couple diagonal neighbours (App. B, Table 2).

The temporal operator $T$ is built from the element-local matrix $D$, and the interface
correction acts only once, on $G$. LWFR is therefore not the Taylor polynomial
$\sum_{j\le N+1}z^j/j!$ applied to the FR semi-discretization, and its CFL numbers do not
follow from that polynomial's stability region *(compiler remark, from the printed
matrices)*. Chouchoulis et al. (2022, §5) make the same point for MDRK–Lax–Wendroff schemes,
where products of discrete derivative symbols differ from the symbol of the higher
derivative.

The Fourier analysis covers uniform Cartesian grids only. On curvilinear meshes a
wave-speed CFL formula with the Fourier number "need not guarantee $L^2$ stability" and has
to be tuned per problem, which motivates error control (Babbar & Chandrashekar 2025, §5).

## Error-based step-size control for a single-stage method

Babbar & Chandrashekar (2025, §5.2, Algorithms 1, 3) build an embedded solution without a
second stage. Write the update as an element-local part plus interface terms, and keep only
the local part. The main local update uses the full $G$ ($N+1$ Taylor terms); the embedded
one truncates it one term earlier:

$$u^{n+1}_{\mathrm{loc}}=u^n-h\,\partial_\xi G^\delta,\qquad \hat u^{n+1}_{\mathrm{loc}}=u^n-h\,\partial_\xi\hat G^\delta,\qquad \hat G^\delta=\sum_{m=0}^{N-1}\frac{h^m}{(m+1)!}\,\partial_t^mg^\delta$$

($\delta$ marks the discontinuous element-local interpolant; metric factors dropped). The
difference feeds the weighted RMS norm of Ranocha et al. over all degrees of freedom, with
$\max\{\lvert u^{n+1}_{\mathrm{loc}}\rvert,\lvert\hat u^{n+1}_{\mathrm{loc}}\rvert\}$ in the
scaling, accumulated inside the cell loop with no extra communication:

$$\mathrm{err}_n=\big\lVert u^{n+1}_{\mathrm{loc}}-\hat u^{n+1}_{\mathrm{loc}}\big\rVert_{\mathrm{WRMS}}.$$

The step is set by the PID controller of the registry with $(\beta_1,\beta_2,\beta_3)=(0.6,-0.2,0)$,
the values Ranocha et al. give for BS3(2)3$_F$, and the limiter
$x\mapsto1+\tan^{-1}(x-1)$ on the step ratio. A step is accepted iff the limited
ratio is at least $0.9^2$ and no inadmissible state appears; otherwise it is redone with
the proposed step (Algorithm 3). The paper uses the inverse-error convention of Ranocha et
al., working with $1/\mathrm{err}_n$. It does not state the exponent order $k$ it uses; with
main order $N+1$ and embedded order $N$, the registry rule gives $k=N+1$ *(compiler
inference)*. See [step-size control](/methods/step-size-control.md) and
[embedded pairs](/methods/embedded-runge-kutta-pair.md).

Results (§6, Table 1; $\mathrm{atol}=\mathrm{rtol}=10^{-6}$ unless stated; step counts
against the best hand-tuned constant CFL coefficient without admissibility failures):

| test | CFL-based steps | error-based steps | ratio |
|---|---|---|---|
| Mach 3 forward step (straight-sided) | 5,679,021 | 7,633,954 ($10^{-6}$); 5,598,338 ($5\times10^{-6}$) | 0.74; 1.01 |
| Mach 3 cylinder (curved) | 1,601,725 | 1,057,844; 768,835 ($5\times10^{-6}$) | 1.51; 2.08 |
| transonic NACA0012 (curved) | 7,530,003 | 4,842,326 | 1.55 |
| Mach 4 blunt body (poor mesh) | no constant CFL reaches $t=10$ | 30,527 (761 rejected) | — |

The estimate costs about 4 % (stated from experiments that are not reported; no timing table or hardware). On a cold-start Mach
2000 jet the controller ramps the effective CFL coefficient from about $10^{-3}$ to
$10^{-1}$ by itself, which a CFL-based run would have to prescribe (§6.1.1, Fig. 5b). The
gain is robustness first and efficiency on curved meshes; on the straight-sided step the
tuned CFL needs fewer steps at the tighter tolerance.

## Cost against Runge–Kutta flux reconstruction

Runge–Kutta needs at least $p$ stages for order $p$ and more at high order: there is no
five-stage fifth-order method for nonlinear problems and no fifth-order SSP method with
positive coefficients, as Babbar et al. (2022, §1) recall. On the 2-D isentropic vortex
LWFR-D2 is 1.1, 1.4, 1.7 times faster in wall-clock time than RKFR for $N=1,2,3$ and 1.2
at $N=4$, each at its own optimal CFL number, with Runge–Kutta accuracy on nonlinear
problems; the ratio LW-D1/LW-D2 (1.4–1.5 for $N>1$) matches the CFL ratios (§12.1, Figs.
37–40; no hardware stated). On the double Mach reflection the RK/LW ratio is 1.1–1.6
(Figs. 41–43). See [isentropic vortex](/benchmarks/isentropic-vortex.md) and
[double Mach reflection](/benchmarks/double-mach-reflection.md).

## Relation to ADER and multiderivative methods

Historical ADER is also a Taylor/Cauchy–Kovalevskaya construction; modern ADER replaces it
by a local Galerkin predictor (see [ADER](/methods/ader-time-integration.md)). LWFR keeps
the Taylor route and removes the Jacobians by finite differences in time. Both are
one-step schemes with one communication per step. The multistage generalization of the
Taylor update is the explicit [multiderivative Runge–Kutta](/methods/multiderivative-runge-kutta.md)
method, made Jacobian-free in the same way by Chouchoulis et al. (2022).

## Qualifications

- **"First" error-based stepping for a single-stage method.** Babbar & Chandrashekar
  (2025, §7) call theirs "the first time error-based time stepping has been introduced for
  a single stage evolution method". This is the authors' claim. The bundle holds no
  counter-example: its ADER sources ([Han Veiga et al. 2021](/sources/hanveiga-2021.md),
  [Gaburro et al. 2023](/sources/gaburro-2023.md), [Wolf et al. 2022](/sources/wolf-2022.md),
  [Popov 2024](/sources/popov-2024.md)) use fixed, prescribed or CFL-set steps; Popov allows
  variable steps but has no controller. The nearest relatives are multi-stage or
  multi-sweep: order adaptivity at fixed step for explicit
  [deferred correction](/methods/deferred-correction.md)
  ([Micalizzi & Torlo 2024](/sources/micalizzi-2024.md), §8), and step selection from the
  increment between sweeps of spectral deferred correction, by doubling and halving in
  Dutt, Greengard & Rokhlin as recalled by [Saupe et al. (2025)](/sources/saupe-2025.md)
  (§1), with a continuous controller in Saupe et al. themselves. Adaptive Taylor-series
  integrators outside the bundle are not checked.
- **Heuristic estimate.** The embedded update is "one order of accuracy lower" by the
  truncation of the flux series; there is no proof that the difference of the two local
  updates, with the interface terms dropped from both, is an asymptotically correct
  estimate of the local error of the full scheme. The controller of Ranocha et al. was
  derived for Runge–Kutta pairs of the full semi-discretization.
- **Stability.** Positivity with the Zhang–Shu limiter is not proved for LW (Babbar et al.
  2022, §8.4); a mild linear instability at $N=4$ with periodic data affects LW and SSP
  Runge–Kutta alike (relative $L^2$ growth slopes about $6\times10^{-10}$ for LW against
  $2$–$3\times10^{-13}$ for SSPRK, Fig. 5d), and the authors' statement that ADER-DG shares
  it is not shown.
- **CFL and timing comparisons.** The 2-D Euler timings use Runge–Kutta at its
  own optimal CFL; the scalar comparisons use LW CFL numbers for both. No hardware is
  stated in either paper.
- **Printed slips** *(compiler check against the PDFs, not in the sources)*. Babbar et al.
  (2022) print a repeated $\frac{2^3}{3!}u^{(3)}$ where the $N=4$ EA state needs
  $\frac{2^4}{4!}u^{(4)}$ (§5.2, against their §4.4 formula for $g^{(4)}$). Babbar &
  Chandrashekar (2025, §5.2) state the acceptance test inverted once ("redo the time step
  if" the ratio is at least $0.9^2$; Algorithm 3 and the preceding sentence are correct),
  and print the CFL step formula (66) as a minimum of metric-scaled wave-speed sums where
  the reciprocal is meant.

# Citations

- [Babbar et al. (2022)](/sources/babbar-2022.md) — §1; §4 (Eqs. (2)–(7)), §4.1, §4.3, §4.4 (approximate Lax–Wendroff formulas); §5 (D1, D2, Remarks 1–3), §5.1–5.2 (AE, EA); §6 (Eq. (11), Table 1); §7; §8.1–8.4 (Figs. 2–21, Remark 4); §12.1 (Figs. 37–40); App. B (Table 2); App. C; §13.
- [Babbar & Chandrashekar (2025)](/sources/babbar-2025.md) — §3.2 (Eqs. (23)–(28)), §3.3 (free-stream preservation); §5, §5.1–5.2 (Eqs. (60)–(66), Algorithms 1, 3); §6.1.1 (Fig. 5b), §6.3 (Table 1); §7.
- [Chouchoulis et al. (2022)](/sources/chouchoulis-2022.md) — Remark 2 (Taylor methods as one-stage MDRK); §3 (CAT, Alg. 1); §5 (CAT CFL 1, MOL remark); §6.1 (Fig. 2, CAT divergence).
- [Micalizzi & Torlo (2024)](/sources/micalizzi-2024.md) — §8 (order-adaptive DeC, for the novelty claim).
- [Saupe et al. (2025)](/sources/saupe-2025.md) — §1 (earlier SDC step selection, for the novelty claim).
- [Popov (2024)](/sources/popov-2024.md) — §1.1 (variable steps without control, for the novelty claim).
