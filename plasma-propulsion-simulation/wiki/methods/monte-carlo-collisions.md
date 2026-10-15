---
type: Method
title: "Monte Carlo collisions and the null-collision method"
description: "The stochastic collision step of PIC-MCC, in which each projectile macroparticle collides with probability set by its collision frequency against a background target sampled from fluid or cell properties, with the null-collision method of Vahedi and Surendra as the common implementation and the same machinery reused for anomalous and wall collisions."
status: established
aliases: [MCC, Monte Carlo collision, null collision, null-collision method]
tags: [mcc, pic, kinetic, numerics]
timestamp: 2026-10-15T00:00:00Z
---

# Monte Carlo collisions and the null-collision method

The collision step of [PIC-MCC](/methods/pic-mcc.md) changes particle
velocities (and creates or removes particles) between pushes. Over one time
step the distribution of a species is updated as
$$f_s(t+\Delta t)=(1-P_c)\,f_s(t)+P_c\,(\text{post-collision distribution}),$$
where $P_c$ is the collision probability ([Taccogna et al. (2023)](/sources/taccogna-2023.md), §II,
Eq. 4, which attributes the rules to Nanbu and prints "the Nanbu (no-time
counter) stochastic Monte Carlo rules"). The registry probability for one
particle in one step is $P_c=1-\exp(-\nu\Delta t)$.

## MCC and DSMC

Taccogna et al. (2023, §II) distinguish two classes. In **MCC** the target
species is a fluid background: the projectile macroparticle collides with a
partner sampled from the background's local properties. In
[DSMC](/methods/dsmc.md) both partners are macroparticles, paired within a
cell. [Boyd (2005)](/sources/boyd-2005.md) (§2.2.1) states the DSMC
conditions — time step much shorter than the mean collision time, cell of
the order of the mean free path, collision probability proportional to
cross section times relative speed (attributed to Bird) — and assigns MCC
(after Birdsall) to the heavy-species collisions of hybrid codes with fluid
electrons.

[Gallo et al. (2021)](/sources/gallo-2021.md) (§2.4) reject both for their
heavy-species channel model: DSMC because the electrons are a fluid, and
standard MCC because neutrals dominate, the neutral flux falls along the
channel and ion and neutral masses differ. They replace ionization by a
cell-based transfer of mass from neutral to ion macroparticles that
conserves the total mass flow.

## Null-collision implementation

[Miranda et al. (2026)](/sources/miranda-2026.md) (§2.1) and
[Troyetsky et al. (2026)](/sources/troyetsky-2026.md) (PIC-MCC model
section) use MCC with the null-collision method; Miranda et al. cite
Vahedi & Surendra for it. [Charoy et al. (2020)](/sources/charoy-2020.md)
(§V) cite Vahedi & Surendra and [Reza et al. (2022)](/sources/reza-2022.md)
(§2) cite an MCC reference; neither names the null-collision step. [Muñoz Tejeda et al. (2025)](/sources/munoz-2025.md) compute instead
a collision frequency per electron macroparticle and reaction $k$,
$\nu_{ek}=n_k\,\sigma_{ek}\sqrt{|\mathbf v_e|^2+\bar v_k^{\,2}}$
(Eq. 8, with $\sigma_{ek}$ evaluated at the reactant energy and $\bar v_k$
a speed of the target species), against a target built from
local cell properties; the null-collision method is not stated.

Taccogna et al. (2023, §II) give the accuracy rule: "It is a good practice
to keep the collision probability P of a given species below 5-10% to limit
the error to less than 1%."

## Processes and data

