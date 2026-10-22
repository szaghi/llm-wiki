---
type: Definition
title: "Numerical dissipation and anti-dissipation"
description: "Numerical dissipation is the part of a scheme's error that damps resolved content, anti-dissipation the part that amplifies or steepens it; the page fixes three measures (flux viscosity term, leading truncation error, imaginary part of the modified wavenumber), the design levers of the sources, and the implicit-LES evidence that dissipation order outweighs convective order."
status: established
aliases: [numerical diffusion, numerical viscosity, anti-diffusion, negative dissipation, ND, high-order artificial dissipation, JST dissipation]
tags: [low-dissipation, numerical-flux, reconstruction, central-scheme]
timestamp: 2026-10-22T20:00:00Z
---

# Numerical dissipation and anti-dissipation

**Numerical dissipation** (numerical diffusion, ND) is the part of the
discretization error that acts like a diffusion term, damping resolved
gradients and Fourier modes; **anti-dissipation** (anti-diffusion, negative
dissipation) is error of the opposite sign, which steepens profiles and amplifies
modes. Shock capturing needs some dissipation at discontinuities; the
low-dissipation literature of this bundle tries to remove it everywhere else.
The sources measure it in three compatible ways, each tied to a
different object.

## 1. The viscosity term of the numerical flux

A two-point flux can be written as a central part plus a dissipation term. For
the Riemann-solver fluxes this is the unified form
$\hat f_{i+1/2}=\tfrac12\big(f(u^-_{i+1/2})+f(u^+_{i+1/2})\big)-\tfrac12\lvert\tilde a_{i+1/2}\rvert[\![u]\!]_{i+1/2}$,
with an averaged signal speed $\tilde a$ fixed by the solver
([Fu (2023)](/sources/fu-2023.md), §3.6, Eq. (29)); the
[local Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md) $h^{\mathrm{LF}}$
is the case $\tilde a=a$. The dissipation is the product of a speed and the
interface jump, so it can be reduced by smaller speed estimates or by smaller
jumps.

- **Smaller jumps** is the logic of [BVD](/definitions/boundary-variation-diminishing.md)
  and of sharper reconstructions such as [THINC](/methods/thinc-reconstruction.md).
- **Smaller speeds.** The [central-upwind flux](/methods/central-upwind-scheme.md)
  uses the one-sided speeds $a^\pm_{i+1/2}$; it "in general" carries more ND than
  upwind fluxes but needs no Riemann solver
  ([Wang et al. (2023)](/sources/wang-2023-b.md), §1). Wang et al. reduce ND by
  tightening $a^\pm$ with regularized discrete Rankine–Hugoniot speeds, by
  replacing them in smooth regions (relative interface jump $\le\Delta x^2$) by
  symmetric speeds built from the fluid velocity and capped by $0.1$ of the
  acoustic estimate, and in 2D by a dissipation switch that scales the sound-speed
  part of $a^\pm$ by the ratio of internal-plus-normal-kinetic-energy jumps to the
  total, which damps it at contacts and shear layers (§3, Eqs. (6)–(18); see
  [adaptive-diffusion CURH flux](/methods/adaptive-diffusion-central-upwind-flux.md)).
  The CURH flux they start from already subtracts a minmod "anti-diffusion"
  correction $\delta U$ from the jump (§3, Eq. (5)): here "anti-diffusion" means a
  reduction of the diffusion term, not a negative one.
- **Field-wise speeds.** [Chertock et al. (2023)](/sources/chertock-2023.md)
  (§3, Eqs. (3.1)–(3.8)) rewrite the central-upwind flux as a central average plus
  a diffusion term $D_{i+1/2}$ and express $D$ through the
  [characteristic decomposition](/methods/characteristic-decomposition.md) at
  $x_{i+1/2}$, with diagonal matrices whose entries are the same scalar functions
  of $a^\pm$ for every field. Replacing these entries by the same functions of the
  one-sided characteristic speeds $\lambda^\pm_l$ gives each field its own
  dissipation; for a linear system the new flux is the upwind flux
  $A^+u^-_{i+1/2}+A^-u^+_{i+1/2}$ whatever the signs of the eigenvalues
  (Lemma 3.1), whereas the original reduces to upwind only when all eigenvalues
  have one sign. See [LCD central-upwind scheme](/methods/lcd-central-upwind-scheme.md).
