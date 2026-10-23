---
type: Method
title: "IMEX linear multistep and IMEX-BDF methods"
description: "IMEX multistep methods treat a stiff part implicitly with BDF and the rest by explicit extrapolation of past values: IMEX-BDF coefficients, explicit versus linearly implicit treatment of the nonlinear term, uniform-in-epsilon accuracy for relaxation systems, robust Navier–Stokes bounds with their CFL-type conditions, and the linearly implicit multistep methods as IMEX schemes."
status: established
aliases: [IMEX-BDF, SBDF, semi-implicit BDF, implicit-explicit multistep method, IMEX LMM, extrapolated BDF, linearly implicit BDF]
tags: [linear-multistep, imex, implicit, stiff, asymptotic-preserving, stability]
timestamp: 2026-10-20T06:18:00Z
---

# IMEX linear multistep and IMEX-BDF methods

For a split right-hand side $f=f^{\mathrm E}+f^{\mathrm I}$, with $f^{\mathrm I}$ stiff, an
**IMEX linear multistep method** combines an implicit multistep method for $f^{\mathrm I}$ with
an explicit one for $f^{\mathrm E}$, both sharing the same $\alpha_j$. The standard family is
**IMEX-BDF**. It takes BDF for the implicit part and evaluates the explicit part on past values
with the weights of polynomial extrapolation to $t_{n+k}$:

$$\sum_{j=0}^k\alpha_jy_{n+j}=h\sum_{j=0}^{k-1}\beta^{\mathrm E}_jf^{\mathrm E}(t_{n+j},y_{n+j})+h\beta_kf^{\mathrm I}(t_{n+k},y_{n+k}),$$

where $\beta^{\mathrm E}_j$ (page-local) is $\beta_k$ times the extrapolation weights
([Ma et al. (2026)](/sources/ma-2026.md), Eq. (2.2), after Hundsdorfer–Ruuth and
Ascher–Ruuth–Wetton). It has order $k$. If $f^{\mathrm I}$ is linear, each step needs one linear
solve with $I-h\beta_kJ^{\mathrm I}$, where $J^{\mathrm I}$ (page-local) is its Jacobian.

## Coefficients

Ma et al. (2026, §2.2) print $k=1,2,3$ with $\alpha_k=1$:

| $k$ | $\alpha$ $(\alpha_0,\dots,\alpha_k)$ | $\beta^{\mathrm E}$ $(\beta^{\mathrm E}_0,\dots,\beta^{\mathrm E}_{k-1})$ | $\beta_k$ |
|---|---|---|---|
| 1 | $(-1,1)$ | $(1)$ | 1 |
| 2 | $(\tfrac13,-\tfrac43,1)$ | $(-\tfrac23,\tfrac43)$ | $\tfrac23$ |
| 3 | $(-\tfrac2{11},\tfrac9{11},-\tfrac{18}{11},1)$ | $(\tfrac6{11},-\tfrac{18}{11},\tfrac{18}{11})$ | $\tfrac6{11}$ |

For $k=2$ and $k=3$ the explicit weights are $\beta_k$ times the extrapolation weights $(-1,2)$
and $(1,-3,3)$ *(compiler check)*. $k=1$ is IMEX Euler. Ma et al. use $k=4$ but do not print its
coefficients.

## Explicit or linearly implicit nonlinear term

For a nonlinear transport term there are two one-solve-per-step options.
[García-Archilla & Novo (2023)](/sources/garciaarchilla-2023.md) compare them for incompressible
Navier–Stokes with variable-step BDF2, with viscous, pressure and grad-div terms implicit (§2).
Let $\hat u$ (page-local) denote the linear extrapolation of the velocity to the new time.

- **IMEX** (their Eq. (20)): the convection term is fully explicit, evaluated as $b(\hat u,\hat u,\cdot)$.
  The system matrix is fixed while the step size is fixed.
- **Semi-implicit**, i.e. linearly implicit (their Eq. (22)): convection is linearized as
  $b(\hat u,u^{n+1},\cdot)$, an Oseen step with extrapolated advecting velocity. The matrix
  changes every step.

Both start with one IMEX Euler step, which costs no order (Lemma 6). The convergence theory
differs between them:

- **IMEX.** The second-order, viscosity-robust error bound needs a CFL-type condition
  $h/\Delta x^2$ bounded (fixed step: Eq. (44), Thm. 1; variable step: Eq. (86), Thm. 3). Its
  only origin is the explicit nonlinear term, bounded with an inverse inequality (Lemma 3,
  Remark 2). The authors contrast it with DeCaria–Schneier, whose condition bounds
  $h\,\Delta x^{-1}\nu^{-1}$, with $\nu$ here the viscosity (page-local; the registry's $\nu$ is
  the Courant number) (§1, Remark 3).
- **Semi-implicit.** No CFL condition is needed, only a $\nu$-independent smallness of the step
  (Thms. 2, 4).
- **Numerical evidence for the IMEX restriction.** At fixed tolerance, the IMEX step count
  roughly doubles and then triples as the mesh is halved twice, while the semi-implicit count
  stays nearly constant (§4.1, Fig. 5). On the [flow past a cylinder](/benchmarks/flow-past-cylinder.md),
  the IMEX steps coincide for two tolerances on $t\in[1.7,3.7]$, i.e. the CFL-type condition and
  not accuracy limits them (§4.2, Fig. 8).
- **Cost.** The authors conclude that the semi-implicit method costs "not much larger" than the
  IMEX one and has no step restriction (§4.2, §5).

## Linearly implicit multistep methods as IMEX schemes

