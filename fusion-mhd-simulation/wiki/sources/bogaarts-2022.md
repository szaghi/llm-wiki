---
type: Source
title: "Bogaarts et al. (2022) — Development and application of a hybrid MHD-kinetic model in JOREK"
description: "Extends JOREK's full-f particle module with an anisotropic (CGL) pressure-coupling term that feeds full-orbit energetic-particle markers into the reduced and full MHD models, adds a kernel-based phase-space resonance diagnostic, benchmarks it linearly on ITPA-TAE and AUG-NLED, and applies it to ASDEX Upgrade discharge #31213."
resource: "doi:10.1063/5.0119435"
source_kind: paper
authors: [Bogaarts T.J., Hoelzl M., Huijsmans G.T.A., Wang X., JOREK Team]
year: 2022
venue: "Phys. Plasmas 29:122501"
local_file: "/home/stefano/papers/mosaic/fusion-mhd-simulation/2022_Crossref_Physics_of_Plasmas_Bogaarts_Development_and_application_of_a_hybrid_MHD-kinetic_model_in.pdf"
tags: [hybrid-kinetic, energetic-particles, alfven-eigenmode, particles, reduced-mhd, full-mhd, finite-elements, code, benchmark]
timestamp: 2026-10-16T00:00:00Z
---

# Summary

The paper extends the full-f particle-in-cell module of
[JOREK](/software/jorek.md) with an anisotropic
[pressure-coupling](/methods/pressure-and-current-coupling.md) scheme for
energetic particles (EPs). The EP pressure tensor, approximated in CGL
(gyrotropic) form from its parallel and perpendicular components, is
deposited from full-orbit, Boris-pushed markers onto the finite-element grid,
averaged over an MHD step and added as an explicit perpendicular force in the
implicitly advanced momentum equation, in both the reduced and the full MHD
models. Current coupling was implemented but "too noisy to obtain useful
results", and the full (non-CGL) tensor "unstable and noisy". A kernel-density
phase-space diagnostic (finite-support kernels replacing δ-functions)
visualizes resonances, with a least-squares gyro-oscillation fit removing
dipole artefacts in $(v_{\parallel p},\mu)$. Linear benchmarks: the ITPA
$n=6$ TAE (full MHD; "reasonable agreement" with other FLR codes, JOREK lower
in growth rate and lowest in frequency) and the AUG-NLED $n=1$ energetic
particle mode (reduced MHD; good agreement in drive versus gradient, mode
structure and continuum position, frequency off). The full-f Maxwellian
initial distribution relaxes, because it is not a function of the constants
of motion, whereas the other codes switch relaxation off, which prevents a
one-to-one comparison. Applied to eight time slices of AUG #31213 with a
NUBEAM distribution, the model finds three regimes ($m=3$ EPM, $m=2,3$ TAE,
$m=2$ RSAE); $t\le0.7$ s and $t\ge0.9$ s match the Mirnov spectrogram,
0.75–0.84 s do not, attributed to $q$-profile uncertainty. Nonlinear use is
left to future verification.

# Key claims

1. **Coupling term** (§II, Eq. 2). EPs enter the momentum equation as
   $-(\nabla\cdot\mathsf P_h)_\perp$. Stated (model definition).
2. **Current coupling too noisy** (§II, p. 4). "Has been implemented as well
   … but was too noisy to obtain useful results". Stated, citing the
   Dvornova thesis; no evidence shown here.
3. **CGL closure** (§II, p. 4). The full pressure tensor "proved to be
   unstable and noisy", so the gyrotropic $p_{\parallel h}$, $p_{\perp h}$
   form is used throughout. Stated.
4. **Explicit EP, implicit MHD** (§II, p. 5). The EP term is explicit and
   averaged over an MHD step while the bulk MHD stays implicit, "a common
   strategy across different hybrid codes". Stated.
5. **Smoothing harmless** (§II, pp. 4–5). Projection smoothing is "always
   chosen small enough not to affect physical results". Stated, with the
   impact studied elsewhere.
6. **Both models** (§II, §VI). Coupling implemented in full and reduced MHD.
   Stated.
