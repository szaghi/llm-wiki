---
type: Property
title: "Entropy stability"
description: "A scheme is entropy stable when its discrete total entropy obeys the entropy inequality of the PDE; the page gives flux- and scheme-level conditions, including non-conservative and moving-mesh forms, entropy-stable DG and FR, correction terms, dissipation, limiting and filtering, discrete entropy tests, the KPP evidence, the limits of the property and the minimum entropy principle."
status: established
aliases: [entropy-stable scheme, entropy dissipative, ES, ED, discrete entropy inequality, entropy-stable DG, ESDG, energy stability, semi-discrete entropy stability, fully discrete entropy stability]
tags: [entropy-stable, dg, numerical-flux, bound-preserving, limiting]
timestamp: 2026-10-23T20:40:00Z
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
Lipschitz continuity (§3.1, Eqs. (19)–(23)). Renac does not prove the flux
inequality directly for the proposed relaxation flux. It follows from an entropy
inequality of the whole three-point scheme by a lemma of Bouchut, as the author
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

**Balance laws with entropy-neutral sources.** For the two-fluid
relativistic plasma equations,
[Bhoriya, Kumar & Chandrashekar (2023)](/sources/bhoriya-2023.md) prove
that smooth solutions satisfy $\partial_ts+v_1\partial_xs=0$ for each species
despite the Lorentz-force sources, so every species entropy
$\eta=-\rho Ws/(\gamma-1)$ satisfies an entropy equality (Prop. 3.1, App. A).
Discretely the source does not enter the entropy balance because it is
orthogonal to the entropy variables, $w\cdot S(u)=0$, which rests on
$v\cdot S_{\rho v}=S_E$ for the momentum and energy rows of the source
(proof of Thm. 4.2). The flux has three independent blocks (ions,
electrons, Maxwell), so entropy stability reduces to that of the two fluid
blocks: with an EC flux plus a dissipation on ENO-reconstructed scaled
entropy variables the semi-discrete scheme satisfies the entropy
inequality for **any** discretization of the Maxwell block (Thm. 4.3,
Remark 4.3; [entropy-conservative two-point fluxes](/methods/entropy-conservative-flux.md),
[TeCNO schemes](/methods/tecno-scheme.md)). The time integrators, explicit
SSP Runge–Kutta and ARK-IMEX with the stiff source implicit, are not
claimed to keep the property; at equal order the explicit and IMEX runs
show almost the same entropy decay on the two-fluid Brio–Wu problem, and
third and fourth order dissipate less entropy than second (§6.1.2, Fig. 1).
The authors recall that entropy solutions of multi-dimensional systems can
be non-unique and still call entropy stability "one of the few nonlinear
stability estimates" (§1).

**Ideal MHD: symmetrized or conservative form.** The conservative ideal
MHD system is not symmetrizable. With the
[Godunov–Powell term](/definitions/godunov-powell-source-term.md) added
it is, and Tadmor's condition gains a term in the jump of the
Godunov–Powell potential
([entropy-conservative fluxes](/methods/entropy-conservative-flux.md)).
[Liu et al. (2025b)](/sources/liu-2025-b.md) discretize this modified
system with nodal DG on LGL points. They prove semi-discrete entropy
stability for an entropy-conservative volume flux and an entropy-stable
surface flux (Thm. 3.1, proof cited to Liu, Shu & Zhang). The scheme is
not conservative because of the source term, and the authors state that
a DG method that is at once conservative, globally divergence-free,
entropy stable and positivity preserving "remains open" (Remark 3.2).

[Liu et al. (2025c)](/sources/liu-2025-c.md) take the conservative system
instead. They state that schemes for the modified system "are inherently
nonconservative", which "can lead to numerical instability and
nonphysical features" (§1). Their Thm. 1 assumes a nodal field that is
divergence-free at every Gauss–Lobatto node and normal-continuous across
faces. The source-term contributions then cancel, so the conservative
flux-differencing scheme is entropy conservative within each element and
entropy stable globally, for periodic, compactly supported or reflective
boundaries (§3.1, App. B). At a reflective wall the HLL flux reduces to
Lax–Friedrichs, and the wall production is $-2\rho^2v_1^2s^+/p\le0$, with
$s^+=-s^-$ the HLL speed (their $-4\beta\rho u_x^2S$, $\beta=\rho/(2p)$).
Without the divergence-free field the conservative scheme "cannot achieve
the entropy stability" (§3.1). Liu et al. (2025c) compare the two routes
through Liu, Shu & Zhang's 2018 scheme for the modified system, the base
of Liu et al. (2025b), not through Liu et al. (2025b) itself (§5)
([divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)).

**Semi-discrete and fully discrete.** All the conditions above are
semi-discrete. [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md)
separate semi-discretely entropy-conservative or dissipative schemes from
fully discrete ones; the semi-discrete property becomes fully discrete only
with relaxation, artificial viscosity, implicit time stepping or, for
their deferred-correction residual-distribution schemes, a correction of
the whole space–time residual (Remark 2.2).

