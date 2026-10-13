---
type: Source
title: "Simon & Mandal (2019b) — Strategies to cure numerical shock instability in the HLLEM Riemann solver"
description: "Shows by scale and saw-tooth perturbation analysis that HLLEM's anti-diffusion on faces transverse to a strong shock cancels the HLL damping of density and normal velocity, and cures it two ways — widened HLL speeds on all faces near the shock (HLLEM-SWM) or sensor-scaled anti-diffusion on transverse faces (HLLEM-ADC) — while showing that shear-only control (HLLEMS) leaves density undamped; first- and second-order tests only."
resource: "doi:10.1002/fld.4710"
source_kind: paper
authors: [Simon S., Mandal J.C.]
year: 2019
venue: "Int. J. Numer. Methods Fluids 89:533-569"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2019-IJNMF-Simon-101002fld4710.pdf"
tags: [riemann-solver, shock-instability, hllem]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

Einfeldt's [HLLEM](/methods/hllem-riemann-solver.md) is HLLE plus
anti-diffusion on the contact and shear waves, and it is unstable at
strong grid-aligned shocks. A scale analysis of the faces transverse to a
perturbed normal shock shows the anti-diffusive parts of the mass and
normal-momentum fluxes to be of the same order as the HLL dissipation.
They cancel its damping. The paper adapts the authors' HLLC cure (HLLEM-SWM)
and proposes anti-diffusion control (HLLEM-ADC). It derives stability
bounds for both and shows that the shear-only control of Xie et al.
(2017) cannot damp density perturbations. All tests are first- or
second-order finite volume with limited Green–Gauss gradients; there is
no WENO. Merged into [numerical shock instability](/definitions/numerical-shock-instability.md),
[its cures](/methods/shock-instability-cures.md), the HLLEM page and the
benchmarks.

# Key claims

1. **HLLE and HLLEM in dissipation form** (§4, eqs. 8–17). Einfeldt speeds
   $S_L = \min(0, v_n^- - c^-, v_n - c)$ and
   $S_R = \max(0, v_n^+ + c^+, v_n + c)$, the last arguments at the Roe
   state (eq. 9). HLLEM subtracts $\frac{S_L S_R}{S_R - S_L}\delta_p$ times
   the contact and shear wave strengths along their Roe-averaged
   eigenvectors, with $\delta_p = c/(c + \vert v_n\vert)$ (Park & Kwon,
   eq. 15).
2. **HLL is stable because it dissipates the linear waves.** Complete
   solvers (Roe, HLLC, HLLEM) are unstable near strong grid-aligned
   shocks (§4).
3. **Mechanism** (§5, eqs. 18–40, Table 1, from the page images). On the
   transverse faces the contact strength is of the order of the
   perturbation, while $\delta_p$ is of order 1. The anti-diffusion is
   therefore "inadvertently activated" at the order of the HLL
   dissipation. In the saw-tooth analysis HLLEM has factors
   $(1, 1, 1 - 2\nu_y)$ for density, normal velocity and pressure, against
   $1 - 2\nu_y$ for all three under HLLE. In each update the anti-diffusion
   exactly cancels the HLL damping (eq. 40).
4. **HLLEM-SWM** (§6.1, eqs. 41–49). Only in the mass and normal-momentum
   fluxes, $S^{\mathrm w}_{L,R}$ replace $S_{L,R}$ throughout the HLL
   dissipation, denominators included (eq. 42). The anti-diffusion keeps
   the original speeds. The coefficient is 3.5, taken from the HLLC paper.
   * Unlike HLLC, transverse faces alone are "necessary but not
     sufficient": the cure must act on every face near the shock.
   * Sensors are taken over a five-face stencil. Variant E uses the
     entropy-fix size, with equal increments on both sides. Variant P uses
     $(1 - \omega_{\mathrm p})\vert S_{L,R}\vert$, with unequal increments
     and none at contacts or shear.
   * Bound: $\nu_y \le 1/(1 + \alpha_{\mathrm{SWM}}\epsilon_{\mathrm{SWM}}/\sqrt\gamma)$ (eq. 49).
5. **HLLEM-ADC** (§6.2, eqs. 50–52). On transverse faces only, the mass and
   normal-momentum fluxes take $\omega_{\mathrm p}$ times the
   anti-diffusion; $\omega_{\mathrm p} = 0$ is HLLE. The factors are
   $1 - 2\nu_y(1 - \omega_{\mathrm p})$ for density and normal velocity,
   and $1 - 2\nu_y$ for pressure. It is the cheapest cure.
