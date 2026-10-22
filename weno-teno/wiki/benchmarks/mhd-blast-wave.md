---
type: Benchmark
title: "MHD blast wave and rotor"
description: "Two-dimensional ideal-MHD robustness tests: the Balsara–Spicer blast wave at plasma beta about 2.5×10^-4, its relativistic counterpart, and the first and second rotor problems, which probe positivity of pressure and the effect of divergence errors, plus a weak, smooth magnetic blast used in three dimensions to verify entropy conservation and stability of DG schemes."
status: established
aliases: [magnetic blast wave, MHD blast, Balsara–Spicer blast wave, MHD rotor, second rotor problem, weak magnetic blast]
tags: [benchmark, mhd, positivity, entropy-stable]
timestamp: 2026-10-23T10:00:00Z
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

### Relativistic MHD blast

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

They report no negative pressure and undistorted Mach-number contours
in the centre, whose distortion earlier work attributes to divergence
errors; the divergence norm stays below $10^{-3}$ (about
$10^{-3.3}$–$10^{-3.6}$ on $200^2$, $10^{-4}$ on $600^2$), with small
overshoots of the third-order scheme in $B_1$ and $B_2$ slices
(Figs. 9–12). Wall times are 333.94 s (second order, $200^2$),
3731.19 s (third order, $200^2$) and 8787.56 s (second order, $600^2$,
16 cores); they read the visual quality of the third-order $200^2$ run
against the second-order $600^2$ one as showing "the superiority of
higher-order methods".

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

- Liu et al. give no CFL number or time-step rule for any test; they
  print periodic boundaries for the rotor without comment.
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
