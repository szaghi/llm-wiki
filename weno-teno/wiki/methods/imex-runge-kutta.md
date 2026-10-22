---
type: Method
title: "IMEX Runge–Kutta schemes"
description: "Implicit–explicit Runge–Kutta schemes pair an explicit tableau for the non-stiff terms with a diagonally implicit one for the stiff terms; the page records the type A/CK/ARS classification, stiff accuracy, the partitioned semi-implicit form used for all-Mach Euler and MHD, the SI-IMEX(4,4,3) and (3,3,2) tableaux and their order check, and additive schemes with stiff local sources solved cell by cell."
status: established
aliases: [IMEX-RK, implicit-explicit Runge–Kutta, additive Runge–Kutta, ARK-IMEX, SI-IMEX, semi-implicit IMEX Runge–Kutta, partitioned IMEX Runge–Kutta, IMEX TVD Runge–Kutta]
tags: [asymptotic-preserving, imex, semi-implicit, finite-difference, relativistic, mhd]
timestamp: 2026-10-23T12:00:00Z
---

# IMEX Runge–Kutta schemes

An **implicit–explicit (IMEX) Runge–Kutta** scheme integrates a semi-discrete system whose
right-hand side has a non-stiff part, treated explicitly, and a stiff part (a relaxation
source, an acoustic pressure term scaled by an inverse Mach number), treated implicitly,
with two Butcher tableaux sharing the stage structure. In this bundle IMEX schemes are the
stepper of [asymptotic-preserving](/properties/asymptotic-preservation.md) discretizations:
the implicit treatment of the stiff term removes a time-step restriction that would
otherwise scale with the small parameter, and the structure of the implicit tableau decides
whether the scheme has the right limit.

Page-local notation: $(\tilde{\mathsf a}_{ij},\tilde{\mathsf b}_i,\tilde{\mathsf c}_i)$ is the
explicit tableau ($\tilde{\mathsf a}_{ij}=0$ for $j\ge i$), $(\mathsf a_{ij},\mathsf b_i,\mathsf c_i)$
the diagonally implicit one ($\mathsf a_{ij}=0$ for $j>i$), with $\tilde{\mathsf c}_i=\sum_{j<i}\tilde{\mathsf a}_{ij}$,
$\mathsf c_i=\sum_{j\le i}\mathsf a_{ij}$ and $s$ stages; $\tilde{\mathsf A}$, $\mathsf A$,
$\mathsf b$, $\tilde{\mathsf c}$, $\mathsf c$ are the matrices and vectors (sans-serif, to keep
$A$ for the flux Jacobian and $b$ for the TENO-A constants). $\gamma_{\mathrm{D}}$ denotes the
common diagonal entry of an SDIRK tableau (not the ratio of specific heats $\gamma$).

## Partitioned (semi-implicit) form

[Boscarino et al. (2022)](/sources/boscarino-2022.md) (§3.2.1, Eqs. (3.20)–(3.27)) use the
partitioned form of Boscarino, Pareschi and Russo: the right-hand side is written as a
function $\mathcal H(u_E,u_I)$ (page-local) of an explicitly and an implicitly treated
argument, and the system $u'=\mathcal H(u,u)$ is doubled into $u_E'=\mathcal H(u_E,u_I)$,
$u_I'=\mathcal H(u_E,u_I)$ with $u_E(t^n)=u_I(t^n)=u^n$. The stages are

$$\begin{aligned}
u_E^{(i)}&=u^n+\Delta t\sum_{j=1}^{i-1}\tilde{\mathsf a}_{ij}\,\mathcal H\big(u_E^{(j)},u_I^{(j)}\big),\\
u_I^{(i)}&=u^n+\Delta t\sum_{j=1}^{i-1}\mathsf a_{ij}\,\mathcal H\big(u_E^{(j)},u_I^{(j)}\big)+\Delta t\,\mathsf a_{ii}\,\mathcal H\big(u_E^{(i)},u_I^{(i)}\big),\\
u^{n+1}&=u^n+\Delta t\sum_{i=1}^{s}\mathsf b_i\,\mathcal H\big(u_E^{(i)},u_I^{(i)}\big).
\end{aligned}$$

