---
type: Method
title: "HLLD Riemann solver"
description: "Four-intermediate-state HLL-type approximate Riemann solver for ideal MHD: constant normal velocity over the fan, states separated by the entropy wave and two Alfvén waves, exact for isolated contact, tangential and rotational discontinuities; Roe-level accuracy at lower cost; the base of UCT-HLLD."
status: established
aliases: [HLLD, multi-state HLL solver]
tags: [riemann-solver, godunov, mhd, shock-capturing, positivity, upwind-emf]
timestamp: 2026-10-13T00:00:00Z
---

# HLLD Riemann solver

[Miyoshi & Kusano (2005)](/sources/miyoshi-kusano-2005.md) extend the
[HLL](/methods/hll-solver.md) construction to 1D ideal MHD with **four**
intermediate states. The "D" stands for discontinuities: the solver
resolves isolated discontinuities exactly, not slow shocks.

## Construction

* **One assumption** (§5.1, eqs. 39–40): the normal velocity is constant
  over the Riemann fan, as in HLLC. Total pressure (gas plus magnetic) is
  then constant across the fan too. Slow shocks cannot form inside the fan;
  rotational discontinuities moving with the Alfvén waves can.
* **Five waves.** Two outer signal speeds bound the fan; the middle
  (entropy) wave moves with the common normal velocity; two Alfvén waves
  sit at the middle speed minus and plus $|B_n|$ over the square root of
  the adjacent outer-state density (eq. 51). They separate two outer and
  two inner states.
* **Closed-form states.** The middle speed and the fan's total pressure
  are the HLLC formulas with gas pressure replaced by total pressure
  (eqs. 38, 41). The outer states follow from the jump conditions across
  the outer waves (eqs. 43–48), the inner states from continuity across
  the middle wave plus the integral conservation law over the fan
  (eqs. 54–63): inner transverse velocity and field are square-root-density
  weighted averages of the outer ones with a $\mathrm{sign}(B_n)$ term.
  Density and total pressure do not jump across the Alfvén waves. All
  jump conditions of the approximate fan are satisfied.
* **Flux** (eqs. 64–66): six cases chosen by the signs of the five speeds.
* **Outer speeds** (p. 328): Davis, Einfeldt, or the simple bounds of their
  eq. 67 (extreme normal velocity plus or minus the larger fast speed);
  results with eq. 67 and Einfeldt's are "indistinguishable".

## Degenerate cases

* **Vanishing normal field.** For $B_n = 0$ the two Alfvén waves merge
  with the middle wave, the inner states are not needed, and the solver is
  HLLC's two-state structure; without any field it is HLLC (p. 328). The
  inner-state jump conditions "become unsolvable" at $B_n = 0$ (p. 326), so
  an implementation needs a switch.
  [Mignone & Del Zanna (2021)](/sources/mignone-2021.md) switch to the
  HLLC limit when the rotational speeds coalesce, at tolerance $10^{-9}$;
  that tolerance is theirs, not Miyoshi & Kusano's, who give none.
* **0/0 in the outer states** (p. 326), when the middle speed equals the
  adjacent normal velocity, the outer speed equals that velocity plus or
  minus the fast speed, the transverse field vanishes and
  $B_n^2 \ge \gamma p$: the outer transverse values are set to the
  unperturbed ones ("there is no shock across" that wave).

## Properties

* **Exact resolution** (§5.2): isolated contact, tangential and rotational
  discontinuities for any outer-speed estimate; an isolated fast shock only
  when the outer speed equals the shock speed. Slow shocks are not exact.
* **Positivity, one-dimensional and conditional** (§5.3). Densities are
  positive; pressures are positive if each outer speed exceeds the adjacent
  normal velocity by more than $\sqrt{(\gamma-1)/(2\gamma)}$ times the
  adjacent fast speed (the HLLC condition with the sound speed replaced by
  the fast speed), so the states lie in $\mathcal G$. The argument assumes
  in addition that the outer speed exceeds the middle speed by at least the
  fast speed, which the authors cannot confirm "at any situation" and check
  only for strong expansions; their conclusion is that HLLD "is thought to
  be a positively conservative scheme". They state that exact positivity
  in multi-D "may not be necessarily assured even in the HLLD solver"
  (§7). For the HLL consequence see
  [HLL Riemann solver](/methods/hll-solver.md).
* **Accuracy and cost.** First-order HLLD is "indistinguishable" from Roe
  on the Dai–Woodward tube, slightly more smeared at the slow compound wave
  of the $\gamma = 5/3$ Brio–Wu tube, and within 1% of Roe in temperature
  on Orszag–Tang up to $N = 400$; it keeps positivity on a Mach-3.1
  super-fast expansion where Roe with an entropy fix fails. Flux cost
  HLL : HLLD : Roe $= 1 : 1.35 : 2.67$, whole run $1 : 1.13 : 1.69$
  (§§6–7). [Stone et al. (2008)](/sources/stone-2008.md) give the same
  ranking: "about as accurate as Roe and much faster".

## Divergence constraint

In 1D the constraint is a constant $B_n$. Miyoshi & Kusano leave CT with
HLLD "beyond the scope" of their paper ("there are no general guidelines
to apply any one-dimensional MHD solver properly") and run their
multi-dimensional test with mixed
[GLM cleaning](/methods/glm-divergence-cleaning.md), parameters not
stated and no divergence measured (§6.2). Later sources supply the CT
coupling:
* **UCT-HLLD.** Mignone & Del Zanna derive HLLD's coefficients for their
  composition formula (eqs. 44–45), so an
  [upwind CT](/methods/upwind-constrained-transport.md) edge EMF is built
  from it. UCT-HLLD is their least dissipative stable EMF, and its
  dissipation does not depend on the 1D solver feeding the fluid.
* **Dissipation inherited by contact-mode EMFs.** With an HLLD base solver
  CT-Contact stays nearly ideal on a Harris sheet where it reconnects early
  with Roe: HLLD diffusion carries field jumps only into the EMF
  ([flux-CT](/methods/flux-ct.md)).

# Citations

1. [Miyoshi & Kusano (2005)](/sources/miyoshi-kusano-2005.md), §§5–7, eqs. 38–67, 88–100, Tables 1–2.
2. [Mignone & Del Zanna (2021)](/sources/mignone-2021.md), §§5–6, eqs. 44–45.
3. [Stone et al. (2008)](/sources/stone-2008.md), §4.3.
