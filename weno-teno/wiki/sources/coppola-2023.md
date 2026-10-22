---
type: Source
title: "Coppola & Veldman (2023) — Global and local conservation of mass, momentum and kinetic energy in the simulation of compressible flow"
description: "Matrix framework for convective semi-discretizations proving that global conservation implies local conservation, deriving duality relations and a skew-symmetry criterion for kinetic-energy preservation that extend split forms to non-uniform grids and biased operators, and mapping finite-difference split forms onto finite-volume fluxes."
resource: "doi:10.1016/j.jcp.2022.111879"
source_kind: paper
authors: [Coppola G., Veldman A.E.P.]
year: 2023
venue: "J. Comput. Phys. 475:111879"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Journal_of_Computational_Physics_Coppola_Global_and_local_conservation_of_mass_momentum_and_kinetic_e.pdf"
tags: [kinetic-energy-preserving, finite-difference, finite-volume, turbulence]
timestamp: 2026-10-21T12:00:00Z
---

# Summary

The paper asks when a spatial semi-discretization of the convective terms of compressible flow
conserves three quantities: the linear invariants mass $\rho$ and momentum $\rho\phi$, and the
quadratic invariant $\tfrac12\rho\phi^2$, which is the kinetic energy $\kappa$ for $\phi=v$. It
treats both global and local conservation. The setting is a periodic one-dimensional grid,
possibly non-uniform. The scheme is $V\,d\phi/dt+\mathcal C\phi=0$, with a diagonal matrix
$V$ of control volumes, and every operator is written as
$D=\sum_k\mathrm{diag}(\mathsf c_k)\mathcal T^k$ with the circulant shift $\mathcal T$. The
symbols are those of the concept pages; the Notation map gives the paper's.

The results:

1. Global conservation of a linear invariant is equivalent to vanishing column sums. Any such
   matrix factors as $(I-\mathcal T^{-1})F$. So global conservation implies
   [local conservation in flux form](/results/local-conservation-flux-form.md), and every
   globally conservative finite-difference scheme is a cell-centred finite-volume scheme
   ([conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)).
   This touches the consistency assumption behind the
   [Lax–Wendroff theorem](/results/lax-wendroff-theorem.md).
2. For [split convective forms](/methods/split-convective-forms.md), conservation holds iff the
   operators satisfy duality relations, $D^\rho=-(D^v)^\top$ and
   $D^0=-(D^m)^\top$. These relations admit directionally biased
   ("dual-sided") operators.
3. [Kinetic energy preservation](/properties/kinetic-energy-preservation.md) holds iff
   $\mathcal C-\tfrac12\mathrm{diag}(\mathbf d_m)$ is skew-symmetric. This
   generalizes the Coppola et al. (2019) weight conditions to non-uniform meshes and non-central
   operators, and the skew-symmetry also gives local energy conservation.
4. For finite volumes, energy preservation forces a momentum flux $m_{i+1/2}\phi_{i+1/2}$ with the
   arithmetic mean of $\phi$, while the mass flux stays free. Such product fluxes are at most
   second order. Richardson extrapolation, after the Verstappen–Veldman
   [symmetry-preserving](/properties/symmetry-preservation.md) discretizations, recovers
   Pirozzoli's fourth-order flux. The relation to
   [entropy-conservative two-point fluxes](/methods/entropy-conservative-flux.md) and to
   [summation-by-parts operators](/operators/summation-by-parts-operator.md) is discussed but not
   developed.

Two tests confirm the theory, using classical RK4 with tiny steps (cited on
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md)):

- a transport model on uniform and stretched grids;
- one-dimensional Euler acoustic-wave steepening, with a fifth-order
  [WENO-JS](/methods/weno-js-reconstruction.md) reference solution.

The invariants are conserved to machine precision. A first-order dual-sided scheme gives a shock
profile without oscillation or smearing, and with no added dissipation.

# Version read

