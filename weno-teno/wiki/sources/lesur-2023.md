---
type: Source
title: "Lesur et al. (2023) — IDEFIX: A versatile performance-portable Godunov code for astrophysical flows"
description: "Code paper for IDEFIX, a Kokkos-based C++17 second-order Godunov finite-volume code for astrophysical hydrodynamics and non-ideal MHD on Cartesian and curvilinear grids, with constrained transport, super time-stepping and orbital advection, validated on standard tests and benchmarked on CPUs and GPUs up to 1024 GPUs."
resource: "doi:10.1051/0004-6361/202346005"
source_kind: paper
authors: [Lesur G.R.J., Baghdadi S., Wafflard-Fernandez G., Mauxion J., Robert C.M.T., Van den Bossche M.]
year: 2023
venue: "Astron. Astrophys. 677:A9"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Astronomy_amp_Astrophysics_Lesur_IDEFIX_A_versatile_performance-portable_Godunov_code_for_ast.pdf"
tags: [software, gpu, mhd, finite-volume, riemann-solver, performance]
timestamp: 2026-10-23T10:00:00Z
---

# Summary

[IDEFIX](/software/idefix.md) is a finite-volume Godunov code for non-relativistic
hydrodynamics and MHD of astrophysical flows, written in C++17 on the Kokkos
performance-portability library so that one source runs on Intel and AMD CPUs and
on NVIDIA and AMD GPUs. It re-writes the design of PLUTO (reconstruct–solve–average,
near-identical input files and outputs) with three deliberate differences: the
pressure is part of the momentum flux, reconstruction acts on primitive variables
without [characteristic decomposition](/methods/characteristic-decomposition.md),
and the hyperbolic and parabolic time-step limits are combined point-wise.

The numerics are standard and recalled, not new: flat, van Leer-limited linear,
LimO3 and extremum-preserving PPM reconstruction; the
[Rusanov](/methods/lax-friedrichs-flux.md), [HLL, HLLC and HLLD](/methods/hll-riemann-solvers.md)
and [Roe](/methods/roe-riemann-solver.md) solvers, ranked "from most to least
diffusive" ([numerical dissipation](/definitions/numerical-dissipation.md));
constrained transport for the [divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
with several EMF reconstructions and an optional vector-potential form;
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md) stepping of orders 1–3;
Runge–Kutta–Legendre super time-stepping for parabolic terms; non-ideal MHD
(Ohmic, ambipolar, Hall); conservative orbital advection; shearing boxes. The code
is globally second order and has no [AMR](/methods/adaptive-mesh-refinement.md).

Validation (§4) runs the [Sod shock tube](/benchmarks/sod-and-lax-shock-tubes.md),
[double Mach reflection](/benchmarks/double-mach-reflection.md) (where the least
diffusive schemes start [Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md)
rolls), the [Sedov blast wave](/benchmarks/sedov-blast-wave.md) through the polar
axis, the [Brio–Wu shock tube](/benchmarks/brio-wu-shock-tube.md), linear MHD wave
convergence, the [magnetized rotor](/benchmarks/mhd-blast-wave.md), the
[Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md), non-ideal shocks and
shearing waves. PPM stops converging at high resolution on linear MHD waves, so
LimO3 is recommended. Performance (§5, 3D Orszag–Tang) reaches 1240 Mcell/s per
4×MI250X node, 49.6 times an Intel Cascade Lake node; weak scaling stays above
95% to 1024 MI250X GCDs; GPUs pay off only for sub-domains above $64^3$. No
theorem is proved.

# Version read

arXiv:2304.13746v1 [astro-ph.IM], 26 Apr 2023: the A&A proof-stage manuscript
("A&A proofs: manuscript no. idefix", dated April 28, 2023), not the typeset
version of record, 18 pages, all read; the equations of pp. 2–5 and 7–10 were
checked on the page images. Page 1 matches Crossref (title, six authors); the
DOI and article number A9 come from Crossref and are not printed in the file.
Section, equation, table and figure numbers are those of this version.

