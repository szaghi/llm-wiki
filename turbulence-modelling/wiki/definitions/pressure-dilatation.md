---
type: Definition
title: "Pressure dilatation"
description: "The pressure dilatation, the product of pressure and velocity divergence, exchanges kinetic and internal energy in compressible flow; this page defines its volume-averaged, turbulent (Favre-averaged), resolved and subgrid forms, how sources measure it in decaying turbulence, wall turbulence and shock interactions, how it is modelled, and how discretizations perturb it."
status: established
aliases: [pressure-dilatation, pressure–dilatation correlation, pressure dilatation work, pressure-dilatation work, pressure-dilatation term, SGS pressure dilatation, subgrid pressure dilatation, pressure dilatation dissipation rate]
tags: [compressible, dns, les, rans, numerical-dissipation]
timestamp: 2026-10-28T07:06:00Z
---

# Pressure dilatation

The **pressure dilatation** is the term $p\,\partial_ju_j$ that appears with
opposite signs in the equations for the kinetic energy and for the internal
energy of a compressible fluid: it is reversible work that converts internal
into kinetic energy where the fluid expands ($\partial_ju_j>0$) and kinetic
into internal energy where it is compressed. Unlike the viscous dissipation
it has no definite sign. In incompressible flow it vanishes identically, so
it is one of the "genuine compressibility" terms of a turbulence budget.
The sources of this bundle meet it in four forms: volume-averaged in
decaying box turbulence, Favre-averaged in the turbulent-kinetic-energy
budget, split into resolved and subgrid parts in LES, and modelled in RANS
compressibility corrections.

Symbols: $\Pi^{\mathrm t}_{\mathrm{pd}}$ the turbulent pressure
dilatation of the Favre-averaged budget, $\Pi^{\mathrm{sgs}}_{\mathrm{pd}}$
the subgrid pressure dilatation of LES (registry §11; neither is the registry's $\Pi$,
the subgrid energy flux, which keeps its meaning below); page-local: $e$ the specific
internal energy; $q_j$ the heat flux.

## The exchange term

For a Newtonian fluid with viscous stress $\sigma_{ij}$, the kinetic and
internal energy equations read

$$\begin{aligned}
\partial_t\big(\tfrac12\rho u_iu_i\big)+\partial_j\big(\tfrac12\rho u_iu_iu_j+pu_j-\sigma_{ij}u_i\big)&=p\,\partial_ju_j-\sigma_{ij}\partial_ju_i,\\
\partial_t(\rho e)+\partial_j(\rho eu_j+q_j)&=-p\,\partial_ju_j+\sigma_{ij}\partial_ju_i,
\end{aligned}$$

so $p\,\partial_ju_j$ and the viscous dissipation $\sigma_{ij}\partial_ju_i$
are the two exchange terms, and only the second is sign-definite
*(compiler check, not in the sources)*. In a periodic box the flux terms
integrate to zero and the decay rate of the mean kinetic energy is the
viscous dissipation minus the volume average $\langle p\,\partial_ju_j\rangle$.
This is the split that [Volpiani (2024)](/sources/volpiani-2024.md), §3.2,
Eq. (25), [Cao et al. (2022)](/sources/cao-2022.md), §3.1, and
[Zhao et al. (2023a)](/sources/zhao-2023.md), §5.1, write for the
compressible [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md):
deviatoric-strain, [bulk-viscous](/definitions/bulk-viscosity.md) and
pressure-dilatation terms, the last with a minus sign,
$-\frac{1}{\rho_0|\Omega|}\int p\,\nabla\cdot\boldsymbol u\,dV$
($\rho_0$ the reference density, $|\Omega|$ the box volume).
[Tonicello et al. (2022)](/sources/tonicello-2022.md), §4, Eq. (4.10),
describe the same term in the resolved kinetic-energy balance as the
exchange between kinetic and internal energy.

## Volume-averaged pressure dilatation in decaying turbulence

- **Nearly incompressible flow.** In the Taylor–Green vortex at Mach 0.1 the
  pressure-dilatation term is negligible against the deviatoric
  dissipation (Cao et al. 2022, §3.1, Fig. 5); Volpiani (2024), at Mach
  0.085, uses it only as part of a "theoretical" dissipation rate checked
  against the incompressible enstrophy relation.
  [Cao et al. (2022b)](/sources/cao-2022-c.md), §IV A, Eq. (16), Fig. 3,
  find the same in implicit and explicit LES of the Taylor–Green vortex at
  $M=0.1$, $Re=1600$ ($256^3$, fourth-order gas-kinetic scheme): the
  pressure-dilatation part $\varepsilon_3=-\frac{1}{\rho_0|\Omega|}\int p\,\nabla\cdot\boldsymbol u\,dV$
  of the physical dissipation is negligible, and all models predict it
  alike.
