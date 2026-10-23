---
type: Source
title: "Duronio & Di Mascio (2024) — Implementation and assessment of a low-dissipative OpenFOAM solver for compressible multi-species flows"
description: "Extends the kinetic-energy-preserving, Ducros-switched AUSM+-up OpenFOAM solver of Modesti and Pirozzoli to multi-species ideal and Peng–Robinson real gases on unstructured grids, assessed on shock–bubble Richtmyer–Meshkov cases, a supercritical LOX/H2 mixing layer and a gaseous Spray G injection."
resource: "doi:10.1016/j.compfluid.2024.106240"
source_kind: paper
authors: [Duronio F., Di Mascio A.]
year: 2024
venue: "Comput. Fluids 274:106240"
local_file: "/home/stefano/papers/mosaic/weno-teno/2024_Crossref_Computers_amp_Fluids_Duronio_Implementation_and_assessment_of_a_low-dissipative_OpenFOAM.pdf"
tags: [software, finite-volume, kinetic-energy-preserving, hybrid-scheme, multiphase, unstructured-mesh]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

An application and software paper. It extends an existing low-dissipation
[OpenFOAM](/software/openfoam.md) solver (Modesti & Pirozzoli 2017, ref. [19])
from a single ideal gas to compressible multi-species flows of ideal and real gases
on unstructured polyhedral grids. The discretization is recalled, not developed.
The inviscid face flux is split AUSM-style into a convective part
$\rho v_n\tilde q$ and a pressure part $p\tilde n$. The central convective part is
the triple-product [split convective form](/methods/split-convective-forms.md) of
Pirozzoli, which by ref. [34] gives semi-discrete
[kinetic energy preservation](/properties/kinetic-energy-preservation.md). The
dissipative parts are AUSM$^+$-up terms built from minmod extrapolations. The
convective dissipation is switched on only where a face-averaged
[Ducros-type sensor](/definitions/ducros-shock-sensor.md) exceeds $\Psi^*=0.05$.
This is the [hybrid central/upwind](/methods/hybrid-weno.md) idea without any WENO.
Time stepping is a low-storage, four-stage, third-order Runge–Kutta method. The new
ingredients are the species mass fractions $Y_k$, carried in the conserved vector
and in $\tilde q$ with mass-weighted mixture properties (a fully conservative
[multicomponent](/definitions/multicomponent-euler-equations.md) model), and a
Peng–Robinson equation of state.

The paper proves nothing and runs no accuracy test on smooth solutions. It
assesses the solver on three applications.

1. Two [shock–bubble](/benchmarks/shock-bubble-interaction.md)
   [Richtmyer–Meshkov](/benchmarks/richtmyer-meshkov-instability.md) cases: an
   N$_2$ square bubble in SF$_6$ against Zhai et al. (2014), and the He bubble in
   N$_2$ against Haas & Sturtevant (1987). A three-grid Roache analysis gives
   observed orders 1.35–1.53.
2. The two-dimensional supercritical LOX/H$_2$ mixing layer of Ruiz et al. (2016),
   run with the Peng–Robinson and the perfect-gas equations of state.
3. Gaseous propane injected through the ECN Spray G injector, with dynamic
   $k$-equation LES. This is a subgrid model, not a
   [wall model](/methods/wall-modeled-les.md).

All agreement claims are graphical or qualitative. The paper does not discuss
interface pressure oscillations, and it reports no timings.

# Version read

Version of record (Elsevier typeset, open access CC BY-NC-ND): received 2 November
2023, accepted 8 March 2024, available online 11 March 2024. 14 pages. Title,
authors, venue and DOI on page 1 match Crossref. Equation, figure and table numbers
are those of this version.

# Key claims

Registry notation: velocity $v$ (normal component $v_n=v\cdot n$), specific total
energy $E/\rho$, specific total enthalpy $H$, mass fractions $Y_k$ for
$k=1,\dots,N_s$, and the modified Ducros sensor $\Psi_{\mathrm D}$ with threshold
$\Psi^*$. Subscripts $O$ and $N$ are the owner and neighbour cells of a face, and
$n$ points from $O$ to $N$.

