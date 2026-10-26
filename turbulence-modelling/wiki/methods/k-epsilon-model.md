---
type: Method
title: "k-ε models"
description: "Two-equation RANS eddy-viscosity models transporting the turbulent kinetic energy and its dissipation rate: the standard high-Reynolds form and its constants, the realizable variant with a two-layer wall treatment, low-Reynolds and elliptic-relaxation relatives, and evidence on bluff-body wakes, periodic hills and learned non-linear corrections."
status: established
aliases: [k-epsilon, standard k-ε, Launder–Sharma k-ε, realizable k-ε, RKE, Shih k-ε, enhanced wall treatment, EWT, two-layer k-ε]
tags: [rans, eddy-viscosity, separated-flow, boundary-layer]
timestamp: 2026-10-26T10:25:00Z
---

# k-ε models

The $k$-$\varepsilon$ models close the RANS equations with a
[Boussinesq](/definitions/boussinesq-hypothesis.md) eddy viscosity built from
two transported quantities, the turbulent kinetic energy $k$ and its
dissipation rate $\varepsilon$:

$$\nu_t=C_\mu\frac{k^2}{\varepsilon}.$$

The family includes the standard high-Reynolds-number model, low-Reynolds
forms with near-wall damping, the realizable model of Shih et al., and
elliptic-relaxation descendants. In this bundle the standard model is the
baseline of a learned non-linear correction (Tang et al. 2023), the
realizable model is the industrial reference of an automotive study
(Delassaux et al. 2023), and the $k$-$\varepsilon$ branch is the outer
formulation of the [$k$-$\omega$ SST model](/methods/k-omega-sst-model.md).

## The standard model

Tang et al. (2023) print the incompressible high-Reynolds-number model that
OpenFOAM solves as their baseline, attributing the constants to Launder &
Sharma ([Tang et al. (2023)](/sources/tang-2023.md), §II A, Eqs. 4–8; arXiv
v1). In registry notation, with $\langle u_j\rangle$ the mean velocity:

$$\begin{aligned}
\partial_tk+\langle u_j\rangle\partial_jk&=\partial_j\Big[\Big(\nu+\frac{\nu_t}{\sigma_k}\Big)\partial_jk\Big]+P_k-\varepsilon,\\
\partial_t\varepsilon+\langle u_j\rangle\partial_j\varepsilon&=\partial_j\Big[\Big(\nu+\frac{\nu_t}{\sigma_\varepsilon}\Big)\partial_j\varepsilon\Big]+C_{\varepsilon1}\frac{\varepsilon}{k}P_k-C_{\varepsilon2}\frac{\varepsilon^2}{k},
\end{aligned}$$

with $P_k=-R_{ij}\partial_j\langle u_i\rangle$ and

| $C_\mu$ | $C_{\varepsilon1}$ | $C_{\varepsilon2}$ | $\sigma_k$ | $\sigma_\varepsilon$ |
|---|---|---|---|---|
| 0.09 | 1.44 | 1.92 | 1.0 | 1.3 |

The printed form carries no low-Reynolds damping functions. The authors
call the $\varepsilon$-equation empirical, "not based on the exact
transport equation" (§II A). Their Reynolds stress is the kinematic,
positive-trace $R_{ij}$ of the registry, closed as
$R_{ij}=\tfrac23k\delta_{ij}-2\nu_t\langle S_{ij}\rangle$ (Eq. 3).

**Expected values in, expected values out.** The destruction
$C_{\varepsilon2}\varepsilon^2/k$ is nonlinear in the transported variables.
Haering et al. (2022) use it as their example of a RANS source calibrated on
mean quantities that acquires spurious correlations when evaluated on
fluctuating fields inside a hybrid simulation; see
[hybrid RANS/LES](/definitions/hybrid-rans-les.md)
([Haering et al. (2022)](/sources/haering-2022.md), §II D, Eqs. 1–2).

## The realizable model and a two-layer wall treatment

Delassaux et al. (2023) use the realizable $k$-$\varepsilon$ model of Shih et
al. in ANSYS Fluent as "the numerical reference for external flow
application" of their industrial partner
([Delassaux et al. (2023)](/sources/delassaux-2023.md), §4.1.1; HAL author
manuscript). They print no equation and describe two departures from the
standard model:

- a new dissipation-rate equation "based on the dynamic equation of the
  mean-square vorticity fluctuation for large Reynolds number";