7. **Full orbit** (§II, p. 4). The Boris pusher retains all finite-orbit-width
   and FLR effects; EP collisions are neglected. Stated.
8. **ITPA-TAE convergence** (§IV A, Fig. 2). At $T_h=700$ keV the growth rate
   varies within 5% over $2\times10^7$–$2\times10^8$ markers and 50–200
   particle steps per gyro-orbit. Shown (spreads ≈0.975–1.027 and
   ≈0.993–1.003).
9. **ITPA-TAE agreement** (§IV A, Fig. 3). Growth rates and frequencies
   versus $T_h$ in "reasonable agreement" with the other FLR-including codes.
   Shown; on Fig. 3, JOREK $\gamma$ lies at the lower edge of the spread for
   $T_h\gtrsim200$ keV (≈15–19 vs ≈18–28×10³ s⁻¹) and JOREK $\omega$
   (≈3.9–4.08×10⁵ rad/s) is below every other code (≈4.0–4.45).
10. **Relaxation of full-f** (§IV A, Fig. 4; §IV B). The Maxwellian relaxes
    in real and velocity space because it "cannot be expressed solely in
    terms of conserved particle quantities"; midplane EP pressure peak drops
    from ≈9.3 to ≈6.5 kPa and the $v_{\parallel p}$ distribution develops a
    dip at zero. Shown.
11. **Resonance** (§IV A, Fig. 5). Dominant ITPA-TAE resonance at $v_A/3$,
    "in agreement with" Könies et al. (2018). Shown.
12. **Nonlinear flattening** (§IV A, Fig. 6). At 400 keV the
    resonant-particle density flattens around the gap at $r=0.5a$ at
    saturation. Shown.
13. **Energy exchange** (§IV A, Fig. 7). "Although the pressure coupling
    scheme does not conserve energy exactly … energy is conserved rather well
    until the saturation phase". Shown, but Fig. 7b gives a relative
    mismatch between EP energy loss and fluid energy gain of ≈10% throughout
    the linear phase, ≈15% late; a 10× smaller dissipation lowers the late
    value only slightly.
14. **Reduced MHD for AUG-NLED** (§IV B). Used "as results agree with full
    MHD while computational costs are lower". Stated, no comparison shown.
15. **EPM identification** (§IV B, Fig. 8). From mode structure and position
    in the continuum. Shown.
16. **AUG-NLED agreement** (§IV B, Fig. 9). Good agreement with HYMAGYC, MEGA
    and ORB5 in drive versus pressure gradient, structure and continuum
    location; frequency agrees less, explained by the constant bulk ion
    density in JOREK. Shown / Stated. On Fig. 9b the JOREK frequency
    decreases with the gradient (≈148→136 kHz) while HYMAGYC and MEGA
    increase (≈150→179, ≈157→165 kHz).
17. **Phase-space resonance vs MEGA** (§IV B, Fig. 10). Both show the
    dominant resonance at $v_{\parallel p}/v_{h0}\approx-2$ and none at $+2$;
    differences attributed to full-f/full-orbit vs δf/drift-kinetic,
    relaxation and the 150 vs 165 kHz frequency gap. Shown / Stated.
18. **AUG #31213 regimes** (§V, Table I, Fig. 15). $m=3$ EPMs for $q>2.5$
    (0.6, 0.65 s); core TAE when $q$ crosses 2.5 (0.7 s); $m=2$ EPM/RSAE for
    $t\ge0.75$ s with flat core $q$. Shown.
19. **Experiment match** (§V, Fig. 16). Good match for $t\le0.7$ s and
    $t\ge0.9$ s; RSAEs predicted at 0.75–0.84 s are absent from the
    spectrogram. Shown.
20. **Cause of mismatch** (§V, Fig. 17). Core $q$ uncertainty strongly
    perturbs the core Alfvén continuum, which "could explain" the
    discrepancy. Shown (sensitivity) / Stated (attribution).
21. **Nonlinear use** (abstract, §VI). "Will require dedicated verification
    and validation left for future work". Stated.