**Staggered grids with a potential source.**
[Goudon & Minjeaud (2024)](/sources/goudon-2024.md) prove a semi-discrete
entropy inequality for an explicit, well-balanced staggered finite-volume
scheme for the barotropic Euler equations with source $-\rho\,\partial_xz$
(page-local potential $z$; shallow water for $p=\rho^2/2$), densities on
primal cells and velocities on the dual nodes. The entropy is the total
energy $\tfrac12\rho v^2+\Phi(\rho)+\rho z$, with page-local internal energy
$\Phi$, $\rho\Phi'-\Phi=p$ (Eq. (29)). The proof combines a discrete
internal-plus-potential energy inequality on the primal cells with a
kinetic-energy inequality on the dual cells, averaged over two dual nodes,
to give $\frac{d}{dt}\eta_{j+1/2}+(H_{j+1}-H_j)/\delta x_{j+1/2}\le0$
(page-local discrete entropy $\eta_{j+1/2}$ and flux $H_j$); its key step is an
inequality for hydrostatically reconstructed states, obtained from the
source-free lemma of the authors' earlier scheme (pp. 1272–1275, Eqs.
(30)–(35); [well-balancing](/properties/well-balancing.md)). The fully
discrete inequality is left open. For collocated hydrostatic-reconstruction
schemes they recall that it has been shown only up to an error vanishing
with the mesh, or with ad hoc artificial viscosity (p. 1275).

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

- **Multicomponent Euler.** Renac (2021) combines the author's EC flux in the
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
[Cicchino & Nadarajah (2025)](/sources/cicchino-2025.md) carry the result to
the 3D Euler equations on curvilinear hexahedra: with Chan's hybridized
flux differencing on [entropy-projected](/methods/entropy-projection.md)
states, an EC volume flux satisfying Tadmor's condition on all volume and
surface node pairs and an EC surface flux, the scheme conserves entropy in
the $(M_K+K_{\mathrm{FR}})$ norm (page-local $M_K$ the mass matrix of
element $K$, $K_{\mathrm{FR}}$ the FR correction operator), for any correction parameter and any
quadrature exact to degree $2N-1$ (Thm. 6.3, Eqs. (54)–(58)). For the
classical ESFR flux differencing of Ranocha et al. and Abe et al. the volume
term keeps a factor $(M_K+K_{\mathrm{FR}})M_K^{-1}$ in the entropy statement,
"which renders it unstable" (Eq. (56)). Entropy dissipation is added through
the jump of the projected entropy variables: as they recall from
Chandrashekar, a positive scalar times the jump of the conservative
variables does not provably dissipate entropy (§6.3). The inviscid
Taylor–Green vortex keeps the entropy change at $O(10^{-13})$ on Gauss and
LGL nodes, with and without overintegration, while conservative DG on Gauss
nodes diverges (§7.3).

On Legendre–Gauss nodes, entropy stability needs two further ingredients:

- the hybridized SBP operator;
- an entropy projection, $\tilde u=u(\mathcal Rw(\mathbf u))$, for the
  surface states.

Ranocha et al. (2023) measure this variant at 1.5× to 5× the cost of the
LGL scheme (§6). [Schwarz et al. (2025)](/sources/schwarz-2025.md) compare
the two entropy-stable collocation DGSEMs, with the entropy pair
$\eta=-\rho s/(\gamma-1)$, $F_\eta=\eta v$ and the Chandrashekar volume flux,
on compressible turbulence in FLEXI: the Gauss scheme is more accurate at
equal $N$ and about twice as expensive, and the authors judge it the more
efficient per accuracy (§2.2, §3.3–3.4, §4; [DGSEM](/methods/dgsem.md)). Ranocha et al. also state, citing the literature, that
flux differencing comes with stability guarantees that overintegration
lacks, and that it stays stable where overintegration fails (§5).

As recalled by Rueda-Ramírez et al. (2022), the classical DG cell entropy
inequality for the square entropy (Jiang–Shu) needs exact volume and surface
integration. That is not feasible for the non-polynomial KPP flux, which is
why the split form is used there (§5.1).

**Modal DG with projected entropy variables.**
[Alberti et al. (2025)](/sources/alberti-2025.md) target the global
condition $\int_\Omega\partial_t\eta\,dx\le0$ (Eq. (16)) in a modal DG solved
in conservative variables with all operators evaluated at the projected
entropy variables. The convective part is made entropy conservative or
stable by an [entropy correction term](/methods/entropy-correction-term.md)
that removes the quadrature error of each element, together with a Tadmor
interface flux (Eqs. (20)–(25)). The viscous part is made entropy stable by
projecting the viscous flux onto the DG space before it enters the
Bassi–Rebay surface terms: $\Pi_{\mathrm{BR1}}$ gives the exact production
$-\sum_K\int_K(\partial w_h+R)^\top\mathsf K(\partial w_h+R)\le0$ and
$\Pi_{\mathrm{BR2}}$ an upper bound (Eqs. (40)–(47); page-local lifting $R$ and
viscous matrices $\mathsf K$;
[Bassi–Rebay](/methods/bassi-rebay-viscous-discretization.md)). They add
that a globally increasing $\rho s$ does not guarantee consistent entropy
evolution in every element, and that only the projected viscous schemes
control the local entropy production (§3.2.2).

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

