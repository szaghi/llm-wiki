---
type: Source
title: "Rosdahl et al. (2013) — RAMSES-RT: Radiation hydrodynamics in the cosmological context"
description: "Adds multigroup ionizing radiative transfer to the cell-based AMR code RAMSES as an explicit first-order M1 moment method in photon number with HLL or global Lax–Friedrichs fluxes, operator-split non-equilibrium H/He thermochemistry and a reduced speed of light whose validity it bounds by f_c = min(1, ~10 t_cross/tau_sim); RT is multi-stepped with the hydro across levels, not subcycled, so photons are conserved exactly in transport."
resource: "doi:10.1093/mnras/stt1722"
source_kind: paper
authors: [Rosdahl J., Blaizot J., Aubert D., Stranex T., Teyssier R.]
year: 2013
venue: "Mon. Not. R. Astron. Soc. 436:2188–2231"
local_file: "~/papers/mosaic/astrophysical-simulation-codes/2013-MNRAS-Rosdahl-101093mnrasstt1722.pdf"
tags: [software, radiation, reduced-speed-of-light, amr, riemann-solver, cosmology, benchmark]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

RAMSES-RT adds radiative transfer of hydrogen- and helium-ionizing photons
to RAMSES, a cell-based oct-tree AMR code. It evolves the first two
angular moments of the transfer equation in photon-number form, in a few
frequency groups, closed with the local M1 Eddington tensor (§2). The
transport is an explicit, first-order Godunov finite-volume scheme with an
HLL or a global Lax–Friedrichs (GLF) flux (§3.2). The gas coupling is
operator-split: photon injection, then transport, then a quasi-implicit
non-equilibrium thermochemistry step that subcycles locally (§3). The
explicit transport makes the light-crossing Courant limit binding, so the
paper adopts a reduced speed of light and derives its validity criterion
from the finite-light-speed Strömgren-sphere solution (§4.2). Each AMR
level does its radiation on that level's hydro step, without subcycling
(§5.2). Verification uses the Iliev et al. (2006, 2009) comparison tests
against C²-Ray. Merged into [RAMSES-RT](/software/ramses-rt.md),
[M1 radiation transport](/methods/m1-radiation-transport.md),
[reduced speed of light](/definitions/reduced-speed-of-light.md),
[approximate Riemann solvers](/methods/approximate-riemann-solvers.md) and
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md).

# Key claims

1. **Moment equations** (§2, eqs. 3–7). Per frequency group, the photon
   number density $N_{\mathrm{ph}}$ and number flux $\mathbf F_{\mathrm{ph}}$
   obey a conservation law with absorption by H I, He I and He II, stellar
   injection and recombination emission as sources. Group cross sections
   and energies are global averages over an assumed source spectrum
   (eqs. 9–11), set by hand or computed on the fly from SED tables (App. B).
2. **M1 closure** (§2, eqs. 12–14).
   $\mathsf f_{\mathrm E} = \tfrac{1-\chi_{\mathrm E}}{2}\mathsf I + \tfrac{3\chi_{\mathrm E}-1}{2}\hat{\mathbf n}\hat{\mathbf n}$,
   $\chi_{\mathrm E} = \frac{3+4f_{\mathrm r}^2}{5+2\sqrt{4-3f_{\mathrm r}^2}}$,
   with $0 \le f_{\mathrm r} \le 1$. The closure is local, the system is
   hyperbolic with wave speeds at most $c$ (§1.1.2). Stated failure:
   opposing beams cannot cross and create a spurious perpendicular source
   (Fig. 1).
3. **Transport scheme** (§3.2, eqs. 20–22). Explicit conservative update
   of $u = (N_{\mathrm{ph}}, \mathbf F_{\mathrm{ph}})$, first order in space and
   time (§7), with no reconstruction.
4. **HLL flux** (§3.2, eq. 23). Wave-speed bounds from the eigenvalues of
   the flux Jacobian, which depend only on $f_{\mathrm r}$ and the angle of
   the flux to the interface, read from the table of González, Audit &
   Huynh (2007). **GLF flux** (eq. 24): HLL with bounds $\pm c$. GLF is more
   diffusive and nearly isotropic around point sources; HLL keeps
   axis-aligned beams and shadows but makes isotropic sources anisotropic;
   diagonal beams leak almost equally with both (Fig. 1). Same cost. GLF is
   the default for cosmological and galactic runs.
5. **Thermochemistry** (§3.3, App. A). $4 + 2M$ coupled equations for $M$
   groups, solved sequentially in a fixed order after Anninos et al.
   (1997), each variable semi-implicit in itself ("quasi-implicit"). The
   "10% rule": a sub-step is redone with half the step if any quantity
   changes by more than 10%, and the next sub-step is doubled if the largest
   change is below 5%. Photons are therefore conserved only "at the 10%
   level" in the thermochemistry; the transport step conserves them
   (footnote 4).
