---
type: Method
title: "Incremental-stencil WENO"
description: "Incremental-stencil WENO (WENO-IS, WENO5IS) of Wang, Xiang and Hu combines two two-point and two three-point candidates into the five-point value with linear weights 15/32, 5/32, 5/16, 1/16, using WENO-Z-type weights with the TENO reference indicator; it serves as WCNS interpolation and as a multiphase base scheme."
status: established
aliases: [WENO-IS, WENO5IS, IS-WENO, incremental-stencil WENO interpolation, WCNS-IS interpolation]
tags: [weno, reconstruction, multiphase, interface-capturing]
timestamp: 2026-10-23T11:06:00Z
---

# Incremental-stencil WENO

Incremental-stencil WENO is the fifth-order WENO of Wang, Xiang & Hu, as recalled by Wong, Angel, Barad &
Kiris (2021, §4.3) and by Zhang, Fleischmann, Adami & Adams (2024a, §3.3, App. C): its four candidates
have **incremental widths** as in [TENO](/methods/targeted-eno.md) — two of two points, two of three — and
are combined by a convex WENO combination, not by a cut-off, into the five-point value. Its weights are of
[WENO-Z](/methods/weno-z.md) type with the TENO reference indicator in place of the WENO-Z global
indicator. Wong et al. call the original a finite-volume reconstruction and adapt it to the node-to-midpoint
interpolation of a [WCNS](/methods/weighted-compact-nonlinear-scheme.md); Zhang et al. use the same
formulas, under the name WENO5IS, as the base of a finite-volume multiphase scheme.

## Candidates and linear weights

