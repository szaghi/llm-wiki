---
type: Method
title: "Deferred correction (DeC) time integration"
description: "Deferred correction reaches a high-order implicit collocation-type time discretization by a fixed number of iterations of a cheap low-order operator; the page records the two-operator iteration, its contraction estimate, the explicit kinetic variant whose stiff source stays implicit but is computed explicitly, its linear stability, and the fully discrete entropy-conservative residual-distribution use."
status: established
aliases: [DeC, defect correction, deferred correction method, DeC(p,K), Abgrall's DeC]
tags: [asymptotic-preserving, entropy-stable, finite-difference, limiting]
timestamp: 2026-10-23T10:00:00Z
---

# Deferred correction (DeC) time integration

A **deferred correction** (DeC, also defect correction) method defines the step
$t^n\to t^{n+1}$ through two operators on the vector of sub-step states: a high-order operator
$\mathcal D^2$ (page-local), whose root is an implicit collocation-type approximation of the
time integral, and a low-order operator $\mathcal D^1$ (page-local), cheap to invert. Instead
of solving $\mathcal D^2=0$, the method iterates $\mathcal D^1$ a fixed number of times, each
iteration gaining one order. In this bundle the technique is Abgrall's: it underlies the
explicit high-order [discrete kinetic relaxation schemes](/methods/discrete-kinetic-relaxation-scheme.md)
of [Abgrall & Nassajian Mojarrad (2024)](/sources/abgrall-2024.md) and the fully discrete
entropy-conservative residual-distribution scheme of
[Abgrall et al. (2022)](/sources/abgrall-2022.md).

Page-local notation: sub-nodes $t^{n,m}=t^n+\mathsf t_m\Delta t$, $0=\mathsf t_0<\dots<\mathsf t_{M_{\mathrm s}}=1$;
quadrature weights $\Omega_{mk}=\int_0^{\mathsf t_m}\ell_k(s)\,ds$ of the Lagrange basis $\ell_k$
on the sub-nodes, so $\sum_k\Omega_{mk}=\mathsf t_m$; $U=(u^{n,1},\dots,u^{n,M_{\mathrm s}})$ the
sub-step states; $U^{(\ell)}$ the $\ell$-th iterate. The registry's $\mathcal L$ is the
semi-discrete spatial operator.

## The iteration

For $\frac{d}{dt}u=\mathcal L(u)$ the two operators are, row $m$,

$$\begin{aligned}
\mathcal D^2(U)_m&=u^{n,m}-u^{n,0}-\Delta t\sum_{k=0}^{M_{\mathrm s}}\Omega_{mk}\,\mathcal L(u^{n,k}),\\
\mathcal D^1(U)_m&=u^{n,m}-u^{n,0}-\Delta t\,\mathsf t_m\,\mathcal L(u^{n,0}),
\end{aligned}$$

the second being a forward-Euler step to each sub-node. The iteration is

$$U^{(0)}=(u^n,\dots,u^n),\qquad \mathcal D^1\big(U^{(\ell+1)}\big)=\mathcal D^1\big(U^{(\ell)}\big)-\mathcal D^2\big(U^{(\ell)}\big),\qquad u^{n+1}=u^{n,M_{\mathrm s},(K_{\mathrm{it}})},$$

with $K_{\mathrm{it}}$ iterations (page-local). Because $\mathcal D^1$ is explicit in $\mathcal L$,
each iteration is a sequence of explicit updates
$u^{n,m,(\ell+1)}=u^{n,0}+\Delta t\sum_k\Omega_{mk}\mathcal L(u^{n,k,(\ell)})$. This is the form of
Abgrall et al. (2022) (§2.1, Eqs. (16)–(18)) for residual distribution, where $\mathcal D^1$
lumps the mass matrix ($\lvert C_\sigma\rvert$, the integral of the basis function) and
$\mathcal D^2$ keeps the consistent mass, and of Abgrall & Nassajian Mojarrad (2024) (§2.1,
Eqs. (7)–(10)) for the kinetic system. Both label schemes DeC$(p,K_{\mathrm{it}})$: order and
iteration count in the 2024 paper (Table 1); Abgrall et al. (2022) use DeC(2,2) and DeC(4,4)
without defining the label in the text.

**Contraction** (Abgrall & Nassajian Mojarrad (2024), §2.2). If $\mathcal D^1-\mathcal D^2$ is
Lipschitz with constant $O(\Delta t)$ in a discrete $H^{-1}$-type norm (Lemma 1, for linear
upwind flux coefficients) and $\mathcal D^1$ is inverse-Lipschitz with a constant independent
of the data (Lemma 2), then, $U^*$ being the unique root of $\mathcal D^2$, there is
$\theta_{\mathrm{DeC}}$ (page-local) with

$$\big\lVert U^{(\ell+1)}-U^*\big\rVert_{L^2}\le(\theta_{\mathrm{DeC}}\Delta t)^{\ell+1}\big\lVert U^{(0)}-U^*\big\rVert_{L^2}$$

(Prop. 1; the proof is a sketch through a discrete Poincaré inequality). For the stiff kinetic
system $\theta_{\mathrm{DeC}}$ is independent of the relaxation time $\varepsilon$, so the
contraction holds uniformly as $\varepsilon\to0$; asymptotic preservation itself is the
separate consistency statement of Prop. 2
([discrete kinetic relaxation schemes](/methods/discrete-kinetic-relaxation-scheme.md)).

## Choices of the high-order operator

Abgrall & Nassajian Mojarrad (2024) (§2.3) take for $\mathcal D^2$:

| Order | Scheme | Sub-nodes | Weights |
|---|---|---|---|
| 1 | implicit Euler | $0,1$ | $\Omega=(1)$ |
| 2 | Crank–Nicolson | $0,1$ | $\Omega=(\tfrac12)$, $\Omega_{10}=\tfrac12$ |
| 4 | three-node scheme cited from Hairer–Wanner | $0,\tfrac12,1$ | rows $(\tfrac5{24},\tfrac13,-\tfrac1{24})$ and $(\tfrac16,\tfrac23,\tfrac16)$ |

*(compiler check, not in the sources: the fourth-order weights are those of the three-stage
Lobatto IIIA collocation method, and the block acting on the unknown sub-steps,
$\begin{pmatrix}1/3&-1/24\\2/3&1/6\end{pmatrix}$, has eigenvalues $\tfrac14\pm\tfrac{\sqrt3}{12}\mathrm i$,
with positive real part.)*

## Stiff sources: implicit in both operators

For a stiff source the 2024 scheme keeps the source in the **same implicit form** in
$\mathcal D^1$ and $\mathcal D^2$, so that it cancels in $\mathcal D^1(U^{(\ell)})-\mathcal D^2(U^{(\ell)})$
except at the new iterate; convection is explicit in $\mathcal D^1$ (Eqs. (9)–(10)). The
resulting step is IMEX in structure but computationally explicit for relaxation systems,
because the projection onto the conserved variables annihilates the relaxation source and
yields the conserved part of the new iterate explicitly (Eq. (12)); see
[discrete kinetic relaxation schemes](/methods/discrete-kinetic-relaxation-scheme.md). The
authors set this against IMEX Runge–Kutta asymptotic-preserving methods, which they say
have "order limitations", and splitting-based relaxation schemes, limited to second order in
time (§1; [IMEX Runge–Kutta](/methods/imex-runge-kutta.md)).

## Linear stability

For $\partial_tu+a\partial_xu+b\partial_yu=0$ ($a,b>0$, page-local) with upwind differences of
Fourier symbols $g_1,g_2$ and $g=\mu g_1+\nu g_2$, $\mu=a\Delta t/\Delta x$, $\nu=b\Delta t/\Delta y$
(page-local), Abgrall & Nassajian Mojarrad (2024) (§4, Eqs. (19)–(24)) write the DeC
amplification factors as recursions whose fixed point is the implicit scheme:

- implicit Euler, $G_1=1/(1+g)$: $G_{1,\ell+1}=1-gG_{1,\ell}$, so
  $G_{1,\ell+1}-G_1=(-1)^{\ell+1}g^{\ell+1}(1-G_1)$, convergent for $\lvert g\rvert<1$;
- Crank–Nicolson, $G_2=(1-g/2)/(1+g/2)$: $G_{2,\ell+1}=1-\tfrac g2-\tfrac g2G_{2,\ell}$, error
  factor $(-g/2)^{\ell+1}$, convergent for $\lvert g\rvert<2$;
- fourth order: a $2\times2$ recursion with matrix
  $\mathsf M_4=\begin{pmatrix}1/3&-1/24\\2/3&1/6\end{pmatrix}$, convergent when $\lvert g\rvert$ times its
  spectral norm is below 1.

Stability of the iterate is then a condition on $\lvert g\rvert$ given by the stability region
after $K_{\mathrm{it}}$ iterations (Fig. 2); "the larger" region "is achieved for $r+1$
iterations for scheme of order $r$" (§4). Table 1 prints the resulting directional CFL bounds
$\max(\lvert\mu\rvert,\lvert\nu\rvert)$: DeC(2,2) 0.4, DeC(2,3) $2/\sqrt3$, DeC(2,4) $\sqrt{2.2}$,
DeC(4,4) $0.75\sqrt{6.8}$, DeC(4,5) 2.25, DeC(4,6) $1.5\sqrt2$, i.e. above one for most
choices. The analysis excludes the source term; in the tests the fourth-order scheme runs at
CFL 1, reaches 1.2 for the isentropic vortex to $t=200$ with five iterations, and does not run
above 1.3 (§4, Remark 1).

## Fully discrete entropy conservation

Abgrall et al. (2022) (Remark 2.2, Eq. (19)) apply an [entropy correction term](/methods/entropy-correction-term.md)
to the **whole space–time bracket** of each DeC update, i.e. to
$\int\varphi_\sigma(u^{n,m}-u^{n,0})+\Delta t\sum_k\Omega_{mk}\Phi_{\sigma}(u^{n,k,(\ell)})$
(page-local test function $\varphi_\sigma$ and space residual $\Phi_\sigma$), using the entropy
difference between the iterate and $u^{n,0}$ and the space–time entropy residual; this gives a
fully discrete entropy-conservative residual-distribution scheme, presented as the first one.
Correcting only the space residual gives semi-discrete entropy conservation, as with
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md) stages. On the radial Sod problem with DeC(2,2)
and linear Bernstein elements the uncorrected Galerkin scheme breaks down at $t\approx0.16$ and
the corrected one runs to $t=0.25$; DeC(4,4) with cubic elements needs
[MOOD](/methods/mood-a-posteriori-limiting.md) positivity enforcement (§4, Figs. 1–5).

