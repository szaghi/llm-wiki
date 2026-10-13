---
type: Source
title: "Balsara & Spicer (1999) — A staggered mesh algorithm using high order Godunov fluxes to ensure solenoidal magnetic fields in MHD simulations"
description: "The primary source of flux-CT: edge EMFs as signed four-face averages of a Godunov scheme's upwind magnetic fluxes, a discrete-Stokes face update, an optional energy correction for low-beta positivity, and a shock-switched directional variant; introduces the MHD rotor test."
resource: "doi:10.1006/jcph.1998.6153"
source_kind: paper
authors: [Balsara D.S., Spicer D.S.]
year: 1999
venue: "J. Comput. Phys. 149:270-292"
local_file: "/home/stefano/papers/mosaic/div-free-amr/1999-JCP-Balsara-101006jcph19986153.pdf"
tags: [constrained-transport, godunov, shock-capturing, staggered, mhd, positivity]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper builds a [constrained-transport](/methods/constrained-transport.md)
update of the magnetic field inside a second-order Godunov MHD scheme. It
exploits a "duality" between the magnetic components of the Godunov face
fluxes and the electric field (§2.1, eqs. 4–6).
* The face-normal field lives at face centres as an area-weighted average;
  the electric field lives at edge centres.
* Each edge EMF is the signed arithmetic average of four time-centred,
  dimension-by-dimension upwinded face fluxes (eqs. 7–9).
* Faces are updated by a discrete Stokes theorem (eqs. 13–15).
* A cell-centred field is also advanced by the Godunov scheme. An optional
  final step replaces its magnetic energy with that of the face-averaged
  field (eq. 16), to protect pressure positivity at low $\beta$.
* A variant (§2.2, eqs. 17–26) weights the $x$- and $y$-flux contributions
  by the local pressure-jump direction where two shock switches fire. It is
  aimed at standing grid-aligned magnetosonic shocks.

The tests are a rotor (new here, with an erratum correcting its
parameters), a strong low-$\beta$ blast and an oblique Alfvén wave. The
claim is that staggering costs nothing in robustness or phase accuracy
compared with a cell-centred Godunov scheme with divergence cleaning. This
is the scheme catalogued as flux-CT by [Tóth (2000)](/sources/toth-2000.md)
and used as "SM" by [Balsara & Kim (2004)](/sources/balsara-kim-2004.md).

# Key claims

1. **Collocation** (§2.1, Fig. 1). "The three components of the magnetic
   field are collocated at the centers of the zone faces to which they are
   orthogonal." The field "is to be treated as an area-weighted average on
   the zone face", a "strict analogue" of volume averages. "The electric
   fields are collocated at zone edges"; their edge line integral is the EMF.
   In registry terms $B_h \in V_h^2$, $E_h \in V_h^1$
   ([staggered grid](/definitions/staggered-grid.md)).
2. **Flux–field duality** (eqs. 3–6). With ideal Ohm's law, the magnetic
   components of the $x$-, $y$- and $z$-fluxes of the eight-component
   conservative system are $(0,-E_z,E_y)$, $(E_z,0,-E_x)$ and
   $(-E_y,E_x,0)$ (eq. 4), whence three symmetries between flux components
   (eq. 6). A Godunov scheme therefore already computes upwinded
   electric-field values at face centres.
3. **Edge EMF as a signed four-flux average** (eqs. 7–9; checked on the
   page image). In 2D registry form, eq. 9 is
   $$E_h\big|_{j+\frac12,k+\frac12} = \tfrac14\left(-f^{x,*}_{j+\frac12,k} - f^{x,*}_{j+\frac12,k+1} + f^{y,*}_{j,k+\frac12} + f^{y,*}_{j+1,k+\frac12}\right),$$
   the plain average $\mathcal E^{\circ}$ ([notation](/notation.md)); eqs. 7–8
   are the other two edge orientations in 3D. The fluxes are second order
   in space and time-centred at $t^{n+1/2}$. The formulas hold for uniform
   zoning; on varying zone sizes "the averaging should be viewed as a
   reconstruction step" (pp. 275–276). The authors call this "the most
   compact second order accurate representation" of the edge fields (p. 276).
