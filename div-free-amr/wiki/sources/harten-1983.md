---
type: Source
title: "Harten (1983) — High Resolution Schemes for Hyperbolic Conservation Laws"
description: "Second-order TVNI (later TVD) schemes built by applying a first-order TVNI scheme to a limited modified flux, with Harten's lemma, the characteristic extension to systems, the entropy fix for the numerical viscosity and a contact steepener: the base scheme of the Ryu–Jones MHD codes."
resource: "doi:10.1016/0021-9991(83)90136-5"
source_kind: paper
authors: [Harten A.]
year: 1983
venue: "J. Comput. Phys. 49:357-393"
local_file: "/home/stefano/papers/mosaic/div-free-amr/1983-JCP-Harten-1010160021-99918390136-5.pdf"
tags: [shock-capturing, tvd, godunov, riemann-solver, entropy-fix]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper builds explicit, 5-point, second-order schemes in conservation
form that are **TVNI**, total variation nonincreasing. TVNI is the paper's
name for what later papers call TVD; the paper never writes "TVD". A
3-point first-order TVNI scheme is applied to a **modified flux**: the
physical flux plus a limited, smoothed approximation of the first-order
scheme's own numerical-diffusion term. The result is second order and keeps
the TVNI property under the original CFL restriction (§§2–3). Systems are
treated by applying the scalar scheme to each characteristic field of a
local Roe-type linearization (§4). TVNI and convergence are proved only for
scalar and constant-coefficient problems. §5 adds an entropy fix, which
makes the numerical-viscosity function positive near zero speed, and a
contact steepener for linearly degenerate fields. §6 applies the scheme to
the Euler equations with the Roe average; §7 tests it on shock tubes,
stationary shocks, quasi-1D nozzles and a Strang-split 2D step.

The paper has **no divergence-constraint content** ($\nabla\cdot B$ or
incompressibility); it is pure gas dynamics. It is ingested because it is
the base scheme of the Ryu–Jones MHD code family
([Ryu & Jones (1995)](/sources/ryu-jones-1995.md),
[Ryu, Jones & Frank (1995)](/sources/ryu-jones-frank-1995.md),
[Ryu et al. (1998)](/sources/ryu-1998.md)) and of the second-order
upwind scheme of [Brio & Wu (1988)](/sources/brio-wu-1988.md).

# Key claims

Paper notation: $\lambda = \Delta t/\Delta x$, $\Delta_{j+1/2}v = v_{j+1} - v_j$.

1. **Convergence framework** (§1, p. 358). A conservation-form scheme
   converges to the entropy weak solution if (i) the total variation in $x$
   is uniformly bounded in $t$, $\Delta t$ and $\Delta x$; (ii) the scheme is
   consistent with the entropy inequality (1.3b) for all entropy functions;
   (iii) the entropy condition implies uniqueness. The argument is
   compactness plus Lax–Wendroff.
2. **TVNI definition** (§2, eqs. 2.4a–b, 2.5):
   $\mathrm{TV}(L\cdot v) \le \mathrm{TV}(v)$ with
   $\mathrm{TV}(u) = \sum_j |\Delta_{j+1/2}u|$
   ([total variation diminishing](/properties/total-variation-diminishing.md)).
3. **Hierarchy** (Theorem 2.1, p. 360). Monotone ⇒ TVNI (from the
   $l_1$-contraction of monotone schemes, eq. 2.6a); TVNI ⇒ monotonicity
   preserving. Monotone schemes are at most first order (eq. 2.7). A
   **linear** monotonicity-preserving scheme has nonnegative coefficients
   (eq. 2.8b, after Godunov), so linear TVNI schemes are first order
   (p. 361). Nonlinear second-order TVNI schemes are not excluded.
4. **Harten's lemma** (Lemma 2.2, p. 362). In incremental form (2.9b)
   $$(L\cdot v)_j = v_j + C_{+,j+1/2}\Delta_{j+1/2}v - C_{-,j-1/2}\Delta_{j-1/2}v ,$$
   the scheme is TVNI if $C_{-,j+1/2} \ge 0$, $C_{+,j+1/2} \ge 0$ (2.10a)
   and $C_{-,j+1/2} + C_{+,j+1/2} \le 1$ (2.10b). Proof: difference (2.9b)
   (eq. 2.11), take absolute values (2.12), re-index. Any 3-point
   conservative scheme with a differentiable flux can be put in this form
   by the mean value theorem (2.13).
