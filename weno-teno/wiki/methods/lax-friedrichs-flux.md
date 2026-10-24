---
type: Method
title: "Lax–Friedrichs (Rusanov) flux and flux splitting"
description: 'The Lax–Friedrichs two-point flux and the Lax–Friedrichs flux splitting $f^\pm=\tfrac12(f\pm au)$, global or local, per field or scalar: the default upwinding of finite-difference WENO and TENO, the surface flux of DG, the low-order flux whose bar-state structure makes invariant-domain and bound-preserving proofs work, its positivity-preserving extension to the total Navier–Stokes flux, and its entropy-stable variant on entropy-variable jumps.'
status: established
aliases: [Rusanov flux, local Lax–Friedrichs, LLF, global Lax–Friedrichs, GLF, Lax–Friedrichs flux splitting, Rusanov flux splitting]
tags: [numerical-flux, finite-difference, bound-preserving, weno, teno]
timestamp: 2026-10-23T20:39:00Z
---

# Lax–Friedrichs (Rusanov) flux and flux splitting

The Lax–Friedrichs (LF) two-point flux is

$$h^{\mathrm{LF}}(u^-,u^+)=\tfrac12\big(f(u^-)+f(u^+)\big)-\tfrac a2\big(u^+-u^-\big),$$

with $a$ an upper bound of the wave speeds: local ($a_{i+1/2}$ from the two states, "local
Lax–Friedrichs", LLF) or a maximum over the domain ("global Lax–Friedrichs", GLF). The
corresponding **flux splitting** $f^\pm(u)=\tfrac12\big(f(u)\pm au\big)$, with
$\pm\,\partial f^\pm/\partial u\ge0$, is the upwinding device of
[conservative finite-difference](/definitions/conservative-finite-difference-scheme.md)
WENO and TENO: $\hat f^+_{i+1/2}$ is reconstructed from $f^+$ on a left-biased stencil,
$\hat f^-_{i+1/2}$ from $f^-$ by the mirror rule, and $\hat f_{i+1/2}=\hat f^+_{i+1/2}+\hat f^-_{i+1/2}$
([Li et al. (2022b)](/sources/li-2022-b.md), §2, Eqs. (1)–(4);
[Ye et al. (2022)](/sources/ye-2022.md), Eq. (20), $a=\max\lvert f'(u)\rvert$).

## Naming conventions

The sources disagree on words, not on mathematics. [Jeong et al. (2022)](/sources/jeong-2022.md)
(§5, Eq. (44)) call $a=\max\lvert f'(u)\rvert$ "over the whole range of" $u$ "the local numerical
viscosity", a global bound under a local name. [Fu (2023)](/sources/fu-2023.md)
(§3.4 Algorithm 1) calls "Rusanov" the splitting with a **global** per-field maximum speed;
[Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md) (§3) and
[Wang et al. (2023b)](/sources/wang-2023-b.md) (§1) use "Rusanov" for the **local** flux;
[Fu (2021)](/sources/fu-2021.md) (§5) uses "Rusanov splitting" for conventional gas dynamics
and "LLF" for extreme cases; [Takagi et al. (2022)](/sources/takagi-2022.md) (§4) write
"Rusanov (global/local Lax–Friedrichs)". [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md)
(§3, Eq. (22)) write the first-order flux as a central average minus
$\tfrac12\lvert Q\rvert(u_{i+1}-u_i)$ and print $Q=\tfrac12I$ for "Lax–Friedrichs" and
$Q=a_{i+1/2}I$ for Rusanov. *(compiler check, not in the sources: the classical
Lax–Friedrichs scheme in this form has $Q=\frac{\Delta x}{\Delta t}I$, so $\tfrac12I$ needs a
normalization the paper does not state.)* This page reads every occurrence by the
speed bound it uses.

## In finite-difference WENO and TENO for systems

The recipe of these finite-difference sources is [characteristic decomposition](/methods/characteristic-decomposition.md)
with Roe averages, LF splitting of each characteristic field with that field's maximum speed,
nonlinear reconstruction of both split parts, and back-projection
([Fu (2023)](/sources/fu-2023.md), Algorithm 1, $a^{(l)}$ the maximum $l$-th characteristic
speed over the whole domain). Users: global LF in [Li et al. (2022b)](/sources/li-2022-b.md)
("with local characteristic fields"; $\Delta t=\nu\,\Delta x/\max_i(\lvert v_i\rvert+c_i)$,
$\nu=0.5$, Eq. (38)), [Luo & Wu (2021)](/sources/luo-2021-b.md),
[Wang & Don (2022)](/sources/wang-2022-b.md) (§3.3, in the well-balanced shallow-water
scheme), [Fu (2021)](/sources/fu-2021.md) and [Takagi et al. (2022)](/sources/takagi-2022.md);
global LF is also one of the fluxes of the alternative formulation in
[Ye et al. (2022)](/sources/ye-2022.md), whose derivative corrections can also be computed
upwind from LF-split fluxes (Eqs. (19)–(22)). The multi-resolution WENO of
[Wang et al. (2021)](/sources/wang-2021.md) uses LF splitting dimension by dimension in
local characteristic fields (§3.1, Remark 1; the speed bound is not printed). In the
conservative two-medium [A-WENO](/methods/alternative-weno.md) of
[Zheng et al. (2021)](/sources/zheng-2021.md) (§2.1–2.2, Eqs. (1), (6)) the LF two-point
flux with $a=\max_u\lvert f'(u)\rvert$ acts on WENO-interpolated primitive variables, and its
derivative corrections are multiplied by a discontinuity indicator near the interface. [Deng (2023)](/sources/deng-2023.md) (§8) states
that the normalised-variable framework extends to conservative finite differences by
applying it to the split flux, or to the split flux in characteristic space.

Further users among the TENO and WENO papers: Rusanov splitting (global or local not
stated) with Roe-averaged characteristic fields in [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md)
(§4) and [Liang et al. (2022)](/sources/liang-2022.md) (§3); global LF splitting of both the
flux and the derivative flux $f'(u)u_x$ of the finite-difference Hermite WENO of
[Fan et al. (2023)](/sources/fan-2023.md) (§2), whose positivity-preserving flux limiter takes
the first-order LF flux as its low-order flux (App. A;
[positivity-preserving flux limiter](/methods/positivity-preserving-flux-limiter.md)); global LF
with $a=\max\rho(\partial f/\partial u)$ in the A-WENO of [Li et al. (2023a)](/sources/li-2023.md)
(Eq. (35)). In the hybrid TENO-S of [Liang & Fu (2024b)](/sources/liang-2024-b.md)
(Algorithm 1) the splitting $f^{(l)\pm}=\tfrac12\big(f^{(l)}\pm a^{(l)}\zeta^{(l)}\big)$ of each
Roe-averaged characteristic field, called Rusanov splitting, is applied only in the cells
that their discontinuity indicator flags, the others taking a non-dissipative split-form
central flux; for the [interacting blast waves](/benchmarks/woodward-colella-blast-wave.md)
they replace it by "the Roe scheme with entropy-fix ... to obtain a stable result" (§4.4;
[Roe solver](/methods/roe-riemann-solver.md)). Three sources make the choice of speed matter:

- **Local characteristic LF for turbulence.** [Li et al. (2022a)](/sources/li-2022.md) use
  global LF splitting, componentwise or in characteristic fields, except for the
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md), where they switch to local
  characteristic LF because, citing earlier work, the global one is too dissipative there
  (§3.4, §4.4).
- **A larger speed for steady convergence.** [Wan & Xia (2022)](/sources/wan-2022.md) (§4)
  march steady Euler problems to convergence with global LF splitting, $a=\max(\lvert v\rvert+c)$
  per direction; multiplying $a$ by 1.1 makes the residue of a stalled scheme converge on the
  [forward-facing step](/benchmarks/forward-facing-step.md) (MRWENO, $90\times30$, Ex. 4.5) and
  on the square-column flows (CWENOZ, Exs. 4.12–4.13), but not on the $400^2$ one-plate flow
  (Ex. 4.7), and per-field speeds instead of $\max(\lvert v\rvert+c)$ make all three schemes
  converge on the shock reflection (Ex. 4.4; [characteristic decomposition](/methods/characteristic-decomposition.md)).
- **A Mach-dependent speed.** In the semi-implicit all-Mach scheme of
  [Boscarino et al. (2022)](/sources/boscarino-2022.md) (Eq. (3.32)) the global LF splitting of
  the explicit flux uses $\max\big(\lvert v_1\rvert+\lvert v_2\rvert+\min(1,1/\varepsilon)\,c\big)$, $\varepsilon$
  the reference Mach number and $c$ the scaled sound speed, so that the acoustic speed
  $c/\varepsilon$ is excluded for $\varepsilon<1$; the implicit acoustic flux is reconstructed
  componentwise with zero numerical diffusion (§1;
  [semi-implicit all-Mach schemes](/methods/semi-implicit-all-mach-scheme.md)).
  [Chen, Wu & Xiong (2023)](/sources/chen-2023-b.md) (§3.3, Eqs. (3.11)–(3.12)) use the same
  device for ideal MHD at sonic Mach number $\varepsilon$: the global speed is
  $\max_k\big(\lvert v_k\rvert+\hat c_{\mathrm f}^{(k)}\big)$, the fast magnetosonic speed built
  from the capped sound speed $\min(1/\varepsilon,1)\sqrt{\gamma p_k/\rho_k}$ (page-local
  $\hat c_{\mathrm f}$), so that dissipation coefficient and time step are independent of
  $\varepsilon$ for $\varepsilon<1$; they apply the cap also to their explicit reference schemes,
  where it "leads to much better results" at low Mach number (§5). Their vector-potential
  equation, a Hamilton–Jacobi equation, uses the Lax–Friedrichs numerical Hamiltonian
  $H(\tfrac12(\partial^-+\partial^+))-\beta_{\mathrm{HJ}}\tfrac12(\partial^+-\partial^-)$ on WENO
  approximations $\partial^\pm$ of the derivative, with $\beta_{\mathrm{HJ}}$ the maximal
  $\lvert\partial H/\partial(\cdot)\rvert$ between them (Eq. (3.14); page-local symbols).

[Balsara et al. (2024)](/sources/balsara-2024.md) (§II, Eq. (2.2)) write the same splitting
at matrix level, $A^\pm=\tfrac12(A\pm aI)$, $a$ the largest eigenvalue of $\lvert A\rvert$,
with first-order CFL limit $\Delta t=\Delta x/a$; the high-order version (Eq. (2.3)) reduces
identically to LF FD-WENO for linear fluxes, and their
[fluctuation-form FD-WENO](/methods/fluctuation-form-fd-weno.md) recovers it in the LLF limit
$s^\pm\to\pm a$ of the [HLL](/methods/hll-riemann-solvers.md) solver (§V). They also note
that the LF splitting needs **two** reconstructions per zone (one per split part), against
one in fluctuation form (§VI).

## As the two-point flux of finite-volume and DG schemes

- Default surface or interface flux: local LF in [Peng et al. (2024)](/sources/peng-2024.md)
  ([OEDG](/methods/oedg.md); upwind for linear problems, §5),
  [Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md) (all tests, §5) and among the
  benchmarked surface fluxes of [Ranocha et al. (2023)](/sources/ranocha-2023.md) (Table 2);
  global LF in all tests of [Cui et al. (2024)](/sources/cui-2024.md) (§7).
- Local LF in the nodal DG of [Yu & Hesthaven (2022)](/sources/yu-2022.md) (§2.2, Eq. (2.10)),
  with $a$ the larger of the two traces' maximal wave speeds on each edge ($\lvert v\rvert+c$ for
  1D Euler) and centred fluxes for the auxiliary-gradient and artificial-viscosity terms; and in
  the third-order finite-volume WENO3-NN tests of [Bezgin et al. (2022)](/sources/bezgin-2022.md)
  (§2, §4), with characteristic reconstruction and TVD-RK3 at CFL 0.6
  ([learned WENO weights](/methods/learned-weno-weights.md)).
