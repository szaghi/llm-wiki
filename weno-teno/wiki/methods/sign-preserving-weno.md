---
type: Method
title: "Sign-preserving WENO"
description: "Sign-preserving WENO reconstructions (SP-WENO, SP-WENOc, DSP-WENO) are third-order four-point WENO forms whose weight perturbations keep the sign property that TeCNO entropy-stable dissipation needs; the page gives the form, the sign constraint, the zero-jump problem at shocks, and the learned feasible-region variant."
status: established
aliases: [SP-WENO, SP-WENOc, DSP-WENO, deep sign-preserving WENO, sign-property WENO, Fjordholm–Ray WENO]
tags: [weno, entropy-stable, reconstruction, finite-difference, machine-learning, sign-property]
timestamp: 2026-10-24T05:57:00Z
---

# Sign-preserving WENO

A **sign-preserving WENO** reconstruction is a WENO reconstruction whose
interface jumps have the **sign property**. That is the condition under
which the dissipation of a [TeCNO scheme](/methods/tecno-scheme.md) stays
entropy stable. The reconstructed jump at an interface must have the sign
of the jump of the cell values. Minmod and ENO have the property by
construction: [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md)
state, citing Fjordholm et al., that minmod is the only symmetric TVD
limiter with it (§4), and [Bhoriya et al. (2023)](/sources/bhoriya-2023.md)
use ENO for that reason (§4.1.2). Fifth-order WENO gets it only through
the componentwise Biswas–Dubey switch of
[Duan & Tang (2022)](/sources/duan-2022.md) (§4) and
[Li, Duan & Tang (2022c)](/sources/li-2022-c.md) (§3.4), which removes the
dissipation where the test fails. Sign-preserving WENO builds the property into the weights instead.
[Charles & Ray (2025)](/sources/charles-2025.md) recall SP-WENO (Fjordholm
& Ray) and SP-WENOc (Ray), and propose DSP-WENO. All three are third-order
reconstructions on a four-point stencil (§1, §3–4; arXiv v2).

## The form and the sign constraint

The reconstruction acts on one component $z$ (page-local) of the scaled
entropy variables $\tilde w$ of the TeCNO page. Let page-local
$\Delta z_{i+1/2}=z_{i+1}-z_i$ be the cell jump and
$[\![z]\!]^{\mathrm{rec}}_{i+1/2}=z^+_{i+1/2}-z^-_{i+1/2}$ the
reconstructed jump. The values are finite-difference point values. Each
side combines two two-point candidates on the union stencil
$\{i-1,\dots,i+2\}$ (Eq. (12), recalled from Fjordholm & Ray):

$$z^-_{i+1/2}=\tfrac12\big(\omega_0(z_i+z_{i+1})+\omega_1(3z_i-z_{i-1})\big),\qquad z^+_{i+1/2}=\tfrac12\big(\tilde\omega_0(3z_{i+1}-z_{i+2})+\tilde\omega_1(z_i+z_{i+1})\big).$$

