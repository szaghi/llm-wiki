---
type: Method
title: "Fractional subgrid-scale model"
description: "The fractional subgrid-scale model closes the divergence of the subgrid stress with a fractional Laplacian of the filtered velocity, derived from a filtered BGK equation; its dynamic form computes the coefficient from a Germano identity posed on forces and fixes the fractional order from filtered DNS of isotropic turbulence."
status: established
aliases: [FSGS, D-FSGS, dynamic fractional SGS model, dynamic nonlocal subgrid-scale model, nonlocal SGS model, fractional Laplacian SGS model]
tags: [les, sgs-model, data-driven, filtering]
timestamp: 2026-10-28T07:07:00Z
---

# Fractional subgrid-scale model

The **fractional subgrid-scale (FSGS) model** is a nonlocal closure: it
models the subgrid force $\partial_j\tau_{ij}$ of the
[filtered equations](/definitions/large-eddy-simulation.md) directly, not
the stress, as a coefficient times a **fractional Laplacian** of the
filtered velocity. Let $s\in(0,1]$ denote the fractional order (page-local;
the source's $\alpha$, which the registry reserves for the DG blending
factor). Then

$$\partial_j\tau_{ij}=\nu_s\,(-\nabla^2)^s\,\bar u_i,\qquad \nu_s=C_{\mathrm{fr}}\,F(s),$$

with $C_{\mathrm{fr}}$ a model coefficient and $F(s)$ a known function of the order
(both page-local). [Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md)
(§II.1, Eqs. 11–15) take the model from the earlier work of their group
(Samiee, Akhavan-Safaei & Zayernouri 2020) and make it
dynamic (§II.2, Eqs. 16–22): the **dynamic fractional SGS model (D-FSGS)**.
They describe it as the first SGS model that is both nonlocal and dynamic
(§I). The Source page records the version read, arXiv:2111.10936v3.

## Kinetic origin

The model is derived at the kinetic level; Seyedi & Zayernouri summarize the
derivation of Samiee et al. (§II.1, Eqs. 5–10).
The single-particle distribution obeys the BGK equation, a relaxation
towards a Maxwellian equilibrium with a relaxation time. Filtering the BGK
equation leaves a closure problem, because the filtered Maxwellian is not
the Maxwellian of the filtered peculiar speed (attributed to Girimaji).
The FSGS model closes the difference with a power-law tail: an isotropic
Lévy-stable distribution times a constant, "addressed in the present
dynamic model". At the continuum level this gives the fractional
Laplacian above, with

$$F(s)=\frac{2^{2s}\,\Gamma\!\big(\tfrac{2s+3}2\big)\,\Gamma(2s+1)}{\pi^{3/2}\,\lvert\Gamma(-s)\rvert},$$

and $C_{\mathrm{fr}}$ proportional to $U^{2s}\mathcal T_r^{2s-1}$ (page-local: $U$ the
thermal agitation speed, $\mathcal T_r$ the relaxation time), an
up-scaling input that the dynamic procedure supplies (Eqs. 14–15).
$\nu_s$ has units of length$^{2s}$/time.

**The operator.** The fractional Laplacian is the singular integral
(Eq. 12)

$$(-\nabla^2)^s\bar u_i(\boldsymbol x)=c_{d,s}\int_{\mathbb R^d}\frac{\bar u_i(\boldsymbol x)-\bar u_i(\boldsymbol y)}{\lvert\boldsymbol x-\boldsymbol y\rvert^{d+2s}}\,d\boldsymbol y,\qquad c_{d,s}=\frac{4^s\,\Gamma(d/2+s)}{\pi^{d/2}\lvert\Gamma(-s)\rvert},$$

with $d=3$ and $c_{d,s}$ page-local. On a periodic domain its Fourier
symbol is $\lvert\boldsymbol k\rvert^{2s}$ (Eq. 13, citing Lischke et al.),
and the authors evaluate it that way in their pseudo-spectral solver.
$s=1$ recovers the integer Laplacian (§II.1). As $s\to1$,
$\lvert\Gamma(-s)\rvert\to\infty$, so $F(s)\to0$ and a finite $\nu_s$ needs
$C_{\mathrm{fr}}\to\infty$; in the dynamic form below only the product
$\nu_s=C_{\mathrm{fr}}F(s)$ is determined, because $Q_i$ carries the factor
$F(s)$ *(compiler check, not in the sources)*. For $s<1$ the
resolved-energy drain at wavenumber $k$ scales as $k^{2s}$ rather than
$k^2$ *(compiler check, not in the sources)*. Unlike the
[Smagorinsky model](/methods/smagorinsky-model.md), the closure does not
pass through a stress aligned with the strain: it is posed on the force,
and the dynamic coefficient can be negative.

