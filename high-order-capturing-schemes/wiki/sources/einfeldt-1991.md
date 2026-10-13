---
type: Source
title: "Einfeldt et al. (1991) — On Godunov-Type Methods near Low Densities"
description: "Defines positively conservative schemes, proves that Godunov's method and the HLLE scheme are positively conservative by a convex-averaging argument, proves that no Godunov-type scheme built on a linearized Riemann solution is (symmetric double rarefaction, with and without shear), gives the HLLE wave speeds that bound the physical signal speeds and a sharper set with an algebraic positivity proof, and recasts Roe's scheme as HLLEM with Roe-eigenvalue speeds; first-order tests only."
resource: "doi:10.1016/0021-9991(91)90211-3"
source_kind: paper
authors: [Einfeldt B., Munz C.D., Roe P.L., Sjögreen B.]
year: 1991
venue: "J. Comput. Phys. 92:273–295"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/1991-JCP-Einfeldt-1010160021-99919190211-3.pdf"
tags: [positivity, riemann-solver, hll, hllem, low-density, euler]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

A conservative scheme is **positively conservative** if it always
produces physical states (positive density and internal energy) from
physical data (§1). Every scheme considered updates cell averages by a
convex average of the states of exact or approximate interface Riemann
solutions, and the admissible set is convex, so an approximate Riemann
solver gives a positively conservative scheme "if and only if all the
states generated are physically real". On that basis the paper proves
the property for Godunov's method (§2) and for the HLLE scheme with
wave speeds that bound the physical ones (§4), and proves that **no
Godunov-type scheme built on a linearized Riemann solution is positively
conservative**: there are symmetric double-rarefaction data, with
(Proposition 3.2) or without (Proposition 3.1) shear, whose exact
solution is physical and vacuum-free while every admissible linearization
yields a negative density or internal energy (§3). A sharper,
less dissipative speed choice keeps HLLE positive by a direct algebraic
argument (eq. 4.10, Appendix). Roe's scheme is HLLEM with Roe-eigenvalue
speeds; its low-density failure is an underestimate of the physical
signal speeds, and HLLEM with the bounding speeds is offered as a repair
that needs no entropy fix (§5). The tests are first order (§6): "all our
results are only first-order accurate as yet" (p. 290).

# Key claims

