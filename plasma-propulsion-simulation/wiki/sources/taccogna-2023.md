---
type: Source
title: "Taccogna et al. (2023) — Plasma propulsion modeling with particle-based algorithms"
description: "Perspective review of particle-based (PIC-MCC, DSMC, hybrid) modelling of electrostatic and electromagnetic thrusters: the explicit PIC cycle and its constraints, plasma-wall and gas-wall models, plume models, and the cost-reduction routes (HPC and GPU, sparse-grid, implicit and energy-conserving, reduced-order PIC, machine learning); all results are attributed to earlier work."
resource: "doi:10.1063/5.0153862"
source_kind: paper
authors: [Taccogna F., Cichocki F., Eremin D., Fubiani G., Garrigues L.]
year: 2023
venue: "J. Appl. Phys. 134:150901"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2023_Crossref_Journal_of_Applied_Physics_Taccogna_Plasma_propulsion_modeling_with_particle-based_algorithms.pdf"
tags: [review, pic, mcc, dsmc, hybrid, kinetic, hall-thruster, ion-thruster, helicon, plume, wall-interaction, numerics, gpu]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

A "perspective" review of particle simulation of electric thrusters. It
sorts thrusters by modelling need: electrostatic ones (pulsed-arc,
electrospray, gridded ion, $\mathbf E\times\mathbf B$/Hall) need only
Poisson's equation; electromagnetic ones (inductive/RF, microwave ECR,
helicon) need Maxwell's equations or a subset (§I). It sets out the explicit
PIC-MCC cycle and its numerical constraints (§II), electrostatic and
electromagnetic thruster applications (§III A–B), plasma–wall and gas–wall
interaction models (§III C), plume models — hybrid with polytropic or
heat-flux electron closures against full PIC — with plume boundary
conditions, spacecraft charging and electromagnetic compatibility (§IV),
and "future challenges": collision data for alternative and molecular
propellants, PIC-MCC coupled to test-particle Monte Carlo neutrals, HPC
(MPI, OpenMP, GPU), sparse-grid, implicit and energy-conserving, and
reduced-order PIC, and deep-learning solvers and closures (§V). The paper
shows no new simulation: every figure is reproduced or adapted from earlier
work, and every quantitative claim is attributed. The manuscript title is
"Plasma propulsion simulation using particles". Merged into
[PIC-MCC](/methods/pic-mcc.md),
[Monte Carlo collisions](/methods/monte-carlo-collisions.md),
[resolution constraints of explicit PIC](/definitions/explicit-pic-resolution-constraints.md),
[permittivity, ion-mass and geometric scaling](/methods/pic-acceleration-scaling.md)
and [particle pushers](/methods/particle-pushers.md), among others listed
below.

# Key claims

All claims are stated or attributed (review); none is proved here.

1. **Macroparticle representation and deposition** (§II, Eqs. 1, 5,
   Fig. 1). $f(\mathbf r,\mathbf v)=\sum_p w_pS(\mathbf r-\mathbf r_p)\delta(\mathbf v-\mathbf v_p)$
   with $\int S=1$; the assignment function is $S$ convolved with a top-hat
   of mesh width; charge and current densities are weighted sums divided by
   the cell volume. Push by Newton–Lorentz (Eq. 2), leapfrog "the most
   diffuse".
2. **Collision step** (§II, Eq. 4). $f(t+\Delta t)=(1-P)f(t)+PQ$, by "the
   Nanbu (no-time counter) stochastic Monte Carlo rules". MCC uses a fluid
   background target; DSMC pairs macroparticles.
3. **Explicit-PIC constraints** (§II, §III A). $\omega_{pe}\Delta t<2$ or
   $c\le\Delta r/\Delta t$ for explicit EM codes; $\Delta r\le\zeta\lambda_{D,e}$
   with $\zeta$ of order 1; collision probability below 5–10 % for under
   1 % error; in electrostatic PIC the CFL condition is set by the
   electrons.
