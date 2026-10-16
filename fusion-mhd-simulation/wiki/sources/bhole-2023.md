---
type: Source
title: "Bhole et al. (2023) — Stabilized bi-cubic Hermite Bézier finite element method with application to gas-plasma interactions occurring during massive material injection in tokamaks"
description: "Adds variational-multiscale (diagonal convective residual, fast-magnetosonic time scale) and field-aligned pressure-sensor shock-capturing stabilization to JOREK's bi-cubic Hermite–Bézier/Fourier finite elements for full MHD with coronal-equilibrium impurities, and shows on JET-like neon shattered pellet injection that shock capturing cuts GMRES hours about 2.7-fold while preserving the thermal-quench dynamics."
resource: "doi:10.1016/j.camwa.2023.04.034"
source_kind: paper
authors: [Bhole A., Nkonga B., Costa J., Huijsmans G., Pamela S., Hoelzl M.]
year: 2023
venue: "Comput. Math. Appl. 142:225-256"
local_file: "/home/stefano/papers/mosaic/fusion-mhd-simulation/2023_Crossref_Computers_amp_Mathematics_with_Applications_Bhole_Stabilized_bi-cubic_Hermite_Bézier_finite_element_method_wit.pdf"
tags: [full-mhd, reduced-mhd, finite-elements, stabilization, time-integration, disruption, impurities, tokamak, numerics]
timestamp: 2026-10-16T00:00:00Z
---

# Summary

The paper adds two stabilization terms to the Galerkin weak form of
[JOREK](/software/jorek.md)'s toroidal-Fourier × bi-cubic Hermite–Bézier
[finite elements](/methods/bezier-finite-elements.md) and applies them to the
single-fluid, single-temperature visco-resistive full-MHD model extended with
one impurity species in coronal equilibrium (ADAS charge-state, ionization-energy
and radiation data). The first is a
[variational multiscale (VMS)](/methods/variational-multiscale-stabilization.md)
term with a diagonal stabilization matrix scaled by the element size over the
element's maximum fast-magnetosonic speed, acting on a residual truncated to
its first-order (convective) part; in all tests only the diagonal of that
operator is kept, which reduces it to per-variable streamline diffusion. The
second is a [shock-capturing artificial viscosity](/methods/shock-capturing-artificial-viscosity.md)
with a field-aligned anisotropic tensor and a scalar coefficient built from a
pressure-gradient sensor and a pressure-rate "shock strength"; it acts on the
hydrodynamic equations, not on the induction equation. Time integration is the
JOREK three-level Crank–Nicolson/BDF2 family with one Newton iteration and
preconditioned GMRES. The application is [shattered pellet injection](/definitions/shattered-pellet-injection.md) (100 neon
or argon fragments) into a JET-like plasma (pulse 85943). In axisymmetric-source
tests, shock capturing smears pressure discontinuities locally and prevents
GMRES failure; in 3D full-MHD neon SPI it cuts the GMRES wall time to
$t\approx1.5$ ms from 13.6 h to 5 h, preserves the $W_{\mathrm{th}}$ and $I_p$
histories including the [thermal quench](/definitions/thermal-quench.md) and
the $I_p$ spike, and restores low-$n$ dominance of the magnetic-energy spectrum.
Too much stabilization alters or suppresses the thermal quench. Coefficients
are hand-tuned, and the effect of VMS alone is never isolated.

# Key claims

1. **Two stabilizations are needed** (§1, §3; pp. 4, 11). Galerkin FEM is
   centred and dispersive for convection-dominated flow, and high-order
   methods develop Gibbs oscillations at shocks, so an $L^2$-type (VMS) and a
   BV-type (shock-capturing) stabilization are combined. Stated.
2. **VMS keeps the order of accuracy** (§1 p. 4; §3.1 p. 12). The VMS term
   scales as $h_e$ times a mesh-independent inverse speed and vanishes as
   $h_e\to0$. Stated; no convergence study is shown.
