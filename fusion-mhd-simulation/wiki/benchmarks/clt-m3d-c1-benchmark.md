---
type: Benchmark
title: "CLT–M3D-C1 tearing and resistive-kink benchmark"
description: "Linear and nonlinear code-to-code benchmark of the explicit finite-difference CLT code against the implicit finite-element M3D-C1 code for the 2/1 resistive tearing mode and the 1/1 resistive kink in circular, R0/a = 10, zero-beta equilibria; growth rates agree to 3-24% and are fitted to the eta^(3/5) and eta^(1/3) scalings."
status: established
aliases: [CLT M3D-C1 benchmark, Zhang 2021 benchmark]
tags: [benchmark, verification, tearing, kink, full-mhd, finite-differences, finite-elements]
timestamp: 2026-10-16T00:00:00Z
---

# CLT–M3D-C1 tearing and resistive-kink benchmark

[Zhang et al. (2021)](/sources/zhang-2021.md) benchmark two nonlinear toroidal
MHD codes that share a physics model but differ in every numerical choice. The
test problems are the two classical resistive core instabilities, the
$m/n=2/1$ [resistive tearing mode](/definitions/tearing-mode.md) and the
$m/n=1/1$ [resistive internal kink](/definitions/resistive-internal-kink.md).
The equilibria are circular, large-aspect-ratio and zero-$\beta$, chosen so
that the linear growth rates can be checked against analytic scalings (§4).

## The two codes

| | [CLT](/software/clt.md) | [M3D-C1](/software/m3d-c1.md) |
|---|---|---|
| Space | 4th-order finite differences on a uniform $(R,\phi,Z)$ grid; cut-cell boundary | $C^1$ triangular elements in $(R,Z)$, Hermite cubic in $\phi$ |
| Time | explicit 4th-order Runge–Kutta, $\Delta t\approx8.5\times10^{-3}\tau_A$ | implicit $\theta_{\mathrm t}$-scheme, $\Delta t=1.0\,\tau_A$ |
| Linear runs | full 3D grid seeded with $n=1$ | "2D-complex" single-harmonic version |
| Resolution, tearing | $256\times16\times256$ | 4800 poloidal elements packed at $q=2$, 16 toroidal planes |
| Resolution, kink | $256\times12\times256$ | 3816 elements packed at $q=1$, 12 planes |
| Equilibrium | interpolates the QSOLVER solution directly | re-solves Grad–Shafranov on its own basis from QSOLVER profiles |
| Initial perturbation | $n=1$ only | random, all toroidal harmonics |

Source: Zhang et al. (2021), §2, Figs. 1, 3, 11.

## Model

Both codes solve single-fluid resistive MHD (§2, Eqs. 1.1–1.6):

$$\begin{aligned}
\partial_t\rho&=-\nabla\cdot(\rho\mathbf v)+\nabla\cdot[D_\perp\nabla(\rho-\rho_0)],\\
\partial_t p&=-\mathbf v\cdot\nabla p-\Gamma p\nabla\cdot\mathbf v+\nabla\cdot[\kappa_\perp\nabla_\perp(p-p_0)]+\nabla\cdot[\kappa_\parallel\nabla_\parallel p],\\
\partial_t\mathbf v&=-\mathbf v\cdot\nabla\mathbf v+(\mathbf J\times\mathbf B-\nabla p)/\rho+\nabla\cdot(\nu\nabla\mathbf v),\\
\partial_t\mathbf B&=-\nabla\times\mathbf E,\qquad \mathbf E=-\mathbf v\times\mathbf B+\eta(\mathbf J-\mathbf J_0),\qquad \mu_0\mathbf J=\nabla\times\mathbf B,
\end{aligned}$$

- $\Gamma=5/3$; the subscript 0 marks equilibrium fields; $\nu$ is a kinematic viscosity.
- The density diffusivity acts on the full gradient (isotropic) in the source; it is written $D_\perp$ here for want of a registry symbol.
- Density diffusion, perpendicular conduction and resistive diffusion act on
  the deviation from equilibrium, so the equilibrium is not diffused away.
