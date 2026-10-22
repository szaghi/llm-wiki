---
type: Definition
title: "Approximate dispersion relation"
description: "The modified-wavenumber characterization of a possibly nonlinear spatial scheme: its sign convention for dissipation, the Hu-type dispersion-to-dissipation ratio and its critique, optimization on the nonlinear ADR, and what the sources read off it for WENO, TENO, THINC, ROUND, MDCD, WCNS, gradient-based, hybrid and multi-resolution schemes and central schemes with artificial dissipation."
status: established
aliases: [ADR, spectral analysis, modified wavenumber analysis, dispersion and dissipation analysis]
tags: [low-dissipation, reconstruction, weno, teno, finite-difference]
timestamp: 2026-10-23T16:00:00Z
---

# Approximate dispersion relation

The **approximate dispersion relation** (ADR) of a spatial discretization of
$\partial_tu+\partial_xu=0$ is the map from the reduced wavenumber
$\vartheta=k_w\Delta x\in[0,\pi]$ to the modified wavenumber
$\tilde\vartheta(\vartheta)=\tilde\vartheta_r+\mathrm i\,\tilde\vartheta_i$ that
the scheme effectively applies to a Fourier mode: $\tilde\vartheta_r$ measures
dispersion (phase error, ideal $\tilde\vartheta_r=\vartheta$) and
$\tilde\vartheta_i$ dissipation (ideal $0$). For a linear scheme the map is
exact and analytic; for a nonlinear scheme (WENO, TENO, ROUND, THINC) it is
*approximate*, evaluated numerically by the procedure of Pirozzoli (2006), which
the sources use but do not restate ([Luo & Wu (2021)](/sources/luo-2021-b.md),
§3; [Li et al. (2022)](/sources/li-2022-b.md), §3.3(3);
[Deng (2023)](/sources/deng-2023.md), Figs. 18, 28;
[Huang et al. (2026)](/sources/huang-2026.md), §5.2;
[Wang et al. (2021)](/sources/wang-2021.md), §4;
[Bezgin et al. (2022)](/sources/bezgin-2022.md), §4.8;
[Hiejima (2022)](/sources/hiejima-2022.md), Appendix).

## Linear schemes and the sign convention

For a linear first-derivative approximation written as
$(\partial_xu)_j\approx\frac1{\Delta x}\sum_lc_lu_{j+l}$ (page-local $c_l$, the
operator coefficients), [Fu (2023)](/sources/fu-2023.md) (§2.5, Eqs. (15)–(16))
gives

$$\tilde\vartheta_r=\sum_lc_l\sin(l\vartheta),\qquad
\tilde\vartheta_i=-\sum_lc_l\cos(l\vartheta),$$

and calls $\tilde\vartheta_i\le0$ dissipative. *(compiler check, not in the
sources: inserting $u_j=\hat u\,e^{\mathrm ij\vartheta}$ gives
$\frac{d\hat u}{dt}=\frac{1}{\Delta x}(-\mathrm i\tilde\vartheta_r+\tilde\vartheta_i)\hat u$,
so the mode decays exactly when $\tilde\vartheta_i<0$ and grows, i.e. is
anti-dissipated, when $\tilde\vartheta_i>0$.)* The same convention is used by
[Luo & Wu (2021)](/sources/luo-2021-b.md) (§3: positive imaginary part
= negative dissipation, "anti-diffusion") and by
[Takagi et al. (2022)](/sources/takagi-2022.md) (§2.3, for THINC). All
chunk-1 sources agree on this sign, none uses the opposite one, and
[Li, Chen & Ren (2022)](/sources/li-2022.md) (§2.1, Eqs. (8)–(15)) use it too.

**A scheme with decoupled dispersion and dissipation.** The fourth-order
six-point MDCD flux of Sun et al. (2011), as used by
[Li, Chen & Ren (2022)](/sources/li-2022.md) (§2.1, Eqs. (6)–(15); see
[MDCD schemes](/methods/mdcd-scheme.md)), has two free parameters, page-local
$c_{\mathrm{disp}}$ and $c_{\mathrm{diss}}$ as on the MDCD page (the source's
$\gamma_{disp}$, $\gamma_{diss}$), and its modified wavenumber splits exactly:

