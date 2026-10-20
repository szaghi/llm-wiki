---
type: Benchmark
title: "Brusselator"
description: "The one-dimensional advection–diffusion–reaction Brusselator, a three-species stiff reaction system with a fast relaxation term, is the shared test of IMEX, multirate and nonlinear-solver studies; the original six-species reaction ODE serves as a production–destruction test; the page gives the variants, parameters and splittings used and what each test showed."
status: established
aliases: [advection–diffusion–reaction Brusselator, stiff Brusselator, 1D Brusselator, original Brusselator, six-species Brusselator]
tags: [stiff, imex, multirate, software, verification, positivity]
timestamp: 2026-10-20T10:00:00Z
---

# Brusselator

The Brusselator in the sources is a one-dimensional
advection–diffusion–reaction system for three species $u$, $v$, $w$
(page-local) whose third reaction term relaxes $w$ on the fast scale
$\varepsilon$. Its three processes have well-separated time scales, so it serves
as the test of choice for [IMEX](/methods/imex-runge-kutta.md),
[multirate infinitesimal](/methods/multirate-infinitesimal-methods.md) and
[IMEX-MRI-GARK](/methods/imex-mri-gark.md) methods and of the stage solvers of
[ARKODE](/software/arkode.md). With advection speed $\mathsf c$, diffusion
$\mathsf d$ and reaction constants $\mathsf a$, $\mathsf b$ (all page-local), the
common form is

$$\begin{aligned}
u_t&=-\mathsf c\,u_x+\mathsf d\,u_{xx}+\mathsf a-(w+1)u+u^2v,\\
v_t&=-\mathsf c\,v_x+\mathsf d\,v_{xx}+wu-u^2v,\\
w_t&=-\mathsf c\,w_x+\mathsf d\,w_{xx}+\frac{\mathsf b-w}{\varepsilon}-wu,
\end{aligned}$$

on $x\in[0,1]$, semi-discretized by finite differences in space (method of lines).

## Variants

| Source | Terms | Parameters | Grid, BCs | Interval | Initial data |
|---|---|---|---|---|---|
| [Chinomona & Reynolds (2021)](/sources/chinomona-2021.md), §5.2 | advection, diffusion, reaction | $\mathsf d=10^{-2}$, advection coefficient $10^{-3}$ (printed $+\rho u_x$), $\mathsf a=0.6$, $\mathsf b=2$, $\varepsilon=10^{-2}$ | 2nd-order centred, 201 or 801 points, stationary BCs $u_t=v_t=w_t=0$ at $x=0,1$ | $[0,3]$ | $u=\mathsf a+0.1\sin\pi x$, $v=\mathsf b/\mathsf a+0.1\sin\pi x$, $w=\mathsf b+0.1\sin\pi x$ |
| [Reynolds et al. (2023)](/sources/reynolds-2023.md), §5.1, eq. 22 | advection, diffusion ($\mathsf d=0$ in the ERK tests), reaction | $\mathsf c=0.001$, $\mathsf d=0.01$, $\mathsf a=0.6$, $\mathsf b=2$, $\varepsilon=0.01$ | 2nd-order centred, $N=512$, stationary BCs | $[0,10]$ | as above |
| [Fish et al. (2024)](/sources/fish-2024.md), §6.2.1 (fixed step) | advection, diffusion, reaction, "same formulation" as Chinomona & Reynolds | $\mathsf d=10^{-2}$, advection $10^{-3}$, $\mathsf a=0.6$, $\mathsf b=2$, $\varepsilon=10^{-2}$ | 2nd-order centred, 201 or 801 points, stationary BCs | $[0,3]$ | as Chinomona & Reynolds |
| Fish et al. (2024), §6.2.2 (adaptive) | as above with time-varying coefficients | $\mathsf d=\mathsf c=6\times10^{-5}+5\times10^{-5}\cos\pi t$, reaction factor $\mathsf r=0.6+0.5\cos4\pi t$, $\mathsf a=1$, $\mathsf b=3.5$, $\varepsilon=10^{-3}$ | 101 points | $[0,3]$ | $u=1.2+0.1\sin\pi x$, $v=3.1+0.1\sin\pi x$, $w=3+0.1\sin\pi x$ |
| [Fish & Reynolds (2023)](/sources/fish-2023.md), §4.1.2 (ODE) | reaction only | $\mathsf a=1$, $\mathsf b=3.5$, $\varepsilon=10^{-2}$ | — | $[0,2]$ | $(u,v,w)(0)=(1.2,3.1,3)$ |
| Fish & Reynolds (2023), §4.8 (PDE) | diffusion and reaction, time-varying | $\mathsf d=0.006+0.005\cos\pi t$, $\mathsf r=0.6+0.5\cos4\pi t$, $\mathsf a=1$, $\mathsf b=3.5$, $\varepsilon=10^{-3}$ | stationary BCs (grid not stated) | $[0,2]$ | as Fish et al. adaptive |
| [Gardner et al. (2022)](/sources/gardner-2022.md), §6.1 | advection, reaction (no diffusion) | $\mathsf c=0.01$, $\mathsf a=1$, $\mathsf b=3.5$, $\varepsilon=5\times10^{-6}$ | 1st-order upwind on $[0,L]$ (page-local length), periodic, $L/n_x=10^{-3}$ | $[0,10]$ | $u=\mathsf a+\varrho$, $v=\mathsf b/\mathsf a+\varrho$, $w=3+\varrho$, $\varrho=0.1\exp(-2(2x/L-1)^2)$ |

