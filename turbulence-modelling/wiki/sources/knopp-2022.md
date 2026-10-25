---
type: Source
title: "Knopp (2022) — An Empirical Wall Law for the Mean Velocity in an Adverse Pressure Gradient for RANS Turbulence Modelling"
description: "Builds an empirical inner-layer wall law for adverse-pressure-gradient turbulent boundary layers from high-Reynolds-number experiments: a log law whose upper edge shrinks with the inner-scaled pressure-gradient parameter, topped by a half-power law, with power-law correlations in Re_τ and the pressure-gradient parameter for the region edges and slope."
resource: "doi:10.1007/s10494-022-00367-1"
source_kind: paper
authors: [Knopp T.]
year: 2022
venue: "Flow Turbul. Combust. 109:571-601"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Flow_Turbulence_and_Combustion_Knopp_An_Empirical_Wall_Law_for_the_Mean_Velocity_in_an_Adverse_Pr.pdf"
tags: [rans, wall-model, boundary-layer, separated-flow]
timestamp: 2026-10-25T19:43:00Z
---

# Summary

Knopp (2022) builds an empirical
[wall law in adverse pressure gradient](/definitions/adverse-pressure-gradient-wall-law.md)
for the mean streamwise velocity in the inner layer of two-dimensional,
incompressible, smooth-wall
[turbulent boundary layers](/benchmarks/turbulent-boundary-layer.md). The
stated aim is better RANS models and wall functions. The data are
wind-tunnel mean-velocity profiles at $Re_\theta>8000$: the 1968
AFOSR-IFP-Stanford collection, Samuel & Joubert (1974), Skare & Krogstad
(1994), Marusic & Perry (1995), the UNH experiment and two DLR/UniBw
experiments. A low-Reynolds-number experiment and the
[DNS](/definitions/direct-numerical-simulation.md) of Coleman et al. (2018)
serve only for validation. The governing parameter is the inner-scaled
pressure gradient $\Delta p_s^+=\nu\,(dP/ds)/(\rho u_\tau^3)$ (page-local).

The assumed structure has a [log law](/definitions/law-of-the-wall.md)
($\kappa=0.41$) up to $y^+_{\log,\max}$, an intermediate region, and above it
an "extended" or half-power law with slope coefficient $K$ up to the edge of
the inner layer, fitted up to $y=0.21\delta$. The log law is robust in an
adverse pressure gradient, but its extent relative to $\delta$ shrinks as
$\Delta p_s^+$ grows. A similarity argument with the reduced Hartree
parameter and a scaling argument with Nickels' velocity scale motivate power
laws in $Re_\tau$ and $\Delta p_s^+$. The data fits are
$y^+_{\log,\max}=1.78Re_\tau^{1/2}(\Delta p_s^+)^{-1/5}$, with the constant
revised to 1.68 after the low-Reynolds-number check, and
$y^+_{\mathrm{sqrt},\min}=4.05Re_\tau^{1/2}(\Delta p_s^+)^{-0.13}$, with
$K=0.45\pm0.15$. No systematic effect of higher-order local parameters is
found. History effects appear only in the DLR/UniBw flows. The paper supports
the conjecture of a local wall law governed at leading order by
$\Delta p_s^+$ and $Re_\tau$. The use in RANS, an augmentation term in the
$\omega$ equation of $k$-$\omega$-type models switched on by these
correlations, is described in words only, with reference to Knopp (2016).

# Version read

Version of record (Springer, open access CC BY 4.0; received 23 March 2022,
accepted 24 August 2022, published online 13 September 2022), 31 pages
(pp. 571–601), all read. The equations were checked on the rendered pages.
The two appendices are printed without letters; the text calls them
appendix A (uncertainty estimation) and appendix B (sensitivity of the
$y^+_{\log,\max}$ method). Page 1 matches the metadata, and there is no
identity problem.

# Key claims

