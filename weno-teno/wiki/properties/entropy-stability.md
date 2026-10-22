---
type: Property
title: "Entropy stability"
description: "A scheme is entropy stable when its discrete total entropy obeys the entropy inequality of the PDE; the page gives flux- and scheme-level conditions, including non-conservative and moving-mesh forms, entropy-stable DG and FR, correction terms, dissipation, limiting and filtering, discrete entropy tests, the KPP evidence, the limits of the property and the minimum entropy principle."
status: established
aliases: [entropy-stable scheme, entropy dissipative, ES, ED, discrete entropy inequality, entropy-stable DG, ESDG, energy stability, semi-discrete entropy stability, fully discrete entropy stability]
tags: [entropy-stable, dg, numerical-flux, bound-preserving, limiting]
timestamp: 2026-10-22T20:00:00Z
---

# Entropy stability

Entropy solutions of $\partial_tu+\nabla\cdot f(u)=0$ satisfy
$\partial_t\eta(u)+\nabla\cdot F_\eta(u)\le0$ for every convex entropy pair
$(\eta,F_\eta)$. A semi-discretization is **entropy stable**, or
entropy-dissipative (ED), when its quadrature-weighted total entropy obeys
the discrete analogue. It is non-increasing apart from boundary fluxes,
and locally its change is an entropy-flux difference plus a non-positive
production. It is **entropy-conservative** (EC) when the production
vanishes. In the sources, scheme-level EC/ED is built from the flux-level
conditions of Tadmor on a two-point flux $h$: $[\![w]\!]\cdot h=[\![\psi]\!]$ (EC, $h=f^{\mathrm{ec}}$) and
$[\![w]\!]\cdot h-[\![\psi]\!]\le0$ (ED)
([Ranocha et al. (2023)](/sources/ranocha-2023.md), Def. 2.5;
[entropy-conservative and kinetic-energy-preserving two-point fluxes](/methods/entropy-conservative-flux.md)).

## Flux-level and scheme-level conditions

[Renac (2021)](/sources/renac-2021.md) lists the requirements on a
directional two-point flux $h(u^-,u^+,n)$: symmetry and consistency of the
entropy-conservative flux, the inequality $[\![w]\!]\cdot h\le[\![\psi\cdot n]\!]$
for the entropy-stable one, conservation $h(u^-,u^+,n)=-h(u^+,u^-,-n)$, and
Lipschitz continuity (§3.1, Eqs. (19)–(23)). He does not prove the flux
inequality directly for his relaxation flux. It follows from an entropy
inequality of the whole three-point scheme by a lemma of Bouchut, as he
recalls it (§3.2, §4.3.2).

**Non-conservative systems.** For GLM-MHD with the Powell and GLM
non-conservative terms, [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md)
generalize Tadmor's condition (Eq. (51)). With page-local
$\Phi^\diamond_{(j,k)}$ the surface non-conservative term between nodes $j$
and $k$, and $\psi$ the entropy flux potential augmented by the
non-conservative contribution (their Eq. (21)), the condition reads

$$[\![w]\!]_{(j,k)}\cdot h_{(j,k)}+w_k\cdot\Phi^\diamond_{(k,j)}-w_j\cdot\Phi^\diamond_{(j,k)}=[\![\psi]\!]_{(j,k)} .$$

Its left-hand side minus its right-hand side is the entropy production
$r_{(j,k)}$ of the interface (Def. 2, Eq. (55)); the scheme dissipates
entropy where $r_{(j,k)}\le0$. The matching numerical entropy flux is
symmetric (Def. 1, Eq. (54)).

