---
type: Source
title: "Rueda-Ramírez et al. (2021) — An entropy stable nodal discontinuous Galerkin method for the resistive MHD equations. Part II: Subcell finite volume shock capturing"
description: "Entropy-stable shock capturing for the split-form LGL DGSEM of resistive GLM-MHD: element-wise blending with a native subcell finite-volume scheme extended to non-conservative terms, a blending lemma preserving entropy stability, a second-order TVD-ES subcell scheme with the sign property, and tests up to Io's plasma interaction."
resource: "doi:10.1016/j.jcp.2021.110580"
source_kind: paper
authors: [Rueda-Ramírez A.M., Hennemann S., Hindenlang F.J., Winters A.R., Gassner G.J.]
year: 2021
venue: "J. Comput. Phys. 444:110580"
local_file: "/home/stefano/papers/mosaic/weno-teno/2021_Crossref_Journal_of_Computational_Physics_Rueda-Ramírez_An_entropy_stable_nodal_discontinuous_Galerkin_method_for_th.pdf"
tags: [dg, limiting, entropy-stable, mhd, non-conservative-systems]
timestamp: 2026-10-22T12:00:00Z
---

# Summary

Part I of the series (Bohm et al.) built an entropy-stable
[flux-differencing](/methods/flux-differencing.md) [DGSEM](/methods/dgsem.md)
on Legendre–Gauss–Lobatto nodes for the resistive GLM-MHD equations, whose
Powell and GLM non-conservative terms are needed for the entropy analysis and
whose cleaning field $\psi_{\mathrm{GLM}}$ controls the
[divergence of the magnetic field](/properties/divergence-free-magnetic-field.md).
[Entropy stability](/properties/entropy-stability.md) assumes positive density
and pressure, so that scheme still crashes at strong shocks. This paper adds
shock capturing that keeps the entropy proof intact.

First, the [subcell finite-volume blending](/methods/subcell-finite-volume-limiting.md)
of Hennemann et al. is extended to systems with non-conservative terms. Each
element blends the split-form DGSEM with a first-order finite-volume scheme on
the LGL subcells through one coefficient $\alpha\in[0,1]$; only the advective
and non-conservative parts are blended, and the visco-resistive terms stay
DGSEM with BR1. A blending lemma shows that if both schemes share the
element-boundary terms, the entropy balance is the $\alpha$-convex combination
of their interior productions, so the blend is entropy conservative or stable
whenever both parts are; the proofs, built on
[summation-by-parts](/operators/summation-by-parts-operator.md) identities, cover
3D curvilinear meshes. Second, a "TVD-ES" subcell scheme adapts the second-order
[TeCNO](/methods/tecno-scheme.md)-type scheme of Fjordholm–Mishra–Tadmor: an
[entropy-conservative flux](/methods/entropy-conservative-flux.md) on the subcell
means plus entropy-variable dissipation acting on minmod-reconstructed
([TVD](/definitions/total-variation-diminishing.md)) jumps with the sign
property, on the non-uniform LGL subcells and with no extra MPI communication.
The default dissipation is an entropy-stable form of the
[Rusanov flux](/methods/lax-friedrichs-flux.md). A Persson–Peraire modal
[indicator](/definitions/troubled-cell-indicator.md) drives $\alpha$; the
paper criticizes [artificial viscosity](/methods/artificial-viscosity.md) and
cites [convex limiting](/methods/convex-limiting.md) as related subcell work.

All runs use [FLUXO](/software/fluxo.md) with
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md) (five stages, fourth order).
[Free-stream preservation](/properties/free-stream-preservation.md) holds with
random $\alpha$ on a heavily warped 3D mesh; on a weak magnetic blast
([MHD blast wave](/benchmarks/mhd-blast-wave.md)) the entropy error of the EC
scheme falls at fourth order in the time step. The
[Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) converges towards Athena
results, the GEM reconnection challenge runs where the unblended scheme
crashes, and a 3D simulation of Io's interaction with the Jovian plasma torus
(20.7 million DOFs) is compared with Galileo magnetometer data.

