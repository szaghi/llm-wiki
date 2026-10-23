---
type: Method
title: "Semi-implicit leapfrog"
description: "NIMROD's time advance: velocity staggered half a step from density, temperature and magnetic field, the fields solved one after another in dependency order, a semi-implicit operator built on the linearized ideal-MHD force stabilizing the waves of the velocity advance, and time-centred implicit advection in the other equations."
status: established
aliases: [implicit leapfrog, mixed implicit/semi-implicit leapfrog, staggered semi-implicit advance, NIMROD time advance]
tags: [time-integration, numerics, full-mhd]
timestamp: 2026-10-16T18:35:00Z
---

# Semi-implicit leapfrog

The semi-implicit leapfrog of [NIMROD](/software/nimrod.md) exploits the data
dependencies of single-fluid MHD: without atomic physics the density depends
on the velocity, the velocity on density, field and temperature, the
temperature on density and velocity, and the field on the velocity,
$n(\mathbf v)$, $\mathbf v(n,\mathbf B,T)$, $T(n,\mathbf v)$, $\mathbf B(\mathbf v)$.
This structure allows the velocity to be staggered in time against the other
fields, which are then solved one after another rather than as one coupled
system ([Taheri et al. (2022)](/sources/taheri-2022.md), §3, attributed to
Sovinec et al.). The scheme is the mixed implicit/semi-implicit leapfrog of
Sovinec and King (2010); NIMROD's predictor–corrector variants are a separate
family (§3). It takes smaller but cheaper steps than a fully consistent
implicit method ([Artola et al. (2021)](/sources/artola-2021.md), §2); compare
the [linearized implicit advance](/methods/implicit-time-integration.md) of
JOREK.

## Staggering and sequence

The velocities live at integer levels $j\to j+1$; density, temperature and
magnetic field at half-integer levels $j+\tfrac12\to j+\tfrac32$. One step of
the plasma–neutral system of [Taheri et al. (2022)](/sources/taheri-2022.md)
(§3, Fig. 1) is

1. $\Delta\mathbf v$ and $\Delta\mathbf v_{\mathrm N}$ from
   $(n_i^{j+1/2},T^{j+1/2},\mathbf B^{j+1/2},\mathbf v^{j})$, solved separately
   for plasma and neutrals;
2. $\Delta n_i$ and $\Delta n_{\mathrm N}$ with $\mathbf v^{j+1}$, solved
   together;
3. $\Delta T$ and $\Delta T_{\mathrm N}$ with $\mathbf v^{j+1}$ and a
   time-centred density, solved together;
4. $\Delta\mathbf B$ with $\mathbf v^{j+1}$.

For single-fluid MHD the neutral unknowns drop out. The velocity of the
neutral species also needs a semi-implicit operator, for its sound waves
(§3).

