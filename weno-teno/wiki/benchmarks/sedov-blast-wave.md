---
type: Benchmark
title: "Sedov blast wave"
description: "Point-explosion benchmark: the energy of one or a few cells drives a strong shock into cold gas of near-zero pressure, in 1D, in a 2D corner or centre and in 3D, with an exact similarity solution; tests positivity preservation at pressure ratios near 10^20, positivity-limited DG, ALE remapping and grid-aligned shock stability, with a gas–liquid variant."
status: established
aliases: [Sedov problem, Sedov–Taylor blast wave, point explosion, Sedov blast]
tags: [benchmark, positivity, bound-preserving, weno]
timestamp: 2026-10-23T11:06:00Z
---

# Sedov blast wave

A finite energy is deposited in a single cell of a gas at rest whose
internal energy elsewhere is $10^{-12}$ per unit volume. A strong
shock (planar in 1D, cylindrical in the 2D corner version) runs outwards, and behind it the density
falls towards zero at the centre, so the solution combines a shock of
enormous strength with a near-vacuum core. The problem has a
self-similar exact solution, which four of the one-dimensional sources
use as reference (the three Fan et al. papers and Li, Shu & Qiu). Pressure is a tiny difference of large energies near the
centre, so a high-order scheme without a
[positivity](/properties/bound-preservation.md) safeguard tends to
produce negative pressure; the sources use the test as a robustness
check and read resolution from the height of the density peak behind
the shock.

## One-dimensional version

The common data, written in $(\rho,v,E)$: $(1,0,10^{-12})$ on $[-2,2]$
except the centre cell, where $E=3200000/\Delta x$, so that the
deposited energy is $3.2\times10^6$ whatever the grid; inlet/outlet
boundaries; $t=0.001$. On 400 cells ($\Delta x=0.01$) the centre cell
holds $E=3.2\times10^8$, $3.2\times10^{20}$ times the ambient value
*(compiler check, not in the sources)*.

| Source | Cells | Reference | Scheme |
|---|---|---|---|
| [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) Ex. 4.4 | 400 | exact solution | positivity-preserving hybrid [HWENO](/methods/hermite-weno.md), Euler and Navier–Stokes ($\mathrm{Re}=1000$) |
| [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) Ex. 3.8 | 400 | exact solution | moment-based multi-resolution HWENO, with and without modified first moments |
| [Wang et al. (2021)](/sources/wang-2021.md) Example 5.5a | 400 | WENO-JS5, 6400 | [multi-resolution WENO](/methods/multi-resolution-weno.md) (New WENO5, original WENO5-MR), WENO-AO5, WENO-JS5 |
| [Fan, Zhang & Qiu (2022)](/sources/fan-2022.md) Example 5.3 | 400 | exact solution | finite-difference WENO-JS5, JS7, ZQ5 with the [positivity-preserving Navier–Stokes flux](/methods/positivity-preserving-navier-stokes-flux.md), $\mathrm{Re}=1000$ |
| [Fan, Zhao, Xiong & Qiu (2023)](/sources/fan-2023.md) Ex. 3.5 | 800 | exact solution | finite-difference HWENO-R, HWENO-L, WENO-ZQ; outflow boundaries |
| [Li, Li, Don & Wang (2023)](/sources/li-2023.md) §3.3 | 800 ($\Delta x=5\times10^{-3}$) | — | MR-AWENO-Si and MR-AWENO with a [PP flux limiter](/methods/positivity-preserving-flux-limiter.md) |
| [Li, Chen & Ren (2022)](/sources/li-2022.md) §4.2 | 800 | — | hybrid MDCD-HY and MDAD-HY, TENO-HY |
| [Zhang & Zhu (2024)](/sources/zhang-2024-c.md) Ex. 3.7 | 400 points or cells | — | ghost multi-resolution GMR-WENO3/5/7 vs [MR-WENO](/methods/multi-resolution-weno.md), finite differences and finite volumes |

