---
type: Method
title: "Runaway-electron fluid model coupled to MHD"
description: "JOREK model in which runaway electrons are a separate species described only by their number density, streaming along the field at the speed of light, drifting with the E×B flow and carrying a current that is removed from the resistive Ohm's law; sources are avalanche with partial screening plus Compton and tritium seeds, treated explicitly."
status: established
aliases: [RE fluid model, JOREK runaway electron fluid]
tags: [runaway-electrons, disruption, reduced-mhd, impurities, neutrals, code]
timestamp: 2026-10-16T00:00:00Z
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
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.11).

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
- **Perpendicular transport** is the $E\times B$ drift only.
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
  an equilibrium with an RE beam and kinetic coupling under development
  ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.5).
- Extensions: the effect of REs on the radial force balance
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.11); planned
  evolution of a mean parallel RE momentum (§2.15); coupling to the JOREK
  SPI model in 3D is "in principle, possible", but the effect of REs on
  pellet ablation is not included
  ([Bandaru et al. (2024)](/sources/bandaru-2024.md), §V).

## Contradictions

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

# Citations

- [Bandaru et al. (2024)](/sources/bandaru-2024.md) — §II, Eqs. 2.1–2.19; §III.A; §IV.A; §V.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — §2.11, §2.15, §4.7, §6.4.2.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) — §3.5.
