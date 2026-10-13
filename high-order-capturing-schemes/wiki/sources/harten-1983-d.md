---
type: Source
title: "Harten et al. (1983) — On upstream differencing and Godunov-type schemes for hyperbolic conservation laws"
description: "Review with original results on first-order three-point conservative schemes: the Lax–Wendroff theorem extended to a discrete entropy inequality, a definition of upstream schemes and a catalogue of their numerical-viscosity matrices, existence of a Roe-type linearization for every system with a convex entropy, the definition of Godunov-type schemes by two integral consistency conditions, the one-intermediate-state (HLL) solver with its entropy property, a two-intermediate-state solver, and flux-vector splitting as a Boltzmann-type scheme; no numerical experiments."
resource: "doi:10.1137/1025002"
source_kind: paper
authors: [Harten A., Lax P.D., van Leer B.]
year: 1983
venue: "SIAM Rev. 25:35–61"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/1983-SIAMRev-Harten-1011371025002.pdf"
tags: [riemann-solver, hll, godunov, entropy, numerical-flux, flux-splitting]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

A review that puts first-order, three-point, explicit conservative
upwind schemes in one framework, with original results. §1 extends the
Lax–Wendroff theorem: a convergent conservative scheme consistent with
a discrete entropy inequality has a limit that is a weak solution
satisfying the entropy inequality; convergence itself is assumed. §2
defines an *upstream* scheme, sorts the existing ones (van Leer, Huang,
Roe, Osher) by their numerical-viscosity matrix, gives the
stationary-shock criterion, and proves (Harten–Lax) that every system
with a convex entropy has a Roe-type linearization. §3 defines
**Godunov-type** schemes by two integral consistency conditions
(Theorem 3.1), shows that they are conservative and upstream, and
constructs the one-intermediate-state solver now called
[HLL](/methods/hll-riemann-solver.md) and a two-intermediate-state
solver with an entropy-variable middle speed. §4 recasts flux-vector
splitting as a collisionless Boltzmann-type scheme and shows that split
fluxes cannot resolve stationary discontinuities exactly. "Numerical
experimentation is not presented" (Introduction, p. 35).

# Key claims

1. **Entropy pairs and entropy conditions** (§1, eqs. 1.1–1.6). Physical
   solutions are vanishing-viscosity limits of
   $\partial_t u + \partial_x f(u) = \mu\,\partial_{xx}u$ (1.4). A convex
   entropy $U(u)$ with an entropy flux whose gradient is $\nabla_u U$
   times $A(u)$ (1.5a) gives the weak inequality
   $\partial_t U(u) + \partial_x(\text{entropy flux}) \le 0$ (1.6a–c), and
   across a discontinuity the shock speed times the jump of $U$ minus the
   jump of the entropy flux is nonnegative (1.6d).
2. **Discrete entropy consistency** (§1, eqs. 1.7–1.8). A conservative
   scheme with a consistent two-point flux,
   $\hat f(u, u) = f(u)$ (1.7c), is *consistent with the entropy
   condition* if a numerical entropy flux consistent with the entropy
   flux exists such that $U(\bar u^{n+1}_i)$ is at most $U(\bar u^n_i)$
   minus $\Delta t/h$ times the difference of the numerical entropy fluxes
   (1.8a).
3. **Theorem 1.1** (Lax–Wendroff extension, §1, p. 37). If such a scheme
   converges boundedly in $L^1_{\mathrm{loc}}$ as the mesh is refined at
   fixed $\Delta t/h$, the limit is a weak solution and satisfies the weak
   entropy inequality (1.6b). It holds for $2l$-point fluxes (1.10), "in
   any number of space variables", and for dimensional splitting when
   each 1D step satisfies (1.8a). **Convergence is assumed:** the
   total-entropy decrease that (1.8a) yields (1.14a,b) "is not strong
   enough to prove the pointwise boundedness of solutions of (1.7), nor
   the existence of convergent subsequences" (p. 38).
4. **Positivity is a caution only** (§1, p. 38): "we must make sure that
   the difference scheme we are using keeps the variables within their
   physical range, i.e., that density and pressure are always positive
   quantities." No scheme in the paper is proved positive.
