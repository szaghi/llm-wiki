---
type: Method
title: "WENO-CU6"
description: "WENO-CU6 (Hu et al.) is a sixth-order central-upwind WENO that adds a downwind three-point stencil to the fifth-order set, uses a six-point global smoothness indicator of order Δx⁶ and a WENO-Z-type weight with constant C = 20; in the bundle it is the main low-dissipation comparator of the TENO papers."
status: established
aliases: [WENO-CU6, sixth-order central-upwind WENO, WENO-CU6-M1]
tags: [weno, reconstruction, low-dissipation, finite-difference, turbulence]
timestamp: 2026-10-23T20:00:00Z
---

# WENO-CU6

WENO-CU6 is the adaptive central-upwind sixth-order WENO scheme of Hu et al., as
recalled by the bundle's sources: Fu (2021, §1) describes it as an "adaptive central-upwind
sixth-order WENO-CU6 scheme with a modified weighting strategy"; Ye et al. (2022, §1) say it was
built "by adding a downwind stencil" to the fifth-order WENO stencils; Li et al. (2022b, §1) that it
uses an "extra three-points substencil and a corresponding global smoothness indicator to construct
the sixth-order central-upwind WENO-Z type scheme"; Hiejima (2022, §1) places it "in the weighting
strategy to reduce the sensitivity of nonlinear adaptation". The global stencil is the six-point
$\{x_{i-2},\dots,x_{i+3}\}$, symmetric about $x_{i+1/2}$.

## Ingredients recalled in the sources

- **Six-point indicator.** The Jiang–Shu indicator of the full stencil,
  $$\begin{aligned}\beta_6=\tfrac1{120960}\big(&271779f_{i-2}^2-2380800f_{i-2}f_{i-1}+4086352f_{i-2}f_i-3462252f_{i-2}f_{i+1}+1458762f_{i-2}f_{i+2}-245620f_{i-2}f_{i+3}\\
  &+5653317f_{i-1}^2-20427884f_{i-1}f_i+17905032f_{i-1}f_{i+1}-7727988f_{i-1}f_{i+2}+1325006f_{i-1}f_{i+3}\\
  &+19510972f_i^2-35817664f_if_{i+1}+15929912f_if_{i+2}-2792660f_if_{i+3}\\
  &+17195652f_{i+1}^2-15880404f_{i+1}f_{i+2}+2863984f_{i+1}f_{i+3}+3824847f_{i+2}^2-1429976f_{i+2}f_{i+3}+139633f_{i+3}^2\big)\end{aligned}$$
  (Ye et al. 2022, Eq. (29), there attributed to Hu et al.; the same form is the $\beta_{3,6}$ of Fu
  2021, Eq. (28)). *(Compiler check, not in the sources: this equals the integral definition of the
  [smoothness indicator](/definitions/smoothness-indicator.md) for the degree-5 candidate on the six
  points.)*
- **Global reference indicator.** In the Jiang–Shu labelling of the three-point stencils ($S_0$ most
  upwind, $S_1$ central, $S_2$ downwind-biased),
  $$\tau_6=\beta_6-\tfrac16\big(\beta_0+\beta_2+4\beta_1\big)=O(\Delta x^6)$$
  (Ye et al. 2022, Eqs. (28)–(32), written there in the TENO labelling; the absolute value is taken in
  the general TENO form, Eq. (39)). *(Compiler check: a Taylor expansion confirms that the $\Delta x^2$
  to $\Delta x^5$ terms cancel.)* Fu (2023, Eq. (18)) recalls the same combination as the sixth-order
  $\tau_K$ used in TENO.
- **Weight template.** Ye et al. (2022, §2.2) write WENO-Z, WENO-CU6 and TENO as
  $\big(C+\tau/(\beta_k+\epsilon)\big)^q$ with $C=1$ for [WENO-Z](/methods/weno-z.md) and $C=20$ for
  WENO-CU6; a large $C$ pulls the weights towards the linear ones. The sources do not print the
  WENO-CU6 linear weights or exponent. Li, Chen & Ren (2022a, §3.1, Eqs. (42)–(45)) evaluate the weights of their MDAD-WENO
  "by the same method as the WENO-CU6 scheme", with
  $\alpha_k=d_k\big(20+\tau_6/(\beta_k+\epsilon)\big)^2$, $\epsilon=10^{-40}$, the downwind three-point indicator
  replaced by $\beta_6$ "following WENO-CU6", and their own dissipation-dependent linear weights
  ([MDCD schemes](/methods/mdcd-scheme.md)); they print $C=20$ and $q=2$ but do not say whether $q=2$ is the
  original WENO-CU6 exponent.
  Li, Sun, Zha, Zhu, Ding & Xia (2023b, Eq. (53)) write WENO-CU6 as $\alpha_k=d_k\big(C+\tau_6/(\beta_k+\epsilon)\big)$,
  exponent 1, "$C\gg1$", choose $C=100$ and $\epsilon=10^{-40}$, and use the same dissipation-dependent
  MDCD linear weights; they define neither the indicators nor $\tau_6$. The bundle's sources thus use
  three weight settings under the name WENO-CU6 ($C=20$ in Ye et al.'s template; $C=20$, $q=2$; $C=100$,
  $q=1$), none of them traced to the original paper.

