---
type: Source
title: "Ebrahimi & Bhattacharjee (2023) — Plasmoid-mediated reconnection during nonlinear peeling–ballooning edge-localized modes"
description: "NIMROD resistive and two-fluid MHD simulations of peeling–ballooning ELMs in two DIII-D equilibria showing a secondary nonlinear burst in which axisymmetric counter-current sheets suppress the edge peeling drive and finger-like edge current sheets break into plasmoids, the suppression being attributed to the fluctuation-induced emf."
resource: "doi:10.1088/1741-4326/ad0062"
source_kind: paper
authors: [Ebrahimi F., Bhattacharjee A.]
year: 2023
venue: "Nucl. Fusion 63:126042"
local_file: "/home/stefano/papers/mosaic/fusion-mhd-simulation/2023_Crossref_Nuclear_Fusion_Ebrahimi_Plasmoid-mediated_reconnection_during_nonlinear_peelingballo.pdf"
tags: [full-mhd, extended-mhd, tokamak, elm, pedestal, ballooning, edge, finite-elements, spectral]
timestamp: 2026-10-16T23:45:00Z
---

# Summary

A six-page letter (arXiv v1, single author; the published article adds
Bhattacharjee) reporting nonlinear [NIMROD](/software/nimrod.md) simulations
of peeling–ballooning (P-B) [edge-localized modes](/definitions/edge-localized-mode.md)
in two reconstructed DIII-D equilibria, with the computational domain
extending into the scrape-off layer (SOL). Case A (resistive MHD, Spitzer
resistivity from the toroidally averaged temperature, 43 toroidal harmonics):
intermediate-$n$ [ballooning](/definitions/ballooning-mode.md)-parity modes
($n=10$–14) grow linearly, the linearly stable low-$n$ peeling-parity modes
($n=1$–6) and the $n\ge20$ modes grow nonlinearly by mode coupling. After the
first saturation a secondary sharp exponential growth of several P-B modes
(the "reconnection burst") is followed by relaxation near $t=2$ ms and a
second burst near 2.4 ms. Two types of current sheet form: (1) a poloidally
extended axisymmetric ($n=0$) toroidal current sheet, generated through
Ampère's law by zonal poloidal fields that the P-B modes' own emf produces,
whose sign is opposite to the equilibrium edge current, so that it removes
the peeling drive; (2) finger-like non-axisymmetric sheets extending radially
in and out of the SOL, which break into small current blobs read as plasmoids.
A two-fluid run (Hall and electron-inertia Ohm's law, $S\sim5\times10^4$, 86
harmonics) shows poloidal flow vortices at about the poloidal Alfvén speed
(≈14 km/s). Case B (DIII-D 145701, uniform resistivity, $S\sim10^5$)
reproduces both sheet types and an $n=0$ counter-current, and the toroidally
averaged fluctuation-induced toroidal emf is bi-directional, consistent with
it. There is no convergence study, no Lundquist-number scan and no growth-rate
table: the evidence is energy traces and 2D cross sections of $j_\phi$,
pressure, field and flow.

# Key claims

Locations are pages and figures of arXiv v1.

1. **Three phases** (p. 2, Fig. 2). (i) Linear growth of intermediate-$n$
   ballooning modes with nonlinearly driven low-$n$ peeling modes;
   (ii) nonlinear saturation with a "secondary nonlinear surge of multiple
   P-B modes" and nonlinear generation of zonal fields and currents;
   (iii) relaxation as the P-B modes "nonlinearly suppress the edge current,
   as well as peeling it away". Shown (case A).
2. **Mode classes, case A** (p. 2, Fig. 2a). $n=10$–14 ballooning parity,
   linearly unstable; $n=1$–6 peeling parity, "linearly stable", nonlinearly
   driven; $n\ge20$ driven by mode–mode coupling. Shown by the energy traces;
   the linear stability of $n=1$–6 is Stated (no linear run reported).
