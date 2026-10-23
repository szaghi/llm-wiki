---
type: Definition
title: "Rankine–Hugoniot jump condition"
description: "The Rankine–Hugoniot condition ties the speed of a discontinuity to the jumps of state and flux across it; in this bundle it is the interface condition that a moving space–time DG method enforces to fit shocks and contacts, and, componentwise and regularized, the source of sharper one-sided speeds in central-upwind fluxes."
status: established
aliases: [Rankine–Hugoniot condition, jump condition, interface condition, interface conservation, discrete Rankine–Hugoniot speed]
tags: [shock-tracking, riemann-solver, numerical-flux, central-scheme]
timestamp: 2026-10-23T20:00:00Z
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

**Tracking without enforcing it.** The high-order implicit shock tracking (HOIST) of
[Huang & Zahr (2022)](/sources/huang-2022.md) recalls that the Rankine–Hugoniot conditions
hold at the discontinuities of the steady or space–time conservation law it solves (§2.1),
but does not impose them: the nodal coordinates are moved by minimizing the DG residual in an
enriched test space of degree $N+1$, subject to the standard DG equations with a smoothed
upwind or Roe flux, and the minimization drives element faces onto the discontinuities
(Eqs. (27)–(30), Remark 5). The two "implicit tracking" methods of the bundle thus differ in
where the jump condition enters: as a weakly enforced interface equation in MDG+ICE, as a
by-product of the residual minimization in HOIST ([implicit shock tracking](/methods/implicit-shock-tracking.md)).

*(compiler check, not in the sources: Lemma 2's algebra gives a speed for any jump,
including $u^-<u^+$, so the interface condition alone also admits the
entropy-violating expansion shock of Burgers' equation; the paper discusses no entropy
condition.)* Separately, Luo et al. note that their method can converge on tangled meshes
with negative-volume elements to solutions that are "either non-physical or meaningless",
e.g. a multivalued Burgers solution in their earlier work (§3.5).

## Discrete Rankine–Hugoniot speeds in central-upwind fluxes

