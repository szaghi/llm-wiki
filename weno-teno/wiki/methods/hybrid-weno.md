---
type: Method
title: "Hybrid central-WENO schemes"
description: "Hybrid schemes use a cheap linear (central, energy-preserving or optimal upwind) reconstruction where a sensor declares the stencil smooth and a nonlinear WENO or TENO reconstruction elsewhere, or switch between flux and state reconstruction; they cut dissipation and cost or restore order, but hinge on the sensor and its threshold."
status: established
aliases: [hybrid WENO, TENO-S, hybrid central/WENO, hybrid compact-WENO, hybrid TENO, hybrid linear–nonlinear scheme, WENO-H, MDAD-HY, TENO-HY, three-region hybrid, hybrid EP–WENO, hybrid EP–TENO, flux/state hybrid, ADADF-HY, hybrid MR-WCNS, MMR-WENO, HMR-WENO, modified MR-WENO, WENO5IS-THINC]
tags: [weno, teno, reconstruction, low-dissipation, turbulence, limiting]
timestamp: 2026-10-23T11:06:00Z
---

# Hybrid central-WENO schemes

A hybrid scheme pairs a **linear** reconstruction, used where the solution is judged smooth, with a
**nonlinear** shock-capturing reconstruction, used elsewhere, and a **sensor** that decides between
them point by point. Luo & Wu (2021, §1) summarize the Li & Qiu strategy: indicators identify the
discontinuities; at a discontinuity or a steep gradient the nonlinear weights are turned on to give
the scheme the [ENO property](/definitions/eno-property.md); for a stencil smooth enough they are
turned off and the linear scheme is used. Two motives recur: lower numerical dissipation in smooth
regions, which matters for turbulence, and lower cost, since the linear scheme needs neither weights
nor, for systems, a [characteristic decomposition](/methods/characteristic-decomposition.md).

## Variants recalled in the sources

- **Hybrid compact-ENO/WENO.** Takagi et al. (2022, §1) recall Adams & Shariff's hybrid compact-ENO
  scheme for shock–turbulence interaction, Pirozzoli's conservative hybrid compact-WENO scheme and the
  characteristic-wise hybrid compact-WENO scheme of Ren et al. with a new flow sensor.
- **Freezing the nonlinear adaptation.** Fu (2021, §1) recalls Hill & Pullin's switch, which freezes
  the WENO adaptation when the ratio of the largest to the smallest smoothness indicator is below a
  problem-dependent threshold.
- **Hybrid TENO.** Fu (2023, §3.4, Eqs. (21)–(24)) recalls a hybrid that builds the sensor from the TENO
  scale separation itself. On four stencils, with $\gamma_k=(\beta_k+\epsilon)^{-q}$, $q=6$, where
  $\epsilon$ "also functions as a cut-off on the stencil smoothness", and $\chi_k=\gamma_k/\sum\gamma_l$,
  the flag is 0 (smooth) if $\chi_k>C_T$ for every $k$, with $C_T=5\times10^{-4}$, and 1 otherwise.
  Flag 0 selects the optimal linear scheme without characteristic decomposition, flag 1 the TENO6
  reconstruction. With SSP-RK3 the efficiency improves "by a factor of four", with unchanged shock
  capturing (reproduced 2-D Riemann configuration 12, Fig. 7). Because the indicator separates
  non-smooth scales in spectral space, Fu calls it "more universal" than physical sensors such as
  Ducros'. The same indicator has driven steepness-adjustable, minimized-dispersion and
  artificial-viscosity hybrids ([targeted ENO](/methods/targeted-eno.md)).
- **TENO-THINC.** Takagi et al. (2022, §3) also hybridize on TENO flags, but differently: in smooth
  regions the TENO5 flux restores the linear scheme anyway, and the flags select cells where THINC
  replaces TENO at genuine discontinuities. They contrast it with classical hybrids, which "dedicate
  to deploying the optimal linear scheme as much as possible in smooth regions" for efficiency
  (§3.2, item 4; [TENO-THINC](/methods/teno-thinc.md)).
- **Hybrid Hermite WENO.** In the moment-based [HWENO](/methods/hermite-weno.md) of Zhao, Chen &
  Qiu, made positivity-preserving by Fan, Zhang & Qiu (2021, §1, §4), a troubled-cell indicator
  selects the cells where the nonlinear HWENO reconstruction, preceded by a limiter on the first
  moment, replaces a linear Hermite reconstruction. With 0.97–19.57 % of cells flagged in their shock
  tests, the hybrid saves 59.05–89.64 % of the CPU time of the non-hybrid positivity-preserving HWENO
  (Table 4.2, hardware not stated), and the positivity limiter is triggered in identical fractions of
  cells in both (Table 4.2). The hybrid of Zhao et al. without positivity preservation blows up on
  their Examples 4.3–4.7 (Euler).

- **PDE-aware hybrids.** Balsara, Samantaray & Subramanian (2023, §6.3) recall Li & Ren's hybrid, which
  uses the central stencil wherever the solution is smooth and WENO only in troubled zones. Hong, Ye & Ye (2022, §1) recall Fu's TENO-based-indicator hybrid as the
  alternative to their own speed-up, which makes TENO itself cheaper instead
  ([targeted ENO](/methods/targeted-eno.md)).

