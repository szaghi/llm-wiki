---
type: Source
title: "Fowler et al. (2022) — A Lagrangian relaxation towards equilibrium wall model for large eddy simulation"
description: "Derives LaRTE, a wall-stress model in which the friction-velocity vector obeys a Lagrangian transport equation on the wall relaxing towards equilibrium with the inertial time scale of the wall-modelled layer, and adds a Stokes-layer model for fast pressure-gradient fluctuations, tested in channel and sudden-spanwise-pressure-gradient flows."
resource: "doi:10.1017/jfm.2021.1156"
source_kind: paper
authors: [Fowler M., Zaki T.A., Meneveau C.]
year: 2022
venue: "J. Fluid Mech. 934:A44"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Journal_of_Fluid_Mechanics_Fowler_A_Lagrangian_relaxation_towards_equilibrium_wall_model_for_l.pdf"
tags: [wall-model, wmles, les, boundary-layer]
timestamp: 2026-10-25T13:44:00Z
---

# Summary

Fowler et al. (2022) derive a wall-stress model for
[wall-modelled LES](/methods/wall-modelled-les.md) from a formal reading of
"quasi-equilibrium". Following Chung & Pullin (2009) and the integral wall
model of Yang et al. (2015), they integrate the wall-parallel thin-boundary-layer
RANS momentum equation from the wall to the matching height $h_{\mathrm{wm}}$.
The ansatz is a [law-of-the-wall](/definitions/law-of-the-wall.md) profile
scaled by a slowly varying friction-velocity vector, $\boldsymbol u_\tau(x,z,t)f(y^+)$.
The time derivative yields $\partial_t\boldsymbol u_\tau$. With continuity,
the advective terms reduce to an advection of $\boldsymbol u_\tau$ by a
velocity built from a "cell displacement thickness" and a "cell momentum
thickness". The result is the
[Lagrangian relaxation towards equilibrium](/methods/lagrangian-relaxation-towards-equilibrium-wall-model.md)
(LaRTE) equation, a transport equation on the wall. Along wall trajectories,
$\boldsymbol u_\tau$ relaxes towards the total forcing of the near-wall layer
(stress at $h_{\mathrm{wm}}$ plus pressure-gradient force) divided by
$u_\tau$. The relaxation time $T_s=f(h^+_{\mathrm{wm}})h_{\mathrm{wm}}/u_\tau$
expresses the inertia of the fluid below $h_{\mathrm{wm}}$. The classical
[equilibrium wall model](/methods/equilibrium-wall-model.md) is the limit
$T_s\to0$. The stress at $h_{\mathrm{wm}}$ is closed with Meneveau's (2020)
fitted equilibrium solution with pressure gradient. An a priori test on
channel DNS at $Re_\tau=1000$ shows that exponential time filtering at $T_s$
collapses the near-wall profiles onto the law of the wall.

A second component adds the laminar Stokes-layer response of the viscous
sublayer to fast pressure-gradient fluctuations. Its wall stress is a
convolution with kernel $(t-t')^{-1/2}$ (a Caputo half-derivative), evaluated
with a sum of exponentials. The LES pressure gradient is split by exponential
time filters into equilibrium, band-pass and high-pass parts.

Tests in [LESGO](/software/lesgo.md) use a Lagrangian scale-dependent
[dynamic](/methods/dynamic-procedure.md) SGS model and a "2Δ spatial
filter" after Bou-Zeid et al. (2005) on the LES velocity (the paper's $\Delta$
is the matching height), which the paper uses against
[log-layer mismatch](/definitions/log-layer-mismatch.md). In the stationary
[channel](/benchmarks/turbulent-channel-flow.md) at $Re_\tau=10^3$ to
$5\times10^5$ the statistics are nearly identical to those of the equilibrium
model, and the wall-stress PDFs are narrower than in filtered DNS. In the
sudden-spanwise-pressure-gradient channel of Lozano-Durán et al. (2020), the
composite model reproduces the early $\sqrt t$ growth of the spanwise wall
stress, which the equilibrium model misses.

# Version read

