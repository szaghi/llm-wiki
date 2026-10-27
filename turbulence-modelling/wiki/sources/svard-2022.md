---
type: Source
title: "Svärd (2022) — Large Eddy Simulations by approximate weak entropy solutions"
description: "Proposes replacing explicit subgrid models by approximate weak entropy solutions of the compressible Navier–Stokes equations, whose fixed-support averages converge on coarse grids; states five necessary scheme conditions and a finite-volume scheme satisfying them, tested on Shu–Osher, Kelvin–Helmholtz and Taylor–Green problems."
resource: "doi:10.1016/j.jcp.2021.110737"
source_kind: paper
authors: [Svärd M.]
year: 2022
venue: "J. Comput. Phys. 448:110737"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Journal_of_Computational_Physics_Svärd_Large_Eddy_Simulations_by_approximate_weak_entropy_solutions.pdf"
tags: [implicit-les, entropy-stable, finite-volume, weak-solutions, compressible, taylor-green-vortex]
timestamp: 2026-10-27T15:49:00Z
---

# Summary

Svärd (2022) proposes to replace explicit
[LES](/definitions/large-eddy-simulation.md) subgrid models by numerical
approximations of weak (averaged) entropy solutions of the compressible
Navier–Stokes–Fourier equations, joining the theory of entropy-stable
shock capturing to turbulence simulation. A weakly convergent sequence of
numerical solutions converges when integrated against fixed test
functions, so averages over a fixed support converge on coarser grids
than point values; such averages are read a posteriori as filtered
quantities ("the LES interpretation of weak solutions"), and a functional
is accepted when refinement stops changing it. The author distinguishes
fixed-width LES, which converges to the filtered equations, from
"vanishing LES" ($\Delta\propto h$) and [implicit LES](/definitions/implicit-les.md),
which converge, if at all, to [DNS](/definitions/direct-numerical-simulation.md).

From the a priori estimates a theory of weak solutions needs, the author
conjectures five necessary conditions on a scheme: conservation form,
[entropy stability](/properties/entropy-conservation.md), at least the
diffusion of [kinetic-energy-preserving](/properties/kinetic-energy-preservation.md)
fluxes, density positivity, and a linearly stable (non-anti-diffusive)
continuity equation, plus a temperature-dependent heat conductivity
([bulk viscosity](/definitions/bulk-viscosity.md) is set to zero). The
proposed finite-volume scheme modifies Chandrashekar's
entropy-conservative, kinetic-energy-preserving flux by an artificial
diffusion on the mass flux only, reused inside the momentum and energy
fluxes; Proposition 4.1 proves the five conditions. A scaling argument
holds that upwind-type [numerical dissipation](/properties/numerical-dissipation.md)
$\nu_t\sim h|u|$ "can not be ruled out" as a subgrid model; the
[Smagorinsky model](/methods/smagorinsky-model.md) enters as the
fixed-width example. The Shu–Osher test needs no extra
[shock-capturing](/methods/artificial-viscosity-shock-capturing.md)
dissipation; in a Kelvin–Helmholtz test box averages converge for the
viscous scheme but not for its Euler version, whose fine-scale roll-ups
are amplified numerical errors; on the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
at $Re=1600$ the $64^3$ peak dissipation matches that of an earlier
second-order scheme on $129^3$. The abstract announces a
[Rayleigh–Taylor](/benchmarks/rayleigh-taylor-mixing.md) test that the
paper does not contain. The paper's "a priori" and "a posteriori" refer
to PDE estimates and to filtering before or after solving, not to
[model testing](/definitions/a-priori-and-a-posteriori-testing.md).

# Version read

Version of record (Elsevier, open access; online 11 October 2021, issue
2022), 20 pages, all read; pp. 3, 7–10, 13–16 and 18–19 also read
visually. Page 1 matches the metadata; no identity issue, but the
abstract's third test differs from the paper's (see Printed slips).
Equation, section and table numbers are those of this version.

# Key claims

Page-local symbols: $\kappa_h$ the heat conductivity; $\mathcal U=-\rho s/(\gamma-1)$
the entropy function with $s=\log(p/\rho^\gamma)$, $\boldsymbol W$ the
entropy variables; $\beta_{\mathrm C}=1/(2RT)$; $\{\!\{a\}\!\}$, $a^{\ln}$,
$[\![a]\!]=a_{i+1}-a_i$ the arithmetic mean, logarithmic mean and jump of a two-point
state at face $i+\tfrac12$; $a^\rho_{i+1/2}$ the artificial-diffusion
coefficient of the mass flux; $\mathbb B$ the averaging box of the
Kelvin–Helmholtz test; $(Re_h)_i$ the turbulent cell Reynolds number;
$\mathcal Z$ the normalized enstrophy.

