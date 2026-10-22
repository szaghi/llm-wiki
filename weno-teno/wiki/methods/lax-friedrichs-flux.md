---
type: Method
title: "Lax–Friedrichs (Rusanov) flux and flux splitting"
description: 'The Lax–Friedrichs two-point flux and the Lax–Friedrichs flux splitting $f^\pm=\tfrac12(f\pm au)$, global or local, per field or scalar: the default upwinding of finite-difference WENO and TENO, the surface flux of DG, the low-order flux whose bar-state structure makes invariant-domain and bound-preserving proofs work, its positivity-preserving extension to the total Navier–Stokes flux, and its entropy-stable variant on entropy-variable jumps.'
status: established
aliases: [Rusanov flux, local Lax–Friedrichs, LLF, global Lax–Friedrichs, GLF, Lax–Friedrichs flux splitting, Rusanov flux splitting]
tags: [numerical-flux, finite-difference, bound-preserving, weno, teno]
timestamp: 2026-10-23T10:00:00Z
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
([Li et al. (2022)](/sources/li-2022-b.md), §2, Eqs. (1)–(4);
[Ye et al. (2022)](/sources/ye-2022.md), Eq. (20), $a=\max\lvert f'(u)\rvert$).

## Naming conventions

The sources disagree on words, not on mathematics. [Jeong et al. (2022)](/sources/jeong-2022.md)
(§5, Eq. (44)) call $a=\max\lvert f'(u)\rvert$ "over the whole range of" $u$ "the local numerical
viscosity", a global bound under a local name. [Fu (2023)](/sources/fu-2023.md)
(§3.4 Algorithm 1) calls "Rusanov" the splitting with a **global** per-field maximum speed;
[Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md) (§3) and
[Wang et al. (2023)](/sources/wang-2023-b.md) (§1) use "Rusanov" for the **local** flux;
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
speed over the whole domain). Users: global LF in [Li et al. (2022)](/sources/li-2022-b.md)
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
with $a=\max\rho(\partial f/\partial u)$ in the A-WENO of [Li et al. (2023)](/sources/li-2023.md)
(Eq. (35)). Three sources make the choice of speed matter:

- **Local characteristic LF for turbulence.** [Li et al. (2022)](/sources/li-2022.md) use
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
- **As a first-order limit.** The first-order version of the
  [discrete kinetic relaxation scheme](/methods/discrete-kinetic-relaxation-scheme.md) of
  [Abgrall & Nassajian Mojarrad (2024)](/sources/abgrall-2024.md) "amounts to global
  Lax–Friedrichs" and is the fallback of its MOOD stabilization (§3.2.2); the first-order
  viscosity $C_{\max}h\lambda_{\max}$ (page-local constant and mesh size) of the residual-viscosity
  continuous finite elements of [Dao & Nazarov (2022)](/sources/dao-2022.md) reproduces 1D
  Lax–Friedrichs for $C_{\max}=0.5$, stated without proof (§4.2;
  [artificial viscosity](/methods/artificial-viscosity.md)).
- [Arun et al. (2022)](/sources/arun-2022.md) (§5) use "a Rusanov-type approximate Riemann
  solver" on hydrostatically reconstructed interface states (no formula printed; see
  [well-balancing](/properties/well-balancing.md)).
