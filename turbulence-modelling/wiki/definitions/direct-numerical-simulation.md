---
type: Definition
title: "Direct numerical simulation"
description: "DNS solves the Navier–Stokes equations with no turbulence model and a grid fine enough for the dissipative range; this page gives its resolution criteria, measured resolutions and cost, the discretizations, GPU codes and floating-point precision used for it, spatially developing boundary layers, weaker variants, looser uses of the term, and its role as reference data."
status: established
aliases: [DNS, quasi-DNS, flame-resolved DNS, under-resolved DNS, DNS embedded in LES, downsized DNS, DNS-like simulation, fully resolved simulation with detailed chemistry]
tags: [dns, les, combustion, boundary-layer, compressible, gpu]
timestamp: 2026-10-26T15:48:00Z
---

# Direct numerical simulation

**Direct numerical simulation (DNS)** is the numerical solution of the
Navier–Stokes equations, without any turbulence or subgrid-scale model, on a
grid and time step fine enough to resolve all dynamically relevant scales of
motion down to the dissipative range, so that the computed field is a
realization of the turbulent flow itself rather than of a filtered or averaged
one. Goc et al. (2021, §1) summarize its standing: there is "little doubt that
first-principles-based, direct numerical simulation would provide accurate
predictions, but the resolution requirements at high Reynolds numbers would be
prohibitive", which is why [large-eddy simulation](/definitions/large-eddy-simulation.md)
and [wall-modelled LES](/methods/wall-modelled-les.md) exist. In this bundle DNS
is chiefly the reference against which closures are trained and tested.

## Resolution criteria and cost

**Mesh size.** [Domingo & Vervisch (2023)](/sources/domingo-2023.md), §2, take
a mesh spacing $h=2\eta$, with $\eta$ the Kolmogorov length, as sufficient to
capture the dissipative range (as recalled from Moin & Mahesh). With the
turbulent Reynolds number $Re_T=k^{1/2}L/\nu\approx(L/\eta)^{4/3}$ (page-local;
$L$ the integral length), the number of points in a cube of side $L_o$ is
$$N_{\mathrm{pts}}=\Big(\frac{L_o}{2\eta}\Big)^3=\Big(\frac{L_o}{2L}\Big)^3Re_T^{9/4}$$
(Eqs. 1–2). Their example: resolving $10^3\,\mathrm{cm}^3$ of the shear layer of
a gas-turbine swirl burner with $Re_T\sim1500$ and $L\sim5$ mm needs more than
$10^{10}$ points; with $L_o=10$ cm the formula gives $1.4\times10^{10}$
*(compiler check, not in the sources)*. A consequence they draw is that DNS
domains contain only a few integral scales ($L_o\simeq L$ in canonical flame
DNS), which limits the range of wrinkling and, in their reading, partly explains
why few DNS-derived closures have reached engineering codes (§1–§2).

**Reacting flows.** With the Damköhler number $Da=\tau_T/\tau_c$ and the
Karlovitz number $Ka=\tau_c/\tau_\eta$ (page-local; $\tau_T=k/\varepsilon$ the
integral time, $\tau_c$ a chemical time), $Da\,Ka\approx Re_T^{1/2}$ and
$$N_{\mathrm{pts}}=\Big(\frac{L_o}{2L}\Big)^3Da\,Ka\,Re_T^{7/4}$$
(Domingo & Vervisch 2023, Eqs. 3–6): DNS cannot reach large $Da$ and large $Ka$
together, and at fixed $Da$ raising $Ka$ by a factor $a$ requires raising $Re_T$
by $a^2$. Cost also grows with the number of transported species, and faster
than linearly because of stiffness.

**Other criteria in use.** Cogo et al. (2022, §2) require the effective
spacing $(\Delta x\,\Delta y\,\Delta z)^{1/3}$ to stay below $4\eta$
everywhere in their boundary layers. Cao et al. (2022, §3.4) adopt
$k_{\max}\eta_0\ge2.71$ (with $k_{\max}$ the largest resolved wavenumber and
$\eta_0$ the initial Kolmogorov length) and a time step
$\Delta t/\tau_{\mathrm{to}}\le5.58\times10^{-3}$ of the initial large-eddy
turnover time, taken from their earlier study, for decaying compressible
isotropic turbulence. Seta & Federrath (2022, §2.4) run a shock-capturing
finite-volume MHD code (FLASH, HLL3R solver) at $512^3$ with explicit
viscosity and resistivity, $Re=Rm=2000$, and argue that because the
numerical Reynolds number of the scheme is approximately
$2n_g^{4/3}\approx8000$ for $n_g=512$ points per direction (as recalled from
McKee et al. 2020), the explicit diffusion "is always significantly higher
and at larger scales than the numerical diffusion"; their runs are DNS in
this sense (see [small-scale dynamo](/results/small-scale-dynamo.md)).
For a transcritical channel, [Bernades et al. (2023)](/sources/bernades-2023.md),
§4.3, argue their $128^3$ grid finer than the Lee & Moser DNS and twice as
fine per direction as an earlier transcritical study, and note that the
density-gradient length there is about ten Kolmogorov lengths.

**Cost scaling and forecasts.** As recalled by
[Morsbach et al. (2024)](/sources/morsbach-2024.md), §1, from Choi & Moin,
the cost of DNS grows roughly as $Re^{3.5}$ and that of wall-resolved LES as
$Re^{2.5}$ (see [grid-point requirements](/results/les-grid-point-requirements.md));
[Delassaux et al. (2023)](/sources/delassaux-2023.md), §4.1, recall
Spalart's forecast that wall-resolved LES and DNS of a full-scale
high-Reynolds-number geometry would become available around 2050 and 2080.

**Exascale isotropic turbulence.** [Yeung et al. (2025)](/sources/yeung-2025.md)
reach $Re_\lambda\approx2500$ on a $32\,768^3$ grid with a GPU Fourier
pseudo-spectral code on Frontier, the first exaflop machine; the largest
grid that fits in its memory is $40\,960^3$ (§1). Their resolution pair is
$k_{\max}\eta$ with the Courant number: about $\{1.4,0.6\}$ for scales
larger than $\eta$ and $\{2.8,0.3\}$ for the dissipation range, with
$k_{\max}\eta=(\sqrt2N_x/3)\eta$ (§2.2). They state the cost: 13 s per step
on 44% of the machine, about 1000 steps per Kolmogorov time and
$T_E/\tau_\eta\approx300$ ($T_E$ the large-eddy turnover time, page-local),
so ten large-eddy times would take "two years or more" (§1); going from
$Re_\lambda=1000$ to 2500 needs four times the points per direction, at
least 64 times the wall time per step and 256 times for a given physical
time, on a machine with at least 64 times the memory (§5). They therefore
use the [multi-resolution independent simulations](/methods/multi-resolution-independent-simulations.md)
protocol, which runs the finest grid only for a few Kolmogorov times from
independent snapshots, and restrict it to dissipation-range statistics. They
add, citing Yakhot & Sreenivasan, that scales finer than the Kolmogorov
scale appear more copiously as the Reynolds number grows, which calls for
better small-scale resolution than is often practised (§1).

**Measured resolutions in the sources.**

