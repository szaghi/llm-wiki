---
type: Method
title: "Conservative remapping for ALE schemes"
description: "Conservative remapping transfers cell averages from one mesh to another; the page records van Leer's 1979 Lagrangean-to-Eulerian remap in MUSCL, Gu et al.'s ALE remap as a moving-mesh solve of a trivial equation with proved positivity, and Cai et al.'s remap with evolved geometric moments, exact on quadratics with O(1) pseudo-time levels."
status: established
aliases: [remapping, remap, conservative interpolation, ALE remapping, WENO remapping, P-WENO remapping, rezone and remap, Lagrange-plus-remap, Eulerian remap, advection-based remapping, TPE(2) remapping]
tags: [finite-volume, weno, positivity, bound-preserving, reconstruction, moving-mesh]
timestamp: 2026-11-01T18:56:00Z
---

# Conservative remapping for ALE schemes

An indirect arbitrary Lagrangian–Eulerian (ALE) method alternates three
steps: a Lagrangian step, in which the mesh moves with the fluid; a
**rezone**, in which a less distorted mesh with the same number of cells
and the same connectivity is chosen; and a **remap**, in which the cell
averages $\bar u_i$ of the conserved variables are transferred from the
old mesh to the new one. The remap must conserve each integral
$\sum_i\lvert I_i\rvert\bar u_i$, keep the accuracy of the Lagrangian
scheme, create no oscillations, and keep the states in the admissible
set $G$ (§1 of the source below). [Gu, Li, Cheng & Shu (2023)](/sources/gu-2023.md)
group the existing remaps into intersection-based methods, which
integrate the old reconstruction over the overlaps of old and new cells,
and transport- or flux-based methods, which advect the data from one mesh
to the other in a pseudo-time (§1). Their own method is of the second
kind.

## Lagrange plus remap in the original MUSCL

The second-order scheme of [van Leer (1979)](/sources/vanleer-1979.md), coded by
P. R. Woodward as [MUSCL](/methods/muscl-hancock.md), is a remap scheme of the simplest
kind: each one-dimensional sweep is a Lagrangean step followed by a remap back to the fixed
Eulerian grid (§3.2). The use of a separate remap step "originated with the group of
W. F. Noh at Livermore"; the idea of using one in MUSCL was Woodward's (§3.2,
Acknowledgments).

- **Geometry** (§3.2, Fig. 1). The time step is restricted so that no gas crosses more than
  one Eulerian boundary; an Eulerian cell then holds matter from one, two or three
  Lagrangean cells. The new mass coordinates of the fixed boundaries follow from the linear
  distributions; to avoid the quadratic equation this gives in specific volume against mass,
  the remap uses density against the volume coordinate (Eqs. (93)–(98)).
- **Least-squares accuracy** (Eqs. (94)–(95)). The piecewise-linear, possibly discontinuous
  distribution inside an Eulerian cell is replaced by the linear function with the same
  zeroth moment (cell integral) and first moment, the slope being the first moment divided
  by $\Delta\zeta^3/12$ ($\Delta\zeta$ the cell size in the mass coordinate, page-local); the
  fourth paper of the series is cited for this moment fitting ("scheme III") being "vastly
  superior" to finite-difference slopes (App. B).
- **Limiting** (§3.3, Eqs. (102)–(103)). The remap slope is limited with factors
  $2/\varphi_{\mathrm{vL}}$ and $2/(1-\varphi_{\mathrm{vL}})$, $\varphi_{\mathrm{vL}}$ (page-local; not the GQL $\varphi_i$) the mass fraction of the Lagrangean cell that
  crosses the Eulerian boundary (page-local), so that the averages of the parts crossing and
  staying lie within the neighbouring averages; positivity is then guaranteed "only for the
  zone averages" ([TVD and slope limiters](/definitions/total-variation-diminishing.md),
  [bound preservation](/properties/bound-preservation.md)).
- **Time step** (Eqs. (99)–(100.5)). The composite scheme needs
  $\Delta t\le\min(\Delta x/\lvert\bar v\rvert,\Delta x/\bar c)$ up to higher-order terms,
  which the author calls less stringent than the Eulerian $\Delta x/(\lvert\bar v\rvert+\bar c)$,
  plus an anti-tangling condition on the velocity slope that the limiters can enforce.
