---
type: Source
title: "Panici et al. (2023) — The DESC stellarator code suite. Part 1. Quick and accurate equilibria computations"
description: "Verifies the pseudospectral Fourier–Zernike equilibrium code DESC against VMEC with a common normalized force-balance error: DESC converges exponentially in radial resolution where VMEC converges at first order, is accurate to the magnetic axis, reaches about tenfold lower error at equal runtime on W7-X, and reproduces near-axis Mercier asymptotics where VMEC does not."
resource: "doi:10.1017/S0022377823000272"
source_kind: paper
authors: [Panici D., Conlin R., Dudt D.W., Unalmis K., Kolemen E.]
year: 2023
venue: "J. Plasma Phys. 89:955890303"
local_file: "/home/stefano/papers/mosaic/fusion-mhd-simulation/2023_Crossref_Journal_of_Plasma_Physics_Panici_The_DESC_stellarator_code_suite_Part_1_Quick_and_accurate_eq.pdf"
tags: [equilibrium, stellarator, spectral, verification, numerics]
timestamp: 2026-10-16T23:45:00Z
---

# Summary

The paper compares two fixed-boundary 3D ideal-MHD
[inverse-equilibrium codes](/methods/inverse-equilibrium-solvers.md). [VMEC](/software/vmec.md) minimizes the MHD energy by a damped
second-order (Richardson) iteration on angular Fourier coefficients defined
on discrete flux surfaces, with radial finite differences.
[DESC](/software/desc.md) expands $R$, $Z$ and the poloidal-angle stream
function in a global Fourier–Zernike basis and drives the volume-weighted
force residual $\mathbf J\times\mathbf B-\nabla p$ to zero at collocation nodes with a
Newton-type (Levenberg–Marquardt) solver. Because VMEC does not output the
real-space force error, the authors derive it from VMEC's Fourier
coefficients (Appendix A) and define a common metric: the force-error
magnitude, flux-surface- or volume-averaged, normalized by the
volume-averaged $|\nabla p|$. On an axisymmetric D-shaped case VMEC converges at
first order in radial resolution (fit slope −1.02) and DESC exponentially.
On the W7-X standard configuration at $\beta\approx2\%$ the codes give visually
identical flux surfaces and the same spectral width, but VMEC's Fourier
coefficients violate the near-axis $s^m$ regularity scaling and its force
error grows sharply toward the axis; DESC reaches about one order of
magnitude lower error at equal runtime on the same CPU. On a quasi-helically
symmetric finite-$\beta$ case, DESC's Mercier criterion matches the near-axis
asymptotics of Landreman & Jorge (2020) down to the axis, while VMEC deviates
near the axis even with 801 surfaces, dominated by the geodesic-curvature
term. VMEC also shows force-error spikes near the edge tied to its multigrid
radial continuation. This is a verification paper, not the DESC methods
paper (Dudt & Kolemen 2020); automatic differentiation is deferred to Part 2.

# Key claims

1. **Accuracy** (Abstract; §5.3.2, Fig. 11). DESC "is able to achieve more
   accurate solutions, especially near axis" than VMEC in normalized
   force-balance error. Shown.
2. **Cost–accuracy** (Abstract; §5.3.2, Fig. 12). "DESC can compute a solution
   with the same accuracy as VMEC in order-of-magnitude less time"; at equal
   runtime its error is "generally an order-of-magnitude lower". Log–log fits
   of error against time: slope −0.27 (VMEC), −0.46 (DESC). One AMD EPYC 7281
   CPU, 32 GB. Shown (scan of resolutions and tolerances); the two statements
   are not equivalent (Citations).
3. **VMEC radial convergence is first order** (§5.2, Fig. 7, Table 1):
   D-shape fit slope −1.02 in log error vs log radial points. Shown; the
   attribution to first-order radial finite differences is Stated.
4. **DESC radial convergence is exponential** (§5.2, Fig. 8): error
   $\approx\exp(-0.61L-0.01)$ over radial resolution $L=16$–24 at poloidal
   resolution 16, from about $5\times10^{-5}$ to $4\times10^{-7}$. Shown (five points).
