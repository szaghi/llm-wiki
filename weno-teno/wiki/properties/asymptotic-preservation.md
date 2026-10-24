---
type: Property
title: "Asymptotic preservation"
description: "A scheme for a singularly perturbed problem is asymptotic preserving if, as the perturbation parameter vanishes, it becomes a consistent scheme for the limit problem under parameter-independent stability constraints; the bundle has relaxation limits of Euler with gravity and friction and of linear partially dissipative systems, the incompressible limits of Euler and ideal MHD, and discrete kinetic schemes."
status: established
aliases: [AP, AP scheme, asymptotic-preserving scheme, unified asymptotic preserving scheme, asymptotic accuracy, AA]
tags: [asymptotic-preserving, well-balanced, finite-volume, mhd]
timestamp: 2026-10-24T06:00:00Z
---

# Asymptotic preservation

Let $P^\varepsilon$ be a singularly perturbed problem with limit $P^0$ as
$\varepsilon\to0$, and $P^\varepsilon_h$ a discretization of it ($\varepsilon$ page-local,
not the WENO regularization $\epsilon$). Following Jin, as recalled by
[Arun et al. (2022)](/sources/arun-2022.md) (§1), the scheme is **asymptotic preserving**
(AP) if

1. as $\varepsilon\to0$, $P^\varepsilon_h$ tends to $P^0_h$, a consistent discretization of
   $P^0$; and
2. its stability constraints on the mesh and time step are independent of $\varepsilon$.

An AP scheme can therefore be run with the same grid across regimes, without resolving the
small scale that $\varepsilon$ introduces.

## A unified AP scheme for two relaxation limits

Arun et al. consider the barotropic Euler equations with gravity and friction,
$p(\rho)=\rho^\gamma$, $\gamma\ge1$, given potential $\phi$ (page-local), in the
multiscale scaling of Boscarino, Pareschi and Russo: squared Mach number
$O(\varepsilon^{2\beta_{\mathrm{ms}}})$, squared Froude number and scaled friction
$O(\varepsilon^{1+\beta_{\mathrm{ms}}})$, with page-local exponent $\beta_{\mathrm{ms}}\in[0,1]$
(§2, Eqs. (2.4)–(2.6)):

$$\partial_t\rho+\partial_x(\rho v)=0,\qquad
\partial_t(\rho v)+\partial_x(\rho v^2)+\varepsilon^{-2\beta_{\mathrm{ms}}}\partial_xp(\rho)=-\varepsilon^{-(1+\beta_{\mathrm{ms}})}\big(\rho v-\rho\,\partial_x\phi\big).$$

As $\varepsilon\to0$ only the density survives (formal asymptotics, Definition 2.1):

- $\beta_{\mathrm{ms}}=1$ (hyperbolic-to-parabolic relaxation): the porous-medium equation
  $\partial_t\rho+\partial_x(\rho\,\partial_x\phi)=\partial_{xx}p(\rho)$ (Eq. (2.9));
- $\beta_{\mathrm{ms}}\in[0,1)$ (hyperbolic-to-hyperbolic relaxation): the transport
  equation $\partial_t\rho+\partial_x(\rho\,\partial_x\phi)=0$ (Eq. (2.10)).

The authors state that standard IMEX Runge–Kutta schemes "are incapable of switching
between these asymptotic regimes" (Abstract, §1, citing the unified IMEX approaches of
Boscarino–Pareschi–Russo and Albi–Dimarco–Pareschi); they do not test one.

**Time discretization** (§3, Eqs. (3.1)–(3.4)). A first-order step, implicit only in the
momentum $(\rho v)^{n+1}$ that appears in the mass flux and in the friction, explicit in
the momentum flux, pressure and gravity. Eliminating $(\rho v)^{n+1}$ gives an explicit
scheme whose mass update carries both the hyperbolic flux and second-derivative terms,
with coefficients that depend on $\varepsilon$ and $\Delta t$ through
$\varepsilon^{1+\beta_{\mathrm{ms}}}/(\varepsilon^{1+\beta_{\mathrm{ms}}}+\Delta t)$. Theorem 3.2:
this semi-discrete scheme is consistent with the scaled system away from vacuum, and as
$\varepsilon\to0$ its mass update becomes an explicit Euler step of the porous-medium
equation ($\beta_{\mathrm{ms}}=1$) or of the transport equation ($\beta_{\mathrm{ms}}<1$),
because the coefficient of the pressure term tends to $\Delta t$ or to $0$.

