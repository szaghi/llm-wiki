---
type: Source
title: "Mathew & Federrath (2021) — The IMF and multiplicity of stars from gravity, turbulence, magnetic fields, radiation and outflow feedback"
description: "Application of FLASH4 (PARAMESH block AMR) to star-cluster formation in two ensembles of ten driven-turbulence MHD runs with and without protostellar outflows, documenting a production configuration: HLL5R solver, multigrid gravity, Jeans refinement at 16 cells, sinks with intrinsic spin and leapfrog integration, a piecewise-polytropic EOS and sub-grid heating and outflow modules, at one resolution and without a convergence study."
resource: "doi:10.1093/mnras/stab2338"
source_kind: paper
authors: [Mathew S.S., Federrath C.]
year: 2021
venue: "Mon. Not. R. Astron. Soc. 507:2448–2467"
local_file: "/home/stefano/papers/mosaic/astrophysical-simulation-codes/2021-MNRAS-Mathew-101093mnrasstab2338.pdf"
tags: [software, mhd, amr, self-gravity, multigrid, sink-particles, riemann-solver, equation-of-state]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

An application paper. With [FLASH](/software/flash.md) ("flash4",
PARAMESH block AMR) the authors run 2 × 10 MHD simulations of a
$775\,M_\odot$, 2 pc periodic box of driven turbulence with self-gravity,
sink particles, a density-dependent polytropic EOS and a sub-grid polar
stellar-heating model; one set (OUTFLOW) adds the sub-grid jet and outflow
model of Federrath et al. (2014), the other (NOWIND) does not. The sets
share turbulence seeds T1–T10 and all numerics. Astrophysically, outflows
halve the star-formation rate per free-fall time (7±2 % against 15±3 %),
double the number of sinks at fixed star-formation efficiency and shift
the sink mass distribution to lower masses by a factor 2.0±0.2 without
changing its shape. For this bundle the paper documents a production FLASH
configuration (HLL5R, multigrid gravity, Jeans refinement at 16 cells
below the finest level, sinks with spin and leapfrog integration) at one
resolution, finest $h = 100$ AU. There is no resolution or convergence
study, the authors name resolution as the main caveat (§6.1), and no
performance numbers are given.

# Key claims

1. **Code and mesh** (§2.1). MHD and gravity are solved "on an adaptive
   mesh refinement (AMR) (Berger & Colella 1989) grid using the PARAMESH
   library (MacNeice et al. 2000) in the flash4 code (Fryxell et al. 2000;
   Dubey et al. 2008)". No minor version.
2. **Equations** (§2.1, eqs. 1–3). Continuity, momentum with Lorentz force,
   total pressure, gravity and a stirring acceleration, and induction with
   $\nabla\cdot\mathbf B = 0$, in Gaussian units. No energy equation (closure
   by the EOS, §2.4). The divergence-control method is not stated.
3. **Self-gravity** (§2.1): "multi-grid Poisson solver ... (Ricker 2008)".
4. **Riemann solver** (§2.1): "5-wave HLL5R approximate Riemann method",
   which "has comparable accuracy to the standard FLASH-Roe solver, but it
   is more efficient and has a better stability (Waagan et al. 2011)" —
   asserted by citation. Reconstruction and time integrator not stated.
5. **Turbulence driving** (§2.2). Ornstein–Uhlenbeck acceleration field,
   "added as a momentum and energy source term", at $k = 1\ldots3$ (units
   of $2\pi/L$), driving parameter $\zeta = 0.5$ (compressive-to-total
   power about 1/3), driven continuously; velocity spectrum about $k^{-2}$.
6. **Sink creation** (§2.3, eq. 4). $\rho_{\rm sink} = \pi c_s^2/(G\lambda_J^2)
   = \pi c_s^2/(4Gr_{\rm sink}^2)$ with $r_{\rm sink} = \lambda_J/2$, plus "a
   series of tests as described by Federrath et al. (2010c)" (the
   ingested [Federrath et al. (2010)](/sources/federrath-2010.md)). Sink
   size $2r_{\rm sink} = 5\Delta x$ at the finest level, which "ensures that
   the Truelove et al. (1997) criterion is satisfied"; $r_{\rm sink} = 250$ AU.
   No new sink within 250 AU of an existing one (§5.2).
