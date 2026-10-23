---
type: Source
title: "Dematté et al. (2024) — An all Mach number scheme for visco-resistive magnetically-dominated MHD flows"
description: "Cell-centred semi-implicit finite-volume scheme for ideal and visco-resistive MHD: an MHD flux-vector splitting with an explicit advective part and an implicit pressure part, solved by nested Picard iterations and GMRES, with staggered or vector-potential constrained transport and a time step set by the flow speed alone."
resource: "doi:10.1016/j.jcp.2024.113229"
source_kind: paper
authors: [Dematté R., Farmakalides A.A., Millmore S., Nikiforakis N.]
year: 2024
venue: "J. Comput. Phys. 514:113229"
local_file: "/home/stefano/papers/mosaic/weno-teno/2024_Crossref_Journal_of_Computational_Physics_Dematté_An_all_Mach_number_scheme_for_visco-resistive_magnetically-d.pdf"
tags: [mhd, semi-implicit, all-mach, finite-volume, navier-stokes]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

The paper builds a conservative, cell-centred,
[semi-implicit all-Mach](/methods/semi-implicit-all-mach-scheme.md)
finite-volume scheme for ideal and visco-resistive MHD whose time step depends
only on the fluid velocity, so that it stays efficient at low Mach number in
both gas-pressure- and magnetic-pressure-dominated regimes; the motivating
application is disruption events in magnetic-confinement fusion. The flux is
split with the MHD flux-vector splitting of Balsara, Montecinos and Toro
(2016), the analogue of the Toro–Vázquez splitting: an advective sub-system
with eigenvalues $0$ and $v_1$, and a "pressure" sub-system holding the gas
pressure, the magnetic pressure and the non-advective magnetic terms. The
advective part is updated explicitly with a [Rusanov flux](/methods/lax-friedrichs-flux.md)
whose dissipation scales with $\lvert v_1\rvert$ only (first order or
MUSCL–Hancock with the van Leer limiter). The pressure part is solved
implicitly by nested Picard iterations: a main loop that contains a loop for
the magnetic field (pressure frozen, provisional momentum) and a loop for the
pressure (field frozen), each a linear system solved by matrix-free GMRES
without preconditioning, two iterations per loop in all tests. Viscous,
resistive and heat-flux terms are also implicit inside the pressure
sub-system. The [divergence constraint](/properties/divergence-free-magnetic-field.md)
is enforced in every magnetic iteration either by a staggered adaptation of
Gardiner–Stone constrained transport or by an unstaggered adaptation of
Rossmanith's vector-potential method; both keep $\nabla\cdot B$ at machine
precision.

Validation: the [Brio–Wu](/benchmarks/brio-wu-shock-tube.md) and three other
1D Riemann problems, second-order spatial convergence and a $t=1000$
stationary run of the [magnetized vortex](/benchmarks/magnetized-vortex.md),
the [MHD rotor and blast wave](/benchmarks/mhd-blast-wave.md), the
[Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md), a low-Mach
[field loop](/benchmarks/field-loop-advection.md) and $\theta$-pinch
equilibria (about two orders of magnitude fewer steps than an explicit
MUSCL–HLLEM–CT scheme), a viscous shear layer and resistive current sheet, a
visco-resistive [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md),
and an MHD [lid-driven cavity](/benchmarks/lid-driven-cavity.md) with a new
accelerating-lid variant that passes from very low Mach to $M\simeq2$ and
back. Stability under the velocity-based time step is shown numerically, not
proved.

# Version read

Version of record (Elsevier typeset, open access CC BY, J. Comput. Phys. 514
(2024) 113229), 36 pages, all read; pp. 5–10, 12–16 and 19–20 read visually
because the text layer garbles the equations. Page 1 matches Crossref (title,
four authors, venue, DOI). The online supplement with example code for the
matrix coefficients was not read (not in the archive). Equation, table and
figure numbers cited here are those of this version.

# Key claims

Registry notation (see the notation map): the source's velocity
$u=(u,v,w)$ is $v=(v_1,v_2,v_3)$, its sound speed $a$ is $c$, its kinetic
energy $k$ is $\kappa$, its CFL number is $\nu$, its resistivity $\eta$ is
written $\eta_{\mathrm r}$.

