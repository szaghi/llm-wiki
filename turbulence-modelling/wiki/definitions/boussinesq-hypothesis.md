---
type: Definition
title: "Boussinesq eddy-viscosity hypothesis"
description: "The linear closure that aligns the deviatoric Reynolds or subgrid stress with the strain rate through a scalar eddy viscosity; its RANS and LES forms and sign conventions, measured misalignment, the best-fit (optimal) eddy viscosity and its conditioning, and why one scalar viscosity cannot carry both mean stress and energy transfer."
status: established
aliases: [Boussinesq approximation, linear eddy-viscosity hypothesis, eddy-viscosity assumption, linear constitutive relation, stress-strain alignment]
tags: [eddy-viscosity, rans, sgs-model, les, data-driven]
timestamp: 2026-10-25T20:38:00Z
---

# Boussinesq eddy-viscosity hypothesis

The Boussinesq hypothesis closes the unresolved stress by a scalar eddy
viscosity $\nu_t$ acting on the strain rate, so that the deviatoric part of
the stress is aligned with the strain. In Reynolds-averaged form it reads

$$R_{ij}-\tfrac23k\,\delta_{ij}=-2\nu_t\langle S_{ij}\rangle ,$$

and in large-eddy simulation, for the subgrid stress
$\tau_{ij}=\overline{u_iu_j}-\bar u_i\bar u_j$,

$$\tau^d_{ij}=\tau_{ij}-\tfrac13\tau_{kk}\delta_{ij}=-2\nu_t\bar S^d_{ij}.$$

The isotropic part ($\tfrac23k\delta_{ij}$, or $\tfrac13\tau_{kk}\delta_{ij}$) is
either carried by a model for $k$ or absorbed into a modified pressure. All
the linear eddy-viscosity closures of this bundle are of this form and differ
only in how they compute $\nu_t$: the [Spalart–Allmaras model](/methods/spalart-allmaras-model.md)
from a transported $\tilde\nu$, the [$k$-$\omega$ SST model](/methods/k-omega-sst-model.md)
from $k$ and $\omega$, the [Smagorinsky model](/methods/smagorinsky-model.md)
from $\Delta$ and $\lvert\bar S\rvert$, the [Vreman model](/methods/vreman-model.md)
from the resolved velocity gradient.

## Forms in the sources

The sources print the same hypothesis with different signs, density weights
and treatments of the trace; translated to the registry they agree.

- **RANS, compressible.** Li & Liu (2022) write the Reynolds stress in the
  $-\rho\langle u_i'u_j'\rangle$ convention as
  $2\mu_t\big(S_{ij}-\tfrac13\partial_ku_k\delta_{ij}\big)-\tfrac23\rho k\delta_{ij}$
  ([Li & Liu (2022)](/sources/li-2022.md), Eq. 38), which is the registry form
  multiplied by $-\rho$ with the deviatoric strain.
