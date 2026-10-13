---
type: Method
title: "HLLC Riemann solver"
description: "Toro, Spruce & Speares' three-wave HLL-type solver for the Euler equations: two star states separated by a contact wave of speed S_M, with equal pressure and normal velocity, so stationary contacts and shear waves are kept exactly; star states and flux, the families of wave-speed estimates (Davis, Roe-average, Einfeldt, pressure-based, Batten's S_M), sonic and low-density behaviour, positivity, and its shock instability."
status: established
aliases: [HLLC, HLLC flux, Harten–Lax–van Leer–contact, HLL with contact restoration]
tags: [riemann-solver, numerical-flux, hllc, euler, contact-discontinuity, shock-instability]
timestamp: 2026-10-13T00:00:00Z
---

# HLLC Riemann solver

**From HLL.** HLL replaces the Riemann fan between the fastest left and
right signal speeds $S_L \le S_R$ by its integral average
$$u^{\mathrm{HLL}}_* = \frac{S_R u^+ - S_L u^- + f(u^-) - f(u^+)}{S_R - S_L},$$
and takes the flux from the integral conservation law, not as
$f(u^{\mathrm{HLL}}_*)$:
$$\hat f^{\mathrm{HLL}} = \frac{S_R f(u^-) - S_L f(u^+) + S_L S_R (u^+ - u^-)}{S_R - S_L} \quad (S_L \le 0 \le S_R),$$
with $f(u^-)$ for $0 \le S_L$ and $f(u^+)$ for $0 \ge S_R$
([Toro (1997)](/sources/toro-1997.md), §§10.2–10.3, eqs. 10.13, 10.20–10.21).
The two-wave model is exact only for $2\times2$ systems. For the Euler
equations it smears contacts, shear waves and material interfaces, which
"is unacceptable" when they are stationary (p. 293).
HLL itself has its own page: [HLL Riemann solver](/methods/hll-riemann-solver.md).

**The HLLC model** (§10.4, eqs. 10.26–10.36). A middle wave of speed
$S_M$ splits the fan into two star states $u^{\mathrm{HLLC}}_{*L}$ and
$u^{\mathrm{HLLC}}_{*R}$. The exact solution satisfies, and HLLC imposes,
equal pressure and equal normal velocity on both sides of the middle
wave, tangential velocity unchanged across the outer waves, and
$S_M$ equal to that normal velocity (eqs. 10.29–10.30). The Rankine–Hugoniot
conditions across $S_L$ and $S_R$ then give, for the left star state in
2D (one tangential component $v_t$; in 3D one row per component),
$$u^{\mathrm{HLLC}}_{*L} = \rho^-\,\frac{S_L - v_n^-}{S_L - S_M}\begin{pmatrix} 1\\ S_M\\ v_t^-\\ \dfrac{E^-}{\rho^-} + (S_M - v_n^-)\left[S_M + \dfrac{p^-}{\rho^-(S_L - v_n^-)}\right]\end{pmatrix},$$
and $u^{\mathrm{HLLC}}_{*R}$ the same with $+$ data and $S_R$. The flux is
$$\hat f^{\mathrm{HLLC}} = \begin{cases} f(u^-), & 0 \le S_L,\\ f(u^-) + S_L\left(u^{\mathrm{HLLC}}_{*L} - u^-\right), & S_L \le 0 \le S_M,\\ f(u^+) + S_R\left(u^{\mathrm{HLLC}}_{*R} - u^+\right), & S_M \le 0 \le S_R,\\ f(u^+), & 0 \ge S_R.\end{cases}$$
A passive scalar advected with the flow is carried by the star states
with the same factor $\rho^\mp(S_{L,R} - v_n^\mp)/(S_{L,R} - S_M)$ (eq. 10.36).
The same flux, written as $\hat f^{\mathrm{HLL}}$ plus the anti-diffusive
term $S_L(u^{\mathrm{HLLC}}_{*L} - u^{\mathrm{HLL}}_*)$ for
$S_L \le 0 \le S_M$, is the starting point of the shock-instability cures
([Simon & Mandal (2019)](/sources/simon-2019.md), eq. 13).

**Wave-speed estimates** (§10.5, eqs. 10.37–10.58). The book lists, as
printed:
* *Davis, direct:* $S_L = v_n^- - c^-$, $S_R = v_n^+ + c^+$; or
  $S_L = \min(v_n^- - c^-,\ v_n^+ - c^+)$, $S_R = \max(v_n^- + c^-,\ v_n^+ + c^+)$.
