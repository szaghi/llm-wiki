---
type: Benchmark
title: "Homogeneous isotropic turbulence (decaying and forced)"
description: "Turbulence in a triply periodic box, decaying from a prescribed spectrum or sustained by forcing: a priori database and a posteriori test of subgrid closures, learned ones included (Re_λ 70 to 418, LES of 24³ to 144³ degrees of freedom), a dissipation test of schemes for hybrid RANS/LES, DNS up to supersonic turbulent Mach numbers, and driven MHD turbulence."
status: established
aliases: [HIT, DHIT, forced HIT, decaying isotropic turbulence, forced isotropic turbulence, periodic box turbulence, compressible isotropic turbulence, turbulent box simulation]
tags: [benchmark, les, sgs-model, data-driven, dns, compressible]
timestamp: 2026-10-26T07:40:00Z
---

# Homogeneous isotropic turbulence (decaying and forced)

Homogeneous isotropic turbulence (HIT) is computed in a periodic cube,
with no walls and no mean flow. In the **decaying**
variant a random field with a prescribed spectrum evolves freely and its
kinetic energy $K=\int E(k)\,dk$ and dissipation $\varepsilon$ decrease in
time. In the **forced** variant a body force $f_i$ injects energy at a rate
that keeps the flow statistically stationary. Because the flow is
homogeneous, the energy spectrum $E(k)$ and the time histories of $K$ and
$\varepsilon$ characterize the solution completely at the level the sources
compare. An LES is judged against a DNS filtered to the LES cutoff. The case
isolates the [subgrid-scale closure](/definitions/large-eddy-simulation.md)
and the [numerical dissipation](/properties/numerical-dissipation.md) of the
discretization from wall and inflow effects. (On this spectral page $k$ is
the wavenumber magnitude and $K$ the kinetic energy, as fixed in the
notation registry.)

## Set-ups in the sources