$$\begin{aligned}
\tilde\vartheta_r&=c_{\mathrm{disp}}\sin3\vartheta-\big(4c_{\mathrm{disp}}+\tfrac16\big)\sin2\vartheta+\big(5c_{\mathrm{disp}}+\tfrac43\big)\sin\vartheta,\\
\tilde\vartheta_i&=c_{\mathrm{diss}}\big(\cos3\vartheta-6\cos2\vartheta+15\cos\vartheta-10\big)=4\,c_{\mathrm{diss}}(\cos\vartheta-1)^3 .
\end{aligned}$$

Since $(\cos\vartheta-1)^3\le0$, $c_{\mathrm{diss}}\ge0$ is dissipative in the
convention above, and $c_{\mathrm{diss}}=0$ is a non-dissipative central scheme
(Eqs. (14)–(15)). The dispersion parameter is fixed at $0.0463783$ by minimizing
$\int_0^\pi e^{-8\vartheta}(\tilde\vartheta_r-\vartheta)^2d\vartheta$ (after Martín et al.,
Eqs. (12)–(13)); with the criterion $\lvert\tilde\vartheta_r-\vartheta\rvert<0.005$ of Hu,
Hussaini and Manthey the well-resolved range then extends to $\vartheta=1.297$, against
$0.976$ for both the sixth-order central (C6) and fifth-order upwind (UW5) schemes, which
have "exactly the same dispersion" (Figs. 1–2). *(Compiler check, not in the sources: the
trigonometric identity for $\tilde\vartheta_i$ follows from $\cos3\vartheta=4\cos^3\vartheta-3\cos\vartheta$
and $\cos2\vartheta=2\cos^2\vartheta-1$.)*