3. **VMS is dissipative for symmetric operators** (Eq. 26, p. 12). If the
   linearized operator $\mathcal L$ is symmetric and the residual is
   approximated by $\mathcal L$ applied to the resolved state, the VMS term is
   a sum of non-negative quadratic forms. Derived (short).
4. **Shock capturing vanishes under refinement** (Eq. 32 p. 14; §4.3.2
   p. 38) through its $h_e^3$ scaling. Stated.
5. **No extra communication** (p. 16): the terms are element-local. Stated.
6. **Reduced MHD, axisymmetric argon source** (§4.2.1.1, Figs. 4–5). Without
   shock capturing the linear solver fails at about 0.59 ms; coefficient 0.1
   is indistinguishable from none; coefficient 1 runs further but deviates.
   Shown.
7. **Full MHD, axisymmetric neon source** (§4.2.1.2, Figs. 6–7). Unstabilized
   fails at about 1.4 ms; coefficient 1 runs past 2.5 ms with nearly the same
   thermal energy and slightly lower ablation. Shown.
8. **3D neon SPI step counts** (§4.3.1, Fig. 9a). Unstabilized needs more than
   9000 steps to reach about 1.7 ms and was abandoned; coefficient 1 needs more
   than 20000 steps to about 3 ms, coefficient 10 fewer than 6000. Shown.
9. **Cost** (Table 1, p. 35; 64 MPI processes, to $t\approx1.5$ ms). The larger
   stable $\Delta t$ outweighs the worse per-solve conditioning: GMRES hours
   13.6 (unstabilized), 11.8, 5.0 and 5.78 for coefficients 0, 1, 10, 50.
   Shown; the arithmetic checks.
10. **Spectrum** (Fig. 10, p. 29). In the unstabilized 3D run $W_{\mathrm{mag}}^{(7)}$
    exceeds the lower harmonics early, an "unphysical" cascade that "denotes a
    lack of resolution"; stabilized runs restore low-$n$ dominance. Shown;
    interpretation the authors'.
11. **Physics preserved** (Fig. 14, p. 33). $W_{\mathrm{th}}$ and $I_p$ agree between
    stabilized and unstabilized runs. Shown, but only up to about 1.75 ms, the
    end of the unstabilized run, i.e. before the thermal quench.
12. **Over-stabilization** (Fig. 11, pp. 30–31). Coefficient 50 "has altered the
    dynamics"; impurity-density snapshots differ from coefficients 1 and 10.
    Shown.
13. **Thermal quench reproduced** (§4.3.1, Figs. 12–14). With coefficient 10:
    core temperature drop between 2 and 3 ms, ergodization, growth of
    $m/n=3/1$, $2/1$ and later $1/1$ when fragments cross $q=2$, an $I_p$ spike at
    the end of the quench, qualitatively as in the reduced-MHD SPI results of
    Hu et al. (2021) and Hoelzl et al. (2020). Shown.
14. **Sensor localization** (Fig. 13 i–l). The shock-capturing coefficient is
    large only at the initial pedestal jump and at moving shocks near impurity
    clouds. Shown.
15. **Low resistivity** (§4.3.2, pp. 34–35). At $\eta_0=4.22\times10^{-9}$ Ω m the
    Eq. 32 sensor "does not provide the required stability"; a stronger
    modulation (Eq. 49) is introduced "based on experience". Stated; no failed
    run shown.
16. **Over-diffusive low-$\eta$ run** (Figs. 15–19). Simulation C (low $\eta$,
    Eq. 49, coefficient 10) runs at the largest step but is "very diffusive": no
    thermal quench, no $I_p$ spike, high-$n$ energies above low-$n$. Shown.
17. **Tuning** (pp. 24–25, §5). Optimal coefficients depend on $\eta$, $\nu$, the
    diffusivities and the grid, "based on experience". Stated.
