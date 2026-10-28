---
type: Source
title: "Adhikari et al. (2023) — Theory and Transport of Nearly Incompressible Magnetohydrodynamic Turbulence: High Plasma Beta Regime"
description: "Derives the leading-order nearly incompressible MHD equations for high plasma beta, fully three-dimensional with 2-D and slab fluctuations at the same order, builds from them a six-equation Elsasser-energy and correlation-length transport model with pickup-ion sources, and compares it with Voyager 2, Ulysses and New Horizons data from 1 to 75 au."
resource: "doi:10.3847/1538-4357/acde57"
source_kind: paper
authors: [Adhikari L., Zank G.P., Wang B., Zhao L., Telloni D., Pitna A., Opher M., Shrestha B., McComas D.J., Nykyri K.]
year: 2023
venue: "Astrophys. J. 953:44"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_The_Astrophysical_Journal_Adhikari_Theory_and_Transport_of_Nearly_Incompressible_Magnetohydrody.pdf"
tags: [mhd, plasma, astrophysics, compressible]
timestamp: 2026-10-28T07:11:00Z
---

# Summary

Adhikari et al. (2023) extend nearly incompressible (NI) MHD, the expansion
of [compressible MHD](/results/compressible-mhd-turbulence.md) in a small
turbulent Mach number $M_t$ about an inhomogeneous background, to a plasma
of high beta ($\beta_p\gg1$), as met in the outer heliosphere where pickup
ions raise the total plasma beta. In this regime the leading-order equations
are incompressible but fully three-dimensional: two-dimensional structures
(flux ropes, magnetic islands) and slab Alfvén waves enter at the same
order, and the Alfvén speed appears. At low and order-one beta, by
contrast, the leading order is two-dimensional, without the Alfvén speed,
and the slab part is a higher-order correction (the homogeneous,
strong-guide-field limit is on [reduced MHD](/definitions/reduced-mhd.md)).
The leading-order velocity is
not solenoidal, so the Elsasser equation (Eq. 7) differs from its
incompressible versions.

With the moment closures of Zank et al. (2012a) (a von Kármán–Taylor
cascade term, two-dimensional mixing tensors, a neglected density-gradient
correlation), they write six transport equations for the Elsasser energies,
the residual energy and their three correlation lengths (Eqs. 8–11). They
reduce them to a steady, spherically symmetric form with a stream-shear and
a pickup-ion source (Eqs. 12–15), add a density-variance equation, and
couple everything to a three-fluid (proton, electron, pickup ion) solar
wind heated by the turbulent dissipation. The model transports Elsasser
energies and correlation lengths; it carries no Reynolds or subgrid stress.

From 1 to 75 au the model agrees, "with some scatter", with 27 years of
Voyager 2 data, Ulysses electron temperatures and New Horizons pickup-ion
data, except for the correlation lengths of the residual energy and of the
velocity. The pickup-ion source flattens the Elsasser energies beyond about
25 au. The normalized cross-helicity and residual energy are reported at
1 au and along the trajectory; they bear on the imbalance and
residual-energy discussion of [critical balance](/properties/critical-balance.md).

# Version read

Version of record (AAS, open access, published 1 August 2023); 14 pages,
all read, pp. 2–6 and 13 visually for the equations. Page 1 matches
Crossref. Equation, section and table numbers are those of the version of
record.

# Key claims

