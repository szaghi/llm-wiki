---
type: Method
title: "Adaptive moving mesh finite differences"
description: "An r-adaptive scheme moves a fixed number of grid points, by variational redistribution with a monitor function, a prescribed mesh Jacobian or an optimal-transport Monge–Ampère map, and discretizes the conservation law on the moving or adapted mesh; the sources make it entropy stable, fast or shock-resolving and measure its cost against uniform meshes."
status: established
aliases: [moving mesh method, r-adaptivity, adaptive moving mesh, mesh redistribution, MM-WENOMR, MM-O5, MM-O6, smooth adaptive meshing, SAM, SAM-ALE, optimal-transport mesh adaptation, Monge–Ampère mesh adaptation]
tags: [finite-difference, entropy-stable, multiphase, relativistic, weno, moving-mesh]
timestamp: 2026-10-23T23:50:00Z
---

# Adaptive moving mesh finite differences

An adaptive moving mesh scheme keeps the number and connectivity of the
grid points fixed and moves them towards the features of the solution
(r-adaptivity). The solution is computed on a uniform mesh in page-local
computational coordinates $\xi=(\xi_1,\xi_2,\xi_3)$, mapped to the physical
mesh by $x=x(\xi,\tau)$ with $t=\tau$. At each time step two problems are
solved: a mesh-redistribution problem gives the new mesh, and the
conservation law, written in the moving curvilinear coordinates, advances
the solution. Two sources of this bundle build the high-order
entropy-stable version of the scheme:

- [Duan & Tang (2022)](/sources/duan-2022.md) for the special-relativistic
  hydrodynamics and MHD equations
  ([relativistic hydrodynamics](/definitions/relativistic-hydrodynamics.md)),
  in 2D and 3D, extending their own second-order entropy-stable
  moving-mesh schemes to arbitrary even order for the entropy-conservative
  flux (§1);
- [Li, Duan & Tang (2022)](/sources/li-2022-c.md), who carry the same
  construction to single- and two-component Euler equations with a
  stiffened-gas law (§1;
  [stiffened-gas equation of state](/definitions/stiffened-gas-equation-of-state.md),
  [multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)).

Li, Duan & Tang state several of their discrete properties with reference
to Duan & Tang; the proofs for the high-order finite-difference case are
those of Duan & Tang (2022), as recorded below.

A third source, [Ramani & Shkoller (2023)](/sources/ramani-2023.md),
builds the mesh differently: it prescribes the Jacobian determinant of the
mesh map instead of solving variational redistribution equations, and
couples the mesh to a simplified finite-difference WENO
arbitrary-Lagrangian–Eulerian (ALE) solver (section "Jacobian-prescribed meshes" below).
A fourth, [Nguyen et al. (2024)](/sources/nguyen-2024.md), moves the nodes
of a steady high-order HDG solution with an optimal-transport map
(section "Optimal-transport meshes" below).

## The conservation law in moving coordinates

With $J=\det\partial(t,x)/\partial(\tau,\xi)$ and the metric terms
$J\partial_t\xi_k$ and $J\partial_{x_j}\xi_k$, the law
$\partial_tu+\sum_j\partial_{x_j}f^{(j)}(u)=0$ becomes (Li, Duan & Tang,
Eq. (2.2); Duan & Tang, Eq. (2.8))

$$\frac{\partial(Ju)}{\partial\tau}+\sum_k\frac{\partial}{\partial\xi_k}\Big(J\frac{\partial\xi_k}{\partial t}\,u+\sum_jJ\frac{\partial\xi_k}{\partial x_j}\,f^{(j)}(u)\Big)=0 .$$

For relativistic MHD, Duan & Tang add on the right-hand side the
symmetrizing source $-\Phi'(w)^\top\sum_k\partial_{\xi_k}\big(\sum_jJ\partial_{x_j}\xi_k B_j\big)$
of the Godunov–Powell type, with page-local $\Phi$ a function of the entropy
variables homogeneous of degree one, so that the entropy pair is an entropy
pair of the modified system (§2, Eqs. (2.4)–(2.5), (2.8); see
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)).
The law holds together with the geometric conservation laws (Li, Duan &
Tang, Eq. (2.3); Duan & Tang, Eq. (2.9)):

- the volume conservation law (VCL),
  $\partial_\tau J+\sum_k\partial_{\xi_k}(J\partial_t\xi_k)=0$;
- the surface conservation laws (SCLs),
  $\sum_k\partial_{\xi_k}(J\partial_{x_j}\xi_k)=0$ for every $j$.

Under them, constant states are exact solutions and the entropy satisfies
$\partial_\tau(J\eta)+\sum_k\partial_{\xi_k}\big(J\partial_t\xi_k\,\eta+\sum_jJ\partial_{x_j}\xi_k\,F^{(j)}_\eta\big)\le0$,
with equality for smooth solutions (Duan & Tang, Eqs. (2.10)–(2.11); the
derivation is deferred to their second-order paper).