**Space discretization** (§4). A finite-volume scheme with a Rusanov-type flux on
hydrostatically reconstructed states, upwinded gravity sources and a central
discretization of the second-derivative terms; the same choices make it
[well-balanced](/properties/well-balancing.md) for hydrostatic states. Theorem 4.3(iii):
the fully discrete scheme is AP for both limits independently of $\beta_{\mathrm{ms}}$; the
limits are explicit first-order schemes for the porous-medium and transport equations
(Eqs. (4.29)–(4.30)). The AP property constrains the reconstruction: the E-reconstruction
in the enthalpy, which other well-balanced schemes use, gives a wrong diffusion coefficient
in the parabolic limit, so the pressure-based P-reconstruction is adopted (Remark 4.2,
citing Natalini, Ribot and Twarogowska).

**Time step** (§5, Eq. (5.1)). $\Delta t=\nu\min\big(\Delta x^2/\varepsilon^{1-\beta_{\mathrm{ms}}},\ \Delta x/\lvert\partial_x\phi\rvert\big)$
with $\nu=0.45$ in every test: for $\beta_{\mathrm{ms}}=1$ the parabolic bound $\Delta x^2$ is
independent of $\varepsilon$, for $\beta_{\mathrm{ms}}<1$ it grows as $\varepsilon\to0$. The
statement that the stability restriction "does not degenerate in the stiff limit" relies
on Boscarino, Pareschi and Russo (Remark 3.1); the paper gives no stability proof.

## Evidence

All tests are 1D and first order (§5):

- a Sod-type tube under gravity $\phi=x$ ($\rho=1$ and $0.125$, $v=0$, $t=0.2$): at
  $\varepsilon=1$ the 100-cell solution agrees with the 1000-cell one; at
  $\varepsilon=10^{-3}$ with 100 cells the density agrees with a first-order porous-medium
  solver ($\beta_{\mathrm{ms}}=1$) and with first-order upwind transport
  ($\beta_{\mathrm{ms}}=0.1$) (§5.1, Figs. 1–2; see
  [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md) — this is the barotropic
  system, with no pressure datum);
- a mesh-sensitivity test on step data, $\varepsilon=10^{-3}$, $\Delta x=10^{-2},10^{-3},10^{-4}$:
  the AP scheme gives "almost identical results", while an unspecified non-AP scheme blows
  up on the coarsest mesh in the parabolic regime and oscillates in the hyperbolic one
  (§5.3, Figs. 11–12).

## The low-Mach limit of full Euler

[Boscarino et al. (2022)](/sources/boscarino-2022.md) take $\varepsilon$ as the reference Mach
number of the scaled full Euler equations; as $\varepsilon\to0$ the thermodynamic pressure
becomes constant, the leading-order velocity divergence-free, and the limit is the
incompressible Euler system with a hydrodynamic pressure solving an elliptic equation (§2,
Eqs. (2.1)–(2.8)). Their [semi-implicit all-Mach scheme](/methods/semi-implicit-all-mach-scheme.md)
treats the acoustic pressure implicitly, so its time step is set by the material speed.

- **AP** (Thm. 4.1, §4.1). For well-prepared data (constant leading pressure,
  divergence-free leading velocity), the first-order time-semi-discrete scheme gives at leading
  order a constant pressure and $\nabla\cdot v_0^{n+1}=0$ **exactly**, a consistent
  discretization of incompressible Euler; the exactness comes from the implicit density in the
  energy flux, whereas the scheme of Cordier, Degond and Kumbaro gives a divergence
  $O(\Delta t)$ (Remark 4.2).
- **Asymptotic accuracy** (AA; Def. 4.3, Prop. 4.4). A scheme is asymptotically accurate if it
  keeps its temporal order on the limit system. A stiffly accurate type-A
  [IMEX Runge–Kutta](/methods/imex-runge-kutta.md) scheme of order $r_{\mathrm{RK}}$ is AA for
  well-prepared data: after one step the limit pressure is constant, the velocity
  divergence-free and the state equals the incompressible solution up to
  $O(\Delta t^{r_{\mathrm{RK}}+1})$. The first stage needs a nonzero diagonal coefficient, which
  rules out ARS-type tableaux (§3.2.2).