Because $\mathcal H$ is linear in the implicit argument for the splittings used there (the
implicit argument enters through the pressure gradient and the energy flux only), each
implicit stage is a linear solve; for the all-Mach Euler system it reduces to one linear
elliptic equation for a pressure perturbation (see
[semi-implicit all-Mach schemes](/methods/semi-implicit-all-mach-scheme.md)). Taking
$\tilde{\mathsf b}=\mathsf b$ keeps $u_E^n=u_I^n$ at every step, so only one solution is stored;
a different $\tilde{\mathsf b}$ would give an embedded estimate for step-size control (§3.2.2,
item 3). The additive form, explicit tableau on one term and implicit tableau on another, is
the special case $\mathcal H(u_E,u_I)=\mathcal F(u_E)+\mathcal G(u_I)$ (page-local $\mathcal F$,
$\mathcal G$).

## Classification and stiff accuracy

Following Boscarino, as recalled by Boscarino et al. (2022) (§3.2.1):

- **type A**: $\mathsf A$ invertible;
- **type CK**: $\mathsf A=\begin{pmatrix}0&0\\ \mathsf a&\hat{\mathsf A}\end{pmatrix}$ with
  $\hat{\mathsf A}$ invertible (page-local block $\hat{\mathsf A}$, column $\mathsf a$);
- **type ARS**: type CK with additionally $\mathsf a=0$ and $\mathsf b_1=0$;
- **stiffly accurate (SA)**: $\mathsf b^\top=e_s^\top\mathsf A$ and $\mathsf c_s=1$, so
  $u^{n+1}$ equals the last implicit stage.

Two design consequences are stated for the low-Mach application (§3.2.2): stiff accuracy of
the implicit part is what the asymptotic-preservation and asymptotic-accuracy analysis needs,
and, citing Hairer and Wanner, an A-stable SA implicit part is L-stable (item 1); type A
($\mathsf a_{11}\ne0$) is "critical" because with $\mathsf a_{11}=0$, e.g. an ARS scheme, the
first stage has no pressure equation and "no proper value" of the hydrodynamic pressure, which
also matters for non-well-prepared initial data (item 2). With $\mathsf A$ invertible,
$\mathsf c_1\ne\tilde{\mathsf c}_1=0$; to simplify the order conditions the authors impose
$\mathsf c_i=\tilde{\mathsf c}_i$ for $i=2,\dots,s$ (item 4).

**First order.** The first-order semi-implicit step of Boscarino et al. is the type-A tableau
$\tilde{\mathsf c}=0$, $\tilde{\mathsf a}=0$, $\tilde{\mathsf b}=1$; $\mathsf c=\mathsf a_{11}=\mathsf b=1$
applied to the partitioned system: $u_E^{(1)}=u^n$, $u^{n+1}=u_I^{(1)}=u^n+\Delta t\,\mathcal H(u^n,u^{n+1})$
(Remark 3.1, Eq. (3.28)). [Arun et al. (2022)](/sources/arun-2022.md) (§3, Eqs. (3.1)–(3.2))
use a step of the same kind for the barotropic Euler equations with gravity and friction:
forward Euler on the momentum flux, pressure and gravity, backward Euler on the momentum that
enters the mass flux and the friction; eliminating the implicit momentum gives an explicit
scheme with $\varepsilon$- and $\Delta t$-dependent coefficients
([asymptotic preservation](/properties/asymptotic-preservation.md)).

## SI-IMEX(4,4,3) and SI-IMEX(3,3,2)