The file is arXiv:2208.14067v1 [physics.flu-dyn] of 30 Aug 2022 ("Preprint submitted to
Elsevier, August 31, 2022"), not the journal version of record. It has 38 pages, all read. The
acknowledgment already thanks the referees, which suggests a post-review manuscript; the equation
numbering of the version of record has not been checked. All numbers cited here are the
preprint's. The Crossref card gives "Veldman A.E.", while page 1 prints "Arthur E. P. Veldman";
the page-1 initials are used. There is no other identity issue.

# Key claims

The claims use the concept pages' symbols (see the Notation map): $\mathcal T$ the shift, $V$
the control volumes, $D$ and $D^m,D^0,D^\rho,D^v$ the (volume-scaled) derivative matrices,
$\mathcal C$ the convective (momentum) matrix, $\mathbf d_m$ the discrete mass transport,
$\mathcal A=\mathcal C-\tfrac12\mathrm{diag}(\mathbf d_m)$, $\zeta$ the mass split weight and
$\mu_D,\mu_\phi,\mu_v,\mu_\rho,\mu_L$ the momentum split weights.

1. For a volume-consistent discretization $V\,d\phi/dt+\mathcal C\phi=0$, global
   conservation of a linear invariant is equivalent to $\mathbf 1^\top\mathcal C=\mathbf 0^\top$
   (vanishing column sums). (§2.4, eq. (20)) **Derived**
2. Lemma A.1: $D=\sum_{k=-\bar k}^{\bar k}\mathrm{diag}(\mathsf c_k)\mathcal T^k$ is locally
   conservative, $D=(I-\mathcal T^{-1})F$, iff all its column sums vanish. The flux is explicit:
   $F=\sum_{k=-\bar k}^{\bar k}\sum_{h=k}^{\bar k}\mathrm{diag}(\mathcal T^{k-h}\mathsf c_h)\mathcal T^k$.
   (App. A.1, eq. (A.1)) **Proved**
3. Observation 1: for volume-consistent discretizations of transport equations, discrete global and
   local conservation are equivalent. (§2.4) **Proved**
4. The Lax–Wendroff-type flux consistency for constant states, eq. (22), is assumed, not proved, at
   this generality; the authors write that they "can not (yet) prove this". (§2.4) **Stated**
5. Observation 2: $V=\mathrm{diag}(D\mathbf x)$ makes $V^{-1}D$ exact on
   linear functions and keeps the order of $D$ on smoothly stretched grids. With the local
   spacing $\tfrac12(x_{i+1}-x_{i-1})$, a fourth-order formula degrades to second order.
   Numerically, the fourth-order central and second-order dual-sided schemes then fall to roughly
   first order. (§2.5, eqs. (23)–(26); §7.2, Fig. 1b) **Derived + Shown**
6. Observation 3: the finite-difference divergence form $V\,d\rho/dt=-Dm$
   conserves globally and locally iff $D$ has vanishing column sums. Derivative matrices
   with vanishing row sums also have vanishing column sums if they are (skew-)symmetric or
   circulant. (§3.2) **Proved**
7. The classical second-order Lagrangian derivative on a non-uniform grid, eq. (35), is neither
   skew-symmetric nor circulant and does not conserve globally. (§3.2) **Stated**
8. Observation 4 concerns the advective form
   $V\,d\rho/dt=-\big(\mathrm{diag}(\rho)D^vv+\mathrm{diag}(v)D^\rho\rho\big)$:
   - it conserves mass iff $D^\rho=-(D^v)^\top$ (duality);
   - a biased $D^v$ must therefore pair with an oppositely biased $D^\rho$
     ("dual-sided");
   - if $D^\rho=D^v$, duality forces skew-symmetry.

   (§3.3, eq. (43)) **Proved**
9. Observation 5: any volume-consistent finite-difference scheme built from divergence and advective
   forms that conserves mass globally is locally conservative. It is a cell-centred finite-volume
   scheme whose mass-flux coefficients are given by eq. (53). (§3.4) **Proved**
10. Observation 6: the generalized momentum operator (56) with $\mu_L=0$ conserves momentum iff
    $D^0=-(D^m)^\top$ and $D^\rho=-(D^v)^\top$ (eq. (58)).
    $\mu_L\ne0$ is incompatible with momentum conservation. (§4.2) **Derived** (the
    $\mu_L\ne0$ part **Stated**, proof "not presented here")
11. Global kinetic-energy conservation holds iff
    $\mathcal A=\mathcal C-\tfrac12\mathrm{diag}(\mathbf d_m)$ is
    skew-symmetric, equivalently
    $\mathrm{diag}(\mathbf d_m)=\mathcal C+\mathcal C^\top$
    (eq. (60a,b)). This proves the necessity of consistent splitting of continuity and momentum,
    which Pirozzoli and Morinishi had observed. (§5.1) **Proved**
12. Under energy preservation, $\mathbf d_m=(\mathcal C+\mathcal C^\top)\mathbf 1$
    (eq. (61)). If momentum is also conserved, then $\mathbf d_m=\mathcal C\mathbf 1$
    and mass is conserved (eq. (62)). For the split family this requires
    $\mu_D+\mu_\phi=\zeta$ and $\mu_v+\mu_\rho+\mu_L=1-\zeta$ (eq. (63)). (§5.1)
    **Derived**
13. Finite-volume interpolation of the product,
    $(m\phi)_{i+1/2}=\tfrac12(m_i\phi_i+m_{i+1}\phi_{i+1})$, gives a zero-diagonal advection matrix.
    It cannot preserve kinetic energy unless $\mathbf d_m=\mathbf 0$. (§5.2, eq. (64); §6.1)
    **Derived**
14. Observation 7: three-point finite-volume schemes conserve kinetic energy globally and locally
    iff the momentum flux is $m_{i+1/2}\phi_{i+1/2}$ with $\phi_{i+1/2}=\tfrac12(\phi_i+\phi_{i+1})$,
    "independent of the geometric position of the face" (eq. (66)).
    - the mass flux $m_{i+1/2}$ is arbitrary, even upwind-biased, if it is used consistently;
    - the local kinetic-energy flux is $\tfrac12m_{i+1/2}\phi_i\phi_{i+1}$.

    (§5.2, eqs. (65)–(71)) **Derived**
15. Eq. (71) collects all three-point energy-preserving finite-volume discretizations:
    $\partial_x(m\psi)\leftrightarrow(I-\mathcal T^{-1})\mathrm{diag}(m_f)\psi$, with
    $\psi\in\{\mathbf 1,\tfrac12(I+\mathcal T)\phi,\tfrac12\mathrm{diag}(\phi)\mathcal T\phi\}$ for
    mass, momentum and energy ($m_f$ the vector of face mass fluxes). (§5.2) **Derived**
16. The weight conditions $\mu_D-\mu_L=\mu_\phi=\tfrac12\zeta$ and
    $\mu_v=\mu_\rho=\tfrac12(1-\zeta)-\mu_L$ (eq. (72), Coppola et al. 2019, eq. (10)),
    together with the duality relations (58), are necessary and sufficient for global energy
    conservation of the generalized split finite-difference family. This extends the 2019 result
    from skew-symmetric operators on uniform meshes to non-uniform meshes and dual operators.
    (§5.3) **Derived**
17. A globally energy-preserving finite-difference scheme also conserves energy locally, with flux
    $\sum_{k>0}\sum_{h=0}^{k-1}\mathcal T^{-h}\mathrm{diag}(\mathsf c_k)\mathrm{diag}(\phi)\mathcal T^k\phi$,
    where $\mathsf c_k$ are the diagonals of $\mathcal A$. (§5.3; Corollary A.4) **Proved**
18. Observation 8: the split family (47)+(56) conserves:
    - mass iff (43) holds;
    - momentum iff $\mu_L=0$ and (58) holds;
    - energy iff (58) and (10) hold.

    For $\mu_L=0$, energy conservation implies momentum conservation, which implies mass
    conservation. For $\mu_L\ne0$, energy conservation does not imply momentum conservation.
    (§5.4) **Derived**
19. For linear three-point stencils, energy-preserving finite-difference discretizations and
    three-point finite-volume discretizations with linear fluxes form the same three-parameter
    family, mapped by eq. (53). (§5.4) **Derived**
20. For wider stencils the finite-volume framework is strictly more general: some face-flux
    products have no finite-difference counterpart. No finite-difference equivalent of the
    logarithmic-mean fluxes of Chandrashekar or Ranocha is known. (§5.4) **Derived / Stated**
21. Observation 9: energy-preserving fluxes of the product form $m_{i+1/2}\phi_{i+1/2}$ are at most
    second order. (§6.1, eq. (74)) **Derived**
22. Richardson extrapolation $(2^3\cdot\text{fine}-\text{coarse})/6$ of the second-order scheme
    gives a fourth-order finite-volume scheme. Its effective volume is
    $V^{\mathrm{4th}}=(8V^{\mathrm{fine}}-V^{\mathrm{coarse}})/6$, and its flux equals
    Pirozzoli's flux with his stencil coefficients $L=2$, $a_1=2/3$, $a_2=-1/12$. (§6.2,
    eqs. (75)–(78)) **Derived**
