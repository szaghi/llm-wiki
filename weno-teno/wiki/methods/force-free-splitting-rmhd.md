---
type: Method
title: "Force-free splitting for relativistic MHD"
description: "Komissarov & Phillips split the electromagnetic field of ideal relativistic MHD into a force-free component and a plasma-inertia perturbation, integrate both conservation subsystems together and recombine them every step, with a thresholded energy transfer, so that conversion to primitive variables survives magnetizations far beyond those of unsplit schemes."
status: established
aliases: [splitting method for relativistic MHD, FFDE splitting, force-free degenerate electrodynamics splitting, split RMHD, background-field splitting]
tags: [relativistic, mhd, finite-difference, bound-preserving]
timestamp: 2026-10-23T15:06:00Z
---

# Force-free splitting for relativistic MHD

[Komissarov & Phillips (2024)](/sources/komissarov-2024.md) (arXiv v3 read)
write the electromagnetic field of ideal special
[relativistic MHD](/definitions/relativistic-hydrodynamics.md) as the sum of a
component that obeys force-free degenerate electrodynamics (FFDE) and a
perturbation due to the inertia of the plasma,
$B=B_{(0)}+B_{(1)}$ and, for the electric field,
$\mathcal E=\mathcal E_{(0)}+\mathcal E_{(1)}$, and integrate the two resulting
systems of conservation laws simultaneously (§2.2–2.3). At the end of every
step the two parts are added, the sum becomes the new force-free field and
the perturbation is reset to zero. The method generalizes Tanaka's
splitting off a static background field to a background that evolves by
FFDE (§1). Its purpose is robustness at high magnetization, where unsplit
conservative schemes fail to recover physical primitive variables.

Page-local symbols: $\mathcal E$ the electric field (registry §10, MHD
meaning), $W$ the Lorentz factor, $w_{\mathrm h}=\rho h_{\mathrm R}$ the
enthalpy density with $h_{\mathrm R}$ the relativistic specific enthalpy of
the relativistic page, $\sigma_{\mathrm M}=\lvert b\rvert^2/w_{\mathrm h}$ the
magnetization with $\lvert b\rvert^2=\lvert B\rvert^2-\lvert\mathcal E\rvert^2$,
$\mathsf e_{(s)}$ and $\mathsf s_{(s)}$ the energy and momentum densities of
subsystem $s=0,1$, and $\alpha_{\mathrm e}$ the energy-transfer threshold.
Units have $c=1$ and no $4\pi$.

## Why unsplit schemes fail at high magnetization

The authors attribute the failures to the integration of Faraday's law, not
of the energy–momentum equations, whose truncation errors are "the same as
in numerical relativistic hydrodynamics" (§2.1). When
$\sigma_{\mathrm M}\gg1$ the field dominates the total energy and momentum,
and the plasma part, obtained by subtracting the field part from the
conserved totals, inherits a field error amplified by $\sigma_{\mathrm M}$.
The plasma energy–momentum four-vector must stay time-like,
$W^2w_{\mathrm h}(2p-w_{\mathrm h})-p^2<0$ (Eq. (11)), and holding the total
fixed while perturbing $B$ along itself the state stays physical only if
the relative field error is below about $W^2/\sigma_{\mathrm M}$: the authors
print $\delta B/B\lesssim2W^2/\sigma_{\mathrm M}$ for velocity parallel to the
field and $\delta B/B\lesssim W^2/\sigma_{\mathrm M}$ for velocity perpendicular
to it (Eqs. (17), (20)). They use the error parameter
$(\delta B/B)\,\sigma_{\mathrm M}/W^2$, with $\delta B$ estimated from
$\nabla\cdot B$, to predict where the unsplit mode crashes (§5.6, Fig. 22):
it is much larger than one for a moving magnetic rope at start-up, about 4
for a cylindrical explosion with $B_0=1$ and about 20 near tearing current
sheets, and at most about 0.3 for an explosion with $B_0=0.1$, where the
unsplit mode succeeds.

## The two subsystems

