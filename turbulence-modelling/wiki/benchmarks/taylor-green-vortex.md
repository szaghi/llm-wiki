---
type: Benchmark
title: "Taylor–Green vortex"
description: "The triply periodic vortex flow that transitions from a single-mode analytic field to decaying turbulence: at Re 40,000 to separate Smagorinsky and implicit LES errors; at Re 100 to 10,000 to split numerical dissipation and test subgrid models, filters and split forms; supersonic for shock capturing; inviscid for energy conservation; laminar and 2D for filter and commutator analysis."
status: established
aliases: [TGV, Taylor-Green vortex, 2D Taylor–Green vortex, inviscid Taylor–Green vortex, supersonic Taylor–Green vortex, laminar Taylor–Green vortex, Brachet Taylor–Green vortex]
tags: [benchmark, les, implicit-les, sgs-model, dns, numerical-dissipation, compressible, filtering, kinetic-energy-preserving]
timestamp: 2026-10-27T06:13:00Z
---

# Taylor–Green vortex

The Taylor–Green vortex (TGV) starts from a single-mode, divergence-free
velocity field in a periodic box. In three dimensions the initial vortices
stretch, break down into turbulence and then decay, so a single run sweeps a
laminar phase, a transition with a peak of dissipation, and decaying
turbulence. Because the initial condition is analytic and the box periodic,
every reference and LES run of the same $Re$ starts from the same state and
filtered DNS can be compared with LES at the same time instant. In two
dimensions the vortex is an exact decaying solution of the Navier–Stokes
equations and serves as an analytic test of filtering and discretization
operators.

## Three-dimensional TGV as an LES benchmark

**Set-up.** [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md),
§6.1, Eq. (43), use the cube $[0,2\pi]^3$ with
$$u=\sin x\cos y\cos z,\qquad v=-\cos x\sin y\cos z,\qquad w=0,$$
incompressible flow and $Re=1/\nu=40{,}000$. The Taylor-scale Reynolds
number after breakdown is about 400 ($Re_\lambda\approx493$ at $t=10$,
$\approx389$ at $t=15$). The reference DNS has $5400^3$ nodes, run on the
impermeable sub-box $[0,\pi]^3$ using the flow's symmetries (eight times
fewer degrees of freedom), over $0\le t\le20$. Diagnostics are the volume
averages
$$K=\frac{1}{(2\pi)^3}\int\tfrac12u_iu_i\,d^3x,\qquad \varepsilon=\frac{1}{(2\pi)^3}\int\nu\,\partial_ju_i\,\partial_ju_i\,d^3x,\qquad \frac{dK}{dt}=-\varepsilon,$$
(Eqs. 44–46), with LES total dissipation $-d\bar K/dt$, and shell-averaged
spectra $E(k)$, the spectral eddy viscosity and the effective filter
transfer function $\sqrt{E_{\mathrm{LES}}/E_{\mathrm{DNS}}}$ (§6.3).

**LES meshes** (cubic cells, cutoff $k_c=\pi/h$ with $h$ the cell size):

| Mesh | Nodes | $k_c$ | DNS cutoff over $k_c$ | Cost reduction against DNS |
|---|---|---|---|---|
| VHR | $1080^3$ | 540 | 5 | not stated |
| HR | $540^3$ | 270 | 10 | $10^4$ |
| LR | $216^3$ | 108 | 25 | $25^4$ |

The solver is the sixth-order compact finite-difference code Incompact3d
with skew-symmetric (kinetic-energy-conserving) convection and third-order
time stepping (§3).

**What it shows.** The case separates the error of an explicit model from
the error of the discretization it runs on:

- *Truncated Euler and no model.* Without viscosity the kinetic-energy-conserving
  scheme keeps $K$ within 1% over $0\le t\le20$ and evolves to a thermalized
  spectrum $E(k)\sim k^2$. A no-model LES on the LR mesh thermalizes over more than
  80% of the wavenumbers, piles energy near $k_c$ from $t=5$ and overestimates the total
  dissipation during breakdown (§6.2, Figs. 4–7). The same $k^2$
  equipartition appears for no-model runs of
  [homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md).
- *Smagorinsky.* With $C_s=0.1$ and the filter width equal to the cell size,
  the [Smagorinsky model](/methods/smagorinsky-model.md) cannot control the
  pile-up and over-dissipates. At fixed $\Delta=\pi/108$, numerical
  convergence through breakdown is reached only with $h=\Delta/5$
  ($k_c=540$), equivalent to $C_s=0.5$ in the cell-based form (§6.3, Figs.
  7–12).
