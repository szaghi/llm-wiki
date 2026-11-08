---
type: Definition
title: "Notation registry"
description: "Normative symbol registry of the bundle: Eulerian and Lagrangian descriptions, the immersed boundary and its configuration, regularized delta functions and the spreading and interpolation operators, forcing, penalization, cut-cell geometry and redistribution, interface jumps, level sets and ghost states, and the compressible-flow symbols; every concept page writes mathematics in this notation, never in paper-native symbols."
status: established
tags: [notation, meta]
timestamp: 2026-11-08T18:48:00Z
---

# Notation registry

Every concept page of this bundle writes mathematics in the symbols below.
A source's own symbols are translated on its Source page (`# Notation map`).
The registry was seeded on 2026-11-08 from chunk 1, the founding papers:
Peskin (1972) and Peskin (2002) on the immersed boundary method, Goldstein,
Handler and Sirovich (1993) on feedback forcing, LeVeque and Li (1994) on the
immersed interface method, Pember et al. (1995) on the embedded-boundary
(cut-cell) method with redistribution, Fedkiw et al. (1999) on the ghost fluid
method, Ye et al. (1999) on the cut-cell finite-volume method, Angot, Bruneau
and Fabrie (1999) on penalization, Fadlun et al. (2000) on direct forcing and
Kim, Kim and Choi (2001) on direct forcing with a mass source. The
Lagrangian–Eulerian symbols follow Peskin (2002), whose notation the
continuous-forcing literature shares; the cut-cell symbols follow the
volume-fraction description of Pember et al. Extend this registry, and log
the extension, before writing a symbol it lacks.

**Conventions that the sources split on, fixed here.** The body (solid,
obstacle) is $\Omega_s$ and the fluid $\Omega_f$; the immersed boundary or
interface is $\Gamma$, never $B$, $S$ or $F$. The unit normal $\mathbf n$ on
$\Gamma$ points **out of the body into the fluid**; a source that points it
the other way (Fedkiw et al. from the negative to the positive level set,
LeVeque and Li toward the "+" side) is translated on its Source page. The
Lagrangian force density is $\mathbf F$ (force per unit Lagrangian measure)
and the Eulerian force density $\mathbf f$ (force per unit volume), as in
Peskin (2002); the boundary-element force of Goldstein et al. and of the
direct-forcing papers is $\mathbf f$ evaluated at a forcing point. The
regularized delta function is $\delta_h$ and its one-dimensional kernel
$\varphi$ (varphi), because $\phi$ is the level set. The penalization
parameter is $\eta$ with the body mask $\chi_s$ multiplying $\eta^{-1}$, as in
Angot et al.; its inverse $1/\eta$ is never written $\lambda$ or $C$. The
volume fraction of a cut cell is $\kappa$, never $\Lambda$ or $A$; the
conserved variables of compressible flow are $\mathbf q$, never $\mathbf U$,
which would collide with velocity. A **jump** is outside minus inside, or
"$+$" minus "$-$" with the "$+$" side named on the page:
$[w]=w^+-w^-$.

## Domain, grid and time

| symbol | meaning |
|---|---|
| $\Omega$, $\Omega_f$, $\Omega_s$ | computational domain, fluid region, body (solid, obstacle) region; $\Omega=\Omega_f\cup\Omega_s$ for a fictitious-domain formulation |
| $\Gamma$ | immersed boundary or interface; for a rigid body $\Gamma=\partial\Omega_s$; an elastic membrane is a surface $\Gamma$ with fluid on both sides |
| $\mathbf n$, $\boldsymbol\tau$ | unit normal on $\Gamma$ (out of the body), unit tangent |
| $\chi_s$ | characteristic function (mask) of $\Omega_s$: $1$ in the body, $0$ in the fluid |
| $\mathbf x=(x_1,x_2,x_3)$, $d$ | Eulerian position, space dimension |
| $h$, $h_{\Gamma}$ | Eulerian mesh width; spacing of the Lagrangian points along $\Gamma$ |
| $\mathbf i=(i,j,k)$, $\mathbf x_{\mathbf i}$ | multi-index of a grid point or cell, its position |
| $\mathbf e_m$ | unit vector of direction $m$ |
| $t$, $\Delta t$, $n$ | time, time step, time level (superscript) |
| $k$ | polynomial degree of a discretization (finite element, discontinuous Galerkin, reconstruction polynomial) |
| $p$ | pressure; the **order of accuracy** is written $r$ ("order $r$") so that $p$ is never overloaded |

