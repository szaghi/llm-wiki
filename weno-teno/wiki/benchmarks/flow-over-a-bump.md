---
type: Benchmark
title: "Shallow-water flow over a bump and lake at rest"
description: "One-dimensional shallow-water tests over an isolated bottom bump: the lake at rest (with and without dry zones), its small perturbation, and sub-, super- and transcritical moving-water steady states, measuring exact well-balancing, accuracy on moving equilibria and spurious waves at hydraulic jumps; two-dimensional analogues are a lake at rest over three mounds and subsonic flow over a Gaussian bump."
status: established
aliases: [flow over a bump, lake at rest, perturbed lake at rest, LeVeque perturbation test, transcritical flow over a bump, subcritical flow over a bump, supercritical flow over a bump, Houghton–Kasahara bump, SWASHES bump]
tags: [benchmark, well-balanced, finite-volume, central-scheme, shallow-water]
timestamp: 2026-10-23T11:06:00Z
---

# Shallow-water flow over a bump and lake at rest

A channel with an isolated bump in the bottom $b(x)$ is a one-dimensional test of
[well-balancing](/properties/well-balancing.md) for the
[shallow-water equations](/definitions/shallow-water-equations.md), with depth $h$, discharge
$q=hv$, gravity $g$ and free-surface level $H_{\mathrm s}=h+b$ (page-local, as on the
shallow-water page). Three families of states are run over the same bump: the **lake at rest**
$v=0$, $H_{\mathrm s}\equiv$ const, which a well-balanced scheme must keep to round-off; a
**small perturbation** of it, whose waves a non-well-balanced scheme hides under its own
truncation error; and **moving-water steady states** with $q\equiv q_0$, reached in long time
from inflow and outflow data, which are subcritical, supercritical or transcritical with a
hydraulic jump depending on the Froude number. The sources run the tests to compare a
well-balanced scheme with a standard one of the same order.

## Setups

| Source | Bottom $b(x)$ | Domain | States and data | Grids, time |
|---|---|---|---|---|
| [Ciallella et al. (2023)](/sources/ciallella-2023.md) §5.1 | $0.05\sin(x-12.5)\exp\big(1-(x-12.5)^2\big)$ | $[0,25]$ | lake at rest $h=1-b$, $q=0$, $g=1$ | $N_x=25$–$800$, $T=1$ |
| Ciallella et al. §5.2 | ten times larger bump, $0.5\sin(x-12.5)\exp(\cdots)$ | $[0,25]$ | $h=1-b+10^{-4}\psi$ on $9<x<10$, $\psi=\exp\big(1-1/(1-r)^2\big)$, $r=4(x-9.5)^2$; $g=9.8$ | $N_x=150$ (and 800), $T=1.5$ |
| Ciallella et al. §5.3 | the §5.1 bump | $[0,25]$ | supercritical: $h(0,t)=2$, $q(0,t)=24$; subcritical: $q(0,t)=4.42$, $h(25,t)=2$; from $h=2-b$, $q=0$; $g=9.812$ | $N_x=25$–$800$; $T=50$, $200$ |
| Ciallella et al. §5.3 | $0.2\exp\big(1-1/(1-(\lvert x-10\rvert/5)^2)\big)$ on $\lvert x-10\rvert<5$ | $[0,25]$ | transcritical: $q(0,t)=0.18$, $h(25,t)=0.33$, from $h=0.33-b$ | $N_x=100$, $T=200$ |
| Ciallella et al. §5.5 | step $b=0.2$ on $8<x<12$ | $[0,25]$ | the §5.3 sub- and supercritical data | $N_x=100$; $T=500$, $50$ |
| [Goudon & Minjeaud (2024)](/sources/goudon-2024.md) §3.1 | $0.2-0.05(x-10)^2$ on $8<x<12$, else 0 | $[0,20]$ | lake at rest $\mathcal E(h)+b=0.3$; with a dry zone $\mathcal E(h)+b=\max(0.1,b)$ | $\Delta x\in\{1,0.1,0.01\}$, $T=1500$ and $1000$ |
| Goudon & Minjeaud §3.2 | $-1+0.25\big(1+\cos(10\pi(x-0.5))\big)$ on $1.4<x<1.6$, else $-1$ | $[0,2]$ | LeVeque's perturbed lake at rest: $+0.001$ on $1.1<x<1.2$; $g=9.8$ | $\Delta x=10^{-2}$, reference $4\times10^{-4}$ |
| Goudon & Minjeaud §3.3 | $\tfrac1{10}(1-x^2/16)$, crest $0.1$ | not printed | Houghton–Kasahara: $h_0=0.2$, Froude number $F_0\in\{0.2,0.3,0.7,1.9\}$, $g=9.8$ | $\Delta x=0.05$–$0.2$; $T=30$–$2000$ |
| Goudon & Minjeaud §3.3.4 | $-1+0.3\exp(-(x-5)^2)$; and $0.2-0.05(x-10)^2$ on $8<x<12$ | $[0,10]$; $[0,25]$ | Castro et al. Test 1 ($q=2$, $h+b+v^2/(2g)=2$, $t=100$); Test 2 transcritical, $q(0,t)=0.18$, $h(25,t)=0.33$, $t=200$ | $\Delta x=0.125$ |
| [Kurganov et al. (2023)](/sources/kurganov-2023.md) §7.2 Ex. 7 | two-layer, $b=0.2$ on $[8,12]$, else 0 | $[0,20]$ | from rest $h_1=8$, $h_2=4$; inflow $q_1=119$, $q_2=60$; $g=1$, $r=0.98$ | $N_x=100$, $500$; $t=100$ |

