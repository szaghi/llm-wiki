---
type: Method
title: "Spalart–Allmaras model and its corrections"
description: "The one-equation eddy-viscosity RANS model transporting the working variable ν̃: its equations and constants, the negative, rotation–curvature, helicity and quadratic-constitutive-relation variants, field-inversion and data-assimilation corrections, its role as host of detached-eddy simulation, and evidence from compressors, rotors, airfoils and high-lift flows."
status: established
aliases: [SA model, Spalart-Allmaras, SA-noft2, SA-neg, negative SA, SA-noft2-QCR2000, β-augmented SA, SA-RC, SARC, SA-R, SA-Helicity, SA-QCR, QCR2000, QCR2013, quadratic constitutive relation]
tags: [rans, eddy-viscosity, turbomachinery, separated-flow, field-inversion]
timestamp: 2026-10-26T15:44:00Z
---

# Spalart–Allmaras model and its corrections

The Spalart–Allmaras (SA) model is a one-equation RANS closure: it transports
a working variable $\tilde\nu$ from which the eddy viscosity of the
[Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md) is computed,
$\nu_t=\tilde\nu f_{v1}$, and it carries no turbulent kinetic energy. With
SST variants it makes up most of the high-lift workshop RANS submissions
recalled by Goc et al. (2021); it is the host model of the field-inversion corrections of
Duraisamy et al. (2019), and the starting point of a family of corrections
for rotation, curvature, helicity and stress anisotropy. On this page the
strain and rotation tensors and their magnitudes $\lvert S\rvert$,
$\lvert\Omega\rvert$ are those of the mean velocity $\langle u_i\rangle$.

## Baseline equations

As printed by Li & Liu (2022), after Spalart & Allmaras (1994)
([Li & Liu (2022)](/sources/li-2022.md), Eqs. 1–5, 33–34):

$$\begin{aligned}
\frac{D\tilde\nu}{Dt}={}&c_{b1}(1-f_{t2})\,S_{\mathrm{SA}}\,\tilde\nu-\Big[c_{w1}f_w-\frac{c_{b1}}{\kappa^2}f_{t2}\Big]\Big(\frac{\tilde\nu}{d}\Big)^2\\
&+\frac1\sigma\Big[\partial_j\big((\nu+\tilde\nu)\partial_j\tilde\nu\big)+c_{b2}\,\partial_i\tilde\nu\,\partial_i\tilde\nu\Big],
\end{aligned}$$

$$S_{\mathrm{SA}}=\lvert\Omega\rvert+\frac{\tilde\nu}{\kappa^2d^2}f_{v2},\qquad
f_w=g\Big[\frac{1+c_{w3}^6}{g^6+c_{w3}^6}\Big]^{1/6},\qquad
g=r+c_{w2}(r^6-r),\qquad r=\min\Big(\frac{\tilde\nu}{S_{\mathrm{SA}}\kappa^2d^2},10\Big),$$

$$\mu_t=\rho\tilde\nu f_{v1},\qquad f_{v1}=\frac{\chi^3}{\chi^3+c_{v1}^3},\qquad \chi=\tilde\nu/\nu,\qquad c_{v1}=7.1 .$$

Let $S_{\mathrm{SA}}$ denote the model's modified vorticity (page-local; the
original papers write it with a tilde, which the registry reserves for
$\tilde\nu$ and Favre filtering). Li & Liu call $\lvert\Omega\rvert$ "the
vorticity" without a formula, and give the value of $c_{v1}$ only: the
constants $c_{b1},c_{b2},\sigma,\kappa,c_{w1},c_{w2},c_{w3}$ and the function
$f_{v2}$ are not printed. $f_{t2}=c_{t3}\exp(-c_{t4}\chi^2)$ makes $\tilde\nu=0$ a
stable laminar solution so that transition happens at a prescribed trip; the
trip term $f_{t1}$ is mentioned but not used. Away from the buffer layer and
the viscous sublayer $\mu_t$ and $\tilde\nu$ are linearly proportional (§3.2).

### Constants and printed forms in other sources

Alauzet et al. (2022) print the same equation with the trip term
$f_{t1}(\Delta\boldsymbol u)^2$, which they set to zero, and the constants
$\sigma=2/3$, $c_{b1}=0.1355$, $c_{b2}=0.622$, $\kappa=0.41$, $c_{w2}=0.3$,
$c_{w3}=2$, $c_{v1}=7.1$, with $f_{v2}=1-\chi/(1+\chi f_{v1})$ and
$S_{\mathrm{SA}}$ built on the vorticity magnitude $\lvert\nabla\times\boldsymbol u\rvert$,
which is the registry's $\lvert\Omega\rvert$
([Alauzet et al. (2022)](/sources/alauzet-2022.md), §2.3, Eqs. 8–9). They
drop $f_{t2}$ as well (SA-noft2), following the argument that it is
unnecessary without the trip, and note that the model "is not a
conservative model", pointing to Catris & Aupoix for a conservative form.
They print $c_{w1}=c_{b1}/\kappa+(1+c_{b2})/\sigma$; see Qualifications.

