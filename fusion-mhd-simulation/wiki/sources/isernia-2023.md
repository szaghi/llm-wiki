---
type: Source
title: "Isernia et al. (2023) — Self-consistent coupling of JOREK and CARIDDI: On the electromagnetic interaction of 3D tokamak plasmas with 3D volumetric conductors"
description: "Couples reduced-MHD JOREK two-way and fully implicitly to the 3D volumetric eddy-current code CARIDDI through a virtual-casing equivalent surface current, verifies the vacuum response against a tilted toroidal wire, benchmarks VDEs and tearing modes against JOREK-STARWALL and CarMa0NL, and shows that wall ports couple toroidal harmonics."
resource: "doi:10.1063/5.0167271"
source_kind: paper
authors: [Isernia N., Schwarz N., Artola F.J., Ventre S., Hoelzl M., Rubinacci G., Villone F., JOREK Team]
year: 2023
venue: "Phys. Plasmas 30:113901"
local_file: "/home/stefano/papers/mosaic/fusion-mhd-simulation/0000_manual_no_journal_Unknown_10106350167271titleSelf-consistent.pdf"
tags: [reduced-mhd, wall, free-boundary, vde, tearing, tokamak, finite-elements, benchmark, code]
timestamp: 2026-10-16T00:00:00Z
---

# Summary

The paper couples the nonlinear reduced-MHD code
[JOREK](/software/jorek.md) with CARIDDI, a 3D eddy-current integral code
that discretizes only the conductors, into a two-way, self-consistent,
fully implicit free-boundary tool for 3D nonlinear plasmas interacting
with 3D *volumetric* (not thin-shell) passive conductors. The coupling is
"indirect" in the Bielak–MacCamy sense and rests on the virtual casing
principle: the plasma's field outside the JOREK domain is represented by
an equivalent surface current on the JOREK boundary, discretized as a thin
CARIDDI shell (thickness 0.1 mm) and obtained in weak form by inverting
the shell inductance matrix against the tangential vector potential that
JOREK supplies. Eliminating the shell currents yields a circuit equation
for the wall currents with a modified wall inductance and plasma–wall
coupling matrices, and a vacuum-response relation for the tangential
poloidal field on the boundary, which is the boundary condition of the
reduced-MHD $\psi$ equation. The structure mirrors JOREK-STARWALL,
including a generalized eigen-decomposition that makes time-step changes
cheap. Only reduced MHD ($\mathbf A=\psi\nabla\phi$) is coupled; the
full-MHD extension is outlined, and halo currents are excluded. The vacuum
response is verified against a tilted toroidal wire (relative RMS error
about 0.1–0.4% for $n=0,1$). Three tests follow: an axisymmetric AUG-like
[VDE](/definitions/vertical-displacement-event.md) benchmarked against
JOREK-STARWALL (growth rates within 2%) and the mass-less CarMa0NL (about
10% late deviation); a large-aspect-ratio $m/n=2/1$
[tearing mode](/definitions/tearing-mode.md) across a wall-resistivity
scan from ideal wall to no wall (JOREK-CARIDDI and JOREK-STARWALL within
1%); and ports in an AUG wall, which couple toroidal harmonics through the
wall and bring the [thermal quench](/definitions/thermal-quench.md) of a 3D
hot VDE forward.

# Key claims

1. **Priority** (§VII). JOREK-CARIDDI is "the first numerical tool
   capable of simulating 3D non-linear MHD plasmas in self-consistent
   interaction with eddy currents in 3D volumetric conductors". Stated.
2. **State of the art** (§I). JOREK-STARWALL is "the only non-linear
   extended MHD code" with self-consistent 3D conductors, limited to thin
   walls; M3D and NIMROD were coupled only to axisymmetric thin walls;
   M3D-C1 puts conductors inside its own domain; CASTOR3D, VALEN and
   MARS-F (linear) use thin conductors only; volumetric-conductor tools
   (CarMa0NL, APEC, CREATE-type) use mass-less axisymmetric or linearized
   3D plasma models, and Bonotto et al. (2020) is the first linear dynamic
   MHD model with fully 3D volumetric conductors. Stated.
