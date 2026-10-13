---
type: Source
title: "Colella & Glaz (1985) — Efficient Solution Algorithms for the Riemann Problem for Real Gases"
description: "Riemann solvers for 1D gas dynamics with a general convex equation of state: an exact secant or Newton solver, and an approximate one that carries two dimensionless indices (the generalized adiabatic index and an energy index), advances the energy index across each wave by a limited jump relation and treats both waves with the shock jump formula; it needs one pressure evaluation per point per dimension per step, keeps second order, and costs about 40 % more than the polytropic solver excluding the EOS call."
resource: "doi:10.1016/0021-9991(85)90146-9"
source_kind: paper
authors: [Colella P., Glaz H.M.]
year: 1985
venue: "J. Comput. Phys. 59:264–289"
local_file: "/home/stefano/papers/mosaic/astrophysical-simulation-codes/1985-JCP-Colella-1010160021-99918590146-9.pdf"
tags: [riemann-solver, equation-of-state, hydro, verification, performance]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper builds Riemann solvers for 1D gas dynamics with a general
convex equation of state $p = p(1/\rho, e)$ that can be used in
second-order Godunov schemes at almost the cost of the polytropic case.
§1 gives the exact solution: wave curves in the pressure–velocity plane,
solved by a secant or a Newton iteration on the mean Lagrangian wave
speeds, with closed-form shock derivatives. Because the exact solution
needs many EOS evaluations (inner iterations and integration through
rarefactions), §2 replaces the EOS by a local model: two dimensionless
indices, $\Gamma_1$ and an energy index $p/(\rho e) + 1$, are carried as
extra variables; the energy index is advanced across each wave by a
limited jump relation, which gives the wave speed in closed form, and both
waves are treated with the shock jump formula, states inside a fan being
linearly interpolated. The method needs one pressure evaluation (plus
$\Gamma_1$) per point per dimension per step. It is built into Lagrangian
and single-step Eulerian second-order Godunov schemes, tested on a
high-explosive/air shock tube and on complex Mach reflection in air with
three EOSs against experiment, and costs about 40 % more than the
polytropic solver, excluding the EOS call (§§3–4). See
[general equations of state](/methods/general-equation-of-state.md) and
[approximate Riemann solvers](/methods/approximate-riemann-solvers.md).

# Key claims

Formulas below are in the **paper's notation**, because three of its
symbols collide with the registry (see the Notation map): $\tau = 1/\rho$
is the specific volume, $c$ the sound speed, $W$ a Lagrangian wave speed
(mass flux), $\gamma$ the energy index (not the ideal-gas constant); the
paper's $\Gamma$ is the registry $\Gamma_1$.

1. **Admissibility** (§1, after eq. 4). $p_\tau < 0$, $p_e > 0$ are
   "sufficient [17] but not necessary [20]" for hyperbolicity and a unique
   Riemann solution; convexity ($\partial^2p/\partial\rho^2$ at constant
   entropy $> 0$) is assumed, so only shocks and rarefactions occur.
2. **Indices** (eqs. 5–8). $c^2 = \tau^2(pp_e - p_\tau)$ (eq. 5),
   $C = \rho c$ (eq. 6), $\Gamma = C^2/(p\rho)$ (eq. 7),
   $\gamma = p\tau/e + 1$ (eq. 8). "For polytropic gases, $\gamma$ is the
   ratio of specific heats and $\gamma = \Gamma$. Neither statement is
   true in general."
3. **Exact solver** (§1, eqs. 12–24). Rankine–Hugoniot conditions
   $[u] = \pm[p]/W$, $W^2 = -[p]/[\tau]$, $[e] = -\bar p[\tau]$ (eq. 12);
   rarefaction ODEs (eq. 13); the mean Lagrangian wave speed (eq. 16); the
   star state from $u_{*L}(p_*) = u_{*R}(p_*)$ (eq. 17), by a secant
   iteration started from two Godunov iterations (eq. 18), or by van Leer's
   Newton iteration with closed-form shock derivatives (eqs. 19–23). The
   wave curves are $C^2$ at the initial states and $C^\infty$ elsewhere.
