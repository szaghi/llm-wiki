---
type: Definition
title: "Log-layer mismatch"
description: "The shift, in wall units, between the mean velocity of a wall-modelled or hybrid simulation and the logarithmic law in the log layer: how the sources measure it, the mechanisms they attribute it to, the remedies they use, and its appearance in learned wall models."
status: established
aliases: [LLM, log-layer shift, super-buffer layer error]
tags: [wmles, wall-model, hybrid-rans-les, boundary-layer]
timestamp: 2026-10-27T10:58:00Z
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

[Zangeneh (2021)](/sources/zangeneh-2021.md) (§I) gives the size of the
wall-stress error in hybrid RANS/LES wall modelling, citing the
literature: a skin friction "on the order of 15% too low" (after Nikitin et
al. 2000, as cited), and about 25 % under-prediction with IDDES in
supersonic boundary layers (Gieseking et al., as cited). In the review of
[Bose & Park (2018)](/sources/bose-2018.md) (§2.1, Fig. 4) the mismatch is
compiled from three WMLES that match at the first cell: a Mach 1.7
boundary layer at $Re_\theta=5\times10^4$ (Kawai & Larsson 2012, first
against third point) and channels at $Re_\tau=4000$ (Templeton et al. 2006)
and 2000 (Lee et al. 2013), as cited; the mismatch appears both in hybrid
RANS/LES (Nikitin et al. 2000) and in wall-stress WMLES (Cabot & Moin 2000;
Nicoud et al. 2001; Lee et al. 2013), with the largest errors in the first
cell.

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
  Bose & Park (2018, §2.1, Eq. 13) quantify the numerical part after Wu &
  Meyers (2013), as cited: for a log profile differenced at $y=d\,\Delta y$
  by an $n$th-order scheme the discrete mean shear is
  $(d\langle u\rangle/dy)\,(1+c_n n!/d^n)$, with $c_n$ the constant of the
  Taylor remainder (page-local $c_n$, $d$, $n$); in the first cell, $d=1/2$
  or 1, the remainder is large and does not vanish as $n$ grows. Kawai &
  Larsson (2012), as cited, found the Reynolds shear stress
  converged for $\Delta y/h_{\mathrm{wm}}\lesssim0.3$ — the "third grid point" —
  but advocate a matching height that is a fraction of $\delta$.
- **Instantaneous local use of a mean law.** [Fowler et al. (2022)](/sources/fowler-2022.md)
  (§1) recall the argument of Bou-Zeid et al. (2005): by the Schwarz
  inequality, applying the law of the wall locally and instantaneously
  over-predicts the mean wall stress. Bose & Park (2018, §2.1) state the same
  argument, citing Bou-Zeid et al. with the year 2004 (Fowler et al. print 2005): an algebraic model
  gives $\langle\tau_w\rangle\propto\langle u(h_{\mathrm{wm}})^2\rangle$ where
  the law of the wall gives $\langle\tau_w\rangle\propto\langle u(h_{\mathrm{wm}})\rangle^2$,
  and $\langle u^2\rangle>\langle u\rangle^2$, so that spatial filtering of the
  input relieves the mismatch.
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
  Bose & Park (2018, §2.1) summarize the mechanism of Yang, Park & Moin
  (2017) as an unphysically high correlation between the wall stress and the
  first-cell LES data, which damps the near-wall Reynolds shear stress and
  raises the velocity gradient; it "deviates from the common perception" that
  numerical or SGS errors near the wall are responsible, would unify the
  filtering and off-wall-matching remedies, but does not explain a
  *negative* mismatch (a velocity deficit), which remains unexplained. The
  control-based wall models they review point the same way: the computed
  streamwise stress correlates best with the LES streamwise fluctuations at
  the second wall-normal point, and with the matching point at the
  wall-adjacent cell, minimizing the deviation from a target profile
  necessarily over-predicts the near-wall intensities (Templeton et al.
  2008, as cited; §2.4).