1. The flux-vector splitting adopted (Eq. (15)) gives an advective sub-system with eigenvalues $0$ (double) and $v_1$ (Eq. (17)) and a pressure sub-system with eigenvalues $0,0,\mp\lvert B_x\rvert/\sqrt\rho$ and $\tfrac12\big[v_1\mp\sqrt{v_1^2+4(c^2+(\gamma-1)(B_y^2+B_z^2)/\rho)}\big]$ (Eq. (19)); the pressure sub-system is always subsonic (§2.1). **Stated** (eigenstructure referred to Balsara, Montecinos and Toro)
2. Nothing guarantees that the "fast" eigenvalues of the pressure sub-system bracket the true fast magnetosonic speeds; for Toro–Vázquez in Euler, $(v_1+\sqrt{v_1^2+4c^2})/2>v_1+c$ "does not always hold true" (§2.1). **Stated**
3. With all magnetic terms of the pressure sub-system implicit, the time step is independent of the Alfvén and fast speeds, provided the Picard iterations converge; there is "no rigorous proof" of stability under the advective CFL condition (§2.1). **Stated** (supported numerically in §4)
4. Unlike Dumbser et al. (2019), which keeps the magnetic terms explicit and is limited by the Alfvén speed, the scheme stays efficient in magnetically dominated flows (§1, §2.1). **Stated**; **Shown** in §§4.2.2–4.2.3
5. The Rusanov dissipation of the advective flux is proportional to the flow speed only, $s^{\max}_{i+1/2,j}=\max(\lvert v_1^-\rvert,\lvert v_1^+\rvert)$ (Eqs. (22)–(23)) (§3.1). **Stated**
6. $\Delta t=\nu/(\max\lvert\lambda_x\rvert/\Delta x+\max\lvert\lambda_y\rvert/\Delta y)$ with the advective eigenvalues (Eq. (24)), $\nu=0.8$ unless stated; a magnetosonic explicit step is used first when the initial velocity is zero or small (§3.1, §4). **Stated**
7. Splitting the Picard iteration into magnetic and pressure sub-steps "does not comprise an additional flux vector splitting": the full pressure sub-system enters every iteration (§3.2). **Stated**
8. Both linear systems (33) and (37) are non-symmetric and less sparse than staggered ones; matrix-free GMRES (tolerance $10^{-15}$) converges without preconditioning in all tests (§3.2.3). **Shown** (§4.5)
9. Picard tolerance $10^{-12}$ (Eq. (38)); in practice two iterations per loop are a good compromise, with residuals after the main loop in $[10^{-12},10^{-4}]$ for Orszag–Tang, Kelvin–Helmholtz and the field loop (§3.2.3, §4.5, Fig. 21). **Shown**
10. The velocity-weighted face averages of $B_x/\rho$, $B_y/\rho$ (Eq. (32)) and of the total enthalpy (Eq. (36)) give no significant difference from arithmetic averages, and neither produces checkerboard instabilities (§3.2.1). **Shown** (asserted from tests, no figure)
11. The staggered CT adaptation (Eqs. (39)–(46)) preserves the face-based discrete divergence (40) exactly, and the averaged cell field satisfies the corner divergence (47) (§3.3.1). **Derived**
12. The unstaggered adaptation of Rossmanith's vector-potential method enforces the central divergence (50) through $B$ computed from the potential (Eq. (49)) (§3.3.2). **Derived** (see Printed slips for the sign of $B_y$ in Eq. (49))
13. Both CT adaptations keep $\lVert\nabla\cdot B\rVert_{L^2}$ near machine precision through the MHD rotor run (§4.1.4, Fig. 8). **Shown**
14. For RP3 and RP4 the purely advective time step is less accurate than an Alfvénic one; lowering $\nu$ (0.8, 0.5, 0.4) slightly improves accuracy, so the time step is dictated by accuracy as well as stability (§4.1.1, Figs. 2–3). **Shown**
15. Second-order spatial convergence on the smooth MHD vortex with fixed $\Delta t=0.01$ and unlimited MUSCL–Hancock: $L_2(\rho)$ orders 1.573, 1.854, 1.966, 1.992, 1.998 from $16^2$ to $512^2$, $L_2(\rho)=3.647\times10^{-5}$ on $512^2$ (§4.1.2, Table 2). **Shown** ("second order of accuracy in space" with $\Delta t$ fixed; "higher order of accuracy in time" with IMEX Runge–Kutta is left to future work)
16. The stationary vortex is preserved to $t=1000$ on $200^2$ cells with $\nu=0.45$, with both CT variants (§4.1.3, Figs. 4–5). **Shown**
17. Low-Mach field loop ($M\approx0.006$): 960 time steps and 2930 s wall-clock against 240427 steps and 85340 s for an explicit second-order MUSCL–HLLEM–CT scheme, whose result is more diffuse (§4.2.1, Fig. 11). **Shown** (hardware not stated)
18. Static $\theta$-pinch ($B_0=8$): the scheme reaches $t=2$ in one time step; the explicit scheme needs 8833 steps and diffuses the profile (§4.2.2, Fig. 12). **Shown**
19. Advected $\theta$-pinch ($t=400$): 1150 against 117546 steps, 104 s against 4240 s ("a factor of 40 speed-up"); over $(B_z)_0\in\{1,2,4,8,16,32\}$ the semi-implicit error and wall time stay nearly constant while both grow for the explicit scheme, which at $(B_z)_0=32$ is nearly fully diffused and "around 250 times longer" (§4.2.3, Fig. 13). **Shown**
20. Viscous shear layer and resistive current sheet (with $B_z=10^4$) match the erf exact solution in 23 time steps, possible "only" because the pressure sub-system and the visco-resistive terms are implicit (§4.3.1, Fig. 14). **Shown**
21. Magnetic- and cross-helicity errors of the scheme on ideal Kelvin–Helmholtz are comparable to those of an explicit second-order divergence-free Godunov scheme; "no standard ideal MHD scheme is set up to enforce their exact conservation at the discrete level" (§4.3.2, Fig. 16). **Shown** / **Stated**
22. The MHD lid-driven cavity at $\nu=0.4$ with a velocity time step agrees "very well" with the hybrid FV/FE reference of Fambri et al. (2023) for $B_{x,0}=0.5$ and $1.0$ (§4.3.3, Figs. 17–18). **Shown**
23. The new accelerating-lid cavity passes from very low Mach to $M\simeq2$ at $t=10$ and back to low Mach by $t=20$; the results are "satisfactory based on physical intuition" (no reference solution) (§4.4, Figs. 19–20). **Shown** (qualitative)
24. GMRES needs fewer than ten iterations per step for both systems on Orszag–Tang and Kelvin–Helmholtz, about one hundred for the pressure system of the field loop (attributed to the low Mach number) (§4.5, Fig. 22). **Shown**
25. Shock-capturing results are "comparable in terms of both efficiency and accuracy to state-of-the-art second-order density-based Godunov-type finite-volume schemes" (§5). **Stated** (not quantified for shocks)
26. A cell-centred layout is chosen to ease sharp-interface (ghost-fluid) coupling with elastoplastic solids, where a staggered layout leaves interface quantities undefined (§1). **Stated**