4. **Dissipation claim** (p. 276): "the electric field is not a quantity that
   we evolve in time. As a result, the interpolation of flux components ...
   does not introduce any significant level of numerical diffusion in the
   time evolution of the magnetic field." No analysis or test of this
   statement is given ([flux-CT](/methods/flux-ct.md) records the later
   qualification).
5. **Face update by discrete Stokes** (eqs. 13–15; checked on the page
   image). Each face value changes by $-\Delta t/A$ times the signed sum of
   edge-length-weighted edge EMFs around the face, with non-uniform edge
   lengths and face areas allowed. In registry terms
   $B_h^{n+1} = B_h^n - \Delta t\, C_h E_h^{n+1/2}$; the signs were checked
   against $\partial_t \mathbf B = -\nabla\times\mathbf E$ (eq. 2).
6. **No divergence proof or diagnostic.** The paper never writes out that
   the discrete divergence is constant. It asserts it from "a discrete
   version of Stokes' theorem" (pp. 273, 277) and from the prior literature.
   The wording is inconsistent: the abstract says "divergence-free up to the
   computer's round-off error" and §2.2 "to machine accuracy", but §4
   (p. 290) says "strictly solenoidal up to discretization error". No test
   reports a divergence measure of the CT scheme.
7. **Coupling to the Godunov scheme** (§2.1, steps 1–6, eqs. 10–12, 16).
   The base scheme is a dimensionally swept predictor–corrector scheme
   (Balsara 1998, refs. 12–13).
   * (1) Interpolate the face field to cell centres (second order).
   * (2)–(4) $x$-, $y$- and $z$-sweeps update all eight cell-centred
     variables (eqs. 10–12) and accumulate flux contributions into the edge
     EMFs by eqs. 7–9.
   * (5) Update the face field by eqs. 13–15.
   * (6) Two cell-centred fields now exist: the one advanced by the Godunov
     fluxes and the average of the new face field. They differ by "the order
     of magnitude of the discretization error", which at low $\beta$ "can be
     substantial enough to cause the pressure to become negative". The
     total energy is corrected by the difference of the two magnetic
     energies (eq. 16).
   Step 6 is "an optional step". It costs "a slight loss of total energy
   conservation at the level of discretization error"; "several real world
   applications and several test problems" ran without it with no pressure
   problem; it is "very useful" for "very low $\beta$ plasmas" (p. 278).
   For an unsplit Godunov scheme steps 2–4 collapse into one (p. 278); for
   multi-stage (Shu–Osher) schemes eqs. 7–9 apply at each stage (p. 276).
   Above second order, eqs. 7–9 must change; eqs. 13–15 stay valid for
   finite-difference schemes, while finite-volume schemes need a Simpson-rule
   edge quadrature, deferred to later work (p. 278).
8. **Shock-switched variant** (§2.2, eqs. 17–26). For a magnetosonic shock
   moving along $x$, the edge EMF is better taken from the two $x$-face
   fluxes alone (eq. 17); along $y$, from the two $y$-face fluxes (eq. 18).
   * Switch 1: the summed undivided pressure jumps in $x$ and $y$ over the
     four cells exceed $0.5$ times their minimum pressure (eq. 19).
   * Switch 2: the undivided velocity divergence is more negative than
     $-0.1$ times the minimum of a fast-speed upper bound (eqs. 20–24).
   * If both fire, the edge EMF is a convex combination of the $x$-only and
     $y$-only averages, weighted by the share of the $x$ pressure jump in the
     total (eqs. 25–26); otherwise the weight is $\tfrac12$ and eq. 9 is
     recovered.
   Upwinding of entropy and torsional Alfvén waves is deliberately not
   attempted (p. 280). On all tests, which have moving shocks, the variant
   gives "practically identical" results; it is expected to matter for
   standing grid-aligned shocks (p. 279, §4). No such test is shown.