- In [A-WENO](/methods/alternative-weno.md) the Rusanov flux was the usual finite-volume
  building block before adaptive-diffusion variants
  ([Wang et al. (2023)](/sources/wang-2023-b.md), §1, App. A); their "OLD" flux is LF with a
  single adaptively reduced coefficient
  ([adaptive-diffusion central-upwind flux](/methods/adaptive-diffusion-central-upwind-flux.md)).

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
- **The original sparse IDP DG.** [Pazner (2021)](/sources/pazner-2021.md) chooses the
  LLF interface flux of his DGSEM because it is compatible with graph viscosity: its jump
  term merges with the in-element graph viscosity
  $d_{ij}=\max\{a(u_i,u_j)\lVert c_{ij}\rVert,\ a(u_j,u_i)\lVert c_{ji}\rVert\}$ into a single
  graph form (§2, Eq. (6); §3.1, Eqs. (30)–(35); page-local $c_{ij}$, $d_{ij}$ the graph
  coefficients and viscosities, $a(\cdot,\cdot)$ the maximal wave speed of the pair), and
  the forward-Euler update is a convex combination of the bar states
  $\tfrac12(u_i+u_j)+\frac{\hat c_{ij}}{2\hat d_{ij}}\cdot\big(f(u_j)-f(u_i)\big)$ (Eqs. (38)–(39),
  Prop. 7). See [convex limiting](/methods/convex-limiting.md).
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
- **Downwinding by sign flip.** [Dzanic et al. (2022)](/sources/dzanic-2022.md) (§2, §4.2) obtain
  the downwind-biased divergence of their time-reversibility shock indicator by negating the
  dissipative term of the Rusanov flux (Davis wave speeds) used in the forward step; the defect
  between the state and its forward-then-backward image drives an
  [artificial viscosity](/methods/artificial-viscosity.md). In their first-order analysis
  with upwind fluxes the viscosity tends to $c_\mu a\Delta x$, which for $c_\mu=\tfrac12$ is the
  viscosity that turns a central scheme into first-order upwind (§3.1, Eqs. (18)–(20); page-local
  constant $c_\mu$).

## Entropy stability: dissipation on entropy-variable jumps

Plain LF dissipation on the conservative jump, $\tfrac a2[\![u]\!]$, added to an
entropy-conservative flux is not entropy stable for MHD
([Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md), §3.3.1, citing Derigs et al.
2017). Their "ES Rusanov" flux replaces $[\![u]\!]$ by $\frac{\partial u}{\partial w}[\![w]\!]$
written with Barth's eigenvector scaling,

$$h=f^{\mathrm{ec}}(u^-,u^+)-\tfrac12R\,\lvert\Lambda\rvert\,\mathcal Z\,R^\top[\![w]\!],$$

with $\lvert\Lambda\rvert$ diagonal with every nonzero entry equal to the largest advective
eigenvalue and $\mathcal Z$ the diagonal Barth scaling, $\frac{\partial u}{\partial w}=R\mathcal ZR^\top$
(page-local $\Lambda$, $\mathcal Z$); the entropy production is
$-\tfrac12[\![w]\!]^\top R\lvert\Lambda\rvert\mathcal ZR^\top[\![w]\!]\le0$ (Eqs. (57)–(60)). It is
their default wherever dissipation is needed (§6). See
[entropy-conservative fluxes](/methods/entropy-conservative-flux.md) and
[entropy stability](/properties/entropy-stability.md).

## Qualifications

- Wu & Shu's LF statements are proved for the first-order scheme; the high-order FV/DG MHD
  result uses Gauss-quadrature LF fluxes with a viscosity bound and its proof is "omitted"
  (Thm. 6.2).
- [Fu (2023)](/sources/fu-2023.md) mis-cites the Rusanov and Roe references by one number in
  Algorithm 1 (a slip of the review, not a disagreement).

# Citations

- [Li et al. (2022)](/sources/li-2022-b.md) — §2 (Eqs. (1)–(4)), Eq. (38).
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
- [Wang et al. (2023)](/sources/wang-2023-b.md) — §1, App. A.
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
- [Li et al. (2023)](/sources/li-2023.md) — Eq. (35), §4.2.
- [Li et al. (2022)](/sources/li-2022.md) — §3.4, §4.4.
- [Wan & Xia (2022)](/sources/wan-2022.md) — §4 (Exs. 4.4, 4.5, 4.7, 4.12–4.13).
- [Boscarino et al. (2022)](/sources/boscarino-2022.md) — §1, §3.3.1 (Eq. (3.32)) (arXiv v2).
- [Kou et al. (2022)](/sources/kou-2022.md) — Eq. (15).
- [Mossier et al. (2022)](/sources/mossier-2022.md) — §8.9.
- [Lesur et al. (2023)](/sources/lesur-2023.md) — §2.3, §4.2 (Fig. 7).
- [Abgrall & Nassajian Mojarrad (2024)](/sources/abgrall-2024.md) — §3.2.2.
- [Dao & Nazarov (2022)](/sources/dao-2022.md) — §4.2.
