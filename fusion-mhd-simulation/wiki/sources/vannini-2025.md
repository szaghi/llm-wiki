---
type: Source
title: "Vannini et al. (2025) — Runaway electron beam formation, vertical motion, termination and wall loads in EU-DEMO"
description: "JOREK–STARWALL study of an upward mitigated hot VDE in EU-DEMO in which a 13 MA runaway beam forms in 2D, is terminated in 3D by n ≤ 7 MHD at q95 ≈ 2.3 (12.3 to 2.8 MA in 1.1 ms, then re-avalanche), and whose 35 MJ is deposited by guiding-centre test markers on the first wall and the sacrificial upper limiters."
resource: "doi:10.1088/1741-4326/adac77"
source_kind: paper
authors: [Vannini F., Bandaru V., Bergström H., Schwarz N., Artola F.J., Hoelzl M., Pautasso G., Nardon E., Maviglia F., Richiusa M.L., Emanuelli E., JOREK Team]
year: 2025
venue: "Nucl. Fusion 65:046006"
local_file: "/home/stefano/papers/mosaic/fusion-mhd-simulation/2025_Crossref_Nuclear_Fusion_Vannini_Runaway_electron_beam_formation_vertical_motion_termination.pdf"
tags: [disruption, runaway-electrons, vde, wall, free-boundary, reduced-mhd, particles, tokamak]
timestamp: 2026-10-16T23:59:00Z
---

# Summary

The paper simulates with [JOREK](/software/jorek.md) coupled to
[STARWALL](/software/starwall.md) a pessimistic disruption of the EU-DEMO
"Single Null Variant (2021)" (start-of-flat-top equilibrium from CREATE-NL,
modified to keep $q>1$, $I_p=19.73$ MA): an upward hot
[VDE](/definitions/vertical-displacement-event.md), mitigated by neon after the
axis has moved by ≈0.7 m, in which a multi-MA
[runaway-electron](/definitions/runaway-electrons.md) (RE) beam forms and then
terminates. The workflow has four stages. (1) Axisymmetric reduced MHD with
coronal-equilibrium neon, the [RE fluid model](/methods/runaway-electron-fluid-model.md)
(tritium, Compton and Rosenbluth–Putvinski avalanche sources) and an artificial
thermal quench gives a beam of ≈13 MA; unlike the run without REs, $q_{95}$
falls, the current centroid follows the axis and the vertical
[wall force](/definitions/wall-forces.md) keeps growing. (2) 3D restarts at
$q_{95}=2.7$, 2.29 and 2.05 are all MHD-unstable; in the reference case
($q_{95}=2.29$, $n\le7$) $n=4$ grows fastest, (2,1) then dominates at
$s=0.6$, the field stochastizes from the edge inward and $I_{\mathrm{RE}}$ falls
from 12.3 to 2.8 MA in 1.12 ms; a core remnant re-avalanches to ≈10 MA.
(3) $10^6$ relativistic guiding-centre test markers (17.6 MeV each, total
≈35 MJ) are traced through the stored 3D fields onto an axisymmetric first wall.
(4) Sacrificial upper limiters (ULs) at their designed positions miss most REs,
because the scenario differs from the design basis; "moved" ULs cut the wetted
first-wall area from ≈68 m² to 6–43 m² but concentrate the load to
≈0.5–2×10⁸ J/m², about one order of magnitude above the unprotected-wall peak.
The authors present this as the first RE-load estimate for the DEMO ULs and a
reusable workflow.

# Key claims

Symbols: $Z_c=\int j_\phi Z\,dR\,dZ/I_p$ current centroid, $N_{\mathrm{RE}}$
total RE number and $W_{\mathrm{RE}}$ magnetic energy channelled to REs
(registry §11); page-local $I_p\Delta Z_c$ vertical current moment and
$\gamma_{\mathrm{RE}}$ growth rate of $I_{\mathrm{RE}}$.

1. **Without REs the vertical force saturates** (§4, Fig. 3, Eq. 2). $q_{95}$
   rises ($q_{95}\propto a^2/I_p$, $I_p$ decaying faster than $a^2$); the centroid
   stagnates near the midplane because much of the current is induced in the halo
   region outside the last closed surface; $I_p\Delta Z_c$ and
   $F_{w,z}$ saturate at $F_{w,z}\approx13$ MN, "in agreement with" Schwarz et al.
   (2023) and Miyamoto (2011). Shown.
