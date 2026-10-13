---
type: Source
title: "Poinsot & Lele (1992) — Boundary conditions for direct simulations of compressible viscous flows"
description: "Introduces NSCBC: boundary values are advanced by the conservation equations with their normal-derivative terms written through characteristic wave amplitudes, outgoing ones from one-sided differences and incoming ones from LODI relations matched to the physical conditions, with no extrapolation; a partially reflecting outflow relaxation fixes the mean-pressure drift of perfectly non-reflecting conditions, and tests with a sixth-order compact scheme show steady states and no spurious upstream waves where an extrapolation outlet fails."
resource: "doi:10.1016/0021-9991(92)90046-2"
source_kind: paper
authors: [Poinsot T.J., Lele S.K.]
year: 1992
venue: "J. Comput. Phys. 101:104–129"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/1992-JCP-Poinsot-1010160021-99919290046-2.pdf"
tags: [boundary-treatment, navier-stokes, finite-difference, compact-scheme]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper introduces Navier–Stokes characteristic boundary conditions
(NSCBC) for low-dissipation, high-order direct simulation of compressible
flow, extending Thompson's characteristic Euler conditions. At a
boundary, the normal-derivative terms of the conservation equations are
written through wave-amplitude variations; outgoing ones come from
one-sided interior differences, incoming ones from local one-dimensional
inviscid (LODI) relations that encode the physical conditions, and the
boundary values are advanced with the remaining equations, so no
variable is extrapolated. Viscous conditions enter only through the
viscous terms. A perfectly non-reflecting outflow makes the mean pressure
drift; a relaxation toward a target pressure removes the drift. Three 2D
tests compare NSCBC with an extrapolation outlet. No well-posedness proof
is given. Merged into
[Navier–Stokes characteristic boundary conditions](/methods/characteristic-boundary-conditions.md).

# Key claims

1. **Physical and soft conditions** (§2.1, Table I): Euler / Navier–Stokes
   counts for well-posedness in 3D are 5/5 (supersonic inflow), 4/5
   (subsonic inflow), 0/4 (supersonic outflow), 1/4 (subsonic outflow).
2. **Extrapolation over-specifies** (§2.1): it "acts as an additional
   physical condition"; soft values must come from the conservation
   equations on the boundary. Design criterion: no extrapolation (§1).
3. **One-sided accuracy** (§§2.1–2.2): one order below the scheme does
   not reduce the overall order (attributed to Gustafsson); in the code,
   third-order one-sided derivatives make the scheme fourth order.
4. **Characteristic form and LODI** (§§2.2–2.3, eqs. 9–37); the classical
   non-reflecting condition is the special case $\mathscr L_1 = 0$
   (eq. 37).
5. **Three-step procedure** (§2.4, Table II) and the condition counts
   against Strikwerda's (§2.5, Tables III–IV): two mismatches, one of them
   unexplained; the only inflow set proved well-posed for Navier–Stokes
   was unstable with NSCBC.
6. **Edges and corners** need a transverse LODI system with a centred
   low-dissipation scheme (§2.6).
7. **Perfect non-reflection is ill-posed in general** (§3.2); relaxation
   $\mathscr L_1 = K(p - p_\infty)$, $K = \sigma(1 - \mathcal M^2)c/L$,
   $\sigma = 0.25$ (eq. 40).
8. **Spurious "q" waves** (§5, after Vichnevetsky) travel upstream even in
   supersonic flow and feed back from the inlet; supersonic outlets are
   not a general solution.

**Tests** (§§4–6, Table V; Lele's sixth-order compact scheme, third-order
explicit Runge–Kutta; NSCBC at inlets and walls; outlet varied between an
extrapolation reference after Rudy–Strikwerda and three NSCBC variants):
a steady ducted shear layer (41×41, Re 2000), a vortex through a Mach 1.1
outlet (81×81, Re 10 000), and low-Re Poiseuille flow (121×81, Re 15).
Only the partially reflecting NSCBC is non-reflecting and drift-free
everywhere (Table VI). Three further configurations (free shear layers,
a 1D acoustic pulse) are reported only in a CTR report.

# Notation map

