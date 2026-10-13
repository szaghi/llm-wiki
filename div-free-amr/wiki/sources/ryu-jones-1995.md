---
type: Source
title: "Ryu & Jones (1995) — Numerical Magnetohydrodynamics in Astrophysics: Algorithm and Tests for One-Dimensional Flow"
description: "Second-order Harten-TVD code for 1D ideal MHD on the seven-wave system with the Brio–Wu renormalized eigenvectors, plus an exact nonlinear Riemann solver, tested on twelve shock tubes (the Ryu–Jones set); the normal field is a constant parameter and no divergence quantity exists."
resource: "doi:10.1086/175437"
source_kind: paper
authors: [Ryu D., Jones T.W.]
year: 1995
venue: "Astrophys. J. 442:228"
local_file: "/home/stefano/papers/mosaic/div-free-amr/1995-ApJ-Ryu-101086175437.pdf"
tags: [tvd, godunov, eigenvectors, riemann-solver, shock-tube, mhd, astrophysics]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper documents a second-order explicit Harten (1983) TVD
finite-difference code for plane-symmetric ideal MHD, built on the
Roe-type linearization of Brio & Wu (§2). The normal field $B_x$ is a
constant parameter, so the system has seven conserved variables and seven
waves. The paper prints the full right and left eigensystems in a
renormalized form. Explicit limiting values and a sign factor keep them
well defined and continuous at the degeneracies ($B_x = 0$ or
$B_y = B_z = 0$) (§2.2).

§3 describes an exact nonlinear MHD Riemann solver. It follows Dai &
Woodward but integrates fast and slow rarefactions exactly. Code and solver
are tested against each other on twelve shock tubes at 512 cells (§4,
Figs. 1–5). These are the **Ryu–Jones shock tubes**; Fig. 2a, a 3D-field
problem with rotational discontinuities, is the one reused most often in
the bundle ([rotated shock tube](/benchmarks/rotated-shock-tube.md)). §5
interprets compound structures at 8192 cells.

**The paper does nothing about $\nabla\cdot\mathbf B$ beyond stating the
constraint.** In 1D the constraint reduces to a constant $B_x$, which is
not a state variable. No projection, CT, source term or cleaning appears,
and no divergence quantity is measured. The bundle reads the paper for the
base scheme of the authors' later multidimensional codes
([Ryu, Jones & Frank (1995)](/sources/ryu-jones-frank-1995.md);
[Ryu et al. (1998)](/sources/ryu-1998.md)), for its eigensystem
normalization and for its shock-tube set.

# Key claims

1. **$\nabla\cdot\mathbf B$: none** (§2.1, after eq. 2.4). The constraint
   is stated, "∇ · B = 0 for the absence of magnetic monopole". The state
   is $q = (\rho, \rho v_x, \rho v_y, \rho v_z, B_y, B_z, E)^T$ (eq. 2.6);
   $B_x$ enters the flux (2.7), the speeds (2.17)–(2.19) and the
   eigenvectors only as a given constant. Units absorb $4\pi$.
2. **Seven eigenvalues, no divergence wave** (§2.2, eqs. 2.10–2.16):
   $v_x \mp c_f$, $v_x \mp c_a$, $v_x \mp c_s$, $v_x$, with
   $c_a = \sqrt{B_x^2/\rho}$ the normal Alfvén speed (eq. 2.17) and
   $a = \sqrt{\gamma p/\rho}$ (eq. 2.20). The system is hyperbolic, but
   "the eigenvalues may coincide in some limiting cases (BW)" (§2.1).
3. **Unnormalized eigenvectors fail at the degeneracies** (§2.2, eqs.
   2.21–2.26). "Near the point where either $B_x = 0$ or $B_y = B_z = 0$,
   the above set of the right eigenvectors is not well defined with
   columns becoming singular", through the factors $c_f^2 - c_a^2$ and
   $c_s^2 - c_a^2$ in the denominators.
