---
type: Method
title: "IMEX multirate infinitesimal stage-restart (IMEX-MRI-SR) methods"
description: "IMEX-MRI-SR methods restart every fast sub-problem at the start of the macro step and follow it by a diagonally implicit slow solve; the page gives the scheme, its GARK form, internal-consistency and third- and fourth-order conditions, the n_Omega ≥ 2 barrier, linear stability, the embedded methods SR2(1), SR3(2), SR4(3), and MERK as a special case."
status: established
aliases: [IMEX-MRI-SR, MRI-SR, multirate infinitesimal stage-restart, IMEX-MRI-SR2(1), IMEX-MRI-SR3(2), IMEX-MRI-SR4(3)]
tags: [multirate, imex, runge-kutta, order-conditions, stability, step-size-control]
timestamp: 2026-10-20T05:00:00Z
---

# IMEX multirate infinitesimal stage-restart (IMEX-MRI-SR) methods

IMEX-MRI-SR methods, introduced by [Fish et al. (2024)](/sources/fish-2024.md),
integrate the same three-way additive problem as
[IMEX-MRI-GARK](/methods/imex-mri-gark.md),

$$y'=f^{\{\mathrm f\}}(t,y)+f^{\mathrm I}(t,y)+f^{\mathrm E}(t,y),$$

with a fast partition $f^{\{\mathrm f\}}$ treated
[infinitesimally](/methods/multirate-infinitesimal-methods.md) and a slow
partition split into a stiff part $f^{\mathrm I}$ (implicit) and a nonstiff part
$f^{\mathrm E}$ (explicit). Their defining feature is the **stage restart**: every
slow stage solves its modified fast problem from $y_n$ over $[0,c_iH]$, instead of
from the previous stage over $[c_{i-1}H,c_iH]$, and then applies one diagonally
implicit slow correction. The restart removes the sorted-abscissae requirement of
IMEX-MRI-GARK, simplifies the order conditions and makes embedded methods
possible (Fish et al. 2024, Def. 1.1, §1.1, §7).

## Why restart

All implicit MRI-GARK and IMEX-MRI-GARK methods need non-decreasing slow
abscissae, which few Runge–Kutta methods of order above two have, so the base
methods must be "padded" with extra stages by trial and error; according to Fish
et al. (2024, §1.1) "no authors have successfully created IMEX-MRI-GARK methods
with embeddings". Restarting each fast problem at $t_n$ frees the abscissae: the
methods below have non-monotone $c$, and IMEX-MRI-SR3(2) has $c_4=17/15>1$.

## The scheme (Fish et al. 2024, Def. 1.1, eqs. 1.5–1.6)

The coefficients are $n_\Omega$ strictly lower-triangular matrices
$\Omega^{(k)}$, $k=0,\dots,n_\Omega-1$, a lower-triangular matrix $\Gamma$ (one
matrix, no polynomial dependence), and abscissae $c$; first rows vanish
(registry symbols $\Omega^{(k)}$, $\Gamma$; the source writes $\Omega^{\{k\}}$ and
$c^{\{S\}}$). With $\omega_{ij}(\vartheta)=\sum_k\omega^{(k)}_{ij}\vartheta^k$ ($\vartheta\in[0,1]$ normalized inner time, page-local),
$\bar\Omega=\sum_k\Omega^{(k)}/(k+1)$, and
$f^{\mathrm I}_j=f^{\mathrm I}(t_n+c_jH,Y_j)$, $f^{\mathrm E}_j$ likewise, one macro
step reads

$$\begin{aligned}
&Y_1=y_n;\qquad\text{for }i=2,\dots,s:\\
&\quad v_i(0)=y_n,\qquad v_i'(\theta)=f^{\{\mathrm f\}}\big(t_n+\theta,v_i(\theta)\big)+\frac1{c_i}\sum_{j=1}^{i-1}\omega_{ij}\Big(\frac{\theta}{c_iH}\Big)\big(f^{\mathrm E}_j+f^{\mathrm I}_j\big),\qquad\theta\in[0,c_iH],\\
&\quad Y_i=v_i(c_iH)+H\sum_{j=1}^{i}\gamma_{ij}f^{\mathrm I}_j;\\
&y_{n+1}=Y_s.
\end{aligned}$$