## A kinetic-energy-preserving TENO hybrid: TENO-S

Liang & Fu (2024b) pair an eight-point TENO with a non-dissipative split-form flux. In cells judged smooth the
interface flux is the cubic (Kennedy–Gruber) split form in Pirozzoli's locally conservative two-point form, extended to
eight points with dispersion-optimized central coefficients (sixth order), which preserves kinetic energy in smooth
flow ([split convective forms](/methods/split-convective-forms.md),
[kinetic energy preservation](/properties/kinetic-energy-preservation.md)); in flagged cells it is a characteristic-wise
eight-point TENO with Rusanov splitting, an optimized sixth-order background scheme and the adaptive cut-off of TENO-A,
$C_T$ between $10^{-7}$ and $10^{-10}$ ([adaptive TENO](/methods/adaptive-teno.md)) (§3.2, Eq. (35), Algorithm 1;
§3.3). The switch is an eight-point variant of the TENO-based indicator above (§3.1, Eqs. (31)–(34)):

- six **equal-sized** three-point stencils, the three standard ones and three that do not contain $x_i$
  ($\{i+1,i+2,i+3\}$, $\{i-3,i-2,i-1\}$, $\{i+2,i+3,i+4\}$), with Jiang–Shu indicators integrated over the target cell
  ([smoothness indicators](/definitions/smoothness-indicator.md));
- $\gamma_k=(\beta_k+\epsilon)^{-6}$ with $\epsilon=10^{-4}$ in 1-D and $10^{-2}$ in multi-D, $\chi_k=\gamma_k/\sum_l\gamma_l$,
  and the cell is smooth only if every $\chi_k>10^{-6}$;
- computed on the conserved variables without characteristic decomposition, on density and total energy in 1-D and on
  density alone in multi-D, dimension by dimension.

Equal stencil sizes keep the indicator cheap; the authors call it "more universal for general conservation laws" than
physical sensors such as Ducros' (no comparison shown; [Ducros sensor](/definitions/ducros-shock-sensor.md)). In double
Mach reflection "more than 90%" of the cells take the split-form branch (§4.6, stated without a count). Wall times on one
CPU (AMD Ryzen 9 5950X) favour TENO-S in every test: on 2-D Riemann configuration 12 ($800^2$) 388.08 s against 517.96 s,
540.17 s and 628.79 s for [WENO-CU6](/methods/weno-cu6.md), TENO6 and TENO8, "about 25.07%, 28.15% and 38.28%" cheaper
(Table 7); on double Mach reflection at $512\times128$ 17.42 s against 29.42 s, 31.13 s and 36.38 s (Table 9). On the
entropy wave it converges at sixth order ($L_1$ orders 5.617 to 5.995; Tables 1–2;
[density-wave advection](/benchmarks/density-wave-advection.md)); on the inviscid
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) ($64^3$, to $t=100$) it keeps the total kinetic energy, where
WENO-CU6, TENO6 and TENO8 smear the small vortices after $t\approx5$ (§4.10, Figs. 17–18). Liang & Fu (§1) criticise the
earlier hybrids: Pirozzoli's compact–WENO hybrid "inevitably generates slight spurious oscillations" because its detector
reads only low-order information, hybrid performance "strongly depends on the discontinuity indicator, which is mostly
problem-sensitive", and compact schemes cost more than central ones of the same order. They leave positivity preservation
for extreme configurations to future work (§5).

## A dissipation-adaptive hybrid: MDAD-HY

Li, Chen & Ren (2022a, §3) hybridize the six-point MDAD flux, a linear fourth-order flux whose
dissipation follows a [scale sensor](/definitions/scale-sensor.md), with its WENO-CU6-type counterpart
MDAD-WENO by a binary flag $\delta^{\mathrm H}_{i+1/2}$ (page-local; [MDCD schemes](/methods/mdcd-scheme.md)),
and compare four detectors on static data and in the approximate dispersion relation:

- **Harten's**, $1-|f_{i-1}-2f_i+f_{i+1}|/(|f_{i-1}-f_i|+|f_i-f_{i+1}|+\epsilon)$ against 0.3 (Eq. (47));
- **Ren et al.'s**, $\mathfrak s_i=(2\mathsf a\mathsf b+\epsilon)/(\mathsf a^2+\mathsf b^2+\epsilon)$ with the one-sided
  variations $\mathsf a=|f_i-f_{i-1}|$, $\mathsf b=|f_i-f_{i+1}|$ (page-local $\mathfrak s$, $\mathsf a$,
  $\mathsf b$), minimized over neighbouring points, $\epsilon=\tfrac{0.9\mathfrak s_c}{1-0.9\mathfrak s_c}\xi^2$,
  $\xi=10^{-3}$ (page-local), threshold $\mathfrak s_c=0.3$ (Eqs. (48)–(54));
