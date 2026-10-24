---
type: Source
title: "Schwarz et al. (2025) — Comparison of entropy stable collocation high-order DG methods for compressible turbulent flows"
description: "Systematic comparison, in FLEXI, of entropy-stable DGSEM collocated on Gauss–Lobatto nodes (diagonal-norm SBP flux differencing) and on Gauss–Legendre nodes (generalized SBP with entropy projection) for Taylor–Green vortices and wall-resolved LES of a three-dimensional diffuser: Gauss nodes are more accurate per degree and, despite twice the cost per step, more efficient."
resource: "doi:10.1016/j.compfluid.2025.106874"
source_kind: paper
authors: [Schwarz A., Kempf D., Keim J., Kopper P., Rohde C., Beck A.]
year: 2025
venue: "Comput. Fluids 303:106874"
local_file: "/home/stefano/papers/mosaic/weno-teno/2025_Crossref_Computers_amp_Fluids_Schwarz_Comparison_of_entropy_stable_collocation_high-order_DG_metho.pdf"
tags: [dg, entropy-stable, turbulence, limiting]
timestamp: 2026-10-23T15:15:00Z
---

# Summary

Schwarz et al. (2025) compare two collocation variants of the entropy-stable
[DGSEM](/methods/dgsem.md) on curved hexahedral meshes, both implemented in
[FLEXI](/software/flexi.md). ESDGSEM-GL collocates on Legendre–Gauss–Lobatto nodes and
uses the diagonal-norm [summation-by-parts operator](/operators/summation-by-parts-operator.md)
with [flux differencing](/methods/flux-differencing.md), $(2Q\circ\mathcal F^{\mathrm{vol}})\mathbf 1$.
ESDGSEM-G collocates on Gauss–Legendre nodes, which have no boundary nodes; it uses Chan's
generalized (hybridized) SBP operator and an [entropy projection](/methods/entropy-projection.md)
of the face states: the entropy variables $w$ are interpolated to the face and mapped back to
conservative variables. Both schemes are [entropy stable](/properties/entropy-stability.md) with
Chandrashekar's two-point volume flux. The viscous terms use BR1 lifting
([Bassi–Rebay](/methods/bassi-rebay-viscous-discretization.md)), and the surface flux is Roe's
with the Harten–Hyman entropy fix (Lax–Friedrichs in the low-Mach Taylor–Green case). Time
stepping is the low-storage RK4-5 of Carpenter & Kennedy at CFL 0.9.

Gauss–Legendre quadrature with $N+1$ nodes is exact to degree $2N+1$, Gauss–Lobatto to degree
$2N-1$. Gauss–Lobatto nodes admit a larger explicit time step and need no entropy projection. A
manufactured solution converges at order $N+1$ for both, with smaller errors on Gauss nodes. On
the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at $\mathrm{Re}=1600$, at
$M_0=0.1$ ($N=7$) and $M_0=1.25$ ($N=3$), ESDGSEM-G converges faster to the reference data and
is less dissipative. In the supersonic case its shocks are sharper and less oscillatory. That
case adds a [subcell finite-volume](/methods/subcell-finite-volume-limiting.md) blending with
$\alpha\in[0.01,0.04]$. In wall-resolved LES of the ERCOFTAC three-dimensional diffuser at
$\mathrm{Re}=10\,000$, at inflow Mach numbers 0.2 and 0.7, Gauss nodes at $N=5$ match
Gauss–Lobatto nodes at $N=7$ in wall pressure. They cut the pressure-recovery error against
experiment by 37 % and remove kinks of the pressure fluctuations at element boundaries. At fixed
$N$ ESDGSEM-G costs about twice as much as ESDGSEM-GL. Because ESDGSEM-GL needs a higher degree,
and a smaller step, for the same accuracy, the authors conclude that Gauss nodes are the more
efficient choice. The evidence is numerical only; the paper proposes no new scheme.

# Version read

The archive file is arXiv:2504.00173v1 [physics.flu-dyn], 31 March 2025 (page-1 footer
"Preprint submitted to Computer and Fluids, April 2, 2025"), 41 pages (text pp. 1–33,
references pp. 33–41), all read; equations of pp. 5–10 checked on the page images. Title and
six authors match the Crossref record of the version of record (Comput. Fluids 303:106874); the
article number and DOI come from Crossref only. A footnote states that D. Kempf and A. Schwarz
share first authorship. The version of record may differ in content; every equation, section
and figure number on this page is that of arXiv v1.