- **Cost** (§3.2). The remap costs about 0.55 of the Lagrangean step in the 1D shock tube
  and up to 0.75 in 2D.

In van Leer's scheme the target mesh is the fixed Eulerian grid, and the time-step
restriction keeps the matter of each Lagrangean cell from crossing more than one Eulerian
boundary (§3.2); the ALE remap below maps between two moving meshes.

## Remapping as a moving-mesh solve

Gu et al. solve the trivial equation $\partial_tu=0$ in a pseudo-time
$t\in[0,T_{\mathrm r}]$ (page-local: $T_{\mathrm r}$ is the final
pseudo-time) on a mesh whose nodes travel on straight lines from their
old positions at $t=0$ to the new ones at $t=T_{\mathrm r}$ (§2.1–2.2).
Let $v_{\mathrm g}$ denote the mesh (grid) velocity, page-local; it is
constant in time at every node,
$v_{\mathrm g}=(x^{T_{\mathrm r}}-x^0)/T_{\mathrm r}$, and linear along
each edge (Eqs. 2.3–2.4). Integrating over the moving control volume
$I_{i,j}(t)$ and applying the Reynolds transport and divergence
theorems turns the trivial equation into a linear conservation law with
flux $-v_{\mathrm g}u$ (Eq. 2.2):

$$\frac{d}{dt}\Big(\lvert I_{i,j}(t)\rvert\,\bar u_{i,j}(t)\Big)+\int_{\partial I_{i,j}(t)}\big(-v_{\mathrm g}u\big)\cdot n\,dl=0 .$$

The solution at $t=T_{\mathrm r}$ is the remapped field. The construction
needs no cell intersections and no bound on the node displacement: only
the topology of the two meshes must agree, so a node may move by more
than one cell (§1, §2). It applies to any polygonal mesh with matching
topology; only quadrilaterals are shown (§2.1).

**Choice of the pseudo-time.** Following the moving-mesh finite-volume
analysis of Klingenberg, Schnucke and Xia and of Li et al., which they
cite and do not re-prove, Gu et al. state that high-order accuracy
needs only boundedness, $\lvert v_{\mathrm g}\rvert\le C_0$, and Lipschitz
continuity, $\lvert\partial v_{\mathrm g}/\partial x\rvert\le C_{0,1}$,
of the mesh velocity, with constants independent of the mesh size; both
hold if $T_{\mathrm r}$ is large enough (§2.2; page-local $C_0$,
$C_{0,1}$, both set to 10). No formula for $T_{\mathrm r}$ is printed;
$T_{\mathrm r}$ "depends on the magnitude of the mesh movement" and
halves with the mesh size (§3.4). They set this against "most existing
transport equation based remapping methods in which the final
pseudo-time is fixed as a constant such as 1", and against transport
remaps that need a sufficiently smooth old-to-new mapping (§1, §3.4).

## Discretization

**Finite volumes on moving quadrilaterals** (§2.3). Each edge integral
is a three-point Gauss–Lobatto (Simpson) sum, chosen over Gauss
quadrature because it eases the positivity decomposition. The flux is
upwind on the sign of $v_{\mathrm g}\cdot n$:
$-v_{\mathrm g}u^{\mathrm{in}}$ when $v_{\mathrm g}\cdot n\le0$ and
$-v_{\mathrm g}u^{\mathrm{out}}$ otherwise, with $u^{\mathrm{in}}$,
$u^{\mathrm{out}}$ the traces from inside and outside the cell
(the source's $u^-$, $u^+$, here not the registry's left and right
states); the sign of the flux reverses the upwind direction with
respect to $v_{\mathrm g}$.

