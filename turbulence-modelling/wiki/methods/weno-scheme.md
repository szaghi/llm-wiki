---
type: Method
title: "WENO and hybrid shock-capturing schemes in scale-resolving simulation"
description: "WENO and TENO schemes capture shocks by nonlinear weighting or selection of candidate stencils; in compressible turbulence their dissipation is reduced by optimized weights, adaptive cut-offs, linear weights in smooth flow or hybrids with central and jump reconstructions, they serve as DG limiters, and in implicit LES as the subgrid dissipation."
status: established
aliases: [WENO, TENO, targeted ENO, weighted essentially non-oscillatory scheme, WENO-Z, WENO-Z+, WENO-Z+M, WENO-ZQ, WENO-SYMBO, HWENO, Hermite WENO, bandwidth-optimized WENO, limiter-optimized WENO, hybrid upwind/WENO scheme, hybrid central/WENO scheme, TENO-THINC, TENO-S, TENOA, THINC, TENO limiter, boundary variation diminishing]
tags: [shock-capturing, numerical-dissipation, dns, compressible, implicit-les, gpu]
timestamp: 2026-10-27T06:08:00Z
---

# WENO and hybrid shock-capturing schemes in scale-resolving simulation

A **weighted essentially non-oscillatory (WENO)** scheme builds the
interface flux (or reconstructed interface state) of a finite-difference or
finite-volume method from several candidate stencils, combined with
solution-dependent nonlinear weights that favour the smooth stencils near a
discontinuity; with the weights frozen at their linear (optimal) values the
same construction is a linear upwind-biased scheme on the full stencil, the
"linear weights" option that [Cao et al. (2022)](/sources/cao-2022.md),
Remark 1, use for smooth low-speed flows. In this bundle WENO matters as
the shock-capturing core of compressible [DNS](/definitions/direct-numerical-simulation.md)
and LES of boundary layers and shock interactions, and as the source of the
dissipation of [implicit LES](/definitions/implicit-les.md). Its
dissipation, harmless at shocks, is the property every source works around
in turbulence (see [numerical dissipation](/properties/numerical-dissipation.md)).

## Variants in the sources

| Variant | Use | Source |
|---|---|---|
| Fifth- and seventh-order WENO (Jiang–Shu) | options of the OpenCFD-SCU library; fifth order near non-periodic boundaries and at the strongest shocks of the hybrid | Dang et al. (2022), §2.2.3, Table 2 |
| Seventh-order WENO-SYMBO (bandwidth-optimized WENO of Martín et al.), same stencil as an eighth-order central scheme | inviscid fluxes of the Mach 2.9 compression-ramp DNS | Dang et al. (2022), §5.1, §6.1 |
| Fourth-order WENO, linearly and nonlinearly (bandwidth) optimized, with absolute and relative limiters and near-wall filtering of the candidate weights | LES of hypersonic shock/boundary-layer interactions | Helm & Martín (2022), §II |
| Seventh-order WENO "optimized by means of limiters" (relative to Jiang–Shu) | DNS of hypersonic boundary layers | Huang et al. (2022), §2.2 |
| Fifth-order WENO with linear weights; WENO-Z with characteristic-variable reconstruction | reconstruction of the [gas-kinetic scheme](/methods/high-order-gas-kinetic-scheme.md): linear weights for the Taylor–Green vortex and channel, WENO-Z for supersonic isotropic turbulence | Cao et al. (2022), Remark 1, §3.4 |
| WENO switched on by the Ducros sensor over energy-preserving central schemes | [STREAmS](/software/streams.md) DNS of supersonic and hypersonic boundary layers | Cogo et al. (2022), §2 |
| Fifth-order WENO for the convective terms | STREAmS implicit LES of a Mars entry capsule wake | Placco et al. (2023), §2 |
| Seventh-order WENO with linear weights (normal direction); fifth-order WENO-Z-type baseline; fifth-order Hermite WENO (HWENO) on a three-cell stencil of cell averages and cell-averaged derivatives | reconstructions of the gas-kinetic scheme used as implicit LES of the Taylor–Green vortex and channel flow | [Zhao et al. (2023a)](/sources/zhao-2023.md), §3 |
| Fifth-order WENO (Jiang–Shu and WENO-Z cited), dimension by dimension | reconstruction kernel of the single- and multi-GPU gas-kinetic DNS code | [Wang et al. (2023b)](/sources/wang-2023-b.md), §2, §3.1 |
| Ducros-sensor hybrid of the KGP split form and an HLLC upwind flux (WENO hybridization cited in §1 as a stabilization of divergence-form schemes) | comparison scheme for density-wave advection in real-gas flow | [Bernades et al. (2023)](/sources/bernades-2023.md), §1, §4.1.1 |
| Fifth-order WENO (Jiang–Shu) and third-order MUSCL | comparison schemes in the inviscid Taylor–Green time-reversal test, against a second-order kinetic-energy-preserving scheme and an optimized sixth-order linear upwind scheme | [Wang et al. (2024)](/sources/wang-2024.md), §3.1 |
| Sixth-order TENO (targeted ENO, cutoff $C_T=10^{-6}$, local Lax–Friedrichs splitting) | OpenSBLI reference and test solver of the supersonic Taylor–Green vortex, up to $2048^3$ | [Chapelier et al. (2024)](/sources/chapelier-2024.md), §II.C, §III.B.c |
| Eighth-order kinetic-energy- and entropy-preserving central scheme blended with a third-order upwind/WENO flux by a linear homotopy in the Ducros sensor | SPADE, same comparison | Chapelier et al. (2024), §III.B.b, h |
| Fifth-order WENO of the Jacobian and Jacobian-weighted conservative variables in computational space | curvilinear gas-kinetic scheme used as implicit LES of a compressible channel and a periodic hill | [Cao et al. (2024)](/sources/cao-2024.md), §2.3 |
| Fifth-order WENO (Jiang–Shu) for the inviscid fluxes, second-order central viscous fluxes, implicit dual time stepping | zonal hybrid RANS/LES of a hydrogen-fuelled scramjet combustor | [Tang et al. (2022)](/sources/tang-2022.md), §2.1 |
| Fifth-order WENO during the initial transient only, then sixth-order central (kinetic-energy- and entropy-preserving) fluxes | STREAmS DNS of thermally perfect CO$_2$ channel flow at bulk Mach 3–5 | [Aiello et al. (2026)](/sources/aiello-2026.md), §3.3 |
| Fifth-order WENO-Z+ (Acker et al., recalled) and the authors' WENO-Z+M, with weights above the ideal ones for the least smooth substencil | one- and two-dimensional Euler shock tests, one Navier–Stokes shock/shear-layer test | [Luo & Wu (2021)](/sources/luo-2021-b.md), §2.3, §3.2 |
| Fifth-order WENO (Jiang–Shu, $\epsilon=10^{-6}$) applied component-wise to primitive variables, in both the conservative shock update and the primitive smooth-flow update of a sensor-switched hybrid | inviscid transcritical (real-gas) flow, no turbulence | [Xu et al. (2026)](/sources/xu-2026.md), §3.2–3.5 |
| Truly two-dimensional fourth-order WENO-ZQ: a cubic polynomial on a 13-cell stencil blended with four linear ones | semi-Lagrangian finite-volume transport of Vlasov and two-dimensional incompressible Euler problems, no turbulence | [Zheng et al. (2022)](/sources/zheng-2022.md), §2.2 |
| Fifth-order TENO (TENO5, $C_T=10^{-5}$) hybridized with a THINC jump reconstruction by a parameter-free pattern of TENO flags | finite-difference shock tests and the inviscid Taylor–Green vortex, $64^3$ | [Takagi et al. (2022)](/sources/takagi-2022.md), §2–4 |
| TENO-S: eight-point TENO with adaptive cut-off in troubled cells, optimized sixth-order skew-symmetric flux elsewhere, switched by an eight-point indicator | shock tests, inviscid and viscous Taylor–Green vortex, decaying compressible isotropic turbulence, $64^3$–$128^3$ | [Liang & Fu (2024)](/sources/liang-2024.md), §3–4 |
| Five-, six- and seven-point TENO with adaptive dissipation (TENO5A–TENO7A), THINC at interfaces and flagged jumps, a posteriori MOOD fallback | finite-volume diffuse-interface two-phase flow (open-source MFC), inviscid, no turbulence | [Li & Fu (2024)](/sources/li-2024-c.md), §3 |
| TENO troubled-cell indicator and TENO limiter of the higher modes for third-order modal Runge–Kutta DG | inviscid Euler tests, uniform Cartesian grids | [Huang & Fu (2024)](/sources/huang-2024.md), §4–5 |
| TENO-THINC limiter with a compact boundary-variation-diminishing selector, same RKDG and indicator | inviscid Euler tests, uniform Cartesian grids | [Huang et al. (2025)](/sources/huang-2025.md), §3–4 |
| Hermite WENO (HWENO) limiting of the turbulent kinetic energy and, at shocks, of the mean flow in modal DG | steady and unsteady RANS with the $k$-$\sqrt kL$ model | [Jiang et al. (2025)](/sources/jiang-2025.md), §3.1, §4.2 |
| Seventh-order WENO-Z interpolation of primitive variables inside a PPM Godunov scheme (PeleC) | $512^3$ DNS of decaying compressible isotropic turbulence, reference of an a priori study | [Valencia et al. (2026)](/sources/valencia-2026.md), §IV |