4. **Renormalized eigensystem** (§2.2, eqs. 2.27–2.38, credited to Brio &
   Wu):
   $$\alpha_f = \frac{\sqrt{c_f^2 - c_a^2}}{\sqrt{c_f^2 - c_s^2}},\quad \alpha_s = \frac{\sqrt{c_f^2 - a^2}}{\sqrt{c_f^2 - c_s^2}},\quad \beta_y = \frac{B_y}{\sqrt{B_y^2 + B_z^2}},\quad \beta_z = \frac{B_z}{\sqrt{B_y^2 + B_z^2}}$$
   (eqs. 2.33–2.36), with the limits $\beta_y = \beta_z = 1/\sqrt2$ if
   $B_y = B_z = 0$ (eq. 2.37), and $\alpha_f = \alpha_s = 1$ if
   $B_y = B_z = 0$ and $B_x^2/\rho = a^2$ (eq. 2.38, the triple point).
   The Alfvén vectors are scaled by $\beta_y$, $\beta_z$ only, e.g.
   $R_{v_x\pm c_a} = (0, 0, \mp\beta_z\,\mathrm{sign}(B_x), \pm\beta_y\,\mathrm{sign}(B_x), \beta_z/\sqrt\rho, -\beta_y/\sqrt\rho, \mp(\beta_z v_y - \beta_y v_z)\,\mathrm{sign}(B_x))^T$
   (eq. 2.28). Left eigenvectors with $L_l\cdot R_m = \delta_{lm}$ are
   printed (eqs. 2.39–2.73), with normalizers
   $\theta_1 = \alpha_f^2 a^2\left(c_f^2 + \frac{2-\gamma}{\gamma-1}a^2\right) + \alpha_s^2 c_f^2\left(c_s^2 + \frac{2-\gamma}{\gamma-1}a^2\right)$ (eq. 2.71) and
   $\theta_2 = \alpha_f^2 c_f a\,\mathrm{sign}(B_x) + \alpha_s^2 c_s c_a\,\mathrm{sign}(B_x)$ (eq. 2.72).
5. **Continuity needs a sign factor** (§2.2, eq. 2.74). "With the above
   normalization, some columns are not continuous." The factor
   $\mathrm{sign}(B_T)$ is $+1$ if $B_y > 0$, or $B_y = 0$ and $B_z > 0$;
   $-1$ if $B_y < 0$, or $B_y = 0$ and $B_z < 0$. It multiplies the slow
   eigenvectors if $a^2 > c_a^2$ and the fast ones if $a^2 < c_a^2$.
6. **Limits** (§2.2, eqs. 2.75–2.79). As $B_y, B_z \to 0$ with
   $a^2 > c_a^2$, the fast eigenvectors become the hydrodynamic sound
   eigenvectors and the two shear eigenvectors are combinations of slow
   and Alfvén ones; for $a^2 < c_a^2$ slow and fast swap roles. For
   $B_z = v_z = 0$ the Alfvén eigenvectors become trivial unit vectors:
   flows with two-dimensional fields "do not produce structures associated
   with Alfvén modes like rotational discontinuities".
7. **Arithmetic interface average** (§2.3, eqs. 2.80–2.86). Following Brio
   & Wu, the interface state is the arithmetic mean of $\rho$, the
   velocities, $B_y$, $B_z$ and the total pressure $p^*$. At $\gamma = 2$
   "the above simple averaging would do just as well when compared to the
   full implementation of Roe's linearization technique" (asserted, no
   data).