5. **CIR scheme** (§2, eqs. 2.1–2.7). Upwind differencing of a linear
   equation is monotone under $\vert f'\vert\Delta t/h \le 1$ (2.2d); its
   modified equation has viscosity
   $\tfrac12 h\vert f'\vert(1 - \vert f'\vert\Delta t/h)$ (2.3), which
   vanishes at zero speed: it "will allow perfectly resolved stationary
   shocks but may also result in admitting entropy violating
   discontinuities". For systems,
   $\hat f_{i+1/2} = \tfrac12\left(f(u_i) + f(u_{i+1})\right) - \tfrac12\vert A\vert(u_{i+1} - u_i)$
   with $\vert A\vert = R\vert\Lambda\vert L$ (2.6b), under
   $\Delta t\max_p\vert\lambda^{(p)}\vert/h \le 1$ (2.6c).
6. **Upstream scheme** (§2, p. 40). A conservative scheme that (i) for
   nearby states linearizes to the CIR flux
   ($\Theta_{i+1/2} = \vert A\vert$ at the mean state up to
   $o(\vert u^+ - u^-\vert)$, 2.11c), and (ii) takes $f(u^-)$ when all
   signal speeds of the flux are positive and $f(u^+)$ when all are
   negative. "The relevant signal speeds generally differ from the
   characteristic speeds of the states."
7. **Stationary-shock criterion** (§2, eq. 2.12). A scheme resolves an
   admissible stationary shock perfectly iff its dissipation vanishes for
   equal-flux states whose entropy flux decreases across the jump
   (2.12b), and must not vanish when it increases (2.12d). The danger
   arises "only for stationary or near-stationary discontinuities". Two
   design options: nonlinear dissipation that slightly spreads the shock,
   or (2.12) plus an admissibility check.
