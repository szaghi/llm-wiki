---
type: Property
title: "Symmetry preservation"
description: "Symmetry preservation has four meanings in the sources: the mirror symmetry of a symmetric flow, which low-dissipation schemes lose unless implemented consistently; the skew-symmetry of the convective operator, which yields kinetic-energy conservation; mirror-symmetric WENO smoothness indicators; and the identical discrete form of the two volume-fraction updates of a two-phase scheme."
status: established
aliases: [mirror symmetry preservation, symmetry breaking, symmetry-preserving discretization, skew-symmetry]
tags: [low-dissipation, teno, weno, kinetic-energy-preserving]
timestamp: 2026-10-24T05:59:00Z
---

# Symmetry preservation

The term covers four distinct properties, which a page or claim must keep apart.

1. **Solution (mirror) symmetry.** A problem whose data are symmetric under a
   reflection, such as the single-mode Rayleigh–Taylor instability or the 2D
   Riemann problem configuration 3, has a symmetric exact solution; a scheme
   preserves symmetry if its discrete solution stays symmetric to round-off.
2. **Operator (skew-)symmetry.** A *symmetry-preserving discretization* in the
   sense of Verstappen and Veldman (as recalled by
   [Coppola & Veldman (2023)](/sources/coppola-2023.md)) keeps the algebraic
   symmetry of the continuous convective operator: discrete convection is
   skew-symmetric, which makes quadratic invariants such as kinetic energy
   discretely conserved.
3. **Symmetric smoothness indicators.** In the sense of
   [Zhong et al. (2023)](/sources/zhong-2023.md), the
   [smoothness indicators](/definitions/smoothness-indicator.md) of a
   fifth-order WENO are symmetry-preserving if $\beta_{2-k}$ is the mirror
   image of $\beta_k$ about the centre cell (section 3 below).
4. **Symmetry of the volume fractions.** In the sense of
   [Yan, Abgrall & Wu (2024)](/sources/yan-2024.md), a discretization of a
   two-phase model with $\phi_1+\phi_2=1$ keeps this symmetry if the
   discrete update of $\phi_2=1-\phi_1$ has exactly the same form as that of
   $\phi_1$ (section 4 below).

## 1. Mirror symmetry of the solution

**The observation.** Low-dissipation schemes break the symmetry of the
Rayleigh–Taylor solution where more dissipative ones keep it. TENO-AA loses it
at $64\times256$, $t=1.95$ ([Fu (2021)](/sources/fu-2021.md), §5.5.2, Fig. 9),
and Fu cites similar asymmetries for WENO-SYMBO, WENO-CU6 and WENO9. [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) (§4.7, Fig. 11)
report the loss on Rayleigh–Taylor at $96\times384$, $t=1.95$, for TENO5, TENO5-A and their
scale-sensor variant ([adaptive TENO](/methods/adaptive-teno.md)). As recalled
by [Fu (2023)](/sources/fu-2023.md) (§3.8), WENO9-JS breaks it at $\Delta x=1/1920$ while
WENO5-JS keeps it, and TENO5 breaks it on a coarse grid where WENO5-JS keeps it.

**The explanations recorded.**

- *Round-off unmasked by low dissipation*: [Fu (2021)](/sources/fu-2021.md)
  (§5.5.2) attributes the asymmetry to machine round-off that low dissipation no
  longer hides, and cites Fleischmann et al. for a cure by careful floating-point
  implementation.
  Huang, Liang & Fu (2023, §4.7) give the same explanation for their TENO runs,
  citing two earlier works, and [Liang et al. (2022)](/sources/liang-2022.md) (§4) state
  that their scheme, TENO-THINC and TENO5, all very low-dissipation, "may cause the
  so-called symmetry breaking issue ... due to machine round-off errors".
  [Hong, Ye & Ye (2022)](/sources/hong-2022.md) (§5.5) raise the regularization to
  $\epsilon=10^{-4}$ in their TENO Rayleigh–Taylor runs "to alleviate" it, following Fu et
  al. (2018).
- *Unstable forms of the smoothness indicators*: Don et al. attribute it to
  round-off in unstable forms of the low-order smoothness indicators and propose
  a compact form (as recalled by Fu 2023, §3.8; see
  [smoothness indicators](/definitions/smoothness-indicator.md)).
