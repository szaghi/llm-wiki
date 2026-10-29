---
type: Method
title: "One-dimensional turbulence (ODT)"
description: "One-dimensional turbulence is Kerstein's stochastic multi-scale model that evolves turbulence on a line by alternating deterministic one-dimensional transport with sampled eddy events implemented by triplet maps and kernel transformations; the page gives its sampling rule, eddy-energy models, compressible forms and couplings to LES."
status: established
aliases: [ODT, one-dimensional turbulence model, stochastic ODT, LES-ODT, ODTLES, conservative compressible ODT, triplet map]
tags: [les, sgs-model, compressible, wall-model, boundary-layer]
timestamp: 2026-10-29T10:04:00Z
---

# One-dimensional turbulence (ODT)

**One-dimensional turbulence (ODT)**, attributed to Kerstein (1999) by
[Chen et al. (2024b)](/sources/chen-2024-c.md), represents turbulence on a
single line, the "ODT line", aligned with the direction of the largest
mean gradient. Two modules alternate. A **deterministic module** advances
one-dimensional truncated transport equations (in the original
incompressible model, diffusion only: convection is produced by the
eddies). A **stochastic module** samples candidate "one-dimensional
eddies" by a Monte Carlo rejection step and implements each accepted
eddy by a measure-preserving rearrangement of the profiles (triplet map)
and, for the velocity, a kernel transformation that redistributes energy
among components. Statistics are ensemble averages over independent
realizations. "One-dimensional turbulence" means a one-dimensional
computational domain, not one-dimensional turbulence (§2.1, Fig. 1).
The model is used stand-alone and as a subgrid or near-wall closure of
[large-eddy simulation](/definitions/large-eddy-simulation.md). Chen et
al. (2024b) is a review written by the developers of the conservative
compressible variant below; it presents no new computations.

## Eddy sampling

An eddy occupies the interval $[y_0,y_0+l_e]$ of the line ($l_e$ the eddy
size, registry §11; $y_0$ its lower end, page-local). Chen et al. (2024b, §2.2.2,
Eqs. 1–3) print the acceptance probability and the eddy rate density as

$$P_a=\frac{\lambda_e(y_0,l_e,t)\,\Delta t_s}{g_1(l_e)\,g_2(y_0)},\qquad \lambda_e=\frac{C_e}{l_e^2\,\tau_e},\qquad \tfrac12\rho\,l_e\Big(\frac{l_e}{\tau_e}\Big)^2\sim E_{\mathrm{kin}}+E_{\mathrm{pe}}-E_{\mathrm{visc}},$$

with $\lambda_e\,dy_0\,dl_e$ the number of eddy events
per unit time in $[y_0,y_0+dy_0]\times[l_e,l_e+dl_e]$ and $\tau_e$ the
eddy time scale (registry §11), and page-local symbols: $\Delta t_s$ the
sampling interval, $g_1g_2$ a presumed joint PDF of eddy size and
position, and $E_{\mathrm{kin}}$,
$E_{\mathrm{pe}}$, $E_{\mathrm{visc}}$ the kinetic, potential and viscous
contributions to the eddy energy. A random number $r\in[0,1]$ is drawn
and the eddy is accepted if $r<P_a$. The form of $g_1g_2$ "will not affect
the calculated results" but affects efficiency (citing Sutherland et al.).
After each accepted eddy the deterministic equations advance to the eddy
time, so equation time and sampling time stay equal, and $P_a$ is updated
with the field (§2.1). The square $(l_e/\tau_e)^2$ is the "eddy energy";
when an eddy-energy model makes it negative, Eq. (3) gives no real
$\tau_e$ and Eq. (2) no event rate *(compiler check, not in the
sources)*.

**Free parameters.** The rate parameter $C_e$ (the first free parameter;
$C_e=1$ implicitly in Kerstein 1999), the energy-redistribution constant
$\alpha_e$ (the second; the fraction of the removable kinetic energy
moved from the dominant component to the two others) and the viscous
penalty $Z_e$ (the third), all in registry §11 (§2.2.2). The original model has
one free parameter $A_e$ (page-local) instead.

## Eddy-energy models

