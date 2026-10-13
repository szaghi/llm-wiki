---
type: Source
title: "Martyushov, Igra & Elperin (2016) — Numerical investigation of shock wave diffraction over a sphere placed in a shock tube"
description: "Euler computation of a fixed 80 mm sphere hit by an M_s = 1.22 shock, with a dimensionally split Harten–Yee TVD scheme on a two-block body-fitted grid, modified to project all stencil increments with the target face's eigenvectors and to fall back to arithmetic means when the Roe sound speed leaves the cell interval; surface pressure and drag histories agree with digitized shock-tube data early (peak C_D 7.55) and qualitatively converge on three grids."
resource: "doi:10.1155/2016/5740435"
source_kind: paper
authors: [Martyushov S., Igra O., Elperin T.]
year: 2016
venue: "Int. J. Aerosp. Eng. 2016:5740435"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2016-IJAeroEng-Martyushov-10115520165740435.pdf"
tags: [benchmark, euler, tvd, eigenvectors, mapped-grid]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

A five-page computation of the unsteady drag on a **fixed** sphere of
80 mm diameter struck head-on by a weak planar shock ($M_s = 1.22$) in a
shock tube, from the computed surface pressure. The model is the inviscid
Euler equations on a moving finite volume, discretized by an explicit,
dimensionally factored version of the Harten–Yee TVD scheme (Yee, Warming
& Harten 1985) with two modifications by Martyushov: an arithmetic-mean
fallback for the Roe state and "pseudocharacteristic" variables, which
project every stencil increment with the eigenvectors of the target face
([characteristic decomposition](/methods/characteristic-decomposition.md)).
The sphere is body-fitted. Surface pressure is compared with Tanno et al.
(2003) at four times and the drag history with Sun et al. (2005), both as
circles digitized from those papers' plots
([shock passing a sphere](/benchmarks/shock-sphere-interaction.md)).

# Key claims

1. **Particle drag from a trajectory** (§1, eqs. 1–3, after Igra and
   Takayama). The equation of motion of a sphere in a gas, with $C_D$,
   the particle Reynolds number and the particle Mach number expressed
   through the recorded acceleration. These relations concern a free
   sphere and are not used in the fixed-sphere computation.
2. **Equations** (§2, eq. 4). Mass, momentum and energy of an "ideal
   nonviscous gas" on a moving finite volume, with the normal flux written
   relative to the velocity of the control-volume boundary. As printed,
   the conserved momentum is $\rho$ times the fluid velocity minus the
   boundary velocity.
3. **Time stepping** (§2). The explicit step operator is factored into a
   symmetric product of operators in the three index directions
   (Strang-type splitting). No order and no CFL number are stated; the
   title of Martyushov's 1996 paper calls the algorithm second order.
4. **Spatial flux** (§2). Face fluxes from "the finite difference scheme
   suggested by Yee et al.", called Harten's scheme in the text, in "a
   slightly improved version":
   * *Roe sound-speed fallback.* Following Vinokur (1989), the Roe
     procedure implies a formula for the face sound speed (the formula is
     not printed) that "may yield results outside the interval
     $[c_j, c_{j+1}]$", which makes the eigenvectors incorrect and can
     flip eigenvalue signs. Where that happens, the Roe interpolation at
     the face "is replaced by a half sum of the corresponding variables in
     the considered cells".
   * *Pseudocharacteristic variables.* The characteristic variables at
     face $j+1/2$ use data from cells $j-2$ to $j+2$. Instead of
     projecting the increments across faces $j-1/2$, $j+1/2$ and $j+3/2$
     each with its own face's left eigenvectors, the scheme projects all
     three with the left eigenvectors of face $j+1/2$, "to reduce the
     influence of the geometric parameters of distant cells". The 1D
     validation is referred to Il'in and Timofeev (1991), not shown.
5. **Grid** (§2, Fig. 1). A body-fitted structured grid of two blocks
   (upstream and downstream of the sphere) from a Thompson-type elliptic
   (Poisson) generator. Block-interface fluxes use the main-scheme
   formulas with Roe states from the two blocks. Whether the computation
   is axisymmetric or 3D is not stated; the grids are two-dimensional in
   appearance and the equations are written in 3D.
6. **Free-sphere formulation** (§3, eq. 5). A moving-grid update of the
   sphere's position and velocity from the axial pressure force is stated
   but not run ("future paper").
7. **Surface pressure versus Tanno et al.** (§3, Fig. 3). The pressure
   coefficient, normalized by the stagnation-point overpressure, agrees
   "very good" at 140 and 208 µs after shock arrival; at 296 and 380 µs
   the experiment is higher on the rear, which the authors attribute to
   the support strut at the trailing edge, not modelled.
8. **Drag versus Sun et al.** (§3, Fig. 4). $C_D$ is based on the
   post-shock density and speed; time is normalized by the radius over
   293.4 m/s, the square root of the gas constant times the pre-shock
   temperature. Agreement is "good". The
   drag is very large during diffraction (normalized time below 1.6),
   with **peak $C_D = 7.55$**, "significantly higher" than in a similar
   shock-free flow. For normalized time above 2.4, $C_D = -0.16$, which
   the authors attribute to shocks reflected from the tube walls hitting
   the rear of a large sphere in a small tube; then $C_D$ rises toward its
   steady value.
