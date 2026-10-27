---
type: Method
title: "Differential Reynolds-stress models"
description: "Second-moment RANS closures that transport the six Reynolds stresses instead of postulating an eddy viscosity: the SSG/LRR-ω model with its F1 blending and constants, its coupling to an intermittency transition model, the ATAAC model, and evidence on turbine and compressor cascades, delta wings, wake vortices and buffet."
status: established
aliases: [Reynolds-stress model, RSM, DRSM, differential Reynolds-stress model, second-moment closure, Reynolds stress transport model, RSTM, SSG/LRR-ω, SSG/LRR-ω-γ, ATAAC DRSM]
tags: [rans, reynolds-stress-model, transition, turbomachinery, separated-flow]
timestamp: 2026-10-26T20:48:00Z
---

# Differential Reynolds-stress models

A differential Reynolds-stress model (RSM, DRSM) closes the RANS equations
at the second-moment level: it solves a transport equation for each of the
six components of $R_{ij}=\langle u_i'u_j'\rangle$ plus one equation for a
length-determining variable, so it needs no
[Boussinesq](/definitions/boussinesq-hypothesis.md) relation between
$R_{ij}$ and the mean strain. Production and rotation terms of the stress
equations are exact; the pressure–strain correlation, the dissipation
tensor and the turbulent diffusion are modelled. In this bundle the model
that appears in detail is SSG/LRR-$\omega$ of Eisfeld et al., used in
turbine and compressor cascades and on a delta wing (Morsbach et al. 2024;
Liu et al. 2024; Mozaffari et al. 2022); a second model, the ATAAC DRSM,
is the precursor RANS of an aircraft-wake study (Bouhafid et al. 2024).

## Motivation and lineage

Liu et al. (2024) give the motivation and the lineage
([Liu et al. (2024)](/sources/liu-2024.md), Introduction):

- linear eddy-viscosity models (Spalart–Allmaras, SST) need added
  rotation–curvature, quadratic-constitutive or non-equilibrium corrections
  to predict anisotropy and non-equilibrium in compressor corner flows,
  while an RSM represents the Reynolds-stress production and Coriolis
  terms exactly and is "more sensitive" to anisotropy;
- the $\varepsilon$-based models (LRR, SSG, the elliptic-blending EB-RSM)
  suffer near-wall numerical stiffness, and LRR needs a wall-reflection
  term in the pressure–strain that further reduces robustness;
- Wilcox showed that the reflection term can be avoided by transporting
  $\omega$ instead of $\varepsilon$, and Eisfeld et al. blended a
  stress-$\omega$ model near the wall with SSG away from it through
  Menter's $F_1$, obtaining the robust SSG/LRR-$\omega$ model.

Bouhafid et al. (2024) justify a DRSM for wing-tip vortices by recalling
that the Reynolds stress and the mean strain are misaligned there because
of rotation, which makes DRSMs "more accurate than two-equations models"
for such flows; the statement is cited, not shown
([Bouhafid et al. (2024)](/sources/bouhafid-2024.md), §2.2). Agrawal &
Koutsourelakis (2024) state the opposite side of the trade-off:
non-linear eddy-viscosity models, Reynolds-stress transport models and
algebraic stress models "have not received widespread attention because
they lack the robustness of LEVM and involve more parameters that need to
be calibrated" ([Agrawal & Koutsourelakis (2024)](/sources/agrawal-2024.md),
§2.1.2; arXiv v2).

## The SSG/LRR-$\omega$ model

Liu et al. (2024) print the model as implemented in OpenFOAM (Eqs. 1–9,
Table 1). Divided by the density and written per unit mass, in registry
notation (mean velocity $\langle u_i\rangle$, Favre and Reynolds averages
not distinguished by the source) *(compiler check, not in the sources)*:

$$\partial_tR_{ij}+\langle u_k\rangle\partial_kR_{ij}=\mathcal P_{ij}+\phi_{ij}-\varepsilon_{ij}+\mathcal D_{ij},\qquad
\mathcal P_{ij}=-R_{ik}\partial_k\langle u_j\rangle-R_{jk}\partial_k\langle u_i\rangle,$$

with $\mathcal P_{ij}$, $\phi_{ij}$, $\varepsilon_{ij}$, $\mathcal D_{ij}$ the
page-local production, pressure–strain, dissipation and diffusion tensors
(the source's $P_{ij}$, $\Pi_{ij}$, $\varepsilon_{ij}$, $D_{ij}$; renamed
because the registry gives $\Pi$ to the SGS energy flux and $D_{ij}$ to the
differentiation matrix). $k=\tfrac12R_{kk}$ and the anisotropy is the
registry's $b_{ij}=R_{ij}/(2k)-\tfrac13\delta_{ij}$ (Eq. 5).