3. **Thin-wall limits** (§I). The thin-wall assumption "is not always
   robust" because the skin depth can be comparable to wall widths
   (Pustovitov 2015). Stated.
4. **No halo currents** (§II C, §VII). The equivalent surface current
   represents only solenoidal current distributions inside the MHD
   domain, so currents crossing the boundary need correction terms.
   Derived/Stated.
5. **Consistency with reduced MHD** (§II C). Neglecting the poloidal
   tangential vector-potential component in the shell equation remains
   consistent with the reduced approximation; the result is the normal
   derivative of the interior flux divided by $R$ plus a term cancelling
   the poloidal-component contribution of the external currents. Stated.
6. **Modified wall inductance** (§II D, Eq. 25a). It is the conductor
   inductance modified by a superconducting shell that holds the flux at
   the JOREK boundary constant. Derived (interpretation).
7. **Quadrature sensitivity** (§III, Fig. 2). The vacuum response is more
   sensitive to the quadrature of the shell inductance matrix than to that
   of the shell field matrix, because the former is inverted. Shown.
8. **Resolution trends** (§III, Fig. 3). The RMS error falls with
   poloidal shell subdivision; for $n=2$ also with toroidal resolution
   (arc-versus-chord error). Evaluating the field 1 mm outside the
   boundary adds at most 0.15%. Shown.
9. **Axisymmetric VDE vs JOREK-STARWALL** (§IV, Figs. 4–5). Growth rates
   differ by less than 2% throughout; Fig. 4 fits
   $\gamma=39.87$ s⁻¹ (JOREK-CARIDDI), $39.59$ s⁻¹ (JOREK-STARWALL),
   $44.38$ s⁻¹ (CarMa0NL). Shown.
10. **VDE vs CarMa0NL** (§IV, §VII). Agreement to about 1% initially,
    diverging later to "about 10%"; attributed to plasma-model
    differences ($\psi_N$ profiles held exactly and $I_p$ fixed in
    CarMa0NL, approximately in JOREK via a current source), not to the
    shared conductor model. Shown (numbers), Stated (cause).
11. **Mass-less approximation validated** (§IV, Fig. 6). The
    near-equilibrium relation between passive-stabilizing-loop currents
    and vertical position also holds in JOREK, which "validates
    essentially also the mass-less approximation" for this case; these
    loop currents dominate the slowing of the vertical motion. Shown /
    Stated.
12. **Tearing mode across wall resistivity** (§V, Fig. 7). Circular
    plasma, $R_0=10$ m, $a=1$ m, wall radius 1.1 m: JOREK-CARIDDI and
    JOREK-STARWALL $n=1$ growth rates agree to better than 1% "over
    several orders of magnitude in the wall resistivity". Shown.
13. **Ports raise the tearing growth rate** (§VI, Table I). Equally
    spaced ports raise the $n=1$ growth rate monotonically from 509.5 to
    573.0 rad s⁻¹ for 0 to 8 holes, each hole obstructing the reaction
    eddy currents. Shown.
14. **Wall-mediated harmonic coupling** (§VI, Table I, Fig. 8). With 2, 4,
    6 or 8 holes there is no wall-mediated $n=1$/$n=2$ coupling, and $n=2$
    is driven nonlinearly with $\gamma_2\approx2\gamma_1$; with 1 or 3
    holes the harmonics couple through the wall, $n=2$ starts earlier and
    $\gamma_2\approx\gamma_1$. Shown. The split follows from keeping only
    $n=1,2$; more harmonics could add indirect coupling. Stated.
15. **Harmonic selection** (§VII). "It may be necessary to tune the
    number of toroidal harmonics to include in the plasma model according
    to the toroidal periodicity of external conductors." Stated
    (inference from claim 14).
16. **3D hot VDE with one port** (§VI, Fig. 10). A midplane or bottom
    port slightly raises the vertical growth rate; the $n>0$ energies jump
    at the control-coil kick to the same amplitude in both codes; the
    thermal quench comes earlier and at larger $q_{95}$. Shown.
