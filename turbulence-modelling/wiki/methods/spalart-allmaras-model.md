---
type: Method
title: "Spalart–Allmaras model and its corrections"
description: "The one-equation eddy-viscosity RANS model transporting the working variable ν̃: its printed forms and constants, negative, rotation–curvature, helicity and quadratic-constitutive-relation variants, positivity and entropy stability at high order, data-driven corrections, its role as host of detached-eddy simulation, and evidence from turbomachinery and airfoils."
status: established
aliases: [SA model, Spalart-Allmaras, SA-noft2, SA-neg, negative SA, SA-noft2-QCR2000, β-augmented SA, SA-RC, SARC, SA-R, SA-Helicity, SA-QCR, QCR2000, QCR2013, quadratic constitutive relation]
tags: [rans, eddy-viscosity, turbomachinery, separated-flow, field-inversion]
timestamp: 2026-10-28T07:10:00Z
---

# Spalart–Allmaras model and its corrections

The Spalart–Allmaras (SA) model is a one-equation RANS closure: it transports
a working variable $\tilde\nu$ from which the eddy viscosity of the
[Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md) is computed,
$\nu_t=\tilde\nu f_{v1}$, and it carries no turbulent kinetic energy. With
SST variants it makes up most of the high-lift workshop RANS submissions
reported by Goc et al. (2021); it is the host model of the field-inversion corrections of
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

Tang et al. (2022) print the incompressible equation with the constants of
Alauzet et al., $c_{w1}=c_{b1}/\kappa^2+(1+c_{b2})/\sigma$, no $f_{t2}$ and no
trip, but build the modified vorticity on the strain magnitude
$\lvert S\rvert=\sqrt{2S_{ij}S_{ij}}$, as Yan et al. do, while citing
Spalart & Allmaras for the model
([Tang et al. (2022)](/sources/tang-2022.md), §2.1, Eq. 2). They use it as
the near-wall branch of a zonal hybrid RANS/LES in which one transported
$\tilde\nu$ blends the SA terms with those of a one-equation subgrid model
through a wall-distance function $F$, and switch the damping off in the LES
region through $f_{v1}=\chi^3/(\chi^3+F^{20}c_{v1}^3)$ (Eqs. 6–9; see
[hybrid RANS/LES](/definitions/hybrid-rans-les.md)).

Shan et al. (2023) print the incompressible model with $f_{t2}$ retained,
$S_{\mathrm{SA}}$ built on the vorticity magnitude
$\lvert\Omega\rvert=\sqrt{2\Omega_{ij}\Omega_{ij}}$, the $f_{v2}$, $f_w$, $g$ and $r$ of
Li & Liu (without the cap on $r$), and the constants $\sigma=2/3$,
$c_{b1}=0.1355$, $c_{b2}=0.622$, $\kappa=0.41$, $c_{w2}=0.3$, $c_{w3}=2$,
$c_{v1}=7.1$, $c_{t3}=1.2$, $c_{t4}=0.5$ and
$c_{w1}=c_{b1}/\kappa^2+(1+c_{b2})/\sigma$
([Shan et al. (2023)](/sources/shan-2023.md), App. A, Eqs. A1–A7). Their
calibration of the nine free constants is below.

Four further printed forms:

- **Compressible, with $f_{t2}$ and a density-gradient term.** Huang et al.
  (2022b) transport $\rho\tilde\nu$ with the SA functions above,
  $f_{t2}=c_{t3}\exp(-c_{t4}\chi^2)$ retained with $c_{t3}=1.2$, $c_{t4}=0.5$,
  the constants of Alauzet et al., $c_{w1}=c_{b1}/\kappa^2+(1+c_{b2})/\sigma$
  and $r=\min(\cdot,10)$; their diffusion flux has the coefficient
  $(\mu+\mu_t)/\sigma$ with $\mu_t=\rho\tilde\nu f_{v1}$, and their diffusion
  source carries, besides the $c_{b2}$ term, a density-gradient term
  $-\sigma^{-1}(\mu+\mu_t)\rho^{-1}\nabla\rho\cdot\nabla\tilde\nu$. The wall
  distance comes from a time-dependent eikonal solve and the far-field value
  is $\rho\tilde\nu_\infty=(3$–$5)\mu_\infty$
  ([Huang et al. (2022b)](/sources/huang-2022-d.md), §2.1, Eqs. 3–6; the
  source writes $\hat\upsilon$ for $\tilde\nu$).
- **Compressible, without the density-gradient term.** Lodares et al.
  (2022) transport $\rho\tilde\nu$ with the diffusion
  $\sigma^{-1}\nabla\cdot\big(\rho(\nu+\tilde\nu)\nabla\tilde\nu\big)$, set
  $f_{t2}=0$ "as in many implementations", and neglect the additional
  compressible diffusive term $-\sigma^{-1}(\nu+\tilde\nu)\nabla\rho\cdot\nabla\tilde\nu$,
  as Ansys Fluent does; their modified vorticity is
  $\lvert\Omega\rvert+\bar S_{\mathrm{SA}}$ with
  $\bar S_{\mathrm{SA}}=\tilde\nu f_{v2}/(\kappa^2d^2)$ (page-local) when
  $\bar S_{\mathrm{SA}}\ge-c_2\lvert\Omega\rvert$, and the limited form
  $\lvert\Omega\rvert+\lvert\Omega\rvert(c_2^2\lvert\Omega\rvert+c_3\bar S_{\mathrm{SA}})/[(c_3-2c_2)\lvert\Omega\rvert-\bar S_{\mathrm{SA}}]$
  otherwise; $\mu_t=\max(\rho\tilde\nu,0)f_{v1}$, the source is set to zero
  where $d=0$ (wall nodes of Gauss–Lobatto elements), and "a usual value"
  of $\tilde\nu_\infty$ is $3\nu_\infty$. Only $\sigma=2/3$ and $c_{b2}=0.622$
  are printed, because they enter the stability proof below
  ([Lodares et al. (2022)](/sources/lodares-2022.md), §2, Eqs. 13–17, §4.5).
- **Incompressible, as the RANS branch of DES.** Pan & Zhang (2023) print
  the "default values" $c_{b1}=0.1355$, $\sigma=0.6667$, $c_{b2}=0.622$,
  $\kappa=0.41$, $c_{w1}=2.5093$, $c_{w2}=0.3$, $c_{w3}=2.0$, $c_{v1}=7.1$ of
  ANSYS Fluent, with no relation for $c_{w1}$, no $f_{t2}$ and no trip; their
  modified vorticity is built, like Yan et al.'s and Tang et al.'s, on the
  strain magnitude $\lvert\bar S\rvert=\sqrt{2\bar S_{ij}\bar S_{ij}}$, while
  the text calls it "the magnitude of modified vorticity"
  ([Pan & Zhang (2023)](/sources/pan-2023.md), §II.B, Eqs. 3–6; see
  Qualifications).
