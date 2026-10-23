---
type: Definition
title: "Five- and six-equation diffuse-interface models"
description: "Single-velocity diffuse-interface models of compressible two-phase flow: the five-equation model (two partial densities, mixture momentum and energy, a non-conservative volume-fraction equation, one pressure) in its Kapila and Allaire forms, and the six-equation pressure-disequilibrium model with instantaneous relaxation; their sound speeds, discretization of the non-conservative term, interface equilibrium and admissible states."
status: established
aliases: [five-equation model, 5-equation model, Kapila model, Allaire–Clerc–Kokh model, six-equation model, 6-equation model, diffuse-interface model, quasi-conservative two-phase model]
tags: [multiphase, interface-capturing, finite-volume, positivity, bound-preserving]
timestamp: 2026-10-23T15:06:00Z
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
([Wong et al. (2021)](/sources/wong-2021.md)), and of a non-dissipative
kinetic-energy- and entropy-preserving central scheme
([Jain & Moin (2022)](/sources/jain-2022.md)); in all four each phase is
closed by the [stiffened-gas equation of state](/definitions/stiffened-gas-equation-of-state.md).
[Chamarthi (2023a)](/sources/chamarthi-2023.md) uses the model, with
ideal-gas phases, as the two-species setting of a
[gradient-based](/methods/gradient-based-reconstruction.md)
finite-difference scheme with a
[monotonicity-preserving limiter](/methods/monotonicity-preserving-limiter.md)
and HLLC fluxes, viscous terms included after Coralic & Colonius.
[Huang & Johnsen (2023)](/sources/huang-2023.md) generalize the model to
$N$ phases with a [phase-field](/methods/phase-field-method.md) flux in
every equation, and solve its hyperbolic part, the five-equation model, by
second-order MUSCL finite volumes with HLLC.
[Yan, Abgrall & Wu (2024)](/sources/yan-2024.md) solve the Kapila form with
ideal-gas phases by bound-preserving
[OEDG](/methods/oedg.md) discontinuous Galerkin schemes, uniformly high order
thanks to a new discretization of the non-conservative term.

Page-local symbols: $\phi_k$, $\rho_k$, $e_k$, $c_k$ (volume fraction,
density, specific internal energy and sound speed of phase $k$),
$Y_k=\phi_k\rho_k/\rho$ the mass fraction, $K$ the Kapila coefficient,
$s_k$ and $T_k$ the specific entropy and temperature of phase $k$, and
$j_k$ the volumetric interface-regularization flux of phase $k$
(defined below), and $\Lambda_k$ the compressibility coefficient of
Huang & Johnsen's $N$-phase form (their $K_p$).

## The five-equation model

The form used by Tsoutsanis et al. (§2), Wong et al. (§2,
Eqs. 1–5) and Chamarthi (2023a, §2, Eqs. 7–12), after Allaire, Clerc &
Kokh, is

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
(Wong et al. Eqs. 7–11). For ideal-gas phases Chamarthi closes the
mixture by $\frac1{\gamma-1}=\sum_k\frac{\phi_k}{\gamma_k-1}$, with
$\gamma_k$ (page-local) the ratio of specific heats of phase $k$
(Eqs. 10–12).

**With viscosity and surface tension.** [Zhang et al. (2024a)](/sources/zhang-2024.md)
(§2.1, Eqs. (1)–(8)) use the Allaire / Murrone–Guillard form with the viscous stress in
the momentum and energy equations and surface tension as a continuum volume force
(Perigaud & Saurel): $-\sigma_{\mathrm{st}}\kappa_{\mathrm c}\nabla\phi_1$ in the momentum
equation and $-\sigma_{\mathrm{st}}\kappa_{\mathrm c}\big(\nabla\cdot(\phi_1v)-\phi_1\nabla\cdot v\big)$
in the energy equation, the volume-fraction equation written as
$\partial_t\phi_1+\nabla\cdot(\phi_1v)-\phi_1\nabla\cdot v=0$ and the capillary energy term
in the same flux-plus-source form "for consistency". *(Compiler check, not in the sources:
the capillary energy term equals $\sigma_{\mathrm{st}}\kappa_{\mathrm c}\,v\cdot\nabla\phi_1$.)*
They compare three mixture sound speeds with stiffened-gas phases (§2.3, Fig. 1): the
mixture-constant form $\rho c^2=\gamma(p+p_\infty)$, used throughout; Wood's, which is
non-monotone in the volume fraction and "may" give inaccurate acoustics across a diffused
interface and computational failure; and the six-equation frozen form, which also works but
is "not as efficient" in their tests.

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
momentum and energy equations (Eqs. 3–4). Jain & Moin use the same
Kapila form, with the same coefficient $K$ (their Eq. 7), and state that
it is preferred over Allaire et al.'s form for high compression or
expansion, while for weakly compressible flows both gave identical
results in their experience (§2; the last part is an observation, not
shown).

**One coefficient for both forms.** Huang & Johnsen (2023) write the
volume-fraction equation of phase $k$, $k=1,\dots,N$, with a coefficient
$\Lambda_k$ subject only to $\sum_k\phi_k\Lambda_k=0$ (§2.1, Eq. (1); here
without their phase-field terms):

$$
\partial_t\phi_k+\nabla\cdot(\phi_kv)=\phi_k(1+\Lambda_k)\,\nabla\cdot v .
$$

