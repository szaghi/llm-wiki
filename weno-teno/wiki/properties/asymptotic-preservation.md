---
type: Property
title: "Asymptotic preservation"
description: "A scheme for a singularly perturbed problem is asymptotic preserving if, as the perturbation parameter vanishes, it becomes a consistent scheme for the limit problem under parameter-independent stability constraints; the bundle has four cases: relaxation limits of Euler with gravity and friction, the incompressible limits of full Euler and of ideal MHD, and the hydrodynamic limit of discrete kinetic schemes."
status: established
aliases: [AP, AP scheme, asymptotic-preserving scheme, unified asymptotic preserving scheme, asymptotic accuracy, AA]
tags: [asymptotic-preserving, well-balanced, finite-volume, mhd]
timestamp: 2026-10-22T19:46:00Z
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

## Stiff sources without an AP claim

Stiffness alone does not make a scheme asymptotic preserving in the sense above, which
needs a limit problem. [Du & Yang (2022)](/sources/du-2022-b.md) treat stiff finite-rate
chemistry in multicomponent reacting Navier–Stokes with a third-order conservative modified
exponential Runge–Kutta (CMERK) method of their own earlier work: an artificial linear damping
$\mu u$ (page-local rate $\mu$) is added to and subtracted from the source, the stages carry
exponential factors $e^{\beta_{10}\mu\Delta t}$, $e^{\mathsf A\mu\Delta t}$ (page-local
Shu–Osher-form coefficients $\alpha_{jl}$, $\beta_{jl}$ and their combination
$\mathsf A=\beta_{20}+\alpha_{21}\beta_{10}+\beta_{21}$, Eq. (3.7); not the weights $\alpha_k$ or
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
- Across the four cases the evidence is of the same kind: formal limits of the
  time-semi-discrete or fully discrete formulas (Arun et al., Thm. 3.2 and 4.3; Boscarino et
  al., Thm. 4.1 and Prop. 4.4; Chen, Wu & Xiong, Thms. 4.1–4.2; Abgrall & Nassajian Mojarrad,
  Prop. 2), with tests at one or a few fixed values of the small parameter; none measures
  stability uniformly in it.
- The time step still carries a parabolic $\Delta x^2$ restriction for $\beta_{\mathrm{ms}}=1$;
  "uniform in $\varepsilon$" does not mean hyperbolic-CFL.
- The printed fully discrete scheme (Eqs. (4.17)–(4.18)) omits a factor $\Delta t$ on the
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