- **Incompressible, in the normalized variable $\chi$.** Husson et al.
  (2024) transport $\chi=\tilde\nu/\nu$ directly,
  $$\partial_t\chi+\boldsymbol u\cdot\nabla\chi=c_{b1}S_{\mathrm{SA}}\chi-c_{w1}f_w\nu\Big(\frac{\chi}{\ell}\Big)^2+\frac\nu\sigma\Big[(1+\chi)\nabla^2\chi+(1+c_{b2})\lvert\nabla\chi\rvert^2\Big],$$
  with $\ell$ the length scale of the destruction ($\ell=d$ in RANS; the
  hybrid choice is on the [DES page](/methods/detached-eddy-simulation.md)),
  $S_{\mathrm{SA}}$ built on the vorticity magnitude, $r=\min(\cdot,10)$,
  $c_{b1}=0.1355$, $\sigma=2/3$, $c_{b2}=0.622$, $\kappa=0.41$, $c_{v1}=7.1$
  and $c_{w1}=c_{b1}/\kappa^2+(1+c_{b2})/\sigma$; $c_{w2}$ and $c_{w3}$ are
  not printed. They state that $f_{v1}$ "ensures a linear behavior
  $\chi=\kappa y^+$ from the log-layer to the wall", as Basile et al. state
  for $\tilde\nu$ ([Husson et al. (2024)](/sources/husson-2024.md), §2.2,
  Eqs. 18–23). The equation is solved by finite differences on the lattice
  of a lattice Boltzmann solver, its eddy viscosity resetting the
  relaxation time (see [lattice Boltzmann methods](/methods/lattice-boltzmann-method.md)
  and [ProLB](/software/prolb.md)). At the forcing nodes of their immersed
  boundary they impose $\chi=\kappa y^+$ and, below a cut-off distance $y_c$
  where the SA wall law is linearized, replace $f_{v1}$ by
  $r_{\mathrm{lin}}(\chi r_{\mathrm{lin}})^3/[c_{v1}^3+(\chi r_{\mathrm{lin}})^3]$
  with $r_{\mathrm{lin}}=y_c/d$ (page-local), which keeps the momentum balance
  with a constant eddy viscosity there (§3.2, Eqs. 38–39, 42; see
  [RANS wall functions](/methods/rans-wall-function.md)).

Two printed forms from detached-eddy applications, set beside Li & Liu's
baseline:

- **Original model with $f_{t2}$, constants by reference.** Li et al.
  (2024b) print exactly the structure of Li & Liu's baseline above: the
  $(1-f_{t2})$ production, the $[c_{w1}f_w-c_{b1}f_{t2}/\kappa^2]$ destruction,
  the diffusion $\sigma^{-1}[\partial_j((\nu+\tilde\nu)\partial_j\tilde\nu)+c_{b2}\partial_i\tilde\nu\partial_i\tilde\nu]$,
  $S_{\mathrm{SA}}$ built on $\lvert\Omega\rvert=\sqrt{2\Omega_{ij}\Omega_{ij}}$,
  $f_{v2}=1-\chi/(1+\chi f_{v1})$, $f_{t2}=c_{t3}\exp(-c_{t4}\chi^2)$ and
  $r=\min(\cdot,10)$, without the trip term; no constant is printed ("can
  be found in Ref. 36", Spalart & Allmaras 1992) and the working variable
  is written with a hat ([Li et al. (2024b)](/sources/li-2024-f.md), §II.B.1,
  Eqs. 3a–3b).
- **Production on the unmodified strain norm, diffusion without molecular
  viscosity.** Zhang et al. (2024) print the transport of the working
  variable, which they write without a tilde and call the "kinematic eddy
  viscosity", as
  $$\frac{D\tilde\nu}{Dt}=c_{b1}S\tilde\nu+\frac1\sigma\Big[\nabla\cdot(\tilde\nu\nabla\tilde\nu)+c_{b2}(\nabla\tilde\nu)^2\Big]-c_{w1}f_w\Big(\frac{\tilde\nu}{d}\Big)^2,\qquad r=\frac{\tilde\nu}{S\kappa^2d^2},$$
  with $S$ "the scalar norm of the deformation tensor" and no modified
  vorticity, no $f_{t2}$ and no trip, and with the constants
  $c_{b1}=0.1355$, $c_{b2}=0.622$, $\kappa=0.41$ ($c_{w1}$, $\sigma$ and the form
  of $f_w$ not printed); the molecular viscosity, present in the diffusion
  of Li & Liu's and Li et al.'s forms, does not appear, and the source
  prints the first diffusion term with a dot inside the gradient
  ([Zhang et al. (2024)](/sources/zhang-2024.md), §2.3, Eqs. 1–2). The page
  records it as printed; in their DDES the molecular viscosity appears in
  the shielding argument $r_d$, "the DDES method adds the molecular
  viscosity" (§2.3, Eqs. 3–4; on the [DES page](/methods/detached-eddy-simulation.md)).

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
Lodares et al. (2022) use "a variation of the standard negative model":
for $\tilde\nu<0$ the source is $c_{b1}(1-c_{t3})\lvert\Omega\rvert\tilde\nu+c_{w1}(\tilde\nu/d)^2$
and the diffusion coefficient is clipped,
$\max(\nu+f_n\tilde\nu,0)$, "to strictly ensure positivity of the diffusion
coefficient", the clipping being the departure from SA-neg (§2, Eqs.
16–17; $c_{n1}$, $c_{t3}$ "usual values"). Huang et al. (2022b) reach a
non-negative $\tilde\nu$ without any negative branch (below).

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

Elzaabalawy et al. (2023) note that high-order DG RANS work has focused on
SA because it is simpler than two-equation models and has no blending
functions that reduce the smoothness of the solution, and cite the
devices used: an algebraic modification against negative eddy
viscosity (Nguyen, Persson & Peraire), artificial dissipation against
oscillations (Oliver & Darmofal, and similarly Crivellini et al.), wall
modelling by function enrichment for an explicit SA with operator
splitting (Krank et al.), a modification against negative viscosity in an
HDG method (Moro et al.), the negative model of Allmaras et al. for coarse
meshes, and an HDG implementation for an exactly divergence-free
incompressible formulation (Peters & Evans, printed "Peter et al.")
([Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md), §1). They
propose a "negative $k$-$kl$" model on the same pattern (§7; see the
[Wilcox $k$-$\omega$ page](/methods/k-omega-model.md)). Ghidoni et al.
(2026) cite Crivellini et al.'s DG implementation among the model
modifications that improve robustness
([Ghidoni et al. (2026)](/sources/ghidoni-2026.md), §1, ref. [6]).

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

