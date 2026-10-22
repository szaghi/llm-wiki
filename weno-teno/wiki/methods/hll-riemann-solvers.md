---
type: Method
title: "HLL-family approximate Riemann solvers"
description: "HLL, HLLE, HLLC and HLLEM/HLLI two-point fluxes as the bundle's sources use them: the single-state HLL form and its non-conservative and anti-diffusive extensions, positivity and CFL properties, carbuncle behaviour, and the switching of low- and high-dissipation solvers in high-order schemes."
status: established
aliases: [HLL flux, HLLE, HLLC, HLLEM, HLLI, Harten–Lax–van Leer solver]
tags: [riemann-solver, numerical-flux, finite-volume, positivity]
timestamp: 2026-10-21T00:00:00Z
---

# HLL-family approximate Riemann solvers

The HLL solver approximates the Riemann fan at $x_{i+1/2}$ by two waves of speeds
$s^-\le s^+$ enclosing a single constant state. The bundle's sources use it, and its
relatives HLLE, HLLC and HLLEM/HLLI, as the two-point flux $h(u^-,u^+)$ of finite-volume and
DG schemes, as the building block of [fluctuation-form FD-WENO](/methods/fluctuation-form-fd-weno.md),
and as the carbuncle-free fallback near strong shocks.

## The single-state HLL solver

As printed by [Balsara et al. (2024)](/sources/balsara-2024.md) (§III, Eqs. (3.1), (3.6),
without non-conservative products), the resolved state and the flux are

$$u^{\mathrm{HLL}}_{i+1/2}=\frac{s^+u^+-s^-u^--\big(f(u^+)-f(u^-)\big)}{s^+-s^-},$$

$$h^{\mathrm{HLL}}(u^-,u^+)=\begin{cases}f(u^-),& s^-\ge0,\\ \dfrac{s^+f(u^-)-s^-f(u^+)+s^+s^-(u^+-u^-)}{s^+-s^-},& s^-<0<s^+,\\ f(u^+),& s^+\le0,\end{cases}$$

(page-local $u^{\mathrm{HLL}}$). In fluctuation form the subsonic case splits the jump into
$s^-(u^{\mathrm{HLL}}-u^-)$ (left-going) and $s^+(u^+-u^{\mathrm{HLL}})$ (right-going). Balsara
et al. note that the HLL solver lets $s^-$ be decreased and $s^+$ increased "within some
reasonable physical limits" and still produce good results — the property their FD-WENO uses
to extremize the speeds over all contributing stencils (§III, §IV) — and that the
[Lax–Friedrichs](/methods/lax-friedrichs-flux.md) solver is its special case $s^\pm=\pm a$
(§III).

*Compiler check, not in the sources:* the subsonic HLL flux above is term by term the
[central-upwind](/methods/central-upwind-scheme.md) flux with $s^\pm=a^\pm$, and the
intermediate state of the central-upwind anti-diffusion of
[Wang et al. (2023)](/sources/wang-2023-b.md) (Eq. (5)) is $u^{\mathrm{HLL}}$ with the same
speeds.

