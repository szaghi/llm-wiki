---
type: Source
title: "Artola et al. (2022) — Non-axisymmetric MHD simulations of the current quench phase of ITER mitigated disruptions"
description: "3D JOREK–STARWALL simulations of ITER mitigated-disruption current quenches at realistic Lundquist number show q95 staying at 3–4, horizontal wall force below 1 MN and a vertical force of 11–14 MN that peaks on the vessel time after the plasma current has vanished, from wall-current diffusion in the up-down asymmetric vessel, so that the force does not rotate."
resource: "doi:10.1088/1741-4326/ac55ba"
source_kind: paper
authors: [Artola F.J., Loarte A., Hoelzl M., Lehnen M., Schwarz N., JOREK Team]
year: 2022
venue: "Nucl. Fusion 62:056023"
local_file: "/home/stefano/papers/mosaic/fusion-mhd-simulation/2022_Crossref_Nuclear_Fusion_Artola_Non-axisymmetric_MHD_simulations_of_the_current_quench_phase.pdf"
tags: [disruption, vde, wall, free-boundary, reduced-mhd, tearing, tokamak]
timestamp: 2026-10-16T20:00:00Z
---

# Summary

The paper presents what it calls the first complete 3D nonlinear MHD
simulations of the current-quench (CQ) phase of ITER mitigated
disruptions at realistic Lundquist numbers (Spitzer resistivity and
Spitzer–Härm parallel conduction). It uses [JOREK](/software/jorek.md)
[reduced](/methods/reduced-mhd.md) visco-resistive MHD coupled implicitly
to [STARWALL](/software/starwall.md), with a 3D thin inner vessel (75 000
triangles), a toroidal-filament outer vessel, the OTS and DIR passive
structures, and toroidal harmonics $n=0,\dots,10$. Two post-TQ states of
a 15 MA / 5.3 T L-mode (density ×20, temperature ×1/20, an artificial
axisymmetric TQ by raised $\kappa_\perp$; core $T_e\approx15$–30 eV) are
followed through the CQ and on to about 1.5 s, beyond the vessel time
$\tau_w\approx500$ ms. Several tearing modes grow at 2–3 ms⁻¹, saturate
and ergodize the field. $q_{95}$ stays at 3–4 because the CQ
($\approx46$ ms) is much faster than $\tau_w$, so no 1/1 mode appears and
the horizontal wall force stays at noise level (<1 MN). Case 1 drifts
upward, case 2 downward (attributed to its larger drop of $l_i$). In both
the vertical force peaks at 11–14 MN some 300–400 ms after $I_p$ has
vanished, caused by diffusion of the net toroidal wall current in the
up-down asymmetric vessel and its interaction with the poloidal-field-coil
field, independent of the drift direction; with no plasma current left
the force cannot rotate toroidally. Halo fractions (8.7%, 16.6%), toroidal
peaking factors (1.2, 1.7) and their products (0.09, 0.17) lie within or
near the ITER category-I range. See
[wall forces](/definitions/wall-forces.md),
[halo current](/definitions/halo-current.md) and
[vertical-force mitigation](/results/vertical-force-mitigation.md).

# Key claims

1. **Priority** (Abstract, §5). "We present for the first time such
   simulations for ITER mitigated disruptions at realistic Lundquist
   numbers". Stated.
2. **$q_{95}$ stays at 3–4** during the CQ in both cases (§4.1, §4.2;
   Figs. 4b, 6b); the abstract says "remains above 2". Shown.
3. **Horizontal force at noise level** (§4.1–4.3, §5; Figs. 4c, 6c, 9).
   No $m/n=1/1$ mode; $F_{w,h}<1$ MN, against JET-based extrapolations of
   about 40 MN; it "completely decays at the moment the plasma current
   vanishes, confirming that the found horizontal force is noise arising
   from a finite employed resolution". Shown.
4. **Why $q_{95}$ stays high** (§1, §5). Fast CQ ($\sim50$ ms) against
   the wall-current decay time ($\sim500$ ms) and induced toroidal halo
   currents; $q_a\propto1/I_p$ rises when $I_p$ decays faster than the
   plasma moves vertically. Shown for the two cases; mechanism Stated.