4. **Secant preferred** (§1, p. 272): "the thermodynamic derivatives $p_e$
   and $p_\tau$ often are not available in real gas equation of state
   software. If they are available, their accurate computation requires
   extra work". If the post-wave $\gamma$ is known, the inner iteration for
   $W^2$ disappears (eq. 24).
5. **Local EOS model** (§2, pp. 272–273). The method needs "only one
   evaluation of the pressure per mesh point per dimension per time step"
   (plus $\Gamma$). It works because "$\gamma$ is a slowly varying function
   of the thermodynamic variables for real gases: although $p, \rho, e$ may
   vary over many orders of magnitude, $\gamma$ stays in the range
   $1 < \gamma \le \frac53$", and because with a post-jump $\gamma$ the
   jump conditions solve "at essentially the same cost as in the polytropic
   case". Compressible water, where $\gamma$ is not slowly varying, "might"
   need another parametrization.
6. **Dynamics of $\gamma$** (eqs. 26–27). Along the streamline
   characteristic
   $$\frac{d\gamma}{d\sigma_0} = \left(1 - \frac{\gamma}{\Gamma}\right)(\gamma - 1)\frac{1}{p}\frac{dp}{d\sigma_0},$$
   and across a jump the same relation holds to $O\big((p_* - p_0)^3\big)$,
   because the Hugoniot and rarefaction curves have second-order contact.
7. **Approximate solver** (eqs. 28–35). $W^2(e_{*S} - e_S) = \tfrac12(p_*^2 - p_S^2)$
   (eq. 28) with $e = p\tau/(\gamma - 1)$ on each side (eqs. 29–30); the
   post-wave index
   $$\hat\gamma_{*S} = \gamma_S + \left(1 - \frac{\bar\gamma}{\bar\Gamma}\right)(\bar\gamma - 1)\frac{p_* - p_S}{\tfrac12(p_* + p_S)}$$
   (eq. 31, bars the arithmetic means of the two initial states, eq. 33),
   clipped to $[\gamma_{\min}, \gamma_{\max}]$, e.g. the extremes of $\gamma$
   over neighbouring points (eq. 32). Then
   $$W^2 = \frac{(p_* - p_S)\left(p_* + \tfrac12(\gamma_{*S}-1)(p_*+p_S)\right)}{p_*\tau_S - \frac{\gamma_{*S}-1}{\gamma_S - 1}p_S\tau_S}$$
   (eq. 34), "exact in the case of a polytropic equation of state"; its
   weak-wave limit $W^2 = \Gamma_Sp_S\rho_S + O(U_L - U_R)$ (eq. 35) makes
   $(u_*, p_*)$ "correct to second order in the jumps".
8. **Two-shock approximation** (p. 275). "The shock jump formula (28) is
   used to compute $W^2$ even for rarefaction waves"; the error is argued
   to be of higher order than the truncation error of a second-order
   scheme, and strong rarefaction jumps are "an extremely rare occurrence"
   because expansions spread over several zones. Inside a fan $p, u, \rho,
   \gamma$ are interpolated linearly between the pre- and post-wave
   states. Hence "a Godunov-type scheme which is second order accurate in
   smooth flow remains so".
9. **Lagrangian scheme** (eqs. 36–41). $p, u, \tau$ are interpolated (PPM or
   piecewise linear), $\gamma$ and $\Gamma$ are piecewise constant (eq. 39);
   this suffices for second order because the Lagrangian fluxes involve only
   $p_*$ and $u_*$ (eq. 41). Only the iteration is needed, no sampling.
10. **Eulerian single-step scheme** (eqs. 42–48). $\gamma$ must be
    interpolated, because "a value for $\gamma$ is required to compute the
    energy flux": piecewise linear $\rho, p, u, \gamma$ with Colella's
    slopes (a fourth-order central difference in smooth regions),
    characteristic tracing of the waves approaching the interface, and the
    interface $\gamma$ from the characteristic relation (eq. 26), limited
    (eq. 47). The energy flux is $\rho u(u^2/2 + \gamma p/(\rho(\gamma-1)))$
    at the interface state (eq. 48).
