---
type: Method
title: "Wilcox k-ω model"
description: "Wilcox's two-equation k-ω eddy-viscosity model and its unblended variants (1998, 2006, Kok's TNT), with constants, near-wall behaviour of ω, the log-ω form, and the obstacles and remedies of solving it with high-order discontinuous Galerkin and hybridizable DG discretizations."
status: established
aliases: [k-omega model, Wilcox k-ω, Wilcox 1998, Wilcox 2006, Wilcox 07, k-ω 2006, TNT, turbulent/non-turbulent k-ω, k-log-ω, k-ln ω]
tags: [rans, eddy-viscosity, dg, boundary-layer]
timestamp: 2026-10-26T20:48:00Z
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
boundary-layer regions", recalling that Menter used 20 and later 10 (§3.1.1,
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

Ghidoni et al. also print $\alpha^*=1$, so $\mu_t=\rho\bar k/\omega$ (§2).
BSL and SST, the blended members of the family, are on the
[SST page](/methods/k-omega-sst-model.md); in Elzaabalawy et al.'s notation
their cross diffusion is $\sigma_d=2\sigma_{\omega2}(1-F_1)$ (§3.2).

The TNT expression for $\alpha$ is the log-layer condition. It gives
$\alpha=0.5532$ for TNT; with the Wilcox (1998) constants and $\kappa=0.41$
it gives 0.520, matching 13/25, and with the Wilcox (2006) constants it
gives 0.520 for $\kappa=0.40$ but 0.507 for $\kappa=0.41$ *(compiler check,
not in the sources)*.

### Near-wall behaviour of $\omega$ and $k$

As $y\to0$, $\omega\to6\nu/(\beta y^2)$, valid for $y^+<3$, and $1/\omega$
is therefore quadratic in the wall distance (Elzaabalawy et al. 2023,
§3.1.1–3.1.2, Eq. 57). The matching viscous-sublayer law for $k$ is
$k^+=C_k(y^+)^{p_k}$ with $p_k=\tfrac12+\sqrt{\tfrac14+6\beta^*/\beta}$ and $C_k$
between 0.0025 and 0.0032 depending on the variant, as recalled (Eq. 58;
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

# Citations

- [Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md) — §1, §3.1 Eqs. 38–44, 55, 57–58, 69–70, §3.2–3.2.1, §4.1–4.2 Eqs. 76–92, §5.1 Table 1, §5.2.1 Tables 2–3 Figs. 13–16, §5.3 Table 4 Figs. 21–27, §5.4, §6 Figs. 37–45, §7.
- [Ghidoni et al. (2026)](/sources/ghidoni-2026.md) — §1, §2 Eqs. 1, 4, §3.1–3.2, §4 Table 1.
- [Zhao et al. (2023b)](/sources/zhao-2023-b.md) — §1, §3.2.
