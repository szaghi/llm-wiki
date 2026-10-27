---
type: Source
title: "Ranjbar et al. (2026) — Self-tuning dynamic explicit modal filtering based on local flow characteristics for large-eddy simulation"
description: "Self-tuning dynamic explicit modal filter for DGSEM LES in HORSES3D: an orthogonality-based nodal-to-modal transform, a tanh kernel on grouped modes, and a cut-off set per element and time step from the grid-to-Kolmogorov ratio and strain and rotation invariants, tested on decaying isotropic turbulence, the Taylor–Green vortex and channel flow."
resource: "doi:10.1063/5.0309811"
source_kind: paper
authors: [Ranjbar M., Mostafavi A., Mashayek F.]
year: 2026
venue: "Phys. Fluids 38:015141"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2026_Crossref_Physics_of_Fluids_Ranjbar_Self-tuning_dynamic_explicit_modal_filtering_based_on_local.pdf"
tags: [filtering, dg, sgs-model, implicit-les, high-order]
timestamp: 2026-10-26T16:21:00Z
---

# Summary

Ranjbar et al. (2026) extend their dynamic explicit modal filter (DEMF) into
a self-tuning dynamic explicit modal filter (STDEMF), an
[explicit modal filtering](/methods/explicit-modal-filtering.md) closure for
[large-eddy simulation](/definitions/large-eddy-simulation.md) with the
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md) of
[HORSES3D](/software/horses3d.md). Instead of adding a viscous flux with a
high-pass modal kernel, as [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
does, the solution itself is transformed to modal space, its high modes are
attenuated by a low-pass kernel, and the filtered field is transformed back and
blended with the unfiltered one. The paper makes three changes to DEMF. The
nodal-to-modal transform follows from discrete orthogonality for any
orthogonal basis (Legendre on Gauss–Lobatto nodes here). A hyperbolic-tangent
kernel acts on mode groups, the modes binned by the radius
$\sqrt{i^2+j^2+k^2}$. The cut-off group is set per element and per time step
from the ratio $\Delta/\eta$ of grid spacing to local Kolmogorov length and
from strain and rotation invariants, with one tunable constant $c$. Filtering
acts only where $\eta<\Delta$.

All tests are [a posteriori](/definitions/a-priori-and-a-posteriori-testing.md)
on unmodelled coarse meshes ([implicit LES](/definitions/implicit-les.md)
baselines) against in-house [DNS](/definitions/direct-numerical-simulation.md)
or Moser et al. (1999). The cases are decaying
[isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md), the
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at $Re=200$ and
$800$ (split form, [kinetic-energy preservation](/properties/kinetic-energy-preservation.md)),
and compressible [channel flow](/benchmarks/turbulent-channel-flow.md) at
$Re_\tau=395$. STDEMF is closest to the reference in all three, with optimal
$c$ of 0.65, 0.25 and 0.5. The [Smagorinsky model](/methods/smagorinsky-model.md)
over-dissipates late in isotropic decay, is called "not a suitable option" for
the Taylor–Green vortex, and is unstable or inaccurate in the channel. The cost
overhead is 1–2.5%, and the filter switches itself off as the flow laminarizes.
The paper frames upwind dissipation of DG as insufficient for under-resolved
turbulence ([numerical dissipation](/properties/numerical-dissipation.md)),
borrows the invariants from machine-learning [mesh adaptation](/methods/mesh-adaptation.md),
and places its channel grid in the wall-resolved range of Choi & Moin
([grid requirements](/results/les-grid-point-requirements.md)).

# Version read

arXiv preprint 2512.03315v1 [physics.flu-dyn] (2 December 2025), not the
version of record; 50 pages (text pp. 1–40, references pp. 41–50), all read,
with Eqs. (6)–(8), (28)–(44), (47)–(50) and Figs. 1, 3, 13–15 checked visually.
Page-1 title and authors agree with Crossref. Equation, figure and page
numbers here are those of the preprint. The polynomial order is printed as a
script $\mathscr P$.

# Key claims

1. Modal coefficients follow from nodal values for any collocation grid and any orthogonal basis through orthogonality: forward matrix $\mathcal M_{ki}$ (Eq. 21) and backward matrix $\mathcal N_{ki}$ (Eq. 24), three successive 1-D products in 3-D (Eqs. 26–27) (§II.B). **Derived**
2. Lagrange polynomials are not orthogonal on $[-1,1]$, but they are discretely orthogonal under the Gauss–Lobatto or Gauss–Legendre nodal quadrature (citing Mateo-Gabín et al. 2022) (§II.B, after Eq. 24). **Stated**
3. Modes are grouped into energy levels $\Gamma_n$ by $\sqrt{i^2+j^2+k^2}\in[n-0.5,n+0.5)$, $2\le n\le N_\Gamma=\mathrm{round}(\sqrt3\,(N+1))$ (Eqs. 28–29), and a 1-D kernel acts on the groups instead of a tensor product of 1-D kernels as in SVV (§II.B). **Stated** (design choice)
4. The tanh kernel (Eq. 31) keeps groups $n\le n_c$, attenuates those above, reaches zero at $n=N_\Gamma$, adapts to the polynomial degree through $N_\Gamma$ and $n_c$, and admits real-valued cut-offs (§II.B). **Derived**
5. The cut-off $n_c=N_\Gamma(\Delta/\eta)^{-c}(1-X)^c$ (Eq. 36) decreases (stronger filtering) as $\Delta/\eta$ and the shear–rotation measure $X$ grow, and evolves in time per element, unlike the fixed cut-offs of Karamanos & Karniadakis (2000), Manzanero et al. (2020a), Mateo-Gabín et al. (2022) and DEMF (§II.B, pp. 14–15). **Derived**
6. Worked example: $N=10$ gives $N_\Gamma=19$; with $X=0.6$, $c=0.4$, elements with $\Delta/\eta=2.5$ and $1.5$ get $n_c=9.12$ and $11.2$ (Fig. 1). Eq. (36) reproduces both values *(compiler check, not in the sources)*. **Derived**
7. Filtering frequency $F$ and blending factor $\alpha_b$ (Eq. 44): after Ghiasi et al. (2019), equal products $\alpha_bF$ give identical results; $\alpha_b=0.01$, $F=1$ in all cases (§II.B). **Stated**
8. Isotropic decay: the HORSES3D DNS ($12^3$ elements, $N=8$, 1,259,712 points) agrees with the DSEM code of Ranjbar et al. (2024c) in turbulent kinetic energy (§III.A, Fig. 3a). **Shown**
9. Isotropic decay on the coarse mesh ($6^3$ elements, $N=7$, 110,592 points): the unmodelled run over-predicts the kinetic energy; Smagorinsky with $C_s=0.12$ ("optimal") agrees but over-dissipates for $t>2.4$; DEMF removing 6 or 7 groups brackets the DNS; STDEMF with $c=0.65$ agrees best (§III.A, Fig. 3). **Shown**
10. Isotropic decay: the mean (standard deviation) of $n_c$ over all elements rises from 3.815 (0.078) at $t=2$ to 4.895 (0.0913) at $t=4$ and 5.923 (0.153) at $t=6$: little spatial variation, less dissipation as turbulence decays (§III.A, Fig. 5). **Shown**
11. The optimal cut-offs of STDEMF are lower than those of DEMF because the tanh kernel attenuates, rather than removes, the groups above the cut-off (§III.A, §III.C). **Stated**
12. Element averages of $Q_S$ and $Q_\Omega$ are larger in magnitude on the coarse mesh than in the DNS, mostly before $t=5$; with STDEMF they are "very close to the DNS results" at a resolution one order of magnitude below DNS (§III.A, Fig. 6). **Shown**
13. The Taylor–Green DNS at $Re=200$ ($18^3$, $N=7$) and $800$ ($20^3$, $N=12$) reproduces the dissipation rate of Fehn et al. (2021) (§III.B, Fig. 7). **Shown**
14. Taylor–Green, $11^3$ elements, $N=4$, $t=6$: joint PDFs associate larger $|Q_S|$, $Q_\Omega$ and $X$ with larger high-index levels $\Gamma_7$, $\Gamma_8$, so the cut-off should depend on strain and rotation invariants as well as on $\eta$ (§III.B, Figs. 8–9). **Shown**
15. Joint PDFs of $n_c$ against high-index $\Gamma$ ($11^3$, $N=4$ at $t=6$; $7^3$, $N=10$ at $t=9$) associate large $\Gamma$ with low $n_c$: more dissipation where unresolved energy accumulates (§III.B, Fig. 10). **Shown**
16. Taylor–Green $Re=200$, $11^3$, $N=4$: mean (standard deviation) of $n_c$ is 5.409 (1.174) at $t=6$, 5.515 (1.136) at $t=10$, 5.363 (1.408) at $t=14$, 5.22 (1.38) at $t=18$; the spread reflects inhomogeneity, and the two peaks of the distribution merge as the flow becomes isotropic (§III.B, Fig. 12). **Shown**
17. Taylor–Green $Re=200$ ($c=0.25$): the coarse mesh over-predicts dissipation after $t=4$ and under-predicts after $t=7$; DEMF removing 3 or 4 groups brackets the DNS; Smagorinsky over-predicts for $t<6$ and under-predicts after $t=7$, "not a suitable option"; STDEMF is closest, slightly low in $t\in[8,12]$; DNS-to-coarse point ratio "roughly 18" (§III.B, Fig. 13). **Shown**
18. Taylor–Green $Re=800$, $7^3$, $N=10$ ($c=0.25$): the coarse run over-predicts after $t=4$ and under-predicts after $t=9$; DEMF (5, 6 groups) improves before $t=9$ but is lower than the coarse run for $9<t<11$; Smagorinsky deviates from $t=2$ because the flow is mostly laminar for $t<4$; STDEMF agrees well, slightly low in $t\in[8.5,12]$ (§III.B, Fig. 14). **Shown**
19. DEMF and STDEMF vanish in the laminar limit through the sensor, unlike Smagorinsky (§III.B). **Stated** (supported by claim 28)
20. STDEMF uses the same $c$ across polynomial degrees ($N=4$ and $10$), whereas DEMF must remove more groups at higher degree (§III.B). **Shown**
21. Channel, $14\times12\times16$ elements, $N=6$, $Re_\tau=395$: the unmodelled run over-predicts all rms velocities (most the wall-normal and spanwise ones), has nonzero wall fluctuations from weakly enforced boundary conditions (Collis 2002) and jumps in the wall-normal rms; modal filtering drives wall values to zero and smooths the jumps; STDEMF with $c=0.5$ lies between DEMF with 5 and 6 groups removed and agrees best with Moser et al. (1999) (§III.C, Fig. 15). **Shown**
22. Channel: averaging Eqs. (38)–(39) over the homogeneous plane, over time, or over the spanwise direction gives nearly identical results (§III.C). **Shown** (not plotted)
23. Channel: Smagorinsky with $C_s<0.15$ is unstable and crashes; $C_s=0.2$ deviates significantly from DNS; results not reported (§III.C). **Stated**
24. Channel: the stationary distribution of $n_c$ has mean about 4.0 and standard deviation about 0.91, stable across flow-through times (§III.C, Fig. 16). **Shown**
25. Eq. (38) was designed for incompressible and low-Mach flows; dilatational effects at high Mach number may require revision (§III.D.1). **Stated**
26. Sensitivity: optimal $c\in[0.2,0.7]$. Isotropic decay ($c_{\mathrm{opt}}=0.65$): $-10\%$ gives $D=0.042$, $-20\%$ gives $D=0.105$ (Eq. 51). Channel ($c_{\mathrm{opt}}=0.5$): a 20% change gives $D=0.151$ (wall-normal rms) and $0.114$ (spanwise rms). The unfiltered channel is unstable (§III.D.2, Fig. 17). **Shown**
27. Cost: Taylor–Green $7^3$, $N=10$, +1.31% wall time; channel +0.96% (time averaging), +1.59% (homogeneous-plane averaging), +2.5% (spanwise averaging), same processor count (§III.D.3). **Shown**
28. Laminar limit: the ratio $R_\Gamma$ of modal energy above the cut-off to the total decays to negligible values as the flow laminarizes, so STDEMF has no effect there (§III.D.4, Fig. 18). **Shown**

The filter, translated. Nodal values $Q_{ijk}$ are mapped to modal
coefficients $a_{ijk}=\sum\mathcal M_{li}\mathcal M_{mj}\mathcal M_{nk}Q_{lmn}$
(Eq. 26) with
$$\mathcal M_{ki}=\frac{\int_{-1}^1\ell_i(\xi)P_k(\xi)\,w(\xi)\,d\xi}{\int_{-1}^1P_k^2(\xi)\,w(\xi)\,d\xi},$$
filtered by group, $a^f_{ijk}=\sigma_na_{ijk}$, with the kernel (Eq. 31)
$$\sigma_n=\begin{cases}1, & n\le n_c,\\ -\tanh\!\Big[-3\,\dfrac{(n-N_\Gamma)^2}{(n_c-N_\Gamma)^2}\Big], & n>n_c,\end{cases}$$
mapped back (Eq. 27) and blended, $Q^r=\alpha_bQ^f+(1-\alpha_b)Q$ (Eq. 44).
The cut-off (Eqs. 34–39):
$$n_c=N_\Gamma\Big(\frac{\Delta}{\eta}\Big)^{-c}(1-X)^c,\quad X=X_SX_\Omega,\quad X_S=1-\exp\!\Big(\frac{-|\bar Q_S|_e}{\langle|\bar Q_S|_e\rangle_u+\epsilon_\kappa}\Big),\quad X_\Omega=1-\exp\!\Big(\frac{-\bar Q_{\Omega,e}}{\langle\bar Q_{\Omega,e}\rangle_u+\epsilon_\kappa}\Big),$$
with $Q_S=\tfrac12[(\mathrm{tr}\,S)^2-\mathrm{tr}(S^2)]$, $Q_\Omega=-\tfrac12\mathrm{tr}(\Omega^2)$,
$(\cdot)_e$ the nodal average over the element and $\langle\cdot\rangle_u$ the
average over unresolved elements (homogeneous directions and/or time; not the
registry's Reynolds average). The sensor (Eqs. 40–42) uses $\eta=Re^{-3/4}\bar\varepsilon_e^{-1/4}$
and $\Delta=\mathcal J^{1/3}/\prod_i(N_i+1)^{1/3}$; filtering acts only where
$\eta<\Delta$. All symbols except $\Delta$, $\eta$, $\mathcal J$, $N$, $S$,
$\Omega$ are page-local.

# Printed slips

- Eq. (7) prints $P=\rho T/(\gamma Ma_c)$, while the heat-flux term of Eq. (4) carries $Ma_c^2$. With the scalings of Eq. (8), $P^*=\rho^*R^*T^*$ gives $P=\rho T/(\gamma Ma_c^2)$ *(compiler check, not in the sources)*.
- p. 6: "The quantity $e$ represents the dimensionless internal energy", but Eq. (5), $\rho e=P/(\gamma-1)+\rho v_iv_i/2$, is the total energy.
- p. 4: modal filtering removes "energy from the large resolved scales"; the rest of the paper removes energy from the high-wavenumber resolved modes.
- §III.D.1: "the correlation between more positive $Q_S$ values and higher-index $\Gamma$ should be further examined", while the preceding sentence and p. 13 associate larger negative $Q_S$ with higher-index $\Gamma$.
- The kernel is said to reduce modes "exponentially" (pp. 12, 20); Eq. (31) is a tanh of a quadratic.
- "Chandrasekar averaging function" (pp. 29, 33) for the cited Chandrashekar (2013).
- The Smagorinsky constant $C_s=0.1$ of the Taylor–Green runs appears only in the legends of Figs. 13–14.
- Reference list: Ferrer & Willden (2011a) and (2011b) are the same article (same title, Comput. Fluids 46:224–230, same DOI); the title of Ferrer et al. (2023) is printed as ": A high-order discontinuous galerkin solver …" without the code name; Mostafavi et al. (2024b) carries the year 2024 with a 2025 JCP DOI and no volume; "mthod" in the title of Zhang & Liu (2022).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathscr P$, $\mathscr P_i$ | $N$, $N_i$ | polynomial degree, $(N+1)^3$ nodes per element; case label "$a\mathscr Pb$" = $a^3$ elements of degree $b$ |
| $N=\mathrm{round}(\sqrt{3(\mathscr P+1)^2})$ | $N_\Gamma$ (page-local) | **collision:** number of mode groups, not the polynomial degree |
| $M$ | $n_c$ (page-local) | **collision** with the Mach number $M$; cut-off mode group, real-valued |
| $\mathscr P_f$ | (number of highest groups removed by DEMF, page-local) | integer, user-chosen |
| $\vec Q$, $\tilde Q_{i,j,k}$ | $Q$, $Q_{ijk}$ (state, nodal values, page-local) | **collision:** tilde is the curvilinear transform, not a Favre filter |
| $\hat Q_{i,j,k}$ | $a_{ijk}$ (modal coefficients, page-local) | **collision:** hat is not a test filter; indices start at 1 in the source |
| $\hat Q^f$, $\tilde Q^f$, $\tilde Q^r$ | $a^f_{ijk}$, $Q^f$, $Q^r$ | filtered modes, filtered and blended nodal values |
| $\mathcal M$, $\mathcal N$ | $\mathcal M$, $\mathcal N$ (page-local) | forward and backward transform matrices |
| $l_i$, $P_i(\xi)$, $w(\xi)$ | $\ell_i$, $P_i$, $w$ (page-local) | Lagrange interpolant, orthogonal (Legendre) polynomial, weight |
| $\Gamma_n$, $\theta(i,j,k)$ | $\Gamma_n$, (group indicator) | energy level, $\ell^2$ norm of group $n$ |
| $\mathscr F_n$ | $\sigma_n$ (page-local) | kernel |
| $\alpha$ | $\alpha_b$ (page-local) | **collision** with the DG/FV blending factor $\alpha$ |
| $F$ | $F$ (page-local) | filtering frequency |
| $c$ | $c$ (page-local) | STDEMF constant |
| $\kappa$ | $\epsilon_\kappa$ (page-local) | **collision** with the von Kármán constant; regularizer, value not printed |
| $Q_S$, $Q_\Omega$, $\bar Q$, $\langle\cdot\rangle$ | $Q_S$, $Q_\Omega$, $(\cdot)_e$, $\langle\cdot\rangle_u$ | **collision:** the source's overbar is an element average, $\langle\cdot\rangle$ an average over unresolved elements |
| $X_S$, $X_\Omega$, $X$ | same (page-local) | shear, rotation and combined measures in $[0,1]$ |
| $\varepsilon$, $\bar\varepsilon$, $\eta$ | $\varepsilon$, $\bar\varepsilon_e$, $\eta$ | nondimensional, Eqs. 40–41 |
| $\Delta$ | $\Delta$ | $\mathcal J^{1/3}/\prod(N_i+1)^{1/3}$ |
| $J$ | $\mathcal J$ | |
| $\mu_t=(C_s\Delta)^2\lvert S\rvert$ | $\mu_t$, $C_s$ | $\lvert S\rvert$ not defined in the source |
| $\tau_{ij}$ | $\sigma_{ij}/\mu$ (viscous stress) | **collision:** not the SGS stress |
| $P$ | $p$ | |
| $Re_c$, $Pr_c$, $Ma_c$ | $Re$, $Pr$, $M$ | channel: bulk velocity and half-height |
| $v_i$, $v'_i$, $v_{i,rms}$ | $u_i$, $u_i'$, (rms velocity) | |
| $K$, $TKE$ | (kinetic energy), $k$ | |
| $D$, $R$ | $D$, $R_\Gamma$ (page-local) | sensitivity measure (Eq. 51); energy ratio above the cut-off |

# Reference list

87 printed references, author–year style, alphabetical, with DOIs or URLs
for most items. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Ferrer & Willden
(2011a) and (2011b) are one printed duplicate, folded into one entry. The
cited Liu, Liu & Zhao (2024, J. Sci. Comput. 102, staggered DG for
quasi-Newtonian Stokes flow) is a different work from the ingested Liu et al.
(2024) and takes the key `liu-2024-c`. Mateo-Gabín et al. (2022) and Ferrer et al.
(2023) are the ingested sources of those slugs. Bassi & Rebay (1996), Tadmor
(1994) and Tikhomirov (1991) are printed as chapters without a book title;
Bozorgpour (2024) is an OSF preprint with a URL for DOI; Mostafavi et al.
(2024a) and Ranjbar et al. (2024b) are meeting abstracts; Xi & Ji (2025) and
Mostafavi (2025b) carry no DOI.

# Pages created or updated

Chunk 7 (2026-10-26). This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Explicit modal filtering as an LES closure](/methods/explicit-modal-filtering.md)
- [Mesh adaptation for turbulent-flow simulation](/methods/mesh-adaptation.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
- [Entropy conservation and entropy stability](/properties/entropy-conservation.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
- [HORSES3D](/software/horses3d.md)