The same two-parameter symbol appears in a different scheme family.
[Zhou et al. (2023)](/sources/zhou-2023.md) (§3, Eqs. (19)–(24)) free the first
and last coefficients of the six-point central midpoint interpolation of a
[weighted compact nonlinear scheme](/methods/weighted-compact-nonlinear-scheme.md)
(page-local $\eta_{\mathrm Z}$ for their sum, $\xi_{\mathrm Z}$ for their difference, as on the WCNS and MDCD pages; the source's $\eta$, $\xi$). The
interpolation is differenced by a sixth-order explicit midpoint-and-node-to-node
formula, and they derive the modified wavenumber of the resulting linear
scheme. Dispersion depends only on $\eta_{\mathrm Z}$ and dissipation only on
$\xi_{\mathrm Z}$, so "the dispersion and dissipation properties of a linear
scheme can be optimized independently" (§3). The special cases are
$\eta_{\mathrm Z}=3/128$, $\xi_{\mathrm Z}=0$, the sixth-order central scheme, and
$\eta_{\mathrm Z}=\xi_{\mathrm Z}=3/128$, the fifth-order upwind scheme. They write the
derivative of a mode as $\mathrm i\Phi/\Delta x$ with $\Im\Phi<0$ dissipative.
*(Compiler check, not in the sources: their $\Re\Phi$ and $\Im\Phi$ are the MDCD
expressions above with $c_{\mathrm{disp}}=\tfrac{64}{45}\eta_{\mathrm Z}$ and
$c_{\mathrm{diss}}=\tfrac{64}{45}\xi_{\mathrm Z}$, term by term. Their
convention is the registry's, with $\tilde\vartheta_r=\Re\Phi$ and
$\tilde\vartheta_i=\Im\Phi$. The linear part of their WCNS is therefore
spectrally the MDCD scheme.)*

**Gradient-based reconstructions.** [Chamarthi (2023a)](/sources/chamarthi-2023.md)
(§3.2, Eqs. (46)–(52)) gives the modified wavenumbers of the author's fourth-order
[gradient-based reconstructions](/methods/gradient-based-reconstruction.md)
as series. They use explicit sixth-order gradients (EG6) or compact
fourth-order gradients (IG4H), and Chamarthi compares them with the fifth-order
upwind U5. Chamarthi writes the symbol $k'$ as an approximation of $\mathrm ik$.
*(Compiler check, not in the sources: in the registry's convention
$\tilde\vartheta_r=\Im k'$ and $\tilde\vartheta_i=-\Re k'$.)* Translated, the
printed series are:

$$\begin{aligned}
\text{U5:}\quad&\tilde\vartheta_r=\vartheta-\tfrac{\vartheta^7}{140}+\dots,&\tilde\vartheta_i&=-\tfrac{\vartheta^6}{60}+\tfrac{\vartheta^8}{240}+\dots,\\
\text{EG6:}\quad&\tilde\vartheta_r=\vartheta+\tfrac{\vartheta^5}{720}+\tfrac{\vartheta^7}{30240}+\dots,&\tilde\vartheta_i&=-\tfrac{\vartheta^6}{1440}-\tfrac{7\vartheta^8}{1920}+\dots,\\
\text{IG4H:}\quad&\tilde\vartheta_r=\vartheta+\tfrac{\vartheta^5}{720}+\tfrac{\vartheta^7}{2016}+\dots,&\tilde\vartheta_i&=-\tfrac{\vartheta^8}{2304}+\dots
\end{aligned}$$

These are fourth order in dispersion and dissipative, which the author calls
"contrary to expectations that the κ-scheme can be only at most third
accurate" and attributes to the point-value setting (§3.2). IG4H has the
better dispersion and both gradient-based schemes "superior dissipation"
to U5 (Fig. 2). In the companion paper,
[Chamarthi (2023b)](/sources/chamarthi-2023-b.md) (§2.2, Eq. (22),
Appendix A) uses the same analysis as a design tool. Two free parameters of
the second-derivative estimate are fixed by Fourier analysis at $38/7$ and
$3/190$ for a seventh-order upwind scheme on the same nine-point flux
stencil. Chamarthi finds the seventh-order scheme less dissipative and the
fourth-order one slightly better in dispersion (§3.2, Fig. 15). *(Compiler
check, not in the sources: the symbols of the printed flux forms, Eq. (33)
for seventh and Eq. (64) for fourth order, are
$\tilde\vartheta_r=\vartheta-\vartheta^9/360$,
$\tilde\vartheta_i=-\vartheta^8/280+\vartheta^{10}/560$ and
$\tilde\vartheta_r=\vartheta+\vartheta^5/720+\vartheta^7/30240+O(\vartheta^9)$,
$\tilde\vartheta_i=-\vartheta^6/1440+O(\vartheta^8)$. The second is the EG6
series above, so the fourth-order scheme of the companion paper is EG6, as
its Remark 2.2 states.)*

**Central schemes with high-order dissipation.**
[Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) (§3, Fig. 1) give the
dispersion and dissipation errors, as functions of $\vartheta$, of the members
of order 1 to 9 of the Lerat–Corre family of finite-difference schemes: a
central approximation of order $2(P+2)$ of the flux derivative plus a
dissipation term of order $2P+3$ on the same $2(P+2)+1$-point stencil ($P$ the
page-local family index; the flux is written out on
[numerical dissipation](/definitions/numerical-dissipation.md)). They read two
facts off the curves:

- the dispersion error of every member is exactly that of the standard central
  scheme of order $2(P+2)$;
- the dissipation of the ninth-order member ($P=3$) acts only on reduced
  wavenumbers $\vartheta\gtrsim0.35\pi$, i.e. on waves resolved with fewer than
  about six points, and leaves larger scales almost unaffected; the authors
  present it on this ground as an implicit subgrid regularization for LES.

*(compiler check, not in the sources: the dissipation term of the flux is an
odd-order difference centred at the interface, so its contribution to the flux
derivative is an even-order symmetric difference; in the splitting of the next
section it belongs to the symmetric part $D_{\mathrm{diss}}$ and contributes only
to $\tilde\vartheta_i$, which is consistent with the first statement.)*

## Dispersion–dissipation splitting and optimization

Fu's group designs the linear background schemes of TENO in spectral space
([Fu (2021)](/sources/fu-2021.md), §4.1, Eqs. (20)–(24);
[Fu (2023)](/sources/fu-2023.md), §2.5, Eqs. (12)–(16)). The operator is split
into an antisymmetric (dispersive) and a symmetric (dissipative) part,

$$\begin{aligned}
D_{\mathrm{disp}}f(x)&=\frac1{\Delta x}\sum_{j=1}^na_j\big(f(x+j\Delta x)-f(x-j\Delta x)\big),\\
D_{\mathrm{diss}}f(x)&=\frac1{\Delta x}\Big(b_0f(x)+\sum_{j=1}^nb_j\big(f(x+j\Delta x)+f(x-j\Delta x)\big)\Big),
\end{aligned}$$

($a_j$, $b_j$ page-local). The $a_j$ follow from an order constraint plus the
minimization of the weighted error integral of Weirs and Candler (as recalled by
Fu 2023)

$$E=\int_0^\pi e^{\sigma(\pi-\vartheta)}\big(\tilde\vartheta_r-\vartheta\big)^2\,d\vartheta ,$$

with a page-local weight $\sigma>0$ that trades low against high wavenumbers
(Fu 2021 does not print the value used). The $b_j$ follow from an order
constraint plus the dispersion-to-dissipation condition attributed to Hu et al.,
which both Fu papers call "the approximate dispersion relation":

$$\zeta=\frac{\big\lvert d\tilde\vartheta_r/d\vartheta-1\big\rvert}{-\tilde\vartheta_i}\approx O(10)$$

($\zeta$ page-local; Fu 2021 prints the numerator without the absolute value,
Fu 2023 with it, and plots the regularized form
$(\lvert d\tilde\vartheta_r/d\vartheta-1\rvert+10^{-3})/(-\tilde\vartheta_i+10^{-3})$,
Fig. 3). The design idea is that dissipation should be just large enough to damp
the modes whose phase is already wrong. [Fu (2021)](/sources/fu-2021.md)
(§3.1) argues that upwind-biased large stencils "typically do not satisfy the
approximate dispersion-relation even with sophisticated optimization methods",
whereas symmetric stencils let dispersion and dissipation be optimized
separately once the order constraint is relaxed; this is why its TENO8-AA and
TENO10-AA linear schemes are of order 6 and 8 rather than 8 and 10 (see
[adaptive TENO](/methods/adaptive-teno.md)).

**The ratio used pointwise.** [Li, Chen & Ren (2022)](/sources/li-2022.md) write the same
condition as $\zeta\sim1<10$ and use it twice. Imposing $\zeta(\pi)\le9$ at the
wavenumber of largest dispersion error gives the fixed dissipation parameter
$c_{\mathrm{diss}}=0.012$ (§2.1, Eqs. (16)–(17)). *(Compiler check, not in the
sources: $\lvert d\tilde\vartheta_r/d\vartheta-1\rvert_{\vartheta=\pi}=16c_{\mathrm{disp}}+\tfrac83=3.4087$
and $\lvert\tilde\vartheta_i(\pi)\rvert=32c_{\mathrm{diss}}$, so $\zeta(\pi)=9$ needs
$c_{\mathrm{diss}}=0.01184$, and $0.012$ gives $\zeta(\pi)=8.88$.)* Inverting the
condition at each wavenumber at $\zeta=9$ gives a dissipation parameter as a function of
$\vartheta$; evaluated at the local wavenumber estimated by a
[scale sensor](/definitions/scale-sensor.md), and replaced below $\vartheta=1$ by the floor
$0.001$, it makes the dissipation adapt to the local scale: the MDAD scheme, whose range with
$\lvert\tilde\vartheta_i\rvert\le0.001$ reaches $\vartheta<1.02$, about 35% beyond the fixed
MDCD (§2.3, Eqs. (34)–(38), Fig. 7). These are sine-wave calibrations of a solution-dependent
scheme, not a linear symbol (the paper calls MDAD "linear" for convenience, §3). On smooth
curvilinear grids, applied to the transformed flux, the one-dimensional stencil keeps the
same modified wavenumber under the stated assumptions (smooth grids, periodicity, a
Fourier component of the transformed flux; §3.4 Remark, Eqs. (62)–(69)).

**Optimizing the nonlinear scheme, not its linear part.**
[Zhou et al. (2023)](/sources/zhou-2023.md) (§§3–4) minimize the same kind of
weighted dispersion error,
$E=\int_0^\pi e^{-\sigma\vartheta}(\tilde\vartheta_r-\vartheta)^2d\vartheta$, with
their weight exponent written as the page's $\sigma$. *(Compiler check, not in
the sources: up to the constant factor $e^{\sigma\pi}$ this is the Weirs–Candler
integral above.)* For the linear scheme, $\sigma=4,\dots,8$ gives
$\eta_{\mathrm Z}=0.0502$, $0.0432$, $0.0384$, $0.0350$, $0.0326$. The peak dispersion
errors are $3.72\%$ to $0.34\%$, and the resolved fraction of $[0,\pi]$ runs
from $60.86\%$ to $41.03\%$ (Table 1). *(Compiler check, not in the sources:
$\sigma=8$, $\eta_{\mathrm Z}=0.0326$ gives $c_{\mathrm{disp}}=\tfrac{64}{45}\cdot0.0326=0.04636$.
This is the $0.0463783$ that Li, Chen & Ren obtain with the weight
$e^{-8\vartheta}$, to the printed digits.)* Zhou et al. then evaluate $E$ on the
numerically computed ADR of the full nonlinear scheme, whose weights carry an
additive constant $C$ of Wong–Lele type. The optimal $\eta_{\mathrm Z}$ then depends on
$C$ and $\xi_{\mathrm Z}$: $0.0675$ and $0.0539$ at $C=10$ for
$\xi_{\mathrm Z}=0$ and $3/128$, down to $0.0385$ for both at $C=10^9$
(Table 2). The nonlinear scheme optimized at $C=10^9$ resolves up to
$\vartheta\approx1.6$, "nearly identical" to its linear scheme, against about
$1.25$ for the linearly optimized ONL6 and the localized-dissipation WCNS-LD on
the same stencil (§4.1, Figs. 4–5). The authors conclude that the optimization
"can completely remedy the dispersion property deterioration caused by
nonlinear mechanism". Their dissipation design is an "idealized" curve: zero
below the critical wavenumber, a quick rise there, and enough dissipation
beyond it. No fixed $C$ or $\xi_{\mathrm Z}$ produces such a curve, so both
are switched by a sensor (WCNS-SA; §4.2–4.3, Figs. 6–7). WCNS-SA's dissipation
increases nearly monotonically for $\vartheta>1.9$, while WCNS-LD's "decreases
evidently when $\vartheta>2.4$". On this ground the authors credit WCNS-SA with
stronger shock-capturing robustness (§4.3, Fig. 7(b);
[scale sensors](/definitions/scale-sensor.md)).

