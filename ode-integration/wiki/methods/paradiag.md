---
type: Method
title: "ParaDiag: diagonalization-based parallel-in-time methods"
description: "ParaDiag writes all time steps of a linear implicit scheme as one space-time system and diagonalizes its time matrix, so that the steps decouple into independent shifted spatial solves. Gander and Palitta keep the circulant-plus-low-rank structure of backward Euler and BDF exactly via Sherman–Morrison–Woodbury and a Krylov capacitance solve."
status: established
aliases: [ParaDiag, all-at-once method, diagonalization-based PinT, alpha-circulant preconditioner, circulant preconditioning, space-time matrix equation]
tags: [parallel, linear-algebra, implicit, stiff]
timestamp: 2026-10-20T03:57:00Z
---

# ParaDiag: diagonalization-based parallel-in-time methods

**ParaDiag** methods solve all $N$ steps of an implicit time discretization of a
linear problem at once; each step is one time slice, so here $\Delta T=h$. For $y'=Ly+g(t)$ with $-L$ the stiffness matrix of a
spatial discretization and backward Euler with constant step $h$, the
**all-at-once system** is the matrix equation

$$(I-hL)\,Y-Y\,\Sigma^\top=\big[y_0+hg_1,\;hg_2,\;\dots,\;hg_N\big],\qquad Y=[y_1,\dots,y_N],$$

where $\Sigma\in\mathbb R^{N\times N}$ (page-local) is zero except for ones on the first
subdiagonal ([Gander & Palitta (2024)](/sources/gander-2024.md), §1, Eq. (1.2), after
Palitta 2021). If the time matrix were diagonal in some basis, a transform in time would
decouple the system into $N$ independent spatial solves, one per process. $\Sigma$ is a
Jordan block and not diagonalizable; the members of the family differ in how they get
around this (§1):

- **variable steps** make the time matrix diagonalizable (Maday–Rønquist), at the price of
  ill-conditioned eigenvector matrices that "can potentially pollute the entire solution
  process, especially for fine time grids" (as recalled);
- **circulant preconditioning** replaces $\Sigma$ by the circulant matrix $C_1$ that
  completes it, diagonalized by the FFT, inside a GMRES iteration on the full system
  (McDonald–Pestana–Wathen, as recalled), or uses an $\alpha$-circulant variant;
- **interpolation and low-rank updates** (Ev-Int, Kressner–Massei–Zhu, as recalled);
- **ParaDiag inside other PinT methods**: periodic approximations combined with
  [Parareal](/methods/parareal.md) or MGRIT, and nonlinear ParaDiag (as recalled).

ParaDiag is the all-at-once branch of
[parallel-in-time integration](/methods/parallel-in-time-integration.md).

## The Sherman–Morrison–Woodbury ParaDiag of Gander & Palitta

**Circulant plus rank one.** $\Sigma=C_1-e_1e_N^\top$, and $C_1=\mathcal D^{-1}\Omega\,\mathcal D$
with $\mathcal D$ the discrete Fourier transform and $\Omega=\mathrm{diag}(\omega_1,\dots,\omega_N)$
its eigenvalues, the $N$-th roots of unity (page-local symbols; Eq. (2.1), Appendix). Earlier
circulant methods drop the rank-one term; Gander & Palitta keep it **exactly**. After the
transform in time, the system matrix is $P+UV^\top$ with the block-diagonal part

$$P=\mathrm{blkdiag}\big((1-\omega_i)I-hL\big)_{i=1}^N$$

and a correction of rank $d$, the dimension of $y$ (the number of spatial unknowns), so the Sherman–Morrison–Woodbury
formula gives the solution through $P^{-1}$ and the inverse of a $d\times d$
**capacitance matrix**

$$S_N=I+\sum_{i=1}^N \gamma_i\big((1-\omega_i)I-hL\big)^{-1},\qquad \gamma_i=\omega_i/N$$