- **Inconsistent RANS and LES eddy viscosities at the interface.**
  Zangeneh (2021, §II.C) argues, for an IDDES whose RANS inner layer is
  solved on an embedded grid, that the resolved velocity, density and
  temperature are identical in the LES and the RANS layer at the matching
  location, because the LES supplies them as boundary values, so the
  discrepancy in total shear stress and heat flux there "arises due to the
  discrepancies between $\mu_{t,\mathrm{LES}}$ and $\mu_{t,\mathrm{RANS}}$ and
  also $Pr_{t,\mathrm{LES}}$ and $Pr_{t,\mathrm{RANS}}$"; the paper gives no
  derivation. The author cites, without resolving it, that Peterson &
  Candler attributed the IDDES mismatch in supersonic boundary layers to the
  calibration of IDDES on low-speed channels, while Mockett et al. found it
  even in low-speed channel IDDES and suggested numerical sensitivity, so that
  "a concrete explanation … has remained elusive" (§I).
  [Heinz (2020)](/sources/heinz-2020.md) (§1) states, citing the
  literature, that the "fundamental inconsistency of RANS and LES equations"
  — LES equations produce fluctuations, RANS equations are not designed to
  deal with them — "is known to be the reason" that hybrid methods fail to
  obtain the logarithmic law of the wall.
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
- **SGS-dominated stress at the first off-wall points (disputed).**
  [Mukha et al. (2025)](/sources/mukha-2025.md) (§II.D, §III.B.2, §III.C)
  recall the framework of Brasseur & Wei, in which an SGS model introduces a
  spurious length scale (an "LES buffer layer") and the mismatch is avoided
  only if, among other criteria, the resolved shear stress dominates the
  modelled one at the first off-wall node. In their continuous
  spectral-element WMLES of channel flow at $Re_\tau\approx8000$ (polynomial
  degree $N=7$, [Nek5000](/software/nek5000.md)) the LES buffer layer is
  visible in the inner-scaled profiles and shrinks with refinement, but no
  mismatch appears on any of three meshes (2, 4 and 8 elements per $\delta$),
  although on the coarsest the SGS shear stress exceeds the resolved one near
  the wall; with the [Vreman](/methods/vreman-model.md) model, the sigma
  model or a high-pass relaxation filter on the finest mesh the mismatch is
  absent as well. They conclude that resolved-stress dominance "is not a
  necessary condition for capturing the log-layer" and that the result
  "appears to contradict the theory of Brasseur and Wei", while noting that
  only one of its three criteria was examined. Brasseur & Wei is not
  ingested here.

## Remedies used or recalled

