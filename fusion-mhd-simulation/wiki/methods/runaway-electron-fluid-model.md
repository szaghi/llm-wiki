---
type: Method
title: "Runaway-electron fluid model coupled to MHD"
description: "Fluid model in which runaway electrons are a separate species described only by their number density, streaming along the field, drifting with the E×B flow and carrying a current that is removed from the resistive Ohm's law; JOREK embeds it in reduced MHD with a diffusive parallel surrogate and explicit avalanche, Compton and tritium sources, M3D-C1 in full MHD with a reduced convection speed and advection by characteristics."
status: established
aliases: [RE fluid model, JOREK runaway electron fluid]
tags: [runaway-electrons, disruption, reduced-mhd, impurities, neutrals, code]
timestamp: 2026-10-16T20:00:00Z
---

# Runaway-electron fluid model coupled to MHD

The [runaway electrons](/definitions/runaway-electrons.md) of a disruption
carry current but no resistive dissipation and no significant pressure.
The fluid model of [JOREK](/software/jorek.md) represents them by one extra
variable, the RE number density $n_{\mathrm{RE}}$, and couples it to the
[reduced MHD](/methods/reduced-mhd.md) through the current
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.11;
[Bandaru et al. (2024)](/sources/bandaru-2024.md), §II). It does not resolve
the RE energy spectrum, but it captures the non-linear interaction of the
REs with the MHD, which the passive test-particle tracer does not
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.11). A second
implementation, in the full MHD of [M3D-C1](/software/m3d-c1.md), is
described below ([Liu et al. (2021)](/sources/liu-2021.md), §2–3).

## Current coupling

All REs are taken to move at the speed of light $c$ along $\mathbf b$, so
the RE current has magnitude $|\mathbf J_{\mathrm{RE}}|=e\,c\,n_{\mathrm{RE}}$
and is parallel to the field. The REs are not resistively damped, so the
resistive Ohm's law acts on the thermal current only:
$$\mathbf E+\mathbf v\times\mathbf B=\eta\,(\mathbf J-\mathbf J_{\mathrm{RE}}).$$
In the reduced model only the toroidal component enters: Bandaru et al.
(2024, Eq. 2.3) subtract $c\,n_{\mathrm{RE}}\,b_\phi$ from the reduced
current variable $j$, with $b_\phi=F_0/(RB)$ and $e$ absorbed in the JOREK
normalization (sign as printed). The Ohmic heating in the pressure equation
uses the same reduced thermal current, $(\Gamma-1)\,\eta\,(j-c\,n_{\mathrm{RE}}b_\phi)^2/R^2$
in normalized units (Eq. 2.8). The model therefore belongs to the
current-coupling family; the general scheme is on
[pressure and current coupling](/methods/pressure-and-current-coupling.md).

## RE transport equation

In canonical notation, the normalized Eq. 2.12 of
[Bandaru et al. (2024)](/sources/bandaru-2024.md) reads
$$\partial_t n_{\mathrm{RE}}=-f_{\mathrm{adv}}\,\nabla\cdot\Big(c\,n_{\mathrm{RE}}\frac{\mathbf B}{B_\phi}\Big)+(1-f_{\mathrm{adv}})\,\nabla\cdot\big(D_{\parallel,\mathrm{RE}}\nabla_\parallel n_{\mathrm{RE}}\big)-\nabla\cdot\big(n_{\mathrm{RE}}\,\mathbf v_{E}\big)+S_{\mathrm{av}}+S_{\mathrm{T}}+S_{\mathrm{C}},$$
with $\mathbf v_E=-R^2\nabla u\times\nabla\phi$ the $E\times B$ velocity of
the stream function $u$ and $B_\phi=F_0/R$. The printed bracket form
$\frac{c}{F_0R}\big([Rn_{\mathrm{RE}},\psi]+F_0\partial_\phi n_{\mathrm{RE}}\big)$
equals the first divergence, and $R[n_{\mathrm{RE}},u]+2n_{\mathrm{RE}}\partial_Zu$
equals $-\nabla\cdot(n_{\mathrm{RE}}\mathbf v_E)$, with
$[f,g]=\mathbf e_\phi\cdot\nabla f\times\nabla g$ and JOREK's
$\mathbf B=F_0\nabla\phi+\nabla\psi\times\nabla\phi$ (compiler's check of the
printed form). Thus:

