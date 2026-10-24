---
type: Definition
title: "Numerical dissipation and anti-dissipation"
description: "Numerical dissipation is the part of a scheme's error that damps resolved content, anti-dissipation the part that amplifies or steepens it; the page fixes three measures (flux viscosity term, leading truncation error, imaginary part of the modified wavenumber), the design levers of the sources, including scale-adaptive control, the non-dissipative alternative, and the implicit-LES evidence on dissipation order."
status: established
aliases: [numerical diffusion, numerical viscosity, anti-diffusion, negative dissipation, ND, high-order artificial dissipation, JST dissipation]
tags: [low-dissipation, numerical-flux, reconstruction, central-scheme]
timestamp: 2026-10-24T05:59:00Z
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
  [Wakimura et al. (2024)](/sources/wakimura-2024.md) (§1, §3.2.1, Eq. (26)) state it
  for the scalar flux $\tfrac12(f(u^-)+f(u^+))-\tfrac{\lvert a\rvert}2(u^+-u^-)$ and
  motivate their two-phase BVD scheme by the limiter dissipation of MUSCL, which smears
  discontinuities; to their knowledge, vapour–liquid interfaces created dynamically by
  phase change "have never been captured" because of it.
  [Huang et al. (2025b)](/sources/huang-2025-b.md) (§3.2, Eq. (18)) give the same rationale
  for MUSCL-THINC-BVD, calling $\lvert u^+-u^-\rvert$ the "boundary variation" whose
  minimization reduces the dissipation of the flux, and keep it while replacing the selection by
  a network prediction ([BVD](/definitions/boundary-variation-diminishing.md)).
- **Smaller speeds.** The [central-upwind flux](/methods/central-upwind-scheme.md)
  uses the one-sided speeds $a^\pm_{i+1/2}$; it "in general" carries more ND than
  upwind fluxes but needs no Riemann solver
  ([Wang et al. (2023b)](/sources/wang-2023-b.md), §1). Wang et al. (2023b) reduce ND by
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
- **A sensor-scaled Rusanov coefficient.** [Wang et al. (2023a)](/sources/wang-2023.md)
  (§3.2, Eqs. (18)–(21)) keep the local Lax–Friedrichs form inside fifth-order
  [A-WENO](/methods/alternative-weno.md) and multiply its coefficient by
  $\max\{\mathsf k_i,\mathsf k_{i+1}\}$, $\mathsf k_i=\max\big(0.1,1-\exp(-10^5\varphi_{\mathrm F,i})\big)$
  (page-local), with $\varphi_{\mathrm F}$ the product of the
  [Ducros ratio](/definitions/ducros-shock-sensor.md) and normalized second differences of
  pressure and density. The stated aim is a small coefficient in smooth regions and the full spectral-radius
  bound near high gradients (§3.1). The floor 0.1 keeps a baseline dissipation where primitive
  variables are constant or linear (Fig. 1). In smooth regions of the Sod and blast-wave
  problems the coefficient falls to about one tenth of the LLF one (Figs. 6, 8). The 2D tests
  show more slip-line and vortex roll-up at 5%–9% extra cost (§4, Table 3); see the
  [Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md) for the evidence and the missing
  monotonicity statement.
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
- **Limiter compression switched by a roughness test.** In the adaptive
  [low-dissipation central-upwind schemes](/methods/low-dissipation-central-upwind-scheme.md) of
  [Chu et al. (2025a)](/sources/chu-2025.md) (§2, Eq. (2.6); arXiv v1, two authors) the flux keeps
  its built-in anti-diffusion, and the amount of dissipation is moved into the slope limiter. The
  two-parameter SBM limiter of Lie & Noelle,
  $\psi^{\mathrm{SBM}}(r)=\min\{\beta r,\,1+\tau_{\mathrm S}(r-1)\}$ on $0<r\le1$, $0$ for $r<0$ and
  $r\,\psi^{\mathrm{SBM}}(1/r)$ otherwise ($\beta\in[1,2]$ and $\tau_{\mathrm S}$ page-local, the
  source's $\theta$ and $\tau$, as on the [TVD](/definitions/total-variation-diminishing.md) page;
  $r$ the slope ratio), is classified, after Lie & Noelle, as dissipative for $\tau_{\mathrm S}\ge0.5$ (contacts
  smeared in time), compressive for $0\le\tau_{\mathrm S}<0.5$ (contacts sharp, smooth extrema
  compressed into kinks) and overcompressive for $\tau_{\mathrm S}<0$ (contacts very sharp,
  smooth profiles turned into staircases or artificial $O(1)$ jumps); larger $\beta$ is less
  dissipative and in general more oscillatory (§2.1.1). With $\beta=2$, $\tau_{\mathrm S}=0.5$
  is the Minmod2 limiter. The adaptive scheme uses $\tau_{\mathrm S}=-0.25$ only in cells a
  roughness indicator flags and Minmod2 elsewhere, in local characteristic variables; it
  resolves the smooth parts of shock–wave interactions, the blast-wave contact and 2D
  instabilities better than Minmod2 everywhere (§4, figures only). With a weak-local-residual
  indicator whose threshold constant is tuned on a coarse mesh, the overcompressive limiter
  reaches smooth regions on a fine mesh and staircases appear (Example 2, Fig. 4.3), the
  failure that the paper's own classification predicts for the overcompressive setting in
  smooth flow.
- **Where the dissipation belongs in a disturbance formulation.**
  [Browne et al. (2022)](/sources/browne-2022.md) (§2.2) argue that in equations for the
  disturbance about a baseflow the Rusanov dissipation should be the full spectral radius times
  the disturbance only, and drop a term proportional to the baseflow state as destabilizing
  ([Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md)).

