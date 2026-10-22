---
type: Definition
title: "Multicomponent Euler equations"
description: "The fully conservative Euler system for a mixture of several gases or stiffened fluids in thermal and mechanical equilibrium, written with partial densities or mass fractions, and its reacting Navier–Stokes extension; its closures, admissible set, wave structure and mixture entropy, and the entropy-stable, positive and bound-preserving schemes built on it, with their behaviour at material interfaces."
status: established
aliases: [multi-component Euler equations, multispecies Euler equations, compressible multicomponent Euler system, HRM model (as named by Renac)]
tags: [multiphase, entropy-stable, positivity, bound-preserving, dg, finite-difference]
timestamp: 2026-10-23T16:00:00Z
---

# Multicomponent Euler equations

The multicomponent Euler equations describe a mixture of $n_{\mathrm c}$
components (page-local symbol) that share one velocity, one pressure and
one temperature. Each component $k$ conserves its own mass; the
mixture conserves momentum and total energy:

$$
\partial_t(\rho Y_k)+\nabla\cdot(\rho Y_kv)=0,\qquad
\partial_t(\rho v)+\nabla\cdot(\rho v\otimes v+pI)=0,\qquad
\partial_tE+\nabla\cdot\big((E+p)v\big)=0,
$$

with mass fractions $Y_k$, $\sum_kY_k=1$, mixture density
$\rho=\sum_k\rho Y_k$ and $E=\rho e+\tfrac12\rho\lvert v\rvert^2$.
[Renac (2021)](/sources/renac-2021.md) §2 writes the unknowns as
$(\rho Y_1,\dots,\rho Y_{n_{\mathrm c}-1},\rho,\rho v,E)$ (Eqs. 1–2);
[Li, Duan & Tang (2022)](/sources/li-2022-c.md) §1 writes them with
the partial densities $\rho Y_k$ of all components (Eq. 1.1), as do
[Nguyen et al. (2022)](/sources/nguyen-2022.md) §2.1 (with
$\rho Y_k=\phi_k\rho_k$, Eqs. 2a–2e) and
[Peng, Atkins & Deiterding (2022)](/sources/peng-2022.md) §2.1 (Eq. 1);
[Du & Yang (2022)](/sources/du-2022-b.md) §2 carry $\rho$ and all
$n_{\mathrm c}$ partial densities, one more unknown than needed
(Eq. 2.1), and so do
[Bielawski et al. (2023)](/sources/bielawski-2023.md) for their reacting
Navier–Stokes system (§2, Eqs. 1–6, accepted manuscript);
[Zhou et al. (2023)](/sources/zhou-2023.md) write the two-species
system with $\rho$ and the single partial density $\rho Y_1$
(Eqs. 1–2). Unlike the
[five-equation model](/definitions/five-equation-model.md), the system
is a system of conservation laws with no volume-fraction equation: the
volume fractions follow from the closure.

Page-local symbols: $T$ temperature, $C_{v,k}$ and $C_{p,k}$ specific
heats, $R_k=C_{p,k}-C_{v,k}=(\gamma_k-1)C_{v,k}$ the gas constant of
component $k$, $\phi_k$ volume fractions, $p_{\infty,k}$ stiffened-gas
constants.

## Closure

**Polytropic ideal gases.** Renac takes polytropic ideal gases,
$p_k=(\gamma_k-1)\rho_ke_k$, $e_k=C_{v,k}T_k$, in thermal and mechanical
equilibrium ($T_k=T$, $p_k=p$). The mixture is then an ideal gas with
composition-dependent constants (Eqs. 3–7):

$$
C_v(Y)=\sum_kY_kC_{v,k},\quad C_p(Y)=\sum_kY_kC_{p,k},\quad
\gamma(Y)=\frac{C_p(Y)}{C_v(Y)},\quad
p=\big(\gamma(Y)-1\big)\rho e=\rho R(Y)T,
$$

