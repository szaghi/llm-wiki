---
type: Method
title: "WENO-JS reconstruction"
description: "The Jiang–Shu weighted ENO reconstruction: a convex combination of r-point candidate polynomials with weights d_k/(β_k+ε)^q, giving order 2r−1 in smooth regions and ENO behaviour at discontinuities; the baseline every later weight design modifies."
status: established
aliases: [WENO-JS, WENO5-JS, classical WENO, Jiang–Shu WENO, WENO3-JS]
tags: [weno, reconstruction, finite-difference, finite-volume]
timestamp: 2026-10-23T10:00:00Z
---

# WENO-JS reconstruction

WENO-JS is the weighted essentially non-oscillatory reconstruction of Jiang and Shu, as recalled
by every WENO source of the bundle. A value at the interface $x_{i+1/2}$ (a numerical flux in
finite differences, a left state $u^-_{i+1/2}$ in finite volumes) is built as a convex combination
of $r$ candidate reconstructions on the $r$-point stencils $S_0,\dots,S_{r-1}$ that cover a
$(2r-1)$-point global stencil:

$$\hat f_{i+1/2}=\sum_{k=0}^{r-1}\omega_k\,\hat f^{(k)}_{i+1/2},\qquad
\omega_k=\frac{\alpha_k}{\sum_{l=0}^{r-1}\alpha_l},\qquad
\alpha_k=\frac{d_k}{(\beta_k+\epsilon)^q}.$$

The linear weights $d_k$ make $\sum_kd_k\hat f^{(k)}_{i+1/2}$ the $(2r-1)$th-order upwind-biased
linear scheme on the global stencil. The [smoothness indicators](/definitions/smoothness-indicator.md)
$\beta_k$ push the weight of a stencil crossed by a discontinuity towards zero, which is the
[ENO property](/definitions/eno-property.md). Classical WENO uses $q=2$ (Fu 2023, §3.1; Ye et al. 2022, §2.2,
"for most WENO schemes"); Li et al. (2022, Eq. (5)) call the exponent the knob that "controls the
magnitude of the numerical dissipation", and Fu (2023, §3.1) contrasts it with TENO's larger $q=6$–$7$.

## Construction

**Finite-difference flux reconstruction.** In the [conservative finite-difference
scheme](/definitions/conservative-finite-difference-scheme.md) the point fluxes, after a
[Lax–Friedrichs splitting](/methods/lax-friedrichs-flux.md) $f=f^++f^-$, are treated as cell
averages of an implicit function, and the WENO procedure reconstructs $\hat f^+_{i+1/2}$ from
$f^+_{i-r+1},\dots,f^+_{i+r-1}$; $\hat f^-_{i+1/2}$ follows "by the symmetric rule" about
$x_{i+1/2}$ (Li et al. 2022, §2; Luo & Wu 2021, §2.1; Takagi et al. 2022, §2.1). For systems the
reconstruction is carried out in local characteristic fields
([characteristic decomposition](/methods/characteristic-decomposition.md)) with Roe-averaged
eigenvectors in Li et al. (2022), Luo & Wu (2021), Fu (2021) and Takagi et al. (2022).

**Candidate fluxes and linear weights.** With $S_k=\{x_{i+k-r+1},\dots,x_{i+k}\}$ ($S_0$ the most
upwind), the fifth-order case ($r=3$) is (Luo & Wu 2021, Eq. (1); Li et al. 2022, Table 2)

$$\begin{aligned}
\hat f^{(0)}_{i+1/2}&=\tfrac13f_{i-2}-\tfrac76f_{i-1}+\tfrac{11}6f_i,\\
\hat f^{(1)}_{i+1/2}&=-\tfrac16f_{i-1}+\tfrac56f_i+\tfrac13f_{i+1},\\
\hat f^{(2)}_{i+1/2}&=\tfrac13f_i+\tfrac56f_{i+1}-\tfrac16f_{i+2},
\end{aligned}\qquad (d_0,d_1,d_2)=\big(\tfrac1{10},\tfrac35,\tfrac3{10}\big),$$

