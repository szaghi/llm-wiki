---
type: Source
title: "Kochurin et al. (2022) — Three-dimensional direct numerical simulation of free-surface magnetohydrodynamic wave turbulence"
description: "Pseudo-spectral simulations of capillary wave turbulence on a ferrofluid surface under a horizontal magnetic field show a transition from the isotropic Kolmogorov–Zakharov spectrum to an anisotropic regime whose k⊥^-3 elevation spectrum and square-root-of-flux and v_A^(-3/2) prefactor match weak shear-Alfvén wave turbulence."
resource: "doi:10.1103/physreve.105.l063101"
source_kind: paper
authors: [Kochurin E., Ricard G., Zubarev N., Falcon E.]
year: 2022
venue: "Phys. Rev. E 105:L063101"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Physical_Review_E_Kochurin_Three-dimensional_direct_numerical_simulation_of_free-surfac.pdf"
tags: [mhd, anisotropy, energy-cascade, dns]
timestamp: 2026-10-27T15:52:00Z
---

# Summary

Kochurin et al. (2022) simulate wave turbulence on the free surface of an
ideal, irrotational, incompressible ferrofluid of infinite depth under a
horizontal magnetic field $B$. Linear surface waves obey
$\omega^2=v_A^2k_\parallel^2+(\sigma_s/\rho)k^3$: the field adds a
dispersionless, Alfvén-like contribution acting only along it. The model
is a pair of Hamiltonian equations for the surface elevation $\varsigma$
and the surface velocity potential $\psi$, truncated at quadratic
nonlinearity, with a hyperviscous dissipation operator at small scales, a
spectral cutoff that the authors interpret as "superviscosity", and
isotropic forcing at large scales; it is integrated pseudo-spectrally with
$1024^2$ harmonics and fourth-order Runge–Kutta. What the title calls
"direct numerical simulation" solves this truncated, hyperviscous model of
surface waves, not the Navier–Stokes equations (compare
[DNS](/definitions/direct-numerical-simulation.md)).

Raising the nondimensional field parameter $V_A^2$ from 0 to 300 turns
isotropic capillary [wave turbulence](/results/weak-wave-turbulence.md),
with the Kolmogorov–Zakharov elevation spectra $\mathcal S(k)\sim k^{-15/4}$ and
$\mathcal S(\omega)\sim\omega^{-17/6}$, into a strongly anisotropic regime in which
energy cascades mainly perpendicular to the field. At $V_A^2=300$ the
spectra are $\mathcal S(k)\approx \mathcal S(k_\perp)=C_1\varepsilon_s^{1/2}v_A^{-3/2}k_\perp^{-3}$ and
$\mathcal S(\omega)=C_2(\sigma_s/\rho)^{2/3}\varepsilon_s^{1/2}v_A^{-3/2}\omega^{-7/3}$ with fitted
$C_1=1.7$, $C_2=1.34$. The $k_\perp^{-3}$ law and its prefactor coincide with
the weak-turbulence prediction for anisotropic shear-Alfvén waves in a
plasma, the transverse-only cascade discussed on
[critical balance](/properties/critical-balance.md), and with a
phenomenological model the authors derive. The $\varepsilon_s^{1/2}$ scaling is
consistent with three-wave interactions, and the resonant triads reported
in the Supplemental Material are "suggesting that wave interactions are
local" (p. 5). The authors conclude that Alfvén
wave turbulence in plasma and surface-wave turbulence on magnetic fluids
are quantitatively analogous, although the energy-transfer mechanisms
differ.

# Version read

