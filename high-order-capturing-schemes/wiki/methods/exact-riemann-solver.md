---
type: Method
title: "Exact Riemann solver for the Euler equations"
description: "The exact solution of the 1D ideal-gas Euler Riemann problem: one monotone pressure equation for the star pressure, solved by Newton–Raphson from an approximate-solver guess, explicit shock and rarefaction relations for the rest of the star region, sampling of the self-similar solution, and closed-form vacuum cases; the flux of Godunov's first-order method and the reference solution of shock-tube tests."
status: established
aliases: [exact Riemann solver, Godunov's exact solver, exact Godunov flux, pressure function, star region, Toro's tests]
tags: [riemann-solver, godunov, euler, riemann-problem, numerical-flux]
timestamp: 2026-10-13T00:00:00Z
---

# Exact Riemann solver for the Euler equations

The data are two constant primitive states $\mathbf W^-$ (left) and
$\mathbf W^+$ (right) of the $x$-split Euler equations for an ideal gas.
The solution is self-similar in $x/t$: a left wave (shock or
rarefaction), a contact and a right wave. Between the two nonlinear waves
lies the star region, with one pressure $p_*$ and one normal velocity
$v_{n*}$, and two densities $\rho_{*L}$, $\rho_{*R}$ that jump at the
contact. Tangential velocity components behave as passive scalars and
jump only at the contact ([Toro (1997)](/sources/toro-1997.md), §§9.2.1,
12.3.4). Toro's Ch. 4 is the complete statement in this bundle (§§4.2–4.6).

**Pressure equation** (§4.2, Prop. 4.2.1, eqs. 4.5–4.9). $p_*$ is the
root of
$$f^{\mathrm p}(p) \equiv f^{\mathrm p}_L(p) + f^{\mathrm p}_R(p) + (v_n^+ - v_n^-) = 0,$$
$$f^{\mathrm p}_L(p) = \begin{cases} (p - p^-)\,g^{\mathrm{TS}}_L(p), & p > p^- \ \text{(shock)},\\ \dfrac{2c^-}{\gamma-1}\left[\left(\dfrac{p}{p^-}\right)^{\frac{\gamma-1}{2\gamma}} - 1\right], & p \le p^- \ \text{(rarefaction)},\end{cases} \qquad g^{\mathrm{TS}}_L(p) = \left[\frac{2/\left((\gamma+1)\rho^-\right)}{p + \frac{\gamma-1}{\gamma+1}\,p^-}\right]^{1/2},$$
with $f^{\mathrm p}_R$ and $g^{\mathrm{TS}}_R$ the same expressions in the
$+$ data. The velocity follows without iteration,
$v_{n*} = \tfrac12(v_n^- + v_n^+) + \tfrac12\left[f^{\mathrm p}_R(p_*) - f^{\mathrm p}_L(p_*)\right]$.
The function $f^{\mathrm p}$ is monotone and concave down (eqs.
4.37–4.38), so a positive root is unique when it exists. Which branch
each side takes at $p_*$ decides the wave pattern: shock–shock,
shock–rarefaction, rarefaction–shock or rarefaction–rarefaction.

**Vacuum** (§4.3.1, eq. 4.40; §4.6). A positive root exists iff
$f^{\mathrm p}(0) < 0$, that is
$$\frac{2c^-}{\gamma-1} + \frac{2c^+}{\gamma-1} > v_n^+ - v_n^-.$$
Otherwise "vacuum is created by the non-linear waves" and the solution is
two rarefactions separated by vacuum, in closed form (eqs. 4.81–4.82).
When one data state is itself vacuum, a shock cannot be adjacent to it
(Prop. 4.6.1); for vacuum on the right the front moves at
$v_n^- + 2c^-/(\gamma-1)$ (eq. 4.76). An approximate solver's
vacuum-generation condition "will in general be different" from the
exact one (p. 143; [positivity preservation](/properties/positivity-preserving.md)).

**Newton–Raphson and the initial guess** (§4.3.2, eqs. 4.44–4.49,
Table 4.2). Iteration stops when the change between two iterates,
relative to their mean, falls below $\mathrm{TOL}$, typically $10^{-6}$.
Four guesses are compared:
* two-rarefaction, exact when both waves are rarefactions,
  $$p_{\mathrm{TR}} = \left[\frac{c^- + c^+ - \tfrac12(\gamma-1)(v_n^+ - v_n^-)}{c^-/(p^-)^{\frac{\gamma-1}{2\gamma}} + c^+/(p^+)^{\frac{\gamma-1}{2\gamma}}}\right]^{\frac{2\gamma}{\gamma-1}};$$
