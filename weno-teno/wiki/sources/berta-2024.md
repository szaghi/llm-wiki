---
type: Source
title: "Berta et al. (2024) — A 4th-order accurate finite volume method for ideal classical and special relativistic MHD based on pointwise reconstructions"
description: "Fourth-order constrained-transport finite-volume scheme for classical and relativistic MHD in PLUTO that reconstructs interface values from point values with pointwise WENO-Z, MP5 and WENO3, converts fluxes with Laplacian corrections, and reduces order near discontinuities with a new derivatives-ratio detector."
resource: "doi:10.1016/j.jcp.2023.112701"
source_kind: paper
authors: [Berta V., Mignone A., Bugli M., Mattia G.]
year: 2024
venue: "J. Comput. Phys. 499:112701"
local_file: "/home/stefano/papers/mosaic/weno-teno/2024_Crossref_Journal_of_Computational_Physics_Berta_A_4th-order_accurate_finite_volume_method_for_ideal_classica.pdf"
tags: [mhd, relativistic, finite-volume, weno, troubled-cell, reconstruction]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

The paper builds a fourth-order finite-volume scheme for ideal classical MHD
and [special relativistic MHD](/definitions/relativistic-hydrodynamics.md) on
Cartesian grids, with constrained transport for the
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md),
implemented in the PLUTO code. It follows the McCorquodale–Colella and
Felker–Stone fourth-order framework: point values and cell, face and edge
averages are converted into one another with Laplacian corrections,
$u_c=\bar u_c-\Delta\bar u_c/24+O(\Delta x^4)$. Its departure is that the
one-dimensional reconstruction acts on **point values**. The cell averages are
first turned into point values at cell centres and converted pointwise to
primitive variables. Finite-difference-style interpolations then give the
interface states directly: a pointwise
[MP5](/methods/monotonicity-preserving-limiter.md), a pointwise
[WENO-Z](/methods/weno-z.md) with linear weights $\{1/16,5/8,5/16\}$ and
Jiang–Shu indicators ([WENO-JS](/methods/weno-js-reconstruction.md)), and a
pointwise WENO3 with $d_0=3/4$, $d_1=1/4$. The reconstruction runs in primitive
or [characteristic](/methods/characteristic-decomposition.md) variables, with
one Riemann problem ([Roe](/methods/roe-riemann-solver.md),
[HLL, HLLC, HLLD](/methods/hll-riemann-solvers.md), GFORCE) per interface. Edge
electric fields come from upwind constrained transport (UCT), with a new
relativistic UCT-GFORCE. Time stepping is five-stage
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md) of order 4.

Robustness comes from an a priori order reduction (the "fallback"). A cell flag
switches off the Laplacian corrections and lowers the reconstruction to WENO3
or piecewise linear. The flag is set by a Jameson-type second-difference sensor
or by a new derivatives-ratio detector built on undivided third and fourth
differences ([troubled-cell indicators](/definitions/troubled-cell-indicator.md)).
The tests are a 3D rotated shock tube, MHD and relativistic
[magnetized vortices](/benchmarks/magnetized-vortex.md),
[circularly polarized Alfvén waves](/benchmarks/circularly-polarized-alfven-wave.md),
[field-loop advection](/benchmarks/field-loop-advection.md), a current sheet,
the [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md), 3D
[blast waves](/benchmarks/mhd-blast-wave.md) and a 3D
[shock–cloud interaction](/benchmarks/mhd-shock-cloud-interaction.md). Observed
$L_1$ orders are near 4. The [numerical dissipation](/definitions/numerical-dissipation.md)
measured by Alfvén-wave damping scales as $N_x^{-5}$, against $N_x^{-3}$ at
second order. A cost model predicts that a second-order $512^3$ run is matched
by about $34^3$ zones at fourth order. Nothing is proved beyond the Taylor
derivation of the conversions.

# Version read