| Source | Variant | $Re_\lambda$ | Reference DNS | LES resolution | Initial field and forcing |
|---|---|---|---|---|---|
| [Flad & Gassner (2017)](/sources/flad-2017.md), §1, §3–5 | decaying | from about 162 to 97 over the run | pseudo-spectral, $512^3$, 2/3-rule de-aliasing | DG, $N=7$: $18^3$ elements ($144^3$ DOF) and $6^3$ elements ($48^3$ DOF) | filtered DNS field; maximum local Mach about 0.1 |
| [Agrawal et al. (2022)](/sources/agrawal-2022.md), §VII.A | decaying | 70 | $128^3$ | $32^3$ | Passot–Pouquet spectrum, $u_{\mathrm{rms}}=1$ |
| [Agrawal et al. (2022)](/sources/agrawal-2022.md), §VII.B–C | forced | 315; and $Re_\lambda\to\infty$ | filtered $1024^3$ DNS of Cardesa et al. | $128^3$ | linear momentum forcing at constant kinetic energy |
| [Beck & Kurz (2023)](/sources/beck-2023.md), §IV A | forced | about 180 | DG $N=7$, $64^3$ elements, 512 points per direction, run to $t=10$ (about 14 large-eddy turnovers) | DG, 24 or 36 DOF per direction, $N=3,5,8$ | Rogallo initialization, linear forcing applied at the nodes |
| [Vela-Martín (2022)](/sources/velamartin-2022.md), §5.1, Table 1 | forced | 140, 240, 324 | $256^3$, $512^3$, $1024^3$, with $k_{\max}\eta=1.5,1.5,2.0$; 290 independent fields | a priori only: filter scales $\ell/L$ from 0.65 to 0.08 | linear forcing |
| [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md), §5, App. G.2 | forced (3D) | not stated ($Re=2000$) | $1024^3$, single precision | $32^3$, $64^3$ | random field with spectrum peaked at wavenumber 20; Kolmogorov force $\sin(8\pi x_2)$ on $[0,1]^3$ |
| [Prakash et al. (2022)](/sources/prakash-2022.md), §III.A, §III.B.1 | forced | 418 (a priori); effectively infinite in the LES ($\nu=10^{-12}$) | Johns Hopkins forced isotropic database (a priori); $k^{-5/3}$ spectrum with Kolmogorov constant 1.6 (a posteriori) | a priori box filters $\Delta\approx6.5\eta$ to $68\eta$, anisotropic up to $15\eta\times292\eta\times292\eta$; LES on $32^3$, $64^3$, $128^3$ trilinear finite elements | spectral forcing of the modes $\lvert k_i\rvert<3$ at injected power 62.843 |
| [Cao et al. (2022)](/sources/cao-2022.md), §3.4, Table 8 | decaying, compressible | 72 (initial) | none: the DNS is offered as reference data | DNS only, $512^3$ cells, $k_{\max}\eta_0=3.61$ | spectrum $E(k)\propto k^4\exp(-2k^2/k_0^2)$, $k_0=8$; turbulent Mach number $M_t=0.8$, 1.0, 1.2, 1.6 |
| [Seta & Federrath (2022)](/sources/seta-2022.md), §2 | forced, MHD, two-phase (heating and cooling) | not given; $Re=Rm=2000$ at the driving scale | none | DNS only, $512^3$, 200 pc box | solenoidal or compressive driving at $1\le kL/2\pi\le3$ to $u_{\mathrm{rms}}\approx10$ km/s; seed field $10^{-10}$ G |
| [Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md), §III, §IV | forced (a priori); decaying (a posteriori) | 170, 240, 355 (a priori); 240 (a posteriori) | pseudo-spectral, $320^3$, $520^3$, $1024^3$; ten snapshots per $Re_\lambda$ | a priori box filters of dimensionless size 2 to 32; LES at sizes 4 and 20 from the $520^3$ DNS | decaying runs started from the filtered statistically stationary field; large-eddy turnover time about 2.7 |
| [Carlsson et al. (2023)](/sources/carlsson-2023.md), §4.2 | decaying (grid turbulence of Comte-Bellot & Corrsin) | not given; $U_0M_g/\nu=34{,}000$ on the grid mesh size $M_g$ | experiment, spectra at $tU_0/M_g=42$, 98, 171 | $32^3$, $64^3$, $128^3$ nodes, second-order finite volumes, SA- and SST-based LES | field built from the measured spectrum; turbulent Mach number 0.1 |
| [Gan et al. (2022)](/sources/gan-2022.md), §2 | forced, compressible isothermal MHD with a strong guide field | not given | none | ideal MHD, $512^3$ ($8\pi\times2\pi\times2\pi$ in one run), ATHENA++ | Ornstein–Uhlenbeck forcing at $0<\lvert\boldsymbol k\rvert\le2$, incompressible or compressible velocity driving; $v_A=8$, $\beta_p=0.4$, turbulent Mach number 0.12–0.18 |
| [Kurz et al. (2023)](/sources/kurz-2023.md), §3–4, Table 2 | forced | about 180 (training and tests); about 240 (generalization) | DNS spectrum and velocity PDF, resolution not stated | DG: $N=5$ on $4^3$, $6^3$, $8^3$ elements and $N=7$ on $4^3$ (24, 36, 48 and 32 DOF per direction) | Rogallo initialization, linear (Lundgren) forcing; Mach 0.1; large-eddy turnover time about 0.7 |
| [Kang et al. (2023)](/sources/kang-2023.md), §2, §3, App. A | forced (training, a posteriori); decaying (a posteriori) | 106 and 286 (training), 164 (validation) | pseudo-spectral, $192^3$, $512^3$ ($256^3$ at 164); 37 to 50 snapshots | pseudo-spectral LES, $24^3$, $48^3$, $96^3$ at 106; $128^3$ at 286 | set-ups of Mohan et al. (106) and Chumakov (286), forcing wavenumbers 2 and 1.5; decaying runs started from the converged filtered field |

The beck-2023 DNS used 16,384 cores of the HAWK system for almost two hours
(about 30,000 CPU hours). [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md)
run their main experiments in two dimensions: Kolmogorov-forced turbulence
at $Re=6000$ (DNS $4096^2$, LES $\bar n=32$ to 256 per direction) and a 2D
decaying case (App. G.1). These are periodic-box turbulence but neither
three-dimensional nor isotropic in the 3D sense, and the paper does not
state the reference velocity and length behind $Re$.

## What the case tests

