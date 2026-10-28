---
type: Source
title: "Devenport & Lowe (2022) — Equilibrium and non-equilibrium turbulent boundary layers"
description: "Review of incompressible high-Reynolds-number turbulent boundary layers organised by equilibrium as self-preservation: log and defect laws, similarity analysis of pressure-gradient layers, rough walls and wall similarity, response lengths, step changes in roughness, and the shear-stress lag of three-dimensional boundary layers."
resource: "doi:10.1016/j.paerosci.2022.100807"
source_kind: paper
authors: [Devenport W.J., Lowe K.T.]
year: 2022
venue: "Prog. Aerosp. Sci. 131:100807"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Progress_in_Aerospace_Sciences_Devenport_Equilibrium_and_non-equilibrium_turbulent_boundary_layers.pdf"
tags: [review, boundary-layer, rans, wall-model, anisotropy]
timestamp: 2026-10-27T20:38:00Z
---

# Summary

Devenport & Lowe (2022) review the physics of incompressible,
high-Reynolds-number [turbulent boundary layers](/benchmarks/turbulent-boundary-layer.md)
under one organising concept: *equilibrium* as self-preservation, all
normalised flow properties self-similar on one consistent set of scales.
Compressibility, separation, curvature, transition, free-stream
turbulence and heat transfer are excluded. The review supplies reference
physics for RANS closures, [wall functions](/methods/rans-wall-function.md)
and wall-modelled LES; it proposes and tests no turbulence model.

Section 2 derives the thin-layer equations, the momentum integral, the
[law of the wall](/definitions/law-of-the-wall.md) (Rotta's overlap
argument as the most general route to the log law, $\kappa$ not universal),
the defect and Coles wake laws, the rough-wall log law with the roughness
function, the Reynolds-stress and turbulent-kinetic-energy transport
equations and a RANS vorticity transport equation, and summarises the
zero-pressure-gradient structure, the
[attached-eddy hypothesis](/definitions/attached-eddy-hypothesis.md) and
Townsend's wall similarity for rough walls. Section 3 shows by a
similarity analysis that outer-region self-preservation needs a power-law
(or, for constant thickness, exponential) edge velocity at constant
Clauser parameter, argues against Castillo & George's broader sufficient
condition, and compiles equilibrium adverse-pressure-gradient studies
([wall law in adverse pressure gradient](/definitions/adverse-pressure-gradient-wall-law.md)).
Section 4 estimates response lengths and reviews non-equilibrium
pressure-gradient layers, rough walls in pressure gradient (evidence for
wall similarity sparse and contradictory) and step changes in roughness
with internal boundary layers. Section 5 treats three-dimensional layers:
skewing angles, the lag of the shear-stress angle behind the flow-gradient
angle and the depression of Townsend's structure parameter, both traced to
pressure–strain redistribution (the mechanism of
[Reynolds-stress models](/methods/reynolds-stress-model.md)), which an
isotropic eddy viscosity ([Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md))
cannot represent. The suddenly imposed spanwise pressure gradient in
[channel flow](/benchmarks/turbulent-channel-flow.md) (from
[DNS](/definitions/direct-numerical-simulation.md)) and the
[NASA Juncture Flow](/benchmarks/nasa-juncture-flow.md) are cited
examples. Evidence is mostly that of the cited works; the
self-preservation argument, the response-length estimates and the
sublayer skewing estimate are the authors' own.

# Version read

Version of record (Elsevier, open access CC BY-NC-ND; received 30 August
2021, revised 31 January 2022, accepted 4 February 2022, online 29 March
2022), 50 pages (46 of text, 4 of references), all read; the
equation-heavy pages were read visually. Page 1 matches the metadata; no
identity issue. A review: equation and section numbers are those of this
version.

# Key claims

Page-local symbols: $\Lambda_{\mathrm{CG}}$ the Castillo–George
pressure-gradient parameter, $m$ the edge-velocity exponent
($U_e\propto|x-x_o|^m$), $K=(\nu/U_e^2)\mathrm dU_e/\mathrm dx$ the
acceleration parameter, $H=\delta^*/\theta$ the shape factor, $k_s$,
$k_g$, $k_o$ the equivalent sand-grain, geometric and hydrodynamic
roughness lengths, $\Delta U^+$ the roughness function, $\Pi_{\mathrm w}$
the Coles wake factor, $A_1=-\langle u'v'\rangle/(2k)$ Townsend's
structure parameter, $\gamma_{\mathrm{FA}}$, $\gamma_{\mathrm{FGA}}$,
$\gamma_{\mathrm{SSA}}$ the flow, flow-gradient and shear-stress angles,
$P^+=\langle p\rangle/(\rho u_\tau^2)$, $\mathscr L_\tau$, $\mathscr L_p$,
$\mathscr L_k$ the response lengths. $y$ is wall-normal, $z$ lateral.