- In the $N$-phase pressure–temperature equilibrium model of
  [Nguyen et al. (2022)](/sources/nguyen-2022.md) (§2.3, Eq. (19)) the Rusanov flux takes $a$ as
  the largest eigenvalue modulus at Roe-averaged states. On a water–air interface advected at
  Mach about 0.001 on 100 cells it smears the interface: with the van Leer limiter it grows
  beyond ten cells, against three to five with HLLC (§3.1, Figs. 3–4;
  [HLL-family solvers](/methods/hll-riemann-solvers.md)).
- In the implicit [Quinpi](/methods/quinpi.md) scheme the global LF flux,
  $a=\max_u\lvert f'(u)\rvert$, is used in every predictor and corrector stage
  ([Puppo et al. (2023)](/sources/puppo-2023.md), Eqs. (14), (20)); together with
  predictor-based reconstruction weights it keeps the stage systems nonlinear only
  through $f$.
- Rusanov as the inviscid interface flux of the volume-penalization
  [flux reconstruction](/methods/flux-reconstruction.md) of [Kou et al. (2022)](/sources/kou-2022.md)
  (with LDG viscous fluxes, Eq. (15)); local LF for the 3D explosion in FLEXI, chosen as "robust ... for this focusing wave
  problem" ([Mossier et al. (2022)](/sources/mossier-2022.md), §8.9); and the most diffusive of
  the four run-time options of IDEFIX, second order with linear reconstruction on linear MHD
  waves ([Lesur et al. (2023)](/sources/lesur-2023.md), §2.3, §4.2, Fig. 7;
  [Roe solver](/methods/roe-riemann-solver.md)).
- In [JAX-Fluids](/software/jax-fluids.md) ([Bezgin et al. (2023)](/sources/bezgin-2023.md),
  §3.3, Table 2) Lax–Friedrichs and Rusanov are among the selectable Riemann solvers, and
  componentwise local Lax–Friedrichs is one of the splittings of its characteristic
  flux-splitting route.
- In the two-fluid relativistic plasma scheme of [Bhoriya et al. (2023)](/sources/bhoriya-2023.md)
  (§4.2) the Maxwell block, whose eigenvalues are bounded by the speed of light and by the
  cleaning speeds, all set to 1, uses the Rusanov flux with $a=1$ on minmod- or
  WENO-reconstructed face values.
