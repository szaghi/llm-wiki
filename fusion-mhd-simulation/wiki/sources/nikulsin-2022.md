---
type: Source
title: "Nikulsin et al. (2022) — JOREK3D: An extension of the JOREK nonlinear MHD code to stellarators"
description: "Implements in JOREK a stellarator reduced MHD model with an analytic Dommaschk-potential vacuum field and a toroidally varying flux-aligned Bézier/Fourier grid initialized from GVEC, shows that W7-A equilibria are preserved, and benchmarks tearing (within 13.2% and 26.2%) and ballooning (within 6.4%) growth rates against CASTOR3D."
resource: "doi:10.1063/5.0087104"
source_kind: paper
authors: [Nikulsin N., Ramasamy R., Hoelzl M., Hindenlang F., Strumberger E., Lackner K., Günter S.]
year: 2022
venue: "Phys. Plasmas 29:063901"
local_file: "/home/stefano/papers/mosaic/fusion-mhd-simulation/2022_Crossref_Physics_of_Plasmas_Nikulsin_JOREK3D_An_extension_of_the_JOREK_nonlinear_MHD_code_to_stel.pdf"
tags: [reduced-mhd, stellarator, finite-elements, spectral, equilibrium, tearing, ballooning, verification, benchmark, code]
timestamp: 2026-10-16T20:00:00Z
---

# Summary

The paper implements in [JOREK](/software/jorek.md) — the result is
[JOREK3D](/software/jorek3d.md) — the stellarator reduced MHD model derived
by Nikulsin et al. (2019, 2021) and runs the first stellarator simulations
with it. The field ansatz is $\mathbf B=\nabla\chi+\nabla\psi_\chi\times\nabla\chi$ with $\chi$ the
vacuum (coil) scalar potential, represented analytically by Dommaschk
harmonics, so that $\nabla^2\chi=0$ and $\nabla\cdot\mathbf B=0$ hold to machine precision;
the velocity is $\mathbf v=\nabla u\times\nabla\chi/|\nabla\chi|^2$, and $v_\parallel$ is dropped in this
paper. An ordering argument in $\lambda_{\mathrm o}=L_\perp/L_\parallel$ shows that a
full-MHD equilibrium leaves a residual force in the reduced equations two
orders above the lowest-order terms. The workflow is GVEC (equilibrium) →
EXTENDER_P (vacuum field) → Legendre/Fourier fit of the Dommaschk
coefficients by triangular linear systems → flux-surface-aligned
non-axisymmetric grid whose Bézier geometry carries its own toroidal Fourier
expansion → initial current and $\psi_\chi$, with the non-homogeneous Dirichlet
boundary value of $\psi_\chi$ obtained from $\mathbf n\cdot\mathbf B=0$ by a Fourier–Galerkin
solve. On Wendelstein 7-A, four stable equilibria ($\beta$ up to 0.022%) keep
the magnetic axis and flux surfaces for about 7 ms and match GVEC. The
(2,1) [tearing-mode](/definitions/tearing-mode.md) growth rates agree with
CASTOR3D within 13.2% in a $\beta$ scan and 26.2% in an $\eta$ scan, the larger
gap attributed to the neglect of $v_\parallel$; $n=10$-dominated
[ballooning](/definitions/ballooning-mode.md) growth rates agree within 6.4%,
mostly explained by spectral blocking in JOREK. An appendix proves that the
linearized ideal reduced operator is self-adjoint.

# Key claims

1. **Residual force** (§II, Eqs. 8–12). A full-MHD stellarator equilibrium is
   not an exact equilibrium of the reduced model: the difference of Lorentz
   forces enters the vorticity and parallel-momentum equations at
   $O(\lambda_{\mathrm o}^4)$ against lowest-order $O(\lambda_{\mathrm o}^2)$ terms, "even in the zero
   β limit". Derived.