| Flow | Resolution | Source |
|---|---|---|
| Circular cylinder, $Re_D=3900$, flux reconstruction $N=3$, about 55.6 M DOF | minimum $\eta/D=0.011$; in-plane spacing $0.25$–$0.83\,\eta$ for $x/D<10$; spanwise $0.85\,\eta$ as printed | Dzanic et al. (2022), §3.2 |
| [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md), $Re=40000$ | $5400^3$ nodes, computed on the symmetric sub-box $\pi^3$ | Vicente Cruz & Lamballais (2023), §6.1 |
| Pipe, $Re_\tau=1000$, immersed boundary on a Cartesian mesh | $768\times768\times1920$, uniform $\Delta x^+=\Delta y^+\approx3$ with no near-wall refinement; agrees with the DNS of El Khoury et al. | Vicente Cruz & Lamballais (2023), §7.1 |
| Forced [isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md), $Re_\lambda\approx180$, DGSEM $N=7$ | $64^3$ elements, $512^3$ points; about 30,000 CPU-hours on 16,384 cores | Beck & Kurz (2023), §IV A |
| Decaying isotropic turbulence, $Re_\lambda$ 162 to 97 | pseudo-spectral, $512^3$, 2/3-rule de-aliasing (reference of the LES) | Flad & Gassner (2017), §1 |
| Supersonic turbulent boundary layer, $M=2.67$, $Re_\theta$ up to 3878 | 1.458 billion DOF per variable (a cited work, shown as a picture) | Krais et al. (2021), §2.2.2 |
| Bunsen jet flame, DNS box | $h=50$ µm $\approx\eta$, 28.58 M nodes | Domingo & Vervisch (2023), §3.1 |
| Bluff-body premixed burner (flame-resolved) | 1.6 billion cells, $h=100$ µm $\approx2\eta$ | Domingo & Vervisch (2023), §3.2 |
| [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md), $Re=1600$, $M=0.1$, [gas-kinetic scheme](/methods/high-order-gas-kinetic-scheme.md) | $128^3$ to $1024^3$ cells; large peak-dissipation discrepancy on $128^3$ and $256^3$, agreement with the reference on refinement; $1024^3$ costs 747,062 core hours | Cao et al. (2022), §3.1–3.2 |
| [Channel](/benchmarks/turbulent-channel-flow.md), $Re_\tau=180$, $M=0.1$, gas-kinetic scheme | $128^3$: $\Delta x^+=8.83$, $\Delta z^+=4.42$, $\Delta y^+$ 0.21–5.83 | Cao et al. (2022), §3.3 |
| Decaying compressible isotropic turbulence, $Re_\lambda=72$, $M_t$ 0.8–1.6 | $512^3$, grid spacing $0.819\eta_0$, $k_{\max}\eta_0=3.613$ | Cao et al. (2022), §3.4 |
| ZPG boundary layers, $M_e=2$ and 5.86, $T_w/T_r=0.76$, $Re_\tau$ up to about 2000 | up to $16384\times832\times2048$ points; $\Delta x^+\le7.9$, $\Delta z^+\le4.8$, $\Delta y^+$ from $\le0.7$ to $\le6.5$ | Cogo et al. (2022), §2, Table 1 |
| ZPG boundary layers, $M_e=2.5$, 4.9, 10.9, $Re_\tau$ up to 1244 | three boxes up to $6300\times690\times600$ points ($x$, wall-normal, spanwise); Mach 10.9: $\Delta x^+=7.1$, $\Delta z^+=6.6$, $\Delta y^+$ 0.43–4.2 | Huang et al. (2022), §2.3, Table 2 |
| Two-phase MHD turbulence (small-scale dynamo), $Re=Rm=2000$ | $512^3$, finite volume | Seta & Federrath (2022), §2.4 |
| Mach 2.9, 24° compression ramp, wide span (over 29 boundary-layer thicknesses) | $16250\times240\times8000$ points (31.2 billion; streamwise, wall-normal, spanwise); $\Delta x^+=1.2$, $\Delta y^+=0.41$, $\Delta z^+=1.2$ at the reference station | Dang et al. (2022), §6.1 |
| Boundary layers at Mach 2.9, 7.2 and 9.0 (nitrogen), $Re_\tau$ 202–495, cold walls at Mach 7 and 9 | 7.3 to 361.3 million points; $\Delta x^+$ 6.8–7.8, $\Delta z^+$ 2.9–4.3, first wall-normal point at $y^+$ 0.21–0.31 (the source writes $y$ spanwise and $z$ wall-normal) | Helm & Martín (2022), Tables I–II (the Mach 9 case is a new DNS, the others earlier ones) |
| 5×5 rod bundle, $Re_D=19{,}000$, spectral elements $N=7$ | 8.4 million elements, 2.87 billion points (resolution in wall units not given) | Fischer et al. (2022), §4.1 |
| Forced isotropic turbulence, $Re_\lambda=170$, 240, 355 | pseudo-spectral, $320^3$, $520^3$, $1024^3$ | Seyedi & Zayernouri (2022), §III |
| Transcritical nitrogen channel, $Re_\tau=100$ (bottom-wall values), walls at 0.75 and 1.5 times the critical temperature | $128^3$, $\Delta x^+=9.8$, $\Delta z^+=3.3$, $0.4\lesssim\Delta y^+\lesssim2.3$, first point $y^+=0.1$; kinetic-energy- and pressure-equilibrium-preserving finite differences | Bernades et al. (2023), §4.3 |
| Incompressible channel, $Re_\tau=400$ | $256\times192\times256$, $\Delta x^+=9.8$, $\Delta y^+$ 0.34–10, $\Delta z^+=4.9$; staggered finite differences, fourth order in $x$, $z$ | [Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md), §III A, App. B |
| Channel, $Re_\tau=395$, $M=0.1$, gas-kinetic scheme on GPUs | $256\times256\times128$: $\Delta x^+=\Delta z^+=9.69$, $\Delta y^+$ 0.45–6.40; against the spectral DNS of Moser, Kim & Mansour | [Wang et al. (2023b)](/sources/wang-2023-b.md), §4.2, Table 6 |
| Compressible channel, bulk $Re=3000$, bulk $M=0.8$, isothermal walls | $128\times256\times128$: $\Delta x^+=8.76$, $\Delta z^+=4.38$, $\Delta y^+$ 0.22–2.90; against Fu et al. | Wang et al. (2023b), §4.2, Table 7 |
| Rectangular prisms in confined cross-flow, aspect ratio 1–4, $Re_0=1000$ and 2000 | $512\times256\times64$ to $1024\times512\times128$; minimum $y^+$ 1.71–2.18; averaged over 77 to 427 time units | [Sirignano & MacArt (2023)](/sources/sirignano-2023.md), §3, Table 1 |
| Decaying Orszag–Tang MHD, $Re\simeq1600$ at peak dissipation | lattice Boltzmann $512^3$ and $768^3$ against pseudo-spectral $512^3$ ([GHOST](/software/ghost.md)) | [Foldes et al. (2023)](/sources/foldes-2023.md), §4.4 |
| [Circular cylinder](/benchmarks/circular-cylinder-wake.md), $Re_D=3900$, second-order central differences, immersed boundary | $1025\times501\times128$ over $30D\times50D\times3.14D$; $\Delta x_{\min}=0.004D$, $\Delta y_{\min}=0.002D$, uniform $\Delta z=0.02453D$; validated against the experiment of Parnaudeau et al. and the DNS of Ma et al. | [Kim et al. (2024)](/sources/kim-2024.md), §2–3, Table 1 |
| Circular cylinder, $Re_D=5000$ | $2049\times1001\times128$ ($\Delta x_{\min}=0.002D$, $\Delta y_{\min}=0.001D$), checked on $2049\times1001\times192$ and $3073\times1281\times128$ | Kim et al. (2024), Table 1 |
| [Channel](/benchmarks/turbulent-channel-flow.md), $Re_\tau=178$ | $96\times97\times96$ over $2\pi\delta\times2\delta\times\pi\delta$ | Kim et al. (2024), App. D |
| Forced [isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md), $Re_\lambda\approx160$ and 259 | pseudo-spectral, 2/3 de-aliasing, second-order Adams–Bashforth; $512^3$ and $1024^3$ | [Wang et al. (2023c)](/sources/wang-2023-c.md), §III, App. B, Tables I, V |
| Temporally evolving incompressible mixing layer | $256\times512\times512$ over $4\pi\times8\pi\times8\pi$ | Wang et al. (2023c), §IV, Table III |
| Premixed stoichiometric methane–air V-flame quenching at the cold wall of a channel, bulk $Re=2770$ on the half-width | 200 million hexahedra, wall spacing 12 µm ($\Delta y^+=0.14$ as printed), Kolmogorov length above 45 µm, laminar flame thickness about 0.5 mm; fed by a 60-million-cell periodic channel precursor; 24-species chemistry; more than 18 million core-hours on 32678 cores (as printed) | [Steinhausen et al. (2023)](/sources/steinhausen-2023.md), §2.1 |
| Forced [isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md), $Re_\lambda\approx390$ to 2500 | Fourier pseudo-spectral, single precision, $2048^3$ to $32\,768^3$; final $k_{\max}\eta\approx2.8$ and Courant number about 0.3, reached by [multi-resolution independent simulations](/methods/multi-resolution-independent-simulations.md) | [Yeung et al. (2025)](/sources/yeung-2025.md), §2, Table 1 |
| Supersonic [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md), $Re=1600$, $M_0=1.25$ | sixth-order TENO finite differences (OpenSBLI), $2048^3$; 57,600 A64FX cores for 34 h (1.96 million core hours), 520 GB per snapshot; the first peak of the dilatational dissipation is not converged even at $2048^3$ | [Chapelier et al. (2024)](/sources/chapelier-2024.md), §II.C |
| Compressible channel, bulk $M=1.5$, bulk $Re=3000$, isothermal walls | gas-kinetic finite volumes, $160^3$ (called DNS; the same scheme at $128^3$ is called implicit LES): $\Delta x^+=16.92$, $\Delta z^+=5.64$, $\Delta y^+_{\min}=0.40$; $Re_\tau=213$ against 222 and 218 for the spectral and B-spline DNS of Coleman et al. and Morinishi et al. | [Cao et al. (2024)](/sources/cao-2024.md), §3.3, Tables 4–5 |
| Compressible channel, $Re_\tau\approx1000$ and 2000, $M_b\approx0.1$ | second-order kinetic-energy- and entropy-preserving central differences; $\Delta x^+=9.0$, $\Delta z^+=4.5$, $\Delta y^+$ 0.5–6.0; $2160\times1440\times669$ and $4320\times2880\times819$ points ($x$, $z$, $y$) | [Maejima & Kawai (2025)](/sources/maejima-2025.md), §2, Tables 1–2 |
| Forced isotropic turbulence, $Re_\lambda\approx100$; temporal mixing layer | pseudo-spectral, 2/3 de-aliasing, second-order Adams–Bashforth; $256^3$ and $256\times256\times128$ (training and reference data of a neural operator) | [Li et al. (2024)](/sources/li-2024.md), §V A–B |
| Decaying isotropic turbulence, $Re_\lambda\approx60$; temporal mixing layer | pseudo-spectral, $128^3$ and $256\times256\times128$, $\Delta t=0.001$ | [Zhao et al. (2025)](/sources/zhao-2025.md), §3.1–3.2 |

