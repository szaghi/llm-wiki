---
type: Source
title: "Vignat et al. (2024) — Analysis of weak secondary waves in a rotating detonation engine using large-eddy simulation and wavenumber-domain filtering"
description: "LES of the AFRL methane–oxygen rotating detonation rocket engine with the Vreman model, finite-rate chemistry and shock sensors, validated on the MVP workshop case, with a wavenumber-domain filter that separates weak counter-rotating secondary waves and links their crossings to injector blockage and thrust modulation."
resource: "doi:10.1016/j.combustflame.2024.113387"
source_kind: paper
authors: [Vignat G., Brouzet D., Bonanni M., Ihme M.]
year: 2024
venue: "Combust. Flame 263:113387"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2024_Crossref_Combustion_and_Flame_Vignat_Analysis_of_weak_secondary_waves_in_a_rotating_detonation_en.pdf"
tags: [les, combustion, detonation, compressible, sgs-model, shock-capturing]
timestamp: 2026-10-28T07:03:00Z
---

# Summary

Vignat et al. (2024) present a
[large-eddy simulation](/definitions/large-eddy-simulation.md) of the Air
Force Research Laboratory rotating detonation rocket engine (RDRE), a
non-premixed methane–oxygen annular combustor with 72 pairs of impinging
injectors, at the "high mass flow rate" case of the Model Validation for
Propulsion (MVP) workshop ($\dot m_{\mathrm{tot}}=352$ g/s, equivalence
ratio 1.16). The solver, called CharlesX in Table 1 (a fully compressible
unstructured finite-volume code; the paper cites Khalighi et al. and Ma,
Lv & Ihme for it and names it in the table only, see
[CharLES](/software/charles.md)), combines a central and an upwind-biased
Riemann flux, two [shock and scalar sensors](/definitions/shock-sensor.md)
that switch to first-order reconstruction, the
[Vreman model](/methods/vreman-model.md) with constant 0.07, turbulent
Prandtl and Schmidt numbers 0.7, the 12-species FFCMy-12 mechanism with
no turbulence–chemistry interaction model, and a balanced operator
splitting, on a 54-million-cell grid. The LES gives two co-rotating
detonation waves where the experiment shows three and under-predicts the
wave speed by 24% (every group's LES does, by up to 30%), but predicts
thrust within 3.1%, specific impulse within 6.6% and wall pressures
within 5%. Table 1 surveys the subgrid treatments other groups used for
the same engine: a one-equation transport model
([one-equation subgrid kinetic-energy models](/methods/subgrid-kinetic-energy-equation-model.md),
one run in [ANSYS Fluent](/software/ansys-fluent.md)), dynamic
Smagorinsky ([dynamic procedure](/methods/dynamic-procedure.md)), and
grid dissipation only ([implicit LES](/definitions/implicit-les.md)). The
SGS model choice is stated, not studied, and the authors call the
adequacy of subgrid models for highly compressible reacting flow open.

The second contribution is wavenumber-domain filtering (WDF), inline
here: a sector-averaged azimuth–time diagram is Fourier transformed in
time and azimuth, split into $k=0$ (longitudinal), $k>0$ (clockwise) and
$k<0$ (counter-clockwise) parts, and transformed back. It isolates weak,
intermittent counter-rotating waves whose crossings with the main
detonations create high-pressure regions precessing by 40°–60° per
rotation. Injector responses sorted by oxidizer-velocity deficit show
that the most blocked fifth has a 24% higher detonation pressure peak and
a 13.9% higher pressure-gain thrust term. Turbulence content is marginal
to the bundle.

# Version read

Version of record (Elsevier; received 12 November 2023, accepted 23
February 2024, online 2 March 2024), 15 pages, all read. The
Supplementary Material (uncertainty methodology) is not in the file and
was not read. Page 1 matches the metadata; no identity issue. Equation,
table and section numbers are those of this version.

# Key claims

Page-local symbols: $\dot m_{\mathrm{tot}}$ total mass flow; $\theta$
azimuth; CW and CCW clockwise (advancing in $-\theta$) and
counter-clockwise waves; $k$ the azimuthal wavenumber and $f$ the
frequency of WDF (not the turbulent kinetic energy); $U_{\mathrm{det}}$
detonation speed; $F_{\mathrm I}$, $F_{\mathrm{II}}$, $F_y$ pressure-gain,
injection and total axial thrust terms of a sector; $f_{\mathrm{CW}}$,
$f_{\mathrm{CCW}}$, $\delta f=f_{\mathrm{CCW}}-f_{\mathrm{CW}}$,
$f_{\mathrm{thrust}}$, $N_{\mathrm{CW}}$ spectral peaks, their difference,
the thrust peak and the number of CW waves.

1. The grid has 54 million control volumes: 58 μm inside the injectors, 50–100 μm in the lower chamber where detonations occur, 300 μm in the upper chamber; it does not resolve shock–turbulence interaction but is claimed to capture the essential dynamics because of finite mixing and the thickened detonation structure (§3.1). **Stated**
2. With the production mesh most jets have a subgrid turbulent-kinetic-energy share $k_{\mathrm{sgs}}/k_{\mathrm{tot}}$ below 20%, "as recommended by Pope [47]", assessed on single-injector-pair simulations (no figure) (§3.1). **Shown**
3. The SGS viscosity $\mu_t$ comes from the Vreman model with constant $C=0.07$, "as specified in the original paper [53]"; $Pr_t$ and the turbulent Schmidt number are both 0.7 (§3.3). **Stated**
4. Previous simulations of this RDRE used a transport-equation SGS model [39, 42, 44, 54], dynamic Smagorinsky [43, 45], or no reported SGS closure [22, 55]; Pal et al. [56] found that different turbulence models did not significantly change the detonation speed (§3.3). **Stated**
5. A modelling framework for highly compressible, turbulent, reacting flows is still lacking, and the adequacy of subgrid models for such flows is open (§3.3, §3.8). **Stated**
6. FFCMy-12 against GRI3.0 at 0.1 MPa, 300 K, equivalence ratio 1: the Chapman–Jouguet speed differs by 0.04% and the post-detonation pressure by 0.25% (Shock and Detonation Toolbox) (§3.4). **Shown**
7. Splitting with a fourth-order semi-implicit Rosenbrock–Krylov integrator for the reactions and third-order SSP Runge–Kutta for advection and diffusion permits a typical convective time step of 4.3 ns (§3.4). **Stated**
8. Reaction rates are evaluated from the filtered variables without a turbulence–chemistry interaction model, a shortcoming that may affect the number of waves and their speed (§3.4). **Stated**
9. Outside the sensor regions reconstruction and flux are fully conservative, fourth-order on uniform and third-order on non-uniform meshes [49]; sensor-active cells use first-order reconstruction (§3.5). **Stated**
10. Walls are no-slip and adiabatic; boundary layers are not resolved; adiabatic walls are "likely" inadequate, but no wall-temperature data exist (§3.6). **Stated**
11. Inlet and outlet use LODI characteristic conditions with relaxation giving a cut-off of 800 Hz, far below the first longitudinal oxidizer-manifold mode ($\approx3745$ Hz); a Bogey et al. sponge starts 30 mm downstream of the chamber exit (§3.6). **Stated**
12. A prior cold-flow run (15 flow-through times, coarse mesh) was needed to obtain stable detonations; after more than 1 ms without mode transition, statistics were collected over 0.75 ms, about four revolutions of each wave (§3.7). **Shown**
13. Table 2, LES against experiment: 2 against 3 waves; $U_{\mathrm{det}}=1264$ against 1668 m/s ($-24\%$); CTAP1 0.522 against 0.497 MPa (4.9%); CTAP2 0.422 against 0.431 MPa ($-2.2\%$); thrust 603.5 against 585.4 N (3.1%); specific impulse 175 against 164 s (6.6%); oxygen plenum 1.53 against 1.44 MPa (+5.6%); fuel plenum 1.68 against 1.49 MPa (+13%) (§3.9). **Shown**
14. All LES of this operating condition under-predict the mean detonation speed, by up to 30%; wave speed, wave number and thrust are not tightly correlated (§3.9, citing [68], [42]). **Shown** (inter-group comparison) / **Stated**
15. The number of waves at steady state depends on the initialization (Prakash [40]); the MVP ignition-kernel procedure creates a counter-rotating pair, while the experiment used a pre-detonator tube (§3.9). **Stated**
16. WDF separates CW and CCW components with forward and inverse Fourier transforms only; it does not separate the contributions of non-linear CW–CCW interactions (§4, Fig. 2). **Derived**
17. Two CW detonations about 160° apart (asymmetric pattern), heat release rate up to 300 GW m$^{-3}$; weak, intermittent CCW secondary waves with a pressure peak "at most three times smaller" than the CW waves (§5.1, Fig. 3). **Shown**
18. CW–CCW crossings produce high-pressure, high-heat-release regions precessing clockwise by 40°–60° per full rotation of the strong waves (§5.1). **Shown**
19. The penetration of the cold reactant jets grows almost linearly with the distance from the previous detonation, up to 13 mm; the high-pressure region behind the shock spans about eight injectors (40°) (§5.2, Fig. 4). **Shown**
20. Oxidizer and fuel plenum pressures fluctuate by 4.2 and 12 kPa peak-to-peak: the plenums are decoupled from the chamber, and the injector dynamics are attributed solely to the chamber waves (§5.3). **Shown**
21. No backflow occurs in either injector; the injector velocity drops by up to 27% (oxidizer) and 21% (fuel) from its pre-detonation value (§5.3). **Shown**
22. Of 375 injector responses sorted by the velocity deficit of Eq. (10), the "low blockage" and "high blockage" quintiles (75 each) have mean deficits of 4% and 23% (oxidizer) and 3% and 14% (fuel) (§5.3). **Shown**
23. The high-blockage population has a 0.21 MPa (24%) higher detonation pressure peak and a 29% higher peak heat release rate; its pre-detonation progress variable is 13% lower (better reactant filling, less secondary combustion) (§5.3, Fig. 7). **Shown**
24. Per-sector thrust, low against high blockage (Table 3): $F_{\mathrm I}$ 1.8 against 2.1 N (13.9%), $F_{\mathrm{II}}$ 5.7 against 5.6 N ($-1.6\%$), $F_y$ 7.5 against 7.8 N (6.6%) (§5.4). **Shown**
25. $F_{\mathrm{II}}$ is almost constant while $F_{\mathrm I}$ fluctuates by 30% peak-to-peak of its mean; the total thrust fluctuates by 7.4% peak-to-peak; interaction intervals coincide with systematic thrust increases (§5.4, Fig. 9). **Shown**
26. Spectra give $f_{\mathrm{CCW}}=13.4\pm1.3$ kHz (broad) and $f_{\mathrm{CW}}=12\pm1.3$ kHz, a precession $\delta f/f_{\mathrm{CW}}\approx42°$ per cycle, and a thrust peak $f_{\mathrm{thrust}}=20\pm1.3$ kHz explained as a modulation $f_{\mathrm{thrust}}=N_{\mathrm{CW}}(f_{\mathrm{CW}}-\delta f)$ (§5.4). **Shown** / **Derived** *(compiler check, not in the sources: $1.4/12\times360°=42°$; $2(12-1.4)=21.2$ kHz, inside the printed $\pm1.3$ kHz band)*
27. Whether secondary waves benefit the overall thrust is open; they are a mechanism for non-constant thrust and engine vibration (§5.4, §6). **Stated**

The governing equations (Eqs. 1–7) are the Favre-filtered reacting
compressible Navier–Stokes equations with a combined molecular and eddy
viscosity stress, $(\bar\mu+\mu_t)[\nabla\tilde{\boldsymbol u}+(\nabla\tilde{\boldsymbol u})^T]-\tfrac23(\bar\mu+\mu_t)(\nabla\cdot\tilde{\boldsymbol u})\boldsymbol I$,
that is $\bar\rho\tau^d_{ij}=-2\mu_t\tilde S^d_{ij}$ in registry form
([Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md)), with no
separate isotropic subgrid part; the Vreman formula itself is not printed.
The WDF steps (Fig. 2) are a temporal transform
$\int\Phi(\theta,t)e^{-i2\pi ft}\,\mathrm dt$, an azimuthal transform
$\int\Phi(\theta,f)e^{-ik\theta}\,\mathrm d\theta$, the inverse azimuthal
transform restricted to $k>0$ (CW) or $k<0$ (CCW), and the inverse
temporal transform, with $\Phi$ a quantity volume-averaged over a 1°
sector ($z=0$–20 mm, $r=31.3$–36.3 mm). The sector thrust (Eqs. 11–14,
after Shepherd & Kasahara and Schwer & Kailasanath) is
$F_y=F_{\mathrm I}+F_{\mathrm{II}}-F_{\mathrm{III}}$, the wall-friction
term $F_{\mathrm{III}}$ being neglected.

# Printed slips

- **§3.9:** "Pal et al. [43] reported two detonation waves in their LES", while Table 2 lists 3 waves for Pal et al. and the same section says their simulation "transitioned to three co-rotating detonation waves" and "correctly predicts the number of waves".
- **§5.3 (p. 9):** "The velocity inside the oxidizer injector can decrease by up to 27% compared to its pre-detonation value ($\overline{V_{inj,fuel,k}}(\theta-\theta_{det}=0)=365$ m s$^{-1}$), and by up to 21% in the fuel injectors ($\overline{V_{inj,ox,k}}(\theta-\theta_{det}=0)=257$ m s$^{-1}$)": each subscript names the other injector than its clause, and §2 gives nominal velocities of 304 m/s (oxidizer) and 390 m/s (fuel).
- **Table 2, oxygen plenum:** 1.53 against 1.44 MPa printed "+5.6%". *(Compiler check, not in the sources: $1.53/1.44-1=6.25\%$, and $5.9\%$ with the lowest value that rounds to 1.53.)*
- **Table 3, total thrust:** $F_y$ 7.5 against 7.8 N printed "6.6%", repeated in the text. *(Compiler check, not in the sources: the rounded values allow $7.75/7.55-1=2.6\%$ to $7.85/7.45-1=5.4\%$; the printed component differences, $+13.9\%$ of 1.8 N and $-1.6\%$ of 5.7 N, add to $(0.25-0.09)/7.5\approx2.1\%$.)*
- **§5.2, phase definition:** "$\theta-\theta_{det}(t)=\max_i(\theta-\theta_{det,i}(t))$ … the azimuthal angle to the closest detonation wave following the CW direction". *(Compiler check, not in the sources: with the differences taken in one sense, the printed maximum over the waves selects the farthest wave, not the closest; the paper states no modulo-360° convention that would reconcile the two.)*
- **§3.4 and §3.2:** the mechanism is "12-species" while "$N_s=13$ is the number of species in the LES"; the paper does not say what the thirteenth species is.
- **Eq. (8)** prints "maxarg" for the argument of the maximum.
- **Fig. 3 caption** "A black dashed line is used in (a)" against §5.1 "black dashed–dotted line"; **Fig. 6 caption** writes "(t − θ)" where the rest of the paper writes "θ − t".
- **§3.2** calls the overbar "Reynolds filtering" and the combined viscous and subgrid stress the "Reynolds-averaged stress tensor" in an LES.
- **Ref. [30]** prints "Proc. Combust. Inst. 3 (2023) 2875–2883" (recorded as printed in the bibliography).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar{(\cdot)}$ ("Reynolds filtering") | $\bar\phi$ | LES filter, unweighted; not a Reynolds average |
| $\tilde{(\cdot)}$ | $\tilde\phi$ | Favre filter |
| $\bar{\boldsymbol\tau}_{\nu+t}$ | $\sigma_{ij}-\bar\rho\tau^d_{ij}$ | viscous plus modelled subgrid stress, entering as $+\nabla\cdot$; $\bar\rho\tau^d_{ij}=-2\mu_t\tilde S^d_{ij}$ |
| $\bar\mu$, $\mu_t$ | $\mu$, $\mu_t$ | molecular and SGS (Vreman) viscosity |
| $C=0.07$ | Vreman prefactor | the [Vreman](/methods/vreman-model.md) page records the prefactor $2.5C_s^2$ of Agrawal et al. |
| $\bar\lambda_T$, $\lambda_{T,t}$ | (thermal conductivity, SGS conductivity) | **collision** with the Taylor microscale $\lambda$ |
| $\bar D_k$, $D_{k,t}$; $Sc_t$ | (molecular and SGS species diffusivities); turbulent Schmidt number | $Pr_t=Sc_t=0.7$ |
| $\tilde Y_k$, $\bar{\dot\omega}_k$, $k$ (species) | (mass fraction, source term) | **collision:** $k$ is also the wavenumber and an injector index; $\dot\omega_k$ is not the specific dissipation rate |
| $\tilde e_{tot}$ | (specific total energy) | the registry's $E$ is per unit volume |
| $k$, $f$ (WDF) | $k$, $f$ (page-local) | azimuthal wavenumber, frequency; **collision** with the turbulent kinetic energy |
| $\phi$, $\varphi$ | (equivalence ratio) | $\phi$ also a generic quantity |
| $\Phi$, $\bar\Phi$ (Fig. 2) | $\Phi$ (page-local) | sector average, not an LES filter |
| $\theta$ | $\theta$ (page-local azimuth) | **collision** with the momentum thickness |
| $F_I$, $F_{II}$, $F_{III}$, $F_y$ | $F_{\mathrm I}$, $F_{\mathrm{II}}$, $F_{\mathrm{III}}$, $F_y$ (page-local) | |
| $\tau_w$ | $\tau_w$ | wall shear stress (neglected term) |
| $\tau_{mix}$ | (mixing time of the RDRE) | not the PaSR $\tau_{\mathrm{mix}}$ of §11 |

# Reference list

74 printed references, numbered style, merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Same-author
same-year works are keyed in printed order (Bennewitz 2019 and 2021,
Lietz 2019, Prakash 2020 and 2021, Pal 2021). Ref. [40] (Prakash, PhD
thesis, University of Michigan, 2022) is a different work from the
ingested source `prakash-2022` and is keyed `prakash-2022-d`. Ref. [37]
prints no author (entered under the MVP workshop as corporate author);
[52] (Cantera), [58] (Shock and Detonation Toolbox) and [59] (GRI-Mech
3.0, an author printed "J. William C. Gardiner") are software or web
items; [30] prints volume "3". No item is unparseable.

# Pages created or updated

Chunk 13 (2026-10-28). This source is cited on:

- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Shock sensors and troubled-cell indicators](/definitions/shock-sensor.md)
- [Turbulent Prandtl number and turbulent heat-flux models](/definitions/turbulent-prandtl-number.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [One-equation subgrid kinetic-energy models](/methods/subgrid-kinetic-energy-equation-model.md)
- [Vreman model](/methods/vreman-model.md)
- [ANSYS Fluent](/software/ansys-fluent.md)
- [CharLES](/software/charles.md)
