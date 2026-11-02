---
type: Definition
title: "Notation registry"
description: "Normative symbol registry of the bundle: component and composite grids, their mappings, point classification, inter-grid interpolation, conservative interfaces, flow equations in Cartesian and curvilinear form, grid motion, Yin–Yang grids, and reserved symbols for high-order, SBP–SAT, immersed-boundary and unstructured overset methods; every concept page writes mathematics in this notation, never in paper-native symbols."
status: established
tags: [notation, meta]
timestamp: 2026-11-02T15:28:00Z
---

# Notation registry

Every concept page of this bundle writes mathematics in the symbols below.
A source's own symbols are translated on its Source page (`# Notation map`).
The registry was seeded on 2026-11-02 from chunk 1, the founding papers:
the Chimera papers of Benek, Steger and Dougherty (1983) and Benek, Buning
and Steger (1985), Meakin and Suhs (1989) on moving bodies, Chesshire and
Henshaw (1990) on composite overlapping grids and CMPGRD, Henshaw (1994)
on fourth-order incompressible flow, Wang (1995) on the conservative
interface, Lee and Baeder (2003) on implicit hole cutting, Rogers, Suhs
and Dietz (2003) on PEGASUS 5, Kageyama and Sato (2004) on the Yin–Yang
grid and Noack (2005) on SUGGAR. The grid, mapping and
interpolation-order symbols follow Chesshire and Henshaw, the only
chunk-1 sources that write them as mathematics; the curvilinear flow
equations follow the Pulliam–Steger form shared by the three Chimera flow
papers. Extend this registry, and log the extension, before writing a
symbol it lacks.

**Conventions that the sources split on, fixed here.** Component grids
are $G_k$, $k=1,\dots,n_g$, never the two-index $G_{\ell,i}$ of Benek's
hierarchy (the level becomes $\ell(k)$), never the letters $A$, $B$ of
Wang, never $\mathcal G_g$; a higher $k$ means a higher priority, as in
CMPGRD. The mapping is $\mathbf x=\mathbf d_k(\mathbf r)$, as in both
sources that write one; later literature writes $\mathbf G_g(\mathbf r)$
and is translated, because $G_k$ is the grid here. The **Jacobian $J$ is
the Pulliam–Steger one**, $J=\det(\partial\boldsymbol\xi/\partial\mathbf x)$,
so $J^{-1}$ is the cell volume and $\hat{\mathbf q}=\mathbf q/J$: all three
sources that print $J$ (Benek 1985, Meakin and Suhs, Lee and Baeder) use
it. **Interpolation order is the error exponent:** a $q$-point Lagrange
formula (polynomial degree $q-1$) is accurate to $O(h^q)$ and is called
"order $q$", so linear interpolation is second order (Chesshire and
Henshaw). Benek et al. (1983) call their linear Taylor formula "first
order"; it is $q=2$ here, and pages write "linear ($q=2$)", never "first
order". The point mask $\iota$ carries the donor grid in its sign, as
Chesshire's `kr` does, because the 0/1 IBLANK of the Chimera sources
cannot tell a receptor from a hole or a field point; the unit normal
$\mathbf n$ is always outward (Henshaw prints it inward in places); total
energy per unit volume is $E$, never $e$, which is the error; time is
$t$, never $\tau$.

**Clashes kept on purpose.** $\alpha$ (angle of attack, unindexed; the
interpolation weights $\alpha_{\mathbf j}$ always carry the stencil index);
$r$ (the spherical radius on Yin–Yang pages, unindexed; the parameter
coordinates $r_m$ always carry their direction index or are bold
$\mathbf r$); $M$ (Mach number; the Yin–Yang matrices are sans-serif
$\mathsf M$, $\mathsf P$); $\delta$ (the Yin–Yang buffer angle, only on
Yin–Yang pages; $\delta_{ij}$ the Kronecker delta carries indices); $N$
(polynomial degree of element methods, reserved; point counts are always
subscripted, $N_m$, $N_{\mathrm{pts}}$). A page that needs both meanings
renames one locally and says so.

## 1. Grids, mappings and the composite grid

