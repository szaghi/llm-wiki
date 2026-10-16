---
type: Source
title: "Bandaru et al. (2024) — Runaway electron fluid model extension in JOREK and ITER relevant benchmarks"
description: "Extends the JOREK current-coupled runaway-electron density model with coronal-equilibrium impurities, diffusive deuterium neutrals, the Hesslow partial-screening avalanche source and Compton and tritium seeds, and benchmarks it against GO (1D runaway-beam formation after D/Ne injection in ITER) and DINA (2D runaway-beam formation with a cold VDE in ITER)."
resource: "doi:10.1063/5.0213962"
source_kind: paper
authors: [Bandaru V., Hoelzl M., Artola F.J., Vallhagen O., Lehnen M., JOREK Team]
year: 2024
venue: "Phys. Plasmas 31:082503"
local_file: "/home/stefano/papers/mosaic/fusion-mhd-simulation/2024_Crossref_Physics_of_Plasmas_Bandaru_Runaway_electron_fluid_model_extension_in_JOREK_and_ITER_rel.pdf"
tags: [runaway-electrons, disruption, vde, impurities, neutrals, reduced-mhd, wall, free-boundary, tokamak, verification]
timestamp: 2026-10-16T23:45:00Z
---

# Summary

The paper extends the [runaway-electron fluid model](/methods/runaway-electron-fluid-model.md)
of [JOREK](/software/jorek.md) (Bandaru et al. 2019, 2021) with partially
ionized impurities in coronal equilibrium (one impurity mass density) and
a diffusive deuterium-neutral fluid, within JOREK's reduced MHD. Runaway
electrons (REs) are a separate species described only by their number
density $n_{\mathrm{RE}}$ and coupled to the MHD by current coupling: the
RE current is subtracted from the current in the resistive term of Ohm's
law and in Ohmic heating. The sources are upgraded to the Hesslow et al.
(2017–2019) avalanche model with partial screening (total free-plus-bound
electron density, an effective critical field $E_c^{\mathrm{eff}}$ and an
effective critical momentum, obtained by Newton–Raphson and a cubic
root), plus Compton and tritium-decay seeds after Martín-Solís et al.
(2017); there is no Dreicer and no hot-tail source. RE sources are
explicit, the rest of JOREK fully implicit. Two ITER-relevant benchmarks
follow. Against the 1D code GO (Vallhagen et al. 2020 cases, rerun with
matched assumptions), RE beam formation after pure-Ne and D-dominated
D+Ne injection in a circular 15 MA plasma, run in JOREK at $R_0=50$ m to
mimic 1D, agrees well in $I_p$, RE current, $T_e$ and RE current-density
profiles, with a time shift in the late $T_e$ of the D-dominated case.
Against the 2D free-boundary code DINA, simultaneous RE beam formation and
a cold [VDE](/definitions/vertical-displacement-event.md) in a 15 MA ITER
plasma with JOREK–STARWALL walls give a matched plateau RE current of
about 10 MA with a JOREK seed of 0.1–1 A against 3.8 kA in DINA
(attributed to DINA neglecting partial screening in the avalanche), a
similar vertical-motion time scale of about $2\times10^{-2}$ s, differing
internal inductance, and a vessel-resistivity scan.

# Key claims

1. **Model definition** (§II, Abstract; Eqs. 2.3, 2.8, 2.12). Only
   $n_{\mathrm{RE}}$ is evolved; REs couple to the bulk "via
   current-coupling". Stated.
2. **Why impurities matter for RE sources** (§II). Partially ionized
   impurities and neutrals make the sources "far more realistic" through
   the raised critical field and the bound electrons available to the
   avalanche, "with the latter effect dominating at high electric
   fields". Stated, attributed to Hesslow et al.
3. **Stronger beams than the previous version** (§II A). The new sources
   lead "to a much stronger RE beam formation than the previous code
   version". Stated; no side-by-side run shown.
4. **Robustness of the full collision frequencies** (§II A). High-energy
   simplified slowing-down and deflection frequencies caused failures in
   the critical-momentum iteration (negative deflection frequency,
   non-convergence at low momentum); the full expressions (Eqs. 2.16–2.17)
   "were observed to be numerically robust". Shown qualitatively, no data.