- a realizable eddy-viscosity formulation "based on the positivity of
  square Reynolds stresses and Schwarz' inequality for turbulent shear
  stresses".

They couple it to Fluent's Enhanced Wall Treatment, a two-layer approach:
with the page-local wall-distance Reynolds number
$R_y=d\sqrt k/\nu$ (the source's $\rho y\sqrt k/\mu$, $y$ the wall distance
of the cell centre), the one-equation model of Wolfshtein supplies the eddy
viscosity where $R_y<200$ and the $k$-$\varepsilon$ formulation is used where
$R_y>200$ (§4.1.1). The same symbol $R_y=d\sqrt k/\nu$ enters the
transition-modified $F_1$ of the [SST page](/methods/k-omega-sst-model.md).
The authors state as a known drawback that the model underestimates the
turbulent kinetic energy in separated regions and therefore overestimates
the recirculation length "in most of the cases" (§4.1.1).

## Low-Reynolds and elliptic-relaxation relatives

- The [active model split](/methods/active-model-split.md) of Haering et al.
  (2022) needs a $k$-equation whose $k$ is the turbulent kinetic energy and
  uses the Chien low-Reynolds $k$-$\varepsilon$ model as one of its two base
  models, rejecting SST because its $k$ in attached boundary layers is "more
  akin to $\tfrac32v^2$" (§IV B, App. A).
- McConkey et al. (2022) build their learned anisotropy correction on the
  OpenFOAM $k$-$\varepsilon$-$\varphi$-$f$ elliptic-relaxation model, whose
  eddy viscosity is $C_\mu\varphi k\mathcal T$ with a time scale
  $\mathcal T=\max(k/\varepsilon,C_T\sqrt{\nu/\varepsilon})$ ($\varphi$,
  $\mathcal T$, $C_T$ page-local, the source's $T$; [McConkey et al. (2022)](/sources/mcconkey-2022.md), Eqs.
  10–16; see
  [periodic hill](/benchmarks/periodic-hill.md) and the
  [Boussinesq page](/definitions/boussinesq-hypothesis.md)).
- Inside SST the outer branch is a $k$-$\varepsilon$ model written in
  $\omega$; its detached-eddy constant is $C_{\mathrm{DES}}=0.61$ against
  0.78 for the inner branch, blended through $F_1$ (Delassaux et al. 2023,
  §4.1.3, Eq. 9; Carlsson et al. 2023, §4.2; see
  [detached-eddy simulation](/methods/detached-eddy-simulation.md)).

## Evidence

**Bluff-body wakes.** On the 25° Ahmed body Delassaux et al. recall from
their earlier calibration that the realizable model gives no separation on
the slant, SST a massive one, and only the scale-resolving models the
separation and reattachment (§5; see [Ahmed body](/benchmarks/ahmed-body.md)).
On a full-scale estate car (Peugeot 308 SW, $Re_L=1.3\times10^7$ on the car
length, 115 million cells, 20 prism layers at $y^+\approx1$) they compare it
with SST and SST-based delayed DES against wind-tunnel data (§6–§7):

- drag coefficient 0.242 against 0.244 measured, the same as SST, and
  insensitive to 30 prism layers (0.242) and to a refined wake grid (0.243)
  (Table 3); the authors attribute this agreement to error cancellation,
  the cumulative drag of this model and of DDES differing at the front
  fairings and at the rear (§6, Fig. 13);
- in the symmetry-plane wake a high-speed jet from the underbody reaches far
  into the wake, absent in the experiment; the recirculation is
  overpredicted, less than with SST but more than with DDES (§7.2, Figs.
  17–18);
- in the upper wake plane the streamwise velocity is predicted better than
  by both SST models (§7.2, Fig. 19);
- on rounded separation lines it overpredicts the pressure coefficient where
  SST is closest to the measurements (§7.3, Fig. 20), and behind the rear
  fairing it gives a recirculation larger than measured (§7.4, Fig. 23).

