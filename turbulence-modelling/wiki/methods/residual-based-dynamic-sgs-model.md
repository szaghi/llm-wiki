---
type: Method
title: "Residual-based dynamic subgrid-scale model"
description: "The residual-based dynamic SGS model sets the eddy viscosity from the residual of the inviscid filtered equations, capped by a first-order-upwind bound. One source compares its residual and time-derivative-free variants, element-constant and nodal, with Smagorinsky and Vreman in a continuous spectral-element code on tracer, Burgers, Taylor–Green and density-current tests."
status: established
aliases: [DSGS, Dyn-SGS, dynamic sub-grid scale model, R-DSGS, T-DSGS, residual-based eddy viscosity, residual-based artificial viscosity]
tags: [les, sgs-model, eddy-viscosity, spectral-element, numerical-dissipation]
timestamp: 2026-10-28T07:10:00Z
---

# Residual-based dynamic subgrid-scale model

The **residual-based dynamic subgrid-scale (DSGS) model** sets the eddy
viscosity $\nu_t$ of the
[eddy-viscosity closure](/definitions/boussinesq-hypothesis.md) of
[LES](/definitions/large-eddy-simulation.md) from the size of the residual
of the inviscid filtered equations. The viscosity is large where the
resolved solution fails to satisfy the equations, at fronts and
discontinuities, and small where the flow is smooth. It is capped by a
bound of first-order-upwind type. The model was not built as an LES
closure: [Reddy et al. (2026)](/sources/reddy-2026.md) state (§1) that it
was designed to stabilize high-order continuous- and discontinuous-Galerkin
spectral-element solvers and capture sharp gradients, and that "as a
by-product" it is effective for turbulence modelling. They cite its
construction to Nazarov & Hoffman (2013) and Marras et al. (cited).
"Dynamic" here means that the coefficient follows the residual; there is
no test filter and no
[Germano identity](/methods/dynamic-procedure.md).

## Construction

Reddy et al. (§2, §3.3, Eqs. 10–14) apply the model to the Favre-filtered
compressible Euler equations of a low-Mach atmospheric model. The equations
are written with potential temperature, page-local $\vartheta$ (not the
momentum thickness $\theta$), and a passive tracer, page-local $q$. The
residuals of the filtered inviscid equations are

$$\begin{aligned}
\mathcal R(\tilde u_i)&=\partial_t\tilde u_i+\tilde u_j\partial_j\tilde u_i+\frac1{\bar\rho}\partial_i\bar p+g\delta_{i3},\\
\mathcal R(\tilde\vartheta)&=\partial_t\tilde\vartheta+\tilde u_j\partial_j\tilde\vartheta,\qquad
\mathcal R(\tilde q)=\partial_t\tilde q+\tilde u_j\partial_j\tilde q ,
\end{aligned}$$

with a residual of the continuity equation defined alike. $\mathcal R$ is
page-local, and $g$ is the gravitational acceleration. The time derivatives
are first-order backward differences; a second-order difference made "no
significant differences" (results not shown, §3.3).

The momentum eddy viscosity is

$$\nu_t=\min(\nu_{\max},\nu_{\mathrm{res}}),\qquad
\nu_{\max}=\tfrac12\Delta\left\|\,|\tilde{\boldsymbol u}|+\sqrt{\gamma\bar p/\bar\rho}\,\right\|_\infty,\qquad
\nu_{\mathrm{res}}=C\Delta^2\frac{\|\mathcal R(\tilde{\boldsymbol u})\|_\infty}{\|\tilde{\boldsymbol u}-\langle\tilde{\boldsymbol u}\rangle_\Omega\|_{\infty,\Omega}} .$$

Here:

- $\nu_{\max}$ and $\nu_{\mathrm{res}}$ are page-local;
- $|\tilde{\boldsymbol u}|+\sqrt{\gamma\bar p/\bar\rho}$ is the maximum wave speed;
- $\langle\cdot\rangle_\Omega$ (page-local) is the average over the whole domain, so the denominator is a normalization constant;
- $C=1$ in every run.

The source writes $\mu$ for this diffusivity, although the quantity has
kinematic units, and a hat for the domain average.

The scalar diffusivities $\kappa_\vartheta$ and $\alpha_q$ (page-local)
follow the same pattern with $\mathcal R(\tilde\vartheta)$ and
$\mathcal R(\tilde q)$, with the same cap, and are scaled by an artificial
Prandtl number, $Pr/(\gamma-1)$ with $Pr=0.7$ (Eqs. 13–14). The closures are

$$\tau_{ij}=-2\nu_t\tilde S_{ij},\qquad
\bar\rho(\widetilde{\vartheta u_j}-\tilde\vartheta\tilde u_j)=-\kappa_\vartheta\,\partial_j\tilde\vartheta ,$$