4. **Cost** (§III A, §V B a). Pulsed-arc thruster at $10^{22}$ m$^{-3}$,
   $T_e\approx10$ eV: $\lambda_{D,e}$ of order $10^{-7}$ m, $\Delta t$ of
   order $10^{-13}$ s, about $10^8$ steps. Other electrostatic thrusters at
   about $10^{18}$ m$^{-3}$: $\lambda_{D,e}$ of order $10^{-5}$ m, $\Delta t$
   of order $10^{-11}$ s, about $10^7$ steps. A 3D SPT-100 channel
   ($\lambda_D\approx20$ µm) needs about 10 billion cells, "hundreds of
   billions of particles" and about 10 TB.
5. **Acceleration tricks** (§III A). Enlarged vacuum permittivity, reduced
   ion mass and size scaling are "still used in many simulations"; no
   validity limits are given; for EM thrusters "the physics might not be
   entirely equivalent". Fixed neutral backgrounds have "shown limited
   conclusions".
6. **Dielectric boundary** (§III A, Eqs. 7–8): capacitor-like surface
   condition $\nabla\phi\cdot\mathbf 1_n=-\sigma_c/\varepsilon_0$ or a
   generalized Poisson equation through the dielectric.
7. **ECDI and MTSI** (§III A d, Figs. 3–4). ECDI with mm wavelength and MHz
   frequency; MTSI in 2D radial–azimuthal runs; 3D ECDI amplitude "typically
   one order of magnitude smaller than in 2D". The LANDMARK axial–azimuthal
   (Charoy et al.) and radial–azimuthal (Villafana et al.) benchmarks were
   reproduced by seven groups.
8. **Electromagnetic PIC** (§III B, Eqs. 9–14). Field split
   $\mathbf E=-\nabla\phi-\partial\mathbf A/\partial t$; frequency-domain
   Helmholtz solve updated about once per RF period, excluding nonlinear
   effects; explicit EM CFL "typically intractable".
9. **Plasma–wall interaction** (§III C). SEE models are phenomenological;
   electron-emission yield data lack below 30 eV; integrated ion wall flux
   up to 40 % of ion production in unshielded configurations; recombination
   probability 7 % (N) and 17 % (O); emitted energy
   $\langle E_{emi}\rangle=(1-\alpha_w)E_{imp}+2\alpha_wT_w$ (Eq. 15).
10. **Gas–wall interaction** (§III C d, Fig. 8). Maxwell and Schamberg
    reflection; purely diffuse reflection overestimates neutral residence
    time; reversed injection raises propellant utilization by at most 30 %.
11. **Plume hybrids** (§IV A, Eq. 16). Isothermal asymptotic potential
    $-\infty$, polytropic $-\gamma T_{e0}/[e(\gamma-1)]$; a convective heat
    flux $\mathbf q_e=\alpha n_eT_e\mathbf u_e$ is equivalent to
    $\gamma=(5+2\alpha)/(3+2\alpha)$; non-neutral regions raise ion
    backflow by about 20 %; full PIC shows anisotropic cooling
    ($\gamma_\parallel\to1$, $\gamma_\perp$ reaching and passing 2).
12. **Plume PIC set-up** (§IV B, Eq. 17). Ion Mach number 10–30;
    half-Maxwellian-flux electron injection; open-boundary electrons
    removed or selectively reflected.
13. **HPC** (§V B). MPI domain decomposition, speed-up of order 1000;
    OpenMP races handled by reductions or atomics; GPU PIC by sorting or by
    atomic adds; ECCOPIC2S-M (CUDA) ran the axial–azimuthal benchmark at
    the explicit codes' $\Delta t$ and $\Delta x$, so its GPU benefit showed
    only in the radial–azimuthal benchmark.