- *Implicit spectral vanishing viscosity.* The
  [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
  form of [implicit LES](/definitions/implicit-les.md) prevents
  thermalization and captures the dissipation peak. The authors report LR
  and HR runs at fixed $\Delta$ as "virtually identical" (not shown). The
  model misses the low-wavenumber plateau of the a priori spectral eddy
  viscosity, which carries up to 24%, 16% and 6% of the total dissipation at
  LR, HR and VHR (§6.4, Figs. 13–18).

The numerical viscosity ratios that §5.3 derives for the HR and LR
cutoff ratios are $\nu_0/\nu=181$ and 700; §6 does not restate the values
used. Details of these results live on the model pages linked above and on
[spectral eddy viscosity](/methods/spectral-eddy-viscosity.md) and
[numerical dissipation](/properties/numerical-dissipation.md).

## Three-dimensional TGV at $Re=1600$ and inviscid

**Set-up.** The sources at this Reynolds number use the same initial velocity as above,
$u=\sin x\cos y\cos z$, $v=-\cos x\sin y\cos z$, $w=0$ on $[0,2\pi]^3$
(scaled by a length $L=1$ and velocity $V_0=1$), with $Re=V_0L/\nu=1600$ or
no viscosity. The compressible solvers add the pressure field
$p=p_0+\tfrac{1}{16}\rho_0V_0^2(\cos2x+\cos2y)(\cos2z+2)$ at low Mach number:
[Cao et al. (2022)](/sources/cao-2022.md), §3.1, at Mach 0.1 with
$\gamma=1.4$, $Pr=0.71$, $0\le t\le20$; [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md),
§6.1, Eq. (124), with $p_0=100$ and no viscosity (their Eq. 124 prints the
pressure product expanded; the two forms agree *(compiler check, not in the
sources)*). [Prakash et al. (2022)](/sources/prakash-2022.md),
§III.B.2, solve the incompressible equations and analyse only the transition
to the fully turbulent state.

| Source | Solver | Resolution | Reference |
|---|---|---|---|
| [Cao et al. (2022)](/sources/cao-2022.md) | finite-volume [high-order gas-kinetic scheme](/methods/high-order-gas-kinetic-scheme.md), no model | $128^3$, $256^3$, $512^3$, $1024^3$ cells | 13-point dispersion-relation-preserving finite differences at $512^3$ (DeBonis) |
| [Prakash et al. (2022)](/sources/prakash-2022.md) | stabilized trilinear finite elements, explicit SGS models | $64^3$, $128^3$ elements | DNS and filtered DNS of Shoraka; spectra of Brachet et al. |
| [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md) | DGSEM, $N=8$, kinetic-energy-preserving split form, low-dissipation Roe flux, SVV-filtered Smagorinsky viscosity | $8^3$ elements ($72^3$ nodes, *compiler check, not in the sources*) | viscous $Re=1600$ result of van Rees et al. at $768^3$ |
| [Kou et al. (2023)](/sources/kou-2023.md) | DG ([HORSES3D](/software/horses3d.md)), $N=3$, Roe and symmetric interior penalty, solution or gradient [jump penalty](/methods/jump-penalty-stabilization.md); Smagorinsky and Vreman for comparison | $32^3$ elements | DNS dissipation rate (cited to a review) |
| [Saini et al. (2023)](/sources/saini-2023.md) | second-order finite volume (OpenFOAM) with [WALE](/methods/wale-model.md); $N=4$ continuous Galerkin ([Nektar++](/software/nektar-plus-plus.md)) with spectral vanishing viscosity | $64^3$, $128^3$ cells; $8^3$, $16^3$ elements | $512^3$ spectral DNS of van Rees et al. |
| [Zhao et al. (2023a)](/sources/zhao-2023.md) | [high-order gas-kinetic scheme](/methods/high-order-gas-kinetic-scheme.md), 5th- and 7th-order non-compact and 5th-order compact reconstruction, no model | $256^3$ cells | DNS (source of the curve not stated) |
| [Wang et al. (2023b)](/sources/wang-2023-b.md) | the same gas-kinetic scheme with 5th-order WENO, on GPUs; also Mach 0.25 to 1.0 | $64^3$ to $512^3$ cells | the authors' earlier CPU runs |
| [Duan & Wang (2024)](/sources/duan-2024.md) | [flux reconstruction](/methods/flux-reconstruction.md) (hpMusic), $N=4$, Mach 0.1; Smagorinsky, WALE and Vreman with three filter widths, against no model | inviscid: $16^3$ elements; $Re=1600$: $64^3$ elements | $Re=1600$: DNS of van Rees et al. |
| [Wang (2024)](/sources/wang-2024-b.md) | flux reconstruction recovering nodal DG (ATHOS), $N=3$, HLLC flux, local modal filter; $Re=1600$ and 5000 | $64^3$ elements | DNS of Gassner & Beck and of Carton de Wiart et al. ($Re=1600$), Incompact3d DNS of Dairay et al. ($Re=5000$) |
| [Kurz et al. (2025)](/sources/kurz-2025.md) | split-form DGSEM, $N=7$, on GPUs ([GALÆXI](/software/galaexi.md)) and CPUs ([FLEXI](/software/flexi.md)), no model; Mach 0.1, constant initial temperature | $64^3$ to $512^3$ degrees of freedom | DeBonis |
| [Wang et al. (2024)](/sources/wang-2024.md) | finite differences, second-order kinetic-energy-preserving split form KGP2 against sixth-order optimized upwind OPT6, MUSCL3 and WENO5; inviscid with flow reversal | $30^3$ cells | the initial field (time reversal) |
| [Brillon & Nadarajah (2026)](/sources/brillon-2026.md) | nonlinearly stable (entropy-stable split-form) [flux reconstruction](/methods/flux-reconstruction.md), Ismail–Roe two-point flux, no upwinding, no over-integration; Mach 0.1; implicit LES and five eddy-viscosity models | DNS: $N=7$ on $32^3$ and $N=3$ on $64^3$ elements ($256^3$ degrees of freedom); LES: $96^3$ ($N=5$), $64^3$ ($N=7$), $48^3$, $24^3$ ($N=5$) | Dairay et al. ($512^3$ compact FD), DeBonis, Chapelier et al., Carton de Wiart et al., van Rees et al. |
| [Caban et al. (2026)](/sources/caban-2026.md) | incompressible half-staggered compact differences (SAILOR) of order 2, 6 and 10, with spectral or compact interpolation and optional explicit regularization filter; implicit LES, Smagorinsky, Vreman, Layton–Lewandowski, approximate deconvolution; also $Re=400$ | DNS $256^3$ and $384^3$; LES $64^3$ | Brachet et al., van Rees et al., $512^3$ pseudo-spectral DNS of the first high-order CFD workshop; LES of Hickel et al. |
| [Volpiani (2024)](/sources/volpiani-2024.md) | finite differences in the Python solver BASIC, $M=0.085$, $p_0=100$: divergence form with relaxation filtering (standard and optimized 11-point schemes and filters) against three [kinetic-energy-preserving](/properties/kinetic-energy-preservation.md) split forms (Feiereisen, Ducros, Kennedy–Gruber) without filter; Smagorinsky, two multi-scale Smagorinsky variants and dynamic Smagorinsky; also inviscid and $Re=2500$–10,000 | inviscid $64^3$; $Re=1600$: $64^3$ to $512^3$; $Re\ge2500$: $128^3$ | inviscid: Brachet et al. and the codes compared by Johnsen et al.; viscous: DNS of Dairay et al. |
| [Liang & Fu (2024)](/sources/liang-2024.md) | hybrid finite differences TENO-S (non-dissipative split central flux, eight-point TENO at flagged cells); WENO-CU6, TENO6, TENO8 for comparison; inviscid to $t=100$ and viscous $Re=100$ to 10,000 | inviscid $64^3$; viscous $64^3$ ($Re\le3000$) and $128^3$ ($Re=5000$, 10,000) | DNS of Brachet et al. ($256^3$) and Dairay et al. ($1280^3$, $2048^3$) |
| [Takagi et al. (2022)](/sources/takagi-2022.md) | finite differences TENO-THINC against WENO5-Z and TENO5; inviscid, $p_0=100$, to $t=10$ | $64^3$ | none named in the text |

**Numerical dissipation of a no-model DNS scheme.**
[Cao et al. (2022)](/sources/cao-2022.md), §3.1, Figs. 2–5, measure the
kinetic-energy decay rate $-dK/dt$ against the dissipation computed from the
resolved field, split into the deviatoric-strain, bulk-viscosity and
pressure–dilatation parts; the remainder is their numerical dissipation. The
kinetic energy agrees with the reference except on $128^3$; the peak
dissipation differs markedly on $128^3$ and $256^3$ and agrees with
refinement. The bulk and pressure–dilatation parts are negligible at Mach
0.1, and the numerical dissipation decreases with refinement. The authors
read the agreement of $-dK/dt$ as evidence that the coarse-mesh numerical
dissipation "correctly mimics" the unresolved dissipation and so supports
[implicit LES](/definitions/implicit-les.md) with high-order methods (see
[numerical dissipation](/properties/numerical-dissipation.md)). Their run
costs (Table 3) grow from 213 core hours at $128^3$ to 747,062 at $1024^3$,
about 1.4 times the core hours of the finite-difference reference at equal
grids, 1.2 after correcting for processor speed (§3.2); the comparison is
across machines and time steps. They call the $1024^3$ run "the finest
resolution" for the problem (§3.1).

**Explicit subgrid models during transition.**
[Prakash et al. (2022)](/sources/prakash-2022.md), §III.B.2, Figs. 5–7:
every model matches the filtered-DNS resolved kinetic energy on $128^3$, and
every model except the dynamic mixed model on $64^3$, which decays too fast.
In resolved dissipation, dynamic Smagorinsky under-predicts, the dynamic
mixed model under-predicts more (significantly even on $128^3$), the
unclipped [gradient model](/methods/gradient-model.md) over-predicts
(especially on $64^3$), and the gradient model with standard or optimal
clipping is the most accurate. At $t=9$ dynamic Smagorinsky and the dynamic
mixed model under-predict the high-wavenumber energy; the gradient-model
variants are closest to filtered DNS, optimal clipping slightly better than
standard clipping on $64^3$. The authors conclude that clipping may be more
accurate than the dynamic mixed model in laminar–turbulent transition
(§IV).

**Interface jump penalties as the implicit model.**
[Kou et al. (2023)](/sources/kou-2023.md), §4.2, Figs. 10–12, run the
compressible TGV at $Re=1600$ and Mach 0.1 with $N=3$ DG on $32^3$
elements, penalizing the momentum equations only. The unpenalized scheme
diverges, which the authors relate to aliasing. With a solution-jump
penalty the dissipation rate shows a spurious second peak at $t\approx11$
besides the reference peak at $t\approx9$ until the penalty exceeds 1.9, after
which the first peak is too high; with a gradient-jump penalty the second
peak disappears above $6.3\times10^{-4}$, and the largest value tested
recovers the peak magnitude but oscillates later. At $t=8$ the solution
penalty hardly changes the spectrum, while large gradient penalties make
the energy decay faster. Both penalties are called "clearly superior" to
the Smagorinsky and Vreman models adapted to DG, which give a lower
dissipation peak, more dissipation before $t=8$ and significant dissipation
at mid wavenumbers; the model constants are not printed. See
[jump-penalty stabilization](/methods/jump-penalty-stabilization.md).

**Splitting the dissipation into viscous, model and numerical parts.**
[Saini et al. (2023)](/sources/saini-2023.md) integrate the resolved
kinetic-energy budget over the box (and subdomains) and take its residual as
the numerical dissipation rate, adding the SGS terms of WALE and the terms of
spectral vanishing viscosity, including one from the spatial variation of
its amplitude (§2.2, Eq. 8). They validate the procedure on the TGV at
$Re=3000$ with 64 solution points per direction: the fluxes vanish over the
whole box, the decay rate and viscous dissipation match their direct
evaluation, and an interior box agrees with the no-model results of
Castiglioni & Domaradzki for $t<3$ (§4, Figs. 5–6). At $Re=1600$ the
numerical part dominates what is removed beyond molecular viscosity: on the
$64^3$ finite-volume grid a peak of model-plus-numerical dissipation near
$t=5$ is about 75% numerical and moves the dissipation peak earlier, and its
ratio to the viscous dissipation approaches 4; on $16^3$ elements at $N=4$
that ratio is at most 1.2 and the peak about a quarter of the $64^3$
finite-volume one, 90–95% numerical (§5.1, Figs. 7–8). As recalled from
the authors' earlier paper, the $16^3$, $N=4$ run costs 1.3 times the
$64^3$ finite-volume run and is about ten times more accurate in the $L_2$
sense (§3.1, Fig. 1). The authors conclude that the gain of the high-order
solver comes mainly from lower
[numerical dissipation](/properties/numerical-dissipation.md), not from the
model.

**Reconstruction order of a gas-kinetic scheme.**
[Zhao et al. (2023a)](/sources/zhao-2023.md) (read in arXiv v1), §5.1, Figs.
3–7, run the TGV at $Re=1600$, Mach 0.1, $Pr=1$ on $256^3$ cells as
[implicit LES](/definitions/implicit-les.md) with their
[high-order gas-kinetic scheme](/methods/high-order-gas-kinetic-scheme.md).
Seventh-order reconstruction (in the face-normal direction, or also
tangentially) and fifth-order compact reconstruction improve the kinetic
energy, dissipation-rate and enstrophy histories over the fifth-order
non-compact scheme, the fully seventh-order variant being best late in the
decay, and lower the numerical dissipation computed, as in Cao et al.
above, as the residual of the compressible dissipation budget; the authors
conclude that the fifth-order non-compact scheme "is still
over-dissipative". The seventh-order runs use 4 Gauss points per face,
with which their own accuracy test drops to about fourth order under
refinement (16 points restore seventh order at about twice the cost, §4,
Tables 3–4).

**GPU timing and compressibility.** [Wang et al. (2023b)](/sources/wang-2023-b.md)
(read in arXiv v1), §4.1, use the TGV at $Re=1600$, Mach 0.1, $Pr=1$ over
20 time units to time the gas-kinetic scheme on GPUs (Table 3): against an
8-core desktop CPU the speedup is about 7 on one TITAN RTX and 16 on one
Tesla V100 at $64^3$ to $256^3$; one V100 takes 11.7 h at $256^3$, and 8
V100s take 22.3 h at $512^3$ against 66 h on 1024 CPU cores of TianHe-II
(Tables 4–5, CPU data from Cao et al. above). At $256^3$ and Mach 0.25,
0.5, 0.75 and 1.0 the dissipation peak is delayed and flattened as the Mach
number grows, the kinetic energy is non-monotone for Mach 0.75 and 1.0 (as
the authors say Peng & Yang report), and the late dissipation ($t\ge11$)
is markedly higher than at low Mach number (Fig. 8).

**Inviscid TGV and the shape of a spectral vanishing viscosity.**
[Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md), §6.1, Fig. 4, add
a [Smagorinsky](/methods/smagorinsky-model.md) viscosity ($C_s=0.2$, filter
width the cube root of the element volume over $(N+1)^3$) filtered modally
by the kernel $(i/N)^{P}$ of an entropy-stable
[spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md),
with $P$ the page-local kernel exponent. This is an explicit modal SVV
acting on an added viscous flux, a different construction from the
implicit SVV of Vicente Cruz & Lamballais above. Unfiltered ($P=0$) the model is
excessively dissipative; $P\approx0.1$ is best, with a spectrum close to
$k^{-5/3}$ over most resolved wavenumbers at $t=20$. The filtered viscosity
acts mainly at low and medium wavenumbers and prevents high-wavenumber
pile-up. For the first five time units the scheme dissipates less than the
viscous reference, then reaches a comparable level. Two sources thus agree
that a plain Smagorinsky viscosity over-dissipates the TGV (this source and
[Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) above),
and [Prakash et al. (2022)](/sources/prakash-2022.md) find the converse
failure, a pile-up at the cutoff, for a model with too little dissipation,
the unclipped gradient model, in forced
[homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md).

**Subgrid models and filter widths in flux reconstruction.**
[Duan & Wang (2024)](/sources/duan-2024.md), §5.1, Figs. 5–7, add the
[Smagorinsky](/methods/smagorinsky-model.md), [WALE](/methods/wale-model.md)
and [Vreman](/methods/vreman-model.md) models to $N=4$ flux reconstruction,
with the eddy viscosity constant in each element and the interface fluxes of
the SGS stress set to zero, and three filter widths built on the cube root
$h$ of the element volume: $h$, $h/\sqrt{N+1}$ and $h/(N+1)$. On the
inviscid TGV ($16^3$ elements) every model with every width dissipates the
eddies heavily compared with the no-model run, and the SGS dissipation is
much larger than the Riemann-solver dissipation of the scheme; the two
smaller widths dissipate clearly less than $h$, and the ranking is WALE
least, then Vreman, then Smagorinsky. At $Re=1600$ ($64^3$ elements) the
no-model enstrophy lies almost on the DNS of van Rees et al.; the models
degrade it significantly with the widths $h$ and $h/\sqrt{N+1}$ and much
less with $h/(N+1)$ (§5.1). The Smagorinsky over-dissipation agrees with
[Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) and
[Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md) above. On this
well-resolved case the authors find implicit LES best; the width
$h/\sqrt{N+1}$ that they recommend comes from decaying grid turbulence and
wall-modelled channel flow (see
[homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
and [turbulent channel flow](/benchmarks/turbulent-channel-flow.md)).

**A localized modal filter that stays off in smooth flow.**
[Wang (2024)](/sources/wang-2024-b.md) (read in arXiv v2), §4.1, Figs.
2–3, uses the TGV at $Re=1600$ and 5000 ($64^3$ elements, $N=3$, HLLC
flux) to check that the author's local modal filter, an exponential modal filter
applied only in elements whose Persson–Peraire smoothness indicator exceeds
a threshold (here $-4$), adds no dissipation: the dissipation-rate history
to $t=20$ and the spectra at $t=9$ ($Re=1600$) and $t=14$ ($Re=5000$) are
indistinguishable from the unfiltered run, and both agree "excellently"
with the DNS; the filter costs about 5.5% more per step. The case shows
the filter inactive in smooth flow; its dissipation where it acts is
tested on the [turbine cascades](/benchmarks/turbine-cascade.md); see
[subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md)
and [discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md).

**Time reversal of the inviscid TGV.** [Wang et al. (2024)](/sources/wang-2024.md),
§3.1, Fig. 2, run the inviscid TGV on $30^3$ cells to $t=20$, reverse the
velocity and advance to $t=40$, after Modesti & Pirozzoli. With the
second-order kinetic-energy-preserving split form KGP2 the kinetic energy
stays constant and the vorticity field at $t=40$ is identical to the
initial one, "verifying" its "non-dissipative energy conservation"; OPT6,
MUSCL3 and WENO5 lose kinetic energy monotonically and do not recover the
initial field, MUSCL3 the most. See
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md).
The same conservation by a kinetic-energy-conserving scheme appears in the
truncated-Euler run of
[Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) above
($K$ within 1% to $t=20$).

**A GPU port reproduces its CPU parent.** [Kurz et al. (2025)](/sources/kurz-2025.md)
(read in arXiv v2), §5.2, run the $Re=1600$ case at $M_0=0.1$ on $8^3$ to
$64^3$ elements at $N=7$: the GPU code and the CPU code give the same
solenoidal dissipation rate "up to machine precision", which converges to
the DeBonis reference with resolution and matches it "almost perfectly" at
$512^3$ degrees of freedom (Fig. 11).

**An entropy-stable flux reconstruction with and without models.**
[Brillon & Nadarajah (2026)](/sources/brillon-2026.md) (read in arXiv
v1, 2024), §3.1, run the compressible TGV at $Re=1600$, Mach 0.1, to
$t=20$, with nonlinearly stable flux reconstruction on Gauss–Lobatto
solution nodes and Gauss (uncollocated) flux nodes, no upwind dissipation
and no over-integration.

- *DNS* ($256^3$ degrees of freedom): kinetic energy, dissipation rate,
  enstrophy, spectra and vorticity contours agree with the references. The
  pressure-dilatation dissipation obtained as the residual of the
  kinetic-energy budget agrees with the literature, while computed
  pointwise it oscillates spuriously; the oscillations are smaller on
  collocated (Gauss–Lobatto) flux nodes and are damped by Roe dissipation
  at the faces (§3.1.1, Figs. 2–4). The authors' measure of
  effective viscosity (decay rate over enstrophy, normalized by the
  physical viscosity) stays within 4.5% of 1 for all DNS schemes (Fig. 4b).
- *Spectra.* Before the FFT the high-order field is resampled on $2(N+1)$
  equidistant points per element and direction; without this an apparent
  pile-up appears near the cutoff, and the kinetic energy integrated from
  the spectrum at $t=9$ misses the volume average by up to 5.0% instead of
  0.5% (Table 4, $64^3$ at $N=7$; §3.1.1–3.1.2, Figs. 6, 9).
- *Implicit LES.* The scheme is stable on all under-resolved grids without
  added dissipation; at $96^3$ the dissipation rate follows the DNS to its
  peak at $t\approx8$ (§3.1.2, Fig. 8). Classical strong-form DG without
  over-integration diverges near $t=6$ (§3.1.3, Fig. 11); with
  over-integration it is stable and costs about twice as much as the split
  form for $N=5$ to 12 (Fig. 12).
- *Choices that do not matter* at $96^3$: the two-point flux (Ismail–Roe,
  Kennedy–Gruber, Chandrashekar, Chandrashekar–Ranocha; see
  [kinetic-energy preservation](/properties/kinetic-energy-preservation.md)
  and [entropy conservation](/properties/entropy-conservation.md)), and the
  FR correction parameter, whose largest stable value raises the CFL limit
  from 0.26 to 0.36, against 0.14 for over-integrated strong DG (Table 5,
  Figs. 14–16).
- *Added dissipation.* Roe and low-dissipation Roe face dissipation lower
  the enstrophy peak; added Lax–Friedrichs dissipation gives a higher
  enstrophy peak than the projected DNS, which the authors call
  "anti-dissipative" (§3.1.7, Fig. 17).
- *Subgrid models.* Smagorinsky ($C_s=0.10$), shear-improved and
  high-pass-filtered Smagorinsky and dynamic Smagorinsky, all with a
  low-Reynolds-number correction, slightly raise the dissipation rate,
  lower the enstrophy peak and remove energy at wavenumbers 25 to 40,
  where the no-model run already lacks energy; they are "not recommended"
  for this flow with this scheme (§3.1.8, Fig. 19).

**Discretization-induced filters, regularization and deconvolution.**
[Caban et al. (2026)](/sources/caban-2026.md), §5.2–5.4, run the
incompressible TGV of Brachet et al. at $Re=1600$ (dissipation peak near
$t=9$, run to $t=20$) on a half-staggered compact-difference code in
which the derivative scheme and the interpolation between velocity and
pressure nodes can be switched. They distinguish three variants: spectral
(non-dissipative) interpolation, dissipative compact interpolation, and
spectral interpolation plus an explicit regularization filter (an
eighth-order compact filter combined with its approximate inverse truncated
at $N_{\mathrm{AD}}=2$) applied every step. They measure accuracy by the time-integrated
relative error of the resolved kinetic energy against DNS up to $t=20$
(Eq. 45). On $64^3$:

- with spectral interpolation and no model the LES diverges near $t=3.5$,
  at the same time as the no-model run of Hickel et al.; Smagorinsky
  ($C_s=0.1$) and Vreman with $\Delta=2h$ diverge near $t=4$, and with
  $\Delta=4h$ they are stable but inaccurate (§5.3.1, Fig. 18);
- dissipative interpolation or the regularization filter alone make the
  runs stable; used without a model they are an
  [implicit LES](/definitions/implicit-les.md) whose error,
  $2.23\times10^{-2}$, is about half that of the best eddy-viscosity run
  (Vreman with regularization, $4.33\times10^{-2}$; Smagorinsky
  $4.76\times10^{-2}$), and they "surpass" the adaptive local deconvolution
  of Hickel et al.; fourth-order instead of tenth-order interpolation
  raises the implicit-LES error to $2.84\times10^{-1}$ (Table 4, Figs.
  19–23);
- the Layton–Lewandowski model (the zeroth term of approximate
  deconvolution, a [scale-similarity model](/methods/scale-similarity-model.md))
  is stable for every filter even with spectral interpolation and gives the
  lowest error, $2.03\times10^{-2}$ with a sixth-order compact filter and
  regularization, 10% below the best implicit LES (Table 5);
- approximate deconvolution with five terms needs added dissipation
  (dissipative interpolation or regularization) to remain stable; its best
  error, $2.31\times10^{-2}$, is about twice as accurate as the
  eddy-viscosity models but not better than Layton–Lewandowski or implicit
  LES; building the discretization-induced filters into the deconvolution
  helps only when the LES filter is of low order (§5.4.2, Tables 6–9; see
  [discretization-consistent closure](/definitions/discretization-consistent-closure.md)).

Most of the error accumulates during transition, $t\approx5$ to 12
(Fig. 23b). The authors' DNS on $384^3$ almost overlaps the $512^3$
pseudo-spectral reference; the $256^3$ run with spectral interpolation
becomes unstable near $t=10$ (§5.2, Figs. 16–17). Their interpolation
results hold for staggered and half-staggered algorithms only; collocated
kinetic-energy-conserving schemes lack that dissipation (§6).

**Relaxation filtering against split forms.** [Volpiani (2024)](/sources/volpiani-2024.md)
compares two ways of stabilizing central differences on the compressible
TGV at $M=0.085$: relaxation filtering, an explicit high-order low-pass
filter of the conservative variables at every step (see
[explicit modal filtering](/methods/explicit-modal-filtering.md) for the
related modal filters), and split forms of the convective terms.

- *Inviscid, $64^3$* (§4, Table 1, Figs. 4–5). Normalized kinetic energy
  at $t=5$ is 0.999 for the Feiereisen and Ducros forms and 0.998 for
  Kennedy–Gruber at every stencil size, against 0.983 to 0.176 for
  relaxation filtering from 11- down to 3-point stencils; the author's
  optimized 11-point scheme and filter retain 0.986, the most of any
  filtered scheme. Normalized enstrophy at $t=3.5$ reaches 3.34 with the
  largest split-form stencils and 3.26 with the optimized filtered scheme,
  against 3.46 in the semi-analytical result of Brachet et al. and 3.13–3.34
  in the codes compared by Johnsen et al. Split forms keep the enstrophy
  monotonic; filtering makes it fall after some time. Spectra at $t=5$
  agree with a $256^3$ run up to wavenumber 17; beyond it the split forms
  pile energy at the highest wavenumbers, which the author ties to aliasing
  from two thirds of the maximum wavenumber on. Per 100 iterations the
  11-point filtered scheme costs 78.9 s and the Kennedy–Gruber form 298.9 s.
- *$Re=1600$, $64^3$ to $512^3$* (§5, Figs. 6–18). Filtered implicit LES
  predicts the dissipation computed from the kinetic-energy decay well on
  all grids while under-predicting the enstrophy-based rate on coarse ones,
  which the author reads as the filter carrying the unresolved
  dissipation; the optimized filter best predicts the dissipation peak.
  Split forms without a model are noisy on $64^3$ and $128^3$ and pile
  aliased energy at high wavenumbers that contaminates even low ones;
  Smagorinsky on a split form is too dissipative, misses transition and
  under-predicts the dissipation peak, independently of the split form;
  the multi-scale variants improve it, the dynamic model does not improve
  on them, and adding the relaxation filter to the split form with a model
  improves the results: aliasing errors, if not removed, affect the
  solution even with an eddy viscosity (Figs. 15–17).
  "Regardless of the model, the best result is achieved for the implicit
  LES with RF with the optimized filter and no SGS model." Combining a split
  form with the filter lets its strength drop from 0.1 to 0.01 (unstable in
  divergence form) and removes the pile-up on $64^3$.
- *$Re=2500$, 5000 and 10,000 on $128^3$* (§5, Fig. 10). The optimized
  filtered implicit LES agrees well with the DNS of Dairay et al. on
  $768^3$, $1280^3$ and $2048^3$, including the dissipation peak, with the
  largest discrepancy at the highest Reynolds number.

**Hybrid TENO schemes and inviscid energy conservation.** On the inviscid
TGV at $64^3$, [Liang & Fu (2024)](/sources/liang-2024.md), §4.10,
Figs. 17–18, run their TENO-S scheme, which uses a non-dissipative split
central flux wherever an eight-point indicator finds the flow smooth, to
$t=100$: it preserves the total kinetic energy and captures the enstrophy
growth, while WENO-CU6, TENO6 and TENO8 dissipate the energy and smear the
small vortices after $t\approx5$. [Takagi et al. (2022)](/sources/takagi-2022.md),
§4.10, Fig. 21, find their TENO-THINC scheme better than WENO5-Z and TENO5
at preserving kinetic energy and capturing enstrophy growth up to $t=10$
(see [shock sensor](/definitions/shock-sensor.md) and
[WENO schemes](/methods/weno-scheme.md)).
On the viscous TGV Liang & Fu report that TENO-S at $64^3$
($Re=100$–3000) and $128^3$ ($Re=5000$, 10,000) agrees well with the DNS
of Brachet et al. and Dairay et al. in the energy dissipation rate and
"performs significantly better" than the other schemes (§4.11,
Figs. 19–20). [Volpiani (2024)](/sources/volpiani-2024.md) (above) also
compares a no-model $128^3$ run with the Dairay et al. DNS up to
$Re=10{,}000$.

**Eddy-viscosity models in high-order TGV runs.** Several sources agree
that adding an eddy-viscosity model to a high-order or low-dissipation
TGV run at $Re=1600$ degrades it: Smagorinsky, WALE and Vreman on $N=4$
flux reconstruction, least with the filter width $h/(N+1)$
([Duan & Wang (2024)](/sources/duan-2024.md)); Smagorinsky and Vreman
against jump penalties on DG ([Kou et al. (2023)](/sources/kou-2023.md));
five Smagorinsky variants on entropy-stable flux reconstruction
([Brillon & Nadarajah (2026)](/sources/brillon-2026.md)); Smagorinsky and
Vreman against implicit LES on compact differences
([Caban et al. (2026)](/sources/caban-2026.md)); Smagorinsky, multi-scale
and dynamic Smagorinsky against filtered implicit LES on central
differences ([Volpiani (2024)](/sources/volpiani-2024.md)). In the last two the
eddy-viscosity runs are also compared with alternatives that win: the
no-model scheme in Brillon & Nadarajah, implicit LES and the
Layton–Lewandowski model in Caban et al.

**Inviscid TGV for subgrid models on continuous spectral elements.**
[Reddy et al. (2026)](/sources/reddy-2026.md) (read in a 2021 preprint),
§7, run the TGV with $u_0=100$ m/s, $\rho=1.178$ kg/m³ and unit wavenumber
in a $2\pi$ box on $32^3$ elements at $N=4$ of the
[continuous-Galerkin spectral-element method](/methods/spectral-element-method.md)
of the atmospheric model NUMA, solving the compressible Euler equations
with an eddy-viscosity closure and no molecular viscosity. They compare
the [Smagorinsky](/methods/smagorinsky-model.md) and
[Vreman](/methods/vreman-model.md) models with element-wise and nodal
variants of a [residual-based dynamic model](/methods/residual-based-dynamic-sgs-model.md):

- the element-wise residual-based variants are the most dissipative on all
  four integral quantities (kinetic energy, its decay rate, enstrophy,
  effective viscosity); the nodal residual-based variant conserves kinetic
  energy best before $t^*\approx12$ but has dissipated more by
  $t^*\approx24$ (Fig. 7a);
- all models peak in dissipation rate at $t^*\approx8$, which the authors
  call in "good agreement" with the peak near $t^*\approx9$ of the DNS of
  Brachet et al.; all show an inflection near $t^*\approx5$, read as
  vortex-tube breakdown (Fig. 7b);
- the nodal variants give the largest enstrophy; all spectra peak at
  $k\approx3$ and follow $k^{-5/3}$ below $k=32$ (Figs. 7c, 8).

The authors call the TGV "homogeneous, isotropic turbulence". Their
equations carry no molecular viscosity, and the comparison with the DNS of
Brachet et al. that they print is the time of the dissipation peak (§7.2).

**Self-tuning modal filtering at $Re=200$ and 800.**
[Ranjbar et al. (2026)](/sources/ranjbar-2026.md) (read in arXiv v1,
2025), §III.B, test an
[explicit modal filter](/methods/explicit-modal-filtering.md) for
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md) in
[HORSES3D](/software/horses3d.md) on the compressible TGV at $Re=200$ and
800 (split form with Chandrashekar averaging, low-dissipation Roe flux;
the Mach number is not stated). DNS: $18^3$ elements at $N=7$ ($Re=200$)
and $20^3$ at $N=12$ ($Re=800$), reproducing the dissipation rate of Fehn
et al.; coarse runs: $11^3$ elements at $N=4$ and $7^3$ at $N=10$.

