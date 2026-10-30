---
type: Definition
title: "Approximate dispersion relation"
description: "The modified-wavenumber characterization of a possibly nonlinear spatial scheme: its sign convention for dissipation, the Hu-type dispersion-to-dissipation ratio, its fully discrete Runge–Kutta form, its Bloch-wave extension to AMR grids, optimization on the nonlinear ADR and its critique, and what the sources read off it for WENO, TENO, THINC, ROUND, MDCD, WCNS, gradient-based, hybrid and central schemes."
status: established
aliases: [ADR, spectral analysis, modified wavenumber analysis, dispersion and dissipation analysis]
tags: [low-dissipation, reconstruction, weno, teno, finite-difference]
timestamp: 2026-10-30T07:53:00Z
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
§3; [Li et al. (2022b)](/sources/li-2022-b.md), §3.3(3);
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
[Li, Chen & Ren (2022a)](/sources/li-2022.md) (§2.1, Eqs. (8)–(15)) use it too.

**A scheme with decoupled dispersion and dissipation.** The fourth-order
six-point MDCD flux of Sun et al. (2011), as used by
[Li, Chen & Ren (2022a)](/sources/li-2022.md) (§2.1, Eqs. (6)–(15); see
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
stencil. Chamarthi (2023b) finds the seventh-order scheme less dissipative and the
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
[Fu, Hu & Adams (2016)](/sources/fu-2016.md) (§4.1, Eq. (30)) and Fu 2023 with it; Fu et al. (2016)
take it "for the non-resolved wave-number range", state that its application to nonlinear
schemes "is fairly straightforward" although it comes from a linear analysis, and plot the same
regularized form "approximately" in their Fig. 5; Fu 2023 plots the regularized form
$(\lvert d\tilde\vartheta_r/d\vartheta-1\rvert+10^{-3})/(-\tilde\vartheta_i+10^{-3})$,
Fig. 3). The design idea is that dissipation should be just large enough to damp
the modes whose phase is already wrong. [Fu (2021)](/sources/fu-2021.md)
(§3.1) argues that upwind-biased large stencils "typically do not satisfy the
approximate dispersion-relation even with sophisticated optimization methods",
whereas symmetric stencils let dispersion and dissipation be optimized
separately once the order constraint is relaxed; this is why its TENO8-AA and
TENO10-AA linear schemes are of order 6 and 8 rather than 8 and 10 (see
[adaptive TENO](/methods/adaptive-teno.md)).

**The founding blend of two sub-schemes.** Before this split, the founding TENO paper
optimized the background differently ([Fu et al. (2016)](/sources/fu-2016.md), §4, Eqs. (31)–(33),
Tables 3–4): an order-$K$ scheme is replaced by
$\hat f^{\mathrm{opt}}_{i+1/2}=\eta_{\mathrm b}g^{(1)}_{i+1/2}+(1-\eta_{\mathrm b})g^{(2)}_{i+1/2}$, a blend of two
order-$(K-1)$ sub-schemes ($\eta_{\mathrm b}$ page-local; the source's $\eta$, here renamed to keep
the entropy $\eta$), with $\zeta$ as the objective "instead of minimizing the dispersion errors". For
even $K$ the sub-schemes are upwind- and downwind-biased with the same dispersion error, so only the
dissipation is tuned; for odd $K$ the dispersion error changes as well, which is "tolerated". On five
points, $g^{(1)}=\tfrac1{12}(f_{i-2}-5f_{i-1}+13f_i+3f_{i+1})$ (upwind) and
$g^{(2)}=\tfrac1{12}(-f_{i-1}+7f_i+7f_{i+1}-f_{i+2})$ (central, non-dissipative); $\eta_{\mathrm b}=0.4$
gives the upwind fifth-order scheme, and lowering $\eta_{\mathrm b}$ from 0.35 to 0.2 raises the extremum
of $\zeta$ "from approximately 5.5 to 16.5, maintaining order $O(10)$" (§4.2); TENO5-opt takes
$\eta_{\mathrm b}=0.2$, $d=(0.55,0.4,0.05)$ in TENO labels, and its nonlinear version adds dissipation only
at high wavenumbers and is "less dissipative than a classical fifth-order linear scheme especially
for intermediate wave numbers". On six points,
$g^{(1)}=\tfrac1{60}(2f_{i-2}-13f_{i-1}+47f_i+27f_{i+1}-3f_{i+2})$ and
$g^{(2)}=\tfrac1{60}(-3f_{i-1}+27f_i+47f_{i+1}-13f_{i+2}+2f_{i+3})$ share the dispersion of the sixth-order
central scheme ($\eta_{\mathrm b}=0.5$); TENO6-opt takes $\eta_{\mathrm b}=0.54$, $d=(0.462,0.3,0.054,0.184)$,
"obtained by enforcing the constraint $\zeta=10$ at" $\vartheta=1.302$, and its nonlinear version has
$\zeta\le35$ everywhere and below 10 at high wavenumbers (§4.3). The blend costs one order: TENO5-opt
is fourth and TENO6-opt fifth order (§5.1). Fu et al. (§4.1) also state that, because the fifth-order
upwind background is so dissipative, $\zeta\le5.5$ for all nonlinear five-point schemes, "free from
spurious waves", whereas $\zeta\approx O(100)$ between the wavenumbers 1.1 and 1.8 for the six-point
schemes over the non-dissipative central background, and that the WENO-SYMBO and WENO-BO schemes
produce anti-dissipation at low to intermediate wavenumbers and "apparently fail to satisfy" the
relation (citing their [22], [29]).