with $R(Y)=C_p(Y)-C_v(Y)$. Mechanical equilibrium gives $\rho R(Y)=\rho_kR_k$
for every $k$, so the volume fractions are explicit,
$\phi_k=R_kY_k/R(Y)$ (Eq. 8).

**Stiffened components.** Li et al. close each component with the
temperature form of the [stiffened-gas law](/definitions/stiffened-gas-equation-of-state.md),
$\rho_ke_k=C_{v,k}\rho_kT+p_{\infty,k}$, again in thermal equilibrium,
which gives $p=\sum_k\big(\rho Y_kR_kT-p_{\infty,k}\big)$ and a mixture
$\gamma=\sum_k\gamma_kC_{v,k}\rho Y_k/\sum_kC_{v,k}\rho Y_k$ (Eq. 1.2).
With $p_{\infty,k}=0$ it reduces to Renac's closure.

**Mixture ratio of specific heats with molar masses.** Zhou et al. give
the two-species mixture of ideal gases by
$$\gamma=\frac{\sum_kY_k\gamma_k/\big(W_k(\gamma_k-1)\big)}{\sum_kY_k/\big(W_k(\gamma_k-1)\big)}$$
with molar masses $W_k$ (page-local; the source's $M_i$) (§2). This is
Renac's $\gamma(Y)=C_p(Y)/C_v(Y)$, since $C_{v,k}=R_u/\big(W_k(\gamma_k-1)\big)$
and $C_{p,k}=\gamma_kC_{v,k}$ with $R_u$ the universal gas constant
*(compiler check, not in the sources)*. They name water at
very high pressure (underwater explosions, shock lithotripsy) as the
application.

**Stiffened phases in pressure–temperature form.** Nguyen et al.
present the same system with stiffened-gas phases, written as functions
of $(p,T)$ (see [stiffened-gas equation of state](/definitions/stiffened-gas-equation-of-state.md)),
as a "fully compressible multiphase model" for interfacial flows with
density ratios near 1000: $\rho_k=\rho_k(p,T)$, $h_k=h_k(p,T)$, mixture
$\rho=\sum_k\phi_k\rho_k$, and the volume fractions follow from the
partial densities, so no volume-fraction advection equation is solved
(§2.1, Eqs. 2–7). They advance the primitive vector
$(p,v,T,\phi_2,\dots,\phi_{n_{\mathrm c}})$ through
$\frac{\partial u}{\partial \mathsf W}\partial_t\mathsf W+\nabla\cdot f(u)=0$ (page-local
$\mathsf W$, the source's $W$; Eq. 7), with the inverse Jacobian printed for two phases and
computed numerically otherwise (Appendix). The paper gives no
reference for the system itself; it is the conservative
pressure–temperature-equilibrium closure above, and the model is
presented as new. [Bai & Li (2022)](/sources/bai-2022.md) take the
sharp-interface alternative for the same gas–gas and gas–water
problems: two Euler systems, one stiffened-gas law per fluid and no
mixture closure, coupled through ghost-fluid states at a level-set
interface ([level-set methods](/methods/level-set-method.md)).

**Thermally perfect, reacting mixtures.** Peng et al. and Du & Yang
take ideal-gas species with temperature-dependent heat capacities
(CHEMKIN-II or NASA polynomials) and formation enthalpies,
$p=\rho R_uT\sum_kY_k/W_k$ with $R_u$ the universal gas constant and
$W_k$ the molar masses, and add finite-rate chemistry as a source
$\dot\omega_k$ in the species equations (Peng et al. Eqs. 4–8; Du &
Yang Eqs. 2.3–2.4; page-local symbols). Du & Yang solve the
Navier–Stokes version, with mixture-averaged diffusion velocities
corrected so that $\sum_kY_kV_k=0$, Wilke viscosity and Mathur
conductivity (§2.2). Peng et al. solve the reactive Euler equations,
planar or axisymmetric, with Strang splitting and a semi-implicit
fourth-order generalized Runge–Kutta integrator (GRK4A) for the chemistry (§2.1).
Bielawski et al. solve the reacting Navier–Stokes equations with NASA
polynomials for the heat capacity, enthalpy and $\gamma$, held constant
below the polynomials' lower bound (typically 300 K), species
viscosities and conductivities fitted with Cantera, a single mixture
diffusivity for all species, a total energy that includes the
formation enthalpies, and finite-rate chemistry split from the flow
by Strang splitting, the stiff reactor problem being integrated cell by
cell on the GPU (§2, Eqs. 4–7; §5; see
[operator splitting](/methods/operator-splitting.md)). The temperature
is recovered from the internal energy by a Newton iteration (§2,
Alg. 2).

## Admissible set and waves

Renac's admissible set is
$\{0\le Y_k\le1,\ \rho>0,\ e>0\}$ (Eq. 9). In direction $n$ the
eigenvalues are $v\cdot n\mp c$ (genuinely nonlinear) and $v\cdot n$
with multiplicity $n_{\mathrm c}+d-1$ (linearly degenerate), with
$c^2=\gamma(Y)\big(\gamma(Y)-1\big)e$ and $\gamma(Y)\le\max_k\gamma_k$
(Eqs. 10–11). Renac notes that, to the author's knowledge, fast upper bounds of
the maximum wave speed (two-rarefaction or Guermond–Popov type), which
simple-wave solvers such as HLL, Rusanov or relaxation need, do not
exist for this model (§1.3). Li et al. give the entropy-scaled right-eigenvector
matrices (whose product with their transpose is $\partial u/\partial w$)
explicitly for one and two stiffened components, following Gouasmi et al.'s ideal-gas
construction for two (§3.4; see
[characteristic decomposition](/methods/characteristic-decomposition.md)).
Nguyen et al. list the eigenvalues of their primitive system as
$v\pm c$ and $v$ with Wood's mixture sound speed
$\frac1{\rho c^2}=\sum_k\frac{\phi_k}{\rho_kc_k^2}$ (Eqs. 16–17), and
assert hyperbolicity "because each phase is considered compressible",
without proof.

For the reacting system Du & Yang define, for calorically perfect
species, $G=\{\rho\ge0,\ P(u)\ge0,\ \rho Y_k\ge0\}$ with
$P(u)=E-\sum_k\rho Y_kh_k(0)-\tfrac12\rho\lvert v\rvert^2$ (page-local,
$h_k(0)$ the formation enthalpy at 0 K), so that $p\ge0$ iff $P\ge0$;
$P$ is concave and $G$ convex (§4.1, Eq. 4.1). The upper bound
$Y_k\le1$ is not in $G$: it follows from $\rho Y_k\ge0$ once
$\sum_kY_k=1$ holds exactly, which the next section obtains from the
scheme.

## Mixture entropy

Both sources use the mass-weighted mixture entropy. Renac sets
$\eta=-\rho s$, $s=\sum_kY_ks_k$, $s_k=C_{v,k}\ln\big(e_k/\rho_k^{\gamma_k-1}\big)+\mathrm{const}$,
and obtains the entropy flux $F_\eta=-\rho sv$ and the flux potential
$\psi=R(Y)\rho v$ (Eqs. 13–18). Li et al. set
$\eta=-\sum_k\rho Y_kS_k$ with $S_k=C_{v,k}\ln T-R_k\ln(\rho Y_k)$, flux
potential $\big(\sum_k(R_k\rho Y_k-p_{\infty,k}/T)\big)v$ (Eqs. 3.16–3.17).
The entropy variables $w$ have one component per partial density (or
mass fraction), plus $v/T$ and $-1/T$ (Renac Eq. 17; Li et al. §3.3).

## Entropy-conservative and entropy-stable schemes

**Two-point entropy-conservative fluxes.** Renac proves that a new
symmetric flux is [entropy conservative](/methods/entropy-conservative-flux.md)
for the mixture (Lemma 3.1, Eq. 24). It needs only three
[logarithmic means](/operators/logarithmic-mean.md), of the density of
the last component, of $\rho$ and of $1/T$, against $n_{\mathrm c}+1$
for the flux of Gouasmi, Duraisamy & Murman type that Renac re-derives in
Appendix B (Eq. B.1). It is therefore cheaper for $n_{\mathrm c}>2$ and
less exposed to floating-point exceptions, since every logarithmic mean
needs positive arguments (Remark 3.1); it is also formally
kinetic-energy preserving in Jameson's sense, a property that can fail
discretely (Remark 3.2). Li et al. derive explicit two-point fluxes for
one and two stiffened components from jumps of the parameter vector
$(\rho Y_k,v,1/T)$ and logarithmic means of the partial densities and
of $1/T$, with an extra "entropy-conservative state" for the
mesh-velocity term on moving meshes (§3.3, Eqs. 3.11–3.18).

**Entropy-stable, positive schemes.**

- Renac composes the Coquel–Perthame energy relaxation (a polytropic
  pressure law with a constant $\gamma>\max_k\gamma_k$ plus an advected
  extra internal energy) with Bouchut's pressure relaxation solver. The
  energy-relaxation entropy is convex but not strictly convex
  (Lemma 4.1), so the general framework of Marmignon, Naddei & Renac
  does not apply directly; the pressure relaxation solver supplies the
  entropy inequality instead (§4, Appendix C). The resulting
  three-wave, HLLC-like flux is entropy stable and positive under
  $\frac{\Delta t}{\Delta x}\max\lvert\lambda\rvert<\frac12$ with
  $\lvert\lambda\rvert=\lvert v\cdot n\rvert+a/\rho$, $a$ Bouchut's
  approximate Lagrangian sound speed (§4.3–4.4, Eqs. 52–56; see
  [HLL-family solvers](/methods/hll-riemann-solvers.md)).
- Used as the surface flux of an entropy-stable [DGSEM](/methods/dgsem.md)
  with [flux differencing](/methods/flux-differencing.md) and the new
  flux in the volume terms, it gives a semi-discrete cell entropy
  inequality (§5, Eqs. 62–64). Theorem 6.1 proves that the forward-Euler
  update keeps the cell averages admissible on unstructured
  straight-sided quadrilaterals under a CFL condition whose right-hand
  side is $1/(2N(N+1))$, through a quadrilateral extension of
  Perthame & Shu's lemma (Lemma 3.2, Appendix A; see
  [optimal cell-average decomposition](/methods/optimal-cell-average-decomposition.md));
  a [Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md)
  adapted to partial densities then restores nodal positivity (§6.3,
  Eq. 67). In the runs a simpler time-step bound of 0.4 kept positivity
  throughout (§7).
- A Roe-type alternative, the entropy-conservative flux plus scalar
  dissipation, is entropy stable (Appendix D.1) but not Lipschitz,
  blocks the positivity proof, needs CFL 0.2 instead of 0.4, and the 2D
  computations with it stop on negative states (Appendix D).
- Li et al. add to their high-order entropy-conservative flux a
  dissipation built on jumps of [multi-resolution WENO](/methods/multi-resolution-weno.md)
  reconstructions of the scaled entropy variables with a sign switch,
  a [TeCNO-type](/methods/tecno-scheme.md) construction, on an
  [adaptive moving mesh](/methods/adaptive-moving-mesh.md) (§3.4,
  Eq. 3.21). They show total-entropy conservation and decay numerically
  ([isentropic vortex](/benchmarks/isentropic-vortex.md)) and state
  that the entropy inequality follows as in the single-component case;
  no proof is printed.

## Bound preservation for reacting mixtures

Du & Yang (2022) build a high-order bound-preserving local DG scheme for
the reacting Navier–Stokes system (see
[discontinuous Galerkin](/methods/discontinuous-galerkin.md) and
[bound preservation](/properties/bound-preservation.md)):

- **Exact species sum.** With the constant vector
  $\mathsf v=(1,0,0,0,-1,\dots,-1)$ (page-local), the model satisfies
  $\frac{d}{dt}(u\cdot\mathsf v)=0$, i.e. $\rho-\sum_k\rho Y_k$ is
  conserved (Def. 2.1, Eq. 2.8). A numerical flux with
  $\hat f\cdot\mathsf v=0$, called consistent, makes the semi-discrete
  and the fully discrete schemes preserve $\sum_kY_k=1$ exactly
  (Thms. 3.1–3.2; 2D Thms. 5.2–5.3), so positivity of every partial
  density gives $Y_k\le1$ without a limiter on the upper bound.
- **Positivity of the viscous flux.** Following Zhang's
  positivity-preserving DG for Navier–Stokes, the convective and viscous
  fluxes are treated as one flux with a
  [Lax–Friedrichs](/methods/lax-friedrichs-flux.md)-type penalty
  $\beta$ large enough that $u\pm\beta^{-1}f\in G$ (Lemma 4.1, Eq. 3.5),
  now including the species diffusion velocities.
- **Stiff chemistry.** A third-order conservative modified exponential
  Runge–Kutta method of the authors replaces
  [SSP Runge–Kutta](/methods/ssp-runge-kutta.md); each stage is a convex
  combination of a convective update, admissible under a CFL bound with
  the Gauss–Lobatto weight $1/(L(L-1))$ (Theorem 4.1; see
  [optimal cell-average decomposition](/methods/optimal-cell-average-decomposition.md)),
  and a source update, admissible for a large enough damping
  coefficient (Theorems 4.2–4.3). A three-step
  [Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md)
  (density, partial densities with one common factor, then $P$) restores
  nodal admissibility (§4.3).

On a stiff accuracy test with source coefficient $10^6$, the exponential
integrator converges at third order ($L^2$ error $1.84\times10^{-3}$ on
10 cells to $1.28\times10^{-8}$ on 640) while SSP-RK3 at the same step
returns NaN on the two coarsest meshes (Table 6.2); without the limiter
the He/N$_2$ shock tube produces a negative mass fraction at
$0.5085\,\mu$s and the code stops (Fig. 6.2). The run uses a time step
$\Delta t=\min(a\Delta x/\beta^*,b\Delta x^2/\eta^*)$ with a simpler
speed $\beta^*$ than the proven bound and restarts a step with doubled
damping and halved $\Delta t$ when a cell average leaves $G$ (§6,
Eq. 6.1): admissibility in the runs rests on this restart, which
Theorem 4.3 guarantees to terminate.

**Species sum under limited interpolation.** Bielawski et al. state,
citing earlier work, that interpolating conserved variables to the faces
with a limiter can make the face mass fractions sum to a value other
than one, because the limiter acts differently on the mass-weighted
scalars and on the face density; each scalar then moves with its own
effective contact speed, and the error "can grow and become
significant over a simulation" (§3, not demonstrated in the paper).
They note that species are limited in mixing and burning regions as
well as at shocks. Du & Yang's consistency condition $\hat f\cdot\mathsf v=0$
(next section) is the property such a scheme loses.

## Material interfaces

Because the system is conservative, its schemes meet the
pressure-equilibrium problem of moving interfaces directly. Renac
proves that the proposed DGSEM resolves stationary material interfaces (different
composition and density, $v=0$, equal $p$) exactly at the nodes: both
fluxes reduce to $(0,0,pn,0)$ there, and an interface on a mesh
interface is resolved exactly (Theorem 6.1; RP4, Fig. 4; see
[stationary contact preservation](/properties/stationary-contact-preservation.md)).
A moving interface (RP5, same states advected at unit speed) produces
spurious pressure and velocity oscillations "inherent to discretely
conservative schemes". Renac accepts them: quasi-conservative
formulations remove them at the price of losing the conservation of
species mass, and non-conservative methods that are not genuinely
multidimensional also oscillate on interfaces not aligned with the mesh
(§1.2, §7.2). This is the trade-off the
[five-equation model](/definitions/five-equation-model.md) resolves the
other way, and sharp-interface [level-set methods](/methods/level-set-method.md)
avoid by keeping two fluids apart.

Zhou et al. (2023) §4.3 attribute the spurious pressure oscillations of
shock-capturing schemes at material interfaces to the jump of fluid
properties, list as remedies the primitive algorithm, the
quasi-conservative method, total-energy correction and the double-flux
algorithm, and take the last, after Abgrall & Karni, into their
[weighted compact nonlinear scheme](/methods/weighted-compact-nonlinear-scheme.md):
while updating node $i$ from $t^n$ to $t^{n+1}$ the node sees a single
fluid with $\gamma=\gamma_i^n$, so each interface flux is computed twice
from the same reconstructed states, $h(u^-_{i+1/2},u^+_{i+1/2};\gamma_i^n)$
for node $i$ and $h(u^-_{i+1/2},u^+_{i+1/2};\gamma_{i+1}^n)$ for node
$i+1$, and $\gamma$ is updated, and the total energy recomputed, only at
the last Runge–Kutta stage (Eq. 33). On the two-species Sod tube the
expansion, shock and material interface are "accurately captured" and
their scheme gives the thinnest interface of the three schemes compared
(§5.4, Figs. 13–14). The two fluxes of one interface differ wherever
$\gamma_i^n\ne\gamma_{i+1}^n$, so the double-flux update is not
discretely conservative there *(compiler check, not in the sources)*;
the paper does not discuss it.

Nguyen et al. report the opposite outcome for a moving interface: a
water–air interface advected at 150 m/s at uniform $p$, $v$ and $T$
keeps velocity, pressure and temperature errors "on the order of
$10^{-14}$", about three cells thick with superbee or the compressive
overbee limiter on the volume fractions, also with initial temperature
jumps of 100 and 500 K (§3.1, Figs. 1–5). Their reconstruction is MUSCL
($\kappa=1/3$) on $(p,v,T,\phi_k)$ with Van Leer on the other variables
and overbee on the volume fractions (Eqs. 26–28; see
[TVD limiters](/definitions/total-variation-diminishing.md)), the flux
Rusanov or an HLLC solver carrying the partial densities with the star
factor (Eqs. 19–25; see [HLL-family solvers](/methods/hll-riemann-solvers.md)),
and the time update acts on the primitive vector; see Qualifications
for what this costs in conservation.

## Tests in the sources

Nguyen et al.: interface advection, a two-fluid Sod tube and a
water–air tube at $10^9$ Pa ([gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md)),
an [underwater explosion](/benchmarks/underwater-explosion.md), the
Mach 1.22 [shock–helium bubble](/benchmarks/shock-bubble-interaction.md)
and the Martin–Moyce dam break. Du & Yang: a He/N$_2$ shock tube,
$(T,v,p,Y_1,Y_2)=(300\ \mathrm K,0,10\ \mathrm{atm},1,0)$ for
$x\le0.4$ m and $(300\ \mathrm K,0,1\ \mathrm{atm},0,1)$ otherwise,
$t=300\,\mu$s (agreeing with Houim & Kuo), and a non-reacting
H$_2$/O$_2$/Ar shock tube (molar ratio 2:1:7),
$(T,p)=(400\ \mathrm K,8000\ \mathrm{Pa})$ against
$(1200\ \mathrm K,80000\ \mathrm{Pa})$, $t=40\,\mu$s, which Peng
et al. §3.2 also run on adaptive meshes; Peng et al. also run a
multispecies shock box (O$_2$:N$_2$ = 1:3.76, Owen et al.). Both
groups then run reacting H$_2$/O$_2$/Ar detonations
([shock-induced combustion and detonation](/benchmarks/shock-induced-combustion.md)).

Renac (polynomial degree $N=3$, SSPRK(4,3)): convection of void-fraction
and density waves at design order $N+1$ ($L^1$ errors at $N=3$:
$0.92849\times10^{-4}$, $0.30461\times10^{-5}$, $0.30281\times10^{-6}$
on $1/16$, $1/32$, $1/64$; Table 1); an entropy-conservation check in
which the global entropy error of the EC flux falls at third order with
$\Delta t$, the order of the time integrator (Table 3); six
two-component Riemann problems including a Sod-type one, a He–N$_2$
shock tube, a near-vacuum double rarefaction and the stationary and
moving interfaces; the [shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)
with helium (Mach 1.22) and hydrogen (Mach 2); and a Richtmyer–Meshkov
instability with re-shock (Mach 1.21, Atwood number 0.6053). Li et al.:
the isentropic vortex in 2D and 3D, a quasi-2D stiffened shock tube, two
2D Riemann problems, a 3D spherical shock tube, a two-material tri-point
problem and the shock–bubble interactions with ideal and stiffened
gases.

Zhou et al.: the two-species Sod tube, $(\rho,v,p,\gamma)=(1,0,1,1.4)$
against $(0.125,0,0.1,1.6)$ on 200 cells to $t=0.2$ at CFL 0.2
([Sod tube](/benchmarks/sod-and-lax-shock-tubes.md)), and the Mach 1.22
[shock–helium bubble](/benchmarks/shock-bubble-interaction.md) on
$D/150$ (§5.4, §5.8). Bielawski et al.: one-dimensional H$_2$/air,
CH$_4$/O$_2$ and RP2/O$_2$ detonations, a CH$_4$–O$_2$ rotating
detonation rocket engine (312 million cells on 1176 GPUs in Table 2; the
text of §6.1 says 118 million cells) and an
ethylene-fuelled scramjet (41 million cells, 300 GPUs)
([shock-induced combustion and detonation](/benchmarks/shock-induced-combustion.md);
§5–6).

## Qualifications

- Renac's design-order table is irregular on coarse meshes (at $N=1$ the
  error grows from $1/4$ to $1/8$; at $N=3$ the rate falls to 3.33 at
  $1/64$ after 4.96), while the text states that the expected order is
  recovered.