1. **Positively conservative** (§1, p. 274; §2, eq. 2.4). Density and
   internal energy "remain positive throughout the computational
   process". The admissible set is the states with $\rho > 0$ and
   $2\rho E - \rho^2\vert\mathbf v\vert^2 > 0$ (2.4), the registry's
   $\mathcal G$ for an ideal gas (eq. 1.3, $\gamma$ "a constant between 1
   and 2"). The setting is 2D Euler, stated to extend to 3D (§1).
2. **Convex-averaging principle** (§1, p. 274), quoted in the Summary.
3. **Godunov's method is positively conservative** (§2, eqs. 2.1–2.4). If
   the cell averages are in $\mathcal G$ and "no vacuum occurs in the
   exact solution to the Riemann problem at the cell interfaces", the
   update, an average of the exact interface solutions over two half
   cells, is in $\mathcal G$, because $\mathcal G$ is convex. The convexity
   is stated ("Note that G is a convex set"), not proved, and the
   time-step condition that keeps the fans in the half cells is not stated
   in the proof; the runs use $\Delta t\max_i(\vert v_{x,i}\vert + c_i)/h \le \tfrac12$
   (eq. 6.1).
4. **Proposition 3.1: every linearization fails in 1D** (§3, pp. 276–278).
   Data $(\rho, \mp\rho v_x, 0, E)$ with $\rho v_x > 0$ on the right (two
   rarefactions moving apart): (a) if
   $4\gamma\rho E/(3\gamma - 1) - (\rho v_x)^2 \le 0$, a vacuum occurs;
   (b) if that quantity is positive and $(\gamma - 1)\rho E - (\rho v_x)^2 \le 0$,
   the problem "has a solution with positive density and internal energy,
   but is not linearizable"; (c) if $(\gamma - 1)\rho E - (\rho v_x)^2 > 0$,
   it is linearizable. Proof: for the linear problem with the Jacobian at
   an average state, the symmetric wave strengths make both intermediate
   densities equal to $\rho$ minus $\rho v_x$ over the average-state sound
   speed (3.7); positive density needs that sound speed to be at least
   $v_x$ (3.8), positive pressure needs it to be at most
   $(\gamma - 1)E/(\rho v_x)$ (3.11), and the two are compatible only
   under (c) (3.12). *Scope (reader's reading of eqs.
   3.10–3.11, not stated by the paper):* "any linearization" means any
   Jacobian at a symmetric average state with zero mean velocity and the
   ideal-gas relation between enthalpy and sound speed, the average sound
   speed free. Compression data are always linearizable (p. 278). In Mach
   number (p. 278): vacuum for $\mathrm{Ma} \ge 2/(\gamma - 1)$, not
   linearizable for $\sqrt{2/(\gamma(3-\gamma))} \le \mathrm{Ma} < 2/(\gamma - 1)$;
   "For a gas with $\gamma = 1.4$ the dangerous zone … is reached already at
   $M = 0.94$." The cause in 1D is "the occurrence of two rarefaction
   waves".
5. **Proposition 3.2: shear** (§3, pp. 279–281, eqs. 3.13–3.18, Fig. 3.1).
   Data $(\rho, \mp\rho v_x, \mp\rho v_y, E)$: with the transverse kinetic
   energy removed from $E$, a vacuum, a non-linearizable but physical
   problem, or a linearizable one, by explicit inequalities. In the
   scaled momenta, linearizable iff a straight-line condition holds
   (3.18a), beside the quadratic data-positivity (3.18b) and no-vacuum
   (3.18c) conditions. "In most cases the failure of linearizations is
   caused by a shear flow" (p. 281). Roe's own average satisfies the
   condition for "the great majority of linearizable problems within the
   category displayed" (Remark, p. 281).
6. **HLLE** (§4, eqs. 4.1–4.4), credited to Harten, Lax & van Leer and
   Einfeldt (1988). Three states separated at $S_L$ and $S_R$; the star
   state is $u^{\mathrm{HLL}}_*$ (4.2); the flux is
   $$\hat f^{\mathrm{HLLE}}_{i+1/2} = \frac{S_R^+ f(u^-) - S_L^- f(u^+)}{S_R^+ - S_L^-} + \frac{S_R^+ S_L^-}{S_R^+ - S_L^-}\left(u^+ - u^-\right) \quad (4.4b).$$
7. **Bounding speeds and the positivity proof** (§4, eq. 4.5, p. 282).
   $S_L = \min(v_{n,\mathrm{Roe}} - c_{\mathrm{Roe}},\ v_n^- - c^-)$,
   $S_R = \max(v_{n,\mathrm{Roe}} + c_{\mathrm{Roe}},\ v_n^+ + c^+)$, with
   $u^\mp$ the first-order cell states. With these speeds the scheme "is
   positively conservative": they are "lower and upper bounds for the
   physical signal velocity", so the star state is the average of the
   exact Riemann solution over $[S_L\Delta t, S_R\Delta t]$ (4.6), in
   $\mathcal G$ by convexity "as long as no vacuum is present". The
   bounding property is asserted ("The proof is straight forward"), not
   proved; the time-step condition is as in claim 3.
8. **Lax–Friedrichs-type member** (eqs. 4.7–4.8). With $S_R$ the largest
   of $\vert v_n\vert + c$ at the Roe state and in the two cells, and
   $S_L = -S_R$, the HLLE flux becomes
   $\tfrac12\left(f(u^-) + f(u^+) - S_R(u^+ - u^-)\right)$, "a numerical
   flux function of Lax–Friedrich type", "very diffusive", giving
   "significantly less accurate results" than (4.4)–(4.5).
9. **Sharpest bound and sharper speeds** (eqs. 4.9–4.12; Appendix
   A1–A11). The scheme (4.4) is positively conservative if
   $(S_R - v_n^+)^2 \ge \frac{\gamma - 1}{2\gamma}(c^+)^2$ and
   $(v_n^- - S_L)^2 \ge \frac{\gamma - 1}{2\gamma}(c^-)^2$ (4.9), "the
   sharpest possible (in the one-dimensional case)" for speeds each
   depending on one side's state. Hence
   $S_L = \min\left(v_{n,\mathrm{Roe}} - c_{\mathrm{Roe}},\ v_n^- - \sqrt{(\gamma-1)/(2\gamma)}\,c^-\right)$
   and $S_R$ symmetrically (4.10), less dissipative at most rarefactions
   (4.11). For a single shock both (4.5) and (4.10) return the Roe
   eigenvalue, "the optimal numerical dissipation for a shock wave"
   (4.12). The proof (Appendix) is direct algebra on the star density and
   internal energy in the worst case of equal side velocities, not the
   convex-average argument of claim 7; (4.10) does not bound the physical
   speeds.
10. **Vinokur's observation** (eqs. 4.13–4.14). Near sonic points a Roe
    eigenvalue can lie outside the range of the two cells' eigenvalues;
    the speeds (4.5) or (4.10) then add dissipation, and "the failure
    (4.13) is not significant" since enlarging the speeds keeps HLLE
    stable; no loss of resolution was observed.
11. **Roe = HLLEM with Roe speeds; why Roe fails** (§5, eqs. 5.1–5.8).
    HLLEM ("proposed in [2]", Einfeldt 1988) adds a linear variation
    inside the fan along the contact and shear eigenvectors at the Roe
    state, centred on the mean speed $\tfrac12(S_L + S_R)$ (5.1–5.4); its
    flux is the HLLE flux minus $\frac{S_R^+S_L^-}{S_R^+ - S_L^-}$ times
    $\sum_{p\in\mathcal I}\delta_p\,\ell^{(p)}(u^+ - u^-)\,r^{(p)}$ (5.5b),
    with $\delta_p = c_{\mathrm{Roe}}/\left(c_{\mathrm{Roe}} + \tfrac12\vert S_L + S_R\vert\right)$
    for both intermediate families (5.6), chosen to "take out excess
    dissipation in the linear degenerate fields, subject to the restriction
    that the stability of the HLLE-schemes is to be preserved". With
    $S_{L,R}$ the Roe eigenvalues HLLEM "becomes equivalent to Roe's scheme"
    (5.7, credited to Einfeldt 1988). On the Proposition 3.1 data the
    intermediate wave strengths vanish, so HLLEM and HLLE differ only in
    the speeds, and with Roe speeds the star density can be negative in
    case (b) because those speeds lie inside the cell speeds (5.8). The
    paper's conclusion: Roe's signal speeds "underestimate the physical
    signal velocities"; the same holds for Proposition 3.2 "if we reset the
    anti-diffusion coefficient $\delta^3$ to zero".
12. **HLLEM in viscosity form, an assertion** (Remark, eqs. 5.9–5.10). The
    eigenvalues of $\Theta_{i+1/2}$ are
    $\frac{S_R^+ + S_L^-}{S_R^+ - S_L^-}\lambda^{(p)} - 2\frac{S_R^+S_L^-}{S_R^+ - S_L^-}$
    on the acoustic fields and the same with $(1 - \delta_p)$ on the second
    term for the intermediate ones ($\lambda^{(p)}$ at the Roe state). "In
    contrast to the original Roe-scheme this scheme does not require an
    artificial entropy fix and does not suffer under the instabilities
    described in Section 3." No positivity proof is given for HLLEM with
    $\delta_p \ne 0$; the shear test runs it with the shear weight set to
    zero (Tests).

# Tests

§6: grid spacing 0.01 (plots span $[-0.5, 0.5]$, about 100 cells),
$\Delta t\max_i(\vert v_{x,i}\vert + c_i)/h \le \tfrac12$ (6.1), first
order; $\gamma$ is not stated for the runs (the §3 remark uses 1.4).
States are printed as $(\rho, \rho v_x, \rho v_y, E)$.

1. **The 1–2–0–3 problem** (Fig. 3.1 point 1; Figs. 6.1–6.3). Right state
   $(1, 2, 0, 3)$; the left state is printed $(1, 2, 0, 3)$, a misprint for
   $(1, -2, 0, 3)$: the text calls the solution two rarefactions moving
   apart and places the data in case (b) of Proposition 3.1 (reader's
   check at $\gamma = 1.4$: $5.25 - 4 > 0$ and $1.2 - 4 \le 0$). In
   primitive variables (reader's arithmetic, $\gamma = 1.4$):
   $\rho = 1$, $v_x = \mp2$, $p = 0.4$. Roe's scheme "explodes after a few
   time-steps"; Roe with the Harten–Hyman entropy fix shows "unphysical
   oscillations" at $t = 0.05$ (Fig. 6.1); Roe with "the commonly used
   entropy fix in [7]" (Harten 1983) "also fails after a few time steps";
   HLLE with (4.5) "solves this problem without any difficulties" (Fig. 6.2,
   $t = 0.05$, 0.1); HLLEM with (4.5) speeds is "similar" (Fig. 6.3,
   $t = 0.1$).
2. **The 1–1–0–5 problem** (point 2; Fig. 6.4). $(1, \mp1, 0, 5)$, case (c):
   "All of our schemes solved this problem without real difficulty",
   though Roe's density shows "some not entirely smooth behaviour" at
   $t = 0.1$.
3. **The 1–1–2–5 problem** (point 3; Figs. 6.5–6.6). The same with
   transverse momentum 2, "two rarefaction waves moving in opposite
   directions, separated by a shear flow"; printed with equal transverse
   momenta on both sides, which would be no shear, so $\mp2$, as in
   Proposition 3.2, is the consistent reading (probable misprint). Reader's
   check at $\gamma = 1.4$: case (b), not linearizable but vacuum-free;
   $p = (\gamma - 1)(5 - \tfrac12\cdot 5) = 1.0$. Roe "explodes after a few
   time-steps", "caused by the presence of shear flow"; HLLE (Fig. 6.5) and
   HLLEM with the shear weight reset to zero (Fig. 6.6), both at $t = 0.1$:
   "Both schemes solved this test problem without breaking down, but the
   results from the unmodified scheme are better behaved." HLLEM with the
   shear anti-diffusion on is not reported.

# Notation map

| Einfeldt et al. (1991) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $w = (\rho, m, n, e)^T$; $v^n_i$ | $u$; $\bar u^n_i$ | **collision**: the paper's $u$ is the $x$-velocity |
| $m$, $n$ | $\rho v_x$, $\rho v_y$ | **collisions**: system size $m$, face normal $\mathbf n$ |
| $e$ (total energy per unit volume) | $E$ | |
| $\varepsilon$ (specific internal energy) | words | **collision**: WENO $\varepsilon$ |
| $u$, $v$ | $v_x$, $v_y$; $v_n$ at a face | |
| $H$, $\hat H$ | words (total specific enthalpy) | not registered |
| $\tau$, $\Delta x$ | $\Delta t$, $h$ | **collision**: WENO-Z $\tau$ |
| $\omega_{RP}$ | words (exact Riemann solution) | **collision**: weights $\omega_k$ |
| $G$ | $\mathcal G$ | same set |
| $b^l$, $b^r$; $b^-$, $b^+$ | $S_L$, $S_R$; $S_L^-$, $S_R^+$ | |
| $v_{i+1/2}$ (HLLE middle state) | $u^{\mathrm{HLL}}_*$ | not an interface trace |
| $a^k_{i+1/2}$; $\lambda^k(v_i)$ | $\lambda^{(p)}$ at the Roe state; $\lambda^{(p)}(u_i)$ | $a^1$, $a^4$ are $v_{n,\mathrm{Roe}} \mp c_{\mathrm{Roe}}$ |
| $R_k$, $\hat R^k$ | $r^{(p)}$ | $R_3$ (3.2b) is not printed |
| $\alpha_k$, $\hat\alpha^k$ | $\ell^{(p)}(u^+ - u^-)$ | **collision**: Lax–Friedrichs $\alpha$ |
| $\hat u$, $\hat c$, $\hat\rho$ | $v_{x,\mathrm{Roe}}$, $c_{\mathrm{Roe}}$, $\rho_{\mathrm{Roe}}$ | eq. 5.3a uses $\sqrt{\rho_i\rho_{i+1}}$ |
| $\delta^2$, $\delta^3$ | $\delta_p$, $p \in \mathcal I$ (contact, shear) | |
| $\bar u_{i+1/2} = (b^r + b^l)/2$ | $\tfrac12(S_L + S_R)$, written out | not the Roe velocity unless the speeds are Roe eigenvalues |
| $Q^k$ | eigenvalues of $\Theta_{i+1/2}$ | |
| $\beta$, $\beta^2 = (\gamma-1)/(2\gamma)$ | written out | **collision**: smoothness indicator $\beta_k$ |
| $a_l$, $a_r$ (Appendix) | $v_n^- - S_L$, $S_R - v_n^+$ | **collision** with the Roe speeds $a^k$ in the same paper |
| $M$ | $\mathrm{Ma}$ | **collision**: TVB constant $M$ |

# Pages created or updated

* Updated [HLL Riemann solver and wave-speed estimates](/methods/hll-riemann-solver.md) (batch-16 block: HLLE's positivity proved here, the printed speeds, what the "HLL/HLLEM class" attribution covers).
* Updated [HLLEM (HLLI) Riemann solver](/methods/hllem-riemann-solver.md) (batch-16 block: Einfeldt's HLLEM as printed, the weight's velocity, positivity asserted).
* Updated [Positivity preservation](/properties/positivity-preserving.md) (batch-16 block: positively conservative schemes, the Godunov and HLLE proofs and their conditions, the failure of linearized solvers).
* Updated [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md) (batch-16 block: the linearization failure, entropy fixes do not help, the formulas called Einfeldt's).
* Updated [Godunov's method](/methods/godunov-method.md) (batch-16 block: positively conservative under no vacuum).
* Updated [Double-rarefaction (near-vacuum) Riemann problems](/benchmarks/double-rarefaction.md) (batch-16 block: the 1–2–0–3 data and the sheared variant).

# Citations

1. `/home/stefano/papers/mosaic/high-order-capturing-schemes/1991-JCP-Einfeldt-1010160021-99919190211-3.pdf`.
   * **Version read.** The published journal version (Academic Press scan,
     23 pages, OCR layer), not a preprint. Received June 27, 1989; revised
     December 7, 1989.
   * **Identity.** doi:10.1016/0021-9991(91)90211-3, checked on Crossref:
     "On Godunov-type methods near low densities", Einfeldt, Munz, Roe,
     Sjögreen, J. Comput. Phys. 92(2):273–295, February 1991.
   * **How it was read.** The OCR is garbled in every display equation,
     so all equations were read from page renders (110 dpi, and 250 dpi
     crops for §§3–5, the Appendix and the figure captions). The figures
     are read qualitatively; no numerical values are printed for them.
   * **Recorded as printed** (reader's reading).
     - Test 1 left state printed with momentum $+2$ (for $-2$); tests 2–3
       left transverse momentum printed equal to the right one (probably
       for its negative).
     - Eigenvector $R_3$ (eq. 3.2b) is not printed; the labels jump from
       3.2a to 3.2c.
     - Eq. 4.7a omits "max" (braces only); the maximum is inferred from the
       context.
     - In-text cross-references misnumbered: "Proposition 2.1/1.2/1.1" for
       3.1/3.2 and "(2.13)" for (3.13), pp. 279, 281, 285, 287.
     - $\gamma$ and the domain of the §6 runs are not stated (the domain is
       read from the plot axes).
   * **Reference list:** 11 entries, all merged, all title-less except
     Smoller's book. The three Harten 1983 works resolve by vol:page to
     `harten-1983-c` (Harten & Hyman, printed "J. Comput. Phys. 235" without
     volume), `harten-1983-d` (Harten, Lax & van Leer) and `harten-1983`
     (Harten, J. Comput. Phys. 49:357). Roe is printed with volume 53
     (`roe-1981`, 43:357). Einfeldt's Proc. Roy. Soc. London paper,
     "submitted", without year, is `einfeldt-1989`. Godunov reads Mat. Sb.
     47:271 on the page image. Bibliography: 3184 entries.
