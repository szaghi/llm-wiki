---
type: Method
title: "Flux vector splitting"
description: "Flux vector splitting writes the flux as a sum of parts whose Jacobians have non-negative and non-positive eigenvalues, so each part is upwinded on its own; the page gives the Lax–Friedrichs, Steger–Warming and van Leer–Hänel splittings, their use in Active Flux and finite differences, and the advective–pressure splittings of all-Mach schemes."
status: established
aliases: [FVS, flux-vector splitting, Steger–Warming splitting, upwind flux splitting, van Leer splitting, van Leer–Hänel splitting, Toro–Vázquez splitting]
tags: [numerical-flux, flux-splitting, finite-difference, finite-volume, characteristic, bound-preserving]
timestamp: 2026-10-24T05:59:00Z
---

# Flux vector splitting

A **flux vector splitting** (FVS) writes the flux of $\partial_tu+\partial_xf(u)=0$ as
$f=f^++f^-$ with

$$\lambda\Big(\frac{\partial f^+}{\partial u}\Big)\ge0,\qquad \lambda\Big(\frac{\partial f^-}{\partial u}\Big)\le0,$$

all eigenvalues of the Jacobian of $f^+$ non-negative and all of $f^-$ non-positive, so that
$\partial_xf^+$ is differenced (or reconstructed) from the left and $\partial_xf^-$ from the right
([Duan, Barsukow & Klingenberg (2025)](/sources/duan-2025.md), §2.2, Eqs. (9)–(10); arXiv v3).
Any splitting with this property is admissible there. The registry's
[Lax–Friedrichs splitting](/methods/lax-friedrichs-flux.md) $f^\pm=\tfrac12(f\pm au)$ is the
member with a scalar dissipation coefficient, and the upwinding of the finite-difference WENO
and TENO schemes collected on that page. A splitting
**by eigenvalue sign** differs from a splitting **by physical sub-system** (advection against
pressure), used by semi-implicit all-Mach schemes to treat one part explicitly and the other
implicitly (last section); both are called flux splittings in the sources.

## Three splittings for the Euler equations

Duan et al. (§2.2.1–2.2.3; Appendix A for 2D) use three, here in registry notation with the
1D eigenvalues $\lambda_1=v-c\le\lambda_2=v\le\lambda_3=v+c$ and
$\lambda^+=\max(\lambda,0)$, $\lambda^-=\min(\lambda,0)$.

- **Local Lax–Friedrichs (LLF).** $f^\pm=\tfrac12(f(u)\pm a_{i+1/2}u)$ with $a_{i+1/2}$ the
  largest spectral radius of $A$ over the five states that enter the update of the point value
  at $x_{i+1/2}$: the point values at $x_{i-1/2},x_{i+1/2},x_{i+3/2}$ and the cell-centred values of
  cells $i$ and $i+1$ (Eq. (12)). A global $a$ is allowed but gives a smaller time step and more
  dissipation.
- **Upwind (Steger–Warming).** $f^\pm=\tfrac12\big(f(u)\pm\lvert A\rvert u\big)$,
  $\lvert A\rvert=R(\Lambda^+-\Lambda^-)L$ (Eq. (13)). For a linear flux $f=Au$ this is the
  Jacobian splitting $A^\pm=R\Lambda^\pm L$; for the Euler equations, whose flux is homogeneous of
  degree one ($f=A(u)u$), it is the Steger–Warming splitting, with page-local
  $\mathsf s^\pm=2(\gamma-1)\lambda_2^\pm+\lambda_1^\pm+\lambda_3^\pm$,
  $$f^\pm=\frac{\rho}{2\gamma}\begin{pmatrix}\mathsf s^\pm\\ \mathsf s^\pm v+c(\lambda_3^\pm-\lambda_1^\pm)\\ \tfrac12\mathsf s^\pm v^2+cv(\lambda_3^\pm-\lambda_1^\pm)+\dfrac{c^2}{\gamma-1}(\lambda_3^\pm+\lambda_1^\pm)\end{pmatrix}.$$
  *(compiler check, not in the sources: $f^++f^-$ gives $(\rho v,\ \rho v^2+p,\ v(E+p))$, using
  $\lambda^++\lambda^-=\lambda$ and $\rho c^2=\gamma p$.)* Because of the absolute values the split
  fluxes need not be differentiable in $u$ (Remark 2.1, after van Leer).