- The unmodelled coarse runs over-predict the dissipation rate after $t=4$
  and under-predict it after $t=7$ ($Re=200$) or $t=9$ ($Re=800$).
- A filter that removes a fixed number of the highest mode groups brackets
  the DNS with two neighbouring settings, and needs more removed groups at
  the higher degree.
- Smagorinsky ($C_s=0.1$) over-predicts the
  dissipation for $t<6$ and under-predicts it after $t=7$ at $Re=200$, and
  deviates from $t=2$ at $Re=800$, while the flow is still mostly laminar;
  the authors call it "not a suitable option" (Figs. 13–14).
- The self-tuning filter, whose cut-off follows the local ratio of grid
  spacing to Kolmogorov length and the strain and rotation invariants, is
  closest to the DNS with one constant ($c=0.25$) at both degrees,
  slightly under-predicting near $t=8$–12; it costs 1.31% more wall time at
  $N=10$ (§III.B, §III.D.3).
- Joint distributions on the coarse runs tie energy accumulation in the
  highest mode groups to large strain and rotation invariants, which
  motivates the cut-off (Figs. 8–10).

**Laminar TGV as a dissipation test of the discretization.**
[Caban et al. (2026)](/sources/caban-2026.md), §5.1, also use the
analytic laminar TGV with seven vortices per period ($Re=1600$, run to
$t=3.772$, when the energy has halved) on $16^3$ to $128^3$ grids. They
define an effective Reynolds number from the energy decay assuming the
analytic decay law (Eq. 42). With spectral interpolation it stays close to
$Re$, so the filters induced by the derivative schemes alone do not lower
it; dissipative interpolation and the regularization filter lower it, the
fourth-order compact interpolation to "several times lower" than $Re$
(Figs. 9–11). The authors read the first result as showing that the
filtering induced by central derivative schemes is non-dissipative.

