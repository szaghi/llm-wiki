---
type: Source
title: "Wang et al. (2024b) — Assessment of high-order interpolation-based weighted essentially non-oscillatory schemes for compressible Taylor–Green vortex flows"
description: "Compares reconstruction-based and interpolation-based fifth-order finite-difference WENO schemes (WENO-JS, US-WENO, AUS-WENO) on the compressible Taylor–Green vortex up to M = 2.5, and introduces HAUS-WENO, a hybrid with an extremum-property sensor, stated to be free of empirical parameters, that cuts the runtime to 74% of WENO-JS while dissipating least."
resource: "doi:10.1063/5.0236997"
source_kind: paper
authors: [Wang Z., Zhu J., Tian L., Zhao N.]
year: 2024
venue: "Phys. Fluids 36:116119"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2024_Crossref_Physics_of_Fluids_Wang_Assessment_of_high-order_interpolation-based_weighted_essent.pdf"
tags: [weno, shock-capturing, numerical-dissipation, compressible, taylor-green-vortex]
timestamp: 2026-10-28T16:59:00Z
---

# Summary

Wang et al. (2024b) ask whether the choice between reconstruction-based
(flux-splitting) and interpolation-based ("alternative", Riemann-solver)
finite-difference [WENO](/methods/weno-scheme.md) matters for the
compressible [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md),
whose supersonic assessment by Lusher & Sandham (2021, ref. 19) had, in
the authors' account, considered reconstruction-based WENO only
([Chapelier et al. (2024)](/sources/chapelier-2024.md), ref. 7, is cited
for the kinetic-energy rise at high Mach number). Four fifth-order schemes are compared:
WENO-JS; the unequal-sized WENO (US-WENO) of Zhu & Qiu, which blends one
quartic and two linear candidates with arbitrary positive linear weights;
its interpolation-based form AUS-WENO, which interpolates point values to
the face, applies the HLL flux and adds fourth- and sixth-order derivative
corrections; and the new hybrid HAUS-WENO. The contribution is the
"extremum-property" [shock sensor](/definitions/shock-sensor.md) of
HAUS-WENO: termwise bounds of the derivative of the quartic interpolant on
the two half-intervals around $x_i$ must keep one sign, and then the
linear fifth-order interpolation replaces the nonlinear weights and the
characteristic decomposition; the density is sensed.

Smooth three-dimensional Euler and Navier–Stokes tests confirm fifth order
for all four schemes. On the inviscid vortex at $M_{\mathrm{ref}}=0.1$, the
viscous vortex at $Re=1600$ for $M_{\mathrm{ref}}=0.1$–$1.25$ and at $Re=400$
for $M_{\mathrm{ref}}=2.0$ and $2.5$, all on $128^3$ grids against
sixth-order TENO and fourth-order subcell finite-volume references, WENO-JS
is the most dissipative, the interpolation-based schemes are less
dissipative than US-WENO and HAUS-WENO is closest to the references. The
solenoidal and dilatational dissipation rates separate the schemes more
than the kinetic energy does, which ties the study to
[numerical dissipation](/properties/numerical-dissipation.md); the
kinetic-energy rise at high Mach number is attributed to the mean pressure
work ([pressure dilatation](/definitions/pressure-dilatation.md)). On one
core HAUS-WENO runs in 74% of the WENO-JS time. No subgrid model is used;
the paper does not call its runs implicit LES. Evidence is numerical
comparison with published reference solutions.

# Version read

Version of record (AIP; submitted 2 September 2024, accepted 15 October
2024, online 7 November 2024), 22 PDF pages (an AIP cover page and article
pages 116119-1 to -21), all read; the equation pages 116119-3 to -6 and
-10 were checked visually. Page 1 matches the metadata. Equation, table,
figure and section numbers are those of this version.

# Key claims

