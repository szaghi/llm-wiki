---
type: Source
title: "Brackbill & Barnes (1980) — The Effect of Nonzero ∇ · B on the Numerical Solution of the Magnetohydrodynamic Equations"
description: "A short note showing that with a nonzero discrete divergence the conservative MHD momentum equation carries a force along B, whose dot product with B is |B|² ∇·B, which corrupts low-speed flows; it names the Poisson projection in one sentence but proposes and tests the nonconservative (curl B × B) momentum equation with conservative induction and energy instead."
resource: "doi:10.1016/0021-9991(80)90079-0"
source_kind: paper
authors: [Brackbill J.U., Barnes D.C.]
year: 1980
venue: "J. Comput. Phys. 35:426-430"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/1980-JCP-Brackbill-1010160021-99918090079-0.pdf"
tags: [mhd, divergence-free, projection, lagrangian]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

A five-page *Note*. Difference equations for MHD do not keep
$\nabla\cdot\mathbf B = 0$ exactly; the error is of the order of the
truncation error. The authors show that with $\nabla\cdot\mathbf B \ne 0$
the MHD equations are no longer a conservation system, so a scheme must
choose which property to keep. The conservative magnetic force, the
divergence of the Maxwell stress, then has a component along $\mathbf B$:
its projection on $\mathbf B$ is $\vert\mathbf B\vert^2\,\nabla\cdot\mathbf B$
(eq. 8). That force drives flow along the field which has no physical
cause, and it matters most when the flow is slow compared with the
Alfvén speed.

The cure they propose and test is **not** a projection. They difference
the momentum equation in nonconservative ($(\nabla\times\mathbf B)\times\mathbf B$)
form and keep induction and energy in conservation form, so that energy
and magnetic flux are conserved exactly, momentum to truncation error,
and the parallel force vanishes for any $\nabla\cdot\mathbf B$
(eqs. 9–10). The Poisson projection
$\nabla^2\Phi + \nabla\cdot\mathbf B = 0$, $\mathbf B \leftarrow \mathbf B + \nabla\Phi$
is named in one sentence as an alternative (p. 428), with no discrete
operators, no solver and no test. One test, an implicit 2D Lagrangian
r–z run of a uniform low-β plasma in a uniform axial field, inverts
cells and stops with the conservative momentum equation (Fig. 1) and
stays undistorted with the nonconservative one (Fig. 2). The note has
no shock problem and no high-order scheme; its place in this bundle is
the origin of the parallel-force argument and of the "Brackbill–Barnes
projection" name that later sources use.

# Key claims

1. **The scheme generates divergence** (p. 426, eq. 2). With
   $\nabla\cdot\mathbf B = 0$ initially, the difference equations give
   $\partial_t(\nabla\cdot\mathbf B) = 0$ only up to terms of first or
   higher order in $h$ and $\Delta t$.
2. **With $\nabla\cdot\mathbf B \ne 0$ the equations are not in
   conservation form** (pp. 426–427, eqs. 3–5 and the energy integral).
   The flux statement (eq. 3) is the induction equation plus the term
   $\mathbf v(\nabla\cdot\mathbf B)$; the momentum equation (eq. 4) is
   $\rho\,\frac{d\mathbf v}{dt} = -\nabla p - \mathbf B\times(\nabla\times\mathbf B)$,
   with $\frac{d}{dt}$ the material derivative; continuity is eq. 5.
   Combined, in units with unit permeability, they give
   $$\frac{d}{dt}\int\left\{\tfrac12\rho\,\vert\mathbf v\vert^2 + \tfrac12\vert\mathbf B\vert^2\right\}dV = \int\left\{\nabla\cdot\left[-\left(p + \tfrac12\vert\mathbf B\vert^2\right)\mathbf v + \mathbf B(\mathbf B\cdot\mathbf v)\right] - (\mathbf B\cdot\mathbf v)\,\nabla\cdot\mathbf B\right\}dV,$$
   which is not in conservation form: "when $\nabla\cdot\mathbf B \neq 0$,
   the magnetic flux, momentum, and energy of an isolated system are not
   constants of the motion" (p. 427).
