---
type: Source
title: "Zhang et al. (2025) — Quantitative magnetohydrodynamic modelling of flux pumping in ASDEX Upgrade"
description: "JOREK full visco-resistive two-temperature MHD simulations of flux pumping in the AUG hybrid discharge #36663 with experimental parameters over the resistive timescale: a 1/1 mode clamps q0 near 0.99 through a slow negative dynamo of a few mV/m, matching the experimental order of magnitude, while 2D runs drop q0 to 0.6–0.79."
resource: "doi:10.1088/1741-4326/adcfb4"
source_kind: paper
authors: [Zhang H., Hölzl M., Krebs I., Burckhart A., Bock A., Günter S., Igochine V., Lackner K., Ramasamy R., Zohm H., JOREK Team, ASDEX Upgrade Team]
year: 2025
venue: "Nucl. Fusion 65:066001"
local_file: "/home/stefano/papers/mosaic/fusion-mhd-simulation/2025_Crossref_Nuclear_Fusion_Zhang_Quantitative_magnetohydrodynamic_modelling_of_flux_pumping_i.pdf"
tags: [full-mhd, kink, tearing, bootstrap-current, tokamak]
timestamp: 2026-10-16T20:00:00Z
---

# Summary

The paper models [magnetic flux pumping](/definitions/magnetic-flux-pumping.md)
in phase III of the sawtooth-free hybrid AUG discharge #36663 (Burckhart et al.
2023) with [JOREK](/software/jorek.md) in its full (non-reduced)
[visco-resistive](/methods/visco-resistive-mhd-model.md) two-temperature
single-fluid model, without Hall or diamagnetic terms, using profiles, sources
and coefficients taken from the experiment (Spitzer $\eta=2.41\times10^{-9}$ Ω m
on axis, $S\approx2.8\times10^8$, magnetic Prandtl number 1400, Hartmann number
7.9×10⁶) and runs spanning the resistive time (700 ms in 3D, up to 1.8 s in
2D). Without non-axisymmetric modes (2D, $n=0$) the off-axis non-inductive
current source peaks $j_\phi$ by about 30% and drives $q_0$ from 1.04 to 0.79
(0.75 saturated at ×100 resistivity). In 3D ($n\le4$) an $n=1$
[quasi-interchange](/definitions/interchange-mode.md) grows at 19.46 ms⁻¹; its
saturation produces an under-damped $q_0$ oscillation at 5.8 kHz driven by a
"fast dynamo" of order V/m, after which a "slow" negative dynamo of order mV/m
holds $q_0\approx0.99$ with flat core current (≈2.5 MA/m²) and flat core
pressure for hundreds of ms. A flux-surface-averaged balance of the toroidal
induction equation attributes the −1.6 mV/m electric-field deficit to the net
dynamo (fluctuation term partly offset by a positive axisymmetric-flow term),
with ≈−0.3 mV/m from resistivity flattening. The saturated core holds two
twisted 1/1 flux tubes, the original one with local $q_0\approx1.04$ (ideal
quasi-interchange) and a new island-like tube with local $q_0\approx0.97$
([resistive tearing](/definitions/tearing-mode.md)). The authors claim the first
quantitative agreement with experiment: the mV/m dynamo matches the
experimentally reconstructed deficit, whereas earlier runs with enhanced
resistivity gave ≈0.1 V/m. Off- and on-axis sources of experimental strength
also remain sawtooth-free; lower Hartmann number gives sawtooth-like
oscillations and then a saturated
[resistive internal kink](/definitions/resistive-internal-kink.md). One 3D case
costs ≈0.5 M core-hours; ITER and DEMO are judged out of reach.

# Key claims

Registry symbols (§11): $f^{(0)}$ and $\tilde f$ the axisymmetric ($n=0$) and
non-axisymmetric ($n\ge1$) parts of a field, $(\cdot)^{(0)}$ also the toroidal
average of a product; $E_{\mathrm{dyn},\parallel}$ the parallel dynamo emf (here
projected on $\bar{\mathbf b}$, not on $\mathbf b$); $\nu_{\mathrm{kin}}$ the
kinematic viscosity. Page-local: $f_{2D}$ a value of the 2D run and
$\Delta f=f^{(0)}-f_{2D}$; $\bar{\mathbf b}=\mathbf B^{(0)}/B_{\phi,\mathrm{eq}}$
(not a unit vector); $P_{\mathrm m}$ the magnetic Prandtl number; $\mathrm{Ha}$
the Hartmann number. $\mathbf J_x=J_x\mathbf e_\phi$ (registry §6) is the
toroidal non-inductive source.