**Reconstruction** (§2.4). The third-order two-dimensional
[multi-resolution WENO](/methods/multi-resolution-weno.md) of Zhu and Shu:
the constant $\bar u_{i,j}$ on the cell itself, and a quadratic fitted by
constrained least squares on the $3\times3$ block of cells, constrained
to reproduce $\bar u_{i,j}$; linear weights $d_1=1/11$, $d_2=10/11$,
called "a good balance" between smooth-flow accuracy (larger $d_2$) and
oscillations. The [smoothness indicator](/definitions/smoothness-indicator.md)
of the quadratic is of Jiang–Shu type with area scaling (Eq. 2.6); that
of the constant, which Eq. (2.6) would set to zero, is replaced by
$\beta_1=\min\{\zeta_1+\zeta_2,\zeta_2+\zeta_3,\zeta_3+\zeta_4,\zeta_4+\zeta_1\}$,
with $\zeta_\ell$ the squared differences between $\bar u_{i,j}$ and its
four edge neighbours (page-local $\zeta_\ell$), because $\beta_1=0$ "does
lead to more smearing" at strong shocks and contacts. The nonlinear
weights are of [WENO-Z](/methods/weno-z.md) type,
$\alpha_k=d_k\big(1+(\tau/(\beta_k+\epsilon))^2\big)$ with
$\tau=\lvert\beta_2-\beta_1\rvert$ and $\epsilon=10^{-3}$. Because the
linear weights of multi-resolution WENO may be any positive numbers
summing to one, they need not be recomputed as the cells deform, which
the authors call "particularly suitable and efficient for the remapping
problem" (§1, §2.4).

**Time stepping** (§2.5). [SSP-RK3](/methods/ssp-runge-kutta.md) on the
products $\lvert I_{i,j}\rvert\bar u_{i,j}$, with the area at the second
stage taken as $\tfrac12(\lvert I_{i,j}^n\rvert+\lvert I_{i,j}^{n+1}\rvert)$
(Eq. 2.7). The step is $\Delta t=0.8\,h/\max\lvert v_{\mathrm g}\cdot n\rvert$,
$h$ the smallest inscribed-circle diameter of the cells, capped at $5h$
for temporal accuracy (Eq. 2.8).

## Positivity

For the Euler variables $u=(\rho,\rho v,E)$ the admissible set is
$G=\{\rho>0,\ \rho e>0\}$, with $\rho e=E-\tfrac12\rho\lvert v\rvert^2$
(§2.6.1). Gu et al. obtain [bound preservation](/properties/bound-preservation.md)
by the Zhang–Shu route.

- **First order.** The first-order upwind remap is positivity-preserving
  for $\Delta t\le\tfrac12\min_{i,j}\big[\lvert I_{i,j}\rvert/\big(\sum_k\lvert e_k\rvert\,\max_k\lvert v_{\mathrm g}\cdot n_k\rvert\big)\big]$,
  $\lvert e_k\rvert$ the edge lengths (page-local) (Theorem 2.1; proof referred to Cheng–Shu
  and Zhang–Shu).
- **High order.** Each cell is mapped to $[-\tfrac12,\tfrac12]^2$ and its
  average is decomposed on the $3\times3$ tensor Simpson points
  (quadrature weights $\mathsf w=\tfrac16,\tfrac23,\tfrac16$) with the
  Jacobian values of the map; the forward-Euler update then becomes a
  convex combination of interior point values and first-order updates
  of the boundary point values (Eq. 2.11). If $\bar u^n_{i,j}\in G$ and
  all nine point values lie in $G$, the update stays in $G$ for
  $\Delta t\le\frac{\mathsf w_1}{2}\cdot\frac12\min_{i,j}\big\{\lvert J\rvert_{i,j}/\big(\sum_k\lvert e_k\rvert\,\max_{k,m}\lvert v_{\mathrm g}\cdot n_k\rvert\big)\big\}$,
  $\mathsf w_1=\tfrac16$, with $\lvert J\rvert_{i,j}$ the smallest
  Jacobian value at the boundary points (Theorem 2.2, Eq. 2.12); SSP-RK3
  inherits it by convexity of $G$.
- **Limiter.** The point values are brought into $G$ by the
  [Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md),
  first for density, then for internal energy, at the nine points
  (§2.6.3).
- **In practice** the code runs at the larger step of Eq. (2.8) and,
  when a new average leaves $G$, repeats the step with $\Delta t/2$;
  Theorem 2.2 bounds the number of repetitions (Remark, §2.6.2).

## Evidence

All remap tests are on $[0,1]^2$, start from a uniform mesh and remap
$N=10$ times through a sequence of meshes back to the initial one, so
the error is $\bar u^N-\bar u^0$ (§3). "WENO" denotes the remap without,
"P-WENO" with the positivity limiter.