5. **Effective critical field as a cubic** (§II A 1). Eqs. 2.18–2.19
   reduce to a cubic in $E_c^{\mathrm{eff}}/E_c$, solved in closed form
   when the discriminant is non-negative and by Newton–Raphson otherwise;
   an array of initial guesses "work[s] robustly in all the simulations
   performed so far". Derived + Stated.
6. **No Dreicer source** (§II A); the Dreicer seed is negligible in these
   ITER scenarios per Vallhagen et al. (2020) and Martín-Solís et al.
   (2017) (§III A). Stated.
7. **Compton seed is worst-case** (§II A). Live-activation Compton
   dominates the long-time decay Compton source; using the burning-phase
   Compton rate during the current quench "should be strictly viewed as a
   conservative or worst-case approach". Stated.
8. **Explicit sources** (§II A). All RE source terms explicit, the rest
   fully implicit. Stated.
9. **JOREK vs GO** (§III B, Figs. 1–4). "A good match is observed" for
   $I_p$ and RE current in both cases, with a much larger RE current for
   pure Ne; RE current-density profiles a "decent match"; $T_e$ a good
   match except the late D-dominated case, "mainly a time-shift, and the
   reason for this is not fully clear"; spatio-temporal maps in "excellent
   agreement". Shown.
10. **Neutral front** (§III B, Fig. 2b). With D-dominated injection a
    neutral front moves inward from the boundary with sequential $T_e$
    flattening, driven by deuterium line-radiation feedback. Shown.
11. **RE conversion cools further** (§III B). RE formation reduces Ohmic
    heating and drives $T_e$ to about 1 eV (pure Ne). Shown.
12. **JOREK vs DINA, seed** (§IV B, Fig. 7a). The plateau RE current of
    about 10 MA matches best with JOREK seeds 0.1–1 A against 3.8 kA in
    DINA; the difference "can be largely attributed to the neglect of the
    effect of partially-ionized impurities on RE avalanche in DINA".
    Shown (match), Stated (cause).
13. **Seed insensitivity** (§IV B). A $10^{-4}$ A seed still gives about
    9.5 MA (not plotted); moderate seed reduction is ineffective in
    "strong-avalanche-gain machines like ITER". Shown (unplotted) / Stated.
14. **Plateau current rise** (§IV B). The increase of current during the
    JOREK plateau comes from vessel-current decay supplying extra electric
    field. Stated; vessel current not shown.
15. **Cold VDE time scale** (§IV B, Fig. 8). About $2\times10^{-2}$ s,
    faster the further the plateau RE current is from 15 MA; "Both the
    codes show a good match". Shown. Without an RE beam a faster VDE is
    expected (Bandaru 2019). Stated.
16. **Time-scale ordering** (§IV B). Poloidal Alfvén time
    $\sim1.1\times10^{-5}$ s, vessel L/R time $\tau_w=0.5$ s; the motion,
    much faster than $\tau_w$, is explained by a small stabilization
    parameter (Leuer 1989) that decreases with $I_p$. Stated.
17. **Internal inductance differs** (§IV B, Fig. 9a). $l_i(3)$ differs
    significantly between DINA and JOREK; attributed to the RE source
    models and possibly different integration domains. Shown / Stated.
18. **Vessel-resistivity scan** (§IV B, Fig. 9b). At nominal resistivity
    the solution has not converged to ideal-wall behaviour; reducing it by
    10 or more removes the fast vertical motion and makes halo currents
    negligible. Shown.
19. **Outlook** (§V). RE fluid plus JOREK SPI model in 3D is "in
    principle, possible"; the RE effect on pellet ablation is not yet
    included. Stated.

# Models and numerics