18. **Element continuity.** The bi-cubic Hermite–Bézier element is called
    $C^1$ because the arc-length derivatives at a vertex are shared,
    element-independent unknowns (§3.3.2). Stated. Other JOREK sources call
    the same element $G^1$; see
    [Bézier–Hermite finite elements](/methods/bezier-finite-elements.md).

# Models and numerics

**Model** (Eqs. 1–5, p. 6), translated to SI with $\mu_0$ explicit (the paper
writes JOREK normalized units, $\mu_0=1$), Weyl gauge $\Phi=0$:

$$\begin{aligned}
&\partial_t\mathbf A=\mathbf v\times\mathbf B-\eta(\mathbf J-\mathbf J_x),\qquad \mathbf B=\frac{F_0}{R}\mathbf e_\phi+\nabla\times\mathbf A,\quad \mu_0\mathbf J=\nabla\times\mathbf B,\\
&\rho(\partial_t\mathbf v+\mathbf v\cdot\nabla\mathbf v)=-\nabla p+\mathbf J\times\mathbf B+\nu\nabla^2\mathbf v-\mathbf S_{\mathbf v},\\
&\partial_t\rho+\nabla\cdot(\rho\mathbf v)=\nabla\cdot(\mathsf D\nabla\rho)+S_\rho+m_{\mathrm{imp}}S_{\mathrm{imp}},\\
&\partial_t p+\mathbf v\cdot\nabla p+\Gamma p\nabla\cdot\mathbf v+\mathcal Q_{\mathrm{ion}}=(\Gamma-1)\nabla\cdot\big[(\mathsf K+n_{\mathrm{imp}}\mathsf D_{\mathrm{ion}})\nabla T\big]+S_p,\\
&\partial_t n_{\mathrm{imp}}+\nabla\cdot(n_{\mathrm{imp}}\mathbf v)=\nabla\cdot(\mathsf D_{\mathrm{imp}}\nabla n_{\mathrm{imp}})+S_{\mathrm{imp}}.
\end{aligned}$$

* $\rho$ is the total mass density (plasma plus impurities), $T$ the total
  temperature with $T_e=T/2$, and $p=(\rho+\alpha\,m_{\mathrm{imp}}n_{\mathrm{imp}})T$ with the impurity
  pressure factor $\alpha=\frac{m_i}{m_{\mathrm{imp}}}\frac{\bar z+1}{Z+1}-1$, $\bar z$ the mean
  impurity charge. Every diffusion tensor has the form
  $X_\parallel\mathbf b\mathbf b+X_\perp(\mathsf I-\mathbf b\mathbf b)$.
* $A_R$, $A_Z$ and $\psi=RA_\phi$ are evolved; $F_0$ is the fixed equilibrium
  function, not evolved. $\nabla\cdot\mathbf B=0$ by construction.
* **Coronal impurities** (Eqs. 11–14): charge-state fractions from ADAS at
  $(n_e,T_e)$, $n_e\simeq$ the total particle density. The ionization energy is
  carried as potential energy, $\mathcal Q_{\mathrm{ion}}=(\Gamma-1)[\partial_t(n_{\mathrm{imp}}E_{\mathrm{ion}})+\nabla\cdot(n_{\mathrm{imp}}E_{\mathrm{ion}}\mathbf v)]$
  with $E_{\mathrm{ion}}$ the coronal-mean cumulative ionization energy, to avoid
  artificial recombination radiation; radiation enters $S_p$ as
  $-n_en_{\mathrm{imp}}L_{\mathrm{rad}}(T_e)$, i.e. a contribution to $P_{\mathrm{rad}}$. See
  [coronal-equilibrium impurity model](/methods/coronal-equilibrium-impurity-model.md).
* **Transport**: $\eta=\eta_0 f(T,Z_{\mathrm{eff}})$, Spitzer-like ($f$ not given);
  $\nu=\nu_0T^{-3/2}$ in §2 and §4.2.1, constant $\nu=2.36\times10^{-7}$ kg m⁻¹ s⁻¹ in
  §4.3.