- **A scalar or a matrix speed.** [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md)
  (§3, Eqs. (20)–(22)) write the first-order upwind flux of a finite-difference
  scheme as $\hat f_{i+1/2}=\tfrac12(f_i+f_{i+1})-\tfrac12\lvert Q_{i+1/2}\rvert(u_{i+1}-u_i)$,
  with a dissipation matrix $Q$ ($Q=a_{i+1/2}I$ gives Rusanov, the Roe matrix gives
  Roe; page-local $Q$). They choose the scalar $a_{i+1/2}$, the spectral radius of
  $A$, because the Roe average has no unique, cheap extension to real and
  multi-species gases, and they attribute to this choice the extra damping of the
  entropy waves behind the shock of the [Shu–Osher problem](/benchmarks/shu-osher-problem.md):
  the scalar viscosity acts equally on acoustic and entropic fields (§4.3, Fig. 4).

- **The choice of solver.** Several sources replace a Lax–Friedrichs-type flux by HLLC for
  this reason. [Bai & Li (2022)](/sources/bai-2022.md) (§2.4) adopt an HLLC–HLL hybrid instead
  of the Lax–Friedrichs flux of an earlier DG cut-cell code "to reduce the numerical
  dissipation", and attribute that code's delayed interface evolution in an air–helium
  shock–bubble interaction to its Lax–Friedrichs flux and low-order cut-cell scheme (§3.4,
  Fig. 25). [Nguyen et al. (2022)](/sources/nguyen-2022.md) (§3.1, Figs. 3–4) find the Rusanov
  flux more diffusive than HLLC on a low-Mach water–air interface, whose thickness grows in time
  with the van Leer limiter. See [HLL-family solvers](/methods/hll-riemann-solvers.md).
- **Built-in anti-diffusion and limiter parameter.** In the path-conservative central-upwind
  scheme of [Chu et al. (2022)](/sources/chu-2022.md) (§2) the jump term carries the same minmod
  anti-diffusion as the CURH flux above, and the generalized minmod parameter $\theta\in[1,2]$
  of the reconstruction (page-local, not the Zhang–Shu factor) is a dissipation control: larger $\theta$ is less dissipative and more
  oscillatory. Chu et al. also state that the original finite-difference WENO relies on flux
  splitting, "which is quite diffusive", and motivate [A-WENO](/methods/alternative-weno.md),
  which uses finite-volume fluxes without splitting (§1); no comparison is run.
- **Where the dissipation belongs in a disturbance formulation.**
  [Browne et al. (2022)](/sources/browne-2022.md) (§2.2) argue that in equations for the
  disturbance about a baseflow the Rusanov dissipation should be the full spectral radius times
  the disturbance only, and drop a term proportional to the baseflow state as destabilizing
  ([Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md)).

### An explicit high-order dissipation term

The same flux form with a higher-order dissipation term is the Lerat–Corre
family that [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) (§3,
Eqs. (23)–(28)) build on: a central approximation of order $2(P+2)$ of the
flux derivative on $2(P+2)+1$ points plus a dissipation term of order $2P+3$,
proportional to $\lvert Q\rvert\Delta^{2P+3}u$ (here $\Delta^m$ is the $m$-th
undivided difference of the registry, taken at the interface for odd $m$;
$P=0,\dots,3$ gives orders 3, 5, 7, 9). Following Jameson, Schmidt and Turkel, the
authors blend it with a second-order term switched on by a shock sensor (§3,
Eqs. (30)–(31)):

$$\begin{aligned}
D_{i+1/2}&=a_{i+1/2}\Big[\mathsf c_{2}\,[\![u]\!]_{i+1/2}+(-1)^{P+1}\mathsf c_{2P+4}\,\Delta^{2P+3}u_{i+1/2}\Big],\\
\mathsf c_{2}&=k_2\max(\Xi_i,\Xi_{i+1}),\qquad
\mathsf c_{2P+4}=\max\big(0,\ k_{2P+4}-k_\varepsilon\,\mathsf c_2\big),
\end{aligned}$$

with $\hat f_{i+1/2}$ the central part minus $D_{i+1/2}$ (page-local:
$\mathsf c_2$, $\mathsf c_{2P+4}$ the blended coefficients, $k_2$, $k_{2P+4}$,
$k_\varepsilon$ constants, $\Xi_i$ the sensor). The default is the
ninth-order member, $P=3$, with $k_2=1$ and $k_{10}=1/1260$, the upwind value;
the shock tubes use $k_2=2$, $k_{10}=1/630$. The sensor is the product of three
factors (§3, Eq. (36)):

