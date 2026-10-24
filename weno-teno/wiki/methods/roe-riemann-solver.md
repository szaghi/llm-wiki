---
type: Method
title: "Roe approximate Riemann solver"
description: "Roe's solver upwinds every characteristic field of a linearized flux Jacobian at the Roe-averaged state; in the bundle's sources it is the least diffusive option of finite-volume codes, the default flux of several WENO and TENO tests, used with a Harten–Hyman-type entropy fix, prone to the carbuncle, and, in a Lagrangian acoustic form, a particle-pair solver."
status: established
aliases: [Roe flux, Roe scheme, Roe solver, linearized Riemann solver, Roe–Harten flux]
tags: [riemann-solver, numerical-flux, characteristic, finite-volume]
timestamp: 2026-10-23T20:07:00Z
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
  (§4.4, CFL 0.35), [Liang et al. (2022)](/sources/liang-2022.md) (§4.3, where TENO5 needs
  $C_T=10^{-4}$ to run stably) and the hybrid TENO-S of
  [Liang & Fu (2024b)](/sources/liang-2024-b.md) (§4.4), "to obtain a stable result".

The fix itself is not written out in any of these sources.

## Uses in the sources

| Source | Discretization | Use |
|---|---|---|
| [Hong et al. (2022)](/sources/hong-2022.md) | FD WENO/TENO comparison | default flux for systems; van Leer flux-vector splitting for the double Mach reflection and 2D Riemann problems |
| [Lesur et al. (2023)](/sources/lesur-2023.md) | second-order Godunov FV, HD and MHD (IDEFIX) | linearized Roe solver of Cargo and Gallice for MHD; Sod tube (Roe, linear, RK2, 500 points), Brio–Wu tube, magnetized rotor; RK3 + PPM + Roe is the most accurate Orszag–Tang combination at a given resolution (§4.1–4.2, Figs. 2, 6, 9–11) |
| [Huang & Zahr (2022)](/sources/huang-2022.md) | high-order implicit shock tracking (DG) | smoothed Roe flux with Harten–Hyman fix |
| [Naudet & Zahr (2024)](/sources/naudet-2024.md) | space-time implicit shock tracking (DG on space-time slabs) | Roe flux in space-time form, eigenvalues shifted by the time component of the normal |
| [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) | FD adaptive TENO | blast waves and Rayleigh–Taylor (§4.4, §4.7) |
| [Liang et al. (2022)](/sources/liang-2022.md) | FD TENO with THINC switch | blast waves (§4.3) |
| [Fu (2021)](/sources/fu-2021.md), [Takagi et al. (2022)](/sources/takagi-2022.md) | FD TENO, TENO-THINC | Rayleigh–Taylor with Rusanov and Roe fluxes ([Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md)) |
| [Basile et al. (2022)](/sources/basile-2022.md) | modal DG (CODA) | convective flux with Harten-type fix |
| [Berta et al. (2024)](/sources/berta-2024.md) | fourth-order FV, MHD and relativistic MHD (PLUTO) | one of six solvers on pointwise-reconstructed face states; Orszag–Tang runs with Roe or HLLD and UCT-HLLD electric fields (§3.3, §5.6) |
| [Ren et al. (2025)](/sources/ren-2025.md) | FV WENO-Z, 2D Euler, shock-instability analysis | smoothed Roe flux in the matrix stability analysis; unstable at first to fifth order on a strong normal shock |
| [Cai, Qiu & Wu (2024)](/sources/cai-2024.md) | FV Hermite WENO, relativistic hydrodynamics | no Roe flux (global Lax–Friedrichs); the eigenvectors of the Eulderink–Mellema Roe matrix, rescaled, for the characteristic reconstruction (§3.1.3, Remark 3.3) |

## Shock instability at first to fifth order

