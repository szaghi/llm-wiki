---
type: Result
title: "Lax–Wendroff theorem"
description: "The Lax–Wendroff theorem makes conservation in flux form with consistent fluxes the condition for convergence to a weak solution; the founding TVD and ENO papers pair it with total-variation bounds and entropy consistency; later sources invoke it for Active Flux, DGSEM subcells and multi-medium schemes, extend it to a vanishing conservation defect, and show wrong shock speeds without conservation."
status: established
aliases: [Lax–Wendroff convergence theorem, Lax–Wendroff consistency condition, conservation and convergence to weak solutions]
tags: [finite-volume, finite-difference, dg]
timestamp: 2026-10-30T08:12:00Z
---

# Lax–Wendroff theorem

Solutions of nonlinear conservation laws develop discontinuities in finite time even from
smooth data, so the natural setting is weak solutions; "for convergence to the weak
solution …, a numerical method needs to be conservative (Lax–Wendroff theorem)"
([Abgrall & Barsukow (2023)](/sources/abgrall-2023.md), §1). The theorem (Lax & Wendroff
1960, cited by the sources, not ingested here) has two hypotheses the sources make explicit:
the scheme is written in **conservation (flux) form**,

$$\frac{d}{dt}\bar u_i=-\frac1{\Delta x}\big(\hat f_{i+1/2}-\hat f_{i-1/2}\big),$$

and the numerical flux is **consistent** with the physical one. The sources use it in one
direction only: conservation (with consistent fluxes) is what a scheme needs for
convergence to a weak solution (Abgrall & Barsukow, §1). The founding papers of TVD and ENO
schemes state the convergence argument around it (next section), and
[Gaburro et al. (2024)](/sources/gaburro-2024.md) restate convergence hypotheses for a
modified version of the theorem (below); otherwise the bundle records the theorem through
what the sources derive from it.

## The convergence argument of the founding papers

