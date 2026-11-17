---
type: Benchmark
title: "Supersonic turbulent boundary layer"
description: "Spatially developing flat-plate turbulent boundary layer at free-stream Mach 2 to 5.86, run as DNS with recycling or digital-filter inflow and as wall-resolved and wall-modeled LES; skin friction, van Driest profiles, fluctuations and spectra against DNS show how much numerical dissipation a convective scheme can inject before wall turbulence is damped, and how split central forms, order and resolution trade against cost."
status: established
aliases: [spatially developing supersonic boundary layer, compressible flat-plate boundary layer, hypersonic turbulent boundary layer, Mach 2 boundary layer]
tags: [benchmark, turbulence, low-dissipation, teno, weno]
timestamp: 2026-11-17T08:43:44Z
---

# Supersonic turbulent boundary layer

A turbulent boundary layer develops along a flat plate in a supersonic
free stream. Turbulence is injected at the inflow, by a digital filter
on a mean profile or by recycling a downstream plane, the layer grows downstream, and its statistics are
taken at a station of given friction Reynolds number
$\mathrm{Re}_\tau$. The flow is nominally shock-free, but a
compressible solver for it must still survive shocklets at high Mach
number, so the sources use it to test how a shock-capturing or hybrid
convective scheme interacts with wall turbulence, and whether a
non-dissipative split central scheme survives it without added
dissipation. The measures are the
skin-friction coefficient $c_f$ against $\mathrm{Re}_\tau$ and the
inner-scaled profiles of mean velocity, turbulent kinetic energy and
temperature, compared with DNS. Here $\delta_0$ is the inflow boundary-layer
thickness, $\mathrm{Re}_{\tau,0}$ the inflow friction Reynolds number
and $T_{\mathrm{rat}}$ the wall-to-recovery temperature ratio
(page-local).

## Data

Common to the three URANOS sources (all with the same finite-difference code,
[URANOS](/software/uranos.md)): domain $L_x\times L_y\times L_z=90\delta_0\times10\delta_0\times6\delta_0$,
periodic in the span, characteristic (NSCBC) top and outflow boundaries,
digital-filter inflow, three-stage SSP Runge–Kutta, Sutherland viscosity.
De Vanna et al. (2023a, 2023c) run at CFL 0.5 and Fourier number 0.1;
De Vanna et al. (2023b) recommend CFL 0.5–0.8 and Fourier number 0.1–0.3.

| Case | Source | Model | $\mathrm{Re}_{\tau,0}\to\mathrm{Re}_\tau$ | Grid | $\Delta x^+\times\Delta y_w^+\times\Delta z^+$ |
|---|---|---|---|---|---|
| Mach 2, DNS | De Vanna et al. (2023b) BL01 | — | $180\to250$ | $2800\times128\times600$ | $8.0\times0.5\times2.5$ |
| Mach 2, WRLES | De Vanna et al. (2023a) cases 1–8; (2023b) BL02 | ILES or WALE | $180\to250$ | $768\times128\times128$, stretched | $29.3\times0.54\times11.7$ (2023a); $\Delta x^+=29.0$ in (2023b) |
| Mach 2, WMLES | De Vanna et al. (2023a) cases 9–51 | WALE | $700\to900$ | $675\times64\times108$, $960\times128\times160$, $1350\times225\times270$ | $120\times70\times50$, $84\times35\times34$, $60\times20\times20$ |
| Mach 5.86, WMLES | De Vanna et al. (2023a) cases 52–66; (2023b) BL03 | WALE | $1000\to1200$ | $1400\times200\times200$ | printed $90\times30\times36$ |
| Mach 2, WMLES over an immersed block | De Vanna et al. (2023c) tbl1–tbl4 | wall model at immersed wall | $250\to252$ up to $2000\to2013$ | $256\times78\times48$ to $1500\times280\times240$ | $87.9\times17.6\times31.3$ to $120.0\times39.3\times50.0$ |