# Key claims

Registry notation (see the Notation map). Page-local: $V_f$ the face-interpolation matrix
(values of $\ell_j(\pm1)$), $\mathcal F^{\mathrm{vol}}$ the contravariant two-point flux with
averaged metric terms, GL / G the Gauss–Lobatto / Gauss–Legendre variants.

1. The authors state this is the first comparison of entropy-stable DGSEM on Gauss–Lobatto and on Gauss–Legendre nodes for compressible, wall-bounded turbulent flows with separation (Abstract; §1). **Stated**
2. Gauss–Legendre collocation integrates polynomials of degree $2N+1$ exactly, Gauss–Lobatto only $2N-1$; the diagonal mass matrix is exact for Gauss–Legendre and a mass lumping for Gauss–Lobatto (§3.1). **Stated**
3. A diagonal mass matrix is necessary for the diagonal-norm SBP operator of ESDGSEM-GL (§3.1). **Stated** (cited)
4. Gauss–Lobatto nodes permit a larger explicit time step than Gauss–Legendre nodes at the same $N$ and Runge–Kutta scheme, and avoid the entropy projection, so they are cheaper per step (§3.1, §3.2). **Stated** (cited; per-step cost **Shown** in §4.4)
5. ESDGSEM-GL is the semi-discrete form (20): volume term $\sum_d(2Q\circ\mathcal F^{\mathrm{vol}}_d)\mathbf 1$ with $Q=MD$, surface terms $h-\mathcal F^{\mathrm{vol}}$ at the face nodes, and the two-point flux chosen for kinetic-energy preservation (Jameson) or entropy conservation (Tadmor), Chandrashekar's by default (§3.3, Eqs. 20–22). **Stated** (recalled)
6. ESDGSEM-G uses the generalized SBP operator (23), printed $\begin{pmatrix}2MD-V_f^\top BV_f & V_f^\top B\\ -V_fB & B\end{pmatrix}$ with $B=\mathrm{diag}(-1,1)$ (see Printed slips), with the volume term $[I\ V_f^\top](Q\circ\mathcal F^{\mathrm{vol}})\mathbf 1$ and entropy-projected face states $u(w_f)$, $w_f$ the face interpolant of $w(u)$ (§3.4, Eqs. 23–25). **Stated** (after Chan; flux-differencing equivalence cited to Mateo-Gabín et al.)
7. On the manufactured solution (27), on sinusoidally curved meshes, both variants reach order $N+1$ in $h$-convergence ($N=3$) and spectral $p$-convergence ($N=2,\dots,8$, $4^3$ elements); GL is less accurate at fixed resolution (§4.1, Fig. 1). **Shown**
8. Taylor–Green vortex, $M_0=0.1$, $\mathrm{Re}=1600$, $N=7$, $64^3$–$512^3$ degrees of freedom, LF surface flux: ESDGSEM-G converges faster to DeBonis' reference in kinetic energy and solenoidal dissipation, and agrees "far better" at $64^3$ (§4.2.1, Figs. 2–3). **Shown**
9. ESDGSEM-G takes about twice the computational time of ESDGSEM-GL on the Taylor–Green vortex (§4.2.1). **Shown** (no table)
10. Taylor–Green vortex, $M_0=1.25$, $\mathrm{Re}=1600$, $N=3$, Roe flux with Harten–Hyman fix, blending bounds $(\alpha_{\min},\alpha_{\max})=(0.01,0.04)$: G captures small scales better, is less dissipative and converges faster to Chapelier et al.; the oscillations of the dilatational dissipation at $256^3$ and $512^3$ are Gibbs oscillations, attributed to the small blending (§4.2.2, Figs. 5–7). **Shown**
11. Mach-number profiles at $t=2.5$ along $x_1=x_3=\pi$: the shock is sharper and less oscillatory under refinement on Gauss–Legendre nodes (§4.2.2, Fig. 8). **Shown**
12. Weakly compressible diffuser ($M_{D,in}=0.208$): LES-G agrees better with experiment at fixed $N$; LES-GL needs $N=7$ to approach LES-G at $N=5$ in $C_p$, and is not converged at $N=7$ (§4.3.2, Fig. 10). **Shown**
13. Pressure recovery $\Delta C_p$ (Table 1): Cherry et al. (experiment) 0.527, Miró et al. 0.500, LES-GL 0.602, LES-GL ($N=7$) 0.560, LES-G 0.574, LES-G ($N=11$) 0.542; LES-G gives "a significant error reduction of 37% compared to the experimental reference" (§4.3.2). **Shown**
14. LES-GL overestimates the log-law region of the inflow-duct velocity profile; LES-G lies closer to the log law ($\kappa_{\mathrm{vK}}=0.41$, $B_{\mathrm{log}}=5.2$) (§4.3.2, Fig. 10). **Shown**
15. LES-GL pressure fluctuations show unphysical kinks at element boundaries; LES-G is much smoother (§4.3.2, Fig. 11; §4.3.3, Fig. 13). **Shown**
16. Mean velocity and normal Reynolds stress of the weakly compressible diffuser show no G/GL trend; deviations grow along the diffuser, where the effective resolution of the structured mesh decreases (§4.3.2, Fig. 11). **Shown**
17. Compressible diffuser ($M_{D,in}=0.703$): $\Delta C_p=1.275$ (GL), $1.263$ (G), against $1.242$ for the reference LES-G at $N=7$; LES-G at $N=5$ is converged in $C_p$, LES-GL is not, even at $N=7$ (§4.3.3, Fig. 12). **Shown**
18. Differences between G and GL are larger in the compressible regime, especially in the higher statistical moments (Reynolds stresses, pressure fluctuations) (§4.3.3, §5). **Shown**
19. Cost: about a factor 2 for G against GL at fixed $N$ in all tests; compressible diffuser LES-GL 27 890 CPU-h, LES-G 62 080 CPU-h. The weakly compressible diffuser needs nearly twice the CPU time of the compressible one, because the higher Mach number allows larger time steps (§4.4). **Shown** (the hardware, HLRS "Hawk", is named in the acknowledgements only)
20. The extra cost of ESDGSEM-G comes from the entropy projection and the additional surface fluxes (§4.4, §5). **Stated**
21. LES on Gauss–Legendre nodes is the more efficient option for a given accuracy, because GL needs a higher $N$, and therefore a smaller time step, for comparable accuracy (§4.3.2, §4.4, §5). **Shown** (indirectly: no CPU time is printed for LES-GL at $N=7$)
22. The findings are contingent on the applications considered; shock / turbulent-boundary-layer interaction is proposed as future work (§5). **Stated**
23. In the finite-volume/DG blending (26), $\partial_t(Ju)=\alpha\,\partial_t(Ju)^{\mathrm{FV}}+(1-\alpha)\,\partial_t(Ju)^{\mathrm{DG}}$, only the volume term needs blending if both schemes share the interface solution. This holds trivially for first-order subcells on Gauss–Lobatto nodes; for second-order subcells or Gauss–Legendre nodes it must be enforced, by blending the surface term (Rueda-Ramírez et al.) or by zero slopes in the outer subcells (Gauss–Lobatto). The interface coefficient is $\alpha_f=\max(\alpha^-,\alpha^+)$ and the indicator a modified Persson–Peraire modal indicator on $\rho p$ (§3.5). **Stated**

