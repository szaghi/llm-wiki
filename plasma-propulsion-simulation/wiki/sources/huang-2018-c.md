---
type: Source
title: "Huang et al. (2018) — Investigation on dynamic behaviors of thermal protection system using a two degree-of-freedom nonlinear theoretical method"
description: "Models a ceramic thermal-protection tile on a strain-isolation pad with a cubic-stiffness spring as a two-degree-of-freedom system under Gaussian random acoustic or base excitation, replaces it by an equivalent linear system through statistical linearization, and shows that the equivalent pad stiffness and all responses fall below those of a least-squares linear model as the nonlinearity grows."
resource: "doi:10.1016/j.actaastro.2018.07.016"
source_kind: paper
authors: [Huang J., Yao W., Li P., Zhou D., Chang C., Lin H.]
year: 2018
venue: "Acta Astronaut. 151:828–835"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Huang_Investigation_on_dynamic_behaviors_of_thermal_protection_sys.pdf"
tags: [context, thermal-protection-system, random-vibration, statistical-linearization, structural-dynamics]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

The paper models one ceramic thermal-protection-system (TPS) tile bonded
through a strain-isolation pad (SIP) to the orbiter structure as a
two-degree-of-freedom lumped system: the tile as a mass, linear spring and
viscous damper, the SIP as a mass, cubic spring $f_2(u)=au+bu^3$ and damper
(§3.1, Fig. 4). Under stationary Gaussian random excitation (an acoustic
pressure PSD on the tile surface, or a ladder-spectrum base-acceleration PSD
at the SIP bottom), the nonlinear system is replaced by an equivalent linear
one through statistical linearization, which gives an SIP equivalent
stiffness of $a$ plus $3b$ times the mean-square SIP deformation, solved by
fixed-point iteration (§3.2, Eqs. 1–24, Fig. 6). RMS responses follow from
integrating the response PSDs (Eq. 25), the SIP RMS stress from Eqs. 26–27.
For a 150 mm × 150 mm tile (§4) the converged equivalent stiffness is
3.02 kN/mm (acoustic) and 3.27 kN/mm (base), well below the 7.0 kN/mm
least-squares linear fit, and the linear model overpredicts accelerations
and SIP stress. A sweep over five cubic laws with the same fitted linear
stiffness shows stiffness, natural frequencies, damping and responses all
decreasing as the nonlinearity grows. Implemented in MATLAB. Launch
vibro-acoustics only: no thermal load, no aerothermodynamics, nothing on
plasma or propulsion.

# Key claims

Symbols are the paper's (see the notation map).

1. **Equivalent stiffness** (§3.2, Eqs. 16, 20, 22, 24, derived): the
   equivalent mass and damping matrices vanish and only the (2,2) stiffness
   entry changes, $K_{e22}=k_1+a+3bE(x_2^2)$ (acoustic) or
   $k_1+a+3bE[(x_2-y)^2]$ (base), hence $k_{e2}=a+3bE(x_2^2)$ or
   $a+3bE[(x_2-y)^2]$ (Eq. 24). This is the standard Gaussian-closure result
   for a cubic spring, obtained through the Atalik–Utku theorem (ref. [17],
   Eq. 9).
2. **Excitation dependence** (§4, Figs. 8–9, shown numerically): for
   $a=2.0\times10^6$ and $b=2.0\times10^{12}$ (N and m), starting from
   7.0 kN/mm, the iteration converges to 3.02 kN/mm (acoustic) and
   3.27 kN/mm (base).
3. **Natural frequencies** (Table 2): linear SIP (7.0 kN/mm)
   $3.13\times10^3$ and $2.36\times10^4$ rad/s for both excitations;
   nonlinear base $2.26\times10^3$ / $2.24\times10^4$ rad/s; nonlinear
   acoustic $2.18\times10^3$ / $2.23\times10^4$ rad/s.
4. **RMS responses** (Table 3): nonlinear base, SIP acceleration
   $2.53\times10^3$ m/s², SIP stress 0.072 MPa, tile acceleration
   $2.83\times10^3$ m/s²; nonlinear acoustic $2.11\times10^3$ m/s²,
   0.057 MPa, $2.30\times10^3$ m/s²; linear base $3.32\times10^3$ m/s²,
   0.11 MPa, $4.17\times10^3$ m/s²; linear acoustic $2.76\times10^3$ m/s²,
   0.087 MPa, $3.44\times10^3$ m/s². The linear model overpredicts every
   response.
