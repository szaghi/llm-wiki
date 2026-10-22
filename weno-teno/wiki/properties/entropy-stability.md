---
type: Property
title: "Entropy stability"
description: "A scheme is entropy stable when its discrete total entropy obeys the entropy inequality of the PDE; the page gives the flux- and scheme-level conditions, entropy-stable DG from EC volume and ED surface fluxes, which limiting steps keep the property, the KPP evidence, and the minimum entropy principle as a convex bound."
status: established
aliases: [entropy-stable scheme, entropy dissipative, ES, ED, discrete entropy inequality, entropy-stable DG, ESDG]
tags: [entropy-stable, dg, numerical-flux, bound-preserving, limiting]
timestamp: 2026-10-21T12:00:00Z
---

# Entropy stability

Entropy solutions of $\partial_tu+\nabla\cdot f(u)=0$ satisfy
$\partial_t\eta(u)+\nabla\cdot F_\eta(u)\le0$ for every convex entropy pair
$(\eta,F_\eta)$. A semi-discretization is **entropy stable**, or
entropy-dissipative (ED), when its quadrature-weighted total entropy obeys
the discrete analogue. It is non-increasing apart from boundary fluxes,
and locally its change is an entropy-flux difference plus a non-positive
production. It is **entropy-conservative** (EC) when the production
vanishes. In the sources, scheme-level EC/ED is built from the flux-level
conditions of Tadmor: $[\![w]\!]\cdot f=[\![\psi]\!]$ (EC) and
$[\![w]\!]\cdot f-[\![\psi]\!]\le0$ (ED)
([Ranocha et al. (2023)](/sources/ranocha-2023.md), Def. 2.5;
[entropy-conservative and kinetic-energy-preserving two-point fluxes](/methods/entropy-conservative-flux.md)).

## Entropy-stable DG

The flux-differencing DGSEM is EC when its symmetric volume flux is EC and
its surface flux is EC. It is ED when the surface flux is ED instead.
This holds on diagonal-norm SBP elements (Ranocha et al. (2023), §2,
citing Carpenter et al. and Gassner–Winters–Kopriva;
[flux differencing](/methods/flux-differencing.md),
[summation-by-parts operator](/operators/summation-by-parts-operator.md)).
[Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) use
an EC volume flux with a local Lax–Friedrichs surface flux, and state that
the resulting scheme "satisfies a discrete entropy inequality" (§5.1).

On Legendre–Gauss nodes, entropy stability needs two further ingredients:

- the hybridized SBP operator;
- an entropy projection, $\tilde u=u(\mathcal Rw(\mathbf u))$, for the
  surface states.

Ranocha et al. (2023) measure this variant at 1.5× to 5× the cost of the
LGL scheme (§6). Ranocha et al. also state, citing the literature, that
flux differencing comes with stability guarantees that overintegration
lacks, and that it stays stable where overintegration fails (§5).

As recalled by Rueda-Ramírez et al. (2022), the classical DG cell entropy
inequality for the square entropy (Jiang–Shu) needs exact volume and surface
integration. That is not feasible for the non-polynomial KPP flux, which is
why the split form is used there (§5.1).

## Which robustness steps keep it

Rueda-Ramírez et al. (2022) map three cases (§2.2, §4; see
[subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md)):

- **Element-wise blending.** One coefficient $\alpha$ per element blends an
  ES DGSEM with an ES finite-volume scheme. The finite-volume scheme uses
  first-order fluxes, or minmod TVD reconstruction of scaled entropy
  variables after Fjordholm–Mishra–Tadmor. The blend stays provably entropy
  stable as long as both schemes share the surface terms. The proofs, for
  Euler and MHD, are cited from Hennemann et al. and follow-ups.
- **Subcell-wise blending.** One coefficient per subcell interface is used.
  The proof of entropy dissipation is "still missing" (§4, item 2).
- **A posteriori limiting.** Invariant-domain bounds from Guermond–Popov bar
  states, plus a local minimum principle on the modified specific entropy
  $e\rho^{1-\gamma}$, guarantee positivity of density and pressure and a
  discrete entropy inequality (§5.2.2, citing Guermond et al.). Rueda-Ramírez
  et al. note that this quantity is cheaper than $s$ and better suited to
  Newton's method. Here $e\rho^{1-\gamma}=\exp(s)/(\gamma-1)$ with
  $s=\ln(p\rho^{-\gamma})$, a monotone function of the physical entropy
  *(compiler check, not in the sources: use $p=(\gamma-1)\rho e$)*. These
  bounds hold for the Rusanov low-order scheme. With HLLE or second-order
  finite volumes they are not guaranteed, and the algorithm returns the
  solution "closest to the restrictions" (§5.2.3).