From their pipe DNS, Vicente Cruz & Lamballais (2023, §7.1) suggest that the
recommendation of about one wall unit for the first wall-normal spacing
"may be somewhat over-demanding".

## Discretizations for DNS

Domingo & Vervisch (2023, §1) list DNS codes of sixth to tenth order, spectral
elements, and fourth- or second-order codes (below). Cao et al. (2022, §1)
state that DNS "is reported rarely within the finite volume framework due to
its over-dissipative nature", and that spectral, pseudo-spectral and
lattice-Boltzmann methods, established for incompressible turbulence, "fail
to capture shocklets and suffer from numerical instability" in compressible
flow with shocks, while compact and hybrid compact–WENO finite differences
have a limiting turbulent Mach number. Their
[high-order gas-kinetic scheme](/methods/high-order-gas-kinetic-scheme.md),
a finite-volume method, reaches $M_t=1.6$ and costs about 1.4 times a
dispersion-relation-preserving finite-difference code on the Taylor–Green
vortex (1.2 after correcting for processor speed; §3.2). For compressible
boundary layers the sources combine a non-dissipative central scheme with
local shock capturing: STREAmS, run on GPUs in CUDA Fortran, uses
energy-preserving schemes in shock-free regions and WENO where the Ducros
sensor detects shocks (Cogo et al. 2022, §2); Huang et al. (2022, §2.2) use a
limiter-optimized seventh-order WENO scheme, or an eighth-order split
convective scheme for their adiabatic Mach 2.5 case, with fourth-order
central viscous fluxes and third-order Runge–Kutta (see
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md)).
[OpenCFD-SCU](/software/opencfd-scu.md) applies Steger–Warming flux splitting
and a hybrid of a linear seventh-order upwind scheme with seventh- and
fifth-order WENO switched by a pressure sensor, with sixth- or eighth-order
central viscous terms (Dang et al. 2022, §2); see
[WENO and hybrid schemes](/methods/weno-scheme.md). Dang et al. (§1) name
the two difficulties of compressible DNS: robustness against low
dissipation at shocks (for Mach numbers "generally exceeding 6" a
dissipative scheme is usually introduced) and cost, from the long domains
needed for developed boundary layers, small time steps, and long times for
low-frequency shock motion. For incompressible flows the sources use Fourier
pseudo-spectral methods, in all directions for isotropic turbulence
(Seyedi & Zayernouri 2022, §III) or in the homogeneous directions of a
channel with second-order finite differences across it and
Adams–Bashforth/Crank–Nicolson time stepping (the channel solver of Kim et
al. 2022, §II A), and
the continuous spectral elements of [Nek5000 and NekRS](/software/nek5000.md)
(Fischer et al. 2022, §2). For the flow past a cylinder, Kim et al. (2024,
§2.1) run DNS and LES with one solver: second-order central differences on a
staggered mesh, a fractional step with third-order Runge–Kutta for
convection and Crank–Nicolson for diffusion, and an
[immersed boundary](/methods/immersed-boundary-method.md) of mass source and
momentum forcing; the scheme "conserves kinetic energy as well as continuity
and momentum, and does not exhibit numerical dissipation" (see
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md)),
and the DNS is the same system with $\tau_{ij}=0$. For reacting flows,
Steinhausen et al. (2023, §2.1) use an in-house OpenFOAM-based finite-rate
chemistry solver of fourth order in space with a second-order implicit
backward time scheme, which they cite as previously validated for
"DNS-like" simulations against DNS reference cases.

**Shock–turbulence reference and the DNS boundary.** For the supersonic
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md),
[Chapelier et al. (2024)](/sources/chapelier-2024.md), §II.C, §III.B.d,
take a sixth-order TENO finite-difference run on $2048^3$ points as the
reference (see [WENO and hybrid schemes](/methods/weno-scheme.md)), describe
the sixth-order compact finite-difference code NS3D, with a tenth-order
compact filter and no shock capturing, as a "compressible high-order DNS
code", and expect the turbulence to be fully or nearly fully resolved at
$512^3$, the shocks sharper but not resolved (§IV.A). For compressible
channel flow [Cao et al. (2024)](/sources/cao-2024.md), §3.3, call a $160^3$
run of their [gas-kinetic scheme](/methods/high-order-gas-kinetic-scheme.md)
DNS and a $128^3$ run of the same scheme implicit LES, and recall (§1) a
limit $M_t\le1.2$ for high-order finite-difference DNS of supersonic
isotropic turbulence against $M_t=2.0$ reached with the gas-kinetic scheme
(both as recalled).

**Thermodynamic consistency.** For real-gas (transcritical) turbulence,
Bernades et al. (2023) show that a kinetic-energy-preserving split form with
a total-energy equation produces spurious pressure oscillations at density
interfaces and diverges in an inviscid mixing layer, and propose a split
form with a pressure equation that is exactly
[pressure-equilibrium preserving](/properties/pressure-equilibrium-preservation.md),
at the price of an $O(h^2)$ total-energy error. In their channel DNS (run with
the C++ code RHEA) both schemes agree to plotting accuracy, "pressure
oscillations are mitigated by physical viscosity", and the lack of
total-energy conservation causes no deviation (§4.3, §5).