**Recalled uses.** As recalled by [Basile et al. (2023)](/sources/basile-2023.md),
§3.2 and §4.2.1, Chapelier et al. fixed a modal-decay smoothness threshold
close to the $-5/3$ slope a priori from TGV DNS at $Re=5000$, and the
authors' earlier TGV tests showed high-order DG more accurate than low
order at equal degrees of freedom. As recalled by
[Pereira et al. (2021)](/sources/pereira-2021.md), the companion study of
[partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md)
on the transitional TGV found that the coherent structures driving
transition must be resolved, which fixes the minimum physical resolution.

## Supersonic TGV at $M_0=1.25$

**Set-up.** [Chapelier et al. (2024)](/sources/chapelier-2024.md) (read in
the HAL accepted manuscript), §II.B, take the case of Lusher & Sandham:
the periodic cube $[-\pi L,\pi L]^3$ with the 3D velocity field above
scaled by $U_0$ and $L$, the same pressure field, a uniform initial
temperature $T_0$ (so the initial density follows the pressure),
$Re=1600$, $M_0=U_0/\sqrt{\gamma p_0/\rho_0}=1.25$, $\gamma=1.4$,
$Pr=0.71$ and Sutherland's law, run to $t=20$ (Eqs. 6–8). It combines
transition, decaying turbulence, strong shocks and shock–turbulence
interaction from an analytic initial condition that any solver can
reproduce; the authors present it as the first multi-code comparison on
this case (§I). Diagnostics are the volume-averaged kinetic energy, the
solenoidal dissipation (from the enstrophy, weighted by $\mu(T)$) and the
dilatational dissipation (from $(\partial_ku_k)^2$), plus the Mach-number
profile along $y$ at $x=z=0$ at $t=2.5$, the first dilatational peak
(Eqs. 9–11).

