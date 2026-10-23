---
type: Source
title: "Rueda-Ramírez et al. (2022) — Subcell limiting strategies for discontinuous Galerkin spectral element methods"
description: "Unified four-ingredient framework for blending nodal DGSEM with a compatible subcell finite-volume scheme, element-wise or subcell-wise and a priori or a posteriori, with proofs that Pazner's sparse invariant-domain-preserving DG equals the LLF subcell scheme and that the Hennemann subcell metrics solve its conservation condition exactly."
resource: "doi:10.1016/j.compfluid.2022.105627"
source_kind: paper
authors: [Rueda-Ramírez A.M., Pazner W., Gassner G.J.]
year: 2022
venue: "Comput. Fluids 247:105627"
local_file: "/home/stefano/papers/mosaic/weno-teno/2022_Crossref_Computers_amp_Fluids_Rueda-Ramírez_Subcell_limiting_strategies_for_discontinuous_Galerkin_spect.pdf"
tags: [dg, limiting, entropy-stable, positivity, mhd]
timestamp: 2026-10-21T12:00:00Z
---

# Summary

The paper builds a unified framework for robust high-order nodal
[DGSEM](/methods/dgsem.md) on Legendre–Gauss–Lobatto (LGL) nodes. Robustness comes from a convex
blend of the high-order scheme with a compatible low-order finite-volume scheme on the same degrees
of freedom. The framework has four ingredients that can be mixed:

1. **The high-order DGSEM.** It can be standard or split form, using
   [flux differencing](/methods/flux-differencing.md) on a
   [summation-by-parts](/operators/summation-by-parts-operator.md) operator with any symmetric
   two-point volume flux, such as an
   [entropy-conservative or kinetic-energy-preserving flux](/methods/entropy-conservative-flux.md).
2. **A compatible subcell finite-volume scheme.** It treats the LGL nodal values as subcell
   averages. Its subcell normals come from the flux-differencing form, so it is watertight and
   [free-stream preserving](/properties/free-stream-preservation.md) on curvilinear meshes. The
   Riemann solver is free: the [Rusanov flux](/methods/lax-friedrichs-flux.md) or an
   [HLL-type](/methods/hll-riemann-solvers.md) one. The reconstruction is first order or minmod
   [TVD](/definitions/total-variation-diminishing.md).
3. **A blending strategy.** It can be element-wise (one $\alpha$ per element) or subcell-wise (one
   $\alpha$ per subcell interface).
4. **A rule for the blending coefficients.** It can be a priori, with a modal-energy
   [troubled-cell indicator](/definitions/troubled-cell-indicator.md), or a posteriori, with
   FCT/Zalesak-type [convex limiting](/methods/convex-limiting.md) against local bounds,
   Guermond–Popov bar states, or a fraction of the finite-volume solution.

This is [subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md) in general
form. Propositions 1 and 2 prove that Pazner's sparse invariant-domain-preserving DG is the subcell
LLF scheme of Hennemann et al. They also show that the Hennemann subcell metrics solve Pazner's
conservation condition exactly, so no SVD is needed.

The tests, run in [FLUXO](/software/fluxo.md) and [Trixi.jl](/software/trixi-jl.md), show:

- **[KPP](/benchmarks/kpp-rotating-wave.md):** the scheme converges to the entropy solution only
  when the DGSEM is [entropy stable](/properties/entropy-stability.md).
- **[Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md):** subcell blending needs about
  $10^3$ times less low-order method.
- **Bow shock:** a Mach-4 bow shock runs with bar-state bounds.
- **[Mach-2000 jet](/benchmarks/high-mach-astrophysical-jet.md):** the jet runs robustly.
- **GLM-MHD [Orszag–Tang](/benchmarks/orszag-tang-vortex.md):** this case tests the
  [divergence-free magnetic field](/properties/divergence-free-magnetic-field.md) setting through
  divergence cleaning.