**A critique of the dispersion–dissipation condition.** Zhou et al. (§4.2–4.3,
Eq. (28), Fig. 7(b)) plot a scheme whose dissipation is the minimum the Hu-type
condition allows at ratio 10, i.e. $\zeta=10$ above. It "has insufficient
dissipation at the high-wavenumber region and thus exhibits weak
shock-capturing robustness". They conclude that the condition "needs to be
improved for actual simulation, although it is physically reasonable". The
evidence is the spectral curve; no simulation with that scheme is reported.
Fu's group uses the condition for the linear backgrounds of TENO, whose shock
capturing comes from the cut-off. Li, Chen & Ren impose it at
$\vartheta=\pi$, and their hybrid hands the highest wavenumbers to WENO.
*(Compiler check, not in the sources: neither use asks the condition alone to
supply the dissipation at shocks, so the critique and those uses concern
different roles of the same condition.)*

**Two meanings of the name.** In the Fu papers "approximate dispersion relation"
names the condition on $\zeta$; in Pirozzoli's usage, followed by Luo & Wu,
Li et al., Deng, Huang et al., Wang et al. (2021), Bezgin et al., Hiejima, Hong et al.,
Wan & Xia and Li, Chen & Ren, it names the numerically evaluated
$\tilde\vartheta(\vartheta)$ of a nonlinear scheme. The two are compatible (the
condition is imposed on the curve) but a page citing "the ADR" must say which
is meant.