and the linear combination is the fifth-order upwind scheme UD5,
$(2f_{i-2}-13f_{i-1}+47f_i+27f_{i+1}-3f_{i+2})/60$ (Luo & Wu 2021, Eq. (3)). Wan & Xia (2022, Eqs. (2.10)–(2.23))
and Jeong, Yang & Yoon (2022, Eqs. (6)–(9)) restate the same scheme, the former with $\epsilon=10^{-6}$, $q=2$. Li et al. (2022,
Tables 1–2) tabulate the seventh- and ninth-order cases: $d=(1/35,12/35,18/35,4/35)$ for $r=4$
and $d=(1/126,10/63,10/21,20/63,5/126)$ for $r=5$. *(Compiler check, not in the sources: all
candidate coefficients and linear weights for $r=3,4,5$ were recomputed by exact integration of
the candidate polynomials; they agree with Li et al.'s tables except the slip noted under
Qualifications.)*

**Third-order compact form.** On the three-cell stencil $\{I_{i-1},I_i,I_{i+1}\}$ of a finite-volume
scheme, Deng (2023, Eqs. (4.19)–(4.23)), Huang et al. (2026, Eqs. (3.1)–(3.5)) and Bezgin, Schmidt &
Adams (2022, §2, Eqs. (6)–(10), with $\epsilon=10^{-15}$) write WENO3-JS as
a blend of the second-order upwind and central reconstructions,

$$u^-_{i+1/2}=\omega_0\big(\tfrac32\bar u_i-\tfrac12\bar u_{i-1}\big)+\omega_1\big(\tfrac12\bar u_i+\tfrac12\bar u_{i+1}\big),\qquad
(d_0,d_1)=\big(\tfrac13,\tfrac23\big),$$

with $\beta_0=(\bar u_{i-1}-\bar u_i)^2$, $\beta_1=(\bar u_i-\bar u_{i+1})^2$ and $q=2$. The linear
limit is the third-order scheme $-\tfrac16\bar u_{i-1}+\tfrac56\bar u_i+\tfrac13\bar u_{i+1}$. Deng and
Huang et al. state the design conditions: consistency $\sum\omega_k=1$, accuracy $\omega_k-d_k=O(\Delta x^2)$,
and $\omega_k\to0$ iff the stencil contains a discontinuity (Deng; Huang et al.).

**Regularization.** Deng (2023, §1) recalls that Jiang and Shu recommended $\epsilon=10^{-6}$, a
value that "reduces the influence of non-linear weights"; Kuzmin & Vedral (2023, §5) use
$\epsilon=10^{-6}$ and $q=2$ for the Jiang–Shu-type weights of their Hermite candidates. For WENO-Z
weights Borges et al. suggest $\epsilon=10^{-40}$ (as recalled by Deng 2023, §4.3), the value Luo &
Wu (2021) use; Wang & Don (2022) test $10^{-12}$ and $10^{-40}$ ([WENO-Z](/methods/weno-z.md)).
Zheng, Shu & Qiu (2021, Eq. (24)) also use $\epsilon=10^{-6}$ with $q=2$. Fan, Zhang & Qiu (2022, §5, Tables 5.1–5.2)
compare $\epsilon=10^{-15}$ with $\epsilon=\Delta x^2$ (after Aràndiga et al.) in a positivity-preserving
Navier–Stokes scheme: WENO-JS5 is about fifth order with both (4.36 at the finest 1-D pair with
$10^{-15}$, 5.10 with $\Delta x^2$), WENO-JS7 reaches seventh order with
$\Delta x^2$ (7.36 in 1-D at 320 points) and shows "certain order loss" with $10^{-15}$ (6.50 at the finest
pair), and outside the accuracy test the choice makes a "marginal difference".

**Interpolation of point values.** When WENO interpolates a function value at an arbitrary
$x\in[x_{i-1/2},x_{i+1/2}]$ from point values, as in the
[alternative formulation](/methods/alternative-weno.md), the linear weights depend on the position.
Zheng, Shu & Qiu (2021, §2.2.4) combine the three quadratics on
$\{x_{i-2+k},x_{i-1+k},x_{i+k}\}$, $k=0,1,2$, into the quartic on five points with

$$d_0(x)=\frac{(x-x_{i+1})(x-x_{i+2})}{12\Delta x^2},\qquad d_2(x)=\frac{(x-x_{i-2})(x-x_{i-1})}{12\Delta x^2},\qquad d_1=1-d_0-d_2,$$

and Jiang–Shu indicators and weights. *(Compiler check, not in the sources: at $x_{i+1/2}$ these give
$(d_0,d_1,d_2)=(\tfrac1{16},\tfrac58,\tfrac5{16})$, the interpolation weights, distinct from the
reconstruction weights above.)* They apply it to primitive variables in local characteristic fields.

