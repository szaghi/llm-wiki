---
type: Method
title: "Dissipation-based WENO stabilization of continuous finite elements"
description: "The CG-WENO method of Kuzmin and Vedral uses a Hermite WENO reconstruction only to measure how far a continuous finite element solution is from smooth, and turns that measure into a cellwise blend of high-order projection stabilization and low-order artificial viscosity; the solution is never overwritten, and the stabilization is O(h^(N+1/2)) consistent for smooth solutions."
status: established
aliases: [CG-WENO, dissipation-based WENO stabilization, WENO-based nonlinear stabilization]
tags: [weno, limiting, low-dissipation]
timestamp: 2026-10-21T00:00:00Z
---

# Dissipation-based WENO stabilization of continuous finite elements

[Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) propose a way to use WENO
reconstructions in high-order **continuous** Galerkin (CG) discretizations of
scalar conservation laws $\partial_tu+\nabla\cdot f(x,u)=0$, also suggested as
an alternative to WENO limiters in DG. Runge–Kutta DG schemes with WENO or
Hermite WENO limiters *overwrite* the finite element polynomial by the
reconstruction in troubled cells. CG-WENO never does: the reconstruction
$u_h^{e,*}$ of cell $K_e$ serves only to compute a cellwise factor
$\varsigma_e\in[0,1]$ (page-local; the source writes $\gamma_e$), and that
factor blends an accuracy-preserving high-order stabilization with a
low-order isotropic [artificial viscosity](/methods/artificial-viscosity.md).
The semi-discrete scheme therefore keeps the structure of a CG method
(Rem. 2), and the authors present it as a multidimensional high-order
finite element version of the Jameson–Schmidt–Turkel design.

## Stabilized Galerkin form

The semi-discrete problem is the Galerkin form plus
$\sum_es_h^e(u_h,w_h)$, with (§3, Eq. (8))
$$s_h^e(u_h,w_h)=\omega_{\mathrm H}\,\varsigma_e\,\mu_e\int_{K_e}(\nabla w_h-\pi_h\nabla w_h)\cdot(\nabla u_h-\pi_h\nabla u_h)\,dx+(1-\varsigma_e)\,\mu_e\int_{K_e}\nabla w_h\cdot\nabla u_h\,dx,$$
$\mu_e=a_eh_e/(2N)$, $a_e=\lVert f'(u_h)\rVert_{L^\infty(K_e)}$, $h_e$ the cell
diameter, $N$ the polynomial degree, $\pi_h$ the consistent-mass $L^2$
projection of gradients, $\omega_{\mathrm H}=1$ in the experiments ($\mu_e$,
$a_e$, $h_e$, $\omega_{\mathrm H}$ page-local). The first term is a symmetric,
coercive projection stabilization whose consistency error is
$O(h^{N+1/2})$; the second is first-order viscosity with an $O(h^{1/2})$
consistency error. The design requirements are that the high-order term
does not degrade convergence and is switched off near discontinuities, and
that the low-order term suppresses oscillations but vanishes when the exact
solution is a polynomial of degree $N$. The blending applies to any such
pair.

## The smoothness sensor

(§3, Eqs. (9)–(10)):
$$\varsigma_e=1-\min\Big\{1,\Big(\frac{\lVert u_h^e-u_h^{e,*}\rVert_e}{\lVert u_h^e\rVert_e}\Big)^{\mathsf q}\Big\},\qquad
\lVert v\rVert_e^2=\sum_{1\le\lvert k\rvert\le N}h_e^{2\lvert k\rvert-d}\int_{K_e}\lvert D^kv\rvert^2dx,$$
$\mathsf q\ge1$ (page-local; 1 by default). $\varsigma_e=1$ means smooth. Its
use as an indicator is recorded on
[troubled-cell indicator](/definitions/troubled-cell-indicator.md). Because the
seminorm involves only derivatives, the cell-average correction of the
candidates does not affect $\varsigma_e$ and can be skipped (Rem. 3).

## Hermite WENO reconstruction used

The reconstruction is outlined "without claiming originality" (§5, Eq. (11)),
after Zhong–Shu-type [Hermite WENO](/methods/hermite-weno.md):

- Candidates. $u_{h,0}^e=u_h^e$ (the cell's own polynomial). For each von
  Neumann neighbour $e'$ (shared vertex, edge or face; at least $d+1$ of
  them), the neighbour polynomial extended into $K_e$ and corrected to the
  cell average, $u_{h,l}^e=u_h^{e'}+\overline{(u_h^e-u_h^{e'})}_e$. All
  derivatives of the candidate equal those of the neighbour.