- **PANS.** Dzanic et al. (2022) close the unresolved stress of
  [partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md)
  by the same relation with the unresolved eddy viscosity and the unresolved
  kinetic energy $f_kk$, added to the viscous stress (so with the opposite
  sign to the registry's stress), printed without $\rho$ on the kinetic energy
  and without the deviatoric projection of $S_{ij}$
  ([Dzanic et al. (2022)](/sources/dzanic-2022.md), §2.1, Eq. 7).
- **LES.** Agrawal et al. (2022) use the registry's positive-trace
  convention, $\tau^d_{ij}=-2\nu_t\bar S_{ij}$, with the isotropic part
  absorbed into the pressure ([Agrawal et al. (2022)](/sources/agrawal-2022.md),
  §II, Eqs. 2–4). Haering et al. (2022) define their subgrid stress with the
  opposite sign and write $+2\nu_{\mathrm{sgs}}\bar S_{ij}$ for it
  ([Haering et al. (2022)](/sources/haering-2022.md), §III, Eq. 3); Agdestein &
  Sanderse (2025) write the closure directly as the force
  $\nabla\cdot(2\nu_t\bar S)$ added to the filtered momentum equation
  ([Agdestein & Sanderse (2025)](/sources/agdestein-2025.md), §4.4.1, Eq. 26).
- **RANS, compressible, as a viscosity substitution.** Alauzet et al. (2022)
  write the RANS equations as the laminar ones with $\mu\to\mu+\mu_t$ and the
  conductivity $\lambda\to\lambda+\lambda_t$, $Pr_t=\mu_tc_p/\lambda_t=0.9$, so the
  total stress is $(\mu+\mu_t)\big(\partial_ju_i+\partial_iu_j-\tfrac23\partial_ku_k\delta_{ij}\big)$;
  the isotropic part $\tfrac23\rho k\delta_{ij}$ is absent, as it must be for
  the Spalart–Allmaras closure they use
  ([Alauzet et al. (2022)](/sources/alauzet-2022.md), §2.1, Eq. 1).
- **Variable-density PANS.** Pereira et al. (2021) close the unresolved stress
  of their [PANS](/methods/partially-averaged-navier-stokes.md) BHR model as
  $2\nu_u\{S_{ij}\}-\tfrac23k_u\delta_{ij}$, with $\{\cdot\}$ their
  density-weighted resolved field and $\nu_u$ the unresolved eddy viscosity:
  the registry form with the opposite sign, i.e. in the
  $-\langle u_i'u_j'\rangle$ convention. The eddy viscosity is built from
  the unresolved energy and a transported length scale rather than from $k$
  and $\varepsilon$ or $\omega$
  ([Pereira et al. (2021)](/sources/pereira-2021.md), §III, Eqs. 5–6).
- **LES viscosity in an artificial-viscosity flux.** Mateo-Gabín et al. (2022)
  add a Smagorinsky viscosity to the molecular one ("Boussinesq's
  approximation", §2) and carry it as the viscosity of an artificial
  Navier–Stokes flux; its dissipation in kinetic-energy entropy variables is
  non-negative by construction (§2.2.1, Eq. 25), which in registry notation is
  $2\mu_aS^d_{ij}S^d_{ij}\ge0$ with $\mu_a$ the added viscosity *(compiler
  check, not in the sources: the printed $\mu_a\big(2\lvert\mathsf S\rvert^2-\tfrac23(\partial_ku_k)^2\big)$
  equals this when the source's $\lvert\mathsf S\rvert^2$ is read as
  $S_{ij}S_{ij}$, which the paper does not define)*
  ([Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md), §2, §2.2.1, §6.1;
  see [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)).
- **RANS, written on the anisotropy.** McConkey et al. (2022) state the
  hypothesis for the deviatoric (anisotropy) part only, $2kb_{ij}\approx-2\nu_t\langle S_{ij}\rangle$
  (the registry form), with $\tfrac23k$ absorbed into a modified pressure.
  They reject the variant $R_{ij}\approx-2\nu_t\langle S_{ij}\rangle$, used in
  the cited works of Liu et al. and Brener et al., as a basis for a best-fit
  eddy viscosity, because $R_{ii}=2k$ while $\langle S_{ii}\rangle=0$
  ([McConkey et al. (2022)](/sources/mcconkey-2022.md), §II, Eqs. 3–4).
  Cato et al. (2023) write $-R_{ij}=2\nu_t\langle S_{ij}\rangle-\tfrac23k\delta_{ij}$
  with the operator $\nabla_s=\nabla+\nabla^{\top}$ (twice the symmetric
  gradient), the registry form with the sign moved across, and also absorb
  the $k$ term into the pressure
  ([Cato et al. (2023)](/sources/cato-2023.md), §II A).
- **LES, wall-bounded.** Kim et al. (2022) close the deviatoric subgrid stress
  of their comparison models as $\tau^d_{ij}=-2\nu_t\bar S_{ij}$, the registry
  form ([Kim et al. (2022)](/sources/kim-2022.md), §II, comparison models).

### A traceless Reynolds stress

A model that carries no $k$, such as Spalart–Allmaras, supplies only the
deviatoric term, so its modelled Reynolds stress has zero trace. Li & Liu
(2022) note that in SA and in SA with the 2000 quadratic constitutive
relation $R_{kk}$ vanishes identically, so the anisotropy tensor $b_{ij}$
cannot be formed. The 2013 version of the relation adds an isotropic term
$\propto\nu_t\lvert S^d\rvert\delta_{ij}$ that "acts similarly" to the
missing $\tfrac23k\delta_{ij}$ ([Li & Liu (2022)](/sources/li-2022.md), §2.3,
Eqs. 26–27; §4.2, Eqs. 35, 38; details on the
[Spalart–Allmaras page](/methods/spalart-allmaras-model.md)).

### Normal stresses reconstructed from the hypothesis

A Boussinesq model fixes all six stress components from $k$, $\nu_t$ and
the mean strain, so its normal stresses are $\tfrac23k-2\nu_t\langle S_{\alpha\alpha}\rangle$
(no sum). François et al. (2022) reconstruct RMS velocities in this way from
$k$-$\omega$ SST and Smith $k$-$l$ RANS of a turbofan fan stage and compare
them with hot-wire data between fan and vanes: the RANS RMS profiles show
"larger discrepancies" than zonal detached-eddy simulation and the wrong
profile shape in the tip-gap region, and the RANS wakes are narrower
([François et al. (2022)](/sources/francois-2022.md), §5.3–5.4, Figs. 13, 15;
the relation itself is not printed).

## Where it sits among the modelling assumptions

Duraisamy et al. (2019) classify the choice of representation of the
Reynolds stress in terms of the mean variables (linear eddy viscosity,
algebraic stress models) as the second of four layers of RANS assumptions,
and the value of $C_\mu$ in two-equation linear models as "a classical L4
closure issue", i.e. a coefficient choice
([Duraisamy et al. (2019)](/sources/duraisamy-2019.md), §2; see
[model-form uncertainty](/definitions/model-form-uncertainty.md)). If the
Reynolds stress depends only on the local mean velocity gradient, the
Cayley–Hamilton theorem gives an exact finite basis: the anisotropy is a
combination $b_{ij}=\sum_ng^{(n)}T^{(n)}_{ij}$ of the ten integrity-basis
tensors of Pope (1975), as recalled by Duraisamy et al. (2019, §2, §5.3,
Eq. 11) and Duraisamy (2021, §III.A, Eq. 4). The Boussinesq hypothesis keeps
only the first term, $T^{(1)}\propto S_{ij}$; the
[tensor-basis neural network](/methods/tensor-basis-neural-network.md) and
the quadratic constitutive relation of the SA page add higher terms.

Haering et al. (2022) derive the scalar eddy viscosity from a
gradient-diffusion argument: a flux $\langle u_i'\phi'\rangle$ is modelled
from the displacement of fluid particles over a decorrelation time $T_\phi$,
which under isotropy gives $\nu_\phi=C\,k_cT_\phi$ with $k_c$ the energy of
the convecting fluctuations ([Haering et al. (2022)](/sources/haering-2022.md),
§III B, Eqs. 12–14). The LES version holds only in expectation.

## Limits of a single scalar eddy viscosity

**Misalignment.** Agrawal et al. (2022) build their model on the statement
that the alignment of the subgrid stress with the resolved strain is invalid
locally, as a priori analyses of DNS show; they quote the a priori
misalignment results of Bardina et al. and of Meneveau & Liu as recalled in
their introduction. On filtered channel DNS at $Re_\tau=395$ and $2000$ their
non-Boussinesq [dynamic tensor-coefficient Smagorinsky model](/methods/dynamic-tensor-coefficient-smagorinsky-model.md)
correlates better with the exact stress than the dynamic Smagorinsky model,
most of all near the wall, while the two models have identical dissipation
correlations, because only the isotropic part of the coefficient tensor
dissipates ([Agrawal et al. (2022)](/sources/agrawal-2022.md), §V, Figs. 1–2).
The authors add that these correlations do not measure alignment.

**Mean stress against energy transfer.** Haering et al. (2022) argue that
one scalar eddy viscosity cannot represent both the mean subgrid stress and
the mean energy transfer to the subgrid scales. The first is the mean of the
stress; the second is governed by the correlation between stress and
resolved strain, which in filtered turbulence is "of order 20% or less" but
equals one, or nearly so, for an eddy-viscosity model. Getting the transfer
right therefore requires a smaller viscosity than getting the stress right.
As recalled from Jiménez & Moser, the dynamic Smagorinsky model gives
channel-flow subgrid stresses "nearly five times smaller than the true
filtered stress" ([Haering et al. (2022)](/sources/haering-2022.md), §II B,
pp. 5–6). They derive the split
$\tau^d_{ij}=-2\nu_s\langle\bar S_{ij}\rangle-2\nu_e\bar S'_{ij}$, with
$\bar S'_{ij}=\bar S_{ij}-\langle\bar S_{ij}\rangle$ the resolved fluctuating
strain and two non-fluctuating viscosities of different magnitude and conclude that
"$\tau^d_{ij}=-2\nu_t\bar S_{ij}$ is not generally valid" (§III B, Eqs.
20–24; see [active model split](/methods/active-model-split.md)).

**Correlation is gauge-dependent.** Vela-Martín (2022) shows that the
subgrid stress is defined only up to an added symmetric divergence-free
tensor, which leaves the resolved dynamics and the mean flux $\langle\Pi\rangle$
unchanged but changes the local flux $\Pi$. The eddy viscosity that
reproduces the local flux exactly,

$$\nu_t^{\mathrm{opt}}=\frac{\Pi}{\lvert\bar S\rvert^2},$$

(the registry translation of the author's
$\tau_{ij}\bar S_{ij}/(2\bar S_{ij}\bar S_{ij})$, whose stress has the
opposite sign) is negative over a large fraction of the domain for the
author's "standard" stress $\overline{u_iu_j}-\bar u_i\bar u_j$ (up to sign) but positive almost everywhere for the stress
representation that minimises the flux variance: a purely dissipative
eddy viscosity that reproduces the local energy exchange exists, in the
flux sense ([Vela-Martín (2022)](/sources/velamartin-2022.md), §7.1, Eqs.
7.2–7.5). Equivalent representations correlate only about 0.6 to 0.4 with
each other (all components, filter scales $\ell/L=0.64$ to $0.08$), so a
poor a priori correlation of a model with the stress $\overline{u_iu_j}-\bar u_i\bar u_j$ "is not
necessarily an indication of poor modelling" (§6.3, §8). The conclusions
are limited to isotropic turbulence away from walls (§8). See
[energy backscatter](/definitions/energy-backscatter.md).

**Alignment measured in wall turbulence.** Kim et al. (2022) measure the
misalignment directly in filtered channel DNS at $Re_\tau=180$ (cut-off
filter, grid $\Delta x^+=70.7$, $\Delta z^+=35.3$), through the angle
between $-\tau^d_{ij}$ and $\bar S_{ij}$, which a linear eddy-viscosity model
fixes at zero (§III E, Eq. 27, Fig. 18):

$$\cos\vartheta=\frac{-\tau^d_{ij}\bar S_{ij}}{\sqrt{\tau^d_{kl}\tau^d_{kl}}\,\sqrt{\bar S_{mn}\bar S_{mn}}},$$

with $\vartheta$ the page-local angle (in incompressible flow the numerator
is the local flux $\Pi$ *(compiler check, not in the sources)*).

- In the filtered DNS the mean angle is near $\pi/2$ at all heights, and the
  authors compare its PDF with that of two random trace-free symmetric
  tensors; a reinforcement-learned tensor model has its peak near 0.3 rad at
  the wall moving towards $\pi/2$ away from it (Fig. 18).
- The correlation between $\bar S_{xy}$ and $-\tau_{xy}$ is $-0.20$ at
  $y^+\approx15$ and $0.19$ at $y^+\approx50$ in the filtered DNS, against
  0.95 and 0.94 for the dynamic Smagorinsky model and 0.34 and 0.58 for the
  learned model (Table IV).
- The ratio of the eigenvalues of $-\tau^d_{ij}$ and $\bar S_{ij}$ (twice a
  plane-averaged eddy viscosity) is "one order of magnitude larger" in the
  filtered DNS than in every model, while the models differ little from
  each other (Fig. 20).
- The variant of the learned model constrained to the eddy-viscosity form
  overpredicts the mean velocity in the buffer and log layers, like the
  dynamic Smagorinsky model, while the tensor-output variants match the
  filtered DNS. The authors conclude that "the eddy-viscosity assumption
  could seriously limit the performance" and that "the non-alignment nature
  between $-\tau^*_{ij}$ and $\bar S_{ij}$, rather than the level of eddy
  viscosity" matters more (§III C, Fig. 7a; §III E; §IV). Details on
  [reinforcement-learning closures](/methods/reinforcement-learning-closure.md).

**Alignment in RANS.** Cato et al. (2023) use Schmitt's alignment indicator,
in registry notation (page-local $c_{RS}$)

$$c_{RS}=\frac{\lvert R_{ij}\langle S_{ij}\rangle\rvert}{\sqrt{R_{kl}R_{kl}}\sqrt{\langle S_{mn}\rangle\langle S_{mn}\rangle}},$$

with $R_{ij}$ in the source's traceless form, so that $c_{RS}=1$ when the
hypothesis is "totally respected" and $0$ for orthogonal tensors (§III C,
Eq. 21). Plotted where $k>0.1k_{\max}$, it falls below 0.8 near the wall
behind the bump of a converging–diverging channel, "in much of the domain
below $y/h=1$" of the periodic hill at bulk $Re=2800$, and is above 0.8 only
in "a few areas" around a square cylinder at $Re=22\,000$ (Figs. 7, 8, 12).
Yet corrections that stay within the hypothesis (a source in the SA
equation) reproduce the DNS mean velocity in all three flows nearly as
well as a free momentum forcing; the authors conclude that "missing the
proper stress alignment does not play a large role for predicting the mean
flow" (§IV B; §V B; see
[field inversion](/methods/field-inversion-machine-learning.md)). They also
show that the mean flow can be accurate while the Reynolds stresses are
wrong, "as long as the Reynolds force vector is correctly represented"
(§V C, Figs. 16–19).