1. The paper extends the solver of ref. [19] (AUSM splitting, a skew-symmetric kinetic-energy-preserving central flux and sensor-switched upwind dissipation) to multi-species flows of ideal and real gases on unstructured OpenFOAM grids (§1, §2). **Stated**
2. The inviscid face flux is split into a convective part and a pressure part, $f\cdot n=\rho v_n\tilde q+p\tilde n$, with $\tilde q=(1,v,H,Y)$ and $\tilde n=(0,n,0,0)$ (Eq. (4), following Liou & Steffen, ref. [33]). **Stated**
3. The central convective flux $\tfrac18(\rho_O+\rho_N)(\tilde q_O+\tilde q_N)(v_O+v_N)\cdot n$ preserves the total kinetic energy in semi-discrete form and "therefore has strong nonlinear stability". The proof is in ref. [34], not in this paper (Eq. (6), §2). **Stated**
4. The central discretization alone is stable for fully resolved DNS. Under-resolved regions and shocks need added numerical dissipation (§2). **Stated**
5. The sensor $\Psi_{\mathrm D}=\max\!\big(-\nabla\cdot v/\sqrt{(\nabla\cdot v)^2+\lvert\nabla\times v\rvert^2+v_0^2/L_0^2},\,0\big)$ lies in $[0,1]$. It is small in smooth zones and $O(1)$ near shocks, and is averaged to faces as $\tfrac12(\Psi_{\mathrm D,O}+\Psi_{\mathrm D,N})$ (Eq. (7), §2). **Stated**
6. Convective dissipation is $I_C\,\mathsf H(\Psi_{\mathrm D,ON}-\Psi^*)\,f^{\mathrm{AUSM}}_u$, with $\Psi^*$ "usually set equal to 0.05" and $\mathsf H$ the Heaviside function. Pressure dissipation is $I_P\,f^{\mathrm{AUSM}}_p$ and, as printed, carries no sensor factor. $I_C$ and $I_P$ are $O(1)$ coefficients whose values are not printed (Eq. (8)). **Stated**
7. The dissipation terms are those of AUSM$^+$-up (ref. [36]), evaluated from minmod extrapolations of the face quantities from the adjacent cells (§2). **Stated**
8. Time integration is a third-order, low-storage, four-stage explicit Runge–Kutta method (§2, ref. [37]). **Stated**
9. Grid convergence on three grids with Roache's procedure (ref. [42]), along the longitudinal axis. Square N$_2$ bubble: observed order 1.53 for $p$ and 1.46 for $\rho$, GCI 0.92 % and 0.97 %. Round He bubble: order 1.35 for $p$ and 1.46 for $\rho$, GCI 1.1 % and 0.77 % (Table 1, §3.1). **Shown**
10. The square-bubble run reproduces the experimental wave sequence of ref. [40] at $t=82$, 188, 374, 588–854, 1068 and 1334 μs. The sequence runs from the transmitted and free precursor shocks, through the triple point and Mach stem, the secondary and reflected transmitted shocks and the diffracted shock, to the corner vortex pairs, the jet and a vortex pair joined by a bridge (Fig. 4, §3.1.2). **Shown** (qualitative)
11. Square bubble: the computed interface width agrees "excellent[ly]" with experiment. The height is "slightly higher than the experimental data for $t>0.75$ ms" (Fig. 5). **Shown**
12. He bubble: the flow evolution and the space–time paths of the upstream and downstream interface points agree with the experiment of ref. [41] ("excellent agreement", Figs. 6–7). **Shown**
13. LOX/H$_2$ mixing layer: large vortical structures of about the momentum thickness ($\approx h$, the lip height) dominate. Finger-like structures on the oxygen surface have a wavelength of about $5h$ (Fig. 9, §3.2.2). **Shown**
14. The LOX density predicted with the ideal-gas equation of state is "relevantly different" from the Peng–Robinson result. Other flow quantities differ less (Fig. 10). **Shown**
15. The mixing-layer thickness, defined by a 1 % threshold on the LOX mass fraction, is in "good overall agreement" with refs. [46, 56] as a function of $x/h$ (Fig. 13). Running averages over 15 flow-through times at $x/h=1,3,5,7$ are compared on two grids (Fig. 12). **Shown**
16. Spray G propane injection (45 bar injection, 4 bar ambient, 390 K): the solver captures a first shock cell inside the counter-bore and a moderately under-expanded "diamond"/"X" jet. On the hole axis the maximum velocity is about 630 m/s and the minimum pressure about 0.5 bar upstream of the shock; the ambient pressure is recovered about 2 mm downstream (Figs. 15–16, §3.3.2). **Shown**
17. The computed log-density-gradient rendering "closely resembles" the Schlieren images of ref. [61], with similar shock structures on comparable length scales (Fig. 17). **Shown** (qualitative)
18. A 7–10 μm grid spacing in the sac and nozzle is sufficient for the turbulent-flow details, per the grid studies of refs. [58–60] (§3.3.1). **Stated**
19. The low-diffusion variants of rhoCentralFoam (refs. [27, 28]) "do not guarantee discrete conservation of some global quantities, like the total kinetic energy in the inviscid limit [29]". The implicit AUSM solver of ref. [30] "performs similarly to rhoCentralFoam", and the PIMPLE multiphase solver of Cerminara et al. (ref. [31]) "showed lower diffusion than rhoCentralFoam" (§1). **Stated** (no comparison is run here)
20. Commercial solvers do not use low-dissipation techniques on unstructured meshes, although ref. [19] proved them possible (§1). **Stated**