9. **Uncleaned collocated Godunov fails** (§3.1, Fig. 3e; §4). On the rotor,
   the undivided $D_h B_h / |B_h|$ of an uncleaned cell-centred scheme ranges
   from $-0.66$ to $0.66$ and corrupts the rotor boundary; the authors state
   that higher resolution "will not prevent the magnetic monopoles from
   forming". Strong shocks moving fast across the mesh do not show the
   damage (§3.2, p. 285). The divergence stencil is not specified.
10. **Weak-field limit** (§4): with vanishing field "the scheme reduces
    exactly to a traditional higher order Godunov scheme".
11. **History as the authors give it** (§1). The staggered "magnetic field
    transport algorithm" based on Stokes' theorem "was first proposed by Yee
    [3]" for electromagnetic fields; Brecht et al. (1981) combined it with an
    FCT limiter; Evans and Hawley "applied the hybrid scheme utilized by
    Brecht et al. to an artificial viscosity based scheme, coining the term
    'constrained transport'"; DeVore applied it to FCT; Stone and Norman
    used characteristics for the Alfvén waves. Dai and Woodward's staggered
    scheme interpolates zone averages to edges rather than using upwinded
    fluxes (pp. 272–273).

# Tests

* **Rotor** (§3.1, Figs. 2–3). Unit square, $400\times400$, Courant number
  0.8. As printed: ambient density 1, pressure 1, at rest; rotor density 10
  for $r<0.1$, tapering linearly to 1 at $r=0.115$; toroidal speed 2 at
  $r=0.1$, tapering to 0 at $r=0.115$; $\gamma = 1.4$; field 5 along $x$.
  Credited to Brackbill. **Erratum** (J. Comput. Phys. 153:671): the figures
  were run with pressure 0.5, $\gamma = 5/3$, rotor speed 1 and field 2.5;
  the printed parameters "also produce an interesting rotor problem but at
  earlier times". Findings: the §2.1 and §2.2 schemes agree; a cell-centred
  scheme with cleaning "looks just like" the CT run; without cleaning it
  fails (claim 9). Orszag–Tang was also run, "comparable" to cleaned runs,
  not shown.
* **Low-$\beta$ blast** (§3.2, Fig. 4, $t=0.01$). Unit square,
  $200\times200$; density 1; pressure 0.1, and 1000 for $r<0.1$;
  $\gamma=1.4$; field 100 along $x$ (Gaussian units, so ambient
  $\beta = 8\pi\cdot0.1/100^2 \approx 2.5\cdot10^{-4}$, compiler
  arithmetic). Results "extraordinarily similar" to the cleaned cell-centred
  scheme; the §2.2 variant identical; a fixed one-sided weight gave "only
  the slightest degradation". Whether eq. 16 was used is not stated. This is
  the "Balsara–Spicer" blast of later sources.
* **Oblique Alfvén wave** (§3.3, Figs. 5–6; suggested by D. Barnes).
  Periodic $[0,6]^2$ at $30^2$, $60^2$, $120^2$; density and pressure 1,
  $\gamma = 1.4$, field 1 along $x$; propagation at $\tan^{-1}6 =
  80.5376°$ to the field, $V_A = 0.046376$, amplitude 0.2 (eqs. 27–29);
  run to $t = 131.161$. With 5, 10 and 20 zones per $x$-wavelength: amplitude
  loss; amplitude right, phase wrong; both captured. CT comparable to the
  cell-centred scheme, "very slight improvement" at higher resolution. No
  error norms or convergence rates.

No divergence measure of the CT scheme is reported in any test.

# Notation map

