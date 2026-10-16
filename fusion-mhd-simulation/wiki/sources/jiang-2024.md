---
type: Source
title: "Jiang et al. (2024) — Development of a gyrokinetic-MHD energetic particle simulation code. I. MHD version"
description: "Presents GMEC_I, the linear reduced-MHD foundation of the GMEC gyrokinetic-MHD hybrid code: an initial-value solver in field-aligned coordinates with high-order finite differences, RK4, a new simple shifted metric and C++20 compile-time symbolic equation generation, benchmarked against the MAS eigenvalue code on ideal ballooning, drift-ballooning and tearing modes."
resource: "doi:10.1063/5.0203252"
source_kind: paper
authors: [Jiang P.Y., Liu Z.Y., Liu S.Y., Bao J., Fu G.Y.]
year: 2024
venue: "Phys. Plasmas 31:073904"
local_file: "/home/stefano/papers/mosaic/fusion-mhd-simulation/2024_Crossref_Physics_of_Plasmas_Jiang_Development_of_a_gyrokinetic-MHD_energetic_particle_simulati.pdf"
tags: [reduced-mhd, hybrid-kinetic, energetic-particles, finite-differences, time-integration, ballooning, tearing, code, verification, benchmark]
timestamp: 2026-10-16T00:00:00Z
---

# Summary

The paper presents GMEC_I, the fluid-only foundation of the GMEC
gyrokinetic-MHD code family that Fu's group at Zhejiang University is
building for energetic-particle-driven Alfvén instabilities in burning
plasmas. GMEC_I is an initial-value code that solves a hierarchy of three
*linearized* reduced-MHD models without equilibrium flow: (A) zero-$\beta$
vorticity and parallel Ohm's law, (B) finite $\beta$ with a pressure
equation in the slow-sound approximation, (C) finite $\beta$ with ion and
electron diamagnetic terms (drift ordering, gyroviscous cancellation). The
domain is an annulus in field-aligned coordinates built on Boozer
coordinates, discretized by arbitrary-order finite differences in all three
directions (default five-point stencils, biased near boundaries); time
integration is RK4 with the resistive and numerical-diffusion terms implicit.
The numerical instability at the twist-shift boundary, caused by the
discontinuity of the integrated local shear, is removed either by Scott's
shifted metric or by a new "simple shifted metric" whose local grids coincide
with the Boozer toroidal angle, so that a particle-in-cell module can push
markers on the field grid without field interpolation. The discrete
equations are generated at compile time by a C++20 metaprogramming
"Compile-time Symbolic Solver" (CSS), whose coefficient merging makes the
parallel-current evaluation 6× faster. Parallelism is MPI (decomposition in
the parallel coordinate only) plus Intel TBB within a node. Benchmarks
against the eigenvalue code MAS: [ideal ballooning](/definitions/ballooning-mode.md)
within 4% (including second stability), drift-ballooning within 1% in
frequency and 20% in growth rate, and the $m/n=2/1$
[tearing mode](/definitions/tearing-mode.md) recovering
$\gamma\propto\eta^{3/5}$ below $10^{-6}$ Ω m.

# Key claims

1. **Linear model hierarchy** (§II). Three reduced-MHD models (A, B, C), all
   linearized without equilibrium flow in this paper; fluid nonlinearity is
   deferred. Stated.
2. **Model provenance** (§II A–C). Model A is Strauss' reduced MHD "except
   for additional resistivity term"; Model B keeps the
   $\nabla\cdot\mathbf v_E$ compressibility in the pressure equation,
   "consistent with Fu and Berk"; Model C's ion diamagnetic term follows from
   gyroviscous cancellation (Hazeltine–Kotschenreuther–Morrison), and the ion
   and electron diamagnetic drifts cancel at leading order in the pressure
   equation. Stated; no derivation shown.
3. **Isothermal electrons** (§II C). $\nabla_\parallel T_e=0$ reduces the
   electron pressure gradient to $T_{e0}\nabla_\parallel n_e$, with $n_e$ from
   a density equation. Stated (Snyder & Hammett 2001).
4. **Boundary instability** (§III A, §VIII, Figs. 10–11). Without a shifted
   metric, field-aligned coordinates develop a numerical instability at the
   twist-shift boundary because the integrated local shear is not periodic and
   the radial covariant basis vector is discontinuous there; for the $n=20$
   ideal ballooning case it grows at $\gamma=0.21\,v_A/R_0$ within about
   $50R_0/v_A$. Shown.
