---
type: Source
title: "Zhang et al. (2021) — Linear and nonlinear benchmarks between the CLT code and the M3D-C1 code for the 2/1 resistive tearing mode and the 1/1 resistive kink mode"
description: "Code-to-code benchmark of the explicit finite-difference CLT code against the implicit finite-element M3D-C1 code for the linear and nonlinear 2/1 resistive tearing mode and 1/1 resistive kink in a circular, large-aspect-ratio, zero-beta equilibrium; growth rates agree to about 5–10% and follow the resistive scalings near η^(3/5) and η^(1/3)."
resource: "doi:10.1016/j.cpc.2021.108134"
source_kind: paper
authors: [Zhang W., Jardin S.C., Ma Z.W., Kleiner A., Zhang H.W.]
year: 2021
venue: "Comput. Phys. Commun. 269:108134"
local_file: "/home/stefano/papers/mosaic/fusion-mhd-simulation/2021_Crossref_Computer_Physics_Communications_Zhang_Linear_and_nonlinear_benchmarks_between_the_CLT_code_and_the.pdf"
tags: [mhd, full-mhd, tokamak, tearing, kink, finite-differences, finite-elements, time-integration, gpu, benchmark, verification]
timestamp: 2026-10-16T00:00:00Z
---

# Summary

A short verification paper that benchmarks [CLT](/software/clt.md)
(Zhejiang University: explicit, fourth-order finite differences in
$(R,\phi,Z)$, fourth-order Runge–Kutta, cut-cell boundary treatment,
OpenACC GPU port) against [M3D-C1](/software/m3d-c1.md) (PPPL: implicit
$\theta$-scheme, $C^1$ triangular elements in $(R,Z)$, Hermite cubic
elements in $\phi$). Both codes solve the same single-fluid resistive MHD
system with identical normalizations and dissipation definitions. Two
cases are run on circular, large-aspect-ratio ($R_0/a=10$), $\beta\approx0$
QSOLVER equilibria: an $m/n=2/1$ [resistive tearing mode](/definitions/tearing-mode.md)
($q_0=1.75$, edge $q=2.5$) and an $m/n=1/1$
[resistive kink](/definitions/resistive-internal-kink.md) ($q_0=0.7$, edge
$q=3.6$). In a resistivity scan $\eta=10^{-7}$–$10^{-5}$ (Alfvén units)
the linear growth rates agree to "about 10%" (tearing) and "about 5%"
(kink); the printed fit exponents are $\gamma\propto\eta^{0.601}$ (CLT) and
$\eta^{0.58}$ (M3D-C1) for tearing, close to the Furth–Killeen–Rosenbluth
$3/5$, and $\eta^{0.31}$ / $\eta^{0.30}$ for the kink, close to Coppi's
$1/3$. Nonlinear runs at $\eta=10^{-5}$ give $n=1$ kinetic energies within
about 7% (tearing saturation) and 5% (kink peak), with near-identical
Poincaré plots. The authors attribute the remaining differences to the
initial perturbations and to slightly different equilibria. Beyond two
tables and four energy values, all agreement statements are visual; no
convergence study is reported. The tabulated growth rates do not
reproduce the printed exponents (see Citations).

# Key claims

1. **Same model in both codes** (§2). CLT and M3D-C1 solve the same
   single-fluid resistive MHD system (Eqs. 1.1–1.6), with the definitions
   and normalizations of the dissipation coefficients checked to be equal.
   Stated.