- *Floating-point inconsistency, not dissipation*: Fleischmann et al. find "no
  causality" between low dissipation and symmetry breaking; removing
  floating-point inconsistencies of the implementation (for example a
  directional dependence), which grow exponentially,
  keeps the TENO5 solution symmetric to machine precision; the same was done for
  BVD schemes (as recalled by Fu 2023, §3.8). The review sides with this view.
- *The mesh itself*: on unstructured meshes the discrete problem is not
  symmetric in the first place. [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md)
  (§4.6, Figs. 16–17) report that their fifth-order unstructured
  [CWENO](/methods/cweno.md) solution of the 2D air–helium
  [shock–bubble interaction](/benchmarks/shock-bubble-interaction.md) loses its
  symmetry at late times on the medium ($D_b/120$) and fine ($D_b/400$) mixed
  meshes, "indicative of multi-dimensional reconstruction nature of the
  framework employed and of the arbitrary unstructured elements in the refined
  shock-bubble interaction zone" ($D_b$ the bubble diameter). The time-averaged
  interface velocities still agree with the experiment within its uncertainty
  (Table 2).

  A counter-example on unstructured meshes: [Ji, Liang & Fu (2022)](/sources/ji-2022.md)
  (§5.4, Figs. 6–7) run the Sod and Lax shock tubes on 1967 uniform triangles with
  finite-volume TENO and report that the one-dimensional symmetry is "well" preserved; the
  evidence is visual, as for the other cases.

- *Spurious post-shock oscillations of the shock-capturing term*:
  [Sousa & Scalo (2022)](/sources/sousa-2022.md) (§5.3, Fig. 11) run a Mach 5 shock
  reflecting off a sinusoidal wall with $\gamma=1.15$ on a sixth-order compact central scheme.
  With the local artificial diffusivity (LAD) of Cook and Kawai–Lele they observe "a high
  level of spurious oscillations" and "an early symmetry breaking behavior"; with their
  [quasi-spectral viscosity](/methods/quasi-spectral-viscosity.md) the run "preserve[s]
  symmetry". No mechanism is proposed; the authors relate the oscillations to similar
  post-shock oscillations reported by Lodato et al. (2017). Here the symmetry loss comes with
  the oscillations of one explicit [artificial viscosity](/methods/artificial-viscosity.md),
  not with low dissipation as such.

**Not every asymmetry is numerical.** In the strong shock–strong vortex interaction
([shock–vortex interaction](/benchmarks/shock-vortex-interaction.md)), Sousa & Scalo, following
Rault et al. (2003) and Tonicello et al. (2020), describe the physical outcome as "a symmetry
breaking event": the vortex splits into two co-rotating vortices, the bottom one trailing the
top one; both QSV and LAD miss the asymmetric splitting on the coarsest grid ($192\times96$) and
converge to it on finer grids (§5.2, Fig. 6). A symmetric numerical result is therefore the
wrong answer for such a flow.

A further low-dissipation case: [Li et al. (2023b)](/sources/li-2023-b.md)
(§4.5, Fig. 21) find their ADADF-HY density field of the Rayleigh–Taylor
instability ($120\times480$, $t=1.95$) slightly asymmetric while the more
dissipative WENO-Z stays symmetric. They attribute this to low dissipation
that does not damp round-off and truncation disturbances, as Fu (2021)
does. Zhong et al. (2023) (§4.4, Fig. 13) report that their IMWENO-P,
despite its symmetric smoothness indicators, "still shows a
symmetry-broken phenomenon" on Rayleigh–Taylor at $240\times960$, and cite
Don et al. for the issue.

