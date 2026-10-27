---
type: Method
title: "Divergence-consistent discretize-first LES"
description: "Agdestein & Sanderse's framework for learned LES closures: discretize, differentiate the constraint, filter with a face-averaging filter that maps discretely divergence-free fields to divergence-free fields, and close inside the pressure projection; it yields exact closure targets and a stable CNN closure."
status: established
aliases: [discretize first filter next, discretize-differentiate-filter-close, DCF formulation, face-averaging filter, discrete commutator error]
tags: [les, sgs-model, neural-network, data-driven]
timestamp: 2026-10-26T20:51:00Z
---

# Divergence-consistent discretize-first LES

Agdestein & Sanderse (2025) build LES for incompressible flow in a fixed
order: **discretize, differentiate the constraint, filter, close**. The DNS
is a second-order finite-volume discretization on a staggered grid. Its
pressure is eliminated by the discrete projection. A discrete
coarse-graining filter is applied to the resulting pressure-free system,
which gives an exact discrete equation for the filtered DNS velocity on the
coarse grid; its remainder is the closure target. A **face-averaging
filter** keeps that target and the filtered velocity discretely
divergence-free. A **divergence-consistent formulation** keeps the LES
solution divergence-free whatever the learned closure returns. The method
is a concrete instance of a
[discretization-consistent closure](/definitions/discretization-consistent-closure.md).

**Page-local notation.**

- $\mathsf D$, $\mathsf G$, $\mathsf P$ are the discrete divergence,
  gradient and pressure projector on the DNS grid.
- $\mathsf F(u)$ is the discrete convection, diffusion and body force.
- Overbarred operators ($\bar{\mathsf D}$, $\bar{\mathsf P}$,
  $\bar{\mathsf F}$, …) are the same operators on the coarse grid. Here the
  overbar marks the coarse operator, not a filtered one.
- $\Phi$ is the discrete filter matrix from the fine to the coarse grid,
  with $\bar u=\Phi u$ the filtered DNS velocity and $\bar v$ the LES
  velocity.
- $m(\bar v;\boldsymbol\theta)$ is the closure model.

## Discretize first, then filter (§2–§3.2)

**DNS.** The continuous equations are $\nabla\cdot u=0$ and
$\partial_tu+\nabla\cdot(uu^{\mathsf T})=-\nabla p+\nu\nabla^2u+f$, with
kinematic pressure, on a periodic box (Eqs. 1–2). The discretization is
Harlow–Welch staggered finite volumes, with pressure at cell centres and
each velocity component on its faces (App. A). The convective term is
written in divergence form and is energy-conserving (skew-symmetric) for
divergence-free velocity fields.

**Pressure elimination.** Solving the pressure Poisson equation gives the
projector $\mathsf P=I-\mathsf G\mathsf L^{\dagger}\Omega_p\mathsf D$, where
$\mathsf L^\dagger$ is the zero-mean Poisson solver and $\Omega_p$ the
diagonal matrix of cell volumes (page-local). The projector satisfies
$\mathsf D\mathsf P=0$ and $\mathsf P^2=\mathsf P$. The DNS becomes
$\mathrm du/\mathrm dt=\mathsf P\mathsf F(u)$ (Eq. 7). Time integration is
Wray's explicit third-order low-storage Runge–Kutta method, with a Poisson
solve at each stage (§2.4).

**Filtering.** Applying $\Phi$ to the pressure-free form gives, exactly,

$$\frac{\mathrm d\bar u}{\mathrm dt}=\bar{\mathsf P}\,\bar{\mathsf F}(\bar u)+c(u),\qquad c(u)=\Phi\mathsf P\mathsf F(u)-\bar{\mathsf P}\,\bar{\mathsf F}(\Phi u)\quad(\text{Eqs. 11–12}).$$

The **discrete commutator error** $c$ contains the subfilter effect and
the coarse-grid discretization error together. It is the exact target for
a closure used with the coarse operator.