The scheme is a [conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
in $\xi$ for the point values $(Ju)_i$ and for $J_i$ (Li, Duan & Tang,
Eqs. (3.1)–(3.2); Duan & Tang, Eqs. (3.4)–(3.5)). Both papers meet the
discrete GCLs the same way:

- the spatial metrics $J\partial_{x_j}\xi_k$ are written in conservative
  cross-product form and discretized with the same central difference
  operator as the entropy-conservative flux (Li, Duan & Tang, Eq. (3.9)).
  Duan & Tang prove that the discrete SCLs then hold exactly, because the
  directional central-difference operators commute (§3.3, Eqs.
  (3.15)–(3.17), after the conservative metric method of Thomas &
  Lombard);
- the temporal metrics are computed from the mesh velocity $\dot x$ as
  $J\partial_t\xi_k=-\sum_j\dot x_j\,J\partial_{x_j}\xi_k$ (Li, Duan & Tang,
  Eq. (3.10); Duan & Tang, Eq. (3.18)), and $J$ is advanced by the
  discrete VCL with the same flux combination.

Duan & Tang prove that the fully discrete scheme with explicit SSP
Runge–Kutta then preserves free streams (Prop. 3.2), and Li, Duan & Tang
state the same for their scheme with reference to Duan & Tang (Remark 3.1);
see [free-stream preservation](/properties/free-stream-preservation.md). As
recalled by Li, Duan & Tang, failing the discrete GCLs misrepresents the
convective velocities and creates spurious sources and sinks (§3.2).

## Entropy-stable fluxes on a moving mesh

**Entropy conservation.** A consistent two-point flux $\hat F_k$ in
direction $k$ makes the scheme entropy-conservative if (Li, Duan & Tang,
Prop. 3.1; Duan & Tang, Def. 3.1, Eq. (3.1))

$$[\![w]\!]\cdot\hat F_k=\{\!\{J\partial_t\xi_k\}\!\}\,[\![\phi]\!]+\sum_j\{\!\{J\partial_{x_j}\xi_k\}\!\}\Big([\![\psi^{(j)}]\!]-\{\!\{B_j\}\!\}\,[\![\Phi]\!]\Big).$$

Here page-local $\phi=w\cdot u-\eta$ is the entropy potential and
$\psi^{(j)}$ the registry's flux potentials; the last term is present only
for relativistic MHD (Duan & Tang), and with $B\equiv0$ the condition is the
one of Li, Duan & Tang. It reduces to the Cartesian condition when the mesh
does not move. Both papers satisfy it with

$$\hat F_k=\{\!\{J\partial_t\xi_k\}\!\}\,\tilde u+\sum_j\{\!\{J\partial_{x_j}\xi_k\}\!\}\,f^{\mathrm{ec},(j)},$$

where the Cartesian flux $f^{\mathrm{ec},(j)}$ satisfies the Cartesian
condition and the page-local "entropy-conservative state" $\tilde u$
satisfies $[\![w]\!]\cdot\tilde u=[\![\phi]\!]$ (Li, Duan & Tang, Eqs.
(3.11)–(3.12); Duan & Tang, Eqs. (3.2)–(3.3)). Duan & Tang give an explicit
$\tilde u$ for relativistic MHD in arithmetic and
[logarithmic means](/operators/logarithmic-mean.md) (§3.1). The explicit
fluxes are on
[entropy-conservative two-point fluxes](/methods/entropy-conservative-flux.md).

**High order.** The two-point flux is raised to even order $2n_{\mathrm o}$
(page-local $n_{\mathrm o}\ge1$) by the LeFloch–Mercier–Rohde linear
combination of two-point fluxes over a widening stencil, and the same
combination discretizes the metrics, the VCL and the MHD source term (Duan
& Tang, Prop. 3.1, Eqs. (3.6)–(3.12)); details on
[flux differencing](/methods/flux-differencing.md). Duan & Tang prove that
the semi-discrete scheme is then of order $2n_{\mathrm o}$ in space and
entropy conservative with an explicit numerical entropy flux (Thm. 3.2,
Eqs. (3.20)–(3.27)).

**Entropy stability.** The interface flux adds to the high-order
entropy-conservative flux a dissipation on jumps of WENO reconstructions
of rotated, scaled entropy variables, with a componentwise sign switch.
This is a [TeCNO-type flux](/methods/tecno-scheme.md). The two papers differ
in the reconstruction of the dissipation:

- Duan & Tang use fifth-order WENO-JS on the sixth-order
  entropy-conservative flux and prove the semi-discrete entropy inequality
  (Thm. 4.1). Their schemes are named MM-O6 (sixth-order entropy
  conservative) and MM-O5 (fifth-order entropy stable); UM-O5 is the same
  entropy-stable scheme on a static uniform mesh and MM-O2 their
  second-order moving-mesh scheme (§6);
- Li, Duan & Tang use multi-resolution WENO (Eq. (3.21)). Their scheme is
  MM-WENOMR; MM-WENOJS uses WENO-JS in the dissipation and UM-WENOMR is the
  same scheme on a uniform mesh (§5).

## Mesh redistribution

The new mesh solves variational redistribution equations, the
Euler–Lagrange equations of a mesh functional of the Winslow variable-
diffusion type (Li, Duan & Tang, Eq. (4.1); Duan & Tang, Eqs. (5.1)–(5.2)),

$$\nabla_\xi\cdot\big(\Pi\,\nabla_\xi x_k\big)=0,\qquad k=1,2,3,$$

with a scalar monitor function $\Pi$ (page-local, as are $\mathsf s_k$ and
$\mathsf a_k$ below). The two papers use different monitors:

- Duan & Tang (Eq. (5.3)) use one physical variable $\mathsf s$ (often
  $\ln\rho$) with amplitude $\mathsf a>0$, and the gradient ratio is not
  squared:
  $$\Pi=\Big(1+\mathsf a\,\frac{\lvert\nabla_\xi\mathsf s\rvert}{\max\lvert\nabla_\xi\mathsf s\rvert}\Big)^{1/2};$$
  the vortex test adds a Laplacian term,
  $\Pi=\big(1+20\lvert\nabla_\xi\rho\rvert/\max\lvert\nabla_\xi\rho\rvert+10\lvert\Delta_\xi\rho\rvert/\max\lvert\Delta_\xi\rho\rvert\big)^{1/2}$
  (Eq. (6.3)), and the Riemann, blast and shock–cloud tests use
  $\mathsf a=1200$ or $800$ (§6);
- Li, Duan & Tang (Eq. (4.2)) use $n_{\mathrm m}$ chosen variables
  $\mathsf s_k$ with weights $\mathsf a_k\ge0$, and square the ratios:
  $$\Pi=\Big(1+\sum_{k=1}^{n_{\mathrm m}}\mathsf a_k\Big(\frac{\lvert\nabla_\xi\mathsf s_k\rvert}{\max\lvert\nabla_\xi\mathsf s_k\rvert}\Big)^2\Big)^{1/2}.$$

These are design choices of each paper; neither source compares them. The
algorithm is the same in both (Li, Duan & Tang, §4; Duan & Tang, §5):

1. Discretize the redistribution equations by second-order central
   differences and take ten Jacobi iterations from the current mesh,
   with interface values $\Pi_{i\pm1/2}$ the averages of neighbouring
   values.
2. Smooth $\Pi$ by a low-pass filter with weights
   $(1/2)^{\lvert j_1\rvert+\lvert j_2\rvert+\lvert j_3\rvert+3}$ over the
   27-point neighbourhood, 3 to 5 times (Duan & Tang, Remark 5.1) or 3 to
   10 times (Li, Duan & Tang, Remark 4.1).
3. Move the mesh by a limited fraction of the Jacobi displacement, so that
   no point passes half the distance to its neighbour in one step.
4. Set the mesh velocity $\dot x$ to the actual displacement divided by
   $\Delta t$.

The monitor of Li, Duan & Tang carries more variables for two components.
Their two-component shock–bubble test with a stiffened gas uses five: a
schlieren function, a variable printed $u$ and never defined (the velocity
is $v$ throughout the paper), the two partial densities and the pressure,
with weights $(600,500,1200,1200,1200)$ (Ex. 5.9). They state that the
multi-component equations need more solution information in the monitor
than the single-component ones to give a good mesh (§1). They show no
ablation of this choice.

## Cost and accuracy

The time step is $\Delta t\le C_{\mathrm{CFL}}/\max_i\sum_k\varrho_{i,k}/\Delta\xi_k$,
with $\varrho_{i,k}$ the spectral radius in direction $k$ (page-local; for
relativistic MHD that of the flux Jacobian plus the source term),
$C_{\mathrm{CFL}}=0.4$ in 2D and $0.3$ in 3D, and SSP-RK3 (Li, Duan & Tang,
Eq. (5.1); Duan & Tang, Eq. (6.1)). The accuracy tests shrink the time step
so that the spatial error dominates:

- Li, Duan & Tang use $\Delta t\propto(\min\Delta\xi_k)^{5/3}$ and observe
  fifth order on the moving mesh for the 2D vortex ($t=4$, $N_x=40$ to
  $320$) and for the 3D vortex rotated to the domain diagonal ($t=0.1$)
  (Ex. 5.1, 5.5);
- Duan & Tang use $\Delta t\propto\Delta\xi_1^2$ for MM-O6 and
  $\Delta\xi_1^{5/3}$ for MM-O5 on the relativistic MHD vortex. MM-O6
  reaches sixth order on a prescribed moving mesh and MM-O5 fifth order on
  the adaptive mesh, in 2D ($t=4$) and 3D ($t=0.1$) (Ex. 6.1, 6.7). The
  discrete total entropy stays constant for MM-O6 and decays for MM-O5
  (Figs. 6.4, 6.14).

The vortices are described on
[isentropic vortex](/benchmarks/isentropic-vortex.md).

The moving-mesh runs match or beat uniform meshes with two to four times
as many points per direction, at a fraction of their CPU time. Li, Duan &
Tang (Tables 5.1–5.3) and Duan & Tang (Tables 6.1–6.2, Exs. 6.2–6.10), all
on Intel Xeon E5-2697A V4 nodes:

| source | test | moving mesh | uniform reference | CPU ratio |
|---|---|---|---|---|
| Li, Duan & Tang | 2D Riemann problem I | $200^2$, 2 min 56 s | $500^2$, 7 min 9 s | 41.0 % |
| Li, Duan & Tang | 2D Riemann problem II | $200^2$, 2 min 50 s | $600^2$, 13 min 10 s | 21.5 % |
| Li, Duan & Tang | 3D spherical shock tube | $100^3$, 13 min 53 s | $200^3$, 37 min 19 s | 37.2 % |
| Li, Duan & Tang | tri-point problem | $350\times150$, 3 min 21 s | $1050\times450$, 18 min 7 s | 18.9 % (printed) |
| Li, Duan & Tang | 2D shock–helium bubble | $800\times160$, 1 h 4 min | $2400\times480$, 4 h 4 min | 26.2 % |
| Li, Duan & Tang | 2D shock–bubble, stiffened gas | $800\times160$, 9 min 28 s | $2400\times480$, 40 min 11 s | 23.6 % |
| Li, Duan & Tang | 3D shock–helium bubble | $400\times80^2$, 11 h 6 min | $800\times160^2$, 38 h 2 min | 29.2 % |
| Li, Duan & Tang | 3D shock–bubble, stiffened gas | $400\times80^2$, 2 h 9 min | $800\times160^2$, 11 h 58 min | 18.0 % |
| Duan & Tang | RHD Riemann problem I | $200^2$, 1 min 2 s | $500^2$, 5 min 49 s | 17.8 % |
| Duan & Tang | RHD Riemann problem II | $200^2$, 1 min 25 s | $500^2$, 4 min 38 s | 30.6 % |
| Duan & Tang | RHD Riemann problem III | $200^2$, 1 min 16 s | $600^2$, 9 min 16 s | 13.7 % |
| Duan & Tang | 2D RMHD blast | $150^2$, 2 min 3 s | $600^2$, 28 min 14 s | 7.26 % |
| Duan & Tang | 2D RMHD shock–cloud | $210\times150$, 4 min 16 s | $560\times400$, 40 min 28 s | 10.5 % |
| Duan & Tang | 3D RHD spherical Riemann problem | $100^3$, 5 min 40 s | $200^3$, 41 min 8 s | 13.8 % |
| Duan & Tang | 3D RHD shock–bubble | $325\times90^2$, 2 h 14 min 44 s | $650\times180^2$, 12 h 34 min 43 s | 17.8 % |
| Duan & Tang | 3D RMHD shock–cloud | $210\times150^2$, 3 h 9 min 57 s | $420\times300^2$, 34 h 46 min 49 s | 9.06 % (printed) |

The tests are listed on
[two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md),
[Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md),
[shock–bubble interaction](/benchmarks/shock-bubble-interaction.md) and
[MHD blast wave](/benchmarks/mhd-blast-wave.md). Both papers judge the
moving-mesh result superior or comparable in every case. Duan & Tang
further compare the fifth-order moving mesh with their second-order
moving-mesh scheme at comparable CPU time: MM-O5 on $150^2$ (29 s, 35 s,
32 s) beats MM-O2 on $200^2$ (30 s, 38 s, 39 s) on the three RHD Riemann
problems, and on the 3D shock–bubble MM-O5 gives sharper bubble interfaces
than MM-O2, "since the high-order accurate scheme has lower dissipation"
(Exs. 6.2–6.4, 6.9).

On equal point counts a moving-mesh run costs about 4 to 7 times a
uniform-mesh run in Li, Duan & Tang, for example 2 min 56 s against 28 s on
Riemann problem I and 11 h 6 min against 2 h 34 min on the 3D helium bubble
*(compiler check, not in the sources: ratios of the printed timings)*; in
Duan & Tang the 2D blast costs 2 min 3 s against 30 s on $150^2$ (Table
6.1). Replacing WENO-JS by multi-resolution WENO in the dissipation
resolves more small-scale structure "with a slight increase in the
computational cost" (Li, Duan & Tang, Remark 3.2); the printed timings give
0.1 % to 12 % more *(compiler check, not in the sources)*.

## Jacobian-prescribed meshes: smooth adaptive meshing

[Ramani & Shkoller (2023)](/sources/ramani-2023.md) argue that the
bottleneck of moving-mesh hydrodynamics is the cost of mesh generation, not
the discretization of the flow equations (§1; arXiv v2). Their smooth
adaptive meshing (SAM) builds the mesh map $\mathsf X:\Omega_{\mathrm{ref}}\to\Omega$
(page-local, as are $\mathsf G$, $\Phi_{\mathrm S}$, $\mathsf w$, $\mathsf Y$,
$\tau_{\mathrm p}$, $\mathsf P$, $N_{\mathrm c}$ and $\Lambda$ below) from a uniform reference mesh by prescribing
its Jacobian through a target cell-size function $\mathsf G$ on the
physical domain:

$$\det\nabla_\xi\mathsf X(\xi)=\mathsf G\big(\mathsf X(\xi)\big)\ \text{in }\Omega_{\mathrm{ref}},\qquad \mathsf X(\xi)\cdot n=\xi\cdot n\ \text{on }\partial\Omega_{\mathrm{ref}},$$

a Monge–Ampère-type equation with no-penetration (tangential slip) boundary
conditions and fixed corners, solvable iff $\int_\Omega1/\mathsf G\,dx=\lvert\Omega\rvert$
(Eqs. (7)–(9)). Small $\mathsf G$ compresses cells. The solution is unique in
1D and not unique for $d\ge2$; optimal transport (Monge–Kantorovich, MK)
selects the map of least $L^2$ displacement (§3.1).

**Static SAM (Algorithm 1)** is a version of the Dacorogna–Moser
deformation method: after normalizing $\mathsf G$ to meet the solvability
condition, solve one Neumann Poisson problem
$\Delta\Phi_{\mathrm S}=1/\mathsf G-1$, $\nabla\Phi_{\mathrm S}\cdot n=0$, and
transport the identity map in a pseudo-time $\tau_{\mathrm p}\in[0,1]$,

$$\partial_{\tau_{\mathrm p}}\mathsf Y+\mathsf w\cdot\nabla\mathsf Y=0,\quad\mathsf Y(\xi,0)=\xi,\qquad \mathsf w=\frac{\nabla\Phi_{\mathrm S}}{\tau_{\mathrm p}+(1-\tau_{\mathrm p})/\mathsf G},$$

with $\mathsf X=\mathsf Y(\cdot,1)$ (Eqs. (10)–(14); the source's flowmap $\eta$
and pseudo-time $\tau$). Ramani & Shkoller prove that
this map solves the prescribed-Jacobian problem by showing that a weighted
Jacobian of the back-to-labels map is constant in $\tau_{\mathrm p}$ (§3.2.1); existence on
rectangles is asserted, not shown (§3.2.2). The Poisson problem is solved by
FFT on a symmetrically doubled domain, the transport by fifth-order linear
upwind differences and RK4 with a pseudo-time CFL of 2 (§3.3). The Eulerian
transport avoids the interpolation of Lagrangian versions of the method,
which the authors credit with "an order of magnitude speed-up" (§3.2.2).

- **Accuracy.** When the target satisfies $\nabla\mathsf G\cdot n=0$ on the
  boundary, the Jacobian error converges at fourth order: from
  $2.85\times10^{-2}$ on $32^2$ to $9.89\times10^{-8}$ on $1024^2$, observed
  orders 2.5 to 4.3 (Table 1). Without the Neumann condition the symmetric
  extension of $\mathsf G$ is only Lipschitz, and the Jacobian converges at
  order 1.5; a tanh boundary smoothing restores it (§3.3.2, App. B). The
  authors state that "all other grid generation schemes are at best 2nd
  order accurate" (§3.4.2).
- **Against MK.** On the Delzanno et al. target $2+\cos(8\pi r)$, SAM with
  the boundary-smoothed target has smaller Jacobian error than MK at every
  resolution ($3.25\times10^{-4}$ against $3.67\times10^{-4}$ on $256^2$), and
  its $L^2$ mesh displacement, $0.0178$, is close to MK's optimal $0.0174$.
  With the unsmoothed target SAM falls to order about 1.75 and its errors
  exceed MK's on $128^2$ and $256^2$ (Table 2). SAM is reported "almost 200
  times faster" than MK on $256^2$ (0.042 s against 8.636 s); the MK times
  are taken from Delzanno et al. and divided by a machine factor of 2.2
  measured on a third method, so the comparison is not a same-machine run
  of both codes (Table 3, App. C.1).
- **Dynamic SAM (Algorithm 2).** For a time-dependent target the map is
  updated by composition, $\mathsf X_{k+1}=\mathsf X_k\circ\delta\mathsf X_{k+1}$,
  where the near-identity map $\delta\mathsf X_{k+1}$ solves the same static
  problem on $\Omega_{\mathrm{ref}}$ with target
  $\mathsf P_{k+1}=(\mathsf G_{k+1}/\mathsf G_k)\circ\mathsf X_k$ (Eqs.
  (25)–(27)). Under a physical CFL condition $\Delta t\sim N_{\mathrm c}^{-1/2}$ in 2D
  ($N_{\mathrm c}$ cells), $\lVert1-1/\mathsf P\rVert_{L^\infty}=O(\Delta t)$, so the
  pseudo-time step stays $O(1)$ and one mesh update costs $O(N_{\mathrm c})$, against
  $O(N_{\mathrm c}^{3/2})$ for static SAM (§4.1.2, §4.2.2, Eq. (29)). Composition
  accumulates distortion; the restarted variant (Algorithm 3) recomputes
  the map by static SAM when an $L^1$ distortion measure exceeds $\Lambda$
  times its reference ($\Lambda=1.01$ or $1.003$, §4.3, §5).

**SAM-ALE solver.** The Euler equations are written on $\Omega_{\mathrm{ref}}$
in ALE conservation form for $(J\rho,J\rho v,JE)$ with the cofactor metrics
and the mesh velocity, and the geometric conservation law
$\partial_tJ-\partial_{\xi_j}(\text{cofactor}\cdot\partial_t\mathsf X)=0$ is
appended as a fifth conserved equation, so $J$ is evolved by the scheme and
not recomputed from the determinant (§6.1.3, Eqs. (44)–(46)). The flux is a
simplified [conservative finite-difference](/definitions/conservative-finite-difference-scheme.md)
form on point values: each transported variable is reconstructed at the
half point by fifth-order WENO-JS, upwinded on the sign of the
interpolated transport velocity, and multiplied by that velocity; the
velocity and pressure use the fourth-order linear average
$(-\mathsf b_{i-1}+7\mathsf b_i+7\mathsf b_{i+1}-\mathsf b_{i+2})/12$ of a quantity $\mathsf b$ (page-local); there is no
characteristic decomposition and no Riemann solver, and stability comes
from the authors' C-method [artificial viscosity](/methods/artificial-viscosity.md)
(Eqs. (47)–(51), Remark 1, App. A). The metrics are fourth-order central
differences of $\mathsf X$. A moving contact is tracked by an explicit
interface curve advected in ALE coordinates (§6.2.2). The authors state that
"many standard schemes (including WENO) fail to preserve the free-stream" on
dynamic adaptive meshes (§6.1.3); theirs keeps
$\lVert\rho-1\rVert_{L^\infty}=9.10\times10^{-14}$ at $T=80$ on an oscillating
$50\times50$ mesh ([free-stream preservation](/properties/free-stream-preservation.md),
§6.2.1).

**Speed-ups.** On the 2D [Noh implosion](/benchmarks/noh-implosion-problem.md) ($\gamma=5/3$, $T=2$) the
$50\times50$ SAM-ALE run has $L^2$ density error $0.4897$ against $0.5406$
for the $200\times200$ uniform run, in 45.6 s against 289 s of CPU time and
7.8 MB against 43.7 MB of memory, "approximately 6 times faster" (Table 6,
§7.1). On a Rayleigh–Taylor problem the $64\times128$ SAM-ALE run is
comparable to the $256\times512$ uniform run, 138 s against 1370 s, and 88
times faster than $512\times1024$ (Table 7, §7.2;
[Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md)).
Mesh generation costs about as much as the flow solve in that run, from
which the authors conclude that an MK-based ALE scheme, 100 to 200 times
slower in mesh generation, "cannot provide a speed-up over uniform mesh
simulations" (§7.2.4); this is a cost extrapolation, not a run. They
describe the moving-mesh literature, citing the preprint of Li, Duan & Tang,
as reporting 2 to 6 times speed-ups (§1), consistent with the CPU ratios
of 18 % to 41 % in the table above.

**Two routes to the mesh.** Duan & Tang and Li, Duan & Tang move the
nodes by Jacobi iterations of a Winslow-type equation driven by a gradient
monitor; Ramani & Shkoller prescribe the cell size directly through
$\mathsf G$ and solve one linear Poisson problem and one transport problem.
No source runs both on a common test.

## Optimal-transport meshes for steady high-order solvers

[Nguyen, Van Heyningen, Vila-Pérez & Peraire (2024)](/sources/nguyen-2024.md)
carry r-adaptivity to steady compressible Euler and Navier–Stokes flows
discretized by hybridizable discontinuous Galerkin (HDG) on isoparametric
elements of degree $4$ (degree $3$ in one case) (§2.5, §4; arXiv v1). The
mesh map is the gradient of a convex potential $\Phi_{\mathrm{OT}}$
(page-local, as are $\varrho_{\mathrm m}$, $\bar\varrho$, $b$ and
$\beta_{\mathrm m}$ below), which by Brenier's theorem exists and is unique
up to a constant; under the equidistribution principle it solves the
Monge–Ampère equation with the second boundary-value condition (§3.1–3.2,
Eqs. (18)–(23)),

$$\varrho_{\mathrm m}(\nabla\Phi_{\mathrm{OT}})\,\det\big(D^2\Phi_{\mathrm{OT}}\big)=\bar\varrho\ \text{ in }\Omega,\qquad \nabla\Phi_{\mathrm{OT}}(x)\in\partial\Omega\ \text{ on }\partial\Omega,\qquad \int_\Omega\Phi_{\mathrm{OT}}\,dx=0,$$

with $\bar\varrho=\int_\Omega\varrho_{\mathrm m}\,dx/\lvert\Omega\rvert$ and
$\varrho_{\mathrm m}$ the mesh density. The mesh density solves a Helmholtz
equation $\varrho_{\mathrm m}-\nabla\cdot(h_{\min}^2\nabla\varrho_{\mathrm m})=b$
with homogeneous Neumann conditions, $h_{\min}$ the smallest mesh size, and
a resolution indicator built either from the clipped velocity divergence,
$b=\sqrt{1+\beta_{\mathrm m}s}$, or from the density gradient,
$b=\sqrt{1+\beta_{\mathrm m}g(\lvert\nabla\rho\rvert)}$, with $s$ the
shock source of their artificial viscosity and $g$ a smooth clipping (Eqs.
(24)–(26)); the smoothing is needed for the Monge–Ampère discretization to
converge (§3.3). The Monge–Ampère equation is solved as a first-order
system by a fixed-point HDG iteration from the authors' earlier work,
extended to a mesh density given by piecewise polynomials on the current
mesh, which needs a Newton inversion of the isoparametric map at every
quadrature point (§3.4, Eqs. (27)–(34)). Shocks are captured by the
PDE-based [artificial viscosity](/methods/artificial-viscosity.md) of the
authors' earlier work, whose amplitude and thickness are minimized by a
homotopy continuation under positivity and modal-smoothness constraints
(§2.2–2.4).

**Algorithm 1** (§3.5): solve the regularized flow problem; compute the
mesh density; solve the Monge–Ampère problem; move the nodes to the new
positions $\nabla\Phi_{\mathrm{OT}}$, averaged at duplicated nodes, with the
same number of nodes and the same connectivity; interpolate the solution
onto the new mesh as initial guess and solve again; repeat until the change
in the solution falls below a tolerance (not printed). The homotopy on the
viscosity parameters runs only on the final mesh. Because the map is the
gradient of a scalar potential, no node can be pinned explicitly (§4.2).
On a polygonal domain, imposing the boundary condition face by face makes the
mesh detach at corners; the authors let boundary nodes slide from face to
face and then move the vertex nearest to each corner onto it, and leave open
whether the detachment comes from the HDG discretization or from the
Monge–Ampère formulation on that domain (§4.2, Figs. 5–6).

The tests are a supersonic channel with a circular-arc bump
([supersonic bump channel](/benchmarks/supersonic-bump-channel.md), an
illustration of Algorithm 1, Fig. 1), the transonic
[NACA 0012 airfoil](/benchmarks/naca0012-airfoil.md) at $M=0.8$,
angle of attack $1.5^\circ$, a $25^\circ$/$37^\circ$ double ramp at $M=3.6$,
inviscid and viscous hypersonic
[cylinders](/benchmarks/flow-past-circular-cylinder.md) ($M=7$; $M=17.6$,
$\mathrm{Re}=376{,}000$) and a type IV shock–shock interaction at $M=8.03$.
The authors report sharp, oscillation-free solutions after two or three
adaptations, an artificial viscosity that shrinks in amplitude and width as
the mesh adapts, a type IV surface-pressure peak closer to the Wieting–Holden
experiment, and a viscous-cylinder heat-transfer coefficient that matches the
LAURA reference only on the adapted mesh (§4, Figs. 2–22). The
density-gradient indicator is reported more effective than the velocity
divergence when boundary layers, shear layers and expansions are present
(§5). No error norm, convergence order, timing or iteration count is
printed.

Like Ramani & Shkoller's SAM, the method solves a Monge–Ampère-type problem
for the mesh, but it selects the optimal-transport map and solves the full
nonlinear equation, which SAM avoids by its Poisson-plus-transport
construction (§3.1 of Ramani & Shkoller); the two sources run no common
test.

## Relation to other adaptive methods

Ramani & Shkoller state that the dyadic jumps of resolution in
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md) produce
spurious reflection and scattering at refinement boundaries that corrupt
Noh and Rayleigh–Taylor solutions and persist under refinement, citing
AMR codes (§1.1, §7.1); a smooth moving mesh has no such jumps.

