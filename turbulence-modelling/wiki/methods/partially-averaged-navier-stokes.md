---
type: Method
title: "Partially-averaged Navier–Stokes"
description: "Girimaji's bridging hybrid model that solves RANS-form transport equations for the unresolved fractions of kinetic energy and dissipation; its SST form on high-order flux reconstruction, its variable-density BHR form for Rayleigh–Taylor mixing, the choice of resolution parameters, and the criticism of feeding RANS equations fluctuating inputs."
status: established
aliases: [PANS, partially averaged Navier-Stokes, PANS k-ω SST, bridging model, PANS BHR-LEVM, variable-density PANS, BHR model]
tags: [pans, hybrid-rans-les, flux-reconstruction, numerical-dissipation, separated-flow]
timestamp: 2026-10-26T07:20:00Z
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

## Variable-density PANS with the BHR closure

Pereira et al. (2021) apply PANS to variable-density, buoyancy-driven
turbulence, closing it with a scale-aware form of the
Besnard–Harlow–Rauenzahn (BHR) linear eddy-viscosity model derived in a
companion paper by the same authors
([Pereira et al. (2021)](/sources/pereira-2021.md), §III, Eqs. 5–21). In
registry notation the overbar is the PANS resolved field and the tilde its
density-weighted (Favre-filtered) counterpart (the source writes
$\langle\cdot\rangle$ and $\{\cdot\}$). Page-local symbols: $\ell_u$ the
unresolved dissipation length scale (source $S_u$), $a_i$ the unresolved
velocity mass-flux vector $\overline{\rho'u_i'}/\bar\rho$ and $b$ the
density–specific-volume correlation $-\overline{\rho'(1/\rho)'}$ (both
unresolved parts), $f_a$, $f_b$ their unresolved-to-total ratios.

**Closure.** The unresolved stress is Boussinesq, in registry sign
$\tfrac23k_u\delta_{ij}-2\nu_t\tilde S_{ij}$, with
$\nu_t=c_\mu\ell_u\sqrt{k_u}$ (Eqs. 5–6; the source prints the opposite sign,
see the [Boussinesq page](/definitions/boussinesq-hypothesis.md)). Six
transport equations are solved, for $k_u$, $\ell_u$, the three components of
$a_i$ and $b$ (Eqs. 7–10). The $k_u$-equation reads

$$\partial_t(\bar\rho k_u)+\partial_j(\bar\rho k_u\tilde u_j)=P_b+P_s-\bar\rho\varepsilon_u+\partial_j\Big(\frac{\bar\rho\nu_t}{\sigma_k}\frac{f_\varepsilon}{f_k^2}\partial_jk_u\Big),$$

with shear production $P_s$ and buoyancy production
$P_b=a_j\,\partial_j\bar p$ (Eqs. 17–18); the $\ell_u$-equation has the
same diffusion factor $f_\varepsilon/f_k^2$, and the $a_i$- and $b$-equations
carry the ratios $f_a$, $f_b$ in their sources. No coefficient value is
printed; they are deferred to the companion paper.

*Compiler check, not in the sources:* with $f_\omega=f_\varepsilon/f_k$, the
diffusion multiplier $f_\omega/f_k$ of the SST form of Dzanic et al. above
equals $f_\varepsilon/f_k^2$, so the two closures scale the turbulent
diffusion of the unresolved quantities identically.

**Resolution parameters.** Besides $f_k$ and $f_\varepsilon$, the closure has
$f_a$ and $f_b$; the length-scale ratio follows as
$f_\ell=f_k^{3/2}/f_\varepsilon$ (page-local; Eq. 21), and the unresolved
eddy viscosity relative to the RANS one is $f_k^2$ when $f_\varepsilon=1$
(Eq. 24). The authors note that $k_u$ and $\varepsilon_u$ are turbulent while
$a_i$ and $b$ can also carry coherent, non-turbulent content. Three
strategies are compared (§III):

- **S1:** prescribe $f_k$, set $f_\varepsilon=f_a=f_b=1$;
- **S2:** prescribe $f_k$, set $f_a=\sqrt{f_k}$, $f_\varepsilon=f_b=1$, assuming
  that density fluctuations come mostly from the coherent field;
- **S3:** $f_\varepsilon=1$, $f_a\approx f_k/2$, $f_b=f_k$, from a priori
  filtering of DNS of homogeneous variable-density turbulence at Atwood
  number 0.75. From a priori filtering of forced isotropic-turbulence DNS,
  $f_\varepsilon=1$ is "adequate for practical computations, i.e.,
  $f_k\ge0.20$" (Fig. 4a, from the companion paper).

**Rayleigh–Taylor results.** In the finite-volume code xRAGE (HLLC,
parabolic reconstruction, low-Mach correction, Heun time stepping) on a
$256^2\times768$ grid, at Atwood number 0.5 and Reynolds number up to about
500, with $f_k=0$ (no closure) as the reference (§II, §IV;
[Rayleigh–Taylor mixing](/benchmarks/rayleigh-taylor-mixing.md)):

| $f_k$ | 0.25 | 0.35 | 0.50 |
|---|---|---|---|
| $\alpha_b$, S1 | 0.016 | 0.012 | 0.027 |
| $\alpha_b$, S2 | 0.024 | 0.015 | 0.016 |
| $\alpha_b$, S3 | 0.018 | 0.012 | 0.013 |

