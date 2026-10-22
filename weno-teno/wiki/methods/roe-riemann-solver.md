---
type: Method
title: "Roe approximate Riemann solver"
description: "Roe's solver upwinds every characteristic field of a linearized flux Jacobian at the Roe-averaged state; in the bundle's sources it is the least diffusive run-time option of finite-volume codes, the default interface flux of several WENO and TENO tests, used with a Harten–Hyman-type entropy fix, and prone to the carbuncle at strong shocks."
status: established
aliases: [Roe flux, Roe scheme, Roe solver, linearized Riemann solver, Roe–Harten flux]
tags: [riemann-solver, numerical-flux, characteristic, finite-volume]
timestamp: 2026-10-23T10:00:00Z
---

# Roe approximate Riemann solver

The **Roe solver** is the two-point numerical flux

$$h^{\mathrm{Roe}}(u^-,u^+)=\tfrac12\big(f(u^-)+f(u^+)\big)-\tfrac12\,\hat R\,\lvert\hat\Lambda\rvert\,\hat L\,(u^+-u^-),$$

where $\hat R$, $\hat L=\hat R^{-1}$ and the diagonal $\lvert\hat\Lambda\rvert$ of eigenvalue moduli
(page-local) belong to a linearized Jacobian $A(\hat u)$ at the **Roe-averaged** state $\hat u$.
It is the matrix-dissipation member of the family
$h=\tfrac12\big(f(u^-)+f(u^+)\big)-\tfrac12\lvert Q\rvert(u^+-u^-)$ that
[Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) (§3, Eqs. (20)–(22)) write with a
dissipation matrix $Q$ (page-local): the Roe matrix gives Roe, the spectral radius times the
identity gives the [Rusanov flux](/methods/lax-friedrichs-flux.md). In its scalar-speed reading,
[Fu (2023)](/sources/fu-2023.md) (§3.6, Eq. (29)) writes Roe, Rusanov, HLL and HLLC as
$h\approx\tfrac12\big(f(u^-)+f(u^+)-\lvert\tilde a_{i+1/2}\rvert(u^+-u^-)\big)$ with a
solver-dependent averaged signal speed ([HLL-family solvers](/methods/hll-riemann-solvers.md)).

## Roe averages

For the Euler equations, as printed by [Ji et al. (2022)](/sources/ji-2022.md) (Eq. (36)) for
the wave speeds of their HLL flux, with $D_\rho=\sqrt{\rho^+/\rho^-}$ (page-local):

$$\hat v=\frac{v^-+v^+D_\rho}{1+D_\rho},\qquad \hat H=\frac{H^-+H^+D_\rho}{1+D_\rho},\qquad \hat c=\sqrt{(\gamma-1)\big(\hat H-\tfrac12\hat v^2\big)} .$$

The same averages supply the eigenvectors of most
[characteristic decompositions](/methods/characteristic-decomposition.md) in the bundle and
the Einfeldt speed bounds of HLLE, $s^-=\min(v^--c^-,\hat v-\hat c)$,
$s^+=\max(v^++c^+,\hat v+\hat c)$ (Ji et al., Eq. (35)); [Hu et al. (2022)](/sources/hu-2022.md)
(Eq. (2.6)) also include $0$ in the minimum and the maximum, so that the flux is fully upwind
in supersonic flow. Sciacovelli et al. avoid the Roe matrix in their dissipation because the Roe
average has no unique, cheap extension to real and multi-species gases (§3).

## Relation to HLL-type solvers

Hu et al. (2022) (§2.3) state that HLLEM, i.e. HLLE plus anti-diffusion on the entropy and
shear waves with Roe-averaged eigenvectors, "is equivalent to the standard Roe solver" for
appropriate anti-diffusion parameters and wave speeds, and, citing earlier work, that HLLEM is
cheaper than Roe, lets the dissipation on the nonlinear waves be adjusted through
$s^-,s^+$, and is free of Roe's sonic-point glitch and expansion shocks (§1). Like Roe and
HLLC, HLLEM resolves contacts and shear layers sharply and suffers shock instabilities at
strong grid-aligned shocks ([carbuncle phenomenon](/definitions/carbuncle-phenomenon.md)).
[Lesur et al. (2023)](/sources/lesur-2023.md) (§2.3) order the Riemann solvers of IDEFIX "from
most to least diffusive" as Rusanov, HLL, HLLC (HLLD in MHD), Roe, all selectable at run time;
on linear MHD waves with linear reconstruction and RK2 all four are second order and within
small factors of each other in error (Fig. 7).

## Entropy fix

Hu et al. (2022) (§1, citing earlier work) list the sonic-point glitch and expansion shocks
among Roe's defects; the sources that use the solver add an entropy fix:

- [Huang & Zahr (2022)](/sources/huang-2022.md) (§6.3–6.4) use a smoothed Roe flux with the
  Harten–Hyman entropy fix as the upwind DG flux of their implicit shock-tracking residual for
  the Euler and quasi-1D Euler equations ([implicit shock tracking](/methods/implicit-shock-tracking.md));
- [Basile et al. (2022)](/sources/basile-2022.md) (§2.3) use Roe's flux with a Harten-type
  entropy fix in the DG solver CODA ([hp-adaptation](/methods/hp-adaptation.md));
- [Mossier et al. (2022)](/sources/mossier-2022.md) (§8) use Roe with the Harten–Hyman entropy
  fix in FLEXI for the Sod, Shu–Osher and transonic-airfoil cases, and HLLE for the double Mach
  reflection and forward-facing step ([FLEXI](/software/flexi.md));
- the finite-difference TENO studies switch from Rusanov flux splitting to a Roe flux with
  entropy fix for the [Woodward–Colella blast waves](/benchmarks/woodward-colella-blast-wave.md):
  [Fu (2021)](/sources/fu-2021.md) (§5.5), [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md)
  (§4.4, CFL 0.35) and [Liang et al. (2022)](/sources/liang-2022.md) (§4.3, where TENO5 needs
  $C_T=10^{-4}$ to run stably).

The fix itself is not written out in any of these sources.

## Uses in the sources

| Source | Discretization | Use |
|---|---|---|
| [Hong et al. (2022)](/sources/hong-2022.md) | FD WENO/TENO comparison | default flux for systems; van Leer flux-vector splitting for the double Mach reflection and 2D Riemann problems |
| [Lesur et al. (2023)](/sources/lesur-2023.md) | second-order Godunov FV, HD and MHD (IDEFIX) | linearized Roe solver of Cargo and Gallice for MHD; Sod tube (Roe, linear, RK2, 500 points), Brio–Wu tube, magnetized rotor; RK3 + PPM + Roe is the most accurate Orszag–Tang combination at a given resolution (§4.1–4.2, Figs. 2, 6, 9–11) |
| [Huang & Zahr (2022)](/sources/huang-2022.md) | high-order implicit shock tracking (DG) | smoothed Roe flux with Harten–Hyman fix |
| [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) | FD adaptive TENO | blast waves and Rayleigh–Taylor (§4.4, §4.7) |
| [Liang et al. (2022)](/sources/liang-2022.md) | FD TENO with THINC switch | blast waves (§4.3) |
| [Fu (2021)](/sources/fu-2021.md), [Takagi et al. (2022)](/sources/takagi-2022.md) | FD TENO, TENO-THINC | Rayleigh–Taylor with Rusanov and Roe fluxes ([Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md)) |
| [Basile et al. (2022)](/sources/basile-2022.md) | modal DG (CODA) | convective flux with Harten-type fix |

## Qualifications

- **Carbuncle.** Fu (2023) (§3.6) states that HLLC and Roe "may induce carbuncle problem in
  proximity to strong shockwaves with low numerical dissipation", while HLL is free of it but
  much more dissipative; Hu et al. (2022) list Roe with HLLC and HLLEM as shock-unstable (§1).
  None of the sources analyses Roe's instability itself; Hu et al.'s linear analysis is of
  HLLEM ([carbuncle phenomenon](/definitions/carbuncle-phenomenon.md)).
- Lesur et al.'s diffusivity ordering is a stated heuristic; their own linear-wave errors
  differ only by small factors (Fig. 7).
- Hong et al. print the 1981 Roe reference with a DOI of 1997 form (ref. [24]); the reference
  is not relied on here.

# Citations

- [Hu et al. (2022)](/sources/hu-2022.md) — §1, §2.2–2.3 (Eqs. (2.5)–(2.8)).
- [Ji et al. (2022)](/sources/ji-2022.md) — Eqs. (35)–(36).
- [Lesur et al. (2023)](/sources/lesur-2023.md) — §2.3, §4.1–4.2 (Figs. 2, 6, 7, 9–11).
- [Hong et al. (2022)](/sources/hong-2022.md) — §2, §5 (baseline schemes), ref. [24].
- [Huang & Zahr (2022)](/sources/huang-2022.md) — §6.3–6.4.
- [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) — §4.4, §4.7.
- [Liang et al. (2022)](/sources/liang-2022.md) — §4.3.
- [Fu (2023)](/sources/fu-2023.md) — §3.6 (Eq. (29)).
- [Fu (2021)](/sources/fu-2021.md) — §5.5.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §4.7.
- [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) — §3 (Eqs. (20)–(22)) (arXiv v1).
- [Basile et al. (2022)](/sources/basile-2022.md) — §2.3.
- [Mossier et al. (2022)](/sources/mossier-2022.md) — §8.