**Moving curvilinear meshes.** [Duan & Tang (2022)](/sources/duan-2022.md)
write the entropy inequality of relativistic (M)HD in time-dependent
curvilinear coordinates, $\partial_\tau(J\eta)+\sum_k\partial_{\xi_k}(\cdot)\le0$,
which holds under the geometric conservation laws (Eqs. (2.10)–(2.11)).
They give a sufficient two-point condition with metric averages and the
non-conservative symmetrizing source (Def. 3.1), prove that the
high-order finite-difference scheme built on it is entropy conservative
(Thm. 3.2), and that the TeCNO-type scheme with a WENO dissipation and a
sign switch satisfies the semi-discrete entropy inequality (Thm. 4.1;
[adaptive moving mesh](/methods/adaptive-moving-mesh.md),
[TeCNO schemes](/methods/tecno-scheme.md)). Li, Duan & Tang (2022) state
the same properties for the stiffened gas with reference to Duan & Tang
(Prop. 3.1).

**Semi-discrete and fully discrete.** All the conditions above are
semi-discrete. [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md)
separate semi-discretely entropy-conservative or dissipative schemes from
fully discrete ones; the semi-discrete property becomes fully discrete only
with relaxation, artificial viscosity, implicit time stepping or, for
their deferred-correction residual-distribution schemes, a correction of
the whole space–time residual (Remark 2.2).

## Entropy-stable DG

The flux-differencing DGSEM is EC when its symmetric volume flux is EC and
its surface flux is EC. It is ED when the surface flux is ED instead.
This holds on diagonal-norm SBP elements (Ranocha et al. (2023), §2,
citing Carpenter et al. and Gassner–Winters–Kopriva;
[flux differencing](/methods/flux-differencing.md),
[summation-by-parts operator](/operators/summation-by-parts-operator.md)).
[Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) use
an EC volume flux with a local Lax–Friedrichs surface flux, and state that
the resulting scheme "satisfies a discrete entropy inequality" (§5.1).

Two sources apply the construction to new systems:

- **Multicomponent Euler.** Renac (2021) combines his EC flux in the
  volume with an entropy-stable relaxation flux at the interfaces on
  straight-sided unstructured quadrilaterals. The scheme satisfies a cell
  entropy inequality, as an instance of the Fisher–Carpenter framework
  (§5.2, Eqs. (62)–(64)).
- **Resistive GLM-MHD.** Rueda-Ramírez et al. (2021) prove the element
  entropy balance of the split-form DGSEM with non-conservative terms
  (Lemma 2, Eq. (61)). Its volume part is $\sum_{j,k}Q_{jk}r_{(j,k)}$. Since
  $Q$ has entries of both signs, a dissipative volume flux gives an
  "unpredictable" entropy balance, so the volume flux must be EC and the
  dissipation must sit in the surface flux (§3.3.2;
  [summation-by-parts operator](/operators/summation-by-parts-operator.md)).
  The visco-resistive terms keep the estimate when BR1 is applied to the
  gradients of the entropy variables, as recalled from earlier work (§2,
  Eqs. (38)–(39)).

**Correction terms instead of fluxes.** Abgrall et al. (2022) obtain an
element-wise entropy equality or inequality without entropy-conservative
fluxes, by adding to any baseline scheme the smallest correction that
enforces it; with the inequality constraint, the baseline is left
unchanged in elements where it already dissipates enough entropy
(Thms. 2.8, 3.1; [entropy correction term](/methods/entropy-correction-term.md)).
On the inviscid Taylor–Green vortex the corrected central schemes conserve
entropy and still blow up, earlier than flux differencing (§4.2.2).

**Flux reconstruction.** For energy-stable flux reconstruction the
relevant norm is the broken Sobolev norm $M+K_{\mathrm{FR}}$ (page-local
$K_{\mathrm{FR}}$ the correction operator). [Cicchino, Nadarajah & Del Rey
Fernández (2022)](/sources/cicchino-2022.md) prove for 1D Burgers that the
classical split form, with the correction acting only on the surface terms,
leaves a volume term without sign in the energy balance, so no nonlinear
stability claim can be made, and that applying the correction to the
volume terms as well gives energy (square-entropy) stability for an
energy-conservative or local Lax–Friedrichs interface flux (Eqs. (23),
(46)–(50); [flux reconstruction](/methods/flux-reconstruction.md)). Their
numerical energy is conserved to $O(10^{-12})$ or decreases monotonically,
while the classical split form does neither (Tables 1–3).