# Key claims

Registry notation: conserved variables $u$, primitive $(\rho,v,B,p)$, total
energy $E$; the source's $\sigma_{\mathrm{CFL}}$ is the CFL number $\nu$, its
$c_{\max,d}$ the maximum wave speed $a$ in direction $d$.

1. IDEFIX evolves cell-averaged conserved quantities with face- and time-averaged fluxes by the reconstruct–solve–average approach, intentionally close to PLUTO (§2.2, Fig. 1). **Stated**
2. Reconstruction acts on primitive variables $(\rho,v,B,p)$, avoiding characteristic decomposition "while keeping the basic physical constraints (density and pressure positivity for instance)" (§2.3). **Stated** (no positivity proof)
3. Reconstructions: flat (first order), linear with van Leer limiter (second), LimO3 "compact 3rd order reconstruction (up to 4th order accurate)", extremum-preserving PPM "4th order accurate on regularly spaced grids"; footnote 1: "the code is still at most globally second order" (§2.3). **Stated**
4. The Riemann solvers, "from most to least diffusive", are Rusanov, HLL, HLLC (HLLD in MHD) and Roe, selectable at run time (§2.3). **Stated**
5. The pressure is in the momentum flux and solved by the Riemann solver (PLUTO treats it as a source), which creates extra pressure source terms in non-Cartesian geometry, so IDEFIX and PLUTO results "are expected to differ, even if the same algorithm combination is chosen" (§2.3). **Stated**
6. Constrained transport (Evans & Hawley 1988) keeps $\nabla\cdot B=0$ at machine precision "in principle", but round-off can accumulate over billions of steps, especially with super time-stepping; the vector-potential option ($\partial_tA=-\mathcal E$, $B=\nabla\times A$, $A$ on edges) is "mathematically equivalent to the original CT algorithm" and prevents the accumulation (§2.4, Eqs. 6–8). **Stated**
7. EMF reconstructions: arithmetic average, $\mathcal E^0$, $\mathcal E^c$ (Gardiner & Stone 2005; default, "good trade-off between accuracy, stability and computing time"), and 2D HLL and HLLD Riemann solvers (Mignone & Del Zanna 2021) (§2.4). **Stated**
8. The Hall effect adds the whistler speed to the HLL fan for the magnetic-field fluxes only (after Marchand et al. 2019), with the EMF by arithmetic averaging; a Hall-modified $\mathcal E^c$ "led to numerical instabilities"; the implementation is "known to be diffusive" but stable, and HLL is "our only solver compatible with the Hall effect" (§2.5, §4.2). **Stated**
9. In polar and spherical geometry the azimuthal conserved quantity is the vertical angular momentum, which "guarantees conservation of angular momentum to machine precision" (§2.6). **Stated**
10. Time integration is Euler, RK2 or RK3 in the Shu–Osher convex form $u_s=w_su^*+w^0_su_0$ with the TVD (SSP) coefficients of Gottlieb & Shu (1998) in Table 1 (§2.7, Eq. 9). **Stated** *(compiler check, not in the sources: for a linear stage operator $I+\Delta t\mathcal L$, the RK2 and RK3 rows of Table 1 reproduce the Taylor polynomial of $e^{\Delta t\mathcal L}$ to second and third order.)*
11. The time step combines hyperbolic and parabolic limits point-wise (Eq. 10), a generalization of Beckers (1992), with no dimension pre-factor ($\nu=D\times C_{a,\mathrm{PLUTO}}$), always stable for $\nu<1$; the resulting $\Delta t$ "can be somewhat larger" than PLUTO's (§2.7). **Stated**
12. Second-order Runge–Kutta–Legendre super time-stepping needs $s_{\mathrm{RKL}}\simeq2\sqrt{\Delta t_{\mathrm{hyp}}/\Delta t_{\mathrm{par}}}$ stages for $\Delta t_{\mathrm{hyp}}\gg\Delta t_{\mathrm{par}}$ (Eq. 13), against $2\Delta t_{\mathrm{hyp}}/\Delta t_{\mathrm{par}}$ steps of explicit RK2; the stages are called alternately before and after the main integrator to keep global second order (§2.8). **Stated**
13. With super time-stepping for Ohmic or ambipolar diffusion, the round-off divergence grows as $O(n)$ in the number of cycles, against $O(\sqrt n)$ for the explicit integrator; the vector potential is recommended (§2.8). **Stated** (no figure)
14. The conservative orbital advection of Mignone et al. (2012) conserves mass, angular momentum and magnetic flux and is fully parallel in 3D (§2.9). **Stated**
15. All data and loops live in device memory (Kokkos `View` aliases and `idefix_for` loops); the host handles only I/O, initial conditions and exceptions (§3.1). **Stated**
16. Sequential dimension-by-dimension ghost-zone exchange is generally faster than simultaneous 26-neighbour exchange, especially on NVIDIA GPUs, but would not suit an AMR version (§3.4). **Stated** (timings not shown)
17. Double Mach reflection at 1920×480: LimO3 and PPM, "the least diffusive schemes in IDEFIX", give a more vigorous jet with incipient Kelvin–Helmholtz rolls (§4.1, Fig. 3). **Shown**
18. Brio–Wu: a small post-shock velocity oscillation, "typical of the primitive variable reconstruction used in IDEFIX" (§4.2, Fig. 6). **Shown**
19. Linear MHD waves with linear reconstruction and RK2: all four Riemann solvers are second order (Fig. 7). With HLLD, LimO3 and PPM (with RK3) have lower error than linear reconstruction, but PPM stops converging at high resolution (error plateau about $10^{-2}$ for the slow mode), as does Athena++ with primitive reconstruction; "the LimO3 scheme should be preferred" (§4.2, Fig. 8). **Shown**
20. Orszag–Tang: RK3 + PPM + Roe is the most accurate combination at a given resolution; constrained transport gives $\lvert\nabla\cdot B\rvert\ll10^{-12}$ in all runs (§4.2, Figs. 10–11). **Shown**
21. Ambipolar C-shock: error below 2% with 2 points per diffusion length; super time-stepping takes about 10% of the explicit time to solution at high resolution (§4.2, Fig. 14). **Shown**
22. Hall-dominated shock: the error falls by a factor 3–4 per resolution doubling, "slightly less than second order", ascribed to grid-scale whistler diffusivity; second order is "strictly" recovered with LimO3 or PPM (§4.2, Fig. 15). **Shown** (LimO3/PPM part **Stated**, not shown)
23. Shearing waves follow the linear solution up to $\Omega t\simeq10$; in hydro $v_z$ then diverges, when the radial wavenumber reaches about 17 points per wavelength at $256^3$ (§4.3, Figs. 16–17). **Shown**
24. Single-node performance (3D Orszag–Tang, HLLD, linear, $\mathcal E^c$, RK2, double precision; Table 4): AMD Rome 41.3 Mcell/s, Intel CSL 25.0, 4×V100 484, 4×MI250X 1240; speedups 19.3 and 49.6 over a CSL node (§5). **Shown**
25. With the Intel compiler, more than 86% of the integration loops are auto-vectorized with AVX2 (§5). **Shown** (stated measurement)
26. Weak scaling (Fig. 18): above 80% efficiency on V100 (512 GPUs) and above 95% on MI250X (1024 GPUs) with $256^3$ sub-domains, above 80% on 131 072 AMD Rome cores; CPU performance close to PLUTO 4.4; peak about $3\times10^{11}$ cell/s; performance "drops substantially" below $64^3$ per sub-domain (§5). **Shown**
27. With TDP as energy proxy, about $3\times10^{10}$ cell/kWh on CPUs against up to $1.8\times10^{11}$ on MI250X, "up to 6 times more energy efficient"; "the usage of GPUs makes sense only for subdomains larger than $64^3$" (§5). **Shown**
28. K-Athena is similar but limited to Cartesian ideal MHD, with "quantitatively similar" performance; Parthenon reaches similar hydro performance and offers the AMR that IDEFIX lacks (§6). **Stated**