* **Equilibrium**: Grad–Shafranov, in registry form
  $\Delta^*\psi=-\mu_0R^2\,\mathrm dp/\mathrm d\psi-F\,\mathrm dF/\mathrm d\psi$ (printed without the
  $\mu_0R^2$ factor; Citations), solved with the same elements on a polar grid,
  then a flux-aligned multi-block grid (Fig. 3).
* **Boundaries** (p. 9): Dirichlet, frozen in time, on flux-aligned
  boundaries; on boundaries crossing flux surfaces a Bohm condition
  $\mathbf v\cdot\mathbf n=\pm\sqrt{\Gamma T}$ and a sheath heat-transmission condition
  with factor 7–8 ([sheath boundary conditions](/methods/sheath-boundary-conditions.md)).
* **Momentum projection** (p. 20): the momentum equation is projected on
  $N_i\mathbf e_R$, $N_i\mathbf e_Z$ and $N_i\mathbf B$; the last, parallel projection removes
  $\mathbf J\times\mathbf B$ and the fast wave from that equation.

**VMS** (§3.1, Eqs. 20–30). With $\mathbf u=\bar{\mathbf u}+\mathbf u'$ and
$\mathbf u'\simeq-\tau_{\mathrm s}\mathcal R(\bar{\mathbf u})$, the weak form gains
$-\int\mathcal L^{T}(\bar{\mathbf u}^*)\cdot\tau_{\mathrm s}\mathcal R(\bar{\mathbf u})\,\mathrm d\Omega$, with
$\tau_{\mathrm s}=(h_e/\text{max fast-magnetosonic speed on the element})\,\mathrm{diag}(C_i)$
and $h_e$ the shorter of the two mid-edge segments. The residual is
truncated to its first-order part (Eq. 28: Euler-like acoustic block in
$(\mathbf v,\rho,T)$ plus passive advection of $\mathbf A$ and of the impurities; no
Lorentz-force or induction coupling); the tests use only its diagonal (Eqs.
29–30), i.e. $\tau_{\mathrm s}(\mathbf v\cdot\nabla\bar u^*)(\mathbf v\cdot\nabla\bar u)$ per variable and
$\tau_{\mathrm s}(\mathbf v\times\nabla\times\mathbf A^*)\cdot(\mathbf v\times\nabla\times\mathbf A)$ for the vector potential.
Sub-scales vanish on element boundaries (no jump terms).

**Shock capturing** (§3.2, Eqs. 31–33, 49). Added form
$\nabla\bar{\mathbf u}^*:\nu_{\mathrm{sc}}[c_\parallel\mathbf b\mathbf b+c_\perp(\mathsf I-\mathbf b\mathbf b)]\nabla\bar{\mathbf u}$ with

$$\nu_{\mathrm{sc}}=h_e^2\,\frac{d_p+d_s}{p}\,\frac{h_e|\nabla p|}{p},$$

where $d_p$ and $d_s$ are the magnitudes of the pressure rates driven by the
differential operator and by the sources (chain rule through $\rho$,
$n_{\mathrm{imp}}$, $T$). It is a diffusivity of order $h_e^3|\dot p||\nabla p|/p^2$. All tests
use $c_\parallel=c_\perp$ (the shock-capturing coefficient quoted below); the
anisotropic option is not exercised. Eq. 49 replaces $(d_p+d_s)$ by an
operator-only rate with a larger value.

**Discretization** (§3.3). Isoparametric bi-cubic Hermite–Bézier
quadrilaterals (Czarny & Huysmans 2008): bi-cubic Bézier geometry, 4 unknowns
per vertex per variable (value, two arc-length first derivatives, mixed
derivative) with element-dependent scale factors; toroidal Fourier series.
Polar-axis singularity treated as in Bhole et al. (2022).