- **Van Leer–Hänel.** With $M=v/c$ and $H=(E+p)/\rho$,
  $$f^\pm=\begin{pmatrix}\pm\tfrac14\rho c(M\pm1)^2\\ \pm\tfrac14\rho c(M\pm1)^2v+p^\pm\\ \pm\tfrac14\rho c(M\pm1)^2H\end{pmatrix},\qquad p^\pm=\tfrac12(1\pm\gamma M)p,$$
  "a quadratic differentiable splitting with respect to the Mach number" (§2.2.3). It is printed
  without a supersonic branch, and the paper does not discuss $\lvert M\rvert>1$.
  *(compiler check, not in the sources: the printed parts sum to the Euler flux for every $M$.)*

## Flux vector splitting for Active Flux point values

In the semi-discrete ("generalized") [Active Flux](/methods/active-flux.md) method the cell
averages are updated conservatively from interface point values, and the point values by a
finite-difference-like formula. The update of Abgrall and Barsukow, as recalled by Duan et al.
(§2, Eqs. (6)–(8)), is a **Jacobian splitting** of the quasilinear form,
$\frac{d}{dt}u_{i+1/2}=-\big[A^+(u_{i+1/2})D^+u+A^-(u_{i+1/2})D^-u\big]$ with $A^\pm=R\Lambda^\pm L$
and $D^\pm$ the derivatives of the parabolic reconstruction of the upwind cell. Duan et al.
replace it by FVS,

$$\frac{d}{dt}u_{i+1/2}=-\Big[\frac{f^+_{i-1/2}-4f^+_i+3f^+_{i+1/2}}{\Delta x}+\frac{-3f^-_{i+1/2}+4f^-_{i+1}-f^-_{i+3/2}}{\Delta x}\Big],$$

the derivatives at $x_{i+1/2}$ of the parabolas through the split fluxes at the two endpoints and
at the cell centre of the upwind cell, where the centre value is $u_i=(-u_{i-1/2}+6\bar u_i-u_{i+1/2})/4$
(Eqs. (9), (11), uniform $\Delta x$ here). The global reconstruction stays continuous. For linear
systems the upwind FVS coincides with the Jacobian splitting when both use the same
reconstructed polynomial (§2.2.2). For nonlinear problems FVS removes two defects of the
Jacobian splitting: the stagnation of both point values at a transonic Burgers discontinuity,
data $2$ / $-1$, which makes the cell average grow into a spike (Ex. 5.1, Fig. 3;
[Burgers tests](/benchmarks/burgers-equation-tests.md)), and the decoupling of the corner and
horizontal-face values from the vertical-face values and cell averages on a grid-aligned
quasi-2D Sod problem on $100\times2$ cells (§3.2, Ex. 5.7, Figs. 10–11).

Measured consequences (Duan et al., §5, App. D):

| splitting | observed order on smooth Euler data | experimental maximal CFL, 1D Euler accuracy test | CFL, LeBlanc / blast waves |
|---|---|---|---|
| Jacobian splitting | 3 | about 0.47 | 0.4 / 0.4 |
| LLF | 3 | about 0.43 | 0.4 / 0.4 |
| Steger–Warming | about 2 | about 0.32 | 0.4 / 0.4 |
| van Leer–Hänel | 3 | about 0.18 | 0.1 / 0.36 |

(Ex. D.1 with $\gamma=3$, all runs at CFL 0.18; near-vacuum isentropic vortex, Ex. 5.6;
[LeBlanc tube](/benchmarks/leblanc-shock-tube.md), Ex. 5.2;
[Woodward–Colella blast waves](/benchmarks/woodward-colella-blast-wave.md), Ex. 5.3.) The
Steger–Warming order loss "might" be explained by its non-differentiability (Remark 2.1), and the
density defects it shows where $v=0$ resemble the sonic-point glitch (Ex. D.1). The maximal CFL
numbers are experimental; their reduction comes from the different stability bounds of the
point-value updates and is "not related to the BP property" (Remarks 2.2, 5.1). The authors find
LLF "the best among all the three FVS in terms of the CFL number and non-oscillatory property for
high-speed flows involving strong discontinuities" (Remark 2.2). The bound-preserving limiting
of averages and point values that makes the shocked runs possible is described on the
[Active Flux](/methods/active-flux.md), [convex limiting](/methods/convex-limiting.md) and
[Zhang–Shu limiter](/methods/zhang-shu-scaling-limiter.md) pages.