5. **Diffusion cure is biased** (§VIII, Fig. 12). A numerical vorticity
   diffusion suppresses the instability only above a normalized coefficient
   $5\times10^{-8}$, and then lowers the physical growth rate to
   $0.081\,v_A/R_0$, 7% below $0.087$. Shown.
6. **Both shifted metrics cure it** (§VIII). Scott's and the simple shifted
   metric remove the instability and give the same
   $\gamma\approx0.087\,v_A/R_0$. Shown.
7. **Simple shifted metric** (§III C, Eqs. 36–38). Choosing the shift as
   minus the integrated shear makes the local binormal coordinate equal the
   toroidal angle, so field grid points coincide with toroidal (Boozer) grid
   points and particles can be pushed "using the same grids without
   interpolation"; the price is a non-zero radial–binormal metric element.
   The two metrics coincide only for orthogonal toroidal coordinates.
   Derived.
8. **Coefficient merging** (§VII B). CSS precomputes products of stencil
   coefficients and equilibrium metric factors, one multiplication per offset
   variable, which "can be proved" minimal (no proof); the parallel-current
   evaluation becomes "6 times faster than the usual method" at `-O2`
   (traditional method ≈60 multiplications per point). Shown (speed-up),
   Stated (minimality).
9. **Scaling** (§IV E, Figs. 6–7). Strong scaling of the ballooning case on
   $1024\times256\times64$ reaches ≈60% efficiency at 32 nodes (1792 cores,
   Xeon Gold 6348) relative to the smallest core count; at fixed 112 cores
   efficiency rises with grid size. That MPI+TBB outperforms pure MPI is
   Attributed (Refs. 15–17), with no in-paper comparison.
10. **Ideal ballooning vs MAS** (§IX A, Figs. 16–18). Maximum growth-rate
    difference <4% over $n=4$–20 and over central pressure 0.4%–2% of
    $B^2/2\mu_0$, with second-stability behaviour; mode structures and
    harmonic peaks at rational surfaces agree. Shown.
11. **Drift-ballooning vs MAS** (§IX B, Figs. 20–23). $n$ scan to 16:
    differences <1% in $\omega$ and <20% in $\gamma$; the diamagnetic term
    stabilizes high $n$ and twists the mode structure. Shown; the paper calls
    the 20% gap "agree well".
12. **Tearing vs MAS** (§IX C, Fig. 28). $m/n=2/1$, $R_0=10$ m, $a=1$ m:
    both codes follow $\gamma\sim\eta^{3/5}$ for $\eta<10^{-6}$ Ω m and agree
    at higher $\eta$, where both fall below the scaling. Shown; no reference
    given for the scaling.
13. **Cost** (§IX A, C). $n=20$ ballooning: 17 s on 448 cores; tearing at
    $\eta=10^{-7}$ Ω m: 10 min on 448 cores. Shown.
14. **Residual discrepancies** (§IX A). Attributed to MAS neglecting some
    equilibrium derivatives and using Boozer coordinates with FFTs, against
    field-aligned finite differences retaining all equilibrium derivatives in
    GMEC_I. Stated.

# Models and numerics

All perturbations are linear ($\delta$), equilibrium quantities carry the
subscript 0; $\boldsymbol\kappa_0\equiv\mathbf b_0\cdot\nabla\mathbf b_0$ is
written out below as the field-line curvature.

**Model A** (Eqs. 1–5), zero $\beta$:

$$\begin{aligned}
\frac{\partial\delta\varpi}{\partial t}&=\nabla\times(\delta A_\parallel\mathbf b_0)\cdot\nabla\Big(\frac{\mu_0j_{\parallel0}}{B_0}\Big)+\mathbf B_0\cdot\nabla\Big(\frac{\mu_0\delta j_\parallel}{B_0}\Big),\qquad
\frac{\partial\delta A_\parallel}{\partial t}=-\mathbf b_0\cdot\nabla\delta\Phi-\eta\,\delta j_\parallel,\\
\delta\varpi&=\nabla\cdot\Big(\frac{1}{v_A^2}\nabla_\perp\delta\Phi\Big),\qquad
\delta j_\parallel=-\frac{1}{\mu_0B_0}\nabla\cdot\Big(B_0^2\nabla_\perp\frac{\delta A_\parallel}{B_0}\Big),\qquad
j_{\parallel0}=\frac{1}{\mu_0}\mathbf b_0\cdot\nabla\times\mathbf B_0 .
\end{aligned}$$