3. **"Two ELM cycles"** within about 3 ms of simulated time (p. 2; Fig. 3c,
   second nonlinear growth at 2.4 ms). Shown. No heating, current drive or
   pedestal rebuild is described, so the second "cycle" is a second burst of
   the not-yet-exhausted drive, not an ELM–inter-ELM cycle in the sense of
   the [ELM page](/definitions/edge-localized-mode.md) (compiler's reading).
4. **Zonal fields** ($n=0$ $B_R$, $B_Z$) form and are amplified near
   $t=1.68$ ms; they are "nonlinear P-B mode structures that then become
   locally more coherent and zonal", produced by "the emf from the P-B modes
   themselves", and relax current and pressure near 2 ms (p. 2, Fig. 2c).
   Generation Shown; emf causation Stated for case A, supported in case B by
   the emf map (Fig. 6d).
5. **Type-1 current sheet** (p. 3, Figs. 3a, 4c). An axisymmetric toroidal
   current sheet driven by the zonal fields through
   $\mu_0j_\phi=\partial_ZB_R-\partial_RB_Z$, of sign opposite to the
   equilibrium edge current, "so it causes the suppression of the free energy
   (edge current) for the P-B modes"; on the low-field side it "is mainly
   broken by the P-B modes during the secondary growth". Shown; the
   suppression mechanism is Stated.
6. **Type-2 current sheets and plasmoids** (p. 3, Fig. 3a). "Finger-type
   non-axisymmetric current sheets radially and vertically extending inside
   and out of the SOL" that "further break and leave small-scale current
   blobs (plasmoids)". Shown qualitatively; the identification as
   reconnection-generated flux ropes rests on current-density snapshots alone
   (no island, flux or reconnection-rate diagnostic).
7. **Pressure fingers carry current** (p. 3, Fig. 3a). Shown (co-located
   pressure and $j_\phi$ fingers).
8. **Relaxation** (p. 3, Fig. 3b). The edge pressure broadens, the plasmoids
   decay and the current relaxes to "a mostly axisymmetric current density".
   Shown.
9. **Modal decomposition at 1.65 ms** (p. 4, Fig. 4). The nonlinear $n=12$
   current extends poloidally "much further away from its simple linear
   structure"; $n=1$ (and $n=2$) currents surround the device and dominate on
   the high-field side (peeling structure); the $n=0$ current opposes the
   background; together the modes "suppress the edge current as well as
   peeling away the edge current". Shown.
10. **Flow vortices** (p. 4, Fig. 5). Poloidal vortices form in MHD and are
    "further verified" in the two-fluid run; flows reach the poloidal Alfvén
    speed $\approx14$ km/s ($B_{\mathrm{pol}}\sim0.0065$ T,
    $n_i=5\times10^{19}$ m⁻³). Existence Shown; their origin (local
    reconnection versus Maxwell and Reynolds stresses) is left open:
    "further analysis is required".
11. **Second equilibrium** (case B, p. 4, Fig. 6). $n=1$ saturates "at large
    amplitude", higher-$n$ P-B modes much lower, the same two sheet types and
    an $n=0$ counter-current. Shown.
12. **Fluctuation-induced emf** (p. 4, Fig. 6d). The toroidal component of the
    toroidally averaged $\mathbf v\times\mathbf B$ of the non-axisymmetric
    fluctuations has a bi-directional poloidal cross-section, "consistent with
    formation of axisymmetric toroidal current density". Shown as a map; no
    quantitative balance against the $n=0$ current evolution.
13. **Lundquist-number dependence** (abstract). "At high Lundquist numbers,
    these current sheets break during a reconnection burst." Stated: the
    three runs differ in $S$ (Spitzer, $5\times10^4$, $10^5$) and in model, so
    no $S$ dependence is isolated.
14. **Self-organization** (p. 5). "The plasma edge goes through magnetic
    self-organization"; current and pressure relax, then grow again. Stated
    (interpretive framing of claims 3, 5, 8).
15. **Positioning and outlook** (pp. 1, 5). The work is presented as "full
    extended MHD" against nonlinear reduced-MHD ELM modelling (JOREK,
    Huysmans & Czarny 2007; Orain et al. 2015; Cathey et al. 2020), with no
    comparison; kinetic effects (ion gyroviscosity, gyrokinetics) are left to
    future work. Stated.

# Models and numerics

**Model** (p. 2, Eqs. 1–6, read on the rendered page), translated to the
registry (SI, $\eta$ the resistivity):