| Remedy | Where |
|---|---|
| Match the wall model away from the wall, $h_{\mathrm{wm}}\ge3\Delta$ (Kawai & Larsson 2012) | recalled by Griffin et al. (2023, §4.1), who use $h_{\mathrm{wm}}=0.3\delta$ with 12 points per half-height; Agrawal et al. (2022, §VII.D) match at the second off-wall point of a staggered mesh |
| Filter the wall-model input in space (the "2Δ spatial filter" of Bou-Zeid et al. 2005) or in time and/or wall-parallel space (Yang, Park & Moin 2017) | recalled by Fowler et al. (2022, §1), who apply a "2Δ spatial filter, like that used in Bou-Zeid et al. (2005)" to $U_{\mathrm{LES}}$ (§5.1; their $\Delta$ is the matching height, the first grid point at half the wall-normal spacing); Vadrot et al. (2023b, §II.B.1, Table II) filter the input of their equilibrium model with a sharp filter of twice the grid spacing |
| Random forcing near the wall | recalled by Vadrot et al. (2023b, §I) |
| Third-point matching, $\Delta y/h_{\mathrm{wm}}\lesssim0.3$ (Kawai & Larsson 2012); adjusting the SGS eddy-viscosity coefficient from the turbulent-kinetic-energy budget (Wu & Meyers 2013); filtering the input (Bou-Zeid et al.) | recalled by Bose & Park (2018, §2.1), who note that in concave junctions a matching point a few cells off the wall is hard to combine with a fixed $h_{\mathrm{wm}}/\delta$ (Park & Moin 2016c, as cited) |
| Random-forest correction of the modelled wall stress and heat flux, fed back through corrected $\mu_t$ and $Pr_t$ | [Zangeneh (2021)](/sources/zangeneh-2021.md) (§II.F–G, §III.A, Fig. 6): removes the mismatch of an SST-IDDES WMLES of a Mach 1.69 flat plate at $Re_\theta=50\,000$ (below) |
| Stochastic forcing at the RANS/LES interface (Piomelli et al.) | recalled by Haering et al. (2022, §II): removes LLM but is problem-dependent; the SAS-F forcing of Menter et al. still showed LLM in channel flow |
| Several cells below the matching height: $h_{\mathrm{wm}}=0.1\delta_0$ with four uniform cells below it ($\Delta y=0.25h_{\mathrm{wm}}$), "to reduce numerical errors from the LES transferred to the wall model (Kawai & Larsson, 2012) and avoid the log-layer mismatch" | [Hoy & Bermejo-Moreno (2022)](/sources/hoy-2022.md) (§3), Mach 3 shock/boundary-layer interaction |
| Impose the wall stress through a wall eddy viscosity, $\nu_t\rvert_w=\tau^{\mathrm m}_w/\big(\rho\,(\partial u/\partial y)_w\big)-\nu$ with no slip kept ("viscosity augmentation"), instead of a Neumann condition | [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) (Methods, Eq. 10), stated, citing earlier work, to be "better at resolving the so-called log-layer mismatch"; $\tau^{\mathrm m}_w$ the modelled wall stress (page-local). In a continuous spectral-element code the same condition fails: Mukha et al. (2025, §III.D, Table IV, Figs. 9–10) find the mean velocity strongly under-predicted for $y^+\lesssim2500$ and over-predicted in the core, which they attribute to the lack of global momentum conservation of the discretization, not to a mismatch mechanism (see [wall-modelled LES](/methods/wall-modelled-les.md)) |
| Short exponential moving average of the wall-model input in time | [Gillyns et al. (2022)](/sources/gillyns-2022.md) (§3, §5, Eq. 4), who recall Yang et al. (2017) and Fowler et al. (2022) for time filtering; without it ($C_t=0$) their wall model diverged, which they attribute "most likely" to Gibbs oscillations at the element boundary, not to the mismatch. Mukha et al. (2025, §III.B.3, Table III, Figs. 4–5), in the same code, see no mismatch without averaging and no systematic gain a posteriori from averaging lengths of 5 to 500 time steps, although a priori the averaging reduces the wall-stress error; they call this "at odds with" Yang et al. (see [equilibrium wall model](/methods/equilibrium-wall-model.md)) |
| Elevating function $f_e$ of IDDES, which raises the RANS length scale near the RANS–LES interface, and the wall-distance-based subgrid length of IDDES, meant to "give a correct log-layer behavior in WMLES without the need to alter the value of the modeling constant" | recalled from Shur et al. (2008) by Carlsson et al. (2023, §2, Eqs. 18–19), who use IDDES; a small mismatch remains at the interface with their low-dissipation schemes (§4.3); recalled also by [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) (Eqs. 30–32; formulas of $f_e$ not printed) for their SST-IDDES in a lattice Boltzmann solver; [Wang et al. (2021)](/sources/wang-2021-l.md) (§1, §2.4, Eq. 20) choose the IDDES length $\tilde f_d(1+f_e)l_{\mathrm{RANS}}+(1-\tilde f_d)l_{\mathrm{LES}}$ for their Reynolds-stress-model hybrid because it avoids grid-induced separation and the mismatch "to a certain extent" (length scales and blending functions page-local, the functions not printed; no channel-flow test) |
| Redefine the states of a reinforcement-learning wall model so that the neutral line does not move with $Re_\tau$ | Vadrot et al. (2023a, §II.B.3, Eq. 10): removes the large-$Re_\tau$ mismatch of BK22 (below) |
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

Mukha et al. (2025, §II.C.1, §III.B, Fig. 3) match at $h_{\mathrm{wm}}=0.2\delta$
by spectral interpolation inside whichever element contains that height; on
their channel meshes of 4, 8 and 16 elements across $2\delta$ this lies inside
the wall-adjacent element on the two coarser meshes and in the second element
on the finest, for elements of equal height *(compiler check, not in the
sources)*. They see no mismatch on
any mesh and report that the argument against sampling inside the first
element, whose values are coupled to the first node, "is not borne out"
(§II.C.1, §V). Their indicator $\kappa y^+\,d\langle u\rangle^+/dy^+$ shows
derivative jumps at element boundaries that converge away only for
$y>0.25\delta$ on the two finer meshes, at the edge of the log layer
(§III.B.2).

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
times larger in wall units at each common $Re_\tau$ ($dz=\delta/(N_z-1)$
on LESGO grids of $24^3$–$72^3$, about $0.014\delta$–$0.043\delta$, against
$0.1\delta$) *(compiler check, not in the sources)*; Vadrot et al. attribute
the difference mainly to grid resolution. The comparison is a qualification
on the [machine-learning wall models](/methods/machine-learning-wall-model.md)
page, not a contradiction.