- **Parallel transport** blends conservative streaming at $c$ with a
  large parallel diffusion that stands in for it, through the advection
  factor $f_{\mathrm{adv}}\in[0,1]$ (after Bandaru et al. 2019). The GO
  benchmark uses $f_{\mathrm{adv}}=10^{-3}$ and
  $D_{\parallel,\mathrm{RE}}=1.54$ m²/s. The DINA benchmark uses
  $f_{\mathrm{adv}}=0$ and $D_{\parallel,\mathrm{RE}}=1.54\times10^8$ m²/s,
  a value said to be "justified through a sensitivity study that will be
  discussed later" that the paper does not present (§III.A, §IV.A).
- **Perpendicular transport** is the $E\times B$ drift only in Eq. 2.12.
- **Sources** are explicit in time, while the rest of JOREK is fully
  implicit ([Bandaru et al. (2024)](/sources/bandaru-2024.md), §II.A).

## Sources (2024 model)

**Avalanche** (Hesslow et al. 2017–2019; Eqs. 2.13–2.17):
$S_{\mathrm{av}}=\Gamma_{\mathrm{av}}n_{\mathrm{RE}}$ with
$$\Gamma_{\mathrm{av}}=\frac{e}{m_ec\ln\Lambda_c}\,\frac{n_e^{\mathrm{tot}}}{n_e}\,\frac{E_\parallel-E_c^{\mathrm{eff}}}{\sqrt{4+\bar\nu_s(\hat p_\star)\,\bar\nu_D(\hat p_\star)}},\qquad n_e^{\mathrm{tot}}=n_e+\sum_j n_j\,(Z_j-z_j),$$
where the sum runs over impurity charge states $j$ of nuclear charge $Z_j$
and charge $z_j$ (so $Z_j-z_j$ bound electrons), $\bar\nu_s$ and $\bar\nu_D$
are the normalized slowing-down and deflection frequencies with partial
screening, and $\hat p_\star$ is the effective critical momentum (in units
of $m_ec$), the root of
$\hat p_\star=(\bar\nu_s\bar\nu_D)^{1/4}(\hat p_\star)\big/\sqrt{E_\parallel/E_c}$
(Eq. 2.15), found by Newton–Raphson at every point. The high-energy-limit
forms of $\bar\nu_s,\bar\nu_D$ gave negative deflection frequencies and
non-convergence at low $\hat p_\star$; the full expressions "were observed
to be numerically robust" (§II.A).

**Effective critical field** (Eqs. 2.18–2.19). $E_c^{\mathrm{eff}}/E_c$ is
an expression in partially screened collision frequencies, synchrotron
damping (through $B^2/n_e$) and bremsstrahlung. Eliminating an auxiliary
variable gives a cubic in $x=E_c^{\mathrm{eff}}/E_c$, solved in closed form
when its discriminant is non-negative and otherwise by Newton–Raphson from
an array of initial guesses, which "work[s] robustly in all the simulations
performed so far" (§II.A.1).

**Tritium decay**: $S_{\mathrm T}=\ln2\,(n_{\mathrm t}/\tau_{\mathrm t})\,F_\beta(W_{\mathrm{crit}})$,
with $n_{\mathrm t}$ the tritium density, $\tau_{\mathrm t}\approx4500$ days
its half-life and $F_\beta$ the fraction of the β spectrum (end-point
18.6 keV) above the critical kinetic energy
$W_{\mathrm{crit}}=m_ec^2(\sqrt{\hat p_\star^2+1}-1)$ (p. 4).

**Compton scattering**: $S_{\mathrm C}$ is $n_e^{\mathrm{tot}}$ times the
integral over photon energy of a fitted wall photon-flux spectrum
multiplied by the Klein–Nishina cross section, integrated over the
scattering angles that give the electron more than $W_{\mathrm{crit}}$
(p. 4).

No Dreicer and no hot-tail source are included (§II.A).

## The EU-DEMO application form (Vannini et al. 2025)

