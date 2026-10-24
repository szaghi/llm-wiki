---
type: Method
title: "Positivity-preserving numerical fluxes for Navier–Stokes"
description: "Zhang's Lax–Friedrichs-type Navier–Stokes flux, with a coefficient that includes viscous stress and heat flux, keeps density and internal energy positive; the page gives its total-flux finite-volume, finite-difference-splitting and LDG forms, Ching et al.'s multicomponent form on the viscous flux alone, graph-viscosity use in nodal DG, CFL conditions, adaptive time stepping and evidence."
status: established
aliases: [positivity-preserving viscous flux, positivity-preserving Navier–Stokes flux, Zhang's positivity-preserving flux, positivity-preserving convection–diffusion flux splitting, total-flux Lax–Friedrichs flux, separated viscous Lax–Friedrichs flux, gradient limiting]
tags: [positivity, bound-preserving, numerical-flux, finite-difference, finite-volume, dg]
timestamp: 2026-10-24T05:57:00Z
---

# Positivity-preserving numerical fluxes for Navier–Stokes

For the Euler equations, positivity of density and pressure is
obtained by writing a high-order update as a convex combination of
first-order updates that are positive by themselves. For the compressible
Navier–Stokes equations, [Fan, Zhang & Qiu (2022)](/sources/fan-2022.md)
state that the diffusion operator has no such first-order
positivity-preserving scheme, "the key difficulty" (§1.1). The remedy that four sources of the bundle use, due
to X. Zhang (2017) as they recall it, treats the **total** flux
$F(u,\nabla u)=f(u)-f^\nu(u,\nabla u)$, advective minus diffusive, as a
single convective flux and applies a
[Lax–Friedrichs](/methods/lax-friedrichs-flux.md)-type flux to it with a
dissipation coefficient $a^{\mathrm{NS}}$ (registry §10; the sources
write $\beta$) that accounts for the
viscous stress and the heat flux. The admissible set is
$G=\{\rho>0,\ \rho e>0\}$ with $\rho e=E-\tfrac12\rho\lvert v\rvert^2$,
convex because $\rho e$ is concave in $u$ for $\rho>0$
([bound preservation](/properties/bound-preservation.md)).
A fifth source, [Ching et al. (2025)](/sources/ching-2025.md), applies the
same kind of flux to the **viscous** flux alone and keeps a separate
inviscid flux (section below).

Page-local symbols: $\tau_{\mathrm v}$ and $q_{\mathrm h}$ the viscous
stress and heat flux (their normal components in multi-D). From the registry:
$N_{\mathrm{GL}}$ the number of Gauss–Lobatto points of a cell-average decomposition (§10) and
$\varpi=1/(N_{\mathrm{GL}}(N_{\mathrm{GL}}-1))$ its end weight on the unit interval (§8).

## The flux and the key lemma

In one dimension the flux at $x_{i+1/2}$ is
$$\hat F_{i+1/2}=\tfrac12\Big[F(u^-,\nabla u^-)+F(u^+,\nabla u^+)-a^{\mathrm{NS}}_{i+1/2}\big(u^+-u^-\big)\Big],\qquad
a^{\mathrm{NS}}_{i+1/2}>\max_{u^\pm,\nabla u^\pm}\Big[\lvert v\rvert+\frac{\sqrt{\rho^2q_{\mathrm h}^2+2\rho^2e\,\lvert\tau_{\mathrm v}-p\rvert^2}+\rho\lvert q_{\mathrm h}\rvert}{2\rho^2e}\Big]$$
([Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) Eqs. (3.4)–(3.5); Fan,
Zhang & Qiu (2022) Eqs. (2.8)–(2.9)). In 2D the coefficient of an
$x$-face uses $\lvert v\cdot n\rvert$, $\lvert q_{\mathrm h}\cdot n\rvert$
and $\lVert\tau_{\mathrm v}n-pn\rVert$ with $n=(1,0)$, and likewise in $y$
(Fan et al. 2021 Eqs. (3.23)–(3.24); 2022 Eqs. (3.21)–(3.22)). The
property that every proof uses, Lemma 6 of Zhang (2017) as cited, is
that for $u\in G$ and a coefficient above this bound
$$u\pm\frac{F(u,\nabla u)}{a^{\mathrm{NS}}}\in G\quad\text{for any }\nabla u,$$
since the gradient enters only through $\tau_{\mathrm v}$ and
$q_{\mathrm h}$, which are treated as free. The coefficient "has no
specific physical meaning" (Fan et al. 2022, §3.1); for
$\tau_{\mathrm v}=q_{\mathrm h}=0$ it reduces to
$\lvert v\rvert+\sqrt{(\gamma-1)p/(2\rho)}$ for an ideal gas, below
$\lvert v\rvert+c$ *(compiler check, not in the sources)*.

**Multicomponent reacting flows.** [Du & Yang (2022)](/sources/du-2022-b.md)
(§3.1, Eq. (3.5); §4.2, Lemma 4.1; 2D Lemma 5.1) extend the lemma to one
partial-density equation per species, with species diffusion velocities
and formation enthalpies, and prove it as an equivalence: $u\pm F/a^{\mathrm{NS}}\in G$
**iff** $a^{\mathrm{NS}}$ exceeds the largest root of a quadratic built
from the heat flux, the stress, the pressure and the species fluxes, and
$\lvert v+v^{\mathrm d}_k\rvert$ for each species diffusion velocity
$v^{\mathrm d}_k$ (page-local). The explicit form is on the
[Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md) page. For one
species without formation energy it is never larger than the bound
above *(compiler check, not in the sources)*. Their flux is also
"consistent", orthogonal to the constant vector that encodes
$\sum_kY_k=1$, which keeps the mass fractions summing to one and gives
$Y_k\le1$ from positivity of the partial densities (Def. 3.1, Thm 3.1).

## Finite volumes: Theorem 1 of Fan et al. (2021)

For a finite-volume (here moment-based Hermite WENO) scheme with a
reconstruction of degree $k$ (page-local), take the $N_{\mathrm{GL}}$-point
Gauss–Lobatto rule with $N_{\mathrm{GL}}=\lceil(k+3)/2\rceil$, so that it is exact for
degree $k$. Fan et al. (2021) (§3.1, Theorem 1, Eqs. (3.9)–(3.13)) prove
that the forward-Euler cell-average update stays in $G$ if the interface
states $u^\pm_{i\pm1/2}$ and the residual state
$(\bar u_i-\varpi u^+_{i-1/2}-\varpi u^-_{i+1/2})/(1-2\varpi)$ are in $G$,
under
$$\frac{\Delta t}{\Delta x}\max_i a^{\mathrm{NS}}_{i+1/2}\le\varpi=\frac1{N_{\mathrm{GL}}(N_{\mathrm{GL}}-1)}.$$
The update is rewritten as a convex combination of the residual state
and of four states of the form $u\pm F/a$, each admissible by the lemma.
In 2D the Gauss × Gauss–Lobatto decomposition weighted by
$\Delta t/\Delta x$ and $\Delta t/\Delta y$ gives
$\Delta t(1/\Delta x+1/\Delta y)\max a^{\mathrm{NS}}<\varpi$ (Theorem 2,
Eqs. (3.26)–(3.30); see
[optimal cell-average decomposition](/methods/optimal-cell-average-decomposition.md)).
A [scaling limiter](/methods/zhang-shu-scaling-limiter.md), density
first and then internal energy with floor $10^{-13}$, enforces the
hypotheses using point values only (Eqs. (3.14)–(3.15)). For their
quintic 1D reconstruction $N_{\mathrm{GL}}=4$ and $\varpi=1/12$, which is also the
time-step constant they use.

## Finite differences: a positivity-preserving flux splitting

A conservative finite-difference WENO scheme has no cell polynomial.
Fan, Zhang & Qiu (2022) (§3.1–3.2) replace its Lax–Friedrichs flux
splitting by a splitting of the total flux with the Navier–Stokes
coefficient, defined separately for each interface:
$$Z^\pm_{i+1/2,j}=\tfrac12\Big(u_j\pm\frac{F(u_j,\nabla u_j)}{a^{\mathrm{NS}}_{i+1/2}}\Big),\qquad j=i-r,\dots,i+r+1,$$
with $a^{\mathrm{NS}}_{i+1/2}$ the bound above maximized over the
$2r+2$ points of the stencil ($r=2$ for fifth-order WENO; page-local
$Z^\pm$). By the lemma each $Z^\pm$ is admissible. The split variables
are read, after Shu and Osher, as cell averages of auxiliary functions
$H^\pm$; WENO reconstructs $H^+$ at $x_{i+1/2}$ from the left and $H^-$
from the right in local characteristic variables of the Roe matrix of
$u_i$, $u_{i+1}$ ([characteristic decomposition](/methods/characteristic-decomposition.md)),
and
$$\hat F_{i+1/2}=a^{\mathrm{NS}}_{i+1/2}\Big[(H^+)^-_{i+1/2}-(H^-)^+_{i+1/2}\Big]$$
(Eqs. (3.2)–(3.5)). When $f^\nu\equiv0$ the scheme reduces to Zhang and
Shu's positivity-preserving finite-difference WENO for the Euler
equations, except that the splitting coefficient is nonlinear; the
authors state that a nonlinear splitting "seems more suitable" for the
nonlinear reconstruction, while its artificial-viscosity properties are
less understood (§1.3, §3).

**Theorem 1** (§3.2, Eqs. (3.6)–(3.11)). The scheme is
positivity-preserving if the reconstructed interface values and two
derived residual states per cell are in $G$, under
$$\frac{\Delta t}{\Delta x}\max_ia^{\mathrm{NS}}_{i+1/2}\le\frac{\varpi}{2}=\frac1{2N_{\mathrm{GL}}(N_{\mathrm{GL}}-1)},\qquad N_{\mathrm{GL}}=\Big\lceil\frac{2r+3}{2}\Big\rceil,$$
i.e. $1/24$ for fifth-order and $1/40$ for seventh-order WENO
*(compiler check, not in the sources)*. The proof splits the update into
two halves, one per interface, and decomposes the "cell average" of
each split variable with a degree-$2r$ interpolating polynomial that is
never used in the implementation. The authors call it a weak
positivity result, intrinsic to any finite-difference scheme read as a
finite-volume scheme, which needs a limiter to enforce its hypotheses
(Remarks 3.2–3.3): a scaling limiter on the reconstructed split values,
density then internal energy, floor $\min\{10^{-13},\bar\rho\}$, toward
the point value of the split variable (§3.3, Eqs. (3.12)–(3.14)). In 2D
the update is the average of two 1D updates with doubled $\Delta t$
(Eq. (3.23)).

**Separate diffusive splitting** (§4, Theorem 2). Alternatively, the
advective flux keeps global Lax–Friedrichs splitting and the diffusive
flux gets its own splitting with flipped signs,
$\tfrac12\big(u\mp f^\nu/a^\nu\big)$, "for the correct upwinding bias",
with $a^\nu$ the bound above without $\lvert v\rvert$ and without $p$
(registry §10), under
$\frac{\Delta t}{\Delta x}\max a^\nu\le\frac1{4N_{\mathrm{GL}}(N_{\mathrm{GL}}-1)}$; results of the
two variants show "no significant difference", and only the first is
shown (§5).

**Gradients.** Theorem 1 holds for any approximation of $\nabla u$, but a
positive scheme can still oscillate: a high-order linear approximation
of $v_x$ and $e_x$ oscillated, so the gradients of $\rho$, $\rho v$ and
$E$ are computed by a WENO finite-difference derivative and those of
$v$ and $e$ by the quotient rule (Remark 3.5; stated from tests, no
figure). Fan et al. (2021) reconstruct the derivatives with a hybrid
Hermite WENO of their own, with linear weights $11/459$, $44/765$,
$124/135$ in 1D (Appendix A; [Hermite WENO](/methods/hermite-weno.md)).

## Time stepping: halve and restart

The CFL bounds give $\Delta t=O(\Delta x)$, since $a^{\mathrm{NS}}$ is
$O(1)$ for smooth solutions, and do not imply the linear-stability
restriction $\Delta t=O(\mathrm{Re}\,\Delta x^2)$ of explicit
convection–diffusion; both are needed, and the positivity bound is
sufficient, not necessary (Fan et al. 2021, §3.3; 2022, Remark 3.3).
Both papers therefore start from
$\Delta t=\min\{\mathsf a\,\Delta x/\max(\lvert v\rvert+c),\ \mathsf b\,\mathrm{Re}\,\Delta x^2\}$
(page-local $\mathsf a$, $\mathsf b$) and, whenever a stage of
[SSP-RK3](/methods/ssp-runge-kutta.md) leaves $G$, halve $\Delta t$ and
restart the step; the restart terminates because the theorem holds once
$\Delta t$ is small enough (Fan et al. 2021 Eq. (3.33), $\mathsf a=1/12$,
$\mathsf b=0.001$; 2022 Algorithm 2 and Remark 3.4, $\mathsf a=0.6$,
$\mathsf b=0.001$). Du & Yang do the same with their exponential
integrator, doubling its damping rate and halving $\Delta t$ on failure,
and report very few recomputations (§6, Eqs. (6.1)–(6.2)).

## As graph viscosity in entropy-stable nodal DG

[Lin, Chan & Tomas (2023)](/sources/lin-2023.md) use the coefficient,
"motivated by Zhang", as the graph-viscosity coefficient of a low-order
scheme for nodal entropy-stable DG on quadrilaterals and triangles, with
the viscous terms explicit (§5, Eqs. 16–20). With $n$ a unit normal and
$\epsilon_0>0$ arbitrarily small ($10^{-14}$ in the runs), their
coefficient is

$$a^{\mathrm{NS}}(u,n)=\epsilon_0+\lvert n\cdot v\rvert+\frac{1}{2\rho^2e}\Big(\sqrt{\rho^2(q_{\mathrm h}\cdot n)^2+2\rho^2e\,\lVert n\cdot\tau_{\mathrm v}-pn\rVert^2}+\rho\lvert q_{\mathrm h}\cdot n\rvert\Big)$$

(Eq. 18, their $\beta$; $q_{\mathrm h}$ and $\tau_{\mathrm v}$ computed
from the auxiliary viscous variables of a local-DG discretization in
entropy variables), and the coefficient of a node pair is the larger of
the two nodal values times the norm of the low-order "normal" built from
the skew part of the sparse SBP operator (Eq. 17). The low-order update is
central flux differencing of the total flux plus this viscosity; written
as a convex combination of bar states
$\tfrac12(u_L+u_R)-\frac{1}{2a^{\mathrm{NS}}_{LR}}\,n\cdot\big(F(u_R)-F(u_L)\big)$,
each admissible by the lemma above (Lemma 5.1), it keeps $u$ in $G$ under
forward Euler and $\Delta t\le m_i/(2\lambda_i)$, $m_i$ the lumped mass and
$\lambda_i$ the summed coefficients of node $i$ (page-local; Theorem 5.2,
Eq. 27). The step scales as $O(h/N^2)$ (Remark 1). Taking the maximum of
this coefficient and a maximum wave-speed bound makes the low-order
scheme also semi-discretely entropy stable (Theorem 6.1, Eq. 45); for the
Euler equations the coefficient never exceeds the wave speed, so the
maximum is the wave-speed estimate itself (§6.2). The high-order update is blended
with it element by element ([convex limiting](/methods/convex-limiting.md),
[bound preservation](/properties/bound-preservation.md)). Unlike Guermond
et al. and Dzanic & Witherden, who split off the parabolic terms
implicitly, Lin et al. keep them explicit and accept the parabolic CFL
condition, which the positivity step does not imply; the hyperbolic step
scales as $O(h)$ and the parabolic one as $O(h^2\mathrm{Re})$, "not overly
restrictive" for $h=O(1/\mathrm{Re})$ (§1, Remark 2, §5).

## The viscous flux alone: multicomponent reacting Navier–Stokes

[Ching et al. (2025)](/sources/ching-2025.md) extend Zhang's flux to the
multicomponent, chemically reacting Navier–Stokes equations with thermally
perfect gases, in a primal DG scheme whose conserved species variables are
molar concentrations $\mathsf C_k$ (page-local; partial density $W_k\mathsf C_k$). Unlike
Zhang and Du & Yang, they penalize only the viscous flux, with
$\delta^\nu=\tfrac{a^\nu}2(u^+-u^-)$ ($\delta^\nu$ page-local, $a^\nu$ registry §10; the source
writes $\beta$), and keep an invariant-region-preserving inviscid flux, HLLC in
practice, which they find more accurate than Lax–Friedrichs (§1, §4.1, Remark 5;
[HLL-family solvers](/methods/hll-riemann-solvers.md)). Separating the two is what
lets them enforce an entropy bound on the convective part only, and changes the
admissible coefficient (Remark 5).

**Lemma 1** (§4.1, Eqs. (4.4)–(4.5)). Let $e^*=e-e\vert_{T=0}$ (page-local), so
that $e^*>0$ iff $T>0$, and $G=\{\rho>0,\ \rho e^*>0,\ \mathsf C_k\ge0\}$, convex because
$\rho e^*$ is concave. If $u\in G$ with every $\mathsf C_k>0$, then
$u\pm f^\nu\cdot n/a^\nu\in G$ for every unit $n$ when
$$a^\nu>\max\Big\{\max_k\frac{\lvert f^\nu_{\mathsf C_k}\cdot n\rvert}{\mathsf C_k},\ a_T\Big\},\qquad
a_T=\frac{\lvert b_T\rvert+\sqrt{b_T^2+2\rho^2e^*\lvert f^\nu_{\rho v}\cdot n\rvert^2}}{2\rho^2e^*},\qquad
b_T=\rho\,f^\nu_E\cdot n-\rho v\cdot\big(f^\nu_{\rho v}\cdot n\big),$$
with $f^\nu_{\rho v}$, $f^\nu_E$, $f^\nu_{\mathsf C_k}$ the momentum, energy and species
components of the viscous flux ($a_T$, $b_T$ page-local); the mass-conservation
correction of the diffusion velocities makes the net diffusive mass flux vanish,
which removes the remaining terms of the quadratic (Eqs. (4.7)–(4.8), Remark 4).
It is stated as sufficient, where Du & Yang state their (total-flux) condition as an
equivalence. Without species diffusion it recovers Zhang's monocomponent condition
(Remark 3). The species bound $\lvert V_k\cdot n\rvert$ ($V_k$ the diffusion velocity)
can blow up as $\mathsf C_k\to0$, and at $\mathsf C_k=0$ with a nonzero species flux no finite
coefficient works, because the species flux is not proportional to $\mathsf C_k$
(Remarks 2–3); the authors state that this holds whether the fluxes are treated
together or separately (§1).

**Split update** (§4.2–4.4). The forward-Euler cell-average update is written as
the mean of a convective and a viscous update, each with the doubled step
$\Delta t^*=2\Delta t$. The convective half stays in the entropy-bounded set under
$\Delta t^*a/h\le\tfrac12\min\{\theta_{\mathrm L},\theta_{\mathrm R}\}$ (from their
inviscid work), and the viscous half in $G$ under
$\Delta t^*/h\le\min\{\theta_{\mathrm L}/a^\nu_{\mathrm L},\theta_{\mathrm R}/a^\nu_{\mathrm R}\}$
(Thm 6), with $\theta_{\mathrm{L,R}}$ (page-local, not the Zhang–Shu factor) the endpoint weights of a Lv–Ihme-type
decomposition for an arbitrary positive quadrature; Theorem 8 is the
multidimensional version on curved elements
([optimal cell-average decomposition](/methods/optimal-cell-average-decomposition.md)).
For $N=0$ the viscous half is a convex combination for any positive coefficient,
even with zero concentrations (Eq. (4.16)). Boundary penalties and the modified
flux interpolation of Johnson & Kercher add their own constraints (§4.4.4, §4.5).
The entropy bound is enforced only on the convective half, because the minimum
entropy principle fails for Navier–Stokes with nonzero thermal diffusivity, as
they recall (§1; [entropy stability](/properties/entropy-stability.md)); the
limiter then scales density, species, $\rho e^*$ and, on the convective half
only, the entropy ([Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md)).

**Adaptive time stepping** (§4.6). The default viscous flux is BR2
([Bassi–Rebay discretizations](/methods/bassi-rebay-viscous-discretization.md)),
which does not guarantee positivity; if a stage leaves the admissible sets the step
is halved once and recomputed with BR2, and only if it fails again is it recomputed
with the Lax–Friedrichs-type viscous flux at all interfaces. A smaller step or a
flux switch is needed in "typically no more than ten percent of time steps".

**Gradient limiting at zero concentration** (§4.7, Eqs. (4.46)–(4.50)). A cell with
zero concentration and zero traces of species $k$ still turns negative under a net
inward diffusive flux, whatever the coefficient, because the limiter makes $\mathsf C_k\ge0$
only at finitely many points (Remark 11, Fig. 4.1). Since the species flux is
homogeneous in the gradient, the gradient in the viscous interface flux is
multiplied by a factor $\omega_{\mathrm g}\in[0,1]$ (page-local), computed pointwise
so that the species average stays non-negative; the coefficient then needs only
$a_T$ and need not be recomputed. It is applied where the step would otherwise be
halved three or more times; in the tests it acts only at the first step of the two
Lax–Friedrichs-type 2D detonation runs, where without it the step "would need to be
halved approximately thirty times". A projection to $N=0$ is a foolproof but
low-fidelity alternative (Remark 12).

**Evidence** (§5). Thermal-bubble advection–diffusion converges at order $N+1$ for
$N=1$–3 with BR2 and with the Lax–Friedrichs-type flux at CFL 0.1. In an H$_2$/O$_2$
premixed flame the scheme agrees "much more closely" with Cantera than species
clipping does. In a multicomponent viscous shock tube the entropy limiter damps
large-scale oscillations "significantly better" than the positivity limiter alone,
and the Lax–Friedrichs-type flux gives a smaller temperature overshoot than BR2
(Fig. 5.6); in a 2D H$_2$–O$_2$–Ar detonation with no-slip walls BR2 shows "much
smaller nonphysical instabilities" (Figs. 5.7–5.9), the result the authors follow
in preferring BR2 as default. Without the entropy limiter the minimum temperature of
the detonation approaches zero before 50 μs (Fig. 5.12).

## Evidence

- **Accuracy with the limiter active.** Fan et al. (2022), at
  $\mathrm{Re}=1000$ with energy $E=(10^{-10}+\sin^8x)/(\gamma-1)$: fifth
  order for WENO-JS5 and WENO-ZQ5 and seventh order for WENO-JS7 with
  $\epsilon=\Delta x^2$, e.g. 1D $L^1$ errors at 320 points
  $2.99\times10^{-8}$ (order 5.10), $9.96\times10^{-11}$ (7.36),
  $8.23\times10^{-9}$ (5.31), with the limiter acting on 0.20–1.25 % of
  the cells in 1D and 0.01–1.04 % in 2D at the finest mesh (Tables 5.1–5.2). Fan et al. (2021), at $\mathrm{Re}=100$:
  about fifth order in 1D and fourth order in 2D (Table 4.1).
- **Extreme tests.** Both papers run the
  [double rarefaction](/benchmarks/double-rarefaction-problem.md), 1D and
  2D [Sedov](/benchmarks/sedov-blast-wave.md), the
  [Leblanc shock tube](/benchmarks/leblanc-shock-tube.md) and the Mach
  5.09 [shock diffraction](/benchmarks/shock-diffraction.md) at
  $\mathrm{Re}=1000$ and $\infty$; Fan et al. (2022) add the Mach 2000
  [jet](/benchmarks/high-mach-astrophysical-jet.md) and a Mach 10
  reflection–diffraction problem. Fan et al. (2022) state that without
  the flux and the limiter all three WENO schemes "will blow up for all
  one- and two-dimensional examples" (§5); Fan et al. (2021) state the
  same for the hybrid HWENO predecessor on their Examples 4.3–4.7.
  Neither shows the blow-ups.
- **Nodal DG** (Lin et al., §8, Tables 2–5, 10–11). On a translating
  steady viscous shock at $M_0=3$ the low-order scheme is first order in
  $L^1$ (rates 0.84–0.97); the limited scheme converges at rates the
  authors describe as between $O(h^N)$ and $O(h^{N+1/2})$, limiting being
  active only on the coarsest mesh (e.g. $N=5$, $N_{\mathrm{el}}=160$ elements, page-local $N_{\mathrm{el}}$:
  $6.652\times10^{-7}$, rate 6.13). At $M_0=20$, $\mu=0.001$, the
  unlimited entropy-stable DG fails on coarse meshes and the limited one
  converges, and is "virtually identical" to the unlimited one at
  $N_{\mathrm{el}}=1600$. The [Daru–Tenaud viscous shock tube](/benchmarks/viscous-shock-tube.md)
  at $\mathrm{Re}=1000$ and 10000 runs robustly; with an added
  Persson–Peraire blending shock capturing the shock and boundary-layer
  structure "appear to be incorrect" against the references (§8.5,
  Figs. 12–14).
- **Reacting flows.** Du & Yang: third order with and without the
  limiter on stiff accuracy tests, and He/N$_2$ and H$_2$/O$_2$/Ar shock
  tubes that blow up without the bound-preserving limiter (§6,
  Figs. 6.1–6.3).

## Qualifications

- The coefficient is evaluated with the interface gradients; for strongly
  viscous flows it can exceed the inviscid wave speed considerably, and
  none of the sources quantifies the added dissipation. Du & Yang's
  running time step uses $\lvert v\rvert+\sqrt{p^2/(2\rho P)}$ without the
  viscous terms (Eq. (6.1)), so the proved CFL condition is not the one
  run; positivity in practice rests on the restart.
- **Heat-flux sign.** Fan et al. (2022) define $q_{\mathrm h}=\frac{1}{\mathrm{Re}}\frac{\gamma}{\mathrm{Pr}}(e_x,e_y)$
  and the diffusive energy flux $v\cdot\tau_{\mathrm v}-q_{\mathrm h}$
  (Eqs. (3.16)–(3.17)), but print the total flux with
  $+\frac{\gamma e_x}{\mathrm{Pr}}$ inside the diffusive part (Eq. (3.18)),
  as their 1D Eq. (2.6) does; Fan et al. (2021) print the same 2D form.
  The coefficient uses $\lvert q_{\mathrm h}\rvert$ and $q_{\mathrm h}^2$
  only, so the bound is unaffected.
- Fan et al. (2022) print $N_{\mathrm{GL}}=\lceil2r+3\rceil$ in Theorem 2, against
  $\lceil(2r+3)/2\rceil$ in Theorem 1, whose proof Theorem 2 follows; the
  Gauss–Lobatto exactness argument gives the latter. Fan et al. (2021)
  print $\rho e=(\gamma-1)(E-\frac12m^2/\rho)$ in Eq. (3.7), which is the
  pressure; their 2D Eq. (3.25) omits the factor.
- **Printed forms in Lin et al. (arXiv v2).** Their motivating condition
  (Eq. 20) prints $2\rho^2e\lVert n\cdot\tau_{\mathrm v}-pn\rVert$ without
  the square that their Eq. (18) and Fan et al. (2021) Eq. (3.5) carry;
  and the second component of $n\cdot\tau_{\mathrm v}$ in Eq. (18) has
  $u_2$ where the first component has $n_2$. Their Table 5c prints the
  $N=2$, $N_{\mathrm{el}}=200$ error as $9.858\times10^{-2}$, while the rates on either
  side, 1.23 and 1.54, follow from $9.858\times10^{-3}$
  *(compiler check, not in the sources:
  $\log_2(2.305\times10^{-2}/9.858\times10^{-3})=1.23$,
  $\log_2(9.858\times10^{-3}/3.382\times10^{-3})=1.54$)*.
- **Printed forms in Ching et al. (2025).** Substituting the viscous flux into
  $b_T$ gives the heat-flux term with the sign opposite to the one printed in
  Remark 3, $b_T=\rho q_{\mathrm h}\cdot n+\dots$; only $\lvert b_T\rvert$ enters $a_T$ in
  the monocomponent limit, so that case is unaffected *(compiler check, not in the
  sources)*. Their Appendix B prints the quadratic of Lemma 14 with the sign of its
  linear term opposite to what the expansion and the printed root need, and with
  $e$ in place of the $e^*$ of Lemma 1.
- **Which viscous flux is better.** Ching et al.'s evidence is mixed: the
  Lax–Friedrichs-type flux gives the smaller overshoot in 1D, BR2 the smaller
  oscillations in 2D (§5.3–5.4); the authors choose BR2 from the 2D runs.
- **Convexity assumed.** Ching et al. assume the entropy-bounded set convex
  throughout, although the entropy constraint is concave only when every
  concentration is positive; they state that this "does not seem to have any
  discernible negative effects" (§4).
- No source compares the cost of the finite-difference scheme with the
  finite-volume or DG versions; Fan et al. (2022) state that it is
  cheaper and easier to implement (§1.3).
- **Two statements of the positivity CFL of SSP-RK3.**
  [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) §3.3 state that Theorems
  1 and 2 "still hold for (2.6) if the CFL is one third of (3.12) and
  (3.30)", (2.6) being the Shu–Osher form of SSP-RK3.
  [Fan, Zhang & Qiu (2022)](/sources/fan-2022.md) §3.5 state for the same
  SSP-RK3 that positivity "still holds due to convex combinations" of
  forward-Euler steps, with no reduction of the CFL bound. Both are
  sufficient conditions and neither paper calls the other's bound wrong,
  so they do not conflict (the same pair of statements, Fan et al. 2021
  against Wong et al. 2021, is a qualification on the
  [SSP Runge–Kutta](/methods/ssp-runge-kutta.md) page). In the Shu–Osher
  form each stage is a convex combination of states and forward-Euler
  steps of size $\Delta t$, which gives the forward-Euler bound unchanged
  *(compiler check, not in the sources)*.

# Citations

- [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) — §1; §3.1–3.3, Eqs. (3.4)–(3.15), (3.23)–(3.33), Theorems 1–2; §4, Ex. 4.1–4.7, Tables 4.1–4.2; Appendix A.
- [Fan, Zhang & Qiu (2022)](/sources/fan-2022.md) — §1.1–1.3; §2.2, Eqs. (2.7)–(2.9); §3.1–3.5, Eqs. (3.1)–(3.24), Theorem 1, Remarks 3.2–3.5, Algorithms 1–2; §4, Theorem 2; §5, Tables 5.1–5.2, Ex. 5.2–5.8.
- [Lin, Chan & Tomas (2023)](/sources/lin-2023.md) — arXiv v2: §1; §5, Eqs. (16)–(28), Lemma 5.1, Theorem 5.2, Remarks 1–2; §6.2, Theorem 6.1, Eq. (45); §8.1.2, Tables 2–5; §8.5, Figs. 12–14.
- [Du & Yang (2022)](/sources/du-2022-b.md) — §3.1, Eqs. (3.4)–(3.5), Def. 3.1, Thm 3.1; §4.2, Lemma 4.1; §5, Lemma 5.1; §6, Eqs. (6.1)–(6.2), Figs. 6.1–6.3.
- [Ching et al. (2025)](/sources/ching-2025.md) — §1; §4.1, Lemma 1, Eqs. (4.4)–(4.10), Remarks 2–5; §4.2–4.5, Thms 6, 8, Eqs. (4.12)–(4.44); §4.6; §4.7, Eqs. (4.45)–(4.50), Remarks 11–12; §5, Figs. 4.1, 5.1–5.12; App. B.
