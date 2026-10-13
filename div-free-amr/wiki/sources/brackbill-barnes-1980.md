---
type: Source
title: "Brackbill & Barnes (1980) — The effect of nonzero ∇·B on the numerical solution of the magnetohydrodynamic equations"
description: "Five-page Note identifying the force parallel to the field, (B·B)∇·B, that the conservative Maxwell-stress momentum equation produces when ∇·B ≠ 0, and removing it with a nonconservative momentum equation instead of a projection."
resource: "doi:10.1016/0021-9991(80)90079-0"
source_kind: paper
authors: [Brackbill J.U., Barnes D.C.]
year: 1980
venue: "J. Comput. Phys. 35:426-430"
local_file: "/home/stefano/papers/mosaic/div-free-amr/1980-JCP-Brackbill-1010160021-99918090079-0.pdf"
tags: [mhd, divergence-constraint, parallel-force, nonconservative-momentum, lagrangian]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

A five-page Note on how small errors in $\nabla\cdot\mathbf B = 0$ corrupt
MHD solutions written in conservation form. When the magnetic force is
written as the divergence of the Maxwell stress, its component along
$\mathbf B$ is $(\mathbf B\cdot\mathbf B)\,\nabla\cdot\mathbf B$ (eq. 8).
This nonphysical parallel force dominates low-speed, low-β integrations
over many transit times, such as equilibria and instabilities.

The cure the paper adopts is **not a projection**. It differences the
momentum equation in **nonconservative** form (eq. 4, force
$-\mathbf B\times(\nabla\times\mathbf B)$), and keeps the induction and
energy equations in conservation form. Energy and magnetic flux are then
exact constants of the motion, momentum is conserved only to truncation
error, and the force has no component along $\mathbf B$ for any
$\nabla\cdot\mathbf B$ (p. 429).

