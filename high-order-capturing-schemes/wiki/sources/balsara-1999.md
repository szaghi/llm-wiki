---
type: Source
title: "Balsara & Spicer (1999) — A staggered mesh algorithm using high order Godunov fluxes to ensure solenoidal magnetic fields in magnetohydrodynamic simulations"
description: "Origin of Balsara–Spicer constrained transport: face-centred magnetic fields updated by discrete Stokes from edge electric fields, each taken as the average of the four adjacent Godunov face fluxes (the flux–electric-field duality), with an optional energy correction for low β and a pressure-switch variant; introduces the MHD rotor, whose printed parameters an erratum corrects."
resource: "doi:10.1006/jcph.1998.6153"
source_kind: paper
authors: [Balsara D.S., Spicer D.S.]
year: 1999
venue: "J. Comput. Phys. 149:270–292"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/1999-JCP-Balsara-101006jcph19986153.pdf"
tags: [mhd, constrained-transport, divergence-free, staggered]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

A staggered-mesh (Yee-type) constrained-transport update of the magnetic
field inside a second-order Godunov MHD scheme. Face-normal field
components are face averages, electric fields live at edge centres, and
Stokes' theorem updates each face from its four edges, so the face-flux
divergence is preserved to round-off. The new idea is a duality: the
induction rows of the upwinded, time-centred Godunov fluxes at face
centres *are* electric-field components, up to sign. Each edge electric
field is therefore the arithmetic average of four face fluxes, instead of
being rebuilt from centred variables as in Evans–Hawley or Dai–Woodward.
An optional energy correction protects the pressure at low β, and a
variant weights the flux pairs by the local pressure-gradient direction at
strong shocks. Three 2D tests are introduced: the MHD rotor, a strong
low-β blast and an oblique Alfvén wave. An erratum appended to the
archived file corrects the rotor parameters. Merged into
[constrained transport](/methods/constrained-transport.md), the
[MHD rotor](/benchmarks/mhd-rotor.md) and the
[MHD blast wave](/benchmarks/mhd-blast-wave.md).

# Key claims

1. **Flux–electric-field duality** (§2.1, eqs. 2–6). With
   $\boldsymbol{\mathcal E} = -\mathbf v\times\mathbf B$ and Gaussian units
   (magnetic pressure $B^2/8\pi$), the induction rows (components 6–8 of
   $(\rho, \rho\mathbf v, E, \mathbf B)$) of the $x$, $y$, $z$ fluxes are
   $(0, -\mathcal E_z, \mathcal E_y)$, $(\mathcal E_z, 0, -\mathcal E_x)$,
   $(-\mathcal E_y, \mathcal E_x, 0)$, so the $x$-flux component 7 is minus
   the $y$-flux component 6, and cyclically (eq. 6).
2. **Edge field as a four-flux average** (eqs. 7–9, read from the page
   image, p. 275):
   $$\bar{\mathcal E}^{n+1/2}_{z;i+1/2,j+1/2,k} = \tfrac14\left[(\hat f_y)_{6;i,j+1/2,k} + (\hat f_y)_{6;i+1,j+1/2,k} - (\hat f_x)_{7;i+1/2,j,k} - (\hat f_x)_{7;i+1/2,j+1,k}\right]$$
   and cyclically, with time-centred, spatially second-order Godunov
   fluxes. Called "the most compact second order accurate representation of
   the electric fields that can be obtained at the zone edges", for uniform
   zoning (non-uniform zoning needs a zone-size-weighted interpolation).
   Because $\boldsymbol{\mathcal E}$ is not an evolved quantity, the
   averaging is claimed to add no "significant level of numerical
   diffusion" (p. 276); asserted, not measured.
3. **Face update by discrete Stokes** (eqs. 13–15, read from the page
   image, p. 277):
   $$\bar B^{n+1}_{x;i+1/2,j,k} = \bar B^n_{x;i+1/2,j,k} - \frac{\Delta t}{h_y h_z}\left(h_z\bar{\mathcal E}^{n+1/2}_{z;i+1/2,j+1/2,k} - h_z\bar{\mathcal E}^{n+1/2}_{z;i+1/2,j-1/2,k} + h_y\bar{\mathcal E}^{n+1/2}_{y;i+1/2,j,k-1/2} - h_y\bar{\mathcal E}^{n+1/2}_{y;i+1/2,j,k+1/2}\right)$$
   and cyclically. The abstract says divergence-free "up to the computer's
   round-off error"; the conclusions say "strictly solenoidal up to
   discretization error". The algebra gives round-off.
