---
type: Method
title: "Pseudo-direct numerical simulation (P-DNS)"
description: "Idelsohn et al.'s two-scale method replaces the subgrid model of a coarse-mesh simulation by fine-scale stresses read from a dimensionless database of off-line DNS on periodic representative volume elements, convects them with the coarse velocity under a relaxation memory model, and reports coarse-mesh results closer to DNS than LES."
status: established
aliases: [P-DNS, pseudo-DNS, RVE-based subgrid closure, representative-volume-element DNS closure]
tags: [les, sgs-model, data-driven, dns]
timestamp: 2026-10-28T07:10:00Z
---

# Pseudo-direct numerical simulation (P-DNS)

**Pseudo-direct numerical simulation** (P-DNS) is a two-scale method in
which both scales are computed numerically: the coarse scale on the
problem mesh, the fine scale off-line by DNS of small periodic domains,
**representative volume elements** (RVEs), whose results are stored in a
problem-independent dimensionless database and read on-line as the
closure of the coarse equations.
[Idelsohn et al. (2024)](/sources/idelsohn-2024.md), an overview of the
authors' method first published in 2020 (cited), rest it on four ideas
(abstract, §1.4, Fig. 1): both scales solved numerically; the fine scale
computed off-line by DNS on RVEs; the RVE results stored as a
dimensionless database used as a surrogate model; the fine-scale
instabilities convected by the coarse velocity. They frame it as a
variation of the [variational multiscale method](/methods/variational-multiscale-method.md)
in which the fine solution is computed rather than approximated through
Green functions, as an off-line evolution of the FE² method of
computational homogenization, and as a reduced-order model (§1.4). Its
premise is that the fully resolved result is "the correct one", so that
P-DNS tends to DNS as the coarse mesh is refined, and that it "does not
assume universality" of the sub-coarse-mesh scales (§1.4).

## Scale split and the inertial stress

The velocity and pressure are split into a coarse part, the
piecewise-linear finite-element or finite-volume field, and a fine part,
$u_i=u^{>}_i+u^{<}_i$, $p=p^{>}+p^{<}$; the split is a numerical one, not
a convolution filter (§2.2). The equations are written in an arbitrary
Lagrangian–Eulerian frame moving with $\boldsymbol u^{>}$, which the
authors call "Lagrangian minus": the fine scales are convected by the
coarse velocity (Eqs. 6–10). The fine fields are given zero mean and zero
mean gradient over each coarse nodal domain or cell (weakly periodic
conditions, Eqs. 15–17), and both parts are divergence-free (Eq. 18).
Neglecting the integral of the fine-scale material acceleration
$\int\rho\,D^{\boldsymbol u^{>}}u^{<}_i/Dt$, whose "validity has yet to be
shown by the numerical results", leaves one fine-to-coarse term in the
coarse momentum equation (Eqs. 19–23), the **inertial stress**

$$\mathcal T_{ij}=\rho\,u^{<}_iu^{<}_j ,$$

($\mathcal T_{ij}$ registry §11), which enters next to the viscous stress as
$-\mathcal T_{ij}$: a fine-scale Reynolds-stress product with positive trace
and density included, the analogue of $\rho\tau_{ij}$ without its trace
removed. For linear finite elements or finite volumes, replacing
$\mathcal T_{ij}$ by its average over the nodal domain is exact; the
approximation enters when that average is replaced by the average over an
RVE (Eqs. 24–27). The RVE size lies between the local coarse mesh size and
twice that value, and RVEs of neighbouring cells may overlap (§2.6–2.7).

## The databases

- **Internal RVEs** (§2.7, Fig. 2–3). A cube of side $H$ (page-local) is
  solved by DNS under a homogeneous shear imposed by jump-periodic
  boundary conditions; Dirichlet conditions were rejected because they
  suppress "a large part of the possible instabilities". The equilibrium
  stress is stored non-dimensionally as $\mathcal T_{ij}H^2\rho/\mu^2$
  against the **instability indices**, cell Reynolds numbers of the coarse
  strain: the index tensor $S^{>}_{ij}H^2\rho/\mu$, built from the
  symmetric coarse gradient to exclude rigid rotation, reduces by
  rotations and incompressibility to two parameters $\mathrm{Id}_1$,
  $\mathrm{Id}_2$ (page-local; Eqs. 28–30, Appendix 1). The database of six
  components, with indices up to $10^5$, is published (Fig. 3). Being DNS,
  the RVE runs need no convection stabilization, only incompressibility
  stabilization (§2.7.3).
