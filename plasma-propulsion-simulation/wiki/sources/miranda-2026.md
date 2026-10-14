---
type: Source
title: "Miranda et al. (2026) — Spectral entropy of plasma oscillations in numerical simulations of a Hall thruster during start-up transients"
description: "2D axial–azimuthal electrostatic PIC-MCC (XOOPIC) of an SPT-100-like Hall thruster in xenon and argon at real mass ratio and permittivity, applying the normalized 1D and 2D Fourier spectral entropy to the azimuthal field of the electron drift instability and conjecturing that more ordered fluctuations go with stronger anomalous transport."
resource: "doi:10.1007/s44205-026-00180-2"
source_kind: paper
authors: [Miranda R.A., Costa S.G.S.P., Alves R.A., Ferreira J.L.]
year: 2026
venue: "J. Electr. Propuls. 5:7"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2026_Crossref_Journal_of_Electric_Propulsion_Miranda_Spectral_entropy_of_plasma_oscillations_in_numerical_simulat.pdf"
tags: [pic, mcc, hall-thruster, instability, anomalous-transport, oscillation]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

The authors run 2D axial–azimuthal electrostatic PIC-MCC simulations of an
SPT-100-like Hall thruster with XOOPIC, in xenon and argon, at the real
mass ratio and the real vacuum permittivity. The domain is 4 cm × 2 cm on a
256 × 256 grid. The runs do not reach a steady state and are presented as
start-up transients. The electron drift instability appears as a ~1 mm
azimuthal wave in $E_\theta$; in argon a ~10 mm wave is superposed. The
contribution is the normalized Fourier power spectral entropy, in 1D (an
azimuthal line) and 2D (the whole axial–azimuthal field), applied to
$E_\theta$. Xenon gives higher entropy (0.57 in 1D, 0.79 in 2D) than argon
(0.44, 0.65), and argon gives the larger mean electron axial velocity. From
this the authors conjecture that ordered wave patterns go with stronger
anomalous transport, a link that "must be verified carefully". Merged into
[Spectral entropy of plasma oscillations](/methods/spectral-entropy.md),
[Electron drift instability (ECDI)](/definitions/electron-drift-instability.md)
and [Anomalous electron cross-field transport](/definitions/anomalous-electron-transport.md).

# Key claims

1. **Instability pattern** (§3, Fig. 6a–b; shown). In xenon, $E_\theta$ and
   $n_i$ show the drift-instability wave at $t=4.24\times10^{-5}$ s, with
   amplitude peaking near $z\sim0.02$ m; wavelength ~1 mm, frequency ~1–10
   MHz (frequency attributed to Lafleur et al., not measured).
2. **Argon** (§3, Figs. 6c–d, 7b; shown). The ~1 mm wave is superposed on a
   ~10 mm wave (spectral peaks at $k\sim100$ and $\sim1000$ m⁻¹). The authors
   say the long wave "may be related" to the lower plasma density, which
   lowers anomalous transport and lets transit-time instabilities develop
   (speculation).
3. **Comparison with linear theory** (§3, Fig. 7a; shown). The xenon 1D
   power spectrum of $E_\theta$ peaks at $k\sim896$ m⁻¹, $\lambda_w=1.1\times10^{-3}$ m,
   against $\lambda_w=2\pi\sqrt2\,\lambda_D=9.34\times10^{-4}$ m and
   $\omega=\omega_{pi}/\sqrt3=8.55\times10^6$ (Boeuf & Garrigues 2018), called
   "consistent with the ion-acoustic theory". Radial–azimuthal PIC shows a
   modified two-stream instability, and 3D PIC is needed (attributed).
4. **Spectral entropy** (§3, Table 1; shown), averaged over the last 10
   snapshots: Xe $H=0.57\pm0.05$ (1D), $0.79\pm0.003$ (2D); Ar $0.44\pm0.12$,
   $0.65\pm0.119$. Mean electron axial velocity over $0.015<z<0.030$: Xe
   $-3488.2\pm1592.9$ m/s, Ar $-6328.4\pm2346.6$ m/s.
5. **Interpretation and conjecture** (§4–5; stated). The waves are coherent
   structures, so the microturbulence "is not a completely random process";
   ordered patterns may go with stronger anomalous transport. Unpublished
   neon runs (no instability, low axial velocity, high entropy) "appear to
   confirm" it; no data shown.
6. **2D above 1D** (§4; stated). $H$ in 2D exceeds $H$ in 1D, possibly from
   random fluctuations in different regions that may be physical or noise
   from low-density regions; a particles-per-cell study is under way.
7. **Other work** (§4; attributed). Croes et al. (2018): instability
   frequency depends on ion mass, electron mobility "seems to be
   independent of the propellant"; Lafleur et al.: transition from three
   wavelengths to one equal to the azimuthal length; Janhunen et al.:
   inverse cascade of transport to low $k$ in larger azimuthal domains.
