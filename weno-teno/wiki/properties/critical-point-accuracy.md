---
type: Property
title: "Accuracy at critical points"
description: "A nonlinear reconstruction keeps its design order at a critical point, where the first m derivatives vanish, only if its weights still converge fast enough to the linear weights there; WENO-JS and WENO-Z lose orders, and mapped, ZN, symmetric-indicator and exponential weight designs restore them up to a scheme-dependent critical-point order or, for exponential weights, at any order."
status: established
aliases: [critical-point accuracy, accuracy near critical points, Cp-property, order degeneracy at extrema]
tags: [weno, reconstruction, finite-difference]
timestamp: 2026-10-23T23:00:00Z
---

# Accuracy at critical points

A point is an **$m$th-order critical point** of $f$ if $f'=\dots=f^{(m)}=0$ there and
$f^{(m+1)}\ne0$ (Deng 2023, Definition 3; Li et al. 2022b, notation of Tables 4–5). A smooth extremum
is a first-order critical point. A nonlinear reconstruction has the property when its observed order
at such points equals its design order; the bundle's sources measure it on $f(x)=x^ke^x$ at $x=0$, a
$(k-1)$th-order critical point (Li et al. 2022b, §4.1).

## Mechanism

At an $m$th-order critical point the [smoothness indicators](/definitions/smoothness-indicator.md)
lose their $O(\Delta x^2)$ leading term: for $r=4$ they become $\beta_k\sim A\Delta x^4$,
$B\Delta x^6$, $C_k\Delta x^8$ at the first, second and third order (Li et al. 2022b, Table 4; page-local
Taylor constants $A$, $B$, $C_k$). The
weight deviation $\omega_k-d_k$ is governed by ratios such as $\tau/\beta_k$, which lose the same
number of orders. Li et al. (2022b, Eqs. (12)–(13)) recall the conditions for the $(2r-1)$th order of
the finite-difference scheme: necessary and sufficient
$\sum_kA_k(\omega^+_k-\omega^-_k)=O(\Delta x^r)$ together with $\omega^\pm_k-d_k=O(\Delta x^{r-1})$,
sufficient $\omega^\pm_k-d_k=O(\Delta x^r)$, where $\pm$ marks the weights at $x_{i\pm1/2}$ (the
coefficients $A_k$ are not defined in the paper).

## Scheme by scheme