4. **Algorithm** (§2.1, steps 1–6). A dimensionally swept
   predictor–corrector TVD scheme (the RIEMANN code); edge fields are
   accumulated over the $x$, $y$, $z$ sweeps; the zone-centred field is also
   evolved by the Godunov scheme; face fields are updated at the end. For an
   unsplit scheme the sweeps collapse into one step; for Shu–Osher
   multi-stage schemes eqs. 7–9 apply at every stage. The method "does not
   depend on dimensional sweeping" (§1).
5. **Energy correction** (step 6, eq. 16, optional). The magnetic energy
   of the Godunov-evolved zone-centred field is replaced, inside $E$, by
   that of the face fields averaged to the zone centre. It costs "a slight
   loss of total energy conservation at the level of discretization error"
   and is motivated by negative pressures in very low-β plasmas
   (pp. 277–278). This is the "Balsara–Spicer energy correction" of later
   sources. Whether it was used in any test is not stated.
6. **Higher order** (p. 278; §1). Above second order eqs. 7–9 must
   change; eqs. 13–15 stay valid for higher-order finite differences, while
   higher-order finite volume needs a Simpson-rule edge integral (deferred
   to a later paper). Extension to FD-ENO and FV-ENO is called trivial,
   not shown.
7. **Pressure-switch variant** (§2.2, eqs. 17–26, page images
   pp. 280–281). Where both a pressure-jump switch (threshold 0.5 of the
   smallest of four neighbouring pressures) and a compression switch
   (undivided divergence of $\mathbf v$ below $-0.1$ times the smallest fast-speed
   bound) are on, the two flux pairs of eq. 9 are weighted by the share of
   the $x$ pressure jump in the total, instead of $\tfrac12$ each. It is
   meant for standing grid-aligned magnetosonic shocks (citing Quirk's
   instability); on every test it gave results "practically identical" to
   the basic scheme and is "more difficult to code". Results are "rather
   insensitive" to the two thresholds.
8. **Divergence errors matter even for higher-order Godunov schemes**
   (§§1, 3.1, 4). Without CT or cleaning the rotor develops "magnetic
   monopoles" where the field lines are most sheared, with
   $2h\,\nabla\cdot\mathbf B/|\mathbf B|$ between $-0.66$ and $0.66$
   (Fig. 3e), and a spurious solution. Higher resolution than $400^2$ "will
   not prevent the magnetic monopoles from forming" (asserted, no
   refinement study). Fast strong shocks do not expose the problem;
   long-lived stationary features do.
9. **Staggering is not less robust with Godunov fluxes** (§§3.2, 4). The
   view that staggered schemes are fragile at shocks is attributed to
   artificial-viscosity experience; with upwinded fluxes the staggered
   scheme matches the zone-centred scheme with cleaning, and with zero
   field it reduces exactly to a higher-order Godunov scheme.
10. **Critique of earlier CT** (§1). Evans–Hawley and Dai–Woodward build
    edge fields from centred or interpolated variables; Stone–Norman (MOC)
    upwind only an Alfvén subsystem. No numerical comparison is shown.
    Projection (Brackbill–Barnes) is called fast with multigrid or FFT but
    not adaptable to all boundary conditions and zonings.

**Tests** (§3; 2D, Gaussian units, second-order split TVD fluxes, Courant
number 0.8; no error norms or cost data; boundary conditions not printed).
1. *Rotor* (§3.1, Figs. 2–3). As printed: unit square, $400^2$; ambient
   $\rho = 1$, $p = 1$, at rest; disc $\rho = 10$ for $r < 0.1$, tapering
   linearly to 1 at $r = 0.115$ (six zones); $\gamma = 1.4$; rigid rotation
   with speed 2 at $r = 0.1$, tapering to 0 at 0.115; uniform $B_x = 5$;
   $t = 0.295$. **Erratum** (J. Comput. Phys. 153:671, 1999): Figs. 2–3
   were run with $p = 0.5$, $\gamma = 5/3$, speed 1 at $r = 0.1$ and
   $B = 2.5$, densities and taper as printed; the printed set "also
   produce[s] an interesting rotor problem but at earlier times". The basic
   and variant schemes agree; the zone-centred scheme without cleaning, at
   $t = 0.317$, is corrupted at the rotor boundary and inside; with
   cleaning it "looks just like Fig. 2". An Orszag–Tang run is called
   "comparable in quality" to cleaned runs, not shown.