**Reference and its convergence.** A sixth-order TENO finite-difference
run (OpenSBLI) at $64^3$ to $2048^3$ points converges in kinetic energy
from $128^3$ and in solenoidal dissipation at about $512^3$; the first
dilatational-dissipation peak, set by the shocks, is not converged even at
$2048^3$, because the shocks keep sharpening until molecular viscosity
resolves them (§II.C, Figs. 2–4). The $2048^3$ run took 57,600 A64FX cores
for 34 h, 1.96 million core hours.

**Seven solvers without a subgrid model** at $64^3$ to $512^3$ degrees of
freedom (Table I), the coarse runs taken as
[implicit LES](/definitions/implicit-les.md):

| Code | Discretization | Order | Shock capturing |
|---|---|---|---|
| CODA | modal DG | 4 | localized artificial diffusivity |
| SPADE | central kinetic-energy- and entropy-preserving FD with upwind/WENO switching by a Ducros sensor | 8 | local upwinding |
| OpenSBLI | TENO finite differences | 6 | built into TENO |
| NS3D | compact central FD | 6 | high-order filter only |
| SD3DvisP | spectral difference | 4 | localized artificial diffusivity |
| [FLEXI](/software/flexi.md) | DGSEM | 4 | [subcell finite volumes](/methods/subcell-finite-volume-shock-capturing.md) (second-order TVD) |
| H3AMR | [flux reconstruction](/methods/flux-reconstruction.md) | 2 | model-based "block spectral stresses" |