On Legendre–Gauss nodes, entropy stability needs two further ingredients:

- the hybridized SBP operator;
- an entropy projection, $\tilde u=u(\mathcal Rw(\mathbf u))$, for the
  surface states.

Ranocha et al. (2023) measure this variant at 1.5× to 5× the cost of the
LGL scheme (§6). Ranocha et al. also state, citing the literature, that
flux differencing comes with stability guarantees that overintegration
lacks, and that it stays stable where overintegration fails (§5).

As recalled by Rueda-Ramírez et al. (2022), the classical DG cell entropy
inequality for the square entropy (Jiang–Shu) needs exact volume and surface
integration. That is not feasible for the non-polynomial KPP flux, which is
why the split form is used there (§5.1).

## Which robustness steps keep it

Rueda-Ramírez et al. (2022) map three cases (§2.2, §4; see
[subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md)):

- **Element-wise blending.** One coefficient $\alpha$ per element blends an
  ES DGSEM with an ES finite-volume scheme. The finite-volume scheme uses
  first-order fluxes, or minmod TVD reconstruction of scaled entropy
  variables after Fjordholm–Mishra–Tadmor. The blend stays provably entropy
  stable as long as both schemes share the surface terms. The proofs, for
  Euler and MHD, are cited from Hennemann et al. and follow-ups.
  Rueda-Ramírez et al. (2021) is one of these follow-ups. Their blending
  lemma (Lemma 3; Lemma 6 in 3D) takes any two schemes with identical
  element-boundary terms and arbitrary interior terms. The entropy balance
  of the blend is the boundary part plus $(1-\alpha)$ times the DG interior
  production plus $\alpha$ times the finite-volume one (Eqs. (64), (68)).
  The blend is therefore EC if both parts are EC, for any element-wise
  $\alpha$, and ES if one part is ES and the other EC or ES (Eq. (69)). The
  lemma covers non-conservative terms and the second-order
  [TeCNO-type subcell scheme](/methods/tecno-scheme.md).
- **Subcell-wise blending.** One coefficient per subcell interface is used.
  The proof of entropy dissipation is "still missing" (§4, item 2).
- **A posteriori limiting.** Invariant-domain bounds from Guermond–Popov bar
  states, plus a local minimum principle on the modified specific entropy
  $e\rho^{1-\gamma}$, guarantee positivity of density and pressure and a
  discrete entropy inequality (§5.2.2, citing Guermond et al.). Rueda-Ramírez
  et al. note that this quantity is cheaper than $s$ and better suited to
  Newton's method. Here $e\rho^{1-\gamma}=\exp(s)/(\gamma-1)$ with
  $s=\ln(p\rho^{-\gamma})$, a monotone function of the physical entropy
  *(compiler check, not in the sources: use $p=(\gamma-1)\rho e$)*. These
  bounds hold for the Rusanov low-order scheme. With HLLE or second-order
  finite volumes they are not guaranteed, and the algorithm returns the
  solution "closest to the restrictions" (§5.2.3).

## Dissipation operators

In the sources an ES flux is an EC flux minus a dissipation. In Rueda-Ramírez
et al. (2021), Li, Duan & Tang (2022) and Renac's Roe-type flux the
dissipation acts on the jump of the entropy variables, not of the
conserved variables, which is what gives the production a provable sign.

- **Lax–Friedrichs on $[\![u]\!]$.** As recalled by Rueda-Ramírez et al.
  (2021) after Derigs et al., $f^{\mathrm{ec}}-\tfrac12a[\![u]\!]$ is not
  entropy stable for MHD (§3.3.1, Eq. (52)).
- **Dissipation on $[\![w]\!]$.** Replacing $[\![u]\!]$ by
  $\frac{\partial u}{\partial w}[\![w]\!]$ at a mean state, with Barth's
  eigenvector scaling, gives the production
  $-\tfrac12[\![w]\!]^\top D_w[\![w]\!]\le0$ with a symmetric positive-definite
  page-local matrix $D_w$ (Eqs. (57)–(60)). The "ES Rusanov" flux of their
  tests puts the largest advective eigenvalue in every entry of the
  eigenvalue matrix (§6).