**Multi-dimensional finite volumes.** A finite-volume WENO in several dimensions needs face
quadrature to keep its order. In the MFC code, Bryngelson et al. (2021, §4.1, §5.4, Fig. 5a)
reconstruct first-, third- or fifth-order WENO dimension by dimension at two-point Gauss nodes of each
face: on the 2-D [isentropic vortex](/benchmarks/isentropic-vortex.md) the $L_\infty$ density error
converges at second order with midpoint (second-order) cell averaging and at fifth order with the
fourth-order averaging, "required to achieve 5th-order accuracy associated with the WENO
reconstructions" ([MFC](/software/mfc.md)). Wong et al. (2021, §4.3), citing Sebastian & Shu, state
that finite-difference WENO and WCNS avoid the multi-dimensional reconstruction and are "four times
cheaper in 2D and nine times cheaper in 3D" than finite-volume WENO (relayed; no timing is printed).
On unstructured meshes, Tsoutsanis et al. (2021, Eq. (32)) keep the Jiang–Shu weight form with $q=4$,
$\epsilon=10^{-6}$; their unstructured WENO carries the full order on every directional stencil,
unlike their [CWENO](/methods/cweno.md) (§3.2). Ji, Liang & Fu (2022, §2.3, Eqs. (15)–(16))
use the same equal-order unstructured WENO as comparator, with exponent 4, $\epsilon=10^{-14}$ and
unnormalized linear weights $10^4$ for the central and 1 for the directional stencils, chosen
"empirically", because on unstructured meshes the optimal linear weights of a high-order combination
"may be negative or may not exist". Their WENO5 and WENO6 fail on
[double Mach reflection](/benchmarks/double-mach-reflection.md) without an additional extended-bounds
limiter of Tsoutsanis, where their TENO and CWENO run (§5.8, Figs. 24–25;
[targeted ENO](/methods/targeted-eno.md)).

**Other carriers of the weights.** The Jiang–Shu weight form is reused on objects that are not
candidate fluxes:

- *DG limiting.* The simple WENO limiter combines a DG cell's polynomial with mean-corrected neighbour
  polynomials by $\omega_i\propto d_i/(\epsilon+\beta_i)^2$, $\epsilon=10^{-6}$, $d_0=0.999$, "the
  classical WENO procedure" (Du, Shu & Zhong 2022, Eqs. (3.4)–(3.5);
  [Hermite WENO](/methods/hermite-weno.md), [WENO limiters for DG](/methods/weno-limiter-dg.md)).
- *Second-order gradients.* Chen, Zhang, Liu & Chen (2022, §5, Eq. (26)) weight the vertex gradients
  of an unstructured second-order scheme by $d_a/(\epsilon+\beta_a)^2$, direction by direction, in
  place of a slope limiter ([gradient reconstruction on unstructured meshes](/methods/unstructured-gradient-reconstruction.md)).
- *Entropy-stable dissipation.* Duan & Tang (2022, §4) apply WENO5-JS to the rotated, scaled entropy
  variables, and the jump of the two reconstructions drives the dissipation of a TeCNO-type flux
  ([TeCNO schemes](/methods/tecno-scheme.md)).
- *WCNS interpolation.* Hiejima's WCNS-JS weights point-value interpolants on TENO-type substencils
  with $q=2$, $\epsilon=10^{-40}$ and Deng–Zhang indicators (2022, Eq. (15);
  [WCNS](/methods/weighted-compact-nonlinear-scheme.md)).

**Hamilton–Jacobi form.** Matsushita & Aoki (2021, §3.1) use the third-order Jiang–Peng WENO for the
advective derivatives of a weakly compressible two-phase solver and blend it with first-order
upwinding through a minmod-limited slope ratio ([hybrid schemes](/methods/hybrid-weno.md)).

## Properties and limitations

- **Accuracy at critical points.** WENO-JS loses order where low derivatives vanish
  ([critical-point accuracy](/properties/critical-point-accuracy.md)). On $x^ke^x$ at $x=0$, Li et
  al. (2022, Table 6) measure for WENO5-JS orders 3.04–3.15 at a first-order critical point, 2.00 at
  a second-order one and 3.39–3.72 at a third-order one; WENO7-JS and WENO9-JS also lose several
  orders (Tables 7–8). Fu (2021), Fu (2023), Takagi et al. (2022), Balsara et al. (2024) and Luo &
  Wu (2021) all recall this defect as the motivation for [mapped WENO](/methods/mapped-weno.md) and
  [WENO-Z](/methods/weno-z.md).
