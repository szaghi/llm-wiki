---
type: Definition
title: "Direct numerical simulation"
description: "DNS solves the Navier–Stokes equations with no turbulence model and a grid fine enough for the dissipative range; this page gives its resolution criteria and cost scalings, the weaker quasi-DNS and DNS-embedded-in-LES variants, and its role as reference data for closure development."
status: established
aliases: [DNS, quasi-DNS, flame-resolved DNS, under-resolved DNS, DNS embedded in LES, downsized DNS]
tags: [dns, les, combustion, boundary-layer, compressible]
timestamp: 2026-10-25T13:42:00Z
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

From their pipe DNS, Vicente Cruz & Lamballais (2023, §7.1) suggest that the
recommendation of about one wall unit for the first wall-normal spacing
"may be somewhat over-demanding".

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
  second moments that they attribute to aliasing (§3.1).
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

# Citations

- [Domingo & Vervisch (2023)](/sources/domingo-2023.md) — §1 (quasi-DNS, codes, a priori caveat); §2, Eqs. (1)–(6); §3.1–3.2 (DNS embedded in LES, flame-resolved burner); §4; §5, Eqs. (13)–(21) (downsizing); §6–§7.
- [Dzanic et al. (2022)](/sources/dzanic-2022.md) — §1 (URDNS = ILES); §3.1; §3.2 (cylinder DNS resolution).
- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §6.1 (TGV DNS); §7.1 (pipe DNS, near-wall spacing).
- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) — §IV.B–C (DNS–inviscid error bound, convergence to DNS).
- [Goc et al. (2021)](/sources/goc-2021.md) — §1 (DNS accurate but prohibitive at high Reynolds number).
- [Beck & Kurz (2023)](/sources/beck-2023.md) — §IV A (DNS of forced isotropic turbulence).
- [Flad & Gassner (2017)](/sources/flad-2017.md) — §1 (pseudo-spectral reference DNS).
- [Krais et al. (2021)](/sources/krais-2021.md) — §2.2.2 (supersonic boundary-layer DNS).
