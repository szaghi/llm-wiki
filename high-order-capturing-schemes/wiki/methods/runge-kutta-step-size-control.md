---
type: Method
title: "Step-size control for Runge–Kutta integration of hyperbolic problems"
description: "Choosing Δt from an embedded error estimate with a PI/PID controller instead of from a CFL number: the weighted error norm, the controller, step-size-control stability at the linear stability limit where convection-dominated runs live, its cost against CFL control, and the bound-violation and SSP rules that sit beside it."
status: established
aliases: [adaptive time stepping, PID step-size controller, error-based step control, embedded error control, CFL-based step control]
tags: [time-discretization, runge-kutta, step-size-control]
timestamp: 2026-10-12T00:00:00Z
---

# Step-size control for Runge–Kutta integration of hyperbolic problems

Capturing schemes usually set $\Delta t = \nu\,h/\max_p\vert\lambda^{(p)}\vert$
with a hand-chosen Courant number $\nu$. The alternative is to let an
[embedded pair](/methods/explicit-runge-kutta.md) estimate the local
error and a controller choose the step.

**Precursor.** Runge already judged a step by the agreement of two
second-order variants and by halving the step, without a rule for
changing it ([Runge (1895)](/sources/runge-1895.md), pp. 172, 177–178).

## Error estimate and controller

[Ranocha et al. (2022)](/sources/ranocha-2022.md) (§2.2, eqs. 6–7) use the
weighted root-mean-square error over all $N_{\mathrm{dof}}$ unknowns,
$$\mathrm{err}^{n+1} = \left(\frac{1}{N_{\mathrm{dof}}}\sum_{i=1}^{N_{\mathrm{dof}}}\left(\frac{u^{n+1}_i - u^{n+1}_{\mathrm{emb},i}}{\mathtt{atol} + \mathtt{rtol}\max\{\vert u^{n+1}_i\vert, \vert u^{n+1}_{\mathrm{emb},i}\vert\}}\right)^2\right)^{1/2},$$
usually with $\mathtt{atol} = \mathtt{rtol} = \mathtt{tol}$, and the PID controller
$$\Delta t^{n+1} = (\mathrm{err}^{n+1})^{-\beta^{\mathrm c}_1/k_{\mathrm c}}\,(\mathrm{err}^{n})^{-\beta^{\mathrm c}_2/k_{\mathrm c}}\,(\mathrm{err}^{n-1})^{-\beta^{\mathrm c}_3/k_{\mathrm c}}\,\Delta t^{n},\qquad k_{\mathrm c} = \min(p_{\mathrm t}, \hat p_{\mathrm t}) + 1,$$
with a smooth limiter on the step factor. A step is accepted if the
factor is at least $0.92$, otherwise it is retried with the predicted
step. Standard PI choices are PI42 $(0.60, -0.20, 0)$, PI33
$(0.66, -0.33, 0)$ and PI34 $(0.70, -0.40, 0)$ (Table 1). The norm treats
fine and coarse unknowns alike, unlike a quadrature norm.

## Step-size-control stability

A convection-dominated run is stability-limited: the controller holds
$z = \Delta t\lambda$ on the boundary of the main method's stability
region, outside the asymptotic regime for which classical controllers
were designed. The log-linearized controller recursion must then be
stable along that boundary, a spectral-radius test on a $6\times6$ matrix
built from $R_{\mathrm{st}}$, the embedded-minus-main stability
polynomial and $\beta^{\mathrm c}_{1,2,3}$ (§4, eqs. 10–11, after
Hairer and Wanner). The controller must be designed for its pair:
* BS5(4)7F at $\mathtt{tol} = 10^{-5}$: PI34 costs 5 015 evaluations of
  $\mathcal L$ with 132 rejections; the tuned $(0.28, -0.23, 0)$ costs
  4 119 with none, at the same error (Table 2).
* No PID controller tested is control-stable with the existing embedded
  method of Ketcheson's SSP-RK(10,4), so that method cannot yet run under
  error control (§5); see the [SSP page](/methods/ssp-runge-kutta.md).
* Tuning is a brute-force search over $\beta^{\mathrm c}$, restricted to
  control-stable values; near the stability limit more damping and a
  smaller $\beta^{\mathrm c}_1$ win, while accuracy-limited runs prefer a
  controller closer to the plain I controller (§§5.4, 6.1). Good
  controllers come within about 5 % of the best (§5.4).

## Error control against CFL control

* Over $\mathtt{tol} \in [10^{-5}, 10^{-3}]$ an untuned PI controller
  takes almost exactly the steps of a CFL controller tuned to the largest
  stable $\nu$; tighter tolerances switch it to accuracy control (§3, Figs. 2–3).
* On large compressible-flow runs at $\mathtt{tol} = 10^{-8}$, CFL control
  at $\nu = 1$ needed about 50 % more evaluations and wall time (a
  wing–body juncture flow and a racing-car front wing, Tables 8–9). CFL
  control crashed SSP3(2)4 at $\nu = 1$ on the coarser wing grid, and
  ran only after retuning to $0.85$ (Table 10). Error control "worked
  robustly with default parameters for all Runge–Kutta methods" (§7.3).
* The recommended tolerance for applied CFD is about $10^{-8}$, where
  the step is almost always stability-limited (§8). The tests use
  entropy-stable DG without shock capturing, so these results are not
  measured on discontinuous solutions.

## Rules that sit beside the controller

* **Bound violations.** A step that produces negative density or
  pressure is rejected and retried with $\Delta t/4$; there is no
  limiter ([Ranocha et al. (2022)](/sources/ranocha-2022.md), §2.2). The
  positivity-limited restart of [Zhang (2017)](/sources/zhang-2017.md)
  (§5.3) halves the step instead.
* **Weight adaptation adds to the error.** When the weights are changed
  for positivity, the perturbation $\Vert\Delta t\sum_j(\tilde{\mathsf b}_j - \mathsf b_j)\mathcal L(Y_j)\Vert$
  is added to the embedded estimate, with a PI controller from Hairer and
  Wanner ([Nüßlein, Ranocha & Ketcheson (2021)](/sources/nusslein-2021.md),
  §4.2, eqs. 4.1–4.2; [positivity-preserving adaptive Runge–Kutta](/methods/positivity-preserving-adaptive-runge-kutta.md)).
* **SSP step selection is not error control.** A variable-step
  [SSP multistep method](/methods/ssp-linear-multistep.md) takes the
  largest step its SSP condition allows, from the forward-Euler limits
  of the past states; there is no error estimate
  ([Hadjimichael et al. (2016)](/sources/hadjimichael-2016.md), §4).

# Citations

1. [Ranocha et al. (2022)](/sources/ranocha-2022.md), §§2.2, 3–5, 7–8 (Tables 1–2, 8–10).
2. [Runge (1895)](/sources/runge-1895.md), pp. 172, 177–178.
3. [Zhang (2017)](/sources/zhang-2017.md), §5.3.
4. [Nüßlein, Ranocha & Ketcheson (2021)](/sources/nusslein-2021.md), §4.2.
5. [Hadjimichael et al. (2016)](/sources/hadjimichael-2016.md), §4.
