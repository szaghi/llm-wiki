---
type: Source
title: "Kokkinakis & Drikakis (2025b) — Overcoming the hyposonic limit of the compressible Navier–Stokes equations in turbulent flow simulations"
description: "Introduces NEHA, a low-Mach correction that limits the face-normal and face-tangential reconstructed velocities with separate Mach-number factors, and compares it with the Thornber et al. correction and normal-only and tangential-only variants in ninth-order WENO implicit LES of a Mach 0.2 channel at Re_tau 395 in CNS3D."
resource: "doi:10.1063/5.0260930"
source_kind: paper
authors: [Kokkinakis I.W., Drikakis D.]
year: 2025
venue: "Phys. Fluids 37:035196"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2025_Crossref_Physics_of_Fluids_Kokkinakis_Overcoming_the_hyposonic_limit_of_the_compressible_NavierSto.pdf"
tags: [implicit-les, weno, numerical-dissipation, finite-volume, channel-flow, compressible]
timestamp: 2026-10-29T05:08:00Z
---

# Summary

Kokkinakis & Drikakis (2025b) address the accuracy loss of compressible
Godunov finite-volume solvers at low Mach number (the "hyposonic limit")
in wall-bounded [implicit LES](/definitions/implicit-les.md). Thornber et
al. (2008) introduced a low-Mach correction (LM) that, after
reconstruction and before the Riemann solver, blends the left and right
reconstructed velocities toward their mean by a factor
$z=\min(1,\max(M_L,M_R))$. The authors' earlier work with ninth-order
[WENO](/methods/weno-scheme.md) (W9) found LM "excessively dispersive",
and Simmonds et al. (2018) limit only the face-normal velocity (LMn). The
new variant, NEHA (Numerical Enhancement for Hyposonic Accuracy), limits
both the face-normal and the face-tangential velocity, each with a factor
built from its own Mach number; LMt and LMtn (tangential only, with the
tangential or the normal Mach number) are diagnostic variants. The
argument for separate factors is that on a hexahedral cell the normal
velocity of one face family is tangential on the others.

All variants run in [CNS3D](/software/cns3d.md) (block-structured finite
volumes, HLLC with an adaptive non-iterative pressure estimate, W9 in
primitive variables with stencil normalization, relative
total-variation limiting, Feng-type mapping and order reduction,
five-stage fourth-order SSP Runge–Kutta) on a
[turbulent channel](/benchmarks/turbulent-channel-flow.md) at
$Re_\tau\simeq395$, $M_b=0.2$, on $64^3$ cells (W9 also on $128^3$),
against the incompressible [DNS](/definitions/direct-numerical-simulation.md)
of Moser, Kim & Mansour (1999). Mean $Re_\tau$: W9 372.5, LM with
velocity-magnitude Mach 367, LM with normal Mach 402.2, LMn 383, LMt 372,
LMtn 371.1, NEHA 392, W9 on $128^3$ 391, DNS 392.24. NEHA on $64^3$
brings $Re_\tau$ and the [mean velocity](/definitions/law-of-the-wall.md)
within 1% of the DNS, removes the dispersed vortices LM produces, beats
W9 on $128^3$ below $y^+=40$ and costs under 10% extra. The authors
separate excess [numerical dissipation](/properties/numerical-dissipation.md)
(W9 alone) from excess dispersion (W9 with LM). Evidence is numerical,
on one case and one grid for the variant comparison.

# Version read

Version of record (AIP; submitted 28 January 2025, accepted 27 February
2025, published online 20 March 2025), 16 PDF pages (AIP cover plus
article pages 035196-1 to -15), all read; equations and figures of
article pp. 3–10 checked visually. Page 1 matches the metadata. Numbering
on this page is that of the version read.

# Key claims

Page-local symbols: $u^\perp=\boldsymbol u\cdot\hat{\boldsymbol n}$ and
$\boldsymbol u^\parallel=\boldsymbol u-u^\perp\hat{\boldsymbol n}$ the
face-normal and face-tangential velocity at a cell face; $M^\perp$,
$M^\parallel$ the Mach numbers built on them; $z$, $z^\perp$,
$z^\parallel=\min(1,\max(M_L,M_R))$ with the magnitude, normal or
tangential Mach number; $\overline{Re}_\tau$ the time mean of the
resolved $Re_\tau(t)$; $B_{\mathrm{TV}}$ the second limiter threshold.