**Locality.** Seyedi & Zayernouri (2022) recall that the hypothesis assumes
the stress proportional to the *local* mean velocity gradient, that
Bradshaw (1973) showed it to fail over curved surfaces, and that Hinze et
al. (1974) found a strongly non-uniform eddy viscosity in the outer layer
downstream of a wall-mounted cap; they take these as motivation for
nonlocal closures such as the
[fractional subgrid-scale model](/methods/fractional-sgs-model.md)
([Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md), §I, pp. 2–3).

## The best-fit eddy viscosity

If a reference stress is known, the scalar $\nu_t$ that brings the
Boussinesq form closest to it in the least-squares sense is the projection
of the stress on the strain. Wu et al.'s optimal eddy viscosity, as
recalled by McConkey et al. (2022, §II A, Eqs. 5–6), is in registry
notation

$$\nu_t^{*}=\arg\min_{\nu_t}\big\lVert 2kb_{ij}+2\nu_t\langle S_{ij}\rangle\big\rVert=-\frac{2k\,b_{ij}\langle S_{ij}\rangle}{\lvert\langle S\rangle\rvert^2},$$

with $\nu_t^*$ page-local. Cato et al. (2023) estimate a DNS eddy viscosity
with the same projection (§III B, Eq. 18, after Volpiani et al.), which in
registry notation is the same expression *(compiler check, not in the
sources)*, and call it "a good approximation for attached flows" whose
injection into RANS "does not guarantee a perfect mean field". The LES
counterpart is the flux-matching $\nu_t^{\mathrm{opt}}=\Pi/\lvert\bar S\rvert^2$
of Vela-Martín above, the same projection applied to the deviatoric subgrid
stress *(compiler check, not in the sources)*.

