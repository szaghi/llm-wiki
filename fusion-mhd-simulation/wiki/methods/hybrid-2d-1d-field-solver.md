---
type: Method
title: "Hybrid 2D/1D field solver and the flute-ordering error"
description: "BOUT++ extension that inverts the vorticity–potential Helmholtz equation of each toroidal harmonic with a 2D solver in orthogonal flux coordinates for n = 0 and low n, and with the flute-ordered 1D radial solver for higher n; it removes the O(1/n) error of the flute ordering at low n and allows full-annulus edge simulations with zonal components."
status: established
aliases: [hybrid field solver, 2D/1D Laplacian inversion, flute ordering, flute-ordering approximation, low-n field solver]
tags: [finite-differences, linear-solver, numerics, ballooning, elm, pedestal, edge]
timestamp: 2026-10-16T20:00:00Z
---

# Hybrid 2D/1D field solver and the flute-ordering error

Reduced fluid models obtain the electrostatic potential from the vorticity by
inverting a perpendicular Helmholtz operator. [BOUT++](/software/bout-plus-plus.md)
evolves its fields in [field-aligned coordinates](/methods/field-aligned-coordinates.md)
and makes this inversion one-dimensional in radius by the **flute ordering**
$\partial_yF=0$, i.e. by dropping the derivatives along the field-aligned
coordinate $y$. The approximation "is not valid for n = 0 mode and may not
be valid for low-n modes"; it forced earlier BOUT++ runs to zero the $n=0$
flow and field and to simulate toroidal wedges of $1/N$ of the torus with
$N\sim5$ ([Seto et al. (2023)](/sources/seto-2023.md), §1, §3.1).
[Seto et al. (2023)](/sources/seto-2023.md) replace it, for the lowest
harmonics, by a 2D solver.

## The field equation

The solver inverts, for axisymmetric coefficients $a_2,a_1,a_0(\psi,\theta)$,
$$\Big(a_2\nabla_\perp^2+\frac{1}{a_1}\nabla a_1\cdot\nabla_\perp+a_0\Big)f=h,\qquad \nabla_\perp^2=\nabla^2-\nabla\cdot(\mathbf b\,\mathbf b\cdot\nabla),\quad \nabla_\perp=\nabla-\mathbf b\,\mathbf b\cdot\nabla$$
(Eq. 15). Coupling between coefficient and field harmonics is excluded (a
Boussinesq-type linearization, perturbed over equilibrium density small), so
each toroidal harmonic $n$ is inverted independently. In the
peeling–ballooning model of §4 the equation is
$[\nabla_\perp^2+B^2\nabla(B^{-2})\cdot\nabla_\perp]\delta\Phi=B^2\delta\varpi$ with
constant density (Eq. 27), i.e. $a_2=1$, $a_1=B^{-2}$, $a_0=0$.

## Three discretizations

- **Flute-ordered 1D** ($\mathcal L_{1D,n}$, Eq. 17): $\partial_y=0$, only
  $\psi$-derivatives kept, second-order central differences, Thomas
  tridiagonal algorithm or its parallel variants. The resonance condition
  $\partial_yF=in\hat qF+\partial_\theta F=0$ still reproduces the poloidal
  structure of moderate- and high-$n$ modes (§3.1).
- **Earlier 2D $n=0$ solver** (Eq. 18): in field-aligned $(x,y)$, which
  coincide with orthogonal flux coordinates only for $n=0$; second order,
  5-point stencil, PETSc GMRES with SOR preconditioning (Dudson and Leddy
  2017; Seto 2019, 2020). It does not extend to $n\ne0$ (§3.1).
- **New 2D solver** ($\mathcal L_{2D,n}$, Eq. 19): for each $n$ in orthogonal
  flux coordinates $(\psi,\theta)$, with no flute ordering, reducing to Eq. 18
  for $n=0$. The operator of harmonic $n$ is
  $$a_2\big[L^{10}\partial_\psi+L^{11}\partial_\psi^2+(L^{20}+in\,L^{23})\partial_\theta+L^{22}\partial_\theta^2+in\,L^{30}-n^2L^{33}\big]F+\frac{1}{a_1}\big(G^{1}\partial_\psi a_1\,\partial_\psi+G^{2}\partial_\theta a_1\,\partial_\theta+in\,G^{3}\partial_\theta a_1\big)F+a_0F=H,$$
  with, among the geometric coefficients,
  $L^{11}=G^1=|\mathbf B_{\mathrm{pol}}|^2R^2$,
  $L^{22}=G^2=B_\phi^2/(h_\theta^2B^2)$,
  $L^{23}=-2B_\phi|\mathbf B_{\mathrm{pol}}|/(h_\theta RB^2)$ and
  $L^{33}=|\mathbf B_{\mathrm{pol}}|^2/(R^2B^2)$, where
  $h_\theta=\sqrt{(\partial_\theta R)^2+(\partial_\theta Z)^2}$ (App. A). It is discretized with fourth-order central differences on
  a 9-point star stencil and solved by PETSc GMRES preconditioned with Hypre
  algebraic multigrid, which "is more effective" than SOR for this problem (no
  numbers given), using the previous step's solution as initial guess (§3.1–3.2,
  Fig. 1).

