---
type: Benchmark
title: "MHD blast wave and rotor"
description: "Two-dimensional ideal-MHD robustness tests: the Balsara–Spicer blast wave (plasma beta about 2.5×10^-4), an extreme variant at pressure ratio 10^5, a 3D blast, relativistic (up to a field of 2000), two-fluid and radiative counterparts, and the first and second rotor problems, which probe pressure positivity and divergence errors; plus a smooth weak magnetic blast verifying entropy conservation of DG."
status: established
aliases: [magnetic blast wave, MHD blast, Balsara–Spicer blast wave, MHD rotor, second rotor problem, weak magnetic blast]
tags: [benchmark, mhd, positivity, entropy-stable]
timestamp: 2026-10-23T11:06:00Z
---

# MHD blast wave and rotor

Two classical robustness tests of ideal MHD sit next to each other in the
sources. In the **blast wave** a small disk of high pressure expands
into a strongly magnetized, low-pressure medium, so that thermal
pressure, a small difference of the total energy and the large
magnetic energy, is at risk of becoming negative. In the **rotor** a
dense disk spins in a uniform field; distortions of the flow near the
rotor are attributed in the literature the sources cite to divergence
errors. A third problem shares the name: a **weak
magnetic blast** with smooth data, used not as a robustness test but to
measure entropy conservation and entropy dissipation of DG schemes.

## Balsara–Spicer blast wave

[Liu et al. (2021)](/sources/liu-2021.md) §4.4, after Balsara & Spicer:
on $[-0.5,0.5]^2$ with outflow boundaries and $\gamma=1.4$,
$\rho=1$, $v=0$, $B=(100/\sqrt{4\pi},\ 0,\ 0)$, and $p=1000$ for
$r\le0.1$, $p=0.1$ otherwise; $t=0.01$ on $200^2$ cells. The ambient
plasma beta, page-local $\beta_{\mathrm p}=2p/|B|^2$, is
$2\cdot0.1/(10^4/4\pi)=2.51\times10^{-4}$, the value they print
*(compiler check, not in the sources)*.

Their second- and third-order locally divergence-free
[WLS-ENO](/methods/wls-eno.md) finite-volume scheme, with HLL flux,
Godunov–Powell source term and a Zhang–Shu-type
[scaling limiter](/methods/zhang-shu-scaling-limiter.md) on density and
pressure, produces no negative pressure, and its density is
"significantly smoother" than earlier published results (Fig. 13).

**One-step HLL-GRP.** [Liu, Feng & Wang (2023a)](/sources/liu-2023.md)
§4.4 run the same data (same domain, outgoing boundaries, $\gamma=1.4$,
$200^2$, $t=0.01$, 100 cores), printing $\beta_{\mathrm p}\approx2.51\times10^{-4}$,
with the same WLS-ENO reconstruction followed by a Barth–Jespersen-type
limiter on density and pressure at edge midpoints, which they call a
"PP limiter" while stating that no positivity proof is made. Their
one-step HLL [generalized Riemann problem](/methods/generalized-riemann-problem.md)
scheme produces no negative pressure; its profiles are "almost
identical" to those of a two-stage SSP-RK2 HLL scheme, its divergence
norm lies between those of the forward-Euler and RK2 HLL schemes, and
the divergence error concentrates at the shock front, where the plasma
beta is lowest (Figs. 8–11).

**Semi-implicit all-Mach finite volumes.** [Dematté et al. (2024)](/sources/dematte-2024.md)
§4.1.6 run the Balsara–Spicer data ($\rho=1$, $v=0$,
$B=(100/\sqrt{4\pi},0,0)$, $p=1000$ for $r\le0.1$ and $0.1$ otherwise) on
$[-0.5,0.5]^2$ with $1000^2$ cells to $t=0.01$, with their default
$\gamma=5/3$ (§4) instead of the $1.4$ of Liu et al., as a strong-shock
check of their cell-centred
[semi-implicit all-Mach scheme](/methods/semi-implicit-all-mach-scheme.md)
with MUSCL–Hancock advective reconstruction and staggered
[constrained transport](/methods/constrained-transport.md) (Fig. 10).
They report results in line with the literature, visually; the time
step is set by the flow speed, with a magnetosonic first step because
the initial velocity is zero (§4).

