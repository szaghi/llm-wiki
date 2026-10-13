---
type: Source
title: "Einfeldt (1988) — On Godunov-type methods for gas dynamics"
description: "HLL for the 1D Euler equations with speeds that need not bound the physical signal speeds but must satisfy a stability condition (the clipped speeds bracket the Roe eigenvalues); a contact anti-diffusion term inside the fan (the later HLLEM) that with Roe-eigenvalue speeds reproduces Roe's flux; two speed algorithms, the Roe eigenvalues (HLLR) and a sqrt(rho)-weighted sound speed (HELL); a min/max entropy modification at sonic rarefactions; no positivity result."
resource: "doi:10.1137/0725021"
source_kind: paper
authors: [Einfeldt B.]
year: 1988
venue: "SIAM J. Numer. Anal. 25:294–318"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/1988-SINUM-Einfeldt-1011370725021.pdf"
tags: [riemann-solver, hll, hllem, wave-speed, entropy, euler]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

Einfeldt builds an approximate Riemann solver for the 1D Euler equations
on Harten, Lax & van Leer's two-wave model. He computes only
approximations to the smallest and largest signal speeds and estimates no
contact pressure or velocity (§§1, 3). Unlike the 1983 paper, the speeds
are **not assumed** to bound the physical signal speeds (p. 298); they are
constrained instead by a stability condition, that the numerical viscosity
matrix have nonnegative eigenvalues, which holds iff the clipped speeds
bracket the eigenvalues of a Roe-type linearization (eqs. 4.4–4.7). An
anti-diffusive linear variation along the contact eigenvector inside the
fan (eqs. 3.12–3.15), the solver later called
[HLLEM](/methods/hllem-riemann-solver.md), reproduces Roe's flux exactly
with Roe-eigenvalue speeds and a particular weight (4.21): "a new
interpretation of Roe's scheme" (§7). Two speed algorithms are given: the
Roe eigenvalues (5.1), the "HLLR" method, and a $\sqrt\rho$-weighted
sound-speed estimate (5.7–5.8) meant to extend to general convex equations
of state, the "HELL" method. A min/max modification (4.11) removes the
entropy-violating stationary shock at sonic rarefactions. Tests: Sod, Lax,
a sonic rarefaction, and 2D shock focusing with a second-order extension.

# Key claims

1. **The solver** (§3, eqs. 3.3–3.7′). Three constant states separated at
   $S_L t$ and $S_R t$; the middle one is fixed by consistency with the
   integral form (3.4). The flux is the three-branch HLL flux (3.7), and in
   one formula with $S_L^-$, $S_R^+$ (3.7′). $S_L$, $S_R$ are
   "Lipschitz-continuous approximations to the smallest and largest
   physical signal velocities"; "In contrast to the original version, we do
   not assume that the numerical signal velocities … are lower and upper
   bounds for the physical signal velocities" (p. 298).
2. **Isolated waves** (eqs. 3.8–3.10). If the algorithm returns the shock
   speed as $S_L$ (or $S_R$), an isolated shock is exact; an isolated
   contact lies strictly inside the fan and is smeared, "a rather rough
   approximation".
3. **Contact anti-diffusion** (eqs. 3.11–3.15), not named HLLEM here.
   Inside the fan the state varies linearly along the contact eigenvector
   $r^{(2)}$, with strength $\ell^{(2)}(u^+ - u^-)$; the velocity and sound
   speed in $r^{(2)}$, $\ell^{(2)}$ are **read off the speeds**,
   $\tfrac12(S_L + S_R)$ and $\tfrac12(S_R - S_L)$ (3.14), not taken from a
   Roe average: "The approximate solution (3.12) is thus completely defined
   by the numerical signal velocities" (p. 299). Conservation is unchanged;
   the flux is the HLL flux minus the anti-diffusive term (3.15). 1D Euler
   has one intermediate (contact) field and no shear field.