1. Weak solutions satisfy the weak form and "should at least be accurate in an averaged way, which is akin to a posteriori filtering", whereas LES filters a priori (§1). **Stated**
2. For viscous Burgers the entropy estimates give convergence of a subsequence to a weak solution satisfying the entropy inequality weakly, but not weak convergence of the entropy equality (§2.1, Eqs. 4–6). **Derived**
3. Boundedness of a numerical solution is not sufficient for convergence of nonlinear problems (§2.1). **Stated**
4. With fixed filter width the grid-converged LES solves the filtered equation, not the original one; with $\Delta\propto h$ and with implicit LES a convergent solution solves the original equation, i.e. DNS (§2.2). **Stated**
5. "There are no strong reasons to assume that neither vanishing LES (with $\Delta\sim h$) nor ILES produce approximations that converge to a DNS solution"; convergent schemes must satisfy a priori estimates (§2.2). **Stated**
6. If a scheme converges weakly, a functional with fixed-support test function converges as $h\to0$, the earlier the larger the support; "In many cases, less than full resolution will be required" (§2.3, Eq. 9). **Stated**
7. A scheme should satisfy Conditions A–E: (A) conservation form, (B) entropy stability, (C) at least as diffusive as kinetic-energy-preserving fluxes, (D) non-negative density, (E) linearly stable continuity equation; the list is conjectured necessary, not sufficient (§3). **Stated** (from **Derived** continuous estimates)
8. With constant heat conductivity only $\nabla\log T\in L^2$ follows; $\kappa_0(1+T^p)\le\kappa_h\le\kappa_1(1+T^p)$ (example $p=2$) is required (§1, §3, Eq. 11). **Derived**
9. For a local Lax–Friedrichs-type flux, a coefficient $\ge\max(|u_i|,|u_{i+1}|)$ keeps the density non-negative; Rusanov's flux satisfies D and is entropy stable, but E-schemes are "very diffusive and generally considered inappropriate for turbulent simulations" (§3, Eqs. 13–15). **Derived**
10. Entropy-conservative fluxes (Ismail–Roe, Chandrashekar) are not locally linearly stable, and linear instability can amplify numerical errors that "trip unphysical turbulence" (§3, citing earlier work; §5.2). **Stated**, **Shown** in §5.2
11. A scheme that is nonlinearly but not linearly stable does not blow up, so a bounded solution is not evidence of an approximation of the true solution (§3). **Stated**
12. Upwind-type dissipation corresponds to $(\nu_t)_{i+1/2}\sim h\max(|u_i|,|u_{i+1}|)$, a turbulent cell Reynolds number $(Re_h)_i=u_ih/\nu_t\sim1$, and "can not be ruled out as subgrid-scale models" (§3.1). **Derived** (scaling argument)
13. Artificial diffusion with a vanishing-viscosity coefficient does not violate Galilean invariance, which matters only for fixed-width LES (§3.1). **Stated**
14. Proposition 4.1: the scheme of Eqs. (20)–(23), with mass flux $\{\!\{\rho\}\!\}\{\!\{u\}\!\}-a^\rho[\![\rho]\!]$, $a^\rho=|\{\!\{u\}\!\}|/2+|[\![u]\!]|/4$, and Chandrashekar's momentum and energy fluxes built on it, satisfies Conditions A–E (§4). **Proved** (one-dimensional proofs; entropy stability by reduction to $(f^\rho-\rho^{\ln}\{\!\{u\}\!\})[\![\rho]\!]/\rho^{\ln}\le0$, Eq. 32)
15. The mass flux $\{\!\{\rho u\}\!\}-a^\rho[\![\rho]\!]$ is an equally valid alternative and behaves similarly (§4). **Stated**
16. The two-dimensional viscous approximation (Eqs. 38–39) is non-symmetric and first-order; a symmetric entropy-stable operator is possible but irrelevant for under-resolved results (§4.1). **Stated**
17. Shu–Osher ($N_x=200$, $\mu=10^{-2}$): stable at the strong shock without additional artificial diffusion, trailing weak shocks diffused but correctly placed, "no undershoot at the strong shock even in the inviscid case" (§5.1, Fig. 1). **Shown**
18. Kelvin–Helmholtz, Euler version ($\mu=\kappa_h=0$): spurious rollers appear from linear instabilities in velocity and temperature (§5.2, Fig. 2). **Shown**
19. Kelvin–Helmholtz with $\mu=\kappa_h=10^{-4}$: unphysical roll-ups on $N_x=128$, absent on finer grids; $\mathbb B$-means differ by less than 10% between $N_x=128$ and 512, and "the averages appear to be converging" (Fig. 3, Table 1). **Shown**
20. The Euler $\mathbb B$-means (Table 2, up to $N_x=1024$) are not on a convergent path; the fine grid is "off by 33% and 42% in the momentum variables in relation to the finest grid values in Table 1" (§5.2). **Shown**
21. Chandrashekar's flux with $\mu=\kappa_h=10^{-4}$ produces more small-scale roll-ups; the coarse-to-fine density difference is 4.1% against 1.8% for the proposed scheme — "local stability improves results on coarse meshes" (§5.2, Fig. 4, Table 3). **Shown**
22. Euler with artificial diffusion on all variables is linearly stable and free of spurious roll-ups but significantly more diffusive and less accurate (Fig. 5, Table 4); on the Taylor–Green vortex it damps kinetic energy at no reasonable rate and is dropped (§5.2). **Shown** / **Stated** (Taylor–Green part not shown)
23. "What may look like turbulent features in under-resolved simulations may be unphysical numerical errors amplified by the scheme"; the most detailed solutions are "essentially non-predictive" (§5.2.1). **Shown**
24. Taylor–Green vortex at $Re=1600$, $M=0.1$: peak kinetic-energy dissipation 0.008551 at $t=10.451$ ($32^3$), 0.011565 at 9.0722 ($64^3$), 0.013569 at 8.6238 ($128^3$) (§5.3, Table 5). **Shown**
25. The scheme is "significantly more accurate than the second-order scheme in [22] with respect to kinetic energy dissipation since it has the same peak with only 64 points and it is more accurate in time" (the [22] value on $129^3$ quoted as $\approx0.0115$ at $t\approx8.3$) (§5.3). **Shown**
26. Enstrophy peaks: the current scheme gives $\mathcal Z\approx4$ and $\approx5$, the reference $\approx10.3$ (§5.3). **Shown**
27. Chandrashekar's scheme gives very similar Taylor–Green results, with a more oscillatory dissipation curve on $32^3$ (§5.3, Fig. 7). **Shown**
28. Averages over large regions should converge faster than local averages; continuity with respect to data holds for weak averages, not point values (§6). **Stated**
29. Like LES the method says nothing about the unresolved eddies; like implicit or vanishing LES its resolved range grows with resolution, DNS being the ultimate target (§6). **Stated**
30. "Standard turbulence models are not exempt from strong requirements (similar to Conditions A-E) since they too should ultimately be well-posed" (§4). **Stated**

