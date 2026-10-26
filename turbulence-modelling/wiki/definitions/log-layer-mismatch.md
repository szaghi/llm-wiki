---
type: Definition
title: "Log-layer mismatch"
description: "The shift, in wall units, between the mean velocity of a wall-modelled or hybrid simulation and the logarithmic law in the log layer: how the sources measure it, the mechanisms they attribute it to, the remedies they use, and its appearance in learned wall models."
status: established
aliases: [LLM, log-layer shift, super-buffer layer error]
tags: [wmles, wall-model, hybrid-rans-les, boundary-layer]
timestamp: 2026-10-25T20:36:00Z
---

# Log-layer mismatch

The log-layer mismatch (LLM) is the offset between the mean velocity predicted
by a [wall-modelled LES](/methods/wall-modelled-les.md) (or a
[hybrid RANS/LES](/definitions/hybrid-rans-les.md)) and the logarithmic
[law of the wall](/definitions/law-of-the-wall.md) in the log layer, measured
in wall units: the computed $u^+$ runs parallel to $\kappa^{-1}\ln y^++B$ but
shifted. Because the wall stress is inferred from (or balances) that velocity,
a mismatch is an error in $\tau_w$: [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md)
(§I) recall, citing Spalart, that LLM produces a 15 % error in the wall-shear
stress.

## Measurement

Vadrot et al. (2023b, Table III, §IV.C) measure the LLM as the inner-unit
difference between the LES mean velocity and $\kappa^{-1}\ln y^++B$ with
$\kappa=0.4$, $B=5$ — positive when the LES profile lies above the log law.
Their values for the reinforcement-learning wall model BK22 in half-channel
flow run from $+2.2$ at $Re_\tau=180$ through $+1.0$ at $10^5$ to $-0.9$ at
$10^6$ and about $-3.2$ for $Re_\tau=10^8$–$10^{10}$. A mismatch need not be a
constant offset: a model whose effective log slope differs from $1/\kappa$
gives a mismatch that grows with the matching height. For the supervised model
ZYZY22, whose WMLES log law has slope $1/0.32$, Vadrot et al. (2023b, Eq. 9)
write $\mathrm{LLM}\sim(1/\kappa_{\mathrm{ZYZY22}}-1/\kappa)\ln y^+$, which
grows with $Re_\tau$.

## Mechanisms recalled by the sources

The sources attribute LLM to the coupling between the wall model and the
under-resolved first cells of the LES, not to the log law itself.

- **Numerical and subgrid errors at the first off-wall points.**
  [Fowler et al. (2022)](/sources/fowler-2022.md) (§1) recall the argument of
  Kawai & Larsson (2012) that the near-wall region of WMLES is inherently
  under-resolved, so the wall-model height should be placed further from the
  wall to reduce LLM. [Griffin et al. (2023)](/sources/griffin-2023.md) (§4.1)
  recall from the same work that LES numerical errors contaminate the matching
  data when the matching distance is of the order of the wall-normal grid
  spacing; in their own WMLES the grid point nearest the wall carries an error
  that persists under refinement, which they call consistent with Kawai &
  Larsson and harmless because the inner solution applies below the matching
  height (Griffin et al. do not use the term log-layer mismatch).
  [Agrawal et al. (2022)](/sources/agrawal-2022.md) (§VII.D) state a related
  mechanism for their dynamic SGS models: both under-predict the SGS stress in
  the under-resolved first cells, which raises the resolved fluctuations and
  flattens the mean-velocity slope.
- **Instantaneous local use of a mean law.** [Fowler et al. (2022)](/sources/fowler-2022.md)
  (§1) recall the argument of Bou-Zeid et al. (2005): by the Schwarz
  inequality, applying the law of the wall locally and instantaneously
  over-predicts the mean wall stress.
