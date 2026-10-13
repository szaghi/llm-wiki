---
type: Source
title: "Orszag & Tang (1979) — Small-scale structure of two-dimensional magnetohydrodynamic turbulence"
description: "A pseudospectral study of 2D incompressible, viscous and resistive MHD turbulence whose deterministic initial condition (v = (−sin y, sin x), A = cos y + ½ cos 2x on a 2π-periodic box) is the origin of the Orszag–Tang vortex; finds 2D MHD less singular than 3D hydrodynamics but more than 2D hydrodynamics; no density, pressure, sound speed or shocks."
resource: "doi:10.1017/S002211207900210X"
source_kind: paper
authors: [Orszag S.A., Tang C.-M.]
year: 1979
venue: "J. Fluid Mech. 90:129–143"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/1979-JFM-Orszag-101017S002211207900210X.pdf"
tags: [mhd, turbulence, pseudospectral, incompressible, benchmark-origin]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

A turbulence study, not a numerical-methods paper. It asks whether
two-dimensional **incompressible, viscous and resistive** MHD develops
small scales (and, in the inviscid limit, singularities) like 3D
hydrodynamics, or stays regular like 2D hydrodynamics. The
vorticity/vector-potential form of 2D incompressible MHD is solved by the
Fourier pseudospectral method (a modification of the KILOBOX code) on a
$2\pi$-periodic square, from one deterministic initial condition (eq. 7,
the flow now called the [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md))
and from a random Gaussian ensemble (eq. 8). Finding: 2D MHD is less
singular than 3D hydrodynamics but more singular than 2D hydrodynamics.
The dissipation rate grows well above its initial value, with a peak time
insensitive to viscosity, which suggests (does not prove) finite-time
vorticity singularities in the ideal limit. The flow has no density,
pressure, ratio of specific heats, sound speed or shocks; the field is the
curl of a potential, so $\nabla\cdot\mathbf B = 0$ holds by construction.
The compressible "Orszag–Tang vortex" of the shock-capturing literature is
a later adaptation of eq. 7.

# Key claims

1. **Equations** (§2, eqs. 1–3). In vorticity–vector-potential form, with
   velocity $\mathbf v$, field $\mathbf B = \nabla\times(A_z\hat{\mathbf z})$,
   vorticity $\nabla\times\mathbf v$ and current $\nabla\times\mathbf B$
   along $\hat{\mathbf z}$: the vorticity is advected by $\mathbf v$, forced
   by $\mathbf B\cdot\nabla$ of the current and diffused by the kinematic
   viscosity (eq. 1); $A_z$ is advected and diffused by the magnetic
   diffusivity (eq. 2); $\nabla\cdot\mathbf B = \nabla\cdot\mathbf v = 0$
   (eq. 3). Periodic box of side $2\pi$.
2. **Invariants** (§2). Without dissipation, total energy, mean-square
   vector potential and cross-helicity are conserved; the dissipation rate
   is viscosity times mean-square vorticity plus diffusivity times
   mean-square current (eq. 4).
3. **Reynolds numbers** (eqs. 5–6), of Taylor-microscale type; both grow by
   $2^{4/3} \doteq 2.52$ when the viscosity and diffusivity are halved.
4. **Numerics** (§2). Pseudospectral, truncated Fourier series (Gottlieb &
   Orszag 1977, ch. 2); KILOBOX (up to $1024^2$ modes); 9 FFTs per step for
   MHD; about 6 s per step at $256^2$ on a CDC 7600; runs of several hundred
   steps; dissipation accurate to better than 1%. Time integrator,
   dealiasing and time step are not stated.
5. **The initial condition** (§3, eq. 7):
   $\mathbf v = (-\sin y, \sin x)$, $A_z = \cos y + \tfrac12\cos 2x$, hence
   $\mathbf B = (-\sin y, \sin 2x)$ (derived, not printed). $64^2$ modes
   suffice for viscosity $\ge 0.02$, $128^2$ for 0.01, $256^2$ for 0.005;
   at viscosity = diffusivity = 0.02 the initial Reynolds numbers are 232
   (kinetic) and 114 (magnetic). Magnetic Prandtl numbers $\tfrac12$, 1, 2.
6. **Dissipation scaling** (§3, Figs. 1–2). Halving viscosity =
   diffusivity lowers the peak dissipation by about 20% (IC 7) or 26%
   (random IC, 0.02 to 0.01), so the data do **not** support Pouquet's
   hypothesis of a finite non-zero limit.
7. **Vorticity production** (§3). In 2D MHD the dissipation rate rises far
   above its initial value (in 2D hydrodynamics it cannot). Kinetic
   enstrophy peaks at about 2, $3\tfrac12$ and 10 times its initial value
   for viscosity 0.04, 0.02, 0.005, at $t \sim 1.5$ roughly independently of
   viscosity for values up to 0.02: together a suggestion of a finite-time
   singularity of the ideal problem, not a proof.
