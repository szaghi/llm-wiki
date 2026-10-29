---
type: Source
title: "Launder & Spalding (1974) — The numerical computation of turbulent flows"
description: "Review and position statement of the Imperial College group that fixes the standard k-ε model, its constants, the log-layer argument for choosing ε as length-scale variable, the standard wall functions, the Jones–Launder low-Reynolds form and the algebraic-stress extension, illustrated on nine engineering flows."
resource: "doi:10.1016/0045-7825(74)90029-2"
source_kind: paper
authors: [Launder B.E., Spalding D.B.]
year: 1974
venue: "Comput. Methods Appl. Mech. Eng. 3:269-289"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/1974_Crossref_Computer_Methods_in_Applied_Mechanics_and_Engineering_Launder_The_numerical_computation_of_turbulent_flows.pdf"
tags: [rans, eddy-viscosity, k-epsilon, wall-model, boundary-layer]
timestamp: 2026-10-29T16:21:00Z
---

# Summary

Launder & Spalding (1974) argue that, with the computers of 1973, the best
compromise between economy, range of applicability and physical realism is a
two-equation eddy-viscosity model transporting $k$ and $\varepsilon$, and they
state that model in the form later cited as the standard
[$k$-$\varepsilon$ model](/methods/k-epsilon-model.md): the transport equations
(2.2-1)–(2.2-3) with $C_\mu=0.09$, $C_{\varepsilon1}=1.44$,
$C_{\varepsilon2}=1.92$, $\sigma_k=1.0$, $\sigma_\varepsilon=1.3$ (Table 2.1,
after Launder et al. 1972) and the
[Boussinesq relation](/definitions/boussinesq-hypothesis.md) (2.4-1).

§2.1 justifies $\varepsilon$ over the alternative length-scale variables
$kL$ and $W$: the variables are interconvertible, but gradient diffusion of
the third-order correlations is not invariant under the change, and in the
constant-stress near-wall layer the generalized length-scale equation
reduces to an algebraic constraint among the constants that only the
$k$-$\varepsilon$ choice satisfies with a diffusion Prandtl number compatible
with free-shear spreading (1.3, against −0.8 for $kL$ and 2.9 for $W$).
§2.2 adds Rodi's round-jet modification of $C_\mu$ and $C_{\varepsilon2}$.
§2.3 gives two near-wall treatments: the
[wall functions](/methods/rans-wall-function.md) for momentum, heat and the
near-wall dissipation, built on the
[law of the wall](/definitions/law-of-the-wall.md) with the velocity scale
$C_\mu^{1/4}k_P^{1/2}$, and the Jones–Launder low-Reynolds-number model
integrated to the wall. §2.4 sketches the implicit algebraic stress model
obtained from the [Reynolds-stress transport equation](/methods/reynolds-stress-model.md)
by neglecting or approximating convection and diffusion, the precursor of
[explicit algebraic Reynolds-stress models](/methods/explicit-algebraic-reynolds-stress-model.md).

§3 shows nine flows computed by the group (figures only): plane jet in a
moving stream, wall jets on cones, low-Reynolds-number pipe flow,
turbine-blade heat transfer with transition, film cooling behind a thick lip,
confined coaxial jets, a ventilated room, twisted-tape tubes (poorer
agreement) and the square duct, whose secondary flow needs the algebraic
stress model. §4 calls for wall functions embodying the low-Reynolds model
and for tested replacements of the isotropic viscosity.

# Version read

Version of record (North-Holland typeset; received 13 August 1973), as a
scanned image PDF with an OCR layer that garbles every equation; all
equations were read visually from the page images, 21 pages (pp. 269–289),
all legible. Page 1 matches the Crossref metadata; no DOI is printed on the
scan. Numbering cited on this page is that of the paper.

# Key claims

Page-local symbols: $L$ the length scale of the energy-containing eddies
(the source's $l$) and $c_l$ the constant of its definition (the source's $C_D$, not the drag
coefficient); $W$ the squared vorticity-fluctuation variable (dimension
time$^{-2}$); $\sigma_t$ the diffusion Prandtl number of a generalized
length-scale variable $k^{m}/L^{n}$; $E$ the log-law wall constant (as on
the [law of the wall](/definitions/law-of-the-wall.md); the total energy
does not occur on this page); $P$ the first node off the wall and
$y_P$ its distance, $k_P$, $\langle u\rangle_P$ the values there; $R_t=k^2/(\nu\varepsilon)$;
$\varepsilon_{ij}$ the dissipation tensor; $C_t$ the Craya–Curtet number.

