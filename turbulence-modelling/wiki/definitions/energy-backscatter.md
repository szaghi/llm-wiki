---
type: Definition
title: "Energy backscatter and the subgrid energy flux"
description: "Energy backscatter is a negative local subgrid energy flux, energy moving from subgrid to resolved scales; the sources define the flux, show that its local sign depends on the gauge of the subgrid stress and on the filter, and disagree in emphasis on whether models must reproduce it or remove it for stability."
status: established
aliases: [backscatter, inverse energy transfer, subgrid-scale energy flux, interscale energy flux, local SGS dissipation]
tags: [les, sgs-model, eddy-viscosity, filtering]
timestamp: 2026-10-25T19:45:00Z
---

# Energy backscatter and the subgrid energy flux

The **local subgrid-scale energy flux** is

$$\Pi=-\tau_{ij}\bar S_{ij},$$

the rate at which the [subgrid stress](/definitions/large-eddy-simulation.md)
removes kinetic energy from the resolved field. $\Pi>0$ is forward transfer
(resolved to subgrid) and $\Pi<0$ is **backscatter**.
[Vela-Martín (2022)](/sources/velamartin-2022.md) (§2.1, Eqs. 2.4–2.7)
writes the resolved energy budget with this flux. With the registry sign,
the subgrid term in the resolved-energy equation splits as

$$-\bar u_i\partial_j\tau_{ij}=D-\Pi,\qquad D=-\partial_j(\bar u_i\tau_{ij}),$$