5. **First-order 3-point scheme** (§3, eqs. 3.1–3.7).
   $$\bar f(v_j,v_{j+1}) = \tfrac12\left[f(v_j) + f(v_{j+1}) - \tfrac1\lambda Q(\lambda\bar a_{j+1/2})\Delta_{j+1/2}v\right],$$
   with $\bar a_{j+1/2} = [f(v_{j+1}) - f(v_j)]/\Delta_{j+1/2}v$ when
   $\Delta_{j+1/2}v \ne 0$ and $a(v_j)$ otherwise. Lemma 3.1: if
   $|x| \le Q(x) \le 1$ for $0 \le |x| \le \mu \le 1$ (3.2), the scheme is
   TVNI under $\lambda\max_j|\bar a^n_{j+1/2}| \le \mu$ (3.3), with
   $C_{\pm,j+1/2} = \tfrac12[Q(\bar\nu_{j+1/2}) \mp \bar\nu_{j+1/2}]$
   (3.5b), $\bar\nu = \lambda\bar a$. Lax–Wendroff is $Q(x) = x^2$ (3.6a).
   Under (3.2) the scheme is only first order (3.7).
6. **Modified-flux second-order scheme** (eqs. 3.8–3.12, Lemmas 3.2–3.4).
   $f^M_i = f(v_i) + (1/\lambda)g_i$,
   $\gamma_{i+1/2} = (g_{i+1} - g_i)/\Delta_{i+1/2}v$ (3.8b), and
   $$\bar f^M_{j+1/2} = \tfrac12[f(v_j) + f(v_{j+1})] + \tfrac{1}{2\lambda}\left[g_j + g_{j+1} - Q(\bar\nu_{j+1/2} + \gamma_{j+1/2})\Delta_{j+1/2}v\right] \quad (3.8d).$$
   The limiter (3.11a–c) is a minmod of neighbouring
   $\tilde g_{i+1/2} = \tfrac12[Q(\bar\nu_{i+1/2}) - (\bar\nu_{i+1/2})^2]\Delta_{i+1/2}v$:
   $g_i = s\min(|\tilde g_{i+1/2}|, |\tilde g_{i-1/2}|)$ when
   $\tilde g_{i+1/2}\tilde g_{i-1/2} \ge 0$, else 0.
   * Lemma 3.2 (p. 365): second order if $Q$ is Lipschitz and (3.9a–b) hold;
     Lemma 3.3 (p. 366): (3.11) satisfies (3.9), with
     $|\gamma_{j+1/2}| \le \tfrac12|Q(\bar\nu_{j+1/2}) - (\bar\nu_{j+1/2})^2|$ (3.12).
   * Lemma 3.4 (p. 367): the 5-point scheme is TVNI under **the same CFL
     restriction (3.3)** as the first-order scheme, since
     $|\bar\nu^M| \le 1 - \tfrac12(|\bar\nu| - 1)^2 \le 1$.
   * Remark 1: convergent in the scalar constant-coefficient case; the
     nonlinear case would need entropy consistency, not proved. Remark 2
     (p. 368): accuracy drops locally to first order at extrema and where
     $Q(\nu) = \nu^2$. Remark 4 gives a simplified flux (3.17a–c) that with
     $Q = x^2 + 1/4$ resembles Boris–Book FCT anti-diffusion.
7. **Systems** (§4, eqs. 4.6–4.16). Characteristic decomposition at an
   average state, wave strengths $\alpha^k_{j+1/2} = L^k_{j+1/2}\Delta_{j+1/2}v$
   (4.7b), and (4.8b)
   $$\bar f_{j+1/2} = \tfrac12[f(v_j) + f(v_{j+1})] + \tfrac{1}{2\lambda}\sum_{k=1}^m R^k_{j+1/2}\left[g^k_j + g^k_{j+1} - Q^k(\nu^k_{j+1/2} + \gamma^k_{j+1/2})\alpha^k_{j+1/2}\right].$$
   Lemma 4.1: second order. **Lemma 4.2: TVNI, for the total variation
   $\sum_j\sum_k|\alpha^k_{j+1/2}|$ (4.12), only for a constant Jacobian**,
   under $\lambda\max|a^k| \le \mu = \min_k\mu^k \le 1$ (4.13). Remark 3
   (p. 373): no TV estimate, and the paper "cannot prove convergence in the
   nonlinear system case". Roe's mean-value Jacobian (4.14–4.16) makes the
   one-equation case identical to the scalar scheme. Different $Q^k$, or
   different scalar schemes, may be used per field (Remark 1, p. 372).
