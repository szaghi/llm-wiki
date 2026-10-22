---
type: Method
title: "THINC reconstruction"
description: "THINC reconstructs a cell's data by a hyperbolic-tangent jump profile fitted to the cell average and bounded by the neighbouring values; this page gives its finite-volume, finite-difference and normalised closed forms, the role of the steepness parameter (diffusive, nearly second order, anti-diffusive), and how it is hybridized with polynomial reconstructions."
status: established
aliases: [THINC, tangent of hyperbola for interface capturing, tanh reconstruction]
tags: [interface-capturing, reconstruction, low-dissipation, finite-volume, finite-difference]
timestamp: 2026-10-22T20:00:00Z
---

# THINC reconstruction

**THINC** (tangent of hyperbola for interface capturing, Xiao et al., as recalled
by the sources) replaces the polynomial inside a cell by a monotone
hyperbolic-tangent profile that joins the two neighbouring values and whose
position is fixed by conservation of the cell average. With steepness
$\beta_{\mathrm T}$ the profile in cell $I_i$ is

$$u^{\mathrm T}(x)=u_{\min}+\frac{u_{\max}-u_{\min}}{2}\Big[1+\xi_{\mathrm T}\tanh\Big(\beta_{\mathrm T}\Big(\frac{x-x_{i-1/2}}{\Delta x}-x^c_i\Big)\Big)\Big],$$

$u_{\min,\max}=\min,\max(\bar u_{i-1},\bar u_{i+1})$,
$\xi_{\mathrm T}=\mathrm{sgn}(\bar u_{i+1}-\bar u_{i-1})$, the jump centre $x^c_i$
(page-local) fixed by $\frac1{\Delta x}\int_{I_i}u^{\mathrm T}dx=\bar u_i$; it is
used where the data are monotone, $(\bar u_{i+1}-\bar u_i)(\bar u_i-\bar u_{i-1})>0$,
and the face value is $\bar u_i$ otherwise
([Deng (2023)](/sources/deng-2023.md), §4.6, Eqs. (4.31)–(4.32)). The profile is
bounded by the two neighbours and cannot create new extrema, so it needs no extra
limiter ([Takagi et al. (2022)](/sources/takagi-2022.md), §2.3;
[Fu (2023)](/sources/fu-2023.md), §3.5).

## Finite-difference flux form

For a conservative finite-difference scheme the same construction is applied to
the split point fluxes, which are treated as cell averages of the Shu–Osher
function $\phi$ of the [conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md) ([Takagi et al. (2022)](/sources/takagi-2022.md), §2.3,
Eqs. (15)–(17); [Fu (2023)](/sources/fu-2023.md), Eqs. (25)–(26)). With
page-local $f_{\mathrm m}=\tfrac12(f_{i-1}+f_{i+1})$, $f_{\mathrm j}=\tfrac12(f_{i+1}-f_{i-1})$,
$\varsigma=(f_i-f_{\mathrm m})/f_{\mathrm j}$ and $\mathcal T=\tanh(\beta_{\mathrm T}/2)$,
the interface flux for $\partial f/\partial u>0$ is

$$\hat f_{i+1/2}=f_{\mathrm m}+f_{\mathrm j}\,\frac{\mathcal A+\mathcal T}{1+\mathcal A\mathcal T},\qquad
\mathcal A=\frac{\mathrm{sgn}(\varsigma)}{\mathcal T}\,\frac{e^{\lvert\varsigma\rvert\beta_{\mathrm T}}-1}{e^{\lvert\varsigma\rvert\beta_{\mathrm T}}+1},$$

with the first-order fallback $\hat f_{i+1/2}=f_i$ where
$(f_{i+1}-f_i)(f_i-f_{i-1})\le10^{-15}$ (Takagi et al., Eq. (17)).
*(Compiler check, not in the sources: $\mathcal A=\tanh(\varsigma\beta_{\mathrm T}/2)/\mathcal T$,
and for $f_{i-1}=0$, $f_i=0.3$, $f_{i+1}=1$, $\beta_{\mathrm T}=1.6$ the formula
agrees to $10^{-13}$ with the value at $x_{i+1/2}$ of the tanh profile whose
average is computed by quadrature: the closed form is the exact face value.)*
Takagi et al. state that this $\mathrm{sgn}/\lvert\cdot\rvert$ form differs from
the one of Deng, Shimizu and Xiao (2019), a difference they relate to symmetry
breaking from floating-point errors (see
[symmetry preservation](/properties/symmetry-preservation.md)).

## Normalised form and the steepness parameter

On the [normalised-variable diagram](/definitions/normalised-variable-diagram.md)
THINC has the closed form