- Linear weights $d_0=1-m_e\cdot10^{-3}$, $d_l=10^{-3}$ for $l=1,\dots,m_e$
  ($m_e$ the number of neighbour candidates, page-local); on the KPP problem
  $d_l=0.2$ for all five candidates, because a smaller weight of the central
  candidate makes shock detection more reliable.
- Nonlinear weights of [Jiang–Shu](/methods/weno-js-reconstruction.md) form,
  $\alpha_l=d_l/(\epsilon+\beta_l)^{q}$, $q=2$, $\epsilon=10^{-6}$, with
  [smoothness indicators](/definitions/smoothness-indicator.md)
  $\beta_l=\lVert u^e_{h,l}\rVert_e^{\mathsf q}$; the source writes the weight
  exponent $r$ and the linear weights $\tilde\omega_l$.

An unimplemented extension adds Lagrange candidates interpolated on the
convex hull of barycentres around each vertex (Rem. 4).

## Analysis

(§6; the authors call it preliminary.) For steady advection–reaction
$v\cdot\nabla u+cu=f$ with $c-\frac12\nabla\cdot v\ge c_0>0$ (page-local
symbols), the stabilization $s_h(u_h;\cdot,\cdot)$ is, for fixed $u_h$, a
symmetric positive semidefinite bilinear form. A Strang-lemma bound reduces
the error to interpolation terms plus $\sqrt{s_h}$ evaluated at the
interpolant:

- worst case, $O(h^{1/2})$;
- for $u\in C^{N+1}$ and sensor exponent 2, a Taylor-basis argument gives
  $\lVert v_h^e-v_h^{e,*}\rVert_e^2=O(h^{2N+2})$ for the interpolant $v_h$,
  the low-order part $O(h^{2N+1})$, hence
  $\sqrt{s_h(I_hu;I_hu,I_hu)}=O(h^{N+1/2})$ (Eqs. (17)–(18)), called optimal
  for general meshes;
- polynomials of degree $\le N$ are reproduced exactly, since the deviation
  then vanishes for any nonlinear weights (Rem. 6);
- the final a priori estimate assumes an unverified Lipschitz-type
  condition on $s_h$.

## Numerical results

MFEM, $\mathbb Q_N$ Lagrange elements, $N=1..4$, explicit RK of order $N+1$,
fixed number of degrees of freedom $N_h$ (§7):

| Test | Result |
|---|---|
| 1D advection of $\cos(2\pi(x-0.5))$, $t=1$, $\mathsf q=3$ | $L^1$ EOC $\approx N+1$: e.g. $N=2$, $N_h=1024$, error $7.90\times10^{-9}$, EOC 3.00; $N=4$, $N_h=512$, $4.30\times10^{-11}$, EOC 5.08 (Table 1) |
| 1D advection, step plus smooth bump, $N_h=200$ | range $[-0.0066,1.0066]$ ($N=1$) to $[0.0000,0.9999]$ ($N=4$); unstabilized CG $[-0.33,1.23]$ at $N=4$ (Table 2) |
| Burgers, $\sin(2\pi x)$, $t=0.1$ (before the shock) | optimal EOCs; unstabilized CG drops to order $N$ for even $N$ (Table 3) |
| Burgers, $t=1$ | sharper shocks than low-order viscosity, almost independent of $N$ at fixed $N_h$ (Fig. 2) |
| LeVeque solid-body rotation, $129^2$ | bounded and non-oscillatory for all $N$, e.g. $N=4$ range $[0.000,0.998]$ (Figs. 3–5) |
| [KPP rotating wave](/benchmarks/kpp-rotating-wave.md), $129^2$, $t=1$ | reproduces the entropy spiral where unstabilized and high-order-only CG fail; range $[0.778,10.980]$ at $N=4$ (Figs. 6–8) |

## Qualifications

- Scalar problems only; the analysis covers the steady linear problem.
- "Superior" results on solid-body rotation mean boundedness, not $L^1$
  error: the high-order-only stabilization has the smaller error there
  ($1.47\times10^{-2}$ against $2.68\times10^{-2}$ for $N=1$).
- On KPP with $N=4$ a small undershoot appears, attributed to a cell-based
  indicator on a coarse mesh and said, not shown, to vanish under
  refinement (§7.4).
- Global bounds and entropy inequalities are not guaranteed; the authors
  suggest enforcing them with algebraic flux correction on top
  ([convex limiting](/methods/convex-limiting.md)).
- arXiv v1 prints the low-order part of $s_h(u_h;v_h,w_h)$ in §6 with
  $\nabla u_h$ where the stated bilinearity requires $\nabla v_h$.

# Citations

- [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) — arXiv v1: §2; §3 (Eqs. (4)–(10), Rem. 1); Rems. 2–4; §5 (Eq. (11)); §6 (Eqs. (12)–(18), Rems. 5–7); §7 (Tables 1–3, Figs. 1–8); §8.