against 0.043 for RANS ($f_k=1$) and 0.025 for the reference, which matches
the DNS of Livescu et al. (Table II, where these two values are printed once; $\alpha_b$ the growth-rate coefficient of the mixing layer). RANS
overpredicts mixing, gives linear mixture-fraction profiles and a molecular
mixing parameter tending to one, and disturbs even the laminar linear
regime. S2 gives the smallest errors: at $f_k=0.25$ it reproduces the
reference, and it needs only $f_k\le0.35$; S1 improves as $f_k$ decreases,
with larger errors and late-time ($t>20$) discrepancies that the authors
attribute to $f_a=1$. S3 does not converge as
$f_k$ decreases, shows an overshoot of $b$ at $t=2.5$ and robustness
problems, which the authors attribute to its fully-developed-turbulence
assumption being violated at early times; they suggest dynamic strategies
for $f_a$, $f_b$ (§IV.2, §IV.3.2, §V). The minimum resolution is set by the
need to resolve the bubbles and spikes that trigger turbulence: for
$f_k\le0.35$ the coherent structures at $t=2.5$ are indistinguishable from
the reference, while larger $f_k$ dissipates them (§IV.3.4, Fig. 16).

**Effective viscosity.** The authors define an effective viscosity
$\nu+\nu_t+\nu_n$, with $\nu_n$ the (unquantified) numerical viscosity, and
the effective Reynolds number built on it (Eqs. 22–23). Excluding $\nu_n$,
the peak planar-averaged ratio to $\nu$ at $t=25$ is 20 737 for RANS, 1376
(S1) and 408 (S2) at $f_k=0.25$, while S3 makes it grow after $t\approx3$ for
$f_k<0.5$ (§IV.3.1, Fig. 11). The effective ratio $\nu_t/\nu_t^{\mathrm{RANS}}$
does not follow the prescribed $f_k^2$, which the authors attribute to the
transient flow's sensitivity to accumulated modelling errors (Fig. 13). See
[numerical dissipation](/properties/numerical-dissipation.md).

S3 is the strategy whose parameters come from a priori filtering of DNS of
a different, fully developed flow; inside the solver, on the transitional
flow, it is the one that fails (see
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)).

## Other uses recalled

Cai et al. (2022) list PANS (Rao et al.) among the "advanced turbulence
models" assessed on the Ahmed body, next to DES, IDDES, embedded LES,
scale-adaptive and stress-blended eddy simulation, without giving its
results ([Cai et al. (2022)](/sources/cai-2022.md), §I). Carlsson et al.
(2023) name PANS among the hybrid RANS-LES methods besides DES and its
delayed, improved and zonal forms
([Carlsson et al. (2023)](/sources/carlsson-2023.md), §1).
Delassaux et al. (2023) cite PANS studies of cars next to DDES and LES ones
for the statement, which they call "well known", that hybrid RANS/LES does
not give better integrated loads than RANS on realistic cars; their own
comparison uses delayed DES, not PANS
([Delassaux et al. (2023)](/sources/delassaux-2023.md), §6; HAL author
manuscript; see [hybrid RANS/LES](/definitions/hybrid-rans-les.md)).

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

- The reference of Pereira et al. is the same code at $f_k=0$ with no
  closure and no artificial viscosity, which the authors call a
  "high-fidelity simulation resolving all flow scales" while noting that the
  initial perturbations are not fully resolved on the $256^2\times768$ grid
  (molecular mixing parameter 0.26 at $t=0$; §IV.2).
- Pereira et al. print the shear production as $-\bar\rho\,\tau^{\mathrm{src}}_{ij}\partial_j\tilde u_i$
  with their stress $\tau^{\mathrm{src}}_{ij}=2\nu_t\tilde S_{ij}-\tfrac23k_u\delta_{ij}$
  (Eqs. 5, 17; $\tau^{\mathrm{src}}$ page-local); with that sign the
  eddy-viscosity part of the production is negative, so either the stress or
  the production carries a sign slip, and the registry form
  $-\bar\rho\big(\tfrac23k_u\delta_{ij}-2\nu_t\tilde S_{ij}\big)\partial_j\tilde u_i$
  is the positive one *(compiler check, not in the sources)*.
- The same paper defines $\alpha_b=\dot h^2/(4ghAt)$ as the growth rate of
  the mixing-layer *half-width* (App. A, Eq. A9), with $h$ the full 5%–95%
  height and $At$ the Atwood number; for $h=\alpha\,At\,g\,t^2$ the formula
  returns $\alpha$, the coefficient of the full height *(compiler check, not
  in the sources)*. The convention matters when comparing with other
  $\alpha_b$ values.
- Pereira et al. state that accuracy improves "monotonically" as $f_k$
  decreases with S1, judged on the height $h(t)$ (Fig. 8a); the S1 values of
  $\alpha_b$ in Table II (0.027, 0.012, 0.016 at $f_k=0.50$, 0.35, 0.25) are
  not monotonic in their distance from 0.025. They also give the maximum
  CFL number as 0.5 for all runs (§II) while saying S3 needed a CFL "not
  exceeding 0.5" (§IV.2).

# Citations

- [Dzanic et al. (2022)](/sources/dzanic-2022.md) — §1, §2.1 Eqs. 1–17, §2.2–2.3 Eqs. 18–24, §3 Eq. 26, §3.1 Figs. 3–6, §3.2 Figs. 8–13, §4.
- [Haering et al. (2022)](/sources/haering-2022.md) — §I, §II D, §V B.
- [Pereira et al. (2021)](/sources/pereira-2021.md) — §II, §III Eqs. 5–21 Fig. 4, §IV.1–IV.3 Eqs. 22–25 Table II Figs. 8–16, §V, App. A Eq. A9.
- [Cai et al. (2022)](/sources/cai-2022.md) — §I (HAL v1).
- [Carlsson et al. (2023)](/sources/carlsson-2023.md) — §1.
- [Delassaux et al. (2023)](/sources/delassaux-2023.md) — §6 (HAL author manuscript).
