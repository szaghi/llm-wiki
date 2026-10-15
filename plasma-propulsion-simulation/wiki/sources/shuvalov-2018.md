---
type: Source
title: "Shuvalov et al. (2018) — Control of the drag on a spacecraft in the earth's ionosphere using the spacecraft's magnetic field"
description: "Measures, in a hypersonic rarefied nitrogen plasma beam, the drag of a sphere carrying an internal dipole field, fits it to empirical laws in the magnetic-to-dynamic pressure ratio and the field–flow angle, shows that a plasma jet injected into the mini-magnetosphere multiplies the drag by about 3.8, and extrapolates to a 0.6–0.8 T body field whose ionospheric drag pressure it states to be close to that of two of the four ion-beam-shepherd beams it quotes."
resource: "doi:10.1016/j.actaastro.2018.06.038"
source_kind: paper
authors: [Shuvalov V.A., Gorev N.B., Tokmak N.A., "Pis'mennyi N.I.", Kochubei G.S.]
year: 2018
venue: "Acta Astronaut. 151:717–725"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Shuvalov_Control_of_the_drag_on_a_spacecraft_in_the_earths_ionosphere.pdf"
tags: [plasma-spacecraft-interaction, magnetic-field, drag, experiment, mini-magnetosphere, debris-removal]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

A laboratory study, run in the plasmadynamic vacuum facility of the
Institute of Technical Mechanics (Dnipro), of the drag on a dielectric
sphere that carries its own dipole magnetic field (a solenoid inside it)
in a hypersonic, rarefied, partially ionized nitrogen plasma beam. The
authors state that the similarity parameters are close to or correspond
to those of a 0.5–1 m spacecraft at about 800 km (Table 1). The drag coefficient, measured with two microbalances,
is fitted to an empirical law in the ratio of the surface magnetic
pressure to the flow dynamic pressure (Eq. 1) and to one in the angle
between field and flow (Eq. 2), combined as Eq. 3. For the field
perpendicular to the flow, the sphere forms an artificial
mini-magnetosphere whose standoff distance follows from pressure balance
(Eqs. 4–5); the measured drag agrees with magnetic-sail simulations from
the literature (Table 2). Injecting a subsonic plasma jet, produced by
electron-heated pyrolysis of an epoxy layer, into the mini-magnetosphere
cavity multiplies the drag by about 3.8 (Eqs. 7–8, Table 3). The authors
extrapolate to the ionosphere and state that a 0.6–0.8 T body field gives
a drag pressure close to that of two ion-beam-shepherd beams, the 10 m
and the ψ∼6° cases (§6, Figs. 8–9; see claim 10). The paper has no simulation of its own: every
"calculation" it compares with is a literature result.

# Key claims

Symbols are the paper's own (see the notation map).

1. **Facility and similarity** (§2.1–2.2, Table 1). N$_2$ plasma beam with
   $N_i=2.1\times10^{15}$–$9.6\times10^{15}$ m$^{-3}$, $U_i\approx11.5$,
   15.6 and 28.3 km/s, $T_e\approx2.6$ eV, $T_i\approx0.52$ eV, ionization
   degree $\varepsilon_i=10^{-2}$–$10^{-1}$, conductivity
   $\sigma=1.9\times10^3$–$3.3\times10^3$ Ω$^{-1}$m$^{-1}$, facility field
   $B_0=2\times10^{-4}$ T, $P_d=8\times10^{-3}$–$1.3\times10^{-1}$ N/m$^2$,
   mean ion mass 19.6 amu, dissociation degree ≈0.6. Table 1:
   $\mathrm{Re}_m$ 1.6–6.2 (ionosphere >1), $M$ 3.6–8.9 (ionosphere
   5.3–7.5), $\mathrm{Kn}_i$ 12–15. The authors state that the parameters
   "close to or correspond" to ionospheric conditions for a non-magnetized
   body. Stated.