| Test (§3) | Mesh sequence | Result |
|---|---|---|
| $u=\sin^2(2\pi x)\sin^2(2\pi y)$ | smoothly moving | $L^1$ error $3.403\times10^{-2}$ ($20^2$) to $5.225\times10^{-6}$ ($320^2$), orders 2.67, 3.63, 2.99, 3.37 (Table 3.1) |
| same | randomly moving, node shifts up to a quarter of a cell per direction ($C_r=0.5$ times a random number in $[-0.5,0.5]$, page-local $C_r$) | $L^1$ orders 3.59, 4.20, 3.46, 3.73; WENO leaves 2.86 % of averages negative at $20^2$, 0.03 % at $320^2$; P-WENO none (Table 3.2) |
| same | "flipping": cell sizes reversed, nodes move more than one cell | WENO $L^1$ orders 2.48, 3.44, 3.08, 3.14, with up to 5.67 % negative averages; P-WENO 2.54, 3.42, 3.05, 3.13, none negative (Table 3.3) |
| piecewise data, values 10, 0.1 and a sinusoid | random, $80^2$ | no oscillations near the discontinuities (Fig. 6) |
| step of height 100; cylinder and cone | random $80^2$; flipping $160^2$ | WENO gives 13, 19 and 35 negative averages (smallest $-3.83\times10^{-4}$, $-1.88\times10^{-3}$); P-WENO none (Figs. 7–12) |

**Cost** (§3.4, Table 3.4). For a mild mesh motion (nodes within one
cell), each remap needs three pseudo-time steps at every resolution
from $20^2$ to $320^2$, because $T_{\mathrm r}$ and the step both halve
under refinement; the cost then scales with the cell count, 0.641 s to
69.47 s (WENO) and 0.641 s to 70.08 s (P-WENO). No hardware is stated.

**Inside an ALE code** (§3.5). With the third-order positivity-preserving
ENO Lagrangian scheme of Cheng and Shu, rezoning and P-WENO remapping
every 20 Lagrangian steps, the ALE runs are robust on the
[Sedov blast wave](/benchmarks/sedov-blast-wave.md) ($t=1$), the Saltzman
piston (to $t=0.925$; the pure Lagrangian run fails after $t=0.6$), the
[Noh implosion](/benchmarks/noh-implosion-problem.md) (to $t=0.6$; the
pure Lagrangian run fails after $t=0.54$), the
[Leblanc shock tube](/benchmarks/leblanc-shock-tube.md) ($t=6$) and a
two-material [Sod tube](/benchmarks/sod-and-lax-shock-tubes.md)
($t=0.2$), Figs. 13–20. In the Noh run the positivity limiter of the
remap is needed: without it negative internal energy and pressure stop
the code; the limited cells are marked in Fig. 17, and no run without
the limiter is displayed.

## Exact remapping with evolved geometric moments

[Cai, Cheng, Wu & Qiu (2026)](/sources/cai-2026.md) (arXiv v1) use the
same transport formulation inside a rezoning moving-mesh scheme, where
every physical step is an evolution on the fixed mesh, a rezoning and a
remap ([adaptive moving mesh](/methods/adaptive-moving-mesh.md)). They
group the remaps as Gu et al. do: intersection-based remaps (Dukowicz;
Dukowicz & Kodis) and swept- or flux-based ones (Dukowicz & Baumgardner)
need no smooth mesh velocity but "rely on complex and robust geometric
operations" on general polygonal or curvilinear cells; advection-based
remaps avoid those operations (§1.2, as recalled).

**The bottleneck they address** (§1.2). An advection-based remap is "in
essence, an ALE discretization" of $\partial_{\tau_{\mathrm p}}u=0$ (page-local
pseudo-time $\tau_{\mathrm p}$, Gu et al.'s $t$) and inherits the ALE need
for a regular mesh velocity; as recalled from Anderson et al., its
convergence "is observed only for 'smooth' problems". Solution-driven
rezoning produces mesh velocities that are bounded but discontinuous. The
mesh can then be smoothed, which limits the resolution of the adapted mesh,
or the remap can take many pseudo-time levels: a fixed final pseudo-time
$T_{\mathrm r}=1$ with $\Delta\tau_{\mathrm p}=O(\Delta x)$ (Lipnikov &
Morgan, as recalled), or Gu et al.'s adapted $T_{\mathrm r}$ above. With a
bounded but discontinuous mesh velocity both need $N_\ell=O(\Delta x^{-1})$
pseudo-time levels per physical step (page-local $N_\ell$); with
$\Delta t=O(\Delta x)$ that is the cost of an effective time step
$O(\Delta x^2)$.