and the tracer flux is closed alike with $\alpha_q$ (Eqs. 4–7).

Reddy et al. argue (§3.3) that the residual scales as $\Delta^{-1}$ at a
discontinuity and is small in smooth regions. The cap $\nu_{\max}$
"is equivalent to a stable upwind scheme in regions with sharp
discontinuities". In the Burgers test the model computes one coefficient
per equation, which the authors credit for its stability (§6.2); in the
density current a single coefficient serves both momentum equations, "as
is done in the other SGS models" (§8.1).

## Variants

Reddy et al. (§3.3) define two residual choices and two spatial
representations of the coefficient.

| Variant | Residual | Coefficient representation |
|---|---|---|
| R-DSGS:E | full residual, with $\partial_t$ | one value per element, the maximum over its Gauss–Lobatto–Legendre (GLL) points |
| R-DSGS:N | full residual, with $\partial_t$ | nodal, expanded in the same polynomial basis as the solution |
| T-DSGS:E | residual with all time derivatives omitted | one value per element |
| T-DSGS:N | residual with all time derivatives omitted | nodal |

- **T-DSGS.** T-DSGS is the only variant the paper introduces. The authors
  call it "transient-based" and state that its coefficients "are
  proportional to the transience" of the flow. As defined, however, it keeps
  only the spatial part of the residual.
- **Nodal coefficient.** The nodal form is the paper's stated departure from
  earlier element-based practice. The authors write (§1) that SGS models in
  element-based Galerkin methods had assumed an eddy viscosity constant
  within each element, even for high-order elements. A variable coefficient
  needs the variable-coefficient diffusion term integrated by parts in the
  weak form (§4, Eq. 18).
- **Expected dissipation.** The elemental form is expected to be more
  dissipative, because each element takes the maximum over its points
  (§3.3). R-DSGS is expected to be less dissipative than T-DSGS, because
  "the magnitude of the residual is typically smaller than the unsteadiness
  of the flow" (§5.2, §9).

## Numerical setting

All tests use the continuous-Galerkin
[spectral-element method](/methods/spectral-element-method.md) of the
atmospheric model NUMA with polynomial degree $N=4$ (§4). Its main features:

- tensor-product Lagrange bases on $(N+1)^3$ GLL points;
- inexact collocated quadrature, giving a diagonal mass matrix;
- direct stiffness summation across elements;
- implicit (grid) filtering.

The filter width is printed as

$$\Delta=\frac{\min(\Delta x,\Delta y,\Delta z)}{N+1},$$

with $\Delta x$, $\Delta y$, $\Delta z$ the paper's grid spacings
(page-local); the values it prints for the tracer, Burgers and
Taylor–Green cases equal the element size divided by $N$ *(compiler
check, not in the sources)*, and the paper does not say whether the
formula uses those values or the element sizes. Table 1 lists
alternatives for anisotropic grids (§3.4). Time integration is a
five-stage third-order Runge–Kutta scheme, or an implicit–explicit
additive Runge–Kutta scheme for the density current. The authors call the
spectral-element discretization "ideal" for comparing SGS models "due to
the lack of inherent numerical dissipation" (§1); see
[numerical dissipation](/properties/numerical-dissipation.md).

## Comparison with Smagorinsky and Vreman

Reddy et al. compare the four DSGS variants with the
[Smagorinsky model](/methods/smagorinsky-model.md) ($C_s=0.14$, 0.21 for
the Burgers test) and the [Vreman model](/methods/vreman-model.md)
($c\approx2.5C_s^2$). All results are a posteriori; the only table is of
density-current front positions.

- **Passive tracers in a reversing deformational flow** (§5, Figs. 2–3).
  The test transports two slotted cylinders on $80\times40$ elements.
  - Smagorinsky keeps the discontinuity sharp, but its errors in the
    extrema are 0.12 and 0.15 kg/kg. Vreman's errors are about 0.05 kg/kg.
  - T-DSGS:E diffuses the interface most and has the smallest errors in
    the extrema.
  - Vreman and R-DSGS:N give "the best balance" between interface
    sharpness and overshoot reduction.
- **Two-dimensional inviscid Burgers system with discontinuities** (§6,
  Figs. 4–6). The test runs on $60\times60$ elements to $t=1$ s.
  - Smagorinsky and Vreman oscillate near and away from the
    discontinuities, and Vreman diverges at $t=0.7$ s.
  - All DSGS variants stay stable, with one coefficient per equation.
  - R-DSGS:N gives the least dissipated non-oscillatory solution; T-DSGS:E
    gives the most dissipated one.
  - The authors attribute Vreman's divergence to the single coefficient
    shared by both equations. The paper reports no DSGS run with a single
    shared coefficient on this test.