Li, Li, Don & Wang and Li, Chen & Ren print the same blast in
$(\rho,v,p)$: pressure $4\times10^{-13}$, and $2.56\times10^8$ in the
cell $|x|\le\Delta x/2$ (Li et al. 2023a), or $1.28\times10^6/\Delta x$ in
the cell centred at $x=2$ with zero-gradient boundaries (Li, Chen &
Ren, who print no domain; a centre at $x=2$ suggests $[0,4]$). With
$\gamma=1.4$, $p=(\gamma-1)E$ maps $4\times10^{-13}$ to $E=10^{-12}$ and
$1.28\times10^6/\Delta x$ to $E=3.2\times10^6/\Delta x$, and
$2.56\times10^8\times5\times10^{-3}=1.28\times10^6$, so all are the
common data *(compiler check, not in the sources)*. Li et al. (2023a)
call the pressure ratio $O(10^{21})$. Wang et al. attribute the setup to Zhang & Shu (2012). Li, Shu & Qiu
print the deposited cell as "the centre cell" and plot density,
velocity, pressure and the troubled cells (Fig. 3.6).

## Two-dimensional corner version

The blast is placed in the lower-left corner cell of $[0,1.1]^2$ with
reflecting (symmetry) left and bottom boundaries and outflow elsewhere,
$\rho=1$, $v=0$, on $160\times160$ cells ($\Delta x=\Delta y=1.1/160$).

- [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) Ex. 4.6: $E=10^{-12}$
  except the corner cell, where $E=0.244816/(\Delta x\Delta y)$; $t=1$;
  30 density contours from 0.95 to 5 (Fig. 4.6).
- [Fu (2021)](/sources/fu-2021.md) §5.7.2: pressure $4\times10^{-13}$
  except the corner cell, where $p=9.79264\times10^{4}/(\Delta x\Delta y)$;
  $t=10^{-3}$; $\gamma$ not printed; [TENO-AA](/methods/adaptive-teno.md)
  with LLF splitting and the
  [positivity-preserving flux limiter](/methods/positivity-preserving-flux-limiter.md).
- [Yu & Hesthaven (2022)](/sources/yu-2022.md) §5.4.3, after Xiong,
  Qiu & Xu's positivity-preserving flux-limiter paper (their ref. [62]):
  the data of Fan, Zhang & Qiu (2021) on triangles of
  size $1.1/160$, the total energy $0.244816/(\Delta x\Delta y)$ put in
  the two triangles at the lower-left corner, inviscid walls on the left
  and bottom and extrapolation elsewhere, $t=1$; nodal DG with
  ANN-predicted [artificial viscosity](/methods/artificial-viscosity.md)
  and no positivity limiter mentioned.

The two setups are one problem under the similarity scaling of the
blast *(compiler check, not in the sources)*. With $\gamma=1.4$,
$p=(\gamma-1)E$ turns Fan, Zhang & Qiu's ambient $E=10^{-12}$ into Fu's
$p=4\times10^{-13}$ and their corner energy into
$p=0.0979264/(\Delta x\Delta y)$, which is $10^{-6}$ times Fu's corner
pressure. Fu's run thus deposits $10^6$ times the energy and stops at
$10^{-3}$ times the time. A cylindrical blast of energy $E_0$ per unit length (page-local; the
corner run is a quarter of it) in gas of density $\rho$ has, by
dimensional analysis, a radius $R\propto(E_0t^2/\rho)^{1/4}$, and
$E_0t^2$ is the same in both runs, so the shock reaches the same radius; velocities are $10^3$ times larger in
Fu's run and its ambient pressure is relatively $10^6$ times smaller,
both immaterial for a strong blast. Fu's printed factor $\times10^4$ is
therefore consistent with a rescaled run, not evidence of a misprint.

**Lagrangian and ALE corner run.** [Gu, Li, Cheng & Shu (2023)](/sources/gu-2023.md)
§3.5.1 run the corner blast on a moving mesh of $35\times35$ cells of
$[0,1.1]^2$: $\rho=1$, $v=0$, specific internal energy $e=10^{-14}$
except $182.09$ in the cell containing the origin, $\gamma=1.4$,
$p=(\gamma-1)\rho e$, reflective boundaries on all four sides, $t=1$.
The deposited energy per unit depth is
$182.09\,(1.1/35)^2\approx0.180$ *(compiler check, not in the
sources)*. Both the pure Lagrangian scheme (the third-order
positivity-preserving ENO Lagrangian scheme of Cheng & Shu) and the
ALE method with their positivity-preserving multi-resolution WENO
[conservative remapping](/methods/conservative-remapping.md) every 20
steps capture the density peak and shock position and keep the radial
symmetry, with better mesh quality in the ALE run (Figs. 13–14).

