---
type: Method
title: "Entropy correction terms"
description: "An entropy correction term adds to each element of a residual-distribution, DG or SBP scheme the smallest perturbation, proportional to the deviation of the entropy variables from their element mean, that keeps local conservation and enforces one or more linear constraints such as entropy conservation, entropy dissipation or kinetic-energy preservation."
status: established
aliases: [Abgrall correction, entropy correction, entropy fix of residual distribution schemes, kinetic-energy correction term]
tags: [entropy-stable, kinetic-energy-preserving, dg, finite-difference]
timestamp: 2026-10-22T20:00:00Z
---

# Entropy correction terms

An entropy correction term is an element-local additive perturbation of a
semi-discrete (or fully discrete) scheme that makes the element's discrete
entropy balance equal to a prescribed numerical entropy flux through the
element boundary, while leaving the element's conservation balance
unchanged. Abgrall introduced it for residual-distribution (RD) schemes in
2018. [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md)
reinterpret it as the explicit unique solution of an equality-constrained
quadratic minimization problem, carry it to the
[summation-by-parts](/operators/summation-by-parts-operator.md) form of
nodal [DG](/methods/discontinuous-galerkin.md), and extend it to an entropy
inequality, to several constraints at once and to
[kinetic energy preservation](/properties/kinetic-energy-preservation.md).
It is an alternative to designing
[entropy-conservative two-point fluxes](/methods/entropy-conservative-flux.md)
and [flux differencing](/methods/flux-differencing.md), and the source
compares the two routes numerically.

Page-local symbols: $\mathbf 1$ the vector of ones on the nodes of an
element; $\mathfrak r_m$ the correction of conserved component $m$ at all
nodes; $\alpha_{\mathrm c}$ its amplitude; $\Delta_\eta$ the entropy defect
of the element (desired minus current entropy production); $\varphi_\sigma$
the basis function of degree of freedom $\sigma$ in an element $K$ with
$\#K$ degrees of freedom; $\Phi^K_\sigma$ the RD sub-residual and
$r^K_\sigma$ the RD correction of $\sigma$; $F^{\mathrm{num}}_\eta$ a numerical
entropy flux and $n$ the outward normal of $\partial K$.

## Residual-distribution form

An RD scheme splits the element residual into nodal sub-residuals
$\Phi^K_\sigma$ whose sum is the boundary flux (local conservation); DG,
continuous Galerkin, SUPG and flux reconstruction can all be written in
this form (Abgrall et al., §2.1, Eqs. (6)–(9)). The scheme conserves
entropy in $K$ when
$\sum_{\sigma\in K}w_\sigma\cdot\Phi^K_\sigma=\oint_{\partial K}F^{\mathrm{num}}_\eta\cdot n$,
with $F^{\mathrm{num}}_\eta$ a numerical entropy flux (Eq. (10)). Abgrall's
correction adds to every sub-residual (Eqs. (11)–(13))

