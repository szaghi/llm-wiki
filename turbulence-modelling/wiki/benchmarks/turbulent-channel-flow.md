---
type: Benchmark
title: "Turbulent channel flow"
description: "Pressure-driven flow between two parallel walls, periodic in the wall-parallel directions: here DNS at Re_τ 100 to 395 (gas-kinetic, GPU, real-gas), wall-resolved and implicit LES at 180 to 2000 (learned subgrid models, grid adaptation), a priori data at 395 to 2000, wall-modelled LES at Re_τ 1000 to 10¹⁰, hybrid RANS/LES to 20,000, and compressible channels to bulk Mach 4."
status: established
aliases: [plane channel flow, channel flow, half-channel flow, compressible channel flow]
tags: [benchmark, wall-model, wmles, hybrid-rans-les, boundary-layer, dns]
timestamp: 2026-10-26T07:40:00Z
---

# Turbulent channel flow

Plane channel flow is the flow between two parallel walls a distance $2\delta$
apart, driven by a mean pressure gradient (or an equivalent body force) and
periodic in the streamwise ($x$) and spanwise ($z$) directions; $y$ is
wall-normal. It is statistically stationary and homogeneous in $x$, $z$ and
time, so the mean velocity $\langle u\rangle(y)$ and the Reynolds stresses
$R_{ij}(y)$ converge from plane and time averages, and DNS exists up to high
friction Reynolds number $Re_\tau=u_\tau\delta/\nu_w$. The **half-channel**
variant simulates $0\le y\le\delta$ with a symmetry condition at $y=\delta$.
The compressible variant adds an energy source and isothermal walls, giving
wall heat flux. In this bundle the channel is the calibration and sanity
check for wall models, the first test of hybrid RANS/LES, the wall-bounded
a posteriori test of subgrid models, the validation case of new DNS
discretizations, and a source of a priori data for subgrid and RANS
closures.

## Configurations in the sources

