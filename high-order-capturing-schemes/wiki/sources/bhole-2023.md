---
type: Source
title: "Bhole et al. (2023) — Stabilized bi-cubic Hermite–Bézier finite element method for gas–plasma interactions in tokamaks"
description: "Stabilizes the C1 bi-cubic Hermite–Bézier (× Fourier) Galerkin method of the JOREK MHD code with two terms: a VMS term with a diagonal time scale h_e/λ_max and the residual cut to its advective part (a per-variable streamline diffusion), and a field-aligned artificial viscosity driven by a pressure-gradient sensor times a pressure-rate shock strength; in implicit full-MHD simulations of shattered-pellet injection into a JET-like plasma the viscosity prevents GMRES failure and cuts the solver time to 1.5 ms from 13.6 h to 5 h, while too large a coefficient alters the thermal quench."
resource: "doi:10.1016/j.camwa.2023.04.034"
source_kind: paper
authors: [Bhole A., Nkonga B., Costa J., Huijsmans G., Pamela S., Hoelzl M.]
year: 2023
venue: "Comput. Math. Appl. 142:225–256"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2023_Crossref_Computers_amp_Mathematics_with_Applications_Bhole_Stabilized_bi-cubic_Hermite_Bézier_finite_element_method_wit.pdf"
tags: [finite-element, stabilization, artificial-viscosity, mhd, implicit, source-terms]
timestamp: 2026-10-16T00:00:00Z
---

# Summary

The paper stabilizes a high-order continuous Galerkin method for an
advection-dominated, shock-forming plasma system. The host is the MHD code
JOREK: isoparametric bi-cubic Hermite–Bézier elements, $C^1$ across
elements, in the poloidal plane, times a Fourier expansion in the toroidal
angle. The model is visco-resistive full MHD in vector-potential form,
extended with an impurity species in coronal equilibrium. Two terms are
added to the Galerkin weak form (§3).
* A **VMS** term models the unresolved scales as
  $u' \approx -\tau_{\mathrm{VMS}}\mathscr R(u_h)$, with a diagonal
  $\tau_{\mathrm{VMS}} = (h_{\mathrm e}/\lambda_{\max,\mathrm e})\,\mathrm{diag}(C^{\mathrm{VMS}}_\ell)$
  and the residual cut to its advective part; the diagonal option used in
  all tests is a streamline diffusion per variable
  ([VMS stabilization](/methods/variational-multiscale-stabilization.md)).
* A **shock-capturing artificial viscosity** acts on the hydrodynamic
  equations only, with a field-aligned anisotropic tensor and a coefficient
  $\mu_{\mathrm{sc}} = h_{\mathrm e}^2\,(\dot p_{\mathrm{op}} + \dot p_{\mathrm{src}})\,\chi_{\mathrm p}/p$
  ([artificial viscosity](/methods/artificial-viscosity.md)).

The authors frame the two as the $L^2$ part, which VMS gives for smooth
solutions, and the BV part, which it does not give near shocks. Time
integration is an implicit three-level BDF2/Crank–Nicolson family with
one Newton step and GMRES. The application is shattered-pellet injection
(SPI) of neon or argon into a JET-like plasma (§4). The viscosity
prevents the linear-solver failures of unstabilized runs, allows larger
steps, and preserves the integrated thermal energy and current as far as
the unstabilized run reaches. Too much of it ($C_{\mathrm{sc}} = 50$, or the
stronger sensor of eq. 49) visibly changes the dynamics. There is no
convergence study and no standard benchmark.

**Fit to this bundle.** The paper belongs here for two things: the
stabilization of a high-order element method for an advection-dominated
system with shocks, and a shock sensor whose strength includes source
terms. It has no dedicated stiff-source scheme: the sources enter only
through $\dot p_{\mathrm{src}}$ in the sensor and through the implicit time
step. Taylor–Galerkin stabilization appears only as JOREK's earlier
stabilization for reduced MHD and in the literature survey (§§1, 3.2); it
is not developed.

# Key claims

1. **Why Galerkin needs stabilization** (abstract, §§1, 3). Galerkin FEM
   gives centred approximations; for convection-dominated flows the
   dispersion errors can give "entirely wrong numerical solutions", and
   high-order methods develop high-wavenumber Gibbs oscillations near
   shocks that harm stability. The fluid models contain "a weakly
   hyperbolic operator" (§3).
