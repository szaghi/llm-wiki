---
type: Method
title: "Partially-averaged Navier–Stokes"
description: "Girimaji's bridging hybrid model that solves RANS-form transport equations for the unresolved fractions f_k and f_ω of the kinetic energy and specific dissipation; its SST form, its use with high-order flux reconstruction, the shift of the optimal f_k with discretization order, and the criticism of feeding RANS equations fluctuating inputs."
status: established
aliases: [PANS, partially averaged Navier-Stokes, PANS k-ω SST, bridging model]
tags: [pans, hybrid-rans-les, flux-reconstruction, numerical-dissipation, separated-flow]
timestamp: 2026-10-25T13:40:00Z
---

# Partially-averaged Navier–Stokes

Partially-averaged Navier–Stokes (PANS), due to Girimaji, is a single-model
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) ("bridging") method. A
RANS closure is rewritten for the *unresolved* part of the turbulence, and
the ratios of unresolved to total kinetic energy, dissipation and specific
dissipation,

$$f_k=\frac{k_u}{k},\qquad f_\varepsilon=\frac{\varepsilon_u}{\varepsilon},\qquad f_\omega=\frac{\omega_u}{\omega},$$

set how much of the turbulence the simulation resolves; $f_k=1$ recovers
unsteady RANS and $f_k\to0$ approaches DNS. The subscript $u$ marks the
unresolved part (page-local symbols $k_u=f_kk$, $\varepsilon_u$,
$\omega_u=f_\omega\omega$). Since $\omega=\varepsilon/(\beta^*k)$, the ratios obey
$f_\omega=f_\varepsilon/f_k$. Dzanic et al. (2022) take $f_\varepsilon=1$
(dissipation scales entirely unresolved, after Girimaji & Wallin and
Pereira et al.), so $f_\omega=1/f_k$ and the model has the single parameter
$f_k$, kept constant in space and time to avoid commutation-error terms
([Dzanic et al. (2022)](/sources/dzanic-2022.md), §2.1).

## PANS with the SST closure

Dzanic et al. (2022) solve the compressible PANS equations, whose
unresolved stress is the [Boussinesq](/definitions/boussinesq-hypothesis.md)
form with the unresolved eddy viscosity $\nu_t$ and kinetic energy $k_u$,
closed by the [$k$-$\omega$ SST model](/methods/k-omega-sst-model.md) written
for $k_u$ and $\omega_u$ (§2.1, Eqs. 1–17; constants of App. A on the SST
page). Rewritten from the printed compressible Eq. 10 in incompressible
kinematic form *(compiler check, not in the sources)*, the $k_u$-equation
is

$$\partial_tk_u+u_j\partial_jk_u=P_k-\beta^*k_u\omega_u+\partial_j\Big[\Big(\nu+\sigma_k\nu_t\frac{f_\omega}{f_k}\Big)\partial_jk_u\Big],\qquad
\nu_t=\frac{a_1k_u}{\max(a_1\omega_u,\lvert\Omega\rvert F_2)},$$

with $u_j$ the resolved velocity. In the $\omega_u$-equation the diffusion and
the SST cross-diffusion are likewise multiplied by $f_\omega/f_k$, and the
destruction is printed as $-\rho(P'-P'/f_\omega+\beta\omega_u/f_\omega)$ with
$P'=\alpha\beta^*k_u/\nu_t$, which reduces to $-\rho\beta\omega_u$ at
$f_\omega=1$ (Eq. 11; see Qualifications and the
[SST page](/methods/k-omega-sst-model.md) for the dimensional correction). The blending functions $F_1$, $F_2$ are those
of SST evaluated with $k_u$, $\omega_u$ (Eqs. 13–15).

### Robustness devices for low-dissipation schemes

High-order schemes add little numerical dissipation, so Dzanic et al. make
the turbulence variables robust explicitly (§2.3):

- the $\omega_u$-equation is solved for $\ln\omega_u$ (after Ilinca &
  Pelletier and Bassi et al.), which keeps $\omega_u$ positive and is smoother
  (Eq. 23);
- a source $S_k=\max\big[0,(k_{\min}-k_u^n)/\Delta t+\nabla\cdot\boldsymbol F_k^n\big]$,
  built from a forward-Euler step with $\boldsymbol F_k$ the flux of $k_u$,
  holds $k_u$ above $k_{\min}=10^{-8}$; Bassi et al. instead allow negative
  $k$ in the solution and clip it to zero in the transport and auxiliary
  equations (Eq. 24; the device is not tested separately);
- the wall value of $\omega_u$ is $f_\omega\,60\nu/(\beta_1\Delta d_1^2)$, with the
  first-point distance $\Delta d_1$ the element height over $N+1$, so it is
  the same for all polynomial degrees (§3, Eq. 26).

## PANS in a high-order flux-reconstruction framework

