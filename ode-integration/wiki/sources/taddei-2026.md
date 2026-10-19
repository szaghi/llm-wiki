---
type: Source
title: "Taddei et al. (2026) — High-order implicit Runge–Kutta time integrators for component-based model reduction of FSI problems"
description: "Applies Radau IIA to the DAE of incompressible ALE fluid–structure interaction, at full and reduced order, with all-stage Newton and static condensation on the interface; the IRK models stay stable where BDF2–Newmark fails, but observed rates fall well below $2s-1$."
resource: "doi:10.1016/j.jcp.2026.115326"
source_kind: paper
authors: [Taddei T., Xu X., Zhang L.]
year: 2026
venue: "J. Comput. Phys. 567:115326"
local_file: "/home/stefano/papers/mosaic/ode-integration/2026_Crossref_Journal_of_Computational_Physics_Taddei_High-order_implicit_RungeKutta_time_integrators_for_componen.pdf"
tags: [runge-kutta, implicit, dae, order-reduction, implicit-stage-solvers]
timestamp: 2026-10-20T01:00:00Z
---

# Summary

The paper builds a projection-based, component-based reduced-order model (ROM) for
incompressible fluid–structure interaction (FSI) in ALE form. Radau IIA
[fully implicit Runge–Kutta](/methods/fully-implicit-runge-kutta.md) methods
integrate both the full-order and the reduced model. The semi-discrete FSI system is
written as a semi-explicit
[differential-algebraic equation](/definitions/differential-algebraic-equation.md)
$y'=f(t,y,w)$, $0=g(t,y)$, with masked momenta as differential and pressure as
algebraic variable. Radau IIA has [stiff accuracy](/properties/stiff-accuracy.md), so
the step value is the last stage.

Structural velocity stages are eliminated through $A^{-1}$, and the coupled
all-stage nonlinear system is solved by Newton with static condensation onto the
interface displacement (see [implicit stage solvers](/methods/implicit-stage-solvers.md)).
Each such Newton step coincides with an SQP step of a constrained minimization. The
ROM uses POD bubble and port bases; it satisfies a semi-discrete energy balance, and
its fully discrete form is the same Runge–Kutta method applied to the semi-discrete ROM.

On a vertical beam in channel flow, Radau IIA with $s=2,3,4$ shows fitted rates of
about 2.1, 2.4 and 3.5 against the formal $2s-1$. The authors attribute this
[order reduction](/definitions/order-reduction.md) loosely to the DAE structure
and to the coupling with space, mesh motion and interface iteration. On the
Turek–Hron FSI3 benchmark, Radau IIA ($s=2$) stays stable with bounded energy,
whereas BDF2 for the fluid plus the undamped
[Newmark method](/methods/newmark-method.md) for the structure is unstable. Damped
Newmark is stable but more dissipative. The comparison draws on the
[A- and L-stability](/properties/a-stability.md) of Radau IIA and the Dahlquist
barrier on the [backward differentiation formulas](/methods/backward-differentiation-formula.md)
and other [linear multistep methods](/methods/linear-multistep-method.md).

At reduced order the IRK ROM stays stable over long times, while the BDF2–Newmark
ROM with the same basis is unstable whatever the Newmark damping. No timings are
reported, and no new time-integration theory is proposed.

# Version read

arXiv:2512.23363v1 [math.NA], 29 Dec 2025, header "Submitted to Elsevier, December
2025"; 32 pages, all read (pp. 14 and 17 also visually). It is not the JCP version
of record. Page 1 prints "Runge-Kutta" with a hyphen where Crossref has an en dash;
title and authors otherwise match. Section, equation, table and figure numbers on
this page are those of arXiv v1.

# Key claims