1. **2D failure** (§3.1, Figs. 4–5, 9d). Without $n>0$ modes the source peaks the
   core current: at 1500 ms $q_{\min}\approx0.79$ at $s=0.1$ and max $j_\phi$
   rises by ≈30% (≈0.8 MA/m²); with ×100 $\eta$ $q_0$ saturates at ≈0.75 (≈0.6 in
   the "modeled" curve of Burckhart et al. 2023), contrary to the observed
   sawtooth-free phase. Shown.
2. **Linear mode** (§3.2, Fig. 6). $n=1$, $m=1$ grows at $\gamma=19.46$ ms⁻¹
   (0.25–1.3 ms); $n=2$–4 are driven by coupling. The flow is a core-wide
   convection cell, "quite distinct" from the internal kink, whose flow peaks at
   $q=1$. Shown. $\gamma$ is "very sensitive to the initial value of $q_0$", the
   saturated state is not. Stated.
3. **Fast dynamo** (§3.3, Fig. 7). At ≈1.3 ms $q_0$ drops by 0.03 in 0.1 ms, then
   oscillates about 1.013 at 5.8 kHz like an "under-damped pendulum"; the parallel
   emf reaches 1.5 V/m, alternates sign at the same frequency and changes sign near
   $s\approx0.2$. Shown. Interpreted as self-regulation removing equilibrium errors,
   so fine-tuning the profiles "is not necessary". Stated.
4. **Quasi-stationary 3D state** (§3.4, Figs. 8–10). $q_0$ falls from 1.04 to ≈1
   within 100 ms and saturates at ≈0.99 over $s<0.3$ after 200 ms; the slow dynamo
   is negative in the core and three orders of magnitude below the fast one; core
   $j_\phi$ stays ≈2.5 MA/m² (2D: >3 MA/m²) and the core pressure gradient "almost
   vanishes". Shown.
5. **Flow** (§3.4, Fig. 11). At 505 ms the flow is 1/1 but distorted, a few m/s
   near $q=1$, comparable to the DIII-D #164661 estimate (Piovesan et al. 2017);
   not measurable in AUG. Shown; comparison Stated.
6. **Two flux tubes** (§3.4, Fig. 12; §6.1). The original axis keeps local
   $q_0\approx1.04$ ("topology … has not changed"); the new island-like tube has
   local $q_0\approx0.97$; flow concentrates at the X-point beneath it,
   "suggesting an incomplete magnetic reconnection". The mode is "a combination of
   the 1/1 ideal quasi-interchange mode and the 1/1 resistive tearing mode". Local
   $q$ Shown; interpretation Stated.
7. **Toroidal electric-field balance** (§4.1, Eq. 8, Fig. 13). The deficit
   $\eta_{2D}\Delta j_\phi\approx-1.6$ mV/m is the same at 90, 205 and 505 ms; the
   net dynamo is −0.3, −1.35, −1.6 mV/m and resistivity flattening ≈0, −0.25,
   −0.3 mV/m. $(\mathbf v^{(0)}\times\mathbf B^{(0)})_\phi$ is positive and
   "non-ignorable", contrary to the $\mathbf v^{(0)}\simeq0$ assumption of Krebs et
   al. 2017; the nonlinear resistive term $(\tilde\eta\tilde j_\phi)^{(0)}$ is
   ≈10⁻³ mV/m. Shown.
8. **Residue** (§4.1, Fig. 14). The right-hand side slightly exceeds the deficit;
   the residual $R^{-1}\partial_t\Delta\psi$ becomes flat ($s<0.3$) and constant
   after 363 ms, a uniform drift of $\psi$ that leaves $q$ and $j_\phi$ unchanged.
   Toroidal flux is conserved by cancellation of the axisymmetric and fluctuation
   terms ("not shown"). Shown / Stated.
