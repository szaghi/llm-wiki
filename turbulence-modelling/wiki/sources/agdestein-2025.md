---
type: Source
title: "Agdestein & Sanderse (2025) — Discretize first, filter next: Learning divergence-consistent closure models for large-eddy simulation"
description: "Defines LES closure targets as the discrete commutator error of a filtered staggered-grid DNS, proves that a face-averaging filter keeps filtered velocities divergence-free, and shows that a projected (divergence-consistent) CNN closure is stable where the unprojected form is not, on 2D and 3D forced turbulence."
resource: "doi:10.1016/j.jcp.2024.113577"
source_kind: paper
authors: [Agdestein S.D., Sanderse B.]
year: 2025
venue: "J. Comput. Phys. 522:113577"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2025_Crossref_Journal_of_Computational_Physics_Agdestein_Discretize_first_filter_next_Learning_divergence-consistent.pdf"
tags: [neural-network, discretization-consistent-closure, commutator-error, a-priori-a-posteriori, incompressible-flow]
timestamp: 2026-10-25T13:40:00Z
---

# Summary

Agdestein & Sanderse (2025) build neural-network
[LES](/definitions/large-eddy-simulation.md) closures for incompressible
flow on the sequence "discretize – differentiate the constraint – filter –
close". The DNS is a second-order staggered finite-volume discretization
whose pressure is removed by the discrete projector $P$, which gives
$\mathrm du/\mathrm dt=PF(u)$. A discrete coarse-graining filter $\Phi$ applied
to this equation gives an exact equation for $\bar u=\Phi u$ with the
discrete commutator error $c(u)=\Phi PF(u)-\bar P\bar F(\Phi u)$. It holds
the subfilter term and the coarse-grid discretization error, so the
training data are exactly consistent with the discrete LES that uses the
closure: the [discretization-consistent](/definitions/discretization-consistent-closure.md)
view.

A face-averaging filter (each coarse face velocity is the area-weighted
mean of the fine face velocities on it) satisfies
$Du=0\Rightarrow\bar D\bar u=0$, proved by a telescoping sum; volume
averaging does not. The paper then compares two
[divergence-consistent LES](/methods/divergence-consistent-les.md)
formulations. The unprojected DIF adds the closure after the projection.
The projected DCF, $\mathrm d\bar v/\mathrm dt=\bar P(\bar F(\bar v)+m)$, acts
with an implied pressure as Lagrange multiplier, and needs no pressure filter.