- **Anti-diffusion of linearly degenerate waves, and its price.** The HLLEM flux adds to
  HLLE "anti-diffusion" terms for the entropy and shear waves, i.e. it removes part of the
  HLLE dissipation on those fields, which resolves contacts like Roe
  ([Hu, Yuan & Zhao (2022)](/sources/hu-2022.md), §2.3, Eqs. (2.7)–(2.8)). Their linear
  saw-tooth analysis shows the price: in the flux transverse to a grid-aligned shock, density
  and shear-velocity perturbations get amplification factor exactly 1 for every time step,
  i.e. no damping, while HLLE damps them under $\Delta t<\Delta y/c$ (§3.1, Eqs. (3.11)–(3.12));
  they hold this responsible for the [carbuncle](/definitions/carbuncle-phenomenon.md), and
  restore damping by multiplying both anti-diffusion terms by a smooth function of a
  transverse pressure-ratio sensor, without a tunable parameter and without a stricter CFL
  bound (§4.1, Eqs. (4.1)–(4.6)). They also write the flux as central part plus a dissipation
  term and lower that term further by a minimal-jump choice of the density in it
  ([BVD](/definitions/boundary-variation-diminishing.md); [HLL-family solvers](/methods/hll-riemann-solvers.md)).
- **Solver against mesh on turbulence.** [Bielawski et al. (2023)](/sources/bielawski-2023.md)
  (App. A, Figs. A.13–A.16; accepted manuscript) compare three convective fluxes in a
  second-order unstructured finite-volume code: a non-dissipative skew-symmetric central scheme,
  HLLC and AUSMDV. The test is decaying compressible isotropic turbulence
  ([compressible isotropic turbulence](/benchmarks/compressible-isotropic-turbulence.md)) on a
  structured $64^3$ mesh and a skewed tetrahedral mesh.
  - At initial turbulent Mach number $0.3$, the central scheme on the structured mesh tracks the
    spectral reference, HLLC is closer to it than AUSMDV, and AUSMDV "adds additional numerical
    dissipation even at the turbulent Mach number of 0.3". The unstructured meshes deviate more and
    show a small-scale energy pile-up.
  - At $0.6$, with eddy shocklets, both upwind fluxes are much more dissipative than the central
    scheme in enstrophy and dilatation, the HLLC–AUSMDV gap narrows, and mesh skewness has minimal
    influence compared with the scheme's own dissipation.

  The authors postulate that a hybrid central/HLLC scheme would be beneficial but do not run one.
- **A ranking of solvers.** [Lesur et al. (2023)](/sources/lesur-2023.md) (§2.3) order the
  Riemann solvers of IDEFIX "from most to least diffusive": Rusanov, HLL, HLLC (HLLD in MHD),
  Roe; on linear MHD waves with linear reconstruction all four are second order and within
  small factors of each other (§4.2, Fig. 7), and on double Mach reflection at $1920\times480$
  the least diffusive reconstructions (LimO3, PPM) give a more vigorous jet with the onset of
  Kelvin–Helmholtz rolls (§4.1, Fig. 3). Their Hall-effect treatment, a whistler speed added to
  the HLL fan for the magnetic fluxes only, is "known to be diffusive" but stable (§2.5). See
  [IDEFIX](/software/idefix.md).
- **Low Mach number.** Upwind numerical viscosity scales as $1/M$ at low Mach number, as
  recalled by [Boscarino, Qiu, Russo & Xiong (2022)](/sources/boscarino-2022.md) (§2), who split
  the acoustic part off implicitly and take the Lax–Friedrichs splitting speed from the material
  waves, $\max(\lvert v_1\rvert+\lvert v_2\rvert+\min(1,1/M)c)$ in their scaled variables
  (Eq. (3.32)); on the Gresho vortex at $M=10^{-1},10^{-2},10^{-6}$ the kinetic energy is "well
  maintained" over two periods, better by their third- than by their second-order scheme on
  $100^2$ (Ex. 5.5, Fig. 5.6). See [semi-implicit all-Mach schemes](/methods/semi-implicit-all-mach-scheme.md)
  and [Gresho vortex](/benchmarks/gresho-vortex.md).
- **Low Mach number by order, not by solver.** [Teissier et al. (2024)](/sources/teissier-2024.md)
  (§4.1, Table 2; arXiv v2) run a 3D MHD vortex advected at about Mach 0.1 for one period
  with Rusanov fluxes, whose dissipation $a[\![u]\!]$ is dominated by the fast
  magnetosonic speed. Their second-order scheme loses 99 % of the fluctuating kinetic plus
  magnetic energy on $64^3$ and 60 % on $256^3$, while the higher orders lose far less (e.g.
  $9.0\times10^{-3}$ at fourth order on $192^3$, $7.7\times10^{-3}$ at sixth order on
  $96^3$). They read raising the order, which shrinks the interface jump, as an
  alternative to low-Mach fixes of Roe or HLLD solvers. Their eighth-order scheme without
  the passage through point values ([cell-average–point-value conversion](/operators/cell-average-point-value-conversion.md))
  converges only at second order but keeps an energy loss close to the full scheme's,
  which they take as a hint that its errors are dispersive rather than dissipative.
  See [magnetized vortex](/benchmarks/magnetized-vortex.md).