2. **Lineage** (§1). Von Neumann–Richtmyer and Wilkins formulated the
   effect of unresolved scales as artificial viscosity; Godunov first
   evaluated subscale effects explicitly through Riemann problems; both
   are "mainly associated with finite volume and DG". Stabilized Galerkin
   families: Taylor–Galerkin, bubble functions, SUPG, VMS. The closest
   precedents are SUPG plus shock capturing for $C^1$ Powell–Sabin
   elements on the 2D Euler equations, and VMS plus discontinuity
   capturing for non-equilibrium industrial plasmas.
3. **VMS derivation** (§3.1, eqs. 20–24). Scale split, linearization
   $\mathscr R(u_h + u') \approx \mathscr R(u_h) + \mathscr J u'$,
   $u' \approx -\tau_{\mathrm{VMS}}\mathscr R(u_h)$ with
   $\tau_{\mathrm{VMS}} \approx \mathscr J^{-1}$; the stabilized form
   subtracts $\int(\mathscr J^{*}w_h)\cdot(\tau_{\mathrm{VMS}}\mathscr R(u_h))$.
   For nonlinear problems an optimal $\tau_{\mathrm{VMS}}$ is "still an open
   question".
4. **Time scale** (eq. 25). $h_{\mathrm e}$ is the shorter of the two
   mid-edge segments of the element, taken as straight-edged;
   $\lambda_{\max,\mathrm e}$ is the largest fast-magnetosonic speed over the
   element; $C^{\mathrm{VMS}}_\ell \ge 0$. $\tau_{\mathrm{VMS}} \to 0$ as
   $h_{\mathrm e} \to 0$, and the order of accuracy is kept (§1; stated, no
   convergence study).
5. **Dissipativity** (eq. 26). If $\mathscr J$ is symmetric and
   $\mathscr R(u_h) \approx \mathscr J u_h$, the term is a sum of
   dissipative contributions (one-line argument).
6. **Truncation** (eqs. 27–30). Following common practice, the residual
   is cut to its first-order part $\mathscr A$ (eq. 28: the acoustic block
   in primitive $(\mathbf v, \rho, T)$ plus passive advection of
   $\mathbf A$ and $\rho_{\mathrm f}$), or to its diagonal
   $\mathscr A_{\mathrm d}$ (eq. 30, used in all tests). The fine scales
   vanish on element boundaries, so the operator is element-local.
7. **Shock-capturing term** (§3.2, eqs. 31–33). The term is
   $\nabla w_h:(\mathbb D_{\mathrm{sc}}\nabla u_h)$ with
   $\mathbb D_{\mathrm{sc}} = \mu_{\mathrm{sc}}[C_\parallel\hat{\mathbf b}\otimes\hat{\mathbf b} + C_\perp(\mathbb I - \hat{\mathbf b}\otimes\hat{\mathbf b})]$
   and $\mu_{\mathrm{sc}} = h_{\mathrm e}^2(\dot p_{\mathrm{op}} + \dot p_{\mathrm{src}})\chi_{\mathrm p}/p$,
   $\chi_{\mathrm p} = h_{\mathrm e}\vert\nabla p\vert/p$. The form follows
   Bassi et al.'s DG viscosity and Giorgiani et al.'s Powell–Sabin
   elements. The extra factor $h_{\mathrm e}$ makes the viscosity vanish
   under refinement. The coefficients "require some tuning" and depend on
   the physical parameters and the local mesh size.
8. **Hydrodynamic variables only** (eq. 38). Zeros in the three
   vector-potential slots: the induction equation gets no viscosity,
   because the shocks of interest are hydrodynamic, from strong local mass
   sources (§§1, 3.2).
9. **Cheap in parallel** (p. 16). Two local contributions are added to
   the existing algorithm: "all computations are local and no additional
   communications associated with the parallel programming are involved".
10. **Reduced MHD, argon, axisymmetric source** (§4.2.1.1, Figs. 4–5).
    Without the viscosity the linear solver fails to converge at about
    0.59 ms, as discontinuities bring wavenumbers the grid cannot resolve.
    $C_{\mathrm{sc}} = 0.1$ is indistinguishable from it; $C_{\mathrm{sc}} = 1$
    runs longer and deviates. Along a chord through the impurity source,
    the pressure jump is smeared locally, more for larger $C_{\mathrm{sc}}$,
    and the solution elsewhere is not significantly affected (Fig. 5b).
11. **Full MHD, neon, axisymmetric source** (§4.2.1.2, Figs. 6–7). VMS
    with $C^{\mathrm{VMS}}_\ell = 10^{-2}$. Without the viscosity the solver
    fails at about 1.4 ms; $C_{\mathrm{sc}} = 1$ runs beyond it, with
    slightly lower ablation and nearly the same thermal energy.
12. **3D full MHD, neon** (§4.3.1, Fig. 9a). The run "without any numerical
    stabilization" needs more than 9000 steps to reach about 1.7 ms and was
    stopped; stabilized runs need fewer than 5000. To reach about 3 ms,
    $C_{\mathrm{sc}} = 1$ needs more than 20000 steps and $C_{\mathrm{sc}} = 10$
    fewer than 6000.
13. **Cost** (Table 1, 64 MPI processes, to $t \approx 1.5$ ms):

    | $C_{\mathrm{sc}}$ | steps | GMRES time per step [s] | total [h] |
    |---|---|---|---|
    | 0 | 8096 | 6.0461 | 13.6 |
    | 1 | 3988 | 10.6423 | 11.8 |
    | 10 | 1182 | 15.2078 | 5 |
    | 50 | 1182 | 17.6222 | 5.78 |

    Each solve grows dearer with stabilization, but larger steps win
    overall: "more than twice the speed up" for $C_{\mathrm{sc}} = 10$.
14. **Mode spectrum** (Fig. 10). In the unstabilized run the $n = 7$
    magnetic energy dominates the lower harmonics, a cascade that "denotes
    a lack of resolution", and the run does not proceed beyond about
    1.75 ms. The stabilized runs keep the low harmonics dominant (the
    "unphysical" reading is the authors').
15. **Physics preserved, within limits** (Figs. 11–14). Thermal energy and
    current agree between stabilized and unstabilized runs, so the
    viscosity "does not alter the underlying physics". The comparison
    stops where the unstabilized run stops, before the thermal quench
    (2–3 ms). $C_{\mathrm{sc}} = 10$ reproduces the quench, the ergodization,
    the 3/1, 2/1 and later 1/1 structures, and a current spike at its end,
    qualitatively as in earlier reduced-MHD studies. $C_{\mathrm{sc}} = 50$
    "has altered the dynamics and is more than required".
16. **Sensor map** (Fig. 13). The viscosity coefficient is large only near
    pressure discontinuities: near the boundaries, from a jump in the
    initial profile, and at moving shocks near impurity clouds.
17. **Lower resistivity** (§4.3.2, Table 2, Figs. 15–19). At a tenfold lower
    resistivity, eq. 32 "does not provide the required stability"; no
    failed run is shown. A stronger modulation, eq. 49, replaces the
    pressure rate by an operator-only expression, "based on experience".
    At the original resistivity it agrees closely with eq. 33 (simulations
    A, B, $C_{\mathrm{sc}} = 1$). At the low resistivity with
    $C_{\mathrm{sc}} = 10$ (simulation C) it runs at the largest step
    throughout but is "very diffusive": no thermal quench, no current
    spike, and high harmonics crossing the low ones.
18. **Conclusions** (§5). Optimal stabilization coefficients remain "a
    challenge" because of the nonlinearity and the many parameters. The
    method extends "straightforwardly" to JOREK's higher-order
    Hermite–Bézier elements (stated, not done). For ITER- or DEMO-size
    problems, AMR or multigrid may also be needed.

# Discretization (§3.3)

* **Space.** $\Omega = \Omega_X \times [0, 2\pi)$; the finite-element space
  is a product of poloidal and toroidal spaces. Toroidally, Fourier modes
  $\{1\}\cup\{\cos k\phi, \sin k\phi\}$ over a chosen set of $k$.
  Poloidally, the isoparametric bi-cubic Hermite–Bézier element of Czarny &
  Huysmans (2008).
  * Geometry is a bi-cubic Bézier patch on the reference square (eq. 41).
    Lines of constant arc-length coordinate are straight in a parametric
    space tiled by structured trapezoids (eq. 42).
  * Each vertex carries four degrees of freedom per variable: the value,
    the two arc-length first derivatives and the mixed derivative. These
    are shared by the four elements meeting at the vertex, which gives
    $C^1$.
  * The interpolant is a sum over the 4 vertices and the 4 degrees of
    freedom of each, with element-dependent scale factors (signed by the
    element orientation) times tensor products of the cubic Hermite
    functions $(1 + 2z)(1 - z)^2$ and $z(1 - z)^2$ (eqs. 43–44).
  * An annulus example gives the scale factors explicitly (§3.3.3).
  * Polar grids built this way have a geometric singularity at the axis,
    treated in Bhole et al. (2022).
* **Projections** (eq. 35, §3.3.4). The toroidal momentum equation is
  projected on $\mathbf B$, which removes the Lorentz force and the fast
  waves from that component (Haverkort et al. 2016).
* **Time** (eq. 40). For $\partial_t u_h$ the three-level difference is
  $\left[(1 + \rho_n\zeta_{\mathrm{BDF}})u^{n+1} - (1 + \zeta_{\mathrm{BDF}}(1 + \rho_n))u^n + \zeta_{\mathrm{BDF}}u^{n-1}\right]/\Delta t^n$,
  with page-local $\rho_n = \Delta t^{n-1}/\Delta t^n$ (not the density).
  The spatial and both stabilization terms are taken at
  $\theta_{\mathrm{BDF}}u^{n+1} + (1 - \theta_{\mathrm{BDF}})u^n$. Each step
  is one Newton iteration with an approximate Jacobian, solved by
  preconditioned GMRES. *Compiler's check:* a Taylor expansion with
  $\theta_{\mathrm{BDF}} = 1$ gives second order only for
  $\zeta_{\mathrm{BDF}} = 1/(\rho_n(1 + \rho_n))$, which is $\tfrac12$ at equal
  steps. With $\zeta_{\mathrm{BDF}} = \tfrac12$ fixed, unequal steps are first
  order. The paper does not say whether $\zeta_{\mathrm{BDF}}$ is adapted,
  and the 3D runs change $\Delta t$ repeatedly.

# Tests

1. **Set-up** (§4.1). JET-like equilibrium after pulse 85943 at 62.4 s:
   toroidal field about 3 T, plasma current about 2 MA, core electron
   temperature about 3.28 keV, core density about $2.1\times10^{19}$ m⁻³.
   Grad–Shafranov initial state on a flux-aligned multi-block grid with an
   X-point. Dirichlet conditions, with Bohm (Mach-1) and sheath conditions
   where the boundary crosses flux surfaces.
2. **SPI model.** 100 fragments released near a point on the boundary
   with random velocity and angle spreads. Fragment ablation
   $\frac{d}{dt}r_i^{5/3} \propto n_e^{1/3}T_e^{5/3}$ (eq. 47), and Gaussian
   impurity sources around each fragment (eq. 48).
3. **Runs.**
   * Reduced MHD, argon: 4130 poloidal elements, toroidal harmonics 0–3,
     BDF2.
   * Full MHD, neon, axisymmetric source: 7645 elements, harmonics 0–3.
   * Full MHD, neon, 3D source: 7645 elements, harmonics 0–7, normalized
     step between 0.1 and 5, axis resistivity $4.22\times10^{-8}$ and
     $4.22\times10^{-9}$ Ω m.
   * Always $C_\parallel = C_\perp$, so the anisotropic option is never
     exercised.
4. **Not present.** Convergence-order study, method of manufactured
   solutions, standard shock problems (Sod, Brio–Wu), VMS-only or
   viscosity-only runs in 3D, comparison with another code or with the
   JET experiment.

# Notation map

| Bhole et al. (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\boldsymbol u$ (interpolated primitive variables $A_r, A_z, \psi, v_r, v_z, v_\phi, \rho, t, \rho_f$) | $u_h$ | paper's $\bar{\boldsymbol u}$ in §3.1; **collision**: $\bar u_i$ is the cell average |
| $\boldsymbol u'$ | $u'$ | unresolved scales |
| $\boldsymbol u^*$, $n_i$, $\boldsymbol w^*$ | $w_h$ | test functions; $\boldsymbol w^*$ are the conservative-variable test functions, $\boldsymbol u^* = \mathbb M^{\mathsf T}\boldsymbol w^*$ (mass matrix kept in words) |
| $\boldsymbol w$ | $u$ (conservative-like) | eq. 15 |
| $\mathcal V$, $\mathcal V_h$, $\mathcal Z$ | $\mathcal V$, $\mathcal V_h$, $\mathcal V'$ | |
| $\boldsymbol{\mathcal R}$, $\boldsymbol{\mathcal R}_u$ | $\mathscr R$ | **collision**: $\mathcal R$ is the subcell reconstruction |
| $\mathcal L$ (Jacobian, eq. 23); $\mathcal L^t$ | $\mathscr J$; $\mathscr J^{*}$ | **collision**: $\mathcal L$ is the spatial operator; the paper also uses $\mathcal L$ for the ionization term (eq. 13) and for the operator inside eq. 33 |
| $\mathcal L_a$, $\mathcal L_d$ | $\mathscr A$, $\mathscr A_{\mathrm d}$ | |
| $\boldsymbol\tau$, $C_i$ | $\tau_{\mathrm{VMS}}$, $C^{\mathrm{VMS}}_\ell$ | **collision**: WENO-Z $\tau$, viscous stress $\boldsymbol\tau$ |
| $h_e$, $\lambda^e_{\max}$ | $h_{\mathrm e}$, $\lambda_{\max,\mathrm e}$ | |
| $D_{vms}$, $D_{sc}$ | words (the VMS and shock-capturing terms) | |
| $\underline{\tau_{sc}}$, $\tau_{sc}$ | $\mathbb D_{\mathrm{sc}}$, $\mu_{\mathrm{sc}}$ | **collision**: $\tau$ as above |
| $c_\parallel$, $c_\perp$, $c$ | $C_\parallel$, $C_\perp$, $C_{\mathrm{sc}}$ | **collision**: $c$ is the sound speed |
| $\boldsymbol b/\Vert\boldsymbol b\Vert$; $\mathbb I$ | $\hat{\mathbf b}$; $\mathbb I$ | the paper's bold $\boldsymbol b$ is the magnetic field |
| $f_p$ | $\chi_{\mathrm p}$ | |
| $d_p$, $d_s$ | $\dot p_{\mathrm{op}}$, $\dot p_{\mathrm{src}}$ | |
| $\beta_{sc}$ | words (the stronger modulation of eq. 49) | |
| $\boldsymbol a$, $\boldsymbol b$, $\boldsymbol j$, $\boldsymbol v$ | $\mathbf A$, $\mathbf B$, words (current), $\mathbf v$ | normalized units without $\mu_0$ |
| $\rho$, $p$, $t$ (temperature), $\gamma$ | $\rho$, $p$, $T$ (page-local), $\gamma$ | $\gamma = 5/3$; **collision**: the text layer prints temperature as $t$ |
| $\rho_f$ | $\rho_{\mathrm f}$ (page-local) | impurity mass density |
| $\eta$ | words (resistivity) | **collision**: $\eta$ is the coercivity constant |
| $\mu$ | words (viscosity) | the paper's $\mu_0$ is the axis viscosity, except in Appendix A, where it is the vacuum permeability |
| $\zeta$, $\theta$, $r_n$ (eq. 40) | $\zeta_{\mathrm{BDF}}$, $\theta_{\mathrm{BDF}}$, page-local $\rho_n$ | **collision**: cell coordinate $\zeta$, limiter $\theta$, stencil count $r$; the paper's $\zeta$ is also its parametric coordinate |
| $\Delta t_n$ | $\Delta t^n$ | variable-step convention of the registry |
| $(s, t)$, $\boldsymbol\zeta$, $\boldsymbol\xi$, $H^o_v$, $\beta^{o,e}_v$, $P^e_{ij}$ | words | element construction, kept on this page in words |
| $\Omega$ | $\Omega$ | |

# Pages created or updated

* Created [Variational multiscale (VMS) stabilization of continuous Galerkin methods](/methods/variational-multiscale-stabilization.md).
* Created [Artificial viscosity (shock-capturing diffusion)](/methods/artificial-viscosity.md),
  which also gathers the artificial-viscosity claims of Sod (1978),
  Woodward & Colella (1984), Balsara (1998) and Dumbser et al. (2014)
  already on their Source pages.
* Updated [WENO limiters for DG](/methods/weno-limited-dg.md),
  [RKDG](/methods/rkdg.md) and
  [fourth-order finite volume](/methods/fourth-order-finite-volume.md): a
  link from their mention of artificial viscosity to the new page.
* Updated [notation](/notation.md): the "Stabilized continuous Galerkin"
  section.

# Citations

1. `/home/stefano/papers/mosaic/high-order-capturing-schemes/2023_Crossref_Computers_amp_Mathematics_with_Applications_Bhole_Stabilized_bi-cubic_Hermite_Bézier_finite_element_method_wit.pdf`.
   * **Version read.** HAL preprint hal-03811224v1, submitted 11 October
     2022: a HAL cover page and 46 numbered pages. This is the submitted
     manuscript, not the version of record. Crossref counts 75 references
     for the published article; this copy prints 66, so the published
     text differs at least in its bibliography.
   * **Identity.** doi:10.1016/j.camwa.2023.04.034, checked on Crossref on
     2026-10-16: the title, the six authors (the HAL title page adds "JOREK
     team"), Computers & Mathematics with Applications 142:225–256, issue of
     July 2023. The slug takes the issue year.
   * **How it was read.** Full text extraction of every section,
     equations and the reference list. Figures were read from their
     captions and the text. Reader notes prepared for another context
     were used as a reading aid only, and each claim used here was checked
     against this PDF.
   * **Recorded as printed.**
     - Eq. 1 prints $+\mathbf v\times\mathbf B$ on the left; the weak form
       (§3.3.4) uses $-\mathbf v\times\mathbf B$, the physical sign.
     - The momentum weak forms print $-\nabla(p + \pi) + \mathbf B\cdot\nabla\mathbf B$
       and $-\nabla p$, opposite to the signs eq. 2 implies. The density
       weak form prints "$-S_\rho n_i + -S_{\rho_f}n_i$".
     - Eq. 25 lists 8 coefficients for 9 unknowns ($C_{v_\phi}$ is missing,
       and the $\psi$ slot is labelled $C_{a_\phi}$).
     - Eq. 28 is called the residual without second-order terms, but it has
       no magnetic coupling.
     - Eq. 49 prints $\frac1\rho\frac{\partial p}{\partial t}\mathcal L(p)$
       where eq. 33 has $\mathcal L(t)$.
     - §4.3.2 says simulation C uses "Eq. (33) with $c = 10$", but Table 2
       gives eq. 49. The text says eq. 32 failed, while Table 2 labels the
       criteria by eq. 33.
     - Table 1 gives $C_{\mathrm{sc}} = 10$ and $50$ the same step count
       (1182), yet the text says $C_{\mathrm{sc}} = 50$ gives "a further
       advantage in terms of time steps". The text also says
       $C_{\mathrm{sc}} = 10$ "takes less than twice the time" of the
       unstabilized run (5 h against 13.6 h), and a few lines later "more
       than twice the speed up".
     - The energy source contains Ohmic heating (§2), but §§4.3.1 and 5
       state that the model used "does not include" it.
     - "$\Gamma_D \cup \Gamma_N = \emptyset$" should be $\cap$ (§3).
     - Fig. 6's caption says argon, while §4.2.1.2 says a neon pellet.
     - "Massive material injection (MGI)" (§1) stands for massive gas
       injection.
     - The viscosity is $\mu_0 T^{-3/2}$ in §2 and §4.2.1, but "constant"
       in §4.3.
     - The Grad–Shafranov equation is printed without a factor $R^2$ on
       $dp/d\psi$.
     - The thermal energy is defined as $\int p\,d\Omega$, without
       $1/(\gamma - 1)$ (Appendix A).
   * **Reference list:** 66 printed entries, all merged; no DOIs are
     printed, so none were added. Same-work merges onto keys already in
     the bibliography:
     - Brooks & Hughes (1982), SUPG, lands on `brooks-1982` (renamed from
       `hughes-1982`, whose key came from a citation with the authors
       reversed; human decision 2026-10-16);
     - Johnson, Szepessy & Hansbo, Math. Comp. 54:107 (1990), is
       `johnson-1990`, kept distinct from the undated preprint
       `johnson-1989` cited by Cockburn et al. (human decision 2026-10-16);
     - the French Mir (1979) translation of Godunov et al. is
       `godunov-1979`, kept distinct from the Russian `godunov-1976`
       (human decision 2026-10-16);
     - Balsara et al. (2016), JCP 304:138, lands on `balsara-2016-d`, and
       Balsara & Nkonga (2017), JCP 346:25, on `balsara-2017-b`;
     - von Neumann & Richtmyer (1950), Balsara (2010) and Dumbser &
       Balsara (2016) land on their own keys.

     Other entries:
     - The ADAS database is printed as a URL only: `adas-2023` (no year
       printed; the citing date).
     - Hughes, Scovazzi & Franca (2004) is printed as a chapter with no
       containing work.
     - Bhole et al. (2022) is printed with given and family names swapped
       and "Accepted in Journal of Computational Physics".
     - Ferraro et al. is printed as Nucl. Fusion 59:016001 dated November
       2018 and keyed by the printed year.

     Bibliography: 3439 entries.
