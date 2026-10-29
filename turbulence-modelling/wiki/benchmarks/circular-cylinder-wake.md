---
type: Benchmark
title: "Circular-cylinder wake"
description: "Flow past circular cylinders, chiefly at Re_D=3900, with separation, shear-layer roll-up and a turbulent wake: it tests neural-network SGS models, PANS, implicit LES, VMS LES and 2D URANS; the drag crisis, the supercritical regime and tandem cylinders test hybrid RANS/LES and immersed-boundary wall models, a Mach-3 cylinder tests wall models, and laminar cylinders validate solver numerics."
status: established
aliases: [cylinder wake, flow over a circular cylinder, flow past a circular cylinder, cylinder at Re_D=3900, tandem cylinders, tandem cylinder benchmark, drag crisis, critical cylinder flow, supercritical cylinder]
tags: [benchmark, separated-flow, les, implicit-les, neural-network, pans, immersed-boundary, field-inversion, des, hybrid-rans-les, aeroacoustics]
timestamp: 2026-10-29T07:40:00Z
---

# Circular-cylinder wake

A uniform stream of velocity $U_\infty$ passes a circular cylinder of
diameter $D$; the Reynolds number is $Re_D=U_\infty D/\nu$. In the regime
used by most sources ($Re_D$ of a few thousand to $10^4$) the boundary layer
is laminar and separates on the cylinder, the separated shear layers roll
up through a Kelvin–Helmholtz instability and become turbulent, and vortices
shed into a turbulent wake. The case is a bluff body without a geometric
separation point, so a model must get the separation, the transition in
the shear layers and the shedding together. The quantities compared are the
mean recirculation length $L_r$ (registry §11: distance from the base point
of the cylinder to the end of the mean recirculation on the centreline),
the base pressure coefficient $C_{pb}$ (page-local), the largest mean
backflow velocity on the centreline $U_{\min}$ (page-local), the drag
coefficient $C_D$, the shedding Strouhal number $St$, mean and fluctuating
velocity profiles at the stations $x/D=1.06$, 1.54 and 2.02, and spectra in
the wake. All lengths below are scaled by $D$ and velocities by $U_\infty$.

## Configurations in the sources

| Item | [Kim et al. (2024)](/sources/kim-2024.md) | [Dzanic et al. (2022)](/sources/dzanic-2022.md) |
|---|---|---|
| $Re_D$ | 3900 (training and main test); 5000 and 10,000 (untrained) | 3900 |
| Domain | $30D\times50D\times3.14D$ (15$D$ upstream), spanwise periodic | C-grid $[-10,25]\times[-10,10]\times[0,\pi]$ in units of $D$, spanwise periodic |
| Discretization | second-order central differences on a staggered grid, immersed boundary, incompressible fractional step | flux reconstruction (PyFR), compressible at $M=0.1$, $N=1$ and $N=3$ at nearly equal degrees of freedom, unstructured prisms |
| Reference simulation | DNS $1025\times501\times128$, $\Delta x_{\min}=0.004D$, $\Delta y_{\min}=0.002D$, $\Delta z=0.02453D$ | DNS at $N=3$, about 55.6 million degrees of freedom, $\eta_{\min}/D=0.011$ |
| Models tested | dynamic Smagorinsky (spanwise-averaged coefficient), six neural-network SGS models, no model | PANS on $k$-$\omega$ SST with $f_k=0.1$, 0.2, 0.3; under-resolved DNS without model |
| LES grids | $449\times271\times64$ (training resolution), $353\times213\times64$, $545\times301\times64$, coarser ones in App. C | $N=1$: $26{,}000\times20$ elements; $N=3$: $6500\times10$ |
| Averaging | $TU_\infty/D=200$ at $Re_D=3900$ | from $tU_\infty/D=100$ to 300 |
| External references | experiment of Parnaudeau et al.; DNS of Ma et al. | LES of Parnaudeau et al.; LES of Witherden et al. |

Reference values printed for the wake at $Re_D=3900$: the DNS of
[Kim et al. (2024)](/sources/kim-2024.md) gives $L_r=1.56$,
$C_{pb}=-0.87$, $U_{\min}=-0.31$, $C_D=1.00$ (Table 3); the DNS of
[Dzanic et al. (2022)](/sources/dzanic-2022.md) gives $St=0.209$, "in
agreement with" Parnaudeau et al., and a Kelvin–Helmholtz frequency
$f_{KH}D/U_\infty=0.668$ (§3.2). The two sources print different quantities,
so their DNS cannot be compared from what they print. At $Re_D=5000$ Kim et
al. run a new DNS ($2049\times1001\times128$, checked on
$2049\times1001\times192$ and $3073\times1281\times128$) giving $L_r=1.39$,
1.41, 1.37 and $C_D=1.01$, 1.00, 1.01 on the three grids, against the
experimental $L_r=1.40$ and $C_D=1.02$ of Norberg that they cite
(Table 1). At $Re_D=10{,}000$ the reference is the experiment of Dong et al.
as cited by Kim et al.: $L_r=0.82$, $C_{pb}=-1.13$, $U_{\min}=-0.25$,
$C_D=1.14$ (§4.2.3). Kim et al. (§4.2.3) cite Williamson for the trend that in this
shear-layer transition regime ($1000<Re_D<200{,}000$) the Strouhal number,
$-C_{pb}$ and $L_r$ decrease and the Reynolds stresses increase with
$Re_D$ (§4.2.3).

See [direct numerical simulation](/definitions/direct-numerical-simulation.md)
for the resolution of both DNS.

## What the case tests

**Neural-network SGS models on a complex geometry.**
[Kim et al. (2024)](/sources/kim-2024.md) train pointwise fully connected
[neural-network SGS models](/methods/neural-network-sgs-model.md) on
box-filtered DNS of the $Re_D=3900$ wake (25 snapshots over about 20
shedding cycles, four spanwise planes, the box $-1\le x/D\le6$,
$-1.5\le y/D\le1.5$, about $4.08\times10^6$ samples), mapping the resolved
strain rate or velocity gradient to the six components of $\tau_{ij}$. The
grid-filtered models (G-) see one filter level; the test-filtered models (T-)
also see a spanwise box test filter $\hat\Delta_z>\Delta_z$ of the same
field, either concatenated in one network (nFU) or in two branches whose
outputs are subtracted (the "fusion" FU architecture, motivated by the
Germano identity of the [dynamic procedure](/methods/dynamic-procedure.md);
§3.2). A posteriori results for $L_r$ (Table 3):

| Model | LES3900 (training grid) | LES3900c (coarser) | LES3900f (finer) | LES5000 | LES10000 |
|---|---|---|---|---|---|
| reference | 1.56 (DNS) | 1.56 | 1.56 | 1.39 (DNS) | 0.82 (exp.) |
| dynamic Smagorinsky | 1.32 | 0.80 | 1.45 | 1.35 | 0.62 |
| no model | 1.25 | 0.74 | — | — | 0.51 |
| G-SR / G-VG | 1.51 / 1.56 | 1.16 / 1.07 | 1.22 / 1.39 | — | — |
| T-SR-nFU / T-VG-nFU | 0.79 / 1.28 | — | — | — | — |
| T-SR-FU / T-VG-FU | 1.59 / 1.56 | 1.55 / 1.49 | 1.62 / 1.57 | 1.45 / 1.47 | 0.85 / 0.70 |

T-SR-nFU is thus farther from the DNS than no model on the training grid
*(compiler check, not in the sources)*. $-C_{pb}$ on the training grid is 0.90, 0.88, 0.88
and 0.86 for G-SR, G-VG, T-SR-FU and T-VG-FU, against 0.94 for dynamic
Smagorinsky and 0.87 for the DNS; at $Re_D=10{,}000$ T-SR-FU gives
$-C_{pb}=1.17$ and $C_D=1.10$ against 1.13 and 1.14 measured (Table 3).
The authors' reading:

