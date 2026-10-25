---
type: Definition
title: "Large-eddy simulation: filtering and the subgrid-scale stress"
description: "Large-eddy simulation resolves the filtered velocity and models the subgrid-scale stress; this page fixes the filtered equations, the filters and filter widths used by the sources (including high-aspect-ratio cells and element methods), the commutation and discretization terms, and the gauge freedom of the subgrid stress."
status: established
aliases: [LES, filtered Navier–Stokes equations, subgrid-scale stress, SGS stress, subfilter stress, coarse-grained equations]
tags: [les, filtering, sgs-model, compressible]
timestamp: 2026-10-25T19:45:00Z
---

# Large-eddy simulation: filtering and the subgrid-scale stress

**Large-eddy simulation (LES)** computes a low-pass filtered velocity
$\bar u_i=G*u_i$ that carries the large, energy-containing eddies, and
replaces the effect of the removed (subgrid) scales by a model of the
**subgrid-scale (SGS) stress**
$\tau_{ij}=\overline{u_iu_j}-\bar u_i\bar u_j$. The filtered equations are
exact but unclosed; the closure question is what replaces $\tau_{ij}$ (an
explicit [subgrid-scale model](/methods/smagorinsky-model.md), the
discretization itself in [implicit LES](/definitions/implicit-les.md), or a
learned correction). The filter can be an explicit convolution, the grid
projection, or the operator induced by the discretization, and the sources
disagree on conventions (sign of $\tau_{ij}$, definition of the filter width
$\Delta$, meaning of "implicit"); this page records them in the registry
notation.

## Filtered equations

For incompressible flow, with a filter that commutes with differentiation,
Agrawal et al. (2022, §II, Eqs. 1–3)
[(source)](/sources/agrawal-2022.md) write

$$\begin{aligned}
\partial_i\bar u_i&=0,\\
\partial_t\bar u_i+\partial_j(\bar u_i\bar u_j)&=-\partial_i\bar p+\nu\,\partial_j\partial_j\bar u_i-\partial_j\tau_{ij},\qquad
\tau_{ij}=\overline{u_iu_j}-\bar u_i\bar u_j ,
\end{aligned}$$

with $p$ the kinematic pressure; the isotropic part
$\tfrac13\tau_{kk}\delta_{ij}$ is absorbed into a modified pressure, so only
the deviatoric part $\tau^d_{ij}$ is modelled. [Prakash et al. (2022)](/sources/prakash-2022.md)
(§II, Eqs. 1–2) and [Abe (2021)](/sources/abe-2021.md) (§II, Eqs. 1–2)
write the same equations; Abe includes $\tfrac13\tau_{kk}$ in the filtered
pressure, while Prakash et al. keep the full (not deviatoric) tensor. The same structure, with the
SGS term written as an operator $M_i=-\partial_j\tau_{ij}$ added to the
right-hand side, is used by [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md)
(§2.1, Eqs. 6–9), who stress that the LES problem can be posed independently
of the mesh: in their usage $\Delta$ is a separation scale, a continuous
parameter, and the cell size $\Delta x$ is chosen separately.

For compressible flow [Goc et al. (2021)](/sources/goc-2021.md) (§2.1,
Eqs. 2.1–2.5) filter the mass, momentum and total-energy equations with the
Favre filter $\tilde\phi=\overline{\rho\phi}/\bar\rho$; the momentum
equation carries $-\partial_j\tau_{ij}$ with
$\tau_{ij}=\bar\rho(\widetilde{u_iu_j}-\tilde u_i\tilde u_j)$, and the
energy equation an SGS heat flux $\bar\rho(\widetilde{eu_j}-\tilde e\tilde u_j)$
plus the SGS work term $-\partial_j(\tilde u_i\tau_{ij})$. Goc et al. call
the overbar and tilde "Reynolds and Favre averaging operators" although they
use them as LES filters. [Hoy & Bermejo-Moreno (2022)](/sources/hoy-2022.md)
(§3) solve the spatially filtered compressible equations with a
cell-centred finite-volume method in arbitrary Lagrangian–Eulerian form, to
follow a deforming panel.