9. **Grid study** (§4, Appendix, Figs. 5–6). Grids of 70×200, 120×300 and
   200×500 points; "the solution quickly converged to a unique result".
   No error norm; the three drag curves overlap at the peak and differ
   slightly in the negative phase (finest lowest).
10. **Validity** (§5). The agreement is taken to support the inviscid
    model; for a free sphere the flow lasts longer and viscous effects
    "cannot be ignored any longer".

**Tests.** One configuration: fixed sphere, $D = 80$ mm, $M_s = 1.22$,
pre-shock pressure 101 kPa and temperature 300 K. The gas (air) and
$\gamma$ are not stated; 293.4 m/s is consistent with a gas constant of
287 J/(kg K) at 300 K (compiler's arithmetic). The initial shock distance, the
computational tube cross-section and the domain length are not printed;
tube-wall reflections are present, so the walls are modelled. Outputs:
isopycnics at 208 µs (Fig. 2, qualitative), surface pressure at four
times (Fig. 3), the drag history (Fig. 4) and the grid study (Figs. 5–6).
No error measure anywhere.

# Notation map

| Martyushov et al. (2016) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\vec U = (\rho, \vec m, e)$ | $u$ | conserved state; $\vec U_g$, $\vec U_p$, $U_0$ are velocities in the same paper |
| $\rho$, $\vec u$, $P$, $e$, $\gamma$ | $\rho$, $\mathbf v$, $p$, $E$, $\gamma$ | |
| $\vec v$, $v_n$ | words | control-volume (grid) velocity; the registry's $\mathbf v$ is the fluid velocity |
| $u_n$ | $v_n$ | normal velocity |
| $j$, $j+1/2$ | $i$, $i+1/2$ | cell and face indices |
| $c$, $c_{j+1/2}$ | $c$ | sound speed; Roe-averaged at the face |
| $L_{1/2}$ | $L$ at $x_{i+1/2}$, rows $\ell^{(p)}$ | |
| $\alpha_{-1/2}$, $\alpha_{1/2}$, $\alpha_{3/2}$ | $\ell^{(p)}_{i+1/2}(u_{i+k+1} - u_{i+k})$, $k = -1, 0, 1$ (all three projected with the eigenvectors of face $i+1/2$) | $\alpha$ is the Lax–Friedrichs speed; the paper also uses $\alpha$ for the sphere's acceleration and for the surface angle |
| $\Delta U_{j+1/2}$ | $u_{i+1} - u_i$ | |
| $M_{\mathrm{shock}}$ | $M_s$ | |
| $r$, $D_p$ | $D/2$, $D$ | $r$ is the stencil count |
| $C_D$ | $C_D$ | same definition |
| $C_P$, $P_0$, $P_1$ | words | pressure coefficient over the stagnation-point overpressure; no registry symbol |
| $\rho_0$, $U_0$; $P_0$, $T_0$ | post-shock; pre-shock | subscript 0 means post-shock for $\rho_0$, $U_0$ and pre-shock for $P_0$, $T_0$ |
| $R$ | words | gas constant; $R$ is the right-eigenvector matrix |
| $T$, $\Delta t$ | $T$, $\Delta t$ | |
| $\mathrm{Re}_p$, $M_p$ | $\mathrm{Re}$, words | particle Reynolds and Mach numbers |

# Pages created or updated

* Contributed to [Shock passing a sphere](/benchmarks/shock-sphere-interaction.md) (the Euler run, surface pressure and drag against experiment, the grid study).
* Updated [Local characteristic decomposition](/methods/characteristic-decomposition.md)
  (batch-12 block: eigenvectors frozen at the target face in a TVD
  scheme, arithmetic-mean fallback).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2016-IJAeroEng-Martyushov-10115520165740435.pdf`.
   * **Version.** The published Hindawi article (open access, CC BY),
     5 pages; received 16 December 2015, accepted 19 June 2016.
   * **Identity.** doi:10.1155/2016/5740435, printed on page 1 and checked
     on Crossref: International Journal of Aerospace Engineering 2016,
     pages 1–5, authors Martyushov, Igra, Elperin. Crossref has no
     article-number field; the article ID 5740435 is printed.
   * **How it was read.** Text extraction, all sections; eqs. 1–5 and the
     missing Vinokur formula checked on the page images.
   * **Recorded as printed.** Vinokur's sound-speed formula is announced
     ("the following formula") but not printed. The right-hand sides of
     eqs. 2–3 are multi-line fractions and are not reproduced. The text's
     peak $C_D = 7.55$ against a Fig. 6 axis that tops at 7.50 (the curve
     peaks near 7.5); the text's $C_D = -0.16$ for normalized time above
     2.4 against Fig. 4, where the curve stays near zero with a dip around
     4.5. The Fig. 3 panels use different tick labels. Subscript 0 means
     post-shock for density and speed and pre-shock for pressure and
     temperature. The experimental circles of Figs. 3–4 are digitized from
     the cited papers, not original data. §1 places Tanno's sphere on a
     strut in a 150 × 500 mm tube, while Tanno's title says "suspended in a
     vertical shock tube"; not checkable here.
   * **Reference list:** 11 printed entries; the Crossref deposit lists 9.
     Suzuki et al. (2005, Meas. Sci. Technol. 16:2431) is keyed
     `suzuki-2005-b`, because `suzuki-2005` is a different work.
