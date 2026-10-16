---
type: Method
title: "Particle-to-finite-element moment projection"
description: "Weak-form (L2) projection of marker-particle moments onto the finite-element basis of an MHD code: the mass matrix is factorized once, the right-hand side is a weighted sum of basis functions at the marker positions, and optional Laplacian or biharmonic regularization and time accumulation control Monte Carlo noise and conservation."
status: established
aliases: [moment projection, particle deposition, L2 projection of particle moments, PIC moment projection]
tags: [particles, finite-elements, hybrid-kinetic, numerics]
timestamp: 2026-10-16T12:00:00Z
---

# Particle-to-finite-element moment projection

A hybrid particle–fluid code has to turn a set of weighted markers into a
field that the fluid equations can use. In finite-element MHD codes this is
done by a Galerkin ($L^2$) projection: the moment is sought in the
finite-element space and its weak form is matched to the particle sum. The
same operation serves impurities, neutrals, runaway electrons and
energetic particles ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md),
§2.10; [Korving et al. (2023)](/sources/korving-2023.md), §IV A;
[Hu et al. (2021b)](/sources/hu-2021-b.md), §2.3;
[Bogaarts et al. (2022)](/sources/bogaarts-2022.md), §II).

## The projection

Let $\Lambda_k(\mathbf x)$ be the basis functions (in
[JOREK](/software/jorek.md), products of the poloidal
[Bézier–Hermite functions](/methods/bezier-finite-elements.md) and the
toroidal Fourier harmonics), and let marker $p$ at $\mathbf x_p$ carry
weight $w_p$ and the quantity $a_p$ (mass, momentum, energy, a pressure
component, a radiated power). The moment density
$M(\mathbf x)=\sum_pw_pa_p\,\delta(\mathbf x-\mathbf x_p)$ is represented as
$\tilde M=\sum_kM_k\Lambda_k$, with coefficients fixed by
$$\int\Lambda_j\,\tilde M\,dV=\int\Lambda_j\,M\,dV=\sum_p w_pa_p\,\Lambda_j(\mathbf x_p)\qquad\text{for all }j$$
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), Eqs. 45–47;
[Korving et al. (2023)](/sources/korving-2023.md), Eq. 22). The left-hand
side is the mass matrix, which depends only on the geometry of the
elements; it is factorized once and reused at every projection, so any
number of moments costs one factorization
([Korving et al. (2023)](/sources/korving-2023.md), §IV A).

## Regularization

The particle sum is noisy, so a smoothing operator is added to the
left-hand side:

- JOREK 2021: $\int\Lambda_j\,(1+\alpha_4\nabla^4)\tilde M\,dV=\int\Lambda_jM\,dV$
  with $\alpha_4\sim10^{-10}$–$10^{-12}$ depending on the application
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), Eq. 48).
- JOREK kinetic neutrals: $\int\Lambda_j\,(1-\alpha_2\nabla^2-\alpha_4\nabla^4)\tilde M\,dV=\int\Lambda_jM\,dV$,
  with coefficients that may differ for the $n=0$ harmonic and the higher
  harmonics and between the parallel and perpendicular directions
  ([Korving et al. (2023)](/sources/korving-2023.md), Eq. 23, checked on the
  printed page).
- For energetic-particle pressures, smoothing terms are "always chosen
  small enough not to affect physical results"
  ([Bogaarts et al. (2022)](/sources/bogaarts-2022.md), §II).

The two printed JOREK forms carry opposite signs on the fourth-order term
(see Contradictions). With positive coefficients, $1-\alpha_2\nabla^2+\alpha_4\nabla^4$
is the positive-definite smoothing operator (in Fourier space
$1+\alpha_2k^2+\alpha_4k^4$); its smoothing length scales as
$\alpha_2^{1/2}$ or $\alpha_4^{1/4}$ (compiler's remark).

## Time accumulation

Particles are pushed with many steps per fluid step: 100–1000 for fast
particles, 1–10 for slow heavy impurities
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.10). Two options exist
for what is projected:

- a **time-integrated source**, summed over every particle step of the
  fluid step, "typically required for good conservation properties for
  particle/energy sources" ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md),
  §2.10). Korving et al. found collecting the contributions "at every
  particle time step" essential for the conservation of the coupled
  system (§IV A), and the
  [collisional-radiative impurity model](/methods/collisional-radiative-impurity-model.md)
  accumulates the ionization energy per particle step and divides by the
  fluid step ([Hu et al. (2021b)](/sources/hu-2021-b.md), Eq. 5);
- an **instantaneous** or orbit-averaged value, used for fast-particle
  pressures: the energetic-particle pressure tensor is averaged over
  several orbits, commonly one MHD step, and entered as an explicit
  momentum source while the bulk MHD stays implicit
  ([Bogaarts et al. (2022)](/sources/bogaarts-2022.md), §II).