**Dissipation by implicit and explicit closures.**
[Flad & Gassner (2017)](/sources/flad-2017.md) use decaying HIT to show that
no-model DG LES with Riemann-solver dissipation and polynomial de-aliasing
matches the DNS at $144^3$ DOF, where 43.2% of the dissipation is resolved
at their 3-points-per-wavelength cutoff $k_c=48$, but fails at $48^3$ DOF,
where 0.9% is resolved at $k_c=16$ (energy pile-up at mid-range wavenumbers,
then a sharp drop). From these two resolutions they infer that roughly 40%
of the dissipation must be resolved for this
[implicit LES](/definitions/implicit-les.md) practice to work. On the
kinetic-energy-preserving split form they show that a
[Smagorinsky model](/methods/smagorinsky-model.md) with $C_s=0.12$ (in the
squared form of their Eq. A.1) beats no-model DG LES at $48^3$ DOF (§4,
Fig. 7). [Beck & Kurz (2023)](/sources/beck-2023.md) find no single best
baseline across polynomial degrees: no-model LES is best at $N=3$,
Smagorinsky with $C_s=0.17$ over-damps high wavenumbers at $N=5$, and the
[dynamic procedure](/methods/dynamic-procedure.md) is close to DNS at 36 DOF
but deviates at 24 DOF; their
[reinforcement-learning closures](/methods/reinforcement-learning-closure.md)
reach or exceed the best baseline in all cases except no-model LES at $N=3$
(§V, Figs. 8–14).

**A reinforcement-learned Smagorinsky coefficient for implicitly filtered DG LES.**
[Kurz et al. (2023)](/sources/kurz-2023.md) (read in arXiv v2), from the
same group and on the same forced case at $Re_\lambda\approx180$ as
[Beck & Kurz (2023)](/sources/beck-2023.md), train with
[Relexi](/software/relexi.md) and [FLEXI](/software/flexi.md) a policy that
sets an element-wise Smagorinsky coefficient $C_s\in[0,0.5]$ from
element-local momentum alone, rewarded by the error of the instantaneous
spectrum against the time-averaged DNS spectrum up to a cutoff of 2.6 to 3
points per wavelength (§3.4–3.5, Table 2). A posteriori, from an unseen
initial state and over four times the training horizon, the policies are
stable; no-model LES piles up energy at high wavenumbers, static
Smagorinsky with $C_s=0.17$ over-dissipates near the resolution limit, the
dynamic Smagorinsky model matches the RL model except at 24 DOF, where the
RL model is "significantly better" and the authors suspect the test filter
lies outside the scale-similar range (§4.2, Fig. 6). The predicted $C_s$
shrinks with resolution (up to 0.5 at 24 DOF, at most 0.3 at 48 DOF); the
36- and 48-DOF policies transfer to each other's resolution and to
$Re_\lambda\approx240$ (§4.4–4.5, Figs. 8–9). Policies fed with the five
velocity-gradient invariants train slower and end worse (§4.3, Fig. 7). See
[reinforcement-learning closures](/methods/reinforcement-learning-closure.md)
and [discretization-consistent closure](/definitions/discretization-consistent-closure.md).

**A neural-network mixed model, a priori and a posteriori.**
[Kang et al. (2023)](/sources/kang-2023.md) train a two-layer, 12-neuron
[neural-network SGS model](/methods/neural-network-sgs-model.md) on
filtered DNS of forced HIT at $Re_\lambda=106$ and 286 (§2, Table 1). With
the resolved strain alone as input, the network predicts a stress almost
aligned with the strain (correlation of its $\tau_{12}$ with $\bar S_{12}$
of $-0.82$, against $-0.28$ for the filtered-DNS stress), no backscatter, and LES almost identical to
the dynamic Smagorinsky model (§3.1, Table 3, Figs. 4–6). Adding the
resolved stress $L_{ij}$ as input doubles the a priori stress correlation
(0.70–0.72 against 0.35–0.37), reproduces the PDF of the SGS dissipation
including backscatter, and runs stably with no averaging or clipping (§3.1,
Table 4, Fig. 8). Trained at one Reynolds number and resolution, with inputs
and output normalized by volume-averaged norms, it predicts decaying HIT at
$24^3$ to $128^3$ and $Re_\lambda=106$ and 286 better than dynamic
Smagorinsky (§3.2, Table 5, Figs. 13–17), and beats the algebraic dynamic
mixed models a posteriori although they correlate as well or better a priori
(§3.3, Table 6, Figs. 19–22), at 0.71 of the cost of the dynamic
Smagorinsky stress evaluation (§3.4). The algebraic dynamic models diverge
within tens of steps without averaging and clipping (Fig. 20). See
[energy backscatter](/definitions/energy-backscatter.md) and
[scale-similarity models](/methods/scale-similarity-model.md).

