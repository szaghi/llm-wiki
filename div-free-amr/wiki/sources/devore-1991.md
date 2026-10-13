---
type: Source
title: "DeVore (1991) — Flux-corrected transport techniques for multidimensional compressible magnetohydrodynamics"
description: "Flux-corrected transport for the induction equation on a staggered mesh: face fields updated by edge fluxes keep the discrete Gauss law to roundoff, and a component-split edge-flux corrector limits each field component's antidiffusion separately; no divergence value reported."
resource: "doi:10.1016/0021-9991(91)90295-V"
source_kind: paper
authors: [DeVore C.R.]
year: 1991
venue: "J. Comput. Phys. 92:142-160"
local_file: "/home/stefano/papers/mosaic/div-free-amr/1991-JCP-DeVore-1010160021-99919190295-V.pdf"
tags: [constrained-transport, staggered, flux-corrected-transport, mhd, induction-equation]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

DeVore gives a flux-corrected transport (FCT) prescription for the
induction equation on a staggered mesh. Face-normal field components sit
on cell faces and the convective fluxes $\mathbf v\times\mathbf B$ on cell
edges, so the discrete integral Gauss law holds to machine roundoff
(abstract; §2, eqs. 5–6). He credits this placement to Schnack & Killeen
(1980) and Evans & Hawley (1988). His own contribution is the flux
corrector. Applying Zalesak's continuity-equation corrector to the total
antidiffusive edge flux is monotone but "excessively diffuse" (§2,
eqs. 14–16). DeVore instead splits each edge antidiffusive flux into one
partial flux per field component, limits each against the extrema of its
own normal component, and recombines them (§2, eqs. 17–23); monotonicity
is then enforced only approximately. The Appendix gives the 2D algorithm
(eqs. A1–A10). Two tests compare the FCT field solver with an FCT
vector-potential solver and with the Evans–Hawley
[CT](/methods/constrained-transport.md) solver: rigid rotation of a
current-carrying cylinder, and Low's self-similar magnetic bubble (§3).
**No divergence value is reported**; the invariant is asserted.

# Key claims

1. **Staggered placement keeps the discrete divergence** (abstract; §2
   pp. 144–145, Fig. 1, eqs. 5–6). Face components are updated from edge
   fluxes $(\mathbf v\times\mathbf B)$ times edge length; fluxes at a
   common edge cancel pairwise, so for any closed surface the rate of
   change of the net magnetic flux is zero (eq. 6). "If Gauss's law in its
   discrete integral form is satisfied by the field configuration
   initially, it is satisfied for all time" (p. 145). The source term of
   the induction equation (eq. 1b) is also evaluated on edges. In registry
   terms the held divergence is $D_h^{\mathrm f}B_h$ and the update is
   $\partial_t B_h = -C_h E_h$ with $E_h$ on edges.
2. **Every stage is an edge-flux update** (Appendix, eqs. A1, A3, A6, A7,
   A10). Convective, diffusive, source and corrected antidiffusive fluxes
   all live on edges, so the low-order, high-order and final fields all
   keep the discrete Gauss law. The partial low-order fields used by the
   corrector "are not divergence-free, but they are used solely to correct
   their associated partial antidiffusive fluxes" (p. 157).
3. **A split field update is nonconservative** (§4, p. 156). Each edge
   flux changes four face values along two directions, so "the calculation
   is inherently multidimensional—an operator-split integration for the
   individual field components is necessarily nonconservative". The
   continuity equation can be split conservatively. Argued, not proved.
4. **FCT procedure** (§2, p. 145, steps 1–4): a low-order positive
   solution by strong diffusion; antidiffusive fluxes giving a high-order
   solution; their correction (limiting); application of the corrected
   fluxes.
5. **Zalesak's corrector, restated** (§2, eqs. 7–13, steps a–f): extrema
   over the $3\times3$ neighbourhood of the old and low-order values;
   cancellation of downstream-directed fluxes; inflow and outflow sums,
   allowances and fractions; the flux factor is the minimum of the
   receiving cell's inflow fraction and the donor cell's outflow fraction.
6. **Why the joint corrector fails for the field** (§2, eqs. 14–16). The
   dominant velocity-independent part of the edge antidiffusive flux
   combines a derivative of one component along the other direction minus
   the converse (eq. 14). Only with uniform coefficients and commuting
   derivatives does $\nabla\cdot\mathbf B = 0$ turn the result into pure
   antidiffusion of each component (eqs. 15–16). Edge-by-edge limiting
   breaks the commutation; the two contributions "may oppose or reinforce
   each other", and a joint corrector then gives a "locally low-order,
   diffusive solution". The divergence identity is used analytically, to
   motivate the limiter.
