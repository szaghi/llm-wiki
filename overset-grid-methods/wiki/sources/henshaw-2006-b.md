---
type: Source
title: "Henshaw (2006) — A high-order accurate parallel solver for Maxwell's equations on overlapping grids"
description: "Fourth-order time-domain Maxwell solver on overlapping grids in second-order (vector wave) form: modified-equation time stepping, symmetric high-order curvilinear Laplacians that conserve a discrete energy, centred compatibility boundary and dielectric-interface conditions, interpolation of width p+1 with high-order dissipation against weak instability, and a parallel implementation."
resource: "doi:10.1137/050644379"
source_kind: paper
authors: [Henshaw W.D.]
year: 2006
venue: "SIAM J. Sci. Comput. 28:1730-1765"
local_file: "/home/stefano/papers/mosaic/overset-chimera/2006_Crossref_SIAM_Journal_on_Scientific_Computing_Henshaw_A_HighOrder_Accurate_Parallel_Solver_for_Maxwells_Equations.pdf"
tags: [composite-grid, high-order, finite-difference, interpolation, parallel]
timestamp: 2026-11-02T14:53:00Z
---

# Summary

Henshaw builds a time-domain solver for [Maxwell's equations on overlapping grids](/methods/maxwell-equations-on-overset-grids.md).
The equations are written in second-order form: the electric and magnetic fields each satisfy a
vector wave equation, so no staggered grid is needed and the principal part is a Laplacian. The
[composite overlapping grid](/definitions/composite-overlapping-grid.md) is the Chesshire–Henshaw
one, with the three-class [point classification](/definitions/point-classification.md) and
smooth mappings, which high order requires. The method has four parts.

- **Modified-equation time stepping.** A three-level Taylor scheme of any even order; at fourth
  order the $\partial_t^4$ term uses a second-order biharmonic, so the stencil stays compact and the
  time-step limit equals the second-order one.
- **Symmetric operators.** High-order approximations (orders 2–8) of $\nabla\cdot(\kappa\nabla)$ in
  conservation form are symmetric in a $\mathcal J$-weighted inner product ($\mathcal J=\det(\partial\mathbf x/\partial\mathbf r)$), so the three-level scheme
  conserves a discrete energy, even on randomly perturbed grids.
- **Compatibility conditions.** Centred numerical boundary conditions come from even time
  derivatives of the boundary conditions, for perfect electrical conductors (PEC) and for
  material interfaces between dielectrics; the interface conditions pass a Godunov–Ryabenkii
  analysis.
- **Overlap coupling.** Tensor-product Lagrange [inter-grid interpolation](/methods/inter-grid-interpolation.md)
  of width $q=p+1$, as the [interpolation-order requirement](/results/interpolation-order-requirement.md)
  gives for a second-order equation. Interpolation and curvilinear boundaries break the symmetry
  of the discrete operator, so high-frequency modes become weakly unstable; a high-order
  dissipation suppresses them and keeps fourth order (see
  [high-order discretizations on overlapping grids](/methods/high-order-overset-discretization.md)).

The solver mx is built on [Overture](/software/overture.md), successor of [CMPGRD](/software/cmpgrd.md),
with distributed arrays and a parallel interpolation that sends at most one message between any two
processors. [Twilight-zone](/methods/twilight-zone-flow.md) tests on a cylinder-in-channel grid
(the geometry of [flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md), here
for Maxwell, not flow) and a sphere-in-box grid give rates of about 4. So do PEC sphere scattering
against the Mie series, dielectric-cylinder scattering and disk eigenvalues. Eigenvalues of an
L-shaped domain with a rounded corner converge at between first and second order.

# Version read

The SIAM version of record (SIAM J. Sci. Comput. 28(5):1730–1765, received 5 November 2005,
published electronically 20 October 2006), 36 pages, all read; equation-heavy pages were checked
visually. Page 1 matches the Crossref card (sole author, LLNL). This is the SISC Maxwell paper, not
the JCP moving-grid paper [Henshaw & Schwendeman (2006)](/sources/henshaw-2006.md).

# Key claims

Below $\mathbf E$, $\mathbf H$ are the electric and magnetic fields (not the total energy $E$),
$\epsilon$, $\mu_{\mathrm m}$ permittivity and permeability (as on [Maxwell's equations on overlapping grids](/methods/maxwell-equations-on-overset-grids.md)), $c=1/\sqrt{\epsilon\mu_{\mathrm m}}$, and $\mathsf L$ the spatial matrix with eliminated boundary conditions.

1. In second-order form $\mathbf E$ and $\mathbf H$ decouple, each satisfying a vector wave
   equation with lower-order terms (Eqs. (1.4)–(1.5)), which for constant coefficients and no
   sources reduces to $\partial_t^2\mathbf E=c^2\nabla^2\mathbf E$ (Eq. (1.6)). (§1) **Derived**
2. The second-order form needs the extra boundary condition $\nabla\cdot\mathbf E=0$ at PEC and
   far-field boundaries; Gauss's law then holds everywhere, since $\nabla\cdot\mathbf E$ satisfies
   a wave equation with zero initial and boundary data. (§2) **Derived**
3. The modified-equation expansion gives three-level schemes of any order; the fourth-order scheme
   (3.2) uses a fourth-order Laplacian and a second-order biharmonic, so its stencil is no wider
   than the fourth-order Laplacian. (§3) **Derived**
4. The compatibility conditions $\mathbf n\times(\nabla^2)^m\mathbf E=0$ and
   $\nabla\cdot(\nabla^2)^m\mathbf E=0$ on PEC boundaries (and $\partial_n(\nabla^2)^mH_z=0$ in 2-D),
   $m=0,1,\dots$, give centred numerical boundary conditions, "in general" more stable and accurate
   than one-sided ones. (§3, Eqs. (3.3)–(3.4)) **Derived** / **Stated** (the preference)
5. Lemma 5.1: $D_{+t}D_{-t}\mathbf U^n=\mathsf L\mathbf U^n$ is stable iff $\mathsf L$ has a complete
   set of eigenvectors with real negative eigenvalues $\lambda$ and $-4<\lambda\Delta t^2<0$. (§5)
   **Proved**
6. For symmetric negative-definite $\mathsf L$ the discrete energy (5.6)–(5.7) is constant in time
   and positive under the step condition. (§5) **Derived**
7. High-order symmetric approximations of $\nabla\cdot(\kappa\nabla)$ exist on any logically rectangular
   curvilinear grid, built from the conservation form (5.10), the $\mathcal J$-weighted inner product (5.11)
   and the midpoint-derivative expansion (5.12); orders 2, 4, 6, 8 are implemented in 2-D and 3-D.
   (§5) **Derived**
8. Symmetric (SD$m$) and standard mapping-method (FD$m$) operators have similar Laplacian errors on
   a smooth nonorthogonal grid; legend rates in 2-D: FD2 2.7, SD2 2.7, FD4 4.0, SD4 4.0, FD6 5.3,
   SD6 5.8, FD8 6.9, SD8 7.5; in 3-D: 2.5, 2.5, 4.0, 4.0, 5.8, 5.8, 7.2, 7.5. (§5, Fig. 1) **Shown**
9. On randomly perturbed periodic grids the SD schemes keep the discrete energy constant to relative
   $10^{-10}$ for $t\in[0,100]$; the FD schemes do not conserve it and are unstable there without
   dissipation. (§5, Fig. 2) **Shown**
10. Lemma 6.1: the fourth-order scheme with PEC numerical boundary conditions (6.2)–(6.6) on
    $[0,1]^2$ (PEC in $x$, periodic in $y$) is stable for $\Delta t<c^{-1}(\Delta x^{-2}+\Delta y^{-2})^{-1/2}$,
    the second-order limit; the 3-D analogue follows "by an argument similar". (§6) **Proved**
    (2-D), **Stated** (3-D)
11. The discrete eigenvalues of this model problem are fourth-order approximations of
    $e^{\mathrm ik\Delta t}$. (§6) **Derived**
12. Away from boundaries the Yee scheme is equivalent to the second-order version of the present
    scheme: each staggered component satisfies the standard centred wave equation. (§6.1)
    **Derived**
13. The material-interface jump conditions (7.3)–(7.6) and their compatibility hierarchy
    (7.7)–(7.10) give centred interface conditions of second order (7.11)–(7.12) and fourth order
    (7.15)–(7.18); interface values are set by (7.13)–(7.14). (§7) **Derived**
14. When $\epsilon_1=\epsilon_2$ the discrete interface conditions reproduce the no-interface
    solution. (§8) **Derived**
15. Lemma 8.1: the second-order interface approximation (8.4)–(8.7) satisfies the
    Godunov–Ryabenkii condition and is second-order accurate. (§8) **Proved**
16. Lemma 8.2: the fourth-order interface approximation (8.16)–(8.21) satisfies the
    Godunov–Ryabenkii condition for $sh\ll1$ ($s$ the Laplace variable); general $sh$ is
    "difficult to prove". (§8) **Proved** (asymptotic regime only)
17. A plane wave crossing a straight interface ($\epsilon_2=4$; a 45°-rotated case with
    $\epsilon_2=16$), $80\times80$ cells per side, stays stable to $t=500$ (about 60000 steps), with
    maximum error 0.01 in $E_y$ and 0.05 in $E_x$ (rotated); without dissipation the interface
    equations must be solved accurately (about 30 iterations) to avoid a late-time instability.
    (§8, §9.3, Fig. 4) **Shown**
18. On a general overlapping grid interpolation and boundary conditions make the scheme
    non-symmetric, so some eigenvalues have nonzero imaginary parts and the high-frequency modes are
    weakly unstable (after Reyna); a fourth-order dissipation (9.9) with coefficient about 1
    suppresses them and keeps fourth order, while sixth-order dissipation brings no significant
    advantage. (§3, §9.2) **Stated** (mechanism argued, not proved)
19. Interpolation width $q=p+1$ for a $p$th-order approximation of the second-order wave equation,
    following Chesshire & Henshaw. (§4) **Stated**
20. The parallel interpolation evaluates the Lagrange formula on the processor owning the donor
    stencil and sends the sums to the owner of the receptors, with at most one message between any
    two processors. (§9.4) **Stated**
21. Strong scaling on a Linux cluster is very good in 2-D (square, $1.1\times10^6$ points;
    circle in a channel, $3.8\times10^6$) and reasonable in 3-D (box; pill-box,
    $3.2\times10^6$); the overlapping grid scales comparably to the box. (§9.4, Fig. 5) **Shown**
22. Twilight zone at $t=1$: 2-D cylinder in a channel, rates $\sigma$ = 4.40 ($E_x$), 3.93 ($E_y$),
    4.02 ($H_z$), 3.94 (normalized divergence) (Table 1); 3-D sphere in a box, 4.12, 4.26, 4.11,
    3.47 (Table 2). (§10.1) **Shown**
23. PEC sphere scattering against the Mie series at $t=3$: rates 3.86, 3.86, 3.85 and 3.09 for the
    divergence. (§10.2, Table 3) **Shown**
24. Dielectric cylinder scattering ($ka=4\pi$, wave speeds 1 outside and 2 inside): rates 3.86,
    3.87, 3.88 and 3.92, verifying the fourth-order interface conditions. (§10.3, Table 4)
    **Shown**
25. Disk eigenvalues of $-\nabla^2\mathbf E=\lambda\mathbf E$ converge at close to fourth order; for
    the L-shaped domain with a rounded corner the five smallest converge at rates between 1 and 2,
    with coarse-grid relative errors from $9.93\times10^{-3}$ to $2.53\times10^{-5}$; the computed
    eigenvalues are real to double precision. (§10.4, Figs. 8–9, Table 5) **Shown**
26. Serial cost per step on a 2.2 GHz Xeon: 2-D cylinder ($3.8\times10^6$ points) 1.73 s, of which
    Cartesian advance 71.4%, curvilinear 14.0%, boundary conditions 10.6%, interpolation 0.46%; 3-D
    pill-box ($10.2\times10^6$ points) 15.0 s, of which 28.2%, 47.8%, 14.8% and 6.8%. In 3-D a
    fourth-order curvilinear point costs about ten Cartesian points. (§10.5, Table 6) **Shown**
27. Memory for the 3-D pill-box ($10.2\times10^6$ points, about $4.2\times10^5$ receptors): 980 MB,
    12.6 reals per point, of which the overlapping grid takes 2.3 (17.8%); storing
    $\partial\mathbf x/\partial\mathbf r$ on all grids would alone take 9 reals per point. (§10.5,
    Table 7) **Shown**
28. Rounding re-entrant corners of large opening angle with smooth boundary-fitted grids is
    recommended for other problem classes too. (§10.4) **Stated**

# Printed slips

- **Lemma 8.1 proof (p. 1747):** "$s_1=-s_2-4$ … implies $s=\pm i/(h\sqrt{\epsilon_1+\epsilon_2})$".
  With $s_k=\epsilon_ks^2h^2$ this gives $s=\pm2\mathrm i/(h\sqrt{\epsilon_1+\epsilon_2})$; the
  conclusion ($s$ imaginary) is unaffected *(compiler check, not in the sources)*.
- **§5 (p. 1738):** the midpoint-derivative series
  $\partial_rw(r+h_r/2)=D_+[1+\sum_n\alpha_nh_r^{2n}(D_+D_-)^n]w$ is printed with $\alpha_1=-\frac16$.
  Since $D_+w=\partial_rw(r+h_r/2)+\frac{h_r^2}{24}\partial_r^3w+O(h_r^4)$, the coefficient is
  $-\frac1{24}$, the value that Eq. (5.12) and the fourth-order operator $\mathcal L^{(4)}_{rr}$ use
  ($h_r^2/24$); the printed $\alpha_2=\frac3{640}$, $\alpha_3=-\frac5{7168}$,
  $\alpha_4=\frac{35}{294912}$ belong to that series *(compiler check, not in the sources)*.
- **§9.1 (p. 1751):** $D^{(4)}_{r_m}=D_{0,r_m}(1-\frac1{12}\Delta r_1{}^2D_{+,r_m}D_{-,r_m})$ is called
  the fourth-order approximation of $\partial/\partial r_m$. Since
  $D_0=\partial+\frac{h^2}{6}\partial^3+O(h^4)$, fourth order needs $\frac16$, as the paper itself
  prints in (6.3) and (8.18), and $\Delta r_m$ for $\Delta r_1$ *(compiler check, not in the
  sources)*.
- **§6.1 (p. 1743):** the second-order form of the Yee scheme is printed
  "$(D_{+x}D_{+x}+D_{+y}D_{-y})U^n_{i+\frac12,j}$" and called "the standard central difference
  operators"; $D_{+x}D_{+x}$ should read $D_{+x}D_{-x}$.
- **§9.1:** "$-\partial_{r_2}(\mathbf a_2\cdot\mathbf E_2)$" and "a$_2\cdot\mathbf E_2$" carry a stray
  subscript ($\mathbf E$).
- **§10.1 (p. 1755):** "$c_x=\cos(\pi x)$, $s_y=\sin(\pi x)$"; only $s_y=\sin(\pi y)$ makes the
  printed exact fields divergence-free, as the text says they are *(compiler check, not in the
  sources)*.
- **§1 (p. 1731):** "the first-order system (1.2)–(1.3)"; the evolution system is (1.1)–(1.2), as the
  same page later says.
- **§6 (p. 1742):** "$\kappa_{mn}$ is a fourth-order accurate approximation", for the $\kappa_{\alpha,\beta}$
  defined a few lines before.
- **Fig. 5 caption and §9.4:** "a box with $256^3$ (1.78e7) grid points"; $256^3=1.68\times10^7$
  *(compiler check, not in the sources)*. The paper does not say whether ghost points are counted.
- **Table 1:** the $E_x$ rate 4.40. Three grids equally spaced in $\log h$ give the least-squares
  slope $\log_2(9.1\times10^{-5}/2.2\times10^{-7})/2=4.35$ from the printed errors *(compiler check,
  not in the sources)*.
- "Zeon" for Xeon (§9.4, Table 6 caption); ref. [9] "Ditkowksi" against "Ditkowski" in the text;
  ref. [5] "Costable" (Costabel); §8 "$[v_{xx}/\epsilon]_{\mathcal I}$ have been imposed" lacks
  "$=0$".

# Notation map

| Henshaw (2006) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathcal G=\{G_g\}$, $\mathbf x=G_g(\mathbf r)$ | $\mathcal G=\{G_k\}$, $\mathbf x=\mathbf d_k(\mathbf r)$ | |
| $d$ | $n_d$ | |
| $N_m$, $\Delta r_m=1/N_m$ | $N_m-1$ intervals, $\Delta r_m$ | **the source's $N_m$ counts intervals, the registry's points** |
| $J=\det[\partial x_i/\partial r_j]$ | $\mathcal J=\det(\partial\mathbf x/\partial\mathbf r)$ (page-local) | **inverse of the registry's Pulliam–Steger $J$ (up to $\Delta r_m$ scaling)** |
| $\mathbf a_m=J\nabla_{\mathbf x}r_m$ | $\mathcal J\nabla_{\mathbf x}r_m$, scaled contravariant basis vectors | page-local |
| discretization, unused, interpolation points | $\mathcal D_k$, $\mathcal H_k$, $\mathcal R_k$ | no mask printed |
| $w$ (interpolation width) | $q$ | **$w$ is also $H_z$ in the TE$_Z$ unknowns** |
| $p$ | $p$ | also the dissipation exponent in $h^{2p}(-\Delta)^p$ |
| $\Delta$, $\Delta_{mh}$, $(\Delta^2)_{mh}$ | $\nabla^2$, $\nabla^2_m$, $m$th-order biharmonic | |
| $D_{\pm r_m}$, $D_{0r_m}$, $D_{\pm t}$ | $D_{\pm m}$, $D_{0m}$, time differences | |
| $\mathbf E$, $\mathbf H$ | electric, magnetic field (page-local) | **$E$ is the total energy in the registry** |
| $\epsilon$, $\mu$, $c$ | $\epsilon$, $\mu_{\mathrm m}$, $c$: permittivity, permeability, wave speed (page-local) | **$\mu$ is the dynamic viscosity in the registry** |
| $\rho$, $\mathbf J$ | $\rho_{\mathrm q}$, $\mathbf J_{\mathrm q}$: charge and current density (page-local) | **$\rho$ is the density, $J$ the Jacobian in the registry** |
| $A$ (5.3), $A^{mn}$ (5.10), $k$ | $\mathsf L$, $a^{mn}$, $\kappa$ (page-local) | spatial matrix with boundary conditions; conservation-form coefficients; coefficient of $\nabla\cdot(k\nabla)$ |
| $\mathcal E_h^n$ | discrete energy | registry's reserved $\lVert u\rVert_{\mathsf H}^2$ is the SBP form, not used here |
| $\kappa$ | amplification factor or spatial root | page-local; not used on the concept pages, where $\kappa$ is the coefficient $k$ |
| $\alpha_n$, $\beta_n$, $\alpha_d$, $\alpha$ | expansion coefficients, dissipation coefficient, interface switch | **not the interpolation weights $\alpha_{\mathbf j}$**; $\beta$ reserved for WENO |
| $\mathbf n$, $\boldsymbol\tau_m$, $[\cdot]_{\mathcal I}$ | $\mathbf n$ outward normal, $\mathbf t_\mu$ unit tangents, $[\cdot]$ jump across the interface | |
| $\sigma$ | $\sigma$ | observed rate |
| $\delta_E$ | normalized divergence $\lVert\nabla\cdot\mathbf E\rVert_\infty/\lVert\nabla\mathbf E\rVert_\infty$ | page-local; **$\delta$ is the Yin–Yang buffer angle** |
| method of analytic solutions | twilight-zone forcing | |
| $\mathcal G_1$, $\mathcal G_2$, $\mathcal G_4$ | coarse grid and its 2× and 4× refinements | |

# Reference list

45 printed references, numbered [1]–[45] in alphabetical order (SIAM style), no DOIs printed, all
merged complete into the [bibliography](/bibliography.md) with `citedby` henshaw-2006-b. Same-author
same-year suffixes: `gustafsson-2004` / `gustafsson-2004-b` ([15], [16]) and `hazard-2002` /
`hazard-2002-b` ([17], [18]). Ref. [20], Henshaw, Kreiss and Reyna (Comput. Fluids 1994), is the
existing entry `henshaw-1994-e`, distinct from the ingested [Henshaw (1994)](/sources/henshaw-1994.md).
Ref. [8], printed "A.-S. B.-B. Dhia", is `bonnetbendhia-1999`; ref. [9] is keyed `ditkowski-2001`
from the body-text spelling. The Overture and Dauge-benchmark web pages appear only in footnotes and
are not numbered references.

# Pages created or updated

Chunk 2 (2026-11-02). This source is cited on:

- [Flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
- [Flow past a sphere](/benchmarks/flow-past-sphere.md)
- [Composite overlapping grid](/definitions/composite-overlapping-grid.md)
- [Overset (Chimera) grid](/definitions/overset-grid.md)
- [Point classification and the iblank mask](/definitions/point-classification.md)
- [High-order discretizations on overlapping grids](/methods/high-order-overset-discretization.md)
- [Inter-grid interpolation](/methods/inter-grid-interpolation.md)
- [Maxwell's equations on overlapping grids](/methods/maxwell-equations-on-overset-grids.md)
- [Parallel and GPU overset grid assembly](/methods/parallel-overset-grid-assembly.md)
- [Twilight-zone flow (manufactured solutions)](/methods/twilight-zone-flow.md)
- [Interpolation order and overlap requirements](/results/interpolation-order-requirement.md)
- [CMPGRD and its solver suite (CGINS, CGNVT, CGES, CGMG, DSK)](/software/cmpgrd.md)
- [Overture (and its grid generator Ogen)](/software/overture.md)