2. *Blast* (§3.2, Fig. 4). Unit square, $200^2$; $\rho = 1$; $p = 0.1$,
   and 1000 inside radius 0.1; $\gamma = 1.4$; at rest; $B = 100$ along $x$
   (ambient plasma beta $2.51\times10^{-4}$, compiler's arithmetic);
   $t = 0.01$ in the caption only. Basic CT and the cleaned zone-centred
   scheme are "extraordinarily similar"; even the zone-centred scheme
   without cleaning is "very similar". Forcing the variant's weight to 1
   or 0 everywhere gives only the slightest degradation of shocks along
   one direction (printed "z-direction" for this $xy$ problem, evidently
   $y$).
3. *Oblique Alfvén wave* (§3.3, Figs. 5–6; suggested by D. Barnes).
   Periodic $[0,6]^2$, $30^2$, $60^2$, $120^2$; $\rho = 1$, $p = 1$,
   $\gamma = 1.4$, $B_x = 1$; a linearly polarized wave in $v_z$
   (amplitude 0.2) and $B_z$ (amplitude $0.2\sqrt{4\pi}$, opposite sign),
   propagating at $80.5376°$ to the field with phase speed 0.046376, to
   $t = 131.161$. Staggered and zone-centred schemes are "entirely
   comparable": at 5 zones per $x$-wavelength the amplitude decays, at 10
   the phase is wrong, at 20 both are captured. Not the
   [circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md).
   *Compiler's note (hypothesis):* the paper calls the solution exact,
   but a linearly polarized wave carries a varying magnetic pressure, so
   it is exact only to linear order in the amplitude.

# Notation map

| Balsara & Spicer (1999) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf U$; $\mathbf F$, $\mathbf G$, $\mathbf H$ | $u$; $\mathbf f$, numerical fluxes $\hat f_x$, $\hat f_y$, $\hat f_z$ | directional subscript added on this page |
| $F_7$, $G_6$, $H_6$, … | $(\hat f_x)_7$, $(\hat f_y)_6$, $(\hat f_z)_6$, … | 1-based index into $(\rho, \rho v_x, \rho v_y, \rho v_z, E, B_x, B_y, B_z)$, as $(f^{**}_x)_7$ on the CT page |
| $\mathbf E$ | $\boldsymbol{\mathcal E}$ | paper's $\mathbf E$ is not the energy |
| $\mathcal E$ (total energy density) | $E$ | swapped with respect to the paper |
| $P$ | $p$ | |
| $B_{x,i+1/2,j,k}$, $E_{z,i+1/2,j+1/2,k}$ | $\bar B_{x;i+1/2,j,k}$, $\bar{\mathcal E}_{z;i+1/2,j+1/2,k}$ | |
| $\Delta x$, $\Delta y$, $\Delta z$; $A_{i+1/2,j,k}$ | $h_x$, $h_y$, $h_z$; $h_y h_z$ | |
| $\mathbf B_c$, $\mathbf B_{fc}$ | words | zone-centred and face-averaged fields |
| $\psi_{xy}$, $\tilde\beta$, $\delta$, $C$ | words | collide with $\psi$, $\beta_k$, $\delta_p$ |
| $V_A$ | $c_A$ | phase speed along the wavevector here |
| Courant number | $\nu$ | |

# Pages created or updated

* Updated [Constrained transport](/methods/constrained-transport.md): the origin of Balsara–Spicer CT.
* Updated [MHD rotor](/benchmarks/mhd-rotor.md): origin set-up and erratum; "Tóth's first rotor" and Ding & Wu's set are the printed and the corrected parameters.
* Updated [MHD blast wave](/benchmarks/mhd-blast-wave.md): origin set-up; the 3D version is not in this paper.
* Also cited on [Hyperbolic (GLM) divergence cleaning](/methods/hyperbolic-divergence-cleaning.md).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/1999-JCP-Balsara-101006jcph19986153.pdf`.
   * **Version.** Typeset publisher version (Academic Press), 25 PDF
     pages: the article (23 pages) and, on PDF pp. 24–25, the "Update"
     (erratum), J. Comput. Phys. 153(2):671, August 1999,
     doi:10.1006/jcph.1999.6318.
   * **Identity.** doi:10.1006/jcph.1998.6153 (article ID printed on
     page 1), checked on Crossref: J. Comput. Phys. 149(2):270–292, March
     1999, authors Balsara and Spicer. The erratum, also checked on
     Crossref, calls the original "Volume 149, Number 1"; Crossref gives
     issue 2.
   * **How it was read.** Text extraction; eqs. 7–9, 13–15 and 17–26 and
     Fig. 3 read from the page images. Eq. (4) is garbled in the text
     layer and is reproduced only through eq. (6).
   * **Recorded as printed.** Round-off (abstract) versus discretization
     error (conclusions) for the divergence; "z-direction" in a 2D $xy$
     test; the rotor parameters that the erratum corrects.
   * **Reference list:** 32 entries. Brackbill & Barnes is printed
     35:462 and merged into `brackbill-1980` (35:426); Evans & Hawley,
     printed 1989, is `evans-1988`; Dai & Woodward's JCP paper is
     `dai-1994-b`; van Leer's chapter is `vanleer-1984-b`.