[Vadrot et al. (2023a)](/sources/vadrot-2023.md) retrain BK22 themselves in
LESGO at $Re_\tau=10^4$ ($48^3$ half-channel grid, $h_{\mathrm{wm}}=\Delta y$):
the retrained model no longer shows the low-Reynolds-number mismatch but
keeps the high-Reynolds-number one, and they ascribe the differences from
the original to the training Reynolds number, the RL settings and possibly
the solver (§II.B.2, Fig. 2). They restate the cause found in their survey:
the mismatch "does not result from directly using velocity at the first
off-wall grid point" but from the rotation of the neutral line with
$Re_\tau$, whose slope $-1/(\ln(\Delta y/\delta)+\ln Re_\tau)$ saturates at
large $Re_\tau$ and so explains why the mismatch saturates (§II.B.3, Eq. 9,
Fig. 3a). The cure is a change of state variable rather than of matching
height or input filter: with the first state
$(1/\kappa_{\mathrm{wm}}-1/\kappa)\ln h^+_{\mathrm{wm}}$ in place of
$1/\kappa_{\mathrm{wm}}$, the neutral line becomes the same straight line
for every $Re_\tau$, and the resulting model VYBA23 recovers the log law up
to $Re_\tau=10^{10}$ whenever $h_{\mathrm{wm}}$ lies in the log layer, while
BK22 keeps its large-$Re_\tau$ mismatch (Eq. 10, Figs. 3b, 6, 9). The
parameters of the agents barely move the mean velocity, except an action
interval above ten LES time steps; a smaller action range or an action
interval of five time steps gives less mismatch together with wall-stress
fluctuations closer to filtered DNS (§III.B, §IV, Figs. 9–10). The equilibrium
baseline of the same paper matches at $\Delta y/2$ with a filtered LES
velocity, after Yang et al. (2017) as cited, to remove its mismatch
(§II.B.1). For scale, they quote that a 2.5 % uncertainty in $\kappa$ alone
corresponds to about one to two wall units of mismatch (§III.B, after Yang
et al. 2019 as cited).

**A learned correction instead of a learned wall model.** Zangeneh (2021)
targets the mismatch of an SST-IDDES used as WMLES of supersonic flows with a
random-forest regression trained to predict the discrepancy of the modelled
wall stress and wall heat flux against DNS or experiment, from local mean
features on a seven-point stencil centred at the second off-wall point (see
[machine-learning wall models](/methods/machine-learning-wall-model.md)). On
a zero-pressure-gradient flat plate trained at $M=2.28$, $Re_\theta=5000$ and
predicted at $M=1.69$, $Re_\theta=50\,000$, the baseline IDDES has the right
log slope but a higher intercept, i.e. too low a skin friction, while the
corrected profile is "almost identical to the experimental result" of
Souverein et al. (as cited), with a log region over $30<y^+<3000$ "without
showing LLM" (§III.A.1, Fig. 6; van Driest-scaled velocity against
$\ln(y^+)/0.41+5.2$). The author calls it "a corrective approach and not
'standard' turbulence model" (§III): the correction is trained on the same
geometry at lower Reynolds number.

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
- [Vadrot et al. (2023a)](/sources/vadrot-2023.md) — §II.B.1–II.B.3, Eqs. (2), (9)–(10), Figs. 2–3; §III.A–III.B, Figs. 6, 9–10; §IV (arXiv v3).
- [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) — Eqs. (30)–(32) (HAL accepted manuscript).
- [Wang et al. (2021)](/sources/wang-2021-l.md) — §1; §2.4, Eq. (20).
- [Mukha et al. (2025)](/sources/mukha-2025.md) — §II.C.1; §II.D; §III.B.2–III.B.3, Table III, Figs. 3–5; §III.C–III.D, Table IV, Figs. 6, 9–10; §V (arXiv v1).
- [Bose & Park (2018)](/sources/bose-2018.md) — §2.1, Eq. (13), Fig. 4; §2.4.
- [Zangeneh (2021)](/sources/zangeneh-2021.md) — §I; §II.C; §II.F–G; §III, §III.A.1, Fig. 6.
- [Heinz (2020)](/sources/heinz-2020.md) — §1.