- **Low Mach number by a solver correction.** [Wilfong et al. (2026)](/sources/wilfong-2026.md)
  (§4.2.4, Fig. 14) implement in [MFC](/software/mfc.md) two corrections of the HLLC flux,
  after Guillard & Viozat's account of the low-Mach accuracy loss. Let $v^\pm$ and $c^\pm$
  denote the normal velocities and sound speeds of the two interface states and
  $\mathsf z=\min\big(\max(\lvert v^-\rvert/c^-,\lvert v^+\rvert/c^+),1\big)$ a local Mach
  number (page-local). The Thornber et al. correction replaces the two velocities by
  $\tfrac12(v^-+v^+)+\tfrac{\mathsf z}2(v^--v^+)$ and $\tfrac12(v^-+v^+)+\tfrac{\mathsf z}2(v^+-v^-)$ in the signal speeds and fluxes, i.e. it scales
  the velocity jump by $\mathsf z$; the anti-dissipation pressure correction of Chen et al. adds
  $(\mathsf z-1)$ times a pressure-dissipation term built from the HLL speeds to the momentum and
  energy fluxes of the two star states. On the [Gresho vortex](/benchmarks/gresho-vortex.md) at
  reference Mach numbers $10^{-1}$ to $10^{-4}$ ($t/t_r=1$) the uncorrected HLLC loses accuracy,
  and both corrections preserve it "to visual accuracy for all tested Mach numbers"
  ([HLL-family solvers](/methods/hll-riemann-solvers.md)).
- **Galerkin as a central scheme.** The plain continuous-Galerkin discretization "is equivalent
  to central differencing" and oscillates at shocks; [Dao & Nazarov (2022)](/sources/dao-2022.md)
  (§4, §4.2–4.3, Eq. (4.10)) add a residual-based viscosity, the minimum of a first-order
  viscosity $\tfrac12h\lambda_{\max}$, which "can be shown" to give the first-order
  Lax–Friedrichs scheme in 1D, and a high-order one proportional to $h^2$ times the normalized
  PDE residual (page-local $h$ the mesh size, $\lambda_{\max}$ the local maximum speed). See
  [artificial viscosity](/methods/artificial-viscosity.md).

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

On a non-uniform three-cell stencil the same rule holds with grid-dependent constants: a
second-order linear operator is diffusive when its intercept and the normalised cell average lie
on the same side of the third-order intercept and of the abscissa of the accuracy point, and
anti-diffusive otherwise ([Deng, Jiang & Yan (2025)](/sources/deng-2025.md), Proposition 3,
Eq. (2.22); formulas on the [normalised-variable diagram](/definitions/normalised-variable-diagram.md)).
Their non-uniform ROUND curve is built to lie wholly in the dissipative region for
$0<\tilde u<1$ (§2.4; [ROUND](/methods/round-scheme.md)).

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
anti-dissipation (the sign convention of Fu 2023, used by all the sources
cited here). Measured this way:

- THINC with $\beta_{\mathrm T}=1.6$ is anti-diffusive in some wavenumber
  ranges, like Superbee ([Takagi et al. (2022)](/sources/takagi-2022.md), §2.3);
- WENO-Z+ with a large coefficient has a narrow band of negative dissipation
  near $\vartheta\approx1.18$ ([Luo & Wu (2021)](/sources/luo-2021-b.md), §3).

**Dissipation added by mesh interfaces.** [Wang et al. (2026)](/sources/wang-2026.md) (§4.4.1,
Fig. 5) extend the measure to a two-level AMR grid by a Bloch-wave analysis of the composite
semi-discrete operator of fifth-order finite-difference WENO with linear weights
([approximate dispersion relation](/definitions/approximate-dispersion-relation.md),
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)). With $\vartheta=k_w\Delta x_c$
on the coarse spacing, their convention $\lambda=-\mathrm i\tilde\vartheta$ makes
$\tilde\vartheta_i<0$ dissipative, as above. All three inter-level closures (cell-centred
Berger–Colella, cell-centred WENO prolongation and restriction, node-based WENO prolongation)
match the uniform-grid dissipation at low wavenumbers. All show excess dissipation from
$\vartheta\gtrsim2$, which the authors interpret as damping of interface-generated parasitic
modes. The WENO closure deviates least near the grid cut-off. In nonlinear runs the ranking
persists: on the [Shu–Osher problem](/benchmarks/shu-osher-problem.md) WENO-type transfers are less
dissipative in smooth regions than second-order Berger–Colella transfers (§6.3.3, Fig. 15). In
decaying [compressible isotropic turbulence](/benchmarks/compressible-isotropic-turbulence.md) at
$M_{t,0}=1.0$, Berger–Colella is the most dissipative, pure WENO interpolation the least (it fails
at $t\approx3.4\tau$ during coarsening), and the hybrid WENO interpolation's dissipation approaches
the WENO one (§6.4.3, Figs. 21–22).

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
([targeted ENO](/methods/targeted-eno.md)). [Ji, Liang & Fu (2022)](/sources/ji-2022.md) (§3.4, §6) put the
same point as the source of WENO dissipation: the smooth weighting of candidates
starts the nonlinear adaptation already at low wavenumbers, while TENO applies a
stencil optimally or discards it; on unstructured meshes they find TENO less
dissipative than CWENO and equal-order WENO at the same order (§5). The same contrast appears in
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

## Dissipation adapted to the local scale

Several sources make the dissipation of the linear background itself a function
of the local resolution.

