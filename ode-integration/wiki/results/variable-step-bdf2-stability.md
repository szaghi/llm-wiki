---
type: Result
title: "Stability of variable-step BDF2 under step-ratio bounds"
description: "Variable-step BDF2 is proved stable under bounds on the step ratios, and each bound secures a different estimate: zero-stability for ratios below 1 + sqrt 2 (sharp), a parabolic energy estimate for ratios up to 1.9398 (two multipliers), and robust Navier–Stokes error bounds under the ratio and ratio-variation hypotheses of García-Archilla and Novo."
status: established
aliases: [variable-step BDF2 stability, BDF2 step-ratio bound, BDF2 ratio restriction, 1.9398 bound]
tags: [linear-multistep, stability, step-size-control, implicit, stiff]
timestamp: 2026-10-20T16:00:00Z
---

# Stability of variable-step BDF2 under step-ratio bounds

With $h_n=t_{n+1}-t_n$ and step ratio $r_n=h_n/h_{n-1}$, variable-step
[BDF2](/methods/backward-differentiation-formula.md) reads

$$\frac{1+2r_n}{1+r_n}\,y_{n+1}-(1+r_n)\,y_n+\frac{r_n^2}{1+r_n}\,y_{n-1}=h_nf(t_{n+1},y_{n+1}).$$

On a uniform grid BDF2 is A-stable and [G-stable](/properties/g-stability.md). On nonuniform
grids its stability needs the step ratios to be bounded above. The sources prove several bounds,
**each for a different estimate**. They are not rival values of one constant, and a larger
bound in one row does not contradict a smaller one in another.

## The bounds and what they secure

| Ratio condition | What is proved | Problem class | Source |
|---|---|---|---|
| $r_n<1+\sqrt2\approx2.414$, sharp | [zero-stability](/definitions/zero-stability.md), i.e. stability for $h\to0$ on Lipschitz ODEs | nonstiff ODEs | recalled by [Akrivis et al. (2024)](/sources/akrivis-2024.md), §1.3, from Crouzeix–Lisbona, Grigorieff and Hairer–Nørsett–Wanner |
| $r_n\le(1+\sqrt3)/2\approx1.366$ | energy estimate without the mesh factor $e^{c\Gamma_n}$ | linear parabolic | Grigorieff, recalled by Akrivis et al. (2024), §1.3 |
| $r_n\le(2+\sqrt{13})/3\approx1.8685$ | energy estimate (1.4) with $e^{c\Gamma_n}$ | linear parabolic | Becker, recalled ibid. |
| $r_n\le1.9104$ | energy estimate | semilinear parabolic | Emmrich, recalled ibid. |
| $r_n\le r^\star\approx1.9398$ | energy estimate (1.4) with $e^{c\Gamma_n}$ | linear parabolic | Akrivis et al. (2024), Thm. 1.1 |
| ratios well above $1+\sqrt2$ | estimates of a different kind, with $(y_1-y_0)/h_0$ on the right-hand side | parabolic | Liao–Zhang and later works, recalled by Akrivis et al. (2024), §1.3 |
| $r_{\min}\le r_n\le r_{\max}\le R(a)$ and bounded $\sum_n(\lvert r_{n-1}-1\rvert+\lvert r_n-1\rvert)$ | viscosity-robust error bounds of order 2 in time | incompressible Navier–Stokes, IMEX and semi-implicit BDF2 | [García-Archilla & Novo (2023)](/sources/garciaarchilla-2023.md), Thms. 3–4 |

Here $\Gamma_n=\sum_{j=2}^{n-2}[r_j-r_{j+2}]_+$ (page-local; indices as in Akrivis et al.,
whose $r_j$ is the ratio of the step ending at $t_j$ to the one before). $\Gamma_n$ vanishes for
non-decreasing ratios. It stays bounded whenever the ratio sequence changes monotonicity a
bounded number of times, uniformly in the number of steps (§1.1). The bound $R(a)$ (page-local)
of García-Archilla & Novo depends on a free parameter $a\in[1,10]$: $R(1)>1.25$, $R(5)>2.12$,
$R(10)>2.61$, and larger $a$ enlarges the error constant (Eqs. (83)–(84), Remark 5).

## Theorem of Akrivis et al. (2024)

**Hypotheses.** $y'=Ly+g(t)$, with $-L$ self-adjoint and positive definite on a Hilbert space
and forcing $g$ (page-local), solved by variable-step BDF2 with arbitrary starting values
$y_0,y_1$ in the energy space.

**Conclusion** (Thm. 1.1). If all ratios satisfy $r_n\le r^\star\approx1.9398$, then

$$\lVert y_n\rVert^2+\sum_{j=2}^nh_{j-1}\lVert y_j\rVert_L^2\le Ce^{c\Gamma_n}\Big(\lVert y_0\rVert^2+\lVert y_1\rVert^2+h_1\lVert y_0\rVert_L^2+h_1\lVert y_1\rVert_L^2+\sum_{j=2}^nh_{j-1}\lVert g_j\rVert_{L,\star}^2\Big),$$

