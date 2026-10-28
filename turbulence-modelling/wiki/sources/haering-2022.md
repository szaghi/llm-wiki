---
type: Source
title: "Haering et al. (2022) — Active model split hybrid RANS/LES"
description: "Proposes active model split (AMS) hybrid RANS/LES: the subgrid stress is split into a mean-stress part from a scaled RANS model and an energy-transfer part from an anisotropic tensor viscosity, with active forcing driven by an anisotropic resolution-adequacy parameter; tested on channel flow and the periodic hill."
resource: "doi:10.1103/physrevfluids.7.014603"
source_kind: paper
authors: [Haering S.W., Oliver T.A., Moser R.D.]
year: 2022
venue: "Phys. Rev. Fluids 7:014603"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Physical_Review_Fluids_Haering_Active_model_split_hybrid_RANSLES.pdf"
tags: [hybrid-rans-les, les, rans, sgs-model, eddy-viscosity, log-layer-mismatch]
timestamp: 2026-10-28T07:10:00Z
---

# Summary

Haering et al. (2022) propose [active model split](/methods/active-model-split.md) (AMS), a
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) framework aimed at four deficiencies the authors
find in most hybrid methods:

- passive generation of resolved turbulence after the modelled stress is reduced, which causes
  modelled-stress depletion;
- a single scalar eddy viscosity asked to carry both the mean subgrid stress and the energy transfer;
- ad hoc RANS-to-LES blending functions built on scalar grid measures;
- RANS transport equations fed with fluctuating inputs.

The core idea is model splitting. The [Boussinesq](/definitions/boussinesq-hypothesis.md) form is
replaced by $\tau^d_{ij}\approx-2\nu_s\langle\bar S_{ij}\rangle-2\nu_e\bar S'_{ij}$, with two non-fluctuating
viscosities: $\nu_s$ acts on the mean strain and $\nu_e$ on the resolved fluctuating strain.
Gradient-diffusion scaling on a triple decomposition gives $\nu_s=\alpha_k(2-\alpha_k)\nu_{\mathrm{tot}}$
and $\nu_e=\alpha_k(1-\alpha_k)\nu_{\mathrm{tot}}$, with $\alpha_k=k_{\mathrm{sgs}}/k_{\mathrm{tot}}$.
Box-filtered [channel](/benchmarks/turbulent-channel-flow.md) DNS at $Re_\tau=1000$ supports this
and gives $\alpha_k=\beta_k^{1.7}$, with $\beta_k=1-k_{\mathrm{res}}/k_{\mathrm{tot}}$ computable in
the simulation.

In AMS, the mean stress is the RANS stress evaluated on a causal pseudo-mean and scaled by
$\alpha_k(2-\alpha_k)$. The energy transfer comes from the anisotropic M43 tensor viscosity driven by
the RANS $\varepsilon$. A Taylor–Green-structured active forcing injects resolved fluctuations wherever
an anisotropic resolution-adequacy parameter, built from the resolution tensor, shows the grid can
resolve more. No blending function is used.

In a second-order finite-volume code, channel flow at $Re_\tau\approx5200$ on grids with
$\Delta x^+\approx700$–$1550$ shows no [log-layer mismatch](/definitions/log-layer-mismatch.md) and
nearly grid-independent means. At $Re_\tau=20{,}000$ the mean is distorted, which the authors
attribute to the RANS model. On the [periodic hill](/benchmarks/periodic-hill.md) at $Re_h=10{,}600$,
grids 14 to 62 times smaller than a wall-resolved LES reproduce reattachment and mean velocity. The
paper criticizes [PANS](/methods/partially-averaged-navier-stokes.md), DES and blending approaches,
and the use of SST's $k$ ([$k$-$\omega$ SST](/methods/k-omega-sst-model.md)). It tests an implicit,
upwinding energy-transfer model ([implicit LES](/definitions/implicit-les.md)), and it compares cell
counts with [wall-modelled LES](/methods/wall-modelled-les.md).

# Version read