2. **Aligned-field drag law** (§3, Eq. 1, Fig. 3). An empirical fit,
   shown against three measured data sets and five literature
   calculations, over $3\times10^1\le P_{BW}/P_d\le2\times10^5$:
   $$c_x(\theta=0^\circ)/c_{0x}=\exp\left[5.85\times10^{-2}\,\lg^2(P_{BW}/P_d)\right]=f_1(P_{BW}/P_d),$$
   with $P_{BW}=B_W^2/2\mu$ and $P_d=\rho_iU_i^2/2$. The ratio rises from
   about 1.1 at $5\times10^1$ to about 4.8 near $10^5$ (read from Fig. 3;
   Eq. 1 itself gives 1.18 and 4.32). Shown.
3. **Angular law** (§3, Eq. 2, Fig. 4). An empirical fit at
   $P_{BW}/P_d\approx2.5\times10^4$:
   $$\frac{c_x(\theta)}{c_x(\theta=0)}\approx|\cos\theta|^{0.5}+0.653\,\sin^7\theta\left[\left(|\sin\theta-|\cos\theta||\right)\left(|\sin^2\theta-|\cos^{0.5}\theta||\right)\right]=f_2(\theta),$$
   so $f_2(0)=1$ and $f_2(\pi/2)=0.653$. Combined (Eq. 3):
   $c_x(\theta)=c_{0x}f_1(P_{BW}/P_d)\,f_2(\theta)$. Literature numerics lie
   below ([21], about 0.58 at 90°) and above ([5,11], about 0.72 at 90°)
   the fit (read from Fig. 4). Shown.
4. **Non-magnetized reference** (§3). $c_{0x}=F_{0x}/(P_dA_W)\approx2.0$ for
   collisionless hypersonic flow about a sphere (attributed to [20]). The
   Coulomb (charged-sphere) drag component
   $c_{\phi x}/c_{0x}\approx1-\exp[-\Phi_W^{0.5}/0.263(r_W/\lambda_d)]\cdot\eta^{2/3}$
   (attributed to [18]; grouping ambiguous as printed) vanishes for
   $r_W/\lambda_d>50$. Attributed.
5. **Mini-magnetosphere standoff** (§4, Eqs. 4–5). Derived from the balance
   of the magnetic pressure $(2B_L)^2/2\mu$ (field doubling at the
   magnetopause, attributed to [22–26]) with the stagnation pressure
   $P_{dL}=\rho_iU_i^2$, for an equatorial dipole field $B_L=P_m/4\pi L^3$
   and $P_m=4\pi B_Wr_W^3$:
   $$L=\left(P_m^2/8\pi^2\mu P_{dL}\right)^{1/6},\qquad L=2^{1/3}r_W\left(P_{BW}/P_{dL}\right)^{1/6}=r_W\left(2P_{BW}/P_d\right)^{1/6}.$$
   Derived; the algebra checks.
6. **Interaction regime** (§4). At $L/r_W\approx4.6$, $U_i\approx28.3$ km/s,
   $N_i\approx9.6\times10^{15}$ m$^{-3}$, $M\approx8.9$,
   $B_W\approx3.9\times10^{-2}$ T: $B_L\approx8\times10^{-4}$ T, magnetopause
   thickness $\Delta\approx c/\omega_{ep}\approx5.7\times10^{-2}$ m,
   diffusive thickness $\Delta_D\approx4.6\times10^{-3}$ m, Larmor radii
   $L_{iT}\approx0.57$ m (thermal ions, 0.52 eV) and $L_{iU}\approx7$ m
   (flow ions, 82 eV), $\Delta/L\approx0.2$,
   $\Delta_D/L=\mathrm{Re}_{mL}^{-1}\approx2\times10^{-2}$,
   $L_{iT}/L\approx2.4$, $\mathrm{Kn}_{ii}=l_{ii}/L\approx2.6$. The setup is
   therefore in a regime transitional between MHD and kinetic, in which the
   Lorentz interaction predominates; both the classification and the
   predominance are attributed to Fujita [6].