# Printed slips

- Eq. (21): $U^\star_{i,j}=U^n_{i,j}+\frac{\Delta t}{\Delta x}\big(F^a_{i+1/2,j}-F^a_{i-1/2,j}\big)+\frac{\Delta t}{\Delta y}\big(G^a_{i,j+1/2}-G^a_{i,j-1/2}\big)$;
  consistency with $\partial_tU+\partial_xF^a=0$ (Eq. (16)) needs minus signs.
  Fig. 1 (top) likewise writes $U^\star=U^n+\Delta t\nabla\cdot F^a$ and
  $U^{n+1}=U^\star+\Delta t\nabla\cdot F^p$, while Fig. 1 (bottom) and Eq. (26)
  use $-\Delta t\nabla\cdot F^p$.
- Eq. (34): the semi-discrete energy update is printed with
  $+\Delta t\,\partial_x\big[(h+2m/\rho)(\rho u)-\tfrac{B_x}{\rho}(\rho u\cdot B)\big]$,
  the opposite sign of the fully discrete Eq. (35) and of
  $-\Delta t\,\partial_xF^p_E$ from Eq. (15).
- Eq. (39): $(B_x)_{i+1/2,j}=(B_x)^n_{i+1/2,j}+\frac{\Delta t}{\Delta y}\big[(E_z)_{i+1/2,j+1/2}-(E_z)_{i+1/2,j-1/2}\big]$
  and $(B_y)_{i,j+1/2}=(B_y)^n_{i,j+1/2}-\frac{\Delta t}{\Delta x}\big[\dots\big]$.
  With the paper's own $E=-v\times B$ (Eq. (11)), $E_z=v_2B_x-v_1B_y$ (Eq. (45))
  and $\partial_tB+\nabla\times E=0$ (Eq. (10)), $\partial_tB_x=-\partial_yE_z$
  and $\partial_tB_y=+\partial_xE_z$, so both signs are reversed; the
  divergence (40) is preserved with either sign. *(compiler check, not in the
  sources.)*