Accepted manuscript distributed through CHORUS, dated 21 December 2021: 49 PDF pages (a CHORUS/APS
cover plus 48 manuscript pages: text pp. 1–41, appendices pp. 42–45, references pp. 45–48). It is
not the journal typeset version. Title and authors in this order match the published version; the
metadata above are those of the published version (Crossref). Equations were read visually on
pp. 7–19 and 42–45 because the text layer garbles them. Page, equation and figure numbers on this
page are those of the manuscript.

# Key claims

The source writes the subgrid stress with the opposite sign to the registry; the claims below are
translated (see the Notation map).

1. Hybrid methods that generate resolved turbulence passively, by reducing the modelled stress, "must exhibit regions of modeled-stress-depletion (MSD)"; introducing resolved fluctuations explicitly at a rate consistent with the reduction "is the only way to prevent regions of MSD" (§II A, p. 4). **Stated**.
2. Body forcing can be read formally as a model of the commutator between the implicit filter and the substantial derivative (§II A, p. 5). **Stated**.
3. A single eddy viscosity cannot represent both the mean subgrid stress and the energy transfer: the correlation between subgrid stress and resolved strain in filtered turbulence is "of order 20% or less", against one for an eddy-viscosity model; citing Jiménez & Moser, the dynamic Smagorinsky model gives subgrid stresses "nearly five times smaller than the true filtered stress" in channel flow (§II B, pp. 5–6). **Stated** (cited).
4. The cube root of the cell volume tends to the smallest cell length at high aspect ratio and overestimates the effective resolution; cell-diagonal measures are preferable (§II C, p. 6). **Stated**.
5. Feeding fluctuating $k$ and $\varepsilon$ to the RANS destruction term $C_{\varepsilon2}\varepsilon^2/k$ makes its mean a complicated function of the resolved fraction, shown by a second-order Taylor expansion (Eq. 2); "what goes in to, and what comes out of, RANS-based transport models must be expected values" (§II D, p. 7). **Derived**.
6. Mean-flow accuracy requires two statistical conditions on the subgrid model: the mean deviatoric stress, $\langle\tau^d_{ij}\rangle\approx-\langle2\nu_t\bar S_{ij}\rangle$ (Eq. 4), and the mean energy transfer, $\langle\tau_{ij}\partial_j\bar u_i\rangle\approx-\langle2\nu_t\bar S_{ij}\partial_j\bar u_i\rangle$ (Eq. 5); RANS models are built for the first only, LES models calibrated for the second only (§III, pp. 8–9). **Derived/Stated**.
7. The split form $\tau^d_{ij}\approx-2\nu_s\langle\bar S_{ij}\rangle-2\nu_e\bar S'_{ij}$ (Eq. 8) can meet both conditions for flows with a one-dimensional mean, provided $\nu_s$ and $\nu_e$ do not fluctuate; otherwise cross-contributions appear (§III A, p. 9). **Derived**.
8. Gradient-diffusion scaling on the triple decomposition gives $\nu_s=\alpha_k(2-\alpha_k)\nu_{\mathrm{tot}}$ and $\nu_e=\alpha_k(1-\alpha_k)\nu_{\mathrm{tot}}$ (Eq. 23), so $\tau^d_{ij}=-2\nu_t\bar S_{ij}$ "is not generally valid": mean and fluctuating gradients scale differently (§III B, Eqs. 15–24, pp. 11–12). **Derived**. *(Compiler check, not in the sources: Eq. 21 minus Eq. 22 gives the coefficients $2\alpha_k-\alpha_k^2$ and $\alpha_k-\alpha_k^2$, as printed.)*
9. For filters and projections that minimize the $L^2$ error the mixed terms vanish; for second-order finite volume, closest to box filtering, they do not, so $\alpha_k\neq\beta_k$ (§III B, p. 12). **Stated**.
10. Box filtering of channel DNS at $Re_\tau=1000$ ($y^+<300$ excluded, six filter sizes, six snapshots) gives $\alpha_k=\beta_k^{1.7}$; in isotropic turbulence at infinite Reynolds number the Kolmogorov spectrum gives $\alpha_k\propto\beta_k$ (§III B, Fig. 1a). **Shown**.
11. The ratio of subgrid to total shear stress from the same data is consistent with $\alpha_k(2-\alpha_k)$, although $\alpha_k^{9/8}(2-\alpha_k)$ fits slightly better (Fig. 1b). **Shown**.
12. Using the true mean in the AMS formulation "yields poor simulation results" (determined empirically); a pseudo-mean keeping only the largest and slowest scales represents the mean stress better (§IV A, p. 14). **Stated** (not shown).
13. SST's $k$ is unsuitable as $k_{\mathrm{tot}}$: in attached boundary layers it is "more akin to $\frac32\overline{v^2}$"; the RANS $k$ must represent the turbulent kinetic energy (§IV B, p. 14). **Stated**.
14. With a non-fluctuating (or uncorrelated) energy-transfer viscosity, the mean of the energy-transfer stress vanishes, so the two stress parts are exactly the mean and fluctuating parts of the model stress (§IV C, p. 15). **Derived**.
15. The resolution indicator $r_{\mathcal M}$ (Eq. 34) is a conservative upper bound on the directional resolution ratio; for an isotropic grid and isotropic equilibrium turbulence it reduces to a DES-like length-scale comparison, "an anisotropic generalization of the DES resolution metric" (§IV D 1, p. 17). **Derived/Stated**.
16. In the DNS limit all model terms (both stresses and the forcing) vanish: AMS "is essentially an LES that by construction respects both RANS and DNS limits" (§IV E, p. 19). **Stated**.
17. The Taylor–Green forcing is not divergence-free; in the incompressible solver its dilatational part is projected out, and in compressible solvers it "may result in spurious acoustic sources" (§IV E, p. 20; §V A 2, p. 24). **Stated**.
18. Channel at $Re_\tau\approx5200$ on four grids: all predict the mean adequately, with no log-layer mismatch; $\beta_k$ drops to 0.4 at the centre on the fine grid, beyond the $\beta_k\lesssim0.1$ that typical LES needs, "enabling true 'coarse' LES" (§V A 1, Figs. 2–3). **Shown**.
19. The RANS $k$ in AMS stays "virtually unchanged" from pure RANS despite the modified production, and the two measures of the turbulent kinetic energy nearly coincide (§V A 1, Fig. 3b). **Shown**.
20. The resolution anisotropy ranges from 2:1 to 20:1, and the converged means indicate that the resolution-adequacy parameter works on anisotropic grids (§V A 1, p. 23). **Shown**.
21. Temporal transition from RANS on the coarse grid overshoots: $\beta_k$ drops to 0.4 at $t_f=1.6$ against a steady minimum of about 0.6; the mean is blunted, then heals by $t_f=8$ (§V A 2, Figs. 4–6). **Shown**.
22. Spatial transition from a RANS inlet in a $16\pi$-long channel shows no overshoot; $\beta_k$ falls only to "just under 0.7" after $12\pi$, so the forcing relies on streamwise periodicity to be most effective (§V A 3, Figs. 5b, 7). **Shown**.
23. At $Re_\tau=20{,}000$ with $\overline{v^2}$–$f$, AMS produces an outer peak of $k$ but the mean departs from the log law for $y^+=200$–$2000$; the authors attribute this to the RANS model, whose $k$ no longer predicts the Reynolds stress there (§V A 4, Fig. 8). **Shown**.
24. Periodic hill at $Re_h=10{,}600$: AMS improves reattachment over RANS (RANS about $x=7$, reference about $x\approx4$); the mean streamwise velocity matches experiment and wall-resolved LES "quite well for all resolutions"; near separation the vertical velocity stays close to RANS because $\beta_k\approx1$ in the separating shear layer (§V B, Figs. 9–11). **Shown**.
25. AMS gives "nearly identical results to the wall-resolved LES of [48] at a resolution reduction of over an order-of-magnitude and computational costs reduced by a factor of 30 or more due to larger timesteps"; the fine grid gives excess $R_{xx}$ and $R_{yy}$ in the recirculation (§V B, Fig. 12). **Shown** (cost factor **Stated**, no timings).
26. A wall-modelled LES of the hill with spacings at most 8%, 2% and 5% of $\delta$ would need about 12M cells on a structured grid or 1.6M with streamwise variation, both above the fine AMS grid of 0.9M (§V B, p. 35). **Derived** (estimate).
27. Reducing $C_r$ from 1 to 0.5 on the coarse channel lowers the centre $\beta_k$ from "just above 0.5" to 0.2 with slight changes of the mean; $C_r<0.5$ distorts mean and $k$; on the hill $C_r=0.2$ gives the best mean velocity by error cancellation; $C_r=0.5$ "may be more appropriate for the numerical schemes used here" (§V C, Figs. 13–15). **Shown**.
28. Among energy-transfer models on the fine channel the anisotropic M43 performs best, the $\alpha_k$-based and the implicit upwinding (iSGET) models perform well, and the isotropic M43 overpredicts the wall stress; "the M43 model does require the anisotropic form to perform well" (§V D, Fig. 16). **Shown**.
29. Using fluctuating-viscosity models (Smagorinsky, Vreman, WALE) for the energy-transfer part would require computing their contribution to the mean stress and adjusting the mean-stress model (§V D, p. 40). **Stated**.
30. AMS gives consistent channel results over a horizontal-resolution range of "a factor of at least 2.2" and hill results on grids "up to 60 times smaller" than LES; "model splitting like that described here is how LES should generally be performed" (§VI). **Stated**. *(Compiler check, not in the sources: $1552/701\approx2.2$ from Table I and $13\text{M}/0.21\text{M}\approx62$ from Table II.)*

