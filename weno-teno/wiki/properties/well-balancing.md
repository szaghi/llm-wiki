---
type: Property
title: "Well-balancing"
description: "A scheme for a balance law is well-balanced if it preserves a steady state such as the lake at rest or a hydrostatic atmosphere exactly; in this bundle it follows from affine-invariant WENO weights, stationary-contact-preserving fluctuations, hydrostatic reconstruction for Euler with gravity in an asymptotic-preserving scheme, and evolution of the deviation from a known MHD equilibrium."
status: established
aliases: [well-balanced scheme, C-property, lake-at-rest property, exact preservation of still water, hydrostatic reconstruction, subtraction technique, perturbation well-balancing]
tags: [well-balanced, weno, finite-difference, finite-volume, central-scheme, asymptotic-preserving]
timestamp: 2026-10-22T12:00:00Z
---

# Well-balancing

For a balance law $\partial_tu+\partial_xf(u)=S(u)$, a discretization is **well-balanced** for
a given steady state if discrete data equal to that steady state stay unchanged up to
round-off, i.e. the discrete flux divergence and the discrete source cancel exactly. For the
shallow-water equations the steady state of interest is still water, "lake at rest";
[Wang & Don (2022)](/sources/wang-2022-b.md) (§2–§3.3) use "WB-property" and "C-property"
for its exact preservation. Below, $h$ is the water depth, $b$ the bottom, $H_{\mathrm s}=h+b$
the free-surface level and $g$ gravity (page-local; $h$ is not a numerical flux here).

## Shallow water: WB from affine invariance

Following Li, Caleffi & Qi (2015) as recalled by Wang & Don (§3.3, Eqs. (26)–(28)), the
equations are written in $(H_{\mathrm s},hv)$,

$$\partial_t\begin{pmatrix}H_{\mathrm s}\\ hv\end{pmatrix}+\partial_x\begin{pmatrix}hv\\ \dfrac{(hv)^2}{H_{\mathrm s}-b}+\tfrac12gH_{\mathrm s}^2-gH_{\mathrm s}b\end{pmatrix}=\begin{pmatrix}0\\ -gH_{\mathrm s}\,\partial_xb\end{pmatrix},$$

with still water $v=0$, $H_{\mathrm s}=$ const. The scheme is characteristic-wise
finite-difference WENO with global [Lax–Friedrichs splitting](/methods/lax-friedrichs-flux.md)
and Roe-averaged eigenvectors. Well-balancing requires that the discrete derivative of
$\tfrac12gH_{\mathrm s}^2-gH_{\mathrm s}b$ equal the discrete $-gH_{\mathrm s}\partial_xb$ at all
times. With classical WENO weights this needs the "WENO linearization technique" — using the
same nonlinear weights for flux and source (App. B of Li et al., as recalled).

Wang & Don observe that at still water this flux component is an **affine** function of $b$,
with scaling $-gH_{\mathrm s}$ and translation $\tfrac12gH_{\mathrm s}^2$. An
[affine-invariant WENO](/methods/affine-invariant-weno.md) operator commutes with affine maps
(their Thm. 1), so its derivative of the flux equals $-gH_{\mathrm s}$ times its derivative of
$b$, matching the source discretization; and because the characteristic projection is linear,
the property survives [characteristic decomposition](/methods/characteristic-decomposition.md)
(§3.3). Well-balancing is therefore intrinsic, without linearization (contribution).

**Evidence** (§3.3, Figs. 9–10): $x\in[0,10]$, smooth bottom $b_1=5e^{-\frac25(x-5)^2}$ and
discontinuous bottom $b_2=4$ on $[4,8]$, $H_{\mathrm s}=10$, $v=0$, $g=9.812$, $t=50$, up to
1000 points, quadruple precision, no linearization. With $\epsilon=10^{-12}$ the
affine-invariant Z- and D-type schemes keep $\lVert H_{\mathrm s}-10\rVert_\infty$ at round-off
(about $10^{-33}$), while classical and scale-invariant WENO errors fall from about
$10^{-11}$ to $10^{-23}$ with refinement on $b_1$ and stay near $10^{-26}$ on $b_2$. With
$\epsilon=10^{-40}$ all operators are well-balanced except the classical and scale-invariant
D-type ones on $b_1$, whose modifier is not affine invariant. See
[scale and affine invariance](/properties/scale-invariance.md).