$\Lambda_k=0$ is Allaire et al.'s form, and
$\Lambda_k=\rho c^2/(\rho_kc_k^2)-1$ is Kapila et al.'s, which gives
Wood's sound speed. For stiffened-gas phases the mixture sound speed of
the general form is

$$
\rho c^2=\frac{\sum_k\phi_k\rho_kc_k^2(1+\Lambda_k)/(\gamma_k-1)}{\sum_k\phi_k/(\gamma_k-1)},
$$

so with $\Lambda_k=0$ it is a convex combination of the phasic
$\rho_kc_k^2$ (§2.9, Eqs. (23)–(25); $\gamma_k$ page-local, the
stiffened-gas ratio of phase $k$). *(Compiler check, not in the sources:
for two phases the Kapila choice gives
$\phi_1\Lambda_1=\phi_1\phi_2(\rho_2c_2^2-\rho_1c_1^2)/(\phi_1\rho_2c_2^2+\phi_2\rho_1c_1^2)$,
which is Bryngelson et al.'s $K$ above, and Wood's relation gives
$\sum_k\phi_k\Lambda_k=\rho c^2\sum_k\phi_k/(\rho_kc_k^2)-1=0$.)* In the
incompressible limit the volume-fraction and mass equations of a phase of
constant density are consistent only if $\Lambda_k=-1$; Kapila's
coefficient satisfies this and Allaire's does not (§5.3). The authors
nonetheless set $\Lambda_1=0$ in all their computations, "as in"
earlier works (§3).

**The same coefficient as a source factor.** Yan, Abgrall & Wu (2024)
(§1, Eqs. (1.1)–(1.3); §2.1, Eq. (2.1)) write Kapila's coefficient with the
phasic compressibilities $\mathsf k_k=1/(\rho_kc_k^2)$ (page-local; not the reduced wavenumber $\vartheta$) as
$K=\phi_1\phi_2(\mathsf k_1-\mathsf k_2)/(\phi_1\mathsf k_1+\phi_2\mathsf k_2)$, and
recast the volume-fraction equation as
$$\partial_t\phi_1+\nabla\cdot(\phi_1v)=\chi_1\phi_1\nabla\cdot v,\qquad
\chi_1=\frac{K}{\phi_1}+1=\frac{\mathsf k_1}{\phi_1\mathsf k_1+\phi_2\mathsf k_2},\quad
\chi_2=-\frac{K}{\phi_2}+1,$$
so that $\chi_1\phi_1+\chi_2\phi_2=1$ (page-local $\chi_k$). $\phi_1$ is then
carried as a "conservative" component with flux $\phi_1v$, plus a
non-conservative source. *(Compiler check, not in the sources: multiplying
numerator and denominator of Bryngelson et al.'s $K$ above by
$\phi_1\phi_2\mathsf k_1\mathsf k_2$ gives Yan et al.'s form, and by Wood's
relation $\chi_k=\rho c^2/(\rho_kc_k^2)=1+\Lambda_k$ with Huang & Johnsen's Kapila
choice of $\Lambda_k$.)* With ideal-gas phases and $p_1=p_2=p$ the mixture
law is $\frac1{\gamma-1}=\sum_k\frac{\phi_k}{\gamma_k-1}$, as in Chamarthi
(2023a). They call the $K=0$ model the Allaire–Massoni model, "also called
the five-equation transport model", citing an earlier paper for its being
"not compatible with the assumption that the material derivatives of the
phase entropies are zero" (§1).

## Conservative diffuse-interface regularization and phase entropy

Jain & Moin (2022) add to the Kapila model the interface-regularization
fluxes of the conservative diffuse-interface (phase-field) method of
Jain, Mani & Moin, which keep the interface at a fixed thickness
(§2, Eqs. 1–5, recalled from that work):

$$
\begin{aligned}
&\partial_t\phi_1+\nabla\cdot(\phi_1v)=(\phi_1+K)\,\nabla\cdot v+\nabla\cdot j_1,\qquad
\partial_t(\phi_k\rho_k)+\nabla\cdot(\phi_k\rho_kv)=\nabla\cdot(\rho_kj_k),\\
&j_1=\Gamma\big(\varepsilon_{\mathrm I}\nabla\phi_1-\phi_1(1-\phi_1)\hat n_1\big),\qquad j_2=-j_1,\qquad
\hat n_1=\frac{\nabla\phi_1}{\lvert\nabla\phi_1\rvert},
\end{aligned}
$$

