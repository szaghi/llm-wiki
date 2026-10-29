---
type: Method
title: "Low-storage Runge–Kutta methods"
description: "Explicit Runge–Kutta methods whose coefficients let a step run in two or three solution-sized registers: the 2N, 2R, 3S* and 3S*+ classes, the Butcher-form characterization of Williamson 2N methods, three registers as the minimum with error estimate and step rejection, SSP, optimized, many-stage and paired variants, and stage coupling in asynchronous distributed solvers."
status: established
aliases: [low-storage RK, LSERK, LSERK-AT, 2N methods, 2N-storage methods, 2R methods, 3S* methods, 3S*+ methods, Williamson methods, register-efficient Runge–Kutta]
tags: [runge-kutta, explicit, low-storage, step-size-control, ssp, order-conditions]
timestamp: 2026-10-29T18:00:00Z
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

[Bazavov (2026)](/sources/bazavov-2026.md) uses "2N-storage" in a narrower sense: Williamson's
form below with every coefficient $A^{\mathrm W}_i\neq0$ for $i\ge2$. Methods with some
$A^{\mathrm W}_i=0$, such as some of Ruuth's, fall outside his theory (§2, Remark 2).

## Williamson 2N-storage methods

**Form.** Williamson's two-register scheme (as recalled by Bazavov 2026, §2, Eqs. (7)–(9);
$A^{\mathrm W}_i$, $B^{\mathrm W}_i$ page-local, unrelated to the Butcher matrix $A$ and to $b$)
keeps the solution in $S_1$ and an accumulated increment in $S_2$:

$$S_1\leftarrow y_n;\qquad\text{for }i=1,\dots,s:\quad S_2\leftarrow A^{\mathrm W}_iS_2+hf(t_n+c_ih,S_1),\quad S_1\leftarrow S_1+B^{\mathrm W}_iS_2;\qquad y_{n+1}\leftarrow S_1,$$

with $A^{\mathrm W}_1=0$. At the start of iteration $i$, $S_1$ holds the stage value $Y_i$. The
Butcher coefficients follow recursively: $a_{i,i-1}=B^{\mathrm W}_{i-1}$,
$a_{ij}=A^{\mathrm W}_{j+1}a_{i,j+1}+B^{\mathrm W}_j$ for $j<i-1$, $b_s=B^{\mathrm W}_s$,
$b_i=A^{\mathrm W}_{i+1}b_{i+1}+B^{\mathrm W}_i$ (Eqs. (13)–(14)). A 2N method has $2s-1$ free
coefficients against $s(s+1)/2$ for a general explicit method.