5. **Vertical force after the CQ** (§1, §4.3, Fig. 9). The force arises
   on the vessel L/R time, after $I_p$ has decayed; since it requires the
   field to penetrate the wall, $\mathbf F_w\approx0$ on times
   $\ll\tau_w$ (from the Maxwell-stress form, Eq. 1). Shown (simulation)
   and Derived. "3D simulations are typically not continued after the
   plasma current vanishes", an effect "largely ignored in the
   literature"; time traces resemble Albanese et al. (2015) and the effect
   was seen by Yanovskiy et al. (2021). Stated.
6. **Magnitude** (§4.3, §5, Fig. 9). Maximum $F_{w,z}$ 11–14 MN (abstract
   "13 MN"; Fig. 9 reads about 11 MN for case 1 and 13.5 MN for case 2),
   "a factor 6 smaller than the largest estimates" of 80 MN. Shown.
7. **Independence of the drift direction** (§4.3, Fig. 10). Maximum
   $F_{w,z}$ and the inner-vessel current distribution at its time are
   "roughly identical" for upward and downward cases; the force "arises
   due to the diffusion of the net toroidal wall current along the wall
   contour and its interaction with the magnetic field produced by the
   poloidal field coils". Shown (comparison), Stated (mechanism).
8. **Design implication** (§4.3, §5). The force "would in principle not
   arise" for an up-down symmetric plasma in an up-down symmetric wall
   (suggested for DEMO). Stated; not simulated.
9. **Non-rotating forces** (§1, §5). For CQ time much shorter than
   $\tau_w$ the forces are "static in the toroidal direction (i.e.
   non-rotating)", so resonance with vessel natural frequencies (Schioler
   et al. 2011) is "not relevant"; "To our knowledge this fact has not
   been identified in the literature so far". Stated (argued from the
   timing; the force phase is not plotted).
10. **CQ times** (§4.1, §4.2). $\tau_{\mathrm{CQ}}\equiv
    (t_{20\%}-t_{80\%})/0.6$ gives 47 ms (case 1) and 45.5 ms (case 2),
    "close to the envisaged minimum CQ time for mitigated disruptions (50
    ms)". Shown.
11. **Case 1 MHD** (§4.1, Figs. 3–5). Several tearing modes with "similar
    growth rates (∼2−3 ms⁻¹)", low $n$ dominant; saturation from 10 ms,
    maximum at 13 ms ($I_p$ 11–12 MA); field almost completely ergodic at
    13 ms, core surfaces re-formed by 23 ms. Shown.
12. **Case 2 MHD** (§4.2, Fig. 6). Stronger 2/1 dominance, saturation at
    $I_p\approx14$ MA ($t=7$ ms), a drop of $l_i(3)$ by 0.26 in 3.3 ms,
    then a rise of halo current and an $I_p$ spike. Shown.
13. **Flattening beyond the LCFS** (§4.2, §5, Figs. 7–8). MHD flattening
    of current and temperature "takes place also beyond the LCFS"; SOL
    currents "may be playing a important role" in the spike. Shown
    (flattening), Stated (spike interpretation).
14. **Drift direction** (§4.2). The downward drift of case 2 is
    attributed to its larger $l_i$ drop, consistent with Lukash et al.
    (2005) and the "vertical dragging effect" of Nakamura et al. (1996).
    Shown (direction), Stated (attribution).
15. **Halo metrics** (§4.1, §4.2, §4.4). Case 1: maximum TPF 1.2 (at halo
    fraction 2%), maximum product 0.09, maximum halo fraction 8.7%,
    maximum toroidal halo current 4.1 MA. Case 2: TPF 1.7 (at 5.7%),
    product 0.17, "slightly above the level for category I" (0.15),
    halo fraction 16.6%, toroidal halo current 8.4 MA. Experimental
    maximum of the product: 0.75. Shown.
16. **SOL temperature** (§4.4, Fig. 8). The SOL reaches 10–15 eV from the
    1 eV boundary value, "consistent with experimental temperature
    measurements"; parallel conduction time $\sim70$ ms for 100 m
    connection length at 10 eV and $10^{20}$ m⁻³. Shown; estimate Derived.
17. **Viscosity insensitivity** (§4.4, Table 1). Raising the parallel
    viscosity ×10 (at 14.3 ms, case 1; 19.8 ms, case 2) for numerical
    stability changed neither $q_{95}$, magnetic energies nor forces in
    re-run fragments. Shown (not plotted).