23. Mass-flux splitting (Feiereisen, KGP, Coppola $\zeta=0$) does not matter for discrete energy
    preservation if it is applied consistently in mass and momentum. It may affect accuracy.
    (§6.1) **Derived**
24. In the transport test ($N_x=21$, $T=1$):
    - central split forms with weights satisfying (10), $\zeta\in\{0,1/2,1\}$, conserve mass,
      momentum and energy to machine accuracy;
    - weights violating (10) conserve mass and momentum but not energy (errors
      $O(10^{-3})$–$O(10^{-4})$);
    - KG1 ($\mu_L=0.5$, $\zeta=0$) does not conserve momentum;
    - the case $\mu_\rho=1$ "turned out not always to be stable".

    (§7.3, Fig. 2) **Shown**
25. The dual-sided discretization (79c) conserves all three invariants to machine accuracy for the
    whole $\zeta$-family. Traditional upwinding (all four operators $I-\mathcal T^{-1}$) conserves
    none of them, except mass for $\zeta=1$. (§7.3, Fig. 3) **Shown**
26. On stretched grids ($s=5$) with $V=\mathrm{diag}(D\mathbf x)$, four schemes attain
    their design orders: central-2 (order 2), central-4 (4), dual-sided (1) and dual-sided-2 (2).
    (§7.2, Fig. 1a) **Shown**
