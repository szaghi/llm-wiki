---
type: Source
title: "Pirozzoli (2011b) — Stabilized non-dissipative approximations of Euler equations in generalized curvilinear coordinates"
description: "Extends kinetic-energy-preserving split convective forms to central finite differences of any order on curvilinear meshes: the Jacobian is absorbed into the density or the contravariant velocity, the Kennedy–Gruber U/J split is written as a locally conservative two-point flux, and it is tested on vortex advection over smooth and randomized meshes and on colliding vortex dipoles against filtered and unfiltered divergence-form central differencing."
resource: "doi:10.1016/j.jcp.2011.01.001"
source_kind: paper
authors: [Pirozzoli S.]
year: 2011
venue: "J. Comput. Phys. 230:2997-3014"
local_file: "/home/stefano/papers/mosaic/weno-teno/2011_Crossref_Journal_of_Computational_Physics_Pirozzoli_Stabilized_non-dissipative_approximations_of_Euler_equations.pdf"
tags: [kinetic-energy-preserving, finite-difference, central-scheme, low-dissipation, turbulence]
timestamp: 2026-11-17T08:42:21Z
---

# Summary

Pirozzoli (2011b) asks how to stabilize non-dissipative central finite differences of the
compressible Euler equations on curvilinear meshes without upwinding or filtering. The answer
is to carry the kinetic-energy-preserving [split convective forms](/methods/split-convective-forms.md)
over to the strong conservation form ([KEP split forms in curvilinear coordinates](/methods/curvilinear-kinetic-energy-preserving-split-forms.md)).
The Jacobian has to be absorbed into the density (RHO/J) or into the contravariant velocity
(U/J); absorbing it into the transported scalar fails. With Feiereisen's or Kennedy–Gruber's
split and central operators that are [summation-by-parts](/operators/summation-by-parts-operator.md)
on a periodic grid, both choices conserve the volume-weighted discrete kinetic energy
([kinetic energy preservation](/properties/kinetic-energy-preservation.md)).