2. **With REs the force keeps growing** (§4, Fig. 3). The beam reaches
   $I_{\mathrm{RE}}\approx13$ MA and slows the $I_p$ decay; $q_{95}$ decreases
   because the plasma shrinks faster than the current falls; the centroid follows
   the axis since "a large portion of the current remains inside the LCMFS";
   $I_p\Delta Z_c\approx43$ MA m and $F_{w,z}\approx60$ MN at 570 ms
   (figure reading), with a flattening that "could indicate" the maximum. Shown,
   2D only; $q_{95}$ reaches unphysically low values because 2D excludes MHD.
3. **$I_p-I_{\mathrm{RE}}$ is the toroidal halo current** (§4, p. 7). Stated.
4. **Impurity scan** (§4, Fig. 4). $\max I_{\mathrm{RE}}$ ≈9.8→13 MA and
   $\gamma_{\mathrm{RE}}$ ≈180→900 s⁻¹ for $n_{\mathrm{imp}}$ ≈1.3×10¹⁸→2.4×10¹⁹
   m⁻³ (four points, figure reading). Shown.
5. **MHD-unstable at every restart** (§5, Fig. 5a). $\gamma\approx1$–8×10⁴ s⁻¹,
   depending on restart time, "similarly to the findings for ITER" (Bandaru et al.
   2024b, `bandaru-2024-b`). Shown.
6. **Instability well above $q_{95}=2$** (§5, p. 8). "The RE beam can become
   unstable a long time before the value of $q_{95}=2.0$"; the 2.05 restart is set
   aside as too close to threshold, earlier restarts not followed for cost.
   Attributed.
7. **Toroidal resolution** (§5, Fig. 5b). $n=4$ is fastest, so all $n\le4$ are
   needed for correct linear dynamics; $n=6,7$ "appear to be nonlinearly driven
   when included"; two-harmonic runs ($n=0$ and $N$) misplace or overestimate the
   rates. Shown.
8. **Termination sequence** (§5, Figs. 6–9). (8,4)/(9,4) at the edge, then (2,1)
   saturating highest at $s=0.6$; the stochastic region grows inward, REs are
   lost by parallel transport, a remnant stays in the core;
   $I_{\mathrm{RE}}$ 12.3→2.8 MA in 1.12 ms; $F_{w,z}$ "slightly" reduced. Shown.
9. **Beam re-formation** (§5, p. 11, Fig. 6a). The core remnant re-avalanches to
   ≈10 MA by 457.29 ms while the dominant mode moves to $s=0.85$ and the
   closed-surface region re-grows; a new MHD burst follows, "and so on". Shown,
   qualitatively; deferred to future work.
10. **3D against 2D after termination** (Fig. 6, figure reading). In 3D $q_{95}$
    rises ≈2.2→2.55 while the 2D trace keeps falling; $I_p$ ≈15.8→14.3 MA; $F_{w,z}$
    grows more slowly than in 2D. Shown.
11. **Marker loading** (§6, Eq. 3). $W_{\mathrm{RE}}=\int J_{\mathrm{RE},\parallel}(E_\parallel-E_c^{\mathrm{eff}})\,dV\,dt\approx35$ MJ
    is shared over equal-weight markers ($N_{\mathrm{RE}}=1.24\times10^{19}$),
    each at $\mathcal E=17.6$ MeV, $\xi=-0.99$ (compiler's check:
    35 MJ/1.24×10¹⁹ = 17.6 MeV). Stated (a modelling simplification: the fluid
    model has no velocity-space information).
12. **Designed ULs miss most REs** (§6, Fig. 10). "The majority of REs do not hit
    the ULs", attributed to the scenario differing from the design basis
    (Richiusa et al. 2024). Shown / Stated.
