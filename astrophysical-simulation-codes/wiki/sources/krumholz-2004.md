---
type: Source
title: "Krumholz, McKee & Klein (2004) — Embedding Lagrangian Sink Particles in Eulerian Grids"
description: "First method for moving, accreting Lagrangian sink particles in an Eulerian (AMR or fixed-grid) code: creation where a cell violates the Truelove Jeans condition with J = 0.25, friends-of-friends merging, a kernel-weighted Bondi–Hoyle accretion rate with an angular-momentum filter, and a softened gas–particle force with Bulirsch–Stoer particle orbits, tested on Shu collapse, Bondi, Mach-3 Bondi–Hoyle and Keplerian-disk problems."
resource: "doi:10.1086/421935"
source_kind: paper
authors: [Krumholz M.R., McKee C.F., Klein R.I.]
year: 2004
venue: "Astrophys. J. 611:399–412"
local_file: "/home/stefano/papers/mosaic/astrophysical-simulation-codes/2004-ApJ-Krumholz-101086421935.pdf"
tags: [amr, self-gravity, hydro, benchmark, verification]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

The paper introduces the first method for embedding moving, accreting
Lagrangian sink particles in an Eulerian hydrodynamics code. Before it,
Eulerian codes had only fixed sink cells (Boss & Black 1982), and sink
particles existed in SPH (Bate et al. 1995). The algorithm has five parts:
creation in any cell that violates the Truelove Jeans condition with
$J = 0.25$; friends-of-friends merging within the accretion radius; a
Bondi–Hoyle interpolation formula for the accretion rate, evaluated with
Gaussian-kernel-weighted averages over an accretion zone of radius $4\Delta x$;
an angular-momentum filter built from $8^3$ ballistic test particles per cell;
and particle motion by a softened gas–particle direct sum plus an unsoftened
Bulirsch–Stoer particle–particle integrator. The host code is "our 3-D AMR
code" (§2.1), a Berger–Oliger/Berger–Colella/Bell et al. AMR code with
Godunov hydrodynamics, multigrid self-gravity and radiative transfer; the paper
never names it and gives no version. The method is tested on Shu collapse,
Bondi accretion for $r_B/\Delta x = 0.1$–$10$, Mach-3 Bondi–Hoyle accretion and
a Keplerian disk. Its stated main limitation is an accretion-rate error of up
to 24% when the Bondi radius is comparable to the accretion radius. Merged
into [sink particles](/methods/sink-particles.md), the
[Jeans resolution criterion](/definitions/jeans-resolution-criterion.md) and
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md).

# Key claims

1. **Host hydro and gravity** (§2.1, eqs. 1–4). Multi-fluid Euler equations
   with gravity source terms and $\nabla^2\phi = 4\pi G\sum_i\rho^i$. Hydro is
   a "conservative high-order Godunov scheme with an optimized approximate
   Riemann solver (Toro 1997)", second order for smooth flows (asserted).
   Gravity is a multigrid solve on each level, used as a source term (Truelove
   et al. 1998). AMR levels are subcycled with a synchronization step for
   conservation across levels; refinement keeps the sink's accretion zone at
   the finest level, and all quoted $\Delta x$, $\Delta t$ refer to that level.
   The sink framework "is not dependent on any of the details of the AMR
   framework, and may be applied equally well to fixed-grid codes" (asserted).
2. **Creation** (§2.2, eqs. 5–7). Jeans condition
   $\Delta x < J\lambda_J = J\sqrt{\pi c_s^2/(G\rho)}$, equivalently
   $\rho_J = J^2\pi c_s^2/(G\Delta x^2)$. A cell above $\rho_J$ with $J = 0.25$
   spawns a sink at the cell centre with mass $[\rho - \rho_J(0.25)]\Delta x^3$,
   leaving the cell at $\rho_J(0.25)$; a proportional share of momentum and
   energy goes to the sink. Rationale: Truelove et al. (1997) found
   $J = 0.25$ sufficient to prevent artificial fragmentation; Jeans violation
   also implies $\nabla\cdot\mathbf v < 0$ by continuity.
