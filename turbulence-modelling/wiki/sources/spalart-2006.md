---
type: Source
title: "Spalart et al. (2006) — A new version of detached-eddy simulation, resistant to ambiguous grid densities"
description: "Introduces delayed detached-eddy simulation (DDES): a boundary-layer sensor and shielding function that keep attached boundary layers in RANS mode on ambiguous grids, curing modelled-stress depletion and grid-induced separation; tests in two codes, a discussion of DES as wall-modelled LES and log-layer mismatch, and a low-Reynolds-number correction."
resource: "doi:10.1007/s00162-006-0015-0"
source_kind: paper
authors: [Spalart P.R., Deck S., Shur M.L., Squires K.D., Strelets M.Kh., Travin A.]
year: 2006
venue: "Theor. Comput. Fluid Dyn. 20:181-195"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2006_Crossref_Theoretical_and_Computational_Fluid_Dynamics_Spalart_A_New_Version_of_Detached-eddy_Simulation_Resistant_to_Ambig.pdf"
tags: [des, hybrid-rans-les, spalart-allmaras, wmles, log-layer-mismatch]
timestamp: 2026-10-29T16:19:00Z
---

# Summary

Spalart et al. (2006) introduce **delayed detached-eddy simulation (DDES)**,
a revision of the original 1997 [detached-eddy simulation](/methods/detached-eddy-simulation.md)
(DES97), a [hybrid RANS/LES](/definitions/hybrid-rans-les.md) method. In
DES97 based on the [Spalart–Allmaras model](/methods/spalart-allmaras-model.md)
the length scale is $d_{\mathrm{DES}}=\min(d,C_{\mathrm{DES}}\Delta_{\max})$.
On "ambiguous" grids, whose wall-parallel spacing falls below the
boundary-layer thickness but is too coarse to resolve boundary-layer eddies,
the limiter switches the outer boundary layer to LES mode and lowers the
eddy viscosity without resolved stresses to replace it: **modelled-stress
depletion**, which when severe causes "grid-induced separation". Following
Menter and Kuntz's shielding with the SST blending functions, DDES defines a
model-independent sensor $r_d$, a shielding function $f_d$ and the length
$d_{\mathrm{DES}}=d-f_d\max(0,d-C_{\mathrm{DES}}\Delta_{\max})$, which depends
on the eddy-viscosity field, so that RANS mode is "self-perpetuating" inside
boundary layers while LES mode still takes over, more abruptly, after massive
separation.

Tests in two codes: a flat-plate boundary layer with $\Delta_{\max}\approx0.1\delta$
(DES97 loses about 75% of the peak eddy viscosity and 19% of the skin
friction, DDES keeps the RANS solution), the circular cylinder at $Re=10^5$
(no change), the A-airfoil (the grid-induced separation disappears), the
[backward-facing step](/benchmarks/backward-facing-step.md) (the opposite-wall
skin-friction drop of up to 60% disappears, LES content after separation
unchanged) and a multi-element airfoil. §4 discusses DES on LES grids as
[wall-modelled LES](/methods/wall-modelled-les.md), whose
[log-layer mismatch](/definitions/log-layer-mismatch.md) (skin friction
about 15% low) DDES does not cure, the possibility of two solutions with
DDES, and a low-Reynolds-number correction $\Psi$ that keeps the SA
low-Reynolds terms from acting in LES mode.

# Version read

Version of record (Springer, Theoretical and Computational Fluid Dynamics;
received 27 May 2005, accepted 23 February 2006, published online 30 May
2006), 15 pages (pp. 181–195), all read; the displayed equations of
pp. 184–185 and 192–193 were read visually. Page 1 matches the Crossref
metadata and prints the DOI. Numbering cited on this page is that of the
paper.

# Key claims

