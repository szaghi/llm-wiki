---
type: Source
title: "Chandravamsi et al. (2023) — On the application of gradient based reconstruction for flow simulations on generalized curvilinear and dynamic mesh domains"
description: "Extends the gradient-based MEG6 and MIG4 schemes and the α-damping viscous flux to 3D curvilinear, multi-block and deforming meshes, with a free-stream-preserving metric recipe and its discrete proof, an implicit LES of a screeching Mach 1.35 jet against WENO-Z, and an OpenACC single-GPU port."
resource: "doi:10.1016/j.compfluid.2023.105859"
source_kind: paper
authors: [Chandravamsi H., Chamarthi A.S., Hoffmann N., Frankel S.H.]
year: 2023
venue: "Comput. Fluids 258:105859"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Computers_amp_Fluids_Chandravamsi_On_the_application_of_gradient_based_reconstruction_for_flow.pdf"
tags: [reconstruction, finite-difference, gpu, turbulence, low-dissipation]
timestamp: 2026-10-23T16:00:00Z
---

# Summary

The paper carries the [gradient-based reconstruction](/methods/gradient-based-reconstruction.md)
schemes MEG6 and MIG4 and the
[α-damping viscous flux](/methods/alpha-damping-viscous-flux.md) of
[Chamarthi (2023a)](/sources/chamarthi-2023.md) from 2D Cartesian grids to 3D
generalized curvilinear, multi-block, static and analytically deforming
meshes. Both schemes are [conservative finite differences](/definitions/conservative-finite-difference-scheme.md)
on cell-centre point values. They reconstruct characteristic variables with
van Leer's $\kappa=1/3$ polynomial built from the value and its first and
second derivatives, which differ only in how the first derivative is computed:
explicit sixth order (E6, MEG6) or compact fourth order (IG4, MIG4). The
improved Suresh–Huynh [MP limiter](/methods/monotonicity-preserving-limiter.md)
captures shocks, and a curvilinear moving-mesh
[HLLC flux](/methods/hll-riemann-solvers.md) is written out.

The first contribution is a [free-stream-preservation](/properties/free-stream-preservation.md)
recipe: Thomas–Lombard conservative metrics, metric derivatives computed with
the linear (unlimited, left/right-averaged) form of the scheme's own
reconstruction, and the same averaged formula for interpolating the metrics to
interfaces, with $\xi_x/J$ interpolated as one quantity. A discrete proof of
the metric identities is given for MEG6, partly by symbolic computation in a
supplement. Uniform flow on sinusoidal and randomized grids, static and
deforming, stays at machine zero. Non-conservative metrics with fourth-order
central derivatives leave errors of $10^{-3}$–$10^{-1}$ and corrupt an
[isentropic vortex](/benchmarks/isentropic-vortex.md) and a
[double Mach reflection](/benchmarks/double-mach-reflection.md) on skewed
grids.

The second part is an implicit LES of a Mach 1.35 under-expanded jet
(NPR 2.97) on 10, 13 and 20 M cells. MEG6 and MIG4 reproduce the screech
fundamental (St 0.308–0.309 against 0.306 measured) and the flapping B mode,
while [WENO-Z](/methods/weno-z.md) on the 13 M grid gives St 0.432 and an
axisymmetric mode. The third part is an OpenACC single-GPU port, timed on DMR,
a viscous [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) and the
jet: up to $230.72\times$ over one CPU core on an A100, and FP32 only
1.3–1.4× faster than FP64, which the authors attribute to memory bandwidth.
The conclusion concedes that the inviscid scheme is second order on nonlinear
problems.

# Version read

arXiv preprint arXiv:2303.10785v1 [physics.flu-dyn], 19 Mar 2023, 45 pages,
all read; not the Computers & Fluids version of record. Page 1 title and the
four authors in printed order match Crossref; no DOI is printed. Section,
equation, table and figure numbers on this page are those of v1.

# Key claims

