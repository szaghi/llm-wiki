---
type: Source
title: "Mullen, Hanawa & Gammie (2021) — An Extension of the Athena++ Framework for Fully Conservative Self-Gravitating Hydrodynamics"
description: "Discretizes the self-gravity momentum and energy source terms in Athena++ as exact discrete divergences of a gravitational stress tensor and energy flux, so total momentum and energy are conserved to round-off with periodic boundaries; shows the stress tensor of Athena and Athena++ v19.0 is not curl-free and causes anomalous accelerations near massive bodies with light atmospheres, and gives a corrected tensor."
resource: "doi:10.3847/1538-4365/abcfbd"
source_kind: paper
authors: [Mullen P.D., Hanawa T., Gammie C.F.]
year: 2021
venue: "Astrophys. J. Suppl. 252:30"
local_file: "/home/stefano/papers/mosaic/astrophysical-simulation-codes/2021-ApJS-Mullen-1038471538-4365abcfbd.pdf"
tags: [software, self-gravity, conservation, hydro, time-integration, verification, benchmark]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

The paper implements in [Athena++](/software/athena-plus-plus.md), on static
uniform Cartesian meshes only, a self-gravity coupling in which the momentum
and energy source terms are each exactly the discrete divergence of a
"gravity flux", so total (fluid plus gravitational) momentum and energy are
conserved to round-off with periodic boundaries (§2.2–2.3, App. A). Gravity
lives on cell faces as differences of the 7-point Poisson solution. The
momentum source is the cell density times the average of the two face-normal
accelerations; the energy source pairs the Riemann mass flux at each face with
the time-averaged face acceleration (eqs. 57–59). The paper also shows that
the stress-tensor discretization of Athena and Athena++ v19.0 does not give a
curl-free gravity and proposes a corrected tensor equivalent to the source-term
scheme (§2.3.1, §3.3). Merged into
[conservative self-gravity](/methods/conservative-self-gravity.md),
[Athena++](/software/athena-plus-plus.md) and
[Jeans wave](/benchmarks/jeans-wave.md).

# Key claims

1. **Equations** (§2.1, eqs. 1–7). Poisson equation, Euler equations with
   sources $\rho\mathbf g$ and $\rho\mathbf v\cdot\mathbf g$, constraint
   $\nabla\times\mathbf g = 0$. Hydrodynamics only in the tests; §4 says the
   implementation covers "(magneto)hydrodynamics", with no MHD test shown.
2. **Conservative forms** (eqs. 8–12, after Jiang et al. 2013). Momentum:
   $\partial_t(\rho\mathbf v) + \nabla\cdot(\rho\mathbf v\mathbf v + p\mathsf I + \mathsf T_{\mathbf g}) = 0$
   with $\mathsf T_{\mathbf g}$ the gravitational stress tensor (eq. 10).
   Energy: $\partial_t(E + E_{\mathrm g}) + \nabla\cdot[(E+p)\mathbf v + \text{gravitational energy flux}] = 0$,
   $E_{\mathrm g} = \tfrac12\rho\Phi$ (eq. 11). The alternative of Hanawa
   (2019) uses $E_{\mathrm g} = -\vert\mathbf g\vert^2/(8\pi G)$ (eqs. 13–14, 19);
   the two volume integrals differ by a surface term that vanishes for
   periodic boundaries (eq. 20).
3. **Conditions** (§2.2, eqs. 23–24). The source-term scheme is fully
   conservative iff $\rho\mathbf g = -\nabla\cdot\mathsf T_{\mathbf g}$ and the
   corresponding energy identity hold discretely, cell by cell.
4. **Gravity discretization** (§2.3, eqs. 25–30). 7-point Poisson stencil;
   face-normal gravity $g_{x,i+1/2} = -(\Phi_{i+1} - \Phi_i)/h$, so the
   discrete Poisson equation is a discrete divergence of face gravity (eq. 30).
5. **Momentum source** (§2.3.1, eqs. 39–48, App. A). A new discretization of
   $\mathsf T_{\mathbf g}$ (eqs. 39–40; off-diagonal components as before)
   whose discrete divergence reduces exactly, through the discrete circulation
   identity around four-cell-centre loops (eqs. A7–A8, Fig. 9) and the
   discrete Poisson equation, to $\rho_i g_{x,i}$ with
   $g_{x,i} = \tfrac12(g_{x,i+1/2} + g_{x,i-1/2})$. This cell-centred gravity
   is curl-free in the central-difference sense (eqs. 49–51).