Goudon & Minjeaud solve the barotropic Euler equations with a potential source, of which
shallow water is the case $\gamma=2$; their tests use the pressure $g h^\gamma/\gamma$ with
$\gamma\in\{1.4,2,3,4\}$ for the lakes at rest. Their equilibrium potential
$\mathcal E(h)=p/h+\int_0^hp(s)/s^2\,ds$ (page-local; their $\rho$ and $z$ are written $h$ and
$b$ here) is $\mathcal E(h)=h$ for shallow water, so that the lake at rest is
$\mathcal E(h)+b\equiv$ const away from dry zones (§2, Eq. (2)); for $p=h^\gamma/\gamma$ it is
$\mathcal E(h)=h^{\gamma-1}/(\gamma-1)$, consistent with their printed lake-at-rest depth
$\big((\gamma-1)(0.3-b)\big)^{1/(\gamma-1)}$ *(compiler check, not in the sources)*. Ciallella et
al. replace the SWASHES bump by a $C^\infty$ one "because the SWASHES bump is only $C^0$"
(§5.1), and modify the SWASHES bathymetry of the transcritical case in the same way (§5.3);
Goudon & Minjeaud's Castro et al. Test 2 keeps the parabolic bump $0.2-0.05(x-10)^2$ with
the same discharge and outflow depth, $0.18$ and $0.33$. Goudon & Minjeaud do not print the
domain extent or the support of the Houghton–Kasahara bump (§3.3). Kurganov et al.'s
Example 7 is the two-layer analogue: a rectangular bump of height 0.2 under two layers driven
from rest by inflow discharges.

## Findings across sources

