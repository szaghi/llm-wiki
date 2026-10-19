---
type: Source
title: "Sreejith et al. (2022) — Analysis and design of a local time stepping scheme for LES acceleration in reactive and non-reactive flow simulations"
description: "LESAULTS, a domain-decomposition local time stepping method for explicit compressible LES: overlapping sub-domains advance with their own steps under frozen interface data and are merged by a Heaviside switch, with overlap widths sized by a global spectral analysis and speed-ups near 2 on vortex, cylinder-wake and flame tests."
resource: "doi:10.1016/j.jcp.2022.111580"
source_kind: paper
authors: [Sreejith N.A., Riber E., Cuenot B.]
year: 2022
venue: "J. Comput. Phys. 470:111580"
local_file: "/home/stefano/papers/mosaic/ode-integration/2022_Crossref_Journal_of_Computational_Physics_NA_Analysis_and_design_of_a_local_time_stepping_scheme_for_LES.pdf"
tags: [local-time-stepping, multirate, explicit, cfd, dispersion-analysis]
timestamp: 2026-10-20T05:00:00Z
---

# Summary

LESAULTS ("LES acceleration using local time stepping") is a
domain-decomposition [local time stepping](/methods/local-time-stepping.md)
method for explicit compressible LES solvers (AVBP). The domain is split
into overlapping sub-domains, each advanced by its own explicit one-step
scheme with its own step $h_i$. All steps divide a common macro step $H$,
so sub-domain $i$ takes $m_i=H/h_i$ sub-steps. During the sub-steps the
interface values are frozen at $t_n$ as Dirichlet data. At $t_{n+1}$ the
overlapping solutions are merged by a Heaviside-like switch at a point
$x_H$, which replaces the hyperbolic-tangent blending of the earlier
Deccoup method of Esnault et al. There is no time interpolation of
interface data and no flux correction: the method is not strictly
conservative.

A speed-up model and an optimal core distribution are derived under ideal
load balancing. The overlap width is chosen by a global spectral analysis
of the boundary-polluted amplification factor on the 1D linear convection
equation, for the Lax–Wendroff and the two-step Taylor–Galerkin (TTGC)
schemes. This gives overlaps of $m_1+m_2+1$ cells (Lax–Wendroff) and
$2(m_1+m_2)+1$ cells (TTGC). The error relative to the single-step
conventional solution is then mapped in dissipation, phase-speed and
group-velocity components. A wavepacket test confirms the map, and grid
convergence at fixed Courant number keeps the spatial orders (2 and 3).

Applications: a 2D convected vortex (an [isentropic vortex](/benchmarks/isentropic-vortex.md)
variant compared with the conventional run, not with an exact solution)
with $m=2,5,10$, speed-ups 1.92–2.21; LES of the 3D cylinder wake at
$Re=3900$ on 720 cores, speed-up 2.37 against 2.57 predicted; LES of Sandia
flame D on 360 cores, speed-up 2.05 against 2.28. Turbulence statistics
match the conventional runs. The introduction places the method in a
taxonomy of explicit local time stepping that also cites multirate
infinitesimal GARK ([multirate GARK](/methods/multirate-gark.md)) as a
fourth-order extension.

# Version read

Version of record (J. Comput. Phys. 470 (2022) 111580, Elsevier typeset),
34 pages, all read; pp. 4, 5, 8, 12, 18, 31 and 32 were checked visually.
Page 1 prints the DOI and matches Crossref in title, venue and DOI. The
byline prints the first author as "Sreejith N.A." (running head "S. N.A.").
Crossref splits the name with family "N.A." and given name "Sreejith", but
the bundle keys the source `sreejith`, the surname by which the author is
cited (the paper's own reference list cites him as "N. Sreejith", ref. [34],
and as "S. Nadakkal", ref. [41], his thesis). Equation and section numbers
on this page are those of the version of record.

# Key claims

