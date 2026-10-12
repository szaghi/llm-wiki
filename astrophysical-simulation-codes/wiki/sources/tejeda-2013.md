---
type: Source
title: "Tejeda & Rosswog (2013) — An accurate Newtonian description of particle motion around a Schwarzschild black hole"
description: "Derives from the low-energy limit of Schwarzschild geodesics a velocity-dependent generalized Newtonian potential whose equations of motion reproduce exactly the characteristic orbit radii, circular-orbit energy and angular momentum, trajectory shapes and pericentre advance, outperforms the Paczyński–Wiita and Nowak–Wagoner potentials on every test but hover thrust, and is added to a Newtonian SPH code for a tidal-disruption run."
resource: "doi:10.1093/mnras/stt853"
source_kind: paper
authors: [Tejeda E., Rosswog S.]
year: 2013
venue: "Mon. Not. R. Astron. Soc. 433:1930–1940"
local_file: "~/papers/mosaic/astrophysical-simulation-codes/2013-MNRAS-Tejeda-101093mnrasstt853.pdf"
tags: [pseudo-newtonian, relativity, verification]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

Writing Schwarzschild geodesic motion in coordinate time and taking the
low-energy limit (relativistic specific energy close to $c^2$), the paper
derives a velocity-dependent **generalized Newtonian potential**
$\Phi_{\mathrm G}(r, \dot r, \dot\varphi)$ and the Newtonian Lagrangian built
from it (§2, eqs. 2.8–2.11). The resulting equations of motion differ from the
exact coordinate-time geodesic equations only by a factor on the first term of
$\ddot r$ (eqs. 2.14–2.19), so they are exact for parabolic-like motion. It
reproduces exactly the photon, marginally bound and marginally stable orbit
radii, the circular-orbit specific energy and angular momentum, the spatial
projection of all trajectories (hence the pericentre advance) and the ratios of
orbital to epicyclic frequencies; it approximates the orbital and radial
epicyclic frequencies to within 5.7% for $r \ge 6r_{\mathrm g}$ (§3, Table 1).
It is compared with the Newtonian, Paczyński–Wiita and Nowak–Wagoner potentials
and wins everywhere except the static-hover thrust. Its Cartesian acceleration
(eq. A.5) is added to an existing Newtonian SPH code for a $\beta = 5$ tidal
disruption (§3.8). Merged into
[pseudo-Newtonian potentials](/methods/pseudo-newtonian-potentials.md).

# Key claims

1. **Low-energy limit** (§2, eqs. 2.1–2.8). With $r_{\mathrm g} = GM/c^2$ and
   dots denoting Schwarzschild coordinate-time derivatives, the specific
   energy in the limit is
   $$E_{\mathrm G} = \frac12\left[\frac{r^2\dot r^2}{(r-2r_{\mathrm g})^2} + \frac{r^3\dot\varphi^2}{r-2r_{\mathrm g}}\right] - \frac{GM}{r},$$
   a limit that "does not necessarily imply low velocities or weak field".
2. **Generalized potential** (eq. 2.10, proved):
   $$\Phi_{\mathrm G} = -\frac{GM}{r} - \frac{2r_{\mathrm g}}{r-2r_{\mathrm g}}\left[\frac{r-r_{\mathrm g}}{r-2r_{\mathrm g}}\dot r^2 + \frac{r^2\dot\varphi^2}{2}\right],$$
   read as the Newtonian term plus "the kinetic energy being also
   gravitationally attracted by the central mass". **Asserted, not
   demonstrated:** "Contrary to a pseudo-Newtonian potential, $\Phi_G$ does
   satisfy the Poisson equation (when the only source of the gravitational
   field is the central mass)" (p. 3); footnote 1 defines "pseudo" as not
   satisfying the Poisson equation.
3. **Conserved quantities** (eqs. 2.11–2.13, proved). The Lagrangian
   $\tfrac12\vert\dot{\mathbf x}\vert^2 - \Phi_{\mathrm G}$ is independent of
   $t$ and $\varphi$, so $E_{\mathrm G}$ and
   $h_{\mathrm G} = r^3\dot\varphi/(r-2r_{\mathrm g})$ are conserved; for
   parabolic-like motion the radial and angular equations are identical to the
   relativistic ones.