14. **Sparse-grid PIC** (§V C a, Fig. 18). Cells from $O(N^d)$ to
    $O(N(\log N)^{d-1})$; ECDI on $512\times512$ cells, 400 per cell,
    $10^8$ against $5.2\times10^6$ particles, gain 6.5 "with a certain
    error".
15. **Implicit PIC** (§V C b). Direct-implicit and implicit-moment schemes
    suffer finite-grid heating or cooling; the explicit finite-grid
    instability triggers when $\Delta x$ exceeds $\lambda_D$; an implicit
    moment scheme with matched assignment and interpolation and
    $\theta=0.5$ conserves energy exactly (ECPIC), with finite-grid
    instability only when the electron drift exceeds the thermal velocity,
    "never conducted for magnetized plasmas".
16. **Reduced-order PIC** (§V C c, Eq. 21, Fig. 19).
    $\phi(x,y)=\chi(x)+\eta(y)$ per region; speed-up up to 50 relative to
    2D, about 2500 expected for quasi-3D.
17. **ML closure** (§V D, Eq. 22). Fitted anomalous collision frequency
    $\nu_{ano}\propto\omega_{c,e}(u_i/v_{d,e})^2$ (Jorns).

# Models and numerics

None of its own. The review surveys: kinetic Boltzmann equations by
macroparticles (Eq. 1); fields from Poisson (Eq. 6), generalized Poisson
(Eq. 8), Faraday–Ampère (Eqs. 10–11) or Helmholtz (Eqs. 12–14) on FD/FV
grids, sometimes AMR, with PARDISO, MUMPS or PETSc; MCC and DSMC after
Nanbu, cross sections from IAEA, LXCat, Quantemol, NIST, NIFS (the
null-collision method is not named); hybrid variants with Boltzmann
electrons (gridded ion engines), fluid electrons (Hall, helicon) and
polytropic or heat-flux plume closures; SEE models from linear to
Furman–Pivi and machine-learned; Maxwell and Schamberg neutral reflection.
Particle weights uniform per species; 400 per cell in Fig. 18, no other
value. Codes named: ECCOPIC / ECCOPIC2S-M, LTP-PIC, EDIPIC, LSP, Warp,
VORPAL, CHAOS, JET2D, 3D-VIRTUS, edupic, MICHELLE, pdFOAM, Ansys HFSS.

# Tests and results

No new simulation or experiment. Reproduced figures, each attributed:
Fig. 2 (3D hybrid beamlet extraction, Perales-Díaz et al.); Fig. 3
(axial–azimuthal ECDI, $E_y$ within ±5×10⁴ V/m, $n_i$ up to 5×10¹⁷ m⁻³,
Boeuf & Garrigues); Fig. 4 (radial–azimuthal benchmark, seven codes,
Villafana et al.); Fig. 5 (µ10 ECR thruster, Yamashita et al.); Fig. 6
(electron-emission yield, first crossover Al₂O₃ 22 eV, BN/SiO₂ 40 eV,
BN 45 eV, Tondu et al.); Fig. 7 (backscattering lobes, Villemant et al.);
Fig. 8 (neutral reflection models, Domínguez-Vázquez et al.); Fig. 9
(hybrid plume around a cubesat, $\gamma=1.1$, Cichocki et al.); Figs. 10–11
(full-PIC plume cooling, Wang & Hu); Fig. 12 (plume potential versus domain
size, Li et al.); Fig. 13 (DAWN plume, $\gamma=1.3$, Araki); Fig. 14
(antenna pattern with plasma, 436 MHz, De Mejanes et al.); Fig. 15
(PIC-MCC/TPMC coupling); Fig. 16 (ionization cost per species); Fig. 17
(Xe rate coefficients with metastables); Fig. 18 (sparse-grid ECDI,
Garrigues et al.); Fig. 19 (reduced-order decomposition, Faraji et al.).

# Notation map