**Lake at rest to round-off.** Ciallella et al.'s well-balanced global-flux WENO3 and WENO5
([flux globalization](/methods/flux-globalization.md)) keep the lake at rest with $L^2$
errors about $10^{-13}$ in $h$ and $10^{-15}$–$10^{-14}$ in $q$ on all grids, while the
non-well-balanced global-flux variant converges with final orders 3.58 and 3.67 (WENO3) and
5.01 and 5.06 (WENO5) in $h$ and $q$ (Table 1). Goudon & Minjeaud's first- and second-order
staggered schemes with hydrostatic reconstruction keep the lake at rest to machine precision
for $\gamma=1.4$, 2, 3 and 4 up to $T=1500$, and also the lake with a dry zone on the bump top
up to $T=1000$; the errors are smaller for $\gamma=1.4$ and on coarser meshes (Figs. 3, 5).
Started from constant density, their solution relaxes to the lake at rest by $T=10000$, faster
on coarser meshes, which the authors attribute to the larger numerical diffusion; with a dry
zone the decay is first exponential and then much slower (Figs. 4, 6).

**Perturbed lake at rest.** On Ciallella et al.'s perturbation of amplitude $10^{-4}$,
standard WENO5 produces a discretization error larger than the perturbation and needs about
$N_x=800$ to match the well-balanced global-flux WENO5 on $N_x=150$ (Figs. 4–6). On LeVeque's
test Goudon & Minjeaud's second-order scheme is clearly better than the first-order one at
$\Delta x=10^{-2}$; when the right-going wave crosses the bump a reflected perturbation forms,
larger for $\gamma$ close to 1 and almost absent for $\gamma=3$ (Figs. 7–9).

**Moving-water steady states.** Over the smooth bump Ciallella et al. find orders 3 and 5 for
all schemes, but errors 2 to 5 orders of magnitude lower with the global flux, most of all in
the well-balanced variant; $q$ and the global flux $K$ are preserved to about $10^{-9}$ (§5.3,
Figs. 7–8). Goudon & Minjeaud's schemes do not preserve moving-water steady states exactly, so
an error proportional to the mesh size remains, visible on the discharge (§3.3); their MUSCL
version still converges at second order in $L^1$ for $F_0=0.2$ (subcritical) and $F_0=1.9$
(supercritical) (Fig. 13), and on Castro et al.'s smooth Test 1 the discharge oscillations are
of order $\Delta x$ (first order) and $\Delta x^2$ (second order) (Figs. 18–19). For
$F_0=0.3$ (stationary shock) and $F_0=0.7$ (moving shock) the constant states and profiles
match the Houghton–Kasahara asymptotic solution, with transient structures that vanish at
later times (Figs. 14–17).

**Hydraulic jumps.** On the transcritical flow with a shock, standard WENO5 produces spurious
oscillations at the jump that propagate through the domain, while global-flux WENO5 has none
and the energy invariant $\Upsilon=\frac{q^2}{2h^2}+gH_{\mathrm s}$ jumps at the shock as it
should (Ciallella et al., Fig. 11). Over the step bottom standard WENO5 oscillates after the
discontinuities, whereas global-flux WENO5 keeps the global flux constant to machine
precision in the supercritical case (§5.5, Figs. 16–17). On Castro et al.'s transcritical
Test 2 Goudon & Minjeaud's second-order scheme does not reach second order, because of the
shock and the limiter, but is more accurate than the first-order one (Figs. 20–21). In the
two-layer Example 7, Kurganov et al.'s well-balanced path-conservative central-upwind scheme
reaches a discrete moving-water steady state with two jumps by $t=100$ and resolves a
$10^{-4}$ perturbation of $h_1$ better than the original path-conservative scheme (Figs.
7.20–7.21; see [path-conservative schemes](/methods/path-conservative-scheme.md)).

## Two-dimensional analogues on unstructured grids

[Del Grosso et al. (2024)](/sources/delgrosso-2024.md) (HAL preprint) run
two-dimensional versions for their multi-dimensional-aware finite-volume
scheme, whose fluxes come from a nodal solver, with $g=9.81$, CFL 0.5
(first order) and 0.25 (second order) and the minmod limiter:

- **Lake at rest over three mounds** (§5.2): $[0,40]^2$ m,
  $b=\max\big(0,\ 1-\tfrac18R_{10,11},\ 1-\tfrac3{10}R_{10,31},\ 1-\tfrac4{10}R_{27,20}\big)$
  with $R_{a,c}=\sqrt{(x-a)^2+(y-c)^2}$ (page-local), $H_{\mathrm s}=4$ m,
  $v=0$, outflow boundaries, $100\times100$ squares, $t=200$ s. The
  first-order multi-point, the second-order and the two-point schemes
  keep it "up to a machine error of order $10^{-15}$" (Fig. 5). The
  multi-point scheme needs no modification for this, because of the
  geometric identity $\sum_p\sum_fl_{pcf}\mathbf n_{pcf}=0$ over the
  subfaces of a cell (their Eq. (48); $l$ and $\mathbf n$ subface lengths
  and normals); the second-order extension needs an extra in-cell term
  (Eq. (60)) (§4.5–4.6).
- **Perturbation** (§5.2.1): $10^{-3}$ added to $h$ on
  $19\le x,y\le21$; snapshots at 0, 0.5 and 1 s, the perturbation leaves
  the domain and the run stops at $t\approx55.45$ s, when the residuals
  fall below $10^{-10}$ (Fig. 6).
- **Subsonic flow over a Gaussian bump** (§5.1, a 1D test of Chalons &
  Del Grosso extended to 2D): $[0,20]\times[0,5]$ m on triangles,
  $h(x,y,0)=2-0.1e^{-(x-10)^2}$, $v=0$,
  $b=0.1-0.01e^{-(x-10)^2}$, outflow left and right and walls top and
  bottom ("no-slip wall" as printed); reference the second-order scheme on 1,007,616 cells; meshes of
  984 to 62,976 cells; the final time is not printed. The $L^1$ orders
  for $h$ are 0.80, 0.87, 0.92 at first order and, without limiter,
  1.80, 1.88, 1.97 at second order (Tables 1–2).

The scheme treats only wet states, $h>0$ (§2, §6); the dry-zone lakes of
Goudon & Minjeaud have no two-dimensional counterpart here.

## Qualifications

- "Well-balanced" covers different classes of states here: Goudon & Minjeaud's scheme is exact
  for the lake at rest only; Ciallella et al.'s is exact for states of constant discrete global
  flux, which are not the analytical moving equilibria (their Remark 3.2); Kurganov et al.'s is
  exact for discrete equilibria defined by equilibrium variables, discontinuous ones included.
  The tests are therefore not all measuring the same property.
- Ciallella et al.'s printed orders in Table 1 are reproduced only with $N_x-1$ in place of
  $N_x$ (a compiler check recorded on their Source page), and their text says the
  non-well-balanced errors "match the order of the reconstruction" while the WENO3 orders
  settle at 3.5–3.7.
- Kurganov et al. print the domain of Example 7 as $[0,20]$ with a free boundary at $x=20$, but
  describe a secondary wave "around $x\in[18,22]$"; one of the two is misprinted.
- Goudon & Minjeaud print $\Delta x=0.05$ in the text and $0.04$ in the Fig. 12 caption for the
  same $F_0=0.2$, $1.9$ runs, and the output times of Figs. 15–16 differ between text and
  captions.

# Citations

- [Ciallella et al. (2023)](/sources/ciallella-2023.md) — §5.1–§5.5, Eqs. (45)–(54), Table 1, Figs. 3–17 (author manuscript).
- [Goudon & Minjeaud (2024)](/sources/goudon-2024.md) — §2 (Eq. (2)), §3.1–§3.3, Figs. 3–21 (HAL deposit of the version of record).
- [Kurganov et al. (2023)](/sources/kurganov-2023.md) — §7.2, Ex. 7, Figs. 7.20–7.21.
- [Del Grosso et al. (2024)](/sources/delgrosso-2024.md) — §4.5–4.6, Eqs. (48), (60), §5.1–§5.2.1, Tables 1–2, Figs. 5–6 (HAL preprint).
