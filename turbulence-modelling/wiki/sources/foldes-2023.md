---
type: Source
title: "Foldes et al. (2023) — Efficient kinetic Lattice Boltzmann simulation of three-dimensional Hall-MHD turbulence"
description: "Presents FLAME, a multi-GPU lattice Boltzmann code for weakly compressible three-dimensional Hall-MHD that adds the Hall term through the magnetic equilibrium with a local current solve, verifies second-order convergence on an exact solution, matches the pseudo-spectral code GHOST on the Orszag–Tang vortex, and runs decaying Hall-MHD turbulence."
resource: "doi:10.1017/s0022377823000697"
source_kind: paper
authors: [Foldes R., Lévêque E., Marino R., Pietropaolo E., De Rosis A., Telloni D., Feraco F.]
year: 2023
venue: "J. Plasma Phys. 89:905890413"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Journal_of_Plasma_Physics_Foldes_Efficient_kinetic_Lattice_Boltzmann_simulation_of_three-dime.pdf"
tags: [mhd, plasma, lattice-boltzmann, gpu, dns, decaying-turbulence]
timestamp: 2026-10-26T07:35:00Z
---

# Summary

Foldes et al. (2023) present FLAME (Fast Lattice-Boltzmann Algorithm for
MHD Experiments), a multi-GPU (OpenCL and MPI)
[lattice Boltzmann](/methods/lattice-boltzmann-method.md) code for
three-dimensional Hall-MHD in the weakly compressible limit. The motivation
is the time step. The Hall term carries whistler waves whose phase speed
grows linearly with the wavenumber, so an explicit scheme needs
$\Delta t\propto\Delta x^2$, and three-dimensional pseudo-spectral Hall-MHD
runs become expensive. The fluid is advanced with a central-moment
multi-relaxation-time collision on a D3Q27 lattice, with an equilibrium
expanded to sixth order in the velocity and the Lorentz force entering
through the Maxwell stress. The induction equation uses Dellar's
vector-valued BGK scheme on a D3Q7 lattice. The authors' contribution is
the Hall term: they insert it by replacing $\boldsymbol u$ with
$\boldsymbol u-\alpha_H\boldsymbol J$ in the magnetic equilibrium. The
current density $\boldsymbol J$ comes locally from the non-equilibrium
first moment of the magnetic distributions, through a $3\times3$ linear
system solved in closed form. They also derive the lattice form of the Hall
parameter and a whistler CFL bound on the Mach number.

An exact damped-wave solution of dissipative Hall-MHD shows stability over
the tested parameters and second-order convergence of the dispersion,
dissipation and numerical-viscosity errors
([numerical dissipation](/properties/numerical-dissipation.md)). On the
three-dimensional Orszag–Tang vortex of
[decaying MHD turbulence](/results/decaying-mhd-turbulence.md), FLAME
agrees with the pseudo-spectral code [GHOST](/software/ghost.md) at
$512^3$ in energies, mean current and energy fluxes. Its kinetic spectrum
is over-damped at high wavenumber at $512^3$ and close to GHOST's at
$768^3$. Hall-MHD Orszag–Tang runs show faster development of turbulence
as the Hall parameter grows, and a magnetic spectrum steepening beyond the
Hall scale, compared with a $k^{-2.73}$ solar-wind slope. All runs are
model-free [direct numerical simulations](/definitions/direct-numerical-simulation.md).
The weakly compressible formulation only serves as a route to
incompressible Hall-MHD: the density fluctuations stay at
$10^{-7}$–$10^{-6}$ ([compressible MHD turbulence](/results/compressible-mhd-turbulence.md)
is not addressed). The paper is peripheral to closure modelling: it is a
plasma-turbulence solver paper.

# Version read

