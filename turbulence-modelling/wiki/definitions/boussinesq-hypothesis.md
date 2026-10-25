---
type: Definition
title: "Boussinesq eddy-viscosity hypothesis"
description: "The linear closure that aligns the deviatoric Reynolds or subgrid stress with the strain rate through a scalar eddy viscosity; its RANS and LES forms, the sign conventions of the sources, and the evidence that one scalar viscosity cannot carry both the mean stress and the energy transfer."
status: established
aliases: [Boussinesq approximation, linear eddy-viscosity hypothesis, eddy-viscosity assumption, linear constitutive relation, stress-strain alignment]
tags: [eddy-viscosity, rans, sgs-model, les]
timestamp: 2026-10-25T13:45:00Z
---

# Boussinesq eddy-viscosity hypothesis

The Boussinesq hypothesis closes the unresolved stress by a scalar eddy
viscosity $\nu_t$ acting on the strain rate, so that the deviatoric part of
the stress is aligned with the strain. In Reynolds-averaged form it reads

$$R_{ij}-\tfrac23k\,\delta_{ij}=-2\nu_t\langle S_{ij}\rangle ,$$

and in large-eddy simulation, for the subgrid stress
$\tau_{ij}=\overline{u_iu_j}-\bar u_i\bar u_j$,

$$\tau^d_{ij}=\tau_{ij}-\tfrac13\tau_{kk}\delta_{ij}=-2\nu_t\bar S^d_{ij}.$$

The isotropic part ($\tfrac23k\delta_{ij}$, or $\tfrac13\tau_{kk}\delta_{ij}$) is
either carried by a model for $k$ or absorbed into a modified pressure. All
the linear eddy-viscosity closures of this bundle are of this form and differ
only in how they compute $\nu_t$: the [Spalart–Allmaras model](/methods/spalart-allmaras-model.md)
from a transported $\tilde\nu$, the [$k$-$\omega$ SST model](/methods/k-omega-sst-model.md)
from $k$ and $\omega$, the [Smagorinsky model](/methods/smagorinsky-model.md)
from $\Delta$ and $\lvert\bar S\rvert$, the [Vreman model](/methods/vreman-model.md)
from the resolved velocity gradient.

## Forms in the sources

The sources print the same hypothesis with different signs, density weights
and treatments of the trace; translated to the registry they agree.

- **RANS, compressible.** Li & Liu (2022) write the Reynolds stress in the
  $-\rho\langle u_i'u_j'\rangle$ convention as
  $2\mu_t\big(S_{ij}-\tfrac13\partial_ku_k\delta_{ij}\big)-\tfrac23\rho k\delta_{ij}$
  ([Li & Liu (2022)](/sources/li-2022.md), Eq. 38), which is the registry form
  multiplied by $-\rho$ with the deviatoric strain.