where $D$ (page-local symbol) is a conservative spatial flux with zero
domain average. Hence $\langle\Pi\rangle$ is the net cascade rate, equal to
the dissipation $\varepsilon$ for a filter in the inertial range. The author
prints the stress with the opposite sign (the paper's $T=\bar S_{ij}\tau^S_{ij}$
is the registry's $\Pi$) and uses $\Pi$ as the cascade flux because it is
Galilean-invariant, scale-local and free of sweeping (citing Eyink and
co-workers).

For an eddy-viscosity model $\Pi=\nu_t\lvert\bar S\rvert^2$, so backscatter
requires $\nu_t<0$. Vela-Martín (2022, §2.2) recalls that negative eddy
viscosity "generally leads to critical numerical instabilities", as in the
local [dynamic procedure](/methods/dynamic-procedure.md), and is removed by
clipping or averaging.

## How much backscatter, and with which filter

In filtered DNS of linearly forced isotropic turbulence at $Re_\lambda=140$,
240 and 324 ($256^3$ to $1024^3$, 290 independent fields, filter scales
$0.08$–$0.65$ of the integral scale), Vela-Martín (2022, §5.3, Fig. 2)
measures the backscatter volume fraction $v^-$ (the fraction of the domain
with $\Pi<0$) and the net backscatter $f^-$ (minus the integral of the
negative part of $\Pi$ divided by the integral of $\Pi$); both symbols are
page-local:

- sharp Fourier filter: $v^-\approx0.5$, $f^-$ close to one;
- Gaussian filter: $v^-\approx0.15$, $f^-\approx0.05$;
- both grow as the filter scale decreases.

Backscatter is therefore not a property of the flow alone: its amount
depends on the filter kernel. Literature values recalled in §2.1 are about
40% of the domain for sharp filters and 15% for Gaussian filters.

## Gauge dependence

The resolved equations depend on $\tau_{ij}$ only through its divergence,
so adding any symmetric divergence-free tensor leaves the dynamics, the
total term $D-\Pi$ and $\langle\Pi\rangle$ unchanged, but changes the local
$\Pi$ and $D$ (Vela-Martín 2022, §3, Eqs. 3.1–3.5; idea attributed to
Jiménez 2016). Vela-Martín minimizes $\langle\Pi^2\rangle$ over all
admissible stresses, i.e. symmetric tensors with the divergence of the
filtered-DNS stress. The method is a projected gradient descent with an
$L^2$ projector solved spectrally (§4, Apps. A–B). Starting from the
filtered-DNS stress, the optimization:

- reduces backscatter by about three orders of magnitude, to
  $v^-\approx10^{-3}$ and $f^-\approx10^{-4}$, nearly independently of
  Reynolds number, filter scale and filter type (§6.1–6.2, Figs. 3–4);
- leaves the spatial flux almost unchanged (correlation 0.9 between old
  and new $D$) while the new $\Pi$ is nearly uncorrelated with the old one
  (correlation about 0.01) (§6.3, Fig. 5);
- removes the scale growth of the flatness of $\Pi$, whereas the flatness
  of the gauge-invariant $D-\Pi$ still grows (§6.3, Fig. 6). Intermittency
  need not be modelled in the flux but persists in the total subgrid
  interaction;
- leaves isolated backscatter spots of size about three filter widths and
  intensity about $-0.1\langle\Pi\rangle$ (§6.4, Fig. 7).

The equivalent stresses (filtered-DNS and optimized) correlate only at
0.4–0.6 with each other (§6.3), so poor a priori correlation of a model with
the filtered-DNS stress is not by itself evidence of poor modelling (§8).

## Optimal eddy viscosity (inline)

The eddy viscosity that best fits a given stress in the $L^2$ sense
reproduces its local flux exactly (Vela-Martín 2022, §7.1, Eqs. 7.2–7.5).
Translated to the registry sign, minimizing
$\int(-2\nu_t\bar S_{ij}-\tau_{ij})^2\,dV$ pointwise gives

$$\nu_t^{\mathrm{opt}}=-\frac{\tau_{ij}\bar S_{ij}}{2\bar S_{ij}\bar S_{ij}}=\frac{\Pi}{\lvert\bar S\rvert^2},\qquad \nu_t^{\mathrm{opt}}\lvert\bar S\rvert^2=\Pi$$

*(compiler check, not in the sources)*. It is gauge-dependent:
negative over a large fraction of the domain for the filtered-DNS stress,
positive almost everywhere for the optimized one. In this sense a purely
dissipative "perfect" eddy-viscosity model exists for the flux. The author
cautions that it may be hard to express in resolved quantities.

The same projection is used as an a priori diagnostic by [Abe (2021)](/sources/abe-2021.md)
(§IV C, Eq. 17): the "equivalent SGS eddy viscosity"
$-\tau^d_{ij}\bar S_{ij}/(2\bar S_{kl}\bar S_{kl})$ of a reference or model
stress, which the author notes reproduces exactly its resolved/subgrid
energy transfer, forward and backward. It equals $\nu_t^{\mathrm{opt}}$
above, since $\bar S_{ii}=0$ *(compiler check, not in the sources)*. Abe
compares it between filtered fine-LES data and five models in a free shear
layer (see [Smagorinsky model](/methods/smagorinsky-model.md) and
[scale-similarity models](/methods/scale-similarity-model.md)).

## Model backscatter and stability

[Prakash et al. (2022)](/sources/prakash-2022.md) (§II, Eqs. 4–8) treat
backscatter of a *model* stress $\tau^{\mathrm M}_{ij}$ (page-local) as a
stability risk. With periodic or homogeneous boundaries and no forcing the
resolved energy decays if and only if
$\int_\Omega\tau_{ij}\bar S_{ij}\,d\Omega\le\int_\Omega2\nu\bar S_{ij}\bar S_{ij}\,d\Omega$,
so excessive model backscatter can make it grow. They enforce the
sufficient pointwise condition of no model backscatter,
$\Pi^{\mathrm M}=-\tau^{\mathrm M}_{ij}\bar S_{ij}\ge0$, and say it is
sufficient, not necessary. Two procedures do so for structural models such
as the [gradient model](/methods/gradient-model.md): standard clipping,
which zeroes the model stress where $\Pi^{\mathrm M}<0$ (attributed to Liu,
Meneveau & Katz), and their optimal clipping, which subtracts from the
stress its projection on $\bar S_{ij}$ there, i.e. adds the eddy viscosity
$\max(-\Pi^{\mathrm M},0)/\lvert\bar S\rvert^2$. Both set the local model
flux to zero where the base model backscatters. A priori on box-filtered
isotropic turbulence at $Re_\lambda=418$, anisotropic (book- and
pencil-type) filters lower the mean model dissipation, which the authors
partly attribute to more model backscatter (§III.A.2, Figs. 2–3).

Prakash et al. and Vela-Martín (2022) both arrive at models without local
backscatter, from different premises: stability of the resolved energy for
Prakash et al., the gauge freedom of the stress and the statistics of the
flux for Vela-Martín. The clipping constraint is imposed on one
representative of the model stress; by the gauge argument above, adding
to it a symmetric divergence-free tensor $T_{ij}$ (page-local) leaves the
resolved dynamics unchanged but shifts the local flux by
$-T_{ij}\bar S_{ij}$, which is not zero in general, so the constraint is
not gauge-invariant *(compiler check, not in the sources)*.

## Interpretation and scope

Vela-Martín (2022, §7.2, §8) concludes that, in isotropic turbulence away
from walls, backscatter is conservative spatial redistribution rather than
a local inverse cascade, and need not be modelled to reproduce the local
resolved/subgrid energy exchange. The author supports this with a
statistical-mechanics argument, presented as an argument rather than a
proof: global inverse cascades are possible but highly improbable. The
conclusions are limited to isotropic turbulence; global
inverse cascades with $\langle\Pi\rangle<0$, and flows with additional
sign-definite invariants (2D, homochiral, MHD), are outside it; and
eliminating backscatter may be unnecessary or undesirable for models with
numerically stable backscatter such as
[similarity models](/methods/scale-similarity-model.md) (§8).

Other sources treat backscatter as a physical effect to be represented:

- [Li & Liu (2022)](/sources/li-2022.md) (§2.3) justify the helicity
  correction of the [Spalart–Allmaras model](/methods/spalart-allmaras-model.md)
  for compressor corner separation by the statement that velocity helicity
  "is correlated with the turbulent energy backscatter", citing earlier
  work (their ref. [22]). They attribute the lower eddy viscosity of the
  corrected model to strong backscatter in strongly rotating turbulence
  (§3.2). This is a RANS argument in a rotation-dominated flow;
  Vela-Martín (2022, §8) limits the conclusions to isotropic turbulence
  and names shear- or rotation-dominated flows as a further application of
  the method.
- The [dynamic tensor-coefficient Smagorinsky model](/methods/dynamic-tensor-coefficient-smagorinsky-model.md)
  of [Agrawal et al. (2022)](/sources/agrawal-2022.md) dissipates only
  through its Smagorinsky-type coefficient; its antisymmetric part changes
  the stress without exchanging energy (§III.A). The dynamic Smagorinsky
  model needs clipping near the wall in their WMLES channel, where the
  tensor model does not (§VII.D).
- In the spectral view of [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md)
  (§2.2), the shell-averaged transfer across the cutoff defines the
  [spectral eddy viscosity](/methods/spectral-eddy-viscosity.md). This
  measures the net transfer at each wavenumber and cannot show the spatial
  sign of $\Pi$ *(compiler check, not in the sources)*.

## Qualifications

- Vela-Martín (2022) prints several slips that do not affect the results:
  Eq. (3.5) uses the unfiltered velocity and swapped indices, and its sign
  disagrees with Eqs. (2.5) and $\langle D\rangle=0$, which give
  $\langle\bar u_i\partial_j\tau^S_{ij}\rangle=-\langle T\rangle$ in the
  paper's notation *(compiler check, not in the sources)*. §6.3 writes
  $\rho(T^S_s,T^O_g)$ for the correlation of the two standard fluxes. The
  Fig. 6 and Fig. 7 captions and §6.4 give $Re_\lambda=320$ where Table 1
  gives 324. The PGD algorithm is called "PSD" once (§6.1).
- At $\Delta=0.33L$, $Re_\lambda=240$ the sharp-filter starting values are
  given as $f^-\approx0.6$, $v^-\approx0.4$ (§6.1), against the general
  "$v^-\approx0.5$" and $f^-$ "close to unity" of §5.3.

# Citations

- [Vela-Martín (2022)](/sources/velamartin-2022.md) — §2.1–2.2, Eqs. (2.4)–(2.8); §3, Eqs. (3.1)–(3.5); §4; §5.3, Eqs. (5.7)–(5.8), Fig. 2; §6.1–6.4, Figs. 3–7; §7.1, Eqs. (7.2)–(7.5); §7.2; §8; Apps. A–B.
- [Li & Liu (2022)](/sources/li-2022.md) — §2.3, Eqs. (19)–(22); §3.2.
- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §III.A; §VII.D.
- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §2.2, Eqs. (16)–(22).
- [Prakash et al. (2022)](/sources/prakash-2022.md) — §II, Eqs. (4)–(15); §III.A.2, Figs. 2–3.
- [Abe (2021)](/sources/abe-2021.md) — §IV C, Eq. (17).
