---
type: Source
title: "Bryson & Gross (1961) — Diffraction of strong shocks by cones, cylinders, and spheres"
description: "Schlieren experiments in an air shock tube on strong plane shocks passing cones, a circular cylinder and a sphere, with the measured triple-point loci compared with Whitham's shock-dynamics theory extended to blunt bodies; the experimental origin of the shock-reflection-from-a-cylinder benchmark, with regular reflection first and Mach reflection from 40°–50° on the cylinder."
resource: "doi:10.1017/S0022112061000019"
source_kind: paper
authors: [Bryson A.E., Gross R.W.F.]
year: 1961
venue: "J. Fluid Mech. 10:1–16"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/1961-JFM-Bryson-101017s0022112061000019.pdf"
tags: [mach-reflection, benchmark]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

An experimental and theoretical study of plane strong shocks diffracting
over cones, a circular cylinder and a sphere. Schlieren photographs taken
in the Harvard 4 in. × 12 in. × 40 ft air shock tube give the loci of the
triple points (Whitham's "shock-shocks") and the shapes of the diffracted
(Mach) shocks. These are compared with Whitham's approximate theory of
shock dynamics (1957, 1958, 1959), which the paper extends to blunt bodies
with a new small-angle approximation near the nose, used to start a
characteristics solution. There is no numerical (CFD) computation. For a
numerics bundle the paper matters as the experimental reference of the
[shock reflection from a cylinder](/benchmarks/shock-reflection-from-cylinder.md)
benchmark and of the [shock passing a sphere](/benchmarks/shock-sphere-interaction.md),
and as an early record of the [regular and Mach reflection](/definitions/mach-reflection.md)
sequence on a curved body.

# Key claims

1. **Facility and diagnostic** (§2, pp. 1–2). Air; schlieren system with a
   spark source of about 0.2 µs; the shock speed is measured between two
   schlieren light screens with an electronic counter, and the second
   screen triggers a variable delay that fires the spark. Each photograph
   is a different run at a different stage, and **no photograph carries a
   time**.
2. **Cones** (§2, plate 1, fig. 2). Semi-apex angles $\theta_{\mathrm w}$
   from 9.7° to 44.7°, mean $M_s = 3.68 \pm 0.16$ (plate 1: $\theta_{\mathrm w} = 35.1°$,
   $M_s = 3.55$). The triple-point loci are straight lines from the apex.
   The measured angle between locus and cone surface lies below Whitham's
   curve, "the same discrepancy as that reported by Whitham (1957) on
   wedges". The cause offered: the theory has no regular reflection and
   predicts Mach reflection for every $\theta_{\mathrm w}$ up to 90°, though
   above about 70° the predicted Mach stem is so short that the reflection
   is regular "for all practical purposes".
3. **Cylinder** (§2, plates 2–4, fig. 6). $D = \tfrac12$ in., mean
   $M_s = 2.82$ (plates 2.82, 2.81, 2.84; fig. 6 caption 2.81). Two series
   a factor 10 apart in post-shock pressure: 9.94 p.s.i. with
   $\mathrm{Re} = 7.79\times10^4$, and 1.08 p.s.i. with
   $\mathrm{Re} = 0.78\times10^4$, $\mathrm{Re}$ formed with $D$ and the
   post-shock flow speed and kinematic viscosity. The diffraction is
   followed through about 7 diameters of incident-shock travel.
   * The reflection is **regular at first; Mach reflection begins between
     40° and 50° from the forward stagnation point** (p. 4).
   * Each side of the symmetry plane carries two triple-point loci, one
     starting at the front and one at the symmetry plane behind the body.
   * The Mach shocks colliding behind the cylinder act as a reflection
     from a wall on the symmetry plane: regular first, with **Mach
     reflection beginning 0.5 to 1.0 diameters behind the cylinder** (p. 4).
   * The slip surface rolls up into a vortex produced by the interaction
     of the boundary layer with the shock when the Mach shock first forms;
     its locus (fig. 6) follows a Whitham ray except near the rear symmetry
     plane. It is not seen in the low-density series. Plates 3–4 show
     boundary-layer separation on the aft sides and the wake interacting
     with the reflected shock.
   * **Changing $\mathrm{Re}$ by a factor 10 does not change the
     triple-point loci** (p. 4, fig. 6).
4. **Sphere** (§2, plates 5–6, fig. 9). A table-tennis ball of $D = 1$ in.
   filled with Wood's metal, hung on 8 nylon strings; two series at
   $M_s = 2.85$ and 4.41 with $\mathrm{Re}$ about constant; about 3.5
   diameters of shock travel. The pattern is that of the cylinder, with
   two pairs of triple-point loci. The converging Mach shock collides at a
   point on the rear stagnation point, and the reflected spherical shock
   penetrates the second Mach shock (plate 6). The measured loci of the two
   $M_s$ coincide with each other and with the predicted first locus;
   the theory gives the same pattern for $M_s \ge 3$.
5. **Theory** (§3). Whitham's ray-tube-area, characteristic-angle and
   "Prandtl–Meyer" functions are tabulated (Table 1) for shock Mach
   numbers from 1 to ∞; the characteristic angle tends to 23.9° and, for
   strong shocks, the ray-tube area varies as the shock Mach number to the
   power $-5.0743$. The paper states that the Prandtl–Meyer function is
   zero at Mach number 1, "which is in error in Whitham's paper of 1957".
   Near the nose of a blunt body the triple-point standoff grows as the
   $6.0743$-th power of the sine of the azimuth from the front stagnation
   point; for the sphere it is half the cylinder's (eqs. 10, 13). The
   approximation is taken as valid to 50° and the characteristics are
   started at 45°. The predicted first triple-point locus agrees with
   experiment ("good" for the cylinder, "very good" for the sphere); the
   second locus on the sphere is not predicted, because the
   characteristics net diverges on the aft side. The reflected shock and
   the vortex are outside the theory.

# Tests

Experiments only, all in air, schlieren, in the same shock tube.

| Body | Size | $M_s$ | Data | Figures |
|---|---|---|---|---|
| Cones | $\theta_{\mathrm w}$ = 9.7°–44.7° | 3.68 ± 0.16 | triple-point-locus angle against $\theta_{\mathrm w}$ (about 7 points) | plate 1, fig. 2 |
| Cylinder | $D = \tfrac12$ in. | 2.82 | both triple-point loci in $(x/D, y/D)$ to $x/D \approx 7$, vortex locus, the two transition locations, two $\mathrm{Re}$ | plates 2–4, fig. 6 |
| Sphere | $D = 1$ in. | 2.85, 4.41 | both triple-point loci to $x/D \approx 3.5$ | plates 5–6, fig. 9 |

Theory against experiment is graphical, with no error numbers. Figs. 6
and 9 are quantitative trajectories a simulation can be scored against;
because the plates carry no times, a simulation must be matched to a
plate by the position of the incident shock.

# Notation map

| Bryson & Gross (1961) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $M_0$ (incident shock Mach number) | $M_s$ | |
| $M$, $M_1$ (local Mach number of the diffracted shock) | words | $M$ is the TVB constant |
| $\theta_w$ (cone semi-apex angle) | $\theta_{\mathrm w}$ | |
| $\theta$ (ray angle), $\chi$ (shock-shock angle) | words | $\theta$ is the limiter scaling, $\chi$ the dense-output fraction |
| $A$, $m$, $\omega$ (ray-tube area, characteristic angle, Prandtl–Meyer function) | words | $A$ is the flux Jacobian, $\omega_k$ the WENO weights |
| $n = 5.0743$ | words | |
| $\lambda$, $\phi$ (standoff, azimuth) | words | $\lambda$ are eigenvalues, $\phi_i$ the PPM flattening |
| $D$ | $D$ | |
| $Re$, $P_2$ | $\mathrm{Re}$, post-shock $p$ | |
| "shock-shock" | triple-point locus | Whitham's term |
| I.S., R.S., M.S., C.D., T.P. | incident shock, reflected shock, Mach stem, slip line, triple point | plate labels; see [regular and Mach reflection](/definitions/mach-reflection.md) |

# Pages created or updated

* Created [Regular and Mach reflection](/definitions/mach-reflection.md) (regular then Mach reflection on the cylinder, the rear reflection, the cone discrepancy).
* Updated [Shock reflection from a cylinder](/benchmarks/shock-reflection-from-cylinder.md) (origin, quantitative loci, transition locations, $\mathrm{Re}$-independence, no printed times, viscous features).
* Contributed to [Shock passing a sphere](/benchmarks/shock-sphere-interaction.md) (1 in. sphere, fig. 9).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/1961-JFM-Bryson-101017s0022112061000019.pdf`.
   * **Version.** The published journal article, a 22-page scan (16 text
     pages and 6 plates) with an OCR text layer. Received 24 July 1960.
   * **Identity.** doi:10.1017/S0022112061000019, checked on Crossref:
     J. Fluid Mech. 10(1):1–16, February 1961, authors A. E. Bryson and
     R. W. F. Gross.
   * **How it was read.** The OCR layer for prose and Table 1; every
     equation, all captions and the key numbers ($D$, $\mathrm{Re}$, $M_s$
     of each plate) checked on page images. Figure curves were not
     digitized.
   * **Recorded as printed.**
     - The low-density series has $\mathrm{Re} = 0.78\times10^4$ in the
       text and $0.87\times10^4$ in the fig. 6 caption; the text prints
       "7·79 + 10⁴" for $7.79\times10^4$.
     - The sphere $M_s$ is 2.85 in the text and fig. 9, and 2.89 in the
       captions of plates 5 and 6; the cylinder $M_s$ is 2.82 in the text
       and 2.81 in the fig. 6 caption.
     - $\gamma$ is never stated; Table 1 is presumably for air.
     - Table 1 prints 1.728 for the Prandtl–Meyer function at Mach number
       1.40, which breaks the smooth increments (1.669, 1.728, 1.887); the
       reader suspects 1.778, not verified.
     - One factor of the closed form of the ray-tube area (p. 8) is
       typographically ambiguous, so it is not reproduced.
   * **Reference list:** 5 entries (Crossref deposits 5): de Haller 1945,
     Shapiro 1954, Whitham 1957, 1958, 1959. The key `bryson-1961` already
     existed, cited by barriosanchez-2024 and natarajan-2022. Whitham
     (1957) has the vol:page of the existing `whitham-1957` entry (J. Fluid
     Mech. 2:145) and is the same work.
