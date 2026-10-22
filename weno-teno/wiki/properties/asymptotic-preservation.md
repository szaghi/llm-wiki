---
type: Property
title: "Asymptotic preservation"
description: "A scheme for a singularly perturbed problem is asymptotic preserving if, as the perturbation parameter vanishes, it becomes a consistent scheme for the limit problem under parameter-independent stability constraints; in this bundle a first-order semi-implicit, well-balanced finite-volume scheme is asymptotic preserving for both the parabolic and the hyperbolic relaxation limits of Euler with gravity and friction."
status: established
aliases: [AP, AP scheme, asymptotic-preserving scheme, unified asymptotic preserving scheme]
tags: [asymptotic-preserving, well-balanced, finite-volume]
timestamp: 2026-10-22T20:00:00Z
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

## Qualifications

- The AP property is shown by limit arguments on the scheme's formulas and by figures; the
  $\varepsilon$-independent stability is asserted with reference to earlier work, not
  proved or measured.
- The time step still carries a parabolic $\Delta x^2$ restriction for $\beta_{\mathrm{ms}}=1$;
  "uniform in $\varepsilon$" does not mean hyperbolic-CFL.
- The printed fully discrete scheme (Eqs. (4.17)–(4.18)) omits a factor $\Delta t$ on the
  right-hand-side terms and some powers of $\varepsilon$ found in the semi-discrete
  scheme (3.3)–(3.4); the limits (4.29)–(4.30) are unaffected *(compiler check, not in the
  sources: by eliminating the implicit momentum from (3.1)–(3.2))*.

# Citations

- [Arun et al. (2022)](/sources/arun-2022.md) — Abstract, §1, §2 (Eqs. (2.4)–(2.10), Def. 2.1), §3 (Eqs. (3.1)–(3.6), Thm. 3.2, Remark 3.1), §4 (Thm. 4.3, Remark 4.2, Eqs. (4.29)–(4.30)), §5 (Eq. (5.1), Figs. 1–2, 11–12) (arXiv v1).
- [Du & Yang (2022)](/sources/du-2022-b.md) — §3.2 (Eqs. (3.6)–(3.10)), §4.2 (Eqs. (4.3)–(4.6), Thms. 4.2–4.3), §6.1 (Eq. (6.1), Table 6.2).