[Vannini et al. (2025)](/sources/vannini-2025.md) (§2, App. A, Eqs. 4,
11, Table 2) cite the same JOREK model (Bandaru et al. 2019 and 2024) and
print a different transport equation,
$$\partial_t n_{\mathrm{RE}}=S_{\mathrm T}+S_{\mathrm C}+S_{\mathrm{av}}-\nabla\cdot\big(n_{\mathrm{RE}}\mathbf v_E\big)+\nabla\cdot\big(D_{\parallel,\mathrm{RE}}\nabla_\parallel n_{\mathrm{RE}}+D_{\perp,\mathrm{RE}}\nabla_\perp n_{\mathrm{RE}}\big),$$
written here in the canonical form of Eq. 2.12 above (the printed
$2n_{\mathrm{RE}}\partial_Zu+R[n_{\mathrm{RE}},u]$ is the same $E\times B$
term), with $D_{\perp,\mathrm{RE}}$ the perpendicular runaway diffusivity:

- **No streaming term.** Parallel transport is pure diffusion "to reduce the
  computational cost", equivalent to $f_{\mathrm{adv}}=0$, with
  $D_{\parallel,\mathrm{RE}}=1.54\times10^9$ m²/s, ten times the DINA-benchmark
  value.
- **Perpendicular diffusion.** $D_{\perp,\mathrm{RE}}=1.54\times10^{-2}$ m²/s,
  a term that Eq. 2.12 does not contain.
- **Avalanche.** Rosenbluth–Putvinski "with corrections for partially
  ionized impurities" (Hesslow et al. 2018, as cited), not the full
  Hesslow form with $\hat p_\star$ described above.
- **Seed.** Tritium decay plus Compton scattering only.
- **Current coupling.** Ohm's law and the Ohmic heating subtract
  $c\,F_0\,n_{\mathrm{RE}}/(BR)$ from $j$ as in Bandaru et al. (2024), while
  §2 writes $j_{\mathrm{RE}}=-e\,c\,n_{\mathrm{RE}}$; the two signs are not
  reconciled in the text (recorded on the Source page).

With this form, 3D restarts of the EU-DEMO beam are MHD-unstable at all
three $q_{95}$ values (growth rates about $1$–$8\times10^4$ s$^{-1}$), the
field stochastizes from the edge inward, and the runaway current falls from
12.3 to 2.8 MA in 1.12 ms before the core remnant re-avalanches (§5,
Figs. 5–9; see [runaway electrons](/definitions/runaway-electrons.md)).
Without a velocity distribution, the energy for the wall-load estimate is
assigned to test markers from an energy balance
([runaway-electron wall loads](/definitions/runaway-electron-wall-loads.md)).

## M3D-C1 implementation (full MHD)

[Liu et al. (2021)](/sources/liu-2021.md) (§2, Eqs. 1–9) couple an RE
density to single-temperature ($T_e=T_i$) full MHD in M3D-C1:

- **RE current.** It includes the $E\times B$ drift,
  $\mathbf J_{\mathrm{RE}}=-e\,n_{\mathrm{RE}}\,(c\,\mathbf b+\mathbf v_E)$
  with $\mathbf v_E=\mathbf E\times\mathbf B/B^2$ (Eq. 4).
- **Momentum.** The force is $e\,n_{\mathrm{RE}}\mathbf E+(\mathbf J-\mathbf J_{\mathrm{RE}})\times\mathbf B-\nabla p$
  (Eq. 1). Substituting Eq. 4 cancels the perpendicular part, and the
  remaining parallel term $e\,n_{\mathrm{RE}}E_\parallel$ "is not included in
  the current implementation" (p. 5).
- **Ohm's law and heating.** Ohm's law is
  $\mathbf E+\mathbf v\times\mathbf B=\eta(\mathbf J-\mathbf J_{\mathrm{RE}})$,
  and the Ohmic heating is $\eta(\mathbf J-\mathbf J_{\mathrm{RE}})^2$
  (Eqs. 5, 8). There is no RE collisional friction, and gradient and
  curvature drifts are neglected.
