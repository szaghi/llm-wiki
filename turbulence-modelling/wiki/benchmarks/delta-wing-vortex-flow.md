---
type: Benchmark
title: "Delta-wing and concentrated vortex flows"
description: "Separation-induced vortices of swept wings and aircraft (sharp and blunt delta wings, the AVT-183 diamond wing, vortex breakdown on the AVT-080 wing, SACCON, CAWAPI F-16XL, X-31, AVT-316): RANS predicts coherent sharp-edge vortices, while secondary vortices, blunt-edge onset, breakdown and hysteresis remain unanchored and favour hybrid RANS/LES with adaptive meshes."
status: established
aliases: [delta wing, delta-wing vortex flow, concentrated vortex flow, leading-edge vortex, vortex breakdown, blunt-leading-edge vortex separation, VFE-2, VFE-2 65° delta wing, AVT-183 diamond wing, AVT-080 delta wing, SACCON, CAWAPI, F-16XL, X-31, AVT-316 triple delta wing]
tags: [benchmark, separated-flow, hybrid-rans-les, des, mesh-adaptation, rans]
timestamp: 2026-10-28T17:05:00Z
---

# Delta-wing and concentrated vortex flows

A swept leading edge at incidence sheds its boundary layer into a free
shear layer that rolls up into a concentrated vortex above the wing; the
vortex induces high-speed spanwise flow and low pressure on the upper
surface, the nonlinear "vortex lift" that slender wings exploit. The same
mechanism appears on strakes, leading-edge extensions, nacelle strakes,
vortex generators and chined forebodies. On a **sharp** leading edge the
separation line is fixed by the geometry; on a **blunt** edge the vortex
starts somewhere down the edge, at a place set by the incidence, Mach
number, Reynolds number, bluntness, camber and roughness, which the
turbulence and transition modelling must predict. On this page $\Lambda$
is the leading-edge sweep, $\alpha$ the angle of attack, $r_{\mathrm{le}}$
the leading-edge radius and $Re_{\mathrm{mac}}$, $Re_{c_r}$ the Reynolds
numbers on the mean aerodynamic and the root chord (all page-local). The
sole source is the capability survey of
[Luckring & Rizzi (2024)](/sources/luckring-2024.md), built from the
authors' experience and a literature database of "over 6000 articles
spanning approximately 20 years"; it computes nothing and reproduces its
evidence from the cited studies.

## Classification of concentrated vortex flows

[Luckring & Rizzi (2024)](/sources/luckring-2024.md), §2.1, class these
flows for the survey by their unsteadiness and coherence:

- *steady* (unsteadiness no larger than that of attached-flow turbulence)
  or *unsteady*;
- *coherent* (a stable vortex with steady structure), *semicoherent*
  (instability and unsteadiness inside an organized, still stationary
  vortex) or *incoherent vorticity* (no organized vortex, as in a bluff-body
  wake); a vortex can pass from coherent to semicoherent at breakdown or
  under shear-layer instability and then to incoherent vorticity.

They call a formulation *anchored* for a new prediction when it has "some
degree of pedigree (historical applications, calibration history,
validation history)", and use the verification, validation, prediction and
calibration definitions of the AIAA and ASME guides. They also place the
vortices on a systems-engineering scale: subcomponent (vortex generators,
for flow control), component (strakes), subsystem (lifting surfaces) and
configuration (§2.1, Fig. 18).

## Flow physics the models must reproduce

The survey's account of the elemental physics (§2.3), all from cited work:

- **Sharp-edge primary vortex.** Its properties depend on geometry,
  incidence and Mach number, "Reynolds number is less influential". The
  core has an outer inviscid rotational region and an inner viscous
  subcore whose extent falls with Reynolds number; in the conical model of
  Hall and of Stewartson & Hall the circumferential velocity is of the
  order of the free stream and the axial velocity approaches three times
  it (§2.3.1.1, Fig. 21). The vortex sheet can carry steady helical
  Kelvin–Helmholtz subvortices (Fig. 22).
- **Secondary separation.** The spanwise flow under the primary vortex
  meets a favourable then an adverse pressure gradient and separates into
  a counter-rotating secondary vortex, which changes the strength and
  position of the primary one; whether the secondary separation is laminar
  or turbulent matters (Hummel, as cited), and tertiary vortices sometimes
  appear (§2.3.1.2).
