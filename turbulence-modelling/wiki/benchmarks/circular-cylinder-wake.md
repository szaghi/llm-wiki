---
type: Benchmark
title: "Circular-cylinder wake"
description: "Flow past circular cylinders, chiefly at Re_D=3900, with separation, shear-layer roll-up and a turbulent wake: it tests neural-network SGS models, high-order PANS and immersed-boundary numerics; tandem cylinders at Re_D=1.6e5 test a Reynolds-stress-based IDDES, and laminar cylinders at Re_D 40 to 100 validate immersed boundaries and data assimilation."
status: established
aliases: [cylinder wake, flow over a circular cylinder, flow past a circular cylinder, cylinder at Re_D=3900, tandem cylinders, tandem cylinder benchmark]
tags: [benchmark, separated-flow, les, neural-network, pans, immersed-boundary, field-inversion, des, aeroacoustics]
timestamp: 2026-10-26T20:47:00Z
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
mean recirculation length $L_r$ (page-local: distance from the base point
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
experimental $L_r=1.40$ and $C_D=1.02$ of Norberg as they recall it
(Table 1). At $Re_D=10{,}000$ the reference is the experiment of Dong et al.
as recalled by Kim et al.: $L_r=0.82$, $C_{pb}=-1.13$, $U_{\min}=-0.25$,
$C_D=1.14$ (§4.2.3). As recalled by Kim et al., citing Williamson, in this
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

T-SR-nFU is thus worse than no model on the training grid (§4.2.1). $-C_{pb}$ on the training grid is 0.90, 0.88, 0.88
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
  at Reynolds number 3900") covers both kinds of data, so the two labels
  can name different parts of it; this is recorded as a qualification, not
  a contradiction.
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
- The tandem cylinders at $Re_D=1.6\times10^5$ lie far above the single
  cylinders of the other sources ($Re_D\le10^4$), and the downstream
  cylinder sits in the wake of the upstream one, so its pressure loads are
  set by vortex impingement rather than by its own separation.

# Citations

- [Kim et al. (2024)](/sources/kim-2024.md) — §1; §2.1–2.2; §3.1–3.3, Table 2, Fig. 5; §4.1, Figs. 6–7; §4.2.1–4.2.3, Tables 1, 3–4, Figs. 8–13; App. C, Table 5; App. E, Table 6.
- [Dzanic et al. (2022)](/sources/dzanic-2022.md) — §3.2, Table 2, Figs. 7–13; §4.
- [Cheylan et al. (2023)](/sources/cheylan-2023.md) — §3.1, Tables 2–3; §3.4, Table 13.
- [Sirignano & MacArt (2023)](/sources/sirignano-2023.md) — §6, Figs. 13–14.
- [Fanizza et al. (2025)](/sources/fanizza-2025.md) — §2.3; §4.1, Figs. 4–6.
- [Wang et al. (2021)](/sources/wang-2021-l.md) — §2.4; §3.2, Table 1, Figs. 3–6; §3.3.
- [D'Ayer et al. (2026)](/sources/dayer-2026.md) — submitted manuscript: §3.1, Eq. 26, Tables 1–2, Figs. 3–5.