Boscarino et al. (§3.2.2, Eqs. (3.30)–(3.31)) build two type-A, stiffly accurate schemes with
$\tilde{\mathsf b}=\mathsf b$ and $\mathsf c_i=\tilde{\mathsf c}_i$ for $i\ge2$; the label
$(s,\sigma,p)$ counts implicit stages, explicit stages and order. **SI-IMEX(4,4,3)**, with
$\gamma_{\mathrm D}=0.435866521508$:

| $\tilde{\mathsf c}$ | $\tilde{\mathsf A}$ | | | |
|---|---|---|---|---|
| $0$ | $0$ | $0$ | $0$ | $0$ |
| $\gamma_{\mathrm D}$ | $\gamma_{\mathrm D}$ | $0$ | $0$ | $0$ |
| $0.717933260754$ | $0.435866521508$ | $0.282066739245$ | $0$ | $0$ |
| $1$ | $-0.733534082748750$ | $2.150527381100$ | $-0.416993298352$ | $0$ |
| $\tilde{\mathsf b}$ | $0$ | $1.208496649176$ | $-0.644363170684$ | $\gamma_{\mathrm D}$ |

| $\mathsf c$ | $\mathsf A$ | | | |
|---|---|---|---|---|
| $\gamma_{\mathrm D}$ | $\gamma_{\mathrm D}$ | $0$ | $0$ | $0$ |
| $\gamma_{\mathrm D}$ | $0$ | $\gamma_{\mathrm D}$ | $0$ | $0$ |
| $0.717933260754$ | $0$ | $0.282066739245$ | $\gamma_{\mathrm D}$ | $0$ |
| $1$ | $0$ | $1.208496649176$ | $-0.644363170684$ | $\gamma_{\mathrm D}$ |
| $\mathsf b$ | $0$ | $1.208496649176$ | $-0.644363170684$ | $\gamma_{\mathrm D}$ |

**SI-IMEX(3,3,2)**, with $\gamma_{\mathrm D}=1-\sqrt2/2$ and $\delta_{\mathrm D}=-2\sqrt2/3$
(page-local): explicit $\tilde{\mathsf c}=(0,\gamma_{\mathrm D},1)$, $\tilde{\mathsf a}_{21}=\gamma_{\mathrm D}$,
$\tilde{\mathsf a}_{31}=\delta_{\mathrm D}$, $\tilde{\mathsf a}_{32}=1-\delta_{\mathrm D}$; implicit
$\mathsf c=(\gamma_{\mathrm D},\gamma_{\mathrm D},1)$, $\mathsf a_{11}=\mathsf a_{22}=\mathsf a_{33}=\gamma_{\mathrm D}$,
$\mathsf a_{32}=1-\gamma_{\mathrm D}$, other entries zero; $\mathsf b=\tilde{\mathsf b}=(0,1-\gamma_{\mathrm D},\gamma_{\mathrm D})$.