- *Kinetic energy.* All solvers capture it from $128^3$. At $64^3$ the
  Riemann-flux codes (CODA, SD3D, OpenSBLI) underestimate it early, the
  dissipation-free central codes (SPADE, NS3D) follow it to $t\approx12$ and
  then exceed it, which the authors attribute to energy pile-up near the
  cutoff without a subgrid closure, and the second-order H3AMR is too
  dissipative (§IV.A, Fig. 5).
- *Dilatational dissipation* ranks the strength of shock capturing: NS3D
  highest and oscillating, then FLEXI with oscillations on coarse grids;
  OpenSBLI oscillation-free at all resolutions; SPADE, SD3D and H3AMR
  lowest (Fig. 6).
- *Solenoidal dissipation.* CODA, FLEXI and NS3D give the highest levels on
  all grids; most of the turbulent dynamics is captured by all solvers from
  $256^3$, and the discontinuous element schemes resolve small scales well
  on coarse grids; high order beats second order (Fig. 7, §V).
- *Shocks.* Artificial diffusivity gives thick, smooth shocks on coarse
  grids; local switching to low order gives sharp but oscillating ones,
  except TENO, sharp and oscillation-free; the filter-only scheme oscillates
  most (§IV.B, Fig. 8, §V). See
  [artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md),
  [WENO and hybrid schemes](/methods/weno-scheme.md) and
  [numerical dissipation](/properties/numerical-dissipation.md).

A subsonic verification at $Re=500$, $M_0=0.5$ shows all codes agreeing on
kinetic energy and solenoidal dissipation to $t=10$ (App. A).