$$\tilde u_{i+1/2}=\frac{\sinh\beta_{\mathrm T}+\cosh\beta_{\mathrm T}-e^{\beta_{\mathrm T}(1-2\tilde u_i)}}{2\sinh\beta_{\mathrm T}},\quad0<\tilde u_i<1,\qquad\tilde u_{i+1/2}=\tilde u_i\ \text{otherwise}$$

([Deng (2023)](/sources/deng-2023.md), Eq. (4.33)), so it is normalisable and
scale-invariant. Deng reads the effect of $\beta_{\mathrm T}$ off the diagram
(§4.6, Fig. 8): $\beta_{\mathrm T}=1.0$ lies entirely below the third-order line
(diffusive); $\beta_{\mathrm T}=1.3$ lies above it near $\tilde u=1/2$
(anti-diffusive, "as the SuperBee TVD limiter"); $\beta_{\mathrm T}=1.1$ passes
close to the accuracy point $(1/2,3/4)$, "almost" second order. This agrees with
the earlier finding, recalled by Deng, that $\beta_{\mathrm T}<1.1$ is diffusive
and $\beta_{\mathrm T}>1.2$ compressive, and with the adaptive THINC of Deng et
al. (2018) that uses $1.1$ in smooth regions and $1.6$ at discontinuities.
*(Compiler check, not in the sources: at $\tilde u_i=1/2$ the formula reduces to
$1/(1+e^{-\beta_{\mathrm T}})$, which equals $3/4$ exactly for
$\beta_{\mathrm T}=\ln3\approx1.0986$; $\beta_{\mathrm T}=1.1$ gives 0.7503.)*

At $\beta_{\mathrm T}=1.6$, the value used by Takagi et al. and recalled as
typical by Fu (2023, §3.5), THINC's modified wavenumber has a positive imaginary
part in some ranges, i.e. anti-diffusion that "squares" smooth profiles
([Takagi et al. (2022)](/sources/takagi-2022.md), §2.3, citing Deng et al.
2018); see [numerical dissipation](/definitions/numerical-dissipation.md). Every
scheme in the sources uses THINC only where a discontinuity is detected or
selected.

## Hybrids

- **BVD**: per-cell selection between a polynomial (WENO, TENO) candidate and
  THINC by minimal interface jump; BVD-TENO5-THINC beats BVD-WENOZ-THINC (as
  recalled by Fu 2023, §3.6); see [BVD](/definitions/boundary-variation-diminishing.md).
- **TENO-THINC**: THINC where the TENO5 stencil flags show the pattern of a jump
  cell; see [TENO-THINC](/methods/teno-thinc.md).
- **Anti-dissipative design**: the behaviour of THINC above the third-order line
  is the precedent Huang et al. cite for the controlled anti-dissipation of
  LD-ROUND ([Huang et al. (2026)](/sources/huang-2026.md), §4.2; see
  [ROUND schemes](/methods/round-scheme.md)).

## Place among interface-sharpening methods

Nguyen, Phan, Duy, Kim & Park (2022, §1) list THINC twice in their review of interface capturing
for compressible multiphase flow: as an interface representation alongside level sets, front
tracking and VOF in ghost-fluid approaches, and as a sharpening technique of diffuse-interface
(five-, six- and seven-equation) models alongside level-set and VOF sharpening
([five-equation model](/definitions/five-equation-model.md),
[level-set method](/methods/level-set-method.md)). Their own model does without it: a MUSCL
reconstruction with the compressive "overbee" limiter of Chiapolino, Saurel & Nkonga on the volume
fractions keeps interfaces about three cells thick (§2.3, §3.1, Figs. 3–4), a limiter-based route to
sharp interfaces without a tanh profile ([TVD limiters](/definitions/total-variation-diminishing.md),
[multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)).

## Qualifications

- Fu (2023, Eq. (25)) and Takagi et al. (§2.3) print the conservation constraint
  without the factor $1/\Delta x$ (or with the integral meant in the local
  coordinate), and the profile of Fu (2023) has unbalanced parentheses.
- The finite-difference form applies a finite-volume construction to point fluxes
  read as cell averages of $\phi$; the sources use it this way without separate
  justification.

# Citations

- [Deng (2023)](/sources/deng-2023.md) — §4.6, Eqs. (4.31)–(4.33), Fig. 8.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §2.3, Eqs. (15)–(17).
- [Fu (2023)](/sources/fu-2023.md) — §3.5, Eqs. (25)–(26); §3.6.
- [Huang et al. (2026)](/sources/huang-2026.md) — §4.2: THINC as precedent for controlled anti-dissipation.
- [Nguyen et al. (2022)](/sources/nguyen-2022.md) — §1: THINC among interface-sharpening methods; §2.3, §3.1: limiter-based alternative.
