---
type: Source
title: "Balsara & Nkonga (2017) — Multidimensional Riemann problem with self-similar internal structure – part III – a multidimensional analogue of the HLLI Riemann solver for conservative hyperbolic systems"
description: "A 1D HLLI variant with a Galerkin first-moment constraint (shifted mean flux, new anti-diffusion weights, dissipation within 23.2 % of Roe in the cases shown) and its two-dimensional MuSIC analogue at vertices, which reduces to multidimensional HLL without sub-structure; used in ADER–WENO of orders 2–4 for Euler, MHD and RMHD, where sub-structure cuts the dissipation of a torsional Alfvén wave 6× at second order and 3× at third."
resource: "doi:10.1016/j.jcp.2017.05.038"
source_kind: paper
authors: [Balsara D.S., Nkonga B.]
year: 2017
venue: "J. Comput. Phys. 346:25–48"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2017-JCP-Balsara-101016jjcp201705038.pdf"
tags: [riemann-solver, multidimensional-riemann-solver, hllem, ader, mhd]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The third paper of Balsara's series on multidimensional Riemann solvers
with self-similar internal structure. It builds a two-dimensional MuSIC
("Multidimensional, Self-similar, strongly-Interacting, Consistent")
Riemann solver for the vertices of Cartesian meshes, the
multidimensional analogue of HLLI. It first re-derives a 1D HLLI with a
first-moment (Galerkin) constraint, which shifts the mean flux away from
HLL and leads to new anti-diffusion weights (§2), and gives the first
quantitative comparison of such a solver's dissipation with Roe's. The
2D solver (§3) reduces to multidimensional HLL at zero slopes. It is
"universal" (Euler, MHD, relativistic MHD) and is used inside ADER–WENO
of orders 2–4 (§§4–5). Merged into the new
[multidimensional Riemann solvers](/methods/multidimensional-riemann-solvers.md)
page and the [HLLEM (HLLI)](/methods/hllem-riemann-solver.md) and
[Riemann-solver](/methods/approximate-riemann-solvers.md) pages.

# Key claims

1. **1D HLLI with the Galerkin constraint** (§2.1, eqs. 2.1–2.8). The fan
   state is linear in the similarity variable scaled to the fan. The
   zeroth moment gives the mean state $u^{\mathrm{HLL}}_*$; the first gives
   a mean flux equal to the HLL flux plus $(S_R - S_L)/6$ times the slope,
   so with sub-structure the mean flux is not the HLL flux. The slope is
   $\sum_{p\in\mathcal I}2\delta_p\,\ell^{(p)}(u^+ - u^-)\,r^{(p)}$.
2. **Flux and weights** (eqs. 2.9c, 2.10, 2.11, page images). HLL plus an
   anti-diffusive term on the intermediate families only, with
   $\delta_p$ bounded so that the viscosity eigenvalues "minimally match
   or exceed" Roe's, and capped at $-3S_RS_L/(S_R - S_L)^2$ (at most 3/4,
   at $S_R = -S_L$) to keep stationary linearly degenerate waves exact; the
   cap is "not mandated by mathematics". The supersonic limit gives HLL
   ([HLLEM](/methods/hllem-riemann-solver.md) has the formulas).
3. **Dissipation against Roe** (§2.2, Fig. 1). With $S_R - S_L = 1$ and one
   subsonic intermediate wave: at most 23.2 % above Roe for
   $(S_L, S_R) = (-0.9, 0.1)$, 17.6 % for $(-0.2, 0.8)$, equal for
   $(-0.7, 0.3)$ and $(-0.5, 0.5)$, practically equal for $(-0.01, 0.99)$;
   zero for a stationary wave.
4. **Against Dumbser–Balsara** (§2.3, eqs. 2.12–2.14). Their "HLLI-type"
   solver has no first-moment constraint, a fan flux quadratic in the
   similarity variable, the HLL mean flux, and a weight that allows larger
   values. The cost is almost the same. "In practice, both work equally
   well."
