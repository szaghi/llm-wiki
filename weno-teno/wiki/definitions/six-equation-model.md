---
type: Definition
title: "Six-equation two-phase model"
description: "The single-velocity pressure-disequilibrium model of compressible two-phase flow: two partial densities, mixture momentum, two phasic energies and a volume fraction relaxed toward pressure equilibrium. With infinite relaxation it recovers the Kapila five-equation model while keeping a monotone frozen sound speed; the page gives its forms, relaxation solvers, phase-change and surface-tension extensions."
status: established
aliases: [6-equation model, six-equation model, pressure-disequilibrium model, Saurel–Petitpas–Berry model, Pelanti–Shyue model, pressure-relaxation model]
tags: [multiphase, interface-capturing, finite-volume]
timestamp: 2026-10-24T05:59:00Z
---

# Six-equation two-phase model

The **six-equation model** describes two compressible phases $k=1,2$ with one
velocity $v$ but two pressures $p_k$: each phase carries its volume fraction
$\phi_k$ ($\phi_1+\phi_2=1$), density $\rho_k$ and energy, and a stiff
relaxation source drives $p_1-p_2$ to zero. It is the pressure-disequilibrium
parent of the [five-equation model](/definitions/five-equation-model.md), which
it recovers when the relaxation is instantaneous, and is used in the bundle in
the form of Saurel, Petitpas & Berry in [MFC](/software/mfc.md)
([Bryngelson et al. (2021)](/sources/bryngelson-2021.md);
[Wilfong et al. (2026)](/sources/wilfong-2026.md)) and in the total-energy form
of Pelanti & Shyue, with heat and mass transfer, by
[Wakimura et al. (2024)](/sources/wakimura-2024.md). Each phase is closed by the
[stiffened-gas equation of state](/definitions/stiffened-gas-equation-of-state.md)
$p_k=(\gamma_k-1)\rho_ke_k-\gamma_kp_{\infty,k}$, with $\gamma_k$ and $c_k$ the ratio
of specific heats and sound speed of phase $k$, $c_k^2=\gamma_k(p_k+p_{\infty,k})/\rho_k$
(page-local $\gamma_k$, $e_k$, $c_k$; $\phi_k$, $\rho_k$, $Y_k=\phi_k\rho_k/\rho$ and
$p_{\infty,k}$ registry §10).

## Internal-energy form (Saurel, Petitpas & Berry)

As written by Wilfong et al. (§2.1.2, after Saurel et al.; Bryngelson et al.
§3.2, Eqs. (11)–(13)), without viscosity and in the registry's symbols,

