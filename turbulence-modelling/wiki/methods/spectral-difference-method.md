---
type: Method
title: "Spectral difference method"
description: "The spectral difference method is a nodal high-order element scheme that interpolates the solution on N+1 points and the flux on N+2 points per direction, made continuous by Riemann fluxes; this page covers its formulation, its place in the flux-reconstruction family, its fully-discrete dispersion–dissipation behaviour, and its DNS and implicit-LES uses."
status: established
aliases: [SD, SD method, spectral difference, staggered-grid Chebyshev multidomain method]
tags: [flux-reconstruction, dns, compressible, immersed-boundary, implicit-les, numerical-dissipation]
timestamp: 2026-10-28T02:13:00Z
---

# Spectral difference method

The **spectral difference (SD) method** discretizes a conservation law
$\partial_tU+\nabla\cdot(F^c(U)-F^v(U,\nabla U))=0$ in its differential form
on tensor-product cells. In each cell the solution is a nodal polynomial of
degree $N$ on $N+1$ **solution points** per direction, and the flux a
polynomial of degree $N+1$ on a staggered set of $N+2$ **flux points** per
direction, two of which lie on the cell faces. The face values of the
flux are replaced by a common value from an approximate Riemann solver,
which makes the flux continuous across cells, and the derivative of the flux
polynomial at the solution points advances the solution
([D'Ayer et al. 2026](/sources/dayer-2026.md), §2.2, Eqs. 6–10, citing
Kopriva & Kolias, Kopriva, Liu, Vinokur & Wang, and Wang et al.). Within the
energy-stable [flux-reconstruction](/methods/flux-reconstruction.md) family
a particular value of the correction parameter, $c_{\mathrm{SD}}$, "recover[s]
the stable spectral difference (SD) scheme"
([Brillon & Nadarajah 2026](/sources/brillon-2026.md), §1, §3.1.5, citing
Allaneau & Jameson). Three scale-resolving uses appear in the
sources: the compressible DNS solver JAGUAR with an immersed boundary
(D'Ayer et al. 2026), the shock-capturing code SD3DvisP in a
supersonic Taylor–Green comparison
([Chapelier et al. 2024](/sources/chapelier-2024.md)), and a DNS of a
supersonic compression/expansion ramp with bulk artificial viscosity
([Tonicello et al. 2022](/sources/tonicello-2022.md)).

Page-local symbols: $\xi_i^{\mathrm{sp}}$ and $\xi_k^{\mathrm{fp}}$ the
solution and flux points of the reference cell; $\ell_i$ the Lagrange
basis on the solution points; $h$ the cell length (registry); $q$ a scalar
model unknown and $f(q)$ its flux.

## Formulation

**One dimension** (D'Ayer et al. 2026, §2.2). For the model equation
$\partial_tq+\partial_xf(q)=0$ on cells of length $h$, each cell is mapped to
a reference cell (the source's is $[0,1]$), where
$\partial_tq+h^{-1}\partial_\xi f(q)=0$ (Eq. 7), so that a single Lagrange
basis serves all cells of the same degree. The solution is
$$q(\xi,t)\approx\sum_{i=1}^{N+1}\ell_i(\xi)\,q_i(t),\qquad \ell_i(\xi)=\prod_{j\ne i}\frac{\xi-\xi_j^{\mathrm{sp}}}{\xi_i^{\mathrm{sp}}-\xi_j^{\mathrm{sp}}}$$
(Eqs. 8–9). One step of the operator:

1. evaluate the solution polynomial at the $N+2$ flux points;
2. at the two face flux points, replace the flux by the solution of a
   Riemann problem with the neighbouring cell (D'Ayer et al. use Roe's
   approximate solver), "thus" restoring the conservativity that the
   cell-wise flux polynomials would break;
3. build the degree-$N+1$ flux polynomial from the corrected face values and
   the interior values;
4. differentiate it at the solution points.

**Node choice and stability.** D'Ayer et al. place the solution points at
the Chebyshev nodes of the first kind and the interior flux points at
Legendre–Gauss points; they state that the choice of interior flux points
is "critical to the stability" and that Legendre–Gauss points make the
one-dimensional SD scheme "linearly stable for any degree" (§2.2, citing
Van den Abeele, Lacor & Wang for the first statement and Jameson's
stability proof for the second). Linear and non-linear stability and the
dissipation and dispersion properties of the method are cited as
established (§1). [Liu & Yuan (2023)](/sources/liu-2023-b.md), §1, cite
the same result in its energy form: Jameson proved the SD schemes energy
stable for one-dimensional linear advection "by using energy estimates and
a norm of Sobolev type", and Vincent et al. used the same technique to
identify the energy-stable flux-reconstruction family; Liu & Yuan list nodal
DG and SD among the methods that flux reconstruction casts in one
framework, as do [Shi & Yan (2023)](/sources/shi-2023.md), §I, who add that
numerical tests support DG, SD and FR/CPR as dissipative methods for
[implicit LES](/definitions/implicit-les.md) without an explicit subgrid
model.

**Several dimensions.** On quadrilaterals and hexahedra the
one-dimensional procedure is repeated direction by direction with tensor
products of the one-dimensional bases (Eq. 10); each direction has its own
staggered flux points (Fig. 1). Viscous fluxes need the solution gradient,
which JAGUAR computes with the first Bassi–Rebay scheme (BR1, §2.2). The
same solver handles triangles and tetrahedra through Raviart–Thomas flux
spaces, not used in that paper (§2.2).

**Cost against FR.** D'Ayer et al. (2026, §1) cite earlier work that
found the computing time of SD "equivalent" to that of flux reconstruction
under favourable conditions and slightly higher in some circumstances.

## Spectral difference as a DNS solver with an immersed boundary

D'Ayer et al. (2026) implement a volume-penalization (Brinkman)
[immersed boundary method](/methods/immersed-boundary-method.md) in JAGUAR,
the CERFACS–ONERA compressible SD solver, to produce
[DNS](/definitions/direct-numerical-simulation.md) databases of
turbulent flow over rough, heated walls for the development of roughness
closures (§1, §4). The scheme runs with the five-stage fourth-order
strong-stability-preserving Runge–Kutta scheme of Spiteri and Ruuth; the
stiff penalization source is split off by Strang splitting and integrated
analytically, so that the time step stays set by the CFL condition with
the permeability fixed at $10^{-10}$ s (§2.4). The penalization and its
splitting are on the immersed-boundary page. Results relevant to the
discretization:

- **Laminar cylinder** ($Re_D=40$, $M=0.2$, $N=2$; §3.1, Tables 1–2;
  [circular-cylinder wake](/benchmarks/circular-cylinder-wake.md)): wake
  length over diameter 2.25 with the immersed boundary against 2.27 with a
  body-fitted SD mesh, separation angle 52.1° against 52.2°, drag
  coefficient 1.54 against 1.55, the differences "less than 1%"; the wall
  vorticity oscillates near the immersed surface, which the authors
  attribute to cells crossed by the solid mask, where a polynomial of any
  degree cannot represent the discontinuous solution (a Runge phenomenon).
- **Rough-wall minimal channel** ($Re_\tau=400$, staggered hemispheres,
  $N=3$; §3.2, Table 3; [turbulent channel flow](/benchmarks/turbulent-channel-flow.md)):
  the body-fitted SD DNS uses 17 million degrees of freedom with
  $\Delta x^+=2.04$, $\Delta z^+=1.11$ and a first wall-normal spacing
  $\Delta y^+=0.92$, the immersed-boundary SD DNS 25 million with $1.73$,
  $1.50$ and $0.51$; mean velocity and temperature agree with a body-fitted
  run, a finite-volume run and the reference DNS below the minimal-channel
  critical height, and the second moments differ by at most about 5%.

The authors conclude that SD with volume penalization is "suitable to
elaborate accurate DNS database of turbulent flows over rough surfaces"
and name automatic $hp$-refinement near the interface as future work (§4).

## Spectral difference as a DNS solver for a shock/boundary-layer interaction

[Tonicello et al. (2022)](/sources/tonicello-2022.md) run a DNS of a
Mach 2.91 turbulent boundary layer ($Re_\theta=2900$, $\delta^+=340$) over a
$24^\circ$ compression ramp followed by an expansion corner, at the
conditions of the DNS of Priebe & Martín, with an SD solver that
originates in Jameson's Stanford group; they state that it is, to their
knowledge, the first spectral-element simulation of this interaction (§2,
acknowledgements). Their formulation (App. A, Eqs. A1–A14) is the one
above, written with the source's $N$ as the order: in registry notation
the polynomial degree is $N=5$, with 6 solution points at Gauss–Legendre
nodes and 7 flux points (the Gauss–Legendre nodes plus the two end
points, "to ensure linear stability", citing Jameson). Curved elements
are mapped by $Q=\det(J)\,U$ and contravariant fluxes (Eq. A8). The
discretization and its resolution (§2, Table 2):

- $(120+120+120)\times28\times27$ elements, first solution point at
  $y^+\approx0.3$, $\Delta x^+=4.75$–15, $\Delta y^+=0.3$–9,
  $\Delta z^+=4.2$ (spacings are the element length over the number of
  solution points), and an effective spacing at most about six
  a-posteriori Kolmogorov lengths downstream of the shock;
- shocks regularized by a bulk
  [artificial viscosity](/methods/artificial-viscosity-shock-capturing.md)
  driven by a characteristic-based modal sensor and multiplied by a
  Ducros-type factor that is non-zero only in compression and switches the
  viscosity off at walls and in vortical regions (Eq. 2.10; see
  [shock sensor](/definitions/shock-sensor.md)); "direct numerical
  simulation" refers to the turbulent scales, the shocks staying
  under-resolved (§2.2);
- a Zhang–Shu positivity-preserving limiter adapted to SD, applied at
  solution and flux points at every Runge–Kutta stage, whose averaged
  activation flag peaks at about $10^{-4}$ (App. C, Fig. 13);
- the explicit differential filters of the a priori analysis are solved
  with the same SD scheme (§4.2).

The kinetic-energy budget closes to nearly zero at $y^+\approx30$, which
the authors read as negligible numerical dissipation, and the
artificial-viscosity term is small against the others (§4.1, Figs. 17–18);
the spectra show no pile-up at the grid Nyquist wavenumber (§3.2). The
validation and the energy-transfer analysis are on
[shock/turbulent boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
and [energy backscatter](/definitions/energy-backscatter.md).

## Spectral difference with artificial viscosity in shock–turbulence flow

In the seven-code comparison of Chapelier et al. (2024) on the supersonic
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) ($Re=1600$,
$M_0=1.25$, no subgrid model, coarse runs treated as
[implicit LES](/definitions/implicit-les.md)), the SD code SD3DvisP
(Jameson's Stanford group) runs at fourth order, $N=3$, on unstructured
hexahedra, $16^3$ to $128^3$ elements for $64^3$ to $512^3$ degrees of
freedom (§III.B.e, Table II). Its ingredients: a Roe interface flux with the
first Harten–Hyman entropy fix, the centred viscous flux of Sun, Wang and
Liu, third-order TVD Runge–Kutta, and a subcell
[artificial viscosity](/methods/artificial-viscosity-shock-capturing.md)
driven by a sensor on the density modes, with self-calibrated ramp and
threshold, amplitude 0.5 instead of 1 "to avoid too strong CFL
restrictions", made $C^0$-continuous by averaging at mesh vertices and
trilinear interpolation, plus positivity preservation. Findings (§IV, §V):

- at $64^3$ it under-predicts the early kinetic energy, as do the other
  Riemann-flux codes, attributed to the
  [numerical dissipation](/properties/numerical-dissipation.md) of the
  interface flux (Fig. 5);
- its dilatational dissipation is among the lowest on all grids, the mark
  of strong shock capturing, and its Mach-number profiles show thick,
  oscillation-free shocks (Figs. 6, 8);
- its solenoidal dissipation is high on the coarse grid and in the lower
  range on finer grids; the authors write that its "strong shock capturing
  strategy is probably hindering" the small scales there (§IV.A, Fig. 7);
- with the DG and DGSEM codes it belongs to the element methods that
  "capture small scales well on coarse grids" (§V).

## Fully-discrete dispersion and dissipation of SD

[Tonicello et al. (2023)](/sources/tonicello-2023.md) extend the spatial
[eigensolution analysis](/methods/eigensolution-analysis.md) of high-order
element methods (a real frequency is prescribed and complex numerical
wavenumbers are sought, as for inflow–outflow problems) from the
semi-discrete setting to the fully-discrete one with explicit Runge–Kutta
time integration, for the SD and DG members of the
[flux-reconstruction](/methods/flux-reconstruction.md) family applied to
one-dimensional linear advection with an upwind-parameterized interface
flux. They then test the predictions with the "improved" SD method of
Liang et al. and Jameson (the Stanford SD solver, Roe flux). Findings that
concern SD itself (the general theory is on the eigensolution page):

- **SD against DG.** With upwind fluxes, FR-SD has a less restrictive CFL
  limit than FR-DG and is spatially more dissipative; the SD dissipation
  curves are "moderately shifted up … and to the left" of the DG ones
  (§3, Fig. 7; App., Figs. 29–30), consistent with earlier semi-discrete
  analyses they cite.
- **Superconvergence and the time scheme.** For fifth-order FR-SD
  ($N=4$) the expected spatial superconvergence of order $2N+1=9$ is
  preserved only in an intermediate range of wavenumbers and frequencies;
  at small ones the three-stage RK33 reduces the convergence to fourth
  order, and smaller time steps extend the order-9 range downward (§3,
  Fig. 8).
- **Time step against dissipation.** For SD with the upwind flux, larger
  time steps reduce the dissipation of the physical mode at high
  frequencies until anti-dissipation (convective instability) at the CFL
  limit, and increase it at low frequencies; with explicit Euler, SD of
  fifth order is anti-dissipative at low frequencies, which a 1D test with
  an oscillating inlet confirms (spatial growth beyond a predicted switch
  near $\Delta t\approx1.0\times10^{-4}$ for $h=0.01$) (§3, §4.1, Figs. 1,
  16–21).
- **Well-resolved vortex.** On an inlet–outlet isentropic vortex at sixth
  and eighth order with RK33, time steps close to the CFL limit slow the
  error convergence, eventually to the order of the time scheme, and on
  deformed meshes this happens at smaller grid sizes; spurious entropy
  oscillations appear only very close to the CFL limit, in agreement with
  the fully-discrete temporal analysis of Vermeire & Vincent (§4.2.1,
  Figs. 23–24).
- **Under-resolved turbulence.** On the inviscid
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at $M=0.1$ on
  $32^3$ elements of sixth-order SD ($N=5$) with third-order Runge–Kutta,
  the numerical dissipation obtained from the kinetic-energy balance at
  $\Delta t/\Delta t_{\max}=0.5$, 0.9 and 0.95 is "almost
  indistinguishable", and "the gradual decrease of numerical dissipation
  observed in the theoretical framework does not manifest" (§4.3.1,
  Fig. 25); a 2D inviscid duct with an oscillating inlet behaves alike
  below about 0.95 of the CFL limit (§4.3.2, Fig. 28). The authors conclude
  that in under-resolved, implicit-LES-like simulations spatial errors
  overshadow the time-integration errors, so the time step matters more
  for DNS-like resolution (abstract, §5); see
  [numerical dissipation](/properties/numerical-dissipation.md) and
  [implicit LES](/definitions/implicit-les.md).

## SD as a comparison target for explicitly filtered LES

[Najafiyazdi et al. (2023)](/sources/najafiyazdi-2023.md), §6.2, compare
their approximate-deconvolution LES (linear finite elements with an
explicit differential filter, see
[scale-similarity models](/methods/scale-similarity-model.md)) on the
Taylor–Green vortex at $Re=1600$ with the flux-reconstruction LES of Bull &
Jameson in three variants, nodal DG, OFR and SD, at $N=1$ on $64^3$
elements (printed as "128 degrees of freedom, i.e. p 1 Legendre polynomials on a 64³ grid"). On their $64^3$ grid
(S64, 274,625 nodes) the deconvolution LES is "more accurate" in both the
energy-based and the vorticity-based dissipation rate (Fig. 10). The SD
results are taken from Bull & Jameson, not recomputed.

## The SD correction parameter in RANS, and SD shock limiting

**$c_{\mathrm{SD}}$ as the default of an implicit FR-RANS solver.**
[Vandenhoeck et al. (2022)](/sources/vandenhoeck-2022.md) run their
implicit [flux-reconstruction](/methods/flux-reconstruction.md) solver for
$k$-$\omega$ SST RANS with Langtry–Menter
[transition](/methods/local-correlation-based-transition-model.md) with the
VCJH parameter $c_{\mathrm{SD}}$ by default (§2). On the ERCOFTAC T3A
[flat plate](/benchmarks/ercoftac-t3-flat-plate.md) at $N=5$ the skin
friction is nearly identical with $c_{\mathrm{SD}}$, $c_{\mathrm{DG}}$ and
$c_{g2}$ (§4.2, Fig. 14), so in this steady RANS case the choice between
the SD-recovering and the DG-recovering corrections does not affect the
result. The solver lives in [COOLFluiD](/software/coolfluid.md), whose
list of discretizations includes a "spectral finite difference" module
beside flux reconstruction (§3.1).

**TENO limiting for SD.**
[Huang et al. (2025)](/sources/huang-2025.md), §1, cite (their ref. 58,
Chen & Fu 2024) a TENO-type limiter with a troubled-cell indicator
applied to the nodal spectral difference method; Huang et al. build the
analogous [shock sensor](/definitions/shock-sensor.md) and limiter for
modal Runge–Kutta DG, not for SD.

## Uses cited by other sources

Four further sources mention SD only through the works they cite:

- **Wall-modelled LES.** In their review of
  [wall-modelled LES](/methods/wall-modelled-les.md),
  [Bose & Park (2018)](/sources/bose-2018.md), §3, list the implementation
  of wall models in "finite element or spectral differencing schemes"
  among the implementation studies they do not discuss, citing the
  structural wall-modelled LES of Lodato, Castonguay & Jameson (2014) with
  a high-order SD scheme for unstructured meshes. They add
  that the cost of wall modelling is often small against that of the rest
  of the flow solution.
- **Moving grids.** [Liu et al. (2022b)](/sources/liu-2022-g.md), §2.1,
  enforce the temporal
  [geometric conservation law](/properties/geometric-conservation-law.md)
  of their moving-grid flux-reconstruction solver with a GCL
  error-compensation approach whose references include a high-order SD
  method for unstructured dynamic grids by Yu, Wang & Hu (2011).
- **Modal filtering.** [Hamedi & Vermeire (2022)](/sources/hamedi-2022.md),
  §2, §6, recall SD (Kopriva; Liu, Vinokur & Wang) among the schemes that
  flux reconstruction recovers and list the optimization of their
  [modal filters](/methods/explicit-modal-filtering.md) for other schemes
  as future work; their filters are optimized only for the DG-recovering
  correction function.
- **The First High-Order CFD Workshop.** [Wang et al. (2013)](/sources/wang-2013.md),
  §1, cite the SD method of Liu, Vinokur & Wang among the high-order
  methods developed for unstructured meshes. None of the workshop
  participants in their Tables II–VII submitted SD results; the entries
  are DG, CPR, finite-difference and finite-volume codes.

## Qualifications

- Evidence for SD in turbulence is three sources: D'Ayer et al. validate an
  immersed boundary (laminar cylinder, one rough channel at one Reynolds
  number) rather than the SD scheme itself, Chapelier et al. compare
  complete codes, so scheme and shock-capturing effects are not separated,
  and Tonicello et al. (2022) validate one supersonic ramp DNS.
  Tonicello et al. (2023) add a linear fully-discrete analysis with
  inviscid tests (vortex, Taylor–Green, 2D duct), none of them a
  turbulence-model assessment.
- **Order convention and node sets.** Tonicello et al. (2022) count $N$ as
  the order (solution degree $N-1$ on $N$ points, flux on $N+1$), D'Ayer
  et al. as the degree; this page writes the degree. Tonicello et al. place
  the solution points at Gauss–Legendre nodes, D'Ayer et al. at
  first-kind Chebyshev nodes, with Gauss–Legendre interior flux points in
  both. Tonicello et al. print 54 million degrees of freedom (Table 2),
  while 360·28·27 elements with $6^3$ solution points each make about
  58.8 million *(compiler check, not in the sources)*.
- **Printed slip (D'Ayer et al. 2026).** §2.2 defines $N+2$ flux points as
  "the two nodes of the considered cell added to the $(p-1)$
  Legendre-Gauss points"; two end points plus $N-1$ interior points make
  $N+1$, not $N+2$, so the interior set needs $N$ points to match the
  stated count and the degree-$N+1$ flux polynomial *(compiler check, not
  in the sources)*.
- **Printed inconsistency (Chapelier et al. 2024).** §III.B.e says the SD3D
  artificial diffusion acts as a bulk viscosity on momentum and a thermal
  diffusivity on energy, with none on mass; §III.B.h says it is "a
  Laplacian operator impacting all conservative variables".
- The version of D'Ayer et al. read is the HAL submitted manuscript
  (hal-05075852v1, May 2025), which prints four authors where the Crossref
  record lists three; the version of Chapelier et al. read is the HAL
  accepted manuscript. The equivalence of $c_{\mathrm{SD}}$ FR with SD is
  cited by Brillon & Nadarajah from the literature, not derived.

- **Order convention (Tonicello et al. 2023).** §2.1 calls $N$ "the
  order of the solution polynomial", while the paper's "5th-order" scheme
  has $N=4$ and superconvergence $2N+1=9$ (App.: "3rd order" with $N=2$),
  so its $N$ is the polynomial degree, as on this page *(compiler check,
  not in the sources)*; Tonicello et al. (2022) above count $N$ as the
  order. Their fully-discrete analysis is linear; the authors state that
  it "is not always representative of more complex nonlinear dynamics"
  (§4.3.2, §5).
- [Najafiyazdi et al. (2023)](/sources/najafiyazdi-2023.md) compare a grid
  of 274,625 nodes (65 per direction *(compiler check, not in the
  sources)*) with SD runs printed as "128 degrees of freedom, i.e. p 1
  Legendre polynomials on a 64³ grid".

# Citations

- [D'Ayer et al. (2026)](/sources/dayer-2026.md) — HAL hal-05075852v1: §1 (SD stability, cost against FR, purpose); §2.1–2.2, Eqs. (1)–(10), Fig. 1 (equations, SD formulation, nodes, Roe flux, BR1, JAGUAR); §2.4 (time integration); §3.1, Tables 1–2, Figs. 3–5 (cylinder); §3.2, Table 3, Figs. 7–10 (rough minimal channel); §4.
- [Tonicello et al. (2022)](/sources/tonicello-2022.md) — §2, Table 2 (DNS set-up and resolution); §2.2, Eqs. (2.6)–(2.10) (bulk artificial viscosity, Ducros factor); §3.2, Figs. 7–8, 13; §4.1–4.2, Figs. 17–18; App. A, Eqs. (A1)–(A14) (SD formulation); App. B–C (modal sensor, positivity limiter).
- [Hamedi & Vermeire (2022)](/sources/hamedi-2022.md) — §2 (SD recovered by FR, cited); §6 (filters for other schemes as future work).
- [Brillon & Nadarajah (2026)](/sources/brillon-2026.md) — arXiv 2411.12108v1: §1, §3.1.5 (ESFR recovers SD; $c_{\mathrm{SD}}$ dissipation ordering).
- [Chapelier et al. (2024)](/sources/chapelier-2024.md) — HAL hal-04582857v1: §III.B.e, h, Tables I–II (SD3DvisP); §IV.A–B, Figs. 5–8; §V.
- [Vandenhoeck et al. (2022)](/sources/vandenhoeck-2022.md) — §2 (VCJH, $c_{\mathrm{SD}}$ default); §3.1 (COOLFluiD modules); §4.2, Fig. 14 (T3A skin friction for three VCJH parameters).
- [Huang et al. (2025)](/sources/huang-2025.md) — §1 (TENO limiter for spectral difference, cited).
- [Bose & Park (2018)](/sources/bose-2018.md) — §3 (wall-model implementation with SD, cited; cost of wall modelling).
- [Liu et al. (2022b)](/sources/liu-2022-g.md) — §2.1 (GCL error compensation, SD on dynamic grids cited).
- [Wang et al. (2013)](/sources/wang-2013.md) — §1 (SD cited among unstructured high-order methods); Tables II–VII (participants).
- [Tonicello et al. (2023)](/sources/tonicello-2023.md) — §2.1–2.2 (FR-SD semi- and fully-discrete spatial analysis); §3, Figs. 1–9, App. Figs. 29–32 (SD against DG, superconvergence, time-step effects); §4.1–4.3, Figs. 10–28 (improved SD tests: linear advection, isentropic vortex, inviscid Taylor–Green vortex, 2D duct); §5.
- [Najafiyazdi et al. (2023)](/sources/najafiyazdi-2023.md) — §6.2, Table 2, Fig. 10 (comparison with Bull & Jameson's FR-SD LES of the Taylor–Green vortex).
- [Liu & Yuan (2023)](/sources/liu-2023-b.md) — §1 (FR casts nodal DG and SD in one framework; Jameson's energy-stability proof for SD, as cited).
- [Shi & Yan (2023)](/sources/shi-2023.md) — §I (FR/CPR unifies DG and SD; DG, SD and FR/CPR for implicit LES, as cited).
