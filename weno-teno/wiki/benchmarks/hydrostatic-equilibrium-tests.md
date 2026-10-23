---
type: Benchmark
title: "Hydrostatic equilibrium tests under gravity"
description: "Suite of Euler-with-gravity tests for well-balanced schemes: isothermal, isentropic and polytropic hydrostatic steady states in one and two dimensions, small perturbations of them, shock tubes and contacts in a gravitational field, and discontinuous thermal shallow-water equilibria, judged by whether the steady state is kept to round-off and the perturbation resolved."
status: established
aliases: [hydrostatic steady state, isothermal equilibrium, polytropic equilibrium, Lane–Emden polytrope, Sod under gravity, stratified atmosphere]
tags: [benchmark, well-balanced, asymptotic-preserving]
timestamp: 2026-10-23T15:17:00Z
---

# Hydrostatic equilibrium tests under gravity

For the Euler equations with a gravitational potential $\phi$, a gas at
rest is in hydrostatic equilibrium when $\partial_xp=-\rho\,\partial_x\phi$.
A scheme that does not balance the discrete flux gradient against the
discrete source exactly drifts away from such a state at the level of
its truncation error, and a small perturbation of the equilibrium below
that level is lost. The suite below, shared across the
[well-balancing](/properties/well-balancing.md) literature, therefore
checks two things: whether a steady state is kept to machine precision,
and whether a perturbation of small amplitude $\eta_{\mathrm p}$
(page-local) is resolved. Equilibrium states are written
$u_{\mathrm e}=(\rho_{\mathrm e},0,p_{\mathrm e})$.

**Sign convention.** [Li et al. (2023a)](/sources/li-2023.md) use the
source $-\rho\,\partial_x\phi$, under which density falls as $\phi$
grows. [Arun, Krishnan & Samantaray (2022)](/sources/arun-2022.md)
print the source as $-\rho\,\partial_x\phi$ in their Eq. (2.2) but use
$+\rho\,\partial_x\phi$ from Eq. (2.6) on, so that all their equilibria
grow with $\phi$. The formulas below are as each source prints them.

## Steady states

| Equilibrium | Arun et al. (2022) §5.2 | Li et al. (2023a) §5 |
|---|---|---|
| isothermal | $\rho_{\mathrm e}=e^{\phi}$, $\gamma=1$, $\phi=x,\ x^2/2,\ \sin2\pi x$ on $[0,1]$ | $\rho_{\mathrm e}=p_{\mathrm e}=e^{-\phi}$, $\phi=x$ on $[0,1]$; 2D $\rho_0=1.21$, $\phi=x+y$ |
| isentropic / polytropic | $\rho_{\mathrm e}=\big(1+\tfrac{\gamma-1}{\gamma}\phi\big)^{1/(\gamma-1)}$, $\gamma=1.4$ | $\rho_{\mathrm e}=\big(1-\tfrac{\gamma-1}{\gamma}\phi\big)^{1/(\gamma-1)}$, $p_{\mathrm e}=\rho_{\mathrm e}^\gamma$; 1D $\phi=3.15x$ |
| 2D polytrope | — | Lane–Emden, $\gamma=2$: $\rho_{\mathrm e}=\sin(\alpha r)/(\alpha r)$, $p_{\mathrm e}=\rho_{\mathrm e}^2$, $\phi=-2\rho_{\mathrm e}$, $\alpha=\sqrt{2\pi}$, $[-0.5,0.5]^2$ |

Every printed pair satisfies its source's balance: $p_{\mathrm e}'=\mp\rho_{\mathrm e}\phi'$
for the exponential and polytropic states with $p_{\mathrm e}=\rho_{\mathrm e}$
or $\rho_{\mathrm e}^\gamma$, and $\nabla p_{\mathrm e}=2\rho_{\mathrm e}\nabla\rho_{\mathrm e}=-\rho_{\mathrm e}\nabla\phi$
for the Lane–Emden state, whatever $\alpha$ *(compiler check, not in the
sources)*.

**Round-off or truncation.** The two sources measure different things.
Li et al. initialize the discrete equilibrium and report it kept: their
well-balanced (WB) scheme stays at $O(10^{-16})$ in double and
$O(10^{-34})$ in quadruple precision on every grid, for the isothermal
states in 1D ($t=2$) and 2D ($t=1$) and the polytropic states in 1D
($t=10$) and 2D ($t=14.8$), while the non-well-balanced (NWB) scheme
starts at $O(10^{-10})$ on 10 cells and reaches machine epsilon in double
only on fine grids (Tables 4, 5, 7, 8). Arun et al. interpolate the exact
continuous equilibrium onto the grid and report $L^1$ density errors at
$t=2$ that fall by a factor of about 100 per tenfold refinement: for the
isothermal state with $\phi=x$, $2.6815\times10^{-6}$ on 100 cells and
$2.7018\times10^{-8}$ on 1000 at $\varepsilon=1$, about
$2.2\times10^{-4}$ and $2.1\times10^{-6}$ for $\phi=\sin2\pi x$ (Table 1);
for the isentropic state, $3.0399\times10^{-7}$ and $3.0717\times10^{-9}$
with $\phi=x$ (Table 2). The ratios 99.2 and 99.0 are second-order
decay, not round-off: the interpolated continuous state is not the
discrete equilibrium that their scheme preserves *(compiler check, not
in the sources)*. Arun et al. also scale the relaxation by a
parameter $\varepsilon$ (page-local; $\varepsilon=1$ to $10^{-3}$), since
their scheme is [asymptotic preserving](/properties/asymptotic-preservation.md)
for the Euler system with gravity and friction.

