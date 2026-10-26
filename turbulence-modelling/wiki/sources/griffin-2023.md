---
type: Source
title: "Griffin et al. (2023) — Near-wall model for compressible turbulent boundary layers based on an inverse velocity transformation"
description: "Proposes a one-ODE compressible wall-stress model that maps the incompressible mixing-length solution through the inverse total-stress-based velocity transformation and closes temperature with a matching-anchored generalized Reynolds analogy, more accurate than the classical model under strong heat transfer in a priori and a posteriori tests."
resource: "doi:10.1017/jfm.2023.627"
source_kind: paper
authors: [Griffin K.P., Fu L., Moin P.]
year: 2023
venue: "J. Fluid Mech. 970:A36"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Journal_of_Fluid_Mechanics_Griffin_Near-wall_model_for_compressible_turbulent_boundary_layers_b.pdf"
tags: [wall-model, wmles, compressible, hypersonic, boundary-layer]
timestamp: 2026-10-25T13:44:00Z
---

# Summary

Griffin et al. (2023) propose a wall-stress model for
[wall-modelled LES](/methods/wall-modelled-les.md) of compressible, high-speed
wall-bounded turbulence with heat transfer. The classical ODE-based
[equilibrium wall model](/methods/equilibrium-wall-model.md) solves two
coupled one-dimensional RANS equations: streamwise momentum with a
van Driest-damped mixing-length eddy viscosity, and total energy with a
constant turbulent Prandtl number $Pr_t=0.9$. The authors argue that it is hard
to converge with strong heat transfer, because two nonlinear boundary-value
problems are iterated together. They also argue that it is inaccurate there,
because its damping function implicitly embeds the van Driest velocity
transformation and its energy equation a constant $Pr_t$.

The [inverse-velocity-transformation wall model](/methods/inverse-velocity-transformation-wall-model.md)
replaces both ingredients. It solves only the incompressible, constant-property
mixing-length equation. It maps the resulting strain rate to the compressible
one through the inverse of the total-stress-based
[compressible velocity transformation](/definitions/compressible-velocity-transformation.md)
of Griffin, Fu & Moin (2021c). It closes the temperature with an algebraic
temperature–velocity relation from the generalized Reynolds analogy of Zhang
et al. (2014), whose quadratic coefficient is fixed by the temperature at the
matching height rather than at the boundary-layer edge. One ODE is integrated
by shooting on $\tau_w$. The inputs are the mean state at one matching height
and at the boundary-layer edge.

[A priori](/definitions/a-priori-and-a-posteriori-testing.md) tests on 48 DNS
cases (channels, pipes, diabatic boundary layers; edge Mach 0.77–11;
$Re_\tau^*$ 170–5700; matching at $0.3\delta$) show the new model much more
accurate than the classical one, with the largest gains at strong wall
cooling. It also beats two semi-local damping variants in boundary layers with
strong heat transfer. A posteriori WMLES of nine compressible
[channel flows](/benchmarks/turbulent-channel-flow.md) in
[CharLES](/software/charles.md) ($M_b$ 0.7–4, 12 points per half-height)
reproduces the DNS mean profiles, $\tau_w$ and $q_w$ with errors that do not
grow with the heat flux. The classical model's errors do grow with the heat
flux, and its log-layer intercept error persists under grid refinement, which
the authors attribute to the wall model rather than to numerical or SGS error. The cost is between 7% lower and 32% higher
than that of the classical model.

# Version read

Version of record (J. Fluid Mech. 970:A36, open access CC-BY 4.0; received 3
December 2022, accepted 22 July 2023), 22 pages (A36-1 to A36-22). The metadata
above are those of this published version; the page matches the metadata card.
A CTR Annual Research Briefs report of 2022 by the same authors carries the
same title; it is an earlier, distinct work in the reference list.

# Key claims

In registry notation $U=\langle u\rangle_\rho$ and $T=\langle T\rangle_\rho$
are the Favre-averaged streamwise velocity and temperature, subscripts $w$,
$e$ and $m$ denote the wall, the boundary-layer edge and the matching height
$h_{\mathrm{wm}}$, and $(\cdot)^*$ is the semi-local scaling.