- Renac calls the model "the HRM model (1)" without expanding the
  acronym.
- The positivity theorem covers the forward-Euler update and cell
  averages; the time-step bound 0.4 used in practice is not covered by
  it.
- Li et al.'s entropy-stability statement and their curvilinear
  entropy-conservation condition are quoted from an earlier paper by the
  same group, with no proof printed in the version read.
- Nguyen et al. state that their scheme "is always mass conservative
  for each phase", but advance the primitive vector,
  $\mathsf W^{n+1}=\mathsf W^n+\Delta t\,\mathcal L(\mathsf W^n)$ with
  $\mathcal L=-[\partial u/\partial \mathsf W]^{-1}\nabla\cdot f$ in each
  stage of the third-order Runge–Kutta method (Eqs. 29–30; the minus
  sign is missing in print), and do not say how the conserved
  variables are recovered. If they are evaluated as $u(\mathsf W^{n+1})$, a
  Taylor expansion gives
  $u(\mathsf W^{n+1})=u(\mathsf W^n)-\Delta t\,\nabla_h\cdot f+O(\Delta t^2)$ per cell,
  with $\nabla_h\cdot f$ the flux difference. Every component of $u$,
  starting with $\phi_k\rho_k(p,T)$, is nonlinear in $\mathsf W$, so the
  $O(\Delta t^2)$ remainder does not telescope over the cells. The
  update then conserves the phasic masses only up to that remainder,
  not to round-off, and the [Lax–Wendroff](/results/lax-wendroff-theorem.md)
  argument does not apply as it stands *(compiler check, not in the
  sources)*. The paper shows no conservation-error measurement.
