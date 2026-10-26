---
type: Source
title: "Beattie et al. (2025) — Taking control of compressible modes: bulk viscosity and the turbulent dynamo"
description: "Adds an explicit bulk viscosity to trans-sonic visco-resistive MHD simulations of the small-scale dynamo, defines a viscous Prandtl number, decomposes the dynamo growth rate into stretching, winding and compression, and argues that shear-viscous compressible DNS are implicit LES of the compressible modes."
resource: "doi:10.1093/mnras/staf1318"
source_kind: paper
authors: [Beattie J.R., Federrath C., Kriel N., Hew J.K.J., Bhattacharjee A.]
year: 2025
venue: "Mon. Not. R. Astron. Soc. 542:2669–2697"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2025_Crossref_Monthly_Notices_of_the_Royal_Astronomical_Society_Beattie_Taking_control_of_compressible_modes_bulk_viscosity_and_the.pdf"
tags: [mhd, dynamo, compressible, dns, implicit-les, astrophysics]
timestamp: 2026-10-26T15:53:00Z
---

# Summary

Beattie et al. (2025) add an explicit [bulk viscosity](/definitions/bulk-viscosity.md)
$\nu_b$ to forced, isothermal, visco-resistive compressible MHD
simulations of the [small-scale dynamo](/results/small-scale-dynamo.md) at rms
Mach number $M_t\approx1$, run with a modified version of the finite-volume
code FLASH on periodic boxes of $128^3$ to $1024^3$ cells. Without it the
compressible (curl-free) velocity modes are damped only by the scheme's
[numerical dissipation](/properties/numerical-dissipation.md). Astrophysical
molecular gases out of equilibrium also carry a physical bulk viscosity: the
authors estimate $\nu_b/\nu\approx30$ for shock-heated H$_2$ and
$\approx1$ for cold CO. They define a bulk Reynolds number and a viscous
Prandtl number $P_\nu=\nu/\nu_b$, and decompose the dynamo growth
rate into stretching, winding (identically zero) and compression terms.

