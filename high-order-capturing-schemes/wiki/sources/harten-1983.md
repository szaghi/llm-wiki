---
type: Source
title: "Harten (1983) — High resolution schemes for hyperbolic conservation laws"
description: "Defines total-variation-nonincreasing (TVD) schemes, proves monotone ⇒ TVD ⇒ monotonicity preserving and the incremental-form sufficient condition (Harten's lemma), notes after Godunov that a linear TVD scheme is first order, and builds explicit second-order TVD schemes by applying a first-order scheme to a flux modified with a limited antidiffusive term, extended to systems field by field with a Roe-type linearization and an entropy fix."
resource: "doi:10.1016/0021-9991(83)90136-5"
source_kind: paper
authors: [Harten A.]
year: 1983
venue: "J. Comput. Phys. 49:357–393"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/1983-JCP-Harten-1010160021-99918390136-5.pdf"
tags: [tvd, monotonicity, limiter, entropy-fix, riemann-solver, euler]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The first systematic construction of explicit, second-order, total
variation nonincreasing ("TVNI", the property this bundle calls
[TVD](/properties/total-variation-diminishing.md)) conservative schemes
for scalar conservation laws, extended to systems field by field. §2
defines TVNI, monotonicity-preserving and monotone schemes and proves
monotone ⇒ TVNI ⇒ monotonicity preserving (Theorem 2.1). It recalls,
after Godunov, that a *linear* monotonicity-preserving scheme is
monotone and therefore first order, so a second-order TVNI scheme must be
nonlinear ([Godunov's order barrier](/results/godunov-order-barrier.md)).
Lemma 2.2 gives sufficient conditions on the coefficients of the
incremental form. §3 applies a three-point first-order TVNI scheme to a
*modified flux*, the physical flux plus a limited, minmod-type
approximation of the first-order scheme's own leading error term. The
result is a five-point second-order scheme that is TVNI under the
original CFL restriction (Lemmas 3.2–3.4). §§4–6 extend it to systems
through a Roe-type characteristic decomposition and add the entropy fix.
§7 tests it on Euler problems: Lax's and Sod's shock tubes, stationary
shocks and an expansion shock, quasi-1D nozzles, and Woodward and
Colella's Mach 3 step on a $10\times30$ grid.

# Key claims

1. **TVNI** (§2, eqs. 2.2–2.5). A conservative scheme is TVNI if
   $TV(u^{n+1}) \le TV(u^n)$ for *all* $u^n$ of bounded total variation,
   $TV(u) = \sum_i \vert \Delta^1 u_i\vert$ (2.4). Motivation: the exact
   scalar solution creates no new extrema, so its total variation does
   not grow (2.2). The paper never uses the word "TVD".
2. **Three definitions and the hierarchy** (§2, p. 360). *Monotonicity
   preserving*: monotone mesh functions are mapped to monotone mesh
   functions. *Monotone*: the new value is a nondecreasing function of
   each of its $2k+1$ arguments (2.3a). **Theorem 2.1**: (i) a monotone
   scheme is TVNI; (ii) a TVNI scheme is monotonicity preserving. Proof of
   (i): monotone schemes are $l_1$-contractive (2.6a, from Crandall &
   Majda), applied to a solution and its shift. Proof of (ii): by
   contradiction on a monotone step profile (2.6b).
3. **Order statements** (§2, p. 361).
   * Monotone schemes approximate a viscous modified equation,
     $\partial_t u + \partial_x f(u) = \Delta t\,\partial_x[\beta(u)\,\partial_x u]$
     with a coefficient that is nonnegative and not identically zero
     (2.7), and are therefore "necessarily first order accurate". They
     converge, and the limit satisfies Oleinik's entropy condition, which
     fixes it uniquely (citing Crandall & Majda and Harten, Hyman & Lax).
   * A linear scheme, each new value a fixed linear combination of the
     $2k+1$ old values around it (2.8a), is monotonicity preserving iff
     all coefficients are nonnegative (2.8b), citing Godunov. "Hence any
     *linear* monotonicity-preserving scheme, and therefore any TVNI
     linear scheme, is a monotone scheme and consequently first order
     accurate."
   * This does not exclude *nonlinear* second-order TVNI or
     monotonicity-preserving schemes, which are then not monotone. Van
     Leer's and Harten's earlier schemes are cited as monotonicity
     preserving, "at least in the constant coefficient case", and second
     order.
4. **Harten's lemma** (§2, Lemma 2.2, eqs. 2.9–2.12). Write the explicit
   scheme in incremental form: the new value is the old value plus a
   coefficient times the forward difference $\Delta^1 u^n_i$ minus a
   coefficient times the backward difference $\Delta^1 u^n_{i-1}$, each
   coefficient a function of the four values around its interface
   (2.9). If both coefficients are nonnegative at every interface (2.10a)
   and their sum at each interface is at most 1 (2.10b), the scheme is
   TVNI. Proof: the new differences are combinations of three old
   differences with nonnegative coefficients (2.11); summing gives the
   result. Any three-point conservative scheme with a differentiable
   numerical flux can be put in this form by the mean value theorem
   (2.13). The lemma is stated for explicit schemes only; the proof of
   Lemma 3.4 uses it also for five-point schemes of the same form.
5. **First-order three-point TVNI family** (§3, Lemma 3.1, eqs.
   3.1–3.7). In registry form the flux is
   $\hat f_{i+1/2} = \tfrac12\left[f(u_i) + f(u_{i+1})\right] - \tfrac12\Theta_{i+1/2}\Delta^1 u_i$
   with the scalar numerical viscosity $\Theta_{i+1/2}$ a function
   ("the coefficient of numerical viscosity", the paper's $Q$) of the
   local Courant number $\hat a_{i+1/2}\Delta t/h$. If
   $\vert\hat a_{i+1/2}\vert \le \Theta_{i+1/2} \le h/\Delta t$ for
   every local Courant number up to a bound $\le 1$ (3.2), the scheme is
   TVNI when the Courant number of the Roe speeds stays below that bound
   (3.3). Lax–Wendroff, $\Theta_{i+1/2} = \hat a^2_{i+1/2}\Delta t/h$,
   violates (3.2). Under (3.2) the scheme is only first order: its flux
   differs from the Lax–Wendroff flux by $O(h)$ times the jump (after
   3.7). $\Theta_{i+1/2} = \vert\hat a_{i+1/2}\vert$ is "the least
   dissipative TVNI scheme of form (3.1)", a generalization of
   Courant–Isaacson–Rees upstream differencing (§5).
6. **Second-order TVNI by a modified flux** (§2 end, §3, eqs.
   2.14–2.16, 3.8–3.12). The first-order scheme approximates, to second
   order, a modified equation with an extra diffusive flux. Applying it
   to the flux $f$ *plus* a discrete approximation of that diffusive
   flux therefore gives a second-order approximation of
   $\partial_t u + \partial_x f(u) = 0$ (2.16). Discretely, the
   correction at node $i$ is the $\operatorname{minmod}$ of the two
   neighbouring interface values of
   $\tfrac12\left[\Theta_{i+1/2}\Delta t/h - (\hat a_{i+1/2}\Delta t/h)^2\right]\Delta^1 u_i$
   (3.11), up to the factor $h/\Delta t$ the antidiffusive flux that
   turns the first-order flux into the Lax–Wendroff flux; the
   correction also shifts the Courant number at which the viscosity is
   evaluated (3.8). **Lemma 3.2**: with a Lipschitz viscosity function
   and a correction satisfying (3.9), the flux is second order in the
   sense (3.6b). **Lemma 3.3**: the minmod correction satisfies (3.9).
   **Lemma 3.4**: the five-point scheme is TVNI under the *same* CFL
   restriction (3.3); the proof shows that the modified local Courant
   number is at most $1 - \tfrac12(\vert\hat a_{i+1/2}\vert\Delta t/h - 1)^2 \le 1$
   (p. 367).
7. **Where second order is lost** (§3, Remark 2, p. 368). Condition
   (3.6) is necessary, and sufficient only if the coefficient of the
   second-order error is differentiable except at finitely many points.
   The scheme "may degenerate locally" where the sign of the
   antidiffusive term jumps, "i.e., where $Q(\nu) - \nu^2 = 0$ or
   $u_x = 0$": at extrema. The §5 schemes are claimed to have the
   monotonicity property (number of local extrema nonincreasing), without
   proof.
8. **Simplified version** (§3, Remark 4, eq. 3.17). Adding the absolute
   value of the correction to the viscosity, instead of shifting its
   argument, keeps second order and TVNI under the same CFL; the
   antidiffusive flux at $x_{i+1/2}$ is then a three-argument
   $\operatorname{minmod}$ of the interface antidiffusive fluxes at
   $i-\tfrac12$, $i+\tfrac12$, $i+\tfrac32$. Harten notes its resemblance, with
   $\Theta_{i+1/2} = (h/\Delta t)\left[(\hat a_{i+1/2}\Delta t/h)^2 + \tfrac14\right]$,
   to Boris and Book's antidiffusion.
9. **Systems** (§4, eqs. 4.1–4.13). The scalar scheme is applied to each
   characteristic field, with any symmetric average state (4.6), the
   wave strengths $\ell^{(p)}\Delta^1 u_i$ and the eigenvectors $r^{(p)}$
   of the Jacobian at that state (4.7–4.8), a generalization of Roe's
   approach. **Lemma 4.2**: for constant $A$ the scheme is TVNI in the
   functional $\sum_i\sum_p \vert \ell^{(p)}\Delta^1 u_i\vert$ (4.12),
   motivated by Glimm's functional, under a CFL bound on all fields
   (4.13). **Corollary 4.3**: convergent and second order for constant
   coefficients. For nonlinear systems Harten has no estimate of the
   growth of the total variation "and therefore cannot prove
   convergence" (Remark 3, p. 373). Different viscosity functions, or
   even different scalar schemes, may be used per field (Remark 1).
10. **Roe linearization** (§§4, 6, eqs. 4.14–4.16, 6.3–6.4). A system
    with an entropy is symmetrizable, and a mean-value Jacobian with
    $f(u_{i+1}) - f(u_i) = A\,\Delta^1 u_i$ exists (citing Harten's ICASE
    report). For Euler it is the Jacobian at Roe's average,
    $v_{\mathrm{Roe}}$ and $H_{\mathrm{Roe}}$ the
    $\sqrt\rho$-weighted means and
    $c_{\mathrm{Roe}} = \left[(\gamma-1)(H_{\mathrm{Roe}} - \tfrac12 v_{\mathrm{Roe}}^2)\right]^{1/2}$
    (6.4); the Euler wave strengths are printed in closed form (6.3).
    "The averaging in (6.4) is rather expensive. Our experiments indicate
    that in many applications the simple arithmetic average (6.4b) will
    do just as well" (p. 380). The extension "does not require any
    particular form of averaging"; Roe's average additionally resolves
    stationary discontinuities perfectly (p. 371).
11. **Entropy violation and the entropy fix** (§5, eqs. 5.2–5.4). With
    $\Theta_{i+1/2} = \vert\hat a_{i+1/2}\vert$ (and Roe's linearization
    for systems), a stationary discontinuity with equal fluxes on both
    sides is a steady solution "regardless of whether or not it satisfies
    the entropy condition": "this scheme admits nonphysical solutions"
    (genuinely nonlinear fields only). The cause is that the viscosity of
    the modified equation vanishes at zero Courant number (5.2). The fix
    replaces the absolute value of the local Courant number, below twice
    a parameter $0 < \varepsilon_{\mathrm H} \le \tfrac12$ (written with a
    subscript here to keep it apart from the WENO $\varepsilon$), by the
    parabola equal to its square over four times the parameter plus the
    parameter (5.4), "with, say, $\varepsilon = 0.1$"; the remaining zero
    at Courant number 1 is avoided by a CFL bound below 1, say 0.95.
    Experiments with 0.05, 0.1, 0.25, and 0 on the linearly degenerate
    field: a larger parameter enforces the entropy condition better and
    costs resolution, but the dependence is "rather slight". The chosen
    values are 0.1 on genuinely nonlinear fields and 0 on linearly
    degenerate fields. Harten also remarks that Godunov's scheme
    "actually exhibits a surprisingly poor entropy enforcement" (p. 374,
    citing Harten & Hyman).
12. **Numerical characteristic speeds** (§5, eq. 5.6). The first-order
    scheme's numerical characteristic field diverges across a transition
    (excess smearing); the second-order correction gives a converging
    field of $O(h)$ that offsets it. The scheme is thus "an overdivergent
    numerical characteristic field on a suitably modified overconvergent
    characteristic field", offered as the heuristic reason for high shock
    resolution with strong entropy enforcement, uniform in shock
    strength, entropy-fix parameter and CFL number.
13. **Artificial compression in the linearly degenerate field** (§5,
    eqs. 5.7–5.8). An extra limited compressive term, switched by a
    sensor, the absolute difference of the two adjacent wave strengths
    over the sum of their absolute values (5.8a), is added in the contact field.
    "It is easy to verify" that second order and TVNI are kept; no proof
    is printed. Remark 2 records an abandoned entropy-viscosity approach
    based on Liu's generalized Oleinik condition: "elegant and amenable to
    rigorous analysis", but slower and worse than (5.4)
    ([contact sharpening](/methods/contact-sharpening.md)).
14. **Named variants** (§7, eqs. 7.1–7.5, 7.13–7.15): ULT1 (the
    second-order scheme), ULT1C (ULT1 plus the contact compression),
    ULT2 (the simplified version), LW (Lax–Wendroff), ROE (first order,
    $\Theta = \vert\hat a\vert$ per field), a 2D hybrid of Lax–Wendroff and
    first order, and a 2D ULT1C; all use the Roe linearization.
15. **Cost** (§7, p. 393): "simple to program and requires not much more
    CPU time than a Lax–Wendroff scheme with some artificial viscosity".
    No timings are printed.

# Tests

All Euler, $\gamma = 1.4$, conserved state $(\rho, \rho v_x, E)$.

1. **Lax's shock tube** (§7.I, eq. 7.7, Figs. 2a–d). Left
   $(0.445, 0.311, 8.928)$, right $(0.5, 0, 1.4275)$ in conserved
   variables (primitive $\approx (0.445, 0.699, 3.528)$ and
   $(0.5, 0, 0.571)$, reader's conversion); 140 cells, 100 steps, CFL
   0.95; ROE, LW, ULT1 and ULT1C against the exact solution. The
   compression sharpens the contact without changing the other waves.
   All runs use $\Theta = \vert\hat a\vert$ and "nevertheless the solution
   has properly developed", which supports the claim that entropy
   violation needs a sonic point in an expansion
   ([Lax shock tube](/benchmarks/lax-shock-tube.md)).
2. **Sod's shock tube** (eq. 7.8a, Fig. 3). Left $(1, 0, 2.5)$, right
   $(0.125, 0, 0.25)$; ULT1C, 100 cells, 50 steps, CFL 0.95
   ([Sod shock tube](/benchmarks/sod-shock-tube.md)).
3. **Sod with a sonic rarefaction** (eq. 7.8b, no figure). Sod translated
   by velocity 0.5: left $(1, 0.5, 2.625)$, right
   $(0.125, 0.0625, 0.265625)$; ULT1 with the entropy fix at 0.1. Results
   "look almost identical to those of Fig. 3" up to the shift.
4. **Stationary shock** (eq. 7.9, Figs. 4a–c). States related by the
   Rankine–Hugoniot conditions in the $v - c$ field with zero speed; ULT2 with upstream $\rho = p = 1$. Upstream Mach 4 (pressure
   ratio 18.5) with entropy-fix parameter 0.1 and 0.25; Mach 10 (ratio
   116.5) with 0.1, "for robustness". Pressure profiles only
   ([stationary normal shock](/benchmarks/stationary-normal-shock.md)).
5. **Stationary expansion shock** (Fig. 5). The inverted, inadmissible
   Mach 4 discontinuity: ULT2 with parameter 0.1 breaks it up; with 0 it
   is "an entropy-violating stationary solution for ULT2". Figs. 4–5:
   100 cells, 50 steps, CFL 0.95. ULT1, ULT1C and ULT2 are "very much
   alike" on all Riemann problems.
6. **Quasi-1D nozzles** (§7.II, eqs. 7.10–7.11, Figs. 6–8, courtesy of
   H. C. Yee). A divergent nozzle with supersonic inlet and subsonic exit
   (ROE against ULT1 on a crude mesh, ULT1 on a finer mesh) and a
   convergent–divergent nozzle subsonic at both ends (ULT1); steady states
   against exact curves. Mesh sizes and some area parameters are not
   printed.
7. **Mach 3 step** (§7.III, eqs. 7.12–7.15, Fig. 9). Woodward and
   Colella's test: channel of width 1 and length 3, step of height 0.2 at
   0.6, Mach 3 inflow with $\rho = 1.4$, $p = 1$; $t = 4$ on a
   $10\times30$ grid ($h = 0.1$), Strang-type splitting, CFL 0.75, sharp
   corner with no rounding or extra viscosity, 30 density contours. The 2D
   hybrid against the 2D ULT1C: 1D high resolution "is also obtainable in
   two-dimensional calculations"
   ([forward-facing step](/benchmarks/forward-facing-step.md)).

# Notation map

| Harten (1983) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $v^n_j$ | $u^n_i$ | mesh function; index $j \to i$ |
| $\lambda = \Delta t/\Delta x$ | $\Delta t/h$, written out | **collision**: eigenvalues $\lambda^{(p)}$ |
| $\Delta x$ | $h$ | |
| $\Delta_{j+1/2}u$ | $\Delta^1 u_i$ | always with the superscript (the bare $\Delta u_i$ is the PPM jump) |
| $\mathrm{TV}(u)$ | $TV(u)$ | |
| TVNI | TVD | the paper's term |
| $L$ (scheme) | words ("the scheme") | **collision**: left-eigenvector matrix $L$ |
| $H(v_{j-k},\dots,v_{j+k})$ | words | **collision** with the Shu–Osher $\mathcal H$ |
| $C_{\pm,j+1/2}$ | words (incremental-form coefficients) | no registry symbol (proposal: $C^\pm_{i+1/2}$) |
| $\bar f_{j+1/2}$, $\bar f(v_j, v_{j+1})$ | $\hat f_{i+1/2}$ | |
| $a(u)$ | $f'(u)$ | |
| $\bar a_{j+1/2}$ | $\hat a_{i+1/2}$ | same definition (3.1b) |
| $\bar\nu_{j+1/2} = \lambda\bar a_{j+1/2}$ | $\hat a_{i+1/2}\Delta t/h$, written out | local signed Courant number; the registry $\nu$ is the global CFL number |
| $\mu$ | words (CFL bound) | **collision**: diffusion coefficient $\mu$ |
| $Q(x)$ | $\Theta_{i+1/2} = (h/\Delta t)\,Q(\hat a_{i+1/2}\Delta t/h)$ (scalar case) | |
| $\varepsilon$ (entropy fix) | $\varepsilon_{\mathrm H}$ on this page only | **collision**: WENO $\varepsilon$ |
| $\beta(u,\lambda)$; $\beta^k$ (§7) | words | **collision**: smoothness indicator $\beta_k$ |
| $g_i$, $\tilde g_{i+1/2}$, $\gamma_{i+1/2}$ | words (correction, antidiffusive flux, Courant shift) | **collisions**: boundary data $g(t)$, ratio of specific heats $\gamma$ |
| $G_{j+1/2}$ (3.17b) | three-argument $\operatorname{minmod}$ | |
| $R^k$, $L^k$, $a^k$ | $r^{(p)}$, $\ell^{(p)}$, $\lambda^{(p)}$ | field index $k \to (p)$ |
| $\alpha^k_{j+1/2}$ | $\ell^{(p)}\Delta^1 u_i$ | wave strength; **collision**: Lax–Friedrichs $\alpha$ |
| $\hat u$, $\hat H$, $\hat c$ (6.4) | $v_{\mathrm{Roe}}$, $H_{\mathrm{Roe}}$, $c_{\mathrm{Roe}}$ | $H$ total specific enthalpy (not registered) |
| $u$, $m = \rho u$ (§6) | $v_x$, $\rho v_x$ | the registry $\mathbf v$ in 1D |
| $\theta_i$, $\sigma(\nu)$ (5.7–5.8) | words | **collisions**: limiter $\theta$, flux-limiter constant $\sigma$ |
| $M_1$ | words (upstream Mach number) | the registry $M$ is the TVB constant |

# Pages created or updated

* Created [Godunov's order barrier for monotone linear schemes](/results/godunov-order-barrier.md) (Theorem 2.1 chain and the linear statement 2.8).
* Contributed to [Godunov's method](/methods/godunov-method.md) (the scheme's poor entropy enforcement in Harten's remark).
* Updated [Total variation diminishing](/properties/total-variation-diminishing.md) (batch-14 block: the primary definition, Theorem 2.1, Lemma 2.2, the modified-flux construction and its CFL condition, the systems extension).
* Updated [Monotone numerical flux](/definitions/monotone-flux.md) (batch-14 block: monotone schemes are TVD, $l_1$-contractive, first order and entropy-convergent).
* Updated [Order barriers and optimal coefficients of SSP time discretizations](/results/ssp-order-barriers.md) (batch-14 block: Lemma 2.2 is for explicit schemes only).
* Updated [Sod shock tube](/benchmarks/sod-shock-tube.md) (batch-14 block: the conserved data, ULT1C run and the sonic variant, eqs. 7.8a–b; added at the 2026-10-13 deep lint).
* Updated [Stationary normal shock test (one-dimensional carbuncle)](/benchmarks/stationary-normal-shock.md) (batch-14 block: the 1D stationary and expansion shocks, eq. 7.9; added at the 2026-10-13 deep lint).
* Updated [Mach 3 wind tunnel with a forward-facing step](/benchmarks/forward-facing-step.md) (batch-14 block: the $10\times30$ run, §7.III; added at the 2026-10-13 deep lint).
* Updated [Contact-discontinuity sharpening (subcell resolution, artificial compression, steepening)](/methods/contact-sharpening.md) (batch-14 block: artificial compression in the contact field, eqs. 5.7–5.8; added at the 2026-10-13 deep lint).

# Citations

1. `/home/stefano/papers/mosaic/high-order-capturing-schemes/1983-JCP-Harten-1010160021-99918390136-5.pdf`.
   * **Version read.** The publisher's scanned journal version (Academic
     Press, 37 PDF pages = pp. 357–393), not a preprint. Received 2
     February 1982, revised 23 June 1982.
   * **Identity.** doi:10.1016/0021-9991(83)90136-5, checked on Crossref:
     "High resolution schemes for hyperbolic conservation laws", Ami
     Harten, J. Comput. Phys. 49(3):357–393, March 1983, reference count
     19.
   * **How it was read.** Text layer for prose (its OCR is poor for
     formulas); every formula quoted checked on the rendered page images
     (pp. 360–381, 387, 392–393). Figures 2–9 are plots; no error norms
     or tabulated numbers are printed, so the resolution claims are
     qualitative.
   * **Recorded as printed.**
     - The proof of Theorem 2.1 reads "at least one local minimum and one
       local minimum" (one should be a maximum).
     - The proof of Lemma 3.4 cites "inequalities (2.10) of Lemma 2.1"
       (Lemma 2.2); Remark 3 cites the modified equation as "(2.6)"
       (2.7).
     - Remark 2 says the scheme "may degenerate locally to $O(\Delta^2)$
       truncation error"; in context this is the loss of the second-order
       flux error (3.6), i.e. a locally first-order scheme.
     - "Lax–Wendorff" (p. 364).
     - The nozzle source term (7.10a) is printed with the state and flux
       of (6.1) unchanged, without area factors; nozzle mesh sizes and the
       entrance and exit areas of (7.11) are not given numerically (they
       are in Yee's report).
     - The proof that the compression (5.7)–(5.8) keeps TVNI and second
       order is not printed.
   * **Reference list:** 19 entries, all merged. Report versions cited
     "in press" are merged into their published entries: ICASE 81-34 into
     `harten-1983-e` (J. Comput. Phys. 49:151), ICASE 82-5 (Harten, Lax &
     van Leer) into `harten-1983-d` (SIAM Rev. 25:35), and Los Alamos
     LA-9105 (Harten & Hyman) into `harten-1983-c` (J. Comput. Phys.
     50:235); the first and third checked on Crossref. Harten & Lax (SIAM
     J. Numer. Anal. 18:289) is `harten-1981`. The paper cites two Roe
     1981 works: the J. Comput. Phys. paper (43:357) is `roe-1981`, and the
     7th ICNMFD proceedings paper is `roe-1981-c`. Woodward & Colella's
     1981 proceedings paper is `woodward-1981`, not the 1984 J. Comput.
     Phys. article. Bibliography: 3104 entries.