## What the sources read off the ADR

- **TENO restores the linear scheme up to a cut-off wavenumber.** Five-point
  TENO keeps the exact dispersion and dissipation of its background linear scheme
  up to intermediate wavenumbers, and the cut-off $C_T$ fixes where it departs
  from it; WENO-JS and WENO-Z depart earlier
  ([Fu (2023)](/sources/fu-2023.md), §2.5, Fig. 2, $C_T\in\{10^{-5},10^{-6},10^{-7}\}$;
  Fig. 3 for TENO8 and the spectrally optimized TENO8-opt). The same property
  is stated without a new ADR computation by
  [Takagi et al. (2022)](/sources/takagi-2022.md) (§2.2). See
  [targeted ENO](/methods/targeted-eno.md).
- **Adaptive-dissipation TENO.** The five-point TENO5-A variant of
  [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md), with a cut-off driven by a scale
  sensor, has better dispersion and dissipation than TENO5, and its optimized third-order
  background "can be restored exactly up to an intermediate wavenumber" (§3.2, Fig. 3,
  against the upwind fifth-order and optimized third-order linear schemes; no cut-off
  wavenumbers printed). See [adaptive TENO](/methods/adaptive-teno.md).
- **TENO-M and its extension threshold.** For the six- and eight-point TENO-M of
  [Hong, Ye & Ye (2022)](/sources/hong-2022.md) (§4.3, Figs. 6–7), $C_s=0$ reproduces the
  spectral properties of TENO5 and $C_s=1$ those of the linear background in the low to
  intermediate range; larger $C_s$ lowers high-wavenumber dissipation, which hurts stable
  shock capturing, and $C_s=0.8$ is the adopted compromise. In the intermediate to high range
  TENO-M has better dispersion than TENO of the same width. See
  [targeted ENO](/methods/targeted-eno.md).
