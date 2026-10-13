---
type: Source
title: "Harten, Lax & van Leer (1983) — On upstream differencing and Godunov-type schemes for hyperbolic conservation laws"
description: "Theory review: an entropy-augmented Lax–Wendroff theorem, upstream schemes in viscosity form, the existence of Roe-type linearizations for systems with an entropy, the Godunov-type framework built on approximate Riemann solutions consistent with the integral form, the one-intermediate-state (HLL) solver, and flux-vector splitting as Boltzmann-type schemes; no numerical tests."
resource: "doi:10.1137/1025002"
source_kind: paper
authors: [Harten A., Lax P.D., van Leer B.]
year: 1983
venue: "SIAM Rev. 25:35-61"
local_file: "/home/stefano/papers/mosaic/div-free-amr/1983-SIAMRev-Harten-1011371025002.pdf"
tags: [riemann-solver, godunov, shock-capturing, entropy-condition]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

A theory review of upstream (upwind) differencing for 1D hyperbolic systems
of conservation laws with a convex entropy. The introduction says
"numerical experimentation is not presented".
* §1 states a Lax–Wendroff-type theorem: a convergent conservative scheme
  that satisfies a discrete entropy inequality converges to an entropy weak
  solution.
* §2 defines **upstream schemes** through the viscosity form of the
  numerical flux, compares the van Leer, Huang, Roe and Osher choices of
  the viscosity term, and proves that a Roe-type linearization exists for
  any system with an entropy (Theorem 2.1, Harten–Lax).
* §3 defines **Godunov-type schemes**: averages of an approximate Riemann
  solution that must be consistent with the integral form of the
  conservation law and of the entropy inequality (Theorem 3.1). It builds
  the **one-intermediate-state solver** that the later literature calls
  HLL (eqs. 3.13–3.15b), and a two-intermediate-state solver separated by
  an entropy-weighted speed (eqs. 3.17–3.33).
* §4 reinterprets flux-vector splitting as Boltzmann-type schemes, proves
  linear $L_2$ stability, and shows that split-flux schemes cannot resolve
  stationary discontinuities exactly.

The paper has **no divergence-constraint content**: it is 1D, with
multi-D mentioned only for Theorem 1.1 and fractional steps. It is ingested
as the origin of the "Godunov-type" framework the bundle's CT pages
presuppose, and of the HLL flux that the
[UCT](/methods/upwind-constrained-transport.md) and positivity pages use.

# Key claims

Paper notation: $\lambda = \tau/\Delta$; $U$, $F$ are the entropy and
entropy flux (not the state).

1. **Weak solutions and entropy conditions** (§1, eqs. 1.2–1.6).
   Rankine–Hugoniot $f(u_R) - f(u_L) = S(u_R - u_L)$ (1.3); an entropy pair
   has $U$ convex and $U_uf_u = F_u$ (1.5a). Physical solutions are
   vanishing-viscosity limits and satisfy $U(u)_t + F(u)_x \le 0$ weakly
   (1.6a–c).
2. **Conservation form** (eqs. 1.7–1.8).
   $v_j^{n+1} = v_j^n - \lambda f_{j+1/2}^n + \lambda f_{j-1/2}^n$ with
   $f(u,u) = f(u)$ (1.7c); the discrete entropy inequality is
   $U_j^{n+1} \le U_j^n - \lambda F_{j+1/2}^n + \lambda F_{j-1/2}^n$
   (1.8a) with $F(u,u) = F(u)$ (1.8d).
3. **Theorem 1.1** (extension of Lax–Wendroff). A scheme consistent with
   the conservation law and the entropy condition that converges boundedly
   in $L^{\mathrm{loc}}_1$ (with $\tau/\Delta$ fixed) converges to a weak
   solution satisfying the entropy condition (1.6b). It also holds for
   $2l$-point fluxes and in any number of space variables; multi-D
   fractional steps inherit the entropy inequality if each 1D step
   satisfies (1.8a). Summing (1.8a) gives non-increasing total entropy
   (1.14), an a priori estimate too weak for pointwise bounds. The authors
   caution that density and pressure must stay positive (end of §1).
