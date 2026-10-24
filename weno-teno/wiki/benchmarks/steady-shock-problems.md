---
type: Benchmark
title: "Steady shock problems"
description: "Steady Euler problems whose solution contains fixed shocks: a 1D stationary shock, oblique shocks, regular reflection, plate and shock-interaction flows run to a steady residual, and a perturbed planar normal shock whose growth rate tests multidimensional shock stability; they measure residual convergence to machine zero and carbuncle-type instability of high-order schemes."
status: established
aliases: [steady shock tests, stationary shock, steady normal shock, regular shock reflection, oblique shock reflection, steady-state convergence tests, planar steady normal shock]
tags: [benchmark, teno, weno, riemann-solver, finite-volume, carbuncle]
timestamp: 2026-10-23T20:30:00Z
---

# Steady shock problems

A steady shock problem is an Euler flow whose exact solution is time-independent and contains
one or more shocks at fixed positions. The sources run such problems for two different
purposes. The first is **convergence to steady state**: a scheme is marched in time from a
uniform or a piecewise-constant start until the residual stops falling, and the level at which it
stalls (round-off, about $10^{-13}$, or a truncation-error level much above it) measures whether
the nonlinear reconstruction keeps switching at the shocks. The second is **shock stability**: a
planar normal shock that is an exact steady solution is perturbed at round-off level, and the
growth or decay of the perturbation shows whether the scheme develops the
[carbuncle phenomenon](/definitions/carbuncle-phenomenon.md). Both lines of work place the cause
in the reconstruction at the shock: Liang & Fu (2026) in the time variation of the reconstruction
formula at fixed interfaces, Ren et al. (2025) in the WENO weights inside the numerical shock
structure, none of which vanishes there.

## One-dimensional stationary shock

[Wan & Xia (2022)](/sources/wan-2022.md) Ex. 4.1 and [Liang & Fu (2026)](/sources/liang-2026.md)
§5.1, Eq. (34) print the same data: a Mach $M_\infty=2$ shock at rest in the middle of the domain,
$\gamma=1.4$, with the left state $(p,\rho,v)=\big(1/(\gamma M_\infty^2),\,1,\,1\big)$ and the
right state

$$
\begin{aligned}
p_r&=p_l\,\frac{2\gamma M_\infty^2-(\gamma-1)}{\gamma+1},\qquad
\rho_r=\frac{\frac{\gamma+1}{\gamma-1}\frac{p_r}{p_l}+1}{\frac{\gamma+1}{\gamma-1}+\frac{p_r}{p_l}},\\
v_r&=\sqrt{\gamma\,\frac{\big(2+(\gamma-1)M_\infty^2\big)p_r}{\big(2\gamma M_\infty^2+(1-\gamma)\big)\rho_r}}
\end{aligned}
$$

(page-local subscripts $l$, $r$). Wan & Xia solve $\partial_xf(u)=0$ on $[-1,1]$ with the shock at
$x=0$ on 400 points; Liang & Fu march the 1D Euler equations on $[0,1]$ with the shock at $x=0.5$ to
$t=12$, on an adaptive grid whose finest level has 512 cells. These are the Rankine–Hugoniot
jump relations: $p_r/p_l=4.5$, $\rho_r=8/3$ and $v_r=0.375=1/\rho_r$, so the mass flux is
continuous *(compiler check, not in the sources)*.

All schemes of both papers reach a residual near machine zero on this problem: fifth-order
finite-difference WENO-H, CWENOZ and MRWENO in Wan & Xia, with WENO-H the least oscillatory, and
finite-volume WENO5-Z, TENO5 and [CENO](/methods/converged-eno.md) in Liang & Fu, CENO-AMR with
the lowest residual throughout (Fig. 5). In one dimension the stall is therefore not observed.

## Two-dimensional steady shock flows

**Regular shock reflection.** An oblique shock enters at the top of $[0,4]\times[0,1]$ and
reflects from the solid bottom wall: initial and left state $(\rho,v_1,v_2,p)=(1,2.9,0,1/1.4)$,
the post-shock state $(1.69997,2.61934,-0.50632,1.52819)$ imposed on the top boundary, a
reflective bottom and supersonic outflow on the right. Three sources print these data:

