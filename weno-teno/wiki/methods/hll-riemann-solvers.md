---
type: Method
title: "HLL-family approximate Riemann solvers"
description: "HLL, HLLE, HLLC, HLLEM/HLLI, HLLD and relaxation two-point fluxes as the bundle's sources use them: the single-state HLL form and its non-conservative and anti-diffusive extensions, HLLC star states and wave-speed estimates for single- and multi-component and curvilinear flows, positivity proofs, the entropy-stable relaxation solver, radiative HLL, carbuncle behaviour, dissipation on turbulence, and solver switching."
status: established
aliases: [HLL flux, HLLE, HLLC, HLLEM, HLLI, RHLLEM, HLLD, Harten–Lax–van Leer solver, relaxation Riemann solver, Suliciu relaxation solver, radiative HLL, Rad-HLL, shock-stable HLLC, HLLC-LM]
tags: [riemann-solver, numerical-flux, finite-volume, positivity, multiphase, entropy-stable]
timestamp: 2026-10-23T23:00:00Z
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

*(compiler check, not in the sources: the subsonic HLL flux above is term by term the
[central-upwind](/methods/central-upwind-scheme.md) flux with $s^\pm=a^\pm$, and the
intermediate state of the central-upwind anti-diffusion of
[Wang et al. (2023b)](/sources/wang-2023-b.md) (Eq. (5)) is $u^{\mathrm{HLL}}$ with the same
speeds.)*

[Liu et al. (2021)](/sources/liu-2021.md) (§2, Eq. (4)) use the single formula
$h=\big(s^+f(u^-)-s^-f(u^+)+s^+s^-(u^+-u^-)\big)/(s^+-s^-)$ with
$s^-=\min(\sigma^{\mathrm l},0)$ and $s^+=\max(\sigma^{\mathrm r},0)$ clipped from the
leftmost and rightmost wave-speed estimates (page-local $\sigma^{\mathrm l},\sigma^{\mathrm r}$),
evaluated on face Gauss points through rotational invariance; the same speeds upwind
the Godunov–Powell divergence term of their MHD scheme (Eq. (3)). *(compiler check, not
in the sources: with this clipping the subsonic formula reduces to $f(u^-)$ or $f(u^+)$
in the supersonic cases, so it covers all three cases above.)* See
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md).

