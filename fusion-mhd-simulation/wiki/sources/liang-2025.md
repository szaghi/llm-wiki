---
type: Source
title: "Liang et al. (2025) — Predictive nonlinear MHD simulations of quiescent H-mode plasma in the HL-3 tokamak"
description: "Predictive JOREK reduced-MHD simulation of HL-3 in realistic lower-single-null geometry reaches, without torque input, a QH-mode with a saturated n = 2 kink-peeling mode and an edge harmonic oscillation of 7.5 kHz fundamental that is asymmetric between high- and low-field sides; the QH-mode is lost, with an ELM-like burst, when q95 drops from 2.5 to 2.3."
resource: "doi:10.1063/5.0238464"
source_kind: paper
authors: [Liang Z., Hoelzl M., Cathey A., Hu D., Dai S.Y., Liu Y.L., Wang D.Z., JOREK Team]
year: 2025
venue: "Phys. Plasmas 32:012502"
local_file: "/home/stefano/papers/mosaic/fusion-mhd-simulation/2025_Crossref_Physics_of_Plasmas_Liang_Predictive_nonlinear_MHD_simulations_of_quiescent_H-mode_pla.pdf"
tags: [elm, pedestal, edge, kink, reduced-mhd, extended-mhd, divertor, tokamak]
timestamp: 2026-10-16T20:00:00Z
---

# Summary

The paper makes predictive [JOREK](/software/jorek.md) simulations of a quiescent
H-mode (QH-mode) for HL-3 (formerly HL-2M; $R_0=1.78$ m, $a=0.65$ m) with no HL-3
discharge as input. The model is single-temperature
[reduced MHD](/methods/reduced-mhd.md) with the ion diamagnetic extension, a
Sauter-evolved [bootstrap](/definitions/bootstrap-current.md) source current,
Mach-1 [sheath conditions](/methods/sheath-boundary-conditions.md) at the targets
and no momentum source, on a realistic lower-single-null grid of 11136
[$G^1$ Bézier elements](/methods/bezier-finite-elements.md). An axisymmetric run
(0–12.72 ms) with ad hoc transport wells and 24 MW heating builds an H-mode
pedestal; then $n=1$–12 are switched on from noise. At $B_\phi=+2.1$ T,
$I_p=-2.0$ MA, $q_{95}=2.5$ only $n=2$ and 3 are linearly unstable; the modes
saturate near 19 ms with $n=2$ dominant and stay quasi-stationary to 60 ms. The
saturated kink-peeling mode stochastizes the edge outside $\psi_N\approx0.93$,
with resilient surfaces near $q=2$ ($\psi_N\approx0.87$), relaxes the pedestal
slightly and stops the thermal energy growth. The
[edge harmonic oscillation](/definitions/edge-localized-mode.md) (EHO) in the
density at $\psi_N=0.95$ has harmonics at integer multiples of a 7.5 kHz
fundamental, which the paper places within the measured JET, DIII-D, AUG and
HL-2A range. The EHO is asymmetric between high-field side (HFS, $n=2$ at 15 kHz
dominant) and low-field side (LFS, $n=3$ at 22.5 kHz comparable to or above
$n=2$ near $\psi_N=0.95$). The density perturbation peaks where $|E_r|$ is locally
weak and the density gradient is steepest; the temperature perturbation peaks
where $E_r$ is strong. Lowering $B_\phi$ to 2.0 T ($q_{95}=2.3$) loses QH-mode:
$n=2$ is linearly stable, a low-amplitude $n=8$ precursor appears, the pedestal
keeps building, and an ELM-like burst ($n=2$, 4) at 52.1 ms removes ≈3% of
$W_{\mathrm{th}}$ in ≈1 ms.

# Key claims

Page-local symbols: $\delta^*=(\Omega_iR_0)^{-1}$ diamagnetic parameter, with
$\Omega_i=eB_0/m_i$ at the axis; $j_{\mathrm{src}}$ the source current (Ohmic
plus bootstrap) in Ohm's law; EHO harmonic frequencies $\omega_n/2\pi$.

