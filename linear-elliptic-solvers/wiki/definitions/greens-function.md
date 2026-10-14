---
type: Definition
title: "Green's function"
description: "Response G(r, r') of a linear operator to a unit point source, L G = delta(r - r'), obeying the problem's homogeneous boundary conditions, so that u = integral of G f solves L u = f; symmetry G(r,r') = conj G(r',r), the one-dimensional construction from two homogeneous solutions, the fundamental solutions of the Laplace, Helmholtz and modified Helmholtz operators, and the split G = G_0 + H."
status: established
aliases: [Green function, fundamental solution, free-space Green's function, point-source solution, isolated boundary conditions, Wronskian construction, spherical Green's function]
tags: [greens-function, poisson, operator-theory]
timestamp: 2026-10-14T00:00:00Z
---

# Green's function

**Definition.** For a linear operator $\mathcal L$ and homogeneous boundary
conditions on $\partial\Omega$, the Green's function solves
$$\mathcal L_{\mathbf r}G(\mathbf r,\mathbf r')=\delta(\mathbf r-\mathbf r'),\qquad\mathbf r'\in\Omega\quad\text{(eq. 21.77)},$$
with $\mathcal L$ acting on $\mathbf r$, and obeys the same boundary
conditions. It is the response to a unit point source at $\mathbf r'$, and
$$u(\mathbf r)=\int_\Omega G(\mathbf r,\mathbf r')f(\mathbf r')\,\mathrm dV(\mathbf r')\quad\text{(eq. 21.78)}$$
solves $\mathcal Lu=f$ under those conditions
([Riley et al. (2006)](/sources/riley-2006.md), §21.5.1, pp. 752–753; the
one-dimensional form is §17.5). [Arfken et al. (2013)](/sources/arfken-2013.md)
give the same definition and the same superposition integral, in one
dimension and in two or three (§10.1, eqs. 10.6–10.7, p. 448; §10.2,
items 1–2, p. 459). Inhomogeneous boundary conditions are
handled either by a change of variable that moves them into the equation
(both books; in one dimension, Arfken et al. subtract the linear function
taking the boundary values, p. 452),
or directly by the [representation formula](/results/greens-representation-formula.md).

**Sign convention.** Both books define $G$ by $+\delta$, as the registry
does. Arfken et al. warn that "some texts (including previous editions of
this book)" define $G$ by $-\delta$, so that $1/(4\pi\lvert\mathbf r-\mathbf r'\rvert)$
goes with $+\nabla^2$ without a minus sign, and that the sign of $G$
always follows the sign of the operator it inverts; physical results are
unaffected because the integral against the source changes sign with it
(p. 462). Their opening example is of that kind: for the electrostatic Poisson
equation written with $-\nabla^2$ and the charge density (over the vacuum
permittivity) on the right, the kernel is the positive Coulomb kernel
$1/(4\pi\lvert\mathbf r-\mathbf r'\rvert)$ divided by the permittivity
(eqs. 10.1–10.3, p. 447). Their reading list adds that Morse & Feshbach often use a source
$4\pi\delta$ (p. 467).

**Symmetry.** For Hermitian $\mathcal L$ the
[eigenfunction series](/methods/eigenfunction-expansion.md) gives
$G(\mathbf r,\mathbf r')=\overline{G(\mathbf r',\mathbf r)}$, a real $G$
being symmetric; the book states that this holds "irrespective of how it is
found" (p. 753). Arfken et al. prove it without the series: for a
Hermitian problem, $\langle G(\cdot,\mathbf r'),\mathcal LG(\cdot,\mathbf r)\rangle=\langle\mathcal LG(\cdot,\mathbf r'),G(\cdot,\mathbf r)\rangle$,
and the delta functions reduce the two sides to $\overline{G(\mathbf r,\mathbf r')}$
and $G(\mathbf r',\mathbf r)$ (eqs. 10.34–10.36, p. 460; the
eigenfunction-series route is eqs. 10.14–10.15, p. 450). Without
Hermiticity the symmetry is lost: the Green's function of an initial-value
problem, e.g. $u''+u=f$ with $u(0)=u'(0)=0$, is $G=0$ for $x<x'$ and
$\sin(x-x')$ for $x>x'$ — causal, not symmetric (Example 10.1.2,
pp. 453–454).

**Regularity** (Arfken et al., p. 460). In two and three dimensions $G$ is
continuous and differentiable away from $\mathbf r=\mathbf r'$, may be
infinite at that point, and its first derivatives must be singular enough
for the second derivatives in $\mathcal L$ to produce the delta function.

## One dimension: construction from two homogeneous solutions

For $\mathcal Lu=-(pu')'+qu=f$ on $[a,b]$ (registry sign; Arfken et al.
write $(pu')'+qu$, so their $p$ is the registry's $-p$) with one
homogeneous condition at each end, Arfken et al. derive (§10.1, eqs.
10.8–10.19, pp. 449–451):

* $G$ is continuous at $x=x'$, and integrating $\mathcal LG=\delta$ across
  $x'$ gives the jump
  $$\partial_xG\big|_{x=x'^+}-\partial_xG\big|_{x=x'^-}=-\frac{1}{p(x')}$$
  (eq. 10.9; $+1/p$ in the book's sign).
* With $u_a$, $u_b$ solving $\mathcal Lu=0$ and satisfying the condition
  at $a$, respectively at $b$, and taken real,
  $$G(x,x')=-\frac{1}{p\,\mathcal W}\begin{cases}u_a(x)\,u_b(x'),&x<x',\\ u_b(x)\,u_a(x'),&x>x',\end{cases}\qquad\mathcal W=u_au_b'-u_a'u_b,$$
  where $p\mathcal W$ is constant (the book quotes the Wronskian identity
  from its unread Ch. 7) (eqs. 10.18–10.19; the constant prefactor is
  written here with the registry sign).
* Direct differentiation confirms that $u=\int_a^bGf\,\mathrm dx'$ meets
  both boundary conditions and solves $\mathcal Lu=f$ (eqs. 10.20–10.23).
* Example: $-u''=f$, $u(0)=u(1)=0$ gives $G=x(1-x')$ for $x<x'$ and
  $x'(1-x)$ for $x>x'$ (Example 10.1.1, p. 452). An outgoing-wave condition
  for $u''+\kappa^2u=f$ gives $G=-\frac{\mathrm i}{2\kappa}\mathrm e^{\mathrm i\kappa\lvert x-x'\rvert}$
  (Example 10.1.3, eq. 10.28, p. 454).
* If $u_a$ and $u_b$ are linearly dependent, as for Legendre's operator
  with boundedness at $\pm1$, no Green's function can be built this way
  (exercise 10.1.6, p. 457). *Compiler's gloss (hypothesis):* a common
  solution meeting both conditions is an eigenfunction with eigenvalue 0,
  the case in which the eigenfunction series (eq. 10.14) also fails.

**Integral-equation form.** With $G$ for $\mathcal L$ and its boundary
conditions, the eigenproblem $\mathcal Lu=\lambda u$ is equivalent to
$u(x)=\lambda\int_a^bG(x,x')u(x')\,\mathrm dx'$, the boundary conditions
now carried by the kernel; Arfken et al. prove both directions and note that
the integral operator is bounded while the differential operator is not
(eqs. 10.29–10.32, pp. 455–456).

## Fundamental solutions of the Laplacian

With $\nabla^2G_0=\delta(\mathbf r-\mathbf r')$ (registry sign convention;
both books derive the forms below by integrating over a ball about
$\mathbf r'$ and applying the divergence theorem — Arfken et al., eqs.
10.40–10.44, pp. 461–462):

* $d=3$, decaying at infinity:
  $$G_0(\mathbf r,\mathbf r')=-\frac{1}{4\pi\lvert\mathbf r-\mathbf r'\rvert}\quad\text{(eq. 21.90)},$$
  derived from spherical symmetry and the divergence theorem on a sphere
  about $\mathbf r'$. It is the full Green's function for the condition
  $u\to0$ as $\lvert\mathbf r\rvert\to\infty$ — the free-space (isolated)
  problem — and yields $u(\mathbf r')=-\frac{1}{4\pi}\int f(\mathbf r)\lvert\mathbf r-\mathbf r'\rvert^{-1}\,\mathrm dV(\mathbf r)$
  over all space, which for an electrostatic charge distribution is the
  familiar Coulomb potential (eq. 21.91, pp. 757–758).
* $d=2$:
  $$G_0(\mathbf r,\mathbf r')=\frac{1}{2\pi}\ln\lvert\mathbf r-\mathbf r'\rvert+\text{const}\quad\text{(eq. 21.93)};$$
  it cannot be made to vanish at infinity, so the constant is not
  necessarily zero (p. 758). Arfken et al. give it without the constant,
  call it "a fundamental 2-D Green's function" although it is infinite at
  infinity, and add the one-dimensional form $\tfrac12\lvert x-x'\rvert$; in
  one and two dimensions the boundary condition is left "arbitrary"
  (eq. 10.44, p. 462; table 10.1, p. 463).

**Helmholtz and modified Helmholtz** (Arfken et al., table 10.1, p. 463;
stated, the three-dimensional entries left to exercises 10.2.4 and 10.2.6).
Outgoing-wave condition for $\nabla^2+\kappa^2$, decay at infinity for
$\nabla^2-\kappa^2$:

| $d$ | $\nabla^2+\kappa^2$ | $\nabla^2-\kappa^2$ |
|---|---|---|
| 1 | $-\frac{\mathrm i}{2\kappa}\mathrm e^{\mathrm i\kappa\lvert x-x'\rvert}$ | $-\frac{1}{2\kappa}\mathrm e^{-\kappa\lvert x-x'\rvert}$ |
| 2 | $-\frac{\mathrm i}{4}H_0^{(1)}(\kappa\lvert\mathbf r-\mathbf r'\rvert)$ | $-\frac{1}{2\pi}K_0(\kappa\lvert\mathbf r-\mathbf r'\rvert)$ |
| 3 | $-\frac{\mathrm e^{\mathrm i\kappa\lvert\mathbf r-\mathbf r'\rvert}}{4\pi\lvert\mathbf r-\mathbf r'\rvert}$ | $-\frac{\mathrm e^{-\kappa\lvert\mathbf r-\mathbf r'\rvert}}{4\pi\lvert\mathbf r-\mathbf r'\rvert}$ |

The $\pm\kappa^2$ term does not alter the singularity at $\mathbf r=\mathbf r'$
(exercise 10.2.3, p. 466).

**Multipole expansion.** In spherical coordinates the three-dimensional
fundamental solution separates into a two-region radial factor times
Legendre polynomials,
$$-\frac{1}{4\pi\lvert\mathbf r-\mathbf r'\rvert}=-\frac{1}{4\pi}\sum_{l=0}^{\infty}\frac{r_<^{\,l}}{r_>^{\,l+1}}P_l(\cos\chi),$$
which Arfken et al. write as $\sum_l\frac{2l+1}{4\pi}g_l\,P_l(\cos\chi)$
with the "spherical Green's function" $g_l=-r_<^{\,l}/[(2l+1)r_>^{\,l+1}]$
(pp. 463–464; derived in their unread Ch. 16). A cylindrical analogue with
modified Bessel functions is quoted from Ch. 14 (p. 464). Its use in fast
solvers is not discussed.

**Split.** A Green's function for a bounded region is sought as
$G=G_0+H$, $G_0$ carrying the singularity at $\mathbf r'$ and $H$ harmonic
($\nabla^2H=0$) in $\Omega$ and chosen to meet the boundary condition
(pp. 756–757). The [method of images](/methods/method-of-images.md)
constructs $H$ from sources outside $\Omega$. Arfken et al. state the same
strategy — start from a Green's function for convenient boundary
conditions and add a solution of the homogeneous equation, which leaves the
singularity untouched (p. 461) — and illustrate it in one dimension:
$\tfrac12\lvert x-x'\rvert-\tfrac12(x+x')+xx'$ is the Dirichlet Green's
function of $\mathrm d^2/\mathrm dx^2$ on $[0,1]$ (Example 10.2.1, p. 464),
the negative of the one for $-\mathrm d^2/\mathrm dx^2$ above.

The free-space Green's function as the kernel of a fast convolution solver
(FFT or multipole) is not treated in either source.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §17.5 (pp. 569–570),
  §21.5.1 (pp. 752–753), §21.5.3 (pp. 756–758).
* [Arfken et al. (2013)](/sources/arfken-2013.md), Ch. 10 introduction
  (pp. 447–448), §10.1 (pp. 448–458), §10.2 (pp. 459–466), Additional
  Readings (p. 467).