# Printed slips

- §2, after Eq. (3): "$H=(e+p)/\rho$ is the total enthalpy", with $e=c_vT+\lVert u\rVert^2/2$ the total energy per unit mass. The sum $e+p$ mixes units; the consistent form is $H=e+p/\rho$ *(compiler check, not in the sources)*.
- Eq. (3) against Eq. (1): the energy component of the viscous flux is printed as $\kappa\,\partial T/\partial x_i$ alone, without the viscous work $\sigma_i\cdot u$ that Eq. (1) contains. The species component is printed $\mathbf D\,\partial\mathbf Y/\partial x_i$ where Eq. (1) has $\rho\mathbf D\nabla\mathbf Y$, so a factor $\rho$ is missing.
- Eq. (1), momentum: "$\nabla\cdot[\rho\mathbf u\otimes\mathbf u+p]$", with $p$ lacking the identity tensor.
- Eq. (8): the pressure dissipation carries no Heaviside factor while the convective one does. The paper does not say whether this is intended. If it is, the scheme as run adds pressure dissipation everywhere and is not exactly kinetic-energy preserving *(compiler check, not in the sources)*.
- §3.1.2: "In Table 1, the grid convergence index and the order of convergence, calculated for the density, are reported", but Table 1 and its caption give both pressure and density.
- §3.1.1: the shock Mach number of either bubble case is never given, and neither are the grid sizes of the He-bubble case.
- §3.2.2 against the Fig. 12 caption: the text lists "axial velocity, transverse velocity, pressure and density", the caption "axial velocity, density, temperature and oxygen mass fraction".
- §3.2.2: "comparing the simulations with experiments was impossible because of the need for experimental data" ("need" for "lack").
- Fig. 11: blue and red $q$-criterion isocontours are described as negative and positive (clockwise and counter-clockwise) vorticity, but the $q$ criterion carries no sense of rotation *(compiler check, not in the sources)*.
- §4: "The algorithm extends the energy-preserving skew-symmetric scheme proposed in [37]". In §§1–2 the extended scheme is ref. [19]; ref. [37] is the arXiv preprint cited for the Runge–Kutta method. The conclusions also speak of "two different engineering problems" where three test cases are run, and of "two simulations … with a density ratio equal to 80" where only the mixing layer has it.
- §3.2 calls a two-dimensional computation at $\mathrm{Re}$ up to $2\times10^5$ "DNS simulations".
- References: [32] prints the authors as "White F, Frank M. White S."; [55] prints "Pope SB, Pope SB." and [62] "Kim W-W, Menon S, Kim W-W, Menon S."; [23] and [58] print no year.

# Notation map

