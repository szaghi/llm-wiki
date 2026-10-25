---
type: Source
title: "Martin-Alvarez et al. (2022) — Towards convergence of turbulent dynamo amplification in cosmological simulations of galaxies"
description: "Shows with 18 cosmological zoom-in MHD runs in RAMSES that a quasi-Eulerian refinement, which keeps the whole galaxy at the finest cell size, resolves more turbulence and gives faster small-scale dynamo growth scaling as Re^1/2 than the standard quasi-Lagrangian refinement."
resource: "doi:10.1093/mnras/stac1099"
source_kind: paper
authors: [Martin-Alvarez S., Devriendt J., Slyz A., Sijacki D., Richardson M.L.A., Katz H.]
year: 2022
venue: "Mon. Not. R. Astron. Soc. 513:3326–3344"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Monthly_Notices_of_the_Royal_Astronomical_Society_Martin-Alvarez_Towards_convergence_of_turbulent_dynamo_amplification_in_cos.pdf"
tags: [dynamo, mhd, astrophysics, numerical-dissipation, mesh-adaptation]
timestamp: 2026-10-25T19:44:00Z
---

# Summary

Martin-Alvarez et al. (2022) study how the refinement strategy of an
adaptive-mesh code changes the resolved turbulence and the
[small-scale (turbulent) dynamo](/results/small-scale-dynamo.md)
amplification of a weak seed field. The setting is cosmological zoom-in
magnetohydrodynamic simulations of a Milky Way-like galaxy. The code is the
authors' modified [RAMSES](/software/ramses.md): octree refinement, a
second-order Godunov solver and constrained transport for a face-centred
magnetic field. The induction equation is ideal ($\eta_m=0$), so all
dissipation is [numerical](/properties/numerical-dissipation.md), as in an
[implicit LES](/definitions/implicit-les.md) (a term the paper does not
use). The seed, $3\times10^{-20}$ G comoving, stays kinematically
unimportant throughout.

The contribution is a quasi-Eulerian refinement, one form of
[mesh adaptation](/methods/mesh-adaptation.md). Every cell denser than
$\rho_{\mathrm{th}}=10^{-24}$ g cm$^{-3}$ is refined to the finest level,
so the galaxy is covered by an almost uniform grid. The aim is to reduce the
number of distinct numerical viscous and resistive scales that multi-level
refinement introduces. It is compared with the standard quasi-Lagrangian
(mass-per-cell) refinement, with boosted and with fiducial supernova
feedback, at finest cell sizes from 10 to 320 pc: 18 runs.

