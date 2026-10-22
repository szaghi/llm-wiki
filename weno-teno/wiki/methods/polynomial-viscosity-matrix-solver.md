---
type: Method
title: "Polynomial viscosity matrix (PVM) Riemann solver"
description: "PVM solvers write the numerical flux as a central average minus a viscosity matrix applied to the interface jump and replace the Roe matrix |A| by a polynomial in A that approximates the absolute value; evaluated by Horner's rule with finite-difference Jacobian–vector products they need neither eigenvectors nor separate wave-speed estimates per subsystem."
status: established
aliases: [PVM, PVM-int-8, Jacobian-free PVM, polynomial viscosity matrix, internal polynomial PVM, viscosity-matrix flux]
tags: [riemann-solver, numerical-flux, relativistic, mhd, finite-volume]
timestamp: 2026-10-23T16:00:00Z
---

# Polynomial viscosity matrix (PVM) Riemann solver

Many two-point fluxes can be written in **viscosity form**

$$h(u^-,u^+)=\tfrac12\big(f(u^-)+f(u^+)\big)-\tfrac12\,\mathsf Q_{i+1/2}\,[\![u]\!]_{i+1/2},$$

with a page-local viscosity matrix $\mathsf Q_{i+1/2}$: the Roe solver has
$\mathsf Q=\lvert A_{i+1/2}\rvert$, the [Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md)
$\mathsf Q=aI$. A **polynomial viscosity matrix** (PVM) solver takes

$$\mathsf Q_{i+1/2}=a\,\pi\big(a^{-1}A_{i+1/2}\big),$$

with $a$ an upper bound of the spectral radius of $A_{i+1/2}$ and $\pi(x)$ (page-local) a
polynomial that approximates $\lvert x\rvert$ on $[-1,1]$, so that the flux approximates the
Roe flux without its eigenstructure. As recalled by
[López-Miralles et al. (2023)](/sources/lopezmiralles-2023.md) (§3.2.2, Eqs. (32)–(33)), the
family goes back to Castro Díaz & Fernández-Nieto (2012), with rational (RVM), Osher-type
(DOT) and Chebyshev variants, and Castro, Gallardo & Marquina (2017) gave Jacobian-free
versions for relativistic MHD.

## The internal polynomial

The "internal" approximation of $\lvert x\rvert$ is built by the recursion

$$\pi_0=1,\qquad \pi_k(x)=\tfrac12\big(2\pi_{k-1}(x)-\pi_{k-1}(x)^2+x^2\big),\qquad \deg\pi_k=2^k,$$

and PVM-int-$2^k$ uses $\pi_k$. López-Miralles et al. use $k=3$ (PVM-int-8):

$$\pi_3(x)=-\tfrac1{128}x^8+\tfrac3{32}x^6-\tfrac{23}{64}x^4+\tfrac{31}{32}x^2+\tfrac{39}{128}$$

(Eqs. (34)–(35)). They state, from Castro et al. (2017), that PVM-int-$n$ solvers
"guarantee the stability conditions needed to ensure the robustness and convergence" (§3.2.2).
*(compiler check, not in the sources: expanding the recursion reproduces these coefficients;
on $[-1,1]$, $\pi_3(x)\ge\lvert x\rvert$ with equality only at $x=\pm1$, and $\pi_3(0)=39/128$,
so every eigenvalue receives at least its own upwind viscosity and the slow waves receive more.)*

## Jacobian-free evaluation

Because $\pi_k$ is even, $\mathsf Q[\![u]\!]$ is a polynomial in $A^2$ applied to the jump,
evaluated by Horner's rule; each product $A^2z$ is replaced by two flux differences
(§3.2.2, Eq. (36)). With the jump $z_0=u^+-u^-$, the mean state $u_{\mathrm m}=\tfrac12(u^-+u^+)$
(at which $A$ is evaluated) and a finite-difference step $\delta_{\mathrm{FD}}=10^{-8}$
(page-local symbols):

1. $\tilde u=u_{\mathrm m}+f(u_{\mathrm m}+\delta_{\mathrm{FD}}z)-f(u_{\mathrm m})$, so that
   $\tilde u-u_{\mathrm m}\approx\delta_{\mathrm{FD}}Az$;
2. $A^2z\approx\big(f(\tilde u)-f(u_{\mathrm m})\big)/\delta_{\mathrm{FD}}$;
3. Horner in $A^2$ with the coefficients of $\pi_3$ (and $a=1$, the speed of light, as the
   spectral bound) gives $\mathsf Q[\![u]\!]$ after four products $A^2z$.