arXiv 2310.11831v4 [astro-ph.HE], 18 Dec 2023, footer "Preprint submitted to
Journal of Computational Physics, December 20, 2023": not the typeset version
of record. It prints no DOI; the published identity is from Crossref. It has
30 pages: main text pp. 1–25, Appendices A–B pp. 26–27, references pp. 28–30.
Title and authors match page 1. Equation, table and figure numbers are those
of the arXiv v4.

# Key claims

Registry notation: $\bar u_c$ and $u_c$ are the cell average and the point
value at the centre of cell $c$, $V$ the primitive variables, $d_k$, $\beta_k$,
$\alpha_k$, $\omega_k$ the WENO linear weights, indicators and weights, $\gamma$
the ratio of specific heats and $W$ the Lorentz factor (see the notation map).

1. The scheme is presented as the first finite-volume scheme to use pointwise versions of the MP5 and WENO-Z reconstructions, "traditionally used in FD schemes" ("to the extent of our knowledge", §1, §3.2). **Stated**
2. Pointwise reconstruction keeps fourth-order accuracy "with fewer operations per step and without even enlarging the stencil size", with one Riemann problem per interface; the Gauss-point approach of Núñez-de la Rosa & Munz and Titarev & Toro needs one per quadrature point, "e.g. 4 in the case of a three-dimensional domain when using 2 Gaussian points" (§1, §3.2). **Stated**
3. Unlike Felker & Stone, the scheme does not convert $\bar u_c$ to $V(\bar u_c)$ and then to an averaged $\bar V_c$ before reconstructing, and it does not solve a Riemann problem with interface-averaged primitive states (§3.2, §3.3). **Stated**
4. The conversions $u_c=\bar u_c-\Delta\bar u_c/24+O(\Delta x^4)$ and $\bar u_c=u_c+\Delta u_c/24+O(\Delta x^4)$, with $\Delta$ the undivided Laplacian, follow in 1D from Taylor expansion and Simpson-like quadrature and extend to Cartesian multi-D by orthogonality (Eqs. 16–19, App. A). **Derived**
5. The pointwise WENO-Z has linear weights $d_0=1/16$, $d_1=5/8$, $d_2=5/16$, which reproduce the five-point point-value interpolation $\frac1{128}(3V_{i-2}-20V_{i-1}+90V_i+60V_{i+1}-5V_{i+2})$ of Eq. (23); the smoothness indicators "have been found to be the same as in Borges", i.e. the Jiang–Shu form on point values, with $\alpha_k=d_k\big(1+\tau_5/(\beta_k+\epsilon)\big)$, $\tau_5=\lvert\beta_0-\beta_2\rvert$ (§3.2, Eqs. 23–26). **Derived** (the five coefficients follow from the three candidate interpolations with these $d_k$ *(compiler check, not in the sources)*)
6. The pointwise WENO3 has $d_0=3/4$, $d_1=1/4$, against $2/3$, $1/3$ in the finite-volume formulation from cell averages, and uses $\epsilon=\Delta x^2$ to avoid loss of accuracy at critical points (§3.2, Eqs. 27–28). **Stated**
7. The WENO-Z regularization is $\epsilon=10^{-40}$ (§3.2). **Stated**
8. The MP5 limiter is unchanged in the pointwise version, "as monotonicity-preserving bounds are equally well expressed in terms of point values" (§3.2). **Stated**
9. The five-stage SSP Runge–Kutta method of order 4 is strongly stable under the forward-Euler restriction, with $\Delta t=\nu\min_{ijk}\big[\min_d(\Delta x^{(d)}/a^{(d)})\big]$, $a^{(d)}$ the outermost fast magnetosonic speed in direction $d$ (§3.3, Eqs. 31–32). **Stated**
10. Near discontinuities the point-value recovery "may easily produce unphysical values such as negative energies or densities"; a flag $\theta_c=0$ removes the Laplacian correction and the flux integration and lowers the reconstruction to WENO3 or piecewise linear (§3.4, Eqs. 33–34). **Stated**
11. The Jameson-type sensor keeps the stencil compact, "albeit three zones may not be sufficient to distinguish a discontinuity from a smooth extremum"; the derivatives-ratio detector needs one extra ghost zone; using primitive variables in the detector "has shown to yield a more robust identification method" (§3.4). **Stated**
12. With point-value reconstruction the electric field is evaluated over 3 layers of transverse ghost zones rather than 4 (§4). **Stated**
13. Appendix B corrects typos of Mignone & Del Zanna (2021): their Eq. 51 "contains 'y' instead of 't'" in the GFORCE transverse velocity (App. B, Eq. B.3). **Stated**
14. 3D rotated shock tubes ($768\times8\times8$; MHD with WENO-Z in characteristic variables, relativistic MHD with MP5 in primitive variables) reproduce the reference profiles; oscillations in the normal field are of the same order as in Mignone's finite-difference scheme and smaller than in an earlier code (§5.1, Figs. 2–3). **Shown**
15. 2D MHD iso-density vortex and new relativistic iso-enthalpy vortex: observed $L_1$ orders of $B_x$ between 3.91 and 4.84 for $N_x=32$–$512$; finest errors 5.76E-09 (MHD) and 1.05E-09 (relativistic) (Table 1). **Shown**
16. Against the fifth-order finite-difference scheme of Mignone, the errors are "very similar" for $N_x\lesssim128$ but the finite-difference scheme converges faster; with RK3 it needs $\Delta t\sim\Delta x^{5/3}$ to keep fifth order (§5.2). **Shown** (against published numbers)
17. Circularly polarized Alfvén waves (2D and 3D, MHD and relativistic; CFL 0.4 in 2D, 0.3 in 3D): $O_{L_1}\to4.00$ at $N_x=512$ in every configuration, with almost identical WENO-Z and MP5 errors (Table 2, Fig. 5). **Shown**
18. In 3D MHD the finite-volume scheme has smaller errors than the fifth-order finite-difference scheme below $256^3$; at $256^3$, $\varepsilon_1(B_y)\sim3.74\cdot10^{-9}$ (finite difference) against $\sim2.91\cdot10^{-9}$ (§5.3). **Shown**
19. With cost $T=\tau N^{d+1}$ and error $\varepsilon=CN^{-p}$, equal errors give $N_4\sim(C_4/C_2)^{1/4}\sqrt{N_2}$ and $T_4/T_2=(C_4/C_2)^{(d+1)/4}(\tau_4/\tau_2)/\sqrt{N_2^{d+1}}$. Measured $\tau_4/\tau_2\sim\{4.3,3.7\}$ and $C_4/C_2\sim\{5.0,8.7\}$ (MHD, relativistic) give $T_4/T_2\sim K/N_2^2$ with $K\sim\{21,32\}$ in 3D; a $512^3$ second-order MHD run is matched by $N_4\sim34$ with a time reduction of $\sim1.2\times10^4$ (§5.3, Eqs. 50–52). **Derived** (with measured constants; $5^{1/4}\sqrt{512}=33.8$, $4.3\times5.0=21.5$, $3.7\times8.7=32.2$, $512^2/21.5\approx1.2\times10^4$ *(compiler check, not in the sources)*)
20. The numerical dissipation measured by the Alfvén-wave decay rate is more than an order of magnitude below the second-order scheme already at $N\sim8$, and scales as $\sim N^{-5}$ at fourth order and $\sim N^{-3}$ at second order (§5.3, Fig. 5; §6). **Shown**
21. Field-loop advection ($256\times128$, two periods): smearing decreases from second to fourth order and WENO-Z "performs the best"; MP5 shows small overshoots (undershoots) at the loop tail (head); magnetic energy decays fastest at second order; the Riemann solver matters only marginally, GFORCE doing better (§5.4, Figs. 6–7). **Shown**
22. The 2D current sheet ($600\times600$, $t=10$) runs with WENO-Z falling back to WENO3 under order reduction (§5.5, Fig. 8). **Shown**
23. Orszag–Tang vortex: at 64 points the fourth-order MP5+HLLD run resolves a central magnetic island; the normalized pressure maximum gives an average effective-resolution gain of $\sim2.23$ over the second-order scheme and an average speedup of $\sim2.58$ (§5.6, Figs. 9–10). **Shown** ($2.23^3/4.3=2.58$ *(compiler check, not in the sources)*)
24. In the 3D blast wave, case C1 "has the largest magnetization our scheme can afford without" the second-order energy-correction step, which C2 and R1 need; the fallback "played an essential role" (§5.7, Table 3, Figs. 11–13). **Shown**
25. In the 3D shock–cloud interaction, order reduction "extended to the selective fluxes integration has been fundamental for the correct evolution of the simulations" (§5.8, Fig. 14). **Shown**
26. Against DG, the scheme evolves fewer equations ("8 instead of 32 for a 4th-order method"), "does not reduce stability with increasing order" and suits mixed smooth and discontinuous flows better, at the price of more inter-processor communication, "one per Runge-Kutta stage" (§6). **Stated**
27. The new relativistic UCT-GFORCE "has been widely validated in the presented benchmarks" (§6). **Shown** (by the relativistic tests)