**Printed values for an eight-point background.** [Liang & Fu (2024b)](/sources/liang-2024-b.md)
(§3.3.1, Eqs. (36)–(46)) give the procedure with numbers. The
dispersive coefficients $a_1,\dots,a_4$ satisfy the Taylor constraints of
the first derivative up to $\Delta x^4f^{(5)}$ (sixth order) and minimize
$E$ with weight $\sigma=7$; they explain the emphasis on low wavenumbers
by the TENO nonlinear adaptation, which "will dominate the spectral
resolution properties" at higher ones. The dissipative coefficients
satisfy four constraints that cancel the $f$, $\Delta xf''$,
$\Delta x^3f^{(4)}$ and $\Delta x^5f^{(6)}$ terms, and the fifth sets
$b_0=0.01$ so that $\zeta\approx O(10)$. They state that splitting the
operator this way also removes the anti-dissipation at intermediate
wavenumbers. The same $a_\ell$ serve their kinetic-energy-preserving
split-form flux, which is the dispersive part alone and so
non-dissipative. *(Compiler check, not in the sources: the resulting
dissipative part is $\tfrac{b_0}{70\Delta x}$ times the eighth undivided
difference; see [targeted ENO](/methods/targeted-eno.md).)*

**Order lost by decoupling, and a piecewise alternative.** [Zhang et al. (2024b)](/sources/zhang-2024-b.md)
(§3.1, Eqs. (18)–(21)) expand the same split on six points: the dispersive part
multiplies $f'$, $\Delta x^2f'''$, $\Delta x^4f^{(5)}$ by
$G_1=2a_1+4a_2+6a_3$, $G_2=\tfrac13a_1+\tfrac83a_2+9a_3$,
$G_3=\tfrac1{60}a_1+\tfrac8{15}a_2+\tfrac{81}{20}a_3$, and the dissipative part has
coefficients of $f$, $\Delta xf''$, $\Delta x^3f^{(4)}$, $\Delta x^5f^{(6)}$ (page-local
$G_\ell$ and $a_j$, $b_j$ as above). Sixth order needs $G_1=1$, $G_2=G_3=0$ and all four
dissipative coefficients zero; dropping $G_3=0$ and the last dissipative constraint frees one
parameter in each part at the cost of two orders, which reproduces the fourth-order MDCD
scheme ([MDCD schemes](/methods/mdcd-scheme.md)). From this they conclude that spectrum
optimization of a finite-difference scheme, by linear weights or by separate dispersion and
dissipation parameters, "inevitably" sacrifices order. Their remedy, piecewise spectrum
optimization (§3.2), keeps the optimal order where it is accurate and lowers it only beyond:
with a 1% tolerance on $\lvert\tilde\vartheta_r/\vartheta-1\rvert$ (Lele's resolved
bandwidth),

$$\begin{aligned}
\text{6th order:}\quad&\tilde\vartheta_r=\tfrac1{30}\big(45\sin\vartheta-9\sin2\vartheta+\sin3\vartheta\big),&&\text{bandwidth }1.100,\\
\text{optimized 4th:}\quad&\tilde\vartheta_r=\tfrac1{150}\big(240\sin\vartheta-57\sin2\vartheta+8\sin3\vartheta\big),&&\text{bandwidth }1.530,\\
\text{optimized 2nd:}\quad&\tilde\vartheta_r=\tfrac1{500}\big(832\sin\vartheta-229\sin2\vartheta+42\sin3\vartheta\big),&&\text{bandwidth }1.726,
\end{aligned}$$