Moving-mesh r-adaptivity is one of several ways the sources concentrate
resolution. [Peng, Atkins & Deiterding (2022)](/sources/peng-2022.md) cite adaptive
mesh redistribution for shock-induced combustion (their ref. [9]); their own
approach is block-structured h-refinement on mapped meshes
([adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)), and
[Bai & Li (2022)](/sources/bai-2022.md) use quadtree h-refinement of a DG
discretization ([h- and hp-adaptation](/methods/hp-adaptation.md)). No
source compares the two strategies on a common test.

[Huang & Zahr (2022)](/sources/huang-2022.md) describe their implicit
shock tracking as having "r-adaptive behavior" (§1): the number and
connectivity of the nodes are fixed apart from element removals, and the
nodes move. The motion is not driven by a monitor function and a
redistribution equation, as here, but is an unknown of an optimization
problem that minimizes an enriched DG residual, so the mesh converges to
one aligned with the discontinuities instead of clustering points near
them ([implicit shock tracking](/methods/implicit-shock-tracking.md)).
Unsteady problems are solved as steady problems in space–time, with no
time step on a moving mesh.

## Qualifications

- The efficiency claims of Duan & Tang and Li, Duan & Tang rest on a visual
  comparison of solutions; no error norm is computed for the shock tests in
  either paper. Ramani & Shkoller compare an $L^2$ density error for Noh and
  vorticity norms for Rayleigh–Taylor (Tables 6–7, Fig. 18).
