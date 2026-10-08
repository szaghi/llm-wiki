---
type: Source
title: "Mignone & Del Zanna (2021) — Systematic construction of upwind constrained transport schemes for MHD"
description: "General composition formula building UCT edge EMFs from any Jacobian-free 1D Riemann solver (new UCT-HLLD, UCT-GFORCE), with a six-way comparison showing the EMF averaging is as consequential as the Riemann solver."
resource: "doi:10.1016/j.jcp.2020.109748"
source_kind: paper
authors: [Mignone A., Del Zanna L.]
year: 2021
venue: "J. Comput. Phys. 424:109748 (arXiv:2004.10542)"
local_file: "~/papers/mosaic/div-free-amr/2021-JCP-Mignone-101016jjcp2020109748.pdf"
tags: [constrained-transport, upwind-emf, riemann-solver, hlld, production-code, mhd]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

The paper does two things. It compares the edge-EMF recipes for
Godunov-type CT, and it generalizes
[upwind constrained transport](/methods/upwind-constrained-transport.md)
into a recipe that works with any *component-wise* (Jacobian-free) 1D
Riemann solver. It is presented at second order in PLUTO, with a claimed
direct extension to higher-order FV and FD and to relativistic MHD.

The six schemes compared, under one base scheme:
* arithmetic averaging;
* CT-Contact, which is the $\mathcal{E}^c$ of Gardiner & Stone;
* CT-Flux, with doubled dissipation;
* UCT-HLL;
* UCT-HLLD and UCT-GFORCE, both new.

The tests cover 2D and 3D field loops, a Harris current sheet,
Orszag–Tang to $t = 2\pi$, a 3D low-$\beta$ blast, a weakly unstable KH
layer and a shearing-box MRI.

The file read is the arXiv v2 preprint. Volume and article number were
verified on Crossref.

# Key claims

1. **The UCT conditions restated** (§4). Staggered field components are
   single-valued in the fluid fluxes at their own faces and two-valued
   (reconstructed) at edges. A four-state solver is used for induction, and
   there is no time splitting. Arithmetic averaging "yields, for 1D
   plane-parallel flows along the grid Cartesian axes, half of the correct
   value".
2. **The composition formula** (§5, eqs. 30–35).
   * Any solver whose induction flux is $a^LF^L + a^RF^R$ minus a diffusion
     term linear in $B_t^{L,R}$ yields an edge EMF (eq. 33). The inputs are
     the face coefficients $a$ and $d$, plus 1D reconstructions of the
     transverse velocity and the staggered field.
   * The coefficients are derived for LLF and HLL (eqs. 31–32) and HLLC
     (same as HLL when $B_n \ne 0$).
   * HLLD (eqs. 44–45) switches to the HLLC limit when the rotational
     speeds coalesce, at tolerance $10^{-9}$. GFORCE is covered in
     eqs. 47–52, and isothermal HLLD in Appendix A.
3. **Dissipation is a property of the EMF, not only of the solver** (§6.2).
   On the Harris sheet, CT-Contact and CT-Flux inherit their dissipation
   from the base solver. With Roe they reconnect early; with HLLD they
   stay near-ideal. UCT-HLLD behaves the same either way, with dissipation
   $O(v_x - \lambda^*)$.
4. **Rankings across tests** (§§6.1–6.6).
   * UCT-HLLD is the least dissipative and stable.
   * CT-Contact is close to it.
   * UCT-GFORCE is intermediate.
   * UCT-HLL is the most diffusive: KH fails to grow at $128\times256$,
     the MRI stress is 0.07 against 0.21, and the Orszag–Tang central
     island appears only at the higher resolution.
   * Arithmetic averaging is unstable or oscillatory. With a third-order Roe
     base scheme on Orszag–Tang, arithmetic averaging and CT-Flux both
     fail.
5. **Field loop** (§6.1). In a loop rotated in 3D, the axial field
   component is nonzero only at truncation level, and it ranks the schemes
   (UCT best, arithmetic worst). Runge–Kutta time stepping avoids the CTU
   interface-state source terms.
6. **Positivity is not supplied by CT** (§6.4, footnote 2). On the
   $\beta \approx 2.5\cdot10^{-4}$ blast, no scheme preserves pressure
   positivity without the Balsara–Spicer energy correction, even with
   minmod.
7. **Authors' assessments** (§7).
   * Doubling the dissipation (CT-Flux, CT-Contact) is "an efficient and
     valid option, although not strictly compliant with the UCT formalism".
   * CT-Contact's selection rule lacks formal justification and is at most
     second order, in agreement with
     [Felker & Stone (2018)](/sources/felker-2018.md).
   * The UCT formula gives a single-valued, continuous numerical flux in
     each direction. "Whether this is an advantage or not should be
     discerned for the particular application."

# Notation map

| Mignone & Del Zanna (2021) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $B_{x_f}, B_{y_f}, B_{z_f}$ | $B_h \in V_h^2$ | face-staggered |
| $E_{z_e}$ (edge emf) | $E_h \in V_h^1$ | |
| eq. (8)–(9) | $\partial_t B_h = -C_h E_h$; $D_h^{\mathrm{f}} B_h = 0$ exactly | |
| N/S/E/W states | four corner states | |
| $a^{L,R}$, $d^{L,R}$ | flux weights and diffusion coefficients | no registry symbol |
| CT-Contact | $\mathcal{E}^c$ | Gardiner & Stone naming kept on concept pages |
| $\Delta_x, \Delta_y, \Delta_z$ | backward differences | not the registry $\Delta$ |

# Pages created or updated

* Updated [Upwind constrained transport](/methods/upwind-constrained-transport.md): the composition formula and the measured ranking.
* Updated [Flux-CT and the Godunov CT variants](/methods/flux-ct.md): the averaging-family comparison and the inherited-dissipation finding.
* Updated [Field-loop advection](/benchmarks/field-loop-advection.md): the rotated 3D loop, and why it differs from Felker & Stone's round-off result.
* Updated [Positivity–divergence coupling](/results/positivity-divergence-coupling.md): exactness on the staggered stencil does not supply positivity.
* Corrected [Gardiner & Stone (2008)](/sources/gardiner-stone-2008.md): its resource DOI was another paper's. The correct DOI is printed in this reference list and verified on Crossref.

# Citations

1. `~/papers/mosaic/div-free-amr/2021-JCP-Mignone-101016jjcp2020109748.pdf` (doi:10.1016/j.jcp.2020.109748): text extraction, all pages including Appendix A and the reference list (62 entries).