**The remedy in practice.** [Takagi et al. (2022)](/sources/takagi-2022.md)
(§4) use the Fleischmann et al. technique in all runs and report preserved
symmetry for TENO-THINC on Rayleigh–Taylor
($64\times256$, $128\times512$) and on Riemann configurations 3 and 12
($1024^2$); they also write the THINC flux with $\mathrm{sgn}(\varsigma)$ and
$\lvert\varsigma\rvert$ rather than in the form of Deng et al. (2019), a
difference they relate to symmetry breaking from floating-point errors (§2.3;
see [THINC](/methods/thinc-reconstruction.md)). [Liang et al. (2022)](/sources/liang-2022.md)
(§4, §§4.9–4.10, Figs. 21–23) apply the same technique, together with the BVD-based
symmetry-preserving enforcement of Wakimura, Takagi and Xiao, and report "rigorous flow symmetry"
for their improved [TENO-THINC](/methods/teno-thinc.md) scheme on the implosion problem
($800^2$, $t=0.8$) and on Rayleigh–Taylor. Symmetry is also reported kept
by ROUND and LD-ROUND on Riemann configuration 3 at $600\times600$
([Huang et al. (2026)](/sources/huang-2026.md), §6.6) and, as "more symmetric"
than WENO-IS-I and WENO-Z9, by WENO-Z+M on the same configuration at $401^2$
([Luo & Wu (2021)](/sources/luo-2021-b.md), §5.3.2).

[Liang & Fu (2024a)](/sources/liang-2024.md) (§4) state that the very low dissipation
of their Gaussian-RBF TENO and of TENO5 can break flow symmetry through round-off and
deploy the Fleischmann et al. technique; [Zhang et al. (2024b)](/sources/zhang-2024-b.md)
(§6.3.2) attribute the symmetry breaking of low-dissipation TENO in the 2D Riemann problem
to floating-point truncation, citing earlier work.

**Two-phase flows.** Two sources carry the floating-point remedy to diffuse-interface
multiphase schemes ([five- and six-equation models](/definitions/five-equation-model.md)):

- [Zhang et al. (2024a)](/sources/zhang-2024.md) (§3.3, Eq. (44)) note that the mirror
  relation between the THINC face values for increasing and decreasing volume fraction
  holds in exact arithmetic but not in floating point, because $e^x=1/e^{-x}$ is not exact,
  so earlier THINC implementations can break symmetry (as noted by Takagi et al.). They
  obtain the values of one orientation by mirror flipping those of the other, so the
  gradient sign never enters the jump centre ([THINC](/methods/thinc-reconstruction.md)).
  On a Mach 10 shocked water column at $480\times320$, $960\times640$ and
  $1920\times1280$, the MUSCL-THINC of Garrick et al. loses symmetry more as the grid is
  refined, while their WENO5IS-THINC "perfectly preserves the symmetry at different
  resolutions"; the head-on droplet collision also stays symmetric (§4.7, Fig. 13; §4.12;
  [shock–water-column interaction](/benchmarks/shock-water-column.md)).
- [Wakimura et al. (2024)](/sources/wakimura-2024.md) (Appendix A) list the rules for a
  BVD scheme with HLLC fluctuations on a symmetric mesh: symmetrize asymmetric initial data
  by averaging at mirror points; use the symmetric THINC closed form, since non-polynomial
  functions break exact identities in floating point ($\ln a\ne-\ln(1/a)$); add the total
  fluctuation of the cell last; and in the HLLC fluctuations add the $v_1-c$ and $v_1+c$
  waves before the contact wave, in every direction. They show no symmetry-error
  measurement.

## 2. Skew-symmetry of the discrete convective operator

For the transport model $\partial_t\rho+\nabla\cdot(\rho v)=0$,
$\partial_t(\rho\phi)+\nabla\cdot(\rho v\phi)=0$ (page-local transported quantity $\phi$, with $\phi=v$ for momentum),
[Coppola & Veldman (2023)](/sources/coppola-2023.md) (§5.1, Eqs. (59)–(60)) prove
that the discrete scheme conserves the quadratic invariant
$\tfrac12\rho\phi^2$ globally iff the discrete operator
$A_{\mathrm{kin}}=C_{\mathrm{mom}}-\tfrac12\mathrm{diag}(d_{\mathrm{mass}})$ is
skew-symmetric (page-local matrix names: $C_{\mathrm{mom}}$ the discrete momentum
convection, $d_{\mathrm{mass}}$ the discrete mass transport), and that
skew-symmetry also yields local conservation with an explicit flux
(Corollary A.4). Skew-symmetry is the operator symmetry of the continuous
kinetic-energy operator; split convective forms achieve it through duality
relations between their derivative operators, such as $D^\rho=-(D^v)^\top$, plus
weight conditions, without requiring each derivative operator to be
skew-symmetric (§3.3, Eq. (43); §5.3, Eqs. (58), (72)), and a fourth-order flux obtained by Richardson
extrapolation generalizes the Verstappen–Veldman construction from incompressible
to compressible flow (§6). These results are developed on
[kinetic energy preservation](/properties/kinetic-energy-preservation.md) and
[split convective forms](/methods/split-convective-forms.md).

