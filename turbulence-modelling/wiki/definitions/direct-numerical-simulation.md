---
type: Definition
title: "Direct numerical simulation"
description: "DNS solves the Navier–Stokes equations with no turbulence model and a grid fine enough for the dissipative range; this page gives its resolution criteria and cost scalings, the discretizations used for it, the set-up of spatially developing compressible boundary layers, weaker variants, and its role as reference data for closure development."
status: established
aliases: [DNS, quasi-DNS, flame-resolved DNS, under-resolved DNS, DNS embedded in LES, downsized DNS]
tags: [dns, les, combustion, boundary-layer, compressible, hypersonic]
timestamp: 2026-10-25T19:47:00Z
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
within 1.9% and 1.7% (App. A). These DNS are the data against which
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
  use "implicit LES (ILES) or under-resolved DNS (URDNS)" as synonyms and use it
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
internal to the wall model.

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
- Seta & Federrath (2022) justify their model-free runs by the ratio of
  explicit to numerical diffusion, and Pereira et al. (2021) their reference
  run by a grid study (App. B); neither states its grid spacing in Kolmogorov
  lengths, so the criteria above cannot be checked for them.

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