- The non-fused test-filtered networks give, a priori, a mean SGS shear
  stress and SGS dissipation of the wrong sign in the near shear layers at
  $x/D=1.06$; the weak SGS dissipation lets the shear layers transition too
  early a posteriori (§4.1, §4.2.1, Figs. 6, 9). All networks predict the
  mean SGS shear stress, dissipation and backscatter better than dynamic
  Smagorinsky a priori, whose backscatter is zero by construction (§4.1);
  see [energy backscatter](/definitions/energy-backscatter.md).
- A better a priori prediction does not guarantee a better a posteriori
  one (§4.1; see [a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)).
- The fused networks keep their accuracy on untrained grids and at
  untrained $Re_D$, whereas the grid-filtered ones degrade off the training
  grid (§4.2.2–4.2.3).
- On the untrained finer grid the authors find dynamic Smagorinsky in good
  agreement with the DNS ($L_r=1.45$ against 1.56) and the fused networks
  still good (1.62 and 1.57), the grid-filtered ones worse (§4.2.2,
  Table 3).
- On the two coarsest grids (Gcc-64, Gccc-64) LES with T-SR-FU, dynamic
  Smagorinsky and no model all diverge; T-SR-FU runs once its stresses are
  set to zero wherever backscatter occurs (App. C).
- Cost on 18 cores: a full time step costs about 2.5 (G-SR) and 2
  (T-SR-FU) times dynamic Smagorinsky on the same grid; T-SR-FU on the
  coarser grid (2.113 s per step) gives results very similar to dynamic
  Smagorinsky on the finer grid (2.986 s per step) with about half the grid
  points (App. E, Table 6).

Kim et al. also estimate the discretization error of the finite-difference
velocity gradient on the LES grids, following Sirignano et al.: the mean
relative difference from the DNS-grid gradient is 0.5690, 0.5455, 0.5320,
0.5136 and 0.4986 from the coarsest grid to LES3900f; they call these
errors "not so significant" and conclude that the networks "may not
suffer" from them (§4.2.2, Table 4); see
[discretization-consistent closure](/definitions/discretization-consistent-closure.md)
for sources that build the discretization error into the closure.

**High order for hybrid RANS/LES.** [Dzanic et al. (2022)](/sources/dzanic-2022.md),
§3.2, compare [partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md)
with unmodelled under-resolved DNS, which they identify with
[implicit LES](/definitions/implicit-les.md), at second and fourth order in
[flux reconstruction](/methods/flux-reconstruction.md):

- Low-order under-resolved DNS overpredicts the edge of the recirculation
  region, which high order remedies; at high order PANS generally prolongs
  the recirculation region (Fig. 8).
- The best agreement is at $f_k=0.3$ at low order (with the DNS) and at
  $f_k=0.1$ at high order (with the LES of Witherden et al.) (Figs. 9–10).
- Low-order runs overpredict the shedding and Kelvin–Helmholtz peak
  frequencies at $x/D=3$ by "roughly 10% and 6%"; high-order runs match the
  DNS frequencies. At $x/D=7$ only high-order PANS resolves both peaks
  (Figs. 11–12); see [numerical dissipation](/properties/numerical-dissipation.md).
- The primary POD mode of the streamwise velocity is placed too far aft at
  low order; high-order PANS agrees with the DNS, high-order under-resolved
  DNS places the shedding region too close to the cylinder (Fig. 13).

**Immersed boundaries on a lattice Boltzmann solver.**
[Cheylan et al. (2023)](/sources/cheylan-2023.md) use the laminar cylinder
at $Re_D=100$ to calibrate a direct-forcing
[immersed boundary method](/methods/immersed-boundary-method.md) in the
[lattice Boltzmann](/methods/lattice-boltzmann-method.md) code
[ProLB](/software/prolb.md): the drag error falls from 0.52 at
$\Delta x=0.08D$ to 0.035 at $\Delta x=0.005D$, with
$C_D=1.408$ against the reference 1.36 (Table 3), and the slip error
scales with the Courant number (§3.1). Their turbulent case is the
benchmark of Breuer et al., an elastic beam behind a fixed cylinder at
$Re_D=10{,}000$, computed as LES with a shear-improved
[Smagorinsky model](/methods/smagorinsky-model.md): Strouhal numbers 0.185
and 0.101 against 0.175 and 0.103 of Breuer et al. (§3.4, Table 13).

**Tandem cylinders for hybrid RANS/LES.** [Wang et al. (2021)](/sources/wang-2021-l.md),
§3.2, use the tandem-cylinder configuration (two cylinders of diameter $D$
in line, spacing $L=3.7D$, with the experiments of Jenkins et al.
and Neuhart et al. and the grid of the ATAAC project) at $M=0.1285$ and
$Re_D=1.6\times10^5$ to compare an IDDES built on the SSG/LRR-$\omega$
[Reynolds-stress model](/methods/reynolds-stress-model.md) (RSM-IDDES)
with SST-IDDES (see
[detached-eddy simulation](/methods/detached-eddy-simulation.md)). The
2D grid of 92,500 cells is extruded over 120 spanwise layers (11.1 million
cells), with pressure far field, no-slip walls and periodic span; the
solver is a cell-centred second-order finite-volume code with an
adaptive-dissipation Roe scheme.

- Mean $C_p$ on both cylinders is "almost identical" for the two models and
  agrees with experiment (Fig. 4). On the downstream cylinder SST-IDDES
  slightly over-predicts the peaks of the RMS pressure coefficient at the
  vortex-impingement angles $45^\circ$ and $315^\circ$; RSM-IDDES agrees
  better, including the separation positions near $110^\circ$ and
  $250^\circ$ (Fig. 5).
- SST-IDDES delays the onset of the shear-layer instability; RSM-IDDES
  gives a shorter shear layer and more small-scale structures, closer to
  the PIV (Fig. 6). On the separate launch-vehicle test of the same paper
  the authors find the RSM-IDDES subgrid stresses smaller than those of
  SST-IDDES and, following Spalart, link smaller subgrid stress to a faster
  Kelvin–Helmholtz instability (§3.3).
- Primary shedding frequency and sound pressure level at the upstream (A)
  and downstream (B) cylinder (Table 1):

| | SST-IDDES | RSM-IDDES | experiment |
|---|---|---|---|
| frequency (Hz) | 172 | 176 | 179 (A), 180 (B) |
| SPL at A (dB) | 115.6 | 114.3 | 116.5 |
| SPL at B (dB) | 137.6 | 136.8 | 138.6 |

**Laminar cylinder for a high-order immersed boundary.**
[D'Ayer et al. (2026)](/sources/dayer-2026.md) (read in the submitted
manuscript), §3.1, validate a volume-penalization
[immersed boundary method](/methods/immersed-boundary-method.md) in the
[spectral difference](/methods/spectral-difference-method.md) code JAGUAR
on the steady 2D cylinder at $Re_D=40$ and $M=0.2$, polynomial degree
$N=2$, against a body-fitted run of the same code. The domain is
$[-30,50]\times[-30,30]$ in units of $D$, with near-wall cells of $0.01D$; the body-fitted mesh has 182,000 cells
(1.63 million solution points), the immersed one 263,000 (2.37 million)
(Table 1). Values in Table 2:

| | recirculation length (printed $L/D$) | separation angle | $C_D$ |
|---|---|---|---|
| Kou et al. (flux reconstruction, as reported) | 2.27 | $52.0^\circ$ | 1.52 |
| Choi et al. (as reported) | 2.27 | $52.0^\circ$ | 1.52 |
| JAGUAR body-fitted | 2.27 | $52.2^\circ$ | 1.55 |
| JAGUAR immersed boundary | 2.25 | $52.1^\circ$ | 1.54 |