The same dependency structure is the stated template of the equation-sparsified
[Fourier neural operator](/methods/fourier-neural-operator-surrogates.md)
(ST-FNO) of [Rahman et al. (2024)](/sources/rahman-2024.md), which "exploits
the same structure of the MHD equations that is exploited by the semi-implicit
leapfrog algorithm within NIMROD" by feeding each output field only from the
fields its evolution equation depends on (§II B 2). The surrogate does not
reproduce the staggering: all its inputs are taken at the same snapshot, and
for the two-fluid model it emulates it drops dependencies by hand, e.g. the
Hall and electron-pressure terms from the field advance (§II B 1–2;
compiler's observation on the staggering).

## The semi-implicit velocity advance

A semi-implicit operator in the velocity advance is "essential" to stabilize
wave propagation in a leapfrog; building it on the ideal-MHD force operator
limits spectral-pollution errors of the time discretization
([Taheri et al. (2022)](/sources/taheri-2022.md), §3, attributed to Schnack et
al. 1987 and Lütjens and Luciani 1996). The operator acting on the velocity
increment is
$$\mathcal L_{\mathrm{SI}}(\Delta\mathbf v)=C_0\Big\{\frac{1}{\mu_0}\big[\nabla\times\nabla\times(\Delta\mathbf v\times\mathbf B)\big]\times\mathbf B+\mathbf J\times\nabla\times(\Delta\mathbf v\times\mathbf B)+\nabla\big(\Delta\mathbf v\cdot\nabla p+\Gamma p\,\nabla\cdot\Delta\mathbf v\big)\Big\}+C_1\,p_{\mathrm{nl}}\nabla^2\Delta\mathbf v$$
(App. A, Eq. 44, printed with $\Gamma=5/3$): the linearized ideal-MHD force
times a coefficient $C_0$, plus an isotropic Laplacian scaled by a
"non-linear pressure" $p_{\mathrm{nl}}$, "typically orders of magnitude
smaller than the total pressure". For neutrals only the sound-wave part
$C_0\nabla(\Delta\mathbf v_{\mathrm N}\cdot\nabla p_{\mathrm N}+\Gamma p_{\mathrm N}\nabla\cdot\Delta\mathbf v_{\mathrm N})$
and the Laplacian remain (Eq. 45). No values of $C_0$, $C_1$ or
$p_{\mathrm{nl}}$ are given. In the momentum equation the operator enters as
$-\Delta t\,\mathcal L_{\mathrm{SI}}(\Delta\mathbf v)$ next to
$m_in_i\,\Delta\mathbf v/\Delta t$ (Eq. 37), i.e. the velocity advance inverts
$\big(m_in_i-\Delta t^2\mathcal L_{\mathrm{SI}}\big)\Delta\mathbf v/\Delta t$
(reader's reading). The advance also linearizes advection,
$$m_in_i^{j+1/2}\Big(\frac{\Delta\mathbf v}{\Delta t}+\theta_{\mathrm t,v}\mathbf v^{j}\cdot\nabla\Delta\mathbf v+\theta_{\mathrm t,v}\Delta\mathbf v\cdot\nabla\mathbf v^{j}+\theta_{\mathrm t,v}^2\Delta\mathbf v\cdot\nabla\Delta\mathbf v\Big)-\Delta t\,\mathcal L_{\mathrm{SI}}^{j+1/2}(\Delta\mathbf v)+\dots=-m_in_i^{j+1/2}\mathbf v^{j}\cdot\nabla\mathbf v^{j}+\mathbf J^{j+1/2}\times\mathbf B^{j+1/2}-\nabla p^{j+1/2}+\dots$$
(Eq. 37, with viscous and atomic terms omitted here), where $\theta_{\mathrm t,v}$ is a
centring parameter the text does not define.

## The implicit field advances

The other fields are advanced implicitly with time-centred advection.
Centring $\theta_{\mathrm t}=\tfrac12$ of the advection terms "is required to maintain
numerical stability" of the mixed scheme
([Taheri et al. (2022)](/sources/taheri-2022.md), §3.1, attributed to Sovinec
and King; no proof in this paper). The density advance is
$$\frac{\Delta n_i}{\Delta t}+\theta_{\mathrm t}\,\nabla\cdot\big(\mathbf v^{j+1}\Delta n_i\big)=-\nabla\cdot\big(\mathbf v^{j+1}n_i^{j+1/2}\big)+(\text{source terms}),\qquad \Delta n_i=n_i^{j+3/2}-n_i^{j+1/2}$$
(Eq. 19), and the induction advance is
$$\frac{\Delta\mathbf B}{\Delta t}-\theta_{\mathrm t}\,\nabla\times\big(\mathbf v^{j+1}\times\Delta\mathbf B\big)+\theta_{\mathrm t,\mathrm{visc}}\nabla\times\big(\eta\,\Delta\mathbf J\big)=\nabla\times\big(\mathbf v^{j+1}\times\mathbf B^{j+1/2}\big)-\nabla\times\big(\eta\,\mathbf J^{j+1/2}\big)$$
(Eq. 43). Spatially NIMROD uses 2D $C^0$ spectral elements (biquintic in these
tests) with a Fourier direction (§2), and the linear solves use GMRES (§3.2).
In a two-fluid DIII-D QH-mode run the algebraic solves are preconditioned
with the SuperLU_DIST direct solver, which per toroidal Fourier mode needs
34 GB of memory, 9 s to factorize and 340 ms to apply on 64 Perlmutter CPU
cores ([Rahman et al. (2024)](/sources/rahman-2024.md), §II B, §III A 1; see
[implicit time integration](/methods/implicit-time-integration.md)).
$\nabla\cdot\mathbf B$ is not identically zero in NIMROD and is controlled by a
diffusive correction added to Faraday's law
([Artola et al. (2021)](/sources/artola-2021.md), §2; see
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)).

## Step size

Leapfrog staggering loses accuracy beyond the flow CFL, so NIMROD adapts
$\Delta t$ to the flow velocity; in the most dynamic part of the 3D NSTX VDE
$\Delta t>0.015\,\tau_A$, "hundreds of times larger than an explicit
stability limit", and more than ten times larger elsewhere
([Artola et al. (2021)](/sources/artola-2021.md), §3;
[benchmark](/benchmarks/nstx-vde-benchmarks.md)). In a two-fluid
extended-MHD DIII-D QH-mode edge run with carbon and deuterium ions,
$\Delta t=5\times10^{-9}$ s gives a compressional-Alfvén CFL number of
about 800 at a flow CFL number of about 2, on $96\times256$ bi-quartic
elements with 22 toroidal Fourier modes, at about 7 s per step on 11
Perlmutter CPU nodes ([Rahman et al. (2024)](/sources/rahman-2024.md),
§III A). Taheri et al. attribute the
common error of all their schemes at large $\Delta t$ in a 1D snowplow test
"likely" to the Crank–Nicolson and leapfrog discretization itself (§5.2).
Adding stiff atomic sources breaks the dependency structure the leapfrog
relies on; the resulting splitting schemes are described on
[operator splitting of atomic sources](/methods/operator-splitting-of-atomic-sources.md).

## Qualifications

- **No stability analysis in the corpus.** Taheri et al. give no von Neumann
  or other formal stability analysis; the stability of the leapfrog and of the
  semi-implicit operator is taken from earlier work (reader's note).
- **Labelling.** [Artola et al. (2021)](/sources/artola-2021.md) label
  NIMROD's advance "split-implicit" in Table 1 and "implicit leapfrog" in the
  text (reader's note).
- **Printed slips in Taheri et al.** $\theta_{\mathrm t,v}$, $\theta_{\mathrm t,\mathrm{visc}}$ and
  the time-centred densities of the temperature advance are undefined; Eq. 37
  uses a fixed $\tfrac12\nabla\cdot\underline\Pi(\Delta\mathbf v)$ rather than a
  centring parameter; and the left side of the neutral velocity advance
  (Eq. 38) prints two charge-exchange friction terms that cancel identically,
  one of which should by analogy with Eq. 37 carry the other subscript
  (reader's notes). The version read is arXiv v1; the CPC version may differ.

# Citations

- [Taheri et al. (2022)](/sources/taheri-2022.md) — §2, §3, §3.1, Eqs. 19, 37–38, 43–45, Fig. 1.
- [Artola et al. (2021)](/sources/artola-2021.md) — §2–3, Table 1.
- [Rahman et al. (2024)](/sources/rahman-2024.md) — §II B, §III A.
