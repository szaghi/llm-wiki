---
type: Method
title: "ENO reconstruction (essentially non-oscillatory schemes)"
description: "ENO schemes build, in each cell or at each interface, one interpolating polynomial on an adaptive stencil grown point by point towards the side with the smaller divided difference, so that the stencil avoids discontinuities; the page gives the cell-average (Harten et al.) and point-value flux (Shu–Osher) constructions, their accuracy notions, systems, cost and the WENO successors."
status: established
aliases: [ENO, ENO scheme, essentially non-oscillatory scheme, adaptive-stencil reconstruction, Harten–Engquist–Osher–Chakravarthy ENO, flux ENO, Shu–Osher ENO]
tags: [reconstruction, finite-volume, finite-difference, characteristic, limiting]
timestamp: 2026-10-30T08:44:00Z
---

# ENO reconstruction (essentially non-oscillatory schemes)

An **ENO scheme** replaces the limited slope of a second-order Godunov-type scheme by a piecewise
polynomial of arbitrary degree whose stencil is chosen adaptively: starting from one point, the
interpolation stencil grows one point at a time towards the side on which the next divided
difference is smaller in absolute value, so that, for data with enough smooth points between
discontinuities, the polynomial is built from the smooth side. "ENO stands for essentially
non-oscillatory" ([Harten et al. (1987a)](/sources/harten-1987.md), §7, p. 263): the reconstruction
may create oscillations at the level of the truncation error, but no $O(1)$ Gibbs phenomenon
(§2; the precise statement is on the [ENO property](/definitions/eno-property.md) page). Two
constructions are founding: the **cell-average** reconstruction of Harten et al. (1987a), used in a
finite-volume (Godunov-type) scheme, and the **point-value flux** construction of
[Shu & Osher (1988)](/sources/shu-1988.md), used in a
[conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md). The
weighted ENO schemes of [Liu et al. (1994)](/sources/liu-1994.md) and
[Jiang & Shu (1996)](/sources/jiang-1996.md) replace the single selected stencil by a convex
combination of all candidates ([WENO-JS](/methods/weno-js-reconstruction.md)).

## Abstract scheme (Harten et al. 1987a)

Harten et al. (1987a, §1, Eqs. (1.10), (1.14)) write the scheme for $\partial_tu+\partial_xf(u)=0$ as
three operations per step: **reconstruction** of a piecewise polynomial $R(x;\bar u^n)$ of degree
$r-1$ from the cell averages $\bar u_i$, **solution in the small** (exact or approximate evolution of
$R$ over $\Delta t$), and **cell averaging** back to $\bar u^{n+1}_i$. With a piecewise-constant $R$ this
is Godunov's scheme, and with a piecewise-linear $R$ it is the second-order MUSCL-type extension
(Eqs. (1.11)–(1.12); [Godunov scheme](/methods/godunov-scheme.md),
[MUSCL](/methods/muscl-hancock.md)). The reconstruction must satisfy three requirements (Eq. (1.9)):

1. accuracy, $R(x;\bar u)=u(x)+e(x)\Delta x^r+O(\Delta x^{r+1})$ wherever $u$ is smooth near $x$;
2. conservation, $\frac1{\Delta x}\int_{I_i}R(x;\bar u)\,dx=\bar u_i$;
3. essential non-oscillation, $TV(R(\cdot;\bar u))\le TV(u)+O(\Delta x^r)$.

The authors drop the "monotonicity limiters" of TVD schemes, which they state are necessarily only
first-order accurate at local extrema (§2, p. 239;
[total variation diminishing](/definitions/total-variation-diminishing.md)), and cite their paper II
for the statement that strict non-oscillation (no new extrema) limits accuracy to second order
(§2).

## Adaptive stencil by divided differences

Harten et al. (1987a, §3, Eqs. (3.1)–(3.4)) recall the adaptive-stencil interpolation of Harten: the
degree-$m$ interpolant on $[x_i,x_{i+1}]$ uses $m+1$ nodes that include $x_i$ and $x_{i+1}$, with left
index $s_m(i)$ (page-local), $1-m\le s_m(i)-i\le0$. The divided differences
$w[x_l,\dots,x_{l+k}]$ (page-local, of the interpolated function $w$) behave as
$\frac1{k!}w^{(k)}$ where $w$ is smooth and as $O(\Delta x^{-k+p})$ across a jump in the $p$th
derivative (Eq. (3.3d)), so their absolute value is an asymptotic smoothness measure. The stencil
starts at $s_1(i)=i$ and is extended by

