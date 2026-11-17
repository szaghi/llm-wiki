---
type: Source
title: "Pirozzoli (2011a) — Numerical methods for high-speed flows"
description: "Annual Review of finite-difference methods for DNS and LES of compressible turbulence with shocks: kinetic-energy- and entropy-consistent split forms for smooth flow, classical shock capturing (TVD, ENO, WENO), hybrid schemes and nonlinear filters driven by shock sensors, artificial viscosity (JST, localized artificial diffusivity) and subgrid regularization, the first-order accuracy of shock capturing behind moving shocks, and a recommendation of central split forms hybridized with WENO through a Ducros-type sensor."
resource: "doi:10.1146/annurev-fluid-122109-160718"
source_kind: paper
authors: [Pirozzoli S.]
year: 2011
venue: "Annu. Rev. Fluid Mech. 43:163-194"
local_file: "/home/stefano/papers/mosaic/weno-teno/2011_Crossref_Annual_Review_of_Fluid_Mechanics_Pirozzoli_Numerical_Methods_for_High-Speed_Flows.pdf"
tags: [review, low-dissipation, shock-capturing, weno, artificial-viscosity, turbulence, central-scheme]
timestamp: 2026-11-17T08:44:05Z
---

# Summary

Pirozzoli (2011a) reviews the finite-difference methods used for direct numerical simulation (DNS)
and large-eddy simulation (LES) of compressible turbulence with shocks. The review sorts them into two
families. **Methods for smooth flows** (§2) are upwinding ([flux vector splitting](/methods/flux-vector-splitting.md), Godunov-type
[Roe](/methods/roe-riemann-solver.md) and [ADER](/methods/ader-scheme.md) fluxes), filtering, the
energy-consistent [split convective forms](/methods/split-convective-forms.md) of Feiereisen, Blaisdell
and Kennedy–Gruber, and entropy-consistent schemes (Tadmor's
[entropy-conservative flux](/methods/entropy-conservative-flux.md), Gerritsen–Olsson entropy splitting,
Honein–Moin); upwinding and filtering stabilize by dissipation, while the energy- and entropy-consistent
schemes seek nonlinear stability without it. A zero-viscosity isotropic-turbulence test (§2.5, Fig. 1) compares them.
**Methods for shocked flows** add "some (possibly not excessive)" dissipation: monotone,
[TVD](/definitions/total-variation-diminishing.md), [ENO](/methods/eno-reconstruction.md),
[WENO](/methods/weno-js-reconstruction.md) and [WCNS](/methods/weighted-compact-nonlinear-scheme.md);
[hybrid schemes](/methods/hybrid-weno.md) and nonlinear (characteristic-based) filters switched by
[shock sensors](/definitions/troubled-cell-indicator.md), among them the
[Ducros sensor](/definitions/ducros-shock-sensor.md);
[artificial viscosity](/methods/artificial-viscosity.md) (von Neumann–Richtmyer,
Jameson–Schmidt–Turkel, spectral vanishing viscosity and the
[localized artificial diffusivity](/methods/localized-artificial-diffusivity.md) of Cook & Cabot); and
regularization by approximate-deconvolution subgrid models.

The review states the limits of shock capturing: Fourier analysis does not apply, the nonlinear WENO
weights spoil the spectral resolution of the linear scheme, and every capturing scheme is first order
behind moving shocks and oscillates behind slow ones
([order of accuracy behind shocks](/results/order-of-accuracy-behind-shocks.md)). It closes with
recommendations: central explicit split forms in locally conservative form for smooth flow, WENO for
DNS and LES "only in hybrid form" with a sensor-marked and padded shock region, the Ducros sensor with
case-by-case tuning, nonlinear artificial viscosity as "an attractive alternative", and local
conservation always. Applications (§5) cover shock/isotropic-turbulence interaction, shock/boundary-layer
interaction, a jet in supersonic crossflow and Richtmyer–Meshkov instability.

# Version read

Version of record from annualreviews.org ("Downloaded ... by Ball State University on 04/21/13"): 34 PDF
pages, the 32 article pages 163–194 plus the two pages v–vi of the volume's table of contents. All
article pages read. The text layer drops several Greek and script glyphs ($\Theta$ of Eq. (29),
$\Psi$ of Eq. (28), $\epsilon$, the indices $\ell$, the filter caret of Eq. (34), $\mathcal G_1$); the
equations of PDF pp. 11 and 16 (Eqs. (23)–(26), (30)–(34)) were checked on renders for this page, the
others against the reader's notes, which re-read every equation from renders at 150–200 dpi. First published online as a Review in Advance on 13 August 2010; no received or
accepted dates are printed. Page 1 matches the Crossref record and the DOI printed there. Bundle label:
Pirozzoli (2011a), distinct from [Pirozzoli (2011b)](/sources/pirozzoli-2011-b.md) (the JCP paper on
curvilinear coordinates). A review: its claims are the author's statements and recollections of others'
results, cited as such; the only computations it shows are Figs. 1, 3 and 4.