- **Compressible decay.** In decaying isotropic turbulence at turbulent Mach
  numbers 0.8 to 1.6, Cao et al. (2022), §3.4, Fig. 14, find that the
  pressure dilatation changes sign during the evolution and then stays
  small and positive, as in the subsonic results of Sarkar et al. that
  they cite, and that early in supersonic decay it can be of the order of
  the total dissipation (see
  [homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)).
- **As a residual.** [Brillon & Nadarajah (2026)](/sources/brillon-2026.md)
  (read in arXiv v1), §3.1.1, Eq. (105), obtain an "observed" pressure
  dilatation of the compressible Taylor–Green vortex as the measured decay
  rate minus the viscous term, which agrees with published DNS, while the
  pressure dilatation computed node by node in their flux-reconstruction
  scheme oscillates spuriously; collocation reduces and upwind interface
  dissipation removes the oscillations (§3.1.7, Figs. 17–18; see
  [flux reconstruction](/methods/flux-reconstruction.md)).
- **Discrete consistency.** [Kuya et al. (2018)](/sources/kuya-2018.md),
  §2.4.2, derive the pressure-diffusion flux consistent with a central
  discretization of the pressure work $u_j\partial_jp$ and of the pressure
  dilatation $p\,\partial_ju_j$, and show that the divergence-form flux
  evaluates the pressure dilatation implicitly as an average over the two
  neighbouring points, which induces internal-energy and entropy errors
  (§4.4, Eq. 66). In their inviscid Taylor–Green runs at $M_0=0.4$ the
  volume-averaged pressure-dilatation rate of the most consistent scheme
  rises suddenly at $M_0t\simeq20$, in step with its kinetic-energy loss,
  and they attribute a "negligibly small" long-run entropy reduction to the
  non-conservative form of the term (§5.2, Figs. 4–5; see
  [kinetic-energy preservation](/properties/kinetic-energy-preservation.md)
  and [entropy conservation](/properties/entropy-conservation.md)).

## Turbulent pressure dilatation in the Favre-averaged budget

With Favre fluctuations $u_i''$ and Reynolds fluctuations $p'$, the
transport equation of $\tfrac12\langle\rho u_i''u_i''\rangle$ contains

$$\Pi^{\mathrm t}_{\mathrm{pd}}=\Big\langle p'\,\frac{\partial u_i''}{\partial x_i}\Big\rangle$$

next to production, turbulent, pressure and viscous diffusion, dissipation
and the mass-flux term $\langle u_i''\rangle(\partial_j\langle\sigma_{ij}\rangle-\partial_i\langle p\rangle)$,
as written by [Yu et al. (2022)](/sources/yu-2022-e.md), Eq. (4.1), who
call the pressure-dilatation and the mass-flux terms the "genuine
compressibility" effects. The sources that measure it in wall turbulence
and shock interactions agree that it is small away from shocks:

- **Oblique shock on a supersonic boundary layer.** In a DNS of a Mach 2.28
  boundary layer ($Re_\tau=201$ at the reference station) hit by the shock
  of an 8° wedge, Yu et al. (2022) find both compressibility terms
  significant only near the impinging shock; upstream of the interaction
  the budget resembles that of canonical compressible wall turbulence (§4,
  Fig. 6). Their scale-by-scale (spanwise-spectral) budget gives a
  pressure-dilatation spectrum that is "trivial" except near the impinging
  and reflected shocks, with a small negative region near the wall at
  $x^*\approx-1.5$ ($x^*$ the streamwise distance from the impingement over
  the reference thickness) (§6.2, Fig. 11a). Their caveat: near the shocks
  the shock-capturing dissipation makes the spectral budget unreliable
  (§7). In the follow-up study of the same DNS database, which follows
  the turbulence recovery downstream of the interaction,
  [Yu et al. (2023)](/sources/yu-2023.md), §5.2, Eq. (5.2), write the same
  Favre budget and drop both the pressure-dilatation and the mass-flux
  terms at $M_\infty=2.28$, citing earlier interaction studies (Li et al.
  2010, Jammalamadaka et al. 2014, Tong et al. 2017) rather than their own
  budget; the retained production, dissipation, advection and turbulent
  transport then carry the recovery, with dissipation about $0.8$ of the
  production in magnitude for $0.2\le y/\delta\le1$. See
  [shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md).