**Model B** (Eqs. 6–8), finite $\beta$, slow-sound approximation: the
vorticity equation gains $\frac{2\mu_0}{B_0}\mathbf b_0\times(\mathbf b_0\cdot\nabla\mathbf b_0)\cdot\nabla\delta p$,
Ohm's law is unchanged, and

$$\frac{\partial\delta p}{\partial t}=-\frac{1}{B_0}\mathbf b_0\times\nabla\delta\Phi\cdot\nabla p_0-\frac{2\Gamma p_0}{B_0}\mathbf b_0\times(\mathbf b_0\cdot\nabla\mathbf b_0)\cdot\nabla\delta\Phi .$$

**Model C** (Eqs. 9–12): the vorticity equation gains the ion diamagnetic
term (the ion diamagnetic frequency operator, density plus temperature parts,
applied to $\delta\varpi$); Ohm's law gains the electron-pressure terms
$\frac{T_{e0}}{en_{e0}}\mathbf b_0\cdot\nabla\delta n_e+\frac{T_{e0}}{en_{e0}B_0}\nabla\times(\delta A_\parallel\mathbf b_0)\cdot\nabla n_{e0}$;
the pressure equation is that of Model B; and
$\partial_t\delta n_e=-\frac{1}{B_0}\mathbf b_0\times\nabla\delta\Phi\cdot\nabla n_{e0}$.
The diamagnetic frequencies are printed in Gaussian form (with $c$) inside an
SI system (Citations).

