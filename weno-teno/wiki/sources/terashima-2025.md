---
type: Source
title: "Terashima et al. (2025) — Approximately pressure-equilibrium-preserving scheme for fully conservative simulations of compressible multi-species and real-fluid interfacial flows"
description: "Derives the discrete pressure-equilibrium condition on interface values for multi-species flow with any equation of state and builds APEC, a fully conservative kinetic-energy-preserving central flux whose internal-energy interface value keeps pressure equilibrium to second order, tested on ideal-gas and transcritical CH4/N2 interfaces."
resource: "doi:10.1016/j.jcp.2024.113701"
source_kind: paper
authors: [Terashima H., Ly N., Ihme M.]
year: 2025
venue: "J. Comput. Phys. 524:113701"
local_file: "/home/stefano/papers/mosaic/weno-teno/2025_Crossref_Journal_of_Computational_Physics_Terashima_Approximately_pressure-equilibrium-preserving_scheme_for_ful.pdf"
tags: [pressure-equilibrium, multiphase, kinetic-energy-preserving, central-scheme, real-fluid]
timestamp: 2026-10-23T19:55:00Z
---

# Summary

Terashima et al. (2025) address the spurious pressure oscillations that fully
conservative discretizations of the
[multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)
produce at material interfaces. With a real-fluid equation of state they appear
even for one species, e.g. cryogenic nitrogen injected into warm nitrogen at
supercritical pressure. Quasi-conservative, double-flux, pressure-based and
enthalpy-based remedies give up total-energy conservation.
[Fujiwara et al. (2023)](/sources/fujiwara-2023.md) built fully conservative fluxes
that keep [pressure equilibrium](/properties/pressure-equilibrium-preservation.md)
exactly, but only for the calorically perfect mixture.

For uniform initial pressure and velocity the authors reduce the discrete
equilibrium condition to a condition on the interface ("half-point") values of the
partial densities $\rho Y_k$ and of $\rho e$, with coefficients
$\mathsf e_k=(\partial\rho e/\partial\rho Y_k)_{\rho Y_{l\ne k},p}$ evaluated at the
node. That condition is asymmetric between the two interfaces of a cell. They split
it into two half-cell relations, shift one and subtract, which gives a symmetric
formula for $(\rho e)_{i+1/2}$. With the arithmetic mean for $(\rho Y_k)_{i+1/2}$
the internal-energy value becomes the arithmetic mean minus a jump correction. Put
into the kinetic-energy-preserving [split form](/methods/split-convective-forms.md),
this is the [APEC flux](/methods/apec-scheme.md). It holds for any equation of state
through $\mathsf e_k$, here the Soave–Redlich–Kwong one. A modified-equation
analysis gives a second-order residual for APEC and for the standard split form
(FC-NPE), with smaller coefficients for APEC. A quasi-conservative variant, PEqC,
keeps equilibrium exactly at the cost of energy conservation; an HLLC-type upwind
form is given in Appendix A.

The tests are smooth [interface advection](/benchmarks/material-interface-advection.md)
problems: a 1D two-species ideal gas, a 1D and 2D transcritical CH4/N2 interface,
and a 2D interface with tangential shear. FC-NPE blows up in every case. APEC
stays stable, conserves energy to round-off, and its equilibrium residual converges
at second order.

# Version read

The archive file is the version of record (J. Comput. Phys. 524:113701; received
21 February 2024, revised 14 November 2024, accepted 21 December 2024, online
27 December 2024), 20 pages, all read; pp. 4–7 and 10 checked on the page images.
Title, authors and DOI match the Crossref record. The ligature artefacts of the PDF
("rea­-fluid", "mod­fied") are font rendering, not slips.

# Key claims

