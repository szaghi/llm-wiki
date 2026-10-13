---
type: Source
title: "Balsara (1998) — Total variation diminishing scheme for adiabatic and isothermal magnetohydrodynamics"
description: "Single-step characteristic TVD Godunov scheme for adiabatic and isothermal MHD (the RIEMANN code) with a periodic FFT projection whose modified wavenumber makes the central divergence exactly zero; no divergence value reported."
resource: "doi:10.1086/313093"
source_kind: paper
authors: [Balsara D.S.]
year: 1998
venue: "Astrophys. J. Suppl. 116:133-153"
local_file: "/home/stefano/papers/mosaic/div-free-amr/1998-ApJS-Balsara-101086313093.pdf"
tags: [projection, fft, tvd, godunov, mhd, astrophysics]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

A second-order, single-step TVD (MUSCL-type) Godunov scheme for ideal
adiabatic (seven waves) and isothermal (six waves) MHD, the scheme of the
author's RIEMANN code. Slopes are limited in characteristic variables;
linearly degenerate fields are steepened after Yang (1990); time-centred
face states come from a Colella (1990) characteristic predictor and fluxes
from the author's companion linearized Riemann solver (ApJS 116:119).
Neither the eigenvectors nor the solver are printed here. A
characteristic-switched second-order viscosity and a fourth-order
hyperviscosity are designed not to damage the TVD property. The field is
collocated and no discrete divergence is preserved by the update. Instead
a periodic FFT [projection](/methods/projection-method.md) replaces the
continuous wavenumber with the Fourier symbol of the central difference,
which makes the central divergence exactly zero (§5). Tests: four
adiabatic and two isothermal Riemann problems, an isothermal
[Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md), and isothermal
and adiabatic 2D blast waves. **No divergence value is reported.**

# Key claims

1. **Characteristic TVD slopes** (§2.1, eqs. 2.1–2.4). Primitive
   variables are projected on the left eigenvectors of zone $i$; the
   limited slope is the MC limiter for genuinely nonlinear fields and
   minmod for linearly degenerate ones, recombined with the right
   eigenvectors. The adiabatic eigenvectors are cited to
   [Roe & Balsara (1996)](/sources/roe-balsara-1996.md), the isothermal
   ones to Balsara (1996, ApJ 465:775).
2. **Steepening of linearly degenerate fields** after Yang (1990) (§2.2,
   eqs. 2.5–2.12): entropy and Alfvén waves (adiabatic), Alfvén waves
   (isothermal), with constants $b = 4.3$ and $c = 33.0$.
3. **Single-step time stepping** (§3, eqs. 3.1–3.5), after Colella
   (1990); multistep TVD Runge–Kutta is explicitly not used. Multi-D runs
   are Strang-split or unsplit; the unsplit variant adds first-order
   transverse flux differences to the face states, as in
   [corner transport upwind](/methods/corner-transport-upwind.md).
4. **The TVD property is asserted.** "The TVD property for upwind schemes
   is already guaranteed by our choice of interpolation and Riemann
   solver" (§4, p. 137). No proof is given for the MHD system
   ([total variation diminishing](/properties/total-variation-diminishing.md)).
5. **Characteristic viscosity and hyperviscosity** (§4, eqs. 4.1–4.18).
   Per-field switches from limiter functions (van Leer for genuinely
   nonlinear, superbee for linearly degenerate fields). The fourth-order
   term switches off where the largest switch exceeds 0.5 (eq. 4.11), the
   condition of Swanson & Turkel (1992) for preserving TVD. The
   second-order term is scaled by the fast and slow speeds and turned off
   by a pressure switch at entropy pulses, Alfvén shocks and weak shocks.
   Constants: second-order coefficient 0.06–0.1, pressure threshold 0.5,
   fourth-order coefficient 1/64–1/32. An entropy fix after Quirk (1994)
   is used against odd–even decoupling. HLLE and HLLEM are rejected for
   MHD because they cannot represent slow shocks exactly (p. 136).
6. **The divergence: projection with a consistent symbol** (§5,
   eqs. 5.1–5.6).
   * The discrete divergence is the zone-centred central difference
     $D_h^{\mathrm c}$ (eq. 5.1).
   * The "traditional" projection (citing Zachary et al. 1994) solves a
     Poisson problem by FFT with the inverse squared continuous wavenumber
     (eqs. 5.2–5.4). On a random vector field it leaves eq. 5.1 "not
     exactly zero", because eq. 5.4 "is not a spectrally accurate version
     of the finite difference operator in equation (5.1)" (p. 138).
   * The fix writes the projection as the tensor
     $\delta_{ij} - k_ik_j/k^2$ (eq. 5.5) and replaces each wavenumber
     component by the central-difference symbol $\sin(kh)/h$ (eq. 5.6).
     This "makes equation (5.1) exactly zero" and is "mathematically
     exact for finite difference schemes" (p. 139). Long wavelengths are
     nearly unchanged. All three field components must be transformed.
   * The modes where the modified symbol vanishes ($k = 0$ and the
     grid-scale mode $kh = \pi$) are not discussed.
   * Cost: the elliptic step "costs no more than 2% of the total
     computational cost" (§6.2.2, p. 152).
