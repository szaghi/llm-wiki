---
type: Method
title: "IMEX multirate infinitesimal GARK methods"
description: "IMEX-MRI-GARK methods split the slow scale of a three-way additive problem into implicit and explicit parts and treat the fast scale infinitesimally; the page states the scheme, its GARK form, internal-consistency and third- and fourth-order conditions, linear stability, the methods 3a, 3b and 4, and their measured behaviour."
status: established
aliases: [IMEX-MRI-GARK, ImEx-MRI-GARK, implicit-explicit multirate infinitesimal GARK, IMEX-MRI-GARK3a, IMEX-MRI-GARK3b, IMEX-MRI-GARK4]
tags: [multirate, imex, runge-kutta, order-conditions, stability]
timestamp: 2026-10-20T06:18:00Z
---

# IMEX multirate infinitesimal GARK methods

IMEX-MRI-GARK methods, introduced by
[Chinomona & Reynolds (2021)](/sources/chinomona-2021.md), integrate the
three-way additive problem

$$y'=f^{\mathrm I}(t,y)+f^{\mathrm E}(t,y)+f^{\{\mathrm f\}}(t,y),$$

with a slow stiff part $f^{\mathrm I}$ treated implicitly, a slow nonstiff part
$f^{\mathrm E}$ treated explicitly and a fast part $f^{\{\mathrm f\}}$ treated
infinitesimally. They extend Sandu's two-way
[MRI-GARK methods](/methods/multirate-infinitesimal-methods.md) by giving the slow
forcing of every modified fast problem an implicit and an explicit polynomial
coupling. Before them, the authors note, the only multirate methods allowing IMEX
slow treatment with an infinitesimal fast scale were the first-order Lie–Trotter
and a second-order Strang–Marchuk [splitting](/methods/operator-splitting.md)
(§1, eqs. 1.3–1.4). [ARKODE](/software/arkode.md) implements all third- and
fourth-order methods of the paper ([Reynolds et al. 2023](/sources/reynolds-2023.md), §2.3).

## The scheme (Chinomona & Reynolds 2021, Def. 2.1, eqs. 2.3–2.4)

Slow abscissae $0=c_1\le\dots\le c_s\le1$ with $\Delta c_i=c_i-c_{i-1}\ge0$; for
$k=0,\dots,k_{\max}$ a **lower** triangular $\Gamma^{(k)}$ (implicit coupling) and a
**strictly lower** triangular $\Omega^{(k)}$ (explicit coupling), each with zero
first row (registry symbols; the source writes $\Gamma^{\{k\}}$, $\Omega^{\{k\}}$).
With $f^{\mathrm I}_j=f^{\mathrm I}(t_n+c_jH,Y_j)$ and $f^{\mathrm E}_j$ likewise, each
slow stage $Y_i$, $i\ge2$, is the end value $v(H)$ of

$$v'(\theta)=\Delta c_i\,f^{\{\mathrm f\}}\big(t_n+c_{i-1}H+\Delta c_i\theta,v\big)+\sum_{j=1}^{i}\gamma_{ij}\big(\tfrac\theta H\big)f^{\mathrm I}_j+\sum_{j=1}^{i-1}\omega_{ij}\big(\tfrac\theta H\big)f^{\mathrm E}_j,\qquad v(0)=Y_{i-1},$$

with $\gamma_{ij}(\tau)=\sum_k\gamma^{(k)}_{ij}\tau^k$, $\omega_{ij}(\tau)=\sum_k\omega^{(k)}_{ij}\tau^k$,
$Y_1=y_n$ and $y_{n+1}=Y_s$.

