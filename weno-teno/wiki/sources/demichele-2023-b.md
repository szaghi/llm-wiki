---
type: Source
title: "De Michele & Coppola (2023) — Asymptotically entropy-conservative and kinetic-energy preserving numerical fluxes for compressible Euler equations"
description: "Short note deriving purely algebraic two-point fluxes for the Euler equations that preserve kinetic energy and pressure equilibrium and approach entropy conservation as a truncation order grows (AEC fluxes), by expanding the logarithmic means of Ranocha's flux; tested on a density wave and the inviscid Taylor–Green vortex."
resource: "doi:10.1016/j.jcp.2023.112439"
source_kind: paper
authors: [De Michele C., Coppola G.]
year: 2023
venue: "J. Comput. Phys. 492:112439"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Journal_of_Computational_Physics_De_Asymptotically_entropy-conservative_and_kinetic-energy_prese.pdf"
tags: [entropy-stable, kinetic-energy-preserving, numerical-flux, central-scheme, finite-difference]
timestamp: 2026-10-23T23:00:00Z
---

# Summary

De Michele & Coppola (2023b) look for two-point fluxes for the convective
terms of the compressible Euler equations that use only algebraic
operations and are at once
[kinetic-energy preserving](/properties/kinetic-energy-preservation.md) (KEP),
[pressure-equilibrium preserving](/properties/pressure-equilibrium-preservation.md)
(PEP) and *asymptotically entropy conservative* (AEC). AEC means that the
entropy production of the spatial discretization can be made as small as
wanted by adding terms of an expansion. The starting point is Ranocha's KEP,
entropy-conservative and PEP flux, rewritten as mass, momentum and
internal-energy fluxes. Its only non-algebraic ingredients are the
[logarithmic mean](/operators/logarithmic-mean.md) of $\rho$ in the mass flux
and the reciprocal of the logarithmic mean of $1/e$ in the internal-energy
flux. The mean inequalities (geometric $\le$ logarithmic $\le$ arithmetic,
hence harmonic $\le1/\{\!\{1/e\}\!\}_{\log}\le$ geometric) lead the authors to
take the harmonic or geometric mean of $e$, not the arithmetic one, as the
algebraic surrogate. This gives the new Aρ-He flux (arithmetic $\rho$,
harmonic $e$) and a fully geometric variant Gρ-Ge.

A series of $[\![\ln\phi]\!]$ in the normalized jump
$\mathsf j_\phi=[\![\phi]\!]/(2\{\!\{\phi\}\!\})$, truncated at order $N_{\mathrm T}$
in both logarithmic means, gives the AEC($N_{\mathrm T}$) hierarchy.
$N_{\mathrm T}=0$ is Aρ-He and $N_{\mathrm T}\to\infty$ is Ranocha's flux.
Every member is PEP when the same $N_{\mathrm T}$ is used for $\rho$ and $e$.
The KEEP($N_{\mathrm T}$) expansion of Tamaki et al. expands differently and
loses PEP. The paper belongs with the
[entropy-conservative two-point fluxes](/methods/entropy-conservative-flux.md).
An appendix extends the two-point fluxes to high order by the
[flux-differencing](/methods/flux-differencing.md) formula.

The tests are a 1D [density wave](/benchmarks/density-wave-advection.md) and
the inviscid [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) on
$32^3$ points with 4th- and 6th-order fluxes. The density wave is run at 61
points with RK4 at CFL 0.01. Aρ-Ae, which is not PEP, diverges near $t=22$.
Aρ-He and Gρ-Ge stay stable up to $t=100$. AEC(1) and KEEP(1) have the
smallest entropy error, and KEEP(1) alone shows spurious pressure
oscillations of order $10^{-7}$. The schemes are non-dissipative and
central, with no shock capturing.

# Version read

arXiv:2307.10918v2 [physics.flu-dyn], stamped 25 Aug 2023, header "A
Preprint" dated August 28, 2023: not the journal's typeset version of
record. 9 pages, a short note in six sections plus Appendix A. The file
prints no DOI or journal reference. The published identity comes from
Crossref (J. Comput. Phys. 492:112439, 2023); title and authors match page
1. Equation, section and figure numbers are those of arXiv v2.

# Key claims