7. **Jeans refinement** (§2.3). "On all other AMR levels, $\lambda_J$ is
   always resolved with at least 16 grid cell lengths to prevent
   underestimation of the turbulent energy and to resolve the local
   collapse reasonably well (Federrath et al. 2011)."
8. **Sink accretion, spin and integration** (§2.3, §5.2). Mass, linear and
   angular momentum updated at every accretion step; the sink moves to the
   centre of mass of sink plus accreted gas. "In order to conserve total
   angular momentum, an intrinsic angular momentum (spin) is introduced
   for the sink particle, which stores the accreted angular momentum"; the
   spin sets the outflow axis. Sink–gas and sink–sink gravity "by direct
   summation over all the sink particles and grid cells", softened within
   the accretion radius; "A second-order leapfrog integrator".
9. **EOS** (§2.4, eqs. 5–7). $P_{\rm EOS} = c_s^2\rho^\gamma$,
   $c_s = 0.2$ km s$^{-1}$, $\mu = 2.35$; $\gamma = 1$, 1.1, 1.4, 1.1, 5/3 with
   breakpoints $2.50\times10^{-16}$, $3.84\times10^{-13}$,
   $3.84\times10^{-8}$, $3.84\times10^{-3}$ g cm$^{-3}$, after
   radiation-hydrodynamic collapse calculations (Larson 1969; Masunaga &
   Inutsuka 2000).
10. **Polar radiative heating** (§2.5.1, eqs. 8–11; Mathew & Federrath
    2020). Absorbed power through an analytic disc and dust model around
    each sink, an equilibrium heating temperature (reprocessed radiation
    neglected), luminosity from the Offner et al. (2009) protostellar
    model, and $P = [P_{\rm EOS}^4 + P_{\rm heat}^4]^{1/4}$ "imposed in the MHD
    momentum equation". Radiative transfer is not solved (impractical for
    the ensemble, §§2.4–2.5.1).
11. **Jets and outflows** (§2.5.2, eqs. 12–13; Federrath et al. 2014).
    Momentum injected in two cones, $\theta_{\rm out} = 30^\circ$,
    $r_{\rm out} = 16\Delta x$, with radial and angular smoothing "to prevent
    numerical artifacts"; $f_m = 0.3$ of the accreted mass ejected;
    $\vert\mathbf V_{\rm out}\vert = 100$ km s$^{-1}$ $(M_{\rm sink}/0.5M_\odot)^{1/2}$;
    $f_a = 0.9$ of the accreted angular momentum returned. Resolution
    independence ("almost independent of the resolution") is cited, not
    tested.
12. **Set-up** (§2.6, Table 1). Triple-periodic $L = 2$ pc box, effective
    $4096^3$, minimum cell 100 AU; $\rho_\circ = 6.56\times10^{-21}$ g cm$^{-3}$,
    $M_{\rm cl} = 775\,M_\odot$, $t_{\rm ff} = 0.82$ Myr, $\sigma_v = 1.0$ km s$^{-1}$,
    $\mathcal M = 5.0$, $B = 10^{-5}$ G along $z$, $\alpha_{\rm vir} = 0.5$.
    Driving without gravity for 2 Myr, then gravity and sinks on; runs end
    at 5 % star-formation efficiency. Root grid and level count not stated.
13. **Statistics instead of resolution** (§3, §§6.1–6.2). Ten realizations
    per model are run instead of higher resolution, to obtain "a
    statistically converged sample of stars"; sub-grid models are argued
    "necessary to obtain statistically conclusive and quantitatively
    accurate results in a cost-efficient way".

Astrophysical results, one line each (Table 1, NOWIND / OUTFLOW): time to
5 % efficiency 0.68±0.15 / 0.89±0.20 $t_{\rm ff}$; star-formation rate per
free-fall time 15±3 % / 7±2 %; 212 / 449 sinks; median mass 1.0±0.3 /
0.5±0.1 $M_\odot$; high-mass slope 1.3±0.2 / 1.5±0.3. Sink-number ratio
2.1±0.1 at equal efficiency (1–5 %), 1.3±0.1 at equal time (§3).

# Tests

No verification test and no standard benchmark.
* **NOWIND against OUTFLOW** (§3, Table 1, Figs. 1–6): 10 + 10 runs with
  identical seeds and numerics; spreads are standard deviations over the
  realizations. Seed-to-seed scatter of the 1D sink velocity dispersion is
  0.65–1.74 km s$^{-1}$, mean 1.1±0.3 (§4.4).