7. **Perpendicular-field drag** (§4, Eq. 6, Table 2). Measured
   $c_x(\theta=\pi/2)$ = 2.7–4.2 for $L/r_W$ = 4.3–5.9, fitted within 7% by
   $$c_x(\theta=\pi/2)/c_{0x}\approx\xi\exp\left(5.85\cdot10^{-2}\lg^2\left[\tfrac12(L/r_W)^6\right]\right),\quad\xi=0.653\pm0.08 .$$
   Table 2 against magnetic-sail numerics: $L/r_W=5.0$, 3.2±0.4 and 2.9 [5]
   against 3.2±0.4 measured; $L/r_W=5.874$, 3.813 [22] against 3.89±0.25;
   $L/r_W=5.0$, 3.4±0.7 [6] against 3.2±0.4. Called "quite satisfactory
   agreement". Shown.
8. **Plasma-jet injection into the cavity** (§5, Eqs. 7–8, Table 3). Total
   drag $F_{\Sigma x}=F_x+F_{in}$ with $F_x=(P_m/\mu)(B_L/L)$ and
   $F_{in}=P_mI_{in}/\pi\delta_W^2$ (attributed to [25,26]):
   $$F_{\Sigma x}=F_x\left(1+\frac{\mu I_{in}}{\pi\delta_W^2}\frac{L}{B_L}\right)=F_x\left[1+\frac{\mu I_{in}}{2\pi\delta_W^2}\frac{r_W}{B_W}\left(\frac{2P_{BW}}{P_d}\right)^{2/3}\right].$$
   Measured $F_{\Sigma x}/F_x\approx3.81\pm0.2$ against 3.72 calculated
   ($I_{in}\approx1.6$ A, $\delta_W=10^{-2}$ m, $L/r_W\approx5.0$,
   $\theta=\pi/2$). Eq. 7: $c_{\Sigma x}(\pi/2)=c_x(\pi/2)\,c_{xin}(\pi/2)$;
   Eq. 8: $c_{\Sigma x}(\theta)=c_x(\theta)\,c_{xin}(\theta)$ with
   $c_{xin}(\theta)=c_{xin}(\pi/2)\,f_2(\alpha)$, valid for $\gamma=\pi/2$,
   $0\le\theta\le\pi/2$, $\pi/2\le\alpha\le\pi$. Results:
   $c_{\Sigma x}\approx12.2\pm1.4$ ($\theta=\pi/2$, $\alpha=\pi$,
   $\gamma=\pi/2$; $c_x=3.2\pm0.2$, $c_{xin}=3.81\pm0.2$) and
   $c_{\Sigma x}\approx13.0\pm1.64$ ($\theta=0$, $\alpha=\gamma=\pi$,
   $P_{BW}/P_d=7.81\times10^3$; $c_x=4.85\pm0.25$, $c_{xin}=2.68\pm0.15$),
   a "several-fold" (about 6×) increase over $c_{0x}\approx2$. Shown, on
   one sphere.
9. **Injected current** (§5). $I_{in}=\pi\delta_W^2N_{ein}(kT_{ein}/2\pi m_e)^{1/2}\beta_{in}$
   with
   $\beta_{in}\approx1+\frac{2r_e}{\delta_W}\sqrt{\Phi_W/\pi}+\frac{2r_e^2}{\pi\delta_W^2}$
   (Eq. 11 of Laframboise & Sonmor [31]); with
   $N_{ein}\approx2.3\times10^{17}$ m$^{-3}$, $T_{ein}\approx2.1$ eV,
   $\Phi_W\approx+17$, $\delta_W/r_e=70$: $\beta_{in}\approx0.56$ and
   $I_{in}\approx1.55$ A, against 1.6 A measured. Shown.