| Source | Grid | Scheme | Steady residual |
|---|---|---|---|
| [Wan & Xia (2022)](/sources/wan-2022.md) Ex. 4.4 | $120\times30$ | fifth-order finite-difference WENO-H vs CWENOZ, MRWENO | with the global Lax–Friedrichs speed $\max(\lvert v\rvert+c)$ only WENO-H reaches about $10^{-12}$; with per-field speeds all three do; CWENOZ and MRWENO show oscillations (Figs. 4.4–4.6) |
| [Duan, Barsukow & Klingenberg (2025)](/sources/duan-2025.md) Example D.5 | $120\times30$, $T=6$ | bound-preserving generalized [Active Flux](/methods/active-flux.md) with [flux vector splitting](/methods/flux-vector-splitting.md) | the shock-sensor flux limiting ($\kappa_{\mathrm s}=0.5$ against 0) accelerates the residual decay once the reflected shock has formed (Fig. 24; arXiv v3) |
| [Liang & Fu (2026)](/sources/liang-2026.md) §5.3 | finest $2048\times512$ (adaptive), against uniform $512\times128$ and $2048\times512$, $t=12$ | finite-volume CENO-AMR vs WENO5-Z, TENO5 | CENO-AMR close to machine zero, without the post-shock oscillations of WENO5-Z and TENO5 (Figs. 11–15) |