**Dissipation of a non-Boussinesq model.**
[Agrawal et al. (2022)](/sources/agrawal-2022.md) use decaying HIT to show
that the [dynamic tensor-coefficient Smagorinsky model](/methods/dynamic-tensor-coefficient-smagorinsky-model.md)
dissipates as well as the dynamic Smagorinsky model: both follow filtered DNS
in kinetic energy and dissipation after a transient of up to one eddy
turnover, with decay exponents $K\sim t^{-1.35}$ for both against
$t^{-1.37}$ for the box-filtered DNS (Figs. 3–4). In forced HIT at
$Re_\lambda=315$ both models recover the $k^{-5/3}$ range of the filtered
DNS spectrum (Fig. 5).

**Equipartition without dissipation.** Three sources agree that a
discretization without subgrid dissipation drives the resolved spectrum
towards energy equipartition, $E(k)\sim k^2$, near the cutoff:
[Agrawal et al. (2022)](/sources/agrawal-2022.md) for a no-model LES as
$Re_\lambda\to\infty$ (§VII.C, Fig. 6);
[Flad & Gassner (2017)](/sources/flad-2017.md) for the dissipation-free split-form
DG scheme at $48^3$ DOF, which stays stable (§3, Fig. 4); and, on the
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md),
[Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) for
truncated Euler and no-model runs (§6.2). This is the statement of the
benchmark that a stable, energy-conserving scheme must be supplemented by
dissipation, explicit or numerical. [Prakash et al. (2022)](/sources/prakash-2022.md),
§III.B.1, Fig. 4, find the same failure in forced HIT at effectively
infinite Reynolds number with a stabilized finite-element solver: the
no-model run (stabilization only) and the unclipped
[gradient model](/methods/gradient-model.md), whose a priori dissipation is
too low, both pile up energy at the highest resolved wavenumbers. Dynamic
Smagorinsky has no pile-up and follows the $k^{-5/3}$ slope but over-predicts
intermediate wavenumbers, as does the dynamic mixed model; the gradient model
with standard or optimal clipping of its backscatter gives the best spectra,
optimal clipping a slightly longer inertial range. The authors state, without
showing it, that the dissipation of the stabilization is much smaller than
the SGS dissipation of every explicit model.
[Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md), §IV, Fig. 8, find the
same pile-up in decaying HIT with a pseudo-spectral solver: the no-model run
on the LES grid accumulates energy at high wavenumbers, the Smagorinsky
model over-dissipates, and their dynamic
[fractional SGS model](/methods/fractional-sgs-model.md) lies between the two,
closest to the filtered DNS.

**A priori structure of structural models.**
[Prakash et al. (2022)](/sources/prakash-2022.md), §III.A, Figs. 1–3, box-filter
the Johns Hopkins forced database at $Re_\lambda=418$ to test the gradient
model. Unclipped, it is highly correlated with the exact SGS stress at all
filter widths but under-predicts the mean SGS dissipation. Standard clipping
(zeroing the stress where it backscatters) restores dissipation and lowers the
correlation, more under anisotropic book- and pencil-type filters; optimal
clipping (the nearest stress without local backscatter) keeps the unclipped
correlation and gives the same mean dissipation as standard clipping. See
[energy backscatter](/definitions/energy-backscatter.md) and
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md).