**Length-scale equation.** With $\nu_t=k/\omega$ (the source's $\upsilon_t$)
and $\tfrac12\mathcal P_{kk}$ the production of $k$,

$$\partial_t\omega+\langle u_k\rangle\partial_k\omega=\frac{\gamma_\omega}{\nu_t}\tfrac12\mathcal P_{kk}+\partial_j\big[(\nu+\sigma_\omega\nu_t)\partial_j\omega\big]-\beta_\omega\omega^2+\frac{\sigma_d}{\omega}\max\big(\partial_jk\,\partial_j\omega,0\big)$$

(Eq. 2); the production and destruction coefficients $\gamma_\omega$,
$\beta_\omega$ (registry §11) and $\sigma_\omega$, $\sigma_d$ (page-local)
are not printed.

**Closures.** The dissipation is isotropic,
$\varepsilon_{ij}=\tfrac23\varepsilon\delta_{ij}$ with $\varepsilon=C_\mu k\omega$
and $C_\mu=0.09$ (Eq. 7). The diffusion is the generalized gradient
diffusion of Daly & Harlow,

$$\mathcal D_{ij}=\partial_k\Big[\Big(\nu\delta_{kl}+\frac{D_{GD}}{C_\mu\omega}R_{kl}\Big)\partial_lR_{ij}\Big]$$

(Eq. 8). The pressure–strain model is the SSG form

$$\begin{aligned}
\phi_{ij}={}&-\big(c_1\varepsilon+\tfrac12c_1^*\mathcal P_{kk}\big)b_{ij}+c_2\varepsilon\big(b_{ik}b_{kj}-\tfrac13b_{kl}b_{kl}\delta_{ij}\big)+k\big(c_3-c_3^*\sqrt{b_{kl}b_{kl}}\big)S^d_{ij}\\
&+c_4k\big(b_{ik}S_{jk}+b_{jk}S_{ik}-\tfrac23b_{kl}S_{kl}\delta_{ij}\big)+c_5k\big(b_{ik}\Omega_{jk}+b_{jk}\Omega_{ik}\big)
\end{aligned}$$

(Eq. 4; $S_{ij}$, $S^d_{ij}$, $\Omega_{ij}$ of the mean velocity, the source's
$S_{ij}$, $S^*_{ij}$, $W_{ij}$). Every coefficient $\phi$ is blended as
$\phi=F_1\phi^{(\mathrm{LRR})}+(1-F_1)\phi^{(\mathrm{SSG})}$ with the
[SST](/methods/k-omega-sst-model.md) function $F_1$: LRR values in the inner
and SSG values in the outer boundary layer (Eq. 9). Table 1 as printed,
with the caption "$c_2^{(\mathrm{LRR})}=0.52$":

| | $c_1$ | $c_1^*$ | $c_2$ | $c_3$ | $c_3^*$ | $c_4$ | $c_5$ | $D_{GD}$ |
|---|---|---|---|---|---|---|---|---|
| LRR | 3.6 | 0 | 0 | 0.8 | 1.3 | 1.25 | 0.4 | $0.75C_\mu$ |
| SSG | 3.4 | 1.8 | 4.2 | 0.8 | 0 | $(18c_2^{(\mathrm{LRR})}+12)/11$ | $(-14c_2^{(\mathrm{LRR})}+20)/11$ | 0.22 |

The $c_i$ are page-local; see Qualifications on the row assignment.

Morsbach et al. (2024) use the same model in DLR's TRACE code, a
high-Reynolds-number form with the LRR pressure–strain near walls and no
explicit near-wall pressure–strain or dissipation terms
([Morsbach et al. (2024)](/sources/morsbach-2024.md), §2, §4.2).

## Coupling to a transition model

Liu et al. (2024) couple SSG/LRR-$\omega$ to Menter's one-equation
intermittency model (see
[local-correlation-based transition models](/methods/local-correlation-based-transition-model.md))
as SSG/LRR-$\omega$-$\gamma$, with $\gamma$ the intermittency (registry §4)
entering the stress equations directly, since there is no eddy viscosity
to multiply (Eqs. 20–21):

$$\partial_tR_{ij}+\langle u_k\rangle\partial_kR_{ij}=\gamma\mathcal P_{ij}+\gamma\phi_{ij}-\max(\gamma,0.1)\,\varepsilon_{ij}+\mathcal D_{ij},$$

and the production of the $\omega$-equation becomes

$$\frac{\gamma_\omega}{\nu_t}\tfrac12\widetilde{\mathcal P}_{kk}=\gamma_\omega(1-\gamma)\lvert S\rvert\lvert\Omega\rvert+\gamma\frac{\gamma_\omega}{\nu_t}\tfrac12\mathcal P_{kk},$$

a $\gamma$-blend of a Kato–Launder production, which avoids overproduction
at stagnation points, and the original one (the tilde marks the modified
production, page-local; the source prints $S$ and $\Omega=\sqrt{2W_{ij}W_{ij}}$,
the strain modulus' normalization not printed). The coupling form is
credited to Nie et al. (2018), who applied it with the
$\gamma$-$Re_\theta$ model to correct too-short transition lengths caused
by the different near-wall $\omega$ production of SST and SSG/LRR-$\omega$;
Kuya et al. (2022) instead activate the modified production only in
favourable pressure gradients (§ Blending, as recalled by Liu et al.).
On the PVD compressor cascade at 25% span, with the modified production
the model predicts separation-induced transition consistent with oil flow,
whereas with the original production transition moves upstream as bypass
transition (Fig. 1). Liu et al. chose Menter's $\gamma$ model over the
laminar-kinetic-energy $k$-$k_L$-$\omega$ model, whose trigger functions
and coefficients are calibrated on a $k$-$\omega$ closure, as "more
compatible" with SSG/LRR-$\omega$ (Introduction). Morsbach et al. (2024)
couple SSG/LRR-$\omega$ to $\gamma$-$Re_\theta$ in TRACE, the intermittency
modifying production, dissipation and pressure–strain after Nie et al.,
the same kind of coupling (§2).

## Host of hybrid RANS/LES

Wang et al. (2021) build an improved delayed
[detached-eddy simulation](/methods/detached-eddy-simulation.md) on the
Favre-averaged SSG/LRR-$\omega$ model (RSM-IDDES) in the unstructured
finite-volume solver HUNS3D, motivated by "problem" flows "where eddy
viscosity model may fail to predict separation accurately"
([Wang et al. (2021)](/sources/wang-2021-l.md), §1, §2.2–§2.4). They keep
the exact production and replace the isotropic dissipation tensor by
$\varepsilon_{ij}=\tfrac23\big(k^{3/2}/l_{\mathrm{IDDES}}\big)\delta_{ij}$, with
$k=\tfrac12R_{ii}$ and the IDDES length blending the RANS length
$\sqrt k/(C_\mu\omega)$ of the BSL $\omega$-equation with
$C_{\mathrm{DES}}\Delta$ (Eqs. 2–5, 16–20). Because the theoretical detached-eddy
constant depends only on the coefficients of the length-scale equation and
the Smagorinsky constant, the LRR and SSG branches get the values of the
$k$-$\omega$ and $k$-$\varepsilon$ branches of SST, 0.805 and 0.630, blended
by $F_1$; calibrated with their scheme on decaying isotropic turbulence the
values are 0.5 and 0.3 (§2.3, §3.1). In the LES region the transported
stress acts as the subgrid stress, and on a transonic hammerhead launch
vehicle all its components are smaller than those of SST-IDDES, which, in
Spalart's view as the authors recall, unlocks the Kelvin–Helmholtz
instability faster (§3.3, Fig. 10). On the tandem cylinders and the
hammerhead RSM-IDDES gives a shorter shear layer, finer resolved
structures, better $C_p$ RMS peaks and a shedding frequency of 176 Hz
against 172 Hz for SST-IDDES and 179–180 Hz measured (§3.2–§3.3, Table 1);
the authors credit the anisotropy captured "because the exact production
terms" (§4). Details on the DES page.

Heinz (2022) records that both the partially integrated transport model and
[continuous eddy simulation](/methods/continuous-eddy-simulation.md) exist
in Reynolds-stress versions, and states that the author's conclusions on the
resolution-dependent destruction coefficient, derived for $k$-$\varepsilon$,
carry over to them ([Heinz (2022)](/sources/heinz-2022.md), Table 1, §4).

## The ATAAC DRSM

Bouhafid et al. (2024) run the ATAAC differential Reynolds-stress model in
ONERA's CHARME solver for the RANS of the NASA CRM with engines at
$M_\infty=0.85$, $\alpha=3^\circ$: six Reynolds-stress transport equations
with pressure–strain modelling "based on Wilcox's work", an $\omega$
equation, and an equation modelling near-wall damping, with no coefficients
printed (§2.2, §4). It runs with wall functions at $y^+\approx80$ on twelve
anisotropically [adapted meshes](/methods/mesh-adaptation.md) up to about
110 million cells, and its Reynolds stresses initialize the synthetic
fluctuations of a temporal LES (§4.2, App. A; see
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) and
[inflow turbulence generation](/methods/inflow-turbulence-generation.md)).

## Evidence

**ERCOFTAC T3 plates.** Fully turbulent SSG/LRR-$\omega$ and SST have
similar accuracy on these single-shear flows. SSG/LRR-$\omega$-$\gamma$
matches the measured transition onset at zero (T3A, T3B, T3A–) and
favourable (T3C1, T3C5) pressure gradient, and downstream of transition its
skin friction is typically higher than the fully turbulent models'. Under
adverse pressure gradient (T3C2–T3C4) it delays onset, "similar to the
problem existing in the SST–$\gamma$ model" (Liu et al. 2024, Fig. 6,
Table 2; grid of $365\times193$ points with $y^+<0.4$, Table 3; see
[ERCOFTAC T3 flat plates](/benchmarks/ercoftac-t3-flat-plate.md)).