2. **Tokamak limit** (§II). With $\chi=F_0\phi$ the model reduces to the existing
   JOREK tokamak reduced model, and the reduction preserves equilibria.
   Stated (citing Hoelzl et al. 2021 and Nikulsin et al. 2021).
3. **Analytic vacuum field** (§II end, §III). Dommaschk harmonics satisfy
   Laplace's equation exactly; a finite-element $\chi$ would make the
   advective terms discontinuous because the elements are only $G^1$.
   Stated.
4. **Fit accuracy** (§III, Fig. 1). The mean relative fit error
   $\langle(\nabla\chi-\mathbf B_{\mathrm{vac}})^2/B_{\mathrm{vac}}^2\rangle$ is minimal, about
   $5\times10^{-11}$, at 9 poloidal Dommaschk modes for W7-A at
   $\beta=2.3\times10^{-3}\%$; 12 modes overfit (about $10^{-7}$). Shown.
5. **Equilibrium preservation** (§V, Figs. 4–6). Four stable W7-A equilibria
   with fivefold periodicity show "no large scale motion"; the axis $R$ is
   constant in time, offset from GVEC by at most about $10^{-4}$ m (an effect
   of the reduced ansatz); Poincaré surfaces match GVEC at start and end.
   Shown.
6. **Initial transient** (§V, Fig. 4). Kinetic energy about $10^{-7}$ J decays
   to about $2\times10^{-11}$ J within about 0.02 ms, damped by implicit Euler
   steps; attributed to the neglected fourth-order terms and the different
   discretizations. Shown.
7. **Tearing, β scan** (§VI, Fig. 8a). $\eta=1.938\times10^{-6}$ Ω m,
   $\beta=2.3\times10^{-5},2.3\times10^{-4},2.3\times10^{-3}\%$: maximum deviation from
   CASTOR3D 13.2% at $\beta=2.3\times10^{-4}\%$, JOREK systematically higher. Shown.
8. **Tearing, η scan** (§VI, Fig. 8b). $\beta=2.3\times10^{-5}\%$,
   $\eta=1.938\times10^{-7}$ to $1.938\times10^{-5}$ Ω m: maximum deviation 26.2% at the
   highest $\eta$, "most likely due to the neglect of $v_\parallel$", which is large
   in a resistive layer that widens with $\eta$ (analogy with the
   $\sqrt{1+2q_s^2}$ quasi-interchange overestimate of Waelbroeck 1989). Shown
   (deviation); Stated (attribution). [Ramasamy et al. (2024)](/sources/ramasamy-2024.md)
   (§3.1, two shared authors) re-attributes the mismatch to insufficient
   CASTOR3D poloidal resolution, without data for the re-run W7-A case.
9. **Nonlinear tearing** (§VI, Figs. 9–10). $n=1$ drives the instability and
   its family ($n=4,6,9$) through toroidal linear coupling; from about 2 ms
   $n=1$ drives $n=2$ nonlinearly, which drives $n=3,7,8$; saturation at about
   3–3.5 ms with a secondary (3,2) island chain. Shown.
10. **Convergence** (§VI). Halving $\Delta t$ or $\nu_h$, or doubling resolution,
    mode count or plane count, changes $\gamma$ by less than 1.5%. Shown.
11. **Ballooning** (§VII, Fig. 12). $\beta=0.11\%,0.21\%$;
    $\eta=1.938\times10^{-7},5.814\times10^{-7}$ Ω m; $n=0,5,10$: maximum deviation 6.4%
    ($\beta=0.11\%$, low $\eta$), the others below 3%. Shown.
12. **Spectral blocking** (§VII). Adding $n=15$ changes the CASTOR3D $n=10$
    growth rate by less than 0.003% but lowers JOREK's by about 5–6%, which
    "accounts for most of discrepancy". Shown.
13. **No high-$n$ cutoff** (§VII). Without equilibrium flows ballooning growth
    rates increase with $n$; runs with $n=15$ and $n=20$ still had the
    highest-$n$ mode fastest. Stated (theory) and shown (data not plotted).
