---
type: Method
title: "Central-upwind schemes"
description: 'Central-upwind fluxes use only one-sided local speeds $a^\pm_{i+1/2}$ and no Riemann solver; the flux is algebraically the HLL form, it reduces to upwind only when all eigenvalues share a sign, and its dissipation is reduced by characteristic-wise diffusion, Rankine–Hugoniot speeds or smoothness switches.'
status: established
aliases: [CU scheme, Kurganov–Noelle–Petrova flux, semi-discrete central-upwind scheme, Riemann-solver-free scheme]
tags: [central-scheme, numerical-flux, finite-volume, characteristic, low-dissipation]
timestamp: 2026-10-23T03:53:00Z
---

# Central-upwind schemes

Central-upwind (CU) schemes are semi-discrete finite-volume (or, inside
[A-WENO](/methods/alternative-weno.md), finite-difference) schemes whose numerical flux needs
no exact or approximate Riemann solver, only estimates of the one-sided local propagation
speeds $a^+_{i+1/2}\ge0\ge a^-_{i+1/2}$. As recalled by
[Chertock et al. (2023)](/sources/chertock-2023.md) (§1), they descend from the staggered
central schemes, which "basically average over the Riemann fans rather than resolving them"
and therefore carry large numerical dissipation; CU schemes use non-uniform control volumes
whose size is proportional to the one-sided speeds, and were proposed to reduce the
excessive dissipation of central schemes; higher resolution, they add, comes from reducing
it further. [Wang et al. (2023b)](/sources/wang-2023-b.md) (§1) state that CU fluxes in
general carry more numerical dissipation than upwind fluxes.

## The second-order CU flux

For $\frac{d}{dt}\bar u_i=-\frac1{\Delta x}\big(\hat f_{i+1/2}-\hat f_{i-1/2}\big)$ with
reconstructed one-sided values $u^\pm_{i+1/2}$, the flux of Kurganov, Noelle and Petrova
(2001), as recalled by [Chertock et al. (2023)](/sources/chertock-2023.md) (§2, Eqs.
(2.2)–(2.4)), is

$$\hat f_{i+1/2}=\frac{a^+_{i+1/2}f(u^-_{i+1/2})-a^-_{i+1/2}f(u^+_{i+1/2})}{a^+_{i+1/2}-a^-_{i+1/2}}+\frac{a^+_{i+1/2}a^-_{i+1/2}}{a^+_{i+1/2}-a^-_{i+1/2}}\big(u^+_{i+1/2}-u^-_{i+1/2}\big),$$

$$a^+_{i+1/2}=\max\big\{\lambda_m(A(u^-_{i+1/2})),\lambda_m(A(u^+_{i+1/2})),0\big\},\qquad a^-_{i+1/2}=\min\big\{\lambda_1(A(u^-_{i+1/2})),\lambda_1(A(u^+_{i+1/2})),0\big\}.$$

*(compiler check, not in the sources: since $a^-\le0\le a^+$, the coefficient of the jump is
non-positive, so the second term is dissipative.)* [Wang et al. (2023b)](/sources/wang-2023-b.md) stress a sign
convention: on $u^\pm$ the superscript denotes the side of the interface, on $a^\pm$ the
largest positive and smallest negative speed (§3.1).

*(compiler check, not in the sources: this is, term by term, the subsonic branch of the
[HLL flux](/methods/hll-riemann-solvers.md) as printed by
[Balsara et al. (2024)](/sources/balsara-2024.md) (Eq. (3.6), without non-conservative
products) with $s^-=a^-$, $s^+=a^+$; the clipping of the speeds at zero makes the CU flux
coincide with HLL also in the supersonic cases. With $a^+=-a^-=a$ it is the
[local Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md).)*

The CU scheme reduces to the upwind scheme for a system whose Jacobian has only positive (or
only negative) eigenvalues, but not otherwise
([Chertock et al. (2023)](/sources/chertock-2023.md), §1, §3). In Chertock et al. the
reconstruction is second-order piecewise linear with the generalized minmod limiter
(one-sided differences weighted by 2) applied to local characteristic variables; applied to
conservative variables it "typically leads to large oscillations" (§2.1; see
[characteristic decomposition](/methods/characteristic-decomposition.md),
[TVD and slope limiters](/definitions/total-variation-diminishing.md)). Time integration is
three-stage third-order [SSP Runge–Kutta](/methods/ssp-runge-kutta.md); the formal order is
fixed by the reconstruction and the ODE solver (§2).

## Central part plus diffusion

[Chertock et al. (2023)](/sources/chertock-2023.md) (§3, Eqs. (3.1)–(3.4)) rewrite the flux
as a central average of the fluxes **of the cell averages** plus a numerical diffusion,

$$\hat f_{i+1/2}=\tfrac12\big(f(\bar u_i)+f(\bar u_{i+1})\big)+\mathcal D_{i+1/2},$$

