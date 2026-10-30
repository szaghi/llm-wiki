---
type: Source
title: "Maltsev et al. (2023) — Hybrid discontinuous Galerkin-finite volume techniques for compressible flows on unstructured meshes"
description: "Hybrid modal DG–finite-volume scheme in UCNS3D for mixed-element unstructured meshes: troubled cells found a priori by a shock detector or MOOD-type criteria have their higher Taylor modes overwritten by a same-order CWENOZ reconstruction, with a study of bounds definition, checking frequency and troubled-cell fraction."
resource: "doi:10.1016/j.jcp.2022.111755"
source_kind: paper
authors: [Maltsev V., Yuan D., Jenkins K.W., Skote M., Tsoutsanis P.]
year: 2023
venue: "J. Comput. Phys. 473:111755"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Journal_of_Computational_Physics_Maltsev_Hybrid_discontinuous_Galerkin-finite_volume_techniques_for_c.pdf"
tags: [dg, cweno, troubled-cell, unstructured-mesh, limiting, shock-capturing]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

The paper builds hybrid
[discontinuous Galerkin](/methods/discontinuous-galerkin.md)–finite-volume
schemes of order 3 to 5 ($N=2$ to $4$) for mixed-element unstructured meshes
in 2D and 3D, inside the open-source code [UCNS3D](/software/ucns3d.md). A
modal DG method with a cell-centred Taylor basis, normalized by the cell
size, evolves the solution. At every Runge–Kutta stage the unlimited DG
solution is checked by an a priori
[troubled-cell indicator](/definitions/troubled-cell-indicator.md). In
flagged cells the higher DG modes are overwritten with the coefficients of a
[CWENOZ](/methods/cweno.md) least-squares reconstruction from the cell
averages; DG and FV share the same basis, so this is a copy of coefficients.
The cell average (mode 0) is kept, so the scheme stays conservative. The
reconstruction has the same order as the DG polynomial, which makes the
method a same-order [WENO limiter for DG](/methods/weno-limiter-dg.md). The
FV part is the [unstructured least-squares reconstruction](/methods/unstructured-gradient-reconstruction.md)
of Tsoutsanis et al., with WENO-Z-type CWENOZ weights and a
derivative-integral [smoothness indicator](/definitions/smoothness-indicator.md).

The study is about the switch. Two indicator families are compared: a
KXRCF- and Fu–Shu-like shock detector (SD), and the PAD and NAD criteria of
[MOOD](/methods/mood-a-posteriori-limiting.md) used a priori, with a strict
or a relaxed discrete maximum principle. The NAD bounds are taken either from
the direct side neighbours ("limited") or from the whole reconstruction
stencil ("extended"). The flag is either re-checked at every RK stage or
frozen for the whole step. The authors claim to be the first to study these
three choices.

All evidence is numerical. The tests are convergence tables for linear
advection and the [isentropic vortex](/benchmarks/isentropic-vortex.md),
[solid-body rotation](/benchmarks/solid-body-rotation.md), square-wave
advection, the [Shu–Osher problem](/benchmarks/shu-osher-problem.md),
[double Mach reflection](/benchmarks/double-mach-reflection.md),
Schardin's shock–wedge [shock diffraction](/benchmarks/shock-diffraction.md),
the subsonic and supersonic inviscid
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md), and the sonic-boom
signature of the LM1021-01 model on a 5.3 M cell mesh. Extended bounds flag
far fewer cells in smooth regions. MOOD flags smooth extrema, and the SD
over-flags smooth scalar profiles. The hybrid approaches DG accuracy as the
mesh is refined, at 1.4–1.5 times the cost of pure DG on coarse meshes and
about 1.05 on fine ones.

# Version read

The version of record (Elsevier typeset, open access CC BY; received 27 Jul
2022, accepted 3 Nov 2022, online 9 Nov 2022), 33 pages: main text pp. 1–26,
Appendices A–C pp. 26–31, references pp. 31–33. Page 1 prints the DOI and
matches the Crossref card. No identity problem. The datasets are deposited
under doi:10.17862/cranfield.rd.21436389 (printed).

# Key claims