14. **Self-adjointness** (App. B, Eqs. B1–B5). The linearized ideal reduced
    operator is self-adjoint, so ideal perturbations have real $\omega^2$.
    Derived.
15. **Scope** (§VIII). JOREK3D "is capable of handling" W7-X and LHD (Stated,
    no evidence here); the JOREK reduced-MHD family "cannot accurately
    reproduce kink modes at higher β" (Stated, citing Hoelzl et al. 2021);
    validity at $\beta\sim3$–5% "remains to be seen".

# Models and numerics

**Ansatz.** The exact (full-MHD) form is
$\mathbf B=\nabla\chi+\nabla\psi_\chi\times\nabla\chi+(\text{compressional term})$ and
$\mathbf v=\nabla u\times\nabla\chi/|\nabla\chi|^2+v_\parallel\mathbf B+(\text{fast-wave term})$ (Eqs. 1–2), the
three parts mapping approximately onto Alfvén, slow and fast waves. The
reduction drops the compressional and fast-wave potentials and the current
component perpendicular to $\nabla\chi$ in Ohm's law; this paper also sets
$v_\parallel=0$ (Eq. 4).

**Equations** (Eq. 3, read on the rendered page). Unknowns $u$, $\psi_\chi$, $\rho$, $p$
and two auxiliary unknowns, the current along $\nabla\chi$,
$j=-\nabla\chi\cdot\mathbf J/|\nabla\chi|^2$, and the vorticity $\varpi=-\nabla\chi\cdot\nabla\times\mathbf v$ (opposite
sign), kept as finite-element unknowns to avoid second derivatives in the
weak form ($G^1$ elements). In words, with derivatives "perpendicular" and
"parallel" taken relative to $\nabla\chi$ unless stated:

* vorticity equation: the operator $\nabla\chi\cdot\nabla\times(|\nabla\chi|^{-2}\,\cdot)$ applied to
  $\partial_t(\rho\mathbf v)+\nabla\cdot(\rho\mathbf v\mathbf v)=\mathbf J\times\mathbf B-\nabla p$ gives
  $\nabla\cdot(\rho|\nabla\chi|^{-2}\nabla^\perp\partial_tu)$ = nonlinear advection brackets +
  $\nabla\cdot(j\mathbf B)$ + a pressure–curvature bracket + viscosity $\nu_\perp$ +
  hyperviscosity $\nu_h$;
* continuity: $\partial_t\rho=-|\nabla\chi|[\rho/|\nabla\chi|^2,u]+\nabla\cdot(D_\perp\nabla_\perp\rho+D_\parallel\nabla_\parallel\rho)+S_\rho$;
* pressure: advection, compression $\Gamma p|\nabla\chi|[|\nabla\chi|^{-2},u]$, anisotropic
  conduction $(\Gamma-1)\nabla\cdot(\kappa_\perp\nabla_\perp T+\kappa_\parallel\nabla_\parallel T)$ plus diffusive
  terms, sources and Ohmic heating;
* induction: $\partial_t\psi_\chi=(\partial^\parallel u-[\psi_\chi,u])/|\nabla\chi|-\eta(j-j_0)+\nabla\cdot(\eta_h\nabla^\perp j)$,
  where $\partial^\parallel=|\nabla\chi|^{-1}\nabla\chi\cdot\nabla$;
* closures $j=\Delta^*\psi_\chi$ with the generalized operator
  $\Delta^*=|\nabla\chi|^{-2}\nabla\cdot(|\nabla\chi|^2\nabla^\perp\,\cdot)$, and $\varpi=\nabla\cdot\nabla^\perp u$.

The bracket is $[f,g]=|\nabla\chi|^{-1}\nabla\chi\cdot(\nabla f\times\nabla g)$. $\nabla_\parallel$, $\nabla_\perp$
(registry) are relative to $\mathbf B$.