Registry notation (see the notation map): velocity components are
$v_1,v_2,v_3$; the computational coordinates $\xi,\eta,\zeta$ and the metric
terms $\xi_x/J$ are kept as printed (no DG nodes or characteristic variables
appear in these claims).

1. MEG6 and MIG4 both give fourth-order inviscid flux derivatives, although MEG6 uses sixth-order explicit and MIG4 fourth-order compact gradients; they differ in dispersion and dissipation (§5.1, theory in ref. [1]). **Stated**
2. For a linear problem the residual $(\hat f_{i+1/2}-\hat f_{i-1/2})/\Delta\xi$ is fourth order with both gradient schemes (§5.1, Step 7). **Stated**
3. The α-damping viscous flux with $\alpha_{\mathrm D}=4$, $\beta_{\mathrm D}=0$ is fourth-order accurate with either gradient scheme (§5.2, Eqs. 29–31). **Stated**
4. Free-stream preservation of MEG6/MIG4 requires (i) conservative Thomas–Lombard metrics, (ii) metric derivatives computed with the inviscid scheme without limiter and with the left/right interpolations averaged, (iii) metric interpolation with the same averaged formula, $\xi_x/J$ interpolated as a whole (§7, Eqs. 36–38). **Derived**
5. With these steps the three discrete metric identities (Eq. 39) hold; for MEG6 the derivative of $y_\xi z$ is the 11-point central stencil $\tfrac1{2880}[2282,-546,89,-3,-1]$ at offsets $1,\dots,5$ (Eq. 41) and the full sum cancels (Eqs. 43–44), the complete arithmetic being in a supplementary Mathematica notebook; MIG4 is said to follow the same steps (§7). **Proved** (for MEG6, partly by symbolic computation). The Eq. (41) coefficients follow from E6 derivatives, the Eq. (19) second derivative and the averaged face value of Eq. (36). *(compiler check, not in the sources: exact rational expansion of $x_{i+1/2}-x_{i-1/2}$.)*
6. Any other interpolation of the metrics than the averaged formula does not satisfy the metric identities for this discretization (§7). **Stated**
7. Uniform flow, $M=0.5$, $t=10$, $20^3$: non-free-stream-preserving metrics give $L_2$ errors in $v_2,v_3$ of about $8.2$–$8.6\times10^{-3}$ (sinusoidal grid) and 0.121–0.386 (randomized grid); the recipe gives $3.1\times10^{-16}$ to $1.3\times10^{-14}$ (Table 2). Conservative metrics differentiated with the explicit fourth-order scheme also fail (§8.1.1). **Shown**
8. Isentropic vortex on a $64\times64$ grid randomized in the centre (20 %, included angles to about 160°): the recipe keeps the vortex and its swirl profile after one period ($t=16$); non-preserving metrics give an unphysical solution (§8.1.2, Fig. 8). **Shown**
9. Double Mach reflection on $768\times256$ with centre nodes displaced by up to 50 % (included angles near 200°): the recipe gives a solution unaffected by the distortion; non-preserving errors appear as rough patches, smaller for MIG4 than for MEG6 (§8.1.3, Fig. 9). **Shown**
10. On a uniform grid at the same resolution WENO-Z resolves the DMR shear layer less well than MEG6 and MIG4 (Fig. 9f). **Shown** (qualitative)
11. Deforming sinusoidal $32^3$ grid: conservative metrics give $L_2(v_2,v_3)$ of $2.3$–$3.2\times10^{-15}$, non-conservative ones $2.88$–$2.93\times10^{-3}$; with the GCL-consistent $(1/J)_t$ of Eq. (14) the schemes preserve free stream on dynamic meshes (§8.2.1, Fig. 10). **Shown**
12. A stationary vortex on a deforming $32^3$ grid stays intact over 8 deformation cycles and matches the exact swirl profile (§8.2.2, Fig. 11). **Shown**
13. Viscous double shear layer ($\mathrm{Re}=10^4$, $M=0.1$, $\gamma=5/3$) on a deforming $360^2$ grid: kinetic-energy and enstrophy histories agree with a $512^2$ stationary MIG4 run and a $512^2$ incompressible reference (§8.2.3, Fig. 12). **Shown**
14. Mach 1.35 jet: on 13 M and 20 M cells the screech fundamental is St 0.308/0.309 (MEG6) and 0.309/0.309 (MIG4) against 0.306 measured; azimuthally averaged SPL 148.1/148.7 dB (MEG6), 149.9/149.5 dB (MIG4) against 148.5 dB from one microphone; at 10 M cells St is 0.443 and 0.435 (Table 3). **Shown**
15. WENO-Z on the 13 M grid gives St 0.432 at 144.1 dB, "significantly off", attributed to its poorer spectral properties (§8.3.2, Table 3). **Shown** (attribution **Stated**)
16. MEG6 captures the flapping B mode (π phase jump about a plane, two amplitude notches, spiral phase field), consistent with Powell et al.; WENO-Z yields an axisymmetric A1 mode (§8.3.3, Figs. 17–18). **Shown**
17. The screech amplitude varies by more than 15 dB with azimuth in the MEG6/MIG4 results; WENO-Z's is nearly constant (§8.3.2, Fig. 16g). **Shown**
18. First shock-cell spacing $\lambda_1=1.15$ against about 1.1 from Pack's formula (Eq. 56); later cells 1.15, 1.0, 1.0, 0.9 (§8.3.1). **Shown**
19. Density POD (1600 snapshots): mode 1 holds about 45 % of the energy with a pure tone at St 0.308; the effective screech source lies between the 3rd and 5th shock cells (§8.3.4, Fig. 19). **Shown**
20. Single-GPU OpenACC speedups over one Xeon Gold 5115 core per 100 iterations, MEG6: DMR (3 M cells) 57.5/100.4/153.14×, TGV (27 M) 92.8/131.3/185.2×, jet (13 M) 61.64/145.7/230.72× on A6000/V100/A100; maxima 211.80× for MIG4 and 209.8× for WENO-Z (Tables 5–7). **Shown**
21. The OpenACC speedups are said to be on a par with CUDA implementations, by comparison with other codes (§9.1). **Stated**
22. MEG6 is the fastest on viscous cases because its derivatives are explicit; WENO-Z is fastest on the inviscid DMR because it needs no gradients; on viscous cases MIG4 and WENO-Z cost about the same (§9.1). **Shown**
23. TGV $256^3$: reconstruction takes over 50 % of the time on CPU and GPU (61.7/68.0 % MEG6, 51.3/55.1 % MIG4); MIG4's tridiagonal gradient routine about 20 %; the Riemann solver has the highest routine speedup, about 420× (§9.2, Fig. 21). **Shown**
24. A100 speedup rises almost linearly to about 2–2.5 M cells, then plateaus (§9.3, Fig. 22). **Shown**
25. GPU memory is about $117(N+8)^3\times64$ bits (117 double-precision 3D arrays with 4 ghost layers per side), of which 71 arrays (about 60 %) are metric terms; a 40 GB A100 handles up to 34 M cells (§9.4, Fig. 23). **Shown**
26. FP32 runs are only 1.3–1.4× faster than FP64; the authors conclude the solver is memory-bandwidth bound (§9.5, Fig. 24). **Shown** (explanation **Stated**)
27. The 13 M-cell jet run (400,000 iterations to $t\,a_\infty/D=800$) takes 34.5 h with MEG6 on one A100 (abstract, §10); §8.3 gives 34.0 h for MEG6 and 41.7 h for MIG4 (see Printed slips). **Shown**
28. Limitation: the inviscid scheme is second order on nonlinear test cases and the MP limiter can activate away from shocks; the method is said nonetheless to outperform a truly fifth-order scheme, per ref. [1] (§10). **Stated**