13. **ULs shield the wall but concentrate the load** (§6, §7, Figs. 11–12).
    Affected first-wall area ≈68 m² without ULs, 29–43 m² with designed, 6–16 m²
    with moved ULs; first-wall peak ≈6–7×10⁶ J/m² without, ≈4.5–6×10⁶ with ULs;
    UL peak ≈5.5×10⁷ J/m² (designed) and 1–2×10⁸ J/m² (moved), "almost 1 order of
    magnitude higher than that onto the FW in absence of ULs". Shown.
14. **Hot spots** (§6, Fig. 10c–d) on one toroidal side of each UL block. Shown.
15. **Marker-count convergence** (§6, Fig. 13a): $10^5$, $10^6$, $10^7$ markers
    overlap. Shown.
16. **Load against toroidal resolution** (§6, Fig. 13b). $n\le3$ gives a higher
    peak (≈1.5×10⁷ against ≈6.5×10⁶ J/m² for $n\le7$) over a smaller area; $n\le5$
    and $n\le7$ are close except at the peak. Shown.
17. **Lower bound on localisation** (§7). A CAD wall would increase localisation
    further, "as shown in Ref. [32] for ITER" (Bergström et al. 2024). Attributed.
18. **Re-formed beam excluded from loads** (§7). Stated limitation.
19. **Novelty** (§6, p. 15). The UL design (8 units, ≈11.25° wide, every 45°) was
    based on TQ charged-particle loads; "the RE loads are estimated for the first
    time in this paper". Stated.
20. **Preconditioner** (§5, p. 9). Without the enhanced preconditioner of Holod et
    al. (2021) "the simulation results here presented would not have been
    possible" ([implicit time integration](/methods/implicit-time-integration.md)).
    Stated.

# Models and numerics

**Coordinates.** Right-handed $(R,Z,\phi)$, $\phi$ "oriented clockwise looking
from above the torus" (§2).

**Model** (§2, App. A, Eqs. 1–13; rendered p. 18 checked). Single-temperature
reduced MHD ($T=T_e+T_i$, $T_e=T_i$) with
$\mathbf B=R^{-1}\nabla\psi\times\mathbf e_\phi+(F_0/R)\mathbf e_\phi$,
$\mathbf v=-R\nabla u\times\mathbf e_\phi$, $u=\Phi/F_0$,
$j=\Delta^*\psi=j_{\mathrm{th}}+j_{\mathrm{RE}}$ with $j_{\mathrm{RE}}=-e\,c\,n_{\mathrm{RE}}$,
$\varpi=\nabla\cdot\nabla_{\mathrm{pol}}u$, $\rho=\rho_{\mathrm{th}}+\rho_{\mathrm{imp}}$,
$[f,g]=\mathbf e_\phi\cdot\nabla f\times\nabla g$. In registry symbols (JOREK
units, $e$ absorbed):

$$\begin{aligned}
\frac1R\partial_t\psi&=\frac{\eta}{R}\Big(j-\frac{cF_0}{BR}n_{\mathrm{RE}}\Big)+[\psi,u]-\frac{F_0}{R}\partial_\phi u-\partial_R(\eta_h\partial_Rj)-\partial_Z(\eta_h\partial_Zj),\\
R\nabla\cdot(R^2\rho\nabla_{\mathrm{pol}}\partial_tu)&=\Big[\tfrac{R^2}{2}|\nabla_{\mathrm{pol}}u|^2,\rho R^2\Big]+[\rho R^4\varpi,u]+[\psi,j]-\frac{F_0}{R}\partial_\phi j-[R^2,\rho T]+R\nabla\cdot(\nu\nabla_{\mathrm{pol}}\varpi),\\
\partial_tn_{\mathrm{RE}}&=S_{\mathrm T}+S_{\mathrm C}+S_{\mathrm{av}}+2n_{\mathrm{RE}}\partial_Zu+R[n_{\mathrm{RE}},u]+\nabla\cdot(D_{\parallel,\mathrm{RE}}\nabla_\parallel n_{\mathrm{RE}}+D_{\perp,\mathrm{RE}}\nabla_\perp n_{\mathrm{RE}}),
\end{aligned}$$