- The free-stream and entropy-conservation results of Li, Duan & Tang are
  stated with reference to Duan & Tang, who print the proofs for the
  high-order finite-difference case (Prop. 3.2, Thm. 3.2, Thm. 4.1 of
  Duan & Tang 2022).
- For the tri-point problem Li, Duan & Tang say the moving-mesh run "only
  takes 18.9 % CPU time of MM-WENOMR with $1050\times450$ cells". The
  comparison in Table 5.2 is with the uniform-mesh run, and the printed
  timings give $201/1087=18.5$ % *(compiler check, not in the sources)*.
- For the 3D RMHD shock–cloud Duan & Tang print 9.06 %; the timings of
  their Table 6.2 give $11397/125209=9.10$ % *(compiler check, not in the
  sources)*. Their other printed percentages agree with their tables.
- Duan & Tang's mesh-motion limiter (§5) mixes $(x_1)$ and $(x_k)$ in one
  formula; $(x_k)$ is evidently meant in both places.
- Ramani & Shkoller's Table 3 prints SAM-over-MK speed-up factors 47, 131,
  160, 174, 190 for $16^2$ to $256^2$; the printed times give 37.5, 107,
  148, 171 and 206 *(compiler check, not in the sources)*. One of the two
  rows is inconsistent; the order of magnitude stands.
