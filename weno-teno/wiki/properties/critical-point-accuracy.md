---
type: Property
title: "Accuracy at critical points"
description: "A nonlinear reconstruction keeps its design order at a critical point, where the first m derivatives vanish, only if its weights still converge fast enough to the linear weights there; WENO-JS and WENO-Z lose orders, and mapped, ZN, symmetric-indicator and exponential weight designs restore them up to a scheme-dependent critical-point order or, for exponential weights, at any order."
status: established
aliases: [critical-point accuracy, accuracy near critical points, Cp-property, order degeneracy at extrema]
tags: [weno, reconstruction, finite-difference, critical-points]
timestamp: 2026-10-23T20:07:00Z
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
| fifth-order TENO-Z, TENO-A, TENO-LAD (global indicator $\tau_5$, fixed or floor-based cut-off) | design order at a first-order critical point; orders 3.00 to 2.26 at a second-order one and 4.01 to 3.26 at a third-order one | Tang 2024, §4.1, Tables 1–3 |
| TENO-AZ ([adaptive TENO](/methods/adaptive-teno.md)), cut-off $C_T=\min(10^{-5},\lvert\beta_0+\beta_2-2\beta_1\rvert)$ | errors of the linear fifth-order scheme at critical points of order 1, 2 and 3 | Tang 2024, §3, Eqs. (19)–(20); §4.1, Tables 1–3 |
| WENO5-NN ([learned WENO weights](/methods/learned-weno-weights.md)) | weights deviate less from $d_k$ than WENO5-JS near the saddle points of $\sin^3(\pi x)$; no order test | Nogueira et al. 2024, §3.4, Fig. 6 |
| fifth-order [multi-resolution WENO](/methods/multi-resolution-weno.md) | $\omega_m=d_m+O(\Delta x^4)$ also at first-order critical points, since $\tau$ and the indicators both drop by two orders there; no critical-point test | Wang et al. 2021, Eqs. (3.18)–(3.20) (derived) |
| sixth-order [RBF-based WENO](/methods/rbf-weno.md) (WENO-G) | $\lvert\omega_k-\bar d_k\rvert\le c\Delta x^4$ "regardless of critical points" for $\epsilon=\Delta x^\ell$, $0<\ell\le4(2q-1)/q$; 6.01 on $\sin(2\pi x-\sin(2\pi x)/\pi)$, where WENO-JS gives 3.54–4.13 | Jeong, Yang & Yoon 2022, Prop. 4.5, Table 2 |
| MR-AWENO-Si ([multi-resolution WENO](/methods/multi-resolution-weno.md)) | $\tau^*=O(\Delta x^{10})$ at first- to third-order critical points is said to recover the order; no proof, no critical-point test | Li, Li, Don & Wang 2023a, §2.3 (stated) |
| sixth-order WENO-CU6-type, TENO6 and TENO6-SA; seventh-order WENO7-Z | rates at critical points of order 0–6 between 2 and 7, see the next section | Zhang et al. 2024b, §5.4, Table 3 |
| [exponential weights](/methods/exponential-nonlinear-weights.md) (WCNS-EXP, interpolation) | fifth order on $x^ke^{0.75(x-1)}$ for every $k=1,\dots,6$, i.e. critical points of order 0 to 5, in quadruple precision | Chen & Deng 2023, Theorem 3.1 (argued), §4.1, Fig. 2 |
| WCNS-JS, WCNS-Z, modified WCNS-MR (interpolation) | third order at $k=2$ for JS and MR, JS back to fifth once $\beta_k<\epsilon=10^{-6}$; Z and MR from second to fifth order as $k$ goes from 3 to 6 | Chen & Deng 2023, §4.1, Fig. 2 |
| WENO-NS, WENO-P (Ha et al., Kim et al.) | sufficient condition at first-order critical points; not optimal at second-order ones ($L_1$ 3.3–3.6, $L_2$ 2.9–3.1 on $\sin^3(\pi x)$) | Zhong et al. 2023, §2 (recalled), Table 4 |
| MWENO-P (Rathan & Naga Raju) | sufficient condition at first- and second-order critical points; about fifth order on $\sin^3(\pi x)$ | Zhong et al. 2023, §2 (recalled), Table 4 |
| IMWENO-P | $\omega_k-d_k=O(\Delta x^3)$ claimed at second-order critical points (the printed chain gives $O(\Delta x^2)$, see below); $L_1$ orders 4.94–5.15 on $\sin^3(\pi x)$ | Zhong et al. 2023, §3.3, Eqs. (27)–(41), Table 4 |
| third-order WENO from mapped TVD weights ([mapped WENO](/methods/mapped-weno.md)), indicators floored by $U^2/n_{\mathrm{sm}}^2$ | weights $\approx\tfrac12$ at critical points by an asymptotic argument; third order on an Alfvén wave, no critical-point test | Komissarov & Phillips 2024, App. A, Eqs. (A7)–(A10) (derived) |