$T_{\mathrm{rat}}=1$ (adiabatic-equivalent) at Mach 2 and $0.76$ (cold
wall) at Mach 5.86, Sutherland reference temperature 273.15 K and 100 K
respectively. The references are the DNS of Pirozzoli & Bernardini at
Mach 2 and of Cogo et al. at Mach 5.86. In the immersed-block runs of
[De Vanna et al. (2023c)](/sources/devanna-2023-c.md) the box is
$90\delta_0\times11\delta_0\times6\delta_0$ (one $\delta_0$ for the
block), the inflow is a digital filter on Musker's profile and the
convective scheme is the hybrid EP–TENO-A7 with Ducros threshold
$\Psi^*=0.1$.

Two independent setups use other codes and inflow methods:

| Case | Source | Inflow | Statistics station | Domain, grid | $\Delta x^+\times\Delta y_w^+\times\Delta z^+$ |
|---|---|---|---|---|---|
| Mach 2, DNS and under-resolved runs | [Pirozzoli (2010)](/sources/pirozzoli-2010.md) §3.2, Table 1 | recycling/rescaling | $x/\delta_0=25$: $\mathrm{Re}_\theta=1573$, $\mathrm{Re}_\tau=356$ | $L_z=5\delta_0$; sinh-stretched in $y$ | DNS $4.4\times0.54\times4.5$ ($\Delta y^+=6.1$ at the edge); grids A $19.0\times0.88\times10.5$, B $28.1\times0.94\times15.9$, C $46.4\times1.05\times25.5$ |
| Mach 2.28, DNS | [Shima et al. (2021)](/sources/shima-2021.md) Appendix | rescaling–reintroducing (Urbin & Knight) | $x=12.5\delta_0$: $\mathrm{Re}_\tau\approx480$ | $15.6\delta_0\times10.4\delta_0\times6.2\delta_0$, $601\times491\times182$ | printed $10\times0.8\times5$ ($\Delta y^+\approx9$ for $y/\delta_0\approx0.5$–6.2) |

Pirozzoli (2010) uses an isothermal wall with unsteady characteristic
conditions, nonreflecting top and outflow, sixth-order central viscous
terms with the Laplacian isolated, and RK4; Shima et al. use an
adiabatic no-slip wall and three-stage TVD Runge–Kutta at CFL about
0.6. The references are the incompressible DNS of Wu & Moin and the
experiments of Erm & Joubert (Pirozzoli), and a sixth-order compact DNS
with eighth-order filtering (Shima et al.).

## Runs and findings