8. **Catalogue of viscosity matrices** (§2, eqs. 2.13–2.23), all of the
   form $\Theta_{i+1/2}(u^+ - u^-)$ with $\Theta = \vert A(u)\vert$ for
   equal states: $\vert A\vert$ at the arithmetic mean (2.14a); the mean
   of $\vert A(u^-)\vert$ and $\vert A(u^+)\vert$ (2.14b, van Leer: it
   "somewhat smears stationary shocks but … excludes nonphysical
   discontinuities"); Huang's sign-matrix form (2.15); Roe's matrix, which maps
   $u^+ - u^-$ exactly to $f(u^+) - f(u^-)$ and has real eigenvalues, a
   complete eigenvector set and consistency (2.16), with
   $\Theta_{i+1/2}$ its absolute value (2.20); and Osher's path
   integral of $\vert A\vert$ along integral curves of the eigenvectors
   (2.21–2.23), whose limits satisfy the entropy condition, which resolves
   a stationary contact perfectly and needs at least one intermediate
   state for a stationary shock.
9. **Roe's scheme admits entropy violations** (§2, p. 43; §3B, p. 49). At
   a stationary discontinuity the jump $u^+ - u^-$ is a null vector of the
   Roe matrix, so the dissipation is zero "whether or not the entropy
   condition … is satisfied". The fix cited is Harten & Hyman's.
10. **Theorem 2.1 (Harten–Lax): a Roe-type linearization exists for
    every system with a convex entropy** (§2, pp. 42–43). In entropy
    variables $\nabla_u U$, the matrix is a product of a symmetric matrix
    (the flux Jacobian in entropy variables averaged along the straight
    path, 2.17–2.18) and a positive definite one (the averaged derivative
    of the state with respect to the entropy variables, 2.19); it is
    similar to a symmetric matrix, hence has real eigenvalues and a
    complete eigenvector set, and is symmetric in its two arguments. The
    multi-D analogue is cited to Harten.
11. **Godunov's scheme in conservation form** (§3A, eqs. 3.3–3.6). The
    update is the cell average of the exact solutions of the interface
    Riemann problems; the flux is the physical flux of the exact solution
    on the interface (3.4c,d). It satisfies the cell entropy inequality
    (1.8a), by the exact solution's entropy inequality and Jensen's
    inequality (p. 45). Non-interaction of neighbouring Riemann problems
    needs $\Delta t\max\vert\lambda\vert/h < \tfrac12$, but the
    conservative form "remains consistent" with the averaging up to
    $\le 1$ (p. 45). The Godunov flux is only piecewise differentiable
    (p. 46); for linear systems it is the CIR flux (3.6).
12. **Godunov-type schemes; Theorem 3.1** (§3A, eqs. 3.7–3.8; Harten–Lax,
    from their earlier paper's Thm. 2.1). An approximate Riemann solution
    must be consistent (i) with the **integral form of the conservation
    law**: its integral over the cell pair at time $\Delta t$ equals
    $\tfrac{h}{2}(u^- + u^+) - \Delta t\left(f(u^+) - f(u^-)\right)$
    (3.7a); and (ii) with the **integral form of the entropy condition**:
    the integral of $U$ of it is at most $\tfrac{h}{2}(U(u^-) + U(u^+))$
    minus $\Delta t$ times the jump of the entropy flux (3.7b); both for
    $h/2 > \Delta t\max\vert\lambda\vert$. Then the scheme that averages it
    over each half cell (3.8) is conservative, consistent and satisfies
    (1.8a); "For proof, see [7, after Thm. 2.1]" (not reproduced). With
    Theorem 1.1: "if such a scheme converges, the limit satisfies the
    conservation law and the entropy condition in the weak sense". (i)
    alone gives conservation form only. Averaging can be replaced by
    Glimm-type sampling.
13. **Flux of a Godunov-type scheme** (§3A, eqs. 3.9–3.10). The flux is
    $f(u^-)$ minus $1/\Delta t$ times the integral of the approximate
    solution over the left half cell plus $\tfrac{h}{2\Delta t}u^-$
    (3.9b), or symmetrically from the right (3.9c); the two agree iff
    (3.7a) holds. Every Godunov-type scheme satisfies upstream condition
    (ii), and the schemes adapt to moving grids.
14. **Roe and Osher in this frame** (§3B, eqs. 3.11–3.12, p. 49). Roe's
    flux is
    $\tfrac12\left(f(u^-) + f(u^+)\right) - \tfrac12\Theta_{i+1/2}(u^+ - u^-)$
    with $\Theta_{i+1/2}$ the absolute value of the Roe matrix (3.12b). Osher's scheme "is not of Godunov type in the sense of (3.9)":
    its path does not correspond to a single-valued approximate Riemann
    solution.
15. **The one-intermediate-state solver (HLL)** (§3B(i), eqs. 3.13–3.16).
    $S_L$ and $S_R$ are "lower and upper bounds, respectively, for the
    smallest and largest signal velocity, calculated according to some
    algorithm"; **no algorithm is given**. The solution is $u^-$, then a
    single state, then $u^+$, separated at $x/t = S_L$ and $S_R$ (3.13);
    (3.7a) gives
    $$u^{\mathrm{HLL}}_* = \frac{S_R u^+ - S_L u^- - \left(f(u^+) - f(u^-)\right)}{S_R - S_L} \quad (3.14)$$
    and the flux (3.15a) is $f(u^-)$ for $0 < S_L$, $f(u^+)$ for $S_R < 0$,
    and
    $$\hat f^{\mathrm{HLL}} = \frac{S_R f(u^-) - S_L f(u^+) + S_L S_R(u^+ - u^-)}{S_R - S_L}$$
    in between; a one-line form with speeds clipped at zero is printed as
    (3.15b). **Entropy:** the star state is the mean of the exact solution
    over $(S_L\Delta t, S_R\Delta t)$, so Jensen's inequality gives (3.7b)
    and the scheme is entropy-satisfying in the sense of Theorem 3.1,
    provided $S_L$, $S_R$ really bound the signal speeds (p. 50).
    **Isolated shocks:** if the data are joined by a single shock of the
    first (last) family and the algorithm returns its speed as $S_L$
    ($S_R$), the solver is exact (3.16).
16. **A two-intermediate-state solver** (§3B(ii), eqs. 3.17–3.33). Built
    for conservation, exactness on a single shock or contact of *any*
    family, and the entropy law; it "differs from" the solver of the
    authors' earlier paper "in some important details" (a suggestion from
    P. Woodward is acknowledged). The middle speed is the ratio of the
    jump of the entropy variables dotted with the flux jump to the same
    vector dotted with the state jump (3.17b); by Lemma 3.2 it is well
    defined, lies between the extreme eigenvalues of the Theorem 2.1
    matrix, and equals the shock speed whenever Rankine–Hugoniot holds
    (3.18). Two star states separated by this speed follow from
    conservation on two triangles with a numerical line flux (3.20–3.30),
    plus an artificial viscosity (3.31) that is zero across a shock and
    positive across an incipient rarefaction (3.33); its constants "can be
    so chosen" that (3.7b) holds, by an analysis referred to the earlier
    paper, and no values are given. The scheme is nonlinear even for
    linear equations, so "not upstream in the sense of our definition";
    "the decrease of entropy guarantees the $L_2$ stability"; cheaper than
    Godunov or Roe for many components, with "more experimentation …
    needed" on accuracy. It is **not** HLLC: a different middle-speed
    estimate, a different star-state closure and an added viscosity.
17. **General entropy correction** (p. 54). Any perfectly resolving
    conservative scheme that admits entropy-violating jumps can be
    corrected by subtracting such a viscosity times the jump from its flux.
18. **Flux-vector splitting** (§4, eqs. 4.1–4.5). $\hat f = f^+(u^-) + f^-(u^+)$
    reduces to CIR in the linear case iff $f^+ - f^-$ is $\vert A\vert u$.
    Steger–Warming uses the homogeneity of the Euler flux; it kinks at
    sonic points, cured by a smooth matrix function or van Leer's
    splitting.
19. **Boltzmann-type schemes** (§4, eqs. 4.6–4.26). Each conservation law
    is replaced by a collisionless Boltzmann equation whose first two
    moments are $u$ and $f(u)$; a three-point scheme under a CFL-type bound
    (4.22); a delta-function choice reproduces Steger–Warming; $L_2$
    stable for linear constant-coefficient symmetric systems; no nonlinear
    stability or entropy analysis.
20. **Split fluxes cannot resolve stationary discontinuities exactly**
    (§4(f), eq. 4.27). The Rankine–Hugoniot condition does not imply equal
    values of $f^+ - f^-$; van Leer's split flux, like Osher's, represents
    a stationary shock with "at best, one intermediate state", and "a
    contact discontinuity, however, will keep on spreading with the use of
    any split flux scheme".

# Tests

None: "The present paper concentrates on reviewing basic concepts and
deriving design principles; numerical experimentation is not presented"
(p. 35). Experiments on moving grids are deferred to Harten & Hyman.

# Notation map

| Harten, Lax & van Leer (1983) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u$, $f(u)$, $A = f_u$ | $u$, $f(u)$, $A(u)$ | |
| $a_k(u)$ | $\lambda^{(p)}$ | eigenvalues |
| $\lambda = \tau/\Delta$ | $\Delta t/h$, written out | **collision**: eigenvalues $\lambda^{(p)}$ |
| $\Delta$, $\tau$ | $h$, $\Delta t$ | **collision**: WENO-Z $\tau$ |
| $v^n_j$ | $\bar u^n_i$ | |
| $T$, $\Lambda$, $R_k$ | $R$, $\Lambda$, $r^{(p)}$ | the paper's $T$ is the registry's $R$ |
| $w$ (three meanings) | $\ell^{(p)}u$; $\nabla_u U$; words | characteristic variables, entropy variables, approximate Riemann solution |
| $u_L$, $u_R$; $f_L$, $f_R$ | $u^-$, $u^+$; $f(u^-)$, $f(u^+)$ | at $x_{i+1/2}$ |
| $f(u,v)$, $f_{j+1/2}$, $f_{LR}$ | $\hat f_{i+1/2}$ | |
| $U$, $F$; $F(u,v)$ | $U(u)$; words (entropy flux, numerical entropy flux) | no registry symbol for the entropy flux |
| $d(u,v)$, $\vert A\vert(u,v)$ | $\Theta_{i+1/2}(u^+ - u^-)$, $\Theta_{i+1/2}$ | same ½ convention |
| $A(u,v)$, $A_{LR}$ | words (the Roe matrix) | no registry symbol for the Roe matrix |
| $J_i$ | $\ell^{(p)}(u^+ - u^-)$ | wave strengths |
| $a_L$, $a_R$; $a^\pm$ | $S_L$, $S_R$; clipped speeds | $S_L^-$, $S_R^+$ cover two of the four clipped values in (3.15b) |
| $u_{LR}$ | $u^{\mathrm{HLL}}_*$ | |
| $u^*_L$, $u^*_R$, $V$ | words | not the HLLC $u^{\mathrm{HLLC}}_{*L}$, $u^{\mathrm{HLLC}}_{*R}$, $S_M$ |
| $S$ (shock speed) | words | **collision**: Rusanov $S$ |
| $\beta$, $C_1$, $C_2$; $\gamma_{L,R}$; $\delta_{L,R}$ | words | **collisions**: $\beta_k$, $\gamma$, $\delta_k$ |
| $\epsilon$ in (1.4) | $\mu$ | **collision**: WENO $\varepsilon$ |
| $\mu(q,u)$, $q$ (Boltzmann) | words | **collisions**: $\mu$, weight power $q$ |
| $f^\pm$ | $f^\pm$ | |

# Pages created or updated

* Updated [HLL Riemann solver and wave-speed estimates](/methods/hll-riemann-solver.md) (batch-16 block: the primary formulas, what Theorem 3.1 proves, no positivity result, no speed algorithm).
* Updated [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md) (batch-16 block: upstream schemes, the viscosity catalogue, Theorem 2.1, Roe's entropy mechanism, Osher, the two-state solver, flux-vector splitting).
* Updated [Godunov's method](/methods/godunov-method.md) (batch-16 block: the definition of Godunov-type schemes, Godunov's flux and entropy inequality, the two Courant bounds).
* Updated [Monotone numerical flux](/definitions/monotone-flux.md) (batch-16 block: the CIR viscosity and the stationary-shock criterion).
* Updated [Positivity preservation](/properties/positivity-preserving.md) (batch-16 block: the paper's caution, and that it proves no positivity).
* Updated [HLLC Riemann solver](/methods/hllc-riemann-solver.md) (batch-16 block: the 1983 two-state solver is not HLLC).
* Updated [Total variation diminishing (TVD) and bounded (TVB)](/properties/total-variation-diminishing.md) (batch-16 block: the Lax–Wendroff theorem with entropy, Theorem 1.1).

# Citations

1. `/home/stefano/papers/mosaic/high-order-capturing-schemes/1983-SIAMRev-Harten-1011371025002.pdf`.
   * **Version read.** The publisher's version of record (SIAM scan with
     an OCR layer, 27 PDF pages = pp. 35–61, downloaded 12/29/13 per the
     watermark), not a preprint. Received March 29, 1982; revised May 5,
     1982.
   * **Identity.** doi:10.1137/1025002 (not printed on page 1; from the
     archive filename), checked on Crossref: "On Upstream Differencing and
     Godunov-Type Schemes for Hyperbolic Conservation Laws", Harten, Lax,
     van Leer, SIAM Rev. 25(1):35–61, January 1983, reference count 23.
   * **How it was read.** Text layer for prose; the OCR is unusable for
     equations, so every formula was read on page images (pp. 37–39,
     41–42, 44–45, 47–54, 59–61).
   * **Recorded as printed** (reader's reading).
     - (2.2c) prints the coefficient $\lambda(1 - \vert a\vert)$ where the
       consistent one is $1 - \lambda\vert a\vert$ (cf. 2.2d–2.3).
     - (3.15a) prints the middle-branch condition "$a_L < 0 < u_R$" (for
       $a_R$).
     - (3.9c) prints the flux with a prime.
     - p. 54 prints "when $a_L \ge 0$, $f_{LR} = f_R$"; (3.32a,b) give
       $f(u^-)$.
     - Proofs referred elsewhere: the assertion after Theorem 3.1, the
       constants of the two-state viscosity, existence of Osher's path.
   * **Reference list:** 23 entries, all merged. Roe's 7th ICNMFD paper is
     `roe-1981-c` (title supplied by this list) and Roe's J. Comput. Phys.
     paper `roe-1981`; Osher's Mathematics Studies 47 paper is
     `osher-1981-b` (not Osher & Solomon); Harten's NYU report
     DOE/ER/03077-167 is noted on `harten-1983`; Harten & Hyman's Los
     Alamos report LA9105 is `harten-1981-c`; the printed author "Rietz"
     is kept (`rietz-1981`). The bibliography title of this paper was
     corrected to "Godunov-type", hyphenated as printed. Bibliography:
     3184 entries.
