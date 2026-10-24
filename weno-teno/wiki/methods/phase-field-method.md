---
type: Method
title: "Conservative phase-field interface methods"
description: "A phase-field flux added to the volume-fraction equation of a diffuse-interface model, and carried consistently into the mass, momentum and energy equations, holds material interfaces at a fixed thickness against numerical diffusion; the page records Huang and Johnsen's N-phase model, its admissibility constraints, and their reduction-consistent, bound-preserving discretization."
status: established
aliases: [phase-field method, Phase-Field mechanism, conservative Allen–Cahn, consistent and conservative phase-field method, reduction-consistent formulation, interface regularization]
tags: [interface-capturing, multiphase, bound-preserving, finite-volume, positivity]
timestamp: 2026-10-24T05:57:00Z
---

# Conservative phase-field interface methods

A material interface is a linearly degenerate (contact) wave: unlike a
shock it has no physical self-steepening, so the numerical diffusion of a
capturing scheme thickens it without bound, and non-uniformly where the
velocity field is non-uniform; higher order only delays the thickening
(§1 and Fig. 1 of [Huang & Johnsen (2023)](/sources/huang-2023.md),
citing Harten). A **phase-field method** counters this at the level of
the model: an extra flux in the volume-fraction equation, of
diffusion–sharpening type, drives the volume fraction towards a profile
of prescribed width, so that the interface stays a few cells thick for
the whole run. Huang & Johnsen build it into a compressible
diffuse-interface model for $N_\phi$ phases ($N_\phi$ registry §10) and require that the added flux
change neither the conservation of phase mass, momentum and energy nor
the equilibrium of an isolated interface. Other bundle sources hold the
interface sharp at the level of the reconstruction instead:
[THINC](/methods/thinc-reconstruction.md) profiles, which Huang & Johnsen
do not cite.

## The model

Let $\phi_k$ be the volume fraction and $\rho_k$ the phase density of
phase $k$ (registry §10), $v$ the single mixture velocity and $J_k$
(page-local) the phase-field flux of phase $k$, interpreted in mixture
theory as $\phi_k(v-v_k)$ with $v_k$ the phase velocity (page-local).
Let $K_k$ (page-local) be a compressibility coefficient with
$\sum_k\phi_kK_k=0$. The model of Huang & Johnsen (§2, Eqs. 1–8) reads

$$\begin{aligned}
&\partial_t\phi_k+\nabla\cdot(v\phi_k)=\nabla\cdot J_k+\phi_k(1+K_k)\Big(\nabla\cdot v-\sum_l\nabla\cdot J_l\Big),\\
&\partial_t(\phi_k\rho_k)+\nabla\cdot\big[(v\phi_k-J_k)\rho_k\big]=0,\\
&\partial_t(\rho v)+\nabla\cdot(\mathsf m\otimes v)=\nabla\cdot\sigma,\qquad \mathsf m=\sum_k(v\phi_k-J_k)\rho_k,\\
&\partial_t\big(\tfrac12\rho\lvert v\rvert^2+\rho e\big)+\nabla\cdot\Big(\mathsf m\tfrac12\lvert v\rvert^2+\sum_k(v\phi_k-J_k)\rho_ke_k\Big)=\nabla\cdot(v\cdot\sigma)+\nabla\cdot q_{\mathrm h}+\nabla\cdot q^{\mathrm{nc}},
\end{aligned}$$

