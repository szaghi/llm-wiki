---
type: Source
title: "Harten et al. (1983) — On Upstream Differencing and Godunov-Type Schemes for Hyperbolic Conservation Laws"
description: "Review that writes upstream schemes for 1D conservation laws as the average of the physical fluxes minus half a dissipation term, extends the Lax–Wendroff theorem to the entropy inequality, defines Godunov-type schemes (conservative averages of approximate Riemann solutions consistent with the integral conservation law and entropy condition), introduces the one-intermediate-state HLL solver and a two-intermediate-state solver, and shows that flux-vector-split schemes cannot resolve stationary discontinuities exactly; no numerical experiments."
resource: "doi:10.1137/1025002"
source_kind: paper
authors: [Harten A., Lax P.D., van Leer B.]
year: 1983
venue: "SIAM Rev. 25:35–61"
local_file: "/home/stefano/papers/mosaic/astrophysical-simulation-codes/1983-SIAMRev-Harten-1011371025002.pdf"
tags: [riemann-solver, hydro]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

A review of upstream (upwind) difference schemes for 1D hyperbolic systems
of conservation laws; "numerical experimentation is not presented"
(Introduction, p. 35). §1 sets up weak solutions, entropy pairs and
entropy-consistent conservative schemes and extends the Lax–Wendroff
theorem to the entropy inequality (Thm. 1.1). §2 writes every three-point
conservative flux as the mean of the two physical fluxes minus half a
dissipation term, classifies the dissipation of van Leer, Huang, Roe and
Osher, and proves (Harten–Lax, Thm. 2.1) that every system with a convex
entropy has a Roe-type linearization. §3 defines **Godunov-type schemes**:
conservative cell averages of an approximate Riemann solution consistent
with the integral conservation law and the integral entropy inequality
(Thm. 3.1), and builds two such solvers, the one-intermediate-state solver
now called **HLL** (eqs. 3.13–3.15) and a two-intermediate-state solver
whose middle speed comes from the entropy variables (eqs. 3.17–3.33). §4
treats flux-vector splitting as a Boltzmann-type scheme and shows that
split-flux schemes cannot resolve stationary discontinuities exactly. See
[approximate Riemann solvers](/methods/approximate-riemann-solvers.md) and
[Godunov's method](/methods/godunov-method.md).

# Key claims

Equations are in the [registry](/notation.md) notation: $u$, $f(u)$,
$A(u)$ with eigenvalues $\lambda^{(p)}$, cell size $h$, time step
$\Delta t$, numerical flux $\hat f_{i+1/2}$ between the states
$u^-_{i+1/2}$ and $u^+_{i+1/2}$ (cell values at first order). Symbols the
registry lacks (entropy pair, signal-speed bounds, shock speed) are in
words (see the Notation map).

1. **Entropy condition** (§1, eqs. 1.3–1.6). Admissible weak solutions
   are vanishing-viscosity limits; with a convex entropy function and its
   entropy flux, they satisfy the entropy inequality (entropy
   non-increasing in this convention), and across a discontinuity the
   jump form (1.6d) alongside Rankine–Hugoniot (1.3).
2. **Entropy-consistent scheme and Theorem 1.1** (§1, eqs. 1.7–1.14). A
   conservative scheme $u_i^{n+1} = u_i^n - \frac{\Delta t}{h}(\hat f_{i+1/2} - \hat f_{i-1/2})$
   with $\hat f(u, u) = f(u)$ is consistent with the entropy condition if a
   numerical entropy flux makes the cell entropy satisfy a discrete
   inequality (1.8a). **Proved** (extending Lax–Wendroff): if such a scheme
   converges boundedly in $L^1_{\mathrm{loc}}$ at fixed $\Delta t/h$, the
   limit is a weak solution **and** satisfies the entropy inequality. It
   holds for wider stencils and in several space variables, and
   dimension-by-dimension fractional steps inherit it if each 1D step
   satisfies (1.8a). The total-entropy estimate is "not strong enough to
   prove the pointwise boundedness" or convergence. Schemes for
   compressible flow must keep density and pressure positive (end of §1,
   p. 38).
3. **Upwind scheme** (§2, eqs. 2.2–2.7). The Courant–Isaacson–Rees scheme
   is monotone under $\nu \le 1$; its modified equation has a viscosity
   that vanishes at zero wave speed, the source both of perfectly
   resolved stationary shocks and of admitted entropy-violating ones. For
   systems the condition is $\frac{\Delta t}{h}\max_p\vert\lambda^{(p)}\vert \le 1$
   (2.6c).
4. **Upstream form** (§2, eqs. 2.10–2.11). Every flux can be written
   $$\hat f_{i+1/2} = \tfrac12\left[f(u^-_{i+1/2}) + f(u^+_{i+1/2})\right] - \tfrac12\,(\text{dissipation term}),$$
   the dissipation term vanishing for equal states; the scheme is
   **upstream** if that term equals $\vert A\vert$ at the mean state times
   $u^+_{i+1/2} - u^-_{i+1/2}$ to leading order, and if the flux is the
   left (right) physical flux when all signal speeds are positive
   (negative).
5. **Stationary discontinuities** (§2, eqs. 2.12). Perfect resolution of
   an admissible stationary shock requires zero dissipation there; an
   inadmissible one requires non-zero dissipation. Two design options:
   switch the differencing direction (a slightly smeared shock), or meet
   both conditions and add an admissibility check.
6. **Catalogue of dissipations** (§2, eqs. 2.13–2.23). Van Leer's form
   smears stationary shocks but excludes non-physical ones; Huang's;
   **Roe's** $\vert A\vert$ of the Roe matrix (2.16, 2.20), which gives zero
   dissipation at any stationary discontinuity "whether or not the entropy
   condition ... is satisfied", so Roe's scheme "may admit nonphysical
   solutions" (fix cited to Harten & Hyman); Osher's path integral, with
   entropy-satisfying limits and at least one intermediate state in a
   stationary shock.
7. **Theorem 2.1 (Harten–Lax)** (§2, eqs. 2.17–2.19). **Proved:** a system
   with a convex entropy has a Roe-type linearization, built on the
   entropy variables.
8. **Godunov's scheme** (§3A, eqs. 3.1–3.6, pp. 44–47). Exact Riemann
   solutions are averaged over cells; in conservation form the flux is
   the physical flux of the exact Riemann solution's value on the
   interface. **Proved** to satisfy the discrete entropy inequality via
   Jensen's inequality (p. 45). Non-interaction of neighbouring Riemann
   problems needs $\nu < \tfrac12$, but the conservation form stays
   consistent with the averaged solution under $\nu \le 1$ (p. 45). The
   Godunov flux is continuous but only piecewise differentiable (p. 46);
   for linear systems the scheme is the upwind scheme (3.5–3.6, Fig. 1).
9. **Godunov-type schemes** (§3A, Thm. 3.1, eqs. 3.7–3.10). An
   approximate Riemann solution consistent with the integral conservation
   law (3.7a) and the integral entropy inequality (3.7b), for
   $\tfrac{h}{2} > \Delta t\max\vert\lambda^{(p)}\vert$, defines a
   conservative scheme that satisfies the discrete entropy inequality, so
   its convergent limits are entropy weak solutions (proof by reference
   to Harten & Lax). Its flux follows from either half of the cell
   (3.9b–c); every Godunov-type scheme has upstream property (ii).
   Godunov-type schemes extend to grids moving in time, "the natural
   choice for adaptive grids" (p. 49).
10. **Roe's solver is of Godunov type** (§3B, eqs. 3.11–3.12):
    $\hat f_{i+1/2} = \tfrac12[f(u^-_{i+1/2}) + f(u^+_{i+1/2})] - \tfrac12\vert A\vert(u^+_{i+1/2} - u^-_{i+1/2})$
    with $\vert A\vert$ of the Roe matrix. Osher's scheme is not, because
    its path does not correspond to a single-valued Riemann solution
    (p. 49).
11. **HLL, the one-intermediate-state solver** (§3B(i), eqs. 3.13–3.16).
    With a left and a right signal speed that are "lower and upper bounds,
    respectively, for the smallest and largest signal velocity, calculated
    according to some algorithm", the approximate solution is the left
    state, one intermediate state and the right state. The intermediate
    state (3.14) is (right bound × $u^+$ − left bound × $u^-$ −
    $(f(u^+) - f(u^-))$) over the bound difference. The flux (3.15a) is
    $f(u^-)$ if the left bound is positive, $f(u^+)$ if the right bound is
    negative, and otherwise (right bound × $f(u^-)$ − left bound ×
    $f(u^+)$ + left bound × right bound × $(u^+ - u^-)$) over the bound
    difference; (3.15b) combines the three cases with the positive and
    negative parts of the bounds. **Proved:** the intermediate state is
    the mean of the exact solution over the fan, so the solver satisfies
    the entropy inequality by Jensen (p. 50). If a bound equals the speed
    of a single shock of the first or last family, the solver is exact for
    it (3.16). The bound algorithm is left open; only the bounding
    property is required. **No positivity property is proved.**
12. **Two-intermediate-state solver** (§3B(ii), eqs. 3.17–3.33, Fig. 2).
    Requirements: conservation, exact single shocks and contacts of any
    family, the entropy law. A middle speed from the entropy-variable jump
    (3.17) separates two star states fixed by conservation (3.23).
    **Proved** (Lemma 3.2): the middle speed is well defined and bounded
    by the extreme eigenvalues, and equals the shock speed under
    Rankine–Hugoniot. A flux correction acts as an artificial viscosity
    that "is zero across a shock and is positive across an incipient
    rarefaction wave" (p. 54); that its constants can be chosen to give the
    entropy condition is **asserted** by analogy with Harten & Lax, not
    proved. The scheme is nonlinear even for linear equations, hence "not
    upstream" in the §2 sense; claimed cheaper than Godunov or Roe for many
    components, with "more experimentation" needed on accuracy (p. 54).
13. **Flux-vector splitting** (§4, eqs. 4.1–4.5). The flux is the
    positive split flux of the left state plus the negative split flux of
    the right. Steger–Warming's splitting departs from upstream form where
    an eigenvalue changes sign, giving a kink near sonic points, rectified
    by a smooth approximation of $\vert A\vert$ or by van Leer's smooth
    splitting.
14. **Boltzmann-type schemes** (§4, eqs. 4.6–4.27). Modelling each
    conservation law by a collisionless Boltzmann equation gives a
    conservative scheme; with a discrete distribution on the eigenvalues
    it **is** Steger–Warming (pp. 58–59), and the CFL condition is its
    three-point condition. Linear $L_2$ stability is shown for symmetric
    $A$; no nonlinear or entropy analysis. **Split-flux schemes cannot
    exactly resolve stationary discontinuities** (4.27): equal physical
    fluxes do not imply equal split dissipations; van Leer's split flux
    represents a stationary shock with at best one intermediate state, and
    "a contact discontinuity ... will keep on spreading with the use of
    any split flux scheme", from "the diffusive nature of the underlying
    Boltzmann model" (p. 60).

# Tests

None: "numerical experimentation is not presented" (Introduction, p. 35).
The only test-like statements are analytical: exact resolution of single
shocks (eqs. 3.16, 3.28) and the stationary-discontinuity analyses
(eqs. 2.12, 4.27).

# Notation map

| Paper | Registry | Note |
|---|---|---|
| $u$, $f(u)$, $m$ | $u$, $f(u)$, $m$ | |
| $A = f_u$, $a_k$ | $A(u)$, $\lambda^{(p)}$ | **collision**: bare $a$ is the registry scale factor |
| $R_k$ | in words | right eigenvectors; no registry symbol |
| $\Delta$ | $h$ | cell size |
| $\tau$ | $\Delta t$ | **collision**: registry $\tau$ is the Valencia energy or an optical depth |
| $\lambda = \tau/\Delta$ | $\Delta t/h$ | **collision**: registry $\lambda^{(p)}$ is an eigenvalue |
| $j$, $j + 1/2$ | $i$, $i + 1/2$ | |
| $v_j^n$ | $u_i^n$ | discrete solution |
| $f(u, v)$, $f_{j+1/2}$ | $\hat f_{i+1/2}$ | numerical flux |
| $u_L$, $u_R$ | $u^-_{i+1/2}$, $u^+_{i+1/2}$ | Riemann data |
| $d(u, v)$ | in words | dissipation term; **collision**: $d$ is the number of space dimensions |
| $U$, $F$, $w = U_u$ | in words | entropy function, entropy flux, entropy variables |
| $S$ | in words | shock speed; **collision** with $s(u)$ and Valencia $S_i$ |
| $a_L$, $a_R$ | in words | lower and upper signal-speed bounds |
| $u_{LR}$ | in words | HLL intermediate state |
| $V$, $u^*_L$, $u^*_R$ | in words | middle speed and star states of the two-state solver; **collision** risk with $\mathbf v$ and $P^*$ |
| $A^\pm$, $\vert A\vert$ | $\vert A\vert$, otherwise in words | functional calculus (2.7) |
| $P$, $B$ (Thm. 2.1) | in words | **collision**: $p$, $P^*$ |
| $\mu$, $\phi$, $q$ (§4) | in words | **collision**: $\mu$ mean molecular weight |
| $\beta$, $C_1$, $C_2$, $\gamma_{L,R}$, $\delta_{L,R}$ | in words | **collision**: $\gamma$, $\beta^i$, $\beta_{\mathrm p}$ |

# Pages created or updated

* Created this Source page.
* Contributed to the new [Godunov's method](/methods/godunov-method.md) (Godunov-type schemes, entropy proof, time-step conditions).
* Updated [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md)
  (batch-9 section: HLL as printed, its wave-speed requirement and
  entropy proof, the HLLE attribution, the GLF and gPLUTO forms, Roe's
  stationary-shock defect, the two-state solver, flux-vector splitting).

# Citations

1. Harten A., Lax P.D., van Leer B. (1983), "On upstream differencing and
   Godunov-type schemes for hyperbolic conservation laws", SIAM Rev.
   25(1):35–61, doi:10.1137/1025002. Local file:
   `/home/stefano/papers/mosaic/astrophysical-simulation-codes/1983-SIAMRev-Harten-1011371025002.pdf`.
   * **Version read.** The publisher's version of record, a SIAM scan
     (27 pp.; received 29 March 1982, revised 5 May 1982). Not a preprint.
     In this bundle the key `harten-1983` is this paper; Harten's
     single-author J. Comput. Phys. 49:357 paper is `harten-1983-b`.
   * **Identity.** Checked on Crossref: title, container SIAM Review,
     vol. 25, issue 1, pp. 35–61, issued 1983-01, authors Harten, Lax,
     Leer (Crossref family name for van Leer), 23 references.
   * **How it was read.** The text layer is an OCR of a scan with most
     equations garbled; every page was read visually (110 dpi; eqs.
     3.24–3.25 and ref. [5] at 250–300 dpi). Eqs. 3.30–3.33 were read at
     the level of Key claim 12 only.
   * **Recorded as printed.** (a) eq. 3.24 reads $f_S(u) = f_S(u_R)$
     (reader's reading: $u_L$ meant); (b) eq. 3.25 subtracts the shock
     speed times $V$ rather than times the entropy (reader's reading: a
     misprint); (c) eq. 3.9c prints the flux with a prime; (d) (3.12a) is
     referenced as "(3.12)". The entropy proof for the two-state solver's
     constants is deferred to Harten & Lax, §4.
   * **Reference list:** 23 printed entries (Crossref 23). Harten's NYU
     report (printed number "DOE/ER/03077-.67") is `harten-1983-b`
     (J. Comput. Phys. 49:357); the Los Alamos report LA-9105 is
     `harten-1983-c` (Crossref 50:235); Roe's 1980 ICNMFD paper is
     `roe-1981-b` (LNP 141), distinct from `roe-1981`; van Leer's Aachen
     talk on flux-vector splitting is `vanleer-1982` (Crossref LNP
     170:507). No DOIs printed. Bibliography: 2407 entries.
