---
type: Definition
title: "Numerical dissipation and anti-dissipation"
description: "Numerical dissipation is the part of a scheme's error that damps resolved content, anti-dissipation the part that amplifies or steepens it; this page fixes the three ways the chunk-1 sources measure and control it (flux viscosity term, leading truncation error on the normalised-variable diagram, imaginary part of the modified wavenumber) and the design levers they use."
status: established
aliases: [numerical diffusion, numerical viscosity, anti-diffusion, negative dissipation, ND]
tags: [low-dissipation, numerical-flux, reconstruction, central-scheme]
timestamp: 2026-10-21T12:00:00Z
---

# Numerical dissipation and anti-dissipation

**Numerical dissipation** (numerical diffusion, ND) is the part of the
discretization error that acts like a diffusion term, damping resolved
gradients and Fourier modes; **anti-dissipation** (anti-diffusion, negative
dissipation) is error of the opposite sign, which steepens profiles and amplifies
modes. Shock capturing needs some dissipation at discontinuities; the
low-dissipation literature of this bundle tries to remove it everywhere else.
The chunk-1 sources measure it in three compatible ways, each tied to a
different object.

## 1. The viscosity term of the numerical flux

A two-point flux can be written as a central part plus a dissipation term. For
the Riemann-solver fluxes this is the unified form
$\hat f_{i+1/2}=\tfrac12\big(f(u^-_{i+1/2})+f(u^+_{i+1/2})\big)-\tfrac12\lvert\tilde a_{i+1/2}\rvert[\![u]\!]_{i+1/2}$,
with an averaged signal speed $\tilde a$ fixed by the solver
([Fu (2023)](/sources/fu-2023.md), §3.6, Eq. (29)); the
[local Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md) $h^{\mathrm{LF}}$
is the case $\tilde a=a$. The dissipation is the product of a speed and the
interface jump, so it can be reduced by smaller speed estimates or by smaller
jumps.

- **Smaller jumps** is the logic of [BVD](/definitions/boundary-variation-diminishing.md)
  and of sharper reconstructions such as [THINC](/methods/thinc-reconstruction.md).
- **Smaller speeds.** The [central-upwind flux](/methods/central-upwind-scheme.md)
  uses the one-sided speeds $a^\pm_{i+1/2}$; it "in general" carries more ND than
  upwind fluxes but needs no Riemann solver
  ([Wang et al. (2023)](/sources/wang-2023-b.md), §1). Wang et al. reduce ND by
  tightening $a^\pm$ with regularized discrete Rankine–Hugoniot speeds, by
  replacing them in smooth regions (relative interface jump $\le\Delta x^2$) by
  symmetric speeds built from the fluid velocity and capped by $0.1$ of the
  acoustic estimate, and in 2D by a dissipation switch that scales the sound-speed
  part of $a^\pm$ by the ratio of internal-plus-normal-kinetic-energy jumps to the
  total, which damps it at contacts and shear layers (§3, Eqs. (6)–(18); see
  [adaptive-diffusion CURH flux](/methods/adaptive-diffusion-central-upwind-flux.md)).
  The CURH flux they start from already subtracts a minmod "anti-diffusion"
  correction $\delta U$ from the jump (§3, Eq. (5)): here "anti-diffusion" means a
  reduction of the diffusion term, not a negative one.
- **Field-wise speeds.** [Chertock et al. (2023)](/sources/chertock-2023.md)
  (§3, Eqs. (3.1)–(3.8)) rewrite the central-upwind flux as a central average plus
  a diffusion term $D_{i+1/2}$ and express $D$ through the
  [characteristic decomposition](/methods/characteristic-decomposition.md) at
  $x_{i+1/2}$, with diagonal matrices whose entries are the same scalar functions
  of $a^\pm$ for every field. Replacing these entries by the same functions of the
  one-sided characteristic speeds $\lambda^\pm_l$ gives each field its own
  dissipation; for a linear system the new flux is the upwind flux
  $A^+u^-_{i+1/2}+A^-u^+_{i+1/2}$ whatever the signs of the eigenvalues
  (Lemma 3.1), whereas the original reduces to upwind only when all eigenvalues
  have one sign. See [LCD central-upwind scheme](/methods/lcd-central-upwind-scheme.md).

## 2. The leading truncation error of a reconstruction

On a three-cell compact stencil, the leading error of a second-order linear
reconstruction is $4(\tfrac13-\mu_0)(\tfrac12-\tilde u_i)u'\Delta x+O(\Delta x^3)$,
diffusive or anti-diffusive according to the sign of $(\tfrac13-\mu_0)(\tfrac12-\tilde u_i)$
([Deng (2023)](/sources/deng-2023.md), Proposition 5, Table 1; $\mu_0$ the
intercept of the operator on the
[normalised-variable diagram](/definitions/normalised-variable-diagram.md),
$\tilde u_i$ the normalised cell average). Two consequences:

