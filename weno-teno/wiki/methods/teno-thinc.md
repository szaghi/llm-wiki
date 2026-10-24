---
type: Method
title: "TENO-THINC"
description: "TENO-THINC uses TENO5 everywhere and replaces its interface flux by a tanh jump flux in cells that a parameter-free detector, built from the binary TENO stencil flags, marks as discontinuous; the page gives the original detector, Liang et al.'s improved detector and two-steepness flux, a TENO-THINC limiter for DG, the evidence and the cost."
status: established
aliases: [TENO5-THINC, hybrid TENO-THINC scheme, TENO-THINC limiter, TENO-THINC RKDG limiter]
tags: [teno, interface-capturing, low-dissipation, finite-difference, reconstruction]
timestamp: 2026-10-23T20:37:00Z
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
all flags are 1: TENO5 classifies the cell containing the jump as smooth.)*

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

## Reuse in a non-polynomial TENO (Liang & Fu 2024a)

[Liang & Fu (2024a)](/sources/liang-2024.md) (§3.3, Eqs. (33)–(36)) take Liang et
al.'s detector and jump flux unchanged into their Gaussian-RBF TENO, whose smooth
branch selects one target stencil from the TENO5 flags
([targeted ENO](/methods/targeted-eno.md), [RBF-WENO](/methods/rbf-weno.md)). They
restate the cell flag $\zeta_i$, the detector of Eq. (24) (their Eq. (34)), the
stricter sensor (their Eq. (36)) and the flux
$\hat f_{i+1/2}=f_{\mathrm m}+f_{\mathrm j}(\tanh\mathcal A+\varsigma)/(1+\varsigma\tanh\mathcal A)$
with $\mathcal A=0.91$, or $1.23$ where the stricter sensor holds, "as the same value
in" Liang et al. (2022). The printed fallback is the first-order flux $f_i$ where
$(f_{i+1}-f_i)(f_i-f_{i-1})\le10^{-15}$; the central flux for non-monotone triples is
not restated. The cell flags are those of the TENO5 classification that also drives
the stencil selection, so the detector again adds no parameter. Their evidence
(fifth order on Gaussian-pulse advection, a sharper Sod shock and contact, a
better-resolved Lax rarefaction, better double-Mach slip lines than WENO5-Z, TENO5 and TENO6) is for the combined scheme, so
the contribution of the jump flux is not separated (§4, Figs. 4–16).

## A TENO-THINC limiter for discontinuous Galerkin (Huang et al. 2025a)

[Huang et al. (2025a)](/sources/huang-2025.md) carry the pairing of a TENO and a THINC candidate into a
limiter for third-order ($\mathbb P^2$, scaled Legendre modal basis) Runge–Kutta
[discontinuous Galerkin](/methods/discontinuous-galerkin.md) methods on uniform 1D and Cartesian 2D meshes.
The selection between the two candidates is not a TENO-flag pattern but a compact
[BVD](/definitions/boundary-variation-diminishing.md) rule. Let $p_i$ denote the DG polynomial of $I_i$
(page-local).

- **Troubled cells** (§3.1, Eqs. (11)–(14)). The TENO indicator of Huang & Fu (2024) is reused: three
  Jiang–Shu-type measures of $p_{i-1},p_i,p_{i+1}$, $\gamma_k=1/(\beta_k+10^{-3})^6$, normalized, and the cell
  troubled when its own share falls below $C_T=10^{-4}$, one parameter set for every test
  ([troubled-cell indicators](/definitions/troubled-cell-indicator.md),
  [smoothness indicators](/definitions/smoothness-indicator.md)). For systems the indicator runs on each
  characteristic variable and the limiter is skipped only if all are smooth (§3.3).
- **TENO candidate** (§3.2.1, Eqs. (15)–(19)). The same measures with $\epsilon=10^{-10}$ and $C_T=10^{-5}$ flag
  the three polynomials; if all survive $p_i$ is kept, otherwise
  $p^{\mathrm{TENO}}_i=\sum_l\omega_lp_l$ with equal weights $\omega_l=\delta_l/\sum_m\delta_m$ over the survivors,
  $l\in\{i-1,i,i+1\}$: no linear weights ([targeted ENO](/methods/targeted-eno.md)).
- **THINC candidate** (§3.2.2, Eqs. (20)–(21)). The THINC face values computed from the three cell averages with
  $\beta_{\mathrm T}=1.6$ ([THINC](/methods/thinc-reconstruction.md)), first order where
  $(\bar u_{i-1}-\bar u_i)(\bar u_i-\bar u_{i+1})<10^{-15}$, define $p^{\mathrm{THINC}}_i\in\mathbb P^2$ as the unique
  quadratic with the cell integral of $p_i$ and these two face values.
- **Selection** (§3.2.3, Eqs. (22)–(24)): the candidate with the smaller total boundary variation against the
  *unlimited* neighbour traces, THINC only above a relative threshold, so the limiter uses only the three-cell
  stencil.
