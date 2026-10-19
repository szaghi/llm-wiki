---
type: Method
title: "Low-storage Runge–Kutta methods"
description: "Explicit Runge–Kutta methods whose coefficients are restricted so that a step needs only two or three solution-sized registers; the 2N, 2R, 3S* and 3S*+ classes, three registers as the minimum with an error estimate and step rejection, and SSP and optimized low-storage pairs."
status: established
aliases: [low-storage RK, 2N methods, 2R methods, 3S* methods, 3S*+ methods, Williamson methods, register-efficient Runge–Kutta]
tags: [runge-kutta, explicit, step-size-control, ssp]
timestamp: 2026-10-19T00:00:00Z
---

# Low-storage Runge–Kutta methods

A **low-storage** explicit [Runge–Kutta method](/definitions/runge-kutta-method.md) is one whose
coefficients admit an implementation that keeps only a few solution-sized arrays
(**registers**, $d$ words each) alive during a step, instead of the $s$ stage derivatives of
a generic implementation. For method-of-lines semidiscretizations with many unknowns the
register count, not the arithmetic, often decides which method fits in memory. The classes are
named by register count and by the form of the update the implementation may perform
([Ranocha et al. 2022](/sources/ranocha-2022.md), §2.1, Remark 3.1).

## Classes

Ranocha et al. (2022) use the storage notation of Ketcheson (2010), as recalled in their §2.1
and Remark 3.1:

- **$n$N** (Williamson; Carpenter–Kennedy): $n$ registers with updates of the form
  $S_j\leftarrow\alpha S_j+F(S_i)$ that need no extra allocation; e.g. CK4(3)5[2N] of Carpenter
  and Kennedy (1994), which has no usable embedded estimator (§5);
- **$n$R** (Kennedy–Carpenter–Lewis): $n$ registers with updates $S_j\leftarrow F(S_j)$; e.g.
  KCL3(2)4[2R$_+$]C, KCL4(3)5[2R$_+$]C, KCL5(4)9[2R$_+$]S;
- **3S\***: three-register methods *including* an error estimate, valid if assignments
  $S_j\leftarrow S_j+F(S_j)$ can be done with $d+o(d)$ memory (otherwise one more register);
- **3S\*$_+$**: three-register methods that need a fourth register for the error estimate.

A subscript $+$ on any class means one extra register when the embedded estimator is used
($S_j$ denotes registers on this page, page-local). Three registers is the fewest possible if an
error estimate *and* step rejection are required (Ranocha et al. §2.1).

## The 3S\* and 3S\*$_+$ algorithms

A 3S\* method is defined by coefficients $c_i,\gamma_{1,i},\gamma_{2,i},\gamma_{3,i},\beta_i,\delta_i$
(Ketcheson's parametrization; page-local symbols, unrelated to the Rosenbrock $\gamma$, the
Shu–Osher $\beta_{ij}$ and the PID exponents). Ranocha et al. (2022), Algorithm 2 (3S\*$_+$),
in registry notation:

$$\begin{aligned}
&S_1\leftarrow y_n,\quad S_2\leftarrow0,\quad S_3\leftarrow y_n,\quad S_4\leftarrow y_n;\\
&\text{for } i=1,\dots,s:\quad F\leftarrow f(t_n+c_ih,S_1),\quad S_2\leftarrow S_2+\delta_iS_1,\\
&\qquad S_1\leftarrow\gamma_{1,i}S_1+\gamma_{2,i}S_2+\gamma_{3,i}S_3+\beta_ihF,\qquad S_4\leftarrow S_4+\hat b_ihF;\\
&y_{n+1}\leftarrow S_1,\qquad \hat y_{n+1}\leftarrow S_4\;\bigl[+\,h\,\hat b_{s+1}f(t_{n+1},y_{n+1})\ \text{(FSAL)}\bigr].
\end{aligned}$$

Without the embedded method (no $S_4$) it reduces to a 3S\* method without estimator. In the
3S\* algorithm (their Algorithm 1) the embedded solution is a normalized combination of the
three registers instead of a fourth register (see Qualifications).

## SSP methods in low-storage form

Several optimal [SSP methods](/methods/strong-stability-preserving-runge-kutta.md) are
low-storage. [Fekete et al. (2022)](/sources/fekete-2022.md) note that Ketcheson's SSPRK(10,4),
with SSP coefficient 6, admits a low-storage implementation (§2.3). Ranocha et al. (2022) give a
three-register implementation of Kraaijevanger's four-stage third-order SSP method with the
embedded weights $\hat b=\tfrac14\mathbf 1$ of Conde, Fekete and Shadid (Appendix A, Eq. (A.2)):