- Nguyen et al. use Wood's sound speed, the speed of mechanical
  equilibrium only, as the eigenvalue of a model in pressure **and**
  temperature equilibrium, without derivation. With $\mathsf b_k$ the
  thermal expansion coefficient of phase $k$ and $\mathsf v_k=1/\rho_k$
  (page-local), holding the mixture entropy fixed instead of each
  phasic entropy adds to Wood's $1/(\rho c^2)$ the term
  $\rho T\big[\sum_kY_k\mathsf v_k^2\mathsf b_k^2/C_{p,k}-\big(\sum_kY_k\mathsf v_k\mathsf b_k\big)^2/\sum_kY_kC_{p,k}\big]$,
  which is $\ge0$ by the Cauchy–Schwarz inequality. The
  $p$–$T$-equilibrium sound speed is therefore not larger than Wood's,
  and smaller unless $\mathsf v_k\mathsf b_k/C_{p,k}$ is the same for
  every phase, so the printed eigenvalues overestimate the wave speeds
  of the model they solve *(compiler check, not in the sources)*.
- Du & Yang print the Wilke mixing rule with $X_i$ where $X_j$ is meant
  inside the denominator sum (as printed the mole fractions cancel), and
  the Arrhenius factor as $\exp\big(E_{a,r}/(R_uT)\big)$, where Peng et
  al. (Eq. 8) print $\exp\big(-E/(RT)\big)$; Du & Yang do not say
  whether their activation energies carry the sign. Peng et al. print the
  axisymmetric source $p$ in the axial momentum row, where the
  axisymmetric form puts it in the radial one, and a "mass" production rate without the molar-mass factor.