**Time integration** (Eq. 40, p. 16). Three-level scheme on
$\mathbf u^{n-1},\mathbf u^n,\mathbf u^{n+1}$ with step ratio $\Delta t_{n-1}/\Delta t_n$, a weight on
$\mathbf u^{n-1}$, and a $\theta_{\mathrm t}$-weighted spatial operator: Crank–Nicolson (weight
0, $\theta_{\mathrm t}=1/2$), BDF2/Gear (weight 1/2, $\theta_{\mathrm t}=1$), implicit Euler (weight 0,
$\theta_{\mathrm t}=1$); see [implicit time integration](/methods/implicit-time-integration.md). One Newton iteration with an approximate Jacobian per step,
preconditioned GMRES; stabilization terms implicit with the same
$\theta_{\mathrm t}$. MPI only, no GPU.

**Runs.** Reduced MHD: 4130 poloidal elements, $n=0..3$,
$\Delta t=1.48\times10^{-3}$ ms. Full MHD axisymmetric: 7645 elements, $n=0..3$,
$\Delta t=2.97\times10^{-4}$ ms, VMS $C_i=10^{-2}$. Full MHD 3D: 7645 elements,
$n=0..7$, BDF2, $\Delta t$ between 0.1 and 5 JOREK time units
($2.97\times10^{-4}$ ms each), 64 MPI processes; ITER HPC, Marconi-Fusion,
JFRS-1.

# Tests and results

**Setup** (§4.1): JET-like equilibrium after pulse 85943 at 62.4 s,
$B_\phi\approx3$ T, $I_p\approx2$ MA, central $T_e\approx3.28$ keV, central
$n_e\approx2.1\times10^{19}$ m⁻³, one X-point, $q=1..7$ surfaces. 100 fragments
injected at $t=0.03564$ ms near $(R,Z,\phi)=(3.05,1.7,4.51)$, straight
trajectories, ablation $\mathrm d r^{5/3}/\mathrm dt\propto-n_e^{1/3}T_e^{5/3}$, Gaussian
deposition (widths 0.08 m poloidally; toroidal width 1000 rad axisymmetric, 2
rad in 3D).

| Case | Model, impurity | Stabilization | Outcome |
|---|---|---|---|
| §4.2.1.1 | reduced MHD, Ar $1.5\times10^{22}$ atoms, axisymmetric | SC 0, 0.1, 1 (VMS unstated) | 0 fails at 0.59 ms; 0.1 ≡ 0; 1 runs on, deviates |
| §4.2.1.2 | full MHD, Ne $1.5\times10^{21}$, axisymmetric | VMS $10^{-2}$ + SC 0, 1 | 0 fails at 1.4 ms; 1 past 2.5 ms, $W_{\mathrm{th}}$ 0.5 → 0.27 MJ |
| §4.3.1 | full MHD, Ne, 3D, $\eta_0=4.22\times10^{-8}$ Ω m | none, or VMS $10^{-2}$ + SC 1, 10, 50 | TQ 2–3 ms, $W_{\mathrm{th}}$ 0.5 → 0.1 MJ, $I_p$ 2.0 → 1.88 MA with spike |
| §4.3.2 A | as §4.3.1 | SC 1, Eq. 33 | reference |
| §4.3.2 B | as §4.3.1 | SC 1, Eq. 49 | agrees with A |
| §4.3.2 C | $\eta_0=4.22\times10^{-9}$ Ω m | SC 10, Eq. 49 | over-diffusive: no TQ, no spike |

GMRES cost to $t\approx1.5$ ms (Table 1):

| SC coefficient | steps | s per solve | total |
|---|---|---|---|
| 0 | 8096 | 6.05 | 13.6 h |
| 1 | 3988 | 10.64 | 11.8 h |
| 10 | 1182 | 15.21 | 5.0 h |
| 50 | 1182 | 17.62 | 5.78 h |

Not present: no convergence-order or manufactured-solution study, no
canonical shock test, no VMS-only or shock-capturing-only 3D run, no
code-to-code or experimental comparison, no successful well-resolved low-$\eta$
run.