8. **Harten TVD scheme** (§2.3, eqs. 2.87–2.95):
   $$\bar f_{i+1/2} = \tfrac12\left[F(q_i^n) + F(q_{i+1}^n)\right] - \frac{\Delta x}{2\Delta t^n}\sum_{k=1}^{7}\beta_{k,i+1/2}R^n_{k,i+1/2}$$
   (eq. 2.88), with
   $\beta_{k,i+1/2} = Q_k\!\left(\frac{\Delta t^n}{\Delta x}a^n_{k,i+1/2} + \gamma_{k,i+1/2}\right)\alpha_{k,i+1/2} - (g_{k,i} + g_{k,i+1})$ (2.89),
   wave strengths $\alpha_{k,i+1/2} = L^n_{k,i+1/2}\cdot(q^n_{i+1} - q^n_i)$
   (2.90), a minmod-type limiter $g_{k,i}$ (2.91)–(2.93) and the entropy
   fix $Q_k(\chi) = \chi^2/(4\varepsilon) + \varepsilon$ for
   $|\chi| < 2\varepsilon$, $|\chi|$ otherwise (2.94), with
   $\varepsilon = 0.1$ ($k = 1, 7$), $0.2$ ($k = 2, 6$), $0.1$
   ($k = 3, 5$), $0.0$ ($k = 4$) (2.95). Time step
   $\Delta t^n = C_{\rm cour}\Delta x/\max(|v^n_{x,i+1/2}| + c^n_{f,i+1/2})$,
   $C_{\rm cour}$ typically 0.8 (p. 14).
9. **Steepening** (§2.3, eqs. 2.96–2.98). For the Alfvén families
   ($k = 2, 6$) the limiter is augmented by a switched steepener; it
   resolves rotational discontinuities in 3–5 cells against 6–8 without.
   Steepening the contact is possible, but "the price ... is additional
   numerical oscillations".
10. **Exact nonlinear Riemann solver** (§3, eqs. 3.1–3.19). Eight states,
    seven structures; Lagrangian jump conditions, Dai–Woodward shock speeds
    with simpler coefficients, "more robust ... particularly in switch-on or
    switch-off shocks", rarefaction ODEs after Jeffrey (1966), an initial
    guess from the §2 eigensystem (eq. 3.19) and Newton–Raphson in four
    unknowns to $10^{-6}$. It agrees "exactly" with Dai & Woodward when
    only discontinuities occur.
11. **Compound structures** (§5, Figs. 6a–b, 8192 cells). The Brio–Wu slow
    compound structure is, numerically, a "2-4" intermediate shock
    (Alfvén Mach number $1.03 \to 0.910$, lab speed 0.284) followed by a
    slow rarefaction. A fast compound structure is a "1-3" intermediate
    shock (Alfvén Mach number $1.027 \to 0.989$, lab speed 0.935) preceded
    by a fast rarefaction. The exact solver, which allows rotational
    discontinuities, finds instead a rotational discontinuity plus a slow
    shock (resp. a fast rarefaction). The authors do not take sides on
    whether intermediate shocks are physical.

# Tests

All in §4: $\gamma = 5/3$, $x \in [0,1]$, 512 cells, Courant number 0.8,
rotational-discontinuity steepening on, contact steepening off. Code
(dots) against the exact solver (lines); only the captions survive in the
preprint (pp. 24–26). States are $(\rho, v_x, v_y, v_z, B_y, B_z, E)$,
$E$ the total energy.

