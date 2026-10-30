---
type: Benchmark
title: "Steady shock problems"
description: "Euler problems with fixed shocks (1D stationary shock, quasi-1D nozzles, oblique shocks, regular reflection, plate and shock-interaction flows run to a steady residual, a perturbed planar normal shock), with slowly moving and single strong shocks as relatives; they measure steady convergence, carbuncle-type instability and post-shock errors of high-order schemes."
status: established
aliases: [steady shock tests, stationary shock, steady normal shock, regular shock reflection, oblique shock reflection, steady-state convergence tests, planar steady normal shock, quasi-one-dimensional nozzle flow, quasi-1D nozzle]
tags: [benchmark, teno, weno, riemann-solver, finite-volume, carbuncle]
timestamp: 2026-10-30T08:08:00Z
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

## Quasi-one-dimensional nozzle flow

Two founding sources of the bundle compute a standing shock inside a nozzle of variable cross-section
$A(x)$: the one-dimensional Euler equations with a geometric source term, marched in time to the
steady state.

**Harten (1983a).** [Harten (1983a)](/sources/harten-1983.md) §8 (II), Eq. (8.7a), writes the
cross-section average of the flow in an axisymmetric nozzle as
$\partial_tw+\partial_xf(w)=-s(w,x)$ with $s=\big(0,\ p\,\tfrac{dA}{dx},\ 0\big)^\top$, "where $w$,
$f(w)$ and $p$ are given in (7.1)" (the Euler variables of the report), and runs two nozzles:

- a **divergent nozzle**, $A(x)=1.398+0.347\tanh(0.8x-4)$ (Eq. (8.7b)), supersonic at the
  entrance and subsonic at the exit: steady states on a crude mesh with Roe's first-order scheme
  (Fig. 4a) and with ULT1 (Fig. 4b), and with ULT1 on a finer mesh (Fig. 5);
- a **convergent–divergent nozzle**,
  $$A(x)=\begin{cases}1+(A_0-1)(1-x/5)^2, & x\le5,\\ 1+(A_E-1)\big[(x-5)/(x_E-5)\big]^2, & x>5,\end{cases}$$
  (Eq. (8.7c)), $A_0$ and $A_E$ the entrance and exit areas, subsonic at both ends: ULT1 (Fig. 6).

ULT1 is the second-order [TVD scheme](/methods/harten-tvd-scheme.md) of the report with the
numerical-viscosity function $Q(x)=\lvert x\rvert$ (Eq. (8.3a)). The values of $A_0$, $A_E$ and
$x_E$, the meshes, $\gamma$ and the residual histories are not printed; the figures are credited to
H. C. Yee, and the report hopes that "a detailed report of these calculations and the particular
approach to steady state will be published elsewhere".

**Jiang & Shu (1996).** [Jiang & Shu (1996)](/sources/jiang-1996.md) §8.2 Ex. 4 add to the 1D
Euler equations the forcing term

