---
type: Source
title: "Villasenor et al. (2021) — Effects of Photoionization and Photoheating on Lyman-α Forest Properties from Cholla Cosmological Simulations"
description: "Extends the GPU code Cholla to cosmological hydrodynamics plus N-body (super-comoving coordinates, an Enzo-like single-threshold dual-energy switch, FFT gravity, cloud-in-cell kick–drift–kick particles, Grackle chemistry), validates it against Enzo, Nyx and Ramses including a new mean-cosmic-temperature test of the dual-energy switch, and runs 2048^3 Lyman-α forest simulations on 512 Summit GPUs."
resource: "doi:10.3847/1538-4357/abed5a"
source_kind: paper
authors: [Villasenor B., Robertson B., Madau P., Schneider E.]
year: 2021
venue: "Astrophys. J. 912:138"
local_file: "~/papers/mosaic/astrophysical-simulation-codes/2021-ApJ-Villasenor-1038471538-4357abed5a.pdf"
tags: [software, hydro, cosmology, gpu, dual-energy, self-gravity, cooling, chemistry, verification, performance]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

The paper extends the GPU-native, uniform-grid code
[Cholla](/software/cholla.md) (Schneider & Robertson 2015) into a
cosmological hydrodynamics plus N-body code and uses it for the CHIPS
(Cholla IGM Photoheating Simulation) suite of Lyman-α forest simulations.
The extension adds super-comoving coordinates (Martel & Shapiro 1998), so
that the unchanged hydro solver integrates the expanding-frame equations;
a [dual-energy](/methods/dual-energy-formalism.md) switch with an
Enzo-like neighbourhood maximum and one threshold, 0.035; an FFT Poisson
solver (PFFT) with a discrete-Laplacian Green's function and fourth-order
potential gradients; cloud-in-cell dark-matter particles advanced by
kick–drift–kick ([particle-mesh N-body](/methods/particle-mesh-gravity.md));
operator-split coupling to [Grackle](/software/grackle.md) with a UV
background; and a combined gas, particle and expansion time step (§2).
Validation: the [Zel'dovich pancake](/benchmarks/zeldovich-pancake.md)
against [Enzo](/software/enzo.md), dark-matter power spectra against Nyx,
Ramses and Enzo (sub-per-cent), adiabatic gas power spectra against Ramses
and Enzo (up to about 7 % and below 15 % at small scales), a new
mean-cosmic-temperature test of the dual-energy switch, and a chemistry
run against Enzo (§3). The production runs use $2048^3$ cells and
particles in a box of $50\,h^{-1}$ Mpc on 512 Summit GPUs (about 11 h,
about 1000 node-hours each), with a resolution study at $512^3$, $1024^3$
and $2048^3$ (§4, App. A). Astrophysically, the Puchwein et al. (2019)
UV background matches the small-scale Lyman-α flux power spectrum at
$2 \lesssim z \lesssim 4.5$ better than Haardt & Madau (2012), but
neither matches all scales and redshifts.

# Key claims

1. **Code extensions** (§1, §2, §7): self-gravity, a Fourier-space
   Poisson solver, a particle integrator, a comoving coordinate scheme and
   a Grackle coupling.
2. **Uniform grid** (§1): the Lyman-α absorbing gas is low-density and
   volume-filling, "making the use of AMR unnecessary and inefficient"; a
   uniform grid samples it better than AMR or SPH at equal resources.
   Argued, not measured.
3. **Comoving equations** (§2.1, eqs. 1–6): mass, momentum, total and
   internal energy in comoving density and pressure with proper peculiar
   velocity; for $\gamma = 5/3$ the expansion term in the energy equations
   vanishes.
4. **Super-comoving variables** (§2.1.2, eqs. 7–11): with them the
   adiabatic $\gamma = 5/3$ equations "are the same as the original
   equations of hydrodynamics in a non-expanding system".
5. **Hydro solver** (§2.2, eq. 12): Godunov finite volume with PPM, which
   the paper calls "third-order accurate in space and second-order accurate
   in time"; the state includes the internal energy. Integrator and
   Riemann solver are not named.
6. **Dual energy** (§2.3, eq. 13): advected internal energy kept where the
   thermal part over the neighbourhood-maximum total energy is below 0.035;
   then the total energy is reset from the internal energy. The
   Teyssier (2015) truncation-error criterion (eqs. 14–15, factor 0.5) is
   "overly restrictive" in these runs (§2.3, §3.4).
7. **Gravity** (§2.4, eqs. 16–22): FFT with the discrete-Laplacian Green's
   function (Hockney & Eastwood 1988), PFFT box decomposition, fourth-order
   gradient, time-centred source terms after the hydro update with a
   linearly extrapolated half-step potential; source-form energy coupling.
8. **Dark matter** (§2.5, eqs. 23–28): CIC deposit and interpolation with
   the same weights "to avoid self-forces"; kick–drift–kick (Miniati &
   Colella 2007), allowing variable time steps.
9. **Chemistry and cooling** (§2.6–2.7, eqs. 29–32): Grackle sub-cycled
   at the end of each step after hydro and gravity sources; species as
   passive scalars; uniform UV background from tabulated rates; optional
   CLOUDY 17.02 metal tables; production runs without metal cooling.
10. **Time step** (§2.8, eqs. 33–35): global minimum of gas (Courant 0.3),
    particle (0.3) and expansion (1 % in scale factor) limits. Cells whose
    gas step falls below 1/50 of the particle step are replaced by the
    average of their six neighbours, "less than a dozen times per
    simulation"; not conservative, effect asserted insignificant.
11. **Host/device split** (§2.9): only the hydro (with species advection)
    runs on the GPUs; FFT gravity, particles and Grackle on the CPUs; a GPU
    distributed FFT had "recently" been integrated at submission. Grackle
    is the slowest step, about half the run time (§4).
12. **Discretization sensitivity** (§3.2): the second-order potential
    gradient changes small-scale matter power by about 15 %, the continuous
    Green's function by up to about 28 %, relative to the defaults.
13. **Gas power** (§3.3): small-scale gas power is "highly sensible [sic]"
    to the hydro implementation; no robust code comparison of it is known
    to the authors.

# Tests

* [Zel'dovich pancake](/benchmarks/zeldovich-pancake.md) (§3.1,
  eqs. 36–39, Fig. 1): the Bryan et al. (2014) set-up, 256 cells; against
  Enzo below 10 % in density and temperature except at sharp shock
  features, about 20 % in velocity at the shock fronts and near zero
  velocity, below 1 % outside the shocks. With the Teyssier criterion the
  central shock is suppressed.
* Dark-matter-only power spectra (§3.2, Fig. 2): $50\,h^{-1}$ Mpc,
  $256^3$ particles and cells, MUSIC initial conditions at redshift 100;
  Nyx about 0.05 % (small scales) and 0.02 % (large); Ramses 0.1 % (large),
  about 0.7 % (small) by redshift 0; Enzo below 0.1 % (large) and 0.3 %
  (small), with matched gradient stencil and Green's function.
* Adiabatic gas power spectra (§3.3, Figs. 3–4): against Ramses (with the
  Ramses dual-energy criterion) about 1 % or less at large scales, up to
  about 7 % at small scales for redshift below 1; against Enzo below 1 %
  and below 15 %.
* Mean-cosmic-temperature test, new (§3.4, eqs. 41–42, Figs. 5–6): the
  threshold 0.035 gives heating onset near redshift 12 like the
  virial-temperature estimate; the Teyssier criterion delays heating to
  about redshift 6 and raises small-scale gas power by 30–80 %.
* Chemistry plus UV background against Enzo (§3.5, Figs. 7–8): fitted
  intergalactic temperature and temperature–density slope within 1 %.
* Resolution study (App. A, Fig. 17): $512^3$, $1024^3$, $2048^3$; the
  two finer runs "agree well"; no convergence rate.
* Cosmological-parameter study (App. B, Table 2, Figs. 18–19): four
  alternative cosmologies; mean baryon density −0.62 % to +2.12 %,
  effective optical depth −2 % to 6 %, temperature parameters ≲3 %.
* Performance (§4): 512 Summit GPUs, about 11 h, about 1000 node-hours per
  $2048^3$ run; no cell-update rate, precision or scaling study.

# Notation map

| Villasenor et al. (2021) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $a$, $\dot a$ | $a$ | scale factor |
| $H$, $H_0$ | words | Hubble parameter; not in the registry |
| $h$ (= $H_0$/100) | words | **collision:** registry $h$ is the cell size |
| $\Omega_M$, $\Omega_\Lambda$, $\Omega_k$, $\Omega_b$ | words | cosmological density parameters |
| $\rho_b$ (comoving baryon density) | $\rho$ | $\rho = a^3\rho_{\mathrm{proper}}$ |
| $\rho_{DM}$, $\bar\rho$ | words | dark-matter density, box mean |
| $\mathbf v$ | $\mathbf v$ | proper peculiar velocity |
| $E$ (specific total energy) | $E/\rho$ | **collision:** registry $E$ is an energy density |
| $e$ | $e$ | specific internal energy |
| $p$ | $p$ | comoving, $p = a^3p_{\mathrm{proper}}$ |
| $\Gamma$, $\Lambda$ (volumetric heating, cooling rates) | words | **collision:** registry $\Gamma_1$ is an adiabatic index; registry $\Lambda(T)$ is a cooling function per $n_{\mathrm e}n_{\mathrm H}$ |
| tilde variables | words ("super-comoving") | Martel–Shapiro rescaling |
| $\phi$, $\mathbf g$, $G$ | $\Phi$, $\mathbf g$, $G$ | |
| $G(\mathbf k)$ (Green's function) | words | **collision** with the gravitational constant $G$ |
| $\mathbf U$, $\mathbf F$ | $u$, $\hat f$ | |
| $\Delta x$ | $h$ | cell size |
| $\eta$ (single dual-energy threshold) | words (0.035) | not $\eta_1$ or $\eta_2$: one test both selects and resynchronizes |
| $\beta$, $e_{\mathrm{trunc}}$ | words | Teyssier (2015) factor and truncation estimate; **collision:** registry $\beta^i$ is the shift |
| $\alpha_{gas}$, $\alpha_{DM}$ | $\nu$; words | gas and particle Courant numbers |
| $m_i$, $\mathbf x_i$, $\mathbf v_i$, $\mathbf g_i$ (particles) | words | subscript $i$ also indexes cells |
| $c_s$, $\gamma$ (EOS) | $c_s$, $\gamma$ | |
| $\gamma$ (IGM temperature–density slope) | words | **collision** with the adiabatic index |
| $T_0$ | words | used for both an initial temperature and the IGM temperature at mean density |
| $\tau$, $\tau_{eff}$ | optical depth (subscripted) | registry bare $\tau$ is the Valencia energy |
| $k_B$, $m_p$ | $k_{\mathrm B}$; words | paper uses the proton mass |
| $J(\nu,z)$, $\sigma_i$, $\Gamma_{\gamma i}$, $\epsilon_i$ | words | UV intensity, cross sections, photoionization and photoheating rates |
| $P_m(k)$, $P(k)$ | words | matter and flux power spectra |

Native formulas of the Zel'dovich pancake initial conditions (§3.1,
eqs. 36–39), in the paper's notation with $x_l$ the Lagrangian
coordinate, $k$ the wavenumber of the mode, $z$ the redshift and
$z_s = 1$ the caustic redshift:
$\rho_b(x_l) = \rho_0\left[1-\frac{1+z_s}{1+z}\cos(kx_l)\right]^{-1}$,
$v(x_l) = -H_0\frac{1+z_s}{(1+z)^{1/2}}\frac{\sin(kx_l)}{k}$,
$T(x_l) = T_0\left(\rho_b(x_l)/\bar\rho_b\right)^{2/3}$,
$x = x_l - \frac{1+z_s}{1+z}\frac{\sin(kx_l)}{k}$; $L = 64\,h^{-1}$ Mpc,
$h = 0.5$, $\Omega_M = 1$, $\rho_0 = \rho_c = 3H_0^2/8\pi G$,
$T_0 = 100$ K, start at $z = 20$.

# Pages created or updated

* Created [Zel'dovich pancake](/benchmarks/zeldovich-pancake.md),
  [Particle-mesh N-body in grid codes](/methods/particle-mesh-gravity.md).
* Updated [Cholla](/software/cholla.md), [Enzo](/software/enzo.md),
  [Dual-energy formalism](/methods/dual-energy-formalism.md),
  [Grackle](/software/grackle.md).
* Per the batch plan, also cited on
  [Poisson solvers for self-gravity on adaptive meshes](/methods/multigrid-self-gravity.md)
  (FFT gravity).

# Citations

1. `~/papers/mosaic/astrophysical-simulation-codes/2021-ApJ-Villasenor-1038471538-4357abed5a.pdf`.
   * **Version.** arXiv:2009.06652v2 [astro-ph.CO], 24 Mar 2021 ("Draft
     version March 26, 2021", AASTeX62), 30 pages; the preprint, not the
     typeset article.
   * **Identity.** doi:10.3847/1538-4357/abed5a, checked on Crossref (same
     four authors in the same order; Crossref title writes "Lyα"):
     Astrophys. J. 912(2):138, issued 2021-05 (print 2021-05-01, online
     2021-05-13). Page 1 matches the Crossref record.
   * **How it was read.** Text extraction of all sections; eqs. 3–6 checked
     on the rendered pages 3–4. Figure values are taken from the text and
     captions only, not read off plots.
   * **Recorded as printed.**
     * Eq. 18 lacks the $4\pi G/a$ prefactor and normalization of the
       Green's function that eq. 16 requires.
     * App. A refers to the "left panel of Figure 19" for the large-scale
       flux-power decline; Figure 17 is meant.
     * §1 quotes "∆x ≈ 35 kpc … L ≈ 75 Mpc" without $h$, i.e.
       $24\,h^{-1}$ kpc and $50\,h^{-1}$ Mpc for $h = 0.6766$.
     * "sympletic" (§2.5) and "highly sensible" (§3.3) as printed.
     * The gas power-spectrum agreement is summarized as "within a few
       percent" (§7) while §3.3 reports up to 7 % (Ramses) and below 15 %
       (Enzo) at small scales.
   * **Reference list:** 76 printed entries (Crossref reference-count 76),
     merged complete; title-less AAS style except three books. The
     Zel'dovich (1970) entry is printed as A&A 500:13 and merged into
     `zeldovich-1970` (A&A 5:84, the pancake paper also cited by Bryan et
     al. 2014). Madau et al. (1999) ApJ 514:648 is `madau-1999-b`, distinct
     from the existing ApJ 517:L9 entry. Collaboration authors are keyed
     `desi-2016`, `desi-2016-b` and `planck-2018`; year suffixes
     `davies-2018-b`, `desi-2016-b`, `gaikwad-2020-b`, `onorbe-2017-b`. The
     bibliography holds 2157 entries after this batch.
