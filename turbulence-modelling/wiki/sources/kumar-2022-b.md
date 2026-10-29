---
type: Source
title: "Kumar & Ghosh (2022) — Application of bandwidth-optimized WENO schemes to DNS of shock–turbulence interaction problems"
description: "Compares bandwidth-optimized WENO schemes with a relative total-variation limiter against WENO-JS, WENO-BS, WENO-Z, WENO-CU6, TENO6 and TENO8 on gas-dynamics tests and grind time, then uses the three-point variant for DNS of a supersonic isothermal channel and of a shock train in a plane isolator."
resource: "doi:10.1007/s00193-021-01052-4"
source_kind: paper
authors: [Kumar S., Ghosh S.]
year: 2022
venue: "Shock Waves 32:69-102"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2021_Crossref_Shock_Waves_Kumar_Application_of_bandwidth-optimized_WENO_schemes_to_DNS_of_sh.pdf"
tags: [weno, shock-capturing, numerical-dissipation, dns, compressible]
timestamp: 2026-10-29T10:05:00Z
---

# Summary

Kumar & Ghosh (2022) assess the bandwidth-optimized
[WENO schemes](/methods/weno-scheme.md) of Martin et al. (2006) with the
relative total-variation limiter of Taylor et al. (2007), in a three-point
variant (four candidate stencils, six points, symmetric set) and a
four-point variant (five stencils, eight points), named after the limiter
threshold. The limiter sets every smoothness indicator to zero, hence the
weights to the optimized linear ones, where the stencil total variations
are within the threshold, so that the nonlinear part acts only at
discontinuities (§1); the switch is recorded with the other
[shock sensors](/definitions/shock-sensor.md). The optimized linear
weights give, in the authors' words, dispersion comparable to the
sixth-order compact central scheme in smooth regions (§1); the paper
mentions hybrid compact/WENO schemes among the alternatives (see
[low-dissipation low-dispersion schemes](/methods/low-dissipation-low-dispersion-scheme.md)). The framework is characteristic-wise Lax–Friedrichs flux-split
finite differences with Roe averaging, third-order TVD Runge–Kutta and
fourth-order central viscous terms. The comparison schemes are WENO-JS,
the seventh-order WENO-BS, WENO-Z, WENO-CU6, TENO6 and TENO8.

On linear advection, the Lax, Shu–Osher and double-blast problems, a 2D
Riemann problem, double Mach reflection, single-mode
[Rayleigh–Taylor](/benchmarks/rayleigh-taylor-mixing.md) instability and
the 2D viscous shock tube, the bandwidth-optimized schemes resolve more
small-scale structure than WENO-JS and in several cases than WENO-BS;
TENO6 and TENO8 resolve slightly more but cost up to 2.9 times WENO-JS,
against 1.045 for the three-point scheme. The inviscid roll-ups are
attributed to [numerical dissipation](/properties/numerical-dissipation.md)
alone. A higher threshold resolves more, but double Mach reflection is
unstable at threshold 7 (three-point) and 5 (four-point); threshold 5 is
chosen. The three-point scheme then runs a [DNS](/definitions/direct-numerical-simulation.md)
of a supersonic isothermal-wall [channel](/benchmarks/turbulent-channel-flow.md)
(centreline Mach 1.49, $Re_\tau=240$), compared with Ghosh et al. (2010),
and a DNS of a shock train in a constant-area isolator without sidewalls,
an internal [shock–boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md).
The shock train extends to $x/L_x=0.3$, near-wall sweeps and ejections
intensify through the shocks, and the centreline axial Reynolds stress
rises in compressions and in the mixing region, the amplification
discussed on [shock-generated turbulence](/results/shock-generated-turbulence.md).
Wall-unit resolution and averaging times of the DNS are not reported.

# Version read

Version of record (Springer, Shock Waves; received 13 February 2020,
revised 5 October 2021, accepted 20 October 2021, online 17 November
2021): 34 pages (pp. 69–102), all read, pp. 71, 73–75, 77 and 95 also
visually. Page 1 matches the metadata; the filename year 2021 is the
online year. Equation, table and figure numbers are those of this
version.

# Key claims