**All-Mach IMEX with constrained transport.** [Chen, Wu & Xiong (2023)](/sources/chen-2023-b.md)
Ex. 5.7 (arXiv v1) run a blast on $[-0.5,0.5]^2$ with periodic
boundaries: $\rho=1$, $v=0$, $B=(10\sin\theta,10\cos\theta,0)$ with
$\theta=\pi/4$, $p=100$ for $r\le0.125$ and $p=10$ otherwise, vector
potential $\mathsf A_3=5\sqrt2(-x+y)$ (page-local) extrapolated at first order outside;
$200^2$ points, sonic Mach parameter $\varepsilon=0.9$, $T=0.02$, in
their non-dimensional MHD scaling with $\gamma=5/3$. Their semi-implicit
IMEX WENO scheme with constrained transport keeps the maximum discrete
divergence at $2.87\times10^{-11}$, against $2.77\times10^{-11}$ for the
explicit WENO reference with constrained transport (Figs. 5.4–5.5; see
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)).

**Extreme variant.** [Dzanic & Witherden (2023)](/sources/dzanic-2023.md)
§5.5 (arXiv v2) raise the Balsara–Spicer field and inner pressure
tenfold, after Wu & Shu's extreme version: on $[-0.5,0.5]^2$, periodic,
$\gamma=5/3$, $\rho=1$, $v=0$, $B=(1000/\sqrt{4\pi},0)$, $p=10^4$ for
$r\le0.1$ and $p=0.1$ otherwise, a pressure ratio of $10^5$; $t=0.001$.
Their nodal DG with positivity-preserving
[entropy filtering](/methods/entropy-filtering.md) runs at
$\mathbb P_4$ on unstructured triangles of $h=1/200$ (about
$1.2\times10^5$ elements, $\Delta t=2\times10^{-7}$) and $h=1/400$ (about
$5\times10^5$, $\Delta t=10^{-7}$) with the HLL flux: the solution is
well behaved, discontinuities are resolved across one or two solution
nodes with thickness decreasing in proportion to $h$, and minor density
oscillations (mesh imprinting) appear on the coarse mesh (Figs. 10–13).
Without the positivity-preserving modifications the scheme "would
diverge almost instantly", as stated; HLL was "much better behaved"
than HLLC here. They print the plasma beta as $2.5\times10^{-4}$; with
$B_1=1000/\sqrt{4\pi}$ and $p=0.1$, $2p/\lvert B\rvert^2=2.51\times10^{-6}$,
and $2.5\times10^{-4}$ is the value of the original data
*(compiler check, not in the sources)*.

### Three-dimensional blast

Liu, Feng & Wang (2023a) §4.6 run a 3D blast after CESE
computations they cite: $\rho=1$, $v=0$,
$B_1=B_2=B_3=1/\sqrt3$, $p=10$ inside the sphere of radius 0.1 about
$(1.5,0,0)$ and $p=0.1$ outside, on $[1,2]\times[-0.5,0.5]^2$ with
outgoing boundaries, $\gamma=1.4$, $200^3$ cells, $t=0.2$, 512 cores.
The HLL-GRP profiles are almost identical to those of RK2, the HLL-GRP
and RK2 divergence norms coincide below that of the forward-Euler
scheme, the divergence is "controlled to the $10^{-3}$ magnitude", and
the results agree with the cited CESE runs (Figs. 16–20). In this
blast $2p/\lvert B\rvert^2=0.2$ in the ambient medium
*(compiler check, not in the sources)*, three orders of magnitude above
the Balsara–Spicer value.