[Shu & Osher (1988)](/sources/shu-1988.md) (§I, Eqs. (1.3)–(1.4)) write the conservative
scheme $u^{n+1}_i=u^n_i-\frac{\Delta t}{\Delta x}(\hat f_{i+1/2}-\hat f_{i-1/2})$ with a
consistent flux $\hat f(u,\dots,u)=f(u)$ and state that this guarantees that bounded,
almost-everywhere convergent subsequences converge to weak solutions, citing the
Lax–Wendroff theorem. [Harten (1983a)](/sources/harten-1983.md) (§1) states the full chain
for a conservative scheme, citing earlier work: (i) a total variation bounded uniformly in
$t$, $\Delta t$ and $\Delta x$, (ii) consistency with the entropy condition for all entropy
functions, and (iii) uniqueness implied by the entropy condition give convergence to the
entropy solution; the discrete entropy inequality the paper defines is
$\eta(u^{n+1}_i)\le\eta(u^n_i)-\frac{\Delta t}{\Delta x}(\hat F_{i+1/2}-\hat F_{i-1/2})$ with a
consistent numerical entropy flux $\hat F$ (page-local; Eq. (1.5)). Harten proves (i)
([TVD](/definitions/total-variation-diminishing.md)) for the paper's scalar scheme and only
conjectures that entropy consistency
([entropy stability](/properties/entropy-stability.md)) carries over to it (§5;
[Harten's TVD scheme](/methods/harten-tvd-scheme.md)).
[Harten et al. (1987a)](/sources/harten-1987.md) (§1, Eq. (1.19)) state the same pairing for
ENO: $TV(u_h(\cdot,t))\le C\,TV(u_0)$ gives convergence of a subsequence in $L^1_{\mathrm{loc}}$ to
a weak solution, and they leave the total-variation bound of ENO as a conjecture
(Eq. (1.22)).

## The consistency condition

[Coppola & Veldman (2023)](/sources/coppola-2023.md) (§2.4, Eq. (22)) write the semi-discrete
scheme as $H\,\frac{d\phi}{dt}+(I-E^{-1})F\phi=0$, with $H$ a diagonal control-volume matrix,
$E$ the circulant shift and $F\phi$ the vector of interface fluxes (page-local symbols of the
source's matrix framework), and state the "classical" Lax–Wendroff condition as

$$F\phi_a\,\mathbf 1=F(\phi_a)\qquad\text{for every constant }\phi_a,$$

which "basically says that conservation and consistency imply that the numerical fluxes are
a fair interpolation between the adjacent nodal values". They assume it at the generality of
their framework and state that they "can not (yet) prove this" (§2.4).

The finite-difference statement is the same with point values: [Jeong et al. (2022)](/sources/jeong-2022.md)
(§2.1) write the conservative scheme $\frac{d}{dt}u_i=-\frac1{\Delta x}(\hat f_{i+1/2}-\hat f_{i-1/2})$
with a numerical flux $\hat f$ that is Lipschitz and consistent, $\hat f(u,\dots,u)=f(u)$, and
invoke the theorem for convergence to weak solutions of their
[RBF-based WENO](/methods/rbf-weno.md) ([conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)).

## Which schemes satisfy the flux-form hypothesis

- **Every globally conservative scheme.** Coppola & Veldman prove that a discrete operator
  with local support is locally conservative, i.e. of the form $(I-E^{-1})F$, if and only if
  all its column sums vanish, which is global conservation (Lemma A.1, Observation 1): for
  volume-consistent discretizations global and local conservation coincide, so every
  globally conservative finite-difference scheme is a cell-centred finite-volume scheme with
  an explicit numerical flux ([local conservation is equivalent to a flux
  form](/results/local-conservation-flux-form.md)). They cite Perot: "any method that is
  globally conservative, and that has weight functions with local support, must also be
  locally conservative" (Remark 1).
- **Active Flux.** The averages are updated by the exact finite-volume balance with the
  interface point values as flux arguments, hence conservatively, while the point values are
  free of the conservation constraint; Abgrall & Barsukow report that an analogue of the
  Lax–Wendroff theorem for [Active Flux](/methods/active-flux.md) has been shown by
  Abgrall (2020) (§1).
- **DGSEM on Gauss–Lobatto nodes.** [Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md)
  (§2.1, Eq. (8)) rewrite the standard and split-form [DGSEM](/methods/dgsem.md) exactly in a
  subcell flux-differencing form with high-order inter-node fluxes and state that this
  "implies local subelement-wise conservation due to the well-known theorem of Lax and
  Wendroff"; it is what allows a compatible subcell finite-volume scheme to be blended in
  ([subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md),
  [flux differencing](/methods/flux-differencing.md)).

## A modified theorem: vanishing conservation defect

[Gaburro et al. (2024)](/sources/gaburro-2024.md) (§4.1, Eq. (49), Prop. 1) relax the
flux-form hypothesis. On a mesh of polygonal cells $K_i$, a scheme satisfies a
**modified local conservation statement** if

$$\lvert K_i\rvert\,\frac{\bar u_i^{n+1}-\bar u_i^n}{\Delta t}+\sum_\ell\hat f^n_{i\ell}=\lvert K_i\rvert\,\mathsf d^n_i,$$

with $\hat f^n_{i\ell}$ the face fluxes and $\mathsf d^n_i$ the **local
conservation defect** (page-local; $\ell$ runs over the faces of $K_i$). Proposition 1:
if the discrete initial data converge weakly to the exact ones, a TVB-type condition
$h^2\sum_i\sum_\alpha\max_{x\in B_{i,\alpha}}\lVert u^n_h(x)-u^n_h(x_{i,\alpha})\rVert\to0$ holds
(Eq. (50); $B_{i,\alpha}$ balls around subcells, page-local), the meshes are shape regular and
$\sup_{i,n}\lVert\mathsf d^n_i\rVert$ vanishes as $h\to0$ (Eq. (51)), then a convergent sequence
of discrete solutions converges to a weak solution. The proof follows Shi and Shu and Abgrall and
Roe, with the extra term bounded by $\lvert\Omega\rvert\,t_{\mathrm f}\,\lVert\varphi\rVert_{L^\infty}\sup_{i,n}\lVert\mathsf d^n_i\rVert$
for a test function $\varphi$ (page-local $t_{\mathrm f}$ the final time). Schemes satisfying it
are called **locally quasi-conservative**.

The authors use it for an ADER-DG scheme that evolves the primitive variables
$(\rho,v,p,\chi)$ of multi-material Euler with [path-conservative](/methods/path-conservative-scheme.md)
fluctuations, whose cell averages of the conserved variables are therefore not updated in
flux form. They show that the defect vanishes (§4.3):

- for locally smooth discrete solutions, in the DG update and in the subcell finite-volume
  update, with $\mathsf d^n_i=O(h)$ under bounds on the first derivatives and on the face jumps
  that they call stronger than the TVB condition (Props. 2–3, App. A);
- at faces between limited and unlimited cells of the a posteriori limiter when the two face
  states differ by $O(h^{1+\beta_{\mathrm c}})$, $\beta_{\mathrm c}>0$ (page-local, the source's $\beta$), which justifies extending the troubled flag to
  neighbours instead of correcting the fluxes of unflagged cells (Prop. 4;
  [MOOD a posteriori limiting](/methods/mood-a-posteriori-limiting.md));
- across quasi-1D contacts with velocity and pressure constant up to terms $O(h^{1+\epsilon_{\mathrm c}})$, $\epsilon_{\mathrm c}>0$ (Eq. (63); page-local exponent), for one
  material and for two materials with the marker closure $1/(\tilde\gamma-1)=\chi/(\gamma-1)$,
  and with $\tilde\gamma=\chi\gamma$ under an extra discrete condition (Prop. 5, App. B; page-local
  $\chi$, $\tilde\gamma$; a generalization of Abgrall's result, in their words;
  [pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)).

At shocks the defect does not vanish. The scheme therefore flags shock cells with a
divergence-based sensor and, in those subcells only, recomputes the update in
**conservative** variables with a Rusanov flux (Eq. (67)), which "entirely removes the local
conservation defect" there (§4.4; [Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md),
[MUSCL–Hancock](/methods/muscl-hancock.md)).

## What dropping conservation costs

Four sources show the consequence the theorem warns of, a wrong shock speed:

- **A non-conservative ENO variant.** [Shu & Osher (1988)](/sources/shu-1988.md) (§III,
  Eqs. (3.18)–(3.19), p. 20) tried a variant of their flux ENO scheme that differentiates the
  interpolant at the grid point instead of differencing fluxes. Without a cap on the divided
  differences it gives the wrong shock location on a Burgers Riemann problem
  ($u=\tfrac12$ left, $u=-1$ right, fifth-order versions); with the cap it becomes, in their
  word, "essentially conservative", a conservative scheme plus $O(\Delta x^2)$, which keeps
  the conclusion of the theorem, and the location is correct but the shock "severely
  smeared"; the variant was abandoned (no figure printed; see
  [Burgers-equation tests](/benchmarks/burgers-equation-tests.md)).

- **Non-conservative blending in time.** The [Quinpi](/methods/quinpi.md) scheme blends a
  high-order and a first-order implicit solution cell by cell, which is not conservative.
  Without the conservative correction that turns the blend back into a flux form, the
  scheme loses mass on Burgers' equation and places the shock wrongly; with it, mass is
  conserved at all times and the shock is located correctly
  ([Puppo et al. (2023)](/sources/puppo-2023.md), §3.3.4, §4.3.2, Fig. 7; see
  [local conservation is equivalent to a flux form](/results/local-conservation-flux-form.md)).
- **Non-conservative interface methods.** [Zheng et al. (2021)](/sources/zheng-2021.md) (§1)
  call the ghost-fluid family (GFM, modified and real GFM) and related interface
  treatments non-conservative, so that convergence to weak solutions is not assured, and
  build a conservative sharp-interface finite-difference scheme instead: a single
  computational variable updated by flux differences and redistributed between the two
  fluids (§2.3). On a strong shock hitting a gas–gas interface a finite-difference WENO
  ghost-fluid method misplaces both the shock front and the interface, while the
  conservative scheme does not (§4, Example 4, Fig. 8). They also recall that
  conservative schemes "tend to give oscillatory results if no special care is taken" at
  material interfaces (§1), which is the price conservation brings there (see
  [characteristic decomposition](/methods/characteristic-decomposition.md) on primitive
  variables).
- **Non-conservative variables at shocks.** On the circular Sod explosion
  ([explosion and implosion problems](/benchmarks/explosion-and-implosion-problems.md)) the
  ADER-DG scheme of [Gaburro et al. (2024)](/sources/gaburro-2024.md) applied to the
  primitive-variable formulation everywhere gives a wrong shock speed; the conservative
  subcell correction in shock-flagged cells alone "is enough to restore" the correct one, at
  $h=1/50$ and $h=1/215$ with $\mathbb P^2$ and $\mathbb P^3$ (§5.1.4, Fig. 3). They recall that the
  segment path of path-conservative schemes is "in general not consistent with the correct
  jump conditions" (§1).

## Qualifications

- What most sources cite is the conservation-and-consistency requirement; only Gaburro
  et al. (2024) prove a statement of the theorem's type for their own scheme, and it is
  conditional, like the theorem: *if* the scheme converges. They print the vanishing of the
  defect as "$O(1)$" in Eqs. (47) and (51) and state that it denotes "a quantity vanishing
  when $h\to0$", i.e. $o(1)$; Props. 2–3 conclude $o(1)$. *(compiler check, not in the sources:
  their smoothness hypotheses bound face jumps by a constant times $h$, so no $O(1)$ jump
  satisfies them; at discontinuities only the contact case of Prop. 5 and the conservative
  shock correction cover the defect.)* Conservation does not select
  the physically relevant weak solution: on the KPP rotating-wave problem the (conservative)
  standard DGSEM with shock capturing gives clean but **nonentropic** solutions, while the
  entropy-stable split-form DGSEM converges to the entropy solution
  ([Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md), §5.1, Figs. 2–3;
  [KPP rotating wave](/benchmarks/kpp-rotating-wave.md),
  [entropy stability](/properties/entropy-stability.md)).
- Rueda-Ramírez et al. attribute "local subelement-wise conservation" to the theorem; the
  conservation itself follows from the flux form (8), while the theorem is what gives it
  meaning for shock capturing.
- **Scope: conservation laws only.** For a system with a non-conservative product,
  $\partial_tu+\partial_xf(u)+\mathcal C(u)\partial_xu=0$, the product has no flux, so the
  flux-form hypothesis cannot be met for it *(compiler check, not in the sources)*. As
  recalled by [Chu et al. (2022)](/sources/chu-2022.md) (§1), weak solutions of such systems
  are defined as Borel measures in the sense of Dal Maso, LeFloch and Murat, which needs a
  choice of path across each jump, and are computed with
  [path-conservative schemes](/methods/path-conservative-scheme.md); with $\mathcal C=0$ their
  path-conservative central-upwind scheme is the conservative central-upwind scheme
  (§2, Eq. (2.1)).
- Coppola & Veldman's dual-sided first-order scheme conserves mass, momentum and total
  energy and gives a shock profile between the oscillating central and the smeared upwind
  scheme in a 1D Euler test without added dissipation (§8.2); they make no entropy claim.

# Citations

- [Abgrall & Barsukow (2023)](/sources/abgrall-2023.md) — §1 (author preprint).
- [Shu & Osher (1988)](/sources/shu-1988.md) — §I (Eqs. (1.3)–(1.4)), §III (Eqs. (3.16)–(3.19), p. 20) (ICASE Report 87-33).
- [Harten (1983a)](/sources/harten-1983.md) — §1 (Eqs. (1.3)–(1.5)), §5 (NYU report DOE/ER/03077-175, March 1982).
- [Harten et al. (1987a)](/sources/harten-1987.md) — §1 (Eqs. (1.19), (1.22)).
- [Coppola & Veldman (2023)](/sources/coppola-2023.md) — §2.4 (Eqs. (18)–(22), Observation 1, Remark 1), App. A.1 (Lemma A.1), §8.2 (arXiv v1).
- [Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md) — §2.1 (Eq. (8)), §5.1 (Figs. 2–3) (arXiv v2).
- [Puppo et al. (2023)](/sources/puppo-2023.md) — §3.3.4, §4.3.2 (Fig. 7) (arXiv v2).
- [Zheng et al. (2021)](/sources/zheng-2021.md) — §1, §2.3, §4 (Example 4, Fig. 8).
- [Chu et al. (2022)](/sources/chu-2022.md) — §1, §2 (Eq. (2.1)).
- [Jeong et al. (2022)](/sources/jeong-2022.md) — §2.1.
- [Gaburro et al. (2024)](/sources/gaburro-2024.md) — §1, §4.1 (Eqs. (47)–(51), Prop. 1), §4.3 (Props. 2–5), §4.4 (Eq. (67)), §5.1.4 (Fig. 3), Apps. A–B (arXiv v1).