(vorticity left-hand side with one $\partial_t$; the print has two, see Recorded
as printed), plus mass and impurity continuity with anisotropic diffusion and
the $2\rho\partial_Zu+R[\rho,u]$ advection form, and a pressure equation with
anisotropic conduction $\nabla\cdot(\chi_\parallel\nabla_\parallel T+\chi_\perp\nabla_\perp T)$,
Ohmic heating $(\Gamma-1)\eta\,(j-cF_0n_{\mathrm{RE}}/(BR))^2/R^2$,
impurity and background ionization energy, deuterium continuum and impurity
radiation, and the impurity coefficients (Eq. 13)
$\alpha_{\mathrm{imp}}=\frac{m_i}{2m_{\mathrm{imp}}}(\langle z\rangle+1)-1$,
$\alpha_{\mathrm{imp},bis}=\alpha_{\mathrm{imp}}+T\,d\alpha_{\mathrm{imp}}/dT$,
$\beta_{\mathrm{imp}}=\frac{m_i}{m_{\mathrm{imp}}}\langle z\rangle-1$
([coronal-equilibrium model](/methods/coronal-equilibrium-impurity-model.md)).
The flux equation carries $+\eta j$ and $-F_0\partial_\phi u/R$, the diffusive
side of the open sign contradiction on [reduced MHD](/methods/reduced-mhd.md);
the vorticity viscous term is $R\nabla\cdot(\nu\nabla_{\mathrm{pol}}\varpi)$.
The RE equation has **no advection at $c$**: parallel transport is pure parallel
diffusion "to reduce the computational cost", and a perpendicular RE diffusion
is added; this differs from the model form printed by
[Bandaru et al. (2024)](/sources/bandaru-2024.md) (advection fraction, no
$D_{\perp,\mathrm{RE}}$, Hesslow avalanche), although both cite the same JOREK
model.

**Sources and closures** (§4, Table 2). Seed $S_{\mathrm T}+S_{\mathrm C}$
switched on after the ATQ, no Dreicer or hot-tail source; avalanche
Rosenbluth–Putvinski with partial-ionization corrections (Hesslow et al. 2018).
Coronal-equilibrium neon from a uniform source. $D=1.04$ m²/s (isotropic, plasma
and impurities); $D_{\parallel,\mathrm{RE}}=1.54\times10^9$ m²/s,
$D_{\perp,\mathrm{RE}}=1.54\times10^{-2}$ m²/s; Spitzer–Härm $\chi_\parallel$
capped at its 876 eV value; $\chi_\perp$ profile with 0.5 m²/s in the core;
Spitzer $\eta$ floored at its 1.26 keV value; $\nu_{\mathrm{core}}=2.47\times10^{-3}$
kg m⁻¹ s⁻¹; $\eta_h$ value not given.

**Artificial TQ.** ≈4 ms, after the axis has moved ≈0.7 m and neon has been
ramped uniformly: raised diffusivities, Ohmic heating off, large hyper-resistivity
to flatten $j$ and mimic the current spike, $T_e\approx10$ eV at the end; then
all parameters restored. The VDE is triggered by a current perturbation in the
in-vessel coils.

**Wall and boundary** ([resistive-wall coupling](/methods/resistive-wall-coupling.md)).
Dirichlet conditions on all variables except $\psi$ and $j$, which come from the
fully implicit JOREK–STARWALL coupling. STARWALL holds CS, PF and in-vessel
vertical-stability coils, inboard and outboard thin vacuum-vessel layers
($\eta_w=0.76$ µΩ m, $d_w=3$ cm; triangles inboard, toroidal filaments
outboard) and the first wall. The JOREK boundary encloses the first wall and
hugs it near the ULs.

**Discretization.** Bézier finite elements on a polar grid (node counts not
given) × toroidal Fourier series; 2D runs $n=0$; 3D runs $n\le N$ with
$N\in\{3,5,7\}$ plus two-harmonic runs $\{0,N\}$. Equilibrium from JOREK's
Grad–Shafranov solver with the CREATE-NL $p(\psi_N)$ and a core-modified $FF'$
($q$ unchanged for $\psi_N>0.8$). Fully implicit time stepping; time step,
resolution and cost not given (Marconi-Fusion).

**Markers** ([particle pushers](/methods/particle-pushers.md)). JOREK particle
module, relativistic guiding-centre equations (Tao et al. 2007), RK4, test
particles without back-reaction in the stored field history; seeded at
452.25 ms from $n_{\mathrm{RE}}$, stopped at 453.59 ms or at wall contact on a
triangulated axisymmetric first wall. UL model: units protruding 70 mm; variants
4×45°, 8×22.5°, 8×11.25°, each at designed and moved poloidal positions.