Page-local symbols: BW3-$P$ and BW4-$P$ the source's WENO3P-LIM-'P' and
WENO4P-LIM-'P'; $P_{\mathrm{TV}}$ the limiter threshold (registry §11; the source's
$\alpha^{RL}_{TV}$); $R_{\mathrm{TV}}$ the relative total variation,
$TV_k$ the total variation of stencil $k$; $q$ the weight exponent; $r$
the number of points per candidate stencil; $f^\pm$ the split fluxes.
WENO weights in registry notation: $\mathrm{IS}_k$, $a_k$, $\mathsf w_k$,
$d_k$; TENO: $\gamma^{\mathrm T}_k$, $\chi^{\mathrm T}_k$,
$\delta^{\mathrm T}_k$, $C_T$.

1. WENO-JS is robust for shocks but too dissipative for turbulence; compact central schemes resolve well but are non-dissipative and unsuited to shocks (§1). **Stated**
2. Bandwidth-optimized WENO has dispersion comparable to the sixth-order compact central scheme in smooth regions and captures discontinuities; the Taylor et al. limiter confines the nonlinear part to discontinuities (§1). **Stated**
3. The three- against four-point comparison on the 2D Riemann problem, Rayleigh–Taylor instability and viscous shock tube has not been shown before; Radice & Rezzolla compared them on double Mach reflection without saying whether the limiter is based on the smoothness indicator or the total variation (§1). **Stated**
4. Three-point scheme: candidate fluxes on $\{i-2..i\}$, $\{i-1..i+1\}$, $\{i..i+2\}$, $\{i+1..i+3\}$ (Eqs. 14–17), $a_k=d_k/(\epsilon+\mathrm{IS}_k)^q$, $\epsilon=10^{-6}$, $d_k=(0.094647545896,0.428074212384,0.408289331408,0.068988910311)$ (Eq. 20), Jiang–Shu indicators (Eq. 22), and $\mathrm{IS}_3=\max_k\mathrm{IS}_k$ to keep the downwind stencil least influential at a discontinuity (Eq. 23); $q=2$ against WENO-JS, $q=1$ otherwise and in the DNS, after Martin et al. (§2.2.1). **Stated** (from [1])
5. Limiter: $\mathrm{IS}_k=0$ for all $k$ if $R_{\mathrm{TV}}=\max_kTV_k/(\epsilon+\min_kTV_k)\le P_{\mathrm{TV}}$, $TV_k=\sum_{l=1}^{r-1}|f^+_{i+k+l-r+1}-f^+_{i+k+l-r}|$ (Eqs. 24–26); $P_{\mathrm{TV}}$ "is an arbitrary constant" whose choice "is important in determining the suitability of the scheme for shock–turbulence interactions" (§2.2.1). **Stated**
6. Four-point scheme: five four-point stencils on $\{i-3..i+4\}$ (Eqs. 41–44), $d_k=(0.040195483373,0.249380000671,0.480268625626,0.200977547673,0.029178342658)$ (Eq. 47), indicators with weights $\tfrac1{36}$, $\tfrac{13}{12}$, $\tfrac{781}{720}$ (Eq. 49) (§2.2.6). **Stated** (from [1])
7. Linear advection of $e^{-300(x-0.5)^2}$ ($t=1$, 101–1601 points): BW3-5 and BW4-5 with $q=2$ agree in $L_\infty$ error with the linear symmetric bandwidth-optimized schemes $r=3$ and $r=4$, and the authors conclude they "demonstrate the accuracy of third and fourth orders, respectively" (§3.1.1, Fig. 3). **Shown** (no rates tabulated)
8. Shu–Osher problem on 200 points: BW3-5 ($q=2$) is closer to the 1600-point WENO-JS reference than WENO-BS, BW4-5 closer still; WENO-JS damps the high-frequency region (§3.1.3, Fig. 6). With $q=1$, BW3-5 captures the peaks better than WENO-Z, WENO-CU6, TENO6 and TENO8 except near $x=0.8$, where WENO-CU6 and TENO6 are slightly better; TENO8 is slightly better than BW4-5 near $x=0.7$ and 0.8 (Fig. 8). **Shown**
9. Raising $P_{\mathrm{TV}}$ from 3 to 10 improves high-frequency peaks (Shu–Osher, Fig. 7) and increases small-scale and vortical structure (2D Riemann Fig. 12, double Mach Fig. 17, Rayleigh–Taylor Fig. 21) (§3.1). **Shown**
10. Grind time normalized by WENO-JS, Shu–Osher (Table 1): WENO-Z 1.024, BW3-5 1.045, WENO-CU6 1.5, TENO6 2.126, WENO-BS 1.416, BW4-5 1.371, TENO8 2.9; 2D Riemann (Table 2): 0.941, 1.066, 1.275, 1.407, 1.371, 1.321, 2.17 (§3.1.3, §3.1.5). **Shown**
11. 2D Riemann problem ($1/400$, $t=0.8$): both bandwidth-optimized schemes capture slip-line roll-up that WENO-JS damps; BW3-5 shows more vortical structure than WENO-BS, WENO-CU6 slightly more than BW3-5, TENO6 and TENO8 clearly more than both; the structures are "purely" numerical-viscosity effects, the flow being inviscid (§3.1.5, Figs. 10–14). **Shown**
12. Double Mach reflection ($1/480$, $t=0.2$): WENO-JS, BW3-3, WENO-BS and BW4-3 capture the shocks, primary slip line and Mach stem but not the secondary slip line in density (it shows in $\rho v$); the bandwidth-optimized schemes resolve roll-up better (§3.1.6, Fig. 16). **Shown**
13. Stability: in double Mach reflection the three-point scheme is not stable with threshold 7, the four-point with threshold 5; TENO8 is unstable at this resolution "due to its less dissipative nature near the shocks" (§3.1.6). **Shown**
14. Rayleigh–Taylor ($\gamma=5/3$, $1/480$ and $1/960$, $t=1.95$): WENO-JS and WENO-BS show no noticeable roll-up on the coarse grid, the bandwidth-optimized schemes do; BW4-5 ($q=2$) breaks symmetry, BW3-5 only marginally on the fine grid; TENO6 and TENO8 show streaky structures; less dissipative schemes lose symmetry, as in Fu et al. (§3.1.7, Figs. 19–22). **Shown**
15. Viscous shock tube, $Re=1000$: the $1/3000$ WENO-JS solution puts the triple point at $x=0.586$, $y=0.155$, matching Daru & Tenaud and Zhou et al.; triple-point heights ($\times10$) on $1/1000$: WENO-JS 1.33, BW3-5 1.38, BW4-5 1.48; on $1/1500$: 1.50, 1.52, 1.53; reference 1.55 (§3.1.8, Table 3, Figs. 23–25). **Shown**
16. BW3 with a proper limiter is a good compromise of cost and accuracy; the schemes are stable with thresholds around 10 except in complex cases like double Mach reflection, very high values give Gibbs oscillations near shocks, and threshold 5 is chosen (§3.2.1). **Shown** (from §3.1) / choice **Stated**
17. Supersonic isothermal channel with BW3-5 ($4\pi\delta\times2\delta\times4\pi\delta/3$, $192\times128\times151$): centreline Mach 1.49 and $Re_\tau=240$ against Ghosh et al.'s 1.48 and 246 (Table 4); mean density, temperature, Mach number and rms velocities agree; small anisotropy differences are attributed to differences in mean density (§3.2.2, Figs. 26–29). **Shown**
18. Shock-train DNS (inflow from a concurrently run periodic channel at Mach 1.5, $Re_\tau=\rho_wu_\tau\delta/\mu_w=247$; outlet pressure about twice the inlet): multiple shocks near the inlet, train up to $x/L_x=0.3$; centreline pressure and density rise in compressions, drop in expansions and rise gradually in the mixing region, the Mach number the opposite (§3.2.3, Figs. 33–35). **Shown**
19. Near-wall sweep–ejection activity intensifies through the shocks; the shocks are not always symmetric about the centreline; separation with boundary-layer thickening occurs near the shocks (§3.2.3, Figs. 30–32). **Shown** (contours)
20. The centreline axial Reynolds stress (normalized by the inlet wall shear stress) jumps in compressions and falls in expansions, grows in the mixing region up to $x/L_x=0.78$, then declines but stays above its inlet value; the other normal stresses behave alike with smaller magnitudes (§3.2.3, Fig. 36). **Shown**
21. The centreline density and pressure behaviour matches the LES of a shock train in a supersonic pipe of Mahapatra et al. (§3.2.3). **Stated**
22. Conclusion: BW3-5 represents the Shu–Osher fluctuations better than WENO-Z and WENO-CU6 and nearly as well as TENO in smooth regions, WENO-CU6 is marginally better near shocks, BW3 with threshold 7–10 "may also show better performance compared to the WENO-CU6 scheme", and the limited bandwidth-optimized schemes are cheaper than TENO6, TENO8 and WENO-CU6 (§4). **Shown** / the threshold remark **Stated**