* linearized (primitive-variable),
  $p_{\mathrm{PV}} = \tfrac12(p^- + p^+) - \tfrac18(v_n^+ - v_n^-)(\rho^- + \rho^+)(c^- + c^+)$,
  floored at $\mathrm{TOL}$;
* two-shock,
  $p_{\mathrm{TS}} = \dfrac{g^{\mathrm{TS}}_L(p_{\mathrm{PV}})\,p^- + g^{\mathrm{TS}}_R(p_{\mathrm{PV}})\,p^+ - (v_n^+ - v_n^-)}{g^{\mathrm{TS}}_L(p_{\mathrm{PV}}) + g^{\mathrm{TS}}_R(p_{\mathrm{PV}})}$,
  with the floored $p_{\mathrm{PV}}$ as argument (floored at $\mathrm{TOL}$
  here, eq. 4.48; the approximate-state TSRS floors at 0, eq. 9.45);
* the arithmetic mean $\tfrac12(p^- + p^+)$.

On the five tests below, 1 to 9 iterations suffice. "By excluding
Test 2, $p_{\mathrm{TS}}$ is the best guess overall" (p. 130); on Test 2
the two-rarefaction guess is exact and converges in one iteration, while
the PV and TS guesses hit the floor and need 8. Toro's program picks
among the three by a hybrid rule, and notes that "the overwhelming
majority of Riemann problems … can be accurately approximated by the
simple value $p_{\mathrm{PV}}$" (p. 133). Used without iteration, the
same formulas are the approximate-state solvers PVRS, TRRS and TSRS
([approximate Riemann solvers](/methods/approximate-riemann-solvers.md)).

**The rest of the star region and sampling** (§§4.4–4.5, eqs.
4.50–4.67). For a left shock,
$$\rho_{*L} = \rho^-\,\frac{p_*/p^- + \frac{\gamma-1}{\gamma+1}}{\frac{\gamma-1}{\gamma+1}\,p_*/p^- + 1}, \qquad \text{shock speed } v_n^- - c^-\left[\frac{\gamma+1}{2\gamma}\frac{p_*}{p^-} + \frac{\gamma-1}{2\gamma}\right]^{1/2}.$$
For a left rarefaction, $\rho_{*L} = \rho^-(p_*/p^-)^{1/\gamma}$ and
$c_{*L} = c^-(p_*/p^-)^{\frac{\gamma-1}{2\gamma}}$; the fan runs from the
head speed $v_n^- - c^-$ to the tail speed $v_{n*} - c_{*L}$, with the
state inside the fan in closed form (eq. 4.56). The right side is
symmetric, with $+$ data and the signs of the wave speeds reversed. A
flow chart samples the solution at any $x/t$ (Fig. 4.14). For a
covolume gas the same structure holds, with an extra iteration only
inside rarefactions (§4.7).

**In Godunov's method** (§§6.2–6.3). The interface flux is the physical
flux of the exact solution on the $t$-axis, $x/t = 0$; Toro enumerates
ten cases to sample there (Fig. 6.5, Table 6.1). Because only that value
is needed, the scheme is stable up to Courant number 1, twice the limit
under which neighbouring Riemann problems do not interact (eqs. 6.9,
6.13). The largest wave speed should come from the nonlinear waves of the
local Riemann problems. The common estimate
$\max_i(\vert (v_x)_i\vert + c_i)$ "can lead to an underestimate", for
example for gas initially at rest, so the book's runs reduce the Courant
number by a factor 0.2 for the first 5 steps (eqs. 6.19–6.20,
Remark 6.4.1). At a reflective wall the ghost state is the mirror state;
its Riemann problem is two shocks or two rarefactions with $v_{n*}$ equal
to zero (or to the wall speed), solvable in closed form (§6.3.3).

**Toro's test suite** (Table 4.1 states and Table 4.3 exact star values,
$\gamma = 1.4$):