switched at $\vartheta=1.085$ and $1.516$, where the dispersion errors on both sides are
equal; the last bandwidth is about 56.9 % above the first. *(Compiler check, not in the
sources: the three bandwidths come out as 1.1001, 1.5303 and 1.7264, the switching points as
1.0850 and 1.5158, and each scheme has $G_1=1$.)* The schemes become the band-wise linear
backgrounds of TENO6-SA ([adaptive TENO](/methods/adaptive-teno.md)).

**The ratio used pointwise.** [Li, Chen & Ren (2022a)](/sources/li-2022.md) write the same
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

## Fully discrete analysis

The relations above concern the semi-discrete operator. [Li et al. (2023b)](/sources/li-2023-b.md)
(§3.1, Eqs. (16)–(22)) carry them to the fully discrete scheme with the three-stage third-order
Runge–Kutta method, at CFL number $\nu=a\Delta t/\Delta x$. Let $\mathcal G(\vartheta,\nu)$ denote
the amplification factor of one step (page-local; the source's $F$). With
$K=-\mathrm i\nu\tilde\vartheta$ (page-local, not the TENO stencil size), it is

$$\mathcal G=1+K+\tfrac12K^2+\tfrac16K^3 .$$

The exact factor of one step is $e^{-\mathrm i\vartheta\nu}$. The ratio of the two defines a
total dissipation error $\lvert\mathcal G\rvert$ (ideal $1$) and a total dispersion error
$\delta_\nu=\arg\mathcal G+\vartheta\nu$ (ideal $0$; page-local, the source's $r_{total}$ and
$\delta_{total}$). Written out,

$$\begin{aligned}
\Re\mathcal G&=1+\nu\tilde\vartheta_i-\tfrac12(\nu\tilde\vartheta_r)^2+\tfrac12(\nu\tilde\vartheta_i)^2-\tfrac12\nu^3\tilde\vartheta_r^2\tilde\vartheta_i+\tfrac16\nu^3\tilde\vartheta_i^3,\\
\Im\mathcal G&=-\nu\tilde\vartheta_r-\nu^2\tilde\vartheta_r\tilde\vartheta_i+\tfrac16\nu^3\tilde\vartheta_r^3-\tfrac12\nu^3\tilde\vartheta_r\tilde\vartheta_i^2
\end{aligned}$$

(Eq. (19)). *(Compiler check, not in the sources: these are the real and imaginary parts of
$1+K+K^2/2+K^3/6$ with $\tilde\vartheta=\tilde\vartheta_r+\mathrm i\tilde\vartheta_i$, verified
symbolically.)* The source's sign convention is the registry's: its MDCD symbol is the one printed
above, with $\tilde\vartheta_i=4c_{\mathrm{diss}}(\cos\vartheta-1)^3\le0$ (Eqs. (7)–(8)).

**Coupling by the time integrator.** The semi-discrete $\tilde\vartheta_r$ depends only on
$c_{\mathrm{disp}}$ and $\tilde\vartheta_i$ only on $c_{\mathrm{diss}}$. In the fully discrete
scheme, $\delta_\nu$ and $\lvert\mathcal G\rvert$ each depend on both. The authors find the
cross-effects "insignificant" for $c_{\mathrm{disp}}<0.1$ and $c_{\mathrm{diss}}<0.012$, with a
visible deviation only at $c_{\mathrm{diss}}=0.033$, and ignore them (§3.1, Figs. 2–3).

**Fully discrete optimization and ratio.** Li et al. (2023b) use three fully discrete
replacements of the semi-discrete tools above.

- *Weighted error integral.* They minimize
  $E=e^{-8\pi}\int_0^\pi e^{8(\pi-\vartheta)}(\arg\mathcal G+\nu\vartheta)^2d\vartheta$ (Eq. (26)).
  They present it as the fully discrete version of the integral of Sun et al. (Eq. (25)), whose
  integrand is $(\tilde\vartheta_r-\vartheta)^2$. The optimum is $c_{\mathrm{disp}}=0.0464$ for $\nu\le0.25$ and a fitted cubic
  in $\nu$ above (Eq. (27)). *(Compiler check, not in the sources: the constant agrees with the
  semi-discrete optimum $0.0463783$ of Li, Chen & Ren printed above, and the cubic of Eq. (27)
  gives $0.04608$ at $\nu=0.25$, $0.04600$ at $0.3$ and $0.04343$ at $0.5$, so the fitted
  function jumps by about $3\times10^{-4}$ at $\nu=0.25$.)*
- *Modified dispersion–dissipation condition.* They impose
  $\lvert\delta_\nu\rvert/\big\lvert\lvert\mathcal G\rvert-1\big\rvert\le10$ (Eq. (38)), the
  fully discrete counterpart of the Hu-type ratio $\zeta$. Its iso-surface at $10$ in
  $(\vartheta,\nu,c_{\mathrm{diss}})$ gives a "critical-adaptive" dissipation parameter. They
  fit it by cubics in the sensed wavenumber for $\nu=0.1$, $0.3$ and $0.5$, with the floor
  $0.001$ and the cap $0.012$ (§3.3, Eqs. (39)–(41), (48)–(50), Fig. 8, Appendix A).
- *Adaptive dispersion.* They choose $c_{\mathrm{disp}}$ so that $\delta_\nu=0$ at the sensed
  wavenumber (Eq. (43)). This replaces the semi-discrete condition $\tilde\vartheta_r=\vartheta$
  of an earlier preprint by Li et al. (Eq. (42)). The two choices differ negligibly at small
  $\nu$ and significantly at large $\nu$ (Eq. (47), Fig. 10).

The local wavenumber comes from a re-optimized [scale sensor](/definitions/scale-sensor.md),
reliable to $\vartheta=2.08$ (§3.2). The resulting scheme, ADADF, is on
[MDCD schemes](/methods/mdcd-scheme.md).

## Bloch-wave analysis of composite AMR operators

A refined patch breaks the translation invariance on which the single-mode ADR rests.
[Wang et al. (2026)](/sources/wang-2026.md) (§§4.1–4.4) extend the analysis to a two-level
[adaptive-mesh-refinement](/methods/adaptive-mesh-refinement.md) grid by Bloch (Floquet) theory,
which they recall from solid-state physics and from earlier flux-reconstruction and finite-element
analyses. Page-local symbols: $\theta_{\mathrm B}$ the Bloch phase, $\mathbb A_\ell$ and
$\mathbb A(\theta_{\mathrm B})$ the coupling blocks and the Bloch operator, $L_{\mathrm M}$ the
macro-cell length, $r_{\mathrm{ref}}$ the refinement ratio, $N_c$, $N_f$, $N_{\mathrm{DoF}}$
the coarse cells, fine cells and unknowns of one macro-cell.

- **Uniform baseline.** For $\frac{d}{dt}u_j=\sum_ma_mu_{j+m}$ the symbol is
  $\lambda=\sum_ma_me^{\mathrm im\vartheta}$ (page-local, not an eigenvalue $\lambda_l$ of $A$), written $\lambda\Delta x=-\mathrm i\tilde\vartheta$
  (Eqs. (14)–(17)). *(Compiler check, not in the sources: then
  $\lambda\Delta x=\tilde\vartheta_i-\mathrm i\tilde\vartheta_r$, so a mode decays for
  $\tilde\vartheta_i<0$. This is the registry's convention above, and the authors read
  dissipation as more negative $\mathrm{Im}\,\tilde\vartheta$.)*
- **Macro-cell.** A periodic coarse–fine–coarse cell holds uniform coarse cells of width
  $\Delta x_c$, a block of fine cells $\Delta x_f=\Delta x_c/r_{\mathrm{ref}}$ and ghost cells. The
  coarse operator reads restricted fine values on refined cells, and the fine operator reads
  prolonged coarse values in its ghost cells (Eqs. (18)–(24)). Linearized about a smooth state, the
  macro-cell evolves by $\frac{d}{dt}u^{(n)}=\sum_{\ell=-J}^J\mathbb A_\ell u^{(n+\ell)}$
  (Eqs. (25)–(26)).
- **Bloch eigenproblem.** The ansatz $u^{(n)}=\phi(\theta_{\mathrm B})e^{\mathrm i(n\theta_{\mathrm B}-\omega t)}$,
  $\theta_{\mathrm B}=k_wL_{\mathrm M}\in[-\pi,\pi]$, gives
  $\mathbb A(\theta_{\mathrm B})\phi=\lambda\phi$ with
  $\mathbb A(\theta_{\mathrm B})=\sum_\ell\mathbb A_\ell e^{\mathrm i\ell\theta_{\mathrm B}}$
  (Eqs. (27)–(29)).
- **Unfolding and branch selection.** Each $\theta_{\mathrm B}$ yields $N_{\mathrm{DoF}}$
  eigenvalues. They are unfolded to coarse-grid wavenumbers
  $\vartheta=k_w\Delta x_c=(\theta_{\mathrm B}+2\pi m)/N_c$, $m=0,\dots,\lceil N_c/2\rceil-1$,
  kept in $[0,\pi]$ (Eqs. (33)–(34)). The physical branch is the eigenvector with the largest
  projection on the normalized plane wave $e^{\mathrm ik_wx}$ sampled at the unknowns' positions,
  and $\lambda_{\mathrm{phys}}\Delta x_c=-\mathrm i\tilde\vartheta$. The other eigenpairs are
  parasitic (aliasing) branches (Eqs. (35)–(37)).

The analysed operator is fifth-order finite-difference WENO with **linear** weights, on
$L_{\mathrm M}=1$, $r_{\mathrm{ref}}=2$, $N_f=8$, $N_c=40$, $\Delta x_c=1/40$, $N_{\mathrm{DoF}}=44$
(§4.4.1). Three inter-level closures are compared (§4.3, Fig. 5): cell-centred Berger–Colella
transfers, cell-centred WENO prolongation and restriction, and the node-based WENO prolongation of
Shen, Qiu & Christlieb.

- **Dispersion.** The cell-centred closures deviate less from the uniform operator than the
  node-based one, most visibly for $\vartheta\in[1.5,2.5]$.
- **Dissipation.** All closures match the uniform dissipation at low wavenumbers and are more
  dissipative from $\vartheta\gtrsim2$. The authors interpret this as damping of
  interface-generated parasitic modes. The WENO closure deviates least near the cut-off, and the
  authors conclude that it is closest to the uniform fifth-order operator at high wavenumbers
  ([numerical dissipation](/definitions/numerical-dissipation.md)).
- **Linear stability.** The global eigenvalues of the semi-discrete cell-centred Berger–Colella and
  WENO operators, $\tilde\lambda_j=\lambda_j\Delta x_f/a$, lie in the closed left half-plane for
  $N_c=100$, $200$ and $1000$; the AMR closures enlarge the spectral footprint (Eq. (39), Fig. 6).
  With one global step set by the fine-level CFL number $\nu=a\Delta t/\Delta x_f$, all of them lie
  inside the stability region of SSP-RK3, $\lvert1+z+\tfrac12z^2+\tfrac16z^3\rvert\le1$,
  $z=\nu\tilde\lambda$, at $\nu=1.43$, which the authors call "aligned with the uniform scheme"
  (§4.4.2, Eqs. (40)–(42); [SSP Runge–Kutta](/methods/ssp-runge-kutta.md)).

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
Li et al. (2022b), Deng, Huang et al. (2026), Wang et al. (2021), Bezgin et al., Hiejima, Hong et al.,
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
  Fig. 3 for TENO8 and the spectrally optimized TENO8-opt). The founding paper states the
  wavenumbers: the five-point linear scheme is recovered "up to wave numbers 1.75, 1.85 and 1.95"
  for $C_T=10^{-5}$, $10^{-6}$ and $10^{-7}$; WENO-CU6 departs from its linear scheme at 1.2 and
  TENO6 "significantly" later, with WENO-CU6-M the least dispersive and dissipative of the six-point
  schemes ([Fu et al. (2016)](/sources/fu-2016.md), §§3.2–3.3, Figs. 3–4). The same property
  is stated without a new ADR computation by
  [Takagi et al. (2022)](/sources/takagi-2022.md) (§2.2). See
  [targeted ENO](/methods/targeted-eno.md).