[Berta et al. (2024)](/sources/berta-2024.md) §5.7, Table 3 (arXiv v4)
run three 3D blasts on $192^3$ zones in a cube of side $L$ centred at
the origin, zero-gradient boundaries, an over-pressurized sphere of
radius $r_0$, and an oblique uniform field
$B=B_0(\sin\theta_B\cos\phi_B,\ \sin\theta_B\sin\phi_B,\ \cos\theta_B)$ with
$\theta_B=\pi/2$, $\phi_B=\pi/4$ (page-local angles), i.e. along the
diagonal of the $xy$ plane:

| Case | $\rho_{\mathrm{in}}$, $\rho_{\mathrm{out}}$ | $p_{\mathrm{in}}$, $p_{\mathrm{out}}$ | $B_0$ | $\gamma$ | $r_0$, $L$ | $t$ | solver | energy correction |
|---|---|---|---|---|---|---|---|---|
| C1 (MHD, Felker & Stone's with three times the magnetization) | 1, 1 | 10, 0.1 | 3 | 5/3 | 0.1, 1 | 0.2 | HLL | no |
| C2 (MHD, Balsara & Spicer) | 1, 1 | $10^3$, 0.1 | $100/\sqrt{4\pi}$ | 1.4 | 0.1, 1 | 0.01 | HLL | yes |
| R1 (RMHD) | $10^{-2}$, $10^{-4}$ | 1, $5\times10^{-3}$ | 1 | 4/3 | 0.08, 6 | 4 | GFORCE | yes |

The ambient $\beta_{\mathrm p}$ is $0.022$ (C1), $2.51\times10^{-4}$ (C2)
and $0.01$ in the lab frame (R1) *(compiler check, not in the
sources)*. C1 has "the largest magnetization our scheme can afford"
without the energy-correction step, which is applied, still at second
order, in C2 and R1. Their fourth-order finite-volume scheme resolves
the anisotropic, oval fast shock and the two plasma blobs moving along
the field and keeps the point symmetry (Figs. 11–13); the order
reduction ("fallback") to WENO3 or linear reconstruction in cells
flagged by a discontinuity detector "played an essential role" in
this test (see [troubled-cell indicators](/definitions/troubled-cell-indicator.md)).

### Relativistic MHD blast

[Ding & Wu (2024)](/sources/ding-2024-b.md) Example 5.8 run the same
relativistic blast geometry ($[-6,6]^2$, $\rho=10^{-2}$, $p=1$ for $r<0.8$,
$\rho=10^{-4}$, $p=5\times10^{-4}$ for $r>1$, a linear taper in between,
$v=0$, $B=(B_{\mathrm a},0,0)$, $t=4$, outflow boundaries) with the
equation of state they label IP, specific enthalpy
$h=2p/\rho+\sqrt{1+4(p/\rho)^2}$ (their Eq. (87)), instead of $\gamma=4/3$, on $400^2$ cells, for $B_{\mathrm a}=0.1$, $0.5$ and
$2000$ (page-local field amplitude; Figs. 10–11). Their $\mathbb P^2$
bound-preserving, locally divergence-free central DG scheme
([discontinuous Galerkin](/methods/discontinuous-galerkin.md), central
variant; [geometric quasilinearization](/methods/geometric-quasilinearization.md))
runs all three cases; without the bound-preserving limiter it fails. The
global divergence error stays small and the local one is zero by
construction. With $B_{\mathrm a}=2000$ the ambient
$2p/\lvert B\rvert^2$ is $2.5\times10^{-10}$ *(compiler check, not in
the sources)*, far below every other blast on this page.

[Duan & Tang (2022)](/sources/duan-2022.md) Ex. 6.5 (arXiv v1) run the
relativistic-MHD blast after earlier relativistic papers: on
$[-6,6]^2$ with outflow boundaries, $\gamma=4/3$, $B_1=0.1$, an
explosion zone $r<0.8$ with $\rho=0.01$, $p=1$, an ambient medium
$r>1$ with $\rho=10^{-4}$, $p=5\times10^{-4}$, and a linear taper of
$\rho$ and $p$ in between; $t=4$. The lab-frame ratio $2p/\lvert B\rvert^2$
of the ambient medium is $0.1$ *(compiler check, not in the sources)*,
so this blast is far less magnetically dominated than the Newtonian one
above. Their fifth-order entropy-stable scheme on an
[adaptive moving mesh](/methods/adaptive-moving-mesh.md) with
$150^2$ cells (2 min 3 s on 4 cores) is much better than the uniform
$150^2$ mesh (30 s) and comparable to the uniform $600^2$ mesh
(28 min 14 s), i.e. at 7.26 % of its CPU time (Table 6.1, Fig. 6.9).

**Two-fluid relativistic plasma.** [Bhoriya, Kumar & Chandrashekar (2023)](/sources/bhoriya-2023.md)
§6.2.2 (arXiv v2) split the same data between ion and electron fluids:
on $[-6,6]^2$ with Neumann boundaries, each species carries half of
$\rho=10^{-2}$, $p=1$ for $r<0.8$ and half of $\rho=10^{-4}$,
$p=5\times10^{-4}$ for $r>1$, with a linear ramp in between;
$B_1=B_0\in\{0.1,1.0\}$, charge-to-mass ratios $\pm10^3$,
$\gamma=4/3$, $200^2$ cells, $t=4$. Their third- and fourth-order
[entropy-stable](/properties/entropy-stability.md) finite-difference
schemes with IMEX time stepping are stable and comparable to Amano
(2016) and Balsara et al. (2016) at both field strengths; the fourth-order
scheme decays less entropy, and its $\nabla\cdot B$ error is less spread
out and, at $B_0=1$, lower in $L^1$ than the third-order one (Figs.
8–13). Divergence is only cleaned hyperbolically and monitored.

**Radiation RMHD.** [López-Miralles, Martí & Perucho (2023)](/sources/lopezmiralles-2023.md)
§4.2.1 (arXiv v1) add grey M1 radiation to a magnetized blast after
Melon Fuksman & Mignone: on $[-6,6]^2$, $360^2$ cells, ambient
$\rho=10^{-4}$, $p=3.49\times10^{-5}$, inside the unit radius
$\rho=10^{-2}$, $p=1.31\times10^{-2}$, $\gamma=4/3$, $B=(0.1,0,0)$, $v=0$,
radiation in thermal equilibrium with zero flux, absorption
coefficient 1 (optically thin, optical depth $2\rho\kappa_{\mathrm a}=0.02$
across the inner disc, $\kappa_{\mathrm a}$ the absorption coefficient,
page-local) or 1000 (thick, 20); $t=4$. In the thin case the maximum Lorentz factor is
about 1.7, as in the cited work, and the radiation stays cylindrically
symmetric; in the thick case an oblate ring forms with maximum Lorentz
factor about 2.72, and the run needs the radiative HLL solver, MinMod
reconstruction and CFL 0.01 to avoid unphysical states, not their new
[polynomial viscosity matrix](/methods/polynomial-viscosity-matrix-solver.md)
solver (Figs. 8–9). A three-dimensional spherical version on $256^3$
is also run (Fig. 10).

## Rotor

[Liu et al. (2021)](/sources/liu-2021.md) §4.3, their "second rotor
problem": on $[0,1]^2$ with $\gamma=5/3$, $v_3=0$,
$B=(2.5/\sqrt{4\pi},\ 0,\ 0)$, $p=0.5$; with $r$ the distance to
$(0.5,0.5)$, $r_0=0.1$, $r_1=0.115$ (page-local), a disk of density 10
rotating rigidly with speed 1 at $r=r_0$,
$(\rho,v_1,v_2)=(10,\ -(y-0.5)/r_0,\ (x-0.5)/r_0)$ for $r<r_0$; ambient
$(1,0,0)$ for $r>r_1$, and a linear taper in between,
$\rho=1+9\varphi$, $v=\varphi\,(-(y-0.5),\ x-0.5)/r$ with
$\varphi=(r_1-r)/(r_1-r_0)$ (page-local); periodic boundaries as printed;
$t=0.295$; $200^2$ cells at second and third order, $600^2$ at second
order.

Liu, Feng & Wang (2023a) §4.5 print the same second-rotor data,
again with periodic boundaries ($200^2$, $t=0.295$, 100 cores): their
one-step HLL-GRP scheme captures the discontinuities crisply, without
spurious oscillations and without distortion of the rotating velocity
field in the central Mach-number plot, and its divergence norm is
slightly lower than those of the forward-Euler and RK2 HLL schemes
(Figs. 12–15).

Liu et al. (2021) report no negative pressure and undistorted Mach-number contours
in the centre, whose distortion earlier work attributes to divergence
errors; the divergence norm stays below $10^{-3}$ (about
$10^{-3.3}$–$10^{-3.6}$ on $200^2$, $10^{-4}$ on $600^2$), with small
overshoots of the third-order scheme in $B_1$ and $B_2$ slices
(Figs. 9–12). Wall times are 333.94 s (second order, $200^2$),
3731.19 s (third order, $200^2$) and 8787.56 s (second order, $600^2$,
16 cores); they read the visual quality of the third-order $200^2$ run
against the second-order $600^2$ one as showing "the superiority of
higher-order methods".

Dematté et al. (2024) §4.1.4 run a rotor with the second-rotor
kinematics (disk of density 10 rotating with $v=(5-10y,\ 10x-5)$, edge speed
$1$ at $r=0.1$, Tóth's taper $(23-200r)/3$ up to $r=0.115$) but $p=1$,
$B=(2.5/\sqrt{4\pi},0,0)$ and their default $\gamma=5/3$, on $[0,1]^2$ with
$800^2$ cells to $t=0.25$; the plasma beta is $8\pi/6.25\approx4.0$
*(compiler check, not in the sources)*, twice that of Liu et al.'s second
rotor. Both of their constrained-transport variants, staggered
(Gardiner–Stone adapted) and unstaggered (vector potential), agree with
published results and keep the $L_2$ norm of the divergence at machine
precision (Figs. 6–8; see
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)).

### First rotor

[Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) §5.3.1
(arXiv v2) run the rotor in the faster, more strongly magnetized form
they attribute to their ref. [34]: on $[0,1]^2$ with free boundaries
and $\gamma=1.4$, $\rho=1+9\varphi$, $p=1$,
$v=\tfrac{2}{r_0}\varphi\,(-(y-0.5),\ x-0.5)$, $B=(5/\sqrt{4\pi},0)$,
with $\varphi=1$ for $r\le r_0$, $1-(r-r_0)/(r_1-r_0)$ for
$r_0<r\le r_1$, $0$ beyond, $r_0=0.1$, $r_1=0.115$; $t=0.15$. The disk
edge thus rotates at speed 2, against 1 in Liu et al.'s second rotor,
and the plasma beta is $2p/|B|^2=8\pi/25\approx1.0$, against
$16\pi/25\approx2.0$ there *(compiler check, not in the sources)*. Their residual-based
[artificial viscosity](/methods/artificial-viscosity.md) ($c_\mu=2$)
gives effectively non-oscillatory profiles at $\mathbb P_4$ on $128^2$
and $\mathbb P_9$ on $64^2$ elements, with discontinuities resolved
over 2–3 solution points and no visible deterioration at the higher
order (Figs. 10–11). They print $r=\sqrt{x^2+y^2}$, while the velocity
field is centred at $(0.5,0.5)$; consistent use requires $r$ to be the
distance to $(0.5,0.5)$.

[Dao & Nazarov (2022)](/sources/dao-2022.md) §5.5 (arXiv v1) print the
same problem up to the taper velocity, citing Balsara & Spicer and calling it the "first rotor"
of Tóth: on $[0,1]^2$ with $\gamma=1.4$, ambient $\rho=1$, $v=0$, $p=1$,
$B=(5/\sqrt{4\pi},0)$; $\rho=10$, $v=\tfrac{u_0}{r_0}(0.5-y,\ x-0.5)$ for
$r<r_0$; $\rho=1+9\varphi$, $v=\varphi\tfrac{u_0}{r}(0.5-y,\ x-0.5)$ in
the taper; $r_0=0.1$, $r_1=0.115$; $t=0.15$. The disk-edge speed $u_0$
is not printed and no boundary conditions are stated; with $u_0=2$ the
disk data are Dzanic et al.'s, while in the taper Dao & Nazarov's speed
$\varphi u_0$ and Dzanic et al.'s $2\varphi r/r_0$ differ by the factor
$r/r_0\le1.15$ *(compiler check, not in the sources)*. Their
continuous-Galerkin $\mathbb P_3$ scheme with residual-based
[artificial viscosity](/methods/artificial-viscosity.md) and projection
divergence cleaning, on $300\times300$ nodes, runs without negative
pressure, with printed ranges $\rho_h\in[0.727,\,8.42]$,
$p_h\in[0.0386,\,1.93]$, Mach number up to 4.82 and magnetic pressure
$\tfrac12\lvert B_h\rvert^2\in[0.0551,\,2.30]$, and captures circular
Mach contours (Fig. 7). The method has no positivity guarantee; they
leave invariant-domain preservation out of scope.

### Relativistic rotor

Ding & Wu (2024) Example 5.6 run a relativistic rotor after its
relativistic extension in the literature they cite, with the
equation of state they label RC,
$h=(12p^2+8p\rho+2\rho^2)/(3p\rho+2\rho^2)$ (their Eq. (89)): on $[-0.5,0.5]^2$ with
outflow boundaries, $\rho=10$, $v=\alpha_{\mathrm r}(-y,x,0)$ for
$r\le0.1$; $\rho=1+9\varphi$, $v=\alpha_{\mathrm r}\varphi\,\tfrac{0.1}{r}(-y,x,0)$
for $0.1<r\le0.115$ with $\varphi=(0.115-r)/0.015$; $\rho=1$, $v=0$
outside; $B=(1,0,0)$, $p=1$ everywhere; $\alpha_{\mathrm r}=9.95$
(page-local), so the disk edge moves at $0.995$ *(compiler check, not in the sources)*; $400^2$ cells, $t=0.4$
(Fig. 8). The bound-preserving central DG scheme runs with zero local
divergence error (Fig. 7b, 7e).

### Rotor in polar coordinates

[Lesur et al. (2023)](/sources/lesur-2023.md) §4.2 (arXiv v1) run the
Balsara–Spicer rotor "as Mignone et al. (2007), with smooth
transitions", without reprinting the data, to validate the curvilinear
implementation of their [IDEFIX](/software/idefix.md) code: once on a
Cartesian $512^2$ grid (Roe solver, RK2, CFL 0.2, constrained transport
with Gardiner–Stone electromotive-force averaging) and once on a polar grid $N_R\times N_\varphi=256\times1024$
with $R\in[0.05,0.5]$ (Fig. 9). See
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md).

