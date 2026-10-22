---
type: Software
title: "FLUXO"
description: "FLUXO is an open-source Fortran code for split-form and entropy-stable DGSEM on 3D curved unstructured hexahedral meshes, with compile-time selection of flux and degree; the sources benchmark it against Trixi.jl and use it for subcell-limiting tests on Euler, ideal and resistive GLM-MHD with non-conservative terms, up to a 20.7 M-DOF Io–plasma-torus run."
status: established
aliases: [FLUXO code]
tags: [software, dg, entropy-stable, mhd, limiting]
timestamp: 2026-10-22T00:00:00Z
---

# FLUXO

FLUXO is a Fortran code for the [DGSEM](/methods/dgsem.md) on 3D curved,
unstructured hexahedral meshes. It implements the split-form
([flux-differencing](/methods/flux-differencing.md)), entropy-stable and
kinetic-energy-preserving variants
([Ranocha et al. (2023)](/sources/ranocha-2023.md), §1, §4). It is the
Fortran counterpart of [Trixi.jl](/software/trixi-jl.md) in Ranocha et al.'s
performance study.

## Design as reported

- **Compile-time options.** Selecting the volume flux at compile time lets
  the compiler inline it, which gives about 5 %. Also fixing the degree $N$
  at compile time gives up to 15 % (Ranocha et al. (2023), §7.3, Fig. 7).
- **Precomputation.** Primitive variables $(\rho,v,p)$, $1/\rho$ and
  $\lvert v\rvert^2$ are precomputed at all nodes, which speeds up the volume
  terms by about 5–25 %. The memory overhead is at most about one half on
  Cartesian 3D meshes and one quarter on curved meshes, which already store
  nine metric terms per node (§7.1, Fig. 5).
- **Gauss collocation.** The entropy-stable Legendre–Gauss variant is
  implemented in the "correction" form (6.3). That form keeps the LGL-type
  flux-differencing volume term and adds a hybridized boundary correction
  (§6).
- **Build.** The study builds FLUXO with Intel Fortran 19.1.3, using
  `-O3 -xHost -shared-intel -inline-max-size=1500 -no-inline-max-total-size -no-prec-div`.
  Restricting it to AVX2 lowers its performance by up to 19 % (§4, §4.1).
- **Time integration.** The benchmarks use 90 steps of a 5-stage,
  fourth-order, 2N-storage Runge–Kutta method with CFL-based step control.
  This gives the same number of right-hand-side evaluations as the Trixi.jl
  runs (§4.1).

Serial performance per degree of freedom is similar to Trixi.jl's
(Ranocha et al. (2023), §4.1, Fig. 1).

## Use in the sources

[Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) run
all their tests except KPP with FLUXO, combining the DGSEM with
[subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md)
and [convex limiting](/methods/convex-limiting.md) (§5). All four tests use
SSP-RK3 at CFL 0.5.

1. **Kelvin–Helmholtz instability**
   ([benchmark](/benchmarks/kelvin-helmholtz-instability.md)).
   - Setup: $N=7$, $64^2$ elements, $t=10$, split form with the
     Chandrashekar flux.
   - Comparison: element-wise against subcell-wise positivity limiting.
   - Result: subcell-wise limiting adds about three orders of magnitude
     less low-order method.
2. **Mach 4 bow shock** on third-order curved elements.
   - Setup: $N=5$, invariant-domain bounds from bar states.
   - Result: the mean blending coefficient is $\bar\alpha=11.03\%$ on 864
     elements and $9.50\%$ on 1536 elements.
3. **Mach $\approx2000$ astrophysical jet**
   ([benchmark](/benchmarks/high-mach-astrophysical-jet.md)).
   - Setup: $N=3$, $256^2$ elements.
   - Low-order variants: first-order finite volumes with LLF, first-order
     with HLLE, and second-order with HLLE.
4. **GLM-MHD Orszag–Tang vortex**
   ([benchmark](/benchmarks/orszag-tang-vortex.md)).
   - Setup: $N=3$, $256^2$ elements, Chandrashekar–Klingenberg volume flux.
   - Limiting: subcell-wise, with density bounds.
   - Note: the conservative GLM form is used even though the
     non-conservative form is needed to prove entropy stability.

[Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) run all
their tests with FLUXO: the entropy-stable split-form DGSEM for resistive
GLM-MHD with the Powell and GLM non-conservative terms and BR1
visco-resistive terms, blended element-wise with first-order or TVD-ES
subcell finite volumes ([TeCNO schemes](/methods/tecno-scheme.md)). FLUXO
is a 3D code; the 2D runs use extruded meshes with one element in $z$, and
the meshes come from the HOPR generator (§6). The time integrator is
five-stage fourth-order SSP-RK with CFL 0.5. The TVD-ES subcell scheme
replaces only the volume integral and needs no additional MPI
communication (§4).

1. **Free-stream and entropy tests** on a heavily warped 3D mesh
   ($10^3$ elements, geometry degree 4, $N=4$ and $6$): free streams kept to
   $10^{-13}$–$10^{-15}$ with random element-wise blending; the EC entropy
   error converges at fourth order in the CFL number (§6.1;
   [free-stream preservation](/properties/free-stream-preservation.md)).
2. **[Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md)** with
   $256^2$ to $1024^2$ degrees of freedom, $N=3$ and $7$, compared with
   the second-order constrained-transport code Athena (§6.2).
3. **GEM reconnection challenge** (resistivity $10^{-3}$ and
   $5\times10^{-3}$, $512\times256$ and $1024\times512$ degrees of freedom).
   The DGSEM without subcell stabilization crashes from loss of
   positivity; with it the runs reach $t=100$ (§6.3).
4. **Io–plasma-torus interaction**: 165 888 curved hexahedra with
   geometry degree 2 and $N=4$, 20.736 M degrees of freedom, run to $t=10$
   and compared with Galileo magnetometer data along the I31 flyby
   (§6.4).

## Qualifications

- The performance figures are single-core measurements on the Euler
  equations. Non-conservative terms and MPI are outside the scope of
  Ranocha et al. (2023), §9. Rueda-Ramírez et al. (2021) report no timings.
- The Io comparison matches the Galileo data only after shifting two
  magnetic-field components by $+240$ nT and $-700$ nT (Rueda-Ramírez et
  al. (2021), §6.4).

# Citations

- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — §1, §4–4.1 Fig. 1, §6 Eq. (6.3), §7.1 Fig. 5, §7.3 Fig. 7, §9.
- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — §5, §5.2.1–5.2.3, §5.3.
- [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) — §4, §5 Eq. (89), §6.1–6.4 Table 1, Figs. 5–19 (arXiv v1).