| Duronio & Di Mascio 2024 | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf q=(\rho,\rho\mathbf u,\rho e,\rho\mathbf Y)$ | $u=(\rho,\rho v,E,\rho Y_k)$ | finite-volume cell averages; **collision**: the source's $\mathbf u$ is the velocity |
| $\mathbf u$, $u_i$, $u_n$ | $v$, $v_i$, $v_n=v\cdot n$ | velocity |
| $e$ (total energy per unit mass) | $E/\rho$ | **collision**: registry $e$ is the specific internal energy |
| $H$ | $H$ | specific total enthalpy; agrees (but see Printed slips) |
| $\mathbf Y=(Y_1,\dots,Y_{N_s})$, $N_s$ | $Y_k$, $N_s$ (local) | species mass fractions and number of species |
| $\mathbf F^e_i$, $\mathbf F^v_i$ | $f^{(i)}$, viscous flux | inviscid and viscous fluxes in direction $i$ |
| $\mathbf F_u$, $\mathbf F_p$; $(\cdot)^C$, $(\cdot)^D$ | $f_u$, $f_p$ (local) | AUSM convective and pressure parts; central and dissipative parts |
| $\tilde{\mathbf q}$, $\tilde{\mathbf n}$ | $\tilde q$, $\tilde n$ (local) | convected vector per unit mass flux, pressure direction |
| $(\cdot)_O$, $(\cdot)_N$ | cells on the two sides of a face | OpenFOAM owner and neighbour, not $i$, $i+1$; **collision**: $N$ is the registry's DG degree |
| $\theta$, $\theta_{ON}$, $\theta^*$ | $\Psi_{\mathrm D}$, face average, $\Psi^*$ | modified (compression-only, non-squared) Ducros sensor; **collision** with the Zhang–Shu factor $\theta$ |
| $u_0^2/L_0^2$ | regularization of $\Psi_{\mathrm D}$ | values not printed |
| $H(x)$ | $\mathsf H$ (local) | Heaviside function; **collision** with the enthalpy $H$ |
| $I_C$, $I_P$ | — | $O(1)$ dissipation coefficients |
| $\kappa$ | thermal conductivity (local) | **collision**: registry $\kappa$ is the kinetic energy |
| $\mu$, $\lambda$ | dynamic viscosity, second viscosity | **collision**: registry $\lambda_l$ are eigenvalues |
| $v$, $a$, $b$, $R$ (Peng–Robinson) | molar volume, attraction and co-volume parameters, gas constant | **collision**: registry $v$ is the velocity, $a$ the wave speed |
| $M_s$, $M_2$ | shock and post-shock Mach numbers | |
| $q$ (Q-criterion) | — | **collision** with the weight exponent $q$ |
| $h$ | lip height, 0.5 mm | |

# Reference list

The paper prints 63 references, numbered [1]–[63] in Elsevier numbered style. The
list is merged complete into the [bibliography](/bibliography.md) with `citedby`
including `duronio-2024`. [23] (Duronio et al., Int. J. Engine Res.) and [58]
(Mohapatra et al., Int. J. Engine Res.) print no year. [23] is a different work from
this source and is kept under its own key. [45], [47] and [62] (AIAA meetings) print
their year only inside the DOI. [57] is a web page with a corporate author. The
preprint [37] (arXiv:1612.05223) is its own entry, distinct from the published
ref. [19]. [7] prints no journal name. Same-author same-year works take suffixes in
printed order (Vuorinen 2014 [27]/[29], Duronio 2021 [17]/[63], Boyd 2021 [8]/[9],
Gärtner 2020 [20]/[21]). [32], [55] and [62] have garbled or duplicated author lists
(see Printed slips). No item is unparseable.

# Pages created or updated

Chunk 7 (2026-10-23), cited further in chunks 8–9 (2026-10-23). This source is cited on:

* [Ducros shock sensor](/definitions/ducros-shock-sensor.md)
* [Kinetic energy preservation](/properties/kinetic-energy-preservation.md)
* [OpenFOAM-based compressible solvers](/software/openfoam.md)
* [Richtmyer–Meshkov instability](/benchmarks/richtmyer-meshkov-instability.md)
* [Shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)
* [Split convective forms](/methods/split-convective-forms.md)
