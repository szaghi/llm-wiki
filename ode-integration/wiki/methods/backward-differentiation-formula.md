---
type: Method
title: "Backward differentiation formulas (BDF)"
description: "The k-step BDF method differentiates the interpolant through the new and k past values, introduced for k = 1 to 4 as Curtiss–Hirschfelder forward interpolation for stiff equations: order k, A-stable for k = 1, 2 and A(alpha)-stable up to k = 6, one nonlinear solve per step; fixed- and variable-step forms, energy stability by G-norms and multipliers, step-ratio bounds, software and use in flow problems."
status: established
aliases: [BDF, BDFk, backward difference formula, Gear's method, forward interpolation, BDF2, variable-step BDF2, variable-coefficient BDF]
tags: [linear-multistep, implicit, stiff, stability, step-size-control, dae, parallel]
timestamp: 2026-10-29T18:13:00Z
---

# Backward differentiation formulas (BDF)

The **$k$-step backward differentiation formula** (BDF$k$) is the
[linear multistep method](/methods/linear-multistep-method.md) with

$$\varrho(\zeta)=\sum_{j=1}^k\frac1j\,\zeta^{k-j}(\zeta-1)^j,\qquad\sigma(\zeta)=\zeta^k,$$

so that $\sum_{j=0}^k\alpha_jy_{n+j}=hf(t_{n+k},y_{n+k})$. It has order $k$
([Akrivis et al. (2021)](/sources/akrivis-2021.md), arXiv v1, §1, Eqs. (1.2)–(1.3)). The left-hand side is
$h$ times the derivative at $t_{n+k}$ of the polynomial interpolating $y_n,\dots,y_{n+k}$. The
method is implicit and needs one nonlinear solve per step at every order, which is the reason
the sources give for its efficiency on stiff and diffusive problems
([Gardner et al. (2022)](/sources/gardner-2022.md), §5.1). It is the implicit member of most
[IMEX multistep schemes](/methods/imex-linear-multistep-methods.md).

## Origin: forward interpolation for stiff equations

[Curtiss & Hirschfelder (1952)](/sources/curtiss-1952.md) introduce BDF1–BDF4, under the name
"forward interpolation", in the paper that defines [stiff](/definitions/stiffness.md) equations.
For the scalar equation $y'=(y-G(t))/a(t,y)$ ($G$, $a$ page-local, as on the stiffness page) they
evaluate the right-hand side at the forward (new) point $t_n$ and replace $y'(t_n)$ by the
derivative of the polynomial through $y_n,y_{n-1},\dots$: a straight line, quadratic, cubic or
quartic (§2–3, Eqs. (8)–(10), (17), (20), (22)). Solved for $y_n$, the steps have denominators
$1-\tfrac{a}{h}$, $1-\tfrac32\tfrac ah$, $1-\tfrac{11}6\tfrac ah$ and $1-\tfrac{25}{12}\tfrac ah$.
The step is explicit in $y_n$ when $a$ does not depend on $y$ and implicit otherwise (p. 240).
"Forward" refers to the new point, not to a forward-difference formula.

Their justification is that the scheme "forces $y_n$ to seek out and approximate" the smooth
solution of the stiff equation "regardless of the starting conditions and regardless of the
direction of integration" (§2, p. 238; §3, p. 242), shown on $y'=5(y-t^2)$ in both directions
(Figs. 3–4). A geometric reading, credited to Creighton Buck, makes each step follow the exact
solution whose tangent at the new point passes through the previous point (§2, p. 240, Fig. 3).
For $a$ independent of $y$ the linear scheme propagates the error with the factor
$-b$, $b=\frac{a/h}{1-a/h}$ (Eq. (15)), and "the larger the interval size $\Delta x$, the smaller
the value of $b$" (§3, p. 241). *(Compiler check, not in the sources: with $z=h/a$,
$-b=1/(1-z)$, the backward-Euler [stability function](/definitions/stability-function.md).)*
The error then tends to an asymptote proportional to $a$ times powers of $h$ (Eqs. (16), (19);
see Qualifications). The paper gives no order, generating polynomials, zero-stability or
stability angles, no BDF5 or BDF6, and no starting procedure.

## Coefficients

