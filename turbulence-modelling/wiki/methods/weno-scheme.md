---
type: Method
title: "WENO and hybrid shock-capturing schemes in scale-resolving simulation"
description: "WENO schemes capture shocks by nonlinear weighting of candidate stencils; in DNS and LES of compressible turbulence their dissipation is reduced by optimized weights and limiters, by linear weights in smooth flow, or by hybrids that apply WENO only where a shock sensor fires, and in implicit LES it serves as the subgrid dissipation."
status: established
aliases: [WENO, TENO, targeted ENO, weighted essentially non-oscillatory scheme, WENO-Z, WENO-Z+, WENO-Z+M, WENO-ZQ, WENO-SYMBO, HWENO, Hermite WENO, bandwidth-optimized WENO, limiter-optimized WENO, hybrid upwind/WENO scheme, hybrid central/WENO scheme]
tags: [shock-capturing, numerical-dissipation, dns, compressible, implicit-les, gpu]
timestamp: 2026-10-26T20:44:00Z
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
