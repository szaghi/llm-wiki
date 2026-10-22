---
type: Definition
title: "Five- and six-equation diffuse-interface models"
description: "Single-velocity diffuse-interface models of compressible two-phase flow: the five-equation model (two partial densities, mixture momentum and energy, a non-conservative volume-fraction equation, one pressure) in its Kapila and Allaire forms, and the six-equation pressure-disequilibrium model with instantaneous relaxation; their sound speeds, discretization of the non-conservative term, interface equilibrium and admissible states."
status: established
aliases: [five-equation model, 5-equation model, Kapila model, Allaire–Clerc–Kokh model, six-equation model, 6-equation model, diffuse-interface model, quasi-conservative two-phase model]
tags: [multiphase, interface-capturing, finite-volume, positivity, bound-preserving]
timestamp: 2026-10-22T12:00:00Z
---

# Five- and six-equation diffuse-interface models

A diffuse-interface model describes two immiscible compressible fluids
as one mixture on the whole domain: every cell carries the volume
fraction $\phi_k$ of each phase $k=1,2$ ($\phi_1+\phi_2=1$), the phasic
densities $\rho_k$, a single velocity $v$ and, in the five-equation
model, a single pressure $p$ (mechanical equilibrium); a material
interface is a thin region where $\phi_1$ goes from 0 to 1, captured
by the scheme like a contact rather than tracked. The six-equation
model drops the single pressure and relaxes the two phasic pressures
to each other. In this bundle the models are the setting of
[MFC](/software/mfc.md) ([Bryngelson et al. (2021)](/sources/bryngelson-2021.md)),
of unstructured [CWENO](/methods/cweno.md)
([Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md)) and of a
positivity-preserving [WCNS](/methods/weighted-compact-nonlinear-scheme.md)
([Wong et al. (2021)](/sources/wong-2021.md)); in all three each phase is
closed by the [stiffened-gas equation of state](/definitions/stiffened-gas-equation-of-state.md).

Page-local symbols: $\phi_k$, $\rho_k$, $e_k$, $c_k$ (volume fraction,
density, specific internal energy and sound speed of phase $k$),
$Y_k=\phi_k\rho_k/\rho$ the mass fraction, $K$ the Kapila coefficient.

## The five-equation model

The form used by Tsoutsanis et al. (§2) and Wong et al. (§2,
Eqs. 1–5), after Allaire, Clerc & Kokh, is

$$
\begin{aligned}
&\partial_t(\phi_1\rho_1)+\nabla\cdot(\phi_1\rho_1v)=0,\qquad
\partial_t(\phi_2\rho_2)+\nabla\cdot(\phi_2\rho_2v)=0,\\
&\partial_t(\rho v)+\nabla\cdot(\rho v\otimes v)+\nabla p=0,\qquad
\partial_tE+\nabla\cdot\big((E+p)v\big)=0,\\
&\partial_t\phi_1+v\cdot\nabla\phi_1=0,
\end{aligned}
$$

with $\rho=\phi_1\rho_1+\phi_2\rho_2$, $\rho e=\phi_1\rho_1e_1+\phi_2\rho_2e_2$
and $p_1=p_2=p$. The first four equations are conservation laws; the
volume-fraction equation is not, which is why the system is called
quasi-conservative. With stiffened-gas phases the mixture is again a
stiffened gas whose constants depend on $\phi_1$ alone, and the mixture
sound speed is $\rho c^2=\gamma(p+p_\infty)$ with the mixture constants
(Wong et al. Eqs. 7–11).

**Kapila form.** Bryngelson et al. write the model as
$\partial_tq+\nabla\cdot F(q)+h(q)\nabla\cdot v=s(q)$ with
$q=(\phi_1,\phi_1\rho_1,\phi_2\rho_2,\rho v,E)$ and a volume-fraction
equation that carries an extra compressibility term (§3.1, Eqs. 1–10):

$$
\partial_t\phi_1+v\cdot\nabla\phi_1=K\,\nabla\cdot v,\qquad
K=\frac{\rho_2c_2^2-\rho_1c_1^2}{\dfrac{\rho_2c_2^2}{\phi_2}+\dfrac{\rho_1c_1^2}{\phi_1}}.
$$

This is Kapila et al.'s model; it is thermodynamically consistent and
its mixture sound speed is Wood's,

$$
\frac{1}{\rho c^2}=\sum_k\frac{\phi_k}{\rho_kc_k^2}.
$$

The models of Allaire et al. and of Massoni et al. omit $K$; according
to Bryngelson et al. they "do not strictly obey the second-law of
thermodynamics, nor reproduce the correct mixture speed of sound", and
MFC offers both. They add that the $K$ term "can result in numerical
instabilities for problems with strong compression or expansion in
mixture regions due to its non-conservative nature", and leave the
choice to the user (§3.1–3.2). MFC also adds viscous stresses to the
momentum and energy equations (Eqs. 3–4).