The upwind schemes act on split fluxes or on characteristic variables.
[OpenCFD-SCU](/software/opencfd-scu.md) splits the flux with Steger–Warming
flux-vector splitting, $f=f^++f^-$ with eigenvalues split as
$\lambda^\pm=(\lambda\pm|\lambda|)/2$, and differences each part upwind;
optionally it projects onto characteristic variables, which raises
robustness and reduces spurious oscillations at higher cost (Dang et al.
2022, §2.2.1–2.2.2, Eqs. 19–40). Dang et al. (§2.2) state that upwind
differencing after flux-vector splitting is more stable than central or
spectral discretization of the convective term and suppresses aliasing
error. Cao et al. (2022, Remark 1) reconstruct characteristic variables at
each Gauss point for their supersonic cases.

## Dissipation in turbulence

- **Too dissipative as is.** Dang et al. (2022, §1) state that the
  dissipation of seventh-order WENO is still too high for good DNS data and
  that the seventh-order WENO used by Pirozzoli & Grasso "could have led to a
  reduction in computational accuracy" (a judgment, not shown). Helm &
  Martín (2022, §III C), recalling Wu & Martín, note that excess numerical
  dissipation suppresses the wall-pressure plateau of a separated
  compression-ramp interaction, which their limited WENO reproduces.
- **Measured irreversibility.** Wang et al. (2024, §3.1, Fig. 2) run the
  inviscid [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) on
  $30^3$ to $t=20L/V_0$, reverse the flow and run to $t=40L/V_0$: the
  second-order kinetic-energy-preserving KGP2 scheme keeps the kinetic
  energy constant and returns to the initial vorticity field, while
  fifth-order WENO, third-order MUSCL and their optimized sixth-order
  upwind OPT6 lose energy monotonically and do not, MUSCL3 departing most.
  They nonetheless recommend the dissipative OPT6 over KGP2 for budgets of
  the turbulent kinetic energy because of its lower dispersion (see
  [low-dissipation low-dispersion schemes](/methods/low-dissipation-low-dispersion-scheme.md));
  WENO is not run in their LES.
- **Remedies within WENO.** Bandwidth optimization and limiters lower the
  dissipation of the nonlinear weights (Helm & Martín 2022, §II; Huang et
  al. 2022, §2.2); linear weights avoid "the numerical dissipation from
  artificially created interface discontinuity" in smooth flow (Cao et al.
  2022, Remark 1).
- **Replacing WENO in smooth regions.** Huang et al. (2022, §2.2) use for
  their adiabatic Mach 2.5 case the eighth-order split-convective central
  scheme of Pirozzoli, which "runs about twice as fast as the conventional
  WENO method" and was shown robust up to edge Mach 4. The hybrids below do
  the same locally.
- **As an implicit subgrid model.** Placco et al. (2023, §2) omit a subgrid
  model and let "the numerical dissipation given by the numerical
  discretisation" act "as artificial viscosity at small scales", citing
  boundary-layer studies where this implicit LES gave results comparable to
  coarse DNS; the convective terms use fifth-order WENO, the viscous terms
  sixth-order central differences, and no switching to a central convective
  scheme is mentioned. Cao et al. (2022, §3.1) read
  the grid-independent agreement of their kinetic-energy dissipation as
  support for implicit LES with the gas-kinetic scheme. Zhao et al. (2023a,
  §5.1) find the fifth-order (linear-weight) reconstruction of that scheme
  "still over-dissipative" as implicit LES and reduce the measured numerical
  dissipation by raising the order to seven or by the compact HWENO
  reconstruction, which also brings the realized $Re_\tau$ of channel flow
  closer to DNS; with $2\times2$ Gauss points per face, however, their
  seventh-order reconstruction converges at only about fourth order in a
  smooth advection test (§4, Table 3). The two verdicts on the fifth-order
  scheme are recorded as an open contradiction on
  [high-order gas-kinetic schemes](/methods/high-order-gas-kinetic-scheme.md).

## Nonlinear weights and the dissipation of the linear scheme