1. In a $\beta_p\gg1$ plasma the leading-order NI MHD equations are fully incompressible and carry both two-dimensional structures and slab (Alfvén-wave) fluctuations at the same order, so the two cannot be told apart at leading order (abstract; §1; §2 after Eq. 6). **Derived**
2. For $\beta_p\ll1$ or $\beta_p\sim1$ the leading order is two-dimensional (structures only), and the higher-order correction carries a minority slab component and a compressible magnetosonic component; both orders are needed for 2-D plus slab turbulence (§1; §2). **Stated** (citing Zank & Matthaeus 1992–1993, Hunana & Zank 2010, Zank et al. 2017)
3. The leading-order Elsasser equation (Eq. 7) contains the Alfvén velocity, "which confirms that the leading-order transport equation in the $\beta\gg1$ plasma is fully 3D", unlike Eq. (63) of Zank et al. (2017) at low beta (§2). **Derived**
4. The leading-order fluctuating velocity is not solenoidal, $\nabla\cdot\boldsymbol u^\infty=-\rho_{sw}^{-1}\boldsymbol u^\infty\cdot\nabla\rho_{sw}$ (Eq. 6), so Eq. (7) differs from the incompressible Elsasser equations of Marsch & Tu (1989) and Zhou & Matthaeus (1990), and Eqs. (8)–(11) from Eqs. (42)–(46) of Zank et al. (2012a) (§2; §8). **Derived**
5. Six coupled transport equations for $\langle|\boldsymbol Z^\pm|^2\rangle$, $E_D$, $\ell^\pm$ and $\ell_D$ (Eqs. 8–11) follow with the closures (i)–(iii) and (A10), (C10) of Zank et al. (2012a) (§2; App. Eqs. 35–36). **Derived**
6. Structural similarity parameters $a_s=b_s=1/2$ give the two-dimensional form of the mixing tensors (§2, closure 2). **Stated**
7. Assuming isotropic turbulence, $\langle\boldsymbol Z^\pm\cdot\nabla\rho_{sw}\rangle\sim0$, unlike the treatment of Zank et al. (2017) (§2, closure 3). **Stated**
8. In steady one-dimensional form, with a super-Alfvénic wind much faster than the Alfvén speed, the model reduces to Eqs. (12)–(15), with a shear source decaying as $r^{-2}$ (Zank et al. 2017) rather than the $r^{-1}$, energy-proportional source of earlier models (§3). **Derived**
9. The von Kármán–Taylor constant is $\alpha_{\mathrm{KT}}=0.03$, chosen so that the turbulent heating is not excessive and the proton and electron temperatures resemble the observations; earlier works used 1, 0.8 and 0.128; $\beta_{\mathrm{KT}}=\alpha_{\mathrm{KT}}/2$ (§3; Table 2). **Stated**
10. Shear-source strengths $c^\pm=0.3$, $c_{E_D}=0.7$ (against about 13 in Zank et al. 1996 and 1–2 in Smith et al. 2006); $\Delta U=200$ km s$^{-1}$; Alfvén speed 45 km s$^{-1}$ at 1 au (§3; Table 2). **Stated**
11. The pickup-ion source fraction is $f_D=0.06$, after Isenberg et al. (2023); pickup ions drive only Alfvénic fluctuations, so the residual-energy equation has no pickup-ion source (§3). **Stated**
12. Density-variance transport (Eqs. 17, 19) with $\alpha_2=0.05$, $\eta_1=1.8\times10^{-4}$ (text), $\eta_2=1.5\times10^{-10}$; the small $\eta_2$ means the pseudosound correction does not matter (§4; Table 2). **Stated**
13. The large-scale energy-transfer rate is set equal to the dissipation rate (fully developed turbulence), so the dissipation physics need not be modelled; the dissipated energy heats protons with fraction $f_p=0.6$ and electrons with $1-f_p$ (§5, Eqs. 27–30). **Stated**
14. Theoretical and observed outward Elsasser energy decrease with distance until about 25 au and then flatten, the flattening due to the pickup-ion source (§6, Fig. 1). **Shown**
15. The observed normalized cross-helicity, $\sigma_c\approx-0.38$ at 1 au, increases slowly with distance; the theory is consistent with it from 1 to 75 au (§6, Fig. 1). **Shown**
16. The observed normalized residual energy, $\sigma_r\approx-0.28$ at 1 au, decreases slowly until about 20 au and then increases; the theoretical one stays negative over 1–75 au (magnetic energy dominating); the observed one is negative until about 40–50 au (§6, Fig. 1). **Shown**
17. $\langle B^2\rangle^{1/2}/B$ is about constant between 1 and 2 au and then decreases, unlike the radial increase inside 1 au found from Parker Solar Probe data (Chhiber 2022), a difference assigned to the radial against azimuthal dominance of the mean field (§6, Fig. 2). **Shown**
18. The density variance falls as $r^{-4.48}$ (theory) and $r^{-4.71}$ (observation), faster than $r^{-4}$ (§6, Fig. 3; §8). **Shown**
19. $\ell^\pm$ and the magnetic correlation length grow until about 20 au and then decrease slightly, in agreement with observation; the theoretical $\ell_D$ and velocity correlation length disagree with the roughly constant observed ones, which the authors assign to the shear source derived for low-beta models (§6, Fig. 4). **Shown**
20. The pickup-ion density is about $5\times10^{-7}$ cm$^{-3}$ at 1 au and peaks near $10^{-3}$ cm$^{-3}$ at about 8 au, consistent with New Horizons (§7, Fig. 5). **Shown**
21. The theoretical pickup-ion temperature decreases as $r^{-0.18}$ and agrees with observation between about 11 and 52 au (§7, Fig. 5). **Shown**
22. The theoretical electron temperature agrees with Ulysses between 4 and 6 au; proton and electron temperatures rise in the outer heliosphere from pickup-ion-driven turbulence dissipation (§7, Fig. 5). **Shown**
23. Proton and electron beta stay below 1 from 1 to 75 au; the pickup-ion beta is about $5\times10^{-6}$ at 1 au and 11.4 at 75 au; the total beta is about 1 between 1 and 10 au and about 11.4 at 75 au (§7, Fig. 6; §8). **Shown**
24. The solar-wind speed decreases by about 19% at 75 au through pickup (§7, Fig. 7). **Shown**
25. The comparison "shows that the NI MHD turbulence transport equations can describe the evolution of turbulence throughout the heliosphere" (§8). **Stated**

