---
type: Source
title: "Fujiwara et al. (2023) — Fully conservative and pressure-equilibrium preserving scheme for compressible multi-component flows"
description: "Derives a discrete compatibility condition for pressure equilibrium in multi-component flows with any equation of state and solves it for ideal-gas mixtures, giving central fluxes (FC/PE) that conserve species mass, momentum and total energy with no extra equation and keep pressure and velocity equilibrium at smooth interfaces."
resource: "doi:10.1016/j.jcp.2023.111973"
source_kind: paper
authors: [Fujiwara Y., Tamaki Y., Kawai S.]
year: 2023
venue: "J. Comput. Phys. 478:111973"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Journal_of_Computational_Physics_Fujiwara_Fully_conservative_and_pressure-equilibrium_preserving_schem.pdf"
tags: [multiphase, kinetic-energy-preserving, central-scheme, numerical-flux, finite-difference]
timestamp: 2026-10-23T23:00:00Z
---

# Summary

For flows in which the ratio of specific heats varies (multi-component
ideal-gas mixtures, supercritical fluids), the conventional fully conservative
schemes for the
[multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)
produce spurious pressure oscillations at material interfaces, even smooth
ones. Fujiwara et al. survey the known remedies, which each give up
something. Karni's pressure-equation scheme and Abgrall's transport of
$\mathsf G=1/(\gamma-1)$ are not conservative. The
[double-flux methods](/methods/double-flux-method.md) carry an extra
transport equation and so, in the authors' words, overspecify the system,
with two discrete values of pressure or of species mass.

The authors derive the analytical
[pressure-equilibrium](/properties/pressure-equilibrium-preservation.md)
condition for any equation of state, a chain-rule identity between the
transport of $\rho e$ and of the partial densities $\rho Y_k$. Its discrete
analog is a *compatibility condition* on the half-point values used in
the fluxes. For ideal gases they solve it for two species and then for
$N_{\mathrm s}$ species. The solution weights the partial densities with
coefficients $\mathsf w^\pm$, built from the mixture molar mass and the density,
and averages $\mathsf G$ arithmetically. In a second-order central flux form
this gives two flux sets. FC/PE (S) is a [split form](/methods/split-convective-forms.md)
that reduces to Shima et al.'s KEEP-PE scheme for one component. FC/PE (D)
is a divergence form that reduces to the standard divergence scheme. Both
are fully conservative (no extra equation) and keep pressure equilibrium
when the velocity is uniform. A nonuniform-velocity analysis shows that
only FC/PE (S) satisfies the extended condition, which explains why
FC/PE (D) diverges in long runs.

The tests are [smooth material-interface advection](/benchmarks/material-interface-advection.md)
problems: 1D with two species, 2D with three species, and 2D with a
tangential velocity jump. FC/PE (S) holds pressure and velocity
equilibrium to about $10^{-13}$ in 1D and $10^{-12}$ in 2D, and it conserves
mass and energy exactly. An appendix extends the construction to the
stiffened-gas equation of state, without tests. Shocks and sharp interfaces
are out of scope: the scheme is a non-dissipative baseline to which
numerical diffusion is still to be added.

# Version read

Version of record (Elsevier typeset; received 16 Jun 2022, revised 12 Dec
2022, accepted 22 Jan 2023, online 27 Jan 2023), 23 pages, DOI printed on
page 1. Title, three authors and venue match Crossref; no identity problem.
Equation, section, table and figure numbers are those of the journal
version.

# Key claims