# Printed slips

- Abstract: the third test is "a turbulent Rayleigh-Taylor problem"; §1 and §5 run a Taylor–Green vortex. Abstract: "Kelvin-Helmoholtz".
- §4, Eq. (20): $\mathbf f_{i+1/2}=\mathbf f^I_{i+1/2}+\mathbf f^V_{i+1/2}$ "is the sum of the inviscid and viscous" fluxes, with $f^{V2}=+\frac43\mu(u_{i+1}-u_i)/h$ (Eq. 23); the generic scheme (12) puts $f^V$ on the right-hand side and the kinetic-energy derivation (p. 10) uses $(-f^m_{i+1/2}+f^{V2}_{i+1/2})$. *(Compiler check, not in the sources: with the printed sum the viscous term of Eq. (20) is anti-diffusive.)*
- p. 10, kinetic-energy derivation: "$\frac12(D_-u_{i+1})(\tilde p_{i+1/2}-\frac43D_-u_{i+1})$" lacks $\mu$, while the paired term and the collected balance carry $\frac{4\mu}{3}$.
- p. 8, positivity proof: "the last inequality follows from $\lambda^\rho_{i+1/2}>\frac12|\bar u_{i+1/2}|$", whereas Eq. (22) gives equality when $\Delta u_{i+1/2}=0$; the non-strict inequality, which the proof needs, holds.
- Eq. (28) has no transpose; "$|\bar\rho-\hat\rho|\le\frac{\Delta\rho}{2}$" lacks the absolute value on the right.
- Eq. (43): $g^E_{ij+1/2}$ contains "$\mathbf g^{m1}_{i+1/2j}$", "$\mathbf g^{m2}_{i+1/2j}$" with $x$-face indices; Fig. 5 caption prints $\Delta(\mathbf u\cdot\mathbf n)/4$ without absolute value; §5.2 "$\hat\rho_{ij+1/2}\bar v_{ij+1/2j}$" and an unclosed parenthesis.
- §5.2: "the relative differences to Table 1, are less than 1%" for Chandrashekar's finest mesh. *(Compiler check, not in the sources: at $N=512$, $\overline{\rho u}$ is 0.215 in Table 3 against 0.212 in Table 1, 1.4%.)*
- §5.2: "off by 33% and 42%". *(Compiler check, not in the sources: Table 2 at $N=1024$ against Table 1 at $N=512$ gives $(0.283-0.212)/0.212=33.5\%$ and $(0.365-0.257)/0.365=29.6\%$; 42% follows only when normalized by the Euler value 0.257.)*
- §5.3: the maximal dissipation "is close to 0.0013", while Table 5 prints 0.008551–0.013569 and the next sentence quotes $\approx0.0115$.
- §5.3: "peaks at $\mathcal E\le2$ $\mathcal E\le4$" (garbled).
- §5.3, Taylor–Green initial data: $u=V_0\sin(x/L)\cos(y/L)\sin(z/L)$, $v=-V_0\cos(x/L)\sin(y/L)\sin(z/L)$ with $p=p_0+\frac{\rho_0V_0^2}{16}(\cos(2x/L)+\cos(2y/L))(\cos(2z/L)+2)$; $w$ not printed. *(Compiler check, not in the sources: the printed pressure satisfies the incompressible pressure Poisson equation $\nabla^2p=-\rho_0\,\partial_iu_j\partial_ju_i$ exactly for the $\cos(z/L)$ velocity and not for the printed $\sin(z/L)$ one.)*
- Fig. 1: the text and panel legends use $N=200,400,800$; the zoom legend shows $900$.

