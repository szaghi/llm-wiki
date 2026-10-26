---
type: Method
title: "STITCH helicity-condensation model"
description: "STITCH replaces explicitly resolved photospheric vortical driving in coronal MHD simulations by one source term in the induction equation that injects condensed magnetic helicity at the base; it is divergence-free, leaves the normal field unchanged, and cuts the cost of energy buildup about fifteenfold."
status: established
aliases: [STITCH, STatistical InjecTion of Condensed Helicity, helicity-condensation source term, statistical helicity injection]
tags: [mhd, astrophysics, plasma, sgs-model]
timestamp: 2026-10-26T05:06:00Z
---

# STITCH helicity-condensation model

**STITCH** (STatistical InjecTion of Condensed Helicity) is a parametrized
source term added to the induction equation of an MHD simulation of the solar
corona. It represents the large-scale outcome of **helicity condensation**:
small, unresolved, same-sense vortical (cyclonic) cells at the photosphere
twist the coronal field, reconnection between neighbouring cells cancels the
twist between them, and an inverse cascade of magnetic helicity carries the
twist flux to the boundaries of the flux system, where it accumulates as
large-scale magnetic shear. [Dahlin et al. (2022)](/sources/dahlin-2022.md)
name the term, give a flux-based discretization for finite-volume MHD codes,
and test it against simulations that resolve the cyclonic cells (§1–§7); the
term itself was derived earlier by Mackay et al. (2014, Eq. A1) for a
magnetofrictional model, as recalled by Dahlin et al. (2022, §2).

The authors call STITCH a "subgrid-scale model", but it is **not an LES
closure** in this bundle's sense: there is no filter, no
[subgrid stress](/definitions/large-eddy-simulation.md) and no subgrid
electromotive force derived from one. It is a boundary source term — an
injected electric field at the base of the atmosphere — whose single
parameter stands for unresolved photospheric driving together with the
reconnection cascade it triggers. Its closest relative in the bundle, the
[subgrid turbulent dynamo model](/methods/subgrid-turbulent-dynamo-model.md),
also acts through the induction equation, but that one closes a
grid-filtered electromotive force in the volume.

Page-local notation: subscripts $n$ and $s$ denote the components normal and
parallel (horizontal) to the solar surface, with $\nabla_s$ and $\nabla_n$
the corresponding gradients ($n=x$ in Cartesian, $n=r$ in spherical
geometry); $\boldsymbol A_s$ is the horizontal part of the vector potential
$\boldsymbol A$; $\mathcal Z$ is the STITCH parameter (the source writes
$\zeta$, which the registry reserves for the Elsasser potentials); $a_c$ and
$\Omega_c$ are the radius and angular rotation rate of a cyclonic cell;
$H_r$ is the relative magnetic helicity and $d\sigma$ the surface element;
PIL is a polarity inversion line (where $B_n$ changes sign). Gaussian units
(G, cm) as in the source.

## The source term

Dahlin et al. (2022, §2, Eq. 1) add to the induction equation

$$\frac{\partial\boldsymbol B}{\partial t}=\nabla\times\frac{\partial\boldsymbol A_s}{\partial t}=-\nabla\times\nabla_s\left(\mathcal Z B_n\right),$$

with the single parameter (Eq. 2)

$$\mathcal Z=\tfrac12\left\langle a_c^2\,\Omega_c\right\rangle,$$

where the angle brackets denote a local space–time average over many cells
(units cm$^2$ s$^{-1}$). Two assumptions underlie it (§2): the cyclonic cells
are small, numerous and nominally identical, though their properties may
vary on large scales; and reconnection between cells is efficient enough
that oppositely directed twist fields cancel algebraically. In practice the
helicity is injected over the bottom layer of grid cells, as in the earlier
magnetofrictional uses (Mackay et al. 2014, 2018; Lynch et al. 2021, as
recalled, §7). The authors read the term as "adjusting the electric field,
i.e. modifying Ohm's law in the coronal plasma, at the base of the
atmosphere" (§7); field changes are strongest where $\mathcal ZB_n$ varies
most rapidly across the surface, that is, at the boundaries of flux systems.

They state that STITCH represents generically the outcome of an inverse
helicity cascade from any helicity-injecting mechanism — vortical or shearing
motions, flux emergence, cancellation — not only convective vortices
(§1, §7).

## Properties

Derived by Dahlin et al. (2022, §2, Eqs. 3–6):

- **Solenoidal by construction.**
  $\partial_t\nabla\cdot\boldsymbol B=-\nabla\cdot[\nabla\times\nabla_s(\mathcal ZB_n)]=0$,
  "subject only to the requirement that [$\mathcal ZB_n$] be sufficiently
  smooth (i.e., differentiable) everywhere" (Eq. 3; the source writes
  $\zeta$).