The paper states that the third-order conditions of Pareschi and Russo were imposed and does
not list them. *(compiler check, not in the sources: with the coefficients of Eq. (3.30) read
from the page image of the arXiv v2, both implicit parts are stiffly accurate with all
diagonal entries $\gamma_{\mathrm D}$, so $\mathsf A$ is invertible, and the stability function of
the (4,4,3) implicit part has $R(\infty)=1-\mathsf b^\top\mathsf A^{-1}\mathbf 1\approx2\times10^{-16}$.
For (4,4,3), $\sum_i\mathsf b_i=1$, $\mathsf b^\top\tilde{\mathsf c}=\mathsf b^\top\mathsf c=\tfrac12$,
$\mathsf b^\top(\tilde{\mathsf c}\circ\tilde{\mathsf c})=\mathsf b^\top(\mathsf c\circ\mathsf c)=\mathsf b^\top(\mathsf c\circ\tilde{\mathsf c})=\tfrac13$
and $\mathsf b^\top\mathsf A\mathsf c=\mathsf b^\top\mathsf A\tilde{\mathsf c}=\mathsf b^\top\tilde{\mathsf A}\mathsf c=\tfrac16$
to about $10^{-12}$, but $\mathsf b^\top\tilde{\mathsf A}\tilde{\mathsf c}=0.198849\ne\tfrac16$. The difference,
$\gamma_{\mathrm D}\sum_i\mathsf b_i\tilde{\mathsf a}_{i1}=-0.0322$, comes from the first stage, where
$\mathsf c_1\ne\tilde{\mathsf c}_1$ and $\tilde{\mathsf a}_{i1}\ne0$, so the simplification
$\mathsf c_i=\tilde{\mathsf c}_i$, $i\ge2$, does not carry $\mathsf b^\top\tilde{\mathsf A}\mathsf c=\tfrac16$
over to $\mathsf b^\top\tilde{\mathsf A}\tilde{\mathsf c}$. In the expansion of the partitioned stages,
$\mathsf b^\top\tilde{\mathsf A}\tilde{\mathsf c}$ is the coefficient of the elementary differential
with both inner derivatives taken in the explicit argument, so as printed the explicit
tableau is second order on that term; in particular, when $\mathcal H$ does not depend on its
implicit argument the scheme reduces to the explicit Runge–Kutta method
$(\tilde{\mathsf A},\mathsf b)$, which is then second order. Either a coefficient is
misprinted or the scheme is third order only on the terms the conditions above cover. For
(3,3,2), $\tilde{\mathsf b}^\top\tilde{\mathsf c}=\mathsf b^\top\mathsf c=2\gamma_{\mathrm D}-\gamma_{\mathrm D}^2=\tfrac12$
exactly.)* The paper does not test temporal order in isolation: its 1D and 2D convergence
tables are dominated by the spatial error (orders 4–5; Tables 5.1–5.2).

## Additive schemes with stiff local sources

When the stiff term is a source that couples the variables of one cell only, the implicit
stages are local nonlinear systems and need no global solver.

**Two-fluid relativistic plasma** ([Bhoriya et al. (2023)](/sources/bhoriya-2023.md), §5.2).
The flux divergence $F_{\mathrm{NS}}$ is explicit and the Lorentz-force and (resistive)
current sources $F_{\mathrm S}$ are implicit, in the additive form
$$u^{(m)}=u^n+\Delta t\sum_{l<m}\tilde{\mathsf a}_{ml}F_{\mathrm{NS}}(u^{(l)})+\Delta t\sum_{l\le m}\mathsf a_{ml}F_{\mathrm S}(u^{(l)}),\qquad
u^{n+1}=u^n+\Delta t\sum_l\tilde{\mathsf b}_lF_{\mathrm{NS}}(u^{(l)})+\Delta t\sum_l\mathsf b_lF_{\mathrm S}(u^{(l)}).$$
The second-order scheme is the L-stable one of Pareschi and Russo with two implicit stages,
$\mathsf a_{11}=\mathsf a_{22}=\gamma_{\mathrm D}=1-1/\sqrt2$, $\mathsf a_{21}=1-2\gamma_{\mathrm D}$,
$\tilde{\mathsf a}_{21}=1$ and $\mathsf b=\tilde{\mathsf b}=(\tfrac12,\tfrac12)$; the third- and
fourth-order schemes are the ARK3 and ARK4 schemes of Kennedy and Carpenter (ARK3 printed in
App. C, Table 5; ARK4 taken from the original). *(compiler check, not in the sources: for the
second-order implicit tableau $\mathsf b^\top\mathsf A^{-1}\mathbf 1=(4\gamma_{\mathrm D}-1)/(2\gamma_{\mathrm D}^2)=1$,
so $R(\infty)=0$, consistent with the stated L-stability, and all second-order and coupling
conditions hold.)* Each implicit stage is an $18\times18$ nonlinear system per cell, solved
by Newton's method with backtracking line search. The schemes reach orders 1.94, 3.21 and
3.92 on a forced smooth solution at 3200 cells, with errors comparable to the explicit SSP
schemes of the same order (Table 3).