- **As a first-order limit.** The first-order version of the
  [discrete kinetic relaxation scheme](/methods/discrete-kinetic-relaxation-scheme.md) of
  [Abgrall & Nassajian Mojarrad (2024)](/sources/abgrall-2024.md) "amounts to global
  Lax–Friedrichs" and is the fallback of its MOOD stabilization (§3.2.2); the first-order
  viscosity $C_{\max}h\,a$ (page-local constant $C_{\max}$ and mesh size $h$) of the residual-viscosity
  continuous finite elements of [Dao & Nazarov (2022)](/sources/dao-2022.md) reproduces 1D
  Lax–Friedrichs for $C_{\max}=0.5$, stated without proof (§4.2;
  [artificial viscosity](/methods/artificial-viscosity.md)).
- [Arun et al. (2022)](/sources/arun-2022.md) (§5) use "a Rusanov-type approximate Riemann
  solver" on hydrostatically reconstructed interface states (no formula printed; see
  [well-balancing](/properties/well-balancing.md)).
- In [A-WENO](/methods/alternative-weno.md), as [Wang et al. (2023b)](/sources/wang-2023-b.md)
  recall (§1, App. A), the Rusanov flux was the finite-volume building block before
  adaptive-diffusion variants; their "OLD" flux is LF with a
  single adaptively reduced coefficient
  ([adaptive-diffusion central-upwind flux](/methods/adaptive-diffusion-central-upwind-flux.md)).

## A learned dissipation coefficient

[Bezgin et al. (2023)](/sources/bezgin-2023.md) (§7.4, Eqs. (48)–(50)) replace the Rusanov
coefficient $a=\max\{\lvert v^-\pm c^-\rvert,\lvert v^+\pm c^+\rvert\}$ by the output of a
multilayer perceptron (three layers of 32 nodes, ReLU, exponential output so that the
coefficient is non-negative) with inputs $\lvert v^+-v^-\rvert$, $\tfrac12(v^-+v^+)$,
$\tfrac12(c^-+c^+)$ and the entropy jump $\lvert s^+-s^-\rvert$. The flux keeps the
Lax–Friedrichs form, so consistency and conservation are untouched. The network is trained
end to end through the differentiable solver on 15-step unrolls of the first 1000 steps of a
2D implosion trajectory coarse-grained from $128^2$ to $32^2$ (Adam, learning rate
$5\times10^{-4}$, batch 20, 200 epochs). The learned flux is less dissipative than Rusanov,
stays stable over the full 2501-step trajectory and gives lower relative $L_1$ errors in
density and pressure throughout, including beyond the training horizon (Figs. 20–21). It is
one trained network on one problem; no generalization test to other flows is shown. See
[learned WENO weights](/methods/learned-weno-weights.md).

## Bound preservation and invariant domains

- **First-order BP.** [Wu & Shu (2023)](/sources/wu-2023-b.md) prove with
  [geometric quasilinearization](/methods/geometric-quasilinearization.md) that the
  first-order finite-volume LF scheme for 1D Euler is bound preserving for
  $G=\{\rho>0,\ p>0\}$ under $\nu\le1$ with $a=\max_i(\lvert v_i\rvert+c_i)$ (§5.1, Ex. 1.1),
  and the 2D ten-moment LF scheme under the sum of the two directional CFL numbers $<1$
  (§5.3); for multicomponent MHD the 2D LF scheme is BP provided a discrete divergence
  vanishes (Thm. 6.1; see [divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)).
  [Cui et al. (2024)](/sources/cui-2024.md) use $c_0=1$ for LF against $c_0=\tfrac12$ for
  HLL/HLLC as the first-order BP CFL constant (§7), so that with LF and their optimal decomposition the
  linear-stability time step $1/(2N+1)$ of $\mathbb P^N$-DG already guarantees BP for $N\le9$
  except $N=8$ (Table 1, Remark 7.7;
  [bound preservation](/properties/bound-preservation.md)).
- **Invariant domains.** [Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md)
  (Prop. 1, §3, Eqs. (30)–(33)) prove that subcell finite volumes with first-order
  reconstruction and the LLF flux are identical to Pazner's sparse invariant-domain-preserving
  low-order DG scheme, a graph-Laplacian form
  $\sum_j\hat d_{ij}(u_j-u_i)$. The bar states
  $\bar u_{(a,b)}=\tfrac12(u_a+u_b)+\frac1{2a_{(a,b)}}\big(f(u_a)-f(u_b)\big)$ (Eq. (25), normal
  fluxes, $a_{(a,b)}$ the maximal wave speed) preserve all convex invariants, so the
  bar-state bounds hold to machine precision with FV-LLF on the bow shock (§5.2.2); they do
  not carry over to HLLE or second-order FV (§5.2.3). See
  [convex limiting](/methods/convex-limiting.md),
  [subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md).
- **Monolithic convex limiting.** [Rueda-Ramírez et al. (2024)](/sources/ruedaramirez-2024.md)
  (§2.2.1, Eqs. (9)–(13)) take the same LGL subcell LLF fluxes as the low-order scheme of
  monolithic convex limiting for DGSEM, with $\lambda^{\max}_{(i,j)}=\lambda^{\max}_{(j,i)}$ an
  upper bound of the maximum wave speed of the Riemann problem between nodes $i$ and $j$
  (page-local). The forward-Euler update is a convex combination of $u_i^n$ and the bar states
  $\bar u_{(i,i\pm1)}$ under $\Delta t\le J\mathsf w_i/(\lambda^{\max}_{(i,i-1)}+\lambda^{\max}_{(i,i+1)})$
  ($J$ the element Jacobian, $\mathsf w_i$ the LGL weight), and the bar state is the HLL
  intermediate state, so it preserves every convex invariant (citing earlier work). The high-order subcell flux is the LLF flux plus an anti-diffusive flux,
  and the limiter bounds the **limited bar states**
  $\bar u_{(i,j)}+\Delta\hat f^{\mathrm{Lim}}_{(i,j)}/\lambda^{\max}_{(i,j)}$ (page-local
  $\Delta\hat f^{\mathrm{Lim}}$) in closed form, at the semi-discrete level, so the limited
  operator does not depend on $\Delta t$ (Eqs. (14)–(24)). The price is the stricter step
  $\Delta t\lesssim\min_im_i/(2\sum_d\lambda^{\max,d}_i)$, $m_i$ the diagonal mass entry, against
  the low-order condition $\Delta t\lesssim\min_i\min_d\Delta x^d_i/\lambda^{\max,d}_i$ (Eqs. (43)–(45), §2.2.4). LLF is
  also the surface flux of all their tests (§3). See
  [convex limiting](/methods/convex-limiting.md).
- **The original sparse IDP DG.** [Pazner (2021)](/sources/pazner-2021.md) chooses the
  LLF interface flux of the author's DGSEM because it is compatible with graph viscosity: its jump
  term merges with the in-element graph viscosity
  $d_{ij}=\max\{a(u_i,u_j)\lVert c_{ij}\rVert,\ a(u_j,u_i)\lVert c_{ji}\rVert\}$ into a single
  graph form (§2, Eq. (6); §3.1, Eqs. (30)–(35); page-local $c_{ij}$, $d_{ij}$ the graph
  coefficients and viscosities, $a(\cdot,\cdot)$ the maximal wave speed of the pair), and
  the forward-Euler update is a convex combination of the bar states
  $\tfrac12(u_i+u_j)+\frac{\hat c_{ij}}{2\hat d_{ij}}\cdot\big(f(u_j)-f(u_i)\big)$ (Eqs. (38)–(39),
  Prop. 7). See [convex limiting](/methods/convex-limiting.md).
