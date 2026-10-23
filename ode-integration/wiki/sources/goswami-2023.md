---
type: Source
title: "Goswami et al. (2023) — Implementation of low-storage Runge-Kutta time integration schemes in scalable asynchronous partial differential equation solvers"
description: "Couples Williamson 2N low-storage Runge–Kutta schemes with asynchrony-tolerant finite differences so that no halo exchange is needed between stages: buffer points are advanced through the stage recurrence with temporal stencils on delayed data, restoring fourth and sixth order and giving up to 6.68x speed-up on 27,000 cores."
resource: "doi:10.1016/j.jcp.2023.111922"
source_kind: paper
authors: [Goswami S.K., Matthew V.J., Aditya K.]
year: 2023
venue: "J. Comput. Phys. 477:111922"
local_file: "/home/stefano/papers/mosaic/ode-integration/2023_Crossref_Journal_of_Computational_Physics_Goswami_Implementation_of_low-storage_Runge-Kutta_time_integration_s.pdf"
tags: [low-storage, runge-kutta, explicit, parallel, hpc, method-of-lines]
timestamp: 2026-10-20T06:18:00Z
---

# Summary

The paper studies explicit finite-difference PDE solvers on distributed
memory when time integration uses multi-stage
[low-storage Runge–Kutta](/methods/low-storage-runge-kutta.md) schemes in
Williamson's 2N form (LSERK). A standard implementation needs a halo exchange
and a synchronization at every stage; over-decomposition (halos wide enough
for all stages) multiplies message size and adds redundant work. Earlier
asynchronous solvers of the same group tolerated delayed halo data through
asynchrony-tolerant (AT) finite differences, whose stencils include older time
levels of ghost values, but coupled them only with Adams–Bashforth schemes.

The authors want LSERK with no communication between stages, no
over-decomposition and, optionally, relaxed synchronization across steps. A
"naive" coupling, which applies AT stencils at processor-boundary points in
every stage while the stale buffer values stay frozen, is shown by
truncation-error analysis and a statistical error model to cap the solution at
third order in space under strong scaling (second under weak scaling). The
"accurate" coupling advances the buffer points themselves through the LSERK
recurrence, replacing the unavailable right-hand side by a one-sided temporal
AT stencil on the delayed buffer history. Its coefficients are chosen to
reproduce the Taylor terms that the stages accumulate, not just $\partial_tu$.
This is the domain-decomposition analogue of supplying
[stage-consistent boundary data](/methods/runge-kutta-stage-boundary-treatment.md).
Explicit stencils are derived for LSERK2 (fourth order in space) and two
third-order LSERKs (sixth order).

One-dimensional advection–diffusion runs (a variant of the
[linear advection equation](/benchmarks/linear-advection-equation.md); the
error analysis is on the [heat equation](/benchmarks/heat-equation.md)) confirm
slope $-3$ for the naive coupling and $-4$/$-6$ for the accurate one, with
error growing linearly in the number of processes. A C++/MPI three-dimensional
[Burgers](/benchmarks/burgers-equation.md)-turbulence solver with
communication-avoiding and synchronization-avoiding algorithms reaches up to
6.68× speed-up over the synchronous baseline on 27,000 cores (strong scaling)
and about 2× in weak scaling.

# Version read

The file is the version of record (Elsevier typeset), 28 pages, all read, with
visual checks of the equations on pp. 4, 7–9, 11–12 and 14–15. Received 20 July
2022, accepted 5 January 2023, online 18 January 2023. The file was
re-downloaded on 2026-10-19 after the original download error (bundle law,
Corpus); title, authors, volume, article number and DOI on page 1 now match
Crossref. No identity problem.

# Key claims

The analysis is for $u_t=\kappa u_{xx}$ with step $h$, mesh width $\Delta x$,
diffusive Courant number $\nu=\kappa h/\Delta x^2$, communication delay $\tilde k$
(in time levels), $N_{\mathrm{PE}}$ processes and $N_x$ grid points; "order"
means the spatial order obtained with $h\sim\Delta x^r$.

