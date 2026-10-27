---
type: Source
title: "Dzanic et al. (2022) — Partially-averaged Navier–Stokes simulations of turbulence within a high-order flux reconstruction framework"
description: "Couples compressible PANS with a k-ω SST closure to second- and fourth-order flux reconstruction at equal degrees of freedom, and shows on the periodic hill and the Re_D=3900 cylinder that high order helps PANS more than unmodelled implicit LES and lowers its optimal f_k."
resource: "doi:10.1016/j.jcp.2022.110992"
source_kind: paper
authors: [Dzanic T., Girimaji S., Witherden F.]
year: 2022
venue: "J. Comput. Phys. 456:110992"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Journal_of_Computational_Physics_Dzanic_Partially-averaged_NavierStokes_simulations_of_turbulence_wi.pdf"
tags: [pans, hybrid-rans-les, flux-reconstruction, implicit-les, numerical-dissipation]
timestamp: 2026-10-26T20:45:00Z
---

# Summary

Dzanic et al. (2022) combine [partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md)
(PANS), a [hybrid RANS/LES](/definitions/hybrid-rans-les.md) bridging model, with
the high-order flux reconstruction (FR) scheme as implemented in PyFR. They ask
how the order of the discretization changes (i) the accuracy of PANS relative to
under-resolved DNS without a model (URDNS, which the paper identifies with
[implicit LES](/definitions/implicit-les.md)) and (ii) the optimal value of the
resolution-control parameter $f_k$ and the sensitivity to it. The compressible
PANS equations are closed with a [Boussinesq](/definitions/boussinesq-hypothesis.md)
unresolved stress and the [$k$-$\omega$ SST model](/methods/k-omega-sst-model.md)
written for the unresolved fields $f_kk$ and $f_\omega\omega$. With
$f_\varepsilon=1$, $f_\omega=1/f_k$, so the model has a single parameter $f_k$,
constant in space and time. For robustness with low-dissipation high-order
schemes the $\omega$ equation is solved in logarithmic form, and a new
forward-Euler source term clips the unresolved kinetic energy at $10^{-8}$.

The comparison is made at fixed total degrees of freedom: FR with $N=1$
(second order) against $N=3$ (fourth order), the $N=1$ meshes having
"approximately 6-8 times as many elements". The test cases are the [periodic hill](/benchmarks/periodic-hill.md)
at $Re_h=10\,595$ (bulk velocity and hill height) on a very coarse grid ($64\times64\times32$ DOF, against the
LES of Fröhlich et al.), with $f_k=0.2,0.3$, and the circular cylinder at
$Re_D=3900$, with $f_k=0.1,0.2,0.3$. For the cylinder the authors run a new
fourth-order [DNS](/definitions/direct-numerical-simulation.md) with about
55.6 million DOF and a POD analysis. High order improves first-order
statistics about equally for URDNS and PANS, but it improves the PANS
second-order statistics (hill) and the flow physics (cylinder shedding and
Kelvin–Helmholtz peaks, primary POD mode) far more than URDNS. High-order
URDNS on the hill shows spurious oscillations in the stresses, which the
authors attribute to aliasing. High-order PANS is less sensitive to $f_k$, and
its optimal $f_k$ is lower (0.1 against 0.3 on the cylinder). The authors
attribute the gains to the lower [numerical dissipation](/properties/numerical-dissipation.md)
of high-order schemes. All evidence is numerical.

# Version read