Chinomona & Reynolds and Reynolds et al. describe their versions as variations of
earlier Brusselator tests; the reaction terms and constants $\mathsf a=0.6$,
$\mathsf b=2$, $\varepsilon=10^{-2}$ coincide, the advection coefficient differs in
sign convention and value. Gardner et al.'s version is far stiffer
($\varepsilon=5\times10^{-6}$) and has no diffusion. In the time-varying variants the
reaction terms are multiplied by $\mathsf r(t)$ (page-local); Fish et al. (2024) take them
from Fish & Reynolds (2023), whose ratio of diffusion to reaction coefficient ranges over
about $10^{-3}$–$10^{-1}$.

**Time scales** (Reynolds et al. 2023, §5.1): for explicit stability, diffusion is
the most restrictive, then reaction, then advection; for accuracy, reaction is the
fastest and advection and diffusion are comparable; $(\mathsf b-w)/\varepsilon$ adds
mild stiffness.

## Splittings and what the tests showed

- **IMEX-MRI-GARK and MRI-GARK** (Chinomona & Reynolds 2021): advection explicit
  slow, diffusion implicit slow, reaction fast (fast step $H/5$, fast implicit DIRKs,
  Newton with banded direct solves; reference ARKODE fifth-order DIRK at
  $H=10^{-7}$; error the maximum over 10 output times; $H=0.1\cdot2^{-k}$,
  $k=0,\dots,10$). Measured rates on 201 / 801 points: Lie–Trotter 0.91 / 0.90,
  Strang–Marchuk 1.92 / 1.87, IMEX-MRI-GARK3a 2.86 / 2.41, 3b 2.92 / 2.47,
  MRI-GARK-ESDIRK34a 2.94 / 3.02, IMEX-MRI-GARK4 3.12 / 2.69, MRI-GARK-ESDIRK46a
  2.94 / 2.42. Higher-order methods show
  [order reduction](/definitions/order-reduction.md) when the grid is refined;
  IMEX-MRI-GARK4 is unstable above $H=1/80$ (201 points) and $1/160$ (801 points),
  MRI-GARK-ESDIRK46a above $1/40$ and $1/80$. The authors call linear advection a
  "best case" for implicit MRI-GARK (§5.2).
- **Explicit methods and controllers** (Reynolds et al. 2023, §5.1.1, Fig. 2;
  advection–reaction, $\mathsf d=0$): Heun–Euler (order 2) is most efficient at
  coarse accuracy despite more than twice the step attempts of order 3;
  Bogacki–Shampine (order 3) for errors $10^{-5}$–$10^{-7}$; Cash–Karp (order 5)
  below $10^{-7}$. The I controller is often least efficient (13–50% rejected
  steps), PI and Gustafsson often most efficient (under 7%), PID in between
  ([step-size control](/methods/step-size-control.md)).
- **DIRK versus IMEX and implicit predictors** (Reynolds et al. 2023, §5.1.2,
  Table 1; tolerances $10^{-4}$ / $10^{-9}$): DIRK and IMEX with advection explicit
  take 21–34 steps; IMEX with advection and reaction explicit and one Newton
  iteration takes about 250 steps. The maximum-order predictor cuts statistics by at
  least 32% for the first two configurations; the cutoff predictor helps the third
  by up to 20% ([implicit stage solvers](/methods/implicit-stage-solvers.md)).
- **Inner solvers of MRI** (Reynolds et al. 2023, §5.1.3, Table 2; IMEX-MRI-GARK3a,
  advection and diffusion slow with $H=0.1$, reactions fast): see
  [multirate infinitesimal methods](/methods/multirate-infinitesimal-methods.md).
- **IMEX-MRI-SR against IMEX-MRI-GARK, fixed step** (Fish et al. 2024, §6.2.1, Fig. 6;
  reaction fast, diffusion implicit, advection explicit, fast step $H/10$, Newton with banded
  solves, reference MATLAB `ode15s`): rates on 201 / 801 points are Lie–Trotter 0.76 / 0.72,
  Strang–Marchuk 1.59 / 1.24, IMEX-MRI-SR2(1) 2.00 / 2.01, SR3(2) 3.09 / 2.90, SR4(3)
  3.00 / 1.90, IMEX-MRI-GARK3a 3.36 / 2.71, 3b 3.25 / 2.69, IMEX-MRI-GARK4 3.41 / 2.42; an error
  floor near $10^{-11}$ is attributed to the reference. SR4(3) is unstable above $H=1/320$ and
  $1/640$, IMEX-MRI-GARK4 above $1/80$ and $1/160$, the latter agreeing with Chinomona &
  Reynolds ([IMEX-MRI-SR](/methods/imex-mri-sr.md)).