3. **Minimum-mass caveat** (§2.2, eqs. 8–9). A Jeans-violating cell holds more
   than $(\pi^{3/2}/1.18)J^3 m_{BE} \approx 0.07\,m_{BE}$ for $J = 0.25$, so a
   sink can be created in a stable region. The check is ex post facto: such a
   sink stays tiny, and the remedy is to rerun at higher resolution.
4. **Merging** (§2.3). At the end of each step, friends-of-friends (Davis et
   al. 1985) with linking length equal to the accretion-zone radius; each group
   becomes one particle at its centre of mass, quantities added
   conservatively. The accretion radius must always be ≤ the merger radius
   (§§2.3, 2.4.2).
5. **Accretion rate** (§2.4.1, eqs. 10–12). $r_{BH} = GM/(v_\infty^2 + c_\infty^2)$;
   $\dot M = 4\pi\rho_\infty r_{BH}^2(\lambda^2c_\infty^2 + v_\infty^2)^{1/2}$
   (Ruffert 1994a; Ruffert & Arnett 1994), $\lambda = e^{3/2}/4 \approx 1.120$
   (isothermal); $\rho_\infty = \bar\rho/\alpha(1.2\,\Delta x/r_{BH})$ with
   $\alpha$ the Bondi density profile and $\bar\rho$ the kernel-weighted mean
   density. The factor 1.2 is empirical; values in 0.5–2.0 raise the error by
   ≤ ~10% (§3.2). Ruffert's (1994b) more complex formula is rejected.
6. **Accretion zone and kernel** (§2.4.2, eqs. 13–14). $r_{\rm acc} = 4\Delta x$
   ("based on experiments"; a run-time parameter); kernel radius $r_K$ is
   $\Delta x/4$, $r_{BH}$ or $r_{\rm acc}/2$ by regime; weight
   $\propto \exp(-r^2/r_K^2)$. The procedure is undefined for overlapping zones.
7. **Angular-momentum filter** (§2.4.2, eq. 15). Each zone cell is split into
   $8^3$ point particles whose ballistic closest approach $r_{\min}$ to the sink
   is computed; the cell's accreted mass is reduced by $n/8^3$, $n$ counting
   points with $r_{\min} > \Delta x/4$. Thresholds 0.1–0.5 in place of 1/4 gave
   "no noticeable differences". At most 25% of a cell's mass may be removed per
   step.
8. **Bookkeeping** (§2.4.2). Only the radial (sink-frame) momentum is reduced
   by the accreted fraction, so the sink accretes no angular momentum; the sink
   receives the opposite momentum change; specific thermal energy is held
   fixed. "This accretion procedure conserves mass, momentum, and angular
   momentum to machine precision" (asserted, no measurement). Total energy is
   not claimed to be conserved.
9. **Particle motion** (§2.5, eqs. 16–17). Gas→particle kick from a
   Plummer-softened direct sum, $\epsilon = 2\Delta x$ by default (host and
   neighbour cells split into $8^3$ points); particle–particle orbits by adaptive
   Bulirsch–Stoer with error control (Press et al. 1992), unsoftened. Time-step
   limit $\max(v_{\rm part})\Delta t < C\Delta x$, $C = 0.5$, "usually less
   stringent than the ordinary gas Courant condition". Not stated: how the
   sink's gravity acts back on the gas, and where accretion and kick sit in the
   hydro step sequence.
10. **Integrator test** (§2.5). Binary with eccentricity 0.998, closest approach
    ~$\Delta x/100$: after several orbits semi-major axis conserved to ~1%,
    eccentricity to ~0.1% (measured).