Basile et al. (2023) recall the near-wall design of the functions: $f_{v1}$
and $f_{v2}$ make $\tilde\nu=\kappa u_\tau y$ hold in the viscous, buffer and
log layers and $S_{\mathrm{SA}}=u_\tau/(\kappa d)$ in the log layer, and $f_w$
lowers $\nu_t$ in the outer layer ([Basile et al. (2023)](/sources/basile-2023.md),
§2.2). In the log layer, where $f_w=1$ and the molecular viscosity is
negligible, the equation of Li & Liu and Alauzet et al. then balances
$c_{b1}u_\tau^2+\sigma^{-1}(1+c_{b2})\kappa^2u_\tau^2=c_{w1}\kappa^2u_\tau^2$, i.e.
$c_{w1}=c_{b1}/\kappa^2+(1+c_{b2})/\sigma\approx3.24$ with Alauzet et al.'s
constants *(compiler check, not in the sources)*.

Yan et al. (2022) print a different baseline (§2.1, Eqs. 2–4): the
production uses
$(1-f_{t2})\lvert S\rvert+\tfrac{\tilde\nu}{\kappa^2d^2}\big[(1-f_{t2})f_{v2}+f_{t2}\big]$,
with $\lvert S\rvert$ the norm of the **mean strain-rate** tensor (norm not
specified), and $r$ uses $\hat S=\max\big(\lvert S\rvert+\tilde\nu f_{v2}/(\kappa^2d^2),0\big)$
(page-local $\hat S$, not a test filter). They print $\sigma=2/3$ and
$\kappa=0.41$ and no other constant.

Cato et al. (2023) print the same constants as Alauzet et al.
($c_{v1}=7.1$, $c_{b1}=0.1355$, $c_{b2}=0.622$, $\sigma=2/3$, $\kappa=0.41$,
$c_{w2}=0.3$, $c_{w3}=2$, the same $f_{v2}$) and give
$c_{w1}=c_{b1}/\kappa^2+(1+c_{b2})/\sigma$, the form required by the log-layer
balance above; they write the von Kármán constant as $k$, the letter of the
turbulent kinetic energy. They regularize the vorticity magnitude as
$\sqrt{\lvert\Omega\rvert^2+M^2}-M$ with $M=10^{-5}$ (page-local $M$, not a
Mach number) to keep the model
differentiable for adjoint computations, and have no trip term
([Cato et al. (2023)](/sources/cato-2023.md), §II A, Eqs. 2–4).

