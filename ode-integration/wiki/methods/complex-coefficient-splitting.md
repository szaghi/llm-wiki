---
type: Method
title: "Splitting and composition with complex coefficients"
description: "Splitting and composition methods with complex coefficients of positive real part escape the negative-coefficient barrier and keep their classical order on parabolic problems generating analytic semigroups, up to order barriers of their own; symmetric-conjugate methods nearly preserve unitarity, and projection onto the real part raises odd orders by one."
status: established
aliases: [complex splitting, complex composition, symmetric-conjugate splitting, complex triple jump, complex Lie–Trotter, CLT, Strang-CLT]
tags: [splitting, order-conditions, stability, geometric-integration]
timestamp: 2026-10-20T16:00:00Z
---

# Splitting and composition with complex coefficients

Allowing the coefficients $a_j,b_j$ of a [splitting method](/methods/operator-splitting.md),
or the weights $\gamma_j$ of a [composition](/methods/composition-methods.md), to be complex
removes the [negative-coefficient barrier](/results/negative-coefficient-barrier.md): the
real-number obstruction $\sum\gamma_j^3=0\Rightarrow\exists\gamma_j<0$ disappears, and
order $\ge3$ is reached with every coefficient in the right half-plane $\operatorname{Re}>0$
([Blanes et al. 2024](/sources/blanes-2024.md), §7). The sub-flows then have to be defined
for complex times, which is natural when each part is linear and generates an analytic
semigroup (diffusion, imaginary-time Schrödinger propagation) or is solved exactly in
Fourier space.

## Parabolic problems

For $y'=(L_1+L_2)y$ (page-local $L_i$) with $L_1$, $L_2$ and $L_1+L_2$ generating analytic
semigroups on a sector $\Sigma_\theta=\{\lvert\arg t\rvert<\theta\}$ (page-local
$\theta$), a splitting of classical order $p$ with all $a_j,b_j\in\Sigma_\theta$ converges
with order $p$ (Blanes et al. 2024, §6.4, Eq. 6.47, as recalled from Hansen & Ostermann
2009 and Castella et al. 2009). For real problems one projects each step,
$y_n=\operatorname{Re}\,\psi_h(y_{n-1})$, and the order is retained. This is the escape
from the order-2 cap that real positive coefficients impose on splittings of diffusion.
Imaginary-time propagation of the Schrödinger equation (Eqs. 6.45–6.46, as recalled from
Bader et al. 2013) is the motivating example.

## Order barriers with positive real part

Complex coefficients have barriers of their own when every coefficient must have
$\operatorname{Re}>0$ (§7.1, as recalled from Blanes et al. 2013 and Hansen & Ostermann
2009):

| Construction | Maximal order with $\operatorname{Re}>0$ |
|---|---|
| iterated compositions of a first-order method | 3 |
| Strang-based recursive two-stage compositions | 6 |
| triple-jump palindromic compositions | 8 |
| quadruple-jump compositions | 14 |

## Named schemes

With $\chi_h$ Lie–Trotter (first order) or a symmetric second-order map (Strang), Blanes et
al. record (§7.1, §6.4):

- **order 2 from Lie–Trotter:** two steps with $\gamma=\tfrac12\pm\tfrac i2$ (see the
  $N$-part section below for its uniqueness);