[Wang et al. (2023b)](/sources/wang-2023-b.md) (§3.1, Eqs. (7)–(9), after Garg, Kurganov
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

*(compiler check, not in the sources: the same jump relation defines the single
intermediate state of the [HLL solver](/methods/hll-riemann-solvers.md):
$u^{\mathrm{HLL}}$ is the state for which $s^-(u^{\mathrm{HLL}}-u^-)+s^+(u^+-u^{\mathrm{HLL}})=[\![f(u)]\!]$,
i.e. the Rankine–Hugoniot relations across its two waves, summed.)*

## Jump relations inside approximate Riemann solvers and shock sensors

[Bai & Li (2022)](/sources/bai-2022.md) use the condition twice in a sharp-interface DG solver
for two-medium flows with a stiffened-gas equation of state.

- **HLLC star states.** Across each outer wave of speed $s^\mp$ the jump relation
  $s\,[\![u]\!]=[\![f(u)]\!]$ is imposed, with the flux split into an advective and a pressure
  part (§2.4, Eqs. (8)–(9)); the mass component gives the star density
  $\rho^*_K(s_K-v^*)=\rho_K(s_K-v_K)$, $K=L,R$, with $v^*$ the contact speed (Eqs. (10)–(14);
  see [HLL-family solvers](/methods/hll-riemann-solvers.md)). Bai & Li print the numerator of
  $\rho^*_K$ as $\beta_L$ for both $K$ (Eq. (11)), where the mass relation requires
  $\beta_K=\rho_K(s_K-v_K)$.
- **A pressure-jump shock indicator** (Eq. (18), $\alpha_{\mathrm s}=0.3$ page-local):
  $$f_p=1\quad\text{if}\quad|p_L-p_R|>\alpha_{\mathrm s}\,|v_L-v_R|\,\sqrt{\gamma\min\big(\rho_L(p_L+p_\infty),\,\rho_R(p_R+p_\infty)\big)},\qquad f_p=0\ \text{otherwise},$$
  with $p_\infty$ the stiffening constant (the registry's $p_{\infty,k}$ of the fluid at hand; [stiffened gas](/definitions/stiffened-gas-equation-of-state.md)).
  The authors say it is derived from the Rankine–Hugoniot conditions "with some empiric
  observations" and is "similar to the Joukowsky equation except for an parameter $\alpha$",
  i.e. equivalent to $|p_L-p_R|>\alpha_{\mathrm s}|v_L-v_R|\min(\rho_Lc_L,\rho_Rc_R)$ (§2.4).
  *(compiler check, not in the sources: the momentum relation across a shock of speed
  $s_{\mathrm d}$ gives $[\![p]\!]=-\rho^-(v^--s_{\mathrm d})[\![v]\!]$, whose acoustic limit is the
  Joukowsky relation $|[\![p]\!]|=\rho c\,|[\![v]\!]|$; for a stiffened gas
  $\rho c=\sqrt{\gamma\rho(p+p_\infty)}$, so the indicator fires when the pressure jump exceeds a
  fraction $\alpha_{\mathrm s}$ of the acoustic one.)* It switches the HLLC–HLL hybrid flux;
  how it is combined is on [carbuncle](/definitions/carbuncle-phenomenon.md).

**Phase interfaces with mass transfer.** At a liquid–vapour interface with evaporation or
condensation, [Long et al. (2023)](/sources/long-2023.md) (§3.1, Eq. (9), after Fechter et al.)
use the jump conditions of a discontinuity of speed $s_{\mathrm p}$ that carries a mass flux
$\dot m$, surface tension $\sigma_{\mathrm{st}}\kappa_{\mathrm c}$ and latent heat $Q_{\mathrm{lat}}$
(page-local):
$[\![\rho(V-s_{\mathrm p})]\!]=0$, $[\![\rho(V-s_{\mathrm p})V+p]\!]=-\sigma_{\mathrm{st}}\kappa_{\mathrm c}$ and
$[\![\rho(V-s_{\mathrm p})(e+\tfrac12V^2)+pV]\!]=\dot mQ_{\mathrm{lat}}-\sigma_{\mathrm{st}}\kappa_{\mathrm c}s_{\mathrm p}$,
$V$ the normal velocity. *(compiler check, not in the sources: with
$\sigma_{\mathrm{st}}=Q_{\mathrm{lat}}=0$ these are $s_{\mathrm p}[\![u]\!]=[\![f(u)]\!]$ for the 1D Euler
equations, and with $\dot m=0$ they reduce to a contact with a surface-tension pressure jump.)*
The jump system is underdetermined for a subsonic phase interface and needs a phase-change
model for $\dot m$. In their four-wave HLL-type solver the outer waves are treated as shocks
obeying the plain jump relations with Davis speeds (Eq. (14)); see
[Riemann solvers with phase change](/methods/phase-change-riemann-solver.md).

**Gradients of an HLL state.** In the HLL-GRP solver the gradient of the intermediate state is
obtained, "according to the Rankine–Hugoniot jump conditions" across the two HLL waves, from an
overdetermined least-squares system
([Liu et al. (2023a)](/sources/liu-2023.md), §3.2.1, Eq. (64);
[generalized Riemann problem](/methods/generalized-riemann-problem.md)).

## Shock states in test problems

Shocked initial data are built from the jump condition with zero speed or with the shock
speed. [Hu et al. (2022)](/sources/hu-2022.md) (§3.2) take the up- and downstream states of
their steady Mach-8 matrix-stability test from the Rankine–Hugoniot relations
([carbuncle](/definitions/carbuncle-phenomenon.md)). *(compiler check, not in the sources: their
Elling data, $(\rho,v_1,p)=(1,1,5/63)$ ahead of $(27/7,7/27,155/189)$, and their Quirk data,
$(896/115,735/112,74.5)$ behind a shock moving into $(1.4,0,1)$, are the exact normal-shock
states of a steady Mach-3 and a moving Mach-8 shock, $\gamma=1.4$.)*
Their Titarev–Toro shock–entropy test is described as driven by "a right-traveling shock wave
with Mach 1.1" (§5.3) with post-shock state $(\rho,v,p)=(1.515695,0.523346,1.805)$ into
$(1,0,1)$, $\gamma=1.4$. *(compiler check, not in the sources: the normal-shock pressure ratio
$p^-/p^+=\frac{2\gamma M^2-(\gamma-1)}{\gamma+1}=1.805$ gives $M^2=1.69$, $M=1.3$, and the
density ratio $\frac{(\gamma+1)M^2}{(\gamma-1)M^2+2}=1.5157$ agrees; the printed state is that
of a Mach-1.3 shock.)*

## Qualifications

- The Luo et al. Lemmas are two-line verifications for single-jump Riemann data on straight
  faces, called proofs; their Eqs. (3.9) and (3.12) print the two terms of the jump with the
  same sign, while the conclusions (3.10) and (3.13) carry $+$. *(compiler check, not in
  the sources: the printed (3.9) gives $x^{n+1}=x^n-a\Delta t$; a face with tangent
  $(\Delta x,\Delta t)$ has normal proportional to $(\Delta t,-\Delta x)$, which gives the
  conclusions with $+$.)*
- In Wang et al.'s Eq. (9) the two branches are not mutually exclusive and the order of
  evaluation is not stated; $[\![u]\!]$ and $[\![f]\!]$ are not defined in §3 and are read
  from App. A as interface jumps.

# Citations

- [Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md) — §3.2 (Eqs. (3.5)–(3.13), Lemmas 1–2), §3.3 (Eqs. (3.14)–(3.15)), §3.5, §IV (author manuscript).
- [Wang et al. (2023b)](/sources/wang-2023-b.md) — §3.1 (Eqs. (6)–(9)), App. A.
- [Bai & Li (2022)](/sources/bai-2022.md) — §2.4 (Eqs. (8)–(18)).
- [Huang & Zahr (2022)](/sources/huang-2022.md) — §2.1, Eqs. (27)–(30), Remark 5.
- [Hu et al. (2022)](/sources/hu-2022.md) — §3.2, §5.3, §5.8, §5.10.
- [Long et al. (2023)](/sources/long-2023.md) — §3.1 (Eqs. (9)–(12)), §3.2 (Eq. (14)).
- [Liu et al. (2023a)](/sources/liu-2023.md) — §3.2.1 (Eq. (64)).