- **Transport.** The continuity equation
  $\partial_tn_{\mathrm{RE}}+\nabla\cdot[n_{\mathrm{RE}}(c_{\mathrm{RE}}\mathbf b+\mathbf v_E)]=S_{\mathrm{RE}}$
  (Eq. 3) convects at a numerical speed $c_{\mathrm{RE}}\le c$,
  "usually set to be a smaller value for numerical
  efficacy" (p. 5), while the current uses $c$. There is no
  parallel-diffusion surrogate.
- **Sources.** None in the instability runs. The post-loss phase uses the
  Rosenbluth–Putvinski avalanche only, with no Dreicer, hot-tail, tritium or
  Compton source (§5.4).
- **Solver.** Eq. 3 was previously advanced by the θ-implicit Galerkin
  scheme of the other fields. In 3D it is now solved by
  [advection along characteristics](/methods/runaway-electron-advection-by-characteristics.md),
  because the implicit solve becomes ill-conditioned when
  $c_{\mathrm{RE}}\gg v_A$ (§3).

**Sensitivity to $c_{\mathrm{RE}}$** (§5.2–5.3, Figs. 9, 14b). The linear
(2,1) growth rate and frequency are "not sensitive" to $c_{\mathrm{RE}}/v_A$
above 4. From the figure, $\gamma\tau_A$ still drops by about 11% from 4 to 16,
and it is 0.073 at 2 against about 0.053 at 8. The nonlinear saturation is
sensitive: at $c_{\mathrm{RE}}/v_A=2$ the peak $W_{\mathrm{mag}}^{(1)}$ is about
3000 J, against 1400–1650 J at 8 and 32. The authors conclude that a large
$c_{\mathrm{RE}}$ is necessary. They cite as consistent the JOREK finding that
the linear growth depends only weakly on the convection speed (§6).

**Limitation common to both implementations.** The model has one density and
no pitch or energy variable. It cannot represent magnetically trapped
runaways, which [McDevitt & Tang (2023)](/sources/mcdevitt-2023.md) find
survive a stochastic flush as a reconstitution seed (compiler's remark; see
[runaway reconstitution after an MHD flush](/results/runaway-reconstitution-after-mhd-flush.md)).
It can still reconstitute a beam from runaways that stay on closed core
surfaces, as in EU-DEMO ([Vannini et al. (2025)](/sources/vannini-2025.md),
§5).

## Coupling to impurities and neutrals

The 2024 extension embeds the RE fluid in a single-temperature reduced
model with [coronal-equilibrium impurities](/methods/coronal-equilibrium-impurity-model.md)
(one $\rho_{\mathrm{imp}}$, Eq. 2.10) and a diffusive deuterium-neutral
fluid ([fluid neutral models](/methods/fluid-neutral-models.md), Eq. 2.11).
These supply $n_e$, $n_e^{\mathrm{tot}}$, $Z_{\mathrm{eff}}$ and the
charge-state densities of the sources; impurity line radiation, deuterium
continuum and line radiation enter the pressure equation (Eq. 2.8)
([Bandaru et al. (2024)](/sources/bandaru-2024.md), §II). Including the
impurities raises the critical field and adds bound electrons for the
avalanche, "with the latter effect dominating at high electric fields"
(§II). The authors state that the new sources give "a much stronger RE beam
formation than the previous code version" (§II.A); no side-by-side run is
shown. In 2021 the interaction terms with the impurity fluid were "under
development" ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.11).

## Verification and use

- Current conversion against GO, and linear resistive internal kinks with
  a prescribed RE current fraction
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §4.7), and the 2024
  ITER benchmarks against GO and DINA
  ([ITER runaway-electron benchmarks](/benchmarks/iter-runaway-electron-benchmarks.md)).
- Applications: VDEs with REs, RE-driven 1/1 kinks, JET benign beam
  termination ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6.4.2);
  beam formation in a 2D EU-DEMO VDE, its 3D termination and the
  marker-based wall loads, the 3D runs feasible only with the enhanced
  JOREK preconditioner of Holod et al. 2021
  ([Vannini et al. (2025)](/sources/vannini-2025.md), §4–6);
  an equilibrium with an RE beam and kinetic coupling under development
  ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.5).
- Extensions: the effect of REs on the radial force balance
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.11); planned
  evolution of a mean parallel RE momentum (§2.15); coupling to the JOREK
  SPI model in 3D is "in principle, possible", but the effect of REs on
  pellet ablation is not included
  ([Bandaru et al. (2024)](/sources/bandaru-2024.md), §V).