| Source | Gas | Processes | Cross sections |
|---|---|---|---|
| Charoy et al. (2020), §V | Xe | e–Xe elastic, four excitations (8.315, 9.447, 9.917, 11.7 eV); Xe$^+$–Xe isotropic scattering and backscattering (charge exchange); no ionization energy loss | LXCat (Phelps) |
| Miranda et al. (2026), §2.1 | Xe, Ar | electron elastic, excitation, ionization; ion charge exchange; Ar also ion elastic | not stated |
| Reza et al. (2022), §§4.2, 5.1 | Xe | single ionization, four excitations, elastic momentum transfer | Biagi-v7.1 (LXCat) |
| Troyetsky et al. (2026) | Xe | e–n elastic, ionization, charge exchange; no excitation, no Coulomb | Biagi v8.97; charge exchange after Miller et al. |
| Muñoz Tejeda et al. (2025), Tables 3–4 | O$_2$, H$_2$O | 18 (oxygen) and 45 (water, as stated) electron-impact reactions in two stages | literature, per reaction |

Troyetsky et al. (2026) specify the post-collision rules: on ionization the
new ion takes the neutral bulk velocity and both electrons scatter
isotropically with a random energy split; momentum-transfer collisions
scatter isotropically; charge exchange samples the neutral from a drifting
Maxwellian at 0.1 eV and swaps velocities. Muñoz Tejeda et al. (2025,
Eq. 9) take the whole reaction energy loss from the incident electron and
share the remainder equally among the outgoing electrons, with directions
from Marsaglia's recipe; the reactive model costs about 34 % of the run
time. Taccogna et al. (2023, §V A) name IAEA, LXCat, Quantemol, NIST and
NIFS as cross-section databases and collisional data for alternative and
molecular propellants as an open need.

Collisions change the physics the particle runs resolve. Charoy et al.
(2020, §V, Fig. 12) find that adding the collision set enhances the
instability-driven electron–ion friction "by almost a factor 2", that
ion–neutral isotropic scattering has no significant effect and that
backscattering (charge exchange) enhances it; electron–neutral drag stays
small against electron–ion friction.

## Collisions as a vehicle for model terms

The MCC step also carries non-binary model terms. Anomalous cross-field
transport is imposed as a fictitious collision that scatters the electron
velocity without energy loss: a Bohm-type
$\nu_{\mathrm{ano}}=\alpha_{\mathrm B}\,\omega_{ce}/16$ with fitted
$\alpha_{\mathrm B}=0.032$–$0.32$ in 2D $r$–$z$ PIC
([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §3.3); a
three-zone step in $z$ (0–0.5, 0.5–1.2, 1.2–2.5 cm)
$\alpha_{\mathrm B}=0.5/0.053/1.6$, and a two-zone $\alpha_{\mathrm B}=0.035/5.0$ (Reza et al. 2022, §§3.1,
5.1); $\alpha_{\mathrm B}=0.01$ with probability $\nu_{\mathrm{ano}}\Delta t$
per step (Muñoz Tejeda et al. 2025, Eq. 7); an isotropic anomalous
scattering with $\alpha_{\mathrm B}$ ramping from 0.16 to 4.0 (Troyetsky et
al. 2026, Eq. 8; the native form is converted on the Source page). Reza et al. (2022, §5.1, Eqs. 14–15) also
implement an ad-hoc electron–wall collision with an energy loss as a
fictitious MCC event. The physics of these coefficients is on
[anomalous electron transport](/definitions/anomalous-electron-transport.md).

# Citations

1. [Taccogna et al. (2023)](/sources/taccogna-2023.md), §§II, V A (accepted manuscript).
2. [Boyd (2005)](/sources/boyd-2005.md), §2.2.1.
3. [Gallo et al. (2021)](/sources/gallo-2021.md), §2.4.
4. [Miranda et al. (2026)](/sources/miranda-2026.md), §2.1.
5. [Troyetsky et al. (2026)](/sources/troyetsky-2026.md), PIC-MCC model section, Eq. 8.
6. [Charoy et al. (2020)](/sources/charoy-2020.md), §V, Fig. 12 (accepted manuscript).
7. [Reza et al. (2022)](/sources/reza-2022.md), §§2, 3.1, 4.2, 5.1 (preprint).
8. [Muñoz Tejeda et al. (2025)](/sources/munoz-2025.md), Eqs. 7–9, Tables 3–4.
9. [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §3.3 (accepted manuscript).
