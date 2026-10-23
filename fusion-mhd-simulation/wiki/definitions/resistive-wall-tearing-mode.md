---
type: Definition
title: "Resistive-wall tearing mode"
description: "A resistive-wall tearing mode is a tearing mode that is stable with an ideally conducting wall but unstable because its flux diffuses through a resistive wall; its growth time scales with the wall time, and it is proposed as the cause of the thermal quench in locked-mode disruptions, with a thermal quench lasting about half a wall time."
status: established
aliases: [RWTM, resistive wall tearing mode, wall-destabilized tearing mode]
tags: [tearing, wall, disruption, mhd, tokamak]
timestamp: 2026-10-16T16:51:00Z
---

# Resistive-wall tearing mode

A **resistive-wall tearing mode (RWTM)** is a
[tearing mode](/definitions/tearing-mode.md) whose tearing index with an
ideal wall at the wall radius is non-positive, so that it is stable if the
wall conducts perfectly, but which grows because its perturbed flux soaks
through a resistive wall on the wall time $\tau_w$
([Strauss et al. (2022)](/sources/strauss-2022.md), §I–II). The mode
differs from the resistive wall mode, an ideal external mode slowed by the
wall, by the presence of a resonant surface and a resistive layer inside
the plasma; the limit Eq. (5) below is described by the source as "a kind
of RWM with a rational surface in the plasma" (§II).

The concept matters for disruptions because Strauss et al. identify the
RWTM, not a critical island width, as the instability that produces the
[thermal quench](/definitions/thermal-quench.md) of locked-mode
[disruptions](/definitions/disruption.md) in DIII-D (shot 154576) and, in
earlier work by the same first author that is cited but not ingested, in
JET (§I).

## Cylindrical thin-wall theory

Symbols: $r_s$ the radius of the resonant surface and
$S_{\mathrm{wall}}\equiv\tau_w/\tau_A$ the wall Lundquist number (registry
§10); page-local $r_w$ the radius of the thin wall, $x_s\equiv r_s/r_w$, and
$\delta\psi$ the helical flux perturbation
$\propto\exp(\gamma t+im\theta+in\phi)$; and
$\tau_A=R_0/v_A$ is built on the major radius
([Strauss et al. (2022)](/sources/strauss-2022.md), §II).

**Wall condition.** Matching $\delta\psi$ continuously to a vacuum solution
$\propto r^{-m}$ outside a thin wall of resistivity $\eta_w$ and thickness
$d_w$ gives, at $r=r_w$,

$$\Big(1+\frac{\gamma\tau_w}{m}\Big)\delta\psi=-\frac{r_w}{m}\,\partial_r\delta\psi,\qquad \tau_w=\frac{\mu_0r_wd_w}{\eta_w}$$

(§II, Eq. 1). The ideal wall ($\tau_w\to\infty$) forces $\delta\psi(r_w)=0$;
no wall ($\tau_w\to0$) recovers the vacuum logarithmic derivative.

**Dispersion relation.** Combining the resistive-layer response with this
condition gives

$$(\gamma\tau_A)^{5/4}S^{3/4}=\Delta_i+\frac{\Delta_x}{\gamma\tau_A\,\hat S_{\mathrm{wall}}+1},$$

with the page-local quantities