## 3. Mirror-symmetric smoothness indicators

Write each Jiang–Shu indicator of fifth-order WENO as a weighted sum of
squared linear combinations of cell averages on its stencil $S_k$,
$k=0,1,2$, the first combination a first-difference term and the second a
second-difference term. Zhong et al. (2023) (§3.1, Eqs. (19)–(20), Table 1,
Fig. 1) call the indicators **symmetry-preserving** when, for both terms
$m=1,2$ and $n=0,1,2$, the coefficient of $\bar u_{i-n}$ in term $m$ of
$\beta_k$ equals $(-1)^{km}$ times the coefficient of $\bar u_{i+n}$ in term
$m$ of $\beta_{2-k}$. The condition concerns the coefficients inside each
squared term, not the prefactors. *(Compiler check, not in the sources:
since the terms are squared, the condition states that the reflection
$\bar u_{i+n}\leftrightarrow\bar u_{i-n}$ maps $\beta_0$ to $\beta_2$ and
$\beta_1$ to itself.)* The Jiang–Shu indicators of WENO-JS, WENO-Z and
WENO-M satisfy it, and so do those of WENO-ZS and WENO-η. The
$L^1$-norm-type indicators of WENO-NS, WENO-P and MWENO-P do not (§3.2).
*(Compiler check, not in the sources: their one-sided first differences
are $\bar u_{i-2}-3\bar u_{i-1}+2\bar u_i$ on $S_0$ and
$\bar u_{i+1}-\bar u_i$ on $S_2$, not mirror images.)*

Zhong et al. build symmetric indicators from the same building blocks,
with the weight of the first-difference term fixed at the mesh width
$\Delta x$:

$$\begin{aligned}
\beta_0&=4\Delta x\,(\bar u_{i-2}-3\bar u_{i-1}+2\bar u_i)^2+(\bar u_{i-2}-2\bar u_{i-1}+\bar u_i)^2,\\
\beta_1&=\Delta x\,(\bar u_{i-1}-\bar u_{i+1})^2+(\bar u_{i-1}-2\bar u_i+\bar u_{i+1})^2,\\
\beta_2&=4\Delta x\,(2\bar u_i-3\bar u_{i+1}+\bar u_{i+2})^2+(\bar u_i-2\bar u_{i+1}+\bar u_{i+2})^2
\end{aligned}$$

(Eqs. (21)–(22); Lemma 1, proof omitted as "straightforward"). Their
global indicator is the square of the fourth undivided difference,
$(\Delta^4\bar u_i)^2=(\bar u_{i-2}-4\bar u_{i-1}+6\bar u_i-4\bar u_{i+1}+\bar u_{i+2})^2$,
itself symmetric (Eqs. (23)–(25)), in WENO-Z-type weights
$\alpha_k=d_k\big(1+((\Delta^4\bar u_i)^2/(\beta_k+\epsilon))^q\big)$ with
$q=1$ (Eq. (26)). The scheme is called IMWENO-P; its accuracy at critical
points is on [accuracy at critical points](/properties/critical-point-accuracy.md).
*(Compiler check, not in the sources: the printed $\beta_0$, $\beta_1$,
$\beta_2$ satisfy the mirror relation above.)*

**Evidence.** On the low-density, low-internal-energy double rarefaction
($(\rho,v,p)=(1,\mp2,0.4)$, 300 cells, $t=0.15$), WENO-NS, WENO-P and
MWENO-P produce negative pressure and fail, while IMWENO-P, WENO-JS,
WENO-Z, WENO-η and WENO-ZS finish (§4.3, Example 10, Figs. 9–10; see
[double rarefaction](/benchmarks/double-rarefaction-problem.md)). The
authors state that this "is not enough to link the symmetry-preserving
property with the positivity-preserving property", while the symmetric
schemes are "more stable numerically ... at least for the present test".
With the symmetry error
$E_s=\big(\tfrac1{N_x}\sum_i\lvert\rho(x_i,t)-\rho(x_{N_x-i},t)\rvert^2\big)^{1/2}$
(Eqs. (45)–(46)), IMWENO-P has the smallest error of the schemes over
$0.041<t<0.093$, and later the level of WENO-JS, WENO-Z and WENO-η,
much below WENO-ZS (Figs. 11–12). This is the only quantified measure of
solution symmetry on this page. The construction is limited to fifth order
"if no further modifications are done" (§3.2).