- Parallel conduction acts on the full pressure.
- The viscosity is a plain Laplacian, not a stress tensor.
- M3D-C1 advances the vector potential; the induction equation is its curl.
- Zhang et al. state that "the definitions and the normalizations of these
  dissipation parameters are the same in the two codes".
- The model is a special case of the
  [single-fluid visco-resistive MHD model](/methods/visco-resistive-mhd-model.md).

**Normalization.**

- Reference scales: length 1 m, field 1 T, density $10^{20}$ m$^{-3}$.
- Time is in units of $\tau_A$ built on the 1 m length.
- $\eta$ is in units of $\mu_0(1\,\mathrm m)^2/\tau_A$. With $a=1$ m, the
  normalized $\eta$ is the inverse Lundquist number $S^{-1}$.
- Diffusivities are in units of $(1\,\mathrm m)^2/\tau_A$.

## Equilibria

Both equilibria are computed by QSOLVER: circular, $R_0/a=10$, $a=1$ m,
$\beta\approx0$.

- **Tearing (Eq. 1.7).**
  $q(\psi_N)=q_0\sqrt{1+\psi_N^2\,[(q(1)/q_0)^2-1]}$ with $q_0=1.75$ and
  edge value $q(1)=2.5$. The single $q=2$ surface lies at $r/a\approx0.7$,
  with $r=a\sqrt{\psi_N}$ (Fig. 2).