arXiv preprint arXiv:2205.11516v1 [physics.plasm-ph], 23 May 2022 ("Dated:
May 25, 2022"; revtex two-column layout), 6 pages, all read. Title and
authors match the Crossref record of the version of record (Phys. Rev. E
105:L063101, a Letter); the preprint prints no DOI. The Supplemental
Material (ref. [40]), which holds the model derivation, the bicoherence,
the time-scale check and the triad analysis, is not in the file and was
not read. Locators are those of the preprint.

# Key claims

1. Linear surface waves on an ideal ferrofluid of infinite depth in a horizontal field along $x$, gravity neglected, obey $\omega^2=[B^2/(\mu_{\mathrm{eff}}\rho)]k_\parallel^2+(\sigma_s/\rho)k^3$ with $\mu_{\mathrm{eff}}=\mu_0(\mu_r+1)/(\mu_r-1)^2$; propagation is anisotropic (Eq. 1, after Melcher [26]). **Stated**
2. $v_A^2=B^2/(\mu_{\mathrm{eff}}\rho)$ is the group velocity of the dispersionless magnetic surface wave along the field, "analogous to Alfvén velocity"; the field dependence of $\mu_r$ in experiments has no impact because $v_A$ is the controlling parameter (p. 1). **Stated**
3. The Kolmogorov–Zakharov spectrum of isotropic capillary wave turbulence is $\mathcal S^c(k)=C_{KZ}\varepsilon_s^{1/2}(\sigma_s/\rho)^{-3/4}k^{-15/4}$, with energy spectrum $E^c(k)=(\sigma_s/\rho)k^2\mathcal S^c(k)$ (Eq. 2, from [4]); it is well confirmed experimentally [27–30] and numerically [31–35]. **Stated**
4. For $B\ne0$ no weak-turbulence prediction for magneto-capillary waves exists, only dimensional analysis [23, 24] (p. 2). **Stated**
5. Weak turbulence of anisotropic Alfvén waves ($k_\perp\gg k_\parallel$) gives $\mathcal S^m(k)=C_m\varepsilon_s^{1/2}v_A^{-3/2}k_\perp^{-3}$ with $C_m=1.467$ [36], "a $\sqrt{2\pi}$ factor was missing in [18]" (Eq. 3). **Stated**
6. The model equations (4)–(5) for $\varsigma$ and $\psi$, with quadratic nonlinearity, describe an ideal irrotational incompressible ferrofluid without free charges or currents, so the field in the liquid is potential; the derivation is in the Supplemental Material (p. 2). **Derived** (not in the Letter)
7. For finite $\mu_r$, surface waves collapse under an infinitely strong horizontal field [41], so regularization by viscosity and surface tension is needed for a correct simulation (p. 2). **Stated**
8. Set-up: pseudo-spectral, $1024\times1024$ harmonics, fourth-order Runge–Kutta with $dt=5\times10^{-5}$, periodic $2\pi\times2\pi$ box, forcing amplitude $F_0=2000$ peaked at $k_0=3$ over $k\in[1,6]$, hyperviscosity $\hat D_kf_k=-\nu_h(k-k_d)^2f_k$ for $k\ge k_d=150$ with $\nu_h=10$, cutoff $k_a=212$, $A_\mu=0.5$ ($\mu_r=3$), $V_A^2=0$, 25, 100, 300; steepness $s_w=0.16$ nearly independent of the field; stationary after $t\approx50$, runs to $t=500$ (p. 2). **Shown**
9. The anti-aliasing filter (harmonics with $k>k_a$ zeroed at every step) "can be thus interpreted as 'superviscosity' acting at small scales" (p. 2). **Stated**
10. Phenomenological model (strong field $V_Ak_\parallel\gg k_\perp^{3/2}$, anisotropy $k_\perp\gg k_\parallel$): the magnetic nonlinear time $T^m_{\mathrm{nl}}\sim\psi/(V_A^2k_\parallel^2\varsigma^2)$ becomes $T^m_{\mathrm{nl}}\sim1/(\psi k_\perp k_\parallel)$ when the magnetic potential energy passes to capillary kinetic energy; with $\varepsilon_s\sim k_\perp E/(\omega T_{\mathrm{nl}}^2)$ this gives $\mathcal S^m(k)\sim \varepsilon_s^{1/2}V_A^{-3/2}k_\perp^{-3}$, "the same as the shear-Alfvén wave turbulence prediction of Eq. (3)" (pp. 2–3; details in the Supplemental Material). **Derived**
11. Increasing the field turns the surface relief from isotropic ($V_A^2=0$) to almost unidirectional ($V_A^2=300$), with waves propagating mainly perpendicular to the field, attributed to the stabilizing effect of a horizontal field [22, 42] (Fig. 1, p. 3). **Shown**
12. In $\mathcal S(k_\parallel,\omega)$ the energy spreads around the linear dispersion relation at $B=0$; with increasing field the nonlinear dispersion relation becomes quasi-dispersionless along the field, $\omega=V_Ak_\parallel$ (Fig. 2a–c). **Shown**
13. In $\mathcal S(k_\perp,\omega)$ higher $k_\perp$ are excited as the field grows, and a second branch $\omega=k_\perp^{3/2}/2^{1/2}$ appears, interpreted as bound waves [43] (Fig. 2d–f). **Shown**
14. At constant frequency $\omega^\star=600$ the spectrum is an isotropic ring at $V_A^2=0$ and strongly perpendicular-dominated, with stronger nonlinear broadening, at $V_A^2=300$ (Fig. 2g–h). **Shown**
15. Three-wave resonant interactions occurring mainly perpendicular to the field are evidenced by the bicoherence of the elevation (Supplemental Material; pp. 3–4). **Shown** (not in the Letter)
16. $\mathcal S(k)$ agrees with $k^{-15/4}$ at $B=0$; its exponent decreases slightly at intermediate field; at high field it turns to $k^{-3}$, "in rough agreement" with the phenomenological model and Eq. 3 (Fig. 3). **Shown**
17. At $V_A^2=300$, $\mathcal S(k_\perp)\sim k_\perp^{-3}$ while $\mathcal S(k_\parallel)$ is "more than one order of magnitude smaller than $\mathcal S(k_y)$ in the inertial range", so $\mathcal S(k)$ is due mainly to perpendicular transfer (Fig. 3 inset). **Shown**
18. The prefactor scales as $\varepsilon_s^{1/2}$ at fixed $V_A^2=300$ and as $V_A^{-3/2}$ at fixed $\varepsilon_s\approx2.7\times10^{-3}$ "for high enough $V_A$"; the perpendicular prefactor follows the same scalings (Fig. 4 insets). **Shown**
19. Empirical law: $\mathcal S(k)\approx \mathcal S(k_\perp)=C_1\varepsilon_s^{1/2}v_A^{-3/2}k_\perp^{-3}$, with $C_1$ independent of $\varepsilon_s$ and $v_A$ (Eq. 6). **Shown**
20. $\mathcal S(\omega)$ agrees with $\omega^{-17/6}$ at $B=0$; at high field $\mathcal S(\omega)=C_2(\sigma_s/\rho)^{2/3}\varepsilon_s^{1/2}v_A^{-3/2}\omega^{-7/3}$ (Fig. 4, Eq. 7). **Shown**
21. Eqs. 6 and 7 are consistent through $\mathcal S(\omega)\,d\omega=\mathcal S(k)\,dk\approx \mathcal S(k_\perp)\,dk_\perp$ with Eq. 1, which gives $C_2=2C_1/3$; the fits give $C_1=1.7$, $C_2=1.34$, and "the ratio $2C_1/3C_2=0.85$ is as expected close to 1" (p. 5). **Derived** + **Shown**
22. $C_1=1.7$ is "close to" the theoretical $C_m=1.467$ of shear-Alfvén wave turbulence [36] (p. 5). **Shown**
23. The $\varepsilon_s^{1/2}$ scaling is consistent with three-wave interactions [2], and the time-scale separation of wave turbulence holds: the nonlinear time is much longer than the linear time at all $k$ (Supplemental Material; p. 5). **Shown** (not in the Letter)
24. A typical resonant triad has wavevectors of the same order, "suggesting that wave interactions are local"; this differs from the 2D MHD weak-turbulence prediction of nonlocal interactions and a flat stationary spectrum [44] (p. 5). **Shown** (Supplemental Material)
25. In a plasma no wave propagates normal to the field, which receives magnetic energy by shearing; here capillary waves propagate normal to the field and receive the magnetic energy, a different mechanism with the same spectral scaling (p. 4). **Stated**
26. An experiment would need a ferrofluid of high susceptibility and saturation magnetization, but such fluids are "at least ten times the water value" in viscosity, which would prevent wave interactions; similar effects are expected for nonconducting liquids in strong electric fields, by equivalence of the equations [45] (Conclusion). **Stated**

# Printed slips

- **Fig. 4 caption.** It derives the frequency spectra "from Eq. (2) using $\omega\sim k^{-3/2}$" and "from Eq. (3) with $\omega\sim k^{-3/2}$". Eq. 1 gives $\omega\propto k^{3/2}$ on the capillary branch, and only that maps $k^{-15/4}$ to $\omega^{-17/6}$: $\mathcal S(\omega)=\mathcal S(k)\,dk/d\omega\propto k^{-15/4}k^{-1/2}=k^{-17/4}=\omega^{-17/6}$ *(compiler check, not in the sources)*. The Fig. 2 caption writes $\omega=k_y^{3/2}$.
- **Eq. 3.** The energy spectrum is printed "$E^m(k)=v_a^2kS^m(k)$" with a lowercase $v_a$; $v_A$ is the defined symbol.
- **Figs. 3–4 legends.** The first curve is labelled "$V_A=0$", the others $V_A^2=25$ and $V_A^2=300$; the $V_A^2=100$ series announced in the text is not plotted in the spectra.
- **Ref. [44].** The journal is printed "Phys. Rev. 87, 033103 (2013)" without a series letter.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\eta(x,y,t)$ | $\varsigma$ (page-local surface elevation) | **collision** with the Kolmogorov length $\eta$ |
| $\psi$ | $\psi$ (page-local surface velocity potential) | |
| $B$ | $B$ (page-local external horizontal field along $x$) | not the guide field $\boldsymbol B_0$ of a plasma; the liquid has no free charge or current |
| $v_A^2=B^2/(\tilde\mu\rho)$ | $v_A$ (page-local magnetic surface-wave speed) | **collision:** not the registry's plasma Alfvén speed $B_0/\sqrt{4\pi\rho}$; printed once as $v_a$ |
| $V_A^2=v_A^2[\rho/(g\gamma)]^{1/2}$ | $V_A$ (page-local nondimensional field parameter) | |
| $k_x$, $k_y$ | $k_\parallel$, $k_\perp$ | along and across the field |
| $\gamma$ | $\sigma_s$ (page-local surface tension) | **collision** with the ratio of specific heats |
| $\mu$ | $\mu_r$ (page-local relative permeability) | **collision** with the dynamic viscosity |
| $\tilde\mu$ | $\mu_{\mathrm{eff}}=\mu_0(\mu_r+1)/(\mu_r-1)^2$ (page-local) | **collision:** the tilde is not a Favre filter |
| $A_\mu=(\mu-1)/(\mu+1)$ | $A_\mu$ (page-local magnetic Atwood number) | 0.5 |
| $\nu$, $\hat D_k$, $k_d$ | $\nu_h$, $\hat D_k$, $k_d$ (page-local hyperviscosity coefficient, operator, onset) | **collision:** $\nu$ is not the kinematic viscosity |
| $\epsilon$ | $s_w$ (page-local mean wave steepness) | not a dissipation rate |
| $\omega$ | $\omega$ (angular frequency) | **collision** with the specific dissipation rate |
| $\nabla_\perp=\{\partial_x,\partial_y\}$ | (horizontal gradient) | "perp" means horizontal, not perpendicular to the field |
| $\hat k$ | (Fourier multiplier by $k$) | not a test filter |
| $S(k)$, $S(\omega)$ | $\mathcal S(k)$, $\mathcal S(\omega)$ (page-local power spectra of the elevation) | |
| $E(k)$, $E^c$, $E^m$ | (surface-wave energy spectra) | not the registry's 3D kinetic-energy spectrum |
| $P$ | $\varepsilon_s$ (page-local energy flux per unit area and density) | plays the role of $\varepsilon$ |
| $C_{KZ}$, $C_m$, $C$, $C'$ | $C_{KZ}$, $C_m$, $C_1$, $C_2$ (Kolmogorov–Zakharov constant, weak Alfvén constant 1.467, fitted constants 1.7 and 1.34) | |
| $T^m_{nl}$ | $T^m_{\mathrm{nl}}$ (magnetic nonlinear time) | |

# Reference list

45 numbered references ([1]–[45]); ref. [16] prints two works (a 2016 book
and a 2018 article by Galtier), so the list yields 46 entries. It is merged
complete into the [bibliography](/bibliography.md) with `citedby` this
slug. Ref. [40] is the paper's own Supplemental Material, with no author or
title printed; it is a different item from the Letter and is kept as its
own `@misc` entry, `kochurin-2022-b`. Same-key works take suffixes in
printed order (`zakharov-1967`/`-b`, `kochurin-2020`/`-b`); ref. [18] is
the existing entry `galtier-2000`. Ref. [12] prints "et al.". No printed
duplicates or unparseable items.

# Pages created or updated

Chunk 3 (2026-10-26). This source is cited on:

- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Reduced MHD and Elsasser variables](/definitions/reduced-mhd.md)
- [Critical balance and the anisotropic MHD cascade](/properties/critical-balance.md)
- [Weak wave turbulence (magneto-capillary waves)](/results/weak-wave-turbulence.md)