- **Scale dependence.** Because $\epsilon$ is absolute, the weights depend on the scale and the
  offset of the data. Deng (2023, Fig. 13) shows WENO-JS3 with $\epsilon=10^{-6}$ varying visibly
  with a scaling factor of the data, and with $\epsilon=10^{-40}$ for factors below $10^{-10}$.
  Wang & Don (2022, App. A, Theorem 2) show that replacing $\epsilon$ by $\epsilon\,\mathsf m^2[f]$,
  with $\mathsf m$ the mean absolute deviation of the stencil data, makes the JS weights affine
  invariant ([affine-invariant WENO](/methods/affine-invariant-weno.md),
  [scale invariance](/properties/scale-invariance.md)).
- **Dissipation.** Luo & Wu (2021, §4) argue that classical weights give the less-smooth stencil
  less than its linear weight, which adds positive nonlinear dissipation, so WENO-JS is always more
  dissipative than its linear scheme UD5 ([numerical dissipation](/definitions/numerical-dissipation.md)).
  Fu (2023, §1) states that for broadband turbulence this excess dissipation can underpredict
  "approximately the upper 3/4 of the resolvable wavenumbers". In the inviscid Taylor–Green vortex
  WENO7-JS dissipates more kinetic energy at $128^3$ than the seventh-order linear upwind scheme at
  $64^3$ (Li et al. 2022, §4.5, Fig. 11). In the normalised-variable plane WENO3-JS lies close to
  the MinMod limiter on $0<\tilde u_i<1$ (Deng 2023, Fig. 5;
  [normalised-variable diagram](/definitions/normalised-variable-diagram.md)).
- **Symmetry.** Fu (2023, §3.8) recalls that WENO9-JS breaks the symmetry of the Rayleigh–Taylor
  instability at $\Delta x=1/1920$ while WENO5-JS keeps it
  ([symmetry preservation](/properties/symmetry-preservation.md)).
- **Measured accuracy.** On $u_t+u_x=0$, $u_0=\sin\pi x$, $t=2$, WENO5-JS has $L_1$ error
  $7.94\times10^{-11}$ at $N_x=640$, against $9.72\times10^{-12}$ for TENO5 (Ye et al. 2022,
  Tables 7–8). On a 1-D Euler density wave at 320 points, WENO-JS5 has $L_1$ error
  $1.93\times10^{-10}$ against $2.93\times10^{-11}$ for the linear Upwind5 scheme, at 1.5809 s against
  0.9217 s (Wang et al. 2021, Table 5.1). In a manufactured-solution test of a 3-D finite-difference
  disturbance solver with characteristic WENO5 on Rusanov-split fluxes, the convective right-hand
  side converges at observed $L_2$ orders of about 5.8–6.0 (Browne et al. 2022, App. A, Table A.1).
  On face reconstruction of $\sin^3(\pi x)$, which has a saddle point, WENO3-JS converges at 2.44 and
  degenerates at the saddle (Bezgin et al. 2022, §3.4–3.5, Figs. 2, 4).
- **Variables at material interfaces.** Reconstructing conserved variables or fluxes across a
  material interface oscillates in pressure and velocity: Zheng, Shu & Qiu (2021, Fig. 6) measure
  $|u-u_0|$, $|p-p_0|$ near $10^{-4}$–$10^{-3}$ for conservative-variable WENO-JS on a moving contact,
  against $10^{-11}$–$10^{-10}$ for their primitive-variable A-WENO, and a spurious interface jump on a
  gas–water Riemann problem (Fig. 11); Tsoutsanis et al. (2021, §4.2) and Bryngelson et al. (2021,
  §4.1) reconstruct primitive variables for the same reason
  ([gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md),
  [five-equation model](/definitions/five-equation-model.md)).
- **Values at fixed points only.** Zheng, Cai, Qiu & Qiu (2022, §1, §2.2) judge WENO-JS unsuitable for
  semi-Lagrangian finite volumes, which need the reconstruction "at any spatial position", and use the
  CWENO-type WENO-ZQ instead ([semi-Lagrangian finite volumes](/methods/semi-lagrangian-finite-volume.md)).