*(Compiler check, not in the sources.)* From Table 1, the error against experiment is
$0.602-0.527=0.075$ for LES-GL and $0.574-0.527=0.047$ for LES-G, a reduction of 37.3 %,
consistent with claim 13. The CPU-hour ratio of claim 19 is $62\,080/27\,890=2.23$.

# Printed slips

- **Eq. (28)**: the second velocity component of the Taylor–Green initial field is printed $v_2=-v_0\cos(x_1/L)\cos(x_2/L)\cos(x_3/L)$ (checked on the page image of p. 13). *(Compiler check, not in the sources:)* with this $v_2$ the field is not divergence-free, $\partial_{x_1}v_1+\partial_{x_2}v_2=\frac{v_0}L\cos\frac{x_1}L\cos\frac{x_3}L\big(\cos\frac{x_2}L+\sin\frac{x_2}L\big)\ne0$. The other sources of the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) page, [Li et al. (2022b)](/sources/li-2022-b.md), [Takagi et al. (2022)](/sources/takagi-2022.md), [Ye et al. (2022)](/sources/ye-2022.md) and [Jain & Moin (2022)](/sources/jain-2022.md), print $v_2=-v_0\cos(x_1/L)\sin(x_2/L)\cos(x_3/L)$ (in their scalings), which makes the field solenoidal.
- §3.3: the SBP property is printed $Q+Q^\top=V_f^{\top}B$ with $Q=MD$ and $B=\mathrm{diag}(-1,1)$ (Eq. 16). *(Compiler check, not in the sources:)* $Q+Q^\top$ is $(N+1)\times(N+1)$ while $V_f^\top B$ is $(N+1)\times2$; the dimensionally consistent form is $Q+Q^\top=V_f^\top BV_f$, the $(N+1)\times(N+1)$ boundary matrix of the registry. Likewise the lower-left block $-V_fB$ of Eq. (23) is not defined for a $2\times(N+1)$ matrix $V_f$; the block that fits is $-BV_f$.
- §2.2 calls $\rho\epsilon$ the "specific internal energy". *(Compiler check, not in the sources:)* the inverse map (6) needs $\rho\epsilon=p/(\gamma-1)$, an internal energy per unit volume.
- §4.1: "$\Omega$ was discretized using $4^3$ to $32^3$ elements", while the caption of Fig. 1 says "Grid sequence ranges from $2^3$ up to $32^3$"; the domain is written "$\Omega\in[0,1]$" for the cube.
- Mach-number labels: §4.3.1 "first bulk diffuser inflow Mach number considered is $M_{D,in}=0.2$", then "$M_{in}=0.2$ or $0.45$ resulting in $M_{D,in}=0.208$ and $0.703$"; the caption of Fig. 11 gives the duct value $M_{in}=0.2$ as "diffuser inflow bulk Mach number"; §4.3.2 writes $M_{b,in}=0.2$.
- Caption of Fig. 11 (weakly compressible case, reference Miró et al.): "With no literature data available, the results are compared to a better-resolved LES (LES-G N = 7)", which contradicts the same caption and §4.3.2; the sentence matches the caption of Fig. 13.
- Figs. 11 and 13 give the profile stations as $x_1/L\in\{-2;4;8;12;15.5;18.5;21.5\}$ and $\{0;4;8;\dots\}$, while the abscissa is $x_1/h\in[0,25]$; with $L=15h$ a station $x_1/L=21.5$ would lie outside the domain (*compiler check, not in the sources:* outlet section, contraction and duct total $12.5h+10h+5h=27.5h$ beyond the diffuser exit, so the domain ends $42.5h\approx2.8L$ downstream of the diffuser inlet). The first station also differs between the captions ($-2$ against $0$).
- §4.3.3: "in contrast to the weakly compressible case, the LES-G simulation at N = 5 shows superior accuracy in comparison to LES-GL", though §4.3.2 reported the same for the weakly compressible case.
- §4 intro: "A weakly incompressible case" for the weakly compressible diffuser. Abstract "To the author's knowledge", §1 "To the authors' knowledge". Fig. 8 legend "DGSEM-GL/DGSEM-G" for ESDGSEM-GL/G.
- Reference list: [19] DOI truncated ("doi:10.1002/fld."); [56] author printed "B. V. A. N. Leer", no journal, pages "276299"; [33] no venue; [23] a URL fused with a Springer link; [12] "ArbitraryOrder", [41] "forcompressible".