## Layered and debris-flow models: WB from stationary contacts

[Balsara et al. (2024)](/sources/balsara-2024.md) link the lake-at-rest property to the
exact preservation of isolated stationary contact discontinuities (§III;
[stationary contact preservation](/properties/stationary-contact-preservation.md)). Their
[fluctuation-form FD-WENO](/methods/fluctuation-form-fd-weno.md), with the HLLI anti-diffusion
and the bottom carried as a variable with non-conservative products, reproduces perturbed
lake-at-rest tests "without any special modifications for the well-balancing":

- Pitman–Le debris flow: bump $b=0.25(\cos(10\pi(x-\tfrac12))+1)$ for $\lvert x-0.5\rvert\le0.1$,
  equilibrium with constant solid fraction and constant surface, perturbation $10^{-3}$ on
  $[-0.6,-0.5]$, 400 zones on $[-1.2,1.2]$, $t=1.25$ (§VIII.a, Fig. 4);
- two-layer shallow water: bump on $[1.4,1.6]$, interface at $0.65$, surface perturbation
  $0.2$ or $10^{-3}$ on $[1.1,1.2]$, 400 zones on $[0,2]$, $t=0.2$ (§VIII.c, Fig. 9).

## Euler with gravity: hydrostatic reconstruction

[Arun et al. (2022)](/sources/arun-2022.md) build a first-order finite-volume
scheme for the barotropic Euler equations with gravity and friction,
$p(\rho)=\rho^\gamma$, $\gamma\ge1$, in a multiscale scaling with page-local
relaxation parameter $\varepsilon$ and exponent $\beta_{\mathrm{ms}}\in[0,1]$
(§2, Eq. (2.6); the scaling and the asymptotic regimes are on
[asymptotic preservation](/properties/asymptotic-preservation.md)). With the
page-local gravitational potential $\phi$, the hydrostatic states are $v=0$,
$\varepsilon^{1-\beta_{\mathrm{ms}}}\partial_xp(\rho)=\rho\,\partial_x\phi$, i.e.
$\rho=C\exp(\varepsilon^{\beta_{\mathrm{ms}}-1}\phi)$ for $\gamma=1$ (§2.1,
Eqs. (2.11)–(2.14)). Following Bouchut, a discrete hydrostatic steady state is
a grid function with zero momentum that satisfies a consistent discrete
equilibrium relation, and a scheme is well-balanced if it maps such states to
themselves (Definition 4.1). The construction (§4):

- **P-reconstruction** of the interface states, in the pressure (4.14):
  $\varepsilon^{1-\beta_{\mathrm{ms}}}p(\rho^-_{i+1/2})=\big[\varepsilon^{1-\beta_{\mathrm{ms}}}p(\rho_i)+\{\!\{\rho\}\!\}_{i+1/2}\big(\min(\phi_i,\phi_{i+1})-\phi_i\big)\big]_+$,
  and $\rho^+_{i+1/2}$ likewise from cell $i+1$, with $[X]_+=\max(0,X)$ keeping
  the density non-negative and $\{\!\{\rho\}\!\}_{i+1/2}=\tfrac12(\rho_i+\rho_{i+1})$;
- a Rusanov-type flux ([Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md))
  on these states, with the gravity source of cell $i$ split into upwinded
  interface contributions proportional to $p(\rho^-_{i+1/2})-p(\rho_i)$ and
  $p(\rho_i)-p(\rho^+_{i-1/2})$ (Eq. (4.6), after Audusse et al. and
  Natalini–Ribot–Twarogowska);