**Characterization (Bazavov 2026, §3–4).** Write any explicit method in increments from the
previous stage, $Y_i=Y_{i-1}+h\sum_jd_{ij}f(t_n+c_jh,Y_j)$ and
$y_{n+1}=Y_s+h\sum_jd_{s+1,j}f(t_n+c_jh,Y_j)$, with $d_{ij}=a_{ij}-a_{i-1,j}$ and
$d_{s+1,j}=b_j-a_{sj}$ ($d_{ij}$ page-local; Bazavov's "α-form", Eqs. (23)–(29)). This
representation is bijective with the Butcher tableau and resembles the Shu–Osher form, but is
not a convex-combination form (Remark 1).

- **Theorem 1.** A method is 2N-storage with all $A^{\mathrm W}_i\ne0$ ($i\ge2$) iff, for
  $j=1,\dots,s-2$,
  $$\frac{d_{j+2,j}}{d_{j+2,j+1}}=\frac{d_{j+3,j}}{d_{j+3,j+1}}=\dots=\frac{d_{s,j}}{d_{s,j+1}}=\frac{d_{s+1,j}}{d_{s+1,j+1}},$$
  and the common ratio is $A^{\mathrm W}_{j+1}$ (Eq. (42)).
- **Theorem 2.** In Butcher form the conditions are quadratic and independent of the order:
  $$a_{ij}\bigl(b_{j-1}-a_{j,j-1}\bigr)=\bigl(a_{i,j-1}-a_{j,j-1}\bigr)b_j,\qquad i=3,\dots,s,\ j=2,\dots,i-1,$$
  (Eq. (47); an equivalent form is Eqs. (45)–(46)). Exactly $(s-1)(s-2)/2$ of them are
  independent, which equals $s(s+1)/2-(2s-1)$, the difference of the parameter counts. The
  polynomial form admits spurious zero solutions, which must be checked against Theorem 1
  (Remark 3). A **2N-storage method of order $p$** is then a solution of the
  [order conditions](/results/runge-kutta-order-conditions.md) together with these constraints.
- **Theorem 3.** Closed, non-recursive maps between $(A^{\mathrm W}_i,B^{\mathrm W}_i)$ and $(A,b)$:
  $B^{\mathrm W}_i=a_{i+1,i}$ ($i<s$), $B^{\mathrm W}_s=b_s$, and
  $A^{\mathrm W}_i=\dfrac{a_{k,i-1}-a_{k-1,i-1}}{a_{ki}-a_{k-1,i}}$ for any $i<k\le s$, or
  $A^{\mathrm W}_i=\dfrac{b_{i-1}-a_{s,i-1}}{b_i-a_{s,i}}$ (Eqs. (59)–(63)). A vanishing numerator or
  denominator means the method is not 2N-storage in this sense; earlier relations of this kind
  existed only for particular $s$ (Carpenter–Kennedy for $s=5$, Allampalli et al. for $s=7$, as
  recalled in §5).
- **Theorems 4–5.** In the general case (nonvanishing denominators) $b$ and $c$ determine
  everything:
  $$a_{ij}=\frac{b_j}{\sum_{k=1}^{j}b_k-c_j}\Bigl[c_i-c_j-\sum_{k=j+1}^{i-1}a_{ik}\Bigr],\qquad
  A^{\mathrm W}_i=\frac{b_{i-1}}{b_i}\,\frac{\sum_{k=1}^{i-1}b_k-c_i}{\sum_{k=1}^{i-1}b_k-c_{i-1}},\qquad
  B^{\mathrm W}_i=\frac{b_i\,(c_{i+1}-c_i)}{\sum_{k=1}^{i}b_k-c_i},$$
  with $b_0=0$, $c_{s+1}=1$ (Eqs. (71), (81)–(82)); the $2s-1$ free parameters may be taken as
  the $b_i$ and $c_i$. A non-recursive form of the first formula (Eq. (80)) is stated without
  proof.
- **Special case $A^{\mathrm W}_i=-1$ ($i>1$).** Then $a_{ij}=b_j+(-1)^{i-j+1}b_i$ and
  $c_i=\sum_{j<i}b_j+\tfrac12\bigl(1+(-1)^i\bigr)b_i$, so the weights are the only free
  parameters; the abscissae come in equal pairs $c_2=c_3$, $c_4=c_5$, … (§6.1, Eqs. (90)–(91)),
  matching a recursive formula of Bernardini and Pirozzoli as recalled there.

**Williamson's conversion for zero weights, corrected.** Williamson's conversion from Butcher
to 2N coefficients is $A^{\mathrm W}_i=(b_{i-1}-B^{\mathrm W}_{i-1})/b_i$ when $b_i\ne0$ and, as
printed in Williamson (1980) and recalled by Bazavov, $A^{\mathrm W}_i=(a_{i+1,i-1}-c_i)/B^{\mathrm W}_i$
when $b_i=0$ (Eqs. (11)–(12)). Bazavov (2026, §5.1, Eqs. (69)–(70)) shows that the second
formula holds only for $i=2$ and that the correct form, valid for every $b_i$, is

$$A^{\mathrm W}_i=\frac{a_{i+1,i-1}-a_{i,i-1}}{B^{\mathrm W}_i},\qquad i\ne1;$$

the two agree only when $c_i=a_{i,i-1}$, which is automatic for $i=2$. His evidence is exact
counterexamples: a four-stage third-order 2N method with $b_3=0$ needs $A^{\mathrm W}_3=\tfrac{130}{81}$,
where Williamson's formula gives $\tfrac{38}{243}$, and a five-stage third-order one with $b_4=0$
needs $A^{\mathrm W}_4=-\tfrac{452}{729}$ against $-\tfrac{862}{729}$; the tableaux rebuilt from
Williamson's values violate the third-order conditions (Tables 1–4, with a Matlab script in
App. E). He says the formula has been copied in "multiple publications going back to 1980"
without naming them, and explains why the error went unnoticed: the Butcher-to-2N conversion is
rarely used, and $b_i=0$ for $i\ge3$ must be imposed deliberately (§5.1). Williamson (1980) is
not ingested in this bundle, so this is recorded as Bazavov's correction with his evidence, not
as a contradiction between bundle sources.