Body-fitted and immersed values differ by less than 1%. The wall $C_p$
agrees closely; the wall vorticity of the immersed run oscillates near the
cylinder, which the authors attribute to cells cut by the discontinuous
mask, inside which a polynomial cannot represent the jump (a Runge
phenomenon) (Figs. 3–5). The immersed $C_D$ is the volume integral of the
penalization force (Eq. 26).

**Unseen geometry for adjoint-trained closures.** As reported on
[model-consistent training](/methods/model-consistent-training.md),
[Sirignano & MacArt (2023)](/sources/sirignano-2023.md), §6, run their
learned SGS closures, trained on rectangular prisms, on a cylinder at
$Re=1000$ never seen in training: the closures "suppress all artificial
primary recirculation", as the DNS does, while no-model LES and the
[anisotropic minimum-dissipation model](/methods/anisotropic-minimum-dissipation-model.md)
predict two recirculation regions (Figs. 13–14).

**Laminar mean-flow assimilation on a high-order discretization.**
[Fanizza et al. (2025)](/sources/fanizza-2025.md), §4.1, validate adjoint
data assimilation of a steady RANS-type system on a modal
[discontinuous Galerkin](/methods/discontinuous-galerkin-spectral-element-method.md)
discretization (ONERA's Aghora code) on the laminar cylinder at $Re_D=80$
and $M=0.15$. The flow sheds vortices; the target is the time-averaged DNS
on the same mesh, which a steady computation does not reproduce: the
baseline steady solution over-estimates the wake size. Grid: 4386 cubic
quadrangles extending to 30$D$, no-slip adiabatic wall, non-reflecting far
field. A momentum and energy source $\rho\boldsymbol f_{\mathrm{DA}}$ (the
correction compared on the
[field inversion](/methods/field-inversion-machine-learning.md) page) is
inferred from dense velocity data with no penalty at polynomial degrees
$N=1$, 2, 3; the corrected axial momentum is "in good agreement with DNS"
at all three degrees (Figs. 4–5). The cost falls by more than three orders
of magnitude at $N=1$ and more than four at $N=2$ and 3, with the lowest
minimum at $N=2$, the lowest degree at which the baseline is free of
mesh-dependency errors (Fig. 6); the authors recommend running the
assimilation at that degree, since higher $N$ adds degrees of freedom the
mean flow does not need. The turbulent bluff-body test of the same paper
is the
[square cylinder](/benchmarks/square-cylinder-flow.md).

**Laminar cylinders for fluid–structure interaction and aeroacoustic adjoints.**
Two further sources use the laminar shedding cylinder to verify a solver,
not a turbulence model.

- [Liu et al. (2022b)](/sources/liu-2022-g.md), §3.1.2, Table 2, verify a
  partitioned fluid–structure coupling in a third-order
  [flux-reconstruction](/methods/flux-reconstruction.md) solver on moving
  triangular grids. The test is the vortex-induced vibration of a
  zero-mass cylinder free to move across the stream at $Re_D=100$,
  $M=0.1$. On 1440, 3360 and 13,120 elements they obtain the plunge
  amplitude $h_p/D=0.44$, 0.42, 0.41, $St=0.149$, 0.148, 0.145 and mean drag
  $C_D=1.66$, 1.61, 1.58 ($h_p$ page-local, not the cell size $h$). The five
  earlier studies they list span $h_p/D=0.42$–0.47, $St=0.146$–0.175 and
  $C_D=1.60$–1.75. The coupling stays stable at zero body mass because the
  fluid impedance enters the rigid-body equation as a damping term (§2.3,
  Eq. 23). A second case adds a nonlinear energy sink at $Re_D=106$
  (§3.2, Table 3; see the
  [geometric conservation law](/properties/geometric-conservation-law.md)
  for the moving-grid formulation).
- [Monfaredi et al. (2021)](/sources/monfaredi-2021.md), §4.1, verify an
  unsteady continuous adjoint of a URANS solver coupled with the
  [Ffowcs Williams–Hawkings analogy](/methods/ffowcs-williams-hawkings-acoustic-analogy.md)
  on a 2D cylinder "in a laminar flow" at $Re=1000$ and $M_\infty=0.2$,
  with $D=0.019$ m. The O-grid has 49,280 nodes ($308\times160$) out to
  $35D$, and about 50 time steps resolve one shedding period. They obtain
  $St=0.24$ and $C_D=1.42$, which they call close to the 0.234 and 1.56
  of an earlier URANS. Adjoint sensitivities of the mean lift, the mean
  drag and a far-field noise objective agree with central finite
  differences (Fig. 5). The same paper's turbulent case is the rod–airfoil
  configuration, whose rod is a cylinder of diameter $c/10$ one chord
  upstream of a NACA 0012 at $Re_c=4.8\times10^5$ ($c$ the chord). There the 2D
  Spalart–Allmaras URANS gives $St=0.24$, as an earlier 2D URANS does,
  against an experimental value of about 0.19. The authors take this
  overprediction of the shedding frequency as a known shortcoming of URANS
  (§1, §4.2).
- [Zou et al. (2025)](/sources/zou-2025-b.md), §III B–C, verify a
  moving-mesh interior-penalty DG solver with block-based adaptive
  refinement (schemes IP(2), IP(3), IP(4) of second to fourth order, the
  polynomial degree not printed; vorticity threshold
  $|\omega_z|D/(2U_\infty)>0.25$ for the finest of five levels) on the
  shedding cylinder at $Re_D=150$, $M=0.2$, $D=0.1$, in a domain
  $[-2.4,4.4]\times[-2.4,2.4]$ (Table II):

  | Run or reference | mean $C_D$ | $\Delta C_D$ | $\Delta C_L$ | $St$ |
  |---|---|---|---|---|
  | IP(2) | 1.33 | 0.0497 | 1.016 | 0.187 |
  | IP(3) | 1.3503 | 0.0518 | 1.04 | 0.1845 |
  | IP(4) | 1.3547 | 0.0512 | 1.0456 | 0.1847 |
  | Zhang et al. (as printed) | 1.348 | 0.0519 | 1.048 | 0.184 |
  | Müller (as printed) | 1.34 | 0.05228 | 1.0406 | 0.183 |

  ($\Delta$ the peak-to-peak amplitude.) The IP(2) flow field shows
  "significant flow field distortion", and the IP(3) and IP(4) vorticity
  fields differ negligibly (Fig. 8). Six
  transverse vortex-induced vibration runs (mass ratio 2, no damping,
  reduced velocity 3 to 8, $M=0.085$, IP(3)) reproduce the lock-in
  amplitude curve of Ahn & Kallinderis and of Borazjani et al., with
  lock-in between reduced velocities of about 4 and 7 (Fig. 10). With two
  synthetic jets at reduced velocity 4 and momentum coefficient 3.0, the
  vibration amplitude falls from 0.562 to 0.0001 at dimensionless actuation
  frequency 5, and to 0.0113, 0.2149 and 0.3153 at 50, 75 and 90 (Table
  III), which the authors attribute to the jet energy leaving as acoustic
  waves at the higher frequencies, from density contours (Figs. 15–17). The
  authors call these two-dimensional laminar runs without a turbulence
  model "direct numerical simulations" (§III C; see
  [direct numerical simulation](/definitions/direct-numerical-simulation.md)).

**Steady laminar cylinder for $h$-adaptation indicators.**
[Bulgarini et al. (2025b)](/sources/bulgarini-2025-b.md), §4.3, compare
four refinement indicators of an isogeometric DG solver (see
[isogeometric analysis](/methods/isogeometric-analysis.md) and
[mesh adaptation](/methods/mesh-adaptation.md)) on the steady cylinder at
$Re_D=40$ and $M=0.1$: an O-type $N=2$ geometry of $16\times18$ rational
Bézier patches with far field at $20D$, four adaptation cycles from a
converged $N=3$ solution, 25% of the elements refined per cycle, and a
reference uniform mesh of 4608 elements at $N=3$ (73,728 degrees of
freedom) with $C_{D,\mathrm{ref}}=1.41764$. The indicators are the
small-scale energy density (SSED: the $L^2$ norm of the momentum content
above degree $N-1$, normalized by the element size), the spectral decay
(SD: the same norm divided by the $L^2$ norm of the momentum, cited to
Persson & Peraire), and a local and a global non-conformity measure of the
interface jumps (LNC, GNC; Eqs. 39–43). All four mark the separation and
the edge of the recirculation and give a speed-up of about 2 against the
reference mesh; SSED over-refines the detachment region, GNC and SSED also
refine regions outside those of interest, SD is "the most effective
overall", LNC performs similarly and "should be used for lower solution
approximations", and anisotropic refinement is more efficient than
isotropic (Figs. 9–10). The same authors then use SD on the
[NACA 0012](/benchmarks/naca-0012-airfoil.md) and the T106A
[turbine cascade](/benchmarks/turbine-cascade.md).

**A transonic cylinder for adaptive-dissipation implicit LES.**
[Tsoutsanis & Nogueira (2025)](/sources/tsoutsanis-2025.md), §5.4, run the
cylinder at $Re_D=1.66\times10^5$ and $M_\infty=0.8$, the experiment of
Murthy & Rose, as an [implicit LES](/definitions/implicit-les.md) with
CWENOZ3 and CWENOZ4 reconstructions plus their a priori
dissipation–dispersion adjustment (ADDA; see
[numerical dissipation](/properties/numerical-dissipation.md)): a hybrid
mesh of about 12 million cells, $20D$ upstream, $50D$ downstream, span
$\pi D$ with 240 cells, $y^+\approx1$, wake refinement over $20D$ with mean
cell length $0.04D$; second-order implicit time stepping with
$\Delta t=t_c/500$, $t_c=D/U_\infty$, $40t_c$ of transient and $90t_c$ of
statistics. CWENOZ4-ADDA gives a shorter wake, more resolved structures and
more high-dissipation regions than CWENOZ3-ADDA; the surface $C_p$ agrees
with Macha and with Murthy & Rose up to $83^\circ$, beyond which all
predictions are sensitive; the scheme stays robust with the shocks,
shocklets and shock/boundary-layer interaction of the flow (Figs. 26–29).

**Implicit LES with a weighted compact nonlinear scheme.**
[Ma et al. (2022)](/sources/ma-2022.md), §3.2, run the cylinder at
$Re_D=3900$ as [implicit LES](/definitions/implicit-les.md) (no SGS
model) with two variants of a weighted compact nonlinear finite-difference
scheme, the original one with an explicit fifth-order nonlinear
interpolation (WCNS-E) and their seventh-order nonlinear tri-diagonal
compact interpolation (WCNS-T; see
[WENO schemes](/methods/weno-scheme.md)). The O-type grid has
$180\times180\times45$ points (streamwise, wall-normal, spanwise) over a
span of $\pi D$ with first wall-normal spacing $0.001D$; the Mach number and
the averaging time are not printed. References are the experiments of Ong
& Wallace, Lourenco & Shih and Parnaudeau et al., the DNS of Ma et al. and
the LES of Kravchenko & Moin and of Lysenko et al.

- The WCNS-T mean streamwise velocity is U-shaped close to the cylinder;
  the authors relate the U/V shape to the position of shear-layer
  transition and state that their runs "confirm" Lysenko et al.'s
  statement that larger inherent numerical dissipation moves the
  shear-layer transition upstream (Fig. 7); see
  [numerical dissipation](/properties/numerical-dissipation.md).
- WCNS-T wake-centreline velocity and surface $C_p$ agree with the
  references; the transverse-velocity spectra at $x/D=3$ and 5 match them
  "much better" than WCNS-E, with a clear inertial subrange, which the
  authors read as WCNS-T not being over-dissipative (Figs. 8–9).
- The comparisons are graphical; no recirculation length, $C_D$ or $St$ is
  printed, so the run cannot be placed in the $L_r$ table above.

**Variational multiscale LES with an immersed cylinder.**
[Kang & Masud (2022)](/sources/kang-2022.md), §5.1, validate their
variational multiscale immersed boundary (VMIB) method, a finite-element
[immersed boundary method](/methods/immersed-boundary-method.md) with
weakly imposed no-slip, combined with the residual-based
[variational multiscale](/methods/variational-multiscale-method.md) LES
model, on the cylinder at $Re_D=3900$ ($\rho=1$, $\mu=2.5641\times10^{-4}$,
$D=1$, $U_\infty=1$). The domain is $-10\le x\le20$, $-20\le y\le20$,
$0\le z\le3.14$, with slip lateral walls and a traction-free outflow; a 2D
quadrilateral mesh extruded over 48 spanwise layers gives 1,514,976 linear
hexahedra whose nodes do not lie on the cylinder; $\Delta t=0.0025$. No
wall resolution in wall units and no averaging time are printed.

- Mean centreline velocity, mean velocity profiles, fluctuations and
  Reynolds shear stress at $x/D=6$, 7, 10 show "good correlation" with the
  LES of Kravchenko & Moin, the experiments (Norberg; Ong & Wallace;
  Lourenco & Shih as reported by Kravchenko & Moin) and the authors'
  earlier body-fitted VMS LES (Figs. 7–12); wake spectra at $x/D=5$, 7, 10
  show a $-5/3$ range (Fig. 13).
- The element-wise error of the weakly imposed no-slip condition, the
  norm of the interfacial fine-scale velocity, stays within 3% of the
  inflow velocity (Fig. 16); Newton iterations converge quadratically, at
  most three per step (Table 3).
- As for Ma et al., the comparison is graphical, without integral values.

**Two-dimensional URANS with high-order DG and adaptive time steps.**
[Ghidoni et al. (2022)](/sources/ghidoni-2022.md), §6.1–6.3, use the
cylinder to assess adaptive time-step control of linearly implicit
(Rosenbrock and peer) time integrators for a high-order modal
[discontinuous Galerkin](/methods/discontinuous-galerkin-spectral-element-method.md)
discretization of 2D URANS with a log-$\omega$
[$k$-$\omega$ model](/methods/k-omega-model.md), at polynomial degree
$N=5$. The cases are:

- $Re_D=3900$, compressible at $M=0.1$ and incompressible, 4037 hybrid
  quadratic elements (84,777 degrees of freedom per equation), first
  element height $y_1^+<4$;
- $Re_D=1.4\times10^5$, compressible at $M=0.1$, 4343 elements;
- tandem cylinders at $Re_D=1.66\times10^5$ with spacing $3.7D$, 5558
  elements, compared with the wall $C_p$ of Khorrami et al.

Values printed for $Re_D=3900$ (Table 9): compressible $C_D=1.62$, RMS lift
coefficient 1.13, $St=0.23$, $-C_{pb}=1.84$, $U_{\min}=-0.43$, separation
angle $87^\circ$; incompressible 1.52, 1.13, 0.23, 1.90, $-0.43$,
$86^\circ$. The authors state that these differ from LES, DNS and
experiment but agree with other 2D URANS (Rajani et al., $C_D=1.65$,
$St=0.244$), and attribute the gap to the missing 3D effects; their aim is
time-integration efficiency, not prediction. At $Re_D=1.4\times10^5$ the
fully turbulent $k$-$\omega$ model (which, unlike Spalart–Allmaras, has no
way to keep the boundary layer laminar up to separation) gives
$St=0.27$, $C_D=0.75$, separation at $91^\circ$, $-C_{pb}=0.86$,
$L_r=0.72$ and RMS lift 0.44, close to the 2D RANS of Moussaed et al.
(Table 12). The time-integration findings (adaptivity helps only near and
beyond the step at which the linearization of a linearly implicit scheme
fails; observed temporal orders on the turbulent cylinder from 1.8 for
the fifth-order peer scheme to 5.4 for ROD5_1) belong to the numerics and
are summarized on the Source page.

**The drag crisis with a temporal-filtering hybrid RANS/LES.**
[Mays et al. (2023)](/sources/mays-2023.md) run the smooth cylinder in the
critical and super-critical regimes, $Re_D=2.5\times10^5$, $3.8\times10^5$,
$5.3\times10^5$ and $7.2\times10^5$, where transition right after laminar
separation lets the flow reattach, separation moves aft and $C_D$ falls.
They cite Zdravkovich for a fall to about 0.2 and Rodríguez et al. for a
value that settles at 0.24, and Lehmkuhl et al. for three successive states:
one-bubble asymmetric, two-bubble asymmetric and two-bubble symmetric
(§1; see [laminar separation bubble](/definitions/laminar-separation-bubble.md)).
The model is the scale-resolving hybrid (SRH) of Duffal et al., a
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) obtained by formally
applying a temporal filter: the dissipation term of the modelled
$k$ equation is multiplied by a factor $\psi_H\ge1$ (registry §11) that
depends on the time-averaged total turbulent kinetic energy, modelled plus
resolved, and on a theoretical modelled-to-total energy ratio computed from
the cell size and time step, with a shielding function of wall distance
over a Kolmogorov length enforcing URANS near the wall (§2.1.2, Eqs. 9–13).
The base RANS is the three-equation lag elliptic-blending
[$k$-$\varepsilon$ model](/methods/k-epsilon-model.md) of Lardeau & Billard,
in Simcenter STAR-CCM+ 2022.1 (segregated incompressible finite volume,
second-order backward time, a hybrid of second-order upwind and bounded
central convection blended by the shielding function; §2.1.1, §2.2).