- **Separated hypersonic interactions.** In the turbulent-kinetic-energy
  budgets of two hypersonic compression-ramp LES (Mach 7.2 over a 33° ramp,
  Mach 9.1 over a 34° ramp),
  [Helm & Martín (2022)](/sources/helm-2022.md), Sec. IV D, Fig. 27, find
  pressure work and pressure dilatation small in the separation shear
  layer, where production is balanced by transport, convection, pressure
  diffusion and (mostly subgrid) dissipation.
- **Strong compression-ramp interaction, budget listed but not
  analysed.** In a DNS of the Mach 2.9, 24° compression ramp,
  [Kang & Lee (2024)](/sources/kang-2024.md), §IV.D, Eq. (22), Table V,
  write the same seven-term Favre budget, with the pressure dilatation
  $\langle p'\,\partial u_i''/\partial x_i\rangle$ listed next to pressure
  diffusion and the mass-flux term, and then analyse only production and
  turbulent transport, "since these terms are dominant", by citation of
  earlier ramp studies, not from their own budget. The turbulence
  amplification they explain with those two terms is on
  [shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md).
- **Hypersonic cold-wall boundary layers.**
  [Zhang et al. (2024b)](/sources/zhang-2024-b.md), §3.1, Eqs. (3.7)–(3.14),
  Fig. 7, compute the full budget of the Mach 6 boundary layers upstream of
  their 34° ramp interactions ($T_w/T_r=0.50$, $0.75$, $1.0$) in semi-local
  scaling. They group pressure diffusion and pressure dilatation into one
  pressure term, $-\partial_i\langle p'u_i''\rangle+\langle p'\,\partial_iu_i''\rangle$,
  and report that the budgets balance and agree with the Mach 5 cold-wall
  DNS of Duan et al. (2010) that they cite; no separate value of the
  pressure-dilatation part is printed.

## Resolved and subgrid pressure dilatation in LES

Filtering splits the term. With the LES filter $\bar\cdot$ and the
Favre filter $\tilde\cdot$, the resolved kinetic-energy equation carries
the **resolved pressure-dilatation work** $\bar p\,\partial_j\tilde u_j$
(Tonicello et al. 2022, Eq. 4.10, their $K_1$), and the subgrid
kinetic-energy equation carries the **subgrid pressure dilatation**

$$\Pi^{\mathrm{sgs}}_{\mathrm{pd}}=\overline{p\,\partial_ju_j}-\bar p\,\partial_j\tilde u_j,$$

as written by [Qi et al. (2022)](/sources/qi-2022-b.md), Eq. (3.6), after
the exact compressible $k_{\mathrm{sgs}}$ equation of Chai & Mahesh that
they cite. [Cao et al. (2022b)](/sources/cao-2022-c.md), §IV B, Eq. (17),
list a subgrid pressure-dilatation term next to production, dissipation
and diffusion in the transport equation of the a priori (box-filtered DNS)
subgrid kinetic energy, referring to an earlier paper of theirs for its
form; their analysis then uses only the production term (see
[energy backscatter](/definitions/energy-backscatter.md)).

**Normalization by the total dissipation.** In decaying compressible
isotropic turbulence of a dense gas (initial $M_t=0.4$ and $0.8$),
[Zhang et al. (2022d)](/sources/zhang-2022-h.md), §IV B, normalize the
subgrid energy flux by the DNS dissipation of kinetic energy written as
$\langle-p\,\nabla\cdot\boldsymbol u\rangle$ plus the viscous dissipation,
i.e. with the pressure dilatation counted as part of it. Their filtered
dense-gas equations (§II, Eqs. 15–23) also carry two pressure-related
subgrid terms an ideal gas lacks in that form: a subgrid pressure, the
filtered pressure minus the pressure of the filtered state (the
Martin–Hou equation of state is nonlinear in density and temperature),
and a subgrid pressure work, $\overline{pu_j}$ minus that pressure times
$\tilde u_j$. A priori (Tables IV–V), the root-mean-square divergence of
the subgrid pressure work is 2.357 at $M_t=0.4$ and 4.112 at $M_t=0.8$,
that of the subgrid turbulent diffusion 7.582 and 5.563, the
subgrid-pressure gradient 0.101 and 0.386 and the subgrid-stress
divergence 1.657 and 1.434; the authors count the pressure work among
the dominant terms and call the subgrid pressure an order of magnitude
smaller than the other unclosed terms (§IV A, §V). Dropping all
thermodynamic subgrid terms changes the a posteriori results little in
these cases (§IV B, §V). See
[large-eddy simulation](/definitions/large-eddy-simulation.md).