| Source | Purpose | $Re_\tau$ | Domain ($x\times y\times z$) | Grid |
|---|---|---|---|---|
| [Flad & Gassner (2017)](/sources/flad-2017.md), §6.2, App. E | DG LES | 590 | $2\pi\times2\times\pi$ | $8^3$ elements, $N=7$; $\Delta x^+\approx58$, $\Delta z^+\approx29$, $\Delta y^+$ from 7 to 28 |
| [Agrawal et al. (2022)](/sources/agrawal-2022.md), §V, §VII.D | a priori SGS test; WMLES | 395, 2000 (a priori); 4200 (WMLES) | $2\pi\delta\times2\delta\times\pi\delta$ | $128\times40\times64$, uniform, $\Delta^+\approx200$ |
| [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md), §IV.B, App. B | WMLES error calibration | 4200 | not printed | isotropic Voronoi, $\Delta/\delta=1/3$ to $1/160$ |
| [Fowler et al. (2022)](/sources/fowler-2022.md), §5 | WMLES of a new wall model | $10^3$ to $5\times10^5$ | $8\pi\times2\times3\pi$ (units $\delta$) | $128\times30\times48$; $\Delta x^+=\Delta z^+=196$, $\Delta y^+=67$ at $Re_\tau=1000$ |
| [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md), §II–III | half-channel WMLES of learned wall models | 180 to $10^{10}$ (eleven values) | $2\pi\delta\times\delta\times2\pi\delta$ | $24^3$, $32^3$, $48^3$, $72^3$ |
| [Haering et al. (2022)](/sources/haering-2022.md), §III B, §V A | a priori filtering; hybrid RANS/LES | 1000 (a priori); about 5200; 20,000 | $8\pi\delta\times2\delta\times3\pi\delta$ | $N_y=110$; $\Delta x^+$ from 701 to 1552 |
| [Griffin et al. (2023)](/sources/griffin-2023.md), §4 | compressible WMLES | 319 to 1842 | $\pi\delta\times2\delta\times(\pi\sqrt3/4)\delta$ | 12 points per half-height (9 to 48 in grid studies) |
| [Cao et al. (2022)](/sources/cao-2022.md), §3.3, Tables 5–7 | DNS with a gas-kinetic scheme | 180 (176.0 and 179.2 obtained) | $2\pi\delta\times2\delta\times\pi\delta$ | $96^3$ and $128^3$, tanh-stretched in $y$; $\Delta x^+=11.77$, 8.83; $\Delta z^+=5.89$, 4.42; $\Delta y^+_{\min}=0.29$, 0.21 |
| [Prakash et al. (2022)](/sources/prakash-2022.md), §III.B.3, Tables 3–4 | wall-resolved LES of structural SGS models | 590 | $2\pi\delta\times2\delta\times\pi\delta$ | trilinear finite elements, $48\times111\times48$ ($\Delta x^+=78$, $\Delta z^+=39$) and $64\times133\times64$ ($\Delta x^+=58$, $\Delta z^+=29$), first point at $\Delta y^+=1$ |
| [Gillyns et al. (2022)](/sources/gillyns-2022.md), §§5–9 | spectral-element WMLES | 1000, 5200 | $2\pi\delta\times2\delta\times\pi\delta$ | $N=7$; $22\times16$ elements in $x$, $z$ ($0.286\delta$, $0.196\delta$ per element) with 4 to 6 elements per half-height at 1000; 20 and 10 elements per half-height at 5200 |
| [Bae & Koumoutsakos (2022)](/sources/bae-2022.md), Methods, Table 1 | in-solver training and testing of RL wall models | 2000, 4200, 8000 (training); 5200 to $10^6$ (testing) | $2\pi\delta\times2\delta\times\pi\delta$ | $\Delta x=\Delta z=0.05\delta$; $\Delta y=0.05\delta$, refined to $0.025\delta$ and $0.01\delta$ in two test cases |
| [Kim et al. (2022)](/sources/kim-2022.md), Tables I–III | in-solver training of a reinforcement-learning SGS model | 180, 360 (training); 720 (testing) | $4\pi\times2\times2\pi$, $2\pi\times2\times\pi$, $\pi\times2\times0.5\pi$ (units $\delta$) | LES $32\times49\times32$ ($\Delta x^+=70.7$, $\Delta z^+=35.3$) and $24\times49\times24$ (94.2, 47.1) at 180; $32\times65\times32$ at 360; $32\times97\times32$ at 720 |
| [Blind et al. (2023)](/sources/blind-2023.md), §3, Tables 1–4 | residual-based grid adaptation of DG LES | 550, 2000 (wall-resolved); 2000 (wall-modelled) | $10\delta\times2\delta\times3\delta$ | DGSEM $N=5$, from $10\times2\times3$ elements to 16,200 elements ($3.5\times10^6$ DOF) at 550 and 142,662 elements ($3.1\times10^7$ DOF) with 2-to-1 mortars at 2000 |
| [Carlsson et al. (2023)](/sources/carlsson-2023.md), §4.3, Table 2 | SST-IDDES with low-dissipation schemes | 395, 2400, 18,000 (bulk Mach 0.15); 500, 1015, 5000 (bulk Mach 1.5) | $2\pi\delta\times2\delta\times\pi\delta$ | $64\times N_y\times64$ with $N_y$ from 75 to 132, first point at $y^+\approx0.5$, stretching 1.14; $\Delta x^+$ from 40 to 1795; one $128\times118\times128$ grid at 1015 |
| [Zhao et al. (2023a)](/sources/zhao-2023.md), §5.2, Tables 6–9 | implicit LES with a gas-kinetic scheme | 180, 395 (Mach 0.1) | $2\pi\times2\times\pi$ (units $\delta$) | $64\times96\times64$ ($\Delta x^+=17.66$, $\Delta y^+_{\min}=0.29$); $96^3$ ($\Delta x^+=25.84$, $\Delta z^+=12.92$, $\Delta y^+_{\min}=0.58$) |
| [Wang et al. (2023b)](/sources/wang-2023-b.md), §4.2, Tables 6–7 | GPU DNS, single against double precision | 395 (Mach 0.1); bulk $Re=3000$ at bulk Mach 0.8, isothermal walls | $2\pi\times2\times\pi$ (units $\delta$) | $256\times128\times128$ and $256\times256\times128$ ($\Delta x^+=\Delta z^+=9.69$); $128^3$ and $128\times256\times128$ ($\Delta x^+=8.76$, $\Delta z^+=4.38$) |
| [Lederer et al. (2023)](/sources/lederer-2023.md), §4, Table 1 | under-resolved LES with a divergence-free mixed finite-element method | 392.24 | $2\pi\times2\times\pi$ | $6^3$, $12^3$, $16^3$ hexahedra at $N=3$ and $4^3$, $6^3$, $8^3$ at $N=6$ (43.2 to 775.7 thousand DOF); first-element height per point $\Delta y^+=3.0$ to 13.6 |
| [Kang et al. (2023)](/sources/kang-2023.md), §3.5, Tables 8, 10 | a priori and a posteriori test of a neural-network SGS model | 180 (training), 395 (testing) | $4\pi\delta\times2\delta\times\tfrac43\pi\delta$ at 180; $2\pi\delta\times2\delta\times\pi\delta$ at 395 | DNS $192^3$; LES $48^3$ ($\Delta x^+=47.2$, $\Delta z^+=15.7$ at 180), $32\times48\times32$, $64^3$ |
| [Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md), §III A, App. B–C | a priori budget of the anisotropic SGS stress | 400 | $2\pi h\times2h\times\pi h$ | DNS $256\times192\times256$; filters and LES at $(\Delta x^+,\Delta z^+)=(26.2,13.1)$, $(52.4,26.2)$, $(105,52.4)$ |
| [Bernades et al. (2023)](/sources/bernades-2023.md), §4.3 | DNS of a transcritical (real-gas) channel | 100 at the cold wall | $4\pi\delta\times2\delta\times\tfrac43\pi\delta$ | $128^3$; $\Delta x^+=9.8$, $\Delta z^+=3.3$, first point $y^+=0.1$ |

Reference DNS named by the sources: Kim, Moin & Moser at $Re_\tau=180$
(Cao et al.); Moser, Kim & Mansour at $Re_\tau=590$ (Flad & Gassner;
Prakash et al.); Lozano-Durán & Jiménez at 2000 and 4200 (Agrawal et al.;
Lozano-Durán et al.); Lee & Moser at 1000 and 5200 (Haering et al.; Fowler
et al.; Vadrot et al.; Gillyns et al.); the Johns Hopkins database at 1000
(Fowler et al.; Vadrot et al.); Trettel & Larsson for the compressible
channels (Griffin et al.). The flow is driven at constant mass flow
(Cao et al.; Prakash et al., at bulk Reynolds number
$Re_b=\langle u\rangle_b\delta/\nu=10{,}975$; Gillyns et al.; Carlsson et al.)
or at constant pressure gradient (Bae & Koumoutsakos), said per source.
Further references: Lee & Moser for the grid-adaptation runs (Blind et al.);
Moser, Kim & Mansour at 395 and Modesti & Pirozzoli for the supersonic
channels at 500 and 1015 (Carlsson et al.); the authors' own DNS at 180, 360
and 720, filtered in the homogeneous directions with a cut-off filter
(Kim et al.).

## What the case tests