| Poinsot & Lele (1992) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u_i$, $m_i = \rho u_i$ | $v_x, v_y, v_z$ (components of $\mathbf v$), $\rho v_x$, … | $u$ is the conserved state; $x_1$ is the boundary normal $x$ |
| $\rho E$ | $E$ | the symbol list calls $E$ specific internal energy, but eq. 4 makes it specific total energy |
| $p$, $\rho$, $\gamma$, $c$, $T$ | same | $c^2 = \gamma p/\rho$ (eq. 18) |
| $\lambda_1, \dots, \lambda_5$ | $\lambda^{(1)}, \dots, \lambda^{(5)}$ | $v_x - c$, $v_x$, $v_x$, $v_x$, $v_x + c$ |
| $\mathscr L_i$ | $\mathscr L^{(p)}$ (registered, batch 11) | never $\mathcal L$, the spatial operator |
| $d_1, \dots, d_5$ | words | collide with $d_k$ and $\mathbf d^{\mathrm{HLL}}$ |
| $K$, $\sigma$, $\sigma'$ | $K_{\mathrm{NR}}$, $\sigma_{\mathrm{NR}}$ (registered, batch 11), words | collide with the degree $K$ and the Hu–Adams–Shu $\sigma$ |
| $\mathcal M$ | $\mathrm{Ma}$, $\mathrm{Ma}_{\max}$ | |
| $p_\infty$ | $p_\infty$ (registered, batch 11) | target far-field pressure |
| $L$, $l$ | $L_x$ (registered, batch 11), words | $L$ is the left-eigenvector matrix |
| $\tau_{ij}$, $q_i$ | $\boldsymbol\tau$, $\mathbf q$ | |
| $\mu$, $\nu$, $\lambda$ (conductivity) | words | $\nu$ is the CFL number, $\lambda$ the eigenvalues |
| $s$, $h$ (entropy, enthalpy) | words | $s$ is the stage count, $h$ the spacing |
| $A_1$, $A_p$, $A_q$; $u_g$, $k_g$ | words | amplitudes and group velocity of the spurious waves |
| $\psi$, $C$, $R_c$, $\theta$ | words | vortex and shear-layer parameters |

# Pages created or updated

* Created [Navier–Stokes characteristic boundary conditions](/methods/characteristic-boundary-conditions.md).
* Updated [Inverse Lax–Wendroff](/methods/inverse-lax-wendroff.md) and [Weighted extrapolation](/methods/weighted-extrapolation.md) (scope of outflow extrapolation).
* Proposed for the [notation registry](/notation.md): $\mathscr L^{(p)}$, $K_{\mathrm{NR}}$, $\sigma_{\mathrm{NR}}$, $p_\infty$, $L_x$.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/1992-JCP-Poinsot-1010160021-99919290046-2.pdf`.
   * **Version.** The published journal article, 26 pages (received
     23 February 1990, revised 12 April 1991), a scan with an OCR layer.
   * **Identity.** doi:10.1016/0021-9991(92)90046-2 (PDF metadata),
     checked on Crossref: J. Comput. Phys. 101(1):104–129, July 1992,
     Poinsot T.J. and Lele S.K.; it agrees with page 1. The bibliography
     already held `poinsot-1992` (cited by `bernardini-2021` and
     `pirozzoli-2002`) under the title "… compressible viscous reacting
     flows"; corrected from Crossref and page 1 to "… compressible viscous
     flows".
   * **How it was read.** The OCR layer garbles every equation and table.
     All equations and Tables I–IV were read from page images; the text
     and Table VI come from the OCR layer, checked against the images.
     Figures were read qualitatively; numbers are quoted only where the
     text states them. Eqs. 29–36 were listed, not transcribed.
   * **Recorded as printed.** Eq. 14 (primitive-variable column) prints a
     $\mu$ in the $d_2$ entry where $u_1$ is dimensionally required; only
     the $\mathscr L$ form is used. Citation-number slips: "Engquist and
     Majda [9]" ([9] is Higdon), "Gustafsson [37]" ([37] is Liu),
     "Rutland and Ferziger [25]" ([25] is Gresho & Sani); "Table IV" for
     Table III (p. 114); "Section 3.5" for the isothermal walls of §3.4
     (p. 124); "Section 4.1" (p. 115) does not exist; the section plan in
     §1 does not match the body (§7 is the conclusions). The OCR drops the
     minus sign of the vortex constant (eq. 48), read from the image.
   * **Reference list:** 40 entries; no article titles and no DOIs are
     printed. Thompson [1] cites JCP 68:1 (1987) and an unnamed submitted
     paper. Lele [2] ("submitted; AIAA Paper 89-0374") is keyed
     `lele-1989`, year from the paper number, plausibly the precursor of
     `lele-1992`, unverified. Gustafsson & Oliger, "Math. Comput. 26, 649
     (1982)", prints the volume and page of the 1972
     Gustafsson–Kreiss–Sundström paper; kept as `gustafsson-1982` with the
     identity unresolved. `vichnevetsky-1986` (with Pariser) and
     `vichnevetsky-1986-b` (sole author) are distinct works.
     `vichnevetsky-1982` and `thompson-1987` were already in the
     bibliography.