5. **Near-axis regularity** (§3.2, Eq. 3.21; §5.1, Fig. 4). The Zernike basis
   enforces $a_m(s)=s^m(a_{m,0}+a_{m,2}s^2+\dots)$ for the poloidal harmonic $m$ of
   any field (Lewis & Bellan 1990) by construction; VMEC coefficients divided
   by $s^m$ diverge toward the axis, "evidence of possibly unphysical modes".
   Derived/Stated; Shown for VMEC.
6. **Spectral width** (§5.1, Fig. 5). Essentially the same for both codes;
   DESC finds an optimal stream function without imposing the
   Hirshman–Breslau constraint. Shown.
7. **Force versus energy objective** (§3.2). The force residual is "faster (by
   a factor of two in some cases)" and converges better "in extensive
   testing". Stated, no data.
8. **Threshold** (§5.4, Figs. 7–8). By analogy with the $10^{-4}$ Picard-iteration
   threshold accepted for EFIT equilibria in tokamak stability analysis, the
   D-shaped DESC equilibrium meets $10^{-4}$ normalized error and VMEC does not
   even at high radial resolution. Numbers Shown; the transfer of the
   threshold is Stated.
9. **Mercier verification** (§5.4, Fig. 15). DESC (radial resolution 12)
   agrees with near-axis asymptotics across the volume; VMEC with 65 and 801
   surfaces deviates near the axis and "requires high radial resolution to
   agree with the asymptotic expression inside of $\rho<0.5$, and even then
   differs … nearer to the magnetic axis". Shown.
10. **Geodesic term** (§5.4, Figs. 15–16). The VMEC near-axis Mercier
    discrepancy is dominated by the geodesic-curvature term, which needs
    higher radial derivatives through $\mathbf J$; its onset is "roughly
    correlated" with the radius where VMEC's force error rises. Correlation
    Shown; the explanation Stated as "one possible explanation".