- **Hybrid schemes and their detectors.** The MDAD-HY hybrid of
  [Li, Chen & Ren (2022)](/sources/li-2022.md) (§3.3, Figs. 11–12) recovers the MDAD dissipation and
  the MDCD dispersion up to $\vartheta=2.06$, beyond which the WENO part activates; TENO-HY and
  MDCD-HY show irregular dissipation at low wavenumbers, which the authors trace to detector
  misjudgments, and WENO-Z is the most dissipative. The same sine-wave procedure grades the
  detectors themselves: the TENO-based one of Fu is correct only below $0.64$, the modified
  Ren detector up to $2.06$ (§3.2, Fig. 9). See [hybrid central–WENO schemes](/methods/hybrid-weno.md).
- **A three-region hybrid for steady states.** The WENO-H of
  [Wan & Xia (2022)](/sources/wan-2022.md) (§3, Fig. 3.2; linear weights $(0.8,0.1,0.1)$,
  $\epsilon=10^{-6}$) has lower dissipative and dispersive errors than the central WENO of
  Zhu and Shu (WENO-ZQ, linear weights $(0.98,0.01,0.01)$), the multi-resolution WENO
  (weights $(1,10,100)/111$) and WENO-JS, with UW5 as reference; the curves are given, no
  values. See [hybrid central–WENO schemes](/methods/hybrid-weno.md) and
  [CWENO](/methods/cweno.md).
- **Negative dissipation in WENO-Z+.** The ADR of WENO-Z+ with large
  coefficient $\lambda$ has $\tilde\vartheta_i>0$ in a narrow band around
  $\vartheta\approx1.1834$, and decreasing $\lambda$ removes it only slowly
  there; taking the square root of the extra term removes it, and the resulting
  WENO-Z+M has a better ADR than WENO-Z, WENO-Z+ and, over a broad band, than
  the linear fifth-order upwind scheme UD5 itself
  ([Luo & Wu (2021)](/sources/luo-2021-b.md), §§3–4, Figs. 1–4). See
  [WENO-Z+](/methods/weno-z-plus.md).
- **WENO-ZN.** Lower dissipation and dispersion error over a large range of
  medium wavenumbers than WENO-JS and WENO-Z at fifth and seventh order, with
  UW5 and UW7 as references ([Li et al. (2022)](/sources/li-2022-b.md),
  §3.3(3), Fig. 2). See [WENO-ZN](/methods/weno-zn.md).
- **THINC is anti-diffusive at $\beta_{\mathrm T}=1.6$.** Its modified wavenumber
  has a positive imaginary part in some ranges, like the TVD Superbee limiter,
  which is why it is confined to discontinuities
  ([Takagi et al. (2022)](/sources/takagi-2022.md), §2.3, citing Deng et al.
  2018). See [THINC](/methods/thinc-reconstruction.md).
- **Compact ROUND schemes.** The dissipative ROUND formulations improve
  dispersion over second-order shock-capturing schemes, and the low-dissipative
  ones are "close to the linear third-order scheme"
  ([Deng (2023)](/sources/deng-2023.md), Figs. 18, 28); the Part-2 ROUND and
  LD-ROUND have lower dispersion error at high wavenumbers than WENO5-JS and
  WENO3-NN, and ROUND markedly lower dissipation there
  ([Huang et al. (2026)](/sources/huang-2026.md), §5.2, Fig. 5). See
  [ROUND schemes](/methods/round-scheme.md).
- **Multi-resolution WENO.** With the Pirozzoli procedure, the fifth-order
  multi-resolution WENO of Zhu and Shu (WENOZS5), WENO-AO(5,3) and the modified
  multi-resolution scheme of [Wang et al. (2021)](/sources/wang-2021.md) all have
  better dispersion and dissipation than WENO-JS5, with the optimal linear
  fifth-order upwind scheme as reference (§4, Fig. 4.1). The paper gives the
  curves but no numerical cut-off wavenumbers. See
  [multi-resolution WENO](/methods/multi-resolution-weno.md) and
  [WENO-AO](/methods/weno-ao.md).

