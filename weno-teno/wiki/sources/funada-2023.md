---
type: Source
title: "Funada & Imamura (2023) — High-order immersed boundary method for inviscid flows applied to flux reconstruction method on a hierarchical Cartesian grid"
description: "Builds sharp-interface immersed-boundary wall states for flux reconstruction on hierarchical Cartesian grids from image lines of Gauss-point image points and curvature-corrected slip-wall conditions, and shows design-order convergence of the entropy error up to the wall for inviscid bump, cylinder and sphere flows."
resource: "doi:10.1016/j.compfluid.2023.105986"
source_kind: paper
authors: [Funada M., Imamura T.]
year: 2023
venue: "Comput. Fluids 265:105986"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Computers_amp_Fluids_Funada_High-order_immersed_boundary_method_for_inviscid_flows_appli.pdf"
tags: [immersed-boundary, flux-reconstruction, dg, compressible-flow, benchmark]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

The paper builds discrete-forcing, sharp-interface
[immersed boundary](/methods/immersed-boundary-method.md) conditions for the
inviscid compressible Euler equations, solved with Huynh's
[flux reconstruction](/methods/flux-reconstruction.md) (FR) on hierarchical
Cartesian grids. The aim is to keep the FR design order $N+1$ up to the wall,
which the authors say earlier immersed boundary methods for FR did not do: the
volume-penalization method of Kou et al. was first order near the wall.

Cells are classified as fluid, wall (cut by the body) and body cells. At each
flux point on a fluid/wall-cell interface a wall-side state is constructed, and
the interface flux is computed with SLAU from it and the fluid-side state. Four
constructions are compared. **LO** copies the state of one image point on the
wall normal and scales the normal velocity linearly; it is first order. The
three high-order variants place $N+1$ image points at the Gauss points of an
image line normal to the wall, take the FR polynomials of the fluid cells at
all but the first, solve for the first from the slip-wall conditions on $u_n$,
$H$, $p\rho^{-\gamma}$ and $u_t$ written at the wall, and interpolate the
resulting polynomials to the flux point. **HO-i/c** imposes the curvature
condition $\partial u_t/\partial n=u_t/R_{\mathrm w}$; **HO-i/f** takes a flat
wall; **HO-e** drops the curvature condition and extrapolates $u_t$ from a
second set of image points that lie in the fluid. Hanging faces are handled by
the mortar element method, and steady states are reached with an implicit
matrix-free Gauss–Seidel method accelerated by defect correction on sub-cells.

