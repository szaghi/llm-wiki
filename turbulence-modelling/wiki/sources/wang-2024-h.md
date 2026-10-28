---
type: Source
title: "Wang & Xu (2024) — Direct numerical simulation of a supersonic turbulent boundary layer with hydrogen combustion"
description: "DNS of a Mach 2.33 flat-plate boundary layer with a sonic hydrogen film and finite-rate chemistry at Re_tau near 1000, against a chemistry-frozen companion: Reynolds-stress recovery, combustion-induced skin-friction reduction by the Renard–Deck decomposition, a priori turbulent Prandtl and Schmidt numbers, strong Reynolds analogies and turbulence–chemistry interaction."
resource: "doi:10.1017/jfm.2024.595"
source_kind: paper
authors: [Wang C., Xu C.]
year: 2024
venue: "J. Fluid Mech. 998:A1"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2024_Crossref_Journal_of_Fluid_Mechanics_Wang_Direct_numerical_simulation_of_a_supersonic_turbulent_bounda.pdf"
tags: [dns, compressible, combustion, boundary-layer, a-priori-a-posteriori]
timestamp: 2026-10-28T07:05:00Z
---

# Summary

Wang & Xu (2024) run a [DNS](/definitions/direct-numerical-simulation.md)
of a non-premixed hydrogen–air flame inside a spatially developing
supersonic flat-plate [boundary layer](/benchmarks/turbulent-boundary-layer.md).
The main stream is vitiated air at $M_\infty=2.33$ and 1700 K. The friction
Reynolds number is about 1000. The chemistry is the 9-species, 19-step
mechanism of Li et al. (2004), and the wall is adiabatic and non-catalytic.
The laminar inlet is a wall jet loosely based on the Burrows–Kurkov
combustor: a sonic cold hydrogen film of height $h_0=4$ mm under a
compressible Blasius main stream. The laminar inlet is a deliberate choice
against turbulent [inflow generation](/methods/inflow-turbulence-generation.md).
A chemistry-frozen companion run on the same $2206\times585\times356$ grid
is the reference. The code is OpenCFD-Comb, the reacting extension of the
OpenCFD family ([OpenCFD-SCU](/software/opencfd-scu.md)).

