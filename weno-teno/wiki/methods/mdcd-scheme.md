---
type: Method
title: "Minimized-dispersion and controllable-dissipation (MDCD) schemes"
description: "MDCD schemes are six-point fourth-order finite-difference fluxes whose dispersion and dissipation are set by two parameters; Li, Chen and Ren make the dissipation follow a scale sensor (MDAD), weight it like WENO-CU6 and hybridize it, Li et al. tune both parameters on the fully discrete scheme (ADADF), and Zhou et al. carry the same two parameters into a WCNS interpolation."
status: established
aliases: [MDCD, MDAD, MDAD-WENO, MDAD-HY, MDCD-HY, minimized dispersion and adaptive dissipation, Sun–Ren MDCD scheme, WCNS-SA, WCNS-opt, ADADF, ADADF-HY]
tags: [finite-difference, low-dissipation, weno, turbulence]
timestamp: 2026-10-24T05:57:00Z
---

# Minimized-dispersion and controllable-dissipation (MDCD) schemes

The MDCD scheme of Sun et al. (2011), as recalled by Li, Chen & Ren (2022a, §2.1), is a linear
[conservative finite-difference](/definitions/conservative-finite-difference-scheme.md) flux on the
six-point stencil $\{i-2,\dots,i+3\}$ whose order is lowered from the maximal six to four, and the two
freed degrees of freedom become a dispersion parameter $c_{\mathrm{disp}}$ and a dissipation parameter
$c_{\mathrm{diss}}$ (page-local; the source's $\gamma_{disp}$, $\gamma_{diss}$, renamed to keep
$\gamma$ for the ratio of specific heats). Li, Chen & Ren make $c_{\mathrm{diss}}$ follow the local
resolved scale ("minimized dispersion and adaptive dissipation", MDAD) and turn the scheme into a
shock-capturing hybrid.

## The linear scheme

With $f_i$ the point fluxes, the MDCD flux is (Eq. (7), with the spurious $1/\Delta x$ prefactor
removed, see Qualifications)

$$\begin{aligned}\hat f_{i+1/2}={}&\big(\tfrac12c_{\mathrm{disp}}+\tfrac12c_{\mathrm{diss}}\big)f_{i-2}+\big(-\tfrac32c_{\mathrm{disp}}-\tfrac52c_{\mathrm{diss}}-\tfrac1{12}\big)f_{i-1}+\big(c_{\mathrm{disp}}+5c_{\mathrm{diss}}+\tfrac7{12}\big)f_i\\
&+\big(c_{\mathrm{disp}}-5c_{\mathrm{diss}}+\tfrac7{12}\big)f_{i+1}+\big(-\tfrac32c_{\mathrm{disp}}+\tfrac52c_{\mathrm{diss}}-\tfrac1{12}\big)f_{i+2}+\big(\tfrac12c_{\mathrm{disp}}-\tfrac12c_{\mathrm{diss}}\big)f_{i+3}.\end{aligned}$$

For linear advection its modified wavenumber (Fourier convention $e^{\mathrm i k_wx}$) separates
exactly (Eq. (11)):

$$\tilde\vartheta_r=c_{\mathrm{disp}}\sin3\vartheta-\big(4c_{\mathrm{disp}}+\tfrac16\big)\sin2\vartheta+\big(5c_{\mathrm{disp}}+\tfrac43\big)\sin\vartheta,\qquad
\tilde\vartheta_i=c_{\mathrm{diss}}\cdot4(\cos\vartheta-1)^3 .$$

*(Compiler check, not in the sources: differencing the flux above reproduces the derivative stencil of
Eq. (6) and both parts of Eq. (11).)* The dispersion depends on $c_{\mathrm{disp}}$ only, the
dissipation on $c_{\mathrm{diss}}$ only; since $(\cos\vartheta-1)^3\le0$, $c_{\mathrm{diss}}\ge0$ is
dissipative (stable for advection speed $>0$) and $c_{\mathrm{diss}}=0$ gives a non-dissipative central
scheme (Eqs. (14)–(15); [approximate dispersion relation](/definitions/approximate-dispersion-relation.md),
[numerical dissipation](/definitions/numerical-dissipation.md)).