with $\Gamma$ a velocity scale and $\varepsilon_{\mathrm I}$ an
interface-thickness scale (page-local), and consistent correction terms
$\nabla\cdot(v\otimes f_{\mathrm r})$ and
$\nabla\cdot(\kappa f_{\mathrm r}/\rho+\sum_k\rho_kh_kj_k)$, where
$f_{\mathrm r}=\sum_k\rho_kj_k$ is the regularization mass flux and $h_k$
the phasic specific enthalpy, in the momentum and energy equations; the
momentum equation also carries viscous stress, surface tension and
gravity. The mixture mass equation becomes
$\partial_t\rho+\nabla\cdot(\rho v)=\nabla\cdot f_{\mathrm r}$ (Eq. 10).
The method conserves the mass of each phase, momentum and total energy,
keeps $\phi_1$ bounded, and reduces to the single-phase Navier–Stokes
equations when the phase properties coincide (§1, §2.3, stated as
properties of Jain, Mani & Moin's method).

From the Gibbs relation of each phase they derive transport equations
for the phasic entropies (§2.2, Eqs. 16–20): $\rho_k\phi_k\,Ds_k/Dt$ is a
combination of terms proportional to the regularization flux $j_k$, so
phase entropy is conserved only in the limit $j_k\to0$ of the equilibrium
(hyperbolic-tangent) interface profile, where
$\partial_t(\rho_k\phi_ks_k)+\nabla\cdot(\rho_k\phi_ks_kv)=0$ and the
mixture entropy $\rho s=\sum_k\rho_k\phi_ks_k$ is conserved (Eq. 21).
Interface regularization is therefore irreversible. On a stationary
air–water slab the entropy change it causes is small and positive for
$\varepsilon_{\mathrm I}=0.75\Delta x$ and $1.25\Delta x$, and
negligible for $\varepsilon_{\mathrm I}=\Delta x$, the equilibrium
thickness (Appendix A, Fig. 12; the paper prints no value in the text).
The entropy here is the physical phasic entropy $s_k$, which increases,
not the registry's mathematical entropy $\eta$.

**A generic regularization flux.** Huang & Johnsen (2023) leave the
flux $j_k$ unspecified and propagate it into every equation: $-\rho_kj_k$
in the flux of the partial density of phase $k$, a consistent mass flux
$\sum_k(\phi_kv-j_k)\rho_k$ in the momentum and energy fluxes, and
$-\sum_k\nabla\cdot j_k$ inside the compressibility term of the
volume-fraction equation (§2.1–2.4, Eqs. (1)–(8)). They state the
conditions on $j_k$ for the second law, Galilean invariance, interface
equilibrium and consistency of reduction (Theorems 2.2–2.5), and single
out $\sum_kj_k=0$ as the favourable case. *(Compiler check, not in the
sources: Jain & Moin's two-phase flux above, with $j_2=-j_1$, is such a
case.)* With the conservative Allen–Cahn model supplying
$\nabla\cdot j_1$, the interface stays 4–5 cells thick for an
interface-thickness parameter equal to $\Delta x$, where without the
regularization it keeps thickening (§4). The discrete flux and its bound
preservation are on [phase-field methods](/methods/phase-field-method.md).

**Rewritten volume-fraction equation.** Tsoutsanis et al., after
Johnsen & Colonius, write the advection equation as
$\partial_t\phi_1+\nabla\cdot(\phi_1v)=\phi_1\nabla\cdot v$ (Eq. 12),
and Wong et al. append $\phi_1v$ to the flux and $\phi_1\nabla\cdot v$
to a source term in the same way (Eqs. 28–31); Chamarthi (2023a) uses
the same rewriting, after Johnsen & Colonius, "for an oscillation-free
interface", with the source $\phi_1\nabla\cdot v$ as the last component
of the source vector (Eq. 13). These forms turn the
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

**Mixture-energy-consistent form with phase change.**
[Wakimura et al. (2024)](/sources/wakimura-2024.md) (§2, Eqs. (1)–(16)) use the
six-equation model of Pelanti & Shyue, with phasic total energies
$E_k=\rho_ke_k+\tfrac12\rho_k\lvert v\rvert^2$ (page-local) in place of internal energies:

$$
\begin{aligned}
&\partial_t\phi_1+v\cdot\nabla\phi_1=\mathsf r_{\mathrm p}(p_1-p_2)+\frac{\mathcal Q}{\kappa_{\mathrm I}}+\frac{\dot m}{\rho_{\mathrm I}},\qquad
\partial_t(\phi_k\rho_k)+\nabla\cdot(\phi_k\rho_kv)=\pm\dot m,\\
&\partial_t(\rho v)+\nabla\cdot\big(\rho v\otimes v+(\phi_1p_1+\phi_2p_2)I\big)=0,\\
&\partial_t(\phi_1E_1)+\nabla\cdot\big(\phi_1(E_1+p_1)v\big)+\Sigma=-\mathsf r_{\mathrm p}p_{\mathrm I}(p_1-p_2)+\mathcal Q+e_{\mathrm I}\dot m,
\end{aligned}
$$

and the $\phi_2E_2$ equation with $-\Sigma$ and opposite sources, where
$\Sigma=-v\cdot\big(Y_2\nabla(\phi_1p_1)-Y_1\nabla(\phi_2p_2)\big)$, $\dot m$ carries the
$+$ sign in the phase-1 mass equation, the heat exchange is
$\mathcal Q=\mathsf r_{\mathrm T}(T_2-T_1)$ and the mass transfer
$\dot m=\mathsf r_{\mathrm g}(\mathsf g_2-\mathsf g_1)$ (page-local: relaxation rates
$\mathsf r_{\mathrm p},\mathsf r_{\mathrm T},\mathsf r_{\mathrm g}$, phasic Gibbs energies
$\mathsf g_k$, interface pressure $p_{\mathrm I}$, density $\rho_{\mathrm I}$, energy
$e_{\mathrm I}$, coefficient $\kappa_{\mathrm I}$; the last three need not be specified for
infinite rates). They choose it because its frozen sound speed $c^2=\sum_kY_kc_k^2$ is
monotone in the volume fraction, unlike Wood's speed of Kapila's model, which (citing earlier
works) can make transport of the mixture zone unstable (§1, §2.3). All rates are taken
infinite and the model is solved by a fractional-step method
([operator splitting](/methods/operator-splitting.md)): a hyperbolic step, then mechanical,
thermal and chemical relaxation in one of four orderings (p; p–pT; p–pTg; p–pT–pTg, Eq. (45)),
the last two with phase change. In closed form (Appendices B–D):

- *mechanical:* with $p_{\mathrm I}=p^*$, the relaxed pressure solves
  $a(p^*)^2+bp^*+d=0$, $a=\gamma_1\phi_2^0+\gamma_2\phi_1^0$,
  $b=-\gamma_1\phi_2^0(p_2^0-p_{\infty,1})-\gamma_2\phi_1^0(p_1^0-p_{\infty,2})$,
  $d=-\gamma_1\phi_2^0p_2^0p_{\infty,1}-\gamma_2\phi_1^0p_1^0p_{\infty,2}$, and
  $\phi_k^*=\phi_k^0\,\frac{(\gamma_k-1)p^*+p_k^0+\gamma_kp_{\infty,k}}{(\gamma_k-1)p^*+p^*+\gamma_kp_{\infty,k}}$
  (Eqs. (B.4)–(B.7), superscript $0$ the state before relaxation);
- *thermal:* a quadratic in the common pressure at constant mass fractions (Eqs. (C.4)–(C.7));
- *chemical:* a quadratic for the temperature as a function of pressure, substituted into the
  saturation curve $\mathsf g_1=\mathsf g_2$ and solved for the pressure by Newton–Raphson
  (Eqs. (D.4)–(D.7)).

The roots are taken in a cancellation-free form, which still loses digits near a double root
(App. E). Thermal and chemical relaxation act only where $10^{-4}\le\phi_1\le1-10^{-4}$, and
chemical relaxation only where the liquid is above the saturation temperature, i.e. evaporation
only; the authors found this does not affect the solution, without showing it (§2.4).
*(Compiler check, not in the sources: the mechanical coefficients follow from
$\phi_1^*+\phi_2^*=1$ with the printed $\phi_k^*$.)* The stiffened-gas parameters of water and
dodecane are on the [stiffened-gas](/definitions/stiffened-gas-equation-of-state.md) page.

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
- **HLLC-consistent face velocities in finite differences.** Chamarthi
  (2023a) evaluates the source at each grid point as
  $\phi_{1,i,j}\big[(v_{1,i+1/2}-v_{1,i-1/2})/\Delta x+(v_{2,j+1/2}-v_{2,j-1/2})/\Delta y\big]$
  (Eq. 95), with face velocities from the HLLC states,
  $$v_{1,i+1/2}=\tfrac12\big(1+\mathrm{sgn}(s_*)\big)\Big[v_1^-+\min(0,s^-)\Big(\frac{s^--v_1^-}{s^--s_*}-1\Big)\Big]+\tfrac12\big(1-\mathrm{sgn}(s_*)\big)\Big[v_1^++\max(0,s^+)\Big(\frac{s^+-v_1^+}{s^+-s_*}-1\Big)\Big]$$
  (Eqs. 93–94; $s_*$ the contact speed, $s^\pm$ the Einfeldt wave
  speeds, $v_1^\pm$ the face states), the volume fraction joining the
  HLLC star state of the two partial densities (Eq. 91;
  [HLL-family solvers](/methods/hll-riemann-solvers.md)).
  Zhang et al. (2024a) (§3.1, Eqs. (21)–(26), App. B) take the same route in finite
  volumes: $\phi_{1,i}\nabla\cdot v$ from the HLLC face velocities (Johnsen & Colonius),
  and the surface-tension terms from the HLLC face volume fraction and face velocity, with
  an HLLC star state and contact speed carrying the capillary pressure jump
  $\sigma_{\mathrm{st}}\kappa_{\mathrm c}[\![\phi_1]\!]$ (after Garrick et al.; see
  [HLL-family solvers](/methods/hll-riemann-solvers.md)).
- **Wave-weighted interface split in DG.** Yan, Abgrall & Wu (2024)
  (§2.1.2, Eqs. (2.8)–(2.15); 2D §3.1.2, Eqs. (3.6)–(3.15)) split the
  source integral $\int_{I_i}\chi_1\phi_1\,\partial_xv\,\varphi\,dx$ ($\varphi$ a DG
  test function, page-local) into the cell interior and two vanishing strips
  at the interfaces. The interior part is Gauss quadrature of
  $\chi_1\phi_1\partial_xv$; the interface part is the velocity jump
  $[\![v]\!]_{i+1/2}$ shared between the two cells with the HLL weights
  $-s^-/(s^+-s^-)$ (left cell) and $s^+/(s^+-s^-)$ (right cell), the wave
  speeds clipped at zero, so that all of the jump goes to the left cell
  when all waves move left and vice versa. Because $v=\rho v/\rho$ is not a
  polynomial in a cell, $\partial_xv$ is taken from the interpolant of $v$ at
  $N+1$ Gauss–Lobatto nodes, which makes the Gauss-quadrature integral of
  $\partial_xv$ equal the jump $v^-_{i+1/2}-v^+_{i-1/2}$ exactly (Eq. (2.10),
  Remark 2.1). They contrast it with the averaging discretization of
  earlier bound-preserving DG schemes, which multiplies the cell average of
  $\chi_1\phi_1$ by a weak derivative of $v$ with interface means and is
  formally second order, as one of those papers itself states (Remarks
  2.2, 3.2). On a smooth test with non-constant velocity the averaging
  variant drops to $L^1$ orders 1.75–1.84 ($\mathbb P^2$) and about 1.95
  ($\mathbb P^3$), while the new one keeps 3.25–3.77 and about 4.5 (Tables
  2–3); in 2D the averaging variant at $\mathbb P^3$ gives 0.91, $-0.08$, 1.42
  against 3.56, 4.12, 4.07 (Tables 5–6). The same split makes the $\phi_2$
  update identical in form to the $\phi_1$ update, the "symmetry of the
  volume fractions" used in the bound-preservation proof below
  ([symmetry preservation](/properties/symmetry-preservation.md)).
- **Midpoint divergence.** Bryngelson et al. evaluate
  $(\nabla\cdot v)$ in each cell by a midpoint rule from face-averaged
  velocities computed like the fluxes (§4.1, Eq. 31).

Huang & Johnsen (2023) give a reason for the first choice. Consistency of
reduction, i.e. that the scheme recovers the single-phase equations where
one phase is absent, requires the discrete $\nabla\cdot v$ of the
volume-fraction equation to equal the discrete $\nabla\cdot(\phi_1v)$
with $\phi_1\equiv1$, so the face velocity must be the one the Riemann
solver returns (§3.1, Theorem A.1).

## Interface equilibrium and the choice of reconstructed variables

Across a material interface moving with the flow, $p$ and $v$ are
continuous while $\rho$, $\phi_k$ and the equation-of-state constants
jump. A scheme that reconstructs conserved variables then mixes the
jumps of every component into the pressure and creates spurious
pressure and velocity oscillations. The three shock-capturing sources
agree on the remedy, reconstruction of primitive variables:

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
- Chamarthi (2023a) reconstructs the primitive vector
  $(\phi_1\rho_1,\phi_2\rho_2,v_1,v_2,p,\phi_1)$, optionally projected
  on characteristic fields at each face with the gradients projected by
  the same frozen left eigenvectors (§3.2–3.3, Eqs. 44–45, 62–64); which of
  the two each test uses is stated only for one figure ("using primitive
  variables"). Chamarthi reports no oscillations at the material interfaces of
  the two-fluid shock tube, the shock–curtain, the
  [shock–helium-cylinder](/benchmarks/shock-bubble-interaction.md), the
  multi-material [triple point](/benchmarks/triple-point-problem.md) and
  a viscous air–SF$_6$ [Richtmyer–Meshkov](/benchmarks/richtmyer-meshkov-instability.md)
  problem, with the interface thinnest for the author's compact-gradient MIG4
  scheme, compared with MEG6 and TENO5 (§4, Exs. 4.14–4.18).
- Huang & Johnsen (2023) state a sufficient condition for the mass
  variables: the partial densities and $\phi_1$ must be reconstructed by
  one scheme that commutes with affine maps $g=af+b$, so that a constant
  phasic density is preserved by the reconstruction ("consistent
  reconstruction of mass and volume fraction", Definition 1). MUSCL with
  most TVD limiters satisfies it; characteristic reconstruction does not.
  They therefore keep only velocity and pressure from the characteristic
  reconstruction and reconstruct the partial densities and $\phi_1$ from
  the primitive variables (§3.1). Reconstructing the partial densities by
  WENO5 with a positivity limiter and $\phi_1$ by MUSCL creates mass
  spikes near the interface (§5.1, Fig. 10). The same condition suffices
  for temperature equilibrium in the hyperbolic step, which they call
  weaker than the conditions of Beig & Johnsen (Theorem 5.2,
  Remark 5.2.1).

- Zhang et al. (2024a) reconstruct all primitive variables with the
  [incremental-stencil WENO](/methods/incremental-stencil-weno.md) and, in interfacial
  cells, replace only $\phi_1$ and the two partial densities by
  [THINC](/methods/thinc-reconstruction.md) values, the partial densities proportional to
  the THINC volume fraction at constant phasic density; velocity and pressure keep the WENO
  values "since pressure and velocity should be continuous at the interface" (§3.3,
  Eq. (45)). On a water block advected ten periods through air ($N_x=128$) the velocity and
  pressure errors are negligible and the interface free of oscillations (§4.1, Fig. 3).
  *(Compiler check, not in the sources: the proportional reconstruction keeps each cell's
  phasic densities constant at its face values, the property Huang & Johnsen's condition
  below is meant to secure.)*
- Wakimura et al. (2024) reconstruct the quasi-primitive vector
  $(\phi_1,\phi_1\rho_1,\phi_2\rho_2,v,p)$ of the six-equation model, at second order only,
  because "a numerical scheme that has accuracy higher than third-order may introduce
  spurious oscillation error due to the reconstruction of primitive variables" (§1, stated
  without evidence; see Qualifications).

Jain & Moin (2022) meet the same requirement in a non-dissipative
second-order central scheme without any reconstruction, by choosing the
split forms of the face fluxes (§3.3, Lemma 3.1, proof in Appendix B as
"Lemma 6.1"). Their interface-equilibrium condition, after Abgrall
(1996), is that uniform $v$ and $p$ stay uniform over one time step.
They prove that it holds, for stiffened-gas phases, when the
internal-energy flux $\widehat{\rho ev}$ has the same split form as the
mass flux and the volume-fraction flux, and the enthalpy part of the
regularization flux has the same split form as the regularization mass
flux. The quadratic split $\widehat{\rho ev}=\overline{\rho e}\,\bar v$
("QS") satisfies it; the cubic split $\bar\rho\,\bar e\,\bar v$ of
Kennedy & Gruber and Kuya et al. ("CS") and Chandrashekar's
harmonic-mean form ("CS-H") do not. At density ratio 10, CS and CS-H
cause "spurious mixing of internal energy at the interface" and diverge
on the inviscid two-phase Taylor–Green vortex and on two-phase isotropic
turbulence, while QS stays stable, also at density ratio 1000 and
initial Mach number up to 0.4 to $M_0t=100$ (§3.5, §4.1.2, §4.2,
Figs. 4–8; see [split convective forms](/methods/split-convective-forms.md),
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md),
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)). For
single-phase flow all three forms are stable (Figs. 2–3). The lemma is
proved for the stiffened gas; extension to a cubic equation of state is
stated, not shown.