**Non-negative optimum.** $\nu_t^*$ is negative where $b_{ij}$ and
$\langle S_{ij}\rangle$ are poorly aligned, which destabilizes an implicit
treatment. McConkey et al. (2022) therefore define the non-negative least
squares fit (page-local $\nu_t^{\dagger}$)

$$\nu_t^{\dagger}=\arg\min_{\nu_t\ge0}\big\lVert 2kb_{ij}+2\nu_t\langle S_{ij}\rangle\big\rVert ,$$

computed cell by cell, and split the anisotropy into a linear and a
remainder part, $2kb_{ij}=-2\nu_t^{\dagger}\langle S_{ij}\rangle+a^{\perp}_{ij}$
(page-local $a^{\perp}$; §II A–B, Eqs. 7, 9), which they call
"proportional/orthogonal". For a single scalar unknown the constrained
minimizer is $\max(0,\nu_t^*)$, and $a^{\perp}_{ij}\langle S_{ij}\rangle=0$ holds
only where the constraint is inactive *(compiler check, not in the
sources)*. They claim to be "the first to propose a stability constraint on
the optimal eddy viscosity" (§I).

**How good is the best fit.** On the parametrized periodic hill (Xiao et
al. DNS, $Re_h=5600$, steepness factor 1.2), even the DNS-optimal $\nu_t^*$
or $\nu_t^\dagger$ leaves errors "on the order of 100%" in all components of
the anisotropy and does not improve substantially on the baseline RANS
anisotropy; the linear fit fails during separation, with $b_{yy}$ errors at
reattachment and the largest $b_{xy}$ errors in the acceleration over the
next hill (local $R^2$ and Thompson et al.'s fit factor; §II B, Figs. 1–3).
Injected alone into RANS, the DNS-derived $\nu_t^\dagger$ is the "upper limit"
of a linear closure and still leaves significant velocity errors at
separation and reattachment (RMSE of $U$ $1.672\times10^{-3}$ m/s; Fig. 4).

**Conditioning.** Injecting the DNS anisotropy fully explicitly gives an
RMSE of $U$ of $2.613\times10^{-3}$ m/s; treating $\nu_t^\dagger$ implicitly
(added to the molecular viscosity) and only $a^\perp$ explicitly gives
$2.265\times10^{-4}$ m/s, "an order of magnitude" smaller, although the
authors note that the explicit run needed first-order schemes for stability
(§II C, Figs. 5–6). They recommend that every injection framework report
the error left after a perfect closure prediction. With learned
$\nu_t^\dagger$ and $a^\perp$ the converged velocity errors are smaller than the
closure errors: "the RANS equations can suppress rather than amplify errors
in the closure prediction" (§IV B, Fig. 20; see
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md),
[model-consistent training](/methods/model-consistent-training.md) and
[tensor-basis neural network](/methods/tensor-basis-neural-network.md)).