$$s_{k+1}(i)=\begin{cases}s_k(i)-1&\text{if }\big|w[x_{s_k(i)-1},\dots,x_{s_k(i)+k}]\big|<\big|w[x_{s_k(i)},\dots,x_{s_k(i)+k+1}]\big|,\\ s_k(i)&\text{otherwise,}\end{cases}$$

Eq. (3.4b); with the strict inequality a tie extends the stencil to the right. The properties
$\frac{d^k}{dx^k}H_m=\frac{d^k}{dx^k}w+O(\Delta x^{m+1-k})$ and
$TV(H_m(\cdot;w))\le TV(w)+O(\Delta x^{m+1})$ of this interpolant $H_m$ (page-local) are proved in
paper II, not in paper III (Eqs. (3.5a,b)). The selection is binary and hierarchical: there are no
weights and no fixed set of candidate sub-stencils, but the final stencil is one of the $r$ stencils
of $r$ cells that contain the cell ([Shu (2009a)](/sources/shu-2009.md), §2.1, describes classical
ENO as choosing one of the three third-order candidates by divided differences, which guarantees
third order and ENO behaviour as long as one substencil is smooth). The scheme assumes "for $h$
sufficiently small" at least $r+1$ points of smoothness between discontinuities; when
discontinuities interact "there are not enough points to select a stencil of $(r+1)$ points from the
region of smoothness" (Harten et al. 1987a, §2, p. 240).

## Cell-average reconstructions RP and RD