# Printed slips

- Eq. (1) reads $2\overline{\partial_j\partial_ku_i\,\partial_j\partial_ku_i}\approx C_{\varepsilon2}\varepsilon^2/k$. *(Compiler check, not in the sources: the left side has dimension $\mathrm{L^{-2}T^{-2}}$ and the right side $\mathrm{L^2T^{-4}}$; a factor $\nu^2$ on the left would balance them.)*
- §V A 3, p. 26: profiles of the spatially developing case are said to be "presented in Fig. 3b"; they are in Fig. 5b (Fig. 3b is the stationary-channel TKE). §V A 2, p. 25: "the wall-normal plane shown in Fig. 5" refers to Fig. 4.
- The resolved-plus-modelled TKE is "the time-averaged resolved turbulence plus α times the RANS $k^+$" in the captions of Figs. 3 and 8, but "plus β times" in the captions of Figs. 13 and 16 and $(\frac12\langle u^>_iu^>_i\rangle+\beta k)$ in the text, p. 23; by the paper's own definition $k_{\mathrm{sgs}}=\alpha k_{\mathrm{tot}}$.
- The coarse-grid steady $\beta$ "only achieves a minimum of about 0.6" (§V A 2, p. 24) but is "just above 0.5" at the centre with $C_r=1$ (§V C, p. 36).
- p. 12: "the subgrid-subgrid term of (III B)": a section label where an equation number is meant.
- $\zeta$ is $3\overline{v^2}/(2k)$ in Eq. (33) but the eddy-viscosity factor ($f_\mu$, or $\overline{v^2}/k$) in Table V; Eq. (B3) uses $\hat{\mathcal M}$ without defining it.
- §IV E, p. 19 lists "under-utilized resolution evaluation" among the AMS components; Fig. 7 caption uses $h$ ("sections of 4h") for the channel, where the text uses $\delta$.
- Eq. (A1) prints the diffusion term as $\partial_k\big(\partial_k\kappa_\phi\phi\big)$, which read literally differentiates the product $\kappa_\phi\phi$, while Tables III–IV give $\kappa_\phi$ as a diffusivity ($\nu+\nu_t/\sigma$).
- Typos: "emperically" (p. 14), "psuedo-mean"/"puesdo-mean", "spitting of the model" (p. 3), "stesses" (p. 8), "near walls were grid scales" (p. 3), "log-layer miss-match" (p. 40).
- Reference list: refs. [22] and [34] are the same work (Girimaji, J. Appl. Mech. 73, 2005) printed twice; [87] "Chapman?s"; [55] "DaneshTafti" without an initial; [13] an empty field; [61] no volume or pages.