- **Fu's TENO-based** one, $\gamma_k=(\beta_k+\epsilon)^{-6}$, $\epsilon=10^{-4}$, smooth iff every normalized
  $\chi_k$ exceeds $5\times10^{-4}$ (Eqs. (55)–(57));
- a **new** one: Ren's form with second differences added to the variations,
  $\mathsf a=|f_i-f_{i-1}|+|f_i-2f_{i-1}+f_{i-2}|$, $\mathsf b=|f_i-f_{i+1}|+|f_i-2f_{i+1}+f_{i+2}|$,
  $\xi=10^{-2}$, $\mathfrak s_c=0.4$ (Eqs. (58)–(60)); without $\epsilon$, $\mathfrak s_i=2/(\mathsf a/\mathsf b+\mathsf b/\mathsf a)$
  vanishes at extrema, where one first difference vanishes, and the second differences, which also jump
  at a discontinuity but vary little at an extremum, keep the ratio moderate.

On sine waves the new detector keeps the smooth flag up to $\vartheta=2.06$, Fu's only below 0.64, and
Harten's and Ren's fail "at very low wavenumbers" by flagging critical points; on a jump between two
sines only the new one separates the jump from both waves (Figs. 9–10). In the approximate dispersion
relation MDAD-HY recovers the linear scheme up to $\vartheta=2.06$, while TENO-HY and MDCD-HY show
irregular dissipation at low wavenumbers (Figs. 11–12;
[approximate dispersion relation](/definitions/approximate-dispersion-relation.md)). Implementation
details matter: inputs normalized by $\max(|f_{\max}|,1)$ (after which TENO-HY detects "obviously
better" than in Fu's own paper), detection on density and entropy once per step, buffer zones of 1–3
points, and a second detection on each split characteristic flux at flagged interfaces (§3.4, §4.3.1).
Thresholds still vary by case: 0.5 for the blast waves, 0.8 for Sedov (§4.2).

## A fully discrete successor: ADADF-HY

Li, Sun, Zha, Zhu, Ding & Xia (2023b, §3.5–3.6, Eqs. (51)–(61)) hybridize their fully discrete
adaptive-dispersion, critical-adaptive-dissipation flux ADADF ([MDCD schemes](/methods/mdcd-scheme.md))
with a [WENO-CU6](/methods/weno-cu6.md) flux whose linear weights are the MDCD ones. The blend is
continuous,

$$\hat f_{i+1/2}=\mathfrak w_{i+1/2}\hat f^{\mathrm{ADADF}}_{i+1/2}+(1-\mathfrak w_{i+1/2})\hat f^{\mathrm{WENO\text{-}CU6}}_{i+1/2},\qquad
\mathfrak w_{i+1/2}=\min\big(1,\mathfrak s_{i+1/2}/\mathfrak s_c\big),\quad \mathfrak s_c=0.4,$$

with Ren et al.'s indicator in the notation of the MDAD-HY section,
$\mathfrak s_i=(2\mathsf a\mathsf b+\delta_{\mathrm R})/(\mathsf a^2+\mathsf b^2+\delta_{\mathrm R})$,
$\delta_{\mathrm R}=10^{-3}$ (page-local; their $\delta$), and $\mathfrak s_{i+1/2}=\min(\mathfrak s_i,\mathfrak s_{i+1})$
(page-local blending weight $\mathfrak w$; their $\sigma$). Where $\mathfrak s\ge\mathfrak s_c$ the WENO-CU6 flux is not computed. For
the Euler equations the indicator is evaluated on Roe-averaged characteristic variables and the split
characteristic fluxes use global Lax–Friedrichs splitting. All evidence is visual: on
[Shu–Osher](/benchmarks/shu-osher-problem.md), 2-D Riemann configurations 3 and 6,
[Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md),
[Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md) and
[double Mach reflection](/benchmarks/double-mach-reflection.md) ADADF-HY resolves the most structure
of WENO-Z, MDCD-HY, MDAD-HY and itself; its Rayleigh–Taylor field is slightly asymmetric, which the
authors attribute to its low dissipation (§4).

Li et al. (2023b) return to Ren et al.'s indicator, which Li, Chen & Ren (2022a) had found to flag
critical points "at very low wavenumbers" and had replaced by their new detector, without comment.
Their Eq. (60) and implementation steps switch between the purely linear flux and a "nonlinear" one
at the threshold instead of blending; the two agree where $\mathfrak w=1$, and which flux "nonlinear"
means is not stated.

## A parameter-free switch: hybrid MR-WCNS

Wang, Zhu, Wang & Zhao (2023c, §3, Step 2, Remark 1) switch the node-to-midpoint interpolation of a
fifth-order [WCNS](/methods/weighted-compact-nonlinear-scheme.md) between the linear five-point value
$\tfrac1{128}(3u_{i-2}-20u_{i-1}+90u_i+60u_{i+1}-5u_{i+2})$ and their multi-resolution interpolation
([multi-resolution WENO](/methods/multi-resolution-weno.md)). The rule: let $p_1$ be the quartic
interpolant on the five points; if no extreme point of its derivative $p_1'$ lies within the stencil,
the linear value is used, otherwise the nonlinear one. The extreme points have an explicit expression
taken from Zhao, Zhu, Chen & Qiu's hybrid WENO. The authors call the switch problem-independent and
free of artificial parameters. It is applied in characteristic variables, which makes the map of
marked points periodic rather than symmetric in their Richtmyer–Meshkov runs; they keep it because
characteristic variables "more accurately identify the troubled cells" (Example 4.7).

Cost relative to WENO-JS (Table 5.1, twelve runs, hardware not stated): 0.81–1.07 for the hybrid,
1.50–2.31 for the non-hybrid MR-WCNS of Zhang, Wang & Zhang. Errors in the smooth accuracy tests are
about one order below WENO-JS (Tables 4.1–4.4).

*(Compiler check, not in the sources: the extreme points of the cubic $p_1'$ are the roots of the
quadratic $p_1''$, i.e. inflection points of $p_1$. A smooth wave with an inflection point inside the
stencil, as the sine waves of the accuracy tests have every half period, therefore takes the nonlinear
branch; the accuracy tables measure the nonlinear interpolation at those points.)* The paper does not
say whether "within the stencil" means $[x_{i-2},x_{i+2}]$ or the union of the five cells.

## Extreme points in the target cell: MMR-WENO and HMR-WENO

Zuo & Zhu (2024a, 2024b) switch, cell by cell, between the linear upwind finite-difference scheme of order
5, 7 or 9 and the [multi-resolution WENO](/methods/multi-resolution-weno.md) of the same order, with a
detector of the same family as the one above: the nodal density on the big stencil (5, 7 or 9 points) is
interpolated by a polynomial $g$ of degree $n_{\mathrm g}=4$, 6 or 8 (page-local $g$, $n_{\mathrm g}$; the sources write $2r$
with their own $r$, not the registry's), and the cell is troubled when $g$ has an
extreme point in the **target cell** $[x_{i-1/2},x_{i+1/2}]$, a narrower interval than the
$[x_{i-5/2},x_{i+5/2}]$ of Zhu & Qiu and Zhao et al. or the $[x_{i-3/2},x_{i+3/2}]$ of a Wang, Tian, Zhu & Zhao
hybrid, as they recall them. They state that those detectors "had a fatal flaw": exact extreme points of a
quintic or higher-degree polynomial are "not only time-consuming but also unavailable", so the detectors
served hybrids of order at most five (2024a, §1; 2024b, §1, Remark 1). The two papers decide the extreme
point differently ([troubled-cell indicators](/definitions/troubled-cell-indicator.md)):

- **Termwise bounds** (MMR-WENO, 2024a, §2.2, Eqs. (2.21)–(2.33), Algorithm 1). The fifth-order quartic is
  expanded about $x_{i-1/2}$ ($g_1$) and about $x_{i+1/2}$ ($g_2$); on the cell each monomial
  $((x-x_{i\mp1/2})/\Delta x)^k$ ranges over $[0,1]$ or $[-1,0]$, so the sums of the termwise maxima and minima
  bound $\Delta x\,g'$, e.g. $\mathrm{MAX}_1=\max(0,4a_4)+\max(0,3a_3)+\max(0,2a_2)+a_1$ for $g_1$ (page-local
  $a_k$), and the cell is troubled when $(\mathrm{MAX}\pm\Delta x)(\mathrm{MIN}\pm\Delta x)<0$ for $g_1$ or for
  $g_2$; $g_2$ is skipped when $g_1$ already flags the cell. The $\pm\Delta x$ margin, after Wang et al., guards
  against round-off. *(Compiler check, not in the sources: $g_1$ and $g_2$ interpolate the same five values with
  degree 4, so they are one polynomial written about two points — the printed coefficients satisfy, e.g.,
  $a_3^{\mathrm R}=a_3^{\mathrm L}+4a_4^{\mathrm L}$ — and the second test differs only through its bounds;
  because the bounds overestimate the range of $g'$, a sign change of the bounds flags the cell without proving
  an extreme point, while equal signs prove that there is none.)*
- **Hierarchical bisection** (HMR-WENO, 2024b, §2.2, Eqs. (2.15)–(2.19), Algorithm 1). Starting from the linear
  $g^{(n_{\mathrm g}-1)}$, each derivative's zeros in the cell (sign test plus bisection) split it into pieces on which the
  next lower derivative is monotonic, down to $g'$, whose zeros are then counted exactly by endpoint signs;
  $\mathrm{icount}>0$ flags the cell. The authors claim the first use of a hierarchical bisection to locate
  monotonicity intervals of an arbitrary-degree polynomial (§1); no tolerance or iteration count is given.

Both are presented as parameter-free and extendable to any order (sextic $g$ at seventh order, octic at
ninth), dimension by dimension in multi-D; in smooth cells the characteristic projection and all weight
computations are skipped (2024a, §1). CPU time relative to the same-order multi-resolution WENO: 20.7–36.8 %
for MMR-WENO on the Lax problem, a 2-D Riemann problem, double Mach reflection and the 3-D Taylor–Green vortex
(2024a, Table 3.1; no hardware stated) and 25–78 % for HMR-WENO on the blast waves, double Mach reflection, the
forward step and the Taylor–Green vortex (2024b, Table 3.1; Lenovo XiaoXinAir 14 laptop, Visual Studio 2017).
Both hybrids keep the design orders 5, 7, 9 on 1-D to 3-D Euler density waves with cleaner fifth-order
convergence than the non-hybrid scheme, and show more roll-up and lower Taylor–Green dissipation than it by
figure ([density waves](/benchmarks/density-wave-advection.md),
[double Mach reflection](/benchmarks/double-mach-reflection.md),
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)); MMR-WENO is said to identify flow features "more
accurately" than the Wang et al. hybrid (2024a, Ex. 3.4, 3.6), while the claim of more precise detection on the
narrower interval is not tested against the earlier detectors in 2024b.