**Complete low-order families (§7–9).** With $c_2,c_3,c_4$ free, every four-stage third-order
2N method follows from one quadratic equation for $b_2$; every five-stage one, with
$c_2,\dots,c_5$ and $b_5$ free, also from a quadratic (the cubic coefficient vanishes
identically). Bazavov conjectures from a parameter count that third-order 2N methods with any
number of stages lead to a final equation of degree at most 3 (§8); *this is a heuristic, not a
proved statement*. A grid search found "over two million" rational five-stage third-order
methods (§9). Printed examples (Tables 5–10) include four (4,3) methods that also satisfy the
Carpenter–Kennedy condition $b^\top A^2c=\tfrac1{24}$, hence are fourth order on linear
problems and share the stability polynomial $\sum_{j\le4}z^j/j!$; and the five-stage method

$$c=\bigl(0,\tfrac14,\tfrac12,\tfrac34,1\bigr),\quad
A=\begin{pmatrix}0\\ \tfrac14&0\\ -\tfrac16&\tfrac23&0\\ \tfrac14&0&\tfrac12&0\\ 0&\tfrac25&\tfrac15&\tfrac25&0\end{pmatrix},\quad
b=\bigl(\tfrac19,\tfrac29,\tfrac13,\tfrac29,\tfrac19\bigr),$$

whose fifth stage is a second-order solution at $t_n+h$, so it carries an
[embedded](/methods/embedded-runge-kutta-pair.md) 3(2) pair at no extra cost (Table 10). On three
scalar test problems all new methods converge at third order, and the best (4,3) method is
"slightly better" than five Carpenter–Kennedy (4,3) schemes (§9, Figs. 1–2).

**Higher order.** Bazavov recommends designing 2N methods of order $\ge4$ by solving the
standard order conditions together with the quadratic constraints in the Butcher variables,
rather than in $(A^{\mathrm W}_i,B^{\mathrm W}_i)$, where the systems have high degree. He recomputes
the six-stage fourth-order 2N method of Berland, Bogey and Bailly to 42 digits this way, by
Newton iteration in 1000-bit arithmetic (§10, App. D).

**Lie-group motivation.** Bazavov's earlier numerical evidence suggests that Williamson 2N
methods become commutator-free Lie-group integrators of the same order when the update
$S_1\leftarrow S_1+B^{\mathrm W}_iS_2$ is replaced by a matrix exponential; this is proved only for
a three-stage third-order method and is *a hypothesis* for more stages and higher order (§1,
§10, recalling his 2021 paper).

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

Storage was an argument for SSP Runge–Kutta methods from the start.
[Shu & Osher (1988)](/sources/shu-1988.md) prefer one-step Runge–Kutta methods to multi-level
TVD time discretizations because the latter must store all levels (§II, p. 7), and they note
that their third-order method (SSPRK(3,3)) needs at stage $i$ only $f$ of the previous stage,
"so there is no need to store the previous $L(u^{(k)})$, lowering the storage requirement
significantly" (p. 12).
[Gottlieb et al. (2001)](/sources/gottlieb-2001.md) (§4.2, Eq. (4.4)) search the Williamson 2N
form above, with $B^{\mathrm W}_1$ as free parameter and closed-form expressions for
$A^{\mathrm W}_2,A^{\mathrm W}_3,B^{\mathrm W}_2,B^{\mathrm W}_3$ in terms of it, for
third-order SSP methods; the best one found, at $B^{\mathrm W}_1=0.924574$ (from Gottlieb–Shu),
has SSP coefficient 0.32, against 1 for SSPRK(3,3). They found no five-stage fourth-order
method of the Carpenter–Kennedy 2N classes with positive Shu–Osher coefficients, and state
that a low-storage method with negative $\beta_{ij}$ "cannot be made SSP", because the
downwind operator $\tilde L$ destroys the low-storage property.

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

## Many-stage and paired methods with two or three registers

Methods designed for large stability regions are built with low storage in mind.