11. **VMEC edge spikes** (§4.1, Figs. 2–3; App. B, Figs. 17–20). Located at the
    radial nodes of the 32-surface grid of the multigrid sequence (16, …,
    1024), not at low-order rational surfaces; not removed by a tighter force
    tolerance or higher angular resolution. Shown; cause ("convergence issues
    with the highly shaped equilibrium") speculative.
12. **Stagnation** (App. C, Figs. 20–22). VMEC error stops decreasing
    appreciably beyond 1024 surfaces (edge spikes grow at 2048) and in angular
    resolution at 20; DESC stops decreasing uniformly around resolution 16.
    Shown.
13. **JIT overhead** (§5.3.2, Fig. 12). DESC runtimes never fall below about 2
    min because of JAX just-in-time compilation. Shown; cause Stated.
14. **Metric sensitivity** (§4, §4.1, Fig. 2). The radial-derivative method
    used for the VMEC force error (2nd/4th-order differences, cubic/quintic
    splines) matters only near the axis; VMEC volume averages exclude
    $\psi_{t,N}<0.1$ and $>0.99$, which "could make the VMEC calculations appear to
    have lower error". Shown and Stated.
15. **Stability codes** (§5.4). VMEC's near-axis inaccuracy "has been found to
    cause issues when conducting ideal MHD stability analyses near the axis".
    Stated (A.H. Glasser, personal communication 2021).

# Models and numerics

**Problem** (§1). Ideal MHD equilibrium $\mathbf J\times\mathbf B=\nabla p$,
$\mu_0\mathbf J=\nabla\times\mathbf B$, $\nabla\cdot\mathbf B=0$, as the force residual
$\mathbf J\times\mathbf B-\nabla p=\mathbf 0$ or as a stationary point of
$\int_V\big(B^2/2\mu_0+p/(\Gamma-1)\big)\,\mathrm dV$. Both codes assume nested flux
surfaces and $p$ a flux function; neither represents islands. Fixed-boundary
inputs: $p$, either $\iota$ or the net toroidal current, and the boundary
shape $R_b(\theta,\phi)$, $Z_b(\theta,\phi)$.

**Common representation.** Inverse coordinates: $R$, $Z$ as functions of a
radial label, a poloidal angle $\theta=\theta^*-\lambda_{\mathrm s}$ (with $\theta^*$
straight-field-line and $\lambda_{\mathrm s}$ the periodic stream function, page-local
symbol) and the geometric toroidal angle $\phi$ over one field period. The
field is
$\mathbf B=\nabla\psi_t\times\nabla\theta^*+\nabla\phi\times\nabla\psi$ with contravariant components
$B^\theta=(\mathrm d\psi/\mathrm dr-\mathrm d\psi_t/\mathrm dr\,\partial_\phi\lambda_{\mathrm s})/\sqrt g$ and
$B^\phi=\mathrm d\psi_t/\mathrm dr\,(1+\partial_\theta\lambda_{\mathrm s})/\sqrt g$ in terms of the radial label $r$
of each code, $\iota=\mathrm d\psi/\mathrm d\psi_t$. The force decomposes into a radial
component $\sqrt g(J^\phi B^\theta-J^\theta B^\phi)+p'$ and a helical component
$\propto J^r$ along $B^\phi\nabla\theta-B^\theta\nabla\phi$ (Eqs. 3.9–3.11, 3.25–3.27). Stellarator
symmetry drops half the Fourier coefficients.

**VMEC** (§3.1). Radial label $\psi_{t,N}$; Fourier series in $(\theta,\phi)$ on
discrete surfaces; first-order radial finite differences; $\lambda_{\mathrm s}$ on the
radial half-mesh. Energy descent replaced by
$\partial_t^2X+\tau^{-1}\partial_tX=(\text{force harmonic})$ with damping time on the
least-damped mode (Eq. 3.15). Spectral width
$\sum m^{p+q}(R_{mn}^2+Z_{mn}^2)/\sum m^p(R_{mn}^2+Z_{mn}^2)$ minimized through $\lambda_{\mathrm s}$
(Hirshman–Breslau). Control: force tolerance FTOL; multigrid radial
continuation over an increasing sequence of surface counts.

**DESC** (§3.2). Radial label $s=\sqrt{\psi_{t,N}}$ (proportional to an
effective minor radius); $R$, $Z$, $\lambda_{\mathrm s}$ expanded in Zernike polynomials
in $(s,\theta)$ times Fourier series in $N_{\mathrm{fp}}\phi$ (Eqs. 3.17–3.20), radial
resolution $L$, ANSI or Fringe indexing. Computational poloidal angle
VMEC-like, unlike Dudt & Kolemen (2020) who used $\theta^*$. The residual
components are weighted by $|\nabla s|$ or the helical-direction norm, $\sqrt g$
and the cell volume (Eq. 3.28) and set to zero at collocation nodes; the
nonlinear system in the spectral coefficients is solved with SciPy
Newton-type methods (Levenberg–Marquardt), quadratically convergent near the
solution. Python + JAX JIT; CPU runs; MPI, GPU and pre-compilation listed as
future work.

**Force-error metric** (§4, App. A). VMEC's force is reconstructed from its
output harmonics (Eqs. A2–A18), with norm
$\sqrt{F_r^2g^{rr}+F_{\mathrm h}^2|\boldsymbol\beta_{\mathrm h}|^2}$ (radial and helical components,
page-local). Volume average over $0.1\le\psi_{t,N}\le0.99$ for VMEC and the full
volume for DESC; flux-surface average analogously; normalized by
$\langle|\nabla p|\rangle$ over the whole volume.

**Mercier criterion** (§5.4, Eqs. 5.7–5.10, Bauer, Betancourt & Garabedian
1984): $D_{\mathrm{Merc}}=D_{\mathrm{Shear}}+D_{\mathrm{Curr}}+D_{\mathrm{Well}}+D_{\mathrm{Geod}}>0$ for
stability, with shear, current, well and geodesic-curvature terms as flux-
surface integrals; compared with the Landreman & Jorge (2020) leading-order
near-axis expressions for the well and geodesic terms of a quasi-symmetric
equilibrium.

**Resolution and cost.** D-shape: poloidal resolution 16, VMEC up to 1024
surfaces, DESC $L=16$–24. W7-X: VMEC angular 8–20, up to 256, 512 or 1024
surfaces, FTOL $10^{-4}$, $10^{-8}$, $10^{-12}$; DESC angular 8–18 with $L$ equal to
it (Table 2). Runtimes about 3 s to $10^5$ s (VMEC) and $3\times10^2$ to
$3\times10^4$ s (DESC), plot readings; VMEC with FTOL below $10^{-14}$ took more
than 24 h. Quasi-helical case: VMEC 65 and 801 surfaces; DESC $L=12$, ANSI,
poloidal 12, toroidal 10.

# Tests and results

| Case | Inputs | Result |
|---|---|---|
| D-shaped tokamak, about 3% $\beta$ (§5.2) | $p=1600-3200s^2+1600s^4$ Pa; $\iota=1-0.67s^2$; $R_b=3.51-\cos\theta+0.106\cos2\theta$, $Z_b=1.47\sin\theta+0.16\sin2\theta$; boundary $\psi_t=1$ Wb (total toroidal flux $2\pi$ Wb) | VMEC error ≈1.6 at the coarsest grid → ≈0.03 at 1024 surfaces, slope −1.02; DESC $5\times10^{-5}$ → $4\times10^{-7}$, exponential; flux surfaces agree (Fig. 9) |
| W7-X standard, $\beta\approx2\%$ (§4, §5.3) | quartic $p(s)$ (central 185.6 kPa), 8th-order $\iota(s)$ from 0.856; boundary harmonics to 12 | flux surfaces agree (Fig. 10); VMEC (1024 surfaces, angular 12–20) ≈ $5\times10^{-2}$–$10^{-1}$ at mid-radius, ≈$10^2$ at the axis; DESC ≈ $10^{-2}$, $3\times10^{-4}$, $10^{-4}$ at resolutions 12, 16, 20, flat to the axis (Fig. 11) |
| Near-axis Fourier scaling (Fig. 4) | W7-X | VMEC $R_{mn}/s^m$ up to ≈$10^{10}$ toward the axis for high $\lvert m\rvert+\lvert n\rvert$; DESC flat |
| Quasi-helical, aspect ratio ≈20 (§5.4) | $p=5000-5000s^2$ Pa, zero net current, $\iota\approx-1.14$ | Mercier-unstable; $-D_{\mathrm{Merc}}$ ≈ $10^3$ near $s=0.1$ to ≈10 at the edge; DESC overlaps theory; VMEC diverges inside $s\approx0.6$ (65 surfaces) and $s\approx0.25$ (801); force error DESC ≈$10^{-3}$, VMEC (801) ≈ $4\times10^{-2}$ mid-radius rising to ≈5 near $s=0.1$ (Fig. 16) |

Values are approximate readings from the figures unless printed. Table 1
lists the expected convergence: angular exponential for both, radial
exponential for DESC and $O(N_{\mathrm{radial}}^{-1})$ for VMEC.

# Notation map

| Panici et al. (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\boldsymbol B$, $\boldsymbol J$, $p$, $\mu_0$ | $\mathbf B$, $\mathbf J$, $p$, $\mu_0$ | SI |
| $\boldsymbol F=\boldsymbol J\times\boldsymbol B-\nabla p$ | words (force residual) | **collision:** registry $F=RB_\phi$; sign reversed in Eq. A8a |
| $W$, $\gamma$, $V$ | words, $\Gamma$, words | **collision:** registry $\gamma$ is a growth rate |
| $(R,\phi,Z)$ | $(R,Z,\phi)$ | orientation not stated |
| $\psi$ (toroidal flux $/2\pi$), $\psi_a$ | $\psi_t$, its boundary value | **collision:** registry $\psi$ is the poloidal flux per radian |
| $\chi$ (poloidal flux $/2\pi$) | $\psi$ | **collision:** registry $\chi$ is the vacuum scalar potential |
| $s=\psi/\psi_a$ (VMEC) | $\psi_{t,N}$ | **collision:** registry $s$ is a square-root label |
| $\rho=\sqrt{\psi/\psi_a}$ (DESC) | $s=\sqrt{\psi_{t,N}}$ | **collision:** registry $\rho$ is mass density |
| $u$, $\theta$ | $\theta$ (VMEC-like, not straight-field-line) | **collision:** registry $u$ is the stream function |
| $v$, $\zeta$ $(=\phi)$ | $\phi$ | here the toroidal angle equals the geometric one |
| $\theta^*$ | $\theta^*$ | straight-field-line angle (§9) |
| $\lambda$ | $\lambda_{\mathrm s}$ (page-local) | **collision:** registry $\lambda_{\mathrm o}$ is an ordering parameter |
| $\iota=\chi'/\psi'$ | $\iota=\mathrm d\psi/\mathrm d\psi_t$ | QH case $\iota<0$ |
| $N_{FP}$ | $N_{\mathrm{fp}}$ | |
| $M$, $N$, $L$; $ns$, $NS$ | words (poloidal, toroidal, radial resolution; surface count) | native $N$ also radial resolution (Figs. 7–8) and helicity (Eq. 5.10, registry $N$ of §9) |
| $X_{mn,c}$, $X_{mn,s}$, $R_{lmn}$, $Z_{lmn}$, $\lambda_{lmn}$ | words (spectral coefficients) | |
| $\mathcal Z_l^m$, $\mathcal R_l^{\lvert m\rvert}$, $\mathcal F^n$ | words (Zernike polynomial, its radial part, toroidal Fourier function) | needed registry extension if concept pages write the basis |
| $M(p,q)$ | words (spectral width) | |
| $\sqrt g$, $g^{ij}$, $B^i$, $J^i$ | same | |
| $F_s$, $F_\rho$, $F_\beta$, $\boldsymbol\beta$ | $F_r$, $F_{\mathrm h}$, $\boldsymbol\beta_{\mathrm h}$ (page-local) | **collision:** native $\boldsymbol\beta$ is a direction, not plasma beta |
| $\tau$, FTOL | words | |
| $D_{\mathrm{Merc}}$ and its four terms | same names | |
| $I(\psi)$, $G(\psi)$, $\vartheta$, $\varphi$ | $I$, $G$ (Boozer covariant components, §9); words (Boozer angles) | |
| $G_0$, $B_0$, $p_2$, $\iota_0$, $\bar\eta$, $\sigma$, $\kappa$ | words (near-axis expansion quantities) | **collision:** native $\bar\eta$ vs resistivity, $\kappa$ (axis curvature) vs conductivity |

# Pages created or updated

Chunk 1 (2026-10-16) created every page of the bundle; chunks 2 and 3 (2026-10-16) extended many. This source is cited on:

* [DESC](/software/desc.md)
* [Divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
* [HINT](/software/hint.md)
* [Interchange modes and the Mercier criterion](/definitions/interchange-mode.md)
* [Quasi-symmetry](/definitions/quasi-symmetry.md)
* [Three-dimensional inverse equilibrium solvers](/methods/inverse-equilibrium-solvers.md)
* [VMEC](/software/vmec.md)

# Citations

1. `/home/stefano/papers/mosaic/fusion-mhd-simulation/2023_Crossref_Journal_of_Plasma_Physics_Panici_The_DESC_stellarator_code_suite_Part_1_Quick_and_accurate_eq.pdf`
   * **Version.** Publisher version of record (Cambridge University Press,
     open access CC-BY 4.0), 32 pages; received 31 October 2022, revised 16
     March 2023, accepted 17 March 2023, online 18 May 2023.
   * **Identity.** doi:10.1017/S0022377823000272, checked on Crossref: J. Plasma
     Phys. 89(3):955890303, issued 2023, five authors in the printed order.
     Data and scripts: Zenodo doi:10.5281/zenodo.6539680.
   * **How read.** Full text including Appendices A–C; plot values are
     approximate readings.
   * **Recorded as printed.**
     * Eq. 3.17 writes $\mathcal Z_l^m$, the definition (3.18) $\mathcal Z_m^l$.
     * Eqs. 3.4 and 3.22 write the first term of $\mathbf B$ with $\nabla s$ or $\nabla\rho$, the
       dimensionless label, while Eq. A9a uses $\nabla\psi$ and Eqs. 3.8, 3.24 carry
       $\psi'$; consistent only if read as $\nabla\psi$.
     * Force sign: Eq. 1.2 $\mathbf J\times\mathbf B-\nabla p$, Eq. A8a $-\mathbf J\times\mathbf B+\nabla p$.
     * $F_\beta$ differs by $\sqrt g$ between the codes (3.10b vs 3.26b),
       compensated in the helical direction vectors (3.11 vs 3.27).
     * Eqs. 4.1–4.3 integrate over "$\theta$, $\phi$" while VMEC's coordinates are
       $(u,v)$.
     * "Levenberg–Marquadt" (§3.2); $s_G$ in Eq. 5.8b, $s_g$ in the text; $\iota$
       printed as iota-bar only in Eq. 5.2.
     * Native $N$ is toroidal resolution, radial resolution (Figs. 7–8 legends)
       and a helicity integer (Eq. 5.10).
     * Quasi-helical resolutions disagree: text and Fig. 15 caption (both codes
       $M=12$, $N=10$), Fig. 13 caption (DESC $L=M=12$, $N=12$), Fig. 14 caption
       (VMEC $M=N=10$).
     * Fig. 17 title "m=1 n=3" against caption and App. B text "$m=3$, $n=1$".
     * App. B attaches the rational-surface sentence to Fig. 18 while §4.1 plots
       rationals in Fig. 3.
     * App. B/C and Fig. 23 write "increasing the FTOL parameter past
       $10^{-14}$" and "low FTOL … terminates the solver prematurely" where
       tightening and too-loose tolerances are meant.
     * App. A prints a first-order forward difference for $\partial R_{mnc}/\partial s$
       while the figure captions state second-order differences.
     * The VMEC volume average excludes $s<0.1$ and $s>0.99$ while DESC's covers
       the full volume, a bias in VMEC's favour acknowledged by the authors.
     * Fig. 11 shows DESC at resolution 20 while Table 2 lists DESC up to 18.
     * Figs. 4–5 write $\rho\sim\sqrt{\psi/\psi_b}$, the text $\psi_a$; Figs. 15–16 use
       $\rho\sim\sqrt{\psi_N}$.
     * Abstract "same accuracy … in order-of-magnitude less time" and Fig. 12
       "order-of-magnitude lower error at equal time" are different
       statements; with fitted slopes −0.27 and −0.46 the equal-accuracy time
       ratio depends on the error level and is not reported.
     * GVEC is cited to Bañón Navarro et al. 2020 (gyrokinetic ITG) and Hudson
       et al. 2020 (SPEC free boundary), neither a GVEC description;
       Rosenbluth, Dagazian & Rutherford 1973 is cited for the scarcity of
       analytic 3D equilibria.
     * "both codes were ran" (§4).
   * **Reference list.** 53 printed references (Crossref 53), merged into the
     bibliography under `panici-2023` (53 entries). DOIs printed only for Dudt
     et al. 2023 (Part 3) and Panici 2022 (Zenodo), entered for those only. The
     DESC methods paper is `dudt-2020`; the GitHub repository, printed with
     second author "Conlin, W.", is `dudt-2022`; Part 2 (printed "Submitted.
     arXiv:2203.15927") is `conlin-2023`; Part 3 is `dudt-2023`. Glasser 2016
     article number printed "72505"; Lao et al. 1985 second author printed
     "John, H.S." (St. John); the JAX entry `bradbury-2018` is labelled version
     0.3.13, which postdates 2018.
