---
type: Source
title: "Mozaffari et al. (2024) — Lattice Boltzmann k-ω SST based hybrid RANS/LES simulations of turbulent flows"
description: "Implements k-ω SST RANS and the SST-based IDDES and continuous-eddy-simulation hybrids in the ProLB lattice Boltzmann solver, tests them on NACA 23012, NACA 0012 up to 45° and the Ahmed body, and finds the equilibrium wall model suppresses slant separation."
resource: "doi:10.1016/j.jcp.2024.113269"
source_kind: paper
authors: [Mozaffari S., Cai S.-G., Jacob J., Sagaut P.]
year: 2024
venue: "J. Comput. Phys. 514:113269"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2024_Crossref_Journal_of_Computational_Physics_Mozaffari_Lattice_Boltzmann_k-ω_SST_based_hybrid_RANSLES_simulations_o.pdf"
tags: [lattice-boltzmann, hybrid-rans-les, k-omega, wall-model, bluff-body, immersed-boundary]
timestamp: 2026-10-27T15:55:00Z
---

# Summary

Mozaffari et al. (2024) implement the [$k$-$\omega$ SST model](/methods/k-omega-sst-model.md)
and two SST-based [hybrid RANS/LES](/definitions/hybrid-rans-les.md) models in a
research version of the [lattice Boltzmann](/methods/lattice-boltzmann-method.md)
solver [ProLB](/software/prolb.md): IDDES, a form of
[detached-eddy simulation](/methods/detached-eddy-simulation.md), and Heinz's
[continuous eddy simulation](/methods/continuous-eddy-simulation.md) (CES). ProLB runs a D3Q19 lattice with a hybrid
recursive regularized collision on octree Cartesian grids. The wall is handled by
[immersed-boundary](/methods/immersed-boundary-method.md) reconstruction and by
the explicit algebraic [equilibrium wall model](/methods/equilibrium-wall-model.md)
of Cai & Sagaut, a unified [law of the wall](/definitions/law-of-the-wall.md).
The eddy viscosity enters the lattice Boltzmann scheme only through the relaxation
time. The $k$ and $\omega$ equations are solved by finite differences inside the
collision step, and RANS wall functions set $k$ and $\omega$ at the boundary nodes.

There are three test cases. On a two-dimensional NACA 23012 airfoil, SST matches
the [Spalart–Allmaras](/methods/spalart-allmaras-model.md) model already in ProLB.
Both give forces close to experiment, and both under-predict $C_p$ near the
leading edge. On a three-dimensional [NACA 0012](/benchmarks/naca-0012-airfoil.md)
the hybrids coincide with RANS while the flow is attached. At $45^\circ$ they
bring lift and drag from the RANS values 2.238 and 2.053 to about 1.2 and
1.0, against the reference 1.097 and 1.180. On the
[Ahmed body](/benchmarks/ahmed-body.md) at $25^\circ$ and $35^\circ$, the
equilibrium wall model, which has no pressure-gradient term, keeps the slant flow
attached for both hybrids. A zero-velocity Dirichlet condition at $y^+\gg1$
restores the separation. IDDES then reproduces the $35^\circ$ wake and drag,
fails at $25^\circ$, and CES separates too early on the roof. The authors
conclude that SST-based hybrids are a cheaper alternative to
[wall-modelled LES](/methods/wall-modelled-les.md) in lattice Boltzmann codes.
They name the missing [adverse-pressure-gradient](/definitions/adverse-pressure-gradient-wall-law.md)
term of the wall model as the dominant error source. The IDDES elevating
function is said to guard against [log-layer mismatch](/definitions/log-layer-mismatch.md).
The introduction reviews lattice Boltzmann LES with the
[Smagorinsky](/methods/smagorinsky-model.md) and related models and earlier
[$k$-$\varepsilon$](/methods/k-epsilon-model.md) hybrids.

# Version read