Chen et al. (2024b, Tables 1–2) collect the eddy-energy closures; the
kernel quantities they contain are defined in the cited works, not in the
review.

| Model | Flow | Eddy energy $(l_e/\tau_e)^2$, as printed | Locator |
|---|---|---|---|
| Kerstein (1999) | decaying homogeneous turbulence, shear flow | $(A_e\Delta u)^2-(16\nu/l_e)^2$, $\Delta u$ the velocity difference across the eddy | Eq. (4) |
| Kerstein (1999) | buoyant stratified flow | $(A_e\Delta u)^2$ minus a gravitational term $\tfrac{27g}{2\rho_0l_e}\int[\hat\rho(y)-\rho(y)]y\,dy$ ($g$ gravity, $\rho_0$ the mean density in the eddy, $\hat\rho$ the density after the eddy; page-local) | Eq. (5) |
| Kerstein et al. (2001), vector ODT | mixing layer, wake | $\tfrac{27}{4}$ times the sum of three squared kernel velocities, minus $Z_e\nu^2/l_e^2$ | Eq. (6) |
| Ashurst & Kerstein (2005), variable density | mixing layers | weighted removable energies $(1-\alpha_e)Q_i+\tfrac{\alpha_e}{2}(Q_j+Q_k)$ minus a viscous penalty ($Q_i$ the removable energy of component $i$, page-local) | Eq. (7) |
| McDermott (2005) | free shear flow, decaying isotropic turbulence, Rayleigh–Taylor context | kinetic plus gravitational plus baroclinic terms, empirical parameter $B=2.2$, gravity components with $g^2+g_c^2=9.8^2$ | Eq. (8) |
| Jozefik et al. (2016), Lagrangian compressible | Darrieus–Landau instability; Richtmyer–Meshkov instability | Eq. (7)-type terms plus a potential energy of the flame acceleration, or of the shock–turbulence interaction with an empirical shock-energy factor | Eqs. (11)–(15) |
| Chen, Gao et al. (2019–2023), conservative compressible | supersonic channels, supersonic scalar mixing layer; Richtmyer–Meshkov | identical to Eq. (7); for shock–turbulence interaction identical in form to Eq. (15) | Eqs. (16)–(17) |

McDermott's buoyant model is relevant to
[Rayleigh–Taylor mixing](/benchmarks/rayleigh-taylor-mixing.md), and the
shock–turbulence term to the Richtmyer–Meshkov problems recorded on
[shock-generated turbulence](/results/shock-generated-turbulence.md).

## Eddy implementation

**Triplet map.** Chen et al. (2024b, §2.2.3, Eq. 9, Fig. 3), after
Kerstein (1999), print the map $\mathcal M$ (registry §11) that each
accepted eddy applies to the profiles:

$$\mathcal M(y)=y_0+\begin{cases}3(y-y_0), & y_0\le y<y_0+\tfrac13l_e,\\ 2l_e-3(y-y_0), & y_0+\tfrac13l_e\le y\le y_0+\tfrac23l_e,\\ 3(y-y_0)-2l_e, & y_0+\tfrac23l_e<y\le y_0+l_e,\\ y-y_0, & \text{otherwise},\end{cases}$$

with a field $\phi$ replaced by $\phi(\mathcal M(y))$. The profile in the
eddy interval is compressed to a third, copied three times and the
middle copy flipped, which keeps it continuous. The map is measure
preserving, so the integrals of mass, momentum and energy are conserved
(§2.2.3). The "otherwise" branch is printed as $y-y_0$, so with the
leading $y_0$ the map is the identity outside the eddy *(compiler check,
not in the sources)*.

**Kernel transformation.** The velocity alone is further modified,
scalars are only triplet-mapped (§2.2.4, Eqs. 10, 19):

$$u_i(y)\to u_i(\mathcal M(y))+c^K_iK_e(y),\qquad K_e(y)=y-\mathcal M(y),$$

(Kerstein et al. 2001; one degree of freedom), and, for variable density
(Ashurst & Kerstein 2005; two degrees of freedom),

$$u_i(y)\to u_i(\mathcal M(y))+b^K_iJ_e(y)+c^K_iK_e(y),\qquad J_e(y)=\lvert K_e(y)\rvert,$$