- **Reconstructed jumps.** Applying the dissipation to reconstructed jumps
  raises its order and keeps the sign if the reconstruction has the sign
  property ([TeCNO schemes](/methods/tecno-scheme.md);
  [Li, Duan & Tang (2022)](/sources/li-2022-c.md), Eq. (3.21)).
- **Robustness of "EC plus dissipation".** Renac (2021) proves that a
  Roe-type flux, his EC flux minus a scalar dissipation on the entropy
  variables, is ES (App. D.1, Eq. (D.1)). He argues that such fluxes are
  not Lipschitz continuous, which blocks the positivity proofs, and they
  are expensive because of the logarithmic means (§1.2). In his tests the
  Roe-type flux needs CFL 0.2 instead of 0.4 and the 2D runs stop on
  negative states (App. D, Figs. D.9–D.10). His alternative is a
  relaxation solver, Bouchut's pressure relaxation composed with a
  Coquel–Perthame energy relaxation. It is ES and positive under
  $\frac{\Delta t}{\Delta x}\max(\lvert v\cdot n\rvert+a_{\mathrm L}/\rho)<\tfrac12$, with page-local Lagrangian
  sound speed $a_{\mathrm L}$, provided the relaxation constant exceeds every
  component's ratio of specific heats (§4.3–4.4, Eqs. (36), (52)).

## Filtering, viscosity and the entropy balance

Shock-capturing steps outside the flux also move the entropy:

- **Solution filtering.** [Edoh (2022)](/sources/edoh-2022.md) writes a
  conservative solution filter in its semi-discrete limit as an artificial
  dissipation operator $\bar{\mathcal D}\le0$ (page-local) and finds that
  filtering the total energy tends to decrease the global entropy, an
  unphysical effect, filtering the momentum tends to increase it, and
  filtering the mass is indefinite (App. B, Eqs. (B.2)–(B.5); periodic
  domain, unit norm). His "entropy-stability-promoting" filter acts on the
  momentum only; on the isentropic vortex it gives strict kinetic-energy
  decay and entropy increase for all his kinetic-energy-preserving
  splittings, while the Kennedy–Gruber split with all variables filtered
  keeps kinetic energy but decreases entropy (Figs. 1, B.5).
- **Entropy-bounded filtering.** [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md)
  choose the strength of a modal filter so that the nodal values satisfy a
  local discrete minimum entropy bound (below;
  [entropy filtering](/methods/entropy-filtering.md)).
- **Time-reversibility viscosity.** [Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md)
  use entropy production as a sensor: where an entropy is conserved the
  system is invariant under $t\to-t$, and at shocks the entropy condition
  makes the entropy solution irreversible, as they recall after Dafermos.
  The defect of a forward–backward step pair sets the viscosity; unlike
  entropy viscosity it needs no entropy pair (§2;
  [artificial viscosity](/methods/artificial-viscosity.md)).

## Entropy stability does not give positivity

The entropy analysis assumes positive density and pressure. Rueda-Ramírez
et al. (2021) note that high-order oscillations at strong shocks can
violate positivity and crash an ES scheme (§1). On the GEM reconnection
challenge their ES DGSEM without subcell stabilization crashes for that
reason (§6.3). Renac (2021) builds positivity in separately: the
relaxation flux makes the first-order scheme positive, the DGSEM cell
averages stay admissible under a CFL condition, and a Zhang–Shu-type
limiter restores the nodal values (Theorem 6.1, Eq. (67);
[bound preservation](/properties/bound-preservation.md)). Abgrall et al.
(2022) find the same in their Taylor–Green tests: corrected schemes that
conserve entropy blow up once nodal density or pressure turns negative,
after which the entropy variables cannot even be formed (§4.2.2, §6).