5. **Positivity** (§§2.1, 2.4). Check the HLL state plus and minus half
   the slope and reduce the slope if needed; at zero slope the flux is
   HLL. Sub-structure is skipped when the HLL density or pressure is
   "substantially" outside the range of the inputs (no threshold). A
   procedure, not a proof.
6. **2D MuSIC solver** (§3.1, eqs. 3.4–3.22). Wave model
   $[S_L, S_R]\times[S_D, S_U]$; a strongly interacting state linear in
   both similarity variables; mean state and fluxes from zeroth and first
   moments, with boundary integrals of the 1D solutions on the four sides
   (eqs. 3.10–3.12, from part I); undivided differences across the wave
   model projected on $x$- and $y$-eigenvectors at the mean state.
7. **"The proof steers us false"** (§3.1, App. B). With 1D HLLI profiles on
   the boundary the 2D flux reduces exactly to 1D HLLI for $x$-aligned
   flow (proved), but those profiles are "overly steepened", produce too
   little entropy in the transverse fluxes, and make the solver unstable at
   strong shocks. The paper therefore uses constant HLL states on the
   boundary; the 2D weights change accordingly (eqs. 3.18–3.21), and the
   reduction to 1D HLLI becomes "closely analogous", not exact.
8. **Properties of the 2D solver** (§3.1). Complete when all waves are
   included; keeps mesh-aligned stationary contacts; "inherits" HLLI
   well-balancing (asserted); positivity enforced at the four vertices of
   the wave model by reducing the differences; exactly multidimensional
   HLL at zero slopes; HLLC or HLLD sides via least squares give "not that
   much incremental benefit".
9. **ADER–WENO integration** (§4). Face fluxes by a "simplified Simpson
   rule": weight 1/6 to each of four multidimensional solves at the edge
   centres of a face and 1/3 to a 1D HLLI solve at the face centre, fed by
   time-averaged predictor states. For MHD the edge solves give the edge
   electric field. The number of Riemann solves does not grow with order.
10. **CFL** (§4). 0.8 for second- and third-order hydrodynamics; 0.4 at
    fourth order, where the assumption that spatial and temporal accuracy
    commute "clearly breaks down". FV schemes for the induction equation
    are stable only up to 0.666 (Balsara & Käppeli 2017), so MHD and RMHD
    use 0.65 at second and third order and 0.4 at fourth.
11. **Dissipation doubling** (§1). Doubling the upwind dissipation of edge
    electric fields (Gardiner–Stone) is "completely unnecessary" with
    multidimensional Riemann solvers. Asserted with citations; no test
    isolates it.
12. **Solver quality against order** (§§5.5, 5.7, 6). On torsional
    Alfvén-wave decay, 1D HLL with a 2D solver without sub-structure
    dissipates 6 times more at second order and 3 times more at third than
    1D HLLI with a 2D solver with sub-structure; at fourth order the
    difference is "almost negligible". Second order with the better
    solvers is less dissipative than third order with the inferior ones.
    The relativistic repeat gives the same ordering (no factors).
    Sub-structure costs "only marginally" more (no timings).

# Tests

All with ADER–WENO and the 2D MuSIC solver (1D HLLI at face centres).