Two further corner runs use the same data on $320\times320$ cells
($\Delta x=1.1/320$), $t=1$: [Fan, Zhang & Qiu (2022)](/sources/fan-2022.md)
Example 5.5, at $\mathrm{Re}=1000$ and $\mathrm{Re}=\infty$, 20 density
contours from 0.1 to 5 (Fig. 5.4), and
[Fan, Zhao, Xiong & Qiu (2023)](/sources/fan-2023.md) Ex. 3.10, Euler,
without positivity limiter.

## Centred two-dimensional version

**Smoothed deposit for positivity-limited DG.**
[Lin, Chan & Tomas (2023)](/sources/lin-2023.md) §8.3 (arXiv v2) put
the energy $E_0=1$ in the disc $r<r_0$, $r_0=4h$, $h=3/K_{1D}$ (page-local
element count per direction), of $[-1.5,1.5]^2$ as the uniform pressure
$p=(\gamma-1)E_0/(\pi r_0^2)$, with $\rho=1$, $v=0$, ambient
$p=10^{-5}$, $\gamma=1.4$, periodic boundaries, $T=1$. With $N=3$
entropy-stable DG on $K_{1D}=100$ quadrilaterals and triangles, blended
elementwise with a low-order positivity-preserving scheme under relaxed
bounds (relaxation $\zeta_{\mathrm r}$, their $\zeta$), all three configurations ($\zeta_{\mathrm r}=0.1$ without and with
shock-capturing blending, $\zeta_{\mathrm r}=0.5$ without) remain robust; with
$\zeta_{\mathrm r}=0.1$ alone spurious oscillations appear on both meshes, and
shock capturing, or to some extent $\zeta_{\mathrm r}=0.5$, reduces them
(Figs. 7–8, density on a log scale truncated to $[0.01,6]$). See
[convex limiting](/methods/convex-limiting.md).

**FLASH-type deposit for monolithic convex limiting.**
[Rueda-Ramírez et al. (2024)](/sources/ruedaramirez-2024.md) §3.4, Eq.
(56) (arXiv v1) use the same kind of deposit, after the FLASH setup:
$\rho=1$, $v=0$, ambient $p_0=10^{-5}$, and
$p=(\gamma-1)e_0/(\pi r_0^2)$ for $r<r_0=0.21875$ with energy $e_0=1$
(page-local), on the periodic $[-2,2]^2$ with $64\times64$ elements of
degree $N=3$, Chandrashekar's entropy-conservative volume flux, CFL 0.9,
to $t=3$; $\gamma$ is not printed for this test. They compare three
orderings of their limiters of LGL-DGSEM: A, sequential limiting of
density, velocity and specific total energy under local bounds, then
the sharp pressure fix and the entropy limiter, shows "artifacts at
the shock front"; B, limiting of the density bar states only, with the
resulting factor applied to all conserved fluxes, then pressure and
entropy, "removes the Carbuncle-like artefacts"; C, B followed by
sequential limiting, removes them too, needs the least pressure limiting
and no entropy limiting at $t=3$, but is "clearly more dissipative"
(Figs. 5–7). See [convex limiting](/methods/convex-limiting.md) and
[carbuncle phenomenon](/definitions/carbuncle-phenomenon.md).

### Grid-aligned instability

[Hu, Yuan & Zhao (2022)](/sources/hu-2022.md) §5.9 place the blast in
the four central cells of $[0,2.4]^2$, $960\times960$ cells:
$(\rho,v_1,v_2,p)=(1,0,0,10^{-10})$ except $p=3.5\times10^5$ in those
cells, reflecting walls, CFL 0.5, $t=0.1$, second-order MUSCL with
second-order TVD Runge–Kutta, $\gamma=1.4$. The test serves as a probe
of the [carbuncle phenomenon](/definitions/carbuncle-phenomenon.md):
where the cylindrical shock is aligned with the grid lines, HLLC and
HLLEM, "especially the latter", produce shock instabilities, while
their shock-stable HLLEM variant RHLLEM-LD does not (§5.9); see
[HLL-family solvers](/methods/hll-riemann-solvers.md). The deposited
energy is $4\,\Delta x^2p/(\gamma-1)=21.9$ with $\Delta x=0.0025$
*(compiler check, not in the sources)*.

## Three-dimensional version

