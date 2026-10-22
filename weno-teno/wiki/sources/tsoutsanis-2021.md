---
type: Source
title: "Tsoutsanis et al. (2021) — CWENO Finite-Volume Interface Capturing Schemes for Multicomponent Flows Using Unstructured Meshes"
description: "Arbitrary-order unstructured finite-volume CWENO (high-order central plus second-order directional polynomials) applied to the five-equation diffuse-interface model in UCNS3D: design order 3–6, lower cost than equal-order WENO, primitive-variable reconstruction against interface oscillations, and multiphase shock–bubble tests."
resource: "doi:10.1007/s10915-021-01673-y"
source_kind: paper
authors: [Tsoutsanis P., Adebayo E.M., Merino A.C., Arjona A.P., Skote M.]
year: 2021
venue: "J. Sci. Comput. 89:64"
local_file: "/home/stefano/papers/mosaic/weno-teno/2021_Crossref_Journal_of_Scientific_Computing_Tsoutsanis_CWENO_Finite-Volume_Interface_Capturing_Schemes_for_Multicom.pdf"
tags: [cweno, finite-volume, multiphase, interface-capturing, reconstruction]
timestamp: 2026-10-22T12:00:00Z
---

# Summary

The paper applies the arbitrary-order unstructured finite-volume
[CWENO](/methods/cweno.md) reconstruction of Tsoutsanis & Dumbser and Dumbser et al. to
compressible multicomponent flows. The model is the quasi-conservative
[five-equation model](/definitions/five-equation-model.md) of Allaire, Clerc and Kokh,
closed by the [stiffened-gas equation of state](/definitions/stiffened-gas-equation-of-state.md).
The volume-fraction equation is rewritten in the Johnsen–Colonius form, and its source is
evaluated as a surface integral with the Riemann-solver normal velocity.

CWENO combines one high-order polynomial on a compact central stencil of $2N_K$ cells with
second-order polynomials on small directional stencils, one per face. All polynomials come
from a constrained least-squares fit in a reference element. The nonlinear weights are of
[WENO-JS](/methods/weno-js-reconstruction.md) type, $q=4$, $\epsilon=10^{-6}$. The
[smoothness indicators](/definitions/smoothness-indicator.md) are quadratic forms with a
precomputed matrix. Fluxes are HLLC ([HLL-family solvers](/methods/hll-riemann-solvers.md)),
time stepping is third-order [SSP Runge–Kutta](/methods/ssp-runge-kutta.md), and the
implementation is the open-source UCNS3D code. No theorem is proved.

On triangular meshes the multi-species advection test reaches design order 3–6 for CWENO and
for the authors' WENO, at almost identical errors. CWENO's printed cost is "approximately
60–80%" of WENO's. At an isolated interface with a jump in $\gamma$, CWENO is less oscillatory
than WENO at third order, and primitive-variable reconstruction removes the pressure and
velocity oscillations. Multiphase tests: a [gas–liquid Riemann problem](/benchmarks/gas-liquid-riemann-problems.md),
shock-induced collapse of an air bubble in water, the Mach 2.4 shock on a water column with and
without a cavity, and the Haas–Sturtevant [shock–helium-bubble interaction](/benchmarks/shock-bubble-interaction.md)
in 2D and 3D. In that test the interface velocities lie within the experimental error,
[Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md) roll-up sharpens with
resolution ([numerical dissipation](/definitions/numerical-dissipation.md)), and
[symmetry](/properties/symmetry-preservation.md) is lost at late times on the finer
unstructured meshes.

# Version read

Version of record (Springer typeset, open access CC BY 4.0; received 11 March 2021, published
online 9 November 2021), 27 pages, article number 64. Title and authors match page 1 and
Crossref. No identity problem. Data are at Cranfield Online Research Data,
doi:10.17862/cranfield.rd.16447212.v1. Numbering is that of the journal version.

# Key claims

Symbols (see the Notation map): $\phi_1$ volume fraction and $p_\infty$ stiffening pressure (registry §10); page-local
$N_K$ number of polynomial coefficients, $d_s$, $\omega_s$, $\beta_s$ the linear weights,
nonlinear weights and smoothness indicators of stencil $s$ ($s=1$ central).