11. **Self-correction** (§3.3). Over- or under-estimates of the rate make gas
    pile up in or drain from the zone, adjusting $\bar\rho$ until the rate
    matches what the hydro delivers; formula details matter little when
    $r_{BH}$ is resolved (argued, supported by the §3.3 test).
12. **Numerical viscosity** (§3.4.2, eqs. 18–22). Fit
    $r_{\rm evac}/\Delta x = 6.1\,[\Omega(r_{\rm acc})t/2\pi]^{0.23}$, giving
    $\alpha \approx 78\,(r_B/\Delta x)(r/\Delta x)^{-3.85}$; e.g. $\alpha = 0.01$ at
    $r = 18.6\Delta x$ for $r_B/\Delta x = 10$. The constant 78 is claimed
    code-dependent, the exponents geometric (asserted).
13. **Limitation** (§§3.2, 5). "one ought not use it in cases where the flow at
    the sink particle is transitioning from subsonic to supersonic"; with AMR
    one can refine temporarily until $r_B > r_{\rm acc}$.

**Tests** (§3–4; measured). Shu (1977) isothermal-sphere collapse, 1 M⊙,
64 cells per radius, at rest and advected at $0.5\,c_s$ and $2\,c_s$: density and
velocity errors "a few percent" next to the accretion region and ~1% further
out, accretion-rate error ~1% in all three runs (Figs. 1–2). Bondi accretion at
marginal resolution (Table 1): errors 0.011, −0.006, −0.122, −0.244, −0.023 for
$r_B/\Delta x$ = 0.1, 0.316, 1.0, 3.16, 10.0 — peaking when $r_B \approx r_{\rm acc}$.
Mach-3 Bondi–Hoyle, finest cells $r_{BH}/50$: mean rate after ~$6t_{BH}$ of
$2.0\times10^{-12}$ M⊙/yr $= 1.17\,\dot M_{BH}$, in agreement with Ruffert (1996)
(Figs. 3–4). Keplerian disk, >100 orbits at the zone edge, with a no-accretion
control: the evacuated region is slightly smaller with accretion, so the sink
causes no artificial angular-momentum transport (Figs. 5–6). Application (§4):
Mach-3 shock hitting a Bondi accretor, $\Delta x = r_B/512$; the rate jumps ~50%
at impact and decays exponentially toward $\dot M_{BH}$ (eq. 23), excess mass
$\Delta M \approx 56\,\dot M_{BH}t_{BH}$ (eq. 24).

# Notation map

| Krumholz et al. (2004) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho^i$, $\sum_i\rho^i$ | $\rho$ | species index dropped after §2.1 |
| $\mathbf v$, $G$ | $\mathbf v$, $G$ | |
| $P^i$ | $p$ | |
| $e^i$ | $E/\rho$ | **collision:** the paper's $e$ is the total non-gravitational specific energy, registry $e$ is specific internal energy |
| $\phi$ | $\Phi$ | |
| $\Delta x$ | $h$ (finest level) | all quoted $\Delta x$ are finest-level spacings |
| $c_s$ | $c_s$ | **note:** isothermal sound speed throughout; registry $c_s$ is adiabatic |
| $J$ | none (words: inverse of cells per Jeans length) | **collision** with $\mathbf J$ (current density); $J = 0.25$ is 4 cells per Jeans length |
| $\lambda_J$, $\rho_J$ | none (words) | Jeans length and Jeans density at fixed $h$ |
| $m_{\rm sink}$, $M$, $m$ | none (words) | sink mass |
| $r_{BH}$, $r_B$, $r_{\rm acc}$, $r_K$, $w$ | none (words) | Bondi–Hoyle and Bondi radii, accretion radius, kernel radius and weight |
| $v_\infty$, $c_\infty$, $\rho_\infty$, $\dot M$ | none (words) | far-field state, accretion rate |
| $\lambda$ (eq. 11) | none (words) | **collision** with eigenvalues $\lambda^{(p)}$ |
| $\alpha(x)$ (Bondi profile); $\alpha$ (eqs. 20–22) | none (words) | **collision:** the same letter is the Bondi density profile and the Shakura–Sunyaev viscosity parameter; registry has $\alpha_{\mathrm L}$ (lapse) |
| $\nu$ (kinematic viscosity) | none (words) | **collision** with registry $\nu$ (Courant number) |
| $\epsilon$ | none (words) | Plummer softening length |
| $C$ (eq. 16) | none (words) | particle Courant-like number, distinct from $\nu$ |
| $j_{sp}$, $e_{sp}$; $e$ (§2.5) | none (local) | sink-frame specific angular momentum and energy; orbital eccentricity — both collide with registry $e$ |
| $\mathcal M$, $\Omega$, $\Sigma$ | none (words) | Mach number, disk angular velocity, surface density |