HAL deposit hal-04921212v1 (deposited 30 January 2025): the author's accepted
manuscript in the Elsevier preprint template, line-numbered, with two sentences
of revision text in red (printed p. 7, lines 202–203). It is not the typeset
version of record. 26 PDF pages (HAL cover plus 25 manuscript pages), all read;
the equations of printed pp. 6–9 were checked visually. Locators are the
manuscript's printed pages, line numbers, sections, equations, figures and
tables. Title, authors, venue and DOI on the cover and page 1 match Crossref; no
identity problem. No hardware, timing or cost figures are given.

# Key claims

1. Turbulence enters the lattice Boltzmann scheme only through the relaxation time of the regularized collision, $\tau_{\mathrm{LB}}=\Delta t/2+(\nu+\nu_t)/c_s^2$ (Eq. 6, §2.1). **Stated**
2. The hybrid recursive regularized collision is used with $\sigma_{\mathrm{HRR}}=0.98$; this parameter introduces a bi-Laplacian hyperviscosity because the strain rate is computed by second-order centred finite differences (§2.1, Eq. 5, lines 105–110, citing Jacob et al. and Astoul et al.). **Stated**
3. The explicit equilibrium wall model of Cai & Sagaut (unified $y^+(Re_y)$ with $p_{\mathrm{wm}}=0.7894$, $s_{\mathrm{wm}}=86.58$; $\kappa\approx0.41$, $E_{\mathrm{wl}}\approx7.9$) is used everywhere; adverse-pressure-gradient effects are knowingly ignored, on the ground that Cai et al. (2022) showed that in fully separated flows the equilibrium wall model operates at low $y^+$, comparable to linear reconstruction (§2.2, Eqs. 9–15, lines 149–152). **Stated**
4. The SST transport equations are solved by finite differences on the Cartesian grid during the collision step: fourth-order centred derivatives, one-sided differences at walls, second-order centred differences at grid transitions, and hybrid TVD centred/upwind advection with a modified Van Albada 1 limiter calibrated on an inclined flat plate to avoid high $\omega$ fluxes near the wall (§2.3, lines 201–209). **Stated**
5. Wall functions set $k$ and $\omega$ at the boundary nodes, switching at $y^+=11.06$ (Kalitzin et al.), with an optional $\omega$ blending from Knopp et al. (Eqs. 22–25). **Stated**
6. The $k$-$\omega$ SST model "has never been used in the standard LBM framework" (lines 68–69); Wang et al. used it in a non-standard finite-volume lattice Boltzmann method on unstructured grids (lines 43–46). **Stated**
7. On the 2D NACA 23012, SST and SA give close $\nu_t$ fields except at $\alpha=0^\circ$, where SST gives a lower $\nu_t$ (§3.1, Figs. 4–5). **Shown**
8. NACA 23012 forces (Table 1): $C_L$ SST/SA/experiment $=0.12/0.12/0.12$ ($0^\circ$), $0.83/0.79/0.79$ ($6.2^\circ$), $1.12/1.175/1.07$ ($9.3^\circ$); $C_D=0.0074/0.0081/0.0075$, $0.0081/0.0083/0.009$, $0.014/0.012/0.0125$. The drag error grows with $\alpha$, largest for SST at $9.3^\circ$. **Shown**
9. Both RANS models under-predict $C_p$, most near the leading edge, which the authors attribute to the inability of RANS to represent local transition (lines 339–342); $C_f$ disagrees with Xfoil and a wall-resolved elsA computation near the leading edge (Fig. 7). **Shown** (cause **Stated**)
10. One extra leading-edge refinement level reduces the $C_p$ error at $9.3^\circ$ by "almost 50%" (Fig. 8, lines 346–350). **Shown**
11. On the 3D NACA 0012 at $\alpha=10^\circ$, IDDES, CES and RANS give identical mean $C_p$; at $15^\circ$ the hybrids differ slightly downstream of the leading edge, because the fine leading-edge grid lets them run as LES in the outer boundary layer with only the first few nodes in RANS mode (Figs. 10–11, lines 372–381). **Shown**
12. The RANS–LES transition is thin in IDDES and smooth and continuous in CES (Fig. 11, lines 382–385). **Shown**
13. For $\alpha=2^\circ$, $6^\circ$, $10^\circ$, $C_L$ and $C_D$ are close to Ladson's data for all models; at $15^\circ$ RANS shows a slight discrepancy; the larger unsteadiness of the hybrids requires longer averaging (Fig. 12, lines 386–394). **Shown**
14. NACA 0012 at $45^\circ$ (Table 2): $C_L/C_D$ RANS $2.238/2.053$, IDDES-SST $1.231/1.038$, CES-SST $1.192/0.993$, reference $1.097/1.180$ (from Shur et al. 1999); convergence needed 234 flow-through times, 110 of them averaged. IDDES and CES perform "almost the same without any superiority" (lines 412–413). **Shown**
15. SST-based hybrids "can be an alternative for the wall-modeled LES in the LBM framework", behaving as WMLES only where separation occurs (lines 413–418). **Stated** (supported by 14)
16. On the Ahmed body with the equilibrium wall model on the body surface, neither hybrid separates on the slant at $25^\circ$ or $35^\circ$, contrary to the fully detached $35^\circ$ reference flow (§3.3, Fig. 16, lines 459–464). **Shown**
17. The cause given: in a mild adverse pressure gradient the equilibrium wall model delays or suppresses separation, and without instabilities on the slant the model does not switch from RANS to LES (lines 465–470, 516–519). **Stated**
18. Replacing the wall model by a zero-velocity Dirichlet condition at $y^+\gg1$ produces separation on the slant; CES then separates on the roof and the separation extends into the wake (to $X=500$ mm), while IDDES has small roof and side bubbles that reattach (Figs. 17, 19, 20). **Shown**
19. IDDES with the no-slip condition at $35^\circ$ reproduces the reference wake topology, including a small recirculation near the end of the slant also seen in the body-fitted IDDES of Guilmineau et al.; the recirculation extends just over 200 mm as in the experiment, the wake being slightly longer than the reference (Figs. 18–19, lines 485–495). **Shown**
20. IDDES with the Dirichlet condition "could recover the WMLES solution" of Cai et al. for the $35^\circ$ Ahmed body at lower cost; no cost figures are given (lines 510–515). **Stated**
21. At $25^\circ$, IDDES with the no-slip condition separates late and does not reattach, giving a wrong wake; attributed to $y^+\approx100$–$150$ on the slant (Figs. 22–24, lines 520–531). **Shown** (cause **Stated**)
22. Ahmed-body $C_D$ (Table 3): IDDES-WM 0.2878 ($35^\circ$), 0.2510 ($25^\circ$); CES-WM 0.2738 ($35^\circ$); IDDES-NS 0.2819 ($35^\circ$), 0.2970 ($25^\circ$); CES-NS 0.3779 ($35^\circ$). Experiments: Ahmed et al. 0.2580/0.2850 ($Re_H=1.2\times10^6$), Meile et al. 0.2790/0.2990 ($7.68\times10^5$), Liu et al. 0.32 ($35^\circ$, $1.4\times10^5$), Thacker et al. 0.3840 ($25^\circ$, $1.4\times10^5$); Guilmineau et al. SST-NS 0.2999/0.3218, IDDES-NS 0.3452/0.3802 ($35^\circ$/$25^\circ$). **Shown**
23. "Primary findings" of the authors indicate that an adverse-pressure-gradient-aware wall model (Wilhelm et al.) improves the Ahmed-body results substantially; no data are shown (lines 553–557). **Stated**