# Printed slips

- **Eq. (50), WENO-BS linear weights:** printed $d_k=(1/35,12/35,8/35,4/35)$. *(Compiler check, not in the sources: they sum to $25/35$, not 1.)* The other printed weight sets (Eqs. 20, 27, 31, 36, 47) sum to 1 to the printed digits.
- **Conclusions against §3.1.6:** §4 names thresholds 7–10 for the three-point scheme, while §3.1.6 reports it unstable at threshold 7 in double Mach reflection.
- **Table 4 / §3.2.2 against §3.2.3:** the periodic channel is given as centreline Mach 1.49, $Re_\tau=240$, the coupled inflow channel on the same domain and grid as Mach 1.5, $Re_\tau=247$, without comment.
- **§3.1.3:** "WENP4P-LIM-'P'" and "WENP4P-LIM-5".
- **Eqs. (16), (43):** the candidate-flux coefficients are printed $\alpha_{kl}$, the letter of the nonlinear weights $\alpha_n^L$.
- **Eq. (24):** "$\le$" while the text says "less than the threshold value".
- **Figs. 19–22 captions:** "color contour range: 0.9–0.22", as printed.
- **Eq. (9):** the Fourier law is printed $q_x=\lambda\,\partial T/\partial x$, without a minus sign.
- **Ref. [35]:** book title printed "Upwind and High-Resolution Schemespp".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\beta_k^L$ | $\mathrm{IS}_k$ | smoothness indicator; **collision:** not the field-inversion $\beta$ |
| $\alpha_n^L$, $\omega_n^L$, $C_n^L$ | $a_k$, $\mathsf w_k$, $d_k$ | **collision:** $\alpha$ is the DG blending factor, $\omega$ the specific dissipation rate in the registry |
| $\alpha_{kl}$, $d_{kml}$ | (candidate-flux and indicator coefficients, page-local) | |
| $\alpha^{RL}_{TV}$ ('P'), $R(TV)$, $TV_k$ | $P_{\mathrm{TV}}$ (registry §11), $R_{\mathrm{TV}}$, $TV_k$ (page-local) | |
| $\delta_n$, $\chi_n$, $\gamma_n$, $C_T$ | $\delta^{\mathrm T}_k$, $\chi^{\mathrm T}_k$, $\gamma^{\mathrm T}_k$, $C_T$ | TENO; **collision:** $\gamma_n$ is not the ratio of specific heats |
| $\tau_5$, $\tau_6$, $\beta_6^L$, $C$ | (reference indicators, six-point indicator, CU6/TENO constant, page-local) | **collision:** $\tau_5$, $\tau_6$ are not stresses |
| $\tau_{ij}$ | $\sigma_{ij}$ | viscous stress; **collision:** not the subgrid stress |
| $\xi,\eta,\zeta$ | (computational coordinates) | **collision:** $\eta$ is not the Kolmogorov length |
| $k_y$ | (grid stretching factor, page-local) | **collision:** not $k$ |
| $\lambda$ | (thermal conductivity) | |
| $P$, $e$ | $p$, (specific total energy) | |
| $h$ | $\delta$ | channel half-width |
| $Re_\tau=\rho_wu_\tau h/\mu_w$ | $Re_\tau$ | wall density and viscosity |
| $N$ | $N_x$ | grid points; **collision:** not the polynomial degree |
| $\gamma$, $Re$ | $\gamma$, $Re$ | viscous shock tube: $\mu=1/Re$ |

# Reference list

51 printed references, numbered style ([1]–[51]), Springer format with
DOIs. The list is merged complete into the [bibliography](/bibliography.md)
with `citedby` this slug. Ref. [28] (Fiévet et al., AIAA J. 2017) prints
no volume or pages; ref. [35] is a chapter of "Upwind and High-Resolution
Schemes" (Springer 1989, pp. 328–374); ref. [17] prints "supersonic
turbulent boundary interaction" in its title. No cited key collides with a
bundle Source slug, and no item is unparseable.

# Pages created or updated

Chunk 9 (2026-10-27). This source is cited on:

- [Rayleigh–Taylor mixing](/benchmarks/rayleigh-taylor-mixing.md)
- [Shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Shock sensors and troubled-cell indicators](/definitions/shock-sensor.md)
- [Low-dissipation low-dispersion schemes with shock sensor](/methods/low-dissipation-low-dispersion-scheme.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Shock-generated turbulence and turbulent shock jump relations](/results/shock-generated-turbulence.md)