The closures are no model, a [Smagorinsky model](/methods/smagorinsky-model.md)
with a coefficient fitted per case, and a five-layer CNN on the staggered
grid. The Smagorinsky baseline is the
[Boussinesq](/definitions/boussinesq-hypothesis.md) closure
$m=\nabla\cdot(2\nu_t\bar S)$, discretized on the coarse grid. Training is [a priori](/definitions/a-priori-and-a-posteriori-testing.md)
(commutator-error loss) or [a posteriori](/methods/model-consistent-training.md)
(50 unrolled steps through a differentiable solver). On 2D forced
turbulence ($4096^2$ DNS, LES grids $32^2$–$256^2$) and 3D forced
[periodic-box turbulence](/benchmarks/homogeneous-isotropic-turbulence.md),
the face-averaging filter gives divergence-free $\bar u$ and $c$ to machine
precision. The DCF CNN with face averaging is stable and accurate even when
trained only a priori, while DIF models go unstable even after a posteriori
training. The paper attributes this to the central convective scheme
losing energy conservation when $\bar D\bar v\ne0$. An appendix shows on
the analytic [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
that discrete and continuous commutator errors have different coefficients.
The paper uses "implicit LES" in a sense of its own (see the
[implicit LES](/definitions/implicit-les.md) page).

# Version read

arXiv preprint 2403.18088v2 [math.NA], 8 November 2024 (footer "Preprint
submitted to Journal of Computational Physics, November 11, 2024"), 53
pages: main text pp. 1–29, appendices A–G pp. 30–49, references pp. 49–53.
The file does not print the DOI. Page 1 title and authors match the
published article; page 1 lower-cases "learning" after the colon. Metadata
(year, venue, DOI) are those of the published version. Section, equation,
table and page numbers on this page are those of arXiv v2.

# Key claims

1. Data obtained by discretizing first and then filtering the discrete DNS are exactly consistent with the discrete LES equations; the LES then carries no coarse-grid discretization error but the fine-grid discretization error plus a discrete commutator error that a network can learn (§1, Fig. 1; §3.2, Eqs. 11–12). **Derived**
2. Discrete coarse-graining filters in general do not commute with discrete differentiation, so $\bar D\bar u\ne0$ in general even when $Du=0$ (§3.1–3.2). **Stated** (shown numerically for volume averaging, Table 2)
3. The face-averaging filter $\Phi_{FA}$ with face-area weights and filter width equal to the coarse spacing satisfies $Du=0\Rightarrow\bar D\bar u=0$ (Eq. 13), hence $\bar D\Phi P=0$ (Eq. 14); proved by a telescoping sum (App. C.1, uniform $3\times3$ example; App. C.2, non-uniform grids in 2D or 3D). **Proved**
4. The property fails for non-uniform weights (other than face-size weights) or a filter width different from the coarse spacing; Gaussian weights "would not work" (§3.3; App. C.2). **Stated**
5. With $\Phi_{FA}$ the commutator error is divergence-free, $\bar Dc=0$, so $c=\bar Pc$ and $\mathrm d\bar u/\mathrm dt=\bar P(\bar F(\bar u)+c(u))$ (Eqs. 15–16). **Derived**
6. For the face-averaging filter $\bar D\Phi=\Psi D$, with $\Psi$ a volume-averaging pressure filter of weights $\lvert\Omega_I\rvert/\lvert\bar\Omega_J\rvert$ (Eq. C.10): "the face-averaging velocity filter goes hand in hand with a volume-averaging pressure filter" (App. C). **Proved**
7. In the DCF formulation no pressure filter is needed: the pressure is implied by the coarse Poisson equation $\bar L\bar p=\bar\Omega_p\bar D(\bar F(\bar u)+c(u))$ (Eq. 19) and acts as a Lagrange multiplier (§3.3, §4.1). **Derived**
8. Filtering the differential-algebraic system directly, without differentiating the constraint, gives a divergence commutator $c_D=(\bar D\Phi-\Psi D)u$ and a pressure commutator $c_P$ whose modelling is unclear (App. D, Eqs. D.3–D.4). **Derived**
9. The continuous face-averaging top-hat filter has transfer function $\hat G^\alpha(\boldsymbol k)=\prod_{\beta\ne\alpha}\sin(\pi k_\beta\Delta/2)/(\pi k_\beta\Delta/2)$, so it damps less than the volume-averaging filter: $\hat G(\boldsymbol k)\le\hat G^\alpha(\boldsymbol k)$, with equality iff $k_\alpha=0$ (App. E, Eqs. E.2, E.5). **Derived**
10. A priori, 2D ($4096^2$, double precision; Table 2): with face averaging $\|\bar D\bar u\|/\|\bar u\|$ is $1.5\times10^{-14}$ to $5.3\times10^{-14}$ and $\|c-\bar Pc\|/\|c\|$ is $2.3\times10^{-13}$ to $1.3\times10^{-12}$; with volume averaging $\|\bar D\bar u\|/\|\bar u\|$ is 1.1, 0.67, 0.39, 0.19 for $\bar n=32,64,128,256$ and the non-solenoidal part of $c$ is 11%, 9.6%, 8.8%, 12% (§5.1.3). **Shown**
11. A priori, 3D ($1024^3$, single precision; Table 2): face averaging gives $\|\bar D\bar u\|/\|\bar u\|\approx2.2$–$2.4\times10^{-5}$ (single-precision level); volume averaging gives non-solenoidal parts of $\bar u$ from 4.3% ($32^3$) to 0.94% ($256^3$) and of $c$ from 19% to 13% (§5.1.3). **Shown**
12. The commutator-error magnitude barely depends on the filter type at equal width. With face averaging at $32^2$ and $128^3$, more than half of the filtered right-hand side is commutator error (0.56 and 0.51) while 92% and 91% of the kinetic energy is resolved; at $256^2$, $c$ is still 7.7% of the right-hand side with all the energy resolved (§5.1.3, Table 2). **Shown**
13. Because $c$ includes the coarse-grid discretization error, the grainy oscillations of the under-resolved central-difference term $\bar P\bar F(\bar u)$ appear in $c$, and the closure must predict them; with a filter-first target they would have to be removed otherwise, e.g. by explicit filtering (§5.1.2, Fig. 8). **Shown** (qualitatively)
14. A-priori-trained CNN parameters give the lowest a priori error for both filters at all resolutions (§5.2.1, Fig. 10). **Shown**
15. In the DCF formulation the CNN clearly beats no closure and Smagorinsky in a posteriori error at $t=0.27$; trained a priori it is much better with face averaging than with volume averaging, and a posteriori training makes the two filters indistinguishable (§5.2.2, Fig. 11). **Shown**
16. In the DIF formulation the a-priori-trained CNN shows signs of instability and is worse than no closure at all $\bar n$ except 32; a posteriori training reduces the error but the energy eventually grows (§5.2.2–5.2.3, Figs. 11–12). **Shown**
17. The DIF instability is explained by the second-order central convective discretization in divergence form, which equals an energy-conserving skew-symmetric form only for divergence-free fields; without $\bar D\bar v=0$ energy conservation is not guaranteed (§5.2.3). **Stated** (consistent with the divergence growth of Fig. 15)
18. In DCF the a-posteriori-trained CNN keeps the total kinetic energy at the reference level much longer than no closure and Smagorinsky ($\bar n=256$, Fig. 12), and its spectrum stays close to the reference at $t=5$, long after the trajectories decorrelate ($\bar n=128$, Fig. 13) (§5.2.3–5.2.4). **Shown**
19. No closure leaves too much energy at high wavenumbers, attributed to central-scheme oscillations, which Smagorinsky corrects; all DIF CNNs put too much energy at high wavenumbers (§5.2.4, Fig. 13). **Shown**
20. Divergence of the LES solutions ($\bar n=256$): the face-averaged reference is $O(10^{-4})$ (single precision), the volume-averaged one $O(10^{-1})$; DIF divergence grows in time for all closures, while DCF gives the reference level with face averaging and divergence-free solutions with volume averaging, although that reference is not divergence-free (§5.2.6, Fig. 15). **Shown**
21. The fitted Smagorinsky coefficients (grid search on the a posteriori training error) decrease with resolution: for DIF from 0.129–0.131 at $\bar n=32$ to 0.000 at $\bar n=256$, for DCF from 0.142–0.144 to 0.014–0.023. The paper explains the zero by the Smagorinsky term not being divergence-free, so a zero coefficient keeps the DIF right-hand side divergence-free (App. B.5, Table B.5). **Shown**
22. On one Nvidia H100 GPU, DNS and filtering of all data took $1.57\times10^4$ s; a priori training (10 000 iterations) 160.6 s to 1583.6 s; a posteriori training (1000 iterations) 4449.3 s to 5849.2 s; DIF and DCF cost the same (§5.2.7, Table 3). **Shown**
23. When the a-priori-trained model is already stable and accurate (DCF with face averaging), a posteriori training brings only a minor gain; the authors still judge it worth its cost because the weights are reusable for the same configuration (§5.2.7, §6). **Shown** / **Stated**
24. Adding noise to the training data, a common stabilizer, could destroy divergence-freeness; with several noise levels the validation error was better without noise (§6). **Stated** (no data shown)
25. For the 2D Taylor–Green vortex under a top-hat filter of width $\Delta$, the continuous convective commutator error is $c_x=-\tfrac12(\mathrm{sinc}^4(\Delta/2)-\mathrm{sinc}(\Delta))\sin2x=-\tfrac{\Delta^4}{480}\sin2x+O(\Delta^6)$ (Eqs. F.9, F.12), while the discrete one is $-\tfrac14E\sin2x$ with a different coefficient $E$ (Eqs. F.29–F.30): same spatial shape, different coefficients, so a filter-first model trained on discretize-first data is inconsistent (App. F). **Derived**
26. 2D decaying turbulence ($\bar n=128$): in DCF all models decay and the CNN energy is most accurate, no closure slightly too dissipative and Smagorinsky more so; in DIF the CNNs become unstable, and a posteriori training delays but does not remove the instability (App. G.1, Fig. G.20). **Shown**
27. 3D forced turbulence ($1024^3$ DNS, $Re=2000$, face averaging, DCF, $\bar n\in\{32,64\}$): a CNN of 234 096 parameters beats no closure and Smagorinsky ($C_s=0.17$) in a priori and a posteriori error at $t=0.29$, keeps the energy close to the target longer, and tracks the reference spectrum after decorrelation; Smagorinsky is too dissipative at high wavenumbers (App. G.2, Figs. G.21–G.23). **Shown**
28. Limitations: uniform (top-hat) weights are required, the filter width must equal the grid spacing, the DNS grid must overlap the LES faces, and divergence-consistency holds only for the second-order staggered divergence; on a collocated grid a face-averaging filter exists but loses divergence-consistency (§6). **Stated**

# Printed slips

1. §4.3, p. 13: "$u_{i+1}=RK_{\Delta t}(u_i)$ is obtained using one RK4 time step from section 2.4", while §2.4 defines Wray's three-stage third-order scheme.
2. §1, p. 3 announces "a decaying turbulence test case" for §5, which is titled "forced turbulence in a periodic box" and uses the body force (31); App. G.2, titled "LES of forced turbulence (3D)", opens with "we consider a decaying turbulence test case" and applies a body force.
3. Eq. (31) prints the force $f^\alpha=\delta_{\alpha=1}\sin(8\pi x_2)$ (amplitude 1), while App. G.2 says "We use the same body force as in the 2D case, namely $f^\alpha(x)=5\delta_{\alpha=1}\sin(8\pi x_2)$" (amplitude 5).
4. Table B.4 caption: "CNN architecture, with $\epsilon=1/100$": no $\epsilon$ appears in the table or the text.
5. Table B.4 caption: "The total radius is 8". Five convolution layers of radius 2 combine to a radius of 10 grid indices before the interpolation layers *(compiler check, not in the sources)*; the paper does not say how it counts 8.
6. §6, p. 29: the face-average filter "naturally extends to unstructured grids, as shown in figure 2"; the unstructured example is Fig. 4 (right).
7. App. B.4: "We then start saving $\bar u$ and $c$ every time step until $t_{\rm end}=5$. Every 50 time steps we compute $\bar u$ and $c(u)$ on four coarse grids": the two sentences disagree on the saving frequency.
8. Table 2 header writes $\|c\|/\|\bar P\bar F+c\|$, the text (p. 19) $\|c\|/\|\bar P\bar F+\bar c\|$.
9. App. E, p. 40: "In 3D, the isocontour of $G$ at a given damping level takes the shape of a sphere, as $G_k$ only depends on $\|k\|$" (also the Fig. E.19 caption), while Eq. (E.2) is a product of one-dimensional factors in each $k_\alpha$. At $\boldsymbol k=(K,0,0)$ and $\boldsymbol k=(K/\sqrt3)(1,1,1)$ the product agrees to second order in $K\Delta$ and differs beyond it, so it is not a function of $\|\boldsymbol k\|$ alone *(compiler check, not in the sources)*.
10. Ref. [27] prints the authors "E Hairer, G Wanner, and O Solving", a spurious third author taken from the title "Solving ordinary differential equations II".
11. Typos: "face-averagining" (p. 20), "decorellated" (p. 22), "weigthed" (p. 34), "be either be known" (p. 2), "this parameter is be fitted" (p. 14).

# Notation map

| Agdestein & Sanderse (2025) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u$, $p$ (discrete vectors), $\nu$, $f$ | $\boldsymbol u$, $p$, $\nu$, $f_i$ | kinematic pressure; the same symbols denote continuous fields up to §2.2 |
| $\bar u=\Phi u$ | $\bar{\boldsymbol u}$ | filtered DNS velocity on the coarse grid |
| $\bar v$ | — | LES solution, distinct from $\bar u$ |
| $\bar D,\bar G,\bar L,\bar P,\bar F$ | — | **collision**: the overbar marks coarse-grid operators, not a filtered operator |
| $G=-\Omega_u^{-1}D^T\Omega_p$ | — | **collision**: discrete gradient, not the filter kernel $G$ |
| $\Omega$, $\Omega_u$, $\Omega_p$, $\Omega_I$ | — | **collision** with $\Omega_{ij}$: domain, volume-size matrices, a finite volume |
| $N$, $\bar N$, $n$, $\bar n$ | $N_x\times N_y(\times N_z)$ | **collision**: grid sizes, not a polynomial degree |
| $\Phi$, $\Phi_{FA}$, $\Phi_{VA}$, $\Psi$ | — | discrete filter matrices; $\Psi$ pressure-point filter |
| $\bar\Delta$ (App. F: $\Delta$) | $\Delta$ | filter width = coarse spacing, "diameter of the averaging domain in the infinity norm" |
| $c(u)$, $c_D$, $c_P$ | — | discrete commutator errors |
| $m(\bar v,\theta)$ | — | closure model |
| $\theta$ (Smagorinsky) | $C_s$ | $\nu_t=(\theta\bar\Delta)^2\sqrt{2\,\mathrm{tr}(\bar S\bar S)}=(C_s\Delta)^2\lvert\bar S\rvert$, factor two present |
| $\theta$ (CNN) | $\boldsymbol\theta$ | trainable parameters |
| $L^{\rm prior}$, $L^{\rm post}$ | $\mathcal L$ | **collision**: $L$ is also the pressure Laplacian |
| $G_k$, $G^\alpha_k$ | $\hat G(\boldsymbol k)$ | transfer functions of the volume- and face-averaging filters |
| $\hat u_k$, $\hat E_k$ | $u_{\boldsymbol k}$, — | **collision**: hat on Fourier coefficients (registry hat = test filter) |
| $\kappa=\|k\|$, $\kappa_p$ | $k$ | **collision** with the von Kármán $\kappa$ |
| $\rho^\alpha_{J,I}$ | — | **collision**: face-filter weights, not density |
| $d$ (App. F) | $h$ | DNS grid spacing; **collision** with the wall distance $d$ |
| $E$ | — | Taylor–Green commutator coefficient (F.30); also total kinetic energy in figures |
| $\lambda_2$, $S$, $T$ | $S_{ij}$, $\Omega_{ij}$ | vortex criterion of symmetric and antisymmetric velocity-gradient parts |
| a priori / a posteriori | a priori / a posteriori | "a-priori" names both a training mode (§4.3) and the analysis before running LES (§5.1) |

# Reference list

77 printed references in numbered style ([1]–[77], roughly alphabetical),
merged complete into the [bibliography](/bibliography.md) with `citedby`
`agdestein-2025`. No printed duplicates. Identity points: ref. [2] (Bae &
Lozano-Durán, arXiv 2022) and ref. [67] (Sirignano & MacArt, arXiv 2023)
are preprints distinct from the same-first-author, same-year published works that share their natural keys; ref.
[74] (van Gastelen et al., February 2023) is the preprint of a later
journal paper and stays a separate entry; ref. [38] prints an arXiv
preprint and its ETNA publication in one item. Irregular items: [27] prints
the spurious author "O Solving"; [17] has a contributor printed only as
"Meredith"; [10], [19], [26], [55] print no page or article number; [63]
and [74] print no venue; [54] is software.

# Pages created or updated

Chunk 1 (2026-10-25). This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Discretization-consistent closure](/definitions/discretization-consistent-closure.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Divergence-consistent discretize-first LES](/methods/divergence-consistent-les.md)
- [Model-consistent (a posteriori) training of learned closures](/methods/model-consistent-training.md)
- [Scale-similarity and mixed subgrid-scale models](/methods/scale-similarity-model.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