27. One-dimensional Euler test, internal-energy formulation, with the dual-sided scheme
    ($\zeta=1/2$, central pressure terms):
    - mass, momentum and total energy are conserved to machine precision, as with the central
      scheme;
    - upwinding at $t=5$ gives normalized errors of $-4.5\times10^{-3}$ (mass), $-1.2\times10^{-2}$
      (momentum) and $-1.5\times10^{-2}$ (total energy).

    (§8.2, Fig. 4a) **Shown**
28. In the same test, after the shock forms ($t\approx3.5$), the second-order central scheme
    oscillates strongly and first-order upwinding smears. The formally first-order dual-sided
    scheme "nicely fits in between", with no artificial dissipation. (§8.2, Fig. 4b) **Shown**
29. The internal-energy formulation conserves total energy if mass and momentum are discretized in
    a kinetic-energy-preserving way and $D^p=-(D^e)^\top$. With Veldman's
    requirement, the dual-sided case with $\zeta=1/2$ gives
    $D^p=D^e=D^{\mathrm{cen}}$. (§8.1) **Stated / Derived**
30. All earlier studies of split convective forms assumed central discretization. Directionally
    biased discretizations are also admissible if they satisfy (58). (§5.4) **Stated**

# Printed slips

- **Eq. (6), p. 5.** In this page's symbols, the preprint prints
  $\partial_t(\tfrac12\rho\phi^2)=\phi A\phi=\partial_x(\tfrac12\rho v\phi^2)$, with $A$ the
  continuous kinetic-energy operator $A\phi=\partial_x(\rho v\phi)-\tfrac12\phi\,\partial_x(\rho v)$.
  A minus sign is missing: from (1a,b),
  $\partial_t(\tfrac12\rho\phi^2)=\phi\,\partial_t(\rho\phi)-\tfrac12\phi^2\partial_t\rho=-\phi A\phi$,
  consistent with eq. (59). *(compiler check, not in the sources: re-derived from (1a,b) and (5))*