**Interface-wise entropy limiting in monolithic convex limiting.**
[Rueda-Ramírez, Bolm, Kuzmin & Gassner (2024)](/sources/ruedaramirez-2024.md)
limit the subcell fluxes of the LGL-DGSEM at the semi-discrete level, so
that the spatial operator does not depend on $\Delta t$
([DGSEM](/methods/dgsem.md), [convex limiting](/methods/convex-limiting.md)).
After the bound-preserving limiters, a last factor
$\alpha^s_{(i,j)}\in[0,1]$ (page-local) scales the limited anti-diffusive
flux so that each subcell flux satisfies Tadmor's condition,
$[\![w]\!]_{(i,j)}\cdot\hat f_{(i,j)}\le[\![\psi]\!]_{(i,j)}$ with
$\hat f_{(i,j)}=\hat f^{\mathrm{FV}}_{(i,j)}+\alpha^s_{(i,j)}\Delta\hat f^{\mathrm{Lim}}_{(i,j)}/(i-j)$
(Eqs. (37)–(39), after Kuzmin, Hajduk & Rupp; arXiv v1). The condition is
linear in $\alpha^s$, so the factor is closed-form, and the authors stress
that all their correction factors are, unlike predictor–corrector schemes
that solve nonlinear equations (Remark 9). Substituting the blended flux
gives $\alpha^s\le\big([\![\psi]\!]-[\![w]\!]\cdot\hat f^{\mathrm{FV}}\big)/\big([\![w]\!]\cdot\Delta\hat f^{\mathrm{Lim}}/(i-j)\big)$
when the denominator is positive, and the numerator is non-negative when
the low-order flux itself satisfies Tadmor's condition *(compiler check,
not in the sources)*. The
predictor–corrector alternative of their 2022 paper, which they compare
against, takes a local minimum of $e\rho^{1-\gamma}$ as bound (§3.2, Eq.
(51)).

[Lin, Chan & Tomas (2023)](/sources/lin-2023.md) add positivity to
entropy-stable nodal DG for Euler and Navier–Stokes, on quadrilaterals and
triangles, and keep the semi-discrete entropy inequality (§5–6; arXiv v2):

- **The low-order scheme is entropy stable.** Their low-order scheme is
  the skew-symmetric DG form with a sparse low-order SBP operator and a
  graph viscosity. With the viscosity coefficient of each node pair taken
  as the larger of a maximum wave-speed bound and the Navier–Stokes
  positivity coefficient of Zhang, the scheme can be read as a subcell
  finite-volume scheme with local Lax–Friedrichs-type fluxes, and it
  satisfies a semi-discrete entropy balance per element, including the
  viscous dissipation (Thm. 6.1, Eqs. (45)–(53)). For Euler the positivity
  coefficient never exceeds the wave speed, so the coefficient reduces to
  the wave-speed estimate (§6.2).