- **PANS.** Dzanic et al. (2022) close the unresolved stress of
  [partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md)
  by the same relation with the unresolved eddy viscosity and the unresolved
  kinetic energy $f_kk$, added to the viscous stress (so with the opposite
  sign to the registry's stress), printed without $\rho$ on the kinetic energy
  and without the deviatoric projection of $S_{ij}$
  ([Dzanic et al. (2022)](/sources/dzanic-2022.md), §2.1, Eq. 7).
- **LES.** Agrawal et al. (2022) use the registry's positive-trace
  convention, $\tau^d_{ij}=-2\nu_t\bar S_{ij}$, with the isotropic part
  absorbed into the pressure ([Agrawal et al. (2022)](/sources/agrawal-2022.md),
  §II, Eqs. 2–4). Haering et al. (2022) define their subgrid stress with the
  opposite sign and write $+2\nu_{\mathrm{sgs}}\bar S_{ij}$ for it
  ([Haering et al. (2022)](/sources/haering-2022.md), §III, Eq. 3); Agdestein &
  Sanderse (2025) write the closure directly as the force
  $\nabla\cdot(2\nu_t\bar S)$ added to the filtered momentum equation
  ([Agdestein & Sanderse (2025)](/sources/agdestein-2025.md), §4.4.1, Eq. 26).

### A traceless Reynolds stress

A model that carries no $k$, such as Spalart–Allmaras, supplies only the
deviatoric term, so its modelled Reynolds stress has zero trace. Li & Liu
(2022) note that in SA and in SA with the 2000 quadratic constitutive
relation $R_{kk}$ vanishes identically, so the anisotropy tensor $b_{ij}$
cannot be formed. The 2013 version of the relation adds an isotropic term
$\propto\nu_t\lvert S^d\rvert\delta_{ij}$ that "acts similarly" to the
missing $\tfrac23k\delta_{ij}$ ([Li & Liu (2022)](/sources/li-2022.md), §2.3,
Eqs. 26–27; §4.2, Eqs. 35, 38; details on the
[Spalart–Allmaras page](/methods/spalart-allmaras-model.md)).

## Where it sits among the modelling assumptions

Duraisamy et al. (2019) classify the choice of representation of the
Reynolds stress in terms of the mean variables (linear eddy viscosity,
algebraic stress models) as the second of four layers of RANS assumptions,
and the value of $C_\mu$ in two-equation linear models as "a classical L4
closure issue", i.e. a coefficient choice
([Duraisamy et al. (2019)](/sources/duraisamy-2019.md), §2; see
[model-form uncertainty](/definitions/model-form-uncertainty.md)). If the
Reynolds stress depends only on the local mean velocity gradient, the
Cayley–Hamilton theorem gives an exact finite basis: the anisotropy is a
combination $b_{ij}=\sum_ng^{(n)}T^{(n)}_{ij}$ of the ten integrity-basis
tensors of Pope (1975), as recalled by Duraisamy et al. (2019, §2, §5.3,
Eq. 11) and Duraisamy (2021, §III.A, Eq. 4). The Boussinesq hypothesis keeps
only the first term, $T^{(1)}\propto S_{ij}$; the
[tensor-basis neural network](/methods/tensor-basis-neural-network.md) and
the quadratic constitutive relation of the SA page add higher terms.

Haering et al. (2022) derive the scalar eddy viscosity from a
gradient-diffusion argument: a flux $\langle u_i'\phi'\rangle$ is modelled
from the displacement of fluid particles over a decorrelation time $T_\phi$,
which under isotropy gives $\nu_\phi=C\,k_cT_\phi$ with $k_c$ the energy of
the convecting fluctuations ([Haering et al. (2022)](/sources/haering-2022.md),
§III B, Eqs. 12–14). The LES version holds only in expectation.

## Limits of a single scalar eddy viscosity

**Misalignment.** Agrawal et al. (2022) build their model on the statement
that the alignment of the subgrid stress with the resolved strain is invalid
locally, as a priori analyses of DNS show; they quote the a priori
misalignment results of Bardina et al. and of Meneveau & Liu as recalled in
their introduction. On filtered channel DNS at $Re_\tau=395$ and $2000$ their
non-Boussinesq [dynamic tensor-coefficient Smagorinsky model](/methods/dynamic-tensor-coefficient-smagorinsky-model.md)
correlates better with the exact stress than the dynamic Smagorinsky model,
most of all near the wall, while the two models have identical dissipation
correlations, because only the isotropic part of the coefficient tensor
dissipates ([Agrawal et al. (2022)](/sources/agrawal-2022.md), §V, Figs. 1–2).
The authors add that these correlations do not measure alignment.

**Mean stress against energy transfer.** Haering et al. (2022) argue that
one scalar eddy viscosity cannot represent both the mean subgrid stress and
the mean energy transfer to the subgrid scales. The first is the mean of the
stress; the second is governed by the correlation between stress and
resolved strain, which in filtered turbulence is "of order 20% or less" but
equals one, or nearly so, for an eddy-viscosity model. Getting the transfer
right therefore requires a smaller viscosity than getting the stress right.
As recalled from Jiménez & Moser, the dynamic Smagorinsky model gives
channel-flow subgrid stresses "nearly five times smaller than the true
filtered stress" ([Haering et al. (2022)](/sources/haering-2022.md), §II B,
pp. 5–6). They derive the split
$\tau^d_{ij}=-2\nu_s\langle\bar S_{ij}\rangle-2\nu_e\bar S'_{ij}$, with
$\bar S'_{ij}=\bar S_{ij}-\langle\bar S_{ij}\rangle$ the resolved fluctuating
strain and two non-fluctuating viscosities of different magnitude and conclude that
"$\tau^d_{ij}=-2\nu_t\bar S_{ij}$ is not generally valid" (§III B, Eqs.
20–24; see [active model split](/methods/active-model-split.md)).