11. **Cost** (§4, Cray 1 timing table, μs per zone per step): full
    real-gas algorithm 24.2; EOS call replaced by a dummy with
    $\gamma = \Gamma = 1.4$, 18.2; also the constant-$\gamma$ Riemann solver,
    14.2; also without the $\gamma$ interpolation and characteristic
    calculation, 12.8. The real-gas overhead excluding the EOS call is
    5.4 μs, "about a 40% increase", mostly in the Riemann solver, much of it
    from "guarding against zero denominators" in eqs. 18 and 34; it is
    "still smaller than the time required to perform the single EOS
    evaluation".
12. **Tabulated EOS** (§4). Gilmore sound speeds from numerically
    differentiated tabulated pressure gave "the same stability and
    robustness" as Hansen with analytic sound speeds. An Osher-type solver
    that integrates along the isentrope "could be quite expensive";
    differentiating a sparse table for $c$ via eq. 5 might cause
    instabilities.
13. **Limiting $\gamma$ is critical** (§4, p. 288). In compressible water,
    with an order-of-magnitude jump in $\gamma$ across the shock, results
    were "of comparable quality": "We feel that the limiting of $\gamma$
    given by (32) is critical to the success of the algorithm in these
    regimes". No water data are shown.

# Tests

No convergence rate is measured: second order is argued analytically
(eqs. 35, 41).

1. **High-explosive / air shock tube** (§3, Fig. 3). 1D, 180 zones,
   discontinuity between zones 60 and 61. Left: PBX-9404 detonation
   products with the JWL EOS (coefficients not printed, taken from the
   cited report); right: air with the Gilmore EOS. Initial data (cgs):
   $(\rho, e, u)_L = (2.0,\ 6.0\times10^{11},\ 0)$,
   $(\rho, e, u)_R = (1.2913\times10^{-3},\ 2.0\times10^{9},\ 0)$. The
   material interface is tracked by an advected air fraction; mixed cells
   use averaged indices. "Good agreement" with the exact §1 solver; a slight
   internal-energy undershoot left of the contact is "a starting error,
   which occupies a fixed number of zones as the mesh is refined"; monotone
   shock profiles. Visual comparison only.
2. **Complex Mach reflection in air** (§3, Figs. 4–9). 20° ramp, shock
   Mach number 7.19, ambient $(\rho, p) = (9.29\times10^{-5},\ 8.0\times10^{4})$
   cgs; $510\times120$ square zones of 1/35 cm; Strang-type operator
   splitting. Three EOSs: perfect gas with $\gamma = 1.4$, Gilmore and
   Hansen (the last two as vectorized table look-ups). The large-scale
   structure agrees in all three; the details differ (Mach stem length,
   triple-point angles, a second triple point with Gilmore and Hansen but
   not with $\gamma = 1.4$; the longest jet with Gilmore). Against the
   experimental wall density, after a shift to match the equilibrium
   region, Hansen agrees "within 2–3 %" over most of the profile, while
   $\gamma = 1.4$ and Gilmore disagree "by substantial percentages". A
   spurious "hot spot" at $x/L \approx 0.4$ in all runs comes from the
   analytic discrete shock used as upper boundary condition. Vibrational
   nonequilibrium (about 10 % of the jumps) is not modelled.
3. **Timing** (§4): claim 11, on the 1D shock tube of test 1, Cray 1 with
   the CFT compiler.

# Notation map

| Paper | Canonical | Note |
|---|---|---|
| $U$, $F(U)$ | $u$, $f(u)$ | |
| $\rho$, $u$, $p$ | $\rho$, $v_x$, $p$ | 1D velocity |
| $E = e + \tfrac12u^2$ | $E/\rho$ | specific total energy; registry $E$ is per volume |
| $e$ | $e$ | specific internal energy |
| $\tau = 1/\rho$ | $1/\rho$, in words | **collision**: registry $\tau$ is the Valencia energy or an optical depth |
| $c$ | $c_s$ | **collision**: registry $c$ is the speed of light |
| $C = \rho c$ | $\rho c_s$, in words | Lagrangian sound speed; **collision** with $C_i$ |
| $\Gamma = C^2/(p\rho)$ | $\Gamma_1$ | identical to $\rho c_s^2/p$ |
| $\gamma = p\tau/e + 1$ | in words ("energy index", $p/(\rho e) + 1$) | **collision** with the ideal-gas $\gamma$, which it equals only for a polytropic gas; no registry symbol (proposed $\gamma_{\mathrm e}$) |
| $W$, $W_S$ | in words | Lagrangian wave speed; **collision**: registry $W$ is the Lorentz factor |
| $p_*$, $u_*$, $\gamma_{*S}$ | in words | star (post-wave) states |
| $\lambda^\pm$, $\lambda^0$ | $\lambda^{(p)}$ | eigenvalues $u \pm c$, $u$ |
| $A(V)$, $V = (\tau, u, p)$ | in words | primitive-variable Jacobian; registry $A(u)$ is the conservative one |
| $x_{j+1/2}$, $\Delta x_j$, $U^n_j$ | $x_{i+1/2}$, $h$, $u^n_i$ | non-uniform $h$ allowed |
| $V^{n+1/2}_{j+1/2,L/R}$ | $u^-_{i+1/2}$, $u^+_{i+1/2}$ (primitive) | |
| $F_{j+1/2}$ | $\hat f_{i+1/2}$ | |
| $\alpha$, $M_s$ | in words | ramp angle, shock Mach number |
| JWL $A, B, R_1, R_2, \omega, V$ | in words | **collision**: $A$, $\mathbf B$ |

