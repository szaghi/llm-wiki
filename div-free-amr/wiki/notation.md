---
type: Definition
title: "Notation registry"
description: "Normative symbol registry — every concept page writes mathematics in this notation, never in paper-native symbols."
status: established
tags: [notation, meta]
timestamp: 2026-07-08T00:00:00Z
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
| $\mathbf{x}_{ijk}$ | node/cell-center location, context per collocation |

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

## Fields

| Symbol | Meaning |
|---|---|
| $B_h$ | discrete magnetic field (collocation stated per method) |
| $u_h$ | discrete velocity field |
| $E_h$ | discrete electric field / electromotive force (edge-collocated in CT schemes) |
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

## Writing rules

- Inline math `$...$`, display math `$$...$$` (KaTeX). Never `\(...\)` / `\[...\]`.
- Multi-line derivations: `$$\begin{aligned} ... \end{aligned}$$`.
- Operators are upright capitals as above; grid-level subscripts $h$/$H$ mark
  fine/coarse; no paper-native symbols outside `# Notation map` sections.