with $\rho=\sum_k\phi_k\rho_k$, $\rho e=\sum_k\phi_k\rho_ke_k$, $\sigma$
the stress tensor, $q_{\mathrm h}$ the heat flux and $q^{\mathrm{nc}}$ an
energy flux associated with $J_k$ (page-local). No particular form of
$J_k$ is assumed. The mass flux $\mathsf m$ (page-local) in the momentum and kinetic-energy
fluxes is the "consistency of mass conservation" and "consistency of
mass and momentum transport" of the first author's incompressible work;
together they give the kinetic-energy balance
$\partial_t(\tfrac12\rho\lvert v\rvert^2)+\nabla\cdot(\mathsf m\tfrac12\lvert v\rvert^2)=v\cdot(\nabla\cdot\sigma)$,
and violating either adds the spurious source
$-\tfrac12\lvert v\rvert^2(\partial_t\rho+\nabla\cdot\mathsf m')$ for a mass
flux $\mathsf m'\ne\mathsf m$ (Theorem 2.1, Remark 2.1.1). The model conserves phase
mass, momentum and total energy and keeps $\sum_k\phi_k=1$ for any
$J_k$ (§2.1–2.4).

**Constraints on the phase-field flux** (§2.5–2.8), all proved:

- *Second law* (Theorem 2.2): the entropy inequality holds under a
  condition on $J_k$, $\sigma$ and the fluxes (Eq. 10); an admissible
  closure is a Newtonian stress, Fourier conduction,
  $q^{\mathrm{nc}}=p\sum_lJ_l$ and $\sum_l(J_l-\mathsf b_l\nabla p)=0$
  with $\mathsf b_l\ge0$ (page-local; Eq. 14).
- *Galilean invariance* (Theorem 2.3) if $J_k$, $K_k$, $\sigma$ and the
  fluxes are frame indifferent.
- *Interface equilibrium* (Theorem 2.4): if $\nabla\cdot J_k=0$ for all
  $k$ at $t=0$, constant $\rho_k$, $v$, $p$ and temperature are kept and
  the volume fractions are only translated; if $\sum_lJ_l=0$, this holds
  for any initial volume fractions (Remark 2.4.1). This is the continuous
  form of [pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md).
- *Consistency of reduction* (Theorem 2.5): an $N_\phi$-phase system must
  recover the $M_\phi$-phase one where $N_\phi-M_\phi$ phases are absent (page-local $M_\phi<N_\phi$); it holds if
  $J_k=0$ where phase $k$ is locally absent and the other fluxes reduce
  to those of the $(N_\phi-1)$-phase system (Eq. 21).

The favourable case is $\sum_kJ_k=0$: it satisfies the second law with
$q^{\mathrm{nc}}=0$, decouples the volume-fraction equations, and keeps
equilibrium for any initial volume fractions (§2.10). Cahn–Hilliard and
conservative Allen–Cahn models supply such fluxes.

**The compressibility coefficient.** With $K_k=0$ (Allaire et al.) the
mixture $\rho c^2$ is a convex combination of the phase values; with
$K_k=\rho c^2/(\rho_kc_k^2)-1$ (Kapila et al.) the Wood sound speed
follows (§2.9, Eq. 25; [five-equation model](/definitions/five-equation-model.md)).
In the incompressible limit the volume-fraction and mass equations are
consistent only if $K_k=-1$; Kapila's coefficient satisfies this,
Allaire's does not, and the consistent incompressible phase-field model
of the first author is recovered (§5.3). All computations nevertheless
use $K_1=0$.

## Discretization

Huang & Johnsen solve the two-phase system ($J_2=-J_1$, Eq. 26) by
splitting each Runge–Kutta stage into a hyperbolic step and a
phase-field step (§3.4).

**Hyperbolic step** (§3.1). The five-equation model by finite volumes:
MUSCL reconstruction of the primitive variables with a TVD limiter
(minmod by default), the [HLLC solver](/methods/hll-riemann-solvers.md),
and the face velocity of the volume-fraction source $\nabla\cdot v$
taken from the Riemann solution, which is required for consistency of
reduction (Theorem A.1). They state a first requirement:

- **Consistent reconstruction of mass and volume fraction**
  (Definition 1): where $\rho_k$ is constant, the reconstructed partial
  density must equal $\rho_k$ times the reconstructed volume fraction. It
  holds if both are reconstructed by the same scheme and the scheme
  commutes with affine maps $f\mapsto af+b$ (MUSCL with most TVD
  limiters). Reconstruction in [characteristic variables](/methods/characteristic-decomposition.md)
  breaks it, so only velocity and pressure are kept from the
  characteristic reconstruction and the partial densities and volume
  fraction are reconstructed from primitive variables.

**Phase-field step** (§3.2). A conservative update
$\partial_tu+\nabla\cdot(-\tilde F^{\mathrm{PF}})=0$ (Eq. 28) with the
discrete phase-field fluxes of all conserved variables. Let $\Upsilon$
(page-local) be an auxiliary potential, and $f^{\uparrow}$, $f^{\downarrow}$
(page-local) the upwind and downwind reconstructed face values of $f$
with respect to the direction of $\nabla\Upsilon$. The
**reduction-consistent formulation** (Eq. 29) is

$$\tilde J_1=\phi_1^{\downarrow}(1-\phi_1)^{\uparrow}\,\nabla\Upsilon,\qquad
(\tilde J_1\rho_1)=(\phi_1\rho_1)^{\downarrow}(1-\phi_1)^{\uparrow}\nabla\Upsilon,\qquad
(\tilde J_1\rho_2)=\big((1-\phi_1)\rho_2\big)^{\uparrow}\phi_1^{\downarrow}\nabla\Upsilon,$$

so the mass fluxes are formed from the partial densities without ever
computing $\rho_1$ or $\rho_2$ (Eq. 30), and the internal-energy fluxes
from the stiffened-gas coefficients and upwind or downwind pressures
(Eq. 31; [stiffened gas](/definitions/stiffened-gas-equation-of-state.md)).
It is a special case of the first author's "consistent formulation" and
satisfies the second requirement:

- **Consistent computation of phase-field fluxes of mass and volume
  fraction** (Definition 2): where $\rho_k$ is constant, the mass flux
  must equal $\rho_k$ times the volume-fraction flux.

$\nabla\Upsilon$ solves the linear Poisson-type equation
$\nabla\cdot(\{\!\{\phi_1\}\!\}\{\!\{1-\phi_1\}\!\}\nabla\Upsilon)=\nabla\cdot J_1$
(Eq. 43), with face values by linear interpolation (an overbar in the source; the arithmetic mean $\{\!\{\cdot\}\!\}$ on a uniform grid),
central differences, homogeneous Neumann conditions and $10^{-6}$ added
to the coefficient; the exact, nonlinear version (Eq. 42) would need the
upwind–downwind products. The replacement costs at most $O(\Delta x)$
near interfaces, where the capturing scheme is anyway below first order
(§3.2.4). The divergence $\nabla\cdot J_1$ comes from the conservative
Allen–Cahn model of Brassel and Bretin,
$\partial_t\phi_1=\Gamma_{\mathrm m}\nabla^2\phi_1-\frac{\Gamma_{\mathrm m}}{\varepsilon_{\mathrm I}^2}g_{\mathrm w}'(\phi_1)+\sqrt{g_{\mathrm w}(\phi_1)}\,\frac{\int_\Omega\frac{\Gamma_{\mathrm m}}{\varepsilon_{\mathrm I}^2}g_{\mathrm w}'\,d\Omega}{\int_\Omega\sqrt{g_{\mathrm w}}\,d\Omega}$,
$g_{\mathrm w}(z)=z^2(1-z)^2$ (Eq. 44), with page-local mobility
$\Gamma_{\mathrm m}=0.5\,\varepsilon_{\mathrm I}\max\lvert v\rvert$ and
interface-thickness parameter $\varepsilon_{\mathrm I}$ (§3.3). The
scheme is at best second order and runs at CFL $\le0.5$, with
sub-cycling of the phase-field step when its own step limit is smaller
than the hyperbolic one (§3.4).