- **Dispersion.** $c_{\mathrm{disp}}=0.0463783$ minimizes the integrated error
  $\int_0^\pi e^{-8\vartheta}(\tilde\vartheta_r-\vartheta)^2d\vartheta$ (Martín et al.'s weight, value
  from Sun et al.; Eqs. (12)–(13)). The well-resolved wavenumber, the largest $\vartheta$ with
  $|\tilde\vartheta_r-\vartheta|<0.005$, is 1.297, against 0.976 for both the sixth-order central (C6)
  and the fifth-order upwind (UW5) schemes, "32.9 % improvement" (§2.1, Figs. 1–2). UW5 and C6 have
  identical dispersion.
- **Dissipation.** Sun et al. chose $c_{\mathrm{diss}}$ by trial and error; Hu & Adams' condition on
  the dispersion–dissipation ratio
  $\Lambda_{\mathrm{dd}}=|\partial\tilde\vartheta_r/\partial\vartheta-1|/|\tilde\vartheta_i|$ (page-local;
  Eq. (16)) imposed at $\vartheta=\pi$ as $\Lambda_{\mathrm{dd}}(\pi)\le9$ gives the minimum fixed value
  $c_{\mathrm{diss}}=0.012$ (Eq. (17)), the recommended MDCD(0.012); MDCD(0.035) dissipates like UW5
  (Fig. 3). *(Compiler check, not in the sources: at $\vartheta=\pi$,
  $|\partial\tilde\vartheta_r/\partial\vartheta-1|=16c_{\mathrm{disp}}+\tfrac83=3.4087$ and
  $|\tilde\vartheta_i|=32c_{\mathrm{diss}}$, so $\Lambda_{\mathrm{dd}}(\pi)=9$ needs
  $c_{\mathrm{diss}}=0.01184$.)*

## Adaptive dissipation: MDAD

Li, Chen & Ren (2022a, §2.3) set $c_{\mathrm{diss}}$ interface by interface from the
[scale sensor](/definitions/scale-sensor.md) $\vartheta_{\mathrm{ESW},i+1/2}$ (Eqs. (34)–(38)).
Inverting the ratio condition pointwise at $\Lambda_{\mathrm{dd}}=9$,
$c_{\mathrm{diss}}(\vartheta)=|\partial\tilde\vartheta_r/\partial\vartheta-1|/(9|4(\cos\vartheta-1)^3|)$
(Eq. (36)), gives two branches meeting at $\vartheta=1$; below it (more than six points per
wavelength) the inverted value is large because the dissipation shape is small, and a floor is used.
The adopted law is

$$c_{\mathrm{diss},i+1/2}=\begin{cases}0.001, & \vartheta_{\mathrm{ESW}}\le\vartheta_c,\\
\min\Big(0.001+0.011\sqrt{\dfrac{\vartheta_{\mathrm{ESW}}-\vartheta_c}{\vartheta_{\max}-\vartheta_c}},\ 0.012\Big), & \text{otherwise},\end{cases}\qquad \vartheta_c=1.0,\ \vartheta_{\max}=2.45 .$$