[Duraisamy (2021)](/sources/duraisamy-2021.md) (§II, Eq. 2) frames LES and
RANS together: coarse-graining a high-fidelity system $\mathcal R(q)=0$ by
low-pass filtering (LES) or ensemble averaging (RANS) gives an equation for
the coarse-grained state plus the divergence of an unclosed term, and this
coarse-grained equation "is *not* an approximation"; the approximation enters
only with the closure.

### Sign conventions in the sources

The registry uses the positive-trace convention above. Three sources print
the opposite sign and are translated here:
[Vela-Martín (2022)](/sources/velamartin-2022.md) (§2.1, Eq. 2.3, said
explicitly by the author) defines the stress as $\bar u_i\bar u_j-\overline{u_iu_j}$
entering with $+\partial_j$; [Haering et al. (2022)](/sources/haering-2022.md)
(§III, Eq. 3) define $\tau^{sgs}_{ij}=-(\overline{u_iu_j}-\bar u_i\bar u_j)$;
Duraisamy (2021, §III.B) writes the SGS stress with the reversed sign while
the RANS stress of the same paper (Table I) is positive. Agrawal et al. (2022), Goc et al.
(2021), Vicente Cruz & Lamballais (2023), Abe (2021) and Prakash et al.
(2022) use the positive convention.

## Filters and filter widths

