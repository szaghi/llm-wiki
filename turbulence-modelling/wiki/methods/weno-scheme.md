---
type: Method
title: "WENO and hybrid shock-capturing schemes in scale-resolving simulation"
description: "WENO schemes capture shocks by nonlinear weighting of candidate stencils; in DNS and LES of compressible turbulence their dissipation is reduced by optimized weights and limiters, by linear weights in smooth flow, or by hybrids that apply WENO only where a shock sensor fires, and in implicit LES it serves as the subgrid dissipation."
status: established
aliases: [WENO, weighted essentially non-oscillatory scheme, WENO-Z, WENO-SYMBO, bandwidth-optimized WENO, limiter-optimized WENO, hybrid upwind/WENO scheme, hybrid central/WENO scheme]
tags: [numerical-dissipation, dns, compressible, implicit-les, gpu]
timestamp: 2026-10-26T05:06:00Z
---

# WENO and hybrid shock-capturing schemes in scale-resolving simulation

A **weighted essentially non-oscillatory (WENO)** scheme builds the
interface flux (or reconstructed interface state) of a finite-difference or
finite-volume method from several candidate stencils, combined with
solution-dependent nonlinear weights that favour the smooth stencils near a
discontinuity; with the weights frozen at their linear (optimal) values the
same construction is a linear upwind-biased scheme on the full stencil, the
"linear weights" option that [Cao et al. (2022)](/sources/cao-2022.md),
Remark 1, use for smooth low-speed flows. In this bundle WENO matters as
the shock-capturing core of compressible [DNS](/definitions/direct-numerical-simulation.md)
and LES of boundary layers and shock interactions, and as the source of the
dissipation of [implicit LES](/definitions/implicit-les.md). Its
dissipation, harmless at shocks, is the property every source works around
in turbulence (see [numerical dissipation](/properties/numerical-dissipation.md)).

## Variants in the sources

| Variant | Use | Source |
|---|---|---|
| Fifth- and seventh-order WENO (Jiang–Shu) | options of the OpenCFD-SCU library; fifth order near non-periodic boundaries and at the strongest shocks of the hybrid | Dang et al. (2022), §2.2.3, Table 2 |
| Seventh-order WENO-SYMBO (bandwidth-optimized WENO of Martín et al.), same stencil as an eighth-order central scheme | inviscid fluxes of the Mach 2.9 compression-ramp DNS | Dang et al. (2022), §5.1, §6.1 |
| Fourth-order WENO, linearly and nonlinearly (bandwidth) optimized, with absolute and relative limiters and near-wall filtering of the candidate weights | LES of hypersonic shock/boundary-layer interactions | Helm & Martín (2022), §II |
| Seventh-order WENO "optimized by means of limiters" (relative to Jiang–Shu) | DNS of hypersonic boundary layers | Huang et al. (2022), §2.2 |
| Fifth-order WENO with linear weights; WENO-Z with characteristic-variable reconstruction | reconstruction of the [gas-kinetic scheme](/methods/high-order-gas-kinetic-scheme.md): linear weights for the Taylor–Green vortex and channel, WENO-Z for supersonic isotropic turbulence | Cao et al. (2022), Remark 1, §3.4 |
| WENO switched on by the Ducros sensor over energy-preserving central schemes | [STREAmS](/software/streams.md) DNS of supersonic and hypersonic boundary layers | Cogo et al. (2022), §2 |
| Fifth-order WENO for the convective terms | STREAmS implicit LES of a Mars entry capsule wake | Placco et al. (2023), §2 |

The upwind schemes act on split fluxes or on characteristic variables.
[OpenCFD-SCU](/software/opencfd-scu.md) splits the flux with Steger–Warming
flux-vector splitting, $f=f^++f^-$ with eigenvalues split as
$\lambda^\pm=(\lambda\pm|\lambda|)/2$, and differences each part upwind;
optionally it projects onto characteristic variables, which raises
robustness and reduces spurious oscillations at higher cost (Dang et al.
2022, §2.2.1–2.2.2, Eqs. 19–40). Dang et al. (§2.2) state that upwind
differencing after flux-vector splitting is more stable than central or
spectral discretization of the convective term and suppresses aliasing
error. Cao et al. (2022, Remark 1) reconstruct characteristic variables at
each Gauss point for their supersonic cases.

## Dissipation in turbulence

- **Too dissipative as is.** Dang et al. (2022, §1) state that the
  dissipation of seventh-order WENO is still too high for good DNS data and
  that the seventh-order WENO used by Pirozzoli & Grasso "could have led to a
  reduction in computational accuracy" (a judgment, not shown). Helm &
  Martín (2022, §III C), recalling Wu & Martín, note that excess numerical
  dissipation suppresses the wall-pressure plateau of a separated
  compression-ramp interaction, which their limited WENO reproduces.
- **Remedies within WENO.** Bandwidth optimization and limiters lower the
  dissipation of the nonlinear weights (Helm & Martín 2022, §II; Huang et
  al. 2022, §2.2); linear weights avoid "the numerical dissipation from
  artificially created interface discontinuity" in smooth flow (Cao et al.
  2022, Remark 1).
- **Replacing WENO in smooth regions.** Huang et al. (2022, §2.2) use for
  their adiabatic Mach 2.5 case the eighth-order split-convective central
  scheme of Pirozzoli, which "runs about twice as fast as the conventional
  WENO method" and was shown robust up to edge Mach 4. The hybrids below do
  the same locally.