| § | Test | Set-up as printed | Result |
|---|---|---|---|
| 4.1 | [Isentropic vortex](/benchmarks/isentropic-vortex.md), 45° | $[-5, 5]^2$ to $t = 10$ at orders 2–3; $[-10, 10]^2$ to $t = 20$ at order 4 (the exponential tail is felt at the boundary); $64^2$–$512^2$ | $L^1$ orders on $512^2$: 2.10, 2.98, 3.76 ($L^\infty$ 2.12, 2.97, 4.24); $L^1$ errors 7.4763E−6, 1.3157E−6, 7.9390E−8 (Table 1) |
| 4.2 | MHD vortex, 45° | same domains and times | $B_x$ $L^1$ orders 2.00, 2.97, 4.11; $L^\infty$ 1.99, 2.41, 4.10. The third-order $L^\infty$ order falls 2.69, 2.60, 2.41 across refinements, uncommented; the paper says all "meet the expected order" (Table 2) |
| 5.1 | [Forward-facing step](/benchmarks/forward-facing-step.md) | Mach 3, $[0, 3]\times[0, 1]$, $960\times320$, $t = 4$, fourth order | the vortex-sheet roll-up from the triple point is captured "very well" |
| 5.2 | [Double Mach reflection](/benchmarks/double-mach-reflection.md) | Mach 10, 60°, $[0, 4]\times[0, 1]$, $1920\times480$, $t = 0.2$, fourth order | "very well-resolved roll-up of the Mach stem" |
| 5.3 | [MHD rotor](/benchmarks/mhd-rotor.md) | $[-0.5, 0.5]^2$, radius 0.1, $1000^2$, $t = 0.29$, fourth order; states not printed | qualitative |
| 5.4 | 3D [MHD blast](/benchmarks/mhd-blast-wave.md) | $\gamma = 1.4$, $\rho = 1$, $p = 0.1$, $B_x = B_y = B_z = 150/\sqrt3$, $p = 1000$ inside radius 0.1; unit cube, $257^3$, plasma beta $1.117\times10^{-4}$, CFL 0.4, $t = 0.0075$, third order | density and pressure "positive as expected"; the positivity safeguards active are not stated |
| 5.5 | [Torsional Alfvén-wave decay](/benchmarks/circularly-polarized-alfven-wave.md) | 9.462° to the $y$-axis, $[-3, 3]^2$, $120^2$, periodic, $t = 129$, orders 2–4 | claim 12 |
| 5.6 | Relativistic [Orszag–Tang](/benchmarks/orszag-tang-vortex.md) | unit square, $1000^2$, $t = 0.8$, fourth order | qualitative |
| 5.7 | RMHD torsional Alfvén decay | after Balsara & Kim | same ordering as §5.5, no numbers |
| 5.8 | Stationary contact, not mesh-aligned | $[-1, 1]^2$, $81^2$, $p = 1$, $\mathbf v = 0$, $\gamma = 1.4$; density a tanh step from 1 inside radius 0.5 to 0.1 outside, width half a cell; $t = 10$; CFL 0.6, 0.8, 0.4 at orders 2, 3, 4 | second order smears "just a little", third much less, fourth "tracks the initial contact discontinuity exactly"; linear reconstruction can give negative vertex densities here |

# Notation map

| Balsara & Nkonga (2017) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf U$, $\mathbf F$, $\mathbf G$ | $u$, $f$ ($x$-flux), $y$-flux in words | |
| $\mathbf U_L$, $\mathbf U_R$ | $u^-$, $u^+$ | |
| $\mathbf U_{RU}$, $\mathbf U_{LU}$, $\mathbf U_{LD}$, $\mathbf U_{RD}$ | same subscripts | the four vertex states, as on the CT page |
| $S_L$, $S_R$, $S_D$, $S_U$ | $S_L$, $S_R$, $S_D$, $S_U$ | |
| $\tilde\xi = x/t$, $\tilde\psi = y/t$; scaled $\xi$, $\psi$ | (words: similarity variables) | collide with $\xi$, $\tilde\xi$, $\psi$ |
| $\xi_c$, $\Delta\xi$ | $(S_R + S_L)/2$, $S_R - S_L$ | |
| $\bar{\mathbf U}$, $\bar{\mathbf F}$, $\bar{\mathbf G}$ | (words: mean strongly interacting state), $f^{**}_x$, $f^{**}_y$ | the overbar is the cell average in the registry |
| $\bar{\mathbf U}_{HLL}$, $\bar{\mathbf F}_{HLL}$ | $u^{\mathrm{HLL}}_*$, $\hat f^{\mathrm{HLL}}$ | |
| $\mathbf U_\xi$, $\mathbf U_\psi$ | (words: slopes of the strongly interacting state) | |
| $\Delta_\xi\mathbf U$, $\Delta_\psi\mathbf U$ | (words: undivided differences across the wave model) | collide with $\Delta^l w_i$, $\Delta u_i$ |
| $\bar{\mathbf A}$, $\bar{\mathbf B}$ | $A$ and the $y$-Jacobian at the mean state | $\mathbf B$ is the magnetic field |
| $\lambda_i$, $r_i$, $l_i$; $\mathbf R$, $\mathbf L$, $\boldsymbol\Lambda$ | $\lambda^{(p)}$, $r^{(p)}$, $\ell^{(p)}$; $R$, $L$, $\Lambda$ | restricted to $p \in \mathcal I$ |
| $I_{int}$ | $\mathcal I$ | |
| $\delta_i$ | $\delta_p$ | a different formula from Dumbser–Balsara's, see [HLLEM](/methods/hllem-riemann-solver.md) |
| $\phi_i$, $\phi^x_i$ (weight caps) | (written out) | collide with $\phi_i$ |
| $\lambda_i^\mp$ | $\min(\lambda^{(p)}, 0)$, $\max(\lambda^{(p)}, 0)$ | |
| $\mathbf E$ (electric field) | $\boldsymbol{\mathcal E}$ | |

