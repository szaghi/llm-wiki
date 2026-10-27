---
type: Definition
title: "Law of the wall"
description: "The inner-layer mean-velocity profile of wall-bounded turbulence — viscous sublayer, buffer layer and logarithmic layer in wall units — with the constants, composite fits and damping functions the sources use, its compressible, displaced (canopy) and outer-layer (defect-law) extensions, and its role as the target every wall model and data-driven RANS correction must reproduce."
status: established
aliases: [logarithmic law, log law, law-of-the-wall profile, inner-layer profile]
tags: [boundary-layer, wall-model, wmles, rans]
timestamp: 2026-10-27T06:08:00Z
---

# Law of the wall

The law of the wall states that, in the inner layer of a smooth-wall turbulent
flow in equilibrium, the mean velocity scaled by the friction velocity is a
universal function of the wall distance in viscous units,
$u^+=f(y^+)$, with $u^+=\langle u\rangle/u_\tau$, $y^+=y/\delta_\nu$,
$u_\tau=\sqrt{\tau_w/\rho_w}$ and $\delta_\nu=\nu_w/u_\tau$ (let $f$ denote this
universal profile, page-local). Its two asymptotes are the viscous sublayer,
$u^+=y^+$, and the logarithmic layer,

$$u^+=\frac1\kappa\ln y^++B ,$$

joined through a buffer layer. Every wall model of this bundle is a way of
inverting $f$ (or an ODE whose solution is $f$) to obtain $\tau_w$ from a
velocity sampled away from the wall; see the
[equilibrium wall model](/methods/equilibrium-wall-model.md) and
[wall-modelled LES](/methods/wall-modelled-les.md).

## Constants used by the sources

The sources do not agree on one pair $(\kappa,B)$; each states its own values,
and the choice is part of the model.

| Source | $\kappa$ | $B$ | Other constants | Use |
|---|---|---|---|---|
| [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md), Eq. (1) | 0.41 | 5.2 | quadratic branch below $y^+=23$ | algebraic wall model in [CharLES](/software/charles.md) |
| [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md), Eq. (1) | 0.4 | 5 | | algebraic wall model in [LESGO](/software/lesgo.md); reference for log-layer mismatch |
| [Fowler et al. (2022)](/sources/fowler-2022.md), App. C | 0.4 | 4.95 | $\kappa_2=9.753$, $\beta=1.903$ (fit) | composite fit (C1); their Fig. 4 log law uses $B=5.0$ |
| [Griffin et al. (2023)](/sources/griffin-2023.md), §1 | 0.41 | — | $A^+=17$ | mixing length with van Driest damping |
| [Agrawal et al. (2022)](/sources/agrawal-2022.md), §VII.D | 0.38 (DNS value at $Re_\tau=4200$) | — | | reference slope for the log-layer error of WMLES |
| [Gillyns et al. (2022)](/sources/gillyns-2022.md), §3, Eq. (3) | 0.38 | 4.1 | Reichardt profile; Österlund et al. values, as they cite them | algebraic wall model in a spectral-element code |
| [Bae & Koumoutsakos (2022)](/sources/bae-2022.md), Eq. (3), Fig. 2 | 0.41 | 5.2 | | reference log law of the reinforcement-learning wall models |
| [Cao et al. (2022)](/sources/cao-2022.md), Eq. (8) | 0.40 | 5.5 | "for the low Reynolds number turbulent channel flow" | estimate of $u_\tau$ for a channel DNS at $Re_\tau=180$ |
| [Knopp (2022)](/sources/knopp-2022.md), §4, Eq. (26) | 0.41 | 5.0 | with Coles' wake, after Coles & Hirst | fit of boundary-layer thickness in adverse pressure gradient |
| [Cogo et al. (2022)](/sources/cogo-2022.md), Fig. 8 | 0.41 | 5.2 | | reference for transformed compressible profiles |
| [Kim et al. (2022)](/sources/kim-2022.md), Fig. 12 | 0.41 | 5.2 | | reference line for the mean velocity of LES with learned SGS models at $Re_\tau=180$–720 |
| [Dang et al. (2022)](/sources/dang-2022.md), Fig. 17 legend | $1/2.44$ | 5.1 | | reference for van Driest-transformed DNS profiles upstream of a Mach 2.9 ramp |
| [Cai et al. (2022)](/sources/cai-2022.md), Eq. (26) | not printed | $\kappa^{-1}\ln E$, $E=11.27$ | blend constants 10.71 and 1.526 | log law written $u^+=\kappa^{-1}\ln(Ey^+)$; explicit equilibrium wall model in a lattice Boltzmann solver |
| [Blind et al. (2023)](/sources/blind-2023.md), §3.3 | not printed | not printed | Spalding's law | algebraic wall model in [FLEXI](/software/flexi.md) |
| [Carlsson et al. (2023)](/sources/carlsson-2023.md), Figs. 4–5 | not printed | not printed | Reichardt's law | reference profile for IDDES of channel flow |
| [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md), §3.2, Eq. (3.1) | 0.41 | 5.2 | quadratic branch below $y^+=23$ | equilibrium baseline of the [building-block-flow wall model](/methods/building-block-flow-wall-model.md), sampled at the second grid point |
| [Lewis et al. (2023)](/sources/lewis-2023.md), §3.2.2 | not printed | not printed | linear for $y^+<11$, logarithmic above | wall law of fan-stage WMLES in AVBP |
| [Kang et al. (2023)](/sources/kang-2023.md), figures | 0.41 | 5.2 | | reference line for LES of channel flow at $Re_\tau=180$ and 395 with learned SGS models |
| [Wang et al. (2023b)](/sources/wang-2023-b.md), Eq. (10) | 0.40 | 5.5 | "for the low Reynolds number turbulent channel flow" | reference for van Driest-transformed compressible channel DNS |
| [Zhao et al. (2023a)](/sources/zhao-2023.md), Eqs. (25)–(26) | 0.40 | 5.5 | "selected for the low-Reynolds-number turbulent channel flow" | sets the viscosity of a channel at a target $Re_\tau$ |
| [Vadrot et al. (2023a)](/sources/vadrot-2023.md), §II.B.1, Eq. (1); §II.B.3 | $\approx0.4$ (0.4 in the states and figures) | $\approx5$ | | algebraic wall model and reference log law of reinforcement-learning wall models in LESGO |
| [Constant et al. (2024)](/sources/constant-2024.md), §3.2, Eq. (8) | 0.41 | not printed | Musker's law (form not printed); van Driest damping $1-e^{-y^+/19}$ in the target-point eddy viscosity | wall function at immersed-boundary target points in RANS |
| [Mozaffari et al. (2024)](/sources/mozaffari-2024.md), §2.2, Eqs. (12)–(15) | $\approx0.41$ | $\kappa^{-1}\ln E$, $E\approx7.9$ | blend constants $s=86.58$, $p=0.7894$ | explicit equilibrium wall model in a lattice Boltzmann solver |
| [Chen et al. (2024)](/sources/chen-2024.md), §2.3, Eqs. (2.7), (2.10) | 0.40 | — | $A^+=26$ divided by the square root of the local total shear stress in wall units; Johnson–King reference damping with 17 | mixing length of the algebraic [Baldwin–Lomax model](/methods/baldwin-lomax-model.md) (a RANS closure, not an LES wall model) |
| [Mukha et al. (2025)](/sources/mukha-2025.md), §III.A, App. A | 0.387 | 4.2 | Spalding's law (formula not printed); values from the channel DNS of Yamamoto & Tsuji at $Re_\tau\approx8000$, as cited | algebraic wall model of spectral-element WMLES of channel flow in [Nek5000](/software/nek5000.md) |
| Mukha et al. (2025), §IV.A; App. A | 0.41 | 5.2 (§IV.A) or 5.5 (App. A) | Spalding's law | the same model for a zero-pressure-gradient flat-plate boundary layer (see Qualifications) |
| [Lohrer & Fröhlich (2025)](/sources/lohrer-2025.md), §5.2, Eqs. (5.7)–(5.8) | 0.41 (0.38 when fitted) | 5.5 | roughness function $\Delta U^+_{\mathrm{vo}}=15.4$ (17.4 with fitted $\kappa$); $B$ after Nezu & Nakagawa (1993), as cited | displaced log law above a submerged flexible canopy (below) |
| [Oulghelou et al. (2025)](/sources/oulghelou-2025.md), Figs. 4, 11 | 0.41 | 5.2 | | reference log law for blended data-driven RANS corrections in channel and flat-plate flow |
| [Wu et al. (2025)](/sources/wu-2025.md), §2.1, Eq. (3) | 0.41 | — | | log-layer calibration constraint of the $k$-$\omega$ SST $\omega$ equation (below) |
| [Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md), §5.2.1, Eqs. (93)–(94) | 0.39 | — | $A^+=26$ in the mixing length, $\nu_t=l^2\lvert\partial u/\partial y\rvert$ | mixing-length model used to verify a high-order HDG RANS solver in channel flow; their flat-plate profile is compared with Coles' law (§5.3) |
| [Ghidoni et al. (2026)](/sources/ghidoni-2026.md), §3.3, Eqs. (12)–(13); §4 | $\sim0.41$ | 5 | power law $u^+=8.3\,(y^+)^{1/7}$ above $y^+=11.81$; Spalding's law for comparison | explicit [RANS wall function](/methods/rans-wall-function.md) in a high-order DG solver (below) |
| [Lederer et al. (2026)](/sources/lederer-2026.md), §4.2 | 0.41 | 5.2 | log layer quoted as $40<y^+<200$; constants "experimentally fitted for mild adverse pressure gradients" | reference for implicit DG LES of the transitional [Eppler 387 airfoil](/benchmarks/eppler-387-airfoil.md) |
| [Rickard & Kasbaoui (2026)](/sources/rickard-2026.md), §4.1, Eq. (4.1) | 0.41 | — | van Driest profile, $A^+=26$ | volume-filtered to model the wall slip of immersed-boundary WMLES (below) |
| [Aiello et al. (2026)](/sources/aiello-2026.md), §4.1, Fig. 1 | 0.41 | 6.0 (fitted) | in $y^*$, log region from $y^*\ge40$ | Trettel–Larsson-transformed DNS of a thermally perfect CO$_2$ channel at $Re_\tau^*=160$–190 |
| [Nuca et al. (2025)](/sources/nuca-2025.md), §V.B, Table V | 0.387 | 4.21 | "high-Re" set after Yamamoto & Tsuji, as cited; the corresponding $C$ and $A^+$ are not printed | fixed-parameter explicit approximations of the Spalding, Reichardt and ODE wall models (below) |
| Nuca et al. (2025), §V.B, Table VI | 0.4 (Spalding, Reichardt); 0.41 (ODE) | 5.5 | $C=7.8$ (Reichardt); $A^+=17$ (ODE), "essentially a standard choice" | "classical" set of the same approximations |
| Nuca et al. (2025), §V.A, Table II | 0.38–0.42 | 4.2–5.5 | $C\in[6.8,7.7]$, $A^+\in[15,19]$ | parameter ranges over which the global explicit approximations are fitted |
| [Husson et al. (2024)](/sources/husson-2024.md), §3.1, Eq. (37) | not printed ($1/0.41$ from the coefficients, see below) | 5.0334 | Allmaras–Johnson composite law, nine printed constants | wall law of RANS and zonal DES on a lattice Boltzmann immersed boundary |
| [Tomboulides et al. (2025)](/sources/tomboulides-2025.md), §3.2 | 0.41 | 5.5 | log layer quoted as $30<y^+<200$ | reference for $k$-$\tau$ RANS of pipe flow at $Re_\tau=1142$ |
| [Ghidoni & Noventa (2026)](/sources/ghidoni-2026-b.md), §IV.A, Figs. 12–13 | 0.41 | 5 | | reference profile for laminar-kinetic-energy transition RANS of the ERCOFTAC plates |
| [Vandenhoeck et al. (2022)](/sources/vandenhoeck-2022.md), §4.1, Fig. 9 | not printed | not printed | Spalding's law, as cited | reference for high-order flux-reconstruction RANS of the Wieghardt plate |
| [Huang et al. (2022b)](/sources/huang-2022-d.md), §2.4.3, Eq. (52) | not printed | not printed | Reichardt-type profile with damping lengths 11 and $1/0.33$ | manufactured boundary-layer profile for testing a high-order reconstruction |