17. **Accuracy of the exterior field** (§VII). Represented "up to an
    error of 0.2%". Stated; see Recorded as printed.
18. **Outlook** (§VII). Full-MHD free-boundary coupling, halo currents,
    stellarators, matrix compression beyond 500k wall degrees of freedom,
    n-fold symmetry. Stated.

# Models and numerics

* **Plasma model (JOREK).** Reduced MHD with
  $\mathbf A=\psi\nabla\phi$ (Eq. 1); full MHD (all components of
  $\mathbf A$, Weyl gauge) is not coupled here. The toroidal component of
  Ampère's law gives the support variable
  $$j=-\mu_0RJ_\phi=\Delta^*\psi=R\Big[\partial_R\Big(\frac{\partial_R\psi}{R}\Big)+\partial_Z\Big(\frac{\partial_Z\psi}{R}\Big)\Big]\quad(\text{Eq. 2}),$$
  whose weak form (Eq. 3) carries the boundary term
  $\oint\hat\lambda\,R^{-1}\partial_{\mathbf n}\psi\,d\ell$ over the JOREK
  boundary ($\hat\lambda$ a Bézier × Fourier test function, words in the
  registry). The required electromagnetic boundary condition is
  $R^{-1}\partial_{\mathbf n}\psi$, only part of the tangential poloidal
  field; full MHD would need both tangential components. Bézier $G^1$
  elements poloidally ([Bézier finite elements](/methods/bezier-finite-elements.md)),
  Fourier toroidally. SI units with $\mu_0$ explicit.
* **Conductor model (CARIDDI).** Magneto-quasi-static integral
  formulation on the conductor volume only:
  $\mathbf E=-\partial_t\mathbf A-\nabla\Phi$, $\mathbf A$ the Biot–Savart
  integral of the conductor current plus the plasma source potential
  (Coulomb gauge), and Ohm's law $\eta_w\mathbf J=\mathbf E$ in weak
  Galerkin form. The current basis is the curl of an electric vector
  potential expanded in edge functions with a tree–cotree gauge; normal
  current is continuous across faces. The result is a circuit equation:
  resistance matrix times wall currents plus inductance matrix times their
  time derivative plus induced source voltages plus electrode terms equal
  zero (Eqs. 7–11). Plasma-facing electrodes, needed for halo currents,
  are excluded. The wall field on the boundary is a Biot–Savart sample
  projected onto the Bézier space (Eq. 12).
* **Virtual casing** (§II C, attributed to Shafranov & Zakharov). An
  equivalent surface current on the boundary reproduces the plasma's
  exterior field (Eq. 13); it is imposed weakly against tangential,
  surface-divergence-free test functions (removing the gauge) on a thin
  volumetric shell. JOREK supplies the total tangential $\mathbf A$; the
  interior part is the total minus the wall contribution (Eqs. 16–18). In
  reduced MHD the poloidal tangential component is dropped. The shell
  field is evaluated 1 mm outside the boundary, because the equivalent
  current makes $\mathbf B$ discontinuous there.
* **Resulting formulation** (§II D). Eliminating the shell currents
  gives (Eqs. 24–25) a wall circuit equation with a modified inductance
  (wall inductance minus wall–shell mutual inductance × inverse shell
  inductance × shell–wall mutual inductance) and a coupling matrix
  multiplying the time derivative of the boundary $\psi$; and (Eqs. 26–27)
  the boundary tangential poloidal field as a linear function of the wall
  currents and of the boundary $\psi$. As in JOREK-STARWALL, the
  generalized eigenproblem of modified inductance against resistance is
  solved once (Eq. 28); in its eigenbasis the wall equation is diagonal
  and easy to invert when the implicit $\Delta t$ changes.
* **Shell mesh.** Each JOREK boundary element is split into poloidal
  sub-elements, offset by half the shell thickness on either side, and
  replicated toroidally with hexahedra or pentahedra; built inside CARIDDI
  from the JOREK boundary data. An automatic test checks the response
  matrices against the analytic field of a tilted toroidal wire.
