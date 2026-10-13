---
type: Source
title: "Brahmi, Hadjadj, Soni & Chaudhuri (2020) — Analysis of shock-wave diffraction over double concave cylindrical wedges. Part I: Shock dynamics"
description: "Viscous simulations (WENO5, RK3, adaptive multiresolution, ray-traced immersed boundary) of a shock over two concave arcs at M_s 1.6–4.5: a five-grid study of the regular-to-Mach transition angle, transition angles rising with M_s and larger on the second arc at M_s 3.5 and 4.5, a single-to-double triple-point sequence, and an empirical time scaling that collapses shock attenuation; no experiment."
resource: "doi:10.1016/j.actaastro.2020.01.025"
source_kind: paper
authors: [Brahmi N., Hadjadj A., Soni V., Chaudhuri A.]
year: 2020
venue: "Acta Astronaut. 172:134–139"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2020-ActaAstronaut-Brahmi-101016jactaastro202001025.pdf"
tags: [benchmark, mach-reflection, immersed-boundary, navier-stokes, weno]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

A numerical parametric study of a planar shock running over two concave
circular arcs in series ("double concave cylindrical wedges") at
$M_s = 1.6$, 2.0, 2.5, 3.5 and 4.5 in air. The 2D compressible
Navier–Stokes equations are solved by the authors' in-house code: WENO5
inviscid fluxes, fourth-order central viscous fluxes, third-order
Runge–Kutta, adaptive multiresolution and a ray-traced immersed boundary
on a Cartesian grid. A five-grid study at $M_s = 1.6$ fixes the grid. The
outputs are the regular-to-Mach transition angle on each arc, triple-point
trajectories, wall pressure and skin friction, and the incident shock's
position and speed. There is no experiment and no second code. Part II is
[Brahmi et al. (2020b)](/sources/brahmi-2020-b.md), and is not cited
here. Merged into
[shock reflection from double concave wedges](/benchmarks/double-concave-shock-reflection.md).

# Key claims

1. **Equations** (§2.1, eqs. 1–5). Compressible Navier–Stokes, ideal gas,
   $\gamma = 1.4$, $\mathrm{Pr} = 0.72$, Sutherland viscosity. Eq. 3
   prints the pressure work as the divergence of $\rho\mathbf v$ where
   that of $p\mathbf v$ is meant; $\nabla$ is used for the divergence.
2. **Numerics** (§2.1). WENO5 for the inviscid fluxes, fourth-order
   central differences for the viscous fluxes, third-order Runge–Kutta,
   adaptive multiresolution, and an immersed-boundary method with the
   solid "embedded in a Cartesian grid tracked using a ray-tracing
   technique" (cited to Chaudhuri et al. 2011). The IB variant, the
   Riemann solver or flux splitting and the RK3 variant are not stated.
3. **Time step** (eqs. 6–7). Courant number 0.7 with a convective and a
   viscous restriction, giving $\Delta t \approx 10^{-8}$ s. The
   quantities eq. 7 calls $\Delta t_x$, $\Delta t_y$ are inverse time
   scales, not time steps.
4. **Grid independence** (§§3, 4.1, Tables 1–2, Figs. 3, 8). Five grids
   G0–G4 (finest spacing 95/88 down to 20/21 µm, 1.83 to 33.55 million
   points). Transition angles (arc 1/arc 2): 9.6°/9.7°, 10.7°/10.8°,
   11.8°/11.8°, 12.7°/12.6°, 12.7°/12.6°. Independent from G3; G4 is used
   for the rest.
5. **Transition angle against $M_s$** (§4.1, Fig. 4). Rises with $M_s$;
   nearly equal on both arcs except at $M_s = 3.5$ and 4.5, where it is
   larger on the second arc by "approximately 7% for $M_s = 4.5$ and 4%
   for $M_s = 3.5$". The fitted curve's formula is not given.
6. **Soni et al. (2017)** (§§1, 4.1) found the angle larger on the second
   reflector up to $M_s = 2.5$; the difference is attributed to a
   different orientation and shock entrance and not reconciled further.
7. **Triple-point tracking** (eq. 8): the running maximum over time steps
   of the pressure-gradient magnitude $\vert\nabla p\vert$.
8. **Wave configurations** (§4.1, Figs. 5–7). Second arc: regular to
   single-triple-point Mach reflection, then a second triple point, at
   $M_s = 3.5$ and 4.5; at 4.5 the triple points later merge again.
9. **Attenuation and scaling** (§4.2, eqs. 9–10, Figs. 8–9). The shock
   keeps its speed until the corner, then slows, more so and earlier for
   larger $M_s$. An empirical time scaling, "found from the data
   analysis", collapses position and velocity for all $M_s$ (tested only
   for $\gamma = 1.4$, radius 50 mm).