# Printed slips

- p. 1: "Received September 15, 1996; accepted March 16, 1997", an A&A template placeholder in a manuscript dated April 28, 2023.
- §4.1, Sod: "$\rho_L=1.0$, $P_L=0.1$ on the left … $\rho_R=0.125$, $P_R=0.1$ of the right, with $v=0$". Equal pressures at rest make a stationary contact, yet Fig. 2 shows a rarefaction, contact and shock; the printed $P_L$ is inconsistent with the paper's own result.
- Signs of the viscous and thermal terms (Eqs. 2, 4 and the definition of $\overline{\overline\Pi}$, p. 2). As printed, $\overline{\overline\Pi}\equiv\eta_1\big(\nabla v+(\nabla v)^\top\big)+(\eta_2-\tfrac23\eta_1)\nabla\cdot v\,\mathbb I$ enters the momentum flux with a $+$ sign, and $+\kappa\nabla T$ enters the energy flux inside the divergence on the left-hand side, while the text calls $\overline{\overline\Pi}$ the viscous stress tensor and $\kappa$ the thermal diffusion coefficient. *(compiler check, not in the sources: moving the flux to the right-hand side, Eq. 2 gives $\partial_t(\rho v)=\dots-\nabla\cdot\overline{\overline\Pi}$, which for constant $\eta_1$ contains $-\eta_1\nabla^2v$, and Eq. 4 gives $\partial_tE=\dots-\nabla\cdot(\kappa\nabla T)$, i.e. $-\kappa\nabla^2T$ for constant $\kappa$: both anti-diffusive. The Ohmic term of Eq. 3 is diffusive, $-\nabla\times(\eta_{\mathrm O}J)=\eta_{\mathrm O}\nabla^2B$ for constant $\eta_{\mathrm O}$ and $\nabla\cdot B=0$, and its energy flux $+\eta_{\mathrm O}J\times B$ is the matching Poynting flux. The momentum and energy viscous terms are mutually consistent ($+\overline{\overline\Pi}$ and $+\overline{\overline\Pi}\cdot v$). The verdict depends on the sign convention: the terms are anti-diffusive under the printed definition of $\overline{\overline\Pi}$ with $\eta_1,\eta_2,\kappa>0$, and diffusive if $\overline{\overline\Pi}$ and $\kappa\nabla T$ are meant with an omitted minus sign (minus the physical stress, the Fourier heat flux $-\kappa\nabla T$); the paper states neither convention. Equations checked on the page image; the published version may differ.)*
- §4.2, 2D Orszag–Tang: the text gives "resolution $128^3$, plus a reference case at $512^3$", the captions of Figs. 10–11 give $128^2$ with a $1024^2$ reference.
- §4.2, C-shock: "$L\equiv\eta_A/v_A$ where $\eta_{AD}\equiv x_{AD}B^2$" mixes $\eta_A$ and $\eta_{AD}$; the Alfvénic Mach number is printed as a bare "$A=10$"; the Hall shock uses "$x_A=25$" for the $x_{AD}$ of Eq. (3).
- §3.1: "IdefixArrayND where $1<N<4$", which excludes the `IdefixArray1D` used in the next listing.
- Fig. 7 caption "seconder order"; Table 1 caption "two and third stages schemes".
- Fig. 8 caption says LimO3 converges "slightly larger than second order", the text "proper second order convergence"; a wording mismatch.