**A second use of the case.** [Kurz et al. (2025)](/sources/kurz-2025.md),
§5.2, run it with constant initial temperature, Sutherland's law and the
subcell finite-volume blending at the same maximum blending factor on all
grids, at $N=7$ and $64^3$ to $512^3$ degrees of freedom: the GPU and CPU
codes give identical solenoidal dissipation, which converges to the
Chapelier et al. reference and is "almost identical" at $512^3$ (Fig. 11).
For shock–boundary-layer configurations see
[shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md).

## TGV as a parallel-performance test

[Ferrer et al. (2023)](/sources/ferrer-2023.md), §3.8, Fig. 5, use the TGV
on a $64^3$ mesh as the strong-scaling test of the DG spectral-element code
[HORSES3D](/software/horses3d.md) at polynomial degrees $N=3$ to 6: hybrid
MPI+OpenMP parallelization reaches "86% of the ideal performance for 600
cores" at $N=6$, and pure MPI scales worse. The abstract states "good
scalability for up to 1000 processors". The paper states neither the
Reynolds number nor whether $64^3$ counts elements or degrees of freedom,
and reports no flow statistics for this run; it cites the TGV as a case
widely used to report subgrid and implicit-LES capabilities.

[Kurz et al. (2025)](/sources/kurz-2025.md), §4.4, use the incompressible
TGV set-up at $N=7$ on $32$ to $256^3$ elements (16,384 to
$8.6\times10^9$ degrees of freedom, 100 time steps) as the scaling test of
the GPU code [GALÆXI](/software/galaexi.md) on 1 to 1024 A100 GPUs: weak
and strong scaling are almost perfect while each GPU holds more than about
$10^6$ degrees of freedom, below which kernel-launch overhead and then
communication dominate; prioritized CUDA streams give up to 92% more
speed-up at low load (Figs. 6–8).

## Two-dimensional analytic TGV as a commutator test

[Agdestein & Sanderse (2025)](/sources/agdestein-2025.md), App. F, use the
2D TGV on $[0,2\pi]^2$ (Eq. F.1),
$$u=-\sin x\cos y\,e^{-2\nu t},\qquad v=\cos x\sin y\,e^{-2\nu t},\qquad p=\tfrac14(\cos2x+\cos2y)\,e^{-4\nu t},$$
not as a simulation but to compute the convective subfilter force in closed
form. Under a continuous top-hat filter of width $\Delta$, the
$x$-component of the force is
$$c_x=-\tfrac12\big(\mathrm{sinc}^4(\Delta/2)-\mathrm{sinc}(\Delta)\big)\sin2x=-\frac{\Delta^4}{480}\sin2x+O(\Delta^6)$$
(Eqs. F.9, F.12). The discrete commutator of the staggered second-order
scheme with a discrete top-hat filter has the same $\sin2x$ dependence but a
different coefficient (Eqs. F.29–F.30). The authors conclude that a closure
trained on discretize-first data is inconsistent with a filter-first LES
equation (see
[discretization-consistent closure](/definitions/discretization-consistent-closure.md)
and [divergence-consistent LES](/methods/divergence-consistent-les.md)).

The 3D initial condition of Vicente Cruz & Lamballais and the 2D solution of
Agdestein & Sanderse differ by an overall sign of the velocity *(compiler check, not in the
sources)*.

## Qualifications

- The sources measure two kinds of dissipation: the decay rate $-dK/dt$ of
  the volume-averaged kinetic energy, which includes model and numerical
  dissipation ([Cao et al. (2022)](/sources/cao-2022.md);
  [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md); the
  dissipation-rate curves of [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md)),
  and the viscous dissipation of the resolved field computed from its
  gradients or enstrophy ([Cao et al. (2022)](/sources/cao-2022.md);
  [Prakash et al. (2022)](/sources/prakash-2022.md), Eq. 27). Only the
  first includes what a model or a scheme removes, so the two are not
  interchangeable when comparing runs.
- [Cao et al. (2022)](/sources/cao-2022.md), §3.1, state both that the peak
  of $-dK/dt$ shows "a large discrepancy" on $128^3$ and $256^3$ and that it
  is "well predicted at all grid levels"; their implicit-LES conclusion
  rests on the second statement. Read in the arXiv v1 preprint.
- [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md) compare an
  inviscid run with a viscous $Re=1600$ reference, so the dissipation
  agreement is qualitative; they print the time as "seconds" and the
  Smagorinsky viscosity (Eq. 125) without a density factor, although it is
  used as a dynamic viscosity. Read in arXiv v3.
- [Ferrer et al. (2023)](/sources/ferrer-2023.md) were read in arXiv v1;
  their scaling figure is not read here, only the stated values.
- [Kou et al. (2023)](/sources/kou-2023.md) recommend, from their
  one-dimensional eigensolution analysis with upwind flux, a negative
  gradient penalty ($-1\times10^{-3}$ at $N=3$, Table 1), but remove the
  spurious TGV peak with positive values above $6.3\times10^{-4}$; the paper
  does not comment on the change of sign. Their scaling of the penalty with
  $Re$ cancels in the face integral as printed (§2.2, Eq. 23) *(compiler
  check, not in the sources)*, although §4.2 explains the larger TGV
  values by that scaling.
- [Saini et al. (2023)](/sources/saini-2023.md) give the share of the
  numerical part of the TGV as 85–95% for the high-order runs in their
  summary and 80–90% (SVV share 10–20%) for the $8^3$ run in the same
  section (§5.1).
- [Zhao et al. (2023a)](/sources/zhao-2023.md) print the internal degrees
  of freedom as $N=(5-3\gamma)(\gamma-1)$ (§2), which gives 0.32 at
  $\gamma=1.4$, while §5.1 uses $N=2$, the value of $(5-3\gamma)/(\gamma-1)$
  *(compiler check, not in the sources)*.
- [Wang et al. (2023b)](/sources/wang-2023-b.md) print the $256^3$ speedups
  as 7.4 and 15.4, while their printed times give 7.5 and 15.6 *(compiler
  check, not in the sources)*.
- [Prakash et al. (2022)](/sources/prakash-2022.md) run no no-model case
  on the TGV and stop the analysis at the end of transition, so their
  ranking does not cover the decay phase.
- [Duan & Wang (2024)](/sources/duan-2024.md) find the SGS dissipation
  much larger than the scheme's in $N=4$ flux reconstruction, while
  [Saini et al. (2023)](/sources/saini-2023.md) find the numerical part
  dominant in second-order finite volumes and $N=4$ continuous Galerkin.
  The set-ups differ: explicit Smagorinsky, WALE and Vreman models on
  $16^3$ (inviscid) and $64^3$ flux-reconstruction elements against WALE
  on $64^3$ and $128^3$ finite-volume cells and spectral vanishing
  viscosity on $8^3$ and $16^3$ continuous-Galerkin elements. Each verdict
  is stated for its own models, schemes and grids (Duan & Wang §5.1; Saini
  et al. §5), so it is recorded as a difference of set-up, not a conflict
  of claims. Duan & Wang do not state the model coefficients
  used.
- [Wang (2024)](/sources/wang-2024-b.md) sets $V_0=0.1\sqrt{p/\rho}$ and
  calls the case Mach 0.1; with the sound speed $\sqrt{\gamma p/\rho}$ that
  is Mach $0.1/\sqrt{1.4}\approx0.085$ *(compiler check, not in the
  sources)*. The initial field (Eq. 23) is printed without the amplitude
  $V_0$.
