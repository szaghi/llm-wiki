---
type: Source
title: "Dai & Woodward (1994) — An Approximate Riemann Solver for Ideal Magnetohydrodynamics"
description: "Nonlinear seven-wave Riemann solver for 1D ideal MHD with the normal field a constant parameter: every wave treated as a jump-condition discontinuity (exact without rarefactions), closed-form shock speeds, a Newton iteration on four unknowns, and the finding that the Brio-Wu problem admits a solution without the compound wave."
resource: "doi:10.1006/jcph.1994.1069"
source_kind: paper
authors: [Dai W., Woodward P.R.]
year: 1994
venue: "J. Comput. Phys. 111:354-372"
local_file: "/home/stefano/papers/mosaic/div-free-amr/1994-JCP-Dai-101006jcph19941069.pdf"
tags: [riemann-solver, mhd, godunov, shock-capturing]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

An approximate nonlinear Riemann solver for 1D ideal MHD with all seven
waves, meant to supply time-averaged interface fluxes to a PPM-type
Godunov scheme under directional splitting (§§1–2). The equations are
written in a Lagrangian mass coordinate with the normal field a constant
parameter (eqs. 2.1–2.7). Every wave, rarefactions included, is treated
as a discontinuity obeying the jump conditions (eqs. 3.1–3.7): the solver
is exact when no rarefaction is present and is limited to weak
rarefactions. Closed-form fast and slow shock speeds follow from the
pre-shock state and one post-shock transverse-field value (eq. 9); a
Newton iteration on four unknowns enforces the contact conditions at the
middle of the fan (eqs. 11a–d). A linear characteristic solver and a
"single strong wave" guess are blended into the initial guess (§5). Six
Riemann problems are tabulated and one 200-zone 1D run is shown. The
physics finding: for the Brio–Wu data the three-component solution has
two slow shocks and a −180° rotational discontinuity in place of the
compound wave (§5, Table IV; §6).

**Bearing on divergence constraints: none beyond 1D.** The field
"satisfies the divergence-free condition" (p. 355), which in 1D is only a
constant normal field without an evolution equation (p. 356). There is no
multidimensional discussion, no treatment of a normal-field jump at a
face and no divergence control. The bundle takes from it the seven-wave
Riemann problem with the normal field as a parameter
([eight-wave formulation](/methods/eight-wave.md)).

# Key claims

1. **Wave structure** (§1, §3, Fig. 2). Seven waves, eight regions R1–R8:
   fast, rotational, slow, contact, slow, rotational, fast. "Two fast
   waves (either shock or rarefaction), two slow waves (either shock or
   rarefaction), two rotational discontinuities, and one contact
   discontinuity" (§1, abstract, §6).
2. **Three components are necessary** (§2, §6). With $u_z = 0$ and
   $B_z = 0$ imposed, Alfvén waves and rotational discontinuities do not
   occur in general; "The three component model is necessary for the MHD
   Riemann problem to display all the discontinuities" (§6). The
   two-component model is valid "only under very limited circumstances"
   (abstract).
3. **Lagrangian system** (§2, eqs. 2.1–2.7). Mass coordinate $dm = \rho\,dx$,
   specific volume, total pressure $P \equiv p + (B_y^2+B_z^2-B_x^2)/8\pi$
   and tension terms $-B_xB_{y,z}/4\pi$ (Gaussian units). $B_x$ "is a
   constant" (p. 356).
4. **Linear solver** (§3, pp. 357–358). A $7\times7$ system; Lagrangian
   fast, slow and Alfvén speeds; Riemann invariants for the entropy wave
   and, as inexact differentials, for the other families. It is "accurate
   only in the limit of weak discontinuities, but it can be used for the
   initial guess". Degenerate forms for vanishing transverse field and for
   vanishing $B_x$ are given (p. 358).
5. **Jump conditions; rarefactions as shocks** (§4, eqs. 3.1–3.7). In mass
   coordinate, equivalent to Landau–Lifshitz's Eulerian conditions.
   Rarefactions are approximated by "rarefaction shocks obeying the jump
   conditions", which "limits the applicability of this work to weak
   rarefactions" (p. 359).
6. **Degeneracies left to the programmer** (pp. 359–360). Where wave
   speeds coincide, Brio & Wu showed the solution depends on the ratio of
   neglected dissipation terms; "it must be the responsibility of the
   programmer to add appropriate physical and/or numerical dissipation
   terms". Intermediate shocks are out of scope.
7. **Shock classification** (§4, eqs. 4–7, Figs. 5–7). Across fast and
   slow shocks other than switch-on/off, $B_z/B_y$ is unchanged (eq. 4b):
   the transverse field keeps or reverses its plane. Only the rotational
   discontinuity, moving at the normal Alfvén speed, can rotate it
   (p. 368); it "cannot be formed by the steepening of a smooth
   disturbance" (p. 360). Largest jumps as the shock speed grows:
   $[B_y] = \frac{2}{\gamma-1}B_{y0}$ (7a), $[V] = -\frac{2}{\gamma+1}V_0$
   (7b).