- §3.3.2: "$A=\nabla\times B$"; the vector potential is defined by
  $B=\nabla\times A$.
- Eqs. (49) and (51): $B_{y,i,j}=(A_{i+1,j}-A_{i-1,j})/(2\Delta x)$ lacks a minus
  sign. From $B=\nabla\times(A\hat z)$, $B_y=-\partial_xA$; with the printed
  sign the central divergence (50) of the field equals
  $(A_{i+1,j+1}-A_{i+1,j-1}-A_{i-1,j+1}+A_{i-1,j-1})/(2\Delta x\Delta y)\ne0$ in
  general, while with the minus sign it vanishes identically. *(compiler check,
  not in the sources.)*
- Eq. (63): the heat-flux Laplacian of $T$ is printed without the conductivity
  $\lambda$ that multiplies it in $\nabla\cdot F^{VR}$ (Eq. (52)).
- §2: "Here $c_p$ and $c_v$ are the heat capacities at constant volume and at
  constant pressure, respectively" (swapped); neither appears in Eq. (2), to
  which the sentence refers. §4.4 calls $\lambda$ "heat-capacity", defined in
  §3.4 as thermal conductivity.
- §§4.1.2–4.1.3, vortex pressure: the kinetic term is printed
  $-\frac12\big(\frac{\tilde\varepsilon}{2\pi}\big)^2e^{\frac12(1-r^2)}$, with an
  undefined $\tilde\varepsilon$. Radial balance $p'=\rho v_\theta^2/r-B_\theta^2/r-B_\theta B_\theta'$
  for $v_\theta=\frac{\varepsilon}{2\pi}re^{\frac12(1-r^2)}$,
  $B_\theta=\frac1{2\pi}re^{\frac12(1-r^2)}$, $\rho=1$ gives
  $p=1-\frac12\big(\frac{\varepsilon}{2\pi}\big)^2e^{1-r^2}+\frac12\big(\frac1{2\pi}\big)^2(1-r^2)e^{1-r^2}$:
  the magnetic term matches the printed one with $\tilde\mu=\sqrt{4\pi}$, the
  kinetic term carries $e^{1-r^2}$. *(compiler check, not in the sources.)*
- §4.2.3: $t=400$ is said to give "a full advection of the equilibrium profile
  once around the domain". *(Compiler check, not in the sources: with
  $v=(0.04,0.04,0)$ the displacement is 16 in each direction, about 2.7 periods
  of the $6\times6$ box.)*
- Eq. (17) labels the advective eigenvalues $\lambda^c$, the text $\lambda^a$;
  Eq. (52) writes $\rho E$ and $p_{mag}$ where Eq. (1) has $E$ and $p_{tot}$.
- "Gardinier and Stone" (pp. 2, 12, 23, 26) against "Gardiner and Stone"
  elsewhere; ref. [50] prints "Träauble", the text "Träuble".
- §4.3.3 prints no viscosity or resistivity for the MHD lid-driven cavity.

# Notation map