- **As a comparator.** In the entropy-stable moving-mesh schemes of Li, Duan & Tang (2022, §5), WENO-JS
  in the dissipation term resolves less small-scale structure than multi-resolution WENO at slightly
  lower cost ([multi-resolution WENO](/methods/multi-resolution-weno.md)); in Wang et al. (2021,
  Examples 5.6–5.9) it captures less Kelvin–Helmholtz roll-up than the multi-resolution schemes on
  2-D shock problems. In Hiejima's WCNS (2022, §§3.3–3.4) raising the interpolation order from 5 to 11
  with Jiang–Shu weights changes neither the Shu–Osher waves nor the absent slip-line roll-up of double
  Mach reflection, which TENO weighting resolves; the author attributes this to the dissipation of the
  Jiang–Shu weights.
- **Cost and dissipation against TENO.** In Hong, Ye & Ye's timings (2022, Table 4) WENO-JS5 is the
  cheapest of eight schemes and the most dissipative, while the paper states that TENO-M costs about as
  much as classical WENO. *(Compiler check, not in the sources: TENO-M6 takes 100.84/88.64 = 1.14,
  1406.65/1252.31 = 1.12 and 1632.51/1432.34 = 1.14 times the WENO-JS5 time, and TENO-M8 0.997–1.007 times
  the ninth-order WENO time.)*
- **Against a sixth-order RBF scheme.** On $\sin(2\pi x-\sin(2\pi x)/\pi)$, whose critical points degrade
  WENO-JS, Jeong, Yang & Yoon (2022, Table 2) measure $L^\infty$ orders 3.54–4.13 for WENO-JS against 6.01
  for their WENO-G ([RBF-based WENO](/methods/rbf-weno.md)).
- **Order near shocks.** Huang & Zahr (2022, §1), motivating implicit shock tracking, state that
  limiters, WENO and artificial viscosity are first order near shocks, "which translates into a globally
  first-order accurate scheme", and that WENO has "not been demonstrated on unstructured meshes for
  practical problems" ([implicit shock tracking](/methods/implicit-shock-tracking.md)); see
  Qualifications.
- **Not TVD.** Bryngelson et al. (2021, §4.2.2) note that "the WENO schemes we utilize are, in
  general, not TVD", which can cause instability "even when the usual CFL criteria are met", and add
  an optional flux limiter.
- **Inside other operators.** Boscarino, Qiu, Russo & Xiong (2022, §3.3) use fifth-order finite-difference
  WENO, characteristic-wise for the explicit and component-wise for the semi-implicit flux of an all-Mach
  scheme, without printing the weights ([semi-implicit all-Mach schemes](/methods/semi-implicit-all-mach-scheme.md));
  Balsara, Samantaray & Subramanian (2023, §1, §8.7) use the Jiang–Shu and Balsara–Shu finite-volume
  class to prolong the charge density on AMR hierarchies at orders 2–5
  ([divergence-preserving prolongation](/methods/divergence-preserving-prolongation.md)).

## Descendants

The later weight designs keep the candidate stencils and change only $\alpha_k$:
[WENO-Z](/methods/weno-z.md) (global indicator $\tau$), [WENO-Z+](/methods/weno-z-plus.md),
[WENO-ZN](/methods/weno-zn.md), [mapped WENO](/methods/mapped-weno.md),
[WENO-CU6](/methods/weno-cu6.md), [affine-invariant weights](/methods/affine-invariant-weno.md).
Others change the stencil family or the role of the weights: [CWENO](/methods/cweno.md),
[WENO-AO](/methods/weno-ao.md), [Hermite WENO](/methods/hermite-weno.md),
[hybrid schemes](/methods/hybrid-weno.md), [targeted ENO](/methods/targeted-eno.md), and the
[alternative formulation](/methods/alternative-weno.md), which interpolates states rather than
reconstructing fluxes.

## Qualifications

- Huang & Zahr's (2022, §1) statement about unstructured WENO sits beside the unstructured WENO,
  CWENO and TENO runs of Tsoutsanis et al. (2021) and Ji et al. (2022), which include double Mach
  reflection and Kelvin–Helmholtz problems on triangles; Huang & Zahr do not define "practical problems",
  nor the error norm of their "globally first-order".
- **Stencil labelling differs between families.** The Jiang–Shu convention used here numbers
  $S_0$ as the most upwind stencil. TENO papers (Fu 2021, Eq. (29); Takagi et al. 2022, Eq. (7);
  Ye et al. 2022, §3.3) number the central stencil $S_0=\{i-1,i,i+1\}$, the downwind-biased
  $S_1=\{i,i+1,i+2\}$ and the upwind $S_2=\{i-2,i-1,i\}$, so their $(d_0,d_1,d_2)=(6/10,3/10,1/10)$
  is the same scheme.