8. **Entropy fix** (§5, eq. 5.4, Fig. 1). With $Q(x) = |x|$, the least
   dissipative choice (a generalized CIR/Roe upwind scheme, 5.3), a
   zero-speed entropy-violating discontinuity is a steady solution. The fix,
   for $0 < \varepsilon \le \tfrac12$:
   $$Q(x) = \frac{x^2}{4\varepsilon} + \varepsilon \ \ (|x| < 2\varepsilon), \qquad Q(x) = |x| \ \ (|x| \ge 2\varepsilon).$$
   Tried with $\varepsilon = 0.05, 0.1, 0.25$; adopted $\varepsilon = 0.1$ for
   genuinely nonlinear fields and $\varepsilon = 0$ for linearly degenerate
   ones (p. 375); the dependence on $\varepsilon$ is "rather slight". The
   modified-equation viscosity then vanishes only at Courant number 1,
   avoided by $\mu = 0.95$ ([Roe's solver](/methods/roe-solver.md)).
9. **Heuristic mechanism** (§5, eqs. 5.6a–d). The first-order scheme's
   numerical characteristic field is divergent, the correction is
   convergent, and the errors cancel to $O(\Delta^2)$; the paper credits
   this with both resolution and entropy enforcement.
10. **Contact steepening** (eqs. 5.7a–d, 5.8a–b). On linearly degenerate
    fields $g_i = \bar g_i + \theta_i\bar{\bar g}_i$, with
    $\theta_i = |\alpha_{i+1/2} - \alpha_{i-1/2}|/(|\alpha_{i+1/2}| + |\alpha_{i-1/2}|)$
    (5.8a) and $\sigma(\nu) = \tfrac12[1 - Q(\nu)]$ (5.8b). The scheme
    "retains its second-order accuracy and remains TVNI under the same CFL
    restriction" ("easy to verify"; no proof). This is the only steepener
    in the paper: there is **no rotational (Alfvén) steepener**, the paper
    being gas dynamics. Remark 1 (5.9) suggests a signed $\theta$ in
    genuinely nonlinear fields for 2D split runs, not implemented.
11. **Euler implementation** (§6, eqs. 6.1–6.4), $\gamma = 1.4$.
    Eigenvalues $u - c, u, u + c$; wave strengths (6.3b–d); the Roe average
    $\hat u = \langle\rho^{1/2}u\rangle/\langle\rho^{1/2}\rangle$,
    $\hat H = \langle\rho^{1/2}H\rangle/\langle\rho^{1/2}\rangle$,
    $\hat c = \{(\gamma - 1)(\hat H - \tfrac12\hat u^2)\}^{1/2}$ (6.4a). The
    paper calls it "rather expensive" and says the arithmetic average (6.4b)
    "will do just as well" in many applications; all §7 runs nevertheless
    use the Roe average (p. 381).
12. **Variants** (§7, eqs. 7.1–7.5). Common form
    $\bar f_{j+1/2} = \tfrac12[f_j + f_{j+1} - \tfrac1\lambda\sum_k\beta^k_{j+1/2}R^k_{j+1/2}]$:
    ULT1 $\beta^k = Q^k(\nu^k + \gamma^k)\alpha^k - (g^k_j + g^k_{j+1})$
    (7.2); ULT1C = ULT1 plus (5.7)–(5.8) on the linearly degenerate field;
    ULT2 $\beta = Q(\nu)\alpha - 2G$ (7.3); LW $\beta^k = (\nu^k)^2\alpha^k$
    (7.4); first-order ROE $\beta^k = |\nu^k|\alpha^k$ (7.5).
13. **Cost** (p. 393): "simple to program and requires not much more CPU
    time than a Lax–Wendroff scheme with some artificial viscosity"; no
    timings.

**Relation to the bundle.** The Ryu–Jones flux (their eqs. 2.88–2.89) is
ULT1, eqs. 7.1b + 7.2, and their entropy fix (2.94) is eq. 5.4 verbatim;
their per-family $\varepsilon$ values (0.1, 0.2, 0.1, 0.0) and those of Ryu,
Jones & Frank (0.3, 0.1, 0.45, 0.0) extend Harten's two values. The
Alfvén-family steepener of Ryu & Jones (their eqs. 2.96–2.98) is their own;
Harten has only the contact steepener. Brio & Wu's second order "by
Harten's approach" is the §4 characteristic extension.

# Tests

All Euler, $\gamma = 1.4$, conserved variables (density, momentum, energy).

1. **Lax shock tube** (§7.I, eq. 7.7, Figs. 2a–d). Left
   $(0.445, 0.311, 8.928)$, right $(0.5, 0, 1.4275)$. ROE, LW, ULT1 and
   ULT1C against the exact solution: 140 cells, 100 steps, CFL $\mu = 0.95$;
   **no output time stated**. The contact steepener improves the contact
   without changing the other waves; ULT1, ULT1C and ULT2 are "very much
   alike" apart from the contact (p. 387).
2. **Sod shock tube** (eq. 7.8a, Fig. 3, ULT1C). Left $(1, 0, 2.5)$, right
   $(0.125, 0, 0.25)$; 100 cells, 50 steps, $\mu = 0.95$; no output time
   stated. Figs. 2–3 use $Q^k = |x|$ (no entropy fix) and develop properly,
   which the paper reads as evidence that entropy violation needs a sonic
   point in an expansion.
3. **Sonic-rarefaction Sod** (eq. 7.8b, no figure): the same data shifted
   by velocity 0.5, left $(1, 0.5, 2.625)$, right
   $(0.125, 0.0625, 0.265625)$. ULT1 with (5.4), $\varepsilon = 0.1$: "almost
   identical" to Fig. 3 up to the shift.
4. **Stationary shock** (eq. 7.9, Fig. 4, ULT2). Zero-speed shock in the
   $u - c$ field, pre-shock density and pressure 1; Mach 4
   (pressure ratio 18.5) with $\varepsilon = 0.1$ and 0.25, and Mach 10
   (116.5) with $\varepsilon = 0.1$. 100 cells, 50 steps, $\mu = 0.95$;
   sharp shocks.
5. **Stationary expansion shock** (Fig. 5). The Mach-4 states inverted,
   ULT2 with $\varepsilon = 0.1$: the discontinuity breaks up. With
   $\varepsilon = 0$ it is a steady entropy-violating solution.
6. **Quasi-1D nozzles** (§7.II, eqs. 7.10–7.11, Figs. 6–8; courtesy of
   H. C. Yee). Steady states with the area source; divergent nozzle with
   supersonic inlet and subsonic exit (ROE and ULT1, crude and finer
   meshes), and a convergent–divergent nozzle subsonic at both ends (ULT1).
7. **2D Mach-3 step** (§7.III, Fig. 9). Woodward–Colella set-up, output at
   $t = 4$ on a $10\times30$ grid ($\Delta x = \Delta y = 0.1$), CFL 0.75,
   corner untreated. Strang splitting $L = L_xL_yL_yL_x$ over two steps
   (7.12a–b). A LW/first-order hybrid (7.13–7.14) against a ULT1C version
   with $Q = x^2 + \tfrac14$ (7.15). Claim: the 1D resolution "is also
   obtainable in two-dimensional calculations".

# Notation map

| Harten (1983) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u$, $v$ (state, scalar or vector); $w = (\rho, m, E)$ (§6) | $U$ (conserved state); scalar case $w_j$ | **collision:** registry $u_h$ is velocity; the paper's $u$ is also the gas velocity in §6 |
| $\lambda = \Delta t/\Delta x$ | $\Delta t/h$, written out | **collision:** registry $\lambda_k$ is a characteristic speed |
| $a^k$, $\bar a_{j+1/2}$ | $\lambda_k$ | characteristic speeds |
| $\nu^k = \lambda a^k$, $\mu$ | words (local Courant number, CFL bound) | |
| $R^k$, $L^k$ | words (right and left eigenvectors) | **collision:** $R$ restriction |
| $\alpha^k_{j+1/2}$ | words (wave strength) | mild clash with $\alpha^{\mathrm{LF}}$ |
| $Q(x)$ | words (numerical-viscosity function) | sans-serif $\mathsf Q$ is the SBP matrix |
| $g_i$, $\tilde g_{i+1/2}$, $\gamma_{j+1/2}$ | words (limited and unlimited corrections, correction speed) | **collision:** $\gamma$ is the adiabatic index, which the paper also writes $\gamma$ in §6 |
| $\beta^k_{j+1/2}$; $\beta(u,\lambda)$ (2.7b) | words | **collision:** $\beta$ is plasma beta |
| $\varepsilon$ | words (entropy-fix width) | distinct from $\epsilon_{\mathrm W}$ |
| $\theta_i$ | words (contact-steepening switch) | |
| $E$, $H$, $m$ | words (total energy, enthalpy, momentum) | **collisions:** $E_h$ EMF, $H$ coarse spacing, $m(E)$ SFC index |
| $\mathrm{TV}(\cdot)$ | words (total variation) | no registry symbol |
| $\bar f_{j+1/2}$ | words (numerical flux) | $f^{x,*}$ is registered for field components only |

# Pages created or updated

* Created [Total variation diminishing (TVD)](/properties/total-variation-diminishing.md): definition, hierarchy, Harten's lemma, the modified-flux construction and its proved scope.
* Created [Roe's approximate Riemann solver](/methods/roe-solver.md): the Euler Roe average as used in a TVD scheme, the arithmetic alternative, the entropy fix.
* Updated Source pages of [Ryu & Jones (1995)](/sources/ryu-jones-1995.md) and [Ryu, Jones & Frank (1995)](/sources/ryu-jones-frank-1995.md) (no rotational steepener in Harten).

# Citations

1. `~/papers/mosaic/div-free-amr/1983-JCP-Harten-1010160021-99918390136-5.pdf`.
   * **Version read.** The published journal version: a 37-page scan of
     the Academic Press article with an OCR text layer. Received 2 February
     1982; revised 23 June 1982.
   * **Identity.** doi:10.1016/0021-9991(83)90136-5, checked on Crossref:
     title and author match; J. Comput. Phys. vol. 49, issue 3,
     pp. 357–393, issued March 1983.
   * **How it was read.** The OCR text layer is usable for prose; every
     equation used here was checked on rendered pages (110 dpi; eq. 4.17 at
     250 dpi). Figures 2–9 are plots, read qualitatively; the paper reports
     no numerical error values.
   * **Recorded as printed.**
     * No output times are printed for the shock-tube runs (Figs. 2–5);
       only cell counts, step counts and CFL numbers.
     * (4.17b) prints all three arguments of the min as
       $\tilde g^k_{j+1/2}$; the scalar analogue (3.17b) has $j-1/2$,
       $j+1/2$, $j+3/2$. (4.17a) has an unbalanced parenthesis.
     * (3.11b) prints $(\bar\nu_{1+1/2})^2$ for $(\bar\nu_{i+1/2})^2$.
     * p. 360: "one local minimum and one local minimum"; p. 367 cites
       "Lemma 2.1" for Lemma 2.2; p. 371 cites "condition (4.3)" for (4.13).
     * Fig. 4 caption $P_2/P_1 = 1.165\times10^2$ against the text's 116.5
       (consistent). Ref. [18] prints "WOODWOARD".
   * **Reference list.** 19 entries, all merged. The "in press" reports
     were resolved to their journal versions: ICASE 81-34 →
     `harten-1983-b`; Los Alamos LA-9105 (Harten & Hyman) → `harten-1983-c`
     (Crossref J. Comput. Phys. 50:235); ICASE 82-5 →
     `harten-lax-vanleer-1983`. Roe's 1980 ICNMFD paper is `roe-1981-b`
     (Lecture Notes in Physics 141:354), distinct from `roe-1981`
     (J. Comput. Phys. 43:357). The bibliography holds 3779 entries after
     this batch.
