---
type: Benchmark
title: "Turbulent boundary layers: zero and adverse pressure gradient, compressible"
description: "Spatially developing turbulent boundary layers on flat walls: the zero-pressure-gradient layer as a wall-model generalization test, adverse-pressure-gradient layers for the extent of the log law, supersonic and hypersonic layers on cooled walls as DNS databases for compressibility transformations, and the Mach 3 shock interaction for WMLES."
status: established
aliases: [TBL, flat-plate boundary layer, ZPG boundary layer, APG boundary layer, compressible turbulent boundary layer, hypersonic boundary layer, shock/boundary-layer interaction, STBLI]
tags: [benchmark, boundary-layer, compressible, hypersonic, dns, wmles]
timestamp: 2026-10-25T19:46:00Z
---

# Turbulent boundary layers: zero and adverse pressure gradient, compressible

A turbulent boundary layer grows along a wall under a free stream of
velocity $U_\infty$; $x$ is streamwise, $y$ wall-normal, $z$ spanwise. Unlike
the [channel](/benchmarks/turbulent-channel-flow.md) it is not homogeneous in
$x$: its thickness $\delta$ (the 99% thickness unless a page says
otherwise), displacement and momentum thickness $\delta^*$, $\theta$, and
$Re_\tau$ grow downstream, an inflow condition must supply turbulence, and
the outer layer meets a non-turbulent free stream. The pressure gradient
along the wall classifies it: zero (ZPG), adverse (APG, decelerating) or
favourable. At high Mach number the wall temperature becomes a parameter,
measured by the ratio $T_w/T_r$ of wall to recovery temperature
$T_r=T_\infty(1+r\frac{\gamma-1}2M_\infty^2)$ (recovery factor $r=0.89$ in
both compressible sources). In this bundle the case serves as a
generalization test for wall models trained in channels, as the data base of
wall laws under pressure gradient, and as a DNS database for compressible
wall scalings.

## Zero-pressure-gradient layer as a wall-model test

[Bae & Koumoutsakos (2022)](/sources/bae-2022.md) (preprint v1, Methods p.
14, Fig. 5) apply a log-law-based
[reinforcement-learning wall model](/methods/machine-learning-wall-model.md),
trained only in channel flow, to a flat-plate ZPG layer at
$Re_\theta=1000$–7000 without retraining. The WMLES domain is
$3570\theta_0\times100\theta_0\times200\theta_0$ ($\theta_0$ the inlet
momentum thickness) with recycling of the inflow at $890\theta_0$ (Lund et
al.), a top condition from the experimental displacement-thickness growth, a
convective outlet, and spanwise periodicity; at $Re_\theta=6500$ the spacing
is $\Delta x^+=128$, $\Delta z^+=105$, $\Delta y^+=64$, with about 10 points
per $\delta$ at the inlet and the matching height at the third point. The
predicted skin friction $C_f(Re_\theta)$ is comparable to the empirical
correlation of Schlichting & Kestin.

## Adverse pressure gradient: the extent of the log law

[Knopp (2022)](/sources/knopp-2022.md) analyses wind-tunnel mean-velocity
profiles of 2D incompressible smooth-wall APG layers at $Re_\theta>8000$:
the 1968 Stanford collection (Bradshaw, Clauser, Ludwieg & Tillmann, Perry,
Schubauer & Klebanoff, Schubauer & Spangenberg), Samuel & Joubert, Skare &
Krogstad, Marusic & Perry, a UNH experiment and two DLR/UniBw experiments,
plus a low-Reynolds-number experiment (Nagano et al., $481\le Re_\tau\le639$)
and a DNS with a separation bubble (Coleman et al., $Re_\tau$ up to 880) for
validation (§3, Table 1). The local parameter is the pressure gradient in
inner units, $\Delta p_s^+=\nu\,(dP/ds)/(\rho u_\tau^3)$ (page-local, $s$
the wall-tangential direction). The log law is robust in APG, but its outer
edge moves down relative to $\delta$ as $\Delta p_s^+$ grows: below
$0.11\delta$ for $\Delta p_s^+>0.005$ and below $0.08\delta$ for
$\Delta p_s^+>0.015$, never reaching $0.15\delta$ except in the mild
equilibrium flows (§5.2). Above it the profile turns upward and follows a
half-power law. The calibrated correlation and the half-power slope are on
[the wall law in adverse pressure gradient](/definitions/adverse-pressure-gradient-wall-law.md).
Only a few experiments reach $\Delta p_s^+>0.02$, and few exceed
$Re_\theta=30{,}000$ (Fig. 2).

