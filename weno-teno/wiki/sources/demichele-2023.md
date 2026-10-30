---
type: Source
title: "De Michele & Coppola (2023) — Numerical treatment of the energy equation in compressible flows simulations"
description: "Analysis of which energy-like equation (total or internal energy, pressure, total enthalpy, sound speed, entropy) to discretize alongside kinetic-energy-preserving central mass and momentum fluxes: induced discrete equations, local conservation, pressure-equilibrium conditions, six new formulations, and robustness tests on the isentropic and Taylor–Green vortices."
resource: "doi:10.1016/j.compfluid.2022.105709"
source_kind: paper
authors: [De Michele C., Coppola G.]
year: 2023
venue: "Comput. Fluids 250:105709"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Computers_amp_Fluids_De_Numerical_treatment_of_the_energy_equation_in_compressible_f.pdf"
tags: [kinetic-energy-preserving, finite-difference, central-scheme, entropy-stable, turbulence]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

The paper asks how the choice of the third balance law, solved with mass and
momentum, affects the discrete conservation properties of central,
non-dissipative finite-difference discretizations of the Euler equations for
shock-free flows. Six choices are compared: total energy $\rho E$, internal
energy $\rho e$, pressure $p$, total enthalpy $\rho H$, sound speed $\rho c$
and entropy $\rho s$. Mass and momentum always use the locally conservative,
[kinetic-energy-preserving](/properties/kinetic-energy-preservation.md)
one-parameter family of [split convective forms](/methods/split-convective-forms.md)
of Coppola et al. (weight $\zeta$: Feiereisen at $\zeta=1$, Kennedy–Gruber–Pirozzoli
(KGP) at $\zeta=\tfrac12$, Coppola et al. at $\zeta=0$). For each choice the
discrete equations *induced* on the other quantities follow from one general
formula that uses only the chain rule in time, valid for exact time
integration, and summation by parts; the discrete product rule is never used.

The analytical results are as follows. The second-order family is a
finite-volume flux with face mass flux
$m_{i+1/2}=\zeta\,\overline{\rho v}+(1-\zeta)\tfrac12(\rho_iv_{i+1}+\rho_{i+1}v_i)$.
The generalized kinetic energy $\tfrac12\rho\phi^2$ then has the local flux
$\tfrac12\phi_i\phi_{i+1}m_{i+1/2}$, which also allows a face-wise weight
$\zeta_i$. Locally conservative discretizations of $\rho e$, $p$, $\rho H$ or
$\rho c$ induce a locally conservative $\rho E$, and conversely. No such
scheme conserves entropy exactly, while a direct entropy discretization
conserves $\rho s$ but loses $\rho E$. A KEP discretization of the
sound-speed equation preserves $\rho c\propto\rho\sqrt e$. Conditions for
[pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)
are stated, and the schemes of Kuya et al. (KEEP), Shima et al.,
Singh–Chandrashekar, Jameson–Pirozzoli, Kok and Honein–Moin are placed
against them. Tables 1–2 collect the induced terms, the second-order fluxes
and the preserved quantities of fifteen formulations, six of them new.