- **§2.2, p. 6.** "$\epsilon=0$" where $\varepsilon$ is meant (font slip; $\varepsilon$ is the
  weight written $\mu_L$ here).
- **Observation 3 (§3.2).** It refers to "the discrete divergence form (28)". (28) is the
  finite-volume form; the finite-difference divergence form is eq. (32).
- **§5.4.** "in Section 4.1 we have seen that the three-point finite-volume discretizations … form a
  three-parameter family": that family is introduced in §3.1, eq. (29).
- **§5.3.** The finite-difference section writes $A^{fv}_{kin}$ where the finite-difference
  $A_{kin}$ (here $\mathcal A$) is meant.
- **§5.2.** The kinetic-energy flux is printed with the subscript "$i+/2$".
- **§7.2.** "$dx/d\xi$": the source's $\xi$, the mass split weight (here $\zeta$), is reused for
  the computational coordinate, which is called $\eta$ in §2.5 and $\sigma$ in §7.1.
- **§7.3 and Fig. 3 caption.** "the traditional upwind discretization (79c)": (79c) is defined as
  the dual-sided discretization. The upwind case uses the matrix of (79c) in all four slots.
- **§8.2.** The time step $1.17\times10^{-4}$ does not match the stated Courant number $10^{-3}$ for
  $N_x=32$. With $\Delta x=2\pi/32$ and $v_{\max}=v_0+0.2c_0\approx1.737$, the step is
  $1.13\times10^{-4}$; $1.17\times10^{-4}$ corresponds to $\Delta x=2\pi/31$, which could be a
  node-counting convention. *(compiler check, not in the sources: recomputed
  $\Delta t=10^{-3}\Delta x/v_{\max}$ with $c_0=\sqrt{1.4}$)*

# Notation map

The concept pages ([split convective forms](/methods/split-convective-forms.md),
[kinetic energy preservation](/properties/kinetic-energy-preservation.md),
[local conservation and flux form](/results/local-conservation-flux-form.md)) use the
page-local symbols of the middle column; this page uses the same ones.

