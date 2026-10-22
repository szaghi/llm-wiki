---
type: Method
title: "TENO-THINC"
description: "TENO-THINC is a finite-difference hybrid that uses TENO5 everywhere and replaces its interface flux by a tanh jump flux in cells that a parameter-free detector, built only from the binary TENO stencil flags, marks as discontinuous; the page gives the original detector and THINC switch, Liang et al.'s improved detector and two-steepness flux, the evidence and the cost."
status: established
aliases: [TENO5-THINC, hybrid TENO-THINC scheme]
tags: [teno, interface-capturing, low-dissipation, finite-difference, reconstruction]
timestamp: 2026-10-23T10:00:00Z
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

([Liang et al. (2022)](/sources/liang-2022.md), §2.3, Table 1, restate the same
table, rule and cell flag, Eqs. (16)–(18)), so the jump cell has $\delta_{1,i}=\delta_{2,i}=1$ while $\delta_{1,i-1}=0$ and
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
the linear upwind-5 scheme; under-resolved fluctuations "mainly" invoke TENO's
nonlinear adaptation; discontinuities that match the pattern of Eqs. (19)–(20) are
handed to THINC. The detector adds
no parameter to those of TENO5. Unlike classical hybrids, which switch to the
linear scheme for efficiency, this one switches *from* TENO to THINC for
resolution. Takagi et al. present it as an alternative to the
[BVD](/definitions/boundary-variation-diminishing.md) selection.

## Improved detector and interpolation-like jump flux (Liang et al. 2022)

[Liang, Xiao, Shyy & Fu (2022)](/sources/liang-2022.md) keep TENO5 ($C=1$, $q=6$,
$\epsilon=10^{-40}$, $\tau_5=\lvert\beta_1-\beta_2\rvert$, $C_T=10^{-5}$) and the
cell flag $\zeta_i$, and change both the detector and the flux used in detected
cells. The resulting scheme has no name in the paper ("the present scheme").

**Two deficits named** (§1, §3.1–3.2): the detector above "is insufficient to
capture all sharp discontinuities" and "more likely to misclassify the high
wavenumber fluctuations due to the excessive use of downwind stencil points";
and THINC, through its cell-average constraint, "still remains a large numerical
dissipation" at the jump for some sub-cell positions of the step (Fig. 6, cases
(c)–(e)). The first deficit is shown on steps that sit on the interface
$x_{i+1/2}$ rather than in a cell: for $f_i=0$ ($i\le5$), $1$ ($i>5$), and for
the variants with $f_5=0.1$ or $0.9$, TENO5 gives $\delta_{1,5}=0$,
$\delta_{2,5}=1$, hence $\zeta_5=1$, and the rule, which needs $\zeta_i=0$,
fails (Eqs. (22)–(23), Tables 2–3); static tests on composite functions show
"lots of misjudgments" of the original detector (Figs. 3–5).

**Improved detector** (Eq. (24)): cell $i$ is flagged iff condition I or II holds,

- I: some $\zeta_{i-3},\zeta_{i-2},\zeta_{i-1}\in\{1,2\}$, $\zeta_i=0$, and some
  $\zeta_{i+1},\zeta_{i+2}\in\{-1,2\}$ (the original rule without $\zeta_{i+3}$);
- II: some $\zeta_{i-2},\zeta_{i-1}\in\{1,2\}$, $\zeta_i=1$ and $\zeta_{i+1}=-1$,
  and $\zeta_{i+2}\in\{-1,2\}$ (a step at the interface).

It adds no parameter and uses only the flags TENO already computes. On
$\sin(10\pi x)$ and $\sin(24\pi x)$ with $N_x=120$ on $[0,2]$ (about 12 and 5
points per wavelength) neither detector fires (Fig. 2). A stricter "very steep"
sensor, Eq. (32), replaces "some" by "all" among the neighbour flags and drops
$\zeta_{i-3}$.

**Interpolation-like flux** (§3.2, Eqs. (25)–(33)). In flagged cells the flux is
not a reconstruction under a cell-average constraint but a tanh curve through
$f_{i-1}$, $f_i$, $f_{i+1}$ in a local coordinate with $x_{i\pm1}=\pm2.5$ (chosen
because $\tanh2.5=0.98661$), shifted so that it passes through $f_i$ at the
centre, i.e. fixed by *point* interpolation:

$$\hat f_{i+1/2}=f_{\mathrm m}+f_{\mathrm j}\,\frac{\tanh\mathcal A+\varsigma}{1+\varsigma\tanh\mathcal A},\qquad
\varsigma=\frac{f_i-f_{\mathrm m}}{f_{\mathrm j}},$$