8. **Shock speed from one post-shock value** (eq. 9, p. 363), with the
   $B_x = 0$ magnetosonic counterpart (eq. 10) and the equivalent pressure
   jump (eq. 8). The physical root of the cubic for the field jump at
   given speed (eq. 6) is chosen by the entropy condition (p. 362).
9. **Algorithm** (§5, pp. 363–365). Guess the transverse field in R2, R4,
   R7 and the common orientation angle of R3–R6 (contact conditions force
   one orientation there); fast shocks to R2, R7; rotation to R3, R6;
   slow shocks to R4, R5; Newton iteration on the continuity of the three
   velocity components and pressure across the contact (eqs. 11a–d).
   Jacobian entries by the chain rule through nested functions. For
   $B_x = 0$, PPM's hydrodynamic iteration on the common total pressure.
10. **Initial guess and relaxation** (pp. 365–366). Blend of the linear
    solver and a single-strong-wave guess, weighted by the largest
    normalized invariant jump, times one quarter, capped at one; "All the
    examples given below are solved using the initial guess from this
    averaging procedure." Under several strong discontinuities the Newton
    update is relaxed by $(1-f^N)$, $0<f<1$, $N$ the iteration count; this
    too can fail (Table VI). The fallback in simulations: "we simply give
    the average values of the left and right states for fluxes if the
    Riemann solver fails" (p. 371), and "the numerical computation
    recovers easily from such transients" (p. 370).
11. **Exactness** (p. 366). "For those MHD Riemann problems which involve
    no rarefaction waves, our Riemann solver is exact."
12. **The compound wave** (§5, p. 368; §6). For the Brio–Wu states the
    solver finds two fast rarefactions, two slow shocks (Mach 2.2 and
    1.05), a −180° rotational discontinuity and a contact (Table IV). The
    compound wave "disappears in our solutions … but it will be generated
    through the conservation law … no matter what approximation we use".
    Feeding the R2/R7 states back as a Riemann problem with only shocks
    and discontinuities, a 1D simulation still shows the compound wave:
    "Apparently, this Riemann problem does not have a unique solution"
    (p. 368).
13. **Cost** (§6, p. 372). "For most problems in MHD, we find that one
    iteration is enough to obtain sufficiently accurate fluxes in an
    actual code even for very strong MHD shocks"; unoptimized, 348,143
    one-iteration solves per second on a Cray C90. The nonlinear solver is
    suggested only where needed, the linear one elsewhere.
14. **Two-component variant** (p. 371). With $B_z = u_z = 0$ the
    rotations drop and three unknowns are iterated. In 2D, Alfvén waves
    appear only when propagation is aligned with the field.

# Tests

$\gamma = 5/3$ unless stated; states $(\rho, p, u_x, u_y, u_z, B_y, B_z)$,
Gaussian units.

| # | Table | Left | Right | $B_x$ | Outcome |
|---|---|---|---|---|---|
| 1 | Ia–Ib | (1.08, 0.95, 1.2, 0.01, 0.5, 3.6, 2.0) | (1.0, 1.0, 0, 0, 0, 4.0, 2.0) | 2 | fast shocks (Mach 1.22, 1.28), slow shocks (1.09, 1.07), rotations 12°, 9°, contact; 3 iterations |
| 2 | IIa–IIb | $(\rho,p,u_x,B_y,B_z)$ = (0.1, 0.4, 50, −1, −2) | (0.1, 0.2, 0, 1, 2) | 0 | two magnetosonic shocks, Mach 12.4 and 10.3; 6 iterations |
| 3 | IIIa–IIIb | $(\rho,p,B_y)$ = (1, 1, 5) | (0.1, 10, 2) | 3 | $B_z = u_z = 0$; fast and slow shocks left, fast and slow rarefactions right, contact; 4 iterations |
| 4 | IVa–IVb | $(\rho,p,B_y)$ = (1, 1, $\sqrt{4\pi}$) | (0.125, 0.1, $-\sqrt{4\pi}$) | 2.6587 | **Brio–Wu**, $\gamma = 2$, zero velocity and $B_z$; fast rarefactions, slow shocks (Mach 2.2, 1.05), −180° rotation (179.92°), contact; $B_z$ in R2–R7 of order $10^{-7}$–$10^{-9}$; 5 iterations |
| 5 | Va–Vb | (1.1, 5.6, 4, 0, 0, 5.0, −3.5) | (1, 1, 0, 0, 0, 4, 2) (text) | 5 | relaxation $f = 0.5$; fast shocks Mach 3.07, 5.133, slow shocks 1.09, 1.07, two rotations, contact; 5 iterations |
| 6 | VI, Fig. 8 | (1, 20, 10, 0, 0, 5, 0) | (1, 1, −10, 0, 0, 5, 0) | 5 | initial guess **fails**; Table VI is the solution "if an appropriate initial guess can be found". 1D run: 200 zones on $[0,1]$, jump at 0.5, $t = 0.08$, failed interfaces use averaged fluxes |

Figs. 6–7 plot jump-condition curves for one pre-shock state at
$B_x = 3$ and $B_x = 0$. No divergence quantity is measured.

