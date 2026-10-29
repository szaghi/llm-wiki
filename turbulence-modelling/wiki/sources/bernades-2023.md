---
type: Source
title: "Bernades et al. (2023) — Kinetic-energy- and pressure-equilibrium-preserving schemes for real-gas turbulence in the transcritical regime"
description: "Analyses the discrete pressure equation induced by kinetic-energy-preserving split forms for a general equation of state, shows that pressure equilibrium is then reachable at most to second order through a discrete chain rule, and proposes KGP-Pt, a KEP scheme evolving pressure that is exactly pressure-equilibrium preserving."
resource: "doi:10.1016/j.jcp.2023.112477"
source_kind: paper
authors: [Bernades M., Jofre L., Capuano F.]
year: 2023
venue: "J. Comput. Phys. 493:112477"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Journal_of_Computational_Physics_Bernades_Kinetic-energy-_and_pressure-equilibrium-preserving_schemes.pdf"
tags: [kinetic-energy-preserving, pressure-equilibrium, compressible, dns, real-gas]
timestamp: 2026-10-29T10:04:00Z
---

# Summary

Bernades et al. (2023) address compressible turbulence with a real-gas
(Peng–Robinson) equation of state in the high-pressure transcritical
regime, where conventional schemes generate spurious pressure oscillations
and the remedies in use (double-flux models, pressure-based formulations)
discretize convection in divergence form and stabilize it with filtering or
upwind ([WENO](/methods/weno-scheme.md), HLLC) hybridization, adding
dissipation. The authors seek schemes that are both
[kinetic-energy preserving](/properties/kinetic-energy-preservation.md) by
convection and [pressure-equilibrium preserving](/properties/pressure-equilibrium-preservation.md)
(uniform pressure and velocity stay uniform while density varies) for a
general equation of state $p=p(\rho,e)$, without artificial dissipation.
They separate [numerical dissipation](/properties/numerical-dissipation.md),
an unwanted property of a method, from artificial dissipation, added on
purpose.

Starting from the one-parameter family of locally conservative
kinetic-energy-preserving split forms of Coppola et al., with the
Kennedy–Gruber–Pirozzoli (KGP) split for mass and momentum, they derive the
discrete pressure equation induced by three choices of energy variable.
With total or internal energy, pressure equilibrium requires a discrete
chain rule of the derivative operator, and in most cases a product rule as
well; since a discrete chain rule is known only for second-order centred
operators, and holds there to $O(h^2)$, pressure equilibrium is then
reachable at most to second order. Their KGP-Pt scheme evolves a
semi-discrete pressure equation instead of the energy equation: it is
exactly pressure-equilibrium preserving and preserves mass, momentum and
kinetic energy globally and locally, but not total energy.

Tests: a one-dimensional density wave (ideal gas and transcritical N$_2$),
a two-dimensional inviscid transcritical mixing layer, in which the
reference KEP scheme KGP-Et produces noisy pressure and diverges while
KGP-Pt stays smooth, and a [direct numerical simulation](/definitions/direct-numerical-simulation.md)
of a transcritical [channel flow](/benchmarks/turbulent-channel-flow.md)
at $Re_\tau=100$, where KGP-Pt and KGP-Et agree. The compared alternatives
include divergence form with a compact filter, related to the filtered
schemes of the [low-dissipation low-dispersion](/methods/low-dissipation-low-dispersion-scheme.md)
page, and double-flux schemes with HLLC.

# Version read

Version of record (Elsevier, open access CC BY; received 30 March 2023,
revised 22 August 2023, accepted 30 August 2023, online 4 September 2023):
21 pages, all read, pp. 4–9 and 12–13 also visually. Page-1 title,
authors, venue and DOI match the metadata above; no identity issue.
Section, equation, table and figure numbers on this page are those of this
version.

# Key claims