Dzanic et al. (2022) implement PANS in PyFR with Huynh's flux
reconstruction, "a generalization of the nodal discontinuous Galerkin
method": a nodal polynomial of degree $N$ per element, a Rusanov-type
Riemann flux, BR2 viscous fluxes and explicit fourth-order Runge–Kutta
(§2.2–2.3). They compare $N=1$ (second order, "comparable to a finite volume
formulation") with $N=3$ (fourth order) at equal degrees of freedom, the
$N=1$ meshes having "approximately 6-8 times as many elements" (8 in both
test cases, by their Tables 1–2), and compare PANS with
under-resolved DNS (implicit LES with no model,
[implicit LES](/definitions/implicit-les.md)) on the same meshes. The stated
aim is "not to evaluate the efficacy of the PANS method, but to show the
effect of high-order discretizations" on it (§3).

**[Periodic hill](/benchmarks/periodic-hill.md)**, $Re_b=10{,}595$, $64\times64\times32$
degrees of freedom (97% fewer than the reference LES of Fröhlich et al.,
85% fewer than a low-order PANS of Razi et al.), $f_k=0.2$ and $0.3$; lower
$f_k$ is "not supported" at this resolution (§3.1):

- at $N=1$ both PANS and implicit LES overpredict flow reversal for
  $0\le x\le5$ and PANS barely improves on it; at $N=3$ both improve
  markedly, $f_k=0.2$ in "excellent agreement" with the reference (Fig. 3);
- the streamwise variance improves from $N=1$ to $N=3$ for PANS but not for
  implicit LES, which overpredicts it at both degrees (Fig. 4);
- at $N=3$ implicit LES shows large oscillations in the wall-normal
  variance, which the authors attribute to aliasing-driven instability of
  high-order schemes in under-resolved turbulence; PANS does not, "likely
  due to the suppression of aliasing errors" by a physically appropriate
  eddy viscosity (Fig. 5); no de-aliasing test is reported.

**Circular cylinder at $Re_D=3900$** (inline here; no page). The authors run
a new $N=3$ DNS with about 55.6 million degrees of freedom (minimum
$\eta/D=0.011$), giving a shedding Strouhal number $St=0.209$ and a
Kelvin–Helmholtz frequency $0.668\,U_\infty/D$, and compare PANS with
$f_k=0.1$, $0.2$, $0.3$ on unstructured prismatic grids with 20–30% fewer
degrees of freedom than an earlier low-order PANS (§3.2, Table 2):

- the best-agreeing $f_k$ moves from 0.3 at $N=1$ (agreeing with the DNS) to
  0.1 at $N=3$ (agreeing with the LES of Witherden et al.), which the
  authors read as "consistent with the PANS methodology": higher fidelity
  means a smaller unresolved fraction (Figs. 8–10);
- the $N=1$ runs overpredict the shedding and Kelvin–Helmholtz frequencies by
  about 10% and 6% at $x/D=3$; at $x/D=7$ only the $N=3$ PANS runs resolve
  both peaks, while $N=3$ implicit LES smears the shedding peak and misses the
  Kelvin–Helmholtz one (Figs. 11–12);
- the leading POD mode of streamwise velocity is placed correctly by $N=3$
  PANS and too close to the body by $N=3$ implicit LES (Fig. 13).

The authors conclude that high order benefits PANS proportionally more than
implicit LES, makes PANS less sensitive to $f_k$, and does so "without a
significant increase in computational effort" (§4); no timings are given.
They attribute the gains to lower [numerical dissipation](/properties/numerical-dissipation.md).

## Criticism: RANS equations with fluctuating inputs

Haering et al. (2022) class PANS, with DES and PITM, among the single-model
unified hybrids whose RANS transport equations, built and calibrated for
mean quantities, are fed fluctuating fields. Nonlinear sources such as the
$\varepsilon$ destruction then acquire spurious correlations, so their mean
depends on how much turbulence is resolved; the authors say the symptoms are
usually masked by numerical dissipation, coefficient tuning or averaging
([Haering et al. (2022)](/sources/haering-2022.md), §II D). They also recall
PANS simulations of the periodic hill at about one million cells with
second-order numerics among the successful hybrid results on that case
(§V B, citing Razi et al. 2017).

## Qualifications

- Dzanic et al. state that PANS blends "between DNS ($f_k=f_\omega=0$) and
  URANS ($f_k=f_\omega=1$)" (§2.1), but with their closure $f_\omega=1/f_k$,
  $f_k\to0$ sends $f_\omega\to\infty$, and their wall and inflow values of
  $\omega_u$ scale as $1/f_k$.
- *Compiler check, not in the sources:* in the printed Eq. 11 the
  destruction bracket has the dimensions of $\rho\omega$ rather than
  $\rho\omega^2$, and the printed log-form Eq. 23 keeps the sources of Eq. 11
  instead of dividing them by $\omega_u$ and lacks the term
  $(\nu+\sigma_\omega\nu_tf_\omega/f_k)\,\partial_j\ln\omega_u\,\partial_j\ln\omega_u$ that
  the change of variable produces from the diffusion; the form implemented
  in PyFR cannot be inferred from the text.
- The cylinder reference data disagree with each other: at $N=1$, $f_k=0.1$
  matches the LES of Parnaudeau et al. and $f_k=0.3$ the new DNS, so the
  "optimal" $f_k$ depends on which reference is preferred.

# Citations

- [Dzanic et al. (2022)](/sources/dzanic-2022.md) — §1, §2.1 Eqs. 1–17, §2.2–2.3 Eqs. 18–24, §3 Eq. 26, §3.1 Figs. 3–6, §3.2 Figs. 8–13, §4.
- [Haering et al. (2022)](/sources/haering-2022.md) — §I, §II D, §V B.