10. **Deorbiting extrapolation** (§6, Figs. 8–9). Calculated from Eq. 3
    with ionospheric parameters of [12,33], not measured: the drag pressure
    $\bar F_x=0.5c_x(\theta)\rho_iU_\infty^2$ at 700 km against $B_W$
    (0.1–3 T), and at 250–800 km for $B_W=0.8$ T. The text (pp. 722–723)
    states that a 0.6–0.8 T field gives a pressure close to that of
    $E_i\approx3.5$ and 6 keV Xe$^+$ ions on an SDO irradiated with a
    plasma beam of divergence half-angle $\psi\sim6^\circ$ from $z=10$ and
    $z=20$ m, i.e. only the 4.04 and 1.44 mN/m$^2$ cases (LEOSWEEP
    [35,36,38]; reorbiter [34]), "confirmed by the data in Fig. 9"
    ($B_W\approx0.8$ T, 250–800 km). Reader's reading of Fig. 8 (700 km):
    the 0.6–0.8 T range of curve 1 gives about 1.1–1.6 mN/m$^2$, matching
    only 1.44 mN/m$^2$; markers 3, 4 and 5 sit on curve 1 at about 2.6,
    1.4 and 2 T. Neutral drag at
    700–800 km is "nearly three orders of magnitude smaller than the
    Lorentz drag pressure". Two schemes are proposed: a "sleeping magnet"
    fitted before launch and unshielded at end of life, or a magnetic
    "harpoon" attached by a servicer. Calculated and proposed; not tested.
11. **Plasma-formation density** (§7, Fig. 5b). The charged-particle
    density in the artificial plasma formation near the surface is 1.5–2
    orders of magnitude above that of the incident flow (isodensity lines
    $1.6\times10^{10}$ to $2.3\times10^{11}$ cm$^{-3}$, read from the
    figure). Shown.

# Methods

* **Experiment only.** No simulation code of the authors'. The calculations
  compared with are literature results: reentry MHD [1–3], [19];
  magnetic-sail MHD and PIC [5,6,21,22].
* **Facility** (§2.2, Fig. 1). Cylindrical vacuum chamber 1.2 m × 3.5 m,
  oil-free pumping and LN$_2$ cryopanels, residual pressure
  $5\times10^{-5}$ N/m$^2$ (CO+N$_2$, H$_2$), working pressure
  $4\times10^{-3}$ N/m$^2$, N$_2$ working gas, uniform beam cross-section
  about 0.3 m. Diagnostics: 5.45 GHz microwave interferometer, cylindrical,
  plane and multi-electrode probes, Faraday cup, two-channel pressure
  transducer [16], mass spectrometer; probe positioning ±0.5 mm, ±0.5°.
* **Models** (§3). Teflon spheres $r_{W1}=4.35\times10^{-2}$ m and
  $r_{W2}=5.25\times10^{-2}$ m with internal solenoids (1400 and 2700 turns
  of 0.75 mm Cu wire). Surface field from $8\times10^{-3}$ T (0.5 A) to
  about $2\times10^{-1}$ T (10 A, short pulses); $1.1\le P_m\le7.2$ A·m$^2$
  (fluxgate magnetometer, ±$10^{-2}$ A·m$^2$). Outside the sphere the field
  is dipolar: $B_z=P_m/2\pi z^3$, $B_\rho=P_m/4\pi\rho^3$. Angular position
  error ±20′.
* **Force measurement** (§3). A compensation moving-coil microbalance
  (0.5 m arm, $10^{-8}$–$10^{-3}$ N, ±4.5%) and a strain-gauge microbalance
  ($10^{-6}$–$10^{-1}$ N, ±3%).