$$
\begin{aligned}
&\partial_t(\phi_k\rho_k)+\nabla\cdot(\phi_k\rho_kv)=0,\qquad
\partial_t(\rho v)+\nabla\cdot(\rho v\otimes v+pI)=0,\\
&\partial_t(\phi_k\rho_ke_k)+\nabla\cdot(\phi_k\rho_ke_kv)+\phi_kp_k\nabla\cdot v=-\mu_{\mathrm p}\,p_{\mathrm I}\,(p_k-p_{k'})\quad(k'\neq k),\\
&\partial_t\phi_1+v\cdot\nabla\phi_1=\mu_{\mathrm p}(p_1-p_2),
\end{aligned}
$$

with mixture density $\rho=\sum_k\phi_k\rho_k$, mixture pressure
$p=\sum_k\phi_kp_k$ *(compiler check, not in the sources: the momentum pressure
of the internal-energy form is not printed by Wilfong et al.; Wakimura et al.'s
momentum flux carries $\phi_1p_1+\phi_2p_2$)*, the pressure-relaxation parameter
$\mu_{\mathrm p}\ge0$ (page-local; the sources' $\mu$) and the interfacial pressure
weighted by the acoustic impedances $z_k=\rho_kc_k$ (page-local),
$$p_{\mathrm I}=\frac{z_2p_1+z_1p_2}{z_1+z_2}$$
(Wilfong et al., Eqs. (7)–(8)). The total energy is not one of the unknowns;
MFC re-initializes the phasic energies from it so that total energy is
conserved (Bryngelson et al., §3.2). The volume-fraction equation and the
$\phi_kp_k\nabla\cdot v$ terms are non-conservative.

**Sound speed.** The model's frozen sound speed is
$$c^2=\sum_kY_kc_k^2$$
(Bryngelson et al., Eq. (14)), monotone in the volume fraction, unlike Wood's
speed of the five-equation model; Wakimura et al. choose the model for this
reason, because, citing earlier works, a non-monotone mixture sound speed can
make the transport of the mixture zone unstable (§1, §2.3).

## Total-energy form with heat and mass transfer (Pelanti & Shyue)

Wakimura et al. (§2, Eqs. (1)–(16)) use phasic total energies
$E_k=\rho_ke_k+\tfrac12\rho_k\lvert v\rvert^2$ (page-local) in place of internal
energies, with momentum flux $\rho v\otimes v+(\phi_1p_1+\phi_2p_2)I$, a
non-conservative exchange term
$\Sigma=-v\cdot\big(Y_2\nabla(\phi_1p_1)-Y_1\nabla(\phi_2p_2)\big)$ between the two
energy equations, and three relaxation sources: mechanical,
$\mu_{\mathrm p}(p_1-p_2)$; thermal, proportional to $T_2-T_1$; chemical, proportional
to the difference of the phasic Gibbs energies, which carries mass transfer.
The full system, with the interface quantities that need not be specified for
infinite rates, is on the
[five-equation model](/definitions/five-equation-model.md) page (section *The
six-equation model*).

## Infinite relaxation and its solvers

With $\mu_{\mathrm p}\to\infty$ the two pressures equalize instantaneously, and
the model "can represent the same physical processes" as Kapila's five-equation model while
avoiding "numerical instability issues that arise from some interface capture
schemes" (Wilfong et al., §2.1.2, following Schmidmayer et al., as recalled);
Wilfong et al. state the instability of Kapila's model as coming from its
non-conservative $K\nabla\cdot v$ term (§2.1.1). In practice the relaxation is
a fractional step after the hyperbolic update
([operator splitting](/methods/operator-splitting.md)):

- **MFC** (Bryngelson et al., §3.2, §4.6) applies infinite relaxation at every
  Runge–Kutta stage, after a first-order explicit step of the non-relaxed
  system and the energy re-initialization; the pressure is then unique at the
  end of the stage and the effective mixture sound speed is Wood's. The
  six-equation model costs about 5% more than the five-equation model on a
  spherical bubble collapse (quoting an earlier MFC paper).
- **Closed-form mechanical relaxation** (Wakimura et al., App. B, Eqs.
  (B.4)–(B.7)). With $p_{\mathrm I}=p^*$ the relaxed pressure is the root of
  $a(p^*)^2+bp^*+d=0$, with
  $a=\gamma_1\phi_2^0+\gamma_2\phi_1^0$,
  $b=-\gamma_1\phi_2^0(p_2^0-p_{\infty,1})-\gamma_2\phi_1^0(p_1^0-p_{\infty,2})$,
  $d=-\gamma_1\phi_2^0p_2^0p_{\infty,1}-\gamma_2\phi_1^0p_1^0p_{\infty,2}$, and
  $\phi_k^*=\phi_k^0\,\frac{(\gamma_k-1)p^*+p_k^0+\gamma_kp_{\infty,k}}{(\gamma_k-1)p^*+p^*+\gamma_kp_{\infty,k}}$
  (superscript $0$: before relaxation). The roots are taken in a
  cancellation-free form, which still loses digits near a double root
  (App. E).
- **Thermal and chemical relaxation** (Wakimura et al., Apps. C–D; Wilfong et
  al., §4.1.3). Wakimura et al. reduce thermal relaxation to a quadratic in
  the common pressure and chemical relaxation to a Newton–Raphson solve of the
  saturation condition, in four orderings p, p–pT, p–pTg, p–pT–pTg (Eq. (45)),
  applied only where $10^{-4}\le\phi_1\le1-10^{-4}$ and, for phase change, only
  for evaporation (§2.4). MFC 5.0 adds $N$-fluid pT and pTg relaxation solved
  by Newton's method, for both the five- and the six-equation model (Wilfong
  et al., §4.1.3, after Saurel et al., Chiapolino et al. and Le Métayer et
  al., as recalled).

## Surface tension

MFC 5.0 adds two-material surface tension to the six-equation model after
Schmidmayer et al. (Wilfong et al., §4.1.8): an advected colour function $\mathsf c$
(page-local, not the sound speed $c$), $\partial_t\mathsf c+v\cdot\nabla\mathsf c=0$, defines the capillary stress
$-\sigma_{\mathrm{st}}\big(\lVert\nabla\mathsf c\rVert I-\nabla\mathsf c\otimes\nabla\mathsf c/\lVert\nabla\mathsf c\rVert\big)$
($\sigma_{\mathrm{st}}$ registry §10), which enters momentum and the total energy
with a capillary energy. The authors state that the model is conservative
except for the pressure-relaxation terms and obeys the second law, and resolve
the Laplace pressure jump of a static water column on $128\times128$ cells
([oscillating droplet](/benchmarks/oscillating-droplet.md)).

## Discretizations in the sources

- **MFC**: finite-volume WENO (fifth order with mapped weights; WENO-Z and
  TENO at orders 3, 5, 7 in version 5.0) with HLL or HLLC fluxes and SSP
  Runge–Kutta, the same reconstruction for the five- and six-equation models
  (Bryngelson et al., §3.2; Wilfong et al., §3, §4.2.2).
- **Wakimura et al.**: HLLC in wave-propagation form, SSP-RK3 and a
  [BVD](/definitions/boundary-variation-diminishing.md) selection between
  MUSCL and [THINC](/methods/thinc-reconstruction.md) applied to the volume
  fraction and partial densities only (§3), tested on cavitation tubes, a
  mainly-vapour shock tube and 2D vapour-bubble problems
  ([gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md),
  [double rarefaction](/benchmarks/double-rarefaction-problem.md),
  [Richtmyer–Meshkov instability](/benchmarks/richtmyer-meshkov-instability.md)).
- **Evidence for phase change**: MFC's five- and six-equation models with pTg
  relaxation reproduce Simões-Moreira & Shepherd's evaporation-front speeds of
  n-dodecane between 180 and 300 °C, better at the higher temperatures
  (Wilfong et al., §4.1.3, Fig. 3).

## Qualifications

- Wilfong et al. print the phase-2 energy flux as $\nabla\cdot(\phi_1\rho_2e_2v)$,
  where symmetry with phase 1 requires $\phi_2\rho_2e_2v$; the work terms as
  "$\phi_kp_k\cdot\nabla v$", a scalar dotted with a tensor, meaning
  $\phi_kp_k\nabla\cdot v$; the interfacial pressure as $P_{\mathrm I}$ in Eq. (7) and
  $p_{\mathrm I}$ in the equations; and the phasic sound speed in Eq. (8) without the
  phase index on $\gamma$ (§2.1.2, §4.1.8). The form above uses the consistent
  reading.
- Wilfong et al. print the relaxation sources as $-\mu_{\mathrm p}p_{\mathrm I}(p_2-p_1)$ for
  phase 1 and $-\mu_{\mathrm p}p_{\mathrm I}(p_1-p_2)$ for phase 2. They cancel in the sum, but
  with $\partial_t\phi_1=\mu_{\mathrm p}(p_1-p_2)+\dots$ the work done by phase 1 when it
  expands is $p_{\mathrm I}\,\partial_t\phi_1$, which requires $-\mu_{\mathrm p}p_{\mathrm I}(p_1-p_2)$
  in the phase-1 equation, as in the form above and in Wakimura et al.'s
  $-\mu_{\mathrm p}p_{\mathrm I}(p_1-p_2)$ for $\phi_1E_1$ (their Eqs. (1)–(16)); the printed
  signs are both reversed *(compiler check, not in the sources)*.
- Wakimura et al. state that restricting thermal and chemical relaxation to
  mixed cells and to evaporation does not affect the solution, without showing
  it (§2.4); the order of their splitting is not stated or measured.
- The instability attributed to Kapila's model and avoided by the six-equation
  model is cited, not demonstrated, in Wilfong et al.

# Citations

- [Wilfong et al. (2026)](/sources/wilfong-2026.md) — §2.1.1–2.1.2, Eqs. (5)–(8); §2.2; §3; §4.1.3, Fig. 3; §4.1.8, Fig. 9; §4.2.2.
- [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) — §3.2, Eqs. (11)–(14); §4.6.
- [Wakimura et al. (2024)](/sources/wakimura-2024.md) — §1; §2, Eqs. (1)–(16); §2.3–2.4; §3; Eq. (45); Apps. B–E.