**Relation to the Ryu–Jones tubes.** Converted from Gaussian units by
$1/\sqrt{4\pi}$, four of the five problems that
[Ryu & Jones (1995)](/sources/ryu-jones-1995.md) credit to Dai & Woodward
are in this paper: RJ 1a = Table VI (same states and $t = 0.08$), RJ 1b =
Table IIIa, RJ 2a = Table Ia, RJ 3a = Table IIa. RJ 2b, credited to "DW
table 5a", does not match Table Va (here $B_x = 5$; RJ 2b has $B_x = 3$).
Ryu & Jones cite Dai & Woodward "in press" and number the tables
differently (their "table 7" is Table VI here), so they quoted another
version (reader's reading) ([rotated shock tube](/benchmarks/rotated-shock-tube.md)).
*Compiler reading:* the seventh entry of the Ryu–Jones states, recorded
as total energy, equals the pressure of these tables in all four matches
(RJ 1a: 20 and 1 against Table VI's pressures 20 and 1). It cannot be the
total energy there, which would be at least the kinetic energy, 50. The
Ryu–Jones Source page records it as total energy.

# Notation map

| Dai & Woodward (1994) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $B_x$ (constant) | $B_n$ | |
| $B_y$, $B_z$ | words (transverse field) | |
| $\rho$, $p$, $u_x$, $u_y$, $u_z$ | words; components of $u_h$ | |
| $E$ (specific total energy) | words | **collision:** $E_h$ electric field |
| $\gamma$ | $\gamma$ | |
| $V$, $m$ | words | specific volume, mass coordinate; **collision:** $V_h^k$, $m(E)$ |
| $P$ (total pressure) | words | **collision:** $P$ prolongation |
| $\Lambda_y$, $\Lambda_z$ | words | magnetic tension terms |
| $C_a$, $C_f$, $C_s$, $C_0$, $C_x$, $C_t$, $C_{ms}$ | words | Lagrangian speeds (density times Eulerian speed); Eulerian $\lambda_k$ = normal velocity $\pm$ $C/\rho$; **collision risk:** $C_h$, $c_h$, $c_p$ |
| $W$ | words | Lagrangian shock speed |
| $\lambda \equiv 1+(B_z/B_y)^2$ | words | **collision:** $\lambda_k$ |
| $R_0$, $R_{f\pm}$, $R_{s\pm}$, $R_{a\pm}$ | words | Riemann invariants; **collision:** $R$ restriction |
| $\psi$ | words (transverse-field angle) | **collision:** $\psi_h$ |
| $A$, $A_0$, $A_1$, $A_2$, $S_0$, $S_1$, $S_2$ | words | **collision:** $A_h$, $S(U)$ |

# Pages created or updated

* Updated [Rotated shock tube](/benchmarks/rotated-shock-tube.md): which Ryu–Jones problems are in this paper; the Brio–Wu problem without a compound wave.
* Updated [Eight-wave formulation](/methods/eight-wave.md): a nonlinear seven-wave solver with the normal field a parameter.

# Citations

1. `~/papers/mosaic/div-free-amr/1994-JCP-Dai-101006jcph19941069.pdf`.
   * **Version read.** The publisher's journal version (Academic Press,
     19 pp.), a scan without a text layer. Received July 6, 1992; revised
     August 25, 1993.
   * **Identity.** doi:10.1006/jcph.1994.1069 (not printed on the scan),
     checked on Crossref: title and authors match; J. Comput. Phys.
     111(2):354–372, issued April 1994. Crossref deposits no reference
     list. This settles the venue conflict between citing sources recorded
     in the log.
   * **How it was read.** `pdftotext` returns nothing; all 19 pages were
     read visually at 110 dpi, dense formulas and the reference list at
     220 dpi. Figs. 6–8 were inspected qualitatively; no values were read
     off the plots.
   * **Recorded as printed.**
     * Eq. 6 coefficient $A_1$ and eq. 9 coefficients $S_1$, $S_2$ contain
       a speed $C_y$ that the paper never defines (only $C_0$, $C_x$,
       $C_t$); possibly $C_t$ or a typo. $S_2$'s brace placement is
       uncertain; these coefficients are not reproduced.
     * Table V: the text gives the right state $u_x = 0$, Table Va R8
       prints $u_x = -4.0$.
     * Fig. 8: the caption gives right pressure 2; the text and Table VI
       give 1.
     * Two-component step 3 (p. 371) sets "regions R3 and R5" equal to R2
       and R7; R6 is presumably meant (reader's reading).
     * The two-component case takes eqs. 6 and 9 with $\lambda = 0$, as
       printed; "swith-off" on p. 362; refs. 4 and 22 print "Collela";
       ref. 2 prints "B. Van Leer".
   * **Reference list.** 28 entries, all merged. Roe, printed J. Comput.
     Phys. 43:358, was merged into `roe-1981`. Correction made at this
     merge: [Tóth (2000)](/sources/toth-2000.md)'s ref. 10, which prints
     the title of Dai & Woodward's PPM paper with the venue of this one,
     was moved from `dai-woodward-1994` to `dai-woodward-1994-b`. The
     bibliography holds 3779 entries after this batch.