* **Model class.** JOREK reduced MHD (normalization of
  [Hoelzl et al. (2021)](/sources/hoelzl-2021.md)) + RE density + coronal
  impurities + diffusive D neutrals; one temperature $T$ for all species
  ($T_e$ in the radiation functions). Field and flow:
  $\mathbf B=R^{-1}\nabla\psi\times\mathbf e_\phi+(F_0/R)\mathbf e_\phi$,
  $\mathbf v=v_\parallel\mathbf b-R\nabla u\times\mathbf e_\phi-\dfrac{\nabla p_i\times\mathbf B}{n_ieB^2}$,
  $\rho=\rho_i+\rho_{\mathrm{imp}}$ (D-ion plus impurity mass density).
* **Ohm's law with current coupling** (Eq. 2.3, JOREK units):
  $$\frac{1}{R^2}\partial_t\psi=\frac{\eta}{R^2}\Big(j-c\frac{F_0}{BR}n_{\mathrm{RE}}\Big)-\frac1R[u,\psi]-\frac{F_0}{R^2}\partial_\phi u+(\text{diamagnetic terms})-\frac{\eta_h}{R}\nabla^2\Big(\frac jR\Big),$$
  i.e. the resistive term acts on $\mathbf J-\mathbf J_{\mathrm{RE}}$ with
  $|\mathbf J_{\mathrm{RE}}|=ecn_{\mathrm{RE}}$ along $\mathbf b$. The
  Ohmic heating in the pressure equation (2.8) uses the same thermal
  current squared. Vorticity (2.4) with $\varpi=\nabla\cdot\nabla_\perp u$
  and $j=\Delta^*\psi$ (2.5–2.6); continuity (2.7) and impurity
  continuity (2.10) with parallel and perpendicular diffusivities and
  ionization/recombination sources; parallel momentum (2.9).
* **Neutrals** (Eq. 2.11): diffusion only, with ionization and
  recombination sinks/sources. Impurity charge states from coronal
  equilibrium (Mosher 1974; see
  [coronal-equilibrium impurity model](/methods/coronal-equilibrium-impurity-model.md)),
  a single impurity mass density, and a conversion factor
  $(m_i/m_{\mathrm{imp}})\langle Z\rangle-1$ from impurity mass density to
  electron-density contribution.
* **RE density** (Eq. 2.12):
  $$\partial_tn_{\mathrm{RE}}=-\alpha_{\mathrm{adv}}\,\frac{c}{F_0R}\Big([Rn_{\mathrm{RE}},\psi]+F_0\partial_\phi n_{\mathrm{RE}}\Big)+(1-\alpha_{\mathrm{adv}})\nabla\cdot(D_{\parallel,\mathrm{RE}}\nabla_\parallel n_{\mathrm{RE}})+R[n_{\mathrm{RE}},u]+2n_{\mathrm{RE}}\partial_Zu+S_{\mathrm C}+S_{\mathrm{T}}+S_{\mathrm{av}},$$
  where $\alpha_{\mathrm{adv}}\in[0,1]$ (the RE advection factor; not in the registry)
  blends parallel advection at $c$ with a large parallel diffusivity;
  perpendicular RE transport is $\mathbf E\times\mathbf B$ only.
* **Avalanche** (Eqs. 2.13–2.17, Hesslow et al.):
  $$\Gamma_{\mathrm{av}}=\frac{e}{m_ec\ln\Lambda_c}\,\frac{n_e^{\mathrm{tot}}}{n_e}\,\frac{E_\parallel-E_c^{\mathrm{eff}}}{\sqrt{4+(\text{normalized slowing-down}\times\text{deflection frequency at the critical momentum})}},$$
  with $n_e^{\mathrm{tot}}$ free plus bound electrons, the relativistic
  Coulomb logarithm $\ln\Lambda_c$, and the Connor–Hastie field
  $E_c=n_ee^3\ln\Lambda_c/(4\pi\varepsilon_0^2m_ec^2)$ (Eq. 2.14). The
  effective critical momentum solves a fixed-point relation (Eq. 2.15) by
  Newton–Raphson; the frequencies include partial screening through
  per-charge-state bound-electron counts, mean excitation energies and
  effective ion sizes.
* **Effective critical field** (Eqs. 2.18–2.19) includes synchrotron and
  bremsstrahlung losses; reduced to a cubic (claim 5).
