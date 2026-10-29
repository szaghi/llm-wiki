---
type: Source
title: "Spalart & Allmaras (1992) — A one-equation turbulence model for aerodynamic flows"
description: "Conference paper that builds the Spalart–Allmaras one-equation eddy-viscosity model in four nested versions (free shear, near-wall, low Reynolds number, laminar region and trip), with its constants, a positivity-preserving implicit solver, and tests on boundary layers and the RAE 2822 airfoil."
resource: "doi:10.2514/6.1992-439"
source_kind: paper
authors: [Spalart P.R., Allmaras S.R.]
year: 1992
venue: "30th Aerospace Sciences Meeting and Exhibit, AIAA Paper 92-0439"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/1992_Crossref_30th_Aerospace_Sciences_Meeting_and_Exhibit_SPALART_A_one-equation_turbulence_model_for_aerodynamic_flows.pdf"
tags: [rans, spalart-allmaras, eddy-viscosity, transition, airfoil]
timestamp: 2026-10-29T16:21:00Z
---

# Summary

Spalart & Allmaras (1992) build "from scratch" a single transport equation
for an eddy-viscosity variable, the
[Spalart–Allmaras model](/methods/spalart-allmaras-model.md), meant for
aerodynamic Navier–Stokes codes on grids of any structure: the equation is
local except through the wall distance $d$. Algebraic models are rejected as
non-local, two-equation models for their near-wall grid demands, stiffness
and freestream values; the Baldwin–Barth model is the closest relative.

The model is presented in four nested versions, each adding terms passive in
the lower ones so that calibration proceeds layer by layer: (i) free shear
flows (production $c_{b1}|\Omega|\nu_t$ and a non-conservative diffusion with
$c_{b2}$, $\sigma$), calibrated on the
[temporal mixing layer](/benchmarks/temporal-mixing-layer.md) and the plane
wake; (ii) a near-wall destruction $-c_{w1}f_w(\nu_t/d)^2$ with $c_{w1}$ fixed
by equilibrium in the log layer of the
[law of the wall](/definitions/law-of-the-wall.md) and $f_w$ calibrated on
flat-plate skin friction of the
[turbulent boundary layer](/benchmarks/turbulent-boundary-layer.md);
(iii) the working variable $\tilde\nu$ with $\nu_t=\tilde\nu f_{v1}$ and the
modified vorticity, extending the log-layer solution to the wall;
(iv) $f_{t2}$, which makes $\tilde\nu=0$ a stable laminar solution, and a trip
source that starts transition at user-specified points.

An implicit backward-Euler solver with positive (M-matrix) discretizations
and an approximate factorization with sub-iterations keeps $\tilde\nu\ge0$.
Tests: sink flow and the Samuel–Joubert adverse-pressure-gradient boundary
layer, and the [RAE 2822 airfoil](/benchmarks/rae-2822-airfoil.md) Cases 6
and 10 and a blunt-trailing-edge variant. The Case 6 shock sits about 1.5%
chord forward of experiment, and in Case 10 the flow does not reattach after
the shock; the model has no compressibility terms.

# Version read

The conference paper as distributed by AIAA (AIAA 92-0439, 30th Aerospace
Sciences Meeting, Reno, 6–9 January 1992): a scan of a cover sheet plus 22
numbered pages (23 PDF pages), all read visually, equations and constants
checked at 200–300 dpi; "p. N" below is the printed page. This is the
conference version, not the 1994 journal version (La Recherche Aérospatiale
no. 1, a different bibliography entry); the appendix is titled "Summary of
the Model, Version I". Page 1 matches the Crossref metadata; no DOI is
printed. Numbering cited on this page is that of the paper.

The archive also holds a byte-identical copy of this PDF (same MD5),
`0000_manual_no_journal_Unknown_10_2514_6_1992-439.pdf`; it is the same file, not another version.

# Key claims

Page-local symbols: $S_{\mathrm{SA}}$ the modified vorticity (the source's
$\tilde S$); $r$, $g$ the arguments of $f_w$; $\Delta U$ the velocity
difference across a free shear layer or between a field point and the trip;
$|\Omega|_{\mathrm t}$ the wall vorticity at the trip (the source's
$\omega_t$), $d_t$ the distance to the trip, $\Delta x_{\mathrm t}$ the
wall-parallel grid spacing there and $g_t=\min(0.1,\Delta U/(|\Omega|_{\mathrm t}\Delta x_{\mathrm t}))$;
$M_{\mathrm w}$ the momentum of a wake.