9. **Quantitative agreement** (Abstract; §4.1; §6.2). The mV/m dynamo field is
   "consistent with the experimentally reconstructed electric field deficit" in AUG
   and DIII-D, while enhanced-resistivity runs give ≈0.1 V/m: "the first
   quantitative result on the flux pumping and dynamo effect in tokamak hybrid
   scenarios". Simulation Shown; comparison Stated (no experimental value
   plotted).
10. **Parallel dynamo emf** (§4.2, Eq. 10, Fig. 15).
    $E_{\mathrm{dyn},\parallel}=\langle\bar{\mathbf b}\cdot(\tilde{\mathbf v}\times\tilde{\mathbf B})^{(0)}\rangle$
    comes "solely" from $n\ge1$, dominated by $n=1$; at 505 ms ≈−1.7 mV/m near
    $s\approx0.07$ and ≈+0.5 mV/m near 0.3, matching the net toroidal dynamo.
    Derived and Shown.
11. **Current-diffusion balance** (§4.3, Eq. 12, Fig. 16). The net drive slightly
    exceeds the dynamo diffusion at 90 ms and cancels it "excellently" at 505 ms;
    smoothing the source weakens the drive, which goes as the second derivative of
    the source profile. Derived and Shown.
12. **Source scan** (§5, Figs. 17–19). Sources peaked off-axis at $s=0.1$ and
    on-axis (both ≈2.70 MA/m²) give in 2D $q_0\approx0.6$ and
    $j_{\max}\approx4$ MA/m², in 3D flat $j_\phi\approx2.5$ MA/m² with $q_0$ near 1
    and a larger dynamo following the source shape; on-axis ECCD is compatible
    with sawtooth suppression, and these runs agree better with the reconstructed
    profiles. Shown.
13. **Toroidal resolution** (§2.4). $n\le1$ "cannot correctly capture the flux
    pumping"; $n\le2$ and $n\le4$ differ by ≈1% in saturated $q_0$ and $j_\phi$;
    time-step and grid scans converge the linear growth and saturation amplitude.
    Stated (not plotted).
14. **Hartmann-number scan** (§6.2; footnote †, p. 8). Raising $\eta$ and $\nu$
    gives sawtooth-like oscillations ($\mathrm{Ha}\sim10^5$, $q_0$ between 0.95
    and 1.0), then a quasi-stationary 1/1 resistive internal kink with $q_0\sim0.7$
    ($\mathrm{Ha}\sim10^4$); RFP studies find multiple helicity at
    $\mathrm{Ha}\gtrsim10^4$ and single helicity at $\lesssim10^3$. Stated (not
    shown; direction wording, see Recorded as printed).
15. **Viscosity** (§6.2) "may significantly influence the amplitude of plasma flow
    … and the success or failure of flux pumping"; the dynamo amplitude rescales
    with $\eta$ to balance the drive. Stated.
16. **Cost and extrapolation** (§6.2). ≈0.5 M core-hours per 3D case
    (Marconi-Fusion); $\tau_R/\tau_A>10^6$ for AUG, JET ≈30% larger, ITER >10×,
    DEMO >40×; 3D runs for ITER and DEMO are "impractical", hence a surrogate model
    (Krebs et al. 2023). Stated.
17. **Mechanisms** (§1, §2.2). Flux pumping needs a $\beta$ threshold (Krebs et al.
    2017) and acts through the negative dynamo of the quasi-interchange and
    resistivity flattening via $T_e$ flattening. Attributed.

# Models and numerics

**Model** (§2.2, Eqs. 1–4, rendered pp. 5–6 checked). Normalized ($\mu_0=1$,
central $\rho_0$) two-temperature single-fluid visco-resistive full MHD in
$(R,Z,\phi)$, in registry symbols:

$$\begin{aligned}
\partial_t\mathbf A&=\mathbf v\times\mathbf B-\eta\,(j_\phi-J_x)\,\mathbf e_\phi-\nabla\Phi,\\
\rho\,\partial_t\mathbf v&=-\rho\mathbf v\cdot\nabla\mathbf v+\mathbf J\times\mathbf B-\nabla p+\nabla\cdot(\nu\nabla\mathbf v)-S_\rho\mathbf v,\\
\partial_t\rho&=-\nabla\cdot(\rho\mathbf v)+\nabla\cdot(D_\perp\nabla_\perp\rho+D_\parallel\nabla_\parallel\rho)+S_\rho,\\
\partial_tp_s&=-\mathbf v\cdot\nabla p_s-\Gamma p_s\nabla\cdot\mathbf v+\nabla\cdot(\kappa_{\perp,s}\nabla_\perp T_s+\kappa_{\parallel,s}\nabla_\parallel T_s)+S_{p,s},\quad s=i,e,
\end{aligned}$$

