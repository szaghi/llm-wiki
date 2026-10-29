---
type: Source
title: "Alberti et al. (2025b) — An entropy-aware discontinuous Galerkin solver for implicit large eddy simulations of wall-bounded flows"
description: "Runs a modal discontinuous Galerkin solver made entropy conserving or stable by entropy projection and a parameter-free entropy-balance correction as an implicit LES of incompressible-limit and supersonic channels, proves an entropy-stable isothermal wall condition, and finds the conserving flux best at low Mach and the stable flux best at high Mach."
resource: "doi:10.1063/5.0270394"
source_kind: paper
authors: [Alberti L., Carnevali E., Colombo A., Crivellini A.]
year: 2025
venue: "Phys. Fluids 37:075105"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2025_Crossref_Physics_of_Fluids_Alberti_An_entropy-aware_discontinuous_Galerkin_solver_for_implicit.pdf"
tags: [implicit-les, dg, entropy-stable, numerical-dissipation, compressible, channel-flow]
timestamp: 2026-10-29T05:18:00Z
---

# Summary

Alberti et al. (2025b) use a high-order modal discontinuous Galerkin
solver (orthonormal hierarchical basis in physical space, full
$\mathbb P^N$ spaces; contrasted with nodal split-form
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md)) as an
[implicit LES](/definitions/implicit-les.md) of turbulent channels. The
unknowns stay conservative, but every space operator is evaluated from the
$L_2$ projection of the solution onto the entropy variables, and the
quadrature error left in the entropy balance is removed by the Direct
Enforcement of the Entropy Balance (DEEB), an explicit element-wise
correction after Abgrall with no user parameter
([entropy conservation](/properties/entropy-conservation.md)). With DEEB,
the Ismail–Roe flux makes the convective discretization entropy
conserving (EC) and the exact-Riemann Godunov flux entropy stable (ES).
Viscous terms use BR2; App. C bounds the BR2 entropy production with the
viscous matrix frozen to element means, so the BR2 penalty acts as an
entropy source ([jump-penalty stabilization](/methods/jump-penalty-stabilization.md)).
A new result is that the weak isothermal no-slip wall with the
exact-Riemann wall pressure is entropy stable (ESW), while extrapolating
the wall pressure gives an entropy-conserving wall (ECW). DEEB is likened
to [artificial viscosity](/methods/artificial-viscosity-shock-capturing.md)
and [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md),
but acts on every mode except the mean and has no shock-capturing role.

[Channel](/benchmarks/turbulent-channel-flow.md) tests at
$Re_\tau=180$, 395, 590 ($M_b=0.18$) and isothermal-wall channels at
$M_b=1.5$ ($Re_\tau=222$, 500, 1000) and $M_b=3$ ($Re_\tau=450$),
compared with [DNS](/definitions/direct-numerical-simulation.md), are
paired with incompressible cases through the Trettel–Larsson
[velocity transformation](/definitions/compressible-velocity-transformation.md).
On moderately under-resolved grids ($N=8$) the profiles collapse on DNS.
On severely under-resolved grids (down to about 1/2000 of the DNS degrees
of freedom) the dissipation-free EC flux with the ESW wall is the most
accurate near the incompressible limit, and the ES flux over-shears the
near-wall fluctuations; at high Mach the ES flux is best, the EC flux
under-predicts the velocity and crashes at $M_b=3$ unless an upwind bias
is added. The thesis is that under-resolved implicit-LES accuracy hinges
on the [numerical dissipation](/properties/numerical-dissipation.md) in
the first wall-adjacent cells. A
[manufactured solution](/methods/method-of-manufactured-solutions.md)
gives order $N$ for EC and $N+1$ for ES. Comparisons cite
[WALE](/methods/wale-model.md) LES by Hamzehloo et al., the
[dynamic Smagorinsky](/methods/smagorinsky-model.md) KEP-DGSEM of
[Flad & Gassner (2017)](/sources/flad-2017.md), Ranocha's
[kinetic-energy-preserving](/properties/kinetic-energy-preservation.md)
flux and the compound [law of the wall](/definitions/law-of-the-wall.md).

# Version read