**Lattice Boltzmann against pseudo-spectral.** Foldes et al. (2023, §4.4)
find their [lattice Boltzmann](/methods/lattice-boltzmann-method.md) MHD
code over-damps the kinetic spectrum at high wavenumbers at the resolution
of a pseudo-spectral reference, the two coming close when the lattice code
has 1.5 times the points per direction, which they call "qualitatively
consistent" with the statement of Shen et al. that the lattice Boltzmann
method needs about twice the resolution; the lattice code resolves up to
the Nyquist wavenumber $N_x/2$, the de-aliased spectral code up to $N_x/3$
($N_x$ points per direction). For
Hall-MHD, whose whistler waves force $\Delta t\propto\Delta x^2$ on both
methods, they state that the GPU lattice code gives "significantly smaller"
turnaround times (§5; no side-by-side timing).

**GPU codes and cost.** Several sources of this bundle describe GPU codes for
DNS. [STREAmS](/software/streams.md) runs the boundary-layer DNS of Cogo et
al. (2022) in CUDA Fortran. OpenCFD-SCU, in CUDA-C translated to HIP, runs
weak-scaling tests at $280^3$ points per GPU on up to 24,576 GPUs (more than
500 billion points, 98.7% efficiency as printed), and 512 GPUs outrun its
CPU predecessor on 131,712 cores (Dang et al. 2022, §5.2–5.3). NekRS scales
to all 27,648 V100 GPUs of Summit with up to 60 billion points, with 80%
parallel efficiency at about 2.5 million points per GPU (Fischer et al. 2022,
§4.2). Maeyama et al. (2022, Methods) report 3.1 PFLOPS on 12,288 nodes of
Fugaku for the gyrokinetic code GKV. The printed efficiencies of OpenCFD-SCU
are not all reproduced by its own timings (see its page) *(compiler check,
not in the sources)*. Wang et al. (2023b, §4.1) port the
[gas-kinetic scheme](/methods/high-order-gas-kinetic-scheme.md) to GPUs:
one Tesla V100 runs the $256^3$ Taylor–Green vortex about 16 times faster
than an 8-core desktop and about as fast as some 300 cores of TianHe-II,
and eight V100s run $512^3$ about three times faster than 1024 TianHe-II
cores. The FLAME lattice Boltzmann code reaches 2.7 billion lattice updates
per second at $512^3$ on three A100 GPUs (Foldes et al. 2023, §5).

**Floating-point precision.** Wang et al. (2023b, §4.2, Table 8) compare
single and double precision for channel DNS: single precision halves memory
and runs 1.7 to 2.7 times faster; statistics averaged over 200
$\delta/U_c$ agree, but instantaneous r.m.s. profiles at $t=20$ and
$200\,\delta/U_c$ after a common restart differ visibly, which the authors
attribute to round-off "approximately equals to or larger than the errors
of numerical scheme". They conclude that single precision "may not be safe
for DNS in turbulence especially for time-evolutionary turbulent flows" and
"may be used" for LES and RANS (§5). The deviation is shown in
instantaneous r.m.s. profiles (Fig. 14); the profiles averaged over 200
$\delta/U_c$ show "negligible" differences between precisions (Figs. 10–13).

Yeung et al. (2025, §2.2) run all their isotropic DNS in single precision
and judge machine-precision effects unlikely to have strongly affected
their conclusions, given segments of about two Kolmogorov times at the
finest resolution and earlier tests on peak dissipation and enstrophy,
while conceding that "rigorous testing is not readily available".

**Compressible DNS and the bulk viscosity.**
[Beattie et al. (2025)](/sources/beattie-2025.md) argue that compressible
"DNS" with an explicit shear viscosity only, under the Stokes hypothesis of
zero [bulk viscosity](/definitions/bulk-viscosity.md), leave the dissipation
of the compressible (longitudinal) velocity modes to the scheme: "the grid
controls the dissipation of the compressible modes", which turns "what is
usually considered a direct numerical simulation (DNS) into an implicit
large eddy simulation for the compressible modes" (§9.1; see
[implicit LES](/definitions/implicit-les.md)). In their isothermal MHD
dynamo runs at rms Mach about 1 (finite volumes, $128^3$ to $1024^3$), with
no explicit bulk viscosity the ratio of compressible to incompressible
kinetic-energy spectra rises from about $10^{-1}$ at large scales to $10^2$
at small scales, a pile-up they call a bottleneck, and should "grow
unbounded" with resolution, "which exactly what one expects for an ILES"
(§6.1–6.2, App. D; as printed). With a bulk viscosity ten times the shear
viscosity the run is "converged on all scales at $512^3$"; with equal
viscosities the bulk-viscous scale is not resolved even at $1024^3$ (App. D).
Their requirement for a compressible DNS that resolves all viscous scales
is an explicit bulk and shear viscosity with ratio of order one (§9.1).
Details are on [small-scale dynamo](/results/small-scale-dynamo.md) and
[bulk viscosity](/definitions/bulk-viscosity.md).

## Spatially developing boundary layers