- **Relativistic hydrodynamics on Gauss–Lobatto points.** [Cai, Qiu & Wu (2024)](/sources/cai-2024.md)
  (§3, Eq. (3.4), Lemma 3.1, Thm. 3.1) use the global LF flux on the interface values of a
  finite-volume [Hermite WENO](/methods/hermite-weno.md) scheme, with $a$ the maximum spectral
  radius over all interface states. The LF splitting property they recall from Wu and Tang,
  $u\in G\Rightarrow u\pm f(u)/a\in G$ for every $a$ not below the spectral radius at $u$, and the
  decomposition of $\bar u_i$, after a Zhang–Shu-type scaling limiter, on the four Gauss–Lobatto points ($N_{\mathrm{GL}}=4$, endpoint
  weight $\tfrac1{12}$) give a physical-constraint-preserving update under
  $\Delta t\le\tfrac1{12}\Delta x/a$, and $\Delta t\le\tfrac1{12}/(a^{(1)}/\Delta x+a^{(2)}/\Delta y)$ in
  2D (Thm. 4.1; page-local directional speeds $a^{(d)}$); the HLL flux is named as an alternative
  whose positivity was proved by [Chen & Wu (2022)](/sources/chen-2022-b.md)
  ([relativistic hydrodynamics](/definitions/relativistic-hydrodynamics.md),
  [bound preservation](/properties/bound-preservation.md)). Their tests run at "CFL number
  0.6", whose definition is not printed (§5). *(compiler check, not in the sources: if that
  number multiplies $\Delta x/a$, it is $7.2$ times the proved bound $\tfrac1{12}$.)*
- **Ideal MHD with a divergence-dependent viscosity.** [Ding & Wu (2024a)](/sources/ding-2024.md)
  (arXiv v1; §2.1, Eqs. (6)–(16), Thm. 2.1) use the LF flux with Gauss or Gauss–Lobatto edge
  quadrature in a high-order finite-volume scheme for the Godunov–Powell form of ideal MHD, and
  prove with [geometric quasilinearization](/methods/geometric-quasilinearization.md) that the
  forward-Euler update keeps density and internal energy positive under
  $\Delta t\big(a^{(1)}/\Delta x+a^{(2)}/\Delta y\big)<1/\big(N_{\mathrm{GL}}(N_{\mathrm{GL}}-1)\big)$, the
  first Gauss–Lobatto weight, provided the interface values satisfy a discrete divergence-free
  condition and are admissible. The LF coefficient must be enlarged by a jump term,
  $a^{(d)}\ge\hat a^{(d)}+\beta^{\mathrm B}_d$, $\beta^{\mathrm B}_1=\max\lvert[\![B_1]\!]\rvert/\big(2\sqrt{\{\!\{\rho\}\!\}}\big)$
  over the edge quadrature points (page-local $\beta^{\mathrm B}_d$), with $\hat a^{(d)}$ Wu's
  positivity-preserving wave-speed bound evaluated on the pairs of traces of the same cell, not on
  the two sides of an interface (Eq. (16)). Their interface-jump source discretization, built from
  $[\![B_d]\!]$ and $\{\!\{u\}\!\}$ at the quadrature points, differs from Wu and Shu's earlier ones and is
  stated to give a milder CFL condition (§2.1; no side-by-side constant given); in the proof the
  divergence remainder cancels exactly by the discrete divergence-free condition (§3.2). As in
  Wu & Shu's multicomponent-MHD result above (Thm. 6.1), positivity is conditional on a discrete
  divergence-free condition. See
  [divergence-free magnetic field](/properties/divergence-free-magnetic-field.md) and
  [bound preservation](/properties/bound-preservation.md).
- **Active Flux averages and point values.** [Duan, Barsukow & Klingenberg (2025)](/sources/duan-2025.md)
  (§4, Lemmas 4.1–4.2, App. B; arXiv v3) take first-order LLF as the low-order scheme of the
  [convex limiting](/methods/convex-limiting.md) of Active Flux cell averages, with
  $a_{i+1/2,j}=\max\{\varrho(\bar u_{i,j}),\varrho(\bar u_{i+1,j})\}$ ($\varrho$ the spectral radius of the
  directional Jacobian, page-local). The update is written through the bar states
  $\tilde u_{i+1/2}=\tfrac12(\bar u_i+\bar u_{i+1})-\frac1{2a_{i+1/2}}\big(f(\bar u_{i+1})-f(\bar u_i)\big)$, which lie
  in $G$ whenever $a_{i+1/2}$ is not below the spectral radius at both states, for scalar laws and
  for Euler (Lemmas B.1–B.2), and the 2D scheme is a convex combination under
  $\Delta t\le\tfrac12\min\{\Delta x_i/(a_{i-1/2,j}+a_{i+1/2,j}),\ \Delta y_j/(a_{i,j-1/2}+a_{i,j+1/2})\}$ (Eq. (30)). A
  second LLF scheme on staggered stencils of point values bounds the point-value update (Lemma 4.2);
  on uniform meshes $\Delta t\le\tfrac14\min\{\Delta x/\lVert\varrho_1\rVert_\infty,\Delta y/\lVert\varrho_2\rVert_\infty\}$
  satisfies both conditions (Remark 4.5), and $\Delta t\le\Delta x/(2\lVert\varrho\rVert_\infty)$ in 1D
  (Remark C.1). The same flux, between the interior state and its mirror image, replaces the
  boundary flux at reflective walls (§3.3). This LLF coefficient differs from the five-state one of
  their LLF flux vector splitting ([flux vector splitting](/methods/flux-vector-splitting.md)).
- **A global-speed flux limiter for Active Flux.** [Kiechle et al. (2025)](/sources/kiechle-2025.md)
  (§3.2, Eqs. (12)–(24), Remark 3.2) blend each Active Flux interface flux with a first-order
  **global** LF flux, $\gamma F^{\mathrm{AF}}+(1-\gamma)F^{\mathrm{LF}}$ (page-local $\gamma\in[0,1]$, $F$),
  with $a_x=\max_i\lvert f'(\bar u_{i,j})\rvert$; the first-order LF scheme is positivity preserving under
  CFL $\le\tfrac12$, but the four one-sided split states of their convex splitting of the 2D update
  are non-negative only under CFL $\le\tfrac14$ with equal weights $\tfrac12$, which is the condition
  of guaranteed positivity. In a comparison with the PAMPA flux limiter of Abgrall et al., a
  global speed gave more accurate results than the local one of that limiter on their test (Fig. 5;
  [positivity-preserving flux limiter](/methods/positivity-preserving-flux-limiter.md)).
- **Positivity by an external limiter.** [Fu (2021)](/sources/fu-2021.md) (§5.7) runs the
  extreme cases (double rarefaction, Le Blanc, Sedov, Mach 80 and Mach 2000 jets) with LLF
  plus the positivity-preserving flux limiter of Hu, Adams & Shu; the TENO reconstruction
  itself is not claimed positivity preserving.