**Bypassing the hypothesis.** Eivazi et al. (2022) avoid any eddy-viscosity
relation: a [physics-informed neural network](/methods/physics-informed-neural-network.md)
outputs the mean velocity, pressure and Reynolds-stress components directly
and is closed by Reynolds-stress data on the domain boundaries instead of a
constitutive model ([Eivazi et al. (2022)](/sources/eivazi-2022.md), §1–§2).

**Consistency of the inputs.** Duraisamy (2021) warns that a feature such
as $\langle S_{ij}\rangle k/\varepsilon$ evaluated from DNS need not equal the same
feature built from a RANS model's $k$ and $\varepsilon$, which play an
operational role ([Duraisamy (2021)](/sources/duraisamy-2021.md), §IV.A);
Duraisamy et al. (2019) make the same point for the dissipation rate
([Duraisamy et al. (2019)](/sources/duraisamy-2019.md), §5.4).

## Qualifications

- Haering et al. (2022) and Vela-Martín (2022) read low stress–strain
  correlations differently. Haering et al. take the correlation of the
  filtered stress with the strain as a property the model's energy transfer
  must match; Vela-Martín shows that this correlation changes with the
  gauge of the stress and that a perfectly flux-matching eddy viscosity
  exists. Haering et al. argue about the mean stress of wall-bounded
  hybrid simulations; Vela-Martín restricts the conclusion to the local
  flux in isotropic turbulence away from walls (§8). No source of this
  bundle compares the two readings in one flow.
