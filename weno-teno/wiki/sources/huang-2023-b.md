---
type: Source
title: "Huang et al. (2023) — A Five-Point TENO Scheme with Adaptive Dissipation Based on a New Scale Sensor"
description: "Replaces the discontinuity sensor that drives the adaptive cut-off of the five-point TENO5-A scheme by a five-point scale sensor that, with exact derivatives, returns the reduced wavenumber of a sinusoid at every point, critical points included, and maps it through a tanh to the cut-off threshold; tested numerically against WENO5-Z, TENO5 and TENO5-A."
resource: "doi:10.4208/cicp.oa-2022-0286"
source_kind: paper
authors: [Huang H., Liang T., Fu L.]
year: 2023
venue: "Commun. Comput. Phys. 33:1106-1131"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Communications_in_Computational_Physics_Huang_A_Five-Point_TENO_Scheme_with_Adaptive_Dissipation_Based_on.pdf"
tags: [teno, low-dissipation, finite-difference, troubled-cell, spectral-analysis]
timestamp: 2026-10-23T10:00:00Z
---

# Summary

The paper modifies the five-point [adaptive TENO](/methods/adaptive-teno.md)
scheme TENO5-A of Fu, Hu and Adams (2019), in which the cut-off $C_T$ of the
[TENO](/methods/targeted-eno.md) stencil selection varies locally between
$10^{-10}$ and $10^{-5}$, driven by Ren et al.'s (2003) discontinuity sensor
$\mu_d$ ([troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)).
The authors argue that $\mu_d$ locates discontinuities only roughly and does not
measure the local wavenumber: on a smooth sine it takes different values at
critical points than elsewhere at the same wavenumber.

They propose a five-point [scale sensor](/definitions/scale-sensor.md)
$\vartheta_{\mathrm{ESW}}$, adapted from the six-point sensor of Li, Chen and Ren (2022)
and Sun et al. It is the square root of the ratio of the third- and fourth-order
undivided Taylor variations to the first- and second-order ones, all estimated at
$x_i$ by five-point central differences. For $A\sin(k_wx+\varphi)$ with exact
derivatives the ratio is $\vartheta^2$, so $\vartheta_{\mathrm{ESW}}=\vartheta$ at every
point; at a discontinuity it is large. The sensor is mapped by
$\tanh(1.01\vartheta_{\mathrm{ESW}})$ to $C_T=10^{-\lfloor b\rfloor}$, $b=10-5\tanh(1.01\vartheta_{\mathrm{ESW}})$.
The rest of TENO5-A is kept: a sixth-order global
[smoothness indicator](/definitions/smoothness-indicator.md) $\tau_5$, $C=1$,
$q=6$ and spectrally optimized linear weights that make the background linear
scheme third order.

The evidence is numerical only. [Approximate dispersion relation](/definitions/approximate-dispersion-relation.md)
plots show lower dispersion and dissipation than TENO5
([numerical dissipation](/definitions/numerical-dissipation.md)). The
[conservative finite-difference](/definitions/conservative-finite-difference-scheme.md)
scheme uses [Rusanov flux splitting](/methods/lax-friedrichs-flux.md), Roe-averaged
[characteristic decomposition](/methods/characteristic-decomposition.md) and
[SSP-RK3](/methods/ssp-runge-kutta.md). Against [WENO5-Z](/methods/weno-z.md),
TENO5 and TENO5-A, the new scheme removes TENO5-A's long-time oscillations in
multi-wave advection, is quieter behind the incident shock of the
[double Mach reflection](/benchmarks/double-mach-reflection.md), and resolves the
most small-scale structure in the [Sod and Lax](/benchmarks/sod-and-lax-shock-tubes.md),
[Woodward–Colella](/benchmarks/woodward-colella-blast-wave.md),
[Shu–Osher](/benchmarks/shu-osher-problem.md) and
[Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md) tests, at the cost
of TENO5-A. The Rayleigh–Taylor asymmetry of the low-dissipation schemes is
attributed to round-off ([symmetry preservation](/properties/symmetry-preservation.md)).

# Version read