With the normalization $\sigma(\zeta)=\zeta^k$:

| $k$ | $\sum_j\alpha_jy_{n+j}$ |
|---|---|
| 1 | $y_{n+1}-y_n$ |
| 2 | $\tfrac32y_{n+2}-2y_{n+1}+\tfrac12y_n$ |
| 3 | $\tfrac{11}6y_{n+3}-3y_{n+2}+\tfrac32y_{n+1}-\tfrac13y_n$ |
| 4 | $\tfrac{25}{12}y_{n+4}-4y_{n+3}+3y_{n+2}-\tfrac43y_{n+1}+\tfrac14y_n$ |
| 6 | $\tfrac1{60}\big(147y_{n+6}-360y_{n+5}+450y_{n+4}-400y_{n+3}+225y_{n+2}-72y_{n+1}+10y_n\big)$ |

(BDF6 from Akrivis et al. 2021, §2; BDF2 from [García-Archilla & Novo (2023)](/sources/garciaarchilla-2023.md),
§2; BDF1–BDF4 are Curtiss & Hirschfelder's Eqs. (10), (17), (20), (22) multiplied out *(compiler
check, not in the sources: each reads $\sum_j\alpha_jy_{n-j}=hf(t_n,y_n)$ with the coefficients of the row, indexed back from the new point; the rows for
$k=1,2$ agree with the other sources)*.) [Ma et al. (2026)](/sources/ma-2026.md) (Eq. (2.2)) normalize $\alpha_k=1$ instead, which
moves the factor to the right-hand side:

$$y_{n+2}-\tfrac43y_{n+1}+\tfrac13y_n=\tfrac23hf_{n+2},\qquad y_{n+3}-\tfrac{18}{11}y_{n+2}+\tfrac9{11}y_{n+1}-\tfrac2{11}y_n=\tfrac6{11}hf_{n+3}.$$

## Linear stability

BDF1 and BDF2 are A-stable. BDF$k$ for $3\le k\le6$ is A($\vartheta_k$)-stable, with
$\vartheta_k$ (page-local) the angle of [A($\alpha$)-stability](/properties/a-stability.md):

| $k$ | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| $\vartheta_k$ | $90^\circ$ | $90^\circ$ | $86.03^\circ$ | $73.35^\circ$ | $51.84^\circ$ | $17.84^\circ$ |