# Models and numerics

**Base code.** JOREK: 3D nonlinear MHD in X-point geometry, implicit time
stepping, poloidal finite elements (Bézier, by reference to Hoelzl et al.
2021) and toroidal Fourier series, reduced and full models. The kinetic
module solves the kinetic equation by PIC; moments are projected onto the
finite-element representation. Pushers range from full orbit to relativistic
gyro-centre; collision, ionization, recombination and radiation models exist;
OpenMP–MPI on CPUs, OpenACC port in progress; markers from analytic profiles
or numerical distributions (NUBEAM).

**Full-f markers** (Eq. 1):
$f_h(\mathbf x,\mathbf v,t)=\sum_{p=1}^{N_p}w_p\,\delta(\mathbf x-\mathbf x_p)\,\delta(\mathbf v-\mathbf v_p)$,
with $w_p$ the number of physical particles per marker (fixed). Full-f, not
[δf](/methods/delta-f-method.md); δf appears only as MEGA's model. EPs are
pushed by a full-orbit Boris scheme in cylindrical geometry (Delzanno &
Camporeale); see [particle pushers](/methods/particle-pushers.md).

**Momentum equation** (Eq. 2), $\mathbf J$ the total current (bulk plus EP):

$$\rho\Big(\frac{\partial\mathbf v}{\partial t}+\mathbf v\cdot\nabla\mathbf v\Big)+\nabla p-\mathbf J\times\mathbf B=-(\nabla\cdot\mathsf P_h)_\perp,\qquad
\mathsf P_h=m_h\int\mathbf v\mathbf v\,f_h\,d^3v,$$

the uncentred second moment. Only the momentum equation is modified; no
change to the energy equation is stated.

**CGL approximation** (p. 4):

$$\mathsf P_h\approx p_{\parallel h}\mathbf b\mathbf b+p_{\perp h}(\mathsf I-\mathbf b\mathbf b),\qquad
p_{\perp h}=\frac{m_h}{2}\int|\mathbf v\times\mathbf b|^2f_h\,d^3v,\qquad
p_{\parallel h}=m_h\int v_{\parallel}^2f_h\,d^3v,$$

evaluated on markers with the field direction at each marker.

**Projection and time coupling.** The tensor is projected onto the fluid
finite elements with small smoothing terms, averaged over several orbits
(usually one MHD step) and applied as an explicit momentum source; the bulk
MHD stays implicit.

**Phase-space diagnostic** (§III, Eqs. 3–4). For a single-particle quantity
(e.g. energy change $\Delta\mathcal E_p$) and reduced coordinates (e.g.
$(v_{\parallel p},\mu)$), the δ-function sum over markers is replaced by a
product of one-dimensional finite-support kernels of unit integral and
bandwidth $l$, accumulated on a grid and optionally time-integrated over many
gyro-motions. The kernel shape is not specified.

**Gyro-oscillation fit** (App. A). For $\mu$ and $v_{\parallel p}$ sampled in
time, a linear least-squares fit of offset + linear trend + cosine and sine
at $\Omega_h$ (estimated from the orbit-mean $B$) gives the gyro-centre trend
at which the power exchange is deposited; inversion by Cramer's rule. A fluid
step holds only ≈5 gyro-motions, so many steps are summed.

**Equilibrium** (§V). IDA profiles imported; MHD temperature $T=T_i+T_e$ set
to reproduce the IDA pressure; $FF'$ imported; JOREK's Grad–Shafranov solver
gives discrete force balance; continua from HELENA + CASTOR. Resistivity and
viscosity fixed (temperature dependence off). Bulk mass density from the
electron minus fast-ion density, as pure deuterium. The $n=0$ component is
frozen in the nonlinear ITPA run. The AUG domain ends at the separatrix; no
other boundary conditions are stated.

**Resolution** ($\tau_A=a\sqrt{\mu_0\rho_0}/B$, central values):