Page-local symbols: $e$ specific internal energy, $e_k=u^2/2$ specific
kinetic energy, $E$ total energy per unit volume (registry); $p_\rho=(\partial p/\partial\rho)_e$,
$p_e=(\partial p/\partial e)_\rho$ and their discrete counterparts
$p^h_\rho$, $p^h_e$; $c$ the speed of sound, $c_v$ the
isochoric specific heat, $\beta_v$ the volume expansivity, $\beta_T$ the
isothermal compressibility, $\boldsymbol q$ the heat flux; $D_x$ the
second-order centred derivative matrix; $C_{\rho\phi}$ the semi-discrete
convective term of $\rho\phi$, with split forms $C^D$, $C^\phi$, $C^u$,
$C^\rho$, $C^L$; $a_{\mathrm K}$, $a_p$, $a_e$ the weights of the source's
Eqs. (11), (12), (21); $W_p$ the pressure term $D_x(pu)$ of
the total-energy equation; $u_0$, $p_0$ uniform values. KEP, PEP and TEC
abbreviate kinetic-energy preserving, pressure-equilibrium preserving and
total-energy conserving.

1. Methods for trans- and supercritical turbulence should ideally be free of numerical and artificial dissipation, free of spurious pressure oscillations, and stable at inviscid conditions; numerical dissipation (undesired behaviour) differs from artificial dissipation (deliberately added) (§1; footnote 1). **Stated**
2. Pressure-based and double-flux approaches discretize convection in divergence form, which is non-linearly unstable in convection-dominated problems, and need filtering or HLLC/WENO hybridization; filtering can interact with thermodynamic non-linearities and amplify pressure oscillations [16] (§1). **Stated**
3. The pressure equation $\partial_tp+\nabla\cdot(p\boldsymbol u)=-(\rho c^2-p)\nabla\cdot\boldsymbol u+\frac1\rho\frac{\beta_v}{c_v\beta_T}(\sigma_{ij}\partial_ju_i-\nabla\cdot\boldsymbol q)$ (Eq. 4) is equivalent to the total-energy equation for a general $p(\rho,e)$ but has different discrete properties (§2.1). **Derived**
4. Locally conservative KEP forms are the family $C^{\mathrm{KEP}}_{\rho\phi}=a_{\mathrm K}\frac{C^D_{\rho\phi}+C^\phi_{\rho\phi}}{2}+(1-a_{\mathrm K})\frac{C^u_{\rho\phi}+C^\rho_{\rho\phi}}{2}$ (Eq. 11): $a_{\mathrm K}=0$ Feiereisen, $a_{\mathrm K}=1$ the "C" form, $a_{\mathrm K}=1/2$ KGP; $C^L$ is excluded because it is not a difference of fluxes (§3.1.1, from [23]). **Stated**
5. The KEP property depends only on the discretization of continuity and momentum; pressure equilibrium depends on the choice of energy variable and its discretization (§3.1.2). **Derived**
6. With $u=u_0$ every split reduces to $C_\rho=u_0D_x\rho$, $C_{\rho u}=u_0^2D_x\rho$, $C_{\rho e_k}=\frac{u_0^3}{2}D_x\rho$ (Eq. 16), so the induced velocity equation gives $u_t=0$ for any split of $C_\rho$, $C_{\rho u}$ (§3.1.2, Eq. 17). **Derived**
7. With the total-energy equation, the induced pressure equation is $p_t=\big[\frac{p_e}{\rho}e-p_\rho\big]u_0D_x\rho-\frac{p_e}{\rho}\big[C_{\rho e}+W_p\big]$ (Eq. 20); pressure equilibrium then needs $a_e=0$ in Eq. (21), a $W_p$ vanishing at equilibrium and a discrete chain rule (Eqs. 22–23) (§3.1.2). **Derived**
8. KGP-Et (KGP split applied to the total enthalpy, pressure term inside convection, as in [22,52]) is not PEP: it needs both the product and the chain rule (§3.1.2–3.1.3, Table 1). **Derived**
9. Second-order centred operators satisfy a discrete chain rule $D_xp=p^h_\rho D_x\rho+p^h_e D_xe$ (Eq. 23), with discrete Jacobians second-order accurate at interior nodes; the result does not extend to higher-order operators [50] (§3.1.2). **Stated** (from Ranocha [50])
10. For an ideal gas the first term of Eq. (20) cancels and pressure equilibrium reduces to $C_{\rho e}+W_p=0$ [51]; Shima et al. [10] achieve it with $C_{\rho e}=(C^D_{\rho e}+C^u_{\rho e})/2$ (PEP-IG) (§3.1.2). **Derived**/**Stated**
11. With $\rho e$ as state variable, $a_e=1$ is needed in Eq. (21) to reach Eq. (22), and the resulting split would be PEP for ideal gases (§3.1.2). **Stated**
12. Internal-energy schemes are total-energy conserving when a KEP method is used, $C_{\rho e}$ is locally conservative and the induced pressure term is an advective form of $D_x(pu)$; hence KGP-et-CR is TEC (§3.1.2). **Derived**
13. With the pressure equation (Eq. 26), any $a_p$ gives $p_t=0$ at equilibrium (exact PEP); total-energy conservation is lost because the induced total-energy equation (Eq. 28) needs an exact chain rule and a product rule; the error lies only in the induced internal-energy balance, the induced kinetic-energy balance being independent of the energy discretization (§3.1.2, Eqs. 27–28). **Derived**
14. "The discrete chain rule appears to constitute a barrier for the development of PEP methods, at least for discretizations based on linear finite-differencing schemes"; it is "only available for second-order differential operators, and is satisfied to $O(h^2)$" (§3.1.3); with total or internal energy, "the discrete pressure-equilibrium condition can be fulfilled at most to second-order accuracy" (Abstract). **Derived**
15. KGP-Pt (KGP plus the pressure equation with $a_p=0$) is, to the authors' knowledge, novel; it is PEP and preserves mass, momentum and kinetic energy globally and locally, but not total energy (§3.1.3, Table 1). **Derived**
16. Table 1: KGP-Et is TEC, not PEP; KGP-Et-CR and KGP-et-CR are TEC and PEP given only a chain rule; KGP-Pt is PEP, not TEC; PEP-IG is TEC, not PEP for a general equation of state. **Derived**
17. Ideal-gas density wave (41 points, CFL 0.3, RK4, $t/t_c=11$): only divergence form, PEP-IG and KGP-Pt are free of pressure oscillations, KGP-Et is not; HLLC dissipates the wave, the Ducros-sensor hybrid slightly less, its sensor being activated mostly by the oscillations (§4.1.1, Fig. 1). **Shown**
18. Transcritical N$_2$ density wave: KGP-Et is not PEP; the chain-rule schemes bring no practical advantage; PEP-IG is not PEP for a real-gas equation of state; double flux avoids pressure disturbances only with an upwind method (UB-Df), not with KGP; filtering does not suppress the oscillations, worst across the pseudo-boiling line; only D-Pt+F4 and KGP-Pt keep pressure equilibrium (§4.1.2, Fig. 2). **Shown**
19. Grid refinement: total- and internal-energy schemes conserve total energy to machine accuracy; for KGP-Pt the total-energy error decays on average as $O(h^2)$ and total energy decreases in all cases; the PEP error is mostly second order; KGP-Et-CR gives PEP errors several orders of magnitude above the others (§4.1.2, Fig. 3). **Shown**
20. KGP-et-CR behaves better than KGP-Et-CR, attributed to the consistency of internal- and kinetic-energy fluxes enforced as in KEEP [24] (§4.1.2, §3.1.3). **Shown** (attribution **Stated**)
21. Inviscid transcritical mixing layer with KGP-Pt: mass and momentum preserved to machine accuracy; total energy not conserved; kinetic energy slightly dissipated, "supposedly as a result of the temporal integrator"; global entropy well conserved although the scheme is not entropy preserving; total-energy error $O(h^2)$ over three grids and dissipative (§4.2, Fig. 5). **Shown**
22. On the $64\times32$ grid at $t/t_c=0.2$ KGP-Et produces noisy pressure that contaminates the velocity and diverges shortly after, while KGP-Pt captures the pressure variations without artificial mechanisms: "the KEP property alone is not sufficient to tackle transcritical flows" (§4.2, Figs. 6–7). **Shown**
23. Transcritical channel DNS ($Re_\tau=100$ at the cold wall, $128^3$, solver RHEA): KGP-Pt and KGP-Et agree to plotting accuracy in mean and Favre-fluctuation statistics of velocity and temperature, Prandtl number and compressibility factor; the lack of total-energy conservation causes no deviation (§4.3, Figs. 8–10). **Shown**
24. In the channel, "pressure oscillations are mitigated by physical viscosity and standard KEP schemes can be profitably applied"; KGP-Et proved stable at relatively low Reynolds numbers [59] (§4.3, §5). **Shown**/**Stated**
25. The obstacle to TEC, KEP and PEP together for a real-gas equation of state is analogous to the difficulty of entropy conservation with arithmetic-average fluxes; a possible remedy is non-linear-average finite-volume fluxes, expected to be cumbersome for Peng–Robinson (§5). **Stated** (conjecture)
26. The relative importance of primary and secondary conservation properties depends on the flow physics, and sacrificing one (here total energy) may be necessary (§5). **Stated**