**Force-free subsystem** (background, the authors' FFDE formulation of 2002;
§2.2, Eqs. (21)–(26)):
$$
\begin{aligned}
&\partial_tB_{(0)}+\nabla\times\mathcal E_{(0)}=0,\qquad
\partial_t\mathsf e_{(0)}+\nabla\cdot\big(\mathcal E_{(0)}\times B_{(0)}\big)=0,\\
&\partial_t\mathsf s_{(0)}+\nabla\cdot\Big[-\mathcal E_{(0)}\otimes\mathcal E_{(0)}-B_{(0)}\otimes B_{(0)}+\tfrac12\big(\lvert\mathcal E_{(0)}\rvert^2+\lvert B_{(0)}\rvert^2\big)I\Big]=0,
\end{aligned}
$$
with $\mathsf e_{(0)}=\tfrac12(\lvert\mathcal E_{(0)}\rvert^2+\lvert B_{(0)}\rvert^2)$,
$\mathsf s_{(0)}=\mathcal E_{(0)}\times B_{(0)}$ and the constraints
$\nabla\cdot B_{(0)}=0$, $\mathcal E_{(0)}\cdot B_{(0)}=0$,
$\lvert B_{(0)}\rvert>\lvert\mathcal E_{(0)}\rvert$. It is hyperbolic under the
last two, with fast and Alfvén pairs, and overdetermined: seven evolution
equations and one algebraic constraint for six unknowns, of which only two
energy–momentum components are independent.

**Perturbation subsystem** (contribution; Eqs. (27)–(33)). Faraday's law for
$B_{(1)}$, mass conservation $\partial_t(\rho W)+\nabla\cdot(\rho Wv)=0$, and
energy and momentum equations that contain the plasma terms
$w_{\mathrm h}W^2-p$, $w_{\mathrm h}W^2v$ and every field term that is linear
or quadratic in the perturbation, e.g. the energy density
$\mathcal E_{(0)}\cdot\mathcal E_{(1)}+B_{(0)}\cdot B_{(1)}+\tfrac12(\lvert\mathcal E_{(1)}\rvert^2+\lvert B_{(1)}\rvert^2)+w_{\mathrm h}W^2-p$
(Eq. (28)). The terms quadratic in the force-free field, which dominate at
high $\sigma_{\mathrm M}$, are absent, which is what reduces the effect of
FFDE truncation errors on the plasma (§2.2). The coupling is ideal Ohm's law
for the total field, $\mathcal E_{(1)}=-v\times B_{(1)}-(\mathcal E_{(0)}+v\times B_{(0)})$
(Eq. (33)).

**One step** (§2.3, Eqs. (34)–(46)):

1. set $B_{(0)}=B^n$, $\mathcal E_{(0)}=\mathcal E^n$, $B_{(1)}=\mathcal E_{(1)}=0$;
2. integrate the combined system for $(B_{(0)},\mathsf e_{(0)},\mathsf s_{(0)})$
   and $(B_{(1)},\mathsf e_{(1)},\mathsf s_{(1)},\rho W)$ over $\Delta t$;
3. recombine $B^{n+1}=B^{n+1}_{(0)}+B^{n+1}_{(1)}$ and likewise $\mathcal E$.

Switches select the subsystems: integrating subsystem 0 alone gives an FFDE
code, skipping it gives a standard unsplit RMHD code ("standard mode"), and
the comparisons below use the second (§2.3). The authors contrast the method
with [operator splitting](/methods/operator-splitting.md): operator splitting
handles stiffness from disparate time scales by successive integration of
reduced equations, this one handles stiffness from disparate magnitudes of
the contributions to the conserved quantities and integrates the whole
system at once (§6).

## Energy transfer at recombination