arXiv preprint arXiv:2106.02582v1 [physics.flu-dyn], 4 June 2021 ("Preprint
submitted to Elsevier"), 20 pages. The metadata above are those of the
published version (J. Comput. Phys. 456:110992, 2022). Title and authors match
the published version up to capitalisation and hyphenation. The archive file
carries a Crossref/JCP filename but holds the arXiv v1. Section, equation and
figure numbers on this page are those of the arXiv v1.

# Key claims

1. PANS with $f_\varepsilon=1$ reduces to a one-parameter model with $f_\omega=f_\varepsilon/f_k=1/f_k$. $f_k$ and $f_\omega$ are kept constant in space and time to avoid commutation-error terms (§2.1). **Stated** (assumption from Girimaji & Wallin and Pereira et al.).
2. Solving for $\ln(f_\omega\omega)$ guarantees positivity of the unresolved specific dissipation, which then appears only through its exponential, and the logarithmic variable is smoother (§2.3, Eq. 23). **Stated** (after Ilinca & Pelletier via Bassi et al.).
3. A source term $S_k^n=\max\left[0,(k_{\min}-(f_kk)^n)/\Delta t+\nabla\cdot\boldsymbol F_k^n\right]$, with $\boldsymbol F_k$ the flux of the unresolved kinetic energy, limits $f_kk$ to $k_{\min}=10^{-8}$. Bassi et al. instead allow negative $k$ in the solution and limit it to zero in the transport and auxiliary equations (§2.3, Eq. 24). **Stated** (contribution; not tested separately).
4. The PyFR implementation uses a Rusanov-type Riemann solver, BR2 viscous fluxes and explicit fourth-order Runge–Kutta (§2.3). **Stated**.
5. FR with $N=1$ is a second-order scheme "comparable to a finite volume formulation" and $N=3$ is fourth order. At equal DOF, the $N=1$ meshes have "approximately 6-8 times as many elements" (§2.3). **Stated**. The grid tables give a factor of 8 for both cases *(compiler check, not in the sources)*.
6. The periodic-hill grids use 97% fewer DOF than the LES of Fröhlich et al. and 85% fewer than the low-order PANS of Razi et al. (§3.1). **Stated**.
7. At the hill resolution, $f_k<0.2$ is not supported "through a posteriori analysis" (§3.1). **Stated** (no analysis shown).
8. Hill mean velocity: at low order, PANS and URDNS both overpredict flow reversal for $0\le x\le5$ and PANS does not improve significantly on URDNS. At high order both improve significantly, $f_k=0.2$ is in "excellent agreement" with the reference LES, and the spread between $f_k$ values shrinks (§3.1, Fig. 3). **Shown**.
9. Hill $\langle u'u'\rangle$: URDNS overpredicts at both orders with no appreciable gain from high order. PANS improves notably from $N=1$ to $N=3$, in excellent agreement for both $f_k$ at $N=3$ (§3.1, Fig. 4). **Shown**.
10. Hill $\langle v'v'\rangle$: high-order URDNS degrades with large oscillations, attributed to aliasing-driven instabilities of high-order schemes in under-resolved turbulence. High-order PANS does not show them, "likely due to the suppression of aliasing errors as a result of the introduction of a physically appropriate eddy viscosity" (§3.1, Fig. 5). **Shown** (oscillations) / **Stated** (attribution).
11. Hill $\langle u'v'\rangle$: high-order PANS is good for both $f_k$, with monotonic profiles outside the separation region. The reduced $f_k$-sensitivity at high order is less evident here than for the variances (§3.1, Fig. 6). **Shown**.
12. Cylinder DNS at $Re_D=3900$ ($N=3$, about 55.6 million DOF): minimum $\eta/D=0.011$, $\Delta s_{xy}/\eta\in[0.25,0.83]$ for $x/D<10$, $\Delta s_z/\eta=0.85$ (§3.2). **Shown** (a posteriori).
13. The DNS gives $St=0.209$, "in agreement with" Parnaudeau et al., and a Kelvin–Helmholtz frequency $f_{KH}=0.668$, with frequencies scaled by $D/U_\infty$ (§3.2). **Shown**.
14. Cylinder centreline velocity: low-order URDNS overpredicts the edge of the recirculation region, which high order remedies. Low-order PANS is sensitive to $f_k$ ($f_k=0.1$ agrees with the LES of Parnaudeau et al., $f_k=0.3$ with the DNS). High-order PANS is less sensitive, and $f_k=0.1$ is in excellent agreement with the LES of Witherden et al. At high order, PANS generally prolongs the recirculation region (§3.2, Fig. 8). **Shown**.
15. Over the profile stations, the best accuracy is obtained at $f_k=0.3$ for low order (agreeing with the DNS) and at $f_k=0.1$ for high order (agreeing with the LES of Witherden et al.). This is "consistent with the PANS methodology, as the increase in fidelity afforded by high-order methods coincides with a decrease in the unresolved portion of the flow" (§3.2, Fig. 9). **Shown** / interpretation **Stated**.
16. Cylinder second-order statistics: the effects of order and model are not consistent across quantities and locations. Except at $f_k=0.3$, high order tends to increase the magnitude of second-order statistics, "likely due to the decrease in numerical dissipation". Order mainly shifts the optimal $f_k$ (0.3 at low order, 0.1 at high order) (§3.2, Fig. 10). **Shown**.
17. Spectra at $x/D=3$: low-order runs overpredict the shedding and KH peak frequencies "by roughly 10% and 6%" and, except at $f_k=0.3$, do not adequately resolve the KH frequency. High-order runs match the DNS frequencies, with more prominent PANS peaks than URDNS. $f_k=0.1$ is excellent and $f_k=0.2$–$0.3$ reasonable (§3.2, Fig. 11). **Shown**.
18. Spectra at $x/D=7$: no low-order run resolves the KH frequency prominently. High-order URDNS fails to resolve KH and smears the shedding peak, while high-order PANS resolves both peaks for all $f_k$, in good agreement with the DNS (§3.2, Fig. 12). **Shown**.
19. Primary POD mode of the streamwise velocity: low order places the shedding region too far aft (monotonically from URDNS to $f_k=0.3$) and misses its circular shape and the shear-layer correlation. High order corrects the shape and the shear-layer correlation. High-order URDNS places the shedding region too close to the cylinder, and high-order PANS agrees with the DNS. For POD, high order brings no significant decrease in $f_k$-sensitivity (§3.2, Fig. 13). **Shown**.
20. High-order discretizations benefit PANS proportionally more than URDNS. The benefit comes from lower numerical dissipation, which lets the scheme resolve small-scale features predicted by the model, and high-order PANS is less sensitive to $f_k$. "High-order discretizations may be an effective approach for increasing the accuracy and reliability of hybrid turbulence models ... without a significant increase in computational effort" (§4). **Shown** (on two cases) / cost claim **Stated** (no timings given).
21. The stated goal "is not to evaluate the efficacy of the PANS method, but to show the effect of high-order discretizations for SRS using PANS and how that effect differs from approaches without any physical models" (§3). **Stated**.

# Printed slips

- **Eq. 12, $\alpha_1$ against $a_1$.** Eq. 12 prints $\mu_u=\rho\alpha_1k_u/\max(\alpha_1\omega_u,\Omega F_2)$. Appendix A lists both $\alpha_1=0.5532$ (an inner SST constant) and a separate $a_1=0.31$ that appears in no printed equation.
- **$\mu_t$ against $\mu_u$.** The diffusion coefficients of Eqs. 10, 11 and 23 print $\mu_t$, whereas the eddy viscosity defined in Eq. 12 and used elsewhere is $\mu_u$. $\mu_t$ is never defined.
- **Production with the molecular stress.** The production is printed $P_k=\tau_{ij}\,\partial u_i/\partial x_j$, with $\tau_{ij}$ defined in Eq. 4 as the molecular viscous stress, not the unresolved stress $\tau'_{ij}$ of Eq. 7.
- **DNS limit.** §2.1 states that PANS blends "between DNS ($f_k=f_\omega=0$) and URANS ($f_k=f_\omega=1$)". With the adopted $f_\omega=1/f_k$, $f_\omega\to\infty$ as $f_k\to0$. The wall value $\omega_u=f_\omega\,60\nu/(\beta_1\Delta d_1^2)$ and the inflow value $\omega_u=f_\omega U_\infty/D$ (Eqs. 26–27) therefore scale as $1/f_k$.
- **Plane of the cross-section.** The §3.1 text and the Fig. 2 caption call the hill cross-section the "streamwise-spanwise plane", although the geometry is "formed by extruding the cross-section along the spanwise direction". The Fig. 7 caption repeats this for the cylinder, whose text calls it the $xy$ plane.
- **Figure normalisation.** The text defines $U_b$ and the hill height $h$; the axes of Figs. 3–6 read $u/U_\infty$ and $y/H$.
- **Time notation.** "fully developed after $t=D/U_\infty=100$ ... until $t=D/U_\infty=300$" (§3.2), for $tU_\infty/D$.
- **Eq. 4** prints $\tau_{ij}=2\mu[S_{ij}-\frac13\partial u_k/\partial x_k]$ without $\delta_{ij}$ on the trace term.
- **Eq. 11, dimensions** *(compiler check, not in the sources)*. $P'=\rho\alpha\beta^*k_u/\mu_u$ has units of 1/s, so the bracket $\rho(P'-P'/f_\omega+\beta\omega_u/f_\omega)$ has units $\rho/\mathrm{s}$. The time derivative $\partial(\rho\omega_u)/\partial t$, the production and the diffusion terms have units $\rho/\mathrm{s}^2$. As printed, the bracket lacks a factor $\omega_u$. The same bracket appears in Eq. 23.
- **Eq. 23, logarithmic form** *(compiler check, not in the sources)*. Rewriting Eq. 11 for $\ln\omega_u$ divides every source term by $\omega_u$ and produces an extra term $(\mu+\mu_t\sigma_\omega f_\omega/f_k)\,\partial_j\ln\omega_u\,\partial_j\ln\omega_u$ from the diffusion. Eq. 23 as printed keeps the sources of Eq. 11, replaces $\omega_u$ by its exponential only in the $\beta$ and cross-diffusion terms, and has no gradient-squared term. The form implemented in PyFR cannot be recovered from the text.
- **Spanwise DNS resolution** *(compiler check, not in the sources)*. Grid B3 has 96 spanwise DOF over $z/D\in[0,\pi]$, so $\Delta s_z/D=\pi/96\approx0.0327$. With the stated minimum $\eta/D=0.011$, this gives $\Delta s_z/\eta\approx2.97$, not the printed 0.85. The printed value would require a local or averaged $\eta/D\approx0.0385$, which the text does not define.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho$, $u_i$, $E$, $P$ (resolved) | $\rho$, $u_i$, $E$, $p$ | the paper marks neither the PANS filter nor Favre weighting on resolved variables |
| $\tau_{ij}=2\mu[S_{ij}-\tfrac13\partial_ku_k]$ (Eq. 4) | $\sigma_{ij}$ | molecular viscous stress |
| $\tau'_{ij}=2\mu_uS_{ij}-\tfrac23k_u\delta_{ij}$ (Eq. 7) | $-\tau_{ij}$ (density-weighted) | **sign:** the source adds $\tau'_{ij}$ to the viscous stress, so it is the negative of the registry's positive-trace subfilter stress; no $\rho$ on $k_u$ and no deviatoric projection of $S_{ij}$ as printed |
| $\mu_u$ (Eq. 12), $\mu_t$ (Eqs. 10, 11, 23) | $\mu_t$ | unresolved eddy viscosity; see Printed slips |
| $k$, $\omega$ | $k$, $\omega$ | total kinetic energy and specific dissipation |
| $k_u$, $\omega_u$ | $k_u=f_kk$, $\omega_u=f_\omega\omega$ | unresolved (modelled) parts; registry §11 shared symbols |
| $f_k$, $f_\omega$, $f_\epsilon$ | $f_k$, $f_\omega$, $f_\varepsilon$ | $f_\varepsilon=1$, $f_\omega=1/f_k$ |
| $\tilde\omega_u=\log\omega_u$ | $\ln(f_\omega\omega)$ | **collision:** this tilde is neither a Favre filter nor the SA variable |
| $P_k$ | (production of $f_kk$) | printed with the molecular stress, see Printed slips; registry $P_k=-R_{ij}\partial_j\langle u_i\rangle$ |
| $W_{ij}$, $\Omega=\sqrt{2W_{ij}W_{ij}}$ | $\Omega_{ij}$, $\lvert\Omega\rvert$ | factor two agrees |
| $S_{ij}$ | $S_{ij}$ | agrees |
| $\alpha,\beta,\sigma_k,\sigma_\omega$; $\alpha_1,\alpha_2$; $a_1$; $\beta^*$ | SST constants | as in the original model; values in App. A |
| $F_1$, $F_2$, $CD_{k\omega}$ | $F_1$, $F_2$, $CD_{k\omega}$ | SST blending functions, cross-diffusion floored at $10^{-10}$ |
| $d$ | $d$ | wall distance |
| $\gamma=1.4$, $Pr=0.71$, $Pr_t=0.9$ | $\gamma$, $Pr$, $Pr_t$ | agree |
| $h$ (specific enthalpy) | (specific enthalpy) | **collision:** also the hill height in §3.1, and the registry's element size $h$ |
| $p$, $\mathbb P_p$ | $N$ | polynomial degree; FR order $N+1$ |
| $N$ (number of elements) | (number of elements) | **collision:** registry $N$ is the polynomial degree |
| $q$, $r$ | (numbers of solution and interface points) | |
| $\hat{\mathbf u}$, $\hat{\mathbf f}^D$, $\hat{\mathbf f}^C$, $\mathbf g_j$ | (FR interpolant, discontinuous flux, correction flux, correction functions) | **collision:** the hat marks the FR interpolant, not a test filter |
| $\mathbf f^I$ | $f^*$ | common interface flux |
| $\Delta d_1=\Delta d_e/(p+1)$ | (first-point wall distance) | $\Delta d_e$ element height |
| $\eta$ | $\eta$ | Kolmogorov length; only its minimum is defined |
| $\Delta s_{xy}$, $\Delta s_z$ | (average subcell size) | element size over DOF per direction |
| "bulk Reynolds number" (hill), $Re_D$ | $Re_h$, $Re_D$ | hill: bulk velocity $U_b$ and hill height $h$; cylinder: diameter |
| $St$, $f_{KH}$ | $St$, (KH frequency) | scaled by $D/U_\infty$ |
| URDNS | implicit LES | the paper writes "implicit LES (ILES) or under-resolved DNS (URDNS)" |

# Reference list

37 printed references in numbered style ([1]–[37]). The list is merged complete
into the [bibliography](/bibliography.md) with `citedby` this slug. No printed
duplicates or unparseable items: ref. [28] (Wang 2009, PhD thesis) prints no
institution, ref. [1] (Reed & Hill 1973) prints no report number, ref. [27]
(Benocci & Pinelli 1990) prints no DOI, and ref. [7] (Girimaji, J. Appl. Mech.)
is recorded with the printed year 2005.

# Pages created or updated

Chunk 1 (2026-10-25), cited further in chunks 2, 5. This source is cited on:

- [Circular-cylinder wake](/benchmarks/circular-cylinder-wake.md)
- [Periodic hill](/benchmarks/periodic-hill.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Flux reconstruction](/methods/flux-reconstruction.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [Partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