Yan, Abgrall & Wu (2024) prove the interface-equilibrium condition, after
Abgrall, for their DG scheme with HLL fluxes: the semi-discrete scheme
with forward Euler (Lemma 2.5), the full scheme with
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md) and the oscillation-eliminating
step (Thm 2.6) and the bound-preserving limiter (Thm 2.14) all keep uniform
$v$ and $p$ uniform, the last two because they preserve every linear
identity of the state ([pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)).
In 2D only a constant velocity vector is covered; a contact with
discontinuous tangential velocity is not (Remark 3.5). On an advected
interface with $\gamma=5/3$ against 1.4 the velocity and pressure errors stay
within $\pm1.5\times10^{-12}$ at $t=1$ (Ex. 4.2, Fig. 4).

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

[Zhang et al. (2024a)](/sources/zhang-2024.md) (§3.3, Eqs. (47)–(48), Algorithm 1) reuse
the interpolation-limiter part of this construction after their WENO–THINC
reconstruction, in the same three loops (partial densities, volume fractions, then
$\rho c^2$), each blending the whole reconstructed primitive vector towards the cell value,
with thresholds $10^{-11}$ for the first two and $10^{-9}$ for the third and an initial
floor of $10^{-8}$; they add no flux limiter. In a Mach 10 bubble collapse the limiter fires
in at most 0.04 % of the cells with their base scheme and in more than 1 % with WENO-JS5
(§4.8, Fig. 16(b)).

