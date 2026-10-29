---
type: Source
title: "Germano et al. (1991) — A dynamic subgrid-scale eddy viscosity model"
description: "Founding paper of the dynamic subgrid-scale model: the Germano identity between grid- and test-level subgrid stresses, a Smagorinsky form at both levels contracted with the resolved strain and averaged over wall-parallel planes, tested a priori and a posteriori in turbulent and transitional channel flow."
resource: "doi:10.1063/1.857955"
source_kind: paper
authors: [Germano M., Piomelli U., Moin P., Cabot W.H.]
year: 1991
venue: "Phys. Fluids A 3:1760-1765"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/1991_Crossref_Physics_of_Fluids_A_Fluid_Dynamics_Germano_A_dynamic_subgrid-scale_eddy_viscosity_model.pdf"
tags: [les, sgs-model, dynamic-procedure, a-priori-a-posteriori, channel-flow, backscatter]
timestamp: 2026-10-29T16:19:00Z
---

# Summary

Germano et al. (1991) introduce the
[dynamic procedure](/methods/dynamic-procedure.md): an eddy-viscosity
subgrid model for [large-eddy simulation](/definitions/large-eddy-simulation.md)
whose coefficient is computed from the resolved field during the run. The
motivation is that the [Smagorinsky model](/methods/smagorinsky-model.md)
with one constant cannot represent sheared, near-wall and transitional flows:
the reported $C_s$ ranges from 0.23 (Lilly, isotropic turbulence) to 0.1
(Deardorff, channel), and wall-bounded and transitional LES need van Driest
damping and intermittency functions.

With a grid filter and a wider test filter, the subgrid stresses at the two
levels and the computable resolved stress $L_{ij}$ satisfy the identity
$L_{ij}=\mathcal T_{ij}-\hat\tau_{ij}$ (Eq. 11, attributed to Germano's 1990
CTR manuscript). Modelling both stresses with the Smagorinsky form and one
coefficient, contracting with $\bar S_{ij}$ and averaging over planes parallel
to the wall gives $C_s^2(y,t)$ (Eq. 16) and the model (Eq. 17); the only
parameter is the filter-width ratio. The model stress vanishes where $L_{ij}$
does (laminar flow, walls), behaves as $y^3$ near the wall without damping,
and admits negative coefficients, i.e. plane-averaged
[backscatter](/definitions/energy-backscatter.md); no clipping is applied.