Registry notation: nodes $x_i$ (source $m$) with interface values $(\cdot)_{i+1/2}$,
velocity $v$, total energy $E=\rho e+\tfrac12\rho v^2$, partial densities
$\rho Y_k$ of species $k$. Page-local: $N_{\mathrm s}$ the number of species;
$\mathsf e_k=(\partial\rho e/\partial\rho Y_k)_{\rho Y_{l\ne k},p}$ (source
$\epsilon_i$), with $\mathsf e_k'$, $\mathsf e_k''$ its $x$-derivatives;
$f_{\mathrm{PE}}$ the discrete equilibrium residual; $F_{\rho Y_k}$, $F_{\rho v}$,
$F_E$ the physical fluxes.

1. The equilibrium condition on the fluxes for multi-species flow with an equation of state $p=p(\rho Y_1,\dots,\rho Y_{N_{\mathrm s}},\rho v,E)$ is $\partial_xF_E=\sum_k(\partial E/\partial\rho Y_k)_{\rho Y_{l\ne k},\rho v,p}\,\partial_xF_{\rho Y_k}+(\partial E/\partial\rho v)_{\rho Y_k,p}\,\partial_xF_{\rho v}$ (§2.3, Eq. (11)). **Derived**
2. The velocity-equilibrium condition $\partial_xF_{\rho v}=v\sum_k\partial_xF_{\rho Y_k}$ (Eq. (12)) holds automatically at the discrete level for the flux form (6)–(8) when pressure and velocity are uniform (§2.5). **Derived**
3. For uniform initial $p_0$, $v_0$ the discrete condition reduces to $(\rho e)_{i+1/2}-(\rho e)_{i-1/2}=\sum_k\mathsf e_k\vert_i\big((\rho Y_k)_{i+1/2}-(\rho Y_k)_{i-1/2}\big)$ (Eq. (19)), which "corresponds to the PE compatibility condition derived in [15]" (Fujiwara et al.). **Derived**
4. Because $\mathsf e_k$ is evaluated at $x_i$, Eq. (19) is asymmetric and "no locally-defined half-point values satisfy Eq. (19) for all cells", "and thereby no conservative schemes may be constructed" (§2.5, §2.6). **Stated** (argued, not proved)
5. Splitting Eq. (19) into the half-cell relations (20)–(21) is "one of the sufficient conditions"; combining (20) with the shifted (22) yields the symmetric half-point formula (23) (§2.6). **Derived**
6. The half-point value of $\rho Y_k$ is not fixed by the equilibrium condition; with the arithmetic mean (24), $(\rho e)_{i+1/2}=\tfrac12\big((\rho e)_i+(\rho e)_{i+1}\big)-\sum_k\tfrac12(\mathsf e_k\vert_{i+1}-\mathsf e_k\vert_i)\,\tfrac12\big((\rho Y_k)_{i+1}-(\rho Y_k)_i\big)$ (Eq. (25)); the second term "serves as a sensor to approximately preserve the PE condition" (§2.6). **Derived**
7. The leading residual of APEC is $\sum_k\big\{\tfrac1{12}\mathsf e_k'(\rho Y_k)''-\tfrac1{12}\mathsf e_k''(\rho Y_k)'\big\}\Delta x^2$ (Eq. (32)); that of the arithmetic-mean scheme FC-NPE is $\sum_k\big\{\tfrac13\mathsf e_k'(\rho Y_k)''+\tfrac16\mathsf e_k''(\rho Y_k)'\big\}\Delta x^2$ (Eq. (33)); both are second order (§2.7). **Derived** *(Compiler check, not in the sources: a Taylor expansion of the residual (27) and of the arithmetic-mean residual, with the continuous condition $(\rho e)'=\sum_k\mathsf e_k(\rho Y_k)'$ imposed, reproduces both coefficient pairs.)*
8. Ranking the two residuals analytically "is configuration dependent"; only the coefficients are smaller for APEC (§2.7). **Stated**
9. If $\sum_k\mathsf e_k'(\rho Y_k)''=\sum_k\mathsf e_k''(\rho Y_k)'$ (Eq. (34)), the second-order residual of APEC vanishes (§2.7). **Derived**
10. APEC is the kinetic-energy-preserving split-form fluxes (35)–(39) plus the new internal-energy flux (40), $(\rho ev)_{i+1/2}=(\rho e)_{i+1/2}\,\tfrac12(v_i+v_{i+1})$ with $(\rho e)_{i+1/2}$ from Eq. (25); the idea applies to upwind schemes too (App. A) (§2.8). **Derived**
11. For any equation of state, $\mathsf e_k=-\rho C_v(\partial p/\partial\rho_k)_{\rho_{l\ne k},T}/(\partial p/\partial T)_{\rho_k}+(\partial\rho e/\partial\rho_k)_{\rho_{l\ne k},T}$ (Eq. (48), App. B). **Derived**
12. PEqC (Eq. (54)) replaces $\partial_x(\rho ev)$ in the energy equation by $\sum_k\mathsf e_k\partial_x(\rho Y_kv)$, preserves equilibrium "precisely" without a pressure evolution equation, and is quasi-conservative (§2.11). **Derived**; equilibrium kept at $10^{-8}$ (Fig. 7) **Shown**
13. APEC does not reduce to Fujiwara's half-point values for the calorically perfect gas; substituting Fujiwara's $(\rho Y_k)_{i+1/2}$ (Eq. (60)) into Eq. (23) yields Fujiwara's arithmetic $(\rho e)_{i+1/2}$ (Eq. (61)) (§3.1). **Derived**
14. The authors "speculate" that Fujiwara's $\rho Y_k$ half-point value makes the scheme solve Abgrall's transport equation of the specific-heat ratio implicitly (§3.1). **Stated**
15. Ideal-gas 1D advection (501 points, $t=8$): FC-NPE generates pressure and velocity oscillations, its equilibrium error diverges from about $t=4.0$ and it blows up after $t=9.0$; APEC keeps the error at $10^{-5}$–$10^{-4}$ without divergence; the error of APEC is "more significant than that with Fujiwara's scheme" (§3.1, Figs. 1–2). **Shown**
16. APEC, FC-NPE and Fujiwara's scheme all conserve total energy to "a sufficiently small order" (Fig. 2a). **Shown**
17. The residual norm of APEC stays nearly constant in time; that of FC-NPE diverges around $t=4.0$ (Fig. 4). **Shown**
18. The residual $f_{\mathrm{PE}}$ of APEC converges at second order under refinement (from 251 points; $t=20$ in Fig. 5, CH4/N2 at $t=0.05$ s in Fig. 10). **Shown**
19. CH4/N2 transcritical 1D advection with the SRK equation of state (501 points): FC-NPE blows up after $t=0.09$ s; APEC is stable over twenty flow-through times; PEqC keeps the equilibrium error at $10^{-8}$ but its energy error grows (Figs. 6–7); Fujiwara's scheme cannot be applied with SRK. **Shown**
20. The maximum error fields (Eqs. (63)–(64)) of APEC are about one quarter of those of FC-NPE at $t=0$ in the CH4/N2 case, attributed to the coefficients; the conclusion says "approximately four times smaller" (§3.2.1, Fig. 8, §4). **Shown**
21. Refinement does not cure FC-NPE: with 501 to 4001 points its error diverges in all cases, and with 4001 points it blows up around $t=0.11$ s; APEC with 4001 points keeps the error almost at its initial value (Fig. 11). **Shown**
22. 2D diagonal CH4/N2 advection ($501\times501$, $t=0.09$ s): FC-NPE reaches errors of about 10% in pressure, 5% in velocity and a 10% temperature overshoot and blows up around $t=0.1$ s; APEC's maximum errors are about 0.02% in pressure and 0.01% in velocity (§3.2.2, Fig. 12). **Shown**
23. 2D advection with tangential velocity ($2001\times2001$): FC-NPE fails before $t=0.044$ s; APEC keeps the pressure and transverse-velocity profiles and conserves total energy; on $3001\times3001$ FC-NPE still oscillates around $t=0.03$ s (§3.2.3, Fig. 14). **Shown**
24. APEC eventually becomes unstable in the shear case as the interface thins, which the authors attribute to under-resolved species-density and temperature oscillations, "not oscillations driven by PE errors" (§3.2.3). **Stated**
25. The second-order residual of APEC "could lead to numerical instabilities if the grid resolution is insufficient", especially for large density ratios; discontinuous problems are left to future work (§3.2.3, §4). **Stated**
26. Before this work "no numerical methods exist to preserve the full conservation and pressure equilibrium properties for compressible multi-species and real-fluid flow simulations"; Fujiwara et al. is "the first one" to preserve both, for the calorically perfect gas (§1). **Stated**