[Luo & Wu (2021)](/sources/luo-2021-b.md), a short note on fifth-order WENO
for hyperbolic conservation laws without turbulence content, separate two
sources of dissipation in a WENO scheme: the linear dissipation of the
underlying fifth-order upwind scheme (UD5, all weights at their ideal
values) and the nonlinear dissipation of the weighting (§4). Page-local
notation: $d_k=(1/10,6/10,3/10)$ the ideal weights of the three
substencils $k=0,1,2$, $\mathsf w_k$ the nonlinear weights, $\mathrm{IS}_k$ the
Jiang–Shu smoothness indicators (the source's $\beta_k$, renamed because
$\alpha_k$, $\beta_k$ are the kinetic-energy fractions of registry §11),
$\mathrm{IS}_{\mathrm G}=|\mathrm{IS}_2-\mathrm{IS}_0|$ the
global indicator (the source's $\tau_5$), $r_k=(\mathrm{IS}_{\mathrm G}+\epsilon)/(\mathrm{IS}_k+\epsilon)$
(the source's $\xi_k$), $\epsilon=10^{-40}$. With the WENO-Z exponent 2
(Eqs. 4–9):
$$\begin{aligned}
\text{WENO-Z:}\quad &\mathsf w_k=\frac{a_k}{\sum_la_l},\qquad a_k=d_k\big(1+r_k^2\big),\\
\text{WENO-Z+:}\quad &a_k=d_k\big(1+r_k^2+\lambda_{\mathrm Z}\,r_k^{-1}\big),\\
\text{WENO-Z+M:}\quad &a_k=d_k\big(1+r_k^2+\lambda_{\mathrm Z}\,z_{\mathrm M}\,r_k^{-1/2}\big),\qquad z_{\mathrm M}=\frac{1+r_{\min}^2}{\sum_kd_k\big(1+r_k^2\big)},
\end{aligned}$$
with $\lambda_{\mathrm Z}$ (page-local, the source's $\lambda$) the
coefficient of the extra term and $r_{\min}=\min_kr_k$, which belongs to
the least smooth substencil.

- **Why weights above ideal.** In WENO-Z the weight of the least smooth
  substencil is always below its ideal value; the extra term of WENO-Z+
  raises it (§1). The authors' interpretation: a weight below ideal adds
  positive dissipation, as in all earlier WENO schemes, which are
  therefore more dissipative than their linear scheme; a weight above ideal
  adds negative dissipation that offsets part of the linear dissipation
  (§4, Figs. 5–7). They present this as an alternative to optimized linear
  coefficients (see
  [low-dissipation low-dispersion schemes](/methods/low-dissipation-low-dispersion-scheme.md)),
  against the view that nonlinear mechanisms always hurt spectral
  properties (§6).
- **The risk.** By the approximate dispersion relation (computed
  numerically for nonlinear schemes, after Pirozzoli), WENO-Z+ with
  Acker et al.'s $\lambda_{\mathrm Z}=\Delta x^{2/3}$ has negative
  dissipation in a band of reduced wavenumbers near 1.1834, which lowering
  $\lambda_{\mathrm Z}$ hardly removes (§3.1, Fig. 1). WENO-Z+M weakens the
  extra term by the square root ($r_k^{-1/2}$, the smallest root the
  authors found free of negative dissipation) and scales it by
  $z_{\mathrm M}$, the ratio of the WENO-Z weight of the least smooth
  substencil to its ideal weight, which is $1+O(\Delta x^6)$ in smooth flow
  and $O(\Delta x^4)$ at discontinuities (orders cited, §3.2, Eqs. 7–9).
  The constant is then raised to $\lambda_{\mathrm Z}=579$, the largest
  value with which the interacting-blast-wave problem runs ($580$ fails)
  (§3.2).
- **Results.** In the two-dimensional Euler accuracy test the WENO-Z+M
  errors at $641\times641$ are $L_1=0.3913\times10^{-13}$ against
  $0.7896\times10^{-13}$ for UD5, about half (§5.3.1, Table 1); at
  $21\times21$ they are larger than UD5's ($0.4060\times10^{-5}$ against
  $0.2612\times10^{-5}$), and WENO-Z+M is ahead only from $81\times81$ on
  (Table 1). In the shock tests (Shu–Osher, Titarev–Toro, Lax, interacting
  blast waves, two-dimensional Riemann problem, double Mach reflection,
  forward-facing step, shock/shear-layer interaction) the authors report
  better resolution than WENO-Z, WENO-Z+, ninth-order WENO-Z and WENO-IS-I,
  by visual comparison of the figures (§5); WENO-Z+ "falsely amplifies"
  the smooth waves of the Titarev–Toro problem (§5.2.3, Fig. 11).

## Hybrid schemes

**Sensor-switched upwind/WENO (OpenCFD-SCU).** Dang et al. (2022, §2.2.3,
Eqs. 41–43) blend three schemes by a modified Jameson pressure sensor,
evaluated in each direction and summed:
$$\phi_i=\frac{|-p_{i-1}+2p_i-p_{i+1}|}{p_{i-1}+2p_i+p_{i+1}},\qquad \theta_J=\phi_i+\phi_j+\phi_k$$
(page-local $\phi$, $\theta_J$, the source's $\theta$, renamed because
$\theta$ is the momentum thickness; $i,j,k$ the grid directions). With
thresholds $\theta_1=0.02$ and $\theta_2=0.1$ ("usually"),
$\theta_J\le\theta_1$ selects a linear seventh-order upwind flux,
$$f^*_{j+1/2}=\frac{-3f_{j-3}+25f_{j-2}-101f_{j-1}+319f_j+214f_{j+1}-38f_{j+2}+4f_{j+3}}{420},$$
$\theta_1<\theta_J\le\theta_2$ seventh-order WENO, and larger $\theta_J$
fifth-order WENO. The authors state that more than 90% of the points use the
upwind scheme, that switching artefacts are slight because all three schemes
are above fifth order, and that with characteristic reconstruction the
simulation "can be guaranteed not to diverge, provided the time step is
appropriate" (no proof or test given). The upwind coefficients sum to one
*(compiler check, not in the sources)*.

**Energy-preserving central/WENO (STREAmS).** Cogo et al. (2022, §2) apply
"consolidated, high-order, energy-preserving schemes" in shock-free regions,
"free of numerical dissipation", and WENO only where the Ducros sensor flags
shocks (see [kinetic-energy preservation](/properties/kinetic-energy-preservation.md)).
The same Ducros dilatation–vorticity factor weights the shock sensor of the
second-order unstructured [LD2C scheme](/methods/low-dissipation-low-dispersion-scheme.md)
(Carlsson et al. 2023), whose conclusion (§5) credits the vorticity-weighted
sensor with better resolved shear stress and grey-area mitigation in the
initial shear layer of a supersonic base flow, compared with the Jameson
sensor alone; in that comparison the dissipation coefficient and the face
extrapolation change too (Table 1).

**Homotopy hybrid (SPADE).** In Chapelier et al. (2024, §III.B.b) the
central kinetic-energy- and entropy-preserving scheme of Kuya et al. and
Totani et al. (order 8 in their runs; orders 2 to 8 available) and a
third-order upwind reconstruction are combined by a linear homotopy whose
parameter is the Ducros sensor, which tends to 0 where the vorticity
magnitude dominates the dilatation and to 1 otherwise (§III.B.h). No
subgrid model is used.

Dang et al. (2022, §1) add that for Mach numbers "generally exceeding 6" a
dissipative scheme is usually introduced for robustness at strong shocks.

**Conservative WENO at shocks, primitive update elsewhere.**
[Xu et al. (2026)](/sources/xu-2026.md) switch, cell by cell, between a
conservative finite-volume update (WENO-5 reconstruction of the primitive
variables and a real-gas Roe flux) where a pressure-ratio sensor built on
the primitive-variable Riemann solver detects a compressive jump (Eq. 18,
threshold 0.05), and a non-conservative primitive-variable update
elsewhere, which preserves pressure equilibrium at transcritical density
interfaces (§3; see
[pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)).
They reconstruct primitive variables component by component "to avoid
characteristic projections through potentially ill-conditioned real-gas
eigenstructures near the critical point" (§3), and stress that a two-point
central difference of fifth-order WENO interface states is only second
order (§3.5, §4.2).

**WENO as the fallback of non-entropy-conserving central schemes.**
[Aiello et al. (2026)](/sources/aiello-2026.md) run their thermally perfect
channel DNS fully central after a WENO5 transient (§3.3) and note that the
non-entropy-conserving schemes they test (KEEP, Ranocha's) would in practice
be coupled with WENO-type procedures, which "could potentially mitigate
such issues" at "the price of" reduced formal cleanliness and added
dissipation, whereas the
[entropy-conserving](/properties/entropy-conservation.md) schemes needed no
shock capturing in these shock-free cases (§4.2).

**Upwind hybrids at density interfaces.** Bernades et al. (2023, §1) list
HLLC and WENO hybridization, with filtering, as the stabilization of the
divergence-form schemes used for transcritical (real-gas) flows, and note
that it adds dissipation. In their ideal-gas density-wave test (§4.1.1,
Fig. 1) a hybrid that switches between the KGP split form and HLLC by the
Ducros sensor dissipates the density wave at a slightly lower rate than pure
HLLC, the sensor being "mostly activated by the oscillations" of the
non-pressure-equilibrium-preserving central scheme (see
[pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)).

## TENO: stencil selection by scale separation

Targeted ENO (TENO, Fu, Hu & Adams, as recalled by
[Takagi et al. 2022](/sources/takagi-2022.md), §2.2, and
[Liang & Fu 2024](/sources/liang-2024.md), §2.2) keeps WENO's convex
combination of candidate fluxes but replaces the smooth weighting by an
ENO-like on/off selection. Page-local notation, extending the one above:
$K$ the number of points of the full stencil, $k=0,\dots,K-3$ the
candidate stencils of **incremental width** (three three-point stencils,
then one each of four, five, … points), $\mathrm{IS}_k$ their Jiang–Shu
indicators, $\mathrm{IS}_{\mathrm G}$ a global reference indicator (the
sources' $\tau_K$), $\gamma^{\mathrm T}_k$, $\chi^{\mathrm T}_k$ the
scale-separated and normalized smoothness measures,
$\delta^{\mathrm T}_k\in\{0,1\}$ the stencil flag, $C_T$ the cut-off
threshold (the sources' $\gamma_k$, $\chi_k$, $\delta_k$, $C_T$; the
superscript keeps them apart from the ratio of specific heats, the
Spalart–Allmaras ratio and the boundary-layer thickness), $d_k$ the optimal
(linear) weights:
$$\gamma^{\mathrm T}_k=\Big(1+\frac{\mathrm{IS}_{\mathrm G}}{\mathrm{IS}_k+\epsilon}\Big)^q,\qquad
\chi^{\mathrm T}_k=\frac{\gamma^{\mathrm T}_k}{\sum_l\gamma^{\mathrm T}_l},\qquad
\delta^{\mathrm T}_k=\begin{cases}0,&\chi^{\mathrm T}_k<C_T\\1,&\text{otherwise}\end{cases},\qquad
\mathsf w_k=\frac{d_k\delta^{\mathrm T}_k}{\sum_ld_l\delta^{\mathrm T}_l},$$
with $q=6$ and $\epsilon=10^{-40}$ (Takagi et al. 2022, Eqs. 8–14; Liang &
Fu 2024, Eqs. 12–20). A stencil is either dropped or used with its
optimal weight, so in smooth flow, where every flag is 1, the scheme is
exactly its background linear scheme up to intermediate wavenumbers. For
TENO5 the three stencils are numbered central, right-biased, left-biased,
with $d_k=(6,3,1)/10$ and $\mathrm{IS}_{\mathrm G}=|\mathrm{IS}_1-\mathrm{IS}_2|$
(Takagi et al., Eq. 7, §2.2.2; Luo & Wu's numbering above is
left, central, right). For six and more points a sixth-order reference
$\mathrm{IS}_{\mathrm G}=|\mathrm{IS}_K-\tfrac16(\mathrm{IS}_1+\mathrm{IS}_2+4\mathrm{IS}_0)|$
is used (Liang & Fu, Eq. 15; [Li & Fu 2024](/sources/li-2024-c.md),
Eq. 40). Every candidate contains at least one upwind point, which the
sources credit for the stability of even-order TENO up to ten points and
eighth order (Takagi et al. §2.2.1; Li & Fu §3.2.1).

**The cut-off as the dissipation control.** $C_T$ sets the wavenumber at
which a stencil is judged non-smooth: Takagi et al. use $10^{-5}$ for
TENO5 "as a compromise of low numerical dissipation and good numerical
robustness" (§2.2.3), Chapelier et al. $10^{-6}$ for TENO6 (above), and
the TENO-S and TENOA families adapt it to a first-order discontinuity
strength $m\in[0,1]$ built from undivided differences (after Ren et al.):
$$m=1-\min\Big(1,\frac{\varrho_{i+1/2}}{C_r}\Big),\qquad
\varrho_i=\frac{|2\Delta f_{i+1/2}\Delta f_{i-1/2}|+\epsilon}{(\Delta f_{i+1/2})^2+(\Delta f_{i-1/2})^2+\epsilon},\qquad
C_T=10^{-\lfloor b\rfloor},\quad b=A_1-A_2\big(1-g(m)\big),\quad g(m)=(1-m)^4(1+4m),$$
with $\Delta f_{i+1/2}=f_{i+1}-f_i$ and $\varrho_{i+1/2}$ the minimum of
$\varrho$ over a few cells around the face ($\varrho$, $A_1$, $A_2$, $b$,
$C_r$ page-local; the sources' $\eta$, $\alpha_1$, $\alpha_2$, $\beta$).
Liang & Fu (2024, Eqs. 47–49) take $A_1=10.5$, $A_2=3.5$, $C_r=0.23$, so
$C_T=10^{-7}$ at a discontinuity and $10^{-10}$ for high-wavenumber
fluctuations; Li & Fu (2024, Eqs. 44–47) take $A_1=10$, $A_2=5$,
$C_r=0.24$ (five and seven points) or $0.17$ (six points), so
$C_T\in[10^{-10},10^{-5}]$. Li & Fu state the rationale: the high-order
undivided differences inside the scale separation react to discontinuities
and to high-wavenumber fluctuations alike, the low-order measure mainly to
genuine discontinuities (§3.2.1).

## TENO hybrids: jump reconstruction at discontinuities, non-dissipative flux in smooth flow

**TENO-THINC.** Takagi et al. (2022) keep TENO5 everywhere except in cells
that contain a discontinuity, where the interface flux is replaced by a
THINC (tangent of hyperbola) reconstruction: a profile
$f_++f_-\tanh(\beta_{\mathrm{TH}}(X-X_c))$ in the cell, $f_\pm$ the half-sum and
half-difference of the two neighbours, $X$ the normalized cell
coordinate, $X_c$ the jump position fixed by conservation, steepness
$\beta_{\mathrm{TH}}=1.6$, with the interface value (Eqs. 15–16)
$$\hat f_{i+1/2}=f_++f_-\frac{A_{\mathrm{TH}}+T_{\mathrm{TH}}}{1+A_{\mathrm{TH}}T_{\mathrm{TH}}},\qquad
T_{\mathrm{TH}}=\tanh\tfrac{\beta_{\mathrm{TH}}}2,\quad
A_{\mathrm{TH}}=\frac{\mathrm{sgn}(\alpha_{\mathrm{TH}})}{T_{\mathrm{TH}}}\frac{e^{|\alpha_{\mathrm{TH}}|\beta_{\mathrm{TH}}}-1}{e^{|\alpha_{\mathrm{TH}}|\beta_{\mathrm{TH}}}+1},\quad
\alpha_{\mathrm{TH}}=\frac{f_i-f_+}{f_-},$$
and a first-order value where the data are not monotone,
$(f_{i+1}-f_i)(f_i-f_{i-1})\le10^{-15}$ (Eq. 17; THINC symbols page-local).
The profile is bounded by the neighbours, so it needs no limiter, but at
$\beta_{\mathrm{TH}}=1.6$ it is anti-diffusive in some wavenumber ranges,
hence unsuitable for smooth scales (§2.3). The cells are found by the
pattern of TENO5's stencil flags (Eqs. 19–20; see
[shock sensors](/definitions/shock-sensor.md)), which adds no parameter.
Results: fifth order with errors identical to the linear upwind scheme on
a smooth pulse (Table 2), sharper contacts than WENO5-Z and TENO5, small
structures of the double Mach reflection at $512\times128$ comparable to
WENO5-Z at $1024\times256$, at 16.8% (17.1%) more cost per step than
TENO5 on the coarse (fine) mesh (§4, Table 3). Turbulence is deferred to a
later paper; the only turbulent-flow test is the inviscid Taylor–Green
vortex below.

**THINC in other TENO hybrids.** Li & Fu (2024, §3.2.2) simplify the THINC
interface values to the closed form
$f_++f_-\big(\coth\beta_{\mathrm{TH}}-e^{-\alpha_{\mathrm{TH}}\beta_{\mathrm{TH}}}/\sinh\beta_{\mathrm{TH}}\big)$
at the right face and its mirror at the left (Eqs. 54–55, with
$\beta_{\mathrm{TH}}=1.5$ and the average-based $\alpha_{\mathrm{TH}}$ above),
which they state is cheaper and
symmetry-preserving, apply THINC unconditionally to the partial densities
and volume fraction of interfacial cells, and elsewhere reuse Takagi et
al.'s flag pattern on their adaptive TENO (Eqs. 58–61). An a posteriori
MOOD loop recomputes with a first-order Godunov scheme every cell that
violates positivity or produces NaN, with its neighbours (§3.5). The tests
are inviscid two-phase problems (shock–bubble and shock–droplet
interactions); the 2D droplet advection error after ten periods is 0.0074
with THINC against 0.0188 with TENO5A alone (§4.1, Table 4). The face flux
uses one quadrature point, so the scheme is second order in several
dimensions, which the authors accept (§3.1). Huang et al. (2025) use the
same jump reconstruction inside a DG limiter (below).

**TENO-S: skew-symmetric flux in smooth cells.** Liang & Fu (2024, §3.1–3.2,
Algorithm 1) take the opposite substitution: smooth cells, flagged by their
eight-point indicator (see [shock sensors](/definitions/shock-sensor.md)),
use a non-dissipative skew-symmetric split flux in physical variables,
the arbitrary-order extension of Pirozzoli's conservative form with
dispersion-optimized sixth-order coefficients (see
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md)
and [low-dissipation low-dispersion schemes](/methods/low-dissipation-low-dispersion-scheme.md));
troubled cells use an eight-point TENO in characteristic variables (Roe
eigenvectors, Rusanov splitting) with the adaptive cut-off above and a
background linear scheme with a small dissipation. Characteristic
decomposition and nonlinear weights are thus computed only in troubled
cells; on one desktop CPU TENO-S is the cheapest scheme in every reported
case, e.g. 388.08 s against 517.96 s (WENO-CU6), 540.17 s (TENO6) and
628.79 s (TENO8) for the two-dimensional Riemann problem 12 at $800^2$, and
40.78% to 52.11% cheaper than the three in the double Mach reflection at
$512\times128$ (§4.5–4.6, Tables 7, 9). The authors state as the motivating
claim that the dissipation of an upwind background scheme prevents
long-time non-dissipative simulation of smooth flows by destroying
quadratic invariants (§1).

## TENO as a limiter for Runge–Kutta DG

[Huang & Fu (2024)](/sources/huang-2024.md) and
[Huang et al. (2025)](/sources/huang-2025.md) move TENO into third-order
modal Runge–Kutta DG ($N=2$, Legendre basis, SSP-RK3 at CFL 0.15, uniform
Cartesian grids), with the TENO troubled-cell indicator of
[shock sensors](/definitions/shock-sensor.md) deciding which cells are
limited.

- **TENO limiter** (Huang & Fu 2024, §4.4, §5.2, Eqs. 36–64). The cell
  average is kept and the higher modal coefficients are rebuilt from
  compact candidate polynomials: in one dimension three (left, right,
  central) with linear weights $11/38$, $11/38$, $8/19$ for the first
  moment and $45/154$, $45/154$, $32/77$ for the second, each candidate
  dropped by the TENO cut-off ($C_T=10^{-4}$, $q=6$, $\epsilon=10^{-10}$);
  in two dimensions the eight Hermite-WENO stencils of Qiu–Shu and Zhu et
  al., with weights $11/76$ (blocks) and $2/19$ (L/T shapes) for the first
  moments and $1/8$ for the mixed and second moments, uniqueness imposed by
  minimizing $\sum d^2$. The central (1D) or larger (2D) stencils are
  favoured by multiplying their measure by $t_k=10$ (page-local), and the 2D smoothness
  indicators of the mixed and second moments include first-derivative terms
  "for better robustness".
- **TENO-THINC limiter** (Huang et al. 2025, §3.2–3.3, §4.2, Eqs. 15–36).
  Two candidates: a TENO polynomial, the equal-weight average of the
  retained cell and neighbour polynomials ($C_T=10^{-5}$,
  $\epsilon=10^{-10}$; no optimal linear weights), and a THINC polynomial,
  the quadratic that keeps the cell average and matches the THINC
  interface values built from three cell averages ($\beta_{\mathrm{TH}}=1.6$).
  A compact boundary-variation-diminishing selector takes THINC when its
  total boundary variation against the **unlimited** neighbour polynomials
  is smaller than TENO's by more than
  $\max\big(10^{-10},10^{-3}(\mathrm{TBV}^{\mathrm{TENO}}+\mathrm{TBV}^{\mathrm{THINC}})\big)$
  (page-local TBV), which needs no reconstructed neighbour values, unlike
  the BVD schemes of Sun et al. and Jiang et al. Systems are limited in
  characteristic variables; in two dimensions the one-dimensional
  procedure runs along $x$ and $y$ and modifies only the modes of that
  direction, the mixed mode always by TENO.

Both report third order on smooth advection with the limiter never active
(the TENO-THINC limiter forced on everywhere still leaves the smooth
solution unchanged, Huang et al. 2025, Table 2), and sharper
discontinuities and more small-scale structure than the compact WENO
limiters they compare with (of Zhu, Qiu & Zhu, and of Zhong & Shu), judged
from figures of the shock tubes, blast waves, Shu–Osher problem, double
Mach reflection, two-dimensional Riemann problems and a single-mode
Rayleigh–Taylor instability. The TENO-THINC limiter costs 172.08 s
against 163.07 s for the WENO limiter on Lax's problem (Table 4, hardware
not stated); on the Shu–Osher problem its gain is smaller than in the
other cases, as for finite-difference TENO-THINC (§5.4). Both papers
obtain asymmetric solutions of symmetric problems (two-dimensional
Riemann problem, Rayleigh–Taylor instability) and attribute them to round-off
disturbances that their low dissipation fails to damp (Huang & Fu 2024,
§6.6; Huang et al. 2025, §5.7), whereas Takagi et al. (2022, §4.7–4.8) keep
the symmetry with the symmetry-preserving technique of Fleischmann et al.

## WENO limiting of turbulence variables in DG RANS

High-order DG solutions of RANS turbulence variables oscillate where the
boundary layer meets the free stream and the profile changes slope
rapidly. [Jiang et al. (2025)](/sources/jiang-2025.md), §3.1, flag such
cells for the turbulent kinetic energy of the $k$-$\sqrt kL$ model with an
element-resolution indicator and replace the polynomial of $k$ by the
Hermite-WENO reconstruction of their shock-capturing scheme, with $k$ as
the reconstruction variable, as they did earlier for the
[Spalart–Allmaras](/methods/spalart-allmaras-model.md) variable; the same
HWENO limiter handles the shock of the transonic RAE2822 airfoil (§4.2).
With this stabilization (and a positivity-preserving surrogate of the
length-scale variable) the preconditioned GMRES solver converges by 5 to 6
orders of magnitude on a flat plate at third and fourth order, and
diverges without it (§4.1, Fig. 1b). The model is on
[scale-adaptive simulation](/methods/scale-adaptive-simulation.md), the
discretization on
[DGSEM and modal DG](/methods/discontinuous-galerkin-spectral-element-method.md).

## TENO in turbulence tests

The TENO papers of this section are shock-capturing numerics; their turbulent-flow
evidence is on the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
and decaying isotropic turbulence, without a subgrid model:

- **Inviscid Taylor–Green vortex, $64^3$.** TENO-THINC preserves the kinetic
  energy and captures the enstrophy growth better than WENO5-Z and TENO5 to
  $t=10$ (Takagi et al. 2022, §4.10, Fig. 21); TENO-S "successfully
  performs long-time stable computations without numerical dissipation by
  preserving the total kinetic energy" to $t=100$, while WENO-CU6, TENO6
  and TENO8 dissipate it and smear small vortices after $t\approx5$ (Liang
  & Fu 2024, §4.10, Figs. 17–18).
- **Viscous Taylor–Green vortex.** TENO-S at $64^3$ for $Re=100$ to 3000 and
  $128^3$ for $Re=5000$ and $10\,000$ agrees with the DNS of Brachet et al.
  and Dairay et al. in the dissipation rate and "performs significantly
  better" than the other schemes (Liang & Fu 2024, §4.11, Figs. 19–20).
- **Decaying compressible isotropic turbulence** ($M_{t0}=0.6$,
  $Re_{\lambda0}=100$, $64^3$, setup of Johnsen et al.): TENO-S predicts
  mean-square velocity, density fluctuation, dilatation, enstrophy and
  temperature fluctuation in good agreement with filtered $256^3$ DNS,
  "significantly better" than WENO-CU6, TENO6 and TENO8 (Liang & Fu 2024,
  §4.12, Fig. 21; see
  [homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)).

All comparisons are visual; the spectra of the inviscid runs, where a
dissipation-free scheme thermalizes (see
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md)),
are not shown. The single-mode Rayleigh–Taylor instabilities of Takagi et
al., Liang & Fu and Huang et al. are inviscid shock-capturing tests, not
the mixing-layer turbulence of
[Rayleigh–Taylor mixing](/benchmarks/rayleigh-taylor-mixing.md).

## TENO and hybrids against element methods: the supersonic Taylor–Green vortex

[Chapelier et al. (2024)](/sources/chapelier-2024.md) compare seven
high-order solvers, all without subgrid model, on the supersonic
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) ($Re=1600$,
$M_0=1.25$) at $64^3$ to $512^3$ degrees of freedom. Targeted ENO (TENO, Fu,
Hu & Adams 2016, as recalled) is described as an ENO-family scheme with a
staggered stencil layout and a "strong scale-separation procedure", giving
"considerably lower numerical dissipation" than ENO and WENO with robust
shock capturing (§II.C; no TENO formula printed); its cutoff
$C_T=10^{-6}$ is chosen as "a good balance between low numerical
dissipation and robust shock-capturing" (§III.B.c).

