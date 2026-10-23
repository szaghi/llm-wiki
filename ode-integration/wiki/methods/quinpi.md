---
type: Method
title: "Quinpi: implicit high-order finite-volume time stepping with a-posteriori time limiting"
description: "Quinpi integrates stiff hyperbolic systems with a third-order SDIRK and CWENO finite volumes, using a first-order implicit predictor to freeze the nonlinear reconstruction weights so that each stage is nonlinear only through the flux, and a conservative entropy-triggered time limiter that falls back to predictor fluxes in troubled cells."
status: established
aliases: [implicit CWENO, Quinpi scheme, Q3, Q3I3, predictor-linearized implicit WENO]
tags: [implicit, runge-kutta, stiff, linear-algebra, structure-preserving]
timestamp: 2026-10-20T06:18:00Z
---

# Quinpi: implicit high-order finite-volume time stepping with a-posteriori time limiting

Quinpi ("implicit CWENO") is a third-order implicit finite-volume scheme for
conservation laws whose wave speeds differ by orders of magnitude, such as low-Mach gas
dynamics, where the step should follow the slow material wave and not the CFL limit of
the fast acoustics. A high-order implicit scheme with WENO-type reconstruction is
nonlinear even for a linear PDE, because the reconstruction weights depend on the
solution. Quinpi removes that nonlinearity with a first-order implicit **predictor**
that freezes the weights, and controls oscillations at large Courant numbers with an
a-posteriori **time limiter** ([Puppo et al. (2024)](/sources/puppo-2024.md), §1–3).
It was introduced for scalar laws by Puppo, Semplice & Visconti (2023), as recalled;
Puppo et al. (2024) extend it to one-dimensional systems and replace the time limiter
by a conservative one. The authors state that they "do not claim that the Quinpi
approach is asymptotic preserving" (§4.2).

**Page-local notation.** Cell averages $U_j$ on a uniform mesh of width $\Delta x$,
numerical flux $\mathcal F(v,w)$ at the interfaces, stage values $U^{(k)}$ of an
$s$-stage DIRK with coefficients $a_{ki}$, $b_k$, $c_k$; flux differences
$\Delta F_j=F_{j+1/2}-F_{j-1/2}$; predictor quantities carry a star.

## Ingredients

1. **Space.** Third-order CWENOZ reconstruction without ghost cells, with adaptive-order
   boundary reconstructions (§2.1), and a Rusanov flux (Eq. (39)). For the Euler tests
   the Rusanov viscosity is the material speed only, a deliberately low dissipation on
   the acoustic waves (§4).
2. **Time.** Alexander's three-stage, third-order SDIRK with $\gamma=0.4358665215$,
   A-stable and stiffly accurate, hence L-stable (§4, p. 20), in flux form:
   $U_j^{(k)}=U_j^n-\frac{h}{\Delta x}\sum_{i\le k}a_{ki}\Delta F^{(i)}_j$,
   $U_j^{n+1}=U_j^n-\frac h{\Delta x}\sum_kb_k\Delta F^{(k)}_j$ (Eqs. (15a)–(15b)); see
   [DIRK methods](/methods/diagonally-implicit-runge-kutta.md). Other DIRKs, such as
   optimal implicit SSP methods, are mentioned as alternatives.
3. **Predictor.** Composite backward Euler through the DIRK abscissae, with sub-steps
   $\theta_k=c_k-c_{k-1}$ and a piecewise-constant reconstruction:
   $U_j^{\star,(k)}=U_j^{\star,(k-1)}-\frac{\theta_kh}{\Delta x}\Delta F^{\star,(k)}_j$
   (Eqs. (19)–(23)). It is itself a first-order DIRK with the same abscissae (Eq. (22)).
   Being first order, it needs no spatial limiting, since first-order implicit schemes
   are unconditionally TVD (cited to the scalar paper), and its Newton Jacobian is
   block-tridiagonal (Eq. (24)).
4. **Frozen-weight corrector.** For corrector stage $k$ the CWENOZ weights are computed
   from $U^{\star,(k)}$, which makes the reconstructed interface values linear in the
   unknown averages (Eqs. (17)–(18)). The stage equation is then nonlinear only
   through the physical flux, and its Newton Jacobian has explicitly computable entries
   (Eqs. (25)–(27)); the predictor stage also gives the initial guess. Predictor and
   corrector alternate stage by stage (Fig. 1). Newton uses GMRES with ILU(0) (§4); see
   [implicit stage solvers](/methods/implicit-stage-solvers.md).
5. **Time limiter** (below).

**Why freezing keeps third order.** The CWENOZ error splits into the error of the
optimal polynomial, $O(\Delta x^3)$, plus $(d_k-\omega_k)$ times second-order terms
(page-local linear and nonlinear weights $d_k$, $\omega_k$), so third order needs
$d_k-\omega_k=O(\Delta x)$ (Eqs. (28)–(29), citing earlier work). Only the weights use
the predictor; the polynomials use the unknown high-order averages. On a smooth profile
the predictor-based weights meet the condition asymptotically, with errors
$3.58\times10^{-1}$ at 20 cells and $1.37\times10^{-3}$ at 5120 (rate 2.03), identical to
those of third-order-based weights from 160 cells on (§3.2.1, Table 1).

## Conservative a-posteriori time limiting

Large implicit steps produce spurious oscillations that space limiting alone does not
prevent: without time limiting a colliding-flows Riemann problem "blows up at time
t = 0.93" (§3.3, §4.1.2, Fig. 4). After the unlimited DIRK update, cells are marked as
troubled with the **numerical entropy production**, the discrete residual of the entropy
inequality for an entropy $\eta$ (page-local symbols: $S$ the production, $\Psi$ the
numerical entropy flux, $Q$ a cell quadrature),