- **Equilibrium wall RVEs** (§2.8, Fig. 4). A Couette-like flow between
  plates at distance $2H$, averaged over the lower half, with one index
  from the wall-parallel shear; it supplies the first layer of wall cells,
  assuming a nearly wall-parallel coarse velocity. The paper does not
  relate it to [RANS wall functions](/methods/rans-wall-function.md).
- **Time-developing boundary-layer RVE** (§2.11, Eqs. 45–61). A DNS of a
  boundary layer growing in time over an infinite flat plate at zero
  pressure gradient, solved once in dimensionless form; a triple split
  (volume average, wall-normal enrichment profile, fine part) adds an
  enrichment inertial stress, a viscous enrichment stress and an enrichment
  wall shear to the first wall cells. It is entered with an index on the
  wall-projected coarse velocity and a shape index, the ratio of the
  coarse velocities of the first two cell layers, which falls from 1.0 to
  about 0.82 when the layer reaches $2H$; values outside $[0.82,1.0]$ need
  extrapolation. It leaves out pressure-gradient effects, so separation
  and recirculation are not covered (§2.11.1). The turbulent wall RVE
  needs 264 cells in the growth direction to resolve the sublayer.

## Memory model for non-equilibrium

The databases hold equilibrium stresses. Each RVE is attached to a virtual
particle convected with the coarse velocity (particle finite-element or
finite-volume methods, cited), and its stress relaxes towards the
equilibrium value of the current coarse state (§2.9, Eqs. 35–40):

$$\mathcal T^{n+1}_{ij}=m\,\mathcal T^{n}_{ij}+(1-m)\,\mathcal T^{\mathrm{eq},n+1}_{ij},\qquad m=e^{-\Delta t/t_r},$$

with $t_r$ and $\mathcal T^{\mathrm{eq}}_{ij}$ as in registry §11. Hundreds of RVE
runs with sudden shear jumps ($\mathrm{Id}_1$ from 200 to 600, Fig. 5 with
100 realizations for a jump from 400 to 200) give
$t_r=2C_\tau/(G_{\mathrm A}+G_{\mathrm B})$ with $C_\tau\simeq1$ and
$G_{\mathrm A}$, $G_{\mathrm B}$ (page-local) the shears before and after
the jump (Eq. 37). The revised model weights the initial shear, the one
consistent with the current stress, by
$W_\tau=C_1b^3+C_2(1-b^3)$, $b$ the normalized shear jump, with
$C_1=6.8$, $C_2=4.0$ calibrated on decaying isotropic turbulence, and
freezes it below a perturbation Reynolds number $Re^*=15$ (Eqs. 38–40;
$W_\tau$, $b$, $C_1$, $C_2$, $Re^*$ page-local). Its constants come from RVE runs, not from a learned regression.

## Results reported

The examples are collected from the authors' earlier papers (cited) and
compared with DNS, experiments and a coarse-mesh LES with the Kim–Menon
dynamic $k$-equation model (see
[one-equation subgrid kinetic-energy models](/methods/subgrid-kinetic-energy-equation-model.md);
$h_s$ is the step height, page-local):

| case | coarse mesh | P-DNS | LES | reference | locator |
|---|---|---|---|---|---|
| Poiseuille, $Re=1.65\times10^5$; Couette, $Re=4\times10^4$ (1-D) | 4 and 3 cells | mean velocity "closely matches" DNS | — | 3-D DNS | §2.10.1, Table 1, Fig. 6 |
| 2-D Poiseuille, $Re=1.5\times10^5$ | refined coarse mesh | friction factor 0.014 | — | Moody diagram 0.016 | §2.10.1, Fig. 7 |
| decaying [isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md), Reynolds numbers about 60 and 500 on the r.m.s. velocity | $32^3$ to $4^3$ | reasonable energy decay down to $4^3$ | accurate at $32^3$, departs as the mesh coarsens | DNS $256^3$ | §2.10.3, Fig. 12 |
| [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) | $64^3$, $32^3$ | at $32^3$ over-predicts the decay between $\hat t=5$ and 8, agrees in most of the final phase | at $32^3$ under-predicts the decay | DNS $512^3$ | §2.10.4, Fig. 13 |
| [backward-facing step](/benchmarks/backward-facing-step.md), $Re_h=5000$ | 142 000 cells, 20 per step height | $x_R=6.05h_s$ | $5.1h_s$ | DNS $6.1h_s$; experiment $(6\pm0.15)h_s$ | §2.10.5, Fig. 16 |
| [square cylinder](/benchmarks/square-cylinder-flow.md), $Re=22\,000$ | about 2 million cells | $St=0.127$, mean $C_D=2.551$, $L_r=1.108$ | 0.115, 2.701, 1.404 | DNS (300 million cells) 0.132, 2.18, 1.04 | §2.10.6, Table 2 |
| flat-plate boundary layer, laminar and turbulent | whole layer in the first (laminar) or first two (turbulent) cell rows | thickness and $C_f$ agree with Blasius; $C_f$ "remarkable agreement" with Schlichting | — | Blasius, Schlichting | §2.12, Figs. 23, 25 |