# Key claims

Registry notation (see Notation map). Claims grouped by section.

**§1 Governing equations.**

1. The Euler fluxes are homogeneous of degree one in the conserved variables, $f^{(d)}=A^{(d)}u$, "a property that is useful for the design of upwind methods based on the flux vector splitting technique (Steger & Warming 1981)" (§1). **Stated**
2. For smooth flow the total kinetic energy changes only by boundary fluxes and pressure work, $\frac{d}{dt}\int_V\kappa\,dV=-\oint_{\partial V}(\kappa+p)\,v\cdot n\,dS+\int_Vp\,\nabla\cdot v\,dV$; the convective terms "do not cause any net variation" (Eq. (5)). **Derived** (standard)
3. For smooth flow $\frac{d}{dt}\int_V\rho g(s)\,dV+\oint_{\partial V}\rho g(s)\,v\cdot n\,dS=0$ for any differentiable $g$ of $s=\log(p\rho^{-\gamma})$ (Harten 1983b, Eq. (6)); entropy variables symmetrize the Euler equations, the symmetrized form gives the energy estimate (8), and Tadmor (1984) showed that (8) implies (6); for $g(s)=\beta_{\mathrm{ES}}\exp\big(s/(\beta_{\mathrm{ES}}(\gamma-1))\big)$, $u$ and $f^{(d)}$ are homogeneous of degree $\beta_{\mathrm{ES}}$ in the entropy variables (Eqs. (7)–(9)). **Stated** (recalled)
4. Shocklets in turbulence occur with velocity fluctuations of the order of the sound speed, but "their frequency and strength are not such to severely threaten the robustness and accuracy of numerical algorithms", and their thickness scales on the Kolmogorov length, so DNS can resolve them (§1, after Lee et al. 1991 and Samtaney et al. 2001). **Stated**

**§2 Methods for smooth flows.**

5. For a compact scheme $\sum_ma_m(\delta_xf)_{i+m}=\frac1{\Delta x}\sum_lb_lf_{i+l}$ (Lele 1992; page-local $a_m$, $b_l$, $(\delta_xf)_i$) the implied numerical flux satisfies $\sum_ma_m\hat f_{i+1/2+m}=\sum_lc_lf_{i+l}$ with a recurrence for $c_l$ (Eqs. (11)–(13); misprinted, see Printed slips). Explicit fluxes with $\hat f(u,\dots,u)=f(u)$ give global conservation by telescoping and satisfy the hypotheses of the Lax–Wendroff theorem (§2). **Derived**
6. Standard central discretizations of high-Reynolds-number turbulence are unstable through aliasing of the nonlinear terms (Phillips 1959), a failure to preserve quadratic invariants (Lilly 1965, Orlandi 2000); "it is usually safer to revert to alternative discretization techniques capable of ensuring stability in the inviscid limit" (§2). **Stated**
7. Upwinding damps the highest wavenumbers; high-order upwind schemes have worked for DNS of shock-free turbulence, but upwind dissipation "can be harmful for LES" (Park et al. 2004) (§2.1). Filtering, like upwinding, "implies artificial energy draining that adds to the physical energy draining caused by molecular viscosity" (§2.2). **Stated**
8. Split forms (Eqs. (18)–(20)): the Feiereisen form, "often improperly referred to as skew-symmetric", gives semi-discrete kinetic-energy preservation when mass and momentum are written in it and the difference operators are summation-by-parts, which holds for periodic central explicit and compact operators of any order (Honein & Moin 2004; Strand 1994; Mansour et al. 1979); the Blaisdell form minimizes aliasing; the Kennedy–Gruber form with weights $\alpha_{\mathrm{KG}}$, $\beta_{\mathrm{KG}}$ "leads to semidiscrete energy conservation in the case $\alpha=\beta=1/4$" (§2.3). **Stated**
9. Ducros et al. (2000) showed local conservation of the Feiereisen and Blaisdell forms with explicit central formulas up to sixth order; Pirozzoli (2010) proved it at any order and gave fluxes for the Kennedy–Gruber form; "Apparently, compact derivative approximations applied to the split form of the convective terms do not guarantee local discrete conservation" (§2.3). **Stated**
10. Tadmor's (1987) second-order flux $f^{\mathrm{ec}}_{i+1/2}=\int_0^1f\big(u(w_i+\xi(w_{i+1}-w_i))\big)\,d\xi$ satisfies Eq. (6) discretely but is "rather expensive" (entropy variables of both states and a quadrature) (Eq. (21)). The Gerritsen–Olsson splitting $\partial_xf=\frac{\beta_{\mathrm{ES}}}{\beta_{\mathrm{ES}}+1}\partial_xf+\frac1{\beta_{\mathrm{ES}}+1}\mathsf B_{\mathrm H}\partial_xw$ with SBP operators gives the SHOEC schemes; $\beta_{\mathrm{ES}}\approx4$ for compressible turbulence (Sandham et al. 2002), $\approx2$ for zero-viscosity isotropic turbulence (Honein & Moin 2004); entropy variables cost transcendental operations (Eq. (22), §2.4). **Stated**
11. Zero-viscosity isotropic turbulence ($32^3$, $E(k)\sim(k/k_0)^4\exp[-2(k/k_0)^2]$, $k_0=6$, third-order SSP Runge–Kutta, $M_{t,0}=0.07$ and $0.3$; Fig. 1): the divergence-form central schemes D2 and D6 diverge in less than one eddy-turnover time "regardless of the order of accuracy"; seventh-order upwinding (D7) avoids divergence but dissipates most of the kinetic energy by 10 turnover times; the split forms S6 (Blaisdell) and K6 (Kennedy–Gruber) conserve kinetic energy and entropy at $0.07$ with "spurious growth of density fluctuations"; Tadmor's T2 has larger long-time errors without diverging; the Honein–Moin H6 "succeeds in correctly predicting the limiting inviscid behavior"; at $0.3$ all fail at large times except K6 and T2 (§2.5). **Shown**