**Compressible decaying turbulence as a DNS test.**
[Cao et al. (2022)](/sources/cao-2022.md), §3.4, run decaying compressible
isotropic turbulence with their
[high-order gas-kinetic scheme](/methods/high-order-gas-kinetic-scheme.md)
at initial $Re_\lambda=72$ and turbulent Mach number $M_t=0.8$ to 1.6
(defined with $\sqrt3\,u_{\mathrm{rms}}$ over the sound speed), $512^3$
cells, viscosity $\propto T^{0.76}$, up to five large-eddy turnover times.
WENO-Z reconstruction in characteristic variables and a collision time
enlarged at pressure jumps keep the runs stable "without extra special
treatment", and the time histories of density rms, kinetic energy, velocity
derivative skewness and flatness, and of the dissipation are offered as
benchmark data. With rising $M_t$ the normalized density rms
$\rho_{\mathrm{rms}}/M_t^2$ decreases, the peak total dissipation grows, its
solenoidal part $\varepsilon_s=\langle\mu\,\omega_i\omega_i\rangle$ decreases
and its dilatational part $\varepsilon_d=\tfrac43\langle\mu(\nabla\cdot\boldsymbol u)^2\rangle$
increases; the pressure–dilatation correlation changes sign and stays small
and positive later, as in the subsonic results of Sarkar et al. that the
authors cite (Figs. 13–14; $\varepsilon_s$, $\varepsilon_d$ page-local).
Shocklets, regions where the dilatation is below $-3$ times its rms, appear as
long narrow ribbons beside block-like expansion regions (Fig. 15). The
resolution criterion $k_{\max}\eta_0\ge2.71$ is taken from the authors'
earlier work. The authors state that compact finite differences are limited
to $M_t\le0.8$ and that spectral and lattice Boltzmann methods fail to capture
shocklets (§1, §3.4).

**Driven MHD turbulence and the small-scale dynamo.**
[Seta & Federrath (2022)](/sources/seta-2022.md) drive turbulence in a
triply periodic box with heating and cooling, so that the gas splits into a
cold supersonic phase (3–4% of the volume by their text, rms Mach number about 5) and a
warm transsonic phase, and follow the growth of a weak seed field. Explicit
viscosity and resistivity at $Re=Rm=2000$ are chosen to exceed the numerical
diffusion, whose effective Reynolds number they estimate at about $2N_x^{4/3}\approx8000$
for $N_x=512$ (§2.4, from McKee et al.). The kinematic growth rate of the
magnetic-to-kinetic energy ratio is the same in both phases, $0.37$ and
$0.18$ per driving time for solenoidal and compressive driving, and both
growth rate and saturation level are lower than the isothermal empirical
model of Federrath et al. at matching Mach numbers (§4.1, Table 1); they
explain the equal growth rates through a vorticity budget (§4.2). As
recalled by [Martin-Alvarez et al. (2022)](/sources/martinalvarez-2022.md),
turbulent-box simulations of this kind (Balsara et al.; Federrath;
Schekochihin et al.) are the reference for the growth rates and the
resolution scaling expected of the dynamo in galaxy simulations. See
[small-scale dynamo](/results/small-scale-dynamo.md).

**A priori structure of the subgrid flux.**
[Vela-Martín (2022)](/sources/velamartin-2022.md) uses the forced database
to show that the mean local SGS flux $\langle\Pi\rangle$ equals $\varepsilon$
at all filter scales tested (inertial-range filtering) and that the
backscatter it contains can be moved into a conservative spatial flux by a
gauge transformation of the SGS stress (see
[energy backscatter](/definitions/energy-backscatter.md)). The flux the
paper writes $T$ equals the registry's $\Pi$, because the paper's SGS
stress has the opposite sign.

**Learned closures, a priori against a posteriori.**
As recalled by [Duraisamy (2021)](/sources/duraisamy-2021.md), §IV.B, Fig. 2,
from Sirignano, MacArt & Freund, an a priori-trained SGS closure
over-predicts the resolved kinetic energy of decaying HIT, while a
model-consistent (differentiable-physics) closure follows the filtered DNS.
[Agdestein & Sanderse (2025)](/sources/agdestein-2025.md), App. G.2, find
that in 3D forced turbulence ($\bar n=32,64$) a CNN closure in their
divergence-consistent formulation beats no model and Smagorinsky
($C_s=0.17$) in a priori and a posteriori error, while Smagorinsky is too
dissipative at high wavenumbers. See
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
and [model-consistent training](/methods/model-consistent-training.md).