*Set-up* (§3, Tables 1, 3): a $20D\times20D$ domain with the cylinder $5D$
from the inlet (5% blockage), spanwise periodic over $1.6D$ (grids A, B) or
$1.0D$ (C, D), no inlet turbulence, first-cell $y^+<1$ everywhere,
initialization from RANS, statistics over at least 25 shedding cycles. The
grids have 7.65, 9.72, 12.43 and 16.64 million cells, about five times fewer
than the wall-resolved [WALE](/methods/wale-model.md) LES of Rodríguez et
al. used as reference (38.4–89.4 million).

*Results* (Tables 2, 4–5):

| $Re_D$ | case | $C_D$ | $C_{L,\mathrm{rms}}$ | $-C_{pb}$ | $L_r$ | $St$ |
|---|---|---|---|---|---|---|
| $2.5\times10^5$ | URANS (A) | 0.436 | 0.187 | 0.95 | 1.107 | 0.35 |
| | SRH (A) | 0.743 | 0.238 | 0.73 | 0.611 | 0.24 |
| | SRH (B) | 0.781 | 0.311 | 0.80 | — | — |
| | WALE LES (A) / (C) | 1.247 / 0.812 | 0.008 / 0.491 | 0.55 / 0.90 | — | — |
| | reference LES | 0.833 | 0.486 | 0.99 | 0.559 | 0.25 |
| $3.8\times10^5$ | URANS (B) | 0.354 | 0.082 | 0.94 | 1.311 | 0.40 |
| | SRH (B) | 0.456 | 0.159 | 0.39 | 0.603 | 0.28 |
| | reference LES | 0.481 | 0.217 | 0.48 | 0.641 | 0.23 |
| $5.3\times10^5$ | URANS (C) | 0.204 | 0.0396 | 0.95 | 1.339 | 0.43 |
| | SRH (C) / (D) | 0.252 / 0.292 | 0.0569 / 0.0628 | 0.35 / 0.31 | 0.676 (C) | 0.35 (C) |
| | reference LES | 0.296 | 0.0705 | 0.305 | 0.727 | 0.38 |
| $7.2\times10^5$ | URANS (D) | 0.156 | 0.0294 | 0.93 | 1.184 | 0.52 |
| | SRH (C) / (D) | 0.301 / 0.276 | 0.0365 / 0.0552 | 0.44 / 0.31 | 0.595 (D) | 0.43 (D) |
| | reference LES | 0.213 | 0.0752 | 0.224 | 0.569 | 0.45 |