## Supersonic and hypersonic layers on cooled walls (DNS)

| Case | Source | $M_\infty$ | $T_w/T_r$ | $Re_\tau$ range | Grid ($N_x\times N_y\times N_z$) |
|---|---|---|---|---|---|
| M2 low/high | [Cogo et al. (2022)](/sources/cogo-2022.md) | 2.00 | 0.76 | 340–620; 1240–2300 | $4096\times320\times512$; $16384\times832\times2048$ |
| M6 low/high | [Cogo et al. (2022)](/sources/cogo-2022.md) | 5.86 | 0.76 | 290–520; 1080–1953 | as M2 |
| M2p5HighRe | [Huang et al. (2022)](/sources/huang-2022.md) | 2.5 | 1.0 (adiabatic) | 395–1199 | three boxes, up to $5200\times680\times800$ |
| M5Tw091 | [Huang et al. (2022)](/sources/huang-2022.md) | 4.9 | 0.91 | 726–1244 | three boxes, up to $5000\times550\times600$ |
| M11Tw020 | [Huang et al. (2022)](/sources/huang-2022.md) | 10.9 | 0.20 | 672–1193 | three boxes, up to $6300\times690\times600$ |

The two databases join: the low-Reynolds-number Mach 5.86 case of Cogo et al.
matches case M6Tw076 of Zhang, Duan & Choudhari (2018), one of the five
earlier cases (Mach 2.5 to 14, $Re_\tau\le686$) that
[Huang et al. (2022)](/sources/huang-2022.md) reuse. Grid spacings are
$\Delta x^+\le7.9$, $\Delta z^+\le4.8$, $\Delta y^+_{\min}\le0.7$ with the
mean spacing below $4\eta$ ([Cogo et al. (2022)](/sources/cogo-2022.md),
Table 1) and $\Delta x^+\approx6.5$–7.8, $\Delta z^+\approx4.7$–6.6
([Huang et al. (2022)](/sources/huang-2022.md), Table 2; their grid counts
are reordered in the table above to $x\times y\times z$ with $y$
wall-normal). Cogo et al. use the GPU code STREAmS
(energy-preserving central schemes with WENO switched by a shock sensor);
Huang et al. a limiter-optimized seventh-order WENO scheme, or an
eighth-order split central scheme for the Mach 2.5 case. Wall temperature
alone does not fix the cooling effect: at equal $T_w/T_r=0.76$ the Mach 2
layers behave as more strongly cooled, which
[Cogo et al. (2022)](/sources/cogo-2022.md) relate to the lower Eckert
number (3.9 against 8.0; §3.1).

**Inflow and domain length.** Both use recycling–rescaling inflow, at
$80\delta_{\mathrm{in}}$ from the inlet in Cogo et al. Huang et al. measure
the induction length, the distance after which the momentum-integral
relation $C_f=2\,d\theta/dx$ holds to 5%: it grows from $20\delta_i$ at Mach
2.5 to $80\delta_i$ at Mach 14 ($\delta_i$ the inflow thickness), is one to
three eddy-turnover lengths $U_\infty\delta_i/u_{\tau,i}$, and is 15 to
$20\delta_i$ longer with digital-filter than with recycling inflow; the outer
layer recovers more slowly than the near-wall region (§3.1, Table 3, Fig.
2).

**Compressible velocity transformations.** The two sources agree on the
ranking of [compressible velocity transformations](/definitions/compressible-velocity-transformation.md)
at $Re_\tau$ up to about 2000 and 1200: the transformation of Volpiani et
al. and the total-stress transformation of Griffin, Fu & Moin collapse the
mean velocity onto the incompressible law through the viscous sublayer and
the log layer; van Driest and, more, Trettel–Larsson leave a scatter of the
log-law intercept in the hypersonic cases
([Cogo et al. (2022)](/sources/cogo-2022.md), §4, Fig. 8;
[Huang et al. (2022)](/sources/huang-2022.md), §4.1, Figs. 10–11). Huang et
al. rank the total-stress transformation best across the inner layer; Cogo
et al. find the two equivalent except in the wake and say their database
cannot decide between them. Both note that Trettel–Larsson collapses
cooled-wall channels, so the scatter is particular to boundary layers. For
the Mach 11 cold wall no clear log region appears up to $Re_\tau=1172$,
which Huang et al. attribute to reduced scale separation under strong
cooling (Fig. 11).