The force-free electric field is recovered from the momentum alone,
$\mathcal E_{(0)}=\mathsf s_{(0)}\times B_{(0)}/\lvert B_{(0)}\rvert^2$ (zero if
$B_{(0)}=0$), and rescaled to $0.9999\lvert B_{(0)}\rvert$ if it exceeds
$\lvert B_{(0)}\rvert$ (Eq. (47)). The force-free energy is therefore not
conserved: the deficit
$\delta\mathsf e_{(0)}=\mathsf e_{(0)}-\tfrac12(\lvert\mathcal E_{(0)}\rvert^2+\lvert B_{(0)}\rvert^2)$,
evaluated with the recovered field, is moved into the plasma energy
$\mathsf e_{(1)}$ only when
$$\delta\mathsf e_{(0)}>\alpha_{\mathrm e}\,\mathsf e_{(0)},\qquad\alpha_{\mathrm e}\ge0$$
(Eqs. (48)–(51)): $\alpha_{\mathrm e}=0$ transfers every positive deficit,
$\alpha_{\mathrm e}=1$ switches the transfer off, and the default is
$10^{-3}$. A positive transfer only heats the plasma, $\delta p=A_{\mathrm e}\,\delta\mathsf e_{(1)}$
with a coefficient $A_{\mathrm e}>0$ for $1<\gamma<2$ (page-local; derived for
an unmagnetized fluid at fixed mass and momentum), so it "should not result
in conversion failure"; a negative one could make the plasma four-vector
space-like and is not done (§2.4). The momentum mismatch is not transferred:
"We have not been able to find a suitable algorithm" (Eq. (52)). The scheme
thus gives up exact total-energy conservation by design, which the authors
consider "inevitable for high-σ RMHD anyway" (§1).

**Energy budget** (§4.2, Table 2, Fig. 5). On a one-dimensional
[Harris sheet](/benchmarks/tearing-mode-instability.md) ($B_0=500$, $p_0=\rho_0=1$,
500 points, sheet about four cells wide) the total energy, initially
$6.30\times10^7$, changes by $-7.81\times10^5$ (about 1 %) with
$\alpha_{\mathrm e}=1$ and by $+5.04\times10^4$ (about 0.09 %) with
$\alpha_{\mathrm e}=0$ by $t=4.5$. The transfer accounts for about 47 % of
the plasma heating; the rest comes from an uncontrolled channel, the
interaction and perturbation field energies zeroed at each recombination.
The threshold $10^{-3}$ suppresses parasitic heating in rarefactions while
keeping the current-sheet heating.

## Discretization used