Registry notation: $\{\!\{\cdot\}\!\}$, $\{\!\{\cdot\}\!\}_{\log}$ and $[\![\cdot]\!]$
are the two-point arithmetic and logarithmic means and the jump between
nodes $i$ and $i+1$; $v$ is the velocity, $e$ the specific internal energy.
Page-local symbols: $\{\!\{\phi\}\!\}_{\mathrm G}=\sqrt{\phi_i\phi_{i+1}}$ and
$\{\!\{\phi\}\!\}_{\mathrm H}=\phi_i\phi_{i+1}/\{\!\{\phi\}\!\}$ (geometric and
harmonic means), $((\phi;\psi))=(\phi_i\psi_{i+1}+\phi_{i+1}\psi_i)/2$ (product
mean), $\mathsf j_\phi=[\![\phi]\!]/(2\{\!\{\phi\}\!\})$, the truncation order
$N_{\mathrm T}$, and $f_\rho$, $f_{\rho v}$, $f_E$,
$f_{\rho e}$ for the mass, momentum, total-energy and
convective internal-energy components of the two-point flux.

1. Ranocha's flux [11] (Eq. 1) is KEP, entropy-conservative and PEP. Its internal-energy form (Eq. 2) is equivalent to the total-energy form under exact time integration, because the pressure term $((p;v))$ corresponds to a central discretization of the advective form $p\partial_xv+v\partial_xp$ (§2, Eqs. 1–2). **Stated**
2. A second-order two-point flux is KEP if and only if the momentum convective flux is the mass flux times the arithmetic mean of the velocity, $f_{\rho v}=f_\rho\{\!\{v\}\!\}$, also on non-uniform or non-Cartesian meshes [3]. The induced kinetic-energy flux is $f_\rho v_iv_{i+1}/2$ [4] (§2). **Stated**
3. The flux with the arithmetic mean of $e$ (Eq. 3) discretizes the internal-energy equation with a full "triple" splitting of $\partial_x(\rho ve)$. Under exact time integration it is equivalent to Kuya et al.'s KEEP scheme [13] and to KGP($\rho e$) [2] (§2, §5). **Stated**
4. The flux with the geometric mean of $e$ (Eq. 4) can be read as a KEP discretization of the equation for $\rho\sqrt e$, whose induced $\rho e$ equation has a conservative convective term with a flux analogous to the kinetic-energy flux; it is inspired by Kok's sound-speed equation [16]. Eqs. 3 and 4 are "dual": Eq. 3 makes the induced equation for $\rho e^2$ conservative, Eq. 4 the balance of $\rho\sqrt e$ (§2). **Derived**
5. For positive $\phi$, $\{\!\{\phi\}\!\}_{\mathrm G}\le\{\!\{\phi\}\!\}_{\log}\le\{\!\{\phi\}\!\}$, strictly when $\phi_i\neq\phi_{i+1}$ (Eq. 5, citing Carlson [17]). **Stated**
6. $\{\!\{\phi\}\!\}_{\mathrm G}=\{\!\{\phi\}\!\}(1-\mathsf j_\phi^2)^{1/2}$ (Eq. 6) and $\{\!\{\phi\}\!\}_{\mathrm H}=\{\!\{\phi\}\!\}_{\mathrm G}(1-\mathsf j_\phi^2)^{1/2}$ (Eq. 8). **Derived**. Both follow from $\phi_i\phi_{i+1}=\{\!\{\phi\}\!\}^2-[\![\phi]\!]^2/4$ and $\{\!\{\phi\}\!\}_{\mathrm H}=\{\!\{\phi\}\!\}_{\mathrm G}^2/\{\!\{\phi\}\!\}$ *(compiler check, not in the sources)*.
7. Applying Eq. 5 to $1/\phi$ gives $\{\!\{\phi\}\!\}_{\mathrm H}\le1/\{\!\{1/\phi\}\!\}_{\log}\le\{\!\{\phi\}\!\}_{\mathrm G}$ (Eq. 7). Hence the harmonic or geometric mean approximates the internal-energy average more legitimately than the arithmetic mean, which Eq. 5 justifies only for $\rho$ (§3). **Derived**
8. The flux with geometric means for both $\rho$ and $e$ (Eq. 9, consistent with Rozema et al. [18]) is PEP and shows "remarkably good" entropy conservation in the tests (§3, §4, §5). **Derived** (PEP) and **Shown** (entropy). With $\rho_ie_i=p_0/(\gamma-1)$ at every node, $\{\!\{\rho\}\!\}_{\mathrm G}\{\!\{e\}\!\}_{\mathrm G}=\sqrt{\rho_ie_i\rho_{i+1}e_{i+1}}=p_0/(\gamma-1)$, while for the arithmetic-$\rho$, geometric-$e$ flux of Eq. 4, $\{\!\{\rho\}\!\}\{\!\{e\}\!\}_{\mathrm G}=\frac{p_0}{\gamma-1}\{\!\{\rho\}\!\}/\{\!\{\rho\}\!\}_{\mathrm G}$ is not constant *(compiler check, not in the sources)*.
9. The exact series $[\![\ln\phi]\!]=\frac{[\![\phi]\!]}{\{\!\{\phi\}\!\}}\sum_{n=0}^{\infty}\frac{\mathsf j_\phi^{2n}}{2n+1}$ holds with $\lvert\mathsf j_\phi\rvert<1$ for positive $\phi$ (Eqs. 11–12). **Derived**
10. Truncating the series at $N_{\mathrm T}$ in both logarithmic means gives the AEC($N_{\mathrm T}$) family (Eq. 13): $f_\rho=\{\!\{\rho\}\!\}\{\!\{v\}\!\}\big(\sum_{n=0}^{N_{\mathrm T}}\frac{\mathsf j_\rho^{2n}}{2n+1}\big)^{-1}$, $f_{\rho v}=f_\rho\{\!\{v\}\!\}$, $f_{\rho e}=f_\rho\{\!\{e\}\!\}_{\mathrm H}\sum_{n=0}^{N_{\mathrm T}}\frac{\mathsf j_e^{2n}}{2n+1}$. $N_{\mathrm T}=0$ is Eq. 10 (Aρ-He), $N_{\mathrm T}\to\infty$ is Ranocha's flux; all members are algebraic (§4). **Derived**. $1/\{\!\{1/e\}\!\}_{\log}=-[\![\ln e]\!]/[\![1/e]\!]=\frac{e_ie_{i+1}}{[\![e]\!]}[\![\ln e]\!]=\{\!\{e\}\!\}_{\mathrm H}\sum_n\frac{\mathsf j_e^{2n}}{2n+1}$, consistent with Eq. 13 *(compiler check, not in the sources)*.
11. Every AEC($N_{\mathrm T}$) flux is PEP for any $N_{\mathrm T}$ if the same $N_{\mathrm T}$ is used in the density and internal-energy expansions. With $v=v_0$ and $p=p_0$ constant, $\{\!\{e\}\!\}_{\mathrm H}=p_0/[\{\!\{\rho\}\!\}(\gamma-1)]$ and $\mathsf j_e=-\mathsf j_\rho$, so $f_{\rho e}=v_0p_0/(\gamma-1)$ (§4, Eq. 14). **Proved**. Both identities follow from $e_i=p_0/((\gamma-1)\rho_i)$ *(compiler check, not in the sources)*.
12. The expansion differs from that of Tamaki et al. [8] (KEEP($N_{\mathrm T}$)), which also expands $[\![1/e]\!]$. This gives an internal-energy flux built on the arithmetic mean, $f_{\rho e}=f_\rho\{\!\{e\}\!\}(1+\mathsf j_e^2/3)/(1+\mathsf j_e^2)$ for KEEP(1), which is not PEP (§4, §5). **Stated** and **Shown**
13. The fluxes of Eqs. 3 and 4, and "other existing methods based on asymptotic approximations", are not PEP at finite order (end of §3). **Stated**
14. A smooth, symmetric and consistent two-point flux $f^{\mathrm{vol}}(u_i,u_{i+k})$ extends to high order by $\hat f_{i+1/2}=2\sum_{k=1}^{L_{\mathrm s}}\mathsf a_k\sum_{m=0}^{k-1}f^{\mathrm{vol}}(u_{i-m},u_{i-m+k})$ (Eq. 18), where $\mathsf a_k$ are the weights of a central derivative of half-width $L_{\mathrm s}$. This follows Theorem 3.1 of Ranocha [7] and Pirozzoli [20], and the derivative has the order of the underlying central formula (App. A). **Derived** (sketch; the proof is in [7])
15. For fluxes built from arithmetic or product means (Eqs. 3, 15), Eq. 18 reduces to a high-order finite-difference discretization of a linear combination of advective and divergence forms. Eq. 18 extends this to nonlinear fluxes that have no direct split-form representation (App. A). **Stated**
16. Density wave: Aρ-Ae (not PEP) diverges near $t=22$, while Aρ-He and Gρ-Ge stay stable up to $t=100$ (§5, Fig. 1a). **Shown**
17. In the density wave, Aρ-He and Aρ-Ap produce the same entropy production up to round-off: for constant $v$ and $p$ both have $f_{\rho e}=v_0p_0/(\gamma-1)$ and the same mass flux (§5). **Derived** and **Shown**
18. At $t=30$ the normalized entropy error $\langle\rho s\rangle$ is $7\times10^{-3}$ for Aρ-He and Aρ-Ap and $-2\times10^{-3}$ for Gρ-Ge (§5). **Shown**
19. KEEP(1) and AEC(1) conserve entropy best in the density wave, AEC(1) slightly better. KEEP(1) shows spurious pressure and velocity oscillations (no PEP; Fig. 1b shows $p-p_0$ on a $10^{-7}$ scale), and AEC(1) does not. The densities of both are visually indistinguishable from that of Ranocha's flux (§5, Fig. 1b). **Shown**
20. With Ranocha's flux the entropy production is "always equal to machine zero" in the tests (§5). **Shown** (not plotted)
21. Taylor–Green vortex ($32^3$, 4th and 6th order): Aρ-He and Gρ-Ge conserve entropy better than Aρ-Ap and Aρ-Ae, and AEC(1) and KEEP(1) keep the entropy integral closest to constant. The linear invariants are conserved to machine precision at CFL 0.1, and the density and temperature fluctuations stay bounded for every scheme (not shown) (§5, Fig. 2). **Shown**
22. The AEC fluxes cost less than logarithmic-mean fluxes and need no local treatment against division by zero in the logarithmic mean (§1, §6). **Stated** (no timings)
23. The density profile is not a pure sine wave because, with a pure sine wave, the authors observed fortuitous global entropy conservation from symmetry despite the lack of local conservation (§5). **Stated**