Tests on the [isentropic vortex](/benchmarks/isentropic-vortex.md)
(eighth-order $40\times40$; fourth-order $30\times30$ to $t=50$ at three CFL
numbers) and the inviscid [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
($32^3$, fourth order, RK4) find the internal-energy and entropy formulations
with the KGP splitting the most robust and accurate. The authors conclude
that a KEP treatment of the energy equation itself is "not necessarily the
best option".

# Version read

arXiv preprint arXiv:2210.01251v1 [physics.flu-dyn], 3 Oct 2022 (footer
"Preprint submitted to Computers and Fluids, October 5, 2022"), 40 pages, all
read; not the version of record. Page 1 title and authors match Crossref.
Equation, table and reference numbers on this page are those of v1.

# Key claims

Registry notation (see the notation map): the source's blending weight $\xi$
is $\zeta$ (page-local, as on the split-forms pages), its velocity $u_\alpha$
is $v$, its mesh width $h$ is $\Delta x$; $\overline a=\tfrac12(a_i+a_{i+1})$
and $[\![g]\!]=(g_{i+1/2}-g_{i-1/2})/\Delta x$ denotes a **flux difference**
(page-local, not the registry's interface jump).

1. At the continuous level any of the $\rho e$, $p$, $\rho H$, $\rho c$, $\rho s$ equations can replace the total-energy equation; the kinetic-energy equation cannot, because it involves only mass and momentum (§2.1). **Stated**
2. With central schemes on uniform periodic meshes summation by parts holds and the discrete product rule does not; all results use only algebraic relations, SBP and the chain rule in time under exact time integration (§2.2). **Stated**
3. The family $\mathcal M=\zeta\mathcal M^D+(1-\zeta)\mathcal M^A$, $C_{\rho\phi}=\zeta C^F+(1-\zeta)C^C$ (Eqs. 15–16) preserves $\tfrac12\rho\phi^2$ globally for any constant $\zeta$; the matrix proof needs skew-symmetry of the bracket of Eq. (19), which follows from skew-symmetry of the derivative matrix (§3.1–3.2, from Coppola et al. 2019). **Derived**
4. A spatially variable $\zeta(x)$ breaks the global proof of Eqs. (17)–(19) (§3.2). **Stated**
5. At second order the family is the flux form $\mathcal M=[\![m_{i+1/2}]\!]$, $C_{\rho\phi}=[\![\overline\phi\,m_{i+1/2}]\!]$, and $m_{i+1/2}$ is "the most general one-parameter symmetric bilinear approximation of the mass flux $\rho u$ over a two-point stencil" (Eqs. 23–25). **Derived**
6. The induced convective term of $\tfrac12\rho\phi^2$ is locally conservative with flux $\tfrac12\phi_i\phi_{i+1}m_{i+1/2}$ (Eqs. 26–27), a splitting of the quadruple product $\rho v\phi\phi$ (Eq. 28); Appendix A gives the high-order version (Eq. A.6). **Derived**
7. In flux form a face-wise weight $\zeta_i$ inside $m_{i+1/2}$ keeps local conservation of the linear invariants and of the generalized kinetic energy, adding degrees of freedom for adaptive optimization (§3.4). **Derived**
8. The induced-equation formula (Eq. 30) follows from the chain rule in time alone and holds discretely for exact time integration; applied to $\tfrac12\rho v_\alpha^2$ it shows that each component is preserved separately (Eq. 31) (§4.1). **Derived**
9. A locally conservative $\rho E$ discretization with KEP mass and momentum conserves $\rho e$ locally, $C_{\rho e}=[\![\mathcal F_{\rho E}-\tfrac12v_iv_{i+1}m_{i+1/2}]\!]$ (Eq. 35); with the KEP flux $\overline E\,m$ this is locally conservative but not KEP for $\rho e$ (Eq. 36) (§4.2.1). **Derived**
10. Conversely, a locally conservative $\rho e$ discretization induces a locally conservative $\rho E$ with flux $\mathcal F_{\rho e}+\tfrac12v_iv_{i+1}m_{i+1/2}$ (Eqs. 38–41); the induced pressure term is locally conservative when the derivative matrices satisfy $D_p=-D_v^\top$ (Eq. 42), Veldman's Requirement 3.2; a KEP $\rho e$ flux is Veldman's Requirement 3.3, sufficient but not necessary for total-energy conservation (§4.2.1). **Derived**
11. For exact time integration it does not matter which equation is discretized directly; only the discrete convective and pressure terms do (§4.2.1). **Derived**
12. The KEEP scheme of Kuya et al. (Eqs. 43–44) is, for exact time integration, the direct KGP discretization of the internal-energy equation, and is not strictly entropy-conservative (§4.2.1, §4.2.5). **Derived**
13. A necessary condition for pressure-equilibrium preservation (PEP) is $v\mathcal M=C_{\rho v}$ for constant $v$ (Eq. 47); every KEP formulation satisfies it, and Ranocha derived a similar condition for finite volumes (§4.2.2). **Derived**
14. The second PEP condition is $C_p+P_p=0$ for constant $v,p$ (Eq. 48); any direct discretization of the pressure equation satisfies it; a $\rho e$ discretization satisfies it when $C_{\rho e}$ blends only the divergence and $v$-advective forms (Eq. 51; Shima et al. use the blend $\tfrac12$), and such a splitting cannot be KEP for $\rho e$ (§4.2.2). **Derived**
15. For a $\rho E$ discretization PEP requires $C_{\rho E}-C_{\rho\kappa}+P_{\rho E}=0$ for constant $v,p$ (Eq. 54), met by splitting $C_{\rho E}$ into internal and kinetic parts and treating $\tfrac{\gamma}{\gamma-1}\partial_x(pv)$ with any combination of the forms of Eq. (32), as Singh & Chandrashekar do (§4.2.2). **Derived**
16. A locally conservative total-enthalpy discretization induces locally conservative $\rho E$ and $\rho e$ (Eqs. 61–62); from $\rho E$ the induced $\rho H$ flux is $\gamma\mathcal F_{\rho E}-(\gamma-1)\tfrac12v_iv_{i+1}m_{i+1/2}$ (Eq. 57) (§4.2.3). **Derived**
17. With $\rho e$ or $\rho E$ discretized directly the induced sound-speed convective term is in general not conservative (Eqs. 67–68); a KEP $\rho c$ discretization induces a locally conservative $\rho e$ with flux $\sqrt{e_ie_{i+1}}\,m_{i+1/2}$ and hence a locally conservative $\rho E$ (Eq. 71), as Kok observed with the Feiereisen splitting (§4.2.4). **Derived**
18. In none of the $\rho E$, $\rho e$, $p$, $\rho H$, $\rho c$ discretizations is entropy strictly conserved, since the terms $s\mathcal M$ and $c_v(C_{\rho e}+P_{\rho e})/e$ of Eqs. (73)–(74) are in general not flux differences; the approach is said to be "basically equivalent" to Tadmor's theory with $\eta=-\rho s$ (§4.2.5). **Stated**
19. With the Feiereisen form ($\zeta=1$) in mass, momentum and entropy, Eqs. (75)–(76) reduce to the inviscid Honein–Moin scheme (§4.2.5). **Derived**
20. Table 2: all $\rho E$, $\rho e$, $\rho c$ and $\rho H$ variants preserve $\rho E$, $\rho e$ and $\rho H$; only the $\rho c$ variants preserve $\rho c$; only the $\rho s$ variants preserve $\rho s$, and they preserve none of the others; only $(\rho E)_{\mathrm{PEP}}$, $(\rho e)_{\mathrm{PEP}}$ and $(\rho e)_{\mathrm{div}}$ are PEP. **Derived**
21. Isentropic vortex ($40\times40$, eighth order, CFL 0.01): every method preserves mass and momentum to machine precision; total energy is preserved except by the entropy schemes, among which KGP limits the spurious energy production best (Fig. 1). **Shown**
22. Same run, blow-up times: $(\rho E)$ about 19, $(\rho E)_{\mathrm{JP}}$ 29, $(\rho E)_{\mathrm{PEP}}$ 33; $(\rho H)_E$ 22, $(\rho H)$ 26, $(\rho H)_{H+\hat p}$ 31. The Jameson–Pirozzoli and PEP variants are more robust although at early times they produce more entropy than plain $(\rho E)$ (§5.1, Fig. 4). **Shown**
23. Robustness study ($30\times30$, fourth order, $t\le50$, Table 3): $(\rho e)$, $(\rho e)_{\mathrm{PEP}}$, $(\rho c)_{\mathrm{KGP}}$ and $(\rho s)_{\mathrm{KGP}}$ never diverge at CFL 0.01, 0.1, 0.5; every $\rho E$/$\rho H$ form diverges except $(\rho E)_{\mathrm{PEP}}$ and $(\rho H)_{H+\hat p}$ at CFL 0.5; larger CFL generally increases robustness, attributed to the slight dissipation of RK4 (§5.1). **Shown**
24. Inviscid Taylor–Green vortex ($32^3$, fourth order, RK4, CFL 0.1, $p_0=100$): the normalized total-energy error at $t=100$ is about $10^{-10}$ for $(\rho s)_{\mathrm{KGP}}$, $5\times10^{-8}$ for $(\rho s)_F$ and $3\times10^{-4}$ for $(\rho s)_C$; $(\rho c)_C$ and $(\rho c)_F$ diverge at $t\approx45$ and $46$ (§5.2, Fig. 6). **Shown**
25. In the Taylor–Green vortex $(\rho s)_C$ departs from exact entropy conservation, attributed to emulating the entropy equation through the total-energy equation (all these runs use $\rho E$ as primary variable) (§5.2, Fig. 8d). **Shown**
26. Temperature and density fluctuations grow in time for every $\rho E$ and $\rho H$ formulation and level off for $(\rho c)_{\mathrm{KGP}}$, $(\rho e)$, $(\rho e)_{\mathrm{PEP}}$, $(\rho s)_F$ and $(\rho s)_{\mathrm{KGP}}$, but not $(\rho s)_C$ (Fig. 10). **Shown**
27. At $M\approx0.3$ the Taylor–Green results match the $M\approx0.1$ case up to $t\approx70$, after which almost all runs show a possibly unbounded growth of fluctuations (§5.2, text only). **Shown**
28. A KEP treatment of the energy equation is "not necessarily the best option"; preserving $\rho\sqrt e\propto\rho c$ gives similar robustness, and internal-energy and entropy formulations with KGP are the most robust (§4.2, §6). **Shown**

# Printed slips

- §3.1: "The cases ξ = 0 and ξ = 1 give the classical Feiereisen form and the newly derived form described in [6]"; by Eqs. (15)–(16) $\xi=1$ gives the Feiereisen form and $\xi=0$ the form of [6], as §4.2.5 ("Feiereisen form (ξ = 1)") and the Table 2 caption ($m_F=\overline{\rho u}$) confirm. The sentence lists the values in reverse order.
- §3.3: "$(\hat F_{i+1/2}-\hat F_{i+1/2})/h$"; the second index should be $i-1/2$.
- Eq. (33): the divergence-form pressure term is printed $\chi\,\delta\rho u_\alpha/\delta x_\alpha$ instead of $\chi\,\delta pu_\alpha/\delta x_\alpha$ (cf. Eq. 32), and the quoted flux $\chi\,\overline p\,\overline u$ is not that of the divergence form, whose second-order flux is $\overline{pu}$ as Table 2 uses for $(\rho E)$.
- §4.2.5: "$G(\rho,e)=c_v\ln(p/\rho^\gamma)$" is $s$, while the derivatives quoted, $G_\rho=s+c_v(1-\gamma)$ and $G_e=c_v\rho/e$, are those of $\rho s$; Eq. (72) is consistent with $G=\rho s$.
- Eqs. (56), (59): "$u_\alpha P_{u_\alpha}$" for $u_\alpha P_{\rho u_\alpha}$ (Eqs. 37, 39, 63).
- Figs. 4 and 9 captions "(d)-(e)" for panels (d)–(f); Table 2 row label "$(\rho H)_{H+p}$" without the hat of the text.
- §5.1: "$\Delta t=1.8\times10^{-4}$" at CFL 0.01 with $h=1/40$; with $c_\infty=1/M_\infty=2$ the convective definition $\mathrm{CFL}\,h/(\lvert u\rvert+c)$ gives $8.3\times10^{-5}$ and $\mathrm{CFL}\,h/u_\infty$ gives $2.5\times10^{-4}$. The paper does not define its CFL number, so the printed step cannot be reproduced. *(compiler check, not in the sources.)*
- §5.1: "$T_\infty=720M_vr_v$" ($=24$ with the printed values *(compiler check, not in the sources)*), not used elsewhere and not consistent with the normalization $p=\rho^\gamma/(\gamma M_\infty^2)$.
- Typos: "Eight-order" (Figs. 2–3), "incresed", "larger that", "did non change".

# Notation map

| De Michele & Coppola (2023a) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u_\alpha$ | $v$ (components $v_\alpha$) | velocity |
| $h$ | $\Delta x$ | uniform mesh width |
| $\delta/\delta x$ | kept | central explicit derivative $\sum_ka_k(\phi_{i+k}-\phi_{i-k})/h$ |
| $\xi$ | $\zeta$ (page-local, as on [split convective forms](/methods/split-convective-forms.md)) | blending weight of the KEP family; **$\xi$ is a DG node in the registry** |
| $\chi$ | $\chi$ (page-local) | blend of divergence and advective pressure forms |
| $\kappa$, $\rho\kappa$ ($\rho k$ in tables) | $\kappa=\tfrac12\rho\lvert v\rvert^2$ | **the source's $\kappa$ is per unit mass, the registry's per unit volume** |
| $\rho s=\rho c_v\ln(p/\rho^\gamma)$ | $\rho\,c_vs$ | the registry's $s$ omits $c_v$; the source's mathematical entropy $-\rho c_vs$ is $c_v(\gamma-1)=R$ times the registry's $\eta=-\rho s/(\gamma-1)$ *(compiler check, not in the sources)* |
| $\mathcal M$, $C_{\rho\phi}$, $P_{\rho\phi}$, $R_{\rho\phi}$ | kept, page-local | convective term of mass, convective, pressure and total terms of the $\rho\phi$ equation |
| $\overline\phi$, $\overline{\overline{(\rho,u)}}$ | $\overline\phi$, $\tfrac12(\rho_iv_{i+1}+\rho_{i+1}v_i)$ | two-point means |
| $m_{i+1/2}$ | $m_{i+1/2}$ | face mass flux |
| $[\![\cdot]\!]$ | flux difference, page-local | **the registry's $[\![a]\!]$ is an interface jump** |
| $\hat p=p/\rho$ | kept | Jameson–Pirozzoli form |
| $D$, $D_p$, $D_u$ | kept | derivative matrices; **$D$ is the DG differentiation matrix in the registry** |
| $M_v$, $r_v$, $M_\infty$ | kept | vortex Mach number, core radius, free-stream Mach number |

# Reference list

42 printed references in numbered style ([1]–[42]), merged complete into the
[bibliography](/bibliography.md) with `citedby` `demichele-2023`. Two items are
printed in pre-publication form and kept as their own entries: ref. [7]
(Coppola & Veldman, "submitted", arXiv 2208.14067, the preprint of the
ingested [Coppola & Veldman (2023)](/sources/coppola-2023.md)) and ref. [39]
(Singh & Chandrashekar, arXiv:2104.14941). Ref. [18] is the ingested
[Edoh (2022)](/sources/edoh-2022.md). Ref. [5] prints a truncated author "N. J.",
[19] the issue number 179 in the volume field, [27] "Kravhcenko"; all are
kept as printed. No printed duplicates were found.

# Pages created or updated

Chunk 5 (2026-10-22), cited further in chunks 6–12 (2026-10-23/30). This source is cited on:

* [Entropy stability](/properties/entropy-stability.md)
* [Entropy-conservative and kinetic-energy-preserving two-point fluxes](/methods/entropy-conservative-flux.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Kinetic energy preservation](/properties/kinetic-energy-preservation.md)
* [Pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)
* [Split convective forms](/methods/split-convective-forms.md)
* [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
