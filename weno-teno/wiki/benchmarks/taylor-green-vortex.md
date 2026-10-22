---
type: Benchmark
title: "Taylor–Green vortex"
description: "Periodic vortex flow that transitions to turbulence: inviscid at low Mach number to compare kinetic-energy loss and enstrophy growth of shock-capturing schemes, viscous at Re=1600 or 5000 and Mach up to 1.2 to compare dissipation rates with DNS, in 2D a robustness test of entropy- and kinetic-energy-preserving DG, with a density slab a test of two-phase schemes."
status: established
aliases: [TGV, inviscid Taylor–Green vortex, Taylor–Green vortex at Re 1600, compressible Taylor–Green vortex]
tags: [benchmark, turbulence, low-dissipation, teno, weno]
timestamp: 2026-10-23T10:00:00Z
---

# Taylor–Green vortex

The Taylor–Green vortex is a smooth, triply periodic initial velocity
field on $[0,2\pi]^3$ that stretches its vorticity, breaks down into
small scales and, if the flow is viscous, decays as turbulence. The sources use it as
the smooth-turbulence test of shock-capturing schemes: there is no
shock, and in the inviscid low-Mach runs the loss of
kinetic energy is read as [numerical dissipation](/definitions/numerical-dissipation.md), and the
volume-averaged kinetic energy $\langle\kappa\rangle$ and enstrophy (the
volume average of half the squared vorticity, in words) are the
measures.

## Setups

**Inviscid, low Mach number.** [Li et al. (2022)](/sources/li-2022-b.md)
§4.5, Eqs. (47)–(49) and [Takagi et al. (2022)](/sources/takagi-2022.md)
§4.10 print

$$
\begin{aligned}
\rho&=1,\qquad v_1=\sin x\cos y\cos z,\qquad v_2=-\cos x\sin y\cos z,\qquad v_3=0,\\
p&=100+\tfrac1{16}\big[(\cos2x+\cos2y)(2+\cos2z)-2\big],
\end{aligned}
$$

on periodic $[0,2\pi]^3$. The background pressure $100$ makes the
maximum Mach number about $0.08$ for $\gamma=5/3$
($c=\sqrt{\gamma p/\rho}\approx12.9$ with $\lvert v\rvert\le1$)
*(compiler check, not in the sources)*, so the flow is nearly
incompressible. Li et al. use $\gamma=5/3$ and grids $64^3$, $128^3$ up
to $t=6$; Takagi et al. do not print $\gamma$ and use $64^3$ to $t=10$.
[Li, Chen & Ren (2022)](/sources/li-2022.md) §4.4.1 print the same
data (after Brachet et al. and Shu et al.) and run four linear schemes
without shock capturing (fifth-order upwind UW5, sixth-order central
C6, and the fourth-order [MDCD](/methods/mdcd-scheme.md) and adaptive
MDAD fluxes) on $128^3$ to $t=10$, with local characteristic
Lax–Friedrichs splitting, which they prefer to the global splitting as
less dissipative here; diagnostics are the kinetic energy, the spectrum
at $t=10$ and $Q=3$ iso-surfaces.
Li et al. write the pressure as $100+([\cos(2z)+2][\cos(2x)+\cos(2y)]-2)/16$,
the same expression.

**Viscous, $\mathrm{Re}=1600$.** [Ye et al. (2022)](/sources/ye-2022.md)
§4.9, Eqs. (49)–(52): a cube of side $2\pi L$, reference Mach number
$M=0.1$,

$$
v_1=M\sin\tfrac xL\cos\tfrac yL\cos\tfrac zL,\quad
v_2=-M\cos\tfrac xL\sin\tfrac yL\cos\tfrac zL,\quad v_3=0,\quad
p=\frac1\gamma+\frac{M^2}{16}\Big(\cos\tfrac{2x}L+\cos\tfrac{2y}L\Big)\Big(\cos\tfrac{2z}L+2\Big),
$$