- Bielawski et al. print the reactor temperature equation as
  $dT/dt=-\sum_kY_k/c_{v,k}\,\sum_k(\epsilon_k/W_k)\Omega_k$ (Eq. 12;
  $\epsilon_k$, $\Omega_k$ page-local: molar internal energy and mass
  production rate). It lacks a factor $1/\rho$ and has
  $\sum_kY_k/c_{v,k}$ where the constant-volume energy balance gives
  $1/\sum_kY_kc_{v,k}$ *(compiler check, not in the sources)*; they
  state that a Newton solve at constant internal energy replaces it in
  practice (§5).
- Du & Yang put the H$_2$/O$_2$/Ar diaphragm at $x=0.5$ cm in a 10 cm
  domain, Peng et al. at 50 mm in a 100 mm domain, with the same states
  and final time; as printed the two runs differ.

# Citations

- [Renac (2021)](/sources/renac-2021.md) — §1.2–1.3; §2, Eqs. (1)–(18); §3.1, Lemma 3.1, Eq. (24), Remarks 3.1–3.2; §4, Lemma 4.1, Eqs. (52)–(56); §5, Eqs. (62)–(64); §6, Theorem 6.1, Eq. (67); §7, Tables 1, 3, Fig. 4; Appendices A–D (arXiv v3).
- [Li, Duan & Tang (2022)](/sources/li-2022-c.md) — §1, Eqs. (1.1)–(1.2); §3.3–3.4, Eqs. (3.11)–(3.21); §5 (arXiv v1).
- [Nguyen et al. (2022)](/sources/nguyen-2022.md) — §1; §2.1–2.3, Eqs. (2)–(31); §3, Figs. 1–5, Table 1; Appendix.
- [Du & Yang (2022)](/sources/du-2022-b.md) — §2, Eqs. (2.1)–(2.8); §3, Thms. 3.1–3.2; §4, Lemma 4.1, Thms. 4.1–4.3; §5; §6, Eq. (6.1), Tables 6.1–6.3, Figs. 6.1–6.3.
- [Peng, Atkins & Deiterding (2022)](/sources/peng-2022.md) — §2.1, Eqs. (1)–(8); §3.2–3.3, Figs. 6–8 (accepted manuscript).
- [Bai & Li (2022)](/sources/bai-2022.md) — §1–2 (sharp-interface contrast only).
- [Bielawski et al. (2023)](/sources/bielawski-2023.md) — §2, Eqs. (1)–(7), Alg. 2; §3; §5, Eqs. (11)–(12); §6 (accepted manuscript).
- [Zhou et al. (2023)](/sources/zhou-2023.md) — §2, Eqs. (1)–(2); §4.3, Eq. (33); §5.4, Figs. 13–14; §5.8.