* **Against Federrath et al. (2014)** (§3): the same factor of about 2 in
  star-formation rate from outflows, although that study had no stellar
  heating; equal-time sink increase about 1.5 there against 1.3±0.1 here.
* **Against IMF models and observations** (§4, Figs. 7–8, Table 2): peak
  mass about 2× above observed; brown-dwarf-to-star ratio 43/225 = 0.19.
* **Multiplicity** (§5.1, eq. 17, Figs. 12–13): the Bate (2009a)
  bound-pair algorithm up to quadruples.
* **Resolution sensitivity estimated, not rerun** (§§5.1–5.2, 6.1,
  Fig. 16): rotational-to-gravitational energy above 0.01 in 92 of 449 sinks
  (20 %), taken as likely to fragment at higher resolution; the separation
  distribution below about 200 AU is "only a lower limit", and "a
  resolution study would be required"; about 10–20 AU would be needed to
  capture the IMF peak if it is set by the first core.
* **Performance:** none reported.

# Notation map

| Mathew & Federrath (2021) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho$, $\mathbf v$, $\mathbf B$ | $\rho$, $\mathbf v$, $\mathbf B$ | $\mathbf B$ in **Gaussian** units ($(\mathbf B\cdot\nabla)\mathbf B/4\pi$, $\vert\mathbf B\vert^2/8\pi$); Heaviside–Lorentz $\mathbf B = \mathbf B_{\rm G}/\sqrt{4\pi}$ |
| $P$ | $p$ | barotropic, plus the heating term |
| $P_{\rm tot}$ | $P^*$ | $p + \vert\mathbf B\vert^2/(8\pi)$ in Gaussian units |
| $P_{\rm EOS}$, $P_{\rm heat}$ | none (words) | polytropic and heating pressures |
| $\mathbf g$ | $\mathbf g$ | gas self-gravity plus the direct-sum sink acceleration |
| $\mathbf F_{\rm stir}$ | none (words) | turbulence-driving acceleration; **collision:** registry $\mathbf F_{\mathrm r}$, $\mathbf F_{\mathrm g}$, $\mathbf F_{\mathrm{ph}}$ are fluxes |
| $\zeta$, $k$ | none (words) | driving parameter; wavenumber in units of $2\pi/L$ |
| $c_s$ | $c_s$ | **note:** isothermal sound speed (registry $c_s$ is adiabatic) |
| $\gamma$ | none (words) | **collision:** piecewise polytropic exponent of $P = c_s^2\rho^\gamma$, not the ratio of specific heats |
| $\rho_1\ldots\rho_4$ | none (words) | EOS breakpoints |
| $\lambda_J$ | $\lambda_{\mathrm J}$ | |
| $\rho_{\rm sink}$ | $\rho_{\mathrm{thr}}$ | sink-formation threshold |
| $r_{\rm sink}$ | $r_{\mathrm{acc}}$ | sink (accretion) radius, 250 AU; also the softening scale |
| $M_{\rm sink}$, $\mathbf V_{\rm sink}$ | $M_{\mathrm s}$, $\mathbf v_{\mathrm s}$ | |
| $\Delta x$, $\Delta x_{\rm cell}$ | $h$ | finest-level cell size, 100 AU |
| $N_{\rm eff,res}^3 = 4096^3$ | $N = 4096$ | effective cells per dimension |
| $t_{\rm ff}$, $\dot M_{\rm acc}$ | $t_{\mathrm{ff}}$, $\dot M$ | |
| $\mu$, $m_H$, $k_B$ | $\mu$, $m_{\mathrm H}$, $k_{\mathrm B}$ | |
| $\kappa$, $\tau$, $\chi$ | $\kappa$, $\tau_\lambda$, none (words) | **collision:** bare $\tau$ is the Valencia energy in the registry |
| $L_\star$, $T_{\rm heat}$, $\sigma_{SB}$ | none (words) | sub-grid heating quantities |
| $\theta_{\rm out}$, $r_{\rm out}$, $f_m$, $f_a$, $M_{\rm out}$, $\mathbf V_{\rm out}$, $\mathbf P_{\rm out}$ | none (words) | outflow parameters; **collision:** registry $f_{\mathrm m}$ is Kastaun's master function |
| $\mathcal M$, $\sigma_v$, $\alpha_{\rm vir}$ | none (words) | sonic Mach number, velocity dispersion, virial parameter |
| $\Gamma$ (IMF slope) | none (words) | **collision** with $\Gamma_1$ |
| $j$, $E_{\rm rot}$, $E_{\rm grav}$, $I$, $\omega$, $\epsilon$ | none (words) | sink-spin diagnostics (eq. 18) and core-to-star efficiency; **collision:** $E$ is the total energy density in the registry |