## Contradictions

**Artificial parallel diffusion as a surrogate for streaming** — Open
(judgement disagreement). [Liu et al. (2021)](/sources/liu-2021.md) (§3,
p. 7) state that reduced convection speeds and artificial diffusion, used in
earlier fluid-RE codes including the 2019 JOREK model, "can possibly reduce
the MHD mode growth or even suppress unstable modes". They also find that a
small convection speed changes the nonlinear saturation (§5.3, Fig. 14b).
[Bandaru et al. (2024)](/sources/bandaru-2024.md) (§III–IV) use exactly such
a surrogate in their ITER benchmarks: $f_{\mathrm{adv}}=10^{-3}$ with
$D_{\parallel,\mathrm{RE}}=1.54$ m²/s against GO, and $f_{\mathrm{adv}}=0$
with $D_{\parallel,\mathrm{RE}}=1.54\times10^8$ m²/s against DINA. They say
the latter value is justified by a sensitivity study that the paper does not
present. Neither paper tests the other's setting. Liu et al. demonstrate no
diffusion-induced suppression, and the GO benchmark freezes the flow, so it
cannot reveal one. [Vannini et al. (2025)](/sources/vannini-2025.md) (§5)
add a data point: with the pure diffusive surrogate at
$D_{\parallel,\mathrm{RE}}=1.54\times10^9$ m²/s the 3D EU-DEMO beam modes
grow at $1$–$8\times10^4$ s$^{-1}$ and stochastize the field, so the
surrogate does not suppress them there; with no streaming control run, this
does not show whether it reduces them. A 3D tearing or kink case with REs,
run once with conservative streaming and once with the diffusive surrogate
at the benchmark values, would settle it.

**Dreicer source in the JOREK RE fluid model** — Open (model version).
[Hoelzl et al. (2021)](/sources/hoelzl-2021.md) (§4.7) describe the GO
benchmark of the model of Bandaru et al. (2019) with Dreicer generation
switched on above $E_\parallel/E_D\ge0.01$ and avalanche above
$E_\parallel/E_c\ge1.7$. [Bandaru et al. (2024)](/sources/bandaru-2024.md)
(§II.A) state that "there is currently no Dreicer source included in the RE
fluid model". The two statements most likely describe different code
versions, with the 2024 source set replacing the 2019 one. Neither paper
says when or why the Dreicer term was removed. Ingesting Bandaru et al.
(2019) and any later model description would settle whether this is a
removal or a source-set replacement.

**Transport terms and avalanche form of the JOREK RE fluid model** — Open
(model version or description). [Bandaru et al. (2024)](/sources/bandaru-2024.md)
(§II, Eq. 2.12) print a streaming term weighted by $f_{\mathrm{adv}}$, no
perpendicular runaway diffusion, and the Hesslow avalanche with an
effective critical momentum $\hat p_\star$ found by Newton–Raphson.
[Vannini et al. (2025)](/sources/vannini-2025.md) (§2, App. A, Eq. 11),
citing the same model (Bandaru et al. 2019, 2024), print no streaming term,
a perpendicular diffusion $D_{\perp,\mathrm{RE}}$, and a Rosenbluth–Putvinski
avalanche with partial-ionization corrections. Either the code offers both
options and each paper describes the one it used, or one description is
incomplete; neither paper says which. A model description that lists the
options (the cited Bandaru et al. 2019, not ingested, or a code manual)
would settle it.

# Citations

- [Bandaru et al. (2024)](/sources/bandaru-2024.md) — §II, Eqs. 2.1–2.19; §III.A; §IV.A; §V.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — §2.11, §2.15, §4.7, §6.4.2.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) — §3.5.
- [Liu et al. (2021)](/sources/liu-2021.md) — §2–3, §5.2–5.4, §6, Eqs. 1–9, Figs. 9, 14.
- [McDevitt & Tang (2023)](/sources/mcdevitt-2023.md) — pp. 1–4.
- [Vannini et al. (2025)](/sources/vannini-2025.md) — §2, §4–6, App. A, Eqs. 4, 11, Table 2.