Both statements are formal (asymptotic expansion, continuous in space). The scheme is not
uniformly accurate in between: the observed order drops to 0.91 at $\varepsilon=10^{-2}$ while
it is about 4 at $\varepsilon=1$ and 5 at $\varepsilon=10^{-6}$ (Table 5.2, Fig. 5.3). On the
[Gresho vortex](/benchmarks/gresho-vortex.md) at $\varepsilon=10^{-1},10^{-2},10^{-6}$ shape and
kinetic energy are kept over two periods with a time step independent of the acoustic speed
(Ex. 5.5).

**Which flux splitting is AP.** [Allegrini & Vignal (2025)](/sources/allegrini-2025.md)
(HAL author manuscript) scale full Euler so that the pressure gradient carries
$1/\varepsilon$ and $M^2=\varepsilon/\gamma$; the formal limit is incompressible Euler with
constant thermodynamic pressure for any initial data (§1, Eqs. (1)–(3)). Asymptotic
stability requires the term $\gamma p\,\nabla\cdot v/(\gamma-1)$ of the internal-energy
equation, i.e. the enthalpy flux, to be implicit, since otherwise the pressure-wave operator
forces $\Delta t=O(\sqrt\varepsilon\,\Delta x)$ (§2.1). For a first-order IMEX step
$\frac{u^{n+1}-u^n}{\Delta t}+\nabla\cdot f_{\mathrm e}(u^n)+\nabla\cdot f_{\mathrm i}(u^{n+1})=0$
(page-local $f_{\mathrm e}$, $f_{\mathrm i}$) they ask for three properties: real eigenvalues
of both Jacobians, the explicit ones bounded in $\varepsilon$; asymptotic consistency; and
preservation of constant contacts. The
[Toro–Vázquez-Cendón splitting](/methods/flux-vector-splitting.md),
$f_{\mathrm e}=(\rho v,\ \rho v\otimes v,\ \kappa_\varepsilon v)$, $f_{\mathrm i}=(0,\ pI/\varepsilon,\ \tfrac{\gamma p}{\gamma-1}v)$
with $\kappa_\varepsilon=\varepsilon\rho\lvert v\rvert^2/2$ the scaled kinetic energy
(page-local), has all three, consistency for non-well-prepared data by citation of
Boscheri et al. (Lemma 1); putting a fraction $\beta_{\mathrm h}\in[0,1)$ of the enthalpy flux in
the explicit part gives $\nabla\cdot v^{n+1}=\frac{\beta_{\mathrm h}}{\beta_{\mathrm h}-1}\nabla\cdot v^n$
in the limit, so only the fully implicit enthalpy flux is consistent (Remark 2.2;
page-local $\beta_{\mathrm h}$). The splitting of Cordier, Degond & Kumbaro is multi-step and
consistent only up to $O(\Delta t)$, as Boscarino et al. also state, the non-conservative
splitting of Dimarco, Loubère & Vignal likewise (Lemma 2), and a Lagrange-projection-type
splitting is consistent iff the initial velocity is well prepared (Lemma 3).