**Kernels.** Vela-Martín (2022, §5.2, Eqs. 5.1–5.4) applies two homogeneous
filters to DNS of isotropic turbulence: the sharp Fourier filter,
$\hat G(k)=1$ for $|\boldsymbol k|<\pi/\Delta$ and 0 otherwise, and the
Gaussian filter $\hat G(k)=\exp\!\big(-k^2\Delta^2/(2\pi^2)\big)$, with
$\Delta$ the filter scale (the author's $\ell$). Vicente Cruz & Lamballais
(2023, §6.3, Eqs. 48–50) instead write the Gaussian as
$\exp(-k^2\Delta^2/24)$ and introduce a super-Gaussian
$\exp(-k^6\Delta^6/256)$; the two Gaussian forms are the same kernel with
widths related by $\Delta^2_{(24)}=12\Delta^2_{(2\pi^2)}/\pi^2$ *(compiler
check, not in the sources)*, a convention difference only. For a priori
filtering of channel DNS, Agrawal et al. (2022, §V) use a discretely
commutative filter with three vanishing moments applied recursively to a
width of three grid sizes. [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md)
(App. E, Eqs. E.1–E.5) give the transfer functions of the top-hat
volume-averaging filter, $\prod_\alpha\mathrm{sinc}(\pi k_\alpha\Delta/2)$,
and of their face-averaging filter, which omits the factor of the face-normal
direction and therefore damps less. Prakash et al. (2022, §III.A) box-filter
DNS of isotropic turbulence ($Re_\lambda=418$) isotropically and
anisotropically: "book-type" filters with one fine and two coarse widths and
"pencil-type" filters with two fine and one coarse width, the coarse
widths up to $292\eta$ against a fine width of $15\eta$. Abe (2021, §IV B, App. C) top-hat filters a fine LES of a
backward-facing-step flow in the two homogeneous-spacing directions only,
and checks with a three-point trapezoidal filter
$\bar\phi_i=\tfrac14(\phi_{i+1}+2\phi_i+\phi_{i-1})$ that filtering also in
the wall-normal direction changes the subgrid values little.

The amount of [backscatter](/definitions/energy-backscatter.md) measured
a priori depends strongly on the kernel: the local flux is negative in about
half of the domain with the sharp filter and in less than one-fifth with the
Gaussian filter (Vela-Martín 2022, §5.3).

**Effective filter of an LES.** Vicente Cruz & Lamballais (2023, §6.3,
Eq. 48) measure the filter an LES actually applies through the transfer
function $T_f(k,t)=\sqrt{E_{\mathrm{LES}}(k,t)/E_{\mathrm{DNS}}(k,t)}$
(page-local symbol). A [Smagorinsky](/methods/smagorinsky-model.md) LES at
numerical convergence gives $T_f(k_\Delta)\approx0.6$ and a slow decay
beyond: a weak filter. The [implicit spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
LES is approximated by the super-Gaussian above.

**Filter width.** The sources define $\Delta$ differently:

| Source | $\Delta$ |
|---|---|
| [Beck & Kurz (2023)](/sources/beck-2023.md), §III B, Eq. 11 | $\sqrt[3]{\mathrm{Vol}}/(N+1)$ for a DG element of volume Vol and degree $N$; the authors note it is not unique (non-equidistant nodes, skewed elements) |
| [Flad & Gassner (2017)](/sources/flad-2017.md), App. A | printed as "the local cell volume divided by $(N+1)^3$" (see Qualifications) |
| Agdestein & Sanderse (2025), §3.3 | the coarse grid spacing, "the diameter of the averaging domain in the infinity norm" |
| Vicente Cruz & Lamballais (2023), §4.1 | a separation scale independent of the mesh; the cell-based variant sets $\Delta=\Delta x$ |
| Haering et al. (2022), §II C | argue that the cube root of the cell volume tends to the smallest cell length at high aspect ratio and overestimates the effective resolution; they prefer measures based on the cell diagonal and a resolution tensor |
| Prakash et al. (2022), §II–III | $(\Delta_1\Delta_2\Delta_3)^{1/3}$ (after Deardorff) for the Smagorinsky and gradient models; the grid size in the a posteriori LES |
| Abe (2021), §II, §IV D | compares $(\Delta x\Delta y\Delta z)^{1/3}$, $\max(\Delta x,\Delta y,\Delta z)$ and, in the author's mixed model, $\sqrt{\max(\Delta x\Delta y,\Delta y\Delta z,\Delta z\Delta x)}$, which equals the maximum when $\Delta x=\Delta z\gg\Delta y$ |
| [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md), §6.1, Eq. (125) | $\Delta^3=\mathrm{Vol}/(N+1)^3$ for a DG element of degree $N$ |
| [Basile et al. (2023)](/sources/basile-2023.md), §2.2 | DES length scale $\sqrt[3]{\mathrm{Vol}}/(N+1)$ on DG elements: the cube root instead of the maximum spacing of classical DES, divided by $N+1$ following Lorteau et al. |
| [François et al. (2022)](/sources/francois-2022.md), §3.1 | DES length scale switching from $\max(\Delta x,\Delta y,\Delta z)$ to $(\Delta x\Delta y\Delta z)^{1/3}$ where the DDES shielding function exceeds 0.8 (ZDES mode 2, after Deck) |

In implicitly filtered LES the filter width and the grid spacing $h$
coincide approximately, $h\approx\Delta$, whereas in explicitly filtered LES
they are chosen independently (Beck & Kurz 2023, §I).

### High-aspect-ratio cells

Abe (2021) isolates the effect of cell anisotropy from wall damping by
testing in the free shear layer behind a [backward-facing step](/benchmarks/backward-facing-step.md)
($Re_\tau=290$ in the driver channel), where the cells are coarse in $x$ and
$z$ ($0.1H$) but fine in $y$ ($\Delta x/\Delta y\sim100$). A priori, the
[Smagorinsky](/methods/smagorinsky-model.md) viscosity with the cube-root
width is "clearly suppressed by the extremely narrow grid width in the
y-direction", and swapping widths between the Smagorinsky model and the
author's mixed model reverses which one is suppressed (§IV C–D, Figs. 9–10).
A posteriori, the mixed model with the cube-root width lengthens the
recirculation bubble (reattachment length $x_R$, page-local) from $x_R/H=7.19$ to 7.43 against the experimental
6.51 (Table III). The author concludes that "the effect of a grid width in
one direction much smaller than in other directions must be excluded in
determining the filter width" (§V), which agrees with the argument of
Haering et al. (2022, §II C) that the cube root tends to the smallest
spacing. Abe tests only a free shear layer; near-wall treatment "was not
our main concern". The [dynamic procedure](/methods/dynamic-procedure.md)
sidesteps the question by computing $(C_s\Delta)^2$ as one product (Abe
2021, §II A); Prakash et al. (2022, §III) use it for the same reason in
their dynamic mixed model, since "the optimal definition of $\Delta$ for
anisotropic grids is not yet known". The two zonal-DES sources above choose the cube root in
LES regions without a comparison of definitions.

### Element methods

In discontinuous Galerkin LES, Basile et al. (2023, §3.2) note two cutoff
wavenumbers, that of the mesh and that of the full discretization, with the
modal spectrum inside an element covering the scales between them; they
build a smoothness indicator on it (see
[mesh adaptation](/methods/mesh-adaptation.md)). They attribute spurious
peaks in centreline rms profiles on coarse elements partly to DG
inter-element discontinuities, recalling an a priori study by Beck et al.
in which filtered DNS projected on a DG/LES grid is itself discontinuous at
element interfaces (§4.2.3, Fig. 10). In the continuous spectral element
method the velocity is continuous across elements but its gradient is not;
on coarse meshes [Gillyns et al. (2022)](/sources/gillyns-2022.md) (§2, §6,
§8) see Gibbs spikes in the fluctuation statistics at element boundaries,
which vanish as the mesh approaches DNS resolution and which they use as a
reference-free mesh-quality indicator. Their subgrid model is Nek5000's
approximate deconvolution model (see
[scale-similarity models](/methods/scale-similarity-model.md)).

## Commutation and discretization terms

Beck & Kurz (2023, §I, Eqs. 1–5) decompose the unclosed terms of the
filtered inviscid Burgers equation $\partial_tu+\tfrac12\partial_x(u^2)=0$
into three parts:

- a **commutation error** $C_1=\partial_x\overline{u^2}-\overline{\partial_x u^2}$,
  nonzero when $\Delta=\Delta(x)$ varies or is anisotropic, and present even
  for linear advection;
- the classical subfilter term $C_2=\partial_x(\bar u\bar u)-\partial_x\overline{u^2}$,
  the one-dimensional analogue of $-\partial_j\tau_{ij}$;
- a **discretization term**
  $C_3=\delta_x(\bar u\bar u)-\partial_x(\bar u\bar u)$, with $\delta_x$ the
  discrete derivative, which in the form of Geurts & van der Bos (as recalled
  by Beck & Kurz) is the divergence of a "computational subgrid stress"
  built with the numerically induced filter.

For $\Delta\approx h$ the computational term can be considerably larger than
the classical term, and for nonlinear schemes (upwinding, limiters,
reconstructions) it depends on the solution and cannot be determined a
priori (Beck & Kurz 2023, §I). This motivates the
[discretization-consistent closure](/definitions/discretization-consistent-closure.md).

Agdestein & Sanderse (2025, §3.2, Eqs. 11–12) make the same point in
discrete form: filtering the discrete DNS with a discrete filter $\Phi$ gives
an exact equation for $\Phi u$ whose closure term, the discrete commutator
error, contains both the subfilter effect and the coarse-grid
discretization error. Discrete filters do not in general commute with the
discrete divergence; their face-averaging filter does, which is the basis of
the [divergence-consistent LES](/methods/divergence-consistent-les.md).
Haering et al. (2022, §II A, §IV) treat their active forcing term as a model
of the commutator between the implicit filter and the substantial
derivative.

## Gauge freedom of the subgrid stress

The resolved equations depend on $\tau_{ij}$ only through its divergence.
Vela-Martín (2022, §3, Eqs. 3.1–3.5), following an idea attributed to
Jiménez (2016), adds to $\tau_{ij}$ any symmetric divergence-free tensor
without changing the resolved dynamics. The total SGS term in the resolved
energy equation and the domain-averaged flux are invariant, but the local
split between the interscale flux $\Pi=-\tau_{ij}\bar S_{ij}$ and a
conservative spatial flux is not. The consequence drawn by the author is
that a model must reproduce the divergence of the stress, not the stress,
and that a poor a priori correlation between a model stress and the filtered
DNS stress is not by itself evidence of poor modelling: equivalent stress
representations correlate with one another only at 0.4–0.6 (§6.3, §8). See
[energy backscatter](/definitions/energy-backscatter.md).

## Resolution and the resolved fraction

Haering et al. (2022, §III B, Eqs. 9–10) use a triple decomposition
$u_i=\langle u_i\rangle+u_i^>+u_i^<$ (mean, resolved fluctuation, subgrid
fluctuation) with a filter that leaves the mean unchanged,
$\bar u_i=\langle u_i\rangle+u_i^>$, and write $\tau_{ij}$ as cross and
subgrid–subgrid products of $u^>$ and $u^<$. Their computable measure of
resolution is the unresolved fraction $1-k_{\mathrm{res}}/k_{\mathrm{tot}}$;
citing Jiménez & Moser, they recall that typical LES requires this fraction
to be below about 0.1 (§V A 1). The grid counts needed for wall-resolved and
wall-modelled LES are on [LES grid-point requirements](/results/les-grid-point-requirements.md),
and the near-wall alternative on [wall-modelled LES](/methods/wall-modelled-les.md).

## Other uses of the filter idea

- [Pereira et al. (2021)](/sources/pereira-2021.md) (§III, Eqs. 13–16) write
  the [PANS](/methods/partially-averaged-navier-stokes.md) decomposition as
  a filter with a resolved and a density-weighted resolved part, which
  reduces to Reynolds and Favre averaging in the RANS limit; see
  [hybrid RANS/LES](/definitions/hybrid-rans-les.md).
- [Liu et al. (2022)](/sources/liu-2022.md) (§1) treat the scales resolved
  by a cosmological MHD simulation as the mean field of mean-field
  electrodynamics, with dissipation provided by truncation errors, and close
  the unresolved induction with a
  [subgrid turbulent dynamo model](/methods/subgrid-turbulent-dynamo-model.md);
  see [implicit LES](/definitions/implicit-les.md).

## Testing a closure

LES closures are assessed [a priori and a posteriori](/definitions/a-priori-and-a-posteriori-testing.md):
on filtered DNS fields outside the solver, or with the model running in the
LES. [Domingo & Vervisch (2023)](/sources/domingo-2023.md) (§1, §3.1) state
that a priori tests miss error accumulation and compensation over time, and
describe a **DNS embedded in LES** of a burner, whose DNS box can be
coarsened to LES resolution to test closures a posteriori in the same
configuration (see [direct numerical simulation](/definitions/direct-numerical-simulation.md)).

[Bae & Koumoutsakos (2022)](/sources/bae-2022.md) (Introduction, p. 3;
Methods, p. 13) train a wall model inside a channel LES (staggered
second-order finite differences, anisotropic minimum-dissipation SGS model,
"known to perform well in highly anisotropic grids") so that the learned
policy compensates for the numerical and SGS errors of that solver; see
[model-consistent training](/methods/model-consistent-training.md). LES
and implicit LES also serve as reference data for RANS closures: the
transition-model study of [Carreño Ruiz & D'Ambrosio (2022)](/sources/carrenoruiz-2022.md)
(§3–4, Tables 5–7; §3.5, Figs. 4–5) compares separation, transition and reattachment on the
SD7003 airfoil at $Re_c=6\times10^4$ with the implicit LES of Galbraith &
Visbal and finds the RANS post-reattachment skin friction much smaller
than the LES one; see
[local-correlation-based transition models](/methods/local-correlation-based-transition-model.md).

## Qualifications

- Flad & Gassner (2017, App. A) print the filter width as "the local cell
  volume divided by $(N+1)^3$", which is a volume, not a length; the length
  form of the same idea is the cube root used by Beck & Kurz (2023, Eq. 11).
- Goc et al. (2021, p. 4) print the resolved viscous stress as
  $\mu(\tilde T)(\tilde S_{ij}-\tfrac13\tilde S_{kk}\delta_{ij})$; with
  $S_{ij}$ defined with the factor $\tfrac12$, the Newtonian deviatoric stress
  is $2\mu S^d_{ij}$ (the registry's $\sigma_{ij}$) *(compiler check, not in
  the sources)*, so the printed formula lacks the factor 2.
- Agdestein & Sanderse (2025, App. E) state that the top-hat transfer
  function in 3D "only depends on $\|k\|$"; their own Eq. (E.2) is a product
  of one-dimensional factors, which is isotropic only to second order near
  $k=0$ *(compiler check, not in the sources)*.

- Abe (2021) gives the coarse-grid case two labels, BSC and, in §III and the
  Fig. 8 caption, "BFC".

# Citations

- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §II, Eqs. (1)–(4); §V (a priori filter).
- [Goc et al. (2021)](/sources/goc-2021.md) — §2.1, Eqs. (2.1)–(2.5).
- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §2.1, Eqs. (6)–(9); §4.1; §6.3, Eqs. (48)–(50).
- [Vela-Martín (2022)](/sources/velamartin-2022.md) — §2.1, Eqs. (2.2)–(2.7); §3, Eqs. (3.1)–(3.5); §5.2–5.3; §6.3; §8.
- [Beck & Kurz (2023)](/sources/beck-2023.md) — §I, Eqs. (1)–(5); §III B, Eq. (11).
- [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md) — §3.2–3.3, Eqs. (11)–(15); App. E.
- [Haering et al. (2022)](/sources/haering-2022.md) — §II A–C; §III, Eqs. (3)–(10); §V A 1.
- [Flad & Gassner (2017)](/sources/flad-2017.md) — App. A.
- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §II, Eqs. (1)–(3), Table I; §III.B.
- [Domingo & Vervisch (2023)](/sources/domingo-2023.md) — §1; §3.1.
- [Abe (2021)](/sources/abe-2021.md) — §II, Eqs. (1)–(2), (4), (12); §IV B–D, Tables I–III, Figs. 9–10; §V; App. C, Eq. (C1).
- [Prakash et al. (2022)](/sources/prakash-2022.md) — §II, Eqs. (1)–(3); §III; §III.A.
- [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md) — §6.1, Eq. (125).
- [Basile et al. (2023)](/sources/basile-2023.md) — §2.2; §3.2; §4.2.3, Fig. 10.
- [François et al. (2022)](/sources/francois-2022.md) — §3.1.
- [Gillyns et al. (2022)](/sources/gillyns-2022.md) — §2; §6; §8.
- [Hoy & Bermejo-Moreno (2022)](/sources/hoy-2022.md) — §3.
- [Pereira et al. (2021)](/sources/pereira-2021.md) — §III, Eqs. (13)–(16).
- [Liu et al. (2022)](/sources/liu-2022.md) — §1.
- [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) — Introduction, p. 3; Methods, p. 13.
- [Carreño Ruiz & D'Ambrosio (2022)](/sources/carrenoruiz-2022.md) — §3–4, Tables 5–7; §3.5, Figs. 4–5.