Here $\theta$ and $v_i$ are page-local inner time and inner solution. Each stage is
"a fast evolution followed by an implicit solve", diagonally implicit in
$f^{\mathrm I}$ through $\gamma_{ii}$. Both slow parts share the explicit forcing
polynomial; only $f^{\mathrm I}$ enters the implicit correction.

**Embedding** (eq. 1.5d). One extra fast solve from $y_n$ over $[0,H]$ with forcing
$\sum_{j<s}\hat\omega_j(\theta/H)(f^{\mathrm E}_j+f^{\mathrm I}_j)$ gives $\hat v(H)$, and
$\hat y_{n+1}=\hat v(H)+H\sum_{j<s}\hat\gamma_jf^{\mathrm I}_j+H\hat\gamma_sf^{\mathrm I}(t_n+H,\hat y_{n+1})$.
All three methods below have $\hat\gamma_s=0$: the embedding costs no extra implicit
solve.

**Slow base method** (§2.1). With $f^{\{\mathrm f\}}\equiv0$ the method reduces to a
stiffly accurate [IMEX Runge–Kutta](/methods/imex-runge-kutta.md) method with
explicit table $(\bar\Omega,e_s^\top\bar\Omega,\bar\Omega\mathbf 1)$ and implicit table
$(\bar\Omega+\Gamma,e_s^\top(\bar\Omega+\Gamma),(\bar\Omega+\Gamma)\mathbf 1)$ ($e_s$ the
last unit vector, page-local). A base ARK that is not
[stiffly accurate](/properties/stiff-accuracy.md) is padded by appending $b^\top$ as
a last row and a zero column (Remark 2.2), the padding also used for IMEX-MRI-GARK.

## GARK form (Fish et al. 2024, §2, eqs. 2.5–2.8)

Representing each fast solve by one step of an $s^{\{\mathrm f\}}$-stage method
$(A^{\{\mathrm f\}},b^{\{\mathrm f\}},c^{\{\mathrm f\}})$ that satisfies the bushy-tree
conditions $b^{\{\mathrm f\}\top}(c^{\{\mathrm f\}})^k=1/(k+1)$, $k<n_\Omega$, the method is
a [GARK method](/methods/generalized-additive-runge-kutta.md) with Kronecker-product
tables, $C=\operatorname{diag}(c)$:

$$A^{\{\mathrm f,\mathrm f\}}=C\otimes A^{\{\mathrm f\}},\qquad A^{\{\mathrm f,\mathrm E\}}=A^{\{\mathrm f,\mathrm I\}}=\sum_k\Omega^{(k)}\otimes A^{\{\mathrm f\}}(c^{\{\mathrm f\}})^k,\qquad A^{\{\mathrm s,\mathrm f\}}=C\otimes b^{\{\mathrm f\}\top},\qquad A^{\{\mathrm s,\mathrm E\}}=\bar\Omega,\qquad A^{\{\mathrm s,\mathrm I\}}=\bar\Omega+\Gamma,$$

and weights equal to the last rows (first same as last). The restart makes the fast
block diagonal; in IMEX-MRI-GARK the fast block chains the stages through
$\Delta c$.

## Order conditions

**Theorem 2.3 (internal consistency).** The GARK abscissae of all partitions agree if

$$\Omega^{(0)}\mathbf 1=c,\qquad\Omega^{(k)}\mathbf 1=0\ (k\ge1),\qquad\Gamma\mathbf 1=0.$$

Compare the IMEX-MRI-GARK condition, which has $\Delta c$ in place of $c$
([IMEX-MRI-GARK](/methods/imex-mri-gark.md), Thm. 2.2 of Chinomona & Reynolds).