- **Numerical dissipation of the scheme in the LES region.**
  [Carlsson et al. (2023)](/sources/carlsson-2023.md) (§4.3, Fig. 4, Table 2)
  run SST-IDDES of channel flow at $M_b=0.15$ and $Re_\tau=395$, 2400 and
  18 000 on grids built to WMLES practice (first node at $y^+\approx0.5$,
  stretching 1.14, $64\times64$ points in the wall-parallel plane, so
  $\Delta x^+\approx40$–1800). With a second-order central scheme carrying
  the fourth-difference artificial dissipation of RANS practice
  ($\kappa^{(4)}=1/128$ in their notation) the mismatch is "significant" at
  all Reynolds numbers: the profile is right in the viscous sublayer, buffer
  layer and the part of the log layer where IDDES runs in RANS mode, "but fails
  as soon as the model switches to LES due to adding to[o] much numerical
  dissipation". Their low-dissipation low-dispersion schemes (fourth-difference
  coefficient 1/1024 or 1/512 plus gradient-extrapolated face values) leave
  only a small mismatch at the RANS–LES interface, near $y^+\approx200$ at
  $Re_\tau=2400$ and $y^+\approx2000$ at $Re_\tau=18\,000$; the same holds for
  the transformed profiles of isothermal-wall channels at $M_b=1.5$ (Fig. 5).
  Each case is run on one grid (Table 2) with the same SST-IDDES, and only
  the convective scheme changes (Table 1: the reference scheme differs from
  the low-dissipation ones in its fourth-difference coefficient and in the
  face extrapolation); the authors attribute the mismatch of the reference
  scheme to its [numerical dissipation](/properties/numerical-dissipation.md)
  (§4.3). Details on
  the [low-dissipation low-dispersion scheme](/methods/low-dissipation-low-dispersion-scheme.md)
  page.
- **Spurious correlation between resolved and modelled quantities.**
  [Kim et al. (2022)](/sources/kim-2022.md) (§III E) mention in passing,
  citing Yang, Park & Moin (2017), that in LES wall modelling "artificial
  correlation between the resolved and modeled variables could cause LOW
  mismatch" (LOW: law of the wall); the remark accompanies their correlation
  analysis of SGS models (Table IV), and they run no wall-modelled LES.
  [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) report the corresponding
  measurement for a wall model: the modelled wall stress of the equilibrium
  model is perfectly correlated with the LES velocity at the sampling
  location, against about 0.3 in DNS (see
  [equilibrium wall model](/methods/equilibrium-wall-model.md)).
- **Modelled-stress depletion in hybrid methods.** [Haering et al. (2022)](/sources/haering-2022.md)
  (§II.A) argue that a hybrid RANS/LES method which reduces the modelled
  stress and waits for resolved turbulence to grow passively must have regions
  where the total stress is depleted, and list LLM among the consequences
  (with reduced body forces, premature separation, delayed reattachment).
  [Cai et al. (2022)](/sources/cai-2022.md) (§I, §II.C.1) describe a related
  depletion at an immersed boundary: the boundary treatment is not
  conservative, so the total (modelled plus resolved) Reynolds stress is not
  maintained near the wall, the skin friction deviates and, in LES, turbulence
  development is "strongly delayed"; they do not use the term log-layer
  mismatch.

## Remedies used or recalled