- **Order traded for dissipation.** The six- and eight-point backgrounds of wide TENO are
  dissipation-optimized at fifth and sixth order instead of sixth and eighth, to damp spurious
  waves at marginally resolved wavenumbers ([Hong, Ye & Ye (2022)](/sources/hong-2022.md), §1,
  §5.1; see [targeted ENO](/methods/targeted-eno.md)).
- **A dissipation parameter set by a scale sensor.** In the MDCD flux of
  [Li, Chen & Ren (2022a)](/sources/li-2022.md) dissipation enters only through the parameter
  $c_{\mathrm{diss}}$ of the [approximate dispersion relation](/definitions/approximate-dispersion-relation.md)
  page. Their MDAD scheme sets it per interface, from $0.001$ where a
  [scale sensor](/definitions/scale-sensor.md) reports a reduced wavenumber of at most 1 (more
  than about six points per wavelength) to $0.012$ at the highest wavenumbers (§2.3, Eq. (38)). On the
  inviscid Taylor–Green vortex at $128^3$ the non-dissipative C6 and the nearly
  non-dissipative MDCD with $0.001$ blow up at $t=4$–$5$, UW5 and MDCD with $0.012$ run but
  dissipate more, and MDAD runs without tuning and best preserves the kinetic energy
  (§4.4.1, Figs. 27–28); at $\mathrm{Re}=1600$ on $256^3$ its enstrophy at $t=9$ is within 4.1%
  of DNS against 16.6% for UW5 and 10.4% for MDCD, at 19.3% more CPU time, and it reaches UW5's
  error with $168^3$ instead of $256^3$ points (§4.4.2, Tables 4–5). See
  [MDCD schemes](/methods/mdcd-scheme.md).
- **A cut-off set by a scale sensor.** [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md)
  (§1, §3.2) aim at low dissipation at low wavenumbers, comparatively high dissipation at high
  wavenumbers and enough at discontinuities by driving the TENO cut-off with an estimated
  wavenumber ([adaptive TENO](/methods/adaptive-teno.md)).
- **Linear and nonlinear dissipation switched together.** In the six-point
  [WCNS](/methods/weighted-compact-nonlinear-scheme.md) of
  [Zhou et al. (2023)](/sources/zhou-2023.md) (§§3–4) dissipation has two sources. The
  first is linear, a parameter $\xi_{\mathrm Z}$ (page-local, as on the WCNS and MDCD pages) of the interpolation that
  enters only the imaginary part of the modified wavenumber. The second is nonlinear, the
  additive constant $C$ of Wong–Lele-type weights, where a larger $C$ is closer to linear. A
  larger $\xi_{\mathrm Z}$ raises dissipation everywhere. A larger $C$ lowers it over the
  whole range and shifts it to higher wavenumbers. At fixed $C$ the dissipation grows
  non-monotonically with the wavenumber, which they attribute to the first-derivative term of
  the smoothness indicators (§4.2, Figs. 3, 6). Since a fixed $C$ or $\xi_{\mathrm Z}$ "(even though it
  takes an optimized value) cannot produce satisfactory dissipation property at the whole
  wavenumber range", WCNS-SA switches both by Li et al.'s second-derivative
  [scale sensor](/definitions/scale-sensor.md). It uses $C=2\times10^{10}$ and
  $\xi_{\mathrm Z}=0.0002$ in smooth, low-wavenumber regions, and $C=2\times10^8$ with
  $\xi_{\mathrm Z}$ rising to $0.028$ at high sensor values (§4.3, Eqs. (31)–(32), Table 3).
  *(Compiler check, not in the sources: $0.028$ exceeds the $3/128\approx0.0234$ of the
  fifth-order upwind interpolation, so at the highest sensor values the linear part is more
  dissipative than upwind-5.)* On the viscous Taylor–Green vortex only WCNS-SA matches
  Brachet's dissipation rate at $\mathrm{Re}=100$ on $32^3$ and at $200$ and $400$ on $64^3$.
  Inviscid on $64^3$, it preserves the kinetic energy better than ONL6 and WCNS-LD on $128^3$
  (§5.9, Figs. 21–24). Its extra cost is 3% over ONL6 (Table 4, 32 cores).
- **No dissipation where smooth, tuned dissipation where flagged.** The TENO-S hybrid
  of [Liang & Fu (2024b)](/sources/liang-2024-b.md) (§§3.1–3.3) uses, in points its
  TENO-type indicator declares smooth, an eight-point kinetic-energy-preserving
  skew-symmetric split-form flux, which has only a dispersive part and is "still
  non-dissipative". In flagged points it uses eight-point TENO whose background's
  dissipation is set separately by one coefficient, $b_0=0.01$, chosen from the Hu-type
  dispersion–dissipation ratio of the
  [approximate dispersion relation](/definitions/approximate-dispersion-relation.md), with a
  TENO-A cut-off between $10^{-7}$ and $10^{-10}$ ([adaptive TENO](/methods/adaptive-teno.md)).
  *(Compiler check, not in the sources: that background is the central scheme plus
  $\tfrac{b_0}{70\Delta x}$ times the eighth undivided difference.)* On the inviscid
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) on $64^3$ to $t=100$ it performs,
  in their words, "long-time stable computations without numerical dissipation by preserving the
  total kinetic energy", where WENO-CU6, TENO6 and TENO8 smear the small vortices after
  $t\approx5$ (§4.10, Figs. 17–18). The non-dissipative property they state is that of the
  smooth branch; the TENO branch is dissipative by design.
