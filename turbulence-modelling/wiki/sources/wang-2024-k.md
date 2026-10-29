---
type: Source
title: "Wang et al. (2024d) — Wall-modeled large eddy simulation in the immersed boundary-lattice Boltzmann method"
description: "Implements an equilibrium wall-stress model in a GPU immersed-boundary lattice Boltzmann solver with diffusive- and sharp-interface boundaries and MRT or recursive-regularized collisions, and tests it on channel flow up to Re_τ 5200, the DARPA SUBOFF hull, the Ahmed body and the cylinder drag crisis, recommending the diffusive interface for external and the sharp one for internal flows."
resource: "doi:10.1063/5.0198252"
source_kind: paper
authors: [Wang L., Liu Z., Jin B.R., Huang Q., Young J., Tian F.-B.]
year: 2024
venue: "Phys. Fluids 36:035167"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2024_Crossref_Physics_of_Fluids_Wang_Wall-modeled_large_eddy_simulation_in_the_immersed_boundary-.pdf"
tags: [wmles, immersed-boundary, lattice-boltzmann, bluff-body, gpu]
timestamp: 2026-10-29T07:38:00Z
---

# Summary

Wang et al. (2024d) put an
[equilibrium wall model](/methods/equilibrium-wall-model.md) into a GPU
[immersed-boundary](/methods/immersed-boundary-method.md)
[lattice Boltzmann](/methods/lattice-boltzmann-method.md) solver for
[wall-modelled LES](/methods/wall-modelled-les.md), in two forms. With the
diffusive-interface boundary (DIB: the penalty, or feedback, method of
Kim & Peskin with Peskin's four-point kernel), a slip velocity is imposed
at a forcing point a small distance off the wall, after Shi et al. (2019);
with the sharp-interface boundary (SIB, after Tessicini et al. and Yang &
Balaras), the velocity of the first off-wall fluid node is reconstructed
from the wall model. The wall model integrates the thin-boundary-layer
equation without its right-hand side between the wall and an LES matching
point, with a van Driest-damped mixing length
([law of the wall](/definitions/law-of-the-wall.md)); the closure is the
[Smagorinsky model](/methods/smagorinsky-model.md) with $\Delta$ the lattice
spacing, and D3Q19 multiple-relaxation-time (MRT) and recursive regularized
(RR) collisions are compared.

The tests are the [turbulent channel](/benchmarks/turbulent-channel-flow.md)
at $Re_\tau=1000$, 2000 and 5200 on a uniform $\delta/20$ mesh, the DARPA
SUBOFF bare hull at $Re_L=1.2\times10^6$, the
[Ahmed body](/benchmarks/ahmed-body.md) with a 35° slant at
$7.85\times10^5$, and the
[circular cylinder](/benchmarks/circular-cylinder-wake.md) from
$Re_D=3900$ (no wall model) through the drag crisis to $10^6$; references
include [DES](/methods/detached-eddy-simulation.md) and
[EARSM](/methods/explicit-algebraic-reynolds-stress-model.md) drag values
of Guilmineau et al. The SIB wall model gives good channel profiles while
the DIB, through extra near-wall
[numerical dissipation](/properties/numerical-dissipation.md), overestimates
the friction velocity; the DIB drives separation more easily and captures
the cylinder drag crisis, which the SIB misses. MRT is less dissipative
than RR but noisy, fails on the SUBOFF friction and is unstable for the
Ahmed body. The recommendation is the DIB wall model for external flows,
the SIB one for internal flows, and RR over MRT; the GPU code is 6–10
times faster than the CPU code. The cost motivation cites the
[grid-point estimates](/results/les-grid-point-requirements.md) of Choi &
Moin (2012). Evidence is numerical comparison with DNS, experiments and
published simulations; a mesh study is made for the channel only.

# Version read

Version of record (AIP, CC BY; submitted 17 January 2024, accepted 5 March
2024, online 25 March 2024), 14 PDF pages (an AIP cover page and article
pages 035167-1 to -13), all read; the equations of pages 3–6 and 12 were
read visually. Pages 1–2 match the metadata. Equation, table, figure and
section numbers are those of this version.

# Key claims

Page-local symbols: $c_s$ the lattice sound speed $\Delta x/(\sqrt3\Delta t)$;
$f_q$, $f_q^{\mathrm{eq}}$, $f_q^{\mathrm{neq}}$, $\boldsymbol c_q$, $w_q$,
$\tau_{\mathrm{LB}}$ the lattice distributions, discrete velocities, weights
and relaxation time (registry §11); $d_b$ the off-wall distance of the
forcing (DIB) or first off-wall (SIB) point $b$, and $h_{\mathrm{wm}}$ the
wall distance of the matching point $c$ as used in Eqs. (20)–(21); $\phi_4$
Peskin's four-point kernel; $\alpha_{\mathrm{fb}}$, $\beta_{\mathrm{fb}}$ the
feedback gains; $h_{\mathrm A}$ the Ahmed-body height; $\theta_{\mathrm{sep}}$
the separation angle.

1. The wall model is implemented in both a diffusive-interface and a sharp-interface IBM within an IB-LBM; earlier WMLES in IB-LBM (e.g. [Cai et al. (2022)](/sources/cai-2022.md), ref. 30) were mostly sharp-interface, leaving the DIB not fully evaluated, which is the stated motivation (§I). **Stated**
2. The closure is the Smagorinsky model $\nu_t=(C_s\Delta)^2\lvert\bar S\rvert$, with $C_s=0.12$ "unless otherwise specified" and $\Delta$ the lattice spacing (§II.A, Eq. 3); the channel uses $C_s=0.16$ (§III.A). **Stated**
3. The effective viscosity enters through the relaxation time, $\nu+\nu_t=(\tau_{\mathrm{LB}}-0.5)c_s^2\Delta t$; the LBM recovers the incompressible Navier–Stokes equations with second-order accuracy (§II.B, after Eq. 10). **Stated**
4. The strain rate for $\nu_t$ is computed locally from non-equilibrium moments (MRT: Eqs. A1–A3; RR: Eq. A4), not by finite differences (Appendix A). **Stated**
5. The equilibrium wall model integrates $\partial_y[(\nu+\nu_t)\partial_yu_s]=0$ from the wall to point $c$, giving $\tau_w$ by Eq. (20), solved by "Newton–Sampson" iteration; intermediate velocities follow Eq. (21), with $\nu_t$ from the van Driest mixing length, $\kappa=0.41$, $A^+=19.0$ (§II.D, Eqs. 19–22). **Stated**
6. In the DIB the forcing-point distance is suggested as $d_b=(0.1$–$0.25)\Delta x$ (after Shi et al.); in the SIB $d_b$ is the real normal distance of the first off-wall node (Fig. 1 caption). For the submarine $h_{\mathrm{wm}}=2.5\Delta s$, $d_b=0.2\Delta s$ (§III.B). **Stated**
7. SIB-WMLES of the channel on a uniform $\delta/20$ mesh ($y^+\approx50$ at $Re_\tau=1000$) predicts the mean velocity profile "very well" at $Re_\tau=1000$, 2000, 5200 against the Lee & Moser DNS; the fluctuations are underestimated, as also reported in refs. 29 and 62 (§III.A, Fig. 2). **Shown**
8. The turbulent energy is more underestimated at lower Reynolds numbers, which the authors attribute "probably" to LBM dissipation rather than to the wall model, since the averaged velocity profiles are well predicted (§III.A). **Stated** (interpretation of Shown data)
9. The power spectral density of turbulent energy at two probes in the channel at $Re_\tau=2000$ reproduces the Kolmogorov $-5/3$ law (§III.A, Fig. 3). **Shown**
10. In the channel the DIB wall model overestimates the friction velocity and underestimates the near-wall streamwise velocity "due to the high viscosity induced by the diffusive-interface method" ($Re_\tau=2000$, Fig. 4). **Shown**
11. MRT- and RR-LBM both predict the averaged channel velocity well; MRT gives slightly higher velocities at $y^+>1000$ and overestimated turbulent energy, more small vortical structures and spurious oscillations, which the authors read as less dissipation with nonphysical small structures (§III.A, Figs. 5–6). **Shown**
12. Channel mesh convergence at $Re_\tau=2000$ with $\Delta x=\delta/20$, $\delta/40$, $\delta/80$: the averaged velocity is well predicted even on the coarsest mesh and the turbulent energy converges with refinement, especially near the wall (Appendix C, Fig. 16). Mesh convergence for the other cases is "computational prohibitive" (hundreds of millions of nodes). **Shown**
13. SUBOFF bare hull at $Re_L=1.2\times10^6$ with DIB-WMLES: four mesh zones, finest $\Delta s=D/80$, the refined wake zone up to $4D$; the averaged $C_p$ and $C_f$ fall within the range of the experiment and of WRLES and WMLES references; $C_f$ is more method-sensitive than $C_p$ (§III.B, Fig. 7). **Shown**
14. On the SUBOFF hull RR-LBM reproduces the streamwise decrease of friction in agreement with flat-plate theory, MRT-LBM fails to, "probably due to the spurious oscillations of the flow near the wall"; the MRT instantaneous fields are much noisier (§III.B, Figs. 7–8). **Shown**
15. Ahmed body (35° slant, $Re=U_0h_{\mathrm A}/\nu=7.85\times10^5$, five mesh zones, finest $h_{\mathrm A}/160$, wake zone $h_{\mathrm A}/80$ up to $2h_{\mathrm A}$ downstream): velocity profiles above the slant from both DIB and SIB agree with URANS, IDDES and experiment; in the near wake DIB agrees better and SIB predicts slightly larger velocities near the bottom wall (§III.C, Fig. 11). **Shown**
16. Ahmed-body drag (Table I): DIB-WMLES $C_D=0.321$ (head/slant/back pressure drag 0.052/0.091/0.097), SIB-WMLES 0.296 (0.073/0.054/0.102), experiment (Ahmed et al.) 0.279 (0.015/0.097/0.089); Guilmineau et al. RANS-EARSM 0.437, "IDES" 0.346, DES 0.316, RANS 0.300; "Cui et al." WMLES 0.235. **Shown**
17. The DIB drives flow separation more easily than the SIB in WMLES: a stronger separation bubble near the slant with DIB, a larger bubble attached to the back with SIB (§III.C, Fig. 12), consistent with the submarine observations. **Shown**
18. The MRT-LBM "encounters stability issues" at the Ahmed-body Reynolds number (§III.C, end). **Stated** (no result shown)
19. Cylinder at $Re_D=3900$ (LES without wall model; five blocks, finest $D/160$, wake zone $D/80$ up to $2.0D$, span $4D$ periodic, streamwise domain $16D$): DIB $\langle C_D\rangle=1.02$, $St=0.215$, $\theta_{\mathrm{sep}}=88°$; SIB 0.98, 0.217, 88°; references 1.04–1.08, 0.210–0.216, 88° (Table II). **Shown**
20. Drag crisis: with the DIB wall model the drag decreases "from 0.99 to 0.28 and 0.22" between $Re_D=10^5$, $5.0\times10^5$ and $1.0\times10^6$, capturing the crisis through the backward shift of separation; the SIB wall model fails to capture the separations at high $Re_D$ and gives lower drag (§III.D, Figs. 14–15). **Shown**
21. The GPU code (MPI and CUDA, all fields resident on the GPU, streaming, macroscopic variables and collision fused in one kernel) is 6–10 times faster than the CPU code (MPI and OpenMP): channel $0.8\times10^6$ nodes, one zone, ratio 10; submarine $23\times10^6$ nodes, four zones, ratio 7; one NVIDIA V100-SXM2-32GB against a 24-core Intel Xeon Platinum 8274 (Appendix B, Table III). The lower submarine ratio is attributed to interpolation between mesh zones, and IBM interpolation and spreading also lower it. **Shown**
22. Conclusion: the DIB wall model for external, the SIB wall model for internal turbulent flows; RR-LBM outperforms MRT-LBM in stability and nonphysical noise (§IV). **Stated** (synthesis of Shown results)

The wall model in registry notation (§II.D, Eqs. 19–22), with $s$ the
wall-tangential direction and $y$ the wall distance: the equilibrium form
of the thin-boundary-layer equation, $\partial_y[(\nu+\nu_t)\partial_yu_s]=0$,
gives

$$\frac{\tau_w}{\rho}=\frac{u_s^c-u_s^w}{\int_0^{h_{\mathrm{wm}}}\frac{\mathrm dy}{\nu+\nu_t}},\qquad u_s^b=u_s^w+\frac{\int_0^{d_b}\frac{\mathrm dy}{\nu+\nu_t}}{\int_0^{h_{\mathrm{wm}}}\frac{\mathrm dy}{\nu+\nu_t}}(u_s^c-u_s^w),\qquad u_y^b=u_y^w+\frac{d_b^2}{h_{\mathrm{wm}}^2}(u_y^c-u_y^w),$$

$$\nu_t=\nu\kappa y^+\big(1-e^{-y^+/A^+}\big)^2,\qquad y^+=u_\tau y/\nu,\qquad\kappa=0.41,\ A^+=19.0,$$

iterated for $u_\tau$. The DIB enforces $u^b$ through the feedback force
$\boldsymbol F=\alpha_{\mathrm{fb}}\int_0^t(\boldsymbol U_{ib}-\boldsymbol U)\,\mathrm dt+\beta_{\mathrm{fb}}(\boldsymbol U_{ib}-\boldsymbol U)$
(gains "large positive free constants", no values), spread with
$\delta_h=\Delta x^{-3}\phi_4(x/\Delta x)\phi_4(y/\Delta x)\phi_4(z/\Delta x)$ and
$\phi_4(r)=\tfrac18(3-2|r|+\sqrt{1+4|r|-4r^2})$ for $|r|<1$,
$\tfrac18(5-2|r|-\sqrt{-7+12|r|-4r^2})$ for $1\le|r|<2$, zero beyond
(Eqs. 15–18); the DIB is described as generally first-order accurate, the
SIB as second or higher order. The equilibrium is
$f_q^{\mathrm{eq}}=w_q\rho[1+\boldsymbol c_q\cdot\boldsymbol u/c_s^2+\boldsymbol u\boldsymbol u:(\boldsymbol c_q\boldsymbol c_q-c_s^2\boldsymbol I)/(2c_s^4)]$
with D3Q19 weights $1/3$, $1/18$, $1/36$, and the forcing is that of Guo et
al. (Eqs. 9–10); RR adds the third-order Hermite terms of Feng et al. and
Jacob et al. (Eqs. 11–14). The channel is driven by a body force and its
bulk Reynolds number set from a Dean correlation (Eqs. 23–24).

# Printed slips

- **Abstract against §III.A:** the abstract says the DIB "fails in the simulation of internal flows of underestimating the wall shear stress due to its extra dissipation"; §III.A says "the diffusive-interface method over-estimate the fraction velocity" (Fig. 4), and $\tau_w=\rho u_\tau^2$ (Eq. 20).
- **Table I:** the WMLES row is "Cui et al.30", while ref. 30 is Cai, Mozaffari, Jacob & Sagaut (the §I text writes "Cai et al.30"); the row "Guilmineau et al.69 (IDES)" against the text's "DES and IDDES".
- **§III.C:** the SIB drag 0.296 is called "slightly smaller than the experimental data" (0.279, Table I); the DIB is said to predict "a larger pressure-induced drag at the head" while Table I gives the SIB a larger head drag (0.073 against 0.052; experiment 0.015).
- **MRT collision signs (Eqs. 4, 7):** $g_i(\cdot)=g_i-\Omega_i+\Delta tG_i$ with $\Omega_i=-(M^{-1}\Lambda M)_{ij}[g_j-g_j^{eq}]$. *(Compiler check, not in the sources: together they give $g_i^{\mathrm{new}}=g_i+(M^{-1}\Lambda M)_{ij}(g_j-g_j^{eq})$, a relaxation away from equilibrium for the non-negative $\Lambda$ the text states.)*
- **Eq. (24):** $g=\frac{u_\tau^2}{H}-(\overline u-\langle u_z\rangle)\delta t$. *(Compiler check, not in the sources: the first term is an acceleration, the second a velocity times a time.)*
- **After Eq. (14):** "$\delta$ is the Dirac delta function" for the $\delta_{\alpha\beta}$ of $H^{(2)}_{i\alpha\beta}=e_{i\alpha}e_{i\beta}-c_s^2\delta_{\alpha\beta}$.
- **Hermite indices:** Eq. (12) writes the second-order equilibrium term $a^{(2)}_{0,\alpha\beta}H^{(0)}_{i\alpha\beta}$, Eq. (14) defines $H^{(2)}_{i\alpha\beta}$; Eq. (A4) writes $H^{(2)}_{i\alpha\beta\gamma}$ with three indices.
- **§II.D:** "Newton–Sampson iteration"; "driest damping"; "the determination of M and S" for the relaxation matrix named $\Lambda$ in Eqs. (7)–(8) and $s$ in Appendix A.
- **Eq. (20):** $\tau_w=\nu\,\partial u_s/\partial l|_0$ (kinematic) and $\tau_w=\rho u_\tau^2$ in the same equation.
- **Fig. 1 caption against Eqs. (20)–(21):** in the DIB "$\Delta c$ is the distance between point c and point b", while Eqs. (20)–(21) integrate $\int_0^{\Delta c}$ from the wall.
- **Figs. 2, 4, 5, 16:** captioned and discussed as "turbulent energy", with the axis label $\langle v'w'\rangle/u_\tau^2$ (printed with angle brackets); the conclusions call it "Reynolds stress".
- **Cylinder runs (§III.D):** first "$10^5$, $5\times10^5$, and $10^6$", then "five Reynolds numbers, i.e., $10^5$, $5.0\times10^5$, $6.0\times10^5$, $8.0\times10^5$, and $10^6$".
- **Uncited legends:** Musker 1979 (Figs. 2, 5), Schlichting 1968 (Fig. 7), Rodriguez et al. 2015, Achenbach 1968, Spitzer 1965 (Fig. 14) and the Ahmed "Experiment (2003)", "uRANS (2017)", "IDDES (2017)" curves (Fig. 11) are not in the reference list; §III refers to "subsection 2 of Appendix" and "subsection 3 of Appendix" for Appendices B and C.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\tilde{\boldsymbol u}$, $\tilde p$ | $\bar{\boldsymbol u}$, $\bar p$ | LES filter, incompressible; **collision:** the tilde is not a Favre filter here |
| $C_S$ ($C_s$) | $C_s$ | $\nu_t=(C_s\Delta)^2\lvert\bar S\rvert$ |
| $S=\sqrt{2\tilde S_{\alpha\beta}\tilde S_{\alpha\beta}}$ | $\lvert\bar S\rvert$ | factor two included |
| $\nu_t$ | $\nu_t$ | the same symbol for the SGS (Eq. 3) and the wall-model mixing-length (Eq. 22) viscosity |
| $g_i$, $g_i^{eq}$, $g_i^{neq}$ | $f_q$, $f_q^{\mathrm{eq}}$, $f_q^{\mathrm{neq}}$ | |
| $\boldsymbol e_i$, $\omega_i$ | $\boldsymbol c_q$, $w_q$ | **collision** of $\omega_i$ with the vorticity |
| $\tau$ | $\tau_{\mathrm{LB}}$ | relaxation time |
| $c_s$ | $c_s$ (page-local) | lattice sound speed; not the Smagorinsky $C_s$ |
| $M$, $\Lambda$ ($s$), $m$ | (MRT transform, relaxation matrix, moments) | |
| $\Omega_i$, $G_i$, $F_i$, $\boldsymbol f$ | (collision operator, force term, discrete forcing), $f_i$ | **collision** of $\Omega_i$ with the rotation tensor |
| $H^{(n)}$, $a^{(n)}_0$, $a^{(n)}_1$ | (Hermite polynomials and coefficients) | RR-LBM |
| $\lambda(r)$, $\delta_h$ | $\phi_4(r)$ (page-local), $\delta_h$ | **collision** of $\lambda$ with the Taylor microscale |
| $\alpha$, $\beta$ (Eq. 15) | $\alpha_{\mathrm{fb}}$, $\beta_{\mathrm{fb}}$ (page-local) | **collision** with the blending factor $\alpha$ and the correction field $\beta(\boldsymbol x)$ |
| $l$, $s$; $l^+$ | $y$, $s$; $y^+$ | wall-normal and tangential |
| $\Delta b$, $\Delta c$ | $d_b$ (page-local), $h_{\mathrm{wm}}$ | as used in Eqs. (20)–(21) |
| $A=19.0$ | $A^+$ | van Driest constant |
| $H$ | $\delta$ | channel half-height |
| $Re_m$ | $Re_b$ | bulk Reynolds number, defined in the text with $\overline uH/\nu$ |
| $h$ (Ahmed) | $h_{\mathrm A}$ (page-local) | body height; **collision** with the cell size $h$ |
| $c_p$, $c_f$, $C_D$, St | $C_p$, $C_f$, $C_D$, $St$ | |
| $\theta_s$ | $\theta_{\mathrm{sep}}$ (page-local) | **collision** with the momentum thickness |
| DIB, SIB | (diffusive-, sharp-interface IBM) | |

# Reference list

75 printed references, numbered AIP style with titles, no DOIs printed.
The list is merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug. Ref. 30 is the ingested
[cai-2022](/sources/cai-2022.md). Two references carry keys of ingested
Source slugs but are different works and are keyed `huang-2022-b` and `wang-2023-d` respectively: ref.
58 (Huang Q. et al., "Streamline penetration, velocity error, and
consequences of the feedback immersed boundary method", Phys. Fluids
34:097101) and ref. 20 (Wang L., Liu & Rajamuni, lattice Boltzmann method
in fluid–structure interaction, Proc. Inst. Mech. Eng. C 237).
Same-author same-year works are keyed in printed order (Ma 2019: refs. 26,
57). Ref. 22 (Tessicini et al., CTR Annual Research Briefs 2002), ref. 66
(Groves et al., David Taylor Research Center 1989) and ref. 68 (Ahmed et
al., SAE paper 840300) are grey literature; the title of ref. 61 (Lee &
Moser) has a garbled $Re_\tau$ symbol. No item is unparseable.

# Pages created or updated

Chunk 14 (2026-10-28). This source is cited on:

- [Ahmed body](/benchmarks/ahmed-body.md)
- [Circular-cylinder wake](/benchmarks/circular-cylinder-wake.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [Equilibrium wall model](/methods/equilibrium-wall-model.md)
- [Explicit algebraic Reynolds-stress models](/methods/explicit-algebraic-reynolds-stress-model.md)
- [Immersed boundary methods](/methods/immersed-boundary-method.md)
- [Lattice Boltzmann methods for turbulent flow](/methods/lattice-boltzmann-method.md)
- [Slip-wall models](/methods/slip-wall-model.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