$$\Xi_i=\tfrac12\Big[1-\tanh\Big(2.5+10\,\tfrac{\Delta x}{c}\nabla\!\cdot v\Big)\Big]\cdot\frac{(\nabla\!\cdot v)^2}{(\nabla\!\cdot v)^2+\lvert\nabla\times v\rvert^2+\epsilon}\cdot\Big\lvert\frac{p_{i+1}-2p_i+p_{i-1}}{p_{i+1}+2p_i+p_{i-1}}\Big\rvert,\qquad\epsilon=10^{-16},$$

the Bhagatwala–Lele dilatation switch, the Ducros dilatation-to-vorticity ratio
and Jameson's pressure sensor. On an underexpanded jet the authors show each
factor's failure alone (Ducros close to one in smooth irrotational regions,
Jameson unable to separate a shock from a high-vorticity solenoidal region,
Bhagatwala–Lele over-damping dilatation on coarse grids) and the product
confining the low-order term to the shocks, with values below $0.02$ elsewhere
(§5.1, Fig. 8). In 1D the Ducros factor is inactive, and the Bhagatwala–Lele
factor improves the entropy waves of the Shu–Osher problem by suppressing
spurious activations of the pressure sensor (§4.3); on the reacting 9000 K shock
tube it had to be turned off "for better numerical robustness" (§4.4). The same
blend of a low- and a high-order term is the idea of
[artificial viscosity](/methods/artificial-viscosity.md) and of the
[hybrid schemes](/methods/hybrid-weno.md); this one is explicit in the flux.

## 2. The leading truncation error of a reconstruction

On a three-cell compact stencil, the leading error of a second-order linear
reconstruction is $4(\tfrac13-\mu_0)(\tfrac12-\tilde u_i)u'\Delta x+O(\Delta x^3)$,
diffusive or anti-diffusive according to the sign of $(\tfrac13-\mu_0)(\tfrac12-\tilde u_i)$
([Deng (2023)](/sources/deng-2023.md), Proposition 5, Table 1; $\mu_0$ the
intercept of the operator on the
[normalised-variable diagram](/definitions/normalised-variable-diagram.md),
$\tilde u_i$ the normalised cell average). Two consequences:

- the sign depends on the data, not only on the scheme (Deng, Remark 3.1);
  symmetric TVD limiters, for example, are dissipative for $\tilde u<1/2$ and
  anti-dissipative for $\tilde u>1/2$ (§4.1);
- on the diagram, curves below the third-order line P3 are diffusive and curves
  above it anti-diffusive (§5).

For the odd-order Lerat–Corre schemes the leading truncation error is
$\frac{\mathsf a_P}{2}\Delta x^{2P+3}\partial_x^{2(P+2)}u$, an even-order derivative, which
the authors call dissipative ([Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md), §3,
Eq. (24); $\mathsf a_P$ the page-local last correction coefficient of the
family, $\mathsf a_3=-1/630$). The authors choose the dissipation order so that the overall
truncation error is dissipation dominated, to limit the appearance and
amplification of spurious oscillations and the activation of the low-order term
(§1); they also recall that explicit odd-order constant-coefficient schemes are
$L^\infty$-stable for non-smooth data under a CFL condition, so their
oscillations stay bounded (§3, citing Thomée and Després). Because the sensor
is off at a contact (constant pressure), the contact smearing in their Sod and
Lax tubes is due to the high-order term alone (§4.2).

Deng's low-dissipative [ROUND](/methods/round-scheme.md) operators deliberately
put parts of the curve above P3, so that positive and negative second-order
errors partly cancel over a cell (Remark 7.2), and Huang et al.'s LD-ROUND does
the same with "controlled anti-dissipation" whose amount grows with two shape
parameters; larger values "may introduce excessive anti-dissipation errors and
potentially lead to numerical instability"
([Huang et al. (2026)](/sources/huang-2026.md), §4.2).

## 3. The imaginary part of the modified wavenumber

In the [approximate dispersion relation](/definitions/approximate-dispersion-relation.md)
of a scheme, $\tilde\vartheta_i<0$ is dissipation and $\tilde\vartheta_i>0$
anti-dissipation (the sign convention of Fu 2023, used by all chunk-1 sources
cited here). Measured this way:

- THINC with $\beta_{\mathrm T}=1.6$ is anti-diffusive in some wavenumber
  ranges, like Superbee ([Takagi et al. (2022)](/sources/takagi-2022.md), §2.3);