1. The model is local, except through $d$, and so compatible with grids of any structure and 2D or 3D Navier–Stokes solvers (Abstract; pp. 1–2). **Stated**
2. Algebraic models are non-local and need decisions that "border on artificial intelligence" with multiple bodies; the authors "abandoned efforts" to generalize them (p. 1). **Stated**
3. Production alone, $D\nu_t/Dt=c_{b1}|\Omega|\nu_t$ (Eq. 1), grows as $\exp(c_{b1}|\Omega|t)$ in homogeneous shear; experiments give growth rates 0.1–0.16, the inhomogeneous calibration 0.13–0.14; Baldwin–Barth and Secundov use at least 0.2 (p. 3). **Stated**
4. Under the basic diffusion of Eq. (2), $D\nu_t/Dt=c_{b1}|\Omega|\nu_t+\sigma^{-1}[\nabla\cdot(\nu_t\nabla\nu_t)+c_{b2}(\nabla\nu_t)^2]$, the integral of $\nu_t^{1+c_{b2}}$ is conserved; for the self-similar axisymmetric wake it increases provided $c_{b2}\le1$ (p. 4). **Derived**
5. Eq. (2) admits the weak ramp $\nu_t=\max(0,A[x+A(1+c_{b2})t/\sigma])$ (Eq. 3), a front moving into non-turbulent fluid iff $c_{b2}>-1$; Secundov's equivalent is 0, Baldwin–Barth's −2 (original) and "somewhat below −1" (published), so its front recedes, which the authors blame for its freestream sensitivity (p. 4). **Derived** / **Stated**
6. $(1+c_{b2})/\sigma$ should exceed 1, and 2 is favourable: above 2 the eddy-viscosity front leads the shear front; 1 gives an exactly triangular mixing-layer profile (p. 4). **Derived** ("approximate analysis")
7. With second-order centred differences, the form $\nu_t\nabla^2\nu_t+(1+c_{b2})(\nabla\nu_t)^2$ yields the weak solution near a $\nu_t=0$ point, while the form of Eq. (2) and two other rearrangements yield the smooth one (p. 4). **Stated**
8. A zero freestream eddy viscosity is recommended; the model is "essentially insensitive" to non-zero values much smaller than those in turbulent regions, a "substantial advantage" over Baldwin–Barth and many two-equation models (p. 4). **Stated**
9. Small $\nu_t$ is amplified by a log-ratio $O(c_{b1})$ outside shear layers but $O(c_{b1}L/\delta)$ inside thin ones, so small values cause "transition" only in thin shear layers (p. 4). **Derived**
10. The free-shear calibration (peak shear stresses $0.01\Delta U^2$ in the mixing layer and $0.06\Delta U^2$ in the wake) leaves a one-parameter family; for $\sigma\in[0.6,1]$, $c_{b2}\in[0.6,0.7]$ and $(1+c_{b2})/\sigma$ from about 2.7 to 1.7; chosen: $\sigma=2/3$, $c_{b1}=0.1355$, $c_{b2}=0.622$, $(1+c_{b2})/\sigma\approx2.4$ (p. 5, Fig. 1). **Shown**
11. In the plane wake the peak eddy viscosity is $0.46M_{\mathrm w}$, "in good agreement with experiment"; no axisymmetric flow was matched; "The model is not intended to be universal" (p. 5). **Shown** / **Stated**
12. Log-layer equilibrium of production, diffusion and destruction requires $c_{w1}=c_{b1}/\kappa^2+(1+c_{b2})/\sigma$, "not negotiable" (p. 6). **Derived**
13. Without $f_w$ the destruction decays too slowly in the outer boundary layer and the flat-plate skin friction is too low (p. 6). **Shown** (stated outcome)
14. $f_w=g[(1+c_{w3}^6)/(g^6+c_{w3}^6)]^{1/6}$, $g=r+c_{w2}(r^6-r)$, $r=\nu_t/(|\Omega|\kappa^2d^2)$ (Eqs. 5–6); $c_{w2}=0.3$ matches $C_f=0.00262$ at $Re_\theta=10^4$, and $c_{w3}=2$ is "reasonable" (p. 6). **Shown**
15. Flat plate at $Re_\theta\approx10^4$: $C_f=0.00262$, shape factor 1.31, Clauser $G\approx6.6$; peak $\nu_t=0.021U_\infty\delta^*$ against $0.0168U_\infty\delta^*$ for Cebeci–Smith (p. 6, Figs. 4–5). **Shown**
16. Ideal near-wall budget in units of production: diffusion $\kappa^2(1+c_{b2})/(\sigma c_{b1})\approx3$, destruction $\approx-4$; it is not kept far into the layer, so $\nu_t$ departs from $\kappa yu_\tau$ but a log layer still forms (p. 7, Fig. 6). **Derived** / **Shown**
17. With $\nu_t=\tilde\nu f_{v1}$, $f_{v1}=\chi^3/(\chi^3+c_{v1}^3)$ (Eq. 7) and $S_{\mathrm{SA}}=|\Omega|+\tilde\nu f_{v2}/(\kappa^2d^2)$, $f_{v2}=1-\chi/(1+\chi f_{v1})$ (Eq. 8), Eq. (9) with molecular diffusion $\sigma^{-1}\nabla\cdot((\nu+\tilde\nu)\nabla\tilde\nu)$ keeps equilibrium "all the way to $d=0$" in a law-of-the-wall situation, a numerically stable solution from a wide range of initial conditions (p. 8). **Shown**
18. $c_{v1}=7.1$ is preferred to Mellor & Herring's 6.9, believed to give a low log-law intercept; no case was found where the choice of $f_{v1}$ mattered (p. 8). **Stated**
19. Linearized for small $\tilde\nu$, Eq. (9) has only production, so $\tilde\nu=0$ is unstable and a code transitions upstream of the trip at a rate set by numerics, "not acceptable"; $f_{t2}=c_{t3}\exp(-c_{t4}\chi^2)$ (Eq. 10) with $c_{t3}=1.1$, $c_{t4}=2$ makes it stable with a small basin (values up to about $\nu/5$), the cross-over at $\chi=\sqrt{\log(c_{t3})/c_{t4}}$ (pp. 8–9). **Shown** / **Derived**
20. "On no account should the turbulence model be trusted to predict the transition location" (p. 8). **Stated**
21. The trip source $f_{t1}\Delta U^2$, $f_{t1}=c_{t1}g_t\exp\big(-c_{t2}\tfrac{|\Omega|_{\mathrm t}^2}{\Delta U^2}[d^2+g_t^2d_t^2]\big)$ (Eqs. 11–12), acts in a roughly semi-elliptic region with integrated contribution $O(U_e\delta)$; $c_{t1}$ worked from 0.1 to 10 ($c_{t1}=1$ chosen); $c_{t2}=2$ reflects laminar values of $\delta|\Omega|_{\mathrm t}/U_e$ (p. 9). **Shown** / **Stated**
22. With backward Euler and M-type implicit operators, $\tilde\nu^{n+1}\ge0$ whenever $\tilde\nu^n\ge0$ (pp. 10–11, Eqs. 21–22, after Baldwin & Barth). **Derived**
23. The central diffusion discretization (Eqs. 27–31) satisfies the M-type constraints for $-1\le c_{b2}\le1$ without the coefficient limiting that Baldwin–Barth needs; $c_{b2}>-1$ "also plays a crucial role in the numerical context" (p. 12). **Derived**
24. No approximate factorization of Eq. (18) keeps unconditional positivity; the chosen diagonally-preconditioned factorization with Steinthorsson–Shih sub-iterations never produced a negative update for time steps from 0.001 to 1000; in practice $\Delta t=10$ with sub-iterations to a relative residual of 0.01 (pp. 13–14). **Shown**
25. Convergence to steady state is "typically as good or better" than with Baldwin–Lomax, attributed to the absence of the "blinking" switch of algebraic models (p. 14). **Shown** / **Stated**
26. Sink flow, acceleration parameter $1.5\times10^{-6}$: $C_f=0.00535$, shape factor 1.35, $Re_\theta=760$, within the experimental ranges (p. 14). **Shown**
27. Samuel–Joubert flow: skin friction slightly high, thicknesses and shape factor low, "a mild but genuine tendency to underpredict the shape factor and thicknesses in adverse pressure gradients"; better than Cebeci–Smith, Baldwin–Lomax and $k$-$\varepsilon$, not as good as Menter's Johnson–King and $k$-$\omega$ results (pp. 14–15, Figs. 7–11). **Shown**
28. RAE 2822 Case 6 (fine grid): shock about 1.5% chord forward of experiment and of Baldwin–Lomax and Johnson–King, within the experimental scatter; $\alpha=2.37°$, $C_D=0.0121$, $C_m=-0.091$ against $2.92°$, 0.0127, −0.095; no wall-shear reversal (p. 16, Figs. 12–13). **Shown**
29. RAE 2822 Case 10: steady on $384\times80$, a limit cycle on $768\times160$ (and on $384\times80$ with halved artificial dissipation); no reattachment after the shock; $\alpha=2.52°$, $C_D=0.0238$, $C_m=-0.104$ against $3.19°$, 0.0242, −0.106 (pp. 16–17, Figs. 14–15). **Shown**
30. Blunt-trailing-edge RAE 2822 Case 1: $\alpha=2.035°$, $C_D=0.0097$, $C_m=-0.061$ against $2.45°$, 0.0098, −0.060; Case 4 at imposed $C_L=0.415$ gives $\alpha=1.94°$, lift slope about 0.155 per degree and a Reynolds-number lift loss of 0.022, "only about 60%" of the experimental loss (pp. 17–19, Figs. 16–20). **Shown**