The six-point indicator, the $\tau_6$ combination and the downwind stencil were carried over into
sixth-order [TENO](/methods/targeted-eno.md) and [AFTENO](/methods/afteno.md) (Ye et al. 2022,
§3.4).

## Performance reported against TENO

WENO-CU6 is the main comparator of Fu (2021), all runs FD with Roe-averaged characteristic
decomposition and SSP-RK3:

- [Shu–Osher](/benchmarks/shu-osher-problem.md) ($N_x=200$) and Titarev–Toro ($N_x=1000$): WENO-CU6
  produces density and velocity oscillations near the shocklets, where TENO8-AA and TENO10-AA stay
  sharp (§5.4, Figs. 4–5);
- [Woodward–Colella blast waves](/benchmarks/woodward-colella-blast-wave.md) ($N_x=400$): pressure
  oscillations and a velocity overshoot at $x\approx0.86$ (§5.5, Fig. 6);
- [double Mach reflection](/benchmarks/double-mach-reflection.md): TENO-AA at $512\times128$ resolves
  more small-scale vortical structure than WENO-CU6 at $1024\times256$ (§5.5.1, Figs. 7–8);
- [Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md) ($64\times256$) and
  [Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md) ($512^2$): finer structure with
  TENO-AA (§5.5.2, §5.6);
- 3-D Noh problem ($64^3$): TENO-AA has smaller density overshoot at the origin than the
  low-dissipation variant WENO-CU6-M1 at the same resolution (§5.8).

In Fu's review (2023, Figs. 4, 15–17) WENO-CU6 is the reference for the inviscid
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at $t=10$ and for decaying compressible
isotropic turbulence on $64^3$, where TENO8-A matches the filtered DNS more closely. Li et al. (2022b)
list WENO-CU6 only in their survey (§1).

Hong, Ye & Ye (2022, §5), with Roe or Van Leer fluxes and characteristic variables, report for
WENO-CU6 a slight oscillation at the Sod contact ($N_x=100$), an overshoot at the left density peak of the
blast waves and near the Shu–Osher valleys, Rayleigh–Taylor resolution comparable to their TENO-M6, and
slightly more dissipation than TENO6 in decaying isotropic turbulence ($128^3$). Their CPU times per 1000
steps put WENO-CU6 about 6 % above TENO-M6 and TENO8 about 50 % above WENO-CU6 (e.g. 1489.53 s against
2277.26 s on double Mach reflection, $960\times240$; Table 4). Li, Chen & Ren (2022a, §4.4.2) use the
low-dissipation WENO-CU6-M1 as comparator in the viscous Taylor–Green vortex at $\mathrm{Re}=1600$, where
their MDAD scheme matches the peak dissipation rate better. Liang et al. (2022, §1) state that WENO-CU6 may
produce spurious waves in under-resolved simulations "due to the non-dissipative nature of the background
central scheme".

## Qualifications

- All comparisons are by the developers of the competing scheme and rest on visual inspection of
  figures; the bundle has no source by the WENO-CU6 authors.
- The WENO-CU6 weights are recalled only through the template above; the exact form of the
  central-upwind weighting is not printed in any ingested source.
- Hong et al. (2022, §1) quote the earlier TENO paper of Fu et al. (its Table 4) for eight-point TENO
  taking "nearly 70 %" more time than WENO-CU6 on double Mach reflection at $1024\times256$; their own
  Table 4 gives 50–55 % *(compiler check, not in the sources: 2277.26/1489.53 = 1.53, and 1.54, 1.50 on
  the other two cases)*. Codes, grids and hardware differ.
- Li et al. (2023b, Table 1) print the downwind linear weight with the opposite sign; see
  [MDCD schemes](/methods/mdcd-scheme.md).
- Li, Chen & Ren (2022a, Eq. (44)) print the $f_{i-2}^2$ coefficient of $\beta_6$ as 271799, against
  271779 above; see [MDCD schemes](/methods/mdcd-scheme.md).

# Citations

- [Fu (2021)](/sources/fu-2021.md) — §1; §4.2, Eq. (28); §5.4–5.8, Figs. 4–15.
- [Ye et al. (2022)](/sources/ye-2022.md) — §1; §2.2, Eq. (6); §3.4–3.5, Eqs. (28)–(39).
- [Li et al. (2022b)](/sources/li-2022-b.md) — §1.
- [Fu (2023)](/sources/fu-2023.md) — §3.1, Eq. (18); Figs. 4, 15–17.
- [Hiejima (2022)](/sources/hiejima-2022.md) — §1.
- [Hong, Ye & Ye (2022)](/sources/hong-2022.md) — §1; §5.2–5.8, Figs. 9–16; §6, Table 4.
- [Li, Chen & Ren (2022a)](/sources/li-2022.md) — §3.1, Eqs. (42)–(45); §4.4.2, Fig. 29.
- [Liang et al. (2022)](/sources/liang-2022.md) — §1.
- [Li et al. (2023b)](/sources/li-2023-b.md) — §3.5, Eqs. (51)–(53), Table 1.