**Why differentiate the constraint first.** Doing so avoids filtering the
continuity equation, whose unknowns live at pressure points, and avoids
defining a filtered pressure. If the differential-algebraic system is
filtered without first differentiating the constraint, two extra
commutators appear: one in the divergence and one in the pressure. The
authors state that how to model the pressure commutator is unclear (App. D,
Eqs. D.3–D.4).

## The face-averaging filter (§3.3, App. C, App. E)

**Definition.** Coarse cells are unions of fine cells, and every coarse
face is tiled by fine faces. The filter $\Phi_{\mathrm{FA}}$ sets each
coarse face velocity to the area-weighted mean of the fine face velocities
on that face (weights fine-face area over coarse-face area, summing to
one). The filter width equals the coarse spacing. The construction follows
Kochkov et al.

**Theorem (Eq. 13; proof App. C.1–C.2).** For every $u$ with $\mathsf Du=0$,
the filtered field satisfies $\bar{\mathsf D}\,\Phi_{\mathrm{FA}}u=0$. This
holds on uniform and on non-uniform grids, in 2D and 3D. The proof is a
telescoping sum: the coarse divergence of the filtered field equals the
volume-weighted sum of the fine divergences in the coarse cell.

**Corollaries.**

- $\bar{\mathsf D}\Phi\mathsf P=0$ (Eq. 14).
- $\bar{\mathsf D}c=0$, so $c=\bar{\mathsf P}c$ and the filtered equation
  becomes $\mathrm d\bar u/\mathrm dt=\bar{\mathsf P}(\bar{\mathsf F}(\bar u)+c(u))$
  (Eqs. 15–16).
- $\bar{\mathsf D}\Phi=\Psi\mathsf D$, with $\Psi$ a volume-averaging
  filter at pressure points (Eq. C.10). In the authors' words, "the
  face-averaging velocity filter goes hand in hand with a volume-averaging
  pressure filter".
- The filter needs no modification at non-periodic boundaries.

**Limits stated by the authors (§3.3, §6, App. C.2).** The property
fails with any other weights (Gaussian weights "would not work") or with a
filter width different from the coarse spacing. It holds only for the
second-order staggered divergence, and requires the DNS grid to overlap
the LES faces. On a collocated grid a face-averaging filter can be defined
but loses divergence-consistency.

**Transfer function.** Its continuous analogue averages over the face
only, so its transfer function is a product of sinc-type factors over the
directions other than the velocity component (Eq. E.5). It therefore
damps less than the volume-averaging top-hat filter, with equality only
when the wavevector has no component along the velocity component
(Eqs. E.2, E.5).

**Comparison filter.** The volume-averaging (top-hat) filter
$\Phi_{\mathrm{VA}}$ averages over a box around each coarse face and is
not divergence-consistent.

**Other candidates (§3.4).** The authors review three other
divergence-consistent filters. Discrete differential filters are only
approximately divergence-free and do not coarsen. Spectral cutoffs are
consistent only with the spectral divergence. Projected volume-averaging
filters are consistent but non-local and more expensive.

## Two LES formulations (§4.1–§4.2, Table 1)

Replacing $c$ by $m$ gives either

$$\mathcal M_{\mathrm{DIF}}:\ \frac{\mathrm d\bar v}{\mathrm dt}=\bar{\mathsf P}\,\bar{\mathsf F}(\bar v)+m(\bar v;\boldsymbol\theta)\qquad\text{or}\qquad\mathcal M_{\mathrm{DCF}}:\ \frac{\mathrm d\bar v}{\mathrm dt}=\bar{\mathsf P}\big(\bar{\mathsf F}(\bar v)+m(\bar v;\boldsymbol\theta)\big)$$

(Eqs. 21–22). $\mathcal M_{\mathrm{DCF}}$ is equivalent to
$\bar{\mathsf D}\bar v=0$ with
$\mathrm d\bar v/\mathrm dt=\bar{\mathsf F}(\bar v)+m-\bar{\mathsf G}\bar q$,
in which the LES pressure $\bar q$ is a Lagrange multiplier (Eq. 23). With
DCF no pressure filter needs to be defined: the pressure is "implied" by
the coarse Poisson equation (Eq. 19).