1. In a standard parallel LSERK implementation an $s$-stage scheme needs $s$ halo exchanges with synchronization per step at each process boundary (§2.3, Fig. 2a). **Stated**
2. Over-decomposition avoids inter-stage communication, but its halo width scales with the spatial stencil times the number of stages, it adds redundant computation, and it does not relax synchronization across steps (§2.3, Fig. 2b). **Stated**
3. Earlier asynchronous solvers used AT schemes with Adams–Bashforth time integration, which "possess poor stability, resulting in a strict CFL condition" (§1, §6). **Stated**
4. The AT2 second-derivative stencil with left-buffer delay $\tilde k$ (Eq. 5) has truncation error $\frac1{12}\Delta x^2u^{(4,0)}+\frac12\tilde k(\tilde k+1)\frac{h^2}{\Delta x^2}u^{(0,2)}+O(h^2/\Delta x)$ (Eq. 6); with $h\sim\Delta x^r$ the asynchrony term is $O(\Delta x^{2r-2})$, second order for diffusion ($r=2$) (§2.2). **Derived** (recalled from earlier work)
5. The naive LSERK2-CD2-AT2 coupling remains second-order accurate (local truncation error Eq. 16; global error at process-boundary points $O(\Delta x^2)$) (§3.1.1). **Derived**
6. Naive LSERK2-AT4: the leading local term is $\frac5{32}\kappa\frac{h^3}{\Delta x^2}u^{(0,2)}$ (Eq. 18), from a stage value whose error would cancel against its mirror in a synchronous computation; the global error at process-boundary points is $O(\Delta x^2)$ (§3.1.1). **Derived**
7. Naive LSERK3-AT6: leading local term $-\frac{63427}{777600}\kappa^2\frac{h^4}{\Delta x^4}u^{(0,2)}$, global $O(\Delta x^2)$ at process-boundary points; "the naive approach can at best provide a second-order accurate solution at the PE boundary points" (Eq. 19). **Derived**
8. Domain-averaged error of naive LSERK2-CD4-AT4: $\langle\overline E\rangle\approx\frac5{32}(J_1+J_2)\frac{N_{\mathrm{PE}}}{N_x}\frac{\nu^2}{\kappa}\Delta x^2\langle u^{(0,2)}\rangle_P\sim N_{\mathrm{PE}}\Delta x^3$: third order under strong scaling, second under weak scaling (Eqs. 22–24). **Derived**
9. The naive degradation is caused by buffer-point values not being updated between stages (§3.2). **Derived**
10. Buffer points can be advanced through the LSERK recurrence with the right-hand side replaced by $\partial_tu$ approximated on delayed levels $n-\tilde k,n-\tilde k-1,\dots$; buffer updates are needed only up to stage $s-1$, so temporal AT stencils are needed at stage levels $0,\dots,s-2$ (Eqs. 26–27, §3.2.1). **Derived**
11. The temporal-stencil coefficients solve the full-rank linear system (32): they match $\gamma^e_jh^j$ in the Taylor coefficient of order $j+1$, $j=0,\dots,e$, and annihilate the zeroth and the orders between $e+2$ and $a/r$, where $\gamma^e_j$ (Eq. 30) are built from the 2N coefficients $A^{\mathrm W}_m$, $B^{\mathrm W}_m$ (§3.2.1). **Derived**
12. For LSERK2 with spatial order $a=4$, $r=2$: $\partial_tu\vert^{(0)}\approx\frac{2\tilde k+3}{2h}u^{n-\tilde k}-\frac{2(\tilde k+1)}{h}u^{n-\tilde k-1}+\frac{2\tilde k+1}{2h}u^{n-\tilde k-2}$ (Eq. 34); for $\tilde k=0$ this is the BDF2 derivative formula. **Derived**
13. For LSERK3a and LSERK3b with $a=6$, $r=2$, four-point temporal stencils give Eqs. (36)–(37); the level-0 formula is the same for both, and the level-1 formula differs because $\gamma^1_1=B^{\mathrm W}_1$ differs ($1/4$ vs $1$) (§3.2.1, Table 3). **Derived**
14. The accurate approach first obtains the buffer values at stage level 0 by an $O(h^2)$ polynomial extrapolation; at process-boundary points it uses the AT stencil in stage 1 only and central differences in later stages (§3.3). **Stated**
15. Accurate LSERK2-AT4-CD4 at process-boundary points: four leading local terms, all $O(\Delta x^6)$, including the buffer-update term $\frac1{144}\kappa^2h^2\Delta x^2u^{(6,0)}$ and the AT term $-\frac5{48}(2\tilde k^3+9\tilde k^2+10\tilde k+2)\kappa\frac{h^4}{\Delta x^2}u^{(0,3)}$ (Eq. 39); global $O(\Delta x^4)$, fourth order (§3.4). **Derived**
16. Domain-averaged error of the accurate approach when asynchrony dominates: $\langle\overline E\rangle\approx(J_1+J_2)\frac{N_{\mathrm{PE}}}{N_x}\big(\frac1{144}\kappa\nu\langle u^{(6,0)}\rangle_P-\frac5{48}(2\overline{\tilde k^3}+9\overline{\tilde k^2}+10\overline{\tilde k}+2)\frac{\nu^3}{\kappa^2}\langle u^{(0,3)}\rangle_P\big)\Delta x^4$, linear in $N_{\mathrm{PE}}$ and dependent on the delay moments up to the third (Eq. 43). **Derived**
17. Naive approach on 1D advection–diffusion: error slope $-4$ for $N_x\le128$, then $-3$ asymptotically for LSERK2 with fourth-order space (Case 3); slope $-6$ turning into $-3$ for LSERK3a with sixth-order space (Case 4) (Fig. 5a,b; $N_{\mathrm{PE}}=8$, maximum delay 3). **Shown**
18. Accurate approach: slopes $-4$ (Case 5) and $-6$ (Case 6), errors close to the synchronous ones, no significant effect of the delay statistics (Fig. 5c,d). **Shown**
19. The error grows linearly with $N_{\mathrm{PE}}$ at fixed $N_x=512$ (Case 5, delay probabilities $\{0.2,0.5,0.3\}$, $\nu=0.08$), as Eq. (43) predicts (Fig. 6). **Shown**
20. Burgers turbulence, $512^3$ on 4096 cores, maximum delay 6: kinetic-energy and dissipation decay of the communication-avoiding (CAA) and synchronization-avoiding (SAA) runs agree with the synchronous (SA) one; velocity and gradient moments agree to about four digits (Fig. 7, Table 4; e.g. fourth-order $\langle(\partial u_1/\partial x_1)^2\rangle$: SA 14.5436, CAA 14.5444, SAA 14.5436). **Shown**
21. Strong scaling, $240^3$, 64 to 27,000 cores (Cray, Intel Haswell nodes): at 27,000 cores CAA is 4.81× and SAA 2.14× faster than SA with fourth order (LSERK2), and 6.68× and 2.7× with sixth order (LSERK3a); SA is slower at 27,000 than at 13,824 cores (Fig. 8; 100 steps, mean of 8 runs). **Shown**
22. The larger speed-up of the sixth-order configuration is attributed to the increase from two to three stages, i.e. more avoided inter-stage communications (§5.2). **Stated**
23. Weak scaling, $18^3$ points per core, 64 to 13,824 cores: CAA/SAA speed-ups up to 2.02×/1.89× (fourth order) and 2.1×/1.76× (sixth order); computation time nearly constant, the departure from ideal coming from communication (Fig. 10). **Shown**
24. In SAA most messages arrive with zero delay; higher-order configurations have larger mean delay; CAA's deterministic delay has mean 2.5 for maximum delay 6; SAA therefore gives the more accurate results (moments identical to SA in Table 4) (§5.2, Fig. 11). **Shown**
25. Abstract and conclusion: "speed-ups up to 6×" on 27,000 cores (§6; 6.68× in Fig. 8b). **Shown**