- **Adaptive IMEX-MRI-SR** (Fish et al. 2024, §6.2.2, Fig. 7; tolerances $10^{-1}$–$10^{-9}$,
  multirate Constant-Constant controller): SR3(2) is generally the most efficient in fast
  evaluations; some runs fail by oscillating between accepted and rejected steps.
- **Multirate controllers** (Fish & Reynolds 2023): the ODE is one of seven tuning problems
  (fast part $-w/\varepsilon$, the rest slow); the time-varying PDE (diffusion slow, reaction fast,
  MRI-GARK-ERK45a, $\mathrm{tol}=10^{-4}$) shows all controllers keeping $m=1$ until reaction
  stiffness appears near $t\approx0.9$ and then raising $m$, and over-solving by two to four
  orders of magnitude over $\mathrm{tol}=10^{-3}$–$10^{-7}$ (§4.8, Figs. 8–9;
  [step-size control](/methods/step-size-control.md)).
- **Task-local Newton** (Gardner et al. 2022, §6.1, Fig. 3; ARKODE default
  third-order IMEX, advection explicit, reaction implicit): solving each MPI
  task's reaction block independently gives 4.2× to 7.9× speedup over a global
  Newton–GMRES solve, weak scaling from 40 to 10,240 tasks (CPU only, averages of
  20 runs); C and Fortran 2003 versions give identical statistics.

## The original six-species Brusselator

[Izzo et al. (2025)](/sources/izzo-2025.md) (Test 3, Eq. (4.25)) use a different system,
the original Brusselator reaction ODE (Lefever–Nicolis) with six species and rate constants
$k_1,\dots,k_4$ (page-local):

$$\begin{aligned}
y_1'&=-k_1y_1, & y_2'&=-k_2y_2y_5, & y_3'&=k_2y_2y_5,\\
y_4'&=k_4y_5, & y_5'&=k_1y_1-k_2y_2y_5+k_3y_5^2y_6-k_4y_5, & y_6'&=k_2y_2y_5-k_3y_5^2y_6,
\end{aligned}$$

with all $k_l=1$, $t\in[0,10]$ and $y(0)=(10,10,0,0,0.1,0.1)$. It is a fully conservative
[production–destruction system](/definitions/production-destruction-system.md) with
$p_{32}=d_{23}=k_2y_2y_5$, $p_{45}=d_{54}=k_4y_5$, $p_{51}=d_{15}=k_1y_1$,
$p_{56}=d_{65}=k_3y_5^2y_6$, $p_{65}=d_{56}=k_2y_2y_5$, so $\sum_iy_i$ is invariant. The two
zero initial components are replaced by the smallest normalized double, about
$2.2\times10^{-308}$, because the Patankar weights divide by them. The modified Patankar
multistep methods of orders 1–6 show observed orders 1.00, 1.98, 2.95, 3.90, 4.80 and 5.68
at the finest step (Table 4), and for $p\ge3$ they are more efficient than the third-order
MPRK of Kopecz–Meister and than modified Patankar deferred correction of the same order
(Figs. 13–14); see [modified Patankar methods](/methods/modified-patankar-methods.md). This
ODE has no transport and no fast relaxation parameter and is unrelated to the PDE variants
above except by name and reaction mechanism.

## Qualifications

- Reynolds et al. print the diffusion term of all three equations as
  $\mathsf d\,u_{xx}$ (eq. 22; *compiler check of the PDF*); the intended terms
  are $\mathsf d\,v_{xx}$ and $\mathsf d\,w_{xx}$, as written above.
- **Printed slips in the reaction term of $u$.** Fish et al. (2024, p. 21 of the arXiv
  version; *compiler check of the PDF*) print $\mathsf a-(w-1)u+u^2v$ in the PDE and in the
  fast partition, while stating they use the formulation of Chinomona & Reynolds, which has
  $\mathsf a-(w+1)u+u^2v$; Fish & Reynolds (2023, §4.1.2) print the right-hand side with
  $-(w+1)u$ but its slow part with $+(w+1)u$, so that the parts do not add up to the
  right-hand side. Both are read as slips, and the runs as using $-(w+1)u$ *(compiler reading; the code was not checked)*.
- The tests measure temporal error against a numerical reference on a fixed grid
  (Chinomona & Reynolds) or the maximum relative error at the final time
  (Reynolds et al.); the rates above are least-squares fits.

# Citations

- [Chinomona & Reynolds (2021)](/sources/chinomona-2021.md) — §5.2, Fig. 3.
- [Reynolds et al. (2023)](/sources/reynolds-2023.md) — §5.1 (eq. 22, Fig. 2, Tables 1–2).
- [Gardner et al. (2022)](/sources/gardner-2022.md) — §6.1 (Fig. 3), §7.1.
- [Fish et al. (2024)](/sources/fish-2024.md) — §6.2 (Figs. 6–7).
- [Fish & Reynolds (2023)](/sources/fish-2023.md) — §4.1.2, §4.8 (Figs. 8–9).
- [Izzo et al. (2025)](/sources/izzo-2025.md) — §4.3 (Eq. (4.25), Table 4, Figs. 10, 13–14); arXiv v1.
