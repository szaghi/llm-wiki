---
type: Definition
title: "Notation registry"
description: "Normative symbol registry — every concept page writes mathematics in this notation, never in paper-native symbols."
status: established
tags: [notation, meta]
timestamp: 2026-10-13T00:00:00Z
---

# Notation registry

This page is **normative** for the bundle. Concept pages must use these symbols
exclusively; each Source page maps its paper's native notation to this registry
in a `# Notation map` section. Extend this registry (and record the extension in
[the log](/log.md)) before writing math that needs a symbol it lacks.

## Grids and refinement

| Symbol | Meaning |
|---|---|
| $h$, $H$ | fine- and coarse-level grid spacing ($H = 2h$ at a 2:1 interface) |
| $\Omega_h$ | discrete grid (a level of a hierarchy) |
| $l$, $r$ | level index of an AMR hierarchy (0 = coarsest) and refinement ratio between consecutive levels (added 2026-10-12; $r$ as a polynomial degree appears only as the FEEC subscript $\mathcal P_r$) |
| $\phi_{\mathrm g}$ | gravitational potential, $\mathbf g = -\nabla\phi_{\mathrm g}$ (distinct from the projection potential; added 2026-10-12) |
| $m(E)$ | space-filling-curve index of a cell, block or element $E$ (added 2026-10-12) |
| $\mathbf{x}_{ijk}$ | node/cell-center location, context per collocation |
| $\Delta t$; superscripts $n$, $n+1/2$, $n+1$ | time step and time level of a discrete field ($B_h^n$, $E_h^{n+1/2}$); registered 2026-10-13, already in use on several pages |

## Discrete spaces and the complex

Degrees of freedom live in discrete spaces indexed by form degree, joined by
operators into the discrete complex (spaces joined by operators — never
operators and a field in one chain):

$$V_h^0 \xrightarrow{G_h} V_h^1 \xrightarrow{C_h} V_h^2 \xrightarrow{D_h} V_h^3$$

| Symbol | Meaning |
|---|---|
| $V_h^0$ | scalar potentials (node/vertex DOFs) |
| $V_h^1$ | circulations (edge DOFs) |
| $V_h^2$ | fluxes (face DOFs) |
| $V_h^3$ | densities (cell DOFs) |
| $G_h$ | discrete gradient, $G_h : V_h^0 \to V_h^1$ |
| $C_h$ | discrete curl, $C_h : V_h^1 \to V_h^2$ |
| $D_h$ | discrete divergence, $D_h : V_h^2 \to V_h^3$ |

Exactness identities, when a scheme provides them:
$D_h C_h = 0$ and $C_h G_h = 0$.

When one page must distinguish concrete divergence stencils, mark the
instantiation with a superscript (added 2026-07-08, Tóth-2000 ingestion):

| Symbol | Stencil |
|---|---|
| $D_h^{\mathrm{f}}$ | face-flux difference over a cell (staggered/Gauss sense) |
| $D_h^{\mathrm{c}}$ | cell-centered central difference on collocated DOFs |
| $D_h^{\mathrm{k}}$ | corner-centered (nodal) difference on collocated DOFs |

Unmarked $D_h$ means "the scheme's own discrete divergence" when the stencil
is irrelevant to the claim.

The collocated counterpart of the curl (added 2026-10-08, zaghi-2026
ingestion): $C_h^{\mathrm{c}}$ is the cell-centered central-difference curl
on collocated DOFs. When $C_h^{\mathrm{c}}$ and $D_h^{\mathrm{c}}$ are built
from one shared antisymmetric 1D derivative primitive, the derivatives
commute on a uniform tensor-product grid and $D_h^{\mathrm{c}} C_h^{\mathrm{c}} = 0$
holds identically. This is the collocated analog of $D_h C_h = 0$.

## FEEC element families