The arbitrary-order 2D Active Flux of [Barsukow et al. (2026)](/sources/barsukow-2026.md)
(§3.4, Eqs. (27)–(32); arXiv v2) keeps the Jacobian splitting for its point values: each normal
derivative is weighted by $A^{(d)\pm}=R^{(d)}\Lambda^{(d)\pm}L^{(d)}$ and taken from the
reconstruction of the upwind cell, while tangential derivatives at edge points, being continuous,
are not upwinded. Only smooth problems are run; limiting, for example with the FVS update of
Duan et al., is left to future work (§5–§6).

## Splittings in finite-difference and finite-volume codes

- **Finite differences.** [Wong et al. (2021)](/sources/wong-2021.md) (§4.3) state that a
  finite-difference WENO scheme "can only be used with flux-vector splitting methods" when high
  order is wanted, since a Riemann solver makes it "degenerate to only second order"; the
  alternative formulation does not need this ([alternative WENO](/methods/alternative-weno.md)).
  The Lax–Friedrichs splitting, global or local, per field or scalar, and its uses are
  collected on the [Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md) page. Steger–Warming splitting is used with
  fifth-order WENO-Z on the Cartesian grid of a hypersonic overset solver by
  [McQuaid & Brehm (2024)](/sources/mcquaid-2024.md) (§3.8; [hybrid schemes](/methods/hybrid-weno.md)),
  and as one of the monotone fluxes of the alternative-formulation TENO of
  [Ye et al. (2022)](/sources/ye-2022.md), where HLLC beats it on the dissipation rate of the
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) (§4.9, Figs. 10–12).
- **Van Leer splitting at shocks.** [Hong et al. (2022)](/sources/hong-2022.md) switch from Roe to
  van Leer FVS for the double Mach reflection and the 2D Riemann problem of their TENO comparison
  (§5.6–5.7). [Chen et al. (2022)](/sources/chen-2022.md) (§2) use it for every shocked case of
  their second-order unstructured finite-volume scheme because it is "robust in shock-capturing
  computations", which lets them "exclude the numerical shock instabilities caused by numerical
  fluxes" ([carbuncle phenomenon](/definitions/carbuncle-phenomenon.md)).
- **Hypersonic codes.** In the immersed-boundary assessment of
  [Başkaya et al. (2024)](/sources/baskaya-2024.md) the body-fitted reference US3D uses a
  modified Steger–Warming flux and the ghost-cell code CHESS Steger–Warming FVS, both with MUSCL
  ([immersed boundaries](/methods/immersed-boundary-method.md)).
- **Kinetic flux vector splitting.** [Wu & Shu (2023)](/sources/wu-2023-b.md) (§5.1) prove with
  [geometric quasilinearization](/methods/geometric-quasilinearization.md) that the first-order
  gas-kinetic (kinetic FVS) scheme for Euler is bound preserving under $\nu\le1$
  ([gas-kinetic schemes](/methods/gas-kinetic-scheme.md)).

## Advective–pressure splittings for all-Mach schemes