* **Time integration.** Fully implicit (JOREK); coupling matrices
  computed once by CARIDDI; parallel I/O and matrix distribution taken over
  from JOREK-STARWALL. Runs on Marconi-Fusion; no run times, time steps,
  wall degrees of freedom or GPU use reported.
* **See also** [free-boundary and resistive-wall coupling](/methods/resistive-wall-coupling.md)
  for the general method.

# Tests and results

* **Vacuum-response test** (§III): AUG-like boundary with 50 boundary
  nodes, tilted toroidal wire, relative RMS error per Fourier harmonic
  (Eq. 29); shell edge aspect ratio $\simeq0.14$, so the toroidal
  quadrature matters.
  * Fig. 2 (8 poloidal subdivisions, 90 toroidal elements, $n=1$): about
    1.5% with 2 toroidal Gauss points for the inductance, about 0.6% with
    4, plateau 0.36–0.37% from 6; the field-matrix quadrature has little
    effect.
  * Fig. 3a: $n=0$ from about 0.5% to 0.1% and $n=1$ from about 1.5% to
    0.25% as poloidal subdivisions go from 4 to 12.
  * Fig. 3b ($n=2$): 1.4–2% with 90 toroidal elements, 0.45–1.5% with
    120 (non-monotonic, minimum near 10 subdivisions).
* **Axisymmetric AUG-like VDE** (§IV): $n=0$ only; wall plus two passive
  stabilizing loops (thin bands in STARWALL, bulky conductors in
  CARIDDI); triggered by a current kick in the vertical control circuit;
  an artificial current source holds the profiles.

  | Code | $\gamma$ [s⁻¹] (Fig. 4 fit) |
  |---|---|
  | JOREK-CARIDDI | 39.87 |
  | JOREK-STARWALL | 39.59 |
  | CarMa0NL | 44.38 |

  With a 10 ms fit window (Fig. 5) the JOREK growth rate falls from about
  110 s⁻¹ (5 ms) to about 28 s⁻¹ (60 ms), while CarMa0NL levels at about
  40–43 s⁻¹. Loop currents $\pm30$ kA for displacements up to 20 cm agree
  across the three codes (Fig. 6).
* **Tearing mode** (§V): no-pressure circular equilibrium unstable to
  2/1, $R_0=10$ m, $a=1$ m, circular wall of radius 1.1 m and thickness
  5 mm, nominal $\eta_w=5\times10^{-7}$ Ω m (equivalent to the STARWALL
  thin-wall $\eta_w/d_w=10^{-4}$ Ω), pentahedra, 120 toroidal elements, 10
  poloidal subdivisions. Wall resistivity scanned by factors
  $10^{-4}$–$10^4$: the $n=1$ growth rate rises from about 630 s⁻¹ (ideal
  wall) to about 960 s⁻¹ (no wall), the two codes within 1% (Fig. 7).
* **Ports and harmonic coupling** (§VI, Table I): AUG-like 2/1 tearing
  equilibrium ($n=2$ linearly stable), no loops, equally spaced bottom
  holes of 30° toroidal and 49.8° poloidal extent, harmonics $n=1,2$ only.

  | Holes | 0 | 1 | 2 | 3 | 4 | 6 | 8 |
  |---|---|---|---|---|---|---|---|
  | $\gamma_{n=1}$ [rad s⁻¹] | 509.5 | 518.7 | 532.9 | 534.4 | 541.8 | 559.7 | 573.0 |
  | $\gamma_{n=2}$ [rad s⁻¹] | 1019.0 | 523.7 | 1065.9 | 535.9 | 1083.4 | 1119.0 | 1144.0 |

* **3D hot VDE with a single port** (§VI, Figs. 10–11): axisymmetric
  wall, midplane port (92.4° poloidal) or bottom port, centred at
  $\phi=-90°$, toroidal extent 33.75°, loop resistance artificially
  increased; $n=1,2,3$ added after an axisymmetric phase; downward VDE
  started by a control-coil kick. With ports, the vertical growth rate is
  slightly higher and the thermal quench earlier (about 12 ms vs 12.5 ms
  by eye) at larger $q_{95}$; $J_\phi$ deviates around the hole.

# Notation map