### Positivity and stability at high order

Three sources add devices for the SA variable in high-order
discretizations, each a different answer to the oscillations that a
high-order polynomial of $\tilde\nu$ develops at the under-resolved edge of
the boundary layer.

The need was stated early. The first High-Order CFD Workshop, whose RANS
cases (the RAE 2822, the 30P-30N multi-element airfoil, the DPW III wing)
list SA first among the recommended models, beside the Wilcox $k$-$\omega$
model (and, for the RAE 2822, an explicit algebraic Reynolds-stress model),
concluded that high-order methods "are still
not as robust as low-order ones" in converging RANS to a steady state, a
difficulty its organizers "believe" related to the non-smoothness
introduced in the turbulence models and met with ad hoc fixes, so that
"smooth turbulence models are needed"
([Wang et al. (2013)](/sources/wang-2013.md), §4.8, §4.11–4.12,
§6, conclusion 4).

**An entropy for the SA equation.** Lodares et al. (2022) build an
entropy-stable discontinuous Galerkin spectral element discretization of
the compressible RANS–SA system. They add to the Navier–Stokes entropy the
SA "energy" $\mathcal E_{\mathrm{SA}}=\tfrac12\rho\tilde\nu^2$, whose entropy variables
$\boldsymbol W_{\mathrm{SA}}=(-\tfrac12\tilde\nu^2,0,0,0,0,\tilde\nu)$ (page-local
names, as on the entropy-conservation page) vanish where the Navier–Stokes
ones do not, so the analysis splits into the known Navier–Stokes part and an
independent SA part. Its dissipation is

$$\mathcal D_{\mathrm{SA}}=\big\langle\rho\tilde\nu(D-P)\big\rangle+\Big\langle\frac\rho\sigma(\hat\sigma-c_{b2}\tilde\nu)\lvert\nabla\tilde\nu\rvert^2\Big\rangle\ \ge\ \big\langle\rho\tilde\nu(D-P)\big\rangle,$$

with $\langle\cdot\rangle$ here the domain integral, $P$, $D$ the SA
production and destruction and $\hat\sigma$ the diffusion coefficient
($\nu+\tilde\nu$, or the clipped negative-branch value), valid if
$c_{b2}\le1$ and $\hat\sigma\ge0$; entropy may grow only where production
exceeds destruction, and for $\tilde\nu<0$ the negative-branch source makes
$\tilde\nu(D-P)\ge0$ (§3.2, Eqs. 38–50). Discretely, any Navier–Stokes
two-point flux extends to SA by the component
$\widehat{\rho U}\{\!\{\tilde\nu\}\!\}$, which satisfies Tadmor's condition for
the SA entropy whatever the momentum average, and the interface flux
$F_{\rho\tilde\nu}^*=F_\rho^*\{\!\{\tilde\nu\}\!\}-\tfrac12\lambda_\nu\lvert F_\rho^*\rvert[\![\tilde\nu]\!]$
is entropy conserving for $\lambda_\nu=0$ and stable for $\lambda_\nu=1$
($\widehat{\rho U}$ the two-point mass flux, $F^*_\rho$ the mass component of
the interface flux, $\lambda_\nu$ and $[\![\cdot]\!]$ the toggle and jump,
page-local; §4.3–4.4, Eqs. 68, 74, §5.1.2, Eqs. 87–89). On random initial data
at $\mu=10^{-8}$, $N=10$, the standard DG scheme diverges while the split
forms stay stable with zero entropy remainder (§7.2). Details are on the
[entropy-conservation page](/properties/entropy-conservation.md).

**Exponential decay of $\rho\tilde\nu$.** Huang et al. (2022b) attribute the
negative eddy viscosity of their fourth-order finite-volume SA solutions to
Gibbs oscillations where the grid is too coarse, typically the outer edge
of the boundary layer (§2.5). Near the minimum of $\tilde\nu$, with diffusion
and $O(h)$ terms neglected and the coefficient frozen, the equation reduces
to $\partial_t\ln(\rho\tilde\nu)\approx R_0$, with a rate $R_0$ that is negative
"usually" when negative values appear, so $\rho\tilde\nu$ decays
exponentially and stays positive (Eqs. 53–57). Their exponential decay
procedure acts on the residual $R$ of the implicit LU-SGS solver: in cells
where the predicted update would fall below $\delta=10^{-6}$ the residual is
replaced by

$$R^*=\frac{(\rho\tilde\nu)^n}{\Delta t}\Big(e^{R\,\Delta t/(\rho\tilde\nu)^n}-1\Big),$$

and any still-negative updated value is replaced by the exponential update
itself (Eqs. 60–69; $R$, $R^*$, $R_0$ page-local). $R^*\to0$ when $R\to0$ or
when $(\rho\tilde\nu)^n\to0$ with $R<0$, so convergence is not prevented. The
authors state that with it the standard model suffices and no negative SA
model and no reconstruction limiter is needed, and that, since it modifies
only the residual, it applies to any spatial discretization (§2.1, §2.5).
Their spatial scheme is a compact fourth-order variational reconstruction
whose interface-jump weights they optimize for near-wall cells of aspect
ratio $10^2$–$10^3$ (§2.3–2.4; see
[boundary-layer-conforming grids](/methods/boundary-layer-conforming-grid.md)).

**A positive surrogate variable.** Jiang et al. (2025) carry Moro et al.'s
always-positive auxiliary variable for SA over to the $k$-$\sqrt kL$
model: the transported variable is kept, and only the sources and the eddy
viscosity use a smooth positive surrogate
([Jiang et al. (2025)](/sources/jiang-2025.md), §3.1, Eqs. 10–13; see
[scale-adaptive simulation](/methods/scale-adaptive-simulation.md)). They also
take from their own DG SA work the Hermite-WENO limiting of the turbulence
variable in troubled cells (§3.1).

## Variants

Li & Liu (2022) sort the modifications into three kinds (§1): scope or
numerical fixes that barely change results; modifications of production or
destruction that express non-equilibrium transport; and nonlinear
constitutive relations replacing the Boussinesq stress.

### Scope and robustness fixes