| Symbol | Meaning | Remark |
|---|---|---|
| $n_d$ | number of space dimensions | 2 or 3 |
| $\mathbf x=(x_1,\dots,x_{n_d})$ | physical coordinates | $(x,y,z)$ when written out |
| $\Omega$, $\partial\Omega$ | physical domain and its boundary | Chesshire's $D$ is translated |
| $G_k$, $k=1,\dots,n_g$ | component grid $k$; $n_g$ grids | logically rectangular unless the page says unstructured |
| $\mathcal G=\{G_k\}_{k=1}^{n_g}$ | composite (overset) grid | with the point classification of §2 |
| $\Omega_k\subset\Omega$ | subdomain covered by $G_k$ | $\Omega=\bigcup_k\Omega_k$ |
| $\Omega_{kk'}=\Omega_k\cap\Omega_{k'}$ | overlap region of $G_k$ and $G_{k'}$ | Wang's $O$ |
| $\ell(k)$ | hierarchy level of $G_k$, $\ell=1$ the background grid | Benek's $G_{\ell,i}$; embedded grids have larger $\ell$ |
| $\mathbf r=(r_1,\dots,r_{n_d})\in[0,1]^{n_d}$ | parameter (unit-square, unit-cube) coordinates | Chesshire's $(r,s)$; direction index $m=1,\dots,n_d$ |
| $\mathbf x=\mathbf d_k(\mathbf r)$, $\mathbf r=\mathbf d_k^{-1}(\mathbf x)$ | mapping of $G_k$ and its inverse | later literature: $\mathbf G_g(\mathbf r)$; time-dependent $\mathbf d_k(\mathbf r,t)$ in §6 |
| $\partial\mathbf x/\partial\mathbf r$, $\partial r_m/\partial x_n$ | mapping Jacobian matrix and its inverse (metric) | CMPGRD's `rsxy`; determinants written out |
| $\boldsymbol\xi=(\xi,\eta,\zeta)$ | curvilinear computational coordinates with unit index spacing | flow-solver form (§5); $\xi_m=r_m/\Delta r_m$ |
| $J=\det(\partial\boldsymbol\xi/\partial\mathbf x)$ | Jacobian (Pulliam–Steger) | $J^{-1}$ = cell volume; Lee's `InvJacob` = $J^{-1}$ |
| $\xi_x,\dots,\zeta_z$ | metric terms $\partial\xi/\partial x$, … | $\xi_t,\eta_t,\zeta_t$ time metrics (§6) |
| $\mathbf i=(i_1,\dots,i_{n_d})$ | grid-point multi-index | $(i,j)$ allowed in 2-D; **never** $(i,j,k)$, $k$ is the grid |
| $(\mathbf i,k)$, $\mathbf x^k_{\mathbf i}$ | point $\mathbf i$ of grid $k$, its position | |
| $N_m$, $N_{\mathrm{pts}}$ | points in direction $m$; total points of $\mathcal G$ | |
| $\Delta r_m$ | parameter spacing, $1/(N_m-1)$ | Henshaw's $1/(n_{m,b}-n_{m,a})$ |
| $h$, $h_k$ | representative physical spacing; of grid $k$ | $\Delta x$, $\Delta\theta$ when direction matters |
| $u^k_{\mathbf i}$, $u^{k,n}_{\mathbf i}$ | discrete value at $(\mathbf i,k)$; at time level $n$ | bold for vectors, $\mathbf U$ for the whole discrete field |

## 2. Point classification

| Symbol | Meaning | Remark |
|---|---|---|
| $\mathcal D_k$ | discretization points of $G_k$ (interior and boundary) | "field", "computed" points of Chimera papers |
| $\mathcal R_k$ | receptor points of $G_k$, values interpolated from another grid | synonyms: interpolation, fringe, intergrid-boundary, recipient, receiver points |
| $\mathcal H_k$ | hole (exterior, unused, blanked) points of $G_k$ | $G_k=\mathcal D_k\cup\mathcal R_k\cup\mathcal H_k$, disjoint |
| $\mathcal O_k\subset\mathcal R_k$ | orphan points: receptors with no valid donor | how a code then treats them is said per page |
| $\iota_k(\mathbf i)$ | point mask | $1$ on $\mathcal D_k$, $0$ on $\mathcal H_k$, $-k'$ on $\mathcal R_k$ with donor grid $k'$ |
| IBLANK, $i_b$ | the 0/1 mask of the Chimera sources (PLOT3D convention) | 1 field, 0 hole (and, in Benek 1985, fringe); translated to $\iota$ |
| $k'$ | donor grid of a receptor | the receptor grid is $k$ |
| $\mathcal S_{\mathbf i}\subset G_{k'}$ | donor stencil of receptor $(\mathbf i,k)$ | $q^{n_d}$ points; the donor cell is its central cell |
| $\mathbf r'=\mathbf d_{k'}^{-1}(\mathbf x^k_{\mathbf i})$ | receptor position in donor parameter coordinates | found by donor search (Newton on $\mathbf d_{k'}$) |
| $\mathbf s\in[0,1]^{n_d}$ | local coordinates of the receptor in the donor cell | Benek's $(\bar\xi,\bar\eta,\bar\zeta)$, Lee's $\mathbf s$, Henshaw's $s_m$ |
| $q$ | interpolation width: donor points per direction | CMPGRD's `iw`; may differ per direction and grid pair |
| $q_{\mathrm d}$ | discretization stencil width (points per direction) | 3 for second-order, 5 for fourth-order centred stencils |
| $d$ | overlap: distance between the innermost receptors of two overlapping grids | Chesshire's definition, not the geometric overlap of the grids |
| $n_f$ | number of fringe layers (receptor rows) at holes and outer boundaries | Rogers' "fringe level", Noack's FRINGE 1/2 |
| $\mathcal C$ | hole-cutting surface (hole boundary) | Benek's level curve $C$; a body surface or a constant-index surface |

## 3. Inter-grid interpolation

| Symbol | Meaning | Remark |
|---|---|---|
| $u^k_{\mathbf i}=\sum_{\mathbf j\in\mathcal S_{\mathbf i}}\alpha_{\mathbf j}u^{k'}_{\mathbf j}$ | interpolation equation at a receptor | Chesshire (5.3) |
| $\alpha_{\mathbf j}$ | interpolation weights | $\sum_{\mathbf j}\alpha_{\mathbf j}=1$ for a consistent formula |
| $L_j(s)$ | 1-D Lagrange basis on $q$ donor points | tensor product $\alpha_{\mathbf j}=\prod_mL_{j_m}(s_m)$; Henshaw's $q_i(s)$ |
| $\mathcal I_{k\leftarrow k'}$ | interpolation operator from $G_{k'}$ to the receptors of $G_k$ | linear map; its matrix is written with the same symbol |
| $p$ | order of accuracy of a discretization, error $O(h^p)$ | Chesshire's $2r$ |
| $q$-point, order $q$ | interpolation of width $q$, degree $q-1$, error $O(h^q)$ | linear: $q=2$; Henshaw's quartic: $q=5$ |
| $2s$ | order of the PDE (highest derivative) in the interpolation-order theory | Chesshire's $2p$ |
| explicit interpolation | donor stencils contain discretization points only | $\mathcal S_{\mathbf i}\subset\mathcal D_{k'}$; receptors updated directly |
| implicit interpolation | donor stencils may contain receptors | interpolation equations coupled, solved as a system |

## 4. Conservation and interfaces

| Symbol | Meaning | Remark |
|---|---|---|
| $V_c$, $\lvert V_c\rvert$ | cell (control volume) and its volume | Wang's $\Delta V$ |
| $f$, $S_f$, $\mathbf n_f$ | face, its area, its outward unit normal | |
| $\mathbf F_f$ | numerical normal flux through face $f$ (per unit area) | flux through the face: $\mathbf F_fS_f$ |
| $\Gamma_{k\mid k'}=\partial\Omega_k\cap\Omega_{k'}$ | part of the boundary of $\Omega_k$ lying inside $\Omega_{k'}$ | Wang's $\Gamma_{BO}$ with $k=B$, $k'=A$ |
| $\Gamma_{kk'}$ | interface (patch boundary) between two patched zones | conservative overset methods convert overlap into a patch |
| $W_f\in[0,1]$ | retained fraction of a face cut by an interface | Wang's area weights |
| $\varepsilon_{\mathrm c}$ | conservation defect: global imbalance of a conserved quantity | $\sum_c\lvert V_c\rvert\,\partial_t\mathbf q_c+\sum_{f\in\partial\Omega}\mathbf F_fS_f$; reported relative, per page |

## 5. Flow equations

| Symbol | Meaning | Remark |
|---|---|---|
| $\rho$, $\mathbf u=(u,v,w)$, $p$, $T$ | density, velocity, pressure, temperature | $u_m$ components; $p$ kinematic on incompressible pages |
| $E$ | total energy per unit volume | sources write $e$ |
| $\mathbf q=(\rho,\rho\mathbf u,E)^T$ | conserved variables | $\mathbf q_{\mathrm p}=(\rho,\mathbf u,p)^T$ primitive variables |
| $\partial_t\mathbf q+\nabla\cdot\mathbf F(\mathbf q)=\mathbf 0$ | conservation law | $\mathbf F=(\mathbf F_1,\mathbf F_2,\mathbf F_3)$; $\mathbf F^{\mathrm i}$, $\mathbf F^{\mathrm v}$ inviscid and viscous parts |
| $\hat{\mathbf q}=\mathbf q/J$ | transformed conserved variables | $\partial_t\hat{\mathbf q}+\partial_\xi\hat{\mathbf F}+\partial_\eta\hat{\mathbf G}+\partial_\zeta\hat{\mathbf H}=\mathbf 0$ |
| $\hat{\mathbf F}=J^{-1}(\xi_t\mathbf q+\xi_x\mathbf F_1+\xi_y\mathbf F_2+\xi_z\mathbf F_3)$ | transformed flux in $\xi$ | $\hat{\mathbf G}$, $\hat{\mathbf H}$ likewise with $\eta$, $\zeta$ |
| $U,V,W$ | contravariant velocities, $U=\xi_t+\xi_xu+\xi_yv+\xi_zw$ | unscaled |
| $\nabla\cdot\mathbf u=0$, $\partial_t\mathbf u+(\mathbf u\cdot\nabla)\mathbf u+\nabla p=\nu\nabla^2\mathbf u+\mathbf f$ | incompressible equations | velocity–pressure form with a pressure Poisson equation, said per page |
| $\mu$, $\nu=\mu/\rho$, $\lambda=-\tfrac23\mu$ | dynamic, kinematic, second viscosity | |
| $\gamma$, $Pr$, $Re$, $M$ | ratio of specific heats, Prandtl, Reynolds, Mach numbers | $M_\infty$, $Re_\infty$ free stream; reference length per page |
| $a$, $\alpha$, $C_p$ | speed of sound, angle of attack, pressure coefficient | $c_p$ specific heat at constant pressure |
| $D_{+m}$, $D_{-m}$, $D_{0m}$ | forward, backward, centred divided differences in direction $m$ | undivided differences say so; $E_{\pm m}$ shifts |
| $\nabla_p$, $\nabla_p\cdot$, $\nabla^2_p$ | $p$th-order discrete gradient, divergence, Laplacian | Henshaw's $\nabla_4$, $\Delta_4$ |
| $\mathbf f$ | body force; the twilight-zone forcing | |
| $u_{\mathrm{ex}}$, $e=u_{\mathrm{ex}}-u$ | exact (manufactured) solution and error | $\lVert e\rVert_\infty$, $\lVert e\rVert_2$ |
| $\sigma$ | observed convergence rate, $\lVert e\rVert\propto h^\sigma$ | |
| $\mathbf f^{\mathrm E}$, $\mathbf f^{\mathrm I}$ | explicit and implicit parts of the semi-discrete right side | IMEX schemes |
| $\Delta t$, $n$ | time step, time level (superscript) | |

## 6. Grid motion

| Symbol | Meaning | Remark |
|---|---|---|
| $\mathbf x=\mathbf d_k(\mathbf r,t)$ | mapping of a moving or deforming component grid; the parameter space $[0,1]^{n_d}$ stays fixed | Henshaw & Schwendeman's $\mathbf G_g(\mathbf r,t)$, Banks et al.'s $g(r,t)$ |
| $\mathbf u_g=\partial_t\mathbf x\rvert_{\boldsymbol\xi}$ | grid velocity | $=\partial_t\mathbf d_k(\mathbf r,t)$ at fixed $\mathbf r$; $\xi_t=-\mathbf u_g\cdot\nabla\xi$, likewise $\eta_t$, $\zeta_t$ |
| $\mathbf x_{\mathrm{cg}}(t)$, $\mathbf v_{\mathrm{cg}}$ | centre-of-gravity position and velocity of a rigid body | |
| $\mathsf R(t)$ | rotation matrix, body to inertial frame | $\mathbf x=\mathbf x_{\mathrm{cg}}+\mathsf R(\mathbf X-\mathbf X_{\mathrm{cg}})$, $\mathbf X$ body-frame coordinates |
| $\boldsymbol\omega_b$ | angular velocity of the body | |
| $m_b$, $\mathsf I_b$ | body mass, inertia tensor | |
| $\boldsymbol{\mathcal F}$, $\boldsymbol{\mathcal M}$ | aerodynamic plus external force and moment on the body | six-degree-of-freedom (6-DOF) equations; Euler angles or quaternions per page |
| $k_{\mathrm r}$ | reduced frequency | Meakin's $\tilde K$; reference length per page |

## 7. Spherical (Yin–Yang) grids

| Symbol | Meaning | Remark |
|---|---|---|
| $(r,\theta,\phi)$ | radius, colatitude $\theta\in[0,\pi]$, longitude | |
| $r_{\mathrm{in}}$, $r_{\mathrm{out}}$ | inner and outer radii of a spherical shell | Kageyama's $r_i$, $r_o$ |
| superscripts $\mathrm n$, $\mathrm e$ | Yin and Yang component grids | upright, never italic $n$ (time level) or $e$ (error) |
| $\delta$ | buffer angle extending each component beyond half coverage | component: $\theta\in[\pi/4-\delta,3\pi/4+\delta]$, $\phi\in[-3\pi/4-\delta,3\pi/4+\delta]$ |
| $\Delta\theta$, $\Delta\phi$, $N_\theta$, $N_\phi$ | angular spacings and point counts of a component | |
| $\mathsf M$ | Cartesian Yin→Yang matrix, $(x^{\mathrm e},y^{\mathrm e},z^{\mathrm e})^T=\mathsf M(x^{\mathrm n},y^{\mathrm n},z^{\mathrm n})^T$ | $\mathsf M^{-1}=\mathsf M$, $\det\mathsf M=+1$ |
| $\psi$ | local angle between the Yin and Yang horizontal bases | position dependent |
| $\mathsf P$ | Yin→Yang matrix of spherical vector components $(v_r,v_\theta,v_\phi)$ | orthogonal, $\mathsf P^{-1}=\mathsf P^T$ |

## 8. Reserved for later chunks

Reserved symbols: a page that first uses one confirms it here (removing
"reserved") and logs it.

| Symbol | Meaning | Remark |
|---|---|---|
| $N$ | polynomial degree of DG and spectral-element methods | in use (DG on overlapping grids); order of accuracy then $p=N+1$ when the page shows it |
| $\mathsf H$ | SBP norm (mass) matrix, symmetric positive definite | reserved |
| $\mathsf D=\mathsf H^{-1}\mathsf Q$, $\mathsf Q+\mathsf Q^T=\mathsf B$ | SBP first-derivative operator and its summation-by-parts property | reserved; $\mathsf B=\mathrm{diag}(-1,0,\dots,0,1)$ in 1-D |
| $\Sigma$ | SAT penalty (scalar or matrix) | in use (overset well-posedness: $\Sigma_u$, $\Sigma_v$, $\Sigma^m$) |
| $\lVert u\rVert_{\mathsf H}^2=u^T\mathsf Hu$ | discrete energy | reserved |
| $\mathcal I_{k\leftarrow k'}$ (matrix) | interpolation operator in SBP-compatible form | reserved use of §3's symbol; the norm-compatibility condition is written as the source states it |
| $\omega_r$, $\beta_r$ | nonlinear (WENO) weights and smoothness indicators of candidate stencil $r$ | in use (DG overset coupling) |
| $\chi$ | solid indicator or volume fraction of an immersed body | reserved |
| $\varphi$ | signed distance (level set) to a body surface or to a fluid interface | in use (multiphase flow); $\varphi<0$ inside the body |
| $d_w$ | wall distance (wall-distance-based hole cutting) | in use (wall-distance hole cutting) |
| $\mathbf f_{\mathrm{IB}}$ | immersed-boundary forcing | reserved |

## 9. Shared page-local symbols

Symbols that only a few pages use, registered here so that two pages do
not give them different meanings.

| Symbol | Meaning | Remark |
|---|---|---|
| $\mathbf j_0$, $(\Delta x,\Delta y)=\mathbf x^k_{\mathbf i}-\mathbf x^{k'}_{\mathbf j_0}$ | donor point of the linear Taylor formula of Benek et al. (1983) and the receptor's offset from it | inter-grid interpolation, PEGASUS; here $\Delta x$ is an offset, not the spacing of §1 |
| $\vartheta_{\mathbf i}$ | discrete divergence of the velocity at point $\mathbf i$ | incompressible flow (Henshaw 1994) |
| $\mathcal T_{\mathbf i}$ | truncation-error forcing of the transport equation of $\vartheta_{\mathbf i}$, $O(h^4)$ | incompressible flow (Henshaw 1994) |
| $\mathcal V_{\mathbf i}=\sum_m\Delta x_{m,\mathbf i}^{-2}$, $C_d$ | spacing factor and coefficient of the divergence-damping term $-C_d\nu\mathcal V_{\mathbf i}\vartheta_{\mathbf i}$ | incompressible flow (Henshaw 1994) |
| $\varsigma$ | multiplier of the compatibility condition of the singular Neumann pressure system | incompressible flow (Henshaw 1994) |
| $\mathcal J=\det(\partial\mathbf x/\partial\mathbf r)$ | Jacobian determinant of the mapping $\mathbf d_k$ with respect to the parameter coordinates: the area (volume) factor of $G_k$ | **not** the Pulliam–Steger $J$ of §1: $\mathcal J=J^{-1}/\prod_m\Delta r_m$, because $\xi_m=r_m/\Delta r_m$; moving grids (Henshaw & Schwendeman 2006), Maxwell (Henshaw 2006) |
| $G_{k_r}$, $\mathbf d_{k_r}(\mathbf r,t)=\mathbf d_k(\mathbf R_{k_r}(\mathbf r),t)$, $\mathbf R_{k_r}$ | refinement grid on base grid $G_k$, its mapping, and the affine restriction map of $[0,1]^{n_d}$ into the base grid's parameter space | italic subscript $r$; the upright $k_{\mathrm r}$ is the reduced frequency of §6; AMR on overlapping grids (Henshaw & Schwendeman 2006) |
| $\kappa_h$, $\kappa_{h,\mathbf i}$ | cell-size ratio of substrate to patch: global (the maximum over the patch receptors) and local (receptor cell $\mathbf i$ of the patch) | Picard et al.'s $\chi$, $\chi_i^{\mathcal V}$ ($\chi$ is reserved, §8); $\kappa_h>1$ means a finer patch; shock capturing (Picard et al. 2021) |
| $\kappa$ | scalar coefficient of the generalized Laplacian $\nabla\cdot(\kappa\nabla w)$; $\kappa_{\mathrm T}$ the diffusivity of a scalar proxy equation | Henshaw's (2006) $k$; Sharma et al.'s $\kappa$; Maxwell, twilight-zone flow |
| $\varpi$ | spatial frequency of trigonometric manufactured (twilight-zone) solutions | Henshaw's (1994) $f$; twilight-zone flow |
| $\Omega_u$, $\Omega_v$, $\Omega_O$; $u$, $v$ | two overlapping subdomains, their overlap ($=\Omega_{kk'}$); the solutions on them | overset well-posedness (Kopriva et al. 2022), DG overset coupling |
| $\eta\in(0,1)$ | overlap weight of the energy and of the penalties | overset well-posedness; not the computational coordinate $\eta$ of §1, which that page does not use |
| $A^\pm$ | positive and negative parts of a symmetric coefficient matrix | overset well-posedness |
| $F$ | fluid volume fraction of a two-phase model | multiphase flow; distinct from the immersed-body $\chi$ |