Time stepping is Shu and Osher's [SSP-RK3](/methods/ssp-runge-kutta.md); the
[Shu–Osher problem](/benchmarks/shu-osher-problem.md) page cites the paper only through that
attribution, not as a test. The jet is called an extreme benchmark with reference to Zhang and
Shu's positivity-preserving DG ([Zhang–Shu limiter](/methods/zhang-shu-scaling-limiter.md)).
[Kinetic energy preservation](/properties/kinetic-energy-preservation.md) enters only as one
choice of volume flux.

# Version read

The file is arXiv:2202.00576v2 [math.NA] of 22 Feb 2022 (margin stamp on page 1), not the
Computers & Fluids version of record. It has 26 pages, all read, and the equations were checked
against the page images. The acknowledgments print the report number LLNL-JRNL-831293. Page 1
matches the published title and authors, so there is no identity issue. All numbers cited here are
the preprint's.

# Key claims

1. Four ingredients define a family of subcell limiting strategies; existing methods are members of
   it, and mixing them gives new ones. The ingredients are: high-order DGSEM on LGL nodes; a
   compatible subcell finite-volume scheme; element- or subcell-wise convex blending; and a priori
   or a posteriori coefficients. (§2, §4) **Stated**
2. DGSEM on LGL nodes, in standard or split form, can be rewritten exactly in flux-differencing
   (subcell finite-volume) form, eq. (8), with high-order inter-node fluxes (9)–(11). This gives
   local conservation at subelement level (Lax–Wendroff). The fluxes differ from those of Fisher
   & Carpenter because the surface terms are transformed too. (§2.1) **Derived**
3. The inner fluxes follow recursively:
   $\hat f^{\mathrm{DG}}_{(0,1)j}=-F^{\mathrm{vol}}_{0j}$ and
   $\hat f^{\mathrm{DG}}_{(i,i+1)j}=\hat f^{\mathrm{DG}}_{(i-1,i)j}-F^{\mathrm{vol}}_{ij}$ for
   $i=1,\dots,N-1$, with $F^{\mathrm{vol}}$ the first-direction volume term. (§2.1) **Derived**
4. The Hennemann et al. subcell normals (14) give a compatible, watertight subcell finite-volume
   discretization on curvilinear meshes. It is free-stream preserving and satisfies the discrete
   subcell metric identities (15). (§2.2) **Stated** (proof in Hennemann et al.)
5. Blending an entropy-stable DGSEM element-wise with a higher-order entropy-stable finite-volume
   scheme (minmod TVD reconstruction of scaled entropy variables) stays entropy stable, provided
   both schemes use the same surface terms. (§2.2) **Stated**
6. Entropy dissipation has been proved only for element-wise blending (Euler and MHD); the proof for
   subcell-wise blending is "still missing". (§4 item (2)) **Stated**
7. The a priori coefficient is a logistic function (20) of the modal-energy indicator (19):
   - sharpness $s=9.21024$, so that $\alpha(\mathbb E=0)=10^{-4}$;
   - threshold $\mathbb T(N)=0.5\cdot10^{-1.8(N+1)^{0.25}}$ (21);
   - optional cap $\alpha\le\alpha_{\max}$ (22).

   It needs only previous-step data and is cheap. It is heuristic, with user parameters. (§2.4)
   **Stated**
8. For a posteriori element-wise blending, each element takes the maximum of its nodal
   coefficients. Linear constraints are solved in closed form from (26). Nonlinear convex
   constraints need a Newton–bisection or Newton–secant solve. (§2.4) **Stated**
9. Subcell-wise a posteriori blending works as follows:
   - for linear bounds it uses a Zalesak-type limiter (28);
   - for convex nonlinear bounds it solves $2d$ nonlinear problems per node with the provisional
     update (29), and $\Gamma=2d$ guarantees the bound;
   - the interface coefficient is $\alpha_{(i,m)j}=\max(\tilde\alpha_{ij},\tilde\alpha_{mj})$.

   Subcell-wise limiting is stricter than element-wise limiting, because each interface must meet
   the bound on its own. (§2.4, eqs. (28)–(29)) **Stated**
10. **Proposition 1.** The subcell finite-volume scheme with first-order reconstruction and the
    Rusanov flux equals Pazner's low-order sparse invariant-domain-preserving scheme,
    $m_i\dot u_i=\sum_{j\in N(i)}\hat c_{ij}\cdot f_j+\sum_{j\in N(i)}\hat d_{ij}(u_j-u_i)$.
    (§3, eqs. (30)–(33)) **Proved**