| Test | $(\rho, v_x, p)^-$ | $(\rho, v_x, p)^+$ | $p_*$ | $v_{n*}$ | $\rho_{*L}$ | $\rho_{*R}$ |
|---|---|---|---|---|---|---|
| 1 ([Sod](/benchmarks/sod-shock-tube.md)) | (1.0, 0.0, 1.0) | (0.125, 0.0, 0.1) | 0.30313 | 0.92745 | 0.42632 | 0.26557 |
| 2 ([123 problem](/benchmarks/double-rarefaction.md)) | (1.0, −2.0, 0.4) | (1.0, 2.0, 0.4) | 0.00189 | 0.00000 | 0.02185 | 0.02185 |
| 3 (left half of the [blast waves](/benchmarks/interacting-blast-waves.md)) | (1.0, 0.0, 1000.0) | (1.0, 0.0, 0.01) | 460.894 | 19.5975 | 0.57506 | 5.99924 |
| 4 (right half) | (1.0, 0.0, 0.01) | (1.0, 0.0, 100.0) | 46.0950 | −6.19633 | 5.99242 | 0.57511 |
| 5 (collision of the shocks of 3 and 4) | (5.99924, 19.5975, 460.894) | (5.99242, −6.19633, 46.0950) | 1691.64 | 8.68975 | 14.2823 | 31.0426 |

The exact solutions are plotted at $t = 0.25$, 0.15, 0.012, 0.035 and
0.035, with no diaphragm position printed. The scheme chapters run a
renumbered set on $[0, 1]$ with 100 cells, Courant number 0.9 and
transmissive boundaries: the *modified* Sod problem ($v^- = 0.75$, a
sonic left rarefaction, diaphragm at 0.3, $t = 0.2$), Test 2 (diaphragm
0.5, $t = 0.15$), Test 3 (0.5, $t = 0.012$) and the collision as Test 4
(0.4, $t = 0.035$) (Table 6.2). Godunov with this solver (§6.4.1) gives,
on the modified Sod problem, a monotone shock over about 4 cells and
contact over about 20, and a small entropy glitch in the sonic
rarefaction, which "arises only in the presence of sonic rarefaction
waves" and should vanish as $h \to 0$ because the method is entropy
satisfying. On Test 2 it is good in $\rho$, $v_x$ and $p$ but poor in the
specific internal energy. On Test 3 the contact is worst, and the
post-shock density is not attained. On Test 4 of the scheme tests (the
shock collision, Test 5 of the table above) the slowly moving left
shock is sharp (2 cells) but not monotone, "so far … an unresolved
difficulty" ([slowly moving shock anomaly](/definitions/slowly-moving-shock-anomaly.md)).

**Uses in this bundle.**
* *Godunov's and Glimm's methods in Sod's survey.* Godunov's iteration as
  modified by Chorin: the star pressure and velocity from the two
  Lagrangian wave speeds, with an under-relaxation halved on
  non-convergence, and an appendix of sampling formulas
  ([Sod (1978)](/sources/sod-1978.md), eqs. 12–19, 46–62). Sod's Glimm
  plateau ($\rho = 0.426$, $v = 0.927$, $p = 0.303$; post-shock
  $\rho = 0.266$) agrees with Toro's exact Test-1 star values to the
  printed digits (compiler comparison of Sod's Table II with Toro's
  Table 4.3).
* *ADER.* In Toro and Titarev's original ADER the leading term of the
  interface state comes from an exact Riemann solver on the extrapolated
  states ([ADER](/methods/ader.md); [Dumbser et al. (2013)](/sources/dumbser-2013.md), §1).
* *Shock instability.* Godunov's exact solver resolves contacts and
  shear exactly and is among the complete solvers prone to the carbuncle
  and kinked Mach stems ([Simon & Mandal (2019)](/sources/simon-2019.md), §4.1;
  [numerical shock instability](/definitions/numerical-shock-instability.md)).
  At first order it kinks the stem of the
  [double Mach reflection](/benchmarks/double-mach-reflection.md), and
  the entropy-control term of Xie et al. can be added to its flux
  ([Xie et al. (2021)](/sources/xie-2021.md), §6.3;
  [cures for numerical shock instability](/methods/shock-instability-cures.md)).
* *Two-shock solvers in cut-cell codes.* An unsplit piecewise-linear
  Godunov scheme with a two-shock Riemann solver
  ([Barrio Sanchez et al. (2024)](/sources/barriosanchez-2024.md), §§2–3),
  and PeleC's two-shock solver
  ([Giuliani et al. (2022)](/sources/giuliani-2022.md), §§5–6). Neither
  page says which two-shock approximation is used; TSRS is the book's
  version.

