---
type: Definition
title: "Approximate dispersion relation"
description: "The modified-wavenumber characterization of a (possibly nonlinear) spatial scheme, its sign convention for dissipation and anti-dissipation, the Hu-type dispersion-to-dissipation design ratio, and what the sources read off it for WENO, TENO, THINC, ROUND and multi-resolution WENO schemes and for central schemes with high-order artificial dissipation."
status: established
aliases: [ADR, spectral analysis, modified wavenumber analysis, dispersion and dissipation analysis]
tags: [low-dissipation, reconstruction, weno, teno, finite-difference]
timestamp: 2026-10-22T20:00:00Z
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
chunk-1 sources agree on this sign; none uses the opposite one.

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

**Two meanings of the name.** In the Fu papers "approximate dispersion relation"
names the condition on $\zeta$; in Pirozzoli's usage, followed by Luo & Wu,
Li et al., Deng, Huang et al., Wang et al. (2021), Bezgin et al. and Hiejima, it names the numerically evaluated
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
- **High-order WCNS whose curves do not separate.** [Hiejima (2022)](/sources/hiejima-2022.md)
  (Appendix, Fig. A.1; $n_x=100$, first-order upwind as reference) computes the ADR of his
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