Zhao et al. (2023a) attribute $\kappa=0.40$, $B=5.5$ to the channel DNS of
Kim et al. (1987), as they cite it; Wang et al. (2023b) give the same values
with the same wording. Zhao et al. (2023a, §5.2, Eqs. 25–26) use the law in the reverse
direction: with the centreline velocity $U_c=1$ and the target centreline
value $y_c^+=Re_\tau=180$, they set $U_c^+=2.5\ln y_c^++5.5$,
$u_\tau=U_c/U_c^+$ and the viscosity $\mu=\rho u_\tau\delta/Re_\tau$ ($\delta$ the
channel half-height, the source's $H$; $U_c$, $U_c^+$, $y_c^+$ page-local); the realized $Re_\tau$ then follows
from the simulation. Dang et al.'s slope $1/2.44$ is $\kappa\approx0.410$, and Cai et al.'s $E=11.27$
corresponds to $B=\kappa^{-1}\ln E\approx2.42/\kappa$, about 5.9 for
$\kappa=0.41$ *(compiler check, not in the sources)*.

Griffin et al. (2023, §3) test Reynolds-number-dependent constants fitted to
the incompressible channel DNS of Lee & Moser (as they cite it): at
$Re_\tau=\{182,543,1000,1990,5190\}$, $\kappa=\{0.400,0.408,0.400,0.391,0.391\}$
and $A^+=\{18.2,17.4,17.0,16.5,16.5\}$. The fitted values improve their
compressible wall model only modestly at $Re_\tau^*=190$ and not at all at
$Re_\tau^*=590$, so they keep $\kappa=0.41$, $A^+=17$. Gillyns et al. (2022,
§3) likewise note that more recent values after Lee & Moser are
$\kappa\simeq0.383$, $B\simeq4.25$, but keep 0.38 and 4.1; the effect of the
choice on $u_\tau$ is not assessed.

Vadrot et al. (2023a, §II.B.3) note that empirical values of $\kappa$ range
over 0.36–0.44 (as they cite it), which matters for their learned wall model
because its first state is built from the chosen $\kappa=0.4$ (see
[machine-learning wall models](/methods/machine-learning-wall-model.md)).
Mozaffari et al. (2024) write the log law as $u^+=\kappa^{-1}\ln(Ey^+)$, as
Cai et al. (2022) do, but with $E\approx7.9$ against 11.27 (see
Contradictions); with $\kappa=0.41$ for both (Cai et al. print no value of
$\kappa$) these correspond to $B\approx5.0$ and $B\approx5.9$
*(compiler check, not in the sources)*.

[Nuca et al. (2025)](/sources/nuca-2025.md) (§III) state that $\kappa$ and
$B$ are subject to low-Reynolds-number effects and that their high-Reynolds-number
values are "not settled upon" (as they cite it), so an approximation of a
wall model must keep them as inputs rather than freeze them; their two fixed
sets and their fitting ranges are in the table. Their high-Re intercept,
4.21, and the 4.2 of Mukha et al. (2025) are both taken from Yamamoto &
Tsuji as cited, and differ only in the printed rounding. Husson et al.
(2024, §3.1) print no $\kappa$ with their composite law; its two
logarithmic terms give the slope $2(c_1-c_2)=2.439=1/0.410$ and, with the
argument order discussed under Qualifications, the intercept $5.0334$
equals the printed additive constant ($c_1$, $c_2$ the law's constants,
page-local) *(compiler check, not in the sources)*.

Aiello et al. (2026, §4.1) attribute their large fitted intercept,
$B=6.0$, to the low transformed friction Reynolds number of their DNS
($Re_\tau^*=160$–190), consistent, they state, with low-Reynolds-number
incompressible flow and earlier supersonic channel DNS (see
[compressible velocity transformation](/definitions/compressible-velocity-transformation.md)).
Lederer et al. (2026, §4.2) take $\kappa=0.41$, $B=5.2$ as constants fitted
for mild adverse pressure gradients and compare the profiles of their
implicit LES in the turbulent part of the airfoil boundary layer, where all
runs follow $u^+=y^+$ for $y^+<5$ and differ from one another above
$y^+=10$ (Fig. 7; see
[high-order projection-based upwind method](/methods/high-order-projection-based-upwind-method.md)).

How much the constants matter is quantified by Lozano-Durán et al. (2022,
§IV.C, Eq. 12): a 10 % error in $\kappa$ or in $B$ produces about 6 % or 3 %
error in $u_\tau$, less than a 10 % error in the LES velocity at the matching
point; their fuselage WMLES errors saturate at about 2 %, which they attribute
to a 3 % deviation in $\kappa$ (§V.C). The constants therefore set an accuracy
floor of wall-modelled LES that grid refinement does not remove (details on the
[equilibrium wall model](/methods/equilibrium-wall-model.md) page). Vadrot et
al. (2023a, §III.B) quote a comparable sensitivity, after Yang et al. (2019)
as they cite it: a 2.5 % uncertainty in $\kappa$ gives about a 5 % error in
the predicted wall stress, that is about one to two wall units of
[log-layer mismatch](/definitions/log-layer-mismatch.md).

## Composite profiles across the buffer layer

A wall model sampled in the buffer layer needs a single smooth $f(y^+)$.

- **Piecewise algebraic profile** (Lozano-Durán et al. 2022, Eq. 1):
  $u^+=y^++a_1(y^+)^2$ for $y^+<23$ and the log law otherwise, with $a_1$
  fixed by $C^1$ continuity at $y^+=23$ (value not printed).
- **Smooth fit of the full-equilibrium solution** (Fowler et al. 2022, Eqs.
  C1–C2), fitted to the numerical solution of the mixing-length equilibrium
  ODE with van Driest damping:

  $$f(y^+)=\left[\frac1\kappa\ln(\kappa_2+y^+)+B\right]\left[1+\left(\frac{y^+}{\kappa_1}\right)^{-\beta}\right]^{-1/\beta},\qquad \kappa_1=\frac1\kappa\ln\kappa_2+B,$$

  with $\kappa=0.4$, $B=4.95$, $\kappa_2=9.753$, $\beta=1.903$ (here $\beta$
  is the fit exponent, page-local). The choice of $\kappa_1$ makes
  $f\to y^+$ in the viscous sublayer. The fit error is below 1 % for $y^+>5$
  and below 2.25 % for $0\le y^+\le5$. Fowler et al. reject Reichardt's (1951)
  profile, as they recall it, because its error exceeds 3 % near $y^+\sim10$.
- **Reichardt's profile** (Gillyns et al. 2022, Eq. 3, as in Frère et al.
  2017, as they cite it):

  $$u^+=\frac1\kappa\ln(1+\kappa y^+)+\left(B-\frac1\kappa\ln\kappa\right)\left(1-e^{-y^+/11}-\frac{y^+}{11}e^{-y^+/3}\right),$$

  with $\kappa=0.38$, $B=4.1$, inverted for $u_\tau$ in their equilibrium
  wall model (the source writes $C$ for $B$). Fowler et al. (2022) reject this
  profile for its error near $y^+\sim10$ (above); Gillyns et al. sample it at
  $y^+\ge63$, where the choice is not tested against an alternative.
  Nuca et al. (2025, §III, Eqs. 3, 6) print the same law with an additive
  constant $C$ and damping lengths $B_1=11$, $B_2=3$ (page-local), and derive
  $C=B-\kappa^{-1}\ln\kappa$ from the limit $y^+\to\infty$, which is the
  coefficient Gillyns et al. write; dropping the damping terms leaves
  $\kappa^{-1}\ln(1+\kappa y^+)$, the profile of the undamped equilibrium ODE
  (below). With $\kappa=0.4$, $B=5.5$ the relation gives $C=7.79$, the
  printed classical 7.8, and with the high-Re set $\kappa=0.387$, $B=4.21$ it
  gives $C=6.66$ *(compiler check, not in the sources)*.