6. **The old tensor** (eqs. 35–38). The Athena / Athena++ v19.0 tensor squares
   the four-point average of the tangential face gravity in its diagonal
   components; it is second-order accurate but does not guarantee
   $\nabla\times\mathbf g = 0$. The new tensor averages products of
   neighbouring tangential components and can be negative (§5).
7. **Energy source** (§2.3.2, eqs. 52–59). Writing
   $\rho\mathbf v\cdot\mathbf g = -\nabla\cdot(\rho\mathbf v\Phi) - \Phi\,\partial_t\rho$
   with face potentials and the discrete continuity equation gives
   $(\rho\mathbf v\cdot\mathbf g)_i = \tfrac12[(\rho v_x)_{i+1/2}g_{x,i+1/2} + (\rho v_x)_{i-1/2}g_{x,i-1/2} + (y) + (z)]$
   (eq. 57). Two requirements: the face mass flux must be **the same Riemann
   mass flux** used in the continuity equation (Mikami et al. 2008), and the
   face gravity must be the **time average** of its values at the start and
   end of the step (eqs. 58–59).
8. **VL2 algorithm** (§3.1, eqs. 60–68). Half-step hydro; Poisson solve;
   half-step sources with the time-averaged gravity; full-step hydro; second
   Poisson solve; full-step sources. **Two Poisson solves per step**, as in
   Athena++ v19.0, with the Poisson solve placed after the continuity update
   and before the energy source, the main porting hurdle (§5). Second order;
   any Riemann solver and reconstruction.
9. **RK2 and RK3** (App. B, eqs. B11–B33). The energy source uses the
   "effective mass flux" of the stage combination, e.g. for RK3
   $\tfrac16(\hat f^{\rho,(0)} + \hat f^{\rho,(1)} + 4\hat f^{\rho,(2)})$ times
   the time-averaged gravity (eq. B33); the previous stage's energy
   contribution is removed before the new one is added; mass fluxes of
   previous stages must be stored (§5). The RK3 Poisson-solve count is not
   stated.
10. **Round-off conservation needs a round-off Poisson solution** (§3.2).
    FFT solvers deliver it; multigrid residuals break it. Only the initial and
    final gravity enter the final-stage energy source, so intermediate
    potentials may carry residuals (§6 suggests relaxed tolerances there).
    For momentum, a uniform corrective acceleration (eq. 70) restores
    $\sum\rho\mathbf g = 0$ when the Poisson residual is non-zero.
11. **Anomalous accelerations** (§3.3, eqs. 72–79, Fig. 1). For a body of mass
    $M$ and radius $R$ with an atmosphere of mass $M_a$, the old flux scheme's
    second-order error grows as $1/M_a$ (eq. 78) while the source-term error
    does not (eq. 77). Errors reach the true gravity at
    $(M_a/M)_{\mathrm{critical}} = \tfrac34(R/h)^{-2}$ (eq. 79), about $10^{-2}$
    for $R/h = 10$. The new tensor gives the source-term error.
12. **Order** (§4.2.1, §6). The source-term evaluation limits the scheme to
    second order regardless of integrator or reconstruction; RK3 and PPM lower
    the error constant.
13. **Analogy** (§5). $\nabla\times\mathbf g = 0$ is the gravity counterpart of
    $\nabla\cdot\mathbf B = 0$ under constrained transport.
14. **Limitations** (§6). Not implemented with AMR in Athena++ (deferred to the
    multigrid work of Tomida et al., then in preparation); unlike the Jiang et
    al. (2013) flux scheme, it needs no extra elliptic solve for
    $\partial_t\Phi$ (§5).

**Tests** (§4; Athena++ FFT Poisson solver, HLLC, ideal gas, VL2 + PLM unless
stated; no CFL number printed). Spitzer sheet advected over one crossing,
$N = 16$ to 2048: second order for both conservative variants, total momentum
conserved to order $10^{-15}$ (Fig. 2). Stable
[Jeans wave](/benchmarks/jeans-wave.md) oblique to the grid
(Gardiner & Stone 2008 geometry, $\lambda/\lambda_J = 1/2$, $N = 8$ to 256):
strict second order for all six combinations of VL2, RK2, RK3 with PLM, PPM
(Fig. 3). Unstable Jeans case ($\lambda/\lambda_J = 3/2$): total energy
conserved within $\pm1\times10^{-13}$ while its components vary by factors of
about 20 (Fig. 4). $\gamma = 2$ polytrope with a low-mass atmosphere
($M_a = 10^{-2}M$, $80^3$, $R/h \sim 10$): the old tensor destroys the
atmosphere with an $m = 4$ pattern, the new tensor and the source-term scheme
keep the equilibrium (Figs. 5–6); with white noise of amplitude
$10^{-4}GM/R$ added to $\Phi$, only the source-term scheme shows no spurious
velocities (Fig. 7); a non-conservative energy source heats the polytrope
steadily and its central density drops by about 30% by $t/\tau = 100$, while the
conservative scheme settles (Fig. 8).