- **order 3 from Strang** (Eq. 7.4): $\gamma_1=\tfrac12\pm i\tfrac{\sqrt3}6$, $\gamma_2=\bar\gamma_1$;
- **smallest-phase recursion** (Eq. 7.6): two-stage recursive compositions whose level-$p$ weight is $\gamma_{p,1}=\tfrac12\pm\tfrac i2\tan\frac{\pi}{2(p+1)}$ (Blanes et al.'s index $r$);
- **complex triple jump** (Eq. 7.8): $\gamma_1=\gamma_3=1/(2-2^{1/3}e^{\pm2i\pi/3})$, $\gamma_2=1-2\gamma_1$ (the sign selects one of the two complex cube roots of 2; the source writes $e^{2i\ell\pi/3}$);
- **symmetric-conjugate order 4** (Eq. 7.9): $\gamma_1=\bar\gamma_3=\tfrac14\pm\tfrac i4\sqrt{5/3}$, $\gamma_2=\tfrac12$.

Their splitting forms are Eqs. (7.10)–(7.12). For the fourth-order compositions (7.8) and
(7.9), the leading error coefficient $\lvert\sum_j\gamma_j^5\rvert$ is about **200 times
smaller** than that of the real triple jump (§7.1, as recalled from Blanes et al. 2022).

## Complex Lie–Trotter for $N$ parts

For $f=\sum_{\ell=1}^Nf^{[\ell]}$ with $N\ge3$ parts (page-local $N$),
[Spiteri & Wei (2026)](/sources/spiteri-2026.md) (§3.3, Case 2, Eqs. (23)–(26), Table 4) show
that the only second-order method with $2N$ non-trivial sub-integrations whose second sweep
again covers all parts is the **complex Lie–Trotter (CLT)** method
$\psi_h=\chi_{\gamma_2h}\circ\chi_{\gamma_1h}$, with $\chi_h$ the $N$-split Lie–Trotter map and

$$\gamma_1+\gamma_2=1,\qquad\gamma_1\gamma_2=\tfrac12,\qquad\gamma_{1,2}=\tfrac12\pm\tfrac i2,$$

together with its conjugate. This is the order-2 composition of Lie–Trotter listed above, here
derived from the $N$-split order conditions and shown to be unique within its class; the
$N=3$ case appeared in Auzinger, Koch & Thalhammer, as recalled (Remark 3.3). For $N\ge4$ the
hybrids **Strang-CLT$_{\ell^*}$** run Strang half steps on parts $1,\dots,\ell^*-1$ around a
CLT step of the remaining parts ($1<\ell^*<N-1$; Eq. (27), Table 7). Every complex fraction has
real part $\tfrac12$, which the authors call "favorable stability properties" (abstract); the
experiments do not test stability. The full enumeration is on
[operator splitting](/methods/operator-splitting.md).

**Cost of complex arithmetic.** With Heun's method for every sub-flow, CLT and Strang-CLT reach
order 2 on all test problems, but on the two real problems (a 5-split rotation–diffusion problem
and a 4-split advection–diffusion–reaction problem) they are the least efficient in wall-clock
time because complex arithmetic costs more than real (§4.1–4.2, Figs. 2–5, §5). Their errors
are about two thirds of Strang's on the first problem and about twice Strang's on the second
(Figs. 2 and 4, read from the plots). For a genuinely complex nonlinear PDE, solving in complex
arithmetic was cheaper than solving the real system of twice the size, for every method
(§4.3, Fig. 7). The hardware is not stated, and the conclusion is tied to Heun sub-integrators.

## Symmetric-conjugate methods

A method is **symmetric-conjugate** if its coefficients satisfy
$a_{s+2-j}=\bar a_j$, $b_{s+1-j}=\bar b_j$ (Eqs. 7.14–7.15), in contrast with palindromic
complex methods ($a_{s+2-j}=a_j$). For problems reversible under complex conjugation it
satisfies $\bar\psi_h=\psi_h^{-1}$. Applied to $iu'=(H_1+H_2)u$ with real $H_i$ and simple
real eigenvalues, it is similar to a unitary map for small $h$, so norm and energy are
nearly preserved over long times; palindromic complex methods lack this, and their
unitarity error grows (§7.2, as recalled from Bernier et al. 2023; Fig. 7.1 on a two-level
system up to $t=1000$). For Schrödinger equations Blanes et al. recommend
$0<a_j<1$ and $b_j$ with positive real part (§7.2).

## Projection on the real axis

For real problems, $R_h=\tfrac12(\psi_h+\bar\psi_h)$ raises the order from $p$ to $p+1$
when $\psi_h$ is symmetric-conjugate and $p$ is odd. A five-stage symmetric-conjugate
composition of Strang maps thus gives a sixth-order $R_h$ (palindromic methods need seven
stages), and nine stages give order 8 (palindromic: fifteen). Time-symmetry and
symplecticity of $R_h$ hold up to order $4k-1$ for odd $p=2k-1$, $4k+3$ for
symmetric-conjugate $p=2k$, and $4k+1$ for palindromic $p=2k$ (§7.3, as recalled from
Blanes et al. 2022 and Chambers 2003).

## Qualifications

- Blanes et al. print $b_1=\tfrac12\pm i\tfrac{\sqrt3}2$ in the splitting form (7.10) of the
  third-order method; consistency with (7.4) ($b_1=\gamma_1=\tfrac12\pm i\tfrac{\sqrt3}6$)
  and with $\gamma_1^3+\bar\gamma_1^3=0$ requires $\tfrac{\sqrt3}6$. In (7.8) they print
  $\gamma_2=1-2\alpha_1$ for $1-2\gamma_1$, and (7.6) mixes the indices $k$ and $r$
  (printed slips, p. 107–108).
- The convergence result (6.47) needs all three operators to generate analytic semigroups
  on the sector containing the coefficients; problems without that structure are outside
  its hypotheses.

# Citations

- [Blanes et al. (2024)](/sources/blanes-2024.md) — §6.4 (Eqs. 6.44–6.47, imaginary-time propagation, Fig. 6.1), §7.1 (barriers, Eqs. 7.4–7.12, error-coefficient comparison), §7.2 (symmetric-conjugate methods, Eqs. 7.14–7.15, Fig. 7.1), §7.3 (projection on the real axis).
- [Spiteri & Wei (2026)](/sources/spiteri-2026.md) — abstract, §3.3 (Case 2, Eqs. (23)–(27), Tables 4 and 7, Remark 3.3), §4.1–4.3 (Figs. 2–7), §5.