Their timings (Table 4, "MPI-parallelized code on a CPU with 10 cores") show where the
implicit treatment pays: for the stiffest charge-to-mass ratio, $10^5/\sqrt{4\pi}$, at 800
cells the IMEX schemes take 12.11 s (second order) and 47.00 s (fourth order) against 413.55 s
and 374.54 s for the explicit ones; for $10^4/\sqrt{4\pi}$ at 800 cells the explicit third- and
fourth-order schemes are faster (13.04 s vs 22.14 s, 37.98 s vs 44.90 s), while the
second-order IMEX scheme is still faster (14.28 s vs 17.90 s). The authors read this as the
source setting the explicit time step on the coarser grids and the CFL limit on the finer
one.

**Radiation–matter coupling** ([López-Miralles et al. (2023)](/sources/lopezmiralles-2023.md),
§3.1, §3.3, Eq. (21)). An IMEX version of the Shu–Osher third-order
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md): each explicit stage
$u^*=\sum(\cdot)+\theta_{\mathrm s}\Delta t\,\mathcal L(u^{(\cdot)})$ is followed by an implicit
source step $u^{(\cdot)}=u^*+\theta_{\mathrm s}\Delta t\,S$ with the same stage weight
$\theta_{\mathrm s}=1,\tfrac14,\tfrac23$ (page-local). Only the radiation energy and flux are
updated implicitly, by an iterated linearized $4\times4$ solve per cell (LU), and the fluid
energy and momentum follow from conservation of the totals, so total energy and momentum are
conserved by the implicit step. The paper calls the scheme "IMEX third-order TVD Runge-Kutta"
but does not analyse its order or stiff accuracy.

**Partitioned form for MHD.** [Chen, Wu & Xiong (2023)](/sources/chen-2023-b.md) (§3.2) use the
partitioned semi-implicit form above for the low-Mach ideal MHD equations with constrained
transport, with the third-order stiffly accurate scheme of Boscarino et al. (2022) and of
Huang, Xing and Xiong (tableau not reprinted); stiff accuracy is the hypothesis of their
asymptotic-accuracy theorem (Thm. 4.2; [semi-implicit all-Mach schemes](/methods/semi-implicit-all-mach-scheme.md)).

## IMEX schemes in the sources

| Source | Scheme | Stiff term | Order |
|---|---|---|---|
| [Boscarino et al. (2022)](/sources/boscarino-2022.md) | SI-IMEX(4,4,3), (3,3,2), first-order type A I | acoustic pressure $\varepsilon^{-2}\nabla p$ and energy flux of full Euler at Mach number $\varepsilon$ | 3, 2, 1 |
| [Arun et al. (2022)](/sources/arun-2022.md) | first-order semi-implicit step after Boscarino–Pareschi–Russo | friction and momentum in the mass flux | 1 |
| [Balsara et al. (2024)](/sources/balsara-2024.md) | IMEX-SSP3(4,3,3) of Pareschi & Russo | stiff relaxation sources | 3; reduces to Shu–Osher [SSP-RK3](/methods/ssp-runge-kutta.md) when the source vanishes (§X) |
| [Chen, Wu & Xiong (2023)](/sources/chen-2023-b.md) | third-order SA SI-IMEX-RK of Boscarino et al. | acoustic pressure and enthalpy flux of ideal MHD at sonic Mach number $\varepsilon$ | 3 (first-order scheme analysed) |
| [Bhoriya et al. (2023)](/sources/bhoriya-2023.md) | Pareschi–Russo L-stable ARK2; Kennedy–Carpenter ARK3, ARK4 | Lorentz-force and resistive sources of two-fluid relativistic plasma | 2, 3, 4 |
| [López-Miralles et al. (2023)](/sources/lopezmiralles-2023.md) | IMEX extension of Shu–Osher SSP-RK3 | radiation four-force (absorption, scattering) | not analysed |