At $Re=Rm=1000$ and $P_\nu$ from $\infty$ to $10^{-3}$, the kinematic growth
rate and the saturated ratio $E_{\mathrm{mag}}/E_{\mathrm{kin}}\approx0.15$
barely change until the bulk-viscous time reaches the driving time. The
compressible share of the kinetic energy scales roughly as $P_\nu$ for
$P_\nu<1$. Stretching dominates growth; compression grows and decays the field
in about equal amounts. Without bulk viscosity the compressible modes pile up
at high wavenumber, which the authors call a
[bottleneck](/definitions/bottleneck-effect.md) and which vanishes for
$P_\nu\le0.1$. Low $P_\nu$ also suppresses high-wavenumber solenoidal and
magnetic modes, so the field becomes larger-scale. The
[compressible MHD turbulence](/results/compressible-mhd-turbulence.md) spectra
are Helmholtz-decomposed: the compressible part follows $k^{-2}$ at
$M_t\approx1$. The methodological claim is that a compressible
[DNS](/definitions/direct-numerical-simulation.md) with shear viscosity only
does not resolve the compressible-mode dissipation scale and is an
[implicit LES](/definitions/implicit-les.md) of those modes; a resolved
compressible DNS needs both viscosities with $P_\nu\sim1$. The forced periodic
box is a [forced isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
setting with an Ornstein–Uhlenbeck forcing.

# Version read

arXiv preprint 2312.03984v4 (5 August 2025; MNRAS style, "Preprint 6 August
2025", "Accepted XXX"), the authors' final arXiv version, not the typeset
version of record. 31 pages (main text 1–22, references 22–25, appendices A–F
25–31), all read; page 18 (Eqs. 56–58) was also read visually. Page numbers
are the preprint's, not 2669–2697. Title and authors match the published
metadata.

# Key claims

Notation: $\boldsymbol u$ velocity, $\boldsymbol B$ magnetic field (Gaussian units), $\nu$ the shear viscosity, $\eta_m$ the resistivity, $\Gamma_E=2\gamma_1$ the kinematic growth rate of the magnetic energy, $t_0$ the forcing correlation time, $\ell_0=L_{\mathrm{box}}/2$ the driving scale, $\boldsymbol u_{\mathrm c}$ and $\boldsymbol u_{\mathrm s}$ the compressive (curl-free) and solenoidal Helmholtz components and $E_{\mathrm c}(k)$, $E_{\mathrm s}(k)$ their kinetic-energy spectra, $E_B(k)$ the magnetic spectrum, $\nu_b$ the kinematic bulk viscosity, $P_\nu=\nu/\nu_b$ the viscous Prandtl number, $\gamma_B$ the instantaneous growth rate of $\langle B^2\rangle$ divided by two (page-local, as on [bulk viscosity](/definitions/bulk-viscosity.md) and [small-scale dynamo](/results/small-scale-dynamo.md); see the Notation map).

1. Earlier supersonic-dynamo studies controlled only the shear viscosity; the decay of compressible modes was then "governed completely by numerical dissipation", set by the flux discretisation, the Riemann solver and the resolution (§1). **Stated**
2. The Stokes hypothesis $\nu_b=0$ is exact for monoatomic gases; for diatomic and triatomic gases out of equilibrium $\nu_b$ "can vary between tens and thousands of times larger than the shear viscosity" (§1, citing Pan & Johnsen 2017, Sharma & Kumar 2019, 2023). **Stated**
3. The rotation tensor neither grows nor dissipates kinetic energy through the viscous stress: $\boldsymbol u\cdot\nabla\cdot(\rho\,\Omega)=0$ by antisymmetry (App. A, Eqs. A1–A3). **Derived**
4. Microphysical estimates: $\nu_b/\nu\approx30$ for H$_2$ shock-heated to $T\approx10^3$ K (rotational relaxation time $\approx2.3\times10^8$ s $\approx7.4$ yr); $\approx1$ for ambient CO at $T\approx10$ K ($\approx7.1\times10^6$ s $\approx3$ months) (§2.1; App. B, Eqs. B1–B2). **Derived** (order of magnitude)
5. The non-dimensional momentum equation carries $1/Re$ on the deviatoric and $1/Re_{\mathrm{bulk}}$ on the bulk term; $P_\nu=\nu/\nu_b=Re_{\mathrm{bulk}}/Re\sim t_{\nu_b}/t_\nu$ (§2.2.1, Eqs. 20–24). **Derived**
6. With $Pm=1$ fixed, the bulk magnetic Prandtl number is $Pm_{\mathrm{bulk}}=\nu_b/\eta_m=P_\nu^{-1}$ (§2.2.2, Eqs. 29–30). **Derived**
7. For $P_\nu<1$ a sub-bulk-viscous range $\ell_0>\ell_{\nu_b}>\ell>\ell_\nu$ appears with $E_{\mathrm s}\gg E_{\mathrm c}$; for $P_\nu>1$ a sub-shear-viscous range $\ell_0>\ell_\nu>\ell>\ell_{\nu_b}$ with $E_{\mathrm c}\gg E_{\mathrm s}$; all $M_t>1$ simulations without explicit bulk viscosity "ought to be" in the second regime (§3.1, Eqs. 31–32, Fig. 1). **Derived** (schematic), **Shown** in §6
8. The first-moment equation $\mathrm d\langle E_{\mathrm{mag}}\rangle/\mathrm dt=2\gamma_B\langle E_{\mathrm{mag}}\rangle-2\eta_mk_u^2\langle E_{\mathrm{mag}}\rangle$, with $\gamma_B=\langle B_iB_j[\partial_ju_i-\tfrac12S_{kk}\delta_{ij}]\rangle/\langle B^2\rangle$, splits $\gamma_B$ into stretching $\langle B_iB_jS^d_{ij}\rangle/\langle B^2\rangle$, winding (the rotation-tensor contraction) and compression $-\langle B^2\,\nabla\cdot\boldsymbol u\rangle/(6\langle B^2\rangle)$ (Eqs. 33–38; App. C). **Derived**
9. The winding term vanishes identically because $B_iB_j$ is symmetric and $\Omega_{ij}$ antisymmetric; the simulations confirm it (§3.2, Eq. 39, §5.2, Fig. 7). **Derived** and **Shown**
10. Compressions ($\nabla\cdot\boldsymbol u<0$) raise the local growth rate by $\tfrac16\lvert\nabla\cdot\boldsymbol u\rvert$ and rarefactions lower it by the same amount; only compressions perpendicular to the field contribute (§3.2, Eq. 40, footnote 6). **Derived**
11. Earlier decompositions that kept the compressive part inside the stretching tensor overestimated the effect of compressions "by a factor of 3 in Seta & Federrath (2021) and 6 in Sur & Subramanian (2023)" (footnote 4). **Stated** (factors asserted, not derived)
12. The saturated $\langle E_{\mathrm{mag}}\rangle/\langle E_{\mathrm{kin}}\rangle\approx0.15$ (Alfvén Mach number $\approx2.5$) changes little over $0.01\le P_\nu\le\infty$, consistent within $1\sigma$ with Federrath et al. (2011) at $P_\nu=\infty$ (§5.1, Table 1, Fig. 5). **Shown**
13. Table 1: $\Gamma_Et_0=1.48\pm0.03$ ($P_\nu=\infty$, $512^3$), $1.42\pm0.02$ ($P_\nu=1$, $512^3$), $1.47\pm0.05$ ($P_\nu=0.1$, $512^3$), $1.46\pm0.03$ ($P_\nu=0.01$, $256^3$), $1.28\pm0.02$ ($P_\nu=0.001$, $256^3$); the text says the growth rate becomes "significantly affected" at "$Re_{\mathrm{bulk}}\le10$, $P_\nu\le0.01$" (§5.2, Table 1). **Shown** (see Printed slips)
14. The compressible kinetic-energy fraction falls from $\approx10^{-1}$ ($P_\nu=\infty$) to $\approx10^{-3}$ ($P_\nu=0.001$), $\langle E_{\mathrm c}\rangle/\langle E_{\mathrm{kin}}\rangle\sim P_\nu$ for $P_\nu<1$ (Eq. 54, Fig. 6). **Shown**
15. The solenoidal saturation is insensitive to $\nu_b$, $\langle E_{\mathrm{mag}}\rangle/\langle E_{\mathrm s}\rangle\approx0.1$; the compressible modes saturate at $1\le\langle E_{\mathrm{mag}}\rangle/\langle E_{\mathrm c}\rangle\le10$ (§5.1, Fig. 6). **Shown**
16. Stretching dominates growth in the kinematic and saturated stages and grows the field "for all quantiles above the 16th percentile"; the compression term is nearly symmetric about zero, a "dual role" at $M_t\approx1$ (§5.2, Figs. 7–8). **Shown**
17. Lower $P_\nu$ contracts the fluctuations of the compression term while keeping its mean near zero, "a key result from this analysis" (§5.2). **Shown**
18. At saturation the median stretching term moves towards zero "by ≈ 2" for all $P_\nu$, as Sur & Subramanian (2023) found at $M_t=3$ (§5.2, Fig. 8). **Shown**
19. For $P_\nu=1$ and $\infty$ excess compressible power piles up at high $k$ (a "bottleneck", the sub-shear-viscous range), with $E_{\mathrm c}(k)/E_{\mathrm s}(k)$ rising from $\approx10^{-1}$ at large scales to $\approx10^2$ at small scales; it "completely disappear[s]" for $P_\nu\le0.1$ (§6.1–6.2, Fig. 9). **Shown**
20. At the lowest $P_\nu$ the low-$k$ compressible modes are suppressed "by roughly $10^2$ in total power" relative to $P_\nu=\infty$ (§6.2). **Shown**
21. The compressible spectrum follows $E_{\mathrm c}(k)\sim k^{-2}$ (Burgers) in the low-$\nu_b$ runs, not the $k^{-3}$ pseudo-acoustic spectrum of Wang et al. (2017) and Sakurai & Ishihara (2023), which holds for $M_t\lesssim0.4$; the solenoidal spectrum is roughly $k^{-5/3}$ over a short range (§6.2, Fig. 9). **Shown**
22. In the Stokes limit the viscous operators decouple the Helmholtz modes (Eqs. 56–57, E9–E10), so the observed high-$k$ coupling of $\boldsymbol u_{\mathrm c}$ and $\boldsymbol u_{\mathrm s}$ is attributed not to the viscous terms but to the reduced small-scale enstrophy production through $\boldsymbol\omega(\nabla\cdot\boldsymbol u)$ (Touber 2019) (§6.2; App. E). **Derived** and **Stated**
23. Low $P_\nu$ makes the magnetic field larger-scale in both stages; the saturated correlation wavenumber settles at $k_{\mathrm{cor}}\ell_0\approx2.5$; the proposed mechanism, the bulk-viscous wavenumber "dragging" the shear-viscous one to lower $k$ and with it the resistive one, $k_{\eta_m}\sim Pm^{1/2}k_\nu$, is a hypothesis (§7, Eq. 58, Figs. 10–12). **Shown** (scale shift), mechanism **Stated**
24. In the kinematic stage $E_B(k)\sim k^2E_{\mathrm s}(k)$ up to the ratio peak, flattening to $\sim kE_{\mathrm s}(k)$ at saturation; the equipartition wavenumber moves from $k\approx100$ to $k\approx10$ ($P_\nu=\infty$) (§8, Fig. 13). **Shown**
25. Resolution: integral statistics and growth rates converge by $256^3$; $P_\nu=0.1$ is "converged on all scales at $512^3$"; for $P_\nu=1$ the shear-viscous wavenumber is resolved between $256^3$ and $512^3$ but the bulk-viscous one is not resolved even at $1024^3$ (App. D, Figs. D1–D4). **Shown**
26. For $P_\nu=\infty$ the high-$k$ compressible modes should never converge and $E_{\mathrm c}(k)/E_{\mathrm s}(k)$ should "grow unbounded" with resolution, "which exactly what one expects for an ILES" (App. D). **Stated**
27. A "compressible DNS where all viscous scales are resolved" needs both $\nu_b$ and $\nu$ with $P_\nu\sim1$; otherwise "the grid controls the dissipation of the compressible modes", turning "what is usually considered a direct numerical simulation (DNS) into an implicit large eddy simulation for the compressible modes" (§9.1). **Stated**, supported by §6 and App. D
28. The explicit diffusion step adds a bulk-viscous time-step limit, $\Delta t\le\mathrm{CFL}\,\min(\tfrac12h^2/\nu,\tfrac12h^2/\nu_b,\tfrac12h^2/\eta_m)$; the $P_\nu=0.001$ run was not taken to saturation because of this cost (App. F1, Eq. F13, Table 1). **Stated**
29. Verification: 3D ($288^3$) and 2D ($1024^2$) bulk-viscous Sedov–Taylor blasts show isotropic damping and the diffusion of $\nabla\cdot\boldsymbol u$ with increasing $\nu_b$; space–time spectra match the linear bulk-damped sound-wave dispersion qualitatively (App. F2, Eqs. F14–F15, Figs. E1–E2, F1). **Shown**
30. For Braginskii-MHD viscosity the decomposition reveals a bulk-viscous-type term $\sim\hat B_i\hat B_j\,\tfrac13S_{kk}\delta_{ij}$ that would damp the fast and slow magnetosonic waves along the field (§9.3). **Stated**

The viscous stress used (Eq. 11), in registry notation:
$$\sigma_{ij}=2\nu S^d_{ij}+\nu_bS_{kk}\delta_{ij},\qquad\nu_b=\lambda_{\mathrm v}+\tfrac23\nu\ \text{(footnote 2)},$$
with $\lambda_{\mathrm v}$ the second viscosity coefficient and the momentum flux $\nabla\cdot(\rho\sigma)$, so that both coefficients are kinematic.

# Printed slips

- After Eq. 11: "where $\nu_{\rm shear}$ and $\nu_{\rm bulk}$ are the coefficients of bulk viscosity and the shear viscosity, respectively" (order swapped).
- Eq. 47, "$\boldsymbol\sigma=2\nu_{\rm shear}\mathbb S+\nu_{\rm bulk}\mathbb B$, using the same definitions as in Section 2.1": with Eq. 7, $\mathbb B=\tfrac13(\nabla\cdot\boldsymbol v)\mathbb I$, this is one third of the bulk term of Eqs. 11 and 16 *(compiler check, not in the sources)*.
- Eq. 13 text: "for translational and vibrational degrees of freedom", while the superscript and Eq. 14 are rotational; §2.1 writes "$\tau_v=\mathcal O(\mathrm{yrs})$" for rotational relaxation times (App. B uses $\tau_r$).
- App. B1: "$\gamma=1-R/c_V$"; with $\gamma=c_p/c_V$ and $c_p-c_V=R$ the relation is $\gamma=1+R/c_V$ *(compiler check, not in the sources)*. App. B1 refers to "Section 1" for a discussion that is in §2.1.
- Footnote 3: "$k_0=\ell_0/(2\pi)$" (a wavenumber written as a length); "Parsevel's theorem".
- Cross-references: §4.3 cites "Equation 23" for $Re$ (Eq. 22) and "Equation 26" for $Pm$ (Eq. 28); §4.5 sends to Appendix F for the energy equations of Appendix E; Figs. E1–E2 sit in Appendix F.
- §3.1: "the $E_{\rm kin,\perp}(k)\sim k^{-2}$ spectrum is not universally measured", where the context (the $k^{-3}$ alternative) is the compressible spectrum.
- Magnetic tension: $+\frac1{4\pi}\boldsymbol b\otimes\boldsymbol b$ inside the flux of Eq. 16, $-\frac1{4\pi}\boldsymbol b\otimes\boldsymbol b$ in Eq. 44.
- Eqs. 9–10: with $\nabla\otimes\boldsymbol v=\partial_iv_j$, Eq. 9 gives $\tfrac12(\partial_iv_j-\partial_jv_i)$ while Eq. 10 prints $\tfrac12(\partial_jv_i-\partial_iv_j)$ (no effect on results, the winding term vanishing either way).
- §5.2: "$t_{\nu_{\rm bulk}}\sim(\ell_0^2/\nu_{\rm bulk})^{-1}\sim t_0$", the inverse of a time, against §1's $t_\nu\sim(k_\nu^2\nu)^{-1}$.
- §5.2: "$2\gamma_1t_0=1.40\pm0.02-1.48\pm0.03$, i.e., every $1.4t_0$ (e-fold time)"; a rate of $1.4/t_0$ e-folds the energy every $t_0/1.4\approx0.71\,t_0$ *(compiler check, not in the sources)*, and "1.40 ± 0.02" is not a Table 1 entry.
- §5.2 against Table 1: the growth rate is "significantly affected" at "$P_\nu\le0.01$", but Table 1 gives $1.46\pm0.03$ at $P_\nu=0.01$, inside the range of the other runs; only $P_\nu=0.001$ (1.28) is lower.
- §4.2 against §5.1: the forcing has "$f^2_\perp/f^2_\parallel=2$, corresponding to 2:1 energy", while §5.1 says the compressible modes are replenished "with the same amount of energy as the incompressible modes".
- §5.1 and Fig. 6 caption: line styles (text: compressible solid; caption: "incompressible (solid) and compressible (dashed)"); "the final saturation of the $\boldsymbol v_\parallel$ modes … $\langle E_{\rm mag}\rangle/\langle E_{\rm kin,\perp}\rangle\approx0.1$ … However, the same is not true for the $\boldsymbol v_\parallel$ modes"; the caption's "$\langle E_{\rm kin,\parallel}\rangle/\langle E_{\rm mag}\rangle<1$" for the incompressible modes.
- §7: "the field is small-scale ($k_{{\rm cor},b}\ell_0<1$)", while the Fig. 11 caption has $k_{{\rm cor},b}\ell_0>1$.
- Fig. 13 caption: "superequipartition k modes ($E_{\rm mag}(k)/E_{\rm kin,\perp}(k)<1$)" against its own definition of subequipartition.
- Eqs. 56–57 (E9–E10) carry no minus sign on a dissipative right-hand side; Eq. E2 transforms $\nabla^2$ to $+k^2$.
- Eq. E1: the coefficient of $\nabla(\nabla\cdot\boldsymbol v)$ is printed $(2\nu_{\rm shear}/3+\lambda)=\nu_{\rm bulk}$; for constant coefficients $\partial_j\sigma_{ij}=\nu\nabla^2u_i+(\nu_b+\nu/3)\partial_i(\nabla\cdot\boldsymbol u)$, so the longitudinal damping in Eq. E5 would be $\tfrac43\nu+\nu_b$ rather than $\nu+\nu_b$; the decoupling conclusion is unaffected *(compiler check, not in the sources)*.
- App. F1, Eqs. F1, F6, F11: the same-direction term $-\frac{\nu_{\rm bulk}}{2\Delta x}(v_{x,ijk}-v_{x,i-1jk})$ approximates half of $\nu_b\partial_xu$, while the cross terms over $4\Delta y$ approximate the full $\partial_yv$, and each sweep is summarised as "$\approx\nu_{\rm bulk}(\partial_xv_x+\partial_yv_y+\partial_zv_z)$" without the sign (*compiler check, not in the sources*; a possible factor-two inconsistency).
- App. F: viscosities in units of "$L^2/t_c$" with $t_c$ undefined (the defined time is $t_s=L/c_s$); Eqs. F14–F15 divide $\nu_{\rm bulk}$ by $\rho_0$, treating it as a dynamic coefficient.
- §9.1 calls $P_\nu$ "the ratio between the bulk and shear viscosities", against Eq. 24, $\nu_{\rm shear}/\nu_{\rm bulk}$.
- Typos: "miscroscale", "formerly" for "formally", "This could is likely because", "which exactly what one expects", "sube-quipartition".
- References: Schekochihin, Boldyrev & Kulsrud 2002b and 2002c are printed identically (ApJ 567, 828) and cited under both labels.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\boldsymbol v$ (also $\boldsymbol u$ in §6.2, App. F) | $\boldsymbol u$ | |
| $\boldsymbol b$ | $\boldsymbol B$ (Gaussian units) | **collision:** the registry's $\boldsymbol b$ is the fluctuation in velocity units; here $E_{\mathrm{mag}}=b^2/8\pi$ |
| $\nabla\otimes\boldsymbol v=\partial_iv_j$ | $(\partial_ju_i)^T$ | **collision:** index order transposed relative to the registry's $\partial_ju_i$ |
| $\mathbb B=\tfrac13(\nabla\cdot\boldsymbol v)\mathbb I$ | $\tfrac13S_{kk}\delta_{ij}$ | "rate of expansion"; **collision:** not a magnetic field |
| $\mathbb S$ | $S^d_{ij}$ | traceless strain, no norm used |
| $\mathbb A$ | $\Omega_{ij}$ (Eq. 10 sign) | Eq. 9 gives $-\Omega_{ij}$ (Printed slips) |
| $\boldsymbol\sigma$ | $\sigma_{ij}/\rho$ (kinematic) | includes the bulk term; momentum flux $\nabla\cdot(\rho\boldsymbol\sigma)$ |
| $\nu_{\rm shear}$ | $\nu$ | |
| $\nu_{\rm bulk}$ | $\nu_b$ (page-local, kinematic) | $=\lambda+\tfrac23\nu$; dynamic in App. F |
| $\lambda$ | $\lambda_{\mathrm v}$ (page-local, second viscosity) | **collision:** not the Taylor microscale or the MHD perpendicular scale |
| $\eta$ | $\eta_m$ | **collision:** not the Kolmogorov length |
| $\mathrm{Re_{shear}}$, $\mathrm{Rm}$, $\mathrm{Pm_{shear}}$ | $Re$, $Rm$, $Pm$ | real-space, on $\ell_0$ and the rms velocity (footnote 3) |
| $\mathrm{Re_{bulk}}$, $\mathrm P\nu$, $\mathrm{Pm_{bulk}}$ | $Re_{\mathrm{bulk}}$, $P_\nu=\nu/\nu_b$, $Pm_{\mathrm{bulk}}$ (page-local) | the paper's new numbers; $P_\nu=\infty$ means no explicit bulk viscosity |
| $\mathcal M$ | $M_t$ | rms sonic Mach number |
| $\mathcal M_A$ | (Alfvén Mach number) | |
| $\gamma$, $\gamma_1$, $\gamma_2$ | $\gamma_B$ (page-local) instantaneous growth rate; $\Gamma_E=2\gamma_1$; (nonlinear growth rate) | **collision:** $\gamma$ is also the ratio of specific heats (§2.1, Apps. B, F) |
| $\boldsymbol v_\parallel$, $\boldsymbol v_\perp$ | $\boldsymbol u_{\mathrm c}$, $\boldsymbol u_{\mathrm s}$ (page-local) | **collision:** $\parallel$ means longitudinal in $\boldsymbol k$, not along the magnetic field ($l_\parallel$) |
| $E_{\rm kin,\parallel}(k)$, $E_{\rm kin,\perp}(k)$, $E_{\rm mag}(k)$ | $E_{\mathrm c}(k)$, $E_{\mathrm s}(k)$, $E_B(k)$ | shell spectra with constant $\rho_0$ |
| $\ell_0$, $k_0$, $L$ | $\ell_0$ (driving scale, page-local), (driving wavenumber), (box size) | $\ell_0=L/2$; **collision:** $L$ is not the integral scale |
| $t_0$ | (forcing correlation time $\ell_0/\langle u^2\rangle^{1/2}$) | time unit |
| $k_{\nu_{\rm shear}}$, $k_{\nu_{\rm bulk}}$, $k_\eta$ | $k_\nu$, $k_{\nu_b}$, $k_{\eta_m}$ | dissipation wavenumbers |
| $k_{{\rm cor},b}$ | $k_{\mathrm{cor}}$ (page-local) | magnetic correlation wavenumber, Eq. 58 |
| $\langle\cdot\rangle_{\mathcal V}$ | $\langle\cdot\rangle$ (volume average) | |
| $\boldsymbol\omega$ | $\omega_i$ | **collision:** $\omega$ is also a wave frequency (§2.1, App. F) |
| $\beta$ | $\beta_p$ | initial $\beta_p=10^{10}$ |
| $\boldsymbol f$ | $f_i$ | Ornstein–Uhlenbeck forcing |
| $N^3$ (Table 1) | $N_x^3$ | **collision:** not a polynomial degree |
| $\Delta x$ | $h$ | cell size |

# Reference list

160 printed references, author–year style with a/b/c suffixes. The list is
merged complete into the [bibliography](/bibliography.md) with `citedby` this
slug. The cited Beattie et al. 2025a (Nature Astronomy) is a different work
from this source and takes the key `beattie-2025-b`; preprints (among them Beattie et al.
2025b, arXiv:2501.09855, `beattie-2025-c`) are kept as their own entries. Schekochihin et al.
2002b and 2002c are printed identically (a printed duplicate, folded into `schekochihin-2002-b`). Several items
print no pages or volume (Federrath et al. 2010, 2021; Federrath & Klessen
2012; Chen et al. 2019; Sur & Subramanian 2023) or no publisher (Choudhuri
1998, Draine 2011, Frisch 1995).

# Pages created or updated

Chunk 6 (2026-10-26). This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Bottleneck effect in the energy spectrum](/definitions/bottleneck-effect.md)
- [Bulk viscosity](/definitions/bulk-viscosity.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Compressible MHD turbulence](/results/compressible-mhd-turbulence.md)
- [Small-scale turbulent dynamo](/results/small-scale-dynamo.md)