- **Only nonlinear dissipation, band by band.** The TENO6-SA of
  [Zhang et al. (2024b)](/sources/zhang-2024-b.md) (§3.2, §5) relays non-dissipative
  central and spectrally optimized dispersion schemes by wavenumber band and leaves all
  dissipation to the TENO cut-off, which it lowers band by band to $10^{-13}$ and raises
  again above the resolved range ([adaptive TENO](/methods/adaptive-teno.md)). Its
  approximate dispersion relation shows "no numerical dissipation in its resolvable region"
  and enough at moderate and high wavenumbers (§5.2, Fig. 5); in the Titarev–Toro problem a
  too-small cut-off in the low band creates pseudo-oscillations (Fig. 13).
- **Dissipation through a kernel shape.** In the Gaussian-RBF TENO of
  [Liang & Fu (2024a)](/sources/liang-2024.md) (§3.2) the shape parameter grows from 3 in
  smooth low-wavenumber regions to 6 at high-wavenumber content, driven by a smoothness
  measure; the nonlinear scheme has better dispersion and dissipation than TENO5 and
  WENO5-Z in the ADR and keeps total kinetic energy better on Kelvin–Helmholtz, where
  WENO5-Z is the most dissipative (§4.7, Figs. 3, 12(b)).
- **A widened cut-off range, overridden at immersed boundaries.** [Chen & Chen (2026)](/sources/chen-2026.md)
  (§2.3.2, §3.1, Fig. 8) treat the TENO cut-off $C_T$ as the dissipation control of a
  fifth-order finite-difference TENO with an [immersed boundary](/methods/immersed-boundary-method.md).
  Away from the body $C_T$ follows the nonlinear adaptation of Fu, Hu & Adams with parameters
  that give the range $[10^{-9},10^{-1}]$ ([adaptive TENO](/methods/adaptive-teno.md)); every
  interface whose stencil contains a ghost point takes the largest value $10^{-1}$, "to enhance
  dissipation near the immersed boundary". On a Mach 3 cylinder the
  [positivity-preserving flux limiter](/methods/positivity-preserving-flux-limiter.md) is then
  rarely activated; with $C_T\in[10^{-15},10^{-5}]$ (still $10^{-1}$ at the wall) its
  activations increase near the shock front, and with $C_T$ fixed at $10^{-14}$ they spread into
  the wake. The authors read this as resolution of high-wavenumber fluctuations bought with
  stability (Fig. 8, maps only, no counts).
- **Dissipation at a jump.** [Liang et al. (2022)](/sources/liang-2022.md) (§1, §3.2, Fig. 6)
  attribute residual dissipation of THINC at discontinuities to its cell-average constraint and
  replace it by point interpolation with two steepness levels in cells a TENO-flag detector marks
  ([TENO-THINC](/methods/teno-thinc.md), [THINC](/methods/thinc-reconstruction.md)).

## Doing without dissipation: consistency instead

[Jain & Moin (2022)](/sources/jain-2022.md) build a non-dissipative central
finite-volume scheme for the compressible two-phase
[five-equation model](/definitions/five-equation-model.md) with no upwinding and no
subgrid model, and obtain stability in under-resolved inviscid turbulence from
discrete consistency conditions instead: kinetic-energy and entropy preservation
of the split fluxes, plus an interface-equilibrium condition tying the internal-energy
flux to the mass and volume-fraction fluxes (§3, Theorems 3.1–3.2, Lemma 3.1). For a
density ratio 10 only the form that satisfies all conditions runs; the single-phase
kinetic-energy-preserving forms of Kennedy–Gruber/Kuya and Chandrashekar diverge, as do a
divergence-form mass flux and inconsistent momentum or kinetic-energy fluxes (§4, Figs. 4–8;
App. C–D). See [kinetic energy preservation](/properties/kinetic-energy-preservation.md) and
[split convective forms](/methods/split-convective-forms.md).

The linear analysis of [Crin-Barat & Manea (2026)](/sources/crinbarat-2026.md) (arXiv v2)
gives the semi-discrete counterpart for the central difference
$D_hv_i=(v_{i+1}-v_{i-1})/(2\Delta x)$ on an infinite grid (page-local $D_h$ and $\ell^2$ inner
product $\langle\cdot,\cdot\rangle$): it satisfies the discrete integration
by parts $\langle u,D_hv\rangle=-\langle D_hu,v\rangle$, hence $\langle u,D_hu\rangle=0$
(Proposition 3.5), and it is $\ell^2$-stable for every symmetric flux matrix, whereas the one-sided
differences are stable only for one sign of the matrix (Proposition 3.4). For their partially
dissipative linear relaxation systems $\partial_tu+A\partial_xu=-\mathsf Bu$, the semi-discrete
solution decays at the rate $(1+t)^{-1/2}$ with a constant independent of $\Delta x$ under the
Kalman rank condition (Theorem 2.1; $A$ symmetric, $\mathsf B$ the page-local symmetric damping matrix;
[asymptotic preservation](/properties/asymptotic-preservation.md)). *(Compiler check, not in the
sources: $\langle u,D_hu\rangle=0$ means the central semi-discretization adds no $\ell^2$
numerical dissipation, so the decay comes from the damping term $-\mathsf Bu$ alone.)*

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
  decay and entropy increase for all the author's splittings and avoids vortex-core deepening on a long
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
Eq. (33)); on the Taylor–Green vortex at Re 1600 on $64^3$ Edoh's rotational-form splitting shows
the larger $\epsilon_{\mathrm{num}}$ and density variability than the Kennedy–Gruber splitting,
attributed to aliasing, and the kinetic-energy-preserving splittings agree as the grid is refined
(Fig. 3).

