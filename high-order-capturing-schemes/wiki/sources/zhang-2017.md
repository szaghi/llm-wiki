---
type: Source
title: "Zhang (2017) — On positivity-preserving high order discontinuous Galerkin schemes for compressible Navier–Stokes equations"
description: "First high-order schemes for 2D compressible Navier–Stokes that keep density and internal energy positive while conserving energy: a Lax–Friedrichs-type viscous flux whose penalty is chosen from the stress, heat flux and state, weak-positivity theorems for FV and DG on rectangles and triangles, an efficient scaling limiter, and the finding that resolved viscous flows need no extra oscillation limiter."
resource: "doi:10.1016/j.jcp.2016.10.002"
source_kind: paper
authors: [Zhang X.]
year: 2017
venue: "J. Comput. Phys. 328:301-343"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2017-JCP-Zhang-101016jjcp201610002.pdf"
tags: [positivity, dg, navier-stokes, limiter]
timestamp: 2026-10-09T00:00:00Z
---

# Summary

Extends the Zhang–Shu positivity framework from the Euler to the
compressible Navier–Stokes equations by treating the convective minus
the viscous flux as one flux. A Lax–Friedrichs-type viscous flux with a
nonlinear penalty $\beta^{\mathrm v}_{i+1/2}$, chosen from $\boldsymbol\tau$,
$\mathbf q$ and the state, keeps the first-order building block
admissible. In a DG scheme of Bassi–Rebay type this amounts to an
interior-penalty term with a nonlinear coefficient. Merged into the
[positivity](/properties/positivity-preserving.md),
[scaling-limiter](/methods/positivity-preserving-scaling-limiter.md),
[WENO-limited DG](/methods/weno-limited-dg.md) and
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md) pages, and the Sedov,
shock-diffraction, double-Mach, Lax, double-rarefaction and vortex
benchmarks.

# Key claims

1. **Admissible set** (§1.2, eqs. 3–4): written with $\rho e(u) > 0$; the
   Hessian of $\rho e$ shows its concavity, hence convexity of the set,
   for a general equation of state.
2. **Lemma 6** (App. B), for an admissible state and unit normal:
   * $\alpha u \pm f(u)\cdot\mathbf n$ is admissible iff
     $\alpha > |\mathbf v\cdot\mathbf n| + \sqrt{p^2/(2\rho^2e)}$
     (for an ideal gas the root equals $(\gamma - 1)\sqrt{e/2}$, below $c$, so the usual $|\mathbf v\cdot\mathbf n| + c$ suffices; $e$ is the specific internal energy);
   * $\beta u \pm \mathbf f^{\mathrm v}\cdot\mathbf n$ is admissible iff
     $\beta > \frac{1}{2\rho^2 e}\left(\sqrt{\rho^2 q_n^2 + 2\rho^2 e\,|\boldsymbol\tau\mathbf n|^2} + \rho|q_n|\right)$, $q_n = \mathbf q\cdot\mathbf n$;
   * the joint flux has the analogous bound with $|\mathbf v\cdot\mathbf n|$
     added and $\boldsymbol\tau\mathbf n - p\mathbf n$ in place of
     $\boldsymbol\tau\mathbf n$. This joint flux is the one used in every
     test (§§2.4, 6.1; checked on the page images).
3. **Viscous flux** (§1.5, eq. 9): the central flux plus
   $\tfrac12\beta^{\mathrm v}_{i+1/2}(u^+ - u^-)$, independent of the
   equation of state, the stress and heat-flux laws, and the gradient
   approximation.
4. **Weak positivity** (Theorems 1–3): cell averages stay admissible under
   $\frac{\Delta t}{h}\max\beta^{\mathrm v} \le \hat w_1 = \frac{1}{N(N-1)}$ in 1D, and
   in 2D under $\Delta t(1/h_x + 1/h_y)\beta^{\mathrm v} \le \hat w_1$ on rectangles
   and a **per-edge** bound $\Delta t\,\frac{|e_i|}{|K|}\beta^{\mathrm v}_i \le \tfrac23\hat w_1$
   on triangles (eq. 33), which the paper calls better than the summed
   bound that follows Zhang–Xia–Shu (2012).
5. **A weak stability.** The positivity bound allows $\Delta t = O(h)$ for
   smooth viscous flow, while linear stability needs $O(\mathrm{Re}\,h^2)$.
   With the first met and the second violated, errors grow exponentially
   while positivity, and $L^1$ stability, still hold (§1.7, Remark 2).
6. **Monotone diffusion stops at second order** (§1.4, App. D): no linear
   finite-difference approximation of $u_{xx}$ above second order is
   monotone, which motivates treating diffusion as a flux.