**Temperature–velocity relations and Reynolds analogies.** Both find the
generalized Reynolds analogy of Zhang et al. (2014) accurate: Walz's
relation stays within 3% at $T_w/T_r=0.76$
([Cogo et al. (2022)](/sources/cogo-2022.md), Fig. 9), and only the Zhang
et al. and Duan & Martin relations fit the Mach 11 cold wall
([Huang et al. (2022)](/sources/huang-2022.md), §4.3.1, Table 5). Huang et
al. also find the strong Reynolds analogy of Morkovin violated, with
velocity–temperature correlation about $-0.55$ for $y/\delta\gtrsim0.2$,
the modified analogy of Huang, Coleman & Bradshaw collapsing all cases, and
the Reynolds analogy factor $2C_h/C_f$ between 1.1 and 1.2 in the
hypersonic cold-wall cases (§3.2, §4.3.2).
See [Morkovin's hypothesis](/definitions/morkovin-hypothesis.md).

**Skin friction and shape factor.** [Huang et al. (2022)](/sources/huang-2022.md),
§3.2, Fig. 3, find that for $T_w/T_r\lesssim0.3$ the van Driest II
transformation over-predicts $C_f$ by up to 10–20% and Spalding–Chi
under-predicts it by 20–40%; van Driest II with the Smits et al. power law
is the best combination (within ±5% supersonic adiabatic, $-15\%$ to $-6\%$
hypersonic cold wall). The shape factor $\delta^*/\theta$ grows strongly
with Mach number and is best correlated by Hopkins et al. (§3.2, Fig. 5).

**Reynolds stresses and structure.** In Morkovin's density-weighted scaling
the Mach 2 stresses of [Cogo et al. (2022)](/sources/cogo-2022.md) agree
with incompressible DNS at matching $Re_\tau$, the streamwise peak rising with
Mach number, and the outer wall-normal and spanwise intensities fall at high
Mach and Reynolds number (§5.1). [Huang et al. (2022)](/sources/huang-2022.md)
find the peak locations collapse in semi-local units $y^*$, a logarithmic
decay of the normal stresses in the quasi-adiabatic cases (slope 1.03 and
intercept 2.39 for the streamwise one), and no such region for the Mach 11
cold wall (§4.2; see [attached-eddy hypothesis](/definitions/attached-eddy-hypothesis.md)).
Both find outer superstructures of length $O(10\delta)$ at all Mach numbers
([Cogo et al. (2022)](/sources/cogo-2022.md), §3.1;
[Huang et al. (2022)](/sources/huang-2022.md), §5). Strong cooling enlarges
near-wall streaks in wall units (semi-local spacing $\lambda_z^*\approx120$
at all Mach numbers) and removes the outer spectral peak and the outer
footprint on the wall stress (Huang et al., §5). At $T_w/T_r=0.76$ the
near-wall temperature streaks are hardly detectable at Mach 2 but strong at
Mach 6 (Cogo et al., §3.1, §5.4). Cogo et al. detect the
turbulent/non-turbulent interface with a density-weighted momentum defect
and find uniform momentum zones, 3.6 and 2.5 on average at Mach 2 and 6, and
for the first time uniform temperature zones, 5.9 and 4.9 (§3.2).

**Fluctuating wall quantities and budgets.** In
[Cogo et al. (2022)](/sources/cogo-2022.md) the pressure rms normalized by
$\tau_w$ is controlled by $Re_\tau$ and nearly independent of Mach number at
$T_w/T_r=0.76$ except very near the wall and in the free stream; the
semi-locally scaled dissipation is independent of Mach and Reynolds number
while production and transport keep a Mach dependence (§5.2–5.3). In
[Huang et al. (2022)](/sources/huang-2022.md) the wall-pressure rms over
$\tau_w$ is 2.6–2.8 for (nearly) adiabatic walls and about 3.6 and 4.5 for
the cold walls of Mach 6–8 and 11–14, and the wall shear-stress rms reaches
0.45–0.5 of its mean on cold walls (§3.2, Figs. 8–9). The two statements
concern different cooling levels.

## Shock/boundary-layer interaction

[Hoy & Bermejo-Moreno (2022)](/sources/hoy-2022.md) simulate a Mach 3
boundary layer ($\delta_0=4$ mm at the reference station, unit Reynolds
number $49.4\times10^6$ m$^{-1}$) hit by the oblique shock of a wedge that
rotates to 17.5°, over a rigid wall and over a flexible steel panel,
replicating the experiment of Daub et al. The
[wall-modelled LES](/methods/wall-modelled-les.md) uses the Vreman SGS model,
the equilibrium wall model of Kawai & Larsson matched at $0.1\delta_0$ with
four cells below it, digital-filter inflow, $\Delta x\approx0.08\delta_0$,
$\Delta z=0.05\delta_0$, about $2\times10^7$ cells for a $5\delta_0$
periodic span and $2\times10^8$ for the full span (§3). The full-span run
shows wall pressure and skin friction nearly two-dimensional (§4.1). Panel
flexibility moves separation about $3\delta_0$ upstream and lengthens the
separation from $7.8\delta_0$ to $12.6\delta_0$ (+60%), lowers the peak wall
pressure, shifts the dominant frequencies down, and lengthens the recovery
of the downstream boundary layer from $47\delta_0$ to $61\delta_0$ (§4.3).
At the separation shock the low-frequency band ($f\delta_0/U_\infty<0.05$)
carries about 70% of the wall-pressure power, against over 80% in the band
above 0.5 upstream (Fig. 10). The authors state that RANS cannot predict the
strong separation and low-frequency dynamics of such interactions and that
DNS and wall-resolved LES are too costly at the experimental Reynolds number
(§1).

## Qualifications

- Coordinate translation: [Huang et al. (2022)](/sources/huang-2022.md)
  write $y$ spanwise and $z$ wall-normal; this page uses $y$ wall-normal.
- Semi-local friction Reynolds number: [Cogo et al. (2022)](/sources/cogo-2022.md)
  evaluate it with free-stream properties, [Huang et al. (2022)](/sources/huang-2022.md)
  with boundary-layer-edge properties; the two agree where the edge state
  equals the free stream *(compiler check, not in the sources)*.
- The sources print the total-stress transformation in different but
  algebraically equivalent forms ([Cogo et al. (2022)](/sources/cogo-2022.md),
  Eq. 4.2, writes the mean shears as derivatives of transformed velocities;
  [Huang et al. (2022)](/sources/huang-2022.md), Eq. 4.4, with viscosity-ratio
  factors); the mapping is on
  [compressible velocity transformations](/definitions/compressible-velocity-transformation.md).
- [Cogo et al. (2022)](/sources/cogo-2022.md), Table 2, print for the low-Reynolds
  Mach 6 station $\delta^*/\delta=0.43$ and $\theta/\delta=3.2\times10^{-2}$
  with shape factor 10.9, while the ratio is 13.4; the other three rows
  agree with their printed shape factors within rounding *(compiler check,
  not in the sources)*.
- [Huang et al. (2022)](/sources/huang-2022.md) give $Re_\tau^*$ at the
  $Re_\tau=1172$ stations as 2626, 9178 and 6213 in §4.1 and 2761, 9114 and
  6149 in Table 4, and print "$Re_\tau=744$" in two figure legends for the
  774 station.
- [Knopp (2022)](/sources/knopp-2022.md) analyses measured mean profiles
  only; no turbulence model is run on these layers.
- [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) compare their skin
  friction with an empirical correlation, although the Reynolds-number range
  was chosen to match the DNS of Sillero et al.
- [Hoy & Bermejo-Moreno (2022)](/sources/hoy-2022.md) place the reference
  station at $x=210$ mm in §2 and at $x=200$ mm in the Table 1 caption and
  later in §2. Their structural-damping coefficient is fitted to the measured
  panel displacement of the same experiment (§3).

# Citations

- [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) — Results pp. 6–8, Fig. 5; Methods p. 14 (preprint v1).
- [Knopp (2022)](/sources/knopp-2022.md) — §3, Table 1; §5.1–5.2, Figs. 2, 4, 7–9.
- [Cogo et al. (2022)](/sources/cogo-2022.md) — §2, Tables 1–3; §3.1–3.2; §4, Figs. 8–9; §5.1–5.4.
- [Huang et al. (2022)](/sources/huang-2022.md) — §2, Tables 1–4; §3.1–3.2, Figs. 2–9; §4.1–4.3, Figs. 10–18; §5, Figs. 20–26.
- [Hoy & Bermejo-Moreno (2022)](/sources/hoy-2022.md) — §1–3, Tables 1–2; §4.1, §4.3, Figs. 4, 8–10.