| Case | MHD model | $n$ | Elements (radial × poloidal) | Markers | MHD $\Delta t$ | Particle $\Delta t$ |
|---|---|---|---|---|---|---|
| ITPA-TAE | full | 6 | 102 × 128 | 40 M (20–200 M in convergence) | $3\tau_A$ | $2\times10^{-10}$ s |
| AUG-NLED | reduced | 1 | 51 × 64 | 10 M | 0.26 µs ≈ $4\tau_A$ | $2\times10^{-10}$ s |
| AUG #31213 | not restated | 1 | 51 × 64 | 20 M | ≈$4\tau_A$ | $2\times10^{-10}$ s |

No wall-clock or core-hour costs are given.

# Tests and results

**ITPA-TAE** (§IV A). $R_0=10$ m, $a=1$ m, flat hydrogen $n_i=2\times10^{19}$
m⁻³, $q=1.71+0.16(r/a)^2$, $n=6$ gap ($m=10,11$) at $r=0.5a$, Maxwellian EPs
with scanned $T_h$; earlier JOREK work used reduced MHD with isotropic
coupling. At 400 keV, $m=10,11$ peak near $s\approx0.5$ and
$\omega\approx4\times10^5$ rad/s inside the gap (Fig. 1). Fig. 3 compares
with CAS3D-K, TAEFL, GYGLES, CKA-EUTERPE, MEGA, NOVA-K, LIGKA, EUTERPE, ORB5,
VENUS (FLR codes only): JOREK $\gamma$ peaks ≈19×10³ s⁻¹ near 400 keV at the
low side of the band; JOREK $\omega$ is the lowest. Energy exchange over
$t\in[0,10^4]\tau_A$ (Fig. 7): ≈10% mismatch in the linear phase; the frozen
$n=0$ and resistive/viscous dissipation are blamed for the nonlinear
mismatch.

**AUG-NLED** (§IV B). AUG #31213 at 0.84 s, off-axis EP peaking, isotropic
Maxwellian at 93 keV, scanned EP density; reduced MHD. $n=1$ EPM, $m=2$
dominant, near $s\approx0.2$ at ≈150 kHz, in the continuum below the TAE gap.
The post-relaxation gradient is scanned by scaling marker weights or by
modifying the initial profile.

| Code | $\gamma$ at nominal gradient [10⁵ s⁻¹] | Frequency at nominal [kHz] |
|---|---|---|
| JOREK | ≈1.7–2.1 | ≈143–150 |
| HYMAGYC | ≈1.7–2.1 | ≈179 |
| MEGA | ≈1.7–2.1 | ≈165 |
| ORB5 | ≈3.5 | ≈127 |

(Fig. 9 readings.)

**AUG #31213** (§V, Table I). NUBEAM distribution, highly anisotropic and
almost purely counter-passing, relaxing much less than the Maxwellian
(Fig. 13); reversed-shear $q$ decreasing in time, flat core ($s<0.4$) for
$t\ge0.75$ s.

| $t$ [s] | 0.6 | 0.65 | 0.7 | 0.75 | 0.8 | 0.84 | 0.9 | 0.93 |
|---|---|---|---|---|---|---|---|---|
| EPs [10¹⁹] | 1.0 | 1.0 | 1.25 | 1.25 | 1.4 | 1.4 | 1.5 | 1.5 |
| frequency [kHz] | 101 | 90 | 128 | 85 | 80 | 76 | 82 | 60 |
| $\gamma$ [10⁵ s⁻¹] | 0.5 | 0.5 | 1.0 | 1.1 | 1.8 | 1.8 | 2.3 | 1.9 |
| type | EPM | EPM | TAE | RSAE | RSAE | RSAE | RSAE | RSAE |
| $m$ | 3 | 3 | 2,3 | 2 | 2 | 2 | 2 | 2 |

Spectrogram (Fig. 11): ≈50 kHz EGAMs, 100–150 kHz rising $n=1$ Alfvénic
modes, 50–70 kHz $n=1$ RSAE.

# Notation map