4. **Viscosity form and stability condition** (§4, eqs. 4.1–4.8). The HLL
   flux is $\tfrac12\left(f(u^-) + f(u^+)\right) - \tfrac12\Theta_{i+1/2}(u^+ - u^-)$
   with $\Theta_{i+1/2}$ a combination of the Roe-type matrix $A$ and the
   identity (4.2); its eigenvalues are
   $\left((S_R^+ + S_L^-)\lambda^{(p)} - 2S_R^+S_L^-\right)/(S_R^+ - S_L^-)$
   (4.4, compiler's expansion), with $\lambda^{(p)}$ the Roe-matrix
   eigenvalues. The necessary condition that they be nonnegative (4.5) "is
   satisfied if" $S_L^- \le \lambda^{(p)} \le S_R^+$ for every $p$ (4.6);
   with strict inequality the scheme is "dissipative of order two", and for
   linear $f$ $L_2$-stable by the Kreiss theorem. The TVD-type condition that
   each eigenvalue be at least $\vert\lambda^{(p)}\vert$ (4.7) gives TVD for
   linear or scalar $f$ under a CFL bound (4.8, after Harten) and "holds if
   and only if the signal velocities satisfy (4.6)" (p. 300).
5. **Least shock dissipation at the Roe eigenvalue** (eqs. 4.9–4.10). A
   single shock moves at a Roe eigenvalue; the dissipation on that field is
   at least the shock speed's magnitude, with equality iff $S_L$ equals it.
   A stationary shock is then resolved perfectly, but "the scheme may admit
   a stationary nonphysical discontinuity" (p. 301).
6. **Entropy modification** (eqs. 4.11–4.12). $S_L$ is replaced by its
   minimum with $v_n^- - c^-$ and $S_R$ by its maximum with $v_n^+ + c^+$
   (the page prints $\mu_i - c_i$, read as $v_n^- - c^-$). By Lax's entropy
   inequality (citing Smoller) shock resolution is unchanged, and the
   modification adds "enough numerical dissipation to avoid the occurrence
   of a nonadmissible discontinuity". **An argument, not a proof**; checked
   numerically (Figs. 10–12).
7. **Contact dissipation exceeds Godunov's** (eqs. 4.13–4.14): "the
   numerical dissipation for a nearly stationary contact discontinuity is
   larger than it is for Godunov's method".
8. **Roe's scheme as HLL plus contact anti-diffusion** (eqs. 4.15–4.22).
   The anti-diffusion weight "should be chosen such that the stability
   condition (4.7) is valid for $k = 2$" (the contact field). With
   $S_L^- = \min(\lambda^{(1)}, 0)$, $S_R^+ = \max(\lambda^{(3)}, 0)$ at the
   Roe state (4.19) and the weight (4.20), equivalent to the dimensionless
   $\delta_p = c_{\mathrm{Roe}}/(c_{\mathrm{Roe}} + \vert v_{n,\mathrm{Roe}}\vert)$
   (reader's algebra), the viscosity term equals Roe's (4.21): "Roe's scheme
   can be considered as a Godunov-type method (3.7) with an antidiffusion
   term in the linear degenerate field" (p. 302). The Remark gives Roe's
   flux in this eigenvector-light form (4.22). **No weight is given for
   other speeds.**
9. **Speed algorithm 1, "HLLR"** (eqs. 5.1–5.3).
   $S_{L,R} = v_{n,\mathrm{Roe}} \mp c_{\mathrm{Roe}}$, with
   $\sqrt\rho$-weighted velocity and total enthalpy.
10. **Speed algorithm 2, "HELL"** (eqs. 5.4–5.10). The exact identity
    (5.4) writes $c_{\mathrm{Roe}}^2$ as the $\sqrt\rho$-weighted mean of
    $(c^\mp)^2$ plus a coefficient $\eta_\gamma$ times $(v_n^+ - v_n^-)^2$
    (5.5). Since $\eta_\gamma$ is below its value at $\gamma = 2$ (stated for
    "most gases", $1 < \gamma < 5/3$, 5.6), replacing it by that value gives
    $$\bar c_{\mathrm E}^2 = \frac{\sqrt{\rho^-}\,(c^-)^2 + \sqrt{\rho^+}\,(c^+)^2}{\sqrt{\rho^-} + \sqrt{\rho^+}} + \frac12\,\frac{\sqrt{\rho^-\rho^+}}{(\sqrt{\rho^-} + \sqrt{\rho^+})^2}\,(v_n^+ - v_n^-)^2 \quad (5.7),$$
    and $S_{L,R} = v_{n,\mathrm{Roe}} \mp \bar c_{\mathrm E}$ (5.8). They are
    "well defined for a general convex equation of state" (5.9), and since
    $\bar c_{\mathrm E} > c_{\mathrm{Roe}}$ (5.10) they "satisfy the
    stability requirement (4.6) for any $\gamma$-law gas"; the question for
    a general equation of state is left open. For weak shocks both are
    second-order close to arithmetic means (5.11).
11. **What the paper does not contain.** No positivity statement or proof
    (the word does not occur; positivity of density or pressure is not
    discussed); no entropy theorem beyond claim 6; no convergence proof. The
    names "HLLE" and "HLLEM" do not occur; the only names are "HLLR" and
    "HELL" (§6, p. 304). The anti-diffusive solver (3.15) is never run.

# Tests

All 1D runs are first order; $\gamma$ is not printed for them (the plotted
minima fit $\gamma = 1.4$, reader's check).

1. **Sod** (§6A, eq. 6.1, Figs. 4–6). 100 cells, CFL 0.8, 50 steps. HLLR
   spreads the contact over "sixteen to eighteen zones", the shock over
   "two to four zones"; Godunov (exact iterative solver) is "almost equal",
   with a slightly sharper contact and right rarefaction corner; Roe is the
   same as Godunov but for a slightly more rounded corner; HELL (not shown)
   is "identical to the plot of Fig. 4"
   ([Sod shock tube](/benchmarks/sod-shock-tube.md)).
2. **Lax problem** (§6A, eq. 6.2, Figs. 7–9). Primitive data
   $(\rho, v_x, p) = (0.445, 0.698, 3.528) \mid (0.5, 0.0, 0.571)$,
   attributed to "Lax in [11]" (Lax 1954), with "Other numerical
   experiments … reported in" Harten (1983). Grid and steps not restated.
   HLLR needs "about three more points" for the contact than Godunov; Roe
   is "nearly identical" to Godunov
   ([Lax shock tube](/benchmarks/lax-shock-tube.md)).
3. **Sonic rarefaction** (§6A, eq. 6.3, Figs. 10–12). Right state
   $\rho = 1.205$, $v_x = 0$, $p = 10$; left state on the same 3-family
   rarefaction with $c^- = \frac{3-\gamma}{\gamma+1}c^+$ and
   $v_x^- = -(c^+ + c^-)$, so the fan crosses a sonic point (reader's
   check). 100 cells, 80 steps, CFL 0.8. Godunov shows the known "kink";
   Roe "admits an entropy violating stationary shock" (Fig. 11), and "The
   same entropy violation occurs for the HLLR scheme" (not shown); HLLR
   with (4.11) is "nearly identical to that of the Godunov scheme. The
   'kink' in the solution is even smaller" (Fig. 12). (4.11) "does not
   alter the numerical results for the two preceding test problems"; a
   nonphysical discontinuity is "only possible if there is a sonic point in
   an expanding region".
4. **2D shock focusing by a parabolic reflector** (§6B, Figs. 13–17).
   Mach 1.1 plane shock in air ($\gamma = 1.4$), stepwise reflector,
   $90\times90$ upper half-plane, second-order Colella–Glaz PLM with
   dimensional splitting, with the exact solver, Roe or HLLR; set-up after
   Olivier & Grönig. Pressure contours with HLLR "very similar" to the
   exact solver's; Roe and exact pressure histories show "no difference";
   with HLLR a slightly lower first maximum and a slight "kink" behind the
   second shock.

# Notation map

| Einfeldt (1988) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $v = (\rho, m, e)^T$ | $u$ | **collision**: registry $\mathbf v$ is velocity |
| $u$ (velocity), $m$, $e$ | $v_x$ ($v_n$), $\rho v_x$, $E$ | **collision**: $u$; $e$ also the specific internal energy (p. 295) |
| $\tau$ (time step; also $1/\rho$ in 5.9) | $\Delta t$; specific volume in words | internal overload |
| $\Delta$, $\lambda = \tau/\Delta$ | $h$, $\Delta t/h$ | **collision**: $\lambda^{(p)}$ |
| $v_i$, $v_{i+1}$ | $u^-$, $u^+$ at $x_{i+1/2}$ | first order |
| $v_{i+1/2}$ | $u^{\mathrm{HLL}}_*$ | |
| $\omega_{i+1/2}(x/t)$ | words (Riemann solution) | **collision**: $\omega_k$ |
| $b^l$, $b^r$; $b^-$, $b^+$ | $S_L$, $S_R$; $S_L^-$, $S_R^+$ | |
| $g_{i+1/2}$; $h_{i+1/2}$ | $\hat f^{\mathrm{HLL}}$; $\hat f_{i+1/2}$ (HLLEM, Roe) | |
| $Q_{i+1/2}$ | $\Theta_{i+1/2}$ | same ½ convention |
| $A_{i+1/2}$, $\alpha^k$ | $A$ at the Roe state, $\lambda^{(p)}$ | **collision**: $\alpha$ |
| $\sigma^k$ | words (eigenvalues of $\Theta_{i+1/2}$) | |
| $\lambda_1$, $\lambda_3$ (4.11) | $v_n^- - c^-$, $v_n^+ + c^+$ | |
| $R^k$, $l^2$, $\eta^k$ | $r^{(p)}$, $\ell^{(p)}$, $\ell^{(p)}(u^+ - u^-)$ | |
| $\delta_{i+1/2}$ (dimension 1/time) | $\delta_p$ up to the factor $\Delta t\,c$ | reader's algebra, subsonic case |
| $\bar u$, $\bar c$ in §3 | $\tfrac12(S_L + S_R)$, $\tfrac12(S_R - S_L)$ | **internal overload**: the same letters are Roe averages in §5 |
| $\bar u$, $\bar H$, $\bar c$ in §5 | $v_{n,\mathrm{Roe}}$, $H_{\mathrm{Roe}}$, $c_{\mathrm{Roe}}$ | |
| $\bar d$ | $\bar c_{\mathrm E}$ | identical formula |
| $\eta_\gamma$, $\eta_2$ | words | letter collides with the wave strength $\eta^k$ |
| $c_i$ | $c^\mp$ | |

# Pages created or updated

* Updated [HLL Riemann solver and wave-speed estimates](/methods/hll-riemann-solver.md) (batch-18 block: speeds that need not bound, the stability condition, the origin of both "Einfeldt" formulas, no positivity result, the sonic-point qualification).
* Updated [HLLEM (HLLI) Riemann solver](/methods/hllem-riemann-solver.md) (batch-18 block: the 1988 construction, Roe's flux as HLL plus contact anti-diffusion, the weight given only for Roe speeds, no positivity).
* Updated [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md) (batch-18 block: "Two formulas called Einfeldt's" settled; the "HLL/HLLEM class" positivity attribution).
* Updated [Lax shock tube](/benchmarks/lax-shock-tube.md), [notation](/notation.md) (the mean velocity of $\bar c_{\mathrm E}$) and [Einfeldt et al. (1991)](/sources/einfeldt-1991.md).

# Citations

1. `/home/stefano/papers/mosaic/high-order-capturing-schemes/1988-SINUM-Einfeldt-1011370725021.pdf`.
   * **Version read.** The publisher's version (SIAM scan, 25 pages =
     pp. 294–318); received January 5, 1987, accepted April 14, 1987.
   * **Identity.** doi:10.1137/0725021 (not printed in the PDF), checked on
     Crossref: "On Godunov-Type Methods for Gas Dynamics", Einfeldt, SIAM J.
     Numer. Anal. 25(2):294–318, April 1988, reference count 26.
   * **How it was read.** The text layer garbles every equation; every
     formula was read from page renders at 130–300 dpi (pp. 297–304, 312,
     317–318). Figs. 4–9 and 13–16 were read only qualitatively, from the
     text.
   * **Recorded as printed** (reader's reading).
     - (3.7) middle branch prints the subscript $i+1/1$.
     - (4.2) prints the unclipped speeds where (4.4) uses the clipped ones.
     - (4.11) prints $\mu_i - c_i$, read as $u_i - c_i$ (velocity minus
       sound speed of the left cell).
     - (5.6) prints $\eta_2(\varphi_i, \varphi_{i+1})$ for
       $\eta_2(\rho_i, \rho_{i+1})$; (5.7) prints $c^2_{i+1/2}$ for
       $c^2_{i+1}$ (both corrected by (5.4) and the sense of the paragraph).
     - (5.10) is stated strict; by (5.4)–(5.7) it is an equality when the
       velocity jump is zero, still enough for (4.6).
     - The iterative Riemann solver of Fig. 13 is cited as [24] (Sod 1978),
       presumably [3] or [6].
     - $\gamma$ is not printed for the 1D tests, and the Lax test does not
       restate its grid or step count.
   * **Reference list:** 26 entries, all merged. Fryxell, Woodward,
     Colella & Winkler (J. Comput. Phys. 63:283), printed with Woodward
     first and the title "An implicit-explicit hybrid method for Lagrangian
     hydrodynamics", is `fryxell-1986`. Roe's paper, printed 53:357, is
     `roe-1981`; Roe's Lecture Notes in Physics 141 paper is `roe-1981-c`;
     Harten, Lax & van Leer is `harten-1983-d`; van Leer's SIAM J. Sci.
     Stat. Comput. 5:1 is `vanleer-1984-c`. Sommerfeld's submitted paper has
     no year and takes the received date (`sommerfeld-1987`). Godunov is
     printed with the title "A difference scheme for numerical computation
     …" and 47:271 (`godunov-1959`). Bibliography: 3380 entries.