The splittings of semi-implicit schemes separate sub-systems instead of eigenvalue signs. In
the **Toro–Vázquez** splitting, as analysed by [Allegrini & Vignal (2025)](/sources/allegrini-2025.md)
(§2.1, Eq. (8), Lemma 1; HAL author manuscript), the explicit part carries the mass flux, the
convective momentum flux and the kinetic-energy flux, $f_{\mathrm e}=(\rho v,\rho v\otimes v,\kappa v)$,
and the implicit part the pressure and the enthalpy flux,
$f_{\mathrm i}=(0,\ p\,\mathbb I,\ \tfrac{\gamma p}{\gamma-1}v)$ (page-local symbols, written here
for the unscaled equations; Allegrini & Vignal scale the pressure gradient by
$1/\varepsilon_{\mathrm A}$, with $M^2=\varepsilon_{\mathrm A}/\gamma$, page-local $\varepsilon_{\mathrm A}$). In 1D the explicit Jacobian has eigenvalues $0,v,v$, so its time step and
its upwind dissipation contain no sound speed, and the implicit one has $0$ and
$\tfrac v2\pm\sqrt{v^2/4+c^2}$ in the unscaled form. The authors note that it was introduced for
contact and shear-wave recognition, not for asymptotic preservation, and prove that both
parts have real eigenvalues, that it is asymptotically consistent for non-well-prepared data and
contact preserving, unlike the Cordier–Degond–Kumbaro, Dimarco–Loubère–Vignal and a
Lagrange-projection-type splitting (Lemmas 1–3). Remark 2.1 observes that, in their Fourier
analysis and tests, it "seems not necessary" for the two parts to be separately hyperbolic: the
double explicit eigenvalue $v$, without a full set of eigenvectors, is accepted. The
Balsara–Montecinos–Toro splitting for MHD used by [Dematté et al. (2024)](/sources/dematte-2024.md)
(§2.1) is the analogue whose advective part has eigenvalues $0$ and $v_1$ only. Both are
described in full on [semi-implicit all-Mach schemes](/methods/semi-implicit-all-mach-scheme.md).

## Qualifications

- **Order of the Steger–Warming loss.** Duan et al. observe second order with Steger–Warming in
  the Active Flux point-value update and attribute it tentatively to non-differentiability; the
  finite-difference users above report no accuracy test of their Steger–Warming runs, so the
  bundle has no evidence on whether the loss is specific to the Active Flux setting.
- **Van Leer splitting and high order.** Chen et al. (2022) rely on van Leer FVS to exclude shock
  instabilities in a second-order scheme; [Ren et al. (2025)](/sources/ren-2025.md) (§4.1.2,
  Figs. 11–12, 15) find that van Leer FVS, which with HLL is "generally believed" to capture
  strong shocks stably at first and second order, gives eigenvalues with positive real part and a
  distorted shock with fifth-order finite-volume WENO-Z on a steady normal shock at Mach 20 and
  on a blunt body. The two statements concern different orders and are compatible
  ([matrix stability analysis](/methods/matrix-stability-analysis.md)).
- The two "$\alpha$" of Duan et al., the FVS coefficient over five states and the Lax–Friedrichs
  coefficient of their low-order bound-preserving flux over two cell averages, are different
  quantities (§2.2.1, §4.1); here both are the registry's $a$, defined where used.
- The van Leer–Hänel and Steger–Warming formulas are those of Duan et al.'s arXiv v3, in the
  registry's eigenvalue order ($\lambda_1=v-c$), whereas the paper numbers $\lambda_1=v$,
  $\lambda_2=v+c$, $\lambda_3=v-c$.

# Citations

- [Duan, Barsukow & Klingenberg (2025)](/sources/duan-2025.md) — §2 (Eqs. (5)–(13), Remarks 2.1–2.2), §3.2, §5 (Exs. 5.1–5.7, Remark 5.1), App. A, App. D (Ex. D.1) (arXiv v3).
- [Barsukow et al. (2026)](/sources/barsukow-2026.md) — §3.4 (Eqs. (27)–(32)), §5–§6 (arXiv v2).
- [Allegrini & Vignal (2025)](/sources/allegrini-2025.md) — §2.1 (Eq. (8), Lemma 1, Remarks 2.1–2.2), §2.2 (Lemmas 2–3) (HAL author manuscript).
- [Dematté et al. (2024)](/sources/dematte-2024.md) — §2.1 (Eqs. (14)–(19)).
- [Wong et al. (2021)](/sources/wong-2021.md) — §4.3.
- [McQuaid & Brehm (2024)](/sources/mcquaid-2024.md) — §3.8.
- [Ye et al. (2022)](/sources/ye-2022.md) — §4, §4.9 (Figs. 10–12).
- [Hong et al. (2022)](/sources/hong-2022.md) — §5.6–5.7.
- [Chen et al. (2022)](/sources/chen-2022.md) — §2.
- [Başkaya et al. (2024)](/sources/baskaya-2024.md) — §3, §4 (Table 1) (author preprint).
- [Wu & Shu (2023)](/sources/wu-2023-b.md) — §5.1.
- [Ren et al. (2025)](/sources/ren-2025.md) — §4.1.2 (Figs. 11–12, 15).