3. **Conservation form is correct only for $\nabla\cdot\mathbf B = 0$**
   (pp. 426–427, eq. 7). Then the magnetic force of eq. 4 equals the
   divergence of the Maxwell stress, $\nabla\cdot\left\{-\tfrac12\vert\mathbf B\vert^2\mathbf I + \mathbf B\mathbf B\right\}$.
   Differencing that form conserves flux, energy and momentum "even when
   $\nabla\cdot\mathbf B \neq 0$". Both forms are consistent with the
   divergence-free equations, since the divergence is of truncation-error
   size.
4. **The parallel force** (p. 427, eq. 8, citing Barnes & Brackbill 1977).
   The projection of the conservative magnetic force on $\mathbf B$ is
   $\vert\mathbf B\vert^2\,\nabla\cdot\mathbf B$, nonzero whenever the
   divergence is. Since that divergence is itself an error proportional to
   $\mathbf B$, "the error in the force relative to the fluid velocity will
   be the greater the lesser the fluid velocity is relative to the Alfven
   speed". In a numerical equilibrium the pressure gradient along
   $\mathbf B$ is nonzero unless $\nabla\cdot\mathbf B = 0$, and "in some
   instances ... no numerical equilibrium exists".
5. **When conservation form matters** (p. 427). Exact conservation form
   "may be imperative only for high-speed flows where Rankine–Hugoniot
   conditions across shocks would not be satisfied otherwise". For
   low-speed flow over many signal transit times (low-β instabilities,
   equilibria) the conservative momentum equation "may be inappropriate".
6. **Cures named and cure chosen** (pp. 428–429). One can formulate MHD
   "in terms of fluxes for which $\nabla\cdot\mathbf B = 0$ automatically",
   or solve $\nabla^2\Phi + \nabla\cdot\mathbf B = 0$ and set
   $\mathbf B \leftarrow \mathbf B + \nabla\Phi$, which is divergence-free
   (unnumbered, p. 428). "However, one can eliminate the parallel force
   without having to solve a potential problem by differencing the
   nonconservative form of the momentum equation, Eq. (4)". No discrete
   divergence, gradient or Laplacian, no Poisson solver, no boundary
   condition and no projection test are given.
7. **The proposed system** (p. 429, eqs. 9–10). The nonconservative
   momentum equation is consistent with energy conservation if the
   induction equation is written in conservation form (eq. 9: eq. 3
   without the $\mathbf v(\nabla\cdot\mathbf B)$ term). Eqs. 4, 5, 9 and 10
   form a system "for which energy and magnetic flux are constants of the
   motion, momentum is conserved to" truncation error, "and
   $\mathbf F\cdot\mathbf B$ is zero for all $\nabla\cdot\mathbf B$"
   ($\mathbf F$ the magnetic force).
8. **Generality** (p. 430). In an explicit calculation with leapfrog and
   Lax–Wendroff time differencing (Turkel, private communication), "the
   residual kinetic energy was decreased by $10^3$ when the
   $\nabla\cdot\mathbf B$ error was corrected"; the authors conclude that
   removing the parallel force "is of universal importance in
   computational magnetohydrodynamics". How Turkel corrected the error is
   not stated.

# Tests

One problem, two runs (pp. 427–430, Figs. 1–2). Implicit 2D Lagrangian
scheme on an initially rectilinear mesh (refs. 4–5 of the note), which
conserves mass, momentum, magnetic flux and energy for all values of
$\nabla\cdot\mathbf B$ and is called "equivalent to the Eulerian
conservation form"; the scheme itself is not described in the note.
Geometry r–z, the symmetry axis as left boundary, $\mathbf v = 0$ on the
top, right and bottom boundaries. Uniform plasma, uniform initial field
parallel to the axis, plasma beta $1.3\times10^{-8}$ (Fig. 1 caption).
The mesh is drawn as 4 × 5 cells (r × z) in both figures.
1. **Conservative momentum** (Fig. 1). After 209 steps, 160 signal transit
   times across the mesh, the mesh is visibly deformed, with vertex
   displacements along $\mathbf B$. The caption gives velocities of about
   $2\times10^{-3}$ times the Alfvén speed; the text (p. 428) says
   $10^{-2}$ (see Citations). The flow "has no physical cause, and it
   eventually inverts cells and terminates the calculation".
2. **Nonconservative momentum, eq. 4** (Fig. 2). Same initial and
   boundary data. After 171 steps, 300 signal transit times, the mesh is
   undistorted; small random velocities appear, "but the kinetic energy is
   only 1/4000 as much as it is with the conservative formulation and
   remaining constant".

No error norms, no divergence values, no shock problem, no projection
run and no cost data are reported.

