---
type: Source
title: "Brahmi, Hadjadj, Soni & Chaudhuri (2020b) — Analysis of shock-wave diffraction over double cylindrical wedges. Part II: Vorticity generation"
description: "Part II of the double-concave-arc study (same code, grids and M_s 1.6–4.5): grid-insensitive circulation growing linearly in time with M_s-dependent rate plateaus, a term-by-term vorticity balance in which viscous diffusion outweighs baroclinicity for M_s ≤ 2.5 and the reverse for M_s ≥ 3.5, and up to 90% dynamic-impulse attenuation by the first arc; no experiment."
resource: "doi:10.1016/j.actaastro.2020.02.017"
source_kind: paper
authors: [Brahmi N., Hadjadj A., Soni V., Chaudhuri A.]
year: 2020
venue: "Acta Astronaut. 172:140–150"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2020-ActaAstronaut-Brahmi-101016jactaastro202002017.pdf"
tags: [benchmark, immersed-boundary, navier-stokes, weno]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The second part of the study of a shock over two concave circular arcs
([Brahmi et al. (2020)](/sources/brahmi-2020.md), cited here as its
reference [20]): the same configuration (radius 50 mm, initial wall
angles 75°), the same $M_s = 1.6$–4.5, the same in-house code (WENO5,
fourth-order central viscous fluxes, RK3, adaptive multiresolution,
ray-traced immersed boundary on a Cartesian grid) and the same five
grids. Its contribution is diagnostic: circulation histories, a
term-by-term vorticity balance, pressure impulses at two probes, and an
accumulated-error "reliability" estimate after Smirnov et al. There is no
experiment. The page-1 title omits the word "concave" that Part I
carries. Merged into
[shock reflection from double concave wedges](/benchmarks/double-concave-shock-reflection.md).

# Key claims

1. **Equations and numerics** (§2, eqs. 1–5). As in Part I, including the
   eq. 3 misprint (divergence of $\rho\mathbf v$ for that of
   $p\mathbf v$). The Riemann solver or flux splitting and the IB
   algorithm are not stated; the IB is cited to Chaudhuri et al. (2011,
   2012).
2. **Grid-insensitive circulation** (§4.1, Table 1, Figs. 3–4). On G0–G4
   at $M_s = 1.6$ the primary-vortex topology changes with resolution
   ($t = 150$ µs), but $\Gamma(t)$ and $\Gamma/t$ do not; $\Gamma$ grows
   linearly in time.
3. **Circulation-rate plateaus** (§4.1, eqs. 6–8, Fig. 5b). $\Gamma/t$,
   scaled by the specific gas constant (287 J kg⁻¹ K⁻¹) times
   $T = 300$ K, tends to 1.78, 3.79, 5.72, 11.42 and 18.73 for
   $M_s = 1.6$, 2.0, 2.5, 3.5 and 4.5 (G4). Circulation is integrated over
   the whole domain. This agrees qualitatively with Sun & Takayama.
4. **Viscous onset** (§4.1). Vorticity production starts in the wall
   boundary layer before the shock diffracts ($t = 12$ µs at
   $M_s = 2.0$), consistent with Tseng & Yang.
5. **Vorticity balance** (§4.2, eq. 9, Figs. 7–9). The dilatation term
   dominates; it and the unsteady and convective parts are almost
   constant in time and grow with $M_s$. Viscous diffusion is "quite
   important" against baroclinicity for $M_s \le 2.5$, inverted for
   $M_s \ge 3.5$ (claimed "for the first time").
6. **Impulses** (§4.3, eqs. 10–12, Figs. 10–13). Probes at $(0.26, 1.6)$
   and $(1.22, 0.86)$ arc radii, at the starts of the two arcs. The first
   arc cuts the dynamic-pressure impulse by up to 90% ($M_s = 2.5$) and
   the static-pressure impulse by up to 75% ($M_s = 4.5$); the peak
   overpressure is not reduced (second-probe peaks exceed the first);
   at high $M_s$ the second probe sees negative overpressure.