- **Reference.** OpenSBLI with sixth-order TENO is run from $64^3$ to
  $2048^3$: the kinetic energy converges at $128^3$, the solenoidal
  dissipation needs $512^3$, and the first peak of the dilatational
  dissipation is not converged even at $2048^3$, since the shocks sharpen
  until molecular viscosity smooths them (§II.C, Figs. 2–4). The $2048^3$ run
  cost 1.96 million core hours (see
  [DNS](/definitions/direct-numerical-simulation.md)).
- **Shocks.** TENO gives sharp and oscillation-free shocks at all
  resolutions, the only order-lowering approach to do so; the hybrid SPADE
  is among the solvers with the lowest dilatational dissipation, i.e. the
  strongest shock capturing (§IV.A–B, Figs. 6, 8; §V).
- **Turbulence.** At $64^3$ OpenSBLI under-predicts the early kinetic energy,
  attributed with the DG and spectral-difference codes to the dissipation of
  Riemann-type fluxes, while SPADE, a central scheme without dissipation in
  smooth flow, is accurate up to $t\approx12$ and slightly too energetic
  afterwards (pile-up near the cut-off, no subgrid closure). OpenSBLI's
  solenoidal dissipation is low on coarse grids but converges well; the
  conclusions state that finite differences with local scheme switching and
  high-order TENO "yield more small-scale dissipation" than DG, spectral
  difference, DGSEM or filtered compact differences (§IV.A, Figs. 5, 7; §V).