**Base IMEX-ARK method.** The construction starts from an
[IMEX Runge–Kutta method](/methods/imex-runge-kutta.md) of the target order $p$ (the source's $q$) whose explicit
and implicit tables share abscissae, have an explicit first stage, and are written
in stiffly accurate form; a table is padded to that form by
$c\to(c,1)$, $A\to\begin{bmatrix}A&0\\b^\top&0\end{bmatrix}$, which leaves its order
conditions unchanged (§2.1). Let $\bar A^{\mathrm I}$, $\bar A^{\mathrm E}$ denote the
padded $s\times s$ tables (page-local).

## GARK representation and internal consistency

Representing the fast solve by one step of an $s^{\{\mathrm f\}}$-stage Runge–Kutta
method $(A^{\{\mathrm f\}},b^{\{\mathrm f\}},c^{\{\mathrm f\}})$ (page-local) whose weights
satisfy $b^{\{\mathrm f\}\top}(c^{\{\mathrm f\}})^k=1/(k+1)$, Chinomona & Reynolds
(§2.1, eqs. 2.5–2.26) write the method as a
[GARK method](/methods/generalized-additive-runge-kutta.md). With
$\bar\Gamma=\sum_k\Gamma^{(k)}/(k+1)$, $\bar\Omega=\sum_k\Omega^{(k)}/(k+1)$ and
$\mathsf E$ the lower-triangular all-ones matrix (page-local):

- the slow tables are $\mathbf A^{\{\mathrm I,\mathrm I\}}=\mathsf E\bar\Gamma$ and
  $\mathbf A^{\{\mathrm E,\mathrm E\}}=\mathsf E\bar\Omega$; consistency with the base
  method when $f^{\{\mathrm f\}}\equiv0$ requires $\mathsf E\bar\Gamma=\bar A^{\mathrm I}$ and
  $\mathsf E\bar\Omega=\bar A^{\mathrm E}$ (eq. 2.11);
- both slow partitions share one slow–fast coupling
  $\Delta C\otimes b^{\{\mathrm f\}\top}$, with $\Delta C$ lower triangular holding
  $\Delta c_j$ in column $j$, which satisfies the row-sum condition automatically
  (eqs. 2.12–2.18);
- the fast and fast–slow tables are Kronecker products of the slow structure with
  the fast tableau (eqs. 2.20–2.26).

**Theorem 2.2 (internal consistency).** The method is internally consistent for
every fast method if and only if

$$\Gamma^{(0)}\mathbf 1=\Omega^{(0)}\mathbf 1=\Delta c,\qquad\Gamma^{(k)}\mathbf 1=\Omega^{(k)}\mathbf 1=0\quad(k\ge1).$$

An internally consistent method whose component tables have order at least 2 is
at least second order (§2.1.1, citing Sandu & Günther).

## Order conditions

Let $\mathsf N$ be the sub-diagonal shift, $\mathsf N_{ij}=\delta_{i,j+1}$, and define the
fast moments $\zeta_k=b^{\{\mathrm f\}\top}A^{\{\mathrm f\}}(c^{\{\mathrm f\}})^k$ and the
matrices $\mathcal A^{\mathrm I}_\zeta=\mathsf N\bar A^{\mathrm I}+\sum_k\zeta_k\Gamma^{(k)}$,
$\mathcal A^{\mathrm E}_\zeta=\mathsf N\bar A^{\mathrm E}+\sum_k\zeta_k\Omega^{(k)}$ (all
page-local; eqs. 2.30–2.39, adapted from Sandu's Lemma 3.8).

**Theorem 2.3 (third order).** An internally consistent IMEX-MRI-GARK method has
order 3 if and only if the base IMEX-ARK has order at least 3 and

$$\Delta c^\top\mathcal A^{\mathrm I}_\zeta\,c=\tfrac16,\qquad\Delta c^\top\mathcal A^{\mathrm E}_\zeta\,c=\tfrac16.$$

**Theorem 2.4 (fourth order).** A method satisfying Theorem 2.3 has order 4 if and
only if the base has order at least 4 and five families of coupling conditions
(2.41a–e) hold for every pair $\sigma,\nu\in\{\mathrm I,\mathrm E\}$; for example
(2.41b) $\Delta c^\top\mathcal A^\sigma_\zeta c^2=\tfrac1{12}$ and (2.41e)
$\Delta c^\top\mathcal A^\sigma_\zeta\bar A^\nu c=\tfrac1{24}$. The others involve the
further fast moments $(b^{\{\mathrm f\}}\circ c^{\{\mathrm f\}})^\top A^{\{\mathrm f\}}(c^{\{\mathrm f\}})^k$
and $b^{\{\mathrm f\}\top}(A^{\{\mathrm f\}})^2(c^{\{\mathrm f\}})^k$ ($\circ$ the
componentwise product). Of the 26 fourth-order
GARK coupling conditions, 10 hold by structure and base-method order (2.48), and
16 reduce to (2.41) (2.49). Taking $b^{\mathrm E}=b^{\mathrm I}$ in the base helps
only (2.41c), whose four conditions collapse to two (Remark 2.5). For
solve-decoupled tables with $k_{\max}=0$, each third-order condition is equivalent
to the MIS third-order condition of Knoth & Wolke (Remark 4.1).

## Linear stability

On $y'=(\lambda^{\{\mathrm f\}}+\lambda^{\mathrm E}+\lambda^{\mathrm I})y$ with
$z^{\{\cdot\}}=H\lambda^{\{\cdot\}}$ and an exact fast solve, variation of constants
gives (§3, eqs. 3.1–3.3)

$$Y_i=e^{\Delta c_iz^{\{\mathrm f\}}}Y_{i-1}+z^{\mathrm E}\sum_{j<i}\tilde\omega_{ij}Y_j+z^{\mathrm I}\sum_{j\le i}\tilde\gamma_{ij}Y_j,\quad
\tilde\omega_{ij}=\sum_kk!\,\omega^{(k)}_{ij}\phi_{k+1}\big(\Delta c_iz^{\{\mathrm f\}}\big),\quad
\tilde\gamma_{ij}=\sum_kk!\,\gamma^{(k)}_{ij}\phi_{k+1}\big(\Delta c_iz^{\{\mathrm f\}}\big),$$

so that
$R_{\mathrm{mr}}(z^{\{\mathrm f\}},z^{\mathrm E},z^{\mathrm I})=e_s^\top\big(I-\operatorname{diag}(e^{\Delta c\,z^{\{\mathrm f\}}})\mathsf N-z^{\mathrm E}\tilde\Omega-z^{\mathrm I}\tilde\Gamma\big)^{-1}e_1$
($e_j$ unit vectors and the matrices $\tilde\Omega=(\tilde\omega_{ij})$, $\tilde\Gamma=(\tilde\gamma_{ij})$
page-local; the source writes $\eta$, $\mu$, and $\eta$ is the registry entropy). The factor $k!$ is the translation of the
source's unnormalized $\varphi_{k+1}$ into the registry's
[$\phi$-functions](/methods/exponential-integrators.md) *(compiler translation, not
in the source)*. The **joint stability region** $\mathcal J_{\alpha,\beta}$ built on
this function is defined on
[linear stability of multirate methods](/definitions/multirate-linear-stability.md).

## Methods

| Method | Base | Slow stages | $k_{\max}$ | Implicit slow solves per step | Construction |
|---|---|---|---|---|---|
| IMEX-MRI-GARK3a | ARS(3,4,3), padded, solve-decoupled | 8 | 0 | 3 | minimum-norm least-squares solution of 50 linear conditions in 54 unknowns |
| IMEX-MRI-GARK3b | same | 8 | 0 | 3 | 4 free variables maximize $\mathcal J_{\alpha,\beta}$ along the negative real axis |
| IMEX-MRI-GARK4 | new order-4 IMEX-ARK of the authors | 12 | 1 | 5 | conditions (2.11), (2.29), (2.40), (2.41) solved in MATLAB |

- **3a and 3b** (§4.1, Apps. A–B): abscissae $c_1=0$,
  $c_2=c_3=\gamma_{\mathrm{ARS}}=0.4358665215\ldots$, $c_4=c_5=0.7179332607\ldots$,
  $c_6=c_7=c_8=1$, with implicit diagonal entries
  $\gamma^{(0)}_{33}=\gamma^{(0)}_{55}=\gamma^{(0)}_{77}=\gamma_{\mathrm{ARS}}$ (page-local
  name for the diagonal coefficient of ARS(3,4,3); the source's $\eta$, renamed because
  $\eta$ is the registry entropy). Coefficients are printed to 36 digits and in
  the authors' repository. 3b's joint region is "significantly larger" than 3a's:
  it covers most of the base IMEX-ARK region for $\alpha=10^\circ,45^\circ$ and
  $\beta\le60^\circ$, while 3a's shrinks considerably as $\beta$ grows from $10^\circ$
  to $80^\circ$ (Fig. 1).
- **IMEX-MRI-GARK4** (§4.2, App. C): $c=(0,\tfrac12,\tfrac12,\tfrac58,\tfrac58,\tfrac34,\tfrac34,\tfrac78,\tfrac78,1,1,1)$,
  implicit diagonal $\tfrac14$; some coefficients are large (e.g.
  $\omega^{(1)}_{83}\approx-77.27$). No order-4 IMEX-ARK with sorted abscissae in
  $[0,1]$ was known to the authors, so they designed one. Even with $z^{\mathrm E}=0$
  its implicit-plus-fast stability region is very small and $\mathcal J_{\alpha,\beta}$
  is empty; the authors "do not promote its widespread use".

## Numerical behaviour

- **Kværnø–Prothero–Robinson** (multirate, nonlinear, non-autonomous;
  [Prothero–Robinson problem](/benchmarks/prothero-robinson-problem.md); fast step
  $H/20$, MATLAB): measured rates 3.10 (3a), 3.14 (3b), 4.15 (4) (§5.1, Fig. 2).
- **Stiff [Brusselator](/benchmarks/brusselator.md)** (advection explicit, diffusion
  implicit, reaction fast; fast step $H/5$; C with ARKODE): rates 2.86, 2.92,
  3.12 on 201 points and 2.41, 2.47, 2.69 on 801 points for 3a, 3b, 4, i.e.
  [order reduction](/definitions/order-reduction.md) under spatial refinement.
  IMEX-MRI-GARK4 is unstable for $H>1/80$ (201 points) and $H>1/160$ (801 points);
  3a and 3b are stable at every tested step. All IMEX-MRI-GARK and implicit
  MRI-GARK methods are more efficient than Lie–Trotter and Strang–Marchuk at every
  accuracy; 3a/3b run as fast as implicit MRI-GARK-ESDIRK34a on 201 points, which
  wins on 801 points (§5.2, Fig. 3).
- The third-order methods beat IMEX-MRI-GARK4 on the Brusselator because they need
  3 instead of 5 slow implicit solves per step, a cheaper fast DIRK (2 instead of 5
  implicit stages) and suffer milder order reduction (the attribution is the
  authors' belief).
- In ARKODE, IMEX-MRI-GARK3a serves as slow method for the inner-solver comparison
  of Reynolds et al. (2023, §5.1.3, Table 2); see
  [multirate infinitesimal methods](/methods/multirate-infinitesimal-methods.md).
- **Re-measured by [Fish et al. (2024)](/sources/fish-2024.md)** (§6, fast step $H/10$,
  least-squares rates): on KPR 3.05 (3a), 3.09 (3b), 4.11 (4); on the stiff Brusselator
  3.36/2.71, 3.25/2.69 and 3.41/2.42 on 201/801 points. They reproduce the instability of
  IMEX-MRI-GARK4 for $H>1/80$ and $H>1/160$. The third-order methods are close to the
  stage-restart [IMEX-MRI-SR3(2)](/methods/imex-mri-sr.md), which is the most efficient method on
  801 points between errors of about $10^{-7}$ and $10^{-11}$, and IMEX-MRI-SR4(3) has a slight
  consistent edge over IMEX-MRI-GARK4 (Fig. 6). The rates differ from Chinomona & Reynolds'
  (e.g. 2.86 against 3.36 for 3a on 201 points); the two papers use different fast steps
  ($H/5$ and $H/10$), and Fish et al. print a Brusselator variant with $-(w-1)u$ in the
  reaction term ([Brusselator](/benchmarks/brusselator.md)), so the runs need not be identical.
- **Reacting flow at scale** ([Loffeld et al. 2024](/sources/loffeld-2024.md), §6): on a
  mass-fraction advection–diffusion–reaction model with GRI-Mech 3.0 chemistry fast, advection
  slow explicit and diffusion (coefficients multiplied by 1000 to make it stiff) slow implicit,
  $128^3$ cells on 512 MPI ranks, IMEX-MRI-GARK3b and IMEX-MRI-GARK4 with ten fast steps per slow
  step (Kutta's third-order method and RK4 as fast solvers) have a "significant performance
  advantage" over a single-rate fourth-order ARK-IMEX of Kennedy & Carpenter (Fig. 5). Per slow
  step 3b costs four $f^{\mathrm E}$ evaluations, three implicit solves and three fast problems,
  IMEX-MRI-GARK4 six, five and five; the single-rate ARK-IMEX costs six explicit evaluations and
  five implicit solves per step (§3.2). The multirate methods needed tighter
  algebraic-solver tolerances than the single-rate method at the same coarse step, which the
  authors attribute to their higher accuracy there (Tables 3–4). Implicit stages use Newton with
  matrix-free GMRES; geometric multigrid preconditioning pays off from $128^3$ cells upward and
  becomes critical at $256^3$ with stiffer diffusion (Tables 5–8;
  [implicit stage solvers](/methods/implicit-stage-solvers.md)). With two-level AMR the
  multirate and multilevel gains compound: 478 against 8582 (time units not printed) for
  single-rate single-level ARK-IMEX, about 18× (Table 9).

## Qualifications

- **Sorted abscissae and embeddings.** Fish et al. (2024, §1.1) note that IMEX-MRI-GARK
  needs non-decreasing abscissae, which forces padding stages chosen by trial and error, and
  that "no authors have successfully created IMEX-MRI-GARK methods with embeddings"; their
  stage-restart variant removes the restriction ([IMEX-MRI-SR](/methods/imex-mri-sr.md)). This
  answers the open item on embeddings of §6 below by a different method class, not within
  IMEX-MRI-GARK.
- Order holds under an exact or sufficiently accurate fast solve. The authors
  expect, without showing it, that 3a/3b would be "significantly more efficient"
  than implicit MRI-GARK on reacting flow with nonlinear shock-capturing advection
  (§5.2). Order-5 conditions, embedded methods, optimized fourth-order methods and
  solve-coupled variants are left open (§6).
- The novelty claim ("no multirate methods allowing IMEX treatment of the slow
  time scale … of order three or higher") is scoped to the authors' knowledge and
  to infinitesimal fast treatment; it is not a claim about multirate GARK methods
  with fixed fast bases ([Multirate GARK](/methods/multirate-gark.md)).
- Printed slips in the version read: the assumption on the fast weights is stated
  for $k=1,\dots,p$ where order $p$ gives $k=0,\dots,p-1$ (§2.1); §4 refers to
  "methods of the form (2.1)" for (2.3); the KPR explicit forcing is printed with a
  plus sign where the exact solution requires a minus sign (p. 21).

# Citations

- [Chinomona & Reynolds (2021)](/sources/chinomona-2021.md) — §1 (eqs. 1.3–1.4), §2 (Def. 2.1, eqs. 2.3–2.49, Thms. 2.2–2.4, Remark 2.5), §3 (eqs. 3.1–3.3), §4 (Remark 4.1, Apps. A–C, Fig. 1), §5 (Figs. 2–3), §6.
- [Reynolds et al. (2023)](/sources/reynolds-2023.md) — §2.3 (MRIStep implements the methods), §5.1.3 (Table 2).
- [Fish et al. (2024)](/sources/fish-2024.md) — §1.1, §6.1–6.2 (Figs. 5–6).
- [Loffeld et al. (2024)](/sources/loffeld-2024.md) — §3.2, §6 (Fig. 5, Tables 3–9).