Their scheme linearizes Boscheri et al.'s reformulated semi-discretization: the enthalpy and
kinetic energy in the elliptic pressure equation are taken from the explicitly convected
state, so density, pressure, momentum and energy follow in sequence from one linear elliptic
solve, without Picard iteration (§3.1, Eq. (13)). The price is consistency only for
well-prepared initial energy, $E(x,0)=E^0+\varepsilon\bar E(x)$ (Lemma 4); the variant that
restores it for general data is rejected because "oscillations appear in some test-cases"
(Remark 3.2). With a Rusanov explicit flux ("L2 AP") a linearized 1D Fourier analysis gives
stability under $\gamma\lvert v\rvert\Delta t=\Delta x$; adding implicit upwinding scaled by
$\lvert v\rvert/2+\sqrt{v^2/4+c^2/\varepsilon}$ ("L∞ AP") relaxes it to $\lvert v\rvert\Delta t=\Delta x$
but makes the consistency hold only up to $O(\Delta t)$ (Lemmas 5–6, Remark 5.2), the
Fourier analysis being completed numerically over $\sqrt\varepsilon\,v/c\in(0,25)$ and
$\gamma\in[1,10]$ or $[1,5]$. Second order uses the ARS(2,2,2)
[IMEX Runge–Kutta](/methods/imex-runge-kutta.md) scheme with MUSCL–minmod on the explicit
flux only, consistent for well-prepared energy (Lemma 8); since second-order IMEX schemes
cannot be SSP, a convex blend $\theta=\beta_{\mathrm{ARS}}/(1-\beta_{\mathrm{ARS}})$, $\beta_{\mathrm{ARS}}=1-1/\sqrt2$ the ARS(2,2,2) coefficient, of the first- and
second-order updates gives a first-order but less diffusive TVD scheme (§4.3; page-local
$\theta$, not the Zhang–Shu factor, and $\beta_{\mathrm{ARS}}$). On the [Gresho vortex](/benchmarks/gresho-vortex.md)
($80^2$, $M=10^{-1}$ to $10^{-3}$) the second-order scheme keeps the Mach-number field
independent of the reference Mach number, and on a double shear layer at $\varepsilon=10^{-3}$
and $10^{-6}$ ($128^2$) it matches the incompressible solution, with density errors
$9.18\times10^{-3}$ ($128^2$) and $5.13\times10^{-3}$ ($256^2$) at $\varepsilon=10^{-3}$,
which they call "of order $\varepsilon$" (§4.5, §4.7).

**Exact mass conservation in compatible finite elements.** [Zampa & Dumbser (2025)](/sources/zampa-2025.md)
(arXiv v1) treat weakly compressible isentropic flow in density–momentum–entropy form
with momentum in a Raviart–Thomas space and density and pressure discontinuous of the same
degree, so that the implicit density update equals the divergence of the discrete
momentum and mass is conserved cell by cell (Thm 3.1). Momentum and entropy convection are
explicit, pressure and density implicit through a Newton iteration on the equation of
state, so the CFL condition depends on the flow speed only (§3.1). **AP statement** (Thm
3.2): for constant density and $1/c^2=0$ the Newton iteration converges in one step to a
new H(div) vorticity–velocity–pressure scheme for incompressible Navier–Stokes. On a
low-Mach Taylor–Green vortex the $L^\infty$ norms of $\nabla\cdot v_h$ and of $\rho_h-1$ fall as
$M^2$ (order 2.00) down to about $M\approx10^{-6}$, where round-off ($\sim10^{-13}$) takes
over (Table 4). The entropy equation is non-conservative, and the authors restrict the
method to Mach numbers from zero to about one, not expecting correct strong shocks
(§3.2.2); its finite-element setting is peripheral to the bundle.

## The low sonic-Mach limit of ideal MHD

[Chen, Wu & Xiong (2023)](/sources/chen-2023-b.md) extend the same construction to the ideal
MHD equations scaled with Alfvén Mach number one and sonic Mach number $\varepsilon$: the
pressure enters the momentum flux as $p/\varepsilon^2$, the fast magnetosonic speed scales as
$\varepsilon^{-1}$, and an explicit scheme needs $\Delta t=O(\varepsilon\Delta x)$ (§2.2). For
well-prepared data ($p=p_0+\varepsilon^2p_2(x)+\dots$ with $p_0$ constant, divergence-free
leading velocity and magnetic field) the formal limit is incompressible MHD with
$p_2$ as the incompressible pressure (§2.3, Eqs. (2.8)–(2.14), recalled from earlier work).
Their [semi-implicit scheme](/methods/semi-implicit-all-mach-scheme.md) keeps
$\nabla\cdot B=0$ by evolving a vector potential.

- **AP** (Thm. 4.1). The first-order time-semi-discrete scheme with well-prepared data at
  $t^n$ gives $\nabla p_0^{n+1}=0$ at $O(\varepsilon^{-2})$ and, at $O(1)$,
  $\frac{p_0^{n+1}-p_0^n}{\Delta t}+\gamma p_0^n\nabla\cdot v_0^{n+1}=0$; integration over the
  domain (periodic or no-slip) gives a constant pressure and $\nabla\cdot v_0^{n+1}=0$, a
  consistent scheme for incompressible MHD. This is the argument of Boscarino et al. above,
  with the magnetic terms carried along.