The Elsasser-energy equation (Eq. 8), in registry form:

$$\partial_t\langle|\boldsymbol Z^\pm|^2\rangle+(\boldsymbol U\mp\boldsymbol V_A)\cdot\nabla\langle|\boldsymbol Z^\pm|^2\rangle+\Big(\tfrac12\nabla\cdot\boldsymbol U\pm\nabla\cdot\boldsymbol V_A\Big)\langle|\boldsymbol Z^\pm|^2\rangle+\Big(2a_s-\tfrac12\Big)E_D\nabla\cdot\boldsymbol U\pm(2b_s-1)E_D\nabla\cdot\boldsymbol V_A\mp\frac{b_s}{\rho_{\mathrm{sw}}}\langle|\boldsymbol Z^\pm|^2\rangle\boldsymbol V_A\cdot\nabla\rho_{\mathrm{sw}}=-2\alpha_{\mathrm{KT}}\frac{\langle|\boldsymbol Z^\pm|^2\rangle\langle|\boldsymbol Z^\mp|^2\rangle^{1/2}}{\ell^\pm}+2S^\pm .$$

# Printed slips

- $\eta_1$: §4 "we use η1 = 1.8 × 10−4 and η2 = 1.5 × 10−10"; Table 2 "η1 1.8 × 10−5".
- Table 2 prints the row "β 0.015" for $\beta_{\mathrm{KT}}=\alpha_{\mathrm{KT}}/2$, with the symbol of the plasma beta.
- §6: "the theoretical σD decreases gradually until ∼15 au, and then increases"; §8: "The theoretical normalized residual energy decreases until ∼20 au, and then increases".
- Pickup-ion temperature agreement: §7 "between ∼11 and 52 au"; §8 "between ∼10–52 au".
- Density ratio: §8 "decreases with increasing distance until 50 au, and then increases slightly"; §6 "The theoretical ratio increases slightly beyond ∼60 au".
- §3: "fD is reduced from the dispersive bispherical value of 0.642–0.06".
- $\lambda_b$ is used in §6 and Fig. 4 without a defining formula; $\sigma_c$ and $\sigma_D$ are not defined by formula.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\boldsymbol z^\pm=\boldsymbol u\pm\boldsymbol B/\sqrt{\mu_0\rho}$ | $\boldsymbol Z^\pm$ | SI form; $+$ outward |
| $\langle z^{\pm2}\rangle$ | $\langle|\boldsymbol Z^\pm|^2\rangle$ | no factor $\tfrac12$ |
| $E_D=\langle\boldsymbol z^+\cdot\boldsymbol z^-\rangle$ | $E_D$ (residual energy, registry §11) | |
| $\sigma_c$, $\sigma_D$ | $\sigma_c$, $\sigma_r$ | normalized cross-helicity and residual energy |
| $\lambda^\pm$, $\lambda_D$, $\lambda_u$, $\lambda_b$ | $\ell^\pm$ (registry §11), $\ell_D$, $\ell_u$, $\ell_b$ (page-local): correlation lengths | **collision** with the perpendicular scale $\lambda$ |
| $\beta$ | $\beta_p$ | plasma beta |
| $\beta^0=\alpha/2$ | $\beta_{\mathrm{KT}}$ (registry §11, as on [compressible MHD turbulence](/results/compressible-mhd-turbulence.md)) | **collision** with $\beta_p$ in Table 2 |
| $\alpha$, $\alpha_2$ | $\alpha_{\mathrm{KT}}$ (registry §11), $\alpha_2$ (page-local): von Kármán–Taylor constants, as on [compressible MHD turbulence](/results/compressible-mhd-turbulence.md)) | **collision** with the DG blending factor $\alpha$ |
| $\epsilon\equiv M_{s0}$ | $M_t$ | expansion parameter |
| $\chi=L/R$ | (scale ratio, page-local) | **collision** with the SA $\chi$ |
| $\boldsymbol U$ ($\boldsymbol U_{sw}$), $\boldsymbol V_A$, $\rho$ ($\rho_{sw}$), $\boldsymbol B_{sw}$ | $\boldsymbol U$, $\boldsymbol V_A$, $\rho_{\mathrm{sw}}$, $\boldsymbol B_{\mathrm{sw}}$ (background wind velocity, Alfvén velocity, density, field; page-local) | $\boldsymbol B_{sw}$ plays the role of $\boldsymbol B_0$ |
| $^\infty$, $^*$ | (leading and higher order of the NI expansion) | |
| $a$, $b$ | $a_s$, $b_s$ (structural similarity parameters, registry §11) | **collision:** $b$ is not the field fluctuation $\boldsymbol b$ |
| $S^\pm$, $S_{E_D}$, $c^\pm$, $c_{E_D}$, $f_D$, $\eta_1$, $\eta_2$ | (sources and their strengths, page-local) | **collision:** $\eta_1$, $\eta_2$ are not the Kolmogorov length |
| $S_t$, $f_p$ | (turbulent heating rate, proton heating fraction, page-local) | |
| $\gamma_s$, $\gamma_e$, $\gamma_p$ | $\gamma$ | 5/3 for each species |

# Reference list

87 printed references, author–year style (AAS), with titles not printed
except for the two books. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Same-author
same-year works follow the printed a/b/c order (Adhikari 2017–2022,
Matthaeus 1999, Telloni 2022, Zank 1992, 2012, 2018, Zhou 1990); Zank
(2014, the book) and Zank et al. (2014, ApJ 797:87) are distinct entries.
Wang et al. (2022, ApJ 928:176) is a work distinct from the existing `wang-2022` entry (venue check) and is keyed `wang-2022-k`. Axford (1972) is read as NASA SP-308, p. 609. No key
collides with a planned Source slug.

# Pages created or updated

Chunk 8 (2026-10-27). This source is cited on:

- [Reduced MHD and Elsasser variables](/definitions/reduced-mhd.md)
- [Critical balance and the anisotropic MHD cascade](/properties/critical-balance.md)
- [Compressible MHD turbulence](/results/compressible-mhd-turbulence.md)