4. **Equations of motion** (eqs. 2.14–2.19). In spherical coordinates the
   exact Schwarzschild coordinate-time geodesic equations differ only by an
   extra factor $c^4/\mathcal E^2$ ($\mathcal E$ the relativistic specific
   energy) on the first term of $\ddot r$.
5. **Cartesian acceleration for hydrodynamics codes** (App. A, eq. A.5, read
   from the rendered page):
   $$\ddot{\mathbf x} = -\frac{GM\mathbf x}{r^3}\left(1-\frac{2r_{\mathrm g}}{r}\right)^2 + \frac{2r_{\mathrm g}(\mathbf x\cdot\dot{\mathbf x})}{r^2(r-2r_{\mathrm g})}\dot{\mathbf x} - \frac{3r_{\mathrm g}\vert\mathbf x\times\dot{\mathbf x}\vert^2}{r^5}\mathbf x .$$
   "The equations of motion derived from this potential can be implemented
   easily within existing Newtonian hydrodynamics codes with hardly any
   additional computational effort" (abstract, §4).
6. **Circular orbits** (§3.2, eqs. 3.3–3.6; App. B). Specific angular momentum
   and energy identical to the relativistic expressions, hence exact
   $r_{\mathrm{ph}} = 3r_{\mathrm g}$, $r_{\mathrm{mb}} = 4r_{\mathrm g}$,
   $r_{\mathrm{ms}} = 6r_{\mathrm g}$. Orbital frequency within 5.7% for
   $r \ge 6r_{\mathrm g}$; the Newtonian potential gives it exactly in
   coordinate time.
7. **Epicyclic frequencies** (§3.3, eqs. 3.12–3.15). Vertical frequency equals
   the orbital one, radial frequency within 5.7% for $r \ge 6r_{\mathrm g}$,
   and both frequency ratios exact.
8. **Hover thrust** (§3.4, eqs. 3.16–3.19). The one property where
   $\Phi_{\mathrm G}$ is worst: static-rocket thrust error up to 63.7% for
   $r > 6r_{\mathrm g}$, vanishing at $r = 2r_{\mathrm g}$ where the exact thrust
   diverges, explained as the potential describing an observer at infinity.
   It reproduces the thrust's independence of angular velocity at
   $r = 3r_{\mathrm g}$ and the centrifugal reversal there, which the authors
   are "not aware of ... ever having been reproduced before by any
   pseudo-Newtonian potential" (§4).
9. **General orbits** (§3.5, eqs. 3.20–3.25). The orbit equation is formally
   identical to GR under the exchange of the constants of motion: spatial
   projections of trajectories are identical and the pericentre advance is
   exact; time evolution along the orbit is exact only for parabolic-like
   motion.
10. **Radial infall** (§3.1, eq. 3.1). Infall times agree only for zero
    specific energy; both diverge at $r = 2r_{\mathrm g}$.
11. **Thin-disc efficiency** (§3.6, eq. 3.29): Newtonian $1/12$,
    Paczyński–Wiita $1/16$, Nowak–Wagoner $1/18$, generalized $1/18 \simeq 0.056$,
    Schwarzschild $1 - 2\sqrt2/3 \simeq 0.057$.
12. **Table 1** (maximum percentage error for $r > 6r_{\mathrm g}$; Newtonian /
    Paczyński–Wiita / Nowak–Wagoner / generalized): infall time from rest
    16.7 / 23.8 / 9.3 / exact; infall at $-0.3c$ 15.9 / 24.3 / 15 / 2.9;
    $r_{\mathrm{ph}}$ – / 33.3 / – / exact; $r_{\mathrm{mb}}$ – / exact / 13.4 /
    exact; $r_{\mathrm{ms}}$ – / exact / exact / exact; circular energy 50 /
    12.5 / 3.3 / exact; circular angular momentum 29.3 / 6.1 / 29.3 / exact;
    orbital frequency exact / 50 / 13.4 / 5.7; radial epicyclic frequency
    ∞ / 83.7 / 41.4 / 5.7; hover thrust 18.4 / 83.7 / 32.1 / 63.7; pericentre
    advance – / ∼30 / >80 / exact; disc efficiency 45.7 / 9.3 / 2.9 / 2.9;
    disc flux ∞ / 58.9 / 11.1 / 7.3.
