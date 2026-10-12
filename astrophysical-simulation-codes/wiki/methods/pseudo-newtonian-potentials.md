---
type: Method
title: "Pseudo-Newtonian and generalized Newtonian potentials"
description: "Replacing the point-mass potential of a non-rotating black hole in a Newtonian code by the Paczyński–Wiita or Nowak–Wagoner potential, or by Tejeda and Rosswog's velocity-dependent generalized Newtonian potential, which reproduces exactly the Schwarzschild orbit shapes, characteristic radii, circular-orbit energy and angular momentum and pericentre advance, and adds a three-term acceleration to the code."
status: established
aliases: [pseudo-Newtonian potential, Paczyński–Wiita potential, Paczynski-Wiita potential, Nowak–Wagoner potential, generalized Newtonian potential, Tejeda–Rosswog potential]
tags: [pseudo-newtonian, relativity, hydro]
timestamp: 2026-10-12T00:00:00Z
---

# Pseudo-Newtonian and generalized Newtonian potentials

A Newtonian code can mimic motion around a non-rotating (Schwarzschild)
black hole of mass $M_{\mathrm{BH}}$ by replacing the point-mass potential
$\Phi_{\mathrm N} = -GM_{\mathrm{BH}}/r$ by a modified one. Below,
$r_{\mathrm g} = GM_{\mathrm{BH}}/c^2$, $r$ is the Schwarzschild radial
coordinate, dots are derivatives in Schwarzschild coordinate time, and
$r_{\mathrm{ph}}$, $r_{\mathrm{mb}}$, $r_{\mathrm{ms}}$ are the photon,
marginally bound and marginally stable circular-orbit radii ($3r_{\mathrm g}$,
$4r_{\mathrm g}$, $6r_{\mathrm g}$ in Schwarzschild). Unlike the registry's
$\Phi$, these potentials do not satisfy the Poisson equation for the
central mass; that is the meaning of "pseudo"
([Tejeda & Rosswog (2013)](/sources/tejeda-2013.md), footnote 1).

## Static potentials

([Tejeda & Rosswog (2013)](/sources/tejeda-2013.md), §1, eqs. 1.1–1.2.)
* **Paczyński–Wiita:** $\Phi_{\mathrm{PW}} = -GM_{\mathrm{BH}}/(r - 2r_{\mathrm g})$.
  Exact $r_{\mathrm{ms}}$ and $r_{\mathrm{mb}}$; circular-orbit binding
  energy within about 13% and angular momentum within 6%, but orbital
  frequency off by up to 50% and radial epicyclic frequency by up to 84%;
  pericentre advance about 30% low.
* **Nowak–Wagoner:**
  $\Phi_{\mathrm{NW}} = -\frac{GM_{\mathrm{BH}}}{r}\left(1 - \frac{3r_{\mathrm g}}{r} + \frac{12r_{\mathrm g}^2}{r^2}\right)$.
  Exact $r_{\mathrm{ms}}$, $r_{\mathrm{mb}}\sim3.5r_{\mathrm g}$; orbital
  frequency within 14%, radial epicyclic within 42%; a pericentre *lag* for
  most eccentricities.
* Others named: Wegg (2012) gets the pericentre shift of parabolic orbits
  within 1% but wrong $r_{\mathrm{ms}}$ and $r_{\mathrm{mb}}$; Kluźniak &
  Lee (2002) reproduce the epicyclic-to-orbital frequency ratio but give
  $r_{\mathrm{ms}} = 3r_{\mathrm g}$.

## The generalized Newtonian potential

[Tejeda & Rosswog (2013)](/sources/tejeda-2013.md) (§2) take the
low-energy limit of Schwarzschild geodesic motion, relativistic specific
energy close to $c^2$, which "does not necessarily imply low velocities or
weak field", and obtain the velocity-dependent potential
$$\Phi_{\mathrm G} = -\frac{GM_{\mathrm{BH}}}{r} - \frac{2r_{\mathrm g}}{r - 2r_{\mathrm g}}\left[\frac{r - r_{\mathrm g}}{r - 2r_{\mathrm g}}\,\dot r^2 + \frac{r^2\dot\varphi^2}{2}\right]$$
(eq. 2.10; $\varphi$ the in-plane angle), interpreted as the Newtonian
term plus the kinetic energy "being also gravitationally attracted". The
Lagrangian $\tfrac12(\dot r^2 + r^2\dot\varphi^2) - \Phi_{\mathrm G}$ conserves
an energy and an angular momentum exactly (eqs. 2.11–2.13). For
parabolic-like motion (relativistic specific energy exactly $c^2$) its
equations of motion coincide with the geodesic ones; otherwise they
differ only by a factor (the squared ratio of $c^2$ to the relativistic
specific energy) on the first term of $\ddot r$ (eqs. 2.14–2.19).

**Acceleration for a code** (App. A, eq. A.5): in Cartesian coordinates,
$$\ddot{\mathbf x} = -\frac{GM_{\mathrm{BH}}\mathbf x}{r^3}\left(1 - \frac{2r_{\mathrm g}}{r}\right)^2 + \frac{2r_{\mathrm g}\,(\mathbf x\cdot\dot{\mathbf x})}{r^2(r - 2r_{\mathrm g})}\,\dot{\mathbf x} - \frac{3r_{\mathrm g}\,\vert\mathbf x\times\dot{\mathbf x}\vert^2}{r^5}\,\mathbf x,$$
a gravity term, a term along the velocity and a term along the position.
The equations "can be implemented easily within existing Newtonian
hydrodynamics codes with hardly any additional computational effort"
(abstract, §4).

