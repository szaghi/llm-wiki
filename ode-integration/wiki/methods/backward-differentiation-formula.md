---
type: Method
title: "Backward differentiation formulas (BDF)"
description: "The k-step BDF method differentiates the interpolant through the new and k past values: order k, A-stable for k = 1, 2 and A(alpha)-stable up to k = 6, one nonlinear solve per step; fixed- and variable-step forms, energy stability by G-norms and multipliers, step-ratio bounds, software and use in flow problems."
status: established
aliases: [BDF, BDFk, backward difference formula, Gear's method, BDF2, variable-step BDF2, variable-coefficient BDF]
tags: [linear-multistep, implicit, stiff, stability, step-size-control, dae]
timestamp: 2026-10-20T01:00:00Z
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

## Coefficients

With the normalization $\sigma(\zeta)=\zeta^k$:

| $k$ | $\sum_j\alpha_jy_{n+j}$ |
|---|---|
| 1 | $y_{n+1}-y_n$ |
| 2 | $\tfrac32y_{n+2}-2y_{n+1}+\tfrac12y_n$ |
| 6 | $\tfrac1{60}\big(147y_{n+6}-360y_{n+5}+450y_{n+4}-400y_{n+3}+225y_{n+2}-72y_{n+1}+10y_n\big)$ |

(BDF6 from Akrivis et al. 2021, §2; BDF2 from [García-Archilla & Novo (2023)](/sources/garciaarchilla-2023.md),
§2.) [Ma et al. (2026)](/sources/ma-2026.md) (Eq. (2.2)) normalize $\alpha_k=1$ instead, which
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
values for $k\le5$. No BDF of order above 2 is A-stable, by Dahlquist's second barrier;
[Taddei et al. (2026)](/sources/taddei-2026.md) (§1.1) give this as their reason to prefer
Radau IIA for high order. The error constants, normalized by $\sigma(1)$, are $1/(k+1)$ in
modulus (Glandon et al. 2022, Table 6.1).

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

## Qualifications

- **Normalizations.** Akrivis et al. (2021) normalize $\sigma(\zeta)=\zeta^k$
  ($\alpha_6=147/60$), Ma et al. (2026) normalize $\alpha_k=1$, and Gardner et al. (2022) print
  CVODE's form with $+h\sum\beta$. The methods are the same; only the coefficients' scale and
  sign differ.
- **Version read.** Akrivis et al. (2021), García-Archilla & Novo (2023), Ma et al. (2026) and
  Taddei et al. (2026) were read as arXiv preprints. Their claims here are those of the
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