Notation of the Notation map: $N$ is the polynomial degree, $\phi^{(k)}_i$
the Taylor basis function $k$ of cell $i$ ($k=0,\dots,\mathcal K$), $u^k_{h,i}$
the DG degrees of freedom, $\tilde a_k$ the CWENOZ coefficients, $d_s$ the
linear weights, $\alpha_s$ and $\omega_s$ the nonlinear weights and $\beta_s$
the smoothness indicators of stencil $s$ ($s=1$ the central one).

1. The hybrid scheme checks the unlimited DG solution at every RK stage. Only in troubled cells it replaces the modes $k=1,\dots,\mathcal K$ by the CWENOZ coefficients $\tilde a_k$ and keeps $u^0_{h,i}=\bar u_i$; this preserves conservation, because the higher Taylor modes have zero cell mean (§2.4, Eq. (33)). **Derived**
2. Normalizing the Taylor basis by $h_i$, the square root of the cell volume, improves the conditioning of the mass matrix. Without it the authors "could not achieve higher than 4th of accuracy" on the meshes and tests tried (§2.1, after Eq. (6)). **Stated** (no data shown)
3. The FV reconstruction is solved in physical space, without the transformation to a reference space of the authors' earlier work (§2.2.1). **Stated**
4. The stencils come from the stencil-based compact algorithm with $M=2\mathcal K$ neighbours. The overdetermined least-squares system is solved by QR and its Moore–Penrose pseudo-inverse is stored (§2.2.1, Eqs. (13)–(17)). **Stated**
5. CWENOZ weights: $\alpha_s=d_s\big(1+\tau/(\epsilon+\beta_s)\big)$, $\omega_s=\alpha_s/\sum_l\alpha_l$, with $\tau=\big(\sum_{s=2}^{s_t}\lvert\beta_s-\beta_1\rvert/(s_t-1)\big)^{b_\tau}$, $\epsilon=10^{-14}$ and $b_\tau=4$. The linear weights are $d_1=1-1/d_1'$ and $d_s=(1-d_1)/(s_t-1)$ for $s\ge2$, with $d_1'=10^7$; any $d_1'>10^3$ gives the design order (§2.2.2, Eqs. (22)–(25); §3.1). **Stated**
6. An extra safety check on the FV reconstruction requires positive density and pressure and $\lvert\rho_{il,\alpha}-\rho_i\rvert<0.8\rho_i$, $\lvert p_{il,\alpha}-p_i\rvert<0.8p_i$ at every face quadrature point. A failure switches the cell to second-order MUSCL or first-order Godunov. The switch was never activated in the paper's tests (§2.4, Eq. (34)). **Stated**
7. On the isentropic vortex, pure DG reaches close to design order, while CWENOZ FV of the same polynomial order reaches it only on finer meshes. For quadrilaterals with $N=4$, the DG $e_{L^2}$ falls from $2.97\times10^{-4}$ to $1.14\times10^{-9}$ from 8 to 64 edges, the FV one from $7.64\times10^{-2}$ to $7.20\times10^{-4}$ (Table 1). **Shown**
8. Strict MOOD flags cells in the core of the smooth isentropic vortex (Fig. 4). The troubled-cell percentage drops from 26–46 % on the coarsest meshes to 0.08–0.16 % on the finest (Table 1). **Shown**
9. The hybrid costs about 1.4–1.5 times pure DG when many cells are troubled, and about 1.05 times on finer meshes with few troubled cells (§3.1; Table 1 CPU column, 1.01 to 1.56). **Shown**
10. On unstructured meshes the extra cost is negligible as long as the troubled-cell fraction stays within 20 % (Appendix B). **Shown** (Table B.3)
11. With all cells artificially flagged, the hybrid keeps the design order on smooth advection on quadrilaterals ($O_{L^2}$ 3.01, 4.04 and 4.99 for $N=2,3,4$), with accuracy comparable to pure FV (Table B.4). **Shown**
12. Convergence of the hybrid with active detectors is "practically difficult to determine … in a consistent way", because refinement lowers the troubled fraction. This explains rates above design order, up to 6.89 for $N=4$ with strict MOOD (Appendix B, Table B.3). **Shown**
13. The SD flags most cells in smooth scalar advection, up to 100 % for $N=4$ on coarse meshes, whereas strict MOOD flags few cells near the peaks (Appendix B, Table B.3). **Shown**
14. Extended bounds flag fewer cells than limited bounds, above all in smooth regions; limited bounds flag too many cells and over-diffuse the profiles (§3.2, Figs. 6–7; Appendix C, Fig. C.26; §3.3). **Shown**
15. In the solid-body rotation the troubled-cell fraction decreases as the order increases, which the authors attribute to the subcell resolution of DG (§3.2, Fig. 6). **Shown**
16. Re-checking the cells at every RK stage, or freezing the flag for the step, makes a negligible difference (§3.2, Fig. 7). **Shown**
17. Strict MOOD with extended bounds is the best compromise in square-wave advection: DG accuracy without oscillations. It gives results similar to relaxed MOOD with limited bounds (Appendix C, Figs. C.25–C.26). **Shown**
18. Shu–Osher on 2D triangles ($h=0.070$): at third order the hybrid improves markedly on pure FV. At higher order pure FV agrees better with the reference than the hybrid with sensitive indicators, because the solver falls back to FV more often. NAD flags erratically, and the SD flags only the shock region (§3.3, Figs. 8–9). **Shown**
19. Double Mach reflection with DG ($N=3$)–CWENOZ4 on about 150 000 triangles: only the less sensitive relaxed MOOD resolves the slip-line roll-up, while SD and strict MOOD flag larger regions and diffuse it. A curved Mach stem appears with all indicators; the authors attribute it to carbuncle sensitivity and shock–grid misalignment. Reconstructing primitive instead of conserved variables reduces it (shown for the SD) (§3.4, Figs. 10–11). **Shown**
20. Schardin's problem: the hybrid variants resolve more structures and acoustic waves than pure FV-CWENOZ5, with troubled cells below 0.4 % ($N=3$) and 0.2 % ($N=4$) throughout (§3.5, Figs. 13–15). **Shown**
21. Inviscid subsonic Taylor–Green vortex on $64^3$ hexahedra: the hybrid (SD, $C_k=0.4$) is closer than pure FV to the DNS of Brachet et al. in kinetic energy and dissipation rate, and follows the Kolmogorov slope over a wider range. The modal DG part shows aliasing errors, but the run does not crash without over-integration, modal filtering or split-form fluxes (§3.6, Fig. 17). **Shown**
22. Supersonic Taylor–Green vortex ($M_{\mathrm{ref}}=1.25$, $C_k=0.2$): the troubled-cell fraction rises suddenly between $t=5$ and $12$ and decreases with refinement. The kinetic energy agrees closely with the $512^3$ WENO5 reference of Lusher & Sandham (§3.7, Fig. 18). **Shown**
23. Sonic boom of the LM1021 ($M_\infty=1.6$, the coarsest workshop mesh of 5.3 M cells): the hybrid DG ($N=2$)–CWENOZ3 matches the measured pressure signature 31.8 inches below the model better than FV-CWENOZ3, with only 45 cells across the model at that distance (§3.8, Fig. 22). **Shown**
24. Fine tuning of the DG-to-FV switching is "not a necessity" when the FV scheme has the same order as DG; with an order mismatch, e.g. a second-order FV scheme, it is mandatory (§4). **Stated**
25. [Subcell limiters](/methods/subcell-finite-volume-limiting.md) keep more DG information, but are problematic on meshes of arbitrary elements with transition layers or poor elements, and can restrict the time step; they have been extended to Voronoi meshes (§2.4). **Stated**
26. A modal basis of degree $N$ in $d$ dimensions has $\frac1{d!}\prod_{l=1}^d(N+l)$ degrees of freedom; the authors say the count "increases exponentially as the order is increased" (§2.1, Eq. (5)). **Stated** (see Printed slips)

