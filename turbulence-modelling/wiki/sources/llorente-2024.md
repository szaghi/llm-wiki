---
type: Source
title: "Llorente (2024) — Theoretical considerations of the volume penalization immersed boundary method for turbulent flows"
description: "A letter deriving the Reynolds-averaged equations of the volume-penalization immersed boundary method by averaging the penalized Navier–Stokes equations, which exposes a resistance–velocity correlation closed as minus the body acceleration, with an energy bound and thermal and compressible sketches."
resource: "doi:10.1063/5.0213290"
source_kind: paper
authors: [Llorente V.J.]
year: 2024
venue: "Phys. Fluids 36:071702"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2024_Crossref_Physics_of_Fluids_Llorente_Theoretical_considerations_of_the_volume_penalization_immers.pdf"
tags: [immersed-boundary, rans, eddy-viscosity, incompressible-flow]
timestamp: 2026-10-27T15:53:00Z
---

# Summary

Llorente (2024) asks how the unsteady Reynolds-averaged equations should be
penalized when a volume-penalization variant of the
[immersed boundary method](/methods/immersed-boundary-method.md) represents a
body. Articles on penalized turbulent flow, of which the author cites Yu &
Yu (2022) as an example, add the penalty source $\chi\eta_p^{-1}(\langle u_i\rangle-\langle u_{b,i}\rangle)$
to the URANS equations. The author argues that the consistent route is the
reverse: penalize the instantaneous Navier–Stokes equations, then
Reynolds-average them. Read as a fluid "resistance" $\mathcal R=\chi/\eta_p$
that fluctuates when the body moves, the penalty yields an averaged source
$\langle\mathcal R\rangle\langle u^{\mathrm{rel}}_i\rangle+\langle\mathcal R'u^{\mathrm{rel}\prime}_i\rangle$,
whose second term is a resistance–velocity correlation that needs closure.

A time-scale analysis puts the penalty in the regime
$\eta_p\ll\mathcal T_c\ll\mathcal T_d$. In that regime the equation inside the body
reduces to a linear relaxation, whose solution carries an "artificial
velocity", a series in powers of $\eta_p$ and of the time derivatives of the body
velocity. The series vanishes only for a body at rest or in uniform motion.
Requiring exact penalization in the averaged equation closes the correlation as
minus the mean body acceleration. The closed URANS system then carries a
source $-\chi\,\partial_t\langle u_{b,i}\rangle$. For a fixed body the two routes
coincide. A theorem bounds the $L^2$ norm of the mean velocity by that of the
body velocity when $\nu+\nu_t\ge0$. Short sketches extend the argument to a
thermal Neumann condition imposed by characteristics-based penalization and to
compressible flow with Favre averaging.

The eddy viscosity is left unspecified, and the closure is printed in a
non-symmetric gradient form with the opposite sign convention (see the
[Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md) and the Notation
map). The letter contains no computations. Its energy estimate is a
continuous-level bound, related only loosely to
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md) of
discretizations.

# Version read

The author accepted manuscript (AIP/REVTeX author layout, running header
"Turbulent VP-IBM", dated 1 July 2024, pages 1–14), all read. The equations
were checked on the page images, because text extraction drops the overbars.
Title and author match the published Letter, and there is no identity problem.
Page and equation numbers on this page are those of the manuscript. The
Letter has one schematic figure, no tables and no numerical results.

# Key claims