The CES modification of the SST dissipation term (Eqs. 33–34), with the
source's symbols renamed (see the Notation map):
$$\beta^*\omega k\;\to\;\beta^*\omega k\,\psi_\beta,\qquad \psi_\beta=\beta_{\mathrm{CES}}+L_+^2(1-\beta_{\mathrm{CES}}),\qquad L_+=\frac{\Delta_{C+}}{(1+\Delta_{C+}^3)^{1/3}},\quad \Delta_{C+}=C_+\frac{\Delta}{L_{\mathrm{tot}}},\quad L_{\mathrm{tot}}=\frac{\sqrt k}{C_\mu\omega}.$$
The paper prints neither $C_+$, nor the value of the coefficient written
$\beta_{\mathrm{CES}}$ here (as on the [continuous eddy simulation](/methods/continuous-eddy-simulation.md)
page), nor the definition of $\Delta$ used in ProLB.
For $\Delta_{C+}\to\infty$, $L_+\to1$ and $\psi_\beta\to1$
(RANS dissipation); for $\Delta_{C+}\to0$,
$\psi_\beta\to\beta_{\mathrm{CES}}$ *(compiler check, not in the sources)*.

# Printed slips

- **Eqs. 16–17, production term:** printed $\tau_{ij}\,\partial u_j/\partial x_j$, which contracts the repeated $j$ and leaves a free index $i$ in a scalar equation; the scalar production needs $\partial u_i/\partial x_j$.
- **Eq. 18** lists $\phi=\{\beta,\gamma,\sigma_k,\sigma_\omega\}$, while lines 192–193 name "$\beta,\beta^*,\gamma,\sigma_k,\sigma_\omega$"; no coefficient values are printed except $a_1=0.31$.
- **Line 196:** "the $k$-$\omega$ SST model proposed by Menter et al. [41]"; ref. [41] is the single-author Menter (2009), and the model was attributed to [40] (Menter 1994) earlier.
- **Line 250 against Eq. 28:** $L_{LES}$ in the text, $l_{LES}$ in the equation.
- **Line 274 (CES):** $\psi_\beta=\beta+R(1-\beta)$ reuses $\beta$, the SST closure coefficient of Eqs. 17–18, without defining it; $C_+$ and $\Delta$ are given neither values nor definitions.
- **Line 96 against Eq. 6:** "$\bar\tau=\tau+0.5$, $\tau=\nu/c_s^2$" (lattice units) against $\bar\tau=\Delta t/2+(\nu+\nu_t)/c_s^2$.
- **Eq. 24** defines $\omega_{log}$ on its left side from $\omega_{b1},\omega_{b2}$, which contain the $\omega_{log}$ of Eq. 23.
- **Line 465:** "As seen before for the airfoil case (Section 3.1), using an equilibrium wall model for a boundary layer under a high adverse pressure gradient can have negative effects"; that discussion is in §3.2 (NACA 0012, lines 395–397).
- **Lines 557–558:** "the previous wall models were replaced by a non-zero Dirichlet velocity", against "zero-velocity Dirichlet" (lines 475–476) and the Table 3 caption.
- **Lines 535–536:** "the corresponding lift and drag coefficients are close to reference values"; Table 3 reports only drag.
- **Table 2:** the caption compares with "reference data by [45]" and the column is headed "Exp.", but [45] is Shur et al. (1999), "Detached-eddy simulation of an airfoil at high angle of attack"; whether the reference values are measured or computed is not stated.
- **§3.2, line 364:** $\alpha=60^\circ$ is announced, but no result at $60^\circ$ is reported.
- **Reference list:** ref. [8] (Cai & Sagaut 2021, Phys. Fluids 33:041703) prints DOI `10.1007/s10494-020-00181-7`, the same DOI printed for ref. [63] (Wilhelm et al. 2021, Flow Turbul. Combust.); ref. [29] (Krüger et al., book) carries a spurious "10, 4–15".
- Typos: "Spallart-Almaras" (line 168), "academcic" (line 32).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $f_i$, $\mathbf c_i$, $w_i$ | $f_q$, $\boldsymbol c_q$, $w_q$ | lattice populations, velocities, weights (§11) |
| $\bar f_i=f_i-\Delta t\,\Omega_i/2$ | shifted populations (no registry symbol) | **collision:** the overbar is not the LES filter |
| $\bar\tau$ (relaxation time) | $\tau_{\mathrm{LB}}$ | **collision:** not the SGS stress $\tau_{ij}$ |
| $c_s$ | $c_s$ | lattice sound speed, page-local (as on [ProLB](/software/prolb.md)) |
| $C_s=340$ m/s (§3.1) | $c_0$ | physical sound speed; **collision** with the Smagorinsky coefficient $C_s$ |
| $\sigma$ (HRR) | $\sigma_{\mathrm{HRR}}$ | page-local; not $\sigma_k$, $\sigma_\omega$ |
| $\Omega_i$ (collision operator) | collision operator (no registry symbol) | **collision** with the rotation tensor $\Omega_{ij}$ |
| $\Omega$ (SST, DDES) | $\lvert\Omega\rvert$ | "absolute value of the vorticity" |
| $S$ (DDES $r_d$) | strain-rate magnitude | factor-two convention not stated |
| $\tau_{ij}$ (Eqs. 16–17) | $R_{ij}$ | undefined in the paper; sign convention not stated |
| $d$, $d_w$ | $d$ | wall distance, both symbols printed |
| $\kappa$, $E$ | $\kappa$, $E_{\mathrm{wl}}$ | $u^+=\kappa^{-1}\ln(E_{\mathrm{wl}}y^+)$, i.e. $B=\kappa^{-1}\ln E_{\mathrm{wl}}\approx5.04$ *(compiler check, not in the sources)*; $E$ **collides** with the total energy |
| $p$, $s$ (Eq. 15) | $p_{\mathrm{wm}}$, $s_{\mathrm{wm}}$ | page-local blending constants of the unified wall law; $p$ is not the pressure |
| $Re_y=uy/\nu$ | $Re_y$ | §11 |
| $h_{max}$ | $h$ (maximum cell edge) | cubic cells |
| $\beta$ in $\psi_\beta$ (CES) | $\beta_{\mathrm{CES}}$ | registry §11, as on the CES page; **collision** with the SST coefficient $\beta$ |
| $\psi_\beta$, $R=L_+^2$, $L_+$, $L_{tot}$, $\Delta_+$, $\Delta_{C+}$, $C_+$ | same ($\psi_\beta$, $L_+$ registry §11; the others page-local) | CES resolution indicators |
| $\phi$ (Ahmed slant angle; also wall-function blend, SST generic coefficient) | written out | **collision**: three meanings in the source |
| $Re_c$, $Re_H$ | $Re_c$, $Re_H$ | chord and body height |

