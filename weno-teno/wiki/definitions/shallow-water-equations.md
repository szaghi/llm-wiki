---
type: Definition
title: "Shallow-water equations"
description: "The one- and two-layer, one- and two-dimensional shallow-water (Saint-Venant) equations with bottom topography and friction, their energy entropy and Lagrangian form, and their steady states — lake at rest, constant energy, and the invariants $q$ and global flux $K$ that survive hydraulic jumps — which decide what well-balancing must preserve."
status: established
aliases: [Saint-Venant equations, SWE, shallow water equations, two-layer shallow-water equations, lake at rest, moving-water equilibrium]
tags: [well-balanced, finite-volume, central-scheme, benchmark, shallow-water]
timestamp: 2026-10-23T23:55:00Z
---

# Shallow-water equations

The one-dimensional **shallow-water** (Saint-Venant) equations with bottom topography $b(x)$
and Manning friction are the balance law

$$\partial_t\begin{pmatrix}h\\ q\end{pmatrix}+\partial_x\begin{pmatrix}q\\ \dfrac{q^2}{h}+\dfrac g2h^2\end{pmatrix}=\begin{pmatrix}0\\ -gh\,\partial_xb-g\,n_{\mathrm M}^2\,\dfrac{q\lvert q\rvert}{h^{7/3}}\end{pmatrix},$$

with water depth $h$, discharge $q=hv$, gravity $g$, Manning coefficient $n_{\mathrm M}$ and
free-surface level $H_{\mathrm s}=h+b$ (all page-local; $h$ is not a numerical flux here and $q$
not a weight exponent; [Ciallella et al. (2023)](/sources/ciallella-2023.md), §2.1, Eqs.
(1)–(2), citing Saint-Venant). The bottom enters only through the source, so the equations
test [well-balancing](/properties/well-balancing.md) in several sources of the bundle: a scheme
must make the discrete flux divergence and the discrete source cancel at a chosen class of
steady states.

## Two dimensions, energy and Lagrangian form

[Del Grosso et al. (2024)](/sources/delgrosso-2024.md) (HAL preprint; §2, Eqs. (2)–(6)) write the 2D
system for $(h,hv_1,hv_2)$ with fluxes $(hv_d,\ hv\,v_d+p\,e_d)$ and source
$(0,-gh\,\partial_{x_1}b,-gh\,\partial_{x_2}b)$, where $p=\tfrac12gh^2$ (page-local "pressure") and $e_d$ the unit
vector; the eigenvalues along a unit normal $n$ are $v\cdot n-\sqrt{gh}$, $v\cdot n$,
$v\cdot n+\sqrt{gh}$. They use the analogy with isentropic gas dynamics ($h$ as density,
$p=\tfrac g2h^\gamma$ with $\gamma=2$) and take the total energy as the entropy:
$$\partial_t(h\mathsf e_{\mathrm s})+\nabla\cdot\big((h\mathsf e_{\mathrm s}+p)v\big)\le-gh\,v\cdot\nabla b,\qquad \mathsf e_{\mathrm s}=\tfrac12gh+\tfrac12\lvert v\rvert^2$$
(page-local $\mathsf e_{\mathrm s}$, the specific energy with internal part $\int p/h^2\,dh=\tfrac12gh$),
equivalent for regular topography to a conservative inequality for $\mathsf e_{\mathrm s}+gb$. Along a
face normal they pass to Lagrangian mass coordinates, $dx_n=h^{-1}dm+v_n\,dt$, in which the system
for $(1/h,v_n,v_t)$ has the ordered eigenvalues $-\sqrt{gh}\,h$, $0$, $\sqrt{gh}\,h$; their approximate
Riemann solver is built there and mapped back ([carbuncle phenomenon](/definitions/carbuncle-phenomenon.md)).
Only wet states $h>0$ are treated.

