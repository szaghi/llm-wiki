---
type: Source
title: "Townsend (2009) — An exact integration scheme for radiative cooling in hydrodynamical simulations"
description: "Integrates the isochoric, operator-split optically thin cooling sub-step exactly for any time step through a temporal evolution function and its inverse, closed-form for piecewise power-law cooling curves, and shows that backward-Euler and Crank–Nicolson cooling updates can have multiple roots and jump between them as the time step varies."
resource: "doi:10.1088/0067-0049/181/2/391"
source_kind: paper
authors: [Townsend R.H.D.]
year: 2009
venue: "Astrophys. J. Suppl. 181:391–397"
local_file: "~/papers/mosaic/astrophysical-simulation-codes/2009-ApJS-Townsend-1010880067-00491812391.pdf"
tags: [cooling, time-integration, hydro, performance, verification]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

The paper presents the **exact integration (EI) scheme** for optically thin
radiative cooling in operator-split hydrodynamics codes. The isochoric
cooling sub-step reduces to a semi-discrete ODE for the zone temperature,
$\mathrm d\bar T_i/\mathrm dt = -\frac{(\gamma-1)\bar\rho_i\mu}{k\mu_e\mu_H}\Lambda(\bar T_i)$.
Because the cooling efficiency $\Lambda$ depends on $T$ alone, the ODE is
separable and is integrated exactly over $\Delta t$ through a "temporal evolution
function" $Y(T)$ and its inverse, both closed-form for power-law and piecewise
power-law $\Lambda(T)$ (Appendix). The paper also shows that implicit cooling
updates (backward Euler and Crank–Nicolson, with secant or Brent root-finding)
can have multiple roots and jump between them as $\Delta t$ varies, against their
"unconditionally stable" reputation. On a frozen steady radiative-shock profile
with a CFL step, EI has zero error by construction (it is the reference) and
costs about 2× the first-order explicit update; the implicit updates cost
2.5–12×. Merged into
[integrating cooling and chemistry source terms](/methods/radiative-cooling-integration.md).

# Key claims

1. **Operator split** (§1–§2, eqs. 1–3). The ideal-gas energy equation with
   loss $-(\gamma-1)n_en_H\Lambda(T)$ is split into an adiabatic part, applied in
   the advection stage with the mass and momentum updates, and a cooling part
   applied in a subsequent stage at constant density (isochoric; "e.g.,
   Mignone 2005"). Footnote 1: an adiabatic advection stage keeps
   characteristic Godunov schemes such as PPM usable. The isochoric stage is
   asserted not to preclude isobaric systems such as cooling flows.
2. **Cooling equation in temperature** (eqs. 4–8). With $P = nkT$ and constant
   $\mu$: $\mathrm dT/\mathrm dt = -\frac{(\gamma-1)\rho\mu}{k\mu_e\mu_H}\Lambda(T)$ (eq. 5);
   $\mu$, $\mu_e$, $\mu_H$ for full ionization (eqs. 6–8). Constant $\mu$ is "a
   reasonable approximation for temperatures $\gtrsim 10^4$ K" (Gnat &
   Sternberg 2007). EI requires $\Lambda = \Lambda(T)$ only; its extension to
   non-equilibrium ionization networks "is not yet clear" (§2).
3. **Semi-discrete equation** (eq. 9), zeroth-order finite-volume in space, with
   $\bar T_i$ from $\bar\rho_i$ and $\bar P_i$.
4. **Explicit updates** (§3.1, eqs. 11–15). Forward Euler
   $\bar T_i^{n+1} = \bar T_i^n[1 - \Delta t/t_{cool}]$ with the single-point cooling
   time $t_{cool}$ (eq. 13); RK2 (eqs. 14–15). Both depart strongly from the
   exact solution as $\Delta t \to t_{cool}$ (Fig. 1); remedies are sub-stepping or
   higher order, each order costing one more $\Lambda$ evaluation.
5. **Implicit updates are not robust** (§3.2, eqs. 16–21, Figs. 2–4).
   Backward Euler (eq. 17) and Crank–Nicolson (eq. 21), root-found by secant
   (bisection fallback) or Brent to a fractional change below $10^{-4}$. At
   $\bar T_i^n = 10^6$ K backward Euler underestimates $\bar T_i^{n+1}$ for
   $0.3\,t_{cool} \lesssim \Delta t \lesssim 0.7\,t_{cool}$ and overestimates it above,
   with abrupt jumps (Fig. 2). The discriminants (eqs. 18–19) intersect five
   times at $\Delta t = 0.3\,t_{cool}$, so eq. 17 has five roots there (Fig. 3).
   Crank–Nicolson also jumps, over a reduced range (Fig. 4). The
   "unconditionally stable" claims of Strickland & Blondin (1995), Pittard et
   al. (2004) and Stone et al. (1997) are called "misplaced": von Neumann
   stability holds for linear equations, not the nonlinear eq. 9. Spurious
   flows from neighbouring zones jumping to different roots are asserted, not
   demonstrated.
6. **EI scheme** (§3.3, eqs. 22–26). With
   $Y(T) = \frac{\Lambda(T_{ref})}{T_{ref}}\int_T^{T_{ref}}\frac{\mathrm dT'}{\Lambda(T')}$
   (eq. 24), the update is
   $\bar T_i^{n+1} = Y^{-1}\left[Y(\bar T_i^n) + \frac{\bar T_i^n}{T_{ref}}\frac{\Lambda(T_{ref})}{\Lambda(\bar T_i^n)}\frac{\Delta t}{t_{cool}}\right]$
   (eq. 26), exact for eq. 9 and any $\Delta t$. Exactness is with respect to the
   semi-discrete isochoric sub-step; the splitting error is not discussed.
   Mignone's (2005) analytic cooling is the power-law special case.