- **Normal field unchanged.**
  $\partial_tB_n=-\hat{\boldsymbol n}\cdot\nabla_s\times\nabla_s(\mathcal ZB_n)\equiv0$
  (Eq. 4), so the photospheric flux distribution — the quantity observations
  constrain — is untouched.
- **Horizontal field.**
  $\partial_t\boldsymbol B_s=-\nabla_n\times\nabla_s(\mathcal ZB_n)=+\nabla_s\times\nabla_n(\mathcal ZB_n)$
  (Eq. 5), valid in spherical and Cartesian coordinates.
- **Helicity injection.**
  $$\frac{dH_r}{dt}=-2\iint\mathcal Z\,B_n^2\,d\sigma$$
  (Eq. 6), required for consistency with helicity conservation through
  reconnection and transport of twist flux; the derivation is deferred to
  Mackay et al. (2014).

## Discretization

On a grid whose horizontal coordinates $s_1$, $s_2$ satisfy
$\hat{\boldsymbol s}_1\times\hat{\boldsymbol s}_2=\hat{\boldsymbol n}$, the
term is applied as changes of magnetic flux $\Phi_{s_1}$, $\Phi_{s_2}$
(page-local) through the vertical cell faces (§2, Eqs. 7–14). With the
coronal base at $n=n_0$ and $\mathcal Z$ set to vanish at the top of the
first layer of cells $n=n_1$, integration over $n$ gives

$$\frac{\partial\Phi_{s_1}}{\partial t}=-\mathrm D_{s_2}\!\left(\mathcal ZB_n\big|_{n_0}\right),\qquad \frac{\partial\Phi_{s_2}}{\partial t}=+\mathrm D_{s_1}\!\left(\mathcal ZB_n\big|_{n_0}\right)$$

(Eqs. 11–12), where $\mathrm D_{s_1}$, $\mathrm D_{s_2}$ (page-local; the
source writes $\Delta_{s_1}$, $\Delta_{s_2}$) are finite differences of
vertex values along $s_1$, $s_2$. The field update divides by the face areas
$\mathcal A_{s_1}$, $\mathcal A_{s_2}$ (page-local; the source writes
$A_{s_1}$, $A_{s_2}$),
$\partial_tB_{s_1}=-\mathrm D_{s_2}(\mathcal ZB_n|_{n_0})/\mathcal A_{s_1}$ and
$\partial_tB_{s_2}=+\mathrm D_{s_1}(\mathcal ZB_n|_{n_0})/\mathcal A_{s_2}$
(Eqs. 13–14), and is multiplied by the time step. Each vertex value enters
the four side faces of a cell twice with opposite signs, so the net flux
change through the cell vanishes: the scheme is a **discrete Gauss law**,
the discrete form of Eq. (3).

The authors give a five-step recipe they state applies to "any of the MHD
codes presently used by the space science community" (§7): assign
$\mathcal Z$; evaluate $\mathcal ZB_n$ at $n=n_0$; difference along the two
horizontal coordinates with the curl signs; divide by the vertical face
areas; multiply by the time step.

**Spatial tailoring.** $\mathcal Z(\boldsymbol x)$ may be restricted to one
polarity or to a region; smooth results require $\mathcal ZB_n\to0$ smoothly
at the boundary of that region (§5, §7). The localized profile used is (§5,
Eq. 15)

$$\mathcal Z=\mathcal Z_0\cos\!\left(\pi\frac{\phi-\phi_0}{\phi_w}\right)\cos\!\left(\pi\frac{\psi-\psi_0}{\psi_w}\right),$$

with $\phi$ longitude and $\psi$ latitude (page-local), centre
$(\phi_0,\psi_0)$ and widths $(\phi_w,\psi_w)$.

## Tests against resolved driving

All runs use the adaptive-mesh code ARMS (DeVore & Antiochos 2008, as
recalled) in spherical geometry, solving the ideal MHD equations, on an
embedded-bipole active region: an elliptical bipole at 22.5° N with peak
$|B_r|\approx50$ G in a 10 G background dipole, with a separatrix dome and a
3D null; a spherically symmetric hydrostatic atmosphere with an inverse-$r$
temperature profile and base temperature $2\times10^6$ K, evolved with an
adiabatic temperature equation (§3). Grid resolutions are not given. The reference is a
**full helicity condensation** (FHC) run with 107 explicitly resolved
cyclonic cells in the minority polarity, maximum surface speed about
50 km s$^{-1}$ (configuration of Dahlin et al. 2019, as recalled).

