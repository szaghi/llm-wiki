---
type: Method
title: "WENO-JS reconstruction"
description: "The Jiang–Shu weighted ENO reconstruction: a convex combination of r-point candidate polynomials with weights d_k/(β_k+ε)^q, giving order 2r−1 in smooth regions and ENO behaviour at discontinuities; the baseline every later weight design modifies."
status: established
aliases: [WENO-JS, WENO5-JS, classical WENO, Jiang–Shu WENO, WENO3-JS]
tags: [weno, reconstruction, finite-difference, finite-volume]
timestamp: 2026-10-21T12:00:00Z
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
$(2f_{i-2}-13f_{i-1}+47f_i+27f_{i+1}-3f_{i+2})/60$ (Luo & Wu 2021, Eq. (3)). Li et al. (2022,
Tables 1–2) tabulate the seventh- and ninth-order cases: $d=(1/35,12/35,18/35,4/35)$ for $r=4$
and $d=(1/126,10/63,10/21,20/63,5/126)$ for $r=5$. *(Compiler check, not in the sources: all
candidate coefficients and linear weights for $r=3,4,5$ were recomputed by exact integration of
the candidate polynomials; they agree with Li et al.'s tables except the slip noted under
Qualifications.)*

**Third-order compact form.** On the three-cell stencil $\{I_{i-1},I_i,I_{i+1}\}$ of a finite-volume
scheme, Deng (2023, Eqs. (4.19)–(4.23)) and Huang et al. (2026, Eqs. (3.1)–(3.5)) write WENO3-JS as
a blend of the second-order upwind and central reconstructions,

$$u^-_{i+1/2}=\omega_0\big(\tfrac32\bar u_i-\tfrac12\bar u_{i-1}\big)+\omega_1\big(\tfrac12\bar u_i+\tfrac12\bar u_{i+1}\big),\qquad
(d_0,d_1)=\big(\tfrac13,\tfrac23\big),$$

with $\beta_0=(\bar u_{i-1}-\bar u_i)^2$, $\beta_1=(\bar u_i-\bar u_{i+1})^2$ and $q=2$. The linear
limit is the third-order scheme $-\tfrac16\bar u_{i-1}+\tfrac56\bar u_i+\tfrac13\bar u_{i+1}$. Both
papers state the design conditions: consistency $\sum\omega_k=1$, accuracy $\omega_k-d_k=O(\Delta x^2)$,
and $\omega_k\to0$ iff the stencil contains a discontinuity.

**Regularization.** Deng (2023, §1) recalls that Jiang and Shu recommended $\epsilon=10^{-6}$, a
value that "reduces the influence of non-linear weights"; Kuzmin & Vedral (2023, §5) use
$\epsilon=10^{-6}$ and $q=2$ for the Jiang–Shu-type weights of their Hermite candidates. For WENO-Z
weights Borges et al. suggest $\epsilon=10^{-40}$ (as recalled by Deng 2023, §4.3), the value Luo &
Wu (2021) use; Wang & Don (2022) test $10^{-12}$ and $10^{-40}$ ([WENO-Z](/methods/weno-z.md)).

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
  Tables 7–8).

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
