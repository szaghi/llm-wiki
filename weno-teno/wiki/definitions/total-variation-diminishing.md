---
type: Definition
title: "Total variation diminishing (TVD) and slope limiters"
description: "TVD schemes do not increase the total variation; the page gives Harten's original TVNI definition and sufficient incremental-form condition, the TVD and TVB definitions of Shu and Osher, van Leer's 1979 slope limiters, the Sweby-region limiter formulas of later sources and their normalised-variable reading, the first-order barrier at extrema, and the roles of limiters in WENO, central and DG schemes."
status: established
aliases: [TVD, TVNI, total variation nonincreasing, TVB, total variation bounded, TVD limiter, flux limiter, slope limiter, MUSCL limiter, minmod, monotonicity algorithm, TVB limiter]
tags: [limiting, reconstruction, finite-volume, central-scheme]
timestamp: 2026-10-30T07:59:00Z
---

# Total variation diminishing (TVD) and slope limiters

**Total variation diminishing** (TVD) schemes satisfy $TV(u^{n+1})\le TV(u^n)$,
$TV(u)=\sum_i\lvert u_{i+1}-u_i\rvert$. The property was introduced by
[Harten (1983a)](/sources/harten-1983.md) as **total variation nonincreasing** (TVNI)
(next section); most later sources of the bundle use it without restating it and
impose it through Sweby's limiter region; the estimate and the incremental-form
conditions behind that region are restated by
[Puppo et al. (2023)](/sources/puppo-2023.md) (§2; below).
For a second-order reconstruction the TVD constraint is imposed through a
**limiter** $\psi$ of the slope ratio

$$r_i=\frac{\bar u_i-\bar u_{i-1}}{\bar u_{i+1}-\bar u_i},\qquad
u^-_{i+1/2}=\bar u_i+\tfrac12\psi(r_i)\,(\bar u_{i+1}-\bar u_i),$$

with the mirror formula, $\psi(1/r_i)$ and $\bar u_{i-1}-\bar u_i$, for
$u^+_{i-1/2}$ ([Deng (2023)](/sources/deng-2023.md), §4.1, Eqs. (4.1)–(4.2)).
Deng places Sweby's **second-order TVD region** between MinMod and SuperBee
(§4.1, Fig. 2).

## Origin: TVNI, TVD and TVB

[Harten (1983a)](/sources/harten-1983.md) (§2, Eqs. (2.2)–(2.4)) defines a scalar scheme
$u^{n+1}=\mathcal Hu^n$ (page-local solution operator $\mathcal H$) to be TVNI if
$TV(\mathcal Hu)\le TV(u)$, motivated by the monotonicity property of entropy solutions,
whose total variation does not increase; the word "TVD" is not printed in the paper. Its
Theorem 2.1 places it between two other notions: monotone $\Rightarrow$ TVNI
$\Rightarrow$ monotonicity preserving, and linear TVNI schemes are monotone and hence
first order ([monotone schemes](/definitions/monotone-scheme.md)). **Lemma 2.2** gives the
condition in incremental form: the scheme

$$u^{n+1}_i=u_i+C^+_{i+1/2}(u_{i+1}-u_i)-C^-_{i-1/2}(u_i-u_{i-1}),$$