(page-local symbols, $\gamma_i$ as in the source; §2, Eqs. (2.3)–(2.6), and Appendix, which derives $\gamma_i=\omega_i/N$ from the transformed $e_N$, with the same eigenvalue ordering as $\Omega$). Applying $P^{-1}$ is $N$ independent complex
shifted solves, one per process.

**Algorithm 2.1.** (i) transform the right-hand side in time; (ii) solve the $N$ shifted
systems in parallel; (iii) form the right-hand side of the capacitance system; (iv) solve
the capacitance system; (v) apply $P^{-1}$ once more in parallel; (vi) transform back.
Forming $S_N$ explicitly would need $P^{-1}$ on $d$ columns, so step (iv) uses a
projection method: a FOM-like Galerkin method on the polynomial Krylov space
$\mathrm{span}\{b,Lb,\dots,L^{m-1}b\}$ of $L$ (not of $S_N$). Shift invariance of the
Arnoldi relation gives cheap reduced systems for all $N$ shifts, and each residual check
costs one parallel-in-time loop (§3, Alg. 3.1, Eqs. (3.3)–(3.5)). The iterate is the
Lanczos approximation of a rational function of $L$ applied to $b$, so a-priori error
bounds could fix the Krylov dimension in advance (§3).

**Theorem 3.1 (conditioning).** If $-L$ is symmetric positive definite, $S_N$ is Hermitian
positive definite for every $N\ge1$ and

$$\operatorname{cond}(S_N)\le1+\frac{1}{h\,\lambda_{\min}(-L)}$$

(Eq. (3.6), proof in the Appendix). Convergence of the inner solve is fast for large
$h\lambda_{\min}(-L)$, i.e. coarse time grids, and can need many iterations for very fine
time grids (§3). For the 2D heat equation with the five-point Laplacian the bound is
$13.97$, $26.94$, $52.88$ for $N=256$, $512$, $1024$, independent of the spatial size, and
a single Galerkin iteration reaches a relative residual below $10^{-8}$; the spectrum of
$S_N$ lies in $[1,1.004]$ (§6.1, Table 6.1).

## $\alpha$-circulant acceleration

Writing $\Sigma=C_\alpha-\alpha e_1e_N^\top$ with the $\alpha$-circulant $C_\alpha$
(corner entry $\alpha\in(0,1]$, page-local), diagonalized by the scaled transform
$\mathcal D\,\mathcal D_\alpha$ with $\mathcal D_\alpha=\mathrm{diag}(1,\alpha^{1/N},\dots,\alpha^{(N-1)/N})$,
the low-rank correction acquires the weight $\alpha^{1/N}$ and the capacitance matrix
becomes $I+\alpha^{1/N}\sum_i\gamma_i((1-\omega_i)I-hL)^{-1}$, a small perturbation of the
identity for $\alpha\ll1$ (§4, Eqs. (4.1)–(4.3)). The price is the condition number
$\operatorname{cond}(\mathcal D\mathcal D_\alpha)=\alpha^{-(N-1)/N}$: the error of the
computed solution grows proportionally, so $\alpha$ trades the size of the correction
against round-off, a choice the authors call "not an easy task" (§4). The same drawback
affects variable-step ParaDiag, as they acknowledge.

**Algorithm 4.1** first computes the direct $\alpha$-circulant part $Y_1$ (one
parallel-in-time loop) and returns it if its residual is small enough; otherwise it adds
the Sherman–Morrison–Woodbury correction $Y_2$. On a 2D advection–diffusion problem (one
Galerkin iteration, $N=64$), the residual of $Y_1+Y_2$ and its error scale like
$\alpha^2$ and that of $Y_1$ alone like $\alpha$; below $\alpha\approx10^{-4}$ the error
grows because of the conditioning (§6.2, Fig. 6.1).

## Extension to BDF

For [BDF$k$](/methods/backward-differentiation-formula.md), $k\le6$, the time matrix is
banded lower-triangular Toeplitz, a circulant minus a rank-$k$ term built from the BDF
coefficients, and the same approach applies with a $kd\times kd$ capacitance matrix solved
by a block Galerkin method on a block Krylov space (§5, Eqs. (5.1)–(5.6), Prop. 5.1). The
authors print the BDF coefficients with signs flipped relative to Hairer–Wanner so that
$-Y\Sigma^\top$ appears (Table 5.1). No experiment uses $k>1$.