1. Wall-resolved LES cost (grid points times time steps) of a turbulent boundary layer scales as $Re^{2.7}$ and wall-modelled LES as $Re^{1.1}$ (§1, citing Yang & Griffin 2021). **Stated**
2. The classical compressible wall model solves $\frac{d}{dy}\left((\langle\mu\rangle+\mu_t)\frac{dU}{dy}\right)=0$ with $\mu_t=\kappa y\langle\rho\rangle\sqrt{\tau_w/\langle\rho\rangle}\,(1-e^{-y^+/A^+})^2$, $\kappa=0.41$, $A^+=17$, together with a total-energy equation with $Pr_t=0.9$ (Eqs. 1.1–1.3; the exponent's sign is a printed slip, see below). Its two coupled boundary-value problems can be hard to converge with strong heat transfer (§1, citing Fu et al. 2021). **Stated**
3. The damping function of the classical model is consistent with the van Driest velocity transformation. Rewritten in $y^*$, it is consistent with the Trettel–Larsson transformation (§3, citing Yang & Lv 2018). **Stated**
4. The new model differs from the classical one in exactly two respects: an incompressible momentum equation with an inverse velocity transformation instead of a compressible one, and an algebraic temperature–velocity relation instead of a constant-$Pr_t$ energy equation (§2). **Stated** (design)
5. The inverse transformation (Eq. 2.2) follows by algebraic rearrangement of the forward total-stress-based transformation $S_t^+=S_{eq}^+/(1+S_{eq}^+-S_{TL}^+)$ (Eq. 2.1), with $S_{eq}^+=(1/\mu^+)\,dU^+/dy^*$ and $S_{TL}^+=\mu^+\,dU^+/dy^+$: $\frac{dU^+}{dy^*}=\left(\frac{1}{\mu^+S_t^+}-\frac1{\mu^+}+\sqrt{\rho^+}\left(1+\frac{y^+}{2\rho^+}\frac{d\rho^+}{dy^+}-\frac{y^+}{\mu^+}\frac{d\mu^+}{dy^+}\right)\right)^{-1}$ (§2.1). **Derived**
6. The constants $\kappa$ and $B$ of the incompressible law are used with $Re_\tau^*$ in place of $Re_\tau$, because $Re_\tau^*$ is invariant under the transformation (§2.1). **Stated**
7. The total-stress-based transformation assumes a constant-stress layer in the buffer region. Griffin et al. (2021c) found this does not significantly affect accuracy in equilibrium flows, and Bai, Griffin & Fu (2022) found the same for moderate pressure gradients (§2.1). **Stated**
8. The constant-$Pr_t$ assumption is less accurate than the generalized Reynolds analogy (§2.2, citing Zhang et al. 2014). **Stated**
9. The temperature–velocity relation $T=T_w+s\,Pr\,(T_r-T_w)\frac{U}{U_e}\left(1-\frac{U}{U_m}\right)+\left(\frac{U}{U_m}\right)^2(T_m-T_w)$ (Eq. 2.5), with Reynolds analogy factor $s=1.14$, recovery factor $r=Pr^{1/3}$ and $T_r=T_e+rU_e^2/(2c_p)$, enforces the exact matching temperature. As a consequence, $q_w=s\tau_wc_p(T_w-T_r)/U_e$ ties the wall heat flux algebraically to the wall stress (§2.2). **Derived**
10. Beyond the inputs of the classical model, the new model needs the velocity and temperature at the boundary-layer edge, found with the method of Griffin, Fu & Moin (2021a) (§2.3). **Stated**
11. Only one ODE is solved: shooting with an initial guess for $\tau_w$, sub-iterating at each step to satisfy Eq. 2.5 and the resulting density and viscosity (§2.3). **Stated**
12. A priori, with $h_{\mathrm{wm}}=0.3\delta$, the new model's velocity and temperature profiles agree with DNS "significantly better" than the classical model in all cases shown (4 channels, 2 pipes, 2 boundary layers) (§3, Figs. 1–4). **Shown**
13. Over 48 DNS cases (edge Mach 0.77–11, $Re_\tau^*$ 170–5700, only $Re_\tau^*>150$ analysed), the new model has much smaller wall-stress and heat-flux errors than the classical model, with the greatest reduction at the highest non-dimensional heat transfer (§3, Fig. 5). **Shown**
14. Reynolds-number-dependent $\kappa$ and $A^+$ fitted to incompressible channel DNS (Lee & Moser 2015; $Re_\tau=182$–$5190$, $\kappa=0.391$–$0.408$, $A^+=16.5$–$18.2$) give a modest improvement at $Re_\tau^*=190$, $M_b=1.7$ and no significant change at $Re_\tau^*=590$, so the constants $\kappa=0.41$, $A^+=17$ are kept (§3, Fig. 6). **Shown**
15. The residual mismatch at low $Re_\tau^*$ is attributed to the documented error of the compressible velocity transformation at $Re_\tau^*\lesssim200$ (§3). **Stated**
16. In channel flows the new model and the semi-local variants of Yang & Lv (2018) and Chen et al. (2022) all perform well, and only the classical model fails, because the Trettel–Larsson and total-stress-based transformations both outperform van Driest in channels (§3, Fig. 7a–d). **Shown**
17. In cooled and heated diabatic boundary layers the classical model is the least accurate, and the two semi-local variants perform almost identically. The new model improves the log slope of the velocity (substantially for the cooled wall, slightly for the heated wall) and the temperature only slightly (§3, Fig. 7e–h). **Shown**
18. A posteriori WMLES (CharLES; the nine channel cases of Table 1; 12 points per half-height; $h_{\mathrm{wm}}=0.3\delta$): the new model is much more accurate than the classical model for mean velocity and temperature in all cases (§4, Figs. 8–9). **Shown**
19. A posteriori, the classical model's $\tau_w$ and $q_w$ errors grow significantly with heat transfer, while the new model's errors are small and independent of the heat flux (§4, Fig. 10). **Shown**
20. The new model is between 7% faster and 32% slower than the classical model, depending on Reynolds number, matching height and Mach number, with an unoptimised implementation and no load balancing (§4). **Shown** (no hardware stated)
21. Resolved fluctuation statistics improve with the new model, which the authors call "likely a consequence of its improved mean statistics". LES fluctuations are generally overpredicted against DNS, which the authors attribute partly to the wall-blocking effect of stress-based wall models and partly to numerical and SGS errors at the coarse resolution. A turbulent Mach number $M_t\sim0.3$ suggests dilatational-dissipation modelling as a next step (§4, Figs. 11–12). **Shown** / **Stated**
22. Grid study at fixed $h_{\mathrm{wm}}=0.3\delta$ ($M_b=3.0$, $Re_\tau^*=590$; 9, 18 and 36 points per half-height; $2.0\times10^4$ to $1.3\times10^6$ control volumes against $6.4\times10^8$ in the DNS): both models are only weakly grid dependent. The classical model's log-intercept error persists with refinement, so its leading error is the wall model, not numerical or SGS error (§4.1, Fig. 13). **Shown**
23. Grid study with $h_{\mathrm{wm}}$ moving with the grid ($0.3\delta$, $0.15\delta$, $0.075\delta$ for 12, 24, 48 points, stated as four wall-normal grid spacings): the new model is accurate and insensitive to resolution at $Re_\tau^*=590$ and 200. The classical model converges non-monotonically at $Re_\tau^*=200$, because its relative error peaks in the buffer and early log layer and $h^*_{\mathrm{wm}}$ enters the buffer region (§4.1, Figs. 14–15). **Shown**
24. A matching height of at least three grid spacings is a typical WMLES choice (Kawai & Larsson 2012). The persistent error at the first off-wall point agrees with Kawai & Larsson (2012) and is harmless because the inner solution applies below $h_{\mathrm{wm}}$ (§4.1). **Stated**
25. The model's accuracy is bounded by that of the forward velocity transformation and of the temperature–velocity relation. Complex flows, such as blunt-body boundary layers behind curved shocks, still need validation (§5). **Stated**
26. The authors attribute the gains to (1) replacing the constant $Pr_t$ with the algebraic temperature–velocity relation and (2) replacing the van Driest transformation with the total-stress-based transformation (§5). **Stated**

# Printed slips

- **Eq. 1.2 (p. A36-2).** Printed $\bar\mu_t=\kappa y\bar\rho\sqrt{\tau_w/\bar\rho}\,(1-\exp(y^+/A^+))^2$, without the minus sign in the exponent. As printed, the factor grows without bound away from the wall, which contradicts the text's description of a damping function that tends to the undamped mixing length; the damping form is $(1-\exp(-y^+/A^+))^2$.
- **Value of $\kappa$ (§3, p. A36-8).** "rather than letting the von Kármán constant $\kappa$ and the damping coefficient $A^+$ be fixed values of 4.1 and 17, respectively". §1 and the end of §3 give $\kappa=0.41$.
- **Case naming (§4.1).** The text names the first grid-study case "$M_b=3.0$ and $Re_\tau=1800$", the Fig. 13 caption "$M_b=3.0$ and $Re_\tau^*=590$". Table 1 shows they are the same case ($Re_\tau=1842$, $Re_\tau^*=589.7$).
- **Matching height in grid spacings (§4.1, p. A36-16)** *(compiler check, not in the sources)*. The text states that $y_m=0.3\delta$, $0.15\delta$ and $0.075\delta$ with 12, 24 and 48 points per half-height "corresponds to $y_m=4\Delta$ for all cases". On a uniform spacing $\delta/12$, $\delta/24$, $\delta/48$ each case gives $3.6$ spacings. The paper defines $\Delta$ as "the wall-normal grid spacing near the wall" (§4.1) but does not give its value on the hexagonally close-packed mesh.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| overline ($\bar\rho$, $\bar\mu$, $\bar\mu_t$) | $\langle\rho\rangle$, $\langle\mu\rangle$, $\mu_t$ | **collision:** the source's overline is a Reynolds average, the registry's an LES filter |
| tilde ($\tilde U$, $\tilde T$) | $\langle u\rangle_\rho$, $\langle T\rangle_\rho$ | **collision:** the source's tilde is a Favre average, the registry's a Favre filter |
| $(\cdot)''$ | $(\cdot)''$ | Favre fluctuation; agrees |
| $y$ | $y$ | wall-normal; agrees |
| $\tau_w$, $q_w$, $u_\tau=\sqrt{\tau_w/\bar\rho_w}$ | $\tau_w$, $q_w$, $u_\tau$ | agree |
| $(\cdot)^+$ | $(\cdot)^+$ | wall units with $u_\tau$, $\rho_w$, $\nu_w$ |
| $(\cdot)^*$, $u_{sl}=\sqrt{\tau_w/\bar\rho(y)}$ | $(\cdot)^*$, $u_\tau^*$ | semi-local scaling; agrees |
| $Re_\tau^*=\bar\rho_eu_{sl}\delta/\bar\mu_e$ | $Re_\tau^*$ | semi-local friction Reynolds number |
| $\kappa=0.41$, $A^+=17$, $B$ | $\kappa$, $A^+$, $B$ | agree |
| $y_m$, $y_m^*$ | $h_{\mathrm{wm}}$, $h^*_{\mathrm{wm}}$ | matching height; default $0.3\delta$ |
| $\Delta$ | (near-wall wall-normal grid spacing) | **collision:** registry $\Delta$ is the filter width |
| $S_t^+$, $S_{eq}^+$, $S_{TL}^+$ | (transformation strain-rate scalings) | Eq. 2.1 |
| $C_p$ | $c_p$ | **collision:** registry $C_p$ is the pressure coefficient |
| $s=1.14$, $r=Pr^{1/3}$, $\tilde T_r$ | (Reynolds analogy factor, recovery factor, recovery temperature) | |
| $b_0$, $b_1$, $b_2$ | (coefficients of the quadratic $T(U)$) | Eq. 2.4 |
| $B_q=q_w/(C_p\tilde T_w\bar\rho_wu_\tau)$ | (wall heat-flux parameter) | negative for cooled walls |
| $\epsilon_{\tau_w}$, $\epsilon_{q_w}$ | (relative model errors, %) | **collision:** registry $\varepsilon$ is the dissipation rate |
| $M_b$, $M_e$, $M_t$ | $M_b$, $M_e$, $M_t$ | $M_b$ uses the wall sound speed |
| $\delta$ | $\delta$ | channel half-height or boundary-layer thickness |

# Reference list

52 printed references, author–year style (JFM), alphabetical. The list is
merged complete into the [bibliography](/bibliography.md) with `citedby` this
slug. Griffin, Fu & Moin (2022a), a CTR Annual Research Briefs report with the
same title as this paper, is a distinct earlier work. Pirozzoli & Bernardini
(2011) is listed but not cited in the text. Same-year items are disambiguated
in printed order (Griffin, Fu & Moin 2021a–c and 2022a–b; Volpiani et al.
2020a–b). Van Driest (1951) is recorded with its printed pages "145–216". No
printed duplicates or unparseable items.

# Pages created or updated

Chunk 1 (2026-10-25), cited further in chunk 2. This source is cited on:

- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Compressible velocity transformations](/definitions/compressible-velocity-transformation.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Log-layer mismatch](/definitions/log-layer-mismatch.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Equilibrium wall model](/methods/equilibrium-wall-model.md)
- [Inverse-velocity-transformation wall model](/methods/inverse-velocity-transformation-wall-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
- [CharLES](/software/charles.md)