13. **Comparison potentials** (§1, eqs. 1.1–1.2).
    $\Phi_{\mathrm{PW}} = -GM/(r-2r_{\mathrm g})$ and
    $\Phi_{\mathrm{NW}} = -\frac{GM}{r}\left(1 - \frac{3r_{\mathrm g}}{r} + \frac{12r_{\mathrm g}^2}{r^2}\right)$;
    $\Phi_{\mathrm{NW}}$ gives a pericentre lag for most eccentricities
    (Fig. 5). Also discussed: Wegg (2012), Semerák & Karas (1999), Kluźniak &
    Lee (2002), Abramowicz et al. (1997).
14. **Hydrodynamics coupling** (§3.8). The host is the authors' unnamed
    Newtonian SPH code (Rosswog et al. 2008, 2009); eq. A.5 is added to each
    particle. Time integration of the velocity-dependent force, any extra
    time-step constraint, the treatment of fluid self-gravity and energy
    monitoring are not stated. For Eulerian codes, simulating in the star's
    rest frame "may be beneficial" and "may require a multipole expansion of
    the tidal field", beyond the paper's scope. Test-particle limit only: no
    spin, no back-reaction; singular at $r = 2r_{\mathrm g}$.

**Tests** (§3; semi-analytic test-particle comparisons against exact
Schwarzschild solutions, except §3.8). Radial infall from infinity at
$-0.3c$, synchronized at $20r_{\mathrm g}$ (Fig. 1); circular-orbit energy,
angular momentum and frequency for $r/r_{\mathrm g}$ from about 3 to 30
(Fig. 2); hover thrust (Fig. 3); an orbit with pericentre $5r_{\mathrm g}$ and
apocentre $40r_{\mathrm g}$, whose spatial projection coincides exactly with GR
(Fig. 4); pericentre advance against eccentricity at fixed apocentre
$40r_{\mathrm g}$ (Fig. 5); Novikov–Thorne thin disc (Fig. 6); a ballistic
accretion inflow ($M = 4M_\odot$, start at $100r_{\mathrm g}$; Fig. 7) whose
streamlines are "basically indistinguishable" from GR. SPH tidal disruption
(§3.8, Fig. 8): $10^6M_\odot$ black hole, $1M_\odot$ $\gamma = 5/3$ polytrope on
a parabolic orbit, $\beta = 5$ (pericentre about $9.4r_{\mathrm g}$), start at
$200r_{\mathrm g}$, $10^4$ particles, four potentials. Paczyński–Wiita gives
about 70% of the relativistic pericentre advance and Nowak–Wagoner a shift of
the opposite sign; the generalized potential's centre-of-mass track is "in very
close agreement" with the geodesic and its matter distribution "closely
resembles" the GR run of Laguna et al. (1993). Visual comparison only: no
quantitative error, no resolution study.

# Notation map