**Tests.** One configuration (§3, Fig. 1): arcs of radius 50 mm with
initial wall angle 75° each, inlet height 0.32, outlet height 1.8 and
length 3.4 arc radii; shock 5 mm ahead of the first corner into air at
300 K and 101.3 kPa; no-slip wall. Grid study at $M_s = 1.6$; a
space–time density diagram along a horizontal line at $M_s = 2.0$
(Fig. 2: incident shock and a left-running secondary shock swept right
by the supersonic flow); the $M_s$ sweep on G4. No error norms, no
order measurement, no experimental data.

# Notation map

| Brahmi et al. (2020) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho$, $\mathbf v$, $p$, $\gamma$, $T$ | $\rho$, $\mathbf v$, $p$, $\gamma$, $T$ | |
| $E$, $e$ | words | specific total and internal energy; the registry's $E$ is an energy density |
| $\tau$ | $\boldsymbol\tau$ | viscous stress; $\tau$ is the WENO-Z indicator |
| $\lambda$ (conductivity) | words | $\lambda^{(p)}$ are eigenvalues |
| $\mu$ | words (dynamic viscosity) | $\mu$ is the diffusion coefficient of the scalar model |
| $Pr$, $CFL$ | $\mathrm{Pr}$, $\nu$ | |
| $\Delta x_{min}$, $\Delta y_{min}$ | $h_x$, $h_y$ | finest spacing |
| $a_1$ | $c$ (of the gas at rest) | |
| $M_s$ | $M_s$ | |
| $R$, $R_1$, $R_2$ | words (arc radius) | $R$ is the eigenvector matrix |
| $\omega_1$, $\omega_2$ | $\theta_{\mathrm w}$ | initial wall (diffraction) angle; $\omega_k$ are the nonlinear weights |
| $\theta^{tr}$, $\theta^{tr}_1$, $\theta^{tr}_2$ | $\theta_{\mathrm{tr}}$ | per arc |
| $W_s$, $W_s^i$ | words | shock speed and its initial value |
| $\phi(\gamma, M_s)$ | words | scaling factor; $\phi_i$ is the PPM flattening |
| $TP^n$ | $\vert\nabla p\vert$ at step $n$ | |
| RR, MR, STP, DTP | words ([definitions](/definitions/mach-reflection.md)) | |

# Pages created or updated

* Created [Shock reflection from double concave wedges](/benchmarks/double-concave-shock-reflection.md).
* Contributed to [Regular and Mach reflection](/definitions/mach-reflection.md).
* Updated [Immersed-boundary methods](/methods/immersed-boundary-method.md).

# Citations

1. `/home/stefano/papers/mosaic/high-order-capturing-schemes/2020-ActaAstronaut-Brahmi-101016jactaastro202001025.pdf`.
   * **Version.** The publisher's version of record (Elsevier, 6 pages).
     Received 18 February 2019, accepted 17 January 2020, online
     31 January 2020.
   * **Identity.** doi:10.1016/j.actaastro.2020.01.025, printed on page 1
     and checked on Crossref: Acta Astronautica 172:134–139, July 2020,
     authors Brahmi, Hadjadj, Soni, Chaudhuri; title as on page 1.
   * **How it was read.** Text extraction, all sections; pages 2–6 and
     eqs. 3 and 10 checked on the page images (eq. 3 at 300 dpi).
   * **Recorded as printed.** Eq. 3 has $\rho$ for $p$ in the pressure
     work. The precedence of $\ln(M_s+1)^{1/\gamma}$ in eq. 10 is
     ambiguous. Fig. 8's caption omits $M_s$ (1.6 implied) and calls the
     reference line "piston theory", the text "shock-tube theory". The
     range is "$1.6 \le M_s \le 4.5$" in §3 and "$1.6 < M_s < 4.5$" in
     §5. In-text years differ from the reference list (Bird "1958" against
     1959; Bazhenova "1978" against 1979, the entry itself printed
     "6 (1951) (1979)"), and the introduction contrasts
     reference [23] with itself where [24] is evidently meant. The
     abstract calls $M_s = 1.6$ "transonic".
   * **Reference list:** 24 entries. Bryson & Gross (1961) and Whitham
     (1957) land on the existing `bryson-1961` and `whitham-1957` (same
     vol:page). The two Berezkina et al. papers (convex surface 2006,
     concave surface 2007) are distinct entries. Chaudhuri et al. (2011,
     J. Comput. Phys. 230:1731) is the existing `chaudhuri-2011`; the
     second Chaudhuri 2011 work (J. Sci. Comput. 47:170) is
     `chaudhuri-2011-b`.