7. **The component-split corrector** (§2, eqs. 17–23). For the partial
   flux from $B_x$: extrema per $x$-face from the old field and the
   $B_x$-only low-order field, over a 3-point transverse search (eq. 17);
   cancellation when the flux opposes the local gradient and one
   neighbouring gradient (eq. 18); sums, allowances and fractions per face
   (eqs. 19–21); the edge factor as the minimum of the receiving and donor
   fractions (eq. 22); recombination of the two corrected partial fluxes
   (eq. 23). It is "not as restrictive as that for the continuity equation,
   but still approximately enforces the monotonicity constraint" (p. 148);
   "the monotonicity constraint clearly cannot be strictly enforced by any
   flux-corrector which splits the antidiffusive fluxes in this way" (§4).
8. **Justification** (§2, pp. 149–150): in smooth regions the coefficients
   are nearly uniform and the transverse contributions give only "benign"
   residual smoothing; at a discontinuity the tangential component changes
   much faster than the normal one, so limiting the tangential partial
   flux does not abruptly change the normal component.
9. **3D generalization** (§2, p. 150): the extremum search spans both
   transverse indices and each edge flux combines partial fluxes from the
   two field components normal to its adjacent faces. No 3D test is run.
10. **2D algorithm and accuracy** (Appendix, eqs. A1–A10; p. 160). Edge
    fields are two-point averages of face values (eq. A2); diffusion and
    antidiffusion coefficients are quadratic in the signed Courant number
    (eqs. A5, A9). For uniform advection on a uniform mesh the low-order
    solution has second-order and the high-order solution fourth-order
    phase and amplitude errors at long wavelengths, and the scheme is
    "absolutely stable" for Courant numbers below $\tfrac12$ in magnitude.
    Stated, not shown.
11. **FCT dissipation acts as a resistivity** (§4, p. 157), concentrated
    at current sheets: "the less restrictive is the rule used, the lower is
    the dissipation rate, but the noisier are the solutions".
12. **Field solver versus potential solver** (§§3–4). Advecting a smooth
    potential monotonically and differentiating it twice gives worse
    current densities. The FCT field solver holds "a small advantage" in
    flux-surface and field accuracy over both the FCT potential solver and
    CT, and a current-density advantage that is "only marginally so with
    respect to the CT field solver". The current errors do not translate
    into substantially different flux or field errors in these tests,
    which DeVore attributes to high $\beta$ and short runs.

# Tests

Relative L1 error of the flux function, the field and the current
density (§3, p. 151). Three solvers: this FCT field solver, an FCT
flux-function solver (companion NRL report, not described), and the
Evans–Hawley CT field solver.

1. **Rigid rotation of a current-carrying cylinder** (§3, pp. 151–154,
   Figs. 2–3). Magnetic analogue of Zalesak's slotted cylinder; uniform
   interior current with a return-current sheath; $100\times100$ mesh,
   radius 15 zones, Courant number 0.25, 1256 steps per rotation. Errors
   after one rotation:
   * flux function: FCT field 6%, FCT potential 4%, CT 14%;
   * field: both FCT 25%, CT 45% (Zalesak's slotted cylinder with the FCT
     fluid solver: 24%);
   * current density: FCT potential 90%, FCT field 79%, CT 91%; the
     potential solver shows a current reversal near the axis above 70% of
     the initial interior value; CT gives "the only monotonic profile, but
     the lowest quantitative accuracy".
2. **Self-similar expansion of a magnetic bubble** (Low; §3, pp. 154–156,
   Fig. 4). Spherical $(r,\theta)$ mesh $100\times100$ with radial spacing
   growing linearly, 600 steps, average Courant number about 0.25,
   predictor–corrector time integration, minimum $\beta = 1$. Errors:
   * flux function 8–9% for all three solvers;
   * field: both FCT 20%, CT 25%;
   * current density: FCT potential 113%, FCT field 88%, CT 88%; current
     reversals at the 90% (potential) and 10% (field) levels.

No shock tube, no 3D run, no convergence study and no divergence
diagnostic.

# Notation map