The inlet gives a two-stage transition, first a mixing-layer instability
and then a boundary-layer one. The excess Reynolds stresses decay
downstream but settle below the canonical adiabatic profiles at the same
$Re_\tau$. The authors attribute this to a lower local friction Reynolds
number caused by non-canonical density and viscosity profiles. The van
Driest and Griffin–Fu–Moin [transformations](/definitions/compressible-velocity-transformation.md)
recover the [log law](/definitions/law-of-the-wall.md) in the inner layer.
Combustion cuts $C_f$ to about 80 % of the non-reacting value, which the
compressible Renard–Deck [skin-friction decomposition](/definitions/skin-friction-decomposition.md)
and a canonical/non-canonical split quantify. The paper evaluates closure
ingredients [a priori](/definitions/a-priori-and-a-posteriori-testing.md).
The [turbulent Prandtl number](/definitions/turbulent-prandtl-number.md) is
about 1.1 in the log region and 0.5–0.9 outside, and the turbulent Schmidt
numbers are species-dependent. The strong Reynolds analogy
([Morkovin's hypothesis](/definitions/morkovin-hypothesis.md)) holds only
for $10<y^+<200$, and its extensions do worse. Laminar chemistry misses the
mean heat release by more than an order of magnitude. A
"drop one fluctuation" diagnostic ranks the hydrogen fluctuations first
among those to be modelled. The introduction reviews LES and
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) of the Burrows–Kurkov
combustor, whose skin-friction predictions disagree on the sign of the
combustion effect.

# Version read

Version of record (Cambridge University Press, open access; received 6
March 2024, revised 23 July 2024, accepted 26 July 2024), 45 pages (A1-1 to
A1-45), all read, with the equation pages checked visually. Page 1 matches
the Crossref metadata; no identity problem.

# Key claims

Notation: streamwise positions are written $x/h_0$ (the source's $x^*$);
$(\cdot)^*$ is semi-local scaling as in the registry (the source's
$(\cdot)^\star$); $Re^*_\tau=\sqrt{\langle\rho\rangle/\rho_w}\,(\mu_w/\langle\mu\rangle)\,Re_\tau$
is the local friction Reynolds number of Patel et al. (2016) (page-local).

1. The authors' preliminary estimate puts $Re_\tau$ in the Burrows–Kurkov experiment above 10 000, "significantly surpassing existing DNS" of compressible boundary layers; its 300 K isothermal wall gives a wall-to-recovery temperature ratio of about 0.09, against 0.15–0.25 in cold-wall DNS (§1.2). **Stated**
2. To the authors' knowledge no DNS of Burrows–Kurkov or similar supersonic combustors resolving the near-wall turbulence existed (§1.2). **Stated**
3. Inflow: main stream $M_\infty=2.33$, $u_\infty=1987$ m/s, $T_\infty=1700$ K, $p=2.76\times10^4$ Pa, $Y_{\mathrm{N_2}}=0.486$, $Y_{\mathrm{O_2}}=0.258$, $Y_{\mathrm{H_2O}}=0.256$; hydrogen stream at Mach 1, 1824 m/s, 254 K, $2.07\times10^4$ Pa, $Y_{\mathrm{H_2}}=1$ (Table 1). **Stated**
4. Resolution of the reacting case at $x/h_0=100$, 125, 150: $\Delta x^+=7.88/6.97/6.46$, $\Delta y^+_w=0.85/0.75/0.69$, $\Delta z^+=4.21/3.73/3.46$, $Re_\tau=1067/1051/1044$, $Re_\theta=2445/2560/2712$, $T_w=1881/1991/2059$ K, within the Poggie et al. (2015) criteria $\Delta x^+<10$, $\Delta y^+<1$, $\Delta z^+<5$; the non-reacting case has $\Delta y^+_w=1.29/1.21/1.17$ (Tables 2–3, §2.3, App. B). **Stated**
5. Ignition makes the boundary layer about 1.5 times thicker than in the non-reacting case at $x/h_0=150$ (§3, Fig. 3, Tables 2–3). **Shown**
6. Transition has two stages: for $0<x/h_0<7.6$ a mixing-layer instability raises the streamwise stress $K_x=\langle\rho u''u''\rangle$ sharply (peak at 7.6) while $C_f$ and the wall hydrogen fraction stay unchanged; beyond 7.6 the boundary-layer instability takes over, the wall hydrogen fraction drops and $C_f$ rises; by $x/h_0=21.7$ the $K_x$ profile is dual-peaked, before combustion matters (§4.1, Figs. 6–7). **Shown**
7. $x/h_0=21.7$ is where the heat release reaches a printed (garbled) fraction of its streamwise maximum; upstream of it reacting and non-reacting statistics coincide (§4.1). **Shown**
8. At $x/h_0=125$ and 150 the van Driest velocity matches the canonical Mach 2, $Re_\tau=1000$ profile up to $y/\delta\approx0.3$ and falls below it in the outer layer; the Griffin–Fu–Moin transformation in semi-local scaling matches the linear and log laws ($\kappa=0.41$, $B=5.2$); the untransformed inner layer already matches well because near-wall density varies slowly (adiabatic wall, near-wall hydrogen) (§4.2, Fig. 8). **Shown**
9. Downstream Reynolds stresses fall below the canonical adiabatic profiles, mainly in the outer region; the peak Reynolds shear stress of both cases plateaus near $x/h_0\approx70$ below the Ceci et al. (2022) correlation, so the deficit is "not limited to the combustion effect" (§4.2, Figs. 9–10a). **Shown**
10. The deficit is attributed to the modulation prefactor $\sqrt{\langle\rho\rangle/\rho_w}\,\mu_w/\langle\mu\rangle$ of $Re^*_\tau$, which in both cases lies below a canonical adiabatic model profile because the temperature is non-monotonic across the cold hydrogen layer (§4.2, Fig. 10b). **Shown**
11. At $x/h_0=50$ $Re^*_\tau$ is larger in the reacting case because hydrogen depletion raises the density ($\sqrt{\langle\rho\rangle/\rho_w}$ "scales with $1-\bar Y_{H_2}$"), so the shear stress decays more slowly; at $x/h_0=150$ heat release raises $T_w$, lowers $Re_\tau$ at the wall and hence $Re^*_\tau$, giving a lower stress plateau (§4.2, Fig. 11). **Shown**
12. At $x/h_0=150$ the reacting $C_f$ is about 80 % of the non-reacting one, through a lower wall shear rate despite a higher $\mu_w$ (§4.3, Fig. 12). **Shown**
13. In the Renard–Deck decomposition at $x/h_0=150$ (reacting) the spatial-development part $C_{f,G}$ is 18 % of $C_f$, the viscous $C_{f,V}$ and turbulent $C_{f,T}$ parts 41 % each; $C_{f,V}$ and $C_{f,T}$ are both lower than in the non-reacting case, $C_{f,T}$ by more (§4.3, Fig. 13a). **Shown**
14. In the canonical/non-canonical split of $C_{f,T}$ the mixing-layer-induced portion is about half at $x/h_0=30$ and nearly vanishes by 70; at 150 the non-canonical part $C_{f,Tn}$ is $-24$ % (reacting) and $-5$ % (non-reacting) of $C_{f,T}$ (§4.3, Eq. 4.5, Fig. 13b). **Shown**
15. Both cases have a non-monotonic mean temperature; in the reacting case at $x/h_0=150$ the temperature peak is at $y^+=795$ and the r.m.s. peak at $y^+=576$; the non-reacting temperature fluctuations peak higher because of steeper mean gradients (§5.1, Fig. 15). **Shown**
16. Premultiplied spanwise spectra of $u$ at $x/h_0=150$ are dual-peaked; the temperature and hydrogen spectra resemble each other and peak near mid-layer at a wavelength of about $\delta/2$ (reacting) (§5.1, Fig. 17). **Shown**
17. $Pr_t$ is discontinuous at the zeros of the $v'$–$T'$ correlation (two in the reacting case, one in the non-reacting case); the authors argue this "may not raise specific concerns" for closures because both $\partial_y\langle T\rangle_\rho$ and $\langle\rho v''T''\rangle$ vanish there; $Pr_t\approx1.1$ in the log region and 0.5–0.9 in the outer layer in both cases, consistent with the film-cooling DNS of Peter & Kloker (2022) (§5.2, Eq. 5.2, Fig. 18). **Shown**
18. Non-reacting $Sc_{t,i}$ rises from the wall to about 0.8 over much of the outer layer; in the reacting case $Sc_{t,i}>1$ near the edge for O$_2$, H$_2$, H$_2$O and N$_2$, $Sc_{t,\mathrm{H_2O}}\approx1$ in the inner layer, the intermediates O, OH, HO$_2$, H$_2$O$_2$ about 0.8 outside with distortions near $y/\delta=0.8$, and $Sc_{t,\mathrm H}$ 0.8–1.5 in the outer region (§5.3, Fig. 19). **Shown**
19. The strong Reynolds analogy (5.4) and its variable-$c_p$ form (5.5) are nearly constant for $10<y^+<200$, the latter closer to unity, and both deviate strongly in the outer region; GSRA, RSRA and HSRA deviate severely and ESRA falls outside the plotted range, because their assumptions fail (Fig. 21) (§5.4, Fig. 20). **Shown**
20. The linear coherence $\xi^2_{u,T}$ is about 0.5 for $y^+<200$ (maximum 0.561) and is lost beyond ($y/h_0>1.62$): large-scale temperature and hydrogen fluctuations do not drive velocity fluctuations of the same scales (§5.4, Fig. 22). **Shown**
21. Near the wall the elementary reactions 3 (OH + H$_2$ ⇔ H + H$_2$O, net negative), 5 (H$_2$ + M ⇔ 2H + M, net negative) and 8 (OH + H + M ⇔ H$_2$O + M, net positive) are non-negligible; all three consume H, 3 and 5 produce H$_2$, and their net effect consumes H$_2$O and produces OH near the wall (§6.1, Fig. 24, Table 4). **Shown**
22. The H$_2$O and H heat-release budgets sum closely to the total heat release; H$_2$O production dominates the outer peak and H depletion the heat release at the wall (adiabatic non-catalytic wall only) (§6.2, Figs. 25–26). **Shown**
23. A one-step global reaction would not capture the near-wall production and consumption of species at an adiabatic non-catalytic wall (§7). **Stated**
24. Laminar chemistry, the source term evaluated at the mean temperature and composition, differs from the true mean heat release by more than an order of magnitude at $x/h_0=68$ and 150 (§6.3, Figs. 27–28). **Shown**
25. In the "drop one fluctuation" diagnostic (Eqs. 6.4–6.6: the true joint p.d.f. with one variable replaced by a delta at its mean), leaving out the H$_2$ fluctuations gives the largest error (overestimation, largest in the outer layer), leaving out O$_2$ underestimates, OH and H give significant errors and H$_2$O, HO$_2$, H$_2$O$_2$ smaller ones; the effect of the temperature fluctuations is smaller at $x/h_0=150$ than at 68 (§6.3, Figs. 27–28). **Shown**
26. $M_{\mathrm{rms}}$ and $M_t$ stay below 0.3, so "compressibility effects are negligible"; the mean pressure varies by less than 4 % across the layer (App. A, Figs. 29–30). **Shown**
27. Spanwise spectra decay at least seven orders of magnitude without pile-up, spanwise autocorrelations reach zero and velocity spectra are dual-peaked; no grid-convergence test was run, because of computational constraints (App. B, Fig. 32). **Shown** (convergence not shown)

The a priori turbulent Prandtl and Schmidt numbers (Eqs. 5.2–5.3), in
registry averaging:

$$Pr_t=\frac{\langle\rho u''v''\rangle\,\partial_y\langle T\rangle_\rho}{\langle\rho v''T''\rangle\,\partial_y\langle u\rangle_\rho},\qquad Sc_{t,i}=\frac{\langle\rho u''v''\rangle\,\partial_y\langle Y_i\rangle_\rho}{\langle\rho v''Y_i''\rangle\,\partial_y\langle u\rangle_\rho}.$$

# Printed slips

- App. B: "The total number of grids employed is 4.6 × 10^9"; the grid of §2.3 gives $2206\times585\times356\approx4.6\times10^8$ *(compiler check, not in the sources)*.
- §7 prints "the one-step global reaction H2 + 2O2 ⇔ 2H2O"; as printed the left side carries 2 H and 4 O atoms and the right side 4 H and 2 O *(compiler check, not in the sources)*.
- §4.2 (p. A1-16): "x∗ = 125 (Reτ = 1067) and x∗ = 150 (Reτ = 1051)"; Table 2 gives $Re_\tau=1067$ at $x/h_0=100$, 1051 at 125 and 1044 at 150.
- §4.1 (p. A1-13): "corresponds to 1L’ of the maximum heat release rate" (corrupted glyph; the percentage is not recoverable).
- §4.1: "Figure 7 presents the profiles of wall-normal velocity ũ"; the Fig. 7 caption reads "Mean velocity profiles" and plots $\tilde u/u_\infty$, the streamwise velocity.
- §4.1: "Since x∗ = 7.6, Kx rapidly decays and attains a local maximum in the streamwise direction", while the preceding paragraph says the decay slows around $x^*=15$ "followed by a slight increase".
- §6.1: "Although elementary reactions 3 and 8 promote the evolution of H2O and OH in opposite directions, reaction 3 exhibits a rate magnitude twice that of reaction 5. With identical stoichiometric coefficients in both reactions…".
- §4.3 (p. A1-21): "the modulation effect results in a negative contribution to Cf,Tc", followed by "Cf,Tn accounts for −24 %"; also "the mixing-layer-induced portion accounts for approximately half of the Cf,Tc" at $x^*=30$.
- Fig. 14(c) is labelled $\bar\tau_{m,xy}$, while the text and caption call it the non-canonical portion $\bar\tau_{n,xy}$; the Fig. 18 caption prints "(a,c,e) Reacting case (black). (b,d,e) Non-reacting case (blue)".
- $\bar\tau^+_{t,xy}$ is normalized by $\bar\rho_wu_\tau^2$ in §4.2 and by $\bar\rho u_\tau^2$ in Eq. (4.4) and the text around it.
- Eq. (2.3) prints $\nabla(\boldsymbol\tau\cdot\boldsymbol u+\boldsymbol q)$ without the divergence dot, while Eq. (2.4) prints $\nabla\cdot$.
- App. A states that "the mean temperature and density are not inversely proportional because of the non-ideal gas law employed", while Eq. (2.5) is Dalton's law $p=\sum_i\rho_iR_0T/M_i$.
- Table 2 header "Tw (K)" against Table 3 "T̄w (K)"; the main-stream thickness is written $\delta_{m,0}$ in §2.3 and $\delta_{0,m}$ in App. B.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar\alpha$, $\alpha'$ | $\langle\alpha\rangle$, $\alpha'$ | time and spanwise Reynolds average (time only in the spectra); **collision:** the registry overbar is the LES filter |
| $\tilde\alpha$, $\alpha''$ | $\langle\alpha\rangle_\rho$, $\alpha''$ | Favre average |
| $\overline{\rho u''u''}$, $-\overline{\rho u''v''}$ | $\langle\rho u''u''\rangle$, $-\langle\rho u''v''\rangle$ | registry $R_{ij}$ in Favre form; positive trace |
| $(\cdot)^*$ ($x^*=x/h_0$) | $x/h_0$ | **collision:** the registry $(\cdot)^*$ is semi-local scaling |
| $(\cdot)^\star$ | $(\cdot)^*$ | semi-local scaling with $\langle\nu\rangle/\sqrt{\tau_w/\langle\rho\rangle}$ |
| $Re_\tau^\star$ | $Re^*_\tau$ | local friction Reynolds number (page-local) |
| $Ma_\infty$, $Ma_t$, $Ma_\tau$ | $M_\infty$, $M_t$, $M_\tau$ | |
| $K_x$ | $K_x=\langle\rho u''u''\rangle$ | page-local, no factor 1/2 |
| $C_{f,V}$, $C_{f,T}$, $C_{f,G}$, $C_{f,Tc}$, $C_{f,Tn}$ | same | Renard–Deck parts, normalized by $\rho_\infty u_\infty^3$ |
| $Pr_t$, $Sc_{t,i}$ | $Pr_t$, $Sc_{t,i}$ | $Sc_{t,i}$ page-local |
| $\kappa$ | $\kappa$ (log law, 0.41); thermal conductivity in Eq. (2.7) | **collision** inside the source |
| $M$, $M_i$, $W_i$ | number of reactions (19), third body; molar mass (both $M_i$ and $W_i$) | **collision** with the Mach number $M$ |
| $\xi^2_{u,T}$ | $\xi^2_{u,T}$ (linear coherence, page-local) | **collision** with the reference coordinate $\xi$ |
| $\hat\alpha$ | $\alpha_{\boldsymbol k}$ (Fourier coefficient, §5); sample-space variable of a p.d.f. (§6.3) | **collision:** the registry hat is the test filter |
| $\breve{\dot\omega}_T$ | "assumed" mean heat release with one fluctuation suppressed | page-local |
| $\dot\omega_i$, $\dot\omega_T$ | species production rate, heat-release rate | **collision** with $\omega$ and $\omega_i$ |
| $\alpha=0.25$ | grid-stretching parameter of Eq. (2.11) | not the DG blending factor |
| $\kappa=0.41$, $B=5.2$ | $\kappa$, $B$ | log-law constants |
| $H=\delta_d/\theta$ | $\delta^*/\theta$ | shape factor |

# Reference list

99 printed references, author–year style (JFM), alphabetical, no DOIs. The
list is merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug; Liu (2017a, b), Yu & Xu (2022) and Yu et al. (2022b),
Yu et al. (2023a, b) take suffixes in printed order. The keys that the
convention gives to Li et al. (2022, Phys. Fluids 34:085102), Yan et al.
(2022, JFM 941:A55), Xu et al. (2023, JFM 965:A4) and Yu et al. (2023b, JFM
972:A32) belong to other works in the bundle; these four are keyed `li-2022-o`, `yan-2022-c`, `xu-2023-c` and `yu-2023-d`;
Cogo et al. (2022), Yu et al. (2023a) and Wei et al. (2023) are the
ingested sources of those keys. Lin et al. (2023) is an arXiv preprint and
enters as its own entry.

# Pages created or updated

Chunk 13 (2026-10-28). This source is cited on:

- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Compressible velocity transformations](/definitions/compressible-velocity-transformation.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Morkovin's hypothesis and Reynolds analogies](/definitions/morkovin-hypothesis.md)
- [Skin-friction decomposition](/definitions/skin-friction-decomposition.md)
- [Turbulent Prandtl number and turbulent heat-flux models](/definitions/turbulent-prandtl-number.md)
- [Inflow turbulence generation](/methods/inflow-turbulence-generation.md)
- [OpenCFD-SCU](/software/opencfd-scu.md)
