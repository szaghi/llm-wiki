---
type: Method
title: "GLM divergence cleaning"
description: "Generalized-Lagrange-multiplier cleaning adds a scalar field coupled to the magnetic-field divergence, so that divergence errors propagate away at a finite speed and are damped instead of accumulating; the page gives the augmented system, the cleaning speeds and damping rates the sources choose, its conservative and non-conservative forms, and its comparison with constrained transport and projection."
status: established
aliases: [GLM, GLM-MHD, generalized Lagrange multiplier, hyperbolic divergence cleaning, Dedner cleaning, Munz cleaning, perfectly hyperbolic Maxwell equations, mixed hyperbolic–parabolic cleaning]
tags: [mhd, relativistic, dg, finite-difference, divergence-free]
timestamp: 2026-10-24T05:59:00Z
---

# GLM divergence cleaning

**Generalized-Lagrange-multiplier (GLM) cleaning**, after Munz et al.
(2000) and Dedner et al. (2002) as the sources recall them, couples the
induction equation to an additional scalar $\psi_{\mathrm{GLM}}$ (registry
§5):
$$
\partial_tB+\nabla\times\mathcal E+\nabla\psi_{\mathrm{GLM}}=0,\qquad
\partial_t\psi_{\mathrm{GLM}}+c_h^2\,\nabla\cdot B=-r_{\mathrm d}\,\psi_{\mathrm{GLM}},
$$
with $\mathcal E$ the electric field (registry §10, MHD meaning;
$\nabla\times\mathcal E=-\nabla\times(v\times B)$ in ideal MHD), $c_h$ the
cleaning speed and $r_{\mathrm d}\ge0$ a damping rate (both page-local; the
sources scale $\psi_{\mathrm{GLM}}$ differently, below). Unlike
[constrained transport](/methods/constrained-transport.md), it enforces no
discrete $\nabla\cdot B=0$: the divergence is transported away at speed
$c_h$ and damped. *(Compiler check, not in the sources: taking the divergence
of the first equation and eliminating $\psi_{\mathrm{GLM}}$ gives
$\partial_t^2(\nabla\cdot B)+r_{\mathrm d}\,\partial_t(\nabla\cdot B)-c_h^2\nabla^2(\nabla\cdot B)=0$,
a damped wave (telegraph) equation for the divergence.)* It is one of the
divergence controls of the
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
page, the one that keeps a cell-centred, unstaggered layout.

## Choices in the sources

| Source | System | Cleaning speed | Damping |
|---|---|---|---|
| [Komissarov & Phillips (2024)](/sources/komissarov-2024.md) §3.1, Eqs. (53)–(54) | ideal relativistic MHD, separately in each subsystem of the [force-free splitting](/methods/force-free-splitting-rmhd.md) | 1 (the speed of light; $\partial_t\psi_{\mathrm{GLM}}+\nabla\cdot B=\dots$) | $r_{\mathrm d}=0.2/\Delta t$, an e-folding time of 5 steps |
| [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) §2.2, §6 | resistive GLM-MHD with Powell and GLM non-conservative terms | recomputed every step as the largest value compatible with the CFL condition | — |
| [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) §5.3, Eqs. (51)–(52) | ideal GLM-MHD, conservative form | recomputed every step as in the 2021 paper | — |
| [Dao & Nazarov (2022)](/sources/dao-2022.md) §3.2 | ideal MHD in continuous finite elements, $\partial_t\psi_{\mathrm{GLM}}+c_h\nabla\cdot B=-\frac{c_rc_h}{h_i}\psi_{\mathrm{GLM}}$, with $-\nabla\psi_{\mathrm{GLM}}$ in the induction equation and $-B\cdot\nabla\psi_{\mathrm{GLM}}$ in the energy (Eq. (3.7)) | largest modulus of the fast eigenvalues over the nodes | ratio $c_r=0.3$ (2D), 1 (3D), $h_i$ the local mesh function (page-local) |
| [Bhoriya et al. (2023)](/sources/bhoriya-2023.md) §2 | two-fluid relativistic plasma, Maxwell's equations in Munz et al.'s "perfectly hyperbolic" form | 1, for both the magnetic and the electric potential | — |

Dao & Nazarov's damping is $r_{\mathrm d}=c_rc_h/h_i$. Their printed coupling is not
the form above under a rescaling of $\psi_{\mathrm{GLM}}$ by a constant $c_h$, which
would need $-c_h\nabla\psi_{\mathrm{GLM}}$ in the induction equation; as printed,
the divergence obeys the damped wave equation with $c_h$ in place of $c_h^2$
*(compiler check, not in the sources)*. In
Bhoriya et al. the same construction also cleans Gauss's law for the
electric field, with a second potential (see
[relativistic hydrodynamics and MHD](/definitions/relativistic-hydrodynamics.md));
the divergence is monitored, not driven to zero.

