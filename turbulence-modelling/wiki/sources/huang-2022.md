---
type: Source
title: "Huang et al. (2022) — Direct numerical simulation of hypersonic turbulent boundary layers: effect of spatial evolution and Reynolds number"
description: "DNS of spatially developing zero-pressure-gradient boundary layers at Mach 2.5, 4.9 and 10.9 up to Re_tau≈1200 over domains longer than 300 inflow thicknesses, quantifying inflow recovery length, skin-friction and heat-transfer correlations, velocity transformations, Reynolds analogies and the effect of strong wall cooling on turbulent structure."
resource: "doi:10.1017/jfm.2022.80"
source_kind: paper
authors: [Huang J., Duan L., Choudhari M.M.]
year: 2022
venue: "J. Fluid Mech. 937:A3"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Journal_of_Fluid_Mechanics_Huang_Direct_numerical_simulation_of_hypersonic_turbulent_boundary.pdf"
tags: [dns, compressible, hypersonic, boundary-layer]
timestamp: 2026-10-25T19:47:00Z
---

# Summary

Huang et al. (2022) report [DNS](/definitions/direct-numerical-simulation.md)
of spatially developing, flat-plate, zero-pressure-gradient
[turbulent boundary layers](/benchmarks/turbulent-boundary-layer.md) over
domains longer than $300\delta_i$ ($\delta_i$ the inflow thickness) at three
new conditions: Mach 2.5 adiabatic, Mach 4.9 quasi-adiabatic
($T_w/T_r=0.91$, a Texas A&M wind-tunnel condition) and Mach 10.9 with a
strongly cooled wall ($T_w/T_r=0.20$, CUBRC Run 7). They reach
$Re_\tau\approx1200$, against at most 686 in the authors' earlier database
(Zhang et al. 2018), whose five cases are reused. The scheme is a
limiter-optimized seventh-order WENO (an eighth-order split-convective
central scheme for the Mach 2.5 case, chosen to reduce
[numerical dissipation](/properties/numerical-dissipation.md) and cost), with
each case run in three overlapping streamwise boxes.

The inflow recovery length, measured by when the von Kármán integral
equation holds to 5%, grows from $20\delta_i$ at Mach 2.5 to $80\delta_i$ at
Mach 14; a digital-filter inflow needs 15–$20\delta_i$ more than
recycling–rescaling. Van Driest II with the Smits et al. power law gives the
best skin-friction prediction, while neither van Driest II nor Spalding–Chi
works for $T_w/T_r\lesssim0.3$. The paper recalls that standard
[Spalart–Allmaras](/methods/spalart-allmaras-model.md) and SST models predict
hypersonic heat flux worse than algebraic models with compressibility
corrections, and finds its Mach 10.9 wall stress and heat flux within 2% of
Baldwin–Lomax RANS.

Among [compressible velocity transformations](/definitions/compressible-velocity-transformation.md),
the data-driven transformation of Volpiani et al. and the total-stress-based
transformation of Griffin et al. collapse the log layer, the latter best;
Trettel–Larsson, which collapses cold-wall
[channels](/benchmarks/turbulent-channel-flow.md), leaves an intercept
scatter. At Mach 10.9 no clear log region of the
[law of the wall](/definitions/law-of-the-wall.md) and no
[attached-eddy](/definitions/attached-eddy-hypothesis.md) logarithmic decay
of the normal stresses appear up to $Re_\tau=1172$. The strong Reynolds
analogy of [Morkovin](/definitions/morkovin-hypothesis.md) fails under
cooling, while Huang et al.'s (1995) modified form collapses all cases.
Semi-local scaling collapses near-wall streak sizes; superstructures exist at
all Mach numbers; strong cooling reduces scale separation and weakens the
inner–outer interaction.

# Version read

Version of record (J. Fluid Mech. 937:A3, open access CC BY 4.0; received 24
March 2021, accepted 20 January 2022), 49 pages (A3-1 to A3-49), all read.
Page-1 title, authors and DOI match the metadata above. No identity problem.
Numbering on this page is that of this version.

# Key claims

The paper's $z$ is wall-normal and $y$ spanwise; the claims are written with
the registry's $y$ wall-normal and $z$ spanwise (see the notation map).