1. BDF2 for the fluid with Newmark for the structure is common practice in incompressible FSI and gives overall second order; standard Newmark can be unstable for geometrically nonlinear structures (§1.1, citing [25–29]). **Stated**
2. Dissipative alternatives (Bossak, generalized-α, ESDIRK) damp spurious high frequencies but risk over-attenuating physical structural dynamics (§1.1, citing [30, 31]). **Stated**
3. The second Dahlquist barrier prevents higher-order linear multistep methods such as BDF from being A- and L-stable; fully implicit Runge–Kutta methods overcome this (§1.1, citing [36, 37]). **Stated**
4. Radau IIA methods are high-order, A-stable, L-stable and stiffly accurate ($a_{si}=b_i$, $c_s=1$), so $y_{n+1}=Y_s$ and the update step can be omitted (§1.1, §3.1). **Stated**
5. Combining projection-based model reduction with implicit Runge–Kutta time integration is new; the cost of the all-stage nonlinear system, which has limited IRK in full-order FSI, matters much less at reduced order, where port reduction allows direct solvers (§1.2). **Stated**
6. The semi-discrete FSI system (10) can be written as a DAE $y'=f(t,y,w)$, $0=g(t,y)$ with $y$ collecting the masked fluid and solid momenta and the solid displacement, and $w=p_f$ (§2.3, Eq. (11)). **Derived**
7. The fully discrete Runge–Kutta FSI system obtained from the coupled DAE is algebraically equivalent to applying the method separately to the fluid DAE and the solid ODE and imposing the interface conditions with mask matrices (§3.1, Appendix A). **Derived**
8. The structural stage velocities are $U_s=\frac1h(A^{-1}\otimes I)D_s-\frac1h\big((A^{-1}\mathbf 1)\otimes I\big)d_{s,n}=:\mathcal D_{s,h}D_s$, which needs $A$ invertible (§3.1, Eq. (18)). **Derived**
9. The all-stage monolithic system has the structure of the BDF–Newmark implicit FSI system with $s$ times more equations and unknowns (§3.1). **Stated**
10. Newton on the all-stage system is solved by static condensation: local fluid and solid updates written in terms of the interface increment $\delta g_\Gamma$, then a Schur-complement system $S_{\mathrm{sc}}\delta g_\Gamma=R_{\mathrm{sc}}$ (§3.2, Eqs. (23)–(24)). **Derived**
11. Each such Newton step equals the SQP step for minimizing $\lVert R_\Gamma\rVert_2$ subject to the local residual equations; this form extends to non-conforming interface grids (§3.2, Eq. (25)). **Stated**
12. Lemma 4.2: for an isolated system the semi-discrete ROM satisfies $\frac{d}{dt}(\hat T_f+\hat T_s+\hat W_s)+D_f(\hat u_f)=0$ (§4.2, Eq. (29)). **Derived** (proof omitted; no fully discrete energy estimate)
13. The fully discrete ROM equals the same Runge–Kutta method applied to the semi-discrete ROM: projection and time discretization commute (§4.3, Remark 4.3). **Stated**
14. The bubble–port construction makes basis enrichment unnecessary; the existing well-posedness theory covers only coercive problems, so the claim for saddle-point FSI rests on numerics (Remark 4.4). **Stated** / **Shown**
15. Vertical beam, full order: Radau IIA with $s=2,3,4$ and $h=0.025,0.05,0.10$ against an $s=4$, $h=0.001$ reference gives $H^1$ solid-displacement errors $7.09\times10^{-5}$, $2.22\times10^{-4}$, $1.32\times10^{-3}$ ($s=2$); $3.81\times10^{-6}$, $6.55\times10^{-5}$, $1.04\times10^{-4}$ ($s=3$); $8.52\times10^{-7}$, $6.38\times10^{-6}$, $1.07\times10^{-4}$ ($s=4$) (§5.1.1, Table 1). **Shown**
16. The fitted temporal rates are about 2.1, 2.4 and 3.5 for $s=2,3,4$, below the formal order $2s-1$; the authors attribute this to the DAE structure and the interaction with spatial discretization, ALE motion and iterative interface coupling (§5.1.1). **Shown** (attribution **Stated**)
17. Turek FSI3, full order: Radau IIA $s=2$ with $h=0.01$ gives periodic drag, lift and total energy after the transient, with bounded energy (Fig. 9). **Shown**
18. BDF2 with Newmark ($\beta_{\mathrm N}=1/4$, $\gamma_{\mathrm N}=1/2$) is unstable on Turek FSI3: force amplitudes and total energy grow (Fig. 10). **Shown**
19. Damped Newmark ($\beta_{\mathrm N}=1/3$, $\gamma_{\mathrm N}=3/5$, within $2\beta_{\mathrm N}\ge\gamma_{\mathrm N}\ge1/2$) removes the instability, but the total energy is significantly lower than with Radau IIA (about 2.675 against 2.69), "consistent with the observation that IRK schemes are less dissipative" (Fig. 11). **Shown**
20. For $s=2,3,4$ and $h=0.01,0.02$ the drag mean is 0.436 in all six runs, the lift half-amplitude 0.1619–0.1676, and the dominant frequency essentially identical (§5.2.1, Table 2, Fig. 12). **Shown**
21. A tighter POD tolerance gives smaller relative ROM errors with more modes (Figs. 5, 14, 18, 24, 29). **Shown**
22. A Turek ROM trained on $t\in[30,33]$ and run on $[30,39]$ reproduces forces, energy and spectra for POD tolerances $10^{-7}$ and $10^{-6}$ with $s=2$, $h=0.01$ and $s=3$, $h=0.02$ (§5.2.2). **Shown**
23. With the same POD basis, the ROM advanced by Radau IIA ($s=2$) is stable and follows the full model, while the ROM advanced by BDF2–Newmark is unstable "irrespective of numerical (Newmark) damping" (§5.2.2, Fig. 17). **Shown**
24. Parametric Turek ROMs in viscosity and mass ratio are stable and accurate, but parametric dependence greatly increases the number of POD modes (§5.2.2, Figs. 19–22). **Shown**
25. High-order Radau IIA with displacement-based interface coupling "significantly improves the numerical stability of the reduced-order model" (§6). **Shown** (two test cases)
26. No timings, speed-ups or CPU costs are reported (whole paper). **Stated** (observation of the reader)

# Printed slips