## Entropy conservation is not robustness

Abgrall et al. (2022) state that "EC/D is not the holy grail" (§4):

- a single-block finite-difference or Fourier collocation scheme is one
  element, so an entropy correction gives only a global entropy balance;
  on periodic Burgers data with a stationary shock and a rarefaction, the
  central scheme with or without correction stays at a stationary,
  non-entropic solution, because the entropy defect is zero
  (Example 2.12);
- nodal DG with closed Newton–Cotes (Boole) quadrature for linear
  advection has an entropy error that falls with the fourth power of
  $\Delta t$, yet highly oscillatory solutions (App. A.2, Fig. 10);
- a bad baseline remains bad when it is forced to be entropy conservative
  or dissipative (§4, App. A.2).

They also note that for a scalar law and a fixed entropy the
entropy-conservative flux is unique, so DG surface fluxes cannot in
general make several entropies conserved at once, while Osher's E-schemes,
which satisfy all entropy inequalities, are at most first order
(Remark 3.3). Together with the KPP evidence below, this places entropy
stability as a necessary ingredient whose sufficiency the sources do not
claim.

## Discrete entropy tests

With EC fluxes everywhere, the semi-discrete total entropy is conserved,
and the fully discrete error is a time-integration error.

- **Renac (2021)**, multicomponent Riemann problem on a periodic domain,
  100 cells, $N=3$, SSP-RK(4,3). The global entropy error falls from
  $-6.34\times10^{-8}$ to $-2.89\times10^{-11}$ as $\Delta t$ is halved four
  times, at observed order 3.00, the order of the time integrator. With the
  ES flux the entropy change is $-7.70\times10^{-7}$ independent of
  $\Delta t$ (§7.2, Table 3).
- **Rueda-Ramírez et al. (2021)**, weak magnetic blast on the warped 3D
  mesh, $N=4$ and $6$, SSP-RK(5,4). The EC entropy error converges to zero
  at fourth order in the CFL number, down to machine precision; the ES and
  TVD-ES schemes dissipate (§6.1, Fig. 5).
- **Li, Duan & Tang (2022)**, finite differences on a moving mesh. The EC
  scheme keeps the total entropy almost constant on the isentropic
  vortex, and the ES scheme decays it monotonically, in 2D and 3D (Ex. 5.1,
  5.5, plotted curves only; [adaptive moving mesh](/methods/adaptive-moving-mesh.md)).
  Their sufficient condition for an EC flux on a moving curvilinear mesh
  weights the jumps of the entropy potential and of the flux potentials
  with averaged metric terms (Prop. 3.1, Eq. (3.5)); its proof is deferred
  to Duan & Tang, and is in Duan & Tang (2022), Thm. 3.2.
- **Duan & Tang (2022)**, relativistic MHD on a moving mesh. The discrete
  total entropy stays constant for the sixth-order EC scheme and decays
  monotonically for the fifth-order ES scheme, on the 2D vortex at
  $N_x=160$ to $t=4$ and on the 3D vortex to $t=0.1$ (Figs. 6.4, 6.14).

Renac and Rueda-Ramírez et al. attribute the EC residual to the time
integrator, and the observed orders 3 and 4 are the orders of their
Runge–Kutta methods
(Renac (2021), §7.2; Rueda-Ramírez et al. (2021), §6, §6.1).

## Evidence: the KPP problem

The [KPP rotating wave](/benchmarks/kpp-rotating-wave.md), with its
non-convex flux $f=(\sin u,\cos u)$, separates entropy-stable from merely
non-oscillatory schemes:

- **Rueda-Ramírez et al. (2022)** (§5.1, Figs. 2–3; $N=3$, $32^2$ to $256^2$
  elements, $t=1$, element-wise shock capturing with $\alpha_{\max}=0.5$).
  The standard DGSEM gives clean, essentially non-oscillatory but
  **non-entropic** solutions. Its spurious structures even trigger the
  shock sensor. The ES split-form DGSEM, with the scalar EC flux in the
  volume and LLF at surfaces, converges to the entropy solution. Shock
  capturing alone does not fix the entropy.