# Printed slips

- Eqs. (17)–(18) print sums $(u_{i+1}+u_{i-1})$, $(u_{i+2}+u_{i-2})$, … inside the brackets where differences are required; with sums a constant field has a non-zero derivative ($2(\tfrac34-\tfrac3{20}+\tfrac1{60})=\tfrac{37}{30}$ for Eq. 17). *(compiler check, not in the sources.)*
- Eq. (15) prints the quadratic coefficient $3\kappa$, which with $\kappa=1/3$ gives $\phi''/6$ at the face; Eq. (16) and Eqs. (21), (36), (38) use $\phi''/12$, i.e. the coefficient $\tfrac{3\kappa}{2}$ of Chamarthi (2023a), Eq. (43).
- Eqs. (41)–(42), first lines: the face values are summed, $(y_{i+1/2}+y_{i-1/2})$, where Eq. (37) and the final antisymmetric stencils require a difference.
- Appendix C.3, $i=3$: printed $-\tfrac12[x'_{i+1}-x'_{i-1}]-2[x_{i+1}-2x_i+x_{i-1}]$ against $+2[\cdot]-\tfrac12[\cdot]$ in Eq. (19); for $x=\xi^2/2$ it returns $-3$ instead of 1. *(compiler check, not in the sources.)*
- Appendix C.2/C.3, $i=2$: the "4th order partially one sided" stencil on $x_i,\dots,x_{i+4}$ with coefficients $(-\tfrac14,-\tfrac56,\tfrac32,-\tfrac12,\tfrac1{12})$ returns the derivative at $\xi_{i+1}$ (2 for $x=\xi^2$ at $\xi_i=0$), so the printed stencil is shifted by one point. *(compiler check, not in the sources.)*
- Labels: "MEG4/MIG4" (§7), "Non-Freestream Preserving MEG6 (Non-FP MIG4)" (§8.1), Fig. 9 "(c) Non-FP MIG6", Fig. 10 caption "20 × 20" against $32^3$ in §8.2.1, Fig. 17 "(b,c)" for (b,d), "Sec. ??" in §9.1, and Fig. 21 caption panels (a)/(b) against five panels.
- Jet run time: §8.3 says 34.0 h for MEG6, the abstract and §10 34.5 h; Table 5 gives $400{,}000\times31.05\,\mathrm{s}/100=124{,}200\,\mathrm{s}=34.5$ h. *(compiler check, not in the sources.)*
- Eq. (55) is labelled $p_e/p_\infty$ but evaluates to about 1.120 for $M_j=1.35$, which equals $p_e/(\rho_\infty a_\infty^2)$ in the paper's scaling ($1.120\times1.4=1.568$, the sonic-exit value $2.97\,(2/2.4)^{3.5}$); $T_n$ is undefined. *(compiler check, not in the sources.)*
- Eq. (47): $u$ carries $C/(U_\infty R)$ and $v$ carries $C/(U_\infty R^2)$.
- §8.1.2: the randomized region is written "$x\in[3,13]\cup y\in[3,13]$" for the central portion of the domain.
- §8.1.2 calls the comparison metrics "non-conservative compact fourth-order", while §8.1 and Eq. (D.2) define an explicit fourth-order central scheme.
- Figs. 17–18 captions give the WENO-Z panels the "fundamental frequency St = 0.308", the text 0.432.
- §1 "Konrad et al. [36]" for Goc K.A. et al.; "Edgington [30]" for Edgington-Mitchell.
- §9.4 "up to 34 million cells" on an A100 against §9.3, where runs stop at 27 M cells "to avoid GPU memory over-subscription".
- $\alpha$ in Eq. (B.3) and the MP5 parameters $\alpha$, $\beta$ of Appendix E are not defined.