**A nonlocal closure, a priori and a posteriori.**
[Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md) use forced HIT at
$Re_\lambda=170$, 240 and 355 to fix the order of their dynamic
[fractional SGS model](/methods/fractional-sgs-model.md) a priori: the order
that maximizes the stress correlation with box-filtered DNS falls with the
filter size and rises with $Re_\lambda$, fitted by a power law of the
filter size (§III.1, Table I). At $Re_\lambda=240$ and dimensionless filter
sizes 4 and 8 the dynamic fractional model correlates better with the exact
SGS stress than static and dynamic Smagorinsky and the static fractional
model in all six components, and predicts a backscatter volume fraction
$v^-$ of 24% and 25% against 26% and 30% in the filtered DNS and 20% and 18%
for dynamic Smagorinsky (§III.2, Figs. 4–5; see
[energy backscatter](/definitions/energy-backscatter.md)). A posteriori in
decaying HIT at $Re_\lambda=240$, its resolved-energy decay is closer to the
filtered DNS than that of dynamic Smagorinsky at filter size 4 and, more
markedly, at the very-large-eddy filter size 20, where dynamic Smagorinsky
decays too fast (§IV, Fig. 9).

**Numerical dissipation of hybrid RANS/LES schemes.**
[Carlsson et al. (2023)](/sources/carlsson-2023.md), §4.2, Fig. 3, run the
decaying grid turbulence of Comte-Bellot & Corrsin with the LES branch of
Spalart–Allmaras- and SST-based
[detached-eddy simulation](/methods/detached-eddy-simulation.md) in an
unstructured second-order finite-volume code. With the fourth-difference
artificial-dissipation coefficient of RANS practice ($1/128$) the spectra
decay too steeply at high wavenumbers on all three grids; the
[low-dissipation low-dispersion scheme](/methods/low-dissipation-low-dispersion-scheme.md)
with $1/512$ or $1/1024$ matches the measured spectra, $1/512$ being only
slightly more dissipative. With it the standard constants $C_{DES}=0.65$
(Spalart–Allmaras) and 0.61 (the $k$-$\varepsilon$ branch of SST) need no
recalibration; 0.78 for the $k$-$\omega$ branch gives nearly identical
results (not shown). The authors conclude that in this case the numerical
dissipation of the convection scheme dominates the decay of turbulent
kinetic energy (§5). See [numerical dissipation](/properties/numerical-dissipation.md).

**Driven compressible MHD turbulence with a guide field.**
[Gan et al. (2022)](/sources/gan-2022.md) drive isothermal compressible MHD
in a periodic box threaded by a strong uniform field and decompose the
fluctuations into Alfvén, fast and slow modes. A spatial projection onto the
linear eigenvectors assigns 0.137 of the power outside the injection range
to fast modes under compressible driving; a space–time Fourier analysis that
counts only power within ±10% of each mode's linear frequency assigns 0.024
to fast modes and 0.73 to 0.79 to fluctuations on no linear branch
(§3, Fig. 2). The guide field makes the box anisotropic; see
[compressible MHD turbulence](/results/compressible-mhd-turbulence.md).

**Not this case: decaying MHD from the Orszag–Tang vortex.**
[Foldes et al. (2023)](/sources/foldes-2023.md) test a
[lattice Boltzmann](/methods/lattice-boltzmann-method.md) MHD code on a
triply periodic box too, but their initial field is the deterministic 3D
Orszag–Tang vortex, not isotropic turbulence (§4.4, §5); that test is
recorded on [decaying MHD turbulence](/results/decaying-mhd-turbulence.md).

**Closure constants.** As recalled by
[Duraisamy et al. (2019)](/sources/duraisamy-2019.md), decay rates of grid
turbulence (Comte-Bellot & Corrsin 1966) constrain the coefficients of RANS
closures (the coefficient layer of their taxonomy of
[model-form uncertainty](/definitions/model-form-uncertainty.md)). As recalled by
[Agrawal et al. (2022)](/sources/agrawal-2022.md), §II.A, Lilly derived
$C_s\approx0.17$ for isotropic turbulence with an inertial-range cutoff;
[Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md), §6.5,
quote Lilly's analytical value $C_s=\pi^{-1}(3C_K/2)^{-3/4}=0.18$ with
Kolmogorov constant $C_K=1.4$. The Chollet–Lesieur spectral eddy viscosity,
whose plateau 0.267 holds for an infinite Kolmogorov spectrum, is the
spectral reference used with HIT in both
[Flad & Gassner (2017)](/sources/flad-2017.md), App. C, and
[Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md), Eq. (55)
(see [spectral eddy viscosity](/methods/spectral-eddy-viscosity.md)).
As recalled by [Basile et al. (2023)](/sources/basile-2023.md), §2.2, the
DES constant $C_{DES}=0.65$ is calibrated on decaying homogeneous turbulence
(see [detached-eddy simulation](/methods/detached-eddy-simulation.md)), the
value with which [Carlsson et al. (2023)](/sources/carlsson-2023.md)
reproduce the Comte-Bellot–Corrsin decay once the scheme's dissipation is
low enough. As
recalled by [Pereira et al. (2021)](/sources/pereira-2021.md), §III, Fig. 4,
from the authors' companion paper, explicit filtering of forced HIT DNS of
Silva et al. at $Re_\lambda=140$ and 300 supports setting the dissipation
ratio of [partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md)
to $f_\varepsilon=1$ for $f_k\ge0.20$.