- **Blended profile with an explicit inverse** (Cai et al. 2022, §II.C.1,
  Eqs. 24–26, after the authors' earlier work as they cite it). The forward
  profile blends the two asymptotes with hyperbolic tangents,

  $$u^+=\left[1-\tanh\frac{y^+}{10.71}\right]^{1.526}y^++\left[\tanh\frac{y^+}{10.71}\right]^{1.526}\frac1\kappa\ln(Ey^+),\qquad E=11.27,$$

  and a separately fitted inverse gives $y^+$ directly from the local Reynolds
  number $Re_y=U y/\nu$ ($U$ the wall-tangential velocity at distance $y$;
  page-local),

  $$y^+=\left[1-\tanh\frac{Re_y}{180.8}\right]^{0.789}Re_y^{1/2}+\left[\tanh\frac{Re_y}{180.8}\right]^{0.789}\frac{e^{W(\kappa ERe_y)}}{E},$$

  with $W$ the Lambert function, $W(x)=\ln\big(x/W(x)\big)$, "expanded
  explicitly into series" (series not printed), so that
  $u_\tau=y^+\nu/y$ needs no Newton iteration. Each branch of the inverse is
  the exact inverse of the matching branch of the forward profile — the
  viscous branch from $Re_y=(y^+)^2$, the log branch from
  $\kappa ERe_y=Ey^+\ln(Ey^+)$, i.e. $\ln(Ey^+)=W(\kappa ERe_y)$ — while the
  two blending functions differ, so the pair is consistent only
  asymptotically; its buffer-layer accuracy is not shown in the source
  *(compiler check, not in the sources)*. See the
  [equilibrium wall model](/methods/equilibrium-wall-model.md).
- **The same explicit inverse with other constants** (Mozaffari et al.
  2024, §2.2, Eqs. 9–15, after Cai & Sagaut as they cite it): the viscous
  branch $y^+=\sqrt{Re_y}$, the log branch $y^+=E^{-1}e^{W(\kappa ERe_y)}$ and
  the unified inverse

  $$y^+(Re_y)=\left[1-\tanh\frac{Re_y}{s}\right]^pRe_y^{1/2}+\left[\tanh\frac{Re_y}{s}\right]^p\frac{e^{W(\kappa ERe_y)}}{E},\qquad u^+=\frac{Re_y}{y^+},$$

  with $s=86.58$, $p=0.7894$, $\kappa\approx0.41$, $E\approx7.9$ ($s$, $p$
  page-local); the exponent $p$ applies to the bracketed blending functions,
  as in the form of Cai et al. (2022) above (manuscript p. 5, Eq. 15, checked
  visually). No pressure-gradient term. See Contradictions for the
  comparison with Cai et al. (2022).
- **An explicit forward law $u^+(Re_y)$, re-fitted, with buffer-layer
  corrections** (Nuca et al. 2025, §III–IV, Eqs. 5, 9–10, 24). Nuca et al.
  write "model 2" of Cai & Sagaut (2021), as they cite it, directly for
  $u^+$,

  $$u^+_{\mathrm{CS}}=\left(e^{-Re_y/s}\right)^p\sqrt{Re_y}+\frac{\left(1-e^{-Re_y/s}\right)^p}{\kappa}\,W\!\left(\kappa e^{\kappa B}Re_y\right),$$

  with exponential, not hyperbolic-tangent, blending functions, and treat
  $p$ and $s$ as free coefficients to be optimized rather than as Cai &
  Sagaut's values (for $\kappa=0.41$, $B=5.525$, Fig. 3 uses $p=1.2411$,
  $s=117.3629$; the optimization bounds of Table III span $p=1.22$–1.29,
  $s=76$–378). The log branch is the same as in the inverses above: from
  $Re_y=u^+y^+$ and $u^+=\kappa^{-1}\ln y^++B$, $\kappa u^+=W(\kappa e^{\kappa B}Re_y)$,
  and with $E=e^{\kappa B}$ this is $\ln(Ey^+)=W(\kappa ERe_y)$ of Cai et
  al. (2022) *(compiler check, not in the sources)*. Their premise is that
  Spalding's law, Reichardt's law, the van Driest equilibrium ODE and this
  explicit law coincide in the linear and logarithmic regions once their
  constants match, so only a buffer-layer perturbation $\Delta u^+$, a sum of
  one to three Gaussian bumps in $\log_{10}Re_y$, has to be fitted to turn
  the explicit law into an approximation of any of the three (§IV, Fig. 3).
  The fits, their printed accuracy (below 1 % for coefficients linear in
  $\kappa$ and in $B$, $C$ or $A^+$; below 0.05 % for fixed constants) and
  the checks of the printed coefficients are on the
  [equilibrium wall model](/methods/equilibrium-wall-model.md) page.