[Yan, Abgrall & Wu (2024)](/sources/yan-2024.md) (§2.3, §3.3, App. A) prove
bound preservation of the cell averages for the Kapila model with
ideal-gas phases, without the tolerance band of Wong et al.:

1. **Volume fraction** (Thm 2.7; 2D Thm 3.6). If $\phi_1\in[0,1]$ at the Gauss
   and Gauss–Lobatto points of every cell, then $\bar\phi_1^{n+1}\in[0,1]$ under
   a CFL condition $\Delta t/\Delta x\le1/(\mathcal A_1+\mathcal A_2)$ in which
   $\mathcal A_1$ comes from the interior source and $\mathcal A_2$ from the HLL
   speeds and the weighted velocity jumps divided by the first Gauss–Lobatto
   weight (page-local $\mathcal A_1$, $\mathcal A_2$; Eqs. (2.31)–(2.32)). The
   lower bound follows from a convex splitting; the upper bound from the
   same argument applied to $\phi_2$, possible because of the symmetric form
   of the two updates.
2. **Partial densities and internal energy** (Thm 2.12; 2D Thm 3.10). With the
   [geometric quasilinearization](/methods/geometric-quasilinearization.md)
   of the admissible set, $\phi_k\rho_k\ge0$, $\rho e>0$, $0\le\phi_1\le1$
   (Lemma 2.10, with free velocity $v_*$ and constraint normal
   $(\tfrac12v_*^2,\tfrac12v_*^2,-v_*,1,0)$ in the ordering
   $(\phi_1\rho_1,\phi_2\rho_2,\rho v,E,\phi_1)$), and flux inequalities for the
   HLL speeds (Lemma 2.11), the cell averages stay admissible under the
   minimum of the volume-fraction condition and the usual condition
   $\Delta t\max(s^+-s^-)/\Delta x\le\varpi$, $\varpi$ the first Gauss–Lobatto weight
   (Eq. (2.37)).