**Mean-velocity error of wall-modelled LES.** All the
[wall-modelled LES](/methods/wall-modelled-les.md) studies use the channel as
the case where the [law of the wall](/definitions/law-of-the-wall.md) holds
and any error is attributable to the LES or the wall model.
[Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md), §IV.B, Fig. 7b,
calibrate the mean-velocity error of WMLES with the
[equilibrium wall model](/methods/equilibrium-wall-model.md) and dynamic
Smagorinsky at $Re_\tau=4200$ as $e_u\approx0.08\,\Delta/\delta$ (registry
$e_q$; their $\varepsilon_u$),
with $\Delta$ the isotropic cell size of their Voronoi grids (linear convergence, the same trend for a staggered finite-difference
solver), and bound it by about 15%, the difference between DNS and an
inviscid solution. Their App. B, Figs. 23–24, documents non-monotonic
convergence for $\Delta/\delta\approx0.03$–$0.05$, which they relate to the
grid's ability to support near-wall streaks; they "still lack a satisfactory
explanation". [Agrawal et al. (2022)](/sources/agrawal-2022.md), §VII.D,
Figs. 8–10, match the wall model at the second off-wall point at
$Re_\tau=4200$ and find that their tensor-coefficient model reduces the error
of the apparent von Kármán constant against the DNS value $\kappa=0.38$ from
7% (dynamic Smagorinsky) to 5%, lowers near-wall intensities, and needs no
clipping where dynamic Smagorinsky does.
[Fowler et al. (2022)](/sources/fowler-2022.md), §5.1, find their
[LaRTE wall model](/methods/lagrangian-relaxation-towards-equilibrium-wall-model.md)
"nearly indistinguishable" from the equilibrium model in mean statistics
from $Re_\tau=10^3$ to $5\times10^5$ on one fixed grid, with a slight
log-layer undershoot at $10^3$; they attribute WMLES-to-DNS differences in
the near-wall stresses to grid and SGS model, because two wall models agree.
[Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) use eleven Reynolds
numbers to test whether [machine-learning wall models](/methods/machine-learning-wall-model.md)
extrapolate: one reproduces the mean at all $Re_\tau$, one fits a log law
with $\kappa=0.32$, and a reinforcement-learning model gives a
[log-layer mismatch](/definitions/log-layer-mismatch.md) of $+2.2$ to
$-3.2$ in wall units across the range (Table III). They advocate the
channel as a sanity check every learned closure should pass (§V).

**Wall models in a high-order spectral-element code.**
[Gillyns et al. (2022)](/sources/gillyns-2022.md) implement an algebraic
equilibrium wall model (Reichardt's law with $\kappa=0.38$ and intercept
4.1, inverted for $u_\tau$) in a continuous spectral-element code with
polynomial degree $N=7$ and an approximate-deconvolution SGS model. The model
samples the velocity at the top node of the wall-adjacent element and
time-filters it; without filtering the run diverges (§5). At
$Re_\tau=1000$, moving the top of the first element from $y^+=63$ to 153
changes the normalized RMS error of the mean velocity from 0.52% to 1.09%
and that of the wall-stress ratio $u_\tau/\langle u\rangle_b$ from 0.37% to
0.87% (Table 1). The mean velocity matches DNS inside the under-resolved
first element down to $y^+\approx10$, which the authors attribute to the
spectral-element discretization without a same-mesh comparison (§7). With
the first element at $0.15\delta$, 5 elements per half-height are judged
acceptable and 4 under-resolved, because the element-interface (Gibbs)
spikes in the velocity fluctuations grow (§8, Table 2). At $Re_\tau=5200$
with 20 and 10 elements per half-height (first element top at $y^+=260$ and
520), the mean-velocity error stays below 1% and the fluctuation errors reach
9% (§9, Table 3).

**Reinforcement-learning wall models trained inside the solver.**
[Bae & Koumoutsakos (2022)](/sources/bae-2022.md) train
[reinforcement-learning](/methods/reinforcement-learning-closure.md) wall
models inside WMLES of the channel at $Re_\tau\approx2000$, 4200 and 8000
(matching height drawn between $0.075\delta$ and $0.15\delta$; episodes of
$2\delta/u_\tau$ started from "a previously obtained WMLES flow field" plus
noise; the reward uses the true mean wall stress), with the anisotropic
minimum-dissipation SGS model. In the a posteriori tests from $Re_\tau=5200$
to $10^6$ (runs of $300\delta/u_\tau$), the velocity-based model works only
while the matching height stays in the trained range
$150<h_{\mathrm{wm}}^+<1200$ and recovers when the wall-normal grid is
refined; the log-law-based model keeps a friction error below 5% and mean
profiles aligned with the log law ($\kappa=0.41$, $B=5.2$) at every
$h_{\mathrm{wm}}^+$ (Table 1, Figs. 3–4). The equilibrium wall model gives a
wall stress perfectly correlated with the matched velocity, the log-law-based
model a maximum correlation of about 0.3, the value the authors quote from
DNS (Figs. 6–7). See [machine-learning wall models](/methods/machine-learning-wall-model.md).

**Wall-resolved LES of subgrid models.**
[Prakash et al. (2022)](/sources/prakash-2022.md), §III.B.3, Table 4, use
the channel at $Re_\tau=590$ as the wall-bounded test of the
[gradient model](/methods/gradient-model.md) with and without clipping of
its backscatter. Skin friction against DNS 0.0058 (coarse/medium mesh):
dynamic Smagorinsky 0.0047/0.0049; gradient model unclipped 0.0063/0.0063,
standard clipping 0.0047/0.0050, optimal clipping 0.0051/0.0053, dynamic
mixed 0.0053/0.0055. Optimal clipping also gives a much better mean velocity
and Reynolds shear stress than standard clipping, approaching the dynamic
mixed model, which is slightly better but needs test filtering and
homogeneous averaging. Because the a priori dissipation of the two clipping
methods is identical, the authors hypothesize that the gain comes from the
higher a priori correlation of the optimally clipped stress with the exact
one (see [scale-similarity and mixed models](/methods/scale-similarity-model.md),
[energy backscatter](/definitions/energy-backscatter.md)). The TKE peak of
the unclipped gradient model is significantly overpredicted on both meshes.

