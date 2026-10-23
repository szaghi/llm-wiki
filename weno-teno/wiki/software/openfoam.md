---
type: Software
title: "OpenFOAM-based compressible solvers"
description: "Three sources build compressible-flow solvers in the unstructured finite-volume framework OpenFOAM: a CUDA port of a reacting-flow solver scaled to 6144 GPUs, RSDFoam coupling blastFoam numerics with Cantera real-gas thermodynamics, and a kinetic-energy-preserving central solver with Ducros-switched AUSM+-up dissipation extended to multi-species real gases."
status: established
aliases: [OpenFOAM, rhoCentralFoam, blastFoam, RSDFoam, UMReactingFlow]
tags: [software, finite-volume, gpu, kinetic-energy-preserving, numerical-flux]
timestamp: 2026-10-23T05:41:00Z
---

# OpenFOAM-based compressible solvers

OpenFOAM is an open-source, cell-centred finite-volume library on
unstructured polyhedral meshes with collocated variables and an
owner/neighbour face convention. Three sources of the bundle build
compressible solvers on it. None of them changes the discretization
framework: the schemes are nominally second order, with face values
from limited linear reconstruction or from arithmetic means, and the
contributions are an implementation, a thermodynamic coupling or an
extension of an existing flux. The bundle's high-order schemes enter
these papers only as comparators or motivation.

## The three solvers

| | [Bielawski et al. (2023)](/sources/bielawski-2023.md) | [Weng & Mével (2023)](/sources/weng-2023.md) | [Duronio & Di Mascio (2024)](/sources/duronio-2024.md) |
|---|---|---|---|
| solver | GPU port of an OpenFOAM reacting-flow solver ("UMReactingFlow", named once) | RSDFoam, OpenFOAM 9, blastFoam v5.0 + Cantera v2.4 | extension of Modesti & Pirozzoli's low-dissipative solver |
| equations | compressible reacting Navier–Stokes, Arrhenius chemistry | reactive multispecies Euler, real gases (Redlich–Kwong, Noble–Abel) | multi-species Navier–Stokes, ideal gas or Peng–Robinson |
| inviscid flux | HLLC with slope-limited face states | blastFoam's choice: HLL, HLLC, HLLC-P, AUSM+, Kurganov, Tadmor; validation with quadratic MUSCL, van Leer limiter, HLLC | kinetic-energy-preserving central flux plus switched AUSM$^+$-up dissipation |
| time stepping | explicit second-order Runge–Kutta, Strang splitting of chemistry | SSP Runge–Kutta (second order in validation), operator splitting | third-order, low-storage, four-stage Runge–Kutta |
| contribution | CUDA kernels, data layout, chemistry integrators, scaling | real-gas coupling and its validation | species and real-gas extension, application tests |

**GPU port** ([Bielawski et al. (2023)](/sources/bielawski-2023.md),
§3–§6, accepted manuscript). The solver keeps OpenFOAM's data structures
and moves its kernels to NVIDIA GPUs with CUDA. Face loops replace cell
loops because they expose about three times more parallelism on
hexahedral meshes and are accessed coalesced; the race when accumulating
into cells is resolved by an `atomicCAS`-based add. Boundary data sit in
separate arrays, so only $O(N_{\mathrm{cells}}^{2/3})$ data move between
host and device for the MPI exchange. Two cell-batched integrators
handle the operator-split chemistry, one of them handing the last few
still-reacting cells to the CPU ([operator splitting](/methods/operator-splitting.md)).
Weak scaling on Summit from 6 to 6144 V100 GPUs at $2^{20}$ cells per GPU
is near-ideal up to 3072 GPUs; the roofline puts the fluid kernels near
the bandwidth limit and the chemistry kernels near peak (Figs. 8–9). The
viscous terms "utilize a KNP formulation", citing Greenshields et al.'s
OpenFOAM implementation of semi-discrete central schemes
([central-upwind schemes](/methods/central-upwind-scheme.md)); no formula
is printed. In Appendix A a skew-symmetric central scheme, HLLC and
AUSMDV are compared on decaying compressible turbulence on structured and
skewed tetrahedral meshes: the dissipation ranks central < HLLC < AUSMDV,
and the authors suggest a hybrid central/HLLC scheme
([numerical dissipation](/definitions/numerical-dissipation.md),
[compressible isotropic turbulence](/benchmarks/compressible-isotropic-turbulence.md)).

**RSDFoam** ([Weng & Mével (2023)](/sources/weng-2023.md), §3, version
of record). Time integration, reconstruction, fluxes and adaptive mesh
refinement come from blastFoam; equations of state, departure-function
thermodynamics and kinetics from Cantera. The 1D refinement of Mao et
al. and the 2D, axisymmetric and 3D refinement of Rettenmaier et al. are
merged and chosen at run time ([adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)).
A frozen sound speed was added to Cantera and to OpenFOAM's
thermophysical classes, and the state is updated from sensible internal
energy, pressure and mass fractions by Newton iteration. Validation runs
against equation-of-state-independent theory: a real-gas
[Sod shock tube](/benchmarks/sod-and-lax-shock-tubes.md), an oblique
shock with four refinement levels, constant-volume ignition, Chapman–Jouguet
speeds up to 10 MPa, ZND structure and 2D
[cellular detonation](/benchmarks/shock-induced-combustion.md) (§4).
Real-gas runs take 2 to 6 times as long as ideal-gas ones (stated). The
authors attribute the remaining differences from Taileb et al.'s cellular
detonations to the order of the scheme, ninth-order monotonicity-preserving
reconstruction there against second-order MUSCL here, and to adaptive
against uniform meshes (§4.6).

