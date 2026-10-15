---
type: Method
title: "Re-entry capsule aerodynamics across flow regimes"
description: "Building a capsule aerodynamic database from free-molecular to continuum flow — Knudsen-number regime map, DSMC in rarefied flow, a sin²-of-log-Knudsen bridging function in the transitional regime, Newtonian and Navier–Stokes estimates in continuum flow — and using it with the ballistic coefficient for trajectory loads, static stability and trim."
status: established
aliases: [aerodynamic database, AEDB, bridging function, flow-regime map, modified Newtonian, Mach-number independence]
tags: [reentry, capsule, rarefied-flow, dsmc, bridging-function, stability, deployable-heat-shield]
timestamp: 2026-10-14T00:00:00Z
---

# Re-entry capsule aerodynamics across flow regimes

A capsule entering from orbit or a suborbital trajectory passes from
free-molecular through transitional to continuum flow, so its aerodynamic
database (AEDB) has to join methods valid in each regime.
[Fedele & Mungiguerra (2018)](/sources/fedele-2018.md) build such a database
(angle of attack 0–180° in 10° steps) for MINI-IRENE, a suborbital
demonstrator with a deployable heat shield (§5, Fig. 25), and use it for
trajectory and stability analysis.

## Flow-regime map

The regime is set by the Knudsen number based on a reference length (here
the capsule's maximum diameter), related to the freestream Mach and Reynolds
numbers by
$$\mathrm{Kn}_\infty=1.25\sqrt{\gamma}\,\frac{\mathrm{Ma}_\infty}{\mathrm{Re}_\infty}$$
([Fedele & Mungiguerra (2018)](/sources/fedele-2018.md), §5, Eq. 2). After
Bird, the flow is free-molecular above $\mathrm{Kn}_\infty\approx10$ and
continuum below about $10^{-3}$, transitional in between; the paper states
these limits as "Kn ≈ M/Re", dropping the factor $1.25\sqrt\gamma$. On the
MINI-IRENE trajectory from 250 km, the flow is free-molecular down to about
125 km, continuum from about 69 km, and turbulent below about 19 km (§5,
Fig. 23). Transition to turbulence is placed at a diameter-based freestream
Reynolds number of $5.0\times10^5$, justified by ARD post-flight data
(Eq. 3, stated without reference).

## Methods per regime

* **Free-molecular: DSMC.** DSMC drag at $\alpha$ = 0, 20 and 30° is linear
  in $\mathrm{Kn}_\infty$, rising from about 2 to about 6 over Kn 0–1400
  (Fig. 26, approximate reading).
* **Transitional: bridging function.** After Mitcheltree, each coefficient
  is the continuum value plus (free-molecular − continuum value) times
  $$\sin^2\left[\frac{\pi}{8}\left(3+\log_{10}\mathrm{Kn}_\infty\right)\right],\qquad 10^{-3}<\mathrm{Kn}_\infty<10,$$
  which gives the S-shaped $C_D(\mathrm{Kn})$ of Fig. 27 (Eqs. 7–8). The
  function is 0 at $\mathrm{Kn}_\infty=10^{-3}$ and 1 at
  $\mathrm{Kn}_\infty=10$.
* **Continuum: Newtonian estimate.** The stagnation pressure is taken as
  $\rho_\infty u_\infty^2$ (Newtonian $C_p=2$) in the trajectory model (§4).
  For a blunted cone, after Bertin, $C_D$ = 2 sin² of the cone half-angle +
  (nose radius / base radius)² × cos⁴ of the half-angle (Eq. 9); for
  MINI-IRENE (half-angle 45°, radius ratio about 0.44) the paper prints no
  value, and the formula evaluates to about 1.05 (reader's evaluation).
  Called "very preliminary".
* **Continuum: Navier–Stokes and panel methods.** Used by CIRA and UNINA;
  codes, grids and models are not stated.

## Mach-number independence

The continuum drag coefficient becomes independent of the Mach number from
about $\mathrm{Ma}_\infty=5$, the Oswatitsch principle (Fig. 28; approximate
readings: at 0° about 1.40 at Mach 2 to 1.29 at Mach 7, at 20° about 1.22 to
1.15, at 30° about 1.14 to 1.08)
([Fedele & Mungiguerra (2018)](/sources/fedele-2018.md), §5).

## Ballistic coefficient and loads

$\beta_B=m/(C_DS)$ ([Fedele & Mungiguerra (2018)](/sources/fedele-2018.md),
§1, Eq. 1). A lower $\beta_B$ lowers the peak stagnation pressure and heat
flux and moves the peaks higher (Fig. 2, illustrated); quoted values are
about 350 kg/m² (Apollo command module), about 430 kg/m² (Space Shuttle) and
25 kg/m² (IRENE target). For MINI-IRENE (8 kg, $C_D$ = 1.1, area
0.0491 m² closed and 0.342 m² deployed) the paper gives 142 kg/m² closed
(the printed inputs give 148) and 21 kg/m² deployed (§4.1).

A 3-DoF point-mass model (lift neglected, US1976 atmosphere, Tauber
stagnation-point heating) reproduces a DLR VSB-30 reference trajectory to
within 0.5% (§4). On the suborbital re-entry from 100.87 km at 1718.26 m/s
it gives peak deceleration about 10 times standard gravity, peak heat flux below 70 kW/m²
(near 50 km), peak temperatures about 973 K (700 °C), and peak dynamic pressure
1.8 kPa with constant $C_D$ or 2.2 kPa with the database $C_D$ (§4.1,
Figs. 10–14). Using a variable instead of a constant $C_D$ shortens the
flight by about 2 min and leaves the impact point within about 52 m
(Table 1). A LEO re-entry (120 km, 7600 m/s, −1°) with the same $\beta_B$
gives thermal loads almost an order of magnitude higher (§4.3).

## Static stability and trim

With the centre of gravity at 0.25 reference lengths, MINI-IRENE is
statically stable, $\partial C_m/\partial\alpha<0$, for $\alpha$ below about
50° ([Fedele & Mungiguerra (2018)](/sources/fedele-2018.md), §5, Fig. 29).
In free-molecular flow (250 km) it trims at 0° (stable) and 180°; in
hypersonic continuum flow it has three trim points, 0°, 140–150° (unstable;
150° at lower and 140° at higher hypersonic speeds) and 180°. The paper's
moment pole is at 0.35 reference lengths and it does not say which point
Fig. 29 refers to. Drop tests of a model downscaled by a factor of 1.5 self-aligned with the
flow within about 2.5 s from initial angles of 90° and 180° (§2, Fig. 6), and
earlier UNINA work found a 45° aero-brake half-cone more stable than a 60°
one (§2, attributed).

## Deployable heat shields

The IRENE concept uses an umbrella-like, mechanically deployed heat shield
(3 mm Nextel flexible layer, ceramic-foam nose) to reach a low $\beta_B$
([Fedele & Mungiguerra (2018)](/sources/fedele-2018.md), §1–3). The paper
judges a VSB-30 sounding-rocket flight not energetic enough to load the
thermal protection significantly, hence a plasma-wind-tunnel test
(SCIROCCO) of a ground demonstrator sized on the LEO re-entry; the open
shield diameter is given as 76 cm in §3, while the 0.342 m² reference area
corresponds to the 0.66 m reference diameter of §5.

# Citations

1. [Fedele & Mungiguerra (2018)](/sources/fedele-2018.md) — §1 (Eq. 1, Fig. 2), §2 (Figs. 5–6), §3, §4–4.3 (Figs. 10–22, Table 1), §5 (Eqs. 2–9, Figs. 23–29).
