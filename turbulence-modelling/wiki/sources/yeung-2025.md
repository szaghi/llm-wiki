---
type: Source
title: "Yeung et al. (2025) — Small-scale properties from exascale computations of turbulence on a 32 768³ periodic cube"
description: "Pseudo-spectral GPU DNS of forced isotropic turbulence up to Re_lambda 2500 on a 32 768³ grid on the Frontier exascale machine, made affordable by multi-resolution independent simulations; reports a constant normalized dissipation, a bottleneck and steeper-than-Kolmogorov spectrum, and dissipation and enstrophy PDF tails."
resource: "doi:10.1017/jfm.2025.10493"
source_kind: paper
authors: [Yeung P.K., Ravikumar K., Uma-Vaideswaran R., Dotson D.L., Sreenivasan K.R., Pope S.B., Meneveau C., Nichols S.]
year: 2025
venue: "J. Fluid Mech. 1019:R2"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2025_Crossref_Journal_of_Fluid_Mechanics_Yeung_Small-scale_properties_from_exascale_computations_of_turbule.pdf"
tags: [dns, isotropic-turbulence, intermittency, gpu, energy-cascade]
timestamp: 2026-10-26T20:48:00Z
---

# Summary

Yeung et al. (2025) report [direct numerical simulations](/definitions/direct-numerical-simulation.md)
of forced, statistically stationary, incompressible
[homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
in a $(2\pi)^3$ periodic box. They reach $Re_\lambda\approx2500$ on a
$32\,768^3$ grid, run with a GPU Fourier pseudo-spectral code in single precision
on Frontier, the first exaflop machine. A long run at this grid is unaffordable:
13 s per step on 44% of the machine, about 1000 steps per Kolmogorov time, and
large-eddy times of about $300\tau_\eta$. The data therefore come from
[multi-resolution independent simulations](/methods/multi-resolution-independent-simulations.md)
(Yeung & Ravikumar 2020), extended here to raise the Reynolds number. A long
run at modest resolution ($k_{\max}\eta\approx1.4$) is continued briefly with a
halved time step and then with a halved grid spacing ($k_{\max}\eta\approx2.8$).
Each refined segment lasts only a few $\tau_\eta$, and the statistics are
ensemble-averaged over 3–4 segments. Higher $Re_\lambda$ is reached by lowering
the viscosity at fixed forcing and fixed $k_{\max}\eta$ while refining the grid.

Five Reynolds numbers are covered, $Re_\lambda\approx390$ to 2500 ($2048^3$ to
$32\,768^3$). The normalized mean dissipation $C_\varepsilon$ shows a weak trend
up to $Re_\lambda\approx1500$ and then a constant slightly above 0.4, so the
dissipative anomaly holds beyond $Re_\lambda=2500$. The compensated energy
spectrum has no plateau: the inertial-range slope is steeper than $-5/3$, and a
[bottleneck](/definitions/bottleneck-effect.md) peaks at $k\eta$ between 0.1
and 0.2. The PDFs of dissipation and enstrophy have chi-square left tails, which
give the kinematic relation $f_{\omega^2}\propto f_\varepsilon^{1/3}$, and
stretched-exponential right tails with nearly equal exponents. Enstrophy moments
exceed dissipation moments by a ratio nearly independent of $Re_\lambda$,
consistent with Nelkin (1999). One $32\,768^3$ snapshot is public in the Johns
Hopkins Turbulence Database. The paper studies small-scale physics, not closure
modelling.

# Version read

Version of record (J. Fluid Mech. Rapids, Cambridge University Press, open
access CC BY 4.0; received 12 June 2025, revised 18 July 2025, accepted 18 July
2025), 12 pages (R2-1 to R2-12), all read; pp. 4–8 checked visually for
equations and symbols. Page 1 matches Crossref (Crossref omits the middle
initials). The printed title writes the grid as $\mathbf{32\,768^3}$; the
frontmatter title uses plain text. Locators are the journal's sections,
equations, figures and tables.

# Key claims

Page-local symbols: $u'$ r.m.s. velocity (one component); $L$ longitudinal
integral scale (the source's $L_1$) and $Re_L=u'L/\nu$; $C_\varepsilon=\langle\varepsilon\rangle L/u'^3$;
$T_E$ large-eddy turnover time; $C_{\mathrm{CFL}}$ Courant number;
$\omega^2=\omega_i\omega_i$ enstrophy density (the source's $\Omega$);
$f_\varepsilon$, $f_{\omega^2}$ PDFs of $\varepsilon/\langle\varepsilon\rangle$ and
$\omega^2/\langle\omega^2\rangle$; $N_1$, $N_2$ grid points per direction before
and after refinement; $M$ number of segments.

1. DNS of forced isotropic turbulence at $Re_\lambda=2500$ on a $32\,768^3$ periodic grid was obtained with a GPU pseudo-spectral code on the 1.1-exaflop Frontier machine (Abstract; §1; Table 1). **Shown**
2. The largest pseudo-spectral DNS that fits in Frontier's memory is $40\,960^3$; $32\,768^3$ is "more realistic for our present purposes" (§1). **Stated**
3. The best timing for $32\,768^3$ is 13 s per step on 44% of the machine (citing the companion CPC paper); at $Re_\lambda\approx2500$ one $\tau_\eta$ takes about 1000 steps and $T_E/\tau_\eta\approx300$, so a $10T_E$ run would need "two years or more of virtually non-stop computing" (§1). **Stated**
4. After the time step or grid spacing is halved, scales of the order of the coarser grid's $\eta$ equilibrate in about $2\tau_\eta$ (§2.2, citing Yeung et al. 2018; Yeung & Ravikumar 2020). **Stated**
5. The protocol has three phases: (1) a long run adequate for scales larger than $\eta$; (2) a halved time step for a few $\tau_\eta$ ($C_{\mathrm{CFL}}$ 0.6 to 0.3); (3) a halved grid spacing for a few $\tau_\eta$ ($k_{\max}\eta$ 1.4 to 2.8); it is repeated from different phase-1 snapshots and ensemble-averaged (§2.2; Table 1 caption). **Stated** (method)
6. Grid refinement can be done in increments, e.g. $N_1\to3N_1/2\to2N_1$ (§2.2). **Stated**
7. A single segment at $Re_\lambda=1000$ on $8192^3$ spanning $27\tau_\eta$ suggests the results are insensitive to the phase-3 durations of Table 1, "presumably because the energy of the large scales is kept frozen by the forcing scheme" (§2.2). **Shown** (test not displayed)
8. All runs are in single precision; round-off effects are judged unlikely to have strongly affected the conclusions, but "rigorous testing is not readily available" (§2.2). **Stated**
9. At fixed forcing and fixed $k_{\max}\eta$, refining $N_1\to N_2$ with $\eta\propto1/N$ and $\langle\varepsilon\rangle$ independent of $\nu$ gives $\nu\propto N^{-4/3}$; with $u'$ unchanged, $\langle\varepsilon\rangle=15\nu u'^2/\lambda^2$ gives $Re_\lambda\propto N^{2/3}$, a 58% increase for $N_2=2N_1$ (§2.2). **Derived**
10. In the $Re_\lambda=2080$ ($12\,288^3$) to 2500 ($16\,384^3$) transition, the kinetic energy varies little, the mean dissipation recovers from the viscosity drop within about $20\tau_\eta$, and the dissipation skewness recovers sooner (§2.2, Fig. 1a). **Shown**
11. At the start of refinement $Re_\lambda$ jumps to $Re_{\lambda1}/0.6814$ and then decreases to about $1.23Re_{\lambda1}$, agreeing with the expected 21.1% increase for $N_2/N_1=4/3$ (§2.2, p. R2-6). **Shown**
12. Under viscosity reduction the dissipation spectrum settles quickly onto a new nearly stationary form; for $N_2/N_1=2$ the transition is longer, $Re_\lambda$ dropping further before rising (§2.2, Fig. 1b). **Shown**
13. $Re_L=C_\varepsilon Re_\lambda^2/15$ with $C_\varepsilon=0.45$; $L/\eta\propto Re_\lambda^{3/2}$ and $(L/u')/\tau_\eta\propto Re_\lambda$ (§3, Fig. 2a,b). **Shown**
14. $C_\varepsilon$ shows a weak trend up to $Re_\lambda\approx1500$ and then stabilizes at a constant "slightly larger than 0.4"; the zeroth law holds beyond $Re_\lambda=2500$ (§3, Fig. 2c). **Shown**
15. The compensated spectrum $E(k)\langle\varepsilon\rangle^{-2/3}k^{5/3}$ has no plateau: the data support a slope steeper than $-5/3$ plus a bottleneck strongest at $k\eta$ between 0.1 and 0.2; the reference lines are the "generally accepted" values 1.62 (3D) and $1.62\times18/55=0.53$ (1D) (§3, Fig. 3b). **Shown**
16. The bottleneck peak lies slightly below the wavenumber of the dissipation-spectrum peak ($\propto k^2E(k)$), "hence viscous effects certainly play a role"; it is weaker in the 1D longitudinal spectrum $E_{11}$ than in $E$; consistency with isotropy relations such as the printed "$E(k)=k^3\,\mathrm d[(1/k)\,\mathrm dE_{11}(k)]/\mathrm dk$" is verified (§3). **Shown** / **Stated**
17. Both very low and very high values of enstrophy are more probable than those of dissipation (§4, Fig. 4). **Shown**
18. Low-amplitude zones are nearly Gaussian, so the left tails behave as chi-square of order 3 (enstrophy) and 5 (dissipation), $f(x)\propto x^{n/2-1}$, giving $f_{\omega^2}(x)\propto[f_\varepsilon(x)]^{1/3}$ (Eq. 4.1), a kinematic relation holding at $Re_\lambda=390$ and 2500 (§4, Fig. 4). **Derived** + **Shown**
19. The right tails are stretched exponentials, $f_\varepsilon\propto\exp(-a_\varepsilon x^{b_\varepsilon})$ and $f_{\omega^2}\propto\exp(-a_\omega x^{b_\omega})$ (Eq. 4.2), with $b_\omega=b_\varepsilon$ and $a_\omega<a_\varepsilon$, so high-order moments differ only through the prefactors (§4). **Shown**
20. In the $\ln(-\ln[f(x)/f(1)])$ test at $Re_\lambda\approx390$, 1000, 2500 the dissipation and enstrophy lines become more nearly parallel as $Re_\lambda$ increases, enstrophy with the smaller intercept; the reference slope 0.518 is stated to correspond to 0.225 of Gotoh & Yeung (2025) with common instead of natural logarithm (§4, Fig. 5). **Shown**
21. Normalized moments of orders 2, 3, 4 of $\omega^2/\langle\omega^2\rangle$ exceed those of $\varepsilon/\langle\varepsilon\rangle$, with a ratio nearly independent of $Re_\lambda$, consistent with Nelkin (1999): enstrophy more intermittent, same asymptotic scaling (§4, Fig. 6). **Shown**
22. The skewness and flatness of the longitudinal velocity gradient agree with the data compiled by Sreenivasan & Antonia (1997) (§4). **Stated** (no figure)
23. The conclusions of Fig. 2(c) and Fig. 6(a,b) "would differ if data points at $R_\lambda\approx1600$ and 2500 were absent" (§5). **Stated**
24. Going from $Re_\lambda=1000$ to 2500 needs four times more grid points per direction, i.e. at least 64 times the wall time per step and 256 times for a given physical time span, on a machine with at least 64 times more memory (§5). **Derived**
25. The protocol may not apply to phenomena evolving on inertial-range or energy-containing time scales (non-stationary turbulence, highly variable forcing); extensions to passive-scalar small scales and short-time Lagrangian statistics are planned (§5). **Stated**
26. Scales finer than the Kolmogorov scale appear more copiously as the Reynolds number increases, requiring better small-scale resolution than often practised (§1, citing Yakhot & Sreenivasan 2005). **Stated**

Run parameters (Table 1; $k_{\max}\eta\approx2.8$, $C_{\mathrm{CFL}}\approx0.3$ at
the finest stage; forcing keeps the energy of the first three wavenumber shells
constant, $k_F=2.5$, after Donzis & Yeung 2010):

| $Re_\lambda$ | $N_x^3$ | $\nu$ | $M$ | phase-3 duration $/\tau_\eta$ |
|---|---|---|---|---|
| 390 | $2048^3$ | $4.370\times10^{-4}$ | 4 | 3.74 |
| 650 | $4096^3$ | $1.732\times10^{-4}$ | 3 | 4.06 |
| 1000 | $8192^3$ | $6.883\times10^{-5}$ | 3 | 2.56 |
| 1600 | $16\,384^3$ | $2.7319\times10^{-5}$ | 3 | 1.84 |
| 2500 | $32\,768^3$ | $1.10555\times10^{-5}$ | 3 | 1.93 |

# Printed slips

- **Eq. (4.1), p. R2-8:** "$f_\Omega(x)\propto[(f_\epsilon(x)^{2/3}]^{1/2}$": one opening parenthesis is never closed.
- **§2.2, p. R2-6:** "$R_\lambda(0)=R_{\lambda1}/0.6814$, then decreases to approximately $0.84R_{\lambda0}=1.23R_{\lambda1}$": $R_\lambda(0)$ and $R_{\lambda0}$ denote the same quantity.
- **Fig. 2:** the text says "The dashed line corresponds to $C_\epsilon R_\lambda^2/15$", the caption "Dotted lines in (a) and (b) show expected power laws".
- **Fig. 5:** "Perfect fits give straight lines of slope equal to the exponent and intercepts on the y-axis equal to the prefactor"; for $f\propto\exp(-ax^b)$ the large-$x$ intercept of $\ln(-\ln[f(x)/f(1)])$ against $\ln x$ is $\ln a$, not $a$ *(compiler check, not in the sources)*. The axis label prints "$f_X(x)/f_x(1)$".
- **§1 cost estimate:** the printed figures (13 s per step, about 1000 steps per $\tau_\eta$, $T_E\approx300\tau_\eta$) give about $3.9\times10^7$ s, about 1.2 years, for $10T_E$, against "two years or more" *(compiler check, not in the sources)*; the paper does not say what else the estimate includes.
- Typos: "Srenivasan" (p. R2-8 and the Yeung, Donzis & Sreenivasan 2012 reference), "itsname" (p. R2-5), "postponeed" and "size,with" (p. R2-10).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $R_\lambda$ | $Re_\lambda$ | $u'\lambda/\nu$, implied by $\langle\varepsilon\rangle=15\nu(u'/\lambda)^2$ |
| $R_\ell$, $L_1$ | $Re_L$, $L$ | longitudinal integral scale |
| $\epsilon$, $\langle\epsilon\rangle$ | $\varepsilon$, $\langle\varepsilon\rangle$ | angle brackets: space–time and ensemble average |
| $\Omega\equiv\omega^2$ | $\omega^2=\omega_i\omega_i$ | **collision** with the rotation-rate tensor $\Omega_{ij}$; no factor 1/2 |
| $C_\epsilon$ | $C_\varepsilon$ | page-local |
| $\eta$, $\tau_\eta$, $\lambda$, $\nu$ | same | |
| $T_E$ | $T_E$ | page-local large-eddy turnover time |
| $N$, $N^3$, $N_1$, $N_2$ | $N_x$, $N_x^3$ | **collision:** the source's $N$ is not the polynomial degree |
| $k_{max}\eta=(\sqrt2N/3)\eta$ | $k_{\max}\eta$ | spectral resolution parameter |
| $C=[\lvert u\rvert+\lvert v\rvert+\lvert w\rvert]_{max}\Delta t/\Delta x$ | $C_{\mathrm{CFL}}$ | **collision** with model constants |
| $E(k)$, $E_{11}(k)$, $D(k)$ | $E(k)$, page-local | dissipation spectrum $\propto k^2E(k)$ |
| $S_\epsilon$ | page-local | dissipation skewness, the negative of the velocity-gradient skewness |
| $f_\epsilon$, $f_\Omega$, $a$, $b$ | $f_\varepsilon$, $f_{\omega^2}$, page-local | PDF tails, Eqs. (4.1)–(4.2) |
| $n$ | page-local | chi-square order and moment order (two meanings in the source) |
| $M$, $T_1$, $T_2$, $T_3$ | page-local | number of segments, phase durations |

# Reference list

27 printed references in JFM author–year style; merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. The cited companion
paper, Yeung, Ravikumar, Nichols & Uma-Vaideswaran (2025, Comput. Phys. Commun.
306:109364), is a different work whose rule key equals this slug, and Kim &
Leonard (2024, Annu. Rev. Fluid Mech. 56:21–44) is a different work from the
ingested `kim-2024`; they are keyed `yeung-2025-b` and `kim-2024-b`. Same-key pairs in printed
order: Donzis & Sreenivasan (2010) and Donzis & Yeung (2010); Okamoto et al.
(2025a/b). Karp et al. (2025) and Okamoto et al. (2025b) are printed as under
review and are preprint entries. Only one DOI is printed (Ravikumar, Appelhans &
Yeung 2019). The "Srenivasan" misspelling of Yeung, Donzis & Sreenivasan (2012)
is recorded as printed.

# Pages created or updated

Chunk 6 (2026-10-26). This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Bottleneck effect in the energy spectrum](/definitions/bottleneck-effect.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Multi-resolution independent simulations](/methods/multi-resolution-independent-simulations.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