# Printed slips

- Eq. (5) against Eq. (2): Eq. (2) sums $k=0,\dots,K$, i.e. $K+1$ basis functions, while Eq. (5) calls $K(r,d)$ "the number of DOFs". For $r=1$, $d=2$ Eq. (5) gives 3, the number of functions $\{1,x,y\}$, i.e. $K+1$ with $K=2$. Eq. (5) is also a polynomial of degree $d$ in $r$, not exponential as the text says *(compiler check, not in the sources)*.
- Eq. (9) is $M_i\,dU_i/dt+R_i(U_i)=0$, while the RK stages (29)–(31) add $+\Delta t\,M^{-1}R_i$: the sign of the residual is inconsistent between the two (the FV form (10) carries the minus sign).
- §3.1: "Temperature and density are defined as $T=p/\rho$, and $S=p/\rho^\gamma$": $S$ is the entropy, not the density.
- §3.1: "The simulation is performed for 10 periods", but errors are taken at "final time $t=10$". With background velocity $(1,1)$ on the periodic $[0,10]^2$ box one period is $t=10$ *(compiler check, not in the sources)*.
- §3.1, §3.2, §3.4, App. B: "$\lambda_1=10^7$" is the non-normalized weight $\lambda_1'$ of Eq. (24); the prime is dropped.
- §3.2: the domain is said to be "again a $[0,10]\times[0,10]$ square", but the rotation centre $(0.5,0.5)$, the shape centres between 0.25 and 0.75 and $r_0=0.15$ belong to a unit square. Appendix C likewise advects a profile on $[0.2,0.8]$ "for one period $t=1$" on a domain printed $[0,10]^2$, and prints the 2D condition as "$(x,y)\in[0.2,0.8]$".
- §2.5 attributes the NAD margins $\alpha=10^{-3}$ and $10^{-1}$ to refs. [71] and [40]; Appendix C attributes them to [27] and [28].
- Table 1, quadrilateral mesh, $N=4$, 32 edges, DG $O_{L^\infty}$: printed 6.69, while $\log_2(6.99\times10^{-5}/5.63\times10^{-7})=6.96$ *(compiler check, not in the sources)*.
- §3.5 and Fig. 14 name the pure FV variant FV(CWENOZ5); the Fig. 15 caption names it FV(CWENOZ4).
- §3.7 says the $128^3$ mesh was run "with a fourth-order DG-FV scheme", but Figs. 19–20 show DG($P_4$)-FV(CWENOZ5) on $128^3$.
- Eq. (33) text: "we simply set $U^j_{h,i}=\tilde a_k$" mixes the indices $j$ and $k$.
- References: [14] prints a phantom author "O.F.C. Laws"; the authors and volume of [7] are garbled; [45] fuses "Azure" into the last author's name; [11] prints "B. Enquist".
- Typos: "his result" (§3.8), "overintergration" (Fig. 17 caption).