1. Three new spatially developing DNS reach $Re_\tau=1199$ (M2p5HighRe, $L_x=313.6\delta_i$), 1244 (M5Tw091, $183.6\delta_i$) and 1193 (M11Tw020, $315.8\delta_i$); the reused Zhang et al. (2018) cases reach at most $Re_\tau=686$ (§2.1, Tables 1–2). **Shown**
2. The inflow induction length (from the inflow plane to where $C_f=2\,d\theta/dx$ first holds to 5%) normalized by $\delta_i$ grows with Mach number, from 20 at Mach 2.5 to 80 at Mach 14 (recycling–rescaling) (§3.1, Table 3). **Shown**
3. Normalized by the eddy-turnover length $L_{to}=U_\infty\delta_i/u_{\tau,i}$ it lies in $1\lesssim\Delta x_{ind}/L_{to}\lesssim3$ and still grows with Mach number; the effective turnover length of Sillero et al. (2013) collapses the cases better, $1\lesssim\tilde x\lesssim2$ (§3.1, Eq. 3.1, Table 3). **Shown**
4. Digital-filter inflow needs a longer induction length than recycling–rescaling, by about $20\delta_i$ (M2p5HighRe: 40 against 20) and $15\delta_i$ (M11Tw020: 85 against 70). At the end of the digital-filter induction length the two inflows differ in the wake by 6.2% in $u^+_{VD}$ and 1.8% in $\langle\rho u''u''\rangle/\tau_w$; at $Re_\tau=774$ by 1.5% and 1.0%; near-wall agreement is "almost perfect" already (§3.1, Fig. 2). **Shown**
5. A significantly longer distance is needed for the outer-layer discrepancy between the inflows to disappear than for near-wall quantities (§6(i), Fig. 2). **Shown**
6. For strongly cooled hypersonic walls ($T_w/T_r\lesssim0.3$: M11Tw020, M14Tw018) neither van Driest II nor Spalding–Chi predicts $C_f$ well: van Driest II overpredicts by up to 10–20%, Spalding–Chi underpredicts by 20–40%; van Driest II remains good for $0.3\lesssim T_w/T_r<1.0$ (§3.2, Fig. 3). **Shown**
7. The Spalding–Chi discrepancy for M11Tw020 decreases as the Reynolds number increases, consistent with Goyne et al. (2003) (§3.2, Fig. 3b). **Shown**
8. Van Driest II combined with the Smits et al. (1983) power law $C_{f,i}=0.024Re_{\theta i}^{-1/4}$ correlates best: within ±5% for the supersonic adiabatic case and within −15% to −6% for the hypersonic cold-wall cases (§3.2, Fig. 3c; §6(ii)). **Shown**
9. The Reynolds analogy factor $2C_h/C_f$ is nearly constant over the DNS range for all hypersonic cold-wall cases, between 1.1 and 1.2, which the authors call "consistent with the usual approximation $R_{af}=Pr^{-2/3}\approx1.256$" although the range lies below it; for M11Tw020 it is about 1.19 at $Re_\tau\lesssim400$ and 1.16 at $Re_\tau\approx1172$, and the DNS values vary far less than the experiments of Goyne et al. (2003) and Holden (1972) (§3.2, Fig. 4). **Shown**
10. The shape factor $\delta^*/\theta$ is insensitive to the Reynolds number, grows strongly with Mach number and decreases with wall cooling; the correlation of Hopkins et al. (1972), Eq. 3.8a, fits best, with relative error about 2% (supersonic adiabatic) and up to 8% (hypersonic cold wall) (§3.2, Fig. 5). **Shown**
11. The near-wall peak of $(\langle\rho u''u''\rangle/\tau_w)^{1/2}$ grows weakly with the Reynolds number at Mach 2.5, following logarithmic fits (Eq. 3.9), but is nearly constant for the hypersonic cold-wall cases; it rises weakly with Mach number, at $Re_\tau=1138$ from 2.9 (M2p5HighRe) to 3.5 (M11Tw020); semi-local scaling accounts for the wall-temperature effect (§3.2, Fig. 6). **Shown**
12. The peak Reynolds shear stress $-\langle\rho u''v''\rangle/\tau_w$ grows weakly with the Reynolds number and follows Yao & Hussain's (2020) $1-8.5Re_\tau^{*-2/3}$ for $Re_\tau^*\lesssim2000$ and $1-3.0Re_\tau^{*-1/2}$ above; the conclusions state that it is insensitive to flow parameters, 0.85–0.9 (§3.2, Eqs. 3.10–3.11, Fig. 7; §6(ii)). **Shown**
13. The wall-pressure rms over the mean wall pressure decreases with the Reynolds number and increases with Mach number and wall-temperature ratio, from about 4% at Mach 2.5 to 25% at Mach 11. Over $\tau_w$ it is 2.6–2.8 for (nearly) adiabatic cases (Eq. 3.12) and almost constant for cold walls: about 3.6 (M6Tw025, M8Tw048) and 4.5 (Mach 11 and 14). In mixed scaling it is 0.12–0.17, above the incompressible 0.112 (§3.2, Fig. 8). **Shown**
14. The wall-shear-stress rms over the mean is about 0.4 at Mach 2.5 at low $Re_\tau$ and follows the incompressible fit $0.298+0.018\log Re_\tau$ (Schlatter & Örlü 2010) for (nearly) adiabatic cases; for hypersonic cold walls it is 0.45–0.5, and the wall-heat-flux rms over the mean is 0.5–0.7, decreasing slightly with $Re_\tau$ (§3.2, Fig. 9, Eq. 3.13). **Shown**
15. Trettel–Larsson collapses the viscous sublayer and buffer layer of all cases but leaves a scatter of the log-law intercept between conditions (also at matched $Re_\tau^*$), whereas it collapses isothermal cold-wall channels almost perfectly (Trettel & Larsson 2016; Yao & Hussain 2020); the authors suggest a stronger influence of cooling on the balance of turbulent and viscous stress in external boundary layers (§4.1, Fig. 10b). **Shown** (interpretation **Stated**)
16. The data-driven transformation of Volpiani et al. (2020) and the total-stress-based transformation of Griffin et al. (2021) collapse the profiles in the viscous sublayer and the log layer up to $Re_\tau=1172$; the total-stress-based one gives the best collapse across the inner layer (§4.1, Figs. 10c,d, 11). **Shown**
17. The van Driest log-law diagnostic $I_{VD}=y^+\,du^+_{VD}/dy^+$ is nearly constant for $y^+\approx40$–100 for M2p5HighRe and M5Tw091 at $Re_\tau=1172$, but M11Tw020 shows no wide constant region up to $Re_\tau=1172$ ($Re_\tau^*=6213$); the authors attribute the missing log region to the reduced scale separation of strong wall cooling (§4.1, Eq. 4.5, Fig. 11). **Shown**
18. The mean velocity follows a power law $\langle u\rangle/U_\infty=(y/\delta_\infty)^{1/n}$ (Eq. 4.6) over $0.2\lesssim y/\delta\lesssim0.6$ with $n$ between 5 and 8; the van Driest velocity follows it over $0.2\lesssim y/\delta\lesssim0.9$ with $n=5$ for all conditions; it fails for $y/\delta\lesssim0.2$ (§4.1, Eqs. 4.6–4.7, Fig. 12). **Shown**
19. Morkovin's scaling collapses the Reynolds stresses of the two nearly adiabatic cases, except for a rise of the streamwise peak from Mach 2.5 to 4.9; M11Tw020 has a much larger streamwise peak and reduced spanwise and wall-normal peaks; semi-local $y^*$ collapses the peak locations at all Mach numbers (§4.2, Figs. 13–14). **Shown**
20. At $Re_\tau=1172$ the quasi-adiabatic cases show the attached-eddy logarithmic decay $\langle\rho u_i''u_i''\rangle/\tau_w=B_i-A_i\log(y/\delta)$ (no sum) with $B_1=2.39$, $A_1=1.03$ (as Pirozzoli & Bernardini 2011), $A_3=0.27$ and $B_3$ from 1.5 to 1.3 for the spanwise component; M11Tw020 shows no such region at $Re_\tau\le1172$ (§4.2, Eq. 4.8, Fig. 13). **Shown**
21. Among temperature–velocity relations $\langle T\rangle=T_w-a_1\langle u\rangle-a_2\langle u\rangle^2$, all agree for M2p5HighRe, but for M11Tw020 only Duan & Martín (2011) and Zhang et al. (2014) fit the DNS; Duan & Martín is significantly simpler (§4.3.1, Table 5, Fig. 15). **Shown**
22. Velocity and temperature fluctuations are nowhere perfectly anticorrelated (the strong Reynolds analogy, Eq. 4.10, fails); their correlation coefficient is positive very near the wall and about $-0.55$ for $y/\delta\gtrsim0.2$, independent of Reynolds number, Mach number and wall cooling (§4.3.2, Fig. 17a). **Shown**
23. Away from the wall $Pr_t$ is of order one and insensitive to flow parameters; the linear fit $Pr_t=1-\tfrac14(y/\delta)$ (Subbareddy & Candler 2011) fits the outer region; $Pr_t$ overshoots near the wall where the wall-normal turbulent heat flux changes sign (§4.3.2, Fig. 17b). **Shown**
24. The original strong Reynolds analogy (Eq. 4.12) does not collapse the data; the modified form of Huang, Coleman & Bradshaw (1995) (Eq. 4.13) collapses all cases to a value close to unity in the outer layer, which gives an estimate of the temperature rms from the velocity rms with $Pr_t\approx1$ (§4.3.2, Fig. 18). **Shown**
25. The skewness and flatness of $u''$ at Mach 2.5 and 4.9 resemble incompressible channel data (Gaussian for $30\lesssim y^*\lesssim1000$), which supports essentially incompressible dynamics up to Mach 4.9 without intense cooling; M11Tw020 has lower values in the viscous sublayer and stronger non-Gaussianity in the log layer; all cases agree at $y^*\approx15$ (§4.4, Fig. 19). **Shown**
26. Near-wall streaks at $y^*\approx15$ more than double their length and spacing in wall units in the cold-wall case ($\lambda_z^+\approx200$ against about 100); in semi-local units all three Mach numbers give $\lambda_x^*\approx1000$ and $\lambda_z^*\approx120$ (§5, Figs. 20–21). **Shown**
27. Superstructures (alternating low- and high-speed regions at least $10\delta$ long) exist at $y^*\approx200$ at all three Mach numbers, with $\lambda_x/\delta=2$–10 and $\lambda_z/\delta\approx1$, shown "for the first time" in the hypersonic regime without Taylor's hypothesis (§1, §5, Figs. 23–24). **Shown**
28. The quasi-adiabatic cases show an outer spectral peak at $y/\delta\approx0.22$, $\lambda_z/\delta\approx0.8$, and a $k_z^{-1}$ plateau; M11Tw020 shows neither up to $Re_\tau=1172$, and its inner peak sits higher in outer units ($\lambda_z/\delta\approx0.28$ against 0.14 at $Re_\tau=774$) (§5, Figs. 21–22). **Shown**
29. At $Re_\tau=1172$ the spanwise spectrum of the wall shear stress has an outer peak at $\lambda_z/\delta\approx1$ (the footprint of outer large-scale motions) in the quasi-adiabatic cases but not for M11Tw020, which the authors read as a weakened inner–outer interaction; at $y/\delta\approx0.5$ all spectra collapse with peaks at $\lambda_x/\delta\approx3$, $\lambda_z/\delta\approx1$ (§5, Figs. 25–26). **Shown**
30. Validation: spanwise refinement ($\Delta z^+$ from 6.6 to 5.0) changes wall heat flux, $u^+_{VD}$ and Reynolds stresses by about 1%; spectra roll off by several decades; M5Tw091 agrees with the PIV of Tichenor et al. (2013); M11Tw020 wall stress and heat flux agree with Baldwin–Lomax RANS (Gnoffo et al. 2013) within 1.9% and 1.7% at $x=1.35$ m, while the CUBRC data scatter (sensor uncertainty about 12%) (App. A, Figs. 28–32). **Shown**
31. Standard one- and two-equation RANS models (SA, SST) predict hypersonic zero-pressure-gradient heat flux less accurately than algebraic models with compressibility corrections (Rumsey 2010; Gnoffo et al. 2013); the agreement with Baldwin–Lomax is consistent with this (§1, App. A.2). **Stated** (from cited work), partly **Shown**