# Printed slips

- Eq. (27), WENO3 second candidate printed $\frac{-V_{i+1}+3V_i}{2}$. With $d_0=3/4$, $d_1=1/4$ the combination is then $\frac68V_i+\frac28V_{i+1}$, with no $V_{i-1}$. The third-order point-value interpolation at $x_{i+1/2}$, $\frac18(-V_{i-1}+6V_i+3V_{i+1})$, is reproduced by these weights only with the candidate $\frac{-V_{i-1}+3V_i}{2}$ *(compiler check, not in the sources)*.
- Eq. (28) prints $\beta_0=\Delta^2_{i-1/2}$, $\beta_1=\Delta^2_{i+1/2}$ with $\Delta_{i+1/2}=V_{i+1}-V_i$. In Eq. (27), $\omega_0$ multiplies the stencil $\{i,i+1\}$, whose jump is $\Delta_{i+1/2}$, and $\omega_1$ the stencil through $i-1$ (after the previous correction), whose jump is $\Delta_{i-1/2}$. The indicator labels are swapped relative to the stencils *(compiler check, not in the sources)*.
- Eq. (37) prints $\delta^{(3)}\langle Q\rangle_c=\frac12\big(\langle Q\rangle_{i+2\hat e_x}-2(\langle Q\rangle_{c+\hat e_x}-2\langle Q\rangle_{c-\hat e_x})-\langle Q\rangle_{c-2\hat e_x}\big)$, which expands to $\frac12(Q_{+2}-2Q_{+1}+4Q_{-1}-Q_{-2})$. Its coefficients sum to 1, so it does not annihilate constants and is not a third-difference approximation; the consistent form is $\frac12\big(Q_{+2}-2(Q_{+1}-Q_{-1})-Q_{-2}\big)$ *(compiler check, not in the sources)*. The subscript "$i+2\hat e_x$" should read "$c+2\hat e_x$".
- Eqs. (29)–(30) write the $y$ and $z$ point fluxes as $F_{y,x_f}$ and $F_{z,x_f}$, against the arguments $V_{y_f}$, $V_{z_f}$ and the left sides $\hat F_{y,y_f}$, $\hat F_{z,z_f}$.
- §5.1: "$t_f=t'_f\cos\alpha\cos\gamma=4/\sqrt{21}$ where $t'_f=0.2$". With $\cos\alpha=2/\sqrt5$ and $\tan\gamma=-1/(2\sqrt5)$, $\cos\alpha\cos\gamma=4/\sqrt{21}\approx0.873$, so $t_f\approx0.175$ for MHD; the printed equality drops the factor $t'_f$ *(compiler check, not in the sources)*.
- Eq. (46), the relativistic vortex balance, carries the centrifugal term $w\gamma v_\phi^2/R$ (source $\gamma$ = Lorentz factor), but the text says its solution is Eqs. (44)–(45) with $f=w$, the classical balance with $\rho$ replaced by $w$ and no Lorentz factor. Since the Lorentz factor varies with $R$ in the static vortex, the two statements are inconsistent *(compiler check, not in the sources)*.
- Eq. (54): $A_z=A_0(R-r)$ for $R_1<r\le R$ and 0 "elsewhere", including $r\le R_1$; $A_z$ then jumps by $A_0(R-R_1)$ at $r=R_1$, so that $B_\phi=-\partial_rA_z$ has a delta-function sheet there *(compiler check, not in the sources)*.
- §5.2: "$k=\mu=1/2\pi$" is ambiguous as printed ($1/(2\pi)$ or $\pi/2$).
- §3.4 and §5.5 lower the reconstruction to WENO3 or piecewise linear, while §6 says the fallback "reverts the spatial order of the scheme to 2".
- Ref. [67] is cited in the text as "Bambozzi & Pires" but printed in the reference list as "M. L. B. de Oliveira, V. A. Pires"; ref. [66] prints no authors, and the text attributes it to Jameson.
- The threshold $\Lambda_{\mathrm d}$ (source $\eta_d$) of Eq. (34) and the sensor guard $\varepsilon$ of Eqs. (35)–(36) are given no value anywhere, nor which detector each test uses.
- Typos: "magnetotosonic" (§3.3), "dumped" for "damped" (§3.4), "[70, 71, 15, 15]" (§5.1), "Same of Fig. 2", and "(bottom column)" for the right column in the Fig. 10 caption.

