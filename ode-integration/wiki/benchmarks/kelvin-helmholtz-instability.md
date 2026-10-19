---
type: Benchmark
title: "Kelvin–Helmholtz instability"
description: "A periodic shear layer whose perturbation rolls up into vortices; the sources use an inviscid Euler version to test multirate P-ERK families and error-based step-size control under shock capturing and positivity limits, and a resistive-MHD version to compare exponential integrators, Leja and Krylov evaluation, step-size controllers and implicit BDF."
status: established
aliases: [KHI, Kelvin–Helmholtz, shear-layer instability]
tags: [verification, multirate, step-size-control, exponential, positivity]
timestamp: 2026-10-20T05:00:00Z
---

# Kelvin–Helmholtz instability

The Kelvin–Helmholtz instability (KHI) test perturbs a periodic shear layer between two
streams; the perturbation grows and rolls up into vortices whose fine structure
depends on numerical dissipation. For time integration it is a stress test of
**nonlinear** stability: the semi-discretization is a convection-dominated DG or
finite-difference system whose spectrum, shock-capturing activity and positivity
margins change during the run. Three sources use it, in two physical settings.

## Euler setting

Both Euler setups are periodic on $[-1,1]^2$ with ratio of specific heats 1.4, the switch function
$B(y)=\tanh(15y+7.5)-\tanh(15y-7.5)$ (page-local), pressure 1 and
$v_2=\tfrac1{10}\sin(2\pi x)$:

| Source | Density | $v_1$ | Final time | Discretization |
|---|---|---|---|---|
| [Doehring et al. (2024b)](/sources/doehring-2024-b.md), §7.2.1 | $\rho=\tfrac12+\tfrac34B$ | $\tfrac12(B-1)$ | $t=3$ | DGSEM $k=3$, HLLE, entropy-conservative volume flux, subcell shock capturing; $2^4\times2^4$ base cells with five AMR levels (finest $\Delta x=2^{-8}$) |
| [Ranocha et al. (2025)](/sources/ranocha-2025.md), §6, eqs. 6.1–6.2 | $\rho=\rho_1+B(\rho_2-\rho_1)$, $\rho_1=1$, $\rho_2=\rho_1\frac{1+\mathcal A}{1-\mathcal A}$ | $B-\tfrac12$ | $t=5$ | entropy-stable Gauss DG with entropy projection, $32^2$ elements, degree 3 |