*(Compiler check, not in the sources, as for the hybrid MR-WCNS above: a detector of extreme points flags every
smooth extremum of the density, so the nonlinear branch runs at the crests of the sine waves of the accuracy
tests; and a jump across which $g$ stays monotonic in the target cell is detected only through the
oscillations of the interpolant.)*

## Energy-preserving central / WENO-TENO hybrids in LES

De Vanna, Baldan, Picano & Benini (2023a) make the hybridization level the parameter of a study of
wall-resolved and wall-modelled LES of supersonic boundary layers in the URANOS code
([URANOS](/software/uranos.md), [wall-modelled LES](/methods/wall-modeled-les.md)). The linear member is a
sixth-order fully split energy-preserving central scheme (Pirozzoli; [split convective forms](/methods/split-convective-forms.md),
[kinetic energy preservation](/properties/kinetic-energy-preservation.md)), the nonlinear one
[WENO-Z](/methods/weno-z.md) of order 3, 5 or 7, [TENO5](/methods/targeted-eno.md) or
[TENO-A5](/methods/adaptive-teno.md). The switch is a modified [Ducros sensor](/definitions/ducros-shock-sensor.md),
$\Psi_{\mathrm D}=\max\big(-\nabla\cdot v/\sqrt{(\nabla\cdot v)^2+|\nabla\times v|^2+\epsilon_{\mathrm D}},0\big)$ with
$\epsilon_{\mathrm D}=(v_\infty/\delta_0)^2$ (Eq. (9)), evaluated at interfaces against a threshold
$\Psi^*$; a flagged interface switches the flagged cell and two, three or four neighbours, depending on the
WENO/TENO order, to the nonlinear scheme (§3.2). $\Psi^*=0$ is the pure shock-capturing scheme.