| Remedy | Where |
|---|---|
| Match the wall model away from the wall, $h_{\mathrm{wm}}\ge3\Delta$ (Kawai & Larsson 2012) | recalled by Griffin et al. (2023, §4.1), who use $h_{\mathrm{wm}}=0.3\delta$ with 12 points per half-height; Agrawal et al. (2022, §VII.D) match at the second off-wall point of a staggered mesh |
| Filter the wall-model input in space (the "2Δ spatial filter" of Bou-Zeid et al. 2005) or in time and/or wall-parallel space (Yang, Park & Moin 2017) | recalled by Fowler et al. (2022, §1), who apply a "2Δ spatial filter, like that used in Bou-Zeid et al. (2005)" to $U_{\mathrm{LES}}$ (§5.1; their $\Delta$ is the matching height, the first grid point at half the wall-normal spacing); Vadrot et al. (2023b, §II.B.1, Table II) filter the input of their equilibrium model with a sharp filter of twice the grid spacing |
| Random forcing near the wall | recalled by Vadrot et al. (2023b, §I) |
| Stochastic forcing at the RANS/LES interface (Piomelli et al.) | recalled by Haering et al. (2022, §II): removes LLM but is problem-dependent; the SAS-F forcing of Menter et al. still showed LLM in channel flow |
| Several cells below the matching height: $h_{\mathrm{wm}}=0.1\delta_0$ with four uniform cells below it ($\Delta y=0.25h_{\mathrm{wm}}$), "to reduce numerical errors from the LES transferred to the wall model (Kawai & Larsson, 2012) and avoid the log-layer mismatch" | [Hoy & Bermejo-Moreno (2022)](/sources/hoy-2022.md) (§3), Mach 3 shock/boundary-layer interaction |
| Impose the wall stress through a wall eddy viscosity, $\nu_t\rvert_w=\tau^{\mathrm m}_w/\big(\rho\,(\partial u/\partial y)_w\big)-\nu$ with no slip kept ("viscosity augmentation"), instead of a Neumann condition | [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) (Methods, Eq. 10), stated, citing earlier work, to be "better at resolving the so-called log-layer mismatch"; $\tau^{\mathrm m}_w$ the modelled wall stress (page-local) |
| Short exponential moving average of the wall-model input in time | [Gillyns et al. (2022)](/sources/gillyns-2022.md) (§3, §5, Eq. 4), who recall Yang et al. (2017) and Fowler et al. (2022) for time filtering; without it ($C_t=0$) their wall model diverged, which they attribute "most likely" to Gibbs oscillations at the element boundary, not to the mismatch |
| Elevating function $f_e$ of IDDES, which raises the RANS length scale near the RANS–LES interface, and the wall-distance-based subgrid length of IDDES, meant to "give a correct log-layer behavior in WMLES without the need to alter the value of the modeling constant" | recalled from Shur et al. (2008) by Carlsson et al. (2023, §2, Eqs. 18–19), who use IDDES; a small mismatch remains at the interface with their low-dissipation schemes (§4.3) |
| Low-dissipation convective scheme in the LES region | Carlsson et al. (2023, §4.3, Figs. 4–5): reduces a significant mismatch to a small one at the RANS–LES interface (above) |
| Near-wall eddy viscosity that enforces the total (modelled plus resolved) stress of a mixing-length RANS model, "several grid points from wall" (constrained LES) | Cai et al. (2022, §II.C.1, Eq. 27) at an immersed boundary; the mean velocity in the log layer is not shown, so its effect on mismatch is not reported (see [wall-modelled LES](/methods/wall-modelled-les.md)) |
| Active forcing of resolved fluctuations at the rate the modelled stress is reduced | [active model split](/methods/active-model-split.md): Haering et al. (2022, §V.A.1) report no LLM in channel flow at $Re_\tau\approx5200$ on four grids with $\Delta x^+\approx700$–$1550$ |

## First-point matching without mismatch

Two sources match at the first off-wall cell centre on Voronoi grids of
[CharLES](/software/charles.md), against the Kawai–Larsson recommendation.
[Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) (§II.B) use no
temporal filtering or other treatment of the LES velocity at the matching
point and do not report LLM; Agrawal et al. (2022, §VII.D) state that
first-point matching on hexagonally close-packed Voronoi grids showed no LLM
in their prior tests. The sources thus agree that the remedy depends on the
discretization: second-point matching for staggered finite-difference meshes,
first-point matching for these Voronoi grids. None of them tests both on the
same grid.

A third discretization gives a similar result.
[Gillyns et al. (2022)](/sources/gillyns-2022.md) (§3, §7, Table 1) sample the
LES velocity at the top node of the first spectral element (polynomial degree
7, $y^+=63$–153 at $Re_\tau=1000$; 260 and 520 at $Re_\tau=5200$), i.e. at the
first element interface. They report mean-velocity errors (normalized RMS,
excluding the first nodes) of 0.52–1.09 % and a mean velocity close to DNS
"down to $y^+\simeq10$" inside the under-resolved first element, which they
attribute to the spectral element method. They do not discuss log-layer
mismatch by name.

