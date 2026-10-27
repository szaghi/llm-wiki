---
type: Source
title: "Ferrand et al. (2022) — An In-depth Numerical Study of Exact Laws for Compressible Hall Magnetohydrodynamic Turbulence"
description: "Tests two exact laws for the energy cascade rate of isothermal compressible Hall-MHD turbulence term by term on decaying 1024³ pseudo-spectral simulations, finds them numerically equivalent in the inertial range, and shows that their stationary form survives free decay through a time-derivative reservoir term."
resource: "doi:10.3847/1538-4357/ac517a"
source_kind: paper
authors: [Ferrand R., Sahraoui F., Galtier S., Andrés N., Mininni P., Dmitruk P.]
year: 2022
venue: "Astrophys. J. 927:205"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_The_Astrophysical_Journal_Ferrand_An_In-depth_Numerical_Study_of_Exact_Laws_for_Compressible_H.pdf"
tags: [mhd, plasma, energy-cascade, compressible, dns, isotropic-turbulence]
timestamp: 2026-10-27T15:52:00Z
---

# Summary

Ferrand et al. (2022) test two [exact laws](/results/turbulence-exact-laws.md)
of isothermal compressible Hall-MHD turbulence: that of Andrés et al.
(2018), labelled A18, and that of Ferrand et al. (2021a), labelled F21.
Exact laws express the energy cascade rate $\varepsilon$ through two-point
structure functions or correlators. They assume statistical homogeneity, and
reach the stationary inertial-range form only by adding time stationarity,
large-scale forcing and infinite Reynolds numbers. The authors write both
laws in a general form that keeps the time-derivative, dissipative and
forcing terms, so that homogeneity is the only hypothesis. They also derive
the A18 dissipative and forcing terms, which the original paper does not
give.

The data are three $1024^3$ runs of
[decaying](/results/decaying-mhd-turbulence.md) isothermal
[compressible MHD turbulence](/results/compressible-mhd-turbulence.md) with
the Hall term, made with the pseudo-spectral code GHOST. The runs have mean
field $B_0=0$ or 2, initial sonic Mach number 0.25 or 0.5, ion inertial
length $d_i=0.02L_0$ and $\nu=\eta_m=3\times10^{-4}$; a $512^3$ run has a
larger $d_i$. Increment-space divergences use the discrete decomposition of
Taylor et al. (2003) with 73 directions under an isotropy assumption.

In the inertial range the two laws give nearly the same MHD and Hall parts
of the cascade rate at almost all scales, numerical evidence that they are
equivalent. The inertial-range rate near $l/d_i\simeq2$ roughly matches
the energy decay rate. Doubling the Mach number changes little. The Hall
part never dominates below the ion scale, which the authors attribute to
dissipation acting too early, and they recommend hyperviscosity. The
general laws close to within 1 to 1.5 orders of magnitude of their
individual terms. In free decay the time-derivative term acts as a
scale-dependent energy reservoir that feeds both the cascade and the
dissipation, so the stationary form of the laws still holds. The paper
contains no turbulence closure.

# Version read

arXiv preprint arXiv:2201.10819v1 [physics.plasm-ph], 26 January 2022
("Draft version January 27, 2022", AASTeX6), 14 pages, not the ApJ version
of record. Title and authors on page 1 match Crossref. The version read
prints no DOI. Section, equation and figure numbers on this page are those
of the preprint. The text cites "Andrés et al. (2018)" without a suffix
while the reference list prints two different 2018 Andrés papers; which of
them states the A18 law is not decided here.

# Key claims

Page-local symbols: $\boldsymbol l$ the two-point increment
($\boldsymbol r^\dagger=\boldsymbol r+\boldsymbol l$), $\phi^\dagger$ the value of a field
$\phi$ at $\boldsymbol r^\dagger$ (the source writes a prime, not a
fluctuation), $\delta\phi=\phi^\dagger-\phi$, $\nabla_l$
the increment-space gradient, $\langle S_2\rangle$ the F21 structure
function, $R_E$ the A18 energy correlator, $E^{\mathrm{tot}}$ the total
energy density, $\mathcal D$ and $\mathcal F$ the two-point dissipative and
forcing terms, $\lambda_H=m_i/q_e$ the Hall parameter, $\boldsymbol j=\boldsymbol J/\rho$, $d_i$ the ion
inertial length. $\varepsilon$ is the total (kinetic, magnetic and
internal) energy cascade rate.