# Notation map

| Mullen et al. (2021) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\phi$ | $\Phi$ | |
| $G$, $\mathbf g$, $\rho$, $\mathbf v$, $E$ | $G$, $\mathbf g$, $\rho$, $\mathbf v$, $E$ | |
| $P$, $\mathbf P$ | $p$, $p\mathsf I$ | bold $\mathbf P$ is the isotropic pressure tensor |
| $e$ | $\rho e$ | **collision:** the paper's $e$ is the internal energy density |
| $\Gamma$, $K$ | words | polytropic exponent and constant |
| $\mathbf T_{\mathbf g}$, $\tilde{\mathbf T}_{\mathbf g}$ | $\mathsf T_{\mathbf g}$ | new and old discretizations |
| $E_{\mathrm g}$, $E'_{\mathrm g}$ | $E_{\mathrm g}$ | two forms of the gravitational energy density |
| $\mathbf F_{\mathbf g}$, $\mathbf F'_{\mathbf g}$ | words | gravitational energy flux; distinct from $\mathbf F_{\mathrm r}$ |
| $\mathbf U$, $\mathbf F[\mathbf U]$, $\mathcal F_\rho$, $L[\mathbf U]$ | $u$, $\hat f_{i+1/2}$, $\hat f^{\rho}$, $\mathcal L(u)$ | |
| $\Delta x$; $d$ (§3.3) | $h$ | **collision:** the paper's $d$ is the cell size; registry $d$ is the number of dimensions |
| $\mathrm g_{x,i+1/2,j,k}$ | $g_{x,i+1/2}$ | |
| $A$, $\lambda$, $\lambda_J$, $\omega$, $M$, $R$, $M_a$, $\tau$, $\varphi$ | words | test-local; $A$ collides with $A(u)$, $\tau$ with the Valencia $\tau$ |

# Pages created or updated

* Created [Conservative self-gravity](/methods/conservative-self-gravity.md).
* Updated [Athena++](/software/athena-plus-plus.md),
  [Jeans wave](/benchmarks/jeans-wave.md).
* Also cited on [Athena (astrophysical MHD code)](/software/athena.md).
* Also cited on [Self-gravitating polytrope](/benchmarks/self-gravitating-polytrope.md).

# Citations

1. `~/papers/mosaic/astrophysical-simulation-codes/2021-ApJS-Mullen-1038471538-4365abcfbd.pdf`.
   * **Version.** arXiv:2012.01340v1 (2 Dec 2020), 34 pages, "Submitted to
     ApJS"; the only arXiv version, post-referee (the acknowledgments thank the
     referee) but not the typeset article. Baseline "Athena++ v19.0"; no
     repository, licence, language or version tag of the new implementation is
     printed. No timing or scaling data.
   * **Identity.** doi:10.3847/1538-4365/abcfbd, checked on Crossref (title,
     three authors, volume, issue, article number and year match): Astrophys.
     J. Suppl. Ser. 252(2):30, February 2021.
   * **How it was read.** Text extraction, all sections; equations checked on
     rendered pages 3, 4, 6, 7, 8, 12 and 14. Appendix B taken from the text
     layer; only the final-stage formulas (B19, B33) recorded.
   * **Recorded as printed.** §3.1 says the energy sources are applied in
     "steps (5) and (6)"; per the algorithm they are steps (3) and (6). The
     Fig. 7 caption puts the run with the corrective acceleration top-right,
     the panel labels bottom-right. Eq. 18 places a divergence inside the time
     derivative (valid, unusual bracketing). §1 restricts "two Poisson solves
     per step" to second-order integrators and points to App. B.2, which does
     not state the RK3 count.
   * **Reference list:** 32 entries, all with printed DOIs, no article titles
     (30 articles, 2 books). "Tomida et al., in preparation" is not in the list.
     Spitzer (1942) is printed "Spitzer, Lyman, J." and recorded as
     Spitzer, L., Jr. Turk et al. (2011, ApJS 192:9) is keyed `turk-2011-c`.
