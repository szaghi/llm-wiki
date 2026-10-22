---
type: Source
title: "Browne et al. (2022) — A nonlinear compressible flow disturbance formulation for adaptive mesh refinement wavepacket tracking in hypersonic boundary-layer flows"
description: "Nonlinear disturbance equations for the compressible Navier–Stokes equations, discretized by fifth-order finite-difference WENO with a disturbance-form Rusanov splitting on a block-structured AMR mesh that tracks the wavepacket, validated on a Mach 9.81 cone and a Mach 5.35 flat plate."
resource: "doi:10.1016/j.compfluid.2022.105395"
source_kind: paper
authors: [Browne O.M.F., Haas A.P., Fasel H.F., Brehm C.]
year: 2022
venue: "Comput. Fluids 240:105395"
local_file: "/home/stefano/papers/mosaic/weno-teno/2022_Crossref_Computers_amp_Fluids_Browne_A_nonlinear_compressible_flow_disturbance_formulation_for_ad.pdf"
tags: [weno, finite-difference, numerical-flux, amr, turbulence]
timestamp: 2026-10-22T20:00:00Z
---

# Summary

The paper presents the nonlinear adaptive-mesh-refinement wavepacket-tracking method
(nonlinear AMR-WPT). It computes the linear and nonlinear evolution of pulse-generated
wavepackets in hypersonic boundary layers at a fraction of the cost of a direct numerical
simulation (DNS). It extends the authors' earlier linear, two-dimensional AMR-WPT to three
dimensions and to nonlinear disturbances.

The core is a set of nonlinear disturbance equations (NLDE, after Morris et al.). The
conserved state, the primitive state and the fluxes of the compressible Navier–Stokes
equations are split exactly into a steady baseflow $u_{\mathrm b}$, a linear disturbance and a
nonlinear disturbance, and the equations are solved for the disturbance $u'=u-u_{\mathrm b}$
only. Dropping the nonlinear terms gives the linear disturbance equations. The convective
disturbance fluxes are discretized by fifth-order finite-difference
[WENO-JS](/methods/weno-js-reconstruction.md) with
[characteristic decomposition](/methods/characteristic-decomposition.md) on a
[conservative finite-difference](/definitions/conservative-finite-difference-scheme.md)
stencil. The flux splitting is a disturbance form of the
[Rusanov (local Lax–Friedrichs) splitting](/methods/lax-friedrichs-flux.md): the paper argues
that subtracting the baseflow split flux from the total-flow split flux leaves a term
$a'u_{\mathrm b}$ that is inconsistent with the Rusanov definition, and it adopts a
[dissipation](/definitions/numerical-dissipation.md) $a\,u'$ instead. Viscous terms are
second-order central, in a non-conservative chain-rule form. Time stepping is classical
Runge–Kutta (fourth or second order), not [SSP](/methods/ssp-runge-kutta.md).

The baseflow lives on a body-fitted curvilinear mesh. The disturbance lives on a
[block-structured AMR](/methods/adaptive-mesh-refinement.md) Cartesian mesh (a customized
PARAMESH) that follows the wavepacket. The baseflow is interpolated onto it by least squares
over donor cells found by a Newton search, and refinement uses a normalized composite
indicator of disturbance vorticity, pressure, pressure gradient and temperature. A
[manufactured-solution](/definitions/method-of-manufactured-solutions.md) study gives about
sixth-order observed convergence of the convective right-hand side and second order with
viscous terms. On a Mach 9.81 cone and a Mach 5.35 flat plate the wavenumber–frequency
spectra agree with DNS and linear stability theory, with on average 60% (linear) and 9%
(strongly nonlinear) of the DNS grid points.

# Version read

Version of record (Elsevier typeset, Comput. Fluids 240, 105395), 23 pages, all read;
equations on pp. 3, 4 and 6 checked visually because the text layer garbles them. Page 1
matches Crossref in title, venue and DOI. Page 1 prints the first author as "Oliver M.F.
Browne" (initials O.M.F.), where Crossref has "Browne O.M."; page 1 is followed. Equation,
table and figure numbers cited here are those of this version.

# Key claims

Registry notation (see the notation map): baseflow $u_{\mathrm b}$, disturbance $u'$, total
spectral radius $a=\lvert v_1\rvert+c$, baseflow and disturbance parts $a_{\mathrm b}$ and
$a'=a-a_{\mathrm b}$, convective disturbance flux $f'$.

