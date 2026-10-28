---
type: Method
title: "Wilcox k-ω model"
description: "Wilcox's two-equation k-ω eddy-viscosity model and its unblended variants (1998, 2006, Kok's TNT, low-Reynolds damping), with constants, the near-wall singularity of ω and its regularized and k-τ remedies, the log-ω form, and the obstacles of solving it with high-order element discretizations."
status: established
aliases: [k-omega model, Wilcox k-ω, Wilcox 1998, Wilcox 2006, Wilcox 07, k-ω 2006, TNT, turbulent/non-turbulent k-ω, k-log-ω, k-ln ω]
tags: [rans, eddy-viscosity, dg, boundary-layer]
timestamp: 2026-10-27T21:07:00Z
---

# Wilcox k-ω model

The $k$-$\omega$ model of Wilcox is a two-equation RANS closure that
transports the turbulent kinetic energy $k$ and the specific dissipation
rate $\omega$ and sets a [Boussinesq](/definitions/boussinesq-hypothesis.md)
eddy viscosity $\nu_t=k/\omega$, with no blending between inner and outer
constant sets. Menter's [$k$-$\omega$ SST](/methods/k-omega-sst-model.md) and
BSL models blend it near the wall with a $k$-$\varepsilon$-equivalent outer
branch; this page holds the unblended forms. Two sources solve it with
high-order element methods: Elzaabalawy et al. (2023) with a hybridizable
discontinuous Galerkin (HDG) method, for the Wilcox (1998), Kok TNT, BSL and
SST variants, and Ghidoni et al. (2026) with a modal DG method for the
Wilcox (2006) model in log-$\omega$ form
([Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md), §3;
[Ghidoni et al. (2026)](/sources/ghidoni-2026.md), §2).

## Equations

Elzaabalawy et al. (2023, §3.1, Eqs. 38–39, 44) write one steady,
incompressible, kinematic form for all their variants; with the mean
velocity $\langle u_j\rangle$ and the mean strain magnitude
$\lvert S\rvert$ (their $P=2S_{ij}S_{ij}=\lvert S\rvert^2$):

$$\begin{aligned}
\partial_j\big(k\langle u_j\rangle\big)&=\nu_t\lvert S\rvert^2-\beta^*\omega k+\partial_j\big[(\nu+\sigma_k\nu_t)\partial_jk\big],\\
\partial_j\big(\omega\langle u_j\rangle\big)&=\alpha\lvert S\rvert^2-\beta\omega^2+\partial_j\big[(\nu+\sigma_\omega\nu_t)\partial_j\omega\big]+\frac{\sigma_d}{\omega}\,\partial_jk\,\partial_j\omega,
\end{aligned}$$

with $\nu_t=k/\omega$ (all variants but SST). The production coefficient
$\alpha$ is the source's $\zeta$ and the cross-diffusion coefficient
$\sigma_d$ (page-local name) its $F_\omega$. The production is limited for all
variants as $\min(\nu_t\lvert S\rvert^2,15\beta^*\omega k)$; the authors take 15
rather than Menter's 10 "because the lower value activates the limiter in
boundary-layer regions", noting that Menter used 20 and later 10 (§3.1.1,
Eq. 55). Boundary conditions: $k=0$ at the wall, $\omega\propto y^{-2}\to\infty$
there, inlet values of $k$ and $\omega$, zero normal fluxes elsewhere
(Eqs. 40–43).

Ghidoni et al. (2026, §2, Eq. 1) print the compressible Wilcox (2006)
model ("Wilcox 07") with $\tilde\omega_\ell=\ln\omega$ as unknown (page-local
symbol; the tilde of the source is not a Favre filter), so the $\omega$
equation divided by $\omega$ gains the term
$(\mu+\sigma_\omega\mu_t)\lvert\nabla\tilde\omega_\ell\rvert^2$, and the
cross diffusion reads $\sigma_d\rho\,e^{-\tilde\omega_\ell}\max(\nabla k\cdot\nabla\tilde\omega_\ell,0)$.
Two limiters enter the eddy viscosity and the sources:
$\mu_t=\alpha^*\rho\bar k\,e^{-\tilde\omega_{\ell,r}}$ with $\bar k=\max(0,k)$
and $\tilde\omega_{\ell,r}=\max(\tilde\omega_\ell,\tilde\omega_{\ell,r0})$, a
"realizability" floor; no stress limiter is printed. Dividing the
$\omega$ equation above by $\omega$ reproduces the printed cross-diffusion
term, $e^{-\tilde\omega_\ell}\nabla k\cdot\nabla\tilde\omega_\ell=\omega^{-2}\nabla k\cdot\nabla\omega$,
and the gradient-squared term *(compiler check, not in the sources)*.

