---
type: Software
title: "CLT"
description: "Zhejiang University explicit 3D toroidal MHD code: fourth-order finite differences on a uniform cylindrical (R, φ, Z) grid, fourth-order Runge–Kutta, a cut-cell embedded boundary and an OpenACC GPU port; benchmarked against M3D-C1 on the 2/1 resistive tearing mode and the 1/1 resistive kink."
status: established
aliases: [CLT code]
tags: [full-mhd, finite-differences, gpu, tearing, kink, verification]
timestamp: 2026-10-16T18:35:00Z
---

# CLT

CLT is an explicit nonlinear toroidal MHD code from Zhejiang University
([Zhang et al. (2021)](/sources/zhang-2021.md), §1–2). It has two-fluid
capability, which the benchmark does not use (§2).

## Physics model

The benchmark runs single-fluid resistive MHD: continuity with density
diffusion acting on $\rho-\rho_0$; pressure with $\Gamma=5/3$, perpendicular
conduction acting on $p-p_0$ and parallel conduction acting on $p$; momentum
with a Laplacian viscosity $\nabla\cdot(\nu\nabla\mathbf v)$; Faraday's law;
and Ohm's law $\mathbf E=-\mathbf v\times\mathbf B+\eta(\mathbf J-\mathbf J_0)$
with $\mu_0\mathbf J=\nabla\times\mathbf B$ (Zhang et al. 2021, Eqs.
1.1–1.6). The subtraction of the equilibrium current and pressure keeps the
equilibrium from diffusing. The benchmark equations advance $\mathbf B$ by
Faraday's law, whereas M3D-C1 advances $\mathbf A$, whose curl is Eq. 1.4
(§2).
Quantities are normalized to $L_0=1$ m (page-local), $B=1$ T, a density of $10^{20}$ m$^{-3}$ and the
Alfvén time $L_0/v_A$; $\eta$ is normalized by $\mu_0L_0^2/\tau_A$, i.e. it is an
inverse Lundquist number referred to $L_0$ (§2). See the
[single-fluid visco-resistive MHD model](/methods/visco-resistive-mhd-model.md).

## Discretization and time integration

* Fourth-order central finite differences in $R$, $\phi$ and $Z$ on a uniform
  cylindrical grid; $256\times16\times256$ points for the tearing case and
  $256\times12\times256$ for the kink case (Zhang et al. 2021, §2).
* Explicit fourth-order Runge–Kutta with $\Delta t\approx8.5\times10^{-3}\,\tau_A$
  (§2), against $\Delta t=1.0\,\tau_A$ for the implicit M3D-C1 run of the same
  case.
* **Cut-cell boundary** (Duan et al.): grid points are classed as regular
  (fourth-order central, five points), first-type irregular (fourth-order
  biased stencils using boundary values), second-type irregular (central
  stencils using boundary and first-type points), dropped-inside points
  closer than half a cell to the boundary (updated by linear interpolation),
  dropped-outside points (not computed), and boundary points with a fixed
  boundary condition; a free boundary condition is planned. The cut-cell
  method replaces an earlier interpolation scheme that "reduces the parallel
  efficiency" (§2, Fig. 1).
* The QSOLVER equilibrium is interpolated directly onto the grid, with no
  Grad–Shafranov re-solve (§2, §4). See the
  [Grad–Shafranov equation](/definitions/grad-shafranov-equation.md).

## GPU

CLT is ported to GPUs with OpenACC, which "typically makes the code 200 times
faster" (Zhang et al. 2021, §2, attributed to the authors' earlier work; no
timing is shown in the benchmark paper).

## Verification

* **M3D-C1** ([CLT–M3D-C1 benchmark](/benchmarks/clt-m3d-c1-benchmark.md)):
  circular, $R/a=10$, $\beta\approx0$ QSOLVER equilibria, $\eta$ from
  $10^{-7}$ to $10^{-5}$ (normalized), other diffusivities $10^{-8}$ and
  $\kappa_\parallel=1$ (Zhang et al. 2021, §2–3).
  * 2/1 [tearing mode](/definitions/tearing-mode.md): CLT growth rates are
    always lower than M3D-C1's, by 7–11 % for $\eta\ge3\times10^{-7}$ and by
    24 % at $\eta=10^{-7}$ (compiler's check of Table 1; the paper says "about
    10%"); the printed fit is $\gamma\propto\eta^{0.601}$, close to the
    $\eta^{3/5}$ theory (Table 1, Fig. 4).
  * 1/1 [resistive internal kink](/definitions/resistive-internal-kink.md):
    differences of 2.7–6.3 % ("about 5%"), printed fit $\eta^{0.31}$ against
    Coppi's $\eta^{1/3}$ (Table 2, Fig. 12).
  * Nonlinear runs at $\eta=10^{-5}$: $n=1$ kinetic-energy saturation
    $1.5\times10^{-6}$ (CLT) against $1.4\times10^{-6}$ (M3D-C1) for tearing,
    peak $4.4\times10^{-5}$ against $4.2\times10^{-5}$ for the kink, with
    near-identical Poincaré plots; $n=0$ and $n=2$ grow as beat modes at twice
    the $n=1$ rate (Figs. 6–9, 14–16). The authors attribute residual
    differences to the initial perturbation (pure $n=1$ in CLT, random in all
    $n$ in M3D-C1) and to the different equilibrium treatment (§4).
* **MARS-F**: an earlier CLT benchmark on the linear plasma response to RMPs
  (§2; no numbers in the cited paper).

## Limitations

* The benchmark is at large aspect ratio and zero $\beta$ only; finite $\beta$
  and $R/a\sim3$–4 are future work (Zhang et al. 2021, §4).
* No resolution-convergence study or timing is reported (§2).
* The printed scaling exponents (0.601, 0.31) are not reproduced by a
  log–log fit of the tabulated growth rates (compiler's fit: 0.54 and 0.285);
  the qualification is recorded on the
  [tearing-mode](/definitions/tearing-mode.md) and
  [resistive-internal-kink](/definitions/resistive-internal-kink.md) pages.
* [Ma & Guo (2022)](/sources/ma-2022.md) (§4.1) cite CLT-group resistive-kink
  results (Wang & Ma 2015) among the earlier simulations their SCELT scaling
  matches, without numbers.

# Citations

1. [Zhang et al. (2021)](/sources/zhang-2021.md) — §§1–4, Tables 1–2, Figs. 1, 4, 6–16.
2. [Ma & Guo (2022)](/sources/ma-2022.md) — §4.1.
