---
type: Source
title: "DeVore (1991) — Flux-Corrected Transport Techniques for Multidimensional Compressible Magnetohydrodynamics"
description: "Flux-corrected transport for the MHD induction equation on a staggered collocation (normal fields on cell faces, v×B on edges) that keeps the discrete Gauss law exactly; Zalesak's limiter applied to the edge flux is monotone but too diffusive, so the antidiffusive edge flux is split into the parts driving each field component and each is limited separately, which keeps monotonicity only approximately; tests compare FCT field, FCT vector-potential and Evans–Hawley CT solvers."
resource: "doi:10.1016/0021-9991(91)90295-V"
source_kind: paper
authors: [DeVore C.R.]
year: 1991
venue: "J. Comput. Phys. 92:142–160"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/1991-JCP-DeVore-1010160021-99919190295-V.pdf"
tags: [mhd, divergence-free, constrained-transport, flux-corrected-transport, staggered, vector-potential]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper integrates the MHD induction equation with flux-corrected
transport (FCT) while keeping $\nabla\cdot\mathbf B = 0$ to round-off.
Divergence control comes from the collocation: normal field components on
the faces of the cell that carries the fluid variables, convective fluxes
$\mathbf v\times\mathbf B$ on the edges, and a discrete Stokes update, so
that the discrete Gauss law (eq. 6) holds for all time if it holds
initially (§2, Fig. 1). This is a staggered collocation of the Evans–Hawley
constrained-transport kind, which DeVore cites. The contribution is the
flux corrector. Zalesak's multidimensional FCT limiter applied directly to
the antidiffusive edge flux is monotone but "excessively diffuse", because
that flux is the difference of a part that drives $B_y$ and a part that
drives $B_x$, which need not be antidiffusive together (eqs. 14–16).
DeVore splits it into these two partial fluxes, limits each against its
own field component (eqs. 17–22) and recombines them (eq. 23);
monotonicity then holds only approximately. The Appendix gives a 2D
algorithm (convection, diffusion, antidiffusion; eqs. A1–A10). Two tests,
a rigidly rotating current-carrying cylinder and Low's self-similar
magnetic-bubble expansion, compare the FCT field solver with an FCT
vector-potential solver and with Evans–Hawley CT.

# Key claims