**Subgrid models trained on mean statistics.**
[Kim et al. (2022)](/sources/kim-2022.md) train a pointwise neural-network
SGS model by [reinforcement learning](/methods/reinforcement-learning-closure.md)
inside channel LES, rewarding only agreement with the filtered-DNS profiles
of the mean viscous stress and the mean resolved Reynolds shear stress. At
$Re_\tau=180$ on the $\Delta x^+=70.7$, $\Delta z^+=35.3$ grid the
tensor-output models reproduce the filtered-DNS mean velocity and Reynolds
shear stress almost exactly and improve the rms velocities, the mean SGS
shear stress and the spectra over the static [Vreman model](/methods/vreman-model.md)
($C_s=0.08$ in their notation), dynamic Smagorinsky and no-model LES; an
eddy-viscosity-output variant over-predicts the mean velocity in the buffer
and log layers, like dynamic Smagorinsky (§III C, Fig. 7). Training also
succeeds on the coarser grid and at $Re_\tau=360$. At untrained Reynolds
numbers (360 and 720 for the model trained at 180) the Reynolds shear stress
stays close to the filtered DNS while the buffer-layer slope of the mean
velocity is under-estimated; on an untrained coarser grid the model fails
(§III D, Figs. 12–13). A variant with backscatter clipped performs almost
the same (see [energy backscatter](/definitions/energy-backscatter.md)).

**Grid adaptation for DG LES.** [Blind et al. (2023)](/sources/blind-2023.md),
§3, use the channel to transfer a residual-based
[mesh-adaptation](/methods/mesh-adaptation.md) method to the DG
spectral-element code [FLEXI](/software/flexi.md) with the Vreman model. At
$Re_\tau=550$ (wall-resolved) the sequence of grids resembles the
finite-difference results of Toosi & Larsson and converges after four
iterations to a spacing of about $\Delta x^+\approx18$, $\Delta y^+\approx1$,
$\Delta z^+\approx8$ per degree of freedom at the wall, where the computed
$Re_\tau$ is 556.57; the mean velocity matches the Lee & Moser DNS on the
last grid and the Reynolds stresses one grid earlier (Table 1, Figs. 1–3).
The suggested wall-parallel spacings are larger in the viscous sublayer than
in the buffer layer, which the authors call correct. At $Re_\tau=2000$ with
2-to-1 mortar interfaces the procedure converges after five iterations
($Re_\tau=1967.37$), and the mortars save about 50% of the elements against a
structured mesh of the same near-wall spacing; the time step is unchanged,
so the saving is in processors (§3.2, Tables 2–3). In wall-modelled LES at
$Re_\tau=2000$ (Spalding's law, matching at $0.1\delta$, $h_{\mathrm{wm}}^+=200$,
Vreman constant raised to 0.11) the target spacing below
$h_{\mathrm{wm}}$ is clamped to its value at $h_{\mathrm{wm}}$; the mean
velocity agrees with DNS above $h_{\mathrm{wm}}$ after three iterations and
the stresses after four, with $\langle u'u'\rangle$ not exactly converged,
which the authors attribute to WMLES (§3.3, Figs. 10–11).

**Element-based LES.** [Flad & Gassner (2017)](/sources/flad-2017.md),
§6.2, Fig. 11, compare split-form DG LES with the dynamic Smagorinsky model
against no-model, de-aliased DG at $Re_\tau=590$; the split-form LES gives
better Reynolds-stress profiles, and both are called "acceptable".

**Validation of DNS discretizations.** [Cao et al. (2022)](/sources/cao-2022.md),
§3.3, run the first channel DNS with their
[high-order gas-kinetic scheme](/methods/high-order-gas-kinetic-scheme.md),
a finite-volume scheme, at $Re_\tau=180$ and Mach 0.1 on $96^3$ and $128^3$
stretched grids. The flow transitions from a perturbed laminar profile in
over $500\,\delta/U_c$ ($U_c$ the centreline velocity) and is averaged over
$350\,\delta/U_c$, after which the total-stress residual is below 2.6% and
1.2%. The skin friction is $7.58\times10^{-3}$ and $7.82\times10^{-3}$ on
the two grids, against $8.39\times10^{-3}$ from Dean's correlation (Table 6).
The mean velocity agrees reasonably with spectral DNS and with lattice
Boltzmann and discrete unified gas-kinetic results; the Reynolds shear
stress is closer to DNS than both near the wall, whereas the other two
methods are better for some rms profiles (Figs. 10–12). The authors still
judge their scheme better overall, and note it uses a coarser, stretched
grid where the lattice Boltzmann run needs $\Delta x^+\approx0.3$ everywhere
(§3.3). See [direct numerical simulation](/definitions/direct-numerical-simulation.md).

**Reconstruction order of an implicit-LES scheme.**
[Zhao et al. (2023a)](/sources/zhao-2023.md) (read in arXiv v1), §5.2,
run the channel with their
[high-order gas-kinetic scheme](/methods/high-order-gas-kinetic-scheme.md)
as [implicit LES](/definitions/implicit-les.md), at constant mass flux
from a perturbed Poiseuille profile (transition about $400\,\delta/U_c$,
averaging $200\,\delta/U_c$). The realized $Re_\tau$ measures the scheme's
dissipation (Tables 8–9):