- **Orders 1–2.** With internal consistency and base and fast methods of order 2,
  there are no further coupling conditions (Remarks 2.1, 2.4).
- **Theorem 2.5 (order 3).** An internally consistent method with a third-order base
  and a fast method of order $\max(3,n_\Omega+1)$ has order 3 if and only if
  $$e_s^\top\Omega_\star c=\tfrac16,\qquad \Omega_\star:=\sum_{k=0}^{n_\Omega-1}\frac{\Omega^{(k)}}{(k+1)(k+2)}$$
  ($\Omega_\star$ page-local). Of the four GARK third-order coupling conditions two hold
  automatically and two coincide because $A^{\{\mathrm f,\mathrm E\}}=A^{\{\mathrm f,\mathrm I\}}$.
- **Theorem 2.6 (order 4).** With a fourth-order base and a fast method of order
  $\max(4,n_\Omega+2)$, order 4 needs six further conditions:
  $$\begin{aligned}
  &e_s^\top\Big(\sum_k\frac{\Omega^{(k)}}{(k+1)(k+3)}\Big)c=\tfrac18, &&e_s^\top\Omega_\star Cc=\tfrac1{12},\\
  &e_s^\top\Gamma C\Omega_\star c=0, &&e_s^\top\bar\Omega C\Omega_\star c=\tfrac1{24},\\
  &e_s^\top\Omega_\star\bar\Omega c=\tfrac1{24}, &&e_s^\top\Omega_\star\Gamma c=0.
  \end{aligned}$$
  They come from the 26 GARK fourth-order coupling conditions (21 once
  $A^{\{\mathrm f,\mathrm E\}}=A^{\{\mathrm f,\mathrm I\}}$), of which four hold automatically.
- **Theorem 2.7 ($n_\Omega\ge2$ for order 3).** With constant forcing ($n_\Omega=1$) the
  base condition $e_s^\top\Omega^{(0)}c=\tfrac12$ and the coupling condition
  $e_s^\top\Omega^{(0)}c=\tfrac13$ are incompatible, so a third-order IMEX-MRI-SR method
  needs at least a linear-in-time forcing.

Against the five families of fourth-order conditions of IMEX-MRI-GARK (with fast
moments of $A^{\{\mathrm f\}}$), the stage-restart conditions involve only the slow
coefficients; this is the "dramatic" simplification Fish et al. claim (§7).

## Linear stability (Fish et al. 2024, §3)

On $y'=(\lambda^{\{\mathrm f\}}+\lambda^{\mathrm E}+\lambda^{\mathrm I})y$, $z^{\{\cdot\}}=H\lambda^{\{\cdot\}}$,
with an exact fast solve,

$$R_{\mathrm{mr}}\big(z^{\{\mathrm f\}},z^{\mathrm E},z^{\mathrm I}\big)=e_s^\top\big(I-(z^{\mathrm E}+z^{\mathrm I})\,\mathcal N(z^{\{\mathrm f\}})-z^{\mathrm I}\Gamma\big)^{-1}e^{c\,z^{\{\mathrm f\}}},\qquad \mathcal N(z^{\{\mathrm f\}})=\sum_kk!\,\operatorname{diag}\big(\phi_{k+1}(c\,z^{\{\mathrm f\}})\big)\Omega^{(k)},$$