# Notation map

| Maltsev et al. 2023 | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf U$, $\mathbf F=(\mathbf f,\mathbf g,\mathbf h)$ | $u$, $f^{(d)}$ | conserved variables and flux tensor |
| $r$ (polynomial degree), $P_r$ | $N$, $\mathbb P^N$ | order $N+1$; **collision**: registry $r$ is the WENO stencil size |
| $K$ (highest basis index) | $\mathcal K$ (local) | **collision** with the TENO stencil size $K$ and the element $K$ |
| $\phi^k_i$ | $\phi^{(k)}_i$ (local) | Taylor basis, zero mean for $k\ge1$; not the volume fraction $\phi_k$ |
| $U^k_{h,i}$; $\bar U_i$ | $u^k_{h,i}$; $\bar u_i$ | DG degrees of freedom; cell average |
| $h_i$ | $h_i$ (local) | square root of the cell volume, also the characteristic length of Eq. (32) |
| $M_{bk}$, $R_i$ | $M$, $R_i$ (local) | mass matrix (not diagonal here), residual; **$R$ is the eigenvector matrix in the registry** |
| $\tilde F_{n_{im}}$, $U_{n_{im},L}$, $U_{n_{im},R}$ | $h(u^-,u^+)$ | HLLC normal flux between own (L) and neighbour (R) traces |
| $\omega_g$, $\omega_\alpha$ | $\mathsf w_g$, $\mathsf w_\alpha$ | quadrature weights; **collision** with the WENO weights $\omega_s$ |
| $M$ (stencil size), $S^c_i$ | $M$ (local), $S_s$ | $M=2\mathcal K$ cells; stencils numbered from 1 (central), **unlike the registry's $S_0$** |
| $\lambda_s$, $\lambda_1'$ | $d_s$, $d_1'$ | linear weights; non-normalized central weight |
| $\tilde\omega_s$, $\omega_s$ | $\alpha_s$, $\omega_s$ | unnormalized and normalized nonlinear weights |
| $\mathcal{SI}_s$, $\mathcal{OI}_{kq}$ | $\beta_s$, $\mathcal{OI}_{kq}$ | smoothness indicator and its oscillation-indicator matrix |
| $\tau$ | $\tau$ | global WENO-Z-type indicator, but here a mean absolute difference raised to $b$, not $\lvert\beta_0-\beta_2\rvert$ |
| $b$ | $b_\tau$ (local) | exponent on $\tau$, not the registry $q$; **collision** with the TENO-A constant $b$ |
| $\epsilon$ | $\epsilon$ | $10^{-14}$; agrees |
| $\epsilon$ (§3.1, value 5) | $\mathcal E$ | vortex strength |
| $C_k$ | $C_k$ (local) | shock-detector threshold, as for KXRCF on the [troubled-cell page](/definitions/troubled-cell-indicator.md); not the TENO $C_T$ |
| $\alpha$, $\delta$ (NAD) | $\alpha_{\mathrm N}$, $\delta_{\mathrm N}$ (local) | relaxation parameter and margin; **collision** with $\alpha_k$ and the TENO flag $\delta_k$ |
| $U^{minL}$, $U^{maxE}$, … | kept | limited and extended bounds |
| MOOD$^O$, MOOD$^R$; subscripts $L$, $X$ | kept | strict ($\alpha=10^{-3}$) and relaxed ($10^{-1}$) NAD; limited and extended bounds |
| CFL, $S_i$ | $\nu$, $a_i$ | Courant number (with the factor $1/(2r+1)$ in $\Delta t$); maximum wave speed |
| $T$, $S$ (§3.1) | $p/\rho$, $p\rho^{-\gamma}$ | temperature-like and entropy-like variables of the vortex |
| $e_{L^2}$, $e_{L^\infty}$, $O_{L^2}$ | kept | volume-weighted errors and observed orders |