| Reconstruction | $Re_\tau$ at nominal 180 | $Re_\tau$ at nominal 395 |
|---|---|---|
| DNS (Moser et al.) | 178.12 | 392.24 |
| 5th order, non-compact | 171.33 | 360.35 |
| 7th order normal, 5th tangential | 177.04 | 378.97 |
| 7th order in all directions | 178.44 | 380.45 |
| 5th order, compact | 176.27 | 377.05 |

The higher-order and compact reconstructions also bring the mean velocity,
rms profiles and Reynolds stress closer to DNS and keep more energy at high
wavenumbers in the spectra at $y^+=30$ and 180, all runs showing a
levelling-off near the cutoff that the authors attribute to the mesh
(§5.2.1–5.2.3, Figs. 8–15). The compact fifth-order scheme nearly matches
the seventh-order one at the cost of the fifth-order non-compact one (0.618
against 0.595 and 0.961 s per step, Table 7).

**Single against double precision on GPUs.**
[Wang et al. (2023b)](/sources/wang-2023-b.md) (read in arXiv v1), §4.2,
run the same family of gas-kinetic schemes on GPUs as DNS of the channel at
$Re_\tau=395$, Mach 0.1, against Moser, Kim & Mansour, and of a compressible
channel at bulk Reynolds number 3000 and bulk Mach 0.8 against the DNS of Fu
et al. Single precision halves the memory and runs 2.7 times faster on a
TITAN RTX and 1.7 times on a V100 (Table 8). Statistics averaged over
$200\,\delta/U_c$ agree between precisions, with a visible deviation of
the streamwise rms, while instantaneous rms profiles at $t=20$ and $200\,\delta/U_c$ after a common restart differ;
the authors attribute the difference to round-off of the same order as the
discretization error and conclude that single precision "may not be safe"
for DNS of time-evolving turbulence but may serve LES and RANS (Figs.
10–14).

**Exactly divergence-free high-order LES.**
[Lederer et al. (2023)](/sources/lederer-2023.md) (read in arXiv v1), §4,
compare no-model LES with upwind jump dissipation, a variational-multiscale
[WALE](/methods/wale-model.md) model and their adaptive
[high-order projection-based upwinding](/methods/high-order-projection-based-upwind-method.md)
at $Re_\tau=392.24$. The mixed method transmits the wall stress exactly, so
a constant body force drives the flow without a controller (§4). All
methods converge to DNS under refinement; the WALE model is close to no
model on the finer meshes and slightly worse on the coarsest ones. Relative
errors of the bulk Reynolds number at $N=3$ on $6^3$, $12^3$, $16^3$
elements are 13.4%, 3.1%, 1.1% without model, 16.3%, 4.7%, 2.7% with WALE
and 0.7%, 1.0%, 0.6% with the adaptive upwinding, which resolves the buffer
layer on the coarsest mesh; at $N=6$ the upwinding changes little (Table
2, Figs. 1, 4–6). The authors interpret the adaptive upwinding as "a wall
model approach for standard DG ILES" (§6).

**A neural-network mixed model in the channel.**
[Kang et al. (2023)](/sources/kang-2023.md), §3.5–3.7, train their
[neural-network SGS model](/methods/neural-network-sgs-model.md) on filtered
DNS of the channel at $Re_\tau=180$, normalizing the output by the
volume-averaged norm of the resolved stress $L_{ij}$, because the gradient
model used for isotropic turbulence has the wrong near-wall scaling. On the
trained $48^3$ grid the skin friction is 0.0092 against 0.0085 for the
filtered DNS, 0.0072 for dynamic Smagorinsky and 0.0103 without model
(Table 11); the mean velocity, rms fluctuations and Reynolds shear stress
improve over dynamic Smagorinsky, which over-predicts the mean velocity, and
the model stays better on untrained grids ($32\times48\times32$, $64^3$) and
at $Re_\tau=395$ (Figs. 25–27). A model trained only on isotropic
turbulence runs stably but under-predicts the mean velocity, which the
authors attribute to the vanishing mean off-diagonal SGS stress of the
isotropic training data; plane-wise normalization partly fixes it (§3.5–3.6).
They name the resolved-stress input as the main factor of generalization to
the channel (§3.7).

**The anisotropic part of the subgrid stress on coarse grids.**
[Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md) (read in arXiv v3)
filter their DNS at $Re_\tau=400$ with a sharp cut-off in $x$ and $z$ only
and split the exact SGS stress into an eddy-viscosity part that carries the
whole local energy transfer and an anisotropic remainder that carries none.
At the medium resolution $(\Delta x^+,\Delta z^+)=(52.4,26.2)$ the remainder
is negligible in the resolved energy budget; at the coarse resolution
$(105,52.4)$ its mean shear stress is comparable to the eddy-viscosity part,
it redistributes energy productively into the spanwise resolved stress near
the wall, comparably to the pressure–strain term below $y^+=100$, with a
spectral peak at $\lambda_z^+\approx130$ that the authors relate to the
streak spacing $\lambda_z^+\sim100$ (§III–IV). An a posteriori dynamic
Smagorinsky LES at the same resolutions predicts the DNS mean velocity on the
fine and medium grids and over-predicts it on the coarse one (App. C,
Table I). See [scale-similarity models](/methods/scale-similarity-model.md),
[gradient model](/methods/gradient-model.md) and
[energy backscatter](/definitions/energy-backscatter.md).

**A real-gas channel as a scheme test.**
[Bernades et al. (2023)](/sources/bernades-2023.md), §4.3, Figs. 8–10, run a
DNS of nitrogen at twice the critical pressure between isothermal walls at
$0.75$ and $1.5$ times the critical temperature ($Re_\tau=100$ at the cold
wall) with their pressure-equilibrium-preserving split scheme and with the
kinetic-energy-preserving scheme that conserves total energy: the two agree
to plotting accuracy in first- and second-order statistics, and the authors
state that in the channel physical viscosity mitigates the pressure
oscillations. See [pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)
and [kinetic-energy preservation](/properties/kinetic-energy-preservation.md).