For the left-biased value at $x_{i+1/2}$, with data $u_j$ (Wong et al. 2021, Eqs. (84)–(90); Zhang et al.
2024a, Eqs. (C.1)–(C.4); stencils numbered as in both sources, not by the registry's upwind convention):

$$\begin{aligned}
S_0=\{x_i,x_{i+1}\}:&\quad u^{(0)}_{i+1/2}=\tfrac12(u_i+u_{i+1}),\\
S_1=\{x_{i-1},x_i\}:&\quad u^{(1)}_{i+1/2}=\tfrac12(-u_{i-1}+3u_i),\\
S_2=\{x_i,x_{i+1},x_{i+2}\}:&\quad u^{(2)}_{i+1/2}=\tfrac18(3u_i+6u_{i+1}-u_{i+2}),\\
S_3=\{x_{i-2},x_{i-1},x_i\}:&\quad u^{(3)}_{i+1/2}=\tfrac18(3u_{i-2}-10u_{i-1}+15u_i),
\end{aligned}$$

second order on $S_0,S_1$, third order on $S_2,S_3$. With
$$d_0=\tfrac{15}{32},\qquad d_1=\tfrac5{32},\qquad d_2=\tfrac5{16},\qquad d_3=\tfrac1{16},$$
$\sum_kd_ku^{(k)}_{i+1/2}=\tfrac1{128}(3u_{i-2}-20u_{i-1}+90u_i+60u_{i+1}-5u_{i+2})$, the fifth-order
interpolant on five points. *(Compiler check, not in the sources: the weighted sum reproduces the five-point
coefficients term by term.)* The right-biased value follows by
mirror symmetry. The coefficients are those of Lagrange interpolation of point values at $x_{i+1/2}$; they are
the same in the two sources.

## Nonlinear weights

Both sources print (Wong et al. 2021, Eqs. (91)–(101); Zhang et al. 2024a, Eqs. (C.7)–(C.11))
$$\omega_k=\frac{\alpha_k}{\sum_{l=0}^3\alpha_l},\qquad
\alpha_k=\begin{cases}d_k\Big(1+\dfrac{\tau^{\mathrm{ref}}_5}{\beta_k+\epsilon}\cdot\dfrac{\tau^{\mathrm{ref}}_5}{\beta_{01}+\epsilon}\Big),&k=0,1,\\
d_k\Big(1+\dfrac{\tau^{\mathrm{ref}}_5}{\beta_k+\epsilon}\Big),&k=2,3,\end{cases}$$
with [smoothness indicators](/definitions/smoothness-indicator.md)

- $\beta_0=(u_i-u_{i+1})^2$, $\beta_1=(u_{i-1}-u_i)^2$ for the two-point stencils;
- Jiang–Shu three-point indicators $\beta_2=\tfrac{13}{12}(u_i-2u_{i+1}+u_{i+2})^2+\tfrac14(3u_i-4u_{i+1}+u_{i+2})^2$,
  $\beta_3=\tfrac{13}{12}(u_{i-2}-2u_{i-1}+u_i)^2+\tfrac14(u_{i-2}-4u_{i-1}+3u_i)^2$;
- an extra indicator on $S_{01}=\{x_{i-1},x_i,x_{i+1}\}$, used only in the weights of the two-point stencils,
  $\beta_{01}=\tfrac{13}{12}(u_{i-1}-2u_i+u_{i+1})^2+\tfrac14(u_{i-1}-u_{i+1})^2$;
- the TENO reference indicator, the third- and fourth-derivative part of the five-point indicator,
  $$\tau^{\mathrm{ref}}_5=\tfrac{13}{12}(u_{i+2}-4u_{i+1}+6u_i-4u_{i-1}+u_{i-2})^2+\tfrac14(u_{i+2}-2u_{i+1}+2u_{i-1}-u_{i-2})^2,$$
  attributed to Fu, Hu & Adams (page-local symbol of the registry §10; it is not the WENO-Z $\tau_5=|\beta_0-\beta_2|$).

The exponent on each ratio is 1. Wong et al. do not print $\epsilon$; Zhang et al. use $\epsilon=10^{-15}$.
The product form for the two-point stencils makes their weights fall away from $d_k$ when either the stencil
itself or the three-point stencil around it is rough.

## Accuracy

Wong et al. (2021, App. B) prove fifth order of the WCNS built on this interpolation for a scalar law with
$f'>0$, away from critical points. The candidates satisfy $u^{(k)}_{i+1/2}=u_{i+1/2}+A_k\Delta x^2+O(\Delta x^3)$
for $k=0,1$ ($A_0=u''/8$, $A_1=-3u''/8$) and $+A_k\Delta x^3+O(\Delta x^4)$ for $k=2,3$ ($A_2=-u'''/16$,
$A_3=-5u'''/16$), the linear combination has error $-\tfrac3{256}u^{(5)}\Delta x^5$ (Eqs. (B.2)–(B.3)), and
fifth order needs $\omega_k-d_k=O(\Delta x^4)$ (Eq. (B.14)). Since every $\beta_k$ leads with $(u')^2\Delta x^2$ and
$\tau^{\mathrm{ref}}_5=(u''')^2\Delta x^6+O(\Delta x^8)$ (Eq. (B.20)), $\tau^{\mathrm{ref}}_5/(\beta_k+\epsilon)=O(\Delta x^4)$ where
$u'\ne0$ (Eq. (B.21)); the last step defers to Borges et al. and Wang et al.
([accuracy at critical points](/properties/critical-point-accuracy.md)). On 2-D volume-fraction advection
the positivity-preserving scheme PP-WCNS-IS reaches $L_2$ orders 4.85–4.97 beyond the first refinement
($1.714\times10^{-13}$ at $256^2$; Table 4).

Zhang et al. (2024a) report no smooth-data convergence test; their observed $L_1$ orders are about one on
discontinuous problems, and they state that in smooth regions the scheme "recovers the finite volume WENO5IS
with HLLC" and that "the overall theoretical accuracy is first-order according to the analysis in" Wong et
al. (§4.4).

## Uses in the sources

- **WCNS interpolation** (Wong et al. 2021, §4). Applied to primitive variables projected on characteristic
  fields of the five-equation model, with HLLC midpoint fluxes and Deng's explicit hybrid cell-midpoint and
  cell-node differencing, plus an interpolation limiter and a flux limiter that make PP-WCNS-IS positivity- and
  boundedness-preserving (details on the [WCNS](/methods/weighted-compact-nonlinear-scheme.md) page;
  [positivity-preserving flux limiter](/methods/positivity-preserving-flux-limiter.md),
  [bound preservation](/properties/bound-preservation.md)). Wong et al. credit the interpolation with the
  robustness of the original reconstruction, "because both can select one of the 2-point stencils when
  discontinuities are closely located" (p. 20, citing Wang et al.), and call the finite-volume WENO-IS
  "computationally more expensive" than the finite-difference WCNS in multi-D (§1).
- **Base scheme of a WENO–THINC hybrid** (Zhang et al. 2024a, §3.3). WENO5IS reconstructs all primitive
  variables of the five-equation model with surface tension and viscosity, and [THINC](/methods/thinc-reconstruction.md)
  replaces the volume fraction and partial densities in interfacial cells
  ([hybrid schemes](/methods/hybrid-weno.md), [five-equation model](/definitions/five-equation-model.md)); the
  Wong et al. interpolation limiter follows. In a Mach 10 shock-induced air-bubble collapse in water at
  $1920\times960$, the fraction of cells in which the positivity/boundedness limiter acts exceeds 1 % with
  WENO-JS5, is much lower with TENO5 and lowest with WENO5IS, never above 0.04 %, for which the authors call
  WENO5IS "the optimal choice" of the three (§4.8, Fig. 16b; [shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)).
  Against the MUSCL-THINC of Garrick et al., the hybrid resolves shocks, rarefactions and small vortices
  better and keeps the symmetry of a Mach 10 [shock–water column](/benchmarks/shock-water-column.md)
  interaction at every resolution, where MUSCL-THINC loses it as the mesh is refined (§4.5–4.7;
  [symmetry preservation](/properties/symmetry-preservation.md)).

## Relation to TENO and to other incremental designs

The incremental candidates are TENO's, but the combination is a WENO one: no candidate is cut off, and the
TENO reference indicator enters WENO-Z-type weights rather than a scale-separated measure with a threshold
([targeted ENO](/methods/targeted-eno.md)). Fu (2023, §2.1) judges that starting TENO from two-point
stencils adds the dissipation of a second-order candidate, "which renders the motivation questionable";
Wong et al. weigh robustness instead (see the TENO page). Luo & Wu (2021, §5) use a different
incremental-stencil scheme, the WENO-IS-I of Zhu & Hu, as a comparator of WENO-Z+M; the bundle has no
formula for it ([WENO-Z+](/methods/weno-z-plus.md)).

## Qualifications

- **Point interpolation applied to cell averages.** Zhang et al. (2024a, §3.1) describe a cell-average
  finite-volume scheme but print the point-value interpolation coefficients above, the same as Wong et al.'s
  finite-difference ones. *(Compiler check, not in the sources: the fifth-order finite-volume reconstruction
  from cell averages is $\tfrac1{60}(2\bar u_{i-2}-13\bar u_{i-1}+47\bar u_i+27\bar u_{i+1}-3\bar u_{i+2})$; applied to
  cell averages, the point-interpolation formula carries the $O(\Delta x^2)$ difference between average and point
  value, so its face value is second-order accurate.)* Zhang et al. claim no fifth order for their scheme.
- Wong et al. (2021) read is the arXiv v1 preprint; $\epsilon$ is not given there.
- The original paper of Wang, Xiang & Hu is not ingested; everything above is as recalled and used by the two
  sources, which agree on every printed formula.

# Citations

- [Wong et al. (2021)](/sources/wong-2021.md) — §1; §4.3, Eqs. (84)–(101); App. B, Eqs. (B.2)–(B.21); §6.1, Table 4 (arXiv v1).
- [Zhang et al. (2024a)](/sources/zhang-2024.md) — §3.1; §3.3, Eq. (49), Algorithm 1; App. C, Eqs. (C.1)–(C.11); §4.4–4.8, Figs. 12–16.
- [Fu (2023)](/sources/fu-2023.md) — §2.1.
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §5.