# Printed slips

- **§4.2, after Eq. (34):** "$k=6$ in order to trigger 3 vortices roll-ups within the domain (wavelength $\lambda=1/k=1/3$ m)", while the same section prints $t_c=\lambda/\Delta u=2/(k\Delta u)$; *(compiler check, not in the sources)* $1/k=1/6$, and $2/k=1/3$ m is the wavelength of $\sin(k\pi x)$.
- **§4.2:** "$A=0.1$ is the amplitude factor reduction", but $A$ appears neither in Eq. (34) nor in $a_y$.
- **§4.2, Eq. (33) against the text** *(compiler check, not in the sources)*: with $u_0=25$ m/s and $A_u=3/8$, Eq. (33) gives far-field velocities $25(1\pm0.375)=15.625$ and $34.375$ m/s, a difference of 18.75 m/s, while the text gives $\Delta u=10$ m/s and $u_{bw}=20$ m/s. The temperature profile of Eq. (33) does give $0.75T_c$ on top and $1.5T_c$ at the bottom, as stated.
- **§3.1.1:** the generalized energy is defined as $G^\phi=\rho\phi^2/2$, but the text then writes "$G^E=\rho E^2$".
- **Table 2:** D+F4 and D-Pt+F4 use "Eq. (29) with $\alpha_f=0.495$ and $N_f=1$"; *(compiler check, not in the sources)* the F4 coefficients $a_0$, $a_1$, $a_2$ of §3.2.1 need $N_f=2$ in the sum $\sum_{n=0}^{N_f}$ of Eq. (29).
- **Table 1, PEP-IG row:** the energy equation is Eq. (24) (internal energy), yet the row carries a $C_{\rho k}=C^{KGP}_{\rho k}$ entry and "$\eta=0$" under the $C_p$ (pressure-equation convection) column.
- **Notation:** "$v_0=1$ m/s" (§4.1.1) against $u_0$ (§4.1.2); Fig. 7 caption "$y/L_y=0.125$", "$x/L_x=0$" against the text's "$y/L$", "$x/L$"; §4.3 "Favre-averaged fluctuations for temperature are shown in Fig. 10(a) for bottom and walls" (missing "top").
- **References:** [60] (Ducros et al. 1999) is printed with volume "1252", kept as printed and left to a venue check; [18] prints "F. Toro" and [58] "E.F. Toro" for the same author.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $P$ (also $p$) | $p$ | |
| $\mathbf u$, $u$ | $\boldsymbol u$, $u$ | |
| $E$ (specific), $\rho E$ | $E/\rho$, $E$ | **collision:** the source's $E$ is per unit mass, the registry's per unit volume |
| $e$, $k=u^2/2$ | $e$, $e_k$ (page-local) | **collision:** the source's $k$ is not the turbulent kinetic energy |
| $h=e+u^2/2+\hat p$, $\hat p=P/\rho$ | (specific total enthalpy, page-local) | **collision:** $h$ is also the grid spacing $L/N$ in the source, which agrees with the registry's $h$ |
| $\boldsymbol\tau$ | $\sigma_{ij}$ | viscous stress; **collision:** not the subgrid stress |
| $\mathbf q$, $\kappa$ | $\boldsymbol q$, (thermal conductivity) | **collision:** $\kappa$ is not the von Kármán constant |
| $P_\rho$, $P_e$, $\widetilde{P_\rho}$, $\widetilde{P_e}$ | $p_\rho$, $p_e$, $p^h_\rho$, $p^h_e$ (page-local) | **collision:** the tilde marks discrete Jacobians, not a Favre filter |
| $c$, $c_v$, $c_p$, $s$ | (speed of sound, specific heats, specific entropy) | |
| $\beta_s$, $\beta_T$, $\beta_v$ | (compressibilities, volume expansivity) | **collision:** not the field-inversion $\beta$ |
| $\omega$ | (acentric factor) | **collision:** not the specific dissipation rate |
| $\xi$, $\eta$, $\chi$ | $a_{\mathrm K}$ (registry §11), $a_p$, $a_e$ (page-local) | **collision:** not the reference coordinate, the Kolmogorov length or the SA ratio |
| $\Pi_{\rho E}$ | $W_p$ (page-local) | **collision:** not the SGS energy flux $\Pi$ |
| $C_p$ (convective term of the pressure equation) | $C_{\mathrm{pr}}$ (page-local) | **collision:** not the pressure coefficient |
| $\bar u$, $\bar P$ | $u_0$, $p_0$ | **collision:** the overbar is a uniform value; also the compact-filter output in Eq. (29) and the domain integral in Eq. (31) |
| $\delta_x$ | $D_x$ (registry §11, as on [pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)) | discrete derivative matrix |
| $\alpha_f$, $a_n$, $N_f$ | (compact-filter parameters) | **collision:** $N_f$ is a stencil half-width, not the registry's modal test-filter degree |
| $\lambda$ | (perturbation wavelength) | **collision:** not the Taylor microscale |
| $\theta$, $\delta$ | $\theta$, $\delta$ | momentum thickness of the mixing layer; channel half-height; agree |
| $Re_{\tau,bw}$, $u_{\tau,bw}$, $y^+$, $\Delta x^+$, $\Delta z^+$ | $Re_\tau$, $u_\tau$, $y^+$, $\Delta x^+$, $\Delta z^+$ | cold (bottom) wall values |
| $Z$, $Pr$ | (compressibility factor), $Pr$ | |

# Reference list

65 printed references, numbered style ([1]–[65]) with titles. The list is
merged complete into the [bibliography](/bibliography.md) with `citedby`
this slug. Ref. [5] (Bernades, Capuano & Jofre, Phys. Fluids 35:015163,
2023) is a different work from this one and is keyed `bernades-2023-b`,
since `bernades-2023` is this Source. Same-author
same-year works are keyed in printed order (three Bernades 2022, two each
of Jofre 2023, Coppola 2019, Jameson 2008, Capuano 2017). [7] prints no
page or article number, [30] no volume, [20] "p. 759" for a Stanford
report; [45] and [46] are arXiv preprints; [60] carries the printed volume
"1252". No item is unparseable.

# Pages created or updated

Chunk 4 (2026-10-26), cited further in chunks 7–8. This source is cited on:

- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Shock sensors and troubled-cell indicators](/definitions/shock-sensor.md)
- [Low-dissipation low-dispersion schemes with shock sensor](/methods/low-dissipation-low-dispersion-scheme.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
- [Entropy conservation and entropy stability](/properties/entropy-conservation.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)