**Compressor cascades.** On the low-speed PVD cascade ($Re\approx2.3\times10^5$,
$M\approx0.07$) and the transonic NACA65 K48 cascade ($M=0.67$,
$Re=5.6\times10^5$), all three-dimensional SSG/LRR-$\omega$ runs fail to reach a
steady state because of wake shedding and separation bubbles, and the
results are time-averaged URANS over 15 chord-passing periods (Liu et al.
2024, § Flow solvers). The fully turbulent SSG/LRR-$\omega$ is "only slightly
more accurate" than SST for corner separation, overestimating the total
pressure loss and the exit angle at $0^\circ$ incidence. With transition,
the model resolves the mid-chord
[laminar separation bubbles](/definitions/laminar-separation-bubble.md), the
$C_p$ plateaus they cause near 45% and 35% axial chord, and a corner
separation closer in size and topology to the oil flow, and improves loss
and exit angle; it still overpredicts the corner separation under strong
adverse pressure gradient and gives a bimodal spanwise distribution of
the relative displacement thickness where the measurement is unimodal
(Figs. 8–17, Conclusions). The authors' mechanism: the transitional model
keeps the upstream layer laminar so that it separates, and the reattached
turbulent layer is fuller than the fully turbulent one, resisting the
downstream separation (Discussion, Fig. 18). They attribute the remaining
error to the treatment of anisotropy and non-equilibrium under strong
adverse pressure gradient and point to the pressure–strain or the
scale-determining equation as the terms to modify (Conclusions).