A wall-free vortex confirms order $N+1$ for $N=1$ to $3$. On a subsonic bump
channel, the [flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
($M=0.3$) and a sphere ($M=0.2$), HO-i/c and HO-e reach design order in the
$L_2$ entropy error, with near-zero drag, and LO and HO-i/f do not: neglecting
the curvature loses the order. The authors recommend HO-e for complex
geometries because it needs no wall curvature. There are no shocks, no limiting
and no theory; the evidence is numerical.

# Version read

Version of record (Elsevier typeset, Comput. Fluids 265:105986; received
19 Jan 2023, accepted 28 Jun 2023, online 5 Jul 2023), 12 pages. Title,
authors, venue and DOI on page 1 match Crossref. Section, equation, table and
figure numbers are those of the version of record.

# Key claims

Registry notation: $N$ is the polynomial degree, so the source's $k$ solution
points per direction are $N+1$ and its design order $k$ is $N+1$; $u$ is the
conserved state (the source's $q$), $v$ the velocity, $p$ the pressure, with
$u_n$, $u_t$ the wall-normal and tangential velocity components kept as printed
(see the Notation map).

1. Earlier immersed boundary methods are typically second order or lower; Kou et al.'s volume-penalization method for FR reached fifth order far from the wall but first order near it, for advection–diffusion (§1). **Stated**
2. FR with $N+1$ solution points at the Gauss points is of order $N+1$. Huynh's correction function $g_{\mathrm{HU}}$ (Eq. (10)) is used for its "large upper bound on the Courant number" (§2.1). **Stated**
3. The common flux is SLAU (Shima & Kitamura), at interior interfaces and at the immersed-wall flux points (§2.1, §2.3). **Stated**
4. At refinement interfaces of the hierarchical grid the flux points of the two sides do not coincide; a three-step mortar projection (coarse-side states to mortar points, common fluxes, projection back) handles them (§2.2, Fig. 3). **Stated**
5. Two sets of adiabatic slip-wall conditions, Eqs. (14) (in $\rho$, $p$, $u_t$, with curvature in $\partial p/\partial n=-\rho u_t^2/R_{\mathrm w}$ and $\partial u_t/\partial n=u_t/R_{\mathrm w}$) and Eqs. (15) ($u_n=0$, $\partial H/\partial n=0$, $\partial(p\rho^{-\gamma})/\partial n=0$, $\partial u_t/\partial n=u_t/R_{\mathrm w}$), are stated to be equivalent for smooth 2-D inviscid flow; Eqs. (15) are used because the curvature enters one equation only (§2.3). **Stated** (no derivation)
6. LO (one image point, Eq. (16)) is first order. It requires an image-point distance $d_{\mathrm{IP}}\ge\sqrt{n_{\mathrm{DIM}}}\Delta x$ (Eq. (17)), and $d_{\mathrm{IP}}=3\Delta x$ is used (§2.3.1). **Stated**
7. Zero- or first-order interpolation from one image point per flux point is known to be inaccurate near the wall, which motivates the multi-point methods (§2.3.2). **Stated**
8. HO-i/c: $N+1$ image points at the Gauss points of the image line; the first is eliminated by imposing the polynomial form of Eqs. (15) at the wall end $\xi=-1$ (Eqs. (18)–(19)), and the flux-point state is interpolated from the degree-$N$ image-line polynomials (§2.3.2). **Derived**
9. HO-i/f is HO-i/c with $R_{\mathrm w}\to\infty$ in Eq. (19d), i.e. $\partial u_t/\partial n=0$ at the wall (Eq. (20)) (§2.3.2). **Derived**
10. HO-e takes $u_n$, $H$ and $p\rho^{-\gamma}$ from the image points of HO-i/c and extrapolates $u_t$ to the flux point from a second set of image points that lie wholly in the fluid (Eq. (21)); it uses no wall curvature (§2.3.2, Fig. 8). **Derived**
11. The second image point must lie in a fluid cell, $d_{\mathrm{IL}}(1+\xi_2)/2\ge\sqrt{n_{\mathrm{DIM}}}\Delta x$ (Eq. (22)), with lower limits $1.79$, $2.83$, $4.29\,\Delta x$ ($N=1,2,3$, 2-D) and $2.20$, $3.46$, $5.25\,\Delta x$ (3-D); the lengths used are $3,3,5\,\Delta x$ (2-D) and $3,5,7\,\Delta x$ (3-D) (§2.3.2). **Derived** (the six limits follow from the Gauss points: 1.793, 2.828, 4.285 and 2.196, 3.464, 5.248 *(compiler check, not in the sources)*)
12. When an image point or image line ends in a cell containing part of another body, the immersed boundary treatment is not used: the wall is a step-wise face and the flux-point values come from the fluid cell (§2.3.2). **Stated**
13. In 3-D the high-order interpolation is done in the plane of the wall normal $n$ and the tangential direction of the velocity at the second image point (Eq. (23)) (§2.3.3). **Stated**
14. Time integration is explicit four-stage fourth-order Runge–Kutta or implicit matrix-free Gauss–Seidel; because the FR Jacobian is dense, defect correction on sub-cells (first-order finite volumes around each solution point) is used (§2.4). **Stated**
15. Wall-free vortex advection: order $N+1$ in the $L_\infty$ error of $v_2$ for $N=1,2,3$ (§3.1, Fig. 10). **Shown**
16. Bump channel ($M=0.5$): HO-i/c and HO-e converge at order $N+1$ in the $L_2$ entropy error against $\sqrt{N_{\mathrm{DoF}}}$, LO and HO-i/f at lower order, with errors "one to three orders of magnitude less" for the former (§3.2, Fig. 12). **Shown**
17. Bump drag coefficients ($N=2$, $\Delta x_{\min}=0.0100$): LO $2.7\times10^{-5}$, HO-i/f $3.6\times10^{-5}$, HO-i/c $7.8\times10^{-7}$, HO-e $1.0\times10^{-7}$; the fore–aft asymmetry of the surface $C_p$ is smaller for HO-i/c and HO-e (§3.2, Table 1, Fig. 15). **Shown**
18. Cylinder ($M=0.3$): against $\sqrt{N_{\mathrm{DoF}}}$ the entropy-error slopes are "much steeper" than design order, which the authors attribute to the error concentrating near the wall of the non-uniform grid (Fig. 18); against $1/\Delta x_{\min}$, HO-i/c and HO-e are of order $N+1$ and LO and HO-i/f are not (§3.3, Figs. 17–19). **Shown**
19. Cylinder drag ($N=2$, $\Delta x_{\min}=0.0244$): LO $5.0\times10^{-2}$, HO-i/f $1.2\times10^{-2}$, HO-i/c $9.1\times10^{-5}$, HO-e $4.5\times10^{-4}$; front and rear stagnation $C_p$ are closer to the theoretical $1.023$ with HO-i/c and HO-e, and the LO and HO-i/f velocity fields are fore–aft asymmetric (§3.3, Table 2, Figs. 20–21). **Shown**
20. Sphere ($M=0.2$): HO-i/c and HO-e are of order $N+1$ against $1/\Delta x_{\min}$, LO and HO-i/f are not; drag ($N=2$, $\Delta x_{\min}=0.0244$) LO $1.5\times10^{-2}$, HO-i/f $1.4\times10^{-2}$, HO-i/c $7.0\times10^{-4}$, HO-e $9.0\times10^{-4}$; stagnation $C_p$ closer to the theoretical $1.010$ (§3.4, Table 3, Figs. 23–25). **Shown**
21. Neglecting the wall curvature while keeping high-order image-line polynomials (HO-i/f) loses the design order; the curvature must be imposed (HO-i/c) or avoided by extrapolating $u_t$ (HO-e) (§3.2–§3.4, §4). **Shown**
22. HO-e is "more versatile" for complex geometries because it needs no robust, accurate wall curvature (§3.4, §4). **Stated** (on the cylinder and sphere HO-i/c gives the smaller drag, claims 19–20)

# Printed slips

- Eq. (12): $q_i(\xi,\eta)=\sum_{l=1}^k\sum_{m=1}^kq_{i;l,m}\phi_l(\xi)\phi_m(\xi)$; the second factor should be $\phi_m(\eta)$, as the left-hand side and the text ("indexes of the SP in the $\xi$ and $\eta$ directions") imply.
- Eq. (28) prints the entropy error with $\frac{P}{P_\infty}\left(\frac{\rho}{\rho_\infty}\right)^\gamma-1$. With $S=P/\rho^\gamma$ (Eq. (15c)) the entropy ratio is $\frac{P}{P_\infty}\left(\frac{\rho_\infty}{\rho}\right)^\gamma$: the printed density ratio is inverted, and the printed expression does not vanish on an isentrope, where it equals $(\rho/\rho_\infty)^{2\gamma}-1$ *(compiler check, not in the sources)*.
- Eq. (15b) writes $H=(E+P)/\rho$, but §2.2 calls $E$ the "specific total energy" (the energy equation carries $\rho E$); with that definition $H=E+P/\rho$.
- §2.3.2 (p. 5): "without using Eq. (15d) which includes the wall curvature. (15d)." — a dangling "(15d).".
- §3.2 (p. 7): the pointer "(see Fig. 14)" after the Table 1 drag statement points to the pressure-coefficient field.
- §3.3 (p. 7): "On the other hand, the velocity distribution is close to line-symmetric." — the subject (HO-i/c and HO-e) is missing.
- §1: "Burger's equation".
- The value of $\gamma$ is printed nowhere. The theoretical stagnation values $C_p=1.023$ ($M=0.3$) and $1.010$ ($M=0.2$) are those of $\gamma=1.4$: $1.0227$ and $1.0100$ *(compiler check, not in the sources)*.
- §3.4 does not state the sphere diameter.
- Reference list: [12] prints the author as "Iaccarino RMG" with "Annu Rev Fluid Mech 2004;24"; [4] and [29] lack pages; [15] lacks a volume ("J Comput Phys 2021;110721").

# Notation map

| Funada & Imamura 2023 | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $k$ (solution points per direction, design order) | $N+1$ | the polynomial degree is $k-1=N$; **collision** with the registry's use of $k$ as a stencil index |
| $q$, $q_{i;j}$ | $u$, nodal value at solution point $j$ of cell $i$ | conserved state at Gauss solution points |
| $f$, $f_i(\xi)$, $f^c_i$, $f^{com}_{i\pm1/2}$ | $f$; interpolated discontinuous flux; corrected flux; $\hat f_{i\pm1/2}$ | common flux from SLAU |
| $\sigma_i$ | correction term (local) | **collision** with the affine scaling $\sigma$ of §10 |
| $g_L$, $g_R$, $g_{HU}$ | FR correction functions | **collision** with the mapping function $g(\omega)$ and constraints $g_i$ |
| $L_k$ | Legendre polynomial (local) | **collision** with the left-eigenvector matrix $L$ |
| $\phi_j$ | $\ell_j$ | Lagrange basis on the Gauss points |
| $\xi$, $\eta$ | reference coordinates | also the image-line coordinate, $\xi=-1$ at the wall; not the nodes $\xi_j$ of §7 when used as a line coordinate |
| $\rho$, $u_i$, $P$ | $\rho$, $v$, $p$ | velocity and pressure translated |
| $E$ ("specific total energy") | $E/\rho$ | registry $E$ is per unit volume |
| $H$ | $H$ | specific total enthalpy; agrees (but see Printed slips) |
| $S=P/\rho^\gamma$ | $e^{s}$ | entropy function, not the registry $s=\ln(p\rho^{-\gamma})$ |
| $u_n$, $u_t$ | $u_n$, $u_t$ (local) | wall-normal and tangential velocity; **collision** with the state $u$, kept for readability with subscripts |
| $R$ | $R_{\mathrm w}$ (local) | wall curvature radius; **collision** with the right-eigenvector matrix $R$; sign convention not stated |
| $n$, $\boldsymbol n$, $\boldsymbol s$, $\boldsymbol u_s$ | wall normal direction, unit normal, tangential unit vector (local) | |
| SP, FP, IP, IP$_A$, IP$_B$, IL | solution, flux and image points; image line | |
| $d_{FP}$, $d_{IP}$, $d_{IL}$, $\xi_2$, $n_{DIM}$ | wall distances, image-line length, coordinate of the second image point, dimension (local) | |
| $\Delta x$, $\Delta x_{min}$ | $\Delta x$, $\Delta x_{\min}$ | local and minimum cell width |
| $M$, $M_\infty$, $\kappa$, $r$ | $M$; vortex parameters (local) | **collision**: $\kappa$ is the registry kinetic energy |
| $N_{DoF}=N_{Grid}k^2$, $N_{Grid}$ | $N_{\mathrm{DoF}}$, number of cells (local) | 2-D count |
| $C_d$, $C_p$, $\Delta C_p$ | drag and pressure coefficients, fore–aft difference | |

# Reference list

The paper prints 33 references, numbered [1]–[33] in Elsevier's numbered
style. The list is merged complete into the [bibliography](/bibliography.md)
with `citedby` including `funada-2023`. Ref. [15] (Kou et al., printed
"J Comput Phys 2021;110721") is the ingested `kou-2022` (J. Comput. Phys.
448:110721) and is keyed to it, not to its printed year. [12] carries a garbled
author string ("Iaccarino RMG") and is kept as printed; [4] and [29] have no
pages and [15] no volume; [1] is a report with no institution printed. No item
is unparseable.

# Pages created or updated

Chunk 5 (2026-10-22), cited further in chunks 6–9 (2026-10-23). This source is cited on:

* [Flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
* [Flux reconstruction and energy-stable FR](/methods/flux-reconstruction.md)
* [Immersed-boundary and cut-cell methods](/methods/immersed-boundary-method.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