## Numerical comparison

On 2D advection–diffusion with a recirculating wind (spatial sizes $16\,384$ and $65\,536$,
$N\in\{32,64,128\}$, viscosity $10^{-1}$ to $10^{-3}$), counted in parallel-in-time loops
(#PinT):

| method | #PinT | relative residuals |
|---|---|---|
| Alg. 4.1, $\alpha=10^{-4}$ | 3 | $3.99\cdot10^{-13}$ to $3.42\cdot10^{-10}$ |
| circulant-preconditioned GMRES | 5 | $4.51\cdot10^{-14}$ to $2.13\cdot10^{-10}$ |
| Ev-Int ($r=2$) | 2 | $2.23\cdot10^{-12}$ to $8.58\cdot10^{-11}$ |

(§6.3, Table 6.2). Iteration counts of Alg. 4.1 and GMRES are robust in size, $N$ and
viscosity; the accuracy of Alg. 4.1 improves as the viscosity decreases, while that of
GMRES generally worsens. At one parallel loop, Alg. 4.1 ($Y_1$ with $\alpha=10^{-6}$) is
"often three orders of magnitude more accurate" than Ev-Int with $r=1$ (Table 6.3). The
authors concede that careful tuning of Ev-Int's parameters may improve it.

## Qualifications

- **Cost is counted, not timed.** All runs were on a laptop, the block solves were applied
  sequentially, and no parallel implementation exists; #PinT is proposed as the fair cost
  measure (§6). One #PinT means $N$ complex shifted solves in Alg. 4.1 and in GMRES alike,
  but the Arnoldi products with $L$ inside the Galerkin solve are sequential in time.
- **Proof of Theorem 3.1.** The Appendix proof has gaps *(compiler check of Eq. (7.1),
  not in the source)*: one step treats $\mathrm{Re}(\gamma_iw)$ as
  $\mathrm{Re}(\gamma_i)\mathrm{Re}(w)$ for complex $\gamma_i$ and quadratic forms $w$, writes a
  minimum of a sum as a sum of minima with equality, and then evaluates every term at
  $\lambda_{\max}$ regardless of the sign of $\mathrm{Re}(\omega_i)$.
  The statement is plausible, since $S_N$ is a real rational function of $L$ and can be
  checked eigenvalue by eigenvalue, and it stays attributed to Gander & Palitta; the printed
  argument is not complete.
- **Scope of the theorem.** Theorem 3.1 covers symmetric positive definite $-L$ only; the
  comparisons of Tables 6.2–6.3 use the nonsymmetric advection–diffusion operator, for
  which no convergence theory is given.
- **BDF.** The extension has no numerical test, and BDF$k$ for $k\ge3$ is not A-stable,
  which the paper does not discuss. The claim that the scheme parallelizes Runge–Kutta
  methods relies on a cited reference (§7).
- **Printed slips.** The shifted Arnoldi relation and Eqs. (3.3)–(3.5) miss a factor $h$
  on the last term; Alg. 3.1 drops the weights $\gamma_i$ in its residual line, which Eq. (3.5)
  has; the GMRES preconditioner of §6.3 is printed with $+$ where the circulant
  approximation has $-$ (recorded on the Source page).
- **Version read.** arXiv v2 (23 Sep 2023), not the SIAM version of record.

# Citations

- [Gander & Palitta (2024)](/sources/gander-2024.md) — arXiv v2: §1 (Eq. (1.2)); §2 (Eqs. (2.1)–(2.6), Alg. 2.1); §3 (Alg. 3.1, Eqs. (3.3)–(3.6), Thm. 3.1); §4 (Eqs. (4.1)–(4.3), Alg. 4.1); §5 (Eqs. (5.1)–(5.6), Table 5.1, Prop. 5.1); §6 (Tables 6.1–6.3, Fig. 6.1); §7; Appendix.
