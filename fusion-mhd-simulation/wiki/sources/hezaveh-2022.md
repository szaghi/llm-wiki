---
type: Source
title: "Hezaveh et al. (2022) — Simulation of convective transport during frequency chirping of a TAE using the MEGA code"
description: "MEGA hybrid simulation of a chirping n = 6 TAE analysed with action-angle variables in a frame co-moving with the chirping wave, giving a momentum conserved during chirping; holes and clumps carry the same resonant particles (convective bucket transport), and chirping speeds up when dissipation is increased, consistent with Berk–Breizman theory."
resource: "doi:10.1088/1741-4326/ac49ab"
source_kind: paper
authors: [Hezaveh H., Todo Y., Qu Z.S., Breizman B.N., Hole M.J.]
year: 2022
venue: "Nucl. Fusion 62:036025"
local_file: "/home/stefano/papers/mosaic/fusion-mhd-simulation/2022_Crossref_Nuclear_Fusion_Hezaveh_Simulation_of_convective_transport_during_frequency_chirping.pdf"
tags: [mhd, hybrid-kinetic, energetic-particles, alfven-eigenmode, particles, tokamak, finite-differences]
timestamp: 2026-10-16T16:51:00Z
---

# Summary

The paper proposes a phase-space diagnostic for long-range frequency chirping
of energetic-particle (EP) driven Alfvén modes and applies it to
[MEGA](/software/mega.md) simulations of an $n=6$
[TAE](/definitions/toroidal-alfven-eigenmode.md). Starting from Littlejohn's
guiding-centre Lagrangian in the canonical straight-field-line coordinates of
Li, Breizman and Zheng (2016), the unperturbed motion is written in
action-angle variables; a type-2 generating function to a frame co-moving with
a single chirping (BGK-type) wave gives a wave-frame momentum, its conjugate
wave angle, and a second momentum that stays an exact constant of motion
**even while the frequency chirps**, unlike the invariant
$\omega P_\phi-n\mathcal E$ used by White et al. (2020), which assumes a fixed
frequency. The poloidal action is obtained numerically for $\mu=0$ particles
by a least-squares polynomial fit to orbit frequencies traced in the
equilibrium. MEGA (nonlinear visco-resistive MHD plus drift-kinetic $\delta f$
EPs, current coupling, finite differences) runs a circular, uniform-density
case with $q$ linear from 1 to 1.3 and an isotropic slowing-down EP population
at $\beta_h=0.6\%$ on axis; the TAE has $\omega/\omega_A=0.4553$,
$\gamma_l/\omega=2.64\%$, $\gamma_d/\gamma_l=0.44$. After saturation up- and
down-chirping branches form; raising viscosity and resistivity 20× and then
40× mid-run makes the chirp faster, read as confirmation of Berk–Breizman
(BB) dissipation-controlled chirping. Poincaré-like plots on a slice of the
conserved momentum, with markers colour-labelled by their initial wave-frame
momentum, show holes and clumps that carry the same particles (a moving
phase-space "bucket"), i.e. convective radial transport; the structures
survive after the frequencies enter the shear-Alfvén continuum. No code
comparison and no convergence study are reported.

# Key claims

Locations are sections of arXiv v1.

1. **Conserved momentum during chirping** (§3, Eqs. 15–17; §4.3–4.4,
   Figs. 8–10). The wave-frame momentum $\mathcal P_2$ (Models) is an exact
   constant of motion of a single chirping wave, so particles stay on fixed
   $\mathcal P_2$ sub-layers through linear growth and long-range chirping.
   Derived (single-resonance Hamiltonian) and Shown for one tracked particle
   ($\Delta\mathcal P_2\approx0$ while $\Delta P_\phi\approx-6$, normalized
   units).
2. **The White invariant drifts** (§4.4, Fig. 10). For the same particle
   $\Delta(\omega P_\phi-n\mathcal E)/\omega$ grows to about +0.8; "slices of
   C = const do not represent the most appropriate sub-layers" during
   long-range chirping. Shown (one particle). A methodological disagreement
   with White et al. (2020), valid beyond the fixed-frequency assumption.