## 4. Symmetry of the volume fractions

Yan, Abgrall & Wu (2024) write the volume-fraction equation of the Kapila
[five-equation model](/definitions/five-equation-model.md) as an advection
with a non-conservative source, $\partial_t\phi_1+\nabla\cdot(\phi_1v)=\chi_1\phi_1\nabla\cdot v$,
whose companion for $\phi_2$ has the "similar (symmetric)" form with
$\chi_2$, where $\chi_1\phi_1+\chi_2\phi_2=1$ (page-local $\chi_k$; §2.1). Their
discontinuous Galerkin discretization of the source, Gauss quadrature of
$\partial_xv$ inside the cell plus an HLL-weighted split of the interface
velocity jump, "inherently ensures the symmetry of the volume fractions"
(Abstract, §1): the update of $\phi_2$ derived from that of $\phi_1$
collapses to the same form with $\chi_2$ (proof of Thm 2.7, Eq. (2.35)).
This requires the discrete identity
$\Delta x\sum_\nu\mathsf w_\nu(\partial_xv)^{[\nu]}=v^-_{i+1/2}-v^+_{i-1/2}$ (Eq. (2.10);
$\mathsf w_\nu$ the normalized Gauss weights, $(\partial_xv)^{[\nu]}$ the derivative at
Gauss point $\nu$, page-local), which they obtain by differentiating a
Gauss–Lobatto interpolant of the velocity (Remark 2.1; 2D Remark 3.1). The
property is structural, not a statement about solution symmetry: it is
what lets the proof of $\phi_1\ge0$ also give $\phi_2\ge0$, i.e.
$\phi_1\le1$ ([bound preservation](/properties/bound-preservation.md);
2D Thm 3.6).

## Qualifications

- Coefficient symmetry of the indicators (meaning 3) does not give mirror
  symmetry of the solution (meaning 1): Zhong et al.'s IMWENO-P breaks the
  Rayleigh–Taylor symmetry, and their symmetric reference schemes WENO-JS
  and WENO-Z keep the double-rarefaction symmetry no worse than IMWENO-P
  at late times. Zhong et al.'s indicators also carry the absolute mesh
  width as the weight of the first-difference term *(compiler check, not
  in the sources: the relative weight of the two terms therefore depends
  on the unit of length, while a rescaling $u\mapsto\sigma u$ multiplies
  every term by $\sigma^2$ and leaves the weights unchanged up to
  $\epsilon$; see [scale invariance](/properties/scale-invariance.md))*.
  The paper does not discuss it.

- Meaning 4 is unrelated to the other three: Yan et al. report no
  mirror-symmetry measurement, and their symmetry is between two unknowns
  of one cell, not between two cells.
- Meanings 1 and 2 are independent: a skew-symmetric (kinetic-energy-preserving)
  central scheme can still break mirror symmetry by round-off, and a
  mirror-symmetric shock-capturing scheme is in general not skew-symmetric.
- On mirror symmetry the evidence is the authors' visual inspection of
  contour plots; none quantifies the asymmetry. Tsoutsanis et al.'s case differs
  from the others: the loss is attributed to the multidimensional reconstruction on
  arbitrary unstructured elements, not to round-off, and no symmetric mesh is run to
  separate the two. Ji et al.'s symmetric shock tubes on uniform triangles show that an
  unstructured TENO reconstruction need not break a planar symmetry on its own; their
  test is one-dimensional and short, Tsoutsanis et al.'s two-dimensional and long, so the
  two observations concern different situations.