Li et al. (2022b, §4.1) also recall that the WENO-Z of Don & Borges with $\epsilon=\Delta x^m$ satisfies a
sufficient condition for optimal order, and reject it for its dimensional inconsistency. Hong, Ye & Ye (2022, §1) recall
the same Don & Borges $\epsilon(\Delta x)$ remedy and Henrick et al.'s analysis of WENO-JS at critical
points, as background for TENO. Jeong et al.'s Proposition 4.5 also uses $\epsilon=\Delta x^\ell$: its proof
assumes $\beta_k=A_k\Delta x^{r_\beta}+\dots$ with $r_\beta\ge2$ and $\tau=O(\Delta x^8)$ (page-local
exponent $r_\beta$), and the experiments do not state the value of $\epsilon$ actually used.

## TENO at higher-order critical points: an adaptive cut-off

Tang (2024, §4.1) uses the definition above with $n_{\mathrm{cp}}\ge0$ the order (page-local symbol; $n_{\mathrm{cp}}=0$
means $f'\ne0$) and the test function

$$f(x)=e^x-\sum_{k=1}^{n_{\mathrm{cp}}}\frac{x^k}{k!},$$

which has an $n_{\mathrm{cp}}$th-order critical point at $x=0$ (Eqs. (21)–(22)). The error is the $L^1$ error of the
finite-difference approximation of $f(x_{1/2})-f(x_{-1/2})$, on six grids $\Delta x=0.001/2^\ell$, $\ell=0,\dots,5$
(page-local level $\ell$; the source writes $q$), with $\epsilon=\Delta x^{2n_{\mathrm{cp}}+3}$, chosen of higher order
than $\beta_k$ after Vevek et al. and Don & Borges (as recalled). The fifth-order TENO-Z (with the WENO-Z
$\tau_5=|\beta_0-\beta_2|$ in $\gamma_k$ and $C_T=10^{-5}$), TENO-A and TENO-LAD give, for the six grids:

| $n_{\mathrm{cp}}$ | TENO-Z, TENO-A, TENO-LAD | TENO-AZ |
|---|---|---|
| 1 | identical errors $5.1972\times10^{-14}$ to $2.5868\times10^{-22}$, orders 6.00, 5.58, 5.41, 5.32, 5.26 | the same |
| 2 | orders 3.00, 2.58, 2.41, 2.32, 2.26 (TENO-Z $2.0823\times10^{-6}$ to $3.3908\times10^{-10}$) | the errors of row 1 |
| 3 | orders 4.01, 3.59, 3.41, 3.32, 3.26 | the errors of row 1 |

(Tables 1–3). Tang reads row 2 as the reduction "to the 2nd-order accuracy at the 2nd-order critical point" of
all three earlier schemes, adaptive cut-offs included. *(Compiler check, not in the sources: the printed errors $e_\ell$
satisfy $e_\ell(\ell+1)2^{p\ell}=\text{const}$ to within 0.3%, so every printed order between levels $\ell-1$ and
$\ell$ equals $p+\log_2\frac{\ell+1}{\ell}$ to within 0.01, with $p=5$ in row 1 and for TENO-AZ, $p=2$ and $p=3$ for
the earlier schemes in rows 2 and 3; the asymptotic rates are therefore 5, 2 and 3, and the rate 2 at a
second-order critical point is that of WENO5-JS in the table above. The test functions differ by polynomials of degree at most 3, which the linear fifth-order scheme
treats exactly, so the identical TENO-AZ errors show that TENO-AZ is the linear scheme on every grid.)*

TENO-AZ (§3, Eqs. (19)–(20)) replaces $\tau_5$ in $\gamma_k=\big(1+\tau_5/(\beta_k+\epsilon)\big)^6$ by the page-local
$\tau_{\mathrm{AZ}}=|\beta_0+\beta_2-2\beta_1|$ and sets $C_T=\min(10^{-5},\tau_{\mathrm{AZ}})$, so that $C_T\to0$, all
stencils are kept and the linear scheme is recovered wherever $\tau_{\mathrm{AZ}}\to0$; at discontinuities the cut-off
is capped at $10^{-5}$. The paper's claim of "optimal accuracy at any order critical point" (Abstract, §5) rests on
Tables 1–3 ($n_{\mathrm{cp}}\le3$); no order of $\tau_{\mathrm{AZ}}$ is derived, and other exponents $q$ are said to give
the same result, not shown (§4.1). *(Compiler check, not in the sources: with the expansions of Wan & Xia recorded on
[smoothness indicators](/definitions/smoothness-indicator.md), the $\Delta x^5$ terms of $\beta_0$ and $\beta_2$ cancel in
the sum and $\tau_{\mathrm{AZ}}=2|f'f'''|\Delta x^4+O(\Delta x^6)$ away from critical points. Since $\gamma_k\ge1$, every
$\chi_k$ is bounded below whenever the ratios $\tau_{\mathrm{AZ}}/(\beta_k+\epsilon)$ stay bounded, and then no $\chi_k$
falls below $C_T=\tau_{\mathrm{AZ}}\to0$; this supports the mechanism at critical points of any order where those ratios
stay bounded, which the choice of $\epsilon$ above helps to ensure.)* Tang also states that keeping $\tau_5$ in
$\gamma_k$ but adopting the new $C_T$ gives the same optimal order, and that $\tau_5$ itself in the cut-off produces
oscillations; neither is shown (§3).

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

**Third order kept at smooth extrema by a learned weighting.** [Fan et al. (2025b)](/sources/fan-2025-b.md)
(§3.1.1, §4.1, Figs. 4, 6–8) make the three-point case the design target of their learned
[WCNS3-MR-NN](/methods/learned-weno-weights.md), a point-value staggered
[WCNS](/methods/weighted-compact-nonlinear-scheme.md). On three points a smooth extremum and a jump give
essentially the same normalized data, so features invariant under scaling cannot separate them; the largest
one-sided difference, however, shrinks under refinement at an extremum and stays constant at a jump, and they add
its logarithm as a scale-variant input ([scale invariance](/properties/scale-invariance.md)). In the
multi-resolution form, where the optimal weights are $(0,1)$, third order needs only that the weight of the
one-point candidate be $O(\Delta x^2)$ (Eqs. (29)–(30)). On linear advection of $10^{-3}\sin(2\pi x)$, whose
extrema are first-order critical points, the scheme converges at order 3.00 in $L^1$, $L^2$ and $L^\infty$ from
$N=80$ to $5120$ (Table 3), and to $N=10240$ on the Euler density wave (Table 4); two WCNS re-implementations of the
WENO3-NN network reach about second order in $L^1$, $L^2$ and first order in $L^\infty$ (Figs. 6–7). Plots of the
weights on profiles with an extremum and a jump (functions not given) show WCNS3-MR-NN closest to $\omega_2=1$ at the
extremum on a coarse grid ($N=20$) and separating extrema from discontinuities on a fine one ($N=500$) as WCNS3-MR
does, while the multi-resolution re-implementation of the WENO3-NN network still drops to first order at extrema
(§4.1.3, Fig. 8). Higher-order critical points are not tested.

## Third-order interpolation with a floored indicator

[Komissarov & Phillips (2024)](/sources/komissarov-2024.md) (App. A1; arXiv v3) state the
three-point version of the defect: weights built from ratios of the two-point indicators
$(u_i-u_{i\pm1})^2$, which are the third-order Jiang–Shu ones, "do not differentiate between
shocks and critical points", because a critical point midway between $x_i$ and $x_{i+1}$ makes
one difference much smaller than the other, as a jump does. Their remedy floors both indicators,
$\beta_\pm=(u_i-u_{i\pm1})^2+U^2(\Delta x/L)^2+\epsilon$ with $U=\max(\lvert u_{i-1}\rvert,\lvert u_i\rvert,\lvert u_{i+1}\rvert)$,
$L=n_{\mathrm{sm}}\Delta x$, $5\lesssim n_{\mathrm{sm}}\lesssim10$ ($n_{\mathrm{sm}}=10$ and
$\epsilon=10^{-25}$ in the tests; page-local symbols), so that near a critical point, where the
squared differences are of order $U^2(\Delta x/L)^4$ in their estimate, both indicators are dominated by the
floor and the TVD weights are close to $\tfrac12$, which the mapping sends to the linear weights
([mapped WENO](/methods/mapped-weno.md)); at strong shocks the floor is negligible. The argument
is asymptotic, and no test isolates a critical point. *(Compiler check, not in the sources: since
$L=n_{\mathrm{sm}}\Delta x$, the floor is the mesh-independent fraction $U^2/n_{\mathrm{sm}}^2$ of the
squared amplitude, so under refinement the differences of any smooth profile, $O(\Delta x^2)$ in
square, fall below it everywhere and the interpolation tends to the linear one; a jump smaller than
about $U/n_{\mathrm{sm}}$ is likewise treated as smooth.)*

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

## Sixth-order schemes at critical points up to order six

Zhang, Jiang, Qin, Qu & Yan (2024b, §5.4, Eq. (38)) use $f(x)=x^{n_{\mathrm{cp}}+1}e^{100x}$, which has an
$n_{\mathrm{cp}}$th-order critical point at $x=0$, and report the convergence rate of the reconstructed derivative at
$x=0$ "disregarding the effect of $\epsilon$" (Table 3; the values of $\epsilon$ and the grids are not given):

| scheme | $n_{\mathrm{cp}}=0$ | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| [WENO7-Z](/methods/weno-z.md) | 7 | 7 | 6 | 3 | 4 | 5 | 6 |
| EWENO-CU6 ([WENO-CU6](/methods/weno-cu6.md)) | 6 | 5 | 2 | 3 | 4 | 5 | 6 |
| TENO6 ([targeted ENO](/methods/targeted-eno.md)) | 6 | 6 | 2 | 4 | 4 | 6 | 6 |
| TENO6-opt | 5 | 5 | 2 | 4 | 4 | 6 | 6 |
| TENO6-A ([adaptive TENO](/methods/adaptive-teno.md)) | 4 | 4 | 4 | 3 | 4 | 6 | 6 |
| TENO6-SA ([scale sensors](/definitions/scale-sensor.md)) | 6 | 6 | 2 | 4 | 4 | 6 | 6 |

All schemes lose order at some critical point; EWENO-CU6 is the only one that loses an order at a first-order
point, TENO6-A the only one that keeps its (spectrally reduced) order up to a second-order point, and the
scale-adaptive TENO6-SA follows TENO6 exactly, "possibly" because the test is "relatively smooth", in the
authors' words. *(Compiler check, not in the sources: WENO7-Z at a third-order point, rate 3, agrees with the
3.24–3.55 of Li et al. (2022b) above, and TENO6 at a second-order point, rate 2, with the asymptotic rate 2 of
fifth-order TENO in Tang's Table 2 derived above.)* Zhang et al. recall a scheme of Zhang et al. that "maintains its order at all critical points by modifying
the $\epsilon$ parameter in the weighting formula to a grid-dependent form" (§5.4).

## Weight of the evidence

Fu (2023, §2.3) recalls Acker et al.'s finding that raising the weights of the less-smooth stencils
matters more for resolution than keeping the order at critical points, and Li et al. (2022b, §2)
relay Baeza et al.'s caveat that shock performance depends on how far from zero the weights of
discontinuous stencils are, not on accuracy at critical points. The improvement at critical points is
therefore one design target among several ([WENO-Z+](/methods/weno-z-plus.md) trades it for
resolution).

## Qualifications

- **Which TENO loses order.** Fu (2023, §3.1) reports no degeneration of TENO at a second-order critical point
  with the sixth-order global indicator $\tau_K$; the TENO-Z, TENO-A and TENO-LAD that Tang (2024, Eqs. (12)–(13),
  Table 2) measures at second order carry the fifth-order $\tau_5=|\beta_0-\beta_2|$. The two statements concern
  different global indicators, so they do not contradict each other. Zhang et al. (2024b, Table 3) measure
  rate 2 at a second-order critical point for TENO6, whose $\tau_6$ has the form of Fu's $\tau_K$; that pair is
  examined on the [TENO](/methods/targeted-eno.md) page.
- Tang (2024, §1) recalls an earlier paper of the author as finding TENO-Z degraded "to the 3rd-order" at
  higher-order critical points; the paper's own Table 2 gives second order at $n_{\mathrm{cp}}=2$ and its Table 3
  third order at $n_{\mathrm{cp}}=3$.
- *(Compiler check, not in the sources.)* TENO-AZ compares the dimensionless $\chi_k$ with $\tau_{\mathrm{AZ}}$, which
  scales as $\sigma^2$ under $f\mapsto\sigma f$ (page-local $\sigma$); wherever $\tau_{\mathrm{AZ}}<10^{-5}$ the cut-off
  decisions therefore depend on the amplitude and units of the data
  ([scale invariance](/properties/scale-invariance.md)). The paper does not discuss scaling.
- The third order of Fan et al. (2025b) on smooth advection and the low orders of Huang et al. (2026, Table 3) on
  $\sin(\pi x)$ concern different three-point schemes (a point-value WCNS with a multi-resolution weighting against
  finite-volume WENO3-NN and ROUND); the two results are not recorded as a contradiction. Fan et al.'s WCNS
  re-implementations of the WENO3-NN network are not the finite-volume WENO3-NN of Bezgin et al. either.
- Nogueira et al. (2024, §3.4) write that WENO5-NN "also alleviates" the critical-point order loss of WENO5-JS;
  the evidence is a plot of the weights on $\sin^3(\pi x)$ at $\Delta x=0.01$, without a convergence test.
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
- [Tang (2024)](/sources/tang-2024.md) — §1; §2, Eqs. (9)–(18); §3, Eqs. (19)–(20); §4.1, Eqs. (21)–(22), Tables 1–3; §5.
- [Nogueira et al. (2024)](/sources/nogueira-2024.md) — §3.4, Fig. 6.
- [Zhang et al. (2024b)](/sources/zhang-2024-b.md) — §5.4, Eq. (38), Table 3.
- [Komissarov & Phillips (2024)](/sources/komissarov-2024.md) — App. A1–A2, Eqs. (A3)–(A23); §4.1, Table 1 (arXiv v3).
- [Fan et al. (2025b)](/sources/fan-2025-b.md) — §3, Eqs. (26), (29)–(30), Fig. 4; §4.1, Tables 3–4, Figs. 6–8: third order at smooth extrema with a scale-variant learned weighting.