# Pages created or updated

* Created [Multidimensional Riemann solvers](/methods/multidimensional-riemann-solvers.md).
* Updated [HLLEM (HLLI) Riemann solver](/methods/hllem-riemann-solver.md) ("HLLI" names a family; the second weight), [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md) (primary source of the solver-quality factors).
* Also cited on [Hyperbolic (GLM) divergence cleaning](/methods/hyperbolic-divergence-cleaning.md).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2017-JCP-Balsara-101016jjcp201705038.pdf`.
   * **Version.** The publisher's version of record (Elsevier, 24 pages).
     Received 18 December 2016, revised 16 May 2017, accepted 18 May 2017,
     online 24 May 2017.
   * **Identity.** doi:10.1016/j.jcp.2017.05.038, printed on page 1 and
     checked on Crossref: J. Comput. Phys. 346:25–48, October 2017, authors
     Balsara, Nkonga; title identical to page 1. Slug `balsara-2017-b`,
     since the bare `balsara-2017` is Balsara & Käppeli (JCP 336:104).
   * **How it was read.** Text extraction, all sections; eqs. 2.1–2.11 and
     3.18–3.22 checked on the page images. Eqs. 3.10–3.12 and the ALE
     appendix were read from the text layer only. Figures are read through
     their captions and the text.
   * **Recorded as printed.**
     * Table 1: the third-order $256^2$ $L^1$ error is printed 1.0361E−6,
       but the printed orders 2.96 and 2.98 on either side both imply
       1.0361E−5.
     * The conclusion that the dissipation is "within ten to twenty
       percent" of Roe "under all circumstances" contradicts the paper's
       own 23.2 % case.
     * §1 cites "Vides, Nkonga and Audit [69]", but [69] is Wendroff; the
       Vides paper is [68]. The §5.4 heading reads "3D be last problem".
   * **Reference list:** 70 printed entries, 69 bibliography entries:
     refs. [64] and [65] are the same Shock Waves 4:25 paper (Toro, Spruce
     & Speares) printed twice with different wording, merged into
     `toro-1994`. Castro-Díaz et al. is `castro-2012`; Harten, Lax & van
     Leer, printed SIAM Rev. 25:289, is `harten-1983-d`. Printed-order
     suffixes of the Balsara self-citations (2009, 2012, 2014, 2015) were
     resolved by vol:page. Ref. [35] prints "48 (70) (2011) 88" and
     ref. [60] an issue "(2.7)", recorded as printed. The bibliography's
     title for this paper was corrected from Crossref; citing papers print
     the earlier title "Formulating multidimensional Riemann solvers in
     similarity variables—part III".