* **Seeds.** Tritium $\beta$-decay above the critical energy (Martín-Solís
  2017; Fülöp 2020; half-life ≈4500 days, endpoint 18.6 keV); Compton
  scattering of a parametrized $\gamma$ spectrum on all (free and bound)
  electrons with the Klein–Nishina cross section integrated above the
  critical angle.
* **Resistivity.** GO benchmark: Spitzer with the Hirshman (1978)
  $Z_{\mathrm{eff}}$ fit; DINA benchmark: $\eta=\eta_{\mathrm{Sp}}Z_{\mathrm{eff}}$.
* **VDE growth rate** (Leuer 1989): $\gamma$ equals $1/\tau_w$ divided by
  (stabilization parameter $-1$), the stabilization parameter exceeding 1.
* **Numerics.** JOREK fully implicit; RE sources explicit; per-point
  Newton–Raphson for the critical momentum and field. Spatial
  discretization (Bézier FEM) not described here. Free boundary and
  resistive walls through JOREK–STARWALL
  ([resistive-wall coupling](/methods/resistive-wall-coupling.md)). All
  runs axisymmetric. No mesh, time step, harmonics, parallelism or cost
  given.
* **Boundary conditions.** GO benchmark: ideal wall at the plasma
  boundary, $T=1$ eV fixed there. DINA benchmark: free boundary with ITER
  structures (vessel inner and outer shells, $\eta_w=0.8\times10^{-6}$ Ω m,
  6 cm each; PF1–6, CS1–6 and further conductors).

# Tests and results

**Benchmark 1, JOREK vs GO (1D)** (§III, Table I, Figs. 1–4).

* Circular 50/50 DT plasma, $R_0=6$ m, $a=2$ m, $I_p=15$ MA,
  $n_e=10^{20}$ m⁻³, current density $1.69[1-(r/a)^2]^{0.41}$ MA m⁻²,
  $T_e=20[1-(r/a)^2]$ keV; JOREK at $R_0=50$ m; flux-surface-averaged
  comparison.
* Uniform D+Ne at $t=0$. Case A: $n_{\mathrm D}/n_{e0}=0$,
  $n_{\mathrm{Ne}}/n_{e0}=1$. Case B: 7 and 0.08.
* Phase 1 (6 ms): imposed exponential cooling with 1 ms time constant to
  a 50 eV floor (core ≈100 eV). Phase 2: self-consistent thermal evolution;
  perpendicular heat diffusivity 0.4 m² s⁻¹ ($\kappa_\perp=4\times10^{19}$
  m⁻¹ s⁻¹).
* JOREK settings: $u=0$, $v_\parallel=0$, no diamagnetic terms; viscosity
  $5.16\times10^{-6}$ kg m⁻¹ s⁻¹; particle diffusivities 0.015 m² s⁻¹; RE
  parallel diffusivity 1.54 m² s⁻¹; $\kappa_\parallel=1.5\times10^{26}$
  m⁻¹ s⁻¹; advection factor $10^{-3}$.
* GO reruns with coronal equilibrium, fixed boundary $T$ and an ideal wall
  at the plasma boundary; the changes from Vallhagen et al. (2020) were
  "found to be significant".
* Results: claims 9–11. $T_e$ settles at 6–9 eV, then about 1 eV after RE
  conversion. No plateau values quoted in the text.

**Benchmark 2, JOREK vs DINA (2D)** (§IV, Figs. 5–9).

* Elongated ITER free-boundary equilibrium, $I_p=15$ MA, uniform
  $n_e=10^{19}$ m⁻³, core $T_e\approx15$ keV, $q_0\approx1$, edge
  $q\approx3.7$.
* 0–1.5 ms near-equilibrium; 1.5–2 ms artificial cooling
  ($\kappa_\perp=1.27\times10^{24}$ m⁻¹ s⁻¹) to core $T_e\approx20$ eV, with
  parallel conduction raised to suppress halo currents; at 2 ms uniform Ne
  inside the LCFS ($4.88\times10^{22}$ atoms,
  $n_{\mathrm{imp}}=0.62\times10^{20}$ m⁻³) and a one-off RE seed (no
  continuing tritium or Compton).