- Duraisamy et al. (2019) print the integrity-basis expansion for the full
  Reynolds stress without an isotropic term (§5.3, Eq. 11), while Duraisamy
  (2021) writes it for the anisotropy with the $\tfrac13I$ term separate
  (§III.A, Eq. 4).
- Kim et al. (2022) and Cato et al. (2023) weigh misalignment differently:
  Kim et al. find the eddy-viscosity form limiting for a pointwise learned
  subgrid model in LES; Cato et al. find a misaligned but
  Boussinesq-constrained RANS model able to reproduce the mean flow once a
  free spatial correction field is optimized against dense DNS velocity
  data of the same flow (§II B, §VII). The settings differ (an a posteriori
  LES closure against an assimilated RANS correction), and no source of this
  bundle tests both in one flow.
- McConkey et al.'s stress-optimal $\nu_t^\dagger$, injected alone, leaves
  large velocity errors on the periodic hill at $Re_h=5600$ (§II B, Fig. 4),
  while Cato et al.'s velocity-optimized corrections $\beta$, $f_{\tilde\nu}$
  and $g_{\tilde\nu}$ reach the DNS velocity in the converging–diverging
  channel with eddy viscosities that "very strongly overshoot" the
  stress-based estimate of their Eq. 18 (§III B, Fig. 6); the eddy-viscosity
  multiplier there stays "pretty much in agreement" with that estimate
  (Fig. 6f). Both sources thus separate the viscosity that fits the stress
  from the one that fits the mean velocity, in different flows; see
  [model-form uncertainty](/definitions/model-form-uncertainty.md).
