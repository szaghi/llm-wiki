---
type: Method
title: "Adaptive moving mesh finite differences"
description: "An r-adaptive finite-difference scheme moves a fixed number of grid points by solving variational mesh-redistribution equations driven by a monitor function, and discretizes the conservation law in time-dependent curvilinear coordinates with discrete geometric conservation laws; Duan and Tang, then Li, Duan and Tang, make it high-order entropy stable and measure its cost against uniform meshes."
status: established
aliases: [moving mesh method, r-adaptivity, adaptive moving mesh, mesh redistribution, MM-WENOMR, MM-O5, MM-O6]
tags: [finite-difference, entropy-stable, multiphase, relativistic, weno, moving-mesh]
timestamp: 2026-10-22T18:00:00Z
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

## Relation to other adaptive methods

Moving-mesh r-adaptivity is one of several ways the sources concentrate
resolution. [Peng, Atkins & Deiterding (2022)](/sources/peng-2022.md) cite adaptive
mesh redistribution for shock-induced combustion (their ref. [9]); their own
approach is block-structured h-refinement on mapped meshes
([adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)), and
[Bai & Li (2022)](/sources/bai-2022.md) use quadtree h-refinement of a DG
discretization ([h- and hp-adaptation](/methods/hp-adaptation.md)). No
source compares the two strategies on a common test.

## Qualifications

- The efficiency claims rest on a visual comparison of solutions; no error
  norm is computed for the shock tests in either paper.
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

# Citations

- [Duan & Tang (2022)](/sources/duan-2022.md) — §1, §2 Eqs. (2.4)–(2.11), §3.1 Def. 3.1 Eqs. (3.1)–(3.3), Prop. 3.1 Eqs. (3.6)–(3.12), §3.3 Eqs. (3.15)–(3.18), Prop. 3.2, Thm. 3.2, §4 Thm. 4.1, §5 Eqs. (5.1)–(5.3), Remark 5.1, §6 Eqs. (6.1)–(6.3), Exs. 6.1–6.10, Tables 6.1–6.2 (arXiv v1).
- [Li, Duan & Tang (2022)](/sources/li-2022-c.md) — §1, §2 Eqs. (2.1)–(2.3), §3 Eqs. (3.1)–(3.12), Prop. 3.1, Remark 3.1, §3.4 Eq. (3.21), Remark 3.2, §4 Eqs. (4.1)–(4.2), Remark 4.1, §5 Eq. (5.1), Ex. 5.1–5.11, Tables 5.1–5.3 (arXiv v1).
- [Peng, Atkins & Deiterding (2022)](/sources/peng-2022.md) — ref. [9] (moving-mesh work cited); block-structured h-refinement used.
- [Bai & Li (2022)](/sources/bai-2022.md) — quadtree AMR of the DG solver.