# Notation map

| Lesur et al. (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U=(\rho,\rho v,B,E)$ | $u$ | conserved variables (cell averages); $B$ is evolved face-averaged by CT |
| $\langle U\rangle$, $\langle F\rangle$ | $\bar u_i$, $\hat f_{i+1/2}$ | cell averages, face- and time-averaged fluxes |
| $(\rho,v,B,P)$, $P$ | $(\rho,v,B,p)$, $p$ | primitive variables; gas pressure |
| $\mathcal P\equiv P+B^2/2$ | kept | total pressure, units without $4\pi$ |
| $E$ | $E$ | total energy per unit volume, including $B^2/2$; not the electric field |
| $\mathcal E$, $\mathcal E^0$, $\mathcal E^c$ | kept | edge EMF and Gardiner–Stone averages; **$\mathcal E$ is the vortex strength in registry §10 (no page uses both)** |
| $A$ | kept | edge vector potential; **$A$ is the flux Jacobian in the registry** |
| $\psi$ | $\phi$ | gravitational potential (registry §10); **$\psi$ is the entropy flux potential in the registry** |
| $\overline{\overline\Pi}$, $\eta_1$, $\eta_2$ | kept | viscous tensor, shear and bulk viscosities; **$\eta$ is the entropy in the registry** |
| $\eta_O$, $x_H$, $x_{AD}$ | kept | Ohmic diffusivity, Hall and ambipolar parameters |
| $\kappa$, $T$ | kept | thermal diffusion coefficient, temperature; **$\kappa$ is the kinetic energy in the registry** |
| $\sigma_{\mathrm{CFL}}$ | $\nu$ | CFL number |
| $c_{\max,d}$ | $a$ (direction $d$) | maximum signal speed |
| $\eta_{\max}$, $d\ell_d$ | kept, $\Delta x$ | maximum diffusivity, cell size |
| $U_s,U^*,U_0,w_s,w^0_s$ | kept | Shu–Osher stage values and weights |
| $U$ (§2.9), $\delta v$ | kept | prescribed orbital velocity and residual; **$U$ also the conserved vector** |
| $\epsilon$ (§4.2) | kept | linear-wave amplitude $10^{-6}$; **$\epsilon$ is the weight regularization in the registry** |
| $c_f$, $c_A$, $c_s$ | kept | fast, Alfvén, slow speeds; **$c_s$ is the sound speed in Fig. 14 and $c$ in the registry** |

# Reference list

58 printed references in A&A author–year style, alphabetical, all parsed and merged
complete into the [bibliography](/bibliography.md) with `citedby` `lesur-2023`. No
DOIs are printed. Childs et al. 2012 (VisIt) has no venue; Grete et al. 2023 is
printed in online-first form (volume "0", article id 10943420221143775); Lesur 2021
has a volume and no page; Pencil Code Collaboration 2021 has a corporate author.
The GitHub and PyPI URLs are footnotes, not references. No printed duplicates
were found.

# Pages created or updated

Chunk 4 (2026-10-22), cited further in chunks 5–11 (2026-10-22/24). This source is cited on:

* [AthenaK](/software/athenak.md)
* [Block-structured adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)
* [Brio–Wu MHD shock tube](/benchmarks/brio-wu-shock-tube.md)
* [Characteristic decomposition](/methods/characteristic-decomposition.md)
* [Divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
* [Double Mach reflection](/benchmarks/double-mach-reflection.md)
* [HLL-family approximate Riemann solvers](/methods/hll-riemann-solvers.md)
* [IDEFIX](/software/idefix.md)
* [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [MHD blast wave and rotor](/benchmarks/mhd-blast-wave.md)
* [MUSCL and MUSCL–Hancock schemes](/methods/muscl-hancock.md)
* [Numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
* [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md)
* [Piecewise parabolic method (PPM)](/methods/piecewise-parabolic-method.md)
* [PLUTO](/software/pluto.md)
* [Roe approximate Riemann solver](/methods/roe-riemann-solver.md)
* [Sedov blast wave](/benchmarks/sedov-blast-wave.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