- **[Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md)** (§7.4, Figs. 6–8;
  $Q_p$ continuous elements, $N_h=129^2$ degrees of freedom). The lumped-mass Galerkin scheme
  oscillates and produces an entropy-violating shock. High-order
  stabilization alone reduces the oscillations but not the entropy defect.
  The low-order and WENO-blended schemes reproduce the spiral entropy
  solution. The authors note that a non-symmetric variational multiscale
  stabilization "may produce entropy", which is why they use a symmetric one
  (§3). Entropy inequalities can be enforced on top via algebraic flux
  correction (§7.4).

As recalled by Rueda-Ramírez et al. (2022), monotone and
maximum-principle-satisfying schemes can still converge to non-entropic
solutions when they lack a discrete entropy inequality (§5.1).

## Minimum entropy principle as a convex bound

[Wu & Shu (2023)](/sources/wu-2023-b.md) use Tadmor's minimum entropy
principle in the form $p\rho^{-\gamma}\ge s_{\min}'$, with $s_{\min}'$
(page-local, their $S_{\min}$) the initial minimum of $p\rho^{-\gamma}$. Together
with positivity it defines a convex invariant region, so it can be enforced
as a [bound-preservation](/properties/bound-preservation.md) constraint
rather than through fluxes (§2, Eq. (2.3)).

[Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) enforce a
*local discrete* minimum entropy principle on the nodal values of nodal DG
and FR. With the physical sign convention, an entropy $\sigma$ that
increases across shocks (page-local), the bound for element $K$ is the
minimum of $\sigma$ over the nodes of $K$ and of its face neighbours at the
previous stage. For an explicit scheme under a CFL condition they take this
neighbourhood to contain the domain of influence of the element over one
step, so that the local minimum is non-decreasing in time over its domain
of influence (§3.2,
Eqs. (20)–(21)). For Euler they take $\sigma=\rho\ln(p\rho^{-\gamma})$,
with a tolerance $10^{-4}$ on the bound (§4.1, §4.3,
[entropy filtering](/methods/entropy-filtering.md)).

Wu & Shu represent it, by
[geometric quasilinearization](/methods/geometric-quasilinearization.md), as
a family of constraints linear in $u$ (Thm 4.7; Eq. (2.3)). For 1D Euler the
family is

$$u\cdot n_*+s_{\min}'\rho_*^{\gamma}\ge0,\qquad n_*=\Big(\tfrac12v_*^2-\frac{\gamma s_{\min}'\rho_*^{\gamma-1}}{\gamma-1},\,-v_*,\,1\Big)^\top,$$

for all free auxiliary $\rho_*>0$ and $v_*\in\mathbb R$. They give the relativistic analogue in Thm 4.10. The local minimum principle on
$e\rho^{1-\gamma}$ in the subcell limiting of Rueda-Ramírez et al. (2022) is
a discrete, local relative of the same principle.

## Qualifications

- **Convergence is asserted, not proved.** Rueda-Ramírez et al. (2022) state
  that the ES DGSEM "will therefore converge to the unique entropic
  solution" of KPP. The support is numerical (Fig. 2). No convergence
  theorem for high-order DG on non-convex fluxes is given in the source.
