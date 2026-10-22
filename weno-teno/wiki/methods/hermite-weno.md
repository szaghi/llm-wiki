---
type: Method
title: "Hermite WENO"
description: "Hermite WENO (HWENO) builds WENO candidates from both cell averages and derivative information, which on element methods means extending each neighbour's polynomial into the cell and correcting its mean; Kuzmin & Vedral use such a reconstruction only to measure smoothness and drive the stabilization of continuous finite elements, never to overwrite the solution."
status: established
aliases: [HWENO, Hermite WENO reconstruction, Zhong–Shu HWENO, HTENO, Hermite TENO]
tags: [weno, reconstruction, dg, compact-scheme]
timestamp: 2026-10-21T12:00:00Z
---

# Hermite WENO

Hermite WENO (HWENO) schemes, "based on the Hermite polynomials", were developed for nonlinear
conservation laws and Hamilton–Jacobi equations (Fu 2023, §1, which recalls them next to the compact
WCNS and CRWENO families). In the form used in the bundle, a candidate takes its derivatives from a
neighbouring cell's polynomial and its mean from the cell itself, so only face neighbours are needed.
The bundle's substantive use is in element methods, where every cell already carries a polynomial.

## HWENO candidates on a finite element mesh

Kuzmin & Vedral (2023, §5, Eq. (11)) outline, "without claiming originality", the Zhong–Shu-type
construction they use. For a cell $K_e$ with finite element polynomial $u_h^e\in\mathbb P^N$ and its
von Neumann neighbours $e'$ (sharing a point, edge or face; at least $d+1$ of them in $d$ dimensions):

- each neighbour polynomial is extended into $K_e$ and its mean corrected,
  $$u^e_{h,l}(x)=u_h^{e'}(x)+\pi_e\big(u_h^e-u_h^{e'}\big),\qquad \pi_ev=\frac1{|K_e|}\int_{K_e}v\,dx,$$
  so that the candidate has the cell's mean and the neighbour's derivatives; the cell's own
  polynomial is the candidate $l=0$ (page-local index $l$, mean operator $\pi_e$);
- the candidates are blended with linear weights that favour the central candidate,
  $\tilde\omega_0=1-m_e\cdot10^{-3}$, $\tilde\omega_l=10^{-3}$ ($m_e$ non-central candidates;
  $\tilde\omega_l=0.2$ for all five candidates in the KPP test), and Jiang–Shu-type nonlinear weights
  $\omega_l\propto\tilde\omega_l/(\epsilon+\beta_l)^2$, $\epsilon=10^{-6}$, with
  $\beta_l=\|u^e_{h,l}\|_e^q$ a power of the scaled Sobolev seminorm of the candidate (page-local
  exponent $q\ge1$, $q=1$ by default; not the registry's weight exponent)
  ([smoothness indicators](/definitions/smoothness-indicator.md),
  [WENO-JS](/methods/weno-js-reconstruction.md)).

Because the seminorm contains only derivatives, the mean correction does not affect the indicator and
is unnecessary in practice (Remark 3). A smaller central linear weight makes shock detection more
reliable and the stabilization stronger (§5, used in the KPP test). Remark 4 proposes, without
implementing them, additional Hermite candidates from vertex neighbours and Lagrange candidates
interpolated on the convex hull of neighbouring barycentres, generalizing a DG-$\mathbb P^1$
construction of Luo et al. to arbitrary order.

## Use as a sensor, not a limiter

Classical RKDG schemes with WENO or HWENO limiters **overwrite** the solution in troubled cells by the
reconstruction. Kuzmin & Vedral (2023, Remark 2) do not: the reconstruction $u_h^{e,*}$ serves only to
compute a cellwise blending factor

$$\gamma_e=1-\min\Big(1,\frac{\|u_h^e-u_h^{e,*}\|_e}{\|u_h^e\|_e}\Big)^q$$

(page-local; Eq. (9)), which blends a high-order symmetric projection stabilization with low-order
artificial viscosity, so the semi-discrete scheme keeps the structure of a continuous Galerkin method
([WENO-stabilized continuous Galerkin](/methods/weno-stabilized-continuous-galerkin.md),
[artificial viscosity](/methods/artificial-viscosity.md),
[troubled-cell indicators](/definitions/troubled-cell-indicator.md)). They argue that overwriting
DG-WENO schemes "have more in common with finite volume methods". If the finite element solution on
the stencil union is a polynomial of degree $\le N$, every candidate equals it, $\gamma_e=1$ for any
nonlinear weights, and polynomial solutions are reproduced exactly (Remark 6).

## Hermite TENO

Fu (2023, §3.10) lists HTENO (Wibisono et al.), a Hermite-polynomial compact variant of
[TENO](/methods/targeted-eno.md); Ye et al. (2022, §1) cite it among the TENO extensions. No formulas
are given in the ingested sources.

## Qualifications

- Li et al. (2022, Eq. (8)) call the rescaled Legendre basis used by Balsara et al. for smoothness
  indicators "Hermite polynomials"; that reconstruction is not Hermite WENO.
- The nonlinear HWENO reconstruction of Kuzmin & Vedral is printed once with a tilde
  ($\tilde u_h^{e,*}$) and referred to without it elsewhere; they are the same object.

# Citations

- [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) — §3, Eq. (8); Eq. (9); §5, Eq. (11), Remarks 2–4, 6; §7.4.
- [Fu (2023)](/sources/fu-2023.md) — §1; §3.10.
- [Ye et al. (2022)](/sources/ye-2022.md) — §1.
- [Li et al. (2022)](/sources/li-2022-b.md) — §2, Eq. (8).