**Ordering** (§II). $|\partial^\parallel|\sim\lambda_{\mathrm o}|\nabla^\perp|$; $\psi_\chi$, $u$, $v_\parallel$ and
$\partial_t$ are $O(\lambda_{\mathrm o})$, $p=O(\lambda_{\mathrm o}^2)$, the compressional potential
$O(\lambda_{\mathrm o}^2)$, $\tau_A=L_\parallel/v_A$. The reduced current is
$\mu_0^{-1}\Delta^*\psi_\chi\,\nabla\chi$ plus an $O(\lambda_{\mathrm o}^2)$ perpendicular part.

**Vacuum field** (§III, Eqs. 13–31). $\chi=F_0\phi+\sum_{n,m}\chi_{n,m}$, a sum of
Dommaschk harmonics in $(R/R_0,Z/R_0,\phi)$ with $R_0$ the toroidally averaged
radius of the vacuum axis. The coefficients are fitted to the EXTENDER_P
field on the cylinder $R=R_0$, $|Z|$ below a half-height, by projection on
$\cos n\phi$, $\sin n\phi$ and Legendre polynomials; the resulting systems are
upper triangular, solved in Python/NumPy, and passed to JOREK, which
evaluates $\chi$ analytically at quadrature points. $F_0$ is the $\phi$-average of
$R_0B_\phi$ on the axis circle.

**Initial and boundary conditions** (§IV). $j_0=-\nabla\chi\cdot\nabla\times\mathbf B_{\mathrm{GVEC}}/|\nabla\chi|^2$
(dropping an $O(\lambda_{\mathrm o}^3)$ term), then $\Delta^*\psi_{\chi,0}=j_0$. On the boundary,
$\mathbf n\cdot(\nabla\psi_\chi\times\nabla\chi)=-\mathbf n\cdot\nabla\chi$ (Eqs. 33–34) is solved by Fourier–Galerkin
with $m\ge1$ (excluding $m=0$ removes the kernel), projected on the boundary
nodes; interior and increments get homogeneous Dirichlet conditions. Fixed
boundary = perfectly conducting wall. $T_0=p_{\mathrm{GVEC}}/\rho_0$, $\rho_0=1$ (constant
density).

**Discretization** (App. A). Cubic Bézier quadrilaterals, 4 unknowns per
vertex, $G^1$, times a toroidal Fourier series
([Bézier–Hermite finite elements](/methods/bezier-finite-elements.md)). New
in JOREK3D: the $(R,Z)$ control points of each element carry their own
toroidal Fourier series (Eq. A1), with geometry and physics harmonics and
periodicities set independently, so a full-torus physics run ($N_{\mathrm{fp}}=1$
in the physics) can use 5-periodic geometry. The grid is flux-surface
aligned from GVEC. Toroidal integrals are sums over 40 poloidal planes.

**Time integration.** Linearization around the current step and an implicit
advance (footnote 38; see
[implicit time integration](/methods/implicit-time-integration.md)); implicit Euler first to damp transients, then
Crank–Nicolson. An iterative linear solver is used (hyper-resistivity was
needed for convergence at low $\eta$); the preconditioner is not stated.

**Resolution.** 41 radial × 48 poloidal nodes (§V–VI), 61 × 72 (§VII).
Geometry $m=0..12$, $n=0,5,\dots,50$. Physics: $n=0..20$ in steps of 5 (§V);
$n=0,5,10$ then full torus $n=0..10$ (§VI); $n=0,5,10$ (§VII). One JOREK time
unit $=6.484\times10^{-4}$ ms. No wall-clock, core count or GPU information.

**Companion codes.** GVEC (fixed-boundary 3D equilibrium, B-spline radial
basis, VMEC-like energy minimization), NEMEC (initial equilibrium),
EXTENDER_P (vacuum field), a Python Dommaschk implementation after
Huslage's BOUT++ version, CASTOR3D (linear 3D full-MHD stability, benchmark
reference).

# Tests and results