[Ren et al. (2025)](/sources/ren-2025.md) (§3–§4) use the Roe flux as the main test case of their
[matrix stability analysis](/methods/matrix-stability-analysis.md) of finite-volume schemes on a
Mach-20 steady normal shock with one intermediate cell ($11\times11$ cells, intermediate-state
position $\varepsilon_{\mathrm s}\in[0,1]$, page-local as on the carbuncle page). To make the flux
differentiable at the mean state they smooth the absolute Roe-averaged eigenvalues
$\hat v_1-\hat c,\hat v_1,\hat v_1,\hat v_1+\hat c$ by $\lvert\lambda\rvert\to(\lambda^2+\delta_0^2)/(2\delta_0)$ for
$\lvert\lambda\rvert<\delta_0=10^{-4}$, after Shen, Yan and Yuan, and state that Roe is differentiable when
the shock does not sit exactly between two cells (§3.3, Eqs. (32)–(33)). When the 1D Roe solution is
itself unstable, the mean flow uses Xie et al.'s mass-flux consistency fix across the shock
(Eq. (37)). Findings (§4.1.1, Table 2, Figs. 9–13): with fifth-order WENO-Z the Roe scheme is stable
only for $\varepsilon_{\mathrm s}=0.8$ and $0.9$; at $\varepsilon_{\mathrm s}=0.1$ its largest growth rate
lies between the first-order and the second-order (MUSCL, van Albada) rates, and the run collapses
at $t=47.8$, at $t=42.2$ with two-point Gauss face integration, whose growth rate is lower. The
predicted growth rate matches the measured one within 0.59% with the smoothing and 21.88% without
it (Table 1). Fifth-order Roe on the transverse faces with first-order van Leer splitting on the
normal faces is unstable, and so is the reverse (§4.2).

## Space-time form

[Naudet & Zahr (2024)](/sources/naudet-2024.md) (§2.1–2.2, Eqs. (2)–(17)) write the generic
linearized-Riemann-solver flux across a face with unit spatial normal $\hat n_x$ as
$\tfrac12\big(f_x(u_{\mathrm{in}})+f_x(u_{\mathrm{ex}})\big)\hat n_x+\tfrac12\tilde A(u_{\mathrm{in}}-u_{\mathrm{ex}})$,
with $f_x$ the $m\times d'$ spatial flux (columns $f^{(d)}$), $u_{\mathrm{in}}$, $u_{\mathrm{ex}}$ the
interior and exterior traces of the element and $\tilde A$ a dissipation matrix (page-local; the
sign of the jump term follows from taking the interior trace first). Roe takes
$\tilde A=\lvert A_x(\hat u,\hat n_x)\rvert=\hat R\lvert\hat\Lambda_x\rvert\hat R^{-1}$, the projected
Jacobian $A_x=\partial(f_x\hat n_x)/\partial u$ at the Roe average $\hat u$ with its eigenvector and
eigenvalue matrices $\hat R$, $\hat\Lambda_x$ (page-local); Rusanov takes the largest eigenvalue
modulus of the two traces times the identity, Vijayasundaram the Jacobian at the arithmetic mean
(Remark 2). Smoothed and entropy-fixed versions replace $\lvert\cdot\rvert$ by a smoothed absolute
value or an entropy fix (Remark 3).

For a time-dependent law rewritten as a steady law on a space-time slab, with space-time flux
$[f_x(u)\ \ u]$ and space-time unit normal $n=(n_x,n_t)$, $n_x=\lVert n_x\rVert\hat n_x$
(page-local), the projected space-time Jacobian is

$$A_{xt}(u,n)=\lVert n_x\rVert\,A_x(u,\hat n_x)+n_t\,I,\qquad \Lambda_{xt}=\lVert n_x\rVert\Lambda_x+n_tI,\qquad R_{xt}=R$$

(Eqs. (10)–(12)), so the space-time Roe flux uses
$\tilde A=\hat R\big\lvert\lVert n_x\rVert\hat\Lambda_x+n_tI\big\rvert\hat R^{-1}$ (Eq. (15)): the
eigenvectors are those of the spatial problem and only the eigenvalues shift by $n_t$. The authors
call this the removal of "one of the implementation burdens associated with space-time methods".
They use the Roe flux in the space-time [implicit shock tracking](/methods/implicit-shock-tracking.md)
of Burgers, shallow-water and Euler problems, with Roe averages and eigen-decompositions of the
shallow-water and Euler Jacobians derived with Maple (§5, App. A).