- **Element-wise blending keeps it.** One limiting parameter per element,
  the largest value in $[0,1]$ that keeps every nodal density and internal
  energy above relaxed bounds, blends the low- and high-order updates; the
  limited solution is a convex combination of two conservative,
  entropy-stable semi-discretizations, so on a periodic domain it is
  conservative and satisfies
  $\frac{d}{dt}\int\eta(u)\le-\sum_{d,d'}\Theta_d^\top MK_{dd'}\Theta_{d'}$ with
  page-local entropy-variable gradients $\Theta_d$ and viscosity blocks
  $K_{dd'}$ (Thm. 6.2, Eqs. (54)–(55)). This is the element-wise case of
  Rueda-Ramírez et al. above, with the positivity limiter choosing the
  coefficient ([bound preservation](/properties/bound-preservation.md)).
- **Subcell convex limiting does not.** With positivity as the only
  constraint, convex limiting cannot be shown to keep a cell entropy
  inequality; earlier convex-limiting work enforces stronger local bounds
  or entropic constraints for that purpose (App. B.1;
  [convex limiting](/methods/convex-limiting.md)).
- **Caveats.** The result is semi-discrete: to the authors' knowledge no
  fully discrete entropy inequality can be proved for the high-order
  method with forward Euler or Runge–Kutta, and they point to space–time
  DG or relaxation Runge–Kutta (§6.2). The Davis wave-speed estimate they
  use is not a guaranteed upper bound, which could compromise the provable
  positivity and entropy stability of the low-order scheme; they observed
  no such case (footnote 3).

**Cell entropy inequality by linear programming.**
[Lin & Chan (2024)](/sources/lin-2024.md) enforce in subcell-limited
[DGSEM](/methods/dgsem.md) only the semi-discrete **cell** entropy
inequality, one scalar inequality per element (and per dimension in 2D),
which high-order entropy-stable DG satisfies while keeping its accuracy,
instead of nodal conditions (§1, §3). The DGSEM and the low-order
scheme, a local Lax–Friedrichs-type finite-volume scheme on the LGL
subcells that is semi-discretely entropy stable, share the LLF surface
flux, so their surface subcell fluxes coincide and the surface part of
the entropy balance does not depend on the limiting factors (Eqs. (17),
(22)). In 1D, with nodes $0,\dots,N$, subcell fluxes
$\hat f_{(i,i+1)}=l_i\hat f^{\mathrm H}_{(i,i+1)}+(1-l_i)\hat f^{\mathrm L}_{(i,i+1)}$
between nodes $i$ and $i+1$, and factors $l_i\in[0,1]$ ($1$ = high
order, i.e. $l_i=1-\alpha$ in the registry's blending convention;
page-local $l_i$, $l^{\mathrm C}_i$), the volume part of the cell entropy
inequality reads

$$\sum_{i=0}^{N-1}\big(w_{i+1}-w_i\big)\cdot\hat f_{(i,i+1)}\big(l_i\big)\le\psi(u_N)-\psi(u_0),$$

one linear inequality in the $l_i$ (Eqs. (23)–(24), translated from the
source's sign convention $\mathsf w_i\frac{d}{dt}u_i=\bar f_i-\bar f_{i-1}$,
$\bar f=-\hat f$). It is the sum over the interior subcell interfaces of
the quantity Tadmor's condition bounds interface by interface, which is
why the interface-wise limiting above, of Kuzmin, Hajduk & Rupp, implies
it *(compiler check, not in the sources)*. The factors are the solution
of the linear program

$$\max\sum_il_i\quad\text{subject to the inequality above and}\quad0\le l_i\le l^{\mathrm C}_i,$$

with $l^{\mathrm C}_i$ the factors of any convex-constraint limiter
(positivity, TVD-like bounds) (LP (25)). **Theorem 3.1:** the LP is
solvable, because $l=0$ (the low-order scheme) is feasible, and its
solution is locally conservative, semi-discretely entropy stable and
preserves the convex constraints. **Theorem 3.2:** the LP is a continuous
knapsack problem, solved exactly by a greedy algorithm after Dantzig.
**Theorem 3.3** states the same for 2D, where the inequality is imposed
dimension by dimension with $N(N+1)$ unknowns per dimension, and the
sort-based Algorithm 2 costs $O(m\log m)$, $m=N(N+1)$ (§3.2, §3.4). A
shock-capturing variant multiplies the admissible entropy budget by
$(1-\beta_{\mathrm e}\epsilon_K)$, $\epsilon_K\in[0,1]$ a modal smoothness factor after
Hennemann et al. and Pazner, $\beta_{\mathrm e}\in[0,1]$ user-chosen (Eq. (49), LP
(51); page-local $\beta_{\mathrm e}$, $\epsilon_K$). The authors state that the
SSP Runge–Kutta step and its CFL condition are needed only for
positivity; the entropy inequality is semi-discrete (footnote 7).

Their accuracy comparison on the [isentropic vortex](/benchmarks/isentropic-vortex.md)
($N=1,\dots,4$, $K=5$ to $80$ elements per direction, relative $L^2$
error, Tables 1–3) sets the cell inequality against the nodal
alternatives:

| entropy constraint | last printed rates, $N=1,2,3,4$ |
|---|---|
| cell entropy inequality (LP) | 1.84, 2.74, 4.28, 4.36 |
| local minimum entropy principle on $\rho^{1-\gamma}e$ | 0.86, 0.93, 0.90, 0.95 |
| relaxed minimum entropy principle | 1.52, 1.21, 1.49, 1.31 |

The authors read the first row as a rate "between $O(h^{N+1/2})$ and
$O(h^{N+1})$" and the others as at most $O(h)$ and $O(h^2)$ for any $N$;
high-order accuracy of the cell-entropy limiter is shown numerically,
not proved (§4.2). They report, by private communication, that
Tadmor's condition imposed on every subcell flux also falls to $O(h^2)$
on a smooth sine wave (footnotes 1, 9). On the modified Sod tube and the
2D KPP problem the unlimited DGSEM is non-entropic and the limiter
restores the entropy solution (§4.1, Figs. 2–3; see
[KPP rotating wave](/benchmarks/kpp-rotating-wave.md)).

**Node-based entropy condition of a multi-point finite-volume scheme.**
For the 2D [shallow-water equations](/definitions/shallow-water-equations.md)
on unstructured grids, [Del Grosso et al. (2024)](/sources/delgrosso-2024.md)
take the total energy $h\mathsf e_{\mathrm s}$ as the entropy and build a
cell-centred scheme whose subface fluxes depend on a nodal velocity
obtained from all cells around a vertex (§3.4, §4; HAL preprint). The
entropy condition is imposed at the node, as the sum over the subfaces
impinging at it, not face by face (Eqs. (13), (37)); the residual of the
face-wise sufficient conditions vanishes by the nodal solver (Eq. (41)).
The face-wise conditions (38)–(39) hold when the Lagrangian wave speeds
of the simple Riemann solver satisfy
$\mathsf z_{\mathrm L}\ge\sqrt{gh^\star_{\mathrm L}}\,h_{\mathrm L}$ and
$\mathsf z_{\mathrm R}\ge\sqrt{gh^\star_{\mathrm R}}\,h_{\mathrm R}$
(page-local $\mathsf z$; $h^\star$ the intermediate depths; Eqs.
(42)–(43), algebra not shown), conditions implicit in the intermediate
state and enforced by iteration (Remark 1). Under them and the
positivity time step, a Jensen argument gives a cell entropy inequality
with an explicit subface entropy flux, and the domain total of the
entropy is non-increasing up to the topography source (Eqs. (55)–(58)).
The same conditions are needed by the face-based two-point version of
the scheme (Remark 2); the second-order extension is stated, not proved,
to keep the property (§4.6). See [well-balancing](/properties/well-balancing.md)
and [carbuncle phenomenon](/definitions/carbuncle-phenomenon.md).

**Damping, scaling and reconstruction steps.**

- **Mean-preserving damping term.** Liu et al. (2025b) (Thm. 3.2) add
  $-\sigma(u_h)\,(u_h-\bar u_h)$ to the nodal DG scheme, with $\sigma\ge0$
  a scalar per element (page-local; the source's Eq. (3.16), see
  [OEDG](/methods/oedg.md)). By orthogonality of the cell-mean projection
  its entropy contribution is
  $-\sigma\sum_i\mathsf w_i\big(\eta'(u_i)-\eta'(\bar u)\big)\cdot(u_i-\bar u)\le0$.
  This holds by the monotonicity of $\eta'$ for convex $\eta$, so the
  damped scheme stays semi-discretely entropy stable. In time each SSP
  stage is split into an explicit step and an implicit damping step with
  the closed form $u\mapsto\bar u+(u-\bar u)/(1+\alpha_\sigma)$, with
  page-local $\alpha_\sigma=2\Delta t\,\sigma/\Delta x$ (§3.3, Eq. (3.21)).
  The fully discrete entropy is not proved non-increasing. It does not
  increase on the Orszag–Tang vortex (Fig. 6).
- **Common-factor scaling toward the mean.** Liu et al. (2025c) recall
  from Chen & Shu that $u_j\mapsto\bar u+\theta(u_j-\bar u)$ with one
  $\theta\in[0,1]$ for all nodes and components does not increase the
  quadrature-weighted cell entropy (Lemma 3, a Jensen argument). Their
  limiter takes $\theta=\exp(-\sigma\Delta t)$ with a jump-based $\sigma$
  (§4.1, Eq. (26)).
- **Field reconstruction with energy correction.** After the
  divergence-free reconstruction of $B$, Liu et al. (2025c) correct the
  total energy node by node to keep the pressure, and hence the entropy,
  unchanged (Eq. (27), Remark 2). Local total-energy conservation is lost
  by the change in magnetic energy. The authors call this high-order
  small if the reconstruction is accurate. Without the correction there
  is no guarantee that the total entropy does not increase.

## Dissipation operators

In the sources an ES flux is an EC flux minus a dissipation. In Rueda-Ramírez
et al. (2021), Li, Duan & Tang (2022) and Renac's Roe-type flux the
dissipation acts on the jump of the entropy variables, not of the
conserved variables, which is what gives the production a provable sign.

- **Lax–Friedrichs on $[\![u]\!]$.** Rueda-Ramírez et al. (2021), after
  Derigs et al., state that $f^{\mathrm{ec}}-\tfrac12a[\![u]\!]$ is not
  entropy stable for MHD (§3.3.1, Eq. (52)) *(compiler check, not in the sources: with scalar dissipation $a\ge0$ added to an entropy-conservative flux the production is $-\tfrac12a[\![w]\!]\cdot[\![u]\!]\le0$ for a convex entropy; see [Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md))*.
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
- **How much the reconstructed jump dissipates.**
  [Charles & Ray (2025)](/sources/charles-2025.md) show that the sign
  property is not enough. The third-order SP-WENO reconstruction keeps it,
  but its reconstructed jump is zero or nearly zero at most shock
  interfaces. The entropy-stable scheme then adds almost no dissipation
  and overshoots on Sod-type, Shu–Osher and Lax problems. A learned
  variant that keeps the jump away from zero removes most overshoots, at
  larger smooth errors (§3.2, §5.3; arXiv v2;
  [sign-preserving WENO](/methods/sign-preserving-weno.md)).
- **Robustness of "EC plus dissipation".** Renac (2021) proves that a
  Roe-type flux, the author's EC flux minus a scalar dissipation on the entropy
  variables, is ES (App. D.1, Eq. (D.1)). Renac argues that such fluxes are
  not Lipschitz continuous, which blocks the positivity proofs, and they
  are expensive because of the logarithmic means (§1.2). In Renac's tests the
  Roe-type flux needs CFL 0.2 instead of 0.4 and the 2D runs stop on
  negative states (App. D, Figs. D.9–D.10). Renac's alternative is a
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
  domain, unit norm). Edoh's "entropy-stability-promoting" filter acts on the
  momentum only; on the isentropic vortex it gives strict kinetic-energy
  decay and entropy increase for all the author's kinetic-energy-preserving
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
Liu et al. (2025b) assume positive density and pressure. They state that
a provably positivity-preserving entropy-stable DG scheme for ideal MHD
"remains an open challenge", since positivity is tied to a discrete
divergence-free condition. They add the Zhang–Shu limiter only for the
Mach 800 and Mach 10000 jets, and observe positivity without it on the
blast and rotor (Remark 3.1, Exs. 6, 8, 10). Liu et al. (2025c) run the
MHD blast, plasma beta about $2.51\times10^{-4}$, without a positivity
limiter, and the minimum pressure at the final time is about 0.0952
(Ex. 5.6). Charles & Ray (2025) state that their scheme is not
positivity preserving, since no constraint enforces it (Remark 5).
Lin, Chan & Tomas (2023) state the same premise for entropy-stable DG of
Euler and Navier–Stokes: the semi-discrete entropy inequality holds only
while density and internal energy stay positive, and nothing in the
scheme enforces that (§1, Thm. 4.1). Without their limiter, entropy-stable
DG fails on a strong isentropic vortex (minimum density
$2.145\times10^{-3}$) and on a Mach-20 viscous shock on coarse meshes
(§8.1.2, §8.2.1).

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

[Jain & Moin (2022)](/sources/jain-2022.md) make the same point for
two-phase flows from the other side. As they recall, discrete
kinetic-energy conservation is enough for stability in incompressible
flow but not in compressible flow, where entropy must also be controlled;
for compressible two-phase flows they add that entropy stability alone is
not enough either: the volume fraction must stay bounded and the scheme
must keep uniform velocity and pressure uniform across interfaces
(§1). In their tests Chandrashekar's internal-energy flux and the cubic
split, which conserve kinetic energy and approximately entropy, are
stable in single-phase under-resolved Taylor–Green and isotropic
turbulence, but diverge at density ratio 10, which the authors attribute
to their violation of the interface-equilibrium condition (§4.1–4.2;
[entropy-conservative two-point fluxes](/methods/entropy-conservative-flux.md)).
The entropy in this analysis is the physical specific entropy of each
phase. Its transport equation contains source terms proportional to the
interface-regularization flux, so phase entropy is conserved only at the
equilibrium (hyperbolic-tangent) interface profile; regularization is
irreversible, and its entropy production in a stationary slab test is
small and positive, of order $10^{-7}$ relative (§2.2, Eqs. (19)–(21),
App. A).

**Entropy stability and the carbuncle.** On 2D Riemann configuration 3,
Charles & Ray (2025) find a carbuncle-like protrusion with two
entropy-stable TeCNO schemes under Roe-type dissipation. A Rusanov-type
dissipation weakens it, so entropy stability does not preclude it (§5.3,
Fig. 10; [carbuncle phenomenon](/definitions/carbuncle-phenomenon.md)).

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

- **Peyvan et al. (2023)**, five-species air with vibrational energy,
  1D DGSEM, 170 elements, $N=3$, EC volume and surface fluxes, no
  stabilization. The global entropy rate stays at order $10^{-5}$ to
  $t=0.1$ instead of machine zero; the authors attribute it to the
  $\sim10^{-7}$ Newton tolerance of the temperature inversion, without
  varying the tolerance ([Peyvan et al. (2023)](/sources/peyvan-2023.md),
  §4.4, Fig. 4; [entropy-conservative fluxes](/methods/entropy-conservative-flux.md)).

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
For ideal MHD, [Dzanic & Witherden (2023)](/sources/dzanic-2023.md) bound
instead the specific quantity $p\rho^{-\gamma}$, implemented as
$p\rho^{-\gamma}-(p\rho^{-\gamma})^K_{\min}-10^{-8}>0$, and cite Dao & Nazarov for a minimum entropy principle of MHD
entropy solutions in the vanishing-viscosity sense, identical to the
gas-dynamics one (§2.1 Eq. (5), §3.1 Eq. (22), §4).

[Trojak & Dzanic (2024)](/sources/trojak-2024.md) carry the local
minimum principle to multi-species flows, on the mixture entropy of
Gouasmi et al. (a partial-density-weighted sum of species entropies),
again in the physical sign convention, and impose it through the filter
only where a pressure-jump sensor detects a shock: imposed everywhere it
over-dissipates species interfaces, where a smooth mixture density can hide
discontinuous partial densities (§2.2, §3.1–3.2, Eqs. (7)–(12), (25)–(27);
arXiv v1). They impose it on an exponentiated, clipped functional and state
that the exponential's strict convexity keeps the principle (§4, Eq. (33));
a lower bound carries over to any increasing function of the entropy, so
monotonicity is what is used *(compiler check, not in the sources; details
on [entropy filtering](/methods/entropy-filtering.md))*.

Wu & Shu represent it, by
[geometric quasilinearization](/methods/geometric-quasilinearization.md), as
a family of constraints linear in $u$ (Thm 4.7; Eq. (2.3)). For 1D Euler the
family is

$$u\cdot n_*+s_{\min}'\rho_*^{\gamma}\ge0,\qquad n_*=\Big(\tfrac12v_*^2-\frac{\gamma s_{\min}'\rho_*^{\gamma-1}}{\gamma-1},\,-v_*,\,1\Big)^\top,$$