$$\begin{aligned}
\partial_t\mathbf B &= -\nabla\times\mathbf E + (\text{divergence-cleaning diffusion of }\nabla\cdot\mathbf B),\\
\mathbf E &= -\mathbf v\times\mathbf B+\eta\mathbf J+\frac{1}{n_ee}\mathbf J\times\mathbf B+\frac{m_e}{n_ee^2}\partial_t\mathbf J,\qquad \mu_0\mathbf J=\nabla\times\mathbf B,\\
\partial_tn_e+\nabla\cdot(n_e\mathbf v) &= \nabla\cdot(D\nabla n_e),\\
\rho(\partial_t\mathbf v+\mathbf v\cdot\nabla\mathbf v) &= \mathbf J\times\mathbf B-\nabla p+\rho\nu\nabla^2\mathbf v\quad(\text{or the rate-of-strain form}),\\
\frac{n_s}{\Gamma-1}(\partial_tT_s+\mathbf v_s\cdot\nabla T_s) &= -p_s\nabla\cdot\mathbf v_s+\nabla\cdot(n_s\mathsf K\cdot\nabla T_s)+Q_s,\qquad s=e,i,
\end{aligned}$$

with $\mathsf K=\chi_\parallel\mathbf b\mathbf b+\chi_\perp(\mathsf I-\mathbf b\mathbf b)$
(thermal diffusivities), $n_e=n_i$ (quasi-neutral; the paper writes $n$), $p_s=n_sT_s$, $Q_s$ a heat source, and $\mathbf v_s$ the
species velocity (not defined further; the registry has no species-velocity
symbol). As printed, Ohm's law has Hall and electron-inertia terms but no
electron-pressure term $-\nabla p_e/(n_ee)$. Case A is called "full MHD"; the
text implies Hall and inertia are switched on only in the two-fluid flow run
(ambiguous, see Citations). The two-temperature equations are called "an
anisotropic pressure model"; they carry anisotropic conduction, not a pressure
tensor.

**Closures.** Resistivity either Spitzer-like, $\propto T^{-3/2}$ evaluated from
the evolving toroidally averaged temperature (case A, said to correspond to a
"realistic" Lundquist number), or uniform ($S\sim5\times10^4$ in the
two-fluid run, $S\sim10^5$ in case B); the lengths in $S=\tau_R/\tau_A$ are
not stated. $\chi_\perp=25$ m²/s, $\chi_\parallel=2.5\times10^5$ m²/s.
Viscosity only through the unmagnetized part of the stress tensor, value not
given. Divergence-cleaning and density diffusivities: values not given.

**Discretization.** NIMROD: finite elements in the poloidal plane, finite
Fourier series toroidally. $40\times60$ elements of fifth- or sixth-order
polynomials, mesh extending past the separatrix into the SOL (Fig. 1d);
$n=0$–42 (43 harmonics, case A) or 86 harmonics (two-fluid run). Time
integration, solvers, boundary conditions, parallelism and cost are not
stated (computations at NERSC).

**Equilibria.** Reconstructions of ELMing DIII-D discharges: case A after
Brennan et al. (2006); case B discharge 145701 "at time 33 ms" from Liao et
al. (2016). Fig. 1 shows $q$, $\mu_0p$ and the normalized parallel current
against $\psi_N$; case A has a pronounced edge (bootstrap-like) current peak
near $\psi_N\approx0.9$ and edge $q\approx5$–6 (figure reading).

# Tests and results