(Added 2026-07-08, deep lint #3.) The two finite-element differential-form
families: $\mathcal{P}_r\Lambda^k$ (full polynomial degree $r$) and
$\mathcal{P}_r^-\Lambda^k$ (Koszul-trimmed); $\mathcal{P}_1^-\Lambda^k$
are the Whitney forms.

## Interface interpolation (SBP)

(Added 2026-07-08, Mattsson–Carpenter-2010 ingestion.) Trace-space
counterparts of $P$/$R$ acting on interface data between nonconforming
blocks:

| Symbol | Meaning |
|---|---|
| $I_{C2F}$ | coarse-to-fine interface interpolation |
| $I_{F2C}$ | fine-to-coarse interface interpolation |

SBP-preserving pair: $\mathsf{H}_F\, I_{C2F} = I_{F2C}^T\, \mathsf{H}_C$
(adjoints in the interface norms).

## Base-scheme (Godunov) quantities

(Added 2026-07-08, deep lint #1.) Starred symbols denote values produced by
the shock-capturing base scheme: $f^{x,*}, f^{y,*}$ are its upwind numerical
fluxes for the magnetic-field components, $B_h^{*}$ (and $u_h^{*}$) a
provisional field before a correction/projection step.

## Reconstruction (WENO, PPM)

(Added 2026-10-13, frontier batch 3a, with the WENO and PPM pages.) $w$ is a generic
scalar being reconstructed: one conserved or characteristic component.

| Symbol | Meaning |
|---|---|
| $\bar w_j$; $w_j$ | cell average of $w$ over cell $j$ (finite volume); point value at $x_j$ (finite difference) |
| $w^-_{j+1/2}$, $w^+_{j+1/2}$ | reconstructed values at face $j+1/2$ from the cell on its left and on its right |
| $k_{\mathrm s}$ | number of points of an ENO/WENO candidate stencil (Jiang–Shu's $r$; distinct from the refinement ratio $r$) |
| $\mathrm{IS}_k$ | WENO smoothness indicator of candidate stencil $k$ |
| $d_k$, $\omega_k$ | linear (optimal) and nonlinear WENO weights of stencil $k$; $\sum_k d_k = \sum_k \omega_k = 1$ |
| $\epsilon_{\mathrm W}$, $p_{\mathrm W}$ | additive constant and power in the nonlinear weights |

## SBP operators

(Added 2026-07-08, Strand-1994 ingestion.) Literature convention writes the
SBP norm matrix as $H$, which collides with our coarse grid spacing — the
registry uses sans-serif for SBP matrices:

| Symbol | Meaning |
|---|---|
| $\mathsf{H}$ | SBP norm/quadrature matrix, SPD, defining $(u,v)_h = u^T \mathsf{H} v$ |
| $\mathsf{Q}$ | almost-skew-symmetric part: $\mathsf{Q} + \mathsf{Q}^T = \mathsf{B}$ (boundary terms) |
| $\mathsf{D}_1 = \mathsf{H}^{-1}\mathsf{Q}$ | SBP first-derivative operator |
| $\mathsf{D}_2 = \mathsf{H}^{-1}(A + \mathsf{B}S)$ | SBP second-derivative operator, $A + A^T \le 0$ (added at deep lint #2) |
| $\mathsf{D}_1^* = \mathsf{H}^{-1}\mathsf{D}_1^{T}\mathsf{H}$ | $\mathsf{H}$-adjoint of $\mathsf{D}_1$; for a nullspace-consistent $\mathsf{D}_1$ ($\ker\mathsf{D}_1 = \mathrm{span}\{1\}$) its kernel is one-dimensional, spanned by the **grid-oscillation mode** (added 2026-10-08, ranocha-2020) |

## Fields

| Symbol | Meaning |
|---|---|
| $B_h$ | discrete magnetic field (collocation stated per method) |
| $u_h$ | discrete velocity field |
| $E_h$ | discrete electric field / electromotive force (edge-collocated in CT schemes) |
| $A_h$ | discrete magnetic vector potential, edge-collocated ($B_h = C_h A_h$); added at deep lint #4 |
| $\phi_h$, $\psi_h$ | discrete scalar potentials (projection, cleaning) |

The central algebraic invariant of the domain is written $D_h B_h = 0$.

## AMR transfer operators

| Symbol | Meaning |
|---|---|
| $P$ | prolongation (coarse $\to$ fine), $P : V_H \to V_h$ |
| $R$ | restriction (fine $\to$ coarse), $R : V_h \to V_H$ |
| $P_D$ | divergence-space prolongation — constructed so prolongation commutes with discrete divergence |
| $\Gamma$ | ghost-fill operator at refinement interfaces (never $G$ — that is the gradient) |

Commutation conventions (fixed operand order):

- restriction: $D_H R = R\, D_h$
- prolongation: $D_h P = P_D\, D_H$

Round-trip compatibility (added 2026-10-08, zaghi-2026 ingestion):
$R P = I$ means that restricting a prolonged field returns the coarse data
exactly.

## Cleaning and verification quantities

(Added 2026-10-08, zaghi-2026 ingestion. $c_h$ and $c_p$ were already in use
on the GLM page; they are registered here.)

| Symbol | Meaning |
|---|---|
| $c_h$ | GLM cleaning (hyperbolic transport) speed |
| $c_p$ | GLM parabolic damping parameter; the damping rate of $\psi_h$ is $c_h^2/c_p^2$ |
| $\mathcal{D}$ | the linear operator coupling $\psi_h$ to the divergence in the GLM system, $\mathcal{D}(\psi) + \nabla\cdot B = 0$; its choice selects the cleaning family (added at deep lint #8, already in use) |
| $q$ | accuracy order of a ghost-fill operator $\Gamma$ (value error $O(h^q)$) |
| $p_{\mathrm{obs}}$ | observed convergence order from a refinement ladder, $p_{\mathrm{obs}} = \log_2(e_h / e_{h/2})$ |

## Edge-EMF constructions

(Added at deep lint #8. These symbols had been in use on the CT pages since
the gardiner-stone-2005 ingestion without being registered.)

| Symbol | Meaning |
|---|---|
| $\mathcal{E}^{\circ}$ | edge EMF as the plain arithmetic average of the four face values (Gardiner & Stone) |
| $\mathcal{E}^{\alpha}$ | edge EMF with Lax–Friedrichs-type dissipation added to the average |
| $\mathcal{E}^{c}$ | edge EMF upwinded by the sign of the contact (mass-flux) mode, the Athena choice; "CT-Contact" elsewhere |

All three are values of $E_h \in V_h^1$; the superscript names the
construction, not a different field.

## Admissibility (positivity)

(Added 2026-10-08, wu-2018 ingestion.)

| Symbol | Meaning |
|---|---|
| $\mathcal{G}$ | admissible state set: conserved states with positive density and positive internal energy (hence pressure) |
| $\alpha^{\mathrm{LF}}$ | Lax–Friedrichs numerical-viscosity parameter of a flux, per direction |

## MHD state and wave quantities

(Added 2026-10-13, deep lint #10. These symbols were already in use on
concept pages without being registered.)

| Symbol | Meaning |
|---|---|
| $B_n$ | normal magnetic-field component at a face, or the (constant) normal component in a 1D problem |
| $\beta$ | plasma beta, ratio of thermal to magnetic pressure (never an angle) |
| $\gamma$ | adiabatic index (ratio of specific heats; never an angle) |
| $\lambda_k$ | characteristic speed (eigenvalue of the flux Jacobian) of the $k$-th wave |
| $\bar B_h$ | cell averages of the magnetic field held as cell-centred DOFs, the field the conservative finite-volume update evolves (bar = cell average, as $\bar w_j$ above) |
| $S(U)$ | eight-wave (Powell) source vector, multiplied by $-\nabla\cdot B$ in the symmetrizable form; $U$ is the conserved state vector |

## Writing rules

- Inline math `$...$`, display math `$$...$$` (KaTeX). Never `\(...\)` / `\[...\]`.
- Multi-line derivations: `$$\begin{aligned} ... \end{aligned}$$`.
- Operators are upright capitals as above; grid-level subscripts $h$/$H$ mark
  fine/coarse; no paper-native symbols outside `# Notation map` sections.
