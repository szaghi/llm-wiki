---
type: Source
title: "Chen et al. (2022) — Turbulent kinetic dissipation analysis for residual-based large eddy simulation of incompressible turbulent flow by variational multiscale method"
description: "Term-by-term resolved kinetic-energy budget of residual-based variational multiscale LES in a coarse Re_tau=180 channel, against Smagorinsky and dynamic LES; one cross-stress term is anti-dissipative on average, and a modified stabilized formulation that reverses its sign improves cavity and channel statistics."
resource: "doi:10.1016/j.cma.2021.114280"
source_kind: paper
authors: [Chen L., Hulshoff S.J., Dong Y.]
year: 2022
venue: "Comput. Methods Appl. Mech. Engrg. 388:114280"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Computer_Methods_in_Applied_Mechanics_and_Engineering_Chen_Turbulent_kinetic_dissipation_analysis_for_residual-based_la.pdf"
tags: [les, implicit-les, numerical-dissipation, stabilized-fem, residual-based]
timestamp: 2026-10-28T07:07:00Z
---

# Summary

Chen et al. (2022) read the residual-based
[variational multiscale method](/methods/variational-multiscale-method.md)
of Bazilevs et al. (2007) for incompressible flow as an
[implicit LES](/definitions/implicit-les.md): the small scales are modelled
algebraically from the residuals, $\boldsymbol u^<=-\tau_{\mathrm M}\boldsymbol r_{\mathrm M}$,
$p^<=-\tau_{\mathrm C}r_{\mathrm C}$, and the closure consists of residual-driven
stabilization terms with no eddy viscosity. Testing the large-scale weak form
with the resolved velocity gives a resolved kinetic-energy equation in which
four small-scale terms appear: two cross-stress terms (I and II), a
Reynolds-stress-like term (III) and the least-squares incompressibility
(LSIC) pressure term (IV).

In a [turbulent channel](/benchmarks/turbulent-channel-flow.md) at
$Re_\tau=180$ on a coarse $32\times64\times32$ trilinear mesh, the VMS LES
gives better mean velocity, fluctuation intensities and shear stress than a
finite-difference LES with the [Smagorinsky model](/methods/smagorinsky-model.md)
($C_s=0.1$) or the [dynamic procedure](/methods/dynamic-procedure.md) on the
same mesh. The averaged [numerical dissipation](/properties/numerical-dissipation.md)
of the VMS terms is smaller than the classical SGS dissipation in the inner
layer and larger in the outer layer, with comparable streamwise, wall-normal
and spanwise components where the SGS dissipation is mainly streamwise.
Term I (the SUPG term) and Term IV carry most of the dissipation, Term III
is two to three orders of magnitude smaller, and Term II has a positive
(energy-producing) average over most of the channel; the authors call this
contrary to the intent of a turbulence model (the paper does not use the
word [backscatter](/definitions/energy-backscatter.md)).

The authors then propose a modified stabilized formulation that keeps Terms
I, III, IV, V and reverses the sign of Term II, so that every stabilization
term is dissipative in the energy budget. On the 2-D lid-driven cavity
($Re=1000$, $125\,000$) and the $Re_\tau=180$ channel it is closer to the
references than VMS and SUPG, notably in the outer-layer mean velocity and
the buffer-layer streamwise intensity; the authors argue that, being
residual-based, its numerical diffusion vanishes under mesh refinement. All
tests are a posteriori on one mesh per case. The work bears on
[large-eddy simulation](/definitions/large-eddy-simulation.md) through the
explicit-against-residual-based comparison.

# Version read

Version of record (Comput. Methods Appl. Mech. Engrg. 388 (2022) 114280;
received 22 April 2021, available online 9 November 2021), 18 pages, all
read; pages 4–6 and 9–12 also read visually for Eqs. (9)–(15), (24)–(29),
(31)–(38) and Figs. 3–5. Page-1 title, authors and DOI match the metadata.
No identity problem. Numbering on this page is that of this version.

# Key claims

