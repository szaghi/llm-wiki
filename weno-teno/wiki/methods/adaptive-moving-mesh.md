---
type: Method
title: "Adaptive moving mesh finite differences"
description: "An r-adaptive finite-difference scheme moves a fixed number of grid points by solving variational mesh-redistribution equations driven by a monitor function, and discretizes the conservation law in time-dependent curvilinear coordinates with discrete geometric conservation laws; Li, Duan and Tang make it entropy stable and measure its cost against uniform meshes."
status: established
aliases: [moving mesh method, r-adaptivity, adaptive moving mesh, mesh redistribution, MM-WENOMR]
tags: [finite-difference, entropy-stable, multiphase, weno, moving-mesh]
timestamp: 2026-10-22T12:00:00Z
---

# Adaptive moving mesh finite differences

An adaptive moving mesh scheme keeps the number and connectivity of the
grid points fixed and moves them towards the features of the solution
(r-adaptivity). The solution is computed on a uniform mesh in page-local
computational coordinates $\xi=(\xi_1,\xi_2,\xi_3)$, mapped to the physical
mesh by $x=x(\xi,\tau)$ with $t=\tau$. At each time step two problems are
solved: a mesh-redistribution problem gives the new mesh, and the
conservation law, written in the moving curvilinear coordinates, advances
the solution. [Li, Duan & Tang (2022)](/sources/li-2022-c.md) build the
scheme of this page. They extend the entropy-stable moving-mesh schemes of
Duan & Tang (developed for special-relativistic (M)HD) to single- and
two-component Euler equations with a stiffened-gas law (§1;
[stiffened-gas equation of state](/definitions/stiffened-gas-equation-of-state.md),
[multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)).

## The conservation law in moving coordinates

With $J=\det\partial(t,x)/\partial(\tau,\xi)$ and the metric terms
$J\partial_t\xi_k$ and $J\partial_{x_j}\xi_k$, the law
$\partial_tu+\sum_j\partial_{x_j}f^{(j)}(u)=0$ becomes (Eq. (2.2))

$$\frac{\partial(Ju)}{\partial\tau}+\sum_k\frac{\partial}{\partial\xi_k}\Big(J\frac{\partial\xi_k}{\partial t}\,u+\sum_jJ\frac{\partial\xi_k}{\partial x_j}\,f^{(j)}(u)\Big)=0 .$$

It holds together with the geometric conservation laws (Eq. (2.3)):

- the volume conservation law (VCL),
  $\partial_\tau J+\sum_k\partial_{\xi_k}(J\partial_t\xi_k)=0$;
- the surface conservation laws (SCLs),
  $\sum_k\partial_{\xi_k}(J\partial_{x_j}\xi_k)=0$ for every $j$.