- **Blunt-leading-edge separation.** Two structures absent on a sharp
  edge appear: an incipient-separation region upstream of the vortex
  origin, resembling leading-edge-bubble physics, and an inner vortex of
  the same sense as the primary one, explained (Hitzel et al., as cited) by
  the collision of the vortex-induced inboard reattached flow with the
  outboard attached flow (§2.3.1.2, Figs. 25, 30). By Luckring's analysis,
  as cited, higher incidence and Mach number promote the vortex
  separation, larger bluntness and Reynolds number delay it. Polhamus's
  separation classes and Poll's three formation mechanisms (full-span
  roll-up, part-span vortices behind short bubbles) connect it to the
  [laminar separation bubble](/definitions/laminar-separation-bubble.md).
  On Poll's $56^\circ$ wing ($r_{\mathrm{le}}/c=1.2\%$, aspect ratio 2.68,
  $M=0.1$), raising the Reynolds number from $1.4\times10^6$ to
  $2.7\times10^6$ replaced the full-span vortex by attached flow with a
  short bubble near mid-span (Fig. 29).
- **Unsteady states.** Vortex breakdown is an abrupt axial deceleration
  into reversed, fluctuating flow, in spiral or bubble form, moving
  upstream with incidence and occurring at lower incidence for lower sweep;
  nonslender wings add vortex wandering, unsteady shear-layer roll-up and
  dual primary vortices; pitching wings show hysteresis and dynamic lift,
  breakdown lagging its static position on the upstroke and downstroke
  (§2.3.2; see [dynamic stall](/definitions/dynamic-stall.md)).

## Modelling levels as the survey ranks them

| Level | What the survey states | Locator |
|---|---|---|
| [DNS](/definitions/direct-numerical-simulation.md) | grid points scale as $Re_L^{9/4}$, cost "approximately with the cube of Reynolds number"; "virtually impossible for flight conditions" | §2.4.1, §2.4.1.1 |
| wall-resolved [LES](/definitions/large-eddy-simulation.md) and [implicit LES](/definitions/implicit-les.md) | high-order runs (AFRL FDL3DI) capture separation bubbles, transition and shock-induced separation that RANS and hybrids do not report, but are "currently restricted to low Reynolds numbers (on the order of $10^4$)" | §3.1.1.2, §4.1.1 |
| steady and unsteady RANS | predict coherent sharp-edge vortices well; eddy-viscosity models work "as long as only one component of the Reynolds stress tensor is significant" | §2.4.1.3, §3.1.1.1 |
| [wall-modelled LES](/methods/wall-modelled-les.md) | resolves the outer boundary layer and detached shear layers; no application to concentrated vortex flows was known to the authors | §2.4.1.4–2.4.1.5 |
| [hybrid RANS/LES](/definitions/hybrid-rans-les.md) | needed for "flows with significant unsteady separated flow"; better than RANS at blunt-edge onset and than URANS on the triple delta | §2.4.1.4, §3.1.1.2, §3.2.3.5 |
| [lattice Boltzmann](/methods/lattice-boltzmann-method.md) | used on landing-gear doors and nacelle strakes; still needs a subgrid model at high Reynolds number | §2.4.1.6 |

The DES length the survey gives is $\min(d,C_{\mathrm{DES}}\Delta)$ with
$C_{\mathrm{DES}}=0.65$, $\Delta$ "the diameter of the cell" (§2.4.1.4; see
[detached-eddy simulation](/methods/detached-eddy-simulation.md)). The
F-15E at $\alpha=65^\circ$ ($M=0.3$, $Re_c=13.6\times10^6$) is their
example of the hybrid need: URANS shows no significant unsteadiness and
virtually no vorticity over the wing, where the hybrid resolves it
(Fig. 51).

## Fundamental cases

**Hummel's $AR=1$ sharp delta wing** ($M\approx0.1$, $Re_{c_r}=2\times10^6$,
$\alpha=20.5^\circ$, experiment): the reference for the secondary vortex,
the trailing-edge wake vortex and vortex lift; the laminar thin-layer
Navier–Stokes computation of Thomas et al. (1987) already correlated well
(§2.3, §3.1.1.1).

