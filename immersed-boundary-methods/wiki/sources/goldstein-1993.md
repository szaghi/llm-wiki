---
type: Source
title: "Goldstein, Handler & Sirovich (1993) — Modeling a no-slip flow boundary with an external force field"
description: "Introduces feedback forcing: a proportional–integral body force at prescribed boundary points brings the flow to rest on a virtual surface; implemented in a pseudo-spectral code with Gaussian spreading, spectral smoothing and a back force against spatial oscillations, and tested on a start-up cylinder, turbulent channel flow with a virtual wall and riblets."
resource: "doi:10.1006/jcph.1993.1081"
source_kind: paper
authors: [Goldstein D., Handler R., Sirovich L.]
year: 1993
venue: "J. Comput. Phys. 105(2):354-366"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/1993_Crossref_Journal_of_Computational_Physics_Goldstein_Modeling_a_No-Slip_Flow_Boundary_with_an_External_Force_Fiel.pdf"
tags: [immersed-boundary, feedback-forcing, spectral, turbulence, stiffness]
timestamp: 2026-11-08T17:40:00Z
---

# Summary

Goldstein, Handler and Sirovich model a no-slip surface by an external force
field chosen during the computation so that the fluid comes to rest on the
surface: [feedback forcing](/methods/feedback-forcing.md),
$\mathbf f=\alpha_f\int(\mathbf u-\mathbf u_\Gamma)\,dt'+\beta_f(\mathbf u-\mathbf u_\Gamma)$ with negative
gains, a two-mode controller whose oscillator analogy fixes the gains and
whose explicit treatment limits the time step. Unlike the elastic
[classical method](/methods/classical-immersed-boundary-method.md), the
boundary point locations are prescribed and each point's force is computed
independently. In a Fourier–Chebyshev pseudo-spectral code the point forces
cause global spatial oscillations, controlled by spreading the force with a
narrow Gaussian ([regularized delta function](/operators/regularized-delta-function.md);
[sharp and diffuse interfaces](/definitions/sharp-and-diffuse-interface.md)),
spectral smoothing and a "back force" inside the body.

# Version read

Version of record, J. Comput. Phys. 105, 354–366 (1993), 13 pages, all read.
The PDF is an image-only scan; it was read through OCR (tesseract, 300 dpi).
Prose and tables are legible; several display equations, including the
discrete time integral of the force, are not, and no equation is quoted here
beyond what the prose states. The OCR text carries no section numbers, so
claims are located by part of the paper. Page-1 title and authors match
Crossref; the page carries no DOI.

# Key claims

1. A flow about a body can be computed on a regular grid in a simple domain, the body imposed by a force field; the fluid "simply sees a body through the forces of pressure and shear" (introduction). **Stated**
2. Specifying point locations rather than inter-point forces makes the force computation simpler than in the elastic immersed boundary models, since each point's force is computed independently (introduction, citing Peskin 1972 and Fauci). **Stated**
3. The feedback law with integral and proportional terms is sufficient; the integral term alone brings the flow to rest, the proportional term acts like the Stokes drag of an unresolved obstacle; derivative or $|\mathbf u|\mathbf u$ terms are conceivable (formulation). **Stated**
4. Neglecting the other terms gives a damped oscillator of natural frequency $(2\pi)^{-1}\sqrt{|\alpha_f|/\rho}$ and damping ratio $-\beta_f/(2\sqrt{|\alpha_f|\rho})$; $\alpha_f$ must make it faster than the energetic flow frequencies (formulation). **Derived**
5. With second-order Adams–Bashforth the stability limit is $\Delta t<(-\beta_f-\sqrt{\beta_f^2-2\alpha_f k})/\alpha_f$, $k$ problem dependent of order one; the solution is stable for moderate gains and insensitive to their exact values (formulation). **Derived**
6. Point forces in a spectral representation produce global spatial oscillations that do not grow in time but persist at the highest practical resolution; spreading with a narrow Gaussian (exact shape "not crucial"), mild spectral smoothing and a back force inside the body remove them (spectral implementation). **Shown**
7. The impulsively started cylinder at $Re\approx550$ (576 surface points, symmetric half domain) forms within $O(10^2)$ time steps and its wake development compares with experiments (examples). **Shown**
8. In turbulent channel flow at $Re_\tau=125$ ($48\times65\times64$) a virtual plate reproduces the mean, rms and Reynolds-stress profiles of a no-slip wall; with $\alpha_f=-200$, $\beta_f=-1.5$ the time step was limited only by the Courant condition (examples). **Shown**
9. Riblets (21 triangular ribs, spacing 18 and height 5 viscous units, $48\times64\times128$) are modelled with a trial-and-error back-force profile (examples). **Shown**

# Notation map

| Goldstein et al. (1993) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf U$ | $\mathbf u$ | velocity |
| $\mathbf x_s$ | $\mathbf X_\ell$ | boundary point |
| $\mathbf f(\mathbf x_s,t)$ | $\mathbf f(\mathbf X_\ell,t)$ | force at a boundary point |
| $\alpha$, $\beta$ | $\alpha_f$, $\beta_f$ | gains (negative) |
| $\mathbf v$ (imposed boundary velocity) | $\mathbf u_\Gamma$ | |
| $\boldsymbol\Omega$ | $\boldsymbol\omega$ | vorticity |
| $S=0$ | $\Gamma$ | |

# Reference list

36 printed references, of which no. 2 is "Deleted in proof"; the other 35
are merged complete into the [bibliography](/bibliography.md) from the OCR
text (Crossref deposits no reference list for this paper). Most journal
references print no title and carry the placeholder title. Refs. 8, 26 and 32
are printed as in press; ref. 1's first author reads "Bae-Lev" in the OCR and
is entered as Bar-Lev.

# Pages created or updated

Chunk 1 (2026-11-08), list updated in chunk 2 (2026-11-08). This source is cited on:

- [Flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
- [Immersed boundary method](/definitions/immersed-boundary-method.md)
- [Sharp and diffuse interface representations](/definitions/sharp-and-diffuse-interface.md)
- [Classical (Peskin) immersed boundary method](/methods/classical-immersed-boundary-method.md)
- [Feedback forcing](/methods/feedback-forcing.md)
- [Volume penalization (Brinkman penalization)](/methods/volume-penalization.md)
- [Regularized delta function $\delta_h$](/operators/regularized-delta-function.md)