| Fig. | Left state | Right state | $B_x$ | $t$ | Structures | Origin |
|---|---|---|---|---|---|---|
| 1a | $(1, 10, 0, 0, 5/\sqrt{4\pi}, 0, 20)$ | $(1, -10, 0, 0, 5/\sqrt{4\pi}, 0, 1)$ | $5/\sqrt{4\pi}$ | 0.08 | FS, SR, CD, SS, FS | DW table 7 |
| 1b | $(1, 0, 0, 0, 5/\sqrt{4\pi}, 0, 1)$ | $(0.1, 0, 0, 0, 2/\sqrt{4\pi}, 0, 10)$ | $3/\sqrt{4\pi}$ | 0.03 | FS, SS, CD, SR, FR | DW table 3a |
| 2a | $(1.08, 1.2, 0.01, 0.5, 3.6/\sqrt{4\pi}, 2/\sqrt{4\pi}, 0.95)$ | $(1, 0, 0, 0, 4/\sqrt{4\pi}, 2/\sqrt{4\pi}, 1)$ | $2/\sqrt{4\pi}$ | 0.2 | FS, RD, SS, CD, SS, RD, FS | DW table 1a |
| 2b | $(1, 0, 0, 0, 6/\sqrt{4\pi}, 0, 1)$ | $(0.1, 0, 2, 1, 1/\sqrt{4\pi}, 0, 10)$ | $3/\sqrt{4\pi}$ | 0.035 | FS, RD, SS, CD, SR, RD, FR | DW table 5a |
| 3a | $(0.1, 50, 0, 0, -1/\sqrt{4\pi}, -2/\sqrt{4\pi}, 0.4)$ | $(0.1, 0, 0, 0, 1/\sqrt{4\pi}, 2/\sqrt{4\pi}, 0.2)$ | 0 | 0.01 | magnetosonic shock, TD, magnetosonic shock | DW table 2a |
| 3b | $(1, -1, 0, 0, 1, 0, 1)$ | $(1, 1, 0, 0, 1, 0, 1)$ | 0 | 0.1 | two magnetosonic rarefactions | new |
| 4a | $(1, 0, 0, 0, 1, 0, 1)$ | $(0.2, 0, 0, 0, 0, 0, 0.1)$ | 1 | 0.15 | FR, SR, CD, SS, switch-on FS | new |
| 4b | $(0.4, -0.66991, 0.98263, 0, 0.0025293, 0, 0.52467)$ | $(1, 0, 0, 0, 1, 0, 1)$ | 1.3 | 0.15 | CD, switch-off FR | new |
| 4c | $(0.65, 0.667, -0.257, 0, 0.55, 0, 0.5)$ | $(1, 0.4, -0.94, 0, 0, 0, 0.75)$ | 0.75 | 0.15 | FS, switch-off SS, CD, hydro shock | new |
| 4d | $(1, 0, 0, 0, 0, 0, 1)$ | $(0.3, 0, 0, 1, 1, 0, 0.2)$ | 0.7 | 0.16 | hydro rarefaction, switch-on SR, CD, SS, RD, FR | new |
| 5a | $(1, 0, 0, 0, 1, 0, 1)$ | $(0.125, 0, 0, 0, -1, 0, 0.1)$ | 0.75 | 0.1 | FR, slow compound, CD, SS, FR | Brio–Wu at $\gamma = 5/3$ |
| 5b | $(1, 0, 0, 0, 1, 0, 1)$ | $(0.4, 0, 0, 0, -1, 0, 0.4)$ | 1.3 | 0.16 | fast compound, SS, CD, SS, FR | new |

FS/FR fast shock/rarefaction, SS/SR slow shock/rarefaction, RD rotational
discontinuity, CD contact, TD tangential discontinuity; DW = Dai &
Woodward.

Findings (§4 and abstract):
* Strong shocks are resolved in 2–4 cells, rotational discontinuities in
  3–5 with steepening, contacts in 6–8 without steepening, tangential
  discontinuities in more than 10.
* Agreement is "satisfactory, and mostly excellent" except at the compound
  structures (Figs. 5a–b).
* Switch-off fast rarefaction (4b): residual tangential field better than
  0.3% of the pre-rarefaction value; switch-off slow shock (4c): $B_\perp$
  turned off to about 0.04% (both from Tables 4b–4c, absent from the
  preprint). Fig. 4b shows "small, yet noticeable" spurious slow and
  hydrodynamic signals.
* **No divergence measurement in any test**; in 1D, with $B_x$ fixed, none
  is possible.

# Notation map