11. The factor $1/2$ in $\hat c$ corresponds to the entries of Pazner's sparsified derivative matrix
    $\widehat D_{1D}$ (34). The other factors of $\hat c$ are Pazner's modified metric terms. (§3)
    **Derived**
12. **Proposition 2.** The Hennemann subcell metrics (14) are exact analytic solutions of Pazner's
    conservation condition $\sum_{j\in N(i)}\hat c_{ij}=\vec0$ (35), so Pazner's SVD minimization
    is unnecessary. (§3, eqs. (35)–(36)) **Proved**
13. The equivalence allows two extensions, both stated without demonstration:
    - sparse invariant-domain-preserving DG with split-form (entropy-stable or
      kinetic-energy-dissipative) volume integrals;
    - replacing the low-order LLF flux by HLLE or HLLEM, which keep density and pressure positive.

    With HLLE or HLLEM, however, the bar-state bounds no longer apply directly. (§4 items (1),
    (3)) **Stated**
14. Rueda-Ramírez & Gassner showed that split-form DGSEM with the Chandrashekar flux plus subcell
    finite volumes is more stable than standard DGSEM, and needs less blending, on under-resolved
    turbulence with shocks. (§4 item (1)) **Stated** (cited)
15. Minmod reconstruction of primitive variables can guarantee monotone solutions and enforce
    positivity. Minmod is not defined at element boundaries, so the scheme falls back to first
    order in the boundary subcells. (§4 item (4), §5.2.3, Fig. 1b) **Stated**
16. KPP ($N=3$, $32^2$–$256^2$ elements, $t=1$, element-wise shock capturing with
    $\alpha_{\max}=0.5$):
    - standard DGSEM gives clean but **nonentropic** solutions;
    - entropy-stable DGSEM (an entropy-conservative volume flux for $\eta=\tfrac12u^2$, LLF at the
      surfaces) converges to the entropy solution;
    - the nonentropic structures of the standard scheme trigger the shock sensor.

    (§5.1, Figs. 2–3) **Shown**
17. Split-form DGSEM with that volume flux and an LLF surface flux satisfies a discrete entropy
    inequality, and "will therefore converge to the unique entropic solution". (§5.1) **Stated**
    (convergence is asserted; the evidence is numerical)
18. The DG cell entropy inequality of Jiang & Shu for the square entropy needs exact volume and
    surface integration. That is not feasible for the non-polynomial KPP flux. (§5.1) **Stated**
19. Kelvin–Helmholtz ($N=7$, $64^2$ elements, $t=10$, bounds $\rho\ge0.1\rho^{\mathrm{FV}}$ and
    $p\ge0.1p^{\mathrm{FV}}$):
    - standard and split-form DGSEM both need positivity limiting;
    - the maximum blending coefficients are similar for the two strategies (peaks about 0.025);
    - subcell-wise blending adds about **three orders of magnitude** less low-order method (mean
      coefficient about $10^{-9}$–$10^{-8}$ against $10^{-6}$–$10^{-5}$);
    - the two solutions differ visibly by $t=6.7$.

    (§5.2.1, Figs. 4–6) **Shown**
20. Bow shock (Mach 4, $\gamma=1.4$, $N=5$, curved third-order mesh, subcell-wise bar-state bounds,
    first-order LLF finite volumes):
    - the bounds hold to machine precision, thanks to the LLF/graph-Laplacian equivalence;
    - the shock is sharp even inside an element;
    - the mean blending is $11.03\%$ on 864 elements and $9.50\%$ on 1536 elements.

    (§5.2.2, Fig. 7) **Shown**
21. The density bounds (47) from bar states and the local minimum principle (48) on
    $\phi=e\rho^{1-\gamma}$ together guarantee positive density and pressure. Bound (48) also
    guarantees a discrete entropy inequality. (§5.2.2) **Stated**
