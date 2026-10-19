---
type: Method
title: "Processing and effective order"
description: "A kernel $\\psi_h$ has effective order $p$ if a near-identity processor $\\pi_h$ makes $\\pi_h\\circ\\psi_h\\circ\\pi_h^{-1}$ of order $p$; since the processor acts only at output times, the kernel needs far fewer order conditions. The page covers Butcher's effective-order Runge–Kutta method, processed splittings and an explicit processor for highly oscillatory Strang splitting."
status: established
aliases: [effective order, processed method, conjugate method, kernel and processor, starting and finishing procedures, corrector]
tags: [splitting, order-conditions, geometric-integration, runge-kutta]
timestamp: 2026-10-19T12:00:00Z
---

# Processing and effective order

Let $\psi_h$ be a one-step map (the **kernel**) and $\pi_h$ a near-identity map (the
**processor**). The processed method is

$$\hat\psi_h=\pi_h\circ\psi_h\circ\pi_h^{-1},\qquad \hat\psi_h^{\,n}=\pi_h\circ\psi_h^{\,n}\circ\pi_h^{-1},$$

so $n$ steps cost one application of $\pi_h^{-1}$ at the start, $n$ kernel steps, and one
application of $\pi_h$ at each output time ([Blanes et al. 2024](/sources/blanes-2024.md),
§1.3, §4.5, Eqs. 4.17–4.18). The kernel has **effective order** $p$ if some processor makes
$\hat\psi_h$ of order $p$; the kernel itself need not have order $p$. Because many order
conditions can be satisfied by the processor, the kernel has to satisfy far fewer, and the
long-run accuracy is governed by the local error of $\hat\psi_h$, not of $\psi_h$ (§4.5).
Blanes et al. write the conjugation as $\pi_h^{-1}\circ\psi_h\circ\pi_h$; their $\pi_h$ is
the inverse of the one used here.

## Effective order of Runge–Kutta methods

The concept is Butcher's (1969). Ketcheson & Ranocha reproduce his effective-order-5
example with the B-series composition law
([Ketcheson & Ranocha 2023](/sources/ketcheson-2023.md), §2.3.2, Eqs. 24–25): a five-stage
explicit main method of classical order 4,

$$c=(0,\tfrac15,\tfrac25,\tfrac12,1),\quad a_{21}=\tfrac15,\ a_{32}=\tfrac25,\ a_{41}=\tfrac3{16},\ a_{43}=\tfrac5{16},\ a_{51}=\tfrac14,\ a_{53}=-\tfrac54,\ a_{54}=2,\quad b=(\tfrac16,0,0,\tfrac23,\tfrac16)$$

(other entries zero), with a starting and a finishing method, both five-stage explicit of
order 3 (tableaux in Eq. 25). The composition finishing∘main∘starting, computed with
[B-series](/definitions/b-series.md) and normalised step sizes, has order 5 (the package's
`order_of_accuracy` returns 4 for the main method and 5 for the composition). In the
notation above the starting method plays the role of $\pi_h^{-1}$ and the finishing method
that of $\pi_h$, each to the accuracy needed *(compiler reading, not stated in the
sources)*. Ketcheson & Ranocha check one composition of the three methods, not $n$ main
steps. Effective-order conditions can be written with the composition law
$B(b,B(a,y))=B(a\cdot b,y)$, which [BSeries.jl](/software/bseries-jl.md) evaluates
symbolically.

## Processed splitting and composition methods

For splittings, the effective-order conditions are written in the BCH coefficients of the
kernel (see [splitting order conditions](/results/splitting-order-conditions.md)), and the
logarithm of the processor has coefficients that are polynomials in them (Blanes et al.
2024, §4.5). Instances:

- **Lie–Trotter has effective order 2:** it is conjugate to Strang splitting through the
  half flow $\varphi^{[1]}_{h/2}$ (§1.3, Eq. 1.18; see
  [operator splitting](/methods/operator-splitting.md)). Yanenko's Crank–Nicolson
  splitting, first order, is likewise conjugate to a symmetric second-order composition
  (§6.1, Eq. 6.11).
- **Near-integrable problems:** processors give generalized order $(2k,2)$ (§4.5, as
  recalled from Wisdom et al. 1996, McLachlan 1996, Laskar & Robutel 2001); Table 8.5
  catalogues processed near-integrable methods such as P:2(6,4) and P:3(7,6,4).
- **Linear systems** $iu'=Hu$ (page-local $u$, $H$ a Hermitian matrix): processed versions use kernels of 19, 32 and 38 stages for
  orders 10, 16 and 20 (§3.4). A Strang-type method for the Schrödinger equation conjugate
  to a fourth-order method keeps its error bounded up to $t\approx2000$ with $h=1/20$
  (§1.6).