1. Equilibrium is self-preservation: all properties self-similar on one consistent set of scales, the normalised flow independent of $x$; "local" and "approximate" equilibrium are distinguished (§1, §3). **Stated**
2. Rotta's argument (viscosity independence in the overlap) is "the most general" derivation of the log law, $u^+=\kappa^{-1}\ln y^++B$, with $\kappa$ often 0.41 and $B=5.0$ (§2.1, Eqs. 2.24–2.25). **Derived**
3. $\kappa$ is not settled: 0.38–0.39 are reported for zero-pressure-gradient boundary layers; Monkewitz et al.'s $\kappa=0.384$, $B=4.17$ differ from 0.41, 5.0 by 0.4% and 1.4% in $u^+$ at $y^+=100$ and 1000 (§2.1). **Stated** *(compiler check, not in the sources: 16.16 against 16.23 and 22.16 against 21.85, consistent.)*
4. $k_o^+\approx0.129$ for $\kappa=0.41$, $B=5.0$; $k_o=k_se^{-\kappa(B+3.5)}\approx0.031k_s$; fully rough flow commonly $k_s^+\gtrsim50$; wall similarity needs $\delta/k_g\gtrsim50$ (Jiménez) (§2.1). **Stated**
5. In the zero-pressure-gradient layer $\langle u'v'\rangle$ and $\langle v'^2\rangle$ scale on $u_\tau$ throughout; the inner peak of $\langle u'^2\rangle/u_\tau^2$ near $y^+\approx15$ grows with $\log Re$, attributed to the footprint of outer large-scale "inactive" motions (§2.2, Figs. 4–6). **Stated**
6. Outside the roughness layer rough-wall stresses agree with smooth-wall ones on $u_\tau$ (wall similarity) for $y/\delta\gtrsim0.15$ when $\delta/k_g\gtrsim50$; Mehdi et al. argue it is unlikely below the location of maximum shear stress, of order $\sqrt{Re_\tau}$ in wall units (§2.2). **Stated**
7. A RANS vorticity transport equation has the turbulent term $\partial_j(\langle u_i'\omega_j'\rangle-\langle\omega_i'u_j'\rangle)=-\epsilon_{ijk}\partial_k\partial_lR_{lj}$; its two-dimensional boundary-layer form mirrors the streamwise momentum equation with one more wall-normal derivative (§2.3, Eqs. 2.53–2.56). **Derived**
8. In a mean two-dimensional layer $\langle v'\omega_z'\rangle<0$, by a mixing-length-type argument analogous to $\langle u'v'\rangle<0$ (§2.3, Fig. 9). **Derived** (heuristic)
9. Self-preservation needs a defect velocity scale proportional to $U_e$ and constant $\Lambda_{\mathrm{CG}}$, so $U_e\propto L_o^{-\Lambda_{\mathrm{CG}}}$; requiring an $x$-independent shear-stress correlation-coefficient profile further forces $\mathrm dL_o/\mathrm dx=$ const, hence $U_e\propto|x-x_o|^m$ with $m=-\Lambda_{\mathrm{CG}}$. The authors use this against Castillo & George's claim that Eq. 3.12 alone suffices (§3.1, Eqs. 3.8–3.17). **Derived**
10. Complete self-preservation, viscous term included, is possible only for the sink flow $U_e\propto(x_o-x)^{-1}$; the constant-thickness case gives an exponential edge velocity, possible only in favourable pressure gradient (§3.1, Eqs. 3.18–3.22). **Derived**
11. With $u_\tau$ and $\delta$ as scales, matching to the log law forces constant $\delta/k_o$: constant $Re_\tau$ (smooth wall, sink flow only) or constant $k_s/\delta$ (fully rough), so exactly self-preserving rough-wall layers exist for any constant-$m$ pressure gradient with suitably scaled roughness (§3.2, Eqs. 3.24–3.25). **Derived**
12. For power-law edge velocity $m/\beta_{RC}=-(C_f/2)(x-x_o)/\delta^*$; with Rotta's and Skote et al.'s $m=-\beta_{RC}/(H(1+\beta_{RC})+2\beta_{RC})$ the $m$–$\beta_{RC}$ relation is not unique at finite $Re$; compiled data (Table 1, Fig. 10) roughly follow Clauser's expectation, $|m|$ levelling near 0.25, with scatter partly explained by $H$ (§3.2, Eqs. 3.27–3.28). **Derived**, data compilation **Shown**
13. Equilibrium adverse-pressure-gradient layers are hard to set up and depend on initial conditions (Bobke et al.: $\beta_{RC}$ drifts); an adverse gradient lowers the log region in DNS and LES but not in some higher-$Re$ experiments; the Clauser-plot method fails for $\beta_{RC}>2$ (Monty et al.) (§3.3). **Stated**
14. An adverse gradient raises outer turbulence: peak shear stress about $2.6\tau_w$ at $\beta_{RC}=2$ (Bobke et al.), about $16\tau_w$ at $\beta_{RC}=20$ (Skåre & Krogstad), with transport terms up to an order of magnitude above zero-pressure-gradient levels on outer scaling (§3.3, Fig. 15). **Stated**
15. Sink-flow turbulence cannot be sustained for $K\gtrsim3.0\times10^{-6}$ (Spalart 1986); favourable gradients thicken the sublayer, raise the log region and attenuate the wake (§3.3). **Stated**
16. Response lengths: $\mathscr L_\tau=2\theta/C_f\approx50\delta$ for a change in wall condition, $\mathscr L_p=2\theta/(C_f\beta_{RC})$ for a change in pressure gradient, and for the turbulence structure about $3\delta$ ignoring dissipation, "above 30" $\delta$ allowing for it (§4.1, Eqs. 4.1–4.7). **Derived** (order of magnitude)
17. Non-equilibrium adverse-gradient layers lag the local $\beta_{RC}$: outer-stress increases are about half the equilibrium values at $\beta_{RC}\approx2$, while the inner region ($y^+\lesssim25$) adapts almost immediately (Bobke et al. 2017) (§4.2). **Stated**
18. Near separation the outer region scales as an embedded shear layer on the inflection-point defect and vorticity thickness (Schatzman & Thomas; Balantrapu et al.), read as a decoupling of the outer flow from the wall (§4.2, Fig. 20). **Stated**
19. Evidence for wall similarity in rough-wall pressure-gradient flows is contradictory and mostly fails the conditions needed to test it; variations of $k_s/k_g$ with flow development are reported. The authors call for fully rough, small-roughness, high-$Re$ experiments with direct skin-friction measurement (§4.3, §6). **Stated**
20. After a smooth-to-rough step $C_f$ jumps from 0.00255 to over 0.01, overshooting the final value of about 0.0068 reached after about $40\delta$ (Efros & Krogstad); the internal layer grows as $x^{0.73}$ there; a new self-preserving layer forms after 20–50 initial $\delta$ (§4.4, Fig. 25). **Stated**
21. Rough-to-smooth recovery is much slower than smooth-to-rough; a roughness strip produces two internal layers and a "stress bore" still visible $55\delta$ downstream (§4.4, Tables 3–4, Figs. 27–29). **Stated**
22. Nearly all three-dimensional boundary layers are non-equilibrium; the known equilibrium ones (Ekman layer, rotating disk) are constant-thickness, wall-homogeneous flows with a depressed wake (§5, §5.2). **Stated**
23. The sublayer solution gives $\gamma_{\mathrm{FA}}\approx(\partial P^+/\partial z^+)y^+/((\partial P^+/\partial x^+)y^++2)$; with $\partial P^+/\partial x_i^+\approx8\beta_{RC}/Re_\tau$ and the gradient along $z$, $\gamma_{\mathrm{FA}}\approx4\beta_{RC}y^+/Re_\tau$: sublayer skewing is nonzero but scales as $Re_\tau^{-1}$ (§5.3, Eq. 5.9). **Derived** (the authors' own; see Printed slips for the quoted angles)
24. Two near-universal observations in three-dimensional layers: $\gamma_{\mathrm{SSA}}$ lags $\gamma_{\mathrm{FGA}}$, and $A_1$ falls below two-dimensional values (e.g. the shear-stress direction turns one third as much as the flow on Bradshaw & Pontikos's swept wing; a lag of about $60t^+$ in Lozano-Durán et al.'s channel) (§5.4, Figs. 37–39). **Stated**
25. Both stem from pressure–strain: suppression of its source of $\langle v'^2\rangle$ reduces the production of both shear stresses (Moin et al.; Lozano-Durán et al.), and Rotta's analysis attributes the misalignment to skewing acting through the anisotropic rapid pressure–strain (§5.4, Figs. 40–42). **Stated**
26. The authors propose $\partial P^+/\partial z^+$ (not Lozano-Durán et al.'s ratio of lateral to streamwise gradients) as the non-equilibrium parameter of boundary layers; sublayer skewing of about 3° at $y^+=3$ or more would mean a shear-stress reduction of at least 5% (§5.4, footnote 6). **Derived** (heuristic)
27. Isotropic eddy-viscosity RANS models assume $\gamma_{\mathrm{SSA}}=\gamma_{\mathrm{FGA}}$, contradicted by the persistent misalignment in three-dimensional layers; methods that do not resolve roughness (almost all RANS and LES) must assume wall similarity and a $k_s/k_g$ independent of pressure gradient and history (§5.1, §6). **Stated**

# Printed slips

- **Eq. 2.33:** the Clauser–Rotta thickness is printed $\Delta=\int_0^\delta\frac{U_e-U_1}{u_\tau}\mathrm dx_2=\delta^*\sqrt{C_f/2}$. *(Compiler check, not in the sources: with the paper's $\delta^*=\int_0^\delta(1-U_1/U_e)\mathrm dx_2$ and $C_f=\tau_w/\tfrac12\rho U_e^2$, the integral is $\delta^*U_e/u_\tau=\delta^*\sqrt{2/C_f}$.)*
- **Eq. 3.30:** $K_r=\frac{k_g}{U_e}\frac{\mathrm dU_e}{\mathrm dx_1}\equiv-\frac{C_f}{4}\frac{k_g}{\delta^*}\beta$. *(Compiler check, not in the sources: from the paper's $\beta=(\delta^*/\tau_w)\mathrm dP_e/\mathrm dx_1$, $P_e=P_{o\infty}-\tfrac12\rho U_e^2$ and its $C_f$, the factor is $C_f/2$; Eq. 3.29 for $K$, checked the same way, is consistent.)*
- **§5.3:** for $\beta=5$ at $x_2^+=3$ the skewing is quoted as "about 1.7° and 0.17° for $Re_\tau=1000$ and 10,000". *(Compiler check, not in the sources: the paper's $\gamma_{FA}\approx4\beta x_2^+/Re_\tau$ gives 0.06 rad, about 3.4°, and 0.34°.)*
- **Eqs. 3.8–3.10, 3.19–3.20:** the derivative of the normal-stress scale is printed $\mathrm dU_{22}^2/\mathrm dx_2$ (and $\frac{L_o}{U_e}\frac{\mathrm dU_e}{\mathrm dx_2}$ in 3.20), though $U_{22}$ and $U_e$ are functions of $x_1$ only and the term comes from the $x_1$-derivative in Eq. 2.15.
- **§4.1:** the dissipation is printed $\varepsilon\equiv\nu\overline{(\partial u_j/\partial x_j)^2}$, which with the repeated index is the squared divergence; Eqs. 2.43–2.45 print $\nu\overline{(\partial u_i/\partial x_j)^2}$.
- **§2.3 (with Eq. 2.57):** "$U_1=\partial\Psi/\partial x_2$ and $U_2=\partial\Psi/\partial x_1$". *(Compiler check, not in the sources: the paper's continuity equation 2.5 with $U_1=\partial\Psi/\partial x_2$ requires $U_2=-\partial\Psi/\partial x_1$.)*
- **§5.1:** $\gamma_{FA}(x_2)=\tan^{-1}U_3(x_2)/U_1(x_1)$, with argument $x_1$ in the denominator.
- **§5.4:** Eqs. (6.1)–(6.2) are numbered as if in a Section 6; $\mathrm{Gain}_{22}$ is printed with $\overline{\varphi_{12}}$ in its numerator over $\overline{\Pi_{22}}(0)$.
- **p. 35:** "Andreopoulos and Wood [178]"; [178] is Wood (1982), Andreopoulos & Wood is [172].
- The TKE budget is cited as Eq. (2.43) (§3.3), (2.44) (§4.1) and (2.45) (Fig. 7 caption); Fig. 8 caption "Schlatter et al. (2010, 1011)".
- Name spellings against the reference list: "Raupach and Raupach and Tom", "Pailas", "Lureiro"/"Louriero", "Jocobi", "Medhi", "Elliot", "Ferris", "Faulkner Skan".
- The paper still cites [213] (Ekman-layer DNS) for Fig. 32 although its own [215] is a retraction notice of [213].
- Printed duplicates in the reference list: [42]=[225], [70]=[95], [93]=[134], [194]=[203].

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $x_1$, $x_2$, $x_3$ | $x$, $y$, $z$ | streamwise, wall-normal, lateral |
| $U_i$, $u_i$, $\overline{(\cdot)}$ | $\langle u_i\rangle$, $u_i'$, $\langle\cdot\rangle$ | **collision:** overbar is the time average |
| $\overline{u_iu_j}$ | $R_{ij}$ | kinematic, positive trace |
| $P$, $p$, $P_e$ | $\langle p\rangle$, $p'$, $P_e$ (page-local) | not kinematic |
| $\Omega_i$, $\varpi_i$ | $\langle\omega_i\rangle$, $\omega_i'$ | **collision:** $\Omega_{ij}$ is the rotation tensor |
| $\kappa$, $A$ | $\kappa$, $B$ | log-law intercept; Fig. 33 prints $B$ |
| $\beta=(\delta^*/\tau_w)\mathrm dP_e/\mathrm dx_1$ | $\beta_{RC}$ | Clauser parameter |
| $\Lambda$ | $\Lambda_{\mathrm{CG}}$ (page-local) | Eq. 3.11 |
| $\Delta$ | $\Delta_{\mathrm{CR}}$ (page-local) | **collision** with the filter width |
| $\Pi$, $W$ | $\Pi_{\mathrm w}$, $W$ (page-local) | **collision** with the SGS flux $\Pi$ |
| $\Pi_{ij}$, $\mathscr P_{ij}$ | (pressure–strain, production of $R_{ij}$) | |
| $\varepsilon$ | $\varepsilon$ | |
| $k=\tfrac12\overline{u_i^2}$ | $k$ | |
| $\delta$, $\delta^*$, $\theta$, $C_f$, $u_\tau$, $Re_\tau$ | same | $\delta$ is the whole rotational region, not $\delta_{99}$ |
| $\gamma_{FA}$, $\gamma_{FGA}$, $\gamma_{SSA}$ | $\gamma_{\mathrm{FA}}$, $\gamma_{\mathrm{FGA}}$, $\gamma_{\mathrm{SSA}}$ (page-local) | not the ratio of specific heats |
| $A_1$ | $A_1$ (page-local) | $\approx0.15$ in 2-D layers |
| $\alpha_i$, $\beta_1$, $\beta_3$ (van den Berg) | (page-local) | not $\beta_{RC}$ |
| $\mathscr L_\tau$, $\mathscr L_p$, $\mathscr L_k$ | same (page-local) | §4.1 |
| $U_d$, $\delta_\omega$ | (page-local) | inflection-point defect, vorticity thickness; $U_d$ reused in §5.3 |

# Reference list

231 printed references, numbered style, without DOIs. The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this
slug; the printed duplicates [42]/[225] (DeGraaff & Eaton 2000), [70]/[95]
(Krogstad et al. 1992), [93]/[134] (Bradshaw & Ferriss 1965) and
[194]/[203] (Rotta 1979) are one entry each. [76] has a garbled author
list and no arXiv identifier; [80] prints its first author split ("G. de,
D. Allen"); [72] prints "Krogstadt"; [113] and [115] lack book titles and
[196], [210], [216], [219], [226] a venue; [43] is a private
communication; [215] is the retraction notice of [213]. The cited
Lozano-Durán et al. (2020) is another work than the ingested
[lozanoduran-2022](/sources/lozanoduran-2022.md) and
[lozanoduran-2023](/sources/lozanoduran-2023.md).

# Pages created or updated

Chunk 11 (2026-10-27). This source is cited on:

- [NASA Juncture Flow](/benchmarks/nasa-juncture-flow.md)
- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Wall law in adverse pressure gradient](/definitions/adverse-pressure-gradient-wall-law.md)
- [Attached-eddy hypothesis](/definitions/attached-eddy-hypothesis.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Wall functions for RANS](/methods/rans-wall-function.md)
- [Differential Reynolds-stress models](/methods/reynolds-stress-model.md)