**Wall models beyond the canonical channel.**
[Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) build their
[building-block-flow wall model](/methods/building-block-flow-wall-model.md)
on channel-type flows: laminar and turbulent channels, Poiseuille–Couette
flows under favourable and adverse pressure gradient up to separation, and
a channel at $Re_\tau=700$ to which a sudden spanwise pressure gradient 80
times the streamwise one is applied (§2.3). In the latter the learned model
keeps its own wall-stress error below 1% and predicts the drop of the
streamwise wall stress and the rotation of the wall stress, which the
equilibrium model misses by construction; in the adverse-gradient
Poiseuille–Couette flows the equilibrium model has the smaller total error
"for the wrong reasons", by error cancellation (§4.5–4.6, Figs. 11–13). A
pipe at $Re_\tau\approx40{,}000$, beyond the training range, gives total
errors of 4–12% for both models with non-monotonic grid convergence (§4.4,
Fig. 10).

**Grid convergence of the classical compressible wall model.**
[Griffin et al. (2023)](/sources/griffin-2023.md), §4, run nine compressible
channels at bulk Mach 0.7 to 4 and dimensionless wall heat flux $-B_q$ from
0.010 to 0.19 (Table 1) with 12 points per half-height and matching at
$0.3\delta$. Their [inverse-velocity-transformation wall model](/methods/inverse-velocity-transformation-wall-model.md)
keeps wall-stress and heat-flux errors small at all heat fluxes, while the
classical model's errors grow with $-B_q$. With fixed matching height and
9, 18, 36 points per half-height ($2.0\times10^4$ to $1.3\times10^6$ control
volumes against $6.4\times10^8$ for the DNS), the classical model's
log-intercept error persists under refinement (§4.1, Fig. 13). See
[compressible velocity transformations](/definitions/compressible-velocity-transformation.md).
As recalled by [Huang et al. (2022)](/sources/huang-2022.md), §4.1, and
[Cogo et al. (2022)](/sources/cogo-2022.md), §4, the Trettel–Larsson
transformation collapses isothermal cooled-wall channels (and pipes), while
both papers find a log-intercept scatter for it in cooled supersonic and
hypersonic boundary layers: the channel does not exhaust the test of a
compressible transformation (see
[turbulent boundary layers](/benchmarks/turbulent-boundary-layer.md)).

**Numerical dissipation in hybrid RANS/LES.**
[Carlsson et al. (2023)](/sources/carlsson-2023.md), §4.3, Figs. 4–6, run
SST-based improved delayed DES on wall-modelled-LES grids in an unstructured
second-order finite-volume code. With the artificial dissipation of RANS
practice, the mean velocity is correct in the RANS region but shows a
significant [log-layer mismatch](/definitions/log-layer-mismatch.md) at all
Reynolds numbers as soon as the model switches to LES; with the
[low-dissipation low-dispersion scheme](/methods/low-dissipation-low-dispersion-scheme.md)
the mean velocity and total stresses agree with DNS at $Re_\tau=395$ and
only a small mismatch remains at the RANS–LES interface ($y^+\approx200$ at
2400, $\approx2000$ at 18,000). In the supersonic channels (bulk Mach 1.5,
isothermal walls) the Trettel–Larsson-transformed profiles agree with DNS
at 500 and 1015 and with Reichardt's law, the dissipative reference scheme
over-estimates the velocity in the LES region, and the streamwise
normal-stress peak is under-predicted, improved on the grid refined in $x$
and $z$ (see [compressible velocity transformations](/definitions/compressible-velocity-transformation.md)).
The shock-capturing term of the scheme switches off by itself in the
low-speed channel.

**Hybrid RANS/LES and transition from RANS.**
[Haering et al. (2022)](/sources/haering-2022.md), §V A, run the
[active model split](/methods/active-model-split.md) method at
$Re_\tau\approx5200$ on four grids from $\Delta x^+\approx701$ to 1552
(84K to 408K times fewer cells than the DNS). The mean is nearly
grid-independent with no log-layer mismatch, and the computable unresolved fraction
$\beta_k=1-k_{\mathrm{res}}/k_{\mathrm{tot}}$ (page-local) falls to 0.4 at
the centreline on the fine grid. Started from
RANS, the hybrid state develops in time with a transient overshoot that heals
by eight flow-throughs, and in space (a $16\pi$-long channel with a RANS
inlet) without overshoot but slowly. At $Re_\tau=20{,}000$ the mean
departs from the log law for $y^+=200$–$2000$, which the authors attribute
to the RANS base model.

**A priori data for closures.** [Agrawal et al. (2022)](/sources/agrawal-2022.md),
§V, Figs. 1–2, filter channel DNS at $Re_\tau=395$ and 2000 (filter width
three grid spacings) and find higher stress-tensor correlations for their
tensor-coefficient model than for dynamic Smagorinsky, mostly near the wall,
and identical dissipation correlations. [Haering et al. (2022)](/sources/haering-2022.md),
§III B, Fig. 1, box-filter DNS at $Re_\tau=1000$ (excluding $y^+<300$) to
fit $\alpha_k=\beta_k^{1.7}$ between the modelled-energy fraction
$\alpha_k=k_{\mathrm{sgs}}/k_{\mathrm{tot}}$ (page-local) and $\beta_k$. [Fowler et al. (2022)](/sources/fowler-2022.md),
§2.3, Fig. 2, time-filter Johns Hopkins DNS at $Re_\tau=1000$ to show that
filtering at their relaxation time collapses near-wall profiles onto the law
of the wall.