[Fu (2023)](/sources/fu-2023.md) (§3.6, Eq. (29)) writes Roe, Rusanov, HLL and HLLC fluxes in
one form, $h\approx\tfrac12\big(f(u^-)+f(u^+)-\lvert\tilde a_{i+1/2}\rvert(u^+-u^-)\big)$, with
$\tilde a_{i+1/2}$ an averaged characteristic signal speed set by the solver (page-local;
the source's $\tilde\partial$), and remarks that all of them scale with the sound or
convection speed.

[Ji et al. (2022)](/sources/ji-2022.md) (§4, Eqs. (29)–(36)) evaluate the same HLL formula on
unstructured meshes in the face-normal frame, $h=T^{-1}h^{\mathrm{HLL}}(Tu^-,Tu^+)$ at each face
Gauss point (page-local rotation $T$), with the Einfeldt–Batten speeds
$s^-=\min(v_1^--c^-,\hat v_1-\hat c)$, $s^+=\max(v_1^++c^+,\hat v_1+\hat c)$ from Roe averages
([Roe solver](/methods/roe-riemann-solver.md)); they state that HLL is "free from Carbuncle
problem and the necessity of entropy fix" and that the solver choice "does not affect our
conclusion" (§5). [Hu et al. (2022)](/sources/hu-2022.md) (Eqs. (2.5)–(2.6)) call the HLL flux
with $s^-=\min(0,v_1^--c^-,\hat v_1-\hat c)$, $s^+=\max(0,v_1^++c^+,\hat v_1+\hat c)$ the **HLLE**
flux; including $0$ in the extrema makes it the upwind $f(u^-)$ or $f(u^+)$ in supersonic flow.

## HLLEM: anti-diffusion on the linearly degenerate fields

As printed by Hu et al. (2022) (§2.3, Eqs. (2.7)–(2.8), after Einfeldt, Munz, Roe and
Sjögreen), for the 2D Euler equations and a face normal to $x$,

$$h^{\mathrm{HLLEM}}=\frac{s^+f(u^-)-s^-f(u^+)}{s^+-s^-}+\frac{s^-s^+}{s^+-s^-}\Big([\![u]\!]-\delta_{\mathrm a}\,\mathfrak w_2\hat r_2-\delta_{\mathrm a}\,\mathfrak w_3\hat r_3\Big),$$

with page-local entropy- and shear-wave eigenvectors and strengths at the Roe average,
$\hat r_2=\big(1,\hat v_1,\hat v_2,\tfrac12(\hat v_1^2+\hat v_2^2)\big)^\top$, $\hat r_3=(0,0,1,\hat v_2)^\top$,
$\mathfrak w_2=[\![\rho]\!]-[\![p]\!]/\hat c^2$, $\mathfrak w_3=\hat\rho\,[\![v_2]\!]$, and anti-diffusion
coefficient $\delta_{\mathrm a}=\hat c/(\hat c+\lvert\hat v_1\rvert)$. Keeping only the
$\hat r_2$ term gives the HLLEC, only the $\hat r_3$ term the HLLES flux (Eqs. (3.17)–(3.18)).
Hu et al. state, citing earlier work, that HLLEM is equivalent to Roe's solver for suitable
parameters, cheaper, adjustable through $s^\pm$ on the nonlinear waves, and free of Roe's
sonic-point glitch and expansion shocks (§1, §2.3); like Roe and HLLC it is shock-unstable.

**RHLLEM** (§4.1, Eq. (4.1)). Both anti-diffusion terms are multiplied by a switching function
$f_{\mathrm s}\in[0,1]$ of a pressure-ratio sensor read on the faces transverse to the current
one, so that $f_{\mathrm s}=1$ recovers HLLEM in smooth flow and $f_{\mathrm s}\to0$ gives HLLE at
strong shocks; the linear and matrix stability analyses behind it, and the absence of a
tunable parameter, are on [carbuncle](/definitions/carbuncle-phenomenon.md).

**RHLLEM-LD** (§4.2, Eqs. (4.7)–(4.9)). Writing the flux as
$\tfrac12\big(f(u^-)+f(u^+)\big)+D$, the density inside the dissipation term $D$ is chosen per
face among MUSCL and [THINC](/methods/thinc-reconstruction.md) left and right values so that
$\lvert\rho^+-\rho^-\rvert$ is the smallest of the four combinations, a face-wise
[BVD](/definitions/boundary-variation-diminishing.md) selection on density only. The THINC
formula and its steepness are not given. With second-order MUSCL and second-order TVD
Runge–Kutta it resolves contacts and waves better than HLLE and HLLEM (and, in 2D, HLLC) on
an isolated contact (100 cells, CFL 0.9), the [Woodward–Colella blast waves](/benchmarks/woodward-colella-blast-wave.md)
(500 cells) and the Titarev–Toro problem (1000 cells, the high-frequency wave), and gives the
sharpest interfaces in an interface-only problem and in
[Richtmyer–Meshkov](/benchmarks/richtmyer-meshkov-instability.md) and
[Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md) runs, where only it keeps the
symmetry (§5.1–5.6, Figs. 5.1–5.6); the BVD step leaves the shock robustness of RHLLEM
unchanged (§5.7). See also [stationary contact preservation](/properties/stationary-contact-preservation.md).

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

## HLLC: star states and wave speeds

HLLC restores the contact by two intermediate states separated by a contact
speed $s^*$ (page-local). It is the default solver of [MFC](/software/mfc.md)
(HLL and an exact solver are options; no formulas printed;
[Bryngelson et al. (2021)](/sources/bryngelson-2021.md), §2.2, §4.1), of all tests
of the unstructured CWENO of [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md),
where its normal velocity also discretizes the $\phi_1\nabla\!\cdot v$ source of
the five-equation model (§3.1, Eqs. (15)–(16)), and of the two sources below,
which print it.

**Five-equation gas–liquid model** ([Wong et al. (2021)](/sources/wong-2021.md),
§3.2, Eqs. (24)–(27)). With $\chi^\pm=(s^\pm-v^\pm)/(s^\pm-s^*)$ (page-local) the
star states are, in 1D,

$$u^{*,\pm}=\chi^\pm\Big(\phi_1\rho_1,\ \phi_2\rho_2,\ \rho s^*,\ E+(s^*-v)\big(\rho s^*+\tfrac{p}{s^\pm-v}\big)\Big)^\pm,\qquad\phi_1^{*,\pm}=\phi_1^\pm,$$

(the superscript $\pm$ outside the bracket: evaluated at $u^\pm$; $\phi_k$ the
volume fractions, registry §10), with the Einfeldt speeds
$s^-=\min(\{\!\{v\}\!\}-\{\!\{c\}\!\},\ v^--c^-)$,
$s^+=\max(\{\!\{v\}\!\}+\{\!\{c\}\!\},\ v^++c^+)$ and the Batten contact speed

$$s^*=\frac{p^+-p^-+\rho^-v^-(s^--v^-)-\rho^+v^+(s^+-v^+)}{\rho^-(s^--v^-)-\rho^+(s^+-v^+)}.$$

The contact speed also advects the volume fraction upwind (Eqs. (40)–(43)).

**Split form for two-medium DG** ([Bai & Li (2022)](/sources/bai-2022.md), §2.4,
Eqs. (7)–(15)). The flux is split as $f=v\,u+\mathsf D$ with the pressure part
$\mathsf D=p\,(0,1,0,v)^\top$ (page-local), and with $\beta_K=\rho_K(s_K-v_K)$, $K=L,R$
(page-local; $L,R$ the sides $u^-,u^+$),

$$s^*=\frac{\beta_Rv_R-\beta_Lv_L+p_L-p_R}{\beta_R-\beta_L},\qquad p^*=\frac{\beta_Rp_L-\beta_Lp_R-\beta_L\beta_R(v_L-v_R)}{\beta_R-\beta_L},$$

the star fluxes being $s^*u^*_K+\mathsf D^*$ with $\mathsf D^*=(0,p^*,0,p^*s^*)^\top$ and the
Einfeldt speeds $s^-=\min(v_L-c_L,\hat v-\hat c)$, $s^+=\max(v_R+c_R,\hat v+\hat c)$ from Roe
averages. *(compiler check, not in the sources: multiplying numerator and denominator by $-1$
turns this $s^*$ into the Batten contact speed printed by Wong et al. above.)* The solver is
blended with HLL by a shock sensor in an HLLC–HLL hybrid
([carbuncle](/definitions/carbuncle-phenomenon.md),
[Rankine–Hugoniot condition](/definitions/rankine-hugoniot-condition.md)); the printed star
density carries a slip, $\beta_L$ for both sides (Eq. (11)).

**$N$-phase pressure–temperature equilibrium model** ([Nguyen et al. (2022)](/sources/nguyen-2022.md),
§2.3, Eqs. (20)–(25)). HLLC is "reconstructed" for one mass equation per phase plus mixture
momentum and energy: every partial density $\phi_k\rho_k$ is carried across the outer waves by
the same factor $(s_K-v_K)/(s_K-s^*)$ as the mixture density, with no special treatment of the
volume fractions; $s^*$ is again the Batten form and the speeds are the Davis–Einfeldt blend
with Roe averages. The printed right speed $s^+=\max(v_R-c_R,\hat v+\hat c)$ uses $v_R-c_R$ where
symmetry with $s^-$ requires $v_R+c_R$ (Eq. (23)). On 1D water–air interface advection HLLC keeps
the interface sharper than the Rusanov flux over Mach 0.001–1, within three to five cells
depending on the limiter (§3.1, Figs. 3–4).

**Five-equation model with gradient-based reconstruction** ([Chamarthi (2023a)](/sources/chamarthi-2023.md),
App. A, Eqs. (88)–(95)). The same construction: Einfeldt speeds from Roe averages, Batten
contact speed, the single-species star state, and for two species the star state extended by
$\phi_1\rho_1$, $\phi_2\rho_2$ and $\phi_1$. The source $\phi_1\nabla\cdot v$ of the
[five-equation model](/definitions/five-equation-model.md) is discretized with the
HLLC-consistent interface velocity

$$v_{i+1/2}=\frac{1+\mathrm{sgn}(s^*)}2\Big[v^-+s^-_0\Big(\frac{s^--v^-}{s^--s^*}-1\Big)\Big]+\frac{1-\mathrm{sgn}(s^*)}2\Big[v^++s^+_0\Big(\frac{s^+-v^+}{s^+-s^*}-1\Big)\Big],$$

$s^-_0=\min(0,s^-)$, $s^+_0=\max(0,s^+)$ (page-local), and
$(\phi_1\nabla\cdot v)_i=(\phi_1)_i\,(v_{i+1/2}-v_{i-1/2})/\Delta x$ per direction, in the manner of
Johnsen and Colonius; no oscillations appear at the material interfaces of the 1D two-fluid
tube, the shock–curtain, the [shock–helium-cylinder](/benchmarks/shock-bubble-interaction.md),
the [triple point](/benchmarks/triple-point-problem.md) and a viscous
[Richtmyer–Meshkov](/benchmarks/richtmyer-meshkov-instability.md) case (Exs. 4.14–4.18). The
companion seventh-order scheme of [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) uses HLLC
throughout and, for the 2D shock–entropy wave and the
[double Mach reflection](/benchmarks/double-mach-reflection.md), the shock-stable HLLC of
Fleischmann et al. to avoid the carbuncle that appeared in the earlier paper (§3, Exs. 3.7–3.8;
[carbuncle](/definitions/carbuncle-phenomenon.md)).

**Moving curvilinear meshes** ([Chandravamsi et al. (2023)](/sources/chandravamsi-2023.md),
§5.1.1, Eqs. (26)–(28)). In contravariant form the speeds are
$\hat s^-=\min(\hat V^--c^-\lvert\nabla\xi\rvert,\ \hat V^+-c^+\lvert\nabla\xi\rvert)$,
$\hat s^+=\max(\hat V^-+c^-\lvert\nabla\xi\rvert,\ \hat V^++c^+\lvert\nabla\xi\rvert)$, and the
contact speed is the Batten form with the pressure jump multiplied by $\lvert\nabla\xi\rvert^2$
(page-local: $\hat V$ the contravariant velocity including the grid velocity, $\nabla\xi$ the
Jacobian-scaled metric vector of the face); the star states carry the metric terms and the
temporal metric. The interface metrics are those of the scheme's free-stream-preserving
interpolation. The authors state that HLLC is less dissipative than HLL and Rusanov (not
tested in the paper).

**Pressure-based speeds** ([Li, Shu & Qiu (2022)](/sources/li-2022-d.md), §2.1,
Eqs. (2.5)–(2.7)), for the Euler equations: a primitive-variable estimate

$$p^*=\tfrac12\big(p^-+p^++(v^--v^+)\{\!\{\rho\}\!\}\{\!\{c\}\!\}\big),\qquad s^*=\tfrac12\Big(v^-+v^++\frac{p^--p^+}{\{\!\{\rho\}\!\}\{\!\{c\}\!\}}\Big),$$

and $s^-=v^--c^-\mathsf z^-$, $s^+=v^++c^+\mathsf z^+$ with $\mathsf z^\pm=1$ if
$p^*\le p^\pm$ and $\mathsf z^\pm=\sqrt{1+\frac{\gamma+1}{2\gamma}(p^*/p^\pm-1)}$
otherwise (page-local $\mathsf z^\pm$), chosen "to better adapt to our high order
scheme" in a moment-based [Hermite WENO](/methods/hermite-weno.md).

## HLL fans with linear data and with phase change

- **Generalized Riemann problem.** The HLL-GRP solver evolves the three states of the HLL fan
  linearly in time from piecewise-linear data, obtains the gradient of the intermediate state
  from a Rankine–Hugoniot-based least-squares system, and gives the one-step second-order flux
  $h^{\mathrm{HLL}}-A(u^{\mathrm{HLL}})^2\,\partial_xu^{\mathrm{HLL}}\,\Delta t/2$ in the subsonic case
  ([Liu et al. (2023a)](/sources/liu-2023.md), §3.2.1, Eqs. (57)–(66); written out on
  [generalized Riemann problem](/methods/generalized-riemann-problem.md)). In their
  multidimensional ideal-MHD scheme the speeds are the Wu–Shu estimates: $s^-$ is the minimum of
  the smallest eigenvalues of both states and of
  $\min(v_1^-,\bar v_1)-\varphi_{\mathrm f}(u^-)-\lvert B^--B^+\rvert/(\sqrt{\rho^-}+\sqrt{\rho^+})$, with
  $\bar v_1$ the $\sqrt\rho$-weighted normal velocity and $\varphi_{\mathrm f}$ a modified fast speed
  built with $(\gamma-1)p$ (page-local), and $s^+$ symmetrically; $0$ is included in the
  minimum and maximum for the weights of the Godunov–Powell source and omitted for the GRP fan
  (Eqs. (10)–(15), (59)–(60)). The forward-Euler and SSP-RK2 comparison schemes use the plain HLL
  flux of Wu and Shu (§4).
- **Non-conservative first-order limit.** The first-order path-conservative central-upwind scheme
  is the semi-discrete HLL scheme for non-conservative systems
  ([Kurganov et al. (2023)](/sources/kurganov-2023.md), Remark 2.2, citing Castro, Morales de
  Luna and Parés 2017; [path-conservative schemes](/methods/path-conservative-scheme.md)).
- **Phase change.** Long et al. extend an HLL-type fan with Davis speeds to four waves (two outer
  shocks, a phase interface, a contact) for the liquid–vapour Riemann problem with evaporation
  and condensation, closed by a density-ratio supplement and the Hertz–Knudsen mass flux
  ([Long et al. (2023)](/sources/long-2023.md), §3.2; [Riemann solvers with phase change](/methods/phase-change-riemann-solver.md)).

## Relaxation solvers

[Renac (2021)](/sources/renac-2021.md) (§4, Eqs. (51)–(56), App. C) builds an
entropy-stable and positive three-point flux for the multicomponent Euler
equations by composing a Coquel–Perthame energy relaxation (a polytropic
pressure law with a constant exponent larger than every species' $\gamma$) with
Bouchut's pressure (Suliciu) relaxation. The result is an HLLC-like three-wave
solver: mass fractions are unchanged across the outer waves, and with Bouchut's
approximate Lagrangian sound speeds $\mathsf a^\pm$ (page-local)

$$s^*=\frac{\mathsf a^-v^-+\mathsf a^+v^++p^--p^+}{\mathsf a^-+\mathsf a^+},\qquad p^*=\frac{\mathsf a^+p^-+\mathsf a^-p^++\mathsf a^-\mathsf a^+(v^--v^+)}{\mathsf a^-+\mathsf a^+},\qquad s^\mp=v^\mp\mp\frac{\mathsf a^\mp}{\rho^\mp}.$$

It is consistent, Lipschitz, entropy stable and positive under
$\frac{\Delta t}{\Delta x}\max_i\big(\lvert v_i\rvert+\mathsf a/\rho\big)<\tfrac12$ (Eq. (52)),
largely by reference to Bouchut and to Marmignon, Naddei and Renac; because the
relaxation entropy is only non-strictly convex (Lemma 4.1), the general
relaxation framework does not apply directly and the pressure relaxation supplies
the entropy inequality. In the experiments the relaxation exponent is
$\max(\gamma_1,\gamma_2)$ and the wave speeds are multiplied by 1.05. Against it, an
entropy-conservative flux plus scalar Rusanov-type dissipation (App. D) is entropy
stable but non-Lipschitz, needs CFL 0.2 instead of 0.4, and the 2D runs stop on
negative solutions (Figs. D.9–D.10). Renac also states that fast upper bounds of the
maximum wave speed, which HLL, Roe and Rusanov need, are not known for this
multicomponent model (§1.3). See [entropy stability](/properties/entropy-stability.md)
and [multicomponent Euler equations](/definitions/multicomponent-euler-equations.md).

## Radiative HLL and relativistic MHD

In relativistic radiation MHD with the M1 closure, [López-Miralles et al. (2023)](/sources/lopezmiralles-2023.md)
(§3.2.1, Eqs. (24)–(31)) use HLL with **separate** speed pairs for the magnetofluid block
(roots of the quartic characteristic equation) and for the radiation block, whose Jacobian
depends only on the radiation energy and flux and whose eigenvalues are closed-form functions
of the reduced flux and its angle to the face normal; common speeds for both blocks cause
excessive diffusion. In optically thick cells the radiation speeds are limited to
$\pm\tfrac4{3\tau_{\mathrm{opt}}}$ (page-local cell optical depth $\tau_{\mathrm{opt}}$, after Sądowski
et al.). The radiative HLLC of Melon Fuksman and Mignone must fall back to HLL when the speeds
are limited, so it improves on HLL only in optically thin media, and HLLD has not been adapted
to radiation (stated). Their alternative is the
[PVM solver](/methods/polynomial-viscosity-matrix-solver.md), which needs no speed estimates
per block.

On the large-amplitude [circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md)
of relativistic MHD (no radiation; Tables 1–3): first-order (Godunov) HLL converges at order
0.92 between 256 and 512 cells; piecewise-linear reconstruction gives second order; HLLC gives
the results of Martí (2015), and HLLD performs like HLLC on this smooth solution; MP3 with
third-order Runge–Kutta gives order 2.998 with HLLD; MP5 with third-order Runge–Kutta stays
third order but with errors almost two orders of magnitude below MP3 ($4.284\times10^{-9}$ vs
$3.224\times10^{-7}$ at 512 cells); MP5 with a five-stage fourth-order SSP Runge–Kutta reaches
orders 4.83–5.05 with HLLD (error $9.006\times10^{-12}$ at 512 cells). The paper does not discuss
why the fourth-order time integrator does not limit the observed order at CFL 0.3.

## Positivity and the bound-preserving CFL

- [Wong et al. (2021)](/sources/wong-2021.md) (§3.3, Eqs. (46)–(70)) prove that the
  first-order HLLC scheme above keeps partial densities non-negative, the volume
  fraction in $[0,1]$ and $\rho e-\bar p_\infty>0$ (page-local mixture stiffening
  pressure of the [stiffened-gas law](/definitions/stiffened-gas-equation-of-state.md)),
  under CFL $\le0.5$ with a directional split of the 2D update. The energy condition
  reduces to a quadratic in $s^*-v^-$ with negative discriminant iff
  $s^-<v^--(p^-+\bar p^-_\infty)/\sqrt{2\rho^-(\rho e-\bar p_\infty)^-}$, and the
  right-hand side exceeds $v^--c^-$, so the Einfeldt speed suffices (Eq. (57)). The
  proof needs the convexity of the admissible set, which holds when the ideal-gas phase
  has the smaller $\gamma$ (Lemma 1, Thm. 1; see
  [bound preservation](/properties/bound-preservation.md)).

- [Chen & Wu (2022)](/sources/chen-2022-b.md) (§3.5, Lemmas 3.6–3.7, Thm. 3.1) prove that the
  HLL flux with $s^-=\min\{\lambda_1(u^-),\lambda_1(u^+),0\}$ and
  $s^+=\max\{\lambda_4(u^-),\lambda_4(u^+),0\}$ keeps the cell averages of a third-order
  finite-volume WENO scheme for special relativistic hydrodynamics on triangles in the
  admissible set (positive density and pressure, subluminal velocity) under
  $\Delta t\,\hat\sigma^{(j)}_K\lvert E^j_K\rvert/\lvert K\rvert\le\tfrac23\hat\omega_1$, with
  $\hat\sigma$ the spectral radius of the normal Jacobian, $\lvert E^j_K\rvert$ the edge lengths,
  $\lvert K\rvert$ the area and $\hat\omega_1=1/(L(L-1))$ the first Gauss–Lobatto weight,
  $L=\lceil(N+3)/2\rceil$ for reconstruction degree $N$ (page-local). The proof works on the
  [geometric-quasilinearization](/methods/geometric-quasilinearization.md) form of the admissible
  set, in which the constraints are linear in $u$ (Lemma 3.4). They also show
  $h^{\mathrm{HLL}}(\sigma u^-,\sigma u^+)=\sigma\,h^{\mathrm{HLL}}(u^-,u^+)$ for $\sigma>0$, since the
  speeds are invariant, which keeps the scheme homogeneous like the relativistic evolution
  (§3.6; [scale invariance](/properties/scale-invariance.md)). That Lax–Friedrichs and HLLC
  "also meet" the property in this framework is stated, not proved (§3.1).
- [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) (§4.1) need the element means of a
  DG/flux-reconstruction scheme to stay positive and to obey a local minimum entropy principle,
  which they attribute, citing Zhang–Shu and Chen–Shu, to SSP time stepping, a CFL condition and
  an entropy-stable positivity-preserving Riemann solver such as Godunov, local Lax–Friedrichs or
  HLLC "with suitable wave speeds"; their implementation uses HLLC
  ([entropy filtering](/methods/entropy-filtering.md)).
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

**Dissipation on compressible turbulence.** In the GPU port of an unstructured OpenFOAM
finite-volume solver, [Bielawski et al. (2023)](/sources/bielawski-2023.md) (App. A) compare a
skew-symmetric central flux, HLLC and AUSMDV on decaying compressible isotropic turbulence
against spectral data. At initial turbulent Mach number 0.3 the central flux tracks the
reference, HLLC is closer to it than AUSMDV, which "adds additional numerical dissipation even
at the turbulent Mach number of 0.3"; at 0.6, with eddy shocklets, both upwind fluxes are much
more dissipative than the central one in enstrophy and dilatation, the HLLC–AUSMDV gap narrows,
and mesh skewness matters little next to the flux's own dissipation (Figs. A.13–A.16). The
authors postulate that a hybrid central/HLLC flux would help (see
[hybrid central-WENO schemes](/methods/hybrid-weno.md)). Their text describes approximate
Riemann solvers as giving "near minimal possible dissipation across discontinuities while
maintaining a monotonicity preserving solution" (§3); the comparison of Appendix A concerns
smooth turbulence and shocklets, not isolated discontinuities.

## Other fluxes in the same codes

Several sources pair or compare HLL-type solvers with other interface fluxes:

- **Hybrid Roe/HLL and AUSM** on mapped meshes ([Peng et al. (2022)](/sources/peng-2022.md),
  §2.3, Eqs. (13)–(14)): the momentum is rotated into the face-normal frame,
  $\hat f=T_S^{-1}h(T_Su^-,T_Su^+)$ with the page-local rotation $T_S$, and $h$ is the AUSM flux of
  Liou–Steffen or a Roe solver that switches to HLL, with a multidimensional entropy correction
  and a mass-fraction positivity correction (not written out). For the stagnation-point
  oscillation of shock-induced combustion in front of a blunt body (Lehr's experiments,
  148 kHz at Mach 4.18 and 425 kHz at Mach 4.48), AUSM and Roe/HLL give 160 and 165 kHz, and
  425 and 430 kHz, with the Jachimowski mechanism; AUSM gives the more regular oscillations at
  Mach 4.18 (§4.3, Table 5; [shock-induced combustion](/benchmarks/shock-induced-combustion.md)).
- **AUSMDV** of Wada and Liou is the interface flux of the high-order
  [WCNS](/methods/weighted-compact-nonlinear-scheme.md) of
  [Hiejima (2022)](/sources/hiejima-2022.md) (§2.2), who stresses that a WCNS can use any
  flux-difference, flux-vector-splitting or AUSM-type flux (§1).
- **Primitive-variable Riemann solver (PVRS)** in the second-order MUSCL–Hancock solver of the
  [immersed-boundary](/methods/immersed-boundary-method.md) method of
  [Wang et al. (2022a)](/sources/wang-2022.md) (§2.1, Eqs. (9)–(11)), chosen "to avoid the
  correction of the Riemann solver for the immersed method":
  $$p^*=\frac{C_Rp_L+C_Lp_R+C_LC_R(v_L-v_R)}{C_L+C_R},\qquad s^*=\frac{C_Lv_L+C_Rv_R+p_L-p_R}{C_L+C_R},\qquad C_K=\sqrt{\gamma p_K\rho_K},$$
  with $\rho^*_K=\rho_K+(p^*-p_K)/c_K^2$; HLL is used for the reactive case (§3.6).
  *(compiler check, not in the sources: these are Renac's relaxation $p^*$, $s^*$ above with the
  Lagrangian sound speeds set to the acoustic impedances, $\mathsf a_K=C_K=\rho_Kc_K$.)*
- **van Leer flux-vector splitting** for every shocked case of the second-order unstructured
  finite-volume scheme of [Chen et al. (2022)](/sources/chen-2022.md), to exclude flux-induced
  shock instabilities, and HLLC, for its contact resolution, for the shock-free ones (§2).

## Solver menus in codes

- **IDEFIX** ([Lesur et al. (2023)](/sources/lesur-2023.md), §2.3–2.5, no formulas printed):
  Rusanov, HLL (Einfeldt), HLLC and, in MHD, HLLD of Miyoshi and Kusano, and Roe, selectable at
  run time and ordered "from most to least diffusive"; the edge electric fields of constrained
  transport can also come from 2D HLL and HLLD solvers. With the Hall effect the whistler speed
  is added to the HLL fan for the magnetic-field fluxes only, which makes HLL "our only solver
  compatible with the Hall effect", "known to be diffusive" but stable; a Hall-modified EMF
  average led to instabilities. On a Hall-dominated shock the error falls by a factor 3–4 per
  doubling, "slightly less than second order", attributed to the grid-scale whistler diffusivity
  (§4.2, Fig. 15). See [IDEFIX](/software/idefix.md).
- **FLEXI** ([Mossier et al. (2022)](/sources/mossier-2022.md), §8.4–8.9): HLLE for the
  [double Mach reflection](/benchmarks/double-mach-reflection.md) and the
  [forward-facing step](/benchmarks/forward-facing-step.md), Roe with a Harten–Hyman entropy fix
  for the Sod, Shu–Osher and transonic-airfoil cases, local Lax–Friedrichs for the 3D explosion
  ([FLEXI](/software/flexi.md)).

- **JAX-Fluids** ([Bezgin et al. (2023)](/sources/bezgin-2023.md), §3.3, Table 2): HLL, HLLC
  and the low-Mach shock-stable HLLC-LM of Fleischmann et al., with arithmetic, Davis, Einfeldt
  or Toro speed estimates, besides Lax–Friedrichs, Rusanov and AUSM+; the default setup is
  primitive-variable WENO5-JS with HLLC and Einfeldt speeds ([JAX-Fluids](/software/jax-fluids.md)).
- **blastFoam / RSDFoam** ([Weng & Mével (2023)](/sources/weng-2023.md), §3.1): HLL, HLLC,
  HLLC-P, AUSM+, Tadmor and Kurganov fluxes with MUSCL reconstruction; the validation runs use
  quadratic MUSCL with the van Leer limiter, HLLC and second-order SSP Runge–Kutta.
- **OpenFOAM on GPUs** ([Bielawski et al. (2023)](/sources/bielawski-2023.md), §3): HLLC with
  limited interpolation of the face states, chosen for its low cost and contact resolution.

## No Riemann solver: shock fitting

In the moving DG method MDG+ICE of [Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md)
the interface condition, enforced weakly, makes the face flux unique at convergence, so
the interior flux is the plain central average and no Riemann solver is used (§3.3,
Eqs. (3.14)–(3.15)); the authors state that how to extend an upwind flux to their
space-time formulation consistently with the interface condition "remains an open
problem", while most upwind fluxes can be used in the steady-state version. See
[implicit shock tracking](/methods/implicit-shock-tracking.md) and
[carbuncle](/definitions/carbuncle-phenomenon.md).

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
- [Wang et al. (2023b)](/sources/wang-2023-b.md) — Eq. (5) (intermediate state).
- [Wong et al. (2021)](/sources/wong-2021.md) — §3.2–3.3 (Eqs. (24)–(70), Lemma 1, Thm. 1) (arXiv v1).
- [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) — §1, §2.1 (Eqs. (2.5)–(2.7)) (arXiv v1).
- [Renac (2021)](/sources/renac-2021.md) — §1.3, §4 (Eqs. (51)–(56), Lemma 4.1), §7, Apps. C–D (arXiv v3).
- [Liu et al. (2021)](/sources/liu-2021.md) — §2 (Eqs. (3)–(4)).
- [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) — §2.2, §4.1 (arXiv v1).
- [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) — §3.1, §3.3.
- [Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md) — §3.3 (author manuscript).
- [Bai & Li (2022)](/sources/bai-2022.md) — §2.4 (Eqs. (7)–(20)).
- [Nguyen et al. (2022)](/sources/nguyen-2022.md) — §2.3 (Eqs. (20)–(25)), §3.1 (Figs. 3–4).
- [Chen & Wu (2022)](/sources/chen-2022-b.md) — §3.1, §3.5 (Lemmas 3.4–3.7, Thm. 3.1), §3.6 (arXiv v1).
- [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) — §4.1, §4.2 (arXiv v3).
- [Peng et al. (2022)](/sources/peng-2022.md) — §2.3 (Eqs. (13)–(14)), §4.3 (Table 5) (accepted manuscript).
- [Hiejima (2022)](/sources/hiejima-2022.md) — §1, §2.2.
- [Wang et al. (2022a)](/sources/wang-2022.md) — §2.1 (Eqs. (9)–(11)), §3.6.
- [Chen et al. (2022)](/sources/chen-2022.md) — §2.
- [Hu et al. (2022)](/sources/hu-2022.md) — §1, §2.2–2.3 (Eqs. (2.5)–(2.8)), §3.2 (Eqs. (3.17)–(3.18)), §4 (Eqs. (4.1)–(4.9)), §5.1–5.7.
- [Ji et al. (2022)](/sources/ji-2022.md) — §4 (Eqs. (29)–(36)), §5.
- [Lesur et al. (2023)](/sources/lesur-2023.md) — §2.3–2.5, §4.2 (Fig. 15).
- [Mossier et al. (2022)](/sources/mossier-2022.md) — §8.4–8.9.
- [Chamarthi (2023a)](/sources/chamarthi-2023.md) — App. A (Eqs. (88)–(95)), Exs. 4.14–4.18 (arXiv v2).
- [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) — §3, Exs. 3.7–3.8 (arXiv v1).
- [Chandravamsi et al. (2023)](/sources/chandravamsi-2023.md) — §5.1.1 (Eqs. (26)–(28)) (arXiv v1).
- [López-Miralles et al. (2023)](/sources/lopezmiralles-2023.md) — §3.2.1 (Eqs. (24)–(31)), §4.1.1 (Tables 1–3) (arXiv v1).
- [Bielawski et al. (2023)](/sources/bielawski-2023.md) — §3, App. A (Figs. A.13–A.16) (accepted manuscript).
- [Bezgin et al. (2023)](/sources/bezgin-2023.md) — §3.3, Table 2 (arXiv v1).
- [Weng & Mével (2023)](/sources/weng-2023.md) — §3.1.
- [Liu et al. (2023a)](/sources/liu-2023.md) — §2.2 (Eqs. (10)–(15)), §3.2.1 (Eqs. (57)–(66)), §4.
- [Kurganov et al. (2023)](/sources/kurganov-2023.md) — Remark 2.2.
- [Long et al. (2023)](/sources/long-2023.md) — §3.2 (Eqs. (13)–(15)).