8. **Comparison with 3D** (Fig. 3). Taylor–Green vortex, Reynolds number
   100–400: a 4× change moves the dissipation peak by about 10%; 2D MHD is
   less prone to singular behaviour than 3D hydrodynamics.
9. **Mechanism** (§4). Field lines stretched into "ropes" and reconnected
   by diffusion; the snapping tension drives small eddies. The authors say
   the argument is not a proof because it relies on diffusion.

# Tests

| § / Fig. | Set-up | Finding |
|---|---|---|
| §3, Fig. 1 | IC (7), viscosity = diffusivity 0.08, 0.04, 0.02, 0.01, 0.005, $t \in [0, 2]$ | peak dissipation near $t \approx 1$–1.2, about −20% per halving (values read from the plot) |
| §3, Fig. 2 | Gaussian ensemble (eq. 8), 0.02 and 0.01 | peak about 26% lower at 0.01 |
| §3, Fig. 3 | 3D Taylor–Green, Reynolds 100–400 | peak changes about 10% |
| §3, Fig. 4 | IC (7), viscosity and diffusivity 0.02/0.04 combinations | magnetic enstrophy governed mainly by the diffusivity |
| §3, Fig. 5 | IC (7), 0.02 | strong kinetic–magnetic energy exchange |
| §3, Fig. 6 | IC (7), weak seed field (magnetic/kinetic energy $10^{-4}$), $t \le 4.5$ | seed field grows by finite factors |
| §3, Figs. 7–11 | IC (7), 0.005, $256^2$, **$t = 1$** | contours of current (an S-shaped central current structure), vorticity, streamlines, $\vert\mathbf B\vert$, field lines |
| §3, Fig. 12 | non-magnetic $\mathbf v = (-\sin y, \sin 2x)$, 0.005, $t = 1$ | vorticity much less intermittent than in MHD |

No error norms, convergence orders or CFL numbers; the only accuracy
statement is the better-than-1% dissipation.

# Notation map

| Orszag & Tang (1979) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf v$ | $\mathbf v$ | |
| $\mathbf h$ | $\mathbf B$ | **collision**: registry $h$ is the grid spacing |
| $A$ ($\mathbf A = A\hat{\mathbf z}$) | $A_z$ | **collision**: Jacobian $A$ |
| $\zeta$ | words (vorticity) | **collision**: cell coordinate $\zeta$ |
| $j$ | words (current density) | registry $\mathbf J$ is a curl-constrained field |
| $\nu$ | words (kinematic viscosity) | **collision**: CFL number $\nu$ |
| $\mu$ | words (magnetic diffusivity) | registry $\mu$ is a diffusion coefficient, compatible but named here |
| $E$, $E^v$, $E^m$ | words (domain-averaged energies) | registry $E$ is an energy density |
| $\epsilon(t)$ | words (dissipation rate) | **collision**: $\varepsilon$, $\epsilon_{\mathcal G}$ |
| $R^v$, $R^m$ | words (Taylor-microscale Reynolds numbers) | not $\mathrm{Re}$ |

# Pages created or updated

* Updated [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) (batch-18 block: the origin is incompressible, viscous, pseudospectral and shock-free).

# Citations

1. `/home/stefano/papers/mosaic/high-order-capturing-schemes/1979-JFM-Orszag-101017S002211207900210X.pdf`.
   * **Version read.** The publisher's version of record (scanned JFM print,
     15 pages, OCR text layer with garbled equations). Received 6 October
     1977.
   * **Identity.** doi:10.1017/S002211207900210X, checked on Crossref
     (2026-10-13): authors Steven A. Orszag and Cha-Mei Tang, J. Fluid Mech.
     90(1):129–143, published 16 January 1979, reference count 10; all
     agree with page 1.
   * **How it was read.** Every equation from page images at 300–400 dpi
     (pp. 130, 131, 133, 135, 142). Peak values of Figs. 1 and 6 are read off
     the plots; Figs. 7–12 were inspected through captions and the text.
   * **Recorded as printed.** Frisch & Bardos (1976) is cited in §1 as
     "unpublished" and is not in the reference list. Tóth's citation of this
     paper prints the first author as "A. Orszag"; page 1 and Crossref give
     Steven A. Orszag.
   * **Reference list:** 10 entries (Crossref also 10), all merged. Only
     Gottlieb & Orszag (book) and Orszag's 1976 and 1977 chapters print
     titles; Gottlieb & Orszag lands on `gottlieb-1977`, printed without the
     subtitle. Bibliography: 3380 entries.