**Correlation is gauge-dependent.** Vela-Martín (2022) shows that the
subgrid stress is defined only up to an added symmetric divergence-free
tensor, which leaves the resolved dynamics and the mean flux $\langle\Pi\rangle$
unchanged but changes the local flux $\Pi$. The eddy viscosity that
reproduces the local flux exactly,

$$\nu_t^{\mathrm{opt}}=\frac{\Pi}{\lvert\bar S\rvert^2},$$

(the registry translation of the author's
$\tau_{ij}\bar S_{ij}/(2\bar S_{ij}\bar S_{ij})$, whose stress has the
opposite sign) is negative over a large fraction of the domain for the
author's "standard" stress $\overline{u_iu_j}-\bar u_i\bar u_j$ (up to sign) but positive almost everywhere for the stress
representation that minimises the flux variance: a purely dissipative
eddy viscosity that reproduces the local energy exchange exists, in the
flux sense ([Vela-Martín (2022)](/sources/velamartin-2022.md), §7.1, Eqs.
7.2–7.5). Equivalent representations correlate only about 0.6 to 0.4 with
each other (all components, filter scales $\ell/L=0.64$ to $0.08$), so a
poor a priori correlation of a model with the standard stress "is not
necessarily an indication of poor modelling" (§6.3, §8). The conclusions
are limited to isotropic turbulence away from walls (§8). See
[energy backscatter](/definitions/energy-backscatter.md).

**Consistency of the inputs.** Duraisamy (2021) warns that a feature such
as $\langle S_{ij}\rangle k/\varepsilon$ evaluated from DNS need not equal the same
feature built from a RANS model's $k$ and $\varepsilon$, which play an
operational role ([Duraisamy (2021)](/sources/duraisamy-2021.md), §IV.A);
Duraisamy et al. (2019) make the same point for the dissipation rate
([Duraisamy et al. (2019)](/sources/duraisamy-2019.md), §5.4).

## Qualifications

- Haering et al. (2022) and Vela-Martín (2022) read low stress–strain
  correlations differently. Haering et al. take the correlation of the
  filtered stress with the strain as a property the model's energy transfer
  must match; Vela-Martín shows that this correlation changes with the
  gauge of the stress and that a perfectly flux-matching eddy viscosity
  exists. Haering et al. argue about the mean stress of wall-bounded
  hybrid simulations; Vela-Martín restricts the conclusion to the local
  flux in isotropic turbulence away from walls (§8). No source of this
  bundle compares the two readings in one flow.
- Duraisamy et al. (2019) print the integrity-basis expansion for the full
  Reynolds stress without an isotropic term (§5.3, Eq. 11), while Duraisamy
  (2021) writes it for the anisotropy with the $\tfrac13I$ term separate
  (§III.A, Eq. 4).

# Citations

- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §I, §II Eqs. 2–5, §V Figs. 1–2, App. C.
- [Li & Liu (2022)](/sources/li-2022.md) — §2.3 Eqs. 23–27, §4.2 Eqs. 35–38.
- [Vela-Martín (2022)](/sources/velamartin-2022.md) — §3, §6.3, §7.1 Eqs. 7.2–7.5, §8.
- [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md) — §4.4.1, Eqs. 26–27.
- [Duraisamy et al. (2019)](/sources/duraisamy-2019.md) — §2 (L2, L4), §5.3 Eq. 11, §5.4.
- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §III.A Eq. 4, §IV.A.
- [Haering et al. (2022)](/sources/haering-2022.md) — §II B, §III Eqs. 3–8, §III B Eqs. 12–24.
- [Dzanic et al. (2022)](/sources/dzanic-2022.md) — §2.1, Eq. 7.
