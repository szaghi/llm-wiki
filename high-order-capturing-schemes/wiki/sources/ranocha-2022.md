---
type: Source
title: "Ranocha, Dalcin, Parsani & Ketcheson (2022) — Optimized Runge–Kutta methods with automatic step size control for compressible computational fluid dynamics"
description: "Replaces CFL-based step selection by embedded-pair error control with PID controllers tuned for step-size-control stability at the linear stability limit; tunes controllers for existing pairs, builds six low-storage 3S*₊ pairs, and finds error control about 50% cheaper than CFL control at ν = 1 and robust without tuning on entropy-stable DG flows."
resource: "doi:10.1007/s42967-021-00159-w"
source_kind: paper
authors: [Ranocha H., Dalcin L., Parsani M., Ketcheson D.I.]
year: 2022
venue: "Commun. Appl. Math. Comput. 4:1191–1228"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2022-CAMC-Ranocha-101007s42967-021-00159-w.pdf"
tags: [time-discretization, runge-kutta, step-size-control, low-storage]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

Compressible-flow runs with explicit Runge–Kutta methods are usually
stability-limited, and the step is usually set by a hand-tuned CFL
number. The paper replaces that by an embedded error estimate and a PID
controller. Its central point is that at the stability limit the
controller must be designed with the pair, for step-size-control
stability. It tunes controllers for general-purpose, SSP and low-storage
pairs, and adds new embedded methods to the 3S\*₊ low-storage methods of
Parsani, Ketcheson and Deconinck. All tests use entropy-dissipative
nodal DG with the SBP property and no shock capturing. Merged into
[step-size control](/methods/runge-kutta-step-size-control.md) and
[low-storage Runge–Kutta](/methods/low-storage-runge-kutta.md).

# Key claims

1. **Pairs and FSAL** (§2, eqs. 2–4, Remark 2): naming
   NAME$p_{\mathrm t}(\hat p_{\mathrm t})s$, with $s$ the effective number
   of evaluations and F for FSAL.
2. **Storage** (§2.1, Algorithms 1–2): 3S\* (three registers including an
   error estimate) and 3S\*₊ (one more for the embedded solution); three
   registers is the minimum with error estimation and rejection.
3. **Controller** (§2.2, eqs. 6–7): weighted RMS error with
   $\mathtt{atol} = \mathtt{rtol} = \mathtt{tol}$; PID form with
   $k_{\mathrm c} = \min(p_{\mathrm t}, \hat p_{\mathrm t}) + 1$; accept if the
   step factor is $\ge 0.92$. A step with negative density or pressure is
   rejected and retried with $\Delta t/4$; there is no limiter.
4. **CFL control** (§3, eqs. 8–9): $\nu$ normalized so that a real
   stability interval of 2 is $\nu = 1$. An untuned PI controller matches
   a tuned CFL controller over $\mathtt{tol} \in [10^{-5}, 10^{-3}]$ (Figs. 2–3).
5. **Step-size-control stability** (§4, eqs. 10–11, Table 2): BS5(4)7F with
   PI34, 5 015 evaluations and 132 rejections; tuned $(0.28, -0.23, 0)$,
   4 119 and none.
6. **Tuning** (§5.4): brute-force search over control-stable
   $\beta^{\mathrm c}$; good controllers within about 5 % of the best.
7. **Existing pairs** (§5.5): BS3(2)3F about 50 % more efficient than the
   fifth-order pairs when stability-limited; SSP3(2)4[3S\*₊] about 50 %
   better than SSP3(2)3 or BS3(2)3F on the Taylor–Green vortex but
   unreliable at tight tolerances; the 2R Kennedy–Carpenter–Lewis pairs
   lose almost everywhere. No PID controller tested is control-stable
   with the existing embedded method of SSP4(3)10 (§5).
8. **New pairs** (§6, Tables 6, 11, B1–B6): RK3(2)5, RK4(3)9 and RK5(4)10
   in 3S\*₊, each with a FSAL variant and its own controller. Not SSP.
   Third-order ones up to 18 % better than BS3(2)3F. The embedded
   stability region is made to contain the main one.