**Upwind dissipation in LES of wall turbulence.**
[De Vanna et al. (2023a)](/sources/devanna-2023.md) vary only the convective scheme in 69 LES
of spatially developing boundary layers at Mach 2 and 5.86, all in one finite-difference
solver ([supersonic turbulent boundary layer](/benchmarks/supersonic-turbulent-boundary-layer.md)).
The schemes are WENO-Z 3/5/7, TENO5, TENO-A5 and a sixth-order kinetic-energy-preserving central
scheme, run pure or hybridized by a [Ducros sensor](/definitions/ducros-shock-sensor.md).

- **Wall-resolved, implicit LES** (§4.2, Figs. 1–2). The upwind schemes underestimate the wall
  friction, overestimate the log-layer velocity and give an augmented peak of turbulent kinetic
  energy. The errors shrink as the WENO order rises and from WENO to TENO, and the central scheme
  fits DNS. Adding the WALE model changes the friction only marginally.
- **Wall-modelled LES** (§4.3). The effect is stronger.
  - Pure upwind schemes damp or destroy wall turbulence. On the coarse grid the $Re_\tau$ range
    stays very narrow, and WENO-Z3 mispredicts the wall flow at every resolution.
  - On the fine grid the pure schemes overestimate the friction "dramatically".
  - Hybridization with the central scheme at Ducros threshold $\Psi^*=0.1$ brings the statistics near
    DNS. No pure WENO or TENO run collapses onto the central solution (§4.3.1, Figs. 4–8).
- **Proposed mechanisms** (§5). In wall-resolved LES, numerical viscosity damps the small scales
  and "freezes the Reynolds stress", and momentum balance then changes the mean wall velocity
  gradient. The authors compare this with polymer drag reduction. In wall-modelled LES the
  Reynolds stresses reach the wall shear stress only through the wall model
  ([wall-modelled LES](/methods/wall-modeled-les.md)), which sees the instantaneous velocity and
  temperature at the matching point and no fluctuation correlations. With predominant shock
  capturing or poor resolution, wall turbulence "can be wholly destroyed".
- **Subgrid model** (Appendix, Fig. 10). Smagorinsky deviates because its eddy viscosity does not
  vanish at the wall; WALE, Sigma and the mixed time-scale model give similar results.

In the same vein, Bielawski et al. (above) find that the dissipation of the upwind flux, not the
mesh skewness, dominates at shocklet-bearing turbulent Mach numbers.

In the opposite direction, [Wang et al. (2021)](/sources/wang-2021.md) motivate
their multi-resolution WENO by the observation, recalled from Johnsen et al.,
that WENO dissipation can overwhelm physical dissipation in turbulence (§1), and
find the new scheme the closest of four WENO schemes to the DNS kinetic-energy
history of the Taylor–Green vortex at $128^3$ (Example 5.13, Fig. 5.22).

## Measured from the decay of an exact wave or a proxy

[Berta et al. (2024)](/sources/berta-2024.md) (§5.3, Fig. 5; arXiv v4) measure the
dissipation of whole MHD schemes from the damping of an exact solution: for a circularly
polarized [Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md) in 3D, the decay
rate of $\big(\iiint B_3^2\,dx\,dy\,dz\big)^{1/2}$, read as
$\tfrac12(\nu_{\mathrm v}+\eta_{\mathrm m})k_w^2$ with an effective viscosity $\nu_{\mathrm v}$
and resistivity $\eta_{\mathrm m}$ and the wavenumber $k_w$ (page-local). Their fourth-order finite-volume scheme is more than an order of magnitude
less dissipative than the second-order one already at 8 points per direction, and the
gap widens: the rate scales as $N^{-5}$ against $N^{-3}$. On the
[field-loop advection](/benchmarks/field-loop-advection.md) the magnetic energy decays
considerably faster at second order than at third and fourth (Fig. 7), and on the
[Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) they use the normalized pressure
maximum $\max(p)/\langle p\rangle$ at the end of the run ($\langle p\rangle$ the average
pressure, page-local), which "generally increases with better resolution", as a proxy for the
decrease of numerical dissipation (§5.6).

**Numerical resistivity.** [Komissarov & Phillips (2024)](/sources/komissarov-2024.md) (§4.3,
Eqs. (87)–(95); arXiv v3) measure the dissipation of their third-order relativistic MHD scheme
as a resistivity, from the decay rate $\nu_{\mathrm d}=\eta_{\mathrm m}k_w^2$ of a degenerate Alfvén wave with the
telegraph equation of resistive MHD (page-local decay rate $\nu_{\mathrm d}$ and resistivity $\eta_{\mathrm m}$, as in the Berta et al. paragraph above). Accumulating a local
truncation error $\propto n_L^{-(\mathsf r+1)}$ ($n_L$ points per field length scale $L$, $\mathsf r$ the order, page-local)
over the resistive time $L^2/\eta_{\mathrm m}$ gives the ansatz

$$\eta_{\mathrm{num}}=A_\eta\,L\,\frac{\Delta x}{\Delta t}\Big(\frac{\Delta x}{L}\Big)^{\mathsf r},$$