Duan et al.'s strength $\kappa_{\mathrm s}$ (page-local) scales the exponent of their shock-sensor
factor $\exp(-\kappa_{\mathrm s}\varphi_{\mathrm J}\Psi_{\mathrm D})$, which blends the limited flux
toward Lax–Friedrichs; $\varphi_{\mathrm J}$ (page-local, the source's $\varphi_1$) is a Jameson
pressure sensor and $\Psi_{\mathrm D}$ (the source's $\varphi_2$) the modified, compression-only
Ducros sensor of the [Ducros shock sensor](/definitions/ducros-shock-sensor.md) page.

**Further configurations of Liang & Fu.** Liang & Fu (2026) §§5.2–5.7 run five more steady flows,
all with $\gamma=1.4$, HLLC, SSP-RK2 with local time stepping at CFL 0.4:

- *Oblique steady shock* (§5.2, after Zhang & Shu as they cite it): on $[0,6]\times[0,3]$ a Mach 4
  shock through $(0.5,3)$ at $30^\circ$ to the $x$-axis, the state $(1,4,0,1/1.4)$ ahead and
  $(2.6667,3.3750,-1.0825,3.2143)$ behind it on the top boundary, outflow on the right and bottom,
  to $t=40$, finest $1024\times512$. The normal Mach number is $4\sin30^\circ=2$, and the
  Rankine–Hugoniot state of that normal shock, with the tangential velocity $4\cos30^\circ$ kept,
  is the printed downstream state *(compiler check, not in the sources)*.
- *Supersonic flow past a long plate* (§5.4): $[0,4]\times[0,2]$, a Mach 3 stream at an angle of
  attack of $25^\circ$, a reflecting plate on $1\le x\le4$ of the bottom, to $t=80$, finest
  $1024\times512$; an oblique shock leaves the plate's leading edge.
- *Heterolateral shock interaction* (§5.5): the oblique-shock data entering from both the top and
  the bottom of $[0,6]\times[0,3]$, with the bottom post-shock state $v_2=+1.0825$, so that the two
  shocks cross, to $t=20$.
- *Ipsilateral shock interaction* (§5.6): $[0,4]\times[0,2]$, a Mach 3 stream at $20^\circ$, a
  reflecting wall on $0.5<x<2$ of the bottom and a Dirichlet state beyond, snapshots to $t=80$;
  the flow carries contacts and small-scale instabilities.
- *Multiple shock reflection* (§5.7): $[0,8]\times[0,1]$ with slip walls, a shocked inflow
  $(2.6667,1.6533,0,3.2143)$ into $(1,2.6108,0,1/1.4)$, snapshots at $t=2.5$, $4.0$ and $40$, finest
  $4096\times512$.

The heterolateral, ipsilateral and multiple-reflection data are taken from the authors'
finite-difference CENO paper, as they cite it.

## Planar steady normal shock: a stability test

[Ren et al. (2025)](/sources/ren-2025.md) §3.2, Eqs. (34)–(36), after Dumbser, Moschetta &
Gressier and their own earlier work as they cite them, place a planar normal shock across an
$11\times11$ Cartesian grid: upstream state $(\rho,v_1,v_2)=(1,1,0)$ with the pressure set by the
upstream Mach number $M_0$, the downstream state from the Rankine–Hugoniot density and pressure
ratios, and a single intermediate state in the shock structure, in column $i=6$, which lies on the
Hugoniot curve between the two. Its position $\varepsilon_{\mathrm s}\in[0,1]$ (page-local, the
source's $\varepsilon$; $\varepsilon_{\mathrm s}\to1$ is close to the downstream state) sets the
intermediate density as $(1-\varepsilon_{\mathrm s})\rho_l+\varepsilon_{\mathrm s}\rho_r$ and the
velocity and pressure by their Eq. (36). The default case is $M_0=20$, $\varepsilon_{\mathrm s}=0.1$;
the mean flow is perturbed by $10^{-7}$, integrated by TVD-RK3 at CFL 0.1, and the transverse
velocity $\lVert v_2\rVert_\infty$, zero in the exact solution, is the diagnostic, growing
exponentially in an unstable run. The boundary conditions are deferred to their earlier paper,
and $\gamma$ is not printed for this test.

The problem is the test case of their
[matrix stability analysis](/methods/matrix-stability-analysis.md) for fifth-order finite-volume
[WENO-Z](/methods/weno-z.md) and the reference of its validation: on the Roe case at
$\varepsilon_{\mathrm s}=0$ the measured growth rate $2.17904$ is matched to 0.59 % by the analysis
with a smoothed eigenvalue modulus (Table 1). Their findings on this grid (§4):

- With mid-point and with two-point Gauss flux integration the stable/unstable verdicts agree for
  every $\varepsilon_{\mathrm s}\in\{0,0.1,\dots,1\}$: Roe is stable only at $\varepsilon_{\mathrm s}=0.8$
  and $0.9$, HLL only at $0.6$ and $0.7$ (Table 2, Fig. 8). They conclude that the computation tends
  to be more stable when the intermediate state is closer to the downstream state (§6).
- At fifth order the Roe and HLLC runs are unstable; the Roe run at $\varepsilon_{\mathrm s}=0.1$
  collapses at $t=47.8$ with mid-point integration and at $t=42.2$ with Gauss integration, whose
  growth rate is lower (Fig. 13). HLL and van Leer
  [flux vector splitting](/methods/flux-vector-splitting.md), stable at first and second order,
  are unstable at fifth order, and so are three fluxes designed to be shock-stable at
  low order: HLLC-ADC, hybrid SLAU and HLLC-EC (Figs. 11–12, 16–19).
- Inside the shock structure every three-point candidate of WENO contains the discontinuity, so
  no weight vanishes; only zeroth-degree (first-order) reconstruction on the faces of the shock
  structure is stable (Figs. 21–22, Table 3).

Their remedy, MR-WENO-SD (a multi-resolution WENO whose weights come from a pressure-jump and
Mach-number shock-detection function and fall to the cell average in the shock structure) with a
hybrid HLLC/HLL flux, has all eigenvalues in the left half-plane on a $50\times25$ version of the
same shock at $M_0=20$, $\varepsilon_{\mathrm s}=0.1$, and a stable density contour (§5.2.2, Fig. 35);
see [multi-resolution WENO](/methods/multi-resolution-weno.md) and the
[carbuncle phenomenon](/definitions/carbuncle-phenomenon.md), where the analysis is set against
earlier accounts of shock instability.

## Findings across sources

**Where the residual stalls.** In one dimension all the schemes of Wan & Xia and of Liang & Fu
converge. In two dimensions the sources report stalls of their baseline high-order schemes: on the
regular reflection, CWENOZ and MRWENO with the global Lax–Friedrichs speed (Wan & Xia), WENO5-Z
and TENO5 with post-shock oscillations (Liang & Fu); on the heterolateral interaction WENO5-Z and
TENO5 stall "around $O(1)$" and on the ipsilateral one "around $10^{-1}$", while CENO-AMR reaches
"around $10^{-13}$" and machine-zero level respectively (Liang & Fu, Figs. 19–24). Wan & Xia's
remedy is a three-region hybrid detector with a smooth transition between linear and nonlinear
reconstruction; Liang & Fu's is the hysteresis of CENO's stencil selection; Duan et al.'s is the
smooth shock-sensor factor. Each source tests only its own remedy against its own baselines, so the
three remedies are not compared with one another.

**Competing explanations of the stall.** Liang & Fu (2026, §1, §3.2.3), following their
finite-difference paper, attribute non-convergence to the time variation of the reconstruction
formula at a fixed interface. Of the remedies that target slight post-shock oscillations they
state that the residual of Zhang & Shu's smoothness indicator and of Zhang, Jiang & Shu's
upwind-biased eigenvectors is "difficult to reduce to near machine zero when encountering strong
shocks passing through the boundaries" (§1), and that the solutions of such schemes, among them
Wan & Xia's as they cite it, "still can not converge to a steady state straightforwardly for some
two-dimensional steady-state problems with shock interactions and reflections" (§3.2.3). Wan & Xia report
round-off residues for their WENO-H on every one of their fourteen steady benchmarks, which include
the regular reflection but not the interaction problems of Liang & Fu. The two papers run no common
problem with both schemes, so the claim and the counter-evidence do not meet on one test.

**Adaptive meshes and cost.** Liang & Fu's adaptation criterion freezes the mesh inside a buffer band
of a discontinuity-detecting variable built from the smoothness indicators, with refine and coarsen
thresholds $0.3$ and $0.7$, because an adaptive mesh that keeps refining at steady state changes the
reconstruction formula as well (§3.3). Data compression exceeds 90 % (85 % on the heterolateral
case), and the results are "not very sensitive" to five threshold pairs (Figs. 9–10). Against
uniform-mesh WENO5-Z at the finest effective resolution, the user CPU time ratio of CENO-AMR is
0.408 (1D), 0.277 (oblique shock), 0.252 (regular reflection), 0.163 (plate), 0.528
(heterolateral) and 0.425 (ipsilateral), TENO5 costing 1.003 to 1.412 times WENO5-Z (Table 1); no
hardware is printed.

**Order of the steady schemes.** Liang & Fu's multi-dimensional finite-volume scheme uses the
mid-point flux rule and is second order overall, fifth order only in 1D, as they state (§4.1); Ren et
al.'s analysed fifth-order scheme also uses the mid-point rule, which they call second order for
nonlinear smooth problems, and they transfer their verdicts to Gauss integration through the
agreement of Table 2 on one problem.

## Qualifications

- Liang & Fu (2026) print no residual values in the text for most cases (the figures carry them),
  and the stall levels of WENO5-Z and TENO5 refer to their finite-volume implementation with HLLC
  and the mid-point rule.
- Ren et al.'s §4.4 states that §§4.1–4.3 reconstruct primitive variables, while their §2.2 and
  §3.1 present the reconstruction and the analysis in conservative variables; which variables the
  normal-shock results use is ambiguous as printed.
- The normal-shock test isolates multidimensional shock instability on a tiny grid; its verdicts
  are confirmed by the authors on a Mach 20 blunt body (see
  [flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)), not on the steady
  convergence problems above.
- Duan et al. are read as arXiv v3; Example D.5 and Fig. 24 are locators of that version.

# Citations

- [Wan & Xia (2022)](/sources/wan-2022.md) — Ex. 4.1, Ex. 4.4, Figs. 4.4–4.6.
- [Liang & Fu (2026)](/sources/liang-2026.md) — §1, §3.2.3, §3.3, §4.1, §§5.1–5.8, Eq. (34), Table 1, Figs. 5–26.
- [Ren et al. (2025)](/sources/ren-2025.md) — §§3.2–3.4, §4, §5.2.2, §6, Eqs. (34)–(36), Tables 1–3, Figs. 8–13, 21–22, 35.
- [Duan, Barsukow & Klingenberg (2025)](/sources/duan-2025.md) — §4.1.3, Example D.5, Fig. 24 (arXiv v3).
