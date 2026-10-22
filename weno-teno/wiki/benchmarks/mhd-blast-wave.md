---
type: Benchmark
title: "MHD blast wave and rotor"
description: "Two-dimensional ideal-MHD robustness tests: the Balsara–Spicer blast wave at plasma beta about 2.5×10^-4 and the Tóth-type rotor, which probe positivity of pressure and the effect of divergence errors, plus a weak, smooth magnetic blast used in three dimensions to verify entropy conservation and stability of DG schemes."
status: established
aliases: [magnetic blast wave, MHD blast, Balsara–Spicer blast wave, MHD rotor, second rotor problem, weak magnetic blast]
tags: [benchmark, mhd, positivity, entropy-stable]
timestamp: 2026-10-22T00:00:00Z
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
*(compiler check of their value)*.

Their second- and third-order locally divergence-free
[WLS-ENO](/methods/wls-eno.md) finite-volume scheme, with HLL flux,
Godunov–Powell source term and a Zhang–Shu-type
[scaling limiter](/methods/zhang-shu-scaling-limiter.md) on density and
pressure, produces no negative pressure, and its density is
"significantly smoother" than earlier published results (Fig. 13).

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
  figures of other papers.
- The weak magnetic blast is smooth, and with entropy-conservative
  fluxes the semi-discrete scheme conserves entropy exactly, so the
  fourth-order decay measures the time-integration error, not a spatial
  order *(compiler remark, not in the sources)*.

# Citations

- [Liu et al. (2021)](/sources/liu-2021.md) — §4.3–4.4, Figs. 9–13.
- [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) — §6.1, Eq. (95), Table 2, Figs. 4–5 (arXiv v1).