[Lesur et al. (2023)](/sources/lesur-2023.md) §4.1 (arXiv v1) validate
the [IDEFIX](/software/idefix.md) code on a Sedov–Taylor blast with
$\gamma=5/3$, $\rho=1$, ambient $P=10^{-2}$ and an energy 1 deposited as
pressure in a sphere of radius $r_i$ (value not printed), $t=0.1$, HLL
solver, linear reconstruction and RK2. They run it on a periodic
Cartesian box of side 1 with $512^3$ cells and on a spherical grid
$n_r\times n_\theta\times n_\phi=256\times256\times512$ covering
$r\in[0.5,1.5]$, $\theta\in[0,0.7]$, $\phi\in[0,2\pi]$, with the blast
at $(x,y,z)=(0.1,0,1)$, close to the polar axis: the spherical shock
crosses the axis, where IDEFIX applies its axis regularity boundary
condition, and the test shows that it propagates through the axis
(Figs. 4–5). With an ambient pressure of $10^{-2}$ this blast is far
from the near-vacuum regime of the other versions.

## Gas–liquid version

[Wong et al. (2021)](/sources/wong-2021.md) §6.4 run a planar
multi-material Sedov problem in the
[five-equation model](/definitions/five-equation-model.md): water
($\gamma=6.12$, stiffening pressure $3.43\times10^8$ Pa) with partial
density 1000 kg m$^{-3}$ and pressure $-3.0\times10^7$ Pa fills
$[0,4]$ m, except the centre cell, which holds air with partial density
1 kg m$^{-3}$ and pressure $1.28\times10^6/\Delta x$ Pa; 401 points,
$t=10^{-3}$ s, reference 4001 points. The negative water pressure is
admissible because the
[stiffened-gas](/definitions/stiffened-gas-equation-of-state.md)
condition requires only $p$ plus the stiffening pressure to be positive.
Both first-order HLLC and their positivity-preserving
[WCNS](/methods/weighted-compact-nonlinear-scheme.md) are free of
spurious oscillations, and the WCNS gives much sharper shocks
(Figs. 9–10).

## Findings across sources

**A positivity safeguard is the price of running the test.** Fan,
Zhang & Qiu (2021) state that the earlier hybrid HWENO of Zhao, Chen & Qiu blows up on
both Sedov problems from loss of positivity (no figure shown); their
scaling limiter is triggered in 3.00 % of the cells in 1D and 1.09 % in
2D, identically for the hybrid and non-hybrid positivity-preserving
schemes (Table 4.2). Fu computes the corner blast, like all the author's
extreme cases, with the positivity-preserving flux limiter and reports
it stable (§5.7). Wang et al. use no
positivity limiter: the ratio of the linear weights "used in this
paper" is "so large" that the scheme cannot run the extreme problems
robustly, and they switch to the weights of the original
multi-resolution scheme (Example 5.5); which weights the paper uses
elsewhere is ambiguous as printed (see
[multi-resolution WENO](/methods/multi-resolution-weno.md)).

Fan, Zhang & Qiu (2022) state that without their positivity flux and
limiter all three WENO schemes blow up on the Sedov tests; in 2D their
limiter acts on 0.303 %, 0.248 % and 0.299 % of the cells per step for
WENO-JS5, JS7 and ZQ5 at $\mathrm{Re}=\infty$, and 0.309 %, 0.119 % and
0.139 % at $\mathrm{Re}=1000$ (Examples 5.3, 5.5). Fan, Zhao, Xiong &
Qiu run both Sedov problems with HWENO-R **without** a positivity
limiter, while HWENO-L, whose flux reconstruction uses the unrestricted
derivative, fails in 1D even with the parametrized PP flux limiter:
after one step its density derivative exceeds 4000, against less than
20 for HWENO-R, and the limiter "can keep the positivity … but cannot
control numerical oscillations" (Ex. 3.5, Fig. 3.9). Li, Li, Don & Wang
use their PP limiter on both schemes; MR-AWENO oscillates near the
shocks at $x\approx\pm1.5$ and MR-AWENO-Si is sharper (§3.3, Fig. 6).
Li, Chen & Ren's hybrid schemes need case-specific thresholds,
$\psi_c=0.4$ for MDCD-HY and $0.8$ for MDAD-HY (against 0.5 on the
blast waves), and TENO-HY (with its optimized TENO6) fails "even with
$C_T=0.1$"; the shock front lies near $x=3.43$ (§4.2, Fig. 18); see
[MDCD schemes](/methods/mdcd-scheme.md).