- the sign depends on the data, not only on the scheme (Deng, Remark 3.1);
  symmetric TVD limiters, for example, are dissipative for $\tilde u<1/2$ and
  anti-dissipative for $\tilde u>1/2$ (§4.1);
- on the diagram, curves below the third-order line P3 are diffusive and curves
  above it anti-diffusive (§5).

Deng's low-dissipative [ROUND](/methods/round-scheme.md) operators deliberately
put parts of the curve above P3, so that positive and negative second-order
errors partly cancel over a cell (Remark 7.2), and Huang et al.'s LD-ROUND does
the same with "controlled anti-dissipation" whose amount grows with two shape
parameters; larger values "may introduce excessive anti-dissipation errors and
potentially lead to numerical instability"
([Huang et al. (2026)](/sources/huang-2026.md), §4.2).

## 3. The imaginary part of the modified wavenumber

In the [approximate dispersion relation](/definitions/approximate-dispersion-relation.md)
of a scheme, $\tilde\vartheta_i<0$ is dissipation and $\tilde\vartheta_i>0$
anti-dissipation (the sign convention of Fu 2023, used by all chunk-1 sources
cited here). Measured this way:

- THINC with $\beta_{\mathrm T}=1.6$ is anti-diffusive in some wavenumber
  ranges, like Superbee ([Takagi et al. (2022)](/sources/takagi-2022.md), §2.3);
- WENO-Z+ with a large coefficient has a narrow band of negative dissipation
  near $\vartheta\approx1.18$ ([Luo & Wu (2021)](/sources/luo-2021-b.md), §3).

**Nonlinear dissipation of WENO weights.**
[Luo & Wu (2021)](/sources/luo-2021-b.md) (§4) split the dissipation of a WENO
scheme into the linear one of its background scheme (UD5 at fifth order) and a
nonlinear one due to the weights: when the least smooth candidate stencil gets
less than its linear weight, $\omega_D<d_D$, the weighting adds positive
dissipation, so classical WENO is always more dissipative than UD5; WENO-Z+-type
weights give it more, $\omega_D>d_D$, which adds negative dissipation partly
cancelling the linear one, so their spectral curves can beat UD5's in a
wavenumber band. The argument is supported by plots of $\omega_k/d_k$ on Fourier
modes, not by a proof. TENO avoids nonlinear dissipation in smooth regions
differently, by restoring the linear weights exactly
([targeted ENO](/methods/targeted-eno.md)).

## Reading dissipation off 2D results

Without a closed-form measure, the 2D sources compare dissipation through flow
features that only dissipation suppresses: the curliness of the contact in the
explosion problem, which is physically unstable and "may be stabilized by the ND
only", and the distance travelled by the jet of the implosion problem
([Wang et al. (2023)](/sources/wang-2023-b.md), Examples 6–7); Chertock et al.
present the explosion problem as a benchmark of the amount of ND and compare at
equal CPU time on the implosion (Examples 6–7). For the Kelvin–Helmholtz
problem, where solutions do not converge under refinement,
[Chertock et al. (2023)](/sources/chertock-2023.md) (Example 8, Fig. 5.9) find
different Cesàro averages for the original and the LCD central-upwind schemes
and read this as non-uniqueness of the limiting dissipative weak solution,
which "apparently depends on the choice of the numerical diffusion".

## Qualifications

- The three measures are not interchangeable. The flux viscosity is local and
  pointwise, the truncation-error sign is a smooth-data statement, the ADR is a
  linear-advection statement on single modes; a scheme can be anti-dissipative in
  one sense and dissipative in another (Deng's symmetric limiters change sign
  with $\tilde u$).
- Visual dissipation proxies (curlier contacts, more vortices) are what most of
  the chunk-1 2D claims rest on; none of these sources quantifies them.

# Citations

- [Fu (2023)](/sources/fu-2023.md) — §3.6, Eq. (29): flux as central part plus jump term.
- [Wang et al. (2023)](/sources/wang-2023-b.md) — §1, §3, Eqs. (5)–(18), Examples 6–7: CURH speeds, ND switch, ND proxies.
- [Chertock et al. (2023)](/sources/chertock-2023.md) — §3, Lemma 3.1, Examples 6–8: field-wise diffusion, Cesàro averages.
- [Deng (2023)](/sources/deng-2023.md) — Proposition 5, Table 1, Remarks 3.1, 7.2, §§4.1, 5: sign of the leading error.
- [Huang et al. (2026)](/sources/huang-2026.md) — §4.2: controlled anti-dissipation.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §2.3: anti-diffusive THINC.
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §§3–4: negative dissipation, nonlinear dissipation of weights.