1. In an adverse pressure gradient the log law in the mean velocity is a robust feature of every flow in the database (§5.1, Figs. 4, 7, 8). **Shown**
2. The log-law region is thinner than in a zero-pressure-gradient layer at the same $Re_\tau$ and does not reach $y=0.15\delta$. Its extent relative to $\delta$ decreases as $\Delta p_s^+$ increases (§1, §5.2, Fig. 9). **Shown**
3. $y_{\log,\max}/\delta$ is below 0.11 for $\Delta p_s^+>0.005$ and $\beta_{RC}>4.5$, and below 0.08 for $\Delta p_s^+>0.015$ and $\beta_{RC}>12$ (§5.2). **Shown**
4. The log-law region reaches $y/\delta=0.15$ only for the mild-pressure-gradient equilibrium flows of Bradshaw and Clauser. For flows entering an adverse gradient from near zero gradient, the reduction is already present at the first adverse-gradient station (§5.2). **Shown**
5. Above the log law the mean velocity turns upward and is fitted by the extended (half-power) law, Eq. (14). The upward turn grows with $\Delta p_s^+$ (§5.1). **Shown**
6. Similarity argument: take the reduced Hartree parameter $-\beta_{H,\mathrm{red}}=\Delta p_s^+Re_\tau^2$ (Eq. 27) as governing, and choose the $Re_\tau$ exponent that minimizes spreading in the data (1/2, Fig. 9 right). This gives $y^+_{\log,\max}=CRe_\tau^{2q+1}(\Delta p_s^+)^q$ with $q=-1/4$ (Eqs. 28–30). **Derived** (heuristic; exponent chosen from data)
7. Scaling argument with Nickels' velocity scale $u_T$: the explicit dependence of the correlation on $u_\tau/u_T$ disappears if $q''=2q'/3$, and $q'=-1/4$ gives $q''=-1/6$ (Eqs. 31–34). **Derived**
8. Final calibration (data fit): $y^+_{\log,\max}=1.78Re_\tau^{1/2}(\Delta p_s^+)^{-1/5}$ (Eq. 35). It changes the correlation of Knopp (2016) after a revised analysis of the database and of Reynolds-number effects. **Shown**
9. The inner edge of the half-power region is $y^+_{\mathrm{sqrt},\min}=4.05Re_\tau^{1/2}(\Delta p_s^+)^{-0.13}$ (Eq. 36). More data are needed for $\Delta p_s^+<0.002$ and $\Delta p_s^+>0.03$ at high Reynolds number (§6.3, Fig. 10 left). **Shown**
10. The half-power slope scatters around $K=0.45\pm0.15$, with the effective pressure gradient set equal to $\Delta p_s^+$ for all flows. A constant $K$ is advocated (§6.4, Fig. 10 right). **Shown**
11. Literature values of $K$ are cited for comparison: $0.48\pm0.03$ (Townsend 1961), 0.48 (Perry 1966), 0.41–0.51 (Szablewski 1960), and for large $\Delta p_s^+\delta^+$ 0.447 (Kader & Yaglom 1978) and 0.57 (Afzal 2008). $K$ depends on the form of the law (Eq. 14 or 15) and on the fit region (§6.4). **Stated**
12. Uncertainties of ±10% in $\delta$, 6% in $u_\tau$ and 1% in $\nu$ enter the error bars of $y^+_{\log,\max}$. Correlation (35) lies within or close to the bars except for the data sets Br1, BrF, Cl1, DM2 and DM3 (§6.5). **Shown**
13. A 25% relative uncertainty in $\Delta p_s^+$ (5% in $dP/ds$, 6% in $u_\tau$, 1% in $\rho$ and $\nu$) gives up to 11% uncertainty in $K$ by a Monte Carlo approach. The total uncertainty of $K$ is 18.0–33.0% per data set (§6.5, App. A, Table 2). **Shown**
14. No systematic trend of $y_{\log,\max}$, $y_{\mathrm{sqrt},\min}$ or $K$ with the higher-order local parameters (the wall-shear-stress-gradient parameter and the second-derivative pressure parameter) can be found. Equilibrium and streamwise-evolving flows cannot be clearly told apart, beyond slightly larger $y^+_{\log,\max}/(\delta^+)^{1/2}$ for mild equilibrium flows. The data do not support a more refined model than Eqs. (35)–(36) (§7.2, Fig. 11). **Shown**
15. The low values of $y^+_{\log,\max}/(\delta^+)^{1/2}$ and $K$ in the DLR/UniBw flows are attributed to history effects from an upstream region of convex curvature and from a favourable-to-adverse pressure-gradient change. Measurement accuracy explains only part of the difference (§7.2, §7.3, Table 3). **Shown** (attribution **Stated**)
16. Low-Reynolds-number data (Nagano et al. 1991, $481\le Re_\tau\le639$; the DNS of Coleman et al. 2018 with $Re_\tau$ up to 880) agree with the high-Reynolds-number correlation. The constant in Eq. (35) is suggested to change from 1.78 to 1.68 (§7.3, Fig. 12). **Shown**
17. An eddy-turnover estimate (Eq. 37), with relaxation within two turnover times after Sillero et al. (2013), gives a relaxation length of about $\delta$ at $y/\delta=0.1$ and about $2\delta$ at $y/\delta=0.2$ for $\Delta p_s^+\gtrsim0.004$. The inner layer thus relaxes fast but not instantaneously, and history effects matter more in the half-power region than in the log region (§7.1). **Derived**
18. Conjecture: a local wall law exists in the inner layer, governed at leading order by $\Delta p_s^+$ and $Re_\tau$ and perturbed by higher-order local and history effects. Couette–Poiseuille flow (Telbany & Reynolds 1980), a self-similar flow in dynamic equilibrium, supports it (§7.1, §8). **Stated** (conjecture supported by data)
19. At $\Delta p_s^+=0.05$, Eq. (35) gives $y^+_{\log,\max}=3.24(\delta^+)^{1/2}$: a log law up to $y^+=92$ at $Re_\tau=800$ and about 162 at $Re_\tau=2500$. The outer edge then falls below the commonly assumed zero-pressure-gradient start of the log region, which agrees with the log-law breakdown at $\Delta p_s^+>0.05$ of Alving & Fernholz (§7.4). **Derived**
20. Strict self-similarity of the inner-layer mean velocity cannot be expected at equal Rotta–Clauser parameter $\beta_{RC}$ alone, in agreement with Bobke et al. (2017) and Vila et al. (2017) (§8). **Derived** (from the $Re_\tau$ dependence of Eq. 35)
21. Experimentalists can use the correlation as a first guess of the data range for the Clauser-chart method (§8). **Stated**
22. For DLR/UniBw II at 36 m/s, $y^+_{\log,\max}$ ranges over 160–248 across choices of the log-fit interval. These changes are much smaller than those of the fitted $\kappa$ (0.312–0.379) and $B$ (1.06–3.69). A Clauser-chart $u_\tau$ lowers $y^+_{\log,\max}$ by about 6% (App. B, Table 3). **Shown**
23. Neglecting the Reynolds-normal-stress term far from incipient separation is supported by the DLR/UniBw experiment II, citing Knopp (2019) (§2.2). **Stated**
24. Nickels' modified velocity scale stays finite at separation: $u_T\to Re_c^{1/3}u_p$, and the pressure parameter in modified scaling tends to $1/Re_c=1/12$ (Eqs. 20, 33). **Derived** (background, Nickels 2004)
25. RANS use (preliminary, Knopp 2016): an augmentation term in the $\omega$ equation is designed to reproduce the half-power solution. A blending function based on the correlations in $y^+$, $Re_\tau$, $\Delta p_s^+$ and $y/\delta$ activates it only in the half-power region (§1). **Stated** (no equations in this paper)