## In learned wall models

Learned wall models can create a mismatch of their own. Vadrot et al. (2023b,
§IV.C) trace the BK22 mismatch to its state map. Let the neutral line be the
set of states where the LES velocity at $h_{\mathrm{wm}}$ equals the log law
(Eq. 10); above it the right action is to raise $\tau_w$, below it to lower it.
In the state variables $(1/\kappa_{\mathrm{wm}},B_{\mathrm{wm}})$ the neutral
line has slope $-1/(\ln(\Delta y/\delta)+\ln Re_\tau)$ (Eq. 12), which moves
with $Re_\tau$ and with the grid, while the learned boundary between raising
and lowering actions stays about the same. When the neutral line lies above
that boundary the mismatch is positive, and when it lies below, negative.
The precision of the "raise" action correlates with the sign and size of the
mismatch; accuracy (about 0.50 at all $Re_\tau$) and recall do not (Table III).

For the reinforcement-learning model BK22 the two sources report under
different conditions: Vadrot et al. (2023b) find a mismatch in LESGO with
$h_{\mathrm{wm}}=dz$, while [Bae & Koumoutsakos (2022)](/sources/bae-2022.md)
report mean profiles aligned with the log law from $Re_\tau=5200$ to $10^6$
in their own solver with $h_{\mathrm{wm}}=2\Delta y$, a matching height several
times larger in wall units at each common $Re_\tau$ *(compiler check, not in
the sources)*; Vadrot et al. attribute
the difference mainly to grid resolution. The comparison is a qualification
on the [machine-learning wall models](/methods/machine-learning-wall-model.md)
page, not a contradiction.

## Qualifications

- Vadrot et al. (2023b) are internally inconsistent about where BK22 errs:
  the abstract places the errors at $Re_\tau<10^3$ and $Re_\tau>10^6$, while
  their Table III gives $+1.5$, $+2.0$, $+2.0$ at $Re_\tau=2\times10^3$,
  $5.2\times10^3$, $10^4$, and §IV.C (l. 365) calls the mismatch at
  $Re_\tau=180$ and $10^3$ "small" although Table III gives $+2.2$ there.
- The slope wording of Vadrot et al. (§IV.C) — "decreases as the Reynolds
  number increases" — holds for the magnitude of the printed slope, which is
  negative and tends to zero as $Re_\tau$ grows *(compiler check, not in the
  sources)*.
- Carlsson et al. (2023, §4.3) cite "Fig. 4(b)" for both the $Re_\tau=2400$
  and the $Re_\tau=18\,000$ interface mismatch; the $Re_\tau=18\,000$ case is
  their Fig. 4(c).

# Citations

- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) — §I; §II.B.1, Table II; §III.A, Eq. (9); §IV.C, Eqs. (10)–(14), Table III.
- [Griffin et al. (2023)](/sources/griffin-2023.md) — §4.1, Figs. 13–15.
- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §VII.D, Figs. 8–10.
- [Fowler et al. (2022)](/sources/fowler-2022.md) — §1; §5.1.
- [Haering et al. (2022)](/sources/haering-2022.md) — §II.A; §II (SAS-F, Piomelli et al.); §V.A.1, Figs. 2–3.
- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) — §II.B.
- [Hoy & Bermejo-Moreno (2022)](/sources/hoy-2022.md) — §3.
- [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) — Methods, Eq. (10); Figs. 3–4.
- [Gillyns et al. (2022)](/sources/gillyns-2022.md) — §3, Eq. (4); §5; §7, Table 1.
- [Carlsson et al. (2023)](/sources/carlsson-2023.md) — §2, Eqs. (18)–(19); Table 1; §4.3, Table 2, Figs. 4–5.
- [Kim et al. (2022)](/sources/kim-2022.md) — §III E, Table IV.
- [Cai et al. (2022)](/sources/cai-2022.md) — §I; §II.C.1, Eq. (27).
