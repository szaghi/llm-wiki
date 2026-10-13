---
type: Method
title: "Multidimensional Riemann solvers"
description: "Riemann solvers at the vertices and edges of a structured mesh, where four states meet: a strongly interacting state bounded by the wave model [S_L, S_R]×[S_D, S_U], in LLF and HLL forms or with linear sub-structure along chosen intermediate families (the MuSIC analogue of HLLI); they upwind edge electric fields for constrained transport without doubled dissipation, and vertex potentials for curl-preserving schemes; stability and positivity are argued, not proved."
status: established
aliases: [MuSIC Riemann solver, multidimensional HLL, multidimensional HLLI, two-dimensional Riemann solver, vertex Riemann solver]
tags: [riemann-solver, multidimensional-riemann-solver, constrained-transport, mhd, numerical-flux]
timestamp: 2026-10-13T00:00:00Z
---

# Multidimensional Riemann solvers

A one-dimensional [Riemann solver](/methods/approximate-riemann-solvers.md)
upwinds a face in its normal direction only. At a vertex of a 2D
structured mesh (an edge in 3D) four states meet, labelled $RU$,
$LU$, $LD$ and $RD$ (right/left, up/down), and a quantity collocated
there needs upwinding in both transverse directions. The prime case is
the edge electric field $\boldsymbol{\mathcal E}$ that updates the face
fields of [constrained transport](/methods/constrained-transport.md)
([Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §§1–3); a
second is the vertex potential of
[curl-preserving schemes](/methods/curl-preserving-reconstruction.md)
([Balsara et al. (2023)](/sources/balsara-2023.md), §§2.5, 3.4). All the
sources here are by Balsara and co-workers.

**Before such solvers.** An ADER–WENO MHD scheme averaged edge electric
fields over the four adjoining faces and, for the electric fields only
and only where $S_L < 0 < S_R$, doubled the HLL dissipation
bracket ([Balsara et al. (2009)](/sources/balsara-2009.md),
§4.1). A multidimensional solver removes any need for that doubling
([Balsara & Kim (2016)](/sources/balsara-2016-b.md), §1), and doubling
"indiscriminately" over-dissipates the transverse field
([Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §1). Neither
paper runs a test that isolates the claim.

## Wave model and strongly interacting state

Wave-speed estimates in the two directions bound a
strongly interacting state in the similarity variables $(x/t, y/t)$ by
the rectangle $[S_L, S_R]\times[S_D, S_U]$. Its mean state and the fluxes
$f^{**}_x$, $f^{**}_y$ follow from conservation over that wave model:
zeroth and first moments, with boundary integrals of the four 1D
Riemann solutions on its sides
([Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §3.1,
eqs. 3.10–3.12, built on part I of the series).

* **LLF limit.** With one signal speed $S$, the induction form with
  anti-symmetric fluxes gives the edge field
  $$\mathcal E^{**}_z = \tfrac14\left(\mathcal E_{z,RU} + \mathcal E_{z,LU} + \mathcal E_{z,LD} + \mathcal E_{z,RD}\right) + \tfrac{S}{2}\left[B_{x,D} - B_{x,U} + B_{y,R} - B_{y,L}\right],$$
  so the dissipation acts only on transverse jumps of the normal field
  ([Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), eq. 12).
  The HLL version adds a supersonic limit through a nine-case conditional
  (eqs. 16–20) and is preferred for strongly supersonic MHD.
* **LLF at a vertex for a scalar potential.** At first order the update
  becomes a centred difference plus $\frac{\vert v_d\vert}{2h_d}$ times a
  second difference in each direction $d$, a properly upwinded scheme on
  an edge-centred control volume
  ([Balsara et al. (2023)](/sources/balsara-2023.md), §§2.5, 3.4).
* **Multidimensional HLL.** The strongly interacting state is constant
  over the wave model. This solver is "genuinely multidimensional even when
  sub-structure is absent" ([Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §3.1).

## Sub-structure (the MuSIC solver)

The strongly interacting state is allowed to vary linearly in both
similarity variables. Its undivided differences between opposite sides
of the wave model are projected onto the intermediate families
$p \in \mathcal I$ of the $x$- and $y$-Jacobians at the mean state, as in
the 1D [HLLI](/methods/hllem-riemann-solver.md) solver. The fluxes are
the mean fluxes corrected by the Jacobian times the slope; the
characteristic matrices are rebuilt from the evaluated sub-eigenstructure
([Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §3.1,
eqs. 3.4–3.22).

* **Relativistic MHD.** A solver built from HLLC/HLLEM pieces keeps
  linear sub-structure of the entropy and Alfvén waves. The edge field is
  $\mathcal E_z = \tfrac12\left(-(f^{**}_x)_7 + (f^{**}_y)_6\right)$, the
  mean of two multidimensionally upwinded flux components
  ([Balsara & Kim (2016)](/sources/balsara-2016-b.md), §4.2;
  [constrained transport](/methods/constrained-transport.md)).
* **Boundary profiles: HLL, not HLLI.** If the four sides carry the 1D
  HLLI linear profiles, the 2D $x$-flux reduces exactly to the 1D HLLI
  flux for $x$-aligned flow (App. B). But those profiles are "overly
  steepened": the transverse fluxes then produce too little entropy, and
  the solver is unstable at strong shocks. "The proof steers us false",
  and the paper uses constant HLL states on the sides. The mean flux
  shift for $x$-aligned flow becomes $(S_R - S_L)/4$ times the slope
  instead of $(S_R - S_L)/6$, the weight takes the 1D form with $/3$
  replaced by $/2$ and the cap $-2S_RS_L/(S_R - S_L)^2$, and the
  reduction to 1D HLLI is "closely analogous", not exact
  ([Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §3.1, eqs. 3.18–3.21).
* **Properties.** At zero slopes the solver is exactly multidimensional
  HLL. With every wave in $\mathcal I$ it is complete. It keeps
  mesh-aligned stationary contacts, and is asserted to inherit the
  well-balancing of HLLI ([well-balanced schemes](/properties/well-balanced.md)).
  Positivity is enforced at the four vertices of the wave model by
  reducing the differences, a procedure rather than a proof. HLLC or HLLD
  sides fitted by least squares are possible but give "not that much
  incremental benefit" (§3.1).

## Use in high-order schemes

* **ADER–WENO face fluxes.** A "simplified Simpson rule" weights each of
  four multidimensional solves at the edge centres of a face by 1/6 and
  one 1D HLLI solve "at the zone center" (as printed; the face centre,
  read physically) by 1/3, fed by time-averaged
  [ADER](/methods/ader.md) predictor states. For MHD the edge solves give
  the edge electric field directly. The number of Riemann solves does not
  grow with order ([Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §4).
* **CFL.** 0.8 at second and third order for hydrodynamics, 0.4 at fourth.
  MHD and RMHD use 0.65 at second and third order and 0.4 at fourth,
  because FV schemes for the induction equation are stable only up to
  0.666 (§4, citing Balsara & Käppeli).
* **Finite-difference hosts.** In [AFD-WENO](/methods/alternative-finite-difference-weno.md)
  the corner fields come from 2D WENO interpolation of cell-centred
  $\mathcal E_z$ and the jumps from 2D WENO reconstruction of the face
  fields, with the LLF or HLL solver above
  ([Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §4).

**Evidence.** On torsional Alfvén-wave decay ($120^2$, $t = 129$), 1D HLL
with a multidimensional solver without sub-structure dissipates 6 times
more at second order and 3 times more at third than 1D HLLI with
sub-structure; at fourth order the difference is "almost negligible"
([Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §5.5;
[Balsara (2017)](/sources/balsara-2017-d.md), §IX.5;
[circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md)).
ADER–WENO with the MuSIC solver reaches design order 2–4 on hydrodynamic
and MHD vortices, and at fourth order tracks a stationary, non-aligned
contact "exactly" over a few thousand steps
([Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §§4.1–4.2, 5.8).
The same solvers carry the fourth-order [MHD rotor](/benchmarks/mhd-rotor.md)
on $1000^2$ and a third-order 3D [MHD blast](/benchmarks/mhd-blast-wave.md)
at plasma beta $1.117\times10^{-4}$, CFL 0.4
([Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §§5.3–5.4; repeated
in [Balsara (2017)](/sources/balsara-2017-d.md), §§IX.3–IX.4).

**Status.** No stability or positivity proof exists for the
multidimensional solvers in these sources. The dissipation analysis
against Roe is one-dimensional (see [HLLEM (HLLI)](/methods/hllem-riemann-solver.md)),
and no source reports timings.

# Citations

1. [Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §§1, 3–5, App. B.
2. [Balsara & Kim (2016)](/sources/balsara-2016-b.md), §§1, 4.2.
3. [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §§1–4.
4. [Balsara et al. (2023)](/sources/balsara-2023.md), §§2.5, 3.4.
5. [Balsara (2017)](/sources/balsara-2017-d.md), §§IX.3–IX.5.
6. [Balsara et al. (2009)](/sources/balsara-2009.md), §4.1.
