---
type: Method
title: "TENO-THINC"
description: "TENO-THINC is a finite-difference hybrid that uses TENO5 everywhere and replaces its interface flux by the THINC jump reconstruction in cells that a parameter-free detector, built only from the binary TENO stencil flags, identifies as containing a discontinuity; this page gives the detector, the switching rule, the evidence and the cost."
status: established
aliases: [TENO5-THINC, hybrid TENO-THINC scheme]
tags: [teno, interface-capturing, low-dissipation, finite-difference, reconstruction]
timestamp: 2026-10-21T12:00:00Z
---

# TENO-THINC

**TENO-THINC** ([Takagi et al. (2022)](/sources/takagi-2022.md)) is a hybrid
reconstruction for the conservative finite-difference scheme on split point
fluxes: fifth-order [TENO](/methods/targeted-eno.md) (TENO5, $q=6$,
$C_T=10^{-5}$, $\epsilon=10^{-40}$) is used everywhere, and in cells detected to
contain a genuine discontinuity its interface flux is replaced by the
non-polynomial [THINC](/methods/thinc-reconstruction.md) flux with steepness
$\beta_{\mathrm T}=1.6$. The motivation (§1, §2.3): TENO restores the spectral
properties of its linear scheme up to intermediate wavenumbers, but near
discontinuities its stencil selection is dissipative and smears contacts; THINC
represents a jump inside a cell with little dissipation, but is anti-diffusive on
smooth scales (positive imaginary part of the modified wavenumber in some ranges),
so it must be confined to discontinuities. [Fu (2023)](/sources/fu-2023.md)
(§3.5, Eqs. (25)–(26), Fig. 8) reviews the scheme: optimal linear scheme where all
$\delta_k=1$, THINC where the $\delta_k$ pattern matches a "target profile" of a
genuine discontinuity.

## The detector

The detector uses only the flags $\delta_{k,i}$ that TENO5 already computes for
the reconstruction at $x_{i+1/2}$ (TENO labelling: $S_0$ central, $S_1$
downwind-biased, $S_2$ upwind-biased).

**Model step** (§3.1, Eq. (18), Table 1): for $f_i=0$ ($i<5$), $0.5$ ($i=5$),
$1$ ($i>5$), TENO5 gives

| $i$ | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|
| $\delta_0$ | 1 | 1 | 0 | 1 | 0 | 1 | 1 |
| $\delta_1$ | 1 | 0 | 0 | 1 | 1 | 1 | 1 |
| $\delta_2$ | 1 | 1 | 1 | 1 | 0 | 0 | 1 |

so the jump cell has $\delta_{1,i}=\delta_{2,i}=1$ while $\delta_{1,i-1}=0$ and
$\delta_{2,i+1}=0$. *(Compiler check, not in the sources: at $i=5$ the outer
stencils give $\beta_1=\beta_2=5/6$, so $\tau_5=0$, $\gamma_k=1$, $\chi_k=1/3$ and
all flags are 1: the cell containing the jump looks smooth to TENO5.)*

**Cell flag** (Eq. (19), page-local $\zeta_i$):

$$\zeta_i=\begin{cases}2,&\delta_{2,i}=0\ \text{and}\ \delta_{1,i}=0\quad(\text{discontinuities on both sides}),\\
1,&\text{else if }\delta_{1,i}=0,\ \delta_{2,i}=1\quad(\text{discontinuity on the right}),\\
-1,&\text{else if }\delta_{2,i}=0,\ \delta_{1,i}=1\quad(\text{discontinuity on the left}),\\
0,&\text{otherwise (smooth, or the jump cell itself).}\end{cases}$$

$\delta_0$ is not used.

**Detection rule** (Eq. (20)): cell $i$ contains a discontinuity iff $\zeta_i=0$,
some $\zeta_{i-3},\zeta_{i-2},\zeta_{i-1}\in\{1,2\}$ and some
$\zeta_{i+1},\zeta_{i+2},\zeta_{i+3}\in\{-1,2\}$. The three-cell reach on each side
accommodates slightly smeared discontinuities.

**Switch** (§3.1): in a detected cell the TENO flux $\hat f_{i+1/2}$ is replaced
by the THINC flux, or by the first-order $\hat f_{i+1/2}=f_i$ where
$(f_{i+1}-f_i)(f_i-f_{i-1})\le10^{-15}$ (non-monotone data); the procedure is
mirrored for the negative split flux and applied per characteristic field (§4.11).

