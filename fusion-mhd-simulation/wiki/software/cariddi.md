---
type: Software
title: "CARIDDI"
description: "3D magneto-quasi-static integral eddy-current code that discretizes only the conductors with edge-element current bases; coupled two-way and fully implicitly to reduced-MHD JOREK through a virtual-casing equivalent surface current, it adds 3D volumetric walls with ports to nonlinear MHD and agrees with JOREK–STARWALL within 2 % (VDE) and 1 % (tearing)."
status: established
aliases: [JOREK-CARIDDI]
tags: [code, wall, free-boundary, vde, tearing, verification]
timestamp: 2026-10-16T23:30:00Z
---

# CARIDDI

CARIDDI is an integral-formulation, magneto-quasi-static eddy-current code
that discretizes only the conducting volumes
([Isernia et al. (2023)](/sources/isernia-2023.md), §II B). Its coupling to
[JOREK](/software/jorek.md), JOREK–CARIDDI, is described as "the first
numerical tool capable of simulating 3D non-linear MHD plasmas in
self-consistent interaction with eddy currents in 3D volumetric conductors"
(§VII). [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) (abstract, §3.1, §5)
count the two-way coupling among the main JOREK developments of 2021–2024. See
[free-boundary and resistive-wall coupling](/methods/resistive-wall-coupling.md).

## Conductor model

From Isernia et al. (2023), §II B, Eqs. 4–12:
* The electric field is $-\partial_t\mathbf A-\nabla\Phi$, with $\mathbf A$ the
  Biot–Savart integral of the conductor currents plus the plasma source, in the
  Coulomb gauge; Ohm's law $\eta_w\mathbf J=\mathbf E$ in the conductor is
  imposed in weak form.
* The current density is the curl of an electric vector potential expanded in
  edge shape functions, with a tree–cotree gauge; the basis lets the
  tangential current jump across faces while the normal component stays
  continuous.
* Galerkin projection gives a circuit equation with resistance, inductance and
  electrode-incidence matrices; electrodes on plasma-facing surfaces, needed
  for halo currents, are excluded in the cited work.

## Coupling to JOREK

From Isernia et al. (2023), §II C–D:
* **Virtual casing.** A superconducting interface at the JOREK boundary would
  shield all interior currents, so an equivalent surface current there
  reproduces the plasma field outside. It is discretized as a thin CARIDDI
  shell (0.1 mm) and found in weak form by inverting the shell inductance
  matrix against the tangential vector potential supplied by JOREK (Eqs.
  13–22). The coupling is "indirect" in the Bielak–MacCamy sense.
* Eliminating the shell currents gives a circuit equation for the wall
  currents with a modified inductance, the wall inductance as seen through a
  superconducting shell that holds the boundary flux constant, and a vacuum
  response for the tangential poloidal field at the boundary. For reduced MHD
  ($\mathbf A=\psi\nabla\phi$) this field is the natural boundary condition of
  the current definition equation, as in JOREK–STARWALL (Eqs. 24–27).
* The structure mirrors JOREK–STARWALL, including a generalized eigenproblem
  that diagonalizes the wall equation when the implicit $\Delta t$ changes
  (Eq. 28); coupling matrices are computed once in CARIDDI, and parallel I/O
  and matrix distribution are inherited from JOREK–STARWALL (§II D).
* The tangential field from the shell is evaluated 1 mm outside the boundary,
  because the equivalent current makes $\mathbf B$ discontinuous there (§II C).

## Verification

From Isernia et al. (2023):
* **Vacuum response** against the analytic field of a tilted toroidal wire on
  an ASDEX Upgrade-like boundary: relative RMS error down to about 0.1 %
  ($n=0$) and 0.25–0.37 % ($n=1$), and 0.45–2 % for $n=2$ depending on toroidal
  resolution; the
  response is more sensitive to quadrature in the inductance matrix that must
  be inverted than in the field matrix; the 1 mm offset adds at most 0.15 %
  (§III, Figs. 2–3). The conclusion's "up to an error of 0.2%" holds only for
  $n=0$ (recorded on the Source page).
* **Axisymmetric ASDEX Upgrade VDE** (wall plus two passive stabilizing loops,
  bulky conductors in CARIDDI, thin bands in STARWALL): growth rates of
  39.87 s$^{-1}$ (JOREK–CARIDDI), 39.59 s$^{-1}$ (JOREK–STARWALL) and
  44.38 s$^{-1}$ (the mass-less CarMa0NL), JOREK–CARIDDI and JOREK–STARWALL
  within 2 % throughout; the CarMa0NL gap, about 1 % initially and about 10 %
  later, is attributed to its fixed profiles and current (§IV, Figs. 4–6). See
  [vertical displacement event](/definitions/vertical-displacement-event.md).
* **2/1 tearing mode** in a circular plasma ($R=10$ m, $a=1$ m, wall radius
  1.1 m, 5 mm thick): the $n=1$ growth rate rises from about 630 s$^{-1}$
  (ideal wall) to about 960 s$^{-1}$ (no wall) over eight decades of wall
  resistivity, the two couplings agreeing within 1 % (§V, Fig. 7). See
  [tearing mode](/definitions/tearing-mode.md).

## Applications

* **Ports and mode coupling** (ASDEX Upgrade-like 2/1 tearing case with
  harmonics $n=1,2$): equally spaced holes raise the $n=1$ growth rate
  monotonically from 509.5 to 573.0 s$^{-1}$ for 0 to 8 holes. With 2, 4, 6 or
  8 holes the wall does not couple $n=1$ and $n=2$, and $n=2$ grows nonlinearly
  at about twice the $n=1$ rate; with 1 or 3 holes the wall couples them and
  $n=2$ grows at about the $n=1$ rate (§VI, Table I, Fig. 8). The authors
  infer that the number of toroidal harmonics may have to be tuned to the
  periodicity of the conductors (§VII).
* **3D hot VDE with a single port**: slightly faster vertical growth, $n>0$
  energies jumping at the control-coil kick, and an earlier thermal quench at a
  larger $q_{95}$; JOREK–CARIDDI and JOREK–STARWALL agree (§VI, Figs. 10–11).
* Hoelzl et al. (2024) (§3.1, Fig. 7) report the eddy-current benchmark with a
  single-hole vessel and note that the non-axisymmetric wall induces mode
  coupling.

## Limitations

* Only reduced MHD is coupled; the full-MHD extension needs both tangential
  field components and is outlined only (Isernia et al. 2023, §II A, §VII).
* The solenoidal equivalent current cannot represent halo currents crossing the
  boundary (§II C, §VII); halo-current and full-MHD coupling were "still
  ongoing" in 2024 (Hoelzl et al. 2024, §3.1).
* The control surface is axisymmetric, so the coupling applies to tokamaks
  only; stellarators are future work (Isernia et al. 2023, §VII).
* No run times, wall mesh sizes or time steps are reported (§IV–VI); matrix
  compression above 500 000 wall degrees of freedom and n-fold symmetry are
  planned (§VII).

# Citations

1. [Isernia et al. (2023)](/sources/isernia-2023.md) — §§I–VII, Table I, Figs. 2–11.
2. [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) — abstract, §3.1, §5, Fig. 7.