- **Wall-modelled LES at Mach 2.** Pure WENO/TENO damp or destroy wall turbulence, most of all WENO-Z3, which
  mispredicts the wall flow regardless of grid resolution; $\Psi^*=0.1$ restores a realistic friction curve and
  brings the medium and fine grids close to DNS; at $\Psi^*=0.4$ all WENO and TENO variants give identical
  curves, since the central scheme covers most of the flow; no pure WENO/TENO collapses on the central solution
  (§4.3, Figs. 5, 7–8).
- **Mach 5.86.** The pure central scheme diverges because of shocklets, and $\Psi^*=0.2$ is "the highest limit
  that ensures the current arrangement's numerical stability"; the authors recommend $\Psi^*\simeq0.2$ (§4.4, §6).
- **Mechanism.** In low-resolution settings the sensor reads numerical noise and turbulent fluctuations as
  shocklets, so the nonlinear scheme acts in nominally smooth regions (§3.2, §4.3.3).
- **Cost.** Wall time per iteration relative to the pure central scheme is 0.90–1.00 for the hybrids and
  0.95–1.32 for the pure schemes (TENO-A5 on the fine grid the highest; 13 Intel KNL nodes; Table 2).

The URANOS paper adds that hybrid schemes have discontinuous error scaling because of the switch, so its
convergence tests use the schemes "in pure state", and that $\Psi^*$ is strongly flow-dependent (De Vanna et
al. 2023b, §3.2). Bielawski, Barwey, Prakash & Raman (2023, App. A.2) find a skew-symmetric central scheme far
less dissipative than HLLC and AUSMDV in enstrophy and dilatation on decaying isotropic turbulence with
eddy shocklets, and postulate, without testing it, that a hybrid central/HLLC scheme would be beneficial
([compressible isotropic turbulence](/benchmarks/compressible-isotropic-turbulence.md)).

## A flux/state hybrid for nonlinear order