- **The cut-off sets the onset of nonlinearity.** [Zhang et al. (2024b)](/sources/zhang-2024-b.md)
  (§3.2, Table 1) tabulate the reduced wavenumber at which their TENO turns nonlinear, from
  $1.058$ at $C_T=10^{-4}$ to $1.794$ at $10^{-13}$ (values on
  [targeted ENO](/methods/targeted-eno.md)), and design TENO6-SA from it. Its resolved
  bandwidth is $1.767$ at 1 % tolerance, against $1.100$ for TENO6 and TENO6-opt, $1.052$ for
  TENO6-A, $1.086$ for EWENO-CU6 and $1.330$ for WENO7-Z; at 1.5 % the values are $1.774$,
  $1.184$, $1.590$, $1.165$ and $1.418$ (§5.2, Fig. 5). They state that their spectra near
  $\vartheta\approx\pi$ "may differ slightly" from those of Fu et al. because of the grid
  resolution of the ADR. They complement the single-mode ADR with the nonlinear spectral
  analysis of Fauconnier & Dick, which applies the scheme to synthetic fields with spectrum
  $\propto\vartheta^{-5/3}$ up to $\pi$ and random phases and reports the mean and standard
  deviation of the modified wavenumber over $10^4$ samples; TENO6-SA has the best mean
  dispersion and a lower deviation at low and moderate wavenumbers (App. A, Fig. 6).
