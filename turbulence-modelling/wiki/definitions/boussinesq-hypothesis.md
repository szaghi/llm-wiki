---
type: Definition
title: "Boussinesq eddy-viscosity hypothesis"
description: "The linear closure that aligns the deviatoric Reynolds or subgrid stress with the strain rate through a scalar eddy viscosity; its RANS and LES forms and sign conventions, measured misalignment, anisotropy slaved to the strain, the best-fit eddy viscosity, explicit non-linear extensions and their conditioning, and why one scalar viscosity cannot carry both mean stress and energy transfer."
status: established
aliases: [Boussinesq approximation, linear eddy-viscosity hypothesis, eddy-viscosity assumption, linear constitutive relation, stress-strain alignment]
tags: [eddy-viscosity, rans, sgs-model, les, data-driven]
timestamp: 2026-10-27T15:55:00Z
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
  $2\nu_t\tilde S_{ij}-\tfrac23k_u\delta_{ij}$, with the tilde the
  density-weighted resolved field and $\nu_t$ the unresolved eddy viscosity
  (the source's $\{\cdot\}$ and $\nu_u$):
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
  Sirignano & MacArt (2023) write the same deviatoric form for their
  dynamic Smagorinsky and anisotropic-minimum-dissipation baselines, the
  isotropic part absorbed into the pressure projection, while their learned
  closure returns a full $3\times3$ stress from the filtered velocity
  gradient and is not of eddy-viscosity form
  ([Sirignano & MacArt (2023)](/sources/sirignano-2023.md), §2.1, §3.2,
  Eq. 3.3; see [neural-network SGS models](/methods/neural-network-sgs-model.md)).
- **RANS, incompressible, with a non-linear remainder.** Tang et al. (2023)
  use the registry convention, $R_{ij}=\tfrac23k\delta_{ij}-2\nu_t\langle S_{ij}\rangle$
  with $\nu_t=C_\mu k^2/\varepsilon$, and add a learned non-linear term
  (below) ([Tang et al. (2023)](/sources/tang-2023.md), §II A–C, Eqs. 3, 9;
  arXiv v1).
- **RANS, compressible, as a viscosity sum.** Zhao et al. (2023b) write the
  total viscosity as $\mu=\mu_L+\mu_T$, with $\mu_L$ from Sutherland's law
  and $\mu_T$ from the [SST model](/methods/k-omega-sst-model.md), in the
  viscous flux of a discontinuous Galerkin RANS solver
  ([Zhao et al. (2023b)](/sources/zhao-2023-b.md), §2, Eq. 2-1).
- **LES, acting on the small scales only.** In the projection-based
  variational multiscale form tested by Lederer et al. (2023), the eddy
  viscosity of the [WALE model](/methods/wale-model.md) acts only on the
  small resolved scales: the stress is $2\big((\nu+\nu_t)\bar S_{ij}-\nu_tg_{ij}\big)$
  with $g_{ij}$ (page-local) the $L^2$ projection of the strain onto
  element-wise symmetric polynomials of degree $m$; a zero projection space
  recovers classical LES and a large enough $m$ removes the model
  ([Lederer et al. (2023)](/sources/lederer-2023.md), §3.1, Eqs. 10–14;
  arXiv v1; the source writes $\epsilon(u)$ for the strain). The sign is
  that of a stress added to the viscous one, opposite to the registry's
  $\tau_{ij}$.

- **RANS, compressible, zero-equation, with an eddy conductivity.** Chen
  et al. (2024) close the Favre-averaged Reynolds stress
  $\langle\rho u_i''u_j''\rangle$ by a scalar $\mu_t$ in the viscosity-sum form
  and the turbulent heat flux by an eddy conductivity $c_p\mu_t/Pr_t$, both
  from the algebraic [Baldwin–Lomax model](/methods/baldwin-lomax-model.md);
  they note that algebraic models cannot represent Reynolds–Favre
  differences ([Chen et al. (2024)](/sources/chen-2024.md), §2.1, Eq. 2.1).
  Their DNS diagnostic of $\mu_t$ is the projection
  $-\langle\rho u''v''\rangle/\partial_y\langle u\rangle_\rho$ (§2.3), and the
  gradient-diffusion analogue for heat fails near the temperature peak of
  cold-wall boundary layers, where the turbulent Prandtl number becomes
  negative or singular (§3.3; see
  [Morkovin's hypothesis](/definitions/morkovin-hypothesis.md)).
- **LES, with a viscosity derived from the resolved transfer.** Domaradzki
  (2024) applies the Boussinesq form to the unfiltered LES field with an
  eddy viscosity computed, at each step and with no adjustable constant,
  from the dissipation of a similarity-type stress of the resolved field,
  filtered once more for stability: in registry sign, the flux-matching
  viscosity $\nu_t^{\mathrm{opt}}$ below applied to the similarity stress
  ([Domaradzki (2024)](/sources/domaradzki-2024.md), §2.4, Eq. 2.47; see
  [autonomous eddy-viscosity model](/methods/autonomous-eddy-viscosity-model.md)).
  Pointwise inversion without the second filtering "will cause numerical
  instabilities" because the flux changes sign; with it, regions of negative
  viscosity (backscatter) remain and no instability appeared (§2.4, §3.1).
- **LES, comparison baseline of a learned model.** Kim et al. (2024) close
  the deviatoric subgrid stress of their dynamic Smagorinsky baseline in the
  registry form, while their neural networks predict the stress components
  directly ([Kim et al. (2024)](/sources/kim-2024.md), §1; see
  [neural-network SGS models](/methods/neural-network-sgs-model.md)).
- **PANS on a dynamic resolution parameter.** Petrocchi & Barakos (2024)
  recall that PANS inherits the Boussinesq form with an eddy viscosity
  reduced through $f_k$ ([Petrocchi & Barakos (2024)](/sources/petrocchi-2024.md),
  §2; see [PANS](/methods/partially-averaged-navier-stokes.md)).
- **Hybrid RANS/LES, Favre form with the modelled energy only.** Möller et
  al. (2024) write the Favre-averaged stress of their transitional DDES in
  the $-\langle\rho u_i''u_j''\rangle$ convention as $\mu_t$ times twice the
  deviatoric strain of the Favre-averaged velocity minus
  $\tfrac23\langle\rho\rangle k\delta_{ij}$, with $k$ the *modelled* part of
  the kinetic energy (the source's $k_{\mathrm{mod}}$; the resolved part is
  carried by the grid): the registry form multiplied by $-\rho$
  ([Möller et al. (2024)](/sources/moller-2024.md), §II.A, Eq. 13; accepted
  manuscript; see [detached-eddy simulation](/methods/detached-eddy-simulation.md)).
- **RANS, compressible Spalart–Allmaras, as a stress added to the viscous
  one.** Fanizza et al. (2025) add
  $\mu_t\big(\nabla\boldsymbol u+\nabla\boldsymbol u^{\top}-\tfrac23(\nabla\cdot\boldsymbol u)\mathbf I\big)$
  to the viscous stress, with no isotropic $k$ term, the model carrying no
  $k$; the turbulent heat flux is the matching eddy conductivity with
  $Pr_t=0.9$ ([Fanizza et al. (2025)](/sources/fanizza-2025.md), §2.1).
- **LES, viscous and subgrid stresses together.** Mukha et al. (2025) write
  one stress $(\nu+\nu_t)(\partial_j\bar u_i+\partial_i\bar u_j)$ for both,
  their strain tensor printed without the factor $\tfrac12$ and entering the
  momentum equation as $+\partial_j(\cdot)$: in registry terms
  $\tau^d_{ij}=-2\nu_t\bar S_{ij}$ with the sign of a stress added to the
  viscous one ([Mukha et al. (2025)](/sources/mukha-2025.md), §II.A,
  Eqs. 2–3; arXiv v1; see [wall-modelled LES](/methods/wall-modelled-les.md)).
- **URANS with volume penalization, as a gradient closure.** Llorente
  (2024) closes the Reynolds stress of penalized URANS as
  $-\langle u_i'u_j'\rangle=\nu_t\partial_j\langle u_i\rangle$ (the source writes
  the Reynolds average as an overbar and calls the left side $R_{ij}$, with
  the sign opposite to the registry's), i.e. in registry notation
  $R_{ij}=-\nu_t\partial_j\langle u_i\rangle$: the velocity gradient in place of
  $2\langle S_{ij}\rangle$ and no $\tfrac23k\delta_{ij}$
  ([Llorente (2024)](/sources/llorente-2024.md), p. 4, carried into the
  total tensor of Eqs. 3–4; author accepted manuscript; see
  [immersed boundary methods](/methods/immersed-boundary-method.md)). For
  incompressible flow and uniform $\nu_t$ the divergence of this stress
  equals that of $-2\nu_t\langle S_{ij}\rangle$, because
  $\partial_j\partial_i\langle u_j\rangle=0$; for a variable $\nu_t$ they differ
  *(compiler check, not in the sources)*. See Qualifications.
- **A feature built on the hypothesis.** Wu et al. (2025) compute the
  production-to-dissipation feature $P_k/\varepsilon$ of their learned
  correction from the Boussinesq Reynolds stress of the
  [SST model](/methods/k-omega-sst-model.md)
  ([Wu et al. (2025)](/sources/wu-2025.md), §2.2, Table 2; authors'
  manuscript).

- **RANS, incompressible, with the viscous stress included.** Elzaabalawy
  et al. (2023) write $2\nu_eS_{ij}-\tfrac23k\delta_{ij}$ with
  $\nu_e=\nu+\nu_t$ as one "modeled Reynolds stress" that already contains
  the molecular stress: the registry form with the opposite sign plus the
  viscous term, the $\tfrac23k$ being absorbed into a modified pressure in
  their first-order form, where the auxiliary unknown is $2S_{ij}$
  ([Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md), §2, Eqs.
  3–8; see the [Wilcox $k$-$\omega$ page](/methods/k-omega-model.md)).
- **RANS, compressible, with limited inputs.** Ghidoni et al. (2026) write
  the turbulent stress as
  $2\bar\mu_t\big(S_{ij}-\tfrac13\partial_ku_k\delta_{ij}\big)-\tfrac23\rho\bar k\delta_{ij}$
  and the total stress as the viscous one plus this term, i.e. the
  $-\rho\langle u_i''u_j''\rangle$ convention, with $\bar k=\max(0,k)$ and an
  eddy viscosity built from $\bar k$ and a floored $\omega$, so that a
  negative $k$ of the high-order solution never enters the stress
  ([Ghidoni et al. (2026)](/sources/ghidoni-2026.md), §2, Eq. 1; the bars
  of the source denote these limited values, not filtering).
- **Hybrid RANS/LES, as the LES target.** Wang et al. (2021) take the
  Boussinesq subgrid stress $2\bar\rho\nu_t\tilde S_{ij}-\tfrac23\bar\rho k\delta_{ij}$
  (the opposite sign to the registry's) with the Smagorinsky viscosity as
  the LES branch that their detached-eddy construction must reproduce under
  equilibrium; in the LES region of their Reynolds-stress-based IDDES the
  transported Reynolds stress itself acts as the subgrid stress, with no
  Boussinesq closure ([Wang et al. (2021)](/sources/wang-2021-l.md), §2.3,
  Eqs. 6–10; see [detached-eddy simulation](/methods/detached-eddy-simulation.md)).
- **URANS against resolved stresses.** Yang & Ma (2022) compare the
  Boussinesq stress of SST URANS,
  $\mu_t(\partial_ju_i+\partial_iu_j)-\tfrac23(\rho k+\mu_t\partial_ku_k)\delta_{ij}$
  in the $-\rho\langle u_i'u_j'\rangle$ convention, with the resolved
  stress $-\rho\langle u_i'u_j'\rangle$ of a DES, the modelled part of the
  DES being left out ([Yang & Ma (2022)](/sources/yang-2022-b.md), §3.2,
  Eqs. 8–9).
- **RANS, compressible, two-equation, with the isotropic part kept.**
  Vandenhoeck et al. (2022) and Jiang et al. (2025) both write the modelled
  stress as $\mu_t\big(2S_{ij}-\tfrac23\partial_ku_k\delta_{ij}\big)-\tfrac23\rho k\delta_{ij}$,
  the $-\rho\langle u_i''u_j''\rangle$ convention, for the log-$\omega$
  [SST model](/methods/k-omega-sst-model.md) and for the
  $k$-$\sqrt kL$ model behind
  [scale-adaptive simulation](/methods/scale-adaptive-simulation.md)
  ([Vandenhoeck et al. (2022)](/sources/vandenhoeck-2022.md), §1.1, Eqs.
  9–10; [Jiang et al. (2025)](/sources/jiang-2025.md), App. A, Eq. A2).
  Vandenhoeck et al. add it to the viscous stress and carry the energy
  exchange $-\rho P_k+\beta^*\rho k\omega$ in the energy equation, with a
  pressure computed from a total energy that excludes $k$ (Eqs. 3, 7);
  Jiang et al. put only $(\mu+\mu_t)$ times the deviatoric strain into the
  momentum flux (Eq. 6) and use the full stress, with $\tfrac23\rho k$, in
  the production (Eq. A2).
- **RANS, incompressible, without the isotropic part.** Tomboulides et al.
  (2025) write the momentum equation with
  $(\mu+\mu_t)\big(2S_{ij}-\tfrac23\partial_ku_k\delta_{ij}\big)$ and call
  $2\mu_tS_{ij}$ the turbulent stress, for their
  [$k$-$\tau$ model](/methods/k-tau-model.md); the
  $-\tfrac23\rho k\delta_{ij}$ part is absent from the printed equation, and
  the paper does not say whether it is absorbed into the pressure
  ([Tomboulides et al. (2025)](/sources/tomboulides-2025.md), §2, Eqs. 1–4).
  Monfaredi et al. (2021) write the same total stress,
  $(\mu+\mu_t)\big(\partial_mv_k+\partial_kv_m-\tfrac23\delta_{km}\partial_\ell v_\ell\big)$,
  in compressible Spalart–Allmaras URANS, also without a
  $-\tfrac23\rho k\delta_{ij}$ term ([Monfaredi et al. (2021)](/sources/monfaredi-2021.md),
  §2.1, Eqs. 1–2; source's $v_k$ the velocity).
- **RANS, compressible Spalart–Allmaras, with an eddy conductivity.**
  Lodares et al. (2022) write the total stress as
  $(\mu+\mu_t)\big(2S_{ij}-\tfrac23\partial_ku_k\delta_{ij}\big)$ and the heat
  flux with $\kappa+\kappa_t$ at constant $Pr_t$, "normally set to 0.9" (page-local
  conductivities $\kappa$, $\kappa_t$, not the von Kármán constant), the
  viscosity-sum form of Alauzet et al. above; their entropy analysis needs
  non-negative viscosity and conductivity, which the clipped eddy
  viscosity $\mu_t=\max(\rho\tilde\nu,0)f_{v1}$ guarantees
  ([Lodares et al. (2022)](/sources/lodares-2022.md), §2, Eqs. 9–13, §3.1;
  see [entropy conservation](/properties/entropy-conservation.md)).
- **LES, compressible, with a modelled trace.** Volpiani (2024) closes the
  deviatoric subgrid stress as
  $-2\bar\rho\nu_t\big(\tilde S_{ij}-\tfrac13\tilde S_{kk}\delta_{ij}\big)$,
  the registry's positive-trace convention in Favre form, and models the
  trace separately after Yoshizawa, $\tau_{kk}=2C_I\bar\rho\Delta^2\lvert\tilde S\rvert^2$
  with $C_I=0.0066$ (page-local $C_I$), stating that the Smagorinsky form
  "follows Boussinesq's hypothesis"
  ([Volpiani (2024)](/sources/volpiani-2024.md), App. 2, Eqs. 26–28; see
  [Smagorinsky model](/methods/smagorinsky-model.md)).
- **RANS, compressible, as the linear part of an algebraic stress model.**
  Sandberg & Michelassi (2022) define the Reynolds stress as
  $-\overline{\rho u_i''u_j''}$ (their overbar a time average) and write the
  explicit algebraic model trained by Akolekar et al. (2019) with
  gene-expression programming as (Eq. 2, in registry symbols with
  $\langle\rho\rangle R_{ij}$ the density-weighted stress of positive trace,
  which is the convention this equation needs, see Qualifications)
  $$\langle\rho\rangle R_{ij}-\tfrac23\langle\rho\rangle k\delta_{ij}=-2\mu_t\langle S^d_{ij}\rangle_\rho+2\langle\rho\rangle k\,G^1T^{(1)}_{ij}+2\langle\rho\rangle k\sum_{m=2}^{4}G^mT^{(m)}_{ij},$$
  labelled "linear Boussinesq", "additional linear term" and "additional
  nonlinear terms", with $\langle S^d_{ij}\rangle_\rho$ the Favre-averaged
  deviatoric strain, $T^{(m)}$ basis tensors built from the
  non-dimensional strain and rotation (Pope 1975) and $G^m(I_1,I_2)$
  functions of two invariants found by the regression (the source's
  $V^k_{ij}$, $\zeta_k$, $I_k$)
  ([Sandberg & Michelassi (2022)](/sources/sandberg-2022.md), §2.2.2.1,
  §4.3, Eq. 2; see [symbolic-regression closures](/methods/symbolic-regression-closure.md)).
  The same review lists the scalar eddy viscosities of the
  $k$-$\varepsilon$, $k$-$\omega$ and $k$-$L$ models as
  $\mu_t=0.09\langle\rho\rangle k^2/\varepsilon$, $\langle\rho\rangle k/\omega$ and
  $0.09\langle\rho\rangle L\sqrt k$ (§2.2.2.1).
  Sandberg & Zhao (2022) print the same definition and the same form for
  the full ten-tensor expansion (Eqs. 1–2; on the
  [explicit algebraic Reynolds-stress model](/methods/explicit-algebraic-reynolds-stress-model.md)
  page), with the same trace inconsistency (Qualifications), and the same
  two eddy viscosities $0.09\langle\rho\rangle k^2/\varepsilon$ and
  $\langle\rho\rangle k/\omega$ ([Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md),
  §3.2, Eqs. 1–2).
- **RANS, incompressible, split into a Boussinesq and an extra
  anisotropy.** Cherroud et al. (2022) use the registry convention,
  $R_{ij}=\tfrac23k\delta_{ij}+2kb_{ij}$, and write the Boussinesq part of the
  anisotropy as $2kb^0_{ij}=-2\nu_t\langle S_{ij}\rangle$, i.e.
  $b^0_{ij}=-\nu_t\langle S_{ij}\rangle/k$, with $\nu_t$ from
  [$k$-$\omega$ SST](/methods/k-omega-sst-model.md); the learned correction
  $b^\Delta_{ij}$ is added to it ([Cherroud et al. (2022)](/sources/cherroud-2022.md),
  §2.1, Eqs. 3–5), the split of Oulghelou et al. below.
- **RANS, incompressible, with a corrected eddy viscosity in a modified
  pressure.** Brenner et al. (2022) write
  $R_{ij}=\tfrac23k\delta_{ij}-\nu_t(\partial_j\langle u_i\rangle+\partial_i\langle u_j\rangle)$,
  the registry form, absorb $\tfrac23k$ into the modified pressure
  $p/\rho+\tfrac23k$ and write the momentum equation with
  $\partial_j\big((\nu+\nu_t)\partial_j\langle u_i\rangle\big)$ only; their
  data-assimilated closure replaces $\nu_t$ by $\beta(\boldsymbol x)\nu_t$,
  with $\nu_t$ frozen from a converged [$k$-$\varepsilon$](/methods/k-epsilon-model.md)
  solution and $\beta$ the spatial multiplier (the source's $\alpha$)
  ([Brenner et al. (2022)](/sources/brenner-2022.md), §2.1.1, Eqs. 1–7;
  see Qualifications for the term the momentum equation omits, and
  [field inversion](/methods/field-inversion-machine-learning.md)).
- **RANS, compressible, with the quadratic constitutive relation.** He et
  al. (2022) write the Reynolds stress in the $-\rho\langle u_i'u_j'\rangle$
  convention as $2\rho\nu_tS^d_{ij}-\tfrac23\rho k\delta_{ij}$ and its QCR form
  (Spalart 2000) with $c_{cr1}=0.3$ and the normalized rotation
  $O_{ij}$ of the [Spalart–Allmaras page](/methods/spalart-allmaras-model.md);
  the $k$ of the isotropic term, absent from SA, is approximated after
  Rumsey et al. as $k=3c_{cr2}\nu_t\sqrt{2\Omega_{ij}\Omega_{ij}}=3c_{cr2}\nu_t\lvert\langle\Omega\rangle\rvert$
  with $c_{cr2}=1.25$, which they call QCR2013V
  ([He et al. (2022)](/sources/he-2022-b.md), §2.1, Eqs. 2–3, 5; the source's
  $W_{ij}$ is the rotation tensor). The isotropic stress it adds,
  $\tfrac23k=2.5\,\nu_t\lvert\langle\Omega\rangle\rvert$, has the coefficient of the
  QCR2013 term $C_{cr2}\nu_t\lvert S^d\rvert$, $C_{cr2}=2.5$, which Li &
  Liu (2022, §2.3) cite, with the rotation magnitude in place of the strain magnitude
  *(compiler check, not in the sources)*.
- **LES, compressible, with a Yoshizawa or a transported trace.** Qi et
  al. (2022) write the deviatoric Favre subgrid stress as
  $-2\mu_{\mathrm{sgs}}$ times the deviatoric filtered strain, with
  $\mu_{\mathrm{sgs}}=\bar\rho C_{sm}\Delta^2\lvert\tilde S\rvert$ ($C_{sm}$ the
  registry's $C_s^2$ *(compiler check, not in the sources)*), and recall the
  Yoshizawa trace $\tau_{kk}=2C_I\bar\rho\Delta^2\lvert\tilde S\rvert^2$, the
  registry's positive-trace convention, as Volpiani (2024) below
  ([Qi et al. (2022)](/sources/qi-2022-b.md), §2, Eqs. 2.11–2.15). Their
  one-equation model replaces the Yoshizawa trace by $2\bar\rho k_{\mathrm{sgs}}$
  from a transported $k_{\mathrm{sgs}}$ and fixes $C_{sm}$ locally by matching
  the anisotropic part of the energy flux (§3.2, Eq. 3.21; see the
  [dynamic procedure](/methods/dynamic-procedure.md) page).
- **LES and RANS of a compressible ramp, opposite sign.** Tonicello et al.
  (2022) define the stress as $\bar\rho\tilde u_i\tilde u_j-\overline{\rho u_iu_j}$,
  the registry's Favre $\tau_{ij}$ with the opposite sign, and write its
  Boussinesq form as $2\bar\rho\nu_t\tilde S^d_{ij}-\tfrac23\bar\rho k\delta_{ij}$
  for both a filter and a Favre time average
  ([Tonicello et al. (2022)](/sources/tonicello-2022.md), §4, Eqs. 4.4,
  4.7); their a priori test of it is below.

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
tensors of Pope (1975), which Duraisamy et al. (2019, §2, §5.3, Eq. 11)
and Duraisamy (2021, §III.A, Eq. 4) cite. The Boussinesq hypothesis keeps
only the first term, $T^{(1)}\propto S_{ij}$; the
[tensor-basis neural network](/methods/tensor-basis-neural-network.md) and
the quadratic constitutive relation of the SA page add higher terms.

Haering et al. (2022) derive the scalar eddy viscosity from a
gradient-diffusion argument: a flux $\langle u_i'\phi'\rangle$ is modelled
from the displacement of fluid particles over a decorrelation time $T_\phi$,
which under isotropy gives $\nu_\phi=C\,k_cT_\phi$ with $k_c$ the energy of
the convecting fluctuations ([Haering et al. (2022)](/sources/haering-2022.md),
§III B, Eqs. 12–14). The LES version holds only in expectation.

Heinz (2020) derives the hypothesis from a stochastic model instead: the
Reynolds (or subgrid) stress is the variance of a velocity probability
(or filtered) density governed by a Fokker–Planck equation with relaxation
time $\tau_L$ and diffusion parameter $0\le c_0\le1$ (page-local), and the
simplest balance of the resulting anisotropy equation,
$b_{ij}=-\tau_L\langle S_{ij}\rangle/3$, gives
$R_{ij}=\tfrac23k\delta_{ij}-2\nu_t\langle S_{ij}\rangle$ with
$\nu_t=k\tau_L/3=C_\mu k^2/\varepsilon$ and $C_\mu=2(1-c_0)/3$
([Heinz (2020)](/sources/heinz-2020.md), §2.2, Eqs. 2–7; constants on the
[$k$-$\varepsilon$ page](/methods/k-epsilon-model.md)). The same author
writes the hypothesis three times in a hybrid simulation, for the total
(RANS) stress with $\nu_{t,\mathrm{tot}}$, for the mean resolved stress
$R^{\mathrm{res}}_{ij}$ with $\nu_{t,\mathrm{res}}$, and for the modelled
stress with $\nu_t$ (page-local subscripts), and links the three viscosities
through $R_{ij}=R^{\mathrm{res}}_{ij}+\langle\tau_{ij}\rangle$ (§2.4, Eqs. 14,
19–20; see [hybrid RANS/LES](/definitions/hybrid-rans-les.md)). The
stochastic view also grounds the realizability Heinz requires of any
stress model: physically, the stress must be the variance of a realizable
stochastic process; mathematically (after Schumann), the modelled stress
must be positive semi-definite, which carries over to subgrid stresses
when the filter is positive (§2.1).

## Limits of a single scalar eddy viscosity

**Misalignment.** Agrawal et al. (2022) build their model on the statement
that the alignment of the subgrid stress with the resolved strain is invalid
locally, as a priori analyses of DNS show; their introduction cites the
a priori misalignment results of Bardina et al. and of Meneveau & Liu. On filtered channel DNS at $Re_\tau=395$ and $2000$ their
non-Boussinesq [dynamic tensor-coefficient Smagorinsky model](/methods/dynamic-tensor-coefficient-smagorinsky-model.md)
correlates better with the exact stress than the dynamic Smagorinsky model,
most of all near the wall, while the two models have identical dissipation
correlations, because only the isotropic part of the coefficient tensor
dissipates ([Agrawal et al. (2022)](/sources/agrawal-2022.md), §V, Figs. 1–2).
The authors add that these correlations do not measure alignment.

**Isotropy blamed for lost anisotropy and unsteadiness.** Yang & Ma (2022)
state that "the isotropic hypothesis of the eddy viscosity model" ignores
the anisotropic nature of turbulence, and that the large eddy viscosity
chosen in RANS for robustness "might erase some unsteadiness of small-scale
flow structures" (§1); in their transonic turbine cascade SST URANS
over-predicts the Reynolds shear stress along the tip-leakage vortex and
misses the trailing-edge mixing (§3.2, Fig. 8), and the resolved anisotropy
of the vortex core moves from one-component towards two-component and then
isotropic states on the Lumley map (§4.6, Fig. 19). Wang et al. (2021)
motivate a Reynolds-stress host for detached-eddy simulation in the same
terms: most DES methods "invoke the eddy-viscosity assumption", and a
[Reynolds-stress model](/methods/reynolds-stress-model.md), "abandoning the
isotropic eddy-viscosity hypothesis", is preferred for "problem" flows
where eddy-viscosity models "may fail to predict separation accurately"
(§1).

**Higher-order gradient closures.** Jakhar et al. (2026) note that the
fourth- and sixth-order truncations of the Taylor expansion of the subgrid
stress (NGM4, NGM6), which their sparse regression selects for forced
two-dimensional turbulence, "violate the Boussinesq hypothesis as they
depend on second-order velocity gradients", and present this as the "need to
go beyond classical turbulence tensors to represent backscatter and
anisotropic effects" ([Jakhar et al. (2026)](/sources/jakhar-2026.md),
p. 5; arXiv v3; see [gradient model](/methods/gradient-model.md) and
[energy backscatter](/definitions/energy-backscatter.md)).

**Mean stress against energy transfer.** Haering et al. (2022) argue that
one scalar eddy viscosity cannot represent both the mean subgrid stress and
the mean energy transfer to the subgrid scales. The first is the mean of the
stress; the second is governed by the correlation between stress and
resolved strain, which in filtered turbulence is "of order 20% or less" but
equals one, or nearly so, for an eddy-viscosity model. Getting the transfer
right therefore requires a smaller viscosity than getting the stress right.
Citing Jiménez & Moser, they state that the dynamic Smagorinsky model gives
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

Brenner et al. (2022) use the same indicator of Schmitt (the source's
$\rho_{RS}$, with the anisotropic stress and the mean strain), equal to one
for aligned tensors, with Schmitt's threshold 0.86 for alignment, which
"in the case of vectors, corresponds to an angle of approximately 30°".
After assimilating averaged LES velocity into a spatial multiplier
$\beta(\boldsymbol x)$ of a frozen $k$-$\varepsilon$ eddy viscosity on the
periodic hill at $Re=10\,595$, the mean velocities "definitely" improve
but the alignment is "neither considerably nor consistently improved",
remaining comparable to the baseline RANS; on synthetic data from a
prescribed multiplier the velocity is recovered while the multiplier is
not, so the inverse problem is non-unique
([Brenner et al. (2022)](/sources/brenner-2022.md), §2.11, Eq. 42, §3.2,
§3.5, Figs. 6–7, 13; see [periodic hill](/benchmarks/periodic-hill.md)).
This agrees with Cato et al.'s finding that a misaligned
Boussinesq-constrained correction can fit the mean flow.

**Corrections inside and outside the hypothesis, in a shock interaction.**
Fanizza et al. (2025) compare four corrections of the compressible
[Spalart–Allmaras model](/methods/spalart-allmaras-model.md), inferred by
adjoint data assimilation on a high-order discontinuous Galerkin
discretization: a momentum and energy source, which corrects the divergence
of the Reynolds stress directly, and three that act through the eddy
viscosity (a multiplier of $\mu_t$, a source and a production multiplier in
the $\tilde\nu$-equation). On the square cylinder at $Re=22\,000$ their
ranking agrees with Cato et al.'s (§4.2). On an oblique shock reflecting on
a turbulent boundary layer ($M_\infty=2.28$, $9.5^\circ$ deflection), with
dense velocity data weighted towards the wall, only the source reduces the
cost, by one to two orders of magnitude, while the other three stay on a
plateau; normalized errors of velocity, $C_p$ and $C_f$ (Table 1):

| Correction | velocity | $C_p$ | $C_f$ |
|---|---|---|---|
| momentum and energy source | 0.049 | 0.1825 | 0.0998 |
| eddy-viscosity multiplier | 0.250 | 0.5788 | 0.5689 |
| source in the $\tilde\nu$-equation | 0.257 | 0.2076 | 0.8920 |
| production multiplier | 0.339 | 0.2829 | 1.1450 |

Only the source improves quantities absent from the cost function. The
authors give as a second reason for the source's better near-wall
reconstruction that the three other corrections "are still constrained by the Boussinesq
assumption", whereas in this interaction the Reynolds stress is not aligned
with the viscous stress (§4.3.1). With wall-pressure data only, the three
Boussinesq-type corrections make $C_f$ worse than the baseline over the
whole wall (§4.3.3, Table 2; see
[shock/boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
and [field inversion](/methods/field-inversion-machine-learning.md)).

**Locality.** Seyedi & Zayernouri (2022) recall that the hypothesis assumes
the stress proportional to the *local* mean velocity gradient, that
Bradshaw (1973) showed it to fail over curved surfaces, and that Hinze et
al. (1974) found a strongly non-uniform eddy viscosity in the outer layer
downstream of a wall-mounted cap; they take these as motivation for
nonlocal closures such as the
[fractional subgrid-scale model](/methods/fractional-sgs-model.md)
([Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md), §I, pp. 2–3).

**Anisotropy slaved to the strain.** Morsbach et al. (2024) state that,
through the linear Boussinesq approximation, the turbulence anisotropy of a
linear eddy-viscosity model equals the strain-rate anisotropy, so that such
a model cannot reproduce free-stream anisotropy (§4.2). They show the consequence in a low-pressure-turbine cascade: the
SSG/LRR-$\omega$ Reynolds-stress model reproduces the measured free-stream
anisotropy and the turbulence intensity along the passage, which SST
underestimates shortly behind the leading edge, and follows the LES towards
the two-component limit where the accelerating flow stretches the
vortices; yet it underpredicts $k$ in the passage vortex and overpredicts
the peak secondary loss more than SST (48% against 34%)
([Morsbach et al. (2024)](/sources/morsbach-2024.md), §3.3, §4.2, Figs. 4,
10, 14–15; see the [SST page](/methods/k-omega-sst-model.md)). Tang et al.
(2023) find the same restriction in their baseline linear $k$-$\varepsilon$ model, whose
anisotropy on the periodic hill lies close to the plane-strain line of the
barycentric map at all stations, with the normal components far from DNS
(§III C, Figs. 7–8; see [k-ε models](/methods/k-epsilon-model.md)).
Agrawal & Koutsourelakis (2024) state the same restriction for the linear
model in general, the anisotropy being confined to the plane-strain line,
and, citing barycentric-map studies, that a tensor-basis closure can reach
other realizable states; with $g^{(1)}=-0.09$ and the other coefficients
zero their closure reduces to the linear $k$-$\varepsilon$ model
([Agrawal & Koutsourelakis (2024)](/sources/agrawal-2024.md), §2.2.1;
arXiv v2; see [model-form uncertainty](/definitions/model-form-uncertainty.md)).

**Rotation, non-equilibrium and the second-moment alternative.** Liu et al.
(2024) recall that linear eddy-viscosity models need added
rotation–curvature, quadratic-constitutive or non-equilibrium corrections
to predict the anisotropy and non-equilibrium of compressor corner flows,
whereas a [differential Reynolds-stress model](/methods/reynolds-stress-model.md)
carries the stress production and the Coriolis terms exactly; their
fully turbulent Reynolds-stress model is nevertheless "only slightly more
accurate" than SST for corner separation
([Liu et al. (2024)](/sources/liu-2024.md), Introduction, Conclusions).
Bouhafid et al. (2024) choose a Reynolds-stress model for an aircraft wake
because, they state citing the literature, the Reynolds stress and the
mean strain are misaligned in wing-tip vortices owing to rotation
([Bouhafid et al. (2024)](/sources/bouhafid-2024.md), §2.2; cited, not
shown). Pacciani et al. (2025) recall that linear eddy-viscosity models
need a boosted turbulent production in separated shear layers to avoid
overpredicted reattachment lengths, the motivation of the separation terms
of their [transition model](/methods/laminar-kinetic-energy-transition-model.md)
([Pacciani et al. (2025)](/sources/pacciani-2025.md), §3.2, §4.5).

**Distorted wakes in blade passages.** Sandberg & Michelassi (2022) state
that the acceleration and turning of the mean flow in a blade passage
misalign the Reynolds stress and the strain in the wake cores, which
invalidates the linear hypothesis, and name non-linear closures or full
Reynolds-stress transport as possible cures (§3.2.3, citing Wu & Durbin
2001, Michelassi et al. 2002, Stieger & Hodson 2005, Michelassi & Wissink
2015). They cite the same failure for the heat flux: in a DNS of a
pulsating flow with intermittent separation and temperature stratification
(Wissink et al. 2004) the turbulent shear stress was rarely aligned with the
velocity deformation and the turbulent heat flux rarely with the
temperature gradient, and the turbulent Prandtl number took values between
0.4 and 4 instead of a constant of about 0.9 (§3.2.3, §3.3). See
[turbine cascades](/benchmarks/turbine-cascade.md).

Sandberg & Zhao (2022) add, in their review of data-driven RANS closures,
that the hypothesis is invalid near the wall even in channel, pipe and
boundary-layer flows because of Reynolds-stress anisotropy, while the
mean flow is still obtainable from traditional models on a fine enough
near-wall grid; that the secondary flow of a square duct is driven by the
imbalance of the normal stresses and is "clearly beyond the scope of
linear eddy-viscosity models", quadratic models not generally ensuring it
either (citing Modesti 2020, with Speziale et al. 1992 as a case of
adequate results); and that stress–strain misalignment in wakes and a
non-constant turbulent Prandtl number in cooling flows defeat the linear
stress and the gradient-diffusion heat flux alike
([Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md), §2.1–2.3).
Their jet-in-crossflow illustration (jet Reynolds number 12 500 on the jet
diameter, $Re_\tau=500$ upstream, blowing ratio 0.5) compares DNS with steady
[SST](/methods/k-omega-sst-model.md) RANS and an eddy-diffusivity heat flux
at $Pr_t=0.9$: the RANS gives a reduced spanwise spread of wall
temperature, wrong values of two Reynolds shear stresses (the source's
$\tau_{xz}$, $\tau_{yz}$), an underpredicted horseshoe vortex, a spanwise
velocity of the wrong sign off the axis and a much too small heat flux
near the wall (§2.3, Fig. 5).

**Eddy viscosity for the deviatoric part only.** Tonicello et al. (2022)
test the hypothesis a priori on a DNS of a Mach 2.91 boundary layer over a
$24^\circ$ compression–expansion ramp, both for a Favre time average and for
an explicit differential filter of width $2h$ to $8h$. They split the
exchange term of the resolved kinetic energy, $K_3$ (the source's symbol,
the registry's $-\Pi$; $K_3<0$ is forward transfer), into a deviatoric part and
the work of the trace, $\Lambda=-\tfrac23\bar\rho k\,\partial_l\tilde u_l$
(page-local), and define the equivalent eddy viscosity of the deviatoric
part

$$\nu_t=\frac{K_3+\Lambda}{-2\bar\rho\tilde S^d_{ij}\partial_j\tilde u_i}$$

([Tonicello et al. (2022)](/sources/tonicello-2022.md), §5, Eqs.
5.1–5.3). In registry terms $K_3+\Lambda=\bar\rho\,\tau^d_{ij}\tilde S^d_{ij}$
with $\tau_{ij}$ the registry's positive Favre stress per unit density, so
this $\nu_t=-\tau^d_{ij}\tilde S^d_{ij}/\lvert\tilde S^d\rvert^2$ is the
flux-matching projection of the deviatoric stress, the compressible
counterpart of $\nu_t^{\mathrm{opt}}$ below *(compiler check, not in the
sources)*. In the averaged fields the joint PDF of $\Lambda$ and $K_3$ lies
almost entirely on the side of positive $\nu_t$, and $K_3+\Lambda$ is
negative (dissipative) everywhere: the mean backscatter near the expansion
corner comes from the trace, not from the deviatoric stress, and a
positive eddy viscosity is "fairly accurate" on average; in the filtered
fields negative $\nu_t$ takes a large share of the points (§5, Figs.
27–28). The authors conclude that an eddy viscosity suits the deviatoric
part and that the trace needs its own model, and suggest heuristically a
[bulk-viscosity](/definitions/bulk-viscosity.md) form
$\tfrac23\bar\rho k\sim-\mu_b\,\partial_k\tilde u_k$ (the registry's bulk
viscosity $\mu_b$, §11, the source's $\beta$), not tested (§5, Eq. 5.5; see
[energy backscatter](/definitions/energy-backscatter.md) and
[pressure dilatation](/definitions/pressure-dilatation.md)).

**Separated 2-D flows: a tuned eddy viscosity suffices.** Cherroud et al.
(2022) learn, by sparse Bayesian regression, both an extra anisotropy
$b^\Delta_{ij}$ and a production correction $b^R_{ij}$ of SST on three
separated flows (periodic hill at $Re=10\,595$, converging–diverging
channel at $12\,600$, curved backward-facing step at $13\,700$). The
cross-validated models with the best compromise over velocity, $k$, shear
stress and $C_f$ have $b^\Delta=0$ and a single production term on
$T^{(1)}$, which raises the eddy viscosity in the separated region; a
Sobol analysis of a richer model finds the quantities of interest mostly
sensitive to the production coefficient near the walls and to the linear
$T^{(1)}$ part of $b^\Delta$ in shear layers and recirculation. They conclude
that linear eddy-viscosity models "are overall sufficient for such 2D
separated flows, provided that the eddy viscosity coefficient is properly
tuned", and, citing Huijing et al. (2021), that this does not hold in 3-D,
where non-linear terms become important
([Cherroud et al. (2022)](/sources/cherroud-2022.md), §4.2–4.3, §5,
Table 2, Fig. 8; see [symbolic-regression closures](/methods/symbolic-regression-closure.md)
and the [explicit algebraic Reynolds-stress model](/methods/explicit-algebraic-reynolds-stress-model.md)).
Sandberg & Zhao (2022) quote the same 3-D result of Huijing et al. on a
wall-mounted cube as "indicating that both a non-linear anisotropy model
and a production correction in the transport equations is needed"
(§4.1).

**What the energy-matching viscosity leaves out.** Inagaki & Kobayashi
(2023) split the deviatoric subgrid stress of filtered channel DNS
($Re_\tau=400$) into the part carried by the flux-matching eddy viscosity
and a remainder (page-local $\tau^{\mathrm{ani}}_{ij}$), following Abe:

$$\tau^d_{ij}=-2\nu_t^{\mathrm{opt}}\bar S_{ij}+\tau^{\mathrm{ani}}_{ij},\qquad \nu_t^{\mathrm{opt}}=\frac{\Pi}{\lvert\bar S\rvert^2},\qquad \tau^{\mathrm{ani}}_{ij}\bar S_{ij}=0,$$

in registry notation (the source's $\nu^{\rm sgs}=-\tau_{ij}\bar s_{ij}/(2\bar s_{ij}\bar s_{ij})$,
the same flux-matching viscosity as Vela-Martín's below *(compiler check,
not in the sources)*), so that $\tau^{\mathrm{ani}}_{ij}$ transfers no energy locally
([Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md), §II A, Eqs. 3–5;
arXiv v3). With a spectral cut-off in $x$ and $z$ only:

- for the "medium" filter (LES spacings $\Delta x^+=52.4$, $\Delta z^+=26.2$)
  the remainder is negligible in the mean shear stress, so eddy-viscosity
  models can predict both the energy transfer and the mean subgrid shear
  stress there (§III C, Fig. 3);
- for the "coarse" filter ($105$, $52.4$) $-\langle\tau^{\mathrm{ani}}_{xy}\rangle$ is
  comparable to the eddy-viscosity part (Fig. 3), and its contribution to
  the budget of the resolved Reynolds stress $R^{\mathrm{res}}_{ij}$
  (page-local, registry §11), the "anisotropic redistribution" (page-local
  $\xi^{\mathrm{AR}}_{ij}$, not the reference coordinate $\xi$), is comparable to the pressure redistribution in the spanwise
  component below $y^+=100$ (§III D–E, Figs. 5, 8); its spanwise component
  is positive (productive) everywhere for both filters;
- the trace of the redistribution is not zero but
  $\xi^{\mathrm{AR}}_{ii}=-\langle\tau^{\mathrm{ani}}_{ij}\rangle\langle\bar S_{ij}\rangle$, the mean–subgrid
  exchange through the remainder (§II C, Eq. 10).

A pure eddy-viscosity model removes this mechanism; the authors infer from
two-dimensional spectra that it participates in generating streamwise
vortices at the streak spacing (§IV A 2, Fig. 12). Details on
[energy backscatter](/definitions/energy-backscatter.md) and the
[scale-similarity model](/methods/scale-similarity-model.md), whose
streamwise redistribution comes closest to the filtered DNS among the three
remainder models tested a priori (§IV B, Fig. 13).

## Explicit non-linear extension

Tang et al. (2023) keep the Boussinesq term and add a learned non-linear
remainder of the anisotropy on Pope's two-dimensional integrity basis. In
registry notation, with the normalized tensors (registry §11)
$\mathsf S_{ij}=(k/\varepsilon)\langle S_{ij}\rangle$ and
$\mathsf W_{ij}=(k/\varepsilon)\langle\Omega_{ij}\rangle$,

$$b_{ij}=\underbrace{-C_\mu\mathsf S_{ij}}_{\text{Boussinesq}}+b^\perp_{ij},\qquad
b^\perp_{ij}=0.35\sum_{m=1}^{3}G^{m}(I_1,I_2)\,T^{(m)}_{ij},$$

$$T^{(1)}=\mathsf S,\quad T^{(2)}=\mathsf S\mathsf W-\mathsf W\mathsf S,\quad T^{(3)}=\mathsf S^2-\tfrac13\operatorname{tr}(\mathsf S^2)\,\mathsf I,\qquad I_1=\operatorname{tr}(\mathsf S^2),\quad I_2=\operatorname{tr}(\mathsf W^2),$$

with $G^m$ and $b^\perp_{ij}$ page-local
(§II C 2, Eqs. 9–16, 19). The source normalizes the anisotropy as
$\boldsymbol\tau/k-\tfrac23\mathbf I$, twice the registry's $b_{ij}$, so its
linear part reads $-2C_\mu\mathsf S$ and its prefactor $\beta/10=0.7$
($\beta=7$, "following the suggestion by Shih", for realizability); the
factors $-C_\mu$ and 0.35 above are that convention halved *(compiler check,
not in the sources)*. The sign of $T^{(2)}$ depends on the orientation of
the rotation tensor, which the source defines through
$\tfrac12(\nabla\boldsymbol u-\nabla\boldsymbol u^{\top})$ without fixing the index
convention of $\nabla\boldsymbol u$. The three scalars $G^m$ are found by
[symbolic regression](/methods/symbolic-regression-closure.md) as
polynomials in the invariants, after the invariants are mapped to $[-1,1]$
by $(1-e^{-I})/(1+e^{-I})$, which equals $\tanh(I/2)$ *(compiler check, not
in the sources)* (Eq. 18).

The split serves conditioning. The linear part is solved implicitly with
the baseline model's eddy viscosity and only $b^\perp$ is injected,
frozen after one evaluation ("loose coupling"); the authors call the
decomposition "necessary", since injecting the full learned stress
explicitly magnifies small errors during the RANS iterations (§II C 2,
§II D), the same conclusion McConkey et al. reach for their
non-negative split below. Trained on one periodic hill, the model improves
the anisotropy on two other hills and the velocity profiles on a
backward-facing step, but not visibly in the recirculation region of the
steepest hill (§III D, Figs. 12–16); its term contributions
show that the linear part and $T^{(1)}$ dominate the shear component, while
$T^{(2)}$ contributes most to the streamwise and $T^{(3)}$ to the spanwise
normal component (§III C, Fig. 11).

Oulghelou et al. (2025) keep the same split in the
[$k$-$\omega$ SST model](/methods/k-omega-sst-model.md): the anisotropy is
$b_{ij}=b^0_{ij}+b^\Delta_{ij}$, with $b^0_{ij}=-\nu_t\langle S_{ij}\rangle/k$ the
Boussinesq part (the registry form divided by $2k$ *(compiler check, not in
the sources)*) and $b^\Delta_{ij}$ (page-local) an additive correction on
the first three integrity-basis tensors, built here on strain and rotation
normalized by $\omega$ rather than by $\varepsilon/k$; a second correction
of the same form enters the $k$-equation as a production-like term
([Oulghelou et al. (2025)](/sources/oulghelou-2025.md), §2, Eqs. 1–10;
arXiv v2). They state that leaving the linear term unaltered "has the
benefit of enhanced numerical stability", citing earlier work (§2, p. 6),
the conditioning argument of Tang et al. and McConkey et al. Their expert
corrections, found by [symbolic regression](/methods/symbolic-regression-closure.md),
are $b^\Delta=5.21\,T^{(2)}$ (with a $k$-equation term $0.681\,T^{(1)}$) for
separated flows and $b^\Delta=0.25\,T^{(1)}$ for a near-sonic jet (Table 1).
A $T^{(1)}$ term is collinear with $b^0$ and only rescales the eddy
viscosity: $0.25\,T^{(1)}$ turns $\nu_t$ into $\nu_t-0.25k/\omega$, i.e.
$0.75\,\nu_t$ where the SST limiter is inactive ($\nu_t=k/\omega$)
*(compiler check, not in the sources)*, consistent with the authors'
statement that the jet expert reduces the eddy viscosity "to compensate for
the so-called jet anomaly" (§4.2.1). How the experts are blended in space
is on the [turbulence-model aggregation](/methods/turbulence-model-aggregation.md)
page.

Cherroud et al. (2022) use the same split, $b_{ij}=b^0_{ij}+b^\Delta_{ij}$ with
$b^\Delta$ on $T^{(1)}$–$T^{(3)}$ of strain and rotation normalized by $\omega$,
plus a production correction $b^R_{ij}$ in the $k$- and $\omega$-equations, and
note that the $T^{(1)}$ term is an additive correction of $\nu_t$ while
$T^{(2)}$ and $T^{(3)}$ are the quadratic terms of the Gatski–Speziale and
Wallin–Johansson explicit algebraic models
([Cherroud et al. (2022)](/sources/cherroud-2022.md), §2.1, Eqs. 5–8,
12–13). Sandberg & Zhao (2022) write the general form with all ten basis
tensors and five invariants, labelling the three parts "linear
Boussinesq", "additional linear term" and "additional non-linear terms",
as Sandberg & Michelassi (2022) do for four tensors (§3.2, Eqs. 2–4). Both
are on the [explicit algebraic Reynolds-stress model](/methods/explicit-algebraic-reynolds-stress-model.md)
page.

## The best-fit eddy viscosity

If a reference stress is known, the scalar $\nu_t$ that brings the
Boussinesq form closest to it in the least-squares sense is the projection
of the stress on the strain. Wu et al.'s optimal eddy viscosity, as
cited by McConkey et al. (2022, §II A, Eqs. 5–6), is in registry
notation

$$\nu_t^{*}=\arg\min_{\nu_t}\big\lVert 2kb_{ij}+2\nu_t\langle S_{ij}\rangle\big\rVert=-\frac{2k\,b_{ij}\langle S_{ij}\rangle}{\lvert\langle S\rangle\rvert^2},$$

with $\nu_t^*$ page-local. Cato et al. (2023) estimate a DNS eddy viscosity
with the same projection (§III B, Eq. 18, after Volpiani et al.), which in
registry notation is the same expression *(compiler check, not in the
sources)*, and call it "a good approximation for attached flows" whose
injection into RANS "does not guarantee a perfect mean field". The LES
counterpart is the flux-matching $\nu_t^{\mathrm{opt}}=\Pi/\lvert\bar S\rvert^2$
of Vela-Martín above, the same projection applied to the deviatoric subgrid
stress *(compiler check, not in the sources)*; Inagaki & Kobayashi's
remainder $\tau^{\mathrm{ani}}_{ij}$ above is the part of the subgrid stress orthogonal
to the strain under that projection, the LES analogue of the remainder
$a^\perp_{ij}$ below where its non-negativity constraint is inactive
*(compiler check, not in the sources)*.

He et al. (2022) extract an LES eddy viscosity for a learned correction
of SA-QCR on a transonic bump the same way, as the minimizer of the
Frobenius misfit between the LES Reynolds stress and the model stress.
For the Boussinesq stress (their Eq. 6, which they attribute to Spalart et
al. 2017) this is, in registry notation,
$-R_{ij}\langle S^d_{ij}\rangle/\lvert\langle S^d\rangle\rvert^2$, McConkey et al.'s
$\nu_t^*$ written for compressible flow *(compiler check, not in the
sources)*; for the QCR2013V stress it is $\nu_t=-R_{ij}X_{ij}/(2X_{ij}X_{ij})$
with $X_{ij}$ (page-local) the QCR tensor including the isotropic
rotation term, which reduces to the Boussinesq form when $c_{cr1}=c_{cr2}=0$
([He et al. (2022)](/sources/he-2022-b.md), §2.7, Eqs. 6–8). Two limiters
are applied: $\nu_t\leftarrow\max(\nu_t,0)$, McConkey et al.'s constraint, and a
floor $S_{\mathrm{ref}}^2$ on the magnitude of the denominator with
$S_{\mathrm{ref}}=10^3\,\mathrm s^{-1}$; samples touched by either limiter are
excluded from training. The QCR-based extraction is "less sensitive to the
limiters and thus more reliable than the Boussinesq-based method"; a low
$S_{\mathrm{ref}}$ leaves non-physical high $\nu_t/\nu$ above the shear layer,
a high one contaminates the shear layer, separation bubble and reattached
boundary layer, and the value was chosen "by trial-and-error" (§2.7,
Appendix, Fig. 19; see [shock/boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)).

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
Sandberg & Michelassi (2022) cite earlier evidence for the same
point: even the true DNS Reynolds stress injected into RANS does not
guarantee an accurate mean flow (Parneix et al. 1998) and can jeopardize
robustness (Wu et al. 2019), and they present field inversion followed by
machine learning as the remedy that yields model-consistent closures, at
the cost of an inverse problem (§4.3; see
[field inversion](/methods/field-inversion-machine-learning.md)).

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
- Cato et al. (2023) conclude that "missing the proper stress alignment does
  not play a large role for predicting the mean flow" from a
  converging–diverging channel, a periodic hill and a square cylinder,
  where corrections within the hypothesis approach a free momentum forcing;
  Fanizza et al. (2025) agree on the square cylinder but, in a supersonic
  shock/boundary-layer interaction, find the three Boussinesq-type
  corrections unable to fix the near-wall flow and $C_f$ (above). The flows
  differ, and Fanizza et al. offer the Boussinesq constraint as a second
  reason, not an isolated one (§4.3.1), so the two findings are not
  incompatible; no source of this bundle tests corrections inside and
  outside the hypothesis on a shock interaction with a stress diagnostic
  like Cato et al.'s $c_{RS}$.
- Llorente (2024) equates the symmetric Reynolds stress to the
  non-symmetric $\nu_t\partial_j\langle u_i\rangle$ (p. 4), so the printed
  closure is not a symmetric tensor; the letter's results (an averaged
  penalty term and an energy bound for $\nu+\nu_t\ge0$) do not use its
  symmetry *(compiler check, not in the sources)*.
- Fanizza et al. (2025) print the stress of their eddy-viscosity
  multiplier as $(1+\chi_h)\mu_t\big(\nabla\boldsymbol u+\nabla\boldsymbol u^{\top}-\tfrac23\mathrm{Tr}(\nabla\boldsymbol u)\big)$,
  without the identity that their §2.1 writes (§3.3; $\chi_h$ the source's
  correction field).
- Sandberg & Michelassi (2022) define $\tau^R_{ij}=-\overline{\rho u_i''u_j''}$
  (§2.2.2.1), whose trace is $-2\langle\rho\rangle k$, so that its deviatoric
  part is $\tau^R_{ij}+\tfrac23\langle\rho\rangle k\delta_{ij}$ and its
  Boussinesq form carries $+2\mu_t$; their Eq. 2 writes
  $\tau^R_{ij}-\tfrac23\langle\rho\rangle k\delta_{ij}=-2\mu_t[\cdots]+\cdots$,
  the form of the positive-trace stress. Eq. 2 is therefore consistent only
  with the opposite sign convention to the definition, and the page writes
  it in that convention *(compiler check, not in the sources)*. Their
  summation index $k$ in Eq. 2 is also the symbol of the turbulent kinetic
  energy.
- Sandberg & Zhao (2022) print the same pair: the Reynolds stress defined
  as $-\langle\rho\rangle\langle u_i''u_j''\rangle$ (§3.2) and its Boussinesq
  form (Eq. 1) and extension (Eq. 2) written as
  $\tau_{ij}-\tfrac23\langle\rho\rangle k\delta_{ij}=-2\mu_t[\cdots]$, consistent only
  with the positive-trace stress; their production $P_k=\tau_{ij}\partial_ju_i$
  (§4.1) uses the negative convention *(compiler check, not in the
  sources)*. The page writes their equations in the registry convention.
- He et al. (2022) call $S_{ij}-\mathrm{tr}(S_{ij})$ "the traceless strain rate
  tensor" (§2.1, after Eq. 2); as printed its trace is $-2\,\mathrm{tr}(S)$,
  and their own extraction formula (Eq. 6) follows from minimizing the
  misfit with $S_{ij}-\tfrac13\mathrm{tr}(S)\delta_{ij}$ *(compiler check, not in
  the sources)*. The page writes $S^d_{ij}$.
- Brenner et al. (2022) state that with $\nu+\beta\nu_t$ in the momentum
  equation the corrected model "satisf[ies] conservation of momentum since
  the divergence operator is applied to the modified term" (§2.1.1), and
  their momentum equation (Eq. 6) keeps only
  $\partial_j\big((\nu+\beta\nu_t)\partial_j\langle u_i\rangle\big)$. From their Eqs.
  2–3 the divergence of the Boussinesq stress also contains
  $\partial_j(\beta\nu_t)\,\partial_i\langle u_j\rangle$ (using continuity), which
  vanishes only for a uniform $\beta\nu_t$ *(compiler check, not in the
  sources)*; the paper does not say whether the implementation keeps it.
- Brenner et al.'s Fig. 13 caption calls values "smaller than 0.86" good
  alignment and "larger than 0.86" bad, the reverse of their §2.11, where
  $\rho_{RS}>0.86$ means aligned and 1 perfect alignment; Brenner et al.
  print the Schmitt threshold 0.86 that Cato et al. attribute to Schmitt
  but replace by 0.8.
- Tonicello et al. (2022) define the stress with the sign opposite to the
  registry's and include $\bar\rho$; their $K_3<0$ is forward transfer.
  Translated, their $\nu_t$ (Eq. 5.3) keeps its sign.

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
- [Tang et al. (2023)](/sources/tang-2023.md) — §II A–D Eqs. 3, 9–19, §III C–D Figs. 7–8, 11–16 (arXiv v1).
- [Morsbach et al. (2024)](/sources/morsbach-2024.md) — §3.3, §4.2 Figs. 4, 10, 14–15.
- [Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md) — §II A Eqs. 3–5, §II C Eq. 10, §III C–E Figs. 3, 5, 8, §IV A 2 Fig. 12, §IV B Fig. 13 (arXiv v3).
- [Sirignano & MacArt (2023)](/sources/sirignano-2023.md) — §2.1, §3.2 Eq. 3.3.
- [Zhao et al. (2023b)](/sources/zhao-2023-b.md) — §2, Eq. 2-1.
- [Lederer et al. (2023)](/sources/lederer-2023.md) — §3.1, Eqs. 10–14 (arXiv v1).
- [Chen et al. (2024)](/sources/chen-2024.md) — §2.1 Eq. 2.1, §2.3, §3.3.
- [Domaradzki (2024)](/sources/domaradzki-2024.md) — §2.4 Eq. 2.47, §3.1.
- [Kim et al. (2024)](/sources/kim-2024.md) — §1.
- [Petrocchi & Barakos (2024)](/sources/petrocchi-2024.md) — §2.
- [Agrawal & Koutsourelakis (2024)](/sources/agrawal-2024.md) — §2.2.1 (arXiv v2).
- [Liu et al. (2024)](/sources/liu-2024.md) — Introduction, Conclusions.
- [Bouhafid et al. (2024)](/sources/bouhafid-2024.md) — §2.2.
- [Pacciani et al. (2025)](/sources/pacciani-2025.md) — §3.2, §4.5.
- [Möller et al. (2024)](/sources/moller-2024.md) — §II.A, Eq. 13 (accepted manuscript).
- [Fanizza et al. (2025)](/sources/fanizza-2025.md) — §2.1, §3.3, §4.2, §4.3.1 Table 1, §4.3.3 Table 2.
- [Mukha et al. (2025)](/sources/mukha-2025.md) — §II.A, Eqs. 2–3 (arXiv v1).
- [Llorente (2024)](/sources/llorente-2024.md) — p. 4, Eqs. 3–4 (author accepted manuscript).
- [Wu et al. (2025)](/sources/wu-2025.md) — §2.2, Table 2 (authors' manuscript).
- [Oulghelou et al. (2025)](/sources/oulghelou-2025.md) — §2 Eqs. 1–10, §4.2.1, Table 1 (arXiv v2).
- [Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md) — §2, Eqs. 3–8.
- [Ghidoni et al. (2026)](/sources/ghidoni-2026.md) — §2, Eq. 1.
- [Wang et al. (2021)](/sources/wang-2021-l.md) — §1, §2.3 Eqs. 6–10.
- [Yang & Ma (2022)](/sources/yang-2022-b.md) — §1, §3.2 Eqs. 8–9 Fig. 8, §4.6 Fig. 19.
- [Jakhar et al. (2026)](/sources/jakhar-2026.md) — p. 5 (arXiv v3).
- [Vandenhoeck et al. (2022)](/sources/vandenhoeck-2022.md) — §1.1, Eqs. 3, 7, 9–10.
- [Jiang et al. (2025)](/sources/jiang-2025.md) — §2 Eq. 6, App. A Eq. A2.
- [Tomboulides et al. (2025)](/sources/tomboulides-2025.md) — §2, Eqs. 1–4.
- [Lodares et al. (2022)](/sources/lodares-2022.md) — §2 Eqs. 9–13, §3.1.
- [Volpiani (2024)](/sources/volpiani-2024.md) — App. 2, Eqs. 26–28.
- [Monfaredi et al. (2021)](/sources/monfaredi-2021.md) — §2.1, Eqs. 1–2.
- [Sandberg & Michelassi (2022)](/sources/sandberg-2022.md) — §2.2.2.1, §3.2.3, §3.3, §4.3, Eq. 2.
- [Heinz (2020)](/sources/heinz-2020.md) — §2.1, §2.2 Eqs. 2–7, §2.4 Eqs. 14, 19–20.
- [Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md) — §2.1–2.3 Fig. 5, §3.2 Eqs. 1–4, §4.1.
- [Cherroud et al. (2022)](/sources/cherroud-2022.md) — §2.1 Eqs. 3–8, 12–13, §4.2–4.3 Table 2 Fig. 8, §5.
- [Brenner et al. (2022)](/sources/brenner-2022.md) — §2.1.1 Eqs. 1–7, §2.11 Eq. 42, §3.2, §3.5 Figs. 6–7, 13.
- [He et al. (2022)](/sources/he-2022-b.md) — §2.1 Eqs. 2–3, 5, §2.7 Eqs. 6–8, Appendix Fig. 19.
- [Qi et al. (2022)](/sources/qi-2022-b.md) — §2 Eqs. 2.11–2.15, §3.2 Eq. 3.21.
- [Tonicello et al. (2022)](/sources/tonicello-2022.md) — §4 Eqs. 4.4, 4.7, §5 Eqs. 5.1–5.5 Figs. 27–28.
