---
type: Definition
title: "Multicomponent Euler equations"
description: "The fully conservative Euler system for a mixture of several gases or stiffened fluids in thermal and mechanical equilibrium, written with partial densities, mass fractions or molar concentrations, and its reacting Navier–Stokes extension; its closures, admissible set, wave structure and mixture entropy, and the entropy-stable, positive and bound-preserving schemes built on it, with their behaviour at material interfaces."
status: established
aliases: [multi-component Euler equations, multispecies Euler equations, compressible multicomponent Euler system, HRM model (as named by Renac)]
tags: [multiphase, entropy-stable, positivity, bound-preserving, dg, finite-difference]
timestamp: 2026-10-24T05:59:00Z
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
[Li, Duan & Tang (2022c)](/sources/li-2022-c.md) §1 writes them with
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
(Eqs. 1–2);
[Fujiwara, Tamaki & Kawai (2023)](/sources/fujiwara-2023.md) solve the
$n_{\mathrm c}$ partial densities, momentum and total energy, and show the
$(\rho,\rho Y_1,\dots,\rho Y_{n_{\mathrm c}-1})$ form equivalent, also
discretely for their scheme (§2.1, Eq. (1); Appendix A);
[Peyvan et al. (2023)](/sources/peyvan-2023.md) solve the one-dimensional
reacting Navier–Stokes system with all partial densities (§2.1, Eqs. (1)–(7);
arXiv v1), and [Trojak & Dzanic (2024)](/sources/trojak-2024.md) solve
the multi-species Euler and Navier–Stokes systems with all partial
densities, $\rho=\sum_k\rho Y_k$, in thermal equilibrium (§2, Eqs.
(1)–(6); arXiv v1). [Ching et al. (2025)](/sources/ching-2025.md)
(§2, Eqs. (2.1)–(2.6)) solve the reacting Navier–Stokes system with the
molar concentrations $\mathsf C_k$ (page-local) as species unknowns,
$u=(\rho v,\ \rho e_{\mathrm t},\ \mathsf C_1,\dots,\mathsf C_{n_{\mathrm c}})$
with $\rho Y_k=W_k\mathsf C_k$ and $\rho=\sum_kW_k\mathsf C_k$ ($e_{\mathrm t}$ the
specific total energy, page-local). [Jiao et al. (2024)](/sources/jiao-2024.md) (§2.1,
Eqs. (2–1)–(2–2)) call their mixture system, mixture mass, momentum
and energy plus one species-mass equation per non-condensable gas, a
"four-equation model" and state that it "is fully conservative when no
additional source terms are introduced". Unlike the
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