arXiv:2303.10020v1 [physics.flu-dyn], 17 Mar 2023 (footer "Preprint submitted to
XXX, March 20, 2023"), not the CiCP version of record; 40 pages, all read, with
pp. 8, 15, 17 and 29 checked on the page images. Page 1 matches Crossref (title,
authors; the first two authors contributed equally). Volume, pages and DOI come
from Crossref and are not printed in the file. Section, equation, table and figure
numbers are those of the arXiv v1.

# Key claims

Registry notation (see the notation map): the source's $w_k$ is $\omega_k$, its
$\varepsilon$ is $\epsilon$; Ren's sensor $m$, $\eta_i$, $\xi$ and the TENO5-A
mapping $g(m)$, $\alpha_{1,2}$, $\beta$ are $\mu_d$, $\sigma_i$, $\xi_{\mathrm A}$,
$\varphi(\mu_d)$, $b_{1,2}$, $b$ as on [adaptive TENO](/methods/adaptive-teno.md);
$K_{\mathrm{SW}}=\omega\Delta x$ is $\vartheta$. Stencils are numbered as in the
source: $S_0$ central, $S_1$ downwind, $S_2$ upwind.

1. TENO5-A's discontinuity sensor "can roughly locate the discontinuities, but is incapable of estimating the specific wavenumber": on test functions its value at critical points differs from that at other points of the same wavenumber, and in one case its value at the discontinuity is smaller than at some critical points (§3.1, Fig. 2). **Shown**
2. For $f=A\sin(k_wx+\varphi)$, $\sqrt{\lvert\mathsf D_3\rvert/\lvert\mathsf D_1\rvert}=\sqrt{\lvert\mathsf D_4\rvert/\lvert\mathsf D_2\rvert}=\vartheta$, with $\mathsf D_p=f^{(p)}\Delta x^p$ the undivided variation of order $p$ (§3.1, Eqs. 22–28). **Derived**
3. Each ratio alone is singular near critical or inflection points; the combination $\vartheta_{\mathrm{ESW}}=\sqrt{(\lvert\mathsf D_3\rvert+\lvert\mathsf D_4\rvert)/(\lvert\mathsf D_1\rvert+\lvert\mathsf D_2\rvert+\varepsilon_{\mathrm s})}$ removes this (§3.1, Eq. 29). **Derived** *(compiler check, not in the sources: with exact derivatives of the sinusoid the numerator is $\vartheta^2$ times the denominator at every point, so the combination equals $\vartheta$ everywhere when $\varepsilon_{\mathrm s}=0$; the paper does not analyse the error of the finite-difference estimates of Eq. 31.)*
4. Results are "not sensitive to the choice of $\varepsilon_1$ as long as it is a small value"; $\varepsilon_{\mathrm s}=10^{-12}$ (§3.1). **Stated** (no sensitivity study)
5. A five-point stencil has too few points to evaluate the sensor at $x_{i+1/2}$ as the six-point sensor does, so it is evaluated at $x_i$; the two are "almost identical" (§3.1). **Stated**
6. The five-point sensor estimates the local wavenumber accurately on four test functions (a sine; two sines with a jump; a zero/damped sine; a chirp), critical points included, and its value at discontinuities differs markedly from smooth regions (§3.1, Fig. 2). **Shown**
7. The tanh mapping is chosen for "its rigorous boundedness and good smoothness": $C_T=10^{-\lfloor b\rfloor}$, $b=b_1-b_2\tanh(1.01\vartheta_{\mathrm{ESW}})$, $b_1=10$, $b_2=5$ (§3.2, Eq. 33). **Stated** (design) *(compiler check, not in the sources: $\tanh\in[0,1)$ gives $b\in(5,10]$, so $C_T\in\{10^{-10},\dots,10^{-5}\}$, the same extremes as TENO5-A; the new map increases with the sensor while TENO5-A's $\varphi(\mu_d)$ enters as $1-\varphi$.)*
8. The new scheme deploys low dissipation at low wavenumbers, comparatively high dissipation at high wavenumbers and adequate dissipation at discontinuities (§1). **Stated**
9. Both dispersion and dissipation of the new scheme are better than TENO5's (approximate dispersion relation), and the optimal background linear scheme "can be restored exactly up to an intermediate wavenumber" (§3.2, Fig. 3). **Shown**
10. With the optimized weights $d_0=0.5065006634$, $d_1=0.3699651429$, $d_2=0.1235341937$ the background linear scheme is third order; TENO5-A and the new scheme both converge at third order for $\partial_tu+\partial_xu=0$, $u_0=\sin(\pi x)$, with errors identical to three digits (640 points: $L_1=7.37\times10^{-8}$, $L_\infty=1.16\times10^{-7}$) (§4.1, Table 2). **Shown**
11. On smooth data both TENO5-A and the new scheme restore the background linear scheme exactly, so they "have the same performance in this case" (§4.1). **Shown**
12. Multi-wave advection, 200 points, $t=2$: TENO5-A and the new scheme are indistinguishable and capture the Gaussian and the triangle more sharply than WENO5-Z and TENO5 (§4.2, Fig. 4). **Shown**
13. Multi-wave advection, $t=18$: TENO5-A shows "obvious oscillations even in the smooth regions"; the new scheme keeps the overall shape and captures the square wave sharply (§4.2, Fig. 5). **Shown**
14. Sod and Lax (100 points): all four schemes capture the discontinuities without spurious oscillations (§4.3, Fig. 6). **Shown**
15. Interacting blast waves (400 points, Roe flux with entropy fix, CFL 0.35): near the density peak at $x=0.78$ TENO5-A and the new scheme do better than WENO5-Z and TENO5 (§4.4, Fig. 7). **Shown**
16. Shu–Osher (200 points, $t=1.8$): TENO5-A and the new scheme resolve the high-wavenumber waves better than WENO5-Z and TENO5; TENO5-A overshoots slightly near $x=3.25$; the new scheme best preserves the velocity amplitude on $x\in[4.3,5.6]$ (§4.5, Fig. 8). **Shown**
17. Double Mach reflection (1024×256, $t=0.2$): the new scheme produces much less noise than TENO5-A behind the incident shock and the richest small-scale structure in $[2,3]\times[0,0.9]$; TENO5 beats WENO5-Z, both too dissipative (§4.6, Figs. 9–10). **Shown**
18. Cost at 512×128 (Table 3, seconds): WENO5-Z 54.99, TENO5 55.10, TENO5-A 78.47, new scheme 80.41, "approximately the same for TENO5-A and the present scheme"; hardware, compiler and step count are not stated (§4.6). **Shown**
19. Rayleigh–Taylor (96×384, $t=1.95$, Roe flux): the new scheme resolves much richer vortical structure; the loss of symmetry of TENO5, TENO5-A and the new scheme is attributed to low dissipation failing to damp round-off disturbances (§4.7, Fig. 11). **Shown** (the attribution **Stated**)
20. The scheme uses the WENO5-JS stencil and is easy to implement; it has "much lower dissipation than the existing five-point shock-capturing schemes" (§5). **Stated** (only WENO5-Z, TENO5 and TENO5-A are compared)
21. TENO restores the background linear scheme exactly in smooth regions, but standard TENO cannot adapt its dissipation between high-wavenumber flow and discontinuities (§1). **Stated**
22. The six-point scale sensors of Su et al. and Sun et al. cannot be applied directly to a five-point scheme because of the limited stencil (§1). **Stated**

Background recalled from earlier TENO papers (§2–§3): general $K$-point TENO with
incremental widths, $\gamma_k=\big(C+\tau_K/(\beta_k+\epsilon)\big)^q$ with $C=1$,
$q=6$, $\epsilon=10^{-40}$; Table 1's formal-order linear weights for $K=3,\dots,8$
(e.g. $K=5$: $d=(6,3,1)/10$); standard TENO5 with $\tau_5=\lvert\beta_1-\beta_2\rvert$
(the two outer stencils, the pair of the registry's $\tau_5=\lvert\beta_0-\beta_2\rvert$
in Jiang–Shu numbering) and $C_T=10^{-5}$ "by spectral analysis"; the sixth-order
$\tau_5$ of TENO5-A (Eq. 32); Ren's sensor printed with a three-point minimum
$\sigma_{i+1/2}=\min(\sigma_{i-1},\sigma_i,\sigma_{i+1})$, $C_r=0.24$,
$\xi_{\mathrm A}=10^{-3}$ (Eq. 19). *(compiler check, not in the sources: Table 1's
rows sum to 1; the TENO5 candidates with $d=(6,3,1)/10$ combine to the fifth-order
upwind flux $\frac1{60}(2f_{i-2}-13f_{i-1}+47f_i+27f_{i+1}-3f_{i+2})$; the quadratic
form of Eq. 32 vanishes on samples of polynomials of degree $\le2$.)*

# Printed slips

- Eq. (20): the second line defines "$\beta=\alpha_1-\alpha_2(1-g(m))$", the third uses "$C_T=10^{-\lfloor\bar\beta\rfloor}$"; Eq. (33) uses $\bar\beta$ throughout. $\beta$ is also the Jiang–Shu indicator and the Gaussian width of Eq. (39).
- Ref. [25] is printed "Computer Physics Communications 26 (4) (2019) 973–1007"; ref. [26] in the same journal and year carries volume 244, and the pattern "26 (4) (2019) 973–1007" fits Communications in Computational Physics (cf. ref. [30], "26 (2) (2019) 311–345"). The bibliography records the work as `fu-2019-b`, Commun. Comput. Phys. 26:973–1007 (doi:10.4208/cicp.oa-2018-0176), so the printed journal name is a slip.
- §4.4 credits "Woodward and Colella [59]", but ref. [59] prints only "P. Woodward".
- §4.1: the final time of the accuracy test is not printed.
- Typos: "gird resolution" (§4.7); "to access the performance" (§4); "This result of this case" (§4.6).

# Notation map

| Huang et al. (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u$, $f(u)$, $h(x)$ | $u$, $f(u)$, kept | Shu–Osher implicit function of finite-difference flux reconstruction |
| $K$, $r_k$, $S_k$ | $K$, $r_k$, $S_k$ | agrees; **TENO5 numbering $S_0$ central, $S_1$ downwind, $S_2$ upwind**, not the registry's $S_0$ most upwind |
| $\hat f_{k,i+1/2}$ | $\hat f^{(k)}_{i+1/2}$ | candidate flux |
| $\beta_{k,r_k}$, $\beta_k$ | $\beta_k$ | Jiang–Shu indicator |
| $\tau_5$, $\tau_K$ | $\tau_5$, $\tau_K$ | TENO5 $\lvert\beta_1-\beta_2\rvert$ (outer pair); sixth-order form in Eq. 32 |
| $\gamma_k$, $C$, $q$, $\chi_k$, $\delta_k$, $C_T$ | same | agrees |
| $\varepsilon$ (Eq. 9) | $\epsilon$ | $10^{-40}$; **the same letter is Ren's regularization in Eq. 19** |
| $d_k$ | $d_k$ | linear weights |
| $w_k$ | $\omega_k$ | nonlinear weights |
| $m$, $\eta_i$, $\eta_{i+1/2}$, $C_r$, $\xi$ | $\mu_d$, $\sigma_i$, $\sigma_{i+1/2}$, $C_r$, $\xi_{\mathrm A}$ | as on [adaptive TENO](/methods/adaptive-teno.md); **$\eta$ is the entropy in the registry** |
| $g(m)$, $\alpha_1$, $\alpha_2$, $\beta$/$\bar\beta$ | $\varphi(\mu_d)$, $b_1$, $b_2$, $b$ | **$g$ collides with the mapped-WENO function, $\alpha_{1,2}$ with $\alpha_k$, $\beta$ with $\beta_k$** |
| $g(K_{ESW})$ | $\tanh(1.01\vartheta_{\mathrm{ESW}})$ | written out |
| $K_{SW}=\omega\Delta x$ | $\vartheta=k_w\Delta x$ | reduced wavenumber; **$\omega$ is a nonlinear weight in the registry** |
| $K_{ESW}$, $\varepsilon_1$ | $\vartheta_{\mathrm{ESW}}$, $\varepsilon_{\mathrm s}$ (page-local, as on [scale sensors](/definitions/scale-sensor.md)) | estimated reduced wavenumber (scale sensor) and its regularization |
| $\Delta f_p$, $\Delta f_{p,i}$ | $\mathsf D_p$ (page-local, as on [scale sensors](/definitions/scale-sensor.md)) | undivided variation $f^{(p)}\Delta x^p$ and its five-point estimate (Eq. 31) |
| $L(\cdot)$ | $\mathcal L$ | semi-discrete operator |
| $p$ (§4.1) | kept | design order in $\Delta t=\Delta x^{p/3}$; not the pressure |
| $\alpha$, $\beta$, $z$, $a$, $\theta$ (Eqs. 38–40) | kept | parameters of the multi-wave initial data |

# Reference list

63 printed references in numbered style ([1]–[63]), all parsed and merged complete
into the [bibliography](/bibliography.md) with `citedby` `huang-2023-b`. Two are
book chapters ([1], [60]); [32] is an arXiv preprint (2021), kept as its own entry;
[25] is identified with `fu-2019-b` (Commun. Comput. Phys.) despite the printed journal name; [34], [52] and
[55] print no volume, [49] no pages; only [52] prints a DOI. Five Fu (2019) papers
and two Tsoutsanis (2021) papers are matched by venue to the bundle's suffixed keys. No printed
duplicates were found.

# Pages created or updated

Chunk 4 (2026-10-22), cited further in chunks 5–10 (2026-10-22/23). This source is cited on:

* [Adaptive TENO (TENO-A, TENO-AA)](/methods/adaptive-teno.md)
* [Approximate dispersion relation](/definitions/approximate-dispersion-relation.md)
* [Characteristic decomposition](/methods/characteristic-decomposition.md)
* [Conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
* [Double Mach reflection](/benchmarks/double-mach-reflection.md)
* [Jiang–Shu composite-wave advection](/benchmarks/jiang-shu-composite-advection.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [Numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
* [Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md)
* [Roe approximate Riemann solver](/methods/roe-riemann-solver.md)
* [Scale sensors and the effective scaled wavenumber](/definitions/scale-sensor.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Symmetry preservation](/properties/symmetry-preservation.md)
* [Targeted ENO (TENO)](/methods/targeted-eno.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
* [WENO-Z weights](/methods/weno-z.md)
* [Woodward–Colella interacting blast waves](/benchmarks/woodward-colella-blast-wave.md)