7. **Reliability estimate** (§5, eqs. 13–16, Table 2). Smirnov et al.'s
   accumulated-error measure, from about $6.45\times10^{23}$ to
   $2.61\times10^{29}$ over 294 µs, read by the authors as a "quite high
   level of reliability". It is a truncation-order bound, not a measured
   error.

**Tests.** One configuration (§3, Fig. 2), with Part I's boundaries and
initial data and $\mathrm{Re}$ of order $10^6$; flow features at
$M_s = 1.6$ ($t = 184$ and 292 µs) and 4.5 ($t = 69$ µs): primary and
secondary vortices, lambda shock, shear-layer instabilities, shocklets
(qualitative); vorticity maps at $M_s = 2.0$; probe histories for all
$M_s$. The comparable data are numerical and from one code.

# Notation map

| Brahmi et al. (2020b) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho$, $\mathbf v$, $p$, $\gamma$, $T$, $T_0$, $p_0$ | $\rho$, $\mathbf v$, $p$, $\gamma$, $T$; words for the pre-shock values | |
| $E$, $e$ | words | specific energies; the registry's $E$ is an energy density |
| $\tau$, $\mu$, $\lambda$ | $\boldsymbol\tau$; words | stress; dynamic viscosity; conductivity |
| $\omega$ (vorticity) | $\nabla\times\mathbf v$ | $\omega_k$ are the nonlinear weights |
| $\omega_1$, $\omega_2$ (wedge angles) | $\theta_{\mathrm w}$ | |
| $\omega_t$, $\omega_c$ | words | unsteady and convective parts of the material derivative |
| VSG, VSC, BAR, DFV | words | stretching, dilatation, baroclinic, viscous terms |
| $\Gamma$ | $\Gamma$ | circulation |
| $R$, $\mathscr R$ | words | arc radius; specific gas constant |
| $I_p$, $I_{pd}$, $\mathscr P$ | words | static and dynamic impulse, overpressure |
| $h$, $L_1$, $k$, $S_{err}$, $\eta$, $R_s$ | words | §5 reliability estimate; $\eta$ is the coercivity constant |
| $M_s$, $\mathrm{Pr}$, $\mathrm{Re}$ | $M_s$, $\mathrm{Pr}$, $\mathrm{Re}$ | |

# Pages created or updated

* Contributed to [Shock reflection from double concave wedges](/benchmarks/double-concave-shock-reflection.md).
* Updated [Immersed-boundary methods](/methods/immersed-boundary-method.md).

# Citations

1. `/home/stefano/papers/mosaic/high-order-capturing-schemes/2020-ActaAstronaut-Brahmi-101016jactaastro202002017.pdf`.
   * **Version.** The publisher's version of record (Elsevier, 11 pages).
     Received 28 January 2020, accepted 9 February 2020, online
     18 February 2020.
   * **Identity.** doi:10.1016/j.actaastro.2020.02.017, printed on page 1
     and checked on Crossref: Acta Astronautica 172:140–150, July 2020,
     authors Brahmi, Hadjadj, Soni, Chaudhuri; title as on page 1.
   * **How it was read.** Text extraction, all sections; eqs. 2–5 checked
     on the page-2 image at 300 dpi, eq. 9 on page 6.
   * **Recorded as printed.** Eq. 3 has $\rho$ for $p$ in the pressure
     work. Eq. 8's scaling uses undefined primed symbols, though the text
     calls the reported values dimensionless. Table 2's grids match G0–G3
     of Table 1 in point count, but its finest grid, 7681 × 3585
     (27.54 million, compiler's arithmetic), does not match G4's 33.55
     million; the paper does not explain this. §6 says the dilatation term
     matters "for low-Mach numbers regimes ($M_s \le 2.5$)", while §4.2
     attaches that qualifier to the viscous-against-baroclinic comparison.
     The abstract calls $M_s = 1.6$–4.5 "transonic to supersonic".
   * **Reference list:** 21 entries. [20] is Part I (`brahmi-2020`).
     Sun & Takayama (2003) is `sun-2003-b`. Bazhenova et al. is printed
     "6 (1951) (1979)" and Chaudhuri et al. (2012) "8 (89)"; the Crossref
     volumes (6, 1979; 89, issue 8) are recorded in the entries' notes. Two Shock
     Waves papers (2017) print no volume.