# Reference list

67 printed references, numbered [1]–[67] in alphabetical order (Elsevier
numbered style). The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Ref. [7] (Cai,
Mozaffari, Jacob & Sagaut 2022) is the ingested source `cai-2022`. Same-author
same-year pairs are keyed in printed order (`cai-2021` = [6], `cai-2021-b` =
[8]; `wang-2020`, `wang-2020-b`; `yu-2005`, `yu-2005-b`). Parsing remarks: the
DOI shared by [8] and [63] is recorded as printed with a note; [25] is an arXiv
preprint; [29] carries a spurious volume and pages; [30] Ladson (1988) prints
only "volume 4074"; [12], [16], [47], [60] lack pages or publisher; the
ProLB web page (author printed "CS") is keyed `cs-2017`, the ERCOFTAC page `ercoftac-2004`.

# Pages created or updated

Chunk 5 (2026-10-26), cited further in chunks 7, 14. This source is cited on:

- [Ahmed body](/benchmarks/ahmed-body.md)
- [NACA 0012 airfoil](/benchmarks/naca-0012-airfoil.md)
- [Wall law in adverse pressure gradient](/definitions/adverse-pressure-gradient-wall-law.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Log-layer mismatch](/definitions/log-layer-mismatch.md)
- [Continuous eddy simulation](/methods/continuous-eddy-simulation.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [Equilibrium wall model](/methods/equilibrium-wall-model.md)
- [Immersed boundary methods](/methods/immersed-boundary-method.md)
- [k-ε models](/methods/k-epsilon-model.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [Lattice Boltzmann methods for turbulent flow](/methods/lattice-boltzmann-method.md)
- [Mesh adaptation for turbulent-flow simulation](/methods/mesh-adaptation.md)
- [Wall functions for RANS](/methods/rans-wall-function.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
- [elsA](/software/elsa.md)
- [ProLB](/software/prolb.md)