The Kennedy–Gruber split with the Jacobian in the velocity (KG-U/J) is retained and written,
after the author's 2010 paper, as a locally conservative flux difference with a triple-product
two-point average, which is cheap and ready for hybrid shock capturing
([local conservation and flux form](/results/local-conservation-flux-form.md),
[flux differencing](/methods/flux-differencing.md)). Metrics are computed with the same
central operator ([free-stream preservation](/properties/free-stream-preservation.md)). In 2D
tests with fourth-order Runge–Kutta, the scheme (SCFD) is compared with divergence-form
central differencing (DFD) and with DFD plus an eighth-order
[compact low-pass filter](/methods/compact-low-pass-filter.md) (FDFD). The tests are an
[isentropic vortex](/benchmarks/isentropic-vortex.md) on a smooth wavy mesh and on a
randomized mesh, and the head-on collision of two Lamb–Chaplygin dipoles (the paper cites Lamb only; the name is the compiler's identification). SCFD conserves the
kinetic energy where DFD blows up and FDFD drifts. It is not robust on a randomized mesh, and
it is noisy for the dipoles unless a little physical viscosity is added. The author calls
kinetic-energy stability "a rather weak form of nonlinear stability" in curvilinear
coordinates.

# Version read

Version of record, J. Comput. Phys. 230 (2011) 2997–3014, 18 pages, all read. `pdftotext`
garbles every display equation, so Eqs. (1)–(36), the two mesh mappings and the dipole field
were read from 150 dpi page renders, Figs. 6 and 13 from the renders, and the dipole mapping
again at 200 dpi. Received 18 August 2010, revised 20 December 2010, accepted 4 January
2011, available online 13 January 2011. Single author, Università degli Studi di Roma "La
Sapienza". The DOI is printed on page 1 and matches the published identity. Bundle label:
Pirozzoli (2011b); the Annual Review of Fluid Mechanics review of the same year is
[Pirozzoli (2011a)](/sources/pirozzoli-2011.md).

# Key claims

Registry notation. The source's $J$ is the determinant of $\partial\xi_j/\partial x_k$, the
**reciprocal** of the registry's Jacobian $J$; its $J_{jk}/J$ is the registry's
$(Ja^{(j)})_k$. Registry §10: $\xi_j$ computational coordinates with unit spacing, $\hat v_j=Ja^{(j)}\cdot v$
(the source's $\hat u_j$), $\delta_j$ with weights $\mathsf a_\ell$ and
half-width $L_{\mathrm s}$ the central operator (the source's $D_j$, $a_\ell$, $L$),
$\{\!\{a\}\!\}_{k,\ell}=\tfrac12(a_k+a_{k+\ell})$, $\alpha_{\mathrm{KG}},\beta_{\mathrm{KG}}$ the
Kennedy–Gruber parameters. Page-local: $\phi$ the transported scalar, $d$ a direction index.

1. Strong conservation form after Vinokur: $J\partial_tu+\sum_j\partial_{\xi_j}(\rho\hat v_j,\ \rho v\hat v_j+p\,Ja^{(j)},\ \rho H\hat v_j)=0$ for a time-independent, locally invertible, smooth map; without pressure every component is $J\partial_t(\rho\phi)+\sum_j\partial_{\xi_j}(\rho\hat v_j\phi)=0$, $\phi\in\{1,v_i,H\}$ (§2, Eqs. (1)–(2)). **Stated**
2. The central operator $\delta_jf_i=\sum_{\ell=1}^{L_{\mathrm s}}\mathsf a_\ell(f_{i+\ell}-f_{i-\ell})$ has order $2L_{\mathrm s}$ for maximum-order weights; DRP weights are allowed (Eqs. (3)–(4)). **Stated**
3. With continuity and momentum split by the same rule, the Feiereisen form, and the Kennedy–Gruber form "only for $\alpha=\beta=1/4$", preserve kinetic energy semi-discretely under exact time integration; Blaisdell's split stabilizes by minimizing aliasing (§2.1, Eqs. (6)–(8)). **Stated** (proved for Feiereisen)
4. The Cartesian proof: momentum times $v_i$ minus continuity times $\tfrac12\lvert v_i\rvert^2$ leaves $\tfrac12\sum_dv_i\cdot\delta_d(\rho v_dv)_i+\tfrac12\sum_d(\rho v_dv)_i\cdot\delta_dv_i$ at node $i$ ($v_d$ the $d$th velocity component), which sums to zero by SBP; on a periodic direction SBP reads $\sum_if_i\delta_jg_i+\sum_ig_i\delta_jf_i=0$ and "holds for central (both explicit and implicit) approximations of any order" (Eqs. (9)–(12), citing Strand and Mansour et al.). **Derived**
5. These split forms are "often referred to as 'skew-symmetric'", which "is not strictly correct in mathematical terms", since the integral of $\rho\varphi^2$ "is not preserved in time" (§2.1). **Stated** (see Notation map and the qualification on the [split-forms page](/methods/split-convective-forms.md))
6. Absorbing the Jacobian into $\phi$ does not give a counterpart of the Cartesian case, because continuity then transports $J\ne1$ (the source's $1/J$) and an extra term appears; absorbing it into the density (RHO/J, Eqs. (13)–(15)) or into the velocity (U/J, Eqs. (17)–(19)) gives conservation of $\sum_iJ_i\kappa_i$, "a legitimate discrete surrogate for the kinetic energy" (§2.2, Eq. (16)). **Derived**
7. The Kennedy–Gruber split also preserves kinetic energy in both formulations. It is more robust than Feiereisen's, which the flux form explains ("density variations are more effectively averaged out"), and U/J is more robust than RHO/J in preliminary tests; of the "four combinations", KG-U/J is retained (§2.2, Eq. (20)). **Stated**
8. The pressure gradient can be centrally differenced "without major drawbacks"; the split $\partial_{\xi_j}(p\,Ja^{(j)})=\tfrac12\partial_{\xi_j}(p\,Ja^{(j)})+\tfrac12p\,\partial_{\xi_j}Ja^{(j)}+\tfrac12Ja^{(j)}\,\partial_{\xi_j}p$ (printed with the unscaled $J_{ji}$, see Printed slips) gives "marginally superior robustness" (§2.2, Eq. (21)). The full semi-discretization is Eq. (22). The total-energy equation is kept; internal-energy or entropy (Honein & Moin) and sound-speed (Kok) equations are recalled as more robust options. **Stated**
9. Franck & Colonius's curvilinear split (Eq. (23)) is more stable than the unsplit form but "does not guarantee discrete energy preservation from convection", whereas the RHO/J form does (§2.2). **Stated**
10. Following Pirozzoli (2010), the KG split has the face flux $2\sum_{\ell}\mathsf a_\ell\sum_{m=0}^{\ell-1}\{\!\{\rho\}\!\}\{\!\{\hat v_j\}\!\}\{\!\{\phi\}\!\}$ over the pairs $(i-m,i-m+\ell)$, the pressure the analogous $\{\!\{p\}\!\}\{\!\{Ja^{(j)}\}\!\}$; the resulting scheme, $\frac{du_i}{dt}=-\frac1{J_i}\sum_j(\hat F^{(j)}_{i+1/2}-\hat F^{(j)}_{i-1/2})$, is "entirely equivalent to (but computationally less expensive than)" Eq. (22) (§2.3, Eqs. (24)–(30)). **Stated** (equivalence from [17]) *(compiler check, not in the sources: equal to round-off for $L_{\mathrm s}=1,\dots,4$ in 1D on random periodic data)*
11. The flux form gives global conservation by telescoping, simple insertion into existing conservative solvers and straightforward hybridization with shock capturing; storing the averages line by line has "insignificant" memory overhead (§2.3). **Stated** (hybridization untested)
12. All metrics are computed with the convective operator, $\partial x_k/\partial\xi_j\approx\delta_jx_k$, "to minimize sources of errors associated with failure to preserve the undisturbed free-stream conditions" (§3, Eq. (33)). **Stated**
13. The comparison filter is Visbal & Gaitonde's compact family at eighth order, $\alpha_{\mathrm P}=0.495$, "a minimum amount of artificial damping", applied to all variables in all directions after each Runge–Kutta step (§3, Eq. (34)). Over DFD, FDFD costs about 30 % and SCFD about 50 % (§3). **Stated**
14. Vortex on the smooth $81\times41$ Kawai–Lele mesh, $M_{\mathrm v}=M_\infty=0.1$ and $0.5$, to $tu_\infty/r_{\mathrm v}=720M_{\mathrm v}$: DFD diverges before the final time; second order is "extremely poor"; contours become rounder with order, SCFD somewhat better "especially for the strong vortex"; SCFD velocity profiles match FDFD, with dispersive oscillations in the strong vortex "better controlled through filtering" (§3.1.1, Figs. 2–5). **Shown**
15. Kinetic energy: SCFD conserves $\sum_iJ_i\kappa_i$ "with very good accuracy" at every order for the weak vortex; DFD always diverges with growing energy; FDFD drifts up or down with the order (up to about $1.5\times10^{-3}$, read from Fig. 6a). For the strong vortex energy oscillates between kinetic and internal modes, and SCFD drifts less than FDFD (Fig. 6). **Shown**
16. At $L_{\mathrm s}=3$ the error norms "scale consistently with the nominal order of accuracy on the curvilinear mesh" (§3.1.1, Fig. 7). **Shown**
17. Randomized $51\times51$ mesh (20 % random displacement), $M_{\mathrm v}=0.0012$: both SCFD and, less, FDFD show dispersive oscillations that "eventually lead to divergence"; FDFD by unbounded growth of the velocity maximum, SCFD keeping it while "oscillations become wilder" (§3.1.2, Fig. 9). **Shown**
18. Dipole collision on a distorted $60\times60$ mesh, eighth order: inviscid SCFD positions the dipoles correctly with "substantial numerical dispersion associated with mesh distortion", smoother on a uniform grid; at $\mathrm{Re}=1000$ SCFD and FDFD are "virtually indistinguishable" (Fig. 12) and their kinetic-energy histories nearly coincide with a $400\times400$ Cartesian run (Fig. 13); DFD is stabilized only for $\mathrm{Re}\lesssim100$ (not shown) (§3.2, Figs. 12–13). **Shown**
19. FDFD keeps less kinetic energy than SCFD over long times, "although minimal" dissipation; the inviscid SCFD enstrophy grows (about 11 % by the end, read from Fig. 13b), "significant small-scale energy pile-up"; FDFD keeps it nearly constant inviscid but "significantly lower" in the resolved case (§3.2, Eq. (36), Fig. 13). **Shown**
20. Arbitrary order is possible "at least for smooth meshes"; finite volumes or immersed boundaries remain needed for complex geometries or non-smooth meshes; the scheme is offered for DNS and LES with "superior computational efficiency over finite-volume methods" (§4). **Stated**
21. The major limitation is the lack of a-priori nonlinear stability for inviscid runs: kinetic energy is not an energy norm, and with the volume weight the velocity can grow large where the mesh is fine without much growth of the total, so "kinetic energy stability is a rather weak form of nonlinear stability for compressible flows in curvilinear coordinates" (§4). **Stated**
22. The dipole is harder than the vortex because its spectrum decays as $k^{-6}$ against exponentially (after Saffman); small viscosity alone controls the dispersive errors; in LES on non-smooth or skewed meshes "judicious use of filtering is still necessary" (§4). **Stated**

Setups (§3). The vortex is a homentropic, zero-circulation vortex after refs. [11,28,7,15],
started at the origin; the wavy mesh is Kawai & Lele's on $[-12,12]\times[-6,6]\,r_{\mathrm v}$ with
amplitudes $0.4r_{\mathrm v}$ and $1.6r_{\mathrm v}$, periodic, and the final time is three (weak) and
fifteen (strong) flow-throughs. The randomized mesh is on $[-6,6]^2r_{\mathrm v}$, with points
inside $\lvert x\rvert,\lvert y\rvert<4.5$ displaced. The dipoles (Eq. (35); exact steady
translation only as $M_{\mathrm v}\to0$, uniform density) start at $(\mp2r_{\mathrm v},0)$ with
$M_{\mathrm v}=0.1$ on $[-4,4]^2r_{\mathrm v}$, periodic, to $tU_{\mathrm d}/r_{\mathrm v}=12\sqrt\gamma$, with
$\mathrm{Re}=U_{\mathrm d}r_{\mathrm v}/\nu_\infty\in\{\infty,10^4,5000,1000\}$ and eighth-order viscous
terms; page-local $U_{\mathrm d}$ the dipole speed.

# Printed slips

- **Pressure metric term.** Eq. (1) has the pressure flux $pJ_{ji}/J$ (inside $f_j/J$), but Eqs. (21), (22), (28), (30) and (31) write $pJ_{ji}$ without $1/J$. Read literally, a uniform pressure would not be steady; the scaled metric of Eq. (1) is evidently meant *(compiler check, not in the sources)*.
- **Fig. 9 caption** prints $M_v=0.012$; the text (§3.1.2) gives $M_v=0.0012$, after Visbal & Gaitonde.
- **Dipole mesh mapping** (§3.2, unnumbered) is printed $x=x_{\min}+\frac3{164\pi}\frac{L_x}{N_\xi-1}\big(\sin(8\pi s)-8\sin(4\pi s)\big)\sin(2\pi t)^4$, $s=\frac{\xi-1}{N_\xi-1}$, $t=\frac{\eta-1}{N_\eta-1}$, and likewise for $y$. It has no term linear in $\xi$ and cannot produce the $8r_{\mathrm v}$-wide mesh of Fig. 10; a linear term $L_xs$ is missing, and the placement of the factor $L_x/(N_\xi-1)$ is not recoverable from the print.
- **Figs. 4–5 captions** announce dotted curves for the KG-RHO/J formulation; no third curve can be told apart in the version of record, so the stated superiority of U/J over RHO/J is not checkable from the figures.
- **§4**: "the vortex swirl given in Eq. (35), and the vortex dipole given in Eq. (35)"; the vortex of §3.1 is unnumbered.
- **Fig. 13** labels its abscissa $tu_\infty/r_v$; the dipole case is timed by $tU/r_v$ (the axis ends near $12\sqrt\gamma\approx14.2$).
- **Eq. (9)** writes $\mathrm d\rho_{\mathcal N}/\partial t$.
- **Typos:** "it does does not guarantee" (§2.2); "It is well know" (§3); "Numerical divergence is curved by the FDFD scheme" (curbed, §3.1.1); "exhibits less energy that the SCFD" (§3.2); "a much smoother solutions was obtained" (§3.2).
- **Reference list:** [2] Lilly is printed in "J. Comput. Phys. 93 (1965) 11–26" (the work is in Mon. Weather Rev. 93); [28] Kawai & Lele is printed "(2007)" for J. Comput. Phys. 227 (2008); [26] prints the pages "386401"; [35] "Phyl. Trans."; [5] spells the co-author "O.V. Vasiliev".

# Notation map

| Pirozzoli (2011b) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\xi_j$, node $\mathcal N=(\xi_1,\dots,\xi_d)$ | $\xi_j$ (registry §10), node index $i$ | unit spacing; not the DG nodes $\xi_j$ |
| $J=\det(\partial\xi_j/\partial x_k)$ | $1/J$ | **reciprocal**: the registry $J$ is the cell volume |
| $J_{jk}=\partial\xi_j/\partial x_k$ | $(Ja^{(j)})_k/J$ | so $J_{jk}/J_{\text{source}}=(Ja^{(j)})_k$ |
| $\tilde u_j=J_{jk}u_k$ | $\tilde v_j=\nabla\xi_j\cdot v$ (registry §10) | contravariant velocity |
| $\hat u_j=\tilde u_j/J$ | $\hat v_j=Ja^{(j)}\cdot v$ (registry §10) | U/J formulation |
| $\hat\rho=\rho/J$ | $J\rho$ | RHO/J formulation |
| $u_i$ | $v_i$ | Cartesian velocity |
| $\mathbf u=(\rho,\rho u_i,\rho E)$, $E$ per unit mass | $u=(\rho,\rho v,E)$ | source $\rho E$ = registry $E$ |
| $H=E+p/\rho$ | $H$ | specific total enthalpy |
| $\varphi$ | $\phi$ (page-local) | transported scalar |
| $D_j$, $a_\ell$, $L$ | $\delta_j$, $\mathsf a_\ell$, $L_{\mathrm s}$ (registry §10) | **collision** of $L$ with $L=R^{-1}$ |
| $(f_{j;\ell})_{\mathcal N}$ | $f_{i+\ell}$ along direction $j$ | shift |
| $\widetilde{(f,g,h)}_{j;n,\ell}$ | $\{\!\{f\}\!\}_{n,\ell}\{\!\{g\}\!\}_{n,\ell}\{\!\{h\}\!\}_{n,\ell}$ | triple product of arithmetic means |
| $\bar f_{j;n,\ell}$ | $\{\!\{f\}\!\}_{n,\ell}=\tfrac12(f_n+f_{n+\ell})$ | |
| $\hat f_{j;1/2}$ | $\hat F^{(j)}_{i+1/2}$ | face flux in direction $j$ |
| $\alpha$, $\beta$ (Kennedy–Gruber) | $\alpha_{\mathrm{KG}}$, $\beta_{\mathrm{KG}}$ (registry §10) | **collision** with $\alpha_k$, $\beta_k$ |
| $K$, $\widehat K$ | $\sum_i\kappa_i$, $\sum_iJ_i\kappa_i$ | discrete total kinetic energy |
| $\omega$, $\widehat\Omega$ | $\omega_{\mathrm v}$, $\tfrac12\sum_iJ_i\omega_{\mathrm v,i}^2$ (page-local) | vorticity and discrete enstrophy; $\omega$ keeps $\omega_k$ |
| $\alpha$, $d_m$, $M$ (filter) | $\alpha_{\mathrm P}$, $a_m$, $n_{\mathrm f}=4$ (registry §10) | as on [compact low-pass filter](/methods/compact-low-pass-filter.md) |
| $h$, $h_j$ | $\Delta x$ | grid spacing (Cartesian case) |
| $M_v$, $M_\infty$, $r_v$, $\hat r$ | $M_{\mathrm v}$, $M_\infty$, $r_{\mathrm v}$ (registry §10), $\hat r$ (page-local) | as on [isentropic vortex](/benchmarks/isentropic-vortex.md) |
| $U$, $\beta$, $C$, $J_0$, $J_1$ (dipole) | $U_{\mathrm d}$, $j_{1,1}\approx3.8317$, $C_{\mathrm d}=2/\mathrm J_0(j_{1,1})$, $\mathrm J_0$, $\mathrm J_1$ (page-local) | **collisions** of $\beta$, $C$, $J$ |
| $Re_v=Ur_v/\nu_\infty$ | $\mathrm{Re}$ | $\nu_\infty$ kinematic viscosity, not the CFL number |
| Courant number | $\nu$ | 0.25 |

# Reference list

The paper prints 35 references, numbered [1]–[35] in order of first citation, merged complete
into the [bibliography](/bibliography.md) with `citedby` including `pirozzoli-2011-b`. [17] is
the ingested [Pirozzoli (2010)](/sources/pirozzoli-2010.md), the source of the flux form. [11]
is Visbal & Gaitonde (2002), J. Comput. Phys. 181, credited with the filter and the
free-stream practice; Lele (1992) is [34], cited for the second-derivative approximations.
[7] and [18] are CTR Annual Research Briefs without pages; [3] (Orlandi) is printed with the
publisher Kluwer; [21] prints "scheme" for the published "schemes"; [24] (Kennedy & Gruber)
has a truncated title. The misprints of [2], [5], [26], [28] and [35] are listed above. No
item is unparseable.

# Pages created or updated

Chunk 14 (2026-11-17). This source is cited on:

* [Artificial viscosity and spectral viscosity](/methods/artificial-viscosity.md)
* [Compact low-pass filter](/methods/compact-low-pass-filter.md)
* [Conservative split central derivative](/operators/conservative-split-derivative.md)
* [Flux differencing and split-form DG](/methods/flux-differencing.md)
* [Free-stream preservation](/properties/free-stream-preservation.md)
* [Hybrid central-WENO schemes](/methods/hybrid-weno.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Kinetic energy preservation](/properties/kinetic-energy-preservation.md)
* [Kinetic-energy-preserving split forms in curvilinear coordinates](/methods/curvilinear-kinetic-energy-preserving-split-forms.md)
* [Local conservation is equivalent to a flux form](/results/local-conservation-flux-form.md)
* [Split convective forms](/methods/split-convective-forms.md)
* [Summation-by-parts operator](/operators/summation-by-parts-operator.md)