Page-local symbols: $d_{\mathrm{DES}}$ the DES length (the source's $\tilde d$,
also $l_{\mathrm{DES}}$), $l_{\mathrm{RANS}}$ the RANS length; $C_{\mathrm{DES}}$
the DES constant; $\Delta_{\max}=\max(\Delta x,\Delta y,\Delta z)$ and
$\Delta_\parallel$ the wall-parallel spacing; $\Psi$ the low-Reynolds-number
correction; $f_w^*$ the high-eddy-viscosity limit of the equilibrium $f_w$;
$N_{\mathrm{cubes}}$ the number of $\delta$-sized cubes filling a boundary
layer; $C_{\mathrm{eq}}$ and $S$ the constant and the strain magnitude
(not defined in the paper) of the equilibrium target
$\nu_t=(C_{\mathrm{eq}}\Delta)^2S$; $a_{\mathrm{Wk}}$, $a^*_{\mathrm{Wk}}$
the Wilcox $k$-$\omega$ coefficients (the source's $\alpha$, $\alpha^*$); $H$
the step height. $r_d$ and $f_d$ are registry §11.

1. DES97 behaves incorrectly when $\Delta_\parallel$ falls below $\delta$: the length follows the LES branch and lowers the eddy viscosity below the RANS level before resolved "LES content" replaces the modelled stresses, which reduces the skin friction and can cause premature separation (Abstract; §1, Fig. 1). **Stated**, **Shown** in §3
2. Three grid types in a boundary layer: Type I (natural DES, spacings above $\delta$, $d_{\mathrm{DES}}=d$ throughout), Type II (ambiguous, the limiter acts "roughly in the upper two-thirds of the boundary layer" without supporting resolved fluctuations), Type III (LES grid; $\Delta\approx\delta/20$ "a plausible starting value", $\delta/10$ "acceptable"); Type III with DES formulas is a type of WMLES (§1, Fig. 1). **Stated**
3. The phenomenon is named **modeled-stress depletion (MSD)**; it "was predicted from the origin of the method", was met by Caruelle and Deck, and severe MSD leads to "grid-induced separation" (Menter and Kuntz) (§1). **Stated**
4. DES is "not simply 'a coarser-grid version of LES'" and "differs from LES only in boundary layers"; the opposite idea "has led to several inappropriate comparisons between LES and DES" (§1). **Stated**
5. MSD faces any hybrid method that brings the grid spacing into the model (e.g. LNS); SAS and TRRANS do not, but "neither approach has been able to sustain LES content in a channel", and TRRANS fails to sustain unsteadiness over a backward-facing step (§1). **Stated**
6. Earlier remedies are insufficient: zonal DES is lengthy and error-prone in complex geometries, aspect-ratio biasing is not robust on unstructured grids, and Forsythe et al.'s $d_{\mathrm{DES}}=\min\big(C_{\mathrm{DES}}\max(n^2C_{\mathrm{DES}}\Delta^2/d,\Delta),d\big)$, $n=3$, is "not much more robust than the use of cell aspect ratio" (§1). **Stated**
7. $r_d\equiv(\nu_t+\nu)/\big(\sqrt{\partial_ju_i\,\partial_ju_i}\,\kappa^2d^2\big)$ (Eq. 2.1, printed $\sqrt{U_{i,j}U_{i,j}}$) equals 1 in a log layer and falls gradually to 0 towards the boundary-layer edge; $\nu$ keeps it away from 0 very near the wall; in SA, $\tilde\nu$ "can be used instead of $\nu_t+\nu$" (§2.1). **Stated** (definition)
8. $f_d\equiv1-\tanh([8r_d]^3)$ (Eq. 2.2) is 1 in the LES region ($r_d\ll1$) and 0 elsewhere, insensitive to $r_d>1$ near the wall, "similar to $1-F_2$, and rather steep near $r_d=0.1$"; the constants 8 and 3 come from "intuitive shape requirements" and flat-plate tests (§2.1, §3.2). **Stated** / **Shown**
9. A constant larger than 8 "would delay LES in even larger regions, which would be safer in the sense of avoiding MSD, but is undesirable overall"; models very different from SA might need "a modest adjustment of $f_d$" (§2.1). **Stated**
10. $d_{\mathrm{DES}}\equiv d-f_d\max(0,d-C_{\mathrm{DES}}\Delta_{\max})$ (Eq. 2.3): $f_d=0$ gives RANS, $f_d=1$ gives DES97; for other RANS hosts DDES multiplies by $f_d$ "the term that constitutes the difference between RANS and DES" (§2.1). **Stated**
11. The length now depends on the eddy-viscosity field and on time; RANS mode is "self-perpetuating", and after massive separation LES takes over "more abruptly following separation than in DES97" — a narrower grey area that speeds the growth of LES content but does not create it (§2.2). **Stated**, partly **Shown** (§3.5)
12. DDES, like $F_2$, does not address MSD in free shear layers, justified by fairly isotropic DES grids outside boundary layers and by shear-layer instabilities at wavelengths much larger than their thickness (§2.2, §3.6). **Stated**
13. Flat plate with $\Delta\approx0.1\delta$: with DES97 "the peak eddy viscosity is reduced by about 75%, and the skin friction by 19% from the RANS prediction"; DDES "preserves the eddy viscosity almost fully"; $f_d$ can rise from 0 in the upper half of the layer because the SA destruction is negligible there (§3.2, Fig. 2). **Shown**
14. Circular cylinder (case LS2, $Re=10^5$, laminar separation): DDES has an insignificant effect on the pressure distribution (§3.3, Fig. 3). **Shown**
15. A-airfoil ($Re=2.1\times10^6$, $\alpha=13.3°$): $\delta$ reaches about 7% of the chord, "or 14 times $\Delta$"; DES97 separates at $x/c=0.77$ on the grid alone, which "has been corrected by the $f_d$ term" (§3.4, Figs. 4–5). **Shown**
16. Backward-facing step: DDES keeps RANS in both attached boundary layers and LES after the corner; "the grid-induced drop by up to 60% on the opposite side is eliminated", and the LES content "is essentially as fine with either approach" (§3.5, Figs. 6–8). **Shown**
17. In a temporal channel started with a RANS field near one wall and an LES field near the other on a Type III grid, "LES mode 'invaded' RANS mode" (§3.5). **Shown** (no figure)
18. Multi-element airfoil ($Re_c=1.8\times10^6$; 250,000 points in $x$–$y$, 31 spanwise, $\Delta z/c=0.002$): slat cove, flap cove and flap wake keep LES content; in the main-element boundary layer at $x/c=0.95$ DES97 sharply reduces the eddy viscosity while DDES preserves it, with $d_{\mathrm{DES}}=d$ over "more than half of the boundary layer" (§3.6, Figs. 9–11). **Shown**
19. Prolate-spheroid tests are not shown because the grids could not resolve the shear-layer eddies (§3.6). **Stated**
20. DES on Type III grids (Nikitin et al.) is a wall model for LES at unlimited $\Delta_\parallel^+$ (up to 8,000), but the modelled and resolved log layers have different intercepts — log-layer mismatch — and the skin friction is under-estimated "by about 15%, which is not acceptable"; the trend is visible for $x/H\ge15$ in Fig. 7, "confirming that log-layer mismatch is insensitive to the DDES modification" (§4.1). **Stated** / **Shown**
21. Wall-resolved LES requires limits of the order of $\Delta z^+\le20$ (§4.1). **Stated**
22. Methods using RANS only as a wall model in LES "should not be called 'DES'"; the essential DES ability is treating an entire boundary layer in RANS mode (§4.1). **Stated**
23. DDES on WMLES grids admits two solutions (continued RANS mode, or WMLES from an initial condition with LES content), with no intermediate state observed; DES97 of a channel on a Type II or III grid with no initial LES content would reach "a pathological state with zero resolved stresses, and weak modeled stresses", which DDES avoids (§4.1). **Stated**
24. $N_{\mathrm{cubes}}=\int\delta^{-2}\,dS$ over the body surface: about $10^7$ for a whole wing boundary layer, "somewhat over $10^4$" for the thick region near separation (§4.1). **Stated**
25. Low-Reynolds-number correction: $l_{\mathrm{DES}}=\min(l_{\mathrm{RANS}},\Psi C_{\mathrm{DES}}\Delta)$ with $\Psi\ge1$ a function of $\nu_t/\nu$, derived so that at equilibrium the subgrid model reduces to $\nu_t=(C_{\mathrm{eq}}\Delta)^2S$; $\Psi^2=\min\Big[10^2,\ \dfrac{1-\frac{c_{b1}}{c_{w1}\kappa^2f_w^*}[f_{t2}+(1-f_{t2})f_{v2}]}{f_{v1}\max(10^{-10},1-f_{t2})}\Big]$ with $f_w^*=0.424$, since the equilibrium $f_w/f_w^*$ is 1 within 2% for $\nu_t>\nu/10$; the correction is inactive ($\Psi=1$) above a subgrid viscosity of about $10\nu$ (§4.2, Eqs. 4.3.1–4.3.4, Fig. 12). **Derived**
26. The correction was applied successfully to homogeneous turbulence, the cylinder and the NACA 0012 at 60°; in a $64^3$ LES of decaying isotropic turbulence its effect on the eddy viscosity is large (§4.2, Fig. 12c). **Shown** (isotropic turbulence) / **Stated** (others)
27. In SA-based DDES, $\chi$ is replaced with $\max(\chi,20f_d)$ before entering $f_{v1}$ and $f_{t2}$ (§4.2). **Stated**
28. For Wilcox's $k$-$\omega$ model, $\Psi=(\beta^*/C_\mu)(2a_{\mathrm{Wk}}/a^*_{\mathrm{Wk}})^{3/4}$ with the model's constants and low-Reynolds functions, and the calibrated $C_{\mathrm{DES}}$ of its subgrid version (decaying isotropic turbulence) is 0.72 (§4.2, footnote 1). **Derived** / **Stated**
29. With DDES, MSD would occur "only in extreme grids"; "loss of LES behavior after massive separation has not been observed"; $f_d$ "appears simple and permanent enough to be recommended" (§5). **Stated**

$C_{\mathrm{DES}}$ for SA is called "of order 1" and its value is not
printed; $\kappa$ is not printed. With $f_d=1$, Eq. 2.3 gives
$d-\max(0,d-C_{\mathrm{DES}}\Delta_{\max})=\min(d,C_{\mathrm{DES}}\Delta_{\max})$,
DES97 *(compiler check, not in the sources)*. The
[DES page](/methods/detached-eddy-simulation.md) quotes $r_d$ from a later
source with $\nu+\tilde\nu$ and $\sqrt{\partial_ju_i\,\partial_iu_j}$; this paper
prints $\nu_t+\nu$ and $\sqrt{U_{i,j}U_{i,j}}$. In a pure shear
$u(y)$ the contracted form $\partial_ju_i\,\partial_iu_j$ vanishes while
$\partial_ju_i\,\partial_ju_i=(\partial_yu)^2$ *(compiler check, not in the sources)*.

# Printed slips

- **Equation numbers:** the equations of §4.2 are numbered (4.3.1)–(4.3.4); there is no §4.3.
- **Step height:** the Fig. 6 caption uses $h$ ("$\Delta z=0.03h$, period $\lambda_z=2h$"); Fig. 7 and the text of §4.1 use $H$ ("$x/H\ge15$").
- **Boundary-layer thickness:** §1 says "$\delta$ can reach 10% of the airfoil chord [7] (see Sect. 3.4)"; §3.4 says "$\delta$ reaches around 7% of the chord, or 14 times $\Delta$".
- **Fig. 12a:** the horizontal axis is labelled "$\nu/\nu$"; Fig. 12b reads "$\nu_t/\nu$" and the text makes $\Psi$ "a function of $\nu_t/\nu$".
- **Typographical:** "DDES over A airfoil" (Fig. 4) against "over a airfoil" (Fig. 5); "Continous" (Fig. 3); "homogeous-turbulence" (p. 193); "feas1ibility" (ref. [1]); "turbulance" (ref. [29]).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\tilde d$, $l_{DES}$ | $d_{\mathrm{DES}}$ (page-local) | **collision** with the Favre/SA tilde |
| $l_{RANS}$, $C_{DES}$ | $l_{\mathrm{RANS}}$, $C_{\mathrm{DES}}$ | as on the DES page |
| $\Delta=\max(\Delta x,\Delta y,\Delta z)$ | $\Delta_{\max}$ (page-local) | |
| $U_{i,j}$ | $\partial_ju_i$ | resolved or mean velocity gradient; $\sqrt{U_{i,j}U_{i,j}}$ the full gradient norm |
| $r_d$, $f_d$ | $r_d$, $f_d$ (§11) | |
| $\nu_t$, $\tilde\nu$, $\chi$ | same | |
| $r$, $f_w$, $g$, $f_{v1}$, $f_{v2}$, $f_{t2}$, $c_{b1}$, $c_{w1}$, $c_{w3}$ | same | SA functions and constants, not re-printed |
| $\Psi$, $f_w^*$ | $\Psi$, $f_w^*$ (page-local) | $1\le\Psi\le10$ |
| $C$ | $C_{\mathrm{eq}}$ (page-local); log-law intercept $B$ | **two meanings** in the source |
| $S$ in $(C\Delta)^2S$ | $S$ (page-local) | strain magnitude, definition not printed |
| $U^+=\log(y^+)/\kappa+C$ | $u^+=\kappa^{-1}\ln y^++B$ | |
| $F_1$, $F_2$ | $F_1$, $F_2$ | SST blending functions |
| $\alpha,\alpha^*,\beta^*,C_\mu$ (Wilcox) | $a_{\mathrm{Wk}}$, $a^*_{\mathrm{Wk}}$ (page-local), $\beta^*$, $C_\mu$ | $k$-$\omega$ constants and functions, named as on the DES page |
| $Re_t=k/(\omega\nu)$ | (turbulence Reynolds number) | |
| $h$, $H$ | $H$ (page-local) | step height, as on the backward-facing-step page (registry $h$ is the cell size) |

# Reference list

31 printed references, numbered [1]–[31]; no DOIs. The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this slug.
Ref. [29] (Spalart, Strelets & Travin, Int. J. Heat Fluid Flow, in press)
would take this source's own key and is keyed `spalart-2006-b`; Travin et al.
(2000, cylinder), Menter & Kuntz (2004), the SAS paper of Menter et al. (2003), Shur
et al. (2003), Forsythe et al. (2004) and Travin et al. (printed 2002) are keyed `travin-2000-b`, `menter-2004-b`, `menter-2003-c`, `shur-2003-b`, `forsythe-2004-b` and `travin-2000` respectively (the last is the existing entry of the same work); ref. [5] (NASA CR-2001-211032) prints Spalart alone
and no separate year. Refs. [25] and [29] are "in press" and kept as such;
the two Deck works of 2002 take suffixes in printed order. No item is
unparseable.

# Pages created or updated

Chunk 17 (2026-10-29). This source is cited on:

- [Backward-facing step](/benchmarks/backward-facing-step.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Log-layer mismatch](/definitions/log-layer-mismatch.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