**Stiffened components.** Li et al. (2022c) close each component with the
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
application. Fujiwara et al. (§2.2, Eq. (4)) write the same rule for the
function $\mathsf G=1/(\gamma-1)$ (page-local; the source's $G$, which is
not the registry's admissible set) as
$$\mathsf G=\bar W\sum_k\frac{\mathsf G_kY_k}{W_k},\qquad \mathsf G_k=\frac1{\gamma_k-1},\qquad \bar W=\Big(\sum_k\frac{Y_k}{W_k}\Big)^{-1},$$
so that $\rho e=p\,\mathsf G$; for stiffened components they add
$\rho e=p\,\mathsf G+\mathsf A$ with the same mixing rule for
$\mathsf A_k=\gamma_kp_{\infty,k}/(\gamma_k-1)$ (Appendix B, Eqs. (B.1)–(B.2);
page-local $\bar W$, $\mathsf A$).

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
$\Omega_k$ (the mass production rate of the registry) in the species equations (Peng et al. Eqs. 4–8; Du &
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
Ching et al. (2025) use NASA polynomials for the species heat capacities,
$p=R_uT\sum_k\mathsf C_k$, a species entropy with the term
$-R_k\ln(\mathsf C_k/\mathsf C_{\mathrm{ref}})$, mixture-averaged diffusion
velocities corrected so that $\sum_kW_k\mathsf C_kV_k=0$ (page-local $V_k$),
whose coefficients "can be nonzero for $\mathsf C_k=0$", Wilke viscosity and
Mathur conductivity, and Strang splitting between transport and a fully
implicit temporal DG step for the chemistry (§2, §3, Eqs. (2.3)–(2.6),
(3.3)–(3.5)).

**Vibrationally excited air.** Peyvan et al. take five-species air
($\mathrm N$, $\mathrm O$, $\mathrm{NO}$, $\mathrm N_2$, $\mathrm O_2$,
no ionization) with a rigid-rotor harmonic-oscillator internal energy and
the ideal-gas law $p=\sum_k\rho Y_kR_kT$ (§2.2.1, §3, Eqs. (8)–(12), (60)).
Let $e^0_k$ be the formation energy, $\theta^{\mathrm v}_k$ the
vibrational characteristic temperature, $\mathsf a_k=3/2$ for atoms and
$5/2$ for diatomic molecules, and $\mathsf d_k\in\{0,1\}$ the vibration
switch (page-local; the source's $\theta_k$, $a_k$, $\alpha_k$). Then

$$e_k=e^0_k+\mathsf a_kR_kT+\mathsf d_kR_k\frac{\theta^{\mathrm v}_k}{e^{\theta^{\mathrm v}_k/T}-1}$$

(Eq. (60)). Transport coefficients (Chapman–Enskog, Stefan–Maxwell
diffusion) and Park's five-reaction finite-rate chemistry come from the
Mutation++ library (§2.2.2–2.2.3).

**Mixture ratio of specific heats from mass fractions.** Trojak & Dzanic
(Eq. (4)) take ideal gases in thermal equilibrium with
$p=(\gamma-1)\rho e$ and the mixture ratio
$\gamma=\sum_k\rho Y_kC_{p,k}\big/\sum_k\rho Y_kC_{v,k}$, and for
Navier–Stokes mass-fraction-weighted viscosity and Prandtl number
(Eq. (6)).

**A barotropic cavitating mixture.** Jiao et al. (§2.2, after Örley et
al. and Trummler et al.) close the system for liquid, liquid–vapour
mixture and up to two isothermal ideal gases by a barotropic
equilibrium law: the liquid density is linearized about saturation,
$\rho=\rho_{\mathrm{sat,liq}}+(p-p_{\mathrm{sat}})/c^2$, with the
mixture sound speed $(p_{\mathrm{sat}}/\rho_{\mathrm{sat,liq}})^{1/2}$
below saturation, the gases are ideal at fixed reference temperatures,
and the vapour volume fraction follows from the density (Eqs.
(2–3)–(2–7)); stiffened-gas and Peng–Robinson closures with an energy
equation are given in appendices.

**A cubic real-fluid law.** [Terashima, Ly & Ihme (2025)](/sources/terashima-2025.md)
(§2.9, Eqs. (41)–(52), after Soave) close the system for transcritical
methane–nitrogen mixtures with the Soave–Redlich–Kwong equation of state,
$p=\rho R_uT/(\bar W-\mathsf b\rho)-\rho^2\mathsf a(T)/\big(\bar W(\bar W+\mathsf b\rho)\big)$, with
$R_u$ the universal gas constant, $\bar W$ the mixture molar mass (registry
§10), and $\mathsf a=\sum_k\sum_lX_kX_l\sqrt{\mathsf a_k\mathsf a_l\mathsf s_k\mathsf s_l}$, $\mathsf b=\sum_kX_k\mathsf b_k$
mole-fraction mixing rules over the critical-point constants
$\mathsf a_k=0.42748R_u^2T_{c,k}^2/p_{c,k}$, $\mathsf b_k=0.08664R_uT_{c,k}/p_{c,k}$ and the
acentric-factor correction $\mathsf s_k(T)$ (page-local $R_u$, $X_k$ the mole
fraction, $\mathsf a$, $\mathsf b$, $\mathsf s_k$, $T_{c,k}$, $p_{c,k}$; the source's $a\alpha$, $b$,
$\alpha_i$); thermally perfect parts follow Chemkin II.
With such a law spurious interface pressure oscillations appear even in a
single-species flow, e.g. cryogenic into warm nitrogen at supercritical
pressure (§1).

**A two-material marker form.** [Gaburro et al. (2024)](/sources/gaburro-2024.md)
(§2.1, Eqs. (8)–(18); arXiv v1) write two-gas Euler with one advected
marker $\chi_{\mathrm m}$ (page-local), conserved as $\rho\chi_{\mathrm m}$,
and the mixture law $p=(\tilde\gamma-1)(E-\tfrac12\rho\lvert v\rvert^2)$
with either $1/(\tilde\gamma-1)=\chi_{\mathrm m}/(\gamma-1)$,
$\chi_{\mathrm m}=(\gamma-1)/(\gamma_k-1)$ in component $k$, or the
"simpler" $\tilde\gamma=\chi_{\mathrm m}\gamma$, $\chi_{\mathrm m}=\gamma_k/\gamma$.
They evolve it in the primitive variables $(\rho,v,p,\chi_{\mathrm m})$
(see Material interfaces).

## Admissible set and waves

Renac's admissible set is
$\{0\le Y_k\le1,\ \rho>0,\ e>0\}$ (Eq. 9). In direction $n$ the
eigenvalues are $v\cdot n\mp c$ (genuinely nonlinear) and $v\cdot n$
with multiplicity $n_{\mathrm c}+d-1$ (linearly degenerate), with
$c^2=\gamma(Y)\big(\gamma(Y)-1\big)e$ and $\gamma(Y)\le\max_k\gamma_k$
(Eqs. 10–11). Renac notes that, to the author's knowledge, fast upper bounds of
the maximum wave speed (two-rarefaction or Guermond–Popov type), which
simple-wave solvers such as HLL, Rusanov or relaxation need, do not
exist for this model (§1.3). Li et al. (2022c) give the entropy-scaled right-eigenvector
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
$\sum_kY_k=1$ holds exactly, which the section on bound preservation
below obtains from the scheme.

## Mixture entropy

Renac and Li et al. (2022c) use the mass-weighted mixture entropy. Renac sets
$\eta=-\rho s$, $s=\sum_kY_ks_k$, $s_k=C_{v,k}\ln\big(e_k/\rho_k^{\gamma_k-1}\big)+\mathrm{const}$,
and obtains the entropy flux $F_\eta=-\rho sv$ and the flux potential
$\psi=R(Y)\rho v$ (Eqs. 13–18). Li et al. (2022c) set
$\eta=-\sum_k\rho Y_kS_k$ with $S_k=C_{v,k}\ln T-R_k\ln(\rho Y_k)$, flux
potential $\big(\sum_k(R_k\rho Y_k-p_{\infty,k}/T)\big)v$ (Eqs. 3.16–3.17).
The entropy variables $w$ have one component per partial density (or
mass fraction), plus $v/T$ and $-1/T$ (Renac Eq. 17; Li et al. (2022c) §3.3).
Peyvan et al. extend the mass-weighted entropy of Gouasmi et al. to the
vibrational energy above,
$s_k=\int c_{v,k}(\tau)\tau^{-1}d\tau-R_k\ln\rho_k$ with
$c_{v,k}=de_k/dT$ (§3, Eqs. (62)–(64)), and their entropy variables have
the same structure (Eqs. (65)–(66)).
Trojak & Dzanic (Eqs. (8)–(11), after Gouasmi et al.) use the
physical-sign mixture entropy
$\rho s=\sum_kC_{v,k}\rho Y_k\ln\big((\rho Y_k)^{1-\gamma_k}T\big)$,
$T=\rho e/\sum_kC_{v,k}\rho Y_k$, with its local minimum principle.
Since $C_{v,k}\ln\big((\rho Y_k)^{1-\gamma_k}T\big)=C_{v,k}\ln T-R_k\ln(\rho Y_k)$,
this is $-\eta$ of Li et al. (2022c) for ideal gases *(compiler check,
not in the sources)*. Enforced everywhere as a constraint of their
positivity-preserving [entropy filter](/methods/entropy-filtering.md),
it over-dissipates at species interfaces, because a smooth mixture
density can consist of discontinuous partial densities that make the
entropy field ill-behaved (§3.1, Figs. 1–4); they enforce it only in
elements where a pressure-jump sensor exceeds 1, keep positivity of
$\rho$, $p$ and every $\rho Y_k$ always, and replace the entropy by the
exponential of the sum with $\max(\epsilon,\rho Y_k)$ in the logarithm
to keep it defined at zero partial density (§§3.1–3.3, Eqs. (22)–(27)).

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
discretely (Remark 3.2). Li et al. (2022c) derive explicit two-point fluxes for
one and two stiffened components from jumps of the parameter vector
$(\rho Y_k,v,1/T)$ and logarithmic means of the partial densities and
of $1/T$, with an extra "entropy-conservative state" for the
mesh-velocity term on moving meshes (§3.3, Eqs. 3.11–3.18).

Peyvan et al. derive two-point entropy-conservative fluxes for the
vibrationally excited mixture from Tadmor's condition, with the parameter
vector $(\rho Y_k,v,1/T)$ (§3, Eqs. (68)–(91)). The vibrational term needs
a new mean. For a page-local quantity $q$ they define the exponential mean
$\{\!\{q\}\!\}_{\exp,k}=(q^+-q^-)/(e^{\theta^{\mathrm v}_kq^+}-e^{\theta^{\mathrm v}_kq^-})$
and the composite mean
$\{\!\{q\}\!\}_{\ln\exp,k}=\{\!\{e^{\theta^{\mathrm v}_kq}-1\}\!\}_{\log}\{\!\{q\}\!\}_{\exp,k}$,
so that $[\![\ln(e^{\theta^{\mathrm v}_kq}-1)]\!]=[\![q]\!]/\{\!\{q\}\!\}_{\ln\exp,k}$
(Eqs. (78)–(82); page-local symbols). The flux is

$$\begin{aligned}
f^{\mathrm{ec}}_{\rho Y_k}&=\{\!\{v\}\!\}\{\!\{\rho Y_k\}\!\}_{\log},\\
f^{\mathrm{ec}}_{\rho v}&=\frac{\sum_kR_k\{\!\{\rho Y_k\}\!\}}{\{\!\{1/T\}\!\}}+\{\!\{v\}\!\}\sum_kf^{\mathrm{ec}}_{\rho Y_k},\\
f^{\mathrm{ec}}_{E}&=\sum_k\Big(e^0_k-\mathsf d_kR_k\theta^{\mathrm v}_k+\frac{\mathsf a_kR_k}{\{\!\{1/T\}\!\}_{\log}}+\frac{\mathsf d_kR_k}{\{\!\{1/T\}\!\}_{\ln\exp,k}}-\tfrac12\{\!\{v^2\}\!\}\Big)f^{\mathrm{ec}}_{\rho Y_k}+\{\!\{v\}\!\}f^{\mathrm{ec}}_{\rho v}
\end{aligned}$$

(Eqs. (89)–(91)). For nearly equal states the exponential mean is
evaluated by a truncated series in $\sinh x/x$, after the device of
Winters et al. for the logarithmic mean (Eqs. (83)–(87);
[logarithmic mean](/operators/logarithmic-mean.md)). The authors claim
that the flux is also kinetic-energy preserving, citing Ranocha, without
showing it (end of §3). They state that no entropy-conservative flux had
been derived before for an internal energy with translational,
rotational and vibrational parts, Gouasmi et al. covering constant or
polynomial specific heats (§1). With entropy-conservative volume and
surface fluxes and no stabilization, the global entropy rate on a smooth
periodic five-species problem stays at $O(10^{-5})$ up to $t=0.1$, which
they attribute to the $\sim10^{-7}$ tolerance of the Newton inversion of
energy to temperature in Mutation++ (§4.4, Fig. 4).

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
- Li et al. (2022c) add to their high-order entropy-conservative flux a
  dissipation built on jumps of [multi-resolution WENO](/methods/multi-resolution-weno.md)
  reconstructions of the scaled entropy variables with a sign switch,
  a [TeCNO-type](/methods/tecno-scheme.md) construction, on an
  [adaptive moving mesh](/methods/adaptive-moving-mesh.md) (§3.4,
  Eq. 3.21). They show total-entropy conservation and decay numerically
  ([isentropic vortex](/benchmarks/isentropic-vortex.md)) and state
  that the entropy inequality follows as in the single-component case;
  no proof is printed.

**Entropy-stable DGSEM for reacting hypersonic flow.** Peyvan et al. use
the flux above in the volume terms of an entropy-stable
[DGSEM](/methods/dgsem.md), with HLLC surface fluxes and the
[subcell finite-volume blending](/methods/subcell-finite-volume-limiting.md)
of Hennemann et al. ($\alpha\le0.5$), BR1 viscous terms and the
low-storage fourth-order Runge–Kutta method of Carpenter and Kennedy
(§2.3, §4). On one-dimensional strong-shock and reacting problems they
compare it with flux reconstruction and spectral difference stabilized by
an [entropy filter](/methods/entropy-filtering.md), the
positivity-preserving modal DG and the positivity-preserving fifth-order
finite-difference WENO of Zhang and Shu. On the three-species Sod problem
with one dissociation reaction all schemes except the modal DG give the
right solution; WENO and ES-DGSEM do not oscillate but smear more (§4.3,
Fig. 3). The filtered FR and SD extensions to five species are unstable,
because no filter strength satisfies positivity of the five densities,
positivity of pressure and the entropy criterion at once (§4.5.1). The
hypersonic ES-DGSEM matches the Grossman–Cinnella non-equilibrium Sod
reference in all five mass fractions (Fig. 6). Equilibrium and finite-rate
chemistry agree at a driver temperature of 2000 K and diverge from
3000 K on (§4.5.2, Fig. 7).

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
  $\beta$ (page-local) large enough that $u\pm\beta^{-1}f\in G$ (Lemma 4.1, Eq. 3.5),
  now including the species diffusion velocities.
- **Stiff chemistry.** A third-order conservative modified exponential
  Runge–Kutta method of the authors replaces
  [SSP Runge–Kutta](/methods/ssp-runge-kutta.md); each stage is a convex
  combination of a convective update, admissible under a CFL bound with
  the Gauss–Lobatto weight $1/(N_{\mathrm{GL}}(N_{\mathrm{GL}}-1))$ (Theorem 4.1; see
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
$\Delta t=\min(a\Delta x/\beta^*,b\Delta x^2/\eta^*)$ (page-local constants $a$, $b$ and bounds $\beta^*$, $\eta^*$, not the registry's wave speed and entropy) with a simpler
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
(above) is the property such a scheme loses.

**Separated viscous flux and an entropy bound on the convective part.**
Ching et al. (2025) extend their positivity-preserving and entropy-bounded
DG scheme for the reacting multicomponent Euler equations to Navier–Stokes
(§4). The admissible set is $\{\rho>0,\ \rho e^*>0,\ \mathsf C_k\ge0\}$ with
$e^*$ the specific internal energy minus its value at zero temperature (positive iff
$T>0$; page-local), convex because $\rho e^*$ is concave, and the entropy-bounded
set adds $\rho s-\rho\sigma\ge0$ for a lower bound $\sigma$ (page-local), which
is concave only if every $\mathsf C_k>0$ and is assumed convex anyway (Eqs.
(4.1)–(4.3)). Unlike Du & Yang, who treat convective and viscous fluxes as
one, they keep an HLLC inviscid flux and apply Zhang's Lax–Friedrichs-type
penalty to the viscous flux alone, with a coefficient larger than the
largest ratio of species diffusive molar flux to concentration and than a
temperature bound (Lemma 1, Eqs. (4.4)–(4.5)); the cell-average update is
split into convective and viscous halves, the first kept in the
entropy-bounded set and the second in the positivity set (Thms 6, 8). The
entropy bound is imposed on the convective part only, because the minimum
entropy principle fails for Navier–Stokes with nonzero thermal diffusivity
(§1). At a zero concentration no finite penalty keeps $\mathsf C_k\ge0$, since
the diffusive molar flux is not proportional to $\mathsf C_k$ (Remarks 2–3);
a scaling of the species gradients restores positivity, needed only at the
first step of two detonation runs (§4.7, §5.4). Details are on
[positivity-preserving Navier–Stokes flux](/methods/positivity-preserving-navier-stokes-flux.md).

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

**A fully conservative, pressure-equilibrium-preserving scheme.**
Fujiwara et al. (2023) state that conventional conservative schemes for
the species masses, momentum and total energy generate spurious pressure
oscillations at interfaces even when the interfaces and the specific heats
vary smoothly, so interface-capturing diffusion is "not a fundamental
solution" (§1). They classify the remedies as non-conservative (Karni's
pressure equation, Abgrall's transport of $\mathsf G$) or overspecified
([double-flux methods](/methods/double-flux-method.md), which carry two
discrete pressures or two species masses). For an arbitrary equation of
state $\rho e=\rho e(p,\rho Y_k)$ with initially uniform $p$ and $v$, they
derive the condition for pressure equilibrium (§2.3, Eqs. (5)–(12)):

$$\partial_x(\rho e)=\sum_k\Big(\frac{\partial\rho e}{\partial\rho Y_k}\Big)_{p,\rho Y_{l\ne k}}\partial_x(\rho Y_k).$$

For ideal gases it reduces to Abgrall's condition
$\partial_t\mathsf G+v\,\partial_x\mathsf G=0$ (Eq. (15)). Its discrete
analogue on a half-point flux form, the "compatibility condition", is a
condition on the interface values used in the fluxes (Eq. (21); see
[pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)).
For ideal gases they satisfy it, for any number of species, by the
symmetric interface values

$$\rho Y_k\big|_{i+1/2}=\tfrac12\big(\mathsf w^-\rho Y_{k,i}+\mathsf w^+\rho Y_{k,i+1}\big),\qquad
\mathsf G\big|_{i+1/2}=\tfrac12(\mathsf G_i+\mathsf G_{i+1}),\qquad
\mathsf w^+=\frac{\bar W_{i+1}\rho_i}{\rho_{i+1}\bar W_i}=\frac1{\mathsf w^-}$$

(Eqs. (38)–(39), (48); page-local $\mathsf w^\pm$, the source's
$\phi^\pm$). In a second-order central flux these give FC/PE (S), a
[split form](/methods/split-convective-forms.md) that reduces to the
KEEP-PE scheme of Shima et al. for one component, and FC/PE (D), a
divergence form (Table 1). Both are fully conservative and preserve
pressure equilibrium for a uniform velocity. With a nonuniform velocity
only FC/PE (S) satisfies the extended condition (§5, Eqs. (55)–(59)).

On smooth (tanh-profiled) interfaces advected at uniform $p$ and $v$,
FC/PE (S) keeps $p$ and $v$ at $\simeq10^{-13}$ (1D, two species, 501
points) and $\simeq10^{-12}$ (2D, three species, $501^2$), conserves mass
and energy exactly and runs to $t=20$. Over the same 1D run the
pressure-equation scheme loses energy conservation and the
$\mathsf G$-transport scheme loses species-mass conservation. FC/PE (D)
diverges at $t\approx3.8$ and the non-equilibrium divergence scheme at
$t\approx6.5$ (1D) and $5.5$ (2D) (§4, Figs. 2–8; see
[material-interface advection](/benchmarks/material-interface-advection.md)).
Shocks and sharp interfaces are outside the scope: the authors offer the
scheme as a non-dissipative baseline to which numerical diffusion must
still be added (§1, §6).

**Approximate pressure equilibrium for any equation of state.**
Terashima, Ly & Ihme (2025) extend the analysis to an arbitrary law
$p=p(\rho Y_k,\rho v,E)$. For initially uniform $p$ and $v$ the discrete
condition on a central half-point flux form reduces to the interface values
of $\rho e$ and $\rho Y_k$ alone,
$$\rho e\big|_{i+1/2}-\rho e\big|_{i-1/2}=\sum_k\varepsilon^{\mathrm e}_{k,i}\big(\rho Y_k\big|_{i+1/2}-\rho Y_k\big|_{i-1/2}\big),\qquad
\varepsilon^{\mathrm e}_k=\Big(\frac{\partial\rho e}{\partial\rho Y_k}\Big)_{p,\rho Y_{l\ne k}}$$
(§2.5, Eq. (19); page-local $\varepsilon^{\mathrm e}_k$, the source's $\epsilon_i$),
which they identify with Fujiwara et al.'s compatibility condition. Because
$\varepsilon^{\mathrm e}_k$ is evaluated at the node $i$, the condition is
asymmetric, and they state that no locally defined interface values satisfy
it in all cells for a general law (§2.5–2.6; argued, not proved). Splitting
it into two half-cell relations and eliminating between neighbours gives,
with arithmetic means of $\rho Y_k$,
$$\rho e\big|_{i+1/2}=\tfrac12(\rho e_i+\rho e_{i+1})-\sum_k\tfrac12\big(\varepsilon^{\mathrm e}_{k,i+1}-\varepsilon^{\mathrm e}_{k,i}\big)\,\tfrac12\big(\rho Y_{k,i+1}-\rho Y_{k,i}\big)$$
(Eq. (25)), the internal-energy value of the fully conservative
[APEC scheme](/methods/apec-scheme.md), whose pressure-equilibrium residual is
second order with smaller constants than the plain arithmetic mean (Eqs.
(32)–(33)). For any law
$\varepsilon^{\mathrm e}_k=-\rho C_v(\partial p/\partial\rho Y_k)_T/(\partial p/\partial T)+(\partial\rho e/\partial\rho Y_k)_T$
(Eq. (48), App. B; $C_v$ the mixture specific heat at constant volume,
page-local), evaluated in closed form for the cubic law above (Eqs.
(49)–(52)); for calorically perfect gases it is Eq. (59). The quasi-conservative
variant PEqC replaces the internal-energy flux divergence in the energy
equation by $\sum_k\varepsilon^{\mathrm e}_k\partial_x(\rho Y_kv)$, which keeps pressure
equilibrium exactly but loses energy conservation (§2.11, Eq. (54)). On
advected methane–nitrogen interfaces the fully conservative scheme with
arithmetic means blows up (1D after $t=0.09$ s, and with 4001 points around $t=0.11$ s; 2D at
about $t=0.1$ s), while APEC stays stable with pressure errors of about
0.02% in 2D and conserves energy; PEqC keeps the pressure error near
$10^{-8}$ with a growing energy error (§3.2, Figs. 6–12;
[pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md),
[material-interface advection](/benchmarks/material-interface-advection.md)).
Fujiwara et al.'s exact ideal-gas interface values do not follow from
Eq. (25); substituting their $\rho Y_k$ values into the general half-cell form
returns their arithmetic $\rho e$ value (§3.1).

Nguyen et al. report the opposite outcome for a moving interface: a
water–air interface advected at 150 m/s at uniform $p$, $v$ and $T$
keeps velocity, pressure and temperature errors "on the order of
$10^{-14}$", about three cells thick with superbee or the compressive
overbee limiter on the volume fractions, also with initial temperature
jumps of 100 and 500 K (§3.1, Figs. 1–5). Their reconstruction is MUSCL
($\kappa_{\mathrm M}=1/3$) on $(p,v,T,\phi_k)$ with Van Leer on the other variables
and overbee on the volume fractions (Eqs. 26–28; see
[TVD limiters](/definitions/total-variation-diminishing.md)), the flux
Rusanov or an HLLC solver carrying the partial densities with the star
factor (Eqs. 19–25; see [HLL-family solvers](/methods/hll-riemann-solvers.md)),
and the time update acts on the primitive vector; see Qualifications
for what this costs in conservation.

**Conservation where it is needed.** Gaburro et al. take the
opposite route to fully conservative schemes. Their ADER-DG scheme
evolves the primitive variables, which avoids the interface pressure
oscillations of conservative schemes; it is not conservative, but they
prove a modified Lax–Wendroff theorem for "locally quasi-conservative"
schemes whose conservation defect vanishes with $h$ (Prop. 1; see
[Lax–Wendroff theorem](/results/lax-wendroff-theorem.md)), show that the
defect vanishes for smooth solutions and across contacts with uniform
velocity and pressure for both marker closures (Props. 2–5,
generalizing Abgrall), and restore exact conservation at shocks by a
conservative second-order finite-volume update in subcells flagged by
a shock sensor (§4.4). They attribute the oscillations of a conservative
second-order finite-volume scheme in the Quirk–Karni and Haas–Sturtevant
problems to "the conservative fluxes at material interfaces", "not
related to Gibbs-like oscillations" ([shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)).
Trojak & Dzanic (§1) state the trade-off from the other side: conservative
multi-species formulations cannot preserve pressure equilibrium at
species interfaces but predict shock speeds correctly, which makes them
"critical" at high Mach number; they expect the oscillations to decay
with resolution (§5.1.3).

**Recomputing the face density from the equation of state.** Jiao et
al. (§3.3, Eq. (3–5)) reconstruct only the gas mass fractions at a
liquid–gas interface, with [THINC](/methods/thinc-reconstruction.md)
($\beta_{\mathrm T}=1.6$), and recompute the face density from the
reconstructed mass fractions and the interface pressure of an all-Mach
flux, $\rho^*=\rho(p^*,Y^*)$, instead of reconstructing it; on 1D
two-component interface advection (100 cells, four periods) pressure and
velocity stay at their initial values (§4.1, Figs. 4.2–4.3; see
[pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)).

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
instability with re-shock (Mach 1.21, Atwood number 0.6053). Li et al. (2022c):
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

Ching et al. (2025): a 1D H$_2$/O$_2$ thermal-bubble advection–diffusion test
(order $N+1$ for $N=1$–3), a premixed H$_2$/O$_2$ flame compared with
Cantera, where species clipping overpredicts velocity and minor species, a
viscous N$_2$/He shock tube with walls (after Houim & Kuo), a 2D
H$_2$–O$_2$–Ar detonation with adiabatic no-slip walls, on which the
temperature approaches zero before 50 μs without the entropy limiter, and a
3D reacting shock–mixing-layer interaction on tetrahedra (§5;
[shock-induced combustion](/benchmarks/shock-induced-combustion.md)).

## Qualifications

- Gaburro et al.'s position that only shocks need exact conservation
  stands beside Fujiwara et al.'s fully conservative scheme that
  preserves pressure equilibrium; the two are not in conflict as
  recorded, because Fujiwara et al.'s interfaces are smooth and
  non-dissipative and Gaburro et al.'s evidence concerns a second-order
  conservative ENO scheme at sharp interfaces. Gaburro et al. print the
  constant $\Gamma_0$ of App. B, case 3, as
  $\frac{1}{\chi_2-\chi_1}\big(\frac1{\gamma_2-1}-\frac1{\gamma_2-1}\big)$,
  identically zero; their own linear map below Eq. (64) has
  $\frac1{\gamma_2-1}-\frac1{\gamma_1-1}$.
- Jiao et al. claim full conservation of their four-equation model
  without a conservation test, while they recall that quasi-conservative
  models conserve species masses poorly.

- Renac calls the moving-interface oscillations "inherent to discretely
  conservative schemes", while Fujiwara et al. present FC/PE (S) as a
  discretely conservative scheme that preserves pressure equilibrium, and
  claim it is the first. The scopes differ: Renac's moving interface is a
  discontinuity computed by a dissipative entropy-stable DGSEM;
  Fujiwara et al.'s interfaces are smooth and their scheme has no
  dissipation. A shock-capturing scheme built on the compatibility
  condition, run on a sharp moving interface, would decide whether the
  two statements conflict. Trojak & Dzanic's general statement that
  conservative formulations cannot preserve pressure equilibrium (§1,
  citing Abgrall and others) has the scope of Renac's, filtered DSEM at
  sharp species interfaces, and is recorded the same way on
  [pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md).
- Peyvan et al. (arXiv v1) print the rotational energy as $R/W_k$ without
  the factor $T$ (Eq. (11)), against $\mathsf a_k=5/2$ in Eq. (60), and the
  vibrational part of $c_{v,k}$ with a negative sign (Eq. (62)), while
  Eq. (64) follows from the positive one *(compiler check, not in the
  sources: $\frac{d}{dT}\frac{\theta}{e^{\theta/T}-1}=\frac{\theta^2}{T^2}\frac{e^{\theta/T}}{(e^{\theta/T}-1)^2}>0$)*.
  *(Compiler check, not in the sources: their Eq. (66) differs from the
  Gibbs form of Eq. (65) by the constant $R_k$, which leaves every jump, and
  hence the flux, unchanged.)* They
  print no timings for their claim that ES-DGSEM "requires the least
  computational effort".

- Renac's design-order table is irregular on coarse meshes (at $N=1$ the
  error grows from $1/4$ to $1/8$; at $N=3$ the rate falls to 3.33 at
  $1/64$ after 4.96), while the text states that the expected order is
  recovered.
- Renac calls the model "the HRM model (1)" without expanding the
  acronym.
- The positivity theorem covers the forward-Euler update and cell
  averages; the time-step bound 0.4 used in practice is not covered by
  it.
- Li et al. (2022c)'s entropy-stability statement and their curvilinear
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
- Du & Yang print the Wilke mixing rule with $X_i$ inside the denominator sum, where
  the summation index requires $X_j$ (as printed the mole fractions cancel), and
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

- [Ching et al. (2025)](/sources/ching-2025.md) — §1; §2, Eqs. (2.1)–(2.7); §3, Eqs. (3.3)–(3.9); §4.1, Lemma 1, Remarks 2–3, 5; §4.2–4.4, Thms 6, 8; §4.7; §5.

- [Trojak & Dzanic (2024)](/sources/trojak-2024.md) — §1; §2, Eqs. (1)–(11); §3, Eqs. (22)–(27) (arXiv v1).
- [Gaburro et al. (2024)](/sources/gaburro-2024.md) — §2.1, Eqs. (8)–(18); §4, Props. 1–5, App. B; §5.2 (arXiv v1).
- [Jiao et al. (2024)](/sources/jiao-2024.md) — §1.1, §1.3; §2.1–2.2, Eqs. (2–1)–(2–7); §3.3, Eq. (3–5); §4.1.
- [Renac (2021)](/sources/renac-2021.md) — §1.2–1.3; §2, Eqs. (1)–(18); §3.1, Lemma 3.1, Eq. (24), Remarks 3.1–3.2; §4, Lemma 4.1, Eqs. (52)–(56); §5, Eqs. (62)–(64); §6, Theorem 6.1, Eq. (67); §7, Tables 1, 3, Fig. 4; Appendices A–D (arXiv v3).
- [Li, Duan & Tang (2022c)](/sources/li-2022-c.md) — §1, Eqs. (1.1)–(1.2); §3.3–3.4, Eqs. (3.11)–(3.21); §5 (arXiv v1).
- [Nguyen et al. (2022)](/sources/nguyen-2022.md) — §1; §2.1–2.3, Eqs. (2)–(31); §3, Figs. 1–5, Table 1; Appendix.
- [Du & Yang (2022)](/sources/du-2022-b.md) — §2, Eqs. (2.1)–(2.8); §3, Thms. 3.1–3.2; §4, Lemma 4.1, Thms. 4.1–4.3; §5; §6, Eq. (6.1), Tables 6.1–6.3, Figs. 6.1–6.3.
- [Peng, Atkins & Deiterding (2022)](/sources/peng-2022.md) — §2.1, Eqs. (1)–(8); §3.2–3.3, Figs. 6–8 (accepted manuscript).
- [Bai & Li (2022)](/sources/bai-2022.md) — §1–2 (sharp-interface contrast only).
- [Bielawski et al. (2023)](/sources/bielawski-2023.md) — §2, Eqs. (1)–(7), Alg. 2; §3; §5, Eqs. (11)–(12); §6 (accepted manuscript).
- [Zhou et al. (2023)](/sources/zhou-2023.md) — §2, Eqs. (1)–(2); §4.3, Eq. (33); §5.4, Figs. 13–14; §5.8.
- [Terashima, Ly & Ihme (2025)](/sources/terashima-2025.md) — §1; §2.1–2.11, Eqs. (1)–(59); §3.1–3.2, Figs. 1–14; App. B.
- [Fujiwara, Tamaki & Kawai (2023)](/sources/fujiwara-2023.md) — §1; §2.1–2.3, Eqs. (1)–(16); §3, Eqs. (17)–(49), Table 1; §4, Figs. 2–8; §5, Eqs. (55)–(59); Appendices A–B.
- [Peyvan et al. (2023)](/sources/peyvan-2023.md) — §1; §2.1–2.3, Eqs. (1)–(55); §3, Eqs. (60)–(91); §4.3–4.5, Figs. 3–7 (arXiv v1).