1. The five-equation model of [1] with stiffened-gas phases is used, with the volume-fraction equation rewritten in the Johnsen–Colonius form $\partial_t\phi_1+\nabla\cdot(\phi_1v)=\phi_1\nabla\cdot v$ (§2, Eqs. 1–12). **Stated**
2. The source $\int_{V_i}\phi_1\nabla\cdot v\,dV$ is approximated by $\phi_1\int_{\partial V_i}v_n^{\mathrm{Riem}}\,dS$, with the normal velocity of the Riemann solver and the cell average of $\phi_1$ at level $n$ (§3.1, Eqs. 15–16). **Stated** (after [32])
3. A polynomial of degree $r$ "provides $r+1$ order of accuracy" (§3.2, Eq. 18). **Stated**
4. The central stencil has $M=2N_K$ cells "for enhanced robustness as reported in several previous studies [15,30,58]", with $N_K(r,d)=\frac1{d!}\prod_{l=1}^d(r+l)$ for degree $r$ in $d$ dimensions (§3.2, Eq. 23). **Stated**
5. The least-squares system is solved by Householder QR, with a Moore–Penrose pseudo-inverse computed once at the start (§3.2, Eq. 28). **Stated**
6. The directional stencils are the "Type3" stencils of [58], one per face, carrying degree-1 (second-order) polynomials; the central polynomial has arbitrary degree (§3.2.1). **Stated**
7. CWENO schemes "were found to be more robust and significantly more computational efficient compared to the original WENO type of schemes for unstructured meshes", the gain coming from low-order polynomials on smaller directional stencils (§1, citing [19,61]). **Stated**; partly **Shown** in §4.1–4.3
8. The smoothness indicators are quadratic forms $\beta_s=\sum_k c^s_k\sum_{k'}\mathcal O_{kk'}c^s_{k'}$ in the polynomial coefficients, with a precomputable oscillation-indicator matrix $\mathcal O$ (§3.2.1, Eqs. 33–35). **Derived**
9. The third-order SSP Runge–Kutta method [26] "is stable for $CFL\le1$" (§3.3). **Stated**
10. Multi-species advection on triangular meshes of 10–80 edges per side reaches the design order for orders 3 to 6. At 80 edges, CWENO6 has $e_{L^\infty}=6.493\times10^{-10}$, $e_{L^2}=2.046\times10^{-10}$ (orders 5.77 and 5.88), and CWENO5 has $e_{L^\infty}=3.327\times10^{-8}$ (orders 5.03 and 4.95) (§4.1, Table 1). **Shown**
11. At equal order, CWENO and WENO errors are almost identical, e.g. third order at 80 edges: $e_{L^\infty}=2.487\times10^{-5}$ against $2.473\times10^{-5}$ (Table 1). **Shown**
12. "For this test the CWENO schemes require approximately 60–80% of the time taken by a WENO scheme of the same spatial order", a figure "expected to improve" on larger and 3D meshes. Normalized times at 80 edges: 673.159 against 798.829 (third order), 928.223 against 1128.293, 1119.209 against 1738.832, 1493.933 against 2417.527 (sixth order) (§4.1, Table 1). **Shown** (but see Printed slips)
13. On a coarse mixed-element mesh (80 edges per side), CWENO3 is "significantly less oscillatory" than WENO3 at an isolated material interface, which the authors attribute to the more compact directional stencils (§4.2, Fig. 2). **Shown**
14. Primitive-variable reconstruction gives oscillation-free pressure and velocity at the isolated interface and conservative-variable reconstruction does not; the normalized pressure and velocity errors of several CWENO schemes are "close to machine precision" (§4.2, Figs. 3–4). **Shown**
15. "It is well documented [31–34] that primitive variable reconstruction is needed to prevent spurious oscillations in problems where $\gamma$ is not constant, since reconstruction in conservative or characteristic variables suffer from oscillations across them" (§4.2). **Stated** (characteristic variables are not tested in the paper)
16. Reconstruction is done in conserved or primitive variables, always converted back to conserved variables before the flux evaluation (§3.3). **Stated**
17. Gas–liquid Riemann problem at 100 edges per side: CWENO5 is less oscillatory than WENO3; from here on only CWENO is used (§4.3, Fig. 5). **Shown**
18. Air-bubble collapse in water ($M=1.72$, about $10^6$ quadrilaterals, edge $\approx D_b/250$, CWENO5): peak pressure 7.7 GPa, against 10.1 GPa of Nourgaliev et al. [39] at $D_b/800$ and 7.8 GPa of Goncalves et al. [25] at $D_b/300$; peak temperature about 15 670 K; centreline pressure peaks at $t\approx3.9\,\mu$s and $4.9\,\mu$s; the bubble-volume history agrees with [39] except for a shallower maximum compression (§4.4, Figs. 6–8). **Shown**
19. Shock on a water column ($M=2.4$, about $0.89\times10^6$ cells, $D_b/192$, CWENO5, to $t^*=10$): the flow features agree with Xiang & Wang [74] and the schlieren images of Sembian et al. [48]; the negative-pressure dip at $t^*=0.8$ is weaker than in [74] but present; with a cavity, the peak of the maximum-pressure history has the right timing and a slightly lower value (§4.5, Figs. 10–13). **Shown**
20. Shock–helium bubble in 2D ($D_b/35$, $D_b/120$, $D_b/400$) and 3D ($D_b/50$), CWENO5, to $1000\,\mu$s: the Kelvin–Helmholtz roll-up sharpens with 2D resolution; the 3D resolution is too coarse to capture it (§4.6, Figs. 16–18). **Shown**
21. Symmetry of the 2D solution is lost at late times on the medium and fine meshes, "indicative of multi-dimensional reconstruction nature of the framework employed and of the arbitrary unstructured elements" (§4.6). **Shown**
22. Time-averaged interface velocities (upstream, jet, downstream, m/s): 2D fine 181.242, 237.086, 145.895; 3D 178.402, 228.375, 144.197; Coralic & Colonius WENO5 [13] 173, 230, 145; experiment [27] $170\pm17$, $230\pm23$, $145\pm15$: all within the experimental variation (Table 2). **Shown**
23. Switching to primitive-variable reconstruction "was needed to remove the oscillations that appear across material interfaces"; future work: the Baer–Nunziato seven-equation model and the GPR model (§5). **Stated**

# Printed slips

- Eq. (16) has no overall minus sign on the flux sum: it prints $d\mathbf U_i/dt=+\frac1{\lvert V_i\rvert}\sum_j\sum_\alpha(F_{\mathbf n_{ij}}-\mathbf a^n_{i,1}u_n^{\mathrm{Riem}})\omega_\alpha\lvert S_{ij}\rvert$, while Eq. (13) has the flux on the left and the source on the right. It also applies the source to the full vector without saying that it enters only the $\phi_1$ component. Eq. (15) writes $\int_{V_i}\phi_1\,dV$, but Eq. (16) uses the cell average.
- Eq. (42), gas–liquid Riemann problem: the state is labelled $(\rho_1,\rho_2,u,v,p,a_1)$, but the left state prints "(1.241, 0, 0, 2.753, 1.4, 1)", with 1.4 where $p$ should be, and the right state prints five entries, "(0, 0.991, 0, 3.059x10$^{-4}$, 0)". The values cannot be read off unambiguously.
- Eq. (32) writes $\tilde\omega_s=\lambda_m/(\epsilon+\mathcal{SI}_s)^b$, with index $m$ on $\lambda$. The text before Eq. (33) names "$\mathcal{SI}_m$" and then defines $\mathcal{SI}_s$, and the sentence "where $\tilde a_k$ are the reconstructed degrees of freedom" refers to a symbol in no equation.
- Eq. (23) is inconsistent with Eqs. (25)–(28) by one *(compiler check, not in the sources)*. $\frac1{d!}\prod_{l=1}^d(r+l)$ counts all coefficients of a degree-$r$ polynomial, including the constant: $r=1$, $d=2$ gives 3, i.e. $1,x,y$. Eqs. (25)–(28) instead index $K$ coefficients $k=1,\dots,K$ beside the separate constant $U_0$.
- Eq. (36), $\lambda_1=1-1/\lambda_1'$: no value of $\lambda_1'$ is given, so the linear weights used cannot be reproduced from the paper.
- Table 1: the order column after $e_{L^2}$ is headed "$O_{L^\infty}$" again (CWENO and WENO); its caption reads "with the CWENO schemes being requiring".
- §4.1 against Table 1 *(compiler check, not in the sources)*: the CWENO/WENO time ratios computed from the printed times are 0.80, 0.94, 0.91, 0.84 (third order, 10–80 edges), 0.84, 0.77, 0.80, 0.82 (fourth), 0.63, 0.66, 0.66, 0.64 (fifth) and 0.60, 0.55, 0.58, 0.62 (sixth). The range is 0.55–0.94, not "approximately 60–80%".
- Reference list: [37] (Meng & Colonius, Shock Waves 25, 2015) prints doi:10.1016/j.jcp.2014.06.003, the DOI printed for [13] (Coralic & Colonius, J. Comput. Phys. 274). [39] (Nourgaliev et al., J. Comput. Phys. 213, 2006) prints doi:10.1016/j.jcp.2009.10.028, the DOI printed for [34] (Johnsen et al. 2010). [41] prints "Pattersen"; [3] prints "Ranam, Z." where [5] has "Rana, Z.".
- §4.5 calls the water column a "water droplet" and a "water bubble". The water parameters differ per test without comment: $\gamma=6.12$, $p_\infty=3.43\times10^8$ (§4.5), $\gamma=4.4$, $p_\infty=6\times10^8$ (§4.4), and non-dimensional $\gamma=5.5$, $p_\infty=1.505$ (§4.3).
- Typos: "Kapila's et al.", "Allaire's et al.", "Essentialy" (§1); "these instabilities. as shown in as shown in Fig. 18" (§4.6); "upstrean" (Table 2 footnote).

# Notation map

| Tsoutsanis et al. 2021 | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $a_1$, $a_2$ | $\phi_1$, $\phi_2$ (registry §10) | volume fractions; **collision** with the wave speed $a$ |
| $\mathbf U$, $\mathbf F_n$, $\mathbf s$ | $u$, normal flux, source $S$ | $u$ includes $\phi_1$; $\mathbf U_i$ are cell averages $\bar u_i$ |
| $\mathbf u=(u,v,w)$, $u_n$ | $v=(v_1,v_2,v_3)$, $v_n$ | velocity, face-normal velocity |
| $\epsilon$ (specific internal energy) | $e$ | **collision** with the weight regularization $\epsilon$, which the source also writes $\epsilon$ |
| $\gamma_i$, $\pi_{\infty,i}$ | $\gamma_i$, $p_{\infty,i}$ (registry §10) | stiffened-gas parameters; the text calls $\gamma$ "specific heats" |
| $\xi=1/(\gamma-1)$ | — | mixture parameter; **collision** with the reference coordinate $\xi$ |
| $\mathbf U_{ij,L}$, $\mathbf U_{ij,R}$ | $u^-$, $u^+$ | own cell and neighbour states at a face point |
| $\omega_\alpha$ (Gauss weights) | $\mathsf w_\alpha$ | keeps $\omega_s$ for the nonlinear weights |
| $r$ (polynomial order) | degree $r$ (local) | **collision**: registry $r$ counts stencil points; design order $r+1$; CWENO$n$ has degree $n-1$ |
| $K(r,d)$ | $N_K$ (local) | number of coefficients; **collision** with the TENO stencil size $K$ |
| $a_k$, $a^s_k$ | $c_k$, $c^s_k$ (local) | polynomial coefficients; **collision** with $a$ and with $a_1$ |
| $s$, $s_t$; $p_s$, $p_{opt}$, $p_{cweno}$ | stencil index ($s=1$ central), number of stencils; polynomials | |
| $\lambda_s$, $\lambda_1'$ | $d_s$, unnormalized central weight | linear weights |
| $\tilde\omega_s$, $\omega_s$ | $\alpha_s$, $\omega_s$ | WENO-JS form |
| $\mathcal{SI}_s$, $\mathcal{OI}_{kq}$ | $\beta_s$, $\mathcal O_{kk'}$ (local) | smoothness indicator and its matrix |
| $\epsilon$, $b$ | $\epsilon=10^{-6}$, $q=4$ | |
| $CFL$ | $\nu$ | |

# Reference list

The paper prints 75 references, numbered [1]–[75] and sorted alphabetically by first author.
The list is merged complete into the [bibliography](/bibliography.md), with `citedby`
including `tsoutsanis-2021`. Ref. [61] (Tsoutsanis & Dumbser 2021, Comput. Fluids) would take
this source's own key and is keyed `tsoutsanis-2021-b`. Same-author same-year works take
suffixes in printed order: Antoniadis 2015 [3]–[5], Dumbser 2007 [16]/[17], Tsoutsanis 2016
[59], [60], [62], [66], Tsoutsanis 2018 [57]/[67], Wallis 2021 [70]/[71]. [68] is the UCNS3D
software, undated (accessed 10 March 2021). Fourteen articles print only a DOI, without volume
or pages. The wrong DOIs of [37] and [39] are recorded as printed, with a note. No item is
unparseable.

# Pages created or updated

Chunk 2 (2026-10-22). This source is cited on:

* [Central WENO (CWENO)](/methods/cweno.md)
* [Characteristic decomposition](/methods/characteristic-decomposition.md)
* [Five- and six-equation diffuse-interface models](/definitions/five-equation-model.md)
* [Gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md)
* [HLL-family approximate Riemann solvers](/methods/hll-riemann-solvers.md)
* [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)
* [Shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)
* [Shock–water-column interaction](/benchmarks/shock-water-column.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Stiffened-gas equation of state](/definitions/stiffened-gas-equation-of-state.md)
* [Symmetry preservation](/properties/symmetry-preservation.md)
* [WENO-JS reconstruction](/methods/weno-js-reconstruction.md)