| Coppola & Veldman | Bundle ([notation](/notation.md) and concept pages) | Note |
|---|---|---|
| $u$ (velocity) | $v$ | registry |
| $\phi$ | $\phi$ | transported scalar (page-local); $\phi=v$ gives momentum and kinetic energy |
| $\tfrac12\rho\phi^2$ ("kinetic energy") | $\kappa=\tfrac12\rho\lvert v\rvert^2$ for $\phi=v$ | a quadratic invariant, not an entropy pair |
| $m=\rho u$ | $m=\rho v$ | mass flux; $m_{i+1/2}$ face value, $M_f=\mathrm{diag}(m_f)$ written out as $\mathrm{diag}(m_f)$ (**collision** of $M$ with the mass matrix) |
| $E$ (shift, $(E\phi)_i=\phi_{i+1}$) | $\mathcal T$ | **collision** with the total energy $E$ |
| $H$ (Fraktur, control volumes) | $V$ | **collision** with the specific total enthalpy $H$ |
| $D$ (Fraktur), $D^{\rho u},D^0,D^\rho,D^u,D^p,D^e$ | $D$, $D^m,D^0,D^\rho,D^v,D^p,D^e$ | page-local; not the DG differentiation matrix $D$ |
| $R,U,\Phi,\Psi$ | $\mathrm{diag}(\rho),\mathrm{diag}(v),\mathrm{diag}(\phi),\mathrm{diag}(\psi)$ | written out; **collision** of $R$ with the eigenvector matrix |
| $C_{mom}$, $d_{mass}$ | $\mathcal C$, $\mathbf d_m$ | discrete convective matrix and mass transport |
| $A_{kin}$ (discrete), $\mathcal A_{kin}$ (continuous) | $\mathcal A$, $A$ | $A$ also the registry's flux Jacobian; the continuous operator stays page-local on the KEP page |
| $M_{mass}$, $C_{mom}$ (continuous) | $\partial_x(\rho v)$, $\partial_x(\rho v\,\cdot)$ | written out |
| $a_k$, $A_k=\mathrm{diag}(a_k)$, $L$ (semi-bandwidth) | $\mathsf c_k$, $\mathrm{diag}(\mathsf c_k)$, $\bar k$ | diagonals of a banded matrix; **collision** of $a$ with the wave speed and of $L$ with the eigenvector matrix |
| $F$, $b_k$ | $F$, $\mathsf b_k$ | flux matrix of $D=(I-\mathcal T^{-1})F$; face $i+1/2$ stored at index $i$ |
| $\alpha,\beta,\gamma,\delta,\varepsilon$ | $\mu_D,\mu_\phi,\mu_v,\mu_\rho,\mu_L$ | **collision** with $\alpha$ (DG–FV blending), $\beta_k$, $\gamma$ (ratio of specific heats) and $\epsilon$ (WENO regularization) |
| $\xi$ | $\zeta$ | mass split weight (divergence vs advective); **collision** with the LGL nodes $\xi_j$ |
| $D^{cen}=\tfrac12(E-E^{-1})$, $D^{upw}=I-E^{-1}$ | $D^{\mathrm{cen}}$, $D^{\mathrm{upw}}$, with $\mathcal T$ | |
| $H_{4th}$, $H_{fine}$, $H_{crse}$ | $V^{\mathrm{4th}}$, $V^{\mathrm{fine}}$, $V^{\mathrm{coarse}}$ | |
| $e$, $p$, $\gamma$, $c_0$ | $e$, $p$, $\gamma$, $c$ | internal energy, pressure, ratio of specific heats, sound speed (§8) |
| $N$ (grid points) | $N_x$ | |

# Reference list

The paper prints 57 references in numbered style [1]–[57]. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` set to `coppola-2023`. Notes on individual items:

- two pairs share an author and year and take suffixes: [7]/[14] (`coppola-2019`,
  `coppola-2019-b`) and [1]/[43] (`pirozzoli-2011`, `pirozzoli-2011-b`);
- [42] and [47] are arXiv preprints;
- [53] is printed as "submitted" with no year and is keyed by the citing year;
- [7] has its pages printed as an article-number range.

No item is unparseable.

# Pages created or updated

Chunk 1 (2026-10-21). This source is cited on:

* [Conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
* [Entropy-conservative and kinetic-energy-preserving two-point fluxes](/methods/entropy-conservative-flux.md)
* [Flux differencing and split-form DG](/methods/flux-differencing.md)
* [Kinetic energy preservation](/properties/kinetic-energy-preservation.md)
* [Lax–Wendroff theorem](/results/lax-wendroff-theorem.md)
* [Local conservation is equivalent to a flux form](/results/local-conservation-flux-form.md)
* [Split convective forms](/methods/split-convective-forms.md)
* [Summation-by-parts operator](/operators/summation-by-parts-operator.md)
* [Symmetry preservation](/properties/symmetry-preservation.md)