The implementation is a third-order point-value
[conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
close to Del Zanna et al.'s ECHO, as the authors describe it (§3):

- [SSP-RK3](/methods/ssp-runge-kutta.md), $\Delta t=C\Delta x$ with $C=0.5$
  (0.4 in the Alfvén-wave test);
- interpolation of primitive variables, because interpolating conserved ones
  "may yield an unphysical state", by a new third-order WENO interpolation
  whose weights map second-order TVD weights with a scale-aware floor in the
  indicators (App. A; on [mapped WENO](/methods/mapped-weno.md) and
  [smoothness indicators](/definitions/smoothness-indicator.md));
- the [HLL flux](/methods/hll-riemann-solvers.md) with speeds $\pm1$ for the
  force-free subsystem and Gammie et al.'s approximate fast speeds for the
  perturbation;
- the DER flux-derivative step of Del Zanna et al., a central quartic
  interpolation of the interface fluxes that the authors call a "3rd-order
  approximation for $\nabla\cdot f$" (§3 (iv), Eqs. (61)–(63)), replaced by the
  first-order flux difference in a "safety zone" around detected strong
  shocks (compression with $\lvert\nabla\cdot(Wv)\rvert>0.5\lvert Wv\rvert$ and a
  total-pressure gradient above half the gas pressure, both by central
  differences); it was switched off for the tearing and later tests;
- [GLM divergence cleaning](/methods/glm-divergence-cleaning.md) in each
  subsystem separately (§3.1).

**Primitive recovery for the split variables** (contribution; §3.6, App. B).
The conserved variables are recombined and the recovery of Del Zanna et al.
is adapted: the unknown is $X=\lvert Wv\rvert^2-\lvert W_{(0)}v_{(0)}\rvert^2$, the
difference from the squared four-velocity of the force-free drift
$v_{(0)}=\mathcal E_{(0)}\times B_{(0)}/\lvert B_{(0)}\rvert^2$ (page-local), chosen
to avoid a cancellation multiplied by $\lvert B_{(0)}\rvert^2$. For each $X$ the
variable $w_{\mathrm h}W^2$ is the non-negative root of a cubic whose constant
term is non-positive, solved by a modified Cardano formula or by Blinn's
substitution; the outer equation is solved by the secant method from the
previous step's value, with a Brent–Dekker fallback on an exponentially
expanding bracket. The secant method needs at most 10 iterations "when σ is
not extremely large", Brent–Dekker up to 60 in extreme cases, and a
Monte-Carlo test found "not a single incident of convergence failure"
(Fig. 1). The terms of order $\lvert B\rvert^4$ cancel analytically (Eq. (B23)).

## Evidence

- **High-magnetization accuracy.** A boosted large-amplitude Alfvén wave at
  $\sigma_{\mathrm M}=545$ converges at third order, $L_1(B_2)$ orders 3.5,
  3.1, 3.0, 3.1 from $N_x=20$ to 320 (Table 1;
  [circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md)).
- **Shocks.** Low- and high-magnetization fast and slow shocks
  (upstream $\sigma_{\mathrm M}$ from $10^{-4}$ to $10^3$ in Table 4; the text gives
  $10^{-3}$ for the sub-relativistic FS9) are captured well; with the energy
  transfer off the gas pressure behind the $\sigma_{\mathrm M}=10^3$ fast shock
  is about 20 % low. The same shock in the upstream rest frame, moving at
  nearly the speed of light, fails in the plasma variables, with a gas
  pressure more than ten times the exact one, which the authors attribute to
  "about one hundred times stronger numerical magnetic dissipation" (§4.5,
  Fig. 11).
- **Multidimensional runs the unsplit mode cannot do.** A moving Lundquist
  rope ($v=0.8$, $\sigma_{\mathrm M}\approx2000$, $200^2$, $t=5$) keeps pressure
  errors within 8 % with field errors "hardly visible", while the standard
  mode crashes at the start even at $C=0.01$; a cylindrical
  [explosion](/benchmarks/mhd-blast-wave.md) runs up to $B_0=10^3$ (ambient
  magnetization $4.5\times10^9$) with $C=0.1$ for the first steps, while the
  standard mode crashes from $B_0=1$ (§5.1, §5.3).
- **Cost.** On the $B_0=0.1$ explosion, $200^2$ to $t=4$: 24 CPU seconds
  (134 steps) on one core of an Apple M2, the standard mode being only about
  20 % faster; variable conversion takes about 36 % of the run time (§5.3).
- **Reconnection.** Harris-sheet tearing at $\sigma_{\mathrm M}=5\times10^4$
  and an ABC grid of ropes are compared with tearing theory and with
  particle-in-cell results ([tearing-mode instability](/benchmarks/tearing-mode-instability.md));
  the numerical resistivity that drives them is calibrated as
  $\eta_{\mathrm{num}}\approx0.031\,L(\Delta x/\Delta t)(\Delta x/L)^3$, with $L$ the
  field length scale and a factor 2 smaller at 45° to the grid (§4.3, §5.2;
  [numerical dissipation](/definitions/numerical-dissipation.md)).

## Qualifications

- **Conservation.** Total energy is not conserved by design, and the momentum
  mismatch is discarded. The bundle's physical-constraint-preserving RMHD
  schemes ([bound preservation](/properties/bound-preservation.md),
  [geometric quasilinearization](/methods/geometric-quasilinearization.md))
  stay conservative and limit towards the admissible set instead; no source
  compares the two approaches on a common test.
- **Scope of the robustness claim.** Conversion failures are eliminated
  "almost completely" with the energy transfer (§2.4); the evidence is the
  test suite above, without a proof that the recovered state is admissible.
- **Printed values.** §4.2 prints the 1D Harris-sheet magnetization as
  54500; with $w_{\mathrm h}=\rho+4p=5$ for $\gamma=4/3$ it is
  $500^2/5=5\times10^4$, the value §5.4 prints for the same $B_0$, $p_0$,
  $\rho_0$ *(compiler check, not in the sources)*. §4.5 prints the upstream-frame
  shock speed as $-0.99968$; composing $-0.5$ with the upstream velocity
  $0.99968283$ gives $-0.999894$, the value of Table 4 *(compiler check, not in
  the sources)*.
- The version read is the post-referee arXiv v3; locators are those of the
  preprint.

# Citations

- [Komissarov & Phillips (2024)](/sources/komissarov-2024.md) — arXiv v3: §1; §2.1–2.4, Eqs. (8)–(52); §3, §3.1–3.6, App. A–B (Eq. (B23)); §4.1–4.5, Tables 1–4, Figs. 1, 5, 11; §5.1–5.6, Fig. 22; §6.