**§3 Methods for shocked flows.**

12. Shock fitting is often more accurate but "only feasible in cases in which the shock topology is extremely simple and no shock wave forms during the calculation"; the review treats shock capturing only (§3). **Stated**
13. Design properties of shock capturing: monotonicity preservation, TVD and monotonicity of entropy solutions; TVD schemes converge to weak solutions, monotone schemes to the entropy solution, monotone schemes are at most first order, and TVD schemes lose accuracy at smooth and non-smooth extrema (§3.1). **Stated** (recalled)
14. "ENO reconstructions of order $r$ guarantee that $TV(u^{n+1})\le TV(u^n)+O(\Delta x^r)$, which implies uniform boundedness of the total variation" (§3.1); Harten et al. (1987a) state the bound as a requirement and, for the scheme, a conjecture ([ENO property](/definitions/eno-property.md)). Free stencil adaptation spoils steady convergence and accuracy (Rogerson & Meiburg 1990), cured by biasing toward the central stencil (Shu 1990). **Stated**
15. WENO in the $2r$-point form with $r+1$ candidates, $\alpha_k=d_k/(\epsilon+\beta_k)^2$; Jiang & Shu set $d_r=0$ (order $2r-1$); Weirs & Candler keep the central stencil with $\beta_r=\max_k\beta_k$ (Eqs. (23)–(26), Fig. 2). Provable properties are "limited to the scalar case" (convergence for smooth solutions; discrete shock profiles of the third-order scheme) (§3.1). **Stated**
16. WENO schemes are "highly accurate and quite robust" but "computationally expensive, mostly because of the large number of floating point operations required for the evaluation of the smoothness measurements"; "spectral-like resolution is never achieved owing to the noxious effect of the nonlinear weights, unless the weights are locally frozen in smooth regions" (Hill & Pullin 2004; Taylor et al. 2007) (§3.1). **Stated** (author's experience)
17. Lax–Liu configuration 13 at $\Delta x=\Delta y=1/1200$, SSP-RK3 at Courant number 0.6: a second-order TVD scheme with van Leer limiter, WENO5 and WENO7 capture the shock pattern "without significant spurious oscillations" (p. 174); WENO rolls up the slip line more finely, WENO7 forms secondary vortex cores; the hybrid (WENO at $x_{i+1/2}$ and two nodes on each side wherever $\lvert\rho_{i+1}-\rho_i\rvert\ge0.2$) gives additional discrete vortices but "some spurious wiggles near shocks", at about 50% less cost than WENO7 (§3.1–3.2, Fig. 3). **Shown**
18. Hybrid lineage: Lee et al.'s a-priori switch (ENO over 12 points on each side of the mean shock), Adams & Shariff's adaptive compact-upwind/ENO hybrid with buffer cells, Pirozzoli's (2002) conservative compact-upwind/WENO7 hybrid, Hill & Pullin's sensor $\lambda_{\mathrm{HP}}=\max_k\beta_k/(\min_k\beta_k+\epsilon)$ (§3.2). Larsson & Gustafsson (2008): two separately stable schemes can couple unstably, but if either is dissipative the coupled system is strongly stable. Smooth blending functions "do not add much to the stability and accuracy" (author's experience) (§3.2). **Stated**
19. Nonlinear filtering (Yee et al. 1999): $\frac{du_i}{dt}=-(\delta_xf)_i-\frac1{\Delta x}(\hat f^*_{i+1/2}-\hat f^*_{i-1/2})$, $\hat f^*_{i+1/2}=\mathsf k_{\mathrm Y}\theta_{\mathrm{AC},i+1/2}\hat d^{\mathrm{TVD}}_{i+1/2}$, applied per characteristic field; it can be applied once per time step, "with substantial savings in terms of CPU time (but with some loss in terms of robustness)". Ducros et al. (1999) replaced the TVD flux by the Jameson–Schmidt–Turkel flux and Harten's switch by the product of Jameson's sensor and $\Phi_{\mathrm D}=\frac{(\nabla\cdot v)^2}{(\nabla\cdot v)^2+\lvert\nabla\times v\rvert^2+\epsilon_{\mathrm D}}$ (Eqs. (27)–(29)). (The original, [Ducros et al. (1999)](/sources/ducros-1999.md) §3, Eq. (8), puts the JST dissipation inside the numerical flux of a four-stage Runge–Kutta finite-volume scheme with a scalar dissipation model and mentions neither filtering nor Harten's switch; see the Qualifications of [Ducros shock sensor](/definitions/ducros-shock-sensor.md).) **Stated**
20. On an instantaneous transonic shock/boundary-layer DNS field, with thresholds chosen for similar shock pictures, the original Ducros sensor "does not perform properly outside of the wall layer (where $\nabla\times v\approx0$), due to excessive sensitivity to dilatational fluctuations" (**Stated**); with $\epsilon_{\mathrm D}=(v_\infty/\delta_0)^2$ — the review's "modified Ducros sensor", still the squared ratio — it isolates genuine shocks, whereas the Jameson, Hill–Pullin and Visbal–Gaitonde sensors (on pressure) also mark vortical regions (§3.2, Fig. 4). **Shown** (Fig. 4)
21. Artificial viscosity: von Neumann–Richtmyer $\mu^*=c_\mu\rho\Delta x^2\lvert\partial_xv\rvert$; the Jameson–Schmidt–Turkel flux $\hat f_{i+1/2}=\hat f^{\mathrm C}_{i+1/2}-\mathcal D_{i+1/2}$, $\mathcal D_{i+1/2}=a_{i+1/2}[\varepsilon_{2,i+1/2}(u_{i+1}-u_i)-\varepsilon_{4,i+1/2}(u_{i+2}-3u_{i+1}+3u_i-u_{i-1})]$, $\varepsilon_{2,i+1/2}=k_2\varphi_{\mathrm J,i+1/2}$, $\varepsilon_{4,i+1/2}=\max(0,k_4-\varepsilon_{2,i+1/2})$, $\varphi_{\mathrm J,i+1/2}=\max(\varphi_{\mathrm J,i},\varphi_{\mathrm J,i+1})$, $k_2\approx1$, $k_4\approx0.01$–$0.05$, with $a_{i+1/2}$ the spectral radius at the Roe average and $\varphi_{\mathrm J}$ applied to pressure for Euler (Eqs. (30)–(32)). **Stated**
22. Localized artificial diffusivity (Cook & Cabot 2004, 2005): artificial shear and bulk viscosities driven by $\rho\Delta^{2(r_{\mathrm L}+1)}\lvert\widehat{\nabla^{2r_{\mathrm L}}\mathsf S}\rvert$, common constants $r_{\mathrm L}=2$, $c^{(2)}_\beta=1$, $c^{(2)}_\mu=0.002$; the bulk term captures shocks "without affecting the vorticity field"; corrections of Mani et al. (2009) and Bhagatwala & Lele (2009) against damping of resolved acoustics (Eqs. (33)–(34), §3.3). **Stated**
23. Adams & Stolz (2002): approximate deconvolution with a relaxation term $-\chi(\hat u-\mathcal F_2\star\hat u)$ regularizes shocks; $\chi$ "apparently cannot be established a priori" (Eqs. (35)–(37), §3.4). **Stated**
24. Fourier analysis does not apply to nonlinear schemes; the frozen-weight transfer function guided optimized WENO, but "the nonlinear features have a dramatic impact": W7 is "substantially poorer (in terms of increased numerical dissipation)" than its linearized D7 (§3.5, Fig. 1). **Shown** (one test)
25. "Even (nominally) uniformly high-order schemes yield first-order accurate solutions downstream of moving shocks, mainly because shocks have zero measure, and therefore their location is only known to $O(\Delta x)$" (Casper & Carpenter 1998, Engquist & Sjögreen 1998); spurious post-shock oscillations, especially behind slowly moving shocks (Arora & Roe 1997), are "apparently unavoidable" without subcell resolution or shock fitting (§3.5; Summary 5). **Stated** (recalled)

**§4 Further topics.**

26. Finite differences extend to smooth curvilinear meshes through the strong conservation form; immersed boundaries are promising but have few compressible applications; finite-volume dimensional splitting has second-order errors unless transverse quadratures are used, but the error "is usually small" in practice; DG and spectral volume are "too demanding currently in terms of memory requirements for large-scale turbulence computations"; ADER and $P_NP_M$ schemes are recalled (§4.1). **Stated**
27. SSP Runge–Kutta is argued to be safer with shocks (Shu 1997), but "standard Runge-Kutta time integration will work out just as fine for most typical DNS and LES applications" (§4.2). **Stated** (author's experience)
28. Viscous terms are better discretized as $\mu\partial^2_xu+\partial_x\mu\,\partial_xu$ with a dedicated second-derivative operator, which avoids the odd–even decoupling of repeated first derivatives (Eq. (38), §4.4). **Stated**

**§6 Conclusions, Summary Points, Future Issues.**

29. Finite differences are preferable for large-scale computations on uniform Cartesian or smooth curvilinear meshes; central explicit split forms are efficient, nonlinearly stable and locally conservative, and the Kennedy–Gruber variant "seems to be promising" for strong density variations (§6; Summary 3–4). **Stated**
30. WENO schemes "seem to have superseded other shock-capturing methods in the past decade" but are CPU intensive and over-dissipative in smooth zones, so for LES and DNS they are suggested "only in hybrid form"; the Ducros sensor "was found to perform reasonably well in many shock/turbulence interaction problems, particularly with some minor case-by-case modification and tuning of the threshold value"; best practice is to mark critical nodes and pad enough nodes that the nondissipative stencil does not cross shocked zones (§6; Summary 6–8). **Stated**
31. Nonlinear artificial viscosity is "an attractive alternative to hybrid-WENO schemes", but "further testing is required to demonstrate comparable reliability to WENO" (§6; Summary 9). **Stated**
32. Local conservation is always encouraged: telescoping, the Lax–Wendroff theorem, "no extra cost", fluxes exist for energy- and entropy-consistent schemes, and hybridization with conservative shock capturing is "more natural" (§6). **Stated**
33. Open issues: global first order and post-shock oscillations in unsteady problems; no systematic quantitative analysis of hybrid coupling; no comparative efficiency analysis (CPU cost for a given error) for shock problems; no efficient low-dissipation methods on unstructured meshes beyond the second-order scheme of Subbareddy & Candler (2009) (§6; Future Issues 1–5). **Stated**

# Printed slips

- **Eq. (13).** The implied-flux recurrence is printed $c_{-L+1}=-a_{-L}$, $c_\ell=c_{\ell-1}-a_{\ell-1}$. *(Compiler check, not in the source: substituting the flux form (12)–(13) into Eq. (11) gives $c_k-c_{k+1}=b_k$, hence $c_{-n_b+1}=-b_{-n_b}$, $c_l=c_{l-1}-b_{l-1}$; the right-hand-side coefficients $b$ of Eq. (11), not the left-hand $a$.)*
- **Eq. (26).** The inner sum of the smoothness indicator runs from $n=1$ to $L-1$, which leaves out the first point $f_{j-L+1+\ell}$ of the $L$-point substencil; the Jiang–Shu indicators use all $L$ values ($n=0$).
- **Eq. (34).** The bulk viscosity is printed $\beta=c^r_\beta\eta_r$ while Eq. (33) calls it $\beta^*$; the next sentence says Mani et al. replaced $S$ by $u_{k,k}$ "in the definition of $c^r_\beta$" and set "$c^r_\beta$ to zero" in expansions, where the change is to the driver of $\beta^*$.
- **§3.4:** "The modified Equation 34 is then discretized through high-order compact differencing" refers to the Adams–Stolz equation, Eq. (35).
- **§5 (p. 184):** "conservative sixth-order central discretization of the split convective form given in Equation 34"; Eq. (34) is the LAD coefficient, the split forms are Eqs. (18)–(20).
- **Eq. (36)** prints $\mathcal G_1=\partial_xf(\hat u)-\partial_xf(\tilde u)$ for the effect of the computed scales on the filtered field; for an equation in the filtered variable the second term would carry the primary filter. Not checked against Adams & Stolz; recorded as printed.
- **Fig. 1 caption vs §2.4.** T2 is "the second-order entropy-conserving scheme of Tadmor (1984)" in the caption, while the text attributes the flux of Eq. (21) to Tadmor (1987); the caption's "$(\beta=4)$" for T2 is not explained in the text.
- **§2.5:** the total kinetic energy is written $K=\int\rho u^2dV$, without the factor $\tfrac12$ (immaterial after normalization by $K_0$).
- **Internal tension.** Summary 3 states that split forms are "nonlinearly stable for smooth flows also in the infinite–Reynolds number limit", and §6 that the "numerical tests herein reported" support nonlinear stability without extra damping, while Fig. 1 at $M_{t,0}=0.3$ shows the Blaisdell split form S6 diverging; only K6 and T2 survive (§2.5).
- **Eq. (32)** states $0\le\varphi_{\mathrm J,i}\le1$, true for positive data; the review applies it to pressure.
- **Attributions.** The third-order SSP Runge–Kutta scheme is cited to Shu & Osher (1989) (§2.5, §4.2); it first appears in [Shu & Osher (1988)](/sources/shu-1988.md), not cited. "Harten et al. 1986" (monotonicity, monotone schemes) is Harten, Hyman & Lax, Commun. Pure Appl. Math. 29 (1976).
- **Naming.** The review calls "modified Ducros sensor" the classical squared ratio $\Phi_{\mathrm D}$ with $\epsilon_{\mathrm D}=(v_\infty/\delta_0)^2$ (§3.2, p. 177, on Fig. 4; §5, Fig. 6 caption and p. 185); other sources of the bundle give the name to the compression-only, unsquared $\Psi_{\mathrm D}$ ([Ducros shock sensor](/definitions/ducros-shock-sensor.md)).
- **Typos:** "Upwinding (scheme D7) curves the divergence" (curbs); "hybrid descretization" (p. 184); "eight-order low-pass filtering" (p. 185).
- **Reference list:** Roe (1981) printed J. Comput. Phys. **34**:357–72 (the volume is 43); Harten, Hyman & Lax printed **1986** (CPAM 29 is 1976); Jiang & Yu printed **1996** (SIAM J. Numer. Anal. 35 is 1998); Kawai & Lele printed **2007** for J. Comput. Phys. 227:9498–526 (2008); Lilly (1965) printed in **J. Comput. Phys.** 93:11–26 (Mon. Weather Rev.); Lund, Wu & Squires (1998) printed in **J. Fluid Mech.** 140:233–58 (J. Comput. Phys. 140); Bogey & Bailly (2004) printed pages 481–91 (194:194–214); Jameson, Schmidt & Turkel (1981) printed "Numerical simulation …", "Pap. 81-1259, NASA" (AIAA Paper 81-1259, "Numerical solution"); Shu (2009) title printed "… convection dominated schemes" (problems); Dupont et al. (2008) "obliques shock"; de Tullio et al. second author "Palma PD"; "LeVecque" for LeVeque.

# Notation map

| Pirozzoli (2011a) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $j$, $h$, $x_j=jh$ | $i$, $\Delta x$, $x_i$ | |
| $v_j(t)$, $\bar v_j$, $v^\pm_{j+1/2}$ | $u_i$, $\bar u_i$, $u^\pm_{i+1/2}$ | same $\pm$ convention |
| $u_i$, $\mathbf u$ (velocity) | $v_d$, $v$ | |
| $\mathbf u$ (conserved), $\mathbf f_i$ | $u$, $f^{(d)}$ | |
| $a(u)$ (Eq. (4)) | $f'(u)$ | |
| $a_{j+1/2}$ (Eq. (15)) | $\bar a_{i+1/2}$ | registry §10, at the reconstructed states |
| $a_{j+1/2}$ (Eq. (30)) | $a_{i+1/2}$ | spectral radius at the Roe average |
| $\mathcal R(\cdot,\cdot)$ | $h(u^-,u^+)$ | two-point flux |
| $Df_j$, $a_m$, $b_\ell$, $c_\ell$, $M$, $L$ (Eqs. (10)–(13)) | $(\delta_xf)_i$, $a_m$, $b_l$, $c_l$, $n_a$, $n_b$ | page-local; **collision** of $M$, $L$ with the mass matrix and left eigenvectors |
| $L$, $S_\ell$, $\omega_\ell$, $\alpha_\ell$, $d_\ell$, $\beta_\ell$, $\epsilon$ (WENO) | $r$, $S_k$, $\omega_k$, $\alpha_k$, $d_k$, $\beta_k$, $\epsilon$ | $S_0$ most upwind; $q=2$ |
| $c_{\ell m}$, $\gamma_{\ell mn}$ | $c_{km}$, $\mathsf g_{kmn}$ | page-local; **collision** of $\gamma$ with TENO's $\gamma_k$ |
| $\lambda$ (Hill–Pullin) | $\lambda_{\mathrm{HP}}$ | page-local; **collision** with eigenvalues $\lambda_l$ |
| $\Theta$, $\epsilon$ (Eq. (29)) | $\Phi_{\mathrm D}$, $\epsilon_{\mathrm D}$ | registry §10 |
| $u_\infty$, $\delta_0$ | $v_\infty$, $\delta_0$ | free-stream velocity, incoming boundary-layer thickness |
| $\Psi_{j+1/2}$ (Eq. (28)) | $\theta_{\mathrm{AC},i+1/2}$ | Harten's switch, registry §10 |
| $k$, $d_{j+1/2}$, $f^*_{j+1/2}$ (Eqs. (27)–(28)) | $\mathsf k_{\mathrm Y}$, $\hat d^{\mathrm{TVD}}_{i+1/2}$, $\hat f^*_{i+1/2}$ | page-local |
| $\hat f^C$, $d_{j+1/2}$, $\epsilon^{(2)}$, $\epsilon^{(4)}$, $k^{(2)}$, $k^{(4)}$, $\psi_j$ | $\hat f^{\mathrm C}$, $\mathcal D_{i+1/2}$, $\varepsilon_2$, $\varepsilon_4$, $k_2$, $k_4$, $\varphi_{\mathrm J,i}$ | as on the artificial-viscosity page |
| $\mu^*=c_\mu\rho h^2\lvert\partial u/\partial x\rvert$ | $\mu^*=c_\mu\rho\Delta x^2\lvert\partial_xv\rvert$ | $c_\mu$ registry §10 |
| $\sigma^*_{ij}$, $\mu^*$, $\beta^*$ ($\beta$ in Eq. (34)), $\eta_r$, $r$, $c^r_\mu$, $c^r_\beta$, $\Delta$, $S$, $S_{ij}$ | $\sigma^*_{ij}$, $\mu^*$, $\beta^*$, $\mathcal H_{r_{\mathrm L}}$, $r_{\mathrm L}$, $c^{(r_{\mathrm L})}_\mu$, $c^{(r_{\mathrm L})}_\beta$, $\Delta$, $\mathsf S$, $S_{ij}$ | page-local on [LAD](/methods/localized-artificial-diffusivity.md); **collisions** of $\eta$ (entropy), $r$ (WENO), $S$ (source term) |
| $G$, $G_2$, $Q$, $\mathcal G_1$, $\mathcal R$, $\chi$ (Eqs. (35)–(37)) | $\mathcal F$, $\mathcal F_2$, $\mathcal Q$, $\mathcal G_1$, $\mathcal R$, $\chi$ | page-local; **collision** of $G$ with the admissible set |
| $\alpha$, $\hat v$, $d_\ell$, $L$ (Eq. (17), filters) | $\alpha_{\mathrm f}$, $u^{\mathrm f}$, $c^{\mathrm f}_l$, $n_{\mathrm f}$ | page-local |
| $\varphi$ (split forms) | $\phi$ | page-local transported quantity, as on the split-forms page |
| $\alpha$, $\beta$ (Eq. (20)) | $\alpha_{\mathrm{KG}}$, $\beta_{\mathrm{KG}}$ | page-local |
| $s=\log(p\rho^{-\gamma})$ | $s$ | registry |
| $v=\partial(\rho g(s))/\partial u$ (entropy variables) | $w$ | canonical $w=\eta'(u)$ with $\eta=-\rho g(s)$ (sign) |
| $P$, $B_i$, $\beta$ (Eqs. (7)–(9), (22)) | $\mathsf P_{\mathrm H}$, $\mathsf B^{(d)}_{\mathrm H}$, $\beta_{\mathrm{ES}}$ | page-local; **collisions** with $B$ (magnetic field, SBP boundary matrix) and $\beta_k$ |
| $\mathbf f_{j+1/2}$ (Eq. (21)) | $f^{\mathrm{ec}}_{i+1/2}$ | |
| $\rho u_ku_k/2$ | $\kappa$ | |
| $M_{t0}$, $k_0$, $E(k)$, $\tau$, $K$, $S$ (§2.5) | $M_{t,0}$, $k_0$, $E_k(k_w)$, eddy-turnover time, total kinetic energy, total entropy | page-local; $\tau$ is not the WENO-Z indicator |
| $P_NP_M$ | $P_NP_M$ | $N$ the registry DG degree, $M$ page-local (flux degree) |

# Reference list

The review prints 153 references in "Literature Cited" (author–year, unnumbered), plus three in
"Related Resources" (Lele 1994, Moin & Mahesh 1998, Tadmor 2010 web page) that the text does not cite;
all 156 are merged into the [bibliography](/bibliography.md) with `citedby` including
`pirozzoli-2011`. One in-text citation has no entry: "M. Bernardini, S. Pirozzoli & F. Grasso,
submitted manuscript" (§5, Fig. 6). Ingested works in the list: [Harten (1983a)](/sources/harten-1983.md),
[Harten et al. (1987a)](/sources/harten-1987.md), [Liu et al. (1994)](/sources/liu-1994.md),
[Jiang & Shu (1996)](/sources/jiang-1996.md), [Shu (2009a)](/sources/shu-2009.md),
[Van Leer (1979)](/sources/vanleer-1979.md), and, in this chunk,
[Ducros et al. (1999)](/sources/ducros-1999.md) and [Pirozzoli (2010)](/sources/pirozzoli-2010.md).
Identity notes: "Harten et al. 1986" is Harten, Hyman & Lax (1976, key `harten-1976`); Jiang & Yu
(printed 1996) is the 1998 SIAM J. Numer. Anal. paper (`jiang-1998-c`); Kawai & Lele (printed 2007) is
the 2008 J. Comput. Phys. paper (`kawai-2008`); Arora & Roe on post-shock oscillations is `arora-1997-b`,
distinct from their limiter paper `arora-1997`; Shu & Osher (1989) is part II, distinct from
[Shu & Osher (1988)](/sources/shu-1988.md). Eleven entries carry margin annotations in the review
(Adams & Shariff 1996, Colonius 2004, Cook & Cabot 2004, Johnsen et al. 2010, Kennedy & Gruber 2008,
Lele 1992, Shu 2009, Subbareddy & Candler 2009, Toro 2009, Wang 2007, Yee et al. 1999).

# Pages created or updated

Chunk 14 (2026-11-17). This source is cited on:

* [ADER schemes](/methods/ader-scheme.md)
* [Approximate dispersion relation](/definitions/approximate-dispersion-relation.md)
* [Artificial viscosity and spectral viscosity](/methods/artificial-viscosity.md)
* [Compact low-pass filter](/methods/compact-low-pass-filter.md)
* [Compressible isotropic turbulence](/benchmarks/compressible-isotropic-turbulence.md)
* [Conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
* [Conservative split central derivative](/operators/conservative-split-derivative.md)
* [Discontinuous Galerkin method](/methods/discontinuous-galerkin.md)
* [Ducros shock sensor](/definitions/ducros-shock-sensor.md)
* [ENO property](/definitions/eno-property.md)
* [ENO reconstruction (essentially non-oscillatory schemes)](/methods/eno-reconstruction.md)
* [Entropy stability](/properties/entropy-stability.md)
* [Entropy-conservative and kinetic-energy-preserving two-point fluxes](/methods/entropy-conservative-flux.md)
* [Flux vector splitting](/methods/flux-vector-splitting.md)
* [Hybrid central-WENO schemes](/methods/hybrid-weno.md)
* [Immersed-boundary and cut-cell methods](/methods/immersed-boundary-method.md)
* [Implicit large-eddy simulation (ILES)](/definitions/implicit-large-eddy-simulation.md)
* [Implicit shock tracking and moving DG (MDG-ICE)](/methods/implicit-shock-tracking.md)
* [Kinetic energy preservation](/properties/kinetic-energy-preservation.md)
* [Lax–Wendroff theorem](/results/lax-wendroff-theorem.md)
* [Local conservation is equivalent to a flux form](/results/local-conservation-flux-form.md)
* [Localized artificial diffusivity (LAD)](/methods/localized-artificial-diffusivity.md)
* [Monotone schemes and monotone numerical fluxes](/definitions/monotone-scheme.md)
* [Monotonicity-preserving (MP) limiter](/methods/monotonicity-preserving-limiter.md)
* [Numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
* [Order of accuracy behind captured shocks](/results/order-of-accuracy-behind-shocks.md)
* [Quasi-spectral viscosity](/methods/quasi-spectral-viscosity.md)
* [Richtmyer–Meshkov instability](/benchmarks/richtmyer-meshkov-instability.md)
* [Roe approximate Riemann solver](/methods/roe-riemann-solver.md)
* [Shock–turbulence interaction](/benchmarks/shock-turbulence-interaction.md)
* [Split convective forms](/methods/split-convective-forms.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Summation-by-parts operator](/operators/summation-by-parts-operator.md)
* [Symmetry preservation](/properties/symmetry-preservation.md)
* [Total variation diminishing (TVD) and slope limiters](/definitions/total-variation-diminishing.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
* [Two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md)
* [Weighted compact nonlinear schemes (WCNS)](/methods/weighted-compact-nonlinear-scheme.md)
* [WENO-JS reconstruction](/methods/weno-js-reconstruction.md)
