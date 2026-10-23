---
type: Method
title: "Bassi–Rebay viscous discretizations (BR1, BR2)"
description: "BR1 and BR2 discretize the viscous terms of DG and flux-reconstruction schemes with lifted gradients: BR1 with a global lifting and central interface averages, BR2 with face-local liftings and a penalty factor; entropy-variable gradients and an extra projection make them entropy stable, but neither guarantees positivity."
status: established
aliases: [BR1, BR2, Bassi–Rebay scheme, first Bassi–Rebay scheme, second Bassi–Rebay scheme, lifting-operator viscous flux, projected entropy-stable BR1, projected entropy-stable BR2]
tags: [dg, flux-reconstruction, entropy-stable, positivity]
timestamp: 2026-10-23T15:13:00Z
---

# Bassi–Rebay viscous discretizations (BR1, BR2)

The Bassi–Rebay schemes discretize the second-order (viscous) terms of a
[discontinuous Galerkin](/methods/discontinuous-galerkin.md) or
[flux-reconstruction](/methods/flux-reconstruction.md) scheme by
introducing a *lifted* gradient: the broken gradient of the element
polynomial plus a lifting of the interface jumps of the solution into the
element interior. For a viscous flux written as
$f_v^{(d)}=-\sum_{d'}\mathsf K_{dd'}\,\partial_{x_{d'}}w$ (page-local
$\mathsf K_{dd'}$, the symmetric positive semi-definite blocks of the
symmetrized viscous operator, here acting on the entropy variables $w$),
the interface viscous flux is built from averages of the lifted-gradient
flux. BR1 (Bassi & Rebay 1997) uses one global lifting and central
averages and is not compact; BR2 is its compact modification with
face-local liftings and a penalty, as recalled by
[Alberti et al. (2025)](/sources/alberti-2025.md) (§2).

## BR1

Let $u_h$ be the element solution of degree $N$. BR1 solves for an
auxiliary gradient $g_h=\nabla_hu_h+R([\![u_h]\!])$, with $R$ the global
lifting operator (page-local), and takes the central average of the
viscous flux at the interfaces. In the modal DG of
[Basile et al. (2022)](/sources/basile-2022.md) the auxiliary variable is
the gradient of the conservative state with global lifting (Eqs. (19)–(23));
in the DGSEM of [Schwarz et al. (2025)](/sources/schwarz-2025.md) the
lifted gradients are those of the primitive variables, discretized by the
DGSEM itself, and the surface viscous flux is the arithmetic mean
$\{\!\{f_v\}\!\}$ of the two traces times the surface metric (§3.2,
Eqs. (18)–(19); [DGSEM](/methods/dgsem.md)).

For entropy stability the lifted gradients must be those of the entropy
variables. [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md)
apply BR1 to the gradients of the entropy variables in the split-form
DGSEM of resistive GLM-MHD, $J\mathsf w_kg_k=\sum_nQ_{kn}w_n$ plus boundary
corrections, and recall from earlier work that the visco-resistive terms
then keep the entropy estimate (§2, Eqs. (38)–(39);
[entropy stability](/properties/entropy-stability.md)).

BR1 is the viscous discretization of PyFR in Dzanic, Trojak & Witherden
(2022) (§4.2; [PyFR](/software/pyfr.md)), of the entropy-stable DGSEM
runs of [Peyvan et al. (2023)](/sources/peyvan-2023.md) (§4.6), and of
[FLEXI](/software/flexi.md) in Schwarz et al. (2025).
[Cernetic et al. (2023)](/sources/cernetic-2023.md) implemented it and
abandoned it: it triples the work of the auxiliary-gradient solve in 3D,
gives large in-cell derivatives for initial data with large jumps, and
"does not converge rapidly at high order either"; they use an $L^2$
recovery of the interface gradient instead (§3.1;
[artificial viscosity](/methods/artificial-viscosity.md)).

## BR2

BR2 replaces the global lifting by face-local liftings $r_F$, defined on
each face $F$ by

$$\sum_K\int_K\tau_h\cdot r_F(\phi)\,dx=-\int_F\phi\,\{\!\{\tau_h\}\!\}\cdot n_F\,dS\qquad\forall\tau_h\in[\mathbb P^N]^d,$$

with $R=\sum_Fr_F$, and takes as interface viscous flux

$$\hat f_v=\Big\{\!\!\Big\{f_v\big(w_h,\ \nabla_hw_h+C_{\mathrm{BR2}}\,r_F([\![w_h]\!])\big)\Big\}\!\!\Big\}\cdot n_F,$$

with page-local penalty factor $C_{\mathrm{BR2}}$ (Alberti et al.,
Eqs. (12)–(14)). The penalty must exceed the number of faces of the
element; Alberti et al. state the requirement both as "greater than the
number of cell faces" and as $C_{\mathrm{BR2}}\ge\mathrm{card}(\mathcal F_K)+1$,
page-local $\mathcal F_K$ the set of faces of $K$, and note that smaller
values often work in practice (§2, §2.1.2).

BR2 is the viscous flux of PyFR in
[Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) (§4.2) and in
[Trojak & Dzanic (2024)](/sources/trojak-2024.md) (§5)
([entropy filtering](/methods/entropy-filtering.md)), and the default
viscous flux of [Ching et al. (2025)](/sources/ching-2025.md) for the
reacting multicomponent Navier–Stokes equations (§3, §4.6).

## Entropy-stable projected variants

Alberti et al. (2025) solve in conservative variables and evaluate all
operators at the projected entropy variables $w_h$
([entropy projection](/methods/entropy-projection.md)). The matrices
$\mathsf K_{dd'}(w_h)$ are then rational functions of the element
polynomial, and the lifting identities used in the entropy analyses of
BR2 do not hold, which earlier analyses "do not consider" (§2.1.2). Their
remedy is an extra $L^2$ projection of the viscous flux onto the DG space,
$\Pi_F\in[\mathbb P^N]^{d\times m}$ per face (page-local), defined by

$$\int_K\phi\,\Pi_{F,d}\,dx=\int_K\phi\sum_{d'}\mathsf K_{dd'}(w_h)\big(\partial_{x_{d'}}w_h+C_{\mathrm{BR2}}\,r_{F,d'}([\![w_h]\!])\big)\,dx\qquad\forall\phi\in\mathbb P^N$$

(Eq. (37)), used in the surface integral. The schemes are called
$\Pi_{\mathrm{BR2}}$ and, with the global lifting, $\Pi_{\mathrm{BR1}}$.

- **$\Pi_{\mathrm{BR2}}$.** The viscous entropy rate becomes (Eq. (40))
  $$\begin{aligned}
  \sum_K\int_Kw_h\cdot\partial_tu_h\,dx={}&-\sum_K\int_K\partial_dw_h^\top\mathsf K_{dd'}\,\partial_{d'}w_h\,dx-2\sum_K\int_K\partial_dw_h^\top\mathsf K_{dd'}R_{d'}\,dx\\
  &-C_{\mathrm{BR2}}\sum_K\sum_{F\in\mathcal F_K}\int_Kr_{F,d}^\top\mathsf K_{dd'}r_{F,d'}\,dx,
  \end{aligned}$$
  with summation over $d,d'$ (the two cross terms of Eq. (40) written as
  one through the symmetry of $\mathsf K$), and the authors bound it with a generalized
  Young inequality for symmetric positive semi-definite matrices (Lemma 1,
  after May) to an entropy inequality (Eq. (42)); see Qualifications for
  the printed signs. "A larger" penalty "increases the entropy stability"
  (§2.1.2).
- **$\Pi_{\mathrm{BR1}}$.** With the global lifting the rate is exactly
  $$\sum_K\int_K\partial_t\eta(u_h)\,dx=-\sum_K\int_K(\partial_dw_h+R_d)^\top\mathsf K_{dd'}(\partial_{d'}w_h+R_{d'})\,dx\le0$$
  (Eq. (47)): an exact entropy-production identity, where BR2 gives only a
  bound (§2.1.2).

The projection does not change the Laplacian discretization, so the BR2
penalty requirement is unchanged (§2.1.2).

## Positivity

Conventional viscous fluxes such as BR2 and SIPG do not guarantee
positivity: the time step that would keep it can be arbitrarily small, as
Ching et al. (2025) recall, whereas Zhang's Lax–Friedrichs-type viscous
flux comes with a strictly positive bound (§1;
[positivity-preserving Navier–Stokes flux](/methods/positivity-preserving-navier-stokes-flux.md)).
Ching et al. therefore use BR2 first and fall back only when needed: if
any cell average of the convective or viscous half-update is
inadmissible, they halve the step once with BR2, and if that fails they
recompute with the Lax–Friedrichs-type viscous flux. A smaller step or a
flux switch is needed in "typically no more than ten percent of time
steps" (§4.6; [bound preservation](/properties/bound-preservation.md)).

## Evidence

- **Accuracy.** Alberti et al.: BR1, BR2, $\Pi_{\mathrm{BR1}}$ and
  $\Pi_{\mathrm{BR2}}$ all converge at $N+1$ for $N=1$–6 on the
  Navier–Stokes manufactured solution of Roy et al. at $\mathrm{Re}=100$
  on $2^i\times2^i$ meshes, $i=1$–4 (§3.2.1, Fig. 8;
  [method of manufactured solutions](/definitions/method-of-manufactured-solutions.md)).
  Ching et al.: BR2 and the Lax–Friedrichs-type flux both reach $N+1$ for
  $N=1$–3 on a 1D thermal-bubble advection–diffusion problem at CFL 0.1,
  except on the coarse $N=1$ grids (§5.1, Fig. 5.1).
- **Robustness.** Alberti et al.'s viscous Kelvin–Helmholtz instability at
  Atwood number 0.99, $\mathrm{Re}=100$, power-law exponent 0.75, $N=3$ on
  a $2^4\times2^4$ mesh: only $\Pi_{\mathrm{BR2}}$ reaches the final time,
  with the least entropy production in the common window, and it fails
  for a penalty below 2; with exponent 0 all schemes complete for
  $\mathrm{Re}<500$ and only $\Pi_{\mathrm{BR2}}$ at $\mathrm{Re}=500$, with
  threshold penalty 4 (§3.2.2, Figs. 9–12;
  [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)).
  They add that a globally increasing $\rho s$ does not guarantee
  consistent entropy evolution in each element, which only the projected
  schemes control (§3.2.2).
- **Spurious oscillations.** Ching et al.: in a 2D H$_2$–O$_2$–Ar
  detonation BR2 gives "much smaller nonphysical instabilities" than the
  Lax–Friedrichs-type viscous flux, while in a 1D viscous multicomponent
  shock tube the Lax–Friedrichs-type flux gives a noticeably smaller
  temperature overshoot (§5.3–5.4, Figs. 5.6–5.9;
  [shock-induced combustion](/benchmarks/shock-induced-combustion.md)).
  The authors keep BR2 as the default and the Lax–Friedrichs-type flux as
  a fallback (§4.6, §6).
- **Cost.** $\Pi_{\mathrm{BR2}}$ costs 1.34, 1.42, 1.52, 1.58 and 1.62 times
  BR2 for $N=3$–7; Alberti et al. write that the overhead (extra projection
  integrals, parallel communication) "tends to hinder its applicability in
  production-grade solvers" (Table 4, §4).

## Qualifications

- Alberti et al. print the BR2 bound (42) as
  $-(1+\epsilon)\int\partial w^\top\mathsf K\,\partial w-\epsilon^{-1}\int R^\top\mathsf KR-C_{\mathrm{BR2}}\sum\int r_F^\top\mathsf Kr_F$
  for all $\epsilon>0$. Bounding the cross term $-2\int\partial w^\top\mathsf
  KR$ of Eq. (40) with their Lemma 1 gives instead
  $-(1-\epsilon)\int\partial w^\top\mathsf K\,\partial w+\epsilon^{-1}\int
  R^\top\mathsf KR-C_{\mathrm{BR2}}\sum\int r_F^\top\mathsf Kr_F$, which is
  negative only if the lifting term is controlled by the penalty term:
  elementwise $\int_KR^\top\mathsf KR\le\mathrm{card}(\mathcal
  F_K)\sum_{F\in\mathcal F_K}\int_Kr_F^\top\mathsf Kr_F$ for positive
  semi-definite $\mathsf K$, so the bound is nonpositive for
  $C_{\mathrm{BR2}}\ge\mathrm{card}(\mathcal F_K)/\epsilon$ with
  $\epsilon<1$; their remark that a larger penalty increases entropy
  stability agrees with this form *(compiler check, not in the sources)*.
- Alberti et al.'s viscous Kelvin–Helmholtz runs report that smaller
  penalties than the theoretical bound work for BR2 in general, yet
  $\Pi_{\mathrm{BR2}}$ needs at least 2 or 4 in their two cases.
- The BR1/BR2 comparisons are each from one code (Alberti et al.'s modal
  solver, Ching et al.'s JENRE framework); no source compares BR1 and BR2
  across codes.

# Citations

- [Alberti et al. (2025)](/sources/alberti-2025.md) — §2 Eqs. (12)–(14), §2.1.2 Eqs. (36)–(47), Lemma 1, §3.2.1 Fig. 8, §3.2.2 Figs. 9–12, Table 4, §4.
- [Ching et al. (2025)](/sources/ching-2025.md) — §1, §3, §4.6, §5.1 Fig. 5.1, §5.3–5.4 Figs. 5.6–5.9, §6.
- [Schwarz et al. (2025)](/sources/schwarz-2025.md) — §3.2 Eqs. (18)–(19) (arXiv v1).
- [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) — §2 Eqs. (38)–(39).
- [Basile et al. (2022)](/sources/basile-2022.md) — Eqs. (19)–(23).
- [Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) — §4.2 (arXiv v2).
- [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) — §4.2 (arXiv v3).
- [Trojak & Dzanic (2024)](/sources/trojak-2024.md) — §5.
- [Peyvan et al. (2023)](/sources/peyvan-2023.md) — §4.6 (arXiv v1).
- [Cernetic et al. (2023)](/sources/cernetic-2023.md) — §3.1.