## Proved discrete properties

- **Equilibrium**: after the phase-field step $v=v_0$ and $p=p_0$, for
  any explicit time integrator and finite-volume divergence (Theorem 3.1);
  with Definition 1 alone the hyperbolic step also keeps the temperature
  (Theorem 5.2), a condition the authors call weaker than that of Beig
  and Johnsen, and Definition 2 does the same for the phase-field step
  (Theorem 5.4).
- **Bounds**: with first-order reconstruction and forward Euler, the
  flux
  $(\tilde J_1)_{i+1/2}=\phi_{1,i+1}(1-\phi_1)_i\max(\partial_x\Upsilon_{i+1/2},0)+\phi_{1,i}(1-\phi_1)_{i+1}\min(\partial_x\Upsilon_{i+1/2},0)$
  (Eq. 38) keeps $\phi_1\in[0,1]$ and both partial densities non-negative
  under Eq. (37), or under the simpler
  $2\Delta t\max_i\lvert\partial_x\Upsilon\rvert/\Delta x\le1$ (Eq. 41),
  "a CFL condition with $\lvert\partial_x\Upsilon\rvert$ playing the role
  of velocity magnitude" (Theorem 3.2). The high-order extension uses a
  Zhang–Shu Gauss–Lobatto decomposition of the cell averages and
  positivity of the reconstructions at the Gauss–Lobatto points, with
  step $\frac{\Delta t}{\mathsf w_{\mathrm{GL}}}\max_i\lvert\partial_x\Upsilon\rvert/\Delta x\le1$
  (Appendix B, Theorems B.3–B.4, Eq. B.12; page-local $\mathsf w_{\mathrm{GL}}$
  the endpoint weight, $\tfrac12$ at second order). See
  [bound preservation](/properties/bound-preservation.md).
- **Allen–Cahn bounds**: with an implicit Laplacian and
  $\Gamma_{\mathrm m}\Delta t/\varepsilon_{\mathrm I}^2\le\tfrac14$ the
  update keeps $\phi_1\in[0,1]$, citing the first author's earlier work;
  the chosen mobility gives $\max\lvert v\rvert\Delta t/\varepsilon_{\mathrm I}\le\tfrac12$,
  less restrictive than the hyperbolic CFL (§3.3).
- **Total variation**: $\phi_1$ and both partial densities are stated to
  be TVD in the first-order phase-field step under Eq. (41) (Theorem C.1;
  see Qualifications).

## Evidence

Huang & Johnsen measure the interface thickness by the page-local
$N_{\mathrm I}$, the average number of cells with $0.05\le\phi_1\le0.95$
(Eq. 47).