**The VFE-2 $65^\circ$ delta wing** (NASA National Transonic Facility,
sharp and blunt edges): RANS with several
[$k$-$\omega$ models](/methods/k-omega-model.md) (Schiavetta et al.,
$M=0.4$, $Re_{\mathrm{mac}}=6\times10^6$) predicts the coherent vortex and
the turbulent secondary vortex, the correlation degrading toward the
trailing edge (Fig. 54); for the blunt edge at $\alpha=13.3^\circ$ a DLR TAU
RANS reproduces the inner vortex, the vortex starting about halfway down
the edge, but "little was established for the details of the incipient
separation region", and the correlation with experiment varied among the
participants (§3.1.1.2, Fig. 57).

**The AVT-183 $53^\circ$ diamond wing** (NACA 64A006 section, Technische
Universität München low-speed tunnel, $M=0.15$, $Re_{\mathrm{mac}}=2.7\times10^6$,
$\alpha=12^\circ$), designed as a unit problem for the vortices of SACCON
(§3.1.1.2, Figs. 58–64):

- with USM3D RANS, Frink et al. find that the extrapolated primary
  reattachment line and the minimum suction under the primary vortex meet
  the minimum leading-edge pressure inside the incipient-separation
  region, supporting Luckring's criterion that this minimum approximates
  the vortex origin (Fig. 62);
- ZDES (Deck & Luckring) and RANS predict the overall flow well when the
  predicted onset matches the experiment, but predicting that onset "is not
  well established", and the hybrid RANS/LES "appear to have done better
  than RANS methods" (§4.1.1);
- with free transition (DLR TAU with the SST-$\gamma$-$Re_\theta$ model of
  [local-correlation-based transition](/methods/local-correlation-based-transition-model.md))
  the whole blunt-edge structure moves upstream and a laminar separation
  bubble appears ahead of the incipient separation, showing the importance
  of tripping at subscale tunnel Reynolds numbers (Buzica & Breitsamter,
  Figs. 63–64).

**Vortex breakdown on the AVT-080 $70^\circ$ delta wing.** "At the time of
this review, there is no reliable prediction technique for vortex
breakdown" (§4.1.2). The most promising predictions came from hybrid
RANS/LES, among them Morton's Spalart–Allmaras DES with
[adaptive mesh refinement](/methods/mesh-adaptation.md) at $M=0.07$,
$Re_c=1.56\times10^6$, $\alpha=27^\circ$, an example of the authors'
statement that meshes adaptive "both in space and time, are necessary"
(§2.4.2, §3.1.2.1, Fig. 53). A hybrid of the full-span wing at $M=0.6$,
$\alpha=30^\circ$ (Nonomura et al.) shows transient asymmetric breakdown,
so full-span simulations may be required. A RANS breakdown study at
$\Lambda=70^\circ$, $M=0.16$, $Re_{c_r}=1.97\times10^6$, $\alpha=35^\circ$
(Görtz) and Visbal's laminar pitch ramp of a $75^\circ$ wing ($25^\circ$ to
$50^\circ$, $M=0.2$, $Re_{c_r}=9.2\times10^3$, 1.2 to 2.3 million points),
which captured the breakdown lag, complete the cases. The survey found no
demonstrated capability to simulate the hysteresis of slender or
nonslender wings under dynamic motion (§4.1.2), and proposes breakdown in
tubes, with the DNS of shock-induced breakdown of Zhang, Zhang & Shu, as a
validation forum transferable to wings (§3.1.2.1).

**Shear-layer instability on semi-infinite and nonslender wings.**
High-order wall-resolved computations (FDL3DI) of a semi-infinite $75^\circ$
sharp delta at $M=0.1$, $\alpha=25^\circ$, $Re_L=25\times10^3$ to
$50\times10^3$ (on the length from the apex, page-local) show that beyond a
critical Reynolds number unsteady substructures appear in the shear layer
and move toward the apex as $Re_L$ rises, which the survey attributes to
unsteady boundary-layer separation and vorticity infusion; a $50^\circ$
nonslender wing ($Re_L=26\times10^3$, $\alpha=15^\circ$) breaks down
conically, without spiral winding or mean reversed flow, with periodic
core wandering (§3.1.2.1, Figs. 55, 73–74).