# Pages created or updated

* Created this Source page.
* Updated [General equations of state in Godunov codes](/methods/general-equation-of-state.md)
  (batch-10 section: transported indices, the minimum EOS information,
  admissibility conditions, tabulated EOS and the $\gamma$ limiter).
* Updated [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md)
  (batch-10 section: the general-EOS origin of the two-shock structure,
  secant over Newton, cost).
* Updated
  [Berger & Colella (1989)](/sources/berger-1989.md) (the low-$\gamma$
  statement does not rest on this paper), and a variants line for
  [double Mach reflection](/benchmarks/double-mach-reflection.md).

# Citations

1. Colella P., Glaz H.M. (1985), "Efficient solution algorithms for the
   Riemann problem for real gases", J. Comput. Phys. 59(2):264–289,
   doi:10.1016/0021-9991(85)90146-9. Local file:
   `/home/stefano/papers/mosaic/astrophysical-simulation-codes/1985-JCP-Colella-1010160021-99918590146-9.pdf`.
   * **Version read.** The published journal version (26-page scan with an
     OCR text layer; received January 5, 1984, revised May 31, 1984). Not a
     preprint. Preliminary versions named in the paper: the Aachen 1982
     proceedings (ref. 5) and Colella's report LBL-14442 (ref. 4). The
     bibliography's `colella-1983` (Colella & Glaz, LBL-15776, "Efficient
     Algorithms for the Solution of the Riemann Problem for Real Gases") is
     not cited here; its title suggests a report version of this paper, not
     verified.
   * **Identity.** Checked on Crossref: title, the two authors, vol. 59,
     issue 2, pp. 264–289, issued 1985-06; agrees with page 1 (the DOI is
     the PII printed there).
   * **How it was read.** Every equation quoted was read from rendered
     pages (110 dpi; 250 dpi for eq. 35), because the OCR garbles the
     displays. Eqs. 43–46 (characteristic tracing with reference states and
     projections) were not rendered and are described in structure only;
     eq. 47 was rendered for the right state only (p. 280). Figs. 3 and 5–9
     were not read quantitatively beyond the text.
   * **Recorded as printed.** The JWL coefficients for PBX-9404 are not
     printed. The water results (claim 13) are asserted without data.
   * **Reference list:** 24 printed entries, all merged. Colella's MUSCL
     paper (SIAM J. Sci. Stat. Comput. 6:104) is `colella-1985-c`, not
     `colella-1985` (this paper). Colella's LBL-14442 report, printed
     1982, is the existing `colella-1984-d` (same title and report number,
     year from another citer). The Aachen proceedings of Colella & Glaz, no
     publication year printed, is `colella-1982-c` with the conference year.
     Glaz et al. ("in press", series printed "Proc. R. Soc. Lond. B", kept
     as printed) and Glaz & Wardlaw ("expected to appear") are keyed with
     the citing year (`glaz-1985`, `glaz-1985-b`). Dobratz (UCRL-51319) is
     printed as editor. The Woodward–Colella blast-wave paper (54:115) and
     PPM (54:174) land on `woodward-1984` and `colella-1984`. Bibliography:
     2522 entries.
