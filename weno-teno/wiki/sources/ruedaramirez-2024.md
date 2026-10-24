---
type: Source
title: "Rueda-Ramírez et al. (2024) — Monolithic Convex Limiting for Legendre-Gauss-Lobatto Discontinuous Galerkin Spectral-Element Methods"
description: "Transfers Kuzmin's monolithic convex limiting to LGL-DGSEM through its subcell flux-differencing form: closed-form bar-state limiters for conserved and ratio variables, a sharp or cautious pressure fix and a semi-discrete entropy limiter give a time-step-independent bound-preserving operator, compared with FCT/IDP subcell limiting."
resource: "doi:10.1007/s42967-023-00321-6"
source_kind: paper
authors: [Rueda-Ramírez A.M., Bolm B., Kuzmin D., Gassner G.J.]
year: 2024
venue: "Commun. Appl. Math. Comput. 6:1860-1898"
local_file: "/home/stefano/papers/mosaic/weno-teno/2024_Crossref_Communications_on_Applied_Mathematics_and_Computation_Rueda-Ramírez_Monolithic_Convex_Limiting_for_Legendre-Gauss-Lobatto_Discon.pdf"
tags: [dg, limiting, bound-preserving, positivity, entropy-stable]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

The paper transfers Kuzmin's monolithic convex limiting (MCL), a
semi-discrete algebraic flux correction designed for continuous finite
elements and extended by Hajduk to Bernstein DG, to the nodal
Legendre–Gauss–Lobatto [DGSEM](/methods/dgsem.md). Because LGL-DGSEM is a
diagonal-norm [summation-by-parts](/operators/summation-by-parts-operator.md)
operator, it has an explicit subcell
[flux-differencing](/methods/flux-differencing.md) form with fluxes between
neighbouring nodes. It also has a compatible low-order invariant-domain-preserving
subcell finite-volume scheme with
[local Lax–Friedrichs](/methods/lax-friedrichs-flux.md) fluxes, the scheme of
[subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md).
No sparsification, graph Laplacian or linear solve is needed, unlike for
Bernstein DG.

The high-order subcell flux is written as the low-order flux plus an
antidiffusive flux, and the update is written in terms of bar states, as in
[convex limiting](/methods/convex-limiting.md). The antidiffusive fluxes are
limited in closed form so that every limited bar state stays within prescribed
bounds. The paper gives four limiters: one for conserved variables with local
or global bounds, a sequential one for ratios (velocity, specific total
energy), a pressure fix linearized through $\alpha^2\le\alpha$ in a "sharp"
and a "cautious" variant, and the semi-discrete entropy limiter of Kuzmin,
Hajduk and Rupp, which enforces Tadmor's condition
([entropy stability](/properties/entropy-stability.md)). Because the limiting
acts on the semi-discrete operator, the limited spatial operator does not
depend on $\Delta t$, unlike FCT/IDP predictor–corrector subcell limiters. The
price is a CFL bound stricter than the low-order one
([bound preservation](/properties/bound-preservation.md)).

The tests (Euler, Trixi.jl) are: [density-wave](/benchmarks/density-wave-advection.md)
convergence, with order $N+1$ under global positivity bounds and at most about 2
under tight local bounds; a [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)
comparing MCL with FCT/IDP; a bow shock on a curvilinear mesh; a
[Sedov blast](/benchmarks/sedov-blast-wave.md) comparing limiter sequences A,
B and C; and a Mach-2000 [astrophysical jet](/benchmarks/high-mach-astrophysical-jet.md).
In the jet, the MCL step count scales exactly inversely with the CFL number
and the FCT/IDP count does not.

# Version read

arXiv preprint arXiv:2303.00374v1 [math.NA], 1 March 2023 (Springer Nature
LaTeX template), 39 pages, all read; Eqs. (33)–(39) were checked visually on
pp. 13–14. It is not the version of record (CAMC 6:1860–1898). Page 1 matches
Crossref in title and authors; the preprint writes "Spectral Element Methods"
without the hyphen. Equation, table and reference numbers cited here are those
of arXiv v1.

# Key claims