9. **Large runs** (§7, Tables 7–10): error control at $\mathtt{tol} = 10^{-8}$
   needs about 50 % fewer evaluations than CFL control at $\nu = 1$ on a
   wing–body juncture flow and a front wing; CFL control crashed
   SSP3(2)4 at $\nu = 1$ (Table 10).
10. **Recommendations** (§8): $\mathtt{tol} \approx 10^{-8}$;
    SSP3(2)4[3S\*₊] or RK3(2)5F[3S\*₊]; design method, estimator and
    controller together; optimize the controller rather than shrink the
    step to fix control instability.

**Tests:** 2D linear advection; inviscid Taylor–Green vortex (Mach 0.1);
3D [isentropic vortex](/benchmarks/isentropic-vortex.md) (Mach 0.5,
strength 5, axis $(1,1,0)$); a smooth 1D flow with a periodic energy
source; a Navier–Stokes viscous shock (Mach 2.5, Re 10); the NASA
juncture flow; the Imperial front wing.

# Notation map

| Ranocha et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $f(t, u)$ | $\mathcal L(u)$ | $f$ is the flux in the registry |
| $A$, $b$, $c$, $\hat b$ | $\mathsf a_{ij}$, $\mathsf b$, $\mathsf c$, $\hat{\mathsf b}$ | |
| $q$, $\hat q$ | $p_{\mathrm t}$, $\hat p_{\mathrm t}$ | $q$ is the weight power |
| $w_{n+1}$, $\varepsilon_{n+1} = 1/w_{n+1}$ | $\mathrm{err}^{n+1}$ | $\varepsilon$ is the weight regularization |
| $\beta_1, \beta_2, \beta_3$, $k$ | $\beta^{\mathrm c}_{1,2,3}$, $k_{\mathrm c}$ | $\beta_k$ are smoothness indicators |
| $R(z)$, $E(z)$, $J(z)$ | $R_{\mathrm{st}}(z)$; words | $R$ is the eigenvector matrix |
| $m$ (unknowns) | $N$ (words) | registry $m$ is the system size |
| $p$ (polynomial degree) | $K$ | |
| $S_j$, $\gamma_{1,i}$, $\gamma_{2,i}$, $\gamma_{3,i}$, $\beta_i$, $\delta_i$ | words | 3S\* coefficients; cite the tables |

# Pages created or updated

* Created [Step-size control](/methods/runge-kutta-step-size-control.md), [Low-storage Runge–Kutta](/methods/low-storage-runge-kutta.md).
* Updated [Explicit Runge–Kutta methods](/methods/explicit-runge-kutta.md) (pairs), [SSP Runge–Kutta](/methods/ssp-runge-kutta.md) (SSP pairs; SSP-RK(10,4) under error control), [Positivity preservation](/properties/positivity-preserving.md) (reject and retry), [Isentropic vortex](/benchmarks/isentropic-vortex.md).
* Updated [Notation registry](/notation.md): $\mathrm{err}^{n+1}$, $\mathtt{tol}$, $\beta^{\mathrm c}$, $k_{\mathrm c}$, $\hat{\mathsf b}$, $R_{\mathrm{st}}$.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2022-CAMC-Ranocha-101007s42967-021-00159-w.pdf`.
   * **Version.** Publisher PDF (open access), received 14 April 2021,
     online 22 November 2021.
   * **Identity.** doi:10.1007/s42967-021-00159-w, checked on Crossref:
     Commun. Appl. Math. Comput. 4(4):1191–1228, issue December 2022.
   * **How it was read.** Text extraction, all sections; eqs. 6, 11 and
     Algorithm 2 checked on the page images. The supplementary material
     (results for degrees 3, 4, 7) was not read. Coefficient tables
     B1–B6 are not transcribed.
   * **Recorded as printed.** In Algorithm 2 the embedded update evaluates
     $\mathcal L$ after the main update of the same register; reuse of
     one evaluation is implied, not printed.
   * **Reference list:** 80 entries, matching Crossref. Ref. 38 prints the
     year 2013 with a 2012 DOI suffix; ref. 35 (NASA TM 109112) prints
     the authors as Kennedy and Carpenter and is merged as
     `carpenter-1994`.
