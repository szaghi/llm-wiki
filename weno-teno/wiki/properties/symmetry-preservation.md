---
type: Property
title: "Symmetry preservation"
description: "Symmetry preservation has two meanings in the sources: keeping the mirror symmetry of a symmetric flow under round-off or on an unstructured mesh, which low-dissipation schemes lose unless implemented consistently, and preserving the skew-symmetry of the continuous convective operator, which yields discrete kinetic-energy conservation; this page states both and the evidence on each."
status: established
aliases: [mirror symmetry preservation, symmetry breaking, symmetry-preserving discretization, skew-symmetry]
tags: [low-dissipation, teno, weno, kinetic-energy-preserving]
timestamp: 2026-10-23T10:00:00Z
---

# Symmetry preservation

The term covers two distinct properties, which a page or claim must keep apart.

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
  Huang et al. (2023, §4.7) give the same explanation for their TENO runs,
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

## Qualifications

- The two meanings are independent: a skew-symmetric (kinetic-energy-preserving)
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
- [Sousa & Scalo (2022)](/sources/sousa-2022.md) — §5.2 (Fig. 6), §5.3 (Fig. 11): physical symmetry breaking in strong shock–vortex interaction; LAD symmetry loss with spurious oscillations, QSV symmetric (arXiv v2).