- **Asymptotic accuracy** (Thm. 4.2). An order-$r_{\mathrm{RK}}$ semi-implicit IMEX Runge–Kutta
  scheme with stiffly accurate implicit part keeps, for $\varepsilon\to0$, a constant pressure,
  $\nabla\cdot v\to0$, $\nabla\cdot B=0$ and the incompressible solution up to
  $O(\Delta t^{r_{\mathrm{RK}}+1})$ after one step; proof by induction over the stages.

Both are formal and space-continuous; no stability proof is given, and the
$\varepsilon$-independent time step is shown numerically. The accuracy tests (third-order scheme)
give about fifth order in space at $\varepsilon=1$, $10^{-6}$ and $0$, and lose order at
$\varepsilon=10^{-2}$: 1D orders 2.78, 1.11, 1.72, 1.60 (Table 5.2), and in 2D errors that do not
decrease between $N=16$ and $N=64$ (Table 5.4). The authors call this "typical behavior of
high-order IMEX schemes for these multi-scale problems". A magnetized
[Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md) run at $\varepsilon=10^{-6}$ is
compared qualitatively with earlier results (Ex. 5.9).

## Hydrodynamic limit of discrete kinetic schemes

For a discrete BGK (Jin–Xin) relaxation system with relaxation time $\varepsilon$, the limit is
the conservation law itself, $\mathsf f=\mathbb M(u)+O(\varepsilon)$ (page-local kinetic unknown
and Maxwellian). [Abgrall & Nassajian Mojarrad (2024)](/sources/abgrall-2024.md) define AP "in
the sense of Jin" as stability and accuracy uniform in $\varepsilon$ (§1) and show for their
explicit [deferred-correction](/methods/deferred-correction.md)
[kinetic scheme](/methods/discrete-kinetic-relaxation-scheme.md) that the iteration contracts
with a constant independent of $\varepsilon$ (Prop. 1) and that, up to $O(\varepsilon)$, the
conserved update is a DeC discretization of the limit conservation law (Prop. 2). The
relaxation source is implicit in form but computed explicitly, because the projection onto the
conserved variables annihilates it. The tests do not state the value of $\varepsilon$.

## Diffusive relaxation of a linear partially dissipative system

[Crin-Barat & Manea (2026)](/sources/crinbarat-2026.md) (arXiv v2 read) prove
asymptotic properties for the simplest semi-discretization of a linear
system $\partial_tu+A\,\partial_xu=-\mathsf Bu$ on the whole line, with $A$
symmetric and the damping matrix $\mathsf B=\mathrm{diag}(0,\tilde{\mathsf B})$
acting only on a block of the unknowns through a positive definite
$\tilde{\mathsf B}$ (page-local $\mathsf B$, $\tilde{\mathsf B}$; §1.1). The
discretization is the second-order central difference
$\delta_hu_i=(u_{i+1}-u_{i-1})/(2\Delta x)$ (page-local) on an infinite uniform
grid, with time left continuous. Among the three two-point differences it is
the only one stable for every symmetric $A$, and it satisfies the
summation-by-parts identity $\langle u,\delta_hv\rangle=-\langle\delta_hu,v\rangle$
in $\ell^2$, the only structure the first proof uses (Props 3.4–3.5;
[summation-by-parts operators](/operators/summation-by-parts-operator.md)).
"Asymptotic preserving" is used in two senses, which must be kept apart:

1. **Large-time decay, uniformly in $\Delta x$** (Thm 2.1). Under the Kalman rank
   condition on $(A,\mathsf B)$, the semi-discrete solution satisfies
   $\lVert u_2(t)\rVert+\lVert\delta_hu(t)\rVert\le C(1+t)^{-1/2}\lVert u_0\rVert_{h^1}$
   with $C$ independent of $\Delta x$, $t$ and $u_0$ ($u_2$ the damped block,
   $h^1$ a discrete Sobolev norm), the discrete counterpart of the continuous
   hypocoercive decay; proof by a time-weighted Lyapunov functional with a
   Beauchard–Zuazua corrector (§4).