1. Models are needed because resolving millimetre eddies over metre- or kilometre-scale domains needs "an immense and totally impractical number of nodes" (§1.1). **Stated**
2. A good model has "extensive universality" (one constant set for many flows) and limited complexity, counted in differential equations and empirical constants (§1.1). **Stated**
3. At the 1972 NASA Langley free-shear-flow conference the $k$-$\varepsilon$ model was "surpassed only by admittedly more complex 'Reynolds-stress' models" (Launder, Morse, Rodi & Spalding [19]) (§1.2). **Stated**
4. Two-equation models using $kL$, $W$ or $\varepsilon$ are interconvertible (Eqs. 2.1-5, 2.1-6) and differ "merely in mathematical form, and not in content" if transformed exactly, but gradient-diffusion modelling of the triple correlations cannot be transformed without introducing gradients of $k$ (§2.1). **Derived**
5. With a uniform length scale the transformations are nearly exact: $d(kL)/kL\approx dk/k$, $dW/W\approx dk/k$, $d\varepsilon/\varepsilon\approx\tfrac32dk/k$ (Eqs. 2.1-7 to 2.1-9). **Derived**
6. In the constant-stress layer with uniform $k$ and $L\propto y$, the generalized equation (2.1-10) reduces to $n^2/\sigma_t+C_1C_\mu^{1/2}/\kappa^2-C_2C_\mu^{1/2}/\kappa^2=0$ (2.1-11), with the log law $\langle u\rangle/(\tau/\rho)^{1/2}=\kappa^{-1}\ln[Ey(\tau/\rho)^{1/2}/\nu]$ (2.1-12) and $\mu_t=C_\mu\rho k^{1/2}L$ (2.1-13) (§2.1). **Derived**
7. With "the proper values" of the constants, (2.1-11) gives $\sigma_t=-0.8$ for $kL$ ($n=-1$), 2.9 for $W$ ($n=2$) and 1.3 for $\varepsilon$ ($n=1$); only the last fits free-shear spreading, so only $k$-$\varepsilon$ avoids making a "constant" depend on $y/L$ (§2.1). **Derived** (the values of $\kappa$ and of the $m,n$-dependent $C_1$, $C_2$ are not printed)
8. The $\varepsilon$-equation (2.2-1) "was first developed and used in the Imperial College group by Hanjalić [17]" (§2.2). **Stated**
9. Recommended constants (Table 2.1, after [19]): $C_\mu=0.09$, $C_{\varepsilon1}=1.44$, $C_{\varepsilon2}=1.92$, $\sigma_k=1.0$, $\sigma_\varepsilon=1.3$, fitted to plane jets and mixing layers and expected equally satisfactory near walls; the high-Reynolds equations are $Dk/Dt=\partial_j[(\nu_t/\sigma_k)\partial_jk]+P_k-\varepsilon$, $D\varepsilon/Dt=\partial_j[(\nu_t/\sigma_\varepsilon)\partial_j\varepsilon]+C_{\varepsilon1}(\varepsilon/k)P_k-C_{\varepsilon2}\varepsilon^2/k$, $\nu_t=C_\mu k^2/\varepsilon$, with $P_k=\nu_t(\partial_k\langle u_i\rangle+\partial_i\langle u_k\rangle)\partial_k\langle u_i\rangle$ (Eqs. 2.2-1 to 2.2-3, §2.2). **Stated**
10. No single constant set predicts axisymmetric jets with plane free shear flows and wall flows; the recommended fix is $C_\mu=0.09-0.04f$, $C_{\varepsilon2}=1.92-0.0667f$ with Rodi's centre-line-decay function $f$ (Eqs. 2.2-4 to 2.2-6), for which "little universality can truly be claimed" (§2.2). **Stated**
11. In weak-shear flows with production well below dissipation (far wakes) $C_\mu$ takes higher values; Rodi correlated it with the wake average of $P_k/\varepsilon$ (§2.2). **Stated**
12. Near walls production is always large, so the Table 2.1 values are "nearly always applicable" in engineering flows (§2.2). **Stated**
13. The wall-function method saves computer time and storage and admits roughness, pressure-gradient and mass-transfer information through $E$ and $A^+$; it requires $(k^{1/2}L/\nu)_P\gg1$ (§2.3-1). **Stated**
14. Momentum wall function (2.3-1): $\langle u\rangle_PC_\mu^{1/4}k_P^{1/2}/(\tau_w/\rho)=\kappa^{-1}\ln\big[Ey_P(C_\mu^{1/2}k_P)^{1/2}/\nu\big]$; it "reproduces identically" the log law when the shear stress is uniform between wall and $P$ and generation balances dissipation, since then $\tau/\rho=C_\mu^{1/2}k$ (§2.3-1(a)). **Derived** ("as is easily shown")
15. The thermal wall function (2.3-2) has a log term with $Pr_t/\kappa$ plus a sublayer-resistance term in $(A^+/\kappa)^{1/2}$, $Pr$ and $Pr_t$, from Jayatillaka's [33] analysis of data (§2.3-1(b)). **Stated**
16. In the Jones–Launder low-Reynolds model the term $-2\nu(\partial_jk^{1/2})^2$ is added to the $k$ equation "for computational rather than physical reasons", so that $\varepsilon=0$ can be imposed at the wall; $C_\mu=C_{\mu\infty}\exp[-2.5/(1+R_t/50)]$, $C_{\varepsilon2}=C_{\varepsilon2\infty}[1-0.3\exp(-R_t^2)]$ (Eqs. 2.3-4 to 2.3-7); a zero-gradient $\varepsilon$ condition admitted no compatible set of Reynolds-number functions (§2.3-2). **Stated**
17. The Jones–Launder values $C_{\varepsilon1}=1.55$, $C_{\varepsilon2}=2.0$ differ from Table 2.1, but in wall flows only $C_{\varepsilon2}-C_{\varepsilon1}$ matters to first order and it is "very nearly the same" (footnote p. 278). **Stated**
18. The scalar viscosity (2.4-1), $R_{ij}-\tfrac23k\delta_{ij}=-2\nu_t\langle S_{ij}\rangle$, is "perfectly adequate" in 2D flows without swirl; in swirling and 3D flows each stress component needs a different viscosity (Roberts [35]) (§2.4). **Stated**
19. Neglecting or approximating $DR_{ij}/Dt$ and $\mathcal D_{ij}$ in the transport equation (2.4-2), whose $\varepsilon_{ij}$ and $\phi_{ij}$ contain no stress gradients, gives implicit algebraic relations $R_{ij}=f(R_{pq},k,\varepsilon,\partial_m\langle u_l\rangle)$ (2.4-3); Launder [36] neglected the terms, Rodi [30] took them proportional to $(Dk/Dt)R_{ij}/k$; the two differ little in practice (§2.4). **Stated**
20. Plane jet in a moving stream: $k$-$\varepsilon$ agrees with Bradbury's data throughout, while mixing-length and one-equation models fail beyond the potential core; "the two-equation level is the simplest at which universality is secured for both jet and mixing layer" (§3.1, Fig. 3.1). **Shown**
21. Wall jets on cones (11° and 90°): $k$-$\varepsilon$ predicts the decay of the maximum velocity; the plane-calibrated mixing length underestimates it (§3.2, Fig. 3.2). **Shown**
22. The low-Reynolds model needs "nearly 100 cross-stream grid points for computational accuracy within 1% (about four times as many as when the wall-function method is used)" (§3.3). **Stated**
23. Pipe flow at $Re=6000$: the measured profile lies above the high-Reynolds log law and the Jones–Launder model reproduces the departure; it gives "excellent" friction factors down to the onset of intermittency, whereas Reynolds-independent near-wall formulae tuned for $Re>20{,}000$ overpredict $C_f$ (§3.3, Figs. 3.3a,b). **Shown**
24. Turbine-blade pressure-surface heat transfer at three free-stream turbulence levels: "extremely close agreement", with transition not specified — the low-Reynolds model "has its own built-in 'transition criterion'" (§3.4, Fig. 3.4). **Shown**
25. Film cooling behind a thick lip and step: the wall-function $\varepsilon$ of (2.3-3) had to be reduced by a factor 20 on the downstream faces of step and lip, attributed to impingement of large-scale fluid; agreement is then "excellent" (§3.5, Fig. 3.5b). **Shown**
26. Confined coaxial jets: separation, eddy-centre and reattachment positions against $C_t$ are reproduced (§3.6, Fig. 3.6b). **Shown**
27. Ventilated room: velocity contours in close agreement; design studies by computation now worthwhile (§3.7, Fig. 3.7). **Shown**
28. Twisted-tape tubes: friction factors "not so good", partly from using the equilibrium log law instead of (2.3-1), mainly from strong non-isotropy of the turbulent viscosity (§3.8, Fig. 3.8). **Shown**
29. Square duct: the algebraic stress model predicts the secondary flow and its effect on the axial-velocity contours; $k$-$\varepsilon$ with (2.4-1) gives no cross-sectional motion (§3.9, Fig. 3.9). **Shown** (the null result **Stated**)
30. $k$-$\varepsilon$ is "the simplest kind of model that permits prediction of both near-wall and free-shear-flow phenomena without adjustments to constants or functions"; needed are wall functions embodying the low-Reynolds model and tested approximations of the pressure-strain and dissipation tensors (§4). **Stated**

