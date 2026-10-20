---
type: Source
title: "Pulicani et al. (2026) — A new hybrid strongly coupled multi-time step approach with enhanced robustness for fluid structure interaction problems"
description: "A non-iterative, strongly coupled partitioned scheme for compressible fluid–structure interaction: explicit Runge–Kutta finite volumes for the fluid and implicit Newmark for the structure, glued by Lagrange multipliers on the interface velocity through the Gravouil–Combescure free/link split, with fluid subcycling stable up to step ratio 300."
resource: "doi:10.1016/j.cma.2025.118717"
source_kind: paper
authors: [Pulicani R., Brun M., Allain O., Gravouil A.]
year: 2026
venue: "Comput. Methods Appl. Mech. Engrg. 452:118717"
local_file: "/home/stefano/papers/mosaic/ode-integration/2026_Crossref_Computer_Methods_in_Applied_Mechanics_and_Engineering_Pulicani_A_new_hybrid_strongly_coupled_multi-time_step_approach_with.pdf"
tags: [local-time-stepping, multirate, partitioned, fluid-structure-interaction, ssp]
timestamp: 2026-10-20T16:00:00Z
---

# Summary

The paper builds a strongly coupled but non-iterative partitioned scheme
for inviscid compressible fluid–structure interaction in the ALE frame. The
fluid (Euler equations, vertex-centred finite volumes, Roe flux, MUSCL) is
advanced explicitly by forward Euler ("RK1") or by the Shu–Osher SSPRK(3,3)
method ([SSP Runge–Kutta](/methods/strong-stability-preserving-runge-kutta.md)).
The linear-elastic structure (finite elements) is advanced implicitly by
the [Newmark](/methods/newmark-method.md) constant-average-acceleration
scheme ($\beta_{\mathrm N}=\frac14$, $\gamma_{\mathrm N}=\frac12$).
"Hybrid explicit/implicit" here means different integrators on different
subdomains, not an additive IMEX splitting of one right-hand side.

Lagrange multipliers enforce continuity of the normal velocity at matching
interface nodes. Following the Gravouil–Combescure method, each
subdomain's end-of-step velocity is split into a "free" part, computed
without interface forces, and a "link" part, linear in the multiplier
$\Lambda$. The velocity constraint then becomes a small interface problem
$(H^{\mathrm f}+H^{\mathrm s})\Lambda=-L^{\mathrm f}u_{\mathrm{free}}-L^{\mathrm s}v_{\mathrm{free}}$,
with $H^{\mathrm f}$ diagonal and $H^{\mathrm s}$ built from an effective
mass factored once. With SSPRK(3,3) the interface problem is solved at each
stage. The multi-time-step version ([local time stepping](/methods/local-time-stepping.md)
across subdomains) lets the fluid take $m$ fine steps $h=H/m$ per
structure step $H$. The structure free velocity is interpolated linearly,
an interface problem is solved at each fine step, and no subiteration over
the coarse step is performed. This is multirate in the structural-dynamics
domain-decomposition tradition, not of [multirate GARK](/methods/multirate-gark.md)
type.

The evidence is numerical: a moving-wall half shock tube (observed order
about 2), a piston–rod problem, a shock wave on a deforming panel against
experiment, and 2D supersonic panel flutter. A conventional serial
staggered scheme becomes unstable for $m>5$ on the piston–rod problem,
while the multiplier scheme stays stable up to $m=300$, with spurious
interface energy below 2 %. The flutter onset lies between Mach 2.24 and
2.25 both for $m=1$ and $m=150$.

# Version read

HAL deposit hal-05455877v1 (submitted 13 January 2026), the author
manuscript in Elsevier preprint layout under CC BY-NC-ND 4.0, not the
journal-typeset version of record. 43 PDF pages (HAL cover, 37 pages of
text, Appendix A, 4 pages of references), all read; pp. 15–17, 22–23 and
39 were checked visually where the text layer garbled equations. The HAL
cover prints the DOI, and page 1 matches Crossref (title, authors, journal,
volume, article number). Equation and section numbers on this page are
those of the HAL manuscript.

# Key claims