## Weak magnetic blast

[Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) §6.1, after
Bohm et al.: ideal GLM-MHD on $[0,3]^3$ with $10^3$ elements of a heavily
warped curvilinear mesh, periodic. Two states are joined smoothly by a
logistic blend across the sphere of radius $0.3$ about
$(1.5,1.5,1.5)$, of width set by $\delta_0=0.1$: inside
$\rho=1.2$, $v=(0.1,0,0.1)$, $p=0.9$, outside $\rho=1$,
$v=(0.2,-0.4,0.2)$, $p=0.3$, with $B=(1,1,1)$ and $\psi_{\mathrm{GLM}}=0$
throughout; $N=4$ and $6$, $t=1$.

The test checks the entropy behaviour of DGSEM blended with subcell
finite volumes on curved meshes. With entropy-conservative fluxes the
relative change of total entropy converges to zero at fourth order in
the time step (their stepper is the fourth-order SSPRK(5,4)), from CFL 0.4 down
to 0.025, until machine precision; with entropy-stable and TVD-ES fluxes
entropy is dissipated (Fig. 5). The entropy-conservative solution
itself is visibly distorted at $t=0.5$, $N=6$ (Fig. 4). See
[entropy stability](/properties/entropy-stability.md) and
[subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md).

## Qualifications