**Configuration.** W7-A-like, 5 field periods, rotating-ellipse boundary
(semi-axes 0.09131 and 0.1178 m), $R=1.99$ m, toroidal flux 0.08 Wb, total
toroidal current 17.5 kA with normalized profile
$3\psi_{t,N}-3\psi_{t,N}^2+\psi_{t,N}^3$, linear pressure in $\psi_{t,N}$, $\beta$
volume-averaged, one $\iota$ profile for all cases.

| Test | Parameters | Result |
|---|---|---|
| Equilibrium (§V) | $p$ on axis 1, 100, 500, 1000 Pa → $\beta=2.3\times10^{-5}$, $2.3\times10^{-3}$, 0.011, 0.022%; $\eta=1.938\times10^{-9}$ Ω m; $\nu=2.90\times10^{-9}$ kg m⁻¹ s⁻¹; implicit Euler then CN for 6.484 ms | axis $R\approx1.9929$–1.9936 m, constant; offset from GVEC ≲ $10^{-4}$ m |
| Tearing β scan (§VI, Fig. 8a) | $\eta=1.938\times10^{-6}$ Ω m, no viscosity or conduction, $\Delta t=1.621\times10^{-2}$ ms | $\gamma\approx$ 10500, 10300, 7450 s⁻¹ (JOREK) vs 9400, 9100, 6600 s⁻¹ (CASTOR3D), plot readings; max 13.2% |
| Tearing η scan (§VI, Fig. 8b) | $\eta=1.938\times10^{-7}$, $10^{-6}$, $10^{-5}$ (×1.938) Ω m | $\gamma\approx$ 3500 → 16300 s⁻¹ (JOREK) vs 3500 → 12900 s⁻¹; max 26.2% |
| Ballooning (§VII, Fig. 12) | $\beta=0.11$, 0.21%; 61 × 72 nodes; $\Delta t=6.484\times10^{-4}$ ms | $\gamma\approx0.9$–$1.6\times10^5$ and $2.0$–$2.6\times10^5$ s⁻¹; max 6.4%, others < 3% |
| Spectral blocking (§VII) | add $n=15$ | JOREK $\gamma$ of $n=10$ −5–6%; CASTOR3D < 0.003% |

