---
type: Benchmark
title: "Prothero–Robinson problem"
description: "The scalar stiff test problem $y'=\\lambda(y-g(t))+g'(t)$, whose smooth exact solution $g$ is independent of the stiffness $\\lambda$; it isolates the stiff-regime error of a one-step method, exposes order reduction through the stage-order residuals, and grounds weak stage order and Scholz's Rosenbrock conditions. Includes the multirate Kværnø–Prothero–Robinson variant."
status: established
aliases: [Prothero–Robinson test equation, PR problem, Kværnø–Prothero–Robinson problem, KPR problem]
tags: [stiff, order-reduction, verification, runge-kutta, parallel]
timestamp: 2026-10-20T08:00:00Z
---

# Prothero–Robinson problem

The **Prothero–Robinson problem** is

$$y'=\lambda\big(y-g(t)\big)+g'(t),\qquad y(t_0)=g(t_0),\qquad \operatorname{Re}\lambda\le0,$$

with $g$ a smooth given function (page-local). Its exact solution is $y=g$ for every
$\lambda$, while any perturbation decays like $e^{\lambda t}$; making $|\lambda|$
large stiffens the problem without changing the solution. A method's error on it
therefore measures how its stages handle a smooth forcing under stiffness, which is
exactly where [order reduction](/definitions/order-reduction.md) arises
([Biswas et al. 2023](/sources/biswas-2023.md), Eq. (5), §2;
[Biswas et al. 2024](/sources/biswas-2024.md), Eq. (8), §2.2;
[Steinebach 2023](/sources/steinebach-2023.md), Eq. (1.4)). With $z=h\lambda$, the
stiff regime is $|z|\gg1$ with $h$ small relative to the scale of $g$.

## Runge–Kutta error analysis

Inserting the exact solution into the stages of a
[Runge–Kutta method](/definitions/runge-kutta-method.md) leaves stage defects
proportional to the stage-order residuals $\tau^{(k)}=Ac^{k-1}-c^k/k$,

$$\sum_{k\ge1}\frac{h^k}{(k-1)!}\,\tau^{(k)}\,g^{(k)}(t_n),$$

and a step defect with coefficients $b^\top c^{k-1}-\frac1k$. The global error
$e_n=y_n-g(t_n)$ obeys

$$e_{n+1}=R(z)\,e_n+z\,b^\top(I-zA)^{-1}\Big(\sum_{k\ge1}\frac{h^k}{(k-1)!}\tau^{(k)}g^{(k)}(t_n)\Big)+\sum_{k\ge1}\frac{h^k}{(k-1)!}\Big(b^\top c^{k-1}-\frac1k\Big)g^{(k)}(t_n)$$

(Biswas et al. 2023, Eqs. (6)–(8), after Prothero–Robinson, Hairer–Wanner and
Burrage et al.). Biswas et al. (2024, Eq. (9)) write the same local error as
$-\sum_k\frac{h^k}{(k-1)!}W_k(z)g^{(k)}(t_n)+\mathcal O(h^{p+1})$ with the
page-local $W_k(z)=z\,b^\top(I-zA)^{-1}\tau^{(k)}$; the two papers define the
defect with opposite signs. The middle term is the order-reducing one: for small
$|z|$ its Neumann series contains $b^\top A^j\tau^{(k)}$, which the order
conditions control, but for $z\to-\infty$ it contains negative powers of $A$
(Biswas et al. 2023, §2). With invertible $A$,
$z(I-zA)^{-1}=-A^{-1}-z^{-1}A^{-2}-\dots$, so
$W_k(z)\to-b^\top A^{-1}\tau^{(k)}$ *(compiler check, not in the sources)*.

Two consequences:

- [Weak stage order](/definitions/weak-stage-order.md) $q_{\mathrm w}$ makes
  $W_k\equiv0$ for $k\le q_{\mathrm w}$, so the local error is
  $\mathcal O(h^{q_{\mathrm w}+1})$ uniformly in $z$; it is the least restrictive
  condition that does so (Biswas et al. 2024, §2.2), and its conditions are
  necessary for any Runge–Kutta method to avoid order reduction on this problem
  (§2.3).
- Biswas et al. (2024, §2.3) recall Montijano's necessary condition
  $b^\top A^{-1}c^j=1$, $0\le j\le r$, for order-$r$ convergence. Under the
  quadrature conditions $b^\top c^{k-1}=1/k$ one has
  $b^\top A^{-1}\tau^{(k)}=\frac1k\big(1-b^\top A^{-1}c^k\big)$, so Montijano's condition
  for $j=k\ge1$ is the vanishing of the stiff limits of $W_k$ *(compiler check)*.

## Rosenbrock error analysis

