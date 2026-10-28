---
type: Definition
title: "Barycentric anisotropy map"
description: "Representation of the Reynolds-stress anisotropy by the eigenvalues of the normalized anisotropy tensor as a convex combination of the one-, two- and three-component limiting states on an equilateral triangle; its weights and colour map, the plane-strain locus of linear eddy-viscosity models, and its use on boundary layers, cascades and learned closures."
status: established
aliases: [barycentric map, barycentric triangle, anisotropy-invariant map, componentality map, Banerjee barycentric map, Emory–Iaccarino colour map, realizability triangle]
tags: [rans, reynolds-stress-model, eddy-viscosity, anisotropy, uncertainty-quantification]
timestamp: 2026-10-28T07:05:00Z
---

# Barycentric anisotropy map

The barycentric map displays the state of the Reynolds-stress anisotropy
through the three ordered eigenvalues of the normalized anisotropy tensor
$b_{ij}=R_{ij}/(2k)-\tfrac13\delta_{ij}$. Any realizable state is a convex
combination of three limiting states, one-component (1C), isotropic
two-component (2C) and isotropic three-component (3C), so it can be placed
inside an equilateral triangle whose vertices are those states. Kokkinakis
et al. (2023) use it in the form of Banerjee et al., with the colour
weights of Emory & Iaccarino, on the Favre Reynolds stress of a
supersonic boundary layer
([Kokkinakis et al. (2023)](/sources/kokkinakis-2023.md), §IV D, Eqs.
4–5). Page-local symbols: $\lambda^b_1\ge\lambda^b_2\ge\lambda^b_3$ the
eigenvalues of $b_{ij}$ (not the Taylor microscale $\lambda$), $C_{1c}$,
$C_{2c}$, $C_{3c}$ the barycentric weights, $X_{ic}$, $C_{\mathrm{off}}$,
$C_{\mathrm{exp}}$ the colour weights and their constants.

## Limiting states and weights

With $R_{ij}=\langle\rho u_i''u_j''\rangle/\langle\rho\rangle$ in compressible
flow and $k=\tfrac12R_{kk}$, the eigenvalues satisfy
$-\tfrac13\le\lambda^b_i\le\tfrac23$, and the limiting states are
(Kokkinakis et al. 2023, §IV D):

| state | eigenvalues $(\lambda^b_1,\lambda^b_2,\lambda^b_3)$ | shape named in the source |
|---|---|---|
| 3C, isotropic | $(0,0,0)$ | "spherical" |
| 2C, isotropic two-component | $(\tfrac16,\tfrac16,-\tfrac13)$ | "pancake-like" |
| 1C, one-component | $(\tfrac23,-\tfrac13,-\tfrac13)$ | "rod or cigar-like" |

The barycentric weights of a state are
$$C_{1c}=\lambda^b_1-\lambda^b_2,\qquad C_{2c}=2(\lambda^b_2-\lambda^b_3),\qquad C_{3c}=3\lambda^b_3+1,$$
and they sum to one because $b_{ij}$ is traceless,
$C_{1c}+C_{2c}+C_{3c}=\lambda^b_1+\lambda^b_2+\lambda^b_3+1=1$ *(compiler check,
not in the sources)*. Each weight is one at its own vertex and zero at the
other two, e.g. $C_{1c}=1$, $C_{2c}=C_{3c}=0$ at the 1C state *(compiler check,
not in the sources)*. The edges of the triangle carry the axisymmetric
states: one edge axisymmetric expansion (one large component, prolate
spheroid), one axisymmetric contraction (one small component, oblate
spheroid), and the third the two-component limit reached near walls
(§IV D).

**Colour map.** For field plots Kokkinakis et al. turn the weights into
red–green–blue colour weights after Emory & Iaccarino,
$$X_{ic}=(C_{ic}+C_{\mathrm{off}})^{C_{\mathrm{exp}}},\qquad C_{\mathrm{off}}=0.65,\quad C_{\mathrm{exp}}=5$$
(Eq. 5), so that a surface or plane coloured by componentality shows the
local state without a triangle per point.

## Linear eddy-viscosity models on the map

Under the [Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md)
the anisotropy is $b_{ij}=-(\nu_t/k)\langle S^d_{ij}\rangle$, a multiple of the
mean strain, and the sources state the consequence on the map: the linear
model restricts the anisotropy to the plane-strain line, and a
tensor-basis closure can explore the other realizable states, as
barycentric-map studies they cite show
([Agrawal & Koutsourelakis (2024)](/sources/agrawal-2024.md), §2.2.1; arXiv
v2). In a two-dimensional incompressible mean flow the mean strain has the eigenvalues
$(s,0,-s)$ for some $s\ge0$, so the Boussinesq $b_{ij}$ has a zero middle
eigenvalue *(compiler check, not in the sources)*. Tang et al. (2023) show
it on the parametrized periodic hills: the anisotropy of their baseline
[$k$-$\varepsilon$ model](/methods/k-epsilon-model.md) lies close to the
plane-strain line at all six stations, while their symbolic-regression
correction moves it towards the DNS with "a tiny minority of outliers"
([Tang et al. (2023)](/sources/tang-2023.md), §III C, Fig. 8; see
[symbolic-regression closures](/methods/symbolic-regression-closure.md)
and [periodic hill](/benchmarks/periodic-hill.md)). Morsbach et al. (2024)
state the same restriction for free-stream turbulence: through the
Boussinesq approximation the turbulence anisotropy of a linear model
equals the strain-rate anisotropy, so it cannot reproduce the anisotropy
of the incoming turbulence
([Morsbach et al. (2024)](/sources/morsbach-2024.md), §4.2).

## Uses in the sources