- **Kink (Eq. 1.8).** A rational $q(\psi_N)$ with $q_0=0.7$ and $q(1)=3.6$.
  - Two further parameters, printed as $q_0'=2.0$ and $q_e'=5.0$, are not
    defined in the paper. Differentiating Eq. 1.8 identifies them as the
    slopes $dq/d\psi_N$ at the axis and at the edge (reader's inference).
  - The $q=1$ surface lies at $r/a\approx0.43$ (Fig. 10).

**Dissipation.**

- Linear scans: $\eta=10^{-7}$ to $10^{-5}$, with
  $D_\perp=\nu=\kappa_\perp=10^{-8}$ and $\kappa_\parallel=1$.
- Nonlinear runs: $\eta=10^{-5}$. The other coefficients are not restated
  for these runs.

## Results

**Linear growth rates** ($\gamma\tau_A$; Tables 1–2; relative differences
computed from the printed values, relative to M3D-C1):

| $\eta$ | $10^{-5}$ | $3\times10^{-6}$ | $10^{-6}$ | $3\times10^{-7}$ | $10^{-7}$ |
|---|---|---|---|---|---|
| 2/1 tearing, M3D-C1 | 0.00178 | 0.00116 | 0.000675 | 0.000330 | 0.000178 |
| 2/1 tearing, CLT | 0.00165 | 0.00104 | 0.000604 | 0.000293 | 0.000135 |
| difference | 7.3% | 10.3% | 10.5% | 11.2% | 24.2% |
| 1/1 kink, M3D-C1 | 0.0115 | 0.00870 | 0.00640 | 0.00440 | 0.00320 |
| 1/1 kink, CLT | 0.0111 | 0.00837 | 0.00617 | 0.00428 | 0.00300 |
| difference | 3.5% | 3.8% | 3.6% | 2.7% | 6.3% |

- **Systematic offset.** CLT is always lower.
- **Printed fits.**
  - Tearing: $\eta^{0.601}$ (CLT) and $\eta^{0.58}$ (M3D-C1), compared with
    the FKR $3/5$ (Fig. 4).
  - Kink: $\eta^{0.31}$ and $\eta^{0.30}$ (legend 0.312 and 0.301),
    compared with $1/3$ (Fig. 12).
- **Mode structures.** The linear mode structures (toroidal electric field)
  match by eye (Fig. 5).

**Nonlinear runs at $\eta=10^{-5}$.**

- **Tearing.**
  - The saturated $n=1$ kinetic energy is $1.5\times10^{-6}$ (CLT) and
    $1.4\times10^{-6}$ (M3D-C1), in normalized units.
  - The $n=0$ and $n=2$ harmonics grow as beat modes at twice the $n=1$
    rate. Saturation comes near $1.8\times10^4\,\tau_A$.
  - The saturated $2/1$ islands are "almost the same" in Poincaré plots.
  - Source: Figs. 6–9.
- **Kink.**
  - The peak $n=1$ kinetic energy is $4.4\times10^{-5}$ (CLT) and
    $4.2\times10^{-5}$ (M3D-C1), reached near $2400\,\tau_A$.
  - The growth rate then turns negative (the crash). The post-crash
    evolution stays qualitatively the same in both codes.
  - Source: Figs. 14–16.
- **Time alignment.** The M3D-C1 curves are shifted by $4200\,\tau_A$
  (tearing) and $270\,\tau_A$ (kink) to overlay CLT. The time to saturation
  is therefore not part of the comparison.

**Attributed causes of the differences** (§4, both *stated*, not tested):

- The different initial perturbations explain the early-time harmonic
  differences and "hardly influence" the growth rates.
- The slightly different equilibria (re-solved vs interpolated) "could be
  why" the nonlinear evolutions are not identical.

No resolution convergence study is reported.

## Qualifications

- **"About 10%" understates the tearing spread.** The caption and §3.1 say
  "about 10% for each case". At $\eta=10^{-7}$ the difference is 24%
  relative to M3D-C1, and 32% relative to CLT.
- **Fit exponents not reproducible from the tables over the full range.**
  - *Compiler's check, not a source claim.* Fitting all five points in
    log–log gives 0.54 (CLT) and 0.51 (M3D-C1) for tearing, and 0.285 and
    0.281 for the kink.
  - The three lowest-$\eta$ points give 0.65 and 0.58 for tearing, and 0.313
    and 0.301 for the kink. Three of the four printed values are therefore
    reproduced by a low-$\eta$ fit. The CLT tearing value of 0.601 matches
    the four lowest points instead (0.60).
  - The fit range is not stated. In Figs. 4 and 12 the drawn fit lines lie
    visibly above the data at $\eta=10^{-5}$.
  - The approach to $3/5$ and $1/3$ is real but holds only at the low-$\eta$
    end. This is consistent with the asymptotic nature of the theory and
    with [Jiang et al. (2024)](/sources/jiang-2024.md) (§IX C, Fig. 28),
    who recover $3/5$ only below $10^{-6}$ Ω m.
- **Nonlinear linear-phase rate vs Table 1.** In Fig. 7, the linear-phase
  $n=1$ growth rate is about $1.4$–$1.45\times10^{-3}\,\tau_A^{-1}$ in both
  codes at $\eta=10^{-5}$. Table 1 gives 0.00165 (CLT) and 0.00178 (M3D-C1)
  at the same $\eta$. The gap is unexplained; the dissipation of the
  nonlinear runs is not restated. For the kink, Fig. 15 (about $0.011$) is
  consistent with Table 2.
- **Growth-rate definition.** The definition used in the nonlinear figures
  (energy or amplitude rate) is not stated.
- **Scope.** The authors defer finite-$\beta$ and realistic-aspect-ratio
  ($R_0/a\sim3$–4) benchmarks to future work (§4).

## Related tests

[Ma & Guo (2022)](/sources/ma-2022.md) (§4) use the same tearing
$q$-profile family ($q_0=1.75$, $q(1)=2.5$), at $R_0/a=5$, for the linear
eigenvalue code [SCELT](/software/scelt.md).
[Jiang et al. (2024)](/sources/jiang-2024.md) (§IX C) use it at $R_0=10$ m,
$a=1$ m for [GMEC](/software/gmec.md). Their printed Eq. 60 inverts the shape
constant relative to their own Fig. 24 (recorded on their Source page).
Neither paper compares growth-rate values with CLT or M3D-C1. The JOREK
nonlinear $2/1$ comparison with SpeCyl uses the same design choice
($R_0/a=10$, zero $\beta$, $S=10^6$) and agrees within about 5%
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §4.4, Fig. 20).

## Contradictions

None open.

# Citations

- [Zhang et al. (2021)](/sources/zhang-2021.md) — §§1–4, Eqs. 1.1–1.8, Tables 1–2, Figs. 1–16.
- [Ma & Guo (2022)](/sources/ma-2022.md) — §4.
- [Jiang et al. (2024)](/sources/jiang-2024.md) — §IX C.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — §4.4.