For a [Rosenbrock–Wanner method](/methods/rosenbrock-wanner-method.md) with diagonal
coefficient $\gamma$, Scholz expressed the Prothero–Robinson error through two
polynomials in $H=z/(1-\gamma z)$ (page-local), $C_2(H)$ and $C_3(H)$, whose
coefficients are elementary-weight-type sums of the method's coefficients; requiring
all of them to vanish (conditions No. 48 and 49 of Steinebach's table) is the
Rosenbrock analogue of weak stage order, and Ostermann and Roche obtained the same
conditions for semi-discretized parabolic problems (Steinebach 2023, §2, Eqs.
(2.5)–(2.13)). The stability function itself is a polynomial in $H$ (Eq. (2.14)).
Steinebach states, citing his own earlier work and Rang, that Scholz's estimate of
the error constant is not sharp: for L-stable methods it behaves like $C_1/z$, so
results are asymptotically exact as $|\lambda|\to\infty$ at fixed $h$, but at fixed
large $|\lambda|$ only order $p-1$ is observed. This is why Rodas4P and Rodas4P2,
which satisfy both conditions, show order 3, while Rodas4PR2 reaches 4 (§2, Table 6).

## Instances in the sources

| source | form | data | purpose |
|---|---|---|---|
| Biswas et al. 2023, §6.1 | $y'=\lambda(y-g)+g'$ | $\lambda=-10^4$, $g(t)=e^{-t}\sin(10t)+\cos(20t)$, $t\in[0,10]$ | order of DIRK schemes with high weak stage order |
| Steinebach 2023, §4 problem 2 | $y'=-\lambda(y-g)+g'$ | $\lambda=10^5$, $g(t)=10-(10+t)e^{-t}$, $t\in[0,2]$, $h=0.25,\dots,0.03125$; also a scan $\lambda\in[1,10^5]$ | order of the Rodas family |
| Biswas et al. 2024, §2.2 | $y'=\lambda(y-g)+g'$ | analytic only | motivation of weak stage order |
| [Chinomona and Reynolds 2021](/sources/chinomona-2021.md), §5.1 | two-component multirate Kværnø–Prothero–Robinson problem | see below | convergence of multirate methods |
| [Fish & Reynolds 2023](/sources/fish-2023.md), §4.1.4 | same KPR problem and partition | as Chinomona and Reynolds | one of seven tuning problems for multirate step-size controllers |
| [Fish et al. 2024](/sources/fish-2024.md), §6.1 | same KPR problem, IMEX three-way partition | as Chinomona and Reynolds, fast step $H/10$ | convergence of IMEX-MRI-SR and MERK methods, nonlinear fast part |
| [Čaklović et al. 2025](/sources/caklovic-2025.md), §4.3, Eq. (4.3) | $y'=(y-g)/\varepsilon+g'$ | $\varepsilon=10^{-3}$ ($\lambda=-10^3$), $g(t)=\cos t$, final time not printed; Newton tolerance $10^{-12}$ | efficiency of diagonal (parallel) SDC against serial SDC |

Steinebach's §4 writes $-\lambda$ with $\lambda>0$, his Eq. (1.4) $+\lambda$ with
$\operatorname{Re}\lambda\ll0$; the problems coincide after $\lambda\mapsto-\lambda$.

**Results.**

- Biswas et al. (2023, Fig. 2): the $q_{\mathrm w}=1$ references DIRK-(5,4,1) and
  DIRK-(5,5,1) converge at order about 1 for large $h$ (stiff regime) and at order
  $p$ for small $h$; DIRK-(7,4,4) and DIRK-(12,5,5) converge at order $p$ throughout
  ([DIRK schemes with high weak stage order](/methods/dirk-high-weak-stage-order.md)).
- Steinebach (2023, Table 6), orders over successive halvings: [Rodas5P](/methods/rodas5p.md)
  3.1/3.0/3.0 (embedded the same), Rodas5 1.3/1.2/1.1, Rodas4 $-3.4$/0.5/0.8,
  Rodas4PR2 about 4, Rodas4P2 about 3. In the $\lambda$ scan only Ros3prl2 converges
  independently of $\lambda$; Rodas4PR2 drops to order 3 in mildly stiff regimes.
- Čaklović et al. (2025, §4.3, Figs. 14–15), with 4 Radau IIA nodes and $K=4$ sweeps: every
  [diagonal SDC](/methods/parallel-sdc.md) variant shows an error plateau over a range of step
  sizes, which the authors attribute to order reduction, citing Weiser. Under their cost model
  (parallel cost divided by $4\times0.8$), MIN-SR-S is more efficient than serial LU-SDC down to an
  error of about $10^{-6}$ and LU-SDC below; with $K=6$ sweeps the crossover moves to about
  $10^{-8}$, so more sweeps lower the plateau. The comparison is modelled, not timed.

## Multirate variant (Kværnø–Prothero–Robinson)

Chinomona and Reynolds (2021, §5.1), adapting Sandu, use

$$\begin{pmatrix}u\\v\end{pmatrix}'=\Lambda\begin{pmatrix}\dfrac{-3+u^2-\cos(20t)}{2u}\\\dfrac{-2+v^2-\cos t}{2v}\end{pmatrix}-\begin{pmatrix}\dfrac{20\sin(20t)}{2u}\\\dfrac{\sin t}{2v}\end{pmatrix},\qquad t\in[0,\tfrac{5\pi}2],$$

with $u$, $v$ and the $2\times2$ coupling matrix $\Lambda$ page-local, $u(0)=2$, $v(0)=\sqrt3$ and exact solution $u=\sqrt{3+\cos(20t)}$,
$v=\sqrt{2+\cos t}$; $u$ is fast, $v$ slow. The coupling matrix has diagonal
$(-10,-1)$ and off-diagonal entries $(1-\epsilon_{\mathrm c})(-10+1)$ and
$-\epsilon_{\mathrm c}(-10+1)$ with $\epsilon_{\mathrm c}=0.1$ (page-local), i.e.
$\Lambda=\begin{pmatrix}-10&-8.1\\0.9&-1\end{pmatrix}$ *(compiler arithmetic from the
printed parameters)*. The problem is nonlinear and non-autonomous, with a known
solution, and does not by itself require an implicit slow scale. With macro step
$H=\pi/2^k$ and fast step $H/20$, least-squares rates are: Lie–Trotter 0.99,
Strang–Marchuk 1.98, IMEX-MRI-GARK3a 3.10, IMEX-MRI-GARK3b 3.14, MRI-GARK-ESDIRK34a
3.06, IMEX-MRI-GARK4 4.15, MRI-GARK-ESDIRK46a 3.93 (Fig. 2); see
[IMEX multirate infinitesimal GARK methods](/methods/imex-mri-gark.md).

Fish et al. (2024, §6.1, eqs. 6.1–6.3, Fig. 5) reuse the problem and the partition (implicit
slow part the second row of $\Lambda$ times the nonlinear vector, fast part the first row, the
forcing explicit) with $H=\pi/2^k$ and fast step $H/10$. The fast partition is nonlinear in
$u$, which makes the problem a test of order for nonlinear fast parts. Rates: IMEX-MRI-SR2(1)
2.01, SR3(2) 3.11, SR4(3) 3.85; MERK2–5 2.06, 3.17, 4.25, 5.32; IMEX-MRI-GARK3a/3b/4 3.05, 3.09,
4.11; Lie–Trotter 1.01, Strang–Marchuk 1.98 ([IMEX-MRI-SR](/methods/imex-mri-sr.md),
[multirate exponential methods](/methods/multirate-exponential-methods.md)). Fish & Reynolds
(2023, §4.1.4) use the same problem, with the component partition of Chinomona and Reynolds and
Sandu, to tune their multirate controllers ([step-size control](/methods/step-size-control.md)).

## Qualifications

- Chinomona and Reynolds print the explicit slow part of their splitting as
  $(0,\ +\sin t/(2v))$; the problem statement and $v'=-\sin t/(2v)$ require a minus
  sign (slip in the arXiv version read). Fish et al. (2024, eq. 6.3), who copy the partition,
  print the same plus sign; in addition the $-20\sin(20t)/(2u)$ forcing appears in none of
  their three parts, and both (6.1) and (6.3) print the second numerator as $-2+u^2-\cos t$
  where the exact solution requires $-2+v^2-\cos t$ (checked visually by the reader). Their
  measured design orders indicate that the code uses the correct problem *(compiler
  inference)*.
- The Prothero–Robinson analysis is linear in $y$; the guarantees it yields for weak
  stage order or Scholz's conditions do not extend to nonlinear stiff problems such
  as Van der Pol, where Biswas et al. (2023, §7.3) still observe order reduction.

# Citations

- [Biswas et al. (2023)](/sources/biswas-2023.md) — §2 Eqs. (5)–(14); §6.1 Fig. 2; §7.3.
- [Biswas et al. (2024)](/sources/biswas-2024.md) — §2.2 Eqs. (8)–(9); §2.3.
- [Steinebach (2023)](/sources/steinebach-2023.md) — Eq. (1.4); §2 Eqs. (2.5)–(2.14); §4 problem 2, Table 6.
- [Chinomona and Reynolds (2021)](/sources/chinomona-2021.md) — §5.1, Fig. 2.
- [Fish & Reynolds (2023)](/sources/fish-2023.md) — §4.1.4.
- [Fish et al. (2024)](/sources/fish-2024.md) — §6.1 (eqs. 6.1–6.3, Fig. 5).
- [Čaklović et al. (2025)](/sources/caklovic-2025.md) — arXiv v2: §4.1, §4.3 (Eq. (4.3), Figs. 14–15).