$$\mathcal D_{i+1/2}=R\,\mathcal P R^{-1}\Big[f(u^-_{i+1/2})-\tfrac12\big(f(\bar u_i)+f(\bar u_{i+1})\big)\Big]+R\,\mathcal M R^{-1}\Big[f(u^+_{i+1/2})-\tfrac12\big(f(\bar u_i)+f(\bar u_{i+1})\big)\Big]+R\,\mathcal Q\,L\big(u^+_{i+1/2}-u^-_{i+1/2}\big),$$

with $R=R_{i+1/2}$ at an averaged state, the diffusion $\mathcal D_{i+1/2}$ and diagonal
$\mathcal P,\mathcal M,\mathcal Q$ (page-local) whose entries are all equal to
$\big(a^+,-a^-,a^+a^-\big)/(a^+-a^-)$. Because the entries are identical, $R\mathcal PR^{-1}$ is
a multiple of the identity and this is only a rewriting; replacing the entries by
field-wise functions of the characteristic speeds gives the
[LCD central-upwind scheme](/methods/lcd-central-upwind-scheme.md).

## Reducing the dissipation

Chertock et al. (§1) list the earlier routes: built-in anti-diffusion from a more accurate
evolution step, a numerical-dissipation switch, and sharper one-sided speeds from discrete
Rankine–Hugoniot conditions. Two of them meet in the
[adaptive-diffusion central-upwind Rankine–Hugoniot flux](/methods/adaptive-diffusion-central-upwind-flux.md)
of [Wang et al. (2023b)](/sources/wang-2023-b.md), which adds to the flux above the
minmod "anti-diffusion" correction

$$u^+_{i+1/2}-u^-_{i+1/2}\ \longrightarrow\ u^+_{i+1/2}-u^-_{i+1/2}-\Delta^{\mathrm{ad}}_{i+1/2},\qquad \Delta^{\mathrm{ad}}_{i+1/2}=\mathrm{minmod}\big(u^+_{i+1/2}-u^{\mathrm{HLL}}_{i+1/2},\,u^{\mathrm{HLL}}_{i+1/2}-u^-_{i+1/2}\big),$$

$$u^{\mathrm{HLL}}_{i+1/2}=\frac{a^+_{i+1/2}u^+_{i+1/2}-a^-_{i+1/2}u^-_{i+1/2}-\big[f(u^+_{i+1/2})-f(u^-_{i+1/2})\big]}{a^+_{i+1/2}-a^-_{i+1/2}}$$

(Eq. (5); $\Delta^{\mathrm{ad}}$ and $u^{\mathrm{HLL}}$ page-local; minmod componentwise), and
tightens $a^\pm$ with regularized Rankine–Hugoniot speeds and a smoothness switch.
The same built-in anti-diffusion appears in the path-conservative CU flux of
[Chu et al. (2022)](/sources/chu-2022.md) (Eqs. (2.2), (2.5)–(2.6)), who note that it "was
switched off" in the second-order path-conservative CU scheme of Castro Díaz, Kurganov and
Morales de Luna (2019) because that scheme was built on the earlier CU flux without it (§2).

Both papers measure the gain by the same qualitative proxies on Euler tests: sharper
contacts in 1D, curlier contact curves in the explosion problem, a longer jet in the
implosion problem, richer [Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md)
and [Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md) structures, better
sideband instability in 2D Riemann configuration 3
([two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md))
([Chertock et al. (2023)](/sources/chertock-2023.md), §5;
[Wang et al. (2023b)](/sources/wang-2023-b.md), §4). See
[numerical dissipation](/definitions/numerical-dissipation.md).

## Non-conservative systems and fifth order

For $\partial_tu+\partial_xf(u)+\mathcal C(u)\partial_xu=0$ the CU flux is combined with path
integrals of the non-conservative product, shared between the two neighbouring cells with the
weights $a^+/(a^+-a^-)$ and $-a^-/(a^+-a^-)$: the path-conservative central-upwind (PCCU)
scheme, recalled by [Chu et al. (2022)](/sources/chu-2022.md) (§2, Eqs. (2.1)–(2.9)) and
written out on [path-conservative schemes](/methods/path-conservative-scheme.md). Chu et al.
insert the PCCU flux of a global flux into [A-WENO](/methods/alternative-weno.md) to reach fifth
order on point values (§4, Eq. (4.1)), with fifth-order WENO-Z interpolation of the interface
states in local characteristic variables of a Roe-averaged matrix (Remark 6.2). For the
two-layer shallow-water system the one-sided speeds are taken from Lagrange-theorem bounds
(citing Kurganov–Petrova) instead of Eq. (2.7) (§2).

[Kurganov et al. (2023)](/sources/kurganov-2023.md) (Remark 2.2, citing Castro, Morales de Luna and
Parés 2017) state that the first-order version of the PCCU scheme coincides with the semi-discrete
HLL scheme for non-conservative systems, which agrees, for the conservative case, with the
compiler check in the section on the second-order CU flux.