| scheme | behaviour at critical points | source |
|---|---|---|
| [WENO-JS](/methods/weno-js-reconstruction.md) | loses order: WENO5-JS 3.04–3.15 (1st), 2.00 (2nd), 3.39–3.72 (3rd); WENO7-JS 2.87–4.00, WENO9-JS 4.00–7.12 at the tested points | Li et al. 2022b, Tables 6–8 |
| [mapped WENO](/methods/mapped-weno.md) | the mapping restores the fifth-order condition at first-order critical points | Li et al. 2022b, §2 (recalled) |
| [WENO-Z](/methods/weno-z.md) | falls to the $r$th-order ENO rate when $\tau_{2r-1}$ and $\beta_k$ have leading terms of the same order; WENO5-Z 5.14–5.37 (1st) but 2.11–2.32 (2nd); WENO7-Z cannot improve at a 3rd-order point for $q=1$ or 2 (3.24–3.55) | Li et al. 2022b, §2, Table 4, Tables 6–7 |
| fifth-order WENO-ZN | fifth order at 1st and 2nd order with $q=2$; fifth/fourth with $q=1$; no improvement at 3rd order | Li et al. 2022b, §3.1 (recalled from the fifth-order paper), Table 6 |
| [WENO-ZN](/methods/weno-zn.md), order $2r-1$ | design order up to $(2r-4)$th-order critical points; WENO7-ZN 6.99–7.91 at 2nd–4th, WENO9-ZN 8.99–9.00 at 3rd–5th | Li et al. 2022b, Table 5, Tables 7–8 |
| WENO-Z$\eta$ (Fan) | up to $(r-1)$th-order points, with an $O(\Delta x^{2r+2})$ global indicator | Li et al. 2022b, §3.3 (derived) |
| OWENO (Baeza et al.) | optimal order at critical points of any order | Li et al. 2022b, §2 (recalled) |
| [TENO](/methods/targeted-eno.md) | design order on a test function with a second-order critical point, no tuning of $\epsilon$ | Fu 2023, §3.1 (stated, numerics in cited work) |
| fifth-order [multi-resolution WENO](/methods/multi-resolution-weno.md) | $\omega_m=d_m+O(\Delta x^4)$ also at first-order critical points, since $\tau$ and the indicators both drop by two orders there; no critical-point test | Wang et al. 2021, Eqs. (3.18)–(3.20) (derived) |
| sixth-order [RBF-based WENO](/methods/rbf-weno.md) (WENO-G) | $\lvert\omega_k-\bar d_k\rvert\le c\Delta x^4$ "regardless of critical points" for $\epsilon=\Delta x^\ell$, $0<\ell\le4(2q-1)/q$; 6.01 on $\sin(2\pi x-\sin(2\pi x)/\pi)$, where WENO-JS gives 3.54–4.13 | Jeong, Yang & Yoon 2022, Prop. 4.5, Table 2 |
| MR-AWENO-Si ([multi-resolution WENO](/methods/multi-resolution-weno.md)) | $\tau^*=O(\Delta x^{10})$ at first- to third-order critical points is said to recover the order; no proof, no critical-point test | Li, Li, Don & Wang 2023a, §2.3 (stated) |
| [exponential weights](/methods/exponential-nonlinear-weights.md) (WCNS-EXP, interpolation) | fifth order on $x^ke^{0.75(x-1)}$ for every $k=1,\dots,6$, i.e. critical points of order 0 to 5, in quadruple precision | Chen & Deng 2023, Theorem 3.1 (argued), §4.1, Fig. 2 |
| WCNS-JS, WCNS-Z, modified WCNS-MR (interpolation) | third order at $k=2$ for JS and MR, JS back to fifth once $\beta_k<\epsilon=10^{-6}$; Z and MR from second to fifth order as $k$ goes from 3 to 6 | Chen & Deng 2023, §4.1, Fig. 2 |
| WENO-NS, WENO-P (Ha et al., Kim et al.) | sufficient condition at first-order critical points; not optimal at second-order ones ($L_1$ 3.3–3.6, $L_2$ 2.9–3.1 on $\sin^3(\pi x)$) | Zhong et al. 2023, §2 (recalled), Table 4 |
| MWENO-P (Rathan & Naga Raju) | sufficient condition at first- and second-order critical points; about fifth order on $\sin^3(\pi x)$ | Zhong et al. 2023, §2 (recalled), Table 4 |
| IMWENO-P | $\omega_k-d_k=O(\Delta x^3)$ claimed at second-order critical points (the printed chain gives $O(\Delta x^2)$, see below); $L_1$ orders 4.94–5.15 on $\sin^3(\pi x)$ | Zhong et al. 2023, §3.3, Eqs. (27)–(41), Table 4 |

Li et al. (2022b, §4.1) also recall that the WENO-Z of Don & Borges with $\epsilon=\Delta x^m$ satisfies a
sufficient condition for optimal order, and reject it for its dimensional inconsistency. Hong, Ye & Ye (2022, §1) recall
the same Don & Borges $\epsilon(\Delta x)$ remedy and Henrick et al.'s analysis of WENO-JS at critical
points, as background for TENO. Jeong et al.'s Proposition 4.5 also uses $\epsilon=\Delta x^\ell$: its proof
assumes $\beta_k=A_k\Delta x^{r_\beta}+\dots$ with $r_\beta\ge2$ and $\tau=O(\Delta x^8)$ (page-local
exponent $r_\beta$), and the experiments do not state the value of $\epsilon$ actually used.