with $L$ defined by $\partial_x^2B=B/L^2$ (page-local $\eta_{\mathrm{num}}$, $A_\eta$); the
authors call it heuristic. With $\mathsf r=3$ the measured $\eta_{\mathrm{num}}$ falls from
$4.9\times10^{-3}$ to $4.8\times10^{-6}$ for 10 to 80 points per wavelength (orders 3.75, 3.1, 3)
and $A_\eta\approx0.031$ from 40 points on (Table 3, Fig. 6). On a field at 45° to the grid the
resistivity is halved for the same $\lvert k_w\rvert$, modelled as $\tfrac14(3+\cos4\vartheta_{\mathrm g})\eta_0$
with $\vartheta_{\mathrm g}$ the angle to the grid (page-local; Eq. (98), Table 5). They use the
ansatz to set an effective Lundquist number in tearing-instability runs
([tearing-mode instability](/benchmarks/tearing-mode-instability.md)) and liken it to anomalous
resistivity, since $\eta_{\mathrm{num}}\propto L^{-2}$ (§6).

## Reading dissipation off 2D results

Without a closed-form measure, the 2D sources compare dissipation through flow
features that only dissipation suppresses: the curliness of the contact in the
explosion problem, which is physically unstable and "may be stabilized by the ND
only", and the distance travelled by the jet of the implosion problem
([Wang et al. (2023b)](/sources/wang-2023-b.md), Examples 6–7); Chertock et al.
present the explosion problem as a benchmark of the amount of ND and compare at
equal CPU time on the implosion (Examples 6–7). For the Kelvin–Helmholtz
problem, where solutions do not converge under refinement,
[Chertock et al. (2023)](/sources/chertock-2023.md) (Example 8, Fig. 5.9) find
different Cesàro averages for the original and the LCD central-upwind schemes
and read this as non-uniqueness of the limiting dissipative weak solution,
which "apparently depends on the choice of the numerical diffusion".

More vortices at the same grid are read the same way for multiphase schemes:
[Zhang et al. (2024a)](/sources/zhang-2024.md) (§4.6) attribute the clearer vortices and
stronger interface instabilities of their WENO5IS-THINC, against MUSCL-THINC, to lower
dissipation, and [Chen & Fu (2024)](/sources/chen-2024.md) (§9) the richer small scales of
their TENO-A limiter for spectral differences, against the WENO limiter, to the same cause;
lowering the TENO cut-off reduces the dissipation of their double Mach reflection (Fig. 13).

Resolution at reduced grid is a third: [Fan et al. (2023)](/sources/fan-2023.md)
(Ex. 3.13, Fig. 3.17) find their fifth-order Hermite WENO on $120\times480$ comparable to
WENO-ZQ on $240\times960$ for the Rayleigh–Taylor instability and read it as lower dissipation
of the compact stencils ([Hermite WENO](/methods/hermite-weno.md)). Two more proxies: [Chen et al. (2022)](/sources/chen-2022.md) (§6.7, Table 3)
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
  the 2D claims above rest on; none of these sources quantifies them.
- Sciacovelli et al. state $k_\varepsilon=\mathsf a_0/\mathsf a_P$, but their explicit members
  print the factors $1$, $\tfrac15$, $\tfrac3{70}$, $\tfrac1{105}$, which are
  $\lvert\mathsf a_P/\mathsf a_0\rvert$; and the sign $-\tfrac{\mathsf a_P}{2}$ of their general
  formula disagrees with the signs of the four explicit members (§3,
  Eqs. (23)–(35)). The page uses the explicit members. Their conclusion on
  dissipation order versus convective order is an ILES conclusion on one
  turbulence test; it is not stated for shocked flows.
- De Vanna et al. (2023a, §5, §6) word their mechanism in two directions. They
  say that numerical viscosity makes "the average wall velocity gradient ...
  increase with a consequent effect in terms of an effective drag reduction",
  while their §4.2 reports friction underestimated by the upwind schemes.
  *(Compiler check, not in the sources: a larger mean wall velocity gradient is
  a larger wall shear stress, so the printed sign of the explanation is
  opposite to the measured friction trend.)* The page records the measured
  trends. Their argument is qualitative and is not tested separately from the
  runs.
- Komissarov & Phillips (2024, Table 5) label a row "$2\eta k^2$" with $k=2\sqrt2\pi$ while
  their resistivity row equals that rate divided by $2(2\pi)^2$, the per-axis wavenumber, which
  is the reading their text adopts; they call the oblique and aligned resistivities "exactly the
  same" where the tables give $0.50\times10^{-2}$ and $0.49\times10^{-2}$ at 10 points. The paper
  also calls truncation error "rounding error" throughout.
- Chu et al. (2025a) judge dissipation from figures only; no error norms or timings are given.
- Bielawski et al.'s ranking comes from a second-order unstructured solver with
  limited reconstruction. Their §3 describes approximate Riemann solvers as
  giving "near minimal possible dissipation across discontinuities while
  maintaining a monotonicity preserving solution"; their own Appendix A finds
  both upwind fluxes much more dissipative than the central scheme at turbulent
  Mach number $0.6$.

# Citations