- **Low-pressure-turbine cascade, LES against RANS.** In the implicit LES of
  Morsbach et al. (2024) the injected free-stream turbulence is
  two-component at the inlet and returns towards isotropy in the channel;
  in the blade passage the flow acceleration stretches the vortices and
  drives the anisotropy towards the two-component axisymmetric corner from
  leading to trailing edge, then back towards isotropy, which the
  SSG/LRR-$\omega$ [Reynolds-stress model](/methods/reynolds-stress-model.md)
  reproduces qualitatively (§3.3, Fig. 4). The LES shows nearly
  one-component turbulence in the transitional separated shear layer and
  nearly isotropic turbulence after transition, which the Reynolds-stress
  model, without near-wall pressure–strain or dissipation terms, misses;
  downstream of the passage vortex the LES carries two-component free-stream
  turbulence where the model gives a large rod-like region (§4.2, Fig. 15;
  see [laminar separation bubble](/definitions/laminar-separation-bubble.md)
  and [turbine cascades](/benchmarks/turbine-cascade.md)).
- **Supersonic boundary layer with a corrected wall model.** On a flat
  plate at $M=1.69$, $Re_\theta=50\,000$, the measured anisotropy is
  two-component near the wall, tends to isotropy outward and approaches
  one-component near the edge; an SST-IDDES wall-modelled LES captures this
  "to some extent" but turns isotropic outside the edge, and its
  random-forest correction of the wall shear stress and heat flux improves
  the map "significantly"
  ([Zangeneh (2021)](/sources/zangeneh-2021.md), §III A 1, Fig. 9; see
  [machine-learning wall models](/methods/machine-learning-wall-model.md)
  and [turbulent boundary layer](/benchmarks/turbulent-boundary-layer.md)).
- **Shock/boundary-layer interaction over deformed panels.** Kokkinakis et
  al. (2023) map the componentality on wall-parallel planes of an implicit
  LES of the $M_\infty=1.94$ oblique-shock interaction over a planar panel and
  six static deformation modes (§IV D, Figs. 10–13):
  - at $y^+=4.8$ the turbulence is mostly two-component, and the shock and
    expansion impingement drive it towards one-component; positive
    (bump-first) modes strengthen this shift near the midspan, most for the
    smallest-amplitude mode $+3$, negative modes hamper it (Fig. 10);
  - at $y^+=24$ and 192 the componentality contours bend concave where the
    surface moves towards the flow and convex where it moves away, most in
    the recovery region downstream of the interaction (Figs. 11–12);
  - at $y^+=2063$ the deformations leave little or no trace (Fig. 13).
  
  The deformations change the topology of the anisotropy, not its state,
  which the authors explain by deformations that vary slowly against the
  boundary-layer thickness (§IV D). The mesh behind these maps has
  $\Delta x^+=717$, $\Delta z^+=634$ (§III B 2, Table III); see
  [shock/boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
  and [implicit LES](/definitions/implicit-les.md).
- **Eigenvalue perturbation for model-form uncertainty.** Writing $b_{ij}$
  through its eigenvalues and eigenvectors, the eigenspace-perturbation
  approach of Emory et al. moves the eigenvalues towards the 1C, 2C and 3C
  vertices of the triangle and runs the model at the extreme states to
  bracket the prediction, as reviewed by
  [Duraisamy et al. (2019)](/sources/duraisamy-2019.md), §4.1, Eq. 10; details
  on [model-form uncertainty](/definitions/model-form-uncertainty.md).
- **Normalization of learned closures.** Sandberg & Zhao (2022, §4.1) cite
  Weatheritt & Sandberg's finding, from barycentric maps, that normalizing
  the strain and rotation by the turbulence time scale is inappropriate
  near walls ([Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md), §4.1;
  see [tensor-basis neural network](/methods/tensor-basis-neural-network.md)
  and [explicit algebraic Reynolds-stress models](/methods/explicit-algebraic-reynolds-stress-model.md)).

## Qualifications

- Kokkinakis et al. (2023) run the interaction on a mesh far coarser in
  the wall-parallel directions than the wall-resolved LES guidance they
  quote ($\Delta x^+\approx50$–130, $\Delta z^+\approx15$–30, §III B 2); the
  near-wall maps are those of that implicit LES. They place the first plane
  at $y^+=4.8$ in the text and at $y^+=5$ in the caption of Fig. 10, and
  give the outer-layer height as $y^+\simeq1000$ in Conclusion 4 while the
  plane analysed is $y^+=2063$.
- Tang et al. (2023, §III C) list the first barycentric station as
  $x/h=1.5$, while the caption and panels of Fig. 8 give $x/h=0.5$.
- Zangeneh (2021) prints the Fig. 9 caption truncated ("Barycentric map of
  Reynolds stress of.").
- No source prints the mapping from the weights to the coordinates of a
  point in the triangle; the page records the weights as printed.

# Citations

- [Kokkinakis et al. (2023)](/sources/kokkinakis-2023.md) — §III B 2 Table III, §IV D Eqs. 4–5 Figs. 10–13, §V.
- [Agrawal & Koutsourelakis (2024)](/sources/agrawal-2024.md) — §2.2.1 (arXiv v2).
- [Tang et al. (2023)](/sources/tang-2023.md) — §III C Fig. 8 (arXiv v1).
- [Morsbach et al. (2024)](/sources/morsbach-2024.md) — §3.3 Fig. 4, §4.2 Fig. 15.
- [Zangeneh (2021)](/sources/zangeneh-2021.md) — §III A 1, Fig. 9.
- [Duraisamy et al. (2019)](/sources/duraisamy-2019.md) — §4.1, Eq. 10.
- [Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md) — §4.1.