| Isernia et al. (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $(r,z,\varphi)$ | $(R,Z,\phi)$ | **collision:** registry $r$ is the minor radius; $\varphi$ orientation not stated |
| $\theta$ (boundary tangent direction) | words | poloidal direction along the boundary |
| $\phi$ (electric scalar potential), $\underline\phi$ (electrode potentials) | $\Phi$; words | **collision:** registry $\phi$ is the toroidal angle |
| $\mathbf A$, $\psi$ | $\mathbf A$, $\psi$ | $\psi=RA_\phi$, per radian, SI |
| $A_\theta$ | words (poloidal tangential component of $\mathbf A$) | full MHD only |
| $\mathbf j$, $j_\varphi$ | $\mathbf J$, $J_\phi$ | |
| $j=-\mu_0rj_\varphi=\Delta^*\psi$ | $j=-\mu_0RJ_\phi=\Delta^*\psi$ | sign stated |
| $\lambda$ (test functions, Eqs. 3, 17, 19–20) | words ($\hat\lambda$ above) | **collision:** also the eigenvalue of Eq. 28 in the paper |
| $\eta$ (conductor) | $\eta_w$ | possibly tensorial |
| $\eta_{wall,thin}$ | $\eta_w/d_w$ | Ω |
| $\mathbf T$ | words (electric vector potential, $\mathbf J=\nabla\times\mathbf T$) | **collision** with temperature $T$ |
| $\mathbf w_k$ | words (CARIDDI solenoidal current basis) | **collision risk** with $w_p$ |
| $R_w$, $L_w$, $F$ | words (resistance, inductance, electrode incidence matrices) | **collision:** registry $F=RB_\phi$ |
| $S_j$ | words (electrode surfaces) | **collision** with Lundquist number $S$ |
| $\mathbf k_{eq}$, $V_{eq}$, $d_{eq}$ | words (equivalent surface current, shell, shell thickness) | |
| $H_\varphi$, $H_\theta$, $M_{eq,w}$, $M_{w,eq}$, $L_{eq}$ | words | shell coupling and inductance matrices |
| $L^*_w$, $N_\varphi$, $N_\theta$ | words (modified wall inductance, coupling matrices) | |
| $B_\theta$, $B^*_{\theta,w}$, $C_{\theta,\varphi}$, $C_{\theta,\theta}$ | words (tangential poloidal field; vacuum-response matrices) | |
| $S_\lambda$, $\lambda$ (Eq. 28) | words (generalized eigenvectors, eigenvalues) | eigenvalues are time constants |
| $n_{sub,\theta}$, $n_\varphi$, $n_L$, $n_B$, $n_{bnd}$ | words | resolution and quadrature counts |
| $\gamma$ | $\gamma$ | growth rate; Table I in rad s⁻¹, figures in s⁻¹ |
| $q_{95}$, $\psi_n$/$\psi_N$, $n$ | $q_{95}$, $\psi_N$, $n$ | |
| $p'$, $FF'$ | words (equilibrium profile derivatives) | $F=RB_\phi$ implied, not defined |

# Pages created or updated

Chunk 1 (2026-10-16) created every page of the bundle; chunk 2 (2026-10-16) extended many. This source is cited on:

* [Bézier–Hermite finite elements with toroidal Fourier harmonics](/methods/bezier-finite-elements.md)
* [CARIDDI](/software/cariddi.md)
* [CASTOR3D](/software/castor3d.md)
* [Divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
* [Free-boundary and resistive-wall coupling](/methods/resistive-wall-coupling.md)
* [Grad–Shafranov equation](/definitions/grad-shafranov-equation.md)
* [Halo current](/definitions/halo-current.md)
* [JOREK](/software/jorek.md)
* [M3D](/software/m3d.md)
* [M3D-C1](/software/m3d-c1.md)
* [MARS-F](/software/mars-f.md)
* [NIMROD](/software/nimrod.md)
* [Reduced MHD for tokamaks](/methods/reduced-mhd.md)
* [Resistive tearing mode](/definitions/tearing-mode.md)
* [Resistive-wall tearing mode](/definitions/resistive-wall-tearing-mode.md)
* [STARWALL](/software/starwall.md)
* [Thermal quench](/definitions/thermal-quench.md)
* [Toroidal mode families in stellarators](/definitions/toroidal-mode-family.md)
* [Vertical displacement event (hot and cold VDE)](/definitions/vertical-displacement-event.md)

# Citations

1. `/home/stefano/papers/mosaic/fusion-mhd-simulation/0000_manual_no_journal_Unknown_10106350167271titleSelf-consistent.pdf`.
   * **Version.** Publisher version of record (AIP, open access CC BY
     4.0) with the AIP cover page; 14 PDF pages = cover + article pp.
     113901-1 to 113901-13. Submitted 11 Jul 2023, accepted 4 Oct 2023,
     online 2 Nov 2023. The filename carries no metadata.
   * **Identity.** doi:10.1063/5.0167271, checked on Crossref: Phys.
     Plasmas 30(11), article 113901, issued 2023-11-01; authors Isernia,
     Schwarz, Artola, Ventre, Hoelzl, Rubinacci, Villone and the group
     author JOREK Team.
   * **How read.** Full text. Equations transcribed from the extracted
     text; the reader notes do not list rendered-page checks. Plot values
     are approximate readings; Table I is transcribed.
   * **Recorded as printed.**
     * Eq. 3: integrating $(\hat\lambda/R)\Delta^*\psi$ by parts, with
       Eq. 2 as a 2D divergence of $R^{-1}\nabla\psi$, gives a volume term
       weighted by $1/R$; the print has $1/R^2$ (compiler's check, assuming
       the poloidal-plane area element as written). The boundary term
       matches.
     * Sign of the boundary condition: $R^{-1}\partial_{\mathbf n}\psi$ in
       §II A, "exactly $-(1/r)\partial\psi_{in}/\partial n$" in §II C; not
       reconciled.
     * $\lambda$ denotes both the JOREK test functions and the eigenvalue
       of Eq. 28; §III writes "$B_{eq}$ (23)" for the shell field matrix.
     * §VII claims the exterior field is represented "up to an error of
       0.2%"; Figs. 2–3 show plateaus of about 0.36% and 0.25% ($n=1$) and
       0.45–2% ($n=2$); only $n=0$ (about 0.1%) is below 0.2%.
     * CarMa0NL deviation: "1%" growing (§IV), "about 10%" (§VII), and
       44.38 vs 39.87 s⁻¹ = 11.3% in the Fig. 4 legend, whose fit window is
       not stated.
     * Port toroidal extents: 30° (equally spaced holes) and 33.75°
       (single port).
     * Table I caption says "ASDEX tearing mode test case", the text
       "AUG-like geometry" (same case). At even hole counts $\gamma_{n=2}$
       is about $2\gamma_{n=1}$ (exactly at 0 holes; 1144.0 vs 1146.0 at 8).
     * Growth rates in rad s⁻¹ (Table I) vs s⁻¹ (Figs. 4, 5, 7): same
       quantity.
     * The nominal resistivity $5\times10^{-7}$ Ω m with the 5 mm wall is
       consistent with $\eta_w/d_w=10^{-4}$ Ω.
     * No run costs, wall mesh sizes or time steps are reported.
     * "Ampére's" (sic).
   * **Reference list.** 57 printed entries, merged into the
     bibliography under `isernia-2023`. Ref. 55 (Isernia et al., 49th EPS
     Conference 2023) is `isernia-2023-b`, not this source; Bondeson 1992
     (Phys. Fluids B) is `bondeson-1992-b`; the two Villone 2008 works
     (refs. 15, 51) are `villone-2008` and `villone-2008-b`. Ref. 26
     spells "Huysmans", ref. 1 "Huijsmans" (same person); refs. 12 and 16
     print La Haye as "R. J. L. Haye" (kept as printed); ref. 28
     (CASTOR3D, Nucl. Fusion 57:016032) is printed with year 2016 (NF
     vol. 57 is 2017); ref. 47 (arXiv:1609.07441) is printed with year
     2018; ref. 3 has "Massuchetts"; refs. 31–32 have unclosed year
     parentheses.