$\mathrm{Re}=1600$, $\mathrm{Pr}=0.71$, $\gamma=1.4$, $256^3$ points,
$t\in[0,20]$; diagnostics are the kinetic energy, the dissipation rate
split into solenoidal and dilatational parts, and $Q$-criterion
iso-surfaces ($Q=2.5$ at $t=10$).

Li, Chen & Ren (2022) §4.4.2 run the same case after Hillewaert, with
unit velocity amplitude, $p=\frac1{\gamma M_0^2}+\frac1{16}(\cos2x+\cos2y)(2+\cos2z)$,
$\rho=\gamma M_0^2p$, $M_0=0.1$, $\mathrm{Pr}=0.71$, against a
pseudo-spectral DNS on $512^3$; comparisons on $256^3$, plus $208^3$
(MDCD) and $168^3$ (MDAD) for equal enstrophy error.

**Viscous, $\mathrm{Re}=1600$, at three Mach numbers.**
[Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) §5.2,
Eqs. (46)–(50), print the same velocity field with unit amplitude and

$$
p=\frac1{\gamma M^2}+\frac1{16}\Big(\cos\tfrac{2x}L+\cos\tfrac{2y}L\Big)\Big(2+\cos\tfrac{2z}L\Big),
$$

constant initial density ($1.292$ kg/m$^3$ as printed),
$\mathrm{Re}=1600$, $\mathrm{Pr}=0.71$, $\gamma=1.4$, and
$M=0.1$, $0.5$, $1$; grids $64^3$ to $1024^3$, third-order Runge–Kutta
at CFL 0.5, up to $t=16$. This is Ye et al.'s field rescaled by the
velocity instead of the sound speed (divide Ye et al.'s velocities by
$M$ and pressure by $M^2$) *(compiler check, not in the sources)*.

**Viscous, $\mathrm{Re}=1600$, element and compact schemes.**
[Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) §5.2.1 (arXiv v3)
and [Edoh (2022)](/sources/edoh-2022.md) §4.2, Eqs. (31)–(32), use Ye
et al.'s field on $[-\pi L,\pi L]^3$ (Dzanic & Witherden with $L=1$,
unit velocity amplitude and $p_0=1/(\gamma M^2)$, i.e. Sciacovelli et
al.'s normalization). Dzanic & Witherden: $M=0.08$,
$\mu=1/1600$, flux reconstruction $\mathbb P_3$ with $96^3$, $128^3$
and $160^3$ DOFs and $\mathbb P_3$–$\mathbb P_5$ at about $120^3$ DOFs,
against the DNS of van Rees et al.; diagnostics the kinetic-energy
dissipation rate (smoothed by a moving average) and the enstrophy-based
rate $\frac{2\mu}{V}\int\tfrac12\rho\lvert\omega\rvert^2$ ($\omega$ the
vorticity, $V=8\pi^3$). Edoh: $M_0=0.1$, $\mathrm{Pr}=0.71$,
$\gamma=1.4$, the sixth-order compact central scheme CD06 for the
convective and pressure terms with second-order viscous terms, RK4,
grids $64^3$, $128^3$ and $192^3$ without filtering, up to $t\approx16t_c$
($t_c$ the convective time); diagnostics kinetic-energy decay rate,
entropy change, density fluctuations, numerical dissipation and
vorticity magnitude at $t\approx9t_c$.

**Viscous, $\mathrm{Re}=5000$, subsonic and supersonic.**
[Sousa & Scalo (2022)](/sources/sousa-2022.md) §§6.1, 7.1 (arXiv v2)
print the same field on $[-\pi L,\pi L]^3$ with $\rho_0=1$,
$p_0=1/\gamma$, $\mathrm{Re}=\rho_0V_0L/\mu_0=5000$ ($V_0$ the velocity
amplitude), at turbulent Mach numbers $M_t=0.1$ and $1.2$: a DNS on
$384^3$, a priori analysis with a sharp filter at $k_c=48$, and LES on
$96^3$ (grid studies $72^3$–$144^3$ at $M_t=0.1$ and $96^3$–$384^3$ at
$M_t=1.2$), with a sixth-order compact scheme; at $M_t=1.2$ shocklets
form near $tV_0/L\approx6.5$–$6.75$.