The authors' reading:

- URANS with the same base model misses the drag crisis: the eddy
  viscosity in the separated shear layers, which they put at least ten
  times the SRH subgrid value (maximum SRH ratio $\nu_t/\nu=9.4$–18.3,
  Table 6), keeps the shear layers stable and the recirculation far too
  long, as Palkin et al. found for linear eddy-viscosity URANS (§3.2.1).
- SRH gives near-LES mean drag, Strouhal number and recirculation length on
  meshes five times coarser than the reference; on the coarse grid A the
  in-house WALE LES over-predicts the drag ($C_D=1.247$) where SRH gives
  0.743 (§3.1, §3.2.2, §4).
- Force fluctuations are damped by the near-wall URANS region, and the
  $C_p$ plateau of the separation bubble is matched less well at the two
  lower $Re_D$; the one-bubble asymmetric state at $2.5\times10^5$, with a
  mean lift an order of magnitude larger than at the other $Re_D$, and the
  return to symmetry at super-critical $Re_D$ are reproduced (§3.2.2,
  Figs. 6, 8).
- Following the criteria of Heinz, the resolved fraction rises under
  refinement while the total turbulent kinetic energy stays nearly
  constant, and the predicted energy ratio approximately matches the
  realized one in turbulent regions (§3.1.1, §3.2.2, Figs. 4, 10).
- SRH on grid A costs 4695 CPU hours, about 39% of WALE on grid C and 51%
  of WALE on grid B at $Re_D=2.5\times10^5$ (Table 3).
- Near-wall resolution must stay high, because under-resolution there is
  fatal to the prediction of transition and separation (§4).

**The supercritical regime with self-adaptive hybrid models.**
[Wu et al. (2024)](/sources/wu-2024.md), §3.2, run the cylinder at
$Re_D=3\times10^6$, $M=0.2$, in the structured code
[PHengLEI](/software/phenglei.md), to test whether a hybrid model captures
the supercritical topology, in which the boundary layer turns turbulent
before separating, separation moves aft and alternate shedding is
suppressed. The models are SST-IDDES, the constant-coefficient
[self-adaptive turbulence eddy simulation](/methods/self-adaptive-turbulence-eddy-simulation.md)
(SATES-SM) and its variant SATES-σ, whose cut-off coefficient is scaled
locally by a [σ-model](/methods/sigma-model.md) factor that vanishes in pure
shear; the convective scheme is the fourth-order linear-weight
[weighted compact nonlinear scheme](/methods/weighted-compact-nonlinear-scheme.md)
(WCNS-E-4), with a MUSCL scheme as the dissipative alternative.

*Set-up* (§3.2): 20$D$ upstream, 25$D$ downstream, 20$D$ transverse, span
$1D$ periodic (justified by a spanwise correlation length below $1D$, as the
authors cite), about 6.7 million cells with $y^+<1$, 150 flow-through times
of which the last 80 are averaged; the time step is printed
"$\Delta tD/U_\infty=1\times10^{-3}$".

*Results* (Table 3; $C_{pb}$ and $L_r$ as defined above):

| case | $St$ | $C_{pb}$ | $L_r$ | $C_D$ |
|---|---|---|---|---|
| SST-IDDES (WCNS) | 0.29 | $-0.68$ | 0.63 | 0.62 |
| SATES-SM (WCNS) | 0.20 | $-1.69$ | 0.33 | 1.39 |
| SATES-σ (WCNS) | 0.24 | $-0.34$ | 0.79 | 0.55 |
| SATES-σ (MUSCL) | 0.19 | $-1.32$ | 0.61 | 1.26 |
| DES, Travin et al. (cases DES-TS7 / DES-TS10, as printed) | 0.35 / 0.33 | $-0.53$ / $-0.64$ | 1.0 / 1.0 | 0.41 / 0.51 |
| LES, Chen et al. (as cited) | 0.311 | $-0.696$ | 0.527 | — |
| LES, Catalano et al., $Re_D=1\times10^6$ (as cited) | 0.35 | $-0.32$ | 1.04 | 0.31 |
| experiment, Shih et al., $Re_D=1\times10^6$ (as cited) | 0.22 | $-0.33$ | — | 0.24 |

