---
type: Method
title: "Split convective forms"
description: "Split forms write the convective terms of the mass and momentum equations as weighted mixtures of divergence and advective forms; the page gives the Coppola–Veldman family, the weight conditions and duality relations under which a discretization conserves mass, momentum and kinetic energy, the dual-sided variant and the finite-volume face fluxes they correspond to."
status: established
aliases: [split forms, skew-symmetric form, Feiereisen splitting, Kennedy–Gruber splitting, KGP splitting, supraconservative discretization, dual-sided discretization]
tags: [kinetic-energy-preserving, finite-difference, finite-volume, turbulence, low-dissipation]
timestamp: 2026-10-21T00:00:00Z
---

# Split convective forms

A **split form** rewrites a convective term with the product rule before
discretizing. The divergence form $\partial_x(\rho v\phi)$ is replaced by a
weighted mixture of algebraically equivalent forms. These forms differ only
discretely, and the choice decides which quadratic invariants the
semi-discretization conserves.
[Coppola & Veldman (2023)](/sources/coppola-2023.md) treat the model pair

$$\partial_t\rho+\partial_x(\rho v)=0,\qquad \partial_t(\rho\phi)+\partial_x(\rho v\phi)=0,$$

whose primary invariants are $\rho$ and $\rho\phi$ and whose secondary
(quadratic) invariant is $\tfrac12\rho\phi^2$. Here $\phi$ is a page-local
transported scalar, and $\phi=v$ gives momentum and the kinetic energy
$\kappa$ (§2.1, after Veldman). The source writes the operators with
$\nabla$; the 1D form is shown here.

## The split family

Mass (Eq. (7)) has two forms:

- divergence: $M^D=\partial_x(\rho v)$;
- advective: $M^A=v\,\partial_x\rho+\rho\,\partial_xv$.

Momentum (Eq. (8)) has five:

- $C^D\phi=\partial_x(\rho v\phi)$;
- $C^\phi\phi=\phi\,\partial_x(\rho v)+\rho v\,\partial_x\phi$;
- $C^v\phi=v\,\partial_x(\rho\phi)+\rho\phi\,\partial_xv$;
- $C^\rho\phi=\rho\,\partial_x(v\phi)+v\phi\,\partial_x\rho$;
- $C^L\phi=\rho\phi\,\partial_xv+\rho v\,\partial_x\phi+v\phi\,\partial_x\rho$.

The family (Eq. (9)) mixes them with page-local weights. The mass weight
$\zeta$ is the source's $\xi$. The momentum weights
$\mu_D,\mu_\phi,\mu_v,\mu_\rho,\mu_L$, summing to 1, are the source's
$\alpha,\beta,\gamma,\delta,\varepsilon$:

$$M=\zeta M^D+(1-\zeta)M^A,\qquad C=\mu_DC^D+\mu_\phi C^\phi+\mu_vC^v+\mu_\rho C^\rho+\mu_LC^L .$$

For central finite differences on uniform grids, the family is
kinetic-energy-preserving iff

$$\mu_D-\mu_L=\mu_\phi=\tfrac12\zeta,\qquad \mu_v=\mu_\rho=\tfrac12(1-\zeta)-\mu_L$$

(Eq. (10), the condition of Coppola et al. 2019, recalled). The named
members have $\mu_L=0$:

| $\zeta$ | name | face mass flux $m_{i+1/2}$ (Table 1) |
|---|---|---|
| 1 | Feiereisen | $\tfrac12(\rho_{i+1}v_{i+1}+\rho_iv_i)$ |
| 1/2 | Kennedy–Gruber, shown kinetic-energy-preserving by Pirozzoli (KGP) | $\tfrac14(\rho_i+\rho_{i+1})(v_i+v_{i+1})$ |
| 0 | Coppola et al. | $\tfrac12(\rho_iv_{i+1}+\rho_{i+1}v_i)$ |

All three take the momentum flux
$(m\phi)_{i+1/2}=\tfrac12m_{i+1/2}(\phi_i+\phi_{i+1})$. The case $\zeta=\mu_D=1$,
with the rest zero, is the pure conservation form (§2.2).

## Discrete conditions in matrix form