where the extra term enforces momentum conservation over the eddy when
the density varies ($K_e$, $J_e$, $b^K_i$, $c^K_i$ page-local; the
amplitudes are given in the cited works). The kernel transformation
models pressure scrambling: it moves kinetic energy from the dominant
component to the other two.

## Variants

- **Variable density and buoyancy.** Ashurst & Kerstein (2005) simulated
  mixing layers with density ratios 1, 2, 4 and 8 and convective Mach
  numbers 0.3, 0.7 and 1.1; the ODT growth rate agreed with DNS at 0.3
  and 0.7, with "a large discrepancy" at 1.1, which the review blames on
  the incompressible framework and a simple kinematic model (§2.3.4,
  §3.1; see [temporal mixing layer](/benchmarks/temporal-mixing-layer.md)).
  McDermott (2005) added buoyancy and baroclinic terms.
- **Adaptive mesh and curvilinear forms.** Adaptive-mesh ODT (Lignell et
  al. 2013) adapts the line mesh in space and time and balances the load
  between regions with many and few eddies (see
  [mesh adaptation](/methods/mesh-adaptation.md)); cylindrical and
  spherical ODT (Lignell et al. 2018) gave "excellent agreement" with DNS
  of temporal pipe flow at $Re_\tau=550$, 1000 and 2000 and was used for
  round jets and a jet flame (§3.1). Applications to combustion,
  multiphase and electrohydrodynamic flows are listed.
- **Lagrangian compressible ODT** (Jozefik et al. 2016). Truncated mass,
  momentum, total-enthalpy and species equations in primitive,
  non-conservative form keep a truncated mean convective term, and the
  stochastic module models only the fluctuating convection. It covered a
  shock tube, Richtmyer–Meshkov instability and deflagration-to-detonation
  transition, but deviated significantly in the Richtmyer–Meshkov
  mixing-zone width and kinetic energy (§2.3.1, §3.2, Fig. 9).
- **Conservative compressible ODT** (Chen, Gao et al., the reviewers' own
  group). The one-dimensional equations keep convection in conservative
  form in $(\rho,\rho u_i,E,\rho Y_\alpha)$ ($Y_\alpha$ species mass
  fractions, page-local), which admits shock-capturing schemes; the
  triplet map acts on these conserved variables, $\rho u_i(y)\to\rho u_i(\mathcal M(y))$
  and so on (Eq. 18), and the two-degree-of-freedom kernel then acts on
  the velocity (§2.3.1–2.3.4, Fig. 10). The equations themselves are not
  printed in the review. Reproduced figures show agreement with DNS of
  the mean velocity of supersonic channel flow in the viscous sublayer,
  buffer and log layers (Fig. 11) and a Richtmyer–Meshkov mixing-zone
  width and kinetic energy "significantly" better than the Lagrangian
  model (Fig. 12). Gao et al. (cited) attribute the Lagrangian model's
  failure to "the inability of the Lagrangian framework to incorporate
  the conservation governing equation and the shock capturing scheme"
  (§3.2).

## Coupling to LES

**LES-ODT: ODT as a subgrid closure** (§2.4.1, Fig. 5). Fine ODT lines
are embedded in the LES grid along the three directions.

- In the finite-volume framework of McDermott (2005), the lines cross at
  LES cell centres, are initialized by interpolating the resolved field,
  are iterated within each LES time step, and return subgrid quantities
  evaluated on each control-volume face, a two-way exchange between
  resolved and subgrid scales. Results: incompressible free shear layers
  and decaying [isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md).
- In the finite-difference framework of Echekki and co-workers, three
  equation sets are solved at LES nodes, line intersections and inner
  line nodes. The LES solves continuity and momentum with a
  [Smagorinsky](/methods/smagorinsky-model.md) subgrid stress; the lines
  solve energy and species and close mixing and heat release
  (autoignition, reacting shear layers, premixed flames).