The appendix (p. 21) prints the constants $c_{b1}=0.1355$, $\sigma=2/3$,
$c_{b2}=0.622$, $\kappa=0.41$, $c_{w1}=c_{b1}/\kappa^2+(1+c_{b2})/\sigma$,
$c_{w2}=0.3$, $c_{w3}=2$, $c_{v1}=7.1$, $c_{t1}=1$, $c_{t2}=2$, $c_{t3}=1.1$,
$c_{t4}=2$, a turbulent Prandtl number 0.9 for heat, $\tilde\nu=0$ at the wall,
freestream and initial values below $\nu/10$, and $r$ truncated "to 10 or so".
These give $c_{w1}=3.239$ and a near-wall diffusion share 3.02
*(compiler check, not in the sources)*. Later sources on the
[Spalart–Allmaras page](/methods/spalart-allmaras-model.md) print
$c_{t3}=1.2$, $c_{t4}=0.5$; this paper prints $c_{t3}=1.1$, $c_{t4}=2$
(p. 9 and appendix).

# Printed slips

- **Vorticity normalization (p. 3):** the paper uses "the vorticity $\omega\equiv\sqrt{\Omega_{ij}\Omega_{ij}}$, where $\Omega_{ij}\equiv\partial U_i/\partial x_j-\partial U_j/\partial x_i$", and states that any candidate is normalized "so that it reduces to $|U_y|$ in a simple shear flow". In simple shear the printed definition gives $\sqrt2|\partial_yu|$, while the printed alternatives $\sqrt{2S_{ij}S_{ij}}$ and $\sqrt{U_{i,j}U_{i,j}}$ give $|\partial_yu|$ *(compiler check, not in the sources)*.
- **Cover sheet against first page:** ZIP code "98214-2207" on the cover, "98124-2207" on p. 1.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $-\overline{u_iu_j}=2\nu_tS_{ij}$ | $R_{ij}=-2\nu_t\langle S_{ij}\rangle$ | no $\tfrac23k\delta_{ij}$ term |
| $U_i$ | $\langle u_i\rangle$ | |
| $\Omega_{ij}=\partial_jU_i-\partial_iU_j$ | $2\Omega_{ij}$ | **collision**: no factor ½ in the source |
| $S$, $\omega$ | $\lvert\Omega\rvert$ | vorticity magnitude, by the source's normalization to $\lvert\partial_yu\rvert$ in simple shear; **collision** with the strain $S$ and the specific dissipation $\omega$ |
| $\tilde S$ | $S_{\mathrm{SA}}$ (page-local) | modified vorticity |
| $\nu_t$, $\tilde\nu$, $\chi=\tilde\nu/\nu$ | $\nu_t$, $\tilde\nu$, $\chi$ | |
| $c_{b1},c_{b2},\sigma,c_{w1..3},c_{v1},c_{t1..4}$ | same | model constants |
| $d$ | $d$ | distance to the closest wall |
| $\omega_t$, $d_t$, $g_t$ | $\lvert\Omega\rvert_{\mathrm t}$, $d_t$, $g_t$ (page-local) | trip quantities |
| $R_\theta$, $H$, $G$ | $Re_\theta$, $\delta^*/\theta$, Clauser $G$ | |
| $K$ | (acceleration parameter) | sink flow |
| $C_d$, $C_l$, $C_m$ | $C_D$, $C_L$, $C_m$ | |
| $\mathbf M,\mathbf P,\mathbf D,\mathbf T$ | (discrete operators) | advection–diffusion, production, destruction, trip |

# Reference list

31 printed references, numbered [1]–[31]; no DOIs. The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this slug.
Many references are AIAA papers printed only with their number, their year
taken from it; ref. [2] (Cebeci & Smith, J. Basic Eng. 92) prints no year; the bibliography keys it `cebeci-1970`, the year Crossref gives for J. Basic Eng. 92:523 (DOI 10.1115/1.3425054); ref. [11] (Secundov et al.) is a
personal communication; ref. [22] (Steinthorsson & Shih) is "submitted" and
kept as such. D. J. Mavriplis (1990), Bradshaw, Ferriss & Atwell (1967) and
Drela (1989, blunt trailing edges) share author–year keys with different works and are keyed `mavriplis-1990-b`, `bradshaw-1967-d` and `drela-1989-b`. No item is unparseable.

# Pages created or updated

Chunk 17 (2026-10-29). This source is cited on:

- [RAE 2822 airfoil](/benchmarks/rae-2822-airfoil.md)
- [Temporally developing mixing layer](/benchmarks/temporal-mixing-layer.md)
- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