The three LSERK schemes of Table 2 convert to Butcher form as the explicit
midpoint rule (LSERK2), $c=(0,\tfrac14,\tfrac23)$, $b=(\tfrac14,0,\tfrac34)$
(LSERK3a) and $c=(0,1,\tfrac13)$, $b=(0,\tfrac14,\tfrac34)$ (LSERK3b); both
three-stage schemes satisfy the four third-order conditions *(compiler check,
not in the sources)*.
The paper does not name their origin. The stage expansion (29)–(30) writes
stage values through pure time derivatives, which is exact for the linear
autonomous problems analysed; the paper does not discuss nonlinear right-hand
sides such as the Burgers benchmark, whose runs check agreement with the
synchronous solution, not convergence order.

# Printed slips

- Eq. (35) (p. 12): the fourth column of the matrix is printed with $(\tilde k+2)$ in every entry, identical to the third column, which would make the matrix singular; the printed solutions (36)–(37) follow with $(\tilde k+3)$ in that column.
- Algorithms 1–3 (pp. 19–20): the stage line "$q_i^{(m)}=a_m\cdot q_i^{(m-1)}+f_i^{(m-1)}$" and the buffer line omit the factor $\Delta t$ present in Eqs. (9), (25), (26).
- §2.3 (p. 5): "improved the accuracy by two orders of magnitude" means two orders of accuracy.
- §6 (p. 26): "Talyor series"; "a speed of 6× was achieved" (speed-up).
- Refs. [7] and [25] are the same SC'12 poster printed twice under two name orders of the same author ("K. Aditya" and "A. Konduri"); both are cited in the text.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $dv/dt=f(v)$ | $y'=f(y)$ | autonomous form of §2.3 |
| $\Delta t$ | $h$ | step |
| $\Delta x$ | $\Delta x$ | agrees |
| $w_m$, $\beta_{mi}$, $\alpha_m$ | $b_m$, $a_{mi}$, $c_m$ | Butcher weights, matrix, abscissae; **$\alpha$, $\beta$ collide** with Shu–Osher coefficients |
| $K_m$ | $hf(t_n+c_mh,Y_m)$ | step times stage derivative |
| $a_m$, $b_m$ | $A^{\mathrm W}_m$, $B^{\mathrm W}_m$ (page-local, as on [low-storage Runge–Kutta](/methods/low-storage-runge-kutta.md)) | Williamson 2N coefficients, $A^{\mathrm W}_1=0$; **collide** with the Butcher $b$ and the splitting $a_j$, $b_j$ |
| $\delta_m$ | $c_{m+1}$ | time fraction of the register after stage $m$, $\delta_s=1$ |
| $q^{(m)}$, $v^{(m)}$/$u^{(m)}$ | — | 2N registers (increment and solution) after stage $m$ |
| **$\nu$** | $\kappa$ (page-local) | diffusivity; **collides with the Courant number $\nu$** |
| $r_\nu=\nu\Delta t/\Delta x^2$ | $\nu$ | diffusive Courant number |
| $\tilde k$, $\tilde k_1$ | $\tilde k$, $\tilde k_1$ | communication delay in time levels; distinct from the multistep $k$ |
| $L$, $C$, $p_k$ | — | maximum delay (also the CAA period), time levels per message, delay probabilities |
| $P$ | $N_{\mathrm{PE}}$ (page-local) | number of processes; **collides** with the stability polynomial $P$ |
| $N$, $\mathcal N$ | $N_x$, $d$ | grid points; ODE dimension |
| $J_1$, $J_2$ | $J_1$, $J_2$ | stencil extents; distinct from the Jacobian $J$ |
| $\tilde c^l_j$, $\tilde c^l$, $L_1$, $L_2$ | — | AT stencil coefficients and temporal extents |
| $a$, $r$, $d$ | — | target spatial order, exponent of $h\sim\Delta x^r$, derivative order |
| $\gamma^e_j$ | $\gamma^e_j$ (page-local) | stage Taylor coefficients; distinct from the Rosenbrock $\gamma$ |
| $u^{(a_1,a_2)}$ | — | $\partial^{a_1+a_2}u/\partial x^{a_1}\partial t^{a_2}$ |
| $I_I$, $I_P$, $I_B$ | — | interior, process-boundary and buffer point sets |
| CD$k$, AT$k$, LSERK$k$ | — | central difference, asynchrony-tolerant and low-storage schemes of order $k$ (spatial for CD, AT; temporal for LSERK) |