for all free auxiliary $\rho_*>0$ and $v_*\in\mathbb R$. They give the relativistic analogue in Thm 4.10. The local minimum principle on
$e\rho^{1-\gamma}$ in the subcell limiting of Rueda-Ramírez et al. (2022) is
a discrete, local relative of the same principle.

[Ching et al. (2025)](/sources/ching-2025.md) enforce the local minimum
entropy principle in positivity-preserving DG for the reacting
multicomponent Navier–Stokes equations, with the physical specific entropy
$s$ of the thermally perfect mixture bounded from below by its minimum over
the quadrature points of the element and its face neighbours at the
previous step, with "a small tolerance" (Eqs. (4.20), (4.38)). The bound
is imposed only on the convective half of a split update, because the
principle does not hold for Navier–Stokes with nonzero thermal
diffusivity, as they recall for monocomponent, calorically perfect gases,
and they "do not expect the conclusion to change" for multicomponent
thermally perfect ones (§1). The forward-Euler cell-average update is
written as half a convective-only update plus half a viscous-only update,
each with step $2\Delta t$ (Eq. (4.12)); the convective half is kept in the
entropy-bounded set by an invariant-region-preserving flux and an entropy
scaling limiter, the viscous half only in the positivity set (§4.2–4.3;
[positivity-preserving Navier–Stokes flux](/methods/positivity-preserving-navier-stokes-flux.md),
[Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md)). The
entropy constraint function $\rho s-\rho s_{\mathrm b}$ (page-local bound
$s_{\mathrm b}$) is concave only when all concentrations are positive; the
authors assume the constrained set convex throughout, an assumption that
"does not seem to have any discernible negative effects" (§4). They contrast their half-sum with the
sequential split of
[Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md), in which the viscous update starts
from the entropy-limited convective state: that state "may not be" in the
positivity set unless the viscous dissipation coefficient adds a further
time-step constraint (§4.3). Evidence: in a 1D viscous N$_2$/He shock tube
the entropy limiter damps large-scale pressure, temperature and entropy
oscillations "significantly better" than positivity alone (§5.3, Figs.
5.5–5.6); in a 2D H$_2$–O$_2$–Ar detonation without it the minimum
temperature approaches zero before 50 μs and the chemistry solver stalls,
while with it the minimum entropy stays roughly constant (§5.4, Fig. 5.12;
[shock-induced combustion](/benchmarks/shock-induced-combustion.md)).