- Ramani & Shkoller's §1.2 claims "better convergence rates" than MK, but
  their own Table 2 gives last-level orders 2.12 and 1.94 for SAM with the
  smoothed target against 1.99 and 1.99 for MK; only the error levels
  favour SAM.
- As printed, Ramani & Shkoller's Noh target (Eq. (57)) has the exponent
  $-400(r^2-t^2/9)$ without a square, which peaks at $r=0$ instead of at the
  shock radius $r=t/3$ that it is said to track; their other targets
  (Eqs. (19), (32)) square the bracket *(compiler check, not in the sources)*.
- Ramani & Shkoller's ALE wave speeds (Eq. (43)) are printed as
  $(v^j\pm c)/J$ with a transport velocity $v^j$ that already contains the
  factor $1/J$; in one dimension the eigenvalues of the ALE flux Jacobian
  are $v\pm c/J$ *(compiler check, not in the sources)*.
- Nguyen et al.'s homotopy update, printed as
  $\lambda_{n,1}=\zeta^{n-1}\lambda_{n-1,1}$ with a reduction factor
  $\zeta\in(0,1)$ (page-local symbols, arXiv v1 §2.4), leaves the first step
  unreduced and compounds to $\zeta^{n(n-1)/2}$ *(compiler check, not in the
  sources)*; the values of $\zeta$ and of the initial amplitude are not
  printed. Their Eq. (21) states the second boundary-value condition for
  all $x\in\Omega$, where their Eq. (22) has it on $\partial\Omega$.