- Wakimura et al. (2024; received 24 February 2024, online 7 June 2024) state in
  Appendix A that "to our knowledge, no symmetry-preserving methods have been proposed for
  two-phase flow". Zhang et al. (2024a; received 7 August 2023, online 28 November 2023)
  call their THINC reconstruction on the five-equation model "symmetry-preserving" (§5)
  and show symmetry kept on a Mach 10 water column (§4.7, Fig. 13); Wakimura et al. do not
  cite them. The two concern different schemes (finite-volume WENO–THINC against BVD with
  HLLC fluctuations).
- [Fu (2021)](/sources/fu-2021.md) (§5.5.2) and the view Fu (2023) adopts are
  compatible on the cause (round-off) and differ on the role of dissipation: in
  the first, low dissipation fails to damp the round-off asymmetry; in the second,
  consistent arithmetic removes it whatever the dissipation. Neither source runs
  TENO-AA with the consistent implementation, which is the test that would show
  whether its asymmetry disappears.

# Citations

- [Fu (2021)](/sources/fu-2021.md) — §5.5.2, Fig. 9: TENO-AA Rayleigh–Taylor asymmetry and its stated cause.
- [Fu (2023)](/sources/fu-2023.md) — §3.8: WENO9-JS, TENO5 asymmetries; Don et al.; Fleischmann et al.; BVD.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §2.3, §4, §§4.7–4.8: consistent implementation, symmetric results.
- [Huang et al. (2026)](/sources/huang-2026.md) — §6.6: symmetric ROUND and LD-ROUND results.
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §5.3.2: WENO-Z+M symmetry on Riemann configuration 3.
- [Coppola & Veldman (2023)](/sources/coppola-2023.md) — §3.3, §5.1, §5.3, §6, Corollary A.4: skew-symmetry and kinetic-energy conservation.
- [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) — §4.6, Figs. 16–17, Table 2: symmetry loss on unstructured meshes.
- [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) — §4.7, Fig. 11: TENO5-type Rayleigh–Taylor asymmetry and its stated cause (arXiv v1).
- [Liang et al. (2022)](/sources/liang-2022.md) — §4, §§4.9–4.10, Figs. 21–23: round-off statement, symmetric results with the consistent implementation.
- [Ji, Liang & Fu (2022)](/sources/ji-2022.md) — §5.4, Figs. 6–7: 1D symmetry on triangular meshes (preprint).
- [Hong, Ye & Ye (2022)](/sources/hong-2022.md) — §5.5: enlarged $\epsilon$ against symmetry breaking.
- [Zhong et al. (2023)](/sources/zhong-2023.md) — §3.1–3.2, Eqs. (19)–(26), Table 1, Fig. 1, Lemma 1; §4.3, Example 10, Eqs. (45)–(46), Figs. 9–12; §4.4, Fig. 13: symmetric smoothness indicators, symmetry error, Rayleigh–Taylor asymmetry.
- [Li et al. (2023b)](/sources/li-2023-b.md) — §4.5, Fig. 21: ADADF-HY Rayleigh–Taylor asymmetry and its stated cause.
- [Sousa & Scalo (2022)](/sources/sousa-2022.md) — §5.2 (Fig. 6), §5.3 (Fig. 11): physical symmetry breaking in strong shock–vortex interaction; LAD symmetry loss with spurious oscillations, QSV symmetric (arXiv v2).
- [Zhang et al. (2024a)](/sources/zhang-2024.md) — §3.3, Eq. (44); §4.7, Fig. 13; §4.12: floating-point asymmetry of THINC, mirror flipping, symmetry at Mach 10 against MUSCL-THINC.
- [Wakimura et al. (2024)](/sources/wakimura-2024.md) — Appendix A, Eqs. (A.3)–(A.5): operation-ordering rules for two-phase BVD with HLLC fluctuations.
- [Liang & Fu (2024a)](/sources/liang-2024.md) — §4: round-off symmetry breaking and the Fleischmann et al. technique.
- [Zhang et al. (2024b)](/sources/zhang-2024-b.md) — §6.3.2: symmetry breaking of low-dissipation TENO attributed to floating-point truncation.
- [Yan, Abgrall & Wu (2024)](/sources/yan-2024.md) — Abstract; §1; §2.1, Eqs. (2.1), (2.10), Remark 2.1; Thm 2.7, Eq. (2.35); Remark 3.1, Thm 3.6: symmetry of the volume fractions.