### Constants

| variant | $\sigma_k$ | $\sigma_\omega$ | $\beta^*$ | $\beta$ | $\alpha$ | $\sigma_d$ | source |
|---|---|---|---|---|---|---|---|
| Wilcox (1998) | 0.5 | 0.5 | 0.09 | 0.072 | 13/25 | 0 | Elzaabalawy et al. (2023), §3.1 |
| Kok TNT | 2/3 | 0.5 | 0.09 | 0.075 | $\beta/\beta^*-\sigma_\omega\kappa^2/\sqrt{\beta^*}$, $\kappa=0.41$ | 0 if $\nabla k\cdot\nabla\omega<0$, 0.5 if $>0$ | Elzaabalawy et al. (2023), §3.1 |
| Wilcox (2006) | 3/5 | 1/2 | 9/100 | 0.0708 | 13/25 | 1/8 (with $\max(\cdot,0)$) | Ghidoni et al. (2026), §2 |
| Wilcox (2006) | 0.6 | 0.5 | 0.09 | 0.0708 | 0.52 | 1/8 (with $\max(\cdot,0)$) | Tomboulides et al. (2025), §2 |
| inner (Wilcox) set of BSL | 0.5 | 0.5 | 0.09 | 0.075 | 0.553 | blended cross diffusion, $2(1-F_1)\sigma_{\omega2}$ | Wu et al. (2023), §2.1.1, Table 1 |

Ghidoni et al. also print $\alpha^*=1$, so $\mu_t=\rho\bar k/\omega$ (§2).
Tomboulides et al. (2025) print the same Wilcox (2006) set in the divisor
convention, diffusivities $\mu+\mu_t/\sigma_k$ and $\mu+\mu_t/\sigma_\omega$
with $\sigma_k=1/0.6$ and $\sigma_\omega=2.0$, which are the multipliers
0.6 and 0.5 of the table; their cross diffusion
$\rho(\sigma_d/\omega)\max(\nabla k\cdot\nabla\omega,0)$ with $\sigma_d=1/8$
is the Ghidoni et al. term written in $\omega$, and they recall that it
removes the free-stream dependence of $\omega$ first recognized by Menter
([Tomboulides et al. (2025)](/sources/tomboulides-2025.md), §2, Eqs. 5–11).
The two sources agree on every constant once the convention is translated
*(compiler check, not in the sources)*.
BSL and SST, the blended members of the family, are on the
[SST page](/methods/k-omega-sst-model.md); in Elzaabalawy et al.'s notation
their cross diffusion is $\sigma_d=2\sigma_{\omega2}(1-F_1)$ (§3.2).
Wu et al. (2023) state that set 1 of the BSL blend is the Wilcox
$k$-$\omega$ model and set 2 the $k$-$\varepsilon$ model, and tabulate the
inner set as in the last row; the TNT expression of the table
(Elzaabalawy et al.) gives $\alpha=0.5532$ for $\beta=0.075$,
$\beta^*=0.09$, $\sigma_\omega=0.5$, $\kappa=0.41$, against the 0.553 Wu et
al. print, and their $\sigma_k=0.5$ equals the Wilcox (1998) value of the
table *(compiler check, not in the sources)* ([Wu et al. (2023)](/sources/wu-2023-b.md), §2.1.1,
Eq. 3, Table 1; they use BSL as the host of a hybrid, see the
[SST page](/methods/k-omega-sst-model.md)).

