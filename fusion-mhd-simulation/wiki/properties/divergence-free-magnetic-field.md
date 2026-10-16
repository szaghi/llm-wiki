---
type: Property
title: "Divergence-free magnetic field"
description: "The constraint ∇·B = 0 and how the MHD codes of this bundle hold it: exactly by construction when B is the curl of a vector potential or a sum of terms ∇a×∇b plus a harmonic gradient (JOREK, M3D-C1, VMEC/DESC), to machine precision with an analytic harmonic vacuum potential (JOREK3D), or approximately with divergence cleaning when B is evolved directly (NIMROD)."
status: established
aliases: [solenoidal magnetic field, div B = 0, magnetic divergence constraint]
tags: [mhd, numerics, finite-elements, stellarator]
timestamp: 2026-10-16T20:00:00Z
---

# Divergence-free magnetic field

Faraday's law preserves $\nabla\cdot\mathbf B=0$ if it holds initially,
since $\partial_t(\nabla\cdot\mathbf B)=-\nabla\cdot(\nabla\times\mathbf E)=0$.
A discretization holds the constraint exactly only if this identity
survives discretization. The codes in this bundle use three strategies.

## 1. Representations that are divergence-free identically

Both $\nabla\cdot(\nabla\times\mathbf A)=0$ and
$\nabla\cdot(\nabla a\times\nabla b)=0$ hold for any smooth $\mathbf A$,
$a$, $b$. A field built only from such terms, plus the gradient of a
harmonic function, is solenoidal by construction.

* **Vector-potential full MHD.** JOREK's full model evolves $\mathbf A$ in
  the Weyl gauge with $\mathbf B=F\nabla\phi+\nabla\times\mathbf A$; $F$ is
  an axisymmetric equilibrium function, so $\nabla\cdot(F\nabla\phi)=0$, and
  $\mathbf B$ is "divergence-free by construction"
  ([Bhole et al. (2023)](/sources/bhole-2023.md), Eqs. 8–10;
  [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), Eq. 5). M3D-C1 also
  advances $\mathbf A$, written through scalar potentials
  ([Artola et al. (2021)](/sources/artola-2021.md), §2;
  [Zhang et al. (2021)](/sources/zhang-2021.md), §2). The JOREK and M3D-C1
  elements are $G^1$ and $C^1$ ([Artola et al. (2021)](/sources/artola-2021.md),
  Table 1), so first derivatives, and with them $\nabla\times\mathbf A$,
  are continuous across element boundaries except where that continuity is
  not enforced: in JOREK, at the magnetic axis and near X-points
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §3.1; the inference
  from continuity to a continuous $\mathbf B$ is the compiler's).
* **Reduced MHD.** $\mathbf B=F_0\nabla\phi+\nabla\psi\times\nabla\phi$ is
  solenoidal for any $\psi$ because $\nabla^2\phi=0$ away from the axis
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), Eq. 25;
  [Isernia et al. (2023)](/sources/isernia-2023.md), Eq. 1; see
  [reduced MHD](/methods/reduced-mhd.md)). Linear ordering-based models
  write the perturbed field as $\nabla\times(\delta A_\parallel\mathbf b)$
  with $A_\parallel=\mathbf A\cdot\mathbf b$
  ([Jiang et al. (2024)](/sources/jiang-2024.md), Eqs. 1, 4).
* **Inverse equilibria.** VMEC and DESC write
  $\mathbf B=\nabla\psi_t\times\nabla\theta^*+\nabla\phi\times\nabla\psi$,
  a sum of two terms $\nabla a\times\nabla b$
  ([Panici et al. (2023)](/sources/panici-2023.md), Eqs. 3.4, 3.22; see
  [inverse equilibrium solvers](/methods/inverse-equilibrium-solvers.md)).
* **Eigenvalue codes.** SCELT imposes $\nabla\cdot\mathbf B=0$ as an
  equation of its linear system and uses it to eliminate the toroidal
  field perturbation, leaving the radial and poloidal components as
  unknowns ([Ma & Guo (2022)](/sources/ma-2022.md), Eqs. 7–8).

## 2. Harmonic vacuum potential (stellarators)

