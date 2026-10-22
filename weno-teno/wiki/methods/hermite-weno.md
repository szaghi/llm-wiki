---
type: Method
title: "Hermite WENO"
description: "Hermite WENO (HWENO) builds WENO candidates from cell averages and derivative or first-moment information, giving compact stencils; the page records the moment-based finite-volume HWENO (moment equations, multi-resolution hierarchy, moment modification, positivity-preserving hybrid), the finite-difference HWENO-R that drops the target-point derivative, and its use as a finite-element sensor."
status: established
aliases: [HWENO, Hermite WENO reconstruction, HWENO-R, HWENO-L, finite-difference HWENO, Zhong–Shu HWENO, moment-based HWENO, multi-resolution HWENO, MR-HWENO, hybrid HWENO, HWENO6-M5-I, HTENO, Hermite TENO]
tags: [weno, reconstruction, finite-volume, dg, compact-scheme]
timestamp: 2026-10-23T10:00:00Z
---

# Hermite WENO

Hermite WENO (HWENO) schemes, "based on the Hermite polynomials", were developed for nonlinear
conservation laws and Hamilton–Jacobi equations (Fu 2023, §1). A candidate polynomial is fitted not
only to cell averages but also to derivative information (derivative averages in the Qiu–Shu schemes,
first moments in the more recent ones, or a neighbour's whole polynomial in element methods), so a
given order needs fewer cells. Fan, Zhang & Qiu (2021, §1) summarize the trade-off: HWENO schemes have
more compact stencils than WENO schemes and higher resolution at the same order, but they are in
practice less robust, and the extra equation for the derivative or moment raises their cost.

## Moment-based HWENO

The finite-volume HWENO of Zhao, Chen & Qiu, used by Fan et al. (2021, §3, Eqs. (3.2)–(3.6)) and by Li,
Shu & Qiu (2022, §2.1, Eqs. (2.2)–(2.8)), evolves the cell average $\bar u_i$ and the first moment
$\bar u^{(1)}_i=\frac1{\Delta x}\int_{I_i}u\,\frac{x-x_i}{\Delta x}\,dx$ (page-local symbol). Testing
$\partial_tu+\partial_xf=0$ with $1$ and $(x-x_i)/\Delta x$ — the $\mathbb P^1$
[discontinuous Galerkin](/methods/discontinuous-galerkin.md) weak form — gives

$$\frac{d\bar u_i}{dt}=-\frac{\hat f_{i+1/2}-\hat f_{i-1/2}}{\Delta x},\qquad
\frac{d\bar u^{(1)}_i}{dt}=-\frac{\hat f_{i+1/2}+\hat f_{i-1/2}}{2\Delta x}+\frac1{\Delta x^2}\int_{I_i}f(u)\,dx,$$

with the volume integral by the four-point Gauss–Lobatto rule on $x_{i\pm1/2}$,
$x_i\pm\frac{\sqrt5}{10}\Delta x$ (weights $\tfrac1{12},\tfrac5{12},\tfrac5{12},\tfrac1{12}$). Only
point values at these four points are reconstructed; the two boundary values feed the numerical flux.
Li et al. (2022, §1) contrast this with their earlier multi-resolution HWENO, which evolved derivative
values and reconstructed function and derivative values at cell boundaries. *(Compiler check, not in
the sources: for linear data $\bar u^{(1)}_i=u'\Delta x/12$, so the moment and derivative variables
agree up to a factor only for linear data.)*

## Sixth-order multi-resolution HWENO (HWENO6-M5-I)

Li, Shu & Qiu (2022, §2) build a sixth-order scheme on three cells in 1-D and $3\times3$ cells in 2-D
("the same size as the general HWENO scheme and more compact than the general WENO scheme of the same
order", Abstract; §4):

- **Hierarchy.** Central polynomials of degree 0, 2, 3, 5: the constant from $\bar u_i$ alone, the
  others from the averages of $I_{i-1},I_i,I_{i+1}$ and zero, one or three first moments (Eq. (2.9)), combined in the multi-resolution manner with linear weights
  $10^{l-1}$ and WENO-Z-type weights; in 2-D the over-determined fits keep the target average exactly
  and the rest in least squares ([multi-resolution WENO](/methods/multi-resolution-weno.md)).
- **Flux.** HLLC with a primitive-variable pressure estimate and pressure-dependent wave-speed
  coefficients, chosen "to better adapt to our high order scheme" (Eqs. (2.5)–(2.7);
  [HLL-family solvers](/methods/hll-riemann-solvers.md)).
- **Troubled cells.** A KXRCF indicator with exponent $(l+1)/3$, $l=5$, on the density, which needs no
  extra reconstruction (Eqs. (2.25), (2.31)–(2.34);
  [troubled-cell indicators](/definitions/troubled-cell-indicator.md)).
- **Moment modification.** In a flagged cell the first moment is replaced by that of the quartic
  fitted to the three neighbouring averages and the two neighbouring moments (Eq. (2.27)),
  $$\bar u^{(1)}_i\leftarrow-\tfrac5{76}\bar u_{i-1}+\tfrac5{76}\bar u_{i+1}-\tfrac{11}{38}\bar u^{(1)}_{i-1}-\tfrac{11}{38}\bar u^{(1)}_{i+1},$$
  and the reconstruction is repeated there (dimension by dimension in 2-D). *(Compiler check: the
  coefficients were recomputed from the quartic's moment conditions; they agree.)* The modified moment
  overwrites the evolved one.
- **Time step.** SSP-RK3 at CFL 0.6 in 1-D and 2-D ([SSP Runge–Kutta](/methods/ssp-runge-kutta.md)).

Remark 1 argues by Taylor expansion that the weights stay at $d_l(1+O(\Delta x^6))$ in smooth regions,
hence sixth order, and that without modification a discontinuity makes the first moment $O(1)$ and
magnifies the low-order layers, smearing the jump, whereas after modification all layers keep weights
near their linear ones, so that resolution "can be increased significantly". With the modification
only in flagged cells, $L^1$ orders at the finest grids are 5.96 (1-D Burgers, $3.95\times10^{-13}$),
6.36 (2-D Burgers), 6.03 (1-D Euler) and 6.49 (2-D Euler); modifying every cell (HWENO6-M5-NI) gives
fifth order, 4.88–5.10, "as expected" (Tables 3.1–3.4;
[Burgers tests](/benchmarks/burgers-equation-tests.md)). The unmodified HWENO6 blows up on the
[double Mach reflection](/benchmarks/double-mach-reflection.md); with the modification the scheme
gives sharper shocks than HWENO6 on the Lax, Shu–Osher, blast-wave, Sedov and
[forward-facing step](/benchmarks/forward-facing-step.md) problems (§3, figure comparisons only).

**Stability history.** Li et al. (2022, §1) state that the original Qiu–Shu HWENO "is not stable enough"
for the double Mach and forward-step problems, largely because first-derivative values become very
large near discontinuities, and that their own earlier multi-resolution HWENO improved resolution but
not stability, "since the first two layers in the hierarchy do not contain the information of the
first order derivative".

## Positivity-preserving hybrid HWENO for Navier–Stokes

Fan, Zhang & Qiu (2021) make the hybrid moment-based HWENO of Zhao, Chen & Qiu positivity-preserving
for compressible Navier–Stokes (Euler at $\mathrm{Re}=\infty$):

- **Hybrid.** A troubled-cell indicator selects the cells where the nonlinear HWENO reconstruction,
  preceded by a non-oscillatory limiter on the first moment, is used; elsewhere a linear Hermite
  reconstruction (§1, §4; [hybrid schemes](/methods/hybrid-weno.md)).
- **Flux.** A Lax–Friedrichs-type flux of the total (advective minus viscous) flux, whose coefficient
  must exceed $|v|+\frac1{2\rho^2e}\big(\sqrt{\rho^2q_h^2+2\rho^2e|\tau_v-p|^2}+\rho|q_h|\big)$ (page-local
  viscous stress $\tau_v$ and heat flux $q_h$), after Zhang 2017 (Eqs. (3.4)–(3.5)).
- **Theorem 1 (1-D).** With degree-$k$ reconstruction, the forward-Euler cell average stays in
  $G=\{\rho>0,\ \rho e>0\}$ if the interface traces and the Gauss–Lobatto residual state
  $(\bar u_i-\hat{\mathsf w}u^+_{i-1/2}-\hat{\mathsf w}u^-_{i+1/2})/(1-2\hat{\mathsf w})$ lie in $G$,
  under $\frac{\Delta t}{\Delta x}\max_i(\text{coefficient})\le\hat{\mathsf w}=\frac1{n_{\mathrm{GL}}(n_{\mathrm{GL}}-1)}$,
  $n_{\mathrm{GL}}=\lceil(k+3)/2\rceil$ (Eqs. (3.11)–(3.12); page-local $\hat{\mathsf w}$, the end
  Gauss–Lobatto weight, and $n_{\mathrm{GL}}$ the number of Gauss–Lobatto points, the source's $N$). Theorem 2 is the 2-D analogue (Eqs. (3.29)–(3.30)). Both are enforced by a density-then-
  internal-energy [scaling limiter](/methods/zhang-shu-scaling-limiter.md) on point values only
  ([bound preservation](/properties/bound-preservation.md)).
- **Viscous derivatives.** App. A reconstructs $u_x$ with HWENO at the interfaces of flagged stencils
  and linearly elsewhere; in 1-D the three Hermite cubics combine into the quintic's derivative with
  linear weights $\tfrac{11}{459},\tfrac{44}{765},\tfrac{124}{135}$, Jiang–Shu-type weights with
  exponent 2, and indicators summing only derivative orders 2–3 (App. A.1;
  [smoothness indicators](/definitions/smoothness-indicator.md)). *(Compiler check: the three weights
  sum to 1.)*

Results: about fifth order in 1-D and fourth order in 2-D at $\mathrm{Re}=100$ (Table 4.1); the hybrid
scheme of Zhao et al. without positivity preservation blows up on Examples 4.3–4.7 (Euler), which the
new one runs; the positivity-preserving hybrid saves 59.05–89.64 % of the CPU time of the
non-hybrid positivity-preserving HWENO, with troubled-cell fractions 0.97–19.57 % (Table 4.2;
[Sedov blast wave](/benchmarks/sedov-blast-wave.md), [Leblanc shock tube](/benchmarks/leblanc-shock-tube.md),
[double rarefaction](/benchmarks/double-rarefaction-problem.md)). A moment-based HWENO without the
first-moment modification and without positivity limiter is non-oscillatory on the Lax problem at
$\mathrm{Re}=100$ but oscillates and loses stability at higher Re, so the authors conclude that it
"itself is unstable" (Example 4.2, Fig. 4.1). On the Lax problem the positivity limiter is never
triggered: the first-moment limiter alone makes the hybrid scheme "already very stable". The authors
read that limiter as "artificial viscosity": fewer troubled cells at $\mathrm{Re}=1000$ give slightly
sharper fronts than at $\mathrm{Re}=\infty$ (Example 4.2, §5;
[artificial viscosity](/methods/artificial-viscosity.md)).

## Finite-difference HWENO without the target-point derivative (HWENO-R)

Finite-difference HWENO (Liu & Qiu; Zhao, Zhang & Qiu; Zhang & Zhao's HWENO-L, as recalled by Fan, Zhao,
Xiong & Qiu 2023, §1) evolves the point values $u_i$ together with $v_i=\partial_xu(x_i)$ through
$\partial_tv+\partial_x\big(f'(u)v\big)=0$, both in [conservative finite-difference](/definitions/conservative-finite-difference-scheme.md)
form with Lax–Friedrichs splitting of $f$ and of $f'(u)v$ (page-local $h_j$ the split derivative
fluxes; Eqs. (2.2)–(2.3)). Fan et al. (2023, §2.1) build **HWENO-R** for the Euler equations by
**dropping the derivative at the target point** from the flux reconstruction:

- the large candidate is the quartic $q_0$ matching the three point fluxes $f^+_{i-1},f^+_i,f^+_{i+1}$ as
  cell averages and the two derivative fluxes $h^+_{i-1},h^+_{i+1}$; the small candidates are the linear
  polynomials on $\{f^+_{i-1},f^+_i\}$ and $\{f^+_i,f^+_{i+1}\}$ (Fig. 2.1(a));
- $q_0(x_{i+1/2})=-\tfrac{23}{120}f^+_{i-1}+\tfrac{19}{30}f^+_i+\tfrac{67}{120}f^+_{i+1}-\Delta x\big(\tfrac3{40}h^+_{i-1}+\tfrac7{40}h^+_{i+1}\big)$
  (sign corrected, see Qualifications), and the derivative flux is the linear value
  $\hat h^+_{i+1/2}=q_0'(x_{i+1/2})=\tfrac1{8\Delta x}(3f^+_{i-1}-16f^+_i+13f^+_{i+1})+\tfrac18h^+_{i-1}-\tfrac38h^+_{i+1}$,
  which "works well without spurious oscillations" (Eq. (2.5));
- the nonlinear combination is the [CWENO](/methods/cweno.md)/WENO-ZQ one with
  $\tau=\big(\tfrac12(|\beta_0-\beta_1|+|\beta_0-\beta_2|)\big)^2$ (page-local), $\epsilon=10^{-10}$ and any
  positive linear weights, recommended $(0.99,0.005,0.005)$; $\tau/(\beta_k+\epsilon)=O(\Delta x^4)$ is
  asserted by Taylor expansion (Step III);
- the derivative unknowns pass through a fifth-order HWENO limiter, a point-value Hermite quartic and two
  linear interpolants with weights $(0.9,0.05,0.05)$, but only in the stage values of SSP-RK3; the
  spatial operator sees the unlimited derivatives (Eqs. (2.6)–(2.7));
- in 2-D the mixed derivative fluxes are fourth-order linear,
  $\tfrac1{12}(-q_{i-1}+7q_i+7q_{i+1}-q_{i+2})$ (page-local $q$), not the third-order split
  reconstruction of earlier schemes (Eq. (2.11)); reconstruction is characteristic-wise for the main
  fluxes and component-wise for the derivative fluxes (Remark 2.2).

HWENO-L also uses $h^+_i$, i.e. $v_i$, in a quintic and a sixth-order reconstruction, but its limiter is fifth
order, so the scheme is fifth order; HWENO-R makes the reconstruction order equal the scheme order
(Remark 2.1). The authors attribute HWENO-L's failures to the unlimited $v_i$: after one step of the 1-D
[Sedov](/benchmarks/sedov-blast-wave.md) problem its density derivative exceeds 4000, against below 20
for HWENO-R, and HWENO-L fails even with a positivity-preserving flux limiter (Example 3.5, Fig. 3.9).
HWENO-R runs the 1-D and 2-D Sedov, [double rarefaction](/benchmarks/double-rarefaction-problem.md) and
[Leblanc](/benchmarks/leblanc-shock-tube.md) problems without positivity limiters; the Mach 2000
[jet](/benchmarks/high-mach-astrophysical-jet.md) and a Mach 10 reflection–diffraction problem need the
parametrized flux limiter of Xiong, Qiu & Xu, active in 0.0146 % and 0.0012 % of cells
([positivity-preserving flux limiter](/methods/positivity-preserving-flux-limiter.md)). It is fifth order
on Burgers, 1-D Euler and a near-vacuum isentropic vortex (Tables 3.1–3.3), more accurate than WENO-ZQ
at equal CPU time (CPU ratios 1.2–1.8, error ratios about 1/5), slightly cheaper than HWENO-L, and on
the [Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md) at $120\times480$ comparable
to WENO-ZQ at $240\times960$ (Example 3.13). Fan et al. (§1) count three points for fifth-order HWENO
against five for WENO.

## HWENO candidates on a finite element mesh

Kuzmin & Vedral (2023, §5, Eq. (11)) outline, "without claiming originality", the Zhong–Shu-type
construction they use. For a cell $K_e$ with finite element polynomial $u_h^e\in\mathbb P^N$ and its
von Neumann neighbours $e'$ (sharing a point, edge or face; at least $d+1$ of them in $d$ dimensions):

- each neighbour polynomial is extended into $K_e$ and its mean corrected,
  $$u^e_{h,l}(x)=u_h^{e'}(x)+\pi_e\big(u_h^e-u_h^{e'}\big),\qquad \pi_ev=\frac1{|K_e|}\int_{K_e}v\,dx,$$
  so that the candidate has the cell's mean and the neighbour's derivatives; the cell's own
  polynomial is the candidate $l=0$ (page-local index $l$, mean operator $\pi_e$);
- the candidates are blended with linear weights that favour the central candidate,
  $\tilde\omega_0=1-m_e\cdot10^{-3}$, $\tilde\omega_l=10^{-3}$ ($m_e$ non-central candidates;
  $\tilde\omega_l=0.2$ for all five candidates in the KPP test), and Jiang–Shu-type nonlinear weights
  $\omega_l\propto\tilde\omega_l/(\epsilon+\beta_l)^2$, $\epsilon=10^{-6}$, with
  $\beta_l=\|u^e_{h,l}\|_e^{\mathsf q}$ a power of the scaled Sobolev seminorm of the candidate
  (page-local sensor exponent $\mathsf q\ge1$, $\mathsf q=1$ by default; not the registry's weight
  exponent $q$)
  ([smoothness indicators](/definitions/smoothness-indicator.md),
  [WENO-JS](/methods/weno-js-reconstruction.md)).

Because the seminorm contains only derivatives, the mean correction does not affect the indicator and
is unnecessary in practice (Remark 3). A smaller central linear weight makes shock detection more
reliable and the stabilization stronger (§5, used in the KPP test). Remark 4 proposes, without
implementing them, additional Hermite candidates from vertex neighbours and Lagrange candidates
interpolated on the convex hull of neighbouring barycentres, generalizing a DG-$\mathbb P^1$
construction of Luo et al. to arbitrary order.

## The simple WENO limiter for DG

The same candidates, the target polynomial and its mean-corrected neighbours, are the simple WENO
limiter of Zhong & Shu and its triangle version by Zhu, Zhong, Shu & Qiu, as recalled by Du, Shu &
Zhong (2022, §1, §3.1), which **overwrites** the DG polynomial of a troubled cell
([WENO limiters for DG](/methods/weno-limiter-dg.md)). Their improvement concerns systems: for each
edge normal $n_l$ of a triangle the original limiter projects all four polynomial vectors (target and
three neighbours) on the characteristic fields of the normal Jacobian at the target average; the new
one projects only the target polynomial $p_0$ and the corrected neighbour across edge $l$, combines
the two per field,

$$p^{\mathrm{new}}_l=\omega_0\,L_lp_0+\omega_1\,L_l\tilde p_l,\qquad \omega_i\propto\frac{d_i}{(\epsilon+\beta_i)^2},$$

maps back with $R_l$, and averages the three directional results with the neighbour areas as weights,
$p^{\mathrm{new}}_0=\sum_lR_lp^{\mathrm{new}}_l|K_l|/\sum_l|K_l|$ (Eqs. (3.1)–(3.8); page-local
$p$, $\tilde p_l$, $L_l$, $R_l$ for the polynomial vectors and the directional eigenvector matrices).
The linear weights are $d_0=0.999$, $d_1=0.001$ on triangles and $0.9995$, $0.0005$ on polygonal meshes
built from point clouds (where the direction is the centre-to-centre vector and $N_j$ neighbours give
$N_j$ two-polynomial combinations instead of one $(N_j+1)$-polynomial one, §3.2, Eq. (3.9)), and
$\epsilon=10^{-6}$; any positive $d_0+d_1=1$ is argued to keep the accuracy, since both candidates are
$(N+1)$th-order in smooth regions (§3.1). The cell average is preserved because each neighbour is
shifted to the target average ([characteristic decomposition](/methods/characteristic-decomposition.md),
[troubled-cell indicators](/definitions/troubled-cell-indicator.md)). Numerically, with the KXRCF
threshold lowered so that up to 91 % of the cells are flagged, both limiters keep the design order
and the error size of unlimited DG for $\mathbb P^1$–$\mathbb P^3$ (Tables 4.1–4.6), the new one
perturbing the error less (e.g. $\mathbb P^1$, $h=2\pi/10$, $L^2$ $2.46\times10^{-2}$ against
$3.87\times10^{-2}$, unlimited $5.63\times10^{-3}$); on shock problems it saves 6–55 % of the CPU time,
most for $\mathbb P^2$ and point clouds, and reduces the spurious Mach stem of the $\mathbb P^2$
[forward-facing step](/benchmarks/forward-facing-step.md) (Tables 4.7–4.18, Fig. 4.9). The authors'
attribution of the sharper resolution to "less information being used for reconstruction in each
direction" is not isolated by any experiment.

Other passages only cite HWENO limiters for RKDG: Du, Shu & Zhong (2022, §1) as earlier
wider-stencil and compact WENO limiters; Yu & Hesthaven (2022, §1) as reducing the stencil, adding that WENO and HWENO
limiters reconstructing whole polynomials are "difficult to extend … to higher order cases (typically
higher than 3rd order) due to the stability issue of extrapolation"; Bai & Li (2022, §3.1.5) use a
simple or Hermite WENO limiter (their refs. [90, 91]) only on their two-phase Shu–Osher problem.

## Use as a sensor, not a limiter

Classical RKDG schemes with WENO or HWENO limiters **overwrite** the solution in troubled cells by the
reconstruction. Kuzmin & Vedral (2023, Remark 2) do not: the reconstruction $u_h^{e,*}$ serves only to
compute a cellwise blending factor

$$\varsigma_e=1-\min\Big\{1,\Big(\frac{\|u_h^e-u_h^{e,*}\|_e}{\|u_h^e\|_e}\Big)^{\mathsf q}\Big\}$$

(page-local; the source writes $\gamma_e$ and $q$; Eq. (9)), which blends a high-order symmetric projection stabilization with low-order
artificial viscosity, so the semi-discrete scheme keeps the structure of a continuous Galerkin method
([WENO-stabilized continuous Galerkin](/methods/weno-stabilized-continuous-galerkin.md),
[artificial viscosity](/methods/artificial-viscosity.md),
[troubled-cell indicators](/definitions/troubled-cell-indicator.md)). They argue that overwriting
DG-WENO schemes "have more in common with finite volume methods". If the finite element solution on
the stencil union is a polynomial of degree $\le N$, every candidate equals it, $\varsigma_e=1$ for any
nonlinear weights, and polynomial solutions are reproduced exactly (Remark 6). The moment modification
of Li, Shu & Qiu (2022), by contrast, does overwrite the evolved moment in flagged cells.

## Hermite TENO

Fu (2023, §3.10) lists HTENO (Wibisono et al.), a Hermite-polynomial compact variant of
[TENO](/methods/targeted-eno.md); Ye et al. (2022, §1) cite it among the TENO extensions. No formulas
are given in the ingested sources.

## Qualifications

- **Linear weights.** Li, Shu & Qiu (2022) state in the Abstract and §4 that the linear weights "can be
  any positive numbers as long as their sum equals one", but in §1 that their gap "cannot be too
  large" and in Remark 1 that larger weights on higher-degree polynomials make the scheme less stable;
  "any" holds for smooth-region accuracy only.
- **HWENO-R slips and limits.** Fan et al. (2023, §2.1) print
  $-\Delta x\big(\tfrac3{40}h^+_{i-1}-\tfrac7{40}h^+_{i+1}\big)$ in $q_0(x_{i+1/2})$. *(Compiler check, not in
  the sources: solving the five Hermite conditions gives $+\tfrac7{40}$; for $f=x$ the corrected value
  returns $x_{i+1/2}$, the printed one does not.)* Their printed indicator of the limiter's point-value
  quartic does not equal the Jiang–Shu integral of that quartic
  ([smoothness indicators](/definitions/smoothness-indicator.md)). "Arbitrary" positive linear weights
  coexist with a recommended band $\gamma_0/\gamma_1\in[100,300]$, $d_0/d_1\in[10,30]$ (Example 3.4), and
  "robust without positivity limiters" coexists with negative minimum pressures on coarse meshes of the
  near-vacuum vortex run without limiters (Table 3.3).
- **Heuristic resolution argument.** Remark 1 of Li, Shu & Qiu (2022) assumes the low-order indicators
  stay $O(\Delta x^2)$ in a cell that contains a discontinuity, and that after modification all
  indicators behave as on smooth data, although the modified moment is built from averages that
  straddle the jump; the resolution gain is supported by figures only. Their claim of "smaller errors
  than multi-resolution WENO under the same meshes" (§4) is not shown in the paper.
- Li, Shu & Qiu (2022) justify the KXRCF exponent $(l+1)/3$ by asking the indicator to converge "twice
  as fast" in smooth regions as it diverges at discontinuities; Krivodonova et al. use $(k+1)/2$.
- **Order of the positivity CFL under SSP-RK3.** Fan et al. (2021, §3.3) state that Theorems 1–2 hold
  for SSP-RK3 "if the CFL is one third" of the forward-Euler bound; the Shu–Osher RK3 is a convex
  combination of forward-Euler steps of size $\Delta t$, so the convexity argument gives the
  forward-Euler bound itself, not a third of it *(compiler check, not in the sources)*; Wong et al.
  (2021, §5.3) state this for their limiters, the SSP-RK extension being "trivial since SSPRK time
  stepping schemes are convex combinations of Euler forward steps"
  ([SSP Runge–Kutta](/methods/ssp-runge-kutta.md)).
- Fan et al. (2021) print $\rho e=(\gamma-1)(E-\tfrac12m^2/\rho)$ in Eq. (3.7) (the pressure; their
  2-D Eq. (3.25) has no $(\gamma-1)$) and a numerator $\rho e(\hat q^k)-\varepsilon$ in the implemented
  1-D energy limiter, where (3.15) and the 2-D version give $\rho e(\bar P_i)-\varepsilon$; the
  Lax-problem CPU savings quoted in the text (77.68 %, 75.08 %) differ from Table 4.2 (71.20 %,
  69.98 %). The 2-D derivative reconstruction is third order (App. A.2) while the 2-D scheme is
  reported fourth order.
- Li et al. (2022, Eq. (8)) — the WENO-ZN paper — call the rescaled Legendre basis used by Balsara et
  al. for smoothness indicators "Hermite polynomials"; that reconstruction is not Hermite WENO.
- The nonlinear HWENO reconstruction of Kuzmin & Vedral is printed once with a tilde
  ($\tilde u_h^{e,*}$) and referred to without it elsewhere; they are the same object.

# Citations

- [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) — Abstract; §1; §2.1–2.2, Eqs. (2.2)–(2.34), (2.36)–(2.59), Remarks 1–3; §3, Tables 3.1–3.4, Examples 3.5–3.10; §4.
- [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) — §1; §3, Eqs. (3.2)–(3.33), Theorems 1–2; §4, Tables 4.1–4.2, Fig. 4.1; §5; App. A.
- [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) — §3, Eq. (8); Eq. (9); §5, Eq. (11), Remarks 2–4, 6; §7.4.
- [Fu (2023)](/sources/fu-2023.md) — §1; §3.10.
- [Ye et al. (2022)](/sources/ye-2022.md) — §1.
- [Li et al. (2022)](/sources/li-2022-b.md) — §2, Eq. (8).
- [Du, Shu & Zhong (2022)](/sources/du-2022.md) — §1; §3.1–3.2, Eqs. (3.1)–(3.9); §4, Tables 4.1–4.18, Fig. 4.9.
- [Yu & Hesthaven (2022)](/sources/yu-2022.md) — §1.
- [Bai & Li (2022)](/sources/bai-2022.md) — §2.6; §3.1.5.
- [Fan, Zhao, Xiong & Qiu (2023)](/sources/fan-2023.md) — §1; §2.1–2.3, Eqs. (2.2)–(2.11), Remarks 2.1–2.4; §3, Tables 3.1–3.4, Examples 3.4–3.13, Fig. 3.9; App.