| Taccogna et al. (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf r$, $\mathbf r_p$, $\mathbf v_p$ | $\mathbf x$, $\mathbf x_p$, $\mathbf v_p$ | |
| $f(\mathbf r,\mathbf v)$ | $f_s(\mathbf x,\mathbf v,t)$ | |
| $w_p$ | $W$ (per particle, $W_p$) | statistical weight |
| $W(\mathbf r)$ (assignment function) | words | **collision:** registry $W$ is the macroparticle weight |
| $W$, $W_s$ (ionization cost, Eqs. 19–20) | words | **collision** with $W$ |
| $S(\mathbf r)$ | $S(\mathbf x)$ | cloud shape |
| $\Delta r$ | $\Delta x$ | **collision:** $r$ is the radial coordinate |
| $\omega_{p,e}$, $\lambda_{D,e}$ | $\omega_{pe}$, $\lambda_D$ | |
| $\zeta$ | words ("a constant of order 1") | |
| $P$ (collision probability) | $P_c$ | **collision:** registry $P$ is electric power |
| $c$ | words (speed of light) | **collision risk** with $c_s$ |
| $v_e$ (ES CFL) | words (fastest electron speed) | not defined precisely |
| $\sigma_c$ (surface charge) | words | **collision:** $\sigma_{sk}$ is a cross section |
| $\sigma(E_p,\theta_p)$ (emission yield) | $\delta_{\mathrm{SEE}}$ | **collision:** $\sigma$ and $\theta$ |
| $\alpha_w$, $\alpha_W$ | $\alpha_E$ | energy accommodation; printed both ways |
| $\eta_m$ | $\eta_m$ | propellant utilization |
| $\gamma$, $\gamma_\parallel$, $\gamma_\perp$ | $\gamma$ | polytropic index |
| $\alpha$ (heat-flux coefficient, §IV A) | words | page-local |
| $\omega_{c,e}$ | $\omega_{ce}$ | |
| $\nu_{ano}$ | $\nu_{\mathrm{ano}}$ | |
| $v_{d,e}$, $u_i$ | words ($\mathbf E\times\mathbf B$ drift speed; ion speed, magnitude of $\mathbf u_i$) | |
| $\chi(x)$, $\eta(y)$ | words | **collision:** $\eta$ is thrust efficiency |
| $\theta$ (implicit mixing parameter) | words | **collision:** azimuthal $\theta$ |

# Pages created or updated

Chunk 1 (2026-10-14) created every page of the bundle. This source is cited on:

* [Anomalous electron cross-field transport](/definitions/anomalous-electron-transport.md)
* [Axial–azimuthal Hall-thruster PIC benchmark (Charoy et al. 2019)](/benchmarks/axial-azimuthal-pic-benchmark.md)
* [Boltzmann-relation electrons](/methods/boltzmann-electron-model.md)
* [Charge-exchange ions](/definitions/charge-exchange-ions.md)
* [Direct simulation Monte Carlo (DSMC)](/methods/dsmc.md)
* [Electron drift instability (ECDI)](/definitions/electron-drift-instability.md)
* [Gas–surface interaction models](/methods/gas-surface-interaction.md)
* [GPU acceleration of particle codes](/methods/gpu-acceleration-of-pic.md)
* [Helicon plasma thruster](/definitions/helicon-plasma-thruster.md)
* [Hybrid PIC–fluid models](/methods/hybrid-pic-fluid-model.md)
* [Magnetic shielding](/definitions/magnetic-shielding.md)
* [Monte Carlo collisions and the null-collision method](/methods/monte-carlo-collisions.md)
* [Particle pushers: leapfrog, Boris and Runge–Kutta](/methods/particle-pushers.md)
* [Particle-in-cell with Monte Carlo collisions (PIC-MCC)](/methods/pic-mcc.md)
* [Permittivity, ion-mass and geometric scaling in PIC](/methods/pic-acceleration-scaling.md)
* [Polytropic electron closure and plume cooling](/definitions/polytropic-electron-closure.md)
* [Pulsed plasma thruster](/definitions/pulsed-plasma-thruster.md)
* [Reduced-order (pseudo-2D) PIC](/methods/reduced-order-pic.md)
* [Resolution constraints of explicit PIC](/definitions/explicit-pic-resolution-constraints.md)
* [Rotating spoke](/definitions/rotating-spoke.md)
* [Secondary electron emission and sheath regimes](/definitions/secondary-electron-emission.md)
* [Semi-implicit, implicit and energy-conserving PIC](/methods/implicit-and-energy-conserving-pic.md)
* [SPT-100 as a validation case](/benchmarks/spt-100.md)

# Citations

1. `~/papers/mosaic/plasma-propulsion-simulation/2023_Crossref_Journal_of_Applied_Physics_Taccogna_Plasma_propulsion_modeling_with_particle-based_algorithms.pdf`.
   * **Version.** Accepted manuscript (AIP author-manuscript layout, 35 pp.,
     "Dated: 20 October 2023"), not the typeset version of record. The
     manuscript title is "Plasma propulsion simulation using particles"; the
     published title (Crossref) is used here. The manuscript prints no DOI.
   * **Identity.** doi:10.1063/5.0153862, found by title search and checked
     on Crossref (title, five authors in order): J. Appl. Phys. 134(15),
     article 150901; issue 2023-10-21, online 2023-10-19.
   * **How it was read.** Text extraction, all sections; Eqs. 6, 12–13, 16,
     21 and 22 checked on rendered pages 3, 4, 8, 15 and 24. Page 12 carries
     invisible overlapping text from a reproduced article page in its text
     layer; it was ignored. The Fig. 13 colour-bar units are not printed
     (m⁻³ implied).
   * **Recorded as printed.** §III B states the CFL restriction as
     "$\Delta r>\min(c\Delta t,\lambda_{D,e})$", which contradicts the
     separate §II conditions $c\le\Delta r/\Delta t$ and
     $\Delta r\le\zeta\lambda_{D,e}$; the §II form is used on concept pages.
     Eq. 16 labels its second branch "for $\gamma\ge1$", singular at
     $\gamma=1$; the text uses $\gamma>1$. $\omega_{pe}\Delta t<2$ is
     attributed to EM codes in §II and applied to ES codes in §III A. The
     parenthesis "Nanbu (no-time counter)" (§II) pairs Nanbu's scheme with
     the name of Bird's DSMC scheme; it is reproduced as printed, not
     resolved. Broken cross-references "Sec. V C 0 b" (§III B) and an
     unresolved citation "algorithms have also been developed? ." (§V C b).
     The accommodation coefficient is printed $\alpha_w$ (Eq. 15) and
     $\alpha_W$ (§III C d). Reference list: refs. 23 and 172, and refs. 136
     and 192, are the same works; ref. 127 repeats ref. 125's journal,
     volume and page with year 2023; refs. 24 and 281 print ISSN-like page
     ranges; ref. 26 prints a truncated article number; ref. 50 prints the
     "49th" Joint Propulsion Conference with year 1993; ref. 258 (Ansys
     HFSS) carries the LANDMARK title; ref. 20 gives "Department of French"
     for a physics thesis. Checked consistent: $\lambda_D\approx23$ µm at
     $10^{18}$ m$^{-3}$ and 10 eV against "≈20 µm"; $512^2\times400\approx1.05\times10^8$
     against $10^8$ particles.
   * **Reference list:** 344 printed entries (Crossref counts 391 for the
     version of record). Duplicate printed works: `emoto-2023-b` = `emoto-2023`,
     `sydorenko-2006-b` = `sydorenko-2006`. Organization keys:
     `landmark-2017`, `ansys-2022`, `iaea-2023`, `lxcat-2023`,
     `quantemol-2023`, `nist-2023`, `nifs-2023`.
