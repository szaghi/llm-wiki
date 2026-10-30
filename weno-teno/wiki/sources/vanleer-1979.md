---
type: Source
title: "Van Leer (1979) — Towards the ultimate conservative difference scheme. V. A second-order sequel to Godunov's method"
description: "Fifth paper of van Leer's series: a second-order Lagrangean extension of Godunov's method with independently stored, limited linear slopes, interface time derivatives from characteristic relations after an exact Riemann solution, and a least-squares remap to the Eulerian grid; coded by Woodward as MUSCL and run on Sod's tube and a Mach 3 step."
resource: "doi:10.1016/0021-9991(79)90145-1"
source_kind: paper
authors: [van Leer B.]
year: 1979
venue: "J. Comput. Phys. 32:101-136"
local_file: "/home/stefano/papers/mosaic/weno-teno/1979_Crossref_Journal_of_Computational_Physics_van_Towards_the_ultimate_conservative_difference_scheme_V_A_seco.pdf"
tags: [finite-volume, reconstruction, limiting, muscl, riemann-solver, euler-equations]
timestamp: 2026-10-30T07:55:00Z
---

# Summary

Van Leer (1979), the last paper of a five-part series, builds a second-order,
conservative, dissipative method for ideal compressible flow in plane,
cylindrical or spherical symmetry and, by time splitting, in several dimensions.
Its core is a one-dimensional **Lagrangean** step in the mass coordinate, called
a second-order sequel to [Godunov's](/methods/godunov-scheme.md) first-order
Lagrangean scheme. In each slab, specific volume, velocity and total energy are
linear: a slab average plus an **independently stored slope**, which "can not be
derived from" the averages. With all slopes zero the scheme is Godunov's. At each
interface the Riemann problem is solved with exact wave relations and an
iterative pressure solution. The first time derivatives of $v$, $p$ and the
specific volume just after resolution follow from the characteristic equations
on both sides of the contact (Eqs. (64)–(66)). A half step with them gives
time-centred interface values and a second-order flux, the interface-derivative
idea treated on the [generalized Riemann problem](/methods/generalized-riemann-problem.md)
page (the paper does not use that name).

The Lagrangean result is then **remapped** onto the fixed Eulerian grid with
first-moment (least-squares) accuracy ([conservative remapping](/methods/conservative-remapping.md)).
Monotonicity is enforced by slope limiters: the limiter (101) before the
Lagrangean step, a mass-fraction limiter (102) in the remap, an optional
narrow-base limiter (104), and the harmonic-mean slope (B2) of paper IV. The
paper speaks of "monotonicity algorithms" that preserve monotonicity and
positivity ([bound preservation](/properties/bound-preservation.md)). It never
uses the word "TVD" ([TVD and slope limiters](/definitions/total-variation-diminishing.md)).

P. R. Woodward coded the method as **MUSCL**, "Monotonic Upstream-centered
Scheme for Conservation Laws" ([MUSCL](/methods/muscl-hancock.md)): Lagrange
step plus remap, stored slopes, interface time derivatives. The paper prints no
$\kappa$ family and no Hancock predictor. Tests: [Sod's tube](/benchmarks/sod-and-lax-shock-tubes.md)
on 100 cells, and Mach 3 flow in a wind tunnel with a step
([forward-facing step](/benchmarks/forward-facing-step.md)) on four grids.
MUSCL at entrance height $H/\Delta y=10$ is stated to mimic Godunov's method at
$30$. Appendix B compares slope-updating options, among them a quadratic,
interface-continuous "scheme V" ([gradient-based reconstruction](/methods/gradient-based-reconstruction.md)),
with dissipative and dispersive error comparisons cited from paper IV
([numerical dissipation](/definitions/numerical-dissipation.md)).
Multidimensional runs use Strang splitting into one-dimensional sweeps
([operator splitting](/methods/operator-splitting.md)).

# Version read

Version of record (Academic Press typeset), received 18 October 1977, revised
17 October 1978, as a 2003 Acrobat Capture scan: 36 pages (pp. 101–136), all
read visually because the OCR layer fails on every equation; Eqs. (B3)–(B4)
checked on a 220-dpi rendering. Nothing is illegible. Page 1 matches the
Crossref record (title, single author "Bram van Leer", Leiden; venue, pages).
Page 1 prints no DOI; the DOI is that of the Crossref record. The bundle's
bibliography also holds the 1997 J. Comput. Phys. 135 reprint of this paper
(`vanleer-1997-b`), kept distinct.

# Key claims

Registry notation: cell $I_i$ with average $\bar u_i$ (source slab
$(\xi_i,\xi_{i+1})$, index $i+1/2$); velocity $v$ (source $u$). Page-local:
mass coordinate $\zeta$ (source $\xi$), specific volume $V=1/\rho$, stored
undivided slope $\mathsf s_i$ of cell $I_i$ (source $\bar\Delta_{i+1/2}Q$),
Lagrangean sound speed $C_{\mathrm L}=\rho c$ (source $C$), Lagrangean wave speed
$W_{\mathrm L}$ (source $W$).

1. The Lagrangean scheme reaches second order by taking linear instead of uniform distributions in each slab; with all slopes zero it is Godunov's scheme, which "accounts for the first-order accuracy of Godunov's scheme" (Abstract, §1, §2.2 p. 107). **Stated**
2. The slopes are independent of the slab averages, "can not be derived from the latter and must be stored separately", which distinguishes the scheme from common finite-difference schemes (§2.2, p. 107). **Stated**
3. The slab-average updates (49)–(51) are exact integrals of the conservation laws over a slab and a time step and "hold regardless of the presence of discontinuities in the slab"; second order needs interface time averages of $v$, $p$ and position within $O(\Delta t^2)$ (§2.2, p. 108). **Derived**
4. In smooth flow on a uniform grid the interface discontinuities are $O(\Delta\zeta^2)$, against $O(\Delta\zeta)$ for Godunov; hence the linear-wave (acoustic) pressure estimate $p^{*(1)}$ of Eq. (60), with error $O(\Delta\zeta^6)$, suffices "anywhere in the smooth part of the flow" (§2.3, p. 110). **Derived**
5. In MUSCL the pressure iteration is invoked only if $p^{*(1)}$ differs by more than 1% from the adjacent interface pressures, and continued until successive iterates differ by less than 1.5%; in the Sod run the extra iterations took 2–3% of the Lagrangean step's computing time (§2.3, p. 110). **Shown**
6. Eqs. (57), (58), (64), (65) separate signals from left and right; the slab averages of the Riemann invariants are then updated by a second-order upstream-centred formula "resembling Fromm's [11] scheme" (§2.3, p. 111). **Stated**
7. The Lagrangean time step obeys $\Delta t\le\Delta x/\bar c$ (67), or $\gamma(\gamma-1)\Delta t^2\le\Delta x^2/\bar e$ (68γ), which avoids a square root (§2.4). **Stated**
8. The composite (Lagrange plus remap) scheme needs $\Delta t\le\min(\Delta x/\lvert\bar v\rvert,\Delta x/\bar c)+O(\Delta\zeta^2,\Delta\zeta\Delta t)$ (99), less stringent than the Eulerian $\Delta t\le\Delta x/(\lvert\bar v\rvert+\bar c)$ (100), plus the anti-tangling condition $-\mathsf s_i[v]\,\Delta t\le\Delta x+O(\Delta\zeta\Delta t^2)$ (100.5), which the monotonicity algorithms can enforce by limiting the velocity slope (§3.2, p. 117). **Stated**
9. The remap costs about 0.55 of the Lagrangean step in the 1D shock tube and up to 0.75 in 2D (§3.2, p. 117). **Shown**
10. Limiter (101) prevents the onset of oscillations in a monotone sequence of slab averages and guarantees positivity of the distributions; it cannot fully guarantee monotonicity for systems, "especially for the largest allowed time steps" (§3.3, pp. 117–118). **Stated**
11. The factors 2 in (101) may be reduced, "however, not beyond $1+O(\Delta Q)$, lest the scheme lose its second-order accuracy" ($\Delta Q$ the variation of the limited quantity); they may be made a decreasing function of the local Lagrangean Courant number; with factors 0 the scheme reduces to Godunov's (§3.3, p. 118). **Stated**
12. With the remap limiter (102), positivity is guaranteed "only for the zone averages" (§3.3, p. 119). **Stated**
13. Limiters (101) and (102) "will clip real peaks to the same degree as a first-order method would do", in particular for $V$, $p$, $E$ at reflecting boundaries; the narrow-base limiter (104) limits as (101) near a plateau and less near a peak (§3.3, pp. 119–120, Fig. 5). **Stated**
14. The $n$-dimensional method carries $(n+1)(n+2)$ independent quantities: $n+2$ slab averages and $n(n+2)$ first moments (§3.4, p. 121). **Stated**
15. Sod's problem, 100 cells, Courant number 0.9: the method "is superior to all methods tested by Sod, including Phoenical SHASTA", which was run at too high a Courant number to remain monotone (§4, Fig. 6, p. 123). **Shown**
16. Cost: 0.47 s per time step on the IBM 370/158 (MVS) for the 100-cell tube, 0.17 s on the CDC 6600 (SCOPE 3.4), plotting excluded (§4, p. 123). **Shown**
17. Mach 3 step: on the 5-zone grid (Fig. 9) a Mach stem appears to be visible but is an artifact of limiters (101)/(102) forcing pressure contours perpendicular to a reflecting wall (§4, p. 123). **Shown**
18. Godunov's method (MUSCL with all slopes zero) at $H/\Delta y=30$ is mimicked by MUSCL at $H/\Delta y=10$; Godunov's method "even when programmed efficiently, will not run more than twice as fast as MUSCL", "a dramatic increase in efficiency" (§4, p. 123; Figs. 8, 11). **Shown**
19. On the 1008-cell grid of Fig. 7 a MUSCL step takes 8.78 s on the IBM 370/158, 2.33 times the FCT code ALFVEN (SHASTA-based); ALFVEN must run at Courant numbers $\le1/2$, so MUSCL is 15–20% slower in absolute time advancement (§4, p. 129; also §1, p. 102). **Shown**
20. Godunov's iteration for $p^*$ gains a factor $O([\![v]\!],[\![p]\!])$ per cycle; the tangent iteration (A1) suggested by P. J. Bedijn gains $O([\![v]\!]^2,[\![p]\!]^2)$ (§2.3, App. A). **Stated**
21. A linear analysis in paper IV shows moment fitting (scheme III) "vastly superior" to finite-difference slopes, its evolutionary convective error smaller by two orders of $\Delta\zeta$; interface differencing (scheme II) and slab-average differencing (scheme I) have equal convection errors as $\Delta t/\Delta\zeta\to0$, the maximum dissipative error per step of scheme II being a factor 3 below scheme I's and a factor 3 above moment fitting's (App. B, p. 134). **Stated** (cited from paper IV)
22. With slab-average differencing the scheme for the Riemann invariants "boils down to" Fromm's upstream-centred second-order scheme, as Godunov's boils down to the Courant–Isaacson–Rees scheme (App. B, p. 134). **Stated**
23. Least-squares updating of the slopes in the Lagrangean step via (B4) is "perfectly valid" but does not reduce to the exact least-squares formula for constant coefficients, is not upstream centred and gives larger phase errors than interface differencing; the results of §4 used (B4) (App. B, p. 135). **Derived**
24. Scheme V (quadratic, interface-continuous initial distributions (B5)) has, per paper IV, the same dispersive and dissipative evolutionary errors as scheme III; it "has not yet been implemented for the equations of ICF" because monotonicity and time splitting destroy interface continuity (App. B, pp. 135–136). **Stated**
25. A separate remap step "originated with the group of W. F. Noh at Livermore"; the separate remap for MUSCL was Woodward's idea (§3.2, Acknowledgments). **Stated**

The limiters as printed, in registry indexing (difference of averages
$\bar u_i-\bar u_{i-1}$ for the source's $\Delta_i\bar Q$):

- (101): $\mathsf s_i^{\mathrm{mono}}=\min\big(2\lvert\bar u_i-\bar u_{i-1}\rvert,\lvert\mathsf s_i\rvert,2\lvert\bar u_{i+1}-\bar u_i\rvert\big)\,\mathrm{sgn}\,\mathsf s_i$ if $\bar u_i-\bar u_{i-1}$, $\bar u_{i+1}-\bar u_i$ and $\mathsf s_i$ have one sign, $0$ otherwise. It bounds a stored slope, not a central difference.
- (102): the same with the factors $2/\varphi$ and $2/(1-\varphi)$, $\varphi$ the mass fraction of the Lagrangean slab that crossed the Eulerian boundary (103).
- (B2): $\mathsf s_i=2ab/(a+b)$ if $a=\bar u_i-\bar u_{i-1}$ and $b=\bar u_{i+1}-\bar u_i$ have one sign, $0$ otherwise, credited to paper IV Eq. (67) and given no name. *(Compiler check, not in the sources: for $r=a/b>0$, $2ab/(a+b)=b\cdot2r/(1+r)=b\,\psi(r)$ with $\psi(r)=(r+\lvert r\rvert)/(1+\lvert r\rvert)$.)*

Test setups as printed. Sod: $[0,1]$, 100 cells, $\gamma=1.4$, $(\rho,p)=(1,1)$
left and $(0.125,0.1)$ right, $v=0$, Courant number 0.9, output after 34 steps at
$t=0.14154$. Mach 3 step (runs by P. Woodward): inflow $v=3$, $c=1$, step height
$H/5$, narrow part $2.4H$ long, square meshes, $\Delta t$ at 0.9 of condition (99),
$t\approx4H/c$; grids $60\times20$ (the "1008-cell grid", Fig. 7), $30\times10$,
$15\times5$, $45\times15$ near steady state at $t=16H/c$, and Godunov on $80\times30$.
*(Compiler check, not in the sources: $60\times20-48\times4=1200-192=1008$, so the
step starts $12$ cells $=0.6H$ from the inlet and the tunnel is $60$ cells $=3H$ long.)*

# Printed slips

1. Fig. 3 caption (p. 118): "The monotonicity condition (100) on the slopes at the beginning of the Lagrangean step". The slope condition is Eq. (101); Eq. (100) is the Eulerian Courant condition. The captions of Figs. 4 and 5 cite (102) and (104).
2. p. 116: "the quadratic equation (93) … in the case of Fig. 10". Eq. (93) is derived for "the (most common) case of Fig. 1c" (p. 115); Fig. 10 is the steady step-flow plot.
3. App. B (p. 134): "the moment-fitting technique of Section 3.1". The least-squares remap is Section 3.2; Section 3.1 is on boundary conditions.
4. App. B (p. 134): "the upstream-centered second-order scheme of Fromm [12]"; ref. [12] is van Leer (Lecture Notes in Physics 18) and Fromm is [11], as cited on pp. 111 and 129. Same paragraph: "Courant, Isaacson and Rees [15]"; ref. [15] is Courant & Friedrichs and Courant, Isaacson & Rees is [14], as cited on p. 130.
5. Eq. (B4) (p. 135): an update formula for the slope printed with a trailing "$=0$".
6. The equation numbering has gaps ((11), (16), (27)–(30), (36)–(37) absent) and inserted numbers "(51.5)" and "(100.5)"; (17γ) appears after (19).
7. p. 102: "15 20% slower", with the dash lost; p. 129 prints "15-20%".

# Notation map

| Van Leer (1979) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| slab $(\xi_i,\xi_{i+1})$, index $i+1/2$; interface $\xi_i$ | cell $I_i$; interface $x_{i-1/2}$ | **collision** of index conventions: the source puts interfaces at integer and cells at half-integer indices |
| $\xi$ | $\zeta$ (local) | Lagrangean mass coordinate, $d\xi=V^{-1}x^\alpha dx$; **collision** with the DG nodes $\xi_j$ |
| $x$, $X=x^{\alpha+1}/(\alpha+1)$ | $x$; $X$ (local) | Euler and volume coordinate |
| $\alpha=0,1,2$ | $\alpha_{\mathrm g}$ (local) | geometry index; **collision** with the weights $\alpha_k$ and the blending $\alpha$ |
| $u$ | $v$ | velocity |
| $V$ | $V=1/\rho$ (local) | specific volume |
| $E$, $e$ | $E/\rho$, $e$ | source $E$ is total energy per unit mass; registry $E$ is per unit volume |
| $p$, $\rho$, $\gamma$ | $p$, $\rho$, $\gamma$ | agree; "γ" after an equation number marks ideal-gas formulas |
| $C=c/V$, $c$ | $C_{\mathrm L}=\rho c$ (local), $c$ | Lagrangean and Eulerian sound speed |
| $\pm W$ | $\pm W_{\mathrm L}$ (local) | Lagrangean wave speed (mass flux); **collision** with the Lorentz factor $W$ |
| $\bar Q_{i+1/2}$, $\bar Q^{i+1/2}$ | $\bar u_i^n$, $\bar u_i^{n+1}$ | mass averages at the start and end of the step |
| $\tilde Q$ | volume average (local) | |
| $Q_{i-}$, $Q_{i+}$ | $u^-_{i-1/2}$, $u^+_{i-1/2}$ | values just left and right of the interface |
| $Q^*$ | $u^*$ (local) | resolved state at an interface |
| $\langle Q\rangle_i$ | time average over the step (local) | |
| $\Delta_i\bar Q=\bar Q_{i+1/2}-\bar Q_{i-1/2}$ | $\bar u_i-\bar u_{i-1}$ | |
| $\bar\Delta_{i+1/2}Q$ | $\mathsf s_i$ (local) | stored undivided slope |
| $\varphi_{i+1}$, $f_{i+1}$ | $\varphi$, $f_{\mathrm v}$ (local) | mass and volume fraction crossing an Eulerian boundary; **collision** of $f$ with the flux |
| $\sigma$ | $\nu$ | local Lagrangean Courant number |
| $J^\pm$ | Riemann invariants (local) | |
| $F$, $G$ | components of $S(u)$ | momentum and internal-energy sources |
| $Z_\pm$, $p_{\min}$ | local | tangent slopes of the wave curves; cavitation floor |

# Reference list

The paper prints 20 references, numbered [1]–[20]; titles are printed only for a
few of them. The list is merged complete into the [bibliography](/bibliography.md),
with `citedby` including `vanleer-1979`. Three 1977 works of van Leer are
identified by volume and page, not by printed order: ref. [2] is paper IV
(J. Comput. Phys. 23:276), ref. [5] paper III (J. Comput. Phys. 23:263), and ref.
[17] the appendix to the original version of this paper (October 1977,
unpublished), a distinct work. Ref. [10] is Boris's NRL Memorandum Report 3237
(March 1976), a different work from the Flux-corrected transport III paper of
the same year. Ref. [4] prints the co-author spelling "Zabrodyn". Refs. [8] and
[16] are private communications from Woodward (1977, 1978). No item is
unparseable.

# Pages created or updated

Chunk 12 (2026-10-30). This source is cited on:

* [Bound preservation](/properties/bound-preservation.md)
* [Conservative remapping for ALE schemes](/methods/conservative-remapping.md)
* [Generalized Riemann problem (GRP) solvers](/methods/generalized-riemann-problem.md)
* [Godunov scheme](/methods/godunov-scheme.md)
* [Gradient-based reconstruction (MEG/MIG schemes)](/methods/gradient-based-reconstruction.md)
* [Mach 3 forward-facing step](/benchmarks/forward-facing-step.md)
* [MUSCL and MUSCL–Hancock schemes](/methods/muscl-hancock.md)
* [Numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
* [Operator splitting for stiff source terms](/methods/operator-splitting.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [Total variation diminishing (TVD) and slope limiters](/definitions/total-variation-diminishing.md)