**Two-dimensional, inviscid.** [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md)
§4.2.2 and App. A.3 (arXiv v4) run the planar field $\rho=1$,
$v=(\sin x\cos y,\ -\cos x\sin y)$,
$p=\frac{100}\gamma+\frac14(\cos2x+\cos2y)$, $\gamma=1.4$, on
periodic $[0,2\pi]^2$, to $t=30$: nodal DG on Gauss–Lobatto nodes,
$N=5$ on $16^2$ elements, SSPRK(10,4) with
$\Delta t=\frac{\Delta x}{10}\frac1{N^2+1}$, and a sixth-order SBP finite
difference scheme on $100^2$ nodes with $\Delta t=\Delta x/8$. It is a
long-time robustness test of the semi-discrete entropy and
kinetic-energy budgets, not a turbulence test.

**Two-phase, inviscid.** [Jain & Moin (2022)](/sources/jain-2022.md)
§4.1 (arXiv v1) put a slab of width $2L$ of fluid 1 across the middle
of the periodic box $[0,2\pi]^3$, with volume fraction
$\phi_1=1-\frac12\big[1+\tanh\big((\lvert x-\pi\rvert-L)/(2\epsilon_{\mathrm i})\big)\big]$
($\epsilon_{\mathrm i}=\Delta x$ the interface thickness, page-local),
density $\rho=\rho_{1o}\phi_1+\rho_{2o}(1-\phi_1)$, $L=1$,
$v_1=M_o\sin x\cos y\cos z$, $v_2=-M_o\cos x\sin y\cos z$, $v_3=0$ and
$p=\frac1\gamma+\frac{\rho M_o^2}{16}(\cos2x+\cos2y)(\cos2z+2)$
(Eq. (66), $M_o$ the initial Mach number, page-local), $\gamma_1=\gamma_2=1.4$,
no viscosity or surface tension, $64^3$, RK4 at CFL about 0.65, to
$M_ot=40$ (and $100$). With $\rho_{1o}=\rho_{2o}=1$ it is the
single-phase vortex with a passive slab ("pseudo-two-phase", §4.1.1);
with $\rho_{2o}/\rho_{1o}=10$ and $1000$ and $M_o=0.05$, $0.2$ (and
$0.4$) it is a [five-equation-model](/definitions/five-equation-model.md)
two-phase flow (§4.1.2).

**Viscous, after Brachet et al.** [Bryngelson et al. (2021)](/sources/bryngelson-2021.md)
§5.4 run the Taylor–Green vortex of Brachet et al. with the
finite-volume WENO5 scheme of [MFC](/software/mfc.md), with parameters
deferred to an earlier MFC paper (Reynolds number, Mach number and grid
are not printed), and compare the kinetic-energy dissipation rate over
$t\in[0,10]$ with Brachet et al.'s spectral solution.

**Reviewed results.** [Fu (2023)](/sources/fu-2023.md) reproduces an
inviscid TGV at $t=10$ (iso-surface $Q=3$, resolution not printed;
WENO-CU6, TENO6, TENO8, TENO8-opt, Fig. 4) and an incompressible viscous
TGV dissipation rate on $64^3$ against DNS on $256^3$ (TENO8-A against
the ALDM and dynamic Smagorinsky models, Fig. 14).

## Findings across sources

**Kinetic-energy loss ranks the schemes; WENO-JS loses most.** Li et
al. find that WENO-JS dissipates the most kinetic energy of the WENO
variants, that at $128^3$ it still dissipates more than the
seventh-order linear upwind scheme at $64^3$, yet its enstrophy grows
faster than that upwind run; [WENO-ZN](/methods/weno-zn.md) has the
least dissipation of the three WENO schemes (Fig. 11). Takagi et al.
find that [TENO-THINC](/methods/teno-thinc.md) preserves kinetic energy
better and gives larger enstrophy growth than WENO5-Z and TENO5 on
$64^3$ (Fig. 21). Fu (2023) shows TENO6 and TENO8 less dissipative than
WENO-CU6.

