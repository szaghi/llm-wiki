---
type: Benchmark
title: "Taylor–Green vortex"
description: "The triply periodic vortex flow that transitions from a single-mode analytic field to decaying turbulence: at Re 40,000 against a 5400³ DNS to separate Smagorinsky and implicit LES errors, at Re 1600 and 5000 to split numerical dissipation and test subgrid models, filter widths and filters, inviscid for energy conservation, and in 2D for commutator errors."
status: established
aliases: [TGV, Taylor-Green vortex, 2D Taylor–Green vortex, inviscid Taylor–Green vortex]
tags: [benchmark, les, implicit-les, sgs-model, dns, numerical-dissipation]
timestamp: 2026-10-26T10:27:00Z
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
| [Wang et al. (2024)](/sources/wang-2024.md) | finite differences, second-order kinetic-energy-preserving split form KGP2 against sixth-order optimized upwind OPT6, MUSCL3 and WENO5; inviscid with flow reversal | $30^3$ cells | the initial field (time reversal) |

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

**Recalled uses.** As recalled by [Basile et al. (2023)](/sources/basile-2023.md),
§3.2 and §4.2.1, Chapelier et al. fixed a modal-decay smoothness threshold
close to the $-5/3$ slope a priori from TGV DNS at $Re=5000$, and the
authors' earlier TGV tests showed high-order DG more accurate than low
order at equal degrees of freedom. As recalled by
[Pereira et al. (2021)](/sources/pereira-2021.md), the companion study of
[partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md)
on the transitional TGV found that the coherent structures driving
transition must be resolved, which fixes the minimum physical resolution.

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