Every flux evaluation at a perturbed state needs a primitive-variable recovery, the
expensive step of relativistic MHD ([relativistic hydrodynamics](/definitions/relativistic-hydrodynamics.md)).
Citing Castro et al. (2017), the authors state that PVM-int-8 costs about twice the
[HLL](/methods/hll-riemann-solvers.md) flux in CPU time, mainly because of these repeated
recoveries; for the radiation subsystem, whose variables are both primitive and conserved,
no extra recovery is needed (§5). No timing of their own code is given.

## In relativistic radiation MHD

López-Miralles et al. (2023) use PVM-int-8 in the finite-volume code Lóstrego for
relativistic radiation MHD with the M1 closure ([relativistic hydrodynamics](/definitions/relativistic-hydrodynamics.md)),
which they call the first use of a Jacobian-free PVM solver in radiation MHD. Its point is
that it treats the full system with one algorithm: the competing radiative HLL needs
separate wave-speed estimates for the magnetofluid block (a quartic characteristic equation)
and for the radiation block, because common speeds over-diffuse (§3.2.1).

**Opacity scaling** (contribution, Eqs. (37)–(38)). In optically thick cells the PVM
viscosity over-diffuses, so the whole viscosity vector is scaled,

$$h=\tfrac12\big(f(u^-)+f(u^+)\big)-\tfrac12\beta_\tau\,\mathsf Q[\![u]\!],\qquad\beta_\tau=\min\{1/\tau^-_{\mathrm{opt}},1/\tau^+_{\mathrm{opt}},1\},$$

with $\tau^\pm_{\mathrm{opt}}$ the "cell opacities" left and right of the interface; the formula is
not restated at Eq. (38), and the cell optical depth defined earlier for the speed limiter is
$\tau_{\mathrm{opt}}=\rho W(\kappa_{\mathrm a}+\sigma_{\mathrm s})\Delta x$ (Eq. (31); page-local
absorption and scattering coefficients $\kappa_{\mathrm a}$, $\sigma_{\mathrm s}$). Suppressing the viscosity outright for $\tau_{\mathrm{opt}}>1$ "yields oscillatory
solutions" (stated). The authors call the choice of $\beta_\tau$ "somehow arbitrary" (§5).

## Evidence

- **Smooth RMHD.** On the large-amplitude [circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md),
  PVM-int-8 errors are "very similar to those found with HLLC"; with MP3 reconstruction and
  third-order Runge–Kutta the observed order is 2.998835 on the finest pair of grids
  (Tables 2, 4, Fig. 1).
- **Optically thin radiation.** On radiation Riemann problems at $2^8$ zones, first order,
  PVM-int-8 is sharper than radiative HLL at the contact in the first test, less so in the
  second; the difference shrinks with piecewise-linear reconstruction (§4.1.2, Fig. 2).
- **Optically thick diffusion.** On a diffusing radiation pulse with cell optical depths 5,
  100 and 1000, PVM-int-8 with $\beta_\tau$ "improves slightly" on radiative HLL with
  optical-depth speed limiting; first-order reconstruction, PVM-int-8 with $\beta_\tau=1$ or HLL
  without speed limiting give "catastrophic diffusive solutions (specially for $\tau>100$)"
  (described, not plotted; §4.1.4, Fig. 7). The authors claim this is the first Riemann
  solver to improve on radiative HLL for $\tau_{\mathrm{opt}}\gg1$ (§5).
- **Degree.** PVM-int-16 gave results identical to PVM-int-8 at higher cost (stated, §5).

## Qualifications

- The stability and positivity of PVM-int-8 for the radiation-MHD system are asserted from
  Castro et al. (2017), not shown; the stiffest case of the paper, the optically thick
  [magnetized blast wave](/benchmarks/mhd-blast-wave.md), was run with radiative HLL, the
  minmod limiter and CFL 0.01, not with PVM (§4.2.1).
- The opacity scaling multiplies the fluid components of the viscosity as well; its effect
  on fluid shock capturing in opaque cells is not discussed. The paper does not relate it to
  [asymptotic preservation](/properties/asymptotic-preservation.md) of the diffusion limit.
- Printed slip: the Horner loop of §3.2.2 is printed for a general degree $2^k$ with
  $k+1$ products and $k+2$ coefficients; this matches the $2^{k-1}$ products and
  $2^{k-1}+1$ coefficients of an even polynomial of degree $2^k$ only for $k=3$, the case used
  *(compiler check, not in the sources)*.

# Citations

- [López-Miralles et al. (2023)](/sources/lopezmiralles-2023.md) — §3.2.1 (Eqs. (24)–(31)), §3.2.2 (Eqs. (32)–(38)), §4.1.1–4.1.4 (Tables 1–4, Figs. 1–2, 7), §4.2.1, §5 (arXiv v1).