The authors' reading:

- SATES-SM predicts "the incorrect flow topology of the subcritical
  regime" ($C_D=1.39$); SATES-σ predicts a turbulent separation that
  suppresses alternate shedding, the supercritical topology (§3.2,
  Figs. 8–10).
- SATES-σ keeps the eddy viscosity low in the initial boundary layer near
  the front stagnation point: the cut-off coefficient rises from its floor
  0.15 to values above 1.0 before separation, the resolution control
  function rises from a low value to 1 near the wall while it stays near 1
  in SATES-SM (Figs. 8, 11–12). With this, the resolved turbulent kinetic
  energy and $C_{p,\mathrm{rms}}$ stay low on the front half, peak sharply,
  then decay, which the authors read as captured laminar–turbulent
  transition; SATES-σ gives the mean $C_f$ closest to Achenbach's
  experiment (Figs. 9–10).
- With MUSCL the same model fails to delay separation, giving a
  subcritical-like $C_p$ and higher drag, a damped Kelvin–Helmholtz
  instability, a shorter recirculation and a wake spectrum without its
  moderate-frequency content (Figs. 13–17), so the authors call the
  low-dissipation scheme "more accurate and necessary" (§4; see
  [numerical dissipation](/properties/numerical-dissipation.md)).
- Results in this regime are sensitive to inflow perturbation, model and
  scheme, and the experiments and simulations they cite "do not have good
  convergence"; the criterion they adopt is the correct tendency of the
  flow topology (§3.2).

**Wall-modelled immersed boundaries from $Re_D=3900$ through the drag
crisis.** Two sources impose a wall model through an
[immersed boundary method](/methods/immersed-boundary-method.md) on a
Cartesian grid and run the cylinder from the subcritical regime upward:

- [Wang et al. (2024d)](/sources/wang-2024-k.md), §III D, in a GPU
  immersed-boundary–[lattice Boltzmann](/methods/lattice-boltzmann-method.md)
  solver with the [Smagorinsky model](/methods/smagorinsky-model.md)
  (constant 0.12, the paper's default "unless otherwise specified", filter
  width the lattice spacing), compare a
  diffused-interface (DIB) and a sharp-interface (SIB) immersed boundary.
  Five grid blocks refined by factors of 2 give $D/160$ at the wall and
  $D/80$ in a wake zone to $2D$; span $4D$ periodic, streamwise domain
  $16D$. At $Re_D=3900$, without wall model, they obtain (Table II):

  | Run | $C_D$ | $St$ | separation angle |
  |---|---|---|---|
  | DIB | 1.02 | 0.215 | $88^\circ$ |
  | SIB | 0.98 | 0.217 | $88^\circ$ |
  | references (Fröhlich et al., Kravchenko & Moin, Meyer et al.) | 1.04–1.08 | 0.210–0.216 | $88^\circ$ |

  With the [equilibrium wall model](/methods/equilibrium-wall-model.md)
  at $Re_D=10^5$ to $10^6$, the DIB run captures the drag crisis through
  the backward shift of separation, its drag falling "from 0.99 to 0.28 and
  0.22" at $Re_D=10^5$, $5\times10^5$ and $10^6$; the SIB run misses the
  separation at high $Re_D$ and gives a lower drag (Figs. 14–15). The
  authors' conclusion is that the diffused interface, which drives
  separation more easily, suits external flows (§IV); the same pairing is
  on [Ahmed body](/benchmarks/ahmed-body.md).