## Hybrid assembly

Harmonics $0\le n\le n_{2D}$ are inverted by the 2D solver and
$n_{2D}<n\le n_{1D}$ by the 1D solver,
$$F_n=\begin{cases}\mathcal L_{2D,n}^{-1}H_n(\psi,\theta), & 0\le n\le n_{2D},\\ \mathcal L_{1D,n}^{-1}H_n(\psi\,|\,\theta), & n_{2D}<n\le n_{1D},\end{cases}$$
and the result is transformed back to field-aligned coordinates by the
phase-shift transform (Eq. 20, Eq. 11). The perpendicular Laplacian and the
$a_1^{-1}\nabla a_1\cdot\nabla_\perp$ term inside the vorticity (and the
parallel current in electromagnetic models) are evaluated in the same hybrid
way; all other operators stay in quasi-ballooning coordinates (§3.3). Only the
flute ordering of the field-solver operators is removed; the flute ordering
built into the reduced-MHD model itself remains (§1). Because the $(\psi,\theta)$
grid is not field-aligned it must resolve the resonant harmonics
$m\sim nq$, which limits the 2D solver to low $n$ (§3.2).

## Verification and use

- **Linear ideal ballooning mode, cbm18_dens8** (see the
  [cbm18 benchmark](/benchmarks/cbm18-ballooning-benchmark.md)): at $n=20$
  the 2D and 1D solvers give $\gamma/\omega_A=0.244$ and $0.246$, against the
  earlier BOUT++ value 0.245 and ELITE 0.239 (§4, Fig. 3; $\omega_A$ the
  inverse poloidal Alfvén time of the source). The 1D solver is higher by
  about 1% at $n=20$ and about 36% at $n=5$, which the paper reads as
  qualitatively consistent with an $O(1/n)$ flute-ordering correction (Connor,
  Hastie and Taylor 1979) (Fig. 3). The $n=20$ eigenfunction carries poloidal
  harmonics $m=33$–51 (Fig. 4).
- **Drift-wave resistive ballooning mode, cbm18_dens4:** most unstable
  $n=32$ at $\gamma/\omega_A=7.86\times10^{-2}$; 1D and 2D solvers differ by
  2–8% for $n=11$–20 (§5.1, Fig. 5b).
- **Choice of $n_{2D}$:** $n_{2D}=4,8,12$ give nearly the same energy loss,
  zonal and non-zonal kinetic energy and spectra, with no spectral
  discontinuity at $n_{2D}$; $n_{2D}=4$ "is enough" (§5.2, Fig. 6).
- **Full versus quarter torus** (pedestal collapse, $n_{2D}=4$,
  $n_{1D}=80$): the final energy loss is similar, but in the full torus the
  low-$n$ and zonal components grow first and the collapse comes at
  $t\approx313\,\tau_A$ instead of $231\,\tau_A$, and a tearing-like $(m,n)=(2,1)$
  structure coexists with high-$n$ filaments (§5.3, Figs. 7–10; see
  [edge-localized mode](/definitions/edge-localized-mode.md)). The paper
  concludes that a wedge may suffice for the final energy loss but the full
  annulus is required for the loss process. A later analysis by the same
  authors of what is, by the compiler's identification (same model, grid and
  linear spectrum; the equilibrium is not named there), the same cbm18_dens4
  run resolves two crashes, the 2023 collapse being the second by the
  compiler's timing cross-check, and adds a half torus with a crash interval
  between the two
  ([Seto et al. (2024)](/sources/seto-2024.md), §III, Figs. 3, 13; see
  [two-stage ELM crash](/results/two-stage-elm-crash.md)). Those runs use
  the same split, $0\le n\le4$ in the 2D solver and $4<n\le80$ in the 1D
  solver, with $n\ge81$ filtered out (§II).
- **Cost:** the full-torus production run took $8.3\times10^5$ core-hours
  (4096 cores for 8.5 days), about 40% of it in the field solver (§5.3).

## Qualifications

- **Low-$n$ overestimate.** The claim that the 2D solver reduces "to some
  level" the low-$n$ overestimate of BOUT++ growth rates against ELITE and
  GATO reported by Dudson et al. (2011) rests on the 1D/2D comparison only; no
  ELITE or GATO low-$n$ values are re-plotted (§4, §6; reader's note).
- The $O(1/n)$ attribution is qualitative; the energy-loss conclusion rests on
  one case (§5.3).
- Seto et al. print the quasi-ballooning coefficient
  $L^{33}_{qb}=B^2/(R^2B_\phi^2)$, a typo for
  $B^2/(R^2|\mathbf B_{\mathrm{pol}}|^2)$ (Eq. A.12; reader's check, see the
  [field-aligned coordinates](/methods/field-aligned-coordinates.md) page).
- BOUT++ v4.4.2 stores fields in flux-surface coordinates but still takes
  derivatives in quasi-ballooning coordinates, so the low-$n$ problem remains
  open there (footnote 1).

# Citations

- [Seto et al. (2023)](/sources/seto-2023.md) — §1–6, Eqs. 15–20, 27, App. A, Figs. 1–10.
- [Seto et al. (2024)](/sources/seto-2024.md) — §II–III, Figs. 3, 13.
