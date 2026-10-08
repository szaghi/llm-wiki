---
type: Method
title: "Eight-wave formulation"
description: "Powell's non-conservative source-term formulation: advects divergence errors with the flow, holding the constraint to truncation error only."
status: established
aliases: [Powell source terms, 8-wave]
tags: [eight-wave, source-terms, divergence-constraint, shock-capturing]
timestamp: 2026-10-08T00:00:00Z
---

# Eight-wave formulation

Powell's modification of the conservative MHD system
([Powell et al. (1999)](/sources/powell-1999.md)): the equations are solved
in their **symmetrizable form** — Godunov's result that pure divergence form
is not symmetrizable, and becomes so exactly when a multiple of
$\nabla\cdot\mathbf{B}$ is added to each equation. The added source terms
(momentum, induction, energy rows) give the Roe-type Riemann solver an
eighth wave: the *divergence wave*, advecting at the flow speed $u$.

## The analytical mechanism

With the source terms,
$$\partial_t(\nabla\cdot\mathbf{B}) + \nabla\cdot(\mathbf{u}\,\nabla\cdot\mathbf{B}) = 0,$$
i.e. $\nabla\cdot\mathbf{B}/\rho$ is a passively convected scalar: clean
initial and boundary data stay clean along particle paths, to truncation
error. Divergence errors are not eliminated but *advected with the flow*,
preventing local accumulation. What the symmetrizable form buys: Galilean
invariance, an entropy conservation law, and no zero eigenvalue in the flux
Jacobian — none of which the unmodified conservative system has. Known
ambiguity, acknowledged in the primary source: isolated recirculating
regions cut off from boundaries. Discretely, the cell source uses the
face-integral divergence
$\frac{1}{V_i}\sum_{\text{faces}} \mathbf{B}\cdot\hat{n}\,dS$ — evaluated as
a source, never held as an invariant; the constraint guarantee is the
weakest among the families compared by [Tóth (2000)](/sources/toth-2000.md).

## Properties, per [Tóth (2000)](/sources/toth-2000.md)

* **Non-conservative — with consequences.** By the Lax–Wendroff theorem only
  conservative schemes are guaranteed correct jump conditions; Tóth's rotated
  shock-tube test demonstrates the failure concretely: across strong
  discontinuities the source terms produce **incorrect jumps that do not
  converge away with resolution**, even though the solution appears to
  converge normally.
* **Grid-agnostic and simple:** no staggering, no elliptic solve; usable on
  any grid type; requires only source terms and a Riemann-solver
  modification of the base scheme.
* **Usually adequate:** in most of the ten test problems it "works
  correctly" with small divergence errors and competitive accuracy — the
  failure mode is occasional, not generic.
* Initial/boundary data must satisfy the constraint to second-order accuracy
  (contrast the roundoff-exact compatibility CT requires:
  [exact discrete divergence](/properties/exact-discrete-divergence.md)).

**Positivity, a second argument for the source term** (alongside Derigs et al.'s thermodynamic one).
[Wu & Shu (2018)](/sources/wu-shu-2018.md) prove that LF-type DG schemes for the
symmetrizable form are positivity-preserving at any order. The schemes
discretize the source term as a penalty, from $D_h^{\mathrm{c}}$ at first order
and from normal-field jumps at faces at high order, and use a locally
divergence-free basis. The proof needs no discrete divergence-free
condition. The conservative form provably needs one
([positivity–divergence coupling](/results/positivity-divergence-coupling.md)).
This weighs against Tóth's wrong-jump result rather than closing it:
Wu & Shu concede the loss of conservation, and they run no
jump-convergence test of the kind Tóth used.

The conservation trade-off is stated openly in the primary source: local
conservation errors are accepted in exchange for symmetrizability. Tóth's
rotated shock-tube result is the concrete realization of the risk that trade
admits — the two sources agree on the mechanism and differ in emphasis on
how often it bites.

[GLM cleaning](/methods/glm-divergence-cleaning.md) later kept the
advect-the-error philosophy while removing the trade: its source term sits
only in the unphysical $\psi$ equation, leaving the physical conservation
laws intact; in the Dedner et al. comparisons GLM is more robust than the
Powell source terms with significantly smaller divergence errors
([Dedner et al. (2002)](/sources/dedner-2002.md)).

A sharper attack targets the *motivation*:
[Balsara (2004)](/sources/balsara-2004.md) (his "Issue 3") notes the
eighth wave exists to handle the jump in the normal field component at
zone faces, which makes seven-wave Riemann solvers ill-defined — but
[divergence-free reconstruction](/methods/divergence-free-reconstruction.md)
keeps that component $C^0$-continuous by construction, "thereby
eliminating the need for an eight-wave model" (with the absence of
physical magnetic monopoles invoked against monopole-introducing source
terms). The critique removes the premise, not the scheme: the eight-wave
formulation remains valid where cell-centered storage is a hard
requirement.

# Citations

1. [Powell et al. (1999)](/sources/powell-1999.md), §§2–3.
2. [Tóth (2000)](/sources/toth-2000.md), §§2–3, 6.3, 7.
3. [Dedner et al. (2002)](/sources/dedner-2002.md), §5.
4. [Balsara (2004)](/sources/balsara-2004.md), §1 (Issue 3).
5. [Derigs et al. (2018)](/sources/derigs-2018.md) — thermodynamic
   rederivation: allowing $\nabla\cdot\mathbf{B}\ne 0$ from first
   principles *produces* the non-conservative terms, recasting them as
   required physics wherever the constraint is not pointwise exact
   (the strongest published defense of the source-term family).
6. [Wu & Shu (2018)](/sources/wu-shu-2018.md), §§1, 3, 5.