- Li et al. (2022, Table 2) print the entry $77/20$ in the $r=5$, $k=4$ row; the row sums to 1 only
  with $77/60$, which is the value the candidate polynomial gives (and the mirror of the $k=0$ row
  of the same table).
- Li et al. (2022, Eq. (8)) call the rescaled Legendre basis of Balsara et al. "Hermite
  polynomials"; it has nothing to do with [Hermite WENO](/methods/hermite-weno.md).

# Citations

- [Li et al. (2022)](/sources/li-2022-b.md) — §2, Eqs. (2)–(7); Tables 1–2, 6–8; §4.5, Fig. 11.
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §2.1, Eqs. (1)–(5); §4.
- [Deng (2023)](/sources/deng-2023.md) — §1; §4.3, Eqs. (4.19)–(4.23); Figs. 5, 13.
- [Huang et al. (2026)](/sources/huang-2026.md) — §3.1, Eqs. (3.1)–(3.5).
- [Wang & Don (2022)](/sources/wang-2022-b.md) — App. A, Eqs. (31)–(33), Theorem 2.
- [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) — §5 (Jiang–Shu-type weights, exponent 2, $\epsilon=10^{-6}$).
- [Fu (2021)](/sources/fu-2021.md) — §1; §3.2, Eq. (11).
- [Fu (2023)](/sources/fu-2023.md) — §1; §3.1; §3.8.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §1; §2.2, Eqs. (7)–(10).
- [Ye et al. (2022)](/sources/ye-2022.md) — §2, Eqs. (3)–(5); §2.2; §4.1, Tables 7–8.
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §I.
- [Zheng, Shu & Qiu (2021)](/sources/zheng-2021.md) — §2.2.4, Eqs. (23)–(24); §4, Figs. 6, 11.
- [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) — §4.1; §4.2.2; §5.4, Fig. 5a.
- [Wong et al. (2021)](/sources/wong-2021.md) — §4.3.
- [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) — §3.2, Eq. (32); §4.2.
- [Matsushita & Aoki (2021)](/sources/matsushita-2021.md) — §3.1, Eqs. (26)–(27).
- [Wang et al. (2021)](/sources/wang-2021.md) — §5, Table 5.1.
- [Li, Duan & Tang (2022)](/sources/li-2022-c.md) — §5, Remark 3.2.
- [Zheng, Cai, Qiu & Qiu (2022)](/sources/zheng-2022.md) — §1; §2.2.
- [Bezgin, Schmidt & Adams (2022)](/sources/bezgin-2022.md) — §2, Eqs. (6)–(10); §3.4–3.5, Figs. 2, 4.
- [Browne et al. (2022)](/sources/browne-2022.md) — §2.2; App. A, Table A.1.
- [Chen, Zhang, Liu & Chen (2022)](/sources/chen-2022.md) — §5, Eqs. (25)–(26).
- [Du, Shu & Zhong (2022)](/sources/du-2022.md) — §3.1, Eqs. (3.4)–(3.6).
- [Duan & Tang (2022)](/sources/duan-2022.md) — §4, Eq. (4.1).
- [Hiejima (2022)](/sources/hiejima-2022.md) — §2.5.1, Eq. (15); §§3.3–3.4.
- [Fan, Zhang & Qiu (2022)](/sources/fan-2022.md) — §5, Tables 5.1–5.2.
- [Ji, Liang & Fu (2022)](/sources/ji-2022.md) — §1; §2.3, Eqs. (15)–(16); §5.8, Figs. 24–25.
- [Hong, Ye & Ye (2022)](/sources/hong-2022.md) — §5; §6, Table 4.
- [Jeong, Yang & Yoon (2022)](/sources/jeong-2022.md) — §2.2, Eqs. (8)–(9); §5, Table 2.
- [Huang & Zahr (2022)](/sources/huang-2022.md) — §1.
- [Boscarino et al. (2022)](/sources/boscarino-2022.md) — §3.3.
- [Balsara, Samantaray & Subramanian (2023)](/sources/balsara-2023.md) — §1; §8.7, Table 12.
- [Wan & Xia (2022)](/sources/wan-2022.md) — §2.2, Eqs. (2.10)–(2.23).