3. **Limiter.** A two-step [Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md)
   (volume fraction and partial densities, then internal energy, floors
   $10^{-13}$) on the Gauss and Gauss–Lobatto points enforces the point-value
   hypotheses and keeps the interface equilibrium (Thms 2.13–2.14).

The CFL number $1/(2N+1)$ is used in all tests, and the volume-fraction
term $\mathcal A_1$ is reported much smaller than $\mathcal A_2$ (Figs. 9, 21).
Without the limiter a double rarefaction and a jet "can terminate" on a
negative density or pressure (stated; no figure).

MFC takes a weaker route: volume fractions are clipped to $[0,1]$ and
renormalized to sum to one only when mixture properties are computed,
so the stored state and mass conservation are untouched, and an
optional limiter blends the WENO flux with a first-order flux according
to a ratio of consecutive volume-fraction differences (minmod, MC,
superbee, van Leer and others), because "the WENO schemes we utilize
are, in general, not TVD" (Bryngelson et al. §4.2, Eqs. 33–34; see
[hybrid central-WENO schemes](/methods/hybrid-weno.md)). Neither device
is a positivity guarantee.

## The parent seven-equation model

[Paula et al. (2023)](/sources/paula-2023.md) (§2.1, Eqs. (1)–(5)) use the
non-equilibrium Baer–Nunziato model, of which the five- and six-equation
models are reductions: each phase has its own volume-fraction, mass,
momentum and energy equations, coupled by non-conservative terms in an
interface pressure and velocity. With two phases it is the
seven-equation model. They name the Kapila, Allaire and six-equation
models only in passing. The [discrete equations method](/methods/discrete-equations-method.md)
obtains the interface pressure and velocity from Riemann solutions, and
the authors use no relaxation (§7.4.1).