- **Factorized many-stage methods.** [Doehring et al. (2024)](/sources/doehring-2024.md) write
  a stability polynomial of degree up to 128 as a product of linear factors and quadratic
  factors for complex-conjugate root pairs, and realize it as a sequence of forward Euler steps
  and two-stage submethods in modified Shu–Osher form, each submethod needing two registers;
  the abstract calls the result "2N storage" (§9, Eqs. (9.1)–(9.8)). See
  [optimal stability polynomials](/methods/optimal-stability-polynomial.md) and
  [internal stability](/definitions/internal-stability.md).
- **Paired explicit methods.** In the [P-ERK](/methods/paired-explicit-runge-kutta.md) tableaux
  only the first column and the first subdiagonal of $A$ are nonzero and only the last two
  weights; [Hedayati Nasab & Vermeire (2022)](/sources/hedayatinasab-2022.md) note that the
  third-order family then needs only three stage derivatives in memory, whatever $s$ (§3.1,
  Eqs. (19)–(21)), and [Doehring et al. (2025)](/sources/doehring-2025.md) that the second-,
  third- and fourth-order members need two stored stages and a constant cost per stage (§3.1,
  §3.2).

## Stage communication in asynchronous distributed solvers

In a domain-decomposed solver every stage of an explicit method needs current halo (ghost)
values from neighbouring processes, so a standard implementation of an $s$-stage Williamson
method performs $s$ halo exchanges with synchronization per step; over-decomposition, a halo
wide enough for all stages, avoids them at the price of larger messages and redundant work
([Goswami, Matthew & Aditya 2023](/sources/goswami-2023.md), §2.3, Fig. 2). Goswami et al.
couple Williamson 2N methods with **asynchrony-tolerant** finite differences, stencils that
use halo values delayed by a random number of time levels, so that the step needs no
communication between stages and, optionally, none at every step. In registry-compatible
notation the 2N recurrence above applies at every point; the methods are (Table 2):

