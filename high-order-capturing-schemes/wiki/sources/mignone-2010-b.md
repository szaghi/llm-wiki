---
type: Source
title: "Mignone & Tzeferacos (2010) — A second-order unsplit Godunov scheme for cell-centered MHD: the CTU-GLM scheme"
description: "Second-order corner-transport-upwind Godunov scheme with mixed GLM cleaning and all variables cell-centred: an exact face solve of the (B_x, ψ) system, the dimensionless damping parameter α_p, a non-conservative EGLM variant, and a same-code comparison with CT and the eight-wave scheme."
resource: "doi:10.1016/j.jcp.2009.11.026"
source_kind: paper
authors: [Mignone A., Tzeferacos P.]
year: 2010
venue: "J. Comput. Phys. 229:2117-2138"
local_file: "~/papers/mosaic/high-order-capturing-schemes/2010-JCP-Mignone-101016jjcp200911026.pdf"
tags: [mhd, divergence-free, glm, second-order]
timestamp: 2026-10-09T00:00:00Z
---

# Summary

The second-order predecessor of the high-order FD-GLM scheme of
[Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md). It combines
Colella's corner-transport-upwind (CTU) integrator with Dedner's mixed
GLM cleaning, keeping every variable at cell centres, and compares it in
PLUTO with Powell's eight-wave scheme and Gardiner–Stone CTU-CT. Merged
into the [GLM](/methods/hyperbolic-divergence-cleaning.md) and
[CT](/methods/constrained-transport.md) pages and the MHD benchmarks.

# Key claims

1. **System** (§2, eqs. 1–3): the telegraph equation for
   $\psi_{\mathrm{GLM}}$; errors travel at $c_h$ independently of the flow,
   so they do not collect at stagnation points.
2. **CTU** (§3.1, eqs. 7–21): 6 Riemann solves per zone; Courant number
   below 1 in 2D and below 1/2 in 3D (defaults 0.8 and 0.4).
   Multidimensional source terms in the normal predictors are "of crucial
   importance". Damping is Strang-split around the advection (eq. 6).
3. **Cleaning speed** (eq. 15): the maximum of $|v_d| + c_{f,d}$, the
   largest speed compatible with the time step.
4. **Exact face solve** (§3.2, eqs. 23–25) of the $(B_x, \psi_{\mathrm{GLM}})$
   system, then a seven-wave Roe solver (Cargo–Gallice) with the face
   value of $B_x$.
5. **Dimensionless damping** (§3.3, eqs. 26–27):
   $\alpha_p = \Delta h\,c_h/c_p^2$, exponent $-\nu\alpha_p$. Dedner's
   $c_p^2/c_h = 0.18$ is "incomplete", having the dimension of a length.
   Optima lie in $[0, 1]$ and are problem-dependent.
6. **EGLM** (§§2, 3.4): non-conservative momentum and energy sources; more
   robust for strongly magnetized oblique shocks.
7. **Conclusions** (§5): GLM and EGLM show no wrong jumps or wave speeds,
   unlike the eight-wave scheme. CTU-GLM is competitive with staggered
   CT, "considerably easier" to implement, and extendable to AMR,
   unstructured grids and higher order.

**Tests** (§4).
* Circularly polarized Alfvén wave, 2D and 3D: second order for every
  scheme. At $N_x = 256$ the errors are GLM $8.48\times10^{-5}$, CT
  $6.73\times10^{-5}$, eight-wave $7.29\times10^{-5}$ ($\nu = 0.8$, 2D).
* Smooth nonlinear flow: all second order.
* 2D and 3D oblique shock tubes (Tables 2–3): the normal-field error is
  9.6 (eight-wave) against 0.4 (CT, GLM, EGLM) $\times10^{-2}$ in 2D, and
  3.6 against 0.5 $\times10^{-4}$ in 3D. Damping optima about 0.5 (2D) and
  0.005–0.01 (3D), independent of resolution.
* Field loops in 2D and 3D: CT and GLM keep the loop, the eight-wave
  scheme distorts it. The growth of $\langle|B_z|\rangle$ converges at order
  0.6–0.7.
* Rotor: GLM and CT give "extremely similar" contours.
* 3D blasts: indistinguishable at plasma beta $2\times10^{-2}$. At
  $2\times10^{-4}$ only EGLM runs; CT "failed even with a minmod limiter".

# Notation map

| Mignone & Tzeferacos (2010) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\psi$ | $\psi_{\mathrm{GLM}}$ | registry $\psi$ is the gauge scalar |
| $c_h$, $c_p$ | $c_h$, $c_p$ | |
| $\alpha = \Delta h\,c_h/c_p^2$ | $\alpha_p$ | the paper's $\alpha$ is also a rotation angle and a sound speed |
| $\Delta h$ | $\min_d h_d$ | |
| $C_a$ | $\nu$ | Courant number |
| $\Gamma$ | $\gamma$ | |
| $c_f, c_a, c_s$ | $c_f, c_A, c_s$ | |
| $\lambda^k$, $l^k$, $r^k$ | $\lambda^{(p)}$, $\ell^{(p)}$, $r^{(p)}$ | |
| $B_x^*$, $\psi^*$ | (inline) | face values of the exact $2\times2$ solve |
| $\mathcal R$, $\mathcal R_7$ | (words: Riemann-solver flux) | registry $\mathcal R$ is subcell reconstruction |
| $\beta$ (limiter, plasma beta) | (words) | registry $\beta_k$ is the smoothness indicator |

# Pages created or updated

* Updated [Hyperbolic (GLM) divergence cleaning](/methods/hyperbolic-divergence-cleaning.md): CTU-GLM, the origin of $\alpha_p$, EGLM, `## Contradictions`.
* Updated [Constrained transport](/methods/constrained-transport.md): the same-code comparison and CT's failure on the low-β blast.
* Updated [Grid-oblique MHD shock tubes](/benchmarks/oblique-mhd-shock-tubes.md), [Field-loop advection](/benchmarks/field-loop-advection.md), [MHD rotor](/benchmarks/mhd-rotor.md), [MHD blast wave](/benchmarks/mhd-blast-wave.md), [Circularly polarized Alfvén waves](/benchmarks/circularly-polarized-alfven-wave.md).
* Updated [PLUTO](/software/pluto.md).
* Also updated in the same run (list completed at the batch-8 deep lint): [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2010-JCP-Mignone-101016jjcp200911026.pdf` (arXiv:0911.3410v1, 17 Nov 2009, the submitted manuscript; doi:10.1016/j.jcp.2009.11.026 checked on Crossref: J. Comput. Phys. 229(6):2117–2138, March 2010): text extraction, all sections; the Alfvén-wave error formula read from the page image. Figures read from captions only; Appendix A eigenvectors not reproduced. Reference list: 29 entries (Crossref lists 28 for the published version).
