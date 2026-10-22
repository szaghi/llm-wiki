---
type: Definition
title: "Multicomponent Euler equations"
description: "The fully conservative Euler system for a mixture of several gases or stiffened fluids in thermal and mechanical equilibrium, written with partial densities or mass fractions; its closure, admissible set, wave structure and mixture entropy, and the entropy-conservative, entropy-stable and positive schemes built on it, with their behaviour at stationary and moving material interfaces."
status: established
aliases: [multi-component Euler equations, multispecies Euler equations, compressible multicomponent Euler system, HRM model (as named by Renac)]
tags: [multiphase, entropy-stable, positivity, dg, finite-difference]
timestamp: 2026-10-22T00:00:00Z
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
the partial densities $\rho Y_k$ of all components (Eq. 1.1). Unlike the
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
With $p_{\infty,k}=0$ it reduces to Renac's closure. They name water at
very high pressure (underwater explosions, shock lithotripsy) as the
application.

## Admissible set and waves

Renac's admissible set is
$\{0\le Y_k\le1,\ \rho>0,\ e>0\}$ (Eq. 9). In direction $n$ the
eigenvalues are $v\cdot n\mp c$ (genuinely nonlinear) and $v\cdot n$
with multiplicity $n_{\mathrm c}+d-1$ (linearly degenerate), with
$c^2=\gamma(Y)\big(\gamma(Y)-1\big)e$ and $\gamma(Y)\le\max_k\gamma_k$
(Eqs. 10–11). Renac notes that, to his knowledge, fast upper bounds of
the maximum wave speed (two-rarefaction or Guermond–Popov type), which
simple-wave solvers such as HLL, Rusanov or relaxation need, do not
exist for this model (§1.3). Li et al. give the entropy-scaled right-eigenvector
matrices (whose product with their transpose is $\partial u/\partial w$)
explicitly for one and two stiffened components, following Gouasmi et al.'s ideal-gas
construction for two (§3.4; see
[characteristic decomposition](/methods/characteristic-decomposition.md)).

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
for the flux of Gouasmi, Duraisamy & Murman type that he re-derives in
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

## Material interfaces

Because the system is conservative, its schemes meet the
pressure-equilibrium problem of moving interfaces directly. Renac
proves that his DGSEM resolves stationary material interfaces (different
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

## Tests in the sources

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

# Citations

- [Renac (2021)](/sources/renac-2021.md) — §1.2–1.3; §2, Eqs. (1)–(18); §3.1, Lemma 3.1, Eq. (24), Remarks 3.1–3.2; §4, Lemma 4.1, Eqs. (52)–(56); §5, Eqs. (62)–(64); §6, Theorem 6.1, Eq. (67); §7, Tables 1, 3, Fig. 4; Appendices A–D (arXiv v3).
- [Li, Duan & Tang (2022)](/sources/li-2022-c.md) — §1, Eqs. (1.1)–(1.2); §3.3–3.4, Eqs. (3.11)–(3.21); §5 (arXiv v1).