| DeVore | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $B_{x,i+1/2,j}$, $B_{y,i,j+1/2}$ | $B_h \in V_h^2$ | face-normal components; the paper evolves field times face area |
| edge flux $(\mathbf v\times\mathbf B)_z L_z\Delta t$ | $-\Delta t\,L_z\,E_h$, $E_h \in V_h^1$ | **sign:** $\mathbf E = -\mathbf v\times\mathbf B$ |
| discrete integral Gauss law, eq. 6 | $D_h^{\mathrm f}B_h$ | face-flux difference over a cell |
| $A_x$, $A_y$ (face areas) | words | **collision:** $A_h$ is the vector potential; the paper also writes $\mathbf A$ for it (eq. 24) |
| $\mathbf A$, $\psi$ (flux function) | $A_h$; in 2D Cartesian $A_z$ | **collision:** $\psi_h$ is the GLM potential |
| $L_z$, $V$ | words | edge length, cell volume |
| $\rho$ (generic transported variable) | $w$ | not only density |
| superscripts $o$, $l$, $h$, $f$ | $n$; words for the FCT stages | **collision:** $h$ is the grid spacing |
| $F^a$, $\tilde F^a$, $F^{ax}_z$, $F^{ay}_z$ | words | uncorrected, corrected and partial antidiffusive fluxes |
| $C$ (correction factor) | words | **collision:** $C_h$ is the discrete curl |
| $P^\pm$, $Q^\pm$, $R^\pm$ | words | **collision:** $P$, $R$ are prolongation and restriction |
| $\nu_{xx}$, $\mu_{xx}$, $\mu_{xy}$ | words | diffusion and antidiffusion coefficients |
| $\varepsilon_x$, $\varepsilon_y$ | words (signed Courant number) | the paper also uses $\varepsilon$ for its error measure |
| $\beta$ | $\beta$ | plasma beta |
| $\mathbf s_1\ldots\mathbf s_5$ | words | source terms |

# Pages created or updated

* Updated [Constrained transport (CT)](/methods/constrained-transport.md): the FCT primary source (staggered FCT, edge-flux limiting, the split-update argument, the current-density evidence); "The Brecht et al. and DeVore papers are not ingested" replaced.
* Updated [Ryu, Miniati, Jones & Frank (1998)](/sources/ryu-1998.md): DeVore's member of the "artificial-viscosity based" CT group is FCT.
* Updated [vector-potential evolution](/methods/vector-potential-evolution.md): a second source for the current-density objection.
* Updated [exact discrete divergence](/properties/exact-discrete-divergence.md): intermediate limiter fields need not be divergence-free.

# Citations

1. `~/papers/mosaic/div-free-amr/1991-JCP-DeVore-1010160021-99919190295-V.pdf`.
   * **Version read.** The published journal version, a 19-page scan
     (Acrobat Capture, 2003) with an OCR text layer. Received 19 July
     1989; revised 25 October 1989.
   * **Identity.** doi:10.1016/0021-9991(91)90295-V, checked on Crossref:
     title and author match; J. Comput. Phys. vol. 92, issue 1, pp.
     142–160, issued January 1991.
   * **How it was read.** The OCR layer garbles every equation; all
     equations were read from page renders at 130–300 dpi (eq. 22 indices
     at 220 dpi; the bubble parameter $GMt_0^2/r_0^3 = \tfrac23$ at 300
     dpi). Eq. A8 is legible but its index subscripts are small; it is
     described, not reproduced. The companion FCT fluid and potential
     solvers are in an unpublished NRL report and are not described.
   * **Recorded as printed.**
     * The source edge flux of the Appendix (p. 159) is written with
       $s_{4z}$ and called "the edge flux due to the source term
       $\mathbf s_4$", while eq. 1b carries $\mathbf s_5$ (reader's
       reading: a misprint).
     * §2, p. 150 says "in Fig. (19)" where eq. (19) is meant.
     * The accuracy and stability statements (Appendix, p. 160) are
       asserted without the analysis.
   * **Reference list.** 15 entries, all merged; only ref. 6 prints a
     title, and no DOIs are printed. Boris & Book's FCT III (J. Comput.
     Phys. 20:397) is the new entry `boris-1976-b`; the NRL Memorandum
     Report 3237 stays `boris-1976`. Book, Boris & Hain (1975), J. Comput.
     Phys. 18:248, is `book-1975`, rekeyed from `boris-1975` on Crossref
     (first author Book; "printed with Boris first by sod-1978"). The
     private communication of Zalesak (1987) is `zalesak-1987-b`, distinct
     from `zalesak-1987`. Löhner et al. (1988), Commun. Appl. Numer.
     Methods 4:717, is `lohner-1988-b`, distinct from `lohner-1988`. Evans & Hawley is the ingested
     `evans-hawley-1988`. The bibliography holds 3834 entries after this
     batch.