## Evidence: the KPP problem

The [KPP rotating wave](/benchmarks/kpp-rotating-wave.md), with its
non-convex flux $f=(\sin u,\cos u)$, separates entropy-stable from merely
non-oscillatory schemes:

- **Rueda-Ramírez et al. (2022)** (§5.1, Figs. 2–3; $N=3$, $32^2$ to $256^2$
  elements, $t=1$, element-wise shock capturing with $\alpha_{\max}=0.5$).
  The standard DGSEM gives clean, essentially non-oscillatory but
  **non-entropic** solutions. Its spurious structures even trigger the
  shock sensor. The ES split-form DGSEM, with the scalar EC flux in the
  volume and LLF at surfaces, converges to the entropy solution. Shock
  capturing alone does not fix the entropy.
- **[Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md)** (§7.4, Figs. 6–8;
  $Q_p$ continuous elements, $N_h=129^2$ degrees of freedom). The lumped-mass Galerkin scheme
  oscillates and produces an entropy-violating shock. High-order
  stabilization alone reduces the oscillations but not the entropy defect.
  The low-order and WENO-blended schemes reproduce the spiral entropy
  solution. The authors note that a non-symmetric variational multiscale
  stabilization "may produce entropy", which is why they use a symmetric one
  (§3). Entropy inequalities can be enforced on top via algebraic flux
  correction (§7.4).

As recalled by Rueda-Ramírez et al. (2022), monotone and
maximum-principle-satisfying schemes can still converge to non-entropic
solutions when they lack a discrete entropy inequality (§5.1).

## Minimum entropy principle as a convex bound

[Wu & Shu (2023)](/sources/wu-2023-b.md) use Tadmor's minimum entropy
principle in the form $p\rho^{-\gamma}\ge s_{\min}'$, with $s_{\min}'$
(page-local, their $S_{\min}$) the initial minimum of $p\rho^{-\gamma}$. Together
with positivity it defines a convex invariant region, so it can be enforced
as a [bound-preservation](/properties/bound-preservation.md) constraint
rather than through fluxes (§2, Eq. (2.3)).

Wu & Shu represent it, by
[geometric quasilinearization](/methods/geometric-quasilinearization.md), as
a family of constraints linear in $u$ (Thm 4.7; Eq. (2.3)). For 1D Euler the
family is

$$u\cdot n_*+s_{\min}'\rho_*^{\gamma}\ge0,\qquad n_*=\Big(\tfrac12v_*^2-\frac{\gamma s_{\min}'\rho_*^{\gamma-1}}{\gamma-1},\,-v_*,\,1\Big)^\top,$$

for all free auxiliary $\rho_*>0$ and $v_*\in\mathbb R$. They give the relativistic analogue in Thm 4.10. The local minimum principle on
$e\rho^{1-\gamma}$ in the subcell limiting of Rueda-Ramírez et al. (2022) is
a discrete, local relative of the same principle.

## Qualifications

- **Convergence is asserted, not proved.** Rueda-Ramírez et al. (2022) state
  that the ES DGSEM "will therefore converge to the unique entropic
  solution" of KPP. The support is numerical (Fig. 2). No convergence
  theorem for high-order DG on non-convex fluxes is given in the source.
- **Sign conventions.**
  - Ranocha et al. (2023) write a mathematical entropy and define ED by
    "$\le$", i.e. production $\le0$, as in the registry
    ($\eta=-\rho s/(\gamma-1)$ for Euler); they do not state the sign
    convention or the convexity explicitly.
  - The KPP tests use $\eta=\tfrac12u^2$.
  - The minimum principles of Rueda-Ramírez et al. and Wu & Shu bound
    functions of the physical specific entropy from below.

# Citations

- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — Def. 2.5, §2, §5, §6.
- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — §2.2, §4 items (1)–(3), §5.1 Eqs. (37)–(40) Figs. 2–3, §5.2.2 Eqs. (47)–(48), §5.2.3.
- [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) — §3, §7.4 Figs. 6–8.
- [Wu & Shu (2023)](/sources/wu-2023-b.md) — Eq. (2.3), Thms 4.7, 4.10.