7. **Limiter** (§4): the single-ratio internal-energy factor $\theta_e$,
   taken from Wang, Zhang, Shu & Ning (2012), is "crude": if the solution
   touches the floor it costs at least $O(h^2)$; if $\rho e \ge m > 2\epsilon_{\mathcal G}$
   it keeps high order. An explicit constant bounds the Liu–Osher scalar
   limiter (Lemma 7). Only the remainder state of the interior
   Gauss–Lobatto points is needed, and the DG volume quadrature points are
   added to the limited set (§§4.3, 5.2).
8. **Time stepping** (§5.3): SSP-RK3, trial step
   $\Delta t = \min\{a\,h/\alpha^*,\ b\,\mathrm{Re}\,h^2\}$ from the convective
   speed only (the viscous $\beta^{\mathrm v}$ blows up at shocks), halved and
   restarted whenever a stage average leaves the admissible set.
9. **No extra limiter for resolved viscous flow** (§§1.7, 6). Euler DG with
   only the positivity limiter becomes *more* oscillatory under refinement
   or higher degree, and oscillations can shift shocks. NS DG with only the
   positivity limiter becomes *less* oscillatory once the viscous scales
   are resolved. TVB-limited DG cannot run the Mach 10 corner problem
   without the positivity limiter and smears its Kelvin–Helmholtz roll-ups.

**Tests** (§6, $\gamma = 1.4$, $\mathrm{Pr} = 0.72$): accuracy of the viscous
flux in 1D and 2D (orders about $K+1$; identical to the central flux to
three digits); the limiter on a strong isentropic vortex (minimum density
$4.22\times10^{-3}$); Lax and double rarefaction; Sedov; Mach 5.09 shock
diffraction; Mach 10 double Mach reflection; Mach 10 reflection and
diffraction on a wedge with a sharp corner, on unstructured triangles.

# Notation map

| Zhang (2017) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf U$, $\mathbf u = (u, v, w)$ | $u$, $\mathbf v$ | the paper's $u$ is a velocity |
| $\mathbf F^a$, $\mathbf F^d$ | $\mathbf f$, $\mathbf f^{\mathrm v}$ | |
| $\boldsymbol\tau$, $\mathbf q$ | $\boldsymbol\tau$, $\mathbf q$ | |
| $\beta_i$, $\beta_{j+1/2}$ | $\beta^{\mathrm v}_{i+1/2}$ | registry $\beta_k$ is the smoothness indicator |
| $\alpha_{j+1/2}$ | $\alpha_{i+1/2}$ | |
| $G$, $G^\varepsilon$, $\varepsilon$ | $\mathcal G$, $\epsilon_{\mathcal G}$ | |
| $\hat\omega_\mu$, $\hat\omega$ | $\hat w_a$, $\hat w_1$ | |
| $k$ | $K$ | polynomial degree |
| $\theta_\rho$, $\theta_e$ | $\theta_\rho$, $\theta_e$ | |
| $\eta$, $\kappa$ (viscosity, conductivity) | (words) | collide with $\eta$ and $\kappa$ |

# Pages created or updated

* Updated [Positivity preservation](/properties/positivity-preserving.md): viscous flows.
* Updated [Zhang–Shu scaling limiter](/methods/positivity-preserving-scaling-limiter.md): the single-ratio factor, triangles, the restart.
* Updated [WENO limiters for DG](/methods/weno-limited-dg.md) and [SSP Runge–Kutta](/methods/ssp-runge-kutta.md).
* Updated [Sedov blast wave](/benchmarks/sedov-blast-wave.md), [Shock diffraction](/benchmarks/shock-diffraction.md), [Double Mach reflection](/benchmarks/double-mach-reflection.md), [Lax shock tube](/benchmarks/lax-shock-tube.md), [Double rarefaction](/benchmarks/double-rarefaction.md), [Isentropic vortex](/benchmarks/isentropic-vortex.md).
* Updated [Notation registry](/notation.md): $\mathbf f^{\mathrm v}$, $\boldsymbol\tau$, $\mathbf q$, $\beta^{\mathrm v}_{i+1/2}$, $\theta_e$.
* Also cited on [Step-size control for Runge–Kutta integration of hyperbolic problems](/methods/runge-kutta-step-size-control.md).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2017-JCP-Zhang-101016jjcp201610002.pdf` (author's revised preprint from the Purdue page, "Submitted on 05/21/2016; Revised on 09/11/2016", no arXiv id; doi:10.1016/j.jcp.2016.10.002 checked on Crossref: J. Comput. Phys. 328:301–343, January 2017): text extraction, all sections; eqs. 5–12, 25–26, 31–33, 37, 41–42, Lemma 6 and Tables 1–3 read from the page images. Figures read from captions. Reference list: 54 entries.