$$\Delta_i\equiv\frac{r_s\Delta'_{\mathrm{ideal}}}{m},\qquad \Delta_x\equiv\frac{2x_s^{2m}}{1-x_s^{2m}},\qquad \hat S_{\mathrm{wall}}\equiv S_{\mathrm{wall}}\frac{1-x_s^{2m}}{2m},$$

where $\Delta'_{\mathrm{ideal}}$ is the tearing index $\Delta'$ computed with
an ideal wall at $r_w$; $\Delta_i$ measures ideal-wall tearing stability and
$\Delta_x$, which depends only on the geometry $x_s$, the destabilization
that the wall removes when it becomes transparent (§II, Eq. 2; the theory
is attributed to earlier cylindrical work, refs. 1 and 11 of the source).

**Limits** (§II, Eqs. 3–5; the compiler checked that each follows from
Eq. 2):

$$\begin{aligned}
&\hat S_{\mathrm{wall}}\to0\ \text{(no wall)}: && \gamma\tau_A=(\Delta_i+\Delta_x)^{4/5}S^{-3/5},\\
&\Delta_i=0,\ \gamma\tau_A\hat S_{\mathrm{wall}}\gg1: && \gamma\tau_A=\Delta_x^{4/9}S^{-1/3}\hat S_{\mathrm{wall}}^{-4/9},\\
&\Delta_i<0,\ \Delta_i+\Delta_x>0: && \gamma\tau_A=-\Big(1+\frac{\Delta_x}{\Delta_i}\Big)\hat S_{\mathrm{wall}}^{-1}.
\end{aligned}$$

The first is the classical $S^{-3/5}$ tearing scaling with the no-wall
index. The third does not contain the plasma resistivity: the growth is set
by the wall alone. No instability exists if $\Delta_i+\Delta_x<0$ (§II).
The source argues that two-fluid effects should be small, "particularly in
the limit (5) which does not contain the resistivity", and that the
residual rotation after locking does not stabilize the mode (§II).

## Onset condition: the q = 2 surface near the wall

The RWTM requires $\Delta_i\le0<\Delta_i+\Delta_x$. In a step-current model
(uniform current inside a radius set by $q_0$), for $(m,n)=(2,1)$,

$$\Delta_i=-2\,\frac{q_0-1-(q_0^2/4)\,x_s^4}{(1-x_s^4)\,\big(q_0-1-q_0^2/4\big)},$$

and $\Delta_i\le0$ requires $x_s^4>(4/q_0^2)(q_0-1)$
([Strauss et al. (2022)](/sources/strauss-2022.md), §IV, Eqs. 7–8). For
$q_0=1.05$ the threshold is $x_s=0.65$ (compiler's check: fourth root of
0.181). A DIII-D locked-mode database places the disruption boundary at a
normalized $q=2$ radius above 0.75, i.e. $x_s>0.625$ for a wall at about
$1.2a$; the simulated case has $x_s=0.67$, and the $q=2$ radius grows in
time during the locked mode (§IV). The source states the instability
condition in §IV as $\Delta_i\le0$ alone; the second condition
$\Delta_i+\Delta_x>0$ of §II is implicit.

## Simulation evidence (DIII-D shot 154576)

- **Linear, [M3D-C1](/software/m3d-c1.md) with a resistive wall.** The
  equilibrium reconstruction (no islands, $q_0>1$ imposed to suppress the
  1/1 mode) is unstable to a (2,1) mode with a resistive wall and stable
  with an ideal wall; the mode penetrates the wall. Over
  $S_{\mathrm{wall}}\approx50$ to $5\times10^4$, $\gamma\tau_A$ falls from
  ≈$6\times10^{-3}$ to ≈$6\times10^{-4}$ (read from the figure) and
  approaches $S_{\mathrm{wall}}^{-2/3}$, intermediate between the second and
  third limits above; the dispersion relation fits with $\Delta_x=1$,
  $\Delta_i=-1/5$ ([Strauss et al. (2022)](/sources/strauss-2022.md), §II,
  Fig. 2). The ideal-wall stability is stated, not plotted.
- **Nonlinear, [M3D](/software/m3d.md).** At $S=10^6$ and
  $S_{\mathrm{wall}}=10^3$–$3.3\times10^4$ the RWTM grows to large amplitude
  and causes a complete thermal quench by parallel heat transport along the
  stochastized field, with a dominantly (2,1) flux perturbation (§III,
  Figs. 3–4). The quench time follows $\tau_{\mathrm{TQ}}\approx3.4/\gamma$
  and the parallel transport time $a^2/(\kappa_\parallel b_n^2)$, with $b_n$
  the normalized normal field perturbation at the wall and $\kappa_\parallel$
  a diffusivity; at the experimental $S_{\mathrm{wall}}=1.2\times10^4$ it
  gives $\tau_{\mathrm{TQ}}\approx\tau_w/2$, as measured (§III, Eq. 6,
  Fig. 4b).
- **Amplitude.** The simulated peak transverse wall perturbation,
  $8.8\times10^{-3}$ of $B$, matches the measured $8.4\times10^{-3}$ (the
  measured (2,1) amplitude at $r_s$ mapped to the wall by $x_s^3$) (§III,
  Fig. 5).

The source explains why the mode reaches large amplitude: $\Delta_x$
depends only on $x_s$ and is "not saturated by local flattening of the
current profile", unlike $\Delta_i$ (§III, hedged as "may be").

## Consequence for ITER

Assuming the same ratio of thermal-quench time to wall time, the ITER wall
time of 250 ms gives thermal quenches of 75–125 ms (the range uses the JET
ratio 0.3 and the DIII-D ratio 0.5; 70 ms from an
$S_{\mathrm{wall}}^{4/9}$ scaling with a 500 eV edge), which would make ITER
disruptions "significantly more benign than previously predicted"
([Strauss et al. (2022)](/sources/strauss-2022.md), §V). This is an
extrapolation from two machines, and the ITER wall-time value conflicts
with other sources of this bundle; both points are recorded on
[thermal quench](/definitions/thermal-quench.md) and
[disruption](/definitions/disruption.md).

## Relation to other wall effects

The [resistive-wall coupling](/methods/resistive-wall-coupling.md) page
records JOREK–CARIDDI and JOREK–STARWALL tearing growth rates that move
between ideal-wall (≈630 s$^{-1}$) and no-wall (≈960 s$^{-1}$) values over a
wall-resistivity scan ([Isernia et al. (2023)](/sources/isernia-2023.md),
§V): there the mode is unstable in both limits. The RWTM is the regime in
which the ideal-wall limit is stable; the two results are compatible.

## Citations

- [Strauss et al. (2022)](/sources/strauss-2022.md), §I–V, Eqs. 1–8, Figs. 1–5.
- [Isernia et al. (2023)](/sources/isernia-2023.md), §V.