# Printed slips

- **Fig. 7 caption against §5.1.** For the Marusic & Perry profile at $Re_\tau=3406$, the caption prints $\Delta p_s^+=7.17\times10^{-3}$ and the text $7.55\times10^{-3}$. For Perry (ID 2907, $Re_\tau=7926$), the caption prints $7.89\times10^{-3}$ and the text $7.85\times10^{-3}$.
- **Eq. (9).** The parameters carry the subscript $x$ ($\Delta p_x^+$, $\Delta u^+_{\tau,x}$), where the rest of the paper uses $s$.
- **§7.4 against §7.3.** §7.4 evaluates Eq. (35) with the constant 1.78 ("$3.24(\delta^+)^{1/2}$", $y^+=92$ and 162), although §7.3 has just suggested 1.68. With 1.68 the factor is 3.06, giving $y^+\approx87$ at $Re_\tau=800$ and $\approx153$ at $Re_\tau=2500$. *(Compiler check, not in the sources.)*
- **Outer edge of the half-power region.** §4.2 first "assumed to extend up to $y=0.2\delta$", then "set to the constant value $y=0.21\delta$". §8 says the law "describes the inner 20% of the boundary layer".
- **Name spelling.** "Spangenberg" in the running text and the Table 1 acronyms, "Sprangenberg" in the reference list and the Table 1 reference column.
- **Fig. 12 caption.** "(left)" appears twice.
- **Overloaded symbols.** In §6.1.1 $s$ is both the streamwise coordinate and the $Re_\tau$ exponent. The $\lambda$ of Telbany & Reynolds in §1 and the $\lambda$ of Eq. (10) are different quantities.
- **Reference list.** Maciel et al. (2018) prints the author list "Maciel, Y., Wei, T., Simens, A.G.G.M.P.". Perry (1966) prints "presssure" in its title. Several page fields ("17–132", "30–136", "3–1311", "051205–115", "105102–1") look like mangled article numbers.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U$, $V$ | $\langle u\rangle$, $\langle v\rangle$ | Reynolds-averaged velocities in wall-fitted coordinates |
| $s$ | $s$ (page-local; wall-tangential, along the mean velocity as $y\to0$, the $x$ of a flat plate) | also the $Re_\tau$ exponent in §6.1.1 |
| $\overline{u'v'}$, $\overline{u'^2}$, $\overline{v'^2}$ | $R_{12}$, $R_{11}$, $R_{22}$ | **collision:** the overbar is a Reynolds average, not the LES filter |
| $\tau$, $\tau^+=\tau/\tau_w$ | (total shear stress $\rho(\nu\,\partial_y\langle u\rangle-R_{12})$, inner-scaled) | **collision:** not the SGS stress $\tau_{ij}$ |
| $P$, $P_w$ | $\langle p\rangle$, its wall value | |
| $\Delta p_s^+=\frac{\nu}{\rho u_\tau^3}\frac{dP}{ds}$ | $\Delta p_s^+$ (page-local) | pressure-gradient parameter in inner scaling, Eq. (2) |
| $\Delta u^+_{\tau,s}$, $\Delta^2p_s^+$ | (wall-shear-stress-gradient parameter, second-derivative pressure parameter) | higher-order local parameters |
| $\alpha^+=\lambda\Delta p_s^+$ | $\alpha^+=\lambda_M\Delta p_s^+$ (page-local, as on the APG wall-law page) | effective pressure gradient, McDonald's $\lambda<1$; $\alpha^+=\Delta p_s^+$ in all fits |
| $\kappa$, $B$ | $\kappa=0.41$, $B=5.0$ | values of Coles & Hirst except where fitted |
| $K$, $B_o$ | (half-power slope coefficient and intercept) | $B_o$ not printed |
| $y^+_{log,max}$, $y^+_{sqrt,min}$, $y_{sqrt,max}$ | $y^+_{\log,\max}$, $y^+_{\mathrm{sqrt},\min}$, $0.21\delta$ | edges of the log and half-power regions |
| $\delta$, $\delta^*$, $\theta$, $\delta_{99.5}$ | $\delta$, $\delta^*$, $\theta$, (99.5% thickness) | $\delta$ from the composite wall–wake fit |
| $Re_\tau\equiv\delta^+$ | $Re_\tau$ | |
| $\beta_{RC}=\frac{\delta^*}{\rho u_\tau^2}\frac{dP_w}{ds}$ | (Rotta–Clauser parameter) | |
| $\beta_H$, $\beta_{H,red}$ | (Hartree and reduced Hartree parameters) | |
| $\Pi$ | (Coles wake factor) | **collision:** not the SGS energy flux $\Pi$ |
| $\eta=y/\delta$ | $y/\delta$ | **collision:** not the Kolmogorov length |
| $u_T$, $u_p$, $Re_c=12$, $y_c^+$ | (Nickels' velocity scale, Stratford pressure velocity, critical Reynolds number, sublayer thickness) | |
| $u^*=\tau^{1/2}$ | (total-stress velocity, per unit density) | **collision:** not the semi-local scaling $(\cdot)^*$ |
| $\delta_\nu$, $\delta_p=\rho u_\tau^2/(dP/ds)$ | $\delta_\nu$, (pressure length scale) | |
| $\log$ | $\ln$ | natural logarithm |

# Reference list

53 printed references in author–year style (alphabetical, Springer). The list
is merged complete into the [bibliography](/bibliography.md) with `citedby`
this slug. Perry (1966) and Perry, Bell & Joubert (1966) are disambiguated in
printed order. Knopp (2016) is an AIAA paper and Knopp (2019) a DLR report
with a URL. The anomalies are recorded as printed with notes: the garbled
author list of Maciel et al. (2018), the mangled page or article numbers,
"presssure" and "Sprangenberg". There are no printed duplicates and no
unparseable items.

# Pages created or updated

Chunk 2 (2026-10-25). This source is cited on:

- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [Wall law in adverse pressure gradient](/definitions/adverse-pressure-gradient-wall-law.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Equilibrium wall model](/methods/equilibrium-wall-model.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