# Tests and results

| Quantity | CREATE-NL | JOREK equilibrium |
|---|---|---|
| $I_p$ [MA] | 18.27 | 19.73 |
| $l_i$; $\beta_p$ | 1.04; 1.02 | 1.08; 1.01 |
| axis $(R,Z)$ [m] | (9.47, 0.06) | (9.37, 0.086) |
| geometric $R$; $a$ [m] | 8.94; 2.88 | 8.85; 2.84 |
| $B_\phi$ [T]; $q_{95}$ | 5.7; 3.51 | 5.78; 3.54 |
| elongation; triangularity | 1.77; 0.44 | 1.8; 0.435 |

* Profiles: $n_e(0)\approx2.35\times10^{20}$ m⁻³, $T_e(0)\approx25$ keV.
* 2D without REs ($n_{\mathrm{imp}}=2.4\times10^{19}$ m⁻³): ATQ at ≈400 ms; $I_p$
  ≈19→3 MA by 530 ms; $q_{95}>8$; $F_{w,z}$ peak ≈13 MN.
* 2D with REs: $q_{95}=2.0$ at ≈459 ms; $F_{w,z}\approx60$ MN at 570 ms, rising.
* Growth rates at $q_{95}=2.29$ ($N=3,5,7$ agree for $n\le5$): ≈2.2, 2.9, 3.8,
  3.9, 3.7×10⁴ s⁻¹ for $n=1$–5; $n=6$, 7 ≈8.3, 7.6×10⁴ s⁻¹ with $N=7$;
  two-harmonic runs peak at $n=4$ (≈4.3×10⁴ s⁻¹).
* Termination window ≈452.3–453.6 ms; $n\ge1$ energies jump from ≈10⁻¹¹ to
  ≈10⁻² (normalized) near 452.5 ms; re-avalanche to ≈10 MA at ≈457.3 ms, decay to
  ≈7.5 MA at ≈458–460 ms.
* Lost markers hit the upper wall at geometric $\theta\approx65°$–110° about the
  axis; smallest wetted first-wall area ≈6 m² with moved ULs, 8×22.5°.

# Notation map