with the page-local $f_{\mathrm m}=\tfrac12(f_{i-1}+f_{i+1})$,
$f_{\mathrm j}=\tfrac12(f_{i+1}-f_{i-1})$, $\varsigma$ of
[THINC](/methods/thinc-reconstruction.md), and the steepness $\mathcal A=0.91$
where Eq. (24) holds, $\mathcal A=1.23$ where Eq. (32) also holds (here
$\mathcal A$ is Liang et al.'s steepness, not the THINC quantity of that page).
*(Compiler check, not in the sources: eliminating the shift from the
centre-interpolation condition with the tanh addition formula gives this form;
it agrees numerically with the direct evaluation of the shifted curve at
$x_{i+1/2}=1.25$. For $f_{i-1}=0$, $f_i=0.5$, $f_{i+1}=1$ the flux is $0.8606$
($\mathcal A=0.91$) or $0.9213$ ($\mathcal A=1.23$), against $0.8320$ for THINC
with $\beta_{\mathrm T}=1.6$.)* Because $\lvert\tanh\rvert<1$ the flux lies between
$f_{i-1}$ and $f_{i+1}$ and needs no further limiter (§3.2). Non-monotone triples,
$\lvert f_i-f_{i-1}\rvert>\lvert f_{i+1}-f_{i-1}\rvert$ or
$\lvert f_{i+1}-f_i\rvert>\lvert f_{i+1}-f_{i-1}\rvert$, take the central flux
$\tfrac12(f_i+f_{i+1})$ (Eqs. (25)–(26)); where
$(f_{i+1}-f_i)(f_i-f_{i-1})\le10^{-15}$ the first-order flux $f_i$ is used
(Eq. (33)). The procedure is mirrored for the negative split flux.

**Evidence** (§4; finite differences with Roe-average characteristic decomposition,
Rusanov splitting, SSP-RK3 at CFL 0.4, the symmetry-preserving techniques of
Fleischmann et al. and Wakimura et al.): fifth order with errors identical to the linear scheme on
Gaussian-pulse advection ($N_x=80$–$1280$, $L_\infty$ orders 4.83–5.00, Table 4), so
neither the TENO nonlinearity nor the jump flux activates on smooth data; sharper
shocks and contacts on Sod and Lax; a slightly better blast-wave peak (where TENO5
needs $C_T=10^{-4}$ to run); on double Mach reflection at $360\times90$,
$512\times128$ and $1024\times256$ results "significantly better" than WENO5-Z,
TENO5 and TENO-THINC "and even better than" TENO6 and TENO8, with the small
disturbances near the oblique shock of TENO-THINC suppressed and little sensitivity
to CFL 0.2–0.6; more structure on Riemann configurations 3 and 7, shock–vortex
interaction, the triple-point, implosion and Rayleigh–Taylor problems (symmetric),
and stable Mach 80 and 2000 jets with the Hu–Adams–Shu positivity-preserving flux
limiter (Figs. 7–25). No timing is reported.

## Evidence for the original TENO-THINC

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
- Activation maps show THINC "generally activated near the discontinuities"
  (§4.11, Figs. 22–25). Fu (2023, Fig. 8) reproduces sharper shear-layer instabilities
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
  the hybrid; for under-resolved smooth regions the paper says only that they
  "mainly" invoke TENO (§3.2), so THINC activation there is not excluded.
- "Parameter-free" holds for the detector; $\beta_{\mathrm T}=1.6$, the three-cell
  reach and the $10^{-15}$ monotonicity threshold are fixed design choices, and
  $C_T$ affects contact overshoots (Fig. 9).
- The finite-volume claim, "straightforward to be deployed in a finite-volume
  solver without any modification", is not tested (§5); so is the claim that the
  results are "among the best in the literature".
- Printed slips: Fig. 10 caption gives $t=2.0$ for double Mach reflection (text
  $t=0.2$); the Shu–Osher domain is printed $[0,10]$ with data on $[-5,5]$; the
  six-point TENO6 comparator is not defined.
- Liang et al. call the original detector "insufficient to capture all sharp
  discontinuities" and prone to misclassify high-wavenumber fluctuations, and show
  this on static functions (Figs. 3–5), not in flow runs. Takagi et al. claim no
  more than that under-resolved fluctuations "mainly" invoke TENO (§3.2) and that
  THINC is "generally activated near the discontinuities" (§4.11); they make no
  claim about steps located at an interface. Neither paper reports a result that
  the other's evidence refutes, so no contradiction is recorded.
- In Liang et al.'s scheme the interface value is fixed by point interpolation at
  the cell centre, which departs from the finite-difference reconstruction of the
  Shu–Osher primitive function (the paper calls it "interpolation-like" and says it
  replaces the reconstruction); its fifth order in smooth regions rests on the
  detector never firing there (Fig. 2, Table 4).
- Read literally, Liang et al.'s Eq. (33) says that none of the formulas of the
  section is used where $(f_{i+1}-f_i)(f_i-f_{i-1})\le10^{-15}$; every non-monotone
  triple of Eq. (25) has a negative product, so the central flux of Eq. (26) would
  never be used. The printed precedence of the two rules is ambiguous.
- Liang et al. print the double-Mach final time as $t=0.2$ in the text and $t=2.0$
  in the captions of Figs. 11–14, the same slip as Takagi et al.'s Fig. 10; their
  implosion is run in a "periodic box". Their claims to "substantially outperform
  all other schemes in the literature" on double Mach reflection and to give "a
  state-of-the-art reference" rest on visual comparison of contours.
- Liang et al. do not state how the detector, designed for $\partial f/\partial u>0$
  and its mirror, is applied per characteristic field.

# Citations

- [Takagi et al. (2022)](/sources/takagi-2022.md) — §§1–5, Eqs. (15)–(20), Tables 1–3, Figs. 2–25.
- [Fu (2023)](/sources/fu-2023.md) — §3.5, Eqs. (25)–(26), Fig. 8: review of TENO-THINC.
- [Liang et al. (2022)](/sources/liang-2022.md) — §§1–5, Eqs. (16)–(33), Tables 1–4, Figs. 2–25: improved detector, interpolation-like two-steepness flux, evidence.