## Interpolation and flux conditions

Chen & Deng (2023, Eq. (25)), recalling Deng & Zhang, state the condition for fifth-order WCNS
*interpolation* as $\omega_k=d_k+O(\Delta x^2)$, against the sufficient $O(\Delta x^3)$ (that is,
$O(\Delta x^r)$ for $r=3$) of finite-difference flux reconstruction recalled by Li et al. (2022b) and
Zhong et al. (2023, Eq. (11)). The two are consistent. *(Compiler check, not in the sources: the
third-order candidates give $\sum_k(\omega_k-d_k)u^{(k)}_{i+1/2}=\sum_k(\omega_k-d_k)\big(u^{(k)}_{i+1/2}-u_{i+1/2}\big)$,
of order $O(\Delta x^2)\cdot O(\Delta x^3)$, while the flux difference of a reconstruction divides by
$\Delta x$ and costs one order.)*

Chen & Deng build their [exponential weights](/methods/exponential-nonlinear-weights.md) on this
interpolation condition. In the limit where the stencil-local exponent $\lambda_{\mathrm E}$ equals 1,
$\alpha_k=d_ke^{-\beta_k}=d_k+O(\Delta x^2)$ for any smooth data, so the order holds at every
critical-point order provided $\lambda_{\mathrm E}\to1$. The weights use only stencil data and no
$\Delta x$-dependent $\epsilon$; the authors set them against earlier unconditionally optimal weights
that rely on dimensional parameters or global data, and against Baeza et al.'s, whose local-data
framework excludes third order (§1).

## Second-order critical points: symmetric indicators (IMWENO-P)

Zhong, Wang, Qiu & Gao (2023, §3) build fifth-order finite-volume weights for second-order critical
points from the $L^1$-type indicator line of WENO-NS, WENO-P and MWENO-P. Their indicators
$\beta^{\mathrm{IMP}}_k$ and global indicator $\tau^{\mathrm{IMP}}$, the squared undivided fourth
difference (page-local; the source's $\bar\beta_s$, $\bar\zeta$), are recorded on
[smoothness indicators](/definitions/smoothness-indicator.md). With Z-type weights of exponent $q=1$
and the Taylor expansions of the indicators (Eqs. (27)–(29)), all at $x_{i+1/2}$:

- for $f'\ne0$, $\beta^{\mathrm{IMP}}_k=4(f')^2\Delta x^3+O(\Delta x^4)$ and $\omega_k=(d_k+O(\Delta x^6))/(1+O(\Delta x^6))$ (Eqs. (30)–(31));
- for $f'=0\ne f''$, $\beta^{\mathrm{IMP}}_k=(f'')^2\Delta x^4+O(\Delta x^5)$ and $\omega_k=(d_k+O(\Delta x^5))/(1+O(\Delta x^5))$ (Eqs. (32)–(33));
- for $f'=f''=0\ne f'''$, $\beta^{\mathrm{IMP}}_0=\tfrac94(f''')^2\Delta x^6$, $\beta^{\mathrm{IMP}}_{1,2}=\tfrac14(f''')^2\Delta x^6$, and the
  paper concludes $\omega_k=d_k+O(\Delta x^3)$, the sufficient condition (Eqs. (34)–(41)).

