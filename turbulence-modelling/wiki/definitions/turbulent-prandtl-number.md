---
type: Definition
title: "Turbulent Prandtl number and turbulent heat-flux models"
description: "The turbulent Prandtl and Schmidt numbers close the turbulent heat and species fluxes by gradient diffusion; the sources measure them far from constant in film cooling, reacting boundary layers, shock interactions and cooling flows, find the heat flux misaligned with the mean temperature gradient, and propose variable, nonlinear and learned heat-flux closures."
status: established
aliases: [turbulent Prandtl number, Pr_t, turbulent Schmidt number, Sc_t, gradient-diffusion hypothesis, GDH, generalized gradient-diffusion hypothesis, GGDH, HoGGDH, eddy-diffusivity heat flux, turbulent heat-flux model]
tags: [rans, eddy-viscosity, compressible, boundary-layer, data-driven, combustion]
timestamp: 2026-10-28T12:22:00Z
---

# Turbulent Prandtl number and turbulent heat-flux models

The turbulent Prandtl number $Pr_t$ is the ratio of the eddy viscosity to the
eddy diffusivity of heat; the turbulent Schmidt number $Sc_t$ (page-local) is
the same ratio for a species or a mixture fraction. Both define the
*gradient-diffusion hypothesis* (GDH), the scalar analogue of the
[Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md): the turbulent
heat flux is taken parallel to the mean temperature gradient,

$$-\langle u_i'T'\rangle=\alpha_{\mathrm{th},t}\,\partial_i\langle T\rangle,\qquad \alpha_{\mathrm{th},t}=\frac{\nu_t}{Pr_t},$$