Chamarthi (2023b, §2.4, Eqs. (31)–(37)) switches not between a linear and a nonlinear scheme but between two ways
of forming the fluxes of a [gradient-based reconstruction](/methods/gradient-based-reconstruction.md): where the
switch is 1, the seventh-order interpolation of the point fluxes, which keeps the design order on nonlinear
problems; where it is 0, the flux of the MP-limited states ([MP limiter](/methods/monotonicity-preserving-limiter.md)).
The limited states always enter the dissipative part of the HLLC flux. The detector is Ren's form with the second
differences of Li, Chen & Ren's new detector above, computed on density only, because density "sees" both shocks
and contacts: $\mathfrak s_i=2/(\mathsf a/\mathsf b+\mathsf b/\mathsf a)$ with
$\mathsf a=|\rho_i-\rho_{i-1}|+|\rho_i-2\rho_{i-1}+\rho_{i-2}|$, $\mathsf b=|\rho_i-\rho_{i+1}|+|\rho_i-2\rho_{i+1}+\rho_{i+2}|$,
the interface value the minimum over $\mathfrak s_{i-2},\dots,\mathfrak s_{i+3}$, $\xi=10^{-3}$, threshold
$\mathfrak s_c=0.5$ (Li, Chen & Ren use $\xi=10^{-2}$, 0.4). A higher threshold "reduces accuracy", a lower one
produces oscillations (stated, no data), and the approach is said to suit explicit better than compact
gradients, which are global (§2.4). With it the isentropic vortex converges at rates 6.0–6.7 instead of the
second order of the pure state reconstruction (Table 1).

## A three-region hybrid for steady states: WENO-H