The evidence is [a priori and a posteriori](/definitions/a-priori-and-a-posteriori-testing.md):
a priori on DNS of [turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
(Kim, Moin & Moser) and of a transitional channel (Zang, Gilbert & Kleiser)
with sharp-cutoff filters, where a test-to-grid width ratio of 2 agrees best;
a posteriori in a Fourier–Chebyshev LES of a transitional channel through to
turbulence. The peak wall stress is within 3% of the DNS, intensities agree
fairly with filtered DNS and better than a damped Smagorinsky LES, and
doubling the width ratio to 4 changes mean and rms velocities by less than
3% — which the authors read as casting doubt on a priori tests as
quantitative guides.

# Version read

Version of record (AIP; received 14 November 1990, accepted 7 March 1991),
a scan of the six journal pages 1760–1765 with an AIP cover sheet (7 PDF
pages), all read; the OCR garbles the equations, which were read visually at
300–1200 dpi. Page 1 matches the Crossref metadata; the DOI is printed on the
cover sheet. The caption of Fig. 1 lists two further width ratios whose
glyphs are degraded on the scan; they are not used here. Numbering cited on
this page is that of the paper.

The archive also holds a byte-identical copy of this PDF (same MD5),
`0000_manual_no_journal_Unknown_10_1063_1_857955.pdf`; it is the same file, not another version.

# Key claims

Page-local symbols: $\mathcal T_{ij}=\widehat{\overline{u_iu_j}}-\hat{\bar u}_i\hat{\bar u}_j$
the test-level subgrid stress (the source's $T_{ij}$); $m^{\mathrm G}_{ij}$ and
$M^{\mathrm G}_{ij}$ the source's model stresses at grid and test level (its
$m_{ij}$, $M_{ij}$); $M_{ij}=\widehat{|\bar S|\bar S_{ij}}-(\hat\Delta/\Delta)^2|\hat{\bar S}|\hat{\bar S}_{ij}$
the difference tensor of the [dynamic-procedure page](/methods/dynamic-procedure.md),
which this paper does not define; $\Delta_{(i)}$, $\hat\Delta_{(i)}$ the directional
filter widths and $r_\Delta=\hat\Delta_{(i)}/\Delta_{(i)}$ their ratio (the source's
$\alpha$); $y$ the distance from the nearest wall.

1. The Smagorinsky eddy viscosity is $\nu_t=(C_s\Delta)^2|\bar S|$; Lilly found $C_s\simeq0.23$ for isotropic turbulence with the cutoff in the inertial subrange and $\Delta$ equal to the grid size, Deardorff used 0.1 in channel flow, Mason & Callen found 0.2 good on fine grids, Piomelli et al. (1988) found an optimum near 0.1 (§I, Eqs. 1–2). **Stated**
2. A single universal constant cannot model the variety of transitional and turbulent phenomena, and the Smagorinsky model cannot represent backscatter (§I). **Stated**
3. The resolved stress $L_{ij}=\widehat{\bar u_i\bar u_j}-\hat{\bar u}_i\hat{\bar u}_j$ (Eq. 10), the test-level stress $\mathcal T_{ij}$ (Eq. 9) and the test-filtered grid-level stress satisfy $L_{ij}=\mathcal T_{ij}-\hat\tau_{ij}$ (Eq. 11; Ref. 14). **Stated** (the identity follows from Eqs. 7, 9, 10)
4. With $\tau^d_{ij}\simeq m^{\mathrm G}_{ij}=-2C_s^2\Delta^2|\bar S|\bar S_{ij}$ (Eq. 12) and $\mathcal T^d_{ij}\simeq M^{\mathrm G}_{ij}=-2\hat\Delta^2|\hat{\bar S}|\hat{\bar S}_{ij}$ (Eq. 13, printed without a coefficient), substitution into Eq. 11 and contraction with $\bar S_{ij}$ gives one scalar equation for the coefficient (Eq. 15). **Derived**
5. The bracket multiplying the coefficient in Eq. 15 can vanish, making it indeterminate or ill-conditioned; a priori channel tests showed this "to be indeed the case", so the coefficient is taken as a function of $y$ and $t$ by averaging over wall-parallel planes (Eq. 16). **Stated** (evidence not shown)
6. The model (Eq. 17) "implicitly assumes similarity between the SGS stresses at the grid and test levels" (§II). **Derived**
7. The model stress vanishes wherever $L_{ij}$ does, as long as the denominator stays finite: laminar flow and solid boundaries (§II). **Stated**
8. Near the wall $m^{\mathrm G}_{ij}\propto y^3$ regardless of the filter widths, the correct asymptotics of $\tau_{12}$; "to the authors' knowledge, this is the only model that satisfies this property without the use of ad hoc damping functions" (§II). **Stated** ("it is easy to show"); the a priori trend $C_s^2\Delta^2\sim(y^+)^3$ is **Shown** in Fig. 2.
9. The modelled dissipation $m^{\mathrm G}_{ij}\bar S_{ij}$ (the negative of the registry's $\Pi$) is proportional to $\langle L_{ij}\bar S_{ij}\rangle$, of either sign, so backscatter is not ruled out; plane averaging does not localize it, local averaging would (§II). **Derived**
10. The only adjustable parameter is $\hat\Delta/\Delta>1$: too small and $L_{ij}$ is contaminated by numerical error, too large and energy-carrying structures determine the subgrid contribution (§II). **Stated**
11. A priori (channel, $Re=3300$ on centre-line velocity and half-width, width by Eq. 19), $r_\Delta=2$ gives the best agreement of the plane-averaged $\langle\tau_{12}\rangle$ and SGS dissipation with filtered DNS (Fig. 1). **Shown**
12. With $r_\Delta=2$, $\Delta$ corresponds to a wavenumber in the decaying part of the one-dimensional spectrum and $\hat\Delta$ to one in the flat part (§III). **Stated**
13. At the channel centre $C_s^2\simeq0.023$ with width Eq. 18 (square root 0.15, "about 50% larger than the value of $C_S$ used by Deardorff") and $\simeq7\times10^{-4}$ with Eq. 19 (0.026) (§III, Fig. 2). **Shown**
14. A priori in transitional flow ($t=176$, $r_\Delta=2$) the dynamic model's SGS dissipation follows the exact one (Fig. 3), while the Smagorinsky model's "is many orders of magnitude larger, and peaks much closer to the wall" (Ref. 11). **Shown** (dynamic) / **Stated** (Smagorinsky)
15. A posteriori results were insensitive to the width definition (Eq. 18 or 19); only Eq. 18 results are shown (§III). **Stated**
16. Transitional channel LES: peak wall stress within 3% of the DNS (Fig. 4); the Smagorinsky LES of Ref. 12 with van Driest damping and intermittency function is less accurate; a coarse DNS resolving the early stages (to $t\simeq170$) cannot predict the drag crisis and breakdown (§III). **Shown** / **Stated** (coarse DNS, Ref. 12)
17. RMS fluctuations and resolved shear stress at $t=176$, 200, 220 agree fairly with filtered DNS; late discrepancies are attributed to slight differences in transition onset (Figs. 5–6). **Shown**
18. "For $t\le185$ the eddy viscosity was negative for significant regions of the channel" (§III). **Shown** (no figure)
19. Fully developed LES at $Re=6100$: low wall stress from an under-resolved wall layer shows as a high log-law intercept (Fig. 7b); overall agreement "fairly good" (Fig. 7). **Shown**
20. The dynamic model gives better intensities than the Smagorinsky model of Ref. 12; the streamwise peak is near $y^+=12$ (Fig. 8). **Shown**
21. Mean streak spacing $\lambda^+=140$, "somewhat larger than the established value of 100, which is also expected of large-eddy simulations" (§III). **Shown** (value stated)
22. Skewness and flatness compare fairly well with unfiltered DNS (Fig. 9). **Shown**
23. Changing $r_\Delta$ from 2 to 4 (described as changing the first denominator coefficient of Eq. 17 "by almost a factor of 4") changes mean and rms velocities by less than 3% and wall stress by less than 6%; the maximum resolved shear stress is about 4% larger with $r_\Delta=2$ (§III). **Shown** (numbers stated)
24. The insensitivity to $r_\Delta$ "is contrary to one's expectations from the a priori tests (Figs. 1 and 3) and casts some doubt on the utility of a priori tests in providing quantitative data for LES" (§III). **Stated**
25. Outlook: other filters (box), the width-ratio sensitivity in very different flows, and local space and time averages in place of the plane average (§IV). **Stated**

With the coefficient that Eq. 15 places in front of both terms, Eq. 15 reads
$L_{ij}\bar S_{ij}=2C_s^2\Delta^2\big(\widehat{|\bar S|\bar S_{ij}}-(\hat\Delta/\Delta)^2|\hat{\bar S}|\hat{\bar S}_{ij}\big)\bar S_{ij}=2C_s^2\Delta^2M_{ij}\bar S_{ij}$,
the second term coming from test-filtering Eq. 12 in $\hat\tau_{ij}$, so Eq. 16 is
$C_s^2=\langle L_{kl}\bar S_{kl}\rangle/\big(2\Delta^2\langle M_{kl}\bar S_{kl}\rangle\big)$, and
$M^{\mathrm G}_{ij}-\widehat{m^{\mathrm G}_{ij}}=2C_s^2\Delta^2M_{ij}$ when $M^{\mathrm G}_{ij}$
carries the coefficient (the plane-averaged coefficient passes through the
wall-parallel test filter) *(compiler check, not in the sources)*. The paper
contracts with $\bar S_{kl}$; a least-squares contraction is not printed in
it.

# Printed slips

- **Eq. (13)** prints $M_{ij}=-2\tilde{\bar\Delta}^2|\tilde{\bar S}|\tilde{\bar S}_{ij}$ without the coefficient $C$, while Eq. (12) prints $-2C\bar\Delta^2|\bar S|\bar S_{ij}$ and Eq. (15) puts $C$ in front of both terms (checked at 600 and 1200 dpi).
- **Eqs. (15)–(17), second term:** on the scan the decoration of the second term of the parenthesis of Eq. (15) and of the denominators of Eqs. (16)–(17) cannot be read with certainty; a test filter spanning the product $|\bar S|\bar S_{pq}$ is not legible.
- **"Almost a factor of 4" (§III):** with the width of Eq. (18), $\hat\Delta^3=\hat\Delta_{(1)}\Delta_{(2)}\hat\Delta_{(3)}$ (no test filter in $y$), $(\hat\Delta/\Delta)^2=r_\Delta^{4/3}$ and the change from $r_\Delta=2$ to 4 is $2^{4/3}=2.52$; with Eq. (19) the factor approaches 4 where $\Delta_{(2)}\ll\Delta_{(1)},\Delta_{(3)}$ *(compiler check, not in the sources)*. The paper does not say which width the $r_\Delta=4$ run used; only Eq. (18) results are presented.
- **Note to Ref. 15:** "The high Reynolds number DNS was performed after the publication of Ref. 11", Ref. 11 being Piomelli, Zang, Speziale & Hussaini (1990).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar f$, $\bar G$, $\bar\Delta$ | $\bar\phi$, $G$, $\Delta$ | grid filter |
| $\tilde f$, $\tilde{\bar f}$, $\tilde{\bar\Delta}$ | $\hat\phi$, $\hat{\bar\phi}$, $\hat\Delta$ | **collision**: the source's tilde is the test filter, not Favre |
| $\alpha=\tilde{\bar\Delta}_i/\bar\Delta_i$ | $r_\Delta$ (page-local) | $\Delta_{(i)}=2\Delta x_i$ |
| $C_S$, $\nu_T$ | $C_s$, $\nu_t$ | |
| $C$, $C(y,t)$ | $C_s^2$ | the source compares $\sqrt C$ with $C_S$ |
| $\tau_{ij}=\overline{u_iu_j}-\bar u_i\bar u_j$ | $\tau_{ij}$ | same sign |
| $T_{ij}$ | $\mathcal T_{ij}$ (page-local) | test-level stress |
| $\mathcal L_{ij}$ | $L_{ij}$ | same sign |
| $m_{ij}$, $M_{ij}$ | $m^{\mathrm G}_{ij}$, $M^{\mathrm G}_{ij}$ (page-local) | **collision**: the source's $M_{ij}$ is the test-level model stress, not the difference tensor $M_{ij}$ |
| $\epsilon_{SGS}=m_{ij}\bar S_{ij}$ | $-\Pi$ (modelled) | negative values are forward transfer |
| $\langle\ \rangle$ | $\langle\cdot\rangle$ | average over wall-parallel planes |
| $y_w$ | $y$ | distance from the nearest wall |
| $u''_i$ | (resolved fluctuation) | $\bar u_i-\langle\bar u_i\rangle$ |
| Re | $Re$ | centre-line velocity and half-width, not $Re_\tau$ |

# Reference list

17 printed references, numbered, AIP style without titles; no DOIs. The
list is merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug. Ref. 14 (Germano, CTR Manuscript 116, 1990) is the cited
origin of the identity; Refs. 2, 4 and 14 are reports, Refs. 16 and 17
chapters; the note printed with Ref. 15 is kept. Refs. 12 (Piomelli & Zang,
Comput. Phys. Commun. 65:224) and 13 (Piomelli, Cabot, Moin & Lee, Phys.
Fluids A 3:1766), both 1991, take suffixes in printed order opposite to the
existing entries of the same works and are matched by volume and page: ref. 12 is `piomelli-1991-b`, ref. 13 `piomelli-1991`. No item is unparseable.

# Pages created or updated

Chunk 17 (2026-10-29). This source is cited on:

- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Energy backscatter and the subgrid energy flux](/definitions/energy-backscatter.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