- **Musker's law** (Constant et al. 2024, §3.2, Eq. 6, after Musker as
  cited): an equilibrium profile fitting viscous, buffer and log layers,
  $u_A=u_\tau f(y_A^+)$ at an immersed-boundary target point $A$, with
  $u_\tau$ from Newton–Raphson at the image point and assumed constant along
  the wall normal; the formula is not printed. Their Fig. 7 compares it with
  Spalding's law and a body-fitted flat-plate RANS profile. The eddy
  viscosity at the target points is $\nu_t=\kappa u_\tau y\,[1-e^{-y^+/19}]$
  with $\kappa=0.41$ (Eq. 8), stated "valid in the log layer and down to the
  wall", and inverted for the Spalart–Allmaras variable $\tilde\nu$; the
  damping enters to the first power and with the constant 19, unlike the
  squared $A^+=17$ form of Griffin et al. (2023).
- **Linear/log switch** (Lewis et al. 2023, §3.2.2, after Schmitt et
  al. as cited): a linear law $u^+=y^+$ for $y^+<11$ and a logarithmic law
  otherwise; the constants are not printed.
- **Spalding's law** is the algebraic wall model of Blind et al. (2023,
  §3.3), solved by Newton's method in every Runge–Kutta stage; the formula
  and its constants are not printed. Mukha et al. (2025, §II.C.1) use it in
  the same role in a continuous spectral-element code and, without printing
  the formula, measure its accuracy against reference profiles (App. A,
  Figs. 18–21). In channel flow at $Re_\tau\approx8000$, with the constants
  $\kappa=0.387$, $B=4.2$ taken from the same DNS, the law reproduces the
  DNS velocity in the log region within 0.2 %, and the wall stress it
  returns from the exact DNS velocity is within $\pm0.2$ % for matching
  heights $0.05\le h_{\mathrm{wm}}/\delta\lesssim0.25$ ($-0.04$ % at
  $h_{\mathrm{wm}}=0.2\delta$ in §III.B.3, "about 0.05 %" in App. A). With
  $\kappa=0.41$ and reference flat-plate profiles the stress error
  is about $\pm1$ %, an order of magnitude larger; the law reaches its
  logarithmic limit only near $y^+\approx150$, which at low Reynolds numbers
  lies near the wake region, and where the error crosses zero depends on
  whether wall-resolved LES or DNS supplies the reference profile (App. A,
  Figs. 20–21). Constant et al. (2024, Fig. 7) compare Spalding's law with
  Musker's law (above). Ghidoni et al. (2026, §3.3, Eq. 12) print the law,
  up to the quadratic term, as
  $y^+=u^++e^{-\kappa B}\big(e^{\kappa u^+}-1-\kappa u^+-(\kappa u^+)^2/2!\big)$
  with $\kappa\sim0.41$, $B=5$, and use it as the implicit reference against
  which their explicit power law (next item) is timed. Nuca et al. (2025,
  §III, Eq. 2) print it with the cubic term as well,

  $$y^+=u^++e^{-\kappa B}\left(e^{\kappa u^+}-1-\kappa u^+-\tfrac12(\kappa u^+)^2-\tfrac16(\kappa u^+)^3\right),$$

  explicit in $y^+$, so that obtaining $\tau_w$ requires Newton iteration;
  they report that this iteration "would often sporadically diverge" in
  complex-flow WMLES (see [equilibrium wall model](/methods/equilibrium-wall-model.md)).
- **The Spalart–Allmaras analytical law** (Husson et al. 2024, §3.1, Eq. 37,
  after Allmaras & Johnson as cited), a composite of two logarithms and two
  arctangents,

  $$u^+=B+c_1\ln\!\big[(y^++a_1)^2+b_1^2\big]-c_2\ln\!\big[(y^++a_2)^2+b_2^2\big]-c_3\,\theta_1-c_4\,\theta_2,$$

  with $\theta_k$ an arctangent of $(y^++a_k)/b_k$ (see Qualifications for
  the printed argument order) and nine constants printed to sixteen digits
  ($B=5.0333908790505579$, $a_1=8.148221580024245$,
  $a_2=-6.9287093849022945$, $b_1=7.4600876082527945$,
  $b_2=7.468145790401841$, $c_1=2.5496773539754747$,
  $c_2=1.3301651588535228$, $c_3=3.599459109332379$,
  $c_4=3.6397531868684494$; $a_k$, $b_k$, $c_k$, $\theta_k$ page-local).
  The authors choose it because its buffer layer is consistent with the
  [Spalart–Allmaras model](/methods/spalart-allmaras-model.md); below a
  cut-off height they replace it by its tangent line (Tamaki et al., as
  cited), so that the wall-normal gradient is constant and resolvable on a
  coarse mesh. Formulas of the linearization and of its eddy viscosity are
  on the [RANS wall function](/methods/rans-wall-function.md) page.
- **Power law with a closed-form inverse** (Ghidoni et al. 2026, §3.3,
  Eqs. 13–15, after Wilhelm et al. as cited): $u^+=y^+$ for
  $y^+\le y_c^+=11.81$ and $u^+=8.3\,(y^+)^{1/7}$ above, which is continuous
  at $y_c^+$ ($8.3\times11.81^{1/7}=11.81$ *(compiler check, not in the
  sources)*). Each branch inverts explicitly for $u_\tau$ given the velocity
  at a distance $y$, and the two friction velocities are blended as
  $(u_{\tau,\mathrm{vis}}^4+u_{\tau,\log}^4)^{1/4}$ after Menter et al. (as
  cited), so no Newton iteration is needed; the law assumes zero pressure
  gradient. Formulas, cost and accuracy are on the
  [RANS wall function](/methods/rans-wall-function.md) page.