**Rewritten volume-fraction equation.** Tsoutsanis et al., after
Johnsen & Colonius, write the advection equation as
$\partial_t\phi_1+\nabla\cdot(\phi_1v)=\phi_1\nabla\cdot v$ (Eq. 12),
and Wong et al. append $\phi_1v$ to the flux and $\phi_1\nabla\cdot v$
to a source term in the same way (Eqs. 28–31). Both forms turn the
non-conservative part into a source proportional to $\nabla\cdot v$,
which the scheme must discretize consistently with the flux (next
section).

## The six-equation model

Bryngelson et al. §3.2 describe the pressure-disequilibrium model of
Saurel, Petitpas & Berry, which MFC also implements: the total-energy
equation is replaced by two phasic internal-energy equations, each phase
keeps its pressure $p_k$, and a relaxation source drives $p_1-p_2$ to
zero at a rate controlled by a relaxation coefficient; the phases
exchange work through an interfacial pressure weighted by the acoustic
impedances $\rho_kc_k$ (Eqs. 11–13). Its frozen sound speed
$c^2=\sum_kY_kc_k^2$ (Eq. 14) differs from Wood's. MFC applies infinite
relaxation at every Runge–Kutta stage, after a first-order explicit
step of the non-relaxed hyperbolic system and an energy
re-initialization that conserves the total energy. The pressure is then
unique at the end of the stage, the effective mixture sound speed is
Wood's, the five- and six-equation models reconstruct the same
variables, and the six-equation model costs about 5 % more on a
spherical bubble collapse (§3.2, §4.6, quoting an earlier MFC paper).

## Discretizing the non-conservative term

The volume-fraction equation needs the velocity divergence (or the
velocity gradient) at the same accuracy and in the same discrete form
as the fluxes; the sources do it in three ways.

- **Riemann-solver velocity on faces.** Tsoutsanis et al. approximate
  $\int\phi_1\nabla\cdot v\,dV$ by the cell average of $\phi_1$ times
  the sum over face quadrature points of the normal velocity returned
  by the HLLC solver, the same estimate as in the flux (Eqs. 15–16).
  Wong et al. use the HLLC contact speed $s_*$ both as the interface
  velocity in $\phi_1\nabla\cdot v$ and as the upwinding speed of the
  volume-fraction flux, and reconstruct the interface velocity of the
  source with the same compact differencing as the flux (§3.2,
  Eqs. 40–45; §4.1, Eqs. 81–82); with this choice the first-order
  update of $\phi_1$ is exactly upwind.
- **Midpoint divergence.** Bryngelson et al. evaluate
  $(\nabla\cdot v)$ in each cell by a midpoint rule from face-averaged
  velocities computed like the fluxes (§4.1, Eq. 31).

## Interface equilibrium and the choice of reconstructed variables

Across a material interface moving with the flow, $p$ and $v$ are
continuous while $\rho$, $\phi_k$ and the equation-of-state constants
jump. A scheme that reconstructs conserved variables then mixes the
jumps of every component into the pressure and creates spurious
pressure and velocity oscillations. The three sources agree on the
remedy, reconstruction of primitive variables:

- Bryngelson et al. recall that, for an advected air–water interface,
  conservative-variable reconstruction is "corrupted by spurious
  oscillations and the pressures can even become negative", while
  primitive-variable reconstruction keeps velocity and pressure free
  of oscillations to round-off (§5.5, recalled from Coralic & Colonius;
  not rerun in the paper). MFC reconstructs primitive variables by
  default, with characteristic and conservative variables as options
  (§2.2, §4.1).
- Tsoutsanis et al. show it on an isolated interface with a jump in
  $\gamma$ ($\gamma=1.4$ against $1.66$, density 10 against 1, $p$ and
  $v$ uniform): conservative reconstruction oscillates, primitive
  reconstruction gives normalized pressure and velocity errors "close
  to machine precision" for several CWENO orders, and they use primitive
  reconstruction in every later test (§4.2, Figs. 3–4). They convert
  back to conservative variables before evaluating fluxes (§3.3).
- Wong et al. interpolate characteristic variables obtained from the
  primitive variables $(\phi_1\rho_1,\phi_2\rho_2,v_1,v_2,p,\phi_1)$ by
  the eigenvectors of the primitive quasilinear system, whose
  eigenvalues in $x$ are $v_1-c$, $v_1$ (four times) and $v_1+c$
  (Appendix A; see [characteristic decomposition](/methods/characteristic-decomposition.md)).
  On a 1D water slab advected through air (density ratio
  $1000/1.204$, $\phi_1=1-10^{-8}$ in the water) the relative velocity
  and pressure errors stay at $O(10^{-12})$ and $O(10^{-10})$ (§6.2,
  Figs. 5–6).

