---
type: Method
title: "Hyperbolic (GLM) divergence cleaning"
description: "Dedner's generalized-Lagrange-multiplier treatment of ∇·B: an extra scalar couples to the induction equation so that divergence errors propagate away at a cleaning speed and are damped, keeping all variables cell-centred; used with high-order finite-difference WENO/MP5 schemes and with ADER on adaptive meshes."
status: established
aliases: [GLM, GLM-MHD, divergence cleaning, mixed hyperbolic–parabolic cleaning, Dedner cleaning]
tags: [mhd, divergence-free, finite-difference, amr]
timestamp: 2026-10-08T00:00:00Z
---

# Hyperbolic (GLM) divergence cleaning

**System** ([Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md),
§2, eqs. 4–9). The induction flux gains the gradient of a scalar
$\psi_{\mathrm{GLM}}$, and $\psi_{\mathrm{GLM}}$ obeys
$$\partial_t\psi_{\mathrm{GLM}} + c_h^2\,\nabla\cdot\mathbf B = -\frac{c_h^2}{c_p^2}\psi_{\mathrm{GLM}}.$$
Divergence errors therefore travel at the cleaning speed $c_h$ and decay
at rate $c_h^2/c_p^2$. Everything is conservative except the source of
$\psi_{\mathrm{GLM}}$, and no staggering or Poisson solve is needed.
* **Speeds.** The system has nine waves: the seven MHD waves and
  $\pm c_h$. The $\pm c_h$ modes carry jumps only in $B_x$ and
  $\psi_{\mathrm{GLM}}$ (eqs. 6–7). $c_h$ is the largest speed the time
  step allows, the domain maximum of $|v_d| + c_{f,d}$ over directions $d$
  (eq. 8).
* **Damping** is a separate exact step,
  $\psi_{\mathrm{GLM}} \leftarrow \psi_{\mathrm{GLM}}\exp\left(-\alpha_p\,c_h\,\Delta t/\min_d h_d\right)$
  with $\alpha_p = c_h\min_d h_d/c_p^2$ (eq. 9). Values $\alpha_p \in [0, 1]$
  minimize the divergence; 0.8 is used for shock tubes and 0.4 for vortices.

**In a finite-difference scheme** (§3.1, eqs. 21–24). The
$(B_x, \psi_{\mathrm{GLM}})$ pair decouples into a $2\times2$ linear system
with constant eigenvectors. Its two characteristic fields are
reconstructed grid-wide, with no local projection, and give the
interface $B_x$. That value then enters the usual $7\times7$ MHD
eigensystem as a parameter. This makes 16 reconstructions per interface
([characteristic decomposition](/methods/characteristic-decomposition.md);
[conservative finite difference](/methods/conservative-finite-difference.md)).
* Divergence errors stay at $10^{-2}$ or below with shocks, bounded under
  refinement, and saturate for $\alpha_p \gtrsim 0.4$. On smooth 3D
  problems they fall below $10^{-8}$ at $128^3$ (§§4.2–4.3).
* For field-loop advection the best $\alpha_p$ depends on the order:
  above about 0.4 at fifth order, below about 0.2 at third
  ([field-loop advection](/benchmarks/field-loop-advection.md)).

**On adaptive meshes.** Third-order ADER-WENO and ADER-DG with subcell
limiting use GLM on cell-by-cell AMR instead of a staggered field. The
[MHD rotor](/benchmarks/mhd-rotor.md) then shows none of the spurious
density and magnetic-pressure oscillations reported for Godunov schemes
without divergence treatment
([Dumbser et al. (2013)](/sources/dumbser-2013.md), §4;
[Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.2;
[high-order AMR](/methods/high-order-amr.md)).

**Against the alternatives.** GLM is not exactly divergence-free, unlike
[constrained transport](/methods/constrained-transport.md), but it keeps
every variable at cell centres. The authors cite comparable accuracy to
CT from earlier work, without showing it here
([Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md), §1). For
curl involutions, GLM-type curl cleaning needs fast cleaning speeds and
many extra fields ([Balsara et al. (2023)](/sources/balsara-2023.md), §5;
[curl-preserving reconstruction](/methods/curl-preserving-reconstruction.md)).

# Citations

1. [Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md), §§1–4 (arXiv v2).
2. [Dumbser et al. (2013)](/sources/dumbser-2013.md), §4.
3. [Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.2.
4. [Balsara et al. (2023)](/sources/balsara-2023.md), §5.
