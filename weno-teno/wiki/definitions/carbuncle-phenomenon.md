---
type: Definition
title: "Carbuncle phenomenon"
description: "The carbuncle is a numerical instability that low-dissipation approximate Riemann solvers such as HLLC, HLLEM and Roe develop near strong shocks, in gas dynamics and in shallow water; a linear analysis traces it in HLLEM to undamped transverse perturbations, and the sources avoid it by HLL, flux-vector splitting, nodal multidimensional fluxes, extra shock dissipation or shock fitting."
status: established
aliases: [carbuncle problem, carbuncle instability, shock instability of low-dissipation Riemann solvers, odd-even decoupling, shock instability, carbuncle-like instability]
tags: [riemann-solver, numerical-flux, carbuncle, benchmark]
timestamp: 2026-10-23T11:06:00Z
---

# Carbuncle phenomenon

The **carbuncle phenomenon** is the numerical instability that some approximate Riemann
solvers develop in the vicinity of strong shock waves. Most sources of this bundle identify
it by the solvers that exhibit it and by the remedy; one, [Hu et al. (2022)](/sources/hu-2022.md),
analyses its mechanism (next section).
[Fu (2023)](/sources/fu-2023.md) (§3.6) states that "the HLLC and Roe solvers may induce
carbuncle problem in proximity to strong shockwaves with low numerical dissipation whereas
the HLL solver is free from carbuncle problem but featuring substantially larger
dissipation", and concludes that "there is no unique Riemann solver capable of handling all
Mach numbers". [Huang et al. (2026)](/sources/huang-2026.md) (§6.7) likewise state that "the
HLLC solver is known to exhibit numerical instabilities in the presence of strong shock
waves".