**RANS calibration and identifiability.** As recalled by
[Duraisamy et al. (2019)](/sources/duraisamy-2019.md), §5.1, channel DNS
was the first data set used to assign Bayesian posterior distributions to
RANS model parameters (Oliver & Moser 2011; Cheung et al. 2011), and a
stochastic discrepancy model for the Reynolds stress was tested in channel
flow at several Reynolds numbers. [Duraisamy (2021)](/sources/duraisamy-2021.md),
§VII, Fig. 4, shows a channel case in which a model-consistent perturbation
of the anisotropy, inferred from mean-velocity data, reproduces the mean
velocity and shear stress but not the anisotropy (non-identifiability; no
Reynolds number given). See
[model-form uncertainty](/definitions/model-form-uncertainty.md) and
[field inversion and machine learning](/methods/field-inversion-machine-learning.md).

## Qualifications

- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) write $z$ for the
  wall-normal coordinate; the table above translates their half-channel to
  $y$ wall-normal.
- [Fowler et al. (2022)](/sources/fowler-2022.md) give the wall-model height
  as $h_{\mathrm{wm}}^+\approx34$ in the a priori test (§2.3) and
  $h_{\mathrm{wm}}^+=33$ for the $Re_\tau=1000$ LES (Table 1), with
  $h_{\mathrm{wm}}=\delta/30$ in both; at $Re_\tau=1000$ the value is
  $1000/30\approx33.3$ *(compiler check, not in the sources)*. Their own
  symbol for the wall-model height is $\Delta$.
- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) print the
  channel grids as $\Delta/\delta=1/3,1/5,1/10$ in §IV.C and as
  $1/3,1/6,1/10$ in the Fig. 8 caption.
- The sources differ on where the equilibrium wall model is matched: the
  second off-wall point on staggered grids
  ([Agrawal et al. (2022)](/sources/agrawal-2022.md)), the first off-wall
  cell centre without temporal filtering
  ([Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md)), half the
  first wall-normal cell ([Fowler et al. (2022)](/sources/fowler-2022.md)),
  $0.3\delta$ ([Griffin et al. (2023)](/sources/griffin-2023.md)), or the
  top node of the first spectral element, time-filtered over about five
  time steps ([Gillyns et al. (2022)](/sources/gillyns-2022.md)); this is a
  difference of practice, discussed on [log-layer mismatch](/definitions/log-layer-mismatch.md).
- The sources use different log-law constants as reference: $\kappa=0.40$,
  $B=5.5$ for the low-Reynolds-number channel
  ([Cao et al. (2022)](/sources/cao-2022.md), Eq. 8); $\kappa=0.41$, $B=5.2$
  ([Bae & Koumoutsakos (2022)](/sources/bae-2022.md)); $\kappa=0.38$ with
  intercept 4.1 in Reichardt's profile
  ([Gillyns et al. (2022)](/sources/gillyns-2022.md), who note 0.383 and
  4.25 as the more recent values); $\kappa=0.38$ as the DNS value
  ([Agrawal et al. (2022)](/sources/agrawal-2022.md)). These are reference
  choices, not competing measurements.
- [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) was read in its
  Research Square preprint (v1, June 2021); its numbers may differ from the
  published version. The text gives the 5% error of the log-law-based model
  as an error in the friction velocity, the Fig. 3 caption as an error in
  the wall stress. The text names only $Re_\tau=2\times10^4$ and
  $5\times10^4$ as the failures of the velocity-based model, while the
  $10^5$ and $10^6$ cases of Table 1 also lie outside the trained
  $h_{\mathrm{wm}}^+$ range and are omitted from Fig. 4.
  [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) report a
  Reynolds-number-dependent log-layer mismatch for the published log-law
  RL model and attribute the difference from Bae & Koumoutsakos's results
  mainly to grid resolution; the disagreement is classified on
  [machine-learning wall models](/methods/machine-learning-wall-model.md).
- [Prakash et al. (2022)](/sources/prakash-2022.md) print the flow-through
  time as $T=\langle u\rangle_b/L_x$, the inverse of a time; say "fine mesh"
  for the medium mesh; and write in consecutive sentences that the gradient
  model without clipping over- and underpredicts the Reynolds shear stress
  (§III.B.3); which variant the second sentence means is not said. They print $\Delta x^+=78$ for the coarse mesh;
  $2\pi\cdot590/48=77.2$ *(compiler check, not in the sources)*.
- [Gillyns et al. (2022)](/sources/gillyns-2022.md) print the wall-stress
  error of the same configuration (6 elements, first element at
  $0.15\delta$) as 0.87% in Table 1 and 0.88% in Table 2, and state "< 9%"
  for the fluctuation errors at $Re_\tau=5200$ where Table 3 prints 9.00%.
  They rate the 4-element mesh "not sufficiently resolved" in §8 and "a fair
  compromise" in §9.
- [Cao et al. (2022)](/sources/cao-2022.md) were read in the arXiv v1
  preprint; they print the wall shear stress as $\partial U/\partial y$ at
  the wall, without the viscosity.
- [Kim et al. (2022)](/sources/kim-2022.md) (read in arXiv v2) write the
  Vreman constant in a form with $2.5C_s^2$; the value 0.08 is theirs. The
  averaging time of their statistics is not quantified.
- [Blind et al. (2023)](/sources/blind-2023.md) were read in arXiv v1, under
  a title that differs from the published one. Their Table 4, captioned as
  the $Re_\tau=550$ wall-modelled channel, holds the $Re_\tau=2000$ case,
  whose computed $Re_\tau$ on the last grid is 1555.60, not discussed in the
  text. Their element counts, $N_y$ and $\Delta_y$ columns are not mutually
  consistent (two elements over the half-height or the full height).