# Reference list

The paper prints 26 references in numbered style ([1]–[26]). The list is
merged complete into the [bibliography](/bibliography.md), with `citedby` this
slug. Refs. [7] and [25] are the same SC'12 poster printed twice under two
forms of one author's name ("K. Aditya", "A. Konduri"); they are folded into
one entry, `aditya-2012`, so the 26 printed items give 25 entries. Ref. [13]
is an arXiv preprint (`aditya-2019`, kept as its own entry), distinct from
the other 2019 Aditya paper [21] (`aditya-2019-b`). Ref. [10] is printed "in this issue" (J. Comput. Phys. 477:111906). Ref.
[1] prints 20 authors. No DOIs are printed. Williamson (1980), Kennedy et al.
(2000), van der Houwen (1996) and Chen et al. (2009) were already in the
bibliography. All items parsed.

# Pages created or updated

Chunk 6 (2026-10-20). This source is cited on:

* [Boundary conditions for Runge–Kutta stages](/methods/runge-kutta-stage-boundary-treatment.md)
* [Burgers equation](/benchmarks/burgers-equation.md)
* [Heat equation](/benchmarks/heat-equation.md)
* [Learned time integrators: neural surrogates and physics-informed Runge–Kutta networks](/methods/learned-time-integrators.md)
* [Linear advection equation](/benchmarks/linear-advection-equation.md)
* [Local time stepping](/methods/local-time-stepping.md)
* [Low-storage Runge–Kutta methods](/methods/low-storage-runge-kutta.md)