At low $\eta$ a hyper-resistivity $\eta_h=9.691\times10^{-14}$ Ω m² was needed and
changes $\gamma$ by less than 1.5% where tested. With 5 physics harmonics, field
lines drift off flux surfaces and anisotropic transport is not properly
modelled (authors' warning).

# Notation map

| Nikulsin et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\chi$, $\tilde\chi=\chi/F_0$, $F_0$ | $\chi$, words, $F_0$ | |
| $B_v=\lvert\nabla\chi\rvert$ | $\lvert\nabla\chi\rvert$ | |
| $\Psi$ | $\psi_\chi$ | field-line-bending potential; not a flux function in a stellarator; the paper says it tends to JOREK $\psi$ in the tokamak limit (registry: $\psi_\chi\to\psi/F_0$, i.e. up to the factor $F_0$ of JOREK normalization); $2\pi$ convention not stated |
| $\Omega$, $\zeta$ | words (compressional and fast-wave potentials) | zero here; **collision:** registry $\zeta$ is a toroidal angle |
| $\psi_v$, $\beta_v$ | words (Clebsch potentials of $\nabla\chi$) | **collision:** $\beta_v$ vs plasma $\beta$ |
| $\Phi$ | $u$ | $\mathbf v=\nabla u\times\nabla\chi/\lvert\nabla\chi\rvert^2$; **collision:** registry $\Phi$ is the electrostatic potential; tokamak limit $\Phi\to F_0u$ |
| $\tilde j$, $\tilde\omega$, $\tilde j_0$ | $j$, $\varpi$, $j_0$ | opposite-sign conventions as defined above |
| $\partial^\parallel$, $\nabla^\perp$, $\Delta^\perp$ | $\partial^\parallel$, $\nabla^\perp$, $\Delta^\perp$ (§9, relative to $\nabla\chi$) | registry $\nabla_\parallel$, $\nabla_\perp$ are relative to $\mathbf B$, as the paper's subscripts |
| $\Delta^*$ | $\Delta^*$ (generalized) | reduces to the registry Grad–Shafranov operator for $\chi=F_0\phi$ |
| $[f,g]$, $(f,g)$ | $[f,g]$ as defined above, words | |
| $\lambda$ | $\lambda_{\mathrm o}$ | ordering parameter |
| $\rho$, $p=\rho RT$, $T$ | $\rho$, $p$, $T$ | **collision:** the $R$ in $p=\rho RT$ is a gas-constant-like factor, not the major radius |
| $\gamma$ | $\Gamma$ | **collision:** registry $\gamma$ is a growth rate (used so in the paper's prose too); also Dommaschk $\gamma_i$ |
| $\eta$, $\eta_{\mathrm{Ohm}}$, $\eta_h$ | $\eta$, words, $\eta_h$ | native $\eta$ is also a test function in App. B |
| $\mu_\perp$ (also $\mu$), $\mu_h$ | $\nu_\perp$, $\nu_h$ | **collision:** registry $\mu$ is a magnetic moment |
| $D_\perp$, $D_\parallel$, $\kappa_\perp$, $\kappa_\parallel$, $S_\rho$, $S_e$ | same, $S_p$ | |
| $\vec B_E$ | $\mathbf B_{\mathrm{vac}}$ (words) | EXTENDER_P field |
| $(R,z,\phi)$ | $(R,Z,\phi)$ | orientation not stated |
| $\psi_{tn}$, ι | $\psi_{t,N}$, $\iota$ | |
| $N_{\mathrm{tor}}$, $N_p$ | $N_{\mathrm{tor}}$ (counts cos and sin separately, $2n_{\max}+1$), words (periodicity) | |
| $N_{\mathrm{ctor}}$, $N_{\mathrm{cp}}$ | words (geometry harmonics and periodicity) | |
| $L(\xi)$, $\xi$ | $\mathcal L$, words (displacement potential) | |
| $\tau_A=L_\parallel/c_A$ | $\tau_A$, $v_A$ | |

# Pages created or updated

Chunk 1 (2026-10-16) created every page of the bundle; chunks 2 and 3 (2026-10-16) extended many. This source is cited on:

* [Ballooning mode](/definitions/ballooning-mode.md)
* [BOUT++](/software/bout-plus-plus.md)
* [Bézier–Hermite finite elements with toroidal Fourier harmonics](/methods/bezier-finite-elements.md)
* [CASTOR3D](/software/castor3d.md)
* [Divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
* [Dommaschk potentials for the vacuum field](/methods/dommaschk-potentials.md)
* [Grad–Shafranov equation](/definitions/grad-shafranov-equation.md)
* [Implicit time integration and preconditioned Krylov solvers for nonlinear MHD](/methods/implicit-time-integration.md)
* [Interchange modes and the Mercier criterion](/definitions/interchange-mode.md)
* [JOREK](/software/jorek.md)
* [JOREK3D](/software/jorek3d.md)
* [Linear MHD eigenvalue codes](/methods/linear-mhd-eigenvalue-codes.md)
* [M3D](/software/m3d.md)
* [M3D-C1](/software/m3d-c1.md)
* [MIPS](/software/mips.md)
* [NIMROD](/software/nimrod.md)
* [Reduced MHD for stellarators](/methods/stellarator-reduced-mhd.md)
* [Reduced MHD for tokamaks](/methods/reduced-mhd.md)
* [Resistive internal kink (m/n = 1/1)](/definitions/resistive-internal-kink.md)
* [Resistive tearing mode](/definitions/tearing-mode.md)
* [Three-dimensional inverse equilibrium solvers](/methods/inverse-equilibrium-solvers.md)
* [Toroidal mode families in stellarators](/definitions/toroidal-mode-family.md)
* [VMEC](/software/vmec.md)

# Citations

1. `/home/stefano/papers/mosaic/fusion-mhd-simulation/2022_Crossref_Physics_of_Plasmas_Nikulsin_JOREK3D_An_extension_of_the_JOREK_nonlinear_MHD_code_to_stel.pdf`
   * **Version.** arXiv:2201.12033v3 [physics.plasm-ph], 12 May 2022 (header
     "Dated: 16 May 2022"), 16 pp. revtex preprint; not the AIP typeset
     version.
   * **Identity.** doi:10.1063/5.0087104, checked on Crossref: Phys. Plasmas
     29(6):063901, issue 2022-06-01, online 2022-06-08; seven named authors plus
     the group author "JOREK Team". Crossref also lists a Publisher's Note,
     doi:10.1063/5.0124567, Phys. Plasmas 29:099902 (2022-09-21), whose content
     was not seen; the published equations may differ from v3.
   * **How read.** Full text including appendices; Eq. 3 checked on the
     rendered page 3; plot values are approximate readings.
   * **Recorded as printed.**
     * Eq. 6 reads "$\nabla\chi\cdot\nabla\times(B_v^{-2}$" with the parenthesis never closed;
       Eq. 7 is only "$\vec B\cdot$"; the $\Delta^*$ definition also lacks its closing
       parenthesis.
     * §III end lists "(22), (23), (26), (27) and (28)" as the linear systems;
       Eq. 28 is the $B_{E,z}$ expansion, the $a_{0,m}$ system is Eq. 31.
     * Eq. 35 uses $N_p$ and $n_{\mathrm{tor}}$ while the text says "where $N_{\mathrm{cp}}$
       is defined in Appendix A".
     * Fig. 3: the plotted "ι" runs from about 5.5 (axis) to 2.2 (edge); under
       either the $\iota$ or the $q=1/\iota$ reading the range contains neither the
       (2,1) nor the interior (3,2) surface reported in §VI. Not resolved.
     * Fig. 6 caption: end time 7.275 ms for $\beta=0.022\%$; the §V schedule
       gives about 7.92 ms including the extra 10 steps of that case (7.275 ms
       is the total without them), and Fig. 5 data extend to about 8 ms.
     * Fig. 4 caption: "first 0.144 ms (20 steps of 1 and 20 of 10 units)";
       220 units are 0.1426 ms.
     * Notation overloads: $\eta$ (resistivity, test function), $\gamma$
       (adiabatic index, Dommaschk coefficients, growth rate), $\beta$ (plasma
       beta, Clebsch potential, Dommaschk coefficients), $\vec B$ in Eq. B4 the
       perturbation; §II writes both $\nabla\beta_V$ and $\beta_v$.
     * Intro: "All three of these codes use full MHD on flux surface aligned
       grids, except for MIPS, which uses a cylindrical grid", self-
       contradictory as worded (MIPS is one of the three).
     * The 26.2% deviation is called "deviations on the order of 10%" at the
       end of §VI; abstract "reasonable", conclusion "decent" agreement.
     * Typos: "was was", "applying applying", "allows on to write",
       "auxilliary", "occuring", a missing "to" in §VIII.
     * No parallel or performance information (cores, wall clock,
       preconditioner).
   * **Reference list.** 46 numbered items, of which item 38 is a footnote, so
     45 bibliographic references, merged into the bibliography under
     `nikulsin-2022` (45 entries); no DOIs printed. Strumberger & Günter, Nucl.
     Fusion 57:016032, printed with year 2016, is `strumberger-2017`. Pamela,
     Huijsmans & Hoelzl (J. Comput. Phys. 2022, $G^n$ elements, no volume
     printed) is `pamela-2022`. The 56-author JOREK paper is the ingested
     `hoelzl-2021`. "Huijsmans" and "Huysmans" spellings are kept as printed
     (`huysmans-2001`, `huysmans-2007`). Ref. 27 has the collective author "W VII-A
     Team" (`wviiateam-1980`); Ref. 43 (Zanini et al.) has a garbled author tail.