In stellarator reduced MHD, $\mathbf B=\nabla\chi+\nabla\psi_\chi\times\nabla\chi$,
so $\nabla\cdot\mathbf B=\Delta\chi$. The constraint holds exactly only if
the represented coil potential is harmonic. JOREK3D uses analytic
[Dommaschk potentials](/methods/dommaschk-potentials.md), each satisfying
$\Delta\chi_{nm}=0$, so $\nabla\cdot\mathbf B=0$ holds "to machine
precision". A finite-element $\chi$ on the $G^1$ elements would not be
exactly harmonic and would make the advective terms discontinuous
([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), §II–III; see
[reduced MHD for stellarators](/methods/stellarator-reduced-mhd.md)).
[Ramasamy et al. (2024)](/sources/ramasamy-2024.md) (§2.2) replace the
Dommaschk representation "in all simulations" by a finite-element $\chi$
obtained from a Poisson problem with $\mathbf n\cdot\nabla\chi=0$ on the
boundary, for robustness in highly shaped devices. For that $\chi$,
$\nabla\cdot\mathbf B_{\rm vac}=\Delta\chi=0$ holds only in the weak
(Galerkin) sense, not to machine precision; the source does not state the
resulting error (compiler's observation). The disagreement with Nikulsin et
al. over the finite-element $\chi$ is recorded on
[Dommaschk potentials](/methods/dommaschk-potentials.md).

## 3. Evolving B with cleaning

NIMROD evolves the components of $\mathbf B$ on $C^0$ spectral elements
through Faraday's law ([Taheri et al. (2022)](/sources/taheri-2022.md),
Eq. 18); $\nabla\cdot\mathbf B$ "is not identically zero" and is
controlled by a diffusive correction proportional to
$\nabla(\nabla\cdot\mathbf B)$ added to Faraday's law
([Artola et al. (2021)](/sources/artola-2021.md), §2). The NIMROD runs with
neoclassical closures write that correction as $D_B\nabla\nabla\cdot\mathbf B$
with a page-local cleaning diffusivity $D_B$
([Howell et al. (2022)](/sources/howell-2022.md), Eqs. 1–10), and the
two-fluid runs also apply divergence cleaning, with no value given
([Ebrahimi & Bhattacharjee (2023)](/sources/ebrahimi-2023.md), p. 2, Eqs. 1–6); see the
variants table on
[visco-resistive MHD](/methods/visco-resistive-mhd-model.md). CLT advances
$\mathbf B$ with fourth-order finite differences
([Zhang et al. (2021)](/sources/zhang-2021.md), Eq. 1.4, §2); the source
does not say how $\nabla\cdot\mathbf B$ is controlled there.

## The companion constraint on the current

With $\mu_0\mathbf J=\nabla\times\mathbf B$, $\nabla\cdot\mathbf J=0$
follows. In JOREK's reduced model it is not built into the representation
but held in weak form: the vorticity equation is the weak form of
$\nabla\cdot\mathbf J=0$, and the poloidal current can be reconstructed
from the momentum equation ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md),
§2.3.3, Eq. 43). In the virtual-casing coupling of JOREK and CARIDDI the
equivalent surface current can represent only solenoidal currents inside
the MHD domain. Halo currents crossing the boundary are therefore excluded
([Isernia et al. (2023)](/sources/isernia-2023.md), §II C, §VII; see
[resistive-wall coupling](/methods/resistive-wall-coupling.md)).

# Citations

* [Ramasamy et al. (2024)](/sources/ramasamy-2024.md) — finite-element Poisson vacuum potential.
* [Nikulsin et al. (2022)](/sources/nikulsin-2022.md) — harmonic vacuum potential and machine-precision $\nabla\cdot\mathbf B$.
* [Bhole et al. (2023)](/sources/bhole-2023.md) — divergence-free field by construction in JOREK full MHD.
* [Artola et al. (2021)](/sources/artola-2021.md) — field representations of JOREK, M3D-C1, NIMROD; NIMROD cleaning.
* [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — field ansatz and weak $\nabla\cdot\mathbf J=0$ in reduced MHD.
* [Howell et al. (2022)](/sources/howell-2022.md), [Ebrahimi & Bhattacharjee (2023)](/sources/ebrahimi-2023.md) — NIMROD divergence cleaning in Faraday's law.
* [Zhang et al. (2021)](/sources/zhang-2021.md), [Isernia et al. (2023)](/sources/isernia-2023.md), [Jiang et al. (2024)](/sources/jiang-2024.md), [Panici et al. (2023)](/sources/panici-2023.md), [Ma & Guo (2022)](/sources/ma-2022.md), [Taheri et al. (2022)](/sources/taheri-2022.md) — further representations.