**Regimes** (§3.2, stated): smooth low-wavenumber data give all $\delta_k=1$ and
the linear upwind-5 scheme; under-resolved fluctuations "mainly" give TENO's
nonlinear adaptation; only discontinuity patterns trigger THINC. The detector adds
no parameter to those of TENO5. Unlike classical hybrids, which switch to the
linear scheme for efficiency, this one switches *from* TENO to THINC for
resolution. Takagi et al. present it as an alternative to the
[BVD](/definitions/boundary-variation-diminishing.md) selection.

## Evidence

All runs use characteristic-wise reconstruction with Roe eigenvectors, Rusanov
splitting (Roe with entropy fix in some cases), SSP-RK3 at CFL 0.4 and the
symmetry-preserving implementation of Fleischmann et al.
([Takagi et al. (2022)](/sources/takagi-2022.md), §4):

- Gaussian-pulse advection: fifth order, $L_\infty$ errors identical to the
  linear upwind-5 scheme from $\Delta x=0.01$ ($4.63\times10^{-3}$) to $\Delta x=0.000625$
  ($5.24\times10^{-9}$), so neither TENO adaptation nor THINC activates (Table 2).
- Jiang–Shu multi-wave advection to $t=200$ ($N_x=200$) and $t=2000$ ($N_x=400$):
  markedly better square wave than WENO5-Z and TENO5.
- Sod, Lax, Shu–Osher, blast waves: contacts sharper; on the blast wave
  ($N_x=400$, CFL 0.35) the contact is resolved "significantly better", and on
  refinement to $N_x=3200$, $C_T=10^{-4}$ converges monotonically while the default
  $10^{-5}$ leaves a small overshoot at the strong contact (Figs. 8–9).
- Double Mach reflection: at $512\times128$ similar to WENO5-Z at $1024\times256$;
  insensitive to CFL (0.4, 0.6) and to $\epsilon\in\{10^{-8},10^{-12},10^{-40}\}$.
- Rayleigh–Taylor, 2D Riemann configurations 3 and 12 at $1024^2$, Mach 80 and
  2000 jets (with the Hu–Adams–Shu positivity-preserving flux limiter), inviscid
  Taylor–Green vortex at $64^3$ (better kinetic-energy preservation, larger
  enstrophy growth): more small-scale structure than WENO5-Z and TENO5, symmetry
  preserved.
- Activation maps show THINC triggered mainly near genuine discontinuities
  (Figs. 22–25). Fu (2023, Fig. 8) reproduces sharper shear-layer instabilities
  in double Mach reflection than WENO5-Z, TENO5 and TENO6 at $512\times128$
  (a reproduction of Takagi et al.'s Fig. 10, whose caption carries the same
  slip $t=2.0$).

**Cost** per time step on double Mach reflection (Table 3, hardware not stated):
WENO5-Z 696 / 2802 ms, TENO5 810 / 3255 ms, TENO-THINC 946 / 3810 ms, TENO6
867 / 3330 ms at $512\times128$ / $1024\times256$: TENO-THINC is 16.8% (17.1%)
more expensive than TENO5.

## Qualifications

- "Restores the spectral properties of the linear scheme exactly" is argued from
  the TENO weighting and the Gaussian test, not shown by a spectral analysis of
  the hybrid; THINC may activate in under-resolved smooth regions, which the paper
  qualifies only with "mainly".
- "Parameter-free" holds for the detector; $\beta_{\mathrm T}=1.6$, the three-cell
  reach and the $10^{-15}$ monotonicity threshold are fixed design choices, and
  $C_T$ affects contact overshoots (Fig. 9).
- The finite-volume claim, "straightforward to be deployed in a finite-volume
  solver without any modification", is not tested (§5); so is the claim that the
  results are "among the best in the literature".
- Printed slips: Fig. 10 caption gives $t=2.0$ for double Mach reflection (text
  $t=0.2$); the Shu–Osher domain is printed $[0,10]$ with data on $[-5,5]$; the
  six-point TENO6 comparator is not defined.

# Citations

- [Takagi et al. (2022)](/sources/takagi-2022.md) — §§1–5, Eqs. (15)–(20), Tables 1–3, Figs. 2–25.
- [Fu (2023)](/sources/fu-2023.md) — §3.5, Eqs. (25)–(26), Fig. 8: review of TENO-THINC.