| Bogaarts et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $f$, $f_h$ | $f_h$ | full-f |
| $N_p$, $w_i$, $\mathbf r_i$, $\mathbf v_i$ | $N_p$ (words), $w_p$, $\mathbf x_p$, $\mathbf v_p$ | |
| $\rho$, $\mathbf V$, $p$ | $\rho$, $\mathbf v$, $p$ | dimensional form; JOREK normalization not discussed |
| $\mathbf J_t$ | $\mathbf J$ | total (bulk + EP) current |
| $\boldsymbol\Pi_h$ | $\mathsf P_h$ | uncentred second moment |
| $p_\parallel$, $p_\perp$ | $p_{\parallel h}$, $p_{\perp h}$ | |
| $\mathbf I$ | $\mathsf I$ | |
| $m_h$, $v_\parallel$ | $m_h$, $v_{\parallel p}$ | |
| $g_i$, $\boldsymbol\xi$, $G$, $G_J$, $K_l$, $l$ | words | diagnostic quantities |
| $\Delta E_i$, $E$ | $\Delta\mathcal E_p$, $\mathcal E$ | **collision:** $E$ vs electric field |
| $\mu$, $P_\phi$ | $\mu$, $P_\phi$ | |
| $\lambda=v_\parallel/v$ | words (pitch) | printed as "pitch angle" |
| $\psi$, $\psi_N$, $s=\sqrt{\psi_N}$ | $\psi$, $\psi_N$, $s$ | $2\pi$ convention not stated |
| $FF'$ | $FF'$ | not defined in the paper |
| $T_f$ | $T_h$ | |
| $T=T_i+T_e$ | $T$ (total, as stated) | |
| $\tau_A=a\sqrt{\mu_0\rho_0}/B$, $\tau_g$ | $\tau_A$ (length $a$), words (gyro-period) | |
| $v_{h0}=\sqrt{E_h/m}$ | words (EP speed normalization) | |
| $n_b$ | $n_i$ | |
| $\alpha$, $\beta$, $\gamma$, $\delta$, $\omega$ (App. A) | words; $\Omega_h$ for $\omega=qB/m$ | **collision:** $\gamma$ growth rate, $\omega$ mode frequency, $\beta$ plasma beta; $\alpha$, $\beta$ also reused in §III |
| $\mathbf X$, $\mathbf Y$, $\phi_j$ (App. A) | words | **collision:** $\mathbf X$ guiding centre, $\phi$ toroidal angle |
| $f$ (kHz, Table I) | $\omega/2\pi$ | |

# Pages created or updated

Chunk 1 (2026-10-16) created every page of the bundle. This source is cited on:

* [Energetic particle mode (EPM) and frequency chirping](/definitions/energetic-particle-mode.md)
* [Grad–Shafranov equation](/definitions/grad-shafranov-equation.md)
* [Hybrid kinetic-MHD models](/methods/hybrid-kinetic-mhd.md)
* [HYMAGYC](/software/hymagyc.md)
* [Implicit time integration and preconditioned Krylov solvers for nonlinear MHD](/methods/implicit-time-integration.md)
* [ITPA n = 6 TAE benchmark](/benchmarks/itpa-tae-benchmark.md)
* [JOREK](/software/jorek.md)
* [Linear MHD eigenvalue codes](/methods/linear-mhd-eigenvalue-codes.md)
* [M3D-C1-K](/software/m3d-c1-k.md)
* [MEGA](/software/mega.md)
* [NLED-AUG energetic-particle benchmark](/benchmarks/nled-aug-benchmark.md)
* [ORB5](/software/orb5.md)
* [Particle pushers: Boris, slow-manifold Boris, guiding-centre and gyrokinetic](/methods/particle-pushers.md)
* [Particle-to-finite-element moment projection](/methods/particle-to-mesh-projection.md)
* [Pressure coupling and current coupling](/methods/pressure-and-current-coupling.md)
* [Reduced MHD for tokamaks](/methods/reduced-mhd.md)
* [Reversed-shear Alfvén eigenmode (RSAE)](/definitions/reversed-shear-alfven-eigenmode.md)
* [The δf particle method](/methods/delta-f-method.md)
* [Toroidal Alfvén eigenmode (TAE)](/definitions/toroidal-alfven-eigenmode.md)
* [XTOR-K](/software/xtor-k.md)