# Notation map

| Bhole et al. (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf A$, $\psi=RA_\phi$, $\mathbf B$, $\mathbf J=\nabla\times\mathbf B$ | $\mathbf A$, $\psi$, $\mathbf B$, $\mu_0\mathbf J=\nabla\times\mathbf B$ | JOREK units, $\mu_0=1$ |
| $F$ | $F_0$ | fixed, not evolved |
| $\mathbf J_\star$ | $\mathbf J_x$ | switched off in the tests |
| $\Phi$ (gauge, $\nabla\Phi\equiv0$) | $\Phi$ | Weyl gauge |
| $\boldsymbol v$ | $\mathbf v$ | |
| $\rho$ | $\rho$ | total mass density |
| $\rho_f$, $n_f$, $m_f$ | $m_{\mathrm{imp}}n_{\mathrm{imp}}$, $n_{\mathrm{imp}}$, $m_{\mathrm{imp}}$ | |
| $Z_f$, $Z_i$, $Z_z$, $z$ | $\bar z$ (words: mean impurity charge), $Z$, $z$ | |
| $\alpha_f$ | $\alpha$ (page-local) | impurity pressure factor |
| $T$, $T_e=T/2$ | $T$ (total), $T_e$ | single-temperature model |
| $\kappa_f$, $\mathcal L(\partial,n_f,n_e,T_e)$ | $E_{\mathrm{ion}}$, $\mathcal Q_{\mathrm{ion}}$ (page-local) | **collision:** native $\kappa$ is an ionization energy, registry $\kappa$ a heat conductivity; native $\mathcal L$ also denotes the Jacobian |
| $L_{\mathrm{rad}}$ | words; contributes to $P_{\mathrm{rad}}$ | |
| $\gamma$ | $\Gamma$ | **collision:** registry $\gamma$ is a growth rate |
| $\gamma_{sh}$ | words (sheath transmission factor) | |
| $\mu$, $\mu_0$ | $\nu$, $\nu_0$ | **collision:** native $\mu_0$ is the axis viscosity in §2 and vacuum permeability in App. A; registry $\mu$ is a magnetic moment |
| $\mathbb D$, $\mathbb D_f$, $\mathbb K$, $\mathbb D_\kappa$ | $\mathsf D$ ($D_\parallel$, $D_\perp$), $\mathsf D_{\mathrm{imp}}$, $\mathsf K$ ($\kappa_\parallel$, $\kappa_\perp$), $\mathsf D_{\mathrm{ion}}$ | |
| $\bar U$, $U'$, $\mathbf W$ | $\bar{\mathbf u}$, $\mathbf u'$, words | registry $\mathbf u$ = discrete state |
| $\mathcal R_u$, $\mathcal L$, $\mathcal L_a$, $\mathcal L_d$ | $\mathcal R$ (words: residual), $\mathcal L$, words | |
| $\tau$, $C_i$ | $\tau_{\mathrm s}$, $C_i$ | |
| $h_e$, $\lambda^e_{\max}$ | $h_e$, words | |
| $\tau_{sc}$, $c^\parallel$, $c^\perp$, $c$ | $\nu_{\mathrm{sc}}$, $c_\parallel$, $c_\perp$ (page-local), words | **collision:** native $c$ vs registry speed of light |
| $f_p$, $d_p$, $d_s$, $\beta_{sc}$ | words, $d_p$, $d_s$ | native $\beta$ is never plasma beta here |
| $\zeta$, $\theta$, $r_n$ (Eq. 40) | words (three-level weight), $\theta_{\mathrm t}$, words | **collision:** native $\zeta$ also a parametric coordinate; registry $\zeta$ a toroidal angle |
| $\Delta t^*$ | $\Delta t$ in JOREK units | 1 unit $=2.97\times10^{-4}$ ms |
| $s,t$; $\boldsymbol\zeta$, $\boldsymbol\xi$ | words (reference, parametric, arc-length coordinates) | |
| ME, TE | $W_{\mathrm{mag}}^{(n)}$, $W_{\mathrm{th}}$ | TE $=\int p$, without $3/2$ |
| $(R,Z,\phi)$, $\psi_N$, $q$ | same | orientation of $\phi$ not stated |

# Pages created or updated

Chunk 1 (2026-10-16) created every page of the bundle. This source is cited on:

* [Bézier–Hermite finite elements with toroidal Fourier harmonics](/methods/bezier-finite-elements.md)
* [Coronal-equilibrium impurity model](/methods/coronal-equilibrium-impurity-model.md)
* [Disruption: phases, current quench and current spike](/definitions/disruption.md)
* [Divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
* [Grad–Shafranov equation](/definitions/grad-shafranov-equation.md)
* [Implicit time integration and preconditioned Krylov solvers for nonlinear MHD](/methods/implicit-time-integration.md)
* [JOREK](/software/jorek.md)
* [Shattered pellet injection and massive material injection](/definitions/shattered-pellet-injection.md)
* [Sheath (Bohm) boundary conditions](/methods/sheath-boundary-conditions.md)
* [Shock-capturing artificial viscosity for MHD finite elements](/methods/shock-capturing-artificial-viscosity.md)
* [Single-fluid visco-resistive MHD model](/methods/visco-resistive-mhd-model.md)
* [Thermal quench](/definitions/thermal-quench.md)
* [Variational multiscale (VMS) stabilization for MHD finite elements](/methods/variational-multiscale-stabilization.md)

# Citations

1. `/home/stefano/papers/mosaic/fusion-mhd-simulation/2023_Crossref_Computers_amp_Mathematics_with_Applications_Bhole_Stabilized_bi-cubic_Hermite_Bézier_finite_element_method_wit.pdf`
   * **Version.** HAL preprint hal-03811224v1 (submitted 11 October 2022), 47
     PDF pages (HAL cover + 46 numbered pages): the pre-review submission, not
     the accepted manuscript or version of record. Page numbers above are
     printed page numbers (PDF page = printed + 1).
   * **Identity.** doi:10.1016/j.camwa.2023.04.034, checked on Crossref: Comput.
     Math. Appl. 142:225–256, issue July 2023, six named authors (the HAL title
     page adds "JOREK team"). Crossref lists 75 references against 66 printed
     here, so the published version differs at least in its bibliography.
   * **How read.** Full text, including appendices; equations, tables and
     figure captions read; plot values are approximate readings.
   * **Recorded as printed.**
     * Eq. 1 prints $\partial_t\mathbf A+\mathbf v\times\mathbf B$; the weak form (p. 20) uses
       $-\mathbf v\times\mathbf B$, the physical sign.
     * Momentum weak form (p. 20): the $\nabla(p+B^2/2)$ and $\mathbf B\cdot\nabla\mathbf B$ terms,
       and $\nabla p$ in the parallel projection, carry inverted signs relative
       to Eq. 2.
     * Induction weak form: the $\mathbf J_x$ term lacks the factor $\eta$ of Eq. 1.
     * Density weak form prints a doubled sign "$-S_\rho N_i+-S_{\rho_f}N_i$"; the
       energy equation of §3.3.4 is written for the extended pressure while
       Eq. 4 uses $p$ plus the ionization term (equivalent only if absorbed).
     * Eq. 25 lists 8 coefficients for 9 unknowns ($C_{v_\phi}$ missing) and
       labels $C_{A_\phi}$ although the unknown is $\psi$.
     * Eq. 28 ($\mathcal L_a$) omits all magnetic coupling, so it is not the
       first-order part of the full-MHD Jacobian as the text says; $\mathcal L$
       denotes three objects (Eqs. 13, 23, 33).
     * Eq. 4 writes $\mathcal L(\partial,n_f,n_e,T_e)$, p. 7 writes
       $\mathcal L(\partial,\rho_f,T_e)$.
     * $S_p$ (p. 8) contains Ohmic heating; p. 33 and §5 state the model used
       does not include it.
     * p. 10: "$\Gamma_D\cup\Gamma_N=\emptyset$" for $\cap$.
     * p. 17: index typo "$\zeta_{2,k+1,l+1l}$"; vertex $\boldsymbol\zeta_{k,l+1}$
       printed with $\zeta_1^{e+}(1)$ where $\zeta_1^{e-}(1)$ is expected.
     * Fig. 6 caption says argon; §4.2.1.2 says neon. Fig. 7 caption ("$n_f$ at
       $t\approx0.562$ ms") contradicts the text (total density at 0.095 ms),
       apparently copied from Fig. 5.
     * §4.3.2: the text calls simulation C's criterion Eq. 33, Table 2 says Eq.
       49; the text says the Eq. 32 sensor failed while Table 2 labels
       criteria by Eq. 33.
     * Eq. 49 uses $\frac1\rho\frac{\partial p}{\partial T}\mathcal L(p)$, not $\mathcal L(T)$ as
       Eq. 33; dimensionally consistent only if $p\sim\rho T$.
     * Table 1: coefficients 10 and 50 have identical step counts (1182) while
       Fig. 9a claims a further step advantage for 50; the text says
       coefficient 10 "takes less than twice the time" of the unstabilized run
       (5 h vs 13.6 h) and a few lines later "more than twice the speed up".
     * p. 3: "Massive material injection (MGI)".
     * Units: diffusivities printed "m².s"; heat conductivities in
       kg m⁻¹ s⁻¹; $K_\perp=4.72\times10^{-7}$ (reduced) vs $1.18\times10^{-6}$ (3D).
     * Viscosity temperature-dependent (p. 8, §4.2.1) but constant in §4.3.
     * Notation overloads: $\mu_0$ (axis viscosity, vacuum permeability),
       $\zeta$ (coordinate, BDF weight), $t$ (time, reference coordinate).
     * Thermal energy is defined as $\int p\,\mathrm d\Omega$ (App. A), without the
       factor $1/(\Gamma-1)=3/2$; the quoted MJ values are 2/3 of the
       conventional thermal energy if taken literally.
     * Grad–Shafranov printed as $R^2\nabla\cdot(R^{-2}\nabla\psi)=-FF'-p'$, without
       $\mu_0R^2$ on $p'$.
     * The VMS effect is not isolated: every stabilized run combines VMS and
       shock capturing, the unstabilized run has neither, and §4.2.1.1 does not
       say whether VMS was on.
     * Compiler's check, not a source claim: the three-level scheme with fixed
       weight 1/2 is second order only for constant $\Delta t$; second order at
       step ratio $r$ needs weight $1/(r(1+r))$. The paper does not say whether
       the weight is adapted, and the 3D runs change $\Delta t$.
   * **Reference list.** 66 printed references, merged into the bibliography
     under `bhole-2023` (66 entries); no DOIs printed, none added. The ADAS web
     resource [41], printed as a bare URL, is `adas-2023` (keyed by the
     earliest citing year in the corpus). Parks' unpublished note [66], printed
     with year 2020 and no venue, is `parks-2019` (the same note hoelzl-2021
     cites as a private communication of 2019). [60], printed with given and
     family names swapped, is `bhole-2022`. [36] (Hu et al. NF 2021, reduced-MHD
     SPI) is `hu-2021`; [40] (collisional-radiative impurity paper) is the
     ingested `hu-2021-b`. [6] (Pamela et al., $G$-continuous Bézier elements)
     is `pamela-2022`. [62] Ferraro et al., printed "Nuclear Fusion 59:016001,
     nov 2018", is `ferraro-2018`. [24] Hughes, Scovazzi & Franca 2004
     (encyclopedia chapter, no containing work printed) is entered as a book.
