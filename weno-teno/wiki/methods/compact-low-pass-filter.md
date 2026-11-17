---
type: Method
title: "Compact low-pass filter"
description: "Tridiagonal Padé-type low-pass filters of Lele and Visbal–Gaitonde, a one-parameter family whose transfer function is 1 at zero wavenumber and 0 at the grid cutoff, given at sixth and eighth order; used to stabilize central schemes on curvilinear meshes, inside artificial-diffusivity shock capturing, as an energy probe of quasi-spectral viscosity and in reference DNS, at the price of energy drained at the highest resolved wavenumbers."
status: established
aliases: [Padé filter, compact filter, implicit filter, Visbal–Gaitonde filter, selective filter]
tags: [finite-difference, compact-scheme, solution-filtering, low-dissipation, turbulence]
timestamp: 2026-11-17T08:43:42Z
---

# Compact low-pass filter

A compact (Padé-type) low-pass filter replaces a grid function $f$ by the filtered field
$\tilde f$ (registry §10; not the normalized variables of §4) that solves a
tridiagonal system along each grid line,

$$\alpha_{\mathrm P}\tilde f_{i-1}+\tilde f_i+\alpha_{\mathrm P}\tilde f_{i+1}=\sum_{m=0}^{n_{\mathrm f}}\frac{a_m}2\big(f_{i+m}+f_{i-m}\big),$$

so that the $m=0$ term contributes $a_0f_i$. The free parameter $\alpha_{\mathrm P}$, the
right-hand-side coefficients $a_m$ and the half-width $n_{\mathrm f}$ are those of registry §10, as on
[quasi-spectral viscosity](/methods/quasi-spectral-viscosity.md). The $a_m$ are functions of
$\alpha_{\mathrm P}$ "constrained ... through Taylor- and Fourier-series analyses so as to achieve
high-order accuracy and selectively damp the Fourier modes with the highest wavenumbers
supported on the computational mesh" ([Pirozzoli (2011b)](/sources/pirozzoli-2011-b.md),
§3, Eq. (34); [Pirozzoli (2011a)](/sources/pirozzoli-2011.md), §2.2, Eq. (17)). The review
credits the high-order filters to Lele (1992) and their use on stretched, curvilinear and
deforming meshes to Visbal & Gaitonde (1999, 2002). With the reduced wavenumber
$\vartheta=k_w\Delta x$ the transfer function is

$$\hat G_{\mathrm P}(\vartheta)=\frac{a_0+\sum_{m=1}^{n_{\mathrm f}}a_m\cos(m\vartheta)}{1+2\alpha_{\mathrm P}\cos\vartheta},$$

with $\hat G_{\mathrm P}(0)=1$ (consistency) and $\hat G_{\mathrm P}(\pi)=0$ (the grid cutoff is
removed). A larger $\alpha_{\mathrm P}$ gives a weaker, more selective filter: Pirozzoli (2011b, §3)
takes $\alpha_{\mathrm P}=0.495$, "which yields a minimum amount of artificial damping", and
Sousa & Scalo (2022, §5.1) call $\alpha_{\mathrm P}>0.495$ "a lower degree of filtering". The
leading error term below is proportional to $1-2\alpha_{\mathrm P}$, and at
$\alpha_{\mathrm P}=\tfrac12$ the members below reduce to the identity *(compiler check, not in
the sources)*. The filter is applied in every coordinate direction, usually once per time
step.

## Members

- **Sixth order** ($n_{\mathrm f}=3$; Lele, as recalled by
  [Sousa & Scalo (2022)](/sources/sousa-2022.md), Eqs. (20)–(22), with
  $\alpha_{\mathrm P}\in(0,\tfrac12)$):
  $a_0=\frac{11+10\alpha_{\mathrm P}}{16}$, $a_1=\frac{15+34\alpha_{\mathrm P}}{32}$,
  $a_2=\frac{-3+6\alpha_{\mathrm P}}{16}$, $a_3=\frac{1-2\alpha_{\mathrm P}}{32}$.
- **Eighth order** ($n_{\mathrm f}=4$; Pirozzoli (2011b), §3, after Visbal & Gaitonde):
  $a_0=\frac{93+70\alpha_{\mathrm P}}{128}$, $a_1=\frac{7+18\alpha_{\mathrm P}}{16}$,
  $a_2=\frac{-7+14\alpha_{\mathrm P}}{32}$, $a_3=\frac{1-2\alpha_{\mathrm P}}{16}$,
  $a_4=\frac{-1+2\alpha_{\mathrm P}}{128}$.
- **Explicit filters** ($\alpha_{\mathrm P}=0$). Bogey & Bailly's optimized selective filters
  have the same right-hand side with $n_{\mathrm f}=4,5,6$; the authors also proposed selective
  filtering as a model of the subgrid scales in place of an eddy viscosity (as recalled by
  Pirozzoli (2011a), §2.2).