## Viscous flows: a positivity-preserving Lax–Friedrichs flux

For the compressible Navier–Stokes equations, [Fan et al. (2021)](/sources/fan-2021.md)
(§3.1, Eqs. (3.4)–(3.5)) use the flux of Zhang (2017), a Lax–Friedrichs form of the
**total** flux $F(u,\nabla u)=f(u)-f^\nu(u,\nabla u)$ (advective minus diffusive):

$$\hat F_{i+1/2}=\tfrac12\Big[F(u^-,\nabla u^-)+F(u^+,\nabla u^+)-a^{\mathrm{NS}}_{i+1/2}\big(u^+-u^-\big)\Big],\qquad
a^{\mathrm{NS}}_{i+1/2}>\max_{\pm}\Big[\lvert v\rvert+\frac{\sqrt{\rho^2q_{\mathrm h}^2+2\rho^2e\,\lvert\tau_{\mathrm v}-p\rvert^2}+\rho\lvert q_{\mathrm h}\rvert}{2\rho^2e}\Big],$$

(page-local: $a^{\mathrm{NS}}$ the dissipation coefficient, $\tau_{\mathrm v}$ the viscous
stress, $q_{\mathrm h}$ the heat flux; the maximum over the two interface states). The key
property, Lemma 6 of Zhang as used by Fan et al., is that $u\in G$ implies
$u\pm F(u,\nabla u)/a^{\mathrm{NS}}\in G$ for any gradient, so the update can be written as a
convex combination of admissible states under
$\frac{\Delta t}{\Delta x}\max a^{\mathrm{NS}}\le\frac1{N_{\mathrm{GL}}(N_{\mathrm{GL}}-1)}$, the
boundary weight of an $N_{\mathrm{GL}}$-point Gauss–Lobatto decomposition (page-local
$N_{\mathrm{GL}}$; Thm. 1, Eqs. (3.11)–(3.13)). *(compiler check, not in the sources: for
$\mathrm{Re}=\infty$, $q_{\mathrm h}=0$ and $\tau_{\mathrm v}=0$, the bound reduces to
$\lvert v\rvert+\sqrt{(\gamma-1)p/(2\rho)}$, below $\lvert v\rvert+c$, so the LF speed $\lvert v\rvert+c$
satisfies it.)* See
[bound preservation](/properties/bound-preservation.md),
[Hermite WENO](/methods/hermite-weno.md) and
[optimal cell-average decomposition](/methods/optimal-cell-average-decomposition.md).

The finite-difference counterpart is [Fan et al. (2022)](/sources/fan-2022.md) (§3,
Eqs. (3.3)–(3.10)): the Lax–Friedrichs splitting of the Shu–Osher finite-difference WENO is
replaced by the splitting of the total flux, $z^\pm=\tfrac12\big(u\pm F(u,\nabla u)/a^{\mathrm{NS}}_{i+1/2}\big)$
(page-local $z^\pm$), with the same bound on $a^{\mathrm{NS}}$ taken over the WENO stencil, which
they say "has no specific physical meaning". A variant (§4, Eqs. (4.1)–(4.4)) splits the advective flux by
global LF and the diffusive flux separately, with the opposite signs and its own coefficient.
The details, the Gauss–Lobatto CFL condition and the halve-and-restart time stepping are on
[positivity-preserving Navier–Stokes fluxes](/methods/positivity-preserving-navier-stokes-flux.md).

**Graph viscosity for entropy-stable DG.** [Lin et al. (2023)](/sources/lin-2023.md) (§5,
Eqs. (16)–(28)) use the same coefficient as the graph viscosity of a sparse low-order nodal DG
scheme for explicit Navier–Stokes: central flux differencing of the total flux with a sparse
low-order [SBP operator](/operators/summation-by-parts-operator.md), plus
$\sum_jd_{ij}(u_j-u_i)$ with $d_{ij}=\max\{a^{\mathrm{NS}}(u_i,\sigma_i,n_{ij}),a^{\mathrm{NS}}(u_j,\sigma_j,n_{ij})\}\lVert n_{ij}\rVert$
(page-local $d_{ij}$, $n_{ij}$ the low-order "normal" from the skew entries of the operator,
$\sigma_i$ the viscous auxiliary flux), where

$$a^{\mathrm{NS}}(u,\sigma,n)=\epsilon_0+\lvert n\cdot v\rvert+\frac{1}{2\rho^2e}\Big(\sqrt{\rho^2(q_{\mathrm h}\cdot n)^2+2\rho^2e\,\lVert n\cdot\tau_{\mathrm v}-pn\rVert^2}+\rho\lvert q_{\mathrm h}\cdot n\rvert\Big),$$

$\epsilon_0>0$ arbitrarily small ($10^{-14}$ in the tests), "motivated by" Zhang (Eq. (18)). *(compiler check, not in the sources: in 1D with
$n=1$ it is the bound of Fan et al. above plus $\epsilon_0$.)* The forward-Euler update is then a convex
combination of the bar states
$\tfrac12(u_i+u_j)-\frac{1}{2a^{\mathrm{NS}}}\frac{n}{\lVert n\rVert}\cdot\big(F(u_j)-F(u_i)\big)$ of the
total flux (Eqs. (21)–(24)), admissible by Lemma 5.1, and Theorem 5.2 proves conservation and
positivity of density and internal energy under $\Delta t\le m_i/(2\lambda_i)$, $m_i$ the lumped
mass and $\lambda_i$ the sum of the node's graph and face coefficients (page-local). The step
scales as $O(h/N^2)$ and is about 2–3 times smaller than the largest stable DG step (Remark 1,
citing earlier work). With the coefficient enlarged to
$\max\{a,a^{\mathrm{NS}}_i,a^{\mathrm{NS}}_j\}$, $a$ a maximum wave-speed bound,
the low-order scheme is also semi-discretely entropy stable, proved by reading it as a subcell
finite-volume scheme with LLF-type fluxes (Theorem 6.1, Eqs. (45)–(53)); for the Euler equations
$a^{\mathrm{NS}}$ never exceeds the maximum wave speed, so the enlargement reduces to the
wave-speed estimate $a$ (§6.2), in agreement with the compiler check on the bound of
Fan et al. above. Details are on
[convex limiting](/methods/convex-limiting.md) and
[positivity-preserving Navier–Stokes fluxes](/methods/positivity-preserving-navier-stokes-flux.md).

**A shared interface flux decouples the cell entropy inequality from limiting.**
[Lin & Chan (2024)](/sources/lin-2024.md) (§2.3, Eqs. (13)–(17), (22)) blend, subcell interface by
subcell interface, the algebraic fluxes of DGSEM with those of the sparse low-order scheme of
Lin et al. (2023), a finite volume on LGL subcells with LLF-type graph viscosity
$\tfrac12\lVert n_{ij}\rVert\,a(u_i,u_j,n_{ij}/\lVert n_{ij}\rVert)$; here, unlike in Lin et al.
(2023), the coefficient is split by dimension (footnote 2). Both schemes use the same LLF
interface flux, $\tfrac12\big(f(u^-)+f(u^+)\big)-\tfrac a2\,\hat n\,(u^+-u^-)$ ($\hat n$ the unit face normal, page-local, placed as printed) with the Davis
estimate $a=\max\{\lvert v^-\cdot\hat n\rvert+c^-,\lvert v^+\cdot\hat n\rvert+c^+\}$ (Eqs. (14), (54)), so the
boundary algebraic fluxes of the two coincide (Eq. (17)), the surface contribution to the cell
entropy balance does not depend on the blending factors (Eq. (22)), and the cell entropy
inequality reduces to one linear inequality in the volume blending factors, which a linear
program solves ([subcell limiting](/methods/subcell-finite-volume-limiting.md),
[entropy stability](/properties/entropy-stability.md)). Solvability of that program rests on the
low-order scheme being semi-discretely entropy stable (Theorem 3.1), which in turn needs a true
wave-speed bound (see Qualifications).