[Glandon et al. (2022)](/sources/glandon-2022.md) (§5, Eq. (5.1)) observe that a Limm-W method
with no $hJf$ terms is an IMEX multistep method for the splitting $f=(f-J_ny)+J_ny$. Its
explicit coefficients are the $\beta_j$ and its implicit coefficients the sums of the $\beta_j$
and the $J$-coefficients. Its order conditions are those of that IMEX pair. On this basis they
prove order $p$ on problems whose stiffness is linear, with a step bound independent of the
stiffness (Thm. 5.8); see
[linearly implicit multistep methods](/methods/linearly-implicit-multistep-method.md).

## Uniform accuracy for relaxation systems

Ma et al. (2026) apply IMEX-BDF$k$, $k\le4$, to linear hyperbolic relaxation systems
$U_t+AU_x=\frac1\varepsilon QU$, with $U$ the state and $A$, $Q$ constant convection and
relaxation matrices (page-local; $A$ is not a Butcher matrix here). The convection is explicit
and the relaxation implicit, with a Fourier–Galerkin discretization of $N$ modes (page-local). Under Yong's structural stability
condition and a symmetry assumption on the relaxation block, they prove:

- **Uniform stability** (Thm. 3.1) for $h\le c/N^2$, with $c$ (page-local) an unspecified
  constant;
- **Uniform accuracy** (Thm. 3.3, Cor. 3.1): error $O(h^k+N^{-2k})$ with constant independent of
  $\varepsilon$, for well-prepared initial data or when the scheme starts after the
  $O(\varepsilon\log(1/\varepsilon))$ initial layer.

The proof uses the multiplier identities of BDF ([multiplier energy technique](/methods/multiplier-energy-technique.md)).
The implicit relaxation term turns into a telescoping dissipation. On linearized Aw–Rascle–Zhang,
[Broadwell](/benchmarks/broadwell-model.md) and Grad moment systems, the observed orders are 2, 3
and 4 for $\varepsilon=10^{-7},\dots,1$, with no order reduction in the intermediate regime
(Tables 4.1–4.3). The only visible dip is to 1.89–2.02 and 2.90–2.95 at $\varepsilon=10^{-3}$ on
Aw–Rascle–Zhang, which the authors do not discuss. The result generalizes Hu & Shu's theorem for
the Jin–Xin model (§1). It is the subject of
[uniform accuracy for relaxation systems](/results/uniform-accuracy-relaxation-systems.md); see
also [asymptotic-preserving schemes](/definitions/asymptotic-preserving-scheme.md) and the
[hyperbolic relaxation system](/benchmarks/hyperbolic-relaxation-system.md).

Ma et al. motivate the multistep choice with the observation that "many IMEX-RK schemes suffer
from accuracy degeneration when $\varepsilon$ goes to zero" (§1). This is a statement about many
schemes, not about all; see [IMEX Runge–Kutta methods](/methods/imex-runge-kutta.md) and
[order reduction](/definitions/order-reduction.md).

## Step-size control

García-Archilla & Novo (2023, §4) run both BDF2 variants with the variable-order strategy of
Hairer–Wanner for fully implicit BDF. That includes its divided-difference local error
estimator, which they note "corresponds to the fully nonlinear BDF, but, nevertheless, it was
used" for the IMEX and semi-implicit schemes. The estimator's error constant does not account
for the explicit extrapolation, and the authors do not justify the reuse; see
[step-size control](/methods/step-size-control.md).

## Qualifications

- **CFL-type conditions are sufficient conditions from energy proofs.** Both analyses obtain a
  parabolic-type scaling, $h\lesssim\Delta x^2$ (García-Archilla & Novo) or $h\lesssim N^{-2}$
  (Ma et al.), for an explicitly treated transport term. Ma et al.'s tests run with $hN^2$ up to
  about 50 (Broadwell model, $N=100$, $h=5\times10^{-3}$), outside any modest constant, so
  their condition is not observed to be sharp *(compiler check on the arXiv v1)*. García-Archilla & Novo's step counts grow by about 2 and 3
  per mesh halving, and the authors read this as "approaching the factor 4" (Fig. 5). The
  settings differ (Fourier spectral relaxation systems, finite-element Navier–Stokes), so the two
  findings are not in conflict.
- **Uniform accuracy needs prepared data.** Ma et al.'s tests add $O(\varepsilon)$ and
  $O(\varepsilon^2)$ corrections to the initial data for $k=3$ and $k=4$ (§4.1–§4.2). A statement
  that IMEX-BDF is "uniformly accurate" must carry this condition.
- **Terminology.** García-Archilla & Novo reserve "IMEX" for the fully explicit treatment of
  convection and call the linearized one "semi-implicit". Elsewhere both count as IMEX or
  linearly implicit.
- **Version read.** García-Archilla & Novo (2023) and Ma et al. (2026) were read as arXiv v1
  preprints. Glandon et al. (2022) was read as a review manuscript whose supplement was missing.

# Citations

- [Ma et al. (2026)](/sources/ma-2026.md) — §1, §2.2 (Eq. (2.2), Lemma 2.1), Thms. 3.1, 3.3, Cor. 3.1, §4 (Tables 4.1–4.3).
- [García-Archilla & Novo (2023)](/sources/garciaarchilla-2023.md) — §1, §2 (Eqs. (20)–(24)), Lemmas 3–4, 6, Thms. 1–4, Remarks 2–3, §4 (Figs. 5, 8), §5.
- [Glandon et al. (2022)](/sources/glandon-2022.md) — §5 (Eq. (5.1), Thm. 5.8).