Lin, Chan & Tomas (2023) do not impose a minimum entropy principle: they
state that it is consistent with the compressible Euler equations but not
with Navier–Stokes, and limit only density and internal energy (§1).
Dzanic & Witherden (2022), whom they cite among the works that impose a
local minimum entropy principle, impose the entropy bound for
Navier–Stokes only on the inviscid update of each stage and filter the
result of the viscous increment for positivity only
([entropy filtering](/methods/entropy-filtering.md)). Without a monotonicity
or entropy bound, Lin, Chan & Tomas's limited solutions oscillate near
shocks; a larger relaxation factor of the bounds or an added shock-capturing
blend reduces the oscillations (§8.2–8.4).

## Qualifications

- Lin & Chan's Table 1 prints for $N=2$ the rates 1.11 ($K=20$) and 2.74
  ($K=80$); its own errors give $\log_2(1.785\times10^{-1}/4.126\times10^{-2})=2.11$
  and $\log_2(6.714\times10^{-3}/1.210\times10^{-3})=2.47$ *(compiler
  check, not in the sources)*. With $2.47$ the $N=2$ rate lies below
  $N+\tfrac12$, as does the $N=4$ rate $4.36$, while the $N=3$ rate $4.28$
  lies above $N+1$ *(compiler check, not in the sources)*. Their
  wave-speed estimate (Davis) is not a guaranteed upper bound, on which
  the solvability of the LP rests through the entropy stability of the
  low-order scheme (footnote 8).

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
  - Rueda-Ramírez et al. (2024) use $\eta=-\rho s/(\gamma-1)$ with
    production $\le0$, as the registry (App. A). Goudon & Minjeaud (2024)
    write the barotropic entropy (total energy) with production $\le0$, and
    their $\eta$ also names the constant water level of the lake at rest.
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
  of $\rho s$ is non-decreasing for entropy solutions. Their MHD paper,
  Dzanic & Witherden (2023), bounds the specific $p\rho^{-\gamma}=e^s$ and
  describes the method as that of the 2022 paper without commenting on the
  change (§3.1, §4). The 2022 entropy tolerance $10^{-4}$ lets $\rho s$ fall
  below its local minimum, whereas the 2023 constant $10^{-8}$, the same
  number as the 2022 positivity floors $\rho_{\min}=p_{\min}$, is printed
  as an offset that $p\rho^{-\gamma}$ must exceed; both are absolute and
  depend on the scale of the data *(compiler check, not in the sources;
  details on [entropy filtering](/methods/entropy-filtering.md))*.