The defining trade-off is therefore between the resolution that a low-dissipation solver
gives to contacts and shear layers and the robustness that the more dissipative HLL solver
gives at strong shocks ([HLL-family solvers](/methods/hll-riemann-solvers.md),
[Roe solver](/methods/roe-riemann-solver.md),
[numerical dissipation](/definitions/numerical-dissipation.md)). Hu et al. (2022) (§1)
list Roe, HLLC and HLLEM as shock-unstable, all three resolving contacts and shear layers
sharply, and record two forms: the carbuncle at a blunt-body bow shock and the odd-even
decoupling of a grid-aligned moving shock (Quirk's channel test). [Ji et al. (2022)](/sources/ji-2022.md)
(§5) state that HLL is "free from Carbuncle problem and the necessity of entropy fix", without
a test.

## Mechanism in HLLEM: two linear analyses

Hu et al. (2022) (§3) diagnose the instability of HLLEM, i.e. HLLE plus anti-diffusion on the
entropy and shear waves, with two tools; $\sigma_x=\Delta t/\Delta x$, $\sigma_y=\Delta t/\Delta y$
and the mean state $(\rho_0,v_{1,0},0,p_0)$ with sound speed $c_0$ are page-local, $x$ is normal
to the shock ("streamwise"), $y$ along it ("transverse").

- **Saw-tooth perturbation analysis** (after Quirk, perturbing both directions; §3.1,
  Eqs. (3.1)–(3.12)). A perturbation alternating in sign from cell to cell is advanced by one
  forward-Euler step of the first-order scheme, giving an amplification matrix for
  $(\delta\rho,\delta v_1,\delta v_2,\delta p)$. Streamwise, HLLE and HLLEM are both damped for
  $\sigma_x<1/(c_0+v_{1,0})$ (subsonic) and coincide in the supersonic case. Transverse, HLLE has
  the matrix $(1-2\sigma_yc_0)I$, damped for $\sigma_y<1/c_0$, whereas HLLEM gives
  $\delta\rho^{n+1}=\delta\rho^n-\frac{2\sigma_y}{c_0}\delta p^n$, $\delta v_1^{n+1}=\delta v_1^n$,
  $\delta v_2^{n+1}=(1-2\sigma_yc_0)\delta v_2^n$, $\delta p^{n+1}=(1-2\sigma_yc_0)\delta p^n$: the
  spectral radius is 1 for every time step, because the density and the shear velocity are not
  damped. The authors conclude that "the non-attenuation of density and shear velocity
  perturbations in the transverse flux is directly responsible for the shock instability".
- **Matrix stability analysis** (after Dumbser, Moschetta and Gressier; §3.2, Eqs.
  (3.13)–(3.16)). The semi-discrete scheme is linearized about a steady Mach-8 shock on
  $30\times30$ cells (states from the
  [Rankine–Hugoniot](/definitions/rankine-hugoniot-condition.md) conditions) and perturbed by
  random noise of relative size $10^{-8}$; it is stable iff the stability matrix has no
  eigenvalue with positive real part. HLLE passes; HLLEM fails independently of the CFL
  number. Directional hybrids (HLLEM streamwise with HLLE, or with HLLE plus only the
  entropy-wave or only the shear-wave anti-diffusion, transverse) show that **both**
  anti-diffusion terms of the transverse flux must be controlled (Figs. 3.3–3.4); the
  stationary inclined-shock test confirms it (§5.7, Fig. 5.7).

The two analyses differ in mean state (uniform vs shocked), perturbation (saw-tooth vs
random) and locality, and Hu et al. require a shock-stable scheme to pass both (§3.3).

## Remedies used in the sources

- **Solver switching by smoothness.** The low-dissipation finite-volume TENO recalled by
  [Fu (2023)](/sources/fu-2023.md) (§3.6, Eq. (30)) uses a low-dissipation flux (HLLC, or the
  central flux for turbulence) where both full reconstruction stencils are flagged smooth by
  the TENO cut-off and the HLL flux otherwise, "to avoid the carbuncle problem while the HLLC
  flux [is] imposed for smooth flows to resolve the fine-scale structures"
  ([targeted ENO](/methods/targeted-eno.md)).
- **HLL for the strong-shock test case.** [Huang et al. (2026)](/sources/huang-2026.md)
  (§6.7) run their compact-stencil reconstructions with HLLC by default but switch to HLL for
  the Mach-10 [double Mach reflection](/benchmarks/double-mach-reflection.md) "to mitigate
  the carbuncle phenomenon".

- **HLL–HLLC hybrid switched by a shock sensor.** [Bai & Li (2022)](/sources/bai-2022.md)
  (§2.4, Eqs. (16)–(20)) replace the Lax–Friedrichs flux of an earlier DG cut-cell code by the
  HLLC–HLL solver of Kim et al. "to reduce the numerical dissipation" and "to avoid the shock
  instability which may meet in the vicinity of strong shock". The star states are blended,
  $\hat u^*_K=f\,u^*_K+(1-f)\,u^{\mathrm{HLL}}$, $K=L,R$, so $f=1$ is HLLC and $f=0$ HLL; $f$ is set
  by the pressure-jump indicator $f_p$ of the
  [Rankine–Hugoniot](/definitions/rankine-hugoniot-condition.md) page and the face-normal Mach
  numbers: "when the indicator function is equal to 1", $f=f_p$ if $M_L,M_R$ are both above or
  both below 1 and $f=0$ otherwise (Eq. (19)); $f$ where the indicator is 0 is not stated.
  *(compiler check, not in the sources: the Mach numbers are those of the face-normal
  velocities in the mesh frame (§2.4), so across a stationary shock aligned with the face the
  upstream one exceeds 1 and the downstream one is below 1, the "otherwise" branch applies and
  the face gets HLL, as the stated aim requires; at a detected moving shock both Mach numbers
  can lie on one side of 1, and Eq. (19) as printed then gives $f=f_p=1$, i.e. HLLC.)*
- **Switching the anti-diffusion off at shocks (RHLLEM).** Hu et al. (2022) (§4.1, Eqs.
  (4.1)–(4.6)) multiply both HLLEM anti-diffusion terms by a switching function
  $f_{\mathrm s}(h_{\mathrm p})$ (page-local), $f_{\mathrm s}=\tfrac12(1-\cos\pi h_{\mathrm p})$
  (recommended) or $h_{\mathrm p}^3$, of the pressure-ratio sensor
  $h_{\mathrm p}=\min_k\min(p^-_k/p^+_k,\ p^+_k/p^-_k)$ taken over the four transverse faces of the
  two cells adjacent to the face; $f_{\mathrm s}=1$ is HLLEM, $f_{\mathrm s}=0$ HLLE. The
  transverse amplification factors become $1-2\nu(1-f_{\mathrm s})$ for density and
  shear velocity and $1-2\nu$ for the others ($\nu=\sigma_yc_0$, a linearized CFL number),
  stable for $0<\nu<\min(1,1/(1-f_{\mathrm s}))$, so no extra time-step restriction;
  the matrix analysis gives a largest real part $-0.6963$ (Fig. 4.2). The authors contrast the
  scheme with Park and Kwon's HLLE+, whose empirical parameter they find fails at $0.01$ and is
  "still undesirable" at $0.1$ on the Elling test, and with an abrupt HLLC-to-HLL switch of Kim
  et al. ([HLL-family solvers](/methods/hll-riemann-solvers.md)).
- **Flux-vector splitting.** [Hong et al. (2022)](/sources/hong-2022.md) use the Roe flux by
  default but van Leer flux-vector splitting for the double Mach reflection and the 2D Riemann
  problems (§5). [Chen et al. (2022)](/sources/chen-2022.md) (§2) compute all
  shocked cases with van Leer flux-vector splitting because it is "robust in shock-capturing
  computations", so that "we are able to exclude the numerical shock instabilities caused by
  numerical fluxes", citing the matrix stability analysis of the carbuncle by Dumbser,
  Moschetta and Gressier; HLLC is reserved for shock-free runs.
- **HLL for relativistic jets.** [Chen & Wu (2022)](/sources/chen-2022-b.md) (Ex. 4.12) report
  "no carbuncle" in their third-order finite-volume WENO run of an axisymmetric relativistic
  jet with the HLL flux on triangles, relativistic Mach number about 41.95
  ([high-Mach jets](/benchmarks/high-mach-astrophysical-jet.md)).
- **Fitting the shock instead of capturing it.** In the moving discontinuous
  Galerkin method MDG+ICE of [Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md)
  the bow shock is a mesh face located by the weakly enforced interface
  ([Rankine–Hugoniot](/definitions/rankine-hugoniot-condition.md)) condition,
  and the interior flux is the plain central average, with no Riemann solver.
  On the steady Mach 8 (315 elements) and Mach 15 (497 elements) flows past a
  half cylinder, computed with linear elements, the authors observe "no shock
  instabilities or carbuncle phenomenon" (§IV.E, Fig. 28). The evidence is the
  figure alone; no shock-capturing comparison is run. See
  [implicit shock tracking](/methods/implicit-shock-tracking.md).
- **A nodal, multidimensional flux.** [Del Grosso et al. (2024)](/sources/delgrosso-2024.md)
  replace the face-based two-point flux of a first-order finite-volume scheme on polygonal
  grids by subface fluxes that depend on all cells around a mesh node (next section); the
  two-point version of the same solver, which they call "a classical HLLC-like two-point flux
  FV scheme, even if with different wave speeds' definition" (§6), shows the carbuncle and the
  nodal one does not (§5.6–5.8).
- **More dissipation at the shock, in DG with subcell limiting.** For the entropy-limited
  [DGSEM](/methods/dgsem.md) of [Lin & Chan (2024)](/sources/lin-2024.md) the cure is to keep
  enough low-order dissipation near shocks (section below).

## A multidimensional-aware scheme: nodal fluxes in shallow water

Del Grosso et al. (2024) (HAL preprint) report the carbuncle outside gas dynamics, for the 2D
[shallow-water equations](/definitions/shallow-water-equations.md) with topography (§1,
§5.6–5.8), and invoke the hypothesis, attributed to Fleischmann et al., that the carbuncle has a
multidimensional nature, so that schemes built from 1D solvers face by face are prone to it and
a "multi-dimensional-aware" scheme "should be insensitive" (§1). Their construction, with
page-local symbols (water depth $h$, velocity $v$, bottom $b$, $p=\tfrac12gh^2$, unit normal
$n_f$ and length $l_f$ of a subface $f$ at a node):

- **Simple solver in Lagrangian coordinates** (§3.3, after Gallice). Across each subface a
  three-wave, four-state approximate Riemann solver is written in mass coordinates, with
  outer wave speeds $\mathsf Z^-,\mathsf Z^+>0$ (page-local, of the dimension of a mass flux,
  approximating the acoustic impedances $h\sqrt{gh}$) and a free intermediate normal velocity
  $v^*_n$. Its jump conditions make the jump of the intermediate pressures, source included,
  equal to $(\mathsf Z^-+\mathsf Z^+)(v^*_n-v^{\mathrm G}_n)$, with the Godunov acoustic
  velocity
  $$v^{\mathrm G}_n=\frac{\mathsf Z^-v^-_n+\mathsf Z^+v^+_n}{\mathsf Z^-+\mathsf Z^+}-\frac{p^+-p^-+\overline{gh\Delta b}}{\mathsf Z^-+\mathsf Z^+},\qquad \overline{gh\Delta b}=g\,\frac{h^-+h^+}2\,(b^+-b^-)$$
  (page-local; Eqs. (29)–(30), (34)), then mapped to Eulerian coordinates (§3.6). The choice
  $v^*_n=v^{\mathrm G}_n$ gives the classical face-based, conservative "two-point" scheme.
- **Nodal solver** (§3.4, from cell-centred Lagrangian hydrodynamics of Maire and of
  Després–Mazeran). Instead, every subface impinging on node $\mathsf p$ takes
  $v^*_{n,f}=v_{\mathsf p}\cdot n_f$ for one nodal velocity $v_{\mathsf p}$ (page-local),
  fixed by a node-based consistency condition, i.e. the $2\times2$ linear system
  $$\Big[\sum_fl_f(\mathsf Z^-_f+\mathsf Z^+_f)\,n_f\otimes n_f\Big]v_{\mathsf p}=\sum_fl_f(\mathsf Z^-_f+\mathsf Z^+_f)\,v^{\mathrm G}_{n,f}\,n_f$$
  (Eq. (33)), stated to be always uniquely solvable (no proof printed). Each subface flux then
  depends on all cells around the node ("multi-point" scheme), and conservation holds by a sum
  around each node rather than by cancellation across each face (§4.3;
  [local conservation](/results/local-conservation-flux-form.md)).
- **The difference from the two-point flux** is a correction of the normal-momentum
  component proportional to $\tfrac12(\mathsf Z^-+\mathsf Z^+)(v_{\mathsf p}\cdot n_f-v^{\mathrm G}_{n,f})$ (Eq. (47)),
  which vanishes when $v_{\mathsf p}\cdot n_f=v^{\mathrm G}_{n,f}$, e.g. at the lake at rest.

The first-order multi-point scheme is proved positive under an explicit time-step condition,
node-wise conservative, entropy stable under lower bounds on $\mathsf Z^\pm$ and well-balanced for
the lake at rest (§4.2–4.5; [well-balancing](/properties/well-balancing.md),
[entropy stability](/properties/entropy-stability.md)); the wave-speed conditions are implicit in
$v^*_n$ and are met by iteration (Remark 1). A second-order version uses limited least-squares
slopes and two-stage Runge–Kutta (§4.6).

**Evidence** ($g=9.81$ unless stated; CFL 0.5 at first and 0.25 at second order; §5.6–5.8):

| Test | Setup as printed | Finding |
|---|---|---|
| colliding flow | $[-2.5,2.5]^2$, $g=1$, $h=1$, $v_1=30$ for $x\le0$ and $-30$ otherwise, random perturbation of size $10^{-5}$, $50\times50$ quadrangles, $t=2$ (§5.6, Fig. 14) | carbuncle with the two-point scheme; the multi-point solution stays symmetric |
| odd-even decoupling (Quirk-type) | moving shock in an $800\times20$ m canal with a bump, $800\times20$ quadrangles, $10^{-3}$ perturbation on the central grid line, $t=20$ and $30$ s (§5.7, Figs. 15–16) | instabilities with the first-order two-point scheme, none with the first- and second-order multi-point ones |
| [flow past a cylinder](/benchmarks/flow-past-circular-cylinder.md) | Froude-5 inflow, cylinder radius $0.5$ m, 81272 triangles (§5.8, Fig. 17) | carbuncle with the two-point scheme, none with the multi-point scheme at first or second order |

The authors also report the two-point scheme "slightly less diffusive" than the multi-point one
on a radial dam break, as earlier work found for the Euler equations (§5.3).

## DG with subcell limiting: a dissipation threshold

Lin & Chan (2024) (§4.4, Figs. 6–7, A.8) run the Mach-2000
[astrophysical jet](/benchmarks/high-mach-astrophysical-jet.md) ($N=3$, $150\times150$
elements, $T=0.001$) with subcell-limited DGSEM in which a linear program chooses the
blending factors so that a semi-discrete cell entropy inequality holds
([subcell limiting](/methods/subcell-finite-volume-limiting.md)). A shock-capturing variant
tightens the entropy bound by a fraction $\beta_{\mathrm e}\epsilon_K$ of the
low-order entropy dissipation (page-local: $\beta_{\mathrm e}\in[0,1]$ user-chosen,
$\epsilon_K$ the elementwise modal smoothness factor; Eq. (49)). With
$\beta_{\mathrm e}=1.0,0.1,0.01,0$ finer features appear as $\beta_{\mathrm e}$ decreases, but
carbuncles appear at $\beta_{\mathrm e}=0.01$ and $0$, and also with a local minimum entropy
principle; an elementwise Zhang–Shu-limited entropy-stable DG run shows none, which the authors
partly explain by that limiter being more dissipative. They conclude that "the carbuncle effect
is not due only to a loss of entropy stability, but rather a lack of sufficient dissipation near
shocks", and that the solution is highly sensitive to $\beta_{\mathrm e}$.

## Test problems

Hu et al. (2022) (§5, second-order MUSCL and second-order TVD Runge–Kutta, comparisons with
HLLE, HLLEM and HLLC) use six shock-instability tests:

| Test | Setup as printed | Finding |
|---|---|---|
| stationary inclined shock | ablations of RHLLEM (§5.7) | HLLEM, and switches on only one anti-diffusion term, unstable |
| Elling's test | shock–vortex-filament case with a **physical** carbuncle (§5.8) | HLLC and HLLEM show the physical carbuncle but oscillate along the shock; HLLE is stable but misses it; RHLLEM-LD gives both an oscillation-free shock and the physical carbuncle; the $h_{\mathrm p}^3$ switch misses it |
| [Sedov blast wave](/benchmarks/sedov-blast-wave.md) | $960\times960$ (§5.9) | HLLC, HLLEM unstable |
| Quirk's moving shock | Mach 8, $1500\times20$, $t=100$ (§5.10, Fig. 5.11) | odd-even decoupling for HLLC, HLLEM |
| [forward-facing step](/benchmarks/forward-facing-step.md) | $720\times240$, $t=4$ (§5.11) | HLLC, HLLEM unstable |
| [shock diffraction](/benchmarks/shock-diffraction.md) | Mach 5.09, $400\times400$, $t=0.15$ (§5.12) | HLLC, HLLEM unstable |

In the last four the authors report instabilities for HLLC and HLLEM, "especially the latter",
and none for RHLLEM-LD (§5.9–5.12). The Elling test makes the point that a cure must not suppress a physically
justified carbuncle by excess dissipation.

## The reconstruction matters too

With the flux held fixed, [Chen et al. (2022)](/sources/chen-2022.md) (§6.5, Fig. 22) find
"kinked Mach stems" in the Mach-10 [double Mach reflection](/benchmarks/double-mach-reflection.md)
on 576,910 triangles for the cell-based weighted-least-squares gradients with the MLP-pw slope
limiter, "especially significant" with the common-vertex stencil, citing for the kinked stem
Kim et al.'s paper on cures for the shock instability of the Roe scheme. Their vertex-based
gradient with nonlinear weights, on the same common-vertex stencil and with the same van Leer
flux, shows "no numerical abnormality". Since the flux is the same in all runs, the abnormality
is ascribed to the reconstruction and limiter (see
[unstructured gradient reconstruction](/methods/unstructured-gradient-reconstruction.md)). The
paper does not call the kinked stem a carbuncle.

## Qualifications

- Hu et al.'s analyses are linear and of the first-order HLLEM flux; that the undamped
  transverse density and shear perturbations cause the instability is their inference,
  supported by the matrix analysis and the hybrid experiments. They cite earlier work for the
  claims that added shear viscosity alone cannot always remove the carbuncle and that rotated
  solvers cost two flux evaluations per face (§1). Fu (2023) cites a dedicated reference for it and, among its references,
  a rotated-hybrid carbuncle-free Riemann solver (Nishikawa & Kitamura), which the review
  mis-cites as the Rusanov solver (§3.6).
- Luo, Absillis & Nourgaliev's Fig. 28 caption gives Mach 8 and 18, the text Mach 8 and 15;
  the page follows the text.
- **Two readings of the cause.** Del Grosso et al. (2024) cite the multidimensional nature
  of the carbuncle as their motivation (§1); Lin & Chan (2024) read their jet runs as a lack of
  shock dissipation rather than a loss of entropy stability (§4.4). The statements concern
  different schemes and are not incompatible. Each rests on a few tests: three for Del Grosso
  et al., one for Lin & Chan. Del Grosso et al. report their two-point scheme as slightly less
  diffusive than the multi-point one (§5.3) and run no other two-point solver against the
  multi-point one.
- Del Grosso et al. attribute the colliding-flow test to two different references (§5 and
  §5.6), print the random perturbation as $\delta(2z-1)$ with $z\in[-1,1]$ *(compiler check, not
  in the sources: this ranges over $[-3\delta,\delta]$, whereas $z\in[0,1]$ would give
  $[-\delta,\delta]$)*, and give the canal inflow of the
  odd-even test as $u_{\mathrm{in}}=13.283$ in m²/s, the unit of a discharge.

# Citations

- [Hu et al. (2022)](/sources/hu-2022.md) — §1, §3.1 (Eqs. (3.1)–(3.12)), §3.2 (Eqs. (3.13)–(3.18), Figs. 3.1–3.4), §3.3, §4.1 (Eqs. (4.1)–(4.6), Fig. 4.2), §5.7–5.12 (Figs. 5.7–5.13).
- [Ji et al. (2022)](/sources/ji-2022.md) — §5.
- [Hong et al. (2022)](/sources/hong-2022.md) — §5.
- [Fu (2023)](/sources/fu-2023.md) — §3.6 (Eq. (30), Fig. 9).
- [Huang et al. (2026)](/sources/huang-2026.md) — §6.7 (Fig. 12).
- [Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md) — §3.3, §IV.E (Fig. 28; author manuscript).
- [Bai & Li (2022)](/sources/bai-2022.md) — §2.4 (Eqs. (16)–(20)).
- [Chen et al. (2022)](/sources/chen-2022.md) — §2, §6.5 (Fig. 22).
- [Chen & Wu (2022)](/sources/chen-2022-b.md) — Ex. 4.12 (Fig. 18) (arXiv v1).
- [Del Grosso et al. (2024)](/sources/delgrosso-2024.md) — §1, §3.3–3.6 (Eqs. (29)–(34)), §4.1–4.6 (Eqs. (33), (47)), §5.3, §5.6–5.8 (Figs. 14–17), §6 (HAL preprint).
- [Lin & Chan (2024)](/sources/lin-2024.md) — §3.3 (Eq. (49)), §4.4 (Figs. 6–7, A.8).