Registry notation: the LGL weight $\omega_i$ is $\mathsf w_i$, the wave-speed
bound $\lambda^{\max}_{(i,j)}$ is $a_{(i,j)}$, the bar state
$\bar u_{(i,j)}$ is $\breve u_{(i,j)}$ (as on the convex-limiting page), the
volume flux $f^*$ is $f^{\mathrm{vol}}$, the entropy $S$, entropy variables
$v$ and potential $\Psi$ are $\eta$, $w$, $\psi$. The MCL factor is written
$\alpha_{\mathrm{MCL}}$ (page-local; 1 = high order, i.e. $1-\alpha$ in the
registry's blending convention).

1. LGL-DGSEM, like any diagonal-norm SBP discretization, can be written as $J\dot u_i=\frac1{\mathsf w_i}\big(\hat f^{\mathrm{DG}}_{(i-1,i)}-\hat f^{\mathrm{DG}}_{(i,i+1)}\big)$ with explicit symmetric subcell fluxes $\hat f^{\mathrm{DG}}_{(i,i+1)}=\sum_{l=0}^{i}\sum_{k=0}^{N}S_{lk}f^{\mathrm{vol}}(u_l,u_k)$, $S=Q-Q^\top$, which gives subcell local conservation (§2.1, Eqs. (5)–(8), Remark 1). **Stated** (cited)
2. DG with a dense mass matrix (e.g. Bernstein, $N>1$) needs $m$ sparse linear systems of size $(N+1)\times(N+1)$ per element and stage to recover a flux-differencing form; LGL-DGSEM needs none (Remark 2). **Stated**
3. Read as subcell means, the nodal values define a subcell finite-volume scheme (Eqs. (9)–(10)) with local Lax–Friedrichs fluxes, compatible with (5) and invariant-domain preserving (§2.2.1). **Stated** (cited)
4. The forward-Euler low-order update is a convex combination of $u^n_i$ and the bar states $\breve u_{(i,i\pm1)}$ under $\Delta t\le J\mathsf w_i/(a_{(i,i-1)}+a_{(i,i+1)})$; the LLF bar state is the HLL intermediate state and keeps every convex invariant (Eqs. (11)–(13)). **Derived**
5. With LGL nodes the DG and FV fluxes at element boundaries coincide when both use the same surface flux, so the blended interface flux does not depend on the blending factor and limiting is purely element-local (Remark 6). **Derived**
6. The high-order update takes bar-state form with high-order bar states $\breve u^{\mathrm{DG}}_{(i,j)}=\breve u_{(i,j)}+\Delta\hat f_{(i,j)}/a_{(i,j)}$, $\Delta\hat f_{(i,j)}=(i-j)\big(\hat f^{\mathrm{DG}}_{(i,j)}-\hat f^{\mathrm{FV}}_{(i,j)}\big)$; MCL replaces them by limited bar states (Eqs. (16)–(21)). **Derived**
7. The closed-form limiter (23) enforces the two-sided bar-state bounds (22) for a conserved scalar, and the limited flux is a convex combination of the FV and DG fluxes (24). Computing the factor explicitly is "unnecessary and numerically ill posed" for small denominators (§2.2.2). **Derived** ("easy to verify")
8. In LGL-DGSEM the bar states of a ratio $\phi=(\rho\phi)/\rho$ are symmetric, $\breve\phi_{(i,j)}=(\breve{\rho\phi})_{(i,j)}/\breve\rho_{(i,j)}$ (Eq. (25)), "a further advantage compared to Bernstein-basis DG methods". **Derived**
9. In the sequential limiter the factor of the auxiliary flux lies in $[0,1]$, but the induced factor of the conserved flux $\Delta\hat f^{\rho\phi}$ "does not necessarily lie in the range [0,1]" (Remark 8). **Stated**
10. Pressure positivity of the limited bar states (31) reduces to quadratic inequalities (33) in one synchronized factor; $\alpha_{\mathrm{MCL}}^2\le\alpha_{\mathrm{MCL}}$ gives the linear sufficient condition $P_p\alpha_{\mathrm{MCL}}\le Q_p$, $P_p=\max\{0,A_p\}+\lvert B_p\rvert$, solved in closed form (35). This uses the symmetry of the low-order LGL bar states, while "the general formula ... is more involved" (§2.2.2, Eqs. (31)–(35)). **Derived** (see Printed slips for $Q_p$)
11. The "cautious" fix, with the upper bound $P^{\max}_p\ge P_p$ (36) for continuous dependence on the data, "can add much more numerical dissipation" than the "sharp" one. In the jet it suppresses the shear-layer vortices that the sharp fix lets develop (§2.2.2, §3.5, Fig. 9). **Shown**
12. The semi-discrete entropy limiter (38)–(39) enforces Tadmor's condition $[\![w]\!]^\top\hat f_{(i,j)}\le[\![\psi]\!]$ (37) through one closed-form factor. All MCL corrections are closed-form, whereas the FCT/IDP alternatives solve nonlinear equations (Remark 9). **Stated** (cited)
13. With a nonnegative density lower bound and a pressure fix (sharp or cautious) as last stage, MCL is positivity preserving (§2.2.3). **Stated**
14. Local bounds built from the low-order bar states, Eqs. (40)–(41), make the MCL constraints feasible. FCT/IDP may take bounds from the next-step low-order solution (42), which is more dissipative but may relax the step restriction (§2.2.3). **Stated**
15. MCL, and FCT/IDP with bar-state bounds, need $\Delta t\lesssim\min_im_i/(2\sum_da^{(d)}_i)$ (44), more restrictive than the usual low-order bound (45), "especially for multiple space dimensions" (§2.2.4). **Derived**
16. "To the authors' knowledge", the only way to avoid the strict bound (44) and still stay within bounds is FCT/IDP without bar-state bounds; the low-order method is provably positive only under (44) (§2.2.4). **Stated**
17. In FCT/IDP the antidiffusive correction, and with it the spatial discretization and its dissipation, depends on $\Delta t$; in MCL it does not (§2.2.4, §4). **Shown** (§3.5, Table 5, Fig. 8)
18. Density wave with global (positivity) bounds only: EOC about $N+1$, mean 4.16 for $N=3$ (Table 1) and 4.75 for $N=4$ (Table 2) over $N_e=4,8,16,32$ (§3.1). **Shown**
19. Same test with local bounds (sequential limiting, Eq. (48)): EOC "at most second order, independent of the polynomial degree", mean 1.82 ($N=3$, Table 3) and 1.61 ($N=4$, Table 4); the bounds must be relaxed, e.g. with a smoothness sensor, to recover high order (§3.1). **Shown**
20. Kelvin–Helmholtz ($N=7$, $64^2$ elements, $t=10$): MCL with strict positivity (47) and FCT/IDP with the heuristic bounds $\rho_i\ge0.1\rho^{\mathrm{FV}}_i$, $p_i\ge0.1p^{\mathrm{FV}}_i$ both reach $t=10$ with "remarkably similar looking results"; FCT/IDP needs a positive threshold, "as otherwise some nodes might get an invalid vacuum state" (§3.2, Fig. 1). **Shown**
21. Kelvin–Helmholtz with local bounds: MCL (density, velocity, specific total energy) and FCT/IDP (density, minimum of the modified specific entropy) give very comparable results; local bounds add more dissipation than global ones; mean limiting factors in Fig. 3 (§3.2, Figs. 2–3). **Shown**
22. Bow shock ($N=5$, curvilinear isoparametric mesh): global positivity bounds suffice to reach $t=10$ but leave spurious oscillations near the shock; local bounds remove them (§3.3, Fig. 4). **Shown**
23. Sedov blast ($N=3$, $64^2$, $t=3$): limiter A (sequential, sharp pressure, entropy) shows "artifacts at the shock front". Limiter B (density bar-state limiter, its effective factor (58) applied to all conserved fluxes, then pressure and entropy) "removes the Carbuncle-like artefacts". Limiter C (B followed by sequential limiting, pressure and entropy) also removes them, needs the least pressure limiting and no entropy limiting at $t=3$, but is "clearly more dissipative" (§3.4, Figs. 5–7). **Shown**
24. Astrophysical jet ($M\approx2000$, $N=3$, $256^2$, $t=10^{-3}$): MCL needs 10284, 20568, 41138 and 102844 steps at CFL 0.9, 0.45, 0.225 and 0.09, FCT/IDP 10758, 25608, 71577 and 241974. The FCT/IDP vortical structures depend strongly on the CFL number, the MCL ones weakly (§3.5, Table 5, Fig. 8). **Shown** (CFL × steps is 9255.6, 9255.6, 9256.1, 9256.0 for MCL and 9682, 11524, 16105, 21778 for FCT/IDP; *compiler check, not in the sources*)
25. In FCT/IDP a smaller CFL number reduces the dissipation: $\rho_{\min}$ falls from $4.43\times10^{-3}$ to $7.11\times10^{-4}$ and $p_{\max}$ rises from 172640 to 228165, which raises the sound speed and shrinks $\Delta t$ further, a "feedback effect" (§3.5, Table 5). **Shown**
26. "Time convergence can be expected for MCL but not for FCT schemes in problems that need stabilization" (§4). **Shown** (jet test only)
27. The method applies to "any other spatial semi-discretization that produces sparse discrete gradient operators with SBP properties", e.g. Gauss-DGSEM (inter-element fluxes and projections need further analysis, Remark 3) or SBP discretizations of non-conservative systems (§1). **Stated**

# Printed slips

- Eq. (33): $Q_{(i,j)}=\bar w^\rho_{(i,j)}\bar w^{\rho E}_{(i,j)}+\frac{\|\bar w^{\rho\vec v}_{(i,j)}\|^2}{2}$ (checked visually, p. 13). Multiplying (31) by $a_{(i,j)}^2$ and inserting (32) gives $A_p\alpha^2_{\mathrm{MCL}}+B_p\alpha_{\mathrm{MCL}}\le Q_p$ with $A_p$, $B_p$ as printed and $Q_p=\bar w^\rho\bar w^{\rho E}-\tfrac12\|\bar w^{\rho\vec v}\|^2$, i.e. $a^2_{(i,j)}$ times $\breve\rho\,(E-\kappa)$ of the low-order bar state. The "+" should be "−" *(compiler check, not in the sources)*.
- Eq. (39): the numerator of the entropy factor is printed $[\![v]\!]\hat f^{\mathrm{FV}}-[\![\Psi]\!]+\epsilon$ (checked visually, p. 14). Inserting (38) into (37) as printed gives the bound $\big([\![\psi]\!]-[\![w]\!]^\top\hat f^{\mathrm{FV}}\big)/\big([\![w]\!]^\top\Delta\hat f^{\mathrm{Lim}}/(i-j)\big)$, and the denominator is positive in the branch $\Pi_{(i,j)}>[\![\psi]\!]$ when the FV flux satisfies (37). The printed numerator has the opposite sign and would give a nonpositive factor up to $\epsilon$ *(compiler check, not in the sources)*.
- §3.3, bow shock: "$\rho=1.4$, $p=1$, $v_1=4$, $v_2=0$, which corresponds to a Mach number Ma = 1.4". With $\gamma=1.4$, $c=\sqrt{\gamma p/\rho}=1$ and the printed state has $M=4$ *(compiler check, not in the sources)*. Either the Mach number or the state is misprinted.
- §3.5: the step count "depends linearly on the CFL number for MCL methods"; Table 5 shows it is inversely proportional (claim 24), and the next sentence speaks of "not inversely proportional" for FCT/IDP.
- Eq. (58) mixes the subscripts $(i,j)$ and $(ij,k)$ in one formula; Eq. (48) prints "$v^{Lim}_{2,(i,j)}$" next to "$v^{Lim}_{1(i,j)}$".
- Typos: "FCT/DIP" (§3.5); "shear layer of the yet" for "jet" (§3.5).
- Abstract and §1 say "If the pressure becomes negative, a simple scaling limiter is applied"; the method presented is the closed-form pressure fix (35).
- Reference list: [24] = [35] (Kuzmin & Quezada de Luna, JCP 411:109411), [34] = [57] (Kuzmin, Hajduk & Rupp, CMAME 389:114428), [40] = [47] (Gassner, SISC 35:1233–1253); ref. [38] prints "Thomas, I." where refs. [8] and [13] print "Tomas, I.".

# Notation map

| Rueda-Ramírez et al. (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u=[\rho,\rho\vec v,\rho E]$ | $u=(\rho,\rho v,E)$ | **source $E$ is specific total energy**: source $\rho E$ = registry $E$ |
| $N$, $K$ (elements), $N_e$ | $N$, kept, $N_x$ | **$K$ counts elements, not the TENO stencil** |
| $\omega_i$, $J$, $m_i$ | $\mathsf w_i$, $J$, $M_{ii}$ | LGL weight; subcell width $J\mathsf w_i$ |
| $Q$, $B$, $S=2Q-B=Q-Q^\top$, $\bar S=Q-B$ | $Q$, $B$, kept | SBP matrices; **$S$ collides with the source term $S(u)$** |
| $f^*_{(i,k)}$ | $f^{\mathrm{vol}}(u_i,u_k)$ | Ranocha EC+KEP flux in most tests, Chandrashekar in Sedov |
| $\hat f^{\mathrm{DG}}_{(i,j)}$, $\hat f^{\mathrm{FV}}_{(i,j)}$ | kept | symmetric two-index subcell fluxes, $\hat f_{(i,i+1)}=\hat f_{i+1/2}$ |
| $\lambda^{\max}_{(i,j)}$ | $a_{(i,j)}$ | LLF dissipation coefficient |
| $\bar u_{(i,j)}$ | $\breve u_{(i,j)}$ | bar state (page-local, as on the convex-limiting page); **registry $\bar u_i$ is a cell average** |
| $\Delta\hat f_{(i,j)}$, $\Delta\hat f^{\mathrm{Lim}}_{(i,j)}$ | kept | antidiffusive flux and its limited value |
| $\alpha_{(i,j)}$, $\alpha^\rho$, $\alpha^\phi$, $\alpha^p$, $\alpha^s$ | $\alpha_{\mathrm{MCL}}$ (page-local) | **1 = high order, the inverse of the registry's blending $\alpha$** (the FCT/IDP comparison uses the registry convention, plotted as $1-\alpha$) |
| $A$, $B$, $Q$, $P$, $P^{\max}$ | $A_p$, $B_p$, $Q_p$, $P_p$, $P^{\max}_p$ (page-local) | pressure-fix coefficients; **$B$, $Q$ collide with the SBP matrices** |
| $\bar w_{(i,j)}=\lambda^{\max}\bar u_{(i,j)}$ | $a_{(i,j)}\breve u_{(i,j)}$ | **$w$ is the registry's entropy variable** |
| $S=-\rho s/(\gamma-1)$, $\vec f^S$, $v$, $\Psi$ | $\eta$, $F_\eta$, $w$, $\psi$ | mathematical entropy; agrees with the registry's default |
| $\eta=e\rho^{1-\gamma}$ | kept in words | modified specific entropy of the FCT/IDP local bound; **$\eta$ is the registry's entropy** |
| $\beta$ | kept | **0.1 FCT/IDP positivity fraction (Eq. (50)) and $\rho/(2p)$ (Eq. (A4))** |
| $e$ | $e$ | specific internal energy; **"$e=1$" in Eq. (56) is the blast energy** |
| $\epsilon$ | kept | regularization of the effective factors, not the WENO $\epsilon$ |
| $N(i)$, $N^*(i)$ | kept | $\{i-1,i,i+1\}$, $\{i-1,i+1\}$ |
| CFL | $\nu$ | multiplies the bound (44) |

# Reference list

76 printed references in numbered style ([1]–[76]), merged complete into
the [bibliography](/bibliography.md) with `citedby` `ruedaramirez-2024`. The
list prints three duplicates, [24]/[35], [34]/[57] and [40]/[47], each
recorded as one work. Ref. [41] is the arXiv preprint of Rueda-Ramírez &
Gassner's subcell positivity limiter and is kept apart from its published
form. The arXiv preprints of Kuzmin & Vedral, Ranocha et al. and Vilar are
likewise kept distinct from their published versions. Ref. [69] (HOW5
workshop) is a web page and ref. [75] the Trixi.jl repository; refs. [38] and
[74] print no volume, [55] prints none ("1–24"), [72] prints no venue. All
items parsed.

# Pages created or updated

Chunk 7 (2026-10-23), cited further in chunks 8–11 (2026-10-23/24). This source is cited on:

* [Bound preservation](/properties/bound-preservation.md)
* [Convex limiting and invariant-domain-preserving schemes](/methods/convex-limiting.md)
* [Density-wave advection](/benchmarks/density-wave-advection.md)
* [Discontinuous Galerkin spectral element method (DGSEM)](/methods/dgsem.md)
* [Entropy stability](/properties/entropy-stability.md)
* [Flux differencing and split-form DG](/methods/flux-differencing.md)
* [High-Mach astrophysical jets](/benchmarks/high-mach-astrophysical-jet.md)
* [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [Sedov blast wave](/benchmarks/sedov-blast-wave.md)
* [Subcell finite-volume limiting for DG](/methods/subcell-finite-volume-limiting.md)
* [Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md)