## Dynamic procedure on forces

The [Germano identity](/methods/dynamic-procedure.md),
$L_{ij}=\mathcal T_{ij}-\hat\tau_{ij}$ with $\mathcal T_{ij}$ the
test-level subgrid stress (page-local, as on the dynamic-procedure page),
is used in divergence form, because the model is defined for the force
(Eqs. 17–19). With the model at the grid level and at the test level
($\hat\Delta=2\Delta$), and with the same coefficient at both levels
("scale invariance"),

$$\partial_jL_{ij}=C_{\mathrm{fr}}\,Q_i,\qquad Q_i=F(s)\Big[(-\nabla^2)^s\hat{\bar u}_i-\widehat{(-\nabla^2)^s\bar u_i}\Big],$$

($Q_i$ page-local; the source's $G_{ij}$ is the registry's $L_{ij}$ and
its $N_i$ is $Q_i$). Lilly's least-squares contraction gives (Eqs. 20–22)

$$C_{\mathrm{fr}}=\frac{\langle Q_i\,\partial_jL_{ij}\rangle}{\langle Q_iQ_i\rangle}.$$

The authors assume $C_{\mathrm{fr}}$ spatially uniform, though "in general a
space-time dependent tensor", and average over directions of statistical
homogeneity (citing Germano et al.) to avoid instability from a
negative coefficient held over long periods (§II.2, p. 10). For isotropic
turbulence this is a volume average *(compiler check, not in the
sources)*.

**Non-commutation.** The two terms of $Q_i$ differ because the test filter
does not commute with the fractional Laplacian, whereas it commutes with
integer-order derivatives for the homogeneous filter used. The authors show
this for $s=0.6$ with PDFs of the two orderings: coincident for
$\partial_x$, different for the fractional operator (§II.2, Fig. 1).

## Choosing the fractional order