# Pages created or updated

* Created [FLASH](/software/flash.md).
* Updated [Adaptive mesh refinement in astrophysical codes](/methods/adaptive-mesh-refinement.md),
  [Poisson solvers for self-gravity on adaptive meshes](/methods/multigrid-self-gravity.md).
* Per the batch plan, also cited on [Sink particles](/methods/sink-particles.md)
  and the [Jeans resolution criterion](/definitions/jeans-resolution-criterion.md).

# Citations

1. `~/papers/mosaic/astrophysical-simulation-codes/2021-MNRAS-Mathew-101093mnrasstab2338.pdf`.
   * **Version.** arXiv:2106.06521v2 (11 Aug 2021), the accepted manuscript
     in MNRAS style ("Preprint 12 August 2021"; "Accepted XXX. Received
     YYY"), 24 PDF pages (21 plus Appendix A figures), not the typeset
     article; section, equation, figure and table numbers are the
     preprint's.
   * **Identity.** doi:10.1093/mnras/stab2338, checked on Crossref: Mon.
     Not. R. Astron. Soc. 507(2):2448–2467, online 2021-08-13, print issue
     2021-08-31; authors Sajay Sunny Mathew and Christoph Federrath, first
     author's surname Mathew on page 1 and on Crossref. The Crossref title
     has a serial comma ("radiation, and outflow feedback").
   * **How it was read.** Text extraction, all sections; eqs. 4, 7 and 11,
     garbled in the text layer, read from rendered pages 3–4. Figures read
     for captions and the numbers in the text only.
   * **Recorded as printed.** Eq. 4 with the printed $c_s = 0.2$ km s$^{-1}$
     and $r_{\rm sink} = 250$ AU gives $3.37\times10^{-16}$ g cm$^{-3}$
     ($3.32\times10^{-16}$ with $r_{\rm sink} = 2.5L/4096$), while Table 1
     prints $\rho_{\rm sink} = 3.8\times10^{-16}$ g cm$^{-3}$, about 13 % higher;
     the paper does not explain the difference. The threshold lies just
     above the first EOS breakpoint, so sinks form in the 1.1 branch. Other
     checks pass: $L/4096 = 100.7$ AU, $M_{\rm cl} = \rho_\circ L^3$,
     $t_{\rm ff} = 0.82$ Myr, $L/\sigma_v = 1.96$ Myr against the printed
     2 Myr. The Fig. 4 caption says "T0–T10" (the text T1–T10); a
     star-formation-rate range is printed as "0.05 < $t_{\rm elap}/t_{\rm ff}$ <
     0.25 $t_{\rm ff}$". The gravity statement (direct summation over sinks
     and grid cells) differs in wording from the cloud-in-cell gas-to-sink
     interpolation of Federrath et al. (2010), §2.4; the code versions
     differ. Not stated: FLASH minor version, reconstruction, time
     integrator, Courant number, $\nabla\cdot\mathbf B$ control, root grid
     and level count, refinement criteria other than Jeans, CPU cost.
   * **Reference list:** 222 printed entries; MNRAS style prints no article
     titles except for Kroupa et al. (2013) and Spitzer (1978), and DOIs
     only for 12 entries. The list's Federrath et al. 2010a is
     `federrath-2010-c` (Highlights Astron.), 2010b is `federrath-2010-b`
     (A&A 512:A81) and 2010c is the ingested `federrath-2010` (ApJ 713:269).
     Printed-order suffixes were resolved by venue, volume and page: the
     Bate 2009 and Hennebelle 2008 pairs swap against the existing keys;
     Cabrit 2007 (A&A 468:L29) is `cabrit-2007-b`, Kim 2019 (AJ 157:109)
     `kim-2019-b`; Krumholz 2007 and Wang 2010 map to the existing
     `krumholz-2007-b` and `wang-2010-b`; works sharing an existing stem
     take new suffixes (`federrath-2011-b`, `gammie-1996-b`,
     `hopkins-2012-b`, `seifried-2012-b`, `shu-1988-b`, `smith-2008-b`).