Coppola & Veldman discretize on periodic, possibly non-uniform 1D grids as
$V\frac{d}{dt}\phi+\mathcal C\phi=0$. Here $V$ (page-local, the source's
$H$) is the diagonal matrix of control volumes and $\mathcal C$ the
discrete convective matrix. Every operator is a banded matrix in the
circulant shift $\mathcal T$, $(\mathcal T\phi)_i=\phi_{i+1}$ (page-local,
the source's $E$). The advective terms use up to four derivative matrices:

- $D^m$ (the source's $D^{\rho u}$), acting on the mass flux;
- $D^0$;
- $D^\rho$, gradient-like;
- $D^v$ (the source's $D^u$), divergence-like.

Their results:

- **Mass** (Observation 4, Eq. (43)). The advective form
  $V\frac{d\rho}{dt}=-\big(\mathrm{diag}(\rho)D^vv+\mathrm{diag}(v)D^\rho\rho\big)$
  conserves mass, globally and locally, iff the *duality relation*
  $D^\rho=-(D^v)^\top$ holds. This is a discrete product rule. A
  directionally biased $D^v$ must be paired with an oppositely biased
  $D^\rho$. If $D^\rho=D^v$, duality forces skew-symmetry.
- **Momentum** (Observation 6, Eq. (58)). The generalized momentum operator
  conserves momentum iff $\mu_L=0$, $D^0=-(D^m)^\top$ and
  $D^\rho=-(D^v)^\top$. $\mu_L\ne0$ would need an exact discrete product
  rule, which no nonzero matrix satisfies. The proof of this
  incompatibility is not printed (§4.2).
- **Kinetic energy** (§5.3, Observation 8). The weight conditions of
  Eq. (10) together with the duality relations are necessary and
  sufficient. This extends the 2019 result from skew-symmetric operators on
  uniform meshes to non-uniform meshes and to dual, non-central operators.
  For $\mu_L=0$, energy conservation implies momentum conservation, which
  implies mass conservation. For $\mu_L\ne0$, energy conservation does not
  imply momentum conservation.
- **Supraconservative family** (Eq. (73)). With $\mu_L=0$ the weights
  reduce to $\mu_D=\mu_\phi=\tfrac12\zeta$, $\mu_v=\mu_\rho=\tfrac12(1-\zeta)$. The
  most general finite-difference scheme that conserves mass, momentum and
  kinetic energy then has two free operators, $D^m$ and $D^v$, and the
  parameter $\zeta$.

**Finite-volume equivalence** (Observation 5, Eq. (53); §5.4). Every split
discretization that conserves mass globally is a cell-centred
finite-volume scheme with an explicit face flux, mapped coefficient by
coefficient ([local conservation and flux form](/results/local-conservation-flux-form.md)).

- **Three-point stencils.** The energy-preserving finite-difference schemes
  and the three-point finite-volume schemes with linear fluxes are the
  same three-parameter family.
- **Wider stencils.** The finite-volume framework is strictly larger. Face
  products such as $\rho_{i-2}v_{i-1}$ have no advective
  finite-difference counterpart.

## Dual-sided discretization

A *dual-sided* scheme pairs a directionally biased operator with its
negative transpose in the dual slot. An example is
$D^m=D^\rho=I-\mathcal T^{-1}$ (backward) with $D^v=D^0=-(I-\mathcal T^{-1})^\top$.
It satisfies the duality relations and so conserves mass, momentum and
kinetic energy. The traditional upwind scheme instead uses
$I-\mathcal T^{-1}$ in all four slots and conserves none of them, except
mass for $\zeta=1$ (§7.3, Fig. 3).

On 1D Euler acoustic-wave steepening, the formally first-order dual-sided
scheme behaves as follows (§8.2, Fig. 4):

- **Setup.** $N_x=32$, internal-energy formulation, $\zeta=1/2$, central
  pressure terms.
- **Conservation.** Mass, momentum and total energy are conserved to
  machine precision. First-order upwind loses $4.5\times10^{-3}$,
  $1.2\times10^{-2}$ and $1.5\times10^{-2}$ of them by $t=5$.
- **Shock profile.** After the shock forms ($t\approx3.5$), the dual-sided
  profile "nicely fits in between" the oscillating second-order central
  scheme and the smeared upwind scheme, with no artificial dissipation.

## Relation to flux-differencing DG

In nodal DG the same split forms arise from the choice of the symmetric
two-point volume flux in [flux differencing](/methods/flux-differencing.md)
([Ranocha et al. (2023)](/sources/ranocha-2023.md), §2, citing
Gassner–Winters–Kopriva). The Shima et al. flux yields a "standard split form
discretization" (§9). Coppola & Veldman remark that all prior studies of
split forms assumed central discretization, and that biased operators are
admissible once they satisfy the duality relations (§5.4). See
[entropy-conservative and kinetic-energy-preserving two-point fluxes](/methods/entropy-conservative-flux.md)
and [kinetic energy preservation](/properties/kinetic-energy-preservation.md).

## Qualifications

- The theory is for periodic 1D grids with exact time integration. The tests
  use classical RK4 with very small steps, and non-periodic boundaries are
  only pointed to (via SBP).
- The non-dissipative dual-sided shock profile is shown on one coarse 1D
  test. The paper makes no entropy-stability claim for it (§8.2).
- In their §7.3 tests with the central split family, weights violating
  Eq. (10) still conserve mass and momentum but lose kinetic energy at
  $O(10^{-3})$–$O(10^{-4})$. The variant $\mu_\rho=1$ ("$\delta=1$" in the
  source's letters) "turned out not always to be stable" (Fig. 2).

# Citations

- [Coppola & Veldman (2023)](/sources/coppola-2023.md) — §2.1–2.2 Eqs. (7)–(11), §3.3 Eq. (43), §3.4 Eq. (53), §4.2 Eqs. (56)–(58), §5.3–5.4 Eqs. (72)–(73) Table 1, §7.3 Figs. 2–3, §8.2 Fig. 4.
- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — §2, §9.