* DINA tracks charge states with large radial charge-state diffusion; a
  "DINA-C" run mimics coronal equilibrium; DINA neglects partial
  screening. JOREK: neutrals not evolved; particle diffusivities 1.54
  (parallel) and 6.2 (perpendicular) m² s⁻¹; viscosity $0.52\times10^{-6}$;
  $\kappa_\perp=0.4\times10^{20}$, $\kappa_\parallel=1.5\times10^{26}$
  m⁻¹ s⁻¹; advection factor 0; RE parallel diffusivity
  $1.54\times10^8$ m² s⁻¹.

| Seed | Code | Plateau RE current |
|---|---|---|
| $10^{-4}$ A | JOREK | ≈9.5 MA (not plotted) |
| 0.1–1 A | JOREK | ≈10 MA (best match) |
| 100 A | JOREK | shown, higher |
| 3.8 kA | DINA, DINA-C | ≈10 MA (DINA-C slower decay) |

* $T_e$ drops to about 2 eV, nearly uniform; reasonable agreement; DINA-C
  oscillates for $t\approx3$–8 ms (not plotted). Halo current negligible.
* Upward cold VDE continuing through the plateau to termination; time
  scale about $2\times10^{-2}$ s in both codes.

# Notation map

| Bandaru et al. (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $R$, $Z$, $\phi$, $\hat{\mathbf e}_\phi$, $\hat{\mathbf b}$ | $R$, $Z$, $\phi$, $\mathbf e_\phi$, $\mathbf b$ | JOREK normalized units ($\mu_0=1$, not restated) |
| $\psi$, $F_0$, $u$, $j=\Delta^*\psi$ | $\psi$, $F_0$, $u$, $j$ | $\psi$ per radian (JOREK convention, not stated); $F_0u$ is the electric potential |
| $\mathbf u$ (mass-averaged velocity) | $\mathbf v$ | **collision:** native $u$ is also the stream function |
| $\omega=\nabla\cdot(\nabla_\perp u)$ | $\varpi$ | **collision:** registry $\omega$ is a frequency |
| $\rho$, $\rho_i$, $\rho_{\rm imp}$, $\rho_n$ | $\rho$; words; words; $m_in_{\mathrm N}$ | |
| $p$, $T$, $T_e$ | $p$, $T$, $T_e$ | one temperature |
| $\eta$, $\eta_h$ | $\eta$, $\eta_h$ | |
| $\tau_{IC}$ | words (diamagnetic factor) | zero in both benchmarks |
| $\mu$, $\mu_\parallel$ | $\nu$, words | **collision:** registry $\mu$ is the magnetic moment |
| $k_\perp$, $k_\parallel$ ($\kappa$ in text) | $\kappa_\perp$, $\kappa_\parallel$ | density × diffusivity units |
| $\gamma$ | $\Gamma$ (Eq. 2.8); words (Lorentz factor); $\gamma$ (VDE growth rate) | **collision:** triply overloaded |
| $D_{\parallel,D}$, $D_{\perp,D}$, $D_{\parallel,\rm imp}$, $D_{\perp,\rm imp}$, $D_{DN}$, $D_{\parallel,RE}$ | $D_\parallel$, $D_\perp$ with words; $D_{\mathrm N}$; $D_{\parallel,\mathrm{RE}}$ | |
| $\beta_{\rm imp}$ | words | **collision:** registry $\beta$ is plasma beta |
| $\langle\sigma v\rangle_{\rm ion,J}$, $\langle\sigma v\rangle_{\rm rec,J}$ | $\langle\sigma v\rangle_{\mathrm{ion}}$, $\langle\sigma v\rangle_{\mathrm{rec}}$ | JOREK-normalized |
| $L_{\rm rad}$, $L_{\rm rad,Dcont}$, $L_{\rm rad,Drays}$ | words; feed $P_{\mathrm{rad}}$ | |
| $n_r$, $n_{RE}$ | $n_{\mathrm{RE}}$ | |
| $c\frac{F_0}{BR}n_r$ | toroidal part of $\mathbf J_{\mathrm{RE}}$ | $e=1$ in JOREK units |
| $f$ (Eq. 2.12) | $\alpha_{\mathrm{adv}}$ above (not in registry) | **collision:** native $f$ is also the tritium fraction and the VDE stabilization parameter; registry $f_s$ is a distribution function |
| $S_{\rm Compton}$, $S_{\rm Tritium}$, $S_{\rm Avalanche}$ | $S_{\mathrm C}$, $S_{\mathrm T}$, $S_{\mathrm{av}}=\Gamma_{\mathrm{av}}n_{\mathrm{RE}}$ | |
| $\Gamma$ (avalanche rate) | $\Gamma_{\mathrm{av}}$ | **collision:** registry $\Gamma$ is the ratio of specific heats |
| $n_e$, $n_e^{\rm tot}$ | $n_e$, words | free vs free + bound |
| $E_\parallel$, $E_c$, $E_c^{\rm eff}$ | $E_\parallel$, $E_c$, $E_c^{\mathrm{eff}}$ | |
| $p$, $p_\star$ | words (normalized momentum, effective critical momentum) | **collision:** registry $p$ is pressure |
| $\bar\nu_s$, $\bar\nu_D$ | words | **collision:** registry $\nu$ is viscosity |
| $\ln\Lambda_c$, $\ln\Lambda_0$, $\ln\Lambda^{ee}$, $\ln\Lambda^{ei}$ | $\ln\Lambda$ with subscript $c$ (relativistic variant); words | |
| $\beta=p^2/(1+p^2)$ | words | **collision** with plasma beta |
| $\epsilon_0$ | $\varepsilon_0$ | |
| $\tau_{A,pol}$, $\tau_{L/R}$ | words, $\tau_w$ | |
| $\eta_{w,\rm fact}$ | words (vessel-resistivity multiplier) | |
| $l_i(3)$ | $l_i$ | the "(3)" definition |

# Pages created or updated

Chunk 1 (2026-10-16) created every page of the bundle; chunks 2 and 3 (2026-10-16) extended many. This source is cited on:

* [Coronal-equilibrium impurity model](/methods/coronal-equilibrium-impurity-model.md)
* [Disruption: phases, current quench and current spike](/definitions/disruption.md)
* [Fluid neutral models and plasma–neutral atomic sources](/methods/fluid-neutral-models.md)
* [Free-boundary and resistive-wall coupling](/methods/resistive-wall-coupling.md)
* [Halo current](/definitions/halo-current.md)
* [Implicit time integration and preconditioned Krylov solvers for nonlinear MHD](/methods/implicit-time-integration.md)
* [ITER runaway-electron benchmarks (JOREK–GO, JOREK–DINA)](/benchmarks/iter-runaway-electron-benchmarks.md)
* [JOREK](/software/jorek.md)
* [M3D-C1](/software/m3d-c1.md)
* [NIMROD](/software/nimrod.md)
* [Operator splitting and Newton–Krylov treatment of atomic-physics sources](/methods/operator-splitting-of-atomic-sources.md)
* [Reduced MHD for tokamaks](/methods/reduced-mhd.md)
* [Runaway electrons and their generation mechanisms](/definitions/runaway-electrons.md)
* [Runaway-electron fluid model coupled to MHD](/methods/runaway-electron-fluid-model.md)
* [Shattered pellet injection and massive material injection](/definitions/shattered-pellet-injection.md)
* [STARWALL](/software/starwall.md)
* [Thermal quench](/definitions/thermal-quench.md)
* [Vertical displacement event (hot and cold VDE)](/definitions/vertical-displacement-event.md)

# Citations

1. `/home/stefano/papers/mosaic/fusion-mhd-simulation/2024_Crossref_Physics_of_Plasmas_Bandaru_Runaway_electron_fluid_model_extension_in_JOREK_and_ITER_rel.pdf`.
   * **Version.** Publisher version of record (AIP, CC BY 4.0) with an
     AIP cover page; 14 PDF pages = cover + article pp. 082503-1 to
     082503-13. Submitted 15 Apr 2024, accepted 9 Jul 2024, online 2 Aug
     2024. Lehnen is marked "Deceased before publication".
   * **Identity.** doi:10.1063/5.0213962, checked on Crossref: Phys.
     Plasmas 31(8), article 082503, issued 2024-08-01; authors Bandaru,
     Hoelzl, Artola, Vallhagen, Lehnen and the JOREK Team; reference count
     30.
   * **How read.** Full text; Eqs. 2.3–2.12 verified on rendered pages
     (pp. 2–3); the source-term formulas of §II A transcribed from the
     text. Plot values are approximate readings. Scope note: the paper
     has no Dreicer and no hot-tail source; those mechanisms appear only
     as represented by the artificial DINA seed or as neglected in the GO
     benchmark.
   * **Recorded as printed.**
     * The Introduction places the GO and DINA benchmarks in Sec. III and
       the summary in Sec. IV; the paper has GO in III, DINA in IV,
       summary in V.
     * Eq. 2.9: a term with lowercase $r^2$ where $R^2$ is used elsewhere;
       the left-hand side $\rho B^2\partial_t(\rho v_\parallel)$ carries an
       unusual extra $\rho$.
     * Eq. 2.8: the kinetic-energy source term is printed with
       $v_\parallel B^2$, dimensionally $v_\parallel^2B^2$ expected.
     * Eq. 2.8 writes $k_\perp,k_\parallel$, the text $\kappa_\perp,\kappa_\parallel$.
     * The relativistic factor printed $p^2/(1+p^2)$ is $v^2/c^2$, usually
       the square of $\beta$; Eq. 2.16 then uses its square (possible
       inconsistency with Hesslow et al.).
     * The frequency normalization defines the normalized momentum with
       $v_\parallel$ instead of the total speed.
     * The constituents of the normalized frequencies are typeset with a
       Latin $\bar v$ instead of $\bar\nu$.
     * Overloads: $f$ (advection factor, tritium fraction, VDE
       stabilization parameter), $\gamma$ (adiabatic index, Lorentz factor,
       growth rate), $u$ (stream function and mass-averaged velocity),
       $\Gamma$ (avalanche rate and photon spectrum).
     * Coulomb logarithms mix $T$ in keV and in eV.
     * §IV A promises a sensitivity study justifying the RE parallel
       diffusivity $1.54\times10^8$ m² s⁻¹ "discussed later"; none
       appears.
     * Halo currents "negligible in all cases" (§IV B) vs "drop to
       negligible values in the lower vessel resistivity cases" (Fig. 9b
       discussion): mild tension.
     * Benchmark 2 gives $\kappa_\perp=0.4\times10^{20}$ m⁻¹ s⁻¹ at
       $n_e=10^{19}$ m⁻³, i.e. a diffusivity of 4 m² s⁻¹, not stated
       (compiler's check).
     * Typos: "effecting critical electric field", "mimicing",
       "Bremmstrahlung", "time-dependant", "3.8KA".
   * **Reference list.** 30 printed entries (author–year, = Crossref
     count), merged into the bibliography under `bandaru-2024`; no DOIs
     printed. The cited Hu et al. 2021 (PPCF 63:125003, non-coronal
     impurities) is the ingested `hu-2021-b`
     ([Hu et al. (2021b)](/sources/hu-2021-b.md)); Korving 2023 is the
     ingested [Korving et al. (2023)](/sources/korving-2023.md); Hoelzl
     2021 is the ingested [Hoelzl et al. (2021)](/sources/hoelzl-2021.md).
     Collaboration authors are printed as persons ("Contributors, J.E.T."
     in Bandaru 2021, "Contributors, JET" in Hu 2018); JOREK Team mapped to
     "and others"; Hender et al. 2007 is truncated after "Gruber, O.";
     Fülöp 2020 printed with "Embreus, O, others."; Merkel & Sempf 2006 is
     an IAEA FEC paper (TH/P3-8) with URL.