5. **Nonlinearity sweep** (§4, Table 4, Figs. 10–13): over five cubic laws,
   $(a/10^6, b/10^{12})$ = (6.0, 0.5), (4.0, 1.0), (3.0, 1.5), (2.0, 2.0),
   (0, 2.5), the equivalent stiffness falls from 6.17/6.13 kN/mm (level 1,
   base/acoustic) through 4.47/4.36, 3.83/3.64, 3.27/3.02 to 2.25/1.94 kN/mm
   (level 5), read from the Fig. 11 bar labels; natural frequencies,
   viscous damping coefficients, accelerations and SIP stress also decrease
   (trends only).
6. **Model adequacy** (§1, §5, stated): the SIP nonlinearity must be
   considered "when the nonlinear effect is obvious"; the linear
   single-degree-of-freedom model of George and Doyle (ref. [14]) gives
   inaccurate responses. Not quantified beyond this example and not
   compared with experiment.
7. **Background** (attributed): the SIP load–displacement law is
   approximately cubic (refs. [10,11], §3.1); SIP stiffness is nonlinear
   (refs. [12,13], §1); Miserentino et al. (ref. [10]) observed a dynamic
   instability with large in-plane motion at half the driving frequency.

# Methods

Two-degree-of-freedom chain structure–SIP–tile with $f_1(u)=k_1u$ and
$f_2(u)=au+bu^3$; coating neglected; stationary Gaussian excitation, acoustic
load uniform on the tile surface with fixed structure, or base excitation
uniform at the SIP bottom (§3.1). Equations of motion Eq. 1 (acoustic
Eqs. 13–15, base Eqs. 17–19). Statistical linearization (§3.2): minimise the
mean-square equation error over the equivalent matrices (Eqs. 2–8) and
apply the Gaussian theorem $E[ZQ_i(Z)]=E[ZZ^T]E[\nabla Q_i(Z)]$ (Eq. 9),
giving each equivalent coefficient as the expected partial derivative of
the restoring force (Eq. 11). Iteration (Fig. 6): guess the stiffness,
solve the linear random-vibration problem, update by Eq. 24, repeat;
tolerance not stated. Mean squares by integrating response PSDs (Eq. 25);
SIP RMS stress $\psi_\sigma^a=(k_{e2}\psi_{x_2}+c_2\psi_{\dot x_2})/S$
(acoustic, Eq. 26) and $\psi_\sigma^b=(m_1\psi_{\ddot x_1}+m_2\psi_{\ddot x_2})/S$
(base, Eq. 27); structural loss factor converted as $c_n=g\,m_n\omega_n$
(Eq. 28). Data (§4, Table 1): tile thickness 54.8 mm, SIP 5.2 mm; tile
Young's modulus 60.0 MPa, Poisson ratio 0.25, density 420 kg/m³, loss factor
0.04; SIP nonlinear modulus, Poisson ratio 0.4, density 521 kg/m³, loss
factor 0.04. Acoustic PSD 100 N²/Hz band-limited white noise over
20–2000 Hz; base PSD (Fig. 3, $G=9.8$ m/s²) 0.02 G²/Hz at 20 Hz rising to
5 G²/Hz at 100 Hz, flat to 1000 Hz, falling to 1 G²/Hz at 2000 Hz (read from
the figure's point labels).

# Tests and results

Case A ($a=2.0\times10^6$, $b=2.0\times10^{12}$; claims 2–4) and the Case B
sweep (claim 5; level 4 is Case A). Reader's check: with tile mass
$m_1=0.518$ kg, SIP mass $m_2=0.0610$ kg (density × thickness × area) and
$k_1=E_1S/t_1=2.46\times10^7$ N/m (the paper does not state the formula for
$k_1$; inferred), the two-degree-of-freedom eigenvalues reproduce Table 2
exactly for 7.0, 3.27 and 3.02 kN/mm; Eq. 27 with these masses and the
Table 3 accelerations gives 0.072 MPa (nonlinear base) and 0.105 MPa (linear
base, printed 0.11).

# Notation map

Structural-dynamics symbols; none has a registry counterpart except an
angular frequency.

| Huang et al. (2018) | Registry | Note |
|---|---|---|
| $m_1$, $m_2$ | words (tile and SIP masses) | **collision:** registry $m_s$ is a species mass |
| $k_1$, $k_{e2}$, $a$, $b$ | words (tile stiffness, SIP equivalent stiffness, cubic-law coefficients) | **collision:** registry $k$ wavenumber, $k_B$, $k_{\mathrm{ion}}$ |
| $c_1$, $c_2$, $c_n$, $g$ | words (viscous damping coefficients, structural loss factor) | $c$ is not the speed of light; $g$ is not the relative collision speed |
| $x_1$, $x_2$, $y$ | words (tile, SIP and base displacements) | not the Cartesian coordinates of the registry |
| $\omega$, $\omega_n$ | words (natural frequency, spectral variable) | the registry $\omega$ is a mode angular frequency; **internal collision:** $\omega_1$, $\omega_2$ are both the natural frequencies (Table 2) and the integration limits (Eq. 25) |
| $S$ | words (tile/SIP surface area) | **collision:** registry $S(\mathbf x)$ is the shape function |
| $S_f$, $S_{\ddot y}$, $S_{\ddot x_i}$, $\psi$ | words (PSDs, RMS values) | |
| $E(\cdot)$, $E_1$ | words (expectation, Young's modulus) | **internal collision** in the paper; not the electric field |
| $\nu$, $\rho$ | words (Poisson ratio, density) | **collision:** registry $\nu_{sk}$, $\rho_c$ |
| $\varepsilon$ | words (linearization error vector) | not $\varepsilon_0$ |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Huang_Investigation_on_dynamic_behaviors_of_thermal_protection_sys.pdf`.
   * **Version.** Publisher's final version (Elsevier, © 2018 IAA), 8
     pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.07.016, printed on page 1
     and checked on Crossref: title, all six authors, Acta Astronaut.
     151:828–835 match; issued 2018-10, no published-online field. Page 1:
     received 27 Apr 2018, revised 11 Jun 2018, accepted 10 Jul 2018, online
     11 Jul 2018. Page 1 matches the filename title. Third of the three
     Huang 2018 files in archive-filename order, hence `huang-2018-c`.
   * **How it was read.** Clean text layer; pages 3, 5 and 7 also rendered.
     Figs. 1, 2, 5, 6, 8, 12 and 13 (schematics, flowchart, iteration
     history, trend plots) were not digitised; Fig. 3 and Fig. 11 values are
     read from point and bar labels. Not stated in the paper: the iteration
     tolerance, the expression for $k_1$, the fitting range of the
     7.0 kN/mm linear stiffness, the response-PSD transfer functions, and
     the units of $a$ and $b$ (consistent with N/m and N/m³).
   * **Recorded as printed.**
     * The Eq. 1 text calls $\{Q\}$ "[Q] … the elastic force vector".
     * Eqs. 16 and 20 print "$[M_e]=0$" twice; the second line evidently
       means $[C_e]=0$.
     * Eq. 12 writes $f_1(x)=k_1u$, $f_2(x)=au+bu^3$ (argument $x$ on the
       left, $u$ on the right).
     * Nomenclature: "root mean square acceleration of tile and tile";
       Table 3's header uses $\psi_\sigma$ without the a/b superscript.
     * Reader's check (§4 vs Table 4, Fig. 10): the paper states that the
       least-squares linear fits of all five cubic laws are 7.0 kN/mm. A
       continuous least-squares slope through the origin over a common
       range $|u|\le L$ is $a+\tfrac35bL^2$; equality across the five pairs
       would need a constant $\Delta a/\Delta b$, but it is
       $-4\times10^{-6}$ m² (levels 1→2, 4→5) and $-2\times10^{-6}$ m²
       (2→3, 3→4). Over ±2 mm (the range of Fig. 10) the fit gives about
       7.2, 6.4, 6.6, 6.8 and 6.0 kN/mm. Either the fit range differs per
       level or "all 7.0" is approximate.
     * Eqs. 26–27 sum RMS values of the elastic and damping (respectively
       the two inertial) contributions; that equals the RMS of the sum only
       for fully correlated in-phase components, so the stresses are
       upper-bound approximations. Not discussed in the paper.
     * The cubic SIP law is attributed to refs. [10,11] in §3.1 and the
       nonlinear SIP stiffness to refs. [12,13] in §1 (inconsistent
       attribution, not a contradiction).
     * The claim against George and Doyle (ref. [14]) is supported only by
       the paper's own linear-versus-nonlinear comparison, not against ref.
       [14] directly or against experiment.
   * **Reference list.** 17 printed entries ([1]–[17]), matching the
     Crossref reference count.