- WENO-Z+ with a large coefficient has a narrow band of negative dissipation
  near $\vartheta\approx1.18$ ([Luo & Wu (2021)](/sources/luo-2021-b.md), §3).

**Nonlinear dissipation of WENO weights.**
[Luo & Wu (2021)](/sources/luo-2021-b.md) (§4) split the dissipation of a WENO
scheme into the linear one of its background scheme (UD5 at fifth order) and a
nonlinear one due to the weights: when the least smooth candidate stencil gets
less than its linear weight, $\omega_D<d_D$, the weighting adds positive
dissipation, so classical WENO is always more dissipative than UD5; WENO-Z+-type
weights give it more, $\omega_D>d_D$, which adds negative dissipation partly
cancelling the linear one, so their spectral curves can beat UD5's in a
wavenumber band. The argument is supported by plots of $\omega_k/d_k$ on Fourier
modes, not by a proof. TENO avoids nonlinear dissipation in smooth regions
differently, by restoring the linear weights exactly
([targeted ENO](/methods/targeted-eno.md)). The same contrast appears in
the weighted compact nonlinear schemes of [Hiejima (2022)](/sources/hiejima-2022.md) (§3.3–3.4,
Figs. 4, 7): with Jiang–Shu weights in the substencils the Shu–Osher result does not change
from fifth to eleventh order and the double-Mach slip line does not roll up at any order,
which the author attributes to the dissipation of the Jiang–Shu weights, "consistent with"
WENO-JS; with TENO-type cut-off weights the high-frequency waves and the Kelvin–Helmholtz
roll-up appear and grow with the order, at the price of weak oscillations that depend on the
cut-off $C_T$. [Bezgin et al. (2022)](/sources/bezgin-2022.md) (§3.2, §3.4) penalize in the
training loss of their learned WENO3 weights the deviation of the weights from the linear
weights in smooth data; without that penalty the scheme converges only at second order (orders
1.90 and 1.95 on two test functions), with it at about third order on $\tanh(2x)$ (2.93)
([learned WENO weights](/methods/learned-weno-weights.md)).

## Explicit dissipation: artificial viscosity and its spectral shape

A scheme can also carry no upwind dissipation and receive an explicit viscosity instead, whose
amount and spectral distribution are design choices
([artificial viscosity](/methods/artificial-viscosity.md)).

- **Spectral shape.** [Sousa & Scalo (2022)](/sources/sousa-2022.md) (§2.3, Fig. 1) compute the
  exact subfilter energy flux of the filtered inviscid Burgers equation as a shock forms: it
  spans all resolved wavenumbers with a "plateau-cusp" rising toward the cut-off. The dynamic
  Smagorinsky model, with a flat broadband spectrum, over-dissipates the large scales and
  under-dissipates near the cut-off, which a posteriori gives a high-wavenumber pile-up and
  oscillations; spectral vanishing viscosity with an inviscid low-wavenumber range always
  under-damps those wavenumbers. Their conclusion, shown on this one Burgers case, is that
  "the closer the spectral content of the added dissipation is to the exact SFS stresses, the
  better is the performance". Their [quasi-spectral viscosity](/methods/quasi-spectral-viscosity.md)
  imposes this shape with filter residuals on a sixth-order compact central scheme and serves as
  both the shock-capturing term and the LES model; on the supersonic Taylor–Green vortex at
  $M_t=1.2$ all runs that add local artificial diffusivity to an LES model over-dissipate at the
  strongest shocklets, while QSV alone stays closest to the fine-grid QSV reference (§7.1,
  Fig. 19). That reference is itself a QSV run.
- **The monotone amount.** In the first-order analysis of the time-reversibility viscosity of
  [Dzanic et al. (2022)](/sources/dzanic-2022.md) (§3.1, Eqs. (18)–(20)) the viscosity at a jump
  tends to $c_\mu a\Delta x$ as $\Delta t\to0$; with $c_\mu=\tfrac12$ it is exactly the viscosity
  that turns a second-order central scheme into first-order upwind (page-local constant
  $c_\mu$). Their viscosity is vector-valued, one entry per conserved component.
- **Over-dissipation by the indicator.** [Yu & Hesthaven (2022)](/sources/yu-2022.md) (§4.1.3,
  Fig. 4) report that the averaged modal-decay indicator of Klöckner et al. estimates a decay rate
  close to the polynomial degree in constant regions, so its artificial viscosity over-dissipates
  there below degree four; their neural-network estimate of the decay rate does not
  ([troubled-cell indicator](/definitions/troubled-cell-indicator.md)).