6. **HLLEMS of Xie et al. (2017)**, shear-only control. Its perturbation
   factors, derived here for the first time, leave density at 1, fed by
   pressure. This contradicts Xie et al.'s claim that shear control
   suffices; HLLEMS fails on the blunt body and the inclined shock
   (§§6.2, 7.3, 7.6).
7. **Viscous cost** (§7.7). On the Blasius plate, variant P matches HLLEM.
   Variant E is close. ADC and HLLEMS are more dissipative, because the
   pressure sensor fires on transverse faces.

**Tests** (§7, coefficient 3.5, first order unless stated):
* Quirk's odd–even test on $800\times20$ with $10^{-6}$ perturbation;
* the double Mach reflection on $480\times120$, end time printed as
  $t = 0.02$;
* the Mach 20 blunt body on $320\times40$;
* shock diffraction on $400\times400$, second order;
* the forward-facing step on $120\times40$, second order;
* the inclined stationary shock on $50\times30$;
* a laminar flat plate at Mach 0.1.

# Notation map

| Simon & Mandal (2019b) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U$; $F$, $G$ | $u$; components of $\mathbf f$ | |
| $u, v$; $u_n, u_t$ | $v_x, v_y$; $v_n, v_t$ | the paper's $u$ is a velocity |
| $a$, $\tilde a$ | $c$, $c$ at the Roe state | |
| $D$; $A$ | $\mathbf d^{\mathrm{HLL}}$; anti-diffusion (words) | $\mathbf A$ is the vector potential |
| $\tilde R_2, \tilde R_3$; $\tilde\alpha_2, \tilde\alpha_3$ | $r^{(p)}$; $\ell^{(p)}(u^+ - u^-)$ | $\alpha$ collides with the LF speed |
| $\delta_2, \delta_3$ | $\delta_p$ | |
| $\bar S_L, \bar S_R$ | $S^{\mathrm w}_L$, $S^{\mathrm w}_R$ | |
| $\alpha$, $\epsilon^{L,R}$ | $\alpha_{\mathrm{SWM}}$, $\epsilon_{\mathrm{SWM}}$ | |
| $\omega$, $f_k$, $\beta = 5$ | $\omega_{\mathrm p}$ | collide with $\omega_k$, $\beta_k$ |
| $\lambda = \sqrt\gamma\,\Delta t/\Delta y$ | $\nu_y$ | |
| $\hat\rho, \hat u, \hat p$ | perturbation amplitudes (words) | the hat marks numerical quantities |

# Pages created or updated

* Created [HLLEM (HLLI) Riemann solver](/methods/hllem-riemann-solver.md), [Numerical shock instability](/definitions/numerical-shock-instability.md), [Cures for numerical shock instability](/methods/shock-instability-cures.md), [Quirk's odd–even decoupling test](/benchmarks/quirk-odd-even-test.md), [Hypersonic blunt-body carbuncle test](/benchmarks/hypersonic-blunt-body.md), [Stationary normal shock test](/benchmarks/stationary-normal-shock.md).
* Updated [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md), [Double Mach reflection](/benchmarks/double-mach-reflection.md), [Forward-facing step](/benchmarks/forward-facing-step.md), [Shock diffraction](/benchmarks/shock-diffraction.md).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2019-IJNMF-Simon-101002fld4710.pdf`.
   * **Version.** arXiv:1806.03187v1 (7 June 2018, "Submitted to Int.
     Journal of Num. Meth. Fluids"), the only arXiv version, 32 pages. It
     is not the typeset article.
   * **A wrong DOI on the arXiv record.** The record's DOI field points to
     the companion HLLC paper (10.1016/j.jcp.2018.11.022). The ADAM
     collection had filed this file under that DOI.
   * **Identity.** doi:10.1002/fld.4710, checked on Crossref: Int. J.
     Numer. Methods Fluids 89(12):533–569, issue of 2019.
   * **How it was read.** Text extraction, all sections. Eqs. 41–49 are
     missing from the text layer and were read from the page images, as
     was Table 1. The contour figures were read only from the text.
   * **Defects in the preprint.** §7 says "HLLC-SWM/ADC" where it means
     HLLEM. The Fig. 13 caption repeats that of the shock diffraction. The
     Quirk upstream velocity is printed as 1.0 for a "stationary fluid".
   * **Reference list:** 34 entries.