# Pages created or updated

* Created [Sink particles](/methods/sink-particles.md),
  [Jeans resolution criterion](/definitions/jeans-resolution-criterion.md).
* Updated [Adaptive mesh refinement in astrophysical codes](/methods/adaptive-mesh-refinement.md).
* Also cited on [Singular isothermal sphere collapse](/benchmarks/singular-isothermal-sphere-collapse.md).

# Citations

1. `~/papers/mosaic/astrophysical-simulation-codes/2004-ApJ-Krumholz-101086421935.pdf`.
   * **Version.** arXiv preprint astro-ph/0312612v1 (23 Dec 2003), 35 pages,
     AAS LaTeX v5.0 preprint format; not the typeset journal article.
     Differences from the published version are unknown. The host code is
     not named (it is the Berkeley/LLNL AMR code of Truelove et al. 1998 and
     Fisher et al. 2004; the name ORION does not appear) and no code version is
     given.
   * **Identity.** doi:10.1086/421935, checked on Crossref: "Embedding
     Lagrangian Sink Particles in Eulerian Grids", Astrophys. J. 611(1):399–412,
     published in print 2004-08-10; authors Krumholz, McKee, Klein as on page 1.
   * **How it was read.** Text extraction, all sections; eqs. 3 and 15 checked
     on rendered pages (pp. 4, 10). Figures 1–10 not digitized; numbers come
     from text and captions.
   * **Recorded as printed.** Eq. 3 prints the energy source as
     $+\rho\mathbf v\cdot\nabla\phi$, inconsistent with the force $-\rho\nabla\phi$ of
     eq. 2 (should be $-$). Eq. 15 prints $2j_{sp}e_{sp}/(GM)^2$, which is not
     dimensionless ($j_{sp}^2e_{sp}$ would be; probable preprint typo). Eq. 22's
     exponent −2.85 "rather than −4.35 = −1/0.23" reproduced, not re-derived.
     §4.3 prints $t_B = r_B/c_s = 6.35\times10^3$ yr and
     $t_{BH} = 6.35\times10^4$ yr, contradicting $r_B = 10\,r_{BH}$ (recomputed
     $t_B \approx 6\times10^5$ yr), and
     "$t_{\rm trans} = 1.1\times10^7$ yr $= 1.7t_B = 17t_{BH}$", consistent with
     neither ($17t_{BH} \approx 1.1\times10^6$ yr); not propagated to concept pages.
   * **Reference list:** 54 printed entries (Crossref lists 52 for the
     published version; not reconciled). No DOIs; titles only for the three
     books (Press et al.; Richtmyer & Morton; Toro, with "Reimann" as printed).
     Ebert (1955) printed with volume 317 (pages 217), kept as printed. The
     Fisher et al. entry is garbled (author list interrupted by "2003");
     Hoyle & Lyttleton entries 2–4 printed 1939 while the text cites
     "1940a,b,c"; Truelove 1997/1998 print the fifth author as "Howell, J. H.".
     Jijina 1999, MacLow et al. 1998, McKee & Tan 2003 and Ruffert 1999 are
     listed but not cited in the text.