- **As an implicit subgrid model.** Placco et al. (2023, §2) omit a subgrid
  model and let "the numerical dissipation given by the numerical
  discretisation" act "as artificial viscosity at small scales", citing
  boundary-layer studies where this implicit LES gave results comparable to
  coarse DNS; the convective terms use fifth-order WENO, the viscous terms
  sixth-order central differences, and no switching to a central convective
  scheme is mentioned. Cao et al. (2022, §3.1) read
  the grid-independent agreement of their kinetic-energy dissipation as
  support for implicit LES with the gas-kinetic scheme.

## Hybrid schemes

**Sensor-switched upwind/WENO (OpenCFD-SCU).** Dang et al. (2022, §2.2.3,
Eqs. 41–43) blend three schemes by a modified Jameson pressure sensor,
evaluated in each direction and summed:
$$\phi_i=\frac{|-p_{i-1}+2p_i-p_{i+1}|}{p_{i-1}+2p_i+p_{i+1}},\qquad \theta_J=\phi_i+\phi_j+\phi_k$$
(page-local $\phi$, $\theta_J$, the source's $\theta$, renamed because
$\theta$ is the momentum thickness; $i,j,k$ the grid directions). With
thresholds $\theta_1=0.02$ and $\theta_2=0.1$ ("usually"),
$\theta_J\le\theta_1$ selects a linear seventh-order upwind flux,
$$f^*_{j+1/2}=\frac{-3f_{j-3}+25f_{j-2}-101f_{j-1}+319f_j+214f_{j+1}-38f_{j+2}+4f_{j+3}}{420},$$
$\theta_1<\theta_J\le\theta_2$ seventh-order WENO, and larger $\theta_J$
fifth-order WENO. The authors state that more than 90% of the points use the
upwind scheme, that switching artefacts are slight because all three schemes
are above fifth order, and that with characteristic reconstruction the
simulation "can be guaranteed not to diverge, provided the time step is
appropriate" (no proof or test given). The upwind coefficients sum to one
*(compiler check, not in the sources)*.

**Energy-preserving central/WENO (STREAmS).** Cogo et al. (2022, §2) apply
"consolidated, high-order, energy-preserving schemes" in shock-free regions,
"free of numerical dissipation", and WENO only where the Ducros sensor flags
shocks (see [kinetic-energy preservation](/properties/kinetic-energy-preservation.md)).
The same Ducros dilatation–vorticity factor weights the shock sensor of the
second-order unstructured [LD2C scheme](/methods/low-dissipation-low-dispersion-scheme.md)
(Carlsson et al. 2023), whose conclusion (§5) credits the vorticity-weighted
sensor with better resolved shear stress and grey-area mitigation in the
initial shear layer of a supersonic base flow, compared with the Jameson
sensor alone; in that comparison the dissipation coefficient and the face
extrapolation change too (Table 1).

Dang et al. (2022, §1) add that for Mach numbers "generally exceeding 6" a
dissipative scheme is usually introduced for robustness at strong shocks.

## Cost on GPUs

On the AMD MI60 GPU the inviscid upwind difference takes 70% of the
OpenCFD-SCU run time and the code is memory-bound, so the optimizations
target global-memory access: coalesced access, warp shuffle of neighbouring
fluxes with redundant computation at block edges, shared-memory transposes
that make the $y$- and $z$-direction WENO-SYMBO kernels as fast as the $x$
one (23.4% faster overall, 60% for the $z$ kernel on a $280^3$ grid), and
hoisting divisions out of the seventh-order WENO kernel (10%) (Dang et al.
2022, §4.3, Figs. 10, 14). The operation count of the WENO-SYMBO kernel is
estimated by hand, a lower bound because library functions take several
operations (§5.4).

## Qualifications

- Dang et al. (2022, §2.2.3) assign $\theta_J=\theta_2$ to both WENO branches
  ("$\theta_1<\theta\le\theta_2$" and "$\theta_2\le\theta$" in their
  symbols), and state that
  higher thresholds give higher dissipation, whereas by their own rule higher
  thresholds send more points to the low-dissipation upwind scheme
  *(compiler check, not in the sources)*.
- Dang et al. (2022) print 216 floating-point operations for the WENO-SYMBO
  kernel in Table 6 and 262 manually counted operations in §5.4. The version
  read is an author manuscript.
- The variants above are compared within each source only; no source of this
  bundle compares two WENO variants on the same turbulent flow.

# Citations

- [Dang et al. (2022)](/sources/dang-2022.md) — §1 (dissipation of WENO in DNS, strong shocks); §2.2.1–2.2.4, Eqs. (19)–(43), Table 2 (flux splitting, characteristic reconstruction, scheme library, hybrid); §4.3, Figs. 10, 14 (GPU kernels); §5.1, §5.4, Table 6; §6.1.
- [Helm & Martín (2022)](/sources/helm-2022.md) — §II (bandwidth-optimized WENO with limiters); §III C (plateau suppressed by excess dissipation).
- [Placco et al. (2023)](/sources/placco-2023.md) — §2 (fifth-order WENO in STREAmS, implicit LES).
- [Cao et al. (2022)](/sources/cao-2022.md) — Remark 1 (linear weights, WENO-Z, characteristic variables); §3.1, §3.4.
- [Cogo et al. (2022)](/sources/cogo-2022.md) — §2 (energy-preserving schemes with WENO switched by the Ducros sensor).
- [Huang et al. (2022)](/sources/huang-2022.md) — §2.2 (limiter-optimized seventh-order WENO; split-convective alternative).
- [Carlsson et al. (2023)](/sources/carlsson-2023.md) — §2.2.3, Eqs. (14)–(15) (Ducros-weighted sensor); Table 1; §5.