**Low-pressure turbine cascade.** On the T161 cascade at an exit Reynolds
number of $9\times10^4$, SSG/LRR-$\omega$ with $\gamma$-$Re_\theta$ follows the LES
decay of $Tu$ through the passage nearly to the trailing edge, where SST
underestimates it shortly behind the leading edge, a result the authors
tie to the correct inflow anisotropy; it reproduces qualitatively the
evolution of the free-stream anisotropy toward the two-component
axisymmetric state and back (Morsbach et al. 2024, §3.3, Fig. 4). It misses
the midspan separation bubble and underestimates the mixed-out wake loss by
29% (SST: 35%), overpredicts the peak end-wall loss by 48% (SST: 34%), and
gives too little $k$ in the passage-vortex core and vortices that are too
compact and too strong, "contrary" to the expectation that such models are
less diffusive for vortices (§4.1–4.2, Figs. 9–14). It misses the
near-one-component turbulence of the transitional shear layer and gives a
rod-like region where the LES has two-component free-stream turbulence; the
authors question the high-Reynolds formulation for this flow (§4.2, Fig.
15). See [turbine cascades](/benchmarks/turbine-cascade.md).

**Delta wing.** On a hybrid delta wing at $\alpha=24^\circ$,
$Re=2.17\times10^6$, $M=0.15$, the SSG/LRR-$\omega$ RANS solution is unsteady,
so the mesh adaptation uses an average-based criterion (68 million cells),
and it gives a smeared vortex velocity field with too much turbulent
kinetic energy, where SST and DDES-SST reproduce the measured vortex
features ([Mozaffari et al. (2022)](/sources/mozaffari-2022.md), §5.2,
Figs. 26–27).