**Correlation with the subgrid energy transfer.** Tonicello et al. (2022)
use a DNS of a Mach 2.91 compression/expansion ramp (spectral difference,
$N=5$ in the registry's convention) a priori, both Favre-averaged in time
and span (the RANS sense) and explicitly filtered with Germano's
differential filter at $\Delta=2h$, $4h$ and $8h$ ($h$ the DNS
resolution). Their stress, Eq. (4.4), is the negative of the registry's,
so their subgrid (or Reynolds-stress) dissipation $K_3$ is the registry's
$-\Pi$, positive for backscatter *(compiler check, not in the sources)*. Joint
PDFs show compression associated with forward transfer and expansion with
backscatter, an effect that strengthens with filter width (§4.2,
Figs. 23–24). The correlation coefficient of $\bar p\,\partial_j\tilde u_j$
with $-\Pi$ is 0.2775 for the Favre average and 0.1936 and 0.2682 for the
filter widths $4h$ and $8h$; per quadrant it is larger in expansion with
backscatter (0.8781, 0.5252, 0.6062) than in compression with forward
transfer (0.070, 0.3278, 0.3269) (Table 4). Removing the spherical part of
the stress, $\Pi_{\mathrm{sph}}=-\tfrac13\tau_{kk}\partial_j\tilde u_j=-\tfrac23\bar\rho k_{\mathrm{sgs}}\partial_j\tilde u_j$
(their $\Lambda$; registry §11), the correlation with the deviatoric
transfer drops to 0.1081, 0.0370 and 0.0889 (Table 6): the mean
dilatation–transfer correlation comes mainly from the trace, while in
filtered fields a mild correlation persists (§5). From the Table 4 trend
the authors conclude that the weight of compressibility in a model is set
"not entirely by the physics of the problem" but strongly by the filter
width (§4.2). The decomposition is on
[energy backscatter](/definitions/energy-backscatter.md); the testing
protocol on
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md).

## Models

- **One-equation LES.** Qi et al. (2022), Eq. (3.24), close the subgrid
  pressure dilatation with the leading term of a Taylor expansion of the
  filtered product, $\Pi^{\mathrm{sgs}}_{\mathrm{pd}}\approx C_0\Delta_m^2\,\partial_m\bar p\,\partial_m\partial_k\tilde u_k$
  (summed over $m$; $C_0$ the single coefficient of their quasi-dynamic
  model, fixed locally by the subgrid kinetic energy; $\Delta_m$ the
  grid spacing in direction $m$), and report a "relatively high" a priori
  correlation for it (Fig. 3); the model is on
  [dynamic procedure](/methods/dynamic-procedure.md).
- **RANS compressibility correction.** The $k$-$\omega$ SST runs of
  [Zhao et al. (2023b)](/sources/zhao-2023-b.md), §2, add the
  pressure-dilatation model of Suzen & Hoffmann that they cite, a term
  proportional to the squared turbulent Mach number with constants 0.4
  and 0.2, active only in the outer branch; it is given on
  [$k$-$\omega$ SST](/methods/k-omega-sst-model.md).
- **The trace as a bulk viscosity.** Tonicello et al. (2022), §5, propose
  (heuristically, without a test) to model the spherical part of the
  subgrid stress, which carries the mean dilatation–transfer correlation,
  by a [bulk viscosity](/definitions/bulk-viscosity.md).

## Qualifications

- **Names.** Qi et al. (2022) call $\Pi^{\mathrm{sgs}}_{\mathrm{pd}}$
  "pressure dilatation" in §3.1 and "pressure diffusion" in §3.2 and the
  Fig. 3 caption, for the same symbol defined by their Eq. (3.6). Yu et
  al. (2022) write the term $\Pi_K$ in Eq. (4.1) and $\Pi_k$ in the text.
  Kang & Lee (2024) write it $\Pi$, the symbol the registry reserves for
  the subgrid energy flux; Zhang et al. (2024b) write $\Pi=\Pi_t+\Pi_d$
  for the pressure diffusion plus the pressure dilatation.