| Tejeda & Rosswog (2013) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $G$, $c$ | $G$, $c$ | |
| $M$, $M_{BH}$ | none (words) | central black-hole mass |
| $r_g = GM/c^2$ | none; written $r_{\mathrm g}$ on this page | gravitational radius |
| $r$, $\theta$, $\phi$, $\varphi$ | none (words) | Schwarzschild coordinates; $\varphi$ the in-plane angle |
| $x^i$ | position $\mathbf x$ | **collision:** registry $x_i$ is a cell centre |
| dot | — | derivative in Schwarzschild coordinate time |
| $\tau$ | none (words) | proper time; **collision** with the Valencia $\tau$ and the optical depth |
| $\Phi_N$, $\Phi_{PW}$, $\Phi_{NW}$, $\Phi_G$ | none; written $\Phi_{\mathrm N}$, $\Phi_{\mathrm{PW}}$, $\Phi_{\mathrm{NW}}$, $\Phi_{\mathrm G}$ on this page | **collision in meaning:** registry $\Phi$ satisfies the Poisson equation; pseudo-Newtonian potentials do not, and $\Phi_{\mathrm G}$ is velocity-dependent |
| $\mathcal E = -u_t$ | none (words) | **collision** with the EMF $\boldsymbol{\mathcal E}$ |
| $E_S$, $E_G$, $E_N$, $E^c$ | none; $E_{\mathrm G}$ on this page | specific orbital energies; **collision** with total energy density $E$ |
| $h_S$, $h_G$, $h^c$ | none; $h_{\mathrm G}$ on this page | specific angular momentum; **collision** with cell size $h$ |
| $T$ | $\tfrac12\vert\dot{\mathbf x}\vert^2$ | kinetic energy per unit mass; **collision** with temperature |
| $L$ | none (words) | Lagrangian per unit mass and, in §3.6, disc luminosity |
| $\Omega$, $\Omega^\perp$, $\Omega^\parallel$ | none (words) | orbital, vertical and radial epicyclic frequencies |
| $r_{ph}$, $r_{mb}$, $r_{ms}$ | none; $r_{\mathrm{ph}}$, $r_{\mathrm{mb}}$, $r_{\mathrm{ms}}$ on this page | photon, marginally bound, marginally stable radii |
| $\mathcal F$ | none (words) | radial hover thrust |
| $e$ | none (words) | accretion efficiency; **collision** with specific internal energy |
| $D$ | none (words) | disc flux; **collision** with the Valencia $D$ |
| $\Gamma = 5/3$ | $\gamma$ | polytropic index of the star |
| $\beta = r_t/r_p$ | none (words) | encounter strength; **collision** with the shift $\beta^i$ |
| $\epsilon_{ijk}$ | — | Levi-Civita symbol (expressed with $\times$ above) |

# Pages created or updated

* Created [Pseudo-Newtonian potentials](/methods/pseudo-newtonian-potentials.md).

# Citations

1. `~/papers/mosaic/astrophysical-simulation-codes/2013-MNRAS-Tejeda-101093mnrasstt853.pdf`.
   * **Version.** arXiv:1303.4068v2 [astro-ph.HE], 14 Jun 2013, MN LaTeX
     style, 11 pages (recompiled by arXiv 27 Nov 2024): not the typeset
     journal version; v2 postdates online publication by three days and was
     not compared with the journal PDF. No code is released.
   * **Identity.** doi:10.1093/mnras/stt853, checked on Crossref: title exact,
     authors Tejeda and Rosswog, Mon. Not. R. Astron. Soc. 433(3):1930–1940,
     online 2013-06-11, issue 2013-08-11.
   * **How it was read.** Text extraction, all sections; eq. A.5 and App. B
     read from rendered pages. Eq. 3.4 is ambiguous in the text layer; the
     App. B form of the circular-orbit energy (rendered p. 11) was used.
     Figure values were not digitized.
   * **Recorded as printed.** The disc-flux error is "better than 7%"
     (abstract), "⩽ 7.2%" (§3.6) and "⩽ 7.3%" (Table 1). The introduction
     rounds the Table 1 values for the comparison potentials (13% for 12.5%,
     6% for 6.1%, 14% for 13.4%, 42% for 41.4%, 30% for 29.3%).
   * **Reference list:** 36 entries; articles without printed titles, books and
     the Novikov & Thorne chapter with titles. The cited Tejeda, Taylor &
     Miller (2013, MNRAS 429:925) is keyed `tejeda-2013-b`. Paczyński (1980) is
     keyed `paczynsky-1980` after the printed spelling "Paczyńsky". Same
     author-year pairs `abramowicz-1990`/`-b` (MNRAS 245:733 / 245:729) and
     `rosswog-2009`/`-b` (New Astron. Rev. 53:78 / ApJ 695:404).