- [Liang & Fu (2024b)](/sources/liang-2024-b.md) — §§3.1–3.3, Eqs. (36)–(49); §4.10, Figs. 17–18: non-dissipative smooth branch, tuned TENO dissipation.
- [Berta et al. (2024)](/sources/berta-2024.md) — §5.3, Fig. 5; §5.4, Fig. 7; §5.6: Alfvén-wave damping, magnetic-energy decay, pressure-maximum proxy (arXiv v4).
- [Fu (2023)](/sources/fu-2023.md) — §3.6, Eq. (29): flux as central part plus jump term.
- [Wang et al. (2023b)](/sources/wang-2023-b.md) — §1, §3, Eqs. (5)–(18), Examples 6–7: CURH speeds, ND switch, ND proxies.
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
- [Hu, Yuan & Zhao (2022)](/sources/hu-2022.md) — §2.3, §3.1, §4.1–4.2, Eqs. (2.7)–(4.9): HLLEM anti-diffusion, undamped transverse perturbations, controlled anti-diffusion.
- [Lesur et al. (2023)](/sources/lesur-2023.md) — §2.3, §2.5, §4.1–4.2, Figs. 3, 7: solver ranking and diffusive Hall treatment (arXiv v1).
- [Boscarino et al. (2022)](/sources/boscarino-2022.md) — §2, Eq. (3.32), Ex. 5.5: low-Mach viscosity scaling, Gresho vortex (arXiv v2).
- [Dao & Nazarov (2022)](/sources/dao-2022.md) — §4, Eq. (4.10): Galerkin as central differencing, residual viscosity (arXiv v1).
- [Ji, Liang & Fu (2022)](/sources/ji-2022.md) — §3.4, §5, §6: WENO weighting dissipation, unstructured TENO (preprint).
- [Hong, Ye & Ye (2022)](/sources/hong-2022.md) — §1, §5.1: order traded for dissipation.
- [Li, Chen & Ren (2022a)](/sources/li-2022.md) — §2.3, Eq. (38); §4.4, Tables 4–5, Figs. 27–30: scale-adaptive dissipation and Taylor–Green evidence.
- [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) — §1, §3.2: wavenumber-adaptive cut-off (arXiv v1).
- [Liang et al. (2022)](/sources/liang-2022.md) — §1, §3.2, Fig. 6: dissipation of THINC's cell-average constraint.
- [Jain & Moin (2022)](/sources/jain-2022.md) — §3, Theorems 3.1–3.2, Lemma 3.1; §4, App. C–D: non-dissipative consistent two-phase scheme (arXiv v1).
- [Fan et al. (2023)](/sources/fan-2023.md) — Ex. 3.13, Fig. 3.17: Rayleigh–Taylor resolution as a dissipation proxy.
- [Bielawski et al. (2023)](/sources/bielawski-2023.md) — §3; App. A.1–A.2, Figs. A.13–A.16: central, HLLC and AUSMDV dissipation on isotropic turbulence, mesh skewness (accepted manuscript).
- [De Vanna et al. (2023a)](/sources/devanna-2023.md) — §§4.2–4.4, §5, §6, Appendix; Tables 1–4, Figs. 1–10: upwind dissipation in wall-resolved and wall-modelled LES.
- [Zhou et al. (2023)](/sources/zhou-2023.md) — §§3–4, Eqs. (31)–(32), Table 3, Figs. 3, 6–7; §5.9, Figs. 21–24, Table 4: linear and nonlinear dissipation switched by a sensor.
- [Teissier et al. (2024)](/sources/teissier-2024.md) — §4.1, Table 2: Rusanov dissipation at low Mach number reduced by order, dispersive errors without point values (arXiv v2).
- [Wakimura et al. (2024)](/sources/wakimura-2024.md) — §1, §3.2.1, Eq. (26): flux dissipation term and BVD motivation.
- [Zhang et al. (2024b)](/sources/zhang-2024-b.md) — §3.2, §5.2, Figs. 5, 13: nonlinear dissipation only, band-wise cut-offs.
- [Liang & Fu (2024a)](/sources/liang-2024.md) — §3.2, §4.7, Figs. 3, 12(b): adaptive kernel shape as dissipation control.
- [Zhang et al. (2024a)](/sources/zhang-2024.md) — §4.6: dissipation judged from vortex resolution.
- [Chen & Fu (2024)](/sources/chen-2024.md) — §9, Fig. 13: TENO-A against WENO limiters, effect of the cut-off.
- [Chu et al. (2025a)](/sources/chu-2025.md) — §2.1–2.2, Eq. (2.6); §4, Examples 1–6, Figs. 4.1–4.10: SBM limiter classes and adaptive overcompression (arXiv v1).
- [Deng, Jiang & Yan (2025)](/sources/deng-2025.md) — §2.2, Proposition 3, Eq. (2.22); §2.4: diffusion sign on non-uniform grids.
- [Komissarov & Phillips (2024)](/sources/komissarov-2024.md) — §4.3, Eqs. (87)–(95), Table 3, Fig. 6; §5.2, Eq. (98), Table 5; §6: numerical-resistivity ansatz and anisotropy (arXiv v3).
- [Huang et al. (2025b)](/sources/huang-2025-b.md) — §3.2, Eq. (18): boundary variation as the dissipation of the flux, kept by deepMTBVD.
- [Wilfong et al. (2026)](/sources/wilfong-2026.md) — §4.2.4, Fig. 14: Thornber and anti-dissipation pressure corrections of HLLC in MFC, Gresho vortex at low Mach number.
- [Chen & Chen (2026)](/sources/chen-2026.md) — §2.3.2, §3.1, Fig. 8: adaptive TENO cut-off range as dissipation control, $10^{-1}$ at ghost-point stencils, positivity-limiter activations.
- [Wang et al. (2023a)](/sources/wang-2023.md) — §3.1–3.2, Eqs. (17)–(21), Fig. 1; §4.3, Figs. 6, 8; Table 3: sensor-scaled LLF coefficient.
- [Wang et al. (2026)](/sources/wang-2026.md) — §4.4.1, Fig. 5; §6.3.3, Fig. 15; §6.4.3, Figs. 21–22: interface dissipation of AMR closures.
- [Crin-Barat & Manea (2026)](/sources/crinbarat-2026.md) — §3.3–3.4, Propositions 3.4–3.5; §2.1, Theorem 2.1: skew-adjoint central difference (arXiv v2).