- **Sign of the dissipation in the budgets.** Kang & Lee (2024), Table V,
  and Zhang et al. (2024b), Eq. (3.12), both define the dissipation so that
  it enters the right-hand side as a negative term, next to a pressure
  dilatation of either sign; Kang & Lee print the production row of
  Table V garbled ("$P_k-\bar\rho\langle u_i''u_i''\rangle\frac{\langle u_i\rangle}{\partial x_j}$",
  with a minus sign for the equals sign, a repeated index and no
  $\partial$ in the numerator).
- **Evidence.** All findings above are from single configurations: one
  shock-interaction DNS each (Yu et al., whose 2023 study neglects the
  term in the recovery region by citation; Tonicello et al.), two LES of
  ramp interactions (Helm & Martín), one family of decaying runs (Cao et
  al.), one dense gas in one decaying configuration (Zhang et al. 2022d). Tonicello et al.'s correlations are a priori, with no LES run.
- **What a "small" term means.** Yu et al. and Helm & Martín judge the
  term against the other terms of the turbulent budget; Cao et al. against
  the total dissipation of the box. Neither comparison is made by the
  other source.

# Citations

- [Tonicello et al. (2022)](/sources/tonicello-2022.md) — §4, Eqs. (4.1)–(4.10) (resolved pressure-dilatation work $K_1$); §4.2, Table 4, Figs. 23–24; §5, Eqs. (5.1)–(5.3), Table 6 (correlation with the subgrid transfer, spherical part).
- [Yu et al. (2022)](/sources/yu-2022-e.md) — §4, Eq. (4.1), Fig. 6 (turbulent pressure dilatation in an oblique shock interaction); §6.2, Fig. 11a (spectral pressure dilatation); §7.
- [Yu et al. (2023)](/sources/yu-2023.md) — §5.2, Eq. (5.2), Fig. 15 (pressure dilatation and mass-flux terms neglected at $M_\infty=2.28$ by citation; $D_K/P_K\approx-0.8$ in the outer layer).
- [Qi et al. (2022)](/sources/qi-2022-b.md) — §3.1, Eqs. (3.1), (3.6); §3.2, Eq. (3.24), Fig. 3 (subgrid pressure dilatation and its model).
- [Cao et al. (2022)](/sources/cao-2022.md) — §3.1, Fig. 5; §3.4, Fig. 14 (volume-averaged pressure dilatation in the Taylor–Green vortex and in compressible decay).
- [Cao et al. (2022b)](/sources/cao-2022-c.md) — §IV A, Eq. (16), Fig. 3 (negligible $\varepsilon_3$ at $M=0.1$); §IV B, Eq. (17) (subgrid pressure dilatation in the a priori $k_{\mathrm{sgs}}$ equation).
- [Zhang et al. (2022d)](/sources/zhang-2022-h.md) — §II, Eqs. (15)–(23) (subgrid pressure and pressure work of dense gas); §IV A, Tables IV–V; §IV B (normalization by $\langle-p\nabla\cdot\boldsymbol u\rangle$ plus viscous dissipation); §V.
- [Zhao et al. (2023a)](/sources/zhao-2023.md) — §5.1, Eqs. (22)–(23) (pressure-dilatation term of the energy budget).
- [Volpiani (2024)](/sources/volpiani-2024.md) — §3.2, Eq. (25) (pressure-dilatation term of the compressible dissipation budget).
- [Brillon & Nadarajah (2026)](/sources/brillon-2026.md) — arXiv 2411.12108v1: §3.1.1, Eq. (105); §3.1.7, Figs. 17–18 (observed and node-wise pressure dilatation).
- [Kuya et al. (2018)](/sources/kuya-2018.md) — §2.4.2, Eqs. (47)–(50); §4.4, Eq. (66); §5.2, Figs. 4–5, Eq. (74) (discrete pressure dilatation).
- [Helm & Martín (2022)](/sources/helm-2022.md) — Sec. IV D, Fig. 27 (small pressure dilatation in separated hypersonic interactions).
- [Zhao et al. (2023b)](/sources/zhao-2023-b.md) — §2, Eq. (2-5) (Suzen–Hoffmann pressure-dilatation model).
- [Kang & Lee (2024)](/sources/kang-2024.md) — §IV.D, Eq. (22), Table V (pressure dilatation listed in the Favre budget of a Mach 2.9 ramp DNS, not analysed).
- [Zhang et al. (2024b)](/sources/zhang-2024-b.md) — §3.1, Eqs. (3.7)–(3.14), Fig. 7 (semi-locally scaled budget of Mach 6 cold-wall boundary layers; pressure diffusion and dilatation grouped).