1. The NLDE are an exact reformulation of the compressible Navier–Stokes equations: baseflow plus NLDE disturbance gives the same total solution as a DNS, since no assumption or approximation enters the derivation of Eq. (41) from Eq. (1) (§2.2, Eqs. (9)–(41)). **Derived** (see Printed slips for the viscous terms)
2. Solving for the disturbance directly reduces round-off error when disturbances are orders of magnitude below the mean flow, helps in single precision (e.g. on GPUs), and allows separate boundary conditions for baseflow and disturbance (§1, citing Hansen et al.). **Stated**
3. The NLDE reduce to the linear disturbance equations by switching off the nonlinear disturbance terms; these hold while the nonlinear part is small against $u_{\mathrm b}$, and nonlinear terms matter for disturbances of order 1% of the baseflow or more, case dependent (§2.2). **Stated**
4. Writing the total-flow Rusanov splitting in disturbance form and subtracting the baseflow split flux gives $f'^\pm=\tfrac12\big(f'\pm\{a_{\mathrm b}u'+a'(u_{\mathrm b}+u')\}\big)$, which is "not consistent with the formal definition of the Rusanov flux"; the extra term $a'u_{\mathrm b}$ "will negatively affect the stability properties" (§2.2, Eqs. (18)–(19)). **Stated** (no stability analysis or numerical comparison)
5. The NLDE Rusanov splitting is defined as $f'^\pm=\tfrac12\big(f'\pm(a_{\mathrm b}+a')u'\big)=\tfrac12(f'\pm a\,u')$, and for the linear disturbance equations as $\tfrac12(f'\pm a_{\mathrm b}u')$, dropping $O(u'^2)$ (Eqs. (21)–(22)). **Derived**
6. The eigenvalues of the disturbance flux Jacobian equal those of the total-flow Jacobian (Eq. (20)). **Stated**
7. Interpolating baseflow primitive variables and differentiating on the disturbance mesh, or interpolating baseflow derivatives directly, gave the same solutions here because the baseflow meshes are of high quality; interpolating derivatives reduces noise from non-smooth solutions at the cost of storage (§2.2, after Eq. (30)). **Shown** (asserted, no figure)
8. The interpolated baseflow is steady on the baseflow mesh but its residual on the disturbance mesh is non-zero; the steady residuals of the AMR and static meshes agree closely, "confirming the baseflow is a valid input to the NLDE" (§3.3, Eq. (63), Fig. 6). **Shown**
9. Refinement interval: $n_R=\Delta t_{x,b}/\Delta t$ with $\Delta t_{x,b}=\Delta x\,n_{x,b}/(v_1+c)$, the time the fastest wave takes to cross a block of $n_{x,b}$ points (§3.4, Eqs. (64)–(65)). **Derived**
10. A composite refinement function of disturbance vorticity, pressure, pressure gradient and (away from the wall) temperature is a good compromise of efficiency and accuracy; the pressure gradient, 90° out of phase with pressure, fills the gaps in the mesh between pressure peaks (§3.4, Figs. 8–10). **Shown**
11. The disturbance mesh is forced to be finer than the baseflow mesh in the wall-normal direction, which over-resolves it (§3.4, §5). **Stated**
12. Baseflow and disturbance solvers use fifth-order WENO for convective terms and second-order central differences for viscous terms; the baseflow is driven to steady state with first-order backward differencing in pseudo-time; disturbances are integrated with fourth-order Runge–Kutta (§4.1), but §5 and Table 6 report second-order Runge–Kutta for the AMR-WPT runs, chosen after temporal convergence studies as a factor-two speed-up. **Stated** (see Printed slips)
13. The cone baseflow agrees with Balakumar & Chou except near the nose ($x=0.2$ m), where the shock is "more sharply captured in the current simulation" (§4.1, Fig. 11a). **Shown**
14. Mach 9.81 cone, linear pulse: AMR-WPT amplitude curves agree with static-WPT and time-spectral solutions; small discrepancies near the domain end come from streamwise under-resolution of the static-WPT mesh; the AMR-WPT solution is grid-converged (§4.2.1, Fig. 14). **Shown**
15. Mach 9.81 cone, nonlinear pulse: the wavepacket saturates when pressure disturbances reach the order of $p_\infty=607.78$ Pa (at $x=1.25$ m); harmonics $2f,3f,4f$ and a rise near $f=0$ appear; the wavepacket splits in two downstream; the instability is second-mode dominated (§4.2.1, Figs. 12–16). **Shown**
16. N-factor slopes from linear AMR-WPT agree with linear stability theory and parabolized stability equations; the onset location and maximum N differ, partly because the latter use a different amplitude measure (§4.2.1, Eq. (69), Fig. 17). **Shown**
17. Mach 5.35 flat plate, 2D: linear AMR-WPT agrees with the 3D DNS (spanwise mode 0) and with 2D static-WPT, and captures the initial rise of the wall-pressure amplitude against linear stability theory (§4.3, Fig. 21). **Shown**
18. Mach 5.35 flat plate, 3D: AMR-WPT wavenumber–frequency spectra at $x=0.3,0.4,0.5$ m agree with DNS for linear (run 2a) and strongly nonlinear (run 2b) pulses, including the second mode, subharmonics and higher harmonics (§4.3, Figs. 23–26). **Shown**
19. The pulse spectrum is largest in $190<f<320$ and $-12<k<12$, and the initial disturbance field scales linearly between the linear and strongly nonlinear cases (§4.3, Fig. 22). **Shown**
20. Linear and rescaled nonlinear wavepackets coincide at $x=0.2,0.3$ m, differ at 0.4 m and show a second envelope peak at 0.5 m; beyond 0.5 m nonlinear mechanisms dominate, and the strongly nonlinear case amplifies a low-frequency (possibly first-mode) region (§4.3, Figs. 20, 27). **Shown**
21. Grid points: DNS $2080\times300\times147\approx91.7\times10^6$ (fourth-order Runge–Kutta, Fourier in span) against AMR-WPT $\approx55\times10^6$ on average for the linear case; DNS $8764\times320\times255\approx715\times10^6$ against $\approx66\times10^6$ for the strongly nonlinear case, i.e. 60% and 9% (§5, Table 6). **Shown**
22. Timings are omitted (different solvers and hardware); with "a mesh size which is about 5% of the size for a conventional approach, the speed up is still roughly an order of magnitude even when accounting for the slight overhead in operation count" (§5). **Stated** (see Printed slips)
23. Refinement overhead is small: about 130,000 time steps with only 520 refinement steps for the 3D flat plate (§5). **Shown**
24. DNS cost scales with the geometry, AMR-WPT cost with the size of the wavepacket (§5). **Stated**
25. Manufactured solutions: the 3D NLDE convective right-hand-side operator converges at observed order about 5.8–6.0 in $L_2$, and the convective plus viscous operator at about 1.9–2.0, consistent with fifth-order convective and second-order viscous operators (App. A, Tables A.1–A.2, Fig. A.30). **Shown**
26. The abstract and conclusions state that AMR-WPT requires "only about 10%" of the DNS grid points for a nonlinear wavepacket on the flat plate (Abstract, §6). **Shown** (the 9% of claim 21)

# Printed slips

- §2.2, after Eq. (19): "The local speed of sound is computed as $\partial p/\partial\rho|_s=\sqrt{\gamma p/\rho}$"; $\partial p/\partial\rho|_s$ is $c^2=\gamma p/\rho$, not $c$.
- §2.2 (p. 5): the baseflow temperature gradients are listed as "$(\partial\bar T/\partial x,\partial\bar T/\partial y,\partial\bar T/\partial y)$"; the third should be $\partial\bar T/\partial z$.
- Eqs. (35)–(36) write the gradient of the disturbance viscosity as $\frac{\partial\tilde\mu}{\partial\tilde T}\frac{\partial\tilde T}{\partial x}$ with $\partial\tilde\mu/\partial\tilde T=\partial\mu/\partial T$, while Eq. (31) defines $\tilde\mu=\mu(T)-\mu(\bar T)$. The exact chain rule gives $\partial_x\tilde\mu=\mu'(T)\,\partial_x\tilde T+\big(\mu'(T)-\mu'(\bar T)\big)\partial_x\bar T$, so the printed form drops the last term, against the "no approximation" claim of §2.2. *(compiler check, not in the sources: differentiation of Eq. (31).)*
- §4.2.1: the cone disturbance domain is printed "$x\in[0.1\text{ m},0.14\text{ m}]$", yet the pulse is at $x\approx0.4$ m and results are reported at $x=1.0$ and 1.25 m (Figs. 13, 16, 17).
- §4.1 says the disturbance equations are integrated with fourth-order Runge–Kutta; Table 6 and §5 give second order for both AMR-WPT runs.
- §5: "a mesh size which is about 5% of the size for a conventional approach" contradicts Table 6 (60% and 9%) and the abstract's "about 10%".
- Table A.2: two entries lack the slash separator ("1.928 1.884", "1.91 2.003"); one $m_y$ entry is printed "1.6457/1.874".
- Table A.1: the continuity $L_\infty$ order falls to 1.672 and 0.971 at the two finest meshes, without comment.
- References [27] and [29] are printed identically (Erwin, Morris & Brentner, AIAA 2009-272).
- Typos: "thee-dimensional" (§4.3), "max/mix contour levels" (Fig. 19), "Federov [3]" for the printed "Fedorov" (§1), "Sivasubramian" for "Sivasubramanian" (§4.1), "non-Local" (Table 1).

# Notation map

| Browne et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf W=(\rho,\rho u,\rho v,\rho w,\rho E_t)$ | $u=(\rho,\rho v,E)$ | conserved state; $\rho E_t=E$ |
| $u,v,w$ | $v_1,v_2,v_3$ | velocity |
| $\bar{(\cdot)}$, $\tilde{(\cdot)}$ | $(\cdot)_{\mathrm b}$, $(\cdot)'$ (page-local) | baseflow and disturbance; **$\bar u_i$ is the cell average and $\tilde u$ a normalized value in the registry** |
| $\tilde{\mathbf W}_l$, $\tilde{\mathbf W}_{nl}$ | $u'_{\mathrm l}$, $u'_{\mathrm{nl}}$ | linear and nonlinear disturbance parts |
| $\mathbf Q=(p,u,v,w,T)$ | kept as primitive state | |
| $\mathbf E_c$, $\tilde{\mathbf E}_c$ | $f$, $f'$ | convective flux in $x$ and its disturbance part; **$\mathbf E$ collides with the total energy $E$** |
| $\mathcal F^\pm_{Rus}$ | $f^\pm$ | Rusanov (local Lax–Friedrichs) split fluxes |
| $\lambda$, $\bar\lambda$, $\tilde\lambda$ | $a$, $a_{\mathrm b}$, $a'$ | spectral radius $\lvert v_1\rvert+c$ and its baseflow and disturbance parts |
| $\mathcal J$, $\tilde{\mathcal J}$ | $A$, $A'$ | flux Jacobians |
| $\bar\Omega$, $\tilde\Omega$ | kept | baseflow (body-fitted) and disturbance (AMR) meshes |
| $\bar{\mathcal N}$ | kept | baseflow spatial operator; registry $\mathcal L$ is the semi-discrete operator |
| $\mu$, $\kappa$, $Pr$ | $\mu$, kept, $\mathrm{Pr}$ | viscosity, conductivity; **$\kappa$ is the kinetic energy in the registry** |
| $n_R$, $n_{x,b}$, $\varphi$, $\varphi_u$, $\varphi_l$, $L_{max}$ | kept | refinement interval, points per block, refinement function, thresholds, levels; **$\varphi$ collides with the GQL constraint function $\varphi_i$** |
| $\alpha$ | kept per use | streamwise wavenumber, interpolation coefficients and MMS wavenumbers; **collides with $\alpha_k$** |
| $\epsilon$ | kept per use | small parameter and MMS step; **not the weight regularization** |
| $k$, $f$ | kept | spanwise mode number and frequency |

# Reference list

53 printed references in numbered style ([1]–[53]), all parsed and merged complete into the
[bibliography](/bibliography.md) with `citedby` `browne-2022`. [27] and [29] are printed
duplicates of one AIAA paper; [36] is a web user guide, [46] a private communication, [16]
an arXiv preprint, [21] a thesis and [52] a Sandia report. DOIs are printed only for [37] and
[51].

# Pages created or updated

Chunk 3 (2026-10-22). This source is cited on:

* [Block-structured adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)
* [Characteristic decomposition](/methods/characteristic-decomposition.md)
* [Conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [Method of manufactured solutions](/definitions/method-of-manufactured-solutions.md)
* [Numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [WENO-JS reconstruction](/methods/weno-js-reconstruction.md)