7. **Closed-form TEFs** (Appendix, eqs. A1–A7). Power law and piecewise power
   law, with constants $Y_k$ by a downward recurrence from $Y_N = 0$. The need
   for $1/\Lambda$ to be analytically integrable is "rarely an issue" (§5).
8. **Time-step interplay** (§4, eqs. 28–30). With a CFL step and subsonic
   post-shock flow, $\Delta t/t_{cool} \lesssim 1/N$ for $N$ zones across the cooling
   region: a resolved cooling layer implies $\Delta t \ll t_{cool}$, where all schemes
   are accurate; non-EI schemes fail when it is under-resolved. An optional
   limiter on the fractional temperature/pressure change per step is mentioned,
   with no threshold.
9. **Cost and recommendation** (Table 1, §4–§5). First-order explicit ~100 ns
   per zone; RK2 and EI ~2× slower, EI faster than RK2 "in all but two tests";
   implicit 2.5–12× the first-order explicit cost. EI is recommended as "the
   cooling scheme of choice" for simple, fast, robust optically thin losses;
   ionization-tracking treatments (Mignone et al. 2007) remain the state of the
   art for fidelity.

**Tests.** Single-zone sweeps in $\Delta t$ at $\bar T_i^n = 10^6, 10^7, 10^8$ K, with
$\Lambda$ a piecewise power-law fit to the Gnat & Sternberg (2007) CIE table, a
$10^4$ K floor, $\gamma = 5/3$, $X = 0.7$, $Z = 0.02$ (Figs. 1–4). Steady 1D
radiative shock (§4, Table 1): post-shock profile after Strickland & Blondin
(1995), $\mathcal M_{in} = 3, 10, 100$, $N = 1, 10, 100$ zones, $\Delta t = \Delta x/c_{max}$
(Courant number 1), one cooling step on a frozen profile, error = max relative
temperature error against EI (eq. 27), on one core of an Intel E5345 at 2.33
GHz. The error falls with $N$; at $N = 10$ it is below 10% except first-order
explicit at $\mathcal M_{in} = 3$ (14.1%); at $N = 100$ below 1% everywhere; at
$N = 1$ the implicit schemes reach 99.9% at $\mathcal M_{in} = 100$. No
time-dependent hydro run and no convergence order.

# Notation map

| Townsend (2009) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $P$ | $p$ | thermal pressure |
| $\rho$, $\gamma$, $T$ | $\rho$, $\gamma$, $T$ | |
| $\mathrm d/\mathrm dt$ | none (words) | Lagrangian derivative |
| $\Lambda(T)$ | none (words) | cooling efficiency |
| $n_e$, $n_H$, $n$ | none (words) | number densities; **collision:** bare $n$ against the time-level superscript of $t^n$ |
| $k$ | none (words) | Boltzmann constant |
| $\mu$, $\mu_e$, $\mu_H$, $\mathrm u$ | $\mu m_{\mathrm H}$, $\mu_{\mathrm e}m_{\mathrm H}$, $\mu_{\mathrm H}m_{\mathrm H}$; words | dimensional mean masses per particle, electron, H (the registry's $\mu$ is dimensionless); atomic mass unit $\mathrm u$ **collides** with registry $u$ |
| $X$, $Z$ | none (words) | hydrogen and metal mass fractions |
| $\bar\rho_i$, $\bar P_i$, $\bar T_i$ | $\rho$, $p$, $T$ averaged over $I_i$ | |
| $\Delta t$, superscript $n$ | $\Delta t$, $t^n$ | |
| $\Delta x$ | $h$ | |
| $c_{max}$ | $\max_i c_s$ | |
| $t_{cool}$, $Y(T)$, $T_{ref}$, $\Lambda_{ref}$ | none (words) | cooling time, temporal evolution function, reference values |
| $\alpha$, $\alpha_k$, $\Lambda_k$, $T_k$, $Y_k$ | none (local) | power-law fit parameters; **paper-internal collision:** $N$ is the node count (Appendix) and the zone count (§4) |
| $\mathcal M_{in}$, $\rho_{in}$, $T_{in}$ | none (words) | upstream Mach number, density, temperature |
| $D_a$, $D_b$, $\varepsilon$ | none (local) | discriminants, max relative error |
| $\tau$ | none (words: CPU time per zone) | **collision** with registry $\tau$ |

# Pages created or updated

* Created [Integrating cooling and chemistry source terms](/methods/radiative-cooling-integration.md).

# Citations

1. `~/papers/mosaic/astrophysical-simulation-codes/2009-ApJS-Townsend-1010880067-00491812391.pdf`.
   * **Version.** arXiv:0901.3146v2 (13 Feb 2009), emulateapj preprint, 7
     pages (consistent with the published 391–397); the header "Draft version
     October 22, 2018" is the arXiv re-typesetting date. Not the typeset
     article; equation and table numbering not checked against it.
   * **Identity.** doi:10.1088/0067-0049/181/2/391, checked on Crossref: title
     as on page 1, sole author Townsend, Astrophys. J. Suppl. Ser.
     181(2):391–397, issued 2009-03-12.
   * **How it was read.** Text extraction, all sections; every equation read
     from rendered pages 1, 2, 5, 7. Figures 1–4 not digitized; quantitative
     statements taken from the text.
   * **Recorded as printed.** The text says "five cooling schemes"; Table 1
     has seven rows (the two implicit orders each with two root-finders).
     "Crank-Nicholson" spelling. $T_{in}$ of the shock benchmark, and the
     coefficients and segment count of the piecewise fit, are not given; the
     $Y$-table search method is not described.
   * **Reference list:** 22 printed entries, alphabetical; titles only for
     the two books (Laney 1998; Press et al. 1992); no DOIs.