4. **Upwind scheme** (§2, eqs. 2.2–2.9). The CIR scheme is monotone under
   $\lambda|a| \le 1$ (2.2d); its viscosity vanishes at $a = 0$, which
   allows perfectly resolved stationary shocks and admits entropy-violating
   ones. Linear upstream flux $f(u,v) = A^+u + A^-v$ (2.8b),
   $A^\pm = \tfrac12(A \pm |A|)$ (2.9).
5. **Upstream scheme** (§2, p. 40; eqs. 2.10–2.12). It reduces to (2.8b) to
   linear order, and gives $f(u)$ ($f(v)$) when all signal speeds are
   positive (negative). In viscosity form
   $f(u,v) = \tfrac12(f(u) + f(v)) - \tfrac12 d(u,v)$ (2.11a). Perfect
   resolution of an admissible stationary shock needs $d = 0$ there;
   rejection of an inadmissible one needs $d \ne 0$ (2.12a–d).
6. **Catalogue of the viscosity term** (eqs. 2.13–2.23): $|A|$ at the
   midpoint state (2.14a) or van Leer's average of $|A|$ (2.14b), which
   slightly smears stationary shocks and excludes nonphysical ones;
   Huang's form (2.15); Roe's linearization
   $f(v) - f(u) = A(u,v)(v - u)$ with real eigenvalues, a complete
   eigenvector set and $A(u,u) = A(u)$ (2.16); Osher's path integral
   (2.21–2.23). Roe's scheme is attributed to Roe's 1980 conference paper
   [19]; the JCP paper [20] is listed but not cited in the text.
7. **Theorem 2.1 (Harten–Lax): a Roe-type linearization exists** for any
   system with an entropy function, as $A = BP$ with $B$ symmetric and $P$
   positive definite, in entropy variables (2.17–2.19); $A$ is similar to a
   symmetric matrix and is symmetric in its two arguments. With
   $d = |A(u,v)|(v - u)$ (2.20), every stationary discontinuity has $d = 0$,
   admissible or not, so Roe's scheme admits entropy-violating stationary
   discontinuities (p. 43); the fix is deferred to Harten & Hyman.
8. **Godunov's scheme** (§3A, eqs. 3.3–3.6). The cell average of the exact
   local Riemann solutions, giving
   $v_j^{n+1} = v_j^n - \lambda[f(\hat v_{j+1/2}) - f(\hat v_{j-1/2})]$ with
   $\hat v_{j+1/2} = u(0; v_j, v_{j+1})$. It satisfies (1.8a) by Jensen's
   inequality. Non-interaction of the Riemann problems needs
   $\lambda|a_{\max}| < \tfrac12$, but the conservation form stays
   consistent with the averaging for $\lambda|a_{\max}| \le 1$ (p. 45).
9. **Theorem 3.1 (Harten–Lax): Godunov-type schemes** (eqs. 3.7–3.10). An
   approximate Riemann solution $w(x/t; u_L, u_R)$ must satisfy
   (i) $\int_{-\Delta/2}^{\Delta/2} w\,dx = \tfrac{\Delta}{2}(u_L + u_R) - \tau f_R + \tau f_L$
   (3.7a) and (ii) the same with $U(w)$, $U$, $F$ and "$\le$" (3.7b), for
   $\Delta/2 > \tau\max|a_k|$. Then the averaged scheme (3.8) is
   conservative, consistent, and satisfies (1.8a) (proof in [7]). Its flux
   is $f_{LR} = f_L - \tau^{-1}\int_{-\Delta/2}^0 w\,dx + \tfrac{\Delta}{2\tau}u_L$
   (3.9b); the right-side form (3.9c) agrees exactly when (3.7a) holds.
   Every Godunov-type scheme is upstream, so a convergent one converges to
   an entropy weak solution. Glimm sampling may replace the averaging.
10. **Moving grids** (pp. 48–49). A Godunov-type scheme "can be used just
    as easily on a grid that varies in time, by adjusting the intervals of
    integration", "the natural choice for adaptive grids" (Harten–Hyman).
    This is the paper's only adaptivity statement and concerns 1D moving
    grids, not refinement interfaces.
11. **Roe as Godunov-type** (§3B, eqs. 3.11–3.12). Roe's solver is the exact
    solution of $w_t + A_{LR}w_x = 0$; its flux is
    $f_{LR} = \tfrac12(f_L + f_R) - \tfrac12|A_{LR}|(u_R - u_L)$ (3.12b).
    Osher's scheme is *not* Godunov-type: its state-space path does not
    correspond to a single-valued $w$ (p. 49).
