---
type: Source
title: "Artola et al. (2021) — 3D simulations of vertical displacement events in tokamaks: A benchmark of M3D-C1, NIMROD, and JOREK"
description: "Three-code benchmark (JOREK, M3D-C1, NIMROD) of a nonlinear 3D hot VDE in an NSTX plasma with a rectangular resistive wall: the codes agree on kink onset, thermal-quench duration and wall forces, and differ on the toroidal asymmetry of the plasma current, which JOREK's reduced-MHD boundary condition suppresses."
resource: "doi:10.1063/5.0037115"
source_kind: paper
authors: [Artola F.J., Sovinec C.R., Jardin S.C., Hoelzl M., Krebs I., Clauser C.]
year: 2021
venue: "Phys. Plasmas 28:052511"
local_file: "/home/stefano/papers/mosaic/fusion-mhd-simulation/2021_Crossref_Physics_of_Plasmas_Artola_3D_simulations_of_vertical_displacement_events_in_tokamaks_A.pdf"
tags: [mhd, reduced-mhd, full-mhd, tokamak, disruption, vde, wall, free-boundary, finite-elements, benchmark, verification]
timestamp: 2026-10-16T21:00:00Z
---

# Summary

The paper is the first code-to-code benchmark of a fully 3D, nonlinear
vertical displacement event (VDE) with a resistive wall, run with
[JOREK](/software/jorek.md) (reduced MHD coupled to STARWALL),
[M3D-C1](/software/m3d-c1.md) (full single-fluid MHD) and
[NIMROD](/software/nimrod.md) (full MHD). The case continues the
axisymmetric benchmark of Krebs et al. (2020): an NSTX equilibrium
(discharge #139536 at 309 ms, EFIT) inside a simplified rectangular wall
($R\in[0.24,1.6]$ m, $Z=\pm1.4$ m, $d_w=0.015$ m,
$\eta_w=3\times10^{-5}$ Ω m). An axisymmetric phase, in which the plasma
drifts down until the lower wall limits it, is followed by a 3D phase
started at the limitation instant, with raised heat and particle
diffusivities. In all three codes, when $q_{95}$ falls to about 2 (the
$q=2$ surface enters the open-field-line region), low-$n$ external kinks
(2/1, 4/2, 6/3) go unstable 0.85–1.10 ms after limitation, stochastize the
field and drive a [thermal quench](/definitions/thermal-quench.md) of
0.14 ms (JOREK), 0.24 ms (M3D-C1) and 0.20 ms (NIMROD): a hot VDE. The
vertical wall force agrees closely (peak about 28–29 kN in magnitude) and
the peak horizontal (sideways) force lies within 2.5–3.5 kN, rotating less
than one toroidal turn. The codes disagree on the toroidal asymmetry of
the plasma current, $\Delta I_p/I_p$: 3–4% (NIMROD), 1–1.4% (M3D-C1),
below 0.01% (JOREK). The authors trace the JOREK value to the reduced-MHD
boundary condition $\Phi=$ const, which makes the plasma boundary a
poloidal ideal conductor. JOREK-only studies split the wall force into
[halo-current](/definitions/halo-current.md) and eddy-current parts (peak
forces come from halo currents) and show that a tenfold $\kappa_\parallel$
shortens the thermal quench threefold while leaving peak forces similar.

# Key claims

1. **First 3D VDE benchmark** (§1). No 3D VDE benchmark among these codes
   existed before. Stated.
2. **Setup inherits the axisymmetric benchmark** (§3). The 2D phase is the
   nonlinear case of Krebs et al. (2020) with wall resistivity, plasma
   resistivity and particle and heat diffusivities all multiplied by 10;
   plasma resistivity is 10 times the Spitzer value throughout. Stated.
3. **Time synchronization** (§4.1.1, Fig. 2). The 2D phase agrees as well
   as in the axisymmetric benchmark. Time is shifted so that limitation is
   at time zero in each code, because different initial perturbations give
   different VDE timings even when growth rates agree. Shown.
4. **Edge modes stabilized in the 2D phase** (§4.1.2). All three codes find
   the initial equilibrium unstable to resistive edge modes at $q=3$ and
   $q=4$; the evolving profiles stabilize them (none at axis height
   $Z=-0.15$ m, 1.4 ms before limitation). Stated (data not plotted).
5. **External-kink trigger** (§4.1.2, Eq. 7, Figs. 3–4). Low-$n$ external
   kinks become unstable when $q_{95}\approx2$, i.e. when the $q=2$ surface
   moves into the open-field region; the dominant structures 2/1, 4/2 and
   6/3 satisfy the external-kink criterion $0<nq_a<m$ with $q_a\approx1.8$.
   Before that, a weakly growing $n=1$ mixed 3/1 external kink and 2/1
   resistive mode is present. Shown.
6. **Onset window and spectrum** (§4.1.2, Figs. 3, 5). All codes go
   unstable 0.85–1.10 ms after limitation; $n=1$ dominates throughout,
   $n=2$ matters at the start of saturation, and $n=3$ transiently exceeds
   $n=1$ in JOREK and M3D-C1. Shown.
7. **Hot VDE** (§4.1.1). The thermal quench is caused by the vertical
   displacement and occurs after a strong loss of plasma volume (volume
   ratio 0.26 at 1.16 ms after limitation in JOREK). Shown.
8. **3D transport dominates the energy loss** (§4.1.1, Fig. 3). Once 3D
   MHD sets in, the thermal-energy decay rate is set by the 3D dynamics, not
   by the raised diffusivities. Shown (JOREK).
9. **High-$n$ ELMs avoided** (§4.1.1). Without raised 3D-phase
   diffusivities, high-$n$ edge-localized modes go unstable; the benchmark
   suppresses them to target low-$n$ wall forces. Stated (runs not shown).
10. **Thermal-quench durations** (§4.1.3, §5). 0.14 ms (JOREK), 0.24 ms
    (M3D-C1), 0.20 ms (NIMROD), consistent with the ~0.2 ms loss of core
    confinement in NSTX disruptions (Gerhardt et al. 2013). Shown.
11. **Stochastization from the edge** (§4.1.3, Figs. 6–7). The kinks grow
    from the edge and penetrate the core, forming an ergodic layer from
    about 1.00 ms, open-field-line core regions and finger-like pressure
    filaments, in all three codes. Shown.
12. **Vertical force** (§4.1.4, Fig. 8). $F_{w,z}$ is already large before
    the instabilities (a 2D effect); magnitudes and time evolution agree
    ("excellent agreement", §5). Shown.
13. **Horizontal force** (§4.1.4, §5, Fig. 8).
    $F_{w,h}=\sqrt{F_{w,x}^2+F_{w,y}^2}$ shows "good agreement in
    magnitude", with peak 3D horizontal forces of 2.5–3.5 kN. Shown.
14. **Force–mode correlation and rotation** (§4.1.4, Fig. 8). $F_{w,h}$
    tracks $W_{\mathrm{mag}}^{(1)}$ (two peaks for two peaks in JOREK). The
    force rotates less than one toroidal turn after the thermal quench:
    none in NIMROD, some between $n=1$ peaks in JOREK and M3D-C1. Shown.
15. **3D halo-current structure** (§4.1.5, Fig. 9, JOREK). At 1.04 ms the
    wall normal current shows filaments with strong $n=3$ content that
    reverse the sign of the $n=0$ normal current near the limiter point
    ($R\approx0.8$ m); at peak horizontal force (1.12 ms) the structure is
    dominantly $n=1$. Shown.
16. **$I_p$ toroidal asymmetry** (§4.1.6, Fig. 10). $\Delta I_p/I_p$ over 10
    toroidal planes: NIMROD 3–4%, M3D-C1 1–1.4%, JOREK below 0.01%;
    experiments show 10–20% (Gerasimov et al. 2015). Shown.
17. **Reduced-MHD boundary as a poloidal ideal conductor** (§4.1.6). In
    reduced MHD the poloidal electric field is $-\nabla_{\mathrm{pol}}\Phi$,
    and the normal-velocity boundary condition implies $\Phi=$ const on the
    boundary, so no current crosses it and $\partial_\phi I_p=0$. In the
    full-MHD codes the poloidal field equals $\eta$ times the poloidal
    current, which is finite, so current can cross the boundary. Derived.
    See [reduced-MHD current asymmetry](/results/reduced-mhd-current-asymmetry.md).
18. **Toroidal resolution** (§4.2, Fig. 11). $n\in[0,20]$ (JOREK) and
    $n\in[0,21]$ (NIMROD) change $I_p$, $W_{\mathrm{th}}$ and the wall forces
    only slightly relative to $n\in[0,10]$. Shown.
19. **Halo vs eddy horizontal force** (§4.3.1, Eq. 9, Fig. 12, JOREK).
    Because $\mathbf J\cdot\mathbf n=0$ at the JOREK wall, the force splits
    cleanly; the horizontal force (mainly $F_{w,y}$) is carried by halo
    currents, and the eddy part opposes it. Shown.
20. **Halo vs eddy vertical force** (§4.3.1, Fig. 12, JOREK). The two parts
    are similar before the thermal quench; afterwards the core-current decay
    induces halo current and the eddy part decreases, as in Clauser et al.
    (2019). Peak forces come from halo currents. Shown.
21. **Sensitivity to $\kappa_\parallel$ and viscosity** (§4.3.2, Fig. 13,
    JOREK). $10\kappa_\parallel$ shortens the thermal quench from 0.14 to
    0.043 ms (factor ≈3, not linear in $\kappa_\parallel$); $F_{w,h}$ is
    larger during the quench but peak forces stay similar (3.5–4.2 kN). A
    threefold smaller viscosity has a minor effect on $I_p$ and
    $W_{\mathrm{th}}$ and a perceptible one on the wall force. Shown.
22. **Ansatz-based reduced MHD at low aspect ratio** (Abstract, §2, §5).
    JOREK's ansatz-based reduced model captures the 3D VDE dynamics and wall
    currents "even in the spherical tokamak limit", unlike reduced models
    ordered in the aspect ratio. Shown by agreement with the full-MHD codes,
    with the $I_p$-asymmetry exception.
23. **Motivation for a JOREK full-MHD wall** (§5). The asymmetry result
    motivates a resistive wall for JOREK's full-MHD model. Stated.
24. **Hot VDEs and forces** (§4.1.1). Hot VDEs show the largest wall forces
    observed in experiments. Stated.
25. **Axisymmetric codes** (§1). Below $q_a\approx2$ the configuration does
    not stay axisymmetric; axisymmetric codes (DINA, TSC, CarMa0NL) may
    impose $q_a\ge1$ by forcing the current profile. Stated.

# Models and numerics

**Code comparison** (Table 1):

| Feature | JOREK | M3D-C1 | NIMROD |
|---|---|---|---|
| Toroidal discretization | Fourier harmonics | cubic Hermite elements | Fourier harmonics |
| Poloidal elements | quadrilateral isoparametric bicubic Bézier | triangular reduced-quintic (Bell) | quadrilateral bicubic $C^0$ spectral elements (Legendre-spaced nodes, degree 3) |
| Continuity | $G^1$ (geometric) | $C^1$ | $C^0$ |
| Wall | axisymmetric thin wall | axisymmetric thick wall | axisymmetric thin wall |
| Vacuum | not meshed, Green's functions (STARWALL) | meshed to the outer boundary | meshed to the outer boundary |
| Model | reduced MHD | full single-fluid MHD | full MHD |
| Time advance | implicit (Gear) | split-implicit | split-implicit (implicit leapfrog in the text) |

**JOREK model** (Eqs. 1–6, SI, $\mu_0$ explicit):

$$\begin{aligned}
\partial_t\mathbf A &= \mathbf v\times\mathbf B-\eta\mathbf J-\nabla\Phi,\\
\rho\,\partial_t\mathbf v &= -\rho\mathbf v\cdot\nabla\mathbf v-\nabla p+\mathbf J\times\mathbf B+(\text{viscous force})+\mathbf S_{\mathbf v},\\
\partial_t\rho &= -\nabla\cdot(\rho\mathbf v)+\nabla\cdot(\mathsf D\nabla\rho)+S_\rho,\\
\partial_t p &= -\mathbf v\cdot\nabla p-\Gamma p\nabla\cdot\mathbf v+(\Gamma-1)\nabla\cdot(\mathsf K\nabla T)+(\Gamma-1)(\text{viscous heating})+S_p,
\end{aligned}$$

with the reduced-MHD ansatz

$$\mathbf B=\nabla\psi\times\nabla\phi+F_0\nabla\phi,\qquad
\mathbf v=-R^2\nabla u\times\nabla\phi+\mathbf v_\parallel,\qquad u=\Phi/F_0 .$$

$\mathsf D$ and $\mathsf K$ are the anisotropic diffusion and conduction
tensors with parallel and perpendicular coefficients $D_\parallel$,
$D_\perp$ and $\kappa_\parallel$, $\kappa_\perp$. $F_0$ is constant, so the toroidal
field is fixed in time: poloidal currents evolve but their contribution to
$B_\phi$ is dropped. The reduction is "ansatz-based and does not result
from geometrical ordering assumptions". The sources are unused. $T$ is the
total temperature. JOREK also has a full-MHD model without a resistive
wall. Free boundary and thin resistive wall come from STARWALL: Green's
functions for the vacuum, linear triangles for the wall (3D walls with
holes are possible; the wall here is axisymmetric).

**M3D-C1.** Fully 3D nonlinear, full single-fluid MHD option. $\mathbf A$
is represented by $\psi$, a second scalar potential for the rest of the
poloidal part, and a term carrying the vacuum toroidal field $F_0$
(proportional to the total coil current); $\mathbf v$ by a stream function,
a toroidal-velocity scalar and a compressional potential (native form in
the Notation map). Other options: 2- and 4-variable reduced MHD,
two-fluid. Conductors advance only $\mathbf A$ with
$\mathbf E=\eta_w\mathbf J$; the vacuum obeys
$\nabla\times\nabla\times\mathbf A=0$. Unstructured triangular poloidal
mesh extruded toroidally; elements are the tensor product of the Bell
element and a Hermite cubic in $\phi$, $C^1$ for every scalar.
Split-implicit order: velocity, magnetic field, pressures, density;
optional implicit hyper-resistivity. Temperature and density conditions
are set at the plasma boundary, magnetic conditions at the outer boundary.

**NIMROD.** Evolves components of $\mathbf B$ and $\mathbf v$. The
equations equal JOREK's except that Faraday's law replaces the
vector-potential equation, particle diffusivity is isotropic, and a
temperature equation replaces the pressure equation. Resistivity uses the
axisymmetric part of $T$. Implicit leapfrog, with smaller but cheaper
steps than fully implicit schemes. Toroidal Fourier harmonics on 2D $C^0$
spectral elements of degree 3. $\nabla\cdot\mathbf B$ is not zero
identically; a diffusive correction proportional to
$\nabla(\nabla\cdot\mathbf B)$ is added to Faraday's law. The thin wall
couples to a meshed external vacuum. A stabilization against numerical
interchange is used.

**Boundary conditions.** Dirichlet density and temperature at their
initial values ($T_e=14.6$ eV, $n_e=2.20\times10^{18}$ m⁻³ at the edge).
Velocity: $\mathbf v=0$ (M3D-C1, NIMROD); $\mathbf v\cdot\mathbf n=0$,
$v_\parallel=0$ and $\varpi=0$ (JOREK).

**Physical parameters** (Table 2). No loop voltage, Ohmic heating,
radiation or sources; deuterium, $Z=1$, $T_e=T_i$. Dynamic viscosity
$5.16\times10^{-7}$ kg m⁻¹ s⁻¹ (parallel and perpendicular; NIMROD raises
the parallel value to 100 times the perpendicular 1.08 ms into the 3D
phase). $\eta=1.75\times10^{-2}\,T_e[\mathrm{eV}]^{-3/2}$ Ω m. 2D phase:
$\kappa_\perp=10^{-5}\kappa_\parallel=1.54\times10^{19}$ (m s)⁻¹,
$D_\perp=D_\parallel=1.54$ m² s⁻¹. 3D phase:
$\kappa_\perp=10^{-5}\kappa_\parallel=2.35\times10^{21}$ (m s)⁻¹,
$D_\perp=D_\parallel=40$ m² s⁻¹. $T_e=T_i=946\,\mathrm{eV}\,(p/p_{\mathrm{axis}})^{0.6}$.

**Resolution and time steps** (§3; $\tau_A$'s length not stated):

* JOREK: polar grid refined where the plasma becomes limited; 22000 Bézier
  elements, 48000 wall triangles, $n\in[0,10]$; $\Delta t\approx5$–10
  $\tau_A$ (2D), 0.1–0.2 $\tau_A$ (3D).
* M3D-C1: mesh of the axisymmetric benchmark, 17424 vertices per plane,
  12 degrees of freedom per scalar per vertex (6 in 2D), 16 toroidal
  planes; $\Delta t=0.5\tau_A$, halved for 0.048 ms around 1.233 ms after
  the 3D start to avoid a numerical instability, after which an upwind
  toroidal diffusion $0.125\,\Delta x\,v_\phi$ ($\Delta x=0.4$ m plane
  spacing) is added to the convection of pressure, density and field.
* NIMROD: 39000 bicubic elements inside the wall, packed near it; vacuum
  meshed as in M3D-C1; $n\in[0,10]$, the most dynamic interval rerun with
  $n\in[0,21]$; $\Delta t$ adapted to the flow CFL (above $0.015\tau_A$ in
  the most dynamic phase, "hundreds of times larger than an explicit
  stability limit").
* Marconi-Fusion and NERSC; no costs, core counts or wall-clock times; no
  GPU.

**Diagnostics.** $W_{\mathrm{mag}}^{(n)}=\int|\mathbf B^{(n)}_{\mathrm{pol}}|^2dV/(2\mu_0)$.
Wall force (JOREK, NIMROD; Eq. 8, after Pustovitov et al. 2017):

$$\mathbf F_w\equiv\int_{\mathrm{wall}}\mathbf J\times\mathbf B\,dV=\frac{1}{\mu_0}\oint_{\mathrm{wall}+}\Big[(\mathbf B\cdot\mathbf n)\mathbf B-\tfrac12B^2\mathbf n\Big]dS ,$$

over a closed toroidal surface enclosing the wall; M3D-C1 integrates
$\mathbf J\times\mathbf B$ over the vessel elements. In JOREK
(Eq. 9) the same integral of the Maxwell stress $\mathbf f$ over the surface just inside the
wall gives the halo part; the eddy part is the difference of the outside
and inside integrals. $I_p$ is evaluated on 10 planes $\phi=2\pi k/10$.

# Tests and results

**Equilibrium** (Fig. 1d): $I_p=5.74\times10^5$ A, magnetic energy
$1.12\times10^5$ J, $W_{\mathrm{th}}=7.61\times10^4$ J, $\beta_N=3.83$%,
$\beta_p=0.532$, $l_i(3)=0.698$, $q_0=2.04$, $q_{95}=7.32$, volume 11.9 m³,
X-point $(0.606,-1.26)$ m with $\psi=1.19\times10^{-2}$ Wb/rad, axis
$(1.07,-1.52\times10^{-2})$ m with $\psi=-4.73\times10^{-2}$ Wb/rad. The
2D phase moves the plasma about 1 m in about 10 ms (experiments: 5–20 ms).

**Comparison** (fig. = approximate plot reading):

| Quantity | JOREK | M3D-C1 | NIMROD |
|---|---|---|---|
| 3D onset after limitation | 0.85–1.10 ms (all) | | |
| Thermal-quench duration | 0.14 ms | 0.24 ms | 0.20 ms |
| Peak $W_{\mathrm{mag}}^{(1)}$ (fig.) | ≈0.2 kJ (two peaks) | ≈0.37 kJ | ≈0.53 kJ |
| Peak $\lvert F_{w,z}\rvert$ (fig.) | ≈28 kN | ≈28 kN | ≈29 kN |
| Peak $F_{w,h}$ (fig.) | ≈3.4 kN | ≈2.8 kN | ≈2.5 kN |
| Force rotation | some, between $n=1$ peaks | some | none |
| $\Delta I_p/I_p$ | <0.01% | 1–1.4% | 3–4% |
| $I_p$ spike peak (fig.) | ≈0.59 MA | ≈0.565–0.57 MA | ≈0.565–0.57 MA |

* M3D-C1's $n\ge1$ growth and saturation lag JOREK and NIMROD by about
  0.1–0.2 ms (Figs. 3, 5, 8), not discussed; NIMROD's $n=1$ shows an
  undiscussed slow early growth from about 0.3 ms.
* Toroidal halo current (JOREK, M3D-C1 only) reaches ≈0.4 and ≈0.35 MA at
  about 1.5 ms (Fig. 2); NIMROD's open/closed-field-line post-processing
  and $q_{95}$ are not available for VDEs.
* JOREK decomposition (Fig. 12): $F_{w,y}$ ≈3.4 kN peak, carried by halo
  currents, eddy part −0.8 to +0.5 kN; $F_{w,x}\le1$ kN; $F_{w,z}$ from
  about −20 to −28 kN between 0.8 and 1.25 ms, halo part −10 to −30 kN,
  eddy part −10 to +2 kN.
* JOREK sensitivity (Fig. 13): thermal quench 0.043 ms at
  $10\kappa_\parallel$; peak $F_{w,h}$ 3.5–4.2 kN across variants.

# Notation map

| Artola et al. (2021) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $(R,\phi,Z)$ | $(R,Z,\phi)$ | handedness of $\phi$ not stated |
| $\rho$ | $\rho$ | called "ion density" in the text; mass density |
| $T$ | $T$ | total temperature $T_e+T_i$ |
| $\Phi$ | $\Phi$; stream function $u=\Phi/F_0$ | Eq. 6 uses $\Phi$ directly in the velocity ansatz |
| $\mathbf v_\parallel$ | $\mathbf v_\parallel=v_\parallel\mathbf b$ | |
| $\gamma$ | $\Gamma$ | **collision:** registry $\gamma$ is a growth rate; value not stated |
| $\underline{\boldsymbol\tau}$ | $\mathsf\Pi$ (viscous part of the stress tensor) | |
| $\underline{\boldsymbol\kappa}$; $\kappa_\parallel,\kappa_\perp$ | $\mathsf K$; $\kappa_\parallel$, $\kappa_\perp$ | printed in (m s)⁻¹, density-times-diffusivity form |
| $\underline{\mathbf D}$; $D_\parallel,D_\perp$ | $\mathsf D$; $D_\parallel$, $D_\perp$ | |
| $\nu_\parallel,\nu_\perp$ | $\nu$ | dynamic viscosity, kg m⁻¹ s⁻¹ |
| $\Delta_w$ | $d_w$ | |
| $\eta_w$ | $\eta_w$ | |
| $w_\phi$ | $\varpi$ | toroidal vorticity (JOREK boundary condition) |
| $\psi$ | $\psi$ | per radian (Wb/rad) |
| $F_0$ | $F_0$ | |
| M3D-C1: $\mathbf A=\psi\nabla\phi+R^2\nabla\phi\times\nabla f-F_0\ln R\,\nabla Z$ | words | **collision:** $f$ vs distribution function $f_s$ |
| M3D-C1: $\mathbf v=R^2\nabla U\times\nabla\phi+wR^2\nabla\phi+R^{-2}\nabla_\perp\chi$ | $U\leftrightarrow u$ (opposite sign convention to JOREK); $w$, $\chi$ words | **collision:** $\chi$ is the registry vacuum scalar potential; $w$ vs marker weight $w_p$; M3D-C1's $\nabla_\perp$ is the gradient in the $(R,Z)$ plane, not across $\mathbf B$ |
| $\kappa_{divb}$ | words (divergence-cleaning diffusivity) | NIMROD |
| $\delta x$ | $\Delta x$ | toroidal plane spacing |
| $W^n_{mag}$ | $W_{\mathrm{mag}}^{(n)}$ | |
| $W_{th}$, $W_{thm}$ | $W_{\mathrm{th}}$ | |
| $\mathbf F$, $F_x,F_y,F_z$, $F_h$ | $\mathbf F_w$, $F_{w,x},F_{w,y},F_{w,z}$, $F_{w,h}$ | |
| $\mathbf f$ | $\mathbf f$ | normal-projected Maxwell stress; distinct from the distribution function $f_s$ |
| $I_{halo,\phi}$ | words (toroidal halo current) | registry $I_{\mathrm{halo}}$ is poloidal unless stated |
| $\mathbf E_{pol}$, $\mathbf J_{pol}$, $\nabla_{pol}$ | words (poloidal components); $\nabla_{\mathrm{pol}}$ | |
| $t'$ | words (time since limitation) | |
| $V_p$ | words (plasma volume) | |
| $q_{95}$, $q_a$ | $q_{95}$, $q_a$ | used interchangeably as "edge q" (see below) |

# Pages created or updated

Chunk 1 (2026-10-16) created every page of the bundle; chunks 2 and 3 (2026-10-16) extended many. This source is cited on:

* [Bézier–Hermite finite elements with toroidal Fourier harmonics](/methods/bezier-finite-elements.md)
* [Disruption: phases, current quench and current spike](/definitions/disruption.md)
* [Divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
* [Edge-localized mode (ELM) and ELM-free regimes](/definitions/edge-localized-mode.md)
* [Electromagnetic wall forces (vertical and sideways)](/definitions/wall-forces.md)
* [Free-boundary and resistive-wall coupling](/methods/resistive-wall-coupling.md)
* [Grad–Shafranov equation](/definitions/grad-shafranov-equation.md)
* [Halo current](/definitions/halo-current.md)
* [Implicit time integration and preconditioned Krylov solvers for nonlinear MHD](/methods/implicit-time-integration.md)
* [JOREK](/software/jorek.md)
* [M3D](/software/m3d.md)
* [M3D-C1](/software/m3d-c1.md)
* [NIMROD](/software/nimrod.md)
* [NSTX VDE benchmarks of JOREK, M3D-C1 and NIMROD (axisymmetric and 3D)](/benchmarks/nstx-vde-benchmarks.md)
* [Reduced MHD for tokamaks](/methods/reduced-mhd.md)
* [Reduced-MHD boundary condition suppresses the toroidal asymmetry of the plasma current](/results/reduced-mhd-current-asymmetry.md)
* [Semi-implicit leapfrog](/methods/semi-implicit-leapfrog.md)
* [Single-fluid visco-resistive MHD model](/methods/visco-resistive-mhd-model.md)
* [STARWALL](/software/starwall.md)
* [Thermal quench](/definitions/thermal-quench.md)
* [Vertical displacement event (hot and cold VDE)](/definitions/vertical-displacement-event.md)
* [Vertical-force mitigation by massive material injection](/results/vertical-force-mitigation.md)

# Citations

1. `/home/stefano/papers/mosaic/fusion-mhd-simulation/2021_Crossref_Physics_of_Plasmas_Artola_3D_simulations_of_vertical_displacement_events_in_tokamaks_A.pdf`
   * **Version.** arXiv:2011.04523v1 [physics.plasm-ph], 9 November 2020,
     29 pages, a pre-submission version ("will be submitted to Physics of
     Plasmas"); not the version of record. Numbers and wording may differ
     from the published article.
   * **Identity.** doi:10.1063/5.0037115, checked on Crossref: Phys.
     Plasmas 28(5), article 052511, issue 1 May 2021, online 24 May 2021;
     title and six authors match page 1. The filename says "Crossref" but
     the content is the arXiv preprint.
   * **How read.** Full text, Tables 1–2 and all equations; a garbled
     text-extraction passage in §4.1.2 was checked on the rendered page.
     Plot values are the reader's approximate readings.
   * **Recorded as printed.**
     * §2 says JOREK uses "typically the Crank-Nicolson or the BDF5 Gears
       scheme" and Table 1 says "Implicit (Gears)"; other JOREK sources
       describe the Gear scheme as BDF2 ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md),
       [Bhole et al. (2023)](/sources/bhole-2023.md)). Recorded as printed; closed by human fiat (2026-10-16) as
       a slip ([implicit time integration](/methods/implicit-time-integration.md)).
     * Table 1 labels NIMROD's time advance "Split-implicit"; the text
       describes implicit leapfrog. Table 1 header: "Toroidal dicretization".
       The Bell element is cited to Braess's textbook.
     * §4.2 says NIMROD was repeated with $n\in[0,20]$; §3 and the Fig. 11
       legend give $n\in[0,21]$.
     * Table 2 units "(ms)⁻¹" and "kg (ms)⁻¹" mean (m s)⁻¹ and kg m⁻¹ s⁻¹.
       The chained "$\kappa_\perp=10^{-5}\kappa_\parallel=1.54\times10^{19}$"
       assigns the number to $\kappa_\perp$, implying
       $\kappa_\parallel=1.54\times10^{24}$ (2D) and $2.35\times10^{26}$
       (m s)⁻¹ (3D) (compiler's reading). "coeffcients" typo.
     * §3: "1.233 after the start of the 3D" lacks a unit (ms implied).
     * §4.1.1: "decreased by more than a factor of two" for a volume ratio
       of 0.26 (nearly a factor 4).
     * Fig. 3 calls $q_{95}$ the "edge safety factor" while Eq. 7 uses the
       cylindrical $q_a\approx1.8$; the JOREK $q_{95}$ minimum in Fig. 3 is
       ≈1.7.
     * Fig. 6 shows M3D-C1 at 1.15, 1.21, 1.25 ms and JOREK/NIMROD at 1.00,
       1.05, 1.10 ms, reflecting M3D-C1's delay without saying so.
     * Eq. 9's inner surface "wall−" is not defined.
     * "2.5–3.5 kN" (§5) and "3.5–4.2 kN" (§4.3.2) refer to different runs
       (benchmark vs JOREK variants); not a contradiction.
     * Supplementary-material URL printed as the placeholder "[link]".
     * §1 syntax "Pfefferlé, et al with [12] M3D-C1 [13]" is garbled.
     * Typos: "equidistiant" (Fig. 10), "Cambrige" (ref. [22]).
   * **Reference list.** 31 printed entries, merged into the bibliography
     under `artola-2021`. Gerhardt 2013 [26] and [28] are `gerhardt-2013`
     and `gerhardt-2013-b`; Artola's thesis, printed "F.J. Artola Such"
     [14], is `artola-2018-c`; the axisymmetric benchmark [17] is
     `krebs-2020`; Pamela et al. full MHD [20], printed "submitted" without
     year, is `pamela-2020` (Phys. Plasmas 27:102510); ref. [6]
     (`jardin-1986`) prints an OSTI report DOI for a J. Comput. Phys.
     article and is kept with a note. Name variants Huysmans/Huijsmans and
     Hölzl/Hoelzl are the same persons. The ITPA disruption review [2] has
     a garbled collaboration name.