**Separated channel flows.** On the parametrized periodic hills of Xiao et
al. ($Re=5600$ on the hill height, steepness factors 0.5, 0.8, 1.0) and the
backward-facing step at $Re=5000$, Tang et al. (2023) find that the standard
model underestimates the separation bubble on the training hill; it
predicts the shear component of the anisotropy reasonably but the normal
components "far removed" from DNS, especially near the bottom wall, and its
anisotropy lies close to the plane-strain line of the barycentric map at
all stations (§III C, Figs. 7–9; see [periodic hill](/benchmarks/periodic-hill.md)
and [backward-facing step](/benchmarks/backward-facing-step.md)). The linear
model cannot produce such normal-stress anisotropy because it ties the
anisotropy to the strain; the non-linear correction Tang et al. learn on top
of it is described on the [Boussinesq page](/definitions/boussinesq-hypothesis.md)
and on [symbolic-regression closures](/methods/symbolic-regression-closure.md).
They report that a converged RANS with the learned correction costs
"basically the same" as the baseline (§III A).

**Low-Reynolds backward-facing step.** Agrawal & Koutsourelakis (2024) use
the standard model (OpenFOAM simpleFoam, 35,709 degrees of freedom, $k$ and
$\varepsilon$ "obtained by solving the respective standard transport
equations") as the baseline of their probabilistic learned closure on a
two-dimensional step of expansion ratio 2 at $Re=500$ on the step height
and inlet bulk velocity
([Agrawal & Koutsourelakis (2024)](/sources/agrawal-2024.md), §3.2, §3.4,
App. A; arXiv v2). Against a spanwise-periodic WALE LES, the baseline
"underestimates the size of the first recirculation zone and almost
completely misses the second one", gives a reattachment length of
$5.61h$ against $9.10h$, and "severely under/over-estimates" the magnitude
of the Reynolds stress and "misrepresents its spatial variability" (§3.4,
Figs. 7–8, Table 5). The authors recall that their tensor-basis closure
reduces to this model for $g^{(1)}=-0.09$ and all other coefficients zero
(§2.2.1, Eq. 15); with the Boussinesq closure and $\nu_t=C_\mu k^2/\varepsilon$
the coefficient of $T^{(1)}=\mathsf S$ in the registry's $b_{ij}$ is
$-C_\mu=-0.09$ *(compiler check, not in the sources)*; see the
[tensor-basis neural network](/methods/tensor-basis-neural-network.md),
[model-form uncertainty](/definitions/model-form-uncertainty.md) and
[backward-facing step](/benchmarks/backward-facing-step.md).

**Lattice Boltzmann hosts.** Mozaffari et al. (2024) recall
$k$-$\varepsilon$ implementations in lattice Boltzmann solvers, including
a $k$-$\varepsilon$-based hybrid RANS/LES of Sajjadi et al., as the
precedent of their SST implementation in a standard lattice Boltzmann
code ([Mozaffari et al. (2024)](/sources/mozaffari-2024.md), §1; HAL accepted
manuscript; see [lattice Boltzmann methods](/methods/lattice-boltzmann-method.md)).

## Qualifications

- Delassaux et al. print neither the realizable model nor the Wolfshtein
  length scales; the statements above are their description.
- Tang et al. attribute the constants to Launder & Sharma while printing the
  model without the damping functions of a low-Reynolds form (§II A); the
  page records the form as printed.
- Delassaux et al. call the drag agreement of both RANS models fortuitous:
  "There is no valid reason that RANS predicts a more accurate $C_d$ than
  DDES" (§6). The agreement is therefore not evidence for the model; see
  [model-form uncertainty](/definitions/model-form-uncertainty.md).

# Citations

- [Tang et al. (2023)](/sources/tang-2023.md) — §II A Eqs. 3–8, §III A, §III C Figs. 7–9 (arXiv v1).
- [Delassaux et al. (2023)](/sources/delassaux-2023.md) — §4.1.1, §4.1.3 Eq. 9, §5, §6 Table 3 Fig. 13, §7.2–7.4 Figs. 17–20, 23 (HAL author manuscript).
- [Haering et al. (2022)](/sources/haering-2022.md) — §II D Eqs. 1–2, §IV B, App. A.
- [McConkey et al. (2022)](/sources/mcconkey-2022.md) — Eqs. 10–16 (arXiv v1).
- [Carlsson et al. (2023)](/sources/carlsson-2023.md) — §4.2.
- [Agrawal & Koutsourelakis (2024)](/sources/agrawal-2024.md) — §2.2.1 Eq. 15, §3.2, §3.4 Figs. 7–8 Table 5, App. A (arXiv v2).
- [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) — §1 (HAL accepted manuscript).