Wan & Xia (2022, §3) argue that hybrid schemes are rarely used for steady problems "since the gap between
different kinds of approximations hinders the convergence of residue", and add a **transition region**.
With the Jiang–Shu indicators of the three stencils, the detector
$\mathfrak n=\tau_5/\big(\epsilon+\tfrac13\sum_k\beta_k\big)$ (page-local $\mathfrak n$; $\epsilon=10^{-6}$) is
$O(\Delta x^3)$ in smooth regions without critical points. A stencil is smooth for $\mathfrak n\le\tfrac12$
(fifth-order linear upwind reconstruction), non-smooth for $\mathfrak n\ge1$, and in transition between, where
the two reconstructions are blended by $M_{\mathrm t}(\mathfrak n)=\exp\!\big(-\tfrac{(2\mathfrak n-1)^2}{1-(2\mathfrak n-1)^2}\big)$
or the linear $2-2\mathfrak n$ (page-local $M_{\mathrm t}$; Eqs. (3.14)–(3.15)), which the authors call "essential for
the steady-state convergence" (no sharp-switch ablation shown). The non-smooth reconstruction uses the
[CWENO](/methods/cweno.md) stencils (a quartic and two linear polynomials) with linear weights
$(0.8,0.1,0.1)$ and WENO-ZQ-type weights whose ratio is divided by
$C_R=\big(\sum_{j=i-2}^{i+2}|u_j|\big)^2\Delta x+\beta_{\mathrm{opt}}+0.01$ (page-local; $\beta_{\mathrm{opt}}$ the quartic's indicator; Eqs. (3.2)–(3.4)), then blended with
the linear combination of the same polynomials so that its indicator stays bounded
([smoothness indicators](/definitions/smoothness-indicator.md)). WENO-H drives the average residue to
$10^{-12}$–$10^{-14}$ on all 14 steady tests, including flows past plates, square columns and a
[forward-facing step](/benchmarks/forward-facing-step.md), where CWENOZ or multi-resolution WENO stall in
some (§4; [multi-resolution WENO](/methods/multi-resolution-weno.md)); on smooth steady problems its errors
equal those of the linear scheme to every printed digit (Tables 4.1, 4.3).

## TENO-flag hybrids at discontinuities

Liang, Xiao, Shyy & Fu (2022) replace, in cells flagged by a detector built only from the TENO5 cut-off
flags, the TENO flux by a tanh interpolation; like [TENO-THINC](/methods/teno-thinc.md), this is a
hybrid whose second member is a jump reconstruction, not a linear scheme. They recall Hill & Pullin's
switch and WENO-RL as other hybrids (§1).

Zhang, Fleischmann, Adami & Adams (2024a, §3.3, Eq. (49), Algorithm 1) build the finite-volume analogue for the
five-equation two-phase model: all primitive variables are reconstructed by the
[incremental-stencil WENO](/methods/incremental-stencil-weno.md) WENO5IS, and in interfacial cells, detected
by $10^{-3}<\phi_1<1-10^{-3}$ with a locally monotone volume fraction (Eq. (46)), the volume fraction and the
two partial densities are replaced by [THINC](/methods/thinc-reconstruction.md) values, velocity and pressure
keeping the WENO values; a positivity- and boundedness-preserving blend with the first-order state follows
($\tilde q=\theta[(1-\delta)\tilde q^{\mathrm{WENO}}+\delta\tilde q^{\mathrm{THINC}}]+(1-\theta)\tilde q^{(1)}$, $\delta$ the
interface switch, $\theta$ the limiter factor, page-local here; [bound preservation](/properties/bound-preservation.md),
[five-equation model](/definitions/five-equation-model.md)).

## Blends with a first-order flux

A second kind of hybrid blends a WENO flux with a **first-order** one through a limiter function,
rather than switching to a linear high-order scheme:

- In MFC, Bryngelson et al. (2021, §4.2.2, Eq. (34)) add an optional flux limiter, because "the WENO
  schemes we utilize are, in general, not TVD": the flux is the first-order (piecewise-constant)
  Riemann flux plus a limiter of the volume-fraction ratio
  $(\phi_i-\phi_{i-1})/(\phi_{i+1}-\phi_i)$ (upwinded with the contact velocity; page-local
  volume fraction $\phi_i$) times the difference between the WENO and first-order fluxes, with
  minmod, MC, ospre, superbee, Sweby, van Albada or van Leer limiters; the blend is described in words
  ([MFC](/software/mfc.md)).
- Matsushita & Aoki (2021, §3.1, Eqs. (26)–(27)) write the advective derivative as
  $f_x^{\mathrm{1st}}+\psi(r_i)\big(f_x^{\mathrm{WENO}}-f_x^{\mathrm{1st}}\big)$ with the minmod
  limiter $\psi$ of the upwinded slope ratio $r_i$ and third-order Hamilton–Jacobi WENO, to prevent
  instabilities at the steep density change of a gas–liquid interface.

- McQuaid & Brehm (2024, §3.8, Eq. (20)) blend, on the Cartesian off-body grid of a hypersonic overset solver, a
  fifth-order characteristic-wise [WENO-Z](/methods/weno-z.md) flux with Steger–Warming splitting and a first-order flux,
  $\hat f_{i+1/2}=(1-\tilde\alpha_{\mathrm D})\hat f^{\mathrm{WENO}}_{i+1/2}+\tilde\alpha_{\mathrm D}\hat f^{\mathrm{O1}}_{i+1/2}$, with the
  "Ducros sensor value" $\tilde\alpha_{\mathrm D}$ (page-local, as on the Ducros page; cited to Ducros et al.) as weight (the formula, any threshold and the regularization are
  not printed; [Ducros sensor](/definitions/ducros-shock-sensor.md)), so that the scheme falls fully to first order at strong
  shocks. Of four convective treatments on a Mach 9.47 capsule at 8° (WENO-Z with local or stencil-wise Rusanov
  splitting, with Steger–Warming, and with the Ducros blend), only the blend removes the velocity streaks that a shock on
  the non-aligned Cartesian grid sends to the near-body interface and that imprint a surface-heating artefact, at the cost
  of a slightly more diffused shock (§4.1, Fig. 14).

The first two are TVD-limiter hybrids localized at material interfaces
([TVD limiters](/definitions/total-variation-diminishing.md)), the counterpart of the
low-order/high-order flux blending used for bound preservation
([positivity-preserving flux limiter](/methods/positivity-preserving-flux-limiter.md)).

## The sensor problem

Wang et al. (2021, §1), recalling Hu, Wang & Adams, call the hybrid method "minimally dissipative"
with "sharp shocks and well-resolved broadband turbulence", but say that it "relies on an appropriate
shock senor [sic]". Takagi et al. (2022, §1) state that hybrid schemes, although much less dissipative than their ENO or
WENO counterparts, depend in practice on the effectiveness of a shock sensor "which is mostly case
and parameter sensitive", and point to the parameter-free
[boundary variation diminishing](/definitions/boundary-variation-diminishing.md) selection as the
exception. Fu (2023, §3.4) recalls a systematic survey of shock sensors for hybrid schemes concluding
that hybrids generally perform better with a low-dissipation TENO than with WENO as the nonlinear
component, regardless of the sensor. Fu (2023, §5.4) also reports that the TENO6-A variant used for
transitional shock/boundary-layer interaction replaces the TENO discontinuity measure by a modified
Ducros sensor ([adaptive TENO](/methods/adaptive-teno.md)).

## Limits of the linear target

Luo & Wu (2021, §1) quote the common view behind hybridization: "the accuracy and resolution of the
upwind central are the limits of the improvement of the WENO scheme". They dispute it with WENO-Z+M,
whose nonlinear weights give smaller errors than the linear scheme UD5 itself on a smooth test
([WENO-Z+](/methods/weno-z-plus.md)). A hybrid cannot do better than its linear scheme in smooth
regions; the gain comes from the choice of that scheme, which TENO papers optimize spectrally
([approximate dispersion relation](/definitions/approximate-dispersion-relation.md)).

## Qualifications

- **Detector rankings depend on the test.** Fu (2023, §3.4) calls the TENO-based indicator "more
  universal" than physical sensors; Li, Chen & Ren (2022a, Figs. 9–12) measure it correct only below
  $\vartheta=0.64$ on sine waves, with detector inputs normalized by $\max(|f_{\max}|,1)$, a step to which
  they attribute TENO-HY's better detection than in Fu's own paper (§4.3.1).
- Chamarthi (2023b) prints the regularization $\varepsilon=\tfrac{0.9\mathfrak s_c}{1-0.9\mathfrak s_c}\xi^2$ (Eq. (37)) but
  not in the detector (Eq. (35)), which is then undefined on constant density; Chamarthi attributes the detector once to
  Li & Jaberi and once, as "the original paper", to Li, Chen & Ren.
- De Vanna et al. (2023a)'s thresholds belong to their non-squared, compression-only sensor with
  $\epsilon_{\mathrm D}=(v_\infty/\delta_0)^2$; they are not transferable to the classical squared Ducros ratio.
- Wan & Xia (2022, Example 4.3) state fifth order for all schemes on the isentropic vortex while their
  WENO-H orders are 2.42 ($L^\infty$) at $80^2$ and 8.19 at $160^2$, with an $L^1$ error at $80^2$ about 3.5
  times that of the linear UW5 (Table 4.2); their bound on the blended indicator is misstated (see
  [smoothness indicators](/definitions/smoothness-indicator.md)).
- Wang et al. (2023c) call their efficiency "the highest among these three methods" (Example 4.1)
  and claim improved efficiency throughout, while their Table 5.1 has the hybrid slower than WENO-JS in
  four of twelve runs (1.01–1.07); it is always faster than the non-hybrid MR-WCNS.
- **TENO-type indicator settings.** The same construction is run with $\epsilon=10^{-4}$ and threshold $5\times10^{-4}$ on
  four stencils (Fu's, as recalled by Li, Chen & Ren 2022a) and with $\epsilon=10^{-4}$ or $10^{-2}$ by dimension and
  threshold $10^{-6}$ on six equal stencils (Liang & Fu 2024b), absolute values applied to the raw conserved variables.
  Liang & Fu present the parameters as fixed for all tests, yet $\epsilon$ changes with the number of dimensions.
- Liang & Fu (2024b, Abstract, §4.10) describe TENO-S as performing inviscid Taylor–Green computations "without numerical
  dissipation". *(Compiler check, not in the sources: the split form conserves kinetic energy semi-discretely only where it
  is used; the TENO branch acts in flagged cells and SSP-RK3 is not kinetic-energy-conservative, so the evidence is the
  plotted energy history of Fig. 17, not an exact property.)*
- McQuaid & Brehm (2024) attribute the residual heating differences of their capsule cases (slight leeward
  over-prediction at 8°, lower peak temperature on AS-202) to the first-order fallback at the shock; this is their
  interpretation, not a tested result (§4.1, §4.3).
- The factor-four speed-up of the hybrid TENO is quoted from earlier work in a review; neither the
  hardware nor the share of flagged points is given in the review.

# Citations

- [Fu (2023)](/sources/fu-2023.md) — §1; §3.4, Eqs. (21)–(24), Fig. 7; §5.4.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §1; §3.2.
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §1; §5.3.1, Table 1.
- [Fu (2021)](/sources/fu-2021.md) — §1.
- [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) — §1; §4, Table 4.2.
- [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) — §4.2.2, Eq. (34).
- [Matsushita & Aoki (2021)](/sources/matsushita-2021.md) — §3.1, Eqs. (26)–(27).
- [Wang et al. (2021)](/sources/wang-2021.md) — §1.
- [Li, Chen & Ren (2022a)](/sources/li-2022.md) — §3.2, Eqs. (46)–(60), Figs. 9–12; §3.4; §4.2–4.3.
- [Wan & Xia (2022)](/sources/wan-2022.md) — §1; §3, Eqs. (3.1)–(3.15), Algorithm 1, Remark 3.1; §4, Tables 4.1–4.3.
- [Liang et al. (2022)](/sources/liang-2022.md) — §1; §3.1–3.2.
- [Balsara, Samantaray & Subramanian (2023)](/sources/balsara-2023.md) — §6.3.
- [Hong, Ye & Ye (2022)](/sources/hong-2022.md) — §1.
- [De Vanna et al. (2023a)](/sources/devanna-2023.md) — §3.1–3.2, Eq. (9); §4.3–4.4, Table 2, Figs. 5–9; §6.
- [De Vanna et al. (2023b)](/sources/devanna-2023-b.md) — §3.2.
- [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) — §2.4, Eqs. (31)–(37); §3, Table 1.
- [Bielawski et al. (2023)](/sources/bielawski-2023.md) — App. A.2, Figs. A.15–A.16.
- [Li et al. (2023b)](/sources/li-2023-b.md) — §3.5–3.6, Eqs. (51)–(61); §4, Figs. 15–23.
- [Wang et al. (2023c)](/sources/wang-2023-c.md) — §1; §3, Step 2, Eqs. (3.6)–(3.9), Remarks 1, 3; §4, Examples 4.1, 4.7, Tables 4.1–4.4; §5, Table 5.1.
- [Liang & Fu (2024b)](/sources/liang-2024-b.md) — §1; §3.1–3.3, Eqs. (31)–(35), Algorithm 1; §4, Tables 1–2, 7, 9, Figs. 17–18; §5.
- [McQuaid & Brehm (2024)](/sources/mcquaid-2024.md) — §3.8, Eq. (20); §4.1, Fig. 14.
- [Zuo & Zhu (2024a)](/sources/zuo-2024.md) — §1; §2.2, Eqs. (2.21)–(2.33), Algorithm 1, Remarks 1–2; §3, Tables 3.1–3.4, Examples 3.4–3.7.
- [Zuo & Zhu (2024b)](/sources/zuo-2024-b.md) — §1; §2.2, Eqs. (2.15)–(2.19), Algorithm 1, Remarks 1–3; §3, Tables 3.1–3.4.
- [Zhang et al. (2024a)](/sources/zhang-2024.md) — §3.3, Eqs. (46)–(49), Algorithm 1.