**Scheme** (§3.1). The vertices move on straight lines,
$x_P(\tau_{\mathrm p})=x^n_P+\tau_{\mathrm p}v_{\mathrm g,P}$ with
$v_{\mathrm g,P}=(x^{n+1}_P-x^n_P)/T_{\mathrm r}$, and $v_{\mathrm g}$ is
interpolated linearly along the edges, as in Gu et al. (Eqs. (3.8),
(3.17)). The evolved unknowns are the cell integrals
$\mathfrak V_{i,j}=\int_{I_{i,j}}u\,dx\,dy$ (page-local), updated with a
three-point Gauss–Lobatto sum on each edge $l_e$ (page-local points
$x_{e,g}$, weights $\mathsf w_g=\tfrac16,\tfrac23,\tfrac16$) and a local
[Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md) for the remap flux
$-u\,(v_{\mathrm g}\cdot n_e)$,

$$\frac{d\mathfrak V_{i,j}}{d\tau_{\mathrm p}}=\sum_{e=1}^4\lvert l_e\rvert\sum_{g=1}^3\mathsf w_g\,\tfrac12\Big[(u^{\mathrm{in}}+u^{\mathrm{out}})(v_{\mathrm g}\cdot n_e)+a_e\,(u^{\mathrm{out}}-u^{\mathrm{in}})\Big]_{e,g},\qquad a_e=\max_g\lvert v_{\mathrm g}\cdot n_e\rvert ,$$

*(written out from the source's Eqs. (3.10)–(3.11), where the flux tensor
is $-u\otimes v_{\mathrm g}$ and the sum carries a minus sign; compiler
rearrangement)*. The new ingredient is that every geometric moment the
reconstruction needs, $\int_{I_{i,j}}x^sy^r\,dx\,dy$ with $s+r\le2$, is
evolved by its own Reynolds-transport equation with the same edge rule and
the same Runge–Kutta stages, instead of being computed from the cell
geometry; these **evolved geometric moments** replace the exact moments in
the reconstruction, and the cell averages are $\mathfrak V_{i,j}$ divided by
the evolved volume (Eqs. (3.7), (3.9), (3.15);
[transport polynomial exactness](/properties/transport-polynomial-exactness.md)).
The remap starts from $\mathfrak V^0_{i,j}=\bar u^{n+1,0}_{i,j}\widetilde{\mathfrak M}^0_{0,0,i,j}$
with the evolved moments inherited from the previous step (§3.1.4). It runs
[SSP-RK3](/methods/ssp-runge-kutta.md) jointly on moments and integrals,
with the stage geometries at $\tau_{\mathrm p}$,
$\tau_{\mathrm p}+\Delta\tau_{\mathrm p}$ and
$\tau_{\mathrm p}+\tfrac12\Delta\tau_{\mathrm p}$ (Eqs. (3.14), (3.18)). The
reconstruction is a [hybrid WENO](/methods/hybrid-weno.md): the optimal
least-squares quadratic in cells the KXRCF
[troubled-cell indicator](/definitions/troubled-cell-indicator.md) leaves
unflagged, Zhu & Qiu's third-order WENO otherwise, with the smoothness
indicators divided by the local variance for
[affine invariance](/methods/affine-invariant-weno.md) (§3.4, Remark 3.6).

**Exactness.** The remap reproduces the averages of any quadratic for any
mesh motion and any $\Delta\tau_{\mathrm p}$ (Thm. 4.3, Prop. 4.4), and with
SSP-RK3 at those stage geometries the evolved moments equal the exact ones
(Thm. 4.7). Because the evolved volume is the evolved zeroth moment, the
scheme also satisfies the classical geometric conservation law, which Gu et
al. do not discuss.

**Pseudo-time step** (§4.5). Since accuracy no longer depends on
$\Delta\tau_{\mathrm p}$, only stability limits it (Eqs. (4.14)–(4.15)):

$$\Delta\tau_{\mathrm p}\le C_{\mathrm{CFL}}\min_{i,j}\frac{\lvert I_{i,j}\rvert}{\max_ea_e\lvert l_e\rvert},\qquad N_\ell\ge\max_{i,j}\frac{\max_P\lvert\delta x_P\rvert\,\max_e\lvert l_e\rvert}{C_{\mathrm{CFL}}\,\lvert I_{i,j}\rvert},$$