## Objections from fully conservative and sharp-interface sources

[Nguyen et al. (2022)](/sources/nguyen-2022.md) §1 classify
interface-capturing approaches into non-conservative
pressure-equation formulations, quasi-conservative schemes that advect
$1/(\gamma-1)$, ghost-fluid methods with a level set, and diffuse-interface
models (the seven-equation Baer–Nunziato model and its six-, five- and
three-equation reductions, possibly sharpened by level set, VOF or
THINC). They raise two objections to the five-equation family and one
to the quasi-conservative alternative:

1. it is not fully conservative and needs a mixture equation of state,
   whose temperature closure in pressure equilibrium is "questionable"
   and "can result in temperature spikes at material discontinuities";
2. the quasi-conservative $1/(\gamma-1)$ approaches are "unclear" for
   three or more fluids, because "the number of unknowns would be higher
   than the number of equations";
3. on the Martin–Moyce dam break, the five-equation results of Murrone &
   Guillard, "without special treatments for the sharp interface",
   overestimate the water level and underestimate the wavefront
   propagation, while their own pressure–temperature-equilibrium model
   stays close to the experiment (§3.5, Figs. 21–22).

Their alternative is the
[multicomponent Euler system](/definitions/multicomponent-euler-equations.md)
with phasic mass equations and pressure–temperature equilibrium. For the
dam break they state that "the same computational grid resolution was
used for the comparison", without saying whether the five-equation
results were recomputed or taken from Murrone & Guillard's paper; the
temperature-spike objection is stated, not demonstrated on any test.
[Bai & Li (2022)](/sources/bai-2022.md) §1 list five-equation models
among the diffuse-interface methods and build a sharp-interface
discontinuous Galerkin solver instead, with one equation of state per
fluid and ghost-fluid states in cut cells
([level-set and ghost-fluid methods](/methods/level-set-method.md)).

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
- Jain & Moin's "entropy preservation" is the observed approximate
  conservation of the physical phasic entropies in shock-free,
  low-Mach ($M\le0.4$) inviscid tests, not a Tadmor-type
  [entropy-conservative flux](/methods/entropy-conservative-flux.md);
  their scheme has no shock capturing and no positivity guarantee.
  They print "QS and CS stands for cubic-split and quadratic-split
  forms, respectively" (§3.5), inverted against their own definitions
  (§3.1, Eqs. 61–62), and write $e=\sum_l\rho_le_l$ (§2), whose
  dimensionally consistent form $\rho e=\sum_k\phi_k\rho_ke_k$ they use in
  Appendix B. Their discretization uses collocated point values and
  two-point arithmetic averages, i.e. a second-order central
  finite-difference-like scheme, although they call it finite-volume.

- Chamarthi (2023a) states that TENO "for the multi-component flows,
  specifically for the 5-equation model, is not presented in the open
  literature" (Ex. 4.16, arXiv v2); no other source of the bundle applies
  TENO to the five-equation model, so the bundle neither confirms nor
  contradicts the priority claim. Chamarthi's interface-thickness ranking is
  shown by plotted profiles and fields (Exs. 4.14–4.18).
- Four sources judge Wood's sound speed in opposite directions. Bryngelson et al.
  call the models without the Kapila term thermodynamically incomplete because they do
  not reproduce Wood's mixture speed, and Jain & Moin prefer the Kapila form at strong
  compression; Wakimura et al. (2024, §1) and Zhang et al. (2024a, §2.3) avoid Wood's speed
  because it is non-monotone in the volume fraction and can make computations fail. The
  first two speak of the model's physics, the last two of the speed used in the numerical
  method, so the page records a difference of priorities, not a contradiction.
- Wakimura et al.'s reason for staying at second order (spurious oscillations from
  primitive-variable reconstruction above third order) is stated without evidence and
  hedged ("may"); in the bundle, fifth-order WENO and gradient-based reconstructions of
  primitive variables run on the five-equation model without interface oscillations
  (Zhang et al. 2024a, Chamarthi 2023a, Wong et al. 2021, above).