# Printed slips

- **Case names.** "M2p5pHighRe" (§2.2, A3-5 and A3-7) for M2p5HighRe; "M11Tw20" (§4.2, three times, A3-27) for M11Tw020; "M51w091" in the Fig. 3(c) legend for M5Tw091.
- **"M5Tw020" (§4.2, A3-27).** "the intercept constant $B_2$ varies from 1.5 (M2p5HighRe) to 1.3 (M5Tw020)"; no case M5Tw020 exists, and the sentence concerns "the quasiadiabatic cases at Mach 2.5 and 4.9".
- **$Re_\tau=744$.** The Fig. 10 and Fig. 11 legends print "M2p5HighRe ($Re_\tau$ = 744)"; Table 4 and the other figures give $Re_\tau=774$ for that station.
- **$Re_\tau^*$ in the text against Table 4.** §4.1 (A3-23) gives $Re_\tau^*=2626$, 9178 and 6213 at $Re_\tau=1172$; Table 4 gives 2761, 9114 and 6149 for the same stations; Table 1 gives the M11Tw020 maximum as 6261.
- **Eq. 4.4.** The total-stress-based transformation is printed with upper limit $u^+$ and differential $dz^*$, with an integrand in $z^*$.
- **Table 3 Reynolds-number ranges** *(compiler check, not in the sources)*. By the Table 1 definitions, $Re_\theta/Re_{\delta2}=\mu_w/\mu_\infty$ is fixed within a case. Tables 1 and 4 respect this (for example M2p5HighRe $2207/1292=1.71$), Table 3 does not: $871/621=1.40$ (M2p5HighRe, lower bound), $2142/785=2.73$ (M6Tw025, upper, against about 1.9), $9848/1621=6.08$ (M6Tw076, upper, against about 5.1–5.2), $9405/1428=6.59$ (M8Tw048, upper, against about 5.0). The M6Tw025 upper $Re_\theta$ equals the Table 1 upper bound while its $Re_\tau$, $Re_{\delta2}$ and $Re_\tau^*$ upper values equal the Table 1 lower bounds.
- **Shape factor of M14Tw018** *(compiler check, not in the sources)*. §3.2 states $H_{12}$ ranges "from $H_{12}\approx4$ for case M2p5 to $H_{12}\approx54$ for case M14Tw018" and that Eq. 3.8a fits the hypersonic cold-wall cases within 8%. Eq. 3.8a at $M_\infty=13.64$, $T_w/T_r=0.18$ gives $4(1+0.344\cdot13.64^2)/(3\cdot1.82^{1.35})=38.6$, about 40% below 54; for M11Tw020 it gives 25.2 against the Table 4 values 26.0 and 26.7.
- **Typos.** "previous studiesc" (A3-27), "outside the the" (A3-8), "it would not be possible to quantity" (A3-46), "whereas and" (A3-18).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $x$, $y$, $z$ | $x$, $z$, $y$ | **collision:** the source's $z$ is wall-normal and $y$ spanwise |
| $u$, $v$, $w$ | $u$, $w$, $v$ | **collision:** the source's $w$ is wall-normal, $v$ spanwise |
| $\bar f$, $f'$ | $\langle f\rangle$, $f'$ | **collision:** the source's overbar is a Reynolds average, the registry's an LES filter |
| $\tilde f$, $f''$ | $\langle f\rangle_\rho$, $f''$ | **collision:** the source's tilde is a Favre average, the registry's a Favre filter; $\tilde x$ (Eq. 3.1) is an effective turnover length |
| $\overline{\rho u_i''u_j''}/\tau_w$ | $\langle\rho u_i''u_j''\rangle/\tau_w$ | Morkovin scaling; positive convention |
| $(u''w'')^*=-\overline{\rho u''w''}/\tau_w$ | $-\langle\rho u''v''\rangle/\tau_w$ | positive Reynolds shear stress |
| $z_\tau=\nu_w/u_\tau$, $z^+$ | $\delta_\nu$, $y^+$ | |
| $z^*$, $\lambda_x^*$, $\lambda_y^*$ | $y^*$, $\lambda_x^*$, $\lambda_z^*$ | semi-local scaling |
| $Re_\tau^*=\rho_\delta\sqrt{\tau_w/\rho_\delta}\,\delta/\mu_\delta$ | $Re_\tau^*$ | at the boundary-layer edge |
| $\delta$, $\delta_i$, $\delta_\infty$ | $\delta_{99}$, (inflow thickness), (height where $\langle u\rangle$ first reaches $U_\infty$) | |
| $H_{12}=\delta^*/\theta$ | (shape factor) | |
| $Re_\theta$, $Re_{\delta2}$ | $Re_\theta$, (momentum-thickness Reynolds number with wall viscosity) | |
| $C_f$, $C_h$, $R_{af}=2C_h/C_f$ | $C_f$, (Stanton number, Reynolds analogy factor) | |
| $F_c$, $F_\theta$ | (skin-friction and Reynolds-number transformation factors) | VD = van Driest II, SC = Spalding–Chi |
| $T_r$, $r=0.89$, $r_g$ | (recovery temperature, recovery factor, generalized recovery factor) | |
| $B_q=q_w/(\rho_wc_pu_\tau T_w)$, $M_\tau$ | (wall heat-flux parameter, friction Mach number) | Table 4 lists $-B_q$ |
| $u^+_{VD}$, $u^+_{TL}$, $u^+_V$, $u^+_{TS}$, $S^+_{eq}$, $S^+_{TL}$ | same | $S^+_{eq}=(\mu_w/\bar\mu)\partial u^+/\partial z^*$, $S^+_{TL}=(\bar\mu/\mu_w)\partial u^+/\partial z^+$, as on the transformation page |
| $k$ in $(1/k)\log z^+$, $C_{VD}$, $C_{TL}$ | $\kappa$, $B$ | $\kappa=0.41$ in the figures; **collision:** $k$ is also the wavenumber |
| $N$ (Eq. 4.6) | $n$ (page-local) | **collision:** registry $N$ is the polynomial degree |
| $A_i$, $B_i$ | (attached-eddy slope, intercept) | **collision:** $B_i$ is not the log-law intercept $B$; source index 2 (spanwise) is registry index 3 |
| $\alpha$, $\beta$ (Eq. 4.9) | $a_1$, $a_2$ (page-local, as on the [Morkovin page](/definitions/morkovin-hypothesis.md)) | **collision:** not the DG blending factor or the field-inversion correction |
| $Pr=0.71$, $Pr_t$ | $Pr$, $Pr_t$ | |
| $R_{u''T''}$ | (velocity–temperature correlation coefficient) | |
| $\eta$, $\phi$ | $\eta$, (viscous dissipation per unit volume) | |
| $\log$ | — | base not stated in Eqs. 3.7c, 3.9, 3.13, 4.8 |

