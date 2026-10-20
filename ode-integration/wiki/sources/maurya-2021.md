---
type: Source
title: "Maurya et al. (2021) — New optimized implicit-explicit Runge-Kutta methods with applications to the hyperbolic conservation laws"
description: "Proposes OPIRK, sequential partitioned updates for linear wave systems in which later equations use a weighted mix of old and already-updated values of earlier unknowns, with weights tuned by a space-time dispersion-relation-preserving optimization; the one-stage method is neutrally stable up to a critical Courant number."
resource: "doi:10.1016/j.jcp.2021.110650"
source_kind: paper
authors: [Maurya P.K., Yadav V.S., Mahato B., Ganta N., Rajpoot M.K., Bhumkar Y.G.]
year: 2021
venue: "J. Comput. Phys. 446:110650"
local_file: "/home/stefano/papers/mosaic/ode-integration/2021_Crossref_Journal_of_Computational_Physics_Maurya_New_optimized_implicit-explicit_Runge-Kutta_methods_with_app.pdf"
tags: [imex, semi-implicit, von-neumann-analysis, dispersion-relation-preserving, wave-propagation]
timestamp: 2026-10-20T16:00:00Z
---

# Summary

The paper proposes "optimized partially implicit-explicit Runge–Kutta"
(OPIRK) integrators for linear(ized) wave systems: the 1D and 2D linearized
Euler equations of acoustics and the 1D and 2D rotating shallow water
equations. The system is partitioned by unknown. The first equation is
advanced explicitly. Each later equation uses a weighted combination of its
operator evaluated at the old values and at the **already updated** values
of the earlier unknowns, with a free weight per evaluation. No linear system
is solved: the update is sequential and explicit, Gauss–Seidel-like across
the equations. The label "implicit-explicit" therefore differs from the
standard [IMEX Runge–Kutta](/methods/imex-runge-kutta.md) meaning. With
weight 1 the one-stage method OPIRK1 is the classical forward–backward
(symplectic-Euler-type) update, which the paper does not say *(compiler
check, not in the sources: with $\omega_1=1$ the second update reads
$p^{n+1}=p^n+hL_2(u^{n+1})$)*.

The free weights are fixed by a dispersion-relation-preserving optimization
of the fully discrete scheme. The objective is the integral of
$\lvert G_{\mathrm{num}}-G_{\mathrm{exact}}\rvert^2$ over wavenumber, with
integral constraints on amplitude, phase-speed and group-velocity errors;
it is solved by grid search at a fixed Courant number. Spatial operators are
second-order central differences (CD2) or the compact OUCS3 scheme. The
analysis is a [von Neumann](/definitions/von-neumann-stability-analysis.md)
study of the amplification matrix, the space–time analogue of the
[stability function](/definitions/stability-function.md). OPIRK1 with
weight 1 has $\lvert G\rvert=1$ up to $\nu=2$ (CD2) or $0.91$ (OUCS3). A
larger weight adds dissipation, and a smaller one is unstable.

In an appendix the authors analyze three
[semi-implicit IMEX](/methods/semi-implicit-imex-runge-kutta.md) schemes
from atmospheric modelling (SIRK3, SIL3, ARS) on the linearized rotating
shallow water equations. SIRK3 is mildly unstable there, while OPIRK1 is
neutral. The tests are acoustic pulses, cylinder scattering, an oscillating
piston, barrier diffraction, reflection with mean flow, shallow water
Gaussians and wave packets, and an unstable jet; they are compared with
classical RK4 graphically or by $L_2$ errors. OPIRK1 runs 2.4–2.8 times
faster than RK4. The orders of accuracy are asserted by name and never
measured.

# Version read

The file is the version of record (Elsevier typeset), 41 pages, available
online 20 Aug 2021. This re-downloaded file's page 1 matches Crossref
(title, six authors, volume, article number, DOI); no identity problem.
Equation and table numbers below are those of this version.

# Key claims

Notation: for the 1D linearized Euler system $u_t=L_1(p)$, $p_t=L_2(u)$;
$G$ the amplification factor of the fully discrete scheme; $a=\nu\zeta(k\Delta x)$
the scaled modified wavenumber; $\omega_1,\dots$ (the source's
$c_1,\dots,c_5$, $d_1,\dots,d_6$) the free weights.