* **Plasma-formation generator** (§5). A 2 mm epoxy layer on a 20 mm
  dielectric disk under a perforated Cu diaphragm (2 mm holes), at the
  frontal point or 3 mm ahead of the sphere, biased $\varphi_W\approx+35$ V.
  Collected electrons heat it to about 120 °C; epoxy pyrolysis releases
  H$_2$O 34.1%, toluene 57.2%, C$_2$H$_4$CO 3.83% ([29], Table 2.4), which
  the beam electrons ionize. Jet: $m_{in}\approx63$ amu,
  $T_{in}\approx550$ K, $V_{in}\approx3.8\times10^2$ m/s,
  $3\times10^{-6}\le P_{in}/P_{BW}\le2\times10^{-5}$. The reactive (thrust)
  force of the jet is neglected. Diagnostics: single cylindrical Langmuir
  probe, microwave and photometric methods [30].
* **Ionospheric extrapolation** (§6). Eq. 3 with plasma parameters from
  Gurevich & Shvartsburg [12] and ECSS-E-ST-10-04C [33], medium solar
  activity; neutral drag with $c_{0x}=2.0$ and fully diffuse scattering.
  The ionospheric parameters are not tabulated.

# Tests and results

| Case | Section | Conditions | Result |
|---|---|---|---|
| Flow visualization | §3, Fig. 2 | $r_{W2}$, $P_{BW}/P_d\approx4.8\times10^3$; $B_W=0$, $\theta\approx0^\circ$, $\theta\approx80^\circ$ | standoff collisionless shock at $\theta\approx0$; mini-magnetosphere at $\theta\approx\pi/2$ |
| $c_x(0)/c_{0x}$ vs $P_{BW}/P_d$ | §3, Fig. 3 | (1) $r_{W1}$, 11.5 km/s, $4\times10^{15}$ m$^{-3}$; (2) $r_{W2}$, 15.6 km/s, $2\times10^{15}$ m$^{-3}$; (3) $r_{W2}$, 28.3 km/s, $9.6\times10^{15}$ m$^{-3}$; literature 4–8 | ≈1.1 at $5\times10^1$ to ≈4.8 near $10^5$ (read); fit Eq. 1 |
| Literature point [5] | §3 | numerical, $\theta\approx0$ | $c_x=4.334\pm0.54$ (abscissa: see Recorded as printed) |
| $c_x(\theta)/c_x(0)$ | §3, Fig. 4 | $P_{BW}/P_d=2.5\times10^4$, $\theta=0$–90° | ≈0.65 at 90°; fit Eq. 2 |
| Mini-magnetosphere | §4, Fig. 2c | $L/r_W\approx4.6$, 28.3 km/s, $9.6\times10^{15}$ m$^{-3}$, $B_W\approx3.9\times10^{-2}$ T | regime of claim 6 |
| $c_x(\pi/2)$ | §4, Eq. 6, Table 2 | $L/r_W$ 4.3–5.9 | 2.7–4.2; fit within 7% |
| Injection, $\theta=\pi/2$ | §5 | $I_{in}\approx1.6$ A, $\delta_W=10^{-2}$ m, $L/r_W\approx5.0$ | $F_{\Sigma x}/F_x\approx3.81\pm0.2$ measured, 3.72 calculated; $c_{\Sigma x}\approx12.2\pm1.4$ |
| Injection, $\theta=0$ | §5, Fig. 6a | $P_{BW}/P_d=7.81\times10^3$, $\alpha=\gamma=\pi$ | $c_{xin}\approx2.68\pm0.15$, $c_x=4.85\pm0.25$, $c_{\Sigma x}\approx13.0\pm1.64$ |
| $c_{xin}(\theta)$ | §5, Table 3, Fig. 7 | $\gamma=\pi/2$, $L/r_W\approx5.0$; error ≤±5% | $\theta=\pi/2$: 3.81; $5\pi/12$: 3.74; $\pi/3$: 3.56; $\pi/4$: 3.22; 0: 2.56 |
| Ionospheric drag at 700 km | §6, Fig. 8 | $B_W$ 0.1–3 T; $\theta=0$ dayside, $\theta=\pi/2$ nightside | comparison points: LEOSWEEP 3.5 keV Xe$^+$, $z=7$ m 8.43 mN/m$^2$, $z=10$ m 4.04 mN/m$^2$; reorbiter 6 keV, $z=20$ m, $\psi\sim3^\circ$ 5.78 mN/m$^2$, $\psi\sim6^\circ$ 1.44 mN/m$^2$ |
| Drag vs altitude | §6, Fig. 9 | $B_W=0.8$ T, 250–800 km, day/night, medium solar activity | Lorentz drag ≈1–5 mN/m$^2$ (read); neutral drag ≈$2\times10^{-3}$ mN/m$^2$ at 800 km (read) |