- **Path-integral Monte Carlo:** the Takahashi–Imada action
  $e^{-\epsilon T/2}e^{-\epsilon V-\frac{\epsilon^3}{24}[V,[T,V]]}e^{-\epsilon T/2}$
  (page-local imaginary-time step $\epsilon$, kinetic $T$, potential $V$) has effective
  order 4, whereas the primitive (Lie–Trotter) action has effective order 2 (§9, as
  recalled).
- **Modified potentials:** a processed sixth-order RKN method with all-positive
  coefficients exists for cubic potentials (§3.2, as recalled from Blanes et al. 2023),
  where classical sixth order would need negative ones
  ([negative-coefficient barrier](/results/negative-coefficient-barrier.md)).
- **Catalogue:** the processed kernels recommended in Table 8.1 are P:11-BCM06 (order 6),
  P:13-BCM06 (order 8) and P:23-BCM06 (order 10); Appendix A instead recommends kernels
  with $s=13,19,23$ for orders 6, 8, 10 (internal inconsistency of the version read; see
  [composition methods](/methods/composition-methods.md)).
- **Hamiltonian Monte Carlo:** symmetrically processed HMC integrators (§9.6, as recalled
  from Blanes et al. 2021).

## An explicit processor for highly oscillatory Strang splitting

Blanes et al. (2024, §5) analyse splittings of $y'=Ay+f^{[2]}(y)$ (page-local $A$: a linear
part whose flow $e^{tA}$ is $2\pi/\omega$-periodic; $f^{[2]}$ polynomial) uniformly in
$\omega$, i.e. for large $h\omega$, not only as $h\to0$. Expanding the exact and the Strang
flows to second order in $h$ with coefficients that depend on $h\omega$ (Eqs. 5.14–5.15),
they build a modified Hamiltonian for Strang, defined under the non-resonance conditions
$k\omega h/2\pi\notin\mathbb Z\setminus\{0\}$ and $(k+\ell)\omega h/2\pi\notin\mathbb Z\setminus\{0\}$
for the Fourier indices $k,\ell$ of the perturbation (page-local; Eqs. 5.31, 5.40). They
then construct a processor that removes the first-order terms: an explicit map of $2N+1$
rotations $\varphi^{[R]}$ by the angle $\vartheta=2\pi/(2N+1)$ interleaved with $2N$ kicks
$\varphi^{[K]}$ of strengths

$$b_j(h)=-b_{2N-j+1}(h)=\frac{2}{2N+1}\sum_{k=1}^{N}\frac1k\Big(\operatorname{sinc}(k\omega h/2)^{-1}-1\Big)\sin\frac{2kj\pi}{2N+1}$$

(page-local $N$, $\vartheta$; Eqs. 5.49–5.50, the source's contribution). The processed
Strang method has local error $O(h^2)$ only in the terms quadratic in the perturbation
(the source's $g'g$ terms) and modified Hamiltonian $H+O(h)$ (Eq. 5.47; page-local $H$
the Hamiltonian). On the pendulum with $(q_0,p_0)=(1/10,0)$, $h=5/6$,
$t\in[0,500]$, the processed Strang P(2,2) has far smaller energy error than Strang (2,2)
away from resonant steps; error spikes appear at $k\omega h/2\pi\in\mathbb Z$ for $k=2,4$,
and for the processed method also at $3h/2\pi\in\mathbb Z$ (§5.7, Figs. 5.1–5.2). The
explicit processor does not carry over to the quasi-periodic case (§5.8).

## Qualifications

- The processor acts only at output times (Blanes et al. 2024, Eq. 4.18), so the kernel
  values between outputs carry the kernel's own error, and output at every step pays the
  processor every step *(compiler remark, not in the sources)*.
- The oscillatory processor of §5 fails near resonant step sizes, where its constants blow
  up (Eqs. 5.44, 5.47).

# Citations

- [Blanes et al. (2024)](/sources/blanes-2024.md) — §1.3 (conjugate methods, Eq. 1.18), §1.6, §3.2, §3.4, §4.5 (Eqs. 4.17–4.18), §5.1–5.8 (oscillatory analysis, Eqs. 5.14–5.50, Figs. 5.1–5.2), §6.1 (Eq. 6.11), §8 (Tables 8.1, 8.5), §9, Appendix A.
- [Ketcheson & Ranocha (2023)](/sources/ketcheson-2023.md) — §2.3 (composition law, Eqs. 21–23), §2.3.2 (Butcher's effective-order-5 method, Eqs. 24–25).