## Qualifications

- Forcing differs between sources (linear forcing at the nodes; linear
  momentum forcing; Kolmogorov forcing at a single wavenumber). [Beck & Kurz (2023)](/sources/beck-2023.md)
  note that their nodal forcing injects energy at all wavenumbers present
  and causes a slight departure of the spectrum from $k^{-5/3}$.
- [Flad & Gassner (2017)](/sources/flad-2017.md), §1, print the large-eddy
  turnover time as "$T=\bar v(t_{\mathrm{start}})/L_{\mathrm{int}}\approx1.3$",
  a velocity over a length; a time is length over velocity.
- [Vela-Martín (2022)](/sources/velamartin-2022.md) prints $Re_\lambda=320$
  in the Fig. 6 and Fig. 7 captions and in §6.4 for the $1024^3$ case, for
  which Table 1 and §5.1 give 324.
- [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md) name the 3D
  case of App. G.2 both "forced" (title) and "decaying" (first sentence)
  while applying a body force, and print its amplitude as 5 while Eq. (31)
  of the 2D case has amplitude 1 and App. G.2 calls it "the same body force".
- [Cao et al. (2022)](/sources/cao-2022.md) were read in the arXiv v1
  preprint. Their Eq. (11) prints the energy balance as
  $d\langle K\rangle/dt=\varepsilon+\langle p\,\nabla\cdot\boldsymbol u\rangle$
  with $\varepsilon=\varepsilon_s+\varepsilon_d$, a sum of non-negative
  terms, while the text describes a decay; a decay needs $-\varepsilon$
  *(compiler check, not in the sources)*. They print the maximum resolved
  wavenumber as $\sqrt2k_0N_x/3$ with $k_0=8$. With $N_x=512$,
  $\Delta=2\pi/512$ and their $\Delta/\eta_0=0.819$, $\sqrt2N_x/3$ gives
  $k_{\max}\eta_0=3.617$, close to their Table 8 value 3.613, while the
  printed factor $k_0=8$ would give 28.9 *(compiler check, not in the
  sources)*. Their Mach number of the
  supersonic runs is the turbulent one; §1 calls the range "hypersonic",
  the abstract and §3.4 "supersonic".
- [Seta & Federrath (2022)](/sources/seta-2022.md) are a non-isothermal,
  magnetized, driven box: the isotropy of the large-scale forcing is the
  only sense in which the case is "isotropic". Read in arXiv v2.
- [Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md) (read in arXiv
  v3) multiply the squared filter width directly by their Smagorinsky
  coefficient, so that it corresponds to the registry's $C_s^2$, and print neither its value nor
  the constant of the static fractional model. Their filter size is the
  filter width over twice the DNS grid spacing, as printed. They label the
  subfilter energy $\tfrac12(\overline{u_iu_i}-\bar u_i\bar u_i)$ "resolved" and
  $\tfrac12\bar u_i\bar u_i$ "filtered" (Eq. 24); the labels are swapped
  relative to the formulas.
- [Carlsson et al. (2023)](/sources/carlsson-2023.md) give the resolution as
  $N^3$ nodes ($N_x^3$ here) and measure time from the first experimental
  station; their tests are hybrid RANS/LES in LES mode, not wall-resolved
  closure tests.
- [Gan et al. (2022)](/sources/gan-2022.md) (read in arXiv v1) are
  periodic-box turbulence but anisotropic by construction (guide field
  $v_A=8$); their fractions exclude the injection range $\lvert\boldsymbol k\rvert\le2$
  and the $(k_\parallel=0,\omega=0)$ component.