| Vannini et al. (2025) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $(R,Z,\phi)$, $\hat{\mathbf e}_{R,Z,\phi}$ | $(R,Z,\phi)$, $\mathbf e_{R,Z,\phi}$ | $\phi$ clockwise from above |
| $\psi$, $\psi_N$ | $\psi$, $\psi_N$ | per radian, $B_R=\partial_Z\psi/R$ |
| $\rho_N=\sqrt{\psi_N}$ | $s$ | **collision:** registry $\rho$ is mass density |
| $F_0$, $u=\Phi/F_0$, $j=\Delta^*\psi$ | $F_0$, $u$, $j$ | |
| $j_{\mathrm{th}}$, $j_{\mathrm{RE}}$, $j_{RE,\parallel}$ | parts of $j_\phi$; $\mathbf J_{\mathrm{RE}}$, $J_{\mathrm{RE},\parallel}$ | |
| $\omega=\Delta_{pol}u$ | $\varpi$ | **collision:** registry $\omega$ is a frequency |
| $\rho$, $\rho_{\mathrm{th}}$, $\rho_{\mathrm{imp}}$ | $\rho$, $\rho_{\mathrm{imp}}$ | |
| $T$ | $T$ (total $T_e+T_i$, stated) | |
| $\eta$, $\eta_{Ohm}$, $\eta_{num}$ | $\eta$, $\eta_h$ | |
| $\mu$ | $\nu$ (dynamic) | **collision:** registry $\mu$ is the magnetic moment |
| $\gamma$ (Eq. 9) | $\Gamma$ | **collision:** the paper also uses $\gamma$ for growth rates (Fig. 5) |
| $\gamma$ (Fig. 5), $\gamma_{\mathrm{RE}}$ | $\gamma$; page-local | |
| $D_{\parallel}$, $D_\perp$, $D_{\parallel,imp}$, $D_{\perp,imp}$ | $D_\parallel$, $D_\perp$ (subscripted) | |
| $D_{\parallel,RE}$, $D_{\perp,RE}$ | $D_{\parallel,\mathrm{RE}}$, $D_{\perp,\mathrm{RE}}$ | |
| $\chi_\parallel$, $\chi_\perp$ | $\chi_\parallel$, $\chi_\perp$ | |
| $S_{RE}$, $S_{avalanche}$ | $S_{\mathrm T}+S_{\mathrm C}$, $S_{\mathrm{av}}$ | |
| $S_\rho$, $S_{imp}$, $S_{bg}$ | $S_\rho$ (subscripted) | |
| $E_{ion}$, $L_{rad}$, $\langle Z_{imp}\rangle$ | $\varepsilon_{\mathrm{ion}}$, $L_{\mathrm{rad}}$, $\langle z\rangle$ | |
| $\alpha_{imp}$, $\alpha_{imp,bis}$, $\beta_{imp}$ | page-local | |
| $F_z$ | $F_{w,z}$ | |
| $Z_{\mathrm{Curr.}}$, $I_p\Delta Z_{\mathrm{Curr.}}$ | $Z_c$ (§11), $I_p\Delta Z_c$ (page-local) | |
| $E_{mag}$, $E_{kin}$ | $W_{\mathrm{mag}}^{(n)}$, $W_{\mathrm{kin}}^{(n)}$ | |
| $E_\parallel$, $E_c^{eff}$ | $E_\parallel$, $E_c^{\mathrm{eff}}$ | |
| $\mathcal E$, $\xi$ | $\mathcal E$, $\xi$ | pitch, §10 |
| $W_{tot}$, $N_{RE}$ | $W_{\mathrm{RE}}$, $N_{\mathrm{RE}}$ (§11) | Eq. 3 |
| $N$ (§5) | $n_{\max}$ ($N_{\mathrm{tor}}=N+1$) | **collision** with $N$ = number of UL units (§6) |
| $\beta_{pol}$, $k$, $\delta$ | $\beta_p$; words (elongation, triangularity) | $\delta$ collides with the perturbation prefix |
| $\eta_w$, $d_w$ | $\eta_w$, $d_w$ | |

JOREK normalized units ($\mu_0=1$, reference mass density) in Eqs. 4–13;
normalization factors not printed; Table 2 is in SI.

# Pages created or updated

Chunk 3 (2026-10-16) created or updated the pages below. This source is cited on:

* [Coronal-equilibrium impurity model](/methods/coronal-equilibrium-impurity-model.md)
* [Disruption: phases, current quench and current spike](/definitions/disruption.md)
* [Electromagnetic wall forces (vertical and sideways)](/definitions/wall-forces.md)
* [Free-boundary and resistive-wall coupling](/methods/resistive-wall-coupling.md)
* [Halo current](/definitions/halo-current.md)
* [Implicit time integration and preconditioned Krylov solvers for nonlinear MHD](/methods/implicit-time-integration.md)
* [JOREK](/software/jorek.md)
* [Particle pushers: Boris, slow-manifold Boris, guiding-centre and gyrokinetic](/methods/particle-pushers.md)
* [Reduced MHD for tokamaks](/methods/reduced-mhd.md)
* [Runaway current reconstitution after an MHD flush](/results/runaway-reconstitution-after-mhd-flush.md)
* [Runaway electrons and their generation mechanisms](/definitions/runaway-electrons.md)
* [Runaway-electron fluid model coupled to MHD](/methods/runaway-electron-fluid-model.md)
* [Runaway-electron wall loads and sacrificial limiters](/definitions/runaway-electron-wall-loads.md)
* [STARWALL](/software/starwall.md)
* [Thermal quench](/definitions/thermal-quench.md)
* [Vertical displacement event (hot and cold VDE)](/definitions/vertical-displacement-event.md)
* [Vertical-force mitigation by massive material injection](/results/vertical-force-mitigation.md)

# Citations