- [Yan et al. (2024)](/sources/yan-2024.md), §III A, couple a
  diffused-interface immersed boundary with explicit wall functions (see
  [non-equilibrium wall models](/methods/nonequilibrium-wall-model.md) and
  [slip-wall models](/methods/slip-wall-model.md)) in the sixth-order
  compact code [Xcompact3d](/software/xcompact3d.md), whose subgrid
  dissipation is the implicit
  [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
  with viscosity ratio at the cut-off $\nu_0/\nu=15$ at $Re_D=3900$ and 300
  at $Re_D=1.4\times10^5$. Domain $-5D\le x\le15D$, $-10D\le y\le10D$,
  span $\pi D$, grid $801\times387\times40$ with about 40 points across the
  diameter, $U_0\Delta t/D=2.5\times10^{-3}$. Their bulk values (Tables
  II–III; recirculation length $L_r$, printed $l_r$):

  | Run | $\overline{C}_D$ | $C_{L,\mathrm{RMS}}$ | $L_r/D$ | $-\overline{C}_{pb}$ | $St$ |
  |---|---|---|---|---|---|
  | $Re_D=3900$, sixth order + iSVV | 1.02 | 0.113 | 1.42 | 0.93 | 0.229 |
  | $Re_D=3900$, second-order central + Smagorinsky, same mesh | 1.17 | 0.017 | 2.42 | 0.59 | 0.223 |
  | $Re_D=1.4\times10^5$, sixth order + iSVV | 1.01 | 0.24 | 0.98 | 1.04 | 0.22 |

  At $Re_D=1.4\times10^5$ the cited LES give $L_r/D=0.42$–0.62 and the
  experiment 0.44, which the authors attribute to flow sensitivity, the
  eddy-viscosity model and the simplified thin-boundary-layer equation of
  the wall model; they also find the favourable-pressure-gradient wall
  stress ahead of separation under-predicted, because the Werner–Wengle
  law ignores favourable gradients (Fig. 9b). A variant without the
  pressure-gradient term (their "EM") fails to reproduce the wake, which
  the full model captures by lowering the slip velocity near separation
  (Fig. 7). The sixth-order/iSVV run costs 15.04 h per $10^5$ steps on 96
  cores against 18.16 h for the second-order/Smagorinsky run, because the
  subgrid terms are not computed explicitly (§III A).

**A Mach-3 cylinder with immersed-boundary wall models.**
[Akbarzadeh & Borazjani (2025)](/sources/akbarzadeh-2025.md), §3.3, run
supersonic flow past a cylinder with their sharp-interface curvilinear
immersed boundary method, a hybrid of fourth-order skew-symmetric central
and third-order WENO fluxes, and the dynamic
[Smagorinsky model](/methods/smagorinsky-model.md) (see
[WENO schemes](/methods/weno-scheme.md)):

- *Small channel* ($8\times4$, after Guermond et al., inviscid reference,
  impulsive start): on the fine grid ($h=0.0025$, page-local: uniform grid
  size) the hybrid scheme and the LES capture the Kelvin–Helmholtz
  instability of the two contact lines leaving the triple points of the
  bow shock, which pure third-order WENO and the hybrid on the coarse grid
  ($h=0.01$) damp; the drag coefficient peaks near 2.25 at impingement and
  settles near 1.1 in the periodic state for all schemes (Figs. 6–9).
- *Wide channel* (experiment of Awasthi et al., $Re=750{,}000$): the bow
  shock stands off about $0.35D$, against 0.324 from Billig's correlation,
  which the authors state under-predicts measurements at Mach 2.7 to 4;
  the reattachment distance of the wake from the cylinder centre is 1.04
  in the experiment, 2.8 with a log-law wall model and similar with the
  integrated stress-balance ("Cabot") model, and 1.1 with a free-slip
  cylinder wall; the subgrid model (dynamic, constant, none) does not
  change it, and three-dimensional runs give reattachment lengths like the
  two-dimensional ones (Figs. 10–13).

The authors conclude that this flow is "more sensitive to the wall model
than the LES subgrid model" (§5); see
[wall-modelled LES](/methods/wall-modelled-les.md) and
[equilibrium wall model](/methods/equilibrium-wall-model.md). Their slip
condition is a zero-shear wall, not the Robin-type condition of
[slip-wall models](/methods/slip-wall-model.md).

**Flow control.** The review of [Fang et al. (2026)](/sources/fang-2026.md),
§3.4, Table 4, lists multi-agent reinforcement learning with ten pairs of
synthetic jets on a three-dimensional cylinder (at $Re_D=3900$ by the cited
title) giving 9% drag reduction, as a cited work; see
[reinforcement-learning closures](/methods/reinforcement-learning-closure.md).

**What the sources share.** In both scale-resolving studies at
$Re_D=3900$ the recirculation length is the measure most sensitive to the
model and the resolution: the SGS model and grid in
[Kim et al. (2024)](/sources/kim-2024.md), the PANS parameter $f_k$ and
the order of the scheme in [Dzanic et al. (2022)](/sources/dzanic-2022.md).
Both use the same three profile stations, $x/D=1.06$, 1.54 and 2.02, and
both lean on Parnaudeau et al. for reference data.

## Qualifications

- [Kim et al. (2024)](/sources/kim-2024.md) call the data of Parnaudeau et
  al. an experiment (Fig. 2); [Dzanic et al. (2022)](/sources/dzanic-2022.md)
  call them an LES. Both cite the same work, whose printed title
  ("Experimental and numerical studies of the flow over a circular cylinder
  at Reynolds number 3900") names both kinds of study.
- In [Dzanic et al. (2022)](/sources/dzanic-2022.md) the reference data
  disagree among themselves: low-order PANS at $f_k=0.1$ agrees with the
  LES of Parnaudeau et al. and at $f_k=0.3$ with the DNS (§3.2), so the
  "optimal" $f_k$ depends on the reference preferred. They print the time
  as "$t=D/U_\infty=100$" for $tU_\infty/D=100$.
- The second-order central scheme of [Kim et al. (2024)](/sources/kim-2024.md)
  is described as having no numerical dissipation (§2.1); it produces
  spurious oscillations near the front of the cylinder, which a hybrid
  QUICK/central scheme for $x/D<-0.25$ removes without changing the wake
  (§4.2.1). The dynamic Smagorinsky coefficient is averaged only in the
  spanwise direction. Their robustness test perturbs the inputs with noise
  whose standard deviation equals that of the training data (§4.1).
- The grids of $Re_D=5000$ and 10,000 are marginal for second-order
  statistics by the authors' own grid study (App. C).
- The cylinder of [Fanizza et al. (2025)](/sources/fanizza-2025.md) at
  $Re_D=80$ is laminar and unsteady; it validates the assimilation method,
  not a turbulence model. Their DG space is the total-degree modal space
  ($(N+1)(N+2)/2$ modes per element in 2D), although §2.3 calls it a
  tensor-product space.
- The cylinder of [Cheylan et al. (2023)](/sources/cheylan-2023.md) at
  $Re_D=100$ is laminar; it tests immersed-boundary numerics, not a
  turbulence model.
- The cylinder of [D'Ayer et al. (2026)](/sources/dayer-2026.md) at
  $Re_D=40$ is steady and laminar; like that of Cheylan et al. it tests
  immersed-boundary numerics. Its Table 2 prints identical values for Kou
  et al. and Choi et al.; the paper does not say whether the second set is
  taken from the first. §3.1 calls the separation angle $\theta$, Table 2
  $\alpha$.
- [Wang et al. (2021)](/sources/wang-2021-l.md) state that the pressure
  fluctuation magnitude is "captured well by both DDES within 1.8% error
  margin" (§3.2): both methods are IDDES, and the RSM-IDDES level at A,
  114.3 dB against 116.5 dB, differs by 1.89% *(compiler check, not in the
  sources)*. The text compares the shedding frequency with "experimental
  data (180 Hz)", while Table 1 gives 179 Hz at A and 180 Hz at B.
- The cylinders of [Liu et al. (2022b)](/sources/liu-2022-g.md)
  ($Re_D=100$, 106) and [Monfaredi et al. (2021)](/sources/monfaredi-2021.md)
  ($Re=1000$, reference length not stated) are
  2D and laminar. Liu et al. print the implicit-time-stepping drag of
  their 3360-element case as "$C_d$ is 0.159" and call it in agreement
  with the explicit runs, whose Table 2 values are 1.58–1.66 (§3.1.2).
- The 2D URANS values of [Ghidoni et al. (2022)](/sources/ghidoni-2022.md)
  at $Re_D=3900$ ($C_D=1.52$–1.62) are far from the 3D scale-resolving
  values above ($C_D=1.00$ for the DNS of Kim et al.); the authors present
  them as a test of time integration, not of the closure. Their §6.1 text
  prints, for the compressible run, an RMS lift of 1.19 and $St=0.225$,
  while Table 9 gives 1.13 and 0.23. Their single-cylinder
  $Re_D=1.4\times10^5$ and tandem $Re_D=1.66\times10^5$ cases sit in the
  same range as the tandem configuration of Wang et al. (2021). For the
  same tandem spacing $3.7D$ the Reynolds number is printed
  $1.66\times10^5$ by Ghidoni et al. (§6.3) and $1.6\times10^5$ by
  [Wang et al. (2021)](/sources/wang-2021-l.md) (§3.2); neither comments on
  the other's value.
- [Ma et al. (2022)](/sources/ma-2022.md) and
  [Kang & Masud (2022)](/sources/kang-2022.md) both print the cylinder
  results only as figures; neither gives a wall resolution in wall units,
  and Ma et al. give neither the Mach number nor the averaging time.
- The tandem cylinders at $Re_D=1.6\times10^5$ lie far above the
  three-dimensional single cylinders of the other sources ($Re_D\le10^4$;
  only the 2D URANS cylinder of Ghidoni et al. (2022) reaches
  $1.4\times10^5$), and the downstream
  cylinder sits in the wake of the upstream one: Wang et al. place the
  peaks of its RMS pressure at the vortex-impingement angles (Fig. 5).

- [Mays et al. (2023)](/sources/mays-2023.md) print the recirculation
  length in "(m)" for a non-dimensional set-up ($D=1$), the fourth Reynolds
  number as $7.8\times10^5$ in Table 6 and as $7.2\times10^5$ everywhere
  else, and a first-cell thickness $\Delta r_1/D=1.0\times10^{-6}$ for grid
  D against $3.0$, $2.0$ and $1.5\times10^{-5}$ for grids A–C (Table 1).
  §3.1 calls the time step of grid A "half that of Grid C's", while Table 1
  gives $\Delta tU_\infty/D=1.0\times10^{-3}$ for A and $7.5\times10^{-4}$
  for C, so A's step is 1.33 times C's *(compiler check, not in the
  sources)*. The reference LES has $C_L=-0.903$ at $Re_D=2.5\times10^5$
  against $+0.822$ and $+0.857$ for SRH (Table 4); the text speaks of "a
  positive value for the lift coefficient" and does not discuss the sign
  difference. The model is
  credited to Manceau (2018) in the abstract and to Duffal et al. (2019) in
  §1 and §2.1.2.
- The drag-crisis cylinders ($Re_D=2.5$–$7.2\times10^5$) lie above all
  other cylinders of this page, including the tandem configuration
  ($1.6\times10^5$). Mays et al. describe this regime as one in which
  transition occurs in the boundary layer just after laminar separation
  and the flow reattaches (§1); their $L_r$ (0.559–0.727 in the reference
  LES, Table 5) is recorded beside the $Re_D=3900$ values above, not
  compared with them.
- [Wang et al. (2024d)](/sources/wang-2024-k.md) first list wall-modelled
  runs at $10^5$, $5\times10^5$ and $10^6$, then "five Reynolds numbers"
  adding $6\times10^5$ and $8\times10^5$ (§III D); they print no averaging
  time. [Yan et al. (2024)](/sources/yan-2024.md) define $St=f_sD/U$ in
  Table II and call the transverse velocity "spanwise" in the captions of
  Figs. 5–6; they do not print the averaging time, and they define $l_r$
  only as the "length of the recirculation bubble" (nomenclature), without
  the point from which it is measured.
- The Mach-3 cylinder of [Akbarzadeh & Borazjani (2025)](/sources/akbarzadeh-2025.md)
  is mostly two-dimensional (three nodes in span with symmetry) and
  partly inviscid; the wall-model conclusion is drawn from the
  reattachment length, with 3D runs for the log-law and free-slip walls
  (§3.3.2, Fig. 13). The authors do not print the near-wall resolution
  in wall units on the cylinder. They cite the stress-balance
  model to Wang & Moin and Kang et al. in §2.4 and call it the "Cabot wall
  model" in §3.3, stating that it reduces to the log law in equilibrium.
- The supercritical cylinder of [Wu et al. (2024)](/sources/wu-2024.md)
  at $Re_D=3\times10^6$ lies above the drag-crisis cylinders of Mays et al.;
  the statement of the previous item holds for the other sources. Its Table 3,
  titled "at $Re_D=3\times10^6$", lists the LES of Catalano et al. and the
  experiment of Shih et al. at $Re_D=1\times10^6$, and the authors call
  SATES-σ's $C_D=0.55$ in good agreement while those two print 0.31 and 0.24.
  The time step is printed $\Delta tD/U_\infty$ and the flow-through times
  as $tU_\infty/C$, with the chord $C$ of the airfoil case (§3.1b, §3.2).
  The authors note that, because SATES-σ runs close to LES mode, transition
  "may not be captured accurately if the computational grid resolution is
  insufficient" (§4).
- Two sources print different drag for the steady cylinder at $Re_D=40$:
  [D'Ayer et al. (2026)](/sources/dayer-2026.md), Table 2, give
  $C_D=1.52$–1.55 at $M=0.2$ in a domain reaching $30D$ upstream and to the
  sides and $50D$ downstream; [Bulgarini et al. (2025b)](/sources/bulgarini-2025-b.md),
  §4.3, give the reference $C_{D,\mathrm{ref}}=1.41764$ at $M=0.1$ with the
  far field at $20D$, and call the $M=0.1$ flow "incompressible". Neither
  source compares with the other.
- The rankings of refinement indicators differ between two adaptive DG
  studies. [Bulgarini et al. (2025b)](/sources/bulgarini-2025-b.md), §4.3,
  on this steady laminar cylinder with an isogeometric DG
  discretization, find the spectral-decay indicator (cited to Persson &
  Peraire) "the most effective overall" and the small-scale energy density
  over-refining. [Ims & Wang (2023)](/sources/ims-2023.md), §5, on the
  unsteady implicit LES of the T106c and T106a cascades with flux
  reconstruction, find the small-scale-energy and residual indicators
  converging fastest and the Persson–Peraire smoothness indicator lagging,
  no faster than random refinement on T106a (see
  [turbine cascade](/benchmarks/turbine-cascade.md)). Bulgarini et al.
  normalize the small-scale energy by the element size (their Eq. 40),
  Ims & Wang use a curvilinear Toosi–Larsson variant; Bulgarini et al. cite
  Ims & Wang (their ref. [19]) and do not discuss the difference.
- [Zou et al. (2025)](/sources/zou-2025-b.md) call their two-dimensional
  laminar runs at $Re_D=150$ "direct numerical simulations" and $M=0.085$
  an "incompressibility condition"; they print no base-mesh resolution or
  degree-of-freedom count and no cost for the adaptive refinement they
  credit with "substantial computational efficiency gains".
- [Monteiro et al. (2026)](/sources/monteiro-2026.md), §2.4.1, list an
  immersed-boundary cylinder at $Re_D=3900$ in the public test suite of
  RHEA-X but show no result for it.

# Citations

- [Kim et al. (2024)](/sources/kim-2024.md) — §1; §2.1–2.2; §3.1–3.3, Table 2, Fig. 5; §4.1, Figs. 6–7; §4.2.1–4.2.3, Tables 1, 3–4, Figs. 8–13; App. C, Table 5; App. E, Table 6.
- [Dzanic et al. (2022)](/sources/dzanic-2022.md) — §3.2, Table 2, Figs. 7–13; §4.
- [Cheylan et al. (2023)](/sources/cheylan-2023.md) — §3.1, Tables 2–3; §3.4, Table 13.
- [Sirignano & MacArt (2023)](/sources/sirignano-2023.md) — §6, Figs. 13–14.
- [Fanizza et al. (2025)](/sources/fanizza-2025.md) — §2.3; §4.1, Figs. 4–6.
- [Wang et al. (2021)](/sources/wang-2021-l.md) — §2.4; §3.2, Table 1, Figs. 3–6; §3.3.
- [D'Ayer et al. (2026)](/sources/dayer-2026.md) — submitted manuscript: §3.1, Eq. 26, Tables 1–2, Figs. 3–5.
- [Liu et al. (2022b)](/sources/liu-2022-g.md) — §2.3, Eq. (23) (zero-mass coupling); §3.1.2, Table 2 (vortex-induced vibration at $Re_D=100$); §3.2, Table 3 (energy sink at $Re_D=106$).
- [Monfaredi et al. (2021)](/sources/monfaredi-2021.md) — §1; §4.1, Figs. 4–5 (laminar cylinder, adjoint verification); §4.2 (rod wake Strouhal number).
- [Ma et al. (2022)](/sources/ma-2022.md) — §3.2, Figs. 7–9 (implicit LES at $Re_D=3900$ with WCNS-E and WCNS-T).
- [Kang & Masud (2022)](/sources/kang-2022.md) — §5.1, Table 3, Figs. 7–16 (VMIB with residual-based VMS LES at $Re_D=3900$).
- [Ghidoni et al. (2022)](/sources/ghidoni-2022.md) — §6.1, Table 9 ($Re_D=3900$); §6.2, Table 12 ($Re_D=1.4\times10^5$); §6.3 (tandem cylinders, $Re_D=1.66\times10^5$).
- [Mays et al. (2023)](/sources/mays-2023.md) — §1 (drag-crisis regimes, as cited); §2.1–2.2, Eqs. (1)–(15) (SRH model, lag elliptic-blending base, convection scheme); §3.1, Tables 1–3, Fig. 4 (grids, cost, resolved fraction); §3.2.1–3.2.2, Tables 4–6, Figs. 6–10 (forces, recirculation, Strouhal number, energy ratio); §4.
- [Wu et al. (2024)](/sources/wu-2024.md) — §2.2–§2.4 (SATES-σ, WCNS-E-4, MUSCL); §3.2, Table 3, Figs. 7–17 (supercritical cylinder at $Re_D=3\times10^6$); §4.
- [Wang et al. (2024d)](/sources/wang-2024-k.md) — §III D, Table II, Figs. 13–15; §IV.
- [Yan et al. (2024)](/sources/yan-2024.md) — §III A, Tables II–III, Figs. 3–9.
- [Akbarzadeh & Borazjani (2025)](/sources/akbarzadeh-2025.md) — §2.4; §3.3.1–3.3.2, Figs. 6–13; §5.
- [Fang et al. (2026)](/sources/fang-2026.md) — §3.4, Table 4 (cited control work, review).
- [Zou et al. (2025)](/sources/zou-2025-b.md) — §II D; §III B, Table II, Figs. 6–9; §III C, Table III, Figs. 10–17 (laminar, 2D).
- [Bulgarini et al. (2025b)](/sources/bulgarini-2025-b.md) — §4.2–4.3, Eqs. 39–45, Table 5, Figs. 9–10.
- [Tsoutsanis & Nogueira (2025)](/sources/tsoutsanis-2025.md) — §5.4, Figs. 26–29.
- [Monteiro et al. (2026)](/sources/monteiro-2026.md) — §2.4.1 (test-suite case named, no result).
