---
type: Benchmark
title: "FitzHugh–Nagumo model"
description: "The FitzHugh–Nagumo reaction–diffusion system of nerve conduction, a stiff method-of-lines test with a cubic excitable reaction; used to show unconditional stability and efficiency of TASE–Runge–Kutta methods with an inexact Jacobian and to compare second-order stabilized Chebyshev methods."
status: established
aliases: [FitzHugh–Nagumo equation, FHN model, FINAG, nerve conduction equation]
tags: [stiff, verification, stability]
timestamp: 2026-10-20T01:00:00Z
---

# FitzHugh–Nagumo model

The FitzHugh–Nagumo model couples a diffusing activator $v$ with a non-diffusing
recovery variable $w$ (page-local symbols). In the form of
[Conte et al. (2024)](/sources/conte-2024.md) (§7.2, Eq. (7.4)), taken from Wallisch,

$$\begin{aligned}
v_t&=D\,v_{xx}+v-\tfrac13v^3-w,\\
w_t&=\tfrac1{12.5}\,(v+0.7-0.8\,w),
\end{aligned}$$

with diffusion coefficient $D=0.01$ (page-local), on $x\in[0,10]$ with periodic
boundary conditions. The cubic reaction makes the system excitable, and diffusion makes
the semi-discretization stiff, with eigenvalues of the discrete Laplacian growing like
$\Delta x^{-2}$ *(compiler remarks, not stated in the sources)*.

## Configurations

- **Conte et al. (2024)** (§7.2, Eqs. (7.4)–(7.5)): fourth-order finite differences
  with 1024 points; initial data
  $v(x,0)=-\tfrac32+3/\Phi(x-1.5)-3/\Phi(x-2)$, $w(x,0)=-\tfrac34/\Phi(x-1.5)$ with
  $\Phi(x)=1+e^{-10\pi\sinh x}$ (page-local $\Phi$, as printed); stability run on
  $[0,200]$, efficiency runs to $t=50$ against an `ode15s` reference with tolerances at
  machine precision.
- **Faleichik & Moisa (2026)** (§5, problem FINAG): "the FitzHugh and Nagumo nerve
  conduction equation, converted into ODE's by the method of lines", with all parameters
  and output points taken from Abdulle's ROCK4 paper and not printed
  ([Faleichik & Moisa 2026](/sources/faleichik-2026.md), §5).

## What it shows

**TASE–Runge–Kutta with an inexact Jacobian** (Conte et al. 2024, §7.2, Fig. 9). The
[TASE operator](/methods/tase-operators.md) is built not on the Jacobian but on the
constant block-diagonal matrix $\kappa\,\mathrm{blkdiag}(DL_{\Delta}-I,\,-\tfrac{0.8}{12.5}I)$
(page-local: $L_\Delta$ the discrete second derivative, $\kappa=1.2$ a scaling). With this
choice the weighted field of values with exponent $1/3$ lies inside the unconditional
stability diagram for TASE orders 2–4, so all three methods are unconditionally stable
by their Theorem 5.6; the four-stage fourth-order method runs stably at step $0.5$ on
$[0,200]$. In error against CPU time, the TASE methods with the constant matrix are
"much more efficient" than Rosenbrock methods ROS2, ROS3, ROS4 of the same order with
the exact Jacobian (Matlab R2023b on a laptop). See
[Rosenbrock–Wanner methods](/methods/rosenbrock-wanner-method.md).

**Second-order stabilized methods** (Faleichik & Moisa 2026, §5, Table 2). Euclidean
global error, function evaluations $N_f$, accepted/rejected steps and time in ms for
tolerances $10^{-3}$, $10^{-5}$, $10^{-7}$:

| method | tol | error | $N_f$ | accepted | rejected | ms |
|---|---|---|---|---|---|---|
| RKC | $10^{-5}$ | $5.36\times10^{-1}$ | 2617 | 340 | 7 | 0.88 |
| RKC | $10^{-7}$ | $2.62\times10^{-2}$ | 6631 | 1716 | 0 | 2.61 |
| TSRKC2 | $10^{-3}$ | $5.75$ | 1801 | 205 | 7 | 0.54 |
| TSRKC2 | $10^{-5}$ | $8.61\times10^{-2}$ | 4890 | 1283 | 0 | 1.74 |
| TSRKC2 | $10^{-7}$ | $1.68\times10^{-3}$ | 19738 | 8869 | 0 | 8.83 |
| MONO | $10^{-3}$ | $4.50$ | 2673 | 76 | 14 | 0.81 |
| MONO | $10^{-5}$ | $1.21\times10^{-1}$ | 4654 | 505 | 2 | 1.59 |
| MONO | $10^{-7}$ | $2.61\times10^{-3}$ | 17413 | 4800 | 0 | 7.34 |

MONO is the monotonic Runge–Kutta–Chebyshev method of the source. The authors' reading
of all four test problems is that it takes larger steps for the same accuracy but more
internal stages, and is comparable with the other second-order stabilized methods (§5).
On FINAG it took fewer accepted steps than TSRKC2 at every tolerance but more than RKC at
$10^{-5}$ and $10^{-7}$, while reaching smaller errors than RKC there *(compiler reading
of Table 2)*. See
[stabilized explicit Runge–Kutta methods](/methods/stabilized-explicit-runge-kutta.md).

## Qualifications

- Faleichik & Moisa print no RKC row at tolerance $10^{-3}$, without explanation, and the
  achieved errors at that tolerance ($5.75$, $4.50$) are far above it for every code
  (Table 2). No hardware is stated.
- Conte et al. compare a constant, once-factorized matrix with Rosenbrock methods that
  use the exact Jacobian; Rosenbrock methods could also freeze the matrix as W-methods,
  so the comparison is not of like linear-algebra cost (reader's remark on the source).
- The two sources use different parameter sets: Conte et al. print theirs, Faleichik &
  Moisa defer to Abdulle.

# Citations

- [Conte et al. (2024)](/sources/conte-2024.md) — §7.2, Eqs. (7.4)–(7.5), Fig. 9; Thm. 5.6.
- [Faleichik & Moisa (2026)](/sources/faleichik-2026.md) — §5 (problem FINAG), Table 2.