# Reference list

The paper prints 99 references, numbered [1]–[99]. The list is merged
complete into the [bibliography](/bibliography.md), with `citedby` including
`maltsev-2023`. [3] and [93] print no venue, and [31] is an undated web page
of the UCNS3D code (accessed 5 May 2022). The authors and volume of [7] are
garbled and are entered as printed with a note; the phantom author of [14]
is dropped with a note, and [14] carries no volume or pages; [45] is entered
with "Azure" in the title. Several Elsevier items print a volume but no
article number ([13], [28], [40], [53]–[56], [58], [96]). Ref. [40]
(Tsoutsanis & Dumbser 2021, Comput. Fluids 225) and ref. [56] (Tsoutsanis
et al. 2021, J. Sci. Comput. 89) must be matched by title to the bundle's
keys: [56] is the ingested source
[Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md). The Tsoutsanis 2016
works [48]–[50] likewise take the bundle's suffixes by title, not this
paper's printed order.

# Pages created or updated

Chunk 6 (2026-10-23), cited further in chunks 7–12 (2026-10-23/30). This source is cited on:

* [Central WENO (CWENO)](/methods/cweno.md)
* [Discontinuous Galerkin method](/methods/discontinuous-galerkin.md)
* [Double Mach reflection](/benchmarks/double-mach-reflection.md)
* [Gradient reconstruction on unstructured meshes](/methods/unstructured-gradient-reconstruction.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [MOOD a posteriori limiting](/methods/mood-a-posteriori-limiting.md)
* [Scale and affine invariance](/properties/scale-invariance.md)
* [Shock diffraction](/benchmarks/shock-diffraction.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [Solid-body rotation](/benchmarks/solid-body-rotation.md)
* [Subcell finite-volume limiting for DG](/methods/subcell-finite-volume-limiting.md)
* [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
* [UCNS3D](/software/ucns3d.md)
* [WENO limiters for discontinuous Galerkin](/methods/weno-limiter-dg.md)
* [WENO-Z weights](/methods/weno-z.md)