- Zhang et al. (2024a) print the deformation tensor as
  $\tfrac12\big(\nabla\cdot v+(\nabla\cdot v)^\top\big)$ (Eq. (8)), a scalar where the
  velocity gradient is meant, and state that $\rho c^2=(p+p_\infty)/(\gamma-1)$ is limited,
  whereas their own Eq. (16) gives $\rho c^2=\gamma(p+p_\infty)$ *(compiler check, not in the
  sources: both are positive exactly when $p+p_\infty>0$, so the limiter acts the same)*.
- Wakimura et al. (received 24 February 2024, online 7 June 2024) state that "to our
  knowledge, no symmetry-preserving methods have been proposed for two-phase flow" (App. A).
  Zhang et al. (2024a) (received 7 August 2023, online 28 November 2023) call their THINC
  reconstruction on the five-equation model "symmetry-preserving" (§5), implement it so as to
  "preclude numerical asymmetry errors" (§1, §3.3) and show symmetry kept in a Mach 10
  water-cylinder test (§4.7, Fig. 13); Wakimura et al. do not cite them
  ([symmetry preservation](/properties/symmetry-preservation.md)).
- Yan, Abgrall & Wu's flux inequality (Lemma 2.11) ends with a strict
  inequality that needs $p/(\rho\sqrt{2e})$ below the Wood sound speed; the
  step is not shown. *(Compiler check, not in the sources: with ideal-gas
  phases $(p/(\rho\sqrt{2e}))^2=(\gamma-1)p/(2\rho)$ and Wood's speed is
  $c^2=p/(\rho\sum_k\phi_k/\gamma_k)$; since
  $\sum_k\phi_k/\gamma_k<\sum_k\phi_k/(\gamma_k-1)=1/(\gamma-1)$, the ratio of the two
  squares is below $\tfrac12$, so the step holds.)* Their admissibility
  results cover ideal-gas phases only, unlike the stiffened-gas setting of
  Wong et al.
- Huang & Johnsen's scheme is at best second order (MUSCL with minmod,
  midpoint face fluxes, CFL $\le0.5$; §3.4), and their argument that
  Allaire's coefficient is inconsistent concerns the incompressible
  limit, while their own runs use it.

# Citations

- [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) — §2.2, §3.1–3.2, Eqs. (1)–(14); §4.1–4.2, Eqs. (31)–(34); §4.6; §5.5 (arXiv v1).
- [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) — §2, Eqs. (1)–(12); §3.1, Eqs. (13)–(16); §3.3; §4.2, Figs. 3–4.
- [Wong et al. (2021)](/sources/wong-2021.md) — §2, Eqs. (1)–(14); §3.2–3.3, Eqs. (19)–(70); §4.1–4.2; §5; §6.2, §6.6; Appendix A (arXiv v1).
- [Jain & Moin (2022)](/sources/jain-2022.md) — §2, Eqs. (1)–(10), (16)–(21); §3.3, Lemma 3.1; §3.5, Eqs. (58)–(62); §4.1–4.2, Figs. 2–8; Appendices A–B (arXiv v1).
- [Chamarthi (2023a)](/sources/chamarthi-2023.md) — §2, Eqs. (7)–(13); §3.2–3.3, Eqs. (44)–(45), (62)–(64); Appendix A, Eqs. (91)–(95); §4, Exs. 4.14–4.18 (arXiv v2).
- [Renac (2021)](/sources/renac-2021.md) — §1.2, §7.2 (comparison only; arXiv v3).
- [Nguyen et al. (2022)](/sources/nguyen-2022.md) — §1; §3.5, Figs. 21–22 (objections and comparison only).
- [Bai & Li (2022)](/sources/bai-2022.md) — §1 (contrast only).
- [Huang & Johnsen (2023)](/sources/huang-2023.md) — §2.1–2.10, Eqs. (1)–(8), (22)–(25), Theorems 2.2–2.5; §3.1, Definition 1, Theorem A.1; §3.4; §4; §5.1–5.3, Fig. 10, Theorem 5.2.
- [Paula et al. (2023)](/sources/paula-2023.md) — §2.1, Eqs. (1)–(5); §7.4.1 (parent model only).
- [Wakimura et al. (2024)](/sources/wakimura-2024.md) — §1; §2, Eqs. (1)–(16); §3, Eq. (45); Appendices B–E: mixture-energy-consistent six-equation model with heat and mass transfer, infinite-rate relaxation in closed form.
- [Yan, Abgrall & Wu (2024)](/sources/yan-2024.md) — §1, Eqs. (1.1)–(1.4); §2.1, Eqs. (2.1)–(2.16), Remarks 2.1–2.2; §2.2, Lemma 2.5, Thms 2.3, 2.6; §2.3, Thms 2.7, 2.12–2.14, Lemmas 2.10–2.11, Eqs. (2.29)–(2.40); §3, Eqs. (3.1)–(3.35), Remarks 3.1, 3.2, 3.5; §4, Exs. 4.1–4.2, Tables 2–3, 5–6, Figs. 4, 9, 21; App. A: Kapila model with uniformly high-order bound-preserving OEDG.
- [Zhang et al. (2024a)](/sources/zhang-2024.md) — §2, Eqs. (1)–(18), Fig. 1; §3.1, Eqs. (21)–(26); §3.3, Eqs. (45)–(48), Algorithm 1; §4.1, §4.8; App. B: five-equation model with viscosity and surface tension, sound-speed choice, HLLC-consistent source terms, THINC on mass variables, interpolation limiter.