Page-local symbols: $\chi$ is the body mask (1 in the body, 0 outside), not
the SA ratio. $\eta_p$ is the penalization parameter ("permeability"; the
source's $\eta$, not the Kolmogorov length). $u_{b,i}$ is the body velocity,
and $u^{\mathrm{rel}}_i=u_i-u_{b,i}$ the relative velocity (the source's $w_i$).
$\mathcal R=\chi/\eta_p$ is the fluid resistance (the source's
$\mathscr R_\eta$). $\mathcal T_c=\mathcal L/\mathcal U$ and
$\mathcal T_d=\mathcal L^2/\nu$ are the convective and diffusive times.
$\langle\cdot\rangle$ is the Reynolds (ensemble) average, the source's
overbar.

1. The penalized incompressible Navier–Stokes equations add $s_i=\chi\eta_p^{-1}(u_i-u_{b,i})$ to the momentum equation. The penalized solution differs from the unpenalized one (Eqs. 2a–2b, p. 2). **Stated**
2. Angot, Bruneau & Fabrie (1999), and later Carbou & Fabrie (2003), proved that the penalized velocity converges to the no-slip velocity as $\eta_p\to0$, with error $\propto\eta_p^{\alpha}$, "$\alpha=1/2$ for Dirichlet boundary conditions". Inside the body the flow is a Darcy flow at order $\eta_p$. Basarić et al. (2022) proved convergence for the Navier–Stokes–Fourier system (p. 2). **Stated**
3. Typical values are "$\eta\in\{10^{-7},10^{-10}\}$" (citing Ménez et al. 2023). The lower limit comes from stability, because small $\eta_p$ makes the source very stiff and restricts the time step (citing Kou et al. 2022) (p. 2). **Stated**
4. Published penalized treatments of turbulent flow, e.g. Yu & Yu (2022), "just simply take the turbulent equations and penalized the turbulent velocity field", adding $\chi\eta_p^{-1}(\langle u_i\rangle-\langle u_{b,i}\rangle)$ to URANS (p. 3, Eqs. 3–4). **Stated**
5. Nondimensionalizing the penalized momentum equation and multiplying by $\eta_p/\mathcal U$ gives Eq. (5), with $\mathcal T_d/\mathcal T_c=Re$. At high Reynolds number the penalty condition is $\eta_p\ll\mathcal T_c\ll\mathcal T_d$ (Eq. 6), which the author identifies with the intermediate damping regime of Hester, Vasil & Burns (2021) (pp. 4–5). **Derived**
6. Under condition (6), the mean velocity inside the body obeys $\partial_t\langle u_i\rangle+\langle u_i\rangle/\eta_p=\langle u_{b,i}\rangle/\eta_p$ (Eq. 7a), solved in closed form (Eq. 7b). Repeated integration by parts gives the series (Eq. 7c), $\langle u_i\rangle=\langle u_{b,i}\rangle+\sum_{k\ge1}(-1)^k\eta_p^k\big[\partial_t^k\langle u_{b,i}\rangle-\partial_t^k\langle u_{b,i}\rangle\big|^0e^{-t/\eta_p}\big]$, so that $\langle u_i\rangle\to\langle u_{b,i}\rangle$ as $\eta_p\to0$. The author says this "complements" Angot et al. (p. 5). **Derived**
7. In general $\langle u_i\rangle\ne\langle u_{b,i}\rangle$ in the body, with equality only for a body at rest or in uniform motion. As $t\to\infty$ the remainder of (7c) persists as an "artificial velocity arising from errors due to the modellization of the volume penalization" (p. 5). **Derived**
8. The coefficient $\chi/\eta_p$ is reinterpreted as a fluid resistance $\mathcal R$ (inverse permeability), a piecewise-constant fluid property like density or viscosity, which fluctuates when the body moves (Eqs. 8a–8b, p. 6, Fig. 1). **Stated** (modelling postulate, the paper's main idea)
9. Reynolds-averaging the penalized system gives the averaged penalty source $\langle s_i\rangle=\langle\mathcal R\rangle\langle u^{\mathrm{rel}}_i\rangle+\langle\mathcal R'u^{\mathrm{rel}\prime}_i\rangle$ (Eq. 9c). The extra term "arises because the body is moving" (p. 6). **Derived**
10. $\mathcal R'$ is concentrated near the body interface, but $\langle\mathcal R'u^{\mathrm{rel}\prime}_i\rangle$ cannot be assumed zero where $\mathcal R'=0$. It decays to zero for a semi-infinite body and is assumed non-zero inside a finite body. Such correlations "cannot therefore be closed, like for the Reynolds stress tensor" (p. 6). **Stated**
11. Requiring $\langle u_i\rangle=\langle u_{b,i}\rangle$ in the body for all $t>0$ in the averaged body equation (Eqs. 10a–10b) gives $\langle\mathcal R'u^{\mathrm{rel}\prime}_i\rangle=-\partial_t\langle u_{b,i}\rangle$ (Eq. 11). The term vanishes "if and only if the body does not move or move uniformly" and is "an unsteady correction: a local force per mass acting on the fluid where the solid is supposed to be" (p. 7). **Derived**
12. For a fixed body the averaged source equals the penalty applied to the mean velocity, so "penalized the traditional URANS equations" and "averaging the penalized iNS equations" are indistinguishable (p. 8). **Derived**
13. The closed URANS system is Eqs. (12a)–(12b): the momentum equation carries $\langle\mathcal R\rangle\langle u^{\mathrm{rel}}_i\rangle-\chi\,\partial_t\langle u_{b,i}\rangle$, with $\langle u_i\rangle=0$ on the outer boundary (12c) and initial value $\chi\langle u_{b,i}\rangle^0$ (12d) (p. 8). **Derived** (contribution)
14. Theorem 1: a solution of (12a)–(12d) has an energy norm bounded by the body motion, provided the total viscosity does not become negative. The proof ends with $\|\langle\boldsymbol u\rangle(\cdot,T)\|_2\le\|\langle\boldsymbol u_b\rangle(\cdot,T)\|_2$ under $\nu+\nu_t\ge0$ (pp. 8–9, Eqs. 13–14d). In term (III) of the proof the author "deduce[s]" $\langle u_i\rangle=\langle u_{b,i}\rangle$ inside the body. **Proved** (see Printed slips)
15. Thermal extension: a Neumann wall condition $\partial T/\partial n=q$ imposed by characteristics-based penalization (Brown-Dymkoski et al. 2014) gives a thermal resistance $\chi/\eta_{p,T}$. Its correlation with the Neumann residual is $-\int\partial_t\langle q\rangle\,\mathrm d\xi$ along the characteristics $\mathrm dx_k/\mathrm d\xi=n_k$ (p. 9). **Derived** (sketch)
16. Compressible extension: with the source $\mathcal R\rho u^{\mathrm{rel}}_i$, Favre decomposition of the relative velocity and Reynolds decomposition of $\mathcal R$ and $\rho$, the averaged source gains the correlation $\langle\rho\mathcal R'u^{\mathrm{rel}\prime\prime}_i\rangle$, closed as $-\partial_t(\langle\rho\rangle\langle u_{b,i}\rangle_\rho)$ (p. 10). **Derived** (sketch, no steps shown)
17. Volume penalization is "highly dependent on the porous medium modelling approach". The same ideas apply to characteristics-based penalization, whose penalty adds non-physical diffusion; in conservative form the new diffusion coefficient would fluctuate (p. 10). **Stated**
18. Conclusion: "deriving a penalized form of the turbulent equations without due care may lead to overlooking terms crucial for accurately modelling turbulence in such penalized flows". The URANS equations of a penalized flow should start from the penalized Navier–Stokes system and then be averaged (pp. 10–11). **Stated**
19. Immersed boundary methods are challenging for turbulent flow because near-wall friction matters at high Reynolds number on non-conforming meshes. Penalization of turbulent flow "is approached more from a numerical perspective than from a physical one" (p. 3). **Stated**

# Printed slips

- **Closure (p. 4):** "$R_{ij}:=-\overline{u'_iu'_j}=\nu_t\,\partial\overline u_i/\partial x_j$". The left side is symmetric and the right side is not, and there is no isotropic part. The same form is carried into the total tensor $\overline\Pi_{ij}$ *(compiler check, not in the sources)*.
- **Energy identity (p. 9):** the last line prints $\|\overline u(\cdot,T)\|_2^2=\|\overline u_b(\cdot,T)\|_2^2-2\int_\Omega(\nu+\nu_t)\partial_j\overline u_i\partial_j\overline u_i\,\mathrm d^3x$, and Eqs. (14b)–(14c) likewise lack the time integral that Eq. (13) carries. *(compiler check, not in the sources)* Integrating (13) over $[0,T]$ makes the dissipation term $-2\int_0^T\!\int_\Omega(\nu+\nu_t)\,\partial_j\langle u_i\rangle\partial_j\langle u_i\rangle\,\mathrm d^3x\,\mathrm dt$.
- **"the above integral is negative semi-definite" (p. 9):** for $\nu+\nu_t\ge0$ the integral is non-negative, and only the term with the factor $-2$ is non-positive.
- **Theorem 1 against Eq. (7c):** *(compiler check, not in the sources)* the proof's term (III) uses $\langle u_i\rangle=\langle u_{b,i}\rangle$ inside the body, which is also the assumption that closes Eq. (11). The paper's own Eq. (7c) gives a non-zero remainder for finite $\eta_p$ when the body accelerates. The theorem therefore holds under exact penalization. On p. 6 the correlation is also said to be one that "cannot … be closed", and it is then closed by this kinematic requirement.
- **Heat equation (p. 9):** printed $\partial T/\partial t+\partial(u_jT+\kappa\,\partial T/\partial x_j)/\partial x_j+\mathscr R_{\eta_T}h=0$. *(compiler check, not in the sources)* With the advective flux $u_jT$ on the left, as in the momentum form (1b) with $-\nu\,\partial u_i/\partial x_j$, diffusion requires $-\kappa\,\partial T/\partial x_j$. The printed sign is anti-diffusive.
- **"$\eta\in\{10^{-7},10^{-10}\}$" (p. 2):** set notation for a range, with the endpoints in reverse order.
- **Symbol clash:** $T$ is the final time in Theorem 1 and the temperature on p. 9.
- **Typos:** "from a more physically perspective" (abstract); "IMBs" (p. 3); "vanishs" (p. 7); "This integral only exits within" (p. 9); "assemble-averaged" and "penlized" (p. 10).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\overline\phi$, $\phi'$ | $\langle\phi\rangle$, $\phi'$ | **collision:** the overbar is the Reynolds (ensemble) average, not the LES filter |
| $\widetilde a=\overline{\rho a}/\overline\rho$, $a''$ (p. 10) | $\langle a\rangle_\rho$, $a''$ | **collision:** the tilde is the Favre *average*, not the Favre filter |
| $R_{ij}:=-\overline{u'_iu'_j}=\nu_t\,\partial\overline u_i/\partial x_j$ (p. 4) | $R_{ij}=\langle u_i'u_j'\rangle=-\nu_t\,\partial_j\langle u_i\rangle$ (the printed closure, translated) | **sign:** the source's $R_{ij}$ is minus the registry's. The printed closure is the non-symmetric velocity gradient without the factor 2 and without $\tfrac23k\delta_{ij}$, against the registry's $R_{ij}-\tfrac23k\delta_{ij}=-2\nu_t\langle S_{ij}\rangle$ |
| $\overline\Pi_{ij}=\overline u_i\overline u_j-(\nu+\nu_t)\partial_j\overline u_i+(\overline p/\rho)\delta_{ij}$ | (total momentum flux, page-local) | built on the printed closure |
| $\nu_t$ | $\nu_t$ | agrees; no RANS model specified |
| $\eta$ | $\eta_p$ (page-local, as on the immersed-boundary page) | **collision:** not the Kolmogorov length |
| $\chi$ | $\chi$ (mask, page-local) | **collision:** not the SA ratio $\tilde\nu/\nu$ |
| $\mathscr R_\eta=\chi/\eta$, $\mathscr R_{\eta_T}=\chi/\eta_T$ | $\mathcal R$, $\chi/\eta_{p,T}$ (page-local, as on the immersed-boundary page) | fluid and thermal resistance |
| $u_{\eta,i}$, $p_\eta$ | $u_i$, $p$ | penalized solution; the subscript is dropped after Eq. (4) |
| $u_{b,i}$ | $u_{b,i}$ (page-local) | body velocity |
| $w_i=u_i-u_{b,i}$ | $u^{\mathrm{rel}}_i$ (page-local) | **collision:** $w_i$ is the quadrature weight in the registry |
| $s_{\eta,i}$, $s^\dagger_{\eta,i}$ | $s_i$ (page-local) | penalty source, on the instantaneous or the mean velocity |
| $\mathcal T_c=\mathcal L/\mathcal U$, $\mathcal T_d=\mathcal L^2/\nu$ | (page-local) | $Re=\mathcal T_d/\mathcal T_c=\mathcal U\mathcal L/\nu$ |
| $\mathfrak u_i$ | (artificial velocity, page-local) | remainder of Eq. (7c) |
| $\kappa$ (p. 9) | (thermal diffusivity, page-local) | **collision:** not the von Kármán constant |
| $T$ | $T$ (temperature) | also the final time of Theorem 1 |
| $\xi$ | (characteristic parameter, page-local) | **collision:** not the reference coordinate of element methods |
| $\|\phi\|_2^2=\int_\Omega\phi^2\,\mathrm d^3x$ | (page-local) | $L^2$ norm over the whole domain |

# Reference list

30 printed references, numbered in order of first citation (AIP superscript
style), with no DOIs or arXiv identifiers. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Ref. [17] (Constant
et al. 2021, J. Comput. Phys. 435:110240) is a different work from the ingested
[constant-2024](/sources/constant-2024.md). Ref. [9] (Kou et al. 2022,
J. Comput. Phys. 448:110721) is a different work from the ingested
[kou-2023](/sources/kou-2023.md). Neither shares a key with them. Doubtful
items, recorded as printed: ref. [30] has a stray author token "Emmanuel"; ref.
[22] gives "AIAA Journal 454" for 2015; ref. [18] pairs volume 21 with 2014; and
ref. [3] reads "applicationa la convection naturelle". No printed duplicates.

# Pages created or updated

Chunk 6 (2026-10-26). This source is cited on:

- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Immersed boundary methods](/methods/immersed-boundary-method.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