# Version read

arXiv preprint 2012.12040v1 [math.NA], 22 Dec 2020 ("Preprint submitted to
Elsevier"), not the version of record; 47 PDF pages (a highlights page plus 46
numbered pages: main text pp. 1–32, references, appendices A–C pp. 35–46), all
read, printed pp. 10–16 and 35–36 read visually to recover the dissipation
matrices. Title (printed in title case) and the five authors in this order
match Crossref; venue and DOI come from Crossref. Section, equation, lemma and
reference numbers cited here are those of the arXiv v1.

# Key claims

Registry notation (see the notation map): entropy $\eta$ with flux $F_\eta$,
entropy variables $w$ (the source's $\mathbf v$), velocity $v$, flux potential
$\psi$ (the source's $\Psi$, including the $\theta B$ term), GLM field
$\psi_{\mathrm{GLM}}$, volume and surface two-point fluxes $f^{\mathrm{vol}}$
and $h$, LGL weights $\mathsf w_j$; the scaled entropy variables
$\underline{\mathbf R}^T\mathbf v$ are $\tilde w=R^\top w$ (the TeCNO page's $\tilde w$ up to the diagonal scaling $\mathcal Z^{1/2}$, which keeps signs).

1. The resistive GLM-MHD system of Derigs et al. needs the Powell term and the GLM Galilean-invariance term for the continuous entropy analysis; these need a special discrete treatment (§2.2, Eqs. 13–15). **Stated**
2. Entropy stability of the DGSEM does not give nonlinear stability: the entropy analysis assumes positive density and pressure, which high-order oscillations at strong shocks can violate (§1). **Stated**
3. The hybrid scheme blends only the advective and non-conservative terms, $J\mathsf w_j\,\dot u_j=(1-\alpha)F^{a,\mathrm{DG}}_j+\alpha F^{a,\mathrm{FV}}_j-F^{\nu,\mathrm{DG}}_j$, with element-local $\alpha$; keeping the diffusive terms pure DGSEM is justified because physical diffusion adds dissipation at the large gradients near shocks (§3, Eq. 28). **Stated** (modelling choice)
4. Lemma 1: the native LGL finite-volume scheme (44) has the cell entropy balance $J\mathsf w_j\dot\eta_j=\hat F_{\eta,(j,j-1)}-\hat F_{\eta,(j,j+1)}+\tfrac12(r_{(j-1,j)}+r_{(j,j+1)})$, with numerical entropy flux (54) and interface entropy production (55) (§3.3.1, Eq. 56; proof App. B.1). **Proved**
5. With the EC flux of Derigs et al. as finite-volume flux, the first-order scheme is semi-discretely entropy conservative "by construction and is virtually dissipation free" (§3.3.1). **Stated** (it follows from the generalized Tadmor condition (51))
6. Lax–Friedrichs dissipation on the conservative jump (52) is not entropy stable for MHD; writing $[\![u]\!]\approx\mathcal H[\![w]\!]$, $\mathcal H=\partial u/\partial w$, gives the ES flux (57) with production $r=-\tfrac12[\![w]\!]^\top D_w[\![w]\!]\le0$, where $D_w=R\lvert\Lambda\rvert\mathcal ZR^\top$ is symmetric positive definite by Barth's scaling $\mathcal H=R\mathcal ZR^\top$ (§3.3.1, Eqs. 52–60). **Derived**
7. Lemma 2: the split-form DGSEM has the element entropy balance $\sum_j\mathsf w_jJ\dot\eta_j=\hat F_{\eta,(0,L)}-\hat F_{\eta,(N,R)}+\tfrac12(r_{(L,0)}+r_{(N,R)})+\sum_{j,k}Q_{jk}r_{(j,k)}+r^\nu$, $r^\nu\le0$ (§3.3.2, Eq. 61; proof App. B.2). **Proved**
8. An entropy-stable (dissipative) flux used as the DGSEM volume flux gives an "unpredictable" entropy balance, because $Q_{jk}$ has entries of both signs; entropy stability needs an EC volume flux and an ES surface flux (§3.3.2). **Derived**
9. Lemma 3 (blending lemma): if two schemes have the form (63), identical element-boundary terms plus arbitrary interior terms, the blend (62) has the entropy balance $\dot\eta_{\partial K}+(1-\alpha)\dot\eta^{\mathrm{DG}}_K+\alpha\dot\eta^{\mathrm{FV}}_K$; it is EC if both parts are EC, for any element-wise $\alpha$, and ES if one part is ES and the other EC or ES (§3.3.3, Eqs. 62–69). **Proved**
10. The hybrid scheme (70) has the balance (71), whose interior terms are $(1-\alpha)\sum_{j,k}Q_{jk}r^{\mathrm{DG}}_{(j,k)}+\alpha\sum_{j=0}^{N-1}r^{\mathrm{FV}}_{(j,j+1)}+r^\nu$; the DG volume flux, the interior FV flux and the surface flux can be chosen independently (§3.3.3). **Proved**
11. A first-order finite-volume scheme on the non-uniform LGL subcells imprints the mesh on the solution, which motivates reconstruction (§4, Fig. 6). **Shown**
12. TVD-ES flux (72): $f^{\mathrm{ec}}(u_L,u_R)-\tfrac12D_w\langle\!\langle w\rangle\!\rangle_{(L,R)}$, with the EC part on the subcell means; it is entropy stable if $\langle\!\langle\tilde w\rangle\!\rangle=\mathcal B[\![\tilde w]\!]$ with diagonal $\mathcal B>0$ (the sign property), with production $r=-\tfrac12[\![w]\!]^\top R\lvert\Lambda\rvert\mathcal Z\mathcal BR^\top[\![w]\!]\le0$ (§4, Eqs. 72–75). **Derived**
13. Minmod is the only symmetric TVD limiter with the sign property (§4). **Stated** (cited from Fjordholm et al.)
14. The EC flux is second-order accurate if and only if the mesh is regular (Winters–Gassner); the LGL subcell mesh is irregular, but the reconstructed dissipation still reduces mesh imprinting (§4). **Stated** (citation) / **Shown** (Fig. 6)
15. The boundary-subcell reconstruction (80) needs only the DGSEM connectivity, so TVD-ES "can be implemented in a DGSEM code by only replacing the volume integral and without any additional MPI communication" (§4). **Stated**
16. Blending map: $\tilde\alpha=1/\big(1+\exp(-\tfrac{s}{\mathbb T}(\mathbb E-\mathbb T))\big)$, $s=9.21024$, $\mathbb T(N)=0.5\cdot10^{-1.8(N+1)^{0.25}}$, clipped with $\alpha_{\min}=0.01$ and $\alpha_{\max}=1$; time relaxation $\alpha^{i+1}=\max\{\alpha^{i+1},0.7\alpha^i\}$ and two spatial sweeps $\alpha=\max\{\alpha,0.7\alpha_E\}$ (§5, Eqs. 84–88). **Stated**
17. A plain modal indicator switches on and off with the position of a moving shock relative to element boundaries, which motivates the time relaxation (§5). **Stated** (not shown)
18. Free-stream preservation holds with random element-wise $\alpha$ redrawn at every stage on a heavily warped 3D mesh ($N=4$, CFL 0.1): $\lVert\partial_tu\rVert_{L^2}\sim10^{-13}$–$10^{-12}$ at $t=0$, and at $t=1$ the deviation is about $10^{-13}$ (EC) and $10^{-14}$–$10^{-15}$ (ES, TVD-ES) (§6.1, Table 1). **Shown**
19. On a weak magnetic blast on the warped mesh, the total entropy change $1-\eta_\Omega(1)/\eta_\Omega(0)$ of the EC scheme converges to zero at fourth order in the time step (CFL 0.4 to 0.025), down to machine precision, for $N=4$ and $6$; the ES and TVD-ES schemes dissipate entropy (§6.1, Fig. 5). **Shown**
20. Orszag–Tang with pure FV ($\alpha=1$, $256^2$ DOFs, $N=7$): TVD-ES has higher resolution and fewer artefacts than first-order FV; of three boundary-subcell variants, no boundary reconstruction gives the best result and is used from then on (§6.2, Fig. 6). **Shown**
21. On Orszag–Tang the blended TVD-ES scheme (indicator on $p$) converges towards the Athena solution (second-order FV, constrained transport, Rusanov) as resolution grows; $N=7$ captures some features better than $N=3$ and needs smaller $\alpha$ (§6.2, Figs. 7–10). **Shown**
22. The total entropy stays constant while the Orszag–Tang solution is smooth and decreases once shocks form; in the resistive GEM case it decreases monotonically from $t=0$, faster for larger resistivity (§6.2–6.3, Figs. 11, 15). **Shown**
23. GEM reconnection challenge: the ES-DGSEM without finite-volume stabilization crashes from loss of positivity; with the indicator on $\rho p$ and little blending the runs complete to $t=100$ (§6.3). **Shown**
24. At equal DOFs $N=3$ gives higher reconnection rates than $N=7$, attributed to higher numerical resistivity; for $\mu_R=5\times10^{-3}$ the reconnected flux follows Birn et al. (2001) for $t\le40$ but is "slightly less resistive" (§6.3, Fig. 14). **Shown**
25. Io–plasma torus: on 165,888 curvilinear hexahedra ($N_{geo}=2$, $N=4$, 20.736 million DOFs) TVD-ES runs to $t=10$ with little blending, mostly in Io's atmosphere; the field along the I31 flyby matches some features of the Galileo data after shifting $B_1$ by $+240$ nT and $B_2$ by $-700$ nT (§6.4, Figs. 17–19). **Shown**
26. Bohm showed that an entropy-stable DG for ideal MHD loses positivity on the Io problem and needed artificial dissipation; the hybrid scheme is "robust enough" for it (§6.4). **Stated** / **Shown**
27. The methods apply to "any hyperbolic-parabolic symmetrizable system with non-conservative terms" (§1, §7). **Stated**
28. The methods are entropy stable on 3D unstructured curvilinear meshes provided the discrete metric identities hold and the Hennemann subcell metrics (150) make the subcell finite volumes watertight (App. C, Lemmas 4–6). **Proved**

# Printed slips

- Eq. (41): "$J\omega_j\dot{\mathbf u}^{FV}_j=\hat{\mathbf f}^a_{(j,j-1)}-\hat{\mathbf f}^a_{(j,j+1)}-J\omega_j\boldsymbol\Upsilon_{1,j}=\mathbf 0$"; the trailing "$=\mathbf 0$" is spurious.
- Eq. (86): the middle case reads "$\tilde\alpha$ if $\tilde\alpha_{\min}\le\alpha\le\alpha_{\max}$" for $\alpha_{\min}\le\tilde\alpha\le\alpha_{\max}$.
- §4, p. 14: "Using Definition 55" for Definition 2 / Eq. (55).
- §6.2, p. 21: the Fig. 6 variants are lettered (b), (c), (c); the last should be (d).
- Eq. (105), App. B.1: the final line ends with "$\tfrac12(r_{(j-1,j)}+r_{(N,R)})$" instead of $r_{(j,j+1)}$, as in Lemma 1, Eq. (56).
- App. B.2: Eq. (125) carries "$-\sum Q_{jk}r_{(j,k)}$" while Eq. (126) and Lemma 2 (61) carry "$+\sum Q_{jk}r_{(j,k)}$"; Eq. (123) reads "$Q_{jk}(\Psi_j-\Psi_k-r_{(j,k)})$".
- Eqs. (79) and (80): $\Theta^l_N$ is printed with $\mathbf w^l_0-\mathbf w^l_{N-1}$, which by symmetry with $\Theta^l_0$ should be $\mathbf w^l_N-\mathbf w^l_{N-1}$; the "central slope" (79) is a one-sided difference.
- Lemma 4 (App. C.1.2): the element sum is printed "$\sum_{i=0}^N$" with a stray "$=+$" for a 3D sum.
- §6 says the EC flux is used "for consistency" as "the same numerical flux in the FV method for the element boundaries and the element interior, $\hat{\mathbf f}^a=\hat{\mathbf f}^{a,FV}$"; which flux is used at the FV interfaces is not stated unambiguously.
- §6.4: "[67, 67, 66]", "iteractions" (p. 28), "sub-Alvénic".
- References: [8] (Part I) is printed "Journal of Computational Physics 1 (2018) 1–35"; [1] repeats "B. van Leer, M. Visbal"; [54] repeats its authors; [55] lists three authors for a PhD thesis.

# Notation map

| Rueda-Ramírez et al. (2021) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf u=(\rho,\rho\vec v,\rho E,\vec B,\psi)$ | $(\rho,\rho v,E,B,\psi_{\mathrm{GLM}})$ | the source's $E$ is specific; $\psi$ is the GLM field |
| $\vec v$ | $v$ | velocity |
| $\overleftrightarrow{\mathbf f}^a$, $\overleftrightarrow{\mathbf f}^\nu$ | $f^{(d)}$, kept | advective and visco-resistive fluxes |
| $\boldsymbol\Upsilon^{MHD}$, $\boldsymbol\Upsilon^{GLM}$, $\boldsymbol\phi^{MHD}$, $\boldsymbol\phi^{GLM}$ | kept | Powell and GLM non-conservative terms and coefficient vectors |
| $\boldsymbol\Phi^\diamond_{(j,k)}$, $\boldsymbol\Phi^*_{(j,k)}$ | kept | surface and volume numerical non-conservative terms, $\boldsymbol\Phi^*=2\boldsymbol\Phi^\diamond-\boldsymbol\Phi_j$ |
| $\mathbf f^*_{(j,k)}$ | $f^{\mathrm{vol}}$ | symmetric volume flux |
| $\hat{\mathbf f}^a_{(i,j)}$, $\hat{\mathbf f}^{a,FV}$ | $h$, kept | surface flux; interior subcell flux |
| $\mathbf f^{EC}$, $\mathbf f^{ES}$, $\mathbf f^{TVD-ES}$ | $f^{\mathrm{ec}}$, kept | entropy-conservative, entropy-stable and TVD-ES fluxes |
| $S=-\rho s/(\gamma-1)$, $\vec f^S$ | $\eta$, $F_\eta$ | mathematical entropy and flux; $s=\ln(p\rho^{-\gamma})$ agrees |
| $\mathbf v$ | $w$ | entropy variables; **$\mathbf v$ is not the velocity** |
| $\vec\Psi$, $\theta=2\beta\vec v\cdot\vec B$ | $\psi$, kept | flux potential including $\theta B$; **$\theta$ is the limiter factor in the registry** |
| $\beta=\rho/(2p)$ | kept | **collides with $\beta_k$** |
| $\mathbf w=\underline{\mathbf R}^T\mathbf v$ | $\tilde w=R^\top w$ | scaled entropy variables |
| $\hat f^S_{(j,k)}$, $r_{(j,k)}$ | $\hat F_{\eta,(j,k)}$, $r_{(j,k)}$ | numerical entropy flux, interface entropy production; **$r$ collides with the WENO stencil size** |
| $\dot S_{\partial K}$, $\dot S^i_K$, $r^\nu$ | $\dot\eta_{\partial K}$, $\dot\eta^i_K$, $r^\nu$ | boundary, interior and diffusive entropy production |
| $[\![a]\!]_{(L,R)}=a_R-a_L$ | $[\![a]\!]$ | agrees |
| $\{\!\{a\}\!\}$, $a^{\ln}$ | $\{\!\{a\}\!\}$, $\{\!\{a\}\!\}_{\log}$ | arithmetic and logarithmic means |
| $\langle\!\langle\mathbf v\rangle\!\rangle$ | $\langle\!\langle w\rangle\!\rangle$ | jump of the reconstructed entropy variables |
| $\underline D$, $\underline D^{\mathbf v}$ | $D_u$, $D_w$ (local) | dissipation matrices on $[\![u]\!]$ and $[\![w]\!]$; **$D$ is the differentiation matrix in the registry** |
| $\underline{\mathbf R}$, $\underline{\boldsymbol\Lambda}$ | $R$, $\Lambda$ | eigenvectors and eigenvalues at a mean state |
| $\underline{\mathcal H}$, $\underline{\mathcal Z}$ | $\mathcal H$, $\mathcal Z$ (local) | entropy Jacobian and Barth scaling, as on the TeCNO page |
| $\underline{\mathbf B}^{ES}$ | $\mathcal B$ (local) | diagonal reconstruction matrix, as on the TeCNO page; the source letter collides with the SBP boundary matrix $B$ and the magnetic field |
| $\Theta^l_j$, MINMOD | kept | subcell slopes and minmod; **$\Theta$ collides with the WENO-ZN term of registry §10** |
| $N$, $\xi_j$, $\omega_j$ | $N$, $\xi_j$, $\mathsf w_j$ | DG degree, LGL nodes and weights |
| $Q_{jk}=\omega_jD_{jk}$, $\mathbf B$ | $Q$, $B$ | SBP matrices; agree |
| $J$, $J\vec a^d$, $\tilde{\vec n}$ | $J$, $Ja^{(d)}$, kept | metric terms; Hennemann subcell normals |
| $\alpha$ | $\alpha$ | blending coefficient, 0 pure DG, 1 pure FV; agrees |
| $\epsilon$, $\mathbb E$, $\mathbb T$, $s$ | kept | indicator quantity, modal energy, threshold, sharpness; **$\epsilon$ collides with the WENO regularization, $s$ with the specific entropy** |
| $c_h$, $\mu_0$, $\mu_R$, $\mu_{NS}$ | kept | cleaning speed, permeability, resistivity, viscosity |
| CFL | $\nu$ | 0.5 in the runs, with the time-step formula (89) |

# Reference list

72 printed references in numbered Elsevier style ([1]–[72]), all parsed and
merged complete into the [bibliography](/bibliography.md) with `citedby`
`ruedaramirez-2021`. [19] prints no year (keyed with the citing year), [17] no
venue, [25] and [29] no volume; [23] and [26] are arXiv preprints and [53]
prints "In Press (2020)"; [63] is garbled ("Jupiter: The Planet m (2003)"),
[64] gives only a title and year, [65] is a NASA PDS dataset; [8] prints the
implausible volume 1. All are kept as printed with notes. No printed
duplicates.

# Pages created or updated

Chunk 2 (2026-10-22), cited further in chunks 3–8 (2026-10-22/23). This source is cited on:

* [Artificial viscosity and spectral viscosity](/methods/artificial-viscosity.md)
* [Discontinuous Galerkin spectral element method (DGSEM)](/methods/dgsem.md)
* [Divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
* [Entropy stability](/properties/entropy-stability.md)
* [Entropy-conservative and kinetic-energy-preserving two-point fluxes](/methods/entropy-conservative-flux.md)
* [Flux differencing and split-form DG](/methods/flux-differencing.md)
* [FLUXO](/software/fluxo.md)
* [Free-stream preservation](/properties/free-stream-preservation.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [Logarithmic mean](/operators/logarithmic-mean.md)
* [MHD blast wave and rotor](/benchmarks/mhd-blast-wave.md)
* [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Subcell finite-volume limiting for DG](/methods/subcell-finite-volume-limiting.md)
* [Summation-by-parts operator](/operators/summation-by-parts-operator.md)
* [TeCNO schemes — entropy-stable reconstruction with the sign property](/methods/tecno-scheme.md)
* [Total variation diminishing (TVD) and slope limiters](/definitions/total-variation-diminishing.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