7. **Divergence control matters, against the literature** (§6.2.1,
   pp. 145–147). "The opinion in the literature so far has been that no
   significant difference is observed when the divergence cleaning step
   is dropped" (citing Dai & Woodward 1994b, Zachary et al. 1994, Ryu,
   Jones & Frank 1996 [sic]). Those authors "have only used dimensionally
   split schemes", ran "for short integration times", and "experimented
   with only the less accurate version of the divergence cleaning step".
   After a long integration, "significant differences do indeed arise".
8. **The form of the constraint is secondary** (§6.2.2, pp. 149, 152):
   "The discretized formulation in which this divergence-free condition
   for the magnetic field is imposed is not as important in obtaining
   good results as the fact that it is indeed imposed." Reasons given:
   spurious divergent field builds up slowly in a second-order consistent
   scheme, most in stagnation regions with small-scale structure; and,
   because total energy is updated, spurious magnetic energy "may on
   occasion cause the pressure to become negative". Divergence control is
   "essential for physical realizability". No run demonstrates the
   negative pressure.
9. **CT noted, not adopted** (§5, p. 138). Evans & Hawley "have shown that
   this can be formally achieved using an area-weighted discretization"
   for artificial-viscosity schemes; Godunov schemes have "so far relied
   on Hodge projection", because zone-centred variables are "very
   important for the conservation form".
10. **Parallel scaling** (§7): "ideal scaling with processor number even
    when the number of processors is in excess of a few hundred"; no
    timing table.

# Tests

1D runs (§6.1, Table 1): $x \in [-0.5, 0.5]$, 800 zones, CFL 0.8,
unsmoothed initial data; hyperviscosity off in all displayed runs.

1. **Fig. 1**, coplanar adiabatic problem with a switch-on fast shock in
   ≤3 zones; no viscosity.
2. **Fig. 2**, the [Brio–Wu](/sources/brio-wu-1988.md) problem
   ($\gamma = 2$): slow compound wave, contact in ≤4 zones; no viscosity.
3. **Fig. 3**, seven discontinuities (after Ryu & Jones, Dai & Woodward);
   viscosity on, without damage to the contact and rotational
   discontinuities.
4. **Fig. 4**, two Mach-25.5 fast shocks; transverse-velocity spikes from
   the unsmoothed start "significantly" smaller than Dai & Woodward's.
5. **Figs. 5–6** (isothermal, Table 2): six discontinuities; an implosion
   with a central density spike attributed to numerical reconnection at a
   stagnation point.
6. **Isothermal Orszag–Tang** (§6.2.1, eqs. 6.1–6.2, Figs. 7–8).
   $(0, 2\pi)^2$, periodic, $200^2$, unit density, velocity amplitude equal
   to the sound speed, gas-to-rms-magnetic pressure ratio 10/3, shown at
   $t = 3.0$. Fig. 7 is Strang-split **without** cleaning, Fig. 8 unsplit
   **with** the modified-symbol cleaning every step. Density and total
   pressure are "reasonably similar"; the split run's kinetic energy has
   "two tiny concentrations at the center that dominate the entire flow
   field". Splitting and cleaning change together, and the paper credits
   the unsplit scheme with "the real benefit of using multidimensional
   fluxes". No divergence is measured.
7. **2D blast waves** (§6.2.2, Figs. 9–11). Unit square, $200^2$, uniform
   field along $x$ of "10.0 G".
   * Isothermal: overdensity 100 inside $r < 0.05$, $t = 0.09$. Fig. 9
     split without cleaning, Fig. 10 unsplit with cleaning (same
     confound); the uncleaned magnetic pressure "shows a great deal of
     small-scale fluctuations especially in the center".
   * Adiabatic: pressure 1000 inside $r < 0.05$, $\gamma = 1.4$,
     $t = 0.02$, split with cleaning (Fig. 11).
   * The field in gauss against code-unit pressure leaves $\beta$
     undetermined; not computed.

# Notation map

