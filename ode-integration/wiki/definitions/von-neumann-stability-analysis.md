---
type: Definition
title: "Von Neumann (Fourier) stability analysis of fully discrete schemes"
description: "Fourier analysis of a fully discrete space–time scheme for a linear constant-coefficient problem on a uniform periodic grid: the amplification factor or matrix per wavenumber and the critical Courant number; it differs from method-of-lines stability-region analysis whenever the time scheme is not a Runge–Kutta method applied to a fixed semi-discretization."
status: established
aliases: [von Neumann analysis, Fourier stability analysis, Fourier analysis, amplification factor, amplification matrix, von Neumann criterion, critical CFL number, Fourier CFL number]
tags: [stability, explicit, lax-wendroff, verification]
timestamp: 2026-10-20T10:00:00Z
---

# Von Neumann (Fourier) stability analysis of fully discrete schemes

Apply a fully discrete scheme to a linear constant-coefficient PDE on a uniform
periodic grid with mesh width $\Delta x$, and insert a single Fourier mode
$u_j^n=W^n e^{\mathrm i\kappa x_j}$ (page-local: $u_j^n$ the grid values, $\kappa$ the
wavenumber, $W^n$ the mode amplitude). Translation invariance makes one step a
multiplication, $W^{n+1}=g(\kappa)W^n$, by the **amplification factor** $g$; a scheme with
several unknowns per cell (DG, flux reconstruction) gives an **amplification matrix**
$H(\nu,\kappa)$ acting on the cell's coefficient vector. The **von Neumann condition**
asks $\lvert g(\kappa)\rvert\le1$, or spectral radius $\rho(H)\le1$, for all
$\kappa\Delta x\in[-\pi,\pi]$. For an explicit scheme this holds up to a **critical
Courant number** $\nu^*$ (registry $\nu$; the sources write $\sigma$), the CFL limit of the
scheme ([Chouchoulis et al. 2022](/sources/chouchoulis-2022.md), §5, Prop. 1;
[Babbar et al. 2022](/sources/babbar-2022.md), §6).

## How the sources compute it

- **Scalar amplification factor.** For the multiderivative Runge–Kutta–Lax–Wendroff
  schemes of Chouchoulis et al. (2022, Prop. 1, Eqs. (21)–(22)), with linear flux
  $a u$ and $\nu=ah/\Delta x$, the stage and step factors obey the same recursion as the
  stages,
  $$g^{(l)}(\kappa)=1+\sum_{k=1}^{r}(-\nu)^k\,\hat P^{(k)}(\kappa)\sum_{j<l}a^{(k)}_{lj}\,g^{(j)}(\kappa),\qquad g(\kappa)=1+\sum_{k=1}^{r}(-\nu)^k\,\hat P^{(k)}(\kappa)\sum_{l}b^{(k)}_l\,g^{(l)}(\kappa),$$
  where $\hat P^{(k)}(\kappa)=\sum_{j=-\mathsf p}^{\mathsf p}\delta^k_je^{\mathrm ij\kappa\Delta x}$
  is the Fourier symbol of the centred $k$-th derivative stencil and $a^{(k)}_{lj}$,
  $b^{(k)}_l$ are the $k$-th derivative coefficients of the $r$-derivative method
  (page-local; see [multiderivative Runge–Kutta](/methods/multiderivative-runge-kutta.md)).
  $\nu^*$ is found by bisection on $\nu$, with $\max\lvert g\rvert$ over 1000 uniform
  samples of $\kappa\in[-\pi,\pi]$, to four decimals (Table 2).