Zhang & Zhu, who call the test an "extreme problem", find that both
their GMR-WENO and MR-WENO "work well" on the common data, plotting
density, velocity and pressure (Ex. 3.7, Figs. 3.13–3.14); the paper
names no positivity safeguard, and its Table 3.1 gives the GMR:MR time
ratios over its Examples 3.5–3.10 as 1:1.23 to 1:2.18 in finite
differences and 1:1.27 to 1:2.25 in finite volumes.

Yu & Hesthaven report that their artificial viscosity suppresses the
spurious oscillations at the strong shock and that its distribution
captures the symmetric structure of the blast (§5.4.3, Figs. 16–17);
the paper names no positivity safeguard for this run.

**Resolution of the density peak.** Wang et al. find WENO-JS5 and both
multi-resolution schemes similar, and all worse than WENO-AO5 near the
peak; they conjecture that near strong shocks of large pressure ratio
their algorithm reduces quickly to first order (Fig. 5.9). Li, Shu &
Qiu find their modified HWENO "much better" resolved than the unmodified
one (comment p. 31).

**Troubled cells and cost.** In Fan, Zhang & Qiu's (2021) hybrid scheme the
nonlinear reconstruction is applied only in troubled cells: 11.92 %
(Navier–Stokes) and 14.50 % (Euler) of the cells in 1D, 13.82 % and
14.62 % in 2D, concentrated in a band behind the shock. The hybrid
saves 68.86 % (Euler) and 69.02 % (Navier–Stokes) of the CPU time of
the non-hybrid scheme in 1D, 62.64 % and 63.64 % in 2D, hardware not
stated (Table 4.2).

## Qualifications

- Fu (2021) prints the corner-cell condition as "$x\le\Delta x$ and
  $x\le\Delta y$"; the second inequality must read $y\le\Delta y$.
- Among the 1D sources only Fan, Zhao, Xiong & Qiu and Li, Li, Don &
  Wang print $\gamma=1.4$ for the problem; Fan, Zhang & Qiu (2021) use
  $\gamma=1.4$ throughout their paper, the others print none.

# Citations

- [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) — §1; Ex. 4.4, Ex. 4.6, Fig. 4.6, Table 4.2.
- [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) — Ex. 3.8, Fig. 3.6; comment p. 31 (arXiv v1).
- [Wang et al. (2021)](/sources/wang-2021.md) — Example 5.5a, Fig. 5.9.
- [Fu (2021)](/sources/fu-2021.md) — §5.7.2, Eq. (44) (arXiv v1).
- [Wong et al. (2021)](/sources/wong-2021.md) — §6.4, Table 7, Figs. 9–10 (arXiv v1).
- [Yu & Hesthaven (2022)](/sources/yu-2022.md) — §5.4.3, Figs. 16–17.
- [Fan, Zhang & Qiu (2022)](/sources/fan-2022.md) — §5, Examples 5.3 and 5.5, Figs. 5.2, 5.4.
- [Fan, Zhao, Xiong & Qiu (2023)](/sources/fan-2023.md) — Ex. 3.5, Ex. 3.10, Fig. 3.9.
- [Li, Li, Don & Wang (2023)](/sources/li-2023.md) — §3.3, Fig. 6.
- [Li, Chen & Ren (2022)](/sources/li-2022.md) — §4.2, Fig. 18.
- [Hu, Yuan & Zhao (2022)](/sources/hu-2022.md) — §5.9.
- [Lesur et al. (2023)](/sources/lesur-2023.md) — §4.1, Figs. 4–5 (arXiv v1).
- [Gu, Li, Cheng & Shu (2023)](/sources/gu-2023.md) — §3.5.1, Figs. 13–14.
- [Lin, Chan & Tomas (2023)](/sources/lin-2023.md) — §8.3, Eq. (65), Figs. 7–8 (arXiv v2).
- [Rueda-Ramírez et al. (2024)](/sources/ruedaramirez-2024.md) — §3.4, Eqs. (56)–(58), Figs. 5–7 (arXiv v1).
- [Zhang & Zhu (2024)](/sources/zhang-2024-c.md) — Ex. 3.7, Figs. 3.13–3.14, Table 3.1.
