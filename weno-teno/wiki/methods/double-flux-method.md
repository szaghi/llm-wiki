---
type: Method
title: "Double-flux method"
description: "The double-flux method removes the spurious pressure oscillations of conservative schemes at multicomponent material interfaces by computing each interface flux twice, once with the frozen mixture properties of each neighbouring cell; the page records Abgrall and Karni's algorithm as embedded in a weighted compact scheme, and the overspecification and conservation objections raised against it."
status: established
aliases: [double flux, double-flux algorithm, Abgrall–Karni double flux, quasi-conservative double-flux method]
tags: [multiphase, finite-difference, numerical-flux, interface-capturing]
timestamp: 2026-10-23T23:00:00Z
---

# Double-flux method

A conservative shock-capturing scheme for the
[multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)
with a ratio of specific heats that varies across a material interface
produces spurious pressure and velocity oscillations where the interface
moves, even when the interface is smooth; the
[pressure-equilibrium-preservation](/properties/pressure-equilibrium-preservation.md)
page records the analysis. The **double-flux method** of Abgrall and
Karni is one remedy. During a time step every cell sees a single fluid
with its own, frozen mixture properties, so each interface flux is
computed twice from the same reconstructed states, once with the
properties of each of the two cells; the mixture properties are updated
only at the end of the step, and the total energy recomputed from them.
The original paper is not a source of this bundle; the description below is that of
[Zhou, Ding, Huang & Luo (2023)](/sources/zhou-2023.md), who use it, and
the assessment is that of [Fujiwara, Tamaki & Kawai (2023)](/sources/fujiwara-2023.md),
who argue against it.

## The algorithm

For two species with mass fractions $Y_k$, molar masses $W_k$ and ratios
of specific heats $\gamma_k$ (registry §10), the mixture ratio is
$\gamma=\sum_k\frac{Y_k\gamma_k}{W_k(\gamma_k-1)}\Big/\sum_k\frac{Y_k}{W_k(\gamma_k-1)}$,
the ratio of the mixture's specific heats at constant pressure and
volume (Zhou et al. Eqs. 1–2). Zhou et al. (§4.3, Eq. 33) combine the
double-flux algorithm, after Abgrall & Karni, with their six-point
[weighted compact nonlinear scheme](/methods/weighted-compact-nonlinear-scheme.md):

- while node $i$ is advanced from $t^n$ to $t^{n+1}$ it sees one fluid
  with $\gamma=\gamma_i^n$;
- each midpoint flux is evaluated twice from the same interpolated
  states, $h(u^-_{i+1/2},u^+_{i+1/2};\gamma_i^n)$ for the update of node
  $i$ and $h(u^-_{i+1/2},u^+_{i+1/2};\gamma_{i+1}^n)$ for node $i+1$
  ([HLLC](/methods/hll-riemann-solvers.md) in their runs);
- $\gamma$ is updated only at the last Runge–Kutta stage, and the total
  energy is then recomputed with the new $\gamma$.

The same group had combined it with WENO before (Zhou et al. §4.3). On
the two-species Sod tube ($\gamma=1.4$ and $1.6$, 200 cells, CFL 0.2) the
expansion, shock and material interface are "accurately captured", and the WCNS-SA variant gives the thinnest interface of the
three six-point schemes compared (§5.4, Figs. 13–14;
[Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)); it is
also used on the Mach 1.22 [shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)
(§5.8).

## Two families and the overspecification objection

Fujiwara et al. (§1) place the method among the remedies for the
oscillations, with page-local $\mathsf G=1/(\gamma-1)$:

- **non-conservative schemes** solve the primitive-variable equations
  (Karni) or the transport equation of $\mathsf G$ instead of the
  species-mass equation (Abgrall; extended by Shyue and by Saurel et
  al.); citing Johnsen, the species-mass conservation errors of the
  latter grow in time;
- **double-flux methods**, proposed "to achieve the conservation of
  primary conservative variables", solve the pressure-evolution equation
  together with the total-energy equation (Fedkiw et al.; Karni), or the
  species-mass equation together with the $\mathsf G$ transport equation
  (Abgrall & Karni; Johnsen & Ham): "one extra transport equation is
  solved in addition to the conservation equations".

They state that double-flux methods "satisfy both the equilibrium and
primary conservation" but "overspecify the equations for the system":
two independent solutions of the pressure are obtained, from the
pressure and the total-energy equation (of the species mass in Johnsen &
Ham's variant), whereas analytically the solution is unique; a hybrid
that switches between "quasi-conservative double-flux" and a fully
conservative method does not, in their view, resolve the
overspecification (§1, §3). Their own answer is a fully conservative
central scheme that solves only the conservation laws of species mass,
momentum and total energy and preserves pressure equilibrium through a
discrete compatibility condition on the interface values
([pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md),
[split convective forms](/methods/split-convective-forms.md)); on their
smooth-interface advection tests the transport of $\mathsf G$ (NC-G)
keeps equilibrium but loses species-mass conservation (§4.1, Fig. 5).

## Qualifications

- In the form described by Zhou et al., the two fluxes of one interface
  differ wherever $\gamma_i^n\ne\gamma_{i+1}^n$, so the energy flux
  leaving node $i$ is not the one entering node $i+1$ and the update is
  not discretely conservative there *(compiler check, not in the
  sources)*; Zhou et al. do not discuss it. Fujiwara et al. state that
  double-flux methods satisfy "primary conservation" and, in the same
  paragraph, call the double-flux component of the hybrid method
  "quasi-conservative"; the bundle's sources give no conservation-error
  measurement of a double-flux scheme.
- Zhou et al.'s evidence is qualitative (profiles and the interface
  thickness of the two-species Sod tube); no pressure-error norm is
  reported.
- Fujiwara et al.'s alternative is non-dissipative and tested only on
  smooth interfaces; it is not a shock-capturing replacement of
  double flux (their §1, §6).

# Citations

- [Zhou, Ding, Huang & Luo (2023)](/sources/zhou-2023.md) — Eqs. (1)–(2); §4.3, Eq. (33); §5.4, Figs. 13–14; §5.8.
- [Fujiwara, Tamaki & Kawai (2023)](/sources/fujiwara-2023.md) — §1; §3; §4.1, Fig. 5; §6.