Fanizza et al. (2025) print the compressible conservative form, with
$\rho\tilde\nu$ as the transported variable, diffusion coefficient
$(\mu+\rho\tilde\nu)/\sigma$, $\chi=\rho\tilde\nu/\mu$, $S_{\mathrm{SA}}$ built on the
vorticity magnitude, no $f_{t2}$ and no trip, and the constants $\sigma=2/3$,
$c_{b1}=0.1355$, $c_{b2}=0.622$, $\kappa=0.41$, $c_{w3}=2$, $c_{v1}=7.1$ and
$c_{w1}=c_{b1}/\kappa^2+(1+c_{b2})/\sigma$, Cato et al.'s form
([Fanizza et al. (2025)](/sources/fanizza-2025.md), §2.2, Eqs. 1–5). In place
of the constant $c_{w2}=0.3$ they use the Spalart–Garbaruk correction "for
shear flows at low Reynolds numbers",
$$c_{w2}=c_{w4}+\frac{c_{w5}}{(\chi/40+1)^2},\qquad c_{w4}=0.21,\quad c_{w5}=1.5,$$
which falls from 1.71 at $\chi=0$ to 0.21 at large $\chi$ and equals 0.3 at
$\chi\approx123$ *(compiler check, not in the sources)*; negative values of
$\tilde\nu$ are handled by the negative SA model of Allmaras et al. (§2.2).
They discretize it with a high-order modal discontinuous Galerkin method
(BR2 viscous fluxes, Roe or local Lax–Friedrichs convective flux,
adjoint-consistent wall conditions and source terms) in ONERA's Aghora
solver (§2.3; see
[discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
for the nodal relative).

**Negative SA.** Basile et al. (2023) use the negative-$\tilde\nu$ model with
$\mu_t=\rho\tilde\nu f_{v1}$ for $\tilde\nu\ge0$ and $\mu_t=0$ for $\tilde\nu<0$
(§2.2, Eq. 5), the same treatment of the mean-flow equations that Li & Liu
record for SA-neg (below). Cato et al. (2023) print the full negative
branch of the variant of Crivellini et al.: for $\chi<0$ the production is
$c_{b1}\tilde\nu\lvert\Omega\rvert g_n$ with $g_n=1-1000\chi^2/(1+\chi^2)$, the
destruction becomes $-c_{w1}(\tilde\nu/d)^2$ (a source), and the diffusion
coefficient $\sigma^{-1}\nu(1+\chi)$ becomes $\sigma^{-1}\nu(1+\chi+\tfrac12\chi^2)$,
with $\nu_t=0$ in the momentum equation (§II A, Eqs. 3–4; $g_n$ page-local).
Ferrer et al. (2023) use a negative SA model in the RANS solver of
[HORSES3D](/software/horses3d.md), citing Oliver's thesis and Joshi et al.,
without printing it ([Ferrer et al. (2023)](/sources/ferrer-2023.md), §4.1).

### Discretization in an unstructured solver

Alauzet et al. (2022, §4.1–4.2) give a vertex-centred mixed finite-volume /
finite-element discretization of SA-noft2: the convection of $\rho\tilde\nu$
takes the upwind value of $\tilde\nu$ times the HLLC mass flux, which they
state is proven to preserve the maximum principle for $\tilde\nu$ (Eq. 16);
the diffusion is P1 Galerkin; the SA system is solved after the mean flow
as a separate linear system (loose coupling), differentiated with respect
to $\tilde\nu$ with $\rho$ frozen. The turbulence equation is left out of
their adjoint and goal-oriented error estimate (Remarks 5.1, 6.1; see
[mesh adaptation](/methods/mesh-adaptation.md)).

Two other discretizations appear in the sources. Cato et al. (2023, §II E)
solve the steady incompressible RANS–SA system with continuous finite
elements in FreeFEM++ (P1-bubble velocity, P1 pressure and $\tilde\nu$, "a
first-order accurate scheme"), SUPG stabilization of the advection terms
only, Newton iterations and the MUMPS direct solver; the adjoint operator
is the transpose of the discrete Jacobian. Ferrer et al. (2023) report that
the group extended entropy-stable discontinuous Galerkin schemes to the SA
equations, implemented in HORSES3D, where the implicit solvers use an
analytic Jacobian for the Navier–Stokes part and a numerical Jacobian with
colouring once SA is included (§3.5, §3.7; see
[discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)).

For discontinuous Galerkin RANS, Zhao et al. (2023b) recall two ways of
keeping the SA variable admissible: Crivellini et al. modify the source and
diffusion terms only where the working variable or the closure functions
become negative (the variant whose negative branch Cato et al. print
above), and Moro et al. use an always-positive auxiliary variable
([Zhao et al. (2023b)](/sources/zhao-2023-b.md), §1). Zhao et al. themselves
avoid the issue for the [SST model](/methods/k-omega-sst-model.md) by
solving the turbulence equations with a first-order finite-volume scheme.
On NACA 0012 at $10^\circ$ their SST pressure coefficient differs from the SA
results of Anderson et al. (SUPG finite elements) near the upper-surface
leading edge, a difference they say "might be interpreted by the
turbulence model" without testing it (§5.2).

## Variants

Li & Liu (2022) sort the modifications into three kinds (§1): scope or
numerical fixes that barely change results; modifications of production or
destruction that express non-equilibrium transport; and nonlinear
constitutive relations replacing the Boussinesq stress.

### Scope and robustness fixes

- **SA-noft2** sets $f_{t2}\equiv0$ (Aupoix & Spalart 2003, as recalled by
  Li & Liu, Eq. 7). In the compressor cascade every model differs from its
  noft2 version by less than 0.1%: $f_{t2}$ is negligible with a turbulent
  inlet above a Reynolds number of $2\times10^5$ (§3.1).
- **SA-neg** (Allmaras, Johnson & Spalart 2012) solves a modified equation
  when $\tilde\nu<0$,
  $D\tilde\nu/Dt=c_{b1}(1-c_{t3})\lvert\Omega\rvert\tilde\nu+c_{w1}(\tilde\nu/d)^2+\sigma^{-1}[\partial_j((\nu+\tilde\nu f_n)\partial_j\tilde\nu)+c_{b2}\partial_i\tilde\nu\partial_i\tilde\nu]$,
  and sets $\mu_t=0$ in the mean-flow equations (Eq. 6; $f_n$ and $c_{t3}$ not
  printed). In the well-resolved cascade it gives "exactly the same value"
  as SA (§3.1).

### Rotation and curvature corrections

These reduce the production where rotation dominates strain.

- **SA-RC** (Spalart & Shur 1997) multiplies the production by
  $$f_{r1}=(1+c_{r1})\frac{2r^*}{1+r^*}\big[1-c_{r3}\tan^{-1}(c_{r2}\hat r)\big]-c_{r1},\qquad r^*=\lvert S\rvert/\lvert\Omega^\star\rvert,$$
  $$\hat r=\frac{2\Omega^\star_{ik}S_{jk}}{D^4}\Big(\frac{DS_{ij}}{Dt}+(\epsilon_{imn}S_{jn}+\epsilon_{jmn}S_{in})\Omega_{\mathrm{rot},m}\Big),\qquad D^2=\tfrac12\big(\lvert S\rvert^2+\lvert\Omega^\star\rvert^2\big),$$
  where $\Omega^\star_{ij}=\Omega_{ij}+\epsilon_{mji}\Omega_{\mathrm{rot},m}$ is the
  rotation tensor including the frame rotation $\Omega_{\mathrm{rot}}$, and
  $\hat r$, $D$, $\Omega^\star$ are page-local names for the source's
  $\tilde r$, $D$, $\tilde\Omega$; $c_{r1}=1.0$, $c_{r2}=12.0$, $c_{r3}=1.0$
  (Li & Liu, Eqs. 8–15). The correction responds to the ratio of strain to
  rotation and to the rotation of the principal axes of strain.
- **SA-R** (Dacles-Mariani et al.) replaces the vorticity by
  $\lvert\Omega\rvert+C_{rot}\min(0,\lvert S\rvert-\lvert\Omega\rvert)$, $C_{rot}=2.0$,
  lowering production where vorticity exceeds strain (Eq. 16).
- **SA-KL** uses the Kato–Launder idea, $\sqrt{\lvert S\rvert\lvert\Omega\rvert}$ in
  place of $\lvert\Omega\rvert$ (Eq. 17).
- **SA-S** uses $\lvert S\rvert$ in place of $\lvert\Omega\rvert$, a variant Li &
  Liu say is "not mentioned in the existing references" (§2.3, Eq. 18).

SA-R and SA-KL "barely take effect where vorticity is close to strain rate,
such as in thin shear layers", and Li & Liu, citing the NASA Turbulence
Modeling Resource, call them less efficient but simpler versions of SA-RC.

Duraisamy et al. (2019) report the field inversion of Singh & Duraisamy
(2016): a spatial multiplier on the SA production, inferred from LES
skin friction on the convex wall of a curved channel alone, reproduces the
LES velocity and Reynolds stresses much better than SA and SARC, and its
trend agrees with the reduction of turbulence by convex curvature; the
comparison suggests that SARC needs improvement in the log layer
([Duraisamy et al. (2019)](/sources/duraisamy-2019.md), §5.1, Figs. 4–5;
see [field inversion and machine learning](/methods/field-inversion-machine-learning.md)).

### Helicity correction

SA-Helicity (Liu, Lu, Fang & Gao 2011, the group of Li & Liu) is built on
SA-noft2 and raises the production measure, in production and destruction
alike, where the normalized helicity is high:

$$S_{\mathrm{SA}}=\big(1+C_{h1}h^{C_{h2}}\big)\lvert\Omega\rvert+\frac{\tilde\nu}{\kappa^2d^2}f_{v2},\qquad
h=\frac{\lvert\omega_iu_i\rvert}{\lvert\Omega\rvert\,\lvert\boldsymbol u\rvert},\qquad C_{h1}=0.71,\ C_{h2}=0.6$$

([Li & Liu (2022)](/sources/li-2022.md), §2.3, Eqs. 19–22; $h$ page-local).
The stated rationale is that velocity helicity correlates with energy
backscatter in strongly rotating turbulence, which Li & Liu present as
proved in the cited work; see [energy backscatter](/definitions/energy-backscatter.md).
Since $h\ge0$ the factor is at least one, so the correction enhances
production, the opposite direction to SA-R and SA-RC.

### Quadratic constitutive relation

QCR keeps the SA equation and changes the stress. In registry form
(translated from Li & Liu's $-\rho$ convention, which leaves the
antisymmetric product unchanged and flips the isotropic term):

$$R^{\mathrm{QCR2000}}_{ij}=R_{ij}-C_{cr1}\big[O_{ik}R_{jk}+O_{jk}R_{ik}\big],\qquad
O_{ik}=\frac{2\Omega_{ik}}{\sqrt{\partial_nu_m\,\partial_nu_m}},\qquad C_{cr1}=0.3,$$

$$R^{\mathrm{QCR2013}}_{ij}=R^{\mathrm{QCR2000}}_{ij}+C_{cr2}\,\nu_t\lvert S^d\rvert\,\delta_{ij},\qquad C_{cr2}=2.5,$$

with $R_{ij}$ the Boussinesq stress
(Spalart 2000 and Mani et al. 2013, as recalled by Li & Liu, Eqs. 23–27).
The QCR2000 correction adds no trace, since $O$ is antisymmetric and $R$
symmetric *(compiler check, not in the sources: the added trace is
$-2C_{cr1}O_{ik}R_{ik}=0$)*, so SA-QCR2000 is traceless like SA; the QCR2013
isotropic term partly supplies the missing $\tfrac23k\delta_{ij}$ (§4.2).
Alauzet et al. (2022) write the SA-noft2-QCR2000 stress as
$\mu\tau+\mu_t(\tau-\tau_{\mathrm{QCR}})$, with $\tau$ twice the deviatoric
strain and $\tau_{\mathrm{QCR}}$ "given in" Spalart (2000), not reproduced
(§2.3, Eq. 10).

### Field-inversion correction of the production

Yan et al. (2022) multiply the SA production by a spatial field
$\beta(\boldsymbol x)$, $c_{b1}S_{\mathrm{SA}}\tilde\nu\to\beta\,c_{b1}S_{\mathrm{SA}}\tilde\nu$
($\beta=1$ recovers SA), infer $\beta$ by Bayesian
[field inversion](/methods/field-inversion-machine-learning.md) from scarce
data (lift only, or lift and drag, or mean-velocity profiles) and learn it
with a neural network embedded in the solver ([Yan et al. (2022)](/sources/yan-2022.md),
§2.1, Eq. 5, §2.3). On three separated flows:

- **GLC305 airfoil with horn ice 944**, $M=0.12$, $Re=3.5\times10^6$:
  baseline SA gives $C_L=0.393$ and $0.495$ against the measured 0.489 and
  0.669 at $4^\circ$ and $6^\circ$; at $6^\circ$ its separation bubble covers
  the whole airfoil, the inverted one about half the chord (§3.3.1, Table 3,
  Fig. 25). The learned model cuts the $C_L$ error to $-7.0\%$ and
  $-5.5\%$ (Table 4) and generalizes over $0^\circ$–$7^\circ$ in the linear
  range, less well beyond $6^\circ$ (Fig. 33).
- **S809 airfoil near stall**, $M=0.10$, $Re=2\times10^6$: inversion on $C_L$
  alone suppresses the production mainly in the strong adverse-pressure-gradient
  region near the boundary layer, enlarges the separation and improves the
  unobserved $C_p$ (§3.1.1, Figs. 6–7).
- **Parametrized periodic hills** at $Re_b=5600$ (the Xiao et al. family,
  not the configuration of the [periodic-hill](/benchmarks/periodic-hill.md)
  page's main case): see the field-inversion page.

In all cases the regularized correction both lowers the production at the
start of the separating shear layer and raises it downstream, in the region
where production greatly exceeds dissipation (§3.2.1, §3.3.1). This
continues the curved-channel field inversion recalled by Duraisamy et al.
(2019) below.

**Comparison of correction sites.** Cato et al. (2023) compare the
production multiplier with five other space-dependent corrections of the
negative SA model, optimized by adjoint-based data assimilation against
dense DNS mean velocity: a momentum forcing, a conservative traceless
tensor forcing, an additive source and a source proportional to $\tilde\nu$
in the $\tilde\nu$-equation, and a multiplier of $\nu_t$ in the momentum
equation. They write the production correction as $(1+\beta)P$, with prior
zero, where Yan et al. and Singh & Duraisamy write $\beta P$ with prior one.
On a converging–diverging channel, the periodic hill at $Re_b=2800$ and a
square cylinder at $Re=22\,000$, the proportional source "performed almost
as well as the source terms in the momentum equations", the production
multiplier and the additive source are intermediate, and the
eddy-viscosity multiplier is poorest and fails on the square cylinder;
corrections placed in the SA equation improve "numerical robustness
regardless of the test case" compared with the eddy-viscosity multiplier
(§II B, Tables I–III, §VII). Error tables, non-uniqueness and over-fitting
of $\nu_t$ are on the
[model-form uncertainty page](/definitions/model-form-uncertainty.md).

**Compressible, high-order data assimilation.** Fanizza et al. (2025)
repeat four of these corrections for the compressible model on the modal
DG discretization above: a momentum and energy source, a multiplier
$(1+\chi_h)$ of $\mu_t$ (page-local $\chi_h$, kept positive by a smooth
limiter), a source $\rho\tilde\nu f_{\tilde\nu}$ in the $\tilde\nu$-equation
(page-local $f_{\tilde\nu}$, Cato et al.'s proportional source) and a
production multiplier $(1+\beta)$ with prior zero, inferred by L-BFGS with
discrete-adjoint gradients computed by flexible inner–outer GMRES and
algorithmic differentiation (§3.3–3.4). On the square cylinder at
$Re=22\,000$ the ranking is that of Cato et al., the eddy-viscosity
multiplier stalling from the first iterations (§4.2, Figs. 7–8). On a
supersonic shock/boundary-layer interaction ($M_\infty=2.28$, $9.5^\circ$
deflection) with the Spalart–Garbaruk model, only the momentum source
corrects the near-wall flow, $C_f$ and wall pressure with dense velocity
data, and with wall-pressure data alone the three corrections of the SA
equation and of $\mu_t$ make $C_f$ worse than the baseline (§4.3, Tables
1–2; numbers on the [Boussinesq page](/definitions/boussinesq-hypothesis.md);
see [field inversion](/methods/field-inversion-machine-learning.md) and
[square-cylinder flow](/benchmarks/square-cylinder-flow.md)). The adjoint
gradient of the eddy-viscosity multiplier is checked against finite
differences (App. A).

### SA as the host of detached-eddy simulation

SA is the RANS closure of the zonal
[detached-eddy simulations](/methods/detached-eddy-simulation.md) of François
et al. (2022) and Basile et al. (2023). In DES zones the wall distance of the
destruction term is capped by a grid length; in the zonal form of Basile et
al. the near-wall functions take their far-wall values, $f_{v1}=1$,
$f_{v2}=0$, $f_w=1$, in LES mode (§2.2, Eqs. 6–7), and the shielding function
of François et al.'s mode 2 is computed from $\tilde\nu$ rather than from
$\nu_t$ ([François et al. (2022)](/sources/francois-2022.md), §3.1).
Carlsson et al. (2023) use SA in DDES with $C_{\mathrm{DES}}=0.65$, which
reproduces the spectra of decaying isotropic turbulence in LES mode with a
low-dissipation scheme, and in SA-DDES of a supersonic base flow with the
shear-layer-adapted length; in channel flow SA-IDDES gives results "very
similar" to SST-IDDES (not shown)
([Carlsson et al. (2023)](/sources/carlsson-2023.md), §3, §4.2–4.4).

### SA with wall functions on immersed-boundary Cartesian grids

Constant et al. (2024) close steady RANS on octree Cartesian grids with the
standard 1992 SA model ($\nu_t=\tilde\nu f_{v1}$, $c_{v1}=7.1$) and an
[immersed boundary](/methods/immersed-boundary-method.md) whose forcing
points carry a wall function
([Constant et al. (2024)](/sources/constant-2024.md), §2.1 Eq. 2, §3.2;
HAL author manuscript). At each forcing point at wall distance $d_A$
(page-local), the eddy viscosity $\nu_t=\kappa u_\tau d_AD$ with
$D=1-\exp(-y_A^+/19)$ and $\kappa=0.41$, "valid in the log layer and down to
the wall", is inverted for the working variable through the quartic

$$\tilde\nu^4-\kappa u_\tau d_AD\,\tilde\nu^3-\kappa u_\tau d_AD\,\nu^3c_{v1}^3=0$$

(Eq. 8, solved by Ferrari's method), which is $\tilde\nu f_{v1}=\nu_t$
written out *(compiler check, not in the sources)*. The friction velocity
comes from Musker's equilibrium wall law at an image point above the
forcing points. Moving the forcing region below an a-priori modelling height,
and adapting that height where the boundary layer is thin at the leading
edge, removes the spurious near-wall oscillations of the coupling and,
with a higher-order wall-pressure reconstruction, cuts the near-field drag
error on NACA 0012 at $15^\circ$ ($M=0.15$, $Re=6\times10^6$) from 94% to 17%
against a body-fitted wall-resolved reference, and on the NASA CRM
high-lift configuration at $17.05^\circ$ from 9.1% to 1.5% against a body-fitted LAVA solution (Tables 3, 9; see
the immersed-boundary page and
[NASA CRM high-lift configuration](/benchmarks/nasa-crm-high-lift.md)). The
remaining error near stall is attributed to the equilibrium wall model at
the leading edge (§6.1).

## Evidence

### Compressor corner separation and a transonic rotor

Li & Liu (2022) run steady RANS with a modified CFL3D on the PVD linear
compressor cascade (chord Reynolds number 230,000, zero incidence, about 1.5
million points in half span, $y^+\approx0.7$) and on NASA Rotor 67 (about 4.75
million points, $y^+\approx0.8$), against experiment only:

- SA "largely overpredicts" the corner separation, with a peak eddy-viscosity
  ratio $\mu_t/\mu$ above 1,100. SA-R, SA-RC, SA-KL and SA-S barely change it;
  SA-RC is worse than SA near mid-span (Table 3, Figs. 3–8).
- SA-Helicity is the most accurate model and has the lowest peak
  $\mu_t/\mu$, about 400. The authors explain the apparent paradox (more
  production, less eddy viscosity) by nonlinearity: enhanced production
  mixes passage and separated flow, suppresses the separation and so avoids
  further eddy-viscosity production. They conclude that the failure of SA
  is the overprediction of $\mu_t$ and that "just decreasing the production
  term (SA-R) is not effective" in large-scale vortices (§3.2).
- SA-KL and SA-S do nothing because $\lvert\Omega\rvert$ exceeds $\lvert S\rvert$
  only moderately in the corner vortex, unlike a tip-leakage vortex (§3.2).
- QCR2000 and QCR2013 improve on SA but still overpredict the separation
  and its loss. Blends of a production variant with QCR inherit both
  behaviours; the anisotropy invariants of the QCR2013 blends barely differ,
  and the authors conclude that the two corrections superpose "with little
  interference" and that "the performance of a blending model mainly
  depends on the EVM utilized" (§4.1–4.2, Figs. 10–15). SA-Helicity-QCR2013
  is the best blend.
- On Rotor 67, SA underestimates the stable operating range by about 14%
  and SA-QCR2013 by about 7.9%, while SA-Helicity and SA-Helicity-QCR2013
  predict the stall point "very accurately"; all models overpredict the
  adiabatic efficiency, the helicity correction lowering it by about 0.5%
  (§5, Figs. 17–19).

Liu et al. (2024) cite this work among the rotation–curvature, QCR and
helicity corrections that linear eddy-viscosity models (SA and SST) need
for compressor corner flows, and take the opposite route of a
[Reynolds-stress model](/methods/reynolds-stress-model.md)
([Liu et al. (2024)](/sources/liu-2024.md), Introduction).

### Mesh-converged RANS of a transonic rotor

Alauzet et al. (2022) run SA-noft2-QCR2000 on NASA Rotor 37 (36 blades,
17 188.7 rpm, cold blade geometry, 23 operating points) on anisotropically
adapted tetrahedral meshes up to about 11 million vertices, after mesh
convergence of mass flow, total-pressure and total-temperature ratios to
1%, and compare with structured [elsA](/software/elsa.md) RANS with standard
SA on 3–32 million cells (§8.2). With discretization error removed, the
total-pressure and total-temperature characteristics lie above the
experimental data, "not in accordance with the literature", which generally
lies below; the efficiency is "a lot higher" than literature and elsA
results, below experiment at high mass flow and matching it near stall. The
authors attribute the first to the cold geometry and the second to the
under-resolution of non-adapted meshes, without testing either (§8.2.4,
Table 2). Transition is not modelled, because LES shows transition almost
at the leading edge (§8.2). They propose comparing SA and SST on such
meshes as future work (§9).

### Aircraft and other uses

- In the AIAA Third High-Lift Prediction Workshop most of the 79 submitted
  data sets were steady RANS with SA or SST variants; they cluster in the
  linear lift range and scatter near maximum lift. An OpenFOAM SA reference
  on 109 million cells cost about $60\times10^3$ core-hours, comparable to the
  medium-grid wall-modelled LES of Goc et al.
  ([Goc et al. (2021)](/sources/goc-2021.md), §1, Fig. 1, §4; see
  [JAXA Standard Model](/benchmarks/jaxa-standard-model.md)).
- HORSES3D runs negative-SA RANS of the NASA Common Research Model at
  $M=0.85$, $Re=5\times10^6$, $2.3^\circ$ incidence on a third-order ($N=2$)
  hexahedral mesh with split-form inviscid fluxes; only surface pressure
  contours are shown ([Ferrer et al. (2023)](/sources/ferrer-2023.md), §4.1,
  Fig. 6).
- FLEXI initialises scale-resolving runs with an SA RANS solution obtained
  by pseudo-time stepping ([Krais et al. (2021)](/sources/krais-2021.md),
  §2.2.3; see [FLEXI](/software/flexi.md)).
- The RSC-SGS hybrid RANS/LES method reduces the mean-strain stress of SA (or
  of a van Driest mixing length) by the averaged resolved stress, as
  recalled by Haering et al. (2022), who class it as effectively zonal
  ([Haering et al. (2022)](/sources/haering-2022.md), §I; see
  [hybrid RANS/LES](/definitions/hybrid-rans-les.md)).
- SA-based local-correlation transition models (Medida & Baeder; Piotrowski
  & Zingg; Bouchard et al.) and the algebraic transition model of
  Cakmakcioglu et al. built on SA at constant free-stream turbulence are
  listed by Menter et al. (2022, §1); see
  [local-correlation-based transition models](/methods/local-correlation-based-transition-model.md).
- Huang et al. (2022) recall that standard one- and two-equation models
  (SA, SST), built on subsonic adiabatic data, predict the heat flux of
  hypersonic zero-pressure-gradient boundary layers less accurately than
  algebraic models with compressibility corrections (Rumsey 2010; Gnoffo et
  al. 2013), and find their cold-wall Mach 11 DNS within 1.9% ($\tau_w$) and
  1.7% (wall heat flux) of a Baldwin–Lomax RANS
  ([Huang et al. (2022)](/sources/huang-2022.md), §1, App. A.2); see
  [Baldwin–Lomax model](/methods/baldwin-lomax-model.md).
- **Transonic buffet.** In the compilation of URANS predictions of the
  OAT15A buffet at $\alpha=3.5^\circ$ by Petrocchi & Barakos (2024), SA mostly
  gives no shock oscillation, while some variants (SALSA, Edwards–Chandra
  forms with compressibility correction) and Reynolds-stress models do,
  at Strouhal numbers of about 0.066–0.074
  ([Petrocchi & Barakos (2024)](/sources/petrocchi-2024.md), App. A, Table
  A.4; a compilation of other authors' results; see
  [PANS](/methods/partially-averaged-navier-stokes.md)).
- **Lattice Boltzmann.** SA, already validated in the lattice Boltzmann
  solver [ProLB](/software/prolb.md), is the reference against which
  Mozaffari et al. (2024) check their SST implementation on the NACA 23012
  at $Re_c=1.88\times10^6$: the two give close eddy-viscosity fields and
  lift coefficients of 0.12, 0.79, 1.175 (SA) against 0.12, 0.79, 1.07
  measured at $0^\circ$, $6.2^\circ$, $9.3^\circ$; both under-predict $C_p$
  near the leading edge, which the authors attribute to the missing
  transition, and one extra refinement level reduces the $C_p$ error at
  $9.3^\circ$ by "almost 50%"
  ([Mozaffari et al. (2024)](/sources/mozaffari-2024.md), §3.1, Table 1,
  Figs. 4–8; HAL accepted manuscript).
- **Host of DDES.** Wang et al. (2024) run SA-based delayed DES of the 30P30N
  three-element high-lift airfoil ($M_\infty=0.17$, $Re=1.7\times10^6$,
  $\alpha=5.5^\circ$, about 27 million cells) with a sixth-order upwind
  scheme, without printing the model
  ([Wang et al. (2024)](/sources/wang-2024.md), §4; see
  [detached-eddy simulation](/methods/detached-eddy-simulation.md)).

## Qualifications

- Li & Liu's ranking rests on one cascade and one rotor, against experiment
  only, with grid adequacy asserted by citation; no LES or DNS reference is
  used (§2.1, §3).
- The helicity–backscatter link is the authors' group's own result, stated
  as proved; the mechanism by which more production yields less eddy
  viscosity is argued, not demonstrated by a dedicated test.
- Li & Liu describe the purpose of QCR2000 once as "more accurate estimation
  of the turbulent stresses" (§1) and once as "of the turbulent viscosity"
  (§4.2); their Eqs. 23–25 change the stress–strain relation and leave
  $\mu_t$ unchanged *(compiler check, not in the sources)*.
- Li & Liu call $h$ a "helicity density", while their Eq. 20 defines a
  normalized, dimensionless relative helicity.
- Alauzet et al. (2022) print $c_{w1}=c_{b1}/\kappa+(1+c_{b2})/\sigma$ (§2.3),
  while their own equation, with Basile et al.'s log-layer solution, requires
  $c_{b1}/\kappa^2$ (Constants above, compiler check); Cato et al. (2023)
  print $c_{b1}/\kappa^2$ with the same constants (§II A), so Alauzet et al.'s
  form is a printed slip, not a variant. Their source vector
  (Eq. 13) prints the destruction $c_{w1}f_w\rho(\tilde\nu/d)^2$ with a plus
  sign, against the minus sign of their Eq. 9; and they label the
  conservative diffusion term "dissipation" and the $c_{b2}$ term "diffusion".
- Yan et al. (2022) print the destruction as $c_{w1}f_w[\tilde\nu/d]$, without
  the square; by their own Eq. 2 the destruction must have the dimensions of
  the production $c_{b1}S_{\mathrm{SA}}\tilde\nu$, which $(\tilde\nu/d)^2$ has
  *(compiler check, not in the sources)*.
- Yan et al.'s baseline production is built on the mean strain-rate norm,
  which in Li & Liu's taxonomy is the SA-S variant that Li & Liu say is "not
  mentioned in the existing references". Yan et al. call it the SA model and
  give no reason for the strain; whether this is a notational choice cannot
  be settled from the paper.

# Citations

- [Li & Liu (2022)](/sources/li-2022.md) — §1, §2.3 Eqs. 1–27, 33–34, §3.1–3.2, §4.1–4.2, §5, Table 3.
- [Duraisamy et al. (2019)](/sources/duraisamy-2019.md) — §5.1, Figs. 4–5.
- [Goc et al. (2021)](/sources/goc-2021.md) — §1 Fig. 1, §4.
- [Haering et al. (2022)](/sources/haering-2022.md) — §I.
- [Krais et al. (2021)](/sources/krais-2021.md) — §2.2.3.
- [Menter et al. (2022)](/sources/menter-2022.md) — §1.
- [Alauzet et al. (2022)](/sources/alauzet-2022.md) — §2.1, §2.3 Eqs. 8–10, 13, §4.1–4.2 Eq. 16, Remarks 5.1, 6.1, §8.2, §8.2.4 Table 2, §9.
- [Yan et al. (2022)](/sources/yan-2022.md) — §2.1 Eqs. 2–5, §2.3, §3.1.1 Figs. 6–7, §3.2.1, §3.3 Tables 3–4, Figs. 25, 33.
- [Basile et al. (2023)](/sources/basile-2023.md) — §2.2, Eqs. 5–7.
- [François et al. (2022)](/sources/francois-2022.md) — §3.1, §3.5.
- [Huang et al. (2022)](/sources/huang-2022.md) — §1, App. A.2.
- [Cato et al. (2023)](/sources/cato-2023.md) — §II A Eqs. 2–4, §II B Eq. 5, §II E, Tables I–III, §VII (HAL v2).
- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — §3.5, §3.7, §4.1 Fig. 6 (arXiv v1).
- [Carlsson et al. (2023)](/sources/carlsson-2023.md) — §3, §4.2–4.4.
- [Zhao et al. (2023b)](/sources/zhao-2023-b.md) — §1, §5.2.
- [Constant et al. (2024)](/sources/constant-2024.md) — §2.1 Eq. 2, §3.2 Eq. 8, §6.1 Table 3, §6.3 Table 9 (HAL author manuscript).
- [Liu et al. (2024)](/sources/liu-2024.md) — Introduction.
- [Petrocchi & Barakos (2024)](/sources/petrocchi-2024.md) — App. A, Table A.4.
- [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) — §3.1, Table 1, Figs. 4–8 (HAL accepted manuscript).
- [Wang et al. (2024)](/sources/wang-2024.md) — §4.
- [Fanizza et al. (2025)](/sources/fanizza-2025.md) — §2.2 Eqs. 1–5, §2.3, §3.3–3.4, §4.2 Figs. 7–8, §4.3 Tables 1–2, App. A.