1. `/home/stefano/papers/mosaic/fusion-mhd-simulation/2025_Crossref_Nuclear_Fusion_Vannini_Runaway_electron_beam_formation_vertical_motion_termination.pdf`.
   * **Version.** arXiv:2407.03940v1, 4 Jul 2024, LaTeX preprint, 23 pp. (17 of
     text, 2-page appendix, 4 of references); not the published version, so
     changes made in review cannot be checked. Section, figure and page numbers are
     the preprint's.
   * **Identity.** doi:10.1088/1741-4326/adac77, checked on Crossref: Nucl. Fusion
     65(4), article 046006, online 2025-03-04; same title and 11 named authors in
     the same order (Crossref spells "Bergström", the PDF "Bergstroem"). The line
     "Nuclear Fusion 61, 065001 (2021)" under the page-1 affiliations is the tail
     of the JOREK-team footnote (Hoelzl et al. 2021), not this paper's venue.
   * **How read.** Full text; Appendix A equations read on rendered p. 18; curve
     values are approximate figure readings. Grid, time step and cost are not
     given in the paper.
   * **Recorded as printed.**
     * §3, p. 5: "as indicated in table 2" should be Table 1 (Table 2 is the
       transport table).
     * §4, p. 7: "second plot from the top of fig. 3 (b)" for $I_{\mathrm{RE}}$,
       which is in Fig. 3(a).
     * §4, p. 7: "given the not unrealistic drop of $q_{95}$ to extremely low
       values" — the logic requires "unrealistic".
     * Eq. 5 left-hand side printed with two time derivatives,
       $R\nabla\cdot(R^2\rho\,\partial_t\nabla_{pol}\partial_tu)$; the JOREK form
       has one. Treated as a typo.
     * Fig. 6(b) axis "$F_z$ [MA]" should be MN.
     * $\gamma$ is both the adiabatic index (Eq. 9) and the growth rate (Fig. 5);
       $N$ is both the highest toroidal mode number and the number of UL units.
     * $j_{\mathrm{RE}}=-ecn_{\mathrm{RE}}$ (§2) against the $+cF_0n_{\mathrm{RE}}/(BR)$
       subtracted from $j$ in Eq. 4; the signs are not reconciled in the text (same
       printed form as Bandaru et al. 2024).
     * Table 2 gives one isotropic $D$ while Eqs. 8 and 10 write separate parallel
       and perpendicular diffusivities; Table 2 is titled "before and after the
       ATQ" but the ATQ values and $\eta_{num}$ are given nowhere.
     * Fig. 11 plots the area receiving at least a given load; the caption says
       only "energy per surface unit that arrives onto a certain area".
     * "Almost 1 order of magnitude" (Conclusion): ≈5.5×10⁷ against 6.5×10⁶ J/m²
       is ≈8.5× for designed ULs, but moved ULs reach 1–2×10⁸, ≈15–30×
       (compiler's arithmetic from figure readings).
     * UL variants 4×45° and 8×22.5° both cover 180°, 8×11.25° covers 90°, so unit
       count and coverage are confounded.
     * The time limits of the Eq. 3 integral are not stated.
   * **Reference list.** 37 printed entries; Hesslow et al. 2018 (PPCF 60:074010)
     is printed twice ([18] = [34]) and merged into one entry, `hesslow-2018`, so
     36 bibliography entries, merged under `vannini-2025`. [19] (printed "Submitted to Physics of
     Plasmas") is `bandaru-2024-d`, the submitted form of the ingested
     [Bandaru et al. (2024)](/sources/bandaru-2024.md) (no `bandaru-2024`
     entry remains; pre-publication citations are kept as distinct entries (human ruling 2026-10-16)), [13] the ingested
     [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), [29] is `bandaru-2024-b`
     (no volume printed), [28] (arXiv 2406.09703) `bandaru-2024-c`, [30]
     `holod-2021`, [32] (printed "PPCF, manuscript under review")
     `bergstrom-2024-b` (published `bergstrom-2024`). The TSDW 2023 poster [33] is kept as
     `bergstroem-2023-b`, distinct from `bergstroem-2023` (different printed
     titles at the same workshop; possibly the same contribution).
     `albanese-2015-b` (CREATE-NL+) is distinct from `albanese-2015`. [1] and [2]
     have garbled author strings; [10], [11] are printed as Scopus records; [19],
     [28], [32] have no year.