2. **Diffusive relaxation limit, uniformly in $\Delta x$** (Thm 2.6, Cor. 2.7).
   For the damped linearized Euler system in diffusive scaling,
   $\partial_t\rho^\varepsilon+\delta_hv^\varepsilon=0$,
   $\varepsilon^2\partial_tv^\varepsilon+\delta_h\rho^\varepsilon+v^\varepsilon=0$, the
   solution converges to the discrete heat equation
   $\partial_t\rho-\delta_h^2\rho=0$ with the discrete Darcy law $v=-\delta_h\rho$ at
   rate $O(\varepsilon^2)$ in discrete Besov, Sobolev and maximum norms, with
   constants independent of $\Delta x$, $\varepsilon$ and $T$. The tool is a
   discrete Littlewood–Paley decomposition whose dyadic bands are defined by
   the symbol $\sin(\vartheta)/\Delta x$ of $\delta_h$ ($\vartheta$ the reduced
   wavenumber, registry §9) rather than by $\lvert k_w\rvert$, which gives
   Bernstein estimates uniform in $\Delta x$ (Prop. 3.8), with low and high
   frequencies split at $\kappa_{\mathrm s}/\varepsilon$ (page-local small
   constant $\kappa_{\mathrm s}$; §1.3, §3.5).

The second sense is closer to Jin's definition above, but it concerns the
space semi-discretization only: with continuous time there is no time-step
constraint to be independent of $\varepsilon$. The authors contrast their
frequency-based route with IMEX Runge–Kutta AP schemes (§2.2.2). Numerically
(Python), the decay is "exactly $(1+t)^{-1/2}$" at $\Delta x=2^{-4}$ (Fig. 3), the
relaxation error falls as $O(\varepsilon^2)$ (Fig. 5), and at $\varepsilon=2^{-5}$,
$T=5$ the maximum error of $\rho^\varepsilon-\rho$ is $1.3758\times10^{-5}$,
$1.3761\times10^{-5}$, $1.3763\times10^{-5}$ for $\Delta x=2^{-4},2^{-5},2^{-6}$, i.e.
uniform in $\Delta x$ (Fig. 6 table; §7). The time integrator and the domain
truncation of the experiments are not stated. A discrete Jin–Xin relaxation
and general partially dissipative systems are sketched as extensions,
without proof (§8; [discrete kinetic relaxation](/methods/discrete-kinetic-relaxation-scheme.md)).

## Stiff sources without an AP claim

Stiffness alone does not make a scheme asymptotic preserving in the sense above, which
needs a limit problem. [Du & Yang (2022)](/sources/du-2022-b.md) treat stiff finite-rate
chemistry in multicomponent reacting Navier–Stokes with a third-order conservative modified
exponential Runge–Kutta (CMERK) method of their own earlier work: an artificial linear damping
$\mu u$ (page-local rate $\mu$) is added to and subtracted from the source, the stages carry
exponential factors $e^{\beta_{10}\mu\Delta t}$, $e^{\mathsf c_{\mathrm E}\mu\Delta t}$ (page-local
Shu–Osher-form coefficients $\alpha_{jl}$, $\beta_{jl}$ and their combination
$\mathsf c_{\mathrm E}=\beta_{20}+\alpha_{21}\beta_{10}+\beta_{21}$, Eq. (3.7); not the weights $\alpha_k$ or
the indicators $\beta_k$), and each stage of the cell-average update is a convex combination of a
convective forward-Euler state and a source state $\bar s/\mu+\bar u$ (§3.2, Eqs. (3.6)–(3.10);
§4.2, Eqs. (4.3)–(4.6)). Bound preservation then holds under a convective CFL condition with
factor $\min\alpha_{jl}/\beta_{jl}$ and a lower bound on $\mu$ set by the source
(Thms. 4.2–4.3). On a 1D accuracy test with artificial sources $\mp c\,(\rho Y_1)^7$ in the two
species equations and $c=10^6$, CMERK
with the step of Eq. (6.1) converges at third order ($L^2$ error $1.28\times10^{-8}$ at
$N=640$, order 2.96), while three-stage [SSP Runge–Kutta](/methods/ssp-runge-kutta.md) with the
same step returns NaN on $N=10,20$ and runs with $\tfrac25\Delta t$ (Table 6.2). No limit
equation and no $c$-uniform stability statement are given, and the paper does not use the term
asymptotic preserving.