# Notation map

| Brackbill & Barnes (1980) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf B$ | $\mathbf B$ | |
| $\mathbf u$ | $\mathbf v$ | fluid velocity |
| $\rho$, $p$ | $\rho$, $p$ | |
| $\mu$ | words (unit permeability) | appears only in the energy integrals; **collision**: registry $\mu$ is a diffusion coefficient |
| $\mathbf F$ | words (conservative magnetic force) | no registry symbol; a bold $\mathbf F$ would read as a flux |
| $\mathbf I$ | $\mathbf I$ | identity tensor |
| $\phi$ | $\Phi$ | projection potential, same sign convention as the registry; **collision**: $\phi_i$ is the PPM flattening |
| $\mathbf B'$ | $\mathbf B$ after $\leftarrow$ | projected field |
| $\Delta x^m$, $\Delta t^n$ | words (orders in $h$ and $\Delta t$) | **collision**: registry $m$ is the system size |
| $d/dt$ | words (material derivative) | eq. 4 |
| $(\mathbf B\cdot\mathbf B)\nabla\cdot\mathbf B$ | $\vert\mathbf B\vert^2\,\nabla\cdot\mathbf B$ | eq. 8 |

# Pages created or updated

* Updated [Constrained transport for high-order capturing schemes (MHD)](/methods/constrained-transport.md) (batch-15 block: the parallel force and the crash are this note's; what it says about projection).
* Updated [Hyperbolic (GLM) divergence cleaning](/methods/hyperbolic-divergence-cleaning.md) (batch-15 block: the "Brackbill–Barnes" projection of Tomida et al. as the note states it; the parallel force against Derigs et al.'s statement; an Open `Contradictions` entry on its printed sign, + here against − in Derigs et al. (2018) eq. 2.21).

# Citations

1. `/home/stefano/papers/mosaic/high-order-capturing-schemes/1980-JCP-Brackbill-1010160021-99918090079-0.pdf`.
   * **Version read.** The published journal version (a *Note*), a
     5-page scan with a poor OCR layer. Received 31 October 1978, revised
     22 May 1979; Los Alamos Scientific Laboratory.
   * **Identity.** doi:10.1016/0021-9991(80)90079-0 (from the PDF's PII;
     not printed on the page), checked on Crossref: "The Effect of Nonzero
     ∇ · B on the numerical solution of the magnetohydrodynamic
     equations", Brackbill J.U., Barnes D.C., J. Comput. Phys. 35(3):426–430,
     May 1980, in agreement with page 1.
   * **How it was read.** Every page rendered and read from the page
     images (110 dpi, with 250–600 dpi crops of the energy integral and the
     Fig. 1 caption); the OCR layer was not relied on.
   * **Recorded as printed.**
     - The equation number of the p. 427 energy integral is not legible in
       the scan (eq. 6 by sequence); its bracket closure and that of eq. 10
       are reproduced as rendered.
     - Eq. 10 lacks the factor $\mathbf v$ after
       $(p + \tfrac12\vert\mathbf B\vert^2)$ that the p. 427 integral carries;
       recorded, not corrected.
     - Fig. 1: caption $2\times10^{-3}$ times the Alfvén speed, text
       (p. 428) $10^{-2}$, for the same run. The caption superscripts (beta
       $1.3\times10^{-8}$, $2\times10^{-3}$) were read at 600 dpi; the OCR
       layer gives "1O-8" and "1O-S".
     - $\mu$ appears in the energy integrals but not in eqs. 4 and 7.
     - The curl term of eq. 3 is printed with a plus sign,
       $\partial_t\mathbf B + \nabla\times(\mathbf v\times\mathbf B) + \mathbf v(\nabla\cdot\mathbf B) = 0$
       (checked by the compiler on the page image, p. 426); the ideal
       induction law reads $\partial_t\mathbf B = \nabla\times(\mathbf v\times\mathbf B)$.
       Recorded as printed, not corrected.
     - Bibliographic: later sources print the pages as 35:462 (a digit
       transposition of 426, confirmed by the running head).
   * **Reference list:** 5 entries, four without titles (the
     journal-style citations of refs. 1, 4 and 5, and Turkel's private
     communication, ref. 2); ref. 3 is Panofsky & Phillips's book, cited at
     p. 162, with the first author's initial printed "N.". All merged.
     Bibliography: 3122 entries.