**TENO beats WENO on the viscous dissipation rate.** Ye et al. find
the kinetic energy nearly scheme-independent at $256^3$, but the
dissipation rate discriminates: all TENO-type schemes beat the
WENO-type ones, the WENO-type schemes underestimate the peak (more so
with a dissipative flux), [AFTENO5](/methods/afteno.md) with HLLC is
best, and HLLC beats Steger–Warming splitting in both alternative-flux
schemes (Figs. 10–12). Fu (2023) reports that
[TENO8-A](/methods/adaptive-teno.md) on $64^3$ beats the dynamic
Smagorinsky model and ALDM for the dissipation rate (§4.2).

The sources agree that WENO-JS-type weights are the most dissipative
of the schemes compared, and no source reports a newer scheme
dissipating more than its WENO-JS baseline.

**Adaptive dissipation in a linear scheme.** In the inviscid run of
Li, Chen & Ren, the non-dissipative C6 and the nearly non-dissipative
MDCD with dissipation parameter 0.001 blow up at $t=4$–$5$; UW5 and
MDCD with 0.012 run but dissipate more; MDAD runs without tuning,
best preserves the kinetic energy and follows a $-5/3$ spectrum slope
at $t=10$ (Figs. 27–28). At $\mathrm{Re}=1600$, C6 diverges and MDAD
matches the DNS kinetic energy before $t=9$ and the peak dissipation
rate, better than a WENO-CU6 variant (Fig. 29). On $256^3$ the enstrophy
at $t=9$ is $9.866$ (MDAD), $9.214$ (MDCD) and $8.581$ (UW5) against
$10.284$ for the DNS, errors of $4.1\%$, $10.4\%$ and $16.6\%$, at a CPU
cost of MDAD 19.3% above UW5 (97268 s against 81525 s) (Table 4); the
printed percentages and the cost ratio 1.193 reproduce from the printed
values *(compiler check, not in the sources)*. At matched enstrophy
error MDAD needs $168^3$ points against $208^3$ for MDCD and $256^3$
for UW5, i.e. 1.90 and 3.54 times as many points in total *(compiler
check, not in the sources)*, and the paper reports efficiency ratios
3.7 and 1.8 (Table 5, Fig. 30(b)).