A Poisson correction ($\nabla^2\phi + \nabla\cdot\mathbf B = 0$,
$\mathbf B' = \mathbf B + \nabla\phi$) is named in one sentence as an
alternative (p. 428) and set aside: "one can eliminate the parallel force
without having to solve a potential problem". It is stated in continuous
form only, with no discrete operators, boundary conditions, solver or test.

The evidence is one equilibrium (uniform plasma, uniform field) on a 2D
axisymmetric implicit Lagrangian mesh (Figs. 1–2). With conservative
momentum, spurious field-aligned flows invert cells; with nonconservative
momentum the kinetic energy is 1/4000 as large and the mesh stays
undistorted.

# Key claims

1. **The problem** (p. 426, eq. 1). Even very small errors in
   $\nabla\cdot\mathbf B = 0$ cause large errors when the MHD equations are
   in conservation form, because they appear as a force parallel to the
   field. The observation is attributed to Roberts & Potter (1968).
2. **Divergence errors arise at truncation order** (eq. 2):
   $\partial_t(\nabla\cdot\mathbf B) = O(\Delta x^m, \Delta t^n)$,
   $m, n \ge 1$.
3. **With $\nabla\cdot\mathbf B \ne 0$ nothing is conserved** (eqs. 3–5 and
   the unnumbered energy display, p. 427). The induction equation carries a
   $\mathbf u(\nabla\cdot\mathbf B)$ term (eq. 3, attributed to Panofsky &
   Phillips), the momentum equation is $\rho\, d\mathbf u/dt = -\nabla p -
   \mathbf B\times(\nabla\times\mathbf B)$ (eq. 4), and the energy integral
   carries a $-(\mathbf B\cdot\mathbf u)\,\nabla\cdot\mathbf B$ term. Magnetic
   flux, momentum and energy of an isolated system are then not constants
   of the motion.
4. **The conservative force** (eq. 7). When $\nabla\cdot\mathbf B = 0$ the
   force of eq. 4 equals $\mathbf F = \nabla\cdot\{-\tfrac12(\mathbf
   B\cdot\mathbf B)\mathbf I + \mathbf B\mathbf B\}$. Differenced in this
   form, the equations conserve magnetic flux, energy and momentum even when
   $\nabla\cdot\mathbf B \ne 0$.
5. **The parallel force** (eq. 8, attributed to Barnes & Brackbill 1977):
   $$\mathbf F\cdot\mathbf B = (\mathbf B\cdot\mathbf B)\,\nabla\cdot\mathbf B .$$
   The error is a force proportional to $\mathbf B$; it matters more the
   smaller the flow speed is relative to the Alfvén speed (p. 427). In a
   numerical equilibrium $\mathbf B\cdot\nabla p \ne 0$ unless
   $\nabla\cdot\mathbf B = 0$, and "in some instances … no numerical
   equilibrium exists".
   *Compiler check (not in the paper):*
   $\nabla\cdot(\mathbf B\mathbf B - \tfrac12|\mathbf B|^2\mathbf I) =
   (\nabla\times\mathbf B)\times\mathbf B + \mathbf B\,(\nabla\cdot\mathbf
   B)$, so eq. 7 is eq. 4 plus $\mathbf B\,(\nabla\cdot\mathbf B)$, which
   reproduces eq. 8. The adopted cure therefore removes the momentum source
   $\mathbf B\,(\nabla\cdot\mathbf B)$. The paper never writes it as a
   source term.
6. **When conservation form matters** (p. 427). It "may be imperative only
   for high-speed flows where Rankine–Hugoniot conditions across shocks
   would not be satisfied otherwise". For low-speed flows over many transit
   times it "may be inappropriate". Both forms are consistent with the PDE,
   since $\nabla\cdot\mathbf B = O(\Delta x^m, \Delta t^n)$.
7. **Three cures named, one adopted** (pp. 428–429).
   * (a) Formulate MHD "in terms of fluxes for which $\nabla\cdot\mathbf
     B = 0$ automatically": one line, no detail.
   * (b) Solve $\nabla^2\phi + \nabla\cdot\mathbf B = 0$ and set
     $\mathbf B' = \mathbf B + \nabla\phi$: continuous form only, not used.
   * (c) **Adopted:** difference the nonconservative momentum equation (4)
     with the conservative induction equation (9), printed as
     $\partial_t\mathbf B + \nabla\times(\mathbf u\times\mathbf B) = 0$.
8. **Properties of the adopted system** (eq. 10, p. 429). Energy and
   magnetic flux are constants of the motion; momentum is conserved to
   $O(\Delta x^m, \Delta t^n)$; $\mathbf F\cdot\mathbf B = 0$ for all
   $\nabla\cdot\mathbf B$.
9. **Corroboration** (p. 430). In an explicit calculation by Turkel
   (private communication), with leapfrog and Lax–Wendroff differencing,
   "the residual kinetic energy was decreased by $10^3$ when the
   $\nabla\cdot\mathbf B$ error was corrected". How it was corrected is not
   stated. The authors conclude that removing the parallel force "is of
   universal importance in computational magnetohydrodynamics".

# Tests

One equilibrium, two runs (pp. 427–430, Figs. 1–2).
* **Setup.** Uniform plasma in a uniform axial field; 2D axisymmetric
  $(r,z)$ Lagrangian mesh, initially rectilinear, axis on the left
  boundary, $\mathbf u = 0$ on the other three boundaries. Plasma
  β = 1.3 × 10⁻³ (Fig. 1 caption; exponent read as 3 from the scan, the OCR
  gives 8, low confidence). The solver is the implicit method of
  Barnes & Brackbill (1977) and Brackbill (1976), which conserves mass,
  momentum, magnetic flux and energy for all $\nabla\cdot\mathbf B$. The
  figures show a 5×5-cell mesh (counted, not stated).
* **Conservative momentum** (Fig. 1): after 209 steps (160 transit times)
  the vertices are displaced parallel to the field. The flow "has no
  physical cause", eventually inverts cells and stops the calculation,
  although it comes from "rather small errors" in $\nabla\cdot\mathbf B$.
  Velocity: about $2\times10^{-3}$ of the Alfvén speed in the caption,
  "$10^{-2}$ times the Alfven speed" in the text (p. 428).
* **Nonconservative momentum** (Fig. 2): after 171 steps (300 transit
  times) no distortion is visible; the kinetic energy is "only 1/4000 as
  much as it is with the conservative formulation and remaining constant"
  (p. 430).
* No value of $\nabla\cdot\mathbf B$, no convergence study and no shock
  test is reported.

# Notation map

| Brackbill & Barnes | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf B$, $\mathbf u$ | $\mathbf B$, $\mathbf u$ (continuous); $B_h$, $u_h$ | the paper is continuous throughout |
| $\nabla\cdot\mathbf B$ | $\nabla\cdot\mathbf B$; discretely $D_h B_h$ | no discrete divergence stencil is specified |
| $\phi$, $\mathbf B' = \mathbf B + \nabla\phi$ | $\phi_h$, $B_h = B_h^* - G_h\phi_h$ | **sign convention differs** from [projection](/methods/projection-method.md): $\phi_{\mathrm{paper}} = -\phi_h$ |
| $\mathbf B'$ | $B_h$ (corrected), $B_h^*$ (provisional) | |
| $\mathbf F$ (eq. 7) | words: Maxwell-stress force | no registry symbol |
| $\mathbf I$ | $I$ | identity |
| $\mu$ | words | appears only in the energy displays |
| $\Delta x$, $\Delta t$; orders $m$, $n$ | $h$, $\Delta t$; orders in words | **collision:** registry superscript $n$ is the time level |

# Pages created or updated

* Updated [Exact discrete divergence](/properties/exact-discrete-divergence.md): the primary statement of the parallel force (eq. 8), its scope, and the paper's cure.
* Updated [Projection method](/methods/projection-method.md): what the paper says about the Poisson correction, and who attributes the MHD projection to it.
* Updated [GLM divergence cleaning](/methods/glm-divergence-cleaning.md): the same qualification on the "Brackbill–Barnes" label of the elliptic member.
* Updated [Eight-wave formulation](/methods/eight-wave.md): the nonconservative momentum equation as the lineage Powell (1994) cites.

# Citations

1. `~/papers/mosaic/div-free-amr/1980-JCP-Brackbill-1010160021-99918090079-0.pdf`.
   * **Version read.** The publisher's version of record, a 5-page scan
     (Acrobat Capture 2003). Received 31 October 1978, revised 22 May 1979.
     The byline is printed at the end, p. 430.
   * **Identity.** doi:10.1016/0021-9991(80)90079-0, checked on Crossref:
     title and authors match; vol. 35, issue 3, pp. 426–430, issued May
     1980.
   * **How it was read.** The OCR text layer garbles every equation. All
     five pages were rendered at 130 dpi and read visually; the Fig. 1
     caption was also read at 300 and 600 dpi.
   * **Recorded as printed.**
     * Eqs. 3 and 9 print "$+\nabla\times(\mathbf u\times\mathbf B)$"; ideal
       MHD has the opposite sign. Not corrected.
     * The energy display on p. 427 carries no visible number (the text
       jumps from eq. 5 to eq. 7); its bracket structure is ambiguous and it
       is not reproduced.
     * Eq. 10 prints $-(p + \tfrac12\mathbf B\cdot\mathbf B/\mu)$ without the
       trailing $\mathbf u$ of the p. 427 display; $\mu$ appears only in the
       energy displays.
     * Fig. 1: the caption velocity ($2\times10^{-3}$ of the Alfvén speed)
       disagrees with the text ($10^{-2}$); both caption exponents are read
       from the scan with low confidence.
   * **Reference list.** 5 entries, all merged; none prints a DOI and only
     the book (Panofsky & Phillips) prints a title. The bibliography key
     `brackbill-1980` was renamed `brackbill-barnes-1980` to match this
     page. The bibliography holds 3654 entries after this batch.