- **What entropy conservation buys.** Peyvan et al. (2023) attribute to
  Gassner et al. the conclusion that the high-order accuracy of
  flux-differencing DGSEM comes from the symmetry and consistency of the
  two-point flux, not from entropy conservation (§2.3.1). Lin, Chan &
  Tomas (2023) and Peyvan et al. use the registry convention
  $\eta=-\rho s/(\gamma-1)$ and a physical-like $\rho s$ respectively;
  Peyvan et al.'s entropy variables are printed as $\partial(\rho s)/\partial u$
  but their last component, $-1/T$, is that of $-\rho s$, a sign
  inconsistency of the text only (Eqs. (63)–(66)).
- **Energy-equation splittings do not conserve entropy.**
  [De Michele & Coppola (2023a)](/sources/demichele-2023.md) show for
  central split forms that none of their total-energy, internal-energy,
  pressure, total-enthalpy or sound-speed discretizations conserves
  entropy exactly: the induced entropy terms are not flux differences in
  general (Eqs. (73)–(74)); a direct entropy discretization conserves
  $\rho s$ but loses total energy (§4.2.5, Table 2;
  [split convective forms](/methods/split-convective-forms.md)).
- **Printed slip (Rueda-Ramírez et al. (2024), arXiv v1).** Eq. (39)
  prints the numerator of $\alpha^s$ as $[\![w]\!]\cdot\hat f^{\mathrm{FV}}-[\![\psi]\!]+\epsilon$,
  the opposite sign of the bound obtained by substituting their Eq. (38)
  into Eq. (37) (see above); as printed it would give $\alpha^s\le0$ up to
  $\epsilon$ in the limited branch *(compiler check, not in the sources)*.