# Reference list

103 printed references, author–year style (JFM), with letter suffixes for
same-author same-year works (Bernardini & Pirozzoli 2011a, b; Hutchins &
Marusic 2007a, b). The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Further
same-key pairs are keyed in printed order (Duan, Beekman & Martín 2011 and
Duan & Martín 2011; Pirozzoli 2011 and Pirozzoli & Bernardini 2011;
Schlatter et al. 2010 and Schlatter & Örlü 2010). The cited Griffin, Fu &
Moin (2021) is distinct from the ingested
[griffin-2023](/sources/griffin-2023.md). Schlatter et al. (2009) prints the
second author "Örl'u" (entered as Örlü); Crocco (1932) prints the journal
"LAerotecnica"; Hopkins & Inouye (1971) prints volume 6 (9) and is recorded
as printed. No printed duplicates or unparseable items.

# Pages created or updated

Chunk 2 (2026-10-25), cited further in chunks 3–4. This source is cited on:

- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Attached-eddy hypothesis](/definitions/attached-eddy-hypothesis.md)
- [Compressible velocity transformations](/definitions/compressible-velocity-transformation.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Morkovin's hypothesis and Reynolds analogies](/definitions/morkovin-hypothesis.md)
- [Inflow turbulence generation](/methods/inflow-turbulence-generation.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