with $\delta x_P$ the vertex displacements and $C_{\mathrm{CFL}}$ the CFL
number (page-local), using $\lvert v_{\mathrm g}\rvert\le\max_P\lvert\delta x_P\rvert/T_{\mathrm r}$.
With $\lvert l_e\rvert=O(\Delta x)$, $\lvert I_{i,j}\rvert=O(\Delta x^2)$,
$\Delta t=O(\Delta x)$ and a bounded physical mesh velocity
$\lvert\delta x_P\rvert/\Delta t$, this gives $N_\ell=O(1)$. The update depends
only on $v_{\mathrm g}\Delta\tau_{\mathrm p}$, so the solution does not depend
on $T_{\mathrm r}$, which is set to $\Delta t$ (Remark 4.12);
$C_{\mathrm{CFL}}\le\tfrac14$ keeps the evolved volume positive (Remark
4.13).

**Evidence** (§5.2, Tables 2–3). Euler [density wave](/benchmarks/density-wave-advection.md)
on randomly rezoned meshes ($C_r=0.5$, drift $(-0.6,-0.8)$), $t=0.1$, C++ on
an Intel Xeon Gold 6348 at 2.60 GHz. "ol" takes $T_{\mathrm r}=\Delta t$
and the step above; "rl" follows Gu et al.'s choice of $T_{\mathrm r}$ and
$\Delta\tau_{\mathrm p}$.