## Conservative and non-conservative forms

In the entropy-stable DGSEM the GLM field changes the structure of the
system. Rueda-Ramírez et al. (2021) keep the non-conservative Powell term
and a GLM term "required by Galilean invariance", which the continuous
entropy analysis needs, and discretize them by two-point volume and surface
terms in the DGSEM and by central differences of interface means in their
subcell finite volumes; with Derigs et al.'s entropy-conservative flux the
scheme satisfies a generalized Tadmor condition that includes both terms,
and the element-wise blend is entropy stable (§2.2, §3, App. A;
[flux differencing](/methods/flux-differencing.md),
[entropy-conservative flux](/methods/entropy-conservative-flux.md),
[subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md)).
Rueda-Ramírez, Pazner & Gassner (2022) solve the conservative form instead,
because it fits their subcell-wise limiting, and leave the entropy proof for
that blending "still missing" (§4, §5.3). The two papers are compatible: they
trade the entropy proof against the limiting framework.

## Comparison with other divergence controls

- **With constrained transport.** Komissarov & Phillips choose GLM because it
  "delivers similar accuracy to CT (Mignone et al. 2010) for ideal MHD, but it
  is much easier to implement" (§3; also §1); the accuracy statement is cited, not
  tested. They also argue that CT's staggered and cell-centred fields are two
  different discrete solutions, and that the energy corrections proposed for
  them are not justified by an analysis (§1). For resistive relativistic MHD,
  [Mignone et al. (2024)](/sources/mignone-2024.md) recall that their earlier
  scheme, which applied CT to both the magnetic and the electric field, "has
  shown to be more robust when compared to cell-centred frameworks such as"
  GLM (§1); the new scheme applies CT to $B$ only.
- **With projection.** On a $40\times40$ $\mathbb P^1$ Orszag–Tang run, Dao &
  Nazarov find that projection, a pseudo-time variant and GLM all keep
  $\int\lvert\nabla\cdot B_h\rvert$ small, pseudo-time stepping being the most
  accurate and most expensive, and projection costing more than GLM because it
  solves a Poisson problem per step (§5.3, Fig. 5; cost stated, no timings).
- **As an error estimator.** Komissarov & Phillips use the residual
  $\nabla\cdot B$ that GLM leaves as an estimate of the field error $\delta B$
  in their criterion for conversion failures at high magnetization (§5.6).

## Uses in the benchmarks

GLM runs of the bundle include the
[Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) (Rueda-Ramírez et al.
2021, 2022; Dao & Nazarov 2022), the high-magnetization
[Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md), cylindrical
[explosions](/benchmarks/mhd-blast-wave.md) and
[Harris-sheet tearing](/benchmarks/tearing-mode-instability.md) of Komissarov
& Phillips, and the two-fluid relativistic tests of Bhoriya et al.

## Qualifications

- The two robustness statements above do not meet on a common case:
  Komissarov & Phillips speak of accuracy in ideal MHD and cite it,
  Mignone et al. of robustness in resistive relativistic MHD with an
  additional electric constraint, citing their own earlier paper. No source of
  the bundle compares GLM and CT on the same test.
- Komissarov & Phillips use $\kappa$ both for $\gamma/(\gamma-1)$ and for the
  damping rate (§3.1); the rate is written $r_{\mathrm d}$ here.
- Nothing in the sources bounds the divergence that remains after cleaning;
  the reported quantities are integrated or monitored divergences on
  particular runs.

# Citations

- [Komissarov & Phillips (2024)](/sources/komissarov-2024.md) — arXiv v3: §1; §3, §3.1, Eqs. (53)–(54); §5.6.
- [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) — arXiv v1: §2.2, Eqs. (13)–(15), (21)–(22); §3; §6; App. A.
- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — arXiv v2: §4; §5.3, Eqs. (51)–(52).
- [Dao & Nazarov (2022)](/sources/dao-2022.md) — arXiv v1: §3.2, Eqs. (3.6)–(3.7); §5.3, Fig. 5.
- [Bhoriya et al. (2023)](/sources/bhoriya-2023.md) — arXiv v2: §2, §6.
- [Mignone et al. (2024)](/sources/mignone-2024.md) — §1.