The TNT expression for $\alpha$ is the log-layer condition. It gives
$\alpha=0.5532$ for TNT; with the Wilcox (1998) constants and $\kappa=0.41$
it gives 0.520, matching 13/25, and with the Wilcox (2006) constants it
gives 0.520 for $\kappa=0.40$ but 0.507 for $\kappa=0.41$ *(compiler check,
not in the sources)*.

**A form with $\omega=\varepsilon/k$.** Heinz (2020) writes a $k$-$\omega$
model whose frequency is $1/\tau=\varepsilon/k$, without the $\beta^*$ of the
registry's $\omega$, so that $\nu_t=C_\mu k/(\varepsilon/k)$; in that variable
the $\omega$ equation is a production–destruction balance with coefficient
$C_{\omega1}$ and destruction ratio $\alpha_\omega=C_{\omega2}/(C_\mu C_{\omega1})$
(registry §11; the source's $\beta$, $\approx1.63$), plus an
optional cross diffusion
$C_\omega k^{-1}(\nu+\nu_t)\partial_jk\,\partial_j(\varepsilon/k)$ that "acts
like a damping function" ([Heinz (2020)](/sources/heinz-2020.md), §2.3,
Eq. 11; $C_{\omega1}$, $C_{\omega2}$, $C_\omega$ the source's names). The
constants, attributed to Bredberg et al., are
$(C_{\omega1},C_{\omega2},C_\mu,C_\omega,\sigma_\omega)=(0.49,0.072,0.09,1.1,1.8)$,
with $\sigma_\omega$ a divisor of $\nu_t$. Heinz's log-law condition is

$$\kappa^2=C_\mu^{1/2}\sigma_\omega\Big(\frac{C_{\omega2}}{C_\mu}-C_{\omega1}\Big),$$

which gives $\kappa=0.41$, against $0.43$ for the standard
[$k$-$\varepsilon$](/methods/k-epsilon-model.md) constants (§2.3). Rewritten
in the registry's $\omega=\varepsilon/(\beta^*k)$ with $\beta^*=C_\mu$, the
model is a Wilcox-type equation with $\alpha=C_{\omega1}=0.49$,
$\beta=C_{\omega2}=0.072$ and multiplier $1/1.8=0.556$ on $\nu_t$ in the
$\omega$ diffusion, and the condition above is the TNT log-layer expression
of the table (Elzaabalawy et al.'s form of the equations above) solved for
$\kappa$; its value is $0.1674$, $\kappa=0.409$
*(compiler check, not in the sources)*. Heinz also records that transforming
the $k$-$\varepsilon$ model into this variable gives $C_{\omega1}=C_{\varepsilon1}-1$
and $C_{\omega2}/C_\mu=C_{\varepsilon2}-1$ (§2.3), and builds on the same
form the resolution-dependent destruction ratio
$\alpha^*_\omega=1+L_+^2(\alpha_\omega-1)$ of
[continuous eddy simulation](/methods/continuous-eddy-simulation.md)
(§4.3, Eqs. 47–51).

### Near-wall behaviour of $\omega$ and $k$

As $y\to0$, $\omega\to6\nu/(\beta y^2)$, valid for $y^+<3$, and $1/\omega$
is therefore quadratic in the wall distance (Elzaabalawy et al. 2023,
§3.1.1–3.1.2, Eq. 57). The matching viscous-sublayer law for $k$ is
$k^+=C_k(y^+)^{p_k}$ with $p_k=\tfrac12+\sqrt{\tfrac14+6\beta^*/\beta}$ and $C_k$
between 0.0025 and 0.0032 depending on the variant, as the authors cite
it (Eq. 58;
page-local $C_k$, $p_k$). With $\beta=0.075$ this exponent is 3.23, the
value in the SST wall functions that Mozaffari et al. (2024) print on the
[SST page](/methods/k-omega-sst-model.md), and 3.28 with the Wilcox (1998)
$\beta=0.072$ *(compiler check, not in the sources)*.

For a wall-resolved DG solution Ghidoni et al. (2026, §2, Eq. 4) set the
wall value from an effective distance that shrinks with the polynomial
degree $N$,

$$\tilde\omega_{\ell,w}=\ln\frac{6\nu_w}{\beta\,(a_Ny_1)^2},\qquad a_N=\exp\Big(-\sum_{n=1}^{N}\frac1n\Big),$$

with $y_1$ the height of the first element (page-local $a_N$), and
$k_w=0$, an adiabatic no-slip wall. They state that a DG solver needs the
first element at $y_1^+\sim10$ for an accurate wall-resolved solution,
against $y_1^+\sim1$ for finite volumes (§1). Their explicit
[wall function](/methods/rans-wall-function.md) for this model, which is assessed up to $y_1^+=320$, is on
that page; on the zero-pressure-gradient plate the error of $C_f$ at
$x/L=0.923$ against their $y_1^+=1$, $\mathbb P^6$ solution without wall
function stays below 2.3% from $\mathbb P^2$ to $\mathbb P^6$ at $y_1^+=320$
(Table 1).

### The wall singularity and its remedies

Tomboulides et al. (2025, §1) state the singularity as the reason the
$k$-$\omega$ model is awkward in high-order codes: near the wall
$\omega\sim y^{-2}$, so $\omega$ and its gradient are singular there;
prescribing an arbitrarily large wall value is satisfactory for
finite-volume codes but leaves the solution sensitive to the near-wall grid
spacing and, in high-order codes with negligible numerical diffusion,
produces persistent oscillations. They use, as finite-volume comparison,
OpenFOAM's wall value $\omega_w=6\nu/(\beta d^2)$ at the first cell for
$y^+\sim1$ (§3.1). Three remedies appear in the sources:

- **Regularization.** The authors' earlier regularized $k$-$\omega$ model
  (Tomboulides et al. 2018, as the 2025 paper describes it) writes $\omega=\omega_w+\omega'$,
  subtracts the analytical singular part $\omega_w$ and solves for the
  bounded remainder $\omega'$ with $\omega'=0$ at the wall. It is
  consistent under $p$- and $h$-refinement and equivalent to the standard
  model, but its extra source terms depend on the wall distance and its
  derivatives, it assumes a negligible Laplacian of the wall distance, and
  those sources cannot be treated implicitly (§1–§2).
- **Change of variable to $\tau_t=1/\omega$.** The
  [$k$-$\tau$ model](/methods/k-tau-model.md) has the wall condition
  $\tau_t=0$ and bounded sources; Tomboulides et al. present it as the
  successor of their regularized model (§1, §4).
- **Change of variable to $\ln\omega$.** The log-$\omega$ unknown of
  Ghidoni et al. above, and of the SST form on the
  [SST page](/methods/k-omega-sst-model.md).

**Low-Reynolds damping.** Tomboulides et al. transfer Wilcox's (1992)
low-Reynolds damping to their $k$-$\tau$ model (§2.1); in $k$-$\omega$
variables the turbulence Reynolds number is $Re_T=\rho k/(\mu\omega)$ and
the damping functions multiply the eddy viscosity ($\alpha^*$), the $k$
destruction ($\beta^*$) and the $\omega$ production ($\alpha$); the
printed functions and constants are on the
[$k$-$\tau$ page](/methods/k-tau-model.md). The low-Reynolds variant of the
regularized $k$-$\omega$ model captures the near-wall peak of $k$ in a pipe
(§3.2).

## High-order discretization

Elzaabalawy et al. (2023, §1) list four obstacles to high-order DG RANS:
stiff non-linear equations solved by fixed-point iteration; the positivity
of $k$ and $\omega$, since clipping or absolute values destroy the
polynomial continuity and low-order positivity devices do not generalize;
large gradients, with $\omega\to\infty$ at the wall and steep gradients at
the boundary-layer edge, where low-order schemes are stabilized by their own
numerical dissipation; and min/max functions, which create discontinuities
inside elements. They reject the $k$-$\ln\omega$ formulation of Bassi et
al. and Ilinca & Pelletier because it generates a non-conservative
non-linear term "problematic for DG methods to treat it implicitly", and
solve for $\omega$ directly with these remedies (§3–§4):

1. **Interpolate $1/\omega$, not $\omega$.** The eddy viscosity and the
   $\omega$-dependent terms use the interpolant of $1/\omega$, which is
   smooth near the wall; since $k_h/\omega_h$ is not a polynomial, the
   choice of node set sets an aliasing error, which "is used effectively to
   damp the oscillations of $\omega$ near the wall", whereas interpolating
   $\omega$ directly oscillates and goes negative (§3.1.1, Fig. 2).
2. **Gradient through $1/\omega$.** $\nabla\omega=-\omega^2\nabla(1/\omega)$
   in the cross diffusion and the SST/BSL blending, which keeps the sign of
   $\nabla\omega$ near the wall, so that the TNT switch does not alternate
   between 0 and 0.5 (§3.1.2, Eqs. 69–70).
3. **Wall elements removed from the $\omega$ problem.** Every element with a
   node (for simplices a vertex) on the wall is excluded, and
   $\omega=6\nu/(\beta y^2)$ is imposed as Dirichlet data on the new
   boundary; a large wall value of $\omega$, as Bassi et al. impose, "is not
   stable for high-order approximations when directly using $\omega$"
   (§3.1.2, Fig. 3).
4. **Mean-preserving scaling limiter** of Zhang & Shu on $k$ and on
   $1/\omega$, which removes negative values while keeping the element mean
   and, as cited, the accuracy (§4.2, Eqs. 88–92).
5. **Regressed eddy viscosity for SST.** The SST viscosity is only $C^0$
   inside an element; it is fitted by a degree-$N$ polynomial at the
   quadrature points, and diffusion terms are put in weak form because the
   derivative of the fit was unstable (§3.2.1).
6. **Segregated fixed-point loops** (exterior, mean flow, turbulence)
   with under-relaxation, because the turbulence equations are much stiffer
   than the mean-flow equations; the recommended factors are 0.4 and 0.5 for
   the velocity, 0.5 and 0.7 for $k$ and $\omega$ (§4.1, Eqs. 76–87).

Ghidoni et al. (2026, §2–§3) take the opposite route for the
$\omega$ variable: log-$\omega$ unknown with the realizability floor, primitive
variables $(p,\boldsymbol u,T,k,\tilde\omega_\ell)$ "to enhance the
robustness of the convergence", a modal DG method with BR2 lifting and exact
Riemann fluxes up to $N=6$, and an implicit linearized backward-Euler
pseudo-transient continuation with GMRES (§3.1–§3.2).
[Zhao et al. (2023b)](/sources/zhao-2023-b.md) avoid the issue by solving SST at first order (see the
[SST page](/methods/k-omega-sst-model.md)).
The log-$\omega$ route goes back to Bassi et al. (2005), who solved the
Wilcox model with $\ln\omega$ in DG, which Lodares et al. (2022) and
Vandenhoeck et al. (2022) cite; Vandenhoeck et al. extend it to SST in flux
reconstruction and compare their Wieghardt flat-plate profiles with the
DG $\mathbb P^2$ Wilcox $k$-$\ln\omega$ solution of Bassi et al. on 8800
elements, and recall that earlier flux-reconstruction RANS solvers were
limited to Spalart–Allmaras and Wilcox $k$-$\omega$
([Lodares et al. (2022)](/sources/lodares-2022.md), §1, §8;
[Vandenhoeck et al. (2022)](/sources/vandenhoeck-2022.md), §0, §1.1, §4.1).
Ghidoni & Noventa (2026) build their laminar-kinetic-energy transition
model on the same log-$\omega$ variable and find a plain $k$-$\ln\omega$
model less sensitive than the transition model to zero values of $k$
clipped in under-resolved far-field elements; they run it for the Blair
plates whose transition sits at the leading edge
([Ghidoni & Noventa (2026)](/sources/ghidoni-2026-b.md), §II, §IV B, §V;
see [laminar kinetic energy transition models](/methods/laminar-kinetic-energy-transition-model.md)).
Tomboulides et al. (2025) solve the regularized model in the spectral-element
codes [Nek5000](/software/nek5000.md) and NekRS with BDF/extrapolation time
stepping (§2.2; see
[spectral element method](/methods/spectral-element-method.md)).

**Unsteady RANS: the turbulence variables set the time step.** Ghidoni et
al. (2022) run the log-$\omega$ model
as unsteady RANS with linearly implicit Rosenbrock and peer time
integrators on their modal DG discretization (BR2, exact-Riemann fluxes,
$N=5$ in the URANS cases). The model is printed with $\bar k=\max(0,k)$,
the log variable $\tilde\omega_\ell$ under "realizability" conditions that
keep the normal stresses positive and the shear stresses within the
Schwarz inequality, and $\mu_t=\alpha^*\rho\bar k\,e^{-\tilde\omega_\ell}$, the
constants named but not printed; $k$ can be limited exactly to zero
because no term is divided by $\bar k$ after substitution
([Ghidoni et al. (2022)](/sources/ghidoni-2022.md), §2, Eqs. 1–8). For
adaptive time stepping they require the embedded error estimator to be
the $L^2$ norm over all variables, $k$ and $\tilde\omega_\ell$ included,
because these "are irregular and the main cause of instability"; a
domain average is not enough (§5, Eq. 67). Linearly implicit schemes,
although A- and L-stable, become unstable beyond a step they call the
"near-stability zone", where the per-step linearization of the stiff
turbulence equations fails; step-size control extends that limit by up
to an order of magnitude on the cylinder at $Re=3900$, with little or no
extra cost for some schemes (§4, §6.1, Tables 10–11; see the
[DG spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
page for the integrators).

## Evidence

- **Order of accuracy.** On a RANS manufactured solution at $Re=10^7$
  with $N=3$ triangles, the HDG velocity and pressure errors converge at
  rates 3.79–4.62 and 2.84–2.97, i.e. $N+1$ and $N$ (Elzaabalawy et al.
  2023, §5.1, Table 1; see
  [method of manufactured solutions](/methods/method-of-manufactured-solutions.md)).
  In a RANS [channel](/benchmarks/turbulent-channel-flow.md) at
  $Re=2\times10^6$ and $2\times10^8$ with Wilcox (1998), the rates are near
  $N+1$ from 30 to 150 elements across the channel and deteriorate on finer
  grids, because the wall singularity of $\omega$ makes the global rate
  "first-order accurate at most", as the authors state also holds for
  second-order finite volumes; an algebraic mixing-length model, without the
  singularity, restores $N+1$ (§5.2.1, Table 2, Figs. 13–16). The wall shear
  computed from the HDG auxiliary strain variable converges at order $N+1$,
  from the velocity gradient at order $N$ (Table 3, Fig. 15).
- **Inlet sensitivity.** On the NASA zero-pressure-gradient flat plate at
  $Re=10^7$, Wilcox (1998) is "very sensitive" to the inlet turbulence,
  TNT and BSL give better results, BSL and SST are less robust than TNT
  and Wilcox (1998) when the inlet eddy viscosity is low, and raising the
  inlet viscosity ratio to 100 is "one of the simplest remedies" at the cost
  of an overestimated skin friction (Elzaabalawy et al. 2023, §5.3, Figs.
  21–27). TNT with inlet ratio 0.1 overestimates the skin friction by about
  2% against an SST finite-volume reference; with ratio 100 the observed
  orders of $C_f$ are 1.84 from the velocity and 3.33 from the auxiliary
  variable (Table 4; see
  [turbulent boundary layer](/benchmarks/turbulent-boundary-layer.md)).
- **Error per degree of freedom.** For TNT on the same plate, HDG with
  $N=3$ on six grids and the finite-volume code ReFRESCO on 26 grids agree
  on the extrapolated drag, and at equal degrees of freedom the HDG
  numerical error is "significantly smaller" for integral, surface and local
  quantities (§6, Figs. 37–45).
- **Airfoil.** On the [NACA 0012](/benchmarks/naca-0012-airfoil.md) at
  $Re=6\times10^6$, $\alpha=0^\circ$, HDG runs with inlet ratio 6;
  $\omega$ oscillates in the wake and at lower inlet ratios the oscillations
  "obstruct the convergence of the solver", which the authors call "one of
  the drawbacks of using high-order methods while using the $k-\omega$
  model" (§5.4).
- **Robustness.** Elzaabalawy et al. find the method stable on fine meshes
  with $y^+<3$ at the wall and $x^+<3$ around the leading and trailing
  edges, and coarse elements at inlet, outlet or boundary-layer edge able to
  destroy the non-linear convergence (§7). Ghidoni et al. (2026) compute
  plates in zero, weak and strong adverse pressure gradient, the
  Driver–Seegmiller [backward-facing step](/benchmarks/backward-facing-step.md)
  and the NACA 0012 at $Re=6\times10^6$ with the Wilcox (2006) model up to
  $\mathbb P^6$, comparing with FUN3D $k$-$\omega$ results of the NASA
  Turbulence Modeling Resource (§4).
- **Regularized model against $k$-$\tau$ and SST.** In a channel at
  $Re_\tau\approx5200$ the regularized model gives $u_\tau=0.0413$ and
  its low-Reynolds variant 0.0415, against 0.0415 from DNS, 0.0412 from
  $k$-$\tau$ and 0.0409 from OpenFOAM SST (Tomboulides et al. 2025, §3.1,
  Table 1); in a pipe at $Re_\tau=1142$, 0.0524 and 0.0529 against 0.0519
  from DNS (§3.2, Table 2). On the Driver–Seegmiller step it reattaches at
  $6.49$ step heights against $6.26$ measured (§3.3); on the NACA 0012 at
  $\alpha=0^\circ$ it gives $C_D=0.00835$ against 0.0081 measured (§3.4,
  Table 3). In the same tables the NASA codes give, with their
  $k$-$\omega$ model, $C_D=0.00854$ (CFL3D) and 0.00837 (FUN3D) at $0^\circ$,
  and $C_D=0.01259$, $C_L=1.0958$ (CFL3D) and 0.01297, 1.1012 (FUN3D) at
  $10^\circ$ against 0.012 and 1.075 measured (Tables 3–4). On an OECD/NEA
  T-junction the regularized model ran at a CFL number of about 0.1, against
  about 2 for $k$-$\tau$, because its additional non-linear sources cannot
  be treated implicitly; its slight departure from $k$-$\tau$ in the core
  is attributed to wall-distance errors near the sharp corner (§3.5, §4).
- **High-order RANS of the RAE 2822.** At the first High-Order CFD
  Workshop the Bergamo group ran the Wilcox $k$-$\omega$ model (and an
  explicit algebraic Reynolds-stress model) with DG on the
  [RAE 2822 airfoil](/benchmarks/rae-2822-airfoil.md), alongside two
  Spalart–Allmaras DG submissions; the organizers report "a large spread
  among the groups and virtually no improvement from high order under
  uniform mesh refinement", attributed partly to the wake alignment of the
  initial mesh and partly to the choice of turbulence model
  ([Wang et al. (2013)](/sources/wang-2013.md), §5.4, Table V, Fig. 23).
  Sandberg & Michelassi (2022) list the model's eddy viscosity
  $\mu_t=\langle\rho\rangle k/\omega$ among the turbomachinery closures
  ([Sandberg & Michelassi (2022)](/sources/sandberg-2022.md), §2.2.2.1).
- **Cylinder wakes in two-dimensional URANS.** Ghidoni et al. (2022)
  compute the circular cylinder with the model at DG $N=5$: at $Re=3900$
  the drag coefficient is 1.52 (incompressible) and 1.62 (compressible,
  $M=0.1$) with $St=0.23$, different from LES, DNS and experiment but in
  line with other two-dimensional URANS (Rajani et al.: 1.65, 0.244),
  which the authors attribute to the missing three-dimensional effects; at
  $Re=1.4\times10^5$, where the model has no means of keeping the boundary
  layer laminar up to separation (unlike Spalart–Allmaras, which can be
  run with zero eddy viscosity there, as in the laminar-separation DES of
  Travin et al. they quote), it gives $St=0.271$, $C_D=0.751$, separation at
  $91^\circ$, base pressure $-C_{pb}=0.86$ and $L_r/D=0.72$, close to the
  two-dimensional RANS of Moussaed et al. (§6.1–6.2, Tables 9, 12; see
  [circular-cylinder wake](/benchmarks/circular-cylinder-wake.md)). On a
  three-blade vertical-axis wind turbine at $Re=1.6\times10^5$ and tip-speed
  ratio 1.5 (rotating frame, $N=2$, extruded mesh) the mean power
  coefficient is 0.173, against 0.171 for a cited two-dimensional RANS and
  0.152 for Noventa et al. (§6.4, Table 17).
- **Outlook.** Elzaabalawy et al. propose the $k$-$kl$ model, with $kl=0$
  at the wall and second velocity derivatives available element-wise in DG,
  and a "negative $k$-$kl$" analogue of negative
  [Spalart–Allmaras](/methods/spalart-allmaras-model.md), as alternatives
  better suited to high order (§7).

## Qualifications

- The two high-order sources disagree on method, not on a fact:
  Elzaabalawy et al. reject the $k$-$\ln\omega$ form for its non-conservative
  term in an implicit DG setting (§1), while Ghidoni et al. use it with an
  implicit DG solver up to $N=6$ (§2–§3). Elzaabalawy et al. require
  $y^+<3$ for robustness, Ghidoni et al. state $y_1^+\sim10$ as the DG
  wall-resolved requirement; the first concerns the node or element nearest
  the wall, the second the first-element height.
- Elzaabalawy et al. state that the polynomial-regression error of the SST
  viscosity is "believed to be negligible" compared with the modelling
  error (§3.2.1), yet judge SST of "questionable" robustness because of that
  regression and drop it (§5.3).
- Elzaabalawy et al. print the limiter floor as "$\epsilon=1^{-12}$"
  (§4.2).
- Sandberg & Michelassi cite the model as "Wilcox et al. (1998)" in the
  text (§2.2.2.1), while their reference list prints the single-author
  Wilcox (1998) book.
- Ghidoni et al. (2022) print the cross-diffusion term $\sigma_d$ in the
  compressible equations (Eq. 1) but not in the incompressible and
  rotating-frame ones (Eqs. 8–9); their pressure contains no $k$ while the
  $k$-sink appears as a source of the mean-flow energy equation (Eqs. 1–2).
  Their text gives the compressible $Re=3900$ lift fluctuation and
  Strouhal number as 1.19 and 0.225, their Table 9 as 1.13 and 0.23.
- By the rewriting above, Heinz's $C_{\omega1}$ plays the role of Wilcox's
  $\alpha$, and Heinz's destruction ratio $\alpha_\omega$ (printed $\beta$) is
  not Wilcox's $\beta$; the names in the table above are Wilcox's.

# Citations

- [Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md) — §1, §3.1 Eqs. 38–44, 55, 57–58, 69–70, §3.2–3.2.1, §4.1–4.2 Eqs. 76–92, §5.1 Table 1, §5.2.1 Tables 2–3 Figs. 13–16, §5.3 Table 4 Figs. 21–27, §5.4, §6 Figs. 37–45, §7.
- [Ghidoni et al. (2026)](/sources/ghidoni-2026.md) — §1, §2 Eqs. 1, 4, §3.1–3.2, §4 Table 1.
- [Zhao et al. (2023b)](/sources/zhao-2023-b.md) — §1, §3.2.
- [Tomboulides et al. (2025)](/sources/tomboulides-2025.md) — §1, §2 Eqs. 5–11, §2.1, §2.2, §3.1–3.5 Tables 1–4, §4.
- [Lodares et al. (2022)](/sources/lodares-2022.md) — §1, §8.
- [Vandenhoeck et al. (2022)](/sources/vandenhoeck-2022.md) — §0, §1.1, §4.1.
- [Ghidoni & Noventa (2026)](/sources/ghidoni-2026-b.md) — §II, §IV B, §V.
- [Heinz (2020)](/sources/heinz-2020.md) — §2.3 Eq. 11, §4.3 Eqs. 47–51.
- [Wang et al. (2013)](/sources/wang-2013.md) — §5.4 Table V Fig. 23.
- [Sandberg & Michelassi (2022)](/sources/sandberg-2022.md) — §2.2.2.1.
- [Ghidoni et al. (2022)](/sources/ghidoni-2022.md) — §2 Eqs. 1–8, §4, §5 Eq. 67, §6.1–6.2 Tables 9–12, §6.4 Table 17.
- [Wu et al. (2023)](/sources/wu-2023-b.md) — §2.1.1, Eq. 3, Table 1.
