---
type: Definition
title: "Rankine–Hugoniot jump condition"
description: "The Rankine–Hugoniot condition ties the speed of a discontinuity to the jumps of state and flux across it; in this bundle it is the interface condition that a moving space–time DG method enforces to fit shocks and contacts, and, componentwise and regularized, the source of sharper one-sided speeds in central-upwind fluxes."
status: established
aliases: [Rankine–Hugoniot condition, jump condition, interface condition, interface conservation, discrete Rankine–Hugoniot speed]
tags: [shock-tracking, riemann-solver, numerical-flux, central-scheme]
timestamp: 2026-10-22T12:00:00Z
---

# Rankine–Hugoniot jump condition

For $\partial_tu+\partial_xf(u)=0$, a discontinuity moving with speed $s_{\mathrm d}$
(page-local) between the states $u^-$ (left) and $u^+$ (right) is a weak solution only if

$$s_{\mathrm d}\,[\![u]\!]=[\![f(u)]\!],\qquad[\![a]\!]=a^+-a^-.$$

In space–time, with the space–time flux $F=(f(u),u)$ in the $(x,t)$ plane and a face of
normal $n$, the same condition is $[\![F\cdot n]\!]=0$: the normal flux is continuous
across the face. [Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md) (§3.2,
Eq. (3.5)) derive it from conservation on a control volume of zero thickness straddling a
face and call it the **interface condition** ("interface conservation" in their
manuscript); it is the transmission condition of hybridized and embedded DG. The
condition says nothing about which discontinuities are admissible: that is the role of an
entropy condition ([entropy stability](/properties/entropy-stability.md)).

## Fitting discontinuities with it

In the moving DG method MDG+ICE the face positions are unknowns, fixed by enforcing the
interface condition weakly against a continuous trace space (Eq. (3.7)); a face that
satisfies it moves at the right speed. Two elementary statements make this explicit (§3.2,
Eqs. (3.8)–(3.13)): for Riemann data on a straight space–time face from $(x^n,t^n)$ to
$(x^{n+1},t^{n+1})$,

- linear advection, $f=au$: the condition holds iff $x^{n+1}=x^n+a\,\Delta t$, a contact at
  speed $a$ (Lemma 1);
- Burgers, $f=u^2/2$: it holds iff $x^{n+1}=x^n+\tfrac12(u^-+u^+)\Delta t$, the
  Rankine–Hugoniot shock speed (Lemma 2).

Once the condition holds, the face flux is unique, so MDG+ICE replaces the Riemann solver
by the central average of the two traces (§3.3). The method then fits shocks and contacts
of the [Sod and Lax tubes](/benchmarks/sod-and-lax-shock-tubes.md) with eight space–time
cells and steady oblique and bow shocks in 2D (§IV); see
[implicit shock tracking](/methods/implicit-shock-tracking.md) and
[carbuncle](/definitions/carbuncle-phenomenon.md).

*(Compiler check, not in the sources: Lemma 2's algebra gives a speed for any jump,
including $u^-<u^+$, so the interface condition alone also admits the
entropy-violating expansion shock of Burgers' equation; the paper discusses no entropy
condition.)* Separately, Luo et al. note that their method can converge on tangled meshes
with negative-volume elements to solutions that are "either non-physical or meaningless",
e.g. a multivalued Burgers solution in their earlier work (§3.5).

## Discrete Rankine–Hugoniot speeds in central-upwind fluxes

[Wang et al. (2023)](/sources/wang-2023-b.md) (§3.1, Eqs. (7)–(9), after Garg, Kurganov
and Liu) tighten the one-sided speeds $a^\pm_{i+1/2}$ of the
[central-upwind flux](/methods/central-upwind-scheme.md) with componentwise, regularized
Rankine–Hugoniot speeds of the interface jump,

$$\hat s^{(l)}_{i+1/2}=\frac{2\,[\![f^{(l)}]\!]_{i+1/2}}{[\![u^{(l)}]\!]_{i+1/2}+[\![u^{(l)}]\!]^{\varepsilon}_{i+1/2}},\qquad
[\![u^{(l)}]\!]^{\varepsilon}=\begin{cases}\max([\![u^{(l)}]\!],\varepsilon),&[\![u^{(l)}]\!]>0,\\ \min([\![u^{(l)}]\!],-\varepsilon),&\text{otherwise},\end{cases}$$

($l$ the component, $\varepsilon$ page-local regularization), which reduce to
$[\![f^{(l)}]\!]/[\![u^{(l)}]\!]$ when the jump exceeds $\varepsilon$ in size. Their extremes
over the components cap the eigenvalue-based speeds: if the largest exceeds $\varepsilon$
it bounds $a^+$ from above and $-a^-$ likewise, and symmetrically for the smallest
(Eq. (9)). The paper's further reduction of the speeds in smooth regions and the
dissipation switch are on [adaptive-diffusion central-upwind flux](/methods/adaptive-diffusion-central-upwind-flux.md).

*(Compiler check, not in the sources: the same jump relation defines the single
intermediate state of the [HLL solver](/methods/hll-riemann-solvers.md):
$u^{\mathrm{HLL}}$ is the state for which $s^-(u^{\mathrm{HLL}}-u^-)+s^+(u^+-u^{\mathrm{HLL}})=[\![f(u)]\!]$,
i.e. the Rankine–Hugoniot relations across its two waves, summed.)*

## Qualifications

- The Luo et al. Lemmas are two-line verifications for single-jump Riemann data on straight
  faces, called proofs; their Eqs. (3.9) and (3.12) print the two terms of the jump with the
  same sign, while the conclusions (3.10) and (3.13) carry $+$. *(Compiler check, not in
  the sources: the printed (3.9) gives $x^{n+1}=x^n-a\Delta t$; a face with tangent
  $(\Delta x,\Delta t)$ has normal proportional to $(\Delta t,-\Delta x)$, which gives the
  conclusions with $+$.)*
- In Wang et al.'s Eq. (9) the two branches are not mutually exclusive and the order of
  evaluation is not stated; $[\![u]\!]$ and $[\![f]\!]$ are not defined in §3 and are read
  from App. A as interface jumps.

# Citations

- [Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md) — §3.2 (Eqs. (3.5)–(3.13), Lemmas 1–2), §3.3 (Eqs. (3.14)–(3.15)), §3.5, §IV (author manuscript).
- [Wang et al. (2023)](/sources/wang-2023-b.md) — §3.1 (Eqs. (6)–(9)), App. A.