The odd power $\Delta x^3$ in the first case comes from their fixed parameter $\xi_{\mathrm{NS}}=\Delta x$ (page-local; the source's $\xi$) of the
first-difference term.

In the third case Eqs. (35)–(36) print $\tau^{\mathrm{IMP}}/\beta^{\mathrm{IMP}}_k=c_k\tilde D\Delta x^2+O(\Delta x^3)$ with
$c_0=\tfrac19$, $c_1=c_2=1$ and $\tilde D=(2f^{(4)}/f''')^2$ (page-local $c_k$, $\tilde D$). *(Compiler check, not
in the sources: normalizing gives
$\omega_0-d_0=-\tfrac89d_0(1-d_0)\tilde D\Delta x^2+O(\Delta x^3)=-\tfrac8{25}\big(f^{(4)}/f'''\big)^2\Delta x^2+O(\Delta x^3)$
for $d_0=\tfrac1{10}$, nonzero when $f^{(4)}\ne0$; a symbolic expansion of the cell averages reproduces Eq. (34)
and this coefficient. The printed steps (38)–(41) divide $1+O(\Delta x^3)$ by $1+O(\Delta x^2)$ and keep
$O(\Delta x^3)$; they support only $\omega_k-d_k=O(\Delta x^2)$.)* Fifth order would then need the
necessary-and-sufficient condition that Li et al. (2022b, Eqs. (12)–(13)) recall, on the difference of the
weights between neighbouring interfaces. Zhong et al. do not examine it.

The numerical evidence (Tables 2–5):
- **$\sin^3(\pi x)$**, a second-order critical point at $x=0$: WENO-JS, WENO-Z, WENO-NS and WENO-P
  fall to $L_1$ orders 3.3–3.6 and $L_2$ orders 2.9–3.1. MWENO-P and IMWENO-P stay near 5
  (IMWENO-P $L_1$ error $8.17\times10^{-9}$ at $N_x=500$).
- **$\sin(\pi x-\sin(\pi x)/\pi)$**: WENO-JS reaches $L_1$ 4.19 and $L_2$ 3.69 at $N_x=500$, IMWENO-P
  5.00.
- **Long-time advection of $\sin^9(\pi x)$** to $t=1000$: IMWENO-P's $L_1$ error is within $-0.53\%$
  of the linear-weight scheme, against $+3647\%$ for WENO-JS, $+1731\%$ for WENO-Z and $+9.28\%$ for
  MWENO-P (Table 5).

These are convergence rates of advected solutions; the function tests of Li et al. (2022b) above
measure the reconstruction alone, so the WENO5-Z orders at second-order points (2.11–2.32 there, $L_1$
about 3.3 here) come from different measurements.

## Accuracy analyses that assume $f'\ne0$

Several order arguments in the bundle stop short of critical points:

- Wong et al. (2021, App. B, Eqs. (B.20)–(B.21)) obtain $\tau^{\mathrm{ref}}_5/(\beta_k+\epsilon)=O(\Delta x^4)$
  for the incremental-stencil interpolation of WCNS-IS, and with it fifth order, explicitly "provided"
  the point is not a critical point ([WCNS](/methods/weighted-compact-nonlinear-scheme.md));
- Li, Shu & Qiu (2022d, Remark 1, Eq. (2.29)) derive sixth order for their multi-resolution Hermite
  WENO from $\beta_l=u'^2\Delta x^2+O(\Delta x^4)$, i.e. assuming $u'\ne0$, and do not discuss critical
  points ([Hermite WENO](/methods/hermite-weno.md));
- Wang et al. (2021) cover $f'\ne0$ and $f'=0,\ f''\ne0$ only (table above).

*(Compiler check, not in the sources, for the multi-resolution case: at $f'=0$, $f''\ne0$ the
indicators become $\tfrac14(f'')^2\Delta x^4$ for the one-point base and $\tfrac{13}{12}(f'')^2\Delta x^4$
for the three- and five-point candidates, so $|\beta_3-\beta_1|=\tfrac56(f'')^2\Delta x^4+\dots$ and
$\tau=O(\Delta x^8)$, $\tau/\beta_m=O(\Delta x^4)$, as Wang et al. state.)*

## Third-order compact schemes