22. Astrophysical jet (Mach about 2000; 2156.91 with respect to the jet sound speed; $N=3$, $256^2$
    elements, $t=10^{-3}$):
    - the run is robust with both blending strategies;
    - resolution improves from first-order LLF to first-order HLLE to second-order HLLE;
    - subcell-wise blending captures shocks more sharply than element-wise blending.

    (§5.2.3, Figs. 8–9) **Shown**
23. Low-order schemes with second-order reconstruction or HLLE are not guaranteed to satisfy the
    bar-state bounds. The bounds are kept "in the absence of better bounds", and the limiter
    returns the solution closest to them. (§5.2.3) **Stated**
24. The conservative form of GLM-MHD is used because it fits the framework, although proving entropy
    stability needs the non-conservative form. (§5.3) **Stated**
25. Orszag–Tang ($N=3$, $256^2$ elements, $t=1$, subcell-wise density bounds from the low-order
    stage solution):
    - the bounds can always be met, because the low-order schemes are monotone in the primitive
      variables;
    - second-order finite volumes give looser bounds, less limiting and more small-scale
      structure than first-order ones.

    (§5.3.1, Figs. 10–11) **Shown**
26. Element-wise blending is simpler and allows a global entropy estimate. It is typically more
    dissipative than subcell-wise blending. (§6) **Stated**
27. All tests use the Shu–Osher three-stage third-order SSP Runge–Kutta method with CFL $=0.5$.
    The blending coefficients are recomputed at every stage. (§5) **Stated**

# Printed slips

- **§5.3.** "The conserved quantities of the GLM-MHD system are $u=[\rho,\rho\vec v,\rho E]^T$":
  the vector leaves out $\vec B$ and $\psi$, although the flux (51) has rows for them.
- **§5.2.2.** "third-order hexahedral elements" for a two-dimensional quadrilateral mesh.
- **§2.1, recursive formula.** The last term is printed $F^{Vol}_{ij}$, without the direction
  superscript (1) of eq. (10).
- **Wording slips:**
  - §1: "identifies a troubled elements";
  - §3: "within the collection or proposed";
  - §2.4: stray periods in the headings;
  - §2.4: "which be recast".
- **Ref. [60].** The page range is printed as "531–531".

# Notation map

| Rueda-Ramírez et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\overleftrightarrow f(u)$ | $f^{(d)}(u)$ | block vector of Cartesian fluxes |
| $N$ | $N$ | DG degree; LGL nodes $i,j=0,\dots,N$ |
| $\omega_i$, $\omega_{ij}=\omega_i\omega_j$ | $\mathsf w_i$, $\mathsf w_i\mathsf w_j$ | LGL weights, also the subcell widths in reference space |
| $Q_{ij}=\omega_i\ell'_j(\xi_i)$, $B$ | $Q=MD$, $B$ | SBP stiffness and boundary matrices |
| $\bar S=Q-B$, $S=2Q-B$ | — | volume matrices of the standard and split forms |
| $J$, $Ja^n_m$, $\vec a^m$ | $J$, $Ja^{(d)}$ | metric terms |
| $\overleftrightarrow f^*(\cdot,\cdot)$ | $f^{\mathrm{vol}}(\cdot,\cdot)$ | symmetric two-point volume flux |
| $\hat f_{(0,L)j}$, $\hat f_{(N,R)j}$ | $\hat f_L$, $\hat f_R$, values of $h(u^-,u^+)$ | surface numerical flux at the left and right element faces, as on the DGSEM page |
| $F^{Vol(1)}_{ij}$ | $F^{\mathrm{vol}}_{ij}$ | volume term in the first direction, as on the DGSEM and flux-differencing pages (page-local) |
| $\tilde f^1_{mj}$, $\tilde f^{1*}_{(i,m)j}$ | $\tilde f_m$, $\tilde f^{\mathrm{vol}}_{(i,m)}$ | contravariant flux and two-point flux with averaged metrics (DGSEM page) |
| $\hat f^{DG}_{(i,i+1)j}$, $\hat f^{FV}_{(i,m)j}$ | kept | high-order and low-order subcell fluxes |
| $\vec n_{(i,i+1)j}$ | $n_{(i,i+1)j}$ | subcell normals, metric-weighted and unnormalized (page-local on the free-stream page) |
| $\alpha$, $\alpha_{(a,b)}$ | $\alpha$ | blending coefficient: 0 is DG, 1 is FV |
| $\lambda_{(a,b)}$ | $a_{(a,b)}$ | maximum wave speed between nodes $a$, $b$ |
| $\bar u_{(a,b)}$ | kept | Guermond–Popov bar state; **collision** with the cell-average bar $\bar u_i$ |
| $\epsilon$, $\hat\epsilon_j$ | — | indicator quantity and its modal coefficients; **collision** with the WENO regularization $\epsilon$ |
| $\mathbb E$, $\mathbb T(N)$, $s$ | kept | modal energy, threshold, sharpness; $s$ is also the RK stage index in (45) |
| $\beta=0.1$ | $\beta_{\mathrm{FV}}$ | fraction of the FV solution in the positivity bound (43); **collision** with $\beta_k$ |
| $U=\tfrac12u^2$, $v$, $\psi$ (KPP) | $\eta$, $w$, $\psi$ | entropy, entropy variable, flux potential |
| $\hat f^{EC}$ | $f^{\mathrm{ec}}$ | |
| $\psi$ (MHD) | $\psi_{\mathrm{GLM}}$ | GLM cleaning field |
| $\rho E$, $E$ (specific) | $E$, $E/\rho$ | the source's $E$ is per unit mass |
| $\phi=e\rho^{1-\gamma}$ | kept | modified specific entropy; $s=\ln(p\rho^{-\gamma})$ as in the registry |
| $\hat c_{ij}$, $\hat d_{ij}$, $m_i$ | kept | Pazner's graph coefficients, graph viscosity, lumped mass |
| $N(ij)$ | kept | five-point low-order stencil, not the DG degree |

