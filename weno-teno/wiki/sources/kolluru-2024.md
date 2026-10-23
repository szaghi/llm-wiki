---
type: Source
title: "Kolluru et al. (2024) — Novel spectral methods for shock capturing and the removal of tygers in computational fluid dynamics"
description: "Numerical study of Besse's spectral relaxation and spectral purging schemes, which relax or reset a Galerkin-truncated Fourier or Chebyshev solution toward a kernel-mollified state; positive kernels give monotone, tyger-free shocks, compared with spectral vanishing viscosity on Burgers, shallow-water, Euler and Hou–Luo tests."
resource: "doi:10.1016/j.jcp.2024.113446"
source_kind: paper
authors: [Kolluru S.S.V., Besse N., Pandit R.]
year: 2024
venue: "J. Comput. Phys. 519:113446"
local_file: "/home/stefano/papers/mosaic/weno-teno/2024_Crossref_Journal_of_Computational_Physics_Kolluru_Novel_spectral_methods_for_shock_capturing_and_the_removal_o.pdf"
tags: [shock-capturing, artificial-viscosity, filtering, shallow-water, benchmark]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

Fourier and Chebyshev pseudospectral approximations of nonlinear conservation
laws conserve energy. At shocks they produce Gibbs oscillations. For the
2/3-dealiased Galerkin-truncated inviscid Burgers equation they also produce
**tygers**: localized oscillations born by resonance at the truncation
wavelength in smooth regions far from the shock, the precursors of
thermalization. The paper is a numerical study of two schemes proposed by Besse
(cited as submitted). The **spectral relaxation (SR)** scheme adds a BGK-type
term $\frac1{\tau_{\mathrm{SR}}}(\mathcal M_mu_N-u_N)$ to the truncated PDE,
with $\mathcal M_m=K_m*$ a convolution with a smoothing kernel. The **spectral
purging (SP)** scheme replaces $u_N$ by $K_m*u_N$ at time intervals
$\tau_{\mathrm{SR}}$. Both take $m=N_{\mathrm F}^{\gamma_{\mathrm{SR}}}$ and
$\tau_{\mathrm{SR}}=N_{\mathrm F}^{-\alpha_{\mathrm{SR}}}$. Besse's convergence
proof (not given here) covers positive kernels with
$\alpha_{\mathrm{SR}}/2<\gamma_{\mathrm{SR}}<1$ and $1<\alpha_{\mathrm{SR}}<2$.

The schemes are compared with spectral vanishing viscosity (SVV, see
[artificial viscosity](/methods/artificial-viscosity.md)) and with SR built on
other filters. Tests: periodic [Burgers](/benchmarks/burgers-equation-tests.md)
with convergence tables; the 1D [shallow-water equations](/definitions/shallow-water-equations.md)
(a water hump and a [dam break](/benchmarks/dam-break-problem.md)); 1D Euler
with a Chebyshev basis and characteristic boundary conditions on
[Sod and Lax](/benchmarks/sod-and-lax-shock-tubes.md),
[Shu–Osher](/benchmarks/shu-osher-problem.md) and the
[Woodward–Colella blast waves](/benchmarks/woodward-colella-blast-wave.md);
and the Hou–Luo wall model of axisymmetric Euler blowup.

A positive kernel (Fejér–Korovkin) gives monotone, tyger-free shocks that
respect the maximum principle. Its observed order is about
$2-\alpha_{\mathrm{SR}}$ before the shock and below 1 after it. The high-order
de La Vallée Poussin kernel converges spectrally in smooth flow but leaves
bounded oscillations at shocks, like SVV. It is needed to resolve Shu–Osher and
fails on the blast waves (negative pressure). The authors conclude that formal
order alone is a misleading design criterion at shocks. All evidence is
numerical, and the parameters are tuned by hand for each problem. The methods
are global spectral, not WENO or DG. They enter the bundle through filtering,
viscous regularization and the shared benchmarks.

# Version read