6. **Radiation time step** (§4.1, eq. 31; §6, eq. 45). In 3D,
   $\Delta t < h/(3c)$; the tests use Courant number 0.8 with the reduced
   speed, $\Delta t = 0.8\,h/(3\hat c)$. The light-speed step is "typically
   300 times shorter" than the hydro step. Implicit transport is rejected:
   it still needs a trial-and-error global step for accuracy and requires
   iterative matrix solves.
7. **Reduced speed of light** (§4.2, eqs. 32–33, Fig. 2, Table 1). From the
   finite-light-speed I-front solution (after Shapiro et al. 2006), the
   front follows its infinite-$c$ limit after one light-crossing time;
   reducing $c$ by $f_c$ multiplies the crossing time by $1/f_c$. Recipe:
   $f_c = \min(1;\ \sim10\,t_{\mathrm{cross}}/\tau_{\mathrm{sim}})$. Table 1
   minimum $f_c$: Milky Way ISM $3\times10^{-2}$, Milky Way cloud
   $6\times10^{-4}$, Iliev tests 1, 2 and 5 $2\times10^{-2}$, Iliev test 4
   (IGM reionization) 1. Galaxy-scale ISM work tolerates
   $f_c \simeq 10^{-4}$–$10^{-3}$ (§4.3); reionization of the IGM needs the
   true $c$.
8. **Smoothed RT** (§4.4, eqs. 34–37). Optional: the thermochemistry starts
   from the pre-injection, pre-transport state and receives the injection
   and transport increments as constant rates. In a cosmological zoom it
   cut thermochemistry subcycles 6-fold and wall time 3.5-fold.
9. **Hydrodynamics** (§5, eqs. 38–42). A second-order Godunov (MUSCL)
   scheme on the Euler equations with gravity and cooling source terms; the
   hydro Riemann solver is not specified in this paper. Super-comoving
   variables in $a$ are extended to the radiation (§5.4); redshift dilution
   of photon energy is not included.
10. **Mesh** (§5, Fig. 4). The oct ($2\times2\times2$ cells) is the basic
    element of a cell-based recursive tree, $r_{\mathrm{ref}} = 2$, uniform
    refinement to a minimum level and adaptive refinement above it, with
    graded (2:1) refinement across cell boundaries.
11. **AMR time stepping** (§5.1, Fig. 5, Listing 1). Two substeps on level
    $l+1$ per step on $l$, $\Delta t_l \le \Delta t_{l-1}$. Fluxes across a
    coarse-fine interface partially update the coarse neighbour, whose state
    stays ill-defined until its step completes (App. D, Fig. D1).
12. **RT on the AMR hierarchy** (§5.2, Fig. 6, Listing 2, App. D). RT is
    **not** subcycled within the hydro step: the partially updated coarse
    states make thermochemistry ill-defined, and App. D argues conservative
    subcycling is "not possible (or at least nontrivial)". Each level runs
    injection, hydro, transport and thermochemistry on one
    $\Delta t_l = \min(\Delta t_{\mathrm{hydro}}, \Delta t_{\mathrm{RT}})$, so
    the radiation is multi-stepped across levels like the hydro. Inter-level
    radiation fluxes partially update coarse cells (§5.3). Optional
    refinement criteria act on photon density, ion fractions and their
    gradients. Storage for $u$ grows by $1.5(1 + 4/9M)$, about 3.5 times for
    $M = 3$.
13. **Conservation across levels** (§5.3, eq. 43, Figs. 7–8). 2D beams
    crossing static refinement from level 6 to 8: total flux constant to
    about 1 in $10^4$ after two crossing times for the 26.5° beam, and to "7
    decimals" (the number precision) for the horizontal beam with HLL;
    within 0.03% with refinement on photon-density gradients (threshold
    0.4). Diffusion comes from the flux function, not from refinement.
14. **Parallelism.** RAMSES's existing MPI strategies (§5.2). No threading
    or GPU. No scaling numbers are given.
15. **Open items** (§7): a second-order (MUSCL-type) transport solver,
    optional RT subcycling at the cost of strict photon conservation,
    coupling with the GPU code ATON for full-$c$ transport on the coarse
    grid, radiation pressure on dust, and further photon groups.