Time integration in all tests is the third-order TVD Runge–Kutta scheme at CFL 0.6.
"Second order" above is the truncation order of the equilibrium residual, not of the
scheme.

# Printed slips

- Definition of $\mathsf e_k$ after Eq. (21) and after Eq. (40) (pp. 4 and 6, checked on the page images): "$(\partial\rho e/\partial\rho Y_i)_{\rho Y_{j\ne j},p}$"; Eqs. (17), (19) and (48) print $j\ne i$.
- Energy-conservation error (§3.1, p. 10): "$\sum_t\{(\sum_{m=1}^{N_g}E_m(t)/\sum_{m=1}^{N_g}E_{0,m})-1\}$"; the leading sum over time does not match a quantity plotted against $t$ in Fig. 2(a).
- Abstract: "The numerical fluxes of internal energy and species-mass are newly constructed"; the species half-point value is the arithmetic mean (24) and the species flux (35) is that of FC-NPE; §2.8 calls only the internal-energy flux (40) new.

# Notation map

| Terashima et al. (2025) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $m$, $\cdot\vert_{m+1/2}$ | $i$, $(\cdot)_{i+1/2}$ | a single central interface value, not $u^\pm_{i+1/2}$ |
| $i$ (species), $N$ | $k$, $N_{\mathrm s}$ (local) | **collision** of $N$ with the DG degree |
| $\rho Y_i$, $\rho_i$; $Y_i$, $X_i$ | $\rho Y_k$; mass and mole fractions | |
| $u$, $v$ | $v_1$, $v_2$ ($v$ in 1D) | |
| $\rho E$, $E=e+\tfrac12uu$ | $E$ (per volume), $e$ | the source's $E$ is specific |
| $F_{\rho Y_i}$, $F_{\rho u}$, $F_{\rho E}$ | $F_{\rho Y_k}$, $F_{\rho v}$, $F_E$ (local) | |
| $\epsilon_i$ | $\mathsf e_k$ (local) | **collision** with the WENO $\epsilon$ and the molar energy $\epsilon_k$ |
| $f_{PE}$; $e^{\rm APEC}$, $e^{\rm FC-NPE}$ | $f_{\mathrm{PE}}$; leading error fields (local) | |
| $\bar M$, $M_i$ | $\bar W$, $W_k$ | molar masses; **collision** of $M$ with the Mach number |
| $\bar\gamma$, $\gamma_i$ | mixture and species $\gamma$ | |
| $a\alpha(T)$, $b$, $\omega_i$ | SRK parameters, acentric factor (local) | **collision** of $\omega$ with WENO weights |
| $C_v$, $T$, $R_u$ | specific heat, temperature, gas constant | |
| APEC, FC-NPE, PEqC | as named | |

# Reference list

The paper prints 23 references, numbered [1]–[23], with titles and no DOIs. The list
is merged complete into the [bibliography](/bibliography.md), with `citedby`
including `terashima-2025`. Ref. [15] is the ingested
[Fujiwara et al. (2023)](/sources/fujiwara-2023.md). The two Terashima 2013 items
(Comput. Fluids 88 and J. Propuls. Power 29) are suffixed in printed order, the first
matching the existing entry; ref. [21] (Chemkin-II) is a Sandia report matching the
existing entry; ref. [16] prints the first author as "Bernades". No item is
unparseable.

# Pages created or updated

Chunk 10 (2026-10-23). This source is cited on:

* [APEC flux for approximate pressure equilibrium](/methods/apec-scheme.md)
* [Material-interface advection tests](/benchmarks/material-interface-advection.md)
* [Multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)
* [Pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)
* [Split convective forms](/methods/split-convective-forms.md)
