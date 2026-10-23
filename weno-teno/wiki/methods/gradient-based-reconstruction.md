---
type: Method
title: "Gradient-based reconstruction (MEG/MIG schemes)"
description: "Gradient-based reconstruction interpolates point values to the interfaces of a conservative finite-difference scheme from the cell-centre value and high-order first and second derivatives, the first derivatives being shared with the viscous fluxes; it is fourth order (MEG6, MIG4) or seventh order (MEG7) for linear problems, MP-limited at shocks, and needs flux reconstruction for nonlinear order."
status: established
aliases: [GBR, GRB, gradient based reconstruction, MEG6, MIG4, MEG7, EG6, IG4H, MEG7-cons, MEG7-prim, monotonicity-preserving explicit gradient reconstruction, monotonicity-preserving implicit gradient reconstruction]
tags: [reconstruction, finite-difference, limiting, low-dissipation, gpu]
timestamp: 2026-10-23T03:53:00Z
---

# Gradient-based reconstruction (MEG/MIG schemes)

**Gradient-based reconstruction** (GBR; Chamarthi 2023a, §3.2; Chamarthi 2023b, §2.2; Chandravamsi
et al. 2023, §5.1) computes the left and right states $u^\mp_{i+1/2}$ of a
[conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md) from
the point value $u_i$ at the cell centre and approximations of its first and second derivatives there.
Let $u'_i$ and $u''_i$ denote these approximations of $\partial_xu$ and $\partial_x^2u$ at $x_i$
(page-local). The same $u'_i$ are reused in the viscous fluxes
([α-damping viscous flux](/methods/alpha-damping-viscous-flux.md)), which the three sources call
"gradient sharing" and present as the point of the method. Shocks are captured by a
[monotonicity-preserving limiter](/methods/monotonicity-preserving-limiter.md) applied to the GBR
state, and the interface flux is HLLC ([HLL-family solvers](/methods/hll-riemann-solvers.md)).

## The interpolation

All three sources start from van Leer's two-moment polynomial on cell $i$,

$$u(x)=u_i+u'_i(x-x_i)+\tfrac32\kappa_{\mathrm M}u''_i\Big[(x-x_i)^2-\tfrac{\Delta x^2}{12}\Big],$$

with the MUSCL parameter $\kappa_{\mathrm M}=\tfrac13$, evaluated at $x_i\pm\Delta x/2$
(Chamarthi 2023a, Eqs. (43)–(44); Chamarthi 2023b, Eqs. (14)–(15); Chandravamsi et al. 2023,
Eqs. (15)–(16)):

$$u^-_{i+1/2}=u_i+\frac{\Delta x}{2}u'_i+\frac{\Delta x^2}{12}u''_i,\qquad
u^+_{i+1/2}=u_{i+1}-\frac{\Delta x}{2}u'_{i+1}+\frac{\Delta x^2}{12}u''_{i+1}.$$

The interpolated $u$ are **point values**, not cell averages; Chamarthi (2023b, Remark 2.5) calls
GBR "fundamentally different" from van Leer's third-order finite-volume scheme although both use the
same polynomial, and Chamarthi (2023a, §3.2) attributes the order of the method to the point-value
reading. Chamarthi (2023a, §1) relates it to the compact finite-volume scheme of Sengupta et al.,
which uses upwind compact derivatives that cannot be reused for the viscous terms. Taking
$\kappa_{\mathrm M}=\tfrac12$ "will lead to anti-dissipation properties (not shown here)"
(Chamarthi 2023a, Remark 3.3).

**Second derivative from first derivatives.** $u''_i$ is the difference of two interface gradients
built with the α-damping construction,

$$\begin{aligned}
(\partial_xu)_{i+1/2}&=\tfrac12\big(u'_i+u'_{i+1}\big)+\frac{\alpha_{\mathrm D}}{2\Delta x}\big(\tilde u^+_{i+1/2}-\tilde u^-_{i+1/2}\big),\qquad u''_i=\frac{(\partial_xu)_{i+1/2}-(\partial_xu)_{i-1/2}}{\Delta x},\\
\tilde u^-_{i+1/2}&=u_i+\tfrac{\Delta x}{2}u'_i+\beta_{\mathrm D}(u_{i+1}-2u_i+u_{i-1}),\qquad
\tilde u^+_{i+1/2}=u_{i+1}-\tfrac{\Delta x}{2}u'_{i+1}+\beta_{\mathrm D}(u_{i+2}-2u_{i+1}+u_i),
\end{aligned}$$