$$S_j=\frac1h\Big[Q\big(\eta(U^{n+1})\big)_j-Q\big(\eta(U^n)\big)_j+\frac h{\Delta x}\sum_kb_k\big(\Psi^{(k)}_{j+1/2}-\Psi^{(k)}_{j-1/2}\big)\Big]$$

(Eq. (31), after Puppo and Puppo & Semplice), which scales like $O(\Delta x^p)$ on
smooth cells of an order-$p$ scheme, like $O(\Delta x^{-1})$ at shocks and $O(1)$ at
contacts (§3.3.1, as recalled). With $S^3$ for the third-order step and $S^1$ for the
predictor, three detectors are compared (Eqs. (34)–(36); page-local thresholds):

* **I1:** mark if $S^3_j>\kappa_1$, with $\kappa_1=\Delta x$;
* **I2:** mark if $S^3_j/(S^1_j+10^{-10})>\kappa_2$;
* **I3:** mark if both hold; this is the recommended detector.

At every interface of a marked cell the stage fluxes $b_kF^{(k)}_{j+1/2}$ are replaced
by the predictor fluxes $\theta_kF^{\star,(k)}_{j+1/2}$, and the update is re-assembled
from the stored stage fluxes; detection and replacement repeat until no cell is marked
(Eqs. (37)–(38)). Each interface carries one flux, so the limiter is conservative by
construction; the stages are not recomputed. It is inspired by MOOD, an a-posteriori
*space* limiter. The cell-centred limiter of the scalar Quinpi paper blends first- and
third-order averages, is not conservative and is "nontrivial" to extend to systems
(§3.3, §5); a related scheme of Visconti et al. blends high- and low-order fluxes
convexly where this one replaces them totally (§3.3.2, as recalled).

## Evidence

* **Order on smooth data.** On an advected density wave at $h/\Delta x=4$, Q3I1 and
  Q3I3 are third order at Courant numbers about 10.7 and 673.3 (pressure $10^0$ and
  $10^4$), with $L^1$ errors $5.44\times10^{-8}$ and $5.15\times10^{-8}$ at 2560 cells,
  identical to the unlimited scheme because the limiter never fires. Detector I2 fails
  on flat regions, where both productions are floating-point zeros, limits everything
  and reduces the scheme to first order (§4.1.1, Tables 3–4).
* **Low Mach number.** On a smooth low-Mach Euler problem at Courant number 20 the
  unlimited scheme has $L^1$ rates 2.94, 2.93 and 2.99 for $\varepsilon=0.8$, $0.3$ and
  $10^{-4}$, with low rates on coarse grids (§4.2.1, Table 6). On
  [colliding acoustic pulses](/benchmarks/colliding-acoustic-pulses.md) it is compared
  with an explicit run graphically (§4.2.2).
* **Stiff Riemann problems.** On a non-symmetric expansion, colliding flows and a
  modified Lax problem at Courant numbers 10–12, Q3I3 is as accurate as Q3 on the contact
  waves and reduces the oscillations on the acoustic waves; I1 alone is more diffusive.
  The limiter acts on all waves early and later mainly on shocks, on 4 % to 83 % of the
  steps (§4.1.2, Table 5, Fig. 5). Against the explicit CWENOZ scheme at its stability
  step, Q3I3 at a step "about 10 times larger" is less accurate on acoustic waves and more
  accurate on the contact (Fig. 6).
* **Scalar comparisons.** On linear transport and Burgers with 400 cells at
  $h/\Delta x$ up to 10, the new limiter is less dissipative than the cell-centred one
  and, at $t=0.6$ on Burgers, avoids the undershoot of the MOOD-type scheme (§4.3,
  Figs. 8–9); see [Burgers equation](/benchmarks/burgers-equation.md).

## Qualifications

* **Third order is verified only where the limiter is inactive.** No convergence study
  with an active limiter is reported, and the observed order on the Riemann problems is
  not given (§4).
* **No cost data.** The "about 10 times larger" step is the only efficiency evidence;
  no CPU time is reported against the explicit scheme, and the authors list cheaper
  limiting, linear solvers and preconditioners as future work (§5).
* **Asymptotic preservation not claimed.** The authors disclaim it, and the low-Mach tests
  show stability and accuracy only (§4.2). The material-speed Rusanov viscosity would not
  be an upwind-stable choice for the acoustics of an explicit scheme *(compiler remark,
  not in the source)*.
* **Printed slips** (arXiv v4; *compiler check against the paper, not in the source*; details
  on the Source page). Eq. (26)
  prints the corrector residual with $-U^{(k-1)}$, the composite backward Euler form; the
  DIRK (15a) requires $-U^n$ plus the earlier stage fluxes. Fig. 1 cites equation numbers
  that do not exist in the paper. The Fig. 7 caption steps do not match the stated
  $h/\Delta x$. The introduction attributes a fifth-order implicit WENO scheme to the
  Gottlieb–Shu–Tadmor SSP review instead of Gottlieb, Mullen & Ruuth.

# Citations

- [Puppo et al. (2024)](/sources/puppo-2024.md) — §1; §2.1–2.2 (Eqs. (14)–(16)); §3 (Eqs. (17)–(27), Fig. 1, Remark 2); §3.2.1 (Eqs. (28)–(29), Table 1); §3.3 (Eqs. (30)–(38)); §4 (Alexander SDIRK3, Eq. (39)); §4.1.1 (Tables 3–4); §4.1.2 (Table 5, Figs. 2–6); §4.2 (Table 6, Fig. 7); §4.3 (Figs. 8–9); §5.