The order $s$ is the remaining free parameter. Three routes are given
(§III.1, Eq. 23, Table I, Fig. 3), all from filtered DNS of forced
[isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
with a box filter. Let $\ell_\Delta$ (registry §11) denote the filter size
divided by twice the DNS grid spacing, the source's $\mathcal L_\delta$.

1. **Optimal correlation.** Sweep $s$ from 0 to 1 in steps of 0.01 and
   maximize the snapshot-averaged correlation, averaged over components,
   between modelled and filtered-DNS stresses. The optimum decreases with
   $\ell_\Delta$ at each $Re_\lambda$ and, at fixed $\ell_\Delta$, increases
   with $Re_\lambda$; its error bars grow at the large filters of the
   very-large-eddy range.
2. **Power law.** $s^{\mathrm{opt}}=a\,\ell_\Delta^{\,b}$ (Eq. 23) with
   $(a,b)=(1.53,-0.62)$ at $Re_\lambda=170$, $(1.39,-0.49)$ at 240 and
   $(1.08,-0.30)$ at 355, $R^2>0.98$ (Table I); interpolation in the table
   is proposed for other $Re_\lambda$. These give
   $s^{\mathrm{opt}}\approx0.65$, 0.70, 0.71 at $\ell_\Delta=4$ and about
   0.27, 0.36, 0.47 at $\ell_\Delta=16$ *(compiler check, not in the
   sources)*.
3. **Modelled-energy rule.** Since "almost all of the LES studies are
   designed to model about less than ten percent of the total kinetic
   energy", $s=0.5$ is taken as an average value for that range, for all
   $Re_\lambda$ (p. 13, Fig. 3b–d).

With the second or third route the authors call the model "totally free of
any tuning parameter including fractional-order" (p. 13). They read
$2s^{\mathrm{opt}}=1$ as the first order of the convective term from which
the closure originates (§III.2, p. 17).

## Evidence

**A priori** (§III.2, Figs. 4–7): forced isotropic turbulence at
$Re_\lambda=170$, 240 and 355 on $320^3$, $520^3$ and $1024^3$ pseudo-spectral
DNS, ten snapshots each, box filters at grid and test level.

- At $Re_\lambda=240$ and $\ell_\Delta=4$ and 8, D-FSGS correlates better
  with the filtered-DNS stress than Smagorinsky, dynamic Smagorinsky and the
  static FSGS, for all six components (Fig. 4). The correlation values are
  only plotted.
- The dynamic procedure raises the correlation substantially for the
  nonlocal model but not for the local one: "dynamic local models do not
  necessarily increase the correlation coefficient remarkably" (Fig. 4).
- Only D-FSGS and dynamic Smagorinsky produce
  [backscatter](/definitions/energy-backscatter.md). The fraction of points
  with $\Pi<0$ is 26% (filtered DNS), 20% (dynamic Smagorinsky) and 24%
  (D-FSGS) at $\ell_\Delta=4$, and 30%, 18% and 25% at $\ell_\Delta=8$
  (p. 15, Fig. 5).
- The PDFs of the subgrid force agree better with filtered DNS for D-FSGS,
  tails and peaks included (Fig. 6).
- With the power-law $s$ or $s=0.5$, D-FSGS keeps the highest correlation
  for $\ell_\Delta$ from 2 to 10, and the dynamic coefficient reduces the
  sensitivity to $s$ near 0.5 (Fig. 7).

**A posteriori** (§IV, Figs. 8–10): decaying isotropic turbulence at
$Re_\lambda=240$ ($520^3$ DNS, large-eddy turnover time about 2.7), LES
started from the filtered DNS field.

- At $\ell_\Delta=4$ the spectra are compared at two and four turnover
  times, chosen long "to address the numerical stability of models"; the
  authors call Smagorinsky "one of the most dissipative models", expect
  the no-model run to accumulate energy at high wavenumbers, and state
  that D-FSGS "should be ideally placed between" the two (Fig. 8); the
  text gives no further measure of the spectra.
- The resolved energy decays closer to filtered DNS than with dynamic
  Smagorinsky at $\ell_\Delta=4$ (LES) and more markedly at
  $\ell_\Delta=20$ (VLES), where dynamic Smagorinsky decays too fast
  (Fig. 9).
- Second-order structure functions are nearly preserved by all models;
  the Smagorinsky-based models deviate more on the third-order one (Fig. 10).

The authors see "promising potential" in filters bigger than the
conventional LES ones, which could offset the high cost of the
fractional operator (§V).

## Qualifications

- The value of $s$ used a posteriori is not stated, nor are the
  coefficients of the static Smagorinsky and static FSGS runs or the
  averaging and clipping of the dynamic Smagorinsky runs (§II, §IV).
- The fractional order is fitted to box-filtered DNS of isotropic
  turbulence at three Reynolds numbers; no other filter or flow is tested.
- §II.2 states that $C_{\mathrm{fr}}$ is spatially uniform and averaged over
  homogeneous directions, while Fig. 2 compares the dynamic Smagorinsky and
  D-FSGS coefficients "in the middle imaginary line" of the domain, as
  functions of position; the paper does not say which averaging the
  plotted values carry.
- Printed slips. The text of Eq. (11) calls the operator "of order
  $2\alpha\in(1,2]$" while the same equation states $\alpha\in(0,1]$, i.e.
  $2s\in(0,2]$; the sweep of §III.1 covers $s$ from 0 to 1, and the power
  law of Table I gives optima below 0.5 at large filters (compiler check
  above). Eqs. (19) and (21) write the
  velocity with the kinetic symbol $V$ where Eq. (16) has $\bar u$. In
  Eq. (24) the text calls $\tfrac12(\overline{u_iu_i}-\bar u_i\bar u_i)$ the
  "resolved" energy and $\tfrac12\bar u_i\bar u_i$ the "filtered" energy;
  the first is the subfilter energy $k_{\mathrm{sgs}}$ and the second the
  resolved one, and the formula of the modelled-energy percentage is not
  printed.

# Citations

- [Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md) — §I; §II.1, Eqs. (5)–(15); §II.2, Eqs. (16)–(22), Figs. 1–2; §III.1, Eqs. (23)–(24), Table I, Fig. 3; §III.2, Figs. 4–7; §IV, Figs. 8–10; §V.