| Ryu & Jones | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\nabla\cdot B = 0$ (after eq. 2.4) | continuous constraint only | no discrete divergence exists in the paper; in 1D it is $B_x$ = const |
| $B_x$ | $B_n$ as on [rotated shock tube](/benchmarks/rotated-shock-tube.md) | fixed parameter, not a state variable |
| $B_y$, $B_z$, $B_\perp$ | transverse components of $B_h$ (words) | |
| $\psi = \tan^{-1}(B_z/B_y)$ (§3) | words: transverse-field angle | **collision** with $\psi_h$ (cleaning potential) |
| $E$ (total energy) | words | **collision** with $E_h$ (electric field) |
| $p^*$ (total pressure) | words | **collision** with the starred base-scheme values ($B_h^*$) |
| $\alpha_f$, $\alpha_s$, $\beta_y$, $\beta_z$ | words: Brio–Wu/Ryu–Jones normalization factors | **collision**: $\alpha$ is the rotation angle of the rotated shock tube; $\alpha^{\mathrm{LF}}$ |
| $\alpha_{k,i+1/2}$ (wave strength) | words | same collision; also an in-paper reuse of $\alpha$ |
| $g_{k,i}$, $\tilde g$, $\gamma_{k,i+1/2}$, $Q_k$, $\varepsilon$ | words: TVD internals | $g$ collides with gravity $\mathbf g$; $\gamma_k$ with the adiabatic $\gamma$ in the same paper |
| $h_f^\pm$, $h_s^\pm$ (eqs. 2.25–2.26) | words | **collision** with $h$ (grid spacing) |
| $R_k$, $L_k$ | words: right and left eigenvectors | **collision**: $R$ is restriction |
| $a$ (sound speed); $a_k$ (eigenvalue $k$) | words | in-paper double use of $a$ |
| $\Delta x$; $\Delta t^n$, superscript $n$ | $h$; $\Delta t$, $n$ | |

# Pages created or updated

* Updated [Eight-wave formulation](/methods/eight-wave.md): a second source for the seven-wave system without a divergence wave, the renormalization's explicit limits and the continuity sign factor.
* Updated [Rotated shock tube](/benchmarks/rotated-shock-tube.md): the Ryu–Jones shock-tube set, its 2a problem and the §5 reading of the compound wave.

# Citations

1. `~/papers/mosaic/div-free-amr/1995-ApJ-Ryu-101086175437.pdf`.
   * **Version read.** The arXiv preprint astro-ph/9404074v1 (29 April
     1994), "Submitted to the Astrophysical Journal", 26 pages. The date
     on page 1 is the arXiv re-typesetting date. The preprint carries no
     figures and no tables, only the figure captions (pp. 24–26); Tables
     4b, 4c, 5a, 5b cited in §4 are absent. The published ApJ text was not
     read, so differences between preprint and print are unknown.
   * **Identity.** doi:10.1086/175437, checked on Crossref: authors Ryu,
     Jones; Astrophys. J. 442, first page 228, issued March 1995 (Crossref
     gives no last page).
   * **How it was read.** Text extraction of all pages; pp. 6, 8, 9, 12, 13
     and 14 were rendered and read visually. Eqs. 2.33–2.38, 2.71–2.72,
     2.74 and 2.87–2.98 are reproduced from clean readings. Eqs.
     2.18–2.19, 2.21–2.26, 2.40–2.70 and 3.8–3.18 sit on a partly garbled
     text layer and are described, not reproduced.
   * **Recorded as printed.**
     * Crossref's title reads "magetohydrodynamics".
     * §4 text lists "a switch-on slow shock" for Fig. 4d; the caption
       and the test's introduction say switch-on slow rarefaction
       (reader's reading: the text is the slip).
     * The claim that simple averaging matches full Roe at $\gamma = 2$ is
       asserted without data.
   * **Reference list.** 16 entries, all merged. Only the books print
     titles; no DOIs are printed. Brio & Wu is printed with first page
     500 (75:500). Dai & Woodward "in press" (J. Comput. Phys.) was merged
     into `dai-woodward-1994` by context. Lind, Payne & Meier 1991 is a
     preprint. The bibliography holds 3711 entries after this batch.