For multicomponent reacting flows [Du & Yang (2022)](/sources/du-2022-b.md) (§3.1, Eq. (3.5);
§4.2, Lemma 4.1) extend the same construction to one partial-density equation per species
with diffusion velocities $v^{\mathrm d}_k$ (page-local) and formation enthalpies, and prove the sharp form:
for $u\in G$, $u\pm F/a^{\mathrm{NS}}\in G$ **iff**

$$a^{\mathrm{NS}}\ge\max\Big\{\Big|v+\frac{b_{\mathrm h}}{2\rho P}\Big|+\frac{\sqrt{D_{\mathrm h}}}{2\rho P},\ \lvert v+v^{\mathrm d}_k\rvert\Big\},\qquad
D_{\mathrm h}=b_{\mathrm h}^2+2\rho P\,(p-\tau_{\mathrm v})^2,$$

with $P$ the internal energy per volume without formation energies and
$b_{\mathrm h}=\rho q_{\mathrm h}-\rho\sum_k\rho Y_k\,h_k(0)\,v^{\mathrm d}_k$ (page-local; $h_k(0)$ the formation
enthalpies). The penalty enters an LDG scheme whose numerical flux must also satisfy
$\hat F\cdot\mathbf e_\Sigma=0$ for the constant vector $\mathbf e_\Sigma$ that encodes $\sum_kY_k=1$
(Def. 3.1, Thm. 3.1; page-local $\mathbf e_\Sigma$), which the LF form satisfies because both physical
fluxes and the jump are orthogonal to $\mathbf e_\Sigma$ when $\sum_kY_k=1$ (stated "easy to check").
*(compiler check, not in the sources: for one species without formation energy,
$b_{\mathrm h}=\rho q_{\mathrm h}$ and $P=\rho e$, and the condition becomes
$\lvert v+q_{\mathrm h}/(2\rho e)\rvert+\sqrt{\rho^2q_{\mathrm h}^2+2\rho^2e(p-\tau_{\mathrm v})^2}/(2\rho^2e)$,
which never exceeds the bound used by Fan et al., since
$\lvert v+x\rvert\le\lvert v\rvert+\lvert x\rvert$.)* The time step actually run uses the different
estimate $\lvert v\rvert+\sqrt{p^2/(2\rho P)}$ (Eq. (6.1)), with a restart (doubled exponential
damping, halved step) whenever a cell average leaves $G$ (§6).

## Variants of the dissipation term