**Kinetic-energy-preserving split forms and two-phase interfaces.**
Jain & Moin find that, for the single-phase (pseudo-two-phase) vortex,
three internal-energy flux forms (their quadratic-split QS, the cubic
split of Kennedy–Gruber and Kuya et al., and Chandrashekar's form)
all conserve kinetic energy, approximately conserve entropy and are
stable at $M_o=0.05$ and $0.2$, so the
[kinetic-energy-preserving](/properties/kinetic-energy-preservation.md)
scheme is not unique (Figs. 2–3). With density ratio 10 only QS is
stable: the two cubic forms violate the interface-equilibrium
condition, produce "spurious mixing of internal energy at the interface"
and diverge (Figs. 4–5). QS stays stable at density ratio 1000 for
$M_o=0.05$, $0.2$, $0.4$ up to $M_ot=100$, the departure of the kinetic
energy from its initial value at larger $M_o$ being reversible pressure
work (Fig. 7). A divergence-form mass flux, or flux forms inconsistent
with their conditions, make the two-phase run diverge (App. C, D). The
evidence is stability and conservation, not agreement with a reference;
the flow has no shocks and $M\le0.4$.

**Shock-capturing devices must stay off.** Dzanic & Witherden find
their [entropy filter](/methods/entropy-filtering.md) predominantly
inactive: all their runs agree with the DNS and are nearly identical to
unfiltered runs (Fig. 7). Sousa & Scalo's
[quasi-spectral viscosity](/methods/quasi-spectral-viscosity.md),
tuned partly on a priori spectra of this flow, stays inactive early, as
do the dynamic Smagorinsky model and the model labelled CvP, but
not plain Smagorinsky; at $M_t=0.1$ on $96^3$ it is closer to the filtered DNS than
the other models from $tV_0/L\approx6$ on, slightly over-damps before,
is the only one to recover the post-peak plateau of the dissipation
rate, and improves monotonically from $72^3$ to $144^3$; without a model
the run diverges near $tV_0/L\approx10$ (§6.1, Figs. 12–14). Its cost on
$96^3$ is $78.5\,\%$ above the model-free run, against $34.3\,\%$ for
Smagorinsky and $72.5\,\%$ for the dynamic model (Table 2, hardware not
stated).

**Supersonic turbulence needs the right energy norm.** At $M_t=1.2$
Sousa & Scalo find the volume-averaged kinetic energy non-monotonic,
with a negative apparent dissipation, while Myers' compressible energy
norm decays monotonically, so they measure dissipation with the latter.
Without shock capturing every turbulence model blows up on $96^3$;
their quasi-spectral viscosity runs stably. With localized artificial
diffusion added, all the other runs over-dissipate around
$tV_0/L\approx6.5$, where the shocks are strongest, and underpredict the
dissipation peak, while the quasi-spectral viscosity stays closest to
its own $384^3$ reference (§7.1, Figs. 16–19).

**Split forms in under-resolved runs.** Edoh finds the divergence
form of the convective terms unstable on his coarse grids (stable only
on $512^3$, footnote 5), while the kinetic-energy-preserving
Kennedy–Gruber splitting and his compressible rotational form are
robust even severely under-resolved; at $64^3$ the rotational form shows
larger density fluctuations and numerical dissipation, attributed to
aliasing, yet cleaner vortical structures, and the two agree as the grid
is refined (Figs. 3–4). In two dimensions, Abgrall, Öffner & Ranocha
find that central DG blows up at $t\approx3.8$; their
[entropy correction terms](/methods/entropy-correction-term.md) remove
the kinetic-energy growth or keep the entropy constant but only delay
the blow-up (to $t\approx4.3$ when both are applied), whereas
[flux-differencing](/methods/flux-differencing.md) DG with
entropy-conservative or kinetic-energy-preserving fluxes stays stable
until $t\approx35$, and the Ducros split form with both corrections
runs to $t=30$ (§4.2.2, Figs. 7–8).
The corrected schemes fail through negative nodal density or pressure,
after which neither the entropy variables nor the correction exist. In
the SBP finite-difference runs, central and corrected schemes blow up
between $t\approx23.5$ and $25.5$, flux differencing with Pirozzoli's or
Ranocha's flux survives $[0,30]$ and crashes around $t\approx35$
(App. A.3, Fig. 11). See
[split convective forms](/methods/split-convective-forms.md) and
[kinetic energy preservation](/properties/kinetic-energy-preservation.md).

**Agreement with spectral DNS.** Bryngelson et al. find that MFC's
dissipation rate "closely match[es]" Brachet et al.'s spectral solution,
with vortex stretching growing until $t\approx5$ before viscous
dissipation dominates (Fig. 5b). Sciacovelli et al. find that at
$M=0.1$ their ninth-order central scheme with adaptive
[artificial dissipation](/methods/artificial-viscosity.md) superposes on
spectral results, with the low-order shock-capturing term correctly
switched off, no energy pile-up at small scales even on $64^3$, and grid
convergence at $512^3$; convergence is faster at larger initial Mach
number (Fig. 9).

**The order of the dissipation, not of the convective flux, decides
the result.** Sciacovelli et al. compare at $M=1$ on $256^3$ the order
of the high-order dissipation term and of the convective and viscous
fluxes. Third-order dissipation on $256^3$ gives results similar to
ninth-order dissipation on $64^3$; ninth-order dissipation is nearly
grid-converged and higher orders add little; and third-order
dissipation combined with convective fluxes up to tenth order gives
nearly identical results, so "the dissipation order is the fundamental
ingredient" (Fig. 11). Viscous fluxes above fourth order have
negligible influence, whereas second-order viscous fluxes give excessive
viscous dissipation on $256^3$ (Fig. 12). They read the scheme's
ninth-order dissipation as an implicit subgrid model that converges to
DNS under refinement, and attribute the stronger damping of the
small-scale spectrum at low Mach number to the larger number of
acoustically limited time steps needed to reach $t=16$, i.e. more
applications of the dissipation operator (§5.2). This framing in terms
of the [numerical dissipation](/definitions/numerical-dissipation.md)
order complements Ye et al.'s finding that, at fixed spatial order, the
choice of weights and flux (TENO against WENO, HLLC against
Steger–Warming) separates the dissipation rates.

## Qualifications

- Takagi et al. head §4.10 "incompressible" Taylor–Green vortex, but
  solve the compressible Euler equations with the background pressure
  $100$; the flow is low-Mach, not incompressible.
- Li et al.'s Fig. 10 caption says the contours are "given by velocity
  from 0 to 1", while the panels are labelled with vorticity-magnitude
  levels $\Omega=1.5$ and $3.0$.
- Bryngelson et al. defer every parameter of their run to an earlier
  paper, so their agreement with Brachet et al. cannot be placed among
  the setups above.
- Sciacovelli et al.'s scheme is a central scheme with artificial
  dissipation, not a WENO or TENO scheme; their conclusion on
  dissipation order is drawn within that family.
- Edoh gives the time step as $\Delta t=t_c/10^4$ and as $\Delta t=10^{-3}$
  with $\nu_{V_0}\approx0.01$ on $64^3$ (§4.2.1). With
  $\Delta x=2\pi L/64=0.098L$, $\nu_{V_0}=0.01$ requires
  $\Delta t\approx10^{-3}t_c$, so $t_c/10^4$ is the inconsistent value
  *(compiler check, not in the sources)*.
- Dzanic & Witherden print the pressure perturbation as
  $\tfrac1{16}(\cos2x+\cos2y)(\cos(2z+2))$; the velocity field is even
  in $z$, so the pressure it induces must be, and the form of the other
  sources, $(\cos2z+2)$, is meant *(compiler check, not in the
  sources)*. They define the kinetic-energy dissipation rate as
  $\mathrm dK/\mathrm dt$ but plot it positive for a decaying flow, so a
  minus sign is missing.
- Abgrall, Öffner & Ranocha's Fig. 7 caption is truncated ("with a
  Taylor-Green").
- Li, Chen & Ren's §4.4.2 refers to "Fig. 3(b)" for the enstrophy
  history at matched error; Fig. 30(b) is meant (Fig. 3 is a linear
  dissipation plot).
- Jain & Moin call the cubic- and quadratic-split forms "QS and CS ...
  cubic-split and quadratic-split forms, respectively" in §3.5, the
  reverse of their own definitions (QS is quadratic split), and write
  "QC" for QS in §4.1.2 and §4.2.
- In the inviscid runs there is no converged reference: the sources
  compare schemes with each other (Li et al. also with a linear upwind
  scheme), not with an exact energy history.

# Citations

- [Li et al. (2022)](/sources/li-2022-b.md) — §4.5, Eqs. (47)–(49), Figs. 10–11.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §4.10, Fig. 21.
- [Ye et al. (2022)](/sources/ye-2022.md) — §4.9, Eqs. (49)–(52), Figs. 10–12.
- [Fu (2023)](/sources/fu-2023.md) — Figs. 4 and 14; §4.2 (reproduced).
- [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) — §5.2, Eqs. (46)–(50), Figs. 9–12 (arXiv v1).
- [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) — §5.4, Fig. 5b (arXiv v1).
- [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) — §5.2.1, Eq. (31), Fig. 7 (arXiv v3).
- [Edoh (2022)](/sources/edoh-2022.md) — §4.2, Eqs. (31)–(32), Figs. 3–4.
- [Sousa & Scalo (2022)](/sources/sousa-2022.md) — §6.1, Eqs. (62)–(66), Figs. 12–14, Table 2; §7.1, Figs. 16–19 (arXiv v2).
- [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) — §4.2.2, Figs. 7–8; App. A.3, Fig. 11 (arXiv v4).
- [Li, Chen & Ren (2022)](/sources/li-2022.md) — §4.4.1–4.4.2, Figs. 27–30, Tables 4–5.
- [Jain & Moin (2022)](/sources/jain-2022.md) — §4.1, Eq. (66), Figs. 2–7; App. C–D (arXiv v1).