with $\alpha_{\mathrm{th},t}$ the turbulent diffusivity (page-local, after
[Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md), Eq. 9), and the RANS or
SGS closure then needs only $\nu_t$ and a value of $Pr_t$ (Favre-averaged or
filtered forms carry $\rho$ and the tilde of the registry). The sources measure
$Pr_t$ and $Sc_t$ in DNS and LES, find both far from the constants used in
practice and the flux misaligned with the gradient, and propose variable,
nonlinear and learned closures. Morkovin scaling, the Reynolds analogies and
earlier compressible $Pr_t$ results are on
[Morkovin's hypothesis](/definitions/morkovin-hypothesis.md); this page
collects the closure question.

## Definitions measured from data

In a statistically two-dimensional wall flow the sources evaluate $Pr_t$ from
the wall-normal fluxes, as the ratio of the eddy viscosity implied by the
shear stress to the eddy diffusivity implied by the heat flux:

$$Pr_t=\frac{\langle\rho u''v''\rangle\,\partial_y\langle T\rangle_\rho}{\langle\rho v''T''\rangle\,\partial_y\langle u\rangle_\rho},\qquad
Sc_t=\frac{\langle\rho u''v''\rangle\,\partial_y\langle Y\rangle_\rho}{\langle\rho v''Y''\rangle\,\partial_y\langle u\rangle_\rho},$$

with $Y$ the mixture fraction (Wei et al. 2023, Eqs. 40–41, for resolved LES
statistics) or a species mass fraction (Wang & Xu 2024, Eqs. 5.2–5.3, for
DNS) ([Wei et al. (2023)](/sources/wei-2023.md);
[Wang & Xu (2024)](/sources/wang-2024-h.md)). Wang & Xu note that this $Pr_t$
is discontinuous where $\langle\rho v''T''\rangle$ changes sign, and argue that
the discontinuities "may not raise specific concerns" for closure, because
$\partial_y\langle T\rangle_\rho$ vanishes there too and any finite $Pr_t$
then gives a near-zero flux (§5.2).

Yu et al. (2023b) instead fit a best eddy diffusivity to the full flux vector
by least squares,
$\alpha_{\mathrm{th},t}=-\langle u_i'T'\rangle\partial_i\langle T\rangle/(\partial_k\langle T\rangle\partial_k\langle T\rangle)$,
the analogue of the best-fit eddy viscosity of the Boussinesq page
([Yu et al. (2023b)](/sources/yu-2023-b.md), §IV, Eqs. 22–23; their
conductivity $\kappa_T$ multiplies a kinematic flux, so it is a diffusivity
here).

## Measured values

| Flow | $Pr_t$ (and $Sc_t$) | Source |
|---|---|---|
| Supersonic H$_2$ film cooling (Burrows–Kurkov, $M=2.44$), wall-resolved LES, no chemistry | mixing-layer $Pr_t$ falls from 1.5 at $x=0.05$ m to 1.0 at $x=0.3$ m, $Sc_t$ similarly | Wei et al. (2023), §IV F, Figs. 34–35 |
| Same, reacting | a narrow near-wall region of high $Pr_t$, $Sc_t$ and a slender low-$Pr_t$ region near $y=0$; all values between 0 and 2 | Wei et al. (2023), §IV F |
| Supersonic reacting boundary layer, DNS ($M=2.33$, $Re_\tau\approx1000$) | $Pr_t\approx1.1$ in the log region, 0.5–0.9 in the outer layer, reacting and non-reacting alike; reaction changes $Sc_{t,i}$ only slightly | Wang & Xu (2024), §5.2–5.3, Fig. 18 |
| Pulsating separated, thermally stratified flow (DNS of Wissink et al. 2004, as cited) | 0.4 to 4 | [Sandberg & Michelassi (2022)](/sources/sandberg-2022.md), §3.2.3 |
| Trailing-edge cooling slots, learned spatially varying $1/Pr_t$ (Haghiri & Sandberg 2020, as cited) | mean 0.42–0.6, against the "typical" 0.85–0.9 | Sandberg & Zhao (2022), §4.2.1 |
| Same, CFD-driven learned model (Lav et al. 2021; Lav & Sandberg 2020, as cited) | mean 0.32 (trained at blowing ratio 1.26); 0.471 (URANS stochastic closure) | Sandberg & Zhao (2022), §4.2.1, §4.4.2 |

Wang & Xu report their log-region and outer values as consistent with the
film-cooling DNS of Peter & Kloker (2022) (§5.2). Yu et al. (2023b) state that
the $Pr_t$ relating shear stress and heat flux is below unity in the
non-equilibrium zone of a shock/boundary-layer interaction (§V). The constants
used in practice are $Pr_t=0.9$ for SST RANS (Sandberg & Zhao 2022, §2.3) and,
for SGS closures, $Pr_t=0.85$ with $Sc_t=0.7$ in Wei et al.'s dynamic
one-equation LES (§II B, Eqs. 14–15) and $Pr_t=Sc_t=0.7$ in the
[Vreman-model](/methods/vreman-model.md) LES of a rotating detonation engine
([Vignat et al. (2024)](/sources/vignat-2024.md), §3.3), where Schau &
Oefelein's LES of the same engine computes $Pr_t$ and $Sc_t$ dynamically
(Table 1, as cited). Wei et al. point out that
their SGS values are constant while the resolved ones vary between 0 and 2.

For the mixture fraction $z$ (page-local) of turbulent-combustion closures,
[Salehi et al. (2024)](/sources/salehi-2024.md) write the filtered flux by
gradient diffusion, $\widetilde{u_i''z''}=-\mathcal D_t\partial_i\tilde z$
with $\mathcal D_t=\nu_t/Sc_t$ ($\mathcal D_t$ page-local), and survey the
values in use: $Sc_t=0.7$ in RANS; in LES either a dynamic $Sc_t$ or a
constant 0.4 or 0.7, the sensitivity to the choice between 0.4 and 0.7 having
been found not significant in the study they cite (Eq. 20 and the text
around it). The same gradient-diffusion form closes the progress-variable
flux there, where they note that counter-gradient transport has been reported
(Eqs. 26–27); see
[conditional source-term estimation](/methods/conditional-source-term-estimation.md).
In compressible URANS codes the constant enters the conductivity directly:
[Ye et al. (2024)](/sources/ye-2024.md) close the heat flux of their
$k$-$\omega$ SST computation of a Mach 5 swept shock/boundary-layer
interaction with the effective coefficient $c_p(\mu/Pr+\mu_t/Pr_t)$ (Eq. 6),
without printing the value of $Pr_t$.

## Misalignment and counter-gradient transport

A constant $Pr_t$ fixes the direction of the flux as well as its magnitude.
Wei et al. (2023) measure the angle between the turbulent heat flux and the
mean temperature gradient,

$$\theta_{qT}=\cos^{-1}\frac{-\langle\rho u_i''T''\rangle\,\partial_i\langle T\rangle_\rho}{\lvert\partial_i\langle T\rangle_\rho\rvert\,\lvert\langle\rho u_i''T''\rangle\rvert+\epsilon}$$

($\theta_{qT}$ page-local; Eq. 39), about $60^\circ$ above $y/s_h=1$ ($s_h$ the slot height, page-local) in the inert
and non-reacting cases (Tavoularis & Corrsin measured $65^\circ$ in
homogeneous shear, as cited), about $75^\circ$ with combustion, approaching
$90^\circ$ near the wall (§IV F, Fig. 32). The streamwise scalar flux
$\langle\rho u''Y''\rangle$ is negative, counter to the gradient-diffusion
picture (Fig. 33). The authors call the misalignment "more vital and
intractable" than the variation of $Pr_t$ (§IV F). Sandberg & Michelassi
(2022) report, from the same pulsating-flow DNS, that the heat flux was
rarely aligned with the temperature gradient (§3.3), and Sandberg & Zhao
(2022) list non-constant $Pr_t$ and counter-gradient transport among the
physics that defeats the closures in use in cooling flows (§2.3).

## Closures beyond constant $Pr_t$

**Pressure-gradient-dependent $Pr_t$.** For RANS of hypersonic
[shock/boundary-layer interactions](/benchmarks/shock-turbulent-boundary-layer-interaction.md),
Yu et al. (2023b) set, together with a wall-pressure-dependent $\beta^*$ in
the [$k$-$\omega$ SST model](/methods/k-omega-sst-model.md),

$$Pr_t=0.9-0.5\tanh\Big(10\,\Big\lvert\frac{\nabla p\,\delta}{U_\infty}\Big\rvert\Big)$$

(§V), given without derivation. With both changes the peak Stanton-number
error on the Schülein Mach 5 oblique-shock cases falls from about 50% to
below 10% (§V, Fig. 21). They cite transport-equation alternatives for $Pr_t$
(an enthalpy-variance equation of Gaffney et al. 2005; a $Pr_t$ transport
equation of Roy & Sinha 2019) (§V).

**Nonlinear algebraic heat fluxes, a priori.** On their DNS of Mach 5
oblique-shock interactions, Yu et al. (2023b) test three additions to the
linear flux, with coefficients $c_{\nabla u}$, $c_S$, $c_\Omega$ (page-local)
fitted to the residual:

$$\begin{aligned}
-\langle u_i'T'\rangle&=\alpha_{\mathrm{th},t}\partial_i\langle T\rangle+c_{\nabla u}\,\partial_k\langle T\rangle\,\partial_k\langle u_i\rangle &&\text{(Eq. 24, worse)},\\
-\langle u_i'T'\rangle&=\alpha_{\mathrm{th},t}\partial_i\langle T\rangle+c_S\,\partial_k\langle T\rangle\,\langle S^d_{ik}\rangle_\rho &&\text{(Eq. 25, minor gain)},\\
-\langle u_i'T'\rangle&=\alpha_{\mathrm{th},t}\partial_i\langle T\rangle+c_\Omega\,\partial_k\langle T\rangle\,\langle\Omega_{ik}\rangle_\rho &&\text{(Eq. 26, much better)}.
\end{aligned}$$

The linear form reconstructs the wall-normal flux upstream and downstream but
not in the interaction zone, where the rotation-based term works best (§IV,
Fig. 20). The authors caution that shock-motion-induced fluctuations should
not be modelled together with turbulent ones (§IV).

**Tensor-diffusivity expansion.** Sandberg & Zhao (2022) write the heat flux
on a basis of ten tensors $\Gamma^{(n)}_{ij}$ (page-local, after Younis et al.
2005), with the non-dimensional gradient
$\partial_i\vartheta=(\beta^*k^{3/2}/\varepsilon)\partial_i\langle T\rangle$
(page-local):

$$-\langle u_i'T'\rangle=\sqrt k\Big[a^{\mathrm h}_1\partial_i\vartheta+\sum_{n=2}^{10}a^{\mathrm h}_n\Gamma^{(n)}_{ij}\partial_j\vartheta\Big]$$

(Eq. 6), of which the GDH ($a^{\mathrm h}_1=1/Pr_t$ only, Eq. 9), the
generalized gradient-diffusion hypothesis GGDH of Daly & Harlow (only
$a^{\mathrm h}_2$, through the Reynolds stress, Eq. 12) and the HoGGDH of
Abe & Suga (only $a^{\mathrm h}_4$, Eq. 13) are special cases. The
heat-flux analogue of the stress basis of the
[explicit algebraic Reynolds-stress model](/methods/explicit-algebraic-reynolds-stress-model.md)
page is thus available to learned closures. Including temperature gradients
in the invariants violates the linearity principle for passive scalars but is
retained because temperature in compressible turbulence is not strictly
passive (§3.3).

**Learned heat-flux closures** (Sandberg & Zhao 2022, §4.2, as cited).
Recursive feature elimination on jet-in-crossflow data found that "the GDH was
not the appropriate basis while the GGDH and HoGGDH featured prominently",
and the resulting gene-expression-programming model beat eddy-diffusivity
models a posteriori (Weatheritt et al. 2020); CFD-driven training with wall
temperature in the cost gave the best trailing-edge-slot models (Lav et al.
2021); coupled stress and heat-flux closures trained by Pareto-based
multi-objective optimisation improved both fields in vertical natural
convection (Waschkowski et al. 2022) (§4.5). Sandberg & Zhao add that "no
existing RANS models have taken into account the strong coupling of heat flux
and turbulence modeling during model development" (§2.4). See
[symbolic-regression closures](/methods/symbolic-regression-closure.md).

## Consequences for predictions

- In the jet-in-crossflow comparison of Sandberg & Zhao (2022), steady SST
  RANS with $Pr_t=0.9$ gives a much reduced spanwise spread of wall
  temperature and a strongly underpredicted heat-flux magnitude, worst near
  the wall (§2.3, Fig. 5); in URANS of trailing-edge cooling, constant-$Pr_t$
  gradient diffusion overpredicts the wall temperature (§2.3, as cited).
- Wei et al. (2023) find that SST RAS of the Burrows–Kurkov film shows no
  combustion-induced friction reduction and a strong heat-flux increase,
  inconsistent with experiment and their LES; they attribute RAS failure to
  the variation of $Pr_t$, $Sc_t$ and to flux–gradient misalignment, and
  recommend anisotropic closures (v2f, RSM) (§IV F).
- Wang & Xu (2024) use the a priori $Pr_t$ and $Sc_{t,i}$ profiles, with the
  strong Reynolds analogy and its extensions (see
  [Morkovin's hypothesis](/definitions/morkovin-hypothesis.md)), to assess
  closure ingredients for reacting supersonic boundary layers (§5); see
  [a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md).

## Qualifications

- The values above belong to different flows, averages and filters (resolved
  LES statistics in Wei et al., DNS in Wang & Xu, learned spatial means in the
  works Sandberg & Zhao cite); they are not one quantity measured several
  times.
- Yu et al. (2023b) do not define $\delta$ in their $Pr_t$ formula for the
  RANS cases, and do not restate the $C_{\mu,1}$ used there (§V). Their
  heat-flux tests (Eqs. 22–26) use Reynolds fluctuations and means while
  their stress tests use Favre quantities; the mixed convention is not
  explained.
- Sandberg & Zhao's GGDH and HoGGDH forms (Eqs. 12–13) are dimensionally
  consistent only if the stress tensor there is the dimensional Reynolds
  stress, not the normalized one defined after Eq. 6 (details on their Source
  page).

# Citations

- [Wei et al. (2023)](/sources/wei-2023.md) — §II B, Eqs. (14)–(15) (SGS $Pr_t=0.85$, $Sc_t=0.7$); §IV F, Eqs. (39)–(41), Figs. 31–35 (misalignment angle, counter-gradient scalar flux, resolved $Pr_t$ and $Sc_t$); Figs. 36–37 (SST RAS comparison); Conclusions.
- [Yu et al. (2023b)](/sources/yu-2023-b.md) — §IV, Eqs. (22)–(26), Fig. 20 (best-fit diffusivity, nonlinear heat-flux terms a priori); §V, Fig. 21 (pressure-gradient $Pr_t$ in SST RANS, Stanton-number error; cited transport-equation approaches).
- [Wang & Xu (2024)](/sources/wang-2024-h.md) — §5.2–5.3, Eqs. (5.2)–(5.3), Fig. 18 ($Pr_t$ and $Sc_{t,i}$ in a reacting supersonic boundary layer; discontinuities at flux sign changes); §5.4.
- [Sandberg & Michelassi (2022)](/sources/sandberg-2022.md) — §3.2.3, §3.3 ($Pr_t$ from 0.4 to 4 and flux–gradient misalignment, as cited).
- [Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md) — §2.3, Fig. 5 (jet in crossflow, SST with $Pr_t=0.9$); §2.4; §3.3, Eqs. (6), (9), (12), (13) (tensor-diffusivity expansion, GDH, GGDH, HoGGDH); §4.2, §4.4.2, §4.5 (learned heat-flux closures).
- [Vignat et al. (2024)](/sources/vignat-2024.md) — §3.3, Table 1 (SGS $Pr_t=Sc_t=0.7$ with the Vreman model; dynamic $Pr_t$, $Sc_t$ of a cited LES).
- [Salehi et al. (2024)](/sources/salehi-2024.md) — Eq. (20) and text ($Sc_t=0.7$ in RANS; dynamic, 0.4 or 0.7 in LES; insensitivity between 0.4 and 0.7, as cited); Eqs. (26)–(27) (gradient-diffusion progress-variable flux, counter-gradient transport noted).
- [Ye et al. (2024)](/sources/ye-2024.md) — §II A, Eq. (6) (conductivity $c_p(\mu/Pr+\mu_t/Pr_t)$ in SST URANS, value not printed).