**Coordinates** (§III). Straight-field-line toroidal coordinates
$(\psi,\theta,\zeta)$, usually Boozer, with $2\pi\psi$ the poloidal flux (the
registry's per-radian $\psi$). Field-aligned coordinates
$x=\psi-\psi_0$, $y=\theta$, $z=\zeta-z_0(\psi,\theta)$, where $z_0$ is the
poloidal integral of the local field-line pitch
$\mathbf B_0\cdot\nabla\zeta/\mathbf B_0\cdot\nabla\theta$ (which reduces to
$q$ in straight-field-line coordinates); its radial derivative is the
integrated local shear, which reduces to $q'(\theta-\theta_0)$. Then
$\partial_y$ is the parallel derivative and the twist-shift condition is
$f(x,y+2\pi,z)=f(x,y,z+2\pi q)$ (Eq. 26). Scott's shifted metric
introduces, at each $y_i$, a local $z'=z-\alpha(x)$ with $\alpha'$ chosen so
that the radial–binormal contravariant metric vanishes; the parallel
difference then needs interpolation in $z$, done with 1D B-splines of
arbitrary order during the ghost update (§IV F). The simple shifted metric
takes $\alpha'$ equal to minus the integrated shear, giving $z'=\zeta$.

**Discretization** (§IV B). Finite differences of arbitrary order and
stencil (default five points per dimension), biased at Dirichlet/Neumann
boundaries, ghost points for periodic and interpolated-periodic boundaries.
All equilibrium derivatives are precomputed externally and stored.
$\delta\Phi$ comes from the 2D (radial–binormal) Poisson problem, with
$\partial_y\delta\Phi\to0$, solved by PARDISO (printed "PARSIDO") with TBB on
one node; its full expansion has 18 terms, that of $\delta j_\parallel$ 48.

**Time integration** (§IV D). Explicit RK4; the resistive term and the
vorticity numerical diffusion $D\nabla\cdot\nabla_\perp\delta\varpi$ are
solved fully implicitly, with $\delta j_\parallel=0$ as boundary condition of
the implicit Ohm's-law solve. $D=0$ for ballooning, $7.0\times10^{-10}$
(normalized) for tearing.

**Boundary conditions** (Eq. 45). Ideal conductor at both radial
boundaries: $\delta j_\parallel=0$, $\delta\varpi=0$, $\delta\Phi=0$,
$\partial_\psi\delta p=0$, $\partial_\psi\delta n_e=0$. In $y$: periodic with
twist-shift interpolation, or plain periodic with a shifted metric; periodic
in $z$.

**CSS** (§V, §VII). C++20 template metaprogramming expands vector equations
into components with arbitrary-order, arbitrary-offset differences, merges
homogeneous terms, assembles implicit and Poisson matrices and emits
"zero-overhead" run-time code; scheme, order, boundary conditions and metric
type are compile-time template parameters, so changing them requires
recompiling. Details are deferred ("reported elsewhere").

**Parallelism and I/O** (§IV E). Equilibrium replicated per MPI rank;
perturbed fields decomposed in $y$ only (the Poisson solve couples $x$, $z$);
ghost exchange with MPL (a C++17 MPI wrapper); Intel TBB tasks for 3D loops;
MPI parallel I/O; JSON input. Nodes: 2× Xeon Gold 6348 (28 cores). No GPU.

**Equilibrium input** (§VI C, App. C–D). MATLAB scripts read VMEC
(transformed to Boozer after Hirshman) or DESC (which supplies
high-precision derivatives).

**Diagnostics and units** (§VI D, App. B). Growth rates are measured on the
field amplitude, half the rate of the $\mathbf E\times\mathbf B$ kinetic
energy; frequencies by FFT or peak spacing. $\mu_0$ is kept explicit; lengths
in the axis major radius, velocities in the axis $v_A$, pressure in
$B^2/2\mu_0$.

# Tests and results

| Case | Setup | Result |
|---|---|---|
| Boundary instability (§VIII) | $n=20$ ideal ballooning, no shifted metric | $\gamma=0.21\,v_A/R_0$ at the $y$ boundary; diffusion $\ge5\times10^{-8}$ needed, giving 0.081; both shifted metrics with $D=0$ give 0.087 |
| Ideal ballooning, Model B (§IX A) | VMEC, $R_0=2.763$ m, $a=1$ m, $\psi_t=0.5$ Wb/rad (axis $B\approx1$ T); $q=2.1+0.8333\psi_N+3.8889\psi_N^2$ ($q=4$ at $\psi_N=0.6$); erf pressure step at 0.6; $\psi_N\in[0.3,0.9]$; $256\times64\times16$ over 1/20 torus | $\gamma$ ≈0.062 ($n=4$) to ≈0.086 (GMEC) / 0.0835 (MAS) at $n=20$; pressure scan peaks near 0.7–0.8% then falls (second stability); max difference <4%; 17 s on 448 cores |
| Convergence (Fig. 14) | $n=20$, central pressure 0.8% | $\gamma$ varies by ≈$2\times10^{-5}$ over $\Delta t=10^{-3}$–$10^{-1}\,R_0/v_A$; grid doubling 0.08645 → 0.0871 (≈0.8%) |
| Drift-ballooning, Model C (§IX B) | same equilibrium, $n_0=10^{19}$ m⁻³ with erf density step | $n=10$: $\gamma=0.066$, $\omega\approx0.064\,v_A/R_0$; $\gamma$ peaks ≈0.083 at $n\approx6$, ≈0.02 at $n=16$; $\omega$ <1%, $\gamma$ <20% (largest gap at $n=12$–16, by eye) |
| Tearing $m/n=2/1$, Model A (§IX C) | DESC, $R_0=10$ m, $a=1$ m, $q_0=1.75$, edge $q=2.5$, $q=2$ at $\psi_N=0.542$; $\psi_N\in[10^{-3},0.95]$; $256\times64\times16$; $\Delta t=0.05R_0/v_A$; $\eta=10^{-7}$–$10^{-4}$ Ω m | $\eta=10^{-7}$: $\gamma=0.422\times10^{-3}\,v_A/R_0$ (10 min, 448 cores); $\eta^{3/5}$ below $10^{-6}$ Ω m, GMEC slightly below MAS at high $\eta$ |
| Strong scaling (Figs. 6–7) | $1024\times256\times64$ | ≈60% at 1792 cores vs ≈56; at 112 cores ≈60% ($128\times32\times8$) to ≈100% ($\ge384\times96\times24$) |

# Notation map

| Jiang et al. (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\psi$ ($2\pi\psi$ = poloidal flux) | $\psi$ | same per-radian convention; figures' $\psi$, $\Psi$, $\psi_n$ are $\psi_N$ |
| $\psi_T$ | $\psi_t$ | |
| $\rho=\sqrt{\psi_T}$ (DESC) | $s$ | **collision:** registry $\rho$ is mass density |
| $\theta$ ($\theta_V,\theta_B,\theta_D$) | $\theta$ (VMEC, Boozer, DESC angle stated) | |
| $\xi$, $\phi$, $\phi_B$ (toroidal angle) | $\zeta$ | **collision:** printed $\phi$ is also the potential |
| $\delta\phi$ | $\delta\Phi$ | |
| $(x,y,z)$, $(x',y',z')$ | $x$, $y$, $z$ (primes for local shifted coordinates) | same roles as the registry |
| $\nu$ (field-line pitch) | words | **collision:** registry $\nu$ is viscosity |
| $z_0$, $I$ (integrated shear), $\alpha$, $M$ | words | **collision:** $I$ is also the Boozer covariant poloidal component (Eq. C9) |
| $g^{ij}$, $g_{ij}$, $J$ (Jacobian) | words | **collision:** $J$ vs current density $\mathbf J$ |
| $\delta\omega$ | $\delta\varpi$ | **collision:** registry $\omega$ is a frequency |
| $\delta A_\parallel$ | $\delta A_\parallel$ | |
| $\delta J_\parallel$, $\delta j_\parallel$, $J_{\parallel0}$ | $\delta j_\parallel$, $j_{\parallel0}$ | |
| $P$, $\delta P$, $P_0$ | $p$, $\delta p$, $p_0$ | $P_0$ also the central-pressure parameter (normalized by $B^2/2\mu_0$), and printed as "$\beta$" |
| $\gamma$ (Eqs. 8, 11) | $\Gamma$ | **collision:** undefined adiabatic index vs growth rate |
| $\gamma$, $\gamma_\phi$, $\gamma_E$, $\omega$ | $\gamma$ (amplitude rate), words, $\omega$ | |
| $\boldsymbol\kappa=\mathbf b_0\cdot\nabla\mathbf b_0$ | written out | **collision risk** with $\kappa_\parallel$, $\kappa_\perp$ |
| $\eta_\parallel$ | $\eta$ | |
| $D$, $\bar D$ | words (numerical vorticity diffusion) | **collision risk** with $D_\parallel$, $D_\perp$ |
| $\omega_{*p,i}$, $\omega_{*n,i}$, $\omega_{*T,i}$ | words (ion diamagnetic frequency operator) | not in the registry |
| $n_{e0}$, $T_{e0}$, $n_{i0}$, $T_{i0}$, $Z_i$ | $n_{e}$, $T_e$, $n_i$, $T_i$, $Z$ | |
| $\mathbf B_0$, $B_0$, $\mathbf b_0$ | $\mathbf B$, $B$, $\mathbf b$ (equilibrium) | $B_0$ is also the normalization field |
| $v_A$, $t_A=R_0/v_A$ | $v_A$, $\tau_A$ | length $R_0$ |
| $E$ (Eq. 49) | $W_{\mathrm{kin}}$ density | **collision:** vs electric field |
| $C_p$, $C_{p,q}$ | words (stencil coefficients) | |
| $g(\psi)$ (Boozer covariant toroidal component) | $F$ | **collision:** vs metric $g$ |

# Pages created or updated

Chunk 1 (2026-10-16) created every page of the bundle; chunk 2 (2026-10-16) extended many. This source is cited on:

* [Ballooning mode](/definitions/ballooning-mode.md)
* [BOUT++](/software/bout-plus-plus.md)
* [CLT–M3D-C1 tearing and resistive-kink benchmark](/benchmarks/clt-m3d-c1-benchmark.md)
* [DESC](/software/desc.md)
* [Divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
* [Field-aligned coordinates, twist-shift condition and shifted metric](/methods/field-aligned-coordinates.md)
* [GMEC](/software/gmec.md)
* [Hybrid kinetic-MHD models](/methods/hybrid-kinetic-mhd.md)
* [Implicit time integration and preconditioned Krylov solvers for nonlinear MHD](/methods/implicit-time-integration.md)
* [Linear MHD eigenvalue codes](/methods/linear-mhd-eigenvalue-codes.md)
* [Reduced MHD for tokamaks](/methods/reduced-mhd.md)
* [Resistive tearing mode](/definitions/tearing-mode.md)
* [Symbolic derivation and automatic discretization of MHD operators](/methods/symbolic-code-generation.md)
* [Three-dimensional inverse equilibrium solvers](/methods/inverse-equilibrium-solvers.md)
* [VMEC](/software/vmec.md)

# Citations

1. `/home/stefano/papers/mosaic/fusion-mhd-simulation/2024_Crossref_Physics_of_Plasmas_Jiang_Development_of_a_gyrokinetic-MHD_energetic_particle_simulati.pdf`
   * **Version.** Publisher version of record (AIP, CC BY 4.0): AIP cover
     page (PDF p. 1) and article pp. 073904-1 to -17; submitted 11 February
     2024, accepted 6 April 2024, online 11 July 2024.
   * **Identity.** doi:10.1063/5.0203252, checked on Crossref: Phys.
     Plasmas vol. 31, issue 7, article 073904, published-print 2024-07,
     five authors in the same order, reference count 22. Part II is
     `liu-2024`; the FP3D paper by Jiang, Feng, Yu & Fu (Phys. Plasmas
     31:023906) is the distinct key `jiang-2024-b`.
   * **How read.** Full text including Apps. B–D; equations read from the
     typeset pages. Plot values are the reader's approximate readings.
   * **Recorded as printed.**
     * Tearing $q$ profile, Eq. 60: the printed
       $q_l=\sqrt{(q_e/q_0)^2-1}$ gives $q_l=1.0202$, $q(\psi_N=1)=2.450$ and
       $q=2$ at $\psi_N=0.564$; Fig. 24 shows $q(1)=2.5$ and $q=2$ at 0.542,
       which is what $q_l=[(q_e/q_0)^2-1]^{-1/2}=0.9802$ gives (compiler's
       check). The printed formula is inverted relative to the figure.
     * Ballooning reference surface: §IX A says the maximum pressure gradient
       and $q_c=4$ are at $\psi=0.5$; Eq. 56 and Fig. 13 use 0.6, where
       $q=4.0$ ($q(0.5)=3.49$).
     * Tearing inner boundary: text $10^{-3}$, Fig. 24 caption 0.01, gray
       region labelled from 0. Fig. 24 caption mentions a pressure profile
       that the case does not have.
     * $n=20$ ballooning time step: $0.1t_A$ (Fig. 14 caption) vs
       $0.2R_0/v_A$ (Fig. 15 text).
     * Instability growth rate: 0.21 (Fig. 10) vs about 0.10 at vanishing
       diffusion (Fig. 12), cases not distinguished.
     * Drift-case probe: text $(\psi,\theta,\xi)=(0.6,0,0)$, Fig. 20 caption
       $(0.5,0,0)$; "perturbed electric potential" vs sub-caption "perturbed
       electron potential".
     * Model naming: §IX uses "model 2" and "model 1" for the models §II
       calls B and A.
     * Eq. 6 prints $J_\parallel$ without subscript 0 (Eqs. 1, 9 have it);
       Eq. 9 prints $\delta A_{\parallel0}$ for $\delta A_\parallel$; Eq. 43
       has $\nabla A$ on the left and $\partial_kh$ on the right.
     * Eq. 52 lacks the leading minus sign of Eq. 48 and differs in the
       $B_0$ factors, implying $\partial(1/B_0)$ terms folded or dropped
       without comment.
     * $\gamma$ is an undefined adiabatic index in Eqs. 8, 11; diamagnetic
       frequencies are Gaussian (with $c$, no $e$) inside SI; $\xi$ and
       $\phi$ are used interchangeably for the toroidal angle; $I$ has two
       meanings; $\beta$ is never defined and is used for $P_0$ (Fig. 18b).
     * §III C states that both shifted metrics "need interpolation in y
       direction" and then that the simple one needs no interpolation (the
       latter meaning field-to-particle interpolation).
     * "Four processors (112 cores)" means four sockets; scaling baselines
       are the smallest core count (Fig. 6) and the largest grid (Fig. 7).
     * Minimal multiplication count "can be proved", no proof.
     * Fig. 28 axis "$V_A/R_0$"; "Major raduis", "gird points"; the
       linear-solver name is printed "PARSIDO".
   * **Reference list.** 22 printed entries (Crossref count 22), merged into
     the bibliography under `jiang-2024`. No DOIs printed, none added.
     Ref. 4 (MAS, Bao et al. 2023) is truncated to 10 authors + others;
     Ref. 12 (Courant–Friedrichs–Lewy) is printed in lowercase without the
     umlaut and corrected in the entry; Refs. 13 (MPL) and 19 (JSON for
     Modern C++) are software; Ref. 18 (HaskellWiki, no author or year,
     accessed 1 February 2024) is keyed `haskellwiki-2024`; Ref. 22
     (Hirshman, VMEC→Boozer note, 1995) is a URL. Shared with `liu-2024`:
     `scott-2001`, `dudson-2009`, `pheatt-2008`, `dudt-2020`.