with page-local damping and curvature parameters $\alpha_{\mathrm D}$, $\beta_{\mathrm D}$
(Chamarthi 2023b, Eqs. (18)–(21); Chandravamsi et al. 2023, Eqs. (29)–(30), which write the same
interface gradient for the viscous flux). Two parameter choices are used:

- **Fourth order**, $\alpha_{\mathrm D}=4$, $\beta_{\mathrm D}=0$:
  $\Delta x^2u''_i=2(u_{i+1}-2u_i+u_{i-1})-\tfrac{\Delta x}{2}(u'_{i+1}-u'_{i-1})$ (Chamarthi 2023a,
  Eq. (39); Chandravamsi et al. 2023, Eq. (19); Chamarthi 2023b, Remark 2.2). Chamarthi (2023a,
  Remark 3.1) notes that this is Adam's (1977) formula. *(Compiler check, not in the sources: the
  formula is exact for polynomials of degree up to 5 when $u'$ is exact.)*
- **Seventh order**, $\alpha_{\mathrm D}=\tfrac{38}{7}$, $\beta_{\mathrm D}=\tfrac3{190}$, found by
  Fourier analysis in Mathematica (Chamarthi 2023b, §2.2, Eq. (22), App. A). With
  $\delta_i=\Delta x\,u'_i$ (page-local),
  $$\Delta x^2u''_i=\tfrac1{70}\big(3u_{i-2}+178u_{i-1}-362u_i+178u_{i+1}+3u_{i+2}+60\delta_{i-1}-60\delta_{i+1}\big),$$
  $$u^-_{i+1/2}=\tfrac1{840}\big(3u_{i-2}+178u_{i-1}+478u_i+178u_{i+1}+3u_{i+2}+60\delta_{i-1}+420\delta_i-60\delta_{i+1}\big)$$
  (Eqs. (23)–(24)). Chamarthi prints Eq. (23) as $\partial_x^2u$; its right-hand side is
  $\Delta x^2\partial_x^2u$, the reading under which Eq. (24) holds.

*(Compiler check, not in the sources: substituting the α-damping formulas with
$\alpha_{\mathrm D}=\tfrac{38}7$, $\beta_{\mathrm D}=\tfrac3{190}$ reproduces Eqs. (23)–(24) exactly.)*

**First derivatives.** The schemes differ only in $u'_i$ (Chamarthi 2023a, §3.1–3.2; Chandravamsi et
al. 2023, Eqs. (17)–(18)):

- **E6 (explicit sixth order)**:
  $u'_i=\frac1{60\Delta x}\big[45(u_{i+1}-u_{i-1})-9(u_{i+2}-u_{i-2})+(u_{i+3}-u_{i-3})\big]$;
- **IG4 (implicit fourth order, "H for Hermitian")**: the tridiagonal compact scheme
  $\tfrac5{14}u'_{i-1}+u'_i+\tfrac5{14}u'_{i+1}=\tfrac{11}{14\Delta x}(u_{i+1}-u_{i-1})+\tfrac1{28\Delta x}(u_{i+2}-u_{i-2})$,
  solved with a tridiagonal solver.

Chamarthi (2023b, Remark 2.3) states that Lele's sixth-order compact first derivatives also give
seventh order with the same $(\alpha_{\mathrm D},\beta_{\mathrm D})$, at the cost of a tridiagonal
solve.

## Named schemes

| scheme | $u'_i$ | $(\alpha_{\mathrm D},\beta_{\mathrm D})$ | limiter | source |
|---|---|---|---|---|
| EG6, IG4H | E6, IG4 | $(4,0)$ | none (linear) | Chamarthi 2023a |
| MEG6, MIG4 | E6, IG4 | $(4,0)$ | MP | Chamarthi 2023a; Chandravamsi et al. 2023 |
| MEG7-cons, MEG7-prim | E6 | $(\tfrac{38}7,\tfrac3{190})$ | MP, with flux hybrid | Chamarthi 2023b |