At a fixed finest cell size, the quasi-Eulerian runs carry more small-scale
turbulence, mostly in the warm phase of the interstellar medium. At 20 pc
they reach about 1 dex more specific magnetic energy, and their growth rates
are higher. In the accretion phase their growth rate scales approximately as
$Re^{1/2}\propto h_{\min}^{-1/2}$. The quasi-Lagrangian runs follow
$h_{\min}^{-0.3}$. An adiabatic-compression estimate shows that
the extra growth is not compressional: the authors attribute it to
field-line stretching. Magnetic spectra show the peak moving to larger
scales with time, which the paper calls an "inverse cascade", and it is more
pronounced with quasi-Eulerian refinement. The authors take turbulent-box
simulations of [isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
as the reference for growth rates. All the evidence is numerical, with no
[DNS](/definitions/direct-numerical-simulation.md) reference.

# Version read

Version of record (MNRAS 513:3326–3344, open access; received 11 April
2022, original form 12 November 2021, accepted 14 April 2022), deposited on
HAL as hal-03456726v1. The PDF is the publisher's typeset article wrapped in
a HAL cover sheet: 20 pages, the cover plus journal pages 3326–3344. Page 1
matches the metadata card (title, six authors in order, DOI). Numbering on
this page is that of the published article.

# Key claims

1. In MHD galaxy-formation simulations, Powell divergence cleaning yields fast amplification, whereas Dedner cleaning and constrained transport (CT) find lower growth rates. CT methods have "significantly higher computational cost and produce considerably lower amplification rates", attributed to "the high numerical diffusivity introduced by the numerical solver" (§1). **Stated**
2. Divergence-cleaning methods report per-cell average ratios of magnetic divergence to field strength of order $10^{-1}$–$10^{-2}$, locally higher in shocks and turbulence (§1). **Stated**
3. Multi-level refinement introduces numerical diffusivity and viscosity at several scales, one per refinement level. Turbulent and magnetic energy is "dissipated significantly more than expected for the $\Delta x_{\max}$ employed", and information on small-scale structure is lost when gas crosses refinement boundaries to coarser levels (§1, §2.1). **Stated**
4. The quasi-Eulerian refinement (density threshold $\rho_{\mathrm{th}}=10^{-24}$ g cm$^{-3}$, refine to $h_{\min}$, $n_{\mathrm{expand}}=1$) resolves the warm and cold phases of the galaxy at approximately the same resolution. Quasi-Lagrangian refinement focuses on the cold dense phase and under-refines the warm and hot phases (§2.1, Fig. 2). **Shown**
5. The additional cost of quasi-Eulerian runs is "minor for resolutions below 80 pc" (printed wording). qEul20 costs about double qLag20, and evolving qEul10 to redshift about 9 costs about four times running qLag20 to redshift 2 (§2.2). **Stated** (no hardware or timings)
6. Active cell counts (Table 1, cells smaller than 320 pc, at redshifts 9 and 2, in $10^6$): qEul10 127 (–), qEul20 31 and 21, qLag20 5 and 10, qLweak20 5 and 10. **Shown**
7. At redshift about 2, the ratio of small-scale turbulent to circular velocity is comparable in the inner kpc, but about 0.5 dex higher in the outskirts of the qEul20 disc than in qLag20 (§3.1, Fig. 1). **Shown**
8. Gas-density PDFs: the boosted-feedback runs peak at $10^{-24}$–$10^{-23}$ g cm$^{-3}$ with a second peak at about $3\times10^{-25}$; qLweak20 peaks at about $10^{-21}$. The uniform 2 pc isolated disc of Iffrig & Hennebelle (2017) peaks at about $10^{-23}$, "comparable to qEul20" (§3.1, Fig. 5). **Shown**
9. Magnetic-field PDFs: qLag20 and qLweak20 peak at $B/B_0\sim5\times10^3$, qEul20 at $B/B_0\sim2\times10^4$. In this setup the refinement strategy affects amplification more than the supernova feedback strength (§3.1, Fig. 5). **Shown**
10. qEul20 shows more pronounced growth of specific magnetic energy than even the higher-resolution qLag10 and qLweak10 (§3.2, Fig. 6). **Shown**
11. In the accretion phase (fit window $t\in[0.3,1.4]$ Gyr), the quasi-Eulerian runs have higher growth rates $\Gamma_E$ at virtually all resolutions. qLag and qLweak have approximately equal rates, so refinement matters more than feedback. The runs separate for $h_{\min}\lesssim40$ pc (§3.2, Fig. 7). **Shown**
12. In the feedback phase ($t\in[1.7,3.3]$ Gyr), the lowest resolutions give negative $\Gamma_E$ (numerical resistivity, reconnection, accretion of pristine gas). Stronger supernova feedback gives higher rates, and quasi-Eulerian refinement adds only minor amplification over qLag (§3.2, Fig. 7). **Shown**
13. The predicted scaling is $\Gamma_E\propto Re^{\gamma_{Re}}$ with $\gamma_{Re}=0.5$ (incompressible, Kolmogorov) or $0.3$ (compressible, Burgers) (Schober et al. 2012). The paper takes as limits the ideal Kolmogorov scaling $Re\propto h_{\min}^{-4/3}$ (Kritsuk et al. 2011) and a linear viscosity scaling $Re\propto h_{\min}^{-1/3}$ (Rieder & Teyssier 2017a; Vazza et al. 2018), "yielding $\Gamma_\varepsilon\propto\Delta x_{\max}^{-2/3}$ and $\Gamma_\varepsilon\propto\Delta x_{\max}^{-1/3}$, respectively" (§3.2). **Stated** (see Printed slips)
14. The quasi-Eulerian growth rates follow $\Gamma_E\propto Re^{1/2}\propto h_{\min}^{-1/2}$ ("Kolmogorov turbulence + viscosity $\nu\propto\Delta x_{\max}$"). qLag and qLweak are better matched for $h_{\min}<80$ pc by $\Gamma_E\propto h_{\min}^{-0.3}$, i.e. $Re^{0.3}$, as obtained by Federrath et al. (2011) (§3.2, Fig. 7). **Shown** (reference lines drawn on the plot; no fitted exponent reported)
15. Extrapolated to 0.7 pc (the finest of the resolutions, 0.7–1.5 pc, of the 200 pc turbulent boxes of Balsara et al. 2004), the accretion-phase rates of qLag fall short ($\Gamma_E\sim10$ Gyr$^{-1}$), while qEul is comparable ($\sim60$ Gyr$^{-1}$). Bendre et al. (2015, NIRVANA, about 8 pc) find 3–8 Gyr$^{-1}$ (§3.2). **Shown**/**Stated**
16. With realistic interstellar viscosities and diffusivities, turbulent dynamo amplification should saturate at redshift $\gg6$, potentially a few hundred Myr after galaxy formation (§3.2). **Stated** (extrapolation)
17. The adiabatic-compression estimate $\mathcal C_{\mathrm{mag}}$ is nearly constant in the quasi-Eulerian runs and grows by about 2 (qLag) or 3 (qLweak) over redshifts 13 to 2. Higher resolution increases the excess of the specific magnetic energy over $\mathcal C_{\mathrm{mag}}$, and at the lowest resolutions it falls below. At redshift 2 and 20 pc, qLweak20 lies about 20 times and qEul20 almost $10^3$ times above $\mathcal C_{\mathrm{mag}}$ (§3.3.1, Fig. 8). **Shown**
18. Within the central kpc, turbulence sustains amplification longer, and qEul20 amplifies through most of the feedback phase (§3.3.2, Fig. 9). **Shown**
19. qEul20 has a turbulence-dominated interstellar medium in the accretion phase, while in the other runs thermal and turbulent energy are comparable. All runs are approximately in equipartition between small-scale turbulent and thermal energy in the feedback phase, which suggests supernova-driven turbulence. The large-scale turbulence estimate shows no important difference among runs (§3.3.3, Fig. 10). **Shown**
20. The specific turbulent energy of the warm phase is higher in qEul20 than in qLag20 and qLweak20 at virtually all times. The warm-to-total ratio falls from about 70 to about 50% in qEul and qLag but decays progressively in qLweak, and "the majority of the turbulent amplification in galaxy simulations takes place in the warm phase of the ISM" (§3.3.4, Fig. 11). **Shown** (interpretive)
21. The small-scale dynamo signature is a magnetic spectrum $E_{\mathrm{mag}}\propto k^{3/2}$ for Kolmogorov turbulence (Kazantsev 1968), from amplification at scales below the viscous scale and above the resistive one. These simulations have a numerical $Pm=\nu/\eta_m\sim2$, so amplification occurs at the smallest resolved scales (§3.3.5). **Stated**
22. At redshift 2, the runs with $h_{\min}\le80$ pc show magnetic spectra rising to a maximum slightly below the disc thickness (the paper's "inverse cascade"), most prominent for qEul. The kinetic spectra show a Kolmogorov-like $-5/3$ range for qEul and qLag, intermediate between Kolmogorov and Burgers ($-2$) for qLweak. At a few hundred pc most spectra decay as $k^{-11/4}$ (§3.3.5, Fig. 12). **Shown**
23. At redshift 8.5, all runs with $h_{\min}\le80$ pc show a weak inverse cascade to $k\sim20$ kpc$^{-1}$. Beyond the resolution wavenumber all spectra decay as $E_{\mathrm{mag}}\propto k^{-2}$, and the quasi-Lagrangian runs show bumps at refinement-level transitions (§3.3.5, Fig. 13). **Shown**
24. qEul20 spectra from redshift 12 to 2: the kinetic power grows by about 2 dex and the large-scale magnetic power by about 4 dex. The inverse cascade develops shortly after redshift 12, its onset moving from $k\sim1$ to $k<0.1$ kpc$^{-1}$, and the magnetic power at kpc scales grows by more than 6 dex (§3.3.5, Fig. 14). **Shown**
25. Zero-padding the FFT box changes the large-scale spectral shape: without padding the spectra are flatter at large scales and the inverse cascade is partly masked. The authors recommend considering zero-padding carefully (App. B, Fig. B1). **Shown**
26. The relative divergence $|\nabla\cdot\boldsymbol B/\boldsymbol B|\,\Delta x_{\mathrm{cell}}$ is virtually always below the per-cent level in all runs for the face-centred field, and negligible for cell-centred fields per oct (App. A, Fig. A1). **Shown**
27. Conclusions: switching to quasi-Eulerian refinement at a fixed maximal resolution gives about 1 dex more specific magnetic energy (Fig. 6). The extra amplification is not compressional but "produced through stretching of magnetic field lines". Unresolved amplification could alternatively be modelled with sub-grid methods (Liu, Kretschmer & Teyssier 2021) (§4). **Shown**/**Stated**

# Printed slips

- **Growth-rate limits (§3.2, pp. 3334–3335):** "linear scaling of the hydrodynamical viscosity with resolution (${\rm Re}\propto\Delta x_{\max}^{-1/3}$ …), yielding $\Gamma_\varepsilon\propto\Delta x_{\max}^{-2/3}$ and $\Gamma_\varepsilon\propto\Delta x_{\max}^{-1/3}$, respectively". *(Compiler check, not in the sources)*: with $\Gamma_E\propto Re^{1/2}$, $Re\propto h_{\min}^{-4/3}$ gives $h_{\min}^{-2/3}$, but $Re\propto h_{\min}^{-1/3}$ gives $h_{\min}^{-1/6}$. The fiducial pairing "viscosity $\nu\propto\Delta x_{\max}$" with $\Gamma_E\propto Re^{1/2}\propto h_{\min}^{-1/2}$ implies $Re\propto h_{\min}^{-1}$, not $h_{\min}^{-1/3}$.
- **Empty interval (§3.1, p. 3332):** "the redshift range 3 < z < 2"; the Fig. 5 caption gives "(3 ≳ z ≳ 2)".
- **Fig. 5 caption:** it lists the magnetic field in the bottom right panel, then says "the magnetic field in the bottom left-hand panel displaying a higher strength for qEul20"; §3.1 also says "bottom right-hand panel of Fig. 5 confirms".
- **Fig. 11 caption:** "qEul20 and qLag20 contain a stable fraction … whereas this ratio decreases for qLag20 throughout the feedback phase"; §3.3.4 names qLweak20 for the decay.
- **Line styles:** §3.3.3 calls the global-turbulence proxy "an additional set of dashed lines" and then "the dotted lines", while the Fig. 10 caption calls it "solid clear lines". In §3.3.5 the rotation-subtracted spectra are "dot-dashed lines", then "dashed lines diverge from their solid counterparts".
- **Exponent notation (§3.3.5):** "most energy spectra decay as $\alpha\sim k^{-11/4}$", where $\alpha$ is the spectral exponent of $E\propto k^\alpha$.
- **Volume factor (Eq. 5):** the per-cell term $\epsilon_{\mathcal C_{\rm mag},i}$ already contains ${\rm d}x_i^3$, and the total is then formed by summing "$V_{\rm cell}\epsilon_{\mathcal C_{\rm mag},i}$".
- **End redshift of qEul10:** "z ∼ 8.5" (Table 1 note, §2.2), "z = 8.5" (Fig. 6 caption), "only evolved to z ∼ 8" (§3.2), and "evolving qEul10 to z ∼ 9" (§2.2).
- **Mass resolutions (§2):** "Stellar and dark matter particles have mass resolutions of $M_{\rm DM}\simeq5\times10^4$ and $M_*\simeq5\times10^3\,M_\odot$, respectively": the word order is opposite to the symbols.
- **Entropy units (§3.1):** the phase thresholds $s_{\rm cold}$, $s_{\rm hot}$ are printed in erg K$^{-1}$ s$^{-1}$.

# Notation map

| Martin-Alvarez et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\boldsymbol v$ | $\boldsymbol u$ | gas velocity in the galaxy frame |
| $\boldsymbol B$, $B_0$ | $\boldsymbol B$, (seed strength) | Gaussian units; **collision:** $B_0$ is the comoving seed, not a guide field |
| $\eta$ | $\eta_m$ | magnetic diffusivity, set to zero; **collision** with the Kolmogorov length |
| $\nu$, Pm, Re | $\nu$, $Pm$, $Re$ | numerical viscosity; $Re$ defined only through its scaling with resolution |
| $\Delta x_{\max}$ | $h_{\min}$ (page-local) | cell size at the maximum refinement level, i.e. the finest cells; run names (qEul20 …) give it in pc |
| $\Delta x_{\rm cell}$ | $h$ | local cell size |
| $\Gamma_\varepsilon$ | $\Gamma_E$ (page-local, as on [small-scale dynamo](/results/small-scale-dynamo.md)) | exponential growth rate of the specific magnetic energy (Gyr$^{-1}$) |
| $\gamma$ (in $\Gamma_\varepsilon\propto{\rm Re}^\gamma$) | $\gamma_{Re}$ (page-local) | **collision** with the ratio of specific heats, which the paper also mentions (5/3) |
| $\alpha$ | (fit normalization; spectral exponent) | **collision** with the registry blending factor; overloaded in the source |
| $\varepsilon_X=E_X/M_{\rm gas}$, $\epsilon_{\rm mag}$ | (specific energy; magnetic energy density) | **collision:** $\varepsilon$ is not the dissipation rate |
| $\bar v_i(\mathcal L_{\rm turb})$, $v_{\rm turb}$ | (top-hat local mean over a sphere of radius $4h_{\min}$; small-scale turbulent velocity) | an analysis filter, neither the LES overbar nor a Reynolds average |
| $\mathcal C_{\rm mag}$ | $\mathcal C_{\mathrm{mag}}$ (page-local) | adiabatic-compression estimate, $B\propto\rho^{2/3}$ |
| $E_{\rm mag}(k)$, $E_{\rm kin}(k)$, $k$ | magnetic and kinetic spectra, $k$ | $k$ is the wavenumber (kpc$^{-1}$), spectral-page convention |
| $k_\nu$, $k_\eta$, $k_{\rm res}=\pi/\Delta x_{\max}$ | viscous, resistive, resolution wavenumbers | |
| $\eta_{\rm SN}$, $\eta_{\rm metals}$ | (supernova mass fractions) | not a diffusivity |
| $z$ | (cosmological redshift) | **collision:** not the spanwise coordinate |

# Reference list

102 printed references, author–year style (MNRAS), no titles and no DOIs
printed. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Same-author
same-year works are disambiguated in printed order (Balsara & Kim 2004 and
Balsara et al. 2004; Rieder & Teyssier 2017a, b). Items incomplete as
printed: Gent 2012 ("PhD thesis, p. 153", no institution), Liu, Kretschmer
& Teyssier 2021 ("MNRAS, 1", no volume), Kimm et al. 2017 (article
identifier "stx052" as page). "Pudritz R. E., Silk J., 2002, ApJ, 342, 650"
is recorded as printed; its year and volume are not verified here. No
printed duplicates or unparseable items.

# Pages created or updated

Chunk 2 (2026-10-25). This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Mesh adaptation for turbulent-flow simulation](/methods/mesh-adaptation.md)
- [Subgrid turbulent dynamo model](/methods/subgrid-turbulent-dynamo-model.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Small-scale turbulent dynamo](/results/small-scale-dynamo.md)
- [RAMSES](/software/ramses.md)