**Tests** (§6, default: H only, smoothed RT, GLF, on-the-spot
approximation, $f_c = 1/100$, three groups for a $10^5$ K blackbody,
typically $64^3$ plus one AMR level, Courant number 0.8). Iliev et al.
(2006) tests 0–4 and Iliev et al. (2009) tests 5–7, compared with C²-Ray
and the other codes of those comparisons: the isothermal Strömgren sphere
matches C²-Ray and the analytic front with an initial RSLA lag (test 1);
$r_{\mathrm{num}}/r_{\mathrm{analyt}}$ is 1.01–1.11 with heating (test 2); the
dense-clump shadow is kept by HLL with $f_c = 0.1$ and eroded by GLF or
without the on-the-spot approximation (test 3); in the cosmological field
$f_c = 1$ lags C²-Ray, which the authors attribute to the infinite-$c$ codes
giving premature fronts (test 4); the RHD tests 5–7 match in front position
and speed, with the clump I-front at about 5.7 kpc against about 5.6 kpc in
four of six comparison codes. No convergence orders or error norms are
reported; all comparisons are code-to-code or against analytic front
positions.

# Notation map

| Rosdahl et al. (2013) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $N_i$, $\mathbf F_i$ | $N_{\mathrm{ph}}$, $\mathbf F_{\mathrm{ph}}$ | per group $i$; photon number, not energy |
| $\mathbb P_i$, $\mathbb D_i$ | $\mathsf P_{\mathrm r}$, $\mathsf f_{\mathrm E}$ | number-based pressure tensor |
| $\chi_i$, $f_i$, $\mathbf n_i$ | $\chi_{\mathrm E}$, $f_{\mathrm r}$, $\hat{\mathbf n}$ | $f$ collides with the registry flux $f(u)$ |
| $c$, $c_r = f_c c$ | $c$, $\hat c = f_c c$ | |
| $\mathcal U$, $\mathcal F(\mathcal U)$, $\mathcal F_{l+1/2}$ | $u$, $\mathbf f(u)$, $\hat f_{i+1/2}$ | **collision:** the paper's $l$ is a cell index |
| $\lambda^\pm$, $\lambda^{\max}$, $\lambda^{\min}$ | $\lambda^{(p)}$ | |
| $\Delta x$ | $h$ | |
| $\ell$, $\ell_{\min}$, $\ell_{\max}$ | $l$ | the paper's root is $\ell = 1$ (one oct); registry root is $l = 0$ |
| $\Delta t_{\mathrm{RT}}$, $\Delta t_\ell$ | $\Delta t$, $\Delta t_l$ | |
| $\kappa_\nu$ | words | **collision:** per unit length here, per unit mass in the registry |
| $\mathbf u$, $P$, $\varepsilon$, $\phi$ | $\mathbf v$, $p$, $\rho e$, $\Phi$ | $\varepsilon$ is the thermal energy density |
| $\Lambda$ | part of $s(u)$ | heating and cooling |
| $a$ | $a$ | scale factor |
| $\tau$ (optical depth), $\tau_\star$ | words | **collision** with the Valencia $\tau$ |

# Pages created or updated

* Created [RAMSES-RT](/software/ramses-rt.md),
  [M1 radiation transport](/methods/m1-radiation-transport.md),
  [Reduced speed of light](/definitions/reduced-speed-of-light.md).
* Updated [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md),
  [Adaptive mesh refinement](/methods/adaptive-mesh-refinement.md).
* Also cited on [Integrating cooling and chemistry source terms](/methods/radiative-cooling-integration.md).

# Citations

1. `~/papers/mosaic/astrophysical-simulation-codes/2013-MNRAS-Rosdahl-101093mnrasstt1722.pdf`.
   * **Version.** arXiv:1304.7126v2 (13 Sep 2013), the accepted manuscript in
     MN LaTeX ("Printed 16 September 2013"), 49 pages, not the typeset
     article. No repository URL, licence, version or language is printed.
   * **Identity.** doi:10.1093/mnras/stt1722, checked on Crossref (title, five
     authors in order, volume, issue and pages match): Mon. Not. R. Astron.
     Soc. 436(3):2188–2231, 2013 (online 2013-10-09).
   * **How it was read.** Text extraction, all sections; eqs. 3–7, 12–14,
     23–24 and 31–37 checked on rendered pages 6, 8, 10, 11 and 12. The
     thermochemistry discretization (App. A, eqs. A1–A30), the rate fits
     (App. E), the SED formulas (App. B) and eqs. 28–30 are garbled in the
     text layer and are not reproduced. Figs. 2 and 5 were read through
     captions and text.
   * **Recorded as printed.** §6.7 says the core Strömgren radius is "given
     by Eq. 47"; the Strömgren radius is eq. 32, and eq. 47 is the
     time-dependent front radius.
   * **Reference list:** 87 entries, no article titles printed (book titles
     only for Osterbrock & Ferland 2006 and Toro 1999). "In preparation"
     works cited in the text (Geen et al. 2013, Powell et al. 2013) are not
     in the list and not merged. Same-stem keys distinguished by
     journal, volume and page: `abel-2002-b`, `cen-1992-b`,
     `krumholz-2007-c`, `shin-2008-b`.