**What it reproduces** (§3; closed-form, test-particle):
* **Exactly:** $r_{\mathrm{ph}}$, $r_{\mathrm{mb}}$, $r_{\mathrm{ms}}$;
  the radial dependence of circular-orbit energy and angular momentum
  (eqs. 3.3–3.4); the spatial projection of every trajectory, hence the
  pericentre advance and the bound, unbound or trapped character
  (eqs. 3.20–3.25); and the ratios of epicyclic to orbital frequencies
  (eq. 3.15). Time dependence along an orbit is exact only for
  parabolic-like motion.
* **Approximately:** orbital and radial epicyclic frequencies within 5.7%
  for $r\ge6r_{\mathrm g}$ (eqs. 3.5, 3.13); note that in coordinate time
  the Newtonian potential gets the orbital frequency exactly (Table 1).
* **Worst case:** the thrust needed to hover statically, in error by up to
  63.7% for $r > 6r_{\mathrm g}$ and vanishing at $2r_{\mathrm g}$, explained
  as the potential describing an observer at infinity. It does reproduce
  the reversal of the centrifugal force at $3r_{\mathrm g}$, which the
  authors are "not aware of ... ever having been reproduced before by any
  pseudo-Newtonian potential" (§3.4, §4).

**Maximum errors for $r > 6r_{\mathrm g}$** (Table 1, copied):

| quantity | $\Phi_{\mathrm N}$ | $\Phi_{\mathrm{PW}}$ | $\Phi_{\mathrm{NW}}$ | $\Phi_{\mathrm G}$ |
|---|---|---|---|---|
| infall time, at rest at infinity | ≤16.7% | ≤23.8% | ≤9.3% | exact |
| infall time, $-0.3c$ at infinity | ≤15.9% | ≤24.3% | ≤15% | ≤2.9% |
| $r_{\mathrm{ph}}$ | − | 33.3% | − | exact |
| $r_{\mathrm{mb}}$ | − | exact | 13.4% | exact |
| $r_{\mathrm{ms}}$ | − | exact | exact | exact |
| circular-orbit energy | ≤50% | ≤12.5% | ≤3.3% | exact |
| circular-orbit angular momentum | ≤29.3% | ≤6.1% | ≤29.3% | exact |
| orbital frequency | exact | ≤50% | ≤13.4% | ≤5.7% |
| radial epicyclic frequency | ∞ | ≤83.7% | ≤41.4% | ≤5.7% |
| hover thrust | ≤18.4% | ≤83.7% | ≤32.1% | ≤63.7% |
| pericentre advance | − | ∼30% | >80% | exact |
| thin-disc efficiency | 45.7% | 9.3% | 2.9% | 2.9% |
| thin-disc flux | ∞ | ≤58.9% | ≤11.1% | ≤7.3% |

Recorded as printed: the disc-flux error of $\Phi_{\mathrm G}$ is "better
than 7%" in the abstract, ≤7.2% in §3.6 and ≤7.3% in Table 1.

## Use in a hydrodynamics code

The only hydrodynamic use is a tidal disruption in the authors' Newtonian
SPH code, unnamed but cited as Rosswog et al. (2008): a Sun-like $\gamma = 5/3$ polytrope on a
parabolic orbit with $r_{\mathrm t}/r_{\mathrm p} = 5$ around
$10^6M_\odot$, $10^4$ particles, four runs with $\Phi_{\mathrm N}$,
$\Phi_{\mathrm G}$, $\Phi_{\mathrm{PW}}$, $\Phi_{\mathrm{NW}}$
([Tejeda & Rosswog (2013)](/sources/tejeda-2013.md), §3.8, Fig. 8).
With $\Phi_{\mathrm G}$ the centre-of-mass track is "in very close
agreement" with the geodesic and the debris "closely resembles" the GR run
of Laguna et al. (1993); $\Phi_{\mathrm{PW}}$ gives about 70% of the
relativistic pericentre advance, $\Phi_{\mathrm{NW}}$ a shift of opposite
sign. The comparison is visual, at one resolution.

**Not stated** (§3.8): how the velocity-dependent acceleration is
integrated in time, any extra time-step limit, the treatment of fluid
self-gravity, or whether the conserved energy is monitored. The potential
is singular at $2r_{\mathrm g}$, covers only a non-rotating hole, and
includes no back-reaction. For Eulerian codes the authors suggest working
in the star's rest frame, possibly with a multipole expansion of the tidal
field, "beyond the scope of the current paper". Because the acceleration
is not the gradient of a static scalar field, energy-conserving
fixed-potential source discretizations (e.g. in
[Athena](/software/athena.md)) do not apply to it as they stand; this is
an inference, not a statement of the paper. The paper also asserts,
without derivation, that $\Phi_{\mathrm G}$, "contrary to a
pseudo-Newtonian potential", satisfies the Poisson equation when the
central mass is the only source (§3).

# Citations

1. [Tejeda & Rosswog (2013)](/sources/tejeda-2013.md), §§1–4, eqs. 1.1–3.25,
   A.5, Table 1, Fig. 8 (arXiv v2).