- Table 1 caption: "time steps ∆t = 0.20, 0.10, 0.05"; the table header and §5.1.1 give 0.025, 0.05, 0.10.
- Table 1 against the text: "an accuracy gain is observed when increasing the number of stages", but at $h=0.10$ the $s=4$ error ($1.07\times10^{-4}$) exceeds the $s=3$ error ($1.04\times10^{-4}$); the local $s=3$ rate is about 0.67 on the coarse pair and 4.1 on the fine pair, so the fitted "2.4" hides non-monotone behaviour.
- Eq. (16), last line: "$P_{f,dir}d_s^{(n+c_i)}=d_{f,dir}^{(n+c_i)}$" for the solid Dirichlet mask $P_{s,dir}$ and data $d_{s,dir}$.
- Eq. (21): $R_{f,in}$ contains "$\mathbf B_{f,\Gamma}U_f$" where the stacked divergence is $\mathbf B_f$ elsewhere.
- §4.1: pressure POD "based on the $L^2(\tilde\Omega_s)$ inner product"; the pressure lives on the fluid domain $\tilde\Omega_f$.
- §5.2.1: the text says the BDF2–Newmark energy grows, but Fig. 10 shows only $t\in[43,45]$, where no trend is visible.
- Symbol reuse: $g$ is both the constraint of Eq. (11) and the interface displacement of Eq. (20); $\beta$ is both the port coordinates and the Newmark parameter.
- Typos: "drag and lifted forces" (Fig. 21), "perperdicularly" (§5.1).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Delta t$ | $h$ | step size |
| $y^{(n)}$ | $y_n$ | numerical solution |
| $t^{(n+c_i)}$, $y^{(n+c_i)}$ | $t_n+c_ih$, $Y_i$ | stage times and stage values |
| $k_i$ | $k_i=f(t_n+c_ih,Y_i)$ | stage derivatives, eliminated |
| $s$, $(A,b,c)$, $\mathbf 1_s$ | $s$, $(A,b,c)$, $\mathbf 1$ | agree |
| $\dot y=f(t,y,z)$, $0=g(t,y)$ | $y'=f(t,y,w)$, $0=g(t,y)$ | **$z$ collides** with the registry $z=h\lambda$; $w$ as on the DAE page |
| $M_f(t)$, $M_s$ | kept | fluid (ALE, time-dependent) and solid mass matrices; the method acts on $M_fu_f$ |
| $D_s$, $U_s$ | kept | stage-stacked solid displacements and velocities |
| $\mathcal D_{s,\Delta t}$ | $\mathcal D_{s,h}$ | discrete time-differentiation operator built from $A^{-1}$ |
| $g:=\mathbf P_{s,\Gamma}D_s$ | $g_\Gamma$ (page-local) | interface displacement; **collides** with the constraint $g$ |
| $j$ | kept | Newton index; **collides** with the Butcher index $j$ |
| $\beta$, $\gamma$ (§5.2.1) | $\beta_{\mathrm N}$, $\gamma_{\mathrm N}$ | Newmark parameters; **collide** with the registry $\beta_j$ and $\gamma$ |
| $\beta$, $\alpha_f$, $\alpha_s$, $\alpha_p$ (§4) | kept | reduced coordinates; **not** the registry $\alpha_{ij}$ |
| "IRK3" | Radau IIA, $s=2$ | third order |

# Reference list

The paper prints 67 references in numbered Elsevier style ([1]–[67]). The list is
merged complete into the [bibliography](/bibliography.md) with `citedby` this slug.
[7] (Sun et al. 2021, cardiovascular FSI) would take the key of the ingested source
`sun-2021`, a different work, and is keyed `sun-2021-b`. [3] (Wang et al. 2016) is
`wang-2016-d`, because the bibliography already held other Wang 2016 works. [36] is the
1991 first edition of Hairer–Wanner II (`hairer-1991`), and [37] is the ingested
[Abu-Labdeh et al. (2023)](/sources/abulabdeh-2023.md). [12] and [23] are book chapters,
[20] has an article number without volume, [30] is an AIAA conference paper, [64]
lecture notes with a URL, and [43] has the first author "R. R. Craig Jr". No printed
duplicates and no unparseable items.

# Pages created or updated

Chunk 3 (2026-10-19). This source is cited on:

* [A-, L-, A(α)- and algebraic stability](/properties/a-stability.md)
* [Backward differentiation formulas (BDF)](/methods/backward-differentiation-formula.md)
* [Differential-algebraic equations and their Runge–Kutta treatment](/definitions/differential-algebraic-equation.md)
* [Flow past a cylinder (Schäfer–Turek)](/benchmarks/flow-past-cylinder.md)
* [Fully implicit collocation Runge–Kutta methods (Gauss, Radau IIA, Lobatto IIIC)](/methods/fully-implicit-runge-kutta.md)
* [Linear multistep methods](/methods/linear-multistep-method.md)
* [Newmark method](/methods/newmark-method.md)
* [Order reduction](/definitions/order-reduction.md)
* [Solving the stage equations of implicit Runge–Kutta methods](/methods/implicit-stage-solvers.md)
* [Stiff accuracy](/properties/stiff-accuracy.md)