The scheme is a [conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
in $\xi$ for the point values $(Ju)_i$ and for $J_i$ (Eqs. (3.1)–(3.2)).
Its discrete SCLs are met by writing $J\partial_{x_j}\xi_k$ in conservative
cross-product form with the same central difference operator as the
entropy-conservative flux (Eq. (3.9)). The discrete VCL is met by computing
$J\partial_t\xi_k=-\sum_j\dot x_j\,J\partial_{x_j}\xi_k$ from the mesh
velocity $\dot x$ (Eq. (3.10)). The authors state that the fully discrete
scheme with SSP-RK3 then preserves free streams, a result proved by Duan &
Tang (Remark 3.1; [free-stream preservation](/properties/free-stream-preservation.md)).
As recalled by them, failing the discrete GCLs misrepresents the convective
velocities and creates spurious sources and sinks (§3.2).

## Entropy-stable fluxes on a moving mesh

**Entropy conservation.** A consistent two-point flux $\hat F_k$ in
direction $k$ makes the scheme entropy-conservative if (Prop. 3.1, proof
deferred to Duan & Tang)

$$[\![w]\!]\cdot\hat F_k=\{\!\{J\partial_t\xi_k\}\!\}\,[\![\phi]\!]+\sum_j\{\!\{J\partial_{x_j}\xi_k\}\!\}\,[\![\psi^{(j)}]\!].$$

Here page-local $\phi=w\cdot u-\eta$ is the entropy potential and
$\psi^{(j)}$ the registry's flux potentials. They satisfy the condition
with $\hat F_k=\{\!\{J\partial_t\xi_k\}\!\}\,\tilde u+\sum_j\{\!\{J\partial_{x_j}\xi_k\}\!\}\,f^{\mathrm{ec},(j)}$,
where the Cartesian flux $f^{\mathrm{ec},(j)}$ satisfies Tadmor's condition and the page-local
"entropy-conservative state" $\tilde u$ satisfies $[\![w]\!]\cdot\tilde u=[\![\phi]\!]$
(Eqs. (3.11)–(3.12)). The explicit fluxes for the stiffened gas are on
[entropy-conservative two-point fluxes](/methods/entropy-conservative-flux.md).

**Entropy stability.** The interface flux adds to the high-order
entropy-conservative flux a dissipation on jumps of the
multi-resolution-WENO reconstructions of the scaled entropy variables, with
a sign switch (Eq. (3.21)). This is a
[TeCNO-type flux](/methods/tecno-scheme.md). The scheme is called
MM-WENOMR; MM-WENOJS uses WENO-JS in the dissipation and UM-WENOMR is the
same scheme on a uniform mesh (§5).

## Mesh redistribution

The new mesh solves the variational redistribution equations (Eq. (4.1)),
of the Winslow–Brackbill type as the authors recall,

$$\nabla_\xi\cdot\big(\Pi\,\nabla_\xi x_k\big)=0,\qquad k=1,2,3,$$

with the scalar monitor function (page-local $\Pi$, $\mathsf s_k$,
$\mathsf a_k$; Eq. (4.2))

$$\Pi=\Big(1+\sum_{k=1}^{n_{\mathrm m}}\mathsf a_k\Big(\frac{\lvert\nabla_\xi\mathsf s_k\rvert}{\max\lvert\nabla_\xi\mathsf s_k\rvert}\Big)^2\Big)^{1/2}.$$

Here $\mathsf s_k$ are $n_{\mathrm m}$ chosen physical variables and
$\mathsf a_k\ge0$ their weights. The algorithm (§4):

1. Discretize the redistribution equations by second-order central
   differences and take ten Jacobi iterations from the current mesh,
   with interface values $\Pi_{i\pm1/2}$ the averages of neighbouring
   values.
2. Smooth $\Pi$ by a low-pass filter with weights
   $(1/2)^{\lvert j_1\rvert+\lvert j_2\rvert+\lvert j_3\rvert+3}$ over the
   27-point neighbourhood, 3 to 10 times (Remark 4.1).
3. Move the mesh by a limited fraction of the Jacobi displacement, so that
   no point passes half the distance to its neighbour in one step.
4. Set the mesh velocity $\dot x$ to the actual displacement divided by
   $\Delta t$.

The monitor carries more variables for two components. The two-component
shock–bubble test with a stiffened gas uses five: a schlieren function,
a variable printed $u$ and never defined (the velocity is $v$ throughout the paper), the two partial densities and the pressure, with weights
$(600,500,1200,1200,1200)$ (Ex. 5.9). The authors state that the
multi-component equations need more solution information in the monitor
than the single-component ones to give a good mesh (§1). They show no
ablation of this choice.

## Cost and accuracy

The time step is $\Delta t\le C_{\mathrm{CFL}}/\max_i\sum_k\varrho_{i,k}/\Delta\xi_k$,
with $\varrho_{i,k}$ the spectral radius in direction $k$ (page-local),
$C_{\mathrm{CFL}}=0.4$ in 2D and $0.3$ in 3D, and SSP-RK3 (Eq. (5.1)). The
accuracy tests use $\Delta t\propto(\min\Delta\xi_k)^{5/3}$. Fifth order is
observed on the moving mesh for the 2D vortex ($t=4$, $N_x=40$ to $320$)
and for the 3D vortex rotated to the domain diagonal ($t=0.1$) (Ex. 5.1,
5.5; [isentropic vortex](/benchmarks/isentropic-vortex.md)).

The moving-mesh runs match or beat uniform meshes with two to three times as
many points per direction, at a fraction of their CPU time (Tables 5.1–5.3,
CPU nodes with Intel Xeon E5-2697A V4):

| test | moving mesh | uniform reference | CPU ratio |
|---|---|---|---|
| 2D Riemann problem I | $200^2$, 2 min 56 s | $500^2$, 7 min 9 s | 41.0 % |
| 2D Riemann problem II | $200^2$, 2 min 50 s | $600^2$, 13 min 10 s | 21.5 % |
| 3D spherical shock tube | $100^3$, 13 min 53 s | $200^3$, 37 min 19 s | 37.2 % |
| tri-point problem | $350\times150$, 3 min 21 s | $1050\times450$, 18 min 7 s | 18.9 % (printed) |
| 2D shock–helium bubble | $800\times160$, 1 h 4 min | $2400\times480$, 4 h 4 min | 26.2 % |
| 2D shock–bubble, stiffened gas | $800\times160$, 9 min 28 s | $2400\times480$, 40 min 11 s | 23.6 % |
| 3D shock–helium bubble | $400\times80^2$, 11 h 6 min | $800\times160^2$, 38 h 2 min | 29.2 % |
| 3D shock–bubble, stiffened gas | $400\times80^2$, 2 h 9 min | $800\times160^2$, 11 h 58 min | 18.0 % |

The tests are listed on
[two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md),
[Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md) and
[shock–bubble interaction](/benchmarks/shock-bubble-interaction.md). The
authors judge the moving-mesh result superior or comparable in every case.
On equal point counts a moving-mesh run costs about 4 to 7 times a
uniform-mesh run, for example 2 min 56 s against 28 s on Riemann problem I
and 11 h 6 min against 2 h 34 min on the 3D helium bubble *(compiler check,
not in the sources: ratios of the printed timings)*. Replacing WENO-JS by
multi-resolution WENO in the dissipation resolves more small-scale structure
"with a slight increase in the computational cost" (Remark 3.2); the printed
timings give 0.1 % to 12 % more *(compiler check, not in the sources)*.

## Qualifications

- The efficiency claims rest on a visual comparison of solutions; no error
  norm is computed for the shock tests.
- The free-stream and entropy-conservation results are stated with
  reference to Duan & Tang. Li, Duan & Tang print no proof.
- For the tri-point problem the text says the moving-mesh run "only takes
  18.9 % CPU time of MM-WENOMR with $1050\times450$ cells". The comparison in
  Table 5.2 is with the uniform-mesh run, and the printed timings give
  $201/1087=18.5$ % *(compiler check, not in the sources)*.

# Citations

- [Li, Duan & Tang (2022)](/sources/li-2022-c.md) — §1, §2 Eqs. (2.1)–(2.3), §3 Eqs. (3.1)–(3.12), Prop. 3.1, Remark 3.1, §3.4 Eq. (3.21), Remark 3.2, §4 Eqs. (4.1)–(4.2), Remark 4.1, §5 Eq. (5.1), Ex. 5.1–5.11, Tables 5.1–5.3 (arXiv v1).