## Multidimensional reconstruction for semi-Lagrangian transport

[Zheng et al. (2022)](/sources/zheng-2022.md), a numerics paper on
kinetic-plasma and two-dimensional inviscid transport without turbulence
content, need reconstructed values at arbitrary points of a cell, which
they state WENO-JS-type reconstructions cannot supply (§1, §2.2). Their
truly two-dimensional WENO-ZQ (after Zhu & Qiu) reconstructs a cubic
polynomial per cell from a 13-cell stencil, blended with four linear
polynomials on three-cell stencils by nonlinear weights built from a global
smoothness indicator, with linear weights 0.8 for the cubic and 0.05 for
each linear polynomial and $\epsilon=10^{-14}$; it degrades towards the
linear polynomials near discontinuities (§2.2, Eqs. 7–16). Combined with
cubic-curved upstream cells, it gives a fourth-order, mass-conservative
semi-Lagrangian finite-volume scheme run at CFL numbers up to 10.2 (§3,
§4).

## Cost on GPUs

On the AMD MI60 GPU the inviscid upwind difference takes 70% of the
OpenCFD-SCU run time and the code is memory-bound, so the optimizations
target global-memory access: coalesced access, warp shuffle of neighbouring
fluxes with redundant computation at block edges, shared-memory transposes
that make the $y$- and $z$-direction WENO-SYMBO kernels as fast as the $x$
one (23.4% faster overall, 60% for the $z$ kernel on a $280^3$ grid), and
hoisting divisions out of the seventh-order WENO kernel (10%) (Dang et al.
2022, §4.3, Figs. 10, 14). The operation count of the WENO-SYMBO kernel is
estimated by hand, a lower bound because library functions take several
operations (§5.4).