- **SA-noft2** sets $f_{t2}\equiv0$ (Aupoix & Spalart 2003, cited by
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
trend agrees with the reduction of turbulence by convex curvature, which
the authors take as showing that SARC needs improvement in the log layer
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
(Spalart 2000 and Mani et al. 2013, cited by Li & Liu, Eqs. 23–27).
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
continues the curved-channel field inversion reported by Duraisamy et al.
(2019) above. In turbomachinery, Sandberg & Michelassi (2022) cite
field inversion with a neural network modifying SA in a low-Reynolds-number
low-pressure-turbine cascade (Ferrero et al. 2020) as giving a posteriori
accuracy similar to a much costlier two-equation model combined with the
$\gamma$-$Re_\theta$ transition model
([Sandberg & Michelassi (2022)](/sources/sandberg-2022.md), §4.3; see
[field inversion](/methods/field-inversion-machine-learning.md)); in the
same review SA is listed among the turbomachinery closures as one equation
for a scaled eddy viscosity (§2.2.2.1).

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

**A single-use corrected model for error estimation.** Fidkowski (2022)
multiplies the production of a conservative, density-weighted negative-SA
form by a spatial field, $\beta P$ with prior one, and infers $\beta$ so
that steady RANS reproduces the *time average* of an unsteady
(laminar-separation, transitional or DES) simulation; a
single-hidden-layer network (30 sigmoid neurons) on the dimensional
state, its gradient and the wall distance then represents $\beta$ inside
the solver and its linearization ([Fidkowski (2022)](/sources/fidkowski-2022.md),
§2.1 Eq. 2, §3.1–3.2). The model is explicitly single-use, retrained at
every mesh-adaptation iteration, and its steady adjoint serves as a
surrogate for the unstable unsteady adjoint of the time-averaged lift. A
new inversion objective weights the state mismatch by the output adjoint
times the element residual Jacobian (Eq. 13). On the
[NACA 0012](/benchmarks/naca-0012-airfoil.md) at $M=0.2$, $\alpha=7^\circ$,
$Re=10^4$ and $2\times10^4$ and on a high-lift airfoil at $Re=10^6$
($\alpha=17^\circ$), uncorrected SA under-predicts the mean lift, misses the
laminar separation bubble of the $2\times10^4$ case and converges under
adaptation to a wrong lift with "imperceptibly small" error estimates:
modelling error dominates, in cases the author notes lie outside the
usual applicability of RANS (§6.1–6.3, §7; see
[mesh adaptation](/methods/mesh-adaptation.md) and
[field inversion](/methods/field-inversion-machine-learning.md)).

**An explained random-forest correction of SA-QCR.** He et al. (2022)
correct the eddy viscosity of SA with the quadratic constitutive
relation, $\nu_t+\Delta\nu_t$, by a random forest on nine bounded local
features, trained a priori with the mean flow frozen at the high-fidelity
field, on the axisymmetric transonic bump of Bachalo & Johnson
($Re_c=2.763\times10^6$, $M_\infty=0.6$–$0.925$). One feature is the SA wall
function $f_w$ itself, which they read as a region classifier: below 0.4
free shear flow or viscous sublayer, 0.4–0.8 outer boundary layer,
0.8–1 near-wall layer in a favourable gradient, 1 the log layer, above 1
a near-wall layer in an adverse gradient (Table 3). Shapley-value
explanations rank the viscosity ratio $\nu_t/\nu$ first, which they relate
to the SA source terms scaling with $\nu_t$ or $\nu_t^2$, then a
normalized Q-criterion (shear raises, rotation lowers the correction),
then $f_w$ ([He et al. (2022)](/sources/he-2022-b.md), §2.2, §2.6, §5.1–5.3,
Fig. 13). They state that the SA equation "was not supported by any
physical conservation law" and was designed for equilibrium attached
boundary layers, and read the increased correction in the log layer and
its decrease elsewhere as a failure of the equilibrium assumption in this
flow (§2.1, §5.1). Only the offline (a priori) phase is reported; see
[model-form uncertainty](/definitions/model-form-uncertainty.md).

### Calibration of the coefficients and a learned replacement

Shan et al. (2023) treat the nine constants
$\boldsymbol\theta=(c_{t3},c_{t4},c_{b1},c_{b2},\sigma,c_{v1},\kappa,c_{w2},c_{w3})$
as free per flow case and calibrate them against measured surface pressure
on NREL wind-turbine airfoils near and beyond stall, minimizing
$\frac1n\sum_{i=1}^n\big(C_p^{i,\mathrm m}(\boldsymbol\theta)-C_p^{i,\mathrm{exp}}\big)^2$
over the $n$ pressure taps with teaching–learning-based optimization, a
population metaheuristic (20 members, each parameter within $\pm50\%$ of
its original value); $c_{w1}$ follows from the others through its formula
([Shan et al. (2023)](/sources/shan-2023.md), §II.B, §II.D, §III.B, Eq. 3,
Fig. 4; $(\cdot)_{\mathrm m}$ registry §11). They call the result a
data-assimilation ("DA") model and class the approach as parameter
calibration, as opposed to the high-dimensional inversion of
[field inversion](/methods/field-inversion-machine-learning.md) (§II.B).
At the calibration conditions the lift error falls from 28.3%, 19.1%,
16.2% and 24.8% (standard SA) to 6.3%, 0.7%, 7.2% and 0.2% (cases DA1–DA4:
S809 at $12.2^\circ$ and $14.2^\circ$, $Re=2\times10^6$; S805 at $12.2^\circ$
and $15.2^\circ$, $Re=10^6$; Table 3), with larger eddy viscosity in the
wake and the separation vortex (Figs. 9–10). The calibrated sets differ
strongly between cases, $c_{v1}$ from 3.550 to 7.295 and $\kappa$ from 0.396
to 0.615 (Table B1), and a set calibrated at one condition does not carry
over a lift curve: on S809 at $Re=2\times10^6$ the mean relative lift error
is 0.0835 with DA1 against 0.1341 with SA, but attached-flow accuracy is
lost, and at $Re=10^6$ DA1 is no better (0.1225 against 0.1200) (§III.C,
Fig. 11). Many calibrated values sit on the $\pm50\%$ bound: $c_{b2}=0.311$
and $c_{v1}=3.550$ are half the A7 values, $\kappa=0.615$ is 1.5 times
0.41, and $c_{w2}=0.150$, $c_{w3}=3.000$, $c_{t3}=0.600$, $c_{t4}=0.250$ in DA4
are at a bound too *(compiler check, not in the sources)*.

The learned model then replaces the SA equation. A fully connected network
maps six invariant mean-flow features (a mixing velocity, the rotation and
strain norms, two wall-distance-weighted forms of them and the
pressure-gradient magnitude) to the working variable $\tilde\nu$, from
which $\nu_t=\tilde\nu f_{v1}$ is computed, and runs inside the solver at
every iteration ("iterative" coupling) (§II.A, §II.C, Table 1, Eq. 10).
$\tilde\nu$ is chosen as the output because near the wall
$\tilde\nu\sim\nu_t^{1/4}$, compressing the range the network must fit; for
a given $\nu_t$ it is the unique positive root of a quartic (§II.C.2);
for small $\chi$, $f_{v1}\approx\chi^3/c_{v1}^3$ gives
$\nu_t\approx\tilde\nu^4/(\nu^3c_{v1}^3)$ *(compiler check, not in the
sources)*. Trained on standard-SA fields in attached flow and DA fields in
separated flow, it keeps SA's accuracy below stall and DA's above: on S809
at $Re=2\times10^6$ its lift errors are 1.2–7.4% from $10.2^\circ$ to
$15.2^\circ$ against 16.6–28.4% for SA, and the mean relative lift error
above stall falls by "over 60%" for S809, S805 and the unseen S814
(§III.E–F, Table 5, Fig. 24). The authors grant that only the coefficient
uncertainty of SA is addressed (§IV; see
[model-form uncertainty](/definitions/model-form-uncertainty.md) and
[Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md)).

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
Pan & Zhang (2023) compare SA-based DES ($C_{\mathrm{DES}}=0.65$, $\Delta$ the
largest cell edge) and DDES with ANSYS Fluent defaults in a stalled
centrifugal impeller, against a same-grid LES (§II.B–C, §IV). Husson et al.
(2024) use the SA-based zonal DES mode 2 (2020) in a lattice Boltzmann
solver, with the LES-zone functions $f_{v1}=1$, $f_{v2}=0$, $f_w=1$ taken from
mode 1 and an enhanced destruction $f_w=100$ in grey areas; they note that
where production and destruction balance $\nu_t\approx\lvert\Omega\rvert\ell^2$,
a Smagorinsky-like viscosity when $\ell\approx\Delta$, which is what
motivates hybridization through $\ell$ (§2.2, Eqs. 29–35). Batther & Lee
(2022) run fully turbulent SA and two SA-based transition models
inside delayed DES of a pitching airfoil (§3.1; Evidence below). Sugaya &
Imamura (2021) run DDES-p, an SA-based DDES whose modified shielding
function protects the RANS regions when the streamwise grid size is small,
which makes it "suitable for unsteady flow simulations using Cartesian
grids" (the function is not printed), for a hovering rotor on moving
Cartesian grids ([Sugaya & Imamura (2021)](/sources/sugaya-2021.md), §2.1,
§4). These formulations are on the [DES page](/methods/detached-eddy-simulation.md).
Li et al. (2024b) run SA-IDDES, with the wall distance of the destruction
term replaced by the IDDES length, on the NASA CRM high-lift configuration
against steady SA-RANS: drag 0.1843 (pressure 0.1691, friction 0.0151)
against 0.1867 (0.1701, 0.0165) and 0.1868 measured; SA-RANS overpredicts
the flap separation behind the inboard bracket and captures only the strong
tip vortices, which the authors link to the undisturbed bracket tip vortex
(§III.D, Figs. 5–9; see the [NASA CRM high-lift configuration](/benchmarks/nasa-crm-high-lift.md)).
Zhang et al. (2024) run SA-DDES with $C_{\mathrm{DES}}=0.65$ for the tip flow of
a compressor tandem cascade (§2.3; see
[compressor cascades](/benchmarks/compressor-cascade.md)).
Mani & Dorgan (2023) state that the original DES is SA-based and that
DES and then delayed DES carried unsteady simulation at Boeing
([Mani & Dorgan (2023)](/sources/mani-2023.md), §4.5.2).
Fidkowski (2022) uses a "simplified DES" for adaptation studies: the wall
distance is attenuated by the mesh-independent
$d_{\max}\tanh(d/d_{\max})$, $d_{\max}=0.02c$, instead of a grid length, so
that the model does not change as the mesh is adapted (§2.1, Eq. 3).
Ghidoni et al. (2022) recall that SA can be run with zero eddy viscosity
upstream of separation to represent laminar separation, as in the
laminar-separation DES of the cylinder at $Re=1.4\times10^5$ they quote,
which the $k$-$\omega$ model cannot ([Ghidoni et al. (2022)](/sources/ghidoni-2022.md),
§6.2, Table 12; see the [Wilcox $k$-$\omega$ page](/methods/k-omega-model.md)).

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

Sugaya & Imamura (2021) use the immersed-boundary wall condition of
Tamaki et al. with the Spalart–Allmaras wall model $u^+=f_{\mathrm{wall}}(y^+)$
(page-local $f_{\mathrm{wall}}$, not printed) and extend it to moving
Cartesian grids (§2.2, Eqs. 10–15, Table 1). At the face between a fluid and
a wall cell, the tangential velocity is extrapolated linearly from an image
point at $d_{\mathrm{IP}}=2\Delta x$ along the wall normal with the slope of
the wall model there, and $u_\tau$ comes from Newton–Raphson iterations on
$u_\tau f_{\mathrm{wall}}(y^+_{\mathrm{IP}})=u_{t,\mathrm{IP}}-V_{t,\mathrm{wall}}$,
with $u_{t,\mathrm{IP}}$ the tangential velocity at the image point and
$V_{t,\mathrm{wall}}$ the tangential wall speed (page-local), which recovers
Tamaki et al.'s condition for a wall at rest; the near-wall modification of
$\tilde\nu$ of Tamaki et al. is used and not printed. Because the grid moves
rigidly with the body, the turbulent boundary layer stays in the same cells
(§2.2). With SA RANS on a NACA 0012 at $Re=6\times10^6$, $\alpha=10^\circ$,
relative Mach 0.15 and $y^+_{\mathrm{IP}}\approx230$ at mid-chord, a
stationary grid in a free stream and a moving grid in quiescent air give
density residuals that differ "in the order of machine zero" and identical
$C_p$, $C_f$, velocity and eddy-viscosity profiles, in agreement with the
body-fitted code FaSTAR on the Turbulence Modeling Resource grid (§3.1,
Table 3, Figs. 4–8). The authors cite agreement of immersed boundaries with
wall functions and body-fitted grids for the surface pressure "when $y^+$ is
approximately 500 or less" (§3.1). Details on the
[immersed-boundary page](/methods/immersed-boundary-method.md) and
[RANS wall functions](/methods/rans-wall-function.md).

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

### Transonic bump with QCR

On the axisymmetric transonic bump He et al. (2022) find that SU2 SA and
SST wall pressures "almost overlap" with CFL3D at $M_\infty=0.875$, and that
SA-QCR predicts a delayed shock front and delayed shock-induced
separation for $M_\infty\ge0.85$, deviating most from the wall-resolved LES
of Uzun & Malik, while SST-QCR predicts the wall pressure well at all six
Mach numbers (§2.4–2.5, Figs. 4–5). Against the LES eddy viscosity (a least-squares fit of the LES
stress, see the [Boussinesq page](/definitions/boussinesq-hypothesis.md))
SA-QCR overpredicts $\nu_t$ in the separation bubble and underpredicts it
in the pre-shock boundary layer, the shear layer, the reattached layer
and at the shock front; the authors attribute the last to shock buffet,
"conceptually impossible to be modeled by steady RANS" (§2.7, Fig. 7; see
[shock/boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)).

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

- Mani & Dorgan (2023) name SA with its rotation–curvature (SA-RC) and
  quadratic-constitutive (SA-QCR) variants, with Menter's SST, as Boeing's
  workhorse RANS models for design, analysis and risk mitigation; all
  work for attached flow and small separation but can be inadequate where
  large separation dominates, and "many other modifications have been
  studied, but rarely have they provided general improvements"
  ([Mani & Dorgan (2023)](/sources/mani-2023.md), §4.5.1). As verification
  evidence they reproduce from the NASA Turbulence Modeling Resource the
  zero-pressure-gradient flat plate ($M=0.2$, $Re_L=5\times10^6$, grids
  $35\times25$ to $545\times385$): CFL3D and FUN3D converge to the same skin
  friction at $x=0.97$ for SA and SA-QCR2000, which lets a code verify its
  implementation without sharing source code (§4.1.1, Fig. 5).
- In the AIAA Third High-Lift Prediction Workshop most of the 79 submitted
  data sets were steady RANS with SA or SST variants; they cluster in the
  linear lift range and scatter near maximum lift. An OpenFOAM SA reference
  on 109 million cells cost about $60\times10^3$ core-hours, comparable to the
  medium-grid wall-modelled LES of Goc et al.
  ([Goc et al. (2021)](/sources/goc-2021.md), §1, Fig. 1, §4; see
  [JAXA Standard Model](/benchmarks/jaxa-standard-model.md)).
- The summary of the wall-modelled-LES group of the Fourth High-Lift
  Prediction Workshop compares its submissions with RANS results of the
  workshop's other groups, without naming their models
  ([Kiris et al. (2023)](/sources/kiris-2023.md), §III; see
  [NASA CRM high-lift](/benchmarks/nasa-crm-high-lift.md)).
- Mo et al. (2023) take the mean inflow profiles of DNS of supersonic and
  hypersonic flat-plate boundary layers from SA RANS, at $\delta=6$ mm
  ($Re_\tau=340$) for an adiabatic Mach 2.9 case and $\delta=7.5$ mm
  ($Re_\tau=155$) for a cold-wall Mach 7.25 case, and add rescaled
  fluctuations from a stored library
  ([Mo et al. (2023)](/sources/mo-2023.md), §II, §III C, §IV B; see
  [inflow turbulence generation](/methods/inflow-turbulence-generation.md)).
- HORSES3D runs negative-SA RANS of the NASA Common Research Model at
  $M=0.85$, $Re=5\times10^6$, $2.3^\circ$ incidence on a third-order ($N=2$)
  hexahedral mesh with split-form inviscid fluxes; only surface pressure
  contours are shown ([Ferrer et al. (2023)](/sources/ferrer-2023.md), §4.1,
  Fig. 6).
- Schotte et al. (2026) run SA-neg (Allmaras, Johnson & Spalart 2012,
  equations not printed) as the closure of every case of their anisotropic
  mesh adaptation for a high-order modal DG solver (CODA): the HLPW4
  three-element airfoil with $N=1$–3, the RAE2822 airfoil, the HLPW5 CRM
  high-lift wing–body and the ONERA M6 wing
  ([Schotte et al. (2026)](/sources/schotte-2026.md), §2.1, §4; HAL deposit
  of the version of record; see [mesh adaptation](/methods/mesh-adaptation.md)
  and [NASA CRM high-lift](/benchmarks/nasa-crm-high-lift.md)).
- FLEXI initialises scale-resolving runs with an SA RANS solution obtained
  by pseudo-time stepping ([Krais et al. (2021)](/sources/krais-2021.md),
  §2.2.3; see [FLEXI](/software/flexi.md)).
- The RSC-SGS hybrid RANS/LES method reduces the mean-strain stress of SA (or
  of a van Driest mixing length) by the averaged resolved stress, as
  Haering et al. (2022) describe it, classing it as effectively zonal
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
- **Fully turbulent DDES of dynamic stall.** On a NACA 0012 pitching up at
  $Re=2\times10^5$, $M=0.1$, fully turbulent SA inside delayed DES
  underpredicts lift at low incidence, matches the trends of a wall-resolved
  LES at larger angles, and forms an abrupt turbulent separation bubble
  between $\alpha=14.1^\circ$ and $14.5^\circ$ instead of a laminar
  separation bubble, a behaviour the authors say "has not yet been
  documented in literature"; it also shows more trailing-edge separation,
  which does not propagate upstream. Of the two SA-based transition models,
  Coder's amplification-factor transport model is the closest to the LES
  and Medida & Baeder's $\gamma$-$Re_\theta$ form oscillates at low
  incidence ([Batther & Lee (2022)](/sources/batther-2022.md), §4.3.1,
  §4.4, Figs. 17, 21–22; see [dynamic stall](/definitions/dynamic-stall.md)
  and the [transition-model page](/methods/local-correlation-based-transition-model.md)).
- **High-order RANS of the RAE 2822.** At the first High-Order CFD
  Workshop two of the three DG submissions on the
  [RAE 2822 airfoil](/benchmarks/rae-2822-airfoil.md) (case 9, $M=0.734$,
  $\alpha=2.79^\circ$, $Re=6.5\times10^6$, transition fixed at 3% chord) used
  SA; across SA, $k$-$\omega$ and an algebraic Reynolds-stress model the
  organizers find "a large spread among the groups and virtually no
  improvement from high order under uniform mesh refinement", attributed
  partly to the wake alignment of the initial mesh and partly to the choice
  of turbulence model, with adaptive mesh optimization "markedly superior"
  (Wang et al. 2013, §4.8, §5.4, Table V, Fig. 23; see
  [mesh adaptation](/methods/mesh-adaptation.md)).
- **Pitching airfoil and hovering rotor on moving Cartesian grids.** With
  SA RANS on the AGARD Case 3 NACA 0012 pitching at $M_\infty=0.6$,
  $Re=4.8\times10^6$ ($y^+\sim100$ at mid-chord), Sugaya & Imamura (2021)
  reproduce the shock position, the $C_l$ and $C_m$ hysteresis loops and the
  lift-trajectory inversion of the experiment and of FUN3D on a body-fitted
  grid, the moment within about 0.005 of experiment, as is the body-fitted
  solution (§3.2, Figs. 10–13). With DDES-p of the
  [Caradonna–Tung rotor](/benchmarks/caradonna-tung-rotor.md) on 75 and 149
  million cells, the thrust coefficient (0.00514–0.00521) and figure of
  merit (0.594–0.618) depend little on grid and scheme (§4.5, Table 7).
- **Rotor wake with URANS.** Han et al. (2022) close URANS of the same
  rotor with SA, no variant stated, to compare reconstructions on an
  18-million-cell overset grid; at tip Mach 0.439 and 0.877 the thrust
  coefficient errors against experiment are 3.5% and 8.2% with third-order
  MUSCL, 1.5% and 5.1% with fifth-order WENO-JS and 0.9% and 3.0% with
  WENO-K ([Han et al. (2022)](/sources/han-2022-c.md), §4, Tables 6–7; see
  [WENO schemes](/methods/weno-scheme.md) and
  [numerical dissipation](/properties/numerical-dissipation.md)).
- **Aeroacoustic shape optimization with an adjoint SA.** Monfaredi et al.
  (2021) run two-dimensional compressible SA URANS (no equation, constant or
  variant printed) as the near field of a permeable Ffowcs Williams–Hawkings
  prediction, and solve the continuous adjoint of the SA equation and of the
  Eikonal wall-distance equation in the unsteady adjoint, the SA adjoint
  formulation being deferred to a thesis
  ([Monfaredi et al. (2021)](/sources/monfaredi-2021.md), §1, §2.1, §3; see
  [FW-H analogy](/methods/ffowcs-williams-hawkings-acoustic-analogy.md)). On a
  rod–airfoil configuration ($M_\infty=0.2$, $Re=4.8\times10^5$ on the airfoil
  chord, $y^+<1$) the shedding Strouhal number is 0.24, as in a published 2D
  URANS and above the measured value of about 0.19, and the mean velocity
  agrees with one published 2D URANS and "seem[s] to outperform" another; at
  $x/C=0.25$ all URANS overpredict the measured profile. The authors ascribe
  part of the differences to SA against the SST of the other URANS, without
  running SST (§4.2, Figs. 7, 10).
- **Square cylinder.** Jiang et al. (2025) compare SA URANS with the
  $k$-$\sqrt kL$ model on a two-dimensional square cylinder at $Re=10^4$,
  calling the comparison possibly unfair because SA was designed for steady
  high-Reynolds flows (§4.3; see
  [square-cylinder flow](/benchmarks/square-cylinder-flow.md)).

### High-order RANS of the NASA verification cases

The NASA Turbulence Modeling Resource cases appear in three sources
computed at high order:

- **NACA 0012, $M=0.15$, $Re=6\times10^6$.** Lodares et al. (2022) run
  their entropy-stable DGSEM with the kinetic-energy-preserving split form
  on the coarsest TMR grid (113×33, quadratic edges), $N=2$–6: at $N=6$,
  $C_L=1.0894$, $C_D=0.01250$ at $10^\circ$ against the reference 1.0909,
  0.01231, and $C_L=1.5502$, $C_D=0.02144$ at $15^\circ$ against 1.5461,
  0.02124; at $0^\circ$, $C_D=0.00813$ for every $N$ against 0.00819 (§7.4,
  Table 2). Tomboulides et al. (2025) list the CFL3D SA values as
  $C_D=0.008190$ at $0^\circ$ and $C_D=0.01231$, $C_L=1.0909$ at $10^\circ$,
  and FUN3D SA as 0.008120 and 0.01242, 1.0983, against 0.0081, 0.012 and
  1.075 measured ([Tomboulides et al. (2025)](/sources/tomboulides-2025.md),
  §3.4, Tables 3–4; see [$k$-$\tau$ model](/methods/k-tau-model.md)).
  Lodares et al.'s reference values coincide with the CFL3D entries of
  Tomboulides et al. *(compiler check, not in the sources)*; see
  Qualifications for the label.
- **NACA 0012 at $15^\circ$, $M=0.15$, $Re=2.88\times10^6$.** With the
  exponential decay procedure, Huang et al.'s fourth-order scheme reaches
  $C_L=1.393$, 1.499 and 1.523 on three C-meshes of 11,880 to 33,150 cells,
  against 1.526 from Gregory & O'Reilly, while the second-order scheme gives
  1.183, 1.277, 1.299, and 1.437 on a fourth mesh of 143,700 cells; it also
  predicts a spurious trailing-edge separation bubble on all meshes, which
  the fourth-order scheme shows only on the coarsest. Measured by the
  inverse of error times CPU time, fourth order becomes more efficient with
  refinement and second order less (§3.2, Table 6, Fig. 29).
- **Zero-pressure-gradient flat plate, $M=0.2$, $Re=5\times10^6$.** Huang et
  al.'s fourth-order scheme on 137×97 cells matches the CFL3D skin friction
  on the 545×385 grid, while second order underpredicts the log-region
  velocity (§3.1); Lodares et al. on the coarsest TMR mesh with $N$ up to
  10 agree with the FUN3D 545×385 skin friction, eddy-viscosity profile
  and law of the wall at $x=0.97$ (§7.3; see
  [turbulent boundary layer](/benchmarks/turbulent-boundary-layer.md)).
- **30P-30N three-element airfoil** at $16^\circ$, $Re=9\times10^6$: Huang
  et al.'s optimized fourth-order scheme on 53,870 cells predicts lift and
  drag closer to the DLR reference than the fourth-order scheme of Pan et
  al. and the second-order scheme, and its skin friction is closer to a
  $p=4$ DG solution of which the finite-volume grid has 4.8% of the degrees
  of freedom (§3.3).

## Qualifications

- Li et al. (2024b) and Zhang et al. (2024) print no value of $c_{w1}$, so
  the log-layer relation above cannot be checked against their forms.
- Li & Liu's ranking rests on one cascade and one rotor, against experiment
  only, with grid adequacy asserted by citation; no LES or DNS reference is
  used (§2.1, §3).
- Li & Liu present the helicity–backscatter link, a result of their own
  group, as proved in the cited work; the mechanism by which more
  production yields less eddy viscosity is argued in the text, with no
  dedicated test.
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
  give no reason for the strain. Pan & Zhang (2023) and Tang et al. (2022) build
  the same strain-based measure while calling it the modified vorticity
  (Pan & Zhang, §II.B, Eqs. 4–5), and Huang et al. (2022b) define their
  "vorticity" magnitude as $\sqrt{2\omega_{ij}\omega_{ij}}$ with $\omega_{ij}$
  printed as $\tfrac12(\partial_ju_i+\partial_iu_j)$, a plus sign that makes it
  the strain magnitude (§2.1); whether these are slips or the SA-S variant
  is not stated by these sources.
- Pan & Zhang (2023) print $f_{v1}=\chi^3/(\chi^3+c_{v1}^6)$, with exponent 6
  on $c_{v1}$ against 3 on $\chi$, unlike every other source on this page
  (§II.B, Eq. 4).
- The printed diffusion coefficients of the compressible forms differ:
  $(\mu+\rho\tilde\nu)/\sigma$ in Fanizza et al. (2025),
  $\rho(\nu+\tilde\nu)/\sigma$ in Lodares et al. (2022), the same thing, and
  $(\mu+\mu_t)/\sigma$ with $\mu_t=\rho\tilde\nu f_{v1}$ in Huang et al.
  (2022b), which departs from $\tilde\nu$ inside the buffer and viscous
  layers where $f_{v1}<1$ *(compiler check, not in the sources)*; Huang et
  al. keep, and Lodares et al. explicitly neglect, the density-gradient
  diffusion term. Neither discusses the alternative.
- Lodares et al. (2022) label the NACA 0012 reference "FUN3D, 897×257" in
  Table 2 and "CFL3D, 897×257" in the legends of Fig. 10 (§7.4).
- Huang et al. (2022b) cite LU-SGS as their ref. [49], which is Reichardt's
  1951 wall-law paper (§2.2).

- He et al. (2022) print the SA equation (Eq. 4) without constant values;
  their wall-region map of $f_w$ (Table 3) and the one in their §5.2
  (log layer $0.3<f_w<0.7$, outer layer $0.7<f_w<2.0$) disagree within the
  paper.

- Shan et al. (2023) print the numerator of the $S_{\mathrm{SA}}$ correction in
  Eq. A3 as an overbarred upsilon, while Eq. A6 writes $\tilde\nu$ in $r$; the
  form above uses $\tilde\nu$. Their Table B1 lists the standard $c_{b1}$ as
  0.136 and $\sigma$ as 0.667, roundings of the A7 values. The experimental
  lift of S809 at $12.2^\circ$ is 0.996 in their Table 3 and 0.995 in Table 5,
  with SA errors of 28.3% and 28.4%. The reduction of the post-stall lift
  error is "over 57%" in the abstract and "over 60%" in §III.F. Their
  conclusions mention a non-negativity constraint on the eddy viscosity in
  the loss function, while the loss of Eq. 12 has only a mean-square and a
  weight-norm term and positivity comes from the ReLU output layer (Eq. 6).
  The member error of Eq. 13 is the square root of the objective of Eq. 3,
  both said to use "the same" variables. Their mixing length (Eq. 8) is
  printed as $\min\{\kappa y(1-e^{y^+/A^+}),\kappa\delta\}$; for $y^+>0$ the
  first argument is negative, so the printed form always returns a negative
  length *(compiler check, not in the sources)*. The text says min–max
  scaling maps the data to $[-1,1]$; the printed formula
  $(x-x_{\min})/(x_{\max}-x_{\min})$ maps it to $[0,1]$ *(compiler check, not
  in the sources)*.

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
- [Tang et al. (2022)](/sources/tang-2022.md) — §2.1, Eqs. 2, 6–9.
- [Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md) — §1, §7.
- [Ghidoni et al. (2026)](/sources/ghidoni-2026.md) — §1.
- [Schotte et al. (2026)](/sources/schotte-2026.md) — §2.1, §4 (HAL deposit of the version of record).
- [Huang et al. (2022b)](/sources/huang-2022-d.md) — §2.1 Eqs. 3–6, §2.2, §2.3–2.5 Eqs. 53–69, §3.1–3.3, Table 6, Fig. 29.
- [Lodares et al. (2022)](/sources/lodares-2022.md) — §2 Eqs. 13–17, §3.2 Eqs. 38–50, §4.3–4.5 Eqs. 68, 74, §5.1.2 Eqs. 87–89, §7.2–7.4 Table 2, Fig. 10.
- [Pan & Zhang (2023)](/sources/pan-2023.md) — §II.B–C Eqs. 3–6, §IV.
- [Husson et al. (2024)](/sources/husson-2024.md) — §2.2 Eqs. 18–23, 29–35, §3.2 Eqs. 38–39, 42.
- [Jiang et al. (2025)](/sources/jiang-2025.md) — §3.1 Eqs. 10–13, §4.3.
- [Tomboulides et al. (2025)](/sources/tomboulides-2025.md) — §3.4, Tables 3–4.
- [Batther & Lee (2022)](/sources/batther-2022.md) — §3.1, §4.3.1, §4.4, Figs. 17, 21–22.
- [Wang et al. (2013)](/sources/wang-2013.md) — §4.8, §4.11–4.12, §5.4 Table V Fig. 23, §6.
- [Sandberg & Michelassi (2022)](/sources/sandberg-2022.md) — §2.2.2.1, §4.3.
- [Sugaya & Imamura (2021)](/sources/sugaya-2021.md) — §2.1, §2.2 Eqs. 10–15 Table 1, §3.1 Table 3 Figs. 4–8, §3.2 Figs. 10–13, §4.5 Table 7.
- [Han et al. (2022)](/sources/han-2022-c.md) — §4, Tables 6–7.
- [Monfaredi et al. (2021)](/sources/monfaredi-2021.md) — §1, §2.1, §3, §4.2 Figs. 7, 10.
- [Fidkowski (2022)](/sources/fidkowski-2022.md) — §2.1 Eqs. 2–3, §3.1–3.2 Eq. 13, §6.1–6.3, §7.
- [He et al. (2022)](/sources/he-2022-b.md) — §2.1 Eq. 4, §2.2, §2.4–2.7 Figs. 4–7 Table 3, §5.1–5.3 Fig. 13.
- [Ghidoni et al. (2022)](/sources/ghidoni-2022.md) — §6.2, Table 12.
- [Shan et al. (2023)](/sources/shan-2023.md) — §II.A–D Eqs. 3, 6, 8, 10–13, §III.A–F Tables 3, 5, B1 Figs. 4, 9–11, 24, §IV, App. A Eqs. A1–A7.
- [Mani & Dorgan (2023)](/sources/mani-2023.md) — §4.1.1 Fig. 5, §4.5.1–4.5.2.
- [Kiris et al. (2023)](/sources/kiris-2023.md) — §III.
- [Mo et al. (2023)](/sources/mo-2023.md) — §II, §III C, §IV B.
- [Li et al. (2024b)](/sources/li-2024-f.md) — §II.B.1, Eqs. (3a)–(3b) (printed SA with $f_{t2}$); §II.B.2 (SA-IDDES); §III.D, Figs. 5–9 (CRM-HL drag and separation, SA-RANS against SA-IDDES).
- [Zhang et al. (2024)](/sources/zhang-2024.md) — §2.3, Eqs. (1)–(4) (printed SA and its DDES shielding argument, constants).