1. High-order WENO (e.g. W9) "do not inherently guarantee high accuracy in low-Mach turbulent boundary layers, mainly when applied to coarser mesh resolutions"; excess dispersion is "partly attributed" to the large weight of the central stencil in smooth regions. §I. **Stated**
2. Because high-order WENO is already nearly central, LM toward central reconstruction "makes the overall numerical scheme excessively dispersive" (citing the authors' Ref. 21), yet without LM even W9 fails for $M\lesssim0.01$ regions on coarse meshes (citing Ref. 22): a "dilemma". §I. **Stated**
3. LM applied directly on unstructured grids creates artifacts (Simmonds et al.), who modify only the face-normal velocity, a concept from the LMRoe/L2Roe solver of Oßwald et al. §I. **Stated**
4. NEHA limits both $u^\perp$ and $\boldsymbol u^\parallel$, each scaled by its own Mach number through separate $z$ functions. §V, Eqs. (34)–(36). **Derived** (definition; contribution)
5. On a quadrilateral or hexahedral element the normal velocity at a face of one direction is tangential at the faces of the others, so separate $z$ functions make the limiting "consistent" across the faces of the element. §V, Fig. 3. **Stated**
6. Using $z^\perp$ instead of the velocity-magnitude Mach number further decreases numerical dissipation, since $\lvert\boldsymbol u\rvert\ge\lvert u^\perp\rvert$, especially at wall-normal and spanwise faces in a boundary layer. §IV A, Eq. (24). **Derived**
7. Density and pressure are not modified by the correction (to avoid diffusing stationary contacts, citing Thornber et al.); internal energy is kept and total energy recomputed with the limited velocities. §IV A. **Stated**
8. On $64^3$, W9 alone gives $\overline{Re}_\tau\simeq372$, "almost 6% error" relative to 395; Table II: 372.5, RMS 4. §VI, Table II. **Shown**
9. W9 on $128^3$ resolves the channel "accurately": 391 (RMS 2.6). §VI, Table II. **Shown**
10. LM with $z^\perp$ over-predicts $\overline{Re}_\tau$ (402.2, "overshoot of nearly 2%"), its dispersion reaching the near-wall region; with the velocity-magnitude Mach number (Ref. 21) LM under-predicts (367). Both rows are called the "original LM" in the text. §VII, Table II. **Shown**
11. LM produces "fuzzy", dispersed vortices around mid-height; LMn and LMt suppress them; NEHA gives the closest $Q_A$-isosurface agreement with the $128^3$ solution. §VII, Fig. 6. **Shown** (qualitative)
12. LMn 383 (RMS 3.3), LMt 372 (RMS 3.5), LMtn 371.1 (RMS 3.2): tangential limiting alone gives "only a minimal improvement over the unmodified W9", and $z^\parallel$ against $z^\perp$ in LMt makes no discernible difference. §VII, Table II. **Shown**
13. NEHA: $\overline{Re}_\tau\simeq392$ (RMS 2.96), "in excellent agreement" with the DNS value 392.24. §VII, Table II. **Shown**
14. LMt alone barely changes $\overline{Re}_\tau$, yet combined with LMn (NEHA) it does better than LMn alone, explained by finer resolved structures. §VII. **Shown**
15. Mean velocity in wall units: W9 departs from DNS from $y^+\approx10$ upward; LM over-corrects; LMt follows W9; LMn improves; NEHA gives "almost perfect alignment". §VII, Fig. 8. **Shown**
16. Streamwise-velocity skewness: all variants except LMt improve below $y^+=10$; LM over-estimates near-wall skewness; NEHA agrees best "for most of the turbulent boundary layer profile height". §VII, Fig. 9. **Shown**
17. Flatness: W9 and LMt under-predict it in the viscous sublayer and over-predict it in the log region; LM over-estimates it in the sublayer; NEHA is best near the wall. §VII, Fig. 10. **Shown**
18. NEHA on $64^3$ is more accurate than W9 on $128^3$ for $y^+<40$; the finer mesh is "slightly better for $y^+>40$". §VIII. **Shown**
19. The mean Mach number falls below 0.1 near the wall and approaches 0.01 at the wall on $64^3$. §VIII, Fig. 4. **Shown**
20. NEHA overhead is below 10%, LM about 5%, relative to W9 with HLLC; with second-order MUSCL the overhead is below 20%. §VIII. **Stated** (no timing table or hardware)
21. NEHA brings $\overline{Re}_\tau$ and mean velocity within 1% of DNS, against about 5.7% for W9 alone. §VIII. **Shown**
22. Stencil normalization (Eq. 5) prevents negative smoothness indicators, reduces numerical dissipation and simplifies the total-variation limiting; it does not affect MUSCL limiters. §III B. **Stated**
23. The Taylor et al. threshold $P_{\mathrm{TV}}=5$ is too high together with the other WENO augmentations; $P_{\mathrm{TV}}=2$ is used "for the sake of numerical stability", with $B_{\mathrm{TV}}=0.2(r-1)$. §III B. **Stated**
24. The order-reduction test (Eq. 15, threshold 0.7) is "never met" in this quasi-incompressible channel. §III B. **Stated**
25. NEHA makes compressible solvers usable across Mach regimes, from very low subsonic to hypersonic, with automotive, meteorological, multiphase-pipeline and engine applications claimed. §VIII. **Stated** (no evidence beyond the channel)

# Printed slips

- **Eqs. (21)–(22), and the same pattern in (28)–(29), (31)–(32), (35)–(36):** $\boldsymbol u^{LM}_L=(\boldsymbol u_s-\boldsymbol u_u)/2$, $\boldsymbol u^{LM}_R=(\boldsymbol u_s+\boldsymbol u_u)/2$ with $\boldsymbol u_s=\boldsymbol u_L+\boldsymbol u_R$, $\boldsymbol u_u=(\boldsymbol u_L-\boldsymbol u_R)z$. *(Compiler check, not in the sources: at $z=1$, where the text says the correction switches off, these give $\boldsymbol u^{LM}_L=\boldsymbol u_R$ and $\boldsymbol u^{LM}_R=\boldsymbol u_L$.)*
- **Eq. (11):** numerator printed $(\Omega^r_k+C^r_k)^{K+1}A$ while the text says $A=1$, $K=2$ "results in the original mapping function". *(Compiler check: at $\Omega^r_k=C^r_k$ the printed form does not return $C^r_k$; with a minus sign in the numerator it does.)*
- **Eq. (5):** $g_{\min}=\mathrm{minval}(S^G)-1$, $g_{\max}=\mathrm{maxval}(S^G)-q_{\min}$, with $q_{\min}$ not defined; the text says the normalized stencil has maximum 1. *(Compiler check: the maximum of $(S^G-g_{\min})/g_{\max}$ is 1 only if $g_{\max}=\mathrm{maxval}(S^G)-g_{\min}$.)*
- **§III B:** an $r$th-order ENO gives a "$(2r-1)$th-order WENO", and later $r$ is "the order of the polynomials used in the $2(r-1)$th-order WENO".
- **Eq. (8):** "if $[R(TV)<A^{TV}_{RL}\ \max(TV_k)<B^{TV}_{RL}]$", described as "two conditions", with no conjunction printed.
- **Domain:** text $L_x=6\pi\delta$; the Fig. 5 schematic labels the streamwise extent $2\pi$.
- **Averaging time:** "$900\,u_b/\delta$, which corresponds to just over 21 flow-throughs based on … $L_x$ and $u_b$"; the unit is printed $u_b/\delta$. *(Compiler check, not in the sources: a time $900\,\delta/u_b$ over the flow-through time $L_x/u_b$ with $L_x=6\pi\delta$ gives $900/(6\pi)=47.7$ flow-throughs.)*
- **Initial perturbation:** "by 5% of the local streamwise velocity" and "($s=10\%$)" in §VI A.
- **Coordinate origin:** Eq. (38) uses $y\in[0,2\delta]$ and Eq. (41) evaluates $\tau_w$ at $y=0$; Eqs. (43)–(44) put $y=0$ at mid-height and the walls at $y=\pm\delta$.
- **§IV C:** titled "Third formulation: 'LMt'", the text says "the second LM formulation will be labeled LMt".
- **Symbols:** $s_L$, $s_R$, $\overline{\rho s}$ of Eqs. (17)–(18) are not defined, while $\bar c$ is defined and not used in Eq. (17); $B$ lacks the subscript $K$ of $B_K$; $g_K$ is written with $p$ for $p_*$; $z$ is both $(\gamma-1)/(2\gamma)$ and the LM factor, $q$ both the primitive vector and the wave-speed factor, $K$ both the mapping exponent and the side index, $Q$ both the pressure ratio and the mass flux; §IV A once writes "$z_n$".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $IS_k$, $\epsilon$ | $\mathrm{IS}_k$, $\epsilon$ | $\epsilon=10^{-41}$ |
| $C^r_k$, $\Omega^r_k$, $\omega^r_k$, $\tilde\omega^r_k$ | $d_k$, $a_k$, $\mathsf w_k$, mapped $\mathsf w_k$ | |
| $A$, $K$ (Eq. 11) | mapping parameters 1, 2 | **collision:** $K$ is also the side index $L$, $R$ |
| $TV_k$, $R(TV)$, $A^{TV}_{RL}$, $B^{TV}_{RL}$ | $TV_k$, $R_{\mathrm{TV}}$, $P_{\mathrm{TV}}$, $B_{\mathrm{TV}}$ (page-local) | relative total-variation limiter |
| $r$ | $r$ | W9: $r=5$ |
| $u^\perp$, $\mathbf u^\perp$, $\mathbf u^\parallel$, $\hat n$ | $u^\perp$, $u^\perp\hat{\boldsymbol n}$, $\boldsymbol u^\parallel$, $\hat{\boldsymbol n}$ (page-local) | |
| $z$, $z^\perp$, $z^\parallel$; $M_K$, $M^\perp_K$, $M^\parallel_K$ | page-local | LM factors and side Mach numbers |
| $\boldsymbol\tau$, $\lambda=-2\mu/3$ | $\sigma_{ij}$ | Stokes hypothesis |
| $q=[\rho,\mathbf u,p]^T$ | primitive vector | **collision** with the HLLC wave-speed factor $q_K$ |
| $Q$, $Q_{user}$ | pressure ratio, threshold 2 | **collision** with the mass flux $Q$ of Eqs. (39)–(41) and the $Q$-criterion ($Q_A$) |
| $\delta$ | $\delta$ | channel half-height |
| $u_\tau$, $Re_\tau$, $\overline{Re}_\tau$ | $u_\tau$, $Re_\tau$, $\overline{Re}_\tau$ (page-local) | the overbar is a time mean here, not the LES filter |
| $u_b$, $Re_b$, $M_\infty$ | $u_b$, $Re_b$, $M_b$ | bulk quantities; $Re_b\simeq6887$ |
| $\langle\cdot\rangle_{xz}$ | $\langle\cdot\rangle$ | plane average, then time average |
| $S_u$, $F_u$ | skewness and flatness of $u'$ | page-local |
| W9, LM, LMn, LMt, LMtn, NEHA | as printed | |

# Reference list

70 printed references, numbered AIP style, no DOIs printed, all parsed.
The list is merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug. Ref. 36 is an undated web page (accessed 2 February
2025), keyed with the citing year; ref. 54 (Harten et al., ENO III) is
printed as J. Comput. Phys. 131:3–47 (1997); ref. 15 prints the authors
"X. s Li and C. w Gu". Same-author same-year works (Ritos 2018, Drikakis
2002, Li 2008, Lenormand 2000) are suffixed in printed order. No key falls
on a bundle source of a different work, and no item is printed twice.

# Pages created or updated

Chunk 15 (2026-10-28). This source is cited on:

- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Vortex identification criteria](/definitions/vortex-identification-criterion.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [CNS3D](/software/cns3d.md)