- **Amplification matrix.** For Lax–Wendroff flux reconstruction, the cell update
  couples the cell to its neighbours through fixed matrices, and
  $H(\nu,\kappa)=I-\nu A_0-\nu A_{-1}e^{-\mathrm i\kappa}-\nu A_{+1}e^{\mathrm i\kappa}$
  ($A_{-1}$, $A_0$, $A_{+1}$ page-local; for $a>0$ with the D2 face flux, which is exactly
  upwind, $A_{+1}=0$ and Babbar et al.'s Eq. (11) has only the left neighbour); $\nu^*$ is
  the largest $\nu$ with
  $\max_\kappa\rho(H)\le1$, again by sampling $\kappa$. In 2-D a Kronecker
  renumbering gives $H(\nu_1,\nu_2,\kappa_1,\kappa_2)$ (Babbar et al. 2022, §6, App. B;
  numbers on [Lax–Wendroff flux reconstruction](/methods/lax-wendroff-flux-reconstruction.md)).
- **Unconditional stability thresholds.** [Tan et al. (2022)](/sources/tan-2022.md)
  (§3, Lemmas 3.1–3.2) test $\lvert g\rvert\le1+10^{-10}$ (finite differences) or the
  spectral radius of a uniformly diagonalizable $3\times3$ amplification matrix
  ($P^2$ local DG) on a sample of wavenumbers and step ratios, to find the smallest
  stabilizing coefficient of the [explicit–implicit–null method](/methods/explicit-implicit-null-method.md).
  [Caliari et al. (2024)](/sources/caliari-2024.md) (§2) do the same per Fourier mode of
  the heat equation, where the factor is a closed-form two-parameter
  [stability function](/definitions/stability-function.md).

The numbers are sharp where tested: linear advection with LWFR blows up for steps slightly
above the computed limit (Babbar et al. 2022, §6), and the EIN threshold 0.54 separates
convergent from divergent runs at 0.53 (Tan et al. 2022, Tables 4.1–4.2).

## Contrast with method-of-lines stability regions

In the method-of-lines approach the semi-discretization $y'=Ly$ is fixed first, and an
ODE integrator with stability function $R$ is stable if $h\lambda\in\mathcal S$ for every
eigenvalue $\lambda$ of $L$ (see [stability function](/definitions/stability-function.md)).
On a uniform periodic grid the eigenvalues of $L$ are the values of its Fourier symbol, so
for a Runge–Kutta method the amplification factor is $R$ evaluated at the symbol and the
two analyses agree *(compiler remark, not in the sources)*. This is how
[Hedayati Nasab et al. (2021)](/sources/hedayatinasab-2021.md) use a "multidimensional von
Neumann analysis": to obtain the semi-discrete spectrum of flux-reconstruction DG over all
wavenumbers and directions, which then defines the target set of an
[optimal stability polynomial](/methods/optimal-stability-polynomial.md).

The two analyses part when the time scheme is not a Runge–Kutta method applied to one
fixed semi-discretization. In Lax–Wendroff, Taylor and multiderivative schemes for PDEs
the higher time derivatives are replaced by discrete space operators, and a product of
two discrete derivative stencils is not the stencil of the higher derivative:
$\hat P^{(i)}\hat P^{(j)}\ne\hat P^{(i+j)}$. The fully discrete factor is then not
$R(-\nu\hat P^{(1)})$. Chouchoulis et al. (2022, §5, Fig. 1, Table 2) conclude that "a
method of lines (MOL) viewpoint is inadequate": among their six schemes the ODE
stability region of 3DRK7-3 looks the largest, yet its fully discrete critical Courant
number is the smallest (0.2300), and two-derivative schemes beat three- and
four-derivative ones (up to 1.4718 for 2DRKCAT4-2, against 1 for the original
compact approximate Taylor method). In LWFR the temporal operator is built from the
element-local derivative matrix and the interface correction acts once per step, so the
same caveat applies (see [Lax–Wendroff flux reconstruction](/methods/lax-wendroff-flux-reconstruction.md)).
[Han Veiga et al. (2021)](/sources/hanveiga-2021.md) (§5.1) leave von Neumann analysis of
their [ADER](/methods/ader-time-integration.md) and [DeC](/methods/deferred-correction.md)
discretizations to future work, because CFL bounds depend on the spatial discretization.

## Scope and limits

- **Linear, constant coefficients, uniform periodic grid.** Babbar & Chandrashekar
  ([2025](/sources/babbar-2025.md), §5) note that the analysis does not apply to
  curvilinear meshes, where a CFL formula built on the Fourier number "need not guarantee
  $L^2$ stability"; they replace it by error-based step-size control.
- **Necessary, not always sufficient.** For a uniformly diagonalizable amplification
  matrix, spectral radius at most one gives stability (Tan et al. 2022, Lemma 3.2). For
  non-normal matrices eigenvalue conditions are only necessary (see
  [strong stability](/properties/strong-stability.md)).
- **Nonlinear problems.** The linear limit does not settle nonlinear behaviour. The
  compact approximate Taylor schemes with $\mathsf p=4,5,6$ are linearly stable up to
  Courant number 1 yet diverge on smooth Burgers data at $\nu=0.5$ (Chouchoulis et al.
  2022, §6.1). Conversely, Chouchoulis et al. run all their smooth tests except one at
  $\nu=0.5$, above their own linear limits for 3DRKCAT5-2 (0.4275) and 3DRKCAT7-3
  (0.2300), and both schemes converge; the paper does not comment, and only 3DRKCAT7-3
  diverges, on a nonlinear Euler case at coarse meshes (§6.3). Their $\nu$ in §6 is based
  on the maximal eigenvalue of the flux Jacobian, not on a constant advection speed.
- **Boundaries.** A global spectral analysis that includes interface or boundary
  pollution, as for the overlapping-subdomain scheme on
  [local time stepping](/methods/local-time-stepping.md), is a different, non-periodic
  analysis.
- **Name clash.** "Von Neumann's lemma" on [A-stability](/properties/a-stability.md)
  and [strong stability](/properties/strong-stability.md) (A-stability implies
  $\lVert R(hL)\rVert\le1$ for seminegative $L$) is a different result, unrelated to
  Fourier analysis.

# Citations

- [Chouchoulis et al. (2022)](/sources/chouchoulis-2022.md) — §5 (Thm. 2, Prop. 1, Eqs. (20)–(22), Table 2, Fig. 1, Remark 3); §6.1, §6.3.
- [Babbar et al. (2022)](/sources/babbar-2022.md) — §6 (Eq. (11), Table 1); App. B (Eq. (26), Table 2, Figs. 44–45).
- [Babbar & Chandrashekar (2025)](/sources/babbar-2025.md) — §5 (limits of Fourier CFL numbers on curvilinear meshes).
- [Tan et al. (2022)](/sources/tan-2022.md) — §3 (Lemmas 3.1–3.2, Props. 3.1–3.2), Tables 4.1–4.2.
- [Caliari et al. (2024)](/sources/caliari-2024.md) — §2 (Fourier analysis of exponential schemes with a partial linear part).
- [Hedayati Nasab et al. (2021)](/sources/hedayatinasab-2021.md) — §4–5 (multidimensional von Neumann spectra for stability polynomials).
- [Han Veiga et al. (2021)](/sources/hanveiga-2021.md) — §5.1 (von Neumann analysis left open).