- **Energy stability of a split ESFR scheme.** For Burgers' equation, $f=u^2/2$,
  [Cicchino et al. (2022)](/sources/cicchino-2022.md) (§3.1.2, Eqs. (46)–(50)) write the interface
  flux as $\tfrac12\big(f(u^-)+f(u^+)\big)-\lambda_{\mathrm F}(u^+-u^-)$ (page-local
  $\lambda_{\mathrm F}=a/2$ in this page's form) and show that their nonlinearly stable split
  [flux-reconstruction](/methods/flux-reconstruction.md) scheme with split parameter
  $\alpha=2/3$ (page-local split weight, not the DG–FV blending coefficient) has interface energy production
  $(u^+-u^-)^2\big(\tfrac1{12}(u^+-u^-)-\lambda_{\mathrm F}\big)$, hence is energy stable iff
  $\lambda_{\mathrm F}\ge\tfrac1{12}(u^+-u^-)$; equality is the energy-conserving flux, and LLF,
  $\lambda_{\mathrm F}=\tfrac12\max(\lvert u^-\rvert,\lvert u^+\rvert)$, satisfies it. With LF the
  discrete energy decreases monotonically in their Burgers tests (Tables 1–3;
  [entropy stability](/properties/entropy-stability.md)).
- **Disturbance form.** [Browne et al. (2022)](/sources/browne-2022.md) (§2.2, Eqs. (16)–(22))
  solve the compressible Navier–Stokes equations for the disturbance $u'=u-u_{\mathrm b}$ about a
  steady baseflow $u_{\mathrm b}$, with fifth-order FD-WENO in characteristic variables on
  Rusanov-split disturbance fluxes $f'$ (page-local subscript $\mathrm b$ and prime, as on the
  Source page). Writing the total Rusanov splitting with $a=a_{\mathrm b}+a'$ and subtracting the
  baseflow splitting leaves
  $f'^\pm=\tfrac12\big(f'\pm\{a_{\mathrm b}u'+a'(u_{\mathrm b}+u')\}\big)$ (Eq. (19)), whose
  term $a'u_{\mathrm b}$ they call "not consistent with the formal definition of the Rusanov flux"
  and destabilizing; they adopt $f'^\pm=\tfrac12\big(f'\pm a\,u'\big)$ for the nonlinear and
  $\tfrac12\big(f'\pm a_{\mathrm b}u'\big)$ for the linearized disturbance equations
  (Eqs. (21)–(22)). The stability claim is argued by inspection; no analysis or comparison is
  shown. *(compiler check, not in the sources: Eq. (19) minus Eq. (21) is $\pm\tfrac12a'u_{\mathrm b}$,
  so with Eq. (21) the discrete disturbance scheme is not the discrete total-flow scheme minus
  the discrete baseflow scheme, although the continuous disturbance equations are an exact
  rewriting.)*
- **Dissipation scaled by the flow speed only.** In the semi-implicit all-Mach MHD scheme of
  [Dematté et al. (2024)](/sources/dematte-2024.md) (§3.1, Eqs. (22)–(23)) the Rusanov flux
  acts only on the explicit advective sub-system of a flux-vector splitting, whose eigenvalues
  are $0$ and $v_1$, with $a_{i+1/2}=\max(\lvert v_1^-\rvert,\lvert v_1^+\rvert)$; the acoustic and magnetic
  waves are treated implicitly, so neither the dissipation nor the time step contains the sound,
  Alfvén or fast speeds ([semi-implicit all-Mach schemes](/methods/semi-implicit-all-mach-scheme.md)).
  [Allegrini & Vignal (2025)](/sources/allegrini-2025.md) (§3.2, Eqs. (15f), (16); HAL author
  manuscript) do the same for full Euler with the Toro–Vázquez splitting: the explicit Rusanov
  coefficient is $\tfrac12\max(\lvert v_i\rvert,\lvert v_{i+1}\rvert)$, "half of the maximum explicit
  eigenvalues", and an optional implicit Rusanov-type upwinding with coefficient
  $\tfrac12\max\lvert\lambda_{\mathrm i}\rvert$, the largest implicit eigenvalue
  $\lvert v\rvert/2+\sqrt{v^2/4+c^2/\varepsilon_{\mathrm A}}$ (page-local; $M^2=\varepsilon_{\mathrm A}/\gamma$),
  acts on the whole state, density included, or contact results are not consistent (Remark 5.1).
  That upwinding reduces the oscillations of the centred implicit fluxes but degrades asymptotic
  consistency to $O(\Delta t)$ (Remark 5.2).
- **Downwinding by sign flip.** [Dzanic et al. (2022)](/sources/dzanic-2022.md) (§2, §4.2) obtain
  the downwind-biased divergence of their time-reversibility shock indicator by negating the
  dissipative term of the Rusanov flux (Davis wave speeds) used in the forward step; the defect
  between the state and its forward-then-backward image drives an
  [artificial viscosity](/methods/artificial-viscosity.md). In their first-order analysis
  with upwind fluxes the viscosity tends to $c_\mu a\Delta x$, which for $c_\mu=\tfrac12$ is the
  viscosity that turns a central scheme into first-order upwind (§3.1, Eqs. (18)–(20); page-local
  constant $c_\mu$).

## Entropy stability: dissipation on entropy-variable jumps

[Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) (§3.3.1, Eqs. (52)–(53), citing
Derigs et al. 2017) write "Lax-Friedrichs type dissipation" on the conservative jump,
$\tfrac12\mathcal D[\![u]\!]$, with a Roe-type matrix $\mathcal D=R\lvert\Lambda\rvert R^{-1}$ (page-local),
LF and Rusanov being the case where every entry of $\lvert\Lambda\rvert$ is the largest eigenvalue,
and state that this dissipation added to an entropy-conservative flux is not entropy stable for
MHD. Their "ES Rusanov" flux replaces $[\![u]\!]$ by $\frac{\partial u}{\partial w}[\![w]\!]$
written with Barth's eigenvector scaling,

$$h=f^{\mathrm{ec}}(u^-,u^+)-\tfrac12R\,\lvert\Lambda\rvert\,\mathcal Z\,R^\top[\![w]\!],$$

with $\lvert\Lambda\rvert$ diagonal with every nonzero entry equal to the largest advective
eigenvalue and $\mathcal Z$ the diagonal Barth scaling, $\frac{\partial u}{\partial w}=R\mathcal ZR^\top$
(page-local $\Lambda$, $\mathcal Z$); the entropy production is
$-\tfrac12[\![w]\!]^\top R\lvert\Lambda\rvert\mathcal ZR^\top[\![w]\!]\le0$ (Eqs. (57)–(60)). It is
their default wherever dissipation is needed (§6). [Bhoriya et al. (2023)](/sources/bhoriya-2023.md)
(§4.1.2, Eq. (21), App. B) use the same Rusanov-type magnitude, the largest eigenvalue
modulus times the identity, with Barth-scaled eigenvectors in their entropy-stable flux for
two-fluid relativistic plasma, and call it "similar to the Roe diffusion operator"
([TeCNO schemes](/methods/tecno-scheme.md)). In the entropy-stable oscillation-free DG scheme
for MHD of [Liu et al. (2025b)](/sources/liu-2025-b.md) (§3.1, Eq. (3.14)) the interface flux is
$h=f^{\mathrm{ec}}-\tfrac12a\,\mathcal H[\![w]\!]$, with $\mathcal H$ the discrete entropy Jacobian of
Derigs et al. such that $[\![u]\!]=\mathcal H[\![w]\!]$ (page-local $\mathcal H$), which the authors say
reduces to the Lax–Friedrichs flux; they recommend the local speed
$a=\max(\lvert\lambda^-_{\max}\rvert,\lvert\lambda^+_{\max}\rvert)$ over the global one. See
[entropy-conservative fluxes](/methods/entropy-conservative-flux.md) and
[entropy stability](/properties/entropy-stability.md).

## Qualifications

- **Wave-speed estimates are not always bounds.** Lin et al. (2023) use the Davis estimate
  $\max\{\lvert v^-\cdot n\rvert+c^-,\lvert v^+\cdot n\rvert+c^+\}$ (Eq. (58)) in the LLF interface flux of
  their entropy-stable DG, which is entropy stable "when the maximum wave speed estimate is
  suitably chosen" (§4), and note, citing Guermond and Popov, that such Davis or Rusanov
  estimates can underestimate the maximum wave speed, which could compromise the positivity and
  entropy stability of the low-order scheme; no issue was observed in their tests (footnote 3).
  [Lin & Chan (2024)](/sources/lin-2024.md) (footnote 8) make the same remark for the same
  estimate (Eq. (54)): with it the low-order subcell scheme is not provably positivity preserving
  and semi-discretely entropy stable, and Theorem 3.1 derives the solvability of their entropy
  linear program from the latter property; no issue was observed.
- Lin et al. print the Navier–Stokes coefficient with $\lVert n\cdot\tau_{\mathrm v}-pn\rVert^2$ in
  Eq. (18) and without the square in the condition (20) that motivates it, and $u_2$ in place of
  $n_2$ in the second component of $n\cdot\tau_{\mathrm v}$ (Eq. (18)).

- **Plain LF dissipation and entropy stability for MHD.** Rueda-Ramírez et al. (2021) state,
  citing Derigs et al., that the Roe-type dissipation $\tfrac12\mathcal D[\![u]\!]$,
  $\mathcal D=R\lvert\Lambda\rvert R^{-1}$, of their Eq. (52) added to an entropy-conservative flux is not
  entropy stable for MHD; Liu et al. (2025b) present their entropy-stable dissipation
  $\tfrac12a\mathcal H[\![w]\!]$, with $[\![u]\!]=\mathcal H[\![w]\!]$, as reducing to the LF flux. Neither source
  proves its statement on the page read. *(compiler check, not in the sources: for the scalar
  case $\mathcal D=aI$, $a\ge0$, the dissipation changes the interface entropy production (55) of
  Rueda-Ramírez et al., written with their generalized Tadmor condition (51) for GLM-MHD with
  non-conservative terms, only by $-\tfrac12a[\![w]\!]\cdot[\![u]\!]$, because the non-conservative terms
  do not involve the dissipation; this is $\le0$ for any $a\ge0$ when $\eta$ is convex on the
  segment between $u^-$ and $u^+$, since $w=\eta'(u)$ is then monotone. The statement of
  non-entropy-stability can therefore apply to a general Roe-type matrix, for which
  $[\![w]\!]\cdot R\lvert\Lambda\rvert R^{-1}[\![u]\!]$ has no sign in general, but not to the scalar LF case, which
  is consistent with Liu et al. (2025b).)* Not recorded as a contradiction: the first statement
  is recalled from a non-ingested source.
- Wu & Shu's LF statements are proved for the first-order scheme; the high-order FV/DG MHD
  result uses Gauss-quadrature LF fluxes with a viscosity bound and its proof is "omitted"
  (Thm. 6.2).
- [Fu (2023)](/sources/fu-2023.md) mis-cites the Rusanov and Roe references by one number in
  Algorithm 1 (a slip of the review, not a disagreement).

# Citations

- [Li et al. (2022b)](/sources/li-2022-b.md) — §2 (Eqs. (1)–(4)), Eq. (38).
- [Ye et al. (2022)](/sources/ye-2022.md) — Eqs. (13), (19)–(22).
- [Fu (2023)](/sources/fu-2023.md) — §3.4 (Algorithm 1), §3.6.
- [Fu (2021)](/sources/fu-2021.md) — §5, §5.7 (arXiv v1).
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §4.
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — numerical set-up.
- [Wang & Don (2022)](/sources/wang-2022-b.md) — §3.3.
- [Deng (2023)](/sources/deng-2023.md) — §8.
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §II (Eqs. (2.2)–(2.3)), §V, §VI.
- [Peng et al. (2024)](/sources/peng-2024.md) — §5 (arXiv v1).
- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — §4.2, Table 2.
- [Cui et al. (2024)](/sources/cui-2024.md) — §7, Remark 7.7 (arXiv v1).
- [Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md) — §3 (Prop. 1, Eqs. (25), (30)–(33)), §5.2 (arXiv v2).
- [Wu & Shu (2023)](/sources/wu-2023-b.md) — §5.1, §5.3, Thms. 6.1–6.2 (arXiv v1).
- [Wang et al. (2023b)](/sources/wang-2023-b.md) — §1, App. A.
- [Fan et al. (2021)](/sources/fan-2021.md) — §3.1 (Eqs. (3.4)–(3.5), (3.11)–(3.13), Thm. 1), §3.2 (Eqs. (3.23)–(3.24)).
- [Pazner (2021)](/sources/pazner-2021.md) — §2 (Eq. (6)), §3.1 (Eqs. (30)–(39), Props. 5–7) (arXiv v1).
- [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) — §3.3.1 (Eqs. (52)–(60)), §6 (arXiv v1).
- [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) — §3 (Eqs. (20)–(22), (29)) (arXiv v1).
- [Puppo et al. (2023)](/sources/puppo-2023.md) — Eqs. (14), (20) (arXiv v2).
- [Arun et al. (2022)](/sources/arun-2022.md) — §4, §5 (arXiv v1).
- [Wang et al. (2021)](/sources/wang-2021.md) — §3.1, Remark 1.
- [Zheng et al. (2021)](/sources/zheng-2021.md) — §2.1–2.2 (Eqs. (1), (6)).
- [Yu & Hesthaven (2022)](/sources/yu-2022.md) — §2.2 (Eq. (2.10)).
- [Bezgin et al. (2022)](/sources/bezgin-2022.md) — §2, §4.
- [Nguyen et al. (2022)](/sources/nguyen-2022.md) — §2.3 (Eq. (19)), §3.1 (Figs. 3–4).
- [Du & Yang (2022)](/sources/du-2022-b.md) — §3.1 (Eqs. (3.4)–(3.5), Def. 3.1, Thm. 3.1), §4.2 (Lemma 4.1), §6 (Eq. (6.1)).
- [Cicchino et al. (2022)](/sources/cicchino-2022.md) — §3.1.2 (Eqs. (46)–(50)), §4 (Tables 1–3) (arXiv v1).
- [Browne et al. (2022)](/sources/browne-2022.md) — §2.2 (Eqs. (16)–(22)).
- [Dzanic et al. (2022)](/sources/dzanic-2022.md) — §2, §3.1 (Eqs. (18)–(20)), §4.2 (arXiv v2).
- [Jeong et al. (2022)](/sources/jeong-2022.md) — §5 (Eq. (44)).
- [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) — §4.
- [Liang et al. (2022)](/sources/liang-2022.md) — §3.
- [Fan et al. (2023)](/sources/fan-2023.md) — §2, App. A.
- [Fan et al. (2022)](/sources/fan-2022.md) — §3 (Eqs. (3.3)–(3.10)), §4 (Eqs. (4.1)–(4.4)).
- [Li et al. (2023a)](/sources/li-2023.md) — Eq. (35), §4.2.
- [Li et al. (2022a)](/sources/li-2022.md) — §3.4, §4.4.
- [Wan & Xia (2022)](/sources/wan-2022.md) — §4 (Exs. 4.4, 4.5, 4.7, 4.12–4.13).
- [Boscarino et al. (2022)](/sources/boscarino-2022.md) — §1, §3.3.1 (Eq. (3.32)) (arXiv v2).
- [Kou et al. (2022)](/sources/kou-2022.md) — Eq. (15).
- [Mossier et al. (2022)](/sources/mossier-2022.md) — §8.9.
- [Lesur et al. (2023)](/sources/lesur-2023.md) — §2.3, §4.2 (Fig. 7).
- [Abgrall & Nassajian Mojarrad (2024)](/sources/abgrall-2024.md) — §3.2.2.
- [Dao & Nazarov (2022)](/sources/dao-2022.md) — §4.2.
- [Chen, Wu & Xiong (2023)](/sources/chen-2023-b.md) — §3.3 (Eqs. (3.11)–(3.14)), §5 (arXiv v1).
- [Bezgin et al. (2023)](/sources/bezgin-2023.md) — §3.3, Table 2, §7.4 (Eqs. (48)–(50), Figs. 20–21) (arXiv v1).
- [Bhoriya et al. (2023)](/sources/bhoriya-2023.md) — §4.1.2 (Eq. (21)), §4.2, App. B (arXiv v2).
- [Lin et al. (2023)](/sources/lin-2023.md) — §4, §5 (Eqs. (16)–(28), Lemma 5.1, Thm. 5.2, Remark 1), §6.2 (Eqs. (45)–(53), Thm. 6.1), §8 (Eq. (58), footnote 3) (arXiv v2).
- [Liang & Fu (2024b)](/sources/liang-2024-b.md) — Algorithm 1, §4.4.
- [Rueda-Ramírez et al. (2024)](/sources/ruedaramirez-2024.md) — §2.2.1–2.2.4 (Eqs. (9)–(24), (43)–(45)), §3 (arXiv v1).
- [Cai, Qiu & Wu (2024)](/sources/cai-2024.md) — §3 (Eq. (3.4), Lemma 3.1, Thm. 3.1), §4 (Thm. 4.1), §5 (arXiv v1).
- [Lin & Chan (2024)](/sources/lin-2024.md) — §2.3 (Eqs. (13)–(17), footnotes 2, 8), §3.1 (Eq. (22), Theorem 3.1), §4 (Eq. (54)).
- [Dematté et al. (2024)](/sources/dematte-2024.md) — §3.1 (Eqs. (22)–(23)).
- [Ding & Wu (2024a)](/sources/ding-2024.md) — §2.1 (Eqs. (6)–(16), Thm. 2.1), §3.2 (arXiv v1).
- [Duan, Barsukow & Klingenberg (2025)](/sources/duan-2025.md) — §3.3, §4.1–4.2 (Eqs. (27)–(30), Lemmas 4.1–4.2, Remark 4.5), App. B (Lemmas B.1–B.2), Remark C.1 (arXiv v3).
- [Kiechle et al. (2025)](/sources/kiechle-2025.md) — §3.2 (Eqs. (12)–(24), Remarks 3.1–3.2, Fig. 5).
- [Allegrini & Vignal (2025)](/sources/allegrini-2025.md) — §3.2 (Eqs. (15f), (16), Remarks 5.1–5.2) (HAL author manuscript).
- [Liu et al. (2025b)](/sources/liu-2025-b.md) — §3.1 (Eq. (3.14)).