- Cato et al. attribute to Schmitt the threshold $c_{RS}>0.86$ for Boussinesq
  validity but draw and discuss 0.8 throughout (§III C, §V A). They print the
  reference stress of their Eq. 9 as $-\nabla\cdot(\cdot)+\tfrac23k\mathbf I$,
  a divergence added to a tensor; the reading consistent with their
  $\mathbf R^{DA}$ of the same equation and the Boussinesq form of §II A,
  which §V C calls "the traceless Reynolds stress tensor", drops the
  divergence *(compiler check, not in the sources)*.

# Citations

- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §I, §II Eqs. 2–5, §V Figs. 1–2, App. C.
- [Li & Liu (2022)](/sources/li-2022.md) — §2.3 Eqs. 23–27, §4.2 Eqs. 35–38.
- [Vela-Martín (2022)](/sources/velamartin-2022.md) — §3, §6.3, §7.1 Eqs. 7.2–7.5, §8.
- [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md) — §4.4.1, Eqs. 26–27.
- [Duraisamy et al. (2019)](/sources/duraisamy-2019.md) — §2 (L2, L4), §5.3 Eq. 11, §5.4.
- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §III.A Eq. 4, §IV.A.
- [Haering et al. (2022)](/sources/haering-2022.md) — §II B, §III Eqs. 3–8, §III B Eqs. 12–24.
- [Dzanic et al. (2022)](/sources/dzanic-2022.md) — §2.1, Eq. 7.
- [Alauzet et al. (2022)](/sources/alauzet-2022.md) — §2.1, Eq. 1.
- [Pereira et al. (2021)](/sources/pereira-2021.md) — §III, Eqs. 5–6.
- [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md) — §2, §2.2.1 Eq. 25, §6.1.
- [François et al. (2022)](/sources/francois-2022.md) — §5.3–5.4, Figs. 13, 15.
- [McConkey et al. (2022)](/sources/mcconkey-2022.md) — §I, §II Eqs. 3–9, §II A–C Figs. 1–6, §IV B Fig. 20 (arXiv v1).
- [Kim et al. (2022)](/sources/kim-2022.md) — §II, §III C Fig. 7, §III E Eq. 27 Table IV Figs. 18, 20, §IV (arXiv v2).
- [Cato et al. (2023)](/sources/cato-2023.md) — §II A, §III B Eq. 18 Fig. 6, §III C Eq. 21 Fig. 7, §IV B Fig. 8, §V A–C Figs. 12, 16–19 (HAL v2).
- [Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md) — §I, pp. 2–3 (arXiv v3).
- [Eivazi et al. (2022)](/sources/eivazi-2022.md) — §1–§2 (arXiv v1).