Wang et al. (2023b, §3.1, §4.1) run the fifth-order WENO reconstruction of
the gas-kinetic scheme as one kernel per direction, one thread per cell, on
Nvidia GPUs; they attribute the fact that a Tesla V100 with about 15 times the
double-precision peak of a TITAN RTX runs only about twice as fast to memory
bandwidth, "the bottleneck for current memory-intensive simulations" (not
profiled; Tables 2–3).

## Qualifications

- Dang et al. (2022, §2.2.3) assign $\theta_J=\theta_2$ to both WENO branches
  ("$\theta_1<\theta\le\theta_2$" and "$\theta_2\le\theta$" in their
  symbols), and state that
  higher thresholds give higher dissipation, whereas by their own rule higher
  thresholds send more points to the low-dissipation upwind scheme
  *(compiler check, not in the sources)*.
- Dang et al. (2022) print 216 floating-point operations for the WENO-SYMBO
  kernel in Table 6 and 262 manually counted operations in §5.4. The version
  read is an author manuscript.
- The variants above are compared within each source only; no source of this
  bundle compares two WENO variants on the same turbulent flow. Luo & Wu
  (2021) compare WENO variants on shock and acoustic tests only; their
  "broadband" sound-wave test is a synthetic acoustic spectrum (§5.2.1). Wang et
  al. (2024) compare WENO5 with other schemes only in the inviscid
  time-reversal test, which measures energy loss, not accuracy in
  turbulence. Chapelier et al. (2024) compare one TENO scheme and one
  central/upwind hybrid with element methods on one turbulent flow, not
  two WENO variants.