2. **Tearing growth rates** (§3.1, Table 1). Linear 2/1 growth rates differ
   by "about 10% for each case" over $\eta=10^{-5}$–$10^{-7}$; CLT is
   always lower. Shown; the difference is 7–11% for
   $\eta\ge3\times10^{-7}$ and 24% at $\eta=10^{-7}$ (compiler's check).
3. **Tearing scaling** (§3.1, Fig. 4). $\gamma\propto\eta^{0.601}$ (CLT)
   and $\eta^{0.58}$ (M3D-C1), "both close to" $\eta^{3/5}$. Shown as
   printed; a log-log fit of Table 1 gives 0.54 and 0.51 (compiler's
   check).
4. **Tearing mode structure** (Fig. 5). Linear 2/1 structures of the
   toroidal electric field are "very similar". Shown (visual).
5. **Tearing saturation** (Fig. 6). At $\eta=10^{-5}$ the $n=1$ kinetic
   energy saturates at $1.5\times10^{-6}$ (CLT) and $1.4\times10^{-6}$
   (M3D-C1); other harmonics' saturation levels are "very close". Shown.
6. **Harmonic growth history** (Fig. 7). The $n=1$ growth rate is constant
   in the linear phase, decreases slowly in the nonlinear phase and
   vanishes at saturation; in CLT $n=0$ and $n=2$ are beat modes growing at
   twice the $n=1$ rate. Shown.
7. **Saturated island** (Figs. 8–9). Poincaré plots of the saturated 2/1
   island are "almost the same"; saturated mode structures are very
   similar. Shown (visual).
8. **Kink growth rates** (§3.2, Table 2). Linear 1/1 growth rates differ by
   "about 5% for each case". Shown; 2.7–6.3% (compiler's check).
9. **Kink scaling** (§3.2, Fig. 12). $\gamma\propto\eta^{0.31}$ (CLT) and
   $\eta^{0.30}$ (M3D-C1) (legend 0.312, 0.301), close to $\eta^{1/3}$.
   Shown as printed; Table 2 fits give 0.285 and 0.281 (compiler's check).
10. **Kink nonlinear evolution** (Figs. 14–15). Peak $n=1$ kinetic energy
    $4.4\times10^{-5}$ (CLT) and $4.2\times10^{-5}$ (M3D-C1); the energy
    grows, saturates and decreases; the growth rate "suddenly reduces to a
    negative value" (a crash) and its evolution stays qualitatively the
    same after the crash. Shown.
11. **Initial perturbations** (§4). The initial perturbations ($n=1$ only in
    CLT, random in all $n$ in M3D-C1) "hardly influence" the linear growth
    rate and the nonlinear evolution and explain the early differences of
    the harmonics. Stated (argued from Figs. 6, 7, 14, 15; no controlled
    test).
12. **Equilibrium difference** (§4). M3D-C1 re-solves the Grad–Shafranov
    equation on its element basis while CLT interpolates the QSOLVER data;
    this "could be why" the nonlinear evolutions differ. Stated
    (hypothesis).
13. **GPU speed-up** (§2). OpenACC "typically makes the code 200 times
    faster". Attributed (to the earlier CLT paper).
14. **Cut-cell boundary** (§2, Fig. 1). The cut-cell method replaces the
    earlier interpolation-based boundary treatment, which "reduces the
    parallel efficiency". Stated.
15. **Scope** (§4). Large aspect ratio and zero $\beta$ are chosen so that
    results can be checked against analytic scalings; finite $\beta$ and
    $R_0/a\approx3$–4 are left to future work. Stated.

# Models and numerics

**Model** (Eqs. 1.1–1.6, both codes; two-fluid options exist but are not
used):

$$\begin{aligned}
\partial_t\rho &= -\nabla\cdot(\rho\mathbf v)+\nabla\cdot\big[D\nabla(\rho-\rho_0)\big],\\
\partial_t p &= -\mathbf v\cdot\nabla p-\Gamma p\nabla\cdot\mathbf v+\nabla\cdot\big[\kappa_\perp\nabla_\perp(p-p_0)\big]+\nabla\cdot\big[\kappa_\parallel\nabla_\parallel p\big],\\
\partial_t\mathbf v &= -\mathbf v\cdot\nabla\mathbf v+(\mathbf J\times\mathbf B-\nabla p)/\rho+\nabla\cdot(\nu\nabla\mathbf v),\\
\partial_t\mathbf B &= -\nabla\times\mathbf E,\qquad
\mathbf E=-\mathbf v\times\mathbf B+\eta(\mathbf J-\mathbf J_0),\qquad
\mu_0\mathbf J=\nabla\times\mathbf B,
\end{aligned}$$

with $\Gamma=5/3$. A subscript 0 marks the equilibrium: density diffusion,
perpendicular conduction and the resistive term act on deviations from it,
so the equilibrium is not diffused away; parallel conduction acts on the
full $p$. Viscosity is the Laplacian form (no stress tensor). M3D-C1
advances $\mathbf A$; Faraday's law is its curl.

**Normalization.** Length $L_0=1$ m, field 1 T, density $10^{20}$ m⁻³,
$v_A$ from these, $\tau_A=L_0/v_A$; $\eta$ is normalized by
$\mu_0L_0^2/\tau_A$ (an inverse Lundquist number referred to $L_0$, here
equal to $a=1$ m); $D$, $\kappa_\perp$, $\kappa_\parallel$, $\nu$ by
$L_0^2/\tau_A$ (kinematic).

**CLT.** Fourth-order finite differences on a uniform cylindrical grid in
$(R,\phi,Z)$; explicit fourth-order Runge–Kutta, $\Delta t\approx8.5\times10^{-3}\tau_A$.
Cut-cell boundary (Duan et al.): regular points use a 5-point fourth-order
central stencil; first-type irregular points a fourth-order biased stencil
with boundary values; second-type irregular points a central stencil using
boundary and first-type points; points just inside the boundary (distance
below half a cell) are updated by linear interpolation; points outside are
not computed; boundary values are fixed (a free boundary is planned).
OpenACC port. Grids $256\times16\times256$ (tearing) and
$256\times12\times256$ (kink) in $(R,\phi,Z)$, the same for linear and
nonlinear runs. CLT interpolates the QSOLVER equilibrium directly.
Initial perturbation: pure $n=1$.

**M3D-C1.** High-order $C^1$ triangular elements in $(R,Z)$ and Hermite
cubic elements in $\phi$; implicit $\theta$-scheme, $\Delta t=1.0\,\tau_A$.
Linear runs use the 2D complex version (one toroidal harmonic), nonlinear
runs the 3D version. Meshes packed at the resonant surface: 4800 poloidal
elements and 16 planes (tearing, packed at $q=2$); 3816 elements and 12
planes (kink, packed at $q=1$). M3D-C1 re-solves the Grad–Shafranov
equation from the QSOLVER profiles. Initial perturbation: random, all
harmonics. Its boundary conditions are not given.

**Equilibria** (QSOLVER, circular, $R_0/a=10$, $a=1$ m, $\beta\approx0$,
radial label $r=\sqrt{\psi_N}$):

* Tearing (Eq. 1.7): $q=q_0\big[1+(\psi_N/q_l)^{\alpha}\big]^{1/\alpha}$ with
  $q_l=\big[(q_{\mathrm{e}}/q_0)^{\alpha}-1\big]^{-1/\alpha}$, $q_0=1.75$,
  edge value $q_{\mathrm e}=2.5$, $\alpha=2$; one $q=2$ surface at
  $r/a\approx0.7$. The shape symbols $q_l$, $\alpha$, $q_{\mathrm e}$ are
  local to this equation.
* Kink (Eq. 1.8): a rational $q(\psi_N)$ with axis value 0.7, edge value
  3.6, axis slope 2.0 and edge slope 5.0 (slopes in $\psi_N$, inferred);
  $q=1$ at $r/a\approx0.43$. The printed form is in the Notation map.

**Dissipation.** Linear scans: $D=\nu=\kappa_\perp=10^{-8}$,
$\kappa_\parallel=1$, constant $\eta\in[10^{-7},10^{-5}]$. Nonlinear runs:
$\eta=10^{-5}$ (other coefficients not restated).

No costs, timings, convergence study or M3D-C1 boundary-condition details
are given.

# Tests and results

**Table 1 — 2/1 tearing, linear $\gamma$ [$\tau_A^{-1}$]:**

| $\eta$ | $10^{-5}$ | $3\times10^{-6}$ | $10^{-6}$ | $3\times10^{-7}$ | $10^{-7}$ |
|---|---|---|---|---|---|
| M3D-C1 | 0.00178 | 0.00116 | 0.000675 | 0.000330 | 0.000178 |
| CLT | 0.00165 | 0.00104 | 0.000604 | 0.000293 | 0.000135 |
| difference relative to M3D-C1 (compiler's check) | 7.3% | 10.3% | 10.5% | 11.2% | 24.2% |

**Table 2 — 1/1 resistive kink, linear $\gamma$ [$\tau_A^{-1}$]:**

| $\eta$ | $10^{-5}$ | $3\times10^{-6}$ | $10^{-6}$ | $3\times10^{-7}$ | $10^{-7}$ |
|---|---|---|---|---|---|
| M3D-C1 | 0.0115 | 0.00870 | 0.00640 | 0.00440 | 0.00320 |
| CLT | 0.0111 | 0.00837 | 0.00617 | 0.00428 | 0.00300 |
| difference (compiler's check) | 3.5% | 3.8% | 3.6% | 2.7% | 6.3% |

| Exponent of $\gamma\propto\eta^{x}$ | CLT | M3D-C1 | Theory |
|---|---|---|---|
| Tearing, printed (Fig. 4) | 0.601 | 0.58 | 3/5 |
| Tearing, fit of Table 1 (compiler's check) | 0.54 | 0.51 | |
| Kink, printed (Fig. 12) | 0.31 (0.312) | 0.30 (0.301) | 1/3 |
| Kink, fit of Table 2 (compiler's check) | 0.285 | 0.281 | |

**Nonlinear, $\eta=10^{-5}$:**

* Tearing: M3D-C1 curves shifted by 4200 $\tau_A$ for comparison. $n=1$
  saturation $1.5\times10^{-6}$ (CLT) vs $1.4\times10^{-6}$ (M3D-C1) near
  $1.8\times10^4\,\tau_A$; linear-phase $\gamma_{n=1}\approx1.4$–$1.45\times10^{-3}$
  (Fig. 7); in CLT $n=0,2$ grow at ≈$2.9\times10^{-3}$; in M3D-C1 they
  start from noise, decay, then lock to the beat rate.
* Kink: M3D-C1 curves shifted by 270 $\tau_A$. Peak $n=1$ kinetic energy
  $4.4\times10^{-5}$ vs $4.2\times10^{-5}$ near $2400\,\tau_A$; linear
  plateau $\gamma_{n=1}\approx0.011$, $\gamma_{n=0,2}\approx0.021$
  (Fig. 15), then a crash to a negative growth rate.
* CLT growth rates are systematically lower and its energies higher.

# Notation map

| Zhang et al. (2021) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $(R,\varphi,Z)$ | $(R,Z,\phi)$ | orientation of $\varphi$ not stated |
| $\rho$, $\rho_0$ | $\rho$; equilibrium value | |
| $p$, $p_0$; $\mathbf J_0$ | $p$, $\mathbf J$; equilibrium values | |
| $\Gamma$ | $\Gamma$ | 5/3 |
| $D$ | $D$ (isotropic particle diffusivity) | registry lists $D_\parallel,D_\perp$ |
| $\kappa_\perp$, $\kappa_\parallel$ | $\kappa_\perp$, $\kappa_\parallel$ | act on $p$, diffusivity units $L_0^2/\tau_A$ |
| $\nu$ | $\nu$ | kinematic, Laplacian form |
| $t_A$ | $\tau_A$ | length $L_0=1$ m |
| $L_0$, $B_{00}$, $n_0$, $M_i$ | words (normalization length, field, density; $m_i$) | |
| $\psi_n$ | $\psi_N$ | $2\pi$ convention not stated |
| $r=\sqrt{\psi_n}$ | words (radial label) | **collision risk:** registry $r$ is the geometric minor radius |
| $q_0$, $q_e$ | $q_0$; words (edge value of $q$) | |
| Eq. 1.7: $q_l$, $\alpha$ | local shape parameters | |
| Eq. 1.8: $q=q_0+\psi_n[q_e-q_0+(q_e'-q_e+q_0)(1-\psi_s)(\psi_n-1)/(\psi_n-\psi_s)]$, $\psi_s=(q_e'-q_e+q_0)/(q_e'+q_0'-2q_e+2q_0)$ | words | $q_0'$, $q_e'$ undefined in the paper; read as $dq/d\psi_N$ at axis and edge; then $\psi_s=1.75$ (pole outside the plasma) |
| $\gamma$, $\gamma_n$ | $\gamma$ | from the harmonic's kinetic energy; factor ($\tfrac12d\ln E/dt$) not stated |
| $E_k$ | $W_{\mathrm{kin}}^{(n)}$ | normalized units |
| $R/a$ | $R_0/a$ | |
| $h_Z$, $d_Z$ | words (grid spacing, distance to the boundary) | |

# Pages created or updated

Chunk 1 (2026-10-16) created every page of the bundle; chunk 2 (2026-10-16) extended many. This source is cited on:

* [Bézier–Hermite finite elements with toroidal Fourier harmonics](/methods/bezier-finite-elements.md)
* [CLT](/software/clt.md)
* [CLT–M3D-C1 tearing and resistive-kink benchmark](/benchmarks/clt-m3d-c1-benchmark.md)
* [Divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
* [Grad–Shafranov equation](/definitions/grad-shafranov-equation.md)
* [Implicit time integration and preconditioned Krylov solvers for nonlinear MHD](/methods/implicit-time-integration.md)
* [M3D-C1](/software/m3d-c1.md)
* [MARS-F](/software/mars-f.md)
* [Resistive internal kink (m/n = 1/1)](/definitions/resistive-internal-kink.md)
* [Resistive tearing mode](/definitions/tearing-mode.md)
* [Resonant magnetic perturbations and plasma response](/definitions/resonant-magnetic-perturbation.md)
* [Sawtooth crash and Kadomtsev reconnection](/definitions/sawtooth-crash.md)
* [Single-fluid visco-resistive MHD model](/methods/visco-resistive-mhd-model.md)
* [XTOR-K](/software/xtor-k.md)

# Citations

1. `/home/stefano/papers/mosaic/fusion-mhd-simulation/2021_Crossref_Computer_Physics_Communications_Zhang_Linear_and_nonlinear_benchmarks_between_the_CLT_code_and_the.pdf`
   * **Version.** Publisher version of record (Elsevier typeset), 8 pages;
     received 28 February 2020, revised 11 July 2021, accepted 5 August
     2021, online 11 August 2021.
   * **Identity.** doi:10.1016/j.cpc.2021.108134, checked on Crossref:
     title, five authors in printed order, Comput. Phys. Commun. 269,
     article 108134, issue December 2021.
   * **How read.** Full text, both tables and all equations; $\Gamma$ in
     "(= 5/3)", dropped by text extraction, was read on the rendered page.
     Figure values are the reader's approximate readings.
   * **Recorded as printed.**
     * "About 10% for each case" (Table 1 caption, §3.1) does not hold at
       $\eta=10^{-7}$: 0.000178 vs 0.000135 is 24% relative to M3D-C1 (32%
       relative to CLT); the other cases are 7–11% (compiler's check).
     * The printed exponents are not reproducible from the tables:
       least-squares log-log fits over all five points give 0.54 (CLT) and
       0.51 (M3D-C1) for tearing, 0.285 and 0.281 for the kink, against the
       printed 0.601/0.58 and 0.31/0.30. The fit method and range are not
       stated, and the drawn fit lines in Figs. 4 and 12 lie above the data
       at $\eta=10^{-5}$. The stated closeness to $3/5$ and $1/3$ is weaker
       than printed (compiler's check).
     * Fig. 7 shows a linear-phase $\gamma_{n=1}\approx1.4$–$1.45\times10^{-3}$
       at $\eta=10^{-5}$ for both codes, while Table 1 gives 0.00165 (CLT)
       and 0.00178 (M3D-C1) at the same $\eta$; unexplained. For the kink,
       Fig. 15 (≈0.011) is consistent with Table 2.
     * The time shifts of the M3D-C1 curves (4200 and 270 $\tau_A$) are
       arbitrary, so times to saturation are not compared.
     * $q_0'$, $q_e'$ in Eq. 1.8 are undefined.
     * $\mathbf J$ is normalized by $B_{00}/(\mu_0a)$ while everything else
       uses $L_0$ (harmless, $a=L_0=1$ m).
     * CLT's linear growth rates come from full 3D runs with an $n=1$ seed
       ($256\times16\times256$), M3D-C1's from its single-harmonic version.
     * Section 3 calls itself a "subsection"; stray period in "M3D-C1
       [28]. is as follows"; table entries with stray spaces ("0. 00116");
       "We have dense the mesh" (Fig. 11 caption).
   * **Reference list.** 32 printed entries, merged into the bibliography
     under `zhang-2021`. Only ref. [20] prints a title; it has no venue and
     a dangling "DOI" without value (`jardin-2016`). Ref. [23] prints year
     2018 for Nucl. Fusion 59 (`ferraro-2018`). La Haye is printed
     "R.J.L. Haye" in [1] and [4]; group-author artefacts in [1], [2], [7].
     The two Zhang 2019 works are `zhang-2019` (CLT GPU paper, [19]) and
     `zhang-2019-b` ([27]); the VDE benchmark [21] is `krebs-2020`.