[Kanbar et al. (2022)](/sources/kanbar-2022.md) §5.4–5.5 (arXiv v1) run
the MHD counterpart, an isothermal stratified atmosphere
$\rho=\rho_0e^{-y/H}$, $p=p_0e^{-y/H}$ at rest, with $p_0=1.13$, $g=2.74$,
$H=p_0/(g\rho_0)=0.158$ (so $\rho_0\approx2.61$ *(compiler check, not in
the sources)*), unmagnetized or with $B=(0,\mu_B,0)$ (page-local field
strength), and show the unperturbed state kept to $t=1.8$ (Fig. 7).

## Perturbations

- Li et al.: $p=p_{\mathrm e}+\eta_{\mathrm p}\exp(-100(x-0.5)^2)$ on the
  isothermal state, $\eta_{\mathrm p}=10^{-4}$ and $10^{-11}$, $N_x=90$,
  $t=0.8$ (domain printed $[-1,2]$, unlike the $[0,1]$ of the steady
  state it perturbs); in 2D $\eta_{\mathrm p}=10^{-12}$ with a Gaussian
  of exponent 121 at $(0.3,0.3)$, $30^2$, $t=0.15$; on the polytropic
  states $\eta_{\mathrm p}=10^{-3}$ and $10^{-12}$ (1D, $N_x=50$) and
  $10^{-10}$ on the 2D polytrope ($50^2$). NWB resolves the large
  amplitudes and fails on the small ones, with oscillations starting at
  the left boundary before the perturbation reaches it; WB resolves all
  (Figs. 10–11, 13–14).
- Arun et al.: $\rho=e^{\phi}+\zeta\exp(-100(x-0.5)^2)$ with
  $\zeta=10^{-3},10^{-5}$ (page-local amplitude, as printed), $N_x=100$,
  plotted at $t=0.25$. At $\varepsilon=1$ WB resolves the perturbation
  and NWB does not; at $\varepsilon=10^{-3}$ NWB gives similar results,
  which they explain by the stiff-limit equation sharing the steady
  state (Figs. 3–4, 9–10). To $t=100$ the NWB momentum drifts at
  $\varepsilon=1$ and oscillates at $\varepsilon=0.1$ and $0.01$
  (Figs. 5–8).
- Kanbar et al.: a piston on the bottom boundary,
  $v_2=\exp(-100(x-1.9)^2)\,c\sin(6\pi t)$ with $c=0.003$ and $0.3$
  (page-local amplitude), on $800\times200$, and a field-aligned driver
  of amplitude 0.3 in the magnetized case, compared visually with
  third-order schemes of earlier work (Figs. 8–12).

## Discontinuities in a gravitational field

- **Sod under gravity.** Li et al. take $\phi_x=1$, the Sod states on
  $[0,1]$ with the jump at 0.5, $N_x=100$, $t=0.2$, against a 3000-cell
  reference: NWB oscillates near the shock ($x\approx0.8$) and the
  contact ($x\approx0.65$), WB does not (Fig. 9). Arun et al. run the
  barotropic version $(\rho,v)=(1,0)$, $(0.125,0)$ with $\phi=x$ (recorded
  on [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)).
- **Contact under gravity.** Li et al.: $(\rho,v,p)=(1,0,1)$ for
  $x\le0.5$ and $(10,0,1)$ beyond, $\phi_x=1$, reflective boundaries,
  $N_x=100$, $t=0.6$; both schemes are essentially non-oscillatory
  (Fig. 12).

## Discontinuous equilibria of thermal shallow water