$$\begin{aligned}
&u\leftarrow y_n+\tfrac h2f(t_n,y_n),\quad u\leftarrow u+\tfrac h2f(t_n+\tfrac h2,u),\quad u\leftarrow u+\tfrac h2f(t_n+h,u),\\
&\hat u\leftarrow\tfrac13y_n+\tfrac23u,\quad u\leftarrow\tfrac23y_n+\tfrac13u,\quad u\leftarrow u+\tfrac h2f(t_n+\tfrac h2,u),\quad \hat u\leftarrow\tfrac12(\hat u+u),
\end{aligned}$$

ending with $u=y_{n+1}$, $\hat u=\hat y_{n+1}$ ($u$, $\hat u$ page-local registers). The error
estimate $\hat y_{n+1}-y_{n+1}$ is available directly as $(\hat u-u)/2$ in the last assignment.
Three memory locations suffice under the low-storage assumption of Ketcheson (2010); otherwise
one more is needed for evaluating $f$.

## Optimized low-storage pairs

Ranocha et al. (2022) construct six 3S\*$_+$ [embedded pairs](/methods/embedded-runge-kutta-pair.md),
RK3(2)5, RK4(3)9 and RK5(4)10 with FSAL variants. Their main methods are the 3S\*
stability-optimized schemes of Parsani, Ketcheson and Deconinck (2013) (see
[optimal stability polynomials](/methods/optimal-stability-polynomial.md)); the embedded weights
and the PID controllers are new (§6, Appendix B, Tables 12–17). The coefficients were refined in
extended precision so that the order conditions hold at least to quadruple precision, and are
printed as $\gamma_{1,i},\gamma_{2,i},\gamma_{3,i},\delta_i,\beta_i,\hat b_i$ (with $c_i$ not
tabulated) and contributed to [DifferentialEquations.jl](/software/differentialequations-jl.md).
Real stability intervals per right-hand-side evaluation (Suppl. Table 1):

| Pair | real stability interval | per evaluation |
|---|---|---|
| BS3(2)3F (not low-storage, reference) | 2.51 | 0.84 |
| SSP3(2)4[3S\*$_+$] | 5.15 | 1.29 |
| KCL4(3)5[3R$_+$]C | 4.66 | 0.93 |
| RK3(2)5[3S\*$_+$] | 4.93 | 0.99 |
| RK4(3)9[3S\*$_+$] | 9.47 | 1.05 |
| RK5(4)10[3S\*$_+$] | 8.23 | 0.82 |

## Performance of low-storage classes

On compressible-flow tests Ranocha et al. (2022) find:

- the Kennedy–Carpenter–Lewis 2R pairs, although designed for convection-dominated CFD, are
  beaten by the general-purpose BS3(2)3F on all test problems at almost all tolerances. They
  attribute this to the stringent 2R constraints, the lack of FSAL, and embedded stability
  regions smaller than the main one in places (§5.5.4, Fig. 5);
- the new 3S\*$_+$ third-order pairs are up to 18% cheaper than BS3(2)3F, and the fourth- and
  fifth-order ones up to 25–35% cheaper than the corresponding KCL pairs with the controller
  KCL recommend (§6.2);
- in 3D runs up to $4.09\times10^7$ degrees of freedom, the low-storage SSP3(2)4[3S\*$_+$] and
  RK3(2)5F[3S\*$_+$] are the most efficient choices with error-based
  [step-size control](/methods/step-size-control.md) (§7, Tables 7–10).

## Qualifications

- Ranocha et al. print the embedded-solution line of their Algorithm 1 (3S\*) as
  $(S_2+\delta_sS_1+\delta_{s+1}S_3)/\sum_{i=1}^{s+1}\delta_i$. Every coefficient table lists only
  $\delta_1,\dots,\delta_s$, with $\delta_s=0$, and the loop already adds $\delta_sS_1$. The
  indices look shifted by one relative to Ketcheson (2010), whose formula uses $\delta_{s+1}$,
  $\delta_{s+2}$ (reader's note, not verified against Ketcheson 2010). The new methods use
  Algorithm 2, which is unaffected.
- The tag F (FSAL) and the stage count in method names follow the effective-evaluation convention
  described on the [embedded-pair page](/methods/embedded-runge-kutta-pair.md).

# Citations

- [Ranocha et al. (2022)](/sources/ranocha-2022.md) — §2.1 (Algorithms 1–2), Remark 3.1, §5, §5.5.4 (Fig. 5), §6.2, §7, Appendix A (Eqs. (A.1)–(A.2)), Appendix B (Tables 12–17), Suppl. Table 1.
- [Fekete et al. (2022)](/sources/fekete-2022.md) — §2.3 (SSPRK(10,4) low-storage implementation).