DNS of spatially developing [boundary layers](/benchmarks/turbulent-boundary-layer.md)
needs a turbulent inflow and a domain long enough for it to be forgotten.
Both compressible studies use a recycling–rescaling inflow (recycling plane
at $80\delta_{\mathrm{in}}$ in Cogo et al. 2022, §2; at $52.7\delta_i$ in
Huang et al. 2022, §2.3, with $\delta_{\mathrm{in}}$, $\delta_i$ the inflow
thickness). Huang et al. (2022, §3.1, Table 3) measure the **induction
length**, the distance from the inflow to where the von Kármán integral
relation $C_f=2\,\mathrm d\theta/\mathrm dx$ first holds to 5%: it grows with
Mach number from $20\delta_i$ at Mach 2.5 to $80\delta_i$ at Mach 14, lies
between one and three eddy-turnover lengths $U_e\delta_i/u_{\tau,i}$, and is
$15$–$20\delta_i$ longer with a digital-filter inflow than with
recycling–rescaling; outer-layer differences between the two inflows persist
much farther downstream than near-wall ones. To reach $Re_\tau\approx1200$
over more than $300\delta_i$ they split the domain into three overlapping
boxes, each fed by inflow planes saved from the one upstream (§2.3, Fig. 1).
Their checks: spanwise refinement from $\Delta z^+=6.6$ to 5.0 changes wall
heat flux, mean velocity and Reynolds stresses by about 1%, and the
Mach 10.9 wall shear stress and heat flux agree with Baldwin–Lomax RANS
within 1.9% and 1.7% (App. A). Helm & Martín (2022, §II) feed their
compression-ramp simulations from an auxiliary boundary layer with
recycling–rescaling over a long box, the solution at its rescaling plane
being interpolated onto the ramp inflow; the long rescaling length
decorrelates the recycled eddies and keeps the boundary-layer state fixed
over the long times needed for low-frequency shock motion. Their Mach 9 DNS
was initialized from a RANS mean profile with incompressible DNS
fluctuations scaled by the mean density, after Morkovin's hypothesis.
Dang et al. (2022, §5.1, §6.1) instead trip the boundary layer by wall
blowing and suction upstream of the region of interest. These DNS are the data against which
[Morkovin's hypothesis](/definitions/morkovin-hypothesis.md), the
[attached-eddy hypothesis](/definitions/attached-eddy-hypothesis.md) and the
[compressible velocity transformations](/definitions/compressible-velocity-transformation.md)
are tested.

## Weaker forms and hybrids

- **Quasi-DNS (flame-resolved DNS).** Quoted by Domingo & Vervisch (2023, §1)
  from Zirwes et al.: "a model-free simulation which does not fulfill all of
  the strict requirements of a DNS, e.g. for complex geometries which do not
  allow the use of higher order discretization schemes, but is accurate enough
  so that the results of a full DNS are expected to be similar". Its spurious
  numerical dissipation needs careful calibration. Their bluff-body burner run
  at about $2\eta$ is of this kind.
- **Under-resolved DNS.** A model-free simulation on a grid too coarse for DNS
  is [implicit LES](/definitions/implicit-les.md); Dzanic et al. (2022, §1)
  use "implicit LES (ILES) or under-resolved DNS (URDNS)" as synonyms, and
  [Kou et al. (2023)](/sources/kou-2023.md), §1, use the two terms
  interchangeably. Dzanic et al. use URDNS
  as the baseline of their [PANS](/methods/partially-averaged-navier-stokes.md)
  study, where high-order URDNS of the periodic hill shows oscillations in the
  second moments that they attribute to aliasing (§3.1). In PANS the limit
  $f_k=0$ is DNS; Pereira et al. (2021, §IV.2) use their $f_k=0$ run of
  [Rayleigh–Taylor mixing](/benchmarks/rayleigh-taylor-mixing.md) on a
  $256^2\times768$ finite-volume grid as "a high-fidelity simulation
  resolving all flow scales", while noting that its molecular-mixing
  parameter is about 0.26 at $t=0$ instead of zero because the initial
  perturbations are not fully resolved; its mixing-layer growth rate
  ($\alpha_b\approx0.025$) matches the DNS of Livescu et al. (as recalled).
  [Prieto Saavedra et al. (2024)](/sources/prietosaavedra-2024.md), §1,
  likewise write that implicit LES is "often referred to in the literature
  as under resolved DNS"; in their stabilized finite-element version the
  dissipation comes from the SUPG/PSPG stabilization term. For the
  [periodic hill](/benchmarks/periodic-hill.md) at $Re_h=5600$ they place
  their meshes ($\Delta y^+_{\mathrm{avg}}$ from 1.66 to 0.61,
  $\Delta x^+_{\mathrm{avg}}$ from 2.96 to 1.39, $\Delta z^+_{\mathrm{avg}}$
  from 4.20 to 1.51; App. B, Table B.6) between the DNS of Krank et al.
  ($\Delta y^+_{\max}<0.86$, $\Delta x^+_{\max}=\Delta z^+_{\max}=7.2$, as
  recalled) and wall-resolved LES ($\Delta x^+\approx50$–100,
  $\Delta y^+\approx1$, $\Delta z^+\approx15$–30), "which is exactly the
  definition of implicit LES when it comes to mesh resolution" (§3.2). Their
  average $\Delta x^+$ and $\Delta z^+$ lie below the maxima of 7.2 they
  quote for the degree-7 finite-element DNS, with linear elements against
  degree 7 *(compiler check, not in the sources; averages and maxima are not
  directly comparable)*. In the other direction,
  [Domaradzki (2024)](/sources/domaradzki-2024.md), §3.1, Fig. 4b, shows that
  a model-free run on the $64^3$ LES mesh of the Comte-Bellot & Corrsin
  decaying grid turbulence fails to follow the measured spectra, which the author's
  [autonomous eddy-viscosity model](/methods/autonomous-eddy-viscosity-model.md)
  follows on the same mesh.
- **DNS-like reacting simulations.** Steinhausen et al. (2023) call their
  turbulent side-wall-quenching flame a "fully resolved simulation with
  detailed chemistry" (Abstract), run with a solver validated for
  "DNS-like" simulations (§2.1); resolution is argued from the wall spacing
  against the Kolmogorov length and the laminar flame thickness (table
  above), not stated as a multiple of $\eta$ throughout the domain. It is
  the reference of their a priori test of a
  [tabulated-chemistry manifold](/methods/flamelet-tabulated-chemistry.md).
  [Böttler et al. (2023)](/sources/bottler-2023.md) use a laminar
  detailed-chemistry reference ("DC", not called DNS) for thermo-diffusively
  unstable hydrogen flames with at least 20 grid points across the flame
  (§2.2), and state that simulations of intrinsic flame instabilities are
  sensitive to domain size, grid resolution, initialization and numerical
  methods, which restricts DNS to academic configurations (§1, §2.2).
- **DNS embedded in LES.** Domingo & Vervisch (2023, §3.1) refine a
  well-resolved LES of a laboratory burner to DNS resolution over a streamwise
  window, with the same low-dissipation discretization in both zones, so that
  the flame sees the turbulence developed by the burner instead of synthetic
  fluctuations. In their Bunsen jet ($D=12$ mm, $Re=24000$) the LES has about
  171 million nodes at 150 µm and the DNS box, at $x/D=4.5$–$5.5$, 28.58
  million nodes at 50 µm. The window length is set with a flame-brush growth
  law whose relaxation time is about half an eddy turnover time (Eq. 7).
- **Downsizing.** Scaling all lengths by a factor $s<1$ (page-local) while
  keeping the fluid properties and velocities gives
  $Re_T^\star=sRe_T$, $\eta^\star=s^{1/4}\eta$, $\varepsilon^\star=\varepsilon/s$,
  $\tau_T^\star=s\tau_T$, $\tau_\eta^\star=s^{1/2}\tau_\eta$ (Domingo &
  Vervisch 2023, §5, Eqs. 13–18). Chemistry must be sped up by $s$ to keep $Da$
  or by $s^{1/2}$ to keep $Ka$, which cannot both hold; the authors choose
  locally by the ratio of scalar to flow length scales (Eqs. 19–21). An
  $s=1/30$ quasi-DNS of a 10 MW incinerator (162 million cells) guided an
  injection change that raised the DeNOx efficiency by 7%, reported also in the
  plant.

## Looser uses of the term

Ferrer et al. (2023, §4.1) give the definition: DNS "solves the
Navier-Stokes equations without additional modelling" and is therefore
restricted to moderate Reynolds numbers. Sources at the edge of the bundle
use or avoid the word in other senses:

- **Model-free but inviscid.** Davidovits et al. (2022, §II A) simulate
  shock-generated turbulence with artificial viscosity and no physical
  viscosity or conduction, and state that the runs "should not be regarded as
  direct numerical simulation (DNS), but are rather in the spirit of implicit
  large eddy simulations"; doubling the resolution changes their averaged
  quantities by 0.6–2.9% (see [shock-generated turbulence](/results/shock-generated-turbulence.md)).
- **Model equations with imposed damping.** Kochurin et al. (2022) call
  "direct numerical simulation" a pseudo-spectral integration ($1024^2$
  harmonics) of quadratically truncated Hamiltonian equations for
  magneto-capillary surface waves, with an imposed damping
  $-\nu_d(k-k_d)^2$ of the Fourier amplitudes above a wavenumber $k_d=150$
  (page-local $\nu_d$, the source's $\nu$, and $k_d$, $k_a$) and a spectral cut-off at $k_a=212$ that
  the authors interpret as "superviscosity" (p. 2) (see [weak wave turbulence](/results/weak-wave-turbulence.md)).
- **Resolved one-dimensional model equations.** [van Gastelen et al. (2024)](/sources/vangastelen-2024.md)
  call "DNS" the fine-grid solutions of the one-dimensional Burgers
  equation ($N_x=1000$, $\nu=0.01$, RK4 with $\Delta t=2.5\times10^{-3}$) and
  of the Korteweg–de Vries equation ($N_x=600$, $\Delta t=10^{-4}$, larger
  steps being unstable) that train and test their
  [energy-conserving neural closure](/methods/neural-network-sgs-model.md)
  (§4, App. E.1). The closed coarse models are at least
  twice as fast as this "DNS" for Burgers, and roughly 20 times for KdV,
  which they attribute to the small DNS time step (§4.3.2).
- **Closure-free plasma simulations.** Maeyama et al. (2022) run
  gyrokinetic simulations that resolve both the electron and the ion
  gyroradius scales without a transport closure, and Coelho et al. (2022)
  global two-fluid simulations of stellarator edge turbulence with small
  numerical diffusion terms added for stability (p. 4); neither paper calls its
  runs DNS (see [cross-scale interaction](/results/cross-scale-interaction.md)).

## DNS as reference and test bed

DNS supplies the filtered or averaged fields of
[a priori tests](/definitions/a-priori-and-a-posteriori-testing.md) and the
statistics against which LES are judged. Domingo & Vervisch (2023, §1) caution
that a priori tests "cannot always allow for reaching definitive conclusions"
because they miss error accumulation and compensation over time, and use their
embedded-DNS database for a posteriori tests by coarsening it to LES. They also
call DNS the right test bed for new numerics, since no subgrid model interferes
(§4). Lozano-Durán et al. (2022, §IV.B–C) bound the mean-velocity error of
wall-modelled LES in canonical flows by the difference between DNS and an
inviscid solution, about 15%, and note that wall-modelled LES may not converge
to DNS until the grid reaches the wall-resolved regime, because of the errors
internal to the wall model. [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md),
§2.3, build their [building-block-flow wall model](/methods/building-block-flow-wall-model.md)
on a database of about 500 DNS of channel, Poiseuille–Couette and
three-dimensional channel flows, but train it not on filtered DNS: because
the subgrid stress of an implicitly filtered LES differs from the stress of
the filtered Navier–Stokes equations, they run wall-modelled LES in the
target solver with a mean-flow correction that forces the DNS mean profile
(§2.5; see [discretization-consistent closure](/definitions/discretization-consistent-closure.md)).

Chunk-2 sources use published DNS as the reference for model calibration and
validation: the channel DNS of Lee & Moser at $Re_\tau=1000$ and 5200 for
wall-modelled LES (Gillyns et al. 2022, §5–§9), the SD7003 airfoil DNS of
Carton de Wiart & Hillewaert at $Re=60{,}000$, $\alpha=4^\circ$
(separation at $x/c=0.209$, reattachment at 0.654, $C_L=0.602$,
$C_D=0.0196$) and two- and three-dimensional simulations of the Eppler 387
airfoil by Sahin et al. for a [transition model](/methods/local-correlation-based-transition-model.md)
(Carreño Ruiz & D'Ambrosio 2022, §3.5, Table 5; §6.3, Fig. 19; their 2D results agree with the 2D
simulations but not with the 3D data), and the adverse-pressure-gradient
boundary-layer DNS of Coleman et al. (2018), $Re_\tau$ up to 880, for an
[adverse-pressure-gradient wall law](/definitions/adverse-pressure-gradient-wall-law.md)
(Knopp 2022, §7.3). Gillyns et al. (2022, §2, §6, §8) observe in
spectral-element wall-modelled LES that the spikes of the velocity
fluctuations at element boundaries (a Gibbs phenomenon of the $C^0$
discretization) vanish as the mesh approaches DNS resolution, and use them
as a reference-free indicator of under-resolution.

**Filtered DNS as the LES reference.** Several sources compare LES not with
DNS but with DNS filtered like the LES. Helm & Martín (2022, §III B) apply a
top-hat filter in space, and in time through Taylor's hypothesis, and find
the spectra essentially unaffected for $f\delta/U_e\lesssim0.4$; against it
their LES of Mach 3 to 10 boundary layers, on grids with 32 times fewer
points and a time step 2.8 times larger, reproduces the mean profiles within
3% (5% at Mach 10) and the peak turbulent kinetic energy within 2%, with an
unresolved share of the kinetic energy, estimated from filtered against
unfiltered DNS, of 14–25% at Mach 7 and 10–15% at Mach 3 and 10, with
near-wall minima of 5–7%; they
call the LES cost "equivalent to 3% of the DNS" (§V). The same code runs as a
DNS with the subgrid terms switched off. Filtered isotropic-turbulence DNS
supplies the a priori stresses of Seyedi & Zayernouri (2022, §III), and
time-averaged profiles of filtered channel DNS are the only training targets
of the reinforcement-learning subgrid model of Kim et al. (2022, §II–§III);
see [a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md),
[fractional SGS model](/methods/fractional-sgs-model.md) and
[reinforcement-learning closures](/methods/reinforcement-learning-closure.md).

Further sources use DNS in the same three roles:

- **A priori database.** Inagaki & Kobayashi (2023, §III A) filter their
  $Re_\tau=400$ channel DNS with a sharp spectral cut-off in the two
  homogeneous directions, at a "medium" and a "coarse" width chosen from
  a posteriori dynamic-Smagorinsky LES, to study the energy-transfer-free
  part of the subgrid stress (see
  [scale-similarity models](/methods/scale-similarity-model.md)).
- **Training target.** Sirignano & MacArt (2023, §3.1) box-filter their
  prism DNS with a coarsening ratio of 4 or 8 kept constant on the
  non-uniform mesh and downsample it as an implicitly filtered LES field; it
  is the target of their adjoint-trained
  [neural-network closure](/methods/neural-network-sgs-model.md) and the
  reference of its tests; they observed no significant difference between
  drag coefficients from DNS and from filtered DNS (§4.1). Kurz et al. (2023,
  §3.5) reward their [reinforcement-learning closure](/methods/reinforcement-learning-closure.md)
  by the error against a time-averaged DNS energy spectrum of forced
  isotropic turbulence, whose resolution they do not state.
- **Reference statistics.** The channel DNS of Moser, Kim & Mansour is the
  reference of the gas-kinetic implicit LES of
  [Zhao et al. (2023a)](/sources/zhao-2023.md), §5.2, and of the
  mixed finite-element implicit LES of [Lederer et al. (2023)](/sources/lederer-2023.md),
  §4, which uses the periodic-hill DNS of Balakumar & Ilhwan as well (§5);
  [Saini et al. (2023)](/sources/saini-2023.md), §3.1, take a $512^3$
  spectral DNS of the Taylor–Green vortex as reference and use the equality
  of the measured decay rate and the enstrophy-based viscous dissipation as
  the mark of a DNS. Morsbach et al. (2024, §3.3) build the turbulent
  end-wall inflow of a turbine-cascade LES by scaling the $Re_\theta=670$
  boundary-layer DNS of Schlatter & Örlü to the operating point (see
  [inflow turbulence generation](/methods/inflow-turbulence-generation.md)).
  Prieto Saavedra et al. (2024, Table 1) rank their periodic-hill implicit
  LES against the finite-volume DNS of MGLET (218 million cells, 38
  flow-throughs), the finite-element DNS of Krank et al. (degree 7, 33.6
  million degrees of freedom) and the finite-difference DNS of Incompact3d
  (37.8 million points), as tabulated there.
  [Pacciani et al. (2025)](/sources/pacciani-2025.md), §6.1, set the abrupt
  transition of their RANS on the VKI LS89 [turbine cascade](/benchmarks/turbine-cascade.md)
  against the smoother transition of the quasi-DNS of Segui et al. (as
  recalled).

Two further uses of DNS as reference:

- **Reference for an algebraic RANS closure.** [Chen et al. (2024)](/sources/chen-2024.md)
  evaluate their compressible recalibration of the
  [Baldwin–Lomax model](/methods/baldwin-lomax-model.md), an algebraic RANS
  closure of the whole boundary layer, solved by boundary-layer marching
  (not an LES wall model), against twelve published DNS of zero-pressure-gradient
  boundary layers at free-stream Mach 2 to 13.64 and $T_w/T_r$ from 0.18 to 1.9,
  plus the incompressible DNS of Schlatter & Örlü (Table 1). They
  extract the DNS eddy viscosity as
  $\mu_t=-\langle\rho u''v''\rangle/\partial_y\langle u\rangle_\rho$
  (§2.3), compare Favre-averaged model profiles with mostly
  Reynolds-averaged DNS data, the difference being negligible as recalled
  from Zhang et al. even at Mach 14 (§2.1), and infer the DNS $C_f$ from
  the printed $\rho_w$ and $u_\tau$ where the references do not list it
  (Table 2). The DNS data serve both for "a priori" diagnostics of the
  scalings (§3) and for the "a posteriori" check of the model (§4); see
  [turbulent boundary layers](/benchmarks/turbulent-boundary-layer.md).
- **Filtered DNS as training data and observations.** Kim et al. (2024,
  §4.2) train their [neural-network SGS models](/methods/neural-network-sgs-model.md)
  on box-filtered cylinder DNS at $Re_D=3900$ and test them against
  filtered DNS at $Re_D=5000$. Their grid-converged $Re_D=5000$ DNS gives
  $L_r/D=1.39$ and $C_D=1.01$, against 1.14 and 1.12 for the DNS of Aljure
  et al. and 1.40 and 1.02 from Norberg's experiments, all as printed in
  their Table 1 ($L_r$ the recirculation length, page-local). Wang et al.
  (2023c, §III) feed filtered DNS of forced isotropic turbulence and of a
  temporal mixing layer to their [ensemble Kalman calibration](/methods/ensemble-kalman-closure-calibration.md)
  as observations, with an observation noise set at machine level,
  uniform in $(-1,1)\times10^{-7}$, "of order $10^{-7}$ for a
  single-precision solver", because the observations come from DNS
  (Table II).

Chunk-6 sources use DNS in the same roles:

- **Reference data for field inversion.** [Fanizza et al. (2025)](/sources/fanizza-2025.md),
  §4, assimilate a time-averaged DNS of a laminar cylinder at $Re=80$
  computed on the same mesh, the DNS of a square cylinder at $Re=22000$ by
  Trias et al., and the DNS of an oblique shock/boundary-layer interaction
  at $M_\infty=2.28$ by Volpiani et al., the authors' own reference, into
  Spalart–Allmaras RANS (see [field inversion](/methods/field-inversion-machine-learning.md)).
- **Training data of learned LES.** Filtered pseudo-spectral DNS train and
  test the [neural-operator surrogates](/methods/neural-operator-les-surrogate.md)
  of Li et al. (2024, §V) and Zhao et al. (2025, §3), and filtered channel DNS
  the [super-resolution SGS model](/methods/super-resolution-sgs-model.md) of
  Maejima & Kawai (2025, §3–4), who stress that on very coarse grids the LES
  field differs from filtered DNS, so no paired training data exist (§1).
- **DNS out of reach.** [Löhrer & Fröhlich (2025)](/sources/lohrer-2025.md),
  §3.2–3.3, call DNS of their flexible aquatic canopy "not feasible due to
  excessive computational resources" and run a wall-resolved LES that, by a
  mean subgrid activity of 0.11, they call "close to a DNS" (App. C; see
  [large-eddy simulation](/definitions/large-eddy-simulation.md)).

Domingo & Vervisch (2023, §1) list DNS codes and orders: SENGA, DINO, S3D,
FK³, KARFS and HOLOMAC of sixth to tenth order; Nek5000 with spectral elements;
NGA, PsiPhi, AVBP and OpenFOAM of fourth or second order. They estimate the
carbon footprint of a 1.68-million-core-hour DNS at 776 kg CO$_2$e in France,
255 kg in Vancouver and 11,000 kg on coal electricity (§6), and judge that the
boundary between DNS and high-fidelity LES is "getting progressively blurred"
in combustion chambers, which are short and free of high-Reynolds-number wall
layers (§7).

## Qualifications

- The $h=2\eta$ criterion is the one Domingo & Vervisch (2023) adopt; other
  works use other criteria, and the sources of this chunk do not compare them.
- Dzanic et al. (2022, §3.2) print a spanwise spacing of $0.85\,\eta$; their
  grid has 96 spanwise degrees of freedom over a span of $\pi D$, i.e. a mean
  spacing of $0.0327D$, which is $2.97$ times the stated minimum $\eta=0.011D$.
  The printed ratio is not reproduced with the stated $\eta$, and the text does
  not say which $\eta$ it uses *(compiler check, not in the sources)*.
- Domingo & Vervisch (2023, §3.1) print 28.58 million nodes for a
  $12\times18\times18$ mm box at 50 µm, which a uniform count puts at about 31
  million; the paper does not say how nodes are counted *(compiler check,
  not in the sources)*.
- Cao et al. (2022, §3.4) print the resolved wavenumber as
  $\kappa_{max}=\sqrt2\kappa_0N/3$, here $k_{\max}=\sqrt2\,k_0N_x/3$ with
  the spectrum peak $k_0=8$ and $N_x$ cells per direction; their tabulated
  $k_{\max}\eta_0=3.613$ is reproduced by $\sqrt2N_x/3$ with $N_x=512$, not
  with the factor $k_0$ *(compiler check, not in the sources)*. The version read is the arXiv v1 preprint.
- Bernades et al. (2023) and Inagaki & Kobayashi (2023) compare their
  channel DNS with published DNS (the latter with Moser et al. and Abe et
  al. at $Re_\tau=395$); Bernades et al. compare their two schemes with each
  other only, against no external data.
- The single-precision conclusion of Wang et al. (2023b) rests on the
  arXiv v1 preprint, which also mislabels the memory ratio (double over
  single printed as single over double) and the number of GPUs of the coarse
  channel runs.
- Seta & Federrath (2022) justify their model-free runs by the ratio of
  explicit to numerical diffusion, and Pereira et al. (2021) their reference
  run by a grid study (App. B); neither states its grid spacing in Kolmogorov
  lengths, so the criteria above cannot be checked for them.
- **Single precision.** Wang et al. (2023b) conclude that single precision
  "may not be safe for DNS ... especially for time-evolutionary turbulent
  flows", from instantaneous profiles of channel flow; Yeung et al. (2025)
  run stationary isotropic DNS in single precision and judge the effect on
  their averaged small-scale statistics unlikely to be strong. The flows,
  quantities and arguments differ, and neither source tests the other's
  case, so no contradiction is recorded; a single- against double-precision
  comparison of dissipation-range statistics would decide it.
- **Shear-viscous compressible DNS.** Beattie et al. (2025) argue that
  without explicit bulk viscosity a compressible run is an implicit LES for
  the compressible modes. Seta & Federrath (2022), recorded above, justify
  their explicitly viscous compressible MHD runs as DNS by the ratio of
  explicit to numerical diffusion and do not state a bulk viscosity. Whether their runs are DNS in Beattie et al.'s sense depends
  on that unstated choice and on a resolution study of the compressible
  modes, so it is recorded here rather than as a contradiction.
- **Cost of a long $32\,768^3$ run.** With Yeung et al.'s figures, ten
  large-eddy times are $3\times10^6$ steps, about 1.2 years at 13 s per
  step, against "two years or more" in the text, which does not say what
  else the estimate includes *(compiler check, not in the sources)*.

# Citations

- [Domingo & Vervisch (2023)](/sources/domingo-2023.md) — §1 (quasi-DNS, codes, a priori caveat); §2, Eqs. (1)–(6); §3.1–3.2 (DNS embedded in LES, flame-resolved burner); §4; §5, Eqs. (13)–(21) (downsizing); §6–§7.
- [Dzanic et al. (2022)](/sources/dzanic-2022.md) — §1 (URDNS = ILES); §3.1; §3.2 (cylinder DNS resolution).
- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §6.1 (TGV DNS); §7.1 (pipe DNS, near-wall spacing).
- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) — §IV.B–C (DNS–inviscid error bound, convergence to DNS).
- [Goc et al. (2021)](/sources/goc-2021.md) — §1 (DNS accurate but prohibitive at high Reynolds number).
- [Beck & Kurz (2023)](/sources/beck-2023.md) — §IV A (DNS of forced isotropic turbulence).
- [Flad & Gassner (2017)](/sources/flad-2017.md) — §1 (pseudo-spectral reference DNS).
- [Krais et al. (2021)](/sources/krais-2021.md) — §2.2.2 (supersonic boundary-layer DNS).
- [Cao et al. (2022)](/sources/cao-2022.md) — §1 (finite-volume DNS, competing methods); §3.1–3.4, Tables 3, 5, 8 (gas-kinetic DNS, resolution criterion, cost).
- [Cogo et al. (2022)](/sources/cogo-2022.md) — §2, Table 1 (STREAmS, recycling–rescaling, resolution, $4\eta$ criterion).
- [Huang et al. (2022)](/sources/huang-2022.md) — §2.2–2.3, Table 2 (scheme, multi-box set-up); §3.1, Table 3 (induction length); App. A (grid check, validation).
- [Seta & Federrath (2022)](/sources/seta-2022.md) — §2.4 (explicit against numerical diffusion).
- [Pereira et al. (2021)](/sources/pereira-2021.md) — §IV.2 ($f_k=0$ reference run); App. B.
- [Gillyns et al. (2022)](/sources/gillyns-2022.md) — §2, §5–§9 (Lee & Moser DNS as reference; Gibbs spikes).
- [Carreño Ruiz & D'Ambrosio (2022)](/sources/carrenoruiz-2022.md) — §3.5, Table 5 (SD7003 DNS reference); §6.3, Fig. 19 (Eppler 387).
- [Knopp (2022)](/sources/knopp-2022.md) — §7.3 (Coleman et al. DNS as validation).
- [Dang et al. (2022)](/sources/dang-2022.md) — §1 (difficulties of compressible DNS); §2 (OpenCFD-SCU numerics); §5.1–5.3 (blowing/suction inflow, GPU performance); §6.1 (31.2-billion-point ramp DNS).
- [Helm & Martín (2022)](/sources/helm-2022.md) — §II (recycling–rescaling auxiliary box, Morkovin-scaled initialization); Tables I–II (boundary-layer DNS resolutions); §III B (filtered DNS as LES reference, unresolved energy); §V (cost ratio).
- [Fischer et al. (2022)](/sources/fischer-2022.md) — §2 (spectral elements); §4.1–4.2 (rod-bundle DNS, scaling on Summit).
- [Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md) — §III (pseudo-spectral isotropic DNS, filtered-DNS a priori data).
- [Kim et al. (2022)](/sources/kim-2022.md) — §II A (channel DNS numerics); §II–§III (filtered-DNS statistics as training targets).
- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — §4.1 (definition of DNS).
- [Davidovits et al. (2022)](/sources/davidovits-2022.md) — §II A (artificial-viscosity runs "not DNS", resolution check).
- [Kochurin et al. (2022)](/sources/kochurin-2022.md) — p. 2 (pseudo-spectral "DNS" with hyperviscosity and spectral cut-off).
- [Maeyama et al. (2022)](/sources/maeyama-2022.md) — Methods (closure-free gyrokinetic simulations, GKV performance).
- [Coelho et al. (2022)](/sources/coelho-2022.md) — p. 4–5 (global fluid simulation with numerical diffusion).
- [Bernades et al. (2023)](/sources/bernades-2023.md) — §4.3, Figs. 8–10 (transcritical channel DNS, resolution argument); §5.
- [Delassaux et al. (2023)](/sources/delassaux-2023.md) — HAL author manuscript: §4.1 (Spalart's forecast).
- [Foldes et al. (2023)](/sources/foldes-2023.md) — arXiv v2: §4.4, Figs. 10–12 (lattice Boltzmann against pseudo-spectral); §5 (GPU performance, Hall-MHD turnaround).
- [Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md) — arXiv v3: §III A, App. B (channel DNS, filtering).
- [Kou et al. (2023)](/sources/kou-2023.md) — §1 (implicit LES and under-resolved DNS used interchangeably).
- [Kurz et al. (2023)](/sources/kurz-2023.md) — arXiv v2: §3.5 (DNS spectrum as reward target).
- [Lederer et al. (2023)](/sources/lederer-2023.md) — arXiv v1: §4–5 (channel and periodic-hill DNS references).
- [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) — §2.3 (DNS database); §2.5 (training in the solver instead of filtered DNS).
- [Morsbach et al. (2024)](/sources/morsbach-2024.md) — §1 (cost scaling); §3.3 (DNS boundary layer as inflow template).
- [Saini et al. (2023)](/sources/saini-2023.md) — §3.1 (spectral DNS reference); Eqs. (16)–(19) (decay rate and viscous dissipation).
- [Sirignano & MacArt (2023)](/sources/sirignano-2023.md) — §3, Table 1 (prism DNS); §3.1, Eq. (3.2) (filtered DNS); §4.1.
- [Wang et al. (2023b)](/sources/wang-2023-b.md) — arXiv v1: §4.1, Tables 3–5 (GPU cost); §4.2, Tables 6–8, Figs. 10–14 (channel DNS, single against double precision); §5.
- [Zhao et al. (2023a)](/sources/zhao-2023.md) — arXiv v1: §5.2 (channel DNS reference).
- [Böttler et al. (2023)](/sources/bottler-2023.md) — arXiv v1: §1, §2.2 (detailed-chemistry flame reference; DNS of intrinsic instabilities restricted to academic configurations).
- [Chen et al. (2024)](/sources/chen-2024.md) — §2.1 (Favre against Reynolds averages of DNS data); §2.3 (DNS eddy viscosity); Table 1 (twelve compressible boundary-layer DNS as RANS reference); Table 2 (DNS $C_f$ inferred); §3–§4.
- [Domaradzki (2024)](/sources/domaradzki-2024.md) — §3.1, Fig. 4b (model-free run fails on the Comte-Bellot & Corrsin LES mesh).
- [Kim et al. (2024)](/sources/kim-2024.md) — §2.1 (kinetic-energy-conserving central scheme, immersed boundary); Table 1 (cylinder DNS at $Re_D=3900$ and 5000, grid convergence, references); §4.2 (filtered DNS as training data); App. D (channel DNS).
- [Pacciani et al. (2025)](/sources/pacciani-2025.md) — §6.1 (quasi-DNS of the LS89 cascade as recalled).
- [Prieto Saavedra et al. (2024)](/sources/prietosaavedra-2024.md) — §1 (implicit LES as under-resolved DNS); §3.2, App. B, Table B.6 (resolution between DNS and wall-resolved LES); Table 1 (periodic-hill DNS references).
- [Steinhausen et al. (2023)](/sources/steinhausen-2023.md) — arXiv v1: Abstract, §2.1 (DNS-like reacting channel simulation: grid, solver, cost).
- [van Gastelen et al. (2024)](/sources/vangastelen-2024.md) — arXiv v5: §4, App. E.1 (one-dimensional "DNS"); §4.3.2 (speed-up against it).
- [Wang et al. (2023c)](/sources/wang-2023-c.md) — arXiv v3: §III, Tables I–II (isotropic DNS, observation noise); §IV, Table III (mixing-layer DNS); App. B, Table V ($1024^3$ DNS).
- [Yeung et al. (2025)](/sources/yeung-2025.md) — §1 (Frontier, largest grid, cost of a long run, sub-Kolmogorov scales); §2.1–2.2, Table 1 (pseudo-spectral code, resolution pair, single precision, MRIS); §5 (cost scaling with $Re_\lambda$).
- [Chapelier et al. (2024)](/sources/chapelier-2024.md) — HAL hal-04582857v1: §II.C (TENO $2048^3$ reference, cost, non-converged dilatational peak); §III.B.d (NS3D); §IV.A.
- [Cao et al. (2024)](/sources/cao-2024.md) — arXiv 2107.08609v1: §1 (recalled $M_t$ limits); §3.3, Tables 4–5 ($160^3$ "DNS" and $128^3$ implicit LES of a compressible channel).
- [Beattie et al. (2025)](/sources/beattie-2025.md) — arXiv 2312.03984v4: §6.1–6.2 (compressible-mode pile-up); §9.1 (shear-viscous DNS as implicit LES of the compressible modes); App. D (resolution study).
- [Maejima & Kawai (2025)](/sources/maejima-2025.md) — §1; §2, Tables 1–2 (channel DNS at $Re_\tau\approx1000$ and 2000); §3–4.
- [Li et al. (2024)](/sources/li-2024.md) — arXiv 2403.16026v2: §V A–B (pseudo-spectral DNS of isotropic turbulence and a mixing layer as training data).
- [Zhao et al. (2025)](/sources/zhao-2025.md) — arXiv 2411.04502v3: §3.1–3.2 (pseudo-spectral DNS as training and reference data).
- [Fanizza et al. (2025)](/sources/fanizza-2025.md) — §4.1–4.3 (DNS references assimilated into RANS).
- [Löhrer & Fröhlich (2025)](/sources/lohrer-2025.md) — §3.2–3.3 (DNS not feasible); App. C (activity parameter).