No verification or benchmark; all results are figure-based (values are the
reader's colour-bar and axis readings).

| Run | Model | $\eta$ | Harmonics | Main results |
|---|---|---|---|---|
| Case A | resistive MHD (two temperatures) | Spitzer, from $T^{(0)}$ | 43 | linear phase to ≈1.5 ms; secondary burst peaking ≈1.6–1.7 ms ($n=1,12,11$ largest); relaxation ≈2 ms; second burst ≈2.3–2.6 ms |
| Two-fluid | + Hall, electron inertia | uniform, $S\sim5\times10^4$ | 86 | vortices, $v_R$ to $\pm6\times10^3$ m/s, $v_Z$ to $\pm8\times10^3$ m/s |
| Case B (DIII-D 145701) | resistive MHD | uniform, $S\sim10^5$ | not stated | time axis to $1.5\times10^{-4}$ s; $n=1$ saturates highest; $n=0$ counter-current |

* Case A at 1.68 ms: zonal $B_R\in[-5.7,6.6]\times10^{-3}$ T,
  $B_Z\in[-5.6,6.2]\times10^{-3}$ T; $j_\phi\in[-3.5,4.7]\times10^5$ A/m²;
  pressure perturbation $\pm1.7\times10^3$ Pa.
* Case A modal currents at 1.65 ms: $n=12$ ≈$\pm10^5$ A/m², $n=1$
  ≈$\pm1.2\times10^4$ A/m², $n=0$ ≈$\pm2\times10^5$ A/m², total down to
  $-1.3\times10^6$ A/m² (core).
* Case B at 0.11 ms: total $j_\phi$ ≈$\pm2.9\times10^5$ A/m², $n=0$
  ≈$\pm2\times10^5$ A/m²; emf map ≈$\pm6$–$8\times10^3$ V/m.
* The quoted $v_A$ on the poloidal field, $0.0065/\sqrt{\mu_0\cdot5\times10^{19}m_D}=1.42\times10^4$
  m/s, implies deuterium (hydrogen would give $2.0\times10^4$ m/s)
  (compiler's check).

# Notation map

| Ebrahimi (2021, arXiv v1) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf V$ | $\mathbf v$ | |
| $\mathbf V_\alpha$, $\alpha=e,i$ | $\mathbf v_s$ (words) | no registry species velocity |
| $J_\phi$ | $j_\phi$ | |
| $n$, $n_\alpha$ | $n_s$ | **collision:** the text also uses $n$ for the toroidal mode number |
| $p_\alpha=n_\alpha kT_\alpha$ | $p_s=n_sT_s$ | $T$ in kelvin as written; registry $T$ in energy units |
| $\kappa_\parallel$, $\kappa_\perp$ | $\chi_\parallel$, $\chi_\perp$ | diffusivities (m²/s), density factored out |
| $\mathbf q_\alpha$, $Q_\alpha$ | words (heat flux), $Q_s$ heat source | |
| $\eta$ | $\eta/\mu_0$ | **collision:** native $\eta$ is a magnetic diffusivity (m²/s); registry $\eta=\mu_0\eta_{\mathrm{native}}$ |
| $\kappa_{divb}$ | words (divergence-cleaning diffusivity) | NIMROD-specific |
| $D$ | $D_\parallel=D_\perp=D$ | isotropic |
| $\Pi$, $W$ | $\mathsf\Pi$ (viscous stress), words (rate-of-strain tensor) | |
| $\nu$ | $\nu$ | kinematic |
| $\hat{\mathbf b}$, $\mathsf I$ | $\mathbf b$, $\mathsf I$ | |
| $\psi$ (Fig. 1) | $\psi_N$ | 0 to 1 |
| $\langle\mathbf J\cdot\mathbf B\rangle/B^2$ | $\langle j_\parallel B\rangle/B^2$ | bracket not defined in the paper |
| $r$, $z$ / $R$, $Z$; $B_r$, $B_z$ | $R$, $Z$; $B_R$, $B_Z$ | the paper mixes lower and upper case; **collision risk:** registry $r$ is the minor radius |
| $\langle\cdot\rangle_{n=0}$, $\langle\cdot\rangle_\phi$ | $f^{(0)}$ (toroidal average) | **collision risk:** registry $\langle\cdot\rangle$ is a flux-surface or gyroaverage |
| $\tilde{\mathbf J}_{n\neq0}$, $\tilde V$, $\tilde B$ | $\tilde{\mathbf J}$, $\tilde{\mathbf v}$, $\tilde{\mathbf B}$ (non-axisymmetric part) | registry $\delta(\cdot)$ is a linear perturbation |
| $\tfrac12\mathrm{Re}[\tilde V_r\tilde B_z^*-\tilde V_z\tilde B_r^*]$ | $(\tilde{\mathbf v}\times\tilde{\mathbf B})^{(0)}\cdot\mathbf e_\phi$ (toroidal mean emf) | toroidal, not the parallel $E_{\mathrm{dyn},\parallel}$; sign convention, see Citations |
| $V_{A(pol)}$, $B_p$ | words ($v_A$ on the poloidal field) | |
| $S=\tau_R/\tau_A$ | $S$ | lengths unstated |

# Pages created or updated

Chunk 2 (2026-10-16) created or updated the pages below; chunk 3 extended some. This source is cited on:

* [Ballooning mode](/definitions/ballooning-mode.md)
* [Bézier–Hermite finite elements with toroidal Fourier harmonics](/methods/bezier-finite-elements.md)
* [Divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
* [Edge-localized mode (ELM) and ELM-free regimes](/definitions/edge-localized-mode.md)
* [MHD dynamo effect](/definitions/mhd-dynamo.md)
* [NIMROD](/software/nimrod.md)
* [Plasmoid instability and plasmoid-mediated reconnection](/definitions/plasmoid-instability.md)
* [Single-fluid visco-resistive MHD model](/methods/visco-resistive-mhd-model.md)

# Citations

1. `/home/stefano/papers/mosaic/fusion-mhd-simulation/2023_Crossref_Nuclear_Fusion_Ebrahimi_Plasmoid-mediated_reconnection_during_nonlinear_peelingballo.pdf`
   * **Version.** arXiv:2110.09706v1 [physics.plasm-ph], 19 October 2021
     (dated 20 October 2021), REVTeX letter, 6 pages; not the published
     version. The file name says "Crossref Nuclear Fusion", but the content
     is the preprint. **The arXiv v1 lists a single author, Ebrahimi F.**
     (PPPL and Princeton); Bhattacharjee is only acknowledged. The published
     article lists Ebrahimi F. and Bhattacharjee A.; its text, figures and
     numbers (two years of revision later) were not checked. All locations
     are arXiv v1 pages.
   * **Identity.** doi:10.1088/1741-4326/ad0062, checked on Crossref: title
     (with an en dash in "peeling–ballooning"), authors Ebrahimi,
     Bhattacharjee, Nucl. Fusion 63(12), article 126042, issued 2023-10-25.
     The frontmatter carries the published identity.
   * **How read.** Full text; Eqs. 1–6 read on the rendered page (the
     equation numbers overprint the right-hand sides, content legible); all
     six figures inspected. Figure values are approximate readings.
   * **Recorded as printed.**
     * "As shown in Fig. 1 (b) at around t = 2 ms" (p. 3): Fig. 1(b) is the
       equilibrium pressure; Fig. 2(b) is meant.
     * Fig. 3(a) caption "at t = 1.65 ms" against the panel title
       "t=1.68ms"; the text puts the zonal fields at 1.68 ms and Fig. 4 at
       1.65 ms.
     * "Anisotropic pressure model" (p. 2): Eq. 6 has scalar temperatures
       with anisotropic conduction, no pressure anisotropy.
     * Ohm's law (Eq. 2) lacks the electron-pressure term a two-fluid Ohm's
       law normally carries; whether case A used Eq. 2 in full is ambiguous
       ("evolving the set of equations (1-6)", p. 2, against "further
       verified in the 2-fluid regime … by including the generalized Ohm's
       law (Eq. 2)", p. 4).
     * $\mu_0J_\phi=\partial B_r/\partial z-\partial B_z/\partial r$ is the
       $\phi$ component of the curl in right-handed $(R,\phi,Z)$, while the
       emf $\tilde V_r\tilde B_z-\tilde V_z\tilde B_r$ is the $\phi$ component
       of $\tilde{\mathbf V}\times\tilde{\mathbf B}$ in the cyclic order
       $(R,Z,\phi)$, i.e. the opposite orientation; the paper states neither.
       The sign of the emf is not usable quantitatively (compiler's check).
     * "DIII-D discharge 145701 at time 33 ms" (p. 2): an unusually early time
       for an ELMing H-mode; possibly a misprint, unverified.
     * The text gives ballooning modes $n=10$–14, while the Fig. 2 legend
       groups $n=8,13,15$ with $n=1,12,11$.
     * The abstract's "at high Lundquist numbers" is not supported by an
       $S$ scan; case B evolves about 20 times faster than case A (0.15 ms
       against about 3 ms), not discussed.
     * The two-fluid run's equilibrium is implied to be case A, not stated.
     * Fig. 5 caption "(a) radial (b) axial" for panels $V_r$, $V_z$;
       Fig. 6(d) "poloidal cross section of EMF" is the toroidal emf
       component in the poloidal plane.
     * Typos: "Lunquist" (p. 2), "the the" (p. 4), "axisymetic",
       "non-axisymmetic" (pp. 3–5).
   * **Reference list.** 50 printed entries ([1]–[50], APS style, no titles),
     merged into the bibliography under `ebrahimi-2023` (50 entries). Coppi
     et al. printed "Sov. J. Plasma Phys 2, 19 (1976)" is the existing
     `coppi-1976` (the Russian original, Fiz. Plazmy 2:961). Tajima &
     Shibata (ref. 28) are editors, entered as a book. Ref. 47 prints
     "Phy. Rev. Lett.". Ref. 49, M. Kim et al., Nucl. Fusion 60:126021
     (2020), the whistler-frequency ELM emission paper, is a different
     work from `kim-2020` (S.K. Kim et al., Nucl. Fusion 60:026009, KSTAR
     RMP); it is keyed `kim-2020-d`.