The digit names the order of the gradient, not of the scheme: MEG6 and MIG4 are both fourth order for
linear problems (Chamarthi 2023a, §3.3; Chandravamsi et al. 2023, §5.1). MEG7 is the "monotonicity-preserving
explicit gradient" scheme with conservative (-cons) or primitive (-prim) variables. Chamarthi (2023a)
reconstructs primitive variables $(\rho,v,p)$ (and $(\phi_1\rho_1,\phi_2\rho_2,v,p,\phi_1)$ for the
[five-equation model](/definitions/five-equation-model.md)); limiting is done in characteristic
variables, the values and the gradients projected with the same frozen $L_{i+1/2}$, which is possible
because the projection is linear (Chamarthi 2023a, §3.3, Eqs. (62)–(64); Chandravamsi et al. 2023,
Eq. (20), with the eigenvectors of the primitive-variable system;
[characteristic decomposition](/methods/characteristic-decomposition.md)).

## Linear spectral properties

Chamarthi (2023a, Eqs. (46)–(49)) prints the symbols of the flux derivative for linear advection,
$\mathrm i\vartheta+\mathrm i\vartheta^5/720+\vartheta^6/1440+\dots$ for EG6 and
$\mathrm i\vartheta+\mathrm i\vartheta^5/720+\mathrm i\vartheta^7/2016+\vartheta^8/2304+\dots$ for IG4H
(registry $\vartheta$; positive real part dissipative in this convention), against
$\mathrm i\vartheta+\vartheta^6/60-\dots$ for the fifth-order upwind scheme U5: fourth order, IG4H with the
better dispersion, both with "superior dissipation" to U5 (Fig. 2). The author calls the fourth order
"contrary to expectations that the κ-scheme can be only at most third accurate", "not by design but
an unexpected outcome" (§3.2). For the seventh-order scheme the symbol is
$\mathrm i\vartheta+\vartheta^8/280-\mathrm i\vartheta^9/360-\vartheta^{10}/560+\dots$ (Chamarthi 2023b,
Eq. (22)); it has lower dissipation than the fourth-order scheme, which has slightly better dispersion
(§3.2, Fig. 15). *(Compiler check, not in the sources: inserting the E6 derivatives into Eq. (24) gives
the nine-point flux $\tfrac1{840}(-u_{i-4}+2u_{i-3}+22u_{i-2}-146u_{i-1}+568u_i+484u_{i+1}-104u_{i+2}+16u_{i+3}-u_{i+4})$
of Chamarthi's Eq. (33), whose difference has the printed symbol.)* The seventh-order and the
fourth-order schemes use the same nine-point flux stencil (Eq. (64)). In the
[approximate dispersion relation](/definitions/approximate-dispersion-relation.md) of the limited
schemes, MIG4 has lower dispersion error than MEG6 and [TENO5](/methods/targeted-eno.md) (Chamarthi
2023a, Fig. 3).

Remark 3.3 of Chamarthi (2023a) argues that a formally fourth-order scheme is acceptable, citing
optimized schemes of Weirs–Candler, Sun et al. and Fu et al. that give up formal order.

## Order for nonlinear problems

GBR is a **state** reconstruction: the interface flux $h(u^-_{i+1/2},u^+_{i+1/2})$ of the
reconstructed states. On the nonlinear [isentropic vortex](/benchmarks/isentropic-vortex.md) every
scheme of Chamarthi (2023a, Table 3), TENO5 included, converges at second order, with errors
$4.10\times10^{-5}$ at $N=2002$ for all; the author attributes it to the primitive-variable,
mid-point-type reconstruction, citing Zhang, Zhang & Shu, and states that genuine fourth
order needs flux reconstruction (§5). Chandravamsi et al. (2023, §10) concede the same second order for
MEG6 and MIG4.

Chamarthi (2023b, §2.4, Eqs. (29)–(37)) restores the order with a per-interface hybrid of a **flux**
reconstruction and the limited state:

$$f^{\mathrm c,\mp}_{i+1/2}=\sigma_{i+1/2}F^\mp_{i+1/2}+(1-\sigma_{i+1/2})f\big(u^{\mp,\mathrm{MP}}_{i+1/2}\big),$$

where $f^{\mathrm c,\mp}_{i+1/2}$ (page-local) are the left and right fluxes entering the central part
of the HLLC flux, $u^{\mp,\mathrm{MP}}_{i+1/2}$ the limited states, $F^\mp_{i+1/2}$ (page-local) is the GBR interpolation applied to the point fluxes $f_j$, the
limited states always enter the dissipative part of the HLLC flux, and $\sigma\in\{0,1\}$ is a
density-based switch ([hybrid schemes](/methods/hybrid-weno.md)). The $L_2$ density errors on the
isentropic vortex fall from $2.55\times10^{-3}$ ($25^2$) to $1.06\times10^{-8}$ ($200^2$) for MEG7-cons
and from $2.38\times10^{-3}$ to $1.03\times10^{-8}$ for MEG7-prim, with rates 5.25/6.03/6.59 and
5.13/6.00/6.68; the seventh-order WCNS7M gives 4.71/6.35/6.24 (Table 1). The text says both MEG7
variants "achieved seventh-order accuracy"; the rates shown stay below 6.7.

## Shock capturing and results

**Fourth-order schemes** (Chamarthi 2023a, §4; MIG4, MEG6 against TENO5, all with HLLC and SSP-RK3 at
CFL 0.2):

- linear advection: MIG4 and MEG6 about fourth order, TENO5 fifth, finest-grid errors nearly equal
  ($N=802$: TENO5 $2.21\times10^{-7}$, MIG4 $3.37\times10^{-7}$, MEG6 $2.35\times10^{-7}$; Table 2);
- [double Mach reflection](/benchmarks/double-mach-reflection.md), the 2-D shock–entropy wave of the
  [Shu–Osher family](/benchmarks/shu-osher-problem.md), [Leblanc](/benchmarks/leblanc-shock-tube.md):
  TENO5 oscillatory, MIG4 the most resolved; [Richtmyer–Meshkov](/benchmarks/richtmyer-meshkov-instability.md)
  (single gas, $320\times80$): no roll-ups with TENO5, the most with MIG4; Titarev–Toro: TENO5
  "severely under-resolves" (Exs. 4.4–4.12);
- [viscous shock tube](/benchmarks/viscous-shock-tube.md) ($\mathrm{Re}=1000$, $1280\times640$): MIG4
  closest to the fine-grid primary vortex; cost (Table 1, hardware not stated) MIG4+α-IG 51146 s,
  MEG6+α-EG 48506 s, TENO5+α-EG 50880 s, TENO5+α-IG 58680 s;
- inviscid [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) ($64^3$, linear schemes only):
  IG4H and EG6 preserve kinetic energy better than U5;
- five-equation multicomponent tests (Abgrall–Karni shock tube, shock–curtain,
  [shock–helium bubble](/benchmarks/shock-bubble-interaction.md),
  [triple point](/benchmarks/triple-point-problem.md), viscous air–SF$_6$ Richtmyer–Meshkov): no
  interface oscillations, MIG4 the thinnest interface (Exs. 4.14–4.18).

**Seventh-order schemes** (Chamarthi 2023b, §3; MEG7 against WCNS7M,
[weighted compact nonlinear scheme](/methods/weighted-compact-nonlinear-scheme.md)): MEG7 sharper on
Leblanc, blast waves, Shu–Osher, Titarev–Toro, Richtmyer–Meshkov, the 2-D shock–entropy wave and the
viscous shock tube, where WCNS7M "deviates significantly"; on the 1-D Sedov problem WCNS7M fails and
MEG7-cons needs a Zhang–Shu positivity treatment ([Sedov blast wave](/benchmarks/sedov-blast-wave.md),
[Zhang–Shu limiter](/methods/zhang-shu-scaling-limiter.md)); primitive reconstruction is less
dissipative on Richtmyer–Meshkov but "slightly more dissipative" on double Mach reflection
(Exs. 3.3–3.10). Wall-clock times (Table 2, same machine, hardware not stated) for MEG7-prim / MEG7-cons
/ WCNS7M are 224/205/345 s, 1025/1031/1502 s, 1806/1946/2493 s and 35455/38062/70082 s on
Richtmyer–Meshkov, the 2-D Riemann problem, double Mach reflection and the viscous shock tube.

## Curvilinear and moving meshes, GPU

Chandravamsi et al. (2023) extend MEG6 and MIG4 to 3-D generalized curvilinear, multi-block, static and
deforming grids with Thomas–Lombard conservative metrics. Their free-stream recipe differentiates and
interpolates the metrics with the unlimited, left/right-averaged GBR interpolation of the scheme itself,
$\tfrac12(x^-_{i+1/2}+x^+_{i+1/2})$, treating each metric term divided by the Jacobian as one variable;
uniform flow is then preserved to $10^{-16}$–$10^{-14}$ on sinusoidal and randomized grids, against
$10^{-3}$–$10^{-1}$ with non-conservative metrics (§7, §8, Table 2;
[free-stream preservation](/properties/free-stream-preservation.md)). In an implicit LES of a Mach 1.35
under-expanded jet at 13 M cells, MEG6 and MIG4 give screech Strouhal numbers 0.308–0.309 against 0.306
measured, [WENO-Z](/methods/weno-z.md) 0.432 (Table 3). Their OpenACC single-GPU port reaches 230.72×
over one Xeon Gold 5115 core for MEG6 on an A100 (jet, 13 M cells) and 211.80× for MIG4; reconstruction
takes more than 50 % of the run time and MIG4's tridiagonal gradient routine about 20 % (§9, Tables 5–6,
Fig. 21).