- **Sign conventions.**
  - Ranocha et al. (2023) write a mathematical entropy and define ED by
    "$\le$", i.e. production $\le0$, as in the registry
    ($\eta=-\rho s/(\gamma-1)$ for Euler); they do not state the sign
    convention or the convexity explicitly.
  - The KPP tests use $\eta=\tfrac12u^2$.
  - Renac (2021) and Li, Duan & Tang (2022) use the mixture entropy
    $\eta=-\rho s$ with the specific entropy of the mixture, without the
    factor $1/(\gamma-1)$; Rueda-Ramírez et al. (2021) use
    $\eta=-\rho s/(\gamma-1)$ as in the registry. All three take $\eta$
    convex and require production $\le0$.
  - The minimum principles of Rueda-Ramírez et al. (2022) and Wu & Shu bound
    functions of the physical specific entropy from below.
  - Duan & Tang (2022) use the convex
    $\eta=-\rho Ws/(\gamma-1)$ of relativistic flows, with production
    $\le0$ (Eq. (2.3)). Dzanic & Witherden (2022) use the physical sign,
    $\partial_t\sigma+\nabla\cdot\Sigma\ge0$ (page-local entropy flux
    $\Sigma$), opposite to Tadmor's (§2.1), yet call $\sigma$ "some convex
    entropy functional" (§3); with the physical sign $\rho s$ is concave
    in $u$, since $-\rho s/(\gamma-1)$ is the registry's convex entropy
    *(compiler check, not in the sources)*.
- **Which entropy the minimum principle bounds** *(compiler check, not in
  the sources: the comparison is the compiler's; the functional is printed
  in Dzanic & Witherden's §4.1, checked on the PDF)*. Tadmor's minimum
  principle, in the forms used by Wu & Shu and by Rueda-Ramírez et al.
  (2022), bounds a function of the *specific* entropy. Dzanic & Witherden
  bound the density-weighted $\sigma=\rho\ln(p\rho^{-\gamma})$ instead
  (§4.1). They state that the entropy pair can be chosen arbitrarily, "the
  particular choice of which is posited to have a minor overall effect"
  (§3.2), and do not test the choice. Their set
  $\{\rho s\ge\sigma_{\min}\}$ is convex, as the superlevel set of a
  concave function, but the sources give no argument that a local minimum
  of $\rho s$ is non-decreasing for entropy solutions.
- **Printed slip.** Renac's cell entropy inequality (64) prints the
  surface sum without the quadrature weight, while the analogous sum in
  the proof of his Theorem 6.1 carries it. The weight is missing in (64).

# Citations

- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — Def. 2.5, §2, §5, §6.
- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — §2.2, §4 items (1)–(3), §5.1 Eqs. (37)–(40) Figs. 2–3, §5.2.2 Eqs. (47)–(48), §5.2.3.
- [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) — §3, §7.4 Figs. 6–8.
- [Wu & Shu (2023)](/sources/wu-2023-b.md) — Eq. (2.3), Thms 4.7, 4.10.
- [Renac (2021)](/sources/renac-2021.md) — §1.2, §3.1–3.2 Eqs. (19)–(23), §4.3–4.4 Eq. (52), §5.2 Eqs. (62)–(64), Theorem 6.1, Eq. (67), §7.2 Table 3, App. D (arXiv v3).
- [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) — §1, §2 Eqs. (21), (38)–(39), §3.3 Eqs. (51)–(69), Lemmas 2–3, §6.1 Fig. 5, §6.3 (arXiv v1).
- [Li, Duan & Tang (2022)](/sources/li-2022-c.md) — Prop. 3.1 Eq. (3.5), Eq. (3.21), Ex. 5.1, 5.5 (arXiv v1).
- [Duan & Tang (2022)](/sources/duan-2022.md) — §2 Eqs. (2.3), (2.10)–(2.11), Def. 3.1, Thm. 3.2, Thm. 4.1, Figs. 6.4, 6.14 (arXiv v1).
- [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) — Remark 2.2, Thms. 2.8, 3.1, Example 2.12, Remark 3.3, §4, §4.2.2, §6, App. A.2 Fig. 10 (arXiv v4).
- [Cicchino, Nadarajah & Del Rey Fernández (2022)](/sources/cicchino-2022.md) — §3 Eq. (23), §3.1.2 Eqs. (43)–(50), Tables 1–3 (arXiv v1).
- [Edoh (2022)](/sources/edoh-2022.md) — App. B Eqs. (B.1)–(B.5), Figs. 1, B.5.
- [Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) — §2 (arXiv v2).
- [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) — §2.1 Eqs. (2)–(4), §3.2 Eqs. (20)–(21), §4.1, §4.3 (arXiv v3).