- **Low dissipation of TENO.** Chapelier et al. (2024) recall that TENO has
  "considerably lower numerical dissipation" than WENO (§II.C) and find, in
  their own comparison, that TENO yields "more small-scale dissipation" than
  the element methods and lower solenoidal dissipation on coarse grids
  (§IV.A, §V). The two statements compare TENO with different schemes, so
  they do not conflict.
- Chapelier et al.'s conclusions group SPADE with the "sharp but
  oscillating" order-lowering schemes, while their §IV.A ranks it among the
  strongest shock-capturing solvers and §IV.B does not describe its Mach
  profiles. The Mach-profile reference of their Fig. 8 is labelled
  "TENO6 512", while the text and Figs. 5–7 use the $2048^3$ run. The version
  read is the HAL accepted manuscript.
- Luo & Wu (2021) calibrate $\lambda_{\mathrm Z}=579$ on one problem at
  one resolution (§3.2, Fig. 13), and their abstract's claim of accuracy
  "superior to the underlying linear scheme" is borne out by their Table 1
  only from $81\times81$ on. Printed slips: §2.1 writes the ideal weights
  with indices 1–3 against $k=0,1,2$ elsewhere; the broadband-sound initial
  velocity of Eq. (12), $u_0+\frac{2}{\gamma-1}(c/c_0)$, does not reduce to
  the stated mean $u_0$ for an unperturbed state *(compiler check, not in
  the sources)*.
- **Cut-off values.** $C_T=10^{-5}$ (Takagi et al. 2022, TENO5; Huang et al.
  2025, limiter), $10^{-4}$ (Huang & Fu 2024, indicator and limiter;
  Huang et al. 2025, indicator), $10^{-6}$ (Chapelier et al. 2024, TENO6)
  and the adaptive ranges above belong to different schemes and roles;
  Huang & Fu (2024, §2) note that $C_T$ "is usually taken as $10^{-5}$".
  They are not conflicting values. Takagi et al. (2022, §4.5, Fig. 9) find
  that with $10^{-5}$ the blast-wave solution develops a small overshoot at
  the strong contact on very fine grids, absent with $10^{-4}$, and keep
  $10^{-5}$ for under-resolved simulations.
- **"Without dissipation".** Liang & Fu's (2024) inviscid claim rests on
  energy histories at $64^3$; their viscous and isotropic-turbulence runs
  have no subgrid model, and the better agreement with DNS is reported
  without a spectral or error measure. Their "no case-by-case tuning" sits
  beside an indicator regularizer of $10^{-4}$ in one dimension and
  $10^{-2}$ in several and a switch to Roe splitting with an entropy fix
  "to obtain a stable result" in the blast-wave case (§4.4).
- **Conservation of the one-dimensional TENO limiter.** Huang et al.
  (2025, Eq. 19) form the limited polynomial as a weighted sum of the cell
  and neighbour polynomials; with a nonzero neighbour weight its mean over
  the cell differs in general from the cell average, since an extrapolated
  neighbour polynomial does not have the cell's mean there, and no shift of
  the neighbours to the cell average is printed for one dimension, while
  the THINC candidate (Eq. 21) and the two-dimensional limiter (which
  leaves the zeroth mode untouched) keep it explicitly *(compiler check,
  not in the sources)*.
- **Printed slips (Huang & Fu 2024).** In Eq. (38) the first moment of the
  quartic target polynomial is printed with
  $\tfrac{15}{19}(u^{(0)}_{i-1}-u^{(0)}_{i+1})$; linear data, for which the
  first moment must equal the slope, and the printed candidates with the
  printed weights of Eq. (40) both require
  $\tfrac{15}{19}(u^{(0)}_{i+1}-u^{(0)}_{i-1})$ ($u^{(l)}_i$ the modal
  coefficients) *(compiler check, not in the sources)*. Table 2 prints the
  $L_\infty$ error at $N_x=50$ as $5.38\times10^{-7}$, below the next
  resolution's $5.56\times10^{-7}$; the printed order 3.27 is
  $\log_2(5.38\times10^{-6}/5.56\times10^{-7})$, so the exponent is $-6$
  *(compiler check, not in the sources)*. Eq. (56) imposes exactness for
  basis functions $v_6$ to $v_9$ that the paper does not define.