Reader's cross-checks of printed numbers (all with $\mu=\mu_0$), consistent:

* §4: $P_{BW}\approx605$ Pa at $B_W=3.9\times10^{-2}$ T; $P_d\approx0.125$ Pa
  at $9.6\times10^{15}$ m$^{-3}$, 19.6 amu, 28.3 km/s; ratio
  ≈$4.8\times10^3$, and $\tfrac12(4.6)^6\approx4.7\times10^3$, matching
  Fig. 2's $4.8\times10^3$.
* Eq. 1 at $7.81\times10^3$ gives $f_1\approx2.43$, so $c_x\approx4.85$
  with $c_{0x}=2$, the measured value.
* Eq. 6 gives 3.17 at $L/r_W=5.0$ and 3.88 at 5.874 (Table 2: 3.2, 3.89).
  Since $\tfrac12(L/r_W)^6=P_{BW}/P_d$ by Eq. 5, Eq. 6 is Eq. 1 times
  $\xi=f_2(\pi/2)=0.653$.
* Eq. 8 against Table 3: $3.81\,f_2(5\pi/6)\approx3.55$ (table 3.56);
  $3.81\times0.653\approx2.49$ (table 2.56).
* $3.2\times3.81=12.19$ and $4.85\times2.68=13.0$.

# Notation map