# Notation map

| Schwarz et al. (arXiv v1) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $q=[\rho,\rho u,\rho e]^\top$ | $u=(\rho,\rho v,E)$ | $e$ total specific energy, so $\rho e=E$ |
| $u$ (velocity) | $v$ | **collision** with the registry state $u$ |
| $F^c$, $F^v$, $F=F^c-F^v$ | $f$, viscous flux (local) | |
| $(v,f^s)=\big(-\frac{\rho s}{\gamma-1},-\frac{\rho su}{\gamma-1}\big)$ | $(\eta,F_\eta)$ | **collision**: source $v$ is the entropy, not the velocity |
| $s=\log(p\rho^{-\gamma})$ | $s$ | agree |
| $w=\partial v/\partial q$, $\tilde w=(\gamma-1)w$ | $w$, $(\gamma-1)w$ | entropy variables; **collision** with the quadrature weights $w_i$ |
| $w_i$ | $\mathsf w_j$ | quadrature weights |
| $\rho\epsilon$ | $\rho e$ | internal energy per volume; $\epsilon$ is not the weight regularization |
| $\mathcal N$, $N$ | $N$ | polynomial degree; $N_{geo}$ geometry degree |
| $\xi$, $\ell_j$ | $\xi_j$, $\ell_j$ | reference coordinates and Lagrange basis |
| $M=\mathrm{diag}(w_i)$, $D_{ij}=\ell_j'(\xi_i)$, $Q=MD$ | $M$, $D$, $Q$ | agree |
| $B=\mathrm{diag}(-1,1)$ (Eq. 16) | $V_f^\top\mathrm{diag}(-1,1)V_f=B$ | source $B$ acts on the two face values |
| $V_f$ | $V_f$ (local) | face-interpolation matrix, $2\times(N+1)$ |
| $\mathcal J$, $J$, $\mathrm{adj}\,J$, $\mathcal M$ | $J$ (determinant), Jacobian matrix, adjugate, metric terms | registry $J$ is the Jacobian determinant |
| $\mathcal F=\mathcal M^\top F$ | contravariant flux (local) | |
| $f^*$ | $h$ | surface numerical flux (Roe with Harten–Hyman fix, or LF) |
| $f^\#$, $\mathcal F^\#$ | $f^{\mathrm{vol}}$, $\mathcal F^{\mathrm{vol}}$ | two-point volume flux; Chandrashekar's is also $f^{\mathrm{ec}}$ |
| $v_f$, $w_f=q(v_f)$ | $w_f$, $u(w_f)$ | face-interpolated entropy variables and projected face state; **collision**: source $w_f$ is a conservative state |
| $\{\{\cdot\}\}$ | $\{\!\{\cdot\}\!\}$ | arithmetic mean |
| $\alpha$, $\alpha_f$ | $\alpha$ | DG–FV blending coefficient; agree |
| $e_k$, $\epsilon_S$, $\epsilon_D$ | kinetic energy, solenoidal and dilatational dissipation (local) | $\epsilon$ is not the weight regularization |
| $M_0$, $\mathrm{Re}$ | $M$, $\mathrm{Re}$ | Taylor–Green Mach and Reynolds numbers |
| $M_{in}$, $M_{D,in}$, $M_{b,in}$ | duct and diffuser inflow bulk Mach numbers (local) | used inconsistently (Printed slips) |
| $C_p$, $\Delta C_p$ | pressure coefficient, pressure recovery (local) | $p_{ref}$ at $x_1/L=0.045$ |
| $\kappa=0.41$, $B=5.2$ | $\kappa_{\mathrm{vK}}$, $B_{\mathrm{log}}$ (local) | log-law constants; **collision** with the kinetic energy $\kappa$ and the SBP $B$ |