- **Two dimensions** (§4.2, Eqs. (26)–(36)). Direction by direction: the 1D TENO and THINC steps run on the trace
  polynomials along $y=y_j$ (resp. $x=x_i$) and rebuild only the $x$-only (resp. $y$-only) modal coefficients,
  the THINC weights being obtained by solving for the three coefficients that reproduce the THINC quadratic
  from the three trace polynomials; the mixed coefficient is always the mean of the $x$- and $y$-TENO
  combinations, never THINC, "to enhance robustness". The authors propose this as a general way of extending 1D
  limiters to 2D, against Hermite WENO limiters that "are not consistent" between 1D and 2D (§1, §4).

*Evidence* (§5; local Lax–Friedrichs flux, SSP-RK3, CFL 0.15; comparison with the simple WENO limiter of Zhong
& Shu driven by the same indicator). On smooth 1D and 2D density waves the indicator flags no cell and the errors
equal those of the unlimited scheme, $L^1$ orders 2.99–3.00 in 1D and 2.98–2.99 in 2D (Tables 1, 3); even with
the limiter forced on in every cell the 1D errors are unchanged, because the BVD rule detects no jump and the TENO
step leaves $p_i$ when all three polynomials survive (Table 2). On Sod, Lax, Woodward–Colella, Shu–Osher,
double Mach reflection, 2D Riemann configuration 7 and Rayleigh–Taylor the results are sharper and show more
small-scale structure than with the WENO limiter (visual comparison); on Shu–Osher the gain is "not as obvious as
in other cases", as for the finite-difference TENO-THINC. On the $1200\times300$ double Mach reflection 9.63% of the
cells are troubled and THINC is selected in 1.8% of the domain (Fig. 6). On Lax's problem the run takes 172.08 s
against 163.07 s with the WENO limiter (Table 4, hardware not stated), about 5.5% more *(compiler check, not in
the sources)*. The Rayleigh–Taylor solution loses its symmetry, which the authors attribute to round-off growing
under low dissipation (§5.7; [symmetry preservation](/properties/symmetry-preservation.md)). The limiter is also
recorded on [WENO limiters for DG](/methods/weno-limiter-dg.md).

## A finite-volume multiphase analogue

[Zhang et al. (2024a)](/sources/zhang-2024.md) (§1, §3.3) cite TENO-THINC and its
symmetry treatment in building a WENO–THINC hybrid for the
[five-equation model](/definitions/five-equation-model.md). Their switch is not a TENO
flag pattern but a volume-fraction test: a cell is interfacial if
$10^{-3}<\phi_{1,i}<1-10^{-3}$ and $\phi_1$ is locally monotone (Eq. (46)), and there
only $\phi_1$ and the two partial densities take THINC values
([THINC](/methods/thinc-reconstruction.md)).

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
- Huang et al. (2025a, Eq. (19)) print the 1D TENO candidate as a combination of the full neighbour
  polynomials, cell averages included, while in 2D (Eqs. (27)–(29)) only the non-constant modes are recombined
  and the mean is kept. *(Compiler check, not in the sources: as printed in 1D, the cell average of
  $p^{\mathrm{TENO}}_i$ over $I_i$ is $\sum_l\omega_l\frac1{\Delta x}\int_{I_i}p_l\,dx$, which differs from $\bar u_i$ when a
  neighbour weight is nonzero, so the 1D formula is conservative only with an unstated shift of the neighbour
  polynomials to the target mean.)* The paper does not discuss it. Its indicator integral (Eq. (11)) is printed
  over the target cell for all three polynomials, whereas Huang & Fu (2024) integrate each over its own cell; see
  [smoothness indicators](/definitions/smoothness-indicator.md).
- The 2D THINC weights of Huang et al. (2025a, Eq. (31)) are not constrained to be non-negative or to sum to one,
  and the troubled-cell flags are set direction by direction (§4.1).

# Citations

- [Takagi et al. (2022)](/sources/takagi-2022.md) — §§1–5, Eqs. (15)–(20), Tables 1–3, Figs. 2–25.
- [Fu (2023)](/sources/fu-2023.md) — §3.5, Eqs. (25)–(26), Fig. 8: review of TENO-THINC.
- [Liang et al. (2022)](/sources/liang-2022.md) — §§1–5, Eqs. (16)–(33), Tables 1–4, Figs. 2–25: improved detector, interpolation-like two-steepness flux, evidence.
- [Liang & Fu (2024a)](/sources/liang-2024.md) — §3.3, Eqs. (33)–(36); §4: detector and two-steepness flux reused in a Gaussian-RBF TENO.
- [Zhang et al. (2024a)](/sources/zhang-2024.md) — §1, §3.3, Eq. (46): volume-fraction switch of a finite-volume WENO–THINC multiphase hybrid.
- [Huang et al. (2025a)](/sources/huang-2025.md) — §1; §§3.1–3.3, Eqs. (11)–(25); §4, Eqs. (26)–(36); §5, Tables 1–4, Figs. 1–8: TENO-THINC limiter for RKDG with a compact BVD selection.