## Configurations

**SACCON** (uninhabited combat air vehicle, AVT-161; $\Lambda=53^\circ$,
$M=0.144$, $Re_{c_{\mathrm{ref}}}=1.6\times10^6$, $\alpha=16.83^\circ$ and
$17.39^\circ$; forced pitch oscillation $15^\circ\pm5^\circ$): RANS from
"well-established codes using well-established turbulence models" gives
significantly different vortex flows at the incidences where the pitch
stability changes rapidly; under forced oscillation neither the
[Spalart–Allmaras model](/methods/spalart-allmaras-model.md) nor
[$k$-$\omega$ SST](/methods/k-omega-sst-model.md) correlates well, SA
being closer (§3.2.3.2, Figs. 84–88; see
[model-form uncertainty](/definitions/model-form-uncertainty.md)).

**CAWAPI, the F-16XL in flight** ($\Lambda=70^\circ/50^\circ$; flight
condition FC-07 at $M=0.304$, $Re_{c_{\mathrm{ref}}}=44.4\times10^6$,
$\alpha=11.9^\circ$; FC-25 at $M=0.24$, $32\times10^6$, $19.8^\circ$):
RANS predicts the primary suction peak of FC-07 well and gives reasonable
boundary-layer rake profiles (Figs. 46–47); the standard deviation among
the CFD solutions at the high incidence was "three times that of the
moderate-angle-of-attack case"; in CAWAPI-2, Elmiligui et al. improved the
secondary vortex with a [$k$-$\varepsilon$ model](/methods/k-epsilon-model.md)
and grid refinement, the authors arguing that SA "fails to predict
secondary separation because it does not transport the right quantities";
in CAWAPI-3 the one-standard-deviation pressure bands of hybrid RANS/LES
bracket the flight data (§3.2.3.3, Figs. 90–91).

**X-31** ($\Lambda=57^\circ/45^\circ$, $M=0.18$, $Re_{c_{\mathrm{ref}}}=2.07\times10^6$,
$\alpha=16^\circ$ to $20.08^\circ$): DLR TAU with SA (about 50 million
cells) and NLR ENSOLV with a turbulent/non-turbulent $k$-$\omega$ model
(about 31 million) produce significantly different wing vortex flows;
modelling the leading-edge flap gaps produces a succession of vortices and
improves the pitching moment (§3.2.3.4, Figs. 93–94).

**AVT-316**: on the OTC1 missile ($M=1.4$, $Re_D=4.89\times10^6$, total
incidence $15^\circ$, roll $2.5^\circ$) FUN3D with SA plus rotation
correction and quadratic constitutive relation and Niceflow with SA plus
rotation correction differ on adapted grids; on the triple delta wing
(URANS at $M=0.85$, $Re_{c_{\mathrm{ref}}}=12.53\times10^6$,
$\alpha=20^\circ$; ISIS-CFD with anisotropic Hessian adaptation at
$M\approx0$, $2.36\times10^6$, $\alpha=24^\circ$, sideslip $5^\circ$) mesh
adaptation was needed to resolve the interacting vortices and hybrid
RANS/LES gave more reliable results than URANS (§3.2.3.5, Figs. 97–98).

**Vortex generators and strakes.** One vortex-generator height downstream,
the resolved-generator approaches of Zastawny (DLR TAU, $M=0.85$,
$Re_{\mathrm{mac}}=5.3\times10^6$) still show a concentrated vortex while
the modelled-generator approach has dissipated it; at five heights all
have, which was considered numerically induced; the survey found "no
evidence of an anchored simulation capability for concentrated vortex
flows from vortex generators" (§3.2.1.2, Fig. 76). Nacelle-strake studies,
lattice Boltzmann on the [NASA CRM high-lift](/benchmarks/nasa-crm-high-lift.md)
configuration and RANS on the DLR F11, report strake-on and strake-off
effects without correlating the strength, trajectory or persistence of the
strake vortex with experiment (§3.2.2.2, Figs. 78–80).

## What the survey concludes