* *Roe-average eigenvalues*, credited to "Davis [94] and Einfeldt [105]":
  $S_{L,R} = v_n \mp c$ at the Roe state, with $\sqrt\rho$-weighted
  velocity and total specific enthalpy and the sound speed from them.
* *Einfeldt:* $S_L$ and $S_R$ are a mean normal velocity (not
  defined on the page) minus and plus $\bar c_{\mathrm E}$,
  $$\bar c_{\mathrm E}^2 = \frac{\sqrt{\rho^-}\,(c^-)^2 + \sqrt{\rho^+}\,(c^+)^2}{\sqrt{\rho^-} + \sqrt{\rho^+}} + \frac12\,\frac{\sqrt{\rho^-\rho^+}}{\left(\sqrt{\rho^-} + \sqrt{\rho^+}\right)^2}\,(v_n^+ - v_n^-)^2 .$$
  The min/max form called "Einfeldt's" on the
  [approximate Riemann solvers](/methods/approximate-riemann-solvers.md)
  page (after Xie et al.) is a different formula under the same name.
* *Pressure-based* (Toro, Spruce & Speares): $S_L = v_n^- - c^-q^{\mathrm w}_L$,
  $S_M = v_{n*}$, $S_R = v_n^+ + c^+q^{\mathrm w}_R$, with
  $q^{\mathrm w}_L = 1$ if $p_* \le p^-$ (rarefaction) and
  $q^{\mathrm w}_L = \left[1 + \frac{\gamma+1}{2\gamma}(p_*/p^- - 1)\right]^{1/2}$
  otherwise (the exact shock speed for that $p_*$), similarly on the
  right. $p_*$ and $v_{n*}$ come from the approximate-state solvers PVRS,
  TRRS or TSRS; "in computational practice we use the hybrid scheme"
  (p. 305; [exact Riemann solver](/methods/exact-riemann-solver.md)).
* *Batten et al.'s middle wave:* given $S_L$ and $S_R$,
  $$S_M = \frac{p^+ - p^- + \rho^- v_n^-(S_L - v_n^-) - \rho^+ v_n^+(S_R - v_n^+)}{\rho^-(S_L - v_n^-) - \rho^+(S_R - v_n^+)},$$
  which makes the pressures $p^\mp + \rho^\mp(S_{L,R} - v_n^\mp)(S_M - v_n^\mp)$
  of the two star states equal (eqs. 10.57–10.58).

**Contacts against HLL** (§10.7, Fig. 10.9). HLLC, like the exact,
Roe and Osher solvers, gives infinite resolution of a stationary
contact. On an isolated stationary contact ($\rho = 1.4 \mid 1$, $p = 1$,
$t = 2$, 100 cells) HLL smears the contact over the whole domain while
HLLC keeps it exact, and HLLC resolves a slowly moving contact
($v = 0.1$) sharply. On Tests 1–4 of the
[exact-solver suite](/methods/exact-riemann-solver.md) HLL and HLLC are
"virtually indistinguishable" (§10.8). In 2D, on a single Mach
reflection at $M_s = 1.2$ on a 30° wedge, a piecewise-linear scheme with
HLL smears the slip surface "very significantly" where HLLC does not
(§17.2, Figs. 17.10–17.12; [double Mach reflection](/benchmarks/double-mach-reflection.md)).
The HLL contact defect is also what [HLLEM](/methods/hllem-riemann-solver.md)
repairs by a linear sub-structure instead of a second star state.

**Sonic points and low density.** Near the sonic point of the modified
Sod problem, first-order HLLC is "more accurate than the corresponding
results using the exact Riemann solver", without an entropy fix:
"correct handling of sonic flow is a distinctive feature of HLL-type
Riemann solvers" ([Toro (1997)](/sources/toro-1997.md), §10.8, p. 308).
On the 123 problem it does not fail, unlike Roe's solver, but it is less
accurate than the exact and approximate-state solvers in velocity and
internal energy (Fig. 10.6; [double rarefaction](/benchmarks/double-rarefaction.md)).
Later papers state the same pair of facts: HLLC works for low density
and sonic points without fixes ([Titarev & Toro (2004)](/sources/titarev-2004.md), §4.1),
and with compact WENO it leaves oscillations in velocity and internal
energy near vacuum, where Lax–Friedrichs is cleaner
([Guo, Xiong & Shi (2014)](/sources/guo-2014.md), Examples 6, 8).

**Positivity.** With Batten et al.'s speeds the star states stay
admissible, and the first-order scheme preserves positivity under
$\Delta t\,\Vert\vert\mathbf v\vert + c\Vert_\infty/h \le 1$
([Guo, Xiong & Shi (2014)](/sources/guo-2014.md), §2.4, Remark 1;
[positivity preservation](/properties/positivity-preserving.md)).