The projected sources are explicit in the implicit fluid step
([kinetic neutral model](/methods/kinetic-neutral-model.md);
[hybrid kinetic-MHD models](/methods/hybrid-kinetic-mhd.md)).

## Uses in the sources

- **Impurities**: ionization power, radiated power, $Z_{\mathrm{eff}}$, mean
  charge and density of the CR impurity markers
  ([Hu et al. (2021b)](/sources/hu-2021-b.md), §2.3, projection method from
  van Vugt (2019)).
- **Neutrals**: mass, momentum and energy sources of ionization, charge
  exchange and radiation ([Korving et al. (2023)](/sources/korving-2023.md),
  Eqs. 22–25).
- **Energetic particles**: the CGL pressure tensor
  $p_{\parallel h}\mathbf b\mathbf b+p_{\perp h}(\mathsf I-\mathbf b\mathbf b)$
  deposited from full-orbit markers for
  [pressure coupling](/methods/pressure-and-current-coupling.md)
  ([Bogaarts et al. (2022)](/sources/bogaarts-2022.md), §II, Eq. 2);
  current coupling was implemented but "too noisy to obtain useful
  results".
- **M3D-C1-K**: $\delta f$ parallel and perpendicular pressures projected by
  the same Galerkin weak form onto M3D-C1's test functions, followed by a
  mass-matrix solve, with a $\delta$-function particle shape
  ([Liu et al. (2022)](/sources/liu-2022.md), Eqs. 15–18). The authors note
  that the $\delta$ shape gives noisy, spiky pressures with high-order
  polynomials, and that a finite-width shape would also require finite-width
  field interpolation (see [M3D-C1-K](/software/m3d-c1-k.md),
  [δf method](/methods/delta-f-method.md)).

- **Runaway-electron advection (M3D-C1)**: the semi-Lagrangian scheme
  places one massless pseudo-particle at every quadrature point (125 per
  element) and projects the pulled-back $n_{\mathrm{RE}}/B$ by the same mass
  matrix. The right-hand side is then an ordinary quadrature sum. The
  projected quantity stays a field, with no marker sampling and no particle
  noise, so no smoothing operator is used
  ([Liu et al. (2021)](/sources/liu-2021.md), §3, Eq. 14; see
  [advection by characteristics](/methods/runaway-electron-advection-by-characteristics.md)).
- **CR impurities in 3D**: the marker moments $Z_{\mathrm{eff}}$, ionization
  power and radiated power are projected in 3D ITER SPI runs with toroidal
  harmonics up to $n=11$ ([Hu et al. (2023)](/sources/hu-2023.md), §2.1–2.2).

Grid-based codes deposit differently: [GMEC](/software/gmec.md) scatters
marker pressures trilinearly to the 8 neighbouring nodes and adds a smoothing
diffusion of the deposited pressure with coefficient $10^{-6}$ (normalized),
which "affect[s] little" the growth rate and frequency
([Liu et al. (2024)](/sources/liu-2024.md), §II A, Eqs. 20–22), and
[HYMAGYC](/software/hymagyc.md) evaluates $\nabla\cdot\mathsf P_h$ on a
separate Cartesian $(R,Z)$ grid whose coarseness filters short-scale noise
([Vlad et al. (2025)](/sources/vlad-2025.md), §3, Fig. 7).

## Contradictions

**Sign of the fourth-order regularization term** — Open.
[Hoelzl et al. (2021)](/sources/hoelzl-2021.md) (Eq. 48) print the JOREK
smoothing operator as $1+\alpha_4\nabla^4$. [Korving et al. (2023)](/sources/korving-2023.md)
(Eq. 23) print $1-\alpha_2\nabla^2-\alpha_4\nabla^4$ for the same JOREK
projection. For a positive coefficient the second form is anti-smoothing
in the fourth-order term. Neither paper states the sign convention of its
coefficients, so the printed forms cannot both describe a positive
smoothing coefficient. The code, or a paper that states the coefficient
values with their signs, would settle it.

# Citations

- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — §2.10, Eqs. 45–48.
- [Korving et al. (2023)](/sources/korving-2023.md) — §IV A, Eqs. 22–25.
- [Hu et al. (2021b)](/sources/hu-2021-b.md) — §2.3, Eq. 5.
- [Bogaarts et al. (2022)](/sources/bogaarts-2022.md) — §II, Eq. 2.
- [Liu et al. (2022)](/sources/liu-2022.md) — Eqs. 15–18.
- [Liu et al. (2024)](/sources/liu-2024.md) — §II A, Eqs. 20–22.
- [Vlad et al. (2025)](/sources/vlad-2025.md) — §3, Fig. 7.
- [Liu et al. (2021)](/sources/liu-2021.md) — §3, Eq. 14.
- [Hu et al. (2023)](/sources/hu-2023.md) — §2.1–2.2.