| Quantity (§3–§4) | FHC | STITCH, uniform $\mathcal Z_0=1.4\times10^{16}$ cm$^2$ s$^{-1}$ |
|---|---|---|
| Energy buildup until eruption | $\approx90{,}000$ s | $\approx6{,}000$ s |
| Computing time | "approximately two continuous months" | "approximately four days" |
| Stored magnetic energy $E_M/E_{M0}$ (page-local) | $\approx1.20$ | $\approx1.24$ |
| Energy released, $\Delta E_M/E_{M0}$ | $0.10$ | $0.04$ |
| Release time scale | $\approx4{,}000$ s | $\approx1{,}000$ s |
| Peak shear proxy $\lvert B_\phi\rvert_{\max}$, before/after eruption | 70/70 G | 110/80 G |

- **Qualitative agreement.** Both runs form a low-lying, highly sheared
  filament channel under weakly sheared overlying field and erupt it as a
  breakout CME with $V>1000$ km s$^{-1}$ (§4, Fig. 3).
- **Cost.** Lower by "a factor of 15", matching the reduction in driving
  time; the saving comes from sub-Alfvénic flux injection replacing subsonic
  vortical driving, and a further saving from coarser grids was "not
  exploited" (§4, §7).
- **Quantitative differences.** STITCH stores "some 20%" more free energy and
  releases less of it, faster (release rate higher "by a factor of
  0.4*4.0 = 1.6", §4). The authors attribute the differences to geometry: uniform-$\mathcal Z$
  STITCH injects shear only in a zone of width $|B_r|/|\nabla_sB_r|$
  next to the PIL, while the FHC channel cannot be narrower than a cell
  diameter $2a_c$; in these runs the two widths are comparable, so the
  overlying loops acquire shear under FHC but not under STITCH (§4).
- **Injected field.** With $\mathcal Z_0=1.4\times10^{16}$ cm$^2$ s$^{-1}$ the
  maximum injection rate is about 1 G s$^{-1}$, but Alfvén waves redistribute
  the field along the channel and the maximum tangential field is about
  100 G, roughly twice the peak radial field of the minority polarity (§3).
- **Localized driving** (§5, Figs. 5–7). Eq. (15) with $\phi_0=0^\circ$,
  $\psi_0=22.5^\circ$, $\phi_w=22.5^\circ$, $\psi_w=11.25^\circ$ energizes
  and erupts one segment of the PIL only; gradients of $\mathcal Z$ spread
  some injection into the polarity interior and impart reversed shear near
  the centre.
- **Complex polarity inversion line** (§6, Figs. 8–9). A synthetic active
  region of 30 random subsurface dipoles with a corrugated PIL, driven with
  $\mathcal Z_0=5\times10^{15}$ cm$^2$ s$^{-1}$, $\phi_w=45^\circ$,
  $\psi_w=27^\circ$ in both polarities, erupts after some 15,000 s with no
  geometry-specific construction of the driver.

The authors propose STITCH for event-based, data-driven CME modelling and
space-weather prediction, as an alternative to flux emergence, imposed
shear flows, flux cancellation and flux-rope insertion, all of which they
describe as difficult to match to observed normal flux and complex PILs
(§7).

## Qualifications

- **Regime not tested.** STITCH is meant for cells much smaller than the
  channel width; the FHC reference has the two comparable. The authors'
  statements that the two methods should agree better, and the cost ratio
  grow, in the true subgrid regime are not simulated (§4). The evidence is
  one FHC run against single-resolution STITCH runs, with no grid-convergence
  study.
- **Validation reference.** The reference is another simulation (FHC), not
  observation or a converged solution.
- **Version read.** The claims are those of the arXiv v1 submitted draft;
  the published version may differ.
- **Printed figures.** The text states that the storage rate is "just over
  15× faster" for STITCH. *(Compiler check, not in the sources: from the
  printed energy gains, $0.24$ and $0.20$ of $E_{M0}$, and buildup times,
  6,000 s and 90,000 s, the mean storage-rate ratio is
  $(0.24/6000)/(0.20/90000)=18$, while the ratio of the buildup times is
  $90000/6000=15$.)* The text attributes its figure to the rate curves of
  Fig. 4b (§4). Eq. (15) is
  printed without saying whether $\mathcal Z$ is truncated to the central
  lobe of the cosines, where both factors are positive.

# Citations

- [Dahlin et al. (2022)](/sources/dahlin-2022.md) — §1; §2, Eqs. (1)–(14); §3; §4, Figs. 3–4; §5, Eq. (15), Figs. 5–7; §6, Figs. 8–9; §7.