- **A learned three-point WENO.** [Bezgin et al. (2022)](/sources/bezgin-2022.md) (§4.8,
  Fig. 17) compare their two neural-network weightings with WENO3-JS, WENO5-JS and the linear
  schemes they label CU1, CU3, CU5, "central-upwind" in their naming, not the Kurganov-type
  [central-upwind fluxes](/methods/central-upwind-scheme.md) (no parameters of the procedure
  printed). WENO3-NN2 is
  "considerably less dissipative" than WENO3-JS over the whole wavenumber range, slightly less
  dissipative than WENO5-JS at high wavenumbers, with a monotone dissipation curve. WENO3-NN1 keeps
  the dissipation minimal and has **zero dissipation at the cut-off wavenumber**, which the
  authors call "counterintuitive to classical discretization-design principles" and read as
  under-resolved wave packets kept "without interacting with resolved scales", "akin to soliton
  solutions". Huang et al. (above) find their ROUND schemes markedly less dissipative than
  WENO3-NN at high wavenumbers. See [learned WENO weights](/methods/learned-weno-weights.md).
- **MP-limited gradient-based reconstruction against TENO5.** With the ADR procedure of
  Zhao et al., [Chamarthi (2023a)](/sources/chamarthi-2023.md) (§3.3, Fig. 3) finds
  that MIG4, the author's compact-gradient scheme with the monotonicity-preserving limiter, has better
  dispersion and dissipation than MEG6 and [TENO5](/methods/targeted-eno.md). Reusing the
  high-order second derivative as the limiter curvature improves the dispersion of MIG4
  over its base version, "marginal[ly]" for MEG6
  ([monotonicity-preserving limiter](/methods/monotonicity-preserving-limiter.md)). Chamarthi's
  summary Table 5 rates the dissipation error "Medium" for MIG4 and MEG6 and "Low" for
  TENO5, and the dispersion error Low, Medium and High (see Qualifications).
- **High-order WCNS whose curves do not separate.** [Hiejima (2022)](/sources/hiejima-2022.md)
  (Appendix, Fig. A.1; $n_x=100$, first-order upwind as reference) computes the ADR of the author's
  [weighted compact nonlinear schemes](/methods/weighted-compact-nonlinear-scheme.md) with
  Jiang–Shu (WCNS-JS) and TENO-type (WCNS-T) weights at interpolation orders 5, 7, 9 and 11:
  WCNS-T is better than WCNS-JS, "however, both cases are not so different in accuracy", and the
  curves of the four orders nearly coincide, which the author reads as an open issue in the
  formulation of the nonlinear weight. The scheme differences the AUSMDV fluxes of the
  interpolated interface states by the two-point formula
  $(\hat f_{i+1/2}-\hat f_{i-1/2})/\Delta x$ and "does not include a compact procedure for
  calculating the flux derivative" (§2.2, Eq. (5)). *(compiler check, not in the sources: for
  exact interface values, $\big(f(x_i+\tfrac{\Delta x}2)-f(x_i-\tfrac{\Delta x}2)\big)/\Delta x=f'(x_i)+\tfrac{\Delta x^2}{24}f'''(x_i)+O(\Delta x^4)$,
  whose modified wavenumber is $2\sin(\vartheta/2)$, so whatever the interpolation order the
  spatial operator carries a second-order dispersion error at low wavenumbers; this is the
  error the derivative corrections of [A-WENO](/methods/alternative-weno.md) remove, and it is
  consistent with curves that do not separate with the interpolation order. The paper offers
  no convergence test that would decide between the two readings.)*

## Qualifications

- The ADR of a nonlinear scheme depends on the test signal (a single Fourier
  mode at given amplitude); none of the chunk-1 sources reports how its curves
  change with amplitude or with the regularization $\epsilon$.
- ADR conclusions are linear-advection conclusions. They predict resolution of
  smooth broadband content but say nothing about robustness at shocks; Luo & Wu
  choose their $\lambda=579$ not from the ADR but as the largest value for which
  the Woodward–Colella blast wave still runs ($\lambda=580$ fails), and their
  Fig. 2 shows the ADR for $\lambda=600$, a value they report as unusable.