3. **Linear TAE** (§4.1, Figs. 2a, 3). $n=6$, dominant $m=6,7$, just above the
   lower tip of the first gap; $\omega/\omega_A=0.4553$; net growth
   $(\gamma_l-|\gamma_d|)/\omega_A=0.0067$; damping from the $\beta_h$-scan
   intercept $\gamma_d/\omega_A=0.0053$; drive $\gamma_l/\omega_A=0.012$;
   $\gamma_d/\gamma_l=0.44$; $\gamma_l/\omega=2.64\%$. Shown (the four numbers
   are mutually consistent, compiler's check).
4. **Linear in $\beta_h$** (Fig. 3a). The net growth is linear in $\beta_h$
   over six points, 0.004–0.009. Shown.
5. **Branch formation** (§4.1, Figs. 2b, 4b, 5b). After saturation sidebands
   form in the gap and evolve into primary up- and down-chirping branches plus
   secondary branches. Shown.
6. **Dissipation speeds up chirping** (§4.1, Figs. 2 vs 4). "The rate of
   frequency chirping increases with the TAE damping rate": with $\nu=\eta$
   raised from $0.3\times10^{-7}$ to $6\times10^{-7}$ (at $t/\tau_A=1119.1$)
   and $1.2\times10^{-6}$ $v_AR_0$ (at 1243.4) the chirp is faster and the
   amplitude lower. Shown qualitatively (two spectrograms; no chirp-rate
   number; $\gamma_d$ after the change not measured); stated as consistent
   with BB theory's balance between the power extracted from the EPs and the
   power dissipated.
7. **Dissipation as a probe** (§4.1). Raising dissipation in the nonlinear
   phase is proposed as "a useful probing tool for nonlinear simulations" that
   "can also save computational resources". Stated.
8. **BB early-chirp law** (Eq. 24, from Berk et al. 1997).
   $\delta\omega/\gamma_l=\tfrac{16\sqrt2}{3\sqrt3\pi^2}(\gamma_dt)^{1/2}\approx0.44(\gamma_dt)^{1/2}$.
   Attributed; not compared with the simulation.
9. **Entry into the continuum** (§4.1, Fig. 5c–d; §5). Chirping frequencies
   move to the gap tips, excite continuum waves, then enter the shear-Alfvén
   continuum with radius-dependent frequencies, "consistent with the
   theoretical model of Ref. [19]" (Wang, Berk, Breizman, Zheng 2018). Shown
   (spectra); agreement Stated.
10. **Resonance** (§4.2, Eq. 25, Fig. 6). Co-passing resonance
    $\omega=n\omega_\phi+\ell\omega_\theta$ with $n=6$, $\ell=-6$ ($\ell=-m$;
    counter-passing would be $-(m+1)$); the $\delta f$ weights localize on the
    resonance line in the $(\mathcal E,P_\phi)$ and frequency planes. Shown.
11. **Convective bucket transport** (§4.4, Fig. 9). Holes (down-chirp) and
    clumps (up-chirp) form on either side of the flattened region and move;
    the colour labels show that resonant particles "are not being locally
    perturbed and then left behind. Rather, the BGK-type chirping wave carries
    the EPs in a moving phase-space bucket in a convective way". At
    $t/\tau_A=2477.8$ the branches have swept +13.55% and −11.33%. Shown.
12. **Second set of holes** (§4.4, Fig. 9g) detaches, attributed to the
    second down-chirping branch of Fig. 4b. Shown; interpretation.
13. **Survival in the continuum** (§5). Holes and clumps formed in the gap
    "survive even in the shear Alfvén continuum". Shown (Figs. 9g–j, 5d) as an
    interpretation.
14. **Action structure** (§4.3, Fig. 7). For $\mu=0$, $|\mathcal P_\theta|$ is
    proportional to $P_\phi$ at fixed $\mathcal E$ and inversely related to
    $\mathcal E$ at fixed $P_\phi$. Shown.
15. **No $\mathbf E\times\mathbf B$ drift in the EP current** "due to
    quasi-neutrality" (§2). Attributed (Todo & Sato 1998).

# Models and numerics

**MEGA** (§2, Eqs. 1–6), in registry notation (subscript 0 = equilibrium;
the 0-terms keep the equilibrium against dissipation):

$$\begin{aligned}
\rho\partial_t\mathbf v &= -\rho\mathbf v\cdot\nabla\mathbf v-\nabla p+(\mu_0^{-1}\nabla\times\mathbf B-\mathbf J_h)\times\mathbf B+\tfrac43\nabla(\nu\rho\nabla\cdot\mathbf v)-\nabla\times(\nu\rho\nabla\times\mathbf v),\\
\partial_t\rho &= -\nabla\cdot(\rho\mathbf v)+D\Delta(\rho-\rho_0),\\
\partial_tp &= -\nabla\cdot(p\mathbf v)-(\Gamma-1)p\nabla\cdot\mathbf v+(\Gamma-1)\big[\nu\rho(\nabla\times\mathbf v)^2+\tfrac43\nu\rho(\nabla\cdot\mathbf v)^2+\eta\mathbf J\cdot(\mathbf J-\mathbf J_0)\big]+\kappa\Delta(p-p_0),\\
\partial_t\mathbf B &= -\nabla\times\mathbf E,\qquad \mathbf E=-\mathbf v\times\mathbf B+\eta(\mathbf J-\mathbf J_0),\qquad \mu_0\mathbf J=\nabla\times\mathbf B,
\end{aligned}$$

with $\Delta$ the Laplacian, $D$ an isotropic mass diffusivity and $\kappa$ an
isotropic pressure diffusivity. EP current ([current coupling](/methods/pressure-and-current-coupling.md)):

$$\mathbf J_h=\sum_pq_hw_p\big(v_{\parallel p}\mathbf B^*/B^*_\parallel+\mathbf v_{\nabla B,p}\big)\mathcal S(\mathbf x-\mathbf x_p)-\nabla\times\Big[\mathbf b\sum_p\mu_pw_p\mathcal S(\mathbf x-\mathbf x_p)\Big],$$

the first term parallel plus curvature and $\nabla B$ drift currents, the
second the magnetization current; $\mathcal S$ is the shape factor,
$B^*_\parallel=B(1+\rho_\parallel\mathbf b\cdot\nabla\times\mathbf b)$ with
$\rho_\parallel=m_hv_{\parallel p}/(q_hB)$. Drift-kinetic $\delta f$ markers
([δf method](/methods/delta-f-method.md)); passive test particles that
respond to the field but do not contribute to $\mathbf J_h$ raise the
phase-space resolution. Finite differences on an Eulerian grid; equilibrium
from a Grad–Shafranov solver for a given $q$. **Not given:** grid size and
coordinates, difference order, time integrator, $\Delta t$, marker and
test-particle counts, toroidal harmonics kept, boundary conditions, cost,
parallelism.

**Phase-space formalism** (§3; page-local symbols, defined here). Guiding-centre
Hamiltonian $H=\tfrac12m_hv_{\parallel p}^2+\mu B$ in the canonical
straight-field-line angles of Li et al. (2016), canonical momenta
$P_\theta=q_h\psi+m_hv_{\parallel p}b_\theta$ and
$P_\phi=-q_h\psi_t+m_hv_{\parallel p}b_\phi$ (covariant field components; the
flux in $P_\phi$ is undefined in the paper and read as the toroidal flux).
Action-angle variables of the unperturbed motion: actions $\mathcal P_\theta$,
$\mathcal P_\phi$, angles $\vartheta$, $\varphi_a$, transit frequencies
$\omega_\theta=\partial H_0/\partial\mathcal P_\theta$,
$\omega_\phi=\partial H_0/\partial\mathcal P_\phi$. For an isolated resonance
the perturbation depends on $\ell\vartheta+n\varphi_a-\varphi_w(t)$, with
wave phase $\varphi_w$, $\dot\varphi_w=\omega(t)$. The generating function
$G_2=\mathcal P_1[\ell\vartheta+n\varphi_a-\varphi_w(t)]+\mathcal P_2\varphi_a+\mathcal P_3\times(\text{gyroangle})$
gives

$$\mathcal P_1=\mathcal P_\theta/\ell,\qquad \mathcal P_2=\mathcal P_\phi-\frac n\ell\mathcal P_\theta,\qquad \Theta=\ell\vartheta+n\varphi_a-\varphi_w(t),$$

with the sign of $\mathcal P_2$ corrected (printed "+", see Citations). The new
Hamiltonian depends on $\Theta$ only, so $\mathcal P_2$ and $\mathcal P_3$
(magnetic moment) are constants and the dynamics is 1D in
$(\mathcal P_1,\Theta)$, whatever $\dot\varphi_w(t)$. The poloidal action for
$\mu=0$ is fitted as a 2D polynomial in $\sqrt{\mathcal E}$ and $\mathcal P_\phi$
by constrained least squares on orbit frequencies (CVX), with constraints
$\partial\mathcal P_\theta/\partial\mathcal E=1/\omega_\theta$ and
$\partial\mathcal P_\theta/\partial\mathcal P_\phi=-\omega_\phi/\omega_\theta$.
Markers are recorded on the plane $Z=0$, $R>R_0$, where the canonical angles
equal the geometric ones and $\mathcal P_\phi=P_\phi$.

**Case** (§4). Circular cross-section, $R_0/a=3.2$, $q=1+0.3r/a$, uniform
density and pressure; first TAE gap ($m=6$–7) at $r/a=0.26$, second ($m=7$–8)
at 0.82, gap condition $q=(m+1/2)/n$. EP distribution
$f_0\propto[1+\mathrm{erf}((\mathcal E_0-\mathcal E)/\Delta\mathcal E)]\exp(-\langle\psi\rangle/\Delta\psi)/(\mathcal E^3+\mathcal E_c^3)$
with $\mathcal E_0=1.44\mathcal E_A$, $\mathcal E_c=0.25\mathcal E_A$,
$\Delta\mathcal E=0.0144\mathcal E_A$, $\Delta\psi=0.148\psi_{\max}$,
$\mathcal E_A=\tfrac12m_hv_A^2$ on axis; $\beta_h=0.6\%$ on axis.
Dissipation $\nu=\eta=0.3\times10^{-7}v_AR_0$ (MEGA units, $\eta$ as a
magnetic diffusivity), $D=\kappa=0$. Runs of ≈2500 $\tau_A$ (base) and ≈3700
$\tau_A$ (modified dissipation).

# Tests and results

One physics case; no code comparison.

| Quantity | Value | Location |
|---|---|---|
| $\omega/\omega_A$ (linear TAE) | 0.4553 | Fig. 1b |
| $(\gamma_l-\lvert\gamma_d\rvert)/\omega_A$ | 0.0067 (fit of $\lvert v_r\rvert$ at $r/a=0.27$, $n=6$, $m=6$) | Fig. 2a |
| $\gamma_d/\omega_A$ | 0.0053 (intercept of the $\beta_h$ scan) | Fig. 3a |
| $\gamma_l/\omega_A$, $\gamma_d/\gamma_l$, $\gamma_l/\omega$ | 0.012, 0.44, 2.64% | §4.1 |
| first saturation | $v_r/v_A\approx1.4\times10^{-4}$ at $t/\tau_A\approx300$ | Figs. 2a, 4a |
| base-run chirp | $\omega/\omega_A$ 0.455 → ≈0.49 and ≈0.43 by $t/\tau_A\approx2200$ | Fig. 2b |
| modified dissipation | amplitude ≈$0.15\times10^{-4}$; ≈0.53 and ≈0.39 by $t/\tau_A\approx3600$; +13.55% / −11.33% at 2477.8 | Fig. 4, §4.4 |
| tracked particle | $\Delta\mathcal P_2\approx0$, $\Delta P_\phi\approx-6$, $\Delta(\omega P_\phi-n\mathcal E)/\omega\approx+0.8$ | Fig. 10 |

* Mode structure: $m=6$ peak at $r/a\approx0.24$, $m=7$ at ≈0.27,
  $v_r/v_A\sim5\times10^{-6}$ at $t/\tau_A=217.6$ (Fig. 3b).
* Radial frequency spectra at $t/\tau_A=196.1$, 469.7, 1713.1, 3570.4: gap
  structure, sidebands, migration to the gap tips, radius-dependent
  continuum frequencies (Fig. 5).
* Phase-space slices: $\mathcal P_2=33,38,43$ lines in the
  $(P_\phi,\mathcal P_\theta)$ plane; analysis at $\mathcal P_2=39\pm0.2$,
  $\mathcal P_1\in[18.6,20.2]$, $\Theta\in[0,4\pi]$; snapshots at
  $t/\tau_A=205.4$, 314.5, 2477.8, 3224.1, 3722.2 (Figs. 8–9).
* Values read from figures are approximate; values in the text are as
  printed.

# Notation map

| Hezaveh et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf j$, $\mathbf j_\alpha$ | $\mathbf J$, $\mathbf J_h$ | |
| $\nu_n$ | $D$ (isotropic) | |
| $\gamma$ (Eq. 3) | $\Gamma$ | **collision:** registry $\gamma$ is the growth rate |
| $\lambda$ (Eq. 3) | $\kappa$ (isotropic) | |
| $\lambda$ (after Eq. 5) | $\xi$ (pitch $v_{\parallel p}/\lvert\mathbf v_p\rvert$) | **collision:** same letter as the conductivity |
| $\nu$, $\eta$ | $\nu$ (kinematic), $\eta$ | in units of $v_AR_0$: $\eta$ is a magnetic diffusivity |
| $eZ_\alpha$, $m$ | $q_h$, $m_h$ | Eq. 7 says "electron charge" |
| $w_i$, $\mathbf x_i$, $S$ | $w_p$, $\mathbf x_p$, $\mathcal S$ (page-local) | **collision:** registry $S$ is the Lundquist number |
| $\mathbf v_{B,i}$, $\mathbf v^*_\parallel$ | $\nabla B$ drift (part of $\mathbf v_d$), $v_{\parallel p}\mathbf B^*/B^*_\parallel$ | |
| $B^*$ | $B^*_\parallel$ | |
| $\rho_\parallel$ | $\rho_\parallel$ (page-local) | **collision risk:** registry $\rho$ is the mass density |
| $E_k$, $E$ | $\mathcal E$ | |
| $\Omega$ | words (gyroangle) | **collision:** registry $\Omega_s$ is the cyclotron frequency |
| $\theta_c$, $\xi_c$ | $\theta$, toroidal angle of the Li et al. coordinates | canonical straight-field-line |
| $P_{\theta_c}$, $P_{\xi_c}$, $P_\Omega$ | $P_\theta$, $P_\phi$, $(m_h/q_h)\mu$ | page-local $P_\theta$ |
| $\tilde\theta_c$, $\tilde\xi_c$; $P_{\tilde\theta_c}$, $P_{\tilde\xi_c}$ | $\vartheta$, $\varphi_a$; $\mathcal P_\theta$, $\mathcal P_\phi$ | page-local |
| $\omega_{\tilde\theta_c}$, $\omega_{\tilde\xi_c}$ | $\omega_\theta$, $\omega_\phi$ | called "bounce" and "precession" in the paper |
| $\chi$ (Eq. 9b) | $\psi_t$ (presumed) | **collision:** registry $\chi$ is the vacuum scalar potential; undefined in the paper |
| $\phi_{m;n;h}$, $U$ | words (orbit-averaged wave amplitudes, perturbation) | **collision:** native $\phi$ is not the toroidal angle |
| $p$, $h$, $l=p/h$ | $\ell$ (with $h=1$) | $\ell$ as on the TAE page |
| $\alpha(t)$ | $\varphi_w(t)$ | registry $\alpha_{\mathrm b}$ is ballooning |
| $P_1,P_2,P_3$; $\zeta$ | $\mathcal P_1,\mathcal P_2,\mathcal P_3$; $\Theta$ | **collision:** native $\zeta$ vs registry toroidal angle $\zeta$ |
| $G$, $M$ (Eqs. 19–21) | words (fit polynomial, objective) | **collision risk** with Boozer $G$ and helicity $M$ |
| $(R,z,\varphi)$, $P_\varphi$ | $(R,Z,\phi)$, $P_\phi$ | orientation not stated |
| $\epsilon$ ("inverse aspect ratio" = 3.2) | $R_0/a$ | see Citations |
| $\omega_{\mathrm{TAE}}$, $\omega_A$, $t_A$ | $\omega$, $1/\tau_A$, $\tau_A$ | length $R_0$ presumed |
| $\gamma_l$, $\gamma_d$ | $\gamma_l$, $\gamma_d$ | drive and damping rates |
| $\beta_{0,EP}$ | $\beta_h$ on axis | |
| $F_{\mathrm{eq},\alpha}$, $\kappa$ | $f_0$, normalization constant | **collision:** $\kappa$ vs conductivity |
| $E_0$, $E_{\mathrm{crt}}$, $\Delta E$, $E_A$ | $\mathcal E_0$, $\mathcal E_c$, $\Delta\mathcal E$, $\mathcal E_A$ | registry $E_c$ is the runaway critical field |
| $C=\omega_{\mathrm{TAE}}P_\varphi-nE$ | $\omega P_\phi-n\mathcal E$ | |

# Pages created or updated

Chunk 2 (2026-10-16) created or updated the pages below; chunk 3 extended some. This source is cited on:

* [Energetic particle mode (EPM) and frequency chirping](/definitions/energetic-particle-mode.md)
* [Hybrid kinetic-MHD models](/methods/hybrid-kinetic-mhd.md)
* [MEGA](/software/mega.md)
* [Pressure coupling and current coupling](/methods/pressure-and-current-coupling.md)
* [The δf particle method](/methods/delta-f-method.md)
* [Toroidal Alfvén eigenmode (TAE)](/definitions/toroidal-alfven-eigenmode.md)
* [Wave-frame action-angle diagnostic of chirping modes](/methods/chirping-phase-space-diagnostic.md)

# Citations

1. `/home/stefano/papers/mosaic/fusion-mhd-simulation/2022_Crossref_Nuclear_Fusion_Hezaveh_Simulation_of_convective_transport_during_frequency_chirping.pdf`
   * **Version.** arXiv:2109.01032v1 [physics.plasm-ph], 2 September 2021
     (LaTeX build 3 September 2021), 14 pages, pre-refereeing preprint; not
     the published version. Numbers and equations may differ from Nucl.
     Fusion 62:036025.
   * **Identity.** doi:10.1088/1741-4326/ac49ab, checked on Crossref: title,
     five authors in printed order, Nucl. Fusion 62(3), article 036025, issue
     March 2022 (online 3 February 2022).
   * **How read.** Full text; all equation pages (2–4, 6, 8) and figure pages
     (5–12) checked rendered. Figure values are approximate readings.
   * **Recorded as printed.**
     * Eq. 16 prints $P_2=P_{\tilde\xi_c}+\frac nlP_{\tilde\theta_c}$. From the
       printed generating function (Eq. 15),
       $P_{\tilde\xi_c}=\partial G_2/\partial\tilde\xi_c=nP_1+P_2$, so
       $P_2=P_{\tilde\xi_c}-\frac nlP_{\tilde\theta_c}$. The paper's numbers
       confirm the minus sign: with $n=6$, $l=-6$, $P_\varphi\approx155$,
       $P_{\tilde\theta}\approx-115$ (Fig. 8), the printed form gives ≈270,
       the corrected one ≈40, matching the analysed $P_2\approx39$, the slope
       −1 lines of Fig. 8 and $P_1\approx+19.2$ on Fig. 9 (compiler's check).
     * Eq. 17 omits the $\partial G_2/\partial t=-\dot\alpha P_1$ term of a
       time-dependent type-2 transformation; the conservation of $P_2$ is
       unaffected (compiler's check).
     * "Inverse aspect ratio ǫ = 3.2" (§4) must be the aspect ratio $R_0/a$.
     * Eq. 7: "e is the electron charge" for EP guiding centres; Eq. 7 has
       $m_i/e$, Eq. 9c $m/e$.
     * Eq. 9b uses $b_{\varphi_c}$ with the angle $\xi_c$; $\chi$ is never
       defined. "$eZ_{alpha}$" (LaTeX not rendered) after Eq. 5.
     * Eq. 14 uses $p$ before it is defined (§4.2).
     * $\omega_{\tilde\theta_c}$, $\omega_{\tilde\xi_c}$ are called "bounce" and
       "precession" frequencies for highly passing ($\mu=0$) particles; they
       are transit frequencies.
     * Eq. 22 parameters are called alpha-particle birth and critical
       energies while §3 motivates $\mu=0$ by an NBI scenario; the loaded
       distribution is isotropic, so the $\mu=0$ slice is an analysis choice.
     * Figs. 9–10 (times to $t/\tau_A=3722.2$) must belong to the
       modified-dissipation run of Fig. 4 (the Fig. 2 run ends near 2500);
       not stated.
     * Fig. 10 axis: non-uniform snapshot times at equal spacing. Fig. 8
       caption and §4.3 drop the subscript $c$ or the tilde.
     * Fig. 1a abscissa labelled $r$, not $r/a$; with $q=1+0.3r/a$ the first
       gap ($q=13/12$) lies at $r/a\approx0.28$, not the printed 0.26
       (toroidal shift plausible).
     * Claim 6 is shown with dissipation coefficients, not a measured damping
       rate, and the base spectrogram ends earlier (≈2200) than Fig. 4b.
     * The BB prefactor $16\sqrt2/(3\sqrt3\pi^2)=0.441$ checks.
     * Typos: "Wee start from the the", "cylinderical", "the damping
       coefficients has been increased".
   * **Reference list.** 38 printed entries; refs. [27] and [28] are the same
     work (Littlejohn 1983, J. Plasma Phys. 29:111), merged into one entry
     `littlejohn-1983`, so 37 entries are merged under `hezaveh-2022`. White's
     book printed 2014 is `white-2013`. Wang X.Q. et al. (PPCF 63, printed
     2020) is `wang-2020-b`. Garbled author tails ("and and H H") in [5], [7],
     [8] are entered with "and others"; Grimm, Greene & Johnson (1976) is a
     book chapter; CVX is a software entry. No titles or DOIs are printed for
     articles.