# Printed slips

- §4, above Eq. 13: "$\overline{e^{-1}}^{\log}=-(\delta\log e)/(\delta e^{-1})$". By the §2 definition, $\{\!\{1/e\}\!\}_{\log}=-[\![1/e]\!]/[\![\ln e]\!]$. The printed right-hand side is its reciprocal, the quantity that enters Eq. 2. Eq. 13 is consistent with the reciprocal, so the slip is in the label only *(compiler check, not in the sources)*.
- §4, PEP proof: "$\overline e^H=P/[(\overline\rho(\gamma-1)]$" has an unbalanced bracket.
- §5 calls AEC$^{(1)}$ "AEP$^{(1)}$" three times ("KEEP(1) and AEP(1), which have better entropy-conservation…", "…KEEP(1) and AEP(1) produce results…", "KEEP(1) and AEP(1) are the schemes which…"). The scheme is defined as AEC$^{(1)}$ in the first paragraph of §5 and in the captions of Figs. 1–2.
- §6 writes "asymptotically entropy-preserving fluxes" and "existing entropy-preserving scheme" for the "entropy-conservative" of the title.
- §5, Taylor–Green initial pressure: printed $p=10+[(\cos2x+\cos2y)(\cos2x+2)-2]/16$. The sources on the [Taylor–Green page](/benchmarks/taylor-green-vortex.md) (Li et al. (2022b), Takagi et al. (2022) and others) print the second factor as $2+\cos2z$.
- Typos: "six-order" (§5), "thorough the study" (§5), "unbound growth" (§5), "could be good candidate" (§6).
- Ref. [5] (Tadmor 1987) prints "Math. Comput., 179:91–103". The bibliography records Math. Comput. 49:91–103 (`tadmor-1987`, DOI 10.2307/2008251), where 179 is the issue number.