# Notation map

| Svärd | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho$, $\mathbf v=(u,v,w)$, $p$, $T$, $E$ | $\rho$, $\boldsymbol u$, $p$, $T$, $E$ | |
| $\mathbf u=(\rho,\rho\mathbf v,E)$, $m$ | conservative state, $\rho u$ | **$\mathbf u$ is the conservative vector, not the velocity** |
| $\mathbb S$, $\tau_{ij}$ | $\sigma_{ij}$ (plus bulk term) | **viscous stress, not the SGS stress $\tau_{ij}$**; in Eq. (8) $\bar{\mathbb S}$ is the filtered strain $\bar S_{ij}$ |
| $\eta$ | $\mu_b$ | bulk viscosity, set to 0; **$\eta$ is the Kolmogorov length in the registry** |
| $\kappa$ | $\kappa_h$ | heat conductivity; **$\kappa$ is the von Kármán constant in the registry** |
| $\nu_T$, $c_s$ | $\nu_t$, $C_s$ | Eq. (8) printed $\nu_T\mathbb S=(c_s\Delta^2)\lvert\bar{\mathbb S}\rvert\bar{\mathbb S}$, no value |
| $\bar u$ (§2.2) | $\bar u$ | LES filter $\Phi_\Delta*u$ |
| $\bar a_{i+1/2}$, $\hat a_{i+1/2}$, $\check a_{i+1/2}$ (§4) | $\{\!\{a\}\!\}$, $a^{\ln}$, geometric mean | **overbar and hat are two-point means here, not filters** |
| $\lambda_{i+1/2}$, $\lambda^\rho_{i+1/2}$ | $a_{i+1/2}$, $a^\rho_{i+1/2}$ (page-local) | **$\lambda$ is the Taylor microscale in the registry** |
| $U$, $S$, $\mathbf w$, $F$, $\Psi$ | $\mathcal U$, $s$, $\boldsymbol W$, entropy flux, potential | **$S$ is not the strain rate**; $U_h$ also denotes the numerical solution |
| $\Delta a_{i+1/2}$ (§4) | $[\![a]\!]$ | jump; **$\Delta$ is the filter width in the registry** |
| $\beta=1/(2RT)$ | $\beta_{\mathrm C}$ | **not the field-inversion multiplier $\beta(\boldsymbol x)$** |
| $N$ | $N_x$ | points per direction |
| $E_k$, $\epsilon$, $\mathcal E$ | normalized kinetic energy, $\varepsilon$, $\mathcal Z$ | normalized by $t_c=L/V_0$ |
| $(Re_h)_i$, $l_T$, $u_T$ | page-local | turbulent cell Reynolds number, length and velocity scales |

# Reference list

22 printed references, numbered style [1]–[22], mostly alphabetical.
The list is merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug. [10] is printed "under review, J. Sci. Comput.
(2020)" and kept as a submitted work; [7] has only an article identifier;
[11] and [12] print no volume; [16] prints the journal as "SINUM". No
printed duplicates and no unparseable items.

# Pages created or updated

Chunk 10 (2026-10-27). This source is cited on:

- [Rayleigh–Taylor mixing](/benchmarks/rayleigh-taylor-mixing.md)
- [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Bulk viscosity](/definitions/bulk-viscosity.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Entropy conservation and entropy stability](/properties/entropy-conservation.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