- [Kurz et al. (2023)](/sources/kurz-2023.md) and
  [Beck & Kurz (2023)](/sources/beck-2023.md) both compare reinforcement-learned
  closures with the dynamic Smagorinsky model on forced HIT at
  $Re_\lambda\approx180$ but in different configurations (polynomial degrees,
  DOF, action noise). Kurz et al. find the RL model equal to the dynamic
  model except at 24 DOF, where it is "significantly better" (§4.2); Beck &
  Kurz find the RL models better than the dynamic model for $N=5$ and $N=8$,
  with the dynamic model close at 36 DOF and off at 24 DOF (§V A–B). Both
  report the dynamic model's weakness at 24 DOF and relate it to the test
  filter leaving the scale-similar range, so they agree where their
  configurations overlap.
- [Kang et al. (2023)](/sources/kang-2023.md), App. A, Table 14, obtain
  $Re_\lambda=122.9$, not 164, when reproducing the forced DNS of Langford &
  Moser with the negative-viscosity forcing that paper describes, and 164.7
  with the deterministic forcing of Machiels. They print the Leaky-ReLU
  activation as $\max[-0.02x,x]$ (§2.4): for $x<0$ this returns
  $-0.02x>0$, a non-monotone function, whereas $\max[0.02x,x]$ has slope
  0.02 for negative arguments *(compiler check, not in the sources)*; the
  paper does not say which form the code uses.
- The set-ups differ in what is forced: velocity modes below a wavenumber
  at fixed power ([Prakash et al. (2022)](/sources/prakash-2022.md),
  Eqs. 21–23), solenoidal or compressive acceleration fields
  ([Seta & Federrath (2022)](/sources/seta-2022.md)), or nothing (the
  decaying runs).

# Citations

- [Flad & Gassner (2017)](/sources/flad-2017.md) — §1, §3–5, Figs. 1–10, App. C.
- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §II.A, §VII.A–C, Figs. 3–6.
- [Beck & Kurz (2023)](/sources/beck-2023.md) — §IV A–B, §V, Figs. 6–14, App. A.
- [Vela-Martín (2022)](/sources/velamartin-2022.md) — §5.1–5.3, Table 1, Figs. 1–7.
- [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md) — §5, App. B.2, App. G.1–G.2.
- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §IV.B, Fig. 2 (recalled result).
- [Duraisamy et al. (2019)](/sources/duraisamy-2019.md) — test-problem list (recalled grid-turbulence calibration).
- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §6.2, §6.4–6.5, Eq. (55).
- [Prakash et al. (2022)](/sources/prakash-2022.md) — §III.A, Tables 1–2, Figs. 1–3; §III.B.1, Eqs. (21)–(24), Fig. 4.
- [Cao et al. (2022)](/sources/cao-2022.md) — §1; §3.4, Eqs. (9)–(11), Table 8, Figs. 13–15.
- [Seta & Federrath (2022)](/sources/seta-2022.md) — §2, §2.4, §4.1–4.2, Table 1, Figs. 7–10.
- [Martin-Alvarez et al. (2022)](/sources/martinalvarez-2022.md) — recalled turbulent-box references.
- [Basile et al. (2023)](/sources/basile-2023.md) — §2.2 (recalled calibration of $C_{DES}$).
- [Pereira et al. (2021)](/sources/pereira-2021.md) — §III, Fig. 4 (recalled a priori filtering).
- [Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md) — §III.1–III.2, Eq. (23), Table I, Figs. 3–7; §IV, Figs. 8–10.
- [Carlsson et al. (2023)](/sources/carlsson-2023.md) — §4.2, Fig. 3; §5.
- [Gan et al. (2022)](/sources/gan-2022.md) — §2; §3, Figs. 1–3.
- [Kurz et al. (2023)](/sources/kurz-2023.md) — §1, §3.4–3.5, Table 2; §4.1–4.5, Figs. 5–9.
- [Kang et al. (2023)](/sources/kang-2023.md) — §2, Table 1; §3.1–3.4, Tables 3–6, Figs. 4–24; App. A, Table 14.
- [Foldes et al. (2023)](/sources/foldes-2023.md) — §4.4, §5 (contrast only: Orszag–Tang initial field).
