---
type: Result
title: "Green's identities"
description: "Green's first and second theorems, ∮_S φ∇ψ·dS = ∫_V (φ∇²ψ + ∇φ·∇ψ) dV and ∮_S (φ∇ψ − ψ∇φ)·dS = ∫_V (φ∇²ψ − ψ∇²φ) dV, obtained from the divergence theorem applied to φ∇ψ."
status: established
aliases: [Green's first theorem, Green's second theorem, Green's first identity, Green's second identity]
tags: [integral-theorems, vector-calculus]
timestamp: 2026-10-13T00:00:00Z
---

# Green's identities

For scalar functions $\phi,\psi$ continuous and differentiable in a volume
$V$ bounded by $S$, the [divergence theorem](/results/divergence-theorem.md)
applied to $\phi\nabla\psi$ gives **Green's first theorem**, and subtracting
the same with $\phi,\psi$ exchanged gives **Green's second theorem**
([Riley et al. (2006)](/sources/riley-2006.md), §11.8.1, eqs. (11.19)–(11.20),
pp. 402–403):

$$\oint_S\phi\nabla\psi\cdot d\mathbf S=\int_V\left[\phi\nabla^2\psi+\nabla\phi\cdot\nabla\psi\right]dV,$$

$$\oint_S(\phi\nabla\psi-\psi\nabla\phi)\cdot d\mathbf S=\int_V(\phi\nabla^2\psi-\psi\nabla^2\phi)\,dV.$$

The book notes the second's use for Green's functions (Ch. 21, outside this
bundle's reading). Exercise 11.20 (p. 412) applies it with $\psi=1/r$ to
express a harmonic function inside $S$ through its boundary values and
normal derivative,
$\phi_P=-\frac{1}{4\pi}\oint_S\phi\,\frac{\partial}{\partial n}\!\left(\frac1r\right)dS+\frac{1}{4\pi}\oint_S\frac1r\frac{\partial\phi}{\partial n}\,dS$.

The [Laplacian](/definitions/laplacian.md) in the integrands may be written in
any coordinates; the identities themselves are coordinate-free.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §11.8.1, pp. 402–403; exercise 11.20, p. 412.