Registry notation: grid index $i$ (the source's $m$), velocity $v$, species
index $k$ with partial density $\rho Y_k$, species ratio of specific heats
$\gamma_k$, species molar mass $W_k$ and mixture ratio $\gamma$. Page-local
symbols: $N_{\mathrm s}$ (number of species), $\bar W$ (mixture molar mass),
$\mathsf G=1/(\gamma-1)$ (its value at node $i$ written $\mathsf G_i$) and $\mathsf G_k=1/(\gamma_k-1)$, $\mathcal J_k$ (the
Jacobian $(\partial\rho e/\partial\rho Y_k)_{p,\rho Y_{l\neq k}}$) and
$\mathcal J'_k=(\partial \mathsf G/\partial\rho Y_k)_{\rho Y_{l\neq k}}$,
$\mathsf w^\pm$ (the interface weights), and $(\cdot)|_{i+1/2}$ for a half-point
value. $\{\!\{a\}\!\}=(a_i+a_{i+1})/2$.

1. Conservative schemes for $(\rho Y_k,\rho v,E)$ with a variable ratio of specific heats produce spurious pressure oscillations at interfaces even when the interfaces and the specific heats vary smoothly, so interface-capturing diffusion is "not a fundamental solution" (§1; Figs. 2, 4, 7, 8 for NPE). **Stated** and **Shown**
2. To the authors' knowledge, no existing scheme keeps pressure equilibrium while solving only the conservation equations of species mass, momentum and total energy. The paper claims to be "the first to achieve both conservation and equilibrium", even for flows without discontinuities (§1, §6). **Stated**
3. Double-flux methods [4, 5, 12, 13] satisfy equilibrium and the primary conservation laws but overspecify the system: they give two independent pressure solutions (pressure and total-energy equations), or two species-mass solutions in [5] (§1). **Stated**
4. For any equation of state $\rho e=\rho e(p,\rho Y_k)$ and initially constant $p_0$, $v_0$, pressure equilibrium $\partial_tp=0$ requires $\partial_x(\rho e)=\sum_k\mathcal J_k\,\partial_x(\rho Y_k)$ (§2.3, Eqs. (5)–(12)). Velocity equilibrium follows from the species equations alone (Eq. (10)). **Derived**
5. For ideal gases ($\rho e=p\mathsf G$) the condition reduces to the known equilibrium condition of Abgrall et al., the advection $\partial_t\mathsf G+v_0\partial_x\mathsf G=0$ (Eq. (15)), with the spatial form Eq. (16) (§2.3, Eqs. (13)–(16)). **Derived**
6. In the half-point flux form (Eq. (17)) with constant $p_0$, $v_0$, velocity equilibrium holds discretely for any half-point density (Eq. (18)). Pressure equilibrium requires Eq. (20), equivalent to the **compatibility condition** (21), $\rho e|_{i+1/2}-\rho e|_{i-1/2}=\sum_k\mathcal J_k|_i\big(\rho Y_k|_{i+1/2}-\rho Y_k|_{i-1/2}\big)$ (§3.2). **Derived**
7. Splitting Eq. (21) into the two one-sided relations (22)–(23) is sufficient. Requiring a single interface value $\rho e|_{i+1/2}$ (local conservation) eliminates it and gives Eq. (25), valid for any equation of state (§3.3.1). **Derived**
8. For two ideal-gas species, Eq. (25) becomes Eq. (34), a bilinear condition on $\rho Y_1|_{i+1/2}$ and $\rho Y_2|_{i+1/2}$; once one is chosen the other is unique (Eq. (36)) (§3.3.1–3.3.2). **Derived**
9. The half-point values $\rho Y_k|_{i+1/2}=\tfrac12\big(\mathsf w^-\rho Y_{k,i}+\mathsf w^+\rho Y_{k,i+1}\big)$, with $\mathsf w^+=\frac{\bar W_{i+1}\rho_i}{\rho_{i+1}\bar W_i}$ and $\mathsf w^-=1/\mathsf w^+$, satisfy Eq. (34) and yield $\mathsf G|_{i+1/2}=\{\!\{\mathsf G\}\!\}$ from Eq. (22) (Eqs. (38)–(39)). They are the continuous choice consistent with the singular limit (37) (§3.3.2). **Derived**. Substituting (38) into the right-hand side of (35) and using $\mathsf w^+\mathsf w^-=1$ returns its left-hand side exactly *(compiler check, not in the sources)*.
10. For $N_{\mathrm s}$ species the compatibility condition (40) reduces to Eq. (47), "an identical equation for each $i,j$ component", and the same half-point form (Eq. (48)) satisfies it for every species (§3.3.3). **Derived**
11. The total-mass half-point value is then $\rho|_{i+1/2}=\tfrac12(\mathsf w^-\rho_i+\mathsf w^+\rho_{i+1})$ (Eq. (49)). Solving $(\rho,\rho v,E,\rho Y_k)$ with $k\le N_{\mathrm s}-1$ and this $\rho|_{i+1/2}$ is discretely equivalent to solving $(\rho Y_k,\rho v,E)$ (§3.3.3, Appendix A, Eq. (A.14)). **Derived**
12. Two complete flux sets satisfy the compatibility condition (Table 1). FC/PE (S) reduces to KEEP-PE [30] for one component, and FC/PE (D) reduces to the standard divergence scheme. Both are central and second order, and "higher-order accuracy may be achieved by increasing the number of stencils", as for the high-order KEEP scheme [27] (§3.4). **Stated** (the higher-order extension is not built)
13. Away from interfaces ($Y_k$ constant) $\mathsf w^\pm=1$ and the fluxes reduce to standard central forms, so FC/PE (S) behaves as KEEP-PE "without any special treatment such as switching fluxes by sensors" (§3.4). **Derived**
14. 1D two-species advection, 501 points, RK4, "CFL number of 0.05 ($\Delta t=10^{-4}$)": at $t=1.0$ FC/PE (S) and FC/PE (D) keep velocity and pressure equilibrium "at a sufficiently small order ($\simeq10^{-13}$)", while NPE shows spurious oscillations (§4.1, Fig. 2). **Shown**
15. In the same problem the pressure error of FC/PE (D) grows quickly and the run diverges near $t=3.8$. FC/PE (S) shows no error growth up to $t=6.0$, and in Fig. 5 up to $t=20$. NPE blows up near $t=6.5$ (§4.1, Figs. 3–5). **Shown**
16. Conservation to $t=20$ (Fig. 5): FC/PE (S), FC/PE (D) and NPE conserve $E$ and $\rho Y_1$ exactly. NC-p (pressure equation [1]) does not conserve total energy, and NC-G (transport of $\mathsf G$ [2]) does not conserve species mass. FC/PE (S) is "the only one that satisfies both the conservation and pressure-equilibrium preservation for a long time" (§4.1). **Shown**
17. 2D three-species circular interface, $501^2$ points: at $t=5.0$ FC/PE (S) keeps pressure and velocity equilibrium at $\simeq10^{-12}$, while NPE blows up near $t=5.5$. Applied dimension by dimension, the scheme works in multi-D with more than two species (§4.2, Fig. 7). **Shown**
18. 2D two-species advection with a tangential velocity jump [10]: at $t=5.0$ FC/PE (S) keeps pressure equilibrium and advects the tangential velocity correctly, and NPE produces pressure and velocity oscillations (§4.3, Fig. 8). **Shown**
19. With a nonuniform velocity the compatibility condition becomes Eq. (55), $(\mathsf G v)|_{i+1/2}-(\mathsf G v)|_{i-1/2}=\sum_k\mathcal J'_k|_i\big((\rho Y_kv)|_{i+1/2}-(\rho Y_kv)|_{i-1/2}\big)$ (§5). **Derived**
20. FC/PE (D) violates Eq. (55): its left side is Eq. (56) and its right side, Eq. (57), carries an extra $-\mathsf G_i(v_{i+1}-v_{i-1})/2$, so the sides differ "with assuming the pressure is constant". It therefore keeps equilibrium only for an exactly constant velocity, and round-off velocity disturbances make it diverge (§5, Eqs. (56)–(57)). **Derived**
21. FC/PE (S) satisfies Eq. (55) for any velocity. Both sides equal $\tfrac12\big[\tfrac{(\mathsf G v)_{i+1}-(\mathsf G v)_{i-1}}2+\mathsf G_i\tfrac{v_{i+1}-v_{i-1}}2+v_i\tfrac{\mathsf G_{i+1}-\mathsf G_{i-1}}2\big]$ (Eqs. (58)–(59)), and the authors recommend FC/PE (S) (§5). **Derived**
22. The construction carries over to the stiffened-gas equation of state $\rho e=p\mathsf G+\mathsf A$, $\mathsf A$ mixed from $\mathsf A_k=\gamma_kp_{\infty,k}/(\gamma_k-1)$. The extra part obeys a condition of the same form (Eq. (B.8), with $\mathsf G_k\to \mathsf A_k$), the half-point $\rho Y_k$ is unchanged, $\mathsf A|_{i+1/2}$ is the arithmetic mean, and the internal-energy flux is $\{\!\{\rho e\}\!\}\{\!\{v\}\!\}$ (Appendix B, Eqs. (B.9)–(B.10)). **Derived** (not tested)
23. Sharp interfaces and shocks require "properly designing and adding numerical diffusion terms" to the scheme, and fluxes for more complex equations of state are left to future work (§1, §3.3.1). **Stated**

# Printed slips

- §4.1–4.3: "CFL number of 0.05 ($\Delta t=10^{-4}$)". With $\Delta x=1/500$ and $v_0=1$, $v_0\Delta t/\Delta x=0.05$. In the pure species-2 region of the 1D test, $c=\sqrt{1.66\cdot0.9/0.2}\approx2.73$, so the acoustic number $(\lvert v\rvert+c)\Delta t/\Delta x\approx0.19$. The printed CFL is therefore the convective one, which the paper does not say *(compiler check, not in the sources)*.
- §4.3: the 2D problem is set on a "periodic region [0, 1]" with $501^2$ points, and $r$ is not redefined (only $x_c=0.5$ is given, no $y_c$). §4.2 writes "periodic plane of dimension [0, 1]" for $[0,1]^2$.
- §3.2 calls $m$ "the cell index", but no cell averages are defined: the scheme is a point-value central flux form.
- Ref. [5] (Johnsen & Ham) prints "J. Comput. Phys. 231 (2006) 5705–5717", while ref. [8] of the same list prints volume 231 with the year 2012. The bibliography entry `johnsen-2012` records 2012, as printed by Bryngelson et al. (2021) and others.
- Ref. [29] prints its second author as "K. Yuichi", while refs. [25]–[28] print the same co-author as "Y. Kuya". Refs. [27] and [28] print no volume, only the article numbers 110482 and 111336.
- Typos: "Spacial discretization" (§3.1 heading), "conservaton" (§6).

# Notation map

| Fujiwara et al. 2023 | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $m$, $m\pm\frac12$ | $i$, $i\pm\frac12$ | grid point and half points |
| $\rho Y_i$, $Y_i$ | $\rho Y_k$, $Y_k$ | partial density and mass fraction of species $k$ (§10); the source's species index $i$ becomes $k$ |
| $N$ | $N_{\mathrm s}$ (local) | number of species; **collision** with the DG degree $N$ |
| $\boldsymbol u$, $u$ | $v$ | velocity; **collision** with the registry state $u$ |
| $E$, $e$, $\rho e$, $p$ | $E$, $e$, $\rho e$, $p$ | agree |
| $p_0$, $u_0$ | $p_0$, $v_0$ | equilibrium pressure and velocity |
| $M_i$, $\bar M$ | $W_k$, $\bar W$ (local) | species and mixture molar mass; **collision** with the Mach number $M$ |
| $\gamma_i$, $\bar\gamma$ | $\gamma_k$, $\gamma$ | species and mixture ratio of specific heats |
| $R_u$, $T$, $c_p$, $c_v$ | as printed | universal gas constant, temperature, specific heats |
| $G=1/(\bar\gamma-1)$, $G_i$ | $\mathsf G$, $\mathsf G_k$ (local) | **collision** with the admissible set $G$ |
| $\beta_i\vert_m$, $\beta'_i$ | $\mathcal J_k\vert_i$, $\mathcal J'_k$ (local) | Jacobians of the equation of state; **collision** with the smoothness indicators $\beta_k$ |
| $\alpha\vert_m$ (Appendix A) | — | $(\partial\rho e/\partial\rho)_{p,\rho Y_k}$, in words; **collision** with $\alpha_k$, $\alpha$ |
| $\phi^+$, $\phi^-$ | $\mathsf w^+$, $\mathsf w^-$ (local) | interface weights; **collision** with the volume fraction $\phi_k$; letter as on the [multicomponent Euler](/definitions/multicomponent-euler-equations.md) page |
| $\tilde C_i$, $\tilde M_u$, $\tilde\Pi$, $\tilde K$, $\tilde I$, $\tilde P$ | $\tilde C_k$, $\tilde M_v$, $\tilde\Pi$, $\tilde K$, $\tilde I$, $\tilde P$ (local) | fluxes of species mass, convective momentum, pressure, kinetic energy, internal energy and pressure work |
| $(a\vert_m+a\vert_{m+1})/2$ | $\{\!\{a\}\!\}$ | arithmetic mean |
| $A$, $A_i$, $\pi$, $\pi_i$ | $\mathsf A$, $\mathsf A_k$ (local), $p_{\infty,k}$ | stiffened-gas terms (Appendix B); **collision** of $A$ with the flux Jacobian |
| $\boldsymbol\delta$ | identity tensor | |
| FC/PE (S), FC/PE (D), NPE, NC-p, NC-G, KEEP, KEEP$_{\rm PE}$ | as printed | NPE is FC/PE (D) with $\mathsf w^\pm=1$ |

# Reference list

The paper prints 32 references, numbered [1]–[32]. The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` including
`fujiwara-2023`. The list prints two Johnsen 2006 works: [5] (Johnsen &
Ham, with the misprinted year) and [15] (Johnsen & Colonius, J. Comput.
Phys. 219:715–732). By volume and page, [5] is the same work as the
bibliography's `johnsen-2012` (see Printed slips). Ref. [11]
(CTR Annual Research Briefs) has no volume. Ref. [29] is recorded with its
authors as printed. No item is unparseable.

# Pages created or updated

Chunk 6 (2026-10-23). This source is cited on:

* [Double-flux method](/methods/double-flux-method.md)
* [Material-interface advection tests](/benchmarks/material-interface-advection.md)
* [Multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)
* [Pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)
* [Split convective forms](/methods/split-convective-forms.md)
* [Stiffened-gas equation of state](/definitions/stiffened-gas-equation-of-state.md)