MHD Riemann solvers with an exact or approximate nonlinear structure
(Dai & Woodward; Ryu & Jones) are on the
[approximate Riemann solvers](/methods/approximate-riemann-solvers.md)
page; the three-wave approximation of this fan is the
[HLLC Riemann solver](/methods/hllc-riemann-solver.md).

**Later uses (batch 14).**

**Godunov's own solver** ([Godunov (1959)](/sources/godunov-1959.md),
Ch. II §4, eqs. 6–8, pp. 287–292). The original is Lagrangian: the
interface sits on the contact, so no sampling of the fan at $x/t = 0$ is
needed, and the interface flux needs only $p_*$ and $v_{n*}$. With the
mass fluxes through the left and right waves, the star pressure is the
combination of $p^-$ and $p^+$ weighted by the *opposite* mass flux, plus
the product of the two mass fluxes times $v^- - v^+$, all over their sum;
$v_{n*}$ follows from a similar linear formula. The mass fluxes depend on
$p_*$ through the shock relation (Hugoniot) or, for $p_* < p^\mp$, the
rarefaction relation, so Godunov iterates on $p_*$: evaluate both mass
fluxes at the previous iterate, update $p_*$, then $v_{n*}$ (formulas on
the [source page](/sources/godunov-1959.md)). The plain iteration
"converges if the decay does not produce very strong rarefaction waves";
for all cases Godunov averages new and old iterates with a weight given
in closed form from the ratio of $p_*$ to $p^- + p^+$, zero when the
formula turns negative (p. 292). The convergence analysis is omitted as
"standard". This relaxation is Godunov's; the halving of the
under-relaxation on non-convergence in the *Uses* list above is Chorin's
modification as Sod reports it. With constant mass fluxes the formulas
reduce to the linear acoustic interface state of Ch. I.

**Step bound and wave interaction.** Godunov bounds the step by the
interface spacing over the largest Lagrangian wave speed, a Courant
number of 1, and justifies it by experiment ("a large number of varied
computations convincingly show" stability), not by proof. The stricter
condition that waves from neighbouring interfaces do not *meet* (half
the step) appears only as the case in which the in-layer solution is
analytically simple (pp. 292–293). This agrees with Toro's account above:
stable to Courant number 1, twice the no-interaction limit.

**Entropy.** Godunov proves that the specific entropy of each layer
average does not decrease over a step (eq. 9) and that limits satisfy
the entropy condition. This supports Toro's statement above that the
method is entropy satisfying, so that the sonic glitch should vanish as
$h \to 0$ ([Godunov's method](/methods/godunov-method.md)).

**Later uses (batch 14): van Leer's iteration.** In the Lagrangean
MUSCL scheme of [van Leer (1979)](/sources/vanleer-1979.md) (pp. 109–110, App. A) the iteration starts from
the acoustic (linear-wave) guess for the interface pressure (eq. 60). It
replaces Godunov's chord iteration, which gains a factor of the order of
the data jumps per cycle, by a tangent (Newton-type) iteration suggested
by P. J. Bedijn, which gains the square of that factor (eqs. A1–A3). In
smooth flow the linear guess alone "is more than adequate"; the code
iterates only where it differs from the neighbouring pressures by more
than 1 %, until successive iterates agree within 1.5 %, at 2–3 % of the
cost of the Lagrangean step on the shock tube (p. 110).

# Citations

1. [Toro (1997)](/sources/toro-1997.md), §§4.2–4.7, 6.2–6.4, 9.2.1, 12.3.4, Tables 4.1–4.3, 6.2.
2. [Sod (1978)](/sources/sod-1978.md), eqs. 12–19, 46–62, Table II.
3. [Dumbser et al. (2013)](/sources/dumbser-2013.md), §1.
4. [Simon & Mandal (2019)](/sources/simon-2019.md), §4.1.
5. [Xie et al. (2021)](/sources/xie-2021.md), §6.3.
6. [Barrio Sanchez et al. (2024)](/sources/barriosanchez-2024.md), §§2–3 (arXiv v1).
7. [Giuliani et al. (2022)](/sources/giuliani-2022.md), §§5–6 (arXiv v2).
8. [Godunov (1959)](/sources/godunov-1959.md), Ch. II §4 (reader's translation of the Russian original).
9. [van Leer (1979)](/sources/vanleer-1979.md), pp. 109–110, App. A.