**Shock instability.** Resolving the contact and shear waves exactly is
what makes HLLC "highly susceptible" to the carbuncle, odd–even
decoupling and kinked Mach stems at strong grid-aligned shocks
([Simon & Mandal (2019)](/sources/simon-2019.md), §§4–5;
[Xie et al. (2021)](/sources/xie-2021.md), §6.3;
[numerical shock instability](/definitions/numerical-shock-instability.md)).
Against HLL and HLL-BVD at second order, in the strong Lax problem HLLC
resolves the stationary contact best but overshoots most at the shock
(on the isolated moving contact, with the data of Toro's Test 6, HLL-BVD
is sharper than HLLC), and HLLC
oscillates most behind a slowly moving shock, decouples odd–even on a
perturbed Mach 20 shock, shows carbuncle-type oscillations along the
axes of a Sedov blast, and kinks the double-Mach-reflection stem
([Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md), §§III A, III C–H;
[slowly moving shock anomaly](/definitions/slowly-moving-shock-anomaly.md)).
The cures (selective wave modification, entropy control) are on the
[shock-instability cures](/methods/shock-instability-cures.md) page.

**Uses in this bundle.**
* FV-WENO in 3D: HLLC about twice as accurate as the Rusanov-based scheme
  on the vortex, and rolls up the slip lines of the double Mach
  reflection more than MUSTA ([Titarev & Toro (2004)](/sources/titarev-2004.md), §§4–5).
* GP-WENO for Euler ([Reyes et al. (2018)](/sources/reyes-2018.md), §5).
* Relativistic MHD: HLLC of Mignone–Bodo, and Kim–Balsara's version with
  a common normal velocity and total pressure in both star states
  ([Balsara & Kim (2016)](/sources/balsara-2016-b.md), §4.1, Appendix B).
* One of the face fluxes of fourth-order FV for MHD
  ([Berta et al. (2024)](/sources/berta-2024.md), §§3.2–3.3).
* HLLC or HLLD sides inside a multidimensional solver give "not that much
  incremental benefit" ([Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §3.1;
  [multidimensional Riemann solvers](/methods/multidimensional-riemann-solvers.md)).
* The cut-element immersed-boundary solver INCA (third-order WENO, HLLC)
  ([Baskaya et al. (2024)](/sources/baskaya-2024.md)).
* WAF with HLLC on Toro's explosion and wedge-reflection tests
  ([Toro (1997)](/sources/toro-1997.md), §§17.1–17.2;
  [multidimensional explosion](/benchmarks/multidimensional-explosion.md)).

The overview of all solvers and their roles in capturing schemes is the
[approximate Riemann solvers](/methods/approximate-riemann-solvers.md) page.

**Later uses (batch 16).** *Not in Harten, Lax & van Leer.* The 1983 paper
([Harten, Lax & van Leer (1983)](/sources/harten-1983-d.md), §3B(ii)) already
builds a two-intermediate-state Godunov-type solver, but it is not HLLC: its
middle speed is an entropy-variable average equal to the shock or contact
speed whenever Rankine–Hugoniot holds, its star states come from a numerical
line flux, and an added viscosity, with unspecified constants, enforces the
entropy inequality. The alias "Harten–Lax–van Leer–contact" names the HLL
lineage, not this solver.

# Citations

1. [Toro (1997)](/sources/toro-1997.md), §§10.2–10.8, 17.1–17.2.
2. [Titarev & Toro (2004)](/sources/titarev-2004.md), §§4–5.
3. [Guo, Xiong & Shi (2014)](/sources/guo-2014.md), §2.4, Examples 6, 8.
4. [Simon & Mandal (2019)](/sources/simon-2019.md), §§4–5, eq. 13.
5. [Xie et al. (2021)](/sources/xie-2021.md), §6.3.
6. [Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md), §§III A, III C–H.
7. [Reyes et al. (2018)](/sources/reyes-2018.md), §5.
8. [Balsara & Kim (2016)](/sources/balsara-2016-b.md), §4.1, Appendix B.
9. [Berta et al. (2024)](/sources/berta-2024.md), §§3.2–3.3 (arXiv v4).
10. [Balsara & Nkonga (2017)](/sources/balsara-2017-b.md), §3.1.
11. [Baskaya et al. (2024)](/sources/baskaya-2024.md) (arXiv v1).
12. [Harten, Lax & van Leer (1983)](/sources/harten-1983-d.md), §3B(ii).