## Qualifications

- **Regime switching.** Arun et al. state that "standard Implicit-Explicit Runge-Kutta
  schemes are incapable of switching" between the hyperbolic and parabolic relaxation
  limits of their system (Abstract, §1), citing unified IMEX approaches as the fix; they do
  not test an IMEX-RK scheme. [Abgrall & Nassajian Mojarrad (2024)](/sources/abgrall-2024.md)
  (§1) state that IMEX-RK asymptotic-preserving methods have "order limitations" and build an
  explicit [deferred-correction](/methods/deferred-correction.md) alternative instead.
- **Uniform accuracy.** The asymptotic accuracy of SA type-A schemes (Boscarino et al.,
  Prop. 4.4) covers the limit $\varepsilon\to0$ only; at intermediate Mach numbers the same
  scheme loses order (Table 5.2: observed order 0.91 at $\varepsilon=10^{-2}$ on the last
  refinement; Fig. 5.3). Arun et al. attribute oscillations of their non-well-balanced variant
  at intermediate $\varepsilon$ to the same IMEX loss of accuracy (§5.2.1, Figs. 6–7, citing
  earlier work).
- **Order reduction at intermediate stiffness.** Chen, Wu & Xiong (Tables 5.2, 5.4) see the
  same loss as Boscarino et al. for MHD: at $\varepsilon=10^{-2}$ the 1D orders are 2.78, 1.11,
  1.72, 1.60 and the 2D errors do not decrease between $N=16$ and $N=64$, while the scheme is
  about fifth order at $\varepsilon=1$, $10^{-6}$ and $0$.
- **Printed ARK3 weights.** In Bhoriya et al.'s Table 5 the stiff weights $\mathsf b$
  (row $b^{[S]}$) differ from the non-stiff weights $\tilde{\mathsf b}$, which equal the last
  implicit row. *(compiler check, not in the sources: with the printed $\mathsf c=(0,\ 1767732205903/2027836641118,\ \tfrac35,\ 1)$,
  the printed $\mathsf b$ gives $\sum_l\mathsf b_l=1$ and $\sum_l\mathsf b_l\mathsf c_l=\tfrac12$ but
  $\sum_l\mathsf b_l\mathsf c_l^2=0.345754\ne\tfrac13$, while $\tilde{\mathsf b}$ gives $\tfrac13$.)*
- The explicit tableau of Eq. (3.30) carries a meaningless $0$ in the $\tilde{\mathsf c}$ column
  of its $\tilde{\mathsf b}$ row, and the order symbol $p$ of the label clashes with pressure; both
  are typographical.

# Citations

- [Boscarino et al. (2022)](/sources/boscarino-2022.md) — §3.2.1 (Eqs. (3.20)–(3.28), Remark 3.1), §3.2.2 (items 1–4, Eqs. (3.30)–(3.31)), Prop. 4.4, Tables 5.1–5.2, Fig. 5.3 (arXiv v2).
- [Arun et al. (2022)](/sources/arun-2022.md) — Abstract, §1, §3 (Eqs. (3.1)–(3.4)), §5.2.1 (arXiv v1).
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §X (Eqs. (10.1)–(10.7)).
- [Abgrall & Nassajian Mojarrad (2024)](/sources/abgrall-2024.md) — §1.
- [Bhoriya et al. (2023)](/sources/bhoriya-2023.md) — §5.1–5.2, §6.1 (Tables 2–4), App. C (Table 5) (arXiv v2).
- [López-Miralles et al. (2023)](/sources/lopezmiralles-2023.md) — §3.1 (Eqs. (18)–(22)), §3.3 (Eqs. (39)–(43)) (arXiv v1).
- [Chen, Wu & Xiong (2023)](/sources/chen-2023-b.md) — §3.2 (Eqs. (3.7)–(3.10)), Thm. 4.2, Tables 5.2, 5.4 (arXiv v1).