12. **The one-intermediate-state solver** (§3B(i), eqs. 3.13–3.16). $a_L$,
    $a_R$ are "lower and upper bounds, respectively, for the smallest and
    largest signal velocity, calculated according to some algorithm"; no
    estimate is given. The solution is $u_L$ for $x/t < a_L$, $u_{LR}$ for
    $a_L < x/t < a_R$, $u_R$ for $a_R < x/t$ (3.13), and (3.7a) gives
    $$u_{LR} = \frac{a_Ru_R - a_Lu_L}{a_R - a_L} - \frac{f_R - f_L}{a_R - a_L} \quad (3.14).$$
    The flux is $f_L$ if $0 < a_L$, $f_R$ if $a_R < 0$, and otherwise
    $$f_{LR} = \frac{a_Rf_L - a_Lf_R + a_La_R(u_R - u_L)}{a_R - a_L} \quad (3.15a),$$
    with the single-formula form (3.15b).
    **What is proved (p. 50):** since $u_{LR}$ satisfies (3.7a), it equals
    the mean of the exact Riemann solution over $(\tau a_L, \tau a_R)$, so by
    Jensen's inequality the scheme satisfies the entropy inequality (3.7b);
    and if $u_L$, $u_R$ are joined by a single 1st- or $m$th-family shock and
    the speed algorithm returns that shock speed, (3.15) is exact. The
    mean-value argument needs $a_L$, $a_R$ to bound the true signal speeds.
    **Positivity is not claimed** for this solver; the only positivity
    statement in the paper is the §1 caution
    ([HLL Riemann solver](/methods/hll-solver.md)).
13. **Entropy-weighted middle speed** (eqs. 3.17–3.19, Lemma 3.2). $V$, a
    Rayleigh quotient in entropy variables, lies between the extreme
    eigenvalues of the Roe-type matrix and equals the shock speed whenever
    (1.3) holds.
14. **Two-intermediate-state solver** (§3B(ii), eqs. 3.20–3.33, Fig. 2;
    a Paul Woodward suggestion acknowledged). States separated by $dx/dt = V$,
    conservation on two triangles (3.23), flux (3.32a–b) with an
    entropy-enforcing artificial viscosity $\beta = C_1\beta_1 + C_2\beta_2$
    (3.31) that vanishes across a shock; single shocks and contacts are
    resolved exactly. It is nonlinear even for linear equations, hence not
    upstream in the §2 sense. Cheaper than Godunov or Roe for many
    components; accuracy "needs more experimentation".
15. **Generic entropy repair** (p. 54): a conservative flux that resolves
    discontinuities perfectly but admits entropy-violating ones can be
    corrected to $f(u,v) - C_1\beta(v - u)$.
16. **Flux-vector splitting as Boltzmann-type schemes** (§4,
    eqs. 4.1–4.27). Steger–Warming via homogeneity; non-homogeneous fluxes
    split through a reference-state Roe linearization; the linear moment
    choice (4.19) reproduces Steger–Warming exactly and, for Euler, the
    Sanders–Prendergast scheme. Linear stability through power-boundedness,
    with "no stability restriction of the time step" for (4.13); no
    nonlinear or entropy analysis (4(e)). Split-flux schemes cannot resolve
    stationary discontinuities exactly, since $f(u) = f(v)$ does not imply
    equality of the split parts (4.27).

**Relation to the bundle.** The bundle's "Godunov-type base scheme"
([constrained transport](/methods/constrained-transport.md),
[flux-CT](/methods/flux-ct.md)) uses the term in the looser modern sense of
any conservative upwind finite-volume scheme, including solvers (Osher)
that this paper's definition excludes. The Lax–Wendroff argument on the
[eight-wave](/methods/eight-wave.md) page is the conservative case of
Theorem 1.1: the eight-wave source term breaks the conservation form (1.7)
that the theorem requires. The HLLE intermediate-state positivity that
[Stone et al. (2008)](/sources/stone-2008.md) state, and the positivity
wave speeds of [Wu & Shu (2019)](/sources/wu-shu-2019.md), are not in this
paper.

# Tests

None: "numerical experimentation is not presented". Fig. 1 (linear Riemann
fan) and Fig. 2 (two-state wave pattern) are diagrams.

# Notation map