- Liu et al. (2021) give no CFL number or time-step rule for any test; they
  print periodic boundaries for the rotor without comment, and so do
  Liu, Feng & Wang (2023a), who run at CFL 0.8 with the Wu–Shu
  time-step condition.
- Liu, Feng & Wang (2023a) label the blast-wave quantity of their
  Fig. 8 "magnetic pressure $\lvert B\rvert$" with range $[21,34]$, while
  their rotor and 3D figures plot $\lvert B\rvert^2/2$; the initial
  $\lvert B\rvert=100/\sqrt{4\pi}=28.2$ lies in $[21,34]$ and
  $\lvert B\rvert^2/2\approx398$ does not, so the plotted quantity is
  $\lvert B\rvert$ *(compiler check, not in the sources)*.
- Dzanic & Witherden define the magnetic pressure as
  $\tfrac12(\gamma-1)\lvert B\rvert^2$ (§2.1), not the $\tfrac12\lvert B\rvert^2$
  of their own flux (Eq. 2) and plasma beta $2p/\lvert B\rvert^2$.
- The blast-wave comparison with earlier results is visual, against
  figures of other papers; so are the rotor runs of Dao & Nazarov and
  Lesur et al.
- The weak magnetic blast is smooth, and with entropy-conservative
  fluxes the semi-discrete scheme conserves entropy exactly, so the
  fourth-order decay measures the time-integration error, not a spatial
  order *(compiler check, not in the sources)*.