[Naudet & Zahr (2024)](/sources/naudet-2024.md) (§5.2, App. A, Eqs. (52)–(53)) use the
geopotential $\Phi_{\mathrm g}=gh$ (page-local) as unknown, with flux
$(\Phi_{\mathrm g}v,\ \Phi_{\mathrm g}v\otimes v+\tfrac12\Phi_{\mathrm g}^2I)$ and bathymetry source
$(0,\ g\Phi_{\mathrm g}\nabla b')$ in their sign convention for the bottom $b'$ (page-local), and 1D
eigenvalues $v_n\mp\sqrt{\Phi_{\mathrm g}}$. [Kolluru et al. (2024)](/sources/kolluru-2024.md)
(arXiv v2; §3.3, Eq. (8a)) use the 1D system without topography, $\partial_t(h,hv)+\partial_x(hv,hv^2+\tfrac12gh^2)=0$.

## Steady states

Ciallella et al. (§2.2, Eqs. (5)–(9)) distinguish three levels.

- **Lake at rest**: $v=0$, $H_{\mathrm s}\equiv$ const (Eq. (5)). It is the steady state for
  which "WB-property" or "C-property" is used by
  [Wang & Don (2022)](/sources/wang-2022-b.md) (§2–§3.3).
- **Constant energy** (smooth, frictionless): $q\equiv q_0$ and
  $\Upsilon=\frac{q^2}{2h^2}+gH_{\mathrm s}\equiv\Upsilon_0$ (page-local $\Upsilon$; Eqs. (6), (8)–(9)),
  obtained from $0=\partial_x\big(\tfrac{q^2}{h}+\tfrac g2h^2\big)+gh\,\partial_xb=h\,\partial_x\Upsilon$.
  It fails where the bottom or the depth is discontinuous, e.g. a transcritical flow with a
  hydraulic jump, across which $\Upsilon$ jumps.
- **General invariants**: $q\equiv q_0$ and the global flux
  $K=\frac{q^2}{h}+\frac g2h^2+g\int_{x_{\mathrm b}}^x\big(h\,\partial_\xi b+n_{\mathrm M}^2h^{-7/3}\lvert q\rvert q\big)d\xi\equiv K_0$
  (Eq. (7)), which "is always true", friction and jumps included. This is the
  [flux-globalization](/methods/flux-globalization.md) view: steady states are the states of
  constant global flux.

Wang & Don (§3.3, Eqs. (26)–(28), after Li, Caleffi and Qi) rewrite the frictionless
equations in $(H_{\mathrm s},hv)$, so that at the lake at rest the momentum flux
$\tfrac12gH_{\mathrm s}^2-gH_{\mathrm s}b$ is an affine function of $b$; this is the route to
well-balancing by [affine-invariant WENO](/methods/affine-invariant-weno.md) recorded on the
well-balancing page.

## Two-layer shallow water

For two immiscible layers, upper depth $h_1$ and lower depth $h_2$, discharges $q_k=h_kv_k$
and density ratio $r=\rho_1/\rho_2<1$ (page-local),
[Kurganov et al. (2023)](/sources/kurganov-2023.md) (§1, Eq. (1.11)) write

$$\begin{aligned}
&\partial_th_1+\partial_xq_1=0,\qquad
\partial_tq_1+\partial_x\Big(\frac{q_1^2}{h_1}+\frac g2h_1^2\Big)=-gh_1\,\partial_x(h_2+b),\\
&\partial_th_2+\partial_xq_2=0,\qquad
\partial_tq_2+\partial_x\Big(\frac{q_2^2}{h_2}+\frac g2h_2^2\Big)=-gh_2\,\partial_x(rh_1+b),
\end{aligned}$$

with a possibly discontinuous bottom. The coupling terms are non-conservative products, so the
system is treated by [path-conservative schemes](/methods/path-conservative-scheme.md);
[Chu et al. (2022)](/sources/chu-2022.md) (Eq. (6.3)) use instead the interface elevation
$w=h_2+b$ as unknown, an equivalent form for smooth solutions.

- **Lake at rest**: $v_1=v_2=0$, $h_1\equiv$ const, $h_2+b\equiv$ const
  (Chu et al., Eq. (6.2); Kurganov et al., §1).
- **Moving-water equilibria**: $q_1$, $q_2$ and the layer energies
  $\frac{q_1^2}{2h_1^2}+g(h_1+h_2+b)$ and $\frac{q_2^2}{2h_2^2}+g(rh_1+h_2+b)$ constant
  (Kurganov et al., §6); these are algebraic equilibrium variables in the sense of the
  flux-globalization page.

Kurganov et al. state that the original path-conservative central-upwind scheme of Castro
Díaz, Kurganov and Morales de Luna preserves only the lake at rest of this system (§1, §4), and
show it failing on a discontinuous steady state over a step (§7.2, Ex. 5). The one-sided
speeds of central-upwind fluxes for the two-layer system come from Lagrange-theorem bounds,
not eigenvalues (Kurganov et al., §6; Chu et al., §2).

## Test problems in the sources

- **Ciallella et al. (2023)** (§5, domain $[0,25]$): lake at rest over the $C^\infty$ bump
  $b=0.05\sin(x-12.5)\exp\big(1-(x-12.5)^2\big)$, chosen because the SWASHES bump is only $C^0$
  ($h=1-b$, $g=1$, $T=1$); its perturbation by $10^{-4}$ on $9<x<10$ with a ten times larger
  bump, $g=9.8$, $T=1.5$; supercritical ($h(0,t)=2$, $q(0,t)=24$, $T=50$) and subcritical
  ($q(0,t)=4.42$, $h(25,t)=2$, $T=200$) flows over the bump, $g=9.812$; a transcritical flow
  with a hydraulic jump over $b=0.2\exp\big(1-1/(1-(\lvert x-10\rvert/5)^2)\big)$ ($q(0,t)=0.18$,
  $h(25,t)=0.33$, $T=200$); a step bottom $b=0.2$ on $8<x<12$; and the same flows with
  $n_{\mathrm M}=0.05$ (§§5.1–5.7).
- **Kurganov et al. (2023)** (§7.2; $g=10$, $r=0.98$ unless stated): a two-layer steady
  state over the step $b=-2$ ($x<0$), $-1$ ($x>0$) with $q_1\equiv12$, $q_2\equiv10$ and layer
  energies $50$ and $55$; two-layer Riemann problems over a step; and a moving-water steady
  state over a bump on $[8,12]$ reached from rest by inflow data $q_1=119$, $q_2=60$
  ($g=1$, $t=100$).
- **Chu et al. (2022)** (§7.1, Ex. 2): a $10^{-5}$ perturbation of $h_1$ over the two-layer lake
  at rest, over a smooth bump and over a step (details on
  [well-balancing](/properties/well-balancing.md)).

- **Del Grosso et al. (2024)** (§5, $g=9.81$ unless stated): lake at rest over three mounds,
  $b=\max\big(0,1-\tfrac18R_{10,11},1-\tfrac3{10}R_{10,31},1-\tfrac4{10}R_{27,20}\big)$ with
  $R_{a,b}$ the distance from $(a,b)$ (page-local), $h+b=4$, $\Omega=[0,40]^2$, $100\times100$ squares,
  $t=200$ s, kept to about $10^{-15}$, and its $10^{-3}$ perturbation; a smooth subsonic accuracy
  test on triangles; radial [dam breaks](/benchmarks/dam-break-problem.md) over flat and
  cosine-bump bottoms ($h=10$ inside $r_0=11$ m, $1$ outside, $t=0.69$ s); an oblique hydraulic
  jump (wall deflection $8.95^\circ$, inflow $h=1$, $v_1=8.57$, exact downstream $h=1.5$,
  $v=7.9556$, jump angle $30^\circ$); a four-quadrant Riemann problem over discontinuous topography;
  and three carbuncle tests (colliding flow, a Quirk-type canal, Froude-5
  [flow past a cylinder](/benchmarks/flow-past-circular-cylinder.md)).
- **Naudet & Zahr (2024)** (§5.2, Eq. (54)): a 1D dam break with $g=1$, flat bottom,
  $\Omega=(-5,5)$, depth $3$ on the left and $1$ on the right at rest, reflecting walls at both
  ends, to $t=6$, tracked through the wall reflections by space-time shock tracking.
- **Kolluru et al. (2024)** (§3.3, Eqs. (8b)–(8c)): a hump of water $h=1+0.4e^{-\beta_{\mathrm h}x^2}$
  (page-local width $\beta_{\mathrm h}$, value not printed) on periodic $[-5,5]$, which steepens into a
  shock at $t\simeq3$, and a dam break with $h_{\mathrm l}>h_{\mathrm r}$ (values and $g$ not printed),
  both on 2665 points with spectral relaxation against a CLAWPACK reference.

## Qualifications

- Ciallella et al. print $\partial_xR\equiv S$ on p. 5, while their Eq. (4) defines $R=-\int^xS$,
  so that $\partial_xR=-S$; their Eq. (18) uses the sign of Eq. (4).
- Kurganov et al. print the switching condition for the modified depths after Eq. (6.11) with
  indices $j-\tfrac12$ where their general rule and the nozzle analogue use $j+\tfrac12$.

- Del Grosso et al. label all three eigenvalues $\lambda^-$ (§2), and print the oblique-jump
  profile along $y=40$ m in a domain $[0,40]\times[0,30]$ m (§5.4).

# Citations

- [Ciallella et al. (2023)](/sources/ciallella-2023.md) — §2.1 (Eqs. (1)–(4)), §2.2 (Eqs. (5)–(9)), §5 (Eqs. (45)–(54)) (author manuscript).
- [Kurganov et al. (2023)](/sources/kurganov-2023.md) — §1 (Eq. (1.11)), §4, §6 (Eqs. (6.1)–(6.13)), §7.2 (Exs. 5–7).
- [Wang & Don (2022)](/sources/wang-2022-b.md) — §2–§3.3 (Eqs. (26)–(28)).
- [Chu et al. (2022)](/sources/chu-2022.md) — §2, §6.1 (Eqs. (6.2)–(6.3)), §7.1 (Ex. 2).
- [Del Grosso et al. (2024)](/sources/delgrosso-2024.md) — §2 (Eqs. (2)–(6)), §2.1, §5.1–5.8 (HAL preprint).
- [Naudet & Zahr (2024)](/sources/naudet-2024.md) — §5.2 (Eqs. (52)–(54)), App. A.
- [Kolluru et al. (2024)](/sources/kolluru-2024.md) — §3.3 (Eqs. (8a)–(8c), Figs. 12–13) (arXiv v2).