- [Chamarthi (2023a)](/sources/chamarthi-2023.md) is not self-consistent on TENO5. The text
  near Fig. 3 says that MIG4 has "superior dispersion and dissipation properties than the MEG6
  and TENO5 scheme", while Table 5 rates TENO5's dissipation error "Low" and MIG4's
  "Medium". Chamarthi also says Fig. 2 shows the "imaginary and real parts" of the modified wavenumber as
  dispersion and dissipation, but labels the panels "Real" and "Imag" in the other order. The page
  uses the printed series, not the panel labels.
- Zhou et al. (2023) do not print the weight exponent $\sigma$ used for their nonlinear optimization
  (Table 2). The large-$C$ limit $0.0384$ equals the linear optimum at $\sigma=6$ of their Table 1.
  They also never print the exponent of their nonlinear weights, although they attribute post-shock
  noise to its value (§5.6).
- [Luo & Wu (2021)](/sources/luo-2021-b.md) (§6) present "beating the
  underlying linear scheme" as contrary to the view, attributed to Pirozzoli,
  that nonlinear shock-capturing mechanisms always degrade spectral
  properties; the mechanism is negative nonlinear dissipation (see
  [numerical dissipation](/definitions/numerical-dissipation.md)).

# Citations

- [Fu (2021)](/sources/fu-2021.md) — §3.1, §4.1, Eqs. (20)–(24): splitting, error integral, $\zeta\approx O(10)$.
- [Fu (2023)](/sources/fu-2023.md) — §2.5, Eqs. (12)–(16), Figs. 2–3: sign convention, TENO spectra.
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §§3–4, Figs. 1–4: Pirozzoli ADR, negative dissipation of WENO-Z+.
- [Li et al. (2022)](/sources/li-2022-b.md) — §3.3(3), Fig. 2: WENO-ZN spectra.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §2.2, §2.3: TENO and THINC spectral statements.
- [Deng (2023)](/sources/deng-2023.md) — Figs. 18, 28: ROUND spectra.
- [Huang et al. (2026)](/sources/huang-2026.md) — §5.2, Fig. 5: ROUND, LD-ROUND, WENO3-NN spectra.
- [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) — §3, Fig. 1: dispersion and dissipation of the Lerat–Corre family, $0.35\pi$ threshold (arXiv v1).
- [Wang et al. (2021)](/sources/wang-2021.md) — §4, Fig. 4.1: multi-resolution WENO spectra.
- [Bezgin et al. (2022)](/sources/bezgin-2022.md) — §4.8, Fig. 17: WENO3-NN spectra, zero dissipation at the cut-off.
- [Hiejima (2022)](/sources/hiejima-2022.md) — §2.2 (Eq. (5)), Appendix (Fig. A.1): WCNS-JS and WCNS-T spectra at orders 5–11.
- [Li, Chen & Ren (2022)](/sources/li-2022.md) — §2.1–2.3, Eqs. (6)–(38), Figs. 1–7; §3.2–3.4, Figs. 9, 11–12, Eqs. (62)–(69): MDCD symbol, pointwise dispersion–dissipation ratio, MDAD-HY and detector spectra.
- [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) — §3.2, Fig. 3: spectra of the scale-sensor TENO5-A (arXiv v1).
- [Hong, Ye & Ye (2022)](/sources/hong-2022.md) — §4.3, Figs. 6–7: TENO-M spectra against $C_s$.
- [Zhou et al. (2023)](/sources/zhou-2023.md) — §§3–4, Eqs. (19)–(28), Tables 1–2, Figs. 3–7: two-parameter WCNS symbol, ADR-based optimization, idealized dissipation, critique of the dispersion–dissipation condition.
- [Chamarthi (2023a)](/sources/chamarthi-2023.md) — §3.2, Eqs. (46)–(52), Fig. 2; §3.3, Fig. 3, Table 5: gradient-based reconstruction spectra, MIG4 and MEG6 against TENO5 (arXiv v2).
- [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) — §2.2, Eq. (22), Appendix A; §3.2, Fig. 15: Fourier design of the seventh-order gradient-based reconstruction (arXiv v1).
- [Wan & Xia (2022)](/sources/wan-2022.md) — §3, Fig. 3.2: WENO-H, WENO-ZQ, MRWENO, WENO-JS spectra.
