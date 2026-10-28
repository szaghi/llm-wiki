---
type: Method
title: "Scale-adaptive simulation"
description: "Menter's scale-adaptive simulation: an unsteady RANS approach whose length-scale equation carries the von Kármán length, so that the eddy viscosity falls in resolved unsteady regions; the k-√kL model as printed, its eddy-viscosity form and log-law calibration, its first high-order discontinuous Galerkin implementation, and comparisons with DES-type hybrids reported by other sources."
status: established
aliases: [SAS, k-√kL model, KSKL, k-sqrt(k)L, Menter–Egorov SAS, SAS-F, forced SAS]
tags: [rans, hybrid-rans-les, eddy-viscosity, dg]
timestamp: 2026-10-27T20:42:00Z
---

# Scale-adaptive simulation

Scale-adaptive simulation (SAS) is an unsteady RANS approach of Menter and
co-workers in which the length-scale equation of a two-equation model
contains the von Kármán length scale

$$L_{\mathrm{vK}}=\kappa\frac{\lvert S\rvert}{\lvert\nabla^2\boldsymbol u\rvert},$$

built from the first and second velocity derivatives (registry §11
$L_{\mathrm{vK}}$). Where the flow develops resolved unsteadiness the second
derivatives grow, $L_{\mathrm{vK}}$ shrinks and the modelled length and eddy
viscosity follow, so that the model can, in the words of Jiang et al.
(2025), "change smoothly from LES to RANS modeling" without an explicit
grid length. It is listed with detached-eddy simulation among the
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) approaches. Its RANS
model is the $k$-$\sqrt kL$ (KSKL) model of Menter, Egorov & Rusch, derived
from Rotta's approach; the bundle's one source that prints it is Jiang et
al. (2025), whose subject is its first implementation in a high-order
discontinuous Galerkin solver ([Jiang et al. (2025)](/sources/jiang-2025.md),
§1–§2, App. A). Heinz (2020) prints the high-Reynolds-number form of the
Menter–Egorov model as a transport equation for $\nu_t$ itself, derives its
log-law calibration and the $k$-$\varepsilon$ and $k$-$\omega$ coefficients it
implies, and classes SAS with PANS and PITM as a "RANS-coefficient" hybrid
([Heinz (2020)](/sources/heinz-2020.md), §3.4, Eqs. 31–37). Sandberg &
Michelassi (2022) cite it as the example of a *unified* hybrid, one that
blends RANS and LES on flow, geometry and grid properties instead of on
predetermined zones ([Sandberg & Michelassi (2022)](/sources/sandberg-2022.md),
§2.2.2.2).

## The $k$-$\sqrt kL$ model

Jiang et al. transport $k$ and a length-scale variable $\Phi_L$
(registry §11, the source's $\Phi$, with the dimensions of $\sqrt k$ times a
length; the paper never writes $\Phi_L=\sqrt kL$ explicitly) in the
compressible RANS equations (App. A, Eqs. A1–A5; the source's $C_u$ read as
$C_\mu$, see Qualifications):

$$\begin{aligned}
\partial_t(\rho k)+\nabla\cdot(\rho k\boldsymbol u)&=\rho\hat P_k-C_\mu^{3/4}\rho\frac{k^2}{\Phi_L}-2\mu\frac{k}{d^2}+\nabla\cdot\big[(\mu+\sigma_k\mu_t)\nabla k\big],\\
\partial_t(\rho\Phi_L)+\nabla\cdot(\rho\Phi_L\boldsymbol u)&=C_{\phi1}\frac{\Phi_L}{k}\rho\hat P_k-C_{\phi2}\rho k-6\mu\frac{\Phi_L}{d^2}f_\phi+\nabla\cdot\big[(\mu+\sigma_\phi\mu_t)\nabla\Phi_L\big],
\end{aligned}$$

with the limited production $\rho\hat P_k=\min\big(\rho P_k,\,20C_\mu^{3/4}\rho k^2/\Phi_L\big)$
($\hat P_k$ page-local; $\rho P_k$ built on the full Boussinesq stress
including $-\tfrac23\rho k\delta_{ij}$, see the
[Boussinesq page](/definitions/boussinesq-hypothesis.md)) and

$$C_{\phi1}=\zeta_1-\zeta_2\Big(\frac{\Phi_L}{\sqrt k\,L_{\mathrm{vK}}}\Big)^2,\qquad C_{\phi2}=\zeta_3,\qquad f_\phi=\frac{1+C_{d1}\xi_d}{1+\xi_d^4},\qquad \xi_d=\frac{\rho d\sqrt{0.3k}}{20\mu}$$