- **Printed slip.** Renac's cell entropy inequality (64) prints the
  surface sum without the quadrature weight, while the analogous sum in
  the proof of Renac's Theorem 6.1 carries it. The weight is missing in (64).

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
- [Jain & Moin (2022)](/sources/jain-2022.md) — §1, §2.2 Eqs. (19)–(21), §4.1–4.2, App. A Fig. 12 (arXiv v1).
- [Bhoriya, Kumar & Chandrashekar (2023)](/sources/bhoriya-2023.md) — §1, Prop. 3.1, App. A, Thms. 4.2–4.3, Remark 4.3, §6.1.2 Fig. 1 (arXiv v2).
- [Dzanic & Witherden (2023)](/sources/dzanic-2023.md) — §2.1 Eq. (5), §3.1 Eq. (22), §4 (arXiv v2).
- [De Michele & Coppola (2023a)](/sources/demichele-2023.md) — §4.2.5 Eqs. (72)–(77), Table 2 (arXiv v1).
- [Lin & Chan (2024)](/sources/lin-2024.md) — §1, §2.3, §3 Eqs. (17)–(28), (49)–(51), Thms. 3.1–3.3, Algorithms 1–3, §4.1–4.2 Tables 1–3, footnotes 1, 7–9.
- [Del Grosso et al. (2024)](/sources/delgrosso-2024.md) — §2, §3.4–3.5.3 Eqs. (13), (37)–(43), Remarks 1–2, §4.4 Eqs. (55)–(58), §4.6 (HAL preprint).
- [Lin, Chan & Tomas (2023)](/sources/lin-2023.md) — §1, Thm. 4.1, §5, §6.1–6.2 Thms. 6.1–6.2 Eqs. (45)–(55), §8.1–8.4, footnote 3, App. B.1 (arXiv v2).
- [Peyvan et al. (2023)](/sources/peyvan-2023.md) — §2.3.1, §3 Eqs. (63)–(66), §4.4 Fig. 4 (arXiv v1).
- [Rueda-Ramírez, Bolm, Kuzmin & Gassner (2024)](/sources/ruedaramirez-2024.md) — §2.2 Eqs. (37)–(39), Remark 9, §3.2 Eq. (51), App. A (arXiv v1).
- [Goudon & Minjeaud (2024)](/sources/goudon-2024.md) — pp. 1272–1275 Eqs. (26)–(35) (HAL wrap of the version of record).
- [Trojak & Dzanic (2024)](/sources/trojak-2024.md) — §2.2 Eqs. (7)–(12), §3.1–3.2 Eqs. (25)–(27), §4 Eq. (33) (arXiv v1).
- [Cicchino & Nadarajah (2025)](/sources/cicchino-2025.md) — §6.3 Thm. 6.3, Eqs. (54)–(58), §7.3.
- [Schwarz et al. (2025)](/sources/schwarz-2025.md) — §2.2 Eq. (4), §3.3–3.4, §4 (arXiv v1).
- [Alberti et al. (2025)](/sources/alberti-2025.md) — §2 Eq. (16), §2.1.1 Eqs. (20)–(25), §2.1.2 Eqs. (40)–(47), §3.2.2.
- [Ching et al. (2025)](/sources/ching-2025.md) — §1, §4 Eqs. (4.1), (4.12), (4.20), (4.38), §4.3, §5.3 Figs. 5.5–5.6, §5.4 Fig. 5.12.
- [Charles & Ray (2025)](/sources/charles-2025.md) — §3.2, §5.3 Figs. 6–10, Remark 5 (arXiv v2).
- [Liu et al. (2025b)](/sources/liu-2025-b.md) — §2, §3.1 Thm. 3.1, §3.2 Thm. 3.2 Eqs. (3.15)–(3.18), Remarks 3.1–3.2, §3.3 Eq. (3.21), Exs. 5–10, Fig. 6.
- [Liu et al. (2025c)](/sources/liu-2025-c.md) — §1, §3.1 Defs. 2–4 Thm. 1, App. B, §4.1 Lemma 3 Eq. (26), §4.2 Eq. (27) Remark 2, Ex. 5.6.