| Dematté et al. (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho$, $u=(u,v,w)$, $p$ | $\rho$, $v=(v_1,v_2,v_3)$, $p$ | **$u$ is both the velocity vector and its $x$-component; bold $v$ is the velocity vector in Eq. (15)** |
| $B=(B_x,B_y,B_z)$ | $B$ | magnetic field, units with $\mu_0=1$ |
| $U$, $F(U)$, $G$ | $u$, $f^{(1)}$, $f^{(2)}$ | conserved vector and fluxes |
| $F^a$, $F^p$; $G^a$ | kept | advective and pressure sub-system fluxes |
| $E=\rho e+k+m$ | $E$ | total energy per unit volume (magnetic part included) |
| $e$, $h=e+p/\rho$ | $e$, kept | specific internal energy, specific enthalpy |
| $k=\tfrac12\rho u^2$ | $\kappa$ | kinetic energy per unit volume |
| $m=\tfrac12B^2$, $p_{tot}=p+m$ | kept | magnetic and total pressure |
| $H=h+2m/\rho$ | kept | gas-plus-magnetic specific enthalpy; **not the registry's specific total enthalpy $H$** |
| $a$ | $c$ | sound speed, $c^2=\gamma p/\rho$ |
| $c_a$, $c_f$, $c_s$ | kept | Alfvén, fast and slow speeds |
| $\lambda^c$, $\lambda^a$, $\lambda^p$ | kept | eigenvalues of the advective and pressure sub-systems |
| $U^\star$ | kept | state after the explicit advective update |
| $U^{L}$, $U^{R}$ | $u^-$, $u^+$ | face states |
| $s^{max}$ | $a_{i+1/2}$ | Rusanov speed, here $\max(\lvert v_1^-\rvert,\lvert v_1^+\rvert)$ |
| $r,q,s$; $R,Q,S$ | kept | main, magnetic and pressure Picard indices and counts; **$q$ collides with the weight exponent, $R$, $Q$, $S$ with eigenvectors, SBP matrix and source** |
| $\tilde B$, $\tilde{(\rho u)}$ | kept | non-solenoidal predictor field, provisional momentum |
| $\tilde b_x$, $\tilde b_y$, $\tilde H$ | kept | face approximations of $B_x/\rho$, $B_y/\rho$ and $H$ |
| $\sigma$ | kept | Picard tolerance; also a Gaussian width in §4.4 |
| $E_z$, $\bar E_z$, $\tilde E_z$ | kept | corner, averaged and cell electric field; **$E$ also the total energy** |
| $A$ | kept | $z$-component of the vector potential; **$A$ is the flux Jacobian in the registry** |
| $\mu$, $\lambda$, $\eta$ | kept, kept, $\eta_{\mathrm r}$ | viscosity, conductivity, resistivity; **$\mu$ collides with the affine translation, $\lambda$ with the eigenvalues, $\eta$ with the entropy** |
| $\tau$, $\Phi$, $R$, $\Pi$ | kept | viscous stress, viscous work, resistive tensor, resistive work |
| $T$, $c_v$ | kept | temperature $p/(c_v(\gamma-1)\rho)$, heat capacity |
| CFL | $\nu$ | 0.8 by default |
| $\Delta t^a$, $\Delta t^{alv}$ | kept | advective and Alfvénic time steps |

# Reference list

86 printed references, numbered Elsevier style ([1]–[86]), all parsed and
merged complete into the [bibliography](/bibliography.md) with `citedby`
`dematte-2024`. Ref. [16] is the ingested Boscarino et al. (2022) paper. Ref.
[31] prints the journal "J. Appl. Math. Comput."; ref. [37] ends with "the
NIMROD Team"; ref. [39] has no pages; ref. [50] prints "Träauble"; ref. [52]
runs "Gmres" into the title; ref. [85] has no article number. Same-author
same-year works take suffixes in printed order (Boscheri 2021, Dumbser 2016).
No printed duplicates and no unparseable items.

# Pages created or updated

Chunk 8 (2026-10-23). This source is cited on:

* [Brio–Wu MHD shock tube](/benchmarks/brio-wu-shock-tube.md)
* [Constrained transport for the induction equation](/methods/constrained-transport.md)
* [Divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
* [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [Lid-driven cavity](/benchmarks/lid-driven-cavity.md)
* [Magnetic field-loop advection](/benchmarks/field-loop-advection.md)
* [Magnetized (MHD) vortex](/benchmarks/magnetized-vortex.md)
* [MHD blast wave and rotor](/benchmarks/mhd-blast-wave.md)
* [MUSCL and MUSCL–Hancock schemes](/methods/muscl-hancock.md)
* [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md)
* [Semi-implicit all-Mach schemes](/methods/semi-implicit-all-mach-scheme.md)