- **Filtering as dissipation.** [Edoh (2022)](/sources/edoh-2022.md) (App. B, Eqs. (B.1)–(B.5))
  writes solution filtering of a kinetic-energy-preserving central scheme as an artificial
  dissipation operator $\bar{\mathcal D}\le0$ (page-local) and shows in the semi-discrete limit
  that filtering the total energy decreases the global entropy, filtering the momentum increases
  it and filtering the mass is indefinite; momentum-only filtering gives strict kinetic-energy
  decay and entropy increase for all his splittings and avoids vortex-core deepening on a long
  isentropic-vortex run (Figs. B.5–B.6; see
  [kinetic energy preservation](/properties/kinetic-energy-preservation.md),
  [entropy stability](/properties/entropy-stability.md)).

## Dissipation as an implicit subgrid model

[Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) use the ninth-order
dissipation as implicit LES regularization, acting only on
$\vartheta\gtrsim0.35\pi$ ([approximate dispersion relation](/definitions/approximate-dispersion-relation.md)).
On the compressible [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
(Re 1600, $M=0.1,0.5,1$, $64^3$–$1024^3$) they report (§5.2, Figs. 9–12):

- no energy pile-up at small scales even at $64^3$, and the low-order term
  correctly off at $M=0.1$;
- third-order dissipation on $256^3$ gives results similar to ninth-order
  dissipation on $64^3$; going beyond ninth order gains little;
- third-order dissipation combined with convective fluxes of orders up to ten
  gives nearly identical results, so "the dissipation order is the fundamental
  ingredient";
- at low Mach number the small scales are damped more, because the acoustic
  time-step limit needs more steps to reach $t^*=16$, hence more applications of
  the dissipation operator (an interpretation, §5.2).

The numerical dissipation rate in such runs is measured, after Schranner et al., as the
kinetic-energy decay not accounted for by the resolved viscous work,
$\epsilon_{\mathrm{num}}=\big\langle-\partial_te_{\mathrm{ke}}-v_i\,\delta_j\tau_{ij}\big\rangle_\Omega$ (volume average,
$e_{\mathrm{ke}}=\tfrac12v_iv_i$, $\delta_j$ the discrete derivative and $\tau_{ij}$ the viscous stress, all page-local), by [Edoh (2022)](/sources/edoh-2022.md) (§4.2,
Eq. (33)); on the Taylor–Green vortex at Re 1600 on $64^3$ his rotational-form splitting shows
the larger $\epsilon_{\mathrm{num}}$ and density variability than the Kennedy–Gruber splitting,
attributed to aliasing, and the kinetic-energy-preserving splittings agree as the grid is refined
(Fig. 3).

In the opposite direction, [Wang et al. (2021)](/sources/wang-2021.md) motivate
their multi-resolution WENO by the observation, recalled from Johnsen et al.,
that WENO dissipation can overwhelm physical dissipation in turbulence (§1), and
find the new scheme the closest of four WENO schemes to the DNS kinetic-energy
history of the Taylor–Green vortex at $128^3$ (Example 5.13, Fig. 5.22).

## Reading dissipation off 2D results

Without a closed-form measure, the 2D sources compare dissipation through flow
features that only dissipation suppresses: the curliness of the contact in the
explosion problem, which is physically unstable and "may be stabilized by the ND
only", and the distance travelled by the jet of the implosion problem
([Wang et al. (2023)](/sources/wang-2023-b.md), Examples 6–7); Chertock et al.
present the explosion problem as a benchmark of the amount of ND and compare at
equal CPU time on the implosion (Examples 6–7). For the Kelvin–Helmholtz
problem, where solutions do not converge under refinement,
[Chertock et al. (2023)](/sources/chertock-2023.md) (Example 8, Fig. 5.9) find
different Cesàro averages for the original and the LCD central-upwind schemes
and read this as non-uniqueness of the limiting dissipative weak solution,
which "apparently depends on the choice of the numerical diffusion".

Two more proxies: [Chen et al. (2022)](/sources/chen-2022.md) (§6.7, Table 3)
read the shorter recirculation length behind a cylinder at $\mathrm{Re}=40$ (2.095 against 2.14
without, experiment 2.13) produced by a face-gradient correction of the viscous flux as extra
numerical dissipation; [Bai & Li (2022)](/sources/bai-2022.md) (§2.5.2, §3.4) call the zero-order
real–ghost mixing of cut cells, transplanted from finite volumes to DG, "excessively
dissipative", the evidence being a delayed interface evolution in the shock–bubble interaction.

## Qualifications

- The three measures are not interchangeable. The flux viscosity is local and
  pointwise, the truncation-error sign is a smooth-data statement, the ADR is a
  linear-advection statement on single modes; a scheme can be anti-dissipative in
  one sense and dissipative in another (Deng's symmetric limiters change sign
  with $\tilde u$).
- Visual dissipation proxies (curlier contacts, more vortices) are what most of
  the chunk-1 2D claims rest on; none of these sources quantifies them.
- Sciacovelli et al. state $k_\varepsilon=\mathsf a_0/\mathsf a_P$, but their explicit members
  print the factors $1$, $\tfrac15$, $\tfrac3{70}$, $\tfrac1{105}$, which are
  $\lvert\mathsf a_P/\mathsf a_0\rvert$; and the sign $-\tfrac{\mathsf a_P}{2}$ of their general
  formula disagrees with the signs of the four explicit members (§3,
  Eqs. (23)–(35)). The page uses the explicit members. Their conclusion on
  dissipation order versus convective order is an ILES conclusion on one
  turbulence test; it is not stated for shocked flows.

# Citations

- [Fu (2023)](/sources/fu-2023.md) — §3.6, Eq. (29): flux as central part plus jump term.
- [Wang et al. (2023)](/sources/wang-2023-b.md) — §1, §3, Eqs. (5)–(18), Examples 6–7: CURH speeds, ND switch, ND proxies.
- [Chertock et al. (2023)](/sources/chertock-2023.md) — §3, Lemma 3.1, Examples 6–8: field-wise diffusion, Cesàro averages.
- [Deng (2023)](/sources/deng-2023.md) — Proposition 5, Table 1, Remarks 3.1, 7.2, §§4.1, 5: sign of the leading error.
- [Huang et al. (2026)](/sources/huang-2026.md) — §4.2: controlled anti-dissipation.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §2.3: anti-diffusive THINC.
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §§3–4: negative dissipation, nonlinear dissipation of weights.
- [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) — §1, §3 (Eqs. (20)–(36)), §4.2–4.4, §5.1–5.2 (Figs. 4, 8–12): scalar dissipation, Lerat–Corre family, JST-type blend, sensor, ILES (arXiv v1).
- [Wang et al. (2021)](/sources/wang-2021.md) — §1, Example 5.13 (Fig. 5.22): WENO dissipation in turbulence.
- [Bai & Li (2022)](/sources/bai-2022.md) — §2.4, §2.5.2, §3.4 (Fig. 25): HLLC instead of Lax–Friedrichs, dissipative zero-order mixing.
- [Nguyen et al. (2022)](/sources/nguyen-2022.md) — §3.1, Figs. 3–4: Rusanov versus HLLC at low Mach.
- [Chu et al. (2022)](/sources/chu-2022.md) — §1, §2: built-in anti-diffusion, minmod parameter, flux splitting called diffusive.
- [Browne et al. (2022)](/sources/browne-2022.md) — §2.2: Rusanov dissipation in disturbance form.
- [Hiejima (2022)](/sources/hiejima-2022.md) — §3.3–3.4, Figs. 4, 7: dissipative Jiang–Shu weights in WCNS.
- [Bezgin et al. (2022)](/sources/bezgin-2022.md) — §3.2, §3.4 (Fig. 2): ideal-weight penalty and order.
- [Sousa & Scalo (2022)](/sources/sousa-2022.md) — §2.3 (Fig. 1), §7.1 (Fig. 19): spectral shape of added dissipation (arXiv v2).
- [Dzanic et al. (2022)](/sources/dzanic-2022.md) — §3.1, Eqs. (18)–(20): monotone viscosity (arXiv v2).
- [Yu & Hesthaven (2022)](/sources/yu-2022.md) — §4.1.3, Fig. 4: over-dissipation of the averaged modal-decay indicator.
- [Edoh (2022)](/sources/edoh-2022.md) — §4.2 (Eq. (33), Fig. 3), App. B (Eqs. (B.1)–(B.5), Figs. B.5–B.6): numerical dissipation rate, filtering as dissipation.
- [Chen et al. (2022)](/sources/chen-2022.md) — §6.7, Table 3: wake length as dissipation proxy.