**Transonic buffet.** In the compilation of URANS predictions of the OAT15A
buffet at $\alpha=3.5^\circ$ by Petrocchi & Barakos (2024), the
Reynolds-stress models listed (EHRSM, SORSM) are among those reported to
give self-sustained shock oscillation, at Strouhal numbers of about
0.066–0.074, where Spalart–Allmaras mostly does not
([Petrocchi & Barakos (2024)](/sources/petrocchi-2024.md), App. A, Table
A.4; a compilation of other authors' results).

**Strong adverse pressure gradient.** Ghidoni et al. (2026) use
SSG/LRR-$\omega$ solutions of Knopp et al., with an adverse-pressure-gradient
modification as cited, as the computed reference for the skin friction of
the DLR/UniBw DM2 and DM3 plates ($25<\beta_{RH}<45$, $\beta_{RH}$ the
pressure-gradient parameter, page-local), beside the experiment, when
assessing their $k$-$\omega$ [wall function](/methods/rans-wall-function.md)
([Ghidoni et al. (2026)](/sources/ghidoni-2026.md), §4.2, Fig. 8; see
[wall law in adverse pressure gradient](/definitions/adverse-pressure-gradient-wall-law.md)).

## Qualifications

- Wang et al. (2021) call the Favre average "the hat" while printing a
  tilde (§2.2).

- Liu et al. (2024) print several values the model needs without giving
  them: $\gamma_\omega$, $\beta_\omega$, $\sigma_\omega$, $\sigma_d$ and their
  blending, so the model is not reproducible from that paper alone.
- In their Table 1 the caption defines $c_2^{(\mathrm{LRR})}=0.52$, while the
  LRR row lists $c_2=0$ and the expressions in $c_2^{(\mathrm{LRR})}$ for
  $c_4$, $c_5$ sit in the SSG row; judged from the table's own labels the
  row assignment of some columns is inconsistent (Table 1). The table above
  is transcribed as printed.
- Liu et al. write that production, pressure–strain "and dissipation term"
  are multiplied "by the factor $\gamma$", while their Eq. 20 multiplies the
  dissipation by $\max(\gamma,0.1)$; the equation is given above. Their
  $c_1$ is both a pressure–strain coefficient (3.6/3.4) and the onset
  constant 2.2 of the transition model (Eq. 15).
- Liu et al. print the kinematic stress as $\rho R_{ij}$ and the production
  $P_{ij}$ with a density factor, then write $\tfrac12c_1^*\rho P_{kk}$ in
  the pressure–strain; the per-unit-mass form above removes the density
  throughout *(compiler check, not in the sources)*.
- The vortex evidence differs by flow: too little $k$ and too compact
  vortices in the turbine passage (Morsbach et al. 2024), a smeared vortex
  with too much $k$ over a delta wing (Mozaffari et al. 2022), and a
  recalled claim of better wing-tip-vortex predictions than two-equation
  models (Bouhafid et al. 2024). The first two are computations of
  different flows with different solvers and grids; the third is recalled,
  not shown.

# Citations

- [Liu et al. (2024)](/sources/liu-2024.md) — Introduction, Eqs. 1–9, 20–21, Table 1, Tables 2–3, Figs. 1, 6, 8–18, § Blending, § Flow solvers, Discussion, Conclusions.
- [Morsbach et al. (2024)](/sources/morsbach-2024.md) — §2, §3.3 Fig. 4, §4.1–4.2 Figs. 9–15.
- [Mozaffari et al. (2022)](/sources/mozaffari-2022.md) — §5.2, Figs. 26–27.
- [Bouhafid et al. (2024)](/sources/bouhafid-2024.md) — §2.2, §4, §4.2, App. A.
- [Agrawal & Koutsourelakis (2024)](/sources/agrawal-2024.md) — §2.1.2 (arXiv v2).
- [Petrocchi & Barakos (2024)](/sources/petrocchi-2024.md) — App. A, Table A.4.
- [Wang et al. (2021)](/sources/wang-2021-l.md) — §1, §2.2–§2.4 Eqs. 2–5, 16–20, §3.1, §3.2–§3.3 Table 1 Fig. 10, §4.
- [Heinz (2022)](/sources/heinz-2022.md) — Table 1, §4.
- [Ghidoni et al. (2026)](/sources/ghidoni-2026.md) — §4.2, Fig. 8.
