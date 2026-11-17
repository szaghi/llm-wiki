---
type: Source
title: "Shima et al. (2021) — Preventing spurious pressure oscillations in split convective form discretization for compressible flows"
description: "Short note deriving the discrete pressure and velocity equations induced by the second-order KEP and KEEP split-form central schemes, showing that neither preserves pressure equilibrium, and proposing KEEP-PE, whose internal-energy flux {{ρe}}{{v}} does; tested on a density wave, the inviscid Taylor–Green vortex and a supersonic turbulent boundary layer without numerical dissipation."
resource: "doi:10.1016/j.jcp.2020.110060"
source_kind: paper
authors: [Shima N., Kuya Y., Tamaki Y., Kawai S.]
year: 2021
venue: "J. Comput. Phys. 427:110060"
local_file: "/home/stefano/papers/mosaic/weno-teno/2021_Crossref_Journal_of_Computational_Physics_Shima_Preventing_spurious_pressure_oscillations_in_split_convectiv.pdf"
tags: [kinetic-energy-preserving, central-scheme, finite-difference, turbulence, low-dissipation]
timestamp: 2026-11-17T08:43:12Z
---

# Summary

Shima, Kuya, Tamaki & Kawai examine whether the
[split convective forms](/methods/split-convective-forms.md) used in
non-dissipative central schemes for compressible turbulence keep the
[pressure equilibrium](/properties/pressure-equilibrium-preservation.md) of
the Euler equations: uniform velocity and pressure with an arbitrary density
stay uniform. They write the second-order face fluxes of the KEEP
(kinetic energy and entropy preserving) scheme of Kuya et al. and of the KEP
scheme of Jameson and Pirozzoli, and derive the discrete pressure and
velocity equations that these fluxes induce. The KEEP pressure-work flux
obeys a discrete product rule, so the KEEP energy equation splits into an
induced kinetic-energy equation and an internal-energy equation whose flux
is the cubic split $\{\!\{\rho\}\!\}\{\!\{e\}\!\}\{\!\{v\}\!\}$. With
$\rho e=p/(\gamma-1)$ this flux gives a nonzero pressure rate at
equilibrium; the KEP enthalpy flux contains the same term. Both schemes keep
velocity equilibrium only as long as the pressure stays uniform.

The proposed **KEEP-PE** scheme keeps every KEEP flux except the
internal-energy one, which becomes
$\{\!\{\rho e\}\!\}\{\!\{v\}\!\}=\{\!\{p\}\!\}\{\!\{v\}\!\}/(\gamma-1)$, and
the induced pressure rate vanishes identically at equilibrium
([KEEP and KEEP-PE schemes](/methods/keep-scheme.md)). On an inviscid
[density wave](/benchmarks/density-wave-advection.md) KEEP-PE keeps $v$ and
$p$ uniform while KEEP and KEP oscillate and diverge. On the inviscid
compressible [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) KEP
blows up, while KEEP and KEEP-PE run to the end with KEEP-PE losing slightly
more entropy. A DNS of a
[supersonic turbulent boundary layer](/benchmarks/supersonic-turbulent-boundary-layer.md)
with KEEP-PE and no numerical dissipation agrees with a filtered
compact-scheme DNS. The flux set reappears in DG as the "Shima et al. flux"
of [Ranocha et al. (2023)](/sources/ranocha-2023.md)
([entropy-conservative two-point fluxes](/methods/entropy-conservative-flux.md)).

# Version read

Version of record (Elsevier typeset, article type "Short note"), J. Comput.
Phys. 427:110060, 10 pages, all read. `pdftotext` garbles the stacked
fractions of Eqs. (8)–(23) and Tables 1–2, so pages 3–9 were read from
page renders (130–170 dpi); every equation and table entry below was read
from the images. Received 16 March 2020, revised 5 November 2020, accepted
5 December 2020, available online 11 December 2020. Page 1 matches the
bibliography entry and its DOI. No identity problem. Bundle label: Shima et
al. (2021).

# Key claims

Registry notation, with node $i$ and face $i+1/2$ for the paper's $m$ and
$m\pm\tfrac12$, velocity $v$ for the paper's $u$, $\{\!\{a\}\!\}=\tfrac12(a_i+a_{i+1})$
at face $i+1/2$, the page-local product mean
$(\!(a;b)\!)=\tfrac12(a_ib_{i+1}+a_{i+1}b_i)$ (as on
[entropy-conservative two-point fluxes](/methods/entropy-conservative-flux.md))
and page-local face fluxes $f_\rho$ (mass), $f_{\rho v}$ (momentum),
$f_{\rho e}$ (internal-energy part of the energy flux). Everything is second
order, central and on a uniform grid.