The weights are perturbations of the linear weights $\tfrac34$ (central
candidate) and $\tfrac14$ (extrapolating candidate):
$\omega_0=\tfrac34+2\mathsf c_1$, $\tilde\omega_0=\tfrac14-2\mathsf c_2$,
$\omega_1=1-\omega_0$, $\tilde\omega_1=1-\tilde\omega_0$ (Eq. (13);
page-local $\mathsf c_1,\mathsf c_2$, the source's $C_1,C_2$). With the
linear weights, the left value is $(-z_{i-1}+6z_i+3z_{i+1})/8$, the
third-order interpolant *(compiler check, not in the sources)*. The
weights are consistent, all in $[0,1]$, if and only if
$-\tfrac38\le\mathsf c_1,\mathsf c_2\le\tfrac18$.

Let $r_i=\Delta z_{i+1/2}/\Delta z_{i-1/2}$ be the slope ratio (registry §4).
The jump can then be rewritten (Eqs. (15)–(16)) as

$$[\![z]\!]^{\mathrm{rec}}_{i+1/2}=\tfrac12\Big(\tilde\omega_0\,(1-r_{i+1})+\omega_1\,(1-1/r_i)\Big)\,\Delta z_{i+1/2}.$$

The source's ratios are $\theta^-_{i+1}=r_{i+1}$ and $\theta^+_i=1/r_i$.
The sign property is therefore the scalar inequality
$\tilde\omega_0(1-r_{i+1})+\omega_1(1-1/r_i)\ge0$. In the perturbations
the jump is (proof of Lemma SM1)

$$[\![z]\!]^{\mathrm{rec}}_{i+1/2}=(\mathsf c_1-\tfrac18)\Delta z_{i-1/2}+(\tfrac14-\mathsf c_1-\mathsf c_2)\Delta z_{i+1/2}+(\mathsf c_2-\tfrac18)\Delta z_{i+3/2}.$$

If $\Delta z_{i+1/2}=0$, every variant sets $z^-=z_i$ and $z^+=z_{i+1}$,
so the jump is zero (Remark 2).

Charles & Ray tabulate the constraints by the position of
$(1/r_i,r_{i+1})$ relative to 1, after Fjordholm & Ray (Table SM1):

- Both ratios above 1 force $\mathsf c_1=\mathsf c_2=\tfrac18$, which
  switches both extrapolating candidates off.
- Both below 1 impose no constraint beyond consistency, and neither do
  the boundary cases where the other ratio is at most 1.
- The mixed cases, one ratio above 1 and one below, are the
  **C-region**. There the sign constraint is a half-plane in
  $(\mathsf c_1,\mathsf c_2)$, bounded by the line on which the jump
  vanishes. Third order additionally requires
  $\mathsf c_1,\mathsf c_2=O(\Delta x)$.

## SP-WENO and SP-WENOc

**SP-WENO** (Fjordholm & Ray, as recalled by Charles & Ray, §3.1) gives
$\mathsf c_1,\mathsf c_2$ in closed form, case by case. It has
consistency, the sign property, negation symmetry, a mirror property,
local monotonicity at inner interfaces ("inner jump condition") and the
jump bound $|[\![z]\!]^{\mathrm{rec}}|\le2|\Delta z_{i+1/2}|$ (Eqs.
(17)–(20)).

Its weakness is the C-region. There the formulas give a reconstructed
jump that is zero, or nearly zero, "in most cases". The TeCNO dissipation
then vanishes exactly where a shock needs it (§3.2, citing Ray).
**SP-WENOc** (Ray) adds a perturbation
$g_{\mathrm c}=\big(\min(|\Delta z_{i+1/2}|/(\tfrac12(|z_i|+|z_{i+1}|)),\,|\Delta z_{i+1/2}|)\big)^3$
(page-local) to the bracket of the jump. It is realised by shifting
$\mathsf c_1$ by $-\tfrac14 g_{\mathrm c}/(1-1/r_i)$ and $\mathsf c_2$ by
$-\tfrac14 g_{\mathrm c}/(1-r_{i+1})$ (Eqs. (21)–(22)). It keeps every
SP-WENO property except the jump bound.

## DSP-WENO: a learned point of the feasible region

Charles & Ray define the **feasible region**: for given ratios, the set
of $(\mathsf c_1,\mathsf c_2)$ that satisfies consistency, the sign
constraint and the order constraint (Definition 1, §3.3). Their vertex
algorithm builds it as a convex polygon with at most five vertices, case
by case over six disjoint subdomains of the ratio plane (§4.1, Algorithm
SM1). The search box has half-width
$\min(\max(|\Delta z^*_{i-1/2}|,|\Delta z^*_{i+1/2}|,|\Delta z^*_{i+3/2}|),\cdot)$,
capped at $\tfrac18$ above and $\tfrac38$ below. Here $z^*$ are the stencil
values divided by $\max(1,\max|z|)$. The box is $O(\Delta x)$ for smooth
data and can grow to the whole consistency box near a jump.

The zero-jump line cuts the box into a triangle and a pentagon. A
triangle on the zero-jump side would bias the choice toward zero
dissipation. So one of its vertices is replaced by a vertex pulled away
from the line, and the centroid is added twice. At least one vertex stays
on the line, for smooth accuracy (Remarks SM2–SM4; the shift is "picked
empirically").

A multilayer perceptron (3 hidden layers of 5 ReLU neurons, softmax
output, 120 parameters) maps five scale-invariant features to five convex
weights. The perturbations are the convex combination of the polygon
vertices (Eqs. (24)–(30)). The features are the three scaled jumps and
$\tanh$ of the two ratios. Every network output is therefore consistent, has
the sign property and is third-order accurate on smooth data **by
construction**. The authors prefer this strong imposition to a penalty in
the loss, which could not guarantee the sign property (§6).

The training data are 100,000 four-point samples of random cubics, sines
and piecewise-linear jumps, half smooth and half discontinuous. No PDE
solutions are used, and one trained network serves scalar advection,
Burgers and 1D/2D Euler (§4.2–4.3, Table 1;
[learned WENO weights](/methods/learned-weno-weights.md)).

Proved and lost properties:

- **Jump bound** (Lemma SM1, Eq. (32)):
  $|[\![z]\!]^{\mathrm{rec}}_{i+1/2}|\le\tfrac12|\Delta z_{i-1/2}|+|\Delta z_{i+1/2}|+\tfrac12|\Delta z_{i+3/2}|$.
  The proof uses only consistency, so the bound holds for every variant
  of the form.
- **Mirror property** lost, through the vertex algorithm and the network
  (§4.4).
- **No positivity**: no constraint enforces it (Remark 5).

## Evidence

All runs use the TeCNO4 flux, which is the fourth-order
LeFloch–Mercier–Rohde entropy-conservative flux plus Roe-type dissipation
on the reconstructed jumps, with SSP-RK3
([TeCNO schemes](/methods/tecno-scheme.md)).

- **Smooth accuracy.** In the reconstruction test every method is at
  least third order.
  SP-WENO and SP-WENOc super-converge (rates up to 3.82 on
  $\sin(10\pi x)+x$), which the authors attribute to the jump "often being
  zero" (Table 2, §5.2.1). On $\sin^4x$ advection (Test 2) at $N=1000$
  the $L^1$ errors are $1.66\times10^{-6}$ for DSP-WENO, $8.94\times10^{-7}$
  for SP-WENO and $8.90\times10^{-7}$ for SP-WENOc. ENO3 has a rate of
  1.32 there, which the authors attribute to the linear instability of
  ENO (Table 3). On the 2D [isentropic vortex](/benchmarks/isentropic-vortex.md)
  DSP-WENO reaches rates 3.13–3.30, SP-WENO and SP-WENOc 3.6–3.9, and ENO3
  about 2.2 (Table 4).
- **Shocks.** On modified Sod, Shu–Osher and Lax, SP-WENO and SP-WENOc
  overshoot at the shock. DSP-WENO shows "very minor" overshoots and
  resolves shocks about as well as ENO3 (§5.3, Figs. 6–8). On a Burgers
  Riemann problem every method oscillates, including minmod, which also
  has the sign property. The authors call this "a fundamental problem with
  high-order TeCNO schemes" (Remark 6).
- **Carbuncle.** On 2D Riemann configuration 3, SP-WENO and DSP-WENO
  show a carbuncle-like protrusion, and SP-WENOc does not. A Rusanov-type
  dissipation matrix $(|v|+c)I$ weakens it, so entropy stability alone
  does not prevent it (Fig. 10;
  [carbuncle phenomenon](/definitions/carbuncle-phenomenon.md)).
- **Cost.** On 100,000 random stencils the reconstruction takes 0.852 s
  (DSP-WENO), against 0.178 s (SP-WENO), 0.192 s (SP-WENOc) and 0.839 s
  (ENO3). The vertex search takes 95 % of the DSP-WENO time. Inside the
  solver DSP-WENO is 2–3 times as expensive at fine resolution. The
  authors attribute this to network queries one interface at a time
  (§5.2.2, Fig. 3).

## Qualifications

- Charles & Ray write that the errors of DSP-WENO "are about an order of
  magnitude larger than those of SP-WENO and SP-WENOc" in the advection
  tests (§5.2.1). Their Table 3 gives ratios of about 1.2 (Test 1) and 1.9
  (Test 2) at $N=1000$. The order of magnitude holds for the
  reconstruction-only Table 2 ($1.22\times10^{-6}$ against
  $1.68\times10^{-7}$ at $N=1280$) and for the vortex, Table 4 *(compiler
  check, not in the sources: ratios from the printed errors)*.
- §4.4 states that DSP-WENO keeps every SP-WENO property except the
  mirror property. This would include the jump bound
  $|[\![z]\!]^{\mathrm{rec}}|\le2|\Delta z|$, but only the weaker
  three-jump bound is proved. Remark SM5 attributes that bound to the sign
  constraint, while the proof uses consistency only.
- The first Euler entropy variable is printed as
  $-\beta|v|^2-(\gamma-s)/(\gamma-1)$ (p. 15, with the source's
  $\beta=\rho/(2p)$). Differentiating their own $\eta=-\rho s/(\gamma-1)$
  gives $(\gamma-s)/(\gamma-1)-\beta|v|^2$, the form printed by
  [Liu et al. (2025b)](/sources/liu-2025-b.md) (§2) *(compiler check, not
  in the sources)*.
- The scalar flux of Eq. (33) has no factor $\tfrac12$ in front of the
  dissipation that Eq. (11) carries. The paper does not comment.
- Evidence on the C-region and the shock behaviour is numerical. The
  lemma on the jump bound is the only new proof.

# Citations

- [Charles & Ray (2025)](/sources/charles-2025.md) — arXiv v2: §1, §2 Eqs. (3)–(11), §3 Eqs. (12)–(22), Definition 1, §4 Eqs. (24)–(32), §4.4, Remark 5, §5 Tables 2–4, Figs. 3–10, Remark 6, §6, SM1–SM3 (Table SM1, Algorithm SM1, Lemma SM1, Remarks SM2–SM5).
- [Liu et al. (2025b)](/sources/liu-2025-b.md) — §2 (entropy variables of the Euler/MHD entropy).
- [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) — §4 (minmod and the sign property).
- [Bhoriya et al. (2023)](/sources/bhoriya-2023.md) — §4.1.2 (ENO reconstruction with the sign property).
- [Duan & Tang (2022)](/sources/duan-2022.md) — §4 (WENO with the sign switch).
- [Li, Duan & Tang (2022c)](/sources/li-2022-c.md) — §3.4 (WENO with the sign switch).