# Citations

1. `/home/stefano/papers/mosaic/fusion-mhd-simulation/2022_Crossref_Physics_of_Plasmas_Bogaarts_Development_and_application_of_a_hybrid_MHD-kinetic_model_in.pdf`
   * **Version.** arXiv:2208.02179v4 [physics.plasm-ph], 10/11 November
     2022, AIP preprint template; 30 pages (text pp. 1–23, references
     pp. 23–26, Figs. 15–20 on pp. 27–30). Not the typeset version of record.
   * **Identity.** doi:10.1063/5.0119435, checked on Crossref by title:
     Phys. Plasmas 29(12), article 122501, online 2 December 2022; authors
     Bogaarts, Hoelzl, Huijsmans, Wang and "JOREK Team" match page 1 (the
     team list is deferred to Hoelzl et al., Nucl. Fusion 61:065001, 2021).
   * **How read.** Full text including App. A; equations read; plot values
     (Figs. 2, 3, 4, 7, 9) are the reader's approximate readings.
   * **Recorded as printed.**
     * Particle time step: §IV A says "$2\cdot10^{-10}$ s ≈ 200$\tau_g$";
       Fig. 2b counts 50–200 particle steps per gyro-orbit, so the step is
       ≈$\tau_g/200$.
     * App. A residual printed with $+\delta\sin(\omega t_i)$; consistent
       with the fit function it is $-\delta\sin(\omega t_i)$. The derivatives
       labelled $\partial S/\partial\alpha$ etc. are $\partial r_i/\partial\beta_j$;
       the independent variable switches between $t$ and $x$; the
       $\mathbf X^T\mathbf Y$ entries lack $\omega$ inside $\cos$, $\sin$.
     * §III: "$\delta(\boldsymbol\xi-\boldsymbol\xi)\to K^\alpha_{\mathbf l}(\boldsymbol\xi)$"
       (argument typo); "(e.g. figures 10, 4, 6, 4)" lists Fig. 4 twice.
     * Eq. 2: the right-hand side is printed underlined, unexplained.
     * $\boldsymbol\Pi_h$ is the uncentred moment, so it includes a
       Reynolds-stress part for EPs with mean flow; not discussed.
     * $t=0.7$ s: Table I "TAE, $m=2,3$"; Fig. 16 caption "the m=2,3 coupled
       EPM mode"; conclusion "a m=2,3 TAE". For $t\ge0.75$ s Fig. 16 says
       "m=2 EPMs or low-shear modes", Table I says RSAE.
     * Fig. 2a spans 20–200 M markers; the production ITPA run used 40 M.
     * §V does not restate the MHD model of the AUG #31213 runs.
     * Fig. 12 calls $\lambda=v_\parallel/v$ the "pitch angle".
     * Energy "conserved rather well" (Fig. 7 text) against the ≈10%
       mismatch of Fig. 7b.
     * Typos: "avaible", "accelaration", "implentation", "intrincially",
       "realxation", "presssure", "terms fo", "equlibrium", "showns",
       "reagion", "quantatitive", "spectogram", "distribuiton", "TThe".
   * **Reference list.** 39 printed entries, merged into the bibliography
     under `bogaarts-2022`. Ref. 9 (Vlad et al. 2021, Nucl. Fusion) has no
     volume or article number printed; Ref. 11 is a private communication
     (Huijsmans 2022); Ref. 16 (Särkimäki 2022) is arXiv:2203.09344; Ref. 20
     (Pamela 2020) ends in "J. Contributors" (JOREK contributors), encoded as
     `and others`; Ref. 27 (Lauber 2016, NLED reference case) is a seminar
     URL; Ref. 32 (`konies-2012`, same title as Ref. 31, no venue, no
     diacritics) is kept distinct from `konies-2018`; Ref. 39 is an
     econometrics textbook with an odd "Vol. 5"; Ref. 13 prints "C. Cheng"
     (C.Z. Cheng); Ref. 29 prints "G. Huysmans" (Huijsmans).