**ODT as a near-wall closure** (§3.3, Figs. 13–16). Schmidt et al. (2003)
filter the ODT momentum flux in time and space to give the subgrid
stresses near the wall, drive the lines by the LES pressure and velocity,
and couple over an overlap region several LES cells thick; channel flow
from $Re_\tau=395$ to 10000 was validated against DNS. Freire & Chamecki
(2021) use ODT as a wall model for LES of smooth and rough channels,
resolving near-wall fluctuations within the first LES cell, at a cost
"considerably higher" than LES alone but reasonable for a fixed-grid
code. The embedded near-wall line resembles the mesh of a wall-stress
model, but transport there comes from eddy events at many scales, not
gradient diffusion (§2.4.1; see [wall-modelled LES](/methods/wall-modelled-les.md)
and [turbulent channel flow](/benchmarks/turbulent-channel-flow.md)).

**ODTLES** (§2.4.2, §3.3, Fig. 6). Schmidt et al. (2005) place three
orthogonal families of ODT sheets on a coarse three-dimensional mesh;
coarse values are integral averages over the lines of each direction, and
continuity is solved on the coarse grid so that random errors do not
accumulate. Gonzalez-Juez et al. (2011) report good agreement with DNS for
a no-slip channel, a channel with a free-slip wall, a lid-driven cavity
and a square duct; with an implicit–explicit time scheme that relaxes the
CFL limit, Glawe et al. resolve channel flow up to $Re_\tau=2040$ on one
single-board computer, in close agreement with DNS.

## Assessment by the review

- **Place among closures.** The review follows Kerstein (cited) in calling
  conventional subgrid closures "parameterization", top-down closures that
  rely on subgrid isotropy and fail near walls, and classes ODT with
  vortex methods and lattice Boltzmann methods as an "autonomous
  microstructure evolution" approach that generates small-scale
  information itself (§4.1; see
  [energy backscatter](/definitions/energy-backscatter.md) for the
  bottom-up transfer it invokes, and
  [lattice Boltzmann methods](/methods/lattice-boltzmann-method.md)).
- **Maturity.** No ODT-based method has yet simulated three-dimensional
  high-speed compressible turbulence; LES-ODT and ODTLES are limited to
  three-dimensional low-speed (reacting and non-reacting) flows, and
  LES-ODT is the more mature of the two (§3, §4.2, §6).
- **Open problems.** The authors propose a conservative compressible
  LES-ODT and list eight challenges: initialization of the lines from the
  LES, coupling design, efficient subgrid ODT solution, subgrid feedback
  to the LES, shock–eddy interaction, free parameters tied to the local
  flow, curvilinear coordinates and parallelization (§5).

## Qualifications

- Chen et al. (2024b) review the conservative compressible variant of
  their own group; the comparisons with the Lagrangian model and with DNS
  are figures reproduced from the authors' earlier papers.
- The review prints two statements on "top-down" and LES-ODT: §2.4.1 says
  the traditional top-down strategy is abandoned in LES-ODT, §3.3 calls
  LES-ODT a top-down strategy and contrasts it with bottom-up ODTLES.
- §4.2 attributes its ref. 52 to Gao, whose first author is Chen (as §2.3.2
  and Table 2 of the review attribute it).
- The viscous penalty enters as $Z_e$ (Eqs. 6, 7, 16), $Z_e/2$ (Eqs. 14,
  15, 17) and $Z_e^2/2$ (Eq. 8).
- In Eq. (14) the two printed lines of the Darrieus–Landau model differ in
  the potential-energy term: substituting the printed Eq. (11) into the
  first line gives a prefactor $16/(27\rho l_e)$, the second line carries
  $8l_e^2/(27\rho)$ ($\rho$ standing for the source's kernel density), a ratio of
  $l_e^3/2$ *(compiler check, not in the sources)*; both lines are joined
  by "$\sim$".

# Citations

- [Chen et al. (2024b)](/sources/chen-2024-c.md) — §2.1, Fig. 1; §2.2.2, Eqs. (1)–(8), Table 1; §2.2.3, Eq. (9), Fig. 3; §2.2.4, Eqs. (10), (19), Fig. 4; §2.3.1–2.3.4, Eqs. (11)–(18), Table 2, Fig. 10; §2.4.1–2.4.2, Figs. 5–6; §3.1–3.3, Figs. 9, 11–16; §4.1–4.2; §5; §6.