8. **Currents and potential** (§3, Figs. 4–5; shown). Plume ion current
   $0.60\pm0.30$ A and electron current $-0.58\pm0.28$ A; typical Hall-thruster
   potential with acceleration region at $z>0.025$ m; negative mean
   azimuthal electron velocity in $0.02<z<0.03$ m, consistent with the
   $\mathbf E\times\mathbf B$ drift.
9. **Method** (§2.2, eqs. 5–11). Normalized 1D and 2D spectral entropy,
   0 for a single mode, 1 for uniform power; previous applications to drift
   waves, mean-field dynamos and a Keplerian shear flow.

# Models and numerics

* **Model.** Fully kinetic electrostatic [PIC-MCC](/methods/pic-mcc.md),
  2D3V; electrons and ions as particles; neutrals a fixed background
  $n_n(z)=n_0\{1-\tanh[(z-0.02)/0.004]\}$, $n_0=3\times10^{19}$ (units not
  printed, presumably SI).
* **Geometry.** Cartesian axial–azimuthal slab, curvature neglected;
  axial 0.04 m (anode at $z=0$, exhaust plane at 0.025 m, plume boundary at
  0.04 m), azimuthal 0.02 m. Grid 256 × 256; printed $\Delta x=7.81\times10^{-5}$ m
  (the azimuthal spacing; the axial spacing $1.56\times10^{-4}$ m is not
  printed). $\Delta t=10^{-11}$ s; snapshots at $4.24\times10^{-5}$ s.
* **Field.** Poisson solve; XOOPIC's solver is not parallelized, so runs
  take "extremely long execution time" (§2.1); run times not stated.
  Dirichlet 300 V at the anode, 0 V at the cathode; periodic in $\theta$;
  particles crossing the axial boundaries are removed; no walls, sheaths or
  SEE.
* **Magnetic field.** Radial, static, Gaussian in $z$ with peak $B_0=170$ G
  at $z=0.025$ m and two widths (eq. 1).
* **Collisions.** MCC with the null-collision method (Vahedi & Surendra);
  xenon: electron elastic, excitation, ionization and ion charge exchange;
  argon adds ion elastic scattering. Cross-section sets not stated.
* **Cathode.** Electrons injected in $0.0375<z<0.039$ m; high initial
  current, then $1.56\times10^{11}$ particles/s, then equal to the
  anode-collected current.
* **Scaling.** None: mass-ratio reduction and permittivity scaling are
  avoided because they make results harder to interpret (§2.1).
* **Constraints** (§3, p. 8, attributed to their refs. 5, 27, 28).
  $\Delta t<0.2/\omega_{pe}$ and $\Delta x<3.4\lambda_D$; with mean
  $n_e\sim1.65\times10^{16}$ m⁻³: $\lambda_D=8.18\times10^{-5}$ m,
  electron Larmor radius $1.15\times10^{-4}$ m, printed bounds
  $\Delta t<1.73\times10^{-10}$ s and $\Delta x<2.78\times10^{-4}$ m (see
  Recorded as printed). Particle weight and particles per cell not stated.
* **Code.** XOOPIC (Verboncoeur, Langdon & Gladd 1995), free licence; no
  GPU; codes at gitlab.com/rmiracer.
* **Anomalous transport model.** None; transport is self-consistent.

# Tests and results

* **Xe** (§3, Figs. 3–7a, Table 1): 300 V, 170 G; no steady state (particle
  count still oscillating, Fig. 3). Results in Key claims 1, 3, 4, 8.
* **Ar** (§3, Figs. 6c–d, 7b, Table 1): same set-up; visibly lower plasma
  density; results in Key claims 2 and 4. Plume currents not reported
  separately.
* No verification or benchmark case, no convergence or particle-count
  study, no experiment; neon mentioned without data (§4).

# Notation map

| Miranda et al. (2026) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $z$ (axial), $\phi$ (azimuthal) | $z$, $\theta$ | **collision:** the paper's $\phi$ is the azimuthal coordinate, the registry's the potential (the paper never names the potential) |
| $E_\phi$ | $E_\theta$ | |
| $B_0$, $z_B$, $\sigma_{B1}$, $\sigma_{B2}$ | $\mathbf B$ peak and profile parameters | page-local |
| $n_N$, $n_0$, $z_N$, $\sigma_N$ ($\sigma_n$) | $n_n$, $n_0$, profile parameters | **collision:** $\sigma_N$ is a width, not a cross section $\sigma_{sk}$ |
| $\omega_{ce}$, $\Omega_{ce}$ | $\omega_{ce}$ | **collision:** registry $\Omega_e$ is the Hall parameter |
| $\tau_{ce}$ | $2\pi/\omega_{ce}$ | |
| $r_{ce}$ | $r_L$ (electron) | |
| $\lambda_D$, $\omega_{pe}$, $\omega_{pi}$ | same | the paper writes $\lambda_D$ with $K_BT_e$, $T_e$ in K |
| $\epsilon_0$, $K_B$ | $\varepsilon_0$, $k_B$ | |
| $v_{ez}$, $\langle v_{ez}\rangle$ | $u_{e,z}$ | mean electron axial velocity |
| $k$, $\lambda$, $\omega$ | $k$, $\lambda_w$, $\omega$ | plotted $k$ behaves as cycles per metre (see below) |
| $\hat f_k$, $p(\hat f_k)$, $S_{1D}$, $S_{2D}$, $N$ | words | Fourier coefficient, normalized mode power, spectral entropy, number of modes |
| $H_{1D}$, $H_{2D}$ | $H$ | normalized spectral entropy |

