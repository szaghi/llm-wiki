---
type: Method
title: "Flux globalization for balance laws"
description: "Flux globalization absorbs the integral of the source or non-conservative product into a global flux $K$, so that steady states, moving and discontinuous ones included, are states of constant $K$; Kurganov et al. build a well-balanced path-conservative central-upwind scheme on it, Ciallella et al. an arbitrary-order WENO finite-volume scheme."
status: established
aliases: [global flux, global flux formulation, flux-globalization-based scheme, GF-WENO, flux-globalized central-upwind scheme, quasi-conservative form]
tags: [well-balanced, finite-volume, central-scheme, weno, numerical-flux]
timestamp: 2026-10-23T03:53:00Z
---

# Flux globalization for balance laws

**Flux globalization** rewrites a balance law $\partial_tu+\partial_xf(u)=S(u)$ in the
quasi-conservative form

$$\partial_tu+\partial_xK=0,\qquad K=f(u)-\mathcal G,\qquad \mathcal G(x,t)=\int_{x_{\mathrm b}}^{x}S\big(u(\xi,t),\xi\big)\,d\xi,$$

with $K$ the **global flux**, $\mathcal G$ its global (source) part and $x_{\mathrm b}$ an
arbitrary lower limit, in practice the left boundary (page-local $K$, $\mathcal G$,
$x_{\mathrm b}$; [Kurganov et al. (2023)](/sources/kurganov-2023.md), §1, Eqs. (1.6)–(1.7);
[Ciallella et al. (2023)](/sources/ciallella-2023.md), §2.1, Eqs. (3)–(4)). Steady states are
then the states with $K\equiv$ const, which covers moving and discontinuous equilibria and
not only the lake at rest. Ciallella et al. write $K=f+R$ with $R=-\int^xS$; Kurganov et al.
write $K=F-R$ with $R=\int^xS$: the same global flux under opposite signs of the global part.

For a non-conservative system, written in the registry form
$\partial_tu+\partial_xf(u)+\mathcal C(u)\partial_xu=0$, the global part is
$\mathcal G=-\int_{x_{\mathrm b}}^x\mathcal C(u)\,\partial_\xi u\,d\xi$, and $K=f+\int^x\mathcal C\,\partial_\xi u$
is the global flux that [Chu et al. (2022)](/sources/chu-2022.md) feed into A-WENO
([path-conservative schemes](/methods/path-conservative-scheme.md)). Kurganov et al. write the
product on the right-hand side, $\partial_tU+\partial_xF=B(U)\partial_xU$, so their $B$ is
$-\mathcal C$ (§1, Eq. (1.1)).

**History, as recalled.** Ciallella et al. (§1) trace the global flux to Gascón and Corberán,
its use in shock capturing for balance laws to Donat and co-workers, and its use in fully
well-balanced schemes to Chertock, Kurganov and co-workers and to Cheng et al.; they add that
the approach is "agnostic of the specific form of the equilibrium". Kurganov et al. (§1)
explain why the earlier flux-globalized schemes use central-upwind fluxes: upwind schemes need
Riemann solvers, which are hard to obtain for global fluxes.

## Equilibrium variables

Kurganov et al. (§1, Eqs. (1.4)–(1.5)) assume that the steady-state operator factors as
$\partial_xf+\mathcal C\,\partial_xu=\mathsf M(u)\,\partial_x\mathsf E(u)$, with an invertible matrix
$\mathsf M$ and algebraically defined **equilibrium variables** $\mathsf E(u)$ (page-local), so
that steady states are $\mathsf E\equiv$ const. Integral (non-algebraic) equilibrium variables are
left to future work. The two systems they treat:

- **Isentropic nozzle flow** with cross-section $\Sigma(x)$ (page-local; the source's $a$),
  $p=\kappa_{\mathrm p}\rho^\gamma$ (page-local constant $\kappa_{\mathrm p}$, the source's
  $\kappa$): unknowns $(\Sigma\rho,\Sigma\rho v,\Sigma)$, non-conservative product
  $p\,\partial_x\Sigma$ in the momentum equation, equilibrium variables the discharge
  $q_{\mathrm n}=\Sigma\rho v$ and the Bernoulli energy
  $\tfrac12v^2+\frac{\kappa_{\mathrm p}\gamma}{\gamma-1}\rho^{\gamma-1}$ (§5, Eqs. (5.1)–(5.5));
- **two-layer shallow water**, equilibrium variables $q_1$, $q_2$ and the layer energies
  $\frac{q_1^2}{2h_1^2}+g(h_1+h_2+b)$, $\frac{q_2^2}{2h_2^2}+g(rh_1+h_2+b)$ (§6; notation of
  [shallow-water equations](/definitions/shallow-water-equations.md)).

For the single-layer shallow-water equations with bottom and Manning friction, Ciallella et
al. (§2.2, Eq. (7)) take the two components of the global flux themselves as equilibrium
variables, $q\equiv q_0$ and $K\equiv K_0$; this holds also across a hydraulic jump, where the
smooth energy invariant is discontinuous (§2.2, Eqs. (8)–(9)).

## The global part is discontinuous for non-conservative products

In the earlier flux-globalized central-upwind schemes, as recalled by Kurganov et al. (§1, §3),
$K$ is reconstructed, the interface states are recovered from $K(u^\pm)=K^\pm$, and the global
part is accumulated by quadratures, $\mathcal G_{i+1/2}=\mathcal G_{i-1/2}+\int_{I_i}S\,dx$,
from $\mathcal G=0$ at the left boundary (Eqs. (3.2)–(3.5)). This relies on $\mathcal G$ being
continuous, true for a balance law even when $u$ jumps. For a non-conservative product it is
"no longer valid", and the interface contribution "was neglected in the derivation of the
original flux globalization based central-upwind schemes" (§1, §8). The straightforward
scheme of their §3 therefore preserves only smooth steady states.

Their **flux-globalized path-conservative central-upwind scheme** (§4, Eqs. (4.1)–(4.4)) lets
$\mathcal G$ jump at every interface and accumulates the one-sided values with the
[path-conservative](/methods/path-conservative-scheme.md) cell and interface integrals:

$$\mathcal G^-_{1/2}=0,\qquad \mathcal G^+_{i+1/2}=\mathcal G^-_{i+1/2}-\mathcal B_{\Psi,i+1/2},\qquad \mathcal G^-_{i+1/2}=\mathcal G^+_{i-1/2}-\mathcal B_i,\qquad K^\pm_{i+1/2}=f(u^\pm_{i+1/2})-\mathcal G^\pm_{i+1/2},$$

with $\mathcal B_i$, $\mathcal B_{\Psi,i+1/2}$ the cell and path integrals of $\mathcal C\,\partial_xu$
as written on the path-conservative page (the source's $B_j$, $B_{\Psi,j+1/2}$ with the opposite
sign). $K$ is no longer reconstructed. Instead:

1. the equilibrium variables are reconstructed, piecewise linearly with the generalized minmod
   limiter, and $u^\pm_{i+1/2}$ is recovered from $\mathsf E(u^\pm)=\mathsf E^\pm$ (Eqs.
   (4.5)–(4.6)); solutions may be non-unique, and a physical criterion selects one;
2. the path is the segment **linear in the equilibrium variables**, $\mathsf E(\Psi(\mathsf s))=\mathsf E^-+\mathsf s(\mathsf E^+-\mathsf E^-)$ (Eq. (4.7));
3. the integrals are evaluated by the trapezoidal rule on
   $\partial_xf+\mathcal C\,\partial_xu=\mathsf M\,\partial_x\mathsf E$ (Eqs. (4.8)–(4.10)), e.g.
   $$\mathcal B_{\Psi,i+1/2}=\tfrac12\big[\mathsf M(u^+_{i+1/2})+\mathsf M(u^-_{i+1/2})\big]\big(\mathsf E^+_{i+1/2}-\mathsf E^-_{i+1/2}\big)-\big(f(u^+_{i+1/2})-f(u^-_{i+1/2})\big)$$
   (Eq. (4.10) in this page's sign).

The numerical flux is the [central-upwind](/methods/central-upwind-scheme.md) flux of $K$,
with the diffusion term rebuilt from modified states (below).

**Theorem 4.1** (Kurganov et al., §4.1). If the discrete data are at a steady state,
$\mathsf E_i\equiv$ const, then $K^+_{i+1/2}=K^-_{i+1/2}=K^+_{i-1/2}$ for all $i$. The
reconstructed equilibrium variables are constant, so the trapezoidal terms vanish and the flux
differences cancel the integrals.

**Diffusion term.** At a discrete steady state $\mathsf E^+=\mathsf E^-$ does not imply
$u^+=u^-$ (e.g. at a jump of $\Sigma$ or of the bottom), and the diffusion term
$\frac{a^+a^-}{a^+-a^-}(u^+-u^-)$ of the central-upwind flux would leave a residual (§4.2,
Eqs. (4.13)–(4.14)). Kurganov et al. replace $u^\pm$ in the diffusion term only by modified
states $\check u^\pm$ that solve a modified inversion $\check{\mathsf E}(\check u^\pm)=\mathsf E^\pm$ (page-local),
built so that $\check u^+=\check u^-$ whenever $\mathsf E^+=\mathsf E^-$ and
$\check u^\pm=u^\pm+O(\Delta x^2)$ for smooth solutions (Eqs. (4.15)–(4.16)). For systems
whose last component is static (cross-section, bottom), the modification replaces its two
interface values by their average (Remark 4.3, Eqs. (4.17)–(4.19)). For the two-layer system
the inversion can have several solutions even at a steady state; their Algorithm 6.1 solves
the left system first and uses its solution as the Newton initial guess of the right one, so
that both coincide at steady states (§6). Newton solvers for the nozzle (a scalar equation
with up to two positive roots, sub- and supersonic) and the two-layer cubics are in Appendices
A–B.

**Local form.** Substituting the recursions into the flux difference, the scheme becomes the
local path-conservative central-upwind scheme with equilibrium-variable reconstruction, the
linear-in-$\mathsf E$ path, the trapezoidal quadratures and the modified diffusion term (Remark
4.2). The authors keep the global form to verify well-balancing and for future
non-algebraic $\mathsf E$ and high-order extensions; the local form eases multi-D and
unstructured extensions.

## Arbitrary order: global-flux WENO finite volumes

[Ciallella et al. (2023)](/sources/ciallella-2023.md) (§3) build the global-flux scheme at
orders 3 and 5 for the shallow-water equations with bottom and friction, on a uniform grid of
cell averages:

$$\frac{d\bar u_i}{dt}+\frac1{\Delta x}\big(\hat f_{i+1/2}-\hat f_{i-1/2}\big)=0\qquad(\text{Eq. (11)}),$$

1. **Cell averages of the global flux** (§3.1, Eqs. (15)–(23)): $\bar K_i$ is the 4-point
   Gauss–Legendre average of $f$ at WENO-reconstructed states plus the average of $\mathcal G$
   at the same nodes; $\mathcal G$ is accumulated cell by cell from $0$ at the left boundary by
   exact integration of the Lagrange interpolant of $S$ through the Gauss nodes, with a jump
   $[\![\mathcal G_{i+1/2}]\!]$ added at each interface because the reconstructed bottom is
   discontinuous there.
2. **WENO reconstruction of the global-flux averages** to the interfaces
   ([WENO-JS](/methods/weno-js-reconstruction.md) weights, $q=2$, $\epsilon=10^{-6}$; WENO3 and
   WENO5, with point-dependent linear weights at the Gauss nodes, §3.2, Eqs. (24)–(29)).
3. **Upwind flux of the homogeneous system**:
   $\hat f_{i+1/2}=R\Lambda^+L\,K^-_{i+1/2}+R\Lambda^-L\,K^+_{i+1/2}$, with $R$, $L$ the
   eigenvectors of the Roe-averaged Jacobian of the homogeneous shallow-water system and
   $\Lambda^\pm$ the diagonal $0/1$ selectors of positive and negative eigenvalues (page-local;
   Eqs. (12)–(14); [Roe solver](/methods/roe-riemann-solver.md)). Other fluxes such as Rusanov
   are admissible if their dissipation vanishes at steady states, e.g. through cut-off
   functions (§3).
4. **Interface depths** from the reconstructed $q$, $K$ and $\mathcal G$ by solving the cubic
   $K-\mathcal G=q^2/h+\tfrac g2h^2$: no positive root unless $q^4<8(K-\mathcal G)^3/(27g)$, in
   which case $h$ comes from the reconstructed free surface; otherwise one negative and two
   positive (sub- and supercritical) roots, and the one closest to the reconstructed
   $H_{\mathrm s}-b$ is chosen (App. A, Eqs. (55)–(59), technique of Cheng et al.).
5. **Time stepping** by explicit [deferred correction](/methods/deferred-correction.md) of the
   matching order, CFL $0.5$ (§4–§5).

**Proposition 3.1** (global-flux property): if $\bar K_i=K_0$ for all $i$, the data are a steady
state of the scheme, because every candidate polynomial reproduces a constant and the upwind
flux then returns $K_0$. *(compiler check, not in the sources: the last step uses
$R(\Lambda^++\Lambda^-)L=I$, which Eq. (14) defines only for non-zero eigenvalues.)*
**Proposition 3.3** (lake at rest, App. B): with the source split as
$-gh\,\partial_xb=-gH_{\mathrm s}\partial_xb+g\,\partial_x(b^2/2)$ (after Xing and Shu), the WENO
weights of $h$ and $b$ both computed from $H_{\mathrm s}$, and the interface jump

$$[\![\mathcal G_{i+1/2}]\!]=-g\,\tfrac12\big(H^+_{\mathrm s}+H^-_{\mathrm s}\big)_{i+1/2}\big(b^+-b^-\big)_{i+1/2}+g\Big(\tfrac12(b^+)^2-\tfrac12(b^-)^2\Big)_{i+1/2}$$

(Eq. (38) in this page's sign of $\mathcal G$), the scheme preserves the lake at rest exactly.
The jump is "similar to classical strategies used in well-balanced path conservative methods"
with a linear path (§3.3), and including it does not affect Proposition 3.1 (Remark 3.4).

The discrete steady states of the scheme are not the analytical equilibria: the scheme at
equilibrium acts like a nonlinear multistep integrator of the steady ODE, for which no
explicit ODE-solver analogy was found (Remark 3.2), and the method "is not exactly well
balanced with respect to all analytically computable equilibria" (§1). Ciallella et al. add
that the simple averaging of the global part used by Cheng et al. "is not enough to reach more
than second order of accuracy" (§3).

## Evidence

- **Kurganov et al. (2023)** (§7; second order, [SSP-RK3](/methods/ssp-runge-kutta.md), CFL
  $1/2$, generalized minmod with $\theta=1.3$, page-local). A discontinuous nozzle steady state
  ($\Sigma=1.5$ for $x<0$, $2.5$ for $x>0$, $N_x=200$, $t=20$) is preserved with $L^1$ and
  $L^\infty$ errors $0$ in $q_{\mathrm n}$ and $8.88\times10^{-16}$ in the Bernoulli energy (Table
  7.1); the non-well-balanced PCCU scheme and the §3 scheme do not preserve it (Fig. 7.1). From
  a Riemann datum the scheme converges to the discontinuous steady state with discharge
  $-13.583$, the §3 scheme to $-13.973$, against the exact $\approx-13.446$ (§7.1). On a
  discontinuous convergent–divergent nozzle the §3 scheme produces unphysical spikes and
  converges to a state with non-constant energy (Ex. 4). For two-layer shallow water a
  discontinuous steady state over a step is preserved exactly while the original PCCU scheme
  fails (Ex. 5), and a moving-water steady state over a bump with two jumps is reached by
  $t=100$ (Ex. 7).
- **Ciallella et al. (2023)** (§5; domain $[0,25]$, CFL $0.5$). Lake at rest preserved at
  $L^2$ errors of about $10^{-13}$ in $h$ and $10^{-15}$–$10^{-14}$ in $q$ for $N_x=25$–$800$
  (Table 1). On sub- and supercritical flows over a smooth bump all schemes show orders 3 and 5,
  but the global-flux scheme has errors 2 to 5 orders of magnitude below a standard WENO
  finite-volume scheme with Rusanov flux (Figs. 7–8). The authors' cost estimate: the
  global-flux scheme takes about twice the time per mesh, and for $10^4$ times smaller errors at
  fifth order the standard scheme would need about 20 times the time (§5.3). *(compiler check,
  not in the sources: a mesh factor $10^{4/5}\approx6.3$ with cost $\propto N_x^2$ gives about 40,
  halved to 20.)* $q$ and $K$ are preserved to about $10^{-9}$ in the moving-equilibrium
  tests, and on a transcritical flow with a shock, a step bottom and Manning friction
  $n_{\mathrm M}=0.05$ (page-local Manning coefficient) the standard WENO5 oscillates while the
  global-flux scheme does not (Figs. 11, 16–19).

## Qualifications

- **Two notions of preserving moving equilibria.** Kurganov et al. preserve every discrete
  state with constant reconstructed equilibrium variables (Theorem 4.1); Ciallella et al.
  preserve every discrete state with constant global-flux averages (Prop. 3.1) and state that
  these are not the analytical equilibria. Both are well-balanced for their own discrete steady
  states; neither claims exact preservation of interpolated analytical moving states. See
  [well-balancing](/properties/well-balancing.md).
- **A global method in name.** By Remark 4.2 the scheme of Kurganov et al. is a local
  path-conservative central-upwind scheme with modified ingredients; the global form is a
  derivation and verification device.
- Kurganov et al. print, for the discontinuous nozzle test with $\gamma=1.6$, the steady values
  "$q\equiv3$ and $E\equiv5.5$" (§7.1). *(compiler check, not in the sources: with
  $\kappa_{\mathrm p}=1$ and the printed states, $\gamma=1.6$ gives $q_{\mathrm n}=3$ and Bernoulli
  energy $14/3$ on both sides, a steady state; $5.5$ is the left-state energy for $\gamma=1.4$, at
  which the right state has $q_{\mathrm n}=2.715$ and energy $5.456$. The printed $5.5$ is a slip,
  not an inconsistency of the test.)*
- Ciallella et al.'s Eq. (36) prints the cell average of the split bottom source with the sign
  of $-\bar S_i$: with Eq. (37) it would give the global part an increment opposite to Eqs.
  (35), (40) and (62c). *(compiler check, not in the sources: from the split form (32),
  $\int_{I_i}S\,dx=-g\int H_{\mathrm s}\partial_xb\,dx+g\big[\tfrac12b^2\big]$, whereas (36) prints
  $+g\int H_{\mathrm s}\partial_xb\,dx-g\big[\tfrac12b^2\big]$.)* Their printed (62e) and (63) carry
  $b^R_{i-1/2}$ and $b^L_{i-1/2}$ where the definition (38) requires the values at $x_{i+1/2}$;
  the conclusion of Proposition 3.3 is unaffected. The version read is an author manuscript
  dated after the 2023 issue.
- Ciallella et al.'s Table 1 orders reproduce exactly when $N_x-1$ replaces $N_x$ in the
  spacing, and the non-well-balanced WENO3 orders settle at 3.5–3.7, above 3, although the text
  says they match the reconstruction order (§5.1).
- Kurganov et al. report no convergence-order study; "second order" is the formal order of the
  piecewise-linear reconstruction.

# Citations

- [Kurganov et al. (2023)](/sources/kurganov-2023.md) — §1 (Eqs. (1.1), (1.4)–(1.8)), §2 (Remark 2.2), §3 (Eqs. (3.2)–(3.5)), §4 (Eqs. (4.1)–(4.19), Theorem 4.1, Remarks 4.2–4.3), §5, §6 (Algorithm 6.1), §7 (Table 7.1, Exs. 1–7), §8, Apps. A–C.
- [Ciallella et al. (2023)](/sources/ciallella-2023.md) — §1, §2 (Eqs. (1)–(9)), §3 (Eqs. (11)–(40), Props. 3.1, 3.3, Remarks 3.2, 3.4), §4, §5 (Table 1, Figs. 7–19), Apps. A–B (author manuscript).
- [Chu et al. (2022)](/sources/chu-2022.md) — §4, §8.