# Citations

- [Liu et al. (2021)](/sources/liu-2021.md) — §4.3–4.4, Figs. 9–13.
- [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) — §6.1, Eq. (95), Table 2, Figs. 4–5 (arXiv v1).
- [Duan & Tang (2022)](/sources/duan-2022.md) — Ex. 6.5, Table 6.1, Fig. 6.9 (arXiv v1).
- [Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) — §5.3.1, Figs. 10–11 (arXiv v2).
- [Dao & Nazarov (2022)](/sources/dao-2022.md) — §5.5, Fig. 7 (arXiv v1).
- [Lesur et al. (2023)](/sources/lesur-2023.md) — §4.2, Fig. 9 (arXiv v1).
- [Chen, Wu & Xiong (2023)](/sources/chen-2023-b.md) — Ex. 5.7, Figs. 5.4–5.5 (arXiv v1).
- [Dzanic & Witherden (2023)](/sources/dzanic-2023.md) — §5.5, Eq. (46), Figs. 10–13 (arXiv v2).
- [Bhoriya, Kumar & Chandrashekar (2023)](/sources/bhoriya-2023.md) — §6.2.2, Figs. 8–13 (arXiv v2).
- [López-Miralles, Martí & Perucho (2023)](/sources/lopezmiralles-2023.md) — §4.2.1, Figs. 8–10 (arXiv v1).
- [Liu, Feng & Wang (2023a)](/sources/liu-2023.md) — §§4.4–4.6, Figs. 8–20.
- [Dematté et al. (2024)](/sources/dematte-2024.md) — §4, §4.1.4, §4.1.6, Figs. 6–8, 10.
- [Ding & Wu (2024)](/sources/ding-2024-b.md) — Examples 5.6, 5.8, Figs. 7–8, 10–11.
- [Berta et al. (2024)](/sources/berta-2024.md) — §5.7, Eq. (55), Table 3, Figs. 11–13 (arXiv v4).