| remap | $N_\ell$, $80^2\to320^2$ | $L^1$ behaviour | total / remap CPU at $320^2$ (s) |
|---|---|---|---|
| evolved moments, ol | 2.0 at every mesh | orders 2.93–2.98 | 5795.1 / 3942.6 |
| GCL only (evolved volume, exact higher moments), ol | 2.0 | orders 2.24–2.91; $L^\infty$ orders down to $-0.55$ | 6211.8 / 4365.8 |
| exact moments, ol | 2.0 | no convergence, about $1.5$–$1.7\times10^{-3}$ | 16490.4 / 10975.8 |
| exact moments, rl (Gu et al.'s strategy) | 4.7, 7.0, 9.4, 12.0, 14.4, 17.1, 19.7 | orders 2.91–3.36, errors above the evolved-moment scheme | 67168.3 / 64781.5 |

The rl strategy holds the measured Lipschitz constant of the mesh velocity
at 10.0, the value of Gu et al.'s bound $C_{0,1}$ above, while under ol it
grows from 1874.9 to 8443.5. The remap takes 68.0 %, 70.3 %, 66.6 % and
96.4 % of the run. The exact-moment ol scheme costs about three times the
evolved-moment one (16490.4/5795.1 = 2.85 *(compiler check)*) because,
according to the authors, the geometric mismatch creates oscillations that
make the KXRCF indicator flag smooth cells and switch on the expensive WENO
branch. On a 2D Riemann problem ($400^2$, $t=0.25$) the evolved-moment remap
with $N_\ell=2$ matches the exact-moment remap with $N_\ell=6$ and changes
little with $N_\ell$ (Fig. 6;
[two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md));
the [double Mach reflection](/benchmarks/double-mach-reflection.md) on
$1920\times480$ extreme random meshes runs without mesh-induced artifacts
(Fig. 7), and with ALE rezoning the
[Woodward–Colella](/benchmarks/woodward-colella-blast-wave.md) and
[Shu–Osher](/benchmarks/shu-osher-problem.md) problems are resolved better
than on a fixed $400\times10$ mesh (Figs. 4–5). These comparisons are
visual.

## Relation to other mesh-motion strategies

The remap is a moving-mesh finite-volume solve with a prescribed,
straight-line node motion, not with the monitor-driven motion of an
[adaptive moving mesh](/methods/adaptive-moving-mesh.md).
[Ramani & Shkoller (2023)](/sources/ramani-2023.md) take the other route
of that page: they write the Euler equations in ALE form on the fixed
reference domain, with the mesh velocity $\partial_t\psi$ of their mesh
map $\psi$ inside the fluxes, so the solution is never transferred
between two meshes (§6.1). The two sources share the concern for the
geometric terms of a moving cell: Ramani & Shkoller evolve the Jacobian
by the geometric conservation law ([free-stream preservation](/properties/free-stream-preservation.md)),
and Gu et al. do not discuss it.

## Qualifications

- The accuracy argument rests on moving-mesh analyses cited from DG,
  LDG and finite-difference WENO work in one dimension or for
  Hamilton–Jacobi equations; it is not proved for this two-dimensional
  finite-volume scheme (§2.2).
- The area of a quadrilateral whose vertices move linearly in time is a
  quadratic polynomial in time, because the shoelace formula is a sum of
  products of two coordinates; the mean
  $\tfrac12(\lvert I^n\rvert+\lvert I^{n+1}\rvert)$ used at the
  second Runge–Kutta stage equals the area at $t^{n+1/2}$ only when the
  quadratic coefficient vanishes *(compiler check, not in the sources)*.
- The internal energy is written per unit volume in §2.6 and per unit
  mass in the Sedov set-up ($p=(\gamma-1)\rho e$); the positivity
  statements are unaffected.
- The statements that the pure Lagrangian scheme fails on Saltzman and
  Noh concern the Lagrangian scheme of Cheng and Shu; the authors note
  that other Lagrangian schemes "may produce better or more robust
  results" (§3.5).
- Gu et al.'s Leblanc initial data are printed with five components for
  a four-component state $(\rho,v_1,v_2,e)$ on the left (§3.5.4); the
  [Leblanc page](/benchmarks/leblanc-shock-tube.md) records the printed
  variants of that problem.
- **Cai et al.'s "tenfold".** Cai et al. write that the rl strategy reaches
  $N_\ell\approx20$ "and results in roughly a tenfold increase in remapping
  time" (§6); §5.2 says "nearly a tenfold increase" in $N_\ell$ and an
  "order of magnitude slower" remap. Their Table 3 gives
  $64781.5/3942.6=16.4$ for the remapping time and $19.7/2.0=9.85$ for the
  levels *(compiler check, not in the sources)*: "tenfold" fits the level
  ratio, and the measured remapping-time ratio is larger.
- **Two settings for the pseudo-time levels.** Gu et al. report three
  pseudo-time steps per remap at every resolution for a mild motion (nodes
  within one cell, Table 3.4), Cai et al. 4.7 to 19.7 levels with Gu et
  al.'s strategy under random rezoning at every physical step (Table 2).
  The motions differ, and Cai et al. attribute the growth to the
  discontinuous mesh velocity; the two tables do not contradict each
  other. Cai et al.'s "exact moments" comparison takes Gu et al.'s
  geometric treatment and pseudo-time strategy with Cai et al.'s own hybrid
  WENO, not Gu et al.'s multi-resolution WENO.
- **Stage geometry.** For the half-step stage of SSP-RK3 Cai et al. use
  the actual cell at $\tau_{\mathrm p}+\tfrac12\Delta\tau_{\mathrm p}$, where Gu
  et al. take the mean of the old and new areas (see the qualification on the
  quadratic area above).
- **Scope of Cai et al.'s remap.** Two-dimensional convex quadrilaterals
  with straight edges (Assumption 3.4); the paper prints no positivity
  treatment of the conserved variables, only the positivity of the evolved
  volume (Remark 4.13). It is an arXiv preprint without a journal version
  as of 2026-11-01.

# Citations

- [Van Leer (1979)](/sources/vanleer-1979.md) — §3.2 (Eqs. (92)–(100.5), Figs. 1–2), §3.3 (Eqs. (102)–(103), Fig. 4), App. B, Acknowledgments: Lagrange-plus-remap MUSCL.
- [Gu, Li, Cheng & Shu (2023)](/sources/gu-2023.md) — §1; §2.1–2.6, Eqs. (2.1)–(2.12), Theorems 2.1–2.2; §3.1–3.5, Tables 3.1–3.4, Figs. 6–20.
- [Ramani & Shkoller (2023)](/sources/ramani-2023.md) — §6.1, Eqs. (41)–(46) (ALE without remap; arXiv v2).
- [Cai, Cheng, Wu & Qiu (2026)](/sources/cai-2026.md) — §1.2; §3.1 Eqs. (3.7)–(3.18); §3.4 Remark 3.6; §4.2 Thm. 4.3, Prop. 4.4; §4.4 Thm. 4.7; §4.5 Eqs. (4.14)–(4.15), Remarks 4.12–4.13; §5.2 Tables 2–3; §5.3–5.4 Figs. 4–7; §6 (arXiv v1).