Version of record (AIP, with a download cover page and a margin stamp of
26 October 2026; submitted 11 March 2025, accepted 22 April 2025, online
2 July 2025), 26 PDF pages (cover plus 075105-1 to 075105-25), all read;
equation pages (article pp. 3–8, 13–14, 17, 22–23) read visually because
the text layer garbles Greek symbols. Page 1 matches the metadata; no
identity issue. The citation label Alberti et al. (2025b) distinguishes it
from [Alberti et al. (2025)](/sources/alberti-2025-b.md). Equation,
figure, table and section numbers are those of this version.

# Key claims

Page-local symbols: $\boldsymbol Q$ the conservative variables;
$\mathcal E=-\rho s/(\gamma-1)$, $s=\ln(p\rho^{-\gamma})$, the
mathematical entropy and $\boldsymbol W=\partial\mathcal E/\partial\boldsymbol Q$
the entropy variables, $\boldsymbol W_h$ their $L_2$ projection (as on the
entropy page); $\sigma^{\mathcal E}_i=u_i\mathcal E$ the entropy flux and
$\psi_i=\rho u_i$ the entropy-flux potential; $a^{\mathrm{DEEB}}_K$ the
DEEB amplitude of element $K$ (the source's $\alpha_K$); $c_{\mathrm{BR2}}$,
$c_{\mathrm{BR2},w}$ the interior and wall BR2 penalties (the source's
$\eta_F$, $\eta_{F,w}$); $\beta_{\mathrm{up}}$ the upwind relaxation of
the biased Ismail–Roe flux; $\Lambda_K$ the largest convective eigenvalue;
$p^*$ the wall pressure; $M_n^-$ the wall-normal Mach number of the
interior state; $r_{\mathrm{DoF}}=N^{\mathrm{DNS}}_{\mathrm{DoF}}/N^{\mathrm{DG}}_{\mathrm{DoF}}$
the under-resolution ratio; $B_q=\dot q_w/(\rho_wc_pu_\tau T_w)$ the wall
heat-flux coefficient; $\langle T_c\rangle_\rho$ the Favre-averaged
centreline temperature; $M_\tau=u_\tau/c_w$.

1. In DG implicit LES the role of the SGS model is "left to the inbuilt numerical dissipation of the interface convective flux"; upwind-biased fluxes localize dissipation at high wavenumbers, so Riemann solvers act as a low-pass spatial filter (§I). **Stated**
2. With the entropy projection ($L_2$ projection of $\boldsymbol Q_h$ onto entropy variables, Eq. 8) plus the DEEB correction, the convective contribution is entropy conserving or stable whenever the numerical flux satisfies Tadmor's condition (Eq. 22), with no specific quadrature nodes or flux-splitting formulas (§I, §II A, Eq. 26). **Derived**
3. DEEB is "completely free from user-defined parameters, since the strength of the correction term is uniquely defined by the entropy balance"; the correction is spread over all modal degrees of freedom except the mean, preserving conservation, and is switched off when its denominator is below $10^{-14}$ (§II A 1, Eqs. 23–25). **Stated**
4. Unlike spectral vanishing viscosity, which acts only at high wavenumbers, the DEEB correction is "passive only at the first mode"; restricting it to higher modes reduced robustness in the authors' experience (§II A 1). **Stated**
5. The isothermal no-slip wall with mirrored velocity, extrapolated thermodynamics and the exact-Riemann wall pressure $p^*$ (Eqs. 28–29) yields a boundary entropy flux $(p^*-p^-)W^-_{1+i}n_{F,i}=\hat\sigma^{\mathcal E,-}_in_{F,i}$ that is always positive (Eq. 31), an entropy-stable wall (ESW); extrapolating the wall pressure ($p^*=p^-$, Ismail–Roe) gives zero, an entropy-conserving wall (ECW); the exactness of these relations holds only with DEEB (§II B). **Derived**
6. The ESW condition is parameter-free and is "the standard method used in our code ... following the original work of Bassi, even though it is not explicitly documented in [Bassi's] literature" (§II B). **Stated**
7. No formal entropy-stability proof of BR2 for Navier–Stokes is available; with the viscous matrix frozen to element-mean values, the BR2 entropy contribution is bounded by a sum of non-negative terms (generalized Young inequality, Eqs. C4–C5), and $c_{\mathrm{BR2}}$ multiplies an entropy source, so raising it raises entropy production, more so for larger interface jumps (App. C). **Derived** (under the frozen-matrix approximation)
8. Moderately under-resolved runs ($N=8$; $r_{\mathrm{DoF}}=9.4$–14.4 near the incompressible limit, 33.1–198.6 compressible; Tables I–II) reproduce the DNS mean velocity, Reynolds stresses and temperature; $\langle T_c\rangle_\rho=1.396$ (DNS 1.387 [38], 1.378 [39]) at $M_b=1.5$, $Re_\tau=222$; 1.377 (DNS 1.372) at $Re_\tau=500$; 1.367 (DNS 1.369) at $Re_\tau=1000$ (§III A 2, Figs. 1–4). **Shown**
9. $B_q$ is $N$-converged: $Re_\tau=222$: 0.0501 ($N=6$), 0.0503 ($N=8$) against 0.048 [38], 0.049 [39]; $Re_\tau=500$: 0.0432, 0.0434 against 0.042; $Re_\tau=1000$: 0.038, 0.039 against 0.038; $M_b=3$, $Re_\tau=450$: 0.121 ($N=6$), 0.136 ($N=8$) against 0.14 [38], 0.137 [39] (Table III). **Shown**
10. At $M_b=3$, $Re_\tau=450$ the DG profiles depart from the Modesti–Pirozzoli DNS beyond $y^+\approx45$ in velocity and after the first cell in temperature, which the authors attribute to power-law against Sutherland viscosity at bulk temperatures more than twice the wall value; DG $\langle T_c\rangle_\rho=2.467$ ($N=8$) against 2.490 [39] (power law) and 2.570 [38] (Sutherland) (§III A 2, Fig. 5). **Shown** (attribution **Stated**)
11. The $M_b=3$ results are insensitive to halving CFL, to $N=8\to9$, to removing the entropy correction at $N=9$, and to the streamwise length ($4\pi$ against $6\pi$) (Figs. 6–7). **Shown**
12. "The baseline DG framework in conservative variables without DEEB is not able to run the compressible channel flow cases" (§III A 2). **Stated** (no figure)
13. Under the Trettel–Larsson mapping, $M_b=1.5$/$Re_\tau=222$ and $M_b=3$/$Re_\tau=450$ collapse on the incompressible $Re_\tau=180$ DNS, $M_b=1.5$/$Re_\tau=1000$ corresponds to $Re_\tau=590$ and $Re_\tau=500$ to about $Re_\tau=350$ (Fig. 8, §III A 2); earlier the text says $M_b=3$, $Re=450$ "corresponds to an incompressible simulation at $Re=140$" (§III A). **Shown**
14. Severely under-resolved near-incompressible implicit LES ($N=6$; $8\times8\times6$, $8\times8\times8$, $12\times12\times12$ elements; $r_{\mathrm{DoF}}=65.5$, 220.6, 261.0, Table IV) with $c_{\mathrm{BR2}}=1$, $c_{\mathrm{BR2},w}=8$: the EC Ismail–Roe flux "significantly enhances the accuracy" over the ES Godunov flux; the ES flux always over-shears the fluctuations in the viscous layer and overshoots the mean velocity, under-estimating $\langle u'v'\rangle$ (Figs. 9–10). **Shown**
15. At $Re_\tau=180$, halving the first-cell height ($\Delta y^+\approx2$) or refining to 8 wall-normal elements ($\Delta y^+\approx3$) changes the EC solution (the location of the solution jump in the viscous layer moves; $\langle u'v'\rangle$ over-estimated from $y^+\approx7$ in one case, under-estimated up to $y^+\approx12$ in the other) but not the ES solution (Figs. 11–12). **Shown**
16. Degree-of-freedom comparisons: about half those of Flad et al. [2, 44] at $Re_\tau=590$; De Wiart et al. [24] at $Re_\tau=395$, 590 used 8 and 9 times more; Bergmann et al. [43] at $Re_\tau=395$ ($N=7$, $8\times8\times8$, split-form DGSEM) about 6 times more, with "much more accurate" results here (§III A 3). **Stated** (the literature figures are not reproduced)
17. Raising $c_{\mathrm{BR2}}\in\{1,3,5\}$ at $Re_\tau=395$ shifts the mean velocity upward (more dissipation) and lowers the shear stress for $y^+\le20$, inside the first cell; the effect is larger for EC than ES because the centred EC flux produces larger jumps (Figs. 13–14). **Shown**
18. Too much near-wall dissipation shears out the turbulent stresses and the mean flow approaches DNS "from above"; too little (over-predicted buffer-layer fluctuations) gives an under-predicted mean velocity approaching DNS "from below" (§III A 3 a, §IV). **Shown** (interpretation **Stated**)
19. With uniform $c_{\mathrm{BR2}}=3$ at $Re_\tau=395$ and the EC interior flux, the ECW wall gives a velocity profile that "abundantly undershoots" DNS and the ESW wall one "almost coincident" with DNS (Fig. 15). **Shown**
20. Severely under-resolved compressible implicit LES ($N=8$; $r_{\mathrm{DoF}}=176.0$, 265.6, 625.8, 1412.3, Table V; baseline $c_{\mathrm{BR2}}=5$): contrary to the incompressible case, the ES Godunov flux is best and the EC flux systematically under-predicts the mean velocity; $c_{\mathrm{BR2}}=1$ mitigates the excess dissipation of the standard ES scheme (Figs. 16–17). **Shown**
21. At $M_b=3$ the pure EC flux "results in an abrupt crash"; the upwind-biased Ismail–Roe flux (Eq. 40) with $\beta_{\mathrm{up}}=0.3$ runs but still needs DEEB to complete, and under-predicts the velocity with excessive $\langle u'v'\rangle$; the ES flux gets "very close" to the DG reference on $16\times16\times8$ (Figs. 18–19). **Shown**
22. On $6\times6\times6$ ($Re_\tau=500$, $r_{\mathrm{DoF}}=637.4$) and $8\times8\times8$ ($Re_\tau=1000$, $r_{\mathrm{DoF}}=2100$) at $N=8$, changing $c_{\mathrm{BR2}}$ alone gives no visible improvement, whereas the upwind-biased EC flux ($\beta_{\mathrm{up}}=0.1$ at $Re_\tau=500$; 1 against 0.3 at $Re_\tau=1000$) improves the mean profile; Ranocha's EC and kinetic-energy-preserving flux agrees with the Ismail–Roe EC flux (Figs. 20–21). **Shown**
23. Ranocha's kinetic-energy-preserving flux "does not discretely ensure this property on the adopted DG modal discretization" (§III A 3 c). **Stated**
24. The EC flux converges at rate $N$, the ES flux at $N+1$ (manufactured solution, $Re=100$, $N\in\{3,4\}$); $N+1$ is retained for $c_{\mathrm{BR2}}\in\{1,3,5\}$ at $N=3$ (App. B, Figs. 22–23). **Shown**
25. Cost: the DEEB correction is below 1% of the CPU time for $N\ge2$, the entropy projection 2.5% ($N=1$) to 6.6% ($N=9$) (Table VI); the total overhead "never exceeds 7%" (App. A). **Shown** (hardware not stated)
26. An EC, upwind-free convective discretization run for high-Mach channel implicit LES "has not been reported for other DG solvers in the literature, at least to the authors' knowledge" (§III A 3). **Stated**
27. The implicit-LES performance of the baseline scheme "should be fully understood before isolating any potentially beneficial effect of physics-inspired subgrid-scale models"; the modal approach is "at least comparable" in robustness to nodal variants such as DGSEM without ad hoc property-preserving operators, and handles any element type and quadrature (§I, §IV). **Stated**

The scheme in registry notation. The DEEB term added to the semi-discrete
system of element $K$ (Eq. 23) is
$a^{\mathrm{DEEB}}_K\int_K\phi_l\bar W_\kappa\,d\Omega/\int_K\bar W_s\bar W_s\,d\Omega$,
with $\bar{\boldsymbol W}_h=\boldsymbol W_h-\{\boldsymbol W_h\}_e$ the
deviation from the element average and
$$a^{\mathrm{DEEB}}_K=\int_K\Big(\frac{\partial\boldsymbol W_h}{\partial x_i}\Big)^{\mathsf T}\boldsymbol F_{c,i}(\boldsymbol W_h)\,d\Omega-\sum_{F\in\mathcal F_K}\int_F\psi_i(\boldsymbol W_h)n_{F,i}\,d\sigma$$
(Eq. 25). Tadmor's condition (Eq. 22) reads
$[\![\boldsymbol W_h]\!]^{\mathsf T}\hat{\boldsymbol F}_c-[\![\psi_i]\!]n_{F,i}\ge0$.
The ESW wall pressure is
$p^*=p^-\big[1+\gamma M_n^-\big(\tfrac{\gamma-1}4M_n^-+\sqrt{1+\tfrac{(\gamma+1)^2}{16}(M_n^-)^2}\big)\big]$
for $u_n>0$ and $p^*=p^-\big[1+\tfrac{\gamma-1}2M_n^-\big]^{2\gamma/(\gamma-1)}$
otherwise (Eqs. 28–29). The biased flux adds
$-\beta_{\mathrm{up}}\tfrac12\max(|\Lambda^+_K|,|\Lambda^-_K|)[\![\boldsymbol Q]\!]$
to the Ismail–Roe flux (Eq. 40), "a naive implementation of a simple
Rusanov-like upwind bias". The viscous stress is $\sigma_{ij}$, the
viscosity a power law $\mu\propto T^{\beta_\mu}$; time stepping is a
five-stage fourth-order SSP Runge–Kutta scheme (CFL value not printed);
averages are Favre averages $\langle\cdot\rangle_\rho$, with no
significant difference from Reynolds averages. The Trettel–Larsson
velocity is
$U^+_{TL}=\int_0^{u^+}\sqrt{\langle\rho\rangle/\rho_w}\,[1+\tfrac{y}{2\langle\rho\rangle}\tfrac{d\langle\rho\rangle}{dy}-\tfrac{y}{\langle\mu\rangle}\tfrac{d\langle\mu\rangle}{dy}]\,du^+$
(Eq. 39); first-cell heights $\Delta y^+$ are divided by the cube root of
the degrees of freedom per element.

# Printed slips

- **Figs. 6 and 7 captions:** "Mean velocity profile for the incompressible channel flows at $M_b=3$ and $Re_\tau=450$".
- **Fig. 3 caption:** "$20\times20\times12$ mesh decomposition", while Table II gives $20\times20\times10$ for $M_b=1.5$, $Re_\tau=500$.
- **Tables I and IV, $Re_\tau=180$:** *(compiler check, not in the sources: $16\cdot16\cdot8$ elements with 165 modes at $N=8$ give 337 920 DG degrees of freedom, so $r_{\mathrm{DoF}}=9.4$ implies about $3.18\times10^6$ DNS degrees of freedom, while Table IV, 32 256 at $r_{\mathrm{DoF}}=65.5$, implies about $2.11\times10^6$; for the other cases the two tables imply the same DNS count within 1%.)*
- **§III A 3 c:** for $M_b=3$ "the solution employs approximately 1/1000 of the DoF of the reference DNS", while Table V gives $r_{\mathrm{DoF}}=1412.3$.
- **Hamzehloo et al.'s case** is quoted at $Re_\tau=215$ (§I) and as "$M_b=1.5$ and $Re=222$" (§III A).
- **§III A:** the $M_b=3$, $Re=450$ case "corresponds to an incompressible simulation at $Re=140$", while Fig. 8(a) and its text give the incompressible $Re_\tau=180$.
- **Table III:** $B_q$ at $M_b=3$ changes from 0.121 ($N=6$) to 0.136 ($N=8$) while the text speaks of "negligible variation with the increase in the polynomial degree".
- **Ref. 72:** authors printed "S. J. Ruuth, R. J. Spiteri, and J. Ruuth".
- **Table VII:** $a^\psi_{1,2}$ for $P$ printed "−250 00".
- **Eq. (C1):** surface sum over "$F\in\mathcal K_h$" (elsewhere $\mathcal F_h$).
- **Signs:** *(compiler check, not in the sources: with the stated $[\![\circ]\!]=\circ^+-\circ^-$ and $\boldsymbol n_F$ from $-$ to $+$ (Eqs. 7, 17), element-wise integration by parts gives a face term $-\sum_F\int_F[\![\phi]\!]\hat F\,d\sigma$, while Eq. (9) prints $+$, and the last equality of Eq. (26) needs the opposite sign; Eqs. (9), (22), (26) agree with each other if the jump is read as $\circ^--\circ^+$.)*
- **Ref. 78** (S. Gottlieb 2005) is listed but not cited in the text.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $x_1$, $x_2$, $x_3$ | $x$, $z$, $y$ | **wall-normal $x_3$ becomes $y$** |
| $p$ (degree) | $N$ | **collision** with the pressure $p$ |
| $N_{DoF}=\prod_m(p+m)/m$ | $N_{\mathrm{dof}}$ (registry §11) | per element and variable, full $\mathbb P^N$ space |
| $\mathbf q$, $\mathbf v$, $\mathbf v_h$ | $\boldsymbol Q$, $\boldsymbol W$, $\boldsymbol W_h$ (page-local) | **collision** of $\mathbf v$ with the velocity |
| $\mathscr S$, $\sigma_i$, $\theta$, $\psi_i$ | $\mathcal E$, $\sigma^{\mathcal E}_i$, $\theta$, $\psi_i$ (page-local) | entropy, entropy flux and potentials; **collision** of $\sigma_i$ with the viscous stress |
| $\tau_{ij}=\mu(\partial_ju_i+\partial_iu_j)+\lambda\partial_ku_k\delta_{ij}$, $\lambda=-\tfrac23\mu$ | $\sigma_{ij}$ | **collision:** viscous stress, not the SGS stress |
| $\tau_{11}$, $\tau_{13}$, … (figures) | $\langle u'u'\rangle$, $\langle u'v'\rangle$, … | Reynolds stresses in inner scaling |
| $[\![\circ]\!]$, $\{\circ\}$ (face) | $[\![\cdot]\!]$, $\{\!\{\cdot\}\!\}$ | jump and arithmetic mean |
| $\{\phi\}=\langle\rho\phi\rangle/\langle\rho\rangle$ | $\langle\phi\rangle_\rho$ | **collision** with the face mean |
| $\mathbf v_{h,0}$ | $\{\boldsymbol W_h\}_e$ | element average |
| $\alpha_K$ | $a^{\mathrm{DEEB}}_K$ (page-local) | **collision** with the DG blending $\alpha$ |
| $\eta_F$, $\eta_{F,w}$ | $c_{\mathrm{BR2}}$, $c_{\mathrm{BR2},w}$ (page-local) | **collision** with the Kolmogorov length $\eta$ |
| $\beta$ (viscosity), $\beta$ (Eq. 40) | $\beta_\mu$, $\beta_{\mathrm{up}}$ (page-local) | two meanings in the source |
| $\lambda_K$ | $\Lambda_K$ (page-local) | **collision** with the Taylor microscale |
| $\hat k$, $\zeta=\hat k/c_p$ | (page-local) | conductivity and thermal diffusivity |
| $u_\tau$, $u^*_\tau$, $Re_\tau$, $Re^*_\tau$, $M^*_\tau$ | $u_\tau$, (page-local), $Re_\tau$ | $Re_\tau$ on the half-height |
| $M_b=u_b/c_w$ | $M_b$ | bulk Mach number on the wall sound speed |
| $u^+_{tl}$ | $U^+_{TL}$ | as on the velocity-transformation page |
| $\Delta x^+_3$, $r$ | $\Delta y^+$ (sub-cell scaled), $r_{\mathrm{DoF}}$ (page-local) | |
| $B_q$, $\{T_c\}$ | $B_q$, $\langle T_c\rangle_\rho$ (page-local) | |

# Reference list

81 printed references, numbered (superscript) AIP style with titles. The
list is merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug. Ref. 2 is the ingested
[Flad & Gassner (2017)](/sources/flad-2017.md). Ref. 64 (Huang, Wang, Wu
& Xu, wall models in spectral/hp implicit LES, Phys. Fluids 34:105129)
shares its key with the ingested [Huang et al. (2022)](/sources/huang-2022.md),
a different work, and is keyed `huang-2022-c`. Ref. 72 is entered with
its author list as printed; AIAA papers (refs. 8, 52, 57, 66) are
reports; refs. 46 and 60 print "et al."; ref. 79 is a proceedings
chapter. No item is unparseable.

# Pages created or updated

Chunk 15 (2026-10-28). This source is cited on:

- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Compressible velocity transformations](/definitions/compressible-velocity-transformation.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Jump-penalty stabilization of high-order methods](/methods/jump-penalty-stabilization.md)
- [Method of manufactured solutions](/methods/method-of-manufactured-solutions.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
- [WALE model](/methods/wale-model.md)
- [Entropy conservation and entropy stability](/properties/entropy-conservation.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