## Qualifications

- **Printed amplification factors.** Abgrall & Nassajian Mojarrad (2024) print the
  fourth-order implicit amplification vector as $\frac1{2\vartheta_G}(24-g^2,\ 24-12g+2g^2)^\top$
  with $\vartheta_G=24+12g+2g^2$ (page-local), the convergence bound as
  $\lvert g\rvert\le\big(\frac{337+\sqrt{104353}}{1152}\big)^{-1}\approx1.745$, the maxima of
  the first- and second-order symbols as 4 and 2, and the second-order recursion with $G_3$
  in place of $G_2$ (Eq. (21)). *(compiler check, not in the sources: solving the printed
  $2\times2$ system gives $\frac1{\vartheta_G}(24-g^2,\ 24-12g+2g^2)^\top$, which equals $(1,1)$ at
  $g=0$ as it must; for the printed matrix $\mathsf M_4$ (page-local) the largest eigenvalue of $\mathsf M_4^\top\mathsf M_4$ is
  $\frac{337+\sqrt{104353}}{1152}\approx0.5729$, so the spectral-norm condition is
  $\lvert g\rvert<1.3211$, the printed bound being the inverse square of the norm; the symbol of
  $u_i-u_{i-1}$ has maximum modulus 2 and that of the second-order upwind difference 4, so the
  two printed maxima are swapped; the spectral radius of the matrix is $1/(2\sqrt3)$, so the
  norm condition is only sufficient.)*