1. **QH-mode at low $q_{95}$** (Abstract; §IV B 1; Figs. 7–8). QH-mode is obtained
   at $q_{95}=2.5$ ($B_\phi=+2.1$ T, $I_p=-2.0$ MA), dominated by a saturated $n=2$
   kink-peeling mode. Shown.
2. **No torque input** (§III, §V). QH-mode is reached "without torque injection (no
   momentum source is included)"; the "self-generated $E\times B$ rotation shear can
   stabilize the high-n modes when the diamagnetic effect is taken into account".
   QH-mode Shown; mechanism Stated (no separate test).
3. **Linear spectrum** (§IV B 1). Separate linear runs of $n=1$–12 give only $n=2$
   and 3 unstable, which justifies truncating at $n=12$ ("even higher n modes are
   stabilized by diamagnetic effect"). Shown (no growth-rate values printed).
4. **Three-wave coupling** (§IV B 1, Fig. 7a). $n=1$ is excited at ≈16 ms by $n=2$
   and 3 with $\gamma_{n=1}\approx\gamma_{n=2}+\gamma_{n=3}$ (Krebs et al. 2013);
   $n=12$ is driven at 16.5 ms; the growth of $n=4,5,10,11$ changes by coupling.
   Shown.
5. **Saturation** (Fig. 7b). At ≈19 ms with $n=2$ dominant; stationary kinetic
   energies to 60 ms. Shown.
6. **Stochastic edge with resilient surfaces** (§IV B 1; Figs. 9–10). A stochastic
   layer outside $\psi_N=0.93$ widens with time; resilient surfaces persist near
   $\psi_N\approx0.87$ ($q=2$) "despite the fact that the KAM surfaces are not
   enforced in JOREK"; $q$ barely changes. Shown.
7. **Pedestal relaxation** (§IV B 1; Figs. 11–12). Transport rises by parallel
   conduction in the stochastic layer and by non-axisymmetric $E\times B$ convective
   cells; $W_{\mathrm{th}}$ inside the separatrix drops slightly at saturation and
   then stays virtually constant (rising steadily in the axisymmetric reference);
   pedestal $p$ and $T_e$ relax at ≈19 ms and the $E_r$ well becomes shallower; no
   visible density pump-out because the pedestal particle source dominates. Shown.
8. **EHO frequency** (§IV B 2, Figs. 13–14). The HFS density at $\psi_N=0.95$
   (31–34 ms) is non-sinusoidal with equally spaced harmonics $\omega_n=n\omega_1$;
   $n=2$ dominates at 15 kHz, so the fundamental is 7.5 kHz, "within the range" of
   measured EHO fundamentals (JET ≈6, DIII-D ≈10, AUG ≈10, HL-2A ≈6 kHz). Shown;
   measured values Attributed.
9. **HFS–LFS asymmetry** (§IV B 2–3, Figs. 15–16a). At the LFS $n=2$ and $n=3$
   (22.5 kHz) contribute comparably at $\psi_N=0.95$ with lower amplitude, and $n=3$
   exceeds $n=2$ there (the $n=2$ profile has a valley at 0.94); at the HFS $n=2$
   dominates except at $\psi_N=0.88$–0.90. Shown. Mechanism "not completely
   understood"; edge gradients and rotation shear "suspected". Stated.
10. **Density and temperature respond differently** (§IV B 3; Figs. 16–17). The
    density perturbation peaks roughly where $E_r$ is locally weak and
    $|\partial n/\partial R|$ is largest; the temperature perturbation peaks at the
    two $E_r$ extrema ($\psi_N=0.915$, 0.976) with similar HFS and LFS structure.
    Shown (correlation only).
11. **Robustness to the start time** (§IV B 3). Starting the 3D phase at 3 or 6 ms
    gives different linear and early-nonlinear phases but the same $n=2$-dominated
    saturated state. Shown (stated, no figure).
12. **No-wall case** (§III). Also reaches QH-mode, though $n=1$ is then linearly
    unstable; with the ideal wall $n=1$ is stable and subdominant. Shown (stated, no
    figure).
13. **Loss of QH-mode at $q_{95}=2.3$** (§IV C; Figs. 18–20). With $B_\phi=2.0$ T
    (shear unchanged, $q<1$ for $\psi_N<0.36$) $n=2$ is linearly stable, $n=8$
    dominates a low-amplitude precursor, the pedestal builds until 50.32 ms, a
    second precursor ($n=2$ oscillating) starts at 50.5 ms, $n=4$ is driven at
    51.5 ms and the burst peaks at 52.1 ms, losing ≈3% of $W_{\mathrm{th}}$ in
    ≈1 ms. Shown. Called a type-I ELM crash; a resolved study ("finer grid
    resolution, a higher toroidal resolution, and smaller time steps") is deferred.
14. **Contrast with AUG** (§IV C). QH-mode access is sensitive to $q$ (Meier et al.
    2023), but this regime has "much lower edge safety factor". Stated.
15. **Enhanced resistivity** (§III). $\eta\propto T_e^{-3/2}$ with
    $\eta\approx2.6\times10^{-6}$ Ω m at $\psi_N=0.95$ (500 eV) is ≈4× Spitzer;
    with $Z_{\mathrm{eff}}=2$ and the neoclassical factor $(1-\sqrt{r/R_0})^{-2}=6.38$
    the realistic value is $0.7\times10^{-6}$ Ω m, which "would exceed the
    computational capability of present HPC resources". Stated.
16. **Full against reduced MHD** "agree excellently" for pedestal and ELM studies
    (§III, Pamela et al. 2020). Attributed.
17. **Implied ELM frequency** (§IV A). Taking the initial profiles as post-ELM and
    the 12 ms build-up as pre-ELM gives a frequency "relevant to" AUG at high
    triangularity (Dunne et al. 2017). Stated (loose).

# Models and numerics

**Model** (§III, Eqs. 1–9, JOREK normalized units). With $F_0=B_0R_0$ constant
(no fast magnetosonic waves) and $\mathbf v_\perp\perp\mathbf e_\phi$ (valid for
$B_{\mathrm{pol}}/B_\phi\ll1$), in registry symbols:

$$\begin{aligned}
\mathbf B&=\frac{F_0}{R}\mathbf e_\phi+\frac1R\nabla\psi\times\mathbf e_\phi,\qquad
\mathbf v=\hat v_\parallel\mathbf B-R\nabla u\times\mathbf e_\phi-\frac{\delta^*R}{\rho}\nabla p_i\times\mathbf e_\phi,\\
\partial_t\rho&=-\nabla\cdot(\rho\mathbf v)+\nabla\cdot(D_\perp\nabla_\perp\rho)+S_\rho,\\
\rho\,\partial_tT&=-\rho\mathbf v\cdot\nabla T-(\Gamma-1)\rho T\nabla\cdot\mathbf v+\nabla\cdot(\kappa_\perp\nabla_\perp T+\kappa_\parallel\nabla_\parallel T)+S_p,\\
\partial_t\psi&=-R\eta\,(j-j_{\mathrm{src}})-R[u,\psi]-F_0\partial_\phi u+\frac{\delta^*R}{\rho}[p_e,\psi]+\frac{F_0\delta^*}{\rho}\partial_\phi p_e,\\
j&=\Delta^*\psi,\qquad\varpi=\Delta^\perp u,
\end{aligned}$$

with $[u,\psi]=\partial_Ru\,\partial_Z\psi-\partial_Zu\,\partial_R\psi$, and the
momentum equation $\rho\partial_t\mathbf v=-\rho\mathbf v\cdot\nabla\mathbf v-\nabla(2\rho T)+\mathbf J\times\mathbf B+\nu\Delta\mathbf v$
projected by $\mathbf e_\phi\cdot\nabla\times$ (vorticity) and $\mathbf B\cdot$
(parallel flow). Variables $\psi,\rho,T,\hat v_\parallel,u,\varpi,j$;
$u=\Phi/F_0$; $T=T_e=T_i$, $p=2nT$; $E_r=-F_0\nabla u\cdot\nabla\psi/|\nabla\psi|$.
For the open sign contradiction on [reduced MHD](/methods/reduced-mhd.md)
the printed flux equation is mixed: the resistive term $-R\eta(j-j_{\mathrm{src}})$
with $j=\Delta^*\psi$ has the sign of [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) and
[Nikulsin et al. (2022)](/sources/nikulsin-2022.md) (non-diffusive with $\Delta^*$ negative semi-definite), while
$-F_0\partial_\phi u$ has the sign of the diffusive-side sources; the extra factor
$R$ on the resistive term also differs from both printed families (compiler's
comparison; the paper does not discuss it).

**Closures and sources.** $D_\perp$ and $\kappa_\perp$ ad hoc profiles with a
pedestal well (Fig. 3; the text gives $\kappa_\perp=\chi_\perp\rho$ in
kg m⁻¹ s⁻¹); particle source concentrated near $\psi_N=0.95$; core-peaked heat
source ≈24 MW; no momentum source. $\eta\propto T_e^{-3/2}$ evolved with $T$.
$j_{\mathrm{src}}$ = constant Ohmic part (from the initial current) + bootstrap
part evolved with the Sauter formula. Viscosity value not given.

**Discretization.** Weak-form finite elements: 11136 $G^1$ Bézier elements on a
flux-aligned lower-single-null grid (71 radial × 121 poloidal points inside the
separatrix; 18 radial points in the SOL, 6 in the private-flux region, 13
poloidal points along the divertor legs; confined radius 0.55 m at the outer
midplane, SOL 0.04 m), refined radially in the pedestal and poloidally at the
X-point; toroidal harmonics $n=0,\dots,12$. Taylor–Galerkin stabilization on the
$u$, $\rho$, $T$, $\hat v_\parallel$ equations
([stabilization](/methods/variational-multiscale-stabilization.md)). Time
integration, time step, solver and cost are not given (cited); the diagnostic
sampling interval is $6.48\times10^{-7}$ s.

**Boundary conditions.** Ideal wall where the boundary is parallel to flux
surfaces (a no-wall case was also run; a resistive wall is insignificant per Liu
et al. 2015); Mach-1 sheath conditions at the targets; fixed boundary (free
boundary named as future work).

**Equilibrium.** HL-3 lower single null, $I_p=-2.0$ MA counter-clockwise from the
top, $B_\phi=+2.1$ T clockwise; JOREK's $(R,Z,\phi)$ has $\phi$ clockwise from the
top. Initial profiles without pedestal (Fig. 2); the Grad–Shafranov equilibrium is
maintained during the axisymmetric phase. Computing at IPP and MPCDF.

# Tests and results

* **Axisymmetric build-up** (0–12.72 ms, Figs. 5–6): pedestal $p$ and $T_e$ grow,
  pedestal $n_e$ drops slightly, the $E_r$ well deepens, $j_\phi$ rises by the
  bootstrap current; at the pedestal top $p\approx40$ kPa ($\psi_N\approx0.75$),
  $T_e\approx1.4$ keV, $n_e\approx0.9\times10^{20}$ m⁻³ (figure readings).
* **QH case** ($n=0$–12 from 12.72 ms, Figs. 7–10): linear phase $n=2$, 3; $n=1$
  driven at 16 ms, $n=12$ at 16.5 ms; saturation ≈19 ms; $n=2$ dominant to 60 ms;
  perturbations of $\psi$, $T_e$, $n_e$ localized at $\psi_N=0.9$–1.0, largest at
  the top and bottom of the flux surfaces (32.17 ms); Poincaré plots at 12.72, 17,
  20, 25, 35, 55 ms with 4/2, 7/3, 5/2, 8/3 and 6/2 surfaces marked.
* **EHO** (Figs. 13–17): HFS 15 kHz ($n=2$); LFS 15 and 22.5 kHz; $n>7$ above
  55 kHz with small amplitude; HFS $n=2$ density peak at $\psi_N=0.95$; $\delta T_e$
  up to ≈0.1 keV for LFS $n=2$ (figure reading).
* **ELM-like case** ($B_\phi=2.0$ T, Figs. 18–20): $W_{\mathrm{th}}\approx2.3$–2.6 MJ;
  pedestal $p$ grows until 50.32 ms and drops visibly at 52.14 ms; core $q<1$ modes
  present but "insignificant".
* No code-to-code benchmark, no convergence study, no experimental validation
  (predictive by design).

| Device (as cited) | Measured EHO fundamental [kHz] |
|---|---|
| JET | ≈6 |
| DIII-D | ≈10 |
| ASDEX Upgrade | ≈10 |
| HL-2A | ≈6 |
| HL-3 (this simulation) | 7.5 |

# Notation map

| Liang et al. (2025) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $R,Z,\phi$, $\mathbf e_\phi$ | $R,Z,\phi$, $\mathbf e_\phi$ | $\phi$ clockwise from the top |
| $\mathbf B_\phi$, $\mathbf B_{pol}$, $B_t$ | words; $B_\phi$ on axis | |
| $F_0=B_0R_0$, $B_0$, $R_0$ | $F_0$; $B_\phi(R_0)$, $R_0$ | |
| $\psi$; $\psi_{norm}$, $\psi_n$, $\Psi_{norm}$ | $\psi$ (per radian); $\psi_N$ | three spellings printed; $\Psi$ collides with $\Psi_{m/n}$ |
| $v_\parallel$ in $\mathbf v_\parallel=v_\parallel\mathbf B$ | $\hat v_\parallel$ | not $\mathbf v\cdot\mathbf b$ |
| $u=\Phi/F_0$, $\Phi$ | $u$, $\Phi$ | |
| $\omega=\nabla_\perp^2u$ | $\varpi=\Delta^\perp u$ | **collision:** registry $\omega$ is a frequency |
| $j=\Delta^*\psi$, $j_\phi$ | $j$, $j_\phi$ | $\mu_0=1$ |
| $j_S$ | $j_{\mathrm{src}}$ (page-local) | Ohmic + bootstrap, i.e. the scalar form of $\mathbf J_x$ plus the Ohmic part |
| $\delta^*$, $\Omega_{ci}$ | page-local; $\Omega_i$ | |
| $\rho$, $n$, $n_e$ | $\rho$, $n_e$ | |
| $T$ | $T=T_e=T_i$ | not the sum; $p=2nT$ |
| $\gamma$ (Eq. 4); $\gamma_n$ | $\Gamma$; $\gamma$ | **collision:** the paper uses $\gamma$ for both |
| $\mu$ | $\nu$ | **collision:** registry $\mu$ is the magnetic moment |
| $\kappa_\perp$ / $K_\perp$, $\kappa_\parallel$, $\chi_\perp$ | $\kappa_\perp$, $\kappa_\parallel$, $\chi_\perp$ | |
| $S_\rho$, $S_T$; $S_p$, $S_E$ (Fig. 3) | $S_\rho$, $S_p$ | |
| $\eta$, $\eta_{95}$ | $\eta$ | |
| $[u,\psi]$, $\Delta^*$, $\nabla_\perp^2$ | $[f,g]$, $\Delta^*$, $\Delta^\perp$ | |
| $E_r$ | $E_r$ | |
| $f_n=nf_{n=1}$ | $\omega_n/2\pi$ | registry: $f$ never a frequency |
| $\kappa$, $\delta$ (Table I) | words (elongation, triangularity) | **collision** with $\kappa_\parallel$ and the $\delta(\cdot)$ prefix |
| $E_{mag}$, kinetic energy per $n$, thermal energy | $W_{\mathrm{mag}}^{(n)}$, $W_{\mathrm{kin}}^{(n)}$, $W_{\mathrm{th}}$ | |

JOREK normalized units in the equations ($\mu_0=1$, density normalized to a
reference mass density); figures in SI.

# Pages created or updated

Chunk 3 (2026-10-16) created or updated the pages below. This source is cited on:

* [Bootstrap current and its MHD implementation](/definitions/bootstrap-current.md)
* [Bézier–Hermite finite elements with toroidal Fourier harmonics](/methods/bezier-finite-elements.md)
* [Edge harmonic oscillation and QH-mode](/definitions/edge-harmonic-oscillation.md)
* [Edge-localized mode (ELM) and ELM-free regimes](/definitions/edge-localized-mode.md)
* [JOREK](/software/jorek.md)
* [Reduced MHD for tokamaks](/methods/reduced-mhd.md)
* [Resonant magnetic perturbations and plasma response](/definitions/resonant-magnetic-perturbation.md)
* [Sheath (Bohm) boundary conditions](/methods/sheath-boundary-conditions.md)
* [Variational multiscale (VMS) stabilization for MHD finite elements](/methods/variational-multiscale-stabilization.md)

# Citations

1. `/home/stefano/papers/mosaic/fusion-mhd-simulation/2025_Crossref_Physics_of_Plasmas_Liang_Predictive_nonlinear_MHD_simulations_of_quiescent_H-mode_pla.pdf`.
   * **Version.** Publisher version of record (AIP, CC BY 4.0) with an AIP cover
     page: 16 PDF pages = cover + article pp. 012502-1 to -15.
   * **Identity.** doi:10.1063/5.0238464, checked on Crossref: Phys. Plasmas
     32(1), article 012502, online 2025-01-10; authors in the printed order (the
     JOREK Team is the author list of Hoelzl et al. 2021, footnote b); 57
     references.
   * **How read.** Full text; Eqs. 1–9 and Table I read; curve values are figure
     readings. Time integration, time step, viscosity value and cost are not given
     in the paper.
   * **Recorded as printed.**
     * Elongation "ranges from 1.8 to 2.2" (§II) against "1.8–2.0" (Table I).
     * Table I baseline $B_t=2.5$ T, $I_p=2.5$ MA; the runs use 2.1 T (2.0 T) and
       −2.0 MA, below baseline (not an error).
     * §IV B 1: "only $n=2$ and $n=3$ modes are linearly unstable" and "the $n=1$
       and $n=12$ modes are linearly stable", yet "the growth rates of linearly
       unstable modes are also changed … in the $n=4,5,10,11$ modes", which implies
       those are linearly unstable.
     * ELM-like case: §IV C "the $n=8$ mode dominates before the saturation" with an
       $n=2$ second precursor; §V "$n=3$ and 2 modes are observed to saturate
       initially at low amplitudes".
     * Energy loss "about 3% … in 1 ms" (§IV C) against "within less than a
       millisecond" (§V).
     * Source symbols $S_\rho$, $S_T$ (Eqs. 3–4) against $S_p$, $S_E$ (Fig. 3); heat
       coefficient $\kappa_\perp$ (Eq. 4) against $K_\perp$ (text, Fig. 3); three
       spellings of the normalized flux.
     * Eq. 2 uses $\nabla p_i$, Eq. 7 $p_e$ in the diamagnetic terms; with one
       temperature $p_i=p_e=p/2$. $\delta^*=(\Omega_{ci}R_0)^{-1}$ carries no mass
       factor in the numerator.
     * $\gamma$ is both the adiabatic index and the growth rate; $\omega$ is the
       vorticity. "Jorek" spelled once in mixed case.
     * Neoclassical factor 6.38 implies $r/R_0\approx0.365$, consistent with
       $r\approx0.65$ m, $R_0=1.78$ m (compiler's check).
   * **Reference list.** 57 printed entries (Crossref also 57), merged into the
     bibliography under `liang-2025`; no DOIs printed. Ref. 44 is the ingested
     [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) (printed title without "a
     review of"); [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) is also cited.
     Ref. 31 (Liu et al. PPCF 60:014039, printed 2018) → `liu-2017`; ref. 39 (Duan
     et al. NF 62:042020) → `duan-2022-b` (`duan-2022` is a different work); ref.
     46 (Wesson, printed "Tokamak") → `wesson-2011`; ref. 9 (Greenfield et al.
     2001 PRL) is distinct from `burrell-2001`. Ref. 55 has a footnote marker fused
     to the title; ref. 21 prints "east".