Symbols: $\boldsymbol u^{>}$, $p^{>}$ the resolved (finite-element)
scales and $\boldsymbol u^<$, $p^<$ the unresolved small scales of the VMS
split (registry §2; the source's $\boldsymbol u^h$, $p^h$ and
$\boldsymbol u'$, $p'$), $\boldsymbol w$ the velocity weighting function
(the source's $\boldsymbol w^h$). Registry §11, as on the
[VMS page](/methods/variational-multiscale-method.md):
$\boldsymbol r_{\mathrm M}$, $r_{\mathrm C}$ the
momentum and continuity residuals; $\tau_{\mathrm M}$, $\tau_{\mathrm C}$ the
stabilization parameters (the source's $\tau_m$, $\tau_c$). Page-local: $\mathcal D_n$
the plane- and time-averaged contribution of Term $n$ to the resolved
kinetic-energy budget, negative when dissipative (the source's
$\langle\epsilon_n\rangle$); $\alpha^{\mathrm G}_m$, $\alpha^{\mathrm G}_f$,
$\gamma^{\mathrm G}$, $\rho^{\mathrm G}_\infty$ the generalized-$\alpha$
parameters (the source's $\alpha_m$, $\alpha_f$, $\gamma$, $\zeta$).

1. The residual-based LES derived from the VMS method is an implicit LES: its small-scale model is "an addition of purely dissipative numerical terms and no eddy viscosity is introduced" (§1, §7). **Stated**
2. Unlike classical filtered LES, the residual-based model keeps numerical consistency and permits the full convergence rate, "whereas, e.g. the convergence rate of the classical LES is limited to $O(h^{4/3})$ due to the artificial viscosity effects" (§1, citing earlier work). **Stated**
3. Setting $\boldsymbol w=\boldsymbol u^{>}$ in the large-scale equation (10) gives the resolved kinetic-energy equation (24), whose second line contains the four VMS Terms (1)–(4) (§3, Eq. 24). **Derived**
4. On the $Re_\tau=180$ channel with the $32\times64\times32$ mesh, the Smagorinsky LES strongly under-predicts the mean streamwise velocity, especially for $y/\delta<0.1$; dynamic-SGS LES and residual-based LES agree well with DNS in the inner layer, the residual-based LES better than the dynamic one (§4.2, Fig. 1). **Shown**
5. The streamwise intensity peaks at $y^+\approx15$ for dynamic-SGS and residual-based LES (as in DNS), while Smagorinsky shifts it outward; the residual-based LES gives better intensities and Reynolds shear stress than both classical LES (§4.2, Fig. 2). **Shown**
6. The Smagorinsky model "engenders very high dissipation in the viscous sublayer ($y^+<5$)", proposed as the cause of its under-predicted statistics; the dynamic model has lower inner-layer and higher outer-layer dissipation than Smagorinsky (§5, Fig. 3, Eq. 33). **Shown**
7. The classical SGS dissipation is mainly in the streamwise component; the three components of the VMS numerical dissipation are "rather comparable" (§5, Fig. 3). **Shown**
8. The VMS total numerical dissipation is "much smaller in the inner layer, larger in the outer region" than the SGS dissipation of the classical LES (§5, Fig. 3; abstract; §7). **Shown**
9. Term I equals the SUPG stabilization term once $\boldsymbol u^<$ is substituted; $\mathcal D_1$ is negative across the channel (§5, Fig. 4). **Shown**
10. Term II, $(\boldsymbol w,\boldsymbol u^<\cdot\nabla\boldsymbol u^{>})$, has positive $\mathcal D_2$ over most of the channel: it "does not dissipate the turbulent kinetic energy but increases energy", which "differs from the intention of the turbulent model" (§5, Figs. 4–5). **Shown**
11. Term III is negative over most of the channel but very small against Term I (§5, Figs. 4–5). **Shown**
12. Term IV (LSIC) "plays an important role in providing the additional dissipation"; its spanwise component is the largest, its wall-normal one small (§5, Figs. 4–5). **Shown**
13. Keeping the convective part of the residual, Term (1) reads $-(\partial_ju^{>}_i)u^{>}_j\tau_{\mathrm M}u^{>}_k\partial_ku^{>}_i$, "which always stays negative when $j=k$"; the streamwise component dominates through $\partial_yu^{>}$ (§5). **Derived**
14. The dominant part of Term (2) is $u^{>}_i\tau_{\mathrm M}u^{>}_k(\partial_ku^{>}_j)(\partial_ju^{>}_i)$; its streamwise component is positive over most of the channel (negative for $y^+<5$) and dominates $\mathcal D_2$; the wall-normal component has the opposite sign (§5, Fig. 5). **Shown**
15. Terms I, III and IV supply turbulent dissipation as numerical diffusion; Term II cannot (§5, §7). **Shown**
16. The proposed formulation (Eq. 38) keeps Terms I, III, IV, V of the large-scale equation and reverses the sign of Term II; it remains residual-based and consistent (§6, Eq. 38). **Derived**
17. In the energy equation of the new formulation (Eq. 39) all four stabilization terms are dissipative; its total numerical diffusion exceeds that of SUPG, which exceeds that of VMS (SUPG keeps only Terms (1) and (4)) (§6.2, Fig. 8a). **Shown**
18. Lid-driven cavity: VMS, SUPG and the modified formulation are very close at $Re=1000$ ($32\times32$ cells); at $Re=125\,000$ ($64\times64$) "the VMS method does not show an advantage in comparison with the SUPG method" and the modified formulation is closest to the reference of Erturk et al., especially next to the wall (§6.1, Fig. 6). **Shown**
19. Channel: the mean velocities of VMS, SUPG and the modified formulation are close for $y^+<10$; in the outer layer SUPG is slightly closer to DNS than VMS and the modified formulation is clearly best (§6.2, Fig. 7a). **Shown**
20. SUPG and the modified formulation improve the streamwise intensity in the buffer layer ($5<y^+<30$), the modified one best; wall-normal intensities are similar; the modified one slightly improves the spanwise intensity in the outer layer; the Reynolds shear stress decreases slightly for SUPG and the modified formulation (§6.2, Fig. 7). **Shown**
21. Larger numerical diffusion "dissipates the bulk velocity and allows the mean velocity profile to become closer to the solution when using a coarse mesh" (§6.2). **Stated**
22. In the modified formulation $\mathcal D_1$, $\mathcal D_3$, $\mathcal D_4$ are close to those of VMS and SUPG; $\mathcal D_2$ has the opposite sign to the VMS one but is not exactly its mirror image (§6.2, Fig. 8b). **Shown**
23. Numerical consistency makes the numerical diffusion "dynamically reduce with refinement until it vanishes when grid spacing satisfies DNS" (§6.2, §7). **Stated** (no mesh-refinement study is shown)
24. Generalized-$\alpha$ time integration is second order if $\gamma^{\mathrm G}=0.5+\alpha^{\mathrm G}_m+\alpha^{\mathrm G}_f$ (as printed, Eq. 21) and unconditionally stable if $\alpha^{\mathrm G}_m\ge\alpha^{\mathrm G}_f\ge1/2$ (Eq. 22), with $\alpha^{\mathrm G}_m=\tfrac12(3-\rho^{\mathrm G}_\infty)/(1+\rho^{\mathrm G}_\infty)$, $\alpha^{\mathrm G}_f=1/(1+\rho^{\mathrm G}_\infty)$, $\rho^{\mathrm G}_\infty=0.5$ (§2.4, Eq. 23). **Stated** (see Printed slips)

# Printed slips

- **Eq. (21):** printed "$\gamma=0.5+\alpha_m+\alpha_f$" as the
  second-order condition. *(compiler check, not in the sources)* With Eq.
  (23) and $\zeta=0.5$ ($\alpha_m=5/6$, $\alpha_f=2/3$), integrating
  $\dot a=-a$ to $t=1$ with the printed update Eqs. (17)–(20) converges at
  order 1.00 with $\gamma=0.5+\alpha_m+\alpha_f=2$ and at order 2.00 with
  $\gamma=0.5+\alpha_m-\alpha_f$. The paper does not say which value the code
  uses.
- **Eq. (14) against Eq. (12):** *(compiler check, not in the sources)* with
  $p$ the kinematic pressure (m²/s²) and $r_c=\nabla\cdot\boldsymbol u^h$
  (1/s), $p'=-\tau_cr_c$ needs $\tau_c$ in m²/s, while the printed
  $\tau_c=\boldsymbol u^h\boldsymbol G\boldsymbol u^h/\mathrm{tr}(\boldsymbol G)$
  has units m²/s².
- **Eq. (38), Term ④:** printed
  $(\nabla\cdot\boldsymbol w^h,\tau_c\nabla\cdot\boldsymbol w^h)_{\Omega_e}$;
  the text says it equals Term IV of Eq. (10), and Eq. (39) uses
  $\tau_c\nabla\cdot\boldsymbol u^h$.
- **§6.2:** "owing to the replacement of Term II in Eq. (10) with Term ① in
  Eq. (38)"; below Eq. (38) the paper states that Term ② replaces Term II.
- **§4.2:** "Certain over-estimations are still caused in the outer layer
  ($y^+<50$)".
- **§2.4:** Eq. (16) is $A(\boldsymbol a)\dot{\boldsymbol a}=B(\boldsymbol a)\boldsymbol a$,
  but the text names "$M$ and $N$" as the matrices.
- **p. 4:** broken citation "By a treatment used in [20,33][?]".
- **Eqs. (10), (38):** the pressure term is printed
  $-(\nabla\boldsymbol w^h,p^h)_\Omega$, without the divergence.
- **Eq. (30) against Table 1:** Eq. (30) maps the nodes to $y\in[0,1]$
  while $L_y=2$. *(compiler check, not in the sources)* With $N_y=64$ and
  $\alpha_s=1.5$ the first node is at $y=0.004883$, i.e. $0.879$ wall units
  if $y$ is measured in channel half-heights, matching Table 1's
  $\Delta y^+_{\min}=0.88$; the paper does not say how the $[0,1]$ map is
  applied to the height 2.
- **§6:** "Martinez and Jansen have coupled…"; ref. [49] is Tejada-Martínez
  & Jansen.
- **Notation:** the filtered velocity is $\tilde u$ in Eqs. (25)–(29) and
  $\bar u$ in Eq. (33); the same symbol $\langle\epsilon_{total}\rangle$
  is used for the VMS (Eq. 31) and the SGS (Eq. 33) dissipation.
- **Ref. [15]:** printed author list "G. Motlagh, Yousef, Ahn, H. Taek,
  Hughes, J.R. Thomas, M. Victor"; **ref. [44]:** "158 (158)"; **refs. [25],
  [29]:** no volume.

# Notation map

| Chen et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\boldsymbol u$, $p$, $\nu$, $\boldsymbol f$ | $\boldsymbol u$, $p$, $\nu$, $f_i$ | $p$ kinematic; channel forcing $\boldsymbol f=(1,0,0)$ |
| $\nabla^s\boldsymbol u$ | $S_{ij}$ | |
| $(\cdot)^h$, $(\cdot)'$ | $(\cdot)^{>}$, $(\cdot)^{<}$ | VMS scale split, not a filter; **collision:** the prime is also the statistical fluctuation in $u'_{rms}$, $\langle u'v'\rangle$ (§4.2) |
| $\boldsymbol w^h$ | $\boldsymbol w$ (page-local) | velocity weighting function |
| $\boldsymbol r_m$, $r_c$ | $\boldsymbol r_{\mathrm M}$, $r_{\mathrm C}$ (registry §11) | |
| $\tau_m$, $\tau_c$ | $\tau_{\mathrm M}$, $\tau_{\mathrm C}$ (registry §11) | **collision** with the SGS stress $\tau_{ij}$ |
| $\boldsymbol G$, $c_1$, $c_2$, $c_3$ | (element metric tensor; 4, 36, 4) | |
| $\alpha_m$, $\alpha_f$, $\gamma$, $\zeta$ | $\alpha^{\mathrm G}_m$, $\alpha^{\mathrm G}_f$, $\gamma^{\mathrm G}$, $\rho^{\mathrm G}_\infty$ (page-local) | **collisions** with $\alpha_f$ (filter strength), $\gamma$, $\boldsymbol\zeta$ |
| $\langle\epsilon_{total}\rangle$, $\langle\epsilon_1\rangle$–$\langle\epsilon_4\rangle$, $\langle\epsilon_x\rangle$, $\langle\epsilon_y\rangle$, $\langle\epsilon_z\rangle$ | $\mathcal D_{\mathrm{tot}}$, $\mathcal D_1$–$\mathcal D_4$, $\mathcal D_x$, $\mathcal D_y$, $\mathcal D_z$ (page-local) | averaged over $x$, $z$, $t$; negative = dissipative, the opposite sign to $\varepsilon$ |
| $\tilde u_i$, $\bar u_i$ (§4–5) | $\bar u_i$ | LES filter; **collision:** the tilde is not a Favre filter |
| $T=2\nu_T\tilde S_{ij}$ | $\tau^d_{ij}=-2\nu_t\bar S^d_{ij}$ | printed without the minus sign |
| $\nu_T$, $C_S^\Delta$, $\tilde\Delta$ | $\nu_t$, $C_s$, $\Delta$ | $\nu_t=(C_s\Delta)^2\lvert\bar S\rvert$; $\lvert\tilde S\rvert$ not defined in the paper |
| $\hat{\tilde\Delta}$, $L_{ij}$, $M_{ij}$ | $\hat\Delta$, $-L^d_{ij}$, (Germano–Lilly tensor) | printed $L_{ij}=\hat{\tilde u}_i\hat{\tilde u}_j-\widehat{\tilde u_i\tilde u_j}$ minus its trace part, the opposite sign of the registry $L_{ij}$ |
| $\delta$, $Re_\tau$, $y^+$, $\langle U\rangle$ | $\delta$, $Re_\tau$, $y^+$, $\langle u\rangle$ | channel half-height |
| $u'_{rms}$, $-\langle u'v'\rangle$ | $\sqrt{R_{11}}$, $-R_{12}$ | |
| $\alpha_s$, $N_y$ | (tanh stretching parameter, wall-normal count) | |

# Reference list

50 printed references, numbered style with titles. The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this slug.
Same-author same-year works take suffixes in printed order (Bazilevs 2010,
Hughes 2001, Akkerman 2012, Chen 2020, and the two "M.F.P.T. Eikelder" 2018
papers, printed without the particle of ten Eikelder, keyed `teneikelder-2018` and `teneikelder-2018-b`). Ref. [15] has a
garbled author list (printed "G. Motlagh"; keyed `ghaffarimotlagh-2013` from the Crossref record of its DOI); refs. [25],
[29] print no volume; ref. [46] has no publisher. No printed duplicates.

# Pages created or updated

Chunk 10 (2026-10-27). This source is cited on:

- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Energy backscatter and the subgrid energy flux](/definitions/energy-backscatter.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Variational multiscale method](/methods/variational-multiscale-method.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