arXiv preprint arXiv:2212.11024v2 [physics.plasm-ph], 7 August 2023,
author-formatted in the JPP class ("Under consideration for publication in
J. Plasma Phys."). It is a revised author version that thanks two
referees, not the version of record. It has 38 pages, all read; Appendix B
(pp. 30–31) and the Appendix A equilibrium (p. 29) were also checked
visually. Page 1 capitalizes "Turbulence" in the title; title, authors and
topic match the metadata. Equation, figure, table and page numbers on this
page are those of this version.

# Key claims

1. Resolving whistler waves, whose phase speed $c_w(k)\propto k$, at the grid scale makes the CFL condition $\Delta t\propto\Delta x^2$ (§1; §3.4, Eqs. 3.40–3.44). **Derived**
2. The Hall term enters the scheme through the magnetic equilibrium $g^{\mathrm{Hall}(0)}_{i\alpha}=W_i[B_\alpha+\xi_{i\beta}((u_\beta-\alpha_HJ_\beta)B_\alpha-B_\beta(u_\alpha-\alpha_HJ_\alpha))/C^2]$, whose first moment is $(\boldsymbol u-\alpha_H\boldsymbol J)\otimes\boldsymbol B-\boldsymbol B\otimes(\boldsymbol u-\alpha_H\boldsymbol J)$ (§3.2, Eqs. 3.24–3.25); "Our original contribution" (§3). **Derived**
3. $\boldsymbol J$ is obtained locally from the non-equilibrium first moment of the magnetic distributions, $J_\gamma=-\epsilon_{\alpha\beta\gamma}(\omega_B/C^2)(\Lambda_{\alpha\beta}-\Lambda^{(0)}_{\alpha\beta})$, "within an $O(Ma^3)$ error" (Eq. 3.26, after Dellar 2002). With the Hall equilibrium this becomes a linear $3\times3$ system whose matrix has non-zero determinant, so the solution "exists and is unique" (§3.2, Eqs. 3.27–3.28; closed form in App. B, Eq. B1, with denominator $D=C^6+4C^2\alpha_H^2\omega_B^2\lvert\boldsymbol B\rvert^2>0$). **Derived**
4. $\nabla\cdot\boldsymbol B\simeq-(\omega_B/C^2)\,\mathrm{Tr}\,\Lambda$, the $O(Ma^3)$ correction cancelling in the trace; in the runs the divergence stayed "to machine round-off error" (Eq. 3.29, §3.2). **Derived**; round-off level **Stated** (no figure)
5. The lattice Hall number is $\epsilon_H^{\mathrm{lbm}}=\epsilon_HN_x$ when the reference velocity equals the Alfvén speed and $\rho\simeq1$, and then equals the number of lattice points per ion inertial length (Eqs. 3.36, 3.39). **Derived**
6. The whistler CFL condition in lattice units is $1\le B_0^{\mathrm{lbm}}/(\pi\epsilon_HN_x(U_0^{\mathrm{lbm}})^2)$; with the reference velocity equal to the Alfvén speed, $M\le(\sqrt3/\pi)/(\epsilon_HN_x^2)$ (Eqs. 3.43–3.44). **Derived**
7. On the Xia–Yang exact solution "All simulations remained numerically stable in the explored range of parameters" ($N_x=32$–$128$; $M=0.01$, $0.007$, $0.005$, $0.003$; $\nu=10^{-3}$ to $1.1\times10^{-4}$) (§4.2, Fig. 4, Table 1). **Shown**
8. Relative density fluctuations are "typically of order $10^{-7}$–$10^{-6}$" and decrease with the Mach number (§4.2, Fig. 5). **Shown**
9. The relative dispersion error (Eq. 4.7, over ten periods) "decreases as $N^{-2}$" and is nearly independent of $M$ and $\nu$ (§4.3, Fig. 6). **Shown**
10. The relative dissipation error (Eq. 4.8) converges as $N_x^{-2}$ in both acoustic (fixed $M$) and diffusive (fixed lattice viscosity) scaling (§4.3, Figs. 7–8). **Shown**
11. The numerical-viscosity ratio $\nu_{\mathrm{num}}/\nu$ is "only a small percentage", decreases as $N_x^{-2}$ and depends only on resolution, not on $\nu$ or $M$ (§4.3, Eq. 4.9, Fig. 9). **Shown**
12. Replacing the D3Q7 magnetic lattice by D3Q15 or D3Q27 brings "no significant improvement", confirming Dellar (2002) (§4.3). **Shown** (data not displayed)
13. On the three-dimensional Orszag–Tang decaying MHD problem at $N_x=512$, FLAME and GHOST agree "very satisfactory" in $\langle\lvert\boldsymbol J\rvert^2\rangle(t)$ and in the kinetic and magnetic energies, with "a slight underestimation of the magnetic dissipation" by FLAME for a few steps after the peak (§4.4, Fig. 10). **Shown**
14. At peak dissipation the lattice Boltzmann kinetic spectrum is "over-damped at high wavenumbers", attributed to the enhanced numerical dissipation of the moment-based collision (Coreixas et al. 2019); at $N_x=768$ it "gets very close" to the $512^3$ pseudo-spectral one, "qualitatively consistent" with Shen et al. (2018) that lattice Boltzmann needs about twice the resolution of a pseudo-spectral method (§4.4, Fig. 11). **Shown**
15. The magnetic spectra of FLAME and GHOST "perfectly match", "reflecting the fact that the BGK collision operator adopted for the magnetic scheme does not add numerical dissipation" (§4.4, Fig. 11). **Shown** (match) / **Stated** (explanation)
16. Lattice Boltzmann resolves up to the Nyquist cutoff $k_{\max}=N_x/2$, against $N_x/3$ for the 2/3-dealiased pseudo-spectral code (§4.4). **Stated**
17. Energy fluxes and dissipation spectra (Eqs. 4.10–4.12) agree between the codes over all resolved wavenumbers, with lattice Boltzmann over-dissipating at the highest ones; the pressure contribution is negligible (§4.4, Fig. 12). **Shown**
18. At $512^3$ on three NVIDIA A100-40GB GPUs FLAME runs "about 20 iterations per second" ("2.7 BLUPS") in double precision, timings including CPU–GPU transfers and on-the-fly diagnostics; wall-clock times to pass the dissipation peak were 10, 55 and 69 h (§5). **Shown** (reported measurement)
19. A larger Hall parameter gives "a faster development of turbulence", attributed to whistler and Hall-drift waves faster than Alfvén waves (§5, Fig. 13). **Shown** (observation) / **Stated** (explanation)
20. A larger Hall parameter moves the Hall scale to larger scales and shortens the $k^{-5/3}$ range of both spectra (§5, Fig. 16). **Shown**
21. Beyond the Hall wavenumber the magnetic spectrum develops, as the Hall parameter grows, "a power-law scaling that is in perfect agreement with the $k^{-2.73}$ scaling" of solar-wind sub-ion spectra (Kiyani et al. 2015) (§5, Figs. 14, 16). **Shown** by overlay of a reference slope only; no fitted exponent is reported
22. In plain MHD the lattice Boltzmann time step is smaller than that of an incompressible pseudo-spectral solver by about the Mach number (Horstmann et al. 2022), so the method has little turnaround advantage; in Hall-MHD both are limited by whistlers, and lattice Boltzmann on GPUs gives "significantly smaller" turnaround times (§5). **Stated** (no GHOST Hall-MHD timing is given)
23. An electron-MHD extension would only require neglecting $\boldsymbol u$ against $\alpha_H\boldsymbol J$ in Eq. 3.25 (§5). **Stated**
24. A main advantage of the kinetic representation is that $\boldsymbol J$, a derivative of the magnetic field, comes out of the solution without a differentiation scheme (§3.2, §7). **Stated**
25. Preliminary tests suggest that the whistler CFL bound could be relaxed, because magnetic and numerical diffusivity damp high-frequency whistlers (§7). **Stated** (no data)
26. Parker Solar Probe (fast wind, 0.09 AU) and Solar Orbiter (slow wind, 0.64 AU) magnetic spectra break at $k\rho_i\sim1$ between a Kolmogorov-like range and a steeper kinetic range (§6, Fig. 17, Table 3). **Shown** (observational data)
27. Solar-wind sub-ion magnetic spectral slopes range from about $-4$ to $-2$ (Smith et al. 2006; Bruno et al. 2014) (§6). **Stated**

# Printed slips

1. D3Q27 weights: §3.1.1 prints $w_{\mathrm{edge}}=1/54$; Appendix A prints "$w_{center}=8/27$, $w_{face}=2/27$, $w_{edge}=8/27$ and $w_{corner}=1/216$". The weights sum to one only with $1/54$: $8/27+6\cdot2/27+12\cdot1/54+8\cdot1/216=1$ *(compiler check, not in the sources)*.
2. Eq. (3.27) prints $(I+\tfrac{2\alpha_H\omega_B}{C^2}M)\boldsymbol J=\boldsymbol J_0$, Appendix B prints $\tilde M\boldsymbol J=-\tfrac{1}{2\alpha_H}\boldsymbol J_0$ with $\tilde M=\tfrac{C^2}{2\alpha_H\omega_B}I+M$. Multiplying Eq. (3.27) by $C^2/(2\alpha_H\omega_B)$ gives $\tilde M\boldsymbol J=\tfrac{C^2}{2\alpha_H\omega_B}\boldsymbol J_0$, so the two printed right-hand sides differ by the factor $-\omega_B/C^2$; Eq. (3.26) supports Appendix B *(compiler check, not in the sources)*.
3. Eq. (B1), $J_y$: the printed numerator begins "$2C^4\omega_BB_xU_z+2C^4\omega_BB_zU_x+C^4\omega_B\Lambda_{xz}-C^4\omega_B\Lambda_{zx}$". For $\alpha_H\to0$ Appendix B's own system gives $\boldsymbol J\to-(\omega_B/C^2)\boldsymbol J_0$, whose $y$ component carries $-2C^4\omega_BB_zU_x$: the sign of the second term is wrong *(compiler check, not in the sources; only the $O(\alpha_H^0)$ terms were checked)*.
4. After Eq. (3.20): "where the relaxation parameter $\omega_m$ is now related to the magnetic resistivity"; the symbol in Eqs. (3.19)–(3.20) is $\omega_B$.
5. Table 2 caption ("the CFL condition (3.4) imposed by whistler waves"), §5 ("see 3.4") and §7 ("according to (3.4)") point to Eq. (3.4), the discrete-velocity BGK equation; §3.4 and Eq. (3.44) are meant.
6. Fig. 12 caption: fluxes "as reported in (4.11)"; the flux is Eq. (4.10), Eq. (4.11) is the dissipation.
7. §5 gives wall-clock times "for the three runs indicated in Tab. 2", and the Fig. 13 caption speaks of "the three simulations", while Table 2 and the Fig. 13 legend list four runs (I–IV).
8. Fig. 14 caption "$N=768^3$", while $N$ is the number of points per direction (Table 2: $N=768$).
9. Fig. 17 caption lists "$k^{-1.67}$, $k^{-1.5}$ and $k^{-2.73}$ scalings"; the figure labels $k^{-5/3}$.
10. Table 3 prints the density unit as "[cm$^3$]" for a number density.
11. $L_0$ is the box length $2\pi$ in §§3–4 but the integral scale $2\pi\int E_v(k)k^{-1}dk/\int E_v(k)dk$ in the Fig. 16 caption that defines $k_H$; §4.4 calls the same integral scale $L$.
12. Appendix A, fourth-order equilibrium terms: "$H^{(4)}_{ixyyx}U_xU_y^2U_z$" (index label against the monomial) and "$H^{(4)}_{ixxyz}U_x^2U_yU_y$"; the full equilibrium was not reconstructed.

# Notation map

| Foldes et al. (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf U$, $u$ | $\boldsymbol u$ | bulk (proton) velocity; lowercase dimensionless; no averaging or filtering in the paper |
| $\mathbf B$, $b$ | $\boldsymbol B$ | rescaled by $\mu_0^{1/2}$, so $\boldsymbol J=\nabla\times\boldsymbol B$ and $v_A=B_0/\sqrt\rho$ |
| $\mathbf J$ | $\boldsymbol J$ (page-local current density) | as on the [ferrand-2022](/sources/ferrand-2022.md) page |
| $\eta$ | $\eta_m$ | **collision:** magnetic diffusivity, not the Kolmogorov length |
| $\nu$, $\mu$ | $\nu$, $\mu$ | Table 1 normalizes $\nu$ by $U_0L_0$, so $Re=1/\nu$ |
| $\zeta$ | (bulk viscosity) | **collision:** not the feature vector $\boldsymbol\zeta$ |
| $Pr_m$, $Re_m$ | $Pm$, $Rm$ | $Pm=1$ throughout |
| $Re$ | $Re$ | $U_0L_0/\nu$ in §3; $UL/\nu$ with rms velocity and integral scale at peak dissipation in §§4.4–5 |
| $V_A$ | $v_A$ | built on $B_0$, unit-rescaled field |
| $B_0$, $U_0$, $L_0$ | $B_0$ (§3.3 reference field), $B_{\mathrm{OT}}$ (§4.4 Orszag–Tang amplitude, page-local), $U_0$, $L_0$ (reference velocity and length, page-local) | **collision:** no mean field in the Orszag–Tang runs, so the amplitude is not the registry's guide field $\boldsymbol B_0$ |
| $Ma$ | $M$ | $Ma=U_0/c_s$; $\sqrt3U_0^{\mathrm{lbm}}$ in lattice units |
| $\alpha_H$, $\epsilon_H$, $\epsilon_H^{\mathrm{lbm}}$ | (Hall parameter $1/(en)$, its dimensionless form $L_H/L_0$, lattice Hall number; page-local) | Figs. 13, 16 print $\epsilon_H$ as "$H$" |
| $d_i$, $L_H$, $k_H$ | $d_i$ (page-local ion inertial length), (Hall length, Hall wavenumber $2\pi/(\epsilon_HL_0)$) | **collision:** $d_i$ is not the wall distance $d$ |
| $\rho_i$ | (ion gyroradius, §6) | **collision:** not the density |
| $N$ | $N_x$ | lattice points per reference length; **collision:** not a polynomial degree |
| $f_i$, $\bar f_i$, $f_i^{(0)}$, $f_i^{mhd(0)}$ | (distribution functions and equilibria, page-local) | **collision:** not the body force $f_i$ |
| $\mathbf c_i$, $\bar{\mathbf c}_i=\mathbf c_i-\mathbf U$, $c_s$ | (lattice and central velocities, lattice sound speed) | $\Delta x/\Delta t=\sqrt3c_s$ |
| $w_i$, $W_i$ | (lattice weights, D3Q27 and D3Q7; page-local) | **collision:** not quadrature weights |
| $\tau$, $\omega$, $\omega_B$ | $\tau_{\mathrm{LB}}$, $\omega_{\mathrm{LB}}$, $\omega_B$ (relaxation time and frequencies, page-local) | **collision:** not the SGS stress, the specific dissipation rate or the vorticity |
| $\lvert k\rangle$, $T$, $S$ | (central moments, transformation and relaxation matrices) | **collision:** $S$ is not the strain rate, $k$ not the kinetic energy |
| $\mathbf g_i$, $\boldsymbol\xi_i$, $C$ | (vector-valued magnetic distributions, their lattice velocities, $\Delta x/\Delta t=2C$) | **collision:** $\boldsymbol\xi_i$ are not quadrature nodes |
| $\Lambda_{\alpha\beta}$, $\Lambda^{(0)}_{\alpha\beta}$, $M$, $\tilde M$, $\mathbf J_0$, $D$ | (first moment of $\mathbf g_i$, its equilibrium, matrices and right-hand side of the current solve; page-local) | **collision:** $M$ is not the Mach number |
| $\epsilon$ | $\varepsilon$ | total (kinetic plus magnetic) energy dissipation rate |
| $\varepsilon_\phi$, $\varepsilon_r$, $\varepsilon_\nu=\nu_{num}/\nu$, $\tilde\nu$ | (dispersion, dissipation and viscosity errors; effective viscosity) | **collision:** $\tilde\nu$ is not the Spalart–Allmaras variable |
| $E_v(k)$, $E_B(k)$, $S_{MHD}(k)$, $D(k)$ | $E(k)$ (kinetic), (magnetic spectrum, cumulative nonlinear flux and dissipation) | **collision:** $D$ is not a differentiation matrix |
| $\tau_0=L_0/U_0$ | (reference time) | |

# Reference list

113 printed references, author–year (JPP) style, alphabetical. The list is
merged complete into the [bibliography](/bibliography.md) with `citedby`
this slug; no printed duplicates. Same-author same-year works take suffixes
in printed order (Adhikari 2015a/b, Bruno 2014 with two different author
lists, Marino 2015a/b, Telloni 2022a/b). The citation of Ferrand et al.
(2022) is the bundle's Source [ferrand-2022](/sources/ferrand-2022.md).
Hénon (1987) prints "Compl. Sys. 462" without separable volume and pages;
Huba (2003) prints its editors without a role label; Marino et al. (2015b)
and Morales et al. (2005) print no page or article number; the title of
Adhikari et al. (2015a) carries a mis-encoded "alfvÃ‰nic"; Dudson et al.
(2015) ends its author list with "et al."; Malaspinas (2015) is an arXiv
preprint. All are recorded as printed.

# Pages created or updated

Chunk 4 (2026-10-26), cited further in chunk 6. This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Bulk viscosity](/definitions/bulk-viscosity.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Lattice Boltzmann methods for turbulent flow](/methods/lattice-boltzmann-method.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Compressible MHD turbulence](/results/compressible-mhd-turbulence.md)
- [Decaying MHD turbulence and its invariants](/results/decaying-mhd-turbulence.md)
- [GHOST](/software/ghost.md)