- Steady coherent vortices from sharp-edged slender wings are predicted
  well, often by RANS; "little to no correlation between simulation and
  physical experiments was found for secondary vortex flow features"
  (§3.1.1.2), and blunt-edge onset, breakdown, nonslender-wing
  unsteadiness, hysteresis and vortex persistence behind generators and
  strakes are not anchored (§4).
- Adaptive mesh refinement, time-accurate for breakdown, is "effectively"
  a requirement, and grid convergence must resolve the core and shear-layer
  substructures (§2.4.2, §5.3.2).
- Cost: following Larsson et al., the inner-layer points of an LES of an
  attached airfoil rise about two orders of magnitude per decade of
  Reynolds number (see [NACA 0012](/benchmarks/naca-0012-airfoil.md) and
  [grid-point requirements of LES](/results/les-grid-point-requirements.md));
  scaling the wall-resolved LES of a C-130-like afterbody (210 million nodes
  at $Re_D=0.2\times10^6$) to flight ($Re_D=7.4\times10^6$) gives about 143
  billion nodes by the authors' estimate (§3.1.1.2). An F-35-based estimate
  they cite puts the CFD programme at about 20 times the cost of a wind
  tunnel programme, and supercomputer speed now grows at about half the
  Moore's-law rate, which delays the projected Zflop/s and Yflop/s
  machines by 16 and 26 years (§5.1, Tables 2–3).
- Recommended: combined tunnel and CFD programmes, open military
  configurations in the style of the drag and high-lift prediction
  workshops, unit-problem experiments (core flow, secondary separation,
  breakdown in tubes, generator and strake vortex persistence, incipient
  separation by high-order wall-resolved LES), GPU solvers, comparisons of
  adaptation methods, reassessment of turbulence models for vortical flows,
  and wall-resolved LES data to train reduced-physics methods; machine
  learning in turbulence modelling (Singh et al., Duraisamy et al., as
  cited) "does not include concentrated vortex flow assessments" (§5).

## Qualifications

- Every result on this page is reproduced from a cited study; the survey
  gives no error metrics and computes nothing beyond cost estimates. The
  model rankings it reports (a $k$-$\varepsilon$ model with grid refinement
  improving the secondary vortex on CAWAPI-2; SA closer than SST on
  SACCON's forced oscillation) each come from one configuration
  (§3.2.3.2–3.2.3.3).
- The survey equates LES that resolves the wall with "wall-resolved LES",
  and calls the same FDL3DI computations wall-resolved LES in captions and
  high-order implicit LES in the text (§2.4.1.2, §3.1.2.1). It states that
  wall-resolved LES is restricted to Reynolds numbers of order $10^4$
  (§4.1.1) while it reports such runs at $Re_c=0.2\times10^6$ (the
  FDL3DI aspect-ratio-4 NACA 0012 wings) and at $Re_c=10^6$ (the NACA 0012
  at $M=0.4$, 267 million nodes) (§3.1.1.2).
- It writes that the second-moment closures incorporate anisotropy and
  extra strains "exactly", and in the same passage that their
  pressure–strain, diffusion and dissipation terms must be modelled
  (§2.4.1.3; see [Reynolds-stress models](/methods/reynolds-stress-model.md)).
- Printed slips: "Spalart [23]" for grid guidelines of hybrid RANS/LES,
  where ref. 23 is Pearcey (1961) on shock-induced separation; "isentropic
  cells" a sentence after isotropic cells (§2.4.1.4); the $50^\circ$
  nonslender study attributed to Visbal & Gordnier [100], the 2003 paper
  on the $75^\circ$ edge, while the 2005 low-sweep study of the reference
  list is Gordnier & Visbal [134]; "CFD Vision 2020" for the reference
  titled "CFD Vision 2030 Study" (§5).

# Citations

- [Luckring & Rizzi (2024)](/sources/luckring-2024.md) — §2.1, Fig. 18; §2.3.1–2.3.2, Figs. 21–32; §2.4.1–2.4.2, Table 1, Figs. 43–53; §3.1.1–3.1.2, Figs. 54–75; §3.2.1–3.2.3, Figs. 76–98; §4.1–4.2; §5, Tables 2–3.