| Test (§4–5) | Set-up | Result |
|---|---|---|
| air–helium Riemann problem | 200 cells, $t=0.4$, $\varepsilon_{\mathrm I}/\Delta x=1.5$ | $N_{\mathrm I}$ stays at 6–7 cells, grows without bound without the phase-field step; with it the volume fraction is insensitive to the TVD limiter (Fig. 3) |
| same, $\varepsilon_{\mathrm I}/\Delta x$ from 0.1 to 2 | | 1–2 cells at 0.1, 8–9 at 2.0; below 1 mass overshoots appear near the interface; $\Delta x\le\varepsilon_{\mathrm I}\le2\Delta x$ recommended (Fig. 4) |
| [gas–liquid Riemann problem](/benchmarks/gas-liquid-riemann-problems.md) | 1000 cells, $\varepsilon_{\mathrm I}/\Delta x=1$ | interface at 4–5 cells (Fig. 5) |
| [advection of a water disk in air](/benchmarks/material-interface-advection.md) | $100^2$, density ratio about 1000, one period | without phase field the disk turns diamond-shaped from mesh anisotropy; with it 4–5 cells and a circular shape; conservation and $v$, $p$ errors at round-off in both cases (Figs. 6–7) |
| [shock–bubble interaction](/benchmarks/shock-bubble-interaction.md) | Mach 1.22 air shock on helium, $200\times100$ | interface held at 4–5 cells; without phase field air diffuses into the bubble (Figs. 8–9) |

**Violating the consistency requirements** (§5.1). Reconstructing the
partial densities by WENO5 with a positivity limiter and the volume
fraction by MUSCL (Definition 1 broken) creates mass spikes at the
interface; updating the volume fraction by $\nabla\cdot J_1$ and the
masses by $\tilde J_1$ (Definition 2 broken) creates mass spikes of up to
40 % and a thickened mass interface, although conservation, boundedness
and equilibrium hold and, the authors state, the volume fraction is similar
(Figs. 10–12). Initializing the volume fraction exactly at 0 and 1 gives
negative round-off values after a few steps in the shock–bubble run,
with or without phase field; $[10^{-15},1-10^{-15}]$ avoids it (§4.4).

## Relation to other approaches

Huang & Johnsen list earlier compressible phase-field methods (Shukla,
Pantano and Freund; Tiwari, Freund and Pantano; Jain, Mani and Moin; So,
Hu and Adams) as tied to a specific $J_1$, as needing assumptions on the
phase densities (small normal gradients, constant densities, or
$\rho_k=(\phi_k\rho_k)/\phi_k$, not robust near 0 and 1), as not
guaranteeing boundedness and positivity together, and as limited to
second order; the first two violate mass conservation, and "there may be
an $O(1)$ model error" between the solved and the theoretical models
(§1, §3.2). These are the authors' characterizations; none of those works
is a source of this bundle. The [five-equation model](/definitions/five-equation-model.md)
is the hyperbolic part of their system; [level-set methods](/methods/level-set-method.md)
keep the interface sharp by a separate distance function instead.

## Qualifications

- The TVD proof of Theorem C.1 has a gap. Its Eq. (C.2) writes
  $(\tilde J_1)_{i+1/2}-(\tilde J_1)_i$, with $(\tilde J_1)_i$ defined by
  Eq. (C.1), as a single factor times $(\phi_{1,i+1}-\phi_{1,i})$. From
  Eqs. (38) and (C.1) the minimum terms cancel and the difference is
  $\phi_{1,i+1}(1-\phi_1)_i\max(\partial_x\Upsilon_{i+1/2},0)-\phi_{1,i}(1-\phi_1)_{i-1}\max(\partial_x\Upsilon_{i-1/2},0)$,
  which is non-zero when $\phi_{1,i+1}=\phi_{1,i}$: with all three volume
  fractions $0.5$, $\partial_x\Upsilon_{i+1/2}=1$ and
  $\partial_x\Upsilon_{i-1/2}=0$ it equals $0.25$, while the right side
  of (C.2) vanishes *(compiler check, not in the sources)*. The bound
  preservation of Theorem 3.2 does not use (C.2).
- The water-disk test is described as a water disk in air with phase 1
  air, but Eq. (50) prints $\phi_1=1$ inside the disk; one of the two is
  inverted. Eqs. (49)–(50) print the initial data without the scaling
  that the dimensional stiffened-gas parameters require.
- The reconstruction is MUSCL; the method is at best second order, and
  "high-order" in the paper refers to the bound-preservation analysis
  of Appendix B.

# Citations

- [Huang & Johnsen (2023)](/sources/huang-2023.md) — §1; §2.1–2.10, Eqs. (1)–(25), Theorems 2.1–2.5; §3.1–3.4, Eqs. (26)–(47), Definitions 1–2, Theorems 3.1–3.2; §4.1–4.4, Figs. 2–9; §5.1–5.3, Theorems 5.2, 5.4; Appendices A–C, Eqs. (B.12), (C.1)–(C.2).