with $e^{c\,z^{\{\mathrm f\}}}$ the vector of $e^{c_iz^{\{\mathrm f\}}}$ (eq. 3.4; page-local $\mathcal N$, the source's $\eta$, renamed because $\eta$ is the registry entropy). The factor $k!$
translates the source's unnormalized $\varphi_{k+1}$ into the registry's
[$\phi$-functions](/methods/exponential-integrators.md) *(compiler translation, not in
the source)*. The restart puts $e^{c_iz^{\{\mathrm f\}}}$ on $y_n$ directly, where
IMEX-MRI-GARK chains $e^{\Delta c_iz^{\{\mathrm f\}}}$ from stage to stage. Fish et al.
use the joint region $\mathcal J_{\alpha,\rho,\beta,\xi}$, with sectors truncated at
radii $\rho$ (fast) and $\xi$ (implicit), and two reduced regions with only the
implicit or only the explicit slow part; definitions and the challenge they raise are on
[linear stability of multirate methods](/definitions/multirate-linear-stability.md).

## Methods (Fish et al. 2024, §4, Apps. A–C)

| Method | Order (embedding) | Slow stages | $n_\Omega$ | Implicit solves | $\gamma_{ii}$ | Abscissae $c$ |
|---|---|---|---|---|---|---|
| IMEX-MRI-SR2(1) | 2 (1) | 4 | 1 | 3 | $\tfrac{11}{23}$ | $(0,\tfrac35,\tfrac4{15},1)$ |
| IMEX-MRI-SR3(2) | 3 (2) | 5 | 2 | 4 | $\tfrac47$ | $(0,\tfrac{23}{34},\tfrac45,\tfrac{17}{15},1)$ |
| IMEX-MRI-SR4(3) | 4 (3) | 7 | 2 | 5 | $\tfrac14$ ($\gamma_{77}=0$) | $(0,\tfrac14,\tfrac34,\tfrac{11}{20},\tfrac12,1,1)$ |

- **SR2(1)**: free coefficients maximize the joint region; the embedding minimizes
  the Prince–Dormand C-statistic
  ([embedded pairs](/methods/embedded-runge-kutta-pair.md)). Its joint region at
  $\alpha=10^\circ$ is "essentially identical" to that of its explicit base; the
  implicit-only region is A-stable for $0^\circ\le\alpha\le45^\circ$, about
  A(80°)-stable at $\alpha=65^\circ$ and an enclosed bubble at $\alpha=85^\circ$ (Fig. 1).
  $\Omega^{(0)}$ has rows $(\tfrac35)$, $(\tfrac{14}{165},\tfrac2{11})$,
  $(-\tfrac{13}{54},\tfrac{137}{270},\tfrac{11}{15})$ below its zero first row.
- **SR3(2)**: implicit-only region A-stable for every plotted $\alpha$ except $85^\circ$
  (Fig. 2).
- **SR4(3)**: base ARK is LIRK4 of Calvo, de Frutos & Novo, padded to stiffly
  accurate form, so the last row of $\Gamma$ vanishes and the final stage has no
  implicit solve. The joint region was empty for every choice of the free
  parameters, so they optimize the explicit-only region; the implicit-only region
  is not A-stable for $\alpha\ne0$. The embedding minimizes
  the 2-norm of its fourth-order error coefficients (the source's $\hat\tau^{(4)}$, not the
  registry stage-order residual) because the C-statistic needs fifth-order conditions.
  The authors "suspect" the missing last-stage solve causes the poor stability (§4.3).

The full rational coefficients are in Apps. A–C of the version read.

## MERK methods as IMEX-MRI-SR methods (Fish et al. 2024, §5, Apps. D–E)

The explicit [multirate exponential Runge–Kutta (MERK)](/methods/multirate-exponential-methods.md)
methods of Luan, Chinomona & Reynolds are IMEX-MRI-SR methods with $\Gamma=0$ and
$f^{\mathrm I}=0$. Checking the new conditions gives "the first theoretical justification" that they keep
their order for a **nonlinear** fast partition (MERK was derived for $f^{\{\mathrm f\}}=Ly$):
MERK2 ($s=3$) and MERK3 ($s=4$) have orders 2 and 3; MERK4 ($s=7$, $n_\Omega=3$) has
order 4 if and only if $c_6=(3-4c_5)/(4-6c_5)$, which Luan et al.'s nodes
$c_5=\tfrac56$, $c_6=\tfrac13$ satisfy; MERK5 ($s=11$, $n_\Omega=4$) has order at least
4 under a condition on $c_9$ that its nodes satisfy, and order 5 is only observed
(fifth-order coupling conditions are not available). The joint and explicit-only
regions of MERK4 and MERK5 are empty, which Fish et al. read as "a deficiency in these
definitions of joint stability" rather than in the methods (§5.3).

## Numerical behaviour (Fish et al. 2024, §6)

- **[Kværnø–Prothero–Robinson](/benchmarks/prothero-robinson-problem.md)** (nonlinear
  fast partition, $h=H/10$): measured rates SR2(1) 2.01, SR3(2) 3.11, SR4(3) 3.85;
  MERK2–5 2.06, 3.17, 4.25, 5.32; IMEX-MRI-GARK3a/3b/4 3.05, 3.09, 4.11; Lie–Trotter
  1.01, Strang–Marchuk 1.98 (Fig. 5).
- **Stiff [Brusselator](/benchmarks/brusselator.md)**, fixed step (reaction fast,
  diffusion implicit, advection explicit; 201/801 points): rates SR2(1) 2.00/2.01,
  SR3(2) 3.09/2.90, SR4(3) 3.00/1.90, IMEX-MRI-GARK4 3.41/2.42; both splittings and both
  fourth-order methods show strong [order reduction](/definitions/order-reduction.md).
  SR4(3) is unstable for $H>1/320$ and $H>1/640$, IMEX-MRI-GARK4 for $H>1/80$ and
  $H>1/160$. SR2(1) is two to three orders of magnitude more accurate than the
  splittings at equal runtime; SR3(2) is the most efficient method on 801 points
  between errors of about $10^{-7}$ and $10^{-11}$; the third-order methods beat the
  fourth-order ones (Fig. 6).
- **Adaptive multirate stepping** with the Constant-Constant controller and LASA-mean
  fast-error estimate of [Fish & Reynolds (2023)](/sources/fish-2023.md)
  ($\mathrm{tol}$ split equally between scales; see
  [step-size control](/methods/step-size-control.md)): SR3(2) is generally the most
  efficient in fast evaluations, SR2(1) the least; SR4(3) sometimes gets "stuck" at the
  same error for different costs, attributed to its low-quality embedding; SR3(2)
  failed at $\mathrm{tol}=10^{-3},10^{-5}$ and SR4(3) at $10^{-4},10^{-5}$ by oscillating
  between accepted and rejected steps (Fig. 7). Fish & Reynolds (2023) had tested their
  controllers on explicit and implicit MRI-GARK methods only.

## Qualifications

- Orders assume an exact or sufficiently accurate fast solve (fast order
  $\max(3,n_\Omega+1)$ for order 3, $\max(4,n_\Omega+2)$ for order 4).
- The version read is arXiv v1; Fish et al. print several index slips in the GARK
  tables (e.g. eq. 2.4c has $b_{j,k}$ for $a^{\{\mathrm f\}}_{j,k}$) and label the second
  MERK4 coefficient block (D.3) $\Omega^{\{1\}}$ where $n_\Omega=3$ requires
  $\Omega^{\{2\}}$; the theorems above are unaffected.
- The source's $\varphi_k$ lacks the $1/(k-1)!$ factor, so $\varphi_k=(k-1)!\,\phi_k$, the
  convention also of Chinomona & Reynolds.

# Citations

- [Fish et al. (2024)](/sources/fish-2024.md) — Def. 1.1–1.2 (eqs. 1.5–1.6), §1.1, §2 (eqs. 2.5–2.8, Remark 2.2, Thms. 2.3, 2.5–2.7), §3 (eqs. 3.4–3.7), §4 (Figs. 1–3, Apps. A–C), §5 (Apps. D–E), §6 (Figs. 5–7), §7.
- [Fish & Reynolds (2023)](/sources/fish-2023.md) — the multirate controller and LASA-mean estimate used in §6.2.2.