1. Exact laws follow from statistical homogeneity alone (then time stationarity and infinite Reynolds number) and express the rate of energy flowing to small scales through two-point structure functions "without requiring the use of closure models" (§1). **Stated**
2. Eq. 8 is "the most general equation obtainable in this model under the sole assumption of statistical homogeneity" for $\langle S_2\rangle$; it was already reported by Ferrand et al. (2021a) (§2.1). **Stated** (derivation cited)
3. With stationarity, forcing at the largest scales and infinite kinetic and magnetic Reynolds numbers, Eq. 8 reduces to the F21 law, Eq. 9 (§2.1). **Stated** (derived in Ferrand et al. 2021a)
4. In the general form, Eq. 10, $\varepsilon_{F21}$ is defined by identification with Eq. 9 and does not rely on the assumptions behind it, so Eq. 10 "remains very general" (§2.1). **Derived**
5. In weakly compressible runs ($\rho\sim\rho^\dagger$) the terms $\mathcal D_{F21}$, $\mathcal F_{F21}$ and $\partial_t\langle E^{\mathrm{tot}}\rangle$ are "likely to be scale-independent" but "still have a significant impact on the energy balance" (§2.1). **Stated**; **Shown** in Fig. 9
6. The A18 dissipative and forcing terms, $\mathcal D_{A18}$ (Eq. 24) and $\mathcal F_{A18}$ (Eq. 25), are not given by Andrés et al. (2018); the paper derives them, and $\mathcal F_{A18}=\mathcal F_{F21}$ (§2.2). **Derived**
7. Simulations: three $1024^3$ runs in a periodic box $L_0=2\pi$, $\nu=\eta_m=3\times10^{-4}$ ("$R_e=R_m\simeq3\times10^3$"), $d_i=0.02L_0$, no forcing, random-phase initial modes in the shell $1\le k\le3$ (§3.1, Table 1). **Stated**
8. Run I ($B_0=2$) shows oscillations of kinetic plus magnetic energy matching the internal-energy fluctuations, attributed to wave-initiated energy exchanges as reported by Yang et al. (2021) (§3.1, Fig. 1). **Shown**
9. Energy decay rates by linear fit at the selected times: "$\sim-0.047$" (Run I) and "$\sim-0.087$" (Runs II and III) (§3.1, Figs. 1–2). **Shown**
10. For $B_0=0$ the increment-space divergence reduces to $l^{-2}\partial_l[l^2\langle F_l\rangle(l)]$, averaged over 73 directions; the isotropic decomposition gave better results than the axisymmetric one even for Run I (§3.2, Eqs. 27–28, Appendix, Fig. 10). **Shown**
11. Time derivatives use a five-point central stencil (Eq. 31): for Run I, 11 snapshots between 8 and 9 turnover times and 7 subsets of 5, averaged; for Runs II and III, 5 snapshots, the other terms on the central one. Averaging those terms over the five snapshots "was found to bring no change to the results (not shown)" (§3.3). **Stated**
12. The A18 and F21 laws give "closely similar components (MHD and Hall) of the cascade rate nearly at all scales", which "validates numerically the equivalence of the two exact laws in the inertial range as anticipated in Ferrand et al. (2021a)" (§4, Fig. 3). **Shown**
13. In Runs I and II the inertial-range cascade rate, "centered around $l/d_i\simeq2$", roughly matches the energy decay rate of the linear fit (§4). **Shown**
14. Raising the sonic Mach number from 0.25 to 0.5 "does not bring significant changes to the total dynamics", in agreement with Andrés et al. (2018) up to 0.5; supersonic flows can develop a dominant compressible cascade component (Ferrand et al. 2020) (§4, Fig. 4). **Shown** (subsonic); **Stated** (supersonic)
15. The Hall part of the cascade rate never dominates the MHD part here, "in contrast with results reported previously from 3D CGL simulations (Ferrand et al. 2021b)"; the offered explanation is that the Hall effect is too weak and dissipation stops the cascade first (§4). **Shown** (observation); **Stated** (explanation)
16. Run I-512 ($512^3$, $\nu=\eta_m=8\times10^{-4}$, larger $d_i$) increases the amplitude of the Hall electric field and extends it to smaller scales (Fig. 5, ratio of the Hall to the ideal part of Ohm's law, Eq. 32). **Shown**
17. In Run I the magnetic spectrum scales as $k^{-5/3}$ over roughly $kd_i\in[0.1,0.7]$; below the ion scale the spectra drop without a clear $k^{-7/3}$ range; Run I-512 shows a clearer knee slightly below $1/d_i$ (§4, Fig. 6). **Shown**
18. Run I-512 gives "little enhancement" of the Hall part, which still does not dominate below the ion scale (§4, Fig. 7). **Shown**
19. Increasing $d_i$ further is impractical because whistler dispersion imposes a time-step bound "that roughly behaves as $\sim(dx)^2/(d_iB)$"; hyperviscosity and hyperdiffusivity are recommended instead (§4). **Stated**
20. Free decay breaks the stationarity behind Eqs. 9 and 20, so the general laws Eqs. 29–30 are evaluated (§5). **Derived**
21. For A18 (Eq. 30), the sum of all terms "lies around 1 to 1.5 orders of magnitude below all other terms" in all three runs (§5.1, Fig. 8). **Shown**
22. The large-scale limit $2\varepsilon_{A18}+\partial_t\langle R_E+R_E^\dagger\rangle=0$ (Eq. 33) is "overall well verified by Run II and III" but not by Run I, whose residual rises at large scales; "the reason for this odd behavior is not fully understood yet" (§5.1, Fig. 8). **Shown**
23. In the small-scale limit $\partial_t\langle R_E+R_E^\dagger\rangle\to2\partial_t\langle E^{\mathrm{tot}}\rangle$, giving $2\varepsilon_{A18}+2\partial_t\langle E^{\mathrm{tot}}\rangle+\mathcal D_{A18}=0$ (Eq. 34), verified in all three runs with a residual at least an order of magnitude below the other terms (§5.1). **Derived** and **Shown**
24. In free decay $-\partial_t\langle R_E+R_E^\dagger\rangle$ (A18) and $-\partial_t\langle S_2\rangle$ (F21) act as a scale-dependent reservoir split between the cascade and the dissipation; at large scales $\mathcal D_{A18}\to0$ and almost all of it feeds the cascade (§5.1–5.2, Eq. 35). **Derived** (interpretation of Figs. 8–9)
25. For F21 (Eq. 29) the local dissipative term and $\partial_t\langle E^{\mathrm{tot}}\rangle$ nearly cancel; the F21 balance "still perfectly holds for Run I", which "may suggest that the model depicted by equation (29) is more robust" than A18 (§5.2, Fig. 9). **Shown**
26. Without a mathematical proof, the paper "brings evidence" that the two compressible laws describe the same cascade, as was proven for the incompressible Hall-MHD laws (Ferrand et al. 2019) (§6). **Shown**
27. The stationary inertial-range form of the laws remains valid in decaying turbulence, e.g. in the solar wind far from the Sun (§6). **Shown** (these simulations); **Stated** (solar wind)
28. The reservoir "overall coincides with the energy dissipation rate, which suggests that the considered cascading energy is ultimately bound to be fully dissipated" (§6). **Stated**
29. An axisymmetric decomposition (57 of the 73 directions, at least 45° from $\boldsymbol B_0$, perpendicular flux only) makes the A18 and F21 rates of Run I, "especially the Hall components", agree less well than the isotropic one; the choice should be made "on a case-by-case basis" (Appendix, Fig. 10). **Shown**

# Printed slips

- **Ion inertial length of Run I-512 (§4).** "$d_i=0.05/L_0$", where §3.1 and Table 1 give $d_i=0.02L_0$ for the other runs; a length divided by $L_0$ is not a length.
- **CGL closure (§4).** "Chew, Goldenberg and Low"; the reference list prints Goldberger.
- **$\mu_0$ factor in Eq. 23** *(compiler check, not in the sources)*. With $\boldsymbol v_A=\boldsymbol B/\sqrt{\mu_0\rho}$ (§2.2) and $\boldsymbol d_\eta=\eta\nabla^2\boldsymbol B$ (Eq. 6), each left-hand term of Eq. 23, e.g. $\rho\boldsymbol v_A\cdot\boldsymbol d_\eta^\dagger/\sqrt{\rho^\dagger}=\sqrt{\rho/\rho^\dagger}\,\boldsymbol B\cdot\boldsymbol d_\eta^\dagger/\sqrt{\mu_0}$, carries $1/\sqrt{\mu_0}$, and the four terms sum to $\frac{1}{2\sqrt{\mu_0}}\langle(\sqrt{\rho/\rho^\dagger}+\sqrt{\rho^\dagger/\rho})(\boldsymbol B\cdot\boldsymbol d_\eta^\dagger+\boldsymbol B^\dagger\cdot\boldsymbol d_\eta)\rangle$; the right-hand side prints $1/(2\mu_0)$. The two sides agree if the resistive term of the $\boldsymbol v_A$ equation (Eq. 17) is $\boldsymbol d_\eta/\sqrt{\mu_0\rho}$ rather than the printed $\boldsymbol d_\eta/\sqrt\rho$.
- **Forcing label (§5.1).** "$-\partial_t\langle R_E+R_E^\dagger\rangle\equiv\mathcal F_{F21}$" in the A18 discussion, where the A18 term $\mathcal F_{A18}$ stands; Eq. 25 makes the two equal.

# Notation map

| Ferrand et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf v$, $\rho$, $P$, $\mathbf B$ | $\boldsymbol u$, $\rho$, $p$, $\boldsymbol B$ | SI-like units with $\mu_0$ |
| $\mathbf v_A=\mathbf B/\sqrt{\mu_0\rho}$ | $\boldsymbol v_A$ (local, SI form) | the registry $v_A$ is Gaussian and built on $B_0$ |
| $\eta$ | $\eta_m$ | **collision:** magnetic diffusivity, not the Kolmogorov length |
| $\nu$ ("dynamic viscosity") | $\nu$ | called dynamic viscosity and placed in the $\rho$-weighted Eq. 2, but added to $\partial_t\boldsymbol u$ without $1/\rho$ in Eq. 16; $Re=1/\nu$ "due to the normalization" (§3.1) |
| $\Delta$ | $\nabla^2$ | **collision:** the Laplacian, not the filter width |
| $\theta=\nabla\cdot\mathbf v$ | $\nabla\cdot\boldsymbol u$ | **collision** with the momentum thickness; $\theta$ is also a polar angle in Eq. 27 |
| $\lambda=m_i/q_e$ | $\lambda_H$ (page-local) | **collision** with the Taylor microscale and the MHD perpendicular scale |
| $d_i$ | $d_i$ (page-local) | **collision** with the wall distance $d$ |
| $\mathbf J$, $\mathbf J_c=\mathbf J/\rho$ | $\boldsymbol J$, $\boldsymbol j$ (page-local current density and its ratio to $\rho$) | |
| $\boldsymbol\ell$, $\xi'$, $\delta\xi$ | $\boldsymbol l$, $\xi^\dagger$, $\delta\xi$ (page-local) | **collision:** the prime is the second point, not a fluctuation |
| $\bar\delta\xi=\tfrac12(\xi+\xi')$ | $\{\!\{\xi\}\!\}$ (two-point mean) | **collision:** not the LES filter |
| $\langle\cdot\rangle$ | $\langle\cdot\rangle$ | ensemble average computed as a domain average |
| $\langle S\rangle$ | $\langle S_2\rangle$ (page-local) | **collision** with the strain rate $S_{ij}$ |
| $R_E$, $R_B$, $R_H$, $H$ | (A18 correlators, cross helicity $\rho\boldsymbol u\cdot\boldsymbol v_A$) | **collision:** $R_E$ is not the Reynolds stress |
| $\varepsilon_{F21}$, $\varepsilon_{A18}$, $\varepsilon_{MHD}$, $\varepsilon_{Hall}$ | (energy cascade rates) | **collision:** total-energy cascade rate, not the TKE dissipation $\varepsilon$ |
| $\mathcal D$, $\mathcal D^{loc}$, $\mathcal F$, $\mathcal F^{loc}$ | (page-local) | **collision:** $\mathcal F$ is not the registry's induced filter $\mathcal F_h$ |
| $E^{tot}$ | $E^{\mathrm{tot}}$ (page-local) | kinetic plus magnetic plus internal energy density |
| $c_s$, $\gamma=1.01$, $e$ | $c_s$, $\gamma$, $e_{\mathrm{int}}$ (internal energy per unit mass) | polytropic index close to 1 for the isothermal closure |
| $M_S$ | $M_t$ | initial turbulent sonic Mach number |
| $R_e$, $R_m$ | $Re$, $Rm$ | $1/\nu$, $1/\eta_m$ |
| $N$ | $N_x$ | 1024 or 512 |
| $B_0$, $L_0$ | $\boldsymbol B_0$ (along $z$), (box size) | |
| $\omega$ | $\omega_i$ | vorticity |
| $k_{down}$, $k_{up}$ | (initial spectral shell, 1 and 3) | |

# Reference list

51 printed references, author–year (AAS) style without titles except Simon
& Sahraoui (2021, arXiv). The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Same-year works
are disambiguated in printed order: Andrés et al. 2018 (Phys. Rev. E and J.
Plasma Phys.), Banerjee 2016 and 2017, Carbone 2009, Ferrand 2021a and b.
The in-text "Andrés et al. (2018)" carries no suffix, so the citation of A18
cannot be assigned to one of the two entries from this paper. Gómez et al.
(2005) prints only "Physica Scripta, 123" (volume or page undecidable);
Simon & Sahraoui (2021) is a preprint entry. No printed duplicates.

# Pages created or updated

Chunk 3 (2026-10-26), cited further in chunk 4. This source is cited on:

- [Reduced MHD and Elsasser variables](/definitions/reduced-mhd.md)
- [Compressible MHD turbulence](/results/compressible-mhd-turbulence.md)
- [Decaying MHD turbulence and its invariants](/results/decaying-mhd-turbulence.md)
- [Exact laws of (Hall-)MHD turbulence](/results/turbulence-exact-laws.md)
- [GHOST](/software/ghost.md)