## Qualifications

- **Formal and observed order.** "Fourth-order" and "seventh-order" are the linear (Fourier) orders.
  With state reconstruction the observed order on a nonlinear problem is two (Chamarthi 2023a, Table 3),
  the limit that Wang et al. (2023b) state on the
  [conservative finite-difference](/definitions/conservative-finite-difference-scheme.md) page for an
  uncorrected two-point flux. The viscous discretization is only second order with Sutherland's law
  (Chamarthi 2023b, Remark 2.1).
- **The "κ-scheme" claim.** The fourth order is framed against van Leer & Nishikawa, who treat the
  finite-volume (cell-average) setting; the two statements concern different discretizations.
- **Internal inconsistency on dissipation.** Chamarthi (2023a) writes that MIG4 has "superior dispersion
  and dissipation properties" than MEG6 and TENO5 (§3.3), while its Table 5 rates the dissipation error
  of MIG and MEG "Medium" and of TENO5 "Low".
- **Printed slips.** Chamarthi (2023a) prints the compact scheme with $u'_{i-1}$ twice (Eq. (28)); the
  symmetric form above reproduces the printed modified wavenumber. In Table 2 the printed MIG4 orders
  3.89, 3.91, 3.97 do not follow from the printed errors *(compiler check, not in the sources: the
  $\log_2$ ratios are 3.93, 3.98, 3.88)*, while the TENO5 and MEG6 columns do. Chamarthi (2023b, Eq. (14))
  and Chandravamsi et al. (2023, Eq. (15)) print the polynomial with prefactors inconsistent with their
  own interface formulas (a $1/\Delta x$ on the first-derivative term, a missing factor $\tfrac12$ on the
  curvature term); the interface formulas above are those of Eq. (15) and Eq. (16) respectively.
  Chandravamsi et al. print sums for the differences of E6 and IG4 (Eqs. (17)–(18)); with sums a
  constant would have non-zero derivative.