## Lagrangian acoustic form between particles

[Jiang et al. (2024)](/sources/jiang-2024.md) (§3.1, Eqs. (9a)–(9c)) stabilize a meshless
Lagrangian weighted-least-squares (LWLS) particle method by solving, for every particle pair
$(i,n)$, a 1D Riemann problem along the unit vector $\mathbf e_{ni}$ from $i$ to $n$, with left
state at $i$, right state at $n$ and normal velocities $v_{\mathrm n}=v\cdot\mathbf e_{ni}$
(page-local). They call the intermediate states, taken from earlier SPH work, "Roe's Lagrangian
intermediate states":
$$p^*=\tfrac12\big[p_L+p_R+C_{LR}(v_{\mathrm n,L}-v_{\mathrm n,R})\big],\qquad v^*=\tfrac12\Big[v_L+v_R+\frac{p_L-p_R}{C_{LR}}\,\mathbf e_{ni}\Big],\qquad C_{LR}=\tfrac12(\rho_Lc_L+\rho_Rc_R),$$
where $C_{LR}$, called an average Lagrangian sound speed, is a mean acoustic impedance.
*(compiler check, not in the sources: with equal impedances $C_L=C_R=C_{LR}$ these are the
primitive-variable Riemann-solver states $p^*$ and $s^*$ (the normal component of $v^*$) of [Wang et al. (2022a)](/sources/wang-2022.md)
recorded on [HLL-family solvers](/methods/hll-riemann-solvers.md).)* The states replace the
neighbour values in the least-squares right-hand side of the derivative fit (LWLS-RR). The
authors report LWLS-RR smooth but "about first-order or lower" near non-uniform particles
(Remark 1); on smooth density waves it converges at order about 2.0, and with WENO-Z+-type
left and right states reconstructed along the pair line (LWLS-WENO-Z) at 2.2–2.35, about five
times dearer (§4.1, Tables 1–2, §5.2.1; [WENO-Z+](/methods/weno-z-plus.md)). On the bubble
collapse near a wall LWLS-RR is too dissipative to reproduce the bubble's depression and the
micro-jet that LWLS-WENO-Z gives (§5.2.3, Fig. 14).

## Qualifications

- **Carbuncle.** Fu (2023) (§3.6) states that HLLC and Roe "may induce carbuncle problem in
  proximity to strong shockwaves with low numerical dissipation", while HLL is free of it but
  much more dissipative; Hu et al. (2022) list Roe with HLLC and HLLEM as shock-unstable (§1).
  Hu et al.'s linear analysis is of HLLEM; the analysis of the Roe flux itself is Ren et al.'s
  (2025), below ([carbuncle phenomenon](/definitions/carbuncle-phenomenon.md)).
- Lesur et al.'s diffusivity ordering is a stated heuristic; their own linear-wave errors
  differ only by small factors (Fig. 7).
- Hong et al. (ref. [24]) and Ren et al. (2025) (ref. [72]) print the 1981 Roe reference with a
  DOI of 1997 form; the reference is not relied on here.

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
- [Berta et al. (2024)](/sources/berta-2024.md) — §3.3, §5.6 (arXiv v4).
- [Jiang et al. (2024)](/sources/jiang-2024.md) — §3.1 (Eqs. (9a)–(10e), Remark 1), §4.1 (Tables 1–2), §5.2.1, §5.2.3 (Fig. 14).
- [Cai, Qiu & Wu (2024)](/sources/cai-2024.md) — §3.1.3, Remark 3.3 (arXiv v1).
- [Liang & Fu (2024b)](/sources/liang-2024-b.md) — §4.4.
- [Naudet & Zahr (2024)](/sources/naudet-2024.md) — §2.1–2.2 (Eqs. (2)–(17), Remarks 2–5), §5, App. A.
- [Ren et al. (2025)](/sources/ren-2025.md) — §3.2–3.3 (Eqs. (32)–(33), (37), Table 1), §4.1.1 (Table 2, Figs. 9–13), §4.2, ref. [72].
