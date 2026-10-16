---
type: Result
title: "Tearing triggered by impurity radiation through resistive-interchange reversal"
description: "NIMROD/KPRAD simulations show that neon deposited on the q = 2 surface of a nominally tearing-stable tokamak plasma triggers a 2/1 tearing mode above a threshold impurity density, because radiative cooling makes the pressure locally hollow and reverses the sign of the Glasser–Greene–Johnson resistive-interchange parameter D_R; the classical radiation-exceeds-Ohmic-heating criterion does not set the threshold, and fast parallel conduction suppresses the mode."
status: established
aliases: [resistive interchange reversal, D_R reversal, radiation-driven tearing onset, thermo-resistive tearing]
tags: [tearing, impurities, disruption, tokamak, mhd]
timestamp: 2026-10-16T12:00:00Z
---

# Tearing triggered by impurity radiation through resistive-interchange reversal

**Statement.** In an EAST-like L-mode equilibrium that the authors call stable
to tearing, a localized neon deposit on the $q=2$ surface triggers a $2/1$
[tearing mode](/definitions/tearing-mode.md) if its peak density exceeds
$2\times10^{19}$ m$^{-3}$. The trigger is the reversal of the resistive-interchange
parameter $D_R$ from negative to positive by a radiatively hollowed pressure
profile ([Zeng et al. (2023)](/sources/zeng-2023.md), §1, §3, §5).

## The resistive-interchange parameter

Glasser, Greene and Johnson (GGJ) showed that finite pressure and toroidal
curvature add a term $D_R$ to resistive stability at a rational surface. With
$r_s$ the radius of the resonant surface, $L_p=p/p'$ and $L_q=q/q'$ signed
gradient lengths and $\hat s$ the magnetic shear (page-local $D_R$, $L_p$,
$L_q$), the source writes

$$D_R\approx\frac{(r_s/R_0)^2\,\beta_p}{\hat s}\,\frac{L_q}{L_p}\Big(1-\frac1{q^2}\Big)$$

(Zeng et al. 2023, §3, p. 6; $r_s/R_0$ and $\hat s$ are the compiler's
reading of symbols the source leaves undefined). For $q>1$, positive shear and
a normally decreasing pressure ($L_p<0$), $D_R<0$ and the term is
stabilizing. A locally *increasing* pressure ($L_p>0$) makes $D_R>0$, a linear
drive. The same reversal is known in negative-central-shear plasmas (Chu et
al. 1996, cited in §1). In the
[modified Rutherford equation](/definitions/modified-rutherford-equation.md)
$D_R$ enters through a term $\propto D_R/\sqrt{w^2+0.65w_d^2}$, important for
small islands.

## Simulation

* **Model.** NIMROD single-temperature resistive MHD with the KPRAD
  impurity module: a continuity equation per neon charge state
  ($z=0$–10), Spitzer $\eta$, constant $\kappa_\parallel=10^{10}$ m²/s,
  $\kappa_\perp=1$ m²/s, $D=0.1$ m²/s (diffusivities), $70\times64$ third-order
  Lagrange elements, toroidal harmonics $n=0,1$, a perfectly conducting wall
  and no vacuum region (§2, Table 1). Checks with $n=0$–6 are stated, without
  data, to leave the conclusion unchanged. See [NIMROD](/software/nimrod.md).
* **Equilibrium.** $a=0.45$ m, $R_0=1.85$ m, $I_p=0.38$ MA, $B=2.267$ T,
  $q_0=1.484$, $q_{95}=9.768$, core $T_e=2.96$ keV, $S_0=6.4\times10^9$. Its
  own $\Delta'$, or a linear check without impurity, is not reported, so
  "stable" is asserted rather than shown.
* **Impurity.** A Gaussian of radial width 1 cm on $q=2$, localized toroidally
  and poloidally, as a crude pellet deposit; peak $n_{\rm imp}$ from $10^{19}$
  to $10^{20}$ m$^{-3}$, line-averaged 1–10% of the background (§2).

## Findings

1. **Threshold.** Below $n_{\rm imp}=2\times10^{19}$ m$^{-3}$ the perturbation
   decays and no island forms; above it the $2/1$ island grows to saturation
   within 1–3 ms, up to about 10–12 cm for the largest deposits (§3,
   Fig. 1a).
2. **The thermo-resistive criterion is insufficient.** On the $q=2$ surface the
   local radiated power "largely exceeds" the Ohmic heating $\eta J^2$ in every
   run, below and above threshold. The criterion "radiation exceeds Ohmic
   heating", used in density-limit models (Gates & Delgado-Aparicio; White et
   al.), therefore cannot explain the threshold (§3, Fig. 1b). Those models
   apply the criterion inside an existing island, whereas here there is no
   initial island, so the disagreement is one of setting as well as of
   sufficiency. Earlier simulations consistent with the thermo-resistive
   theory started from $\Delta'>0$ profiles with pre-existing islands (§1).
3. **Mechanism of onset.** Cooling digs a narrow hollow-pressure layer around
   $q=2$, with a dip in $j_\parallel$ inside and spikes at its edges; force
   balance stays quasi-static (perturbed flows $10$–$10^2$ m/s). The hollow
   layer turns $D_R$ positive, peaking near 1.5 for the largest deposit, and
   $D_R$ dominates the small-island phase (§3, Figs. 2–3).
4. **Measured tearing index.** The source computes the tearing index from the
   simulation as the jump of the radial derivative of the $2/1$ radial field
   across $q=2$, normalized by the field there; it ranges from 0 to 30 and
   tracks the $2/1$ helical current (§3, Fig. 4b).
5. **Nonlinear phase.** After about 0.5 ms $D_R$ relaxes to about zero while
   the island keeps growing. The growth is then attributed mainly to the $2/1$
   resistivity perturbation from radiative cooling, acting through the
   helical current, against a stabilizing perturbed Pfirsch–Schlüter current
   (§3, Figs. 4c–d). The decomposition of the helical current that supports
   this is called "schematic" and contains undefined coefficients.
6. **Parallel conduction suppresses the mode.** At threshold deposit the island
   grows for $\kappa_\parallel<10^9$ m²/s and stays below 1 cm at
   $10^{10}$ m²/s. Faster parallel equilibration restores the negative
   pressure gradient sooner and turns $D_R$ negative; this agrees with the
   earlier finding that a smaller $\kappa_\parallel/\kappa_\perp$ ratio makes
   tearing more unstable (§4, Fig. 5). A $T_e$-dependent transport model
   gives the same conclusion.

## Relevance

The result is a candidate pre-disruption trigger near the density limit and
after pellet deposition (see [disruption](/definitions/disruption.md) and
[shattered pellet injection](/definitions/shattered-pellet-injection.md)), and
a possible seed of [neoclassical tearing modes](/definitions/neoclassical-tearing-mode.md)
at high $\beta$ (Zeng et al. 2023, §1).

**Limits of the evidence.** Two toroidal harmonics; constant transport
coefficients in the main runs; impurity levels above typical experiment "to
accelerate the dynamics"; the energy equation is printed with anti-diffusive
signs, a typesetting slip recorded on the Source page. The file read is the
arXiv preprint.

## Contradictions

None open. The disagreement with the thermo-resistive onset criterion concerns
references that are not ingested, and the settings differ (no initial
island).

# Citations

- [Zeng et al. (2023)](/sources/zeng-2023.md) — §§1–5, Table 1, Eqs. 1–9, Figs. 1–5.