with $\lVert v\rVert_L=\lVert(-L)^{1/2}v\rVert$ and $\lVert v\rVert_{L,\star}=\lVert(-L)^{-1/2}v\rVert$
(page-local). The constants $C$ and $c$ are independent of the final time, of $L$, of $g$ and of
the partition. The theorem has no numerical experiments.

**Proof route.** The scheme is tested with the two multipliers $y_n-\mu_1y_{n-1}-\mu_2y_{n-2}$
(the source's $\delta$, $\eta$)
and the elliptic terms are summed before they are bounded. Uniform positive definiteness of the
resulting non-Toeplitz matrices reduces to positivity of a quadratic on $[-1,1]$; this is a
Grenander–Szegő variant (Lemma 2.1). The difference terms telescope under
$r\le r^\star(\mu_1,\mu_2)$ (Lemma 3.2), and the two conditions are optimized jointly (§4).
Details are on [multiplier energy technique](/methods/multiplier-energy-technique.md).

**Optimality.** The value
$r^\star\approx1.9398285699451$, at $\mu_1^\star\approx0.9672$ and $\mu_2^\star\approx-0.1793$,
is the best obtainable within the two-multiplier technique (§4). Within the same framework,
Emmrich's 1.9104 is optimal for one multiplier (Remark 3.1). The paper does not claim that
1.9398 is sharp for parabolic stability.

**Graded meshes.** For $t_i=(i/N)^\alpha$ with $\alpha>1$ (exponent page-local), the ratios
decrease to 1. So $r_i\le r^\star$ holds except for finitely many $i$, and $\Gamma_n$ is bounded
(§1.1).

## The Navier–Stokes analysis of García-Archilla & Novo (2023)

For inf-sup stable mixed finite elements with grad-div stabilization, García-Archilla & Novo
prove $\max_n\lVert u_h^n-u(t_n)\rVert=O(h^2_{\max}+\Delta x^{d_u}+\Delta x^{d_p+1})$ with
constants free of inverse powers of the viscosity $\nu$. Here $u$ is the velocity, $u_h^n$ its
discrete approximation, and $d_u$, $d_p$ are the polynomial degrees of the velocity and pressure
spaces; these symbols and $\nu$ are page-local, the registry's $\nu$ being the Courant number
(Thms. 3–4, Remark 6). Two
variants are covered:

- **Semi-implicit variant** (linearized convection): no restriction beyond a $\nu$-independent
  smallness of the steps.
- **IMEX variant** (explicit convection): additionally a CFL-type condition
  $h_n/\Delta x^2\lesssim\kappa$, with $\kappa$ (page-local) a free constant that enters the
  error constant exponentially (Eq. (86), Remark 5).

The variable-step argument is a perturbation of the constant-step G-form by the ratio variation;
see [G-stability](/properties/g-stability.md). The authors present it as the first analysis of
variable-step BDF2 for Navier–Stokes (§1, §5).

## Practical consequences

- **Staying inside the theory.** A BDF2 controller that caps the ratio at about 1.94 and does
  not let the ratios oscillate so that $\Gamma_n$ grows stays within the hypotheses of Thm. 1.1;
  the bound is sufficient, not shown necessary *(compiler inference from Akrivis et al. 2024,
  Thm. 1.1 and §1.1; the source gives no controller advice)*. See
  [step-size control](/methods/step-size-control.md).
- **Theory and computation can diverge.** García-Archilla & Novo's adaptive runs use a
  controller with no explicit ratio limiter, and they do not check their ratio hypotheses
  (§4, Fig. 8). Their theory therefore does not formally cover their computations.

## Qualifications

- **Different norms and hypotheses.** The zero-stability bound concerns nonstiff ODEs with a
  Lipschitz right-hand side. The parabolic bounds concern energy estimates uniform in the
  stiffness. The Liao–Zhang-type bounds concern estimates with a different right-hand side, and
  García-Archilla & Novo's bounds concern Navier–Stokes error estimates. A statement that
  "variable-step BDF2 is stable for ratios below X" is incomplete without the estimate it refers
  to.
- **Version read.** García-Archilla & Novo (2023) was read as arXiv v1; Akrivis et al. (2024)
  as the version of record.
- **Printed value.** $\min p\approx7.3592\cdot10^{-6}$ (Akrivis et al. 2024, p. 12) is evaluated
  at the rounded ratio 1.9398. At the exact bound it is about $7.107\cdot10^{-6}$; both exceed the
  constant $10^{-6}$ that is used, so the result is unaffected *(compiler check)*.

# Citations

- [Akrivis et al. (2024)](/sources/akrivis-2024.md) — §1.1 (Eq. (1.5), $\Gamma_n$, graded meshes), §1.3 (history of ratio bounds, zero-stability), Thm. 1.1 (Eq. (1.4)), Lemmas 2.1, 3.2–3.3, Remark 3.1, §4 (Eq. (4.17)).
- [García-Archilla & Novo (2023)](/sources/garciaarchilla-2023.md) — §1, Lemma 7, Thms. 3–4 (Eqs. (83)–(89)), Remarks 5–6, §4 (Fig. 8), §5.