In resistive relativistic MHD, [Mignone et al. (2024)](/sources/mignone-2024.md)
integrate the stiff Ohm's-law source, proportional to the inverse
resistivity, with [IMEX Runge–Kutta](/methods/imex-runge-kutta.md) schemes on
point values (§3.2–3.4). Their implicit update starts the Newton–Broyden
iteration from the ideal-MHD solution when the stage-scaled resistivity is
below one (§3.4), but the paper states no limit scheme and makes no AP claim;
its evidence on the stiff regime is that the fourth-order ARK4 becomes
unstable at small resistivity (below $10^{-4}$ on a charged vortex, failing at
$10^{-6}$ on a rotor) while the third-order SSP3(4,3,3) runs (§4.2–4.3, §5;
[relativistic hydrodynamics and MHD](/definitions/relativistic-hydrodynamics.md)).

In relativistic radiation MHD, [López-Miralles et al. (2023)](/sources/lopezmiralles-2023.md)
meet the optically thick (diffusion) regime of the radiation moments: on a diffusing
radiation pulse with cell optical depths 5, 100 and 1000, first-order reconstruction, an
unscaled flux or radiative HLL without speed limiting give "catastrophic diffusive solutions", especially above optical
depth 100 (described, not plotted). Their radiative HLL limits the radiation
wave speeds by the optical depth, and their
[PVM flux](/methods/polynomial-viscosity-matrix-solver.md) scales its viscosity by the inverse
optical depth (§3.2, §4.1.4), a choice they call "somehow arbitrary"; the paper states no limit scheme and
does not use the term asymptotic preserving. Their stiff radiation–matter coupling is
integrated with an [IMEX](/methods/imex-runge-kutta.md) extension of third-order Runge–Kutta
(§3.1, §3.3).

## Qualifications

- The AP property is shown by limit arguments on the scheme's formulas and by figures; the
  $\varepsilon$-independent stability is asserted with reference to earlier work, not
  proved or measured.
- For four of the nonlinear cases the evidence is of the same kind: formal limits of the
  time-semi-discrete or fully discrete formulas (Arun et al., Thm. 3.2 and 4.3; Boscarino et
  al., Thm. 4.1 and Prop. 4.4; Chen, Wu & Xiong, Thms. 4.1–4.2; Abgrall & Nassajian Mojarrad,
  Prop. 2), with tests at one or a few fixed values of the small parameter; none measures
  stability uniformly in it. Crin-Barat & Manea's case is different in kind: rigorous
  estimates uniform in $\Delta x$ and $\varepsilon$, but for a linear constant-coefficient system,
  a central semi-discretization without shock capturing and no time discretization.
- Crin-Barat & Manea call $\delta_h$ a "first-order" operator in the sense of a
  first-derivative approximation (§3.2, §8); it is second-order accurate *(compiler check,
  not in the sources)*. The Jin–Xin approximation they recall for the extension (Eq. (8.4), §8.2) prints
  $\varepsilon^2(\partial_tv^\varepsilon+\partial_x\rho^\varepsilon)=v^\varepsilon-f(\rho^\varepsilon)$, with which
  $v-f(\rho)$ grows like $e^{t/\varepsilon^2}$; relaxation of $v$ towards $f(\rho)$ needs
  $f(\rho^\varepsilon)-v^\varepsilon$ on the right *(compiler check, not in the sources)*. Their
  Prop. 3.4 proof bounds the exponential of the $A$ part alone, while $A$ and $\mathsf B$ need
  not commute; the result follows from an energy estimate since $-\mathsf B$ is
  non-positive *(compiler check, not in the sources)*.