# Reference list

The paper prints 72 references in numbered style [n], in order of first citation. The list is
merged complete into the [bibliography](/bibliography.md) with `citedby` set to
`ruedaramirez-2022`. Notes on individual items:

- [4] has no year and is keyed by the citing year;
- [26] has only a conference name (WCCM-ECCOMAS2020) for its year;
- [24] has an article number but no volume, and [22] has neither volume nor pages;
- [49] and [65] have no venue;
- [61] is a workshop web page and [21] an arXiv preprint;
- three pairs share an author and year and take suffixes in printed order: `sonntag-2017`/`-b`,
  `fisher-2013`/`-b` and `guermond-2016`/`-b`.

There are no printed duplicates.

# Pages created or updated

Chunk 1 (2026-10-21), cited further in chunks 2–6 (2026-10-22/23). This source is cited on:

* [Bound preservation](/properties/bound-preservation.md)
* [Convex limiting and invariant-domain-preserving schemes](/methods/convex-limiting.md)
* [Discontinuous Galerkin method](/methods/discontinuous-galerkin.md)
* [Discontinuous Galerkin spectral element method (DGSEM)](/methods/dgsem.md)
* [Divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
* [Entropy stability](/properties/entropy-stability.md)
* [Entropy-conservative and kinetic-energy-preserving two-point fluxes](/methods/entropy-conservative-flux.md)
* [Flux differencing and split-form DG](/methods/flux-differencing.md)
* [FLUXO](/software/fluxo.md)
* [Free-stream preservation](/properties/free-stream-preservation.md)
* [High-Mach astrophysical jets](/benchmarks/high-mach-astrophysical-jet.md)
* [HLL-family approximate Riemann solvers](/methods/hll-riemann-solvers.md)
* [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)
* [Kinetic energy preservation](/properties/kinetic-energy-preservation.md)
* [KPP rotating wave](/benchmarks/kpp-rotating-wave.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [Lax–Wendroff theorem](/results/lax-wendroff-theorem.md)
* [Local conservation is equivalent to a flux form](/results/local-conservation-flux-form.md)
* [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Subcell finite-volume limiting for DG](/methods/subcell-finite-volume-limiting.md)
* [Summation-by-parts operator](/operators/summation-by-parts-operator.md)
* [Total variation diminishing (TVD) and slope limiters](/definitions/total-variation-diminishing.md)
* [Trixi.jl](/software/trixi-jl.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