- **A Gaussian-RBF TENO.** [Liang & Fu (2024a)](/sources/liang-2024.md) (§3.2, Fig. 3;
  128 points) find both dispersion and dissipation of their nonlinear Gaussian-RBF TENO
  better than TENO5 and WENO5-Z, with the background linear scheme "restored exactly up to an
  intermediate wavenumber"; curves only ([RBF-WENO](/methods/rbf-weno.md)).
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
  [Li, Chen & Ren (2022a)](/sources/li-2022.md) (§3.3, Figs. 11–12) recovers the MDAD dissipation and
  the MDCD dispersion up to $\vartheta=2.06$, beyond which the WENO part activates; TENO-HY and
  MDCD-HY show irregular dissipation at low wavenumbers, which the authors trace to detector
  misjudgments, and WENO-Z is the most dissipative. The same sine-wave procedure grades the
  detectors themselves: the TENO-based one of Fu is correct only below $0.64$, the modified
  Ren detector up to $2.06$ (§3.2, Fig. 9). See [hybrid central–WENO schemes](/methods/hybrid-weno.md).
- **Resolution that does not degrade with the CFL number.** On the fully discrete curves of
  [Li et al. (2023b)](/sources/li-2023-b.md) (§3.4, Fig. 11), ADADF keeps a resolving efficiency
  of about $65.58\%$ for every $\nu$ tested, while the total dispersion errors of MDCD and MDAD
  grow rapidly with $\nu$. Its dissipation is much lower than MDCD's at low $\vartheta$ and grows
  at large $\vartheta$. *(Compiler check, not in the sources: $65.58\%$ of $\pi$ is
  $\vartheta=2.06$, against the sensor limit $2.08$, i.e. $66.21\%$.)*
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
  UW5 and UW7 as references ([Li et al. (2022b)](/sources/li-2022-b.md),
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
  solutions". Huang et al. (2026) (above) find their ROUND schemes markedly less dissipative than
  WENO3-NN at high wavenumbers. See [learned WENO weights](/methods/learned-weno-weights.md).
- **A learned five-point WENO and its hyperparameters.** [Nogueira et al. (2024)](/sources/nogueira-2024.md)
  (§3.3, Fig. 5) apply Pirozzoli's ADR to their WENO5-NN, whose weights a
  network outputs; the network is trained with a loss carrying two
  hyperparameters that they name $\alpha$ and $\beta$: $\alpha$ is the
  exponent of the loss, and $\beta$ is never identified with a printed
  symbol of it. Over a large wavenumber range it has
  less dispersion error than WENO5-JS and less dissipation in the
  well-resolved range. The five pairs $(\alpha,\beta)$ tested give a
  family of schemes with similar dispersion and different
  high-wavenumber dissipation, so the training hyperparameters act as
  spectral design parameters; $(0.2,0.1)$ is adopted. No values are
  printed. This WENO5-NN is not Stevens & Colonius's scheme of the same
  name (see [learned WENO weights](/methods/learned-weno-weights.md)).
- **An adaptive cut-off from a global smoothness factor.** The TENO-AZ of
  [Tang (2024)](/sources/tang-2024.md) (§3, Fig. 1) has better dispersion
  and lower dissipation than TENO-Z but is worse than TENO-A and TENO-LAD
  in both, with "some bias" of its curves near reduced wavenumbers 1.5
  (dispersion) and 2.0 (dissipation); see [adaptive TENO](/methods/adaptive-teno.md).
- **MP-limited gradient-based reconstruction against TENO5.** With the ADR procedure of
  Zhao et al., [Chamarthi (2023a)](/sources/chamarthi-2023.md) (§3.3, Fig. 3) finds
  that MIG4, the author's compact-gradient scheme with the monotonicity-preserving limiter, has better
  dispersion and dissipation than MEG6 and [TENO5](/methods/targeted-eno.md). Reusing the
  high-order second derivative as the limiter curvature improves the dispersion of MIG4
  over its base version, "marginal[ly]" for MEG6
  ([monotonicity-preserving limiter](/methods/monotonicity-preserving-limiter.md)). Chamarthi (2023a)'s
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
- **A learned third-order WCNS.** [Fan et al. (2025b)](/sources/fan-2025-b.md) (§4.2, Fig. 9)
  apply Pirozzoli's procedure to their WCNS3-MR-NN, a third-order
  [weighted compact nonlinear scheme](/methods/weighted-compact-nonlinear-scheme.md) whose
  multi-resolution weights a network predicts ([learned WENO weights](/methods/learned-weno-weights.md)),
  against WCNS3-JS, WCNS3-MR and the linear third-order WCNS: WCNS3-MR-NN has the better
  dispersion over a wide wavenumber range and the lower dissipation of the nonlinear schemes.
  The comparison is given by the curves only; no cut-off wavenumbers or values are printed.

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
  "Medium". Chamarthi (2023a) also says Fig. 2 shows the "imaginary and real parts" of the modified wavenumber as
  dispersion and dissipation, but labels the panels "Real" and "Imag" in the other order. The page
  uses the printed series, not the panel labels.
- Zhou et al. (2023) do not print the weight exponent $\sigma$ used for their nonlinear optimization
  (Table 2). The large-$C$ limit $0.0384$ equals the linear optimum at $\sigma=6$ of their Table 1.
  They also never print the exponent of their nonlinear weights, although they attribute post-shock
  noise to its value (§5.6).
- The fully discrete design of [Li et al. (2023b)](/sources/li-2023-b.md) is tied to the
  three-stage third-order Runge–Kutta method and calibrated at $\nu=0.1$, $0.3$, $0.5$ only. Its
  evidence is spectral curves and figures; the paper prints no error norms, convergence study or
  timings. The fits are not continuous. *(Compiler check, not in the sources: the dissipation cubics of
  Eqs. (48)–(50) give $0.00348$, $0.00372$ and $0.00264$ at the sensed wavenumber $2.08$, where
  the floor $0.001$ ends, and the $\nu=0.5$ cubic gives $0.01292$ at $\vartheta=\pi$, above the cap
  $0.012$.)* The authors call the effect of extending the floor to $2.08$ small and ignore it (§3.3).
- Zhang et al. (2024b) print the coefficient of $\Delta x\,f''$ in the dissipative part as
  $b_1+4b_2+6b_3$ (Eq. (21)); the expansion of $\sum_jb_j\big(f(x+j\Delta x)+f(x-j\Delta x)\big)$
  gives $\sum_jj^2b_j=b_1+4b_2+9b_3$, the pattern their other printed coefficients follow
  *(compiler check, not in the sources)*. Their §3.2 states the order conditions as
  "$G_1=0$", while §3.1 and the printed schemes have $G_1=1$.
- Wang et al. (2026) analyse the linear-weight operator only, so their Bloch curves and the
  $\nu=1.43$ bound say nothing about the nonlinear weights or the hybrid switch used in their
  shock tests. They normalize the eigenvalues by $\Delta x_f$ in Eq. (38) and by $\Delta x_c$ in
  the caption of Fig. 6; the CFL number of Eq. (40) uses $\Delta x_f$. They write the unfolded
  phase as $\theta_{\mathrm B}+2\pi m$ in Eq. (36) and divided by $N_c$ in Eq. (34), a notational
  difference.
- Zhang et al. (2024b)'s observation that conclusions from monochromatic ADR "do not transfer
  directly to nonlinear problems" (§6.1.3) rests on one cut-off study of the Titarev–Toro
  problem; see [adaptive TENO](/methods/adaptive-teno.md).
- [Luo & Wu (2021)](/sources/luo-2021-b.md) (§6) present "beating the
  underlying linear scheme" as contrary to the view, attributed to Pirozzoli,
  that nonlinear shock-capturing mechanisms always degrade spectral
  properties; the mechanism is negative nonlinear dissipation (see
  [numerical dissipation](/definitions/numerical-dissipation.md)).

# Citations

- [Fu, Hu & Adams (2016)](/sources/fu-2016.md) — §§3.2–3.3, Figs. 3–4; §4, Eqs. (30)–(33), Tables 3–4, Figs. 5–9: TENO spectra against $C_T$, $\zeta\approx O(10)$, blended optimized backgrounds.
- [Fu (2021)](/sources/fu-2021.md) — §3.1, §4.1, Eqs. (20)–(24): splitting, error integral, $\zeta\approx O(10)$.
- [Fu (2023)](/sources/fu-2023.md) — §2.5, Eqs. (12)–(16), Figs. 2–3: sign convention, TENO spectra.
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §§3–4, Figs. 1–4: Pirozzoli ADR, negative dissipation of WENO-Z+.
- [Li et al. (2022b)](/sources/li-2022-b.md) — §3.3(3), Fig. 2: WENO-ZN spectra.
- [Li et al. (2023b)](/sources/li-2023-b.md) — §3.1–3.4, Eqs. (16)–(27), (38)–(50), Figs. 2–3, 8–11: RK3 fully discrete errors, fully discrete integrated error and dispersion–dissipation ratio, ADADF spectra.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §2.2, §2.3: TENO and THINC spectral statements.
- [Deng (2023)](/sources/deng-2023.md) — Figs. 18, 28: ROUND spectra.
- [Huang et al. (2026)](/sources/huang-2026.md) — §5.2, Fig. 5: ROUND, LD-ROUND, WENO3-NN spectra.
- [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) — §3, Fig. 1: dispersion and dissipation of the Lerat–Corre family, $0.35\pi$ threshold (arXiv v1).
- [Wang et al. (2021)](/sources/wang-2021.md) — §4, Fig. 4.1: multi-resolution WENO spectra.
- [Bezgin et al. (2022)](/sources/bezgin-2022.md) — §4.8, Fig. 17: WENO3-NN spectra, zero dissipation at the cut-off.
- [Liang & Fu (2024b)](/sources/liang-2024-b.md) — §3.3.1, Eqs. (36)–(46): dispersion–dissipation splitting with printed weight, constraints and $b_0$.
- [Nogueira et al. (2024)](/sources/nogueira-2024.md) — §3.3, Fig. 5: ADR of WENO5-NN for five hyperparameter pairs.
- [Tang (2024)](/sources/tang-2024.md) — §3, Fig. 1: ADR of TENO-AZ against TENO-Z, TENO-A and TENO-LAD.
- [Hiejima (2022)](/sources/hiejima-2022.md) — §2.2 (Eq. (5)), Appendix (Fig. A.1): WCNS-JS and WCNS-T spectra at orders 5–11.
- [Li, Chen & Ren (2022a)](/sources/li-2022.md) — §2.1–2.3, Eqs. (6)–(38), Figs. 1–7; §3.2–3.4, Figs. 9, 11–12, Eqs. (62)–(69): MDCD symbol, pointwise dispersion–dissipation ratio, MDAD-HY and detector spectra.
- [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) — §3.2, Fig. 3: spectra of the scale-sensor TENO5-A (arXiv v1).
- [Hong, Ye & Ye (2022)](/sources/hong-2022.md) — §4.3, Figs. 6–7: TENO-M spectra against $C_s$.
- [Zhou et al. (2023)](/sources/zhou-2023.md) — §§3–4, Eqs. (19)–(28), Tables 1–2, Figs. 3–7: two-parameter WCNS symbol, ADR-based optimization, idealized dissipation, critique of the dispersion–dissipation condition.
- [Chamarthi (2023a)](/sources/chamarthi-2023.md) — §3.2, Eqs. (46)–(52), Fig. 2; §3.3, Fig. 3, Table 5: gradient-based reconstruction spectra, MIG4 and MEG6 against TENO5 (arXiv v2).
- [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) — §2.2, Eq. (22), Appendix A; §3.2, Fig. 15: Fourier design of the seventh-order gradient-based reconstruction (arXiv v1).
- [Wan & Xia (2022)](/sources/wan-2022.md) — §3, Fig. 3.2: WENO-H, WENO-ZQ, MRWENO, WENO-JS spectra.
- [Zhang et al. (2024b)](/sources/zhang-2024-b.md) — §3, Eqs. (18)–(21), Table 1, Fig. 1; §5.2, Figs. 5–6; §6.1.3; App. A: order cost of decoupled optimization, piecewise spectrum optimization, cut-off against nonlinearity onset, resolved bandwidths, nonlinear spectral analysis.
- [Liang & Fu (2024a)](/sources/liang-2024.md) — §3.2, Fig. 3: ADR of a Gaussian-RBF TENO.
- [Wang et al. (2026)](/sources/wang-2026.md) — §§4.1–4.4, Eqs. (14)–(42), Figs. 4–6: Bloch-wave analysis of AMR closures, global spectra, SSP-RK3 CFL bound.
- [Fan et al. (2025b)](/sources/fan-2025-b.md) — §4.2, Fig. 9: ADR of WCNS3-MR-NN against WCNS3-JS, WCNS3-MR and linear WCNS3.