Akrivis et al. (2021, §1) give the angles for $k\le6$, citing Hairer–Wanner and Akrivis–Katsoprinakis
for the exact values. [Glandon et al. (2022)](/sources/glandon-2022.md) (Table 6.1) give the same
values for $k\le5$. No BDF of order above 2 is A-stable, by
[Dahlquist's order barrier](/results/dahlquist-second-barrier.md);
[Taddei et al. (2026)](/sources/taddei-2026.md) (§1.1) give this as their reason to prefer
Radau IIA for high order. [Kennedy & Carpenter (2003)](/sources/kennedy-2003.md) (§1) state that at
third order and above BDF are "only L($\alpha$) stable; they lack A-stability but still have a
vanishing stability function for extremely stiff eigenvalues", and that SBDF methods, which use
BDF for the implicit part, "may be quite effective for equations whose stiff terms give rise to
predominately real eigenvalues" but suit transients such as chemical ignition less, "because they
lack stepsize adjustment"; their comparison with IMEX Runge–Kutta methods is on
[IMEX linear multistep methods](/methods/imex-linear-multistep-methods.md). The error constants, normalized by $\sigma(1)$, are $1/(k+1)$ in
modulus (Glandon et al. 2022, Table 6.1); the leading truncation coefficients $\tfrac12$,
$\tfrac13$, $\tfrac14$, $\tfrac15$ printed by Curtiss & Hirschfelder (1952, Eqs. (14), (18),
(21), (23)) for $k=1,\dots,4$ have these moduli *(compiler check, not in the sources)*.

## Variable steps

On a nonuniform grid, with $h_n=t_{n+1}-t_n$ and $r_n=h_n/h_{n-1}$, variable-step BDF2 reads

$$\frac{1+2r_n}{1+r_n}\,y_{n+1}-(1+r_n)\,y_n+\frac{r_n^2}{1+r_n}\,y_{n-1}=h_nf(t_{n+1},y_{n+1}).$$

This is [Akrivis et al. (2024)](/sources/akrivis-2024.md) (Eq. (1.2)) and García-Archilla & Novo
(2023, §2, operator $\mathcal D$) written in registry notation; both forms reduce to the same
coefficients *(compiler check)*. At $r_n=1$ they are those of the table. The two sources also
split the operator differently:

- **Akrivis et al. (2024)** use backward differences, with weights $1/(1+r_n)$ and
  $\big(r_n/(1+r_n)\big)^2$ (Eq. (1.6)).
- **García-Archilla & Novo (2023)** use the linear extrapolation $y_n+r_n(y_n-y_{n-1})$ to
  $t_{n+1}$, the same value that the IMEX variant gives to the explicit term.

Variable-order, variable-step codes recompute all coefficients from the step history
(Gardner et al. 2022, §2.1; Glandon et al. 2022, §7).

**Stability with variable steps.** The sources prove several step-ratio bounds, each for a
different estimate:

- zero-stability of variable-step BDF2 holds for $r_n<1+\sqrt2\approx2.414$, sharp
  (Akrivis et al. 2024, §1.3, as recalled);
- an energy estimate for parabolic problems holds for $r_n\le1.9398$ (Akrivis et al. 2024,
  Thm. 1.1);
- García-Archilla & Novo (2023, Thms. 3–4) prove Navier–Stokes error bounds under their own
  ratio bounds and a bound on the total variation of the ratios.

These numbers bound different quantities and are not competing values of one constant. The
comparison is on [variable-step BDF2 stability](/results/variable-step-bdf2-stability.md), and
the ODE notion on [zero-stability](/definitions/zero-stability.md).

## Energy stability for parabolic problems

For $y'=Ly$ with $-L$ self-adjoint and positive definite, stability proofs by the energy method
depend on $k$:

- **$k=1,2$.** A-stability gives a [G-norm](/properties/g-stability.md), and the energy method
  applies directly (Akrivis et al. 2021, §1; Akrivis et al. 2024, §1.3).
- **$k=3,4,5$.** Testing the scheme with $y_{n+k}-\sum_j\mu_jy_{n+k-j}$, with Nevanlinna–Odeh
  multipliers $\mu_j$, extends the technique (Akrivis et al. 2021, §2); see
  [multiplier energy technique](/methods/multiplier-energy-technique.md).
- **$k=6$.** No Nevanlinna–Odeh multiplier exists. Akrivis et al. (2021) prove stability with a
  relaxed multiplier condition; see [BDF6 energy stability](/results/bdf6-energy-stability.md).

Ma et al. (2026, Lemma 2.1) use the multiplier identities for $k\le4$ to prove uniform accuracy
of IMEX-BDF for hyperbolic relaxation systems.

## Implementations and use

- **SUNDIALS.** [CVODE](/software/cvode.md) uses variable-order, variable-step BDF of orders 1–5
  in fixed-leading-coefficient form for stiff problems, and IDA uses the same orders for DAEs
  $F(t,y,y')=0$ (Gardner et al. 2022, §2.1–2.2; see
  [differential-algebraic equations](/definitions/differential-algebraic-equation.md)). On a
  $4096^2$ heat equation, CVODE's BDF took 8.8 s against 67.3 s for ARKODE's default DIRK
  (Gardner et al. 2022, §5.1, Table 5). A multistep inner integrator restarts at first order
  after every reset, which costs it in multirate use
  ([Reynolds et al. (2023)](/sources/reynolds-2023.md), §5.1.3).
- **Comparisons with linearly implicit multistep methods.** Glandon et al. (2022, §8) use a
  self-starting variable-step, variable-order BDF in their own MATLAB framework as the baseline.
  It shares the controller and the error estimator of their
  [Limm methods](/methods/linearly-implicit-multistep-method.md). MATLAB's ode15s in its BDF and
  NDF modes is a second baseline. Limm was slightly faster than the same-framework BDF on two
  problems (Figs. 8.2–8.3).
- **Incompressible flow.** García-Archilla & Novo (2023) analyse BDF2 with implicit viscosity
  and either explicit or linearly implicit convection. They use variable-order (BDF1/BDF2)
  adaptive steps after Hairer–Wanner §III.5 on the
  [flow past a cylinder](/benchmarks/flow-past-cylinder.md) (§4). BDF2 for the fluid with a
  [Newmark](/methods/newmark-method.md) structure solver is the common practice in fluid–structure
  interaction. On the Turek–Hron FSI3 benchmark this pairing was unstable when undamped, and
  stable but more dissipative than Radau IIA when damped (Taddei et al. 2026, §1.1, §5.2.1,
  Figs. 10–11).

## Positivity-preserving solution by dual time stepping

[Sayyari & Yamaleev (2026)](/sources/sayyari-2026.md) use BDF1 and constant-step BDF2 in
physical time for a positivity-preserving entropy-stable spectral-collocation discretization
of compressible Navier–Stokes, and solve each step by dual time stepping: a pseudotime
iteration whose update is a forward-Euler step scaled by $C_1=h/(h+\delta)$ (BDF1) or
$C_2=2h/(2h+3\delta)$ (BDF2), $\delta$ the pseudo-step, applied to a combination of the
current iterate and the past solutions (§4, §7, Eqs. (9)–(13), (23)–(24); scheme on
[implicit stage solvers](/methods/implicit-stage-solvers.md)). Their results and limits:

- **Positivity per pseudo-iteration.** Density positivity holds for pseudo-steps below a
  bound that exceeds the forward-Euler one by the BDF term (Thm. 1, Eq. (16); BDF2 analogue in
  §7.1, where the excess is guaranteed only if the density does not drop by more than a factor
  4 in one step, see the Qualifications of [implicit stage solvers](/methods/implicit-stage-solvers.md)), and internal-energy positivity holds for some positive pseudo-step (Eqs. (18)–(19),
  (26)). The property concerns every iterate; the converged BDF solution, as their limit, is
  only guaranteed nonnegative, and convergence of the iteration is not proved *(compiler
  remark)*. "No constraint on the physical time step" therefore holds for the BDF solution
  only, with an explicit bound remaining on the pseudo-step (§9).
- **Entropy stability.** BDF1 is unconditionally entropy stable (Tadmor, as recalled), so the
  converged BDF1 scheme with entropy-dissipative spatial terms is entropy stable, provided the
  pseudo-residual is driven below the BDF1 entropy dissipation (§5); nothing is claimed for
  BDF2.
- **Why not higher order.** BDF3 and higher are excluded because they are not A-stable
  (Remark 3), the A($\vartheta$) angles of the table above.
- **Evidence.** BDF2 converges at about second order on a 3D viscous shock on perturbed grids
  (rates 2.10 in $L^1$ and 2.19 in $L^2$ at the finest level, Table 1), and on a Mach 10
  Taylor–Green vortex takes physical steps on average 20 times those of SSPRK3, about 30%
  faster in wall-clock time at degree 6 on $64^3$ elements, slightly more dissipative in line
  profiles (§8.1, §8.4.2). See [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) and
  [positivity preservation](/properties/positivity-preservation.md).

## Parallel in time

With constant steps, the BDF$k$ equations of all $N$ steps of a linear problem $y'=Ly+g$ form one
space-time system whose time matrix is banded lower-triangular Toeplitz, with the BDF
coefficients on the first $k$ subdiagonals. [Gander & Palitta (2024)](/sources/gander-2024.md)
write it as a circulant matrix minus a rank-$k$ correction built from the BDF coefficients, so
that their [ParaDiag](/methods/paradiag.md) solver applies: after an FFT in time, $N$ independent
shifted solves with $hL$ scaled by $\beta_k$, plus a $kd\times kd$ capacitance system solved by a
block Galerkin method (§5, Eqs. (5.1)–(5.6), Prop. 5.1). They recall that BDF of order above 6 is
unstable (§5, citing Hairer–Wanner), i.e. not [zero-stable](/definitions/zero-stability.md). No
experiment uses $k>1$; the tests are backward Euler only (§6).

## Qualifications

- **Curtiss & Hirschfelder's error formulas.** Their asymptotes (Eqs. (16), (19)) and error
  recursions (Eqs. (18), (21), (23)) are derived for $a$ independent of $y$. The sign of
  Eq. (16), the sign and coefficients of Eq. (19) and an index in Eq. (23) differ from what the
  printed recursions give *(compiler check, not in the sources; recorded under Printed slips on
  the [Source page](/sources/curtiss-1952.md))*; only the proportionality of the asymptotic error to
  $a$ times powers of $h$ is used on this page. "The series converges for values of $b$ less than
  unity" (p. 241) is printed without a modulus; for their Fig. 4, $a/h=-\tfrac15$, Eq. (15) gives
  $b=-\tfrac16$ *(compiler check, not in the sources)*.

- **Normalizations.** Akrivis et al. (2021) normalize $\sigma(\zeta)=\zeta^k$
  ($\alpha_6=147/60$), Ma et al. (2026) normalize $\alpha_k=1$, and Gardner et al. (2022) print
  CVODE's form with $+h\sum\beta$. Gander & Palitta (2024, Table 5.1) normalize $\alpha_k=1$ and
  move the past values to the right-hand side, $y_{n+k}=\sum_{j}\tilde\alpha_jy_{n+k-j}+h\beta_kf_{n+k}$
  with $\tilde\alpha_j$ (page-local) the negated coefficients, e.g. $\tfrac43,-\tfrac13$ and
  $\beta_2=\tfrac23$ for BDF2 and $\beta_6=\tfrac{60}{147}$ for BDF6; they state the sign flip
  relative to Hairer–Wanner. The methods are the same; only the coefficients' scale and sign
  differ.
- Gander & Palitta (2024) do not discuss that BDF$k$ is not A-stable for $k\ge3$; their
  conditioning theorem covers backward Euler with symmetric positive definite $-L$ only.
- **Version read.** Akrivis et al. (2021), García-Archilla & Novo (2023), Ma et al. (2026),
  Taddei et al. (2026) and Sayyari & Yamaleev (2026) were read as arXiv preprints. Their claims here are those of the
  preprints.
- **The FSI evidence is numerical.** The BDF2–Newmark instability is shown on one benchmark.
  The plot that shows it covers a time window in which no energy growth is visible (Taddei et al.
  2026, Fig. 10; recorded on the Source page).

# Citations

- [Akrivis et al. (2021)](/sources/akrivis-2021.md) — arXiv v1: §1 (Eqs. (1.2)–(1.3), order, A($\vartheta$) angles), §2 (BDF6 polynomial, multipliers).
- [Akrivis et al. (2024)](/sources/akrivis-2024.md) — §1 (Eqs. (1.2), (1.6)), §1.3, Thm. 1.1.
- [García-Archilla & Novo (2023)](/sources/garciaarchilla-2023.md) — §2 (variable-step BDF2 operator), Thms. 1–4, §4.
- [Ma et al. (2026)](/sources/ma-2026.md) — Eq. (2.2), Lemma 2.1.
- [Glandon et al. (2022)](/sources/glandon-2022.md) — §7, §8 (Figs. 8.2–8.3), Table 6.1.
- [Taddei et al. (2026)](/sources/taddei-2026.md) — §1.1, §5.2.1 (Figs. 10–11).
- [Gardner et al. (2022)](/sources/gardner-2022.md) — §2.1–2.2, §5.1 (Table 5).
- [Reynolds et al. (2023)](/sources/reynolds-2023.md) — §5.1.3.
- [Gander & Palitta (2024)](/sources/gander-2024.md) — arXiv v2: §5 (Eqs. (5.1)–(5.6), Table 5.1, Prop. 5.1), §6.
- [Curtiss & Hirschfelder (1952)](/sources/curtiss-1952.md) — §2 (Eqs. (8)–(10), pp. 238–240, Figs. 3–4); §3 (Eqs. (11)–(23), pp. 240–242).
- [Kennedy & Carpenter (2003)](/sources/kennedy-2003.md) — read as NASA/TM-2001-211038: §1 (L($\alpha$)-stability of BDF, SBDF).
- [Sayyari & Yamaleev (2026)](/sources/sayyari-2026.md) — arXiv v3: §4–5 (Eqs. (9)–(19), Thm. 1, Remark 1), §7 (Eqs. (23)–(26), Remark 3), §8.1 (Table 1), §8.4.2, §9.
