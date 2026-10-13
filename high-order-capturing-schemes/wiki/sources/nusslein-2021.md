---
type: Source
title: "Nüßlein, Ranocha & Ketcheson (2021) — Positivity-preserving adaptive Runge–Kutta methods"
description: "Makes the output of a Runge–Kutta step nonnegative by solving, after the stages, a linear program for weights closest in ℓ1 to the original ones under the bounds and the order conditions up to a reduced order; keeps all linear invariants, proves a stability-region inclusion for convex weight combinations, and finds the approach useful mainly with implicit methods."
resource: "doi:10.2140/camcos.2021.16.155"
source_kind: paper
authors: [Nüßlein S., Ranocha H., Ketcheson D.I.]
year: 2021
venue: "Commun. Appl. Math. Comput. Sci. 16:155–179"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2021-CAMCoS-Nusslein-102140camcos202116155.pdf"
tags: [time-discretization, runge-kutta, positivity]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

Once the stages of a Runge–Kutta step are computed, the update and the
order conditions are linear in the weights. The paper chooses new
weights by a linear program: as close as possible in $\ell_1$ to the
original weights, subject to a nonnegative (or box-bounded) output and
the order conditions up to a possibly reduced order. Every adapted step
is still a Runge–Kutta step, so every linear invariant is kept.
Projection by clipping breaks mass conservation. The tests are ODEs and
first- or second-order semi-discretized linear PDEs. The authors
conclude the method pays off mainly with diagonally implicit or
extrapolation methods. Merged into
[positivity-preserving adaptive Runge–Kutta](/methods/positivity-preserving-adaptive-runge-kutta.md).

# Key claims

1. **Target** (§§1–2, eqs. 1.3–1.4, 2.5–2.7): $u^n \ge 0 \Rightarrow u^{n+1} \ge 0$
   componentwise, or box bounds. Only the step output is constrained;
   stages may be negative (§5.1).
2. **Background** (§1): unconditionally positive Runge–Kutta or general
   linear methods are at most first order (Bolley & Crouzeix, cited); SSP
   methods are positive for $\Delta t \le \mathcal C\Delta t_{\mathrm{FE}}$.
3. **Free and convex adaptation** (§3.2, LPs 3.1–3.2). The $\ell_1$
   objective keeps the designed stability and error properties and
   penalizes large weights.
4. **Degrees of freedom** (§§3.1, 4.1, Tables 1–2): adaptation needs free
   weights, in effect $\tilde p_{\mathrm t} < s$ (§3.1 prints "$\le s$").
   RK4 has none at order 3; SSP-RK(10,4) has four at order 4; Cash–Karp
   and Dormand–Prince must drop order.
5. **Active set and algorithm** (§§3.3–3.4): constraints only on
   components that go negative; at most two iterations in the tests; if
   no order works, the step is reduced.
6. **Error estimate** (§4.2, eqs. 4.1–4.2): the weight perturbation is
   added to the embedded estimate; a PI controller from Hairer and Wanner
   (parameters not printed).
7. **Stability** (§4.3): Theorem 4.1 (a convex combination of weight
   vectors keeps the intersection of their stability regions) and
   Lemma 4.2 (the stability function moves by at most
   $\Vert\tilde{\mathsf b} - \mathsf b\Vert_1$ times a bounded factor). LP
   feasibility for explicit methods and convergence are not proved.
8. **Conclusion** (§6): for explicit methods the useful step window is
   narrow; the method is "mainly interesting for diagonally implicit
   methods".

**Tests:** a linear 2×2 system where SSP(3,3) at $\Delta t = 1/3$ goes
negative (§2.1); a four-species production–destruction system with
Cash–Karp (§2.2); advection with decay, first-order upwind, Dormand–Prince,
useful window $0.0082 < \Delta t \le 0.016$ (§5.1); the heat equation with
backward-Euler extrapolation (§5.2); advection–diffusion–reaction with
adaptive steps, 264 steps of which 72 adapted (§5.3); stratospheric
chemistry, 249 steps, 2 rejected, invariants to round-off (§5.4). None is
an Euler test.

# Notation map

| Nüßlein et al. (2021) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $f(t, u)$, $f_j$, $F$ | $\mathcal L(u)$, $\mathcal L(Y_j)$; words | $f$ is the flux in the registry |
| $A$, $b$, $c$, $\hat b$, $\tilde b$ | $\mathsf a_{ij}$, $\mathsf b$, $\mathsf c$, $\hat{\mathsf b}$, $\tilde{\mathsf b}$ | $A$ is the flux Jacobian |
| $y_j$ | $Y_j$ | |
| $p$, $\tilde p$ | $p_{\mathrm t}$, $\tilde p_{\mathrm t}$ | $p$ is the pressure |
| $R(z)$ | $R_{\mathrm{st}}(z)$ | |
| $\alpha$, $\beta$ (bounds) | words | collide with $\alpha$, $\beta_k$ |
| $Q_{\tilde p}$, $r_{\tilde p}$, $h$ (active set), $B$, $g$ | words | collide with $r$, $h$, $\mathbf B$ |

# Pages created or updated

* Created [Positivity-preserving adaptive Runge–Kutta](/methods/positivity-preserving-adaptive-runge-kutta.md).
* Updated [Explicit Runge–Kutta methods](/methods/explicit-runge-kutta.md) (stability function; weight modification), [Relaxation Runge–Kutta](/methods/relaxation-runge-kutta.md), [Step-size control](/methods/runge-kutta-step-size-control.md), [Positivity preservation](/properties/positivity-preserving.md), [SSP Runge–Kutta](/methods/ssp-runge-kutta.md), [SSP order barriers](/results/ssp-order-barriers.md) (positivity barrier, second-hand).
* Updated [Notation registry](/notation.md): $\tilde{\mathsf b}$, $\tilde p_{\mathrm t}$.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2021-CAMCoS-Nusslein-102140camcos202116155.pdf`.
   * **Version.** arXiv:2005.06268v2 (30 April 2021), 21 pages, not the
     typeset article.
   * **Identity.** doi:10.2140/camcos.2021.16.155, checked on Crossref:
     Commun. Appl. Math. Comput. Sci. 16(2):155–179, 2021.
   * **How it was read.** Text extraction, all sections; pp. 4–6 checked on
     the page images. Figure values (Figs. 3, 7, 9) are axis or legend
     labels.
   * **Recorded as printed.** "$\tilde p \le s$" in §3.1 against
     "$\tilde p < s$" in §§4.1, 6; eq. 3.3 sums from $j = 0$; the sign of
     $0.003u_4$ in eq. 2.14d differs from eq. 5.5d.
   * **Reference list:** 32 entries. Ref. 23, the authors' reproducibility
     repository, is keyed `nusslein-2020`.