with $\mathbf B=F\nabla\phi+\nabla\times\mathbf A$, $\mathbf J=\nabla\times\mathbf B$,
$p=\rho(T_i+T_e)$, $\Gamma=5/3$. $F(\psi)$ comes from the Grad–Shafranov
equilibrium and is frozen in time. $\eta$ acts **only on the toroidal component**
"to improve the numerical stability", so $A_R$, $A_Z$ and $B_\phi$ evolve
ideally. $\Phi$ is removed by the Weyl gauge. Ohmic heating (small against
auxiliary heating), ion–electron equipartition ("causing numerical
instabilities"), Hall and diamagnetic terms are omitted. Full MHD is chosen
because $B\,\delta B_\parallel\sim-\delta p$ for the quasi-interchange (Pamela et
al. 2020).

**Analysis equations** (§4). With $\psi=RA_\phi$ (per radian):
$\partial_t\psi=R[(\mathbf v\times\mathbf B)_\phi-\eta(j_\phi-J_x)]$ (Eq. 5); its
axisymmetric part
$\partial_t\psi^{(0)}=R[(\mathbf v^{(0)}\times\mathbf B^{(0)})_\phi+(\tilde{\mathbf v}\times\tilde{\mathbf B})^{(0)}_\phi-\eta^{(0)}(j_\phi^{(0)}-J_x)-(\tilde\eta\tilde j_\phi)^{(0)}]$
(Eq. 6); the 2D run $\partial_t\psi_{2D}=-R\eta_{2D}(j_{\phi,2D}-J_x)$ (Eq. 7); and
the linearized difference

$$R^{-1}\partial_t\Delta\psi=(\mathbf v^{(0)}\times\mathbf B^{(0)})_\phi+(\tilde{\mathbf v}\times\tilde{\mathbf B})^{(0)}_\phi-\eta_{2D}\Delta j_\phi-\Delta\eta\,(j_\phi^{(0)}-J_x)\quad\text{(Eq. 8)}.$$

Projection on $\bar{\mathbf b}$ gives $E_{\mathrm{dyn},\parallel}$ (Eqs. 9–10;
$B_{\phi,\mathrm{eq}}$ used "because it has lower numerical noise"). The
flux-surface-averaged current-diffusion balance (Eq. 12, dropping toroidal and
poloidal derivatives and $1/R^2$ terms for $L^2/R^2\ll1$) is
$\partial_t\langle j_\phi\rangle\simeq\mu_0^{-1}(|\nabla\psi|^2\partial_\psi^2+\nabla^2\psi\,\partial_\psi)\langle-(\mathbf v\times\mathbf B)_\phi+\eta(j_\phi-J_x)\rangle$.

**Closures** (§2.4, Table 1). $\eta=\eta_0(T_e/T_{e,0})^{-3/2}$,
$\eta_0=2.41\times10^{-9}$ Ω m (8.85×10⁻¹⁰ JOREK units); dynamic
$\nu=\nu_0(T_e/T_{e,0})^{-3/2}$, $\nu_0=4.51\times10^{-7}$ kg m⁻¹ s⁻¹ (kinematic
2.70 m²/s), between the Braginskii perpendicular and gyro-viscosities;
Spitzer–Härm $\kappa_\parallel\propto T^{5/2}$ reduced 30× for the heat-flux
limit ($\kappa_{\parallel,e,0}=1174$, $\kappa_{\parallel,i,0}=37$ kg m⁻¹ s⁻¹);
$\kappa_\perp$ profiles solved so that the 2D temperatures are stationary
($\kappa_\parallel/\kappa_\perp\sim10^{10}$); $D_\perp=0$, uniform
$D_\parallel=2.17\times10^5$ m²/s for stability; $S_\rho=0$. $J_x$: experimental
NBI + ECCD + bootstrap source, heavily smoothed (peak 2.05 against 2.70 MA/m² at
$s=0.1$), Ohmic share ≈20% in the core; the
[bootstrap](/definitions/bootstrap-current.md) part is a fixed profile.
Dimensionless numbers with $L=0.1$ m: $P_{\mathrm m}=\nu\mu_0/(\rho\eta)=1400$,
$\mathrm{Ha}=(\mu_0L^2v_A^2/(\eta\nu_{\mathrm{kin}}))^{1/2}=7.9\times10^6$,
$S=\mu_0Lv_A/\eta=2.8\times10^8$ (compiler's check with
$\rho=0.98\times10^{20}m_p$: $v_A\approx5.7\times10^6$ m/s, $S\approx2.9\times10^8$,
$P_{\mathrm m}\approx1430$, $\mathrm{Ha}\approx7.9\times10^6$). The Table 1
ratios imply $\eta_N=\eta\sqrt{\rho_0/\mu_0}$, $\nu_N=\nu\sqrt{\mu_0/\rho_0}$,
$D_N=D\sqrt{\mu_0\rho_0}$, $\kappa_N\approx(\Gamma-1)\kappa\sqrt{\mu_0/\rho_0}$
with $\rho_0=1.64\times10^{-7}$ kg/m³ to ≈2% (reader's inference).

**Equilibrium and boundary** (§2.3). IDE reconstruction with IMSE ($q$ good to
0.1); $B_\phi(R_0)=-2.57$ T, $F_0=-4.41$ T m, $I_p=-0.806$ MA held by PID
feedback on the boundary loop voltage; $q_0=1.04$, shear-free to $s\approx0.4$;
core $j_\phi\approx2.4$ MA/m²; fixed boundary at the last closed flux surface.

**Discretization** (§2.4). Implicit Gear scheme (order not stated);
$G^1$ bicubic [Bézier elements](/methods/bezier-finite-elements.md) on a polar
grid of 100×100 × toroidal Fourier series, $n\le4$; $\Delta t=2.30\times10^{-3}$ ms.
Linear solver not discussed. $q$ from field-line tracing of the $n=0$ field
(Fig. 12: total field about the helical axis). Marconi-Fusion and JFRS-1.

# Tests and results

| Run | $q_0$ | max $j_\phi$ [MA/m²] | Note |
|---|---|---|---|
| 2D, source 1 | 1.04 → 0.79 (1827 ms, unsaturated) | 2.4 → >3 | 0.75 saturated at ×100 $\eta$ |
| 3D, source 1 | ≈0.99 after 200 ms | ≈2.5 | 700 ms run |
| 2D, sources 2/3 (×100 $\eta$) | ≈0.6 | ≈4 | |
| 3D, sources 2/3 | ≈1 | ≈2.5 | $|E_{\mathrm{dyn},\parallel}|$ up to ≈3 mV/m |

| $t$ [ms] | deficit [mV/m] | net dynamo [mV/m] | resistivity flattening [mV/m] |
|---|---|---|---|
| 90 | −1.6 | −0.3 | ≈0 |
| 205 | −1.6 | −1.35 | −0.25 |
| 505 | −1.6 | −1.6 | −0.3 |

* At 505 ms the two dynamo pieces are individually ≈−3 mV/m (fluctuation) and
  ≈+3 mV/m (axisymmetric flow) near $s\approx0.2$ (figure reading), so the net
  value is a strong cancellation.
* Flow a few m/s, up to ≈40 m/s on the Fig. 11 colour bar.
* No code-to-code benchmark; AUG #36663 is a validation reference.

# Notation map

| Zhang et al. (2025) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $(R,Z,\varphi)$, $\hat e_\varphi$ | $(R,Z,\phi)$, $\mathbf e_\phi$ | orientation not stated; $B_0$, $F_0$, $I_p<0$ |
| $\mathbf A$, $\Phi$ | $\mathbf A$, $\Phi$ | Weyl gauge |
| $\Psi$ (gauge function) | words | **collision** with registry $\Psi_{m/n}$ |
| $\mathbf J=\nabla\times\mathbf B$ | $\mu_0\mathbf J=\nabla\times\mathbf B$ | $\mu_0=1$ in Eqs. 1–4; Eqs. 11–12 carry $\mu_0$ |
| $J_\varphi$ | $j_\phi$ | |
| $S_j$ | $J_x$ ($\mathbf J_x=J_x\mathbf e_\phi$) | |
| $\gamma=5/3$; $\gamma_{n=1}$ | $\Gamma$; $\gamma$ | **collision:** the paper uses $\gamma$ for both |
| $\nu$, $\nu_0$; $\tilde\nu_0$ | $\nu$ (dynamic); $\nu_{\mathrm{kin}}$ (kinematic, §11) | |
| $\kappa_{\perp,s}$, $\kappa_{\parallel,s}$ | $\kappa_\perp$, $\kappa_\parallel$ | |
| $S_{T_{i(e)}}$ | $S_{p,s}$ | |
| $\psi\equiv RA_\varphi$, $\psi_n$ | $\psi$ (per radian), $\psi_N$ | |
| $\rho_p=\sqrt{\psi_n}$ | $s$ | **collision:** registry $\rho$ is mass density |
| $\rho_0$, $\rho_m$ | $\rho$ (reference, central) | |
| $F$, $F_0=R_0B_0$ | $F$; $F$ on axis | registry $F_0$ is the vacuum constant |
| $B_0$ (§2–3); $\mathbf B_0$ (§4) | $B_\phi$ on axis; $\mathbf B^{(0)}$ | **collision:** subscript 0 = axis value and $n=0$ part |
| $f_0$, $f_1$ | $f^{(0)}$, $\tilde f$ (§11) | **collision** with axis values and registry $f_0$ (equilibrium distribution) |
| $(\cdot)_{n=0}$ | $(\cdot)^{(0)}$ | |
| $f_{2D}$, $\Delta f$ | page-local | |
| $\bar{\mathbf b}_0=\mathbf B_0/B_{\varphi,eq}$ | $\bar{\mathbf b}$ (page-local) | not the unit vector $\mathbf b$ |
| $\varepsilon_\parallel$ | $E_{\mathrm{dyn},\parallel}$ (§11) | **collision** risk with $\varepsilon_0$; projected on $\bar{\mathbf b}$ |
| $q_0$ | $q_0$ | also used for $q$ at $s=0.1$ (Fig. 9c) and local tube $q$ (Fig. 12) |
| $E_{mag,n}$, $E_{kin,n}$ | $W_{\mathrm{mag}}^{(n)}$, $W_{\mathrm{kin}}^{(n)}$ | |
| $P$ (Prandtl), $H$ (Hartmann) | $P_{\mathrm m}$, $\mathrm{Ha}$ (page-local) | $H$ collides with helicity $\mathcal H$ |
| $S$, $\tau_R$, $\tau_A$, $v_A$, $L$ | $S$, $\tau_R$, $\tau_A$, $v_A$; $L=0.1$ m | |
| $B_T$, $\beta_N$ | $B_\phi$, $\beta_N$ | |

# Pages created or updated

Chunk 3 (2026-10-16) created or updated the pages below. This source is cited on:

* [Bootstrap current and its MHD implementation](/definitions/bootstrap-current.md)
* [Bézier–Hermite finite elements with toroidal Fourier harmonics](/methods/bezier-finite-elements.md)
* [CASTOR3D](/software/castor3d.md)
* [Implicit time integration and preconditioned Krylov solvers for nonlinear MHD](/methods/implicit-time-integration.md)
* [Interchange modes and the Mercier criterion](/definitions/interchange-mode.md)
* [JOREK](/software/jorek.md)
* [Magnetic flux pumping](/definitions/magnetic-flux-pumping.md)
* [MHD dynamo effect](/definitions/mhd-dynamo.md)
* [Neoclassical tearing mode](/definitions/neoclassical-tearing-mode.md)
* [Resistive internal kink (m/n = 1/1)](/definitions/resistive-internal-kink.md)
* [Resistive tearing mode](/definitions/tearing-mode.md)
* [Sawtooth crash and Kadomtsev reconnection](/definitions/sawtooth-crash.md)
* [Single-fluid visco-resistive MHD model](/methods/visco-resistive-mhd-model.md)

# Citations

1. `/home/stefano/papers/mosaic/fusion-mhd-simulation/2025_Crossref_Nuclear_Fusion_Zhang_Quantitative_magnetohydrodynamic_modelling_of_flux_pumping_i.pdf`.
   * **Version.** arXiv:2503.03344v3 [physics.plasm-ph], 11 Apr 2025, author
     LaTeX preprint, 31 pp.; not the publisher version. Page, equation and figure
     numbers are the preprint's.
   * **Identity.** doi:10.1088/1741-4326/adcfb4, checked on Crossref: Nucl. Fusion
     65(6), article 066001, online 2025-05-02; 12 authors including the two teams.
     The second author is printed "Hölzl" (elsewhere in the bundle "Hoelzl"). The
     slug is distinct from `zhang-2021`. A follow-up (Zhang et al., NF 66, 2026,
     on bifurcated helical-core relaxations) is not ingested; it is most likely
     the "separate paper" on the Hartmann scan announced in footnote †.
   * **How read.** Full text; Eqs. 1–12 read on rendered pages; Fig. 13 legend
     checked on rendered p. 18; curve values are figure readings.
   * **Recorded as printed.**
     * Hartmann scan (§6.2, footnote †): done "by increasing viscosity and
       resistivity", "with the increase of Hartmann number" the state turns
       sawtooth-like at $H\sim10^5$, "further increased above ∼10⁴" a resistive
       kink. Since $\mathrm{Ha}\propto(\eta\nu)^{-1/2}$ and the printed values fall
       (7.9×10⁶ → 10⁵ → 10⁴), "increase" and "above" should read "decrease" and
       "below" (compiler's reading).
     * Eq. 10: the middle line begins "$\bar{\mathbf b}_0\cdot\{-[\dots]\}$" with no
       connecting sign.
     * $q_0=0.79$ in 2D is placed at 1500 ms in §3.1 (as $q_{\min}$ at
       $\rho_p=0.1$) and at 1827 ms in Fig. 9(d) and its caption.
     * "$q_0$" denotes the axis value, $q$ at $\rho_p=0.1$ (Figs. 7a, 9c) and local
       tube $q$ (Fig. 12); subscript 0 also marks $n=0$ parts in §4.
     * Fig. 13: the plotted black curve is $-\eta_{2D}\Delta J_\varphi$ (positive,
       ≈+1.5 mV/m), the text's "deficit of −1.6 mV/m" its negative; the
       flattening curve reads ≈−0.5 mV/m near the axis at 505 ms against −0.3 in
       the text (rough reading).
     * §6.1 "first decreases slightly below unity in the first 200 ms" against
       §3.4 "decreases to unity … within 100 ms, then saturates around 0.99 … after
       200 ms" (consistent, differently worded).
     * The abstract's "quantitative agreement … for the first time" rests on an
       order-of-magnitude comparison; no experimental emf is plotted.
     * Eq. 11 carries $\mu_0$ although Eqs. 1–4 are normalized.
     * Figs. 18–19 captions both call the source the "dotted line in panel (a)",
       while Fig. 17 draws source 2 dash-dotted (not verified visually).
     * Typos: "Weyls' guage", "Sweet-Park model", "magnetic flux surfac",
       "Tecniques"; "Huysmans"/"Huijsmans" spelled both ways.
   * **Reference list.** 55 printed entries in v3 (Crossref counts 54 for the
     published list), all titled, merged into the bibliography under
     `zhang-2025`. Ref. [1] is the ingested
     [Hoelzl et al. (2024)](/sources/hoelzl-2024.md), whose full title it prints;
     [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) and
     [Bogaarts et al. (2022)](/sources/bogaarts-2022.md) are also cited. Key
     decisions: Siccinio et al. (EU-DEMO technical requirements, FED 179) is
     `siccinio-2022-b`; Shi T. et al. (EAST (2,1) NTM–(1,1) coupling, PST 17) is
     `shi-2015-b`; the 2017 TUM thesis of Krebs is `krebs-2017-b` (`krebs-2017` is
     the PoP paper); `halpern-2011-b`, `zhang-2020-d` (Hall-effect PPCF) and
     `zhang-2020-e` (arXiv 2004.12067) avoid collisions; Zhang W. NF 60 is
     `zhang-2020-c`. Ref. [54] prints 2016 for NF 57(1) → `strumberger-2017`;
     ref. [6] cites the Russian original of Kadomtsev → `kadomtsev-1975`; ref.
     [46] (JCP 464) → `pamela-2022`.