Version of record (J. Fluid Mech. 934:A44, open access CC-BY 4.0; received 5
July 2021, accepted 20 December 2021), 37 pages (A44-1 to A44-37). The
metadata above are those of this published version; the page matches the
metadata card. The supplementary material at the DOI (the sum-of-exponentials
weights and exponents) was not read.

# Key claims

1. Substituting $\boldsymbol u_\tau(x,z,t)f(y^+)$ for the wall-parallel velocity in the wall-parallel RANS momentum equation and integrating over $0\le y\le h_{\mathrm{wm}}$ gives a vector transport equation (Eq. 2.14) for $\boldsymbol u_\tau$ with relaxation time $T_s=f(h^+_{\mathrm{wm}})h_{\mathrm{wm}}/u_\tau$ (Eq. 2.15), and "does not require additional ad hoc assumptions" (§2, Eqs. 2.6–2.16, App. A). **Derived**
2. The horizontal advective terms make the time derivative Lagrangian, with advection velocity $\boldsymbol V_\tau=(1-\delta^*_h/h_{\mathrm{wm}}-\theta_h/h_{\mathrm{wm}})f(h^+_{\mathrm{wm}})\boldsymbol u_\tau$ (Eq. 2.12), where $\delta^*_h$ and $\theta_h$ are displacement and momentum thicknesses integrated up to $h_{\mathrm{wm}}$. The vertical-advection contribution cancels exactly against part of the horizontal one (App. A, Eqs. A5–A6). **Derived**
3. For one component of the wall stress without pressure gradient, the relaxation time is $T_s/2$ (Eq. 2.18). Chung & Pullin (2009) derived this time scale originally: their $1/(\Lambda\tilde\eta_0)$ equals $T_s/2$ (§2.1). **Derived** (equivalence **Stated**)
4. The classical equilibrium wall model is the limit $T_s\to0$ of LaRTE (wall stress equal to the total stress at $h_{\mathrm{wm}}$), justified only under full time-scale separation (§2.2). **Derived**
5. The explicit time filter of Yang et al. (2015), $\sim h_{\mathrm{wm}}/(\kappa u_\tau)$, is shorter than $T_s$ by the factor $\kappa f(h^+_{\mathrm{wm}})$ (§2.1). The suggested minimum multiplier of 5 gives "a coincidentally rather similar time scale as $T_s$ for $\Delta^+=34$" (§2.3). **Stated**. With Eq. C1, $T_s=13.63\,h_{\mathrm{wm}}/u_\tau$ at $h^+_{\mathrm{wm}}=34$, against $5h_{\mathrm{wm}}/(0.4u_\tau)=12.5\,h_{\mathrm{wm}}/u_\tau$ *(compiler check, not in the sources)*.
6. A priori, on channel DNS at $Re_\tau=1000$ from the Johns Hopkins database (horizontal Gaussian filter of width 196 wall units, $0\le y^+\le34$, $0\le tu_\tau/\delta\le0.3245$), exponential time filtering at $T_s$ "almost completely collapses" the profiles onto the law of the wall when they are scaled with the local friction velocity. No filter, or a filter at $h_{\mathrm{wm}}/u_\tau$, does not (§2.3, Fig. 2). **Shown**
7. The non-equilibrium laminar wall stress driven by fast pressure-gradient fluctuations is $\boldsymbol\tau''_w(t)=\sqrt{\nu/\pi}\int_{t_0}^t\left(-\rho^{-1}\nabla_hp''\right)(t')(t-t')^{-1/2}\,dt'$ (Eq. 3.5), with $p''$ the high-pass part of the LES pressure; it is the solution of a generalised Stokes problem (Eqs. 3.1–3.4). **Derived**
8. This stress is a Caputo fractional derivative of order 1/2 of the non-equilibrium free-stream velocity (Eq. 3.6). **Derived** (sign slip, see Printed slips)
9. The laminar non-equilibrium stress scales as $\nu^{1/2}$ and "vanishes in the limit of infinite Reynolds number", unlike turbulent wall-layer fluctuations (§5.1, discussion of Fig. 10). **Derived**/**Shown** (PDF narrowing from $Re_\tau=1000$ to 5200)
10. The LES pressure gradient is split into an equilibrium part (time filter at $3T_s$; "results appear to be quite insensitive to this choice"), a high-pass part (above the frequency $1/t_\nu$, $t_\nu=(l_s^+)^2\nu/u_\tau^2$, $l_s^+\approx12$) driving the Stokes-layer model, and a band-pass part (between $t_\nu$ and $3T_s$) entering LaRTE (§4.1, Eqs. 4.1–4.5). **Stated** (insensitivity not shown)
11. Discretisation: forward Euler with a semi-Lagrangian step (first-order bilinear interpolation at the upstream point) (Eqs. 4.6–4.7). The numerical diffusion of the low-order interpolation stands in for the horizontal diffusion term, which is neglected (§4.2). **Stated**
12. Sum-of-exponentials evaluation of the $(t-t')^{-1/2}$ convolution: with time step $4\times10^{-4}$, tolerance $10^{-9}$ and horizon 1, the optimisation of Jiang et al. (2017) yields 48 exponentials. Storage is $O(N_{\exp})$ and work $O(N_TN_{\exp})$, against $O(N_T)$ storage and $O(N_T^2)$ work for direct evaluation (§4.3). **Stated**
13. Sum-of-exponentials against the L1 method on a representative pressure-gradient signal ($Re_\tau=1000$, $h_{\mathrm{wm}}=\delta/30$): normalised differences below 0.021 ($x$) and 0.011 ($z$) (App. D, Fig. 18). **Shown**
14. Stationary channel ($Re_\tau=1000$, 5200, $2\times10^4$, $10^5$ and $5\times10^5$ on the same $128\times30\times48$ grid): the mean velocity follows the law of the wall, with a slight log-layer undershoot at $Re_\tau=1000$ and a wake overshoot. The equilibrium-model results are "nearly indistinguishable" from LaRTE with the laminar model (§5.1, Figs. 4–5). **Shown**
15. The differences between WMLES and DNS one-point statistics (overpredicted $\langle w'w'\rangle$, underpredicted $\langle u'u'\rangle$ near the wall) are attributed to the grid and the SGS model, not to the wall model, because two different wall models agree (§5.1). **Shown**/**Stated**
16. In LES at $Re_\tau=1000$ with $h_{\mathrm{wm}}/\delta=1/30$, the mean $T_su_\tau/\delta\approx0.45$, and LaRTE filters out almost all $u_\tau$ fluctuations faster than $T_s$ (§5.1, Fig. 6). **Shown**. Eq. C1 gives $f(33.3)=13.56$ and $T_su_\tau/\delta=0.452$ *(compiler check, not in the sources)*.
17. In the LaRTE equation, the Eulerian time derivative and the advective term are anticorrelated. The term in $\partial_t\boldsymbol s$ (the rate of change of the stress direction) is negligible in $x$ but contributes in $z$ (§5.1, Fig. 7). **Shown**
18. An Eulerian version of the relaxation equation "pins" fluctuations at the wall and elongates structures excessively in the streamwise direction. The Lagrangian version "appears more physically reasonable", with the caveat that no "true" reference distribution exists (§5.1, Fig. 9). **Shown** (qualitative)
19. Against Gaussian-filtered DNS, the LaRTE wall-stress PDFs peak at the right values but are significantly narrower. The laminar part adds fluctuations, but streamwise fluctuations remain underpredicted. The spanwise PDF is slightly overestimated at $Re_\tau=1000$ and predicted "very well" at 5200 (§5.1, Fig. 10). **Shown**
20. A one-sided exponential filter with a fluctuating short time scale ($t_\nu$) does not preserve the mean, so the non-equilibrium stress PDF has a non-zero mean (§5.1). **Shown**
21. Sudden spanwise pressure gradient ($Re_{\tau0}=1000$, $\partial_zp_\infty=10\,\partial_xp_\infty=10\rho u_{\tau0}^2/\delta$): for $0\le tu_{\tau0}/\delta\le0.05$ the spanwise wall stress follows the laminar Stokes first-problem solution, dominated by the non-equilibrium component; afterwards LaRTE dominates (§5.2, Fig. 12). **Shown**
22. The LaRTE part responds faster than $T_su_{\tau0}/\delta\approx0.45$ because of the band-pass pressure gradient. Without it the spanwise stress is delayed by $O(T_s)$; without the high-pass part it grows nearly linearly and misses the $\sqrt t$ trend (§5.2). **Shown** (runs described, not plotted)
23. The new model agrees with the DNS better than the equilibrium model, which responds linearly. The equilibrium model here is closer to the DNS than that of Lozano-Durán et al. (2020) because of a smaller matching height, which the authors "have verified" (§5.2). **Shown**/**Stated**
24. The model misses the slight initial decrease of the streamwise wall stress after the spanwise gradient is switched on (a three-dimensional scrambling mechanism), an error "less than 1 %–2 % of $u_{\tau0}$". The streamwise stress follows the DNS trend for $tu_{\tau0}/\delta>1$ and returns to unity at long times (§5.2, Fig. 13). **Shown**
25. Mean spanwise velocity profiles after the pressure-gradient change agree with the DNS for both wall models (§5.2, Fig. 14). **Shown**
26. The fit C1 for $f(y^+)$ has an error below 1% for $y^+>5$ and below 2.25% for $0\le y^+\le5$; Reichardt's profile errs by over 3% near $y^+\sim10$. The fits C3 and C5 for the cell thicknesses have a maximum error of 0.5% over $10^{-1}\le h^+_{\mathrm{wm}}\le10^5$. The cell shape factor tends to 3 (linear profile) at small $h^+_{\mathrm{wm}}$ (App. C, Fig. 17). **Shown**
27. The response of near-wall turbulence above the viscous sublayer at time scales between $t_\nu$ and $T_s$ (turbulence scrambling, drag reduction by spanwise oscillation) is not modelled and remains open (§4.1, §6). **Stated**

# Printed slips

- **Argument of $\boldsymbol u_\tau$ (§4.2, p. A44-15).** "The full model embodied by (2.14) is a nonlinear PDE for $\boldsymbol u_\tau(x,y,t)$"; Eq. 2.1 and the rest of the paper write $\boldsymbol u_\tau(x,z,t)$.
- **Gradient symbol (§2.1, p. A44-8).** The forcing is written "$(-\rho^{-1}\nabla_s\bar p\Delta+\bar{\boldsymbol\tau}_\Delta)/u_\tau$" with $\nabla_s$, whereas Eq. 2.14 uses $\nabla_h$.
- **Fig. 10 caption.** The caption assigns "dashed black" both to "the filtered DNS" and to "the composite model (LaRTE + non-equilibrium)".
- **Matching height in wall units.** §2.3 gives $\Delta^+\approx34$ for $Re_\tau=1000$; Table 1 gives 33 for the same case.
- **App. D wording.** "root-mean-sum difference"; "(N_exp) terms to be stored" without the $O(\cdot)$.
- **Sign of Eq. 3.6** *(compiler check, not in the sources)*. Eq. 3.6 prints $\boldsymbol\tau''_w=-\sqrt{\nu/\pi}\,\Gamma(1/2)D_t^{1/2}(\tilde{\boldsymbol u}''_\infty)$. By Eq. 3.7 at order 1/2, $\Gamma(1/2)D_t^{1/2}v=\int_{t_0}^tv'(t')(t-t')^{-1/2}dt'$, and Eq. 3.2 gives $\partial_t\tilde{\boldsymbol u}''_\infty=-\rho^{-1}\nabla_h\tilde p''$. So $\sqrt{\nu/\pi}\,\Gamma(1/2)D_t^{1/2}(\tilde{\boldsymbol u}''_\infty)$ equals $+\boldsymbol\tau''_w$ of Eq. 3.5. Eq. 3.5 itself follows from Eq. 3.4, since $\nu\,\partial_y\mathrm{erf}(y/(2\sqrt{\nu s}))|_{y=0}=\sqrt{\nu/\pi}\,s^{-1/2}$. The leading minus sign of Eq. 3.6 is inconsistent with Eqs. 3.2, 3.5 and 3.7.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Delta$, $\Delta^+$ | $h_{\mathrm{wm}}$, $h^+_{\mathrm{wm}}$ | **collision:** the source's $\Delta$ is the matching height ($\Delta_y/2$, the first LES point), not the filter width |
| $\Delta_x,\Delta_y,\Delta_z$ | (LES grid spacings) | |
| overline ($\bar{\boldsymbol u}_s$, $\bar p$, $\bar{\boldsymbol\tau}_w$) | (quasi-equilibrium quantities) | **collision:** horizontal LES-scale filter plus an implicit time average, neither the registry's LES filter alone nor a Reynolds average |
| tilde ($\tilde{\boldsymbol u}$, $\tilde p=p_{LES}$) | (LES fields, not time-filtered) | **collision:** not a Favre filter (incompressible) |
| $(\cdot)'$, $(\cdot)''$ | (band-pass part), $(\cdot)''$ (high-pass part, page-local on the concept pages) | **collision:** $\tilde p=P+\bar p'+\tilde p''$, $\bar p=P+\bar p'$ (Eq. 4.1); not Reynolds or Favre fluctuations |
| $\langle\cdot\rangle_T$ | (one-sided exponential time filter at scale $T$) | $\langle\cdot\rangle$ without subscript is a plane or ensemble average, as in the registry |
| $\boldsymbol u_\tau$, $u_\tau$ | (friction-velocity vector), $u_\tau$ | prognostic variable of LaRTE |
| $\bar{\boldsymbol\tau}_w=u_\tau\boldsymbol u_\tau$ | $\tau_w/\rho$ (vector) | kinematic wall stress |
| $\bar{\boldsymbol\tau}_\Delta$ | $\boldsymbol\tau_h$ (page-local) | total (viscous plus turbulent) kinematic stress at the matching height |
| $f(y^+)$ | $u^+=f(y^+)$ | law-of-the-wall function, fit C1 |
| $\kappa=0.4$, $B=4.95$ | $\kappa$, $B$ | Fig. 4 log law uses $B=5.0$ |
| $\delta^*_\Delta$, $\theta_\Delta$, $H_\Delta$ | $\delta^*_h$, $\theta_h$ (page-local), (cell shape factor) | thicknesses integrated up to $h_{\mathrm{wm}}$ |
| $\nabla_h$ | $\nabla_h$ (page-local wall-parallel gradient) | the subscript is not the registry's element size $h$ |
| $h$ | $\delta$ | channel half-height |
| $\boldsymbol U_{LES}$, $\hat{\boldsymbol e}_u$ | $U_{\mathrm{LES}}$, (its direction) | LES velocity at $h_{\mathrm{wm}}$, spatially filtered ("2Δ spatial filter") |
| $Re_\Delta=U_{LES}\Delta/\nu$ | (matching-height Reynolds number) | |
| $\nu_T$ | $\nu_t$ | RANS eddy viscosity |
| $T_s$, $t_\nu$, $l_s^+$ | (relaxation time, Stokes-layer diffusion time, its length in wall units) | |
| $\theta$ (Yang et al. multiplier) | (time-filter multiplier) | not $\theta_{\mathrm{wm}}$ |
| $\omega_m$, $s_m$, $N_{\exp}$ | (sum-of-exponentials weights, exponents, count) | **collision:** $\omega_m$ is neither a vorticity nor the specific dissipation |
| $Re_\tau$ | $Re_\tau$ | based on the half-height |

# Reference list

64 printed references, author–year style (JFM), alphabetical. The list is
merged complete into the [bibliography](/bibliography.md) with `citedby` this
slug. The two JHTDB and LESGO web pages are entered as web items; Graham et
al. (2016) prints "et al." and is recorded with "others"; the reference list
prints no DOIs. Same-year items are disambiguated in printed order (He 2011a,
b; Sundstrom 2018a, b, c). No printed duplicates or unparseable items.

# Pages created or updated

Chunk 1 (2026-10-25). This source is cited on:

- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Log-layer mismatch](/definitions/log-layer-mismatch.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Equilibrium wall model](/methods/equilibrium-wall-model.md)
- [Lagrangian relaxation towards equilibrium (LaRTE) wall model](/methods/lagrangian-relaxation-towards-equilibrium-wall-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [LESGO](/software/lesgo.md)