- [Zhao et al. (2023a)](/sources/zhao-2023.md) print the viscosity of the
  $Re_\tau=180$ case as $2.83\times10^{-4}$, while their own log-law
  procedure (Eqs. 25–26, $\kappa=0.40$, $B=5.5$, $U_c=1$) gives
  $U_\tau=1/(2.5\ln180+5.5)=0.0541$ and $\mu=U_\tau/180=3.0\times10^{-4}$,
  as do the realized values of Table 8 (e.g. $0.0515/171.33$), and the same
  procedure reproduces the printed $1.24\times10^{-4}$ at $Re_\tau=395$; and $\Delta z^+=8.33$ where $\pi\cdot180/64=8.84$
  *(compiler check, not in the sources)*. Their seventh-order runs use 4
  Gauss points per face, with which their accuracy test gives about fourth
  order (§4).
- [Wang et al. (2023b)](/sources/wang-2023-b.md) say that two of their
  channel cases ran on one GPU and two on two GPUs, while Table 8 states two
  GPUs for all. They draw the "may not be safe" conclusion from the
  instantaneous rms profiles (Fig. 14), while the statistics averaged over
  $200\,\delta/U_c$ agree between precisions (Figs. 10–13).
- [Lederer et al. (2023)](/sources/lederer-2023.md) print the friction
  Reynolds number with the half-height and call their bulk-Reynolds-number
  error "only a rough error estimate"; their averaging time is not printed.
- [Kang et al. (2023)](/sources/kang-2023.md) give the $Re_\tau=395$ LES
  spacings ($\Delta x^+=52.0$ on $48^3$) slightly above $2\pi\cdot395/48=51.7$
  *(compiler check, not in the sources)*.
- [Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md) filter only in the
  wall-parallel directions; their "medium" and "coarse" resolutions are those
  of the filters, matched to the LES grids of App. C.
- [Morsbach et al. (2024)](/sources/morsbach-2024.md), §3.1, §3.3, run a
  channel of finite length with parallel end walls and synthetic inflow
  (83,790 elements, $N=5$) as a precursor that calibrates the inflow of a
  turbine cascade; it is a developing flow, not the periodic channel of this
  page (see [inflow turbulence generation](/methods/inflow-turbulence-generation.md)).
- [Carlsson et al. (2023)](/sources/carlsson-2023.md) show Reynolds stresses
  only at $Re_\tau=395$ and in the supersonic cases, although their
  conclusion calls the resolved stresses excellent at all three subsonic
  Reynolds numbers; the $Re_\tau=5000$ supersonic case has no DNS.

# Citations

- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §V, Figs. 1–2; §VII.D, Figs. 7–10.
- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) — §IV.B–C, Figs. 7–8; App. B, Figs. 23–24.
- [Fowler et al. (2022)](/sources/fowler-2022.md) — §2.3, Fig. 2; §5.1, Table 1, Figs. 4–10.
- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) — §II–IV, Table III, Figs. 5–15, App. A–B.
- [Haering et al. (2022)](/sources/haering-2022.md) — §III B, Fig. 1; §V A, Table I, Figs. 2–8.
- [Griffin et al. (2023)](/sources/griffin-2023.md) — §4, Table 1, Figs. 8–15.
- [Flad & Gassner (2017)](/sources/flad-2017.md) — §6.2, App. E, Fig. 11.
- [Duraisamy et al. (2019)](/sources/duraisamy-2019.md) — §5.1 (recalled calibration studies).
- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §VII, Fig. 4.
- [Cao et al. (2022)](/sources/cao-2022.md) — §3.3, Eq. (8), Tables 5–7, Figs. 7–12.
- [Prakash et al. (2022)](/sources/prakash-2022.md) — §III.B.3, Tables 3–4, Figs. 8–10; §IV.
- [Gillyns et al. (2022)](/sources/gillyns-2022.md) — §§3–9, Eqs. (3)–(7), Tables 1–3, Figs. 3–13.
- [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) — Results pp. 4–8, Table 1, Figs. 2–7; Methods pp. 12–14 (preprint v1).
- [Huang et al. (2022)](/sources/huang-2022.md) — §4.1 (recalled channel results).
- [Cogo et al. (2022)](/sources/cogo-2022.md) — §4 (recalled channel results).
- [Kim et al. (2022)](/sources/kim-2022.md) — §II A–F, Tables I–III; §III C–D, Figs. 7–13.
- [Blind et al. (2023)](/sources/blind-2023.md) — §3.1–3.3, Tables 1–4, Figs. 1–11 (arXiv v1).
- [Carlsson et al. (2023)](/sources/carlsson-2023.md) — §4.3, Table 2, Figs. 4–6; §5.
- [Zhao et al. (2023a)](/sources/zhao-2023.md) — §5.2, Tables 6–9, Figs. 8–17.
- [Wang et al. (2023b)](/sources/wang-2023-b.md) — §4.2, Tables 6–8, Figs. 9–14.
- [Lederer et al. (2023)](/sources/lederer-2023.md) — §4, §4.1, Tables 1–2, Figs. 1–6.
- [Kang et al. (2023)](/sources/kang-2023.md) — §3.5–3.7, Tables 8–13, Figs. 25–33.
- [Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md) — §III–IV; App. B–C, Table I, Figs. 16–17.
- [Bernades et al. (2023)](/sources/bernades-2023.md) — §4.3, Figs. 8–10; §5.
- [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) — §2.3; §4.4–4.6, Figs. 10–13.
- [Morsbach et al. (2024)](/sources/morsbach-2024.md) — §3.1, §3.3, Table 2.