- **Printed slips (Takagi et al. 2022).** The double Mach reflection ends
  at $t=0.2$ in the text and $t=2.0$ in the caption of Fig. 10; the
  Shu–Osher data are defined on $[-5,5]$ (Eq. 29) while the text gives the
  domain $[0,10]$; the THINC conservation constraint is printed without the
  $1/\Delta x$ of Eq. (3).
- **Printed slips (Li & Fu 2024).** Eq. (42) normalizes over three
  stencils, $\sum_{l=0}^{2}$, while the six- and seven-point schemes have
  four and five; §4.1 calls the two-dimensional time step
  $5\times10^{-6}$ s "smaller" than the one-dimensional $2\times10^{-6}$ s;
  MOOD is expanded in two different ways (abstract, §3.5).
- Valencia et al. (2026) use WENO-Z only for their reference DNS and state
  nothing about its dissipation; their a priori study is on
  [scale-similarity models](/methods/scale-similarity-model.md).
- Zheng et al. (2022) state fourth-order accuracy for the swirling
  deformation test, whose Table 2 orders are 3.47 to 3.71 up to $1280^2$
  (Example 4.2); their $L^2$-stability proposition checks the amplification
  factor by sampling (Prop. 3.9, App. C). Table 5's caption gives CFL 1 and
  the text CFL 10.2 for the same runs.

# Citations

- [Dang et al. (2022)](/sources/dang-2022.md) — §1 (dissipation of WENO in DNS, strong shocks); §2.2.1–2.2.4, Eqs. (19)–(43), Table 2 (flux splitting, characteristic reconstruction, scheme library, hybrid); §4.3, Figs. 10, 14 (GPU kernels); §5.1, §5.4, Table 6; §6.1.
- [Helm & Martín (2022)](/sources/helm-2022.md) — §II (bandwidth-optimized WENO with limiters); §III C (plateau suppressed by excess dissipation).
- [Placco et al. (2023)](/sources/placco-2023.md) — §2 (fifth-order WENO in STREAmS, implicit LES).
- [Cao et al. (2022)](/sources/cao-2022.md) — Remark 1 (linear weights, WENO-Z, characteristic variables); §3.1, §3.4.
- [Cogo et al. (2022)](/sources/cogo-2022.md) — §2 (energy-preserving schemes with WENO switched by the Ducros sensor).
- [Huang et al. (2022)](/sources/huang-2022.md) — §2.2 (limiter-optimized seventh-order WENO; split-convective alternative).
- [Carlsson et al. (2023)](/sources/carlsson-2023.md) — §2.2.3, Eqs. (14)–(15) (Ducros-weighted sensor); Table 1; §5.
- [Zhao et al. (2023a)](/sources/zhao-2023.md) — arXiv v1: §3.1–3.3, Fig. 2 (seventh-order WENO, WENO-Z baseline, HWENO); §4, Table 3 (order with four Gauss points); §5.1 (over-dissipation of the fifth-order scheme).
- [Wang et al. (2023b)](/sources/wang-2023-b.md) — arXiv v1: §2 (fifth-order WENO in the gas-kinetic scheme); §3.1 (GPU kernels); §4.1, Tables 2–3 (memory-bandwidth-bound speedup).
- [Bernades et al. (2023)](/sources/bernades-2023.md) — §1 (upwind and WENO hybridization of divergence-form schemes); §3.2, §4.1.1, Fig. 1 (Ducros-sensor hybrid of KGP and HLLC).
- [Wang et al. (2024)](/sources/wang-2024.md) — §3.1, Eq. (14), Fig. 2 (inviscid Taylor–Green time reversal: KGP2, OPT6, MUSCL3, WENO5); §5.
- [Chapelier et al. (2024)](/sources/chapelier-2024.md) — HAL hal-04582857v1: §II.C, Figs. 2–4 (TENO reference and convergence); §III.B.b, c, h (SPADE homotopy hybrid, OpenSBLI TENO, Ducros sensor); §IV.A–B, Figs. 5–8; §V.
- [Cao et al. (2024)](/sources/cao-2024.md) — arXiv 2107.08609v1: §2.3 (WENO in computational space on curvilinear meshes).
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §1; §2.1–2.3, Eqs. (1)–(6) (WENO-JS, WENO-Z, WENO-Z+); §3.1–3.2, Eqs. (7)–(9), Figs. 1–3 (approximate dispersion relation, WENO-Z+M); §4, Figs. 4–7 (linear and nonlinear dissipation); §5, Table 1, Figs. 8–18; §6.
- [Xu et al. (2026)](/sources/xu-2026.md) — arXiv 2508.21599v1: §3, §3.2–3.5, Eqs. (11)–(23) (WENO-5 on primitive variables, sensor-switched conservative/primitive hybrid); §4.2.
- [Zheng et al. (2022)](/sources/zheng-2022.md) — §1, §2.2, Eqs. (7)–(16) (two-dimensional WENO-ZQ); §3–4, Tables 2, 5, App. C.
- [Tang et al. (2022)](/sources/tang-2022.md) — §2.1 (WENO-5 in a hybrid RANS/LES combustor solver).
- [Aiello et al. (2026)](/sources/aiello-2026.md) — §3.3 (WENO5 transient in STREAmS); §4.2 (WENO hybridization of non-entropy-conserving schemes).
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §1; §2.2–2.3, Eqs. (5)–(17) (TENO5, THINC); §3.1–3.2, Eqs. (18)–(20), Table 1 (TENO-THINC); §4, Tables 2–3, Figs. 9–21 (tests, cost, inviscid Taylor–Green vortex); §5.
- [Liang & Fu (2024)](/sources/liang-2024.md) — §1; §2.2, Eqs. (8)–(20) (TENO); §3.1–3.3, Eqs. (31)–(49), Algorithm 1 (TENO-S, adaptive cut-off); §4, Tables 3–12, Figs. 17–21 (cost, Taylor–Green vortex, isotropic turbulence); §5.
- [Li & Fu (2024)](/sources/li-2024-c.md) — §3.1; §3.2.1–3.2.3, Eqs. (28)–(61), Table 1 (TENOA, simplified THINC, pattern indicator); §3.5 (MOOD); §4.1, Table 4.
- [Huang & Fu (2024)](/sources/huang-2024.md) — §2, Eqs. (7)–(15) (TENO5 recalled); §4.4, Eqs. (36)–(50); §5.2, Eqs. (51)–(64) (TENO limiter); §6, Tables 1–4, Figs. 4–15.
- [Huang et al. (2025)](/sources/huang-2025.md) — §3.2–3.3, Eqs. (15)–(25); §4.2, Eqs. (27)–(36) (TENO-THINC limiter, compact BVD); §5, Tables 1–4, Figs. 1–8.
- [Jiang et al. (2025)](/sources/jiang-2025.md) — §3.1 (HWENO limiting of $k$); §4.1, Fig. 1b (convergence with and without it); §4.2 (HWENO at the RAE2822 shock).
- [Valencia et al. (2026)](/sources/valencia-2026.md) — §IV (PeleC with seventh-order WENO-Z inside PPM for the reference DNS).