$$r^K_\sigma=\alpha_{\mathrm c}\,(w_\sigma-\bar w),\qquad \bar w=\frac1{\#K}\sum_{\sigma\in K}w_\sigma,\qquad \alpha_{\mathrm c}=\frac{\Delta_\eta}{\sum_{\sigma\in K}\lvert w_\sigma-\bar w\rvert^2},$$

with $\Delta_\eta=\oint_{\partial K}F^{\mathrm{num}}_\eta\cdot n-\sum_{\sigma\in K}w_\sigma\cdot\Phi^K_\sigma$.
Then $\sum_\sigma r^K_\sigma=0$ (conservation is kept) and
$\sum_\sigma w_\sigma\cdot r^K_\sigma=\Delta_\eta$ (the entropy balance is
met), and $\alpha_{\mathrm c}=0$ when $w$ is constant in $K$ (Thm. 2.1,
Eqs. (14)–(15)). The correction applies on any grid, any node
distribution and any scheme of RD type; only the error of $\Delta_\eta$,
controlled by the quadrature, matters (§2.1). Entropy-dissipative
variants add jump or streamline diffusion to the correction (§2.1).

## DG form with mass-matrix weighting

For nodal DG with a diagonal-norm SBP mass matrix $M$, write the
semi-discretization as $\frac{d}{dt}u=\mathrm{VOL}+\mathrm{SURF}+\mathfrak r$
(§2.2, Eqs. (20)–(25)). Local conservation is $\mathbf 1^\top M\frac{d}{dt}u_m$
equal to the boundary flux of component $m$ (Eq. (23)); entropy
conservation is $\sum_mw_m^\top M\frac{d}{dt}u_m$ equal to the boundary
entropy flux (Eq. (24)). The mass-matrix-weighted correction is (Eq. (26))

$$\mathfrak r_m=\alpha_{\mathrm c}\Big(w_m-\frac{\mathbf 1^\top Mw_m}{\mathbf 1^\top M\mathbf 1}\mathbf 1\Big),\qquad \alpha_{\mathrm c}=\frac{\Delta_\eta}{\sum_l\Big(w_l^\top Mw_l-\dfrac{(\mathbf 1^\top Mw_l)^2}{\mathbf 1^\top M\mathbf 1}\Big)},$$

with $\Delta_\eta$ the boundary entropy flux (with the sign of Eq. (24))
minus $\sum_lw_l^\top M(\mathrm{VOL}_l+\mathrm{SURF}_l)$. If the
denominator vanishes, $w$ is constant in the element by Cauchy–Schwarz
(§2.2).

**Optimality** (Abgrall et al., Thm. 2.8, Prop. 2.10). For $\Delta_\eta\ne0$
and non-constant $w$, (26) is the unique solution of

$$\min_{\mathfrak r}\tfrac12\lVert\mathfrak r\rVert_M^2\quad\text{subject to}\quad \mathbf 1^\top M\mathfrak r_m=0\ \ \forall m,\qquad \sum_mw_m^\top M\mathfrak r_m=\Delta_\eta,$$

proved from the KKT system: $M\mathfrak r_m$ lies in the span of $M\mathbf 1$
and $Mw_m$, with a common coefficient of $Mw_m$. Abgrall's original
correction is the unique minimizer of the same problem in the identity
norm; its pointwise rewrite is optimal in the $M$-norm, and the integrated
(RD) form of (26) is optimal in the $M^{-1}$-norm (Prop. 2.10, Eqs.
(31)–(34)). Both corrections are explicit: no optimization solver is
needed, and the $M$-weighted variant costs the same as the original
(§2.2). The RD and DG corrections differ in sign convention, because one
is added on the residual side and the other on the time-derivative side
(§2.2).

**Compatibility of the constraints.** Conservation and entropy
conservation contradict each other only when the solution is constant in
the element; with entropy-conservative surface fluxes in Tadmor's sense
they do not contradict at all, because the constant-in-element scheme is
then an entropy-conservative finite-volume scheme (Remarks 2.5–2.7,
Eq. (29)).

## Extensions

- **Entropy inequality** (Thm. 3.1). With the constraint
  $\sum_mw_m^\top M\mathfrak r_m\le\Delta_\eta$, the unique minimizer is
  $\mathfrak r=0$ when $\Delta_\eta>0$ and (26) when $\Delta_\eta\le0$: the
  baseline is left untouched in elements where it already produces enough
  entropy, which gives a semi-discretely entropy-dissipative scheme
  (Eq. (35)).
- **Several constraints** (Thm. 3.2). With a second linear constraint
  on a second set of variables $\tilde w$ and defect $\tilde\Delta$
  (page-local), the minimum-$M$-norm correction is
  $\mathfrak r_m=\alpha_{\mathrm c}\big(w_m-\frac{\mathbf 1^\top Mw_m}{\mathbf 1^\top M\mathbf 1}\mathbf 1\big)+\tilde\alpha_{\mathrm c}\big(\tilde w_m-\frac{\mathbf 1^\top M\tilde w_m}{\mathbf 1^\top M\mathbf 1}\mathbf 1\big)$,
  with $(\alpha_{\mathrm c},\tilde\alpha_{\mathrm c})$ from an explicit
  $2\times2$ linear system whose matrix is the $M$-Gram matrix of the
  mean-free parts of $w$ and $\tilde w$ (Eq. (37)).
- **Kinetic energy** (§3.3, Prop. 3.5). For the compressible Euler
  equations, taking $w=\partial\kappa/\partial u$ and the kinetic-energy
  balance of a kinetic-energy-preserving scheme, which contains the
  volume pressure work $p^\top MD_jv_j$ and a surface term for
  $-p\,\partial_jv_j$, as the constraint gives the unique $M$-optimal
  kinetic-energy correction (Eqs. (39)–(42)). With kinetic-energy-preserving
  surface fluxes the conservation and kinetic-energy constraints do not
  contradict in a finite-volume setting (Remark 3.4).
- **Entropy and kinetic energy together.** Theorem 3.2 with
  $\eta=-\rho s/(\gamma-1)$ and $\kappa$ corrects both (Remark 3.6).
- **Fully discrete entropy conservation.** For deferred-correction
  space–time RD schemes, applying the correction to the whole space–time
  residual of each correction step, not only to the spatial residual,
  gives a fully discretely entropy-conservative scheme; correcting only
  the spatial residual gives a semi-discretely conservative one, which
  needs relaxation, artificial viscosity or implicit time stepping to be
  fully discrete (Remark 2.2, Eq. (19)). The authors present this as the
  first fully discrete entropy-conservative RD scheme (abstract).
- **Entropy-stable $p$-refinement and coarsening** (App. A.1). Transfer
  between a coarse and a fine polynomial space is posed as a convex
  problem: the $M$-closest state to the interpolant under conservation
  and a non-increasing total entropy (Eqs. (47)–(50)), solved with Ipopt.
  Interpolation and $L^2$ projection create spurious entropy (refinement
  $3.566\times10^{-3}$; coarsening $9.749\times10^{-2}$ and
  $7.767\times10^{-2}$), the optimization does not (entropy changes
  $-3.980\times10^{-8}$ and $-3.429\times10^{-7}$; the simplified refinement
  problem prints $+2.497\times10^{-8}$, within the solver tolerance; Fig. 9).
  See [h- and hp-adaptation](/methods/hp-adaptation.md).

## Evidence

All tests are in Abgrall et al. (2022), §4 and App. A:

- **Weightings.** On a 2D linear "rotation" test with fourth-order
  continuous Galerkin RD and SSP-RK(5,4), the unweighted and the
  $M$-weighted corrections give energy changes and $L^\infty$ errors that
  agree to eight to ten significant digits ($L^\infty$ errors
  $1.5323772081\times10^{-4}$ and $1.5323772103\times10^{-4}$, Table 1); on a 2D Burgers-type test the
  entropy changes are $1.6819\times10^{-15}$ and $1.6822\times10^{-15}$ (§4.1).
- **Shocks with RD.** On the 2D radial Sod problem, uncorrected continuous
  Galerkin with jump stabilization breaks down at $t\approx0.16$; with the
  semi-discrete correction it runs to $t=0.25$. With wall boundaries and
  the fully discrete correction, the more dissipative psi baseline behaves
  better than Galerkin, and a MOOD positivity fix is needed at fourth
  order (§4.1, Figs. 1–5;
  [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)).
- **Taylor–Green vortex.** On the inviscid 2D
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md), nodal DG with
  $N=5$ on $16^2$ elements: the central scheme blows up at $t\approx3.8$,
  the corrections control kinetic energy and entropy until blow-up, the
  combined correction blows up at $t\approx4.3$, and flux differencing with
  an entropy-conservative and kinetic-energy-preserving volume flux runs
  to $t\approx35$ (§4.2.2, Fig. 7). A sixth-order SBP finite-difference
  scheme on $100^2$ nodes shows the same ordering: central $t\approx23.5$,
  kinetic-energy correction about the same, entropy correction $24.8$,
  both $25.5$, flux differencing with the Pirozzoli or Ranocha flux
  beyond $t=30$ (App. A.3, Fig. 11). The Ducros et al. split form, neither
  entropy conservative nor kinetic-energy preserving alone, plus both
  corrections conserves entropy and does not blow up to $t=30$ (Fig. 8).
  The authors attribute the blow-ups to negative nodal density or
  pressure, after which entropy variables cannot be formed (§4.2.2, §6).