1. Continuum: the internal-energy equation $\partial_t(\rho e)+\partial_x(\rho ev)+p\,\partial_xv=0$ with $\rho e=p/(\gamma-1)$ gives the pressure equation $\partial_tp=-\partial_x(pv)-(\gamma-1)p\,\partial_xv$ (Eqs. (3)–(4), after Karni), and momentum minus $v$ times mass gives $\partial_tv=-\tfrac1\rho\big(\partial_x(\rho vv)+\partial_xp-v\,\partial_x(\rho v)\big)$ (Eq. (5)). For $v\equiv v_0$, $p\equiv p_0$ and any $\rho_0(x)$ both rates vanish (Eqs. (6)–(7)). Velocity and pressure equilibrium are coupled: disturbing one disturbs the other (§2.1.2). **Derived**
2. KEEP discretizes the total-energy equation in the form $\partial_tE+\partial_x(\rho\tfrac12\lvert v\rvert^2v)+\partial_x(\rho ev)+\partial_x(vp)=0$ (Eq. (1)), KEP in the enthalpy form (Eq. (2)). Mass, momentum and total energy are conserved exactly by construction; both schemes preserve the total kinetic energy in the incompressible limit; KEEP conserves the total entropy only approximately, "not strictly preserved at the discrete level" (§2.1.1). **Stated**
3. Face fluxes (Table 1): mass $f_\rho=\{\!\{\rho\}\!\}\{\!\{v\}\!\}$ and momentum $f_{\rho v}=f_\rho\{\!\{v\}\!\}+\{\!\{p\}\!\}$ for both schemes. KEEP: kinetic $f_\rho\tfrac12v_iv_{i+1}$, internal $\{\!\{\rho\}\!\}\{\!\{e\}\!\}\{\!\{v\}\!\}$, pressure work $(\!(p;v)\!)$. KEP: kinetic $f_\rho\{\!\{\tfrac12v^2\}\!\}$ and enthalpy $\{\!\{\rho\}\!\}\{\!\{e+p/\rho\}\!\}\{\!\{v\}\!\}$ (§2.2.1, Eqs. (8)–(11)). **Stated** (recalled from refs. [1]–[4])
4. Because the KEEP pressure-work flux satisfies the discrete product rule (credited to Kuya et al. [3]), the KEEP energy equation is the sum of the kinetic-energy equation induced by mass and momentum, with pressure term $v_i(p_{i+1}-p_{i-1})/(2\Delta x)$, and the internal-energy equation $\frac{d}{dt}(\rho e)_i+\big((f_{\rho e})_{i+1/2}-(f_{\rho e})_{i-1/2}\big)/\Delta x+p_i(v_{i+1}-v_{i-1})/(2\Delta x)=0$ (§2.2.2, Eqs. (12)–(13)). **Derived** *(Compiler check, not in the sources: $(\!(p;v)\!)_{i+1/2}-(\!(p;v)\!)_{i-1/2}=\tfrac12p_i(v_{i+1}-v_{i-1})+\tfrac12v_i(p_{i+1}-p_{i-1})$ is exact algebra.)*
5. With the KEEP internal-energy flux, at $v\equiv v_0$, $p\equiv p_0$ the induced pressure rate is $\frac{dp_i}{dt}=-\frac{v_0p_0}2\Big[\frac1{\rho_i}\frac{\rho_{i+1}-\rho_{i-1}}{2\Delta x}+\rho_i\frac{\rho_{i+1}^{-1}-\rho_{i-1}^{-1}}{2\Delta x}\Big]\ne0$ (Eqs. (14)–(15)), so KEEP cannot keep pressure equilibrium. **Derived** *(Compiler check, not in the sources: the bracket factors as $\frac{dp_i}{dt}=-\frac{v_0p_0(\rho_{i+1}-\rho_{i-1})(\rho_{i+1}\rho_{i-1}-\rho_i^2)}{4\Delta x\,\rho_{i-1}\rho_i\rho_{i+1}}=-\tfrac12v_0p_0\Delta x^2(\ln\rho)'(\ln\rho)''+O(\Delta x^4)$, checked symbolically together with its equality to the conservative KEEP right-hand side; the error is second order and vanishes where $\ln\rho$ is locally linear on the grid, so "$\ne0$" holds for generic, not every, density.)*
6. The KEP enthalpy flux decomposes as $\{\!\{\rho\}\!\}\{\!\{e\}\!\}\{\!\{v\}\!\}+\{\!\{\rho\}\!\}\{\!\{p/\rho\}\!\}\{\!\{v\}\!\}$ (Eq. (16)); its first part is the KEEP internal-energy flux, and its pressure part "cannot be decomposed" into pressure work and pressure dilatation by the discrete product rule, so KEP is not pressure-equilibrium preserving either. "The existing linear schemes based on the split convective forms, such as used in the KEP and KEEP schemes, do not maintain the pressure equilibrium even in smooth flow regions" (§2.2.2). **Derived** (for the forms analysed)
7. KEEP-PE: the internal-energy flux $f_{\rho e}=\{\!\{\rho e\}\!\}\{\!\{v\}\!\}=\{\!\{p\}\!\}\{\!\{v\}\!\}/(\gamma-1)$ (Eq. (17)), all other fluxes as in KEEP (Table 2). The induced pressure equation (Eq. (18)) gives $dp_i/dt=0$ at $v_0$, $p_0$ (Eq. (19)). "The whole idea ... is not to split the internal energy ($\rho e$)", so that it reduces to $p$ (§2.2.3). **Derived**
8. Pointwise form of the KEEP-PE internal-energy term: $\partial_x(\rho ev)\simeq\tfrac12\big(\delta(\rho ev)/\delta x+v\,\delta(\rho e)/\delta x+\rho e\,\delta v/\delta x\big)$, $\delta$ a discrete derivative (Eq. (20)). **Stated**
9. KEEP-PE and KEEP satisfy Kuya et al.'s three "analytical relations" for the exchange between kinetic and internal energy; KEP is "inconsistent" with them and preserves entropy worse. The changed internal-energy flux "may affect the entropy preservation property" (§2.2.3). **Stated**
10. KEEP-PE, KEEP and KEP share mass, momentum and pressure-gradient fluxes, so the induced velocity equation (Eqs. (21)–(22)) vanishes for all three at $v_0$, $p_0$ (Eq. (23)). KEEP and KEP lose velocity equilibrium through their pressure error, via the pressure-gradient term (§2.2.4). **Derived**
11. A high-order extension of KEEP-PE "can be straightforward" following Kuya & Kawai's high-order KEEP on curvilinear grids (ref. [14]); it is not built (§2.2.1). **Stated**
12. Time integration for §3: classical four-stage RK4 at CFL ≈ 0.1, chosen as temporally converged (CFL 0.1 and 0.01 give "almost the same" results); KEEP-PE also runs stably at CFL ≈ 1, whose results "differ from the temporally converged results" and are not shown (§3). **Stated**
13. Density wave: $(\rho_0,v_0,p_0)=(2+\sin2\pi x,\,1,\,1)$ on $[0,1]$, periodic, 41 points ($\Delta x=0.025$), $\gamma=1.4$. At $t=11$ KEEP-PE keeps $v$ and $p$ uniform with no numerical dissipation; KEEP shows small and KEP large oscillations of $p$, $v$ and $\rho$, growing in time, and the runs diverge at $t\approx12.9$ (KEEP) and $t\approx11.1$ (KEP). Because of the second-order spatial accuracy, the computed density wave shows "slight dispersion (phase) errors" (§3.1, Fig. 1). **Shown** *(Compiler check, not in the sources: a rerun of this setup (41 points with both periodic ends, 40 unknowns) with RK4 at CFL 0.1 diverges at $t=12.89$ (KEEP) and $t=11.16$ (KEP), and KEEP-PE keeps $\max\lvert p-1\rvert\approx4\times10^{-14}$ to $t=20$.)*
14. Inviscid compressible Taylor–Green vortex: $\rho=1$, $v_1=M_0\sin x\cos y\cos z$, $v_2=-M_0\cos x\sin y\cos z$, $v_3=0$, $p=1/\gamma+(\rho_0M_0^2/16)(\cos2x+\cos2y)(\cos2z+2)$, $M_0=0.4$, periodic $[0,2\pi]^3$ with $65^3$ points, time $\hat t=M_0t$ to 160. KEEP and KEEP-PE preserve total kinetic energy and total entropy "well" and run to $\hat t=160$ without dissipation, also at $\Delta x=2\pi/32$; KEEP-PE "slightly increases the total kinetic energy and also decreases the total entropy compared to the KEEP scheme". KEP shows a "non-physical rapid decrease in the entropy" and blows up at $\hat t\approx120$. The kinetic-energy drop near $\hat t\approx20$ is physical pressure work (§3.2, Fig. 2). Read from Fig. 2b: the normalized entropy change of KEEP-PE reaches about $-5\times10^{-3}$ at $\hat t=160$, KEEP's stays near zero. The detailed entropy analysis is "in progress". **Shown**
15. Supersonic turbulent boundary layer DNS, nominally zero pressure gradient: $M_\infty=2.28$, $\mathrm{Re}_\tau\approx480$ at $x=12.5\delta_{\mathrm{in}}$; domain $15.6\delta_{\mathrm{in}}\times10.4\delta_{\mathrm{in}}\times6.2\delta_{\mathrm{in}}$ with $601\times491\times182$ points; $\Delta x^+\approx10$, $\Delta z^+\approx5$, $\Delta y^+_{\mathrm{wall}}\approx0.8$, $\Delta y^+\approx9$ in the uniform region $y/\delta_{\mathrm{in}}\approx0.5$–$6.2$; adiabatic no-slip wall, spanwise periodic, rescaling–reintroducing inflow (Urbin & Knight), third-order TVD Runge–Kutta at CFL ≈ 0.6. KEEP-PE without numerical dissipation agrees with a sixth-order compact DNS with eighth-order filtering for the van Driest mean velocity, Reynolds stresses and turbulent-kinetic-energy budget, and reproduces near-wall streaks (Appendix, Fig. 3). **Shown**
16. Abstract and Conclusions: KEEP-PE shows "a superior numerical stability property without spurious pressure oscillations"; its entropy decrease relative to KEEP is "much smaller than that of the existing KEP scheme" (§4). **Stated** (the density wave is the only test in which KEEP-PE outlives KEEP)
17. Literature recalled (§1): Godunov-type finite volumes induce spurious oscillations at single-component contacts (Clerc); component-wise WENO induces velocity and pressure oscillations (Johnsen 2011); point-wise flux vector splitting such as Steger–Warming induces them while global Lax–Friedrichs splitting "may prevent" them (He et al. 2015); the authors know of no prior study of the pressure equilibrium of split convective forms. **Stated**

# Printed slips

- Eq. (16): the second underbrace is labelled $\tilde P_j$, the symbol Table 1 uses for the KEEP pressure-work flux $(\!(p;v)\!)$; the braced term is $\{\!\{\rho\}\!\}\{\!\{p/\rho\}\!\}\{\!\{v\}\!\}$, a different flux, as the text itself says. The symbol is overloaded.
- Eq. (15), "$\ne0$": holds for a generic density, not for every density; the rate vanishes where $\rho_{i+1}=\rho_{i-1}$ or the density is locally geometric (claim 5).
- Eq. (21): the $u$ multiplying the mass-flux difference carries no node index; Eq. (22) has $u|_{(m)}$.
- Appendix: $\Delta x^+\approx10$ and $\Delta z^+\approx5$ on uniform streamwise and spanwise grids are not consistent with the printed domain and point counts: $15.6\delta_{\mathrm{in}}/600\approx0.026\delta_{\mathrm{in}}$ and $6.2\delta_{\mathrm{in}}/182\approx0.034\delta_{\mathrm{in}}$ give $\Delta z/\Delta x\approx1.3$, so $\Delta x^+\approx10$ implies $\Delta z^+\approx13$ *(compiler check, not in the sources; assumes one $u_\tau/\nu$)*. Which number is off cannot be decided from the paper.
- Fig. 2b: the diagnostic $\Delta(\rho s)=-(\rho s-\rho_0s_0)$ is divided by $\rho_0s_0=\ln(1/1.4)<0$, so the two sign flips cancel and a falling curve is a loss of entropy, as the text says; "total" (domain integral) is meant though the formula is written pointwise.
- Headings of §2.2.3 and §2.2.4 typeset KEEP$_{\mathrm{PE}}$ as italic math letters; roman elsewhere.
- Reference list: [13] prints the title "Hybrid multifluid algolithms" (algorithms); [4] has no volume (Comput. Fluids 200:104427); [14] is printed as submitted to J. Comput. Phys. (2020); [8] prints "Consistent numerical diffusion terms", while the bibliography entry from another citing source has "term".

# Notation map

| Shima et al. (2021) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $m$, $m\pm\tfrac12$ | $i$, $i\pm1/2$ | node and face index |
| $u$, $u_i$, $u_j$ | $v$, $v_d$ | velocity |
| $k=u_iu_i/2$, $\rho k$ | $\tfrac12\lvert v\rvert^2$, $\kappa$ | registry $\kappa$ is per unit volume |
| $e$, $\rho e$, $E=\rho e+\rho k$ | $e$, $\rho e$, $E$ | |
| $h=e+p/\rho$ | $e+p/\rho$ | written out: $h$ is the two-point flux in the registry |
| $s=\log(p\rho^{-\gamma})$ | $s=\ln(p\rho^{-\gamma})$ | |
| $\frac{a\vert_{(m\pm1)}+a\vert_{(m)}}2$ | $\{\!\{a\}\!\}$ | arithmetic mean at the face |
| $\frac{u_j\vert_{(m\pm1)}p\vert_{(m)}+u_j\vert_{(m)}p\vert_{(m\pm1)}}2$ | $(\!(p;v)\!)$ | product mean, page-local |
| $\frac{u_i\vert_{(m\pm1)}u_i\vert_{(m)}}2$ | $\tfrac12v_iv_{i+1}$ | |
| $\tilde C_j$ | $f_\rho$ | mass flux, page-local |
| $\tilde M_{ij}$, $\tilde\Pi$ | $f_\rho\{\!\{v\}\!\}$, $\{\!\{p\}\!\}$ | convective and pressure parts of $f_{\rho v}$ |
| $\tilde K_j$, $\tilde I_j$, $\tilde P_j$, $\tilde H_j$ | kinetic, internal ($f_{\rho e}$), pressure-work and enthalpy parts of the energy flux | page-local names |
| $\delta/\delta x_j$ | $\delta/\delta x$ | discrete derivative, page-local |
| $M_0$, $\hat t=M_0t$ | page-local | Taylor–Green vortex |
| $\Delta(\rho s)$ | page-local | entropy diagnostic of Fig. 2b |
| KEEP$_{\mathrm{PE}}$ | KEEP-PE | wiki spelling |
| $M_\infty$, $\mathrm{Re}_\tau$, $\delta_{\mathrm{in}}$, $y^+$ | same, page-local | boundary-layer appendix |

# Reference list

The paper prints 17 references, numbered [1]–[17] in order of first
citation, without DOIs. The list is merged complete into the
[bibliography](/bibliography.md), with `citedby` including `shima-2021`.
Fourteen reuse existing entries. [2] is
[Pirozzoli (2010)](/sources/pirozzoli-2010.md) and [15] is
[Pirozzoli (2011b)](/sources/pirozzoli-2011-b.md). [3] (Kuya, Totani &
Kawai 2018) and [4] (Kuya & Kawai, Comput. Fluids 2020) define the KEEP
scheme. [14] (Kuya & Kawai, high-order KEEP on curvilinear grids) is printed
"submitted for publication" and is kept as its own entry `kuya-2020-b`,
apart from the published `kuya-2021`, under the bundle's preprint rule. New
entries: `clerc-1999`, `kuya-2020-b`, `urbin-2001`. No item is unparseable.

# Pages created or updated

Chunk 14 (2026-11-17). This source is cited on:

* [APEC flux for approximate pressure equilibrium](/methods/apec-scheme.md)
* [Compact low-pass filter](/methods/compact-low-pass-filter.md)
* [Density-wave advection](/benchmarks/density-wave-advection.md)
* [Discontinuous Galerkin spectral element method (DGSEM)](/methods/dgsem.md)
* [Entropy stability](/properties/entropy-stability.md)
* [Entropy-conservative and kinetic-energy-preserving two-point fluxes](/methods/entropy-conservative-flux.md)
* [Flux differencing and split-form DG](/methods/flux-differencing.md)
* [KEEP and KEEP-PE schemes](/methods/keep-scheme.md)
* [Kinetic energy preservation](/properties/kinetic-energy-preservation.md)
* [Multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)
* [Pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)
* [Split convective forms](/methods/split-convective-forms.md)
* [Subcell finite-volume limiting for DG](/methods/subcell-finite-volume-limiting.md)
* [Supersonic turbulent boundary layer](/benchmarks/supersonic-turbulent-boundary-layer.md)
* [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