- [Wang et al. (2024)](/sources/wang-2024.md) do not state the Mach number
  of their inviscid run; the comparison involves schemes of different order
  (second and sixth) as well as different dissipation.

- [Chapelier et al. (2024)](/sources/chapelier-2024.md) print the
  equation of state as $p=(\gamma-1)(\rho E-\tfrac12\boldsymbol u\cdot\boldsymbol u)$,
  missing $\rho$ in the kinetic term, and $Re=\rho_0U_0/\mu_0$ without
  the length $L$ *(compiler check, not in the sources)*. The legend of
  their Fig. 8 names the Mach-profile reference "TENO6 512" while the text
  gives the $2048^3$ run as reference. They describe the SD3D artificial
  diffusion as a bulk viscosity on momentum and a diffusivity on energy
  only (§III.B.e) and as a Laplacian on all conservative variables
  (§III.B.h). Their summary states that shock capturing has "a low
  impact" on the representation of turbulent scales (§V), while the same
  section says that finite differences with local switching and TENO
  "yield more small-scale dissipation", and §IV.A that the SD3D shock
  capturing is "probably hindering" small scales on the finer grids.
- [Kurz et al. (2025)](/sources/kurz-2025.md) cite the Chapelier et al.
  reference as submitted; their Fig. 11 caption marks both references
  "(left)"; their scaling mesh, "doubled in each direction" from
  $4\times4\times2$, cannot reach $256^3$ *(compiler check, not in the
  sources)*.
- [Brillon & Nadarajah (2026)](/sources/brillon-2026.md) print the
  spectral cutoff of the $N=7$, $32^3$-element DNS as 122 (Table 2), while
  their own Eq. (103) gives $32\times7/2=112$, the value of the other rows'
  rule; they print the grid cutoff of the $4^3$-element run as 4 where
  Eq. (104) gives 2 *(compiler check, not in the sources)*. They clip the
  dynamic coefficient to $[0,C_s^2]$ in §2.6.4 and "at $C_{max}=0.1$" in
  §3.1.8. They use "iLES" for implicitly filtered LES with an explicit
  model and "ILES" for implicit LES without one.
- [Caban et al. (2026)](/sources/caban-2026.md) call the filter induced by
  first-derivative central schemes "non-dissipative" in §1 and §3.2.1 and
  "dissipative … without inducing numerical diffusion" in the abstract and
  §6. They point to "Table 7" for the implicit-LES and eddy-viscosity
  errors, which are in Table 4. Their conclusions are for $Re=1600$ on
  $64^3$ only.
- [Ranjbar et al. (2026)](/sources/ranjbar-2026.md) use a different
  filter constant per flow (0.65 for decaying isotropic turbulence, 0.25
  for the TGV, 0.5 for the channel) and give the optimal range as
  $[0.2,0.7]$ (§III.D.2); the Smagorinsky constant of the TGV runs is
  printed only in the legends of Figs. 13–14.
- [Reddy et al. (2026)](/sources/reddy-2026.md) title the paper on the
  Navier–Stokes equations but solve the Euler equations (§2); they state
  that the Brachet DNS Reynolds number is "similar" to theirs without
  defining a viscosity for their runs, and they describe the most
  dissipative variants inconsistently within §7.2.

- [Volpiani (2024)](/sources/volpiani-2024.md) prints "$1288$" for the
  $128^3$ grid (p. 910) and refers to Eq. (25), the compressible
  dissipation, for the enstrophy-based rate given by Eq. (24) (p. 906), so
  which of the two Fig. 6 plots is ambiguous. The Smagorinsky constant of
  the runs and the dynamic model's test filter are not printed. The
  filtered runs are no-model implicit LES that the author also describes
  as "explicitly filtered with a well-defined filter function" (§5,
  p. 908); see [implicit LES](/definitions/implicit-les.md).
- [Liang & Fu (2024)](/sources/liang-2024.md) do not print the Mach
  number or the Reynolds-number definition of their viscous runs, and
  [Takagi et al. (2022)](/sources/takagi-2022.md) name no reference curve
  for their inviscid run.

# Citations

- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §3; §5.3; §6.1–6.5, Eqs. (43)–(46), Figs. 4–22.
- [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md) — App. F, Eqs. (F.1), (F.5), (F.9), (F.12), (F.29)–(F.30).
- [Cao et al. (2022)](/sources/cao-2022.md) — §3.1–3.2, Tables 1–4, Figs. 2–6.
- [Prakash et al. (2022)](/sources/prakash-2022.md) — §III.B.2, Eqs. (25)–(27), Figs. 5–7; §IV.
- [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md) — §6.1, Eqs. (123)–(125), Fig. 4.
- [Basile et al. (2023)](/sources/basile-2023.md) — §3.2, §4.2.1 (recalled TGV studies).
- [Pereira et al. (2021)](/sources/pereira-2021.md) — §IV.3.4 (recalled companion TGV study).
- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — Abstract; §3.8, Fig. 5.
- [Kou et al. (2023)](/sources/kou-2023.md) — §3, Table 1; §4.2, Eq. (28), Figs. 10–12.
- [Saini et al. (2023)](/sources/saini-2023.md) — §2.2, Eqs. (6)–(11); §3.1, Fig. 1; §4, Figs. 5–6; §5.1, Figs. 7–8.
- [Zhao et al. (2023a)](/sources/zhao-2023.md) — §4, Tables 3–4; §5.1, Eqs. (18)–(23), Figs. 3–7.
- [Wang et al. (2023b)](/sources/wang-2023-b.md) — §4.1, Tables 3–5, Figs. 5–8.
- [Duan & Wang (2024)](/sources/duan-2024.md) — §3, Eqs. (26)–(30); §5.1, Figs. 5–7; §6.
- [Wang (2024)](/sources/wang-2024-b.md) — §2.3, Eqs. (17)–(19); §4.1, Eq. (23), Figs. 2–3.
- [Wang et al. (2024)](/sources/wang-2024.md) — §2.3–2.5; §3.1, Eq. (14), Fig. 2.
- [Chapelier et al. (2024)](/sources/chapelier-2024.md) — HAL accepted manuscript: §I; §II.A–C, Eqs. 1–11, Figs. 2–4; §III.A–B, Tables I–II; §IV.A–B, Figs. 5–8; §V; App. A, Figs. 9–10.
- [Kurz et al. (2025)](/sources/kurz-2025.md) — arXiv v2: §4.4, Figs. 6–8; §5.2, Figs. 10–11.
- [Reddy et al. (2026)](/sources/reddy-2026.md) — 2021 preprint: §1; §7.1–7.2, Figs. 7–8; §9.
- [Brillon & Nadarajah (2026)](/sources/brillon-2026.md) — arXiv v1: §2.5, §2.9; §3.1.1–3.1.8, Eqs. (91)–(107), Tables 2–5, Figs. 2–19.
- [Caban et al. (2026)](/sources/caban-2026.md) — §5.1, Eq. (42), Figs. 9–11; §5.2, Figs. 14–17; §5.3.1, Eq. (45), Table 4, Figs. 18–23; §5.4, Tables 5–9; §6.
- [Ranjbar et al. (2026)](/sources/ranjbar-2026.md) — arXiv v1: §III.B, Eq. (46), Figs. 7–14; §III.D.3.
- [Volpiani (2024)](/sources/volpiani-2024.md) — §1; §4, Table 1, Figs. 4–5; §5, Figs. 6–18; §6.
- [Liang & Fu (2024)](/sources/liang-2024.md) — §4.10, Figs. 17–18; §4.11, Figs. 19–20.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §4.10, Fig. 21.