# Notation map

| Chandravamsi et al. (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\xi,\eta,\zeta$, $\Delta\xi=1$ | kept | curvilinear computational coordinates; **$\xi$ collides with the DG nodes $\xi_j$ and $\zeta$ with the characteristic variables** |
| $J$, $\hat\xi_x=\xi_x/J$ | $1/J$, components of $Ja^{(d)}$ | the source's $1/J=\det\partial(x,y,z)/\partial(\xi,\eta,\zeta)$ is the registry's $J$, so the source's $J$ is its inverse; $\hat\xi_x$ is a contravariant metric term |
| $\phi^L_{i+1/2}$, $\phi^R_{i+1/2}$ | $u^-_{i+1/2}$, $u^+_{i+1/2}$ | interface states |
| $Q$, $P=[\rho,u,v,w,p]$ | $u$; primitive vector kept as $P$ | **$P$ is not the CWENO polynomial** |
| $u,v,w$ | $v_1,v_2,v_3$ | velocity |
| $W=R_\xi^{-1}P$ | $\zeta$ (characteristic variables) | of the primitive-form matrix $B_\xi$ |
| $R_\xi$, $R_\xi^{-1}$ | $R$, $L$ | |
| $\hat U,\hat V,\hat W$ | kept | contravariant velocities; **$\hat W$ collides with the characteristic $W$ in the source** |
| $u'_i$, $u''_i$ | $u'_i$, $u''_i$ | from E6 or IG4 and Eq. (19) |
| $\kappa$ | $\kappa_{\mathrm M}$ | $1/3$; **$\kappa$ is kinetic energy in the registry** |
| $\alpha$ (Eq. 18) | kept, page-local | compact coefficient $5/14$ |
| $\alpha$, $\beta$ (App. E) | $\xi_{\mathrm{MP}}$ (page-local on the [MP limiter](/methods/monotonicity-preserving-limiter.md)) | MP5 parameters, values not given |
| $\alpha_D$, $\beta_D$ | $\alpha_{\mathrm D}$, $\beta_{\mathrm D}$, page-local on [α-damping viscous flux](/methods/alpha-damping-viscous-flux.md) | damping and curvature coefficients $4$, $0$ |
| $\hat S^L$, $\hat S^R$, $\hat S^*$ | $s^-$, $s^+$, $s^*$ | HLLC speeds, contravariant |
| $c$, $a$ | $c$ | sound speed (both used); **$a$ is the maximum wave speed in the registry** |
| $E$ (Eq. 54) | kept, page-local | enstrophy; **$E$ is the total energy** |
| St, NPR, $M_j$, $\lambda_n$ | kept | Strouhal number, nozzle pressure ratio, jet Mach number, shock-cell spacing |

# Reference list

78 printed references in numbered style ([1]–[78]), merged complete into the
[bibliography](/bibliography.md) with `citedby` `chandravamsi-2023`. Ref. [1]
is [Chamarthi (2023a)](/sources/chamarthi-2023.md). Ref. [72] (Chandravamsi et
al., Phys. Fluids 35:016121) is a different work whose rule key equals this
slug, and ref. [23] (Chamarthi et al., C&F 251:105742) one whose rule key
equals the slug of a different chunk-5 source; both take disambiguated keys.
Ref. [43] is an arXiv preprint kept distinct from its published version.
Ref. [50] prints no volume, [36] and [56] no pages, [37] no volume; [73] and
[74] are undated OpenACC web pages without author. DOIs are printed only for
[13], [14], [24], [44] and [72]. No printed duplicates were found.

# Pages created or updated

Chunk 5 (2026-10-23). This source is cited on:

* [Characteristic decomposition](/methods/characteristic-decomposition.md)
* [Double Mach reflection](/benchmarks/double-mach-reflection.md)
* [Free-stream preservation](/properties/free-stream-preservation.md)
* [Gradient-based reconstruction (MEG/MIG schemes)](/methods/gradient-based-reconstruction.md)
* [HLL-family approximate Riemann solvers](/methods/hll-riemann-solvers.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Monotonicity-preserving (MP) limiter](/methods/monotonicity-preserving-limiter.md)
* [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
* [WENO-Z weights](/methods/weno-z.md)
* [α-damping viscous flux discretization](/methods/alpha-damping-viscous-flux.md)