- **Cost wording.** Chamarthi (2023b, §3.1) calls MEG7 "at least 40 % cheaper" than WCNS7M on average.
  *(Compiler check, not in the sources: from Table 2, MEG7-prim saves 35, 32, 28 and 49 %, on average
  36 %; WCNS7M costs 38–98 % more than MEG7-prim.)*
- The comparisons are made by the authors of the schemes; TENO5's parameters are not printed in
  Chamarthi (2023a), and Chamarthi (2023b) compares MEG7-cons with a positivity treatment against WCNS7M
  without one on Sedov.

# Citations

- [Chamarthi (2023a)](/sources/chamarthi-2023.md) — §1; §3.1, Eqs. (27)–(40); §3.2, Eqs. (41)–(52), Remarks 3.1–3.4, Fig. 2; §3.3, Eqs. (53)–(64), Fig. 3, Table 5; §4, Tables 1–3, Exs. 4.1–4.18; §5.
- [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) — §1.2; §2.1–2.4, Eqs. (8)–(37), Remarks 2.1–2.5; §3, Tables 1–2, Exs. 3.1–3.11; §3.2, Figs. 15–16; App. A, Eq. (64).
- [Chandravamsi et al. (2023)](/sources/chandravamsi-2023.md) — §5.1, Eqs. (15)–(25); §5.2, Eqs. (29)–(30); §7, Eqs. (36)–(44); §8, Tables 2–3; §9, Tables 5–6, Fig. 21; §10.