- **Mixing length with van Driest damping**, the differential form behind
  the fit of Fowler et al.: the eddy viscosity is $\nu_t=\kappa y\,u_\tau(1-e^{-y^+/A^+})^2$,
  and integrating the constant-stress equation gives $f$ (Griffin et al.
  2023, Eq. 1.2, in its incompressible form; see Qualifications for the
  printed form). Rickard & Kasbaoui (2026, §4.1, Eq. 4.1) write the van
  Driest profile in closed integral form,

  $$u^+(y^+)=\int_0^{y^+}\frac{2\,d\eta'}{1+\sqrt{1+4\big[\kappa\eta'\big(1-e^{-\eta'/A^+}\big)\big]^2}},\qquad\kappa=0.41,\ A^+=26$$

  ($\eta'$ the integration variable, page-local). The integrand is the
  root of the constant-stress balance $(1+\nu_t^+)\,du^+/dy^+=1$ with the
  mixing length $l^+=\kappa y^+(1-e^{-y^+/A^+})$ and
  $\nu_t=l^2\lvert\partial u/\partial y\rvert$, the form with the damping
  inside the squared length; it is not the profile of Griffin et al.'s
  eddy viscosity, which is linear in $u_\tau$ and gives
  $du^+/dy^+=1/\big(1+\kappa y^+(1-e^{-y^+/A^+})^2\big)$ *(compiler check,
  not in the sources)*. Nuca et al. (2025, §III, Eq. 4) integrate exactly
  that equilibrium ODE, $u^+=\int_0^{y^+}d\eta'/\big(1+\kappa\eta'(1-e^{-\eta'/A^+})^2\big)$,
  with $\kappa=0.41$, $A^+=17$ after Kawai & Larsson (as cited; Cabot used
  $A^+=19$, as they recall), and note that without damping it integrates to
  $\kappa^{-1}\ln(1+\kappa y^+)$, while with damping no closed form links the
  intercept $B$ to $A^+$, so $B$ is evaluated pointwise as
  $u^+(\hat y^+)-\kappa^{-1}\ln\hat y^+$ at some $\hat y^+\gg30$ (Eqs. 1, 8;
  $\hat y^+$ page-local). Elzaabalawy et al. (2023,
  §5.2.1, Eqs. 93–94) use the mixing length $l=0.39\,y\,(1-e^{-y^+/26})$ with
  $\nu_t=l^2\lvert\partial u/\partial y\rvert$ ($l$ page-local) as an
  algebraic RANS model for verifying a high-order solver: without the
  singular wall value of $\omega$, their mean velocity converges at the
  optimal order (Fig. 16).

## Generalizations carried by the sources

- **Rotating channels.** The supervised wall model HYK19 analysed by Vadrot
  et al. (2023b, §II.B.2, Eq. 5) learns the departure of the LES velocity from
  an empirical profile $g(y^+,l^+_\Omega)$ that equals $\kappa^{-1}\ln y^+$
  without rotation and switches to a linear-plus-log form beyond
  $y^+=l^+_\Omega/\kappa$, with $l_\Omega=u_\tau/(2\Omega_{\mathrm{rot}})$ the
  rotation length (page-local). Without rotation the network therefore
  predicts a wall-distance-dependent intercept in place of $B$.
- **Compressible flows.** With variable density and viscosity the profile
  holds only after a [compressible velocity transformation](/definitions/compressible-velocity-transformation.md);
  Griffin et al. (2023, §3) report, citing Yang & Lv, that the classical van
  Driest damping is consistent with the van Driest transformation and its
  semi-local version (written in $y^*$) with the Trettel–Larsson one.
  [Chen et al. (2024)](/sources/chen-2024.md) (§3.1, Eqs. 3.1–3.2) derive
  the same equivalence for the inner layer of the algebraic
  [Baldwin–Lomax model](/methods/baldwin-lomax-model.md): a mixing length
  $\kappa y[1-e^{-y^*/A^+}]$ ($\kappa=0.40$) with semi-local damping is the
  mixing-length relation written for the Trettel–Larsson velocity. Their
  DNS diagnostic of the semi-local eddy viscosity, compared with the
  Johnson–King inner scaling $\kappa y^*[1-e^{-y^*/17}]^2$, collapses up to
  the buffer layer but falls below it in the log region of diabatic
  boundary layers, and follows it more closely with the Griffin–Fu–Moin
  transformation (§3.1, Fig. 3).
- **Outer (defect) layer.** Chen et al. (2024, §3.2, Eqs. 3.9–3.12) use
  Clauser's defect law $u_e^+-u^+=g(y/\Delta_{RC})$ with the Rotta–Clauser
  thickness $\Delta_{RC}=u_e^+\delta^*$ (page-local $u_e^+$, $g$,
  $\Delta_{RC}$); for the incompressible zero-pressure-gradient layer they
  take, from Monkewitz et al. (2007) as they cite it, the outer maximum 5.55
  of $y\,\partial u^+/\partial y$ at $y/\Delta_{RC}=0.155$. For compressible
  layers the van Driest-transformed defect collapses better, with outer
  velocity scale $u_\tau/\sqrt{\langle\rho\rangle/\rho_w}$, after Smits &
  Dussauge as they cite it (Eq. 3.12, Fig. 5); this is the basis of their
  outer-layer correction (see
  [compressible velocity transformation](/definitions/compressible-velocity-transformation.md)).
- **Adverse pressure gradients.** [Knopp (2022)](/sources/knopp-2022.md)
  finds the log law robust in adverse-pressure-gradient boundary layers but
  confined below $y^+_{\log,\max}=1.78\,Re_\tau^{1/2}(\Delta p_s^+)^{-1/5}$, with
  $\Delta p_s^+=\nu\rho^{-1}u_\tau^{-3}dP/ds$ the inner-scaled pressure
  gradient, and a half-power law above it (Eq. 35; page-local symbols); the
  log layer then ends below $0.11\delta$ for $\Delta p_s^+>0.005$ and a
  Rotta–Clauser parameter above 4.5 (§5.2). Details on
  the [wall law in adverse pressure gradient](/definitions/adverse-pressure-gradient-wall-law.md)
  page. Gillyns et al. (2022, §1) place the validity of the law of the wall
  at $y/\delta\lesssim0.15$ and expect an algebraic wall model to fail once
  Coles' wake reaches the matching point near separation.
- **Pressure gradients in wall models.** The equilibrium fit of Meneveau (2020), as used by
  Fowler et al. (2022, Algorithm 1), returns $\langle u_\tau\rangle h_{\mathrm{wm}}/\nu$
  as a function of $U_{\mathrm{LES}}h_{\mathrm{wm}}/\nu$ and a dimensionless
  wall-parallel pressure gradient, and returns zero friction (separation) for
  strong adverse gradients.

- **Hypersonic cold walls.** [Huang et al. (2022)](/sources/huang-2022.md)
  (§4.1, Eq. 4.5, Fig. 11) test logarithmic behaviour with the diagnostic
  function $y^+\,du^+/dy^+$ applied to the transformed velocity: it is nearly
  constant for $y^+\approx40$–100 in their Mach 2.5 and 4.9 quasi-adiabatic
  boundary layers at $Re_\tau=1172$, but their Mach 10.9 boundary layer with
  $T_w/T_r=0.20$ shows no wide constant region up to that $Re_\tau$, which they
  attribute to reduced scale separation from strong wall cooling. Above the
  log region the mean velocity follows a power law
  $\langle u\rangle/U_\infty=(y/\delta_\infty)^{1/n_{pl}}$ over
  $0.2\lesssim y/\delta\lesssim0.6$ with $n_{pl}=5$–8, and the van Driest
  velocity over $0.2\lesssim y/\delta\lesssim0.9$ with $n_{pl}=5$ (Eqs.
  4.6–4.7; page-local $n_{pl}$, $\delta_\infty$ the height where the mean
  velocity first reaches $U_\infty$).
- **Vegetated (canopy) walls: the displaced log law.** Over a submerged
  canopy of flexible blades in open-channel flow,
  [Lohrer & Fröhlich (2025)](/sources/lohrer-2025.md) (§5.2, Eqs. 5.6–5.8),
  after Nepf (2012) as they cite it, write the mean velocity above the
  canopy as

  $$\frac{\langle u\rangle}{u_{\tau,\mathrm{vo}}}=\frac1\kappa\ln\frac{y-y_{\mathrm{vo}}}{\nu/u_{\tau,\mathrm{vo}}}+B-\Delta U^+_{\mathrm{vo}},$$

  with $y_{\mathrm{vo}}$ the displacement height (virtual origin),
  $u_{\tau,\mathrm{vo}}$ the friction velocity built from the total shear
  stress at $y_{\mathrm{vo}}$ and $\Delta U^+_{\mathrm{vo}}$ a roughness
  function (all page-local; the viscous length $\nu/u_{\tau,\mathrm{vo}}$
  "plays the same role as the roughness length in rough-wall boundary
  layers"). A fit over $2.5h_c\le y\le0.8H$ ($h_c=0.20H$ the mean hull height of
  the reconfigured canopy, $H$ the water depth, page-local) with $\kappa=0.41$, $B=5.5$ gives
  $y_{\mathrm{vo}}=0.18H$, $\Delta U^+_{\mathrm{vo}}=15.4$ and
  $u_{\tau,\mathrm{vo}}=0.16U$; fitting $\kappa$ as well gives $\kappa=0.38$,
  $y_{\mathrm{vo}}=0.13H$ and $\Delta U^+_{\mathrm{vo}}=17.4$, so the
  displacement height is sensitive to the assumed $\kappa$. Below the canopy,
  scaled with the bed friction velocity, $u^+=y^+$ holds only up to
  $y^+\approx2$. The flow is a fluid–structure-interaction problem resolved by
  LES with an immersed boundary, not a wall-modelled flow.
- **Volume-filtered law of the wall: the wall slip.** Filtering the flow
  with a compact kernel of support width $\Delta_f$ (page-local) that is
  truncated at the wall but not rescaled leaves a non-zero filtered velocity
  at the wall, the slip. Rickard & Kasbaoui (2026, §4.1, Eqs. 4.2–4.5) obtain
  a model of the mean slip by filtering the van Driest profile above; for
  $\Delta_f^+\gg1$ it tends to $\varphi_{f,w}^{-1}(2\kappa)^{-1}\ln(\Delta_f^+/2)$,
  with $\varphi_{f,w}$ the fluid volume fraction at the wall (1/2 at a planar
  wall; page-local), and a fitted correction makes it accurate within 1 %
  for $\Delta_f^+\ge100$. The slip grows logarithmically with the filter
  width, $6.93u_\tau$ at $\Delta_f^+=50$ and $13.5u_\tau$ at $\Delta_f^+=300$
  in filtered channel DNS at $Re_\tau=5200$ (§3.2). The law of the wall
  thus survives filtering as a law for the slip; see
  [wall-modelled LES](/methods/wall-modelled-les.md).
- **Low Reynolds number.** [Kim et al. (2022)](/sources/kim-2022.md) (§III D,
  Fig. 12) recall, citing the channel DNS of Moser, Kim & Mansour, that the
  DNS mean velocity at $Re_\tau=180$ deviates slightly from the log law in the
  logarithmic region, and use this non-universality to explain why an SGS
  model trained by reinforcement learning at $Re_\tau=180$ under-estimates the
  buffer-layer slope at $Re_\tau=360$, while one trained at 360 over-estimates
  the mean velocity at 180 (see
  [reinforcement-learning closures](/methods/reinforcement-learning-closure.md)):
  "the non-universal characteristic of $Re_\tau=180$ affects the
  generalization performance of the DRL model".
- **Separated regions.** Cai et al. (2022, §II.C.2) state that equilibrium
  and non-equilibrium wall models assume quasi-parallel near-wall flow and
  that their use under separation is "physically not appropriate", but that
  the small wall stress there keeps the model in the low-$y^+$ range "where
  linear profile applies", and recall three studies finding the flow not very
  sensitive to the wall model in the recirculation zone.
- **Universality claimed for learned models.** Bae & Koumoutsakos (2022,
  Discussion) state, citing the literature, that all flows with inner–outer
  scale separation exhibit a log law, and take this as the reason a state
  space built on the local log-law slope and intercept can extend to
  roughness, stratification and compressibility (not shown).

- **RANS on DG grids.** [Zhao et al. (2023b)](/sources/zhao-2023-b.md)
  (§5.1, Fig. 5-2) report that the velocity profile of their interior-penalty
  DG solver with the [$k$-$\omega$ SST model](/methods/k-omega-sst-model.md)
  on a turbulent flat plate ($M=0.2$, $Re_L=1.12\times10^7$, first-cell
  $y^+=1$) agrees with a reference profile they cite in the log layer.
  [Lodares et al. (2022)](/sources/lodares-2022.md) (§7.3, Fig. 8a) compare
  the $u^+(y^+)$ profile of their entropy-stable DG Spalart–Allmaras RANS on
  the coarsest flat-plate mesh of the NASA Turbulence Modeling Resource
  ($M=0.2$, $Re=5\times10^6$, profile at $x=0.97008$, $N=4$, 7, 10) with the
  viscous sublayer, the log law and a fine-grid FUN3D solution, "in good
  agreement". [Vandenhoeck et al. (2022)](/sources/vandenhoeck-2022.md)
  (§4.1, Figs. 9–10) find the velocity profiles of their flux-reconstruction
  $k$-$\omega$ SST solution of the Wieghardt plate in agreement with
  experiment and Spalding's law, coinciding across orders, on meshes whose
  first element reaches $y_1^+\simeq25$ without wall function (see
  [RANS wall function](/methods/rans-wall-function.md)).
- **Pipe flow and transitional plates in RANS.** [Tomboulides et al. (2025)](/sources/tomboulides-2025.md)
  (§3.2, Fig. 5) find their [$k$-$\tau$](/methods/k-tau-model.md) and
  regularized $k$-$\omega$ pipe-flow profiles at $Re_\tau=1142$ in excellent
  agreement with DNS in the viscous sublayer ($y^+<5$) and with the log law
  ($\kappa=0.41$, $B=5.5$) for $30<y^+<200$, with minor RANS–DNS
  differences there and "expected deviations" in the outer layer.
  [Ghidoni & Noventa (2026)](/sources/ghidoni-2026-b.md) (§IV.A,
  Figs. 12–13) use $u^+=y^+$ and the log law with $\kappa=0.41$, $B=5$ as
  reference for the turbulent part of the transitional ERCOFTAC plate
  boundary layers computed with their
  [laminar-kinetic-energy transition model](/methods/laminar-kinetic-energy-transition-model.md),
  with which all their velocity profiles agree.
- **Compressible channel.** Wang et al. (2023b, §4.2, Eqs. 10–11, Fig. 11)
  compare the van Driest-transformed mean velocity of their gas-kinetic DNS of
  a channel at bulk $M_b=0.8$ and bulk Reynolds number 3000 (isothermal walls)
  with the incompressible log law; see the
  [compressible velocity transformation](/definitions/compressible-velocity-transformation.md).

## The law of the wall as a constraint

Vadrot et al. (2023b, §V) make preservation of the law of the wall the minimum
requirement of any learned wall model: a model must reproduce the log law in
channel flow at all Reynolds numbers, seen and unseen, before it is credited
with improvements elsewhere (see [machine-learning wall models](/methods/machine-learning-wall-model.md)).
Their a priori test of the ZHY21/ZYZY22 networks feeds a law of the wall built
by stitching the $Re_\tau=5200$ DNS wall layer to $u^+=\kappa^{-1}\ln y^++B$ at
$y^+=100$ (§IV.B). The mean-velocity departure from the log law is the
[log-layer mismatch](/definitions/log-layer-mismatch.md).
Bae & Koumoutsakos (2022, Methods, Eq. 3) build the states of their
log-law-based reinforcement-learning wall model from the instantaneous local
slope and intercept of the log law at the matching height, so that the agent
learns to raise or lower $\tau_w$ according to whether the local state lies
above or below $u^+=0.41^{-1}\ln y^++5.2$ (Fig. 2); see
[machine-learning wall models](/methods/machine-learning-wall-model.md).
Vadrot et al. (2023a, §V) state the same position for their own
reinforcement-learning model: recovering the log law is "an essential
step", since "if a model cannot capture the log law, it would be hard for it
to capture other flow phenomena"; their model, trained at $Re_\tau=10^4$,
recovers $u^+=0.4^{-1}\ln y^++5$ in half-channel WMLES up to
$Re_\tau=10^{10}$ whenever the matching height lies in the log layer, while
at $Re_\tau=180$ its profile lies above the DNS (§III.A, Fig. 6).

**Data-driven RANS corrections.** Two sources make the same point for
learned corrections of the [$k$-$\omega$ SST model](/methods/k-omega-sst-model.md):
a correction trained on separated flows breaks the log law unless it is
kept out of the attached boundary layer.
[Wu et al. (2025)](/sources/wu-2025.md) (§2.1, Eqs. 3–4) recall, after
Wilcox as they cite it, the log-layer calibration of the $\omega$ equation,

$$\beta_\omega-\beta^*\gamma_\omega=\kappa^2\sqrt{\beta^*}\,\sigma_\omega,\qquad\kappa=0.41,$$

with $\gamma_\omega$, $\beta_\omega$ the production and destruction
coefficients of the $\omega$ equation (page-local; the source's $\gamma$
and $\theta$), a "necessary condition for accurate resolution of the log
layer". A [field-inversion](/methods/field-inversion-machine-learning.md)
multiplier $\beta(\boldsymbol x)$ on the destruction term turns the
left-hand side into $\beta(\boldsymbol x)\beta_\omega-\beta^*\gamma_\omega$,
so the constraint holds only where $\beta=1$. Their conditioned inversion
switches the multiplier off inside the boundary layer with the DDES shielding
function; on a zero-pressure-gradient flat plate at $Re_L=10^7$ the
conditioned symbolic model keeps $\beta=1$ there and matches SST and the
viscous and log layers, while the unconditioned one gives $\beta\approx1.06$
in the boundary layer, an "erroneous log layer", a thicker boundary layer
and an over-predicted $C_f$ (§4.5, Figs. 47–48).
[Oulghelou et al. (2025)](/sources/oulghelou-2025.md) (§4.2.1, Table 3)
quantify the same effect for sparse symbolic corrections in channel flow at
$Re_\tau=1000$: the mean absolute error of $u^+$ is 0.44 for the baseline
SST, 2.41 for a correction trained on separated flows and 8.97 for one
trained on a near-sonic jet, which strongly lowers the eddy viscosity; their
locally weighted blend of the three gives the baseline's 0.44, with a
weight of the baseline close to one across the channel. On the unseen flat
plate the blend's error is 0.7 against 0.42 for SST and 6.27 for the jet
correction, although the jet correction receives a significant weight in
the log region, which the authors read as weight shifts there having "little
impact on the overall accuracy" (§5.1.1, Table 9, Fig. 11). See
[turbulence-model aggregation](/methods/turbulence-model-aggregation.md).

**A diagnostic of logarithmic behaviour.** The premultiplied gradient
$y^+\,du^+/dy^+$ is constant, equal to $1/\kappa$, in a log layer: Huang et
al. (2022, Eq. 4.5) use it on transformed hypersonic profiles (above), and
Mukha et al. (2025, §III.B.2, Fig. 3) use $\kappa y^+\,du^+/dy^+$, equal to
one in a log layer, to expose the jumps of the velocity derivative at the
element boundaries of their spectral-element WMLES (see
[log-layer mismatch](/definitions/log-layer-mismatch.md)).

The friction velocity is also the first quantity a near-wall LES must get
right without a wall model: [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md)
(§7.2–7.4) report $u_\tau$ errors in pipe flow at $Re_\tau=1000$ of $+15.3$ %
(no model), $+9.6$ % (Smagorinsky with van Driest damping) and $-1.8$ %
(implicit [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md))
on a uniform mesh with $\Delta x^+=\Delta y^+\approx9$.

## Qualifications

- The constants are source choices, not measurements of this bundle; the
  table records them and no value is preferred here.
- Mozaffari et al. (2024) print for Cai & Sagaut (2021), their ref. [8], a
  DOI identical to the one they print for Wilhelm et al. (2021), ref. [63];
  one of the two DOIs is a slip.
- **Printed viscosity of Zhao et al. (2023a).** For $Re_\tau=180$ they print
  $\mu=2.83\times10^{-4}$ (§5.2). With their Eqs. (25)–(26), $\rho=1$, $\delta=1$
  and $U_c=1$: $U_c^+=2.5\ln180+5.5\approx18.48$, $u_\tau\approx0.0541$ and
  $\mu\approx3.01\times10^{-4}$ *(compiler check, not in the sources)*; the
  printed value is not reproduced.
- Griffin et al. (2023) print Eq. (1.2) as
  $\mu_t=\kappa y\langle\rho\rangle\sqrt{\tau_w/\langle\rho\rangle}\,(1-\exp(y^+/A^+))^2$,
  without the minus sign in the exponent; their own text describes a damping
  function that tends to the undamped mixing length away from the wall, which
  holds only for $(1-e^{-y^+/A^+})^2$. In §3 they print "$\kappa$ … 4.1" for
  the 0.41 stated in §1 and at the end of §3.
- **Intercept of Mukha et al. (2025) for the boundary layer.** §IV.A
  prints "here with $\kappa=0.41$ and $B=5.2$" for the flat-plate WMLES, and
  App. A prints "$\kappa=0.41$ and $B=5.5$" for the accuracy analysis of the
  same law on the same flow; which value the simulations used cannot be
  told from the arXiv v1 read.
- **Argument order of the arctangents of Husson et al. (2024).** They define
  $\mathrm{atan2}(y,x)$ as the principal argument of $x+iy$ and print the
  terms as $\mathrm{atan2}(y^++a_k,b_k)$, the argument of $b_k+i(y^++a_k)$.
  Evaluated so, the law gives $u^+(0)\approx10.84$ and a log-law intercept
  near $-6.3$; with the arguments exchanged, the argument of
  $(y^++a_k)+ib_k$, it gives $u^+(0)=0$ to machine precision, $u^+\approx1.00$
  at $y^+=1$, the slope $1/0.41$ and the intercept 5.033 at $y^+=10^5$
  *(compiler check, not in the sources)*. The printed order is therefore
  inconsistent with the printed definition; the exchanged order is the one
  that yields a wall law.
- **Printed truncations of Spalding's law.** Ghidoni et al. (2026, Eq. 12)
  print the series up to the quadratic term, Nuca et al. (2025, Eq. 2) up to
  the cubic term; both call it Spalding's law. The difference is recorded
  without a test of which form either code uses beyond the printed one.
- **Printed slips of Nuca et al. (2025).** The text gives $\kappa$ "from 0.38
  to 0.41" for the global fits, Table II up to 0.42 (0.40 for Reichardt);
  the relation for $B$ appears twice, as Eqs. (1) and (8), written with
  $\log$ and $\ln$. The high-Re constants give $C=6.66$, outside the range
  $C\in[6.8,7.7]$ over which the global Reichardt approximation is fitted,
  so its use with the high-Re set in the channel test is an extrapolation
  that the paper does not mention *(compiler check, not in the sources)*.
- **Printed slips of Huang et al. (2022b)** (§2.4.3). The friction velocity
  of their manufactured profile is printed as
  $\sqrt{\rho_0u_0^2C_f/\rho}=\sqrt{a\rho_0u_0^2x^b/(2\rho)}$ with the fit
  $C_f=ax^b$, the two forms differing by the factor 1/2 under the root; with
  $\tau_w=\tfrac12\rho_0u_0^2C_f$ the second is the consistent one *(compiler
  check, not in the sources)*. The fit is said to be of the data "shown in
  Fig. 8", which is Fig. 9; the profile's $\kappa$ and additive constant are
  not printed, and the cited Reichardt (1951) is attached in the text to the
  LU-SGS solver instead.
- Oulghelou et al. (2025) and Wu et al. (2025) write the steady
  incompressible RANS equations and solve them in OpenFOAM (Wu et al. also run CFL3D for a
  compressible airfoil case); their log-law statements concern RANS
  profiles, not LES.

## Contradictions

- **Constants of the explicit inverse wall law of Cai & Sagaut (2021).**
  [Cai et al. (2022)](/sources/cai-2022.md) (§II.C.1, Eqs. 24–26) present
  the tanh-blended explicit inverse $y^+(Re_y)$ as the model "proposed in
  Refs. 23 and 29" (ref. 29 is Cai & Sagaut 2021) and print the blend scale
  180.8, the exponent 0.789 and, in the companion forward profile, $E=11.27$.
  [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) (§2.2, Eqs. 12–15,
  lines 160–164) give the same functional form "in the form [8]" (ref. [8]
  is Cai & Sagaut 2021) with $s=86.58$, $p=0.7894$ and $E\approx7.9$,
  $\kappa\approx0.41$. Cai is a co-author of both and both run in ProLB;
  neither paper says that its constants recalibrate the cited model, so the
  two sources disagree on the constants of the same attributed law (the
  blend scales differ by a factor of about two and the log branches through
  $E$). Cai & Sagaut (2021) is not ingested. [Nuca et al. (2025)](/sources/nuca-2025.md)
  (§III, Eq. 5) print a third form attributed to "model 2" of Cai & Sagaut
  (2021), a forward law $u^+(Re_y)$ blended with powers of
  $e^{-Re_y/s}$ instead of $\tanh$, and say that they re-optimize $p$ and
  $s$; their constants therefore do not bear on the disagreement, but the
  functional form they attribute differs from that of the other two, so the
  ingested sources do not fix the form either. What would decide it: the
  printed equations and constants of Cai & Sagaut (2021). *Open.*

# Citations

- [Fowler et al. (2022)](/sources/fowler-2022.md) — App. C, Eqs. (C1)–(C2), Fig. 17; Algorithm 1; Fig. 4.
- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) — §II.B, Eq. (1); §IV.C, Eq. (12); §V.C.
- [Griffin et al. (2023)](/sources/griffin-2023.md) — §1, Eq. (1.2); §3, Fig. 6.
- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) — §II.B, Eqs. (1)–(6); §IV.B; §V.
- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §VII.D, Fig. 8.
- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §7.2–7.4, Figs. 25–27.
- [Gillyns et al. (2022)](/sources/gillyns-2022.md) — §1; §3, Eq. (3).
- [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) — Eq. (3); Fig. 2; Discussion; Methods.
- [Knopp (2022)](/sources/knopp-2022.md) — §4, Eq. (26); §5–6, Eq. (35).
- [Huang et al. (2022)](/sources/huang-2022.md) — §4.1, Eqs. (4.5)–(4.7), Figs. 11–12.
- [Cao et al. (2022)](/sources/cao-2022.md) — §3.3, Eq. (8).
- [Cogo et al. (2022)](/sources/cogo-2022.md) — §4, Fig. 8.
- [Kim et al. (2022)](/sources/kim-2022.md) — §III D, Fig. 12.
- [Cai et al. (2022)](/sources/cai-2022.md) — §II.C.1, Eqs. (24)–(26); §II.C.2.
- [Blind et al. (2023)](/sources/blind-2023.md) — §3.3.
- [Carlsson et al. (2023)](/sources/carlsson-2023.md) — §4.3, Figs. 4–5.
- [Dang et al. (2022)](/sources/dang-2022.md) — §5.1, Fig. 17.
- [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) — §3.2, Eq. (3.1).
- [Lewis et al. (2023)](/sources/lewis-2023.md) — §3.2.2 (HAL accepted manuscript).
- [Kang et al. (2023)](/sources/kang-2023.md) — channel-flow mean-velocity figures (§3).
- [Wang et al. (2023b)](/sources/wang-2023-b.md) — §4.2, Eqs. (10)–(11), Fig. 11 (arXiv v1).
- [Zhao et al. (2023a)](/sources/zhao-2023.md) — §5.2, Eqs. (25)–(26) (arXiv v1).
- [Zhao et al. (2023b)](/sources/zhao-2023-b.md) — §5.1, Fig. 5-2.
- [Vadrot et al. (2023a)](/sources/vadrot-2023.md) — §II.B.1, Eq. (1); §II.B.3; §III.A–III.B, Fig. 6; §V (arXiv v3).
- [Constant et al. (2024)](/sources/constant-2024.md) — §3.2, Eqs. (6)–(8), Fig. 7 (HAL author manuscript).
- [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) — §2.2, Eqs. (9)–(15); ref. [8] (HAL accepted manuscript).
- [Chen et al. (2024)](/sources/chen-2024.md) — §2.3, Eqs. (2.7)–(2.10); §3.1, Eqs. (3.1)–(3.4), Fig. 3; §3.2, Eqs. (3.9)–(3.12), Fig. 5.
- [Mukha et al. (2025)](/sources/mukha-2025.md) — §II.C.1; §III.A; §III.B.2–III.B.3, Fig. 3; §IV.A; App. A, Figs. 18–21 (arXiv v1).
- [Lohrer & Fröhlich (2025)](/sources/lohrer-2025.md) — §5.2, Eqs. (5.6)–(5.8).
- [Oulghelou et al. (2025)](/sources/oulghelou-2025.md) — §4.2.1, Table 3, Fig. 4; §5.1.1, Table 9, Fig. 11 (arXiv v2).
- [Wu et al. (2025)](/sources/wu-2025.md) — §2.1, Eqs. (3)–(4); §4.5, Figs. 47–48 (authors' manuscript).
- [Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md) — §5.2.1, Eqs. (93)–(94), Fig. 16; §5.3.
- [Ghidoni et al. (2026)](/sources/ghidoni-2026.md) — §3.3, Eqs. (12)–(15); §4.
- [Lederer et al. (2026)](/sources/lederer-2026.md) — §4.2, Fig. 7 (arXiv v1).
- [Rickard & Kasbaoui (2026)](/sources/rickard-2026.md) — §3.2, Fig. 6; §4.1, Eqs. (4.1)–(4.5), Fig. 11.
- [Aiello et al. (2026)](/sources/aiello-2026.md) — §4.1, Fig. 1.
- [Nuca et al. (2025)](/sources/nuca-2025.md) — §I; §III, Eqs. (1)–(8); §IV, Eqs. (9)–(10), (24), Fig. 3; §V.A–V.B, Tables II–VI.
- [Husson et al. (2024)](/sources/husson-2024.md) — §3.1, Eqs. (36)–(38).
- [Tomboulides et al. (2025)](/sources/tomboulides-2025.md) — §3.2, Fig. 5.
- [Ghidoni & Noventa (2026)](/sources/ghidoni-2026-b.md) — §IV.A, Figs. 12–13.
- [Vandenhoeck et al. (2022)](/sources/vandenhoeck-2022.md) — §4.1, Figs. 9–10.
- [Lodares et al. (2022)](/sources/lodares-2022.md) — §7.3, Fig. 8.
- [Huang et al. (2022b)](/sources/huang-2022-d.md) — §2.4.3, Eq. (52), Fig. 9.