| Harten, Lax & van Leer | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u$, $u_L$, $u_R$ (state) | $U$ (conserved state) | |
| $U(u)$, $F(u)$ (entropy, entropy flux) | words | **collision:** registry $U$ is the conserved state |
| $f(u)$; $f(u,v)$, $f_{j+1/2}$, $f_{LR}$ | words (physical, numerical flux) | $f^{x,*}$ is registered for field components only |
| $a_k$, $a_i$ | $\lambda_k$ | characteristic speeds |
| $\lambda = \tau/\Delta$; $\Delta$, $\tau$ | $\Delta t/h$; $h$, $\Delta t$ | **collision:** $\lambda_k$ |
| $a_L$, $a_R$ | words (HLL signal-speed bounds) | no registry symbol |
| $u_{LR}$ | words (HLL intermediate state) | must not be starred: $^*$ marks provisional base-scheme values |
| $u_L^*$, $u_R^*$ | words | **collision:** starred provisional fields |
| $A$, $A_{LR}$, $\lvert A\rvert$, $A^\pm$ | words (flux Jacobian, Roe matrix) | **collision:** $A_h$ vector potential |
| $S$ | words (shock speed) | **collision:** $S(U)$ Powell source |
| $V$, $\beta$, $\gamma_L$, $\gamma_R$, $\delta_L$, $\delta_R$ | words | **collisions:** $\beta$ plasma beta, $\gamma$ adiabatic index |
| $w = U_u$ (entropy variables); $w(x/t)$ | words | **collision:** registry $w$ reconstructed scalar |
| $d(u,v)$ | words (numerical viscosity term) | |
| $P$, $P_i$ | words | **collision:** $P$ prolongation |
| $\mu$, $\phi$, $q$ (§4) | words | **collisions:** $\phi_h$, $q$ ghost-fill order |

# Pages created or updated

* Created [HLL Riemann solver](/methods/hll-solver.md): the one-intermediate-state solver, its consistency, what is proved, the wave-speed requirement.
* Created [Roe's approximate Riemann solver](/methods/roe-solver.md): Theorem 2.1, Roe as a Godunov-type solver, the stationary entropy defect.
* Updated [Upwind constrained transport (UCT)](/methods/upwind-constrained-transport.md): origin of the HLL flux, and what HLvL do and do not prove about it.

# Citations

1. `~/papers/mosaic/div-free-amr/1983-SIAMRev-Harten-1011371025002.pdf`.
   * **Version read.** The publisher's Version of Record, a SIAM scan
     (download stamp 29 December 2013), 27 pages. Received 29 March 1982;
     revised 5 May 1982. The work was done at ICASE, NASA Langley
     (footnote, p. 35).
   * **Identity.** doi:10.1137/1025002, checked on Crossref: SIAM Review
     vol. 25, issue 1, pp. 35–61, issued January 1983; authors Harten, Lax,
     van Leer.
   * **How it was read.** The OCR text layer garbles the equations; all
     equations quoted were read from page images at 110 dpi (pp. 36, 37,
     41, 42, 45, 47–54, 59–61), ref. [5] at 300 dpi. §4 eqs. 4.6–4.23 are
     summarized in words, not reproduced; only (4.19), (4.24)–(4.27) and the
     stability statement were checked visually. Theorem 3.1 and the entropy
     property of the two-state solver are proved in [7], not here.
   * **Recorded as printed.**
     * (3.15a) prints the middle-case condition "$a_L < 0 < u_R$", where
       $a_R$ is meant.
     * p. 54: "when $a_L \ge 0$, $f_{LR} = f_R$"; substituting into (3.32)
       gives $f_L$ (reader's reading: a misprint).
     * The left side of (3.9c) is printed $f'_{LR}$.
     * (3.15b) was checked algebraically against the middle case of
       (3.15a) by the reader.
   * **Reference list.** 23 entries, all merged. Harten's NYU report (March
     1982) → `harten-1983`; van Leer's "Towards the ultimate … III"
     (J. Comput. Phys. 23:263) is the new `vanleer-1977-b`, distinct from
     part IV (`vanleer-1977`); the Aachen 1982 talk → `vanleer-1982`
     (Crossref Lecture Notes in Physics 170:507). Bibliography key renamed
     `harten-lax-1983` → `harten-lax-vanleer-1983`. The bibliography holds
     3779 entries after this batch.