| Formulation | Filter | filtered DNS divergence-free | LES divergence-free |
|---|---|---|---|
| DIF | volume averaging | no | no |
| DIF | face averaging | yes | only if $\bar{\mathsf D}m=0$ |
| DCF | volume averaging | no | yes |
| DCF | face averaging | yes | yes |

DCF with face averaging is the preferred combination. The authors stress
that Eq. 23 has the form of classical filter-first LES, but here the filter is
precisely defined and the training data are consistent with the discrete
target.

## Closures and training (§4.3–§4.4)

- **No closure.** The baseline.
- **[Smagorinsky](/methods/smagorinsky-model.md).** $m$ is the divergence
  of $2\nu_t\bar S_{ij}$, with $\nu_t=(C_s\Delta)^2|\bar S|$ and $\Delta$
  the coarse spacing (Eqs. 26–27). $C_s$ is fitted per grid, filter and
  formulation by grid search on the a posteriori error (Table B.5).
- **Staggered-grid CNN (§4.4.2, Table B.4).**
  - *Architecture.* A "collocate" layer interpolates face velocities to
    cell centres, five convolutional layers follow, and a "decollocate"
    layer interpolates back to the faces.
  - *2D size.* $5\times5$ kernels and channels $2\to24\to24\to24\to24\to2$,
    with tanh activation and bias in the inner layers and a linear last
    layer without bias; 45 696 parameters in total.
  - *3D size.* $5\times5\times5$ kernels, 234 096 parameters.
  - *Choice of output.* The authors chose not to output the divergence of
    a learned stress tensor, because $c$ also contains discretization
    effects.
- **A priori training (Eq. 24).** Minimizes the batch-averaged relative
  error $\|m(\bar u)-c(u)\|^2/\|c(u)\|^2$ over $10^4$ Adam iterations.
- **A posteriori training (Eq. 25).** Fine-tunes the a priori parameters
  on the relative trajectory error over 50 unrolled LES steps, with
  gradients obtained by automatic differentiation through the solver (see
  [model-consistent training](/methods/model-consistent-training.md)).

## Results

**Divergence of filtered DNS (§5.1.3, Table 2).**

- *2D.* DNS on $4096^2$ points at $Re=10^4$ in double precision, filtered
  to $\bar n=32,\dots,256$ points per direction. With face averaging, the
  normalized divergence of $\bar u$ is $1.5\times10^{-14}$ to
  $5.3\times10^{-14}$. With volume averaging it is 1.1, 0.67, 0.39 and 0.19
  for $\bar n=32$, 64, 128 and 256, and 8.8–12% of $c$ is not
  divergence-free.
- *3D.* DNS on $1024^3$ points in single precision. Face averaging gives
  $2.2$–$2.4\times10^{-5}$, the single-precision level. Volume averaging
  leaves 4.3% ($32^3$) to 0.94% ($256^3$) of $\bar u$, and 19% to 13% of
  $c$, non-solenoidal.
- *Commutator-error size.* It barely depends on the filter type, because
  the width is the same.

**2D Kolmogorov-forced turbulence (§5.2).** The DNS uses $4096^2$ points,
$Re=6000$ and the body force $\sin(8\pi y)$ along $x$ on the unit square,
with 6 trajectories for training and 2 for validation and testing. The
results are:

- **DCF.** The CNN clearly beats no closure and Smagorinsky in a
  posteriori error at $t=0.27$. Trained a priori, it is much better with
  face averaging than with volume averaging; a posteriori training closes
  the gap (Fig. 11). Its total kinetic energy stays at the reference level
  much longer than the other closures ($\bar n=256$, Fig. 12). Its
  spectrum stays close to the reference at $t=5$, after the trajectory has
  decorrelated ($\bar n=128$, Fig. 13).