Deng (2023, §1) recalls that third-order WENO schemes on the three-cell stencil "always fail to obtain
the expected order near critical points", and locates critical points with the normalized cell average
$\tilde u_i=(\bar u_i-\bar u_{i-1})/(\bar u_{i+1}-\bar u_{i-1})$
([normalised-variable diagram](/definitions/normalised-variable-diagram.md)). Lemma 1: without a
critical point in the stencil, $\tilde u_i=\tfrac12-\frac{f''(x_c)\Delta x}{4f'(x_c)}+O(\Delta x^2)$.
Lemma 2: at a first-order critical point $x_c=x_{i-1/2}+\delta\Delta x$, $\delta\ne\tfrac12$,
$\tilde u_i=\delta/(2\delta-1)+O(\Delta x)$. Proposition 1: on fine meshes a critical point inside
$I_i$ gives $\tilde u_i<0$ or $>1$, one in $I_{i-1}$ gives $0<\tilde u_i<\tfrac12$, one in $I_{i+1}$
gives $\tfrac12<\tilde u_i<1$. Huang et al. (2026, §3.4) use the first statement to read
$\tilde u_i<0$ as "cell $i$ contains a critical point" when they analyse the learned WENO3-NN, which
moves from the second-order upwind towards the second-order central reconstruction there
([learned WENO weights](/methods/learned-weno-weights.md)).

On $\sin(\pi x)$, which has first-order critical points at $x=\pm\tfrac12$, the compact schemes of
Huang et al. (2026, Table 3) converge at $L_1$ orders 2.4–2.6 and $L_\infty$ orders 1.6–1.7
(WENO3-NN, ROUND, LD-ROUND, $t=20$, $N_x=320$–$1280$); the paper does not comment on the order.

Bezgin, Schmidt & Adams (2022, §3.4, Fig. 2) measure the $L_2$ convergence of the face reconstruction
of a function, not of a PDE solution: on $\tanh(2x)$, which has no critical point, WENO3-JS, WENO3-Z
and WENO3-NN reach 3.00, 3.01 and 2.93; on $\sin^3(\pi x)$ on $[-1,1]$, with a saddle point at $x=0$
*(compiler check, not in the sources: $\sin^3(\pi x)=\pi^3x^3+O(x^5)$, so $f'=f''=0\ne f^{(3)}$ at $x=0$, a
second-order critical point)*, all three fall to 2.44, 2.40 and 2.33. Plotting
$\omega_0$, they find that WENO3-JS and WENO3-Z "degenerate at the saddle point" while WENO3-NN
"distinguish[es]" it, as does WENO-F3+ (§3.5, Fig. 4); the order is not improved by it
([learned WENO weights](/methods/learned-weno-weights.md)).

## Second-order limiters

Chen, Zhang, Liu & Chen (2022, §1) state that second-order TVD-type slope limiters "typically loss
their designed accuracy at smooth critical points" and, citing Zhang, Liu & Chen (2018, the MLP-pw
limiter), that several common limiters
"cannot strictly guarantee the monotonicity principle"; their WENO-type weighting of vertex gradients
replaces the limiter. The only evidence is the isentropic vortex on triangles, where the weighted and
the linear schemes have the same error on the two finest meshes (last order 1.90) and the weighted one
a larger error on the coarsest (Table 1); no extremum test is run
([gradient reconstruction on unstructured meshes](/methods/unstructured-gradient-reconstruction.md),
[TVD limiters](/definitions/total-variation-diminishing.md)).

## Weight of the evidence

Fu (2023, §2.3) recalls Acker et al.'s finding that raising the weights of the less-smooth stencils
matters more for resolution than keeping the order at critical points, and Li et al. (2022b, §2)
relay Baeza et al.'s caveat that shock performance depends on how far from zero the weights of
discontinuous stencils are, not on accuracy at critical points. The improvement at critical points is
therefore one design target among several ([WENO-Z+](/methods/weno-z-plus.md) trades it for
resolution).

## Qualifications