The same equilibrium requirement drives the multicomponent
([Renac (2021)](/sources/renac-2021.md), see
[multicomponent Euler equations](/definitions/multicomponent-euler-equations.md))
and sharp-interface ([level-set methods](/methods/level-set-method.md))
literature; the property is a moving-interface analogue of
[stationary contact preservation](/properties/stationary-contact-preservation.md).

## Admissible states and bound preservation

The physically admissible set of the five-equation model is
$0\le\phi_1\le1$, $\phi_k\rho_k\ge0$ and $\rho c^2>0$. Wong et al.
prove that it is convex when the ideal-gas phase has the smaller
$\gamma$ (Lemma 1, Theorem 1; see
[stiffened-gas equation of state](/definitions/stiffened-gas-equation-of-state.md)),
and build a scheme that stays in it:

1. **First-order HLLC.** With Einfeldt wave speeds and Batten's contact
   speed, all HLLC star states have non-negative partial densities,
   keep $\phi_1$ of the upwind state and keep $\rho e-p_\infty>0$; the
   needed bound on the left wave speed is implied by
   $s^-\le v_1-c$ of the left state. The first-order scheme with the
   contact speed as advection velocity is positivity- and
   boundedness-preserving in 2D under CFL $\le0.5$, by a directional
   convex splitting of the update (§3.3, Eqs. 46–70; see
   [HLL-family solvers](/methods/hll-riemann-solvers.md)).
2. **High-order limiting.** An interpolation limiter blends each
   interpolated state with the first-order nodal state, successively
   for partial densities, volume fractions and $\rho e-p_\infty$; a flux
   limiter then blends the high-order flux with the first-order HLLC
   flux in the same three stages (Algorithms 1–6). The tolerances are
   $10^{-10}$ (partial densities and volume fractions) and $10^{-8}$
   ($\rho e-p_\infty$), so the volume fraction is kept in
   $[10^{-10},1-10^{-10}]$, not in $[0,1]$. The limiting is
   conservative for the conservative equations, i.e. all but the
   $\phi_1$ equation, and extends to SSP Runge–Kutta at the same CFL
   bound 0.5 (§5). See [positivity-preserving flux limiter](/methods/positivity-preserving-flux-limiter.md)
   and [bound preservation](/properties/bound-preservation.md).
3. **Necessity.** On a Mach 10 shock–water-column problem the scheme
   without the limiters fails with an imaginary sound speed, while the
   limited scheme runs (§6.6; see
   [shock–water-column interaction](/benchmarks/shock-water-column.md)).

MFC takes a weaker route: volume fractions are clipped to $[0,1]$ and
renormalized to sum to one only when mixture properties are computed,
so the stored state and mass conservation are untouched, and an
optional limiter blends the WENO flux with a first-order flux according
to a ratio of consecutive volume-fraction differences (minmod, MC,
superbee, van Leer and others), because "the WENO schemes we utilize
are, in general, not TVD" (Bryngelson et al. §4.2, Eqs. 33–34; see
[hybrid central-WENO schemes](/methods/hybrid-weno.md)). Neither device
is a positivity guarantee.

## Qualifications

- "Characteristic variables" means different projections in the
  sources. Tsoutsanis et al. state that "reconstruction in conservative
  or characteristic variables suffer from oscillations" at interfaces
  with variable $\gamma$, citing earlier work (§4.2), while Wong et al.
  interpolate characteristic variables of the primitive system without
  oscillations. The two statements are compatible if Tsoutsanis et
  al.'s characteristic variables are those of the conservative system;
  Tsoutsanis et al. do not test characteristic reconstruction.
- Wong et al.'s convexity result assumes one ideal-gas phase and
  $\gamma_{\mathrm{liquid}}>\gamma_{\mathrm{gas}}$; Bryngelson et al.'s
  thermodynamic objection to the models without $K$ applies to the form
  Tsoutsanis et al. and Wong et al. use, which neither of them
  discusses.
- Tsoutsanis et al. print the semi-discrete update (Eq. 16) with the
  flux sum on the right-hand side without the minus sign their Eq. (13)
  implies, and multiply the whole vector by the source term that only
  enters the $\phi_1$ component.
- The six-equation results (cost, sound speed after relaxation) are
  quoted by Bryngelson et al. from an earlier paper, not shown in the
  paper read.

# Citations

- [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) — §2.2, §3.1–3.2, Eqs. (1)–(14); §4.1–4.2, Eqs. (31)–(34); §4.6; §5.5 (arXiv v1).
- [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) — §2, Eqs. (1)–(12); §3.1, Eqs. (13)–(16); §3.3; §4.2, Figs. 3–4.
- [Wong et al. (2021)](/sources/wong-2021.md) — §2, Eqs. (1)–(14); §3.2–3.3, Eqs. (19)–(70); §4.1–4.2; §5; §6.2, §6.6; Appendix A (arXiv v1).
- [Renac (2021)](/sources/renac-2021.md) — §1.2, §7.2 (comparison only; arXiv v3).