- **Primitive function (RP).** With the primitive $\mathfrak W(x)=\int^xu\,dx$ (page-local; the sources' $W$, renamed to keep the Lorentz factor $W$ free), known exactly at the
  interfaces as partial sums $\mathfrak W(x_{i+1/2})=\sum_{l\le i}\Delta x\,\bar u_l$, the reconstruction is
  $R=\frac{d}{dx}H_r(x;\mathfrak W)$, the stencil chosen by the rule above on the point values of $\mathfrak W$
  (Harten et al. 1987a, Eqs. (3.6)–(3.10)). Conservation is exact and the mesh need not be uniform;
  $\frac{d^l}{dx^l}R=\frac{d^l}{dx^l}u+O(\Delta x^{r-l})$ (Eq. (3.9)). The same primitive-function
  candidates are the building blocks of finite-volume WENO (Liu et al. 1994, §3.2; Shu 2009a, §2.2).
- **Deconvolution (RD).** On a uniform mesh the cell averages are interpolated by $H_m$ with
  $m\ge r-1$; the derivatives at $x_i$ are taken as the minmod of the one-sided values and then
  deconvolved by an upper-triangular matrix built from the Taylor coefficients of the sliding average
  (Eqs. (3.11)–(3.19)). This is the deconvolution of cell averages recorded on the
  [cell-average to point-value conversion](/operators/cell-average-point-value-conversion.md) page.
  With $r=2$ both RP and RD reproduce the slope of a second-order TVD scheme, RD giving zero slope at
  extrema (Remark 3.2).

**Accuracy notion.** Where the error coefficient $e(x)$ fails to be Lipschitz, at points where the
stencil changes orientation, the local error is only $O(\Delta x^r)$ and the pointwise error
$O(\Delta x^{r-1})$; Harten et al. (1987a, Remark 1.2, Remarks 3.1–3.2) call such schemes
"$r$th order accurate" in quotation marks ($L_1$ order $r$, maximum-norm order $r-1$). RP with $m=r$
and RD with $m=r-1$ are of this kind; RD with $m=r$ gives a Lipschitz $e(x)$ and pointwise order $r$.
On Burgers' equation (Tables IA–IB, $t=0.3$, CFL 0.6) the printed $L_1$ rates at $J=64\to128$ cells are
0.99, 1.83, 2.56, 3.53, 4.62 (RP) and 0.99, 2.18, 3.35, 4.53, 5.53 (RD) for $r=1,\dots,5$
([Burgers tests](/benchmarks/burgers-equation-tests.md)). Irregular random grids lose the extra order:
the error is $O(\Delta x^{r-1})$ (§7 C3).

## Evolution: Cauchy–Kowalewski flux and method of lines

Harten et al. (1987a, §4, Eqs. (4.11)–(4.14)) do not solve the generalized Riemann problem exactly:
each side's polynomial is extended to a local space–time Taylor series whose time derivatives come
from repeated differentiation of the PDE (a [Cauchy–Kowalewski procedure](/methods/cauchy-kowalewski-procedure.md), the predictor idea that
[ADER schemes](/methods/ader-scheme.md) also use), and the interface flux is a Gaussian-type
quadrature in time of a Riemann flux evaluated on the two expansions. They argue that the Riemann
solver acts only as a "pointer" to the side whose expansion is valid, so the exact flux can be
replaced by Roe's without loss of order (§4, pp. 252–253; [Roe solver](/methods/roe-riemann-solver.md)),
and that for $r>1$ the Cauchy–Kowalewski step is "in general, more important than the Riemann
solver" (§7 A2, p. 274). A semi-discrete Runge–Kutta form, Eq. (7.18), is mentioned as easier to
program but less efficient (§7 C2).

Shu & Osher (1988, §I–II) replace the Lax–Wendroff/Cauchy–Kowalewski time discretization by the
method of lines with TVD Runge–Kutta steppers ([SSP Runge–Kutta](/methods/ssp-runge-kutta.md)), on the
grounds that the former is complicated in several dimensions and with forcing terms, and that
linear stability analysis "does not apply to ENO schemes at all" because the stencil is not fixed
(§I(1), p. 5).

## Point-value flux ENO (Shu & Osher 1988)

Shu & Osher (1988, §III, Eqs. (3.1)–(3.15)) build the numerical flux $\hat f_{i+1/2}$ of the
conservative finite-difference scheme directly from point values. The flux is split by global
Lax–Friedrichs, $f^\pm=\tfrac12(f\pm au)$ with a constant $a\ge\max|f'(u)|$
([Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md)); each part is interpolated by a polynomial $p^\pm$ (page-local, as on the
[alternative WENO](/methods/alternative-weno.md) page) of degree $2m$ (page-local $m$) on $2m+1$ points chosen by the divided-difference rule in Newton form,
starting from $x_i$ for $f^+$ and from $x_{i+1}$ for $f^-$ (a tie extends the stencil to the left,
Eqs. (3.12)–(3.13)); and the flux is the interpolant at $x_{i+1/2}$ plus the even-derivative
corrections $a_2\Delta x^2\partial_x^2p^\pm+a_4\Delta x^4\partial_x^4p^\pm+\dots$ of the same polynomial with $a_2=-\tfrac1{24}$,
$a_4=\tfrac7{5760}$ (page-local $a_{2k}$, Eqs. (3.5), (3.9)), giving order $2m$. The same expansion
underlies [alternative WENO](/methods/alternative-weno.md). Remarks 3.1: the first member of the family
is the Lax–Friedrichs scheme, the second is "similar to" the minmod TVD scheme, and for linear
equations the scheme coincides with the primitive-function ENO of Harten et al. apart from the
stencil choice (divided differences of $f^\pm(u)$ instead of cell averages of $u$). The report
version read constructs only even orders $2m$, while its tests run third- and fifth-order members
whose construction is not printed (Shu & Osher 1988, §IV; see the Source page).

- **Building block.** Any monotone or E-flux can replace the Lax–Friedrichs splitting through flux
  increments (Eqs. (3.20)–(3.21)), but most E-fluxes are not smooth at sonic points and ENO schemes
  built on them "will lose accuracy at sonic points"; Lax–Friedrichs is $C^\infty$, and higher-order
  ENO with it is only "slightly inferior" to upwind building blocks (pp. 20–22).
- **TVB cap.** Limiting the divided differences, $\tilde c^{(n)}=\min(|c^{(n)}|,M^{(n)})\,\mathrm{sign}(c^{(n)})$
  (Eq. (3.16)), makes the flux a second-order TVD flux plus $O(\Delta x^2)$, hence TVB; numerically
  the cap makes "no essential difference", and the authors "strongly believe" the uncapped scheme is
  TVB "for most practical problems" (pp. 18–19).
- **Accuracy.** On 1D Burgers at $t=0.3$, 3-3-LF-ENO and 4-4-LF-ENO reach $L_1$ orders 3.13 and 4.76
  at $\Delta x=1/40$ (Table 1); errors farther than $0.1$ from the shock after it forms are of the same
  size as in the smooth case (Table 2).

## Systems

Both founding papers reconstruct systems in characteristic variables
([characteristic decomposition](/methods/characteristic-decomposition.md)). Harten et al. (1987a, §5,
Eq. (5.8)) project the averages with the left eigenvectors of the **cell** state $\bar u_i$ of the cell
being reconstructed and project back with its right eigenvectors; Shu & Osher (1988, pp. 22–23) use
the eigenvectors of $A(u_i)$ at the **node** and a constant splitting matrix frozen at one state.
Harten et al. motivate it by Riemann data (Eq. (5.6)): component-wise reconstruction can oscillate
where discontinuities of different fields are closer than $r+1$ points, and on the Lax problem it is
"much noisier" than the characteristic version (§7 B1, Figs. 12, 15;
[Sod and Lax tubes](/benchmarks/sod-and-lax-shock-tubes.md)). For the Woodward–Colella blast waves
they add a local positivity check that lowers the reconstruction order wherever the sum of the
scaled derivatives $\big|\partial^k_x\cdot\big|\frac{(\Delta x/2)^k}{k!}$, $k=1,\dots,r-1$, of the reconstructed pressure
(or density) in a cell reaches $0.8$ times its cell value, Eq. (7.13b); in the blast-wave run the order was reduced during two time steps before the interaction, in the interaction zone only, and in none of the Riemann problems (§7 B2, p. 285)
([Woodward–Colella blast waves](/benchmarks/woodward-colella-blast-wave.md),
[bound preservation](/properties/bound-preservation.md)). In their experiments the schemes were
stable at CFL 1 (§7, p. 264), and converged to the entropy solution of nonconvex scalar Riemann
problems with a crude entropy fix of Roe's flux
([nonconvex scalar Riemann problems](/benchmarks/nonconvex-scalar-riemann-problem.md)).

## From ENO to WENO

The weighted schemes keep ENO's candidate polynomials and replace the selection by weights.

- **Motivation.** Liu et al. (1994, §1) expect a smoother dependence on the data, which "may help in
  obtaining a convergence proof", and one order more accuracy from the convex combination. They
  recall that standard ENO "experienced an (easily fixed) loss of accuracy" on $\sin^4(\pi x)$ data
  and report "No such degeneracy" for WENO (p. 207, Table II).
- **Cost.** Liu et al. (1994, Remark 2) state that WENO is "a little more expensive" than ENO of the
  same order on sequential computers and "much less expensive" on parallel ones, because ENO's
  stencil choice moves more data. Jiang & Shu (1996, §7, Table 6) time both in one code: on a CRAY
  C-90 vector machine, 1D CPU times are 16.67 s for ENO-LF-4 against 7.44 s and 7.45 s for WENO-LF-4
  and WENO-LF-5. The two statements concern different machines and codes.
- **Two-dimensional problems.** In Jiang & Shu (1996, §8.3 Ex. 4) unmodified ENO-LF-4/5 lose accuracy
  on the two-dimensional shock–entropy wave, while WENO "work[s] nicely without any modification".
- **Naming.** Jiang & Shu (1996, §3) count the order "in $L^1$ sense", so their ENO-RF-4 is the
  ENO-RF-3 of Shu & Osher.

Later ENO-type selections in the bundle keep the binary choice but change what is chosen:
[targeted ENO](/methods/targeted-eno.md) (keep or drop each candidate with its linear weight),
[converged ENO](/methods/converged-eno.md), [AENO](/methods/aeno-reconstruction.md) and
[WLS-ENO](/methods/wls-eno.md).

## Qualifications

- *Version read.* Shu & Osher (1988) were read in the ICASE report version (Report 87-33, May 1987);
  equation numbers are those of the report.
- *Printed slips* of the founding papers (the RD back-substitution coefficient, table entries of
  Harten et al.; the odd-order gap and Table 1 exponent of Shu & Osher) are listed on their Source
  pages.

# Citations

- [Harten et al. (1987a)](/sources/harten-1987.md) — §1, Eqs. (1.9)–(1.14), Remark 1.2; §2, pp. 239–240; §3, Eqs. (3.1)–(3.19), Remarks 3.1–3.2; §4, Eqs. (4.11)–(4.14), (4.21); §5, Eq. (5.8); §7, Tables IA–IB, Eq. (7.13), pp. 263–274, 297.
- [Shu & Osher (1988)](/sources/shu-1988.md) — §I(1); §III, Eqs. (3.1)–(3.21), Remark 3.1; pp. 18–23; §IV, Tables 1–2.
- [Liu et al. (1994)](/sources/liu-1994.md) — §1; §3.2; Remark 2; p. 207, Table II.
- [Jiang & Shu (1996)](/sources/jiang-1996.md) — §3; §7, Table 6; §8.3 Ex. 4.
- [Shu (2009a)](/sources/shu-2009.md) — §2.1, p. 86; §2.2.