| Method | $c_{i+1}$ (the source's $\delta_i$) | $A^{\mathrm W}_i$ | $B^{\mathrm W}_i$ |
|---|---|---|---|
| LSERK2 | $\tfrac12,1$ | $0,-\tfrac12$ | $\tfrac12,1$ |
| LSERK3a | $\tfrac14,\tfrac23,1$ | $0,-\tfrac{17}{32},-\tfrac{32}{27}$ | $\tfrac14,\tfrac89,\tfrac34$ |
| LSERK3b | $1,\tfrac13,1$ | $0,-4,\tfrac1{27}$ | $1,\tfrac29,\tfrac34$ |

*(Compiler check, not in the source: with the recursion above, LSERK2 is the explicit midpoint
rule; LSERK3a has $c=(0,\tfrac14,\tfrac23)$, $b=(\tfrac14,0,\tfrac34)$, $a_{31}=-\tfrac29$,
$a_{32}=\tfrac89$, and LSERK3b has $c=(0,1,\tfrac13)$, $b=(0,\tfrac14,\tfrac34)$,
$a_{31}=\tfrac19$, $a_{32}=\tfrac29$; both satisfy the four third-order conditions.)* The paper
does not name the origin of the two third-order methods.

**Naive coupling loses order.** Applying the delay-tolerant stencils at every stage while the
halo values stay at their delayed level degrades the result: at process-boundary points the
local truncation error of the second-order method with fourth-order differences has a leading
term $\tfrac5{32}\kappa h^3\Delta x^{-2}\,\partial_t^2u$ (Eq. (18); $\kappa$ the diffusivity and $u$
the PDE solution, page-local; the source writes $\nu$, the registry Courant number), which in a synchronous run would cancel between the stage
values on the two sides. The domain-averaged error then scales like $P\,\Delta x^3$ under strong
scaling with $P$ processes, and like $\Delta x^2$ under weak scaling, whatever the orders of the
spatial and temporal schemes (Eqs. (19)–(24)). The cause is that halo values are not advanced
between stages (§3.2). This is the communication analogue of the inconsistent intermediate
stage data treated on [Runge–Kutta stage boundary treatment](/methods/runge-kutta-stage-boundary-treatment.md).

**Accurate coupling.** The halo points are advanced by the same 2N recurrence, with
$hf$ at a halo point replaced by $h\,\partial_tu$ approximated by a one-sided **temporal**
stencil on the delayed history (Eqs. (25)–(27)). The stencil weights are not chosen to
approximate $\partial_tu$ at the stage, but to reproduce the low-order Taylor terms the stages
accumulate: the stage derivative is expanded as
$\partial_tu^{(e)}=\sum_{j=0}^e\gamma^e_jh^j\partial_t^{j+1}u$ with $\gamma^e_j$ built from the 2N
coefficients ($\gamma^e_0=1$, $\gamma^e_e=B^{\mathrm W}_1\cdots B^{\mathrm W}_e$; page-local
$\gamma^e_j$), and the weights solve a small linear system (Eqs. (28)–(32)). For LSERK2 and a
delay of $\tilde k$ levels (page-local $\tilde k$)

$$\partial_tu^{(0)}\approx\frac{2\tilde k+3}{2h}u^{n-\tilde k}-\frac{2(\tilde k+1)}{h}u^{n-\tilde k-1}+\frac{2\tilde k+1}{2h}u^{n-\tilde k-2}$$

(Eq. (34)), the BDF2 derivative formula when $\tilde k=0$; four-point formulas for LSERK3a and
LSERK3b are Eqs. (36)–(37). Only levels $0,\dots,s-2$ are needed, and the halo value at the start of the
step comes from an $\mathcal O(h^2)$ polynomial extrapolation (§3.3). The predicted orders, fourth with fourth-order
differences and sixth with sixth-order ones under $h\sim\Delta x^2$, are observed on 1D linear
advection–diffusion (slopes $-4$ and $-6$, against $-3$ asymptotically for the naive coupling),
with an asynchrony error growing linearly in $P$ (Eq. (43), Figs. 5–6). On 3D Burgers turbulence
the communication-avoiding variant is up to 4.81 (second-order method) and 6.68 times
(third-order method) faster than the synchronous code on 27,000 cores, and about 2 times in
weak scaling (Figs. 8, 10). The larger gain of the three-stage method is attributed to the
inter-stage communications it avoids (§5.2). Earlier asynchronous solvers of the same group used
Adams–Bashforth schemes, which the authors say have "poor stability, resulting in a strict CFL
condition" (§1); no stability comparison is shown.

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

Later studies agree. [Ranocha et al. (2025)](/sources/ranocha-2025.md) use SSP3(2)4[3S\*$_+$],
RDPK3(2)5F[3S\*$_+$] and RDPK4(3)9F[3S\*$_+$] up to $7.68\times10^8$ degrees of freedom and find
the SSP pair usually the most efficient for lower-Mach and positivity-critical problems (§2.5,
§8). [Al Jahdali et al. (2022)](/sources/aljahdali-2022.md) find the error-controlled 3S\*$_+$
pairs, like BS3(2), much cheaper than a CFL-controlled third-order method (4250 against 7135
evaluations on the Imperial Front Wing; §3, Table 4). Doehring et al. (2025, §6) compare their
fourth-order paired methods with the 2N method CK4(3)5 of Carpenter and Kennedy, the 14-stage
method of Niegemann, Diehl and Busch, the three-register 18-stage method of Parsani, Ketcheson
and Deconinck, and others from OrdinaryDiffEq.jl; the classical RK4, not implemented in
low-storage form there, is "disproportionally slow" in their memory-bound code.

## Qualifications

- Ranocha et al. print the embedded-solution line of their Algorithm 1 (3S\*) as
  $(S_2+\delta_sS_1+\delta_{s+1}S_3)/\sum_{i=1}^{s+1}\delta_i$. Every coefficient table lists only
  $\delta_1,\dots,\delta_s$, with $\delta_s=0$, and the loop already adds $\delta_sS_1$. The
  printed line is therefore inconsistent with the tables. The new methods use Algorithm 2,
  which is unaffected.
- **Goswami et al. (2023), scope of the buffer derivation.** The expansion of stage
  derivatives in pure time derivatives $\partial_t^{j+1}u$ is exact for linear autonomous
  problems, the setting of their analysis. For nonlinear $f$ the stage derivative
  $f(u^{(1)})=f+B^{\mathrm W}_1hf'f+\tfrac12(B^{\mathrm W}_1h)^2f''(f,f)+\dots$ carries elementary
  differentials that the expansion does not contain *(compiler check, not in the source)*; the
  Burgers experiments check agreement with the synchronous solution, not the order.
- **Printed slips in Goswami et al. (2023).** The matrix of Eq. (35) prints the fourth column
  with $\tilde k+2$, which duplicates the third column and makes the system singular; with
  $\tilde k+3$ its solutions are exactly the printed Eqs. (36)–(37) *(compiler check, not in the
  source)*. Algorithms 1–3 omit the factor $h$ in the stage and halo updates that Eqs. (9),
  (25)–(26) contain.
- **"Asynchronous"** in Goswami et al. means delayed halo data between processes at a common
  step, not the cell-wise local steps of asynchronous
  [local time stepping](/methods/local-time-stepping.md).
- The tag F (FSAL) and the stage count in method names follow the effective-evaluation convention
  described on the [embedded-pair page](/methods/embedded-runge-kutta-pair.md).
- **Terminology.** "2N" in the Ketcheson classes of Ranocha et al. (2022) is a register-update
  class, while Bazavov (2026) restricts it to Williamson's form with all $A^{\mathrm W}_i\neq0$
  ($i\ge2$). Statements about "2N methods" carry over between the two only within Bazavov's
  class.
- Bazavov (2026) was read as the arXiv v1 preprint. The Source page records printed slips
  found by exact recomputation: one term of the linear coefficient of the (4,3) quadratic
  (Eq. (95)) has the wrong sign (with the printed sign the four printed (4,3) schemes leave
  nonzero residuals, with the corrected one zero); Table 8 prints $a_{51}=\tfrac{12053}{11172}$ for $\tfrac{2053}{11172}$;
  Table 9 prints $A^{\mathrm W}_5=-\tfrac8{25}$ for $-\tfrac{261}{625}$; Eq. (46) has an index $j$ that
  must be $i-1$ (as recorded on the Source page). The theorems and the printed tableaux of
  Tables 5–7 and 10 are unaffected.
- Doehring et al. (2024) do not detail the register count of their two-stage submethods beyond
  the "2N storage" of the abstract, and print the first submethod stage without the factor $h$
  (Eq. (9.6a)).

# Citations

- [Ranocha et al. (2022)](/sources/ranocha-2022.md) — §2.1 (Algorithms 1–2), Remark 3.1, §5, §5.5.4 (Fig. 5), §6.2, §7, Appendix A (Eqs. (A.1)–(A.2)), Appendix B (Tables 12–17), Suppl. Table 1.
- [Fekete et al. (2022)](/sources/fekete-2022.md) — §2.3 (SSPRK(10,4) low-storage implementation).
- [Shu & Osher (1988)](/sources/shu-1988.md) — §II, pp. 7, 12 (storage of multi-level versus Runge–Kutta methods; Eq. (2.18)); read as ICASE Report 87-33.
- [Gottlieb et al. (2001)](/sources/gottlieb-2001.md) — §4.2 (Eq. (4.4), third-order 2N SSP method, no five-stage fourth-order SSP member found).
- [Bazavov (2026)](/sources/bazavov-2026.md) — §2 (Eqs. (7)–(14), Remark 2), §3–4 (Eqs. (23)–(29), Theorems 1–2, Eqs. (42)–(47), Remark 3), §5 (Theorem 3, Eqs. (59)–(63)), §5.1 (Eqs. (69)–(70), Tables 1–4), §6 (Theorems 4–5, Eqs. (71), (80)–(82)), §6.1, §7–9 (Tables 5–10, Figs. 1–2), §10, App. D–E; arXiv v1.
- [Doehring et al. (2024)](/sources/doehring-2024.md) — abstract, §9 (Eqs. (9.1)–(9.8)).
- [Hedayati Nasab & Vermeire (2022)](/sources/hedayatinasab-2022.md) — §3.1 (Eqs. (19)–(21)).
- [Doehring et al. (2025)](/sources/doehring-2025.md) — §3.1–3.2, §6 (comparison methods).
- [Ranocha et al. (2025)](/sources/ranocha-2025.md) — §2.5, §8.
- [Al Jahdali et al. (2022)](/sources/aljahdali-2022.md) — §2.1, §3 (Table 4).
- [Goswami, Matthew & Aditya (2023)](/sources/goswami-2023.md) — §1, §2.3 (Eqs. (8)–(10), Table 2, Fig. 2), §3.1 (Eqs. (11)–(24)), §3.2–3.4 (Eqs. (25)–(43), Table 3), §4 (Algorithms 1–3), §5 (Figs. 5–11).