**Convective schemes in WRLES and WMLES.** [De Vanna et al. (2023a)](/sources/devanna-2023.md)
compare, over 69 cases, a sixth-order energy-preserving (EP) central
scheme, [WENO-Z](/methods/weno-z.md) of orders 3, 5, 7
($\epsilon=10^{-12}$), TENO5 ($C_T=10^{-7}$) and
[adaptive TENO](/methods/adaptive-teno.md) TENO-A5, each used either
everywhere ("pure") or in a [hybrid](/methods/hybrid-weno.md) with the
EP scheme switched by a modified [Ducros sensor](/definitions/ducros-shock-sensor.md)
at thresholds $\Psi^*=0.1,0.2,0.4$ (the threshold $\Psi^*$ of the
modified sensor $\Psi_{\mathrm D}$, notation of the sensor page; the
sources' $\bar\theta$):

- *WRLES, Mach 2.* Upwinding lowers $c_f$, raises the log-layer velocity
  and the turbulent-kinetic-energy peak; the error shrinks as the WENO
  order rises and with TENO, and the EP scheme fits the DNS (§4.2,
  Figs. 1–2). WENO-Z3 gives a much shorter $\mathrm{Re}_\tau$ range over
  the same plate. The WALE model changes $c_f$ only marginally.
- *WMLES, Mach 2.* The effect is much stronger. On the coarse grid pure
  WENO/TENO do not develop wall turbulence; on the fine grid they
  overestimate the friction "dramatically"; pure WENO-Z3 is wrong on every
  grid. Hybridization at $\Psi^*=0.1$ brings all schemes close to the
  DNS and the EP solution, and at $\Psi^*=0.4$ all WENO and TENO
  curves coincide, because most of the flow is computed by the EP scheme
  (§4.3, Figs. 5–8). No pure shock-capturing scheme reaches the EP
  solution.
- *WMLES, Mach 5.86.* A pure EP run diverges on shocklets, and
  $\Psi^*=0.2$ is the largest stable threshold. At $\Psi^*=0.2$
  all TENO variants capture the mean velocity and the temperature is
  nearly scheme-independent (§4.4, Fig. 9). The authors recommend
  $\Psi^*\simeq0.2$ (§6).
- *Cost.* Per iteration and relative to pure EP, the hybrid runs take
  0.90–1.00 and the pure runs 0.95–1.32 (TENO-A5 on the fine grid the
  largest) on Intel KNL nodes (Table 2).

**Code validation.** [De Vanna et al. (2023b)](/sources/devanna-2023-b.md)
report that BL01 agrees excellently and BL02 well with the Mach 2 DNS
(a minor shift of the streamwise-fluctuation peak), and that BL03 with
TENO-A5 agrees excellently in mean velocity and temperature with the
Mach 5.86 DNS, with deviations in the inner-layer kinetic energy
(§5.2, Figs. 8–10).

**Conservative split central schemes on stretched grids.**
[Pirozzoli (2010)](/sources/pirozzoli-2010.md) (§3.2, Figs. 4–9) runs
the DNS with the sixth-order locally conservative Kennedy–Gruber split
flux (C-KG-SF) of the [conservative split derivative](/operators/conservative-split-derivative.md),
applied in computational space through the chain rule on the stretched
wall-normal grid, because, citing Ducros et al. (2000), "a fully conservative
finite-difference discretization using the split form of the convective
derivatives is not possible on a mesh with variable spacing"; central
differencing of the divergence form diverges in a short time even on
the DNS grid. The van Driest velocity
$\int_0^{\bar v_1}(\bar\rho/\bar\rho_w)^{1/2}d\bar v_1$ (Eq. (19), bars for
means, page-local) collapses on Wu & Moin's DNS with a small
logarithmic region; the transverse fluctuations agree with DNS and
experiment, the streamwise ones differ in the inner layer, which the
author ascribes to compressibility (maximum turbulent Mach number about
0.24); some ringing appears at the boundary-layer edge where the
density gradients are not resolved. On the coarsened grids A–C at
sixth order the three split forms give similar statistics, with a
non-monotone trend of the rms peak (down on A, up on B and C) and
energy pile-up in the spectra; the Feiereisen form is the least robust
and diverges on grid C, and the Kennedy–Gruber form is somewhat more
robust than Blaisdell's on still coarser grids, where the statistics
are inaccurate. On grid A second order overestimates the rms peak and
the high-wavenumber energy, and orders of six and above represent the
outer layer adequately. With the spectral error
$\varepsilon_{\mathrm{sp}}(k_z)=E_z(k_z)/E^{\mathrm{DNS}}_z(k_z)-1$ (Eq. (20);
$E_z$ the spanwise spectrum of the streamwise fluctuation, page-local)
and the effective bandwidth $k_{\mathrm{eff}}$ at which
$\lvert\varepsilon_{\mathrm{sp}}\rvert$ first exceeds 0.25, 0.5 or 1, after
Johnsen et al., and a cost model $(2+\tfrac72L+\tfrac12L^2)/k_{\mathrm{eff}}^4$
(half-width $L$, page-local), higher orders are cheaper at a given
error, with an optimal order from about ten for strict tolerances down
to six for rough ones (Fig. 9).

**Pressure-equilibrium-preserving split form without dissipation.**
[Shima et al. (2021)](/sources/shima-2021.md) (Appendix, Fig. 3) run
the second-order [KEEP-PE](/methods/keep-scheme.md) scheme without any
numerical dissipation and find the van Driest mean velocity, the
Reynolds stresses and the turbulent-kinetic-energy budget in good
agreement with the filtered compact-scheme DNS, with near-wall streaks
in the wall-parallel snapshots.

**Wall model at an immersed wall.** De Vanna et al. (2023c) overestimate
$c_f$ slightly against the DNS, less so as $\mathrm{Re}_\tau$ grows; at
$\mathrm{Re}_\tau=2000$, which they call double the largest in the
literature, they compare with a power-law fit of the DNS data,
$c_f=0.01474596\,\mathrm{Re}_\tau^{-0.27720095}$ (§4.3, Eq. 32,
Fig. 13). See [wall-modeled LES](/methods/wall-modeled-les.md) and
[immersed boundary method](/methods/immersed-boundary-method.md).

## Qualifications

- All evidence is numerical comparison with DNS; no final times or
  averaging windows are printed.
- The URANOS sources are one group with one code. Pirozzoli (2010)
  and Shima et al. (2021) are single runs with their own codes and
  inflow methods, and Shima et al.'s case serves only as a
  demonstration of the dissipation-free scheme.
- Pirozzoli (2010)'s efficiency estimate assumes cost proportional to
  $k_{\mathrm{eff}}^{-4}$ (points per direction and time steps both
  $\propto1/k_{\mathrm{eff}}$) and uses per-node operation counts, not
  timings; the first four Fourier modes are discarded. Pirozzoli (2010)
  §3.2 names a "C-FE-BL" scheme, read here as C-FE-SF *(compiler check,
  not in the sources: the three schemes compared are C-BL-SF, C-FE-SF and
  C-KG-SF, and the next sentence names the other two)*, and prints
  $\Delta x^+\approx\Delta z^+\approx4.5$ in the text against 4.4 and 4.5 in
  Table 1. The conclusions (§4) state that local conservation "cannot be proved on
  non-uniform grids" (§4); see
  [local conservation](/results/local-conservation-flux-form.md) for the
  open contradiction with later results.
- Shima et al.'s printed spacings are mutually inconsistent: with
  $15.6\delta_0$ on 601 and $6.2\delta_0$ on 182 points, $\Delta z/\Delta x\approx1.31$,
  so $\Delta x^+\approx10$ implies $\Delta z^+\approx13$, and $\Delta z^+\approx5$
  implies $\Delta x^+\approx3.8$ *(compiler check, not in the sources)*.
- The Ducros thresholds are specific to the modified, non-squared,
  compression-only sensor of these papers, with regularization
  $\epsilon_{\mathrm D}=(v_\infty/\delta_0)^2$; they do not transfer to sensors of other form.
- De Vanna et al. (2023a) attribute a "roughly doubled computing cost" of
  TENO against EP to cited works; their own Table 2 shows at most 1.32.
- The printed $\Delta x^+=90$ of the Mach 5.86 case does not follow from
  $L_x=90\delta_0$, $N_x=1400$ and $\mathrm{Re}_\tau=1200$, which give
  77.1, while the same rule reproduces every other printed spacing of
  Tables 1–4 of De Vanna et al. (2023a) *(compiler check, not in the sources)*.
- The explanatory text of De Vanna et al. (2023a) calls the effect of
  numerical viscosity a drag reduction while describing an increased mean
  wall velocity gradient (§5); the data (underestimated $c_f$ in WRLES)
  are unaffected.

# Citations

- [De Vanna et al. (2023a)](/sources/devanna-2023.md) — §§4.1–4.4, 6, Tables 1–4, Figs. 1–9.
- [De Vanna et al. (2023b)](/sources/devanna-2023-b.md) — §5.2, Table 2, Figs. 8–10.
- [De Vanna et al. (2023c)](/sources/devanna-2023-c.md) — §4.3, Table 4, Eq. 32, Figs. 11–14.
- [Pirozzoli (2010)](/sources/pirozzoli-2010.md) — §3.2, §4, Eqs. (19)–(20), Table 1, Figs. 4–9.
- [Shima et al. (2021)](/sources/shima-2021.md) — Appendix, Fig. 3.