- **Table 1 is not reproducible from the text.** The text bounds
  $\lvert\mu g(\vartheta_1)+\nu g(\vartheta_2)\rvert$ by $2\max(\lvert\mu\rvert,\lvert\nu\rvert)\max_\vartheta\lvert g\rvert$
  against the stability radii printed in the caption of Fig. 2. *(compiler check, not in the sources: the
  fourth-order entries are $2\rho_{\mathrm s}/\max\lvert g\rvert$ with $\max\lvert g\rvert=8/3$ and
  the printed radii $\rho_{\mathrm s}$ (page-local), the second-order DeC(2,2) and DeC(2,4)
  entries equal the radii themselves, and DeC(2,3) $=2/\sqrt3$ matches neither rule for the
  printed radius $\sqrt3$; the printed decimal "$\sqrt{2.2}\approx1.58$" is $1.483$.)* The
  values are therefore quoted as printed.
- **Iteration count.** Both papers write the final state with the number of sub-nodes as
  superscript where the iteration count is meant (Abgrall et al. (2022), p. 7: "$K$
  corrections $k=0,\dots,M$"; Abgrall & Nassajian Mojarrad (2024), §2.1, $\mathbf F^{(M)}$
  while Table 1 runs five or six iterations with two sub-steps).
- The contraction estimate (Prop. 1) and the $\varepsilon$-uniform bounds it needs are shown
  for orders 1 and 2; for order 4 they are "easy to observe" and not shown (§2.3).

# Citations

- [Abgrall & Nassajian Mojarrad (2024)](/sources/abgrall-2024.md) — §1, §2.1 (Eqs. (7)–(14)), §2.2 (Lemmas 1–2, Prop. 1), §2.3, §4 (Eqs. (19)–(24), Table 1, Fig. 2, Remark 1).
- [Abgrall et al. (2022)](/sources/abgrall-2022.md) — §2.1 (Eqs. (16)–(19), Remark 2.2), §4 (Figs. 1–5) (arXiv v4).