- **[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)** (§7,
  Figs. 7–8). The domain is a $(2\pi)^3$ box with $32^3$ elements.
  - The elemental DSGS variants are the most dissipative of the six models.
  - R-DSGS:N conserves kinetic energy best before $t^*\approx12$ but has
    dissipated more by $t^*\approx24$.
  - Vreman conserves more kinetic energy than Smagorinsky.
  - All models peak in dissipation rate near $t^*\approx8$, against
    $t^*\approx9$ in the DNS of Brachet et al. (cited).
  - The nodal DSGS variants give the largest enstrophy.
  - All spectra show a $k^{-5/3}$ range for $k<32$.
- **Straka density current** (§8, Figs. 9–10, Table 2). This is a cold
  bubble in a $25\times6.4$ km domain at effective resolutions of 50, 25
  and 12.5 m (§8.1), the element size over $N$.
  - At $t=900$ s the fronts of all six models lie in [14 600, 15 040] m at
    50 m, [14 900, 15 120] m at 25 m and [15 075, 15 160] m at 12.5 m. The
    literature range is [14 400, 15 030] m.
  - The front advances monotonically with refinement for every model
    except Smagorinsky (15 034, 15 117, 15 091 m).
  - Kelvin–Helmholtz rotors appear at 50 m with Smagorinsky and Vreman,
    and only at 25 and 12.5 m with DSGS. Nodal DSGS resolves them at
    coarser resolution than elemental DSGS.
  - Smagorinsky and Vreman give the largest tracer overshoots; elemental
    DSGS damps them (supplementary figures, not in the file read).

The overall ranking of the conclusions (§9) favours R-DSGS:N. Smagorinsky
and Vreman produce Gibbs oscillations that DSGS damps, DSGS is "more
robust" as a stabilization, and R-DSGS:N "best preserves kinetic energy".

## Relation to other closures

Reddy et al. (§1) present the model as a stabilization of high-order
Galerkin solvers that is effective for turbulence "as a by-product". Other
viscosities driven by a smoothness indicator and bounded by a first-order
value are on
[artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md);
other uses of one dissipation for stabilization and subgrid modelling are
on [implicit LES](/definitions/implicit-les.md) and
[spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md).
Reddy et al. distinguish their approach from implicit LES, which they
call "very different" (§1): the model is an explicit eddy viscosity added
to an implicitly (grid-)filtered solution (§2.1).

## Qualifications

- **Version read.** The claims are those of a preprint dated 4 March 2021;
  the 2026 version of record was not read.
- **Euler or Navier–Stokes.** The title speaks of the Navier–Stokes
  equations, but §2 solves the compressible Euler equations, and no
  molecular viscosity appears in any test.
- **Internal inconsistencies in which variant is most dissipative or
  sharpest.**
  - §7.2 calls the elemental DSGS variants the most dissipative in the
    Taylor–Green vortex, then says that the R-DSGS models have the highest
    and "consistently higher" dissipation rate.
  - The abstract credits Smagorinsky and Vreman with resolving finer
    structures in shear flows, while the end of §8.2 and of §9 credit
    R-DSGS:N with the least diffused rotors.
  - These statements are printed, not reconciled.
- **Printed slips.**
  - §9 says Smagorinsky preserves stability "until $t=0.7$ s" in the
    Burgers test, while §6.2 says Smagorinsky "does not diverge" and its
    solution is shown at $t=1$ s; 0.7 s is Vreman's divergence time.
  - The §3.1 prose writes $S_{ij}=\partial_ju_i+\partial_iu_j$ without the
    factor $\tfrac12$ of p. 4.
  - Table 1 divides one filter width by $N$ while the width used divides
    by $N+1$.
  - Eq. (12) carries an outer "max" that Eqs. (13a,b) omit.
- **Physical model.** The closure $\tau_{ij}=-2\nu_t\tilde S_{ij}$ is applied
  to the full stress, not its deviatoric part. Reddy et al. define $\tau_{ij}$
  with $\bar\rho$ but omit $\bar\rho$ in the closure (Eqs. 3–4).

# Citations

- [Reddy et al. (2026)](/sources/reddy-2026.md) — preprint of 4 March 2021: §1 (origin, nodal coefficient, spectral elements as "ideal"); §2 (filtered equations, Eqs. 1–7); §3.1–3.4 (Smagorinsky, Vreman, DSGS Eqs. 10–14, variants, Table 1 filter widths); §4 (CG spectral elements, Eq. 18); §5.2, Figs. 2–3 (tracers); §6.2, Figs. 4–6 (Burgers); §7.2, Figs. 7–8 (Taylor–Green vortex); §8.2, Figs. 9–10, Table 2 (density current); §9 (conclusions).