- *(Compiler check, not in the sources.)* Lemma 2 gives sharper bounds than Proposition 1 states:
  $\delta\in(-1,0)$ (critical point in $I_{i-1}$) maps to $0<\tilde u_i<\tfrac13$ and
  $\delta\in(1,2)$ (in $I_{i+1}$) to $\tfrac23<\tilde u_i<1$. Proposition 1 is correct but weaker.
- The WENO-ZN order count of Li et al. ignores the adaptive term of the weight; see the
  Qualifications of [WENO-ZN](/methods/weno-zn.md).
- Li et al. (2023a, §2.3) argue from the order of $\tau^*$ alone. *(Compiler check, not in the sources:
  $\tau^*$ is $O(\Delta x^{10})$ for any smooth data, critical point or not; what decides the weights is
  $\tau^*/(\beta_k+\epsilon\mathsf m^2)$, and at an $m$th-order critical point $\beta_k$ also drops to
  $O(\Delta x^{2m+2})$, which their statement does not examine.)*
- Wang & Don (2022) name the property ("Cp-property") but run no critical-point test of their
  affine-invariant weights ([affine-invariant WENO](/methods/affine-invariant-weno.md)).
- Chen & Deng's Theorem 3.1 concerns the interpolation; the order of the full WCNS derivative at
  critical points is not tested. The comparator WCNS-MR is their modification of the published scheme
  ([multi-resolution WENO](/methods/multi-resolution-weno.md)).
- Zhong et al. (2023, Example 2) write that $\sin(\pi x-\sin(\pi x)/\pi)$ "satisfies $u'=0$ and
  $u'''\ne0$", while their §4.2 says Examples 1 and 2 "only have first-order critical points".
  *(Compiler check, not in the sources: with $g=\pi x-\sin(\pi x)/\pi$, $g'=\pi-\cos(\pi x)>0$, and
  wherever $(\sin g)'=0$ one has $(\sin g)''=-\sin(g)\,g'^2\ne0$; the points are first-order critical
  points, as §4.2 says.)*

# Citations

- [Li et al. (2022b)](/sources/li-2022-b.md) — §1–§2, Eqs. (12)–(23), Table 4; §3, Table 5; §4.1, Tables 6–8.
- [Deng (2023)](/sources/deng-2023.md) — §1; §2.2, Def. 3, Lemmas 1–2, Prop. 1.
- [Huang et al. (2026)](/sources/huang-2026.md) — §3.4; §6.1, Table 3.
- [Fu (2023)](/sources/fu-2023.md) — §2.3; §3.1.
- [Wang & Don (2022)](/sources/wang-2022-b.md) — Cp-property named, not tested.
- [Wang et al. (2021)](/sources/wang-2021.md) — §3.1.1, Eqs. (3.13)–(3.20).
- [Wong et al. (2021)](/sources/wong-2021.md) — App. B, Eqs. (B.14)–(B.21).
- [Li, Shu & Qiu (2022d)](/sources/li-2022-d.md) — §2.1, Remark 1, Eq. (2.29).
- [Bezgin, Schmidt & Adams (2022)](/sources/bezgin-2022.md) — §3.4, Fig. 2; §3.5, Fig. 4.
- [Chen, Zhang, Liu & Chen (2022)](/sources/chen-2022.md) — §1; §6.3, Table 1.
- [Jeong, Yang & Yoon (2022)](/sources/jeong-2022.md) — §4.3, Prop. 4.5, Eqs. (39)–(43); §5, Table 2.
- [Li, Li, Don & Wang (2023a)](/sources/li-2023.md) — §2.3 (properties of $\tau^*$).
- [Hong, Ye & Ye (2022)](/sources/hong-2022.md) — §1.
- [Chen & Deng (2023)](/sources/chen-2023.md) — §1; §3, Eqs. (25)–(34), Theorem 3.1; §4.1, Fig. 2.
- [Zhong et al. (2023)](/sources/zhong-2023.md) — §2, Eqs. (10)–(18); §3.3, Eqs. (27)–(41); §4.1, Tables 2–5; §4.2.