- in the mass update, which in their semi-implicit time discretization carries
  second-derivative terms, a central difference of $p$ and the averaged potential
  flux $\big[\{\!\{\rho\}\!\}_{i+1/2}(\phi_{i+1}-\phi_i)-\{\!\{\rho\}\!\}_{i-1/2}(\phi_i-\phi_{i-1})\big]/\Delta x^2$,
  which cancel exactly on the discrete equilibrium
  $\varepsilon^{1-\beta_{\mathrm{ms}}}p(\rho_{i+1})-\{\!\{\rho\}\!\}_{i+1/2}\phi_{i+1}=\varepsilon^{1-\beta_{\mathrm{ms}}}p(\rho_i)-\{\!\{\rho\}\!\}_{i+1/2}\phi_i$
  (Eq. (4.16)).

Theorem 4.3(ii) states well-balancing for this discrete state: there
$u^-_{i+1/2}=u^+_{i+1/2}$, the flux differences cancel the upwinded sources, and
the central terms of the mass update cancel. *(Compiler check, not in the
sources: inserting (4.16) into (4.14) gives equal arguments of $[\cdot]_+$ for
$\rho^-_{i+1/2}$ and $\rho^+_{i+1/2}$, so the two reconstructed states indeed
coincide.)* The well-balancing must hold in the mass equation too, which a
hydrostatic reconstruction alone does not give. Arun et al. discard the
alternative E-reconstruction, in the enthalpy $\frac{\gamma}{\gamma-1}\rho^{\gamma-1}$,
because, citing Natalini, Ribot and Twarogowska, it gives a wrong diffusion
coefficient in the parabolic limit and so loses asymptotic preservation
(Remark 4.2).

**Evidence** (§5.2, Tables 1–2, Figs. 3–10). Isothermal and isentropic
equilibria with $\phi=x,\ x^2/2,\ \sin(2\pi x)$, $T=2$: for $\phi=x$, $\gamma=1$,
$\varepsilon=1$, the $L^1$ density errors are $2.6815\times10^{-6}$ ($N_x=100$)
and $2.7018\times10^{-8}$ ($N_x=1000$); for $\sin(2\pi x)$ about
$2.2\times10^{-4}$ and $2.1\times10^{-6}$ for all $\varepsilon$. A Gaussian
perturbation of amplitude $10^{-3}$ or $10^{-5}$ is resolved by the WB scheme
and not by the non-well-balanced (NWB) one at $\varepsilon=1$; at
$\varepsilon=10^{-3}$ the NWB scheme gives similar results, which the authors
explain by the limit equation sharing the steady state and by the NWB scheme
being asymptotic preserving; in long runs ($T=100$) the NWB scheme drifts at
$\varepsilon=1$ and oscillates at $\varepsilon=0.1,0.01$.

## Known equilibria: evolving the deviation

[Kanbar et al. (2022)](/sources/kanbar-2022.md) make an
[unstaggered central scheme](/methods/unstaggered-central-scheme.md)
well-balanced for 2D ideal MHD with gravity by a "subtraction technique", after
Berberich, Chandrashekar and Klingenberg and their own Euler version. Given a
stationary solution $u_{\mathrm e}$ (analytic or numerical; page-local), the
scheme evolves the deviation $\delta u=u-u_{\mathrm e}$ by

$$\partial_t\delta u+\partial_x\big[f(\delta u+u_{\mathrm e})-f(u_{\mathrm e})\big]+\partial_y\big[g(\delta u+u_{\mathrm e})-g(u_{\mathrm e})\big]=S(\delta u),$$