For $n=1$, (2.1-11) reads $\sigma_\varepsilon=\kappa^2/[(C_{\varepsilon2}-C_{\varepsilon1})C_\mu^{1/2}]$, which the Table 2.1 constants satisfy with $\kappa=0.433$; and $C_{\varepsilon2}-C_{\varepsilon1}$ is 0.45 for Jones–Launder against 0.48 for Table 2.1 *(compiler check, not in the sources)*.

With the paper's local-equilibrium relation $\tau/\rho=C_\mu^{1/2}k$ (§2.3-1(a)),
the log law (2.1-12) and production equal to dissipation, $\varepsilon=(\tau/\rho)\,\partial_y\langle u\rangle=C_\mu^{3/4}k^{3/2}/(\kappa y)$, whose
integral carries the prefactor $C_\mu^{3/4}k_P^{3/2}/\kappa$; the printed (2.3-3) has
$C_\mu k_P^{3/2}/\kappa$ in front of the logarithm, and the paper states the
proportionality $\varepsilon\propto k^{3/2}/y$ without its constant *(compiler check, not in the sources)*.

# Printed slips

- **Log-law constant:** the Nomenclature (p. 269) lists "$F$ — Constant in near-wall description of velocity profile ($\simeq9$)"; the text, Eqs. (2.1-12) and (2.3-1)–(2.3-3) and p. 277 use $E$ ("approximately equal to 9.0 for a smooth wall").
- **Eq. (2.3-3):** the logarithm's argument is printed $Ey_P(\surd C_\mu^{1/2}k_P)^{1/2}/\nu$, with a square-root sign absent from the argument $Ey_P(C_\mu^{1/2}k_P)^{1/2}/\nu$ of (2.3-1) and (2.3-2); with the extra root the argument has dimension (velocity)$^{-1/2}$ *(compiler check, not in the sources)*.
- **Length scale:** §2.1 defines $l=C_Dk^{3/2}/\varepsilon$ (2.1-2) and $\mu_t=C_\mu\rho k^{1/2}l$ (2.1-13), §2.2 calls $\mu_t=C_\mu\rho k^2/\varepsilon$ (2.2-3) "its equivalent in terms of $\epsilon$", and §2.3 uses $l\equiv k^{3/2}/\epsilon$; (2.1-2) with (2.1-13) gives $\mu_t=C_\mu c_l\rho k^2/\varepsilon$, with $c_l$ the printed $C_D$ *(compiler check, not in the sources)*; the value of $C_D$ is not printed.
- **Prandtl number for heat:** the Nomenclature (p. 270) lists $\sigma_h$ as "Molecular Prandtl number"; p. 277 defines $\sigma_h$ as the effective turbulent Prandtl number and $\sigma_{h,l}$ as the laminar one.
- **Equation numbering:** the Craya–Curtet equations of §3.6 are numbered (3.1-1), (3.1-2).
- **Symbol $U_c$:** the Nomenclature defines it as the "mean streamwise velocity on axis", §3.2 uses it for the slot exit velocity, §3.6 defines it by Eq. (3.1-2); §2.2 writes the axis velocity $U_{cl}$.
- **Eq. (2.3-4):** the subscript of the $\varepsilon$-diffusion Prandtl number is printed in a glyph resembling $\sigma_c$.
- **§3.3, p. 283:** "had the prediction been tried to equation (2.3-1)".
- **Spelling:** "trully" (p. 275), "preditions" (p. 275), "prefectly" (p. 279), "devlopment" (p. 285), "most not induce" (p. 286), "geatly" (p. 287); ref. [16] "Kolavandin" against "Kolovandin" in the text (p. 271); "Saffmann" in ref. [23] and the text (p. 272).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u_i$, $U_i$, overbar | $u_i'$, $\langle u_i\rangle$, $\langle\cdot\rangle$ | overbar is the Reynolds average here |
| $\overline{u_iu_j}$ | $R_{ij}$ | positive trace; $-\rho\overline{u_iu_j}$ the stress (2.4-1) |
| $\epsilon$ | $\varepsilon$ | full definition $\nu\overline{(\partial_ku_i)^2}$ (2.1-4) |
| $C_1$, $C_2$ | $C_{\varepsilon1}$, $C_{\varepsilon2}$ | 1.44, 1.92 |
| $\sigma_k$, $\sigma_\epsilon$, $C_\mu$ | $\sigma_k$, $\sigma_\varepsilon$, $C_\mu$ | 1.0, 1.3, 0.09 |
| $C_D$ | $c_l$ (page-local) | **collision** with the drag coefficient $C_D$ |
| $\sigma_t$ | $\sigma_t$ (page-local) | diffusion Prandtl number of $k^m/l^n$ |
| $\sigma_h$, $\sigma_{h,l}$ | $Pr_t$, $Pr$ | |
| $E$ ($F$ in the Nomenclature) | $E$ | log-law constant as on the law-of-the-wall page; $\approx9.0$ smooth wall |
| $l$ | $L$ (page-local) | length scale of the energy-containing eddies |
| $A$ | $A^+$ | Van Driest constant, 26.0 |
| $x_1$, $x_2$ (also $y$) | $x$, $y$ | streamwise, wall-normal |
| $(\tau/\rho)_w$ | $\tau_w/\rho=u_\tau^2$ | $u_\tau$ not named in the source |
| $U^+$, $y^+$ | $u^+$, $y^+$ | |
| $D_{ij}$, $\epsilon_{ij}$, $R_{ij}$ | $\mathcal D_{ij}$, $\varepsilon_{ij}$ (page-local), $\phi_{ij}$ | **collision**: the source's $R_{ij}$ is the pressure redistribution, not the Reynolds stress |
| $W=\epsilon^2/(C_Dk)^2$ | $W$ (page-local) | time$^{-2}$, not Wilcox's $\omega$ |
| $R_t=k^2/\nu\epsilon$ | $R_t$ (page-local) | |
| $C_t$ | $C_t$ (page-local) | Craya–Curtet number |

# Reference list

51 printed references, numbered [1]–[51], cited by number (ref. [51] only
in the legend of Fig. 3.3a; refs. [41], [44], [47], [50] are private
communications); no DOIs. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Ref. [8] (Nee &
Kovasznay) prints two venues and is kept as one entry; ref. [28] (Gibson &
Spalding) prints no year, only the ASME paper number 72/HT/15; ref. [14]
(Rotta) prints two parts and is one entry. Bradshaw, Ferriss & Atwell (1967)
and Harlow & Nakayama (1968) share author–year keys with different works and are keyed `bradshaw-1967-d` and `harlow-1968-b`; ref. [22] (Spalding 1971, Chem. Eng. Sci. 26:95)
and ref. [23] (printed "Saffmann", 1970) are the same works as the existing entries `spalding-1971-b` and `saffman-1970`. No item is unparseable.

# Pages created or updated

Chunk 17 (2026-10-29). This source is cited on:

- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Explicit algebraic Reynolds-stress models](/methods/explicit-algebraic-reynolds-stress-model.md)
- [k-ε models](/methods/k-epsilon-model.md)
- [Wall functions for RANS](/methods/rans-wall-function.md)
- [Differential Reynolds-stress models](/methods/reynolds-stress-model.md)