1. **Staggered collocation, exact discrete Gauss law** (§2, eqs. 3–6,
   Fig. 1). Fluid variables are cell-centred with fluxes $\rho\mathbf v$ on
   faces (eq. 4); field components on the faces of the same cell, fluxes
   $\mathbf v\times\mathbf B$ on edges (Fig. 1, right). In 2D with forward
   Euler (eq. 5, page image), the face-area-weighted change of $B_x$ at
   $(i+1/2, j)$ is the difference of the edge-length-weighted
   $v_yB_x - v_xB_y$ at the edges $(i+1/2, j\mp1/2)$, and cyclically.
   Since $v_yB_x - v_xB_y = \mathcal E_z$, this is
   $\partial_t B_x = -\partial_y\mathcal E_z$, the Yee update with the
   registry sign (reader's check). Pairwise cancellation of edge fluxes
   gives eq. 6: "if Gauss's law in its discrete integral form is satisfied
   by the field configuration initially, it is satisfied for all time"
   (p. 145); this also holds with a conservative edge source.
2. **Governing form** (eq. 1). $\partial_t\rho + \nabla\cdot(\rho\mathbf v)$
   equals a general source, where $\rho$ stands for **any** fluid variable
   (mass, momentum or energy density); $\partial_t\mathbf B = \nabla\times(\mathbf v\times\mathbf B)$
   plus the curl of an edge source.
3. **FCT recipe** (§2, steps 1–4, p. 145). A low-order positive solution by
   strong diffusion; antidiffusive fluxes giving a high-order solution;
   correction; application of the corrected fluxes to the low-order
   solution.
4. **Zalesak's limiter restated** (§2 (a)–(f), eqs. 7–13). Bounds from the
   larger of old and low-order values, maximized (minimized) over the
   9-point block (eq. 7); cancellation of an antidiffusive flux that points
   down the low-order gradient and down a neighbouring gradient (eq. 8);
   sums of incoming and outgoing antidiffusive fluxes (eq. 9); ratios
   $\min(1, \text{allowance}/\text{sum})$ with allowances the distance of the
   low-order value to the bounds times the volume (eqs. 10–11); the face
   factor is the smaller of the receiving cell's incoming ratio and the
   donor cell's outgoing ratio (eq. 12); the corrected flux is the factor
   times the antidiffusive flux (eq. 13). The corrected update is the
   blend $\theta_{i+1/2}\hat f^{\mathrm{HO}} + (1 - \theta_{i+1/2})\hat f^{\mathrm{LO}}$
   with $\theta$ the FCT factor, but the bounds are local extrema, not
   $\mathcal G$ (reader's identification).
5. **Why the hydrodynamic corrector fails for the induction equation**
   (pp. 147–148, eqs. 14–16). The dominant, velocity-independent part of the
   edge antidiffusive flux is a coefficient times $\partial_xB_y$ minus a
   coefficient times $\partial_yB_x$ (eq. 14), used as
   $\partial_tB_x = +\partial_y(\cdot)$, $\partial_tB_y = -\partial_x(\cdot)$
   (eq. 15). Only the first term of each is antidiffusive; the cross terms
   become antidiffusive only for uniform coefficients, when
   $\nabla\cdot\mathbf B = 0$ turns them into antidiffusion of the same
   component (eq. 16). Applying Zalesak's limiter per edge "is guaranteed
   to be monotonic, but it also is excessively diffuse, in practice"
   (p. 147): the two contributions "may oppose or reinforce each other, or
   one may overwhelm the other", and the corrector cuts the flux to protect
   the smaller one.
6. **The split flux corrector** (§2 (a)–(f), eqs. 17–23, page images at
   220 dpi). Per field component, on faces, ignoring the transverse
   component's contribution: bounds for $B_x$ at $(i+1/2, j)$ are the
   extrema of three values along the **transverse index $j$ only**, of the
   larger of old and $B_x$-only low-order values (eq. 17); cancellation as
   in eq. 8 along $j$ (eq. 18); incoming and outgoing sums of the partial
   flux at the two edges $(i+1/2, j\pm1/2)$ (eq. 19); ratios with
   allowances times the face area (eqs. 20–21); edge factor from the two
   faces (eq. 22); the corrected edge flux is the difference of the two
   corrected partial fluxes (eq. 23). "The monotonicity constraint of FCT
   ... cannot be strictly enforced without producing an excessively
   diffuse solution" (§1, p. 142); the split corrector "still approximately
   enforces the monotonicity constraint" (p. 148). The justification is
   heuristic (p. 149): in smooth regions the coefficients are nearly uniform,
   so eq. 16 nearly holds and the transverse terms add only "benign ...
   residual smoothing"; at a discontinuity the tangential field changes
   much faster than the normal one, so limiting the tangential part need not
   change the normal field abruptly.
7. **3D** (p. 150), stated, not tested: extremum search over both
   transverse indices; both modified partial fluxes enter the sums; the edge
   flux is combined as in eq. 23.
8. **Operator splitting** (§4, p. 156). Each edge flux touches four field
   values along two directions, so "an operator-split integration for the
   individual field components is necessarily nonconservative"; yet the
   corrector **must** treat the field components separately, otherwise
   fluxes "tend to be severely limited, producing a diffuse, inaccurate
   solution".
9. **Dissipation** (§4, p. 157). FCT on the field "generally will produce
   some dissipation of magnetic flux", acting "much like a physical
   resistivity", concentrated at current sheets; "the less restrictive is
   the rule used, the lower is the dissipation rate, but the noisier are
   the solutions". Suitability for instabilities, turbulence and
   reconnection is left open.
10. **2D algorithm and accuracy** (Appendix, eqs. A1–A10, p. 160).
    Convective edge fluxes from two-point averages of face fields; low-order
    diffusion coefficient $\tfrac16 + \tfrac13\nu_x^2$ and antidiffusion
    coefficients $\tfrac16 - \tfrac16\nu_x^2$ and $-\tfrac12\nu_x\nu_y$ in
    terms of the signed directional Courant numbers (A5, A9; registry-style
    reading of the paper's signed Courant numbers). For uniform advection
    on a uniform mesh the low-order phase and amplitude errors are second
    order and the high-order ones fourth order at long wavelengths,
    "absolutely stable for Courant numbers" below $\tfrac12$ in magnitude
    per direction; stated, with no proof or dispersion relation printed.
11. **Vector potential against field** (§3, eqs. 24–27). In 2D the flux
    function obeys a passive advection equation (eq. 26). The potential
    solver gives a smooth flux function but its derivatives amplify error:
    current reversals and the worst current errors, confirmed in both
    tests.

# Tests

Error measure (p. 151): relative $L^1$ error summed over edges, of the
flux function, the field and the current. Solvers: FCT field (this paper),
FCT potential (the companion fluid FCT on eq. 26), CT (Evans & Hawley).

1. **Rigid rotation of a current-carrying cylinder** (§3, pp. 151–154,
   Figs. 2–3), "analogous to Zalesak's slotted-cylinder test". Inside
   radius $r_0$: azimuthal field proportional to radius, uniform axial
   current; a return-current sheath at $r_0$ makes everything vanish
   outside. Rigid rotation, $100\times100$, cylinder of radius 15 zones in
   the upper half plane, Courant number 0.25, 1256 steps for one rotation;
   purely kinematic.
   * Flux-function errors: **6% FCT field, 4% FCT potential, 14% CT**.
   * Field errors: **25%** for both FCT solvers, **45%** CT (Zalesak's
     slotted cylinder with the FCT fluid solver: 24%).
   * Current errors: **79%** FCT field, **90%** FCT potential, **91%** CT.
     The potential solver reverses the current near the axis by more than
     **70%** of its initial interior value; CT gives the only monotone
     current profile, but the most smoothed.
2. **Self-similar expansion of a strong shock and magnetic bubble out of a
   stellar gravity well** (Low; §3, pp. 154–156, Fig. 4). Inertial flow
   $v_r = r/t$; $2t_0 \le t \le 5t_0$ on $r_0 \le r \le 5r_0$,
   $0 \le \theta \le \pi/2$, $100\times100$, radial spacing growing
   linearly; 600 steps at average Courant number about 0.25; minimum plasma
   beta 1; full compressible MHD with gravity.
   * Flux-function errors **8–9%** for all three; field errors **20%** (both
     FCT), **25%** (CT); current errors **113%** FCT potential, **88%** FCT
     field, **88%** CT. Current reversals: potential solver at the 90%
     level, field solver at the 10% level.
   * For long, low-beta runs "the direct solution for the magnetic field may
     be more clearly preferable" (p. 156): an expectation, not tested.

No convergence study, no shock tube, no divergence plot (exactness is by
construction).

# Notation map

| DeVore (1991) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho$ (any fluid variable) | a component of $u$ | **collision**: registry $\rho$ is density only |
| $\mathbf v$, $\mathbf B$ | $\mathbf v$, $\mathbf B$ | |
| $\mathbf v\times\mathbf B$ (edge flux) | $-\boldsymbol{\mathcal E}$ | $v_yB_x - v_xB_y = \mathcal E_z$ |
| $\mathbf s_5$ | words (edge source) | |
| $\mathbf A$, $A_z$, $A_\phi$ | $\mathbf A$ | |
| $A_x$, $A_y$ (face areas) | words | **collision**: Jacobian $A$, potential $\mathbf A$ |
| $V$ (cell volume), $L_z$ (edge length) | words | **collision**: Voronoi $V_i$ |
| $\psi$ (flux function) | words; $A_z$ in Cartesian 2D | **collision**: gauge scalar $\psi$ |
| $J_z$ | words (current density) | **collision**: registry $\mathbf J$ |
| superscripts $o$, $l$, $h$, $f$, $c$ | words (old, low-order, high-order, final, convected); cf. $\hat f^{\mathrm{LO}}$, $\hat f^{\mathrm{HO}}$ | |
| $\mathbf F^a$, $\tilde{\mathbf F}^a$ | $\hat f^{\mathrm{HO}} - \hat f^{\mathrm{LO}}$, and $\theta_{i+1/2}$ times it | |
| $C_{x,i+1/2,j}$, $C^x_z$ | $\theta_{i+1/2}$ | bounds are local extrema, not $\mathcal G$ |
| $P^\pm$, $Q^\pm$, $R^\pm$ | words (Zalesak sums, allowances, ratios) | **collision**: $P(x)$, eigenvector matrix $R$ |
| $\varepsilon_x$, $\varepsilon_y$ | signed directional Courant numbers (words) | **collision**: $\varepsilon$; registry $\nu_y$ is the saw-tooth Courant number |
| $\nu_{xx}$, $\mu_{xx}$, $\mu_{xy}$ | words (diffusion, antidiffusion coefficients) | **collision**: CFL $\nu$, diffusion $\mu$ |
| $\beta$ | plasma beta (words) | |

# Pages created or updated

* Updated [Constrained transport](/methods/constrained-transport.md) (batch-18 block: DeVore's staggered FCT, eqs. 5–6, the split flux corrector, FCT vs potential vs CT, the accuracy statement as printed).
* Updated [Positivity-preserving flux limiter](/methods/positivity-preserving-flux-limiter.md) (batch-18 block: Zalesak's FCT limiter as DeVore writes it, eqs. 7–13).

# Citations

1. `/home/stefano/papers/mosaic/high-order-capturing-schemes/1991-JCP-DeVore-1010160021-99919190295-V.pdf`.
   * **Version read.** The publisher's PDF, a 2003 Acrobat scan of 19
     pages with a poor OCR layer. Received July 19, 1989; revised October
     25, 1989.
   * **Identity.** doi:10.1016/0021-9991(91)90295-V (from the PII and the
     archive filename), checked on Crossref: "Flux-corrected transport
     techniques for multidimensional compressible magnetohydrodynamics",
     C. Richard DeVore, J. Comput. Phys. 92(1):142–160, January 1991.
   * **How it was read.** Prose from `pdftotext -layout`; every equation from
     page images (110 dpi; eqs. 17–23, A5, A8–A9 and the stability line at
     220–300 dpi). A1–A4, A6–A7 and A10 were read at 110 dpi and are given
     only in words (signs checked, indices not transcribed); the argument
     order of eq. 7 was not transcribed.
   * **Recorded as printed** (reader's reading).
     - §4 (p. 156) says the FCT field solver "holds a small advantage over
       both the FCT potential solver and the constrained transport (CT)
       scheme ... in the quantitative accuracy to which the flux surfaces and
       field strengths are reproduced", but test 1 reports flux-function
       errors of 6% (FCT field) against 4% (FCT potential), and test 2 gives
       8–9% for all three. The statement holds for field strengths against
       CT, not for flux surfaces against the potential solver in test 1.
     - Eq. 25 is printed $\partial_t\mathbf A = \mathbf v\times\nabla\times\mathbf A + \mathbf s_5$
       (no gauge term).
     - p. 150 refers to "Fig. (19)" for the sums of eq. 19.
     - The stability bound and error orders of the Appendix are stated
       without derivation; the companion fluid solver (DeVore 1989, NRL
       Memorandum Report 6544) is unpublished.
   * **Reference list:** 15 entries, all merged; only ref. 6 prints a
     title. FCT III (Boris & Book, J. Comput. Phys. 20:397) is `boris-1976`
     and the NRL Memorandum 3237 `boris-1976-b`; Book, Boris & Hain (1975)
     is `book-1975`, printed with Book first (sod-1978 prints Boris first);
     Book, Boris & Zalesak's "Flux-corrected transport" chapter (Springer
     1981, p. 29) is `book-1981-b`, distinct from `book-1981` (Lecture Notes
     in Physics 141:84); Löhner et al. (Commun. Appl. Numer. Methods 4:717)
     is `lohner-1988-b`, distinct from `lohner-1988`; Zalesak's 1987
     private communication (NRL Plasma Physics Division) is not the IMACS
     linear-advection paper `zalesak-1987`; Low's two ApJ 281 papers are
     `low-1984`, `low-1984-b`. Bibliography: 3380 entries.