The thermal rotating shallow-water (Ripa) equations carry a buoyancy
$\mathsf b$ (page-local; the sources' $b$) in the pressure
$\tfrac{\mathsf b}2h^2$ of a layer of thickness $h$ over a bottom $b$
(page-local; the sources' $Z$), and admit steady states at rest whose
thickness and buoyancy jump while that pressure stays continuous, the
shallow-water analogue of a hydrostatic state with a contact.
[Chu et al. (2025b)](/sources/chu-2025-b.md) §5.2 test their
flux-globalization [LCD central-upwind](/methods/lcd-central-upwind-scheme.md)
scheme (LCD-PCCU) against the scalar-diffusion PCCU scheme on two of
them (SSP-RK3, CFL 0.45):

- *Constant-pressure equilibrium* (Ex. 6, 1D in $y$, flat bottom):
  $(h,v,\mathsf b)=(2,0,1)$ for $y<0$ and $(1,0,4)$ otherwise on
  $[-5,5]$, free boundaries, $\Delta y=1/20$, $t=10$; both schemes keep
  it exactly: the errors in $h$ and $\mathsf b$ "are zeros". The
  pressure is $\tfrac{\mathsf b}2h^2=2$ on both sides *(compiler check, not
  in the sources)*. Perturbed by $0.1$ in $h$ on $y\in[-1.8,-1.7]$, with
  a reference of LCD-PCCU on $\Delta y=1/400$, the $L^1$ errors of $h$
  at $t=1.2$ on $\Delta y=1/20,1/40,1/80$ are $8.16\times10^{-2}$,
  $4.72\times10^{-2}$, $2.49\times10^{-2}$ for PCCU (rates 0.790,
  0.923) and $1.25\times10^{-2}$, $8.55\times10^{-3}$,
  $5.05\times10^{-3}$ for LCD-PCCU (rates 0.548, 0.760) (Table 5.3):
  LCD-PCCU is "much more accurate" and "substantially less
  oscillatory", with lower experimental rates.
- *Small perturbation of a 2D steady state* (Ex. 8, no Coriolis force):
  $(h,v_1,v_2,\mathsf b)=(3-b,0,0,\tfrac43)$ for $x^2+y^2<0.25$ and
  $(2-b,0,0,3)$ outside, with $h$ raised by $0.1$ in the ring
  $0.01<x^2+y^2<0.09$; the bottom $b=0.5e^{-100[(x+0.5)^2+(y+0.5)^2]}$ for
  $x<0$ and $0.6e^{-100[(x-0.5)^2+(y-0.5)^2]}$ otherwise; $[-1,1]^2$,
  free boundaries, $\Delta x=\Delta y=1/50$, $t=0.12$, diagonal slices
  against PCCU on $1/400$. LCD-PCCU resolves $h$ and $\mathsf b$ more
  sharply than PCCU (Figs. 5.12–5.13). Away from the two bottom bumps the
  unperturbed pressure is $\tfrac12\cdot\tfrac43\cdot3^2=6=\tfrac12\cdot3\cdot2^2$
  on both sides of the circle *(compiler check, not in the sources)*.

The authors' 2D scheme preserves exactly only steady states whose
global flux in $x$ does not depend on $x$ and in $y$ not on $y$; it does
not preserve genuinely two-dimensional steady states, and they state
that "to the best of our knowledge, no existing numerical method is
capable of exactly preserving general 2-D steady states, even the
smooth ones" (Remark 4.1); see
[flux globalization](/methods/flux-globalization.md) and
[well-balancing](/properties/well-balancing.md).

The [Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md)
starts from a hydrostatic state too, but is used as a resolution test,
not as a well-balancing one.

## Qualifications

- Li et al.'s well-balancing rests on a scale-invariant multi-resolution
  [A-WENO](/methods/alternative-weno.md) interpolation in
  characteristic variables (their Theorem 5, 1D); Arun et al.'s scheme is
  first order in space and time; Kanbar et al.'s is a second-order
  [unstaggered central scheme](/methods/unstaggered-central-scheme.md)
  written for the deviation $u-u_{\mathrm e}$ from a supplied equilibrium.
- Li et al. call the drop of the polytropic accuracy-test error from
  $7.49\times10^{-4}$ ($N_x=32$) to $1.25\times10^{-7}$ (printed order
  12.55) "super-convergence"; from $N_x=64$ on, WB and NWB errors coincide
  (Table 6), so the large order is the drop from one anomalously large
  coarse-grid error *(compiler check, not in the sources)*.
- Arun et al.'s preprint (arXiv v1) prints the perturbation final time
  only in the figure titles.
- Chu et al. (2025b)'s rates in Table 5.3 are lower for LCD-PCCU than
  for PCCU although its errors are 4.9 to 6.5 times smaller *(compiler
  check, not in the sources)*; both stay below one. They write the 1D
  Ripa mesh as $\Delta x$ and its zoom window in $x$ although the
  problem is posed in $y$.

# Citations

- [Li et al. (2023a)](/sources/li-2023.md) — §5.1–5.2, Theorem 5, Tables 3–8, Figs. 9–14.
- [Arun, Krishnan & Samantaray (2022)](/sources/arun-2022.md) — §2, §5.1–5.2, Tables 1–2, Figs. 1–10 (arXiv v1).
- [Kanbar et al. (2022)](/sources/kanbar-2022.md) — §5.4–5.5, Figs. 7–12 (arXiv v1).
- [Chu et al. (2025b)](/sources/chu-2025-b.md) — §4, Remark 4.1, §5.2, Examples 6 and 8, Table 5.3, Figs. 5.8–5.13.
