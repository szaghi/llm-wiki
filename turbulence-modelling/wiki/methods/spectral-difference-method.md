---
type: Method
title: "Spectral difference method"
description: "The spectral difference method is a nodal high-order element scheme that interpolates the solution on N+1 points and the flux on N+2 points per direction, made continuous by Riemann fluxes and differentiated at the solution points; this page covers its formulation, its place in the flux-reconstruction family, and its DNS and shock-capturing uses."
status: established
aliases: [SD, SD method, spectral difference, staggered-grid Chebyshev multidomain method]
tags: [flux-reconstruction, dns, compressible, immersed-boundary, implicit-les, numerical-dissipation]
timestamp: 2026-10-27T10:58:00Z
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
([D'Ayer et al. 2026](/sources/dayer-2026.md), §2.2, Eqs. 6–10, recalling
Kopriva & Kolias, Kopriva, Liu, Vinokur & Wang, and Wang et al.). Within the
energy-stable [flux-reconstruction](/methods/flux-reconstruction.md) family
a particular value of the correction parameter, $c_{\mathrm{SD}}$, "recover[s]
the stable spectral difference (SD) scheme"
([Brillon & Nadarajah 2026](/sources/brillon-2026.md), §1, §3.1.5, as
recalled from Allaneau & Jameson). Two scale-resolving uses appear in the
sources: the compressible DNS solver JAGUAR with an immersed boundary
(D'Ayer et al. 2026) and the shock-capturing code SD3DvisP in a
supersonic Taylor–Green comparison
([Chapelier et al. 2024](/sources/chapelier-2024.md)).

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
established (§1).

**Several dimensions.** On quadrilaterals and hexahedra the
one-dimensional procedure is repeated direction by direction with tensor
products of the one-dimensional bases (Eq. 10); each direction has its own
staggered flux points (Fig. 1). Viscous fluxes need the solution gradient,
which JAGUAR computes with the first Bassi–Rebay scheme (BR1, §2.2). The
same solver handles triangles and tetrahedra through Raviart–Thomas flux
spaces, not used in that paper (§2.2).

**Cost against FR.** As recalled by D'Ayer et al. (2026, §1), earlier work
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

**TENO limiting for SD.** As recalled by
[Huang et al. (2025)](/sources/huang-2025.md), §1 (their ref. 58, Chen &
Fu 2024), a TENO-type limiter with a troubled-cell indicator has been
applied to the nodal spectral difference method; Huang et al. build the
analogous [shock sensor](/definitions/shock-sensor.md) and limiter for
modal Runge–Kutta DG, not for SD.

## Uses cited by other sources

Three further sources mention SD only through the works they cite:

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
- **The First High-Order CFD Workshop.** [Wang et al. (2013)](/sources/wang-2013.md),
  §1, cite the SD method of Liu, Vinokur & Wang among the high-order
  methods developed for unstructured meshes. None of the workshop
  participants in their Tables II–VII submitted SD results; the entries
  are DG, CPR, finite-difference and finite-volume codes.

## Qualifications

- Evidence for SD in turbulence is two sources: D'Ayer et al. validate an
  immersed boundary (laminar cylinder, one rough channel at one Reynolds
  number) rather than the SD scheme itself, and Chapelier et al. compare
  complete codes, so scheme and shock-capturing effects are not separated.
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
  recalled by Brillon & Nadarajah from the cited literature, not derived.

# Citations

- [D'Ayer et al. (2026)](/sources/dayer-2026.md) — HAL hal-05075852v1: §1 (SD stability, cost against FR, purpose); §2.1–2.2, Eqs. (1)–(10), Fig. 1 (equations, SD formulation, nodes, Roe flux, BR1, JAGUAR); §2.4 (time integration); §3.1, Tables 1–2, Figs. 3–5 (cylinder); §3.2, Table 3, Figs. 7–10 (rough minimal channel); §4.
- [Brillon & Nadarajah (2026)](/sources/brillon-2026.md) — arXiv 2411.12108v1: §1, §3.1.5 (ESFR recovers SD; $c_{\mathrm{SD}}$ dissipation ordering).
- [Chapelier et al. (2024)](/sources/chapelier-2024.md) — HAL hal-04582857v1: §III.B.e, h, Tables I–II (SD3DvisP); §IV.A–B, Figs. 5–8; §V.
- [Vandenhoeck et al. (2022)](/sources/vandenhoeck-2022.md) — §2 (VCJH, $c_{\mathrm{SD}}$ default); §3.1 (COOLFluiD modules); §4.2, Fig. 14 (T3A skin friction for three VCJH parameters).
- [Huang et al. (2025)](/sources/huang-2025.md) — §1 (TENO limiter for spectral difference, recalled).
- [Bose & Park (2018)](/sources/bose-2018.md) — §3 (wall-model implementation with SD, cited; cost of wall modelling).
- [Liu et al. (2022b)](/sources/liu-2022-g.md) — §2.1 (GCL error compensation, SD on dynamic grids cited).
- [Wang et al. (2013)](/sources/wang-2013.md) — §1 (SD cited among unstructured high-order methods); Tables II–VII (participants).