- **Accuracy.** With $N=4$ the corrections do not degrade the convergence
  of a smooth Euler density wave; at low resolution the $M$-weighted
  correction gives lower errors than the unweighted one (Table 2).

## Qualifications

- **Entropy conservation is not robustness.** Abgrall et al. state that
  "EC/D is not the holy grail" (§4): a single-block finite-difference or
  Fourier collocation scheme is one element, so the correction gives only
  a global entropy balance, and on periodic Burgers data with a stationary
  shock and a rarefaction the central scheme with or without correction
  keeps a stationary non-entropic solution because the defect is zero
  (Example 2.12). Nodal DG with Boole quadrature on linear advection has
  an entropy error falling with the fourth power of $\Delta t$ and yet
  highly oscillatory solutions (App. A.2). See
  [entropy stability](/properties/entropy-stability.md).
- **No free lunch.** The correction avoids the case-by-case algebra of
  entropy-conservative fluxes, which the authors tie to the calorically
  perfect gas (§5), but in the Taylor–Green tests it is less robust than
  flux differencing. The authors suggest that the gap comes from positivity
  loss and possibly from the inter-element or subcell entropy balances
  that flux differencing satisfies and an element-wise correction does
  not (§6).
- The arXiv v4 read prints a missing factor $\alpha$ in the proof of
  Thm. 2.1 and calls the conservation constraint (23) "the EC constraint"
  in Remark 2.7; the EC constraint is (24).

# Citations

- [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) — §2.1 Eqs. (6)–(19), Thm. 2.1, Remark 2.2, §2.2 Eqs. (20)–(34), Remarks 2.5–2.7, Thm. 2.8, Prop. 2.10, Example 2.12, §3 Thms. 3.1–3.2, Eqs. (35)–(42), Remarks 3.3–3.6, Prop. 3.5, §4 Tables 1–2, Figs. 1–8, §5, §6, App. A.1–A.3 Eqs. (47)–(50), Figs. 9–11 (arXiv v4).