# Notation map

| De Michele & Coppola 2023b | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho$, $u$, $p$ | $\rho$, $v$, $p$ | **collision**: source $u$ is the velocity, registry $u$ the conserved state |
| $e$ | $e$ | specific internal energy; agree |
| $E=e+u^2/2$ | $E/\rho$ | **collision**: source $E$ is specific total energy, registry $E$ is per unit volume ($=$ source $\rho E$) |
| $\gamma$, $s=\log(p/\rho^\gamma)$ | $\gamma$, $s$ | agree; $\gamma=1.4$ |
| $\langle\rho s\rangle$ | $\langle\rho s\rangle$ (local) | normalized global entropy error, $(\widetilde{\rho s}-\widetilde{\rho_0s_0})/\widetilde{\rho_0s_0}$ with the tilde the domain integral |
| $\overline\phi$ | $\{\!\{\phi\}\!\}$ | arithmetic mean |
| $\overline\phi^{\log}$ | $\{\!\{\phi\}\!\}_{\log}$ | logarithmic mean |
| $\overline\phi^{G}$, $\overline\phi^{H}$ | $\{\!\{\phi\}\!\}_{\mathrm G}$, $\{\!\{\phi\}\!\}_{\mathrm H}$ (local) | geometric and harmonic means |
| $\overline{\overline{(\phi,\psi)}}$ | $((\phi;\psi))$ (local) | product mean, as on the Ranocha et al. (2023) page; **collision** of $\psi$ with the entropy potential (here a generic quantity) |
| $\delta\phi=\phi_{i+1}-\phi_i$ | $[\![\phi]\!]$ | jump |
| $\hat\phi=\delta\phi/(2\overline\phi)$ | $\mathsf j_\phi$ (local) | normalized jump, $\lvert\mathsf j_\phi\rvert<1$; letter as on the [logarithmic-mean](/operators/logarithmic-mean.md) page (the source's hat is not the numerical-flux hat) |
| $N$ | $N_{\mathrm T}$ (local) | truncation order of AEC/KEEP; **collision** with the DG degree $N$ |
| $\mathcal F_\rho$, $\mathcal F_{\rho u}$, $\mathcal F_{\rho E}$ | $f_\rho$, $f_{\rho v}$, $f_E$ (local) | components of the two-point flux |
| $\mathcal F^c_{\cdot}$ | $f_{\cdot}$ (local) | convective parts in internal-energy form ($f_{\rho e}$ is the source's $\mathcal F^c_{\rho e}$); the pressure term $p\partial_xv$ is central |
| $\mathcal F(w_i,w_{i+k})$, $w=(\rho,u,e)$ | $f^{\mathrm{vol}}(u_i,u_{i+k})$ | symmetric two-point flux (App. A) |
| $\mathcal F^h_{i+1/2}$ | $\hat f_{i+1/2}$ | high-order face flux (Eq. 18) |
| $a_k$, $L$ | $\mathsf a_k$, $L_{\mathrm s}$ (local) | central derivative weights and half-width; **collision** with the wave speed $a$ and the left-eigenvector matrix $L$ |
| $U$, $P$ | $v_0$, $p_0$ (local) | constant velocity and pressure of the PEP analysis |
| Aρ-Ae, Aρ-Ge, Aρ-He, Gρ-Ge, Aρ-Ap, AEC$^{(N)}$, KEEP$^{(N)}$ | as printed | mean used for $\rho$ in the mass flux and for $e$ in the internal-energy flux; Ap: $\{\!\{v\}\!\}\{\!\{\rho e\}\!\}$ |

# Reference list

The paper prints 20 references, numbered [1]–[20]. The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` including
`demichele-2023-b`. Two cited works are ingested sources of the bundle: [4]
([Coppola & Veldman (2023)](/sources/coppola-2023.md), J. Comput. Phys.
475:111879) and [10]
([De Michele & Coppola (2023a)](/sources/demichele-2023.md), Comput. Fluids
250:105709). Coppola 2019 [1] (Appl. Mech. Rev.) and [2] (J. Comput. Phys.
382:86–104) take suffixes in printed order. Ref. [15] is a conference
contribution (ECCOMAS 2022, Oslo) without pages. No item is unparseable.

# Pages created or updated

Chunk 6 (2026-10-23). This source is cited on:

* [Density-wave advection](/benchmarks/density-wave-advection.md)
* [Entropy-conservative and kinetic-energy-preserving two-point fluxes](/methods/entropy-conservative-flux.md)
* [Flux differencing and split-form DG](/methods/flux-differencing.md)
* [Kinetic energy preservation](/properties/kinetic-energy-preservation.md)
* [Logarithmic mean](/operators/logarithmic-mean.md)
* [Pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)
* [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