Notation (see the notation map): $H=t_{n+1}-t_n$ the macro step (the
source's $\mathcal{LCM}(\Delta t_i)$), $h_i$ the step of sub-domain $i$,
$m_i=H/h_i$ its sub-step count (the source's $R_{\delta t,i}$); $\Delta x$
the grid spacing (the source's $h$); $\nu$ the Courant number (the source's
$N_c$); $G(\kappa\Delta x,\nu)$ the amplification factor of a fully discrete
one-step scheme, $\kappa$ the wavenumber (the source's $k$).

1. LESAULTS advances each overlapping sub-domain independently with its own explicit step; the steps divide the macro step, $m_i=H/h_i$ (§2, Table 1, Fig. 2). **Stated**
2. During the intermediate stage the interface values of each sub-domain are kept at their $t_n$ values as Dirichlet conditions (§2, p. 4). **Stated**
3. The overlapping solutions are merged by a Heaviside-like switch, $u^{n+1}=(1-\mathrm H(x-x_H))\,u_1^{n+1}+\mathrm H(x-x_H)\,u_2^{n+1}$ at coincident overlap nodes (Eq. (4)), instead of the tanh blending of Esnault et al., which the authors judge unsuited to multi-dimensional, complex overlaps (§4, p. 7). **Stated**, and **Shown** accurate by the tests
4. Under ideal load balancing the theoretical speed-up is $S_{\mathrm{th}}=\max_i(m_i)\big(\sum_iN_i-\frac12\sum_j\sum_iN_{ij}\big)/\sum_im_iN_i$ (Eq. (1)), with $N_i$ the node counts and $N_{ij}$ the overlap node counts. **Derived**
5. The load-balancing core count is $C_i=m_iN_iC_{tot}/\sum_im_iN_i$ (Eq. (2)). **Derived**
6. For two sub-domains, overlap neglected and $m_1=1$, $S_{\mathrm{th}}=m(R_n+1)/(R_n+m)$ with $R_n=N_1/N_2$ (Eq. (3), Fig. 3); local time stepping pays off when very few cells set the limiting step. **Derived**
7. The method needs a priori knowledge of the steps of all sub-domains (§3, p. 5). **Stated**
8. The boundary-induced error of the frozen interface is maximal at the boundary node and decays inward; for Lax–Wendroff it vanishes identically beyond node $m+1$ because the stencil is local; for $m=2$ node 2 has maximal error 0.005 (Figs. 7–8, §4; $\nu=0.1$, $\Delta x=0.01$, 101 nodes). **Shown**
9. For TTGC (P1 mass matrix, "spatially implicit") the boundary error never vanishes exactly; at node 6 it is $O(10^{-7})$ for $m=2$; rule of thumb: node $2m+1$ (Figs. 7(b), 8, §4). **Shown**
10. Overlap width: $m_1+m_2+1$ cells for Lax–Wendroff and $2(m_1+m_2)+1$ for TTGC, with penetration depths $(m_2+1)\Delta x$ and $(2m_2+1)\Delta x$ (§4, p. 9). **Shown** (heuristic from the spectral analysis; the TTGC rule is stated for $\nu=0.1$ and "could differ" at higher $\nu$)
11. In the sub-domain whose Courant number equals the conventional one, the LESAULTS error with respect to the conventional solution is identically zero upstream of $x_H$ (Eqs. (23)–(24), §5.1). **Derived**
12. In the large-step sub-domain the error is $\int\big[G(\kappa\Delta x,m\nu)-G(\kappa\Delta x,\nu)^m\big]\hat U e^{i\kappa x_q}d\kappa\ne0$, decomposed into dissipation $\epsilon_G$, phase-speed $\epsilon_{CN}$ and group-velocity $\epsilon_{Vgn}$ errors (Eqs. (25)–(28), §5.1). **Derived**
13. With $m=2$, Lax–Wendroff keeps $\epsilon_G<1\%$ for all $\kappa\Delta x$ up to $\nu=0.1$, TTGC up to $\nu=0.25$; for any $\nu$, Lax–Wendroff is accurate for $\kappa\Delta x<0.5$ and TTGC for $\kappa\Delta x<0.75$; the accurate regions shrink as $m$ grows (Fig. 11, §5.2). **Shown**
14. Group velocity: Lax–Wendroff is accurate for all $\kappa\Delta x$ when $\nu<0.1$, TTGC up to $\nu=0.2$; any stable $\nu$ resolves $\kappa\Delta x<0.2$ (Lax–Wendroff) and $\kappa\Delta x<0.3$ (TTGC) (Fig. 12, §5.2). **Shown**
15. Recommendation: keep the Courant number of the larger-step sub-domain below 0.1 (Lax–Wendroff) or 0.25 (TTGC) when high-frequency content crosses the overlap (§5.2, p. 13). **Stated** (from the spectral maps)
16. Wavepacket test, $m_2=10$ (Table 2): Lax–Wendroff with $\nu=0.5/0.05$ gives $\epsilon_G=2.9\times10^{-3}$, $\epsilon_{Vgn}=3.28\times10^{-2}$, and with $0.05/0.005$ gives $1.7\times10^{-5}$, $3.35\times10^{-4}$; TTGC gives $8.1\times10^{-4}$, $1.45\times10^{-2}$ and $2.8\times10^{-8}$, $9.37\times10^{-7}$; the solutions at $t=2$ follow the predicted ordering (§5.3, Fig. 13). **Shown**
17. Spatial order is preserved: the maximum-norm errors decay with order 2 (Lax–Wendroff) and 3 (TTGC) for $\Delta x=0.1,\dots,10^{-4}$ with $\nu_1=\nu_3=0.1$, $m_2=10$, like the conventional solver (Fig. 15, §5.4). **Shown** (with $h\propto\Delta x$; temporal order of the coupling is not tested separately)
18. LESAULTS is not strictly conservative; the conservation error equals the boundary-value mismatch, which in spectral space equals $\epsilon_G$, small at low $\kappa\Delta x$ and $\nu$ (Eqs. (31)–(33), §5.5). **Derived** (informal; it assumes a vanishing overlap integral "under steady state conditions")
19. 2D vortex: the errors relative to the conventional run are of the same order on uniform and stretched meshes, lower for quadrilaterals than triangles, lower for TTGC than Lax–Wendroff, and grow with $m$ (Fig. 18, §6.1.1–6.1.2). **Shown**
20. 2D vortex speed-ups for $m=10$, uniform meshes ($S_{\mathrm{th}}/S_{\mathrm{act}}/$efficiency): 2.25/2.21/98 % (quad, Lax–Wendroff), 2.09/1.92/92 % (quad, TTGC), 2.39/2.21/92 % (tri, Lax–Wendroff), 2.31/2.09/90 % (tri, TTGC), overlap nodes neglected in $S_{\mathrm{th}}$ (Table 4, §6.1.3). **Shown**
21. 3D cylinder LES at $Re=3900$ (Lax–Wendroff, Sigma subgrid model, hexahedra): conventional run 3,704,760 nodes at $h=2\times10^{-7}$ s; sub-domains of 900,360 nodes at $2\times10^{-7}$ s and 2,922,480 nodes at $10^{-6}$ s ($m=5$); on 720 Haswell cores $S_{\mathrm{th}}=2.57$, $S_{\mathrm{act}}=2.37$, efficiency 92 % (Tables 5–6, §6.2.1). **Shown**
22. Cylinder mean velocities and resolved Reynolds stresses of LESAULTS match the conventional LES closely, and both deviate from experiment in similar ways (Figs. 20–24, §6.2.2). **Shown**
23. Sandia flame D LES (Lax–Wendroff, artificial viscosity, Sigma model, 2-step 6-species CH$_4$ mechanism, tetrahedra): $h=10^{-7}$ s and $4\times10^{-7}$ s ($m=4$), overlap of 6 cells, 360 cores split 202/158; $S_{\mathrm{th}}=2.28$, $S_{\mathrm{act}}=2.05$, efficiency 90 % (Table 7, §6.3). **Shown**
24. Flame D mean and rms profiles of temperature, mixture fraction, CH$_4$, CO and CO$_2$ match the conventional LES at $x/d=1,15,45$ (Figs. 26–28, §6.3.2). **Shown**
25. Implicit schemes rarely achieve their theoretical unconditional stability in LES (Choi and Moin: cell Courant number limited to 2–3), have poorer resolution than explicit ones, and IMEX interfaces can act as sources of spurious wave packets (§1). **Stated** (cited)
26. Multirate and AMR schemes are "often limited to structured block grids", whereas domain-decomposition local time stepping applies to unstructured grids (§1, p. 3). **Stated**

*(Reader caveats, not in the source.)* Freezing interface values at $t_n$
over all sub-steps is a zeroth-order-in-time coupling; the order test of
claim 17 holds $h\propto\Delta x$ with an overlap that grows with $m$, so it
shows spatial order at fixed Courant number only. Claim 26 overlooks
unstructured-grid multirate and local time stepping methods, including
works the paper itself cites. The introduction's attribution of Knoth and
Wolke (1998) and of Sandu's MRI-GARK (2019) as third- and fourth-order
extensions of multirate local time stepping is loose.

# Printed slips

1. §2, p. 4: "The overlapped zones between the sub-domains are named as OZ12 and OZ13 such that $OZ12=D1\cap D2$ and $OZ23=D2\cap D3$", and "be $N_{12}$ and $N_{13}$" — OZ13 and $N_{13}$ should be OZ23 and $N_{23}$.
2. Eqs. (23)–(24): "$\epsilon_p={}_1u_p^{n+1}-{}_cu_i^{n+1}$" with $e^{ikx_i}$ — node index $i$ in place of the coincident node $p$.
3. §5.5, p. 18: after Eq. (33) the text says "Hence the error in conservation is given by $({}_2u_{N1}-{}_cu_j)$" — it should be ${}_1u_{N_1}$; the claim "it is proven in Section 5.1 that ${}_2u_1={}_cu_i$" assigns to sub-domain 2 the zero-error result §5.1 proves for the sub-domain at the conventional Courant number.
4. §5.2, p. 14: in the discussion of the group-velocity error (Fig. 12) the text says "the phase speed is captured accurately for all wavenumbers for $N_c<0.1$" — phase speed for group velocity.
5. §5.3, p. 16: "the dissipation error of TTGC scheme is half that of the LW scheme" — Table 2 gives $8.1\times10^{-4}$ against $2.9\times10^{-3}$, a ratio of about 0.28.
6. Table 4, Case 4 (tri, TTGC): the node counts $N_1=50125$, $N_2=N_3=40501$ repeat Case 1, for which Eq. (1) gives 2.25, yet $S_{\mathrm{th}}=2.31$ is printed; Cases 1–3 check. The counts of Case 4 look copied from Case 1.
7. Table 7 (Sandia D): $m=4$, $N_1=240738$, $N_2=940311$ give $4\cdot1181049/(4\cdot240738+940311)=2.48$, not the printed $S_{\mathrm{th}}=2.28$ (which would need about 96,000 overlap nodes subtracted, not printed); the core split 202/158 disagrees with Eq. (2), which gives about 182 cores for the first sub-domain. Table 6 (cylinder) checks.
8. Eq. (30): $\mathrm{Error}_{inf}=\max(u-u_{exact})/\max(u_{exact})$ printed without absolute values.
9. §6.2.2: "The PIV measurements of Laurenco and Shih [52]" — ref. [52] is Kravchenko and Moin (2000); the Lourenco–Shih data are not in the reference list.
10. §6.2: "transitionally periodic" for translationally periodic.
11. Refs. [41] and [57] carry garbled French ("dirigae", "thee de doctorat dirigage", "eschelles", "prolongee"); ref. [33] mixes a Fifth MIT Conference paper with "Comput. Struct. 87 (2009)".

The reader verified Eq. (A.15) by differentiating (A.14), and Eq. (A.21)
by substituting (A.17)–(A.20).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathcal{LCM}(\Delta t_i)=t^{n+1}-t^n$ | $H$ | macro step; multirate convention of the registry |
| $\Delta t_i$ | $h_i$ | step of sub-domain $i$ |
| $R_{\delta t,i}$, $R_{\delta t}$ | $m_i$, $m$ | sub-step count, the multirate ratio |
| **$h$** | $\Delta x$ | grid spacing; **collides** with the registry step |
| $N_c=c\Delta t/h$ | $\nu$ | Courant number |
| **$k$**, $kh$ | $\kappa$, $\kappa\Delta x$ | wavenumber; **$k$ collides** with the multistep step count |
| $G_{int}$, $G_{int}^{R_{\delta t}}$, ${}_2G_i^{R}$ | $G$, $G^m$, kept | amplification factor of a fully discrete one-step scheme, the space–time analogue of the [stability function](/definitions/stability-function.md) |
| $\epsilon_G$, $\epsilon_{CN}$, $\epsilon_{Vgn}$ | kept | dissipation, phase-speed and group-velocity errors relative to the conventional solver |
| $\epsilon_{bnd,i}$ | kept | frozen-boundary error at node $i$ |
| $H(x-x_H)$ | $\mathrm H(x-x_H)$ | Heaviside-like switch; roman to avoid the macro step $H$ |
| **$[A]$**, $[B]$, $[C]$ | kept (page-local) | scheme matrices, $[C]=[A]^{-1}[B]$; **$[A]$ is not** the Butcher matrix ($[A]=I$ for Lax–Wendroff, P1 mass matrix for TTGC) |
| **$\beta$**, $\theta$ | kept | numerical phase angle and $\arg G$; **$\beta$ collides** with the PID and multistep $\beta$ |
| $\alpha_{TTGC}$, $\beta_{TTGC}$, $\gamma_{TTGC}$ | kept | TTGC constants; not Shu–Osher or Rosenbrock coefficients |
| $S_{th}$, $S_{act}$, $\eta_{LESAULTS}$ | $S_{\mathrm{th}}$, $S_{\mathrm{act}}$, efficiency | **$\eta$ collides** with the registry entropy |
| $N_i$, $N_{ij}$, $R_n$, $C_i$, $C_{tot}$ | kept | node and core counts |
| $c$ | kept | advection speed of $u_t+cu_x=0$; not the abscissae |

# Reference list

57 printed references, numbered [1]–[57]. The list is merged complete into
the [bibliography](/bibliography.md) with `citedby` sreejith-2022. Ref. [2]
prints a DOI and a ScienceDirect URL; [17] and [29] are AIAA conference
papers with sparse data; [33] mixes proceedings and journal data; [41] is
the first author's thesis under the name "S. Nadakkal" and [34] lists him
as "N. Sreejith"; [50] is a 1997 technical report without institution;
[56] prints a proceedings preface before C. R. Mécanique 341. Same-key
works take suffixes in printed order: Sengupta et al. 2013 ([34], [44]),
Sengupta et al. 2020 ([38], [40]), Colin 2000 ([43], and the thesis [57]).
There are no printed duplicates and no unparseable items.

# Pages created or updated

Chunk 4 (2026-10-20). This source is cited on:

* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Local time stepping](/methods/local-time-stepping.md)
* [Multirate GARK methods (MrGARK, compound-fast, multirate backward Euler)](/methods/multirate-gark.md)