*(Compiler check, not in the sources: for both members $\hat G_{\mathrm P}(0)=1$ and
$\hat G_{\mathrm P}(\pi)=0$ for every $\alpha_{\mathrm P}$, and
$1-\hat G_{\mathrm P}=\frac{1-2\alpha_{\mathrm P}}{64(1+2\alpha_{\mathrm P})}\vartheta^6+O(\vartheta^8)$ (sixth order),
$\frac{1-2\alpha_{\mathrm P}}{256(1+2\alpha_{\mathrm P})}\vartheta^8+O(\vartheta^{10})$ (eighth order). At
$\alpha_{\mathrm P}=0.495$ the eighth-order filter has $\hat G_{\mathrm P}=0.9994$ at $\vartheta=\pi/2$,
$0.845$ at $0.9\pi$ and $0.560$ at $0.95\pi$; symbolic check.)*

## Uses in the sources

- **Stabilizing central differences on curvilinear meshes.** Explicit selective filtering of
  the flow variables is the usual cure for the parasitic waves that central differences
  produce on non-uniform curvilinear meshes, "at the price of adding some extra
  dissipation" (Pirozzoli (2011b), §1, after Visbal & Gaitonde). The paper applies the
  eighth-order filter at $\alpha_{\mathrm P}=0.495$, "which yields a minimum amount of artificial
  damping", to all flow variables in all directions after each fourth-order Runge–Kutta step,
  on divergence-form central differencing of orders 2 to 8 (FDFD), at about 30 % extra cost
  (§3). On a smooth wavy mesh the filter prevents the blow-up of the unfiltered scheme, but
  the kinetic energy of a weak vortex still drifts, up or down depending on the order, by up
  to about $1.5\times10^{-3}$ over three flow-throughs (relative drift $\sum_iJ_i\kappa_i$ against its initial value, read from Fig. 6a; the text says only that a drift is observed, "either an increase or a decrease ... depending upon the order"). It controls dispersive
  oscillations better than the kinetic-energy-preserving split scheme in a strong vortex and
  in an inviscid dipole collision, and over long times keeps less kinetic energy and, even
  when resolved, less enstrophy than that scheme, which the author reads as "numerical
  dissipation at the highest wavenumbers resolved" (Figs. 5, 12–13). On a mesh randomized by
  20 % of the spacing it does not prevent divergence; the stronger filtering Visbal & Gaitonde
  call for there was not tried (§3.1.2; [KEP split forms in curvilinear coordinates](/methods/curvilinear-kinetic-energy-preserving-split-forms.md)).
- **Shock capturing.** Localized artificial diffusivity is run with a low-pass filter:
  Kawai & Lele's LES of a sonic jet in supersonic crossflow uses sixth-order compact
  derivatives "coupled with eight-order low-pass filtering" (as recalled by Pirozzoli (2011a),
  §5, Fig. 7), and Sousa & Scalo's LAD reference needs an explicit Padé filter with
  $\alpha_{\mathrm P}=0.495$ on Sod, "probably due to difficulties with high-wavenumber energy
  build-up", where their quasi-spectral viscosity needs none (an optional filter at 0.499
  removes residual oscillations) (§5.1, Fig. 4;
  [localized artificial diffusivity](/methods/localized-artificial-diffusivity.md),
  [artificial viscosity](/methods/artificial-viscosity.md)). Visbal & Gaitonde (2005) and
  Bogey et al. (2009) capture shocks by locally decreasing the filter bandwidth (as recalled by
  Pirozzoli (2011a), §3.2).
- **Energy probe.** The residual $1-\hat G_{\mathrm P}$ of the sixth-order filter at
  $\alpha_{\mathrm P}=0.45$ estimates the energy at the grid cutoff in the quasi-spectral
  viscosity of Sousa & Scalo (2022) (§3.1; [quasi-spectral viscosity](/methods/quasi-spectral-viscosity.md)).
- **Reference DNS.** [Shima et al. (2021)](/sources/shima-2021.md) compare their
  non-dissipative [KEEP-PE scheme](/methods/keep-scheme.md) on a supersonic turbulent boundary
  layer with a DNS run with sixth-order compact differences and "an eighth-order filtering
  (numerical dissipation)" (Appendix, Fig. 3).

## Qualifications

- **Energy draining.** "As for upwinding, filtering can eliminate spurious instabilities, but
  it implies artificial energy draining that adds to the physical energy draining caused by
  molecular viscosity" (Pirozzoli (2011a), §2.2). In LES the filter can mask the dissipation
  of the subgrid model, but on non-smooth or severely skewed meshes "judicious use of
  filtering is still necessary" (Pirozzoli (2011b), §4).
- **Parameter range.** Sousa & Scalo state $\alpha_{\mathrm P}\in(0,\tfrac12)$; Pirozzoli (2011b)
  gives no range. The denominator of $\hat G_{\mathrm P}$ stays positive for
  $\lvert\alpha_{\mathrm P}\rvert<\tfrac12$ *(compiler check, not in the sources)*.

# Citations

- [Pirozzoli (2011b)](/sources/pirozzoli-2011-b.md) — §1, §3 Eq. (34), §3.1 Figs. 5–6, 9, §3.2 Figs. 12–13, §4.
- [Pirozzoli (2011a)](/sources/pirozzoli-2011.md) — §2.2 Eq. (17), §3.2, §5 Fig. 7.
- [Sousa & Scalo (2022)](/sources/sousa-2022.md) — §3.1 Eqs. (20)–(22), §5.1 Fig. 4.
- [Shima et al. (2021)](/sources/shima-2021.md) — Appendix, Fig. 3.