| Balsara & Spicer | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| face-centred $B_{x,i+1/2,j,k}$ etc. | $B_h \in V_h^2$ | area-weighted face average |
| $\mathbf B_c$ (Godunov-advanced, cell-centred) | $B_h^{*}$ | a second, provisional cell-centred field |
| $\mathbf B_{fc}$ | words: cell average of $B_h$ | no registry symbol needed |
| edge $E_x, E_y, E_z$ | $E_h \in V_h^1$ | eqs. 7–9 are $\mathcal E^{\circ}$ |
| $F_7, G_6$ (and $F_8, G_8, H_6, H_7$) | $f^{x,*}, f^{y,*}$ | the $z$-flux has no registry symbol; written in words |
| $\psi_{xy}$ (eqs. 25–26) | words | **collision:** $\psi_h$ is the cleaning potential |
| $\mathbf F, \mathbf G, \mathbf H$ | words | **collision:** $H$ is the coarse spacing, $G_h$ the gradient |
| $\mathcal E$ (total energy density) | words | **collision:** $\mathcal E^{\circ,\alpha,c}$ are edge EMFs |
| $A_{i+1/2,j,k}$ (face area) | words | **collision:** $A_h$ is the vector potential |
| $\Delta x, \Delta y, \Delta z$ | $h$ (uniform case) | |
| $\tilde\beta$, $\delta$ (switch thresholds) | words | collide with plasma $\beta$ |
| undivided $\nabla\cdot B$ (Fig. 3e) | $h\,D_h B_h$ | stencil not specified |

# Pages created or updated

* Updated [Flux-CT and the Godunov CT variants](/methods/flux-ct.md): primary source for flux-CT (eqs. 7–9, 13–15, 16, the §2.2 variant), the dissipation claim and its qualification.
* Updated [Constrained transport](/methods/constrained-transport.md): the history as Balsara & Spicer give it.
* Updated [Exact discrete divergence](/properties/exact-discrete-divergence.md): no proof or diagnostic in the primary source; inconsistent wording.
* Updated [Positivity–divergence coupling](/results/positivity-divergence-coupling.md): the energy correction as printed.
* Updated [CT–finite-volume equivalence](/results/ct-finite-volume-equivalence.md): the separately advanced cell-centred field is not the face average.
* Updated [Staggered grid](/definitions/staggered-grid.md): no necessity argument.
* Updated [Tóth (2000)](/sources/toth-2000.md): the BS table remark.

# Citations

1. `~/papers/mosaic/div-free-amr/1999-JCP-Balsara-101006jcph19986153.pdf`.
   * **Version read.** The publisher's final PDF (Academic Press): 23
     article pages, an Elsevier update cover, and the **Erratum**
     (J. Comput. Phys. 153:671, 1999, doi:10.1006/jcph.1999.6318) on the
     last page. Received 8 January 1998, revised 21 September 1998.
   * **Identity.** doi:10.1006/jcph.1998.6153, checked on Crossref: title
     and authors match; vol. 149, issue 2, pp. 270–292, issued March 1999;
     reference count 32.
   * **How it was read.** Text extraction, all sections; eqs. 4, 7–9,
     13–15 and 19–26 checked on rendered page images. Figures 2–6 are used
     through captions and text only.
   * **Recorded as printed.**
     * Divergence wording: round-off (abstract), machine accuracy (§2.2),
       discretization error (§4).
     * p. 275: during a "y-sweep" a version of $-H_6$ is available; $H$ is
       the $z$-flux, so a $z$-sweep is meant.
     * §3.2: "degradation in the propagation of shocks in the z-direction"
       on a 2D $xy$ problem, presumably $y$.
     * §1 names "Evans and Hawley [5]" and "Hawley and Evans [5]" for the
       same reference.
     * The erratum calls the issue "Number 1"; Crossref gives issue 2.
     * The rotor parameters of §3.1 are superseded by the erratum for the
       figures shown.
   * **Reference list.** 32 entries, all merged; Crossref's reference count
     agrees. Evans & Hawley is printed as 1989 with initials C.H. and J.H.
     and was merged into `evans-hawley-1988`, the ingested
     [source](/sources/evans-hawley-1988.md). Brackbill & Barnes is printed
     J. Comput. Phys. 35:462 (the published page is 35:426). Ryu & Jones
     (Astrophys. J. 442:228) and Dai & Woodward (J. Comput. Phys. 115:485)
     were merged into existing entries. The bibliography key `balsara-1999`
     was renamed `balsara-spicer-1999` to match this page. The bibliography
     holds 3639 entries after this batch.