## Fluid

| symbol | meaning |
|---|---|
| $\mathbf u$ | Eulerian velocity |
| $\rho$, $\mu$, $\nu$ | density, dynamic and kinematic viscosity |
| $\mathbf f_0$ | external body force (distinct from the immersed-boundary force density $\mathbf f$) |
| $\boldsymbol\Sigma$ | Cauchy stress |
| $\mathbf U_\ell$ | velocity interpolated at Lagrangian point $\ell$ |
| $Re$, $M$, $St$ | Reynolds, Mach and Strouhal numbers |
| $C_D$, $C_L$ | drag and lift coefficients |
| $\mathbf q$ | conserved variables of a compressible system ($\rho$, $\rho\mathbf u$, $E$) |
| $E$, $e$ | total energy per unit volume, internal energy per unit mass |
| $\gamma$ | ratio of specific heats |
| $\boldsymbol{\mathcal F}(\mathbf q)$, $\hat{\mathcal F}$ | physical flux, numerical flux |
| $\mathcal P$ | projection onto discretely divergence-free fields (Leray / Chorin projection) |

## Lagrangian description of the immersed boundary

| symbol | meaning |
|---|---|
| $\mathbf s$ (scalar $s$ on a curve) | Lagrangian (material) coordinates labelling points of the immersed structure; Peskin's $(q,r,s)$ |
| $\mathbf X(\mathbf s,t)$ | position of material point $\mathbf s$ at time $t$ (configuration) |
| $\mathbf X_\ell$, $\ell=1,\dots,N_\Gamma$ | discrete Lagrangian (marker, forcing) points |
| $\mathbf F(\mathbf s,t)$ | Lagrangian force density exerted by the structure on the fluid |
| $\mathbf f(\mathbf x,t)$ | Eulerian force density (body force per unit volume) |
| $\mathcal E[\mathbf X]$ | elastic energy functional; $\mathbf F=-\wp\mathcal E/\wp\mathbf X$ (Fréchet derivative) |
| $M_\Gamma(\mathbf s)$ | Lagrangian mass density of the structure |
| $T$, $k_s$, $\ell_0$ | fibre tension, spring stiffness, rest length |
| $\mathbf u_\Gamma$ | prescribed velocity of the boundary (the target velocity of a forcing scheme) |
| $\mathbf u_c$, $\boldsymbol\omega_c$, $\mathbf x_c$ | translational velocity, angular velocity and centre of a rigid body (particle); $\mathbf u_\Gamma=\mathbf u_c+\boldsymbol\omega_c\times(\mathbf X-\mathbf x_c)$ |
| $\mathbf x_{BI}$, $\mathbf x_{IP}$, $\Delta l$ | boundary intercept (foot of the normal from a ghost point), image point in the fluid, ghost-to-image distance |
| $\mathbf f_b$, $[L]$, $[L']$ | forcing of the whole flow system and the unmodified and modified discrete operators in the continuous/discrete forcing classification |

## Coupling operators

| symbol | meaning |
|---|---|
| $\delta$ | Dirac delta in $d$ dimensions |
| $\delta_h$ | regularized (discrete, smoothed) delta function of width $O(h)$; tensor-product form $\delta_h(\mathbf x)=h^{-d}\prod_m\varphi(x_m/h)$ |
| $\varphi(r)$ | one-dimensional kernel of $\delta_h$, $r$ in mesh units; its support half-width is written $w$ ("$w$-point" kernels have support $2w$) |
| $\mathcal S$ | spreading: Lagrangian density → Eulerian density, $\mathbf f(\mathbf x)=\sum_\ell \mathbf F_\ell\,\delta_h(\mathbf x-\mathbf X_\ell)\,\Delta s_\ell$ |
| $\mathcal J$ | interpolation: Eulerian field → Lagrangian value, $\mathbf U_\ell=\sum_{\mathbf i}\mathbf u_{\mathbf i}\,\delta_h(\mathbf x_{\mathbf i}-\mathbf X_\ell)\,h^d$ |
| $\langle\cdot,\cdot\rangle_h$, $\langle\cdot,\cdot\rangle_\Gamma$ | Eulerian and Lagrangian discrete inner products |

## Forcing and penalization

| symbol | meaning |
|---|---|
| $\alpha_f$, $\beta_f$ | gains of feedback forcing, $\mathbf f=\alpha_f\int_0^t(\mathbf u-\mathbf u_\Gamma)\,dt'+\beta_f(\mathbf u-\mathbf u_\Gamma)$; both negative; dimensions $1/T^2$ and $1/T$ per unit density |
| $\tilde{\mathbf u}$ | provisional velocity of a time step computed without the forcing (direct forcing) |
| $\mathbf V$ | target velocity imposed at a forcing point, reconstructed from $\mathbf u_\Gamma$ and nearby fluid values |
| $q_m$ | mass source/sink in cut cells ($\nabla\cdot\mathbf u=q_m$) |
| $\eta$ | penalization parameter (dimensionless permeability); the penalty term is $\eta^{-1}\chi_s(\mathbf u-\mathbf u_\Gamma)$ |

## Cut cells (embedded boundaries)

| symbol | meaning |
|---|---|
| $\kappa_{\mathbf i}$ | volume fraction of cell $\mathbf i$ inside $\Omega_f$; $\kappa=1$ regular (full) cell, $0<\kappa<1$ cut (mixed, irregular) cell, $\kappa=0$ body cell |
| $a_{\mathbf i+\frac12\mathbf e_m}$ | area (aperture) fraction of a cell face |
| $\mathbf q^{\mathrm{ref}}$, $\mathbf q^{\mathrm c}$ | reference (non-conservative, body-ignoring) update and conservative update of a cut cell |
| $\delta\mathbf M_{\mathbf i}$ | conserved-quantity deficit of a cut cell to be redistributed |
| $w_{\mathbf i\mathbf j}$ | redistribution weights from cut cell $\mathbf i$ to neighbour $\mathbf j$ |

## Surrogate boundaries and redistribution neighbourhoods

| symbol | meaning |
|---|---|
| $\tilde\Omega$, $\tilde\Gamma$, $\tilde{\mathbf n}$ | surrogate domain of whole mesh elements, its boundary, its normal (shifted boundary method) |
| $\mathcal M$, $\mathbf d$ | map from $\tilde\Gamma$ to $\Gamma$ (closest-point projection) and distance vector $\mathbf d=\mathcal M(\tilde{\mathbf x})-\tilde{\mathbf x}$ |
| $S^m_h$ | Taylor shift operator of order $m$, $S^m_hu=\sum_{j\le m}\partial^j_{\mathbf d}u/j!$ |
| $M_{\mathbf i}$, $N_{\mathbf k}$, $\hat{\mathbf q}_{\mathbf i}$ | merging neighbourhood of cell $\mathbf i$, overlap count of cell $\mathbf k$, neighbourhood average (state redistribution) |
| $V_{\mathbf k}$ | cell volume $\kappa_{\mathbf k}h^d$ |

## Interfaces, jumps and level sets

| symbol | meaning |
|---|---|
| $[w]$ | jump of $w$ across $\Gamma$, "$+$" side minus "$-$" side |
| $\beta(\mathbf x)$ | (possibly discontinuous) coefficient of an elliptic interface problem $\nabla\cdot(\beta\nabla u)+\kappa_0 u=f_0$; $\kappa_0$, $f_0$ its reaction coefficient and source |
| $\sigma(\mathbf s)$ | strength of a singular (single-layer) source on $\Gamma$ |
| $(\xi,\zeta)$ | local normal and tangential coordinates at a point of $\Gamma$ |
| $\phi(\mathbf x,t)$ | level-set function; $\Gamma=\{\phi=0\}$; signed distance near $\Gamma$ |
| superscript $G$ | ghost value (ghost cell, ghost node, ghost fluid) |

## Clashes kept on purpose

$\kappa$ (volume fraction, unindexed or indexed by a cell) and $\kappa_0$ (the
reaction coefficient of the elliptic model problem, always subscripted).
$\beta$ (the elliptic coefficient, only on interface-method pages) and
$\beta_f$ (the feedback gain, always subscripted). $\sigma$ (singular source
strength) is not used for stress; the Cauchy stress is $\boldsymbol{\Sigma}$.
$\phi_v$ and $\phi_p$ (the reduced volume fraction and the porosity of compressible penalization, always subscripted) and the level set $\phi$. $r$ (the kernel argument of $\varphi$, only inside kernel formulas) and the
order of accuracy $r$; a page that needs both renames one locally and says so.