18. **SOL model limitation** (§4.4). Very cold halos could re-induce
    current in the core, slowing the $I_p$ decay relative to the vertical
    motion and lowering $q_{95}$; more complete SOL models (Ohmic heating,
    impurities, radiation, neutrals, sheath) are needed. Stated.
19. **Blanket modules omitted** (§2). Expected not to change the maximum
    forces because the insulated modules cannot carry toroidal current.
    Stated.
20. **Cost** (§5). "Of the order of 5 million core.hours per simulation".
    Stated.

# Models and numerics

* **Model** (§2, Eqs. 2–5, single temperature, SI as printed):
  $$\begin{aligned}
  \partial_t\mathbf A&=\mathbf v\times\mathbf B-\eta\mathbf J-\nabla\Phi,\\
  \rho\,\partial_t\mathbf v&=-\rho\mathbf v\cdot\nabla\mathbf v-\nabla p+\mathbf J\times\mathbf B+\nabla\cdot\mathsf\Pi,\\
  \partial_t\rho&=-\nabla\cdot(\rho\mathbf v)+\nabla\cdot(\mathsf D\nabla\rho),\\
  \partial_tp&=-\mathbf v\cdot\nabla p-\Gamma p\nabla\cdot\mathbf v+\nabla\cdot(\mathsf K\nabla T),
  \end{aligned}$$
  with $\mathsf\Pi$ the viscous stress tensor (the paper's $\boldsymbol\tau$, sign as printed),
  $T=T_e+T_i$, $\mathsf K$ strongly anisotropic and $\mathsf D$ "normally
  isotropic". No Ohmic heating and no impurity radiation: the two are
  assumed to cancel (all magnetic energy radiated, justified by the >90%
  radiation efficiency required in ITER DT). No density or temperature
  sources.
* **Reduced ansatz** (Eqs. 6–7):
  $$\mathbf B=\nabla\psi\times\nabla\phi+F_0\nabla\phi,\qquad \mathbf v=-R^2\nabla u\times\nabla\phi+v_\parallel\mathbf b,\quad u=\Phi/F_0,$$
  with $F_0$ constant; poloidal currents evolve but their contribution to
  the toroidal field is neglected. The validity for wall forces rests on
  the axisymmetric and 3D VDE benchmarks with NIMROD and M3D-C1 (Krebs et
  al. 2020; [Artola et al. (2021)](/sources/artola-2021.md), see the
  [NSTX VDE benchmarks](/benchmarks/nstx-vde-benchmarks.md)).
* **Wall force** (Eq. 1, after Pustovitov et al. 2017), in corrected form:
  $$\mathbf F_w=\int_{\mathrm{wall}}\mathbf J\times\mathbf B\,dV=\oint_{\mathrm{wall}^+}\mathbf f\,dS,\qquad \mathbf f=\frac{1}{\mu_0}\Big[(\mathbf B\cdot\mathbf n)\mathbf B-\tfrac12B^2\mathbf n\Big],$$
  $F_{w,h}=\sqrt{F_{w,x}^2+F_{w,y}^2}$. The printed placement of $1/\mu_0$
  differs (Recorded as printed).
* **Halo diagnostics.** Halo fraction $I_{\mathrm{halo}}/I_p$ (poloidal
  halo current over the pre-disruptive plasma current); TPF (Eq. 8):
  $$\mathrm{TPF}=\max_\phi\Big(\tfrac12\oint_\phi|\mathbf J\cdot\mathbf n|\,R\,dl\Big)\Big/\big(I_{\mathrm{halo}}/2\pi\big),$$
  with $dl$ the poloidal length element of the wall contour at fixed
  $\phi$. CQ time $\tau_{\mathrm{CQ}}=(t_{20\%}-t_{80\%})/0.6$ (Eidietis et
  al. 2015).
* **Coefficients** (Table 1; $T_{e0}=300$ eV; constant except $\eta$ and
  $\kappa_\parallel$): $D=2$ m² s⁻¹; $\kappa_\perp=2\times10^{21}$
  (m s)⁻¹; $\kappa_\parallel=\kappa_0(T_e/T_{e0})^{5/2}$ with
  $\kappa_0=1.77\times10^{28}$ (m s)⁻¹; $\eta=\eta_0(T_e/T_{e0})^{-3/2}$,
  $\eta_0=6.74\times10^{-7}$ Ω m; dynamic viscosities (parallel,
  perpendicular) $=(1630, 4.24)\times10^{-7}$ kg m⁻¹ s⁻¹, parallel raised
  ×10 at some times. The (m s)⁻¹ units are density-weighted diffusivities
  ($\kappa_\perp/n_e=2$ m² s⁻¹ at $10^{21}$ m⁻³, compiler's reading).
* **Initial state.** The pre-TQ equilibrium rescaled with $n\times20$,
  $T\times1/20$ (same pressure, same Grad–Shafranov solution); artificial
  axisymmetric TQ by raised $\kappa_\perp$ for 5 ms (case 1) or 2.1 ms
  (case 2), giving core $T_e\approx15$ eV / 30 eV, $n_e\approx10^{21}$
  m⁻³, $q_0\approx1.3$, edge $q\approx4$. The $q$ profile is deliberately
  not flattened inside $q=2$. The temperatures approximate a post-TQ
  neon-[SPI](/definitions/shattered-pellet-injection.md) state. The 3D run
  starts with $n\in[0,10]$ seeded at noise level.
* **Boundary conditions.** Dirichlet at the plasma–wall interface:
  $n_e=10^{20}$ m⁻³, $T_e=1$ eV, $\mathbf v\cdot\mathbf n=0$,
  $v_\parallel=0$; equivalent to $\Phi=0$, so heat leaves only by
  conduction. No sheath condition.
* **Discretization.** Polar grid of 100×200 third-order
  [Bézier](/methods/bezier-finite-elements.md) quadrilaterals, boundary
  roughly following the ITER first wall (no divertor details); 11
  toroidal harmonics; fully implicit
  ([implicit time integration](/methods/implicit-time-integration.md)).
  Time step and solver settings not given.
* **Wall model** ([resistive-wall coupling](/methods/resistive-wall-coupling.md)).
  Thin wall, implicit JOREK–STARWALL; inner vessel layer with 3D currents
  (75 000 linear triangles); outer layer as toroidal filaments
  (axisymmetric currents, justified because the CQ is much shorter than
  the inner-layer penetration time); OTS and DIR as filaments for
  vertical stability; $\eta_w=0.8$ µΩ m, $d_w=6$ cm (unit as corrected);
  axisymmetric DINA benchmark of the model cited; vessel L/R time about
  500 ms. Blanket modules and port asymmetries omitted.
* **Resources.** About 5 M core-hours per run (ITER cluster,
  Marconi-Fusion, Google Cloud); simulated time to about 1.6 s.

# Tests and results

No benchmark; two application cases.

| Quantity | Case 1 | Case 2 |
|---|---|---|
| Axisymmetric pre-phase | 5 ms | 2.1 ms |
| Dominant modes | several tearing modes, low $n$ | stronger 2/1 |
| Growth rate | 2–3 ms⁻¹ | similar |
| Saturation | from 10 ms, max 13 ms, $I_p$ 11–12 MA | 7 ms, $I_p\approx14$ MA |
| $\tau_{\mathrm{CQ}}$ | 47 ms | 45.5 ms |
| Vertical drift | upward | downward |
| $q_{95}$ during CQ | 3–4 | 3–4 |
| Drop of $l_i(3)$ | slow | 0.26 in 3.3 ms |
| Max TPF (halo fraction then) | 1.2 (2%) | 1.7 (5.7%) |
| Max halo fraction × TPF | 0.09 | 0.17 |
| Max halo fraction | 8.7% | 16.6% |
| Max toroidal halo current | 4.1 MA | 8.4 MA |
| Max $F_{w,h}$ | <1 MN (noise) | <1 MN (noise) |
| Max $F_{w,z}$ (Fig. 9, read) | ≈11 MN at ≈400 ms | ≈13.5 MN at ≈330 ms |

* Poincaré plots of case 1 (Fig. 5) at 5, 13, 18, 23, 28 ms: near-complete
  stochasticity at 13 ms, core surfaces at 23 ms; runaway-electron
  confinement in these fields is studied elsewhere (Särkimäki et al.).
* During the CQ $F_{w,z}$ of case 1 is about −1 to −1.5 MN; that of case 2
  is still rising (≈5 MN) at 60 ms (read).
* Comparisons: $F_{w,h}<1$ MN against ≈40 MN (JET extrapolations), 30 MN
  and 4 MN (Strauss 2018, for CQ time much longer or shorter than
  $\tau_w$), and an eddy-current-only kink estimate an order of magnitude
  below 40 MN (Pustovitov et al. 2021); $F_{w,z}$ 11–14 MN against ≈80 MN
  (Sugihara et al. 2007, Clauser et al. 2019).
* Relation to the bundle: [Hoelzl et al. (2021)](/sources/hoelzl-2021.md)
  (§6.3) predict halo fractions of 10–20% for 50–150 ms CQs, agreeing
  with 8.7–16.6% here, and a TPF below about 1.15 in 3D ITER 15 MA fast-CQ runs, against 1.7
  here in a different scenario; it also states that CQs below 50 ms are
  not allowed in ITER, while these cases run at 45.5–47 ms.
  [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) (§3.3) summarize this
  paper's result.

# Notation map

| Artola et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf A$, $\mathbf B$, $\mathbf J$, $\mathbf v$, $\Phi$, $\eta$ | same | SI as printed |
| $\mathbf v_\parallel$ (vector, Eq. 7) | $v_\parallel\mathbf b$ | |
| $\rho$ ("ion density") | $\rho$ | mass density |
| $p$, $T$, $T_e$, $T_{e0}$, $n_e$ | same | $T=T_e+T_i$ |
| $\underline{\boldsymbol\tau}$ | $\mathsf\Pi$ (viscous part) | enters as $+\nabla\cdot\underline{\boldsymbol\tau}$ |
| $\mu_\parallel$, $\mu_\perp$ | $\nu$ (dynamic, parallel and perpendicular) | **collision:** registry $\mu$ is the magnetic moment |
| $\underline{\boldsymbol\kappa}$, $\kappa_\parallel$, $\kappa_\perp$, $\kappa_0$ | $\mathsf K$, $\kappa_\parallel$, $\kappa_\perp$ | density-weighted units |
| $\underline{\mathbf D}$, $D$ | $\mathsf D$, $D_\perp=D_\parallel$ | |
| $\gamma$ | $\Gamma$ | **collision:** registry $\gamma$ is the growth rate |
| $\psi$, $\psi_N$, $F_0$ | same | per radian |
| $\Phi$ in $\mathbf v_\perp=-\frac{R^2}{F_0}\nabla\Phi\times\nabla\phi$ | $u=\Phi/F_0$ | |
| $q_a$, $q_{95}$, $l_i(3)$, $I_p$ | same | $l_i$ definition (3) not printed |
| $I_{halo,\theta}$, $I_{halo,\phi}$, HF | $I_{\mathrm{halo}}$, words (toroidal halo current), $I_{\mathrm{halo}}/I_p$ | |
| TPF | TPF | |
| $\mathbf F$, $F_h$, $F_z$ | $\mathbf F_w$, $F_{w,h}$, $F_{w,z}$ | |
| $\tau_w$, $\eta_w$, $d_w$ | same | |
| $\tau_{CQ}$ | $\tau_{\mathrm{CQ}}$ | defined as $(t_{20\%}-t_{80\%})/0.6$ |
| $W_{mag}$ | $W_{\mathrm{mag}}^{(n)}$ | |
| $Z_{axis}$ | words (vertical position of the axis) | |

# Pages created or updated

Chunk 2 (2026-10-16) created or updated the pages below; chunk 3 extended some. This source is cited on:

* [Bézier–Hermite finite elements with toroidal Fourier harmonics](/methods/bezier-finite-elements.md)
* [Disruption: phases, current quench and current spike](/definitions/disruption.md)
* [Electromagnetic wall forces (vertical and sideways)](/definitions/wall-forces.md)
* [Free-boundary and resistive-wall coupling](/methods/resistive-wall-coupling.md)
* [Halo current](/definitions/halo-current.md)
* [JOREK](/software/jorek.md)
* [NSTX VDE benchmarks of JOREK, M3D-C1 and NIMROD (axisymmetric and 3D)](/benchmarks/nstx-vde-benchmarks.md)
* [Reduced MHD for tokamaks](/methods/reduced-mhd.md)
* [Resistive tearing mode](/definitions/tearing-mode.md)
* [Runaway electrons and their generation mechanisms](/definitions/runaway-electrons.md)
* [Sheath (Bohm) boundary conditions](/methods/sheath-boundary-conditions.md)
* [STARWALL](/software/starwall.md)
* [Vertical displacement event (hot and cold VDE)](/definitions/vertical-displacement-event.md)
* [Vertical-force mitigation by massive material injection](/results/vertical-force-mitigation.md)

# Citations

1. `/home/stefano/papers/mosaic/fusion-mhd-simulation/2022_Crossref_Nuclear_Fusion_Artola_Non-axisymmetric_MHD_simulations_of_the_current_quench_phase.pdf`.
   * **Version.** arXiv:2112.05600v1 [physics.plasm-ph], 10 December 2021,
     titled "Complete 3D MHD simulations of the current quench phase of
     ITER mitigated disruptions"; 11 pages, 10 figures, 1 table, 31
     printed references. Not the version of record despite the filename.
   * **Identity.** doi:10.1088/1741-4326/ac55ba, checked on Crossref by
     title: Nucl. Fusion 62(5), article 056023, issued 2022-03-28 (CC BY
     4.0), authors Artola, Loarte, Hoelzl, Lehnen, Schwarz and the JOREK
     Team, published under the new title above. Crossref lists 34
     references against 31 here, so the published text was revised;
     numbers may differ in the version of record, which was not read.
   * **How read.** Full text; Eqs. 1–8 checked on rendered pages (pp. 1,
     5); plot values are the reader's approximate readings.
   * **Recorded as printed.**
     * Eq. 1 places $1/\mu_0$ on the volume integral of
       $\mathbf J\times\mathbf B$ instead of on the Maxwell-stress surface
       integral; as printed the two sides differ by $\mu_0$.
     * "$\eta_w=0.8\,\mu\Omega$" lacks the metre; one value pair is given
       for "each layer".
     * Abstract "13 MN" and "safety factor remains above 2" against body
       11–14 MN and $q_{95}$ 3–4 (consistent but looser).
     * Refs. [11] and [12] are the same work (the JOREK review, Hoelzl et
       al. 2021), [11] printed "submitted, 2020"; [11] is cited for the
       DINA benchmark, which is odd for a code review.
     * Figs. 4 and 6 captions list $n=0,1,2,3$ in panel (d), the text "n =
       1, 2, 3"; Fig. 6b plots $-Z_{\mathrm{axis}}$; Figs. 4b and 6b plot
       $4\,l_i(3)$ (legend "li3x4"), unmentioned in the text.
     * Table 1: $\kappa$ in (m s)⁻¹, i.e. density-weighted diffusivities.
       Compiler's check, not a paper claim: $\eta_0=6.74\times10^{-7}$ Ω m
       at 300 eV is about 4× the $Z=1$ Spitzer value (≈$1.7\times10^{-7}$
       Ω m for $\ln\Lambda\approx17$); no $Z_{\mathrm{eff}}$ or $\ln\Lambda$
       is stated, so "realistic" resistivity cannot be verified.
     * Missing journal names in refs. [21], [23], [25], [29], [31]; [30]
       "in preparation".
     * Typos: "toroial", "cannot lost", "are the identical", "a important
       role".
     * Time step, solver settings and the initial "noise level" are not
       given.
   * **Reference list.** 31 printed entries, merged into the bibliography
     under `artola-2022`. Refs. [11] and [12] (`hoelzl-2021`, printed once
     as submitted and once as published) merge to the single entry of the
     ingested [Hoelzl et al. (2021)](/sources/hoelzl-2021.md). Ref. [5] is
     the ingested [Artola et al. (2021)](/sources/artola-2021.md); the
     COMPASS PPCF paper is `artola-2021-b`; Kiramov & Breizman PoP
     25:092501 is `kiramov-2018` (distinct from `kiramov-2017`); the
     COMPASS-U force paper is `yanovskiy-2021` (distinct from
     `yanovskiy-2022`); [30], printed 2021 "in preparation", is
     `sarkimaki-2022`; Pautasso et al. (printed "nov 2016", PPCF 59) is
     `pautasso-2016`. This source is itself cited as `artola-2022` by
     [Bandaru et al. (2024)](/sources/bandaru-2024.md),
     [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) and
     [Korving et al. (2023)](/sources/korving-2023.md).