**Low-dissipative multi-species solver**
([Duronio & Di Mascio (2024)](/sources/duronio-2024.md), §2, version of
record). The inviscid face flux is split as in AUSM into a convective
part $\rho v_n\tilde q$, $\tilde q=(1,v,H,Y_1,\dots,Y_{N_s})$, and a
pressure part, and each part into a central and a dissipative part
(Eqs. 4–5; page-local $\tilde q$, $v_n=v\cdot n$, $N_s$ species). The
central convective part is the triple-product form
$$\hat f^{\mathrm C}_u=\tfrac18(\rho_O+\rho_N)(\tilde q_O+\tilde q_N)(v_O+v_N)\cdot n$$
between owner $O$ and neighbour $N$ cell centres, after Pirozzoli, and
the central pressure part $\tfrac12(p_O+p_N)n$ (Eq. 6;
[split convective forms](/methods/split-convective-forms.md)); the
species enter only through $\tilde q$. The dissipative parts are the
AUSM$^+$-up dissipation terms evaluated from minmod extrapolations of
the face states; the convective one is switched on only where the face average
$\Psi_{\mathrm D,ON}$ of the compression-only Ducros-type sensor
$\Psi_{\mathrm D}=\max\big(-\nabla\cdot v/\sqrt{(\nabla\cdot v)^2+\lvert\nabla\times v\rvert^2+\epsilon_{\mathrm D}},\,0\big)$,
$\epsilon_{\mathrm D}=v_0^2/L_0^2$, exceeds the threshold $\Psi^*=0.05$
(a Heaviside factor), and the pressure one carries no switch as
printed (Eqs. 7–8; $\Psi_{\mathrm D}$, $\Psi^*$, $\epsilon_{\mathrm D}$ as on
the Ducros page, page-local $v_0$, $L_0$, whose values are not printed; [Ducros shock sensor](/definitions/ducros-shock-sensor.md),
[hybrid schemes](/methods/hybrid-weno.md)). The real-gas closure is the
Peng–Robinson equation of state. The paper's tests are applications:
two shock–bubble [Richtmyer–Meshkov](/benchmarks/richtmyer-meshkov-instability.md)
cases against experiment (N$_2$ in SF$_6$; helium in N$_2$,
[shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)), with
three-grid observed orders 1.35–1.53 and grid convergence indices
0.77–1.1 % (Table 1); a 2D LOX/H$_2$ supercritical mixing layer with
density ratio about 80; and vapour propane injection through an
eight-hole gasoline injector with LES. Agreement is assessed graphically.

## Positions on OpenFOAM's schemes

- Duronio & Di Mascio state that earlier low-diffusion variants of
  rhoCentralFoam, OpenFOAM's solver based on the Kurganov–Tadmor central
  scheme, "do not guarantee discrete conservation of some global
  quantities, like the total kinetic energy in the inviscid limit", that an
  implicit AUSM-based OpenFOAM solver "performs similarly to
  rhoCentralFoam", and that commercial solvers do not use low-dissipation
  techniques on unstructured meshes although Modesti & Pirozzoli proved
  them possible (§1). They run no head-to-head comparison.
- [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) contrast their
  [MFC](/software/mfc.md) with OpenFOAM, whose higher-order and
  interface-capturing models are "only available via links to external
  forked projects" (§1).
- Bielawski et al. observe that limiting conservative variables at faces
  can break $\sum_kY_k=1$, giving each scalar its own effective contact
  speed, and that the one-dimensional projection between neighbouring
  cell centres need not pass through the face centre on skewed cells
  (§3; stated, not demonstrated).

## Qualifications

- The kinetic-energy preservation Duronio & Di Mascio invoke, proved by
  Pirozzoli for the central flux, covers the central part only: with the
  pressure dissipation active everywhere as printed (Eq. 8), the scheme
  as run is not kinetic-energy preserving, and no inviscid test of the
  property is shown *(compiler check, not in the sources)*. They do not
  discuss the spurious pressure oscillations that fully conservative
  mass-fraction models with real-gas equations of state can produce at
  interfaces ([pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)).
- Duronio & Di Mascio print $H=(e+p)/\rho$ as the total enthalpy with $e$
  the total energy per unit mass, a dimensional slip for $H=e+p/\rho$; the
  shock Mach numbers of their bubble cases are not printed, nor the
  coefficients of the dissipation terms or the time step.
- Weng & Mével's numerics are blastFoam's, unchanged; Bielawski et al.'s
  discretization is the baseline solver's, unchanged. Neither paper
  reports an order-of-accuracy study.

# Citations

- [Bielawski et al. (2023)](/sources/bielawski-2023.md) — accepted manuscript: §3; §4; §5.1–5.2; §6.3, Figs. 8–9; App. A.
- [Weng & Mével (2023)](/sources/weng-2023.md) — version of record: §3.1–3.3; §4; §4.6.
- [Duronio & Di Mascio (2024)](/sources/duronio-2024.md) — version of record: §1; §2, Eqs. (1)–(10); §3, Table 1, Figs. 2–17.
- [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) — arXiv v1: §1 (OpenFOAM positioning).