[Fu (2023)](/sources/fu-2023.md) (§3.6, Eq. (29)) writes Roe, Rusanov, HLL and HLLC fluxes in
one form, $h\approx\tfrac12\big(f(u^-)+f(u^+)-\lvert\tilde a_{i+1/2}\rvert(u^+-u^-)\big)$, with
$\tilde a_{i+1/2}$ an averaged characteristic signal speed set by the solver (page-local;
the source's $\tilde\partial$), and remarks that all of them scale with the sound or
convection speed.

## Non-conservative products and anti-diffusion (HLLEM/HLLI)

For $\partial_tu+\partial_xf+\mathcal C(u)\partial_xu=0$ the resolved state acquires
path-integrated $\mathcal C$ terms and becomes implicit; Balsara et al. solve it by fixed-point
iteration (Eqs. (3.1)–(3.5)). The anti-diffusive term of Dumbser & Balsara (2016), restricted
to linearly degenerate fields and weighted so that stationary waves receive the most
anti-diffusion, restores the intermediate waves that the single-state solver smears, and
makes stationary contacts exact (Eqs. (3.7)–(3.9)). Balsara et al. call the result "HLLI";
the title of Dumbser & Balsara (2016) calls it HLLEM. Details on
[fluctuation-form FD-WENO](/methods/fluctuation-form-fd-weno.md) and
[stationary contact preservation](/properties/stationary-contact-preservation.md).
[Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md) (§4) state that HLLE and HLLEM
preserve positivity of density and pressure.

## Positivity and the bound-preserving CFL

- [Cui et al. (2024)](/sources/cui-2024.md) (§7, Eq. (7.5), Remark 7.7) use the maximum CFL
  number $c_0$ of the first-order bound-preserving three-point scheme: $c_0=1$ for
  Lax–Friedrichs and $c_0=\tfrac12$ for HLL and HLLC (cited from earlier work). The
  bound-preserving time step of a high-order scheme is $c_0$ times the boundary weight of the
  [cell-average decomposition](/methods/optimal-cell-average-decomposition.md); with
  $c_0=\tfrac12$ it is the binding constraint, though still much milder than with the classic
  decomposition ([bound preservation](/properties/bound-preservation.md)).
- In subcell limiting of DGSEM, replacing the local Lax–Friedrichs low-order flux by HLLE
  keeps positivity, but the bar-state bounds of the invariant-domain-preserving scheme no
  longer apply, since they belong to Lax–Friedrichs graph-Laplacian dissipation
  ([Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md), §4 item (3), §5.2.3). On the
  Mach-2000 [astrophysical jet](/benchmarks/high-mach-astrophysical-jet.md) shock resolution
  and small scales improve from first-order FV with LLF to first-order FV with HLLE to
  second-order FV with HLLE (Figs. 8–9); the bounds are then kept "in the absence of better
  bounds" without a guarantee.

## Dissipation, carbuncle and solver switching

[Fu (2023)](/sources/fu-2023.md) (§3.6) states that no Riemann solver handles all Mach
numbers: HLLC and Roe may produce the [carbuncle](/definitions/carbuncle-phenomenon.md) near
strong shocks because of their low dissipation, while HLL is free from it but substantially
more dissipative. Finite-volume Riemann solvers, designed for discontinuities, are
over-dissipative for smooth flow; the low-dissipation finite-volume TENO therefore switches,
per interface,

$$h_{i+1/2}=\begin{cases}h^{\mathrm{low}}(u^-,u^+),&\text{both full reconstruction stencils smooth},\\ h^{\mathrm{high}}(u^-,u^+),&\text{otherwise},\end{cases}$$

using the TENO smoothness flag of the full stencil (Eq. (30)); e.g. HLLC as $h^{\mathrm{low}}$ and
HLL as $h^{\mathrm{high}}$, while for turbulence the non-dissipative central flux is "generally
preferred" as $h^{\mathrm{low}}$. Reproduced results: better wave resolution on the
Titarev–Toro problem with 1000 points (Fig. 9). See [targeted ENO](/methods/targeted-eno.md).

[Huang et al. (2026)](/sources/huang-2026.md) use HLLC by default in their compact-stencil
finite-volume tests and HLL for the [double Mach reflection](/benchmarks/double-mach-reflection.md)
"to mitigate the carbuncle phenomenon", HLLC being "known to exhibit numerical instabilities
in the presence of strong shock waves" (§6.7). In the
[alternative-formulation TENO](/methods/afteno.md) of [Ye et al. (2022)](/sources/ye-2022.md),
where any monotone two-point flux can be used, HLLC gives the best dissipation-rate results
on the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) and beats Steger–Warming
splitting in both alternative-formulation schemes (§4.9, Figs. 10–12).

## Cost

In the flux microbenchmarks of [Ranocha et al. (2023)](/sources/ranocha-2023.md) (§4.2,
Table 2) the local Lax–Friedrichs and HLL surface fluxes cost between the cheap
kinetic-energy-preserving and the expensive entropy-conservative volume fluxes. In 3D the
directional HLL flux is slightly *faster* than the Cartesian one (22.9 vs 23.3 ns), against
the text's general statement that Cartesian fluxes are 5–20 % faster.

# Citations

- [Balsara et al. (2024)](/sources/balsara-2024.md) — §III (Eqs. (3.1)–(3.9)), §IV (accepted manuscript).
- [Fu (2023)](/sources/fu-2023.md) — §3.6 (Eqs. (29)–(30), Fig. 9).
- [Huang et al. (2026)](/sources/huang-2026.md) — §6 (default HLLC), §6.7 (DMR with HLL).
- [Cui et al. (2024)](/sources/cui-2024.md) — §7 (Eq. (7.5), Remark 7.7, Fig. 12) (arXiv v1).
- [Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md) — §4, §5.2.3 (Figs. 8–9) (arXiv v2).
- [Ye et al. (2022)](/sources/ye-2022.md) — §3, §4.9 (Figs. 10–12).
- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — §4.2, Table 2 (arXiv v2).
- [Wang et al. (2023)](/sources/wang-2023-b.md) — Eq. (5) (intermediate state).