In a spatially developing plane mixing layer (velocities 4 and 13 m/s,
meshes of $128\times30$, $256\times61$ and $512\times121$ cells) the two
finer meshes agree with the Oster & Wygnanski experiment and the coarsest
predicts less than half the turbulence intensity; the transported
effective viscosity, printed as $\mathcal T_{xy}/G_{xy}$ with
$G_{xy}=\partial_yu^{>}_x$ the coarse velocity gradient (so the density
stays in it), decreases as
the mesh is refined, which the authors read as moving the limit between
large and small scales. They state, without a figure, that standard LES on
the two coarser meshes "is not able to capture the instabilities"
(§2.10.2, Figs. 9–10). Laminar-to-turbulent transition on the flat plate
is handled only by a threshold that switches from the laminar to the
turbulent database (§2.12).

The authors conclude that for the homogeneous-fluid problems "using coarse
and medium mesh sizes, P-DNS provides better match to the experimental data
than LES", that LES methods "do not comply with the self-similarity
property or the averaged symmetry over the time of the flow", and that
P-DNS "may be cheaper than LES" because it avoids meshes fine enough to
capture every large eddy (§4). The LES comparators are single runs on the
same coarse meshes as P-DNS; no cost comparison is tabulated.

**Particle-laden extension** (§3, about 40% of the paper). Particle-laden
RVEs (126 runs) map turbulence enhancement and attenuation against volume
fraction, particle size and the index; no fixed enhancement threshold at a
Stokes number of 10 is found (§3.2.1, Fig. 27). In a particle-laden channel
at $Re=57\,000$ on $36\times12\times12$ cells P-DNS reproduces the DNS change
of mean velocity and kinetic energy, while static
[Smagorinsky](/methods/smagorinsky-model.md) LES is inaccurate and URANS
with the [$k$-$\varepsilon$ model](/methods/k-epsilon-model.md) shows a
negligible laden/unladen difference (§3.2.2, Fig. 28). A continuous
particle method closes a transported particle concentration with RVE
fluxes (§3.3–3.4). The multiphase material is on the
[Source page](/sources/idelsohn-2024.md).

## Qualifications

- **Printed values.** In the square-cylinder case the text gives the
  P-DNS recirculation length as 1.04, "again, closer to the DNS reference",
  while Table 2 prints 1.04 for the DNS and 1.108 for P-DNS (§2.10.6); the
  table is quoted above. The coarse kinetic energy of the isotropic case is
  printed $u^{>}_iu^{>}_i$ without the factor $\tfrac12$, while the
  initialization of the inertial stress from the fine energy and the
  energy sums of Eqs. (42)–(44) are consistent only with the factor
  $\tfrac12$ *(compiler check, not in the sources)*.
- **Approximations stated by the authors.** The neglected fine-scale
  acceleration term, the replacement of the cell average by the RVE
  average, the equilibrium databases with a scalar relaxation time, and
  the shape-index extrapolation are each stated as approximations to be
  justified by results (§2.4, §2.6, §2.9, §2.11).

# Citations

- [Idelsohn et al. (2024)](/sources/idelsohn-2024.md) — abstract; §1.4, Fig. 1; §2.2–2.9, Eqs. (6)–(40), Figs. 2–5; §2.10.1–2.10.6, Figs. 6–18, Tables 1–2; §2.11–2.12, Eqs. (45)–(61), Figs. 19–25; §3.2–3.4, Figs. 27–28; §4; Appendix 1.