Their evidence that the high order pays off is a comparison at equal cost: in a 2D two-layer
interface-propagation problem the fifth-order scheme on $\Delta x=\Delta y=1/200$ and the
second-order PCCU scheme (generalized minmod parameter $\theta=1$, page-local) on $1/450$ take "approximately the same
CPU time", and the fifth-order scheme gives the better resolution (§7.2, Ex. 6, Fig. 7.10; no
absolute timings or hardware printed). In 1D the fifth-order scheme resolves the intermediate
state of an interface Riemann problem "much better" than the second-order scheme on the same
meshes, $\Delta x=1/200$ and $1/400$ (Ex. 3, Fig. 7.4).

## Global fluxes and well-balanced diffusion

Central-upwind fluxes are the natural partner of [flux globalization](/methods/flux-globalization.md)
because they need no Riemann solver for the global flux $K$, which upwind schemes would
([Kurganov et al. (2023)](/sources/kurganov-2023.md), §1). The flux-globalized CU flux is the
formula above with $f(u^\pm)$ replaced by $K^\pm_{i+1/2}$ (§3, Eq. (3.3)). At a discrete steady
state $K^+=K^-$, but the diffusion term $\frac{a^+a^-}{a^+-a^-}(u^+-u^-)$ survives wherever the
interface states differ, which is generic at a jump of the cross-section or of the bottom, and
the scheme is then not well-balanced unless $a^+a^-=0$ or $u^+=u^-$ (§4.2, Eqs.
(4.13)–(4.14)). Kurganov et al. therefore replace $u^\pm$ in the diffusion term only by
modified states $\check u^\pm$ (page-local) that coincide whenever the reconstructed equilibrium variables
coincide and differ from $u^\pm$ by $O(\Delta x^2)$ in smooth flow (Eqs. (4.15)–(4.16)); for a
static component (cross-section, bottom) its two interface values are replaced by their
average (Remark 4.3). The scheme is written out on
[flux globalization](/methods/flux-globalization.md) and its well-balancing on
[well-balancing](/properties/well-balancing.md).

Their second-order setting is piecewise-linear reconstruction with the generalized minmod
limiter, parameter $1.3$ in the range $[1,2]$ (Chertock et al. use $2$, CFL $0.4$), three-stage
SSP Runge–Kutta and CFL $1/2$, $\Delta t=\Delta x/(2\max_i\max(a^+_{i+1/2},-a^-_{i+1/2}))$ (§2, §7).

## In finite-volume codes

Two OpenFOAM-based solvers of the bundle name the Kurganov-type central fluxes.
[Weng & Mével (2023)](/sources/weng-2023.md) (§3.1) list "Kurganov" and "Tadmor" fluxes among
the options of blastFoam, next to HLL-type and AUSM+ fluxes, but run their validation with
HLLC ([HLL-family solvers](/methods/hll-riemann-solvers.md)).
[Bielawski et al. (2023)](/sources/bielawski-2023.md) (§3) write that the viscous terms of their
GPU-ported OpenFOAM solver "utilize a KNP formulation", citing the OpenFOAM implementation of
Greenshields et al. ("semi-discrete, non-staggered central schemes ... for high-speed viscous
flows"), while the inviscid fluxes use HLLC; no formula for the viscous terms is printed.

## Qualifications

- No positivity, entropy or linear-stability analysis is given for the dissipation-reduced
  variants in either paper; the evidence is visual comparison with the predecessor scheme.
- Chertock et al. note that for Kelvin–Helmholtz the numerical solutions do not converge
  under refinement; Cesàro averages of the two CU schemes differ, which they read as a
  limiting dissipative weak solution that depends on the numerical diffusion (§5.2, Ex. 8).
  Finer small-scale structure is therefore not by itself evidence of accuracy.
- Wang et al. print the $\Delta U$, $\Delta F$ jumps in the Rankine–Hugoniot speeds without
  defining them in §3; Appendix A gives $\Delta u=u^+-u^-$.

# Citations

- [Chertock et al. (2023)](/sources/chertock-2023.md) — §1, §2 (Eqs. (2.2)–(2.8)), §3 (Eqs. (3.1)–(3.4)), §5 (arXiv v2).
- [Wang et al. (2023b)](/sources/wang-2023-b.md) — §1, §3 (Eqs. (5)–(9)), §4.
- [Balsara et al. (2024)](/sources/balsara-2024.md) — Eq. (3.6), the HLL flux used for the comparison.
- [Chu et al. (2022)](/sources/chu-2022.md) — §2 (Eqs. (2.1)–(2.9)), §4 (Eq. (4.1)), Remark 6.2, §7 (Exs. 3, 6).
- [Weng & Mével (2023)](/sources/weng-2023.md) — §3.1.
- [Kurganov et al. (2023)](/sources/kurganov-2023.md) — §1, §2 (Eqs. (2.2)–(2.4), Remark 2.2), §3 (Eq. (3.3)), §4.2 (Eqs. (4.13)–(4.16), Remark 4.3), §7.
- [Bielawski et al. (2023)](/sources/bielawski-2023.md) — §3 (accepted manuscript).