- Nguyen et al. dismiss limiters as hard to combine with implicit time
  integration and high-order methods on complex geometries (§1), a stated
  motivation, not a measured comparison.
- The SAM-ALE solver is described by its authors as "not meant to be
  representative of the full class of ALE solvers" (§7.2.4): it misses the
  small-scale Rayleigh–Taylor roll-up that the tracked interface shows.

# Citations

- [Duan & Tang (2022)](/sources/duan-2022.md) — §1, §2 Eqs. (2.4)–(2.11), §3.1 Def. 3.1 Eqs. (3.1)–(3.3), Prop. 3.1 Eqs. (3.6)–(3.12), §3.3 Eqs. (3.15)–(3.18), Prop. 3.2, Thm. 3.2, §4 Thm. 4.1, §5 Eqs. (5.1)–(5.3), Remark 5.1, §6 Eqs. (6.1)–(6.3), Exs. 6.1–6.10, Tables 6.1–6.2 (arXiv v1).
- [Li, Duan & Tang (2022)](/sources/li-2022-c.md) — §1, §2 Eqs. (2.1)–(2.3), §3 Eqs. (3.1)–(3.12), Prop. 3.1, Remark 3.1, §3.4 Eq. (3.21), Remark 3.2, §4 Eqs. (4.1)–(4.2), Remark 4.1, §5 Eq. (5.1), Ex. 5.1–5.11, Tables 5.1–5.3 (arXiv v1).
- [Peng, Atkins & Deiterding (2022)](/sources/peng-2022.md) — ref. [9] (moving-mesh work cited); block-structured h-refinement used.
- [Bai & Li (2022)](/sources/bai-2022.md) — quadtree AMR of the DG solver.
- [Huang & Zahr (2022)](/sources/huang-2022.md) — §1, §2.1 (arXiv v2).
- [Ramani & Shkoller (2023)](/sources/ramani-2023.md) — §1, §3 Eqs. (7)–(14), (16)–(17), Tables 1–3, App. B, C.1; §4 Eqs. (25)–(29), Algorithms 1–3; §5; §6 Eqs. (41)–(51), Remark 1, App. A; §7 Tables 6–7 (arXiv v2).
- [Nguyen, Van Heyningen, Vila-Pérez & Peraire (2024)](/sources/nguyen-2024.md) — §1, §2.2–2.5, §3.1–3.5 Eqs. (18)–(34), Algorithm 1, §4.1–4.5 Figs. 1–22, §5 (arXiv v1).