with coefficients depending on $u_{i-1},\dots,u_{i+2}$ and $u_{i-2},\dots,u_{i+1}$
respectively (page-local $C^\pm$), is TVNI **if**
$C^+_{i+1/2}\ge0$, $C^-_{i+1/2}\ge0$ and $C^+_{i+1/2}+C^-_{i+1/2}\le1$ (Eqs. (2.9)–(2.10)); the
paper states the condition as sufficient and proves it by summing the absolute values of
$\Delta_{i+1/2}u^{n+1}=C^-_{i-1/2}\Delta_{i-1/2}u+(1-C^-_{i+1/2}-C^+_{i+1/2})\Delta_{i+1/2}u+C^+_{i+3/2}\Delta_{i+3/2}u$
(Eq. (2.11); $\Delta_{i+1/2}u=u_{i+1}-u_i$, page-local). Every three-point conservative scheme
with a differentiable flux can be put in this form by the mean-value theorem (Eq. (2.13));
Harten's own second-order TVNI scheme is built on it
([Harten's TVD scheme](/methods/harten-tvd-scheme.md)).

[Shu & Osher (1988)](/sources/shu-1988.md) (§I, Eqs. (1.5)–(1.7)) use the name TVD for
$TV(u^{n+1})\le TV(u^n)$ and define **total variation bounded** (TVB) on $0\le t\le T$:
$TV(u^n)\le B$ for all $n$ and $\Delta t$ with $0\le n\Delta t\le T$, with $B$ depending only on
$TV(u^0)$ (page-local $B$). They carry both notions to the time discretization: a
Runge–Kutta method that is a convex combination of forward-Euler steps is TVD (TVB) under a
scaled CFL condition whenever forward Euler is ([SSP Runge–Kutta](/methods/ssp-runge-kutta.md),
§II); [Shu (2009a)](/sources/shu-2009.md) (§3.1) states that these methods keep the stability of
forward Euler "in the total variation seminorm, or any other norm or seminorm". [Harten et al. (1987a)](/sources/harten-1987.md) (§1, Eqs. (1.19)–(1.21)) state the
stability notion behind both: total variation bounded uniformly in time,
$TV(u_h(\cdot,t))\le C\,TV(u_0)$, gives convergence of a subsequence to a weak solution; the
[Godunov scheme](/methods/godunov-scheme.md) and MUSCL are TVD in the scalar case.

## TVD conditions in incremental form, explicit and implicit

[Puppo et al. (2023)](/sources/puppo-2023.md) (§2) revisit the TVD bounds for
$\partial_tu+a\partial_xu=0$, $a>0$, periodic data, to motivate an implicit
high-order scheme ([Quinpi](/methods/quinpi.md)). Write the limited
second-order update in Harten's incremental form, with page-local coefficients
$\mathsf C_i$:

$$\begin{aligned}
\text{explicit:}\quad u^{n+1}_i&=u^n_i-\mathsf C_{i-1}\big(u^n_i-u^n_{i-1}\big),\\
\text{implicit:}\quad u^{n}_i&=u^{n+1}_i+\mathsf C_{i-1}\big(u^{n+1}_i-u^{n+1}_{i-1}\big),
\end{aligned}\qquad
\mathsf C_{i-1}=\frac{a\Delta t}{\Delta x}\Big[1-\tfrac12\Big(\psi(r_{i-1})-\frac{\psi(r_i)}{r_i}\Big)\Big],$$

with the slope ratio $r_i$ and limited slope $\psi(r_i)(u_{i+1}-u_i)$ of this
page. Then (Puppo et al., §2, citing Harten, Sweby and LeVeque):

- the explicit step is TVD iff $\mathsf C_i\ge0$ and $1-\mathsf C_i\ge0$; the
  first condition gives Sweby's region $0\le\psi(r)/r\le2$, $0\le\psi(r)\le2$, the
  second a CFL condition. Puppo et al. state the "iff" for this one-coefficient upwind
  form; Harten (1983a, Lemma 2.2) prints the two-coefficient incremental form above with
  $C^\pm\ge0$, $C^++C^-\le1$ as a sufficient condition;
- the implicit step is TVD if $\mathsf C_i\ge0$ and $1+\mathsf C_i\ge0$; the first
  condition is the same limiter region and the second always holds, so the
  implicit Euler step with a TVD limiter is TVD for every $\Delta t/\Delta x$;
  the first-order implicit upwind scheme ($\psi\equiv0$) is unconditionally
  TVD by the reverse triangle inequality;
- second-order accuracy needs $\psi(1)=1$ and $\psi$ at least Lipschitz, so
  $\psi$ and $r$ may be computed from any at least first-order approximation of
  $u(x,t^{n+1})$, e.g. a predictor.

In the implicit step the coefficients $\mathsf C_i$ depend on $u^{n+1}$ through
$\psi$ and $r$. Quinpi carries the last item over to its CWENO reconstruction,
whose nonlinear weights it computes from a first-order predictor (§2–§3).

## Limiter formulas

| name | $\psi(r)$ | source |
|---|---|---|
| MinMod | $\max[0,\min(1,r)]$ | Deng, Eq. (4.10) |
| SuperBee | $\max[0,\min(2r,1),\min(2,r)]$ | Deng, Eq. (4.11) |
| van Leer | $(r+\lvert r\rvert)/(1+\lvert r\rvert)$ | Deng, Eq. (4.12) |
| van Albada | $(r^2+r)/(r^2+1)$ | Deng, Eq. (4.13); de Romémont et al. (2026), §3.1 |
| OSPRE | $1.5(r^2+r)/(r^2+r+1)$ | Deng, Eq. (4.14) |
| Deng's shape-preserving limiter | $(2r+4r^2)/(1+2r+3r^2)$ for $r\ge0$, $0$ otherwise | Deng, Eq. (6.2) |
| SuperBee, parametrized | $\max[0,\min(\beta r,1),\min(r,\beta)]$, $\beta=2$ | Nguyen et al., Eq. (28b) |
| OverBee (Chiapolino, Saurel, Nkonga) | $\max\big[0,\min\big[2,2r,\max[\min(2r,\beta),\min\{(2-\beta)r+2(\beta-1),r\}]\big]\big]$, $1\le\beta\le2$ | Nguyen et al., Eq. (28c) |

In the last two rows $\beta$ is the limiter's parameter (page-local, as below).
[Nguyen et al. (2022)](/sources/nguyen-2022.md) print SuperBee in a form that equals Deng's for
$\beta=2$, and van Leer as in the table (Eq. (28a)). *(compiler check, not in the sources: the
OverBee formula gives $\psi(1)=\beta$, so for $\beta>1$ it violates the second-order condition
$\psi(1)=1$ of Puppo et al. above; the $\beta$ used is not printed.)* Nguyen et al. apply OverBee to the volume fractions and van Leer to the other
primitive variables of their multiphase model, in the MUSCL $\kappa_{\mathrm M}$-scheme with $\kappa_{\mathrm M}=1/3$ ([MUSCL](/methods/muscl-hancock.md))
(Eqs. (26)–(27)); OverBee and SuperBee keep a water–air interface about three cells thick, van
Leer lets it grow beyond ten cells at Mach 0.001 with the Rusanov flux (§2.3, §3.1, Figs. 1–4),
and OverBee is retained after the shock–helium-bubble comparison for its better interface
thickness and smoothness (§3.4, Fig. 17). In the source of the OverBee limiter, as reported by
Nguyen et al., it is switched on only by an interface indicator.

**Van Leer's 1979 monotonicity algorithms.** [Van Leer (1979)](/sources/vanleer-1979.md)
(§3.3, Eqs. (101)–(104); App. B, Eq. (B2)) never prints "TVD" or "total variation"; it
speaks of "monotonicity algorithms" acting on slopes that MUSCL **stores independently**
of the cell averages ([MUSCL](/methods/muscl-hancock.md)). With
$\delta^-=\bar u_i-\bar u_{i-1}$, $\delta^+=\bar u_{i+1}-\bar u_i$ and the stored undivided slope
$\Delta_i$ of cell $i$ (page-local), the limiter applied before the Lagrangean step is

$$\Delta^{\mathrm{mono}}_i=\begin{cases}\mathrm{sgn}(\Delta_i)\min\big(2\lvert\delta^-\rvert,\ \lvert\Delta_i\rvert,\ 2\lvert\delta^+\rvert\big),&\mathrm{sgn}\,\delta^-=\mathrm{sgn}\,\delta^+=\mathrm{sgn}\,\Delta_i,\\ 0&\text{otherwise},\end{cases}$$

by three rules: the linear profile must not exceed the neighbouring averages, the slope is
zero at an extremum of the averages, and zero if its sign disagrees with their trend
(Eq. (101), Fig. 3). The factors 2 may be reduced, "however, not beyond $1+O(\Delta Q)$, lest
the scheme lose its second-order accuracy", and may decrease with the local Courant number;
with factors 0 the scheme is Godunov's (§3.3, p. 118). The limiter guarantees positivity of
the distributions but "can not fully guarantee monotonicity" for systems at the largest
time steps (pp. 117–118). The paper adds a remap limiter with factors $2/\varphi$ and
$2/(1-\varphi)$, $\varphi$ the mass fraction of a cell crossing a fixed boundary (Eqs.
(102)–(103); page-local $\varphi$), which keeps only the zone averages positive, and a
"narrow-base" limiter using stored interface values, weaker near a peak (Eq. (104),
Fig. 5); both (101) and (102) "clip real peaks to the same degree as a first-order method
would do" (§3.3). For slopes recomputed from averages on a uniform grid, Appendix B
recalls from the fourth paper of the series the harmonic-mean slope
$2\delta^-\delta^+/(\delta^-+\delta^+)$ when $\delta^-\delta^+>0$, zero otherwise (Eq. (B2)),
"so that the crudest monotonicity condition is automatically accounted for".
*(compiler check, not in the sources: with $r=\delta^-/\delta^+>0$ this is
$\psi(r)\,\delta^+$ with $\psi(r)=2r/(1+r)=(r+\lvert r\rvert)/(1+\lvert r\rvert)$, the "van Leer" row
of the table, which the 1979 paper gives no name; and if the stored slope in (101) is
replaced by the central difference $\tfrac12(\delta^-+\delta^+)$, (101) becomes the
three-argument $\mathrm{MC}_\beta$ limiter below with $\beta=2$, a substitution the paper does
not make.)*

**Minmod in the founding papers.** Harten's second-order TVNI scheme limits a correction of
the flux, not a slope, by what is the two-argument minmod of the neighbouring corrections
([Harten's TVD scheme](/methods/harten-tvd-scheme.md), Eq. (3.11)); the paper does not use
the word. Harten et al. (1987a) define $M(x,y)=s\min(\lvert x\rvert,\lvert y\rvert)$ if
$\mathrm{sgn}\,x=\mathrm{sgn}\,y=s$, zero otherwise (Eq. (3.16)), and apply it to one-sided
derivatives in their deconvolution ENO reconstruction; with $r=2$ their ENO slopes are those
of a second-order TVD scheme and differ from the primitive-function slope only at extrema,
where the deconvolution gives zero (Remark 3.2, Eq. (3.24)). Shu & Osher (1988) (§III,
Remark 3.1(b)) note that the second-order member of their flux ENO family is "similar to the
usual minmod second order TVD scheme", with minmod replaced by "choosing the value closer to
zero", and "is still a TVD method" (derivation omitted).

**Symmetric limiters** satisfy $\psi(r)/r=\psi(1/r)$; they can be written as
slope limiters, $u^\mp=\bar u_i\pm\tfrac12\tilde\psi(1/r_i)\,s_i$ with the central
difference $s_i=\tfrac12(\bar u_{i+1}-\bar u_{i-1})$ (MUSCL–Hancock form; Deng,
Eqs. (4.6)–(4.7), $\tilde\psi$ page-local for the slope-form limiter).

**Two-argument slope limiters.** With $\delta^+=\bar u_{i+1}-\bar u_i$ and
$\delta^-=\bar u_i-\bar u_{i-1}$ (page-local),
[Balsara et al. (2024)](/sources/balsara-2024.md) (App. D, Eqs. (D.9)–(D.10)) use

$$\begin{aligned}
\mathrm{MC}_\beta(\delta^+,\delta^-)&=\tfrac12\big(\mathrm{sgn}\,\delta^++\mathrm{sgn}\,\delta^-\big)\min\big(\lvert\delta^++\delta^-\rvert/2,\ \beta\lvert\delta^+\rvert,\ \beta\lvert\delta^-\rvert\big),\quad1\le\beta\le2,\\
\mathrm{vA}_\varepsilon(\delta^+,\delta^-)&=\frac{\big((\delta^-)^2+\varepsilon\big)\delta^++\big((\delta^+)^2+\varepsilon\big)\delta^-}{(\delta^+)^2+(\delta^-)^2+2\varepsilon},
\end{aligned}$$

($\beta$ and $\varepsilon$ here are the limiter's own parameters, not a
smoothness indicator and not the WENO regularization), and recommend van Albada
for implicit problems because it is continuous in the slopes.
[Kanbar et al. (2022)](/sources/kanbar-2022.md) (§3, Eq. (8)) use the
three-argument form of the MC limiter for the undivided slope,

$$\mathrm{minmod}\Big(\beta(\bar u_i-\bar u_{i-1}),\ \tfrac12(\bar u_{i+1}-\bar u_{i-1}),\ \beta(\bar u_{i+1}-\bar u_i)\Big),\qquad 1<\beta<2,$$

with $\beta=1.5$ in all tests (the source's $\theta$), componentwise on the
conserved deviation $\delta u=u-u_{\mathrm e}$ from a known steady state (and on
$u^n$ and $u_{\mathrm e}$ for the predictor) of their
[unstaggered central scheme](/methods/unstaggered-central-scheme.md); the formula is
written here for $\bar u$.
*(compiler check, not in the sources: this is $\mathrm{MC}_\beta$ above, since
$\tfrac12(\mathrm{sgn}\,\delta^++\mathrm{sgn}\,\delta^-)\min(\cdot)$ equals the
three-argument minmod; the generalized minmod with factor 2 below is the case
$\beta=2$.)* The MFC code offers minmod, MC, OSPRE, SuperBee, Sweby, van Albada
and van Leer as flux limiters ([Bryngelson et al. (2021)](/sources/bryngelson-2021.md),
§4.2.2; no formulas printed).
*(compiler check, not in the sources: with $\varepsilon=0$, $\mathrm{vA}$ is the
undivided slope $\delta^+\psi(r_i)$ of the van Albada limiter of the table, since
$\tfrac12\delta^+\psi(r_i)=\tfrac12\delta^+\delta^-(\delta^++\delta^-)/((\delta^+)^2+(\delta^-)^2)$.)*

The **generalized minmod** limiter with factor 2,

$$(u_x)_i=\mathrm{minmod}\Big(2\frac{\bar u_i-\bar u_{i-1}}{\Delta x},\ \frac{\bar u_{i+1}-\bar u_{i-1}}{2\Delta x},\ 2\frac{\bar u_{i+1}-\bar u_i}{\Delta x}\Big),$$

with $\mathrm{minmod}(z_1,z_2,\dots)=\min_jz_j$ if all $z_j>0$, $\max_jz_j$ if all
$z_j<0$, $0$ otherwise, is the reconstruction of the second-order
central-upwind schemes ([Chertock et al. (2023)](/sources/chertock-2023.md),
§2.1, Eqs. (2.5)–(2.7)). The same minmod function enters the
anti-diffusion correction of the CURH flux
([Wang et al. (2023b)](/sources/wang-2023-b.md), §3, Eq. (5)). [Chu et al. (2025b)](/sources/chu-2025-b.md)
(§2, Eqs. (2.5)–(2.6)) use the same three-argument form with factor $\beta=1.3$ (their $\theta$)
on conservative or equilibrium variables, as Kurganov et al. (2023) do.

**Slopes on stretched and mapped meshes.** [Peng et al. (2022)](/sources/peng-2022.md)
(§2.4, Eqs. (15)–(20)) use minmod-limited MUSCL in a MUSCL–Hancock finite-volume scheme on
curvilinear meshes, dividing the cell differences by physical centroid-to-face distances,
$\delta_i=(\bar u_{i+1}-\bar u_i)/(L^-_{i+1}+L^+_i)$, with $L^+_i$ ($L^-_i$) the distance from the
centroid of cell $i$ to its right (left) face (page-local). *(compiler check, not in the sources:
the printed left-face value, with the MUSCL parameter $\kappa_{\mathrm M}=0$ (the source's $\omega$), is
$\bar u_i-\tfrac12\big(\delta_{i-1}L^-_i+\delta_iL^+_i\big)$, which for linear data
$\delta_{i-1}=\delta_i=b$ gives $\bar u_i-\tfrac12b(L^-_i+L^+_i)$ instead of $\bar u_i-bL^-_i$; the
reconstruction is exact for linear data only where $L^-_i=L^+_i$, whereas the Cartesian form,
Eqs. (15)–(16), is exact. Whether the code does this is not stated.)* See
[MUSCL–Hancock](/methods/muscl-hancock.md).

## Properties read on the normalised-variable diagram

[Deng (2023)](/sources/deng-2023.md) rewrites the flux-limiter form in the
normalised variable $\tilde u_i$ of the
[normalised-variable diagram](/definitions/normalised-variable-diagram.md),
$\tilde u_{i+1/2}=\tilde u_i+\tfrac12\psi\big(\tilde u_i/(1-\tilde u_i)\big)(1-\tilde u_i)$
(Eq. (4.3), using $r_i=\tilde u_i/(1-\tilde u_i)$), and reads:

- MinMod is always dissipative; SuperBee is anti-dissipative for $\tilde u$
  between about 0.3 and 0.8 (§4.1, Fig. 3);
- the symmetric limiters (van Leer, van Albada, OSPRE) are dissipative for
  $\tilde u<1/2$ and anti-dissipative for $\tilde u>1/2$, "not symmetric in terms
  of numerical dissipation errors", which distorts transported shapes; because the
  third-order line does not satisfy the symmetry condition, a symmetric TVD
  limiter cannot be third order (Remark 4.1);
- Deng's new limiter is tangent to the third-order line at $\tilde u=1/2$ and to
  the left TVD boundary $\tilde u_{i+1/2}=2\tilde u_i$ at $0$, lies in the
  dissipative second-order TVD region, gives lower $L_1$ error than the symmetric
  limiters on sine advection (van Leer is slightly better in $L_\infty$; SuperBee
  "loses the accuracy as the grid is refined"), and preserves shapes better than
  van Leer in 2D rotation (§6.1, Figs. 10–12). *(compiler check, not in the sources: inserting
  $\psi$ of Eq. (6.2) with $r=\tilde u/(1-\tilde u)$ into Eq. (4.3) reproduces
  Deng's normalised form $(2\tilde u+\tilde u^3)/(1+2\tilde u^2)$ identically
  (symbolic simplification), with value $3/4$ at $1/2$.)*
- The left TVD boundary has slope 2 (CFL 0.5 for the fully discrete scheme);
  Deng makes its slope a CFL-dependent parameter, and, citing Giuliani and
  Krivodonova, calls CFL $<0.5$ "overly stringent" with high-order SSP
  Runge–Kutta stepping (§4.1, §5).

[Chertock et al. (2023)](/sources/chertock-2023.md) (§2.1) report, after their
ref. [26], a classification of limiters into dissipative, compressive and
overcompressive (compressive ones may create kinks, overcompressive ones jumps),
with minmod "the most compressive out of dissipative limiters".
[Chu et al. (2025a)](/sources/chu-2025.md) (§2.1.1, Eq. (2.6)) give this classification a
one-parameter form through the **SBM limiter** of Lie and Noelle, as they recall it, with
parameters $\beta\in[1,2]$ and $\tau_{\mathrm S}$ (page-local; the source's $\theta$, $\tau$):

$$\psi^{\mathrm{SBM}}(r)=0\ (r<0),\qquad \psi^{\mathrm{SBM}}(r)=\min\{\beta r,\ 1+\tau_{\mathrm S}(r-1)\}\ (0<r\le1),\qquad \psi^{\mathrm{SBM}}(r)=r\,\psi^{\mathrm{SBM}}(1/r)\ (r>1).$$

$\tau_{\mathrm S}\ge0.5$ is dissipative (contacts smeared in time), $0\le\tau_{\mathrm S}<0.5$
compressive (sharp contacts, smooth extrema compressed into kinks), $\tau_{\mathrm S}<0$
overcompressive (very sharp contacts, artificial $O(1)$ jumps in smooth flow); larger $\beta$ is
less dissipative and more oscillatory. With $\beta=2$, $\tau_{\mathrm S}=0.5$ it is the
generalized minmod with factor 2 below ("Minmod2", §2.2). *(compiler check, not in the sources:
for $0<r\le1$ both give $\min\{2r,(1+r)/2\}$, for $r>1$ both $\min\{2,(1+r)/2\}$; the third branch
makes the limiter symmetric, $\psi(r)/r=\psi(1/r)$. For every $\tau_{\mathrm S}$, $\psi(1)=1$; with $\beta=2$,
$\tau_{\mathrm S}=-0.25$ the limiter exceeds SuperBee ($=1$ there) for $1/2<r<1$, where it equals
$\min\{2r,\,1.25-0.25r\}>1$, yet stays inside Sweby's region $\psi\le\min\{2r,2\}$.)* Chu et al. (2025a) switch between the overcompressive setting $\tau_{\mathrm S}=-0.25$ in
cells flagged rough and Minmod2 elsewhere, in characteristic variables
([low-dissipation central-upwind schemes](/methods/low-dissipation-central-upwind-scheme.md)).

## Roles of limiters in high-order schemes

- **Flux-limited WENO.** "The WENO schemes we utilize are, in general, not TVD",
  which can cause instability "even when the usual CFL criteria are met"; MFC
  therefore optionally blends the first-order (piecewise-constant) Riemann flux
  with the WENO Riemann flux, low-order flux plus $\psi(r_i)$ times the
  difference, where $r_i$ is the slope ratio of the volume fraction taken on
  the upwind side of the contact velocity of the Riemann solver
  ([Bryngelson et al. (2021)](/sources/bryngelson-2021.md), §4.2.2, Eq. (34); the
  blend is described in words). The dissipation is so confined to material
  interfaces where WENO "cannot form a smooth stencil". See
  [hybrid central-WENO schemes](/methods/hybrid-weno.md) and [MFC](/software/mfc.md).
- **The sign property.** In the entropy-stable TVD-ES subcell scheme of
  [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) (§4,
  Eqs. (72)–(81)) the minmod reconstruction of the scaled entropy variables
  makes every reconstructed jump have the sign of the cell-mean jump, which is
  what entropy stability needs; citing Fjordholm, Mishra and Tadmor, they state
  that minmod is the only symmetric TVD limiter with this sign property. The
  reconstruction is done in reference space on the non-uniform Gauss–Lobatto
  subcell grid, and the variant without reconstruction in the element-boundary
  subcells gave the best Orszag–Tang results (§6.2, Fig. 6). See
  [TeCNO schemes](/methods/tecno-scheme.md).

- **Variable choice.** Minmod applied to conservative variables "typically leads
  to large oscillations", so Chertock et al. apply it to local characteristic
  variables (§2.1; see [characteristic decomposition](/methods/characteristic-decomposition.md)).
  [Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md) (§4 item (4),
  §5.2.3, Fig. 1b) use minmod-limited second-order reconstruction on primitive
  variables inside the subcell finite-volume scheme of a DG method, because it
  keeps positivity; at element-boundary subcells minmod is not defined and the
  scheme falls back to first order. A TVD minmod reconstruction of scaled
  entropy variables, after Fjordholm, Mishra and Tadmor, gives a higher-order
  entropy-stable finite-volume scheme (§2.2; see
  [subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md)).
- **Base polynomial of multi-resolution WENO.** The third-order multi-resolution
  WENO of Zhu and Shu falls to a first-order base polynomial when smoothness is
  lost, and Balsara et al. found it "less than second order" on "somewhat large"
  meshes; their fix replaces that base by an $\mathrm{MC}_\beta$- or van
  Albada-limited linear polynomial ([Balsara et al. (2024)](/sources/balsara-2024.md),
  §VII.a, App. D, Eqs. (D.7)–(D.8); see [WENO-AO](/methods/weno-ao.md)).
- **Replaced by nonlinear weights on unstructured grids.**
  [Chen et al. (2022)](/sources/chen-2022.md) (§1, §5) state that second-order TVD-based
  limiters "typically loss [sic] their designed accuracy at smooth critical points", that the TVD
  principle cannot guarantee the removal of oscillations on unstructured grids (citing
  Jameson), and that several common limiters cannot strictly guarantee monotonicity (citing the
  MLP-pw paper). They replace the slope limiter of a vertex-based least-squares gradient by
  WENO-type weights, $d_j/(\epsilon+SI_j)^2$ with the linear vertex weights $d_j$ (the source's
  $\gamma_j$) and directional indicators $SI_j=(\partial_x\varphi_j)^2\times$ cell area of the
  vertex gradients ($SI_j$, $\varphi_j$ page-local), and report
  that this converges where the MLP-pw limiter with the Venkatakrishnan function stalls or
  diverges on Mach-5 and Mach-10 cylinder flows, at lower cost (14.84 against 17.92 ms per
  reconstruction, §6.4, Table 2). The critical-point claim rests on one smooth test, the
  isentropic vortex, where the nonlinear weights leave the order at about 2 but raise the error on
  the coarse meshes (Table 1). See
  [unstructured gradient reconstruction](/methods/unstructured-gradient-reconstruction.md) and
  [critical-point accuracy](/properties/critical-point-accuracy.md).
- **Bounds called "TVD-like".** The density bounds
  $\min_k\bar\rho_{(ij,k)}\le\rho_{ij}\le\max_k\bar\rho_{(ij,k)}$ of
  [Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md) (§5.2.2,
  Eq. (47)) are local discrete maximum principles over bar states, not
  total-variation estimates, as their printed form shows (see
  [convex limiting](/methods/convex-limiting.md)).

- **Subcell fallback of a $p$-adaptive DG.** In the FLEXI scheme of
  [Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) (§4.2) troubled elements switch
  whole to a second-order TVD finite-volume scheme on $N_{\mathrm{FV}}^d$ equidistant
  reference-space subcells, with MinMod-limited piecewise-linear reconstruction; the
  subcell count $N_{\mathrm{FV}}=2N+1$ is the largest that does not shrink the explicit time
  step (page-local $N_{\mathrm{FV}}$; see
  [subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md),
  [hp-adaptation](/methods/hp-adaptation.md), [FLEXI](/software/flexi.md)).
- **Limiting a high-order difference operator.** [Abgrall & Nassajian Mojarrad (2024)](/sources/abgrall-2024.md)
  (§3.2.1) limit the upwind differences of their discrete kinetic scheme in the spirit of
  Sweby and of Yee, Warming and Harten: the high-order difference is written as the
  first-order one times $1+\phi_{\mathrm A}(r_{\mathrm A})r_{\mathrm A}/6$, with a page-local
  smoothness ratio $r_{\mathrm A}$ of differences ($r_{\mathrm A}\approx0$ on smooth data) and a
  page-local limiter $\phi_{\mathrm A}$ (the source's $\theta$) equal to 1 on a central interval
  and cut back outside it so that $0\le1+\phi_{\mathrm A}r_{\mathrm A}/6\le M_{\mathrm A}$ (page-local
  bound $M_{\mathrm A}\ge1$, which controls the CFL number). On a radial Sod problem the limited and the
  [MOOD](/methods/mood-a-posteriori-limiting.md)-stabilized fourth-order runs are almost
  identical; the limiter removes the shock overshoot and reduces the undershoot (§5.2.2,
  Figs. 8–9). The authors expect weaknesses because the limiting acts on kinetic variables,
  without any role for the projection onto conservative variables (§3.2.1). See
  [discrete kinetic relaxation schemes](/methods/discrete-kinetic-relaxation-scheme.md).
- **The TVB-corrected minmod of RKDG.** [Zhang & Shu (2010b)](/sources/zhang-2010-b.md)
  (§4.2, Eq. (4.2)) recall the characteristic TVB limiter of RKDG: the modified minmod
  returns its first argument $a_1$ when $\lvert a_1\rvert\le M_{\mathrm{TVB}}\Delta x^2$ and the
  minmod of all arguments otherwise, with one $M_{\mathrm{TVB}}$ per characteristic field
  (page-local, the source's $M_i$); for scalar problems it is related to the second
  derivative of the initial data near smooth extrema. In their positivity-preserving DG for
  Euler the TVB limiter is applied first, and it remains necessary at shocks: without it
  the scheme blows up on the Sedov blast waves even with the positivity limiter. Without the
  positivity limiter the scheme with $M_{\mathrm{TVB}}>0$ may blow up, and the positivity
  limiter lets $M_{\mathrm{TVB}}$ be tuned "in a much larger range", up to $(10^{10},10,10^{10})$
  for the three fields on the [Leblanc tube](/benchmarks/leblanc-shock-tube.md) at 800 cells
  and $(10^{20},100,10^{20})$ at 6400 (§4.2–4.3, Fig. 4.4; see
  [Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md)).
- **A TVB comparator.** The second-order member of the semi-implicit all-Mach schemes of
  [Boscarino et al. (2022)](/sources/boscarino-2022.md) (§3.3, S2T2) uses a second-order TVB
  reconstruction with constant $M_{\mathrm{TVB}}=1$ (page-local, the source's $M$, renamed to
  keep $M$ for the Mach number) in place of fifth-order WENO; it is
  between the WENO scheme and the oscillatory variants on 2D Riemann problems, with poorer
  resolution (Ex. 5.4).
- **A TVD blend of IMEX schemes.** [Allegrini & Vignal (2025)](/sources/allegrini-2025.md)
  recall that implicit Runge–Kutta methods of order above one cannot be SSP without a time-step
  restriction (Gottlieb, Shu and Tadmor, as they cite it) and that the same holds for IMEX
  schemes (their ref. [19]); on their low-Mach shock tube, second order in time with first-order
  space oscillates more as the Mach number decreases (§4, §4.3, Fig. 11). They therefore take the
  convex combination
  $u^{n+1}=(1-\theta_{\mathrm{TVD}})u^{n+1,\mathrm{O1}}+\theta_{\mathrm{TVD}}u^{n+1,\mathrm{O2}}$ of the
  first-order (implicitly upwinded) and second-order updates, with page-local
  $\theta_{\mathrm{TVD}}=\gamma_{\mathrm D}/(1-\gamma_{\mathrm D})$, $\gamma_{\mathrm D}=1-1/\sqrt2$ the
  ARS(2,2,2) parameter, a blending weight "proved in [19] to be the largest possible value to
  ensure the TVD property in the case of an advection equation" (§4.3, Eq. (28)). The "TVD-AP"
  scheme is asymptotically consistent as a convex combination and first order, with a lower error
  than the first-order schemes on the isentropic vortex (Fig. 12). *(compiler check, not in the
  sources: $\theta_{\mathrm{TVD}}=\sqrt2-1\approx0.414$.)* See
  [semi-implicit all-Mach schemes](/methods/semi-implicit-all-mach-scheme.md) and
  [IMEX Runge–Kutta](/methods/imex-runge-kutta.md).
- **A limiter around learned slopes.** In the learned MUSCL scheme of
  [de Romémont et al. (2026)](/sources/deromemont-2026.md) a convolutional network supplies the
  three slope coefficients of each cell, and the van Albada limiter of the table is kept, its ratio
  taken between the learned slopes of cells $i-1$ and $i$ (§4.1–4.2, Eq. (17)); van Albada is chosen
  because it is smooth and differentiable, unlike minmod, which suits training through the
  solver (§3.1). The growth of the discrete total variation over one step enters the training
  loss only as a soft penalty, $\max\big(0,TV(u^{n+1})-TV(u^n)\big)$ (Eqs. (23)–(24)); the authors
  note that a TV bound does not hold in general in several space dimensions or for systems
  (§4.4). See [learned WENO weights](/methods/learned-weno-weights.md).

## The first-order barrier at extrema

The founding sources state the barrier in several forms.
[Shu & Osher (1988)](/sources/shu-1988.md) (§I, p. 3) state that TVD schemes "must
degenerate to first order accuracy at extremacy", although TVD schemes of up to fifteenth
spatial order (17-point stencil) exist away from extrema, and recall that the TVB
modification of Shu's earlier paper "recovers global high order accuracy even at critical
points", and that Sanders' third-order TVD scheme, which measures the variation on a
piecewise-parabolic interpolant, degenerates only to second order at extrema and has no
method-of-lines analogue (pp. 3–6). [Harten et al. (1987a)](/sources/harten-1987.md) (§2,
p. 239) call TVD schemes "necessarily only first-order accurate at local extrema" and drop
"monotonicity limiters" for the [ENO property](/definitions/eno-property.md); they add that
for MUSCL-type schemes the leading error coefficient of the reconstruction is
discontinuous at extrema, which costs one order in the maximum norm there (§1, Remark
1.2). In Harten's own second-order TVNI scheme the order may degenerate locally where
$\partial_xu=0$ (Harten 1983a, §3, Remark 2). [Zhang & Shu (2010b)](/sources/zhang-2010-b.md)
(§1, §4.2) recall the same degeneracy for the minmod limiter of RKDG: their TVB limiter with
parameter $M_{\mathrm{TVB}}=0$ "reduces to a TVD limiter", first order at extrema, with
unsatisfactory results (next section).

[Pazner (2021)](/sources/pazner-2021.md) (§4.4) recalls that TVD schemes are
provably at most first-order accurate at smooth extrema, and observes the
analogous loss for the local maximum principle of Pazner's flux-corrected DG: with
strictly enforced local bounds the $L^1$ convergence rates on $\sin(2\pi x)$
advection are about one (1.00, 1.04, 1.29 for $p=3,4,5$), while relaxing the
bounds to global ones in cells flagged smooth by a modal indicator restores
4.00, 5.00, 5.86 (§5.1, Table 1; $p$ the source's polynomial degree). See
[convex limiting](/methods/convex-limiting.md) and
[critical-point accuracy](/properties/critical-point-accuracy.md).

## Qualifications

- Deng's claim that symmetric TVD limiters cannot reach uniform second order in
  smooth regions is relayed from Tang and Li's accuracy tests (Deng, §1); the
  third-order impossibility is Deng's own (Remark 4.1).
- Abgrall & Nassajian Mojarrad's §3.2.1 is printed with inconsistencies: the
  factor $\tfrac16$ appears twice in one line and is dropped in a later one, and the
  second branch of the limiter reads "$r<-6+\theta$", with the limiter's own symbol as its threshold,
  and a gap is left between the first and third branches. *(Compiler check, not in the
  sources: the printed difference $\tfrac16(f_{i-2}-3f_i+2f_{i+1})$, labelled second minus
  first order, is the third- minus the first-order upwind difference of their §3.1; the
  second- minus first-order one is $\tfrac12f_{i-2}-f_{i-1}+\tfrac12f_i$.)* The page records
  only the structure the printed branches share.
- The TVD left boundary of slope 2 is Sweby's; Deng's reading of it as a free
  CFL-dependent slope $k$ is a reinterpretation, not Sweby's statement.

# Citations

- [Deng (2023)](/sources/deng-2023.md) — §1, §4.1, Eqs. (4.1)–(4.15), Remark 4.1, §6.1, Eqs. (6.1)–(6.2), Figs. 2–3, 10–12.
- [Chertock et al. (2023)](/sources/chertock-2023.md) — §2.1, Eqs. (2.5)–(2.7): generalized minmod, limiter classes.
- [Wang et al. (2023b)](/sources/wang-2023-b.md) — §3, Eq. (5): minmod in the CURH anti-diffusion term.
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §VII.a, App. D, Eqs. (D.7)–(D.10): MC and van Albada base polynomial.
- [Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md) — §2.2, §4, §5.2: minmod subcell reconstruction, TVD-like bounds.
- [Puppo et al. (2023)](/sources/puppo-2023.md) — §2: explicit and implicit incremental-form TVD conditions (arXiv v2).
- [Kanbar et al. (2022)](/sources/kanbar-2022.md) — §3, Eq. (8): three-argument MC limiter, $\beta=1.5$ (arXiv v1).
- [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) — §4.2.2, Eq. (34): flux-limited WENO in MFC (arXiv v1).
- [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) — §4, Eqs. (72)–(81), §6.2: minmod and the sign property (arXiv v1).
- [Pazner (2021)](/sources/pazner-2021.md) — §4.4, §5.1, Table 1: first-order barrier at extrema (arXiv v1).
- [Nguyen et al. (2022)](/sources/nguyen-2022.md) — §2.3, Eqs. (26)–(28), §3.1, §3.4: SuperBee, OverBee and van Leer in a multiphase MUSCL scheme.
- [Peng et al. (2022)](/sources/peng-2022.md) — §2.4, Eqs. (15)–(20): minmod MUSCL on mapped meshes (accepted manuscript).
- [Chen et al. (2022)](/sources/chen-2022.md) — §1, §5, §6.3–6.4, Tables 1–2: limiters versus nonlinear weights on unstructured grids.
- [Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) — §4.2: MinMod TVD subcell finite volumes in FLEXI.
- [Abgrall & Nassajian Mojarrad (2024)](/sources/abgrall-2024.md) — §3.2.1, §5.2.2, Figs. 8–9: flux limitation of kinetic upwind differences.
- [Boscarino et al. (2022)](/sources/boscarino-2022.md) — §3.3, Ex. 5.4: TVB reconstruction in S2T2 (arXiv v2).
- [Chu et al. (2025a)](/sources/chu-2025.md) — §2.1.1–§2.2, Eq. (2.6): SBM limiter, dissipative/compressive/overcompressive settings, Minmod2 (arXiv v1).
- [Chu et al. (2025b)](/sources/chu-2025-b.md) — §2, Eqs. (2.5)–(2.6): generalized minmod with factor 1.3.
- [Allegrini & Vignal (2025)](/sources/allegrini-2025.md) — §4, §4.3, Eq. (28), Figs. 11–12: TVD convex blend of first- and second-order IMEX schemes (HAL author manuscript).
- [de Romémont et al. (2026)](/sources/deromemont-2026.md) — §3.1, §4.1–4.4, Eqs. (13), (17), (23)–(24): van Albada on learned slopes, TV-increase training penalty.
- [Harten (1983a)](/sources/harten-1983.md) — §2 (Eqs. (2.2)–(2.13), Theorem 2.1, Lemma 2.2), §3 (Eq. (3.11), Remark 2): TVNI definition, sufficient incremental condition, minmod-limited correction (NYU report DOE/ER/03077-175, March 1982).
- [Shu & Osher (1988)](/sources/shu-1988.md) — §I (Eqs. (1.5)–(1.7), pp. 3–6), §II, §III (Remark 3.1(b)): TV, TVD and TVB definitions, degeneracy at extrema, TVD Runge–Kutta (ICASE Report 87-33).
- [Harten et al. (1987a)](/sources/harten-1987.md) — §1 (Eqs. (1.19)–(1.21), Remark 1.2), §2 (p. 239), §3 (Eq. (3.16), Remark 3.2, Eq. (3.24)): TVD at first order at extrema, minmod.
- [Van Leer (1979)](/sources/vanleer-1979.md) — §3.3 (Eqs. (101)–(104), Figs. 3–5), App. B (Eq. (B2)): monotonicity algorithms for stored slopes.
- [Zhang & Shu (2010b)](/sources/zhang-2010-b.md) — §1, §4.2–4.3 (Eq. (4.2), Fig. 4.4): TVB-corrected minmod, $M=0$ as TVD.
- [Shu (2009a)](/sources/shu-2009.md) — §3.1: TVD (SSP) Runge–Kutta stability in the total variation seminorm.