MDAD has the maximum dissipation of MDCD(0.012) but much less for $\vartheta\in(0.6,1.0)$; the range
with $|\tilde\vartheta_i|\le0.001$ extends to $\vartheta<1.02$, "35 % larger" (§2.3, Fig. 7; "1.348
times" in §3.4). The authors call MDAD "linear" for convenience; the coefficient depends on the
solution, so the scheme is nonlinear, and its spectral curves are sine-wave calibrations (§3).

## MDAD-WENO and the hybrid MDAD-HY

**MDAD-WENO** (§3.1). The MDAD flux is a convex combination of the four three-point candidates on
$\{i-2,i-1,i\}$, $\{i-1,i,i+1\}$, $\{i,i+1,i+2\}$ and the downwind $\{i+1,i+2,i+3\}$ (the last
$\tfrac16(11f_{i+1}-7f_{i+2}+2f_{i+3})$; Eq. (40)) with linear weights depending on both parameters
(Table 1):

$$d_0=\tfrac32\big(c_{\mathrm{disp}}+c_{\mathrm{diss}}\big),\quad d_1=\tfrac12-\tfrac32\big(c_{\mathrm{disp}}-3c_{\mathrm{diss}}\big),\quad d_2=\tfrac12-\tfrac32\big(c_{\mathrm{disp}}+3c_{\mathrm{diss}}\big),\quad d_3=\tfrac32\big(c_{\mathrm{disp}}-c_{\mathrm{diss}}\big),$$

non-negative for $0\le c_{\mathrm{diss}}\le\min(c_{\mathrm{disp}},\tfrac19-\tfrac13c_{\mathrm{disp}})$
(§2.3, §3.1). *(Compiler check, not in the sources: $\sum_kd_k\hat f^{(k)}_{i+1/2}$ reproduces the MDAD
flux exactly.)* The nonlinear weights follow [WENO-CU6](/methods/weno-cu6.md):
$\alpha_k=d_k\big(20+\tau_6/(\beta_k+\epsilon)\big)^2$, $\epsilon=10^{-40}$, with Jiang–Shu indicators on
the three upwind stencils, the downwind indicator replaced by the six-point $\beta_6$ because a fully
downwind stencil weighted like the others "may cause the instability", and
$\tau_6=|\beta_6-\tfrac16(\beta_0+\beta_2+4\beta_1)|$ (Eqs. (41)–(45);
[smoothness indicators](/definitions/smoothness-indicator.md)). Because the $d_k$ carry
$c_{\mathrm{diss},i+1/2}$, the nonlinear scheme inherits the adaptive dissipation.

**MDAD-HY** (§3.2). $\hat f_{i+1/2}=\delta^{\mathrm H}_{i+1/2}\hat f^{\mathrm{MDAD}}+(1-\delta^{\mathrm H}_{i+1/2})\hat f^{\mathrm{MDAD\text{-}WENO}}$
with a binary flag $\delta^{\mathrm H}\in\{0,1\}$ (page-local; Eq. (46)) from a new shock detector, a
modification of Ren et al.'s, recorded on [hybrid schemes](/methods/hybrid-weno.md). Its implementation for
systems (§3.4): the detector runs once per time step on density and entropy with normalized inputs,
flagged interfaces get buffer zones of 1–3 points; smooth interfaces use the linear flux on
component-wise global Lax–Friedrichs-split fluxes, flagged ones a
[characteristic decomposition](/methods/characteristic-decomposition.md) (eigenvectors at the simple
average), a second detection on each split characteristic flux, and MDAD-WENO where it fires. Viscous
terms use fourth-order central differences, curvilinear grids fourth-order central metrics; time
stepping is a low-storage fourth-order Runge–Kutta scheme at CFL 0.6. For smooth curvilinear grids the
1-D modified wavenumber carries over to the transformed flux (Remark, Eqs. (62)–(69)).

## Fully discrete design: ADADF

Li, Sun, Zha, Zhu, Ding & Xia (2023b) keep the six-point flux above and make **both** parameters
adaptive, tuned on the fully discrete scheme with three-stage third-order Runge–Kutta rather than on
the semi-discrete one. They name two defects of MDAD: its dissipation law ignores the errors of the
time integrator, and its scale sensor underestimates the wavenumber at medium and large $\vartheta$,
so it dissipates too little there (§1, §3.2). The scheme is called ADADF (adaptive dispersion,
critical-adaptive dissipation, fully discrete). Li et al. (2023b, §2) print the same flux and the same
modified wavenumber as Li, Chen & Ren (2022a), with the Fourier convention $e^{-\mathrm ik_wx}$ and
$\tilde\vartheta_i=4c_{\mathrm{diss}}(\cos\vartheta-1)^3\le0$ dissipative.

**Fully discrete errors** (§3.1, Eqs. (16)–(22)). For linear advection at CFL number $\nu$, one RK3
step multiplies a Fourier mode by $\mathcal G=1+K+K^2/2+K^3/6$, $K=-\mathrm i\tilde\vartheta\nu$
(page-local $\mathcal G$, $K$, as on the [approximate dispersion relation](/definitions/approximate-dispersion-relation.md) page), against $e^{-\mathrm i\vartheta\nu}$ exactly. The total dissipation error
is $|\mathcal G|$ and the total dispersion error $\delta_\nu=\arg \mathcal G+\vartheta\nu$
(page-local $\delta_\nu$). Each now depends on both parameters; the cross-effects are called
insignificant for $c_{\mathrm{disp}}<0.1$, $c_{\mathrm{diss}}<0.012$ and are ignored (Figs. 2–3).

**Three design steps** (§3.1–3.3):

1. *Fixed dispersion.* Minimizing $\int_0^\pi e^{-8\vartheta}\delta_\nu^2d\vartheta$ gives
   $c_{\mathrm{disp}}=0.0464$ for $\nu\le0.25$ and a cubic fit in $\nu$ above (Eqs. (26)–(27)), the
   semi-discrete optimum 0.0463783 recalled by Li, Chen & Ren for small $\nu$.
2. *Critical-adaptive dissipation.* The ratio condition of Hu et al., used by MDAD with bound 9, is
   replaced by $|\delta_\nu|/\big||\mathcal G|-1\big|\le10$ (Eq. (38)). Its iso-surface at 10 gives
   $c_{\mathrm{diss}}$ as a function of the sensed wavenumber, fitted by cubics for $\nu=0.1,0.3,0.5$,
   floored at 0.001 and capped at 0.012 (Eqs. (39)–(41)); after step 3 the floor is extended to
   $\vartheta<2.08$ (Eqs. (48)–(50)).
3. *Adaptive dispersion.* $c_{\mathrm{disp}}$ is chosen to make $\delta_\nu=0$ at the sensed
   wavenumber, the fully discrete form of Li, Ren & Su's semi-discrete condition
   $\tilde\vartheta_r=\vartheta$; cubic fits for $\nu=0.1,0.3,0.5$ run from about 0.034 below
   $\vartheta=0.3$ to 0.093–0.100 above 2.08 (Eqs. (42)–(46)).

Both parameters follow a re-optimized six-point [scale sensor](/definitions/scale-sensor.md), reliable
to $\vartheta=2.08$. With them ADADF keeps a resolving efficiency of about 65.58 % at every $\nu$ tested,
while the total dispersion errors of MDCD and MDAD grow with $\nu$ (§3.4, Fig. 11). The hybrid with
WENO-CU6, ADADF-HY, is on [hybrid schemes](/methods/hybrid-weno.md). Its WENO-CU6 partner uses the
MDAD-WENO linear weights above, $\alpha_k=d_k\big(100+\tau_6/(\beta_k+\epsilon)\big)$ with exponent 1 and
$\epsilon=10^{-40}$ (Eq. (53)), where Li, Chen & Ren use $\big(20+\tau_6/(\beta_k+\epsilon)\big)^2$.

**Results** (§4; figures only, no error norms, convergence orders or timings): on multi-wave advection
($m=20$ waves, 150 points, $\nu=0.5$) only ADADF-HY keeps phase and amplitude; on
[Shu–Osher](/benchmarks/shu-osher-problem.md), 2-D Riemann problems,
[Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md),
[Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md) and
[double Mach reflection](/benchmarks/double-mach-reflection.md) it shows the most small-scale
structure, with a slightly asymmetric Rayleigh–Taylor density field that the authors attribute to its low
dissipation (§4.5); in the inviscid [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) ($128^3$) the
kinetic energy decays as $t^{-1.2}$ and the spectrum follows $-5/3$ best. The title's "arbitrarily
high-order" family is only claimed: the fourth-order six-point member is the one built.

## The same two parameters in a WCNS interpolation

Zhou, Ding, Huang & Luo (2023, §3–4) free the first and last coefficients of the six-point central
*interpolation* of a [WCNS](/methods/weighted-compact-nonlinear-scheme.md), which gives a dispersion parameter
$\eta_{\mathrm Z}$ and a dissipation parameter $\xi_{\mathrm Z}$ (page-local, as on the WCNS page), and
difference the interface fluxes with Deng et al.'s sixth-order explicit midpoint-and-node scheme. Their modified
wavenumber (Eq. (24)) separates like Eq. (11) above. *(Compiler check, not in the sources: it is Eq. (11) with
$c_{\mathrm{disp}}=\tfrac{64}{45}\eta_{\mathrm Z}$, $c_{\mathrm{diss}}=\tfrac{64}{45}\xi_{\mathrm Z}$, the dissipative
part being $\tfrac{64}{45}\xi_{\mathrm Z}\cdot4(\cos\vartheta-1)^3$; the linear optimum for the weight
$e^{-8\vartheta}$, $\eta_{\mathrm Z}=0.0326$ (Table 1), corresponds to $c_{\mathrm{disp}}=0.0464$, the value 0.0463783 that Li, Chen & Ren quote from Sun et al.)*
Zhou et al. frame the work explicitly on Sun et al.'s criterion and extend it in two directions:

- **Dispersion optimized with the nonlinear weights.** The integrated error is evaluated with the
  [approximate dispersion relation](/definitions/approximate-dispersion-relation.md) of the full nonlinear scheme,
  and the optimal $\eta_{\mathrm Z}$ then depends on the weight constant $C$ and on $\xi_{\mathrm Z}$ (Table 2),
  becoming independent of $\xi_{\mathrm Z}$ near $C=10^9$; relaying Sun et al., they state that for the nonlinear
  scheme dispersion "mainly relies on" the dispersion parameter, while in Table 2 the optimum still depends on
  $\xi_{\mathrm Z}$ for $C\le10^5$ (0.0675 for $\xi_{\mathrm Z}=0$ against 0.0539 for $\tfrac3{128}$ at $C=10$; 0.0394 against 0.0373 at $C=10^5$).
- **Sensor-driven dissipation.** Like MDAD, the dissipation parameter follows a sensor, here the
  second-derivative ratio of Li et al. (Zhou et al.'s ref. [42], not ingested), together with $C$ ([scale sensor](/definitions/scale-sensor.md)); unlike MDAD the
  maximum $\xi_{\mathrm Z}=0.028$, i.e. $c_{\mathrm{diss}}=0.0398$, exceeds the dissipation of the fifth-order upwind
  scheme ($\xi_{\mathrm Z}=\tfrac3{128}$) *(compiler check, not in the sources: $\tfrac{64}{45}\cdot0.028=0.0398$)*.
  The authors also argue that Hu et al.'s dispersion–dissipation condition, the criterion behind MDCD(0.012),
  gives insufficient high-wavenumber dissipation (§4.2, Fig. 7b, a spectral comparison only).

The four-candidate weights of their WCNS-SA, $d_0=\tfrac43(\xi_{\mathrm Z}+\eta_{\mathrm Z})$, …,
$d_3=\tfrac43(\eta_{\mathrm Z}-\xi_{\mathrm Z})$ (Eq. (27)), are the interpolation counterpart of the MDAD-WENO
weights above; results are on the WCNS page.

## Results (Li, Chen & Ren 2022a, §4)

Comparators: [WENO-Z](/methods/weno-z.md), MDCD-HY and TENO-HY (Fu 2019,
[targeted ENO](/methods/targeted-eno.md)).

- **Linear advection** of a multi-wave packet: WENO-Z and TENO-HY converge at fifth order, MDCD-HY and
  MDAD-HY at fourth; MDAD-HY has the lowest $L_2$ error on relatively coarse grids (§4.1, Fig. 14).
- **Approximate dispersion relation.** MDAD-HY recovers MDAD dissipation and MDCD dispersion up to
  $\vartheta=2.06$, where its detector starts to fire; TENO-HY and MDCD-HY show irregular dissipation at
  low wavenumbers from detector misjudgments; WENO-Z is the most dissipative (§3.3, Figs. 11–12).
- **Shock problems.** On [Shu–Osher](/benchmarks/shu-osher-problem.md) ($N_x=200$) MDAD-HY resolves the
  post-shock waves best. Robustness needs tuning: detector threshold 0.5 on the
  [Woodward–Colella blast waves](/benchmarks/woodward-colella-blast-wave.md), 0.8 on
  [Sedov](/benchmarks/sedov-blast-wave.md), and $C_T=10^{-5}$ for TENO-HY on the blast waves; TENO-HY
  and the optimized TENO6 fail on Sedov "even with $C_T=0.1$" (§4.2). On
  [double Mach reflection](/benchmarks/double-mach-reflection.md) ($800\times200$) and
  [Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md) ($128\times512$) MDAD-HY gives the finest
  slip-line and interface structures (§4.3.1–4.3.2).
- **Efficiency.** On a viscous [shock–vortex interaction](/benchmarks/shock-vortex-interaction.md) on a
  $58\times58$ curvilinear mesh, MDAD-HY is the only scheme with centreline density $L_1$ error below
  $10^{-3}$ ($0.977\times10^{-3}$, 1.644 s; WENO-Z $2.464\times10^{-3}$, 3.013 s). At matched error the
  efficiency $1/(\text{error}\times\text{CPU time})$ of MDAD-HY is 1.5, 2.2 and 5.8 times that of
  MDCD-HY, TENO-HY and WENO-Z (Tables 2–3; no hardware given).
- **Turbulence.** In the inviscid [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) ($128^3$)
  C6 and MDCD(0.001) blow up at $t=4$–5, UW5 and MDCD(0.012) are more dissipative, MDAD runs untuned
  and best follows the $-5/3$ spectrum. At $\mathrm{Re}=1600$ on $256^3$ the enstrophy at $t=9$ is 9.866
  (MDAD, 4.1 % error) against 8.581 (UW5) and 9.214 (MDCD), DNS 10.284, at 19.3 % more CPU time; matching
  the UW5 error needs $168^3$ points with MDAD against $256^3$ with UW5 (§4.4, Tables 4–5).

## Qualifications

- The stability statement ($c_{\mathrm{diss}}\ge0$) holds for the frozen-coefficient linear scheme;
  the paper does not analyse a dissipation coefficient that varies between interfaces.
- Robustness depends on per-case detector thresholds (0.4, 0.5, 0.8) and buffer widths (0 to 3),
  which qualifies the claim of adaptivity without tuning; the efficiency comparison is on one test.
- Li, Chen & Ren print the flux (Eqs. (7), (34)) with a prefactor $1/\Delta x$ that Eq. (4) already
  applies to the flux difference; without it the flux reproduces Eq. (6), as checked above.
- In Eq. (44) Li, Chen & Ren print the $f_{i-2}^2$ coefficient of $\beta_6$ as 271799; Ye et al. (2022,
  Eq. (29)) print 271779 ([WENO-CU6](/methods/weno-cu6.md)). *(Compiler check, not in the sources:
  with 271799 the coefficients sum to 20, so the printed $\beta_6$ does not vanish on constant data;
  with 271779 they sum to 0.)* They also call MDAD-WENO "MADA-WENO" once (§3.4) and index the candidate
  fluxes by $i$ while the interface is $j+1/2$.

- **Printed slips of Li et al. (2023b).**
  - Table 1 prints $d_3=\tfrac32(c_{\mathrm{diss}}-c_{\mathrm{disp}})$, the negative of the value of
    Li, Chen & Ren (2022a, Table 1) above. *(Compiler check, not in the sources: solving
    $\sum_kd_k\hat f^{(k)}=\hat f$ gives $d_3=\tfrac32(c_{\mathrm{disp}}-c_{\mathrm{diss}})$, and with
    the printed sign the weights sum to $1+3c_{\mathrm{diss}}-3c_{\mathrm{disp}}$.)*
  - The cubic fits are discontinuous at their joins. *(Compiler check, not in the sources: the
    $c_{\mathrm{disp}}$ cubic of Eq. (27) gives 0.04608 at $\nu=0.25$ against 0.0464; the
    $c_{\mathrm{diss}}$ cubics of Eqs. (48)–(50) give 0.00348, 0.00372 and 0.00264 at
    $\vartheta=2.08$, where the floor is 0.001, and the $\nu=0.5$ cubic reaches 0.01292 at $\vartheta=\pi$,
    above the cap 0.012.)* The authors call the effect of extending the floor small.
  - The text after Eq. (46) calls $c_{\mathrm{disp}}$ the dissipation parameter; §4.7 attributes the
    Taylor–Green results to "the ADADF scheme", not ADADF-HY.

# Citations

- [Li, Chen & Ren (2022a)](/sources/li-2022.md) — §1; §2.1, Eqs. (6)–(17), Figs. 1–3; §2.3, Eqs. (34)–(38), Figs. 6–7; §3.1–3.4, Eqs. (39)–(69), Table 1, Figs. 8–12; §4, Tables 2–5, Figs. 14–30.
- [Ye et al. (2022)](/sources/ye-2022.md) — Eq. (29) ($\beta_6$ coefficient).
- [Li et al. (2023b)](/sources/li-2023-b.md) — §1; §2, Eqs. (3)–(15); §3.1–3.4, Eqs. (16)–(50), Figs. 2–11; §3.5, Eq. (53), Table 1; §4, Figs. 13–25.
- [Zhou, Ding, Huang & Luo (2023)](/sources/zhou-2023.md) — §1; §3, Eqs. (19)–(26), Table 1; §4, Eqs. (27)–(32), Tables 2–3, Fig. 7.