Notation (see the notation map): $H$ the structure (coarse) step and
$h=H/m$ the fluid (fine) step (the source's $\Delta t^s$, $\Delta t^f$);
$m$ the step ratio; $\beta_{\mathrm N}$, $\gamma_{\mathrm N}$ the Newmark
parameters; $M$, $K_{\mathrm s}$ the structural mass and stiffness and
$\tilde M=M+\beta_{\mathrm N}h^2K_{\mathrm s}$; $\Lambda$ the discrete
multiplier; $L^{\mathrm f}$, $L^{\mathrm s}$ the constraint matrices;
$H^{\mathrm f}$, $H^{\mathrm s}$ the condensed interface operators.

1. The coupling is hybrid explicit (fluid RK1 or SSPRK(3,3)) and implicit (structure Newmark), strongly coupled through multipliers on the normal velocity, with fluid subcycling, and "non-iterative in the sense that it does not require any subiteration" (Abstract, §4.4). **Stated** (design property)
2. To the authors' knowledge the only earlier multiplier-based finite-volume/finite-element coupling with velocity constraints is that of Casadei and Leconte, fully explicit (forward Euler fluid, central-difference structure) (§1). **Stated**
3. In structural domain decomposition "it has been proved, through the energy method, that kinematic continuity must be prescribed in terms of velocity to guarantee the stability of the multi-time step algorithms, for any Newmark time integration schemes with their own time step", extended to generalized-α by heterogeneous asynchronous time integrators (HATI) (§1). **Stated** (cited)
4. The free/link split $u=u_{\mathrm{free}}+u_{\mathrm{link}}$, $v=v_{\mathrm{free}}+v_{\mathrm{link}}$, with link parts linear in $\Lambda$, reduces the coupled step to $(H^{\mathrm f,n+1}+H^{\mathrm s,n+1})\Lambda^{n+1}=-L^{\mathrm f,n+1}u^{n+1}_{\mathrm{free}}-L^{\mathrm s,n+1}v^{n+1}_{\mathrm{free}}$ (Eqs. (46)–(49)). **Derived**
5. $H^{\mathrm f}$ is diagonal, $H^{\mathrm f}_{ii}=h/(\rho_i^{n+1}C_i^{n+1})$ with $C_i$ the dual-cell measure (Eq. (41)); the multiplier flux has no density component, so $\rho^{n+1}$ is known before $\Lambda$ (remark after Eq. (35)). **Derived**
6. $H^{\mathrm s}=\gamma_{\mathrm N}hL^{\mathrm s}\tilde M^{-1}L^{\mathrm s\top}$ is full, but $\tilde M$ is constant, so its inverse is computed once; only $L^{\mathrm s}$ changes with the interface normals (Eqs. (26), (45), §3.5.3). **Derived**
7. With SSPRK(3,3) the interface problem is solved at each of the three stages (Eq. (54)), the mid-stage structure free velocity being $v^{n+1/2}_{\mathrm{free}}=\frac12(v^n_{\mathrm{free}}+v^{n+1}_{\mathrm{free}})$ (Eq. (55)). **Derived**
8. In subcycling, $v^j_{\mathrm{free}}=\frac{m-j}{m}v^0_{\mathrm{free}}+\frac jmv^m_{\mathrm{free}}$ (Eq. (57)), and an analogous interpolation is "assumed" for the free acceleration (Eq. (58)). **Derived** (Eq. (58) is an assumption)
9. Extrapolating the interface mesh at each fine step from the free kinematics corrected by $\Lambda^{j-1}$ (Eqs. (59)–(60)) "ensures stability without requiring cycling over the coarse time step" and "allows for large time step ratios" (§4.4). **Shown**
10. The multiplier-based moving-wall flux reproduces the analytical half-Riemann solutions for wall velocities $\pm1$ about as well as the classical sliding-wall flux; the classical flux has larger artifacts in compression, the multiplier flux in expansion (§5.2, Figs. 5–6). **Shown**
11. For the smooth piston motion $u_p(t)=t\sin(t^2)$, the observed orders are 2.087 in time (at fixed CFL 0.5, so $\Delta x$ shrinks with $h$) and 2.064 in space: "second-order of accuracy in both time and space" with SSPRK(3,3) and MUSCL (§5.2, Eq. (64), Fig. 7). **Shown**
12. Piston–rod problem: with one step the conventional serial staggered scheme and the multiplier scheme agree; with subcycling the staggered scheme has stability issues for $m>5$, while the multiplier scheme stays stable at $m=300$ (§5.3, Figs. 9–10). **Shown**
13. With the multiplier scheme, $m=50$ matches the single-step result, and $m=100$ and $300$ are less accurate, attributed to the coarse structural step ($m=100$ gives $H=1.25\times10^{-3}$ s, "only ten time steps with respect to the third-mode period") (§5.3). **Shown**
14. The spurious interface energy for $m=50$ is 0.4 % of the maximum external energy at final time; it grows with time, stays below 2 % for the ratios tested, and is dissipative (§5.3, Fig. 11). **Shown**
15. Time convergence of the coupled piston–rod problem under a smooth load: observed order 2.001 for the structure and 1.41 for the fluid (§5.3, Fig. 12). **Shown**
16. Shock wave on a deforming panel (Giordano et al. 2005): the single-step scheme matches the measured top displacement and upstream pressure (§5.4, Fig. 15). **Shown**
17. With subcycling, near-perfect agreement up to $m=100$; spurious energy below 1 % of the interface energy exchange at $m=100$; mean relative displacement error below 0.5 % for $m\le100$, growing roughly linearly in $m$ up to about 100 and faster beyond (§5.4, Figs. 16–17, Eq. (67)). **Shown**
18. Supersonic panel flutter: decaying response below Mach 2.24, limit-cycle flutter from Mach 2.25, with amplitude increasing with Mach (§5.5, Fig. 21). **Shown**
19. The single-step multiplier scheme converges faster under mesh refinement than the staggered scheme at Mach 2.23 and is more accurate in phase and amplitude on the coarse mesh (§5.5, Fig. 22). **Shown**
20. The flutter response is captured with $m=100$, 150 and 200, with the same instability threshold (Mach 2.24–2.25) at $m=150$ (§5.5, Figs. 23, 27). **Shown**
21. Interface-mesh extrapolation over the coarse step (Eq. (61)) gives a larger, "not necessarily dissipative" spurious interface energy than the fine-step extrapolation (Eq. (60)) (§5.5, Fig. 26). **Shown**
22. "As classically observed when coupling subdomains using the GC method, the proposed multi-time step approach only introduces a controlled energy dissipation, while preserving the numerical stability" (§6). **Shown** (numerically; no proof here)
23. Constant average acceleration "has the advantage of being unconditionally stable, second-order accurate, and without numerical dissipation" (§3.4). **Stated**
24. SSPRK(3,3) "exhibits a greater stability than the previous RK1 scheme when combined with the MUSCL strategy" (§4.3). **Stated**

*(Compiler caveats, not in the sources.)* The observed order about 2 with a
third-order Runge–Kutta method is a combined space–time error at fixed
CFL, and the fluid reaches only 1.41 in the coupled case; the stage-wise
multipliers (link weights 1, 1/2, 1 against the flux weights of
SSPRK(3,3)) and the interpolated mid-stage structure velocity are not
analysed for order. Energy-based stability is proved only in the cited
structural-dynamics works; for this Runge–Kutta–Newmark coupling it is
shown numerically.

# Printed slips

1. Eq. (52), stage 2, p. 15: "$u^2_{free,i}=\dots+\frac{\Delta t}{4\rho^2_iC^{n+1/2}_i}\left(\phi^{u,1}_i+\phi^{\rho,0}_i\right)$" (checked visually) — by consistency with $U^2_{free}$, which uses $\Phi^0_i+\Phi^1_i$, it should be $\phi^{u,0}_i+\phi^{u,1}_i$; a density flux added to a momentum flux is dimensionally inconsistent.
2. Eq. (53), stage 3: the free state is labelled $U^3_{free,i}$ but its velocity $u^{n+1}_{free,i}$ (harmless), and the flux is printed "$\Phi_{Roe}(U^2_i,U^2_k,,n^{f,2}_{i,k},w^{f,2}_{i,k})$" with a double comma.
3. Eq. (4), p. 4: "$p=(\gamma-1)\left(\rho E+\frac12\rho\|u\|^2\right)$" — the sign must be minus (checked visually).
4. Eq. (21), p. 8: "$w^{f,n+1}=w^{f,n+1}.n^{n+1}=\frac{A_{swept}}{l^n_{edge}}\Delta t$" — dimensional consistency requires $\frac{A_{swept}}{l^n_{edge}\Delta t}$ (checked visually).
5. §1: "A popular popular family of staggered algorithms" (doubled word; the sentence lacks a verb).
6. Fig. 10(a) caption: "Different time step ration m".
7. Ref. [59] prints "B. Van Leer, Efficient implementation of essentially non-oscillatory shock-capturing schemes., J. Comp. Phys. 77 (2) (1988) 439–471"; that work is by C.-W. Shu and S. Osher, the "Shu scheme" the paper names.
8. Ref. [49] (Roe, "Approximate riemann solvers…") prints "J. Comp. Phys. 135 (2) (1981) 250–258", mixing the 1997 reprint (vol. 135, pp. 250–258) with the 1981 original (vol. 43, pp. 357–372).
9. Ref. [61] prints the authors as "H. G. Boniface Nkonga" (garbled; [50] carries the same title); refs. [8] and [9] carry identical titles; [37] prints pages "43–44" and [35] pages "116–134" (implausible; likely the article number 116134); [20] prints "K. V. der Zee".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Delta t^s$, $\Delta t^f$, $\Delta t$ | $H$, $h=H/m$, $h$ | structure (coarse) and fluid (fine) steps; multirate convention of the registry |
| $m$ | $m$ | step ratio; agrees |
| $n$, $j$ | $n$, $j$ | coarse step index and fine index $j=1,\dots,m$; the registry micro index $\ell$ is not used to keep the printed equations |
| **$\beta$, $\gamma$** | $\beta_{\mathrm N}$, $\gamma_{\mathrm N}$ | Newmark parameters, as on the [Newmark page](/methods/newmark-method.md); **$\gamma$ also** the heat-capacity ratio in Eq. (4) and $\gamma_s$ in Eq. (59) |
| $M$ | $M$ | structural (consistent) mass matrix; agrees |
| **$K$** | $K_{\mathrm s}$ | structural stiffness; **collides** with the registry iteration count $K$ |
| $\tilde M=M+\beta\Delta t^2K$ | $\tilde M=M+\beta_{\mathrm N}h^2K_{\mathrm s}$ | effective mass |
| $d$, $v$, $a$ | kept | structure displacement, velocity, acceleration |
| $U_i$, $C_i$, $u$ | kept | fluid conservative state, dual-cell measure, fluid velocity |
| $U^1$, $U^2$; $\Phi^0,\Phi^1,\Phi^2$ | $Y_i$-type stage values; stage tendencies | SSPRK(3,3) in increment form on moving cells |
| **$J$** | kept (page-local) | Jacobian of the ALE map; **not** the registry Jacobian $\partial f/\partial y$ |
| $\Lambda$, $\lambda$ | kept | discrete and continuous multipliers (interface pressure); **$\lambda$ is not** the registry eigenvalue |
| $L^f$, $L^s$ | $L^{\mathrm f}$, $L^{\mathrm s}$ | constraint matrices; **not** the registry linear operator $L$ |
| $H^f$, $H^s$ | $H^{\mathrm f}$, $H^{\mathrm s}$ | condensed interface operators; **not** the macro step $H$ |
| $w^f$ | kept | mesh velocity, fixed by the discrete geometric conservation law |
| RK1, RK3 ("Shu") | forward Euler, SSPRK(3,3) | |
| CFL | $\nu$ | Courant number, Eq. (66) |
| CSS, GC, HATI | kept | conventional serial staggered; Gravouil–Combescure; heterogeneous asynchronous time integrators |

# Reference list

65 printed references, numbered [1]–[65]. The list is merged complete into
the [bibliography](/bibliography.md) with `citedby` pulicani-2026. Same-key
works take suffixes in printed order: Michler et al. 2003 ([14], [15]) and
Farhat et al. 1994 ([41], [42]). Ref. [59], printed under the author Van Leer
(1988), is Shu and Osher's paper and is merged into its existing entry
`shu-1988`, whose note records the printed author; [25] (Li, Combescure &
Leboeuf 2013) is keyed `li-2013-b`, distinct from an unrelated Li 2013
entry; [49] is kept
as printed with its mixed volume and year; [61] has a garbled author
string; [3] gives a book title as chapter title; [26] is a Collège de France
seminar entered as proceedings. There are no printed duplicates; all items
were parsed.

# Pages created or updated

Chunk 4 (2026-10-20). This source is cited on:

* [Local time stepping](/methods/local-time-stepping.md)
* [Multirate GARK methods (MrGARK, compound-fast, multirate backward Euler)](/methods/multirate-gark.md)
* [Newmark method](/methods/newmark-method.md)
* [Strong-stability-preserving (SSP) Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md)