1. OPIRK methods "carry the advantages of implicitness, while they do not require numerical inversion of the resultant coefficient matrices", at a cost similar to explicit schemes (§1). **Stated**
2. OPIRK1 for the 1D linearized Euler system: $u^{n+1}=u^n+hL_1(p^n)$, $p^{n+1}=p^n+h[(1-\omega_1)L_2(u^n)+\omega_1L_2(u^{n+1})]$, with amplification factors $G_{1,2}=1-\omega_1a^2/2\mp a\sqrt{\omega_1^2a^2-4}/2$ (§2.1, Eqs. 6–8). **Derived**
3. In the wave regime ($\omega_1^2a^2<4$), stability requires $\omega_1\ge1$ (§2.1). **Derived**; it follows from $\lvert G\rvert^2=\det M_1=1+(1-\omega_1)a^2$ *(compiler check)*
4. OPIRK1 is neutrally stable for all wavenumbers at $\omega_1=1$, with critical Courant number 2.0 (CD2) and 0.91 (OUCS3) (§3.1, Table 1, Figs. 1–3). **Derived**
5. Table 1: $\omega_1=0.5$ gives $\max\lvert G\rvert=1.22474$ (CD2) and 1.26885 (OUCS3); $\omega_1=1.5$ gives $\min\lvert G\rvert=0.70711$ and 0.62455, critical numbers 1.34 and 0.61 (Table 1). **Derived**
6. The two-stage OPIRK2 with weights (0.75, 1.5) or (0.5, 0.5) is neutral; critical Courant numbers 1.48/0.68 and 2.00/0.91 (CD2/OUCS3) (§2.2, Eq. 10, Table 2). **Derived**
7. The numerical properties of OPIRK1 and OPIRK2 are almost the same on the 1D linearized Euler system (§3.1, Figs. 1, 4). **Shown**
8. The weights minimize $\int_0^{\gamma}\lvert G_{\mathrm{num}}-G_{\mathrm{exact}}\rvert^2\,d(k\Delta x)$, $G_{\mathrm{exact}}=e^{i\nu k\Delta x}$, subject to integral bounds on $\lvert G\rvert-1$, group-velocity and phase-speed errors, by grid search at fixed $\nu$ (§3, Eqs. 12–13). **Stated** (bounds not given numerically)
9. 1D acoustic pulse, OUCS3, $h=10^{-6}$ s: $L_2$ errors of OPIRK1 at $t=0.005$–$0.02$ are $1.394\times10^{-4}$ to $8.602\times10^{-4}$, against $1.826\times10^{-3}$ to $8.642\times10^{-4}$ for RK4 (§3.2, Table 3). **Shown**
10. 2D OPIRK1: $G_1=1$, $G_{2,3}=\delta\mp i\Omega$, $\delta=1-\omega_5(a^2+b^2)/2$, wave regime $(a^2+b^2)\omega_5^2<4$ (§4.1, Eqs. 22–23). **Derived**
11. Table 4 (2D, $\nu=0.2$): $\omega_5=1$ is neutral for CD2 and OUCS3; $\omega_5=0.5$ gives $\max\lvert G\rvert=1.01980$ and 1.09325 (Table 4). **Derived** (two entries inconsistent; see Printed slips)
12. Cylinder scattering (CAA workshop benchmark), OPIRK1-OUCS3, $h=10^{-4}$: $L_2$ errors $1.354\times10^{-5}$ and $1.024\times10^{-5}$ at the two probes, against $2.134\times10^{-5}$ and $2.856\times10^{-5}$ for RK4 (§4.2, Table 5). **Shown**
13. Oscillating piston, barrier diffraction (against Kawai's experiment) and pulse reflection with mean flow at Mach 0.5: OPIRK1 agrees with analytical or experimental data and with RK4 (Figs. 12, 14, 16). **Shown** (graphical)
14. "Although the OPIRK1 method is first-order accurate, the accuracy of the computed results is comparable to that of RK4 method" (§7). **Shown** (graphical; order not measured)
15. Wall-clock times RK4/OPIRK1: about 32/13 s (1D pulse), 91/32 (reflection), 250/95 (cylinder), 126/53 (piston) (Table 6). **Shown** (hardware and per-method steps not stated)
16. On the linearized rotating shallow water equations with CD2 at $\nu=0.2$, SIRK3 "is slightly unstable", SIL3 and ARS are stable, and OPIRK1 is neutrally stable up to the Nyquist limit (§9, App. A, Fig. 17). **Derived** (eigenvalues by symbolic computation)
17. OPIRK1 for the rotating shallow water equations with weights $\omega_1=\omega_2=1$ is neutral for CD2 and OUCS3; a second weight below 1 gives $\max\lvert G\rvert>1$ (§9, Eq. 37, Table 7). **Derived**
18. OPIRK2 for the rotating shallow water equations with weights (0.5, 0, 0.5, 0) is neutral (§10, Eq. 42, Table 8). **Derived**
19. Percentage DRP area on the rotating shallow water equations: 0.134 and 0.192 (OPIRK1, OPIRK2 with CD2), 11.766 and 11.731 (with OUCS3); compared with another paper's RK4 table this "established the better performance of the OPIRK methods" (§11, Table 9). **Derived**
20. 1D shallow water Gaussian: RK4-OUCS3 develops "Gibbs oscillations at later time instants ... which result in instability", OPIRK1 does not (§12.1, Fig. 23). **Shown** (questioned below)
21. 2D wave packet near the $q$-wave limit ($k_0\Delta x=2.3365$ against 2.3910 for OUCS3): OPIRK1-OUCS3 admits $q$-waves that skew the solution; larger weights add dissipation (§12.2, Figs. 24–25). **Shown**
22. Unstable jet on a doubly periodic f-plane: RK4 with $h=2$ s and OPIRK1 with $h=10$ s both represent vortex formation to 10 days; no quantitative errors (§12.3, Fig. 26). **Shown**
23. "Computational complexity of the developed methods is comparable with explicit Runge-Kutta methods of same order" (§13). **Stated**
24. For the rotating shallow water equations the new methods have a larger DRP area than RK4 (§13, Table 9). **Stated**

Three caveats. The time-step comparison against RK4 (claim 15) sets a
one-stage first-order method against a four-stage fourth-order one at
apparently equal steps, without error-against-cost curves. In claim 20 the
Courant number is about $31.3\times0.05/1000\approx1.6\times10^{-3}$, far
inside RK4's imaginary-axis stability interval *(compiler check)*, so the
reported RK4 instability is unlikely to come from the time integrator. No
order conditions are written, and with Eq. 10 as printed OPIRK2 would not
be second order in $u$ (see Printed slips).

# Printed slips

- Eq. 10, third line: "$u^{n+1}=\frac12[u^n+u^1+\Delta tL_1(p^n)]$" collapses to $u^{n+1}=u^n+\Delta tL_1(p^n)$; the matrix $M_2$ (entry $1-a^2/2$) and the 2D analogue Eq. 42 need $L_1(p^1)$. "$2c_3L_2u^1$" lacks parentheses.
- The condition after Eq. 11 is written with $c_3,c_4$, while Eq. 11 uses $c_2,c_3$.
- Table 4, rows $c_5=1.01$: printed $\min\lvert G\rvert$ 0.99600 (CD2) and 0.99000 (OUCS3). The relation $\lvert G_{2,3}\rvert^2=1+(1-c_5)(a^2+b^2)$ reproduces the other rows and gives about 0.99960 and 0.99805 here *(compiler check)*; as printed the row is smaller than the $c_5=1.05$ row.
- Table 1 states no Courant number; its CD2 entries match $\nu=1$ and its OUCS3 entries $\nu=0.5$ *(compiler check)*.
- Table 2 ("Optimized values of free parameters") and Table 7 list anti-dissipative or unstable choices ($\max\lvert G\rvert$ up to 1.11803 and 1.04747).
- §4.1 "$G=[G_1,G_2,G_2]^T$"; §9 "ARS 2.5/2.5" once; §10 "eigenvalues of $M_2$" for $M_5$; Fig. 24 caption "$(k_0\Delta x, k_0\Delta x)$".
- §9 and App. A attribute SIRK3 to "Kar [39]" and SIL3 to "Whitaker and Kar [40]", but [39] is Whitaker & Kar (2006) and [40] is Kar (2013): the numbers are swapped relative to the names.
- The SIRK3 tableau prints implicit diagonal entries $(1-\epsilon)/4$, $(1-\epsilon)/2$, while Eq. 51 has $(1+\epsilon)/4$, $(1+\epsilon)/2$.
- The phase is $\beta=-\tan^{-1}(G_i/G_r)$ in §2.1 and §9 but $\beta=\tan^{-1}(\Omega/\delta)$ in §4.1.
- Table 9 lists "Order of spatial discretization scheme: 2nd" also for the OUCS3 rows; §12.1 calls $\eta$ "the water depth" (it is the surface elevation); "free-stream parameter $c_5$" for free parameter.
- Ref. [17] "J. Theor. Comput. Accous."; ref. [6] first author printed "A. N.-Yazdi".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Delta t$ | $h$ | |
| $u^n$, $p^n$, $u^1$, $u^{(1)}$ | same (page-local) | per-unknown levels and first-stage values (stage values, not derivatives) |
| $L_1,\dots,L_5$ | same (page-local) | per-equation spatial operators of a partitioned system, not an additive split of one right-hand side; **collision** with the linear operator $L$ |
| $c_1,\dots,c_5$, $d_1,\dots,d_6$ | $\omega_1,\dots$ (page-local) | free weights of the updated-value evaluations; **collision**: not RK abscissae $c_i$ |
| $N_c$, $N_{cx}$, $N_{cy}$ | $\nu$ | Courant numbers |
| $G$, $G_r$, $G_i$ | same (page-local) | amplification factor of the fully discrete scheme, analogue of $R(z)$; **collision** with the G-norm matrix $G$ |
| $M_1,\dots,M_5$ | same (page-local) | amplification matrices; **collision** with the mass matrix $M$ |
| $a=N_c\zeta$, $b=N_{cy}\psi$ | same (page-local) | scaled modified wavenumbers; **collision** with the RK coefficients |
| $\zeta(k\Delta x)$, $k$ | same (page-local) | modified wavenumber; $k$ the wavenumber, **collision** with the multistep $k$ |
| $c$, $c_N$, $V_{gN}$, $\omega_N$ | same (page-local) | physical and numerical phase speed, group velocity, frequency |
| $\beta$ | same (page-local) | numerical phase shift per step; **collision** with the PID and multistep $\beta$ |
| $p=f\Delta t$ | same (page-local) | Coriolis number; **collision** with the pressure $p$ and the order $p$ |
| $\lambda=\Delta y/\Delta x$ | same (page-local) | grid aspect ratio; **collision** with the eigenvalue $\lambda$ |
| $\eta$ | same (page-local) | surface elevation; **collision** with the entropy $\eta(y)$ |
| $A$, $\tilde A$, $b$, $\tilde b$, $c$ | $A^{\mathrm E}$, $A^{\mathrm I}$, $b^{\mathrm E}$, $b^{\mathrm I}$, $c$ | IMEX tableaux of App. A, Coriolis part explicit, gravity part implicit |
| $\epsilon$ | same (page-local) | SIRK3 decentering parameter |

# Reference list

The paper prints 49 references in numbered style ([1]–[49]). The list is
merged complete into the [bibliography](/bibliography.md), with `citedby`
this slug. Tam & Hardin (1997) [29] and Tam, Kurbatskii & Fang (1997) [30]
share a key and take suffixes in printed order (`tam-1997`, `tam-1997-b`).
Ref. [6] is keyed from its printed first author "A. N.-Yazdi"
(`nyazdi-2013`). Workshop items [29]–[32] are NASA CP
3352 / ICASE contributions. No printed duplicates or unparseable items.

# Pages created or updated

Chunk 6 (2026-10-20). This source is cited on:

* [IMEX and additive Runge–Kutta methods](/methods/imex-runge-kutta.md)
* [Semi-implicit and linearly implicit IMEX Runge–Kutta methods](/methods/semi-implicit-imex-runge-kutta.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)
* [Von Neumann (Fourier) stability analysis of fully discrete schemes](/definitions/von-neumann-stability-analysis.md)