($\xi_d$ the source's $\xi$, page-local, not the reference coordinate). The
von Kármán length is bounded as printed,
$\Phi_L/(C_{11}\sqrt k)<L_{\mathrm{vK}}<C_{12}\kappa d\,[\cdots]$, the upper
bound involving the ratio of production to destruction with an ambiguous
grouping (Eq. A4). Constants (A5): $\sigma_k=\sigma_\phi=2/3$, $\kappa=0.41$,
$C_\mu=0.09$, $C_{11}=10$, $C_{12}=1.3$, $\zeta_1=0.8$, $\zeta_2=1.47$,
$\zeta_3=0.0288$; $C_{d1}$ is used in $f_\phi$ but given no value.

The term that makes the model scale-adaptive is $-\zeta_2(\Phi_L/(\sqrt kL_{\mathrm{vK}}))^2$
in the production coefficient of the $\Phi_L$ equation: a small
$L_{\mathrm{vK}}$ lowers the production of $\Phi_L$ and hence the length
scale *(compiler check, not in the sources)*. The paper's computations are two-dimensional, where the Laplacian
magnitude is $\big[(\nabla^2u)^2+(\nabla^2v)^2\big]^{1/2}$ (A3). The
original eddy viscosity is not printed; the modified one below,
$\mu_t=C_\mu^{1/4}\rho\nu\psi$, reduces to $C_\mu^{1/4}\rho\Phi_L$ when the
surrogate equals $\Phi_L/\nu$ *(compiler check, not in the sources)*.

## The eddy-viscosity form and its log-law calibration

Heinz (2020) writes the model, derived from a corrected Rotta $kL$
equation, in its high-Reynolds-number form for the eddy viscosity
(§3.4, Eqs. 31–32):

$$\frac{D\nu_t}{Dt}=a^2k\big(\zeta_1-\zeta_2R_{\mathrm{SAS}}^2\big)-C_\mu^{1/4}\zeta_3k+\frac{\partial}{\partial x_j}\Big[\frac{\nu_t}{\sigma_\Phi}\frac{\partial\nu_t}{\partial x_j}\Big],$$

$$a=-\frac{R_{12}}{k}=\frac{\nu_t\lvert S\rvert}{k},\qquad R_{\mathrm{SAS}}=\frac{C_\mu^{3/4}L}{L_{\mathrm{vK}}},\qquad L=\frac{\nu_t}{C_\mu k^{1/2}},\qquad L_{\mathrm{vK}}=\kappa\Big\lvert\frac{\lvert S\rvert}{S'}\Big\rvert,\qquad S'=\Big[\frac{\partial^2\langle u_i\rangle}{\partial x_k^2}\frac{\partial^2\langle u_i\rangle}{\partial x_j^2}\Big]^{1/2},$$

with $a$, $R_{\mathrm{SAS}}$ and $S'$ page-local, $\lvert S\rvert$ with the
registry's factor two (the source's $S$), and $\sigma_\Phi$ the diffusion
constant, a divisor of $\nu_t$ (the source's own symbols).
In the log layer $C_\mu^{3/4}L=L_{\mathrm{vK}}=\kappa y$, so
$R_{\mathrm{SAS}}=1$, and log-law consistency requires (Eq. 33)

$$\sigma_\Phi C_\mu^{1/2}\big(\zeta_2-\zeta_1+C_\mu^{-3/4}\zeta_3\big)=\kappa^2 .$$

Heinz's "standard settings" $(\zeta_1,\zeta_2,\zeta_3,\sigma_\Phi)=(0.8,1.47,0.0288,2/3)$
with $C_\mu=0.09$ gives $\kappa=0.41$, which Heinz states; these are the
values Jiang et al. (2025) list for the $k$-$\sqrt kL$ model, though their
$\sigma_\phi=2/3$ multiplies $\mu_t$ in the $\Phi_L$ diffusion while Heinz's
$\sigma_\Phi$ divides $\nu_t$. The left side evaluates to $0.1691$, $\kappa=0.411$
*(compiler check, not in the sources)*. Rewritten as $\varepsilon$ and
$\omega$ equations (Eqs. 34–36), the model carries the factor
$1+\zeta_2R_{\mathrm{SAS}}^2/C_{\varepsilon1}$ on $P_k/\varepsilon$, and the
equivalent coefficients (Eq. 37) are $C_{\varepsilon1}=2-\zeta_1=1.2$ and
$C_{\varepsilon2}=2-\zeta_3C_\mu^{-3/4}=1.82$, against 1.44 and 1.92 of the
standard [$k$-$\varepsilon$ model](/methods/k-epsilon-model.md); in Heinz's
$k$-$\omega$ form, whose $\omega=\varepsilon/k$ carries no $C_\mu$ (unlike the
registry's $\omega$), the coefficients are $0.2$ and $0.82$. Heinz states the
mechanism: resolved fluctuations reduce $L_{\mathrm{vK}}$, so $R_{\mathrm{SAS}}>1$ and the production of
$\nu_t$ drops, lowering the modelled viscosity (§3.4).

## High-order discontinuous Galerkin implementation

Jiang et al. state that, to their knowledge, KSKL had been developed and
assessed only in finite-volume codes (§1). In a modal (Taylor-basis) DG
solver with a local Lax–Friedrichs flux, BR2 viscous fluxes, preconditioned
GMRES for steady and ESDIRK for unsteady runs, they add three devices
(§2–§3):

1. **Hermite-WENO limiting of $k$.** Oscillations of $k$ near the
   under-resolved boundary-layer edge, where the $k$ profile changes slope
   rapidly, are detected by an element-resolution indicator and the
   polynomial of $k$ in the troubled cells is replaced by a Hermite-WENO
   reconstruction, the one the authors use for shocks (§3.1; see
   [WENO schemes](/methods/weno-scheme.md) and
   [shock sensors](/definitions/shock-sensor.md)).
2. **A positive surrogate of $\Phi_L$.** Following Moro et al.'s treatment
   of the [Spalart–Allmaras](/methods/spalart-allmaras-model.md) variable,
   with $\chi_\Phi=\Phi_L/\nu$ (registry §11),
   $$\psi=\begin{cases}0.02\log\big(1+e^{50\chi_\Phi}\big),&\chi_\Phi\le5,\\ \chi_\Phi,&\chi_\Phi>5,\end{cases}$$
   and $\nu\psi$ replaces $\Phi_L$ in all source terms and in the eddy
   viscosity $\mu_t=C_\mu^{1/4}\rho\nu\psi$, while $\Phi_L$ remains the
   transported variable (Eqs. 10–13). $\psi$ is positive whatever $\Phi_L$,
   so $\mu_t$ is positive. The two branches join at $\chi_\Phi=5$ only with
   the natural logarithm, which the paper does not specify
   *(compiler check, not in the sources: $0.02\ln(1+e^{250})=5.000$)*.
3. **Compact second derivatives.** $L_{\mathrm{vK}}$ needs second velocity
   derivatives whose order matches the first derivatives and whose stencil
   stays on face neighbours; central differencing of the kind used in finite
   volumes fails both in DG. The authors $L^2$-project the first
   derivatives onto the element basis and take the gradient of the
   projection corrected by the BR2 global lift operator,
   $\boldsymbol g_h=\nabla\boldsymbol s_h+\boldsymbol R_h$ (page-local:
   $\boldsymbol s_h$ the projected first derivatives, $\boldsymbol R_h$ the
   sum of the face lifts of the jumps already formed for the viscous
   fluxes), against a "local derivative method" $\nabla\boldsymbol s_h$
   alone (§3.2, Eqs. 14–20).

## Evidence

All from Jiang et al. (2025, §4), two-dimensional:

- **Turbulent flat plate**, $M=0.3$, $Re=3\times10^6$ on the plate length,
  three meshes ($y^+\approx1$, 0.6, 0.4), $N=1$–3. With explicit Runge–Kutta
  the stabilized method shows much less oscillation of the residual; with
  GMRES the computation diverges without the stabilization and drops
  5–6 orders with it at $N=2$ and 3. The lift-operator derivative removes
  an anomaly of $L_{\mathrm{vK}}$ near $y^+\approx3000$ given by the local
  derivative. Velocity profiles agree with the viscous-sublayer and log
  laws, and $C_f$ improves with grid and order; near the leading edge a
  laminar-looking region grows with grid density and order, which the
  authors, citing Rumsey, call a numerical effect, not physical transition
  (§4.1, Figs. 1–4; see
  [turbulent boundary layer](/benchmarks/turbulent-boundary-layer.md)).
- **RAE2822 airfoil**, $M=0.734$, $Re=6.5\times10^6$, $\alpha=2.79^\circ$,
  8958 elements, Hermite-WENO shock limiting: $C_L=0.779$ ($N=2$) and 0.782
  ($N=3$), $C_D=0.0177$ and 0.0176, against 0.803 and 0.0168 measured,
  errors "around the range of 3% and 5%"; $L_{\mathrm{vK}}$ oscillates at
  the shock without visibly affecting $\mu_t$ (§4.2, Figs. 6–7).
- **Square cylinder**, $Re=10^4$, $M=0.05$, $N=3$: through
  $L_{\mathrm{vK}}$ the model gives a smaller eddy viscosity than
  Spalart–Allmaras in the separated wake and "slightly chaotically vortex
  flows", which the authors call SAS-like; mean velocities agree with a 2D
  DNS above the cylinder and follow its trend in the wake (§4.3; details on
  [square-cylinder flow](/benchmarks/square-cylinder-flow.md)).

**Comparisons reported by other sources.** On four 25° [Ahmed bodies](/benchmarks/ahmed-body.md),
Delassaux et al. (2023) report from their own calibration that SAS, SST-DDES
and stress-blended eddy simulation all separate and reattach on the slant,
SAS overestimating the recirculation length, and that SST-DDES is closest
to experiment, which is why they select it
([Delassaux et al. (2023)](/sources/delassaux-2023.md), §5; see
[detached-eddy simulation](/methods/detached-eddy-simulation.md)). Haering
et al. (2022) recall that the forced variant SAS-F of Menter et al., which
adds resolved fluctuations at the RANS/LES interface, still showed
[log-layer mismatch](/definitions/log-layer-mismatch.md) in channel flow
([Haering et al. (2022)](/sources/haering-2022.md), §II). Liu et al. (2024)
list DES, SAS and related hybrids as too expensive for routine
turbomachinery design ([Liu et al. (2024)](/sources/liu-2024.md),
Introduction). In Heinz's compilation of published
[periodic-hill](/benchmarks/periodic-hill.md) results, SAS is among the
methods (with source-term methods and unified RANS-LES) that "apparently
reduce the RANS error significantly", while PANS, PITM, DES and
wall-modelled LES show large variability through their design parameters
(Heinz (2020), §5.1, Fig. 6; compiled from the literature, no new runs).
Mani & Dorgan (2023) count SST-based hybrids among Boeing's unsteady
tools, citing among them Winkler et al. (2011), a paper on scale-adaptive
simulations on unstructured grids, beside DES-type variants; the review
gives no SAS formulation or result ([Mani & Dorgan (2023)](/sources/mani-2023.md),
§4.5.2). Idelsohn et al. (2024) name SAS, with DES and PANS, as a global
hybrid model in which the large eddies are resolved away from walls and the
boundary layers are covered by a RANS model
([Idelsohn et al. (2024)](/sources/idelsohn-2024.md), §1.2).

## Qualifications

- **Two dimensions.** Jiang et al.'s "SAS-like" behaviour comes from 2D
  URANS, which the authors call a verification, not a validation, and they
  defer a fair comparison to three-dimensional DES or SAS (§4.3). Their
  long-term goal is hybrid RANS/LES with DG (§5).
- **Where the surrogate departs from $\Phi_L$.** With the natural
  logarithm, Eq. 10 gives $\psi-\chi_\Phi=0.02\ln\big(1+e^{-50\chi_\Phi}\big)$
  on the first branch: about $1.3\times10^{-4}$ (0.13% of $\chi_\Phi$) at
  $\chi_\Phi=0.1$, $1.6\times10^{-3}$ (3%) at $\chi_\Phi=0.05$, and
  $0.02\ln2\approx0.014$ at $\chi_\Phi=0$, so $\nu\psi$ differs appreciably
  from $\Phi_L$ only for $\chi_\Phi\lesssim0.1$ and for negative $\Phi_L$
  *(compiler check, not in the sources)*. The paper presents the device as
  a positivity safeguard and does not quantify this departure (§3.1).
- **Printed slips.** Eqs. 4, 11, A1 and A2 print a constant $C_u^{3/4}$
  where Eq. 13, A4 and the constant list use $C_\mu$, and A5 defines no
  $C_u$; Eqs. 11–12 use the unlimited production $P_k$ where A1 uses the
  limited one; $C_{d1}$ has no value; $\kappa$ denotes both the thermal
  conductivity and the von Kármán constant.

# Citations

- [Jiang et al. (2025)](/sources/jiang-2025.md) — §1–§3 Eqs. 6, 10–20, §4.1–4.3 Figs. 1–11, §5, App. A Eqs. A1–A5.
- [Delassaux et al. (2023)](/sources/delassaux-2023.md) — §5 (HAL author manuscript).
- [Haering et al. (2022)](/sources/haering-2022.md) — §II.
- [Liu et al. (2024)](/sources/liu-2024.md) — Introduction.
- [Heinz (2020)](/sources/heinz-2020.md) — §3.4 Eqs. 31–37, §5.1 Fig. 6.
- [Sandberg & Michelassi (2022)](/sources/sandberg-2022.md) — §2.2.2.2.
- [Mani & Dorgan (2023)](/sources/mani-2023.md) — §4.5.2.
- [Idelsohn et al. (2024)](/sources/idelsohn-2024.md) — §1.2.