| Balsara | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $(\nabla\cdot B)_{i,j,k}$, eq. 5.1 | $D_h^{\mathrm c}B_h$ | denominators printed without the factor 2 |
| $\phi$; $\nabla\phi$ in eq. 5.3 | $\phi_h$; $G_h\phi_h$ (central, through eq. 5.6) | printed signs inconsistent (see below) |
| $\delta_{\alpha\beta} - k_\alpha k_\beta/\lvert k\rvert^2$ | spectral projector $\delta_{ij} - k_ik_j/k^2$ | $\alpha$, $\beta$ here are tensor indices |
| $\sin(k\Delta x)/\Delta x$ | symbol of the central difference, $\sin(kh)/h$ | |
| $\Delta x$ | $h$ | uniform grids |
| $B$ (zone-centred) | $\bar B_h$, collocated | |
| $\lambda^\alpha_i$; $l^\alpha$, $r^\alpha$ | $\lambda_k$; words | **collision:** the paper's wave index is $\alpha$; $r$ is the refinement ratio |
| $w^\alpha$ | characteristic components of $w$ | |
| $\Psi$, $b$, $c$, $\beta^\alpha_i$, $\mu^\alpha_i$, $\sigma^\alpha_i$ | words | **collision:** $\beta^\alpha_i$ is not plasma $\beta$; $c$ (33.0) is not the sound speed |
| $D^2$, $D^4$ | words (second- and fourth-difference dissipation) | **collision:** not the divergence $D_h$ |
| $\kappa^{(2)}$, $\kappa^{(4)}$, $\nu^\alpha_i$, $\nu^P$ | words | |
| $\Gamma$ (Table 1), $\gamma$ (§6.2.2) | $\gamma$ | **collision:** $\Gamma$ is the ghost-fill operator |
| $U$ | $U$ | conserved state |

# Pages created or updated

* Updated [Projection method](/methods/projection-method.md): the modified-wavenumber FFT projection, its cost, Balsara's characterization of earlier projections (an Open `Contradictions` entry on Ryu, Jones & Frank), and the 1998 "formulation is secondary" claim beside Balsara & Kim (2004).
* Updated [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md): the isothermal variant and the qualification of "no visible difference".
* Updated [Constrained transport (CT)](/methods/constrained-transport.md): the 1998 status of CT in Godunov MHD.
* Updated [positivity–divergence coupling](/results/positivity-divergence-coupling.md): the 1998 statement of the mechanism.
* Updated [total variation diminishing](/properties/total-variation-diminishing.md): the asserted TVD property and the hyperviscosity switch.

# Citations

1. `~/papers/mosaic/div-free-amr/1998-ApJS-Balsara-101086313093.pdf`.
   * **Version read.** The published journal version (21 pp., Acrobat
     Distiller 1998). Received 21 December 1995; accepted 3 December 1997.
   * **Identity.** doi:10.1086/313093, checked on Crossref: title and
     author match; Astrophys. J. Suppl. vol. 116, issue 1, pp. 133–153,
     issued May 1998. Dai & Woodward (1998, JCP) cite the work as "Total
     variation diminishing scheme for magnetohydrodynamics", submitted to
     J. Comput. Phys.; that citation is merged into this key by title (see
     [Dai & Woodward (1998, JCP)](/sources/dai-woodward-1998.md)).
   * **How it was read.** Text extraction of all pages; pp. 134, 135,
     137, 138, 139 and 145 rendered at 110 dpi for every equation and
     Table 1. Figures were read from captions and text only. The
     eigenvectors and the Riemann solver are in other papers and are not
     reproduced; the isothermal modification of eq. 4.16 is not given.
   * **Recorded as printed.**
     * Eq. 5.1 prints the central differences over $\Delta x$, $\Delta y$,
       $\Delta z$ instead of twice those spacings (checked on the page
       image); eq. 5.6 implies the factor 2 (reader's reading: a misprint;
       the zero set is unaffected).
     * Eqs. 5.2–5.3 print $\nabla^2\phi = -\nabla\cdot B$ followed by
       $B - \nabla\phi$, which doubles the divergence if taken literally:
       the same sign inconsistency as Zachary et al.'s eq. 34
       ([projection](/methods/projection-method.md)).
     * Eq. 5.5 lacks its closing parenthesis.
     * The text cites "Ryu, Jones, & Frank 1996"; the reference list has
       1995, ApJ 452:785. The text spells "Jorgensen & Terkel 1993"; the
       list has Jorgenson & Turkel. §5 cites "Evans & Hawley (1989)".
   * **Reference list.** 34 entries, all merged; ApJ style without
     titles. Brackbill & Barnes printed as J. Comput. Phys. 35:462. Harten
     (1977) printed as Comm. Pure Appl. Math. 30:661; Crossref
     (doi:10.1002/cpa.3160300506) gives 30:611–638. ApJ 465:775 is the
     new entry `balsara-1996-b`, distinct from `balsara-1996` (J. Comput.
     Phys., submitted). Evans & Hawley, printed 1989, is
     `evans-hawley-1988`; Roe & Balsara, printed in SIAM J. Numer. Anal.
     56:57, is `roe-balsara-1996`. The bibliography holds 3834 entries
     after this batch.