$$
S(u)=-\frac{A'(x)}{A(x)}\big(\rho v,\ \rho v^2,\ v(E+p)\big)^\top .
$$

The nozzle has unit length, and its shape is determined "by assuming a linear, isentropic Mach
number distribution, which is 0.8 at $x=0$ (the entrance) and 1.8 at $x=1$ (the exit)"; the exit
condition is set by the prescribed shock position $x=0.5$. With 34 points and third-order TVD
Runge–Kutta, finite-difference WENO-Roe-4 and WENO-Roe-5 "converge nicely to the exact solution"
(Fig. 8), and the residue "settles down to $10^{-7}$ for this grid, and to a smaller number for a
finer grid". The authors conclude that "WENO has its advantage for steady state calculations" and
credit it (§1) to the WENO flux being smoother than the ENO flux. $\gamma$ is not printed anywhere in
the paper.

The two sources write the quasi-one-dimensional equations in different forms (Harten as a momentum
source acting on cross-section averages, Jiang & Shu as a source proportional to $A'/A$ in all
three equations), and neither relates its form to the other's.

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

## Moving single-shock relatives

Two later sources run a single one-dimensional shock that moves, not
a steady one; they test what a steady shock tests, the behaviour of the
scheme in and behind a captured shock, under a strong pressure jump or
across mesh interfaces.

**Slowly moving shocks across AMR interfaces.**
[Wang et al. (2026)](/sources/wang-2026.md) §6.2 run two shocks moving
to the right at speed $0.01$ through a two-level
[AMR](/methods/adaptive-mesh-refinement.md) grid on which thin refined
sheets of width $1/10$ produce seven coarse–fine interfaces (base
$N=64$, ratio 2), against a uniform $N=512$ reference, with the exact
states imposed at the boundaries:

| Case | Behind the shock $(\rho,v,p)$ | Ahead $(\rho,v,p)$ | Initial position | End |
|---|---|---|---|---|
| Mach 2 (Fig. 11) | $(2.6667,\,-0.8774,\,4.5)$ | $(1.0,\,-2.3564,\,1.0)$ | $x=0.05$ | $t=90$, shock at $x=0.95$ |
| Mach 3 (Fig. 12, Table 5) | $(3.86,\,-0.91,\,10.33)$ | $(1.0,\,-3.54,\,1.0)$ | $x=0.37$ | $t=30$, shock at $x=0.67$ |

In the frame of the shock both are steady normal shocks of Mach 2 and
3 with $\gamma=1.4$, to the printed digits *(compiler check, not in the
sources)*, so the problem is a steady shock seen from a moving frame,
which forces the shock through every interface. On the Mach 3 case the
pure WENO inter-level interpolation without flux correction distorts
at the first interface, with flux correction it oscillates by $t=10$,
and both fail later, while AMR-HybridWENO, which uses conservative
linear interpolation in cells flagged by a Roe-averaged Lax wave-speed
criterion and a pressure-curvature sensor, keeps a sharp shock to
$t=30$ (Fig. 12). The shock-position error $0.001791$ and post-shock
overshoot $0.001609$ do not change over the tested thresholds
$\alpha_{\mathrm{Liu}}\in\{0.05,0.1,0.2\}$ and
$\theta_{\mathrm{map}}\in\{10^{-3},10^{-2},10^{-1}\}$ (their symbols,
page-local), the share of troubled cells falling from 6.25 % to
4.6875 % (Table 5). The authors trace the failure to Appendix C of
their paper: non-conservative transfers break the discrete
[Rankine–Hugoniot](/definitions/rankine-hugoniot-condition.md) balance
and perturb the shock speed by $\mathcal O(\Delta x)$, which accumulates
into a drift for slowly moving shocks; see
[local conservation](/results/local-conservation-flux-form.md).

**A single strong shock.** [Cao et al. (2026)](/sources/cao-2026.md)
Ex. 6.6, after a published comparison of DG limiters, put
$(\rho,v,p)=(1,0,1)$ for $x\le0$ against
$\big(\tfrac{1+6\eta_{\mathrm p}}{\eta_{\mathrm p}+6},\ \tfrac{1-\eta_{\mathrm p}}{\sqrt{1.2\eta_{\mathrm p}+0.2}},\ \eta_{\mathrm p}\big)$
for $x>0$ on $[-50,50]$ with the pressure ratio $\eta_{\mathrm p}=10^5$
($\eta_{\mathrm p}$ page-local, not the entropy), $\gamma=1.4$, 1000 cells, $t=0.1$, zoom on $[-37,-32]$.
The right state is the Rankine–Hugoniot state behind a shock of
pressure ratio $\eta_{\mathrm p}$ running to the left into gas at rest, with density
ratio about 6 and shock speed about $346$, which puts the shock near
$x=-34.6$ at $t=0.1$, inside the zoom *(compiler check, not in the
sources)*. Third-order local [COS(DG)](/methods/cos-dg.md) gives the
sharpest non-oscillatory profile among ten DG techniques, the TVB
limiter being run with the tuned $M=20$ (Fig. 6).

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
- Wang et al. (2026) write that the WENO run without flux correction distorts "as soon as the
  shock passes through the first interface at approximately $x=4.7$" on the domain $[0,1]$; the
  printed position cannot be on their grid *(compiler check, not in the sources)*.

# Citations

- [Wan & Xia (2022)](/sources/wan-2022.md) — Ex. 4.1, Ex. 4.4, Figs. 4.4–4.6.
- [Liang & Fu (2026)](/sources/liang-2026.md) — §1, §3.2.3, §3.3, §4.1, §§5.1–5.8, Eq. (34), Table 1, Figs. 5–26.
- [Ren et al. (2025)](/sources/ren-2025.md) — §§3.2–3.4, §4, §5.2.2, §6, Eqs. (34)–(36), Tables 1–3, Figs. 8–13, 21–22, 35.
- [Duan, Barsukow & Klingenberg (2025)](/sources/duan-2025.md) — §4.1.3, Example D.5, Fig. 24 (arXiv v3).
- [Wang et al. (2026)](/sources/wang-2026.md) — §6.2, Figs. 11–12, Table 5; Appendix C.
- [Cao et al. (2026)](/sources/cao-2026.md) — Ex. 6.6, Fig. 6.
- [Harten (1983a)](/sources/harten-1983.md) — §8 (II), Eqs. (8.3a), (8.7a)–(8.7c), Figs. 4–6 (NYU report DOE/ER/03077-175, March 1982).
- [Jiang & Shu (1996)](/sources/jiang-1996.md) — §1, §8.2 Ex. 4, Fig. 8 (author preprint).