with $\mathcal A$ the Atwood parameter (page-local), $\mathcal A=3/7$ or $0.7$, and DG
degree $k$ (page-local). Doehring et al. take their setup from an earlier Trixi.jl
study; Ranocha et al. from a study of entropy-stable Gauss DG. As printed, $B(0)=2\tanh7.5\approx2$, so $B$
ranges over $[0,2]$: Doehring et al.'s density runs from $\tfrac12$ to 2 and Ranocha et al.'s at
$\mathcal A=3/7$ from 1 to 4, exactly twice as large, so both have density ratio 4 and the
nominal $\rho_2/\rho_1=2.5$ of Ranocha et al. is exceeded in the layer; the velocity profiles
differ ($v_1\in[-\tfrac12,\tfrac12]$ against $[-\tfrac12,\tfrac32]$) *(compiler check of the
printed formulas, verified on both PDFs' printed equations, not in the sources)*.

**What it tests.**

- **Multirate partition interfaces.** Doehring et al. (2024b, §7.2.1, Table 10) run a
  three-member third-order [paired explicit Runge–Kutta](/methods/paired-explicit-runge-kutta.md)
  family P-ERK$_{3;\{4,6,11\}}$ on the AMR mesh. It is the fastest scheme, but only at 70 %
  of the CFL number of the standalone P-ERK$_{3;11}$, because partition interfaces
  lose monotonicity on inviscid flow; relative runtimes are 1.311 (standalone
  P-ERK$_{3;11}$), 1.426 (SSPRK(3,3)), 1.169 (seven-stage low-dissipation DG method of
  Toulorge–Desmet), 1.866 and 1.659 (two DG/CFD-optimized five-stage methods). The
  low-dissipation method beats the optimized standalone P-ERK and SSPRK(3,3) beats the
  DG-optimized methods; runtime is not proportional to right-hand-side count because
  P-ERK triggers shock capturing in more cells. The same case supplies the spectrum
  for the shifted-Arnoldi boundary estimate on
  [optimal stability polynomials](/methods/optimal-stability-polynomial.md).
- **Error-based step-size control.** Ranocha et al. (2025, §6, Tables 4–5) compare
  error-based [step-size control](/methods/step-size-control.md) with tuned CFL control.
  At $\mathcal A=3/7$ error-based control always needs fewer right-hand-side evaluations
  and steps, "usually around 5 %"; SSP3(2)4[3S*$_+$] is most efficient (5478 evaluations),
  then RDPK3(2)5$_F$ (6403); RDPK4(3)9$_F$ needs $\mathrm{tol}=10^{-5}$. At $\mathcal A=0.7$
  the evolved variables lose [positivity](/properties/positivity-preservation.md) near
  $t\approx3$ even at Courant number 0.05 for SSP3(2)4, so **CFL-based control is not
  possible**, while error-based control runs directly (SSP3(2)4: 6618 evaluations).

## Resistive-MHD setting

[Deka & Einkemmer (2022)](/sources/deka-2022.md) (§4.1, Table 2, Eqs. 12–13) use a 2.5-D
resistive-MHD shear layer on $[-1.25,1.25]\times[-0.5,0.5]$, periodic in both directions:
$v=(v_0\tanh(y/\xi)+v_{\mathrm{pert}},0,0)$,
$v_{\mathrm{pert}}=\epsilon_x\cos(2\pi\omega_xx/L_x)+\epsilon_y\sin(\pi(2\omega_y-1)y/L_y)$ with
$\epsilon_x=\epsilon_y=0.1$, $\omega_x=\omega_y=2$, $\xi=0.1$, $\rho=1$, $P=0.25$,
magnetic field $(0.1,0,10)$ (all page-local; $v_0$ is not given numerically). Four cases: I $512^2$,
$t=1$ and II $800^2$, $t=0.3$ with dimensionless viscosity, resistivity and conductivity
$(0.25,10^{-2},10^{-4})$ (diffusion-dominated); III $128^2$, $t=2$ and IV $256^2$, $t=1$ with
$(10^{-4},10^{-4},10^{-4})$. Errors are $\ell^2$ against a run at $\mathrm{tol}=10^{-11}$.

**What it tests** (fourth-order exponential Rosenbrock EXPRB43, see
[exponential integrators](/methods/exponential-integrators.md)):

- **Leja versus Krylov** evaluation of the $\phi$-functions
  ([φ-function evaluation](/methods/phi-function-evaluation.md)): Leja is faster by a factor
  2.5 (case I, against tolerance), 3 (case II) and about 6 and 8 (cases III–IV, against
  tolerance) and shows a systematic decrease of error with cost, while Krylov's cost is
  "somewhat unpredictable" (§4.2).
- **Cost-based versus error-based step control**: the cost-minimizing controller beats
  the traditional one for both Leja and Krylov in cases I–II and for Leja in III–IV;
  with the traditional controller Krylov converges only at $\mathrm{tol}=10^{-5},10^{-6}$ in
  case I (§4.2; [step-size control](/methods/step-size-control.md)).
- **Against explicit and implicit baselines**: EXPRB43 with Leja is 6.3× and 8.4× faster
  than RK43 and DOPRI54 at equal error in case II, and up to 3× (case III) and 2.3× (case
  IV) faster than [CVODE](/software/cvode.md)'s variable-order
  [BDF](/methods/backward-differentiation-formula.md) (§4.3, Figs. 7–8).
- **Spectral-estimate frequency**: re-estimating the largest Jacobian eigenvalue every 50
  steps instead of every step costs 1.7 % instead of 39 % of the runtime (case III,
  $\mathrm{tol}=10^{-4}$; Table 3).

## Qualifications

- The two settings share only the name and the shear-layer geometry; results do not
  transfer between them. No hardware is stated for Deka & Einkemmer's timings.
- Deka & Einkemmer's Fig. 1 shows case-IV snapshots at $t=2$ and $t=2.75$, beyond case IV's
  stated final time $t=1$; their abstract's "up to a factor of three" Leja gain is smaller
  than the factors 6–8 reported in §4.2.
- Doehring et al. (2024b) print the optimality of the KHI family as $\kappa=92.4\,\%$ (Table
  10) but call it "1.035 of the optimal" in the text, where $1/0.924\approx1.082$.

# Citations

- [Doehring et al. (2024b)](/sources/doehring-2024-b.md) — §4.1 (Fig. 5), §7.2.1 (Table 10).
- [Ranocha et al. (2025)](/sources/ranocha-2025.md) — §6 (eqs. 6.1–6.2, Tables 4–5).
- [Deka & Einkemmer (2022)](/sources/deka-2022.md) — §4.1 (Table 2, Eqs. 12–13), §4.2 (Figs. 2–6, Table 3), §4.3 (Figs. 7–8).