Page-local symbols: $p_n$, $q_n$ ($n=1,2,3$) the reconstruction
(cell-average) and interpolation (point-value) polynomials, $q_1$ quartic;
$c_\ell$, $\varphi_\ell=((x-x_i)/h)^\ell$ the coefficients and monomial
basis of $q_1$ (the source's $a_\ell$); $\mathrm{MAX}1$, $\mathrm{MIN}1$,
$\mathrm{MAX}2$, $\mathrm{MIN}2$ the termwise bounds of the sensor;
$\tau_{\mathrm U}$ the global smoothness indicator; $E_k$ the volume-averaged
kinetic energy; $\varepsilon_{\mathrm{tot}}=\varepsilon_s+\varepsilon_d$ the
total viscous dissipation.

1. Only finite-difference reconstruction-based WENO schemes had been used to study the supersonic TGV problem before this paper; interpolation-based counterparts "have not been seen yet" (§I, p. 2). **Stated**
2. The interpolation-based WENO scheme can be paired with any approximate Riemann solver, giving smaller numerical dissipation, and per refs. 15, 21, 22 has better free-stream-preserving features (§I; §II.C). **Stated**
3. The US-WENO linear weights "cannot be unique" (any positive set summing to one), making it easier to generalise to unstructured grids and giving better steady-state convergence (refs. 50, 51, 53, 54) (§II.B). **Stated**
4. Per ref. 38, among Riemann solvers in AUS-WENO, LF is most stable but most dissipative, HLLC least dissipative but least stable, HLL balances both; HLL is used here (§II.C, after Eq. 16). **Stated**
5. The extremum-property (EP) sensor detects troubled cells from the sign of termwise maximum and minimum bounds of the derivative of the quartic interpolation polynomial over $[x_{i-3/2},x_i]$ and $[x_i,x_{i+3/2}]$, without finding the roots of $q_1'(x)$ explicitly (§II.D, Eqs. 21–23). **Derived** (contribution)
6. The EP sensor "does not contain empirical parameters" and is robust for supersonic TGV flows (Abstract; §I). **Stated**
7. All four schemes reach fifth order on the 3D Euler smooth test ($T=2$, grids $20^3$–$100^3$); US-WENO has smaller errors than WENO-JS on the same grid, and AUS- and HAUS-WENO slightly smaller than US-WENO ($L^1$ at $100^3$: WENO-JS $8.30\times10^{-8}$, US-WENO $1.21\times10^{-8}$, AUS-WENO $1.04\times10^{-8}$, HAUS-WENO $1.04\times10^{-8}$) (Table I). **Shown**
8. On the 3D Navier–Stokes smooth test ($Re=1000$, $80^3$), $L^1$ errors: WENO-JS $2.55\times10^{-5}$, US-WENO $3.63\times10^{-6}$, AUS-WENO $3.08\times10^{-6}$, HAUS-WENO $3.08\times10^{-6}$; orders approach 5 (WENO-JS only 2.65 and 4.17 on the coarser pairs) (Table II). **Shown**
9. In error against CPU time (Figs. 1–2), US-WENO and WENO-JS have similar times, AUS-WENO is slightly slower, HAUS-WENO is the most efficient (it avoids characteristic decomposition and nonlinear weights) (§III.A). **Shown**
10. Inviscid TGV, $M_{\mathrm{ref}}=0.1$, $128^3$: the exact kinetic energy stays $E_k=0.125$; WENO-JS dissipates fastest, US-WENO less, the interpolation-based US-WENO is closer to the theoretical value, HAUS-WENO best "because it uses a linear method with less dissipation in some areas" (§III.B, Fig. 3a). **Shown**
11. The inviscid TGV enstrophy agrees with the Brachet et al. (ref. 4) solutions before $t\approx4$ (Fig. 3b); Q-criterion iso-surfaces at $t=10$ show that WENO-JS loses small structures and that the two interpolation-based schemes are slightly better than the reconstruction-based US-WENO (Fig. 4). **Shown**
12. Grid sensitivity of HAUS-WENO at $M_{\mathrm{ref}}=1.25$, $Re=1600$: the solution "gradually converge[s]" to the sixth-order TENO $512^3$ reference of ref. 19 (Fig. 5). **Shown**
13. The kinetic energy decays monotonically at $M_{\mathrm{ref}}=0.1$, 0.25, 0.5; at higher Mach number there is an interval of increasing kinetic energy, consistent with refs. 7, 19, 23, attributed to the mean pressure work exceeding the viscous dissipation rate and converting internal into kinetic energy early on; strongest at $M_{\mathrm{ref}}=1.25$ (§III.C, Fig. 6). **Shown** (mechanism **Stated**)
14. WENO-JS is the most dissipative at every Mach number; at $M_{\mathrm{ref}}=0.1$, 0.25, 0.5 HAUS-WENO is closest to the reference in kinetic energy, while at higher Mach number all US-WENO variants perform similarly in kinetic energy (§III.C, Fig. 6). **Shown**
15. The total dissipation rate $\varepsilon_{\mathrm{tot}}$ discriminates the schemes more than the kinetic energy; HAUS-WENO is best; the dissipation peak is delayed and lowered as the Mach number increases; a double peak appears at $M_{\mathrm{ref}}=0.75$, 1.0, 1.25 (as reported in ref. 19); after $t=12$ the dissipation drops fast for $M_{\mathrm{ref}}\le0.5$ and stays flatter at higher Mach number (§III.C, Fig. 7). **Shown**
16. At $M_{\mathrm{ref}}=1.25$ shocklets produce an additional dissipation peak for $2<t<4$ which none of the schemes captures at $128^3$, attributed to insufficient grid points as explained in ref. 19 (§III.C). **Stated** (absence **Shown**)
17. The dilatational dissipation $\varepsilon_d$ is much smaller than the solenoidal $\varepsilon_s$ and shows two distinct early peaks at $M_{\mathrm{ref}}=1.0$ and 1.25, due to early shocklets; HAUS-WENO is closest to the reference, especially in $\varepsilon_s$ (§III.C, Figs. 8–9). **Shown**
18. At $M_{\mathrm{ref}}=1.25$ on $256^3$, the HAUS-WENO density gradient shows eight shock waves at $t=2$ from the initial symmetry, slender reflected structures at $t=7$, a subsonic state with propagating shocklets and four counter-rotating flows at $t=15$, and chaotic flow at $t=20$ with the symmetry still preserved (Fig. 12). **Shown**
19. At $Re=400$, $M_{\mathrm{ref}}=2.0$, 2.5, the differences between schemes in kinetic energy are less obvious (all US-WENO variants slightly better than WENO-JS); the interpretation is that at $Re=1600$ numerical viscosity dominates physical viscosity while at $Re=400$ they are comparable (§III.D, Fig. 13). **Shown** (interpretation **Stated**)
20. At $M_{\mathrm{ref}}=2.0$, 2.5, $\varepsilon_d$, $\varepsilon_s$ and $\varepsilon_{\mathrm{tot}}$ discriminate the schemes more; AUS-WENO and HAUS-WENO are closer to the reference than US-WENO and WENO-JS; numerical dissipation matters more in later stages (Figs. 18–19). The velocity-divergence shocklet structures of US-, AUS- and HAUS-WENO are similar and slightly sharper than those of WENO-JS (Figs. 16–17). **Shown**
21. Runtime, $M_{\mathrm{ref}}=1.25$, $Re=1600$, $128^3$, one core of a 64 GB E5-2640V4 CPU: total runtime WENO-JS 41 542.4 s (1.00), US-WENO 42 781.6 s (1.03), AUS-WENO 46 959.5 s (1.13), HAUS-WENO 30 046.8 s (0.74); single step 17.31, 17.38, 19.05, 12.09 s (ratios 1.00, 1.00, 1.10, 0.70) (Table III). **Shown**
22. HAUS-WENO's runtime is "only 74%" of WENO-JS ("efficiency is improved by nearly 30%") and its efficiency is increased by 35% relative to AUS-WENO; the AUS-WENO overhead (13%) is due to computing the high-order derivative terms (§III.E) *(compiler check, not in the sources: $1-30\,046.8/46\,959.5=0.36$)*. **Shown**
23. Conclusion: reconstruction-based US-WENO generates more small-scale dissipation; interpolation-based US-WENO captures more small-scale structures; the differences grow with the Reynolds number (§IV). **Shown**

The schemes in registry notation (§II.B–§II.D). US-WENO splits the flux
with global Lax–Friedrichs, $f^\pm(U_i)=\tfrac12[f(U_i)\pm\alpha_{\mathrm{LF}}U_i]$
(the source's $\alpha$, the global maximum wave speed, page-local), and
reconstructs $\hat f^+_{i+1/2}$ from $p_1$ on $\{I_{i-2},\dots,I_{i+2}\}$ and
$p_2$, $p_3$ on $\{I_{i-1},I_i\}$, $\{I_i,I_{i+1}\}$. With Jiang–Shu
indicators $\mathrm{IS}_n=\sum_{\alpha=1}^{r}\int_{I_i}h^{2\alpha-1}(\mathrm d^\alpha p_n/\mathrm dx^\alpha)^2\mathrm dx$
($r=4$ for $p_1$, 1 for $p_2$, $p_3$), the weights are

$$\tau_{\mathrm U}=\Big(\frac{\lvert\mathrm{IS}_1-\mathrm{IS}_2\rvert+\lvert\mathrm{IS}_1-\mathrm{IS}_3\rvert}{2}\Big)^2,\qquad a_n=d_n\Big(1+\frac{\tau_{\mathrm U}}{\epsilon_{\mathrm Z}+\mathrm{IS}_n}\Big),\qquad \mathsf w_n=\frac{a_n}{\sum_\ell a_\ell},$$

$\epsilon_{\mathrm Z}=10^{-6}$, $(d_1,d_2,d_3)=(0.98,0.01,0.01)$, and
$\hat f^+_{i+1/2}=\mathsf w_1\big(p_1/d_1-(d_2/d_1)p_2-(d_3/d_1)p_3\big)+\mathsf w_2p_2+\mathsf w_3p_3$
at $x_{i+1/2}$ (Eqs. 6–12). AUS-WENO forms the same combination of the
interpolants $q_n$ to get $u^{L}_{i+1/2}$, $u^R_{i+1/2}$, evaluates the HLL
flux $f^*_{i+1/2}$ and corrects it,
$\hat f_{i+1/2}=f^*_{i+1/2}-\tfrac1{24}h^2\partial_x^2f+\tfrac{7}{5760}h^4\partial_x^4f$
at $x_{i+1/2}$, with six-point central differences of $O(h^6)$ (Eqs. 13–20);
both work in local characteristic variables. HAUS-WENO writes
$q_1'\propto4c_4\varphi_3+3c_3\varphi_2+2c_2\varphi_1+c_1\varphi_0$, sums the
termwise maxima and minima at the end points of each half-interval into
$\mathrm{MAX}1$, $\mathrm{MIN}1$ (left) and $\mathrm{MAX}2$, $\mathrm{MIN}2$
(right), and declares the point smooth when
$(\mathrm{MAX}1\pm h)(\mathrm{MIN}1\pm h)>0$ and
$(\mathrm{MAX}2\pm h)(\mathrm{MIN}2\pm h)>0$ (the "$\pm h$" is printed without
further explanation); there $u^L_{i+1/2}=q_1(x_{i+1/2})$ (Eqs. 21–23).
Time integration is third-order TVD Runge–Kutta at CFL 0.6; the viscous
terms use central differences of the corresponding accuracy. The vortex is
initialized by Eq. (25) on $[0,2\pi]^3$ with a density perturbation of
amplitude $\gamma M_{\mathrm{ref}}^2$ (inviscid and $Re=1600$) or 1
($Re=400$), and $p=\rho T/(\gamma M_{\mathrm{ref}}^2)$.

# Printed slips

- **Eq. (18), linear term of $q_1$:** printed $q_1(x)=u_i-\frac{u_{i-2}-8u_{i-1}+8u_{i+1}-u_{i+2}}{12}\frac{x-x_i}{h}+\dots$. *(Compiler check, not in the sources: for $u_j=j$, $h=1$, $x_i=0$ the numerator is 12, so the printed term has slope $-1$, while the interpolation conditions of Eq. (17) for $u=x$ require slope $+1$.)*
- **Eq. (28):** the derivatives are printed $\partial u_k/\partial u_j$ and $\partial u_j/\partial u_j$, and the prefactors $\frac1{\rho_{ref}Re}$, $\frac4{3\rho_{ref}Re}$ lack the $\lvert V\rvert$ that the text defines immediately after and that Eqs. (26)–(27) carry.
- **Table III:** the total-runtime ratio of HAUS-WENO is printed 0.74, and the text repeats "only 74%". *(Compiler check, not in the sources: $30\,046.8/41\,542.4=0.723$; the other ratios, 1.03, 1.13 and 1.00, 1.10, 0.70 per step, agree.)*
- **Table I:** the HAUS-WENO $L^\infty$ order from $20^3$ to $40^3$ is printed 4.99. *(Compiler check, not in the sources: $\log_2(5.46\times10^{-5}/1.77\times10^{-6})=4.95$.)*
- **Accuracy test (§III.A):** "$\mu=0.0005$, $Pr=2/3$, $\gamma=1.4$, $Re=1000$" are printed together, while Eq. (3) states Sutherland's law; how $\mu$ and $1/Re$ relate is not stated.
- **Notation:** the headings of §III.C and §III.D print $M_{ref}$, the text $Ma_{ref}$; the legends of Fig. 1 include a "Linear" scheme not described in the text.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $Ma_{ref}$ ($M_{ref}$) | $M_{\mathrm{ref}}$ | reference Mach number of the vortex |
| $\tau_{ij}$ (Eq. 3) | $\sigma_{ij}$ | viscous stress, Stokes hypothesis; **collision** with the SGS stress $\tau_{ij}$ |
| $\gamma_n$ | $d_n$ | linear weights; **collision** with $\gamma$, the ratio of specific heats (1.4) |
| $\beta_n$ | $\mathrm{IS}_n$ | Jiang–Shu smoothness indicators |
| $\bar\omega_n$, $\omega_n$ | $a_n$, $\mathsf w_n$ | **collision** with the vorticity $\omega_j$ |
| $\tau$ (Eq. 11) | $\tau_{\mathrm U}$ (page-local) | global smoothness indicator |
| $\varepsilon=10^{-6}$ (Eq. 11) | $\epsilon_{\mathrm Z}$ | **collision** with the dissipation rates |
| $\alpha$ (Eq. 6) | $\alpha_{\mathrm{LF}}$ (page-local) | global maximum wave speed; **collision** with the DG blending factor $\alpha$ |
| $h(u^L,u^R)$, $f_{i+1/2}$ | $f^*_{i+1/2}$ | monotone (HLL) flux; the source's $h$ is also the grid spacing |
| $h$ | $h$ | grid spacing |
| $a_\ell$, $\varphi_\ell$ | $c_\ell$, $\varphi_\ell$ (page-local) | **collision** of $a_\ell$ with the WENO weights $a_k$ |
| $MAX1$, $MIN1$, $MAX2$, $MIN2$ | same (page-local) | EP sensor bounds |
| $E_k$ | $E_k$ | volume-averaged kinetic energy over $\rho_{ref}\lvert V\rvert$ |
| $\zeta$ | $\mathcal Z$ | density-weighted, with the factor $\tfrac12$ |
| $\varepsilon^S$, $\varepsilon^D$, $\varepsilon^T$ | $\varepsilon_s$, $\varepsilon_d$, $\varepsilon_{\mathrm{tot}}$ (page-local) | solenoidal, dilatational, total viscous dissipation |
| $Q$ (Eq. 29) | $Q_A$ | Q criterion, in the form printed in Eq. (29) |
| $C$ (Eq. 25) | (density-perturbation amplitude) | $\gamma M_{\mathrm{ref}}^2$ or 1 |
| $\sigma$ (Eq. 1) | (Euler/Navier–Stokes switch) | 0 or 1 |
| $DoV$ | $\nabla\cdot\boldsymbol u$ | velocity divergence |

# Reference list

54 printed references, numbered AIP style in alphabetical order, no DOIs
printed. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Ref. 7 is the
ingested [chapelier-2024](/sources/chapelier-2024.md). Five references
carry first-author-year keys equal to planned Source slugs but are
different works and are keyed `pereira-2021-e`, `wang-2024-m`, `wang-2023-k`, `wang-2023-l` and `xu-2023-d` respectively: ref. 24 (Pereira et al.,
Phys. Rev. Fluids 6:054611, transitional TGV with PANS), ref. 34 (Wang Y.B.
et al., Phys. Fluids 36:016137, compact gas-kinetic scheme), ref. 39 (Wang
et al., Commun. Nonlinear Sci. Numer. Simul. 126:107439), ref. 40 (Wang et
al., J. Comput. Phys. 490:112299) and ref. 43 (Xu & Chen, Phys. Fluids
35:045128). Same-author same-year works are keyed in printed order (Wang
2021, 2023; Zhu 2017, 2018). Ref. 54 (Zhang, Zhu & Shu 2019) is printed
after ref. 53, out of the alphabetical order; names are kept as printed
("Schiling, O." in ref. 33). No item is unparseable.

# Pages created or updated

Chunk 14 (2026-10-28). This source is cited on:

- [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
- [Pressure dilatation](/definitions/pressure-dilatation.md)
- [Shock sensors and troubled-cell indicators](/definitions/shock-sensor.md)
- [High-order gas-kinetic schemes for turbulence simulation](/methods/high-order-gas-kinetic-scheme.md)
- [Partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md)
- [Symbolic-regression turbulence closures](/methods/symbolic-regression-closure.md)
- [Weighted compact nonlinear schemes](/methods/weighted-compact-nonlinear-scheme.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