# Notation map

| Berta et al. (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U$, $F$ | $u$, $f^{(d)}$ | conserved variables and flux |
| $\langle Q\rangle_c$ | $\bar u_c$ | cell (volume) average of cell $c=(i,j,k)$ |
| $Q_c$, $Q_{x_f}$, $Q_{x_e}$ | $u_c$, kept | point values at cell, face and edge centres |
| $\hat Q_{x_f}$, $\bar Q_{x_e}$ | kept | face and edge averages; **the source's bar is an edge average, not the registry's cell average** |
| $h$ | $\Delta x$ | cell width (App. A) |
| $\Delta$, $\Delta_x$, $\Delta^x_\perp$ | kept | undivided Laplacian, second difference, transverse Laplacian; **$\Delta_{i+1/2}=V_{i+1}-V_i$ in Eq. (28) reuses the letter** |
| $V$, $V^L_{i+1/2}$, $V^R_{i-1/2}$ | $V$, $V^-_{i+1/2}$, $V^+_{i-1/2}$ | primitive variables and left and right interface states |
| $d_l$, $\beta_l$, $\alpha_l$, $\omega_l$ | $d_k$, $\beta_k$, $\alpha_k$, $\omega_k$ | WENO linear weights (point-value interpolation $\{1/16,5/8,5/16\}$), indicators, weights |
| $\lvert\beta_0-\beta_2\rvert$ | $\tau_5$ | WENO-Z global indicator, power 1 |
| $\varepsilon$ | $\epsilon$ | $10^{-40}$ (WENO-Z), $\Delta x^2$ (WENO3); **also the sensor guard of Eqs. (35)–(36) and the error $\varepsilon_1$ of §5** |
| $\theta_c$, $\eta_c$, $\eta_d$ | $\theta_c$ kept, $\Lambda$, $\Lambda_{\mathrm d}$ | order-reduction flag, detector value, threshold (page-local, as on the troubled-cell page); **$\theta$ is the Zhang–Shu factor and $\eta$ the entropy in the registry** |
| $\eta^o_c$, $\eta^e_c$, $\delta^{(m)}$, $\langle Q\rangle_c$ in Eqs. (35)–(37) | $\Lambda^{\mathrm o}$, $\Lambda^{\mathrm e}$, $\delta^{(m)}$, $\bar\Upsilon$ | odd and even derivatives-ratio detectors, undivided differences, detector quantity (page-local, as on the troubled-cell page) |
| $\mathscr F_{x,y,z}$ | $h$ | one-dimensional Riemann solver |
| $\mathscr L$, $\mathscr C$ | $\mathcal L$, $\nu$ | semi-discrete operator, CFL number; the GFORCE "Courant factor" $c$ is a separate symbol |
| $\lambda^d_{\max}$ | $a$ in direction $d$ | outermost fast magnetosonic speed |
| $a_{x,y}$, $d_{x,y}$ | kept | UCT flux and diffusion coefficients; **$d$ collides with the linear weights and with the dimension of Eq. (50)** |
| $\Gamma$ | $\gamma$ | ratio of specific heats |
| $\gamma$ | $W$ | Lorentz factor |
| $D$, $m$, $E$, $h$, $w$, $w_t$, $b$ | kept | relativistic density, momentum, energy, specific enthalpy, enthalpy density, total enthalpy, field vector; **$h$ is not the numerical flux** |
| $\eta$ (§5.3) | kept | Alfvén-wave amplitude and resistivity in the damping rate |
| $\tau$, $C$, $p$, $N$ (§5.3) | kept | cost per cell update, error constant, order, linear resolution; **$\tau$ is not the WENO-Z indicator, $N$ not a DG degree** |

# Reference list

85 printed references in numbered style ([1]–[85]), all parsed and merged
complete into the [bibliography](/bibliography.md) with `citedby`
`berta-2024`. Ref. [66] prints no authors (the text attributes it to Jameson)
and is merged into the existing `jameson-1981` (AIAA Paper 81-1259) by title
and year. Ref. [12] prints "high?resolution" (an encoding glitch). Ref. [43]
is an arXiv e-print, ref. [64] a book with a Google Books URL; ref. [32] is
printed as J. Comput. Phys. 341 (2016) 230–257, kept as printed.
Same-author-year works take suffixes in printed order (`mignone-2007`,
`mignone-2007-b`; `mignone-2012`, `mignone-2012-b`;
`nunezdelarosa-2016`, `nunezdelarosa-2016-b`). No printed duplicates were
found apart from the repeated in-text citation "[70, 71, 15, 15]".

# Pages created or updated

Chunk 7 (2026-10-23), cited further in chunks 8–10 (2026-10-23). This source is cited on:

* [Brio–Wu MHD shock tube](/benchmarks/brio-wu-shock-tube.md)
* [Cell-average to point-value conversion](/operators/cell-average-point-value-conversion.md)
* [Characteristic decomposition](/methods/characteristic-decomposition.md)
* [Circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md)
* [Constrained transport for the induction equation](/methods/constrained-transport.md)
* [Divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
* [Ducros shock sensor](/definitions/ducros-shock-sensor.md)
* [HLL-family approximate Riemann solvers](/methods/hll-riemann-solvers.md)
* [Magnetic field-loop advection](/benchmarks/field-loop-advection.md)
* [Magnetized (MHD) vortex](/benchmarks/magnetized-vortex.md)
* [MHD blast wave and rotor](/benchmarks/mhd-blast-wave.md)
* [MHD shock–cloud interaction](/benchmarks/mhd-shock-cloud-interaction.md)
* [Monotonicity-preserving (MP) limiter](/methods/monotonicity-preserving-limiter.md)
* [MOOD a posteriori limiting](/methods/mood-a-posteriori-limiting.md)
* [Numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
* [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md)
* [PLUTO](/software/pluto.md)
* [Roe approximate Riemann solver](/methods/roe-riemann-solver.md)
* [Special relativistic hydrodynamics and MHD](/definitions/relativistic-hydrodynamics.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Tearing-mode instability](/benchmarks/tearing-mode-instability.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
* [WENO-JS reconstruction](/methods/weno-js-reconstruction.md)
* [WENO-Z weights](/methods/weno-z.md)