# Reference list

The file prints 65 references, numbered [1]–[65]. The list is merged complete into the
[bibliography](/bibliography.md), with `citedby` including `schwarz-2025`. Ref. [56] (van Leer)
has a garbled author and no journal and is keyed from its printed title and year; ref. [19] has
a truncated DOI, which is not recorded; ref. [33] has no venue. Two same-author pairs, Gassner
et al. 2016 and Chan et al. 2022, are resolved by volume and page against existing entries, not
by key. No item is unparseable.

# Pages created or updated

Chunk 9 (2026-10-23), cited further in chunk 10 (2026-10-23). This source is cited on:

* [Bassi–Rebay viscous discretizations (BR1, BR2)](/methods/bassi-rebay-viscous-discretization.md)
* [Discontinuous Galerkin spectral element method (DGSEM)](/methods/dgsem.md)
* [Entropy projection](/methods/entropy-projection.md)
* [Entropy stability](/properties/entropy-stability.md)
* [FLEXI](/software/flexi.md)
* [Flux differencing and split-form DG](/methods/flux-differencing.md)
* [Free-stream preservation](/properties/free-stream-preservation.md)
* [Kinetic energy preservation](/properties/kinetic-energy-preservation.md)
* [Method of manufactured solutions](/definitions/method-of-manufactured-solutions.md)
* [Subcell finite-volume limiting for DG](/methods/subcell-finite-volume-limiting.md)
* [Summation-by-parts operator](/operators/summation-by-parts-operator.md)
* [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