# Notation map

| Haering et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\tau^{sgs}_{ij}=-(\overline{u_iu_j}-\overline u_i\overline u_j)$ | $-\tau_{ij}$ | **sign opposite to the registry**; $2k_{sgs}$ is the trace of $-\tau^{sgs}_{ij}$ |
| $\tau^s_{ij}$, $\tau^e_{ij}$, $\tau^R_{ij}$ | — | mean-stress and energy-transfer parts of the model stress, RANS stress on the pseudo-mean; all in the source sign |
| $\langle\cdot\rangle$, $u'_i$ | $\langle\cdot\rangle$, $u'_i$ | Reynolds mean and fluctuation |
| $\overline{(\cdot)}$ | $\bar\phi$ | implicit LES filter (projection on the discrete space); the bar of $\overline{v^2}$ is a RANS variable name |
| $u^>_i$, $S^>_{ij}$, $u^<_i$ | $\bar u_i'$, $\bar S'_{ij}$ (page-local on the AMS page), $\phi^<$ | resolved fluctuation and its strain, with $\bar u_i=\langle u_i\rangle+u^>_i$ (here $u^>$ excludes the mean, unlike the registry's $\phi^>$); subgrid fluctuation |
| $\overline{v^2}$ | $v^2$ (page-local on the AMS and SST pages) | wall-normal velocity variance variable of the $v^2$-$f$ model |
| $\{\cdot\}$, $[\cdot]$ | — | pseudo-mean (causal exponential time filter, $C_\phi=1$ and $4$) |
| $\nu_s$, $\nu_e$, $\nu_{tot}$ | $\nu_t$ family | mean-stress, energy-transfer and total eddy viscosities |
| $k_{tot}$, $k_{sgs}$, $k_{res}$ | $k_{\mathrm{tot}}$, $k_{\mathrm{sgs}}$, $k_{\mathrm{res}}$ | as in the registry; $k_{tot}$ from the RANS $k$-equation |
| $\alpha$ | $\alpha_k$ (registry §11) | $k_{sgs}/k_{tot}$; **collision** with the DG blending factor |
| $\beta$ | $\beta_k$ (registry §11) | $1-k_{res}/k_{tot}$; **collision** with the field-inversion $\beta(\boldsymbol x)$ |
| $\langle S\rangle=(\langle S_{ij}\rangle\langle S_{ij}\rangle)^{1/2}$ | $\lvert\langle S\rangle\rvert/\sqrt2$ | **no factor two** (App. A) |
| $\zeta$ | — | anisotropy measure $3\overline{v^2}/(2k)$ (Eq. 33), overloaded in Table V; **collision** with the feature vector $\boldsymbol\zeta$ |
| $\mathcal M_{ij}$, $r_{\mathcal M}$, $C_r$ | — | resolution tensor, resolution-adequacy parameter and its coefficient |
| $\rho(\mathbf e)$ | — | directional resolution ratio (Eq. 32), not the density |
| $\eta$, $F_r$, $D_{lim}$ | — | forcing limiters; $\eta$ **collides** with the Kolmogorov length, $F_r$ with the SATES resolution control function (registry §11) |
| $\delta_w$, $\delta^+$ | $d$, $y^+$ | wall distance and its wall-unit form |
| $Re_h$ | $Re_h$ | hill-height Reynolds number |

# Reference list

88 printed references in numbered (Phys. Rev.) style, all merged into the
[bibliography](/bibliography.md) with `citedby` this slug. Refs. [22] and [34] are the same work
(Girimaji 2005) printed twice and are folded into one entry. Haering et al. 2019 is cited twice
for two different works ([49], AIAA Scitech; [73], the M43 paper), which take suffixes in printed
order. Ref. [88] is an arXiv preprint and is kept as its own entry. Ref. [56] is kept with its
printed year 2020. No DOIs are printed; incomplete items are listed under Printed slips, and none
is unparseable.

# Pages created or updated

Chunk 1 (2026-10-25), cited further in chunks 2, 4, 8. This source is cited on:

- [Periodic hill](/benchmarks/periodic-hill.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Log-layer mismatch](/definitions/log-layer-mismatch.md)
- [Active model split hybrid RANS/LES](/methods/active-model-split.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [k-ε models](/methods/k-epsilon-model.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [Partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md)
- [Scale-adaptive simulation](/methods/scale-adaptive-simulation.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
- [Vreman model](/methods/vreman-model.md)
- [WALE model](/methods/wale-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