# Pages created or updated

Chunk 1 (2026-10-14) created every page of the bundle. This source is cited on:

* [Anomalous electron cross-field transport](/definitions/anomalous-electron-transport.md)
* [Electron drift instability (ECDI)](/definitions/electron-drift-instability.md)
* [Monte Carlo collisions and the null-collision method](/methods/monte-carlo-collisions.md)
* [Particle-in-cell with Monte Carlo collisions (PIC-MCC)](/methods/pic-mcc.md)
* [Permittivity, ion-mass and geometric scaling in PIC](/methods/pic-acceleration-scaling.md)
* [Resolution constraints of explicit PIC](/definitions/explicit-pic-resolution-constraints.md)
* [Spectral entropy of plasma oscillations](/methods/spectral-entropy.md)
* [SPT-100 as a validation case](/benchmarks/spt-100.md)

# Citations

1. `~/papers/mosaic/plasma-propulsion-simulation/2026_Crossref_Journal_of_Electric_Propulsion_Miranda_Spectral_entropy_of_plasma_oscillations_in_numerical_simulat.pdf`.
   * **Version.** Published version (Springer Nature open access, CC
     BY-NC-ND 4.0), 12 pages, running headers "(2026) 5:7". Received
     31 March 2025, accepted 25 January 2026. Sections are unnumbered; the
     numbering 2–5 used here follows the outline on p. 2.
   * **Identity.** doi:10.1007/s44205-026-00180-2, printed on p. 1 and
     checked on Crossref: J. Electr. Propuls. 5(1), article 7, online and
     issued 2026-02-12, no print date.
   * **How it was read.** Full text; Figs. 2–5 and 7 through text and
     captions only; Fig. 1a channel-radius labels illegible.
   * **Recorded as printed.**
     * §3, p. 8: "$\omega_{pe}\sim1.16\times10^9$ s⁻¹" for
       $n_e=1.65\times10^{16}$ m⁻³ is $\omega_{pe}/2\pi$; $\omega_{pe}$ is
       about $7.25\times10^9$ s⁻¹, so the stated bound
       $\Delta t<1.73\times10^{-10}$ s is too loose by $2\pi$ (about
       $2.76\times10^{-11}$ s); the chosen $10^{-11}$ s still satisfies it. The
       printed $\omega_{pi}=1.48\times10^7$ is consistent with the correct
       $\omega_{pe}$, so the two printed values are mutually inconsistent
       (reader's arithmetic).
     * §3, p. 9: $2\pi\sqrt2\,\lambda_D$ with the printed
       $\lambda_D=8.18\times10^{-5}$ m is $7.27\times10^{-4}$ m, not the
       printed $9.34\times10^{-4}$ m.
     * §3, p. 9: "$k\sim896$ m⁻¹, and $\lambda=1.1\times10^{-3}$ m" matches
       $\lambda_w=1/k$, so the plotted $k$ is in cycles per metre, against
       the $\exp(ikx)$ convention of eq. 5; likewise $k\sim100$ m⁻¹ for the
       0.01 m argon wave.
     * "$\omega=8.55\times10^6$ Hz" is an angular frequency in s⁻¹ labelled
       Hz (about 1.36 MHz).
     * p. 8: the power spectrum is taken "over the line z = 0.02 cm",
       almost certainly 0.02 m; the 1D entropy uses $z=0.025$ m (p. 9), and
       whether the two lines coincide is unclear.
     * §2.1, p. 4: "time step must be less than the cyclotron frequency"
       means the cyclotron period.
     * Eq. 2 uses $\sigma_N$ and the text $\sigma_n$; $\Omega_{ce}$ and
       $\omega_{ce}$ name the same quantity.
     * $\Delta x<3.4\lambda_D$ (p. 8, attributed) is looser than the usual
       $\Delta x$ of order $\lambda_D$; the implied axial spacing is about
       $1.9\lambda_D$ at the mean density (reader's note).
     * Ref. 30 (Janhunen et al.) printed 2017 with Phys. Plasmas
       25:011608, a 2018 volume; kept as printed.
   * **Reference list:** 37 printed entries; Crossref reference count 37.
     Rempel 2009 appears twice (refs. 9, 10): `rempel-2009`,
     `rempel-2009-b`.