arXiv:2402.17688v2 [math.NA], stamped 28 Feb 2024 and dated "March 1, 2024"
under the affiliations: a preprint, not the version of record. It has 41 pages,
all read. Pages 1, 11, 21–22, 30 and 36–40 were also checked visually. Page 1
(title, three authors, IISc Bangalore and Observatoire de la Côte d'Azur)
matches Crossref. The arXiv copy prints no DOI. Section, equation, table and
figure numbers are those of v2.

# Key claims

Registry notation (see the notation map): Fourier truncation wavenumber
$N_{\mathrm F}$, SR/SP parameters $\alpha_{\mathrm{SR}}$, $\gamma_{\mathrm{SR}}$,
$\tau_{\mathrm{SR}}$, SVV amplitude $\epsilon_{\mathrm{SV}}$ and activation
wavenumber $M_{\mathrm{SV}}$ (all page-local), velocity $v$.

1. In SR the relaxation term $\frac1{\tau_{\mathrm{SR}}}(\mathcal M_mu_N-u_N)$ removes energy from high-wavenumber modes at an exponential rate $1/\tau_{\mathrm{SR}}$ and forces $u_N$ toward the generalized "Maxwellian" $\mathcal M_mu_N$ (§2.2, Eq. 3a). **Stated**
2. Besse proves strong $L^2$ convergence, as $N_{\mathrm F}\to\infty$, of SR and SP to the entropy solution of 1D inviscid Burgers for positive kernels (Fejér–Korovkin, Jackson, Jackson–de La Vallée Poussin). The conditions quoted are $\alpha_{\mathrm{SR}}/2<\gamma_{\mathrm{SR}}<1$, $1<\alpha_{\mathrm{SR}}<2$ (§2.2, §3.2). **Stated** (proof in the cited work)
3. Unlike SVV, the SR and SP solution operators are not monotone and do not satisfy the maximum principle as operators. These properties come from the positivity of the kernels, not from the structure of the dissipative operator (§1). **Stated**
4. $\alpha_{\mathrm{SR}}>1$ is "a sufficient condition for the aliasing error to be controlled or dominated by the dissipation induced by the relaxation term" (§3.2). **Stated**
5. SR and SP need no 2/3 dealiasing: for every test problem a suitable $(\alpha_{\mathrm{SR}},\gamma_{\mathrm{SR}})$ controls the aliasing errors (§2.2). **Shown**
6. For Burgers with $u_0=\sin2\pi x$ (IC0) at $N_x=615$, minimizing the time-integrated and maximum $L^2$ errors over $t\in[0,9.9]$ gives $(\alpha_{\mathrm{SR}},\gamma_{\mathrm{SR}})=(0.7,0.99)$ for SR-FeKo and $(0.65,0.99)$ for SP-FeKo (§3.1). **Shown**
7. SR-FeKo removes the tygers and is monotone at the shock. SP-FeKo still shows attenuated tyger-like structures at $t=0.2$, because SP is discontinuous in time (§3.1, Figs. 3, 7). **Shown**
8. SR-FeKo at $(0.7,0.99)$ without dealiasing (Table 1): at $t=0.07$ (smooth) the asymptotic order is about 1.28 in $L^1$ and 1.27 in $L^2$; after the shock it is about 0.9 in $L^1$ and 0.78 in $L^2$. At $N_x=7995$ the $L^1$ errors are $5.8\cdot10^{-6}$ ($t=0.07$), $4.6\cdot10^{-4}$ ($t=0.2$) and $6.5\cdot10^{-5}$ ($t=2$). **Shown**
9. The SR order follows from the scaling of the right-hand side, printed $\frac1{\tau_{\mathrm{SR}}}\big(\frac1m\big)^2\simeq N_{\mathrm F}^{-(2\gamma_{\mathrm{SR}}-\alpha_{\mathrm{SR}})}$, i.e. $N_{\mathrm F}^{-(2-\alpha_{\mathrm{SR}})}$ for $\gamma_{\mathrm{SR}}\simeq1$. Fig. 4 ($L^\infty$ errors at $t=0.07$) shows orders falling linearly from about 1.95 at $\alpha_{\mathrm{SR}}=0$ to about 1.05 at $\alpha_{\mathrm{SR}}=0.9$ (§3.1). **Derived** (heuristic) and **Shown**
10. After shock formation the solution is only $BV$ in $x$, so the order of convergence is bounded above by 1 (§3.1). **Stated**
11. SR-DlVP at $(0.89,0.9)$, $r=0.5$, converges spectrally before the shock (Table 2): the $L^1$ error falls from $1.2\cdot10^{-5}$ at $N_x=39$ to $2.8\cdot10^{-13}$ at $N_x=205$ (orders 6.82, 9.89, 15.28) and then saturates at round-off. After the shock the $L^1$ order is about 0.95, as for FeKo, but the $L^2$ order is about 0.5 ($t=0.2$) and 0.44 ($t=2$), against about 0.8 for FeKo. **Shown**
12. The better $L^2$ convergence of the low-order FeKo kernel at shocks is attributed to its monotonicity and maximum principle; DlVP produces bounded oscillations and over- and undershoots. "High-order approximations as the sole criterion for designing accurate numerical schemes can be misleading" (§3.1, citing LeVeque). **Shown** and interpretation
13. Among positive kernels (FeKo, Jackson, Jackson–de La Vallée Poussin) the SR and SP results differ very little; FeKo is slightly better near the shock (§3.1, Fig. 6). **Shown**
14. SVV with $\epsilon_{\mathrm{SV}}=N_{\mathrm F}^{-1}$, $M_{\mathrm{SV}}=2\sqrt{N_{\mathrm F}}$ keeps small Gibbs-like oscillations near the shock, while SR-FeKo and SP-FeKo stay monotone (§3.1, Fig. 7). **Shown**
15. SR with non-positive filters from the literature is less accurate than SR-FeKo, worsening in the order Tadmor–Tanner, Majda–McDonough–Osher, regularized Shannon kernel (§3.1, Fig. 8). **Shown**
16. The growth of aliasing errors depends on the initial condition. For IC1 $=\sin(2\pi x-\pi/2)$, plain SR-FeKo at $(0.97,0.98)$ blows up and needs $(1.18,0.99)$ (Table 3: $L^1$ orders about 0.80 at all times, $L^2$ about 0.40 after the shock). For IC0, SR-FeKo is stable for $\alpha_{\mathrm{SR}}\in[0.7,2)$ and $\gamma_{\mathrm{SR}}\in[0.9,1)$ (§3.2). **Shown**
17. 2/3 dealiasing makes the aliasing growth similar across initial conditions. It makes plain pseudospectral solutions worse for IC0 and better for IC1, and lets SR-FeKo run at lower $\alpha_{\mathrm{SR}}$: dealiased $(0.97,0.98)$ gives $L^1$ orders about 0.99 at $t=0.07$ and 0.95 at $t=2$, less diffusive and of higher order (§3.2, Table 4, Fig. 10). **Shown**
18. SVV behaves the same way: $(\epsilon_{\mathrm{SV}},M_{\mathrm{SV}})=(N_{\mathrm F}^{-1},2N_{\mathrm F}^{1/2})$ is stable for IC0 but not for IC1, which needs $(0.25N_{\mathrm F}^{-1/4},N_{\mathrm F}^{1/4})$ (§3.2, Fig. 11). **Shown**
19. Shallow water at $N_x=2665$, no dealiasing. Water hump: SR-FeKo $(0.5,0.99)$ follows the CLAWPACK reference through shock formation ($t\simeq3$); SR-DlVP $(0.8225,0.98)$ is close but oscillates boundedly at the shock. Dam break: SR-FeKo $(0.55,0.99)$ is slightly overdamped; SR-DlVP $(0.70,0.98)$ is closer but oscillatory (§3.3, Figs. 12–13). **Shown**
20. Chebyshev SR for 1D Euler with characteristic boundary conditions needs no extra boundary treatment (§3.4, §4, App. B). **Shown**
21. Sod ($N_x=615$): dealiased Chebyshev pseudospectral solutions destabilize quickly. SR-FeKo $(0.785,0.99)$ is oscillation-free but slightly overdamped; SR-DlVP $(0.94,0.95)$ is closer, with small bounded oscillations at corners. Lax: SR-FeKo $(0.91,0.99)$, SR-DlVP $(1.10,0.98)$, same pattern (§3.4, Figs. 14–15). **Shown**
22. Shu–Osher ($N_x=615$): SR-FeKo $(0.95,0.97)$ "does not converge to the correct solution" and loses the entropy-wave oscillations because the kernel is low order. SR-DlVP $(1.14,0.95)$ resolves both the shock and the fine structure (§3.4, Fig. 16). **Shown**
23. Blast waves ($N_x=1599$): dealiased pseudospectral solutions destabilize at once. SR-DlVP destabilizes "for virtually every choice" of the parameters, because the oscillations make $\rho$ and $p$ negative and $c$ cannot be computed. SR-FeKo stays positive and stable, accurate until $t=0.032$, but does not resolve the post-interaction fine structure (§3.4, Fig. 17). **Shown**
24. The blast-wave interaction is "a challenging test case for purely spectral methods", and the authors know of no purely spectral shock-capturing scheme tested on it. They classify Cai & Shu's scheme, which uses ENO interpolation near discontinuities, as not purely spectral (§3.4). **Stated**
25. For the Hou–Luo model, SR-DlVP $(1.6,0.99)$ at $N_x=7995$ stays tyger-free and captures the discontinuity of the vorticity-like variable at $x=0,L/2,L$ without Gibbs oscillations near $t_*=0.0035056$. At $N_x=2665$ it shows attenuated tygers (§3.5, Fig. 18). **Shown**
26. SR keeps nearly all wavenumbers, so the exponential tail of the spectrum can be fitted over a wider range. The analyticity-strip widths $\delta(t)$ from SR-DlVP at $N_x=2665$ and 7995 follow the reference (pseudospectral at $N_x=26650$) longer than plain pseudospectral solutions at the same resolution (§3.5, Fig. 19). **Shown**
27. The fit window must exclude the dissipative ramp of the DlVP kernel. The predicted change of spectral slope is at $k=\frac{2\pi}L\times0.92\times(N/2-1)^{\gamma_{\mathrm{SR}}}\approx43000$ for $N_x=2665$, against a slope change "around $k\sim40000$ as read from the Fig. 19" by the authors (§3.5). **Derived** and **Shown** (see Printed slips)
28. The optimal parameters depend on the problem, the initial data and the resolution. Except for Burgers they were chosen manually by visual agreement; gradient descent or machine learning could automate the search (§4). **Stated**

# Printed slips

- §3.4, below Eq. (9a): "$p=(\gamma-1)\rho$ is the pressure". The ideal-gas law consistent with the total energy of (9a) is $p=(\gamma-1)(E-\tfrac12\rho v^2)$ *(compiler check, not in the sources)*.
- **App. B, Eq. (23b).** $\mathbf l_2^T=(c^2,1,0)$ contradicts Eq. (28b), $\mathcal L_2=\lambda_2(c^2\partial_x\rho-\partial_xp)$, which needs $\mathbf l_2^T=(c^2,-1,0)$. With $\mathbf U=(\rho,p,v)$ and the matrix of Eq. (21), $(c^2,-1,0)$ is a left eigenvector for $\lambda_2=v$ and $(c^2,1,0)$ is not. *(Compiler check, not in the sources.)*
- **App. B, Eq. (30).** Printed $d_1=(1/c^2)\big(\mathcal L_2-\tfrac12(\mathcal L_3+\mathcal L_1)\big)$. From Eq. (28), $\big(\mathcal L_2+\tfrac12(\mathcal L_1+\mathcal L_3)\big)/c^2=v\partial_x\rho+\rho\partial_xv$, so the plus sign is needed for (32a) to be the continuity equation. *(Compiler check, not in the sources.)*
- App. B.2(b) heading: "Supersonic outflow at $x_L$ and non-reflecting subsonic inflow at $x_R$". The body text says supersonic inflow at $x_L$ and subsonic outflow at $x_R$.
- Blast waves: the text gives SR-FeKo at "($\alpha=1.35,\gamma=0.99$)", the Fig. 17 caption "($\alpha=1.355,\gamma=0.999$)".
- Hou–Luo reference resolution: "$N_x=15990$" in the text, "$N_x=15590$" in the Fig. 18 caption.
- DlVP parameter for the Hou–Luo model: $r=0.9$ in App. A.2.1 and the Fig. 21 caption, $r=0.92$ in §3.5, and "$n=0.92$" in the Fig. 18 caption.
- **§3.5 cutoff estimate.** "$k=\frac{2\pi}L\times0.92\times(N/2-1)^\gamma\approx43000$ for $N_x=2665$". With $L=1/6$, $\gamma_{\mathrm{SR}}=0.99$, the value 43000 comes out with $N=N_x=2665$ (42975); with the paper's own Fourier convention $N_x=2N+1$ ($N=1332$) it is about 21600. The formula also differs from the kernel definition $n=rN^\gamma$ of App. A.2.1. *(Compiler check, not in the sources.)*
- App. A.2.2: the optimal Tadmor–Tanner parameters are printed "($\alpha=-0.95,\gamma=0.1$)". A negative $\alpha_{\mathrm{SR}}$ gives a growing relaxation time and contradicts $\alpha>0$ in Eq. (3b).
- Fig. 16 caption "Osher–Shu problem"; Fig. 21 caption "MMO58" for the 1978 filter; "Fejé-Korovkin", "Féjer–Korovkin" (§4) and "Jackson–de La Vallé Poussin" (§3.1).
- App. A.2.4 defines the normalized sinc function, which does not appear in Eq. (18).
- Missing data: Eq. (8b) gives no value for the hump width $\beta$ and Eq. (8c) none for $h_l$, $h_r$; $g$ is never given.

# Notation map

| Kolluru et al. (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u$, $u_N$, $\hat u(k,t)$ | $u$, $u_N$, $\hat u(k,t)$ (page-local) | Burgers solution, its pseudospectral approximation and Fourier coefficients; collocation values, not finite-difference point values or cell averages |
| $N$ | $N_{\mathrm F}$ (page-local) | Fourier truncation wavenumber, $N_x=2N_{\mathrm F}+1$; **$N$ is the DG degree in the registry**; in the Chebyshev case it is the polynomial degree and "$N_x=N$" |
| $N_x$ | $N_x$ | number of collocation points; agrees |
| $\mathcal P_N$, $K_G=2N/3$ | kept | pseudospectral projection, 2/3 dealiasing cutoff |
| $K_m$, $\hat K_m$, $\mathcal M_m=K_m*$ | kept | smoothing kernel and convolution; **$K$ is also the TENO stencil size and a DG element** |
| $m=N^\gamma$ | $m=N_{\mathrm F}^{\gamma_{\mathrm{SR}}}$ | kernel cutoff wavenumber |
| $\tau=N^{-\alpha}$ | $\tau_{\mathrm{SR}}=N_{\mathrm F}^{-\alpha_{\mathrm{SR}}}$ | relaxation time (SR), purging interval (SP); **$\tau$ is the WENO-Z global indicator** |
| $\alpha$, $\gamma$ | $\alpha_{\mathrm{SR}}$, $\gamma_{\mathrm{SR}}$ | **$\gamma$ is also the ratio of specific heats in §3.4 and App. B; $\alpha$ collides with $\alpha_k$** |
| $n$, $p$, $r$ (DlVP) | kept with the kernel | plateau end, ramp width, $r=n/N^\gamma$; **$p$ is also the pressure, the TT05 order and the MMO78 exponent; $n$ is also the SP time index** |
| $\epsilon$, $M$, $\hat Q$ (SVV) | $\epsilon_{\mathrm{SV}}$, $M_{\mathrm{SV}}$, $\hat{\mathcal K}_{\mathrm{SV}}$ | as on the [artificial viscosity](/methods/artificial-viscosity.md) page; **$M$ is also the number of SP intervals, $\epsilon$ also the Shu–Osher amplitude** |
| $\xi=10^{-\beta}$ | kept | MMO78 strength; **$\beta$ is also the Kosloff–Tal-Ezer parameter and the hump width** |
| $\delta(t)$, $t_*$ | kept | analyticity-strip width, blowup time |
| $\rho$, $u$, $p$, $E$, $c$ | $\rho$, $v$, $p$, $E$, $c$ | the conserved vector is ordered $(\rho,E,\rho v)$ |
| $h$, $hu$, $g$ | $h$, $hv$, $g$ | shallow-water depth, discharge, gravity |
| $\mathbf U=(\rho,p,u)$, $\tilde{\mathbf U}$ | kept | primitive and conserved vectors of App. B |
| $\lambda_i$, $\mathbf l_i$, $\mathbf S$, $\Lambda$ | $\lambda_l$, rows of $L$, $R$, $\mathrm{diag}(\lambda_l)$ | eigenstructure of the primitive system |
| $\mathcal L_i$, $\mathbf d$, $\mathbf P$ | kept | Thompson wave amplitudes; **$\mathcal L$ is the semi-discrete operator in the registry** |
| IC0, IC1 | kept | $\sin2\pi x$, $\sin(2\pi x-\pi/2)$ |
| "order" | observed rate | from adjacent-resolution errors in $L^1$, $L^2$ or $L^\infty$; SR has no design order |

# Reference list

The paper prints 75 references, numbered [1]–[75] and sorted alphabetically by
first author. All are parsed and merged complete into the
[bibliography](/bibliography.md) with `citedby` including `kolluru-2024`. Only
[3] and [57] print DOIs. [13], [32] and [61] are arXiv preprints. [2] (Besse,
"Submitted", no year) is a pre-publication entry keyed by the citing year.
[22] (HyPar) has no year. The Clawpack URL of [46] is printed with
percent-escaped LaTeX and is decoded. [47] prints the author as "Qian Liwen"
with no school, read with Qian as the surname. [5] (Butzer & Nessel) is printed
as an "In:" item of a review series and kept as printed. [54] ends its author
list with "et al.". Canuto et al. 2007 [10]/[11] take suffixes in printed
order. No printed duplicates.

# Pages created or updated

Chunk 8 (2026-10-23). This source is cited on:

* [Artificial viscosity and spectral viscosity](/methods/artificial-viscosity.md)
* [Burgers equation tests](/benchmarks/burgers-equation-tests.md)
* [Dam-break problems](/benchmarks/dam-break-problem.md)
* [Shallow-water equations](/definitions/shallow-water-equations.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [Woodward–Colella interacting blast waves](/benchmarks/woodward-colella-blast-wave.md)