which uses that the gravity source $S$ is linear in $u$ (§3, Eqs. (4)–(7)), and
recovers $u=\delta u+u_{\mathrm e}$. If $\delta u^n=0$, the predictor gives
$\delta u^{n+1/2}=0$ (proved, Eq. (17)), and the staggered and back-projected
updates stay zero (called "straight forward"), so the reference state is
preserved "up to machine precision". *(Compiler check, not in the sources: the
cancellation uses that $f(u_{\mathrm e})$ is subtracted with the same discrete
operator, that the limited slopes of $u^n$ and $u_{\mathrm e}$ coincide when
$u^n=u_{\mathrm e}$, and that $S(0)=0$.)*

**Evidence** (§§5.3–5.5, Figs. 6–12): a stationary MHD vortex with
$u_{\mathrm e}$ the vortex itself ($32^2$–$128^2$), an isothermal stratified
atmosphere $\rho=\rho_0e^{-y/H}$, $p=p_0e^{-y/H}$ ($H=0.158$, $p_0=1.13$, $g=2.74$)
unchanged at $t=1.8$, and its magnetized version $B=(0,\mu_B,0)$ (page-local
field strength $\mu_B$); small and large piston perturbations of the atmosphere are compared
visually with Fuchs et al. No error norm is printed. The method is
well-balanced for the supplied $u_{\mathrm e}$; the concluding claim that it
"is capable of preserving any type of known equilibrium states" holds in that
sense only.

## Qualifications

- Wang & Don's "well-balanced for any $\epsilon$" rests on two values of $\epsilon$; it follows
  from their Thm. 1 in exact arithmetic. The claim that characteristic-wise WB WENO is also
  well-balanced for the Euler equations under gravity without linearization is stated but not
  tested in their paper (Abstract, §3.3). The linearization is still required when the WENO
  operator acts on sums or products of functions, e.g. two-$\gamma$ multicomponent
  equilibria (Introduction).
- Balsara et al. write "We don't consider well-balancing in this paper" (§III) and later
  call the method well-balanced (§VIII.c); their evidence is visual agreement with the
  reference results of Dumbser & Balsara (2016), not a round-off equilibrium measurement.
- **Three kinds of evidence.** Wang & Don measure round-off ($\approx10^{-33}$ in
  quadruple precision); Arun et al. state that the challenge is to resolve perturbations
  "up to machine precision" (§1) but report $L^1$ errors of $10^{-6}$ to $10^{-4}$ on 100
  cells; they interpolate the exact equilibrium onto the grid (§5.2.1); Kanbar et al. print
  no magnitude. *(Compiler check, not in the sources: the errors fall by about 100 per
  tenfold refinement, i.e. second order; and for $\gamma=1$, $\varepsilon=1$, $\phi=x$ the
  interpolated state $\rho_i=e^{x_i}$ misses the discrete equilibrium (4.16) by
  $\rho_{i+1}-\rho_i-\{\!\{\rho\}\!\}_{i+1/2}(\phi_{i+1}-\phi_i)=-\tfrac1{12}e^{x_i}\Delta x^3+O(\Delta x^4)$,
  so the tests start from a state that Theorem 4.3(ii) does not cover, consistent with
  truncation-level rather than round-off errors.)*
- Arun et al.'s scheme is first order in space and time; the deviation formulation of
  Kanbar et al. is applied to a second-order scheme whose order is not measured.

# Citations

- [Wang & Don (2022)](/sources/wang-2022-b.md) — Introduction, §2.3 (Thm. 1), §3.3 (Eqs. (26)–(30), Figs. 9–10).
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §III, §VIII.a (Fig. 4), §VIII.c (Fig. 9) (accepted manuscript).
- [Arun et al. (2022)](/sources/arun-2022.md) — §1, §2.1, §4 (Def. 4.1, Eqs. (4.6), (4.14), (4.16), Thm. 4.3, Remark 4.2), §5.2 (Tables 1–2, Figs. 3–10) (arXiv v1).
- [Kanbar et al. (2022)](/sources/kanbar-2022.md) — §3 (Eqs. (4)–(7), (17)), §§5.3–5.5, §6 (arXiv v1).