- Allegrini & Vignal's stability lemmas (5–7) are linear, 1D and completed numerically,
  with a maximal root modulus of 1; their closing step asserts a matrix norm with
  $\lVert\mathcal G\rVert\le r(\mathcal G)$ for the amplification matrix $\mathcal G$ (registry §10; the source's $B$),
  $r$ the spectral radius. That holds only under extra conditions
  (e.g. the eigenvalues of modulus $r(\mathcal G)$ semisimple): for $\mathcal G=\begin{pmatrix}1&1\\0&1\end{pmatrix}$,
  $r(\mathcal G)=1$ but $\lVert\mathcal G^n\rVert$ grows like $n$, so no norm gives $\lVert\mathcal G\rVert\le1$
  *(compiler check, not in the sources)*. The printed argument therefore completes the
  lemmas only if the eigenvalues of modulus one are semisimple, which the paper does not
  examine. Their second-order scheme uses ARS(2,2,2), the kind of tableau
  Boscarino et al. exclude from asymptotic **accuracy** (above); Allegrini & Vignal prove
  asymptotic **consistency** only (Lemma 8), so the two statements do not conflict.
- Zampa & Dumbser's AP theorem covers constant density only; their low-Mach
  Kelvin–Helmholtz test is outside it (§4). Their Thm 3.1 prints the cell mass balance with
  $+\Delta t\int_{\partial T}m_h\cdot n$, whereas the density update they state,
  $\rho_h^{n+1}=\rho_h^n-\Delta t\,\nabla\cdot m_h^{n+1}$, gives a minus sign by the divergence
  theorem *(compiler check, not in the sources)*.
- Arun et al.'s time step still carries a parabolic $\Delta x^2$ restriction for $\beta_{\mathrm{ms}}=1$;
  "uniform in $\varepsilon$" does not mean hyperbolic-CFL.
- Arun et al.'s printed fully discrete scheme (Eqs. (4.17)–(4.18)) omits a factor $\Delta t$ on the
  right-hand-side terms and some powers of $\varepsilon$ found in the semi-discrete
  scheme (3.3)–(3.4); the limits (4.29)–(4.30) are unaffected *(compiler check, not in the
  sources: by eliminating the implicit momentum from (3.1)–(3.2))*.

# Citations

- [Arun et al. (2022)](/sources/arun-2022.md) — Abstract, §1, §2 (Eqs. (2.4)–(2.10), Def. 2.1), §3 (Eqs. (3.1)–(3.6), Thm. 3.2, Remark 3.1), §4 (Thm. 4.3, Remark 4.2, Eqs. (4.29)–(4.30)), §5 (Eq. (5.1), Figs. 1–2, 11–12) (arXiv v1).
- [Du & Yang (2022)](/sources/du-2022-b.md) — §3.2 (Eqs. (3.6)–(3.10)), §4.2 (Eqs. (4.3)–(4.6), Thms. 4.2–4.3), §6.1 (Eq. (6.1), Table 6.2).
- [Boscarino et al. (2022)](/sources/boscarino-2022.md) — §2 (Eqs. (2.1)–(2.9)), §3.2.2, §4 (Thm. 4.1, Remark 4.2, Def. 4.3, Prop. 4.4), §5 (Table 5.2, Fig. 5.3, Ex. 5.5) (arXiv v2).
- [Abgrall & Nassajian Mojarrad (2024)](/sources/abgrall-2024.md) — §1, §2.2 (Props. 1–2), §5.
- [Chen, Wu & Xiong (2023)](/sources/chen-2023-b.md) — §2.2–2.3 (Eqs. (2.6)–(2.14)), §4 (Thms. 4.1–4.2), §5 (Tables 5.2, 5.4, Ex. 5.9) (arXiv v1).
- [López-Miralles et al. (2023)](/sources/lopezmiralles-2023.md) — §3.1–3.3, §4.1.4, §5 (arXiv v1).
- [Crin-Barat & Manea (2026)](/sources/crinbarat-2026.md) — arXiv v2: §1.1–1.3; §2.1–2.2 (Thms 2.1, 2.3, 2.6, Cor. 2.7); §3.2–3.5 (Props 3.4, 3.5, 3.8); §4; §7 (Figs. 3, 5, 6); §8 (Eq. (8.4)).
- [Mignone et al. (2024)](/sources/mignone-2024.md) — §3.2–3.4; §4.2–4.3; §5.
- [Allegrini & Vignal (2025)](/sources/allegrini-2025.md) — HAL v1: §1, Eqs. (1)–(4); §2.1–2.2, Eqs. (6)–(11), Lemmas 1–3, Remarks 2.1–2.2; §3.1–3.3, Eqs. (13)–(23), Lemmas 4–7, Remarks 3.2, 5.1–5.2; §4.1–4.3, Eqs. (24)–(28), Lemma 8; §4.5, §4.7, Figs. 13–16.
- [Zampa & Dumbser (2025)](/sources/zampa-2025.md) — arXiv v1: §1; §2.2; §3.1; §3.2.2; Thms 3.1–3.2; §4.4; §4.5, Table 4.