| Shuvalov et al. (2018) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $c_x$, $c_{0x}$ | $C_D$, $C_{D0}$ | referred to $P_d$ and the sphere cross-section $A_W$ |
| $c_{\phi x}$, $c_{xin}$, $c_{\Sigma x}$ | words (Coulomb drag coefficient; injection factor; total drag coefficient) | |
| $P_d=\rho_iU_i^2/2$ | $p_{\mathrm{dyn}}$ | same convention |
| $P_{dL}=\rho_iU_i^2$ | $2p_{\mathrm{dyn}}$ (stagnation pressure) | |
| $P_{BW}=B_W^2/2\mu$ | $p_{Bw}$ | |
| $\mathbf B_W$, $B_W$ | $B_w$ | the equatorial surface field in Eq. 5 ($P_m=4\pi B_Wr_W^3$) |
| $B_0$ | $\mathbf B$ | external facility field |
| $B_L$ | words (field at the standoff boundary) | undoubled in Eq. 4, doubled in §4–§5 (see Recorded as printed) |
| $r_W$, $r_{W1}$, $r_{W2}$ | $r_w$ | |
| $L$ | $L_{\mathrm{so}}$ | **collision:** registry $L$ is a domain length |
| $\theta$ (angle between $\mathbf B_W$ and $\mathbf U_i$) | words (field–flow angle) | **collision:** registry $\theta$ is the azimuthal coordinate |
| $\alpha$ (angle between $\mathbf U_i$ and $\mathbf V_{in}$) | words | collides by letter with $\alpha_{\mathrm B}$, $\alpha_E$ |
| $\gamma$ (angle between $\mathbf V_{in}$ and $\mathbf B_W$) | words | **collision:** registry $\gamma$ is the polytropic index |
| $P_m$ | words (magnetic dipole moment) | used as $\mu_0$ times the SI moment; visual collision with $P$, $P_c$ |
| $\mu$ | $\mu_0$ | the paper calls it "magnetic permeability" |
| $\sigma$ | words (electrical conductivity) | **collision:** registry $\sigma_{sk}$ is a cross section |
| $N_i$, $N_{ein}$ | $n_i$, $n_e$ | |
| $U_i$, $U_\infty$ | $u_i$ | beam or flight speed |
| $T_e$, $T_i$, $T_n$ | $T_e$, $T_i$, $T_n$ | eV |
| $m_i$, $m_e$ | $m_i$, $m_e$ | |
| $k$ | $k_B$ | **collision:** registry $k$ is a wavenumber |
| $\lambda_d$ | $\lambda_D$ | |
| $\omega_{ep}$ | $\omega_{pe}$ | |
| $\omega_{\alpha B}$ | $\omega_{ce}$ (electrons), words (ions) | |
| $\nu_{\alpha m}=\nu_{\alpha i}+\nu_{\alpha n}$ | $\nu_{ei}+\nu_{en}$ (electrons) | |
| $\omega_{\alpha B}\nu_{\alpha m}^{-1}$ | $\Omega_e$ (electrons) | |
| $r_i$, $r_e$, $L_i$, $L_{iT}$, $L_{iU}$ | $r_L$ with subscripts | |
| $\Delta$, $\Delta_D$ | words (inertial and diffusive magnetopause thickness) | |
| $\mathrm{Re}_m$, $\mathrm{Re}_{mL}$ | words (magnetic Reynolds number) | not in the registry |
| $M$ | words (Mach number) | |
| $\mathrm{Kn}_i$, $\mathrm{Kn}_{ii}$ | $\mathrm{Kn}$ | |
| $l_{ii}$ | $\lambda_{\mathrm{mfp}}$ | |
| $\varepsilon_i$ | words (ionization degree) | |
| $F_x$, $F_{in}$, $F_{\Sigma x}$ | words (drag forces) | registry $F$ is thrust |
| $\varphi_W$, $\Phi_W=e\varphi_W/kT_e$ | differences of $\phi$; words | |
| $\eta=2e\varphi_W/m_iU_i^2$ | words | **collision:** registry $\eta$ is thrust efficiency |
| $\xi$ | words (fit constant 0.653) | also $\xi_{di}$, the dissociation degree |
| $\beta_{in}$, $I_{in}$, $\delta_W$ | words (current-collection factor, injected current, radius of the collecting diaphragm element) | |

# Pages created or updated

Chunk 3 (2026-10-15). This source is cited on:

* [Plasma drag augmentation of a magnetized body](/results/magnetized-body-plasma-drag.md) — created.
* [Ion beam shepherd](/definitions/ion-beam-shepherd.md) — created (§6 comparison).

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Shuvalov_Control_of_the_drag_on_a_spacecraft_in_the_earths_ionosphere.pdf`.
   * **Version.** Publisher's typeset version (Elsevier), 9 pages. Funding:
     NAS of Ukraine Research Grant II-25-18.
   * **Identity.** doi:10.1016/j.actaastro.2018.06.038, printed on page 1
     and checked on Crossref (2026-10-15): title, five authors in this
     order, volume 151, pages 717–725, issued and published-print 2018-10,
     no online date in the record, reference count 39. Page 1: received 10
     October 2017, revised 2 April 2018, accepted 15 June 2018, available
     online 18 June 2018. Page 1 matches the filename.
   * **How it was read.** Full text; the text layer is clean except the
     display formulas, which were read from rendered pages 3–8. Figure
     values are the reader's approximate readings. The grouping of the
     Coulomb-drag formula (§3, attributed to [18]) is ambiguous as printed:
     whether $\eta^{2/3}$ multiplies the exponent argument or the
     exponential is not decidable from the page.
   * **Recorded as printed.**
     * §5 prints $B_W=3.9\times10^{-3}$ T for the $L/r_W\approx5.0$
       injection test. With $P_{BW}/P_d=\tfrac12 5^6\approx7.8\times10^3$
       it implies $P_d\approx7.7\times10^{-4}$ N/m$^2$, below the facility
       range ($8\times10^{-3}$–$1.3\times10^{-1}$, §2.2), and it gives
       $F_{\Sigma x}/F_x\approx27.9$ from the printed formula; $3.9\times10^{-2}$ T
       (the §4 value) gives ≈3.69, matching the printed 3.72. Almost
       certainly a misprint of $3.9\times10^{-2}$ T.
     * $B_L$ changes meaning: Eqs. 4–5 use the undoubled equatorial dipole
       field $B_L=P_m/4\pi L^3$ with $P_m=4\pi B_Wr_W^3$, i.e.
       $B_L=B_W(r_W/L)^3$; §4 and §5 write $B_L\approx2B_W(r_W/L)^3$, the
       doubled boundary field. The second form of the injection formula
       (claim 8) and the calculated 3.72 use the doubled value (with $r_{W2}$;
       $r_{W1}$ gives 3.23); the first form with the Eq. 4 definition would
       give a ratio about twice as far from 1 (reader's check: ≈6.4 instead
       of ≈3.7).
     * The magnetic moment is quoted as $1.1\le P_m\le7.2$ A·m$^2$, but the
       dipole formulas treat $P_m$ as $\mu_0$ times the SI moment
       (T·m$^3$). Reader's check: a 0.2 T surface field on $r_{W2}$ implies
       an SI moment of about $1.4\times10^2$ A·m$^2$, 20–40 times the quoted
       maximum, unless the field is not a centred dipole at the surface; the
       paper does not say.
     * §3 gives the Nishida & Funaki point [5], $c_x=4.334\pm0.54$, at
       $P_{BW}/P_d\approx7.8\times10^4$; Fig. 3 plots it near
       $8\times10^3$ at $c_x/c_{0x}\approx2.2$. Eq. 1 gives ≈2.43 at
       $7.8\times10^3$ and ≈4.05 at $7.8\times10^4$, so the figure placement
       fits and the text value is probably a misprint.
     * Fig. 9: the §6 text assigns curve 5 to the 6 keV reorbiter beam and
       curve 6 to the 3.5 keV LEOSWEEP beam; the caption has them the other
       way round. The text refers to a "curve 8" for the neutral drag; the
       figure has curves 1–7 (neutral is 7).
     * Fig. 8: the text gives points 3–6 as 8.43, 4.04, 5.78 and
       1.44 mN/m$^2$; the plotted markers read about 5.5, 2.9, 4.2 and
       1.15 mN/m$^2$ (log axis, reader's estimate), lower by a near-constant
       factor of 1.3–1.5. Soft flag.
     * Fig. 8 pairs $\theta=0$ with dayside and $\theta=\pi/2$ with
       nightside; Fig. 9 treats angle and day/night as independent (four
       curves). The Fig. 8 pairing is a modelling choice, not a physical
       tie.
     * The Fig. 4 caption cites "[5], Figs. 6 and 8, and [11]"; the text
       cites "[5], Figs. 6, 8, and 11".
     * Eq. 6 gives ≈3.90 at $L/r_W=5.9$ against the measured 4.2, 7.7% low,
       at the edge of the stated "within 7%".
     * Typographical: "Lorenz", "Lolentz", "SDQs", "Fq. (3)",
       "magnetrometer", a Cyrillic "radiнs", "trust" for thrust in ref. [5],
       "AJAA/…/SAF" for AIAA/…/SAE in refs. [10,11], "P.M. Zubrin" in [22].
   * **Reference list.** 39 printed entries ([1]–[39]), merged in full.
     Self-citations: [16,17,18,28,30,36]. The Bombardelli et al. (2011)
     entry matches the existing `bombardelli-2011` (same journal, volume and
     page). Printed oddities are kept in the bibliography notes ([5]
     "trust", [10]/[11] conference names, [22] initials, [33] "Noordwick").