- **DIF.** The a priori-trained CNN shows signs of instability and is
  worse than no closure at every $\bar n$ except 32. A posteriori training
  reduces the error but the energy eventually grows. The divergence of DIF
  solutions grows in time for every closure (Fig. 15).
- **Explanation of the DIF instability.** The convective discretization
  conserves energy only for divergence-free velocity fields. Without
  $\bar{\mathsf D}\bar v=0$ energy conservation is not guaranteed (§5.2.3).
  The fitted Smagorinsky coefficient for DIF falls to 0.000 at
  $\bar n=256$, which the authors attribute to the Smagorinsky term not
  being divergence-free (App. B.5).
- **No closure.** It carries too much energy at high wavenumbers, which
  the authors attribute to central-scheme oscillations. Smagorinsky
  corrects this, but every DIF CNN shows the same excess (Fig. 13).

**Further cases (App. G).**

- *2D decaying turbulence ($\bar n=128$).* Under DCF the CNN gives the
  most accurate energy, no closure is slightly too dissipative and
  Smagorinsky more so. DIF CNNs become unstable.
- *3D forced turbulence ($1024^3$, $Re=2000$, face averaging, DCF,
  $\bar n=32$ and 64).* The CNN beats no closure and Smagorinsky with
  $C_s=0.17$ in a priori and a posteriori error. Smagorinsky is too
  dissipative at high wavenumbers.

**Cost (§5.2.7, Table 3).** All runs used one Nvidia H100 GPU with the
authors' open-source Julia package IncompressibleNavierStokes.jl. A priori
training took 160.6–1583.6 s, a posteriori training 4449.3–5849.2 s, and
the DNS with filtering $1.5739\times10^4$ s.

## Qualifications

- **Printed slips in Agdestein & Sanderse (2025).**
  - Test-case naming is inconsistent. §1 announces "a decaying turbulence
    test case", but §5 is forced. App. G.2, titled "LES of forced
    turbulence (3D)", opens with "we consider a decaying turbulence test
    case" and then applies a body force.
  - App. G.2 prints the force amplitude as 5 ("the same body force as in
    the 2D case"), while Eq. 31 has amplitude 1.
  - §4.3 says the reference step uses "one RK4 time step from section
    2.4", but §2.4 defines Wray's third-order scheme.
- **Run parameters.** The §5.1 2D divergence statistics use $Re=10^4$,
  while the §5.2 LES data use $Re=6000$ on the same grid; they are
  different datasets.
- **Reynolds number.** The Reynolds number is introduced as $UL/\nu$, but
  the reference velocity and length of the test cases are not stated.
- **Symmetry of the volume-averaging transfer function.** App. E states
  that it "only depends on $\|k\|$", with spherical iso-contours in 3D. A
  product of one sinc factor per Cartesian component (Eq. E.2) is not a
  function of $\|k\|$ alone; it is isotropic only to second order near
  $k=0$ *(compiler check, not in the sources)*.
- **Scope.** All tests are periodic and wall-free, with second-order
  central differences. The authors present discretize-first as removing
  the need for backscatter clipping, a posteriori training or projection of
  the eddy viscosity (§1). In their §5.2 results, the CNN with volume
  averaging still needs a posteriori training to catch up, and DIF stays
  unstable after it; only DCF with face averaging works with a priori
  training alone.
- **Usage of "implicit LES".** The authors call any LES that keeps the DNS
  equations in their original form and adds a closure "implicit LES"
  (§1). That differs from the usage in which the discretization is the
  closure; see [implicit LES](/definitions/implicit-les.md).

# Citations

- [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md) — §1; §2 and App. A (staggered DNS, projection, Wray scheme); §3.2–§3.4, Eqs. 11–20; §4.1–§4.4, Eqs. 21–29, Table 1; §5.1–§5.2, Tables 2–3, Figs. 8–15; §6; App. B.4–B.5, Tables B.4–B.5; App. C (proofs); App. D; App. E; App. F; App. G.
