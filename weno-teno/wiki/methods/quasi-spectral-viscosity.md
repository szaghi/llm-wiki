---
type: Method
title: "Quasi-spectral viscosity"
description: "Quasi-spectral viscosity (QSV) is one explicit eddy/artificial viscosity for high-order compact finite differences that serves both as subfilter model in LES and as shock capturing: filter residuals estimate the energy at the grid cutoff and impose a plateau-cusp wavenumber shape on the dissipation; the page gives the closure, its constants and the evidence."
status: established
aliases: [QSV, QSV closure, quasi-spectral eddy viscosity]
tags: [low-dissipation, turbulence, finite-difference, compact-scheme, central-scheme]
timestamp: 2026-10-22T09:49:00Z
---

# Quasi-spectral viscosity

The **quasi-spectral viscosity** (QSV) of
[Sousa & Scalo (2022)](/sources/sousa-2022.md) is an
[artificial viscosity](/methods/artificial-viscosity.md) for a
sixth-order compact (Padé) central finite-difference discretization of the
Favre-filtered compressible Navier–Stokes equations, designed to be at the
same time the subfilter-scale (SFS) model of a large-eddy simulation and the
shock-capturing method. Its magnitude comes from an estimate of the energy at
the grid cutoff, obtained in physical space as the residual of a test
filter; its wavenumber distribution is shaped by a combination of filter
residuals to the **plateau-cusp** spectrum that the exact SFS energy flux
shows both in turbulence (Kraichnan, Chollet–Lesieur, as recalled) and, in
the paper's own a priori analysis, in a forming shock. There is no separate
shock sensor: the cutoff-energy estimate switches the dissipation on at
shocks as it does at under-resolved eddies (§4.2). The scheme has no
upwinding, Riemann solver, reconstruction or limiter.

## One form for eddy and spectral viscosities

Sousa & Scalo write the dynamic Smagorinsky model (DYN), the Chollet–Lesieur
spectral eddy viscosity (SEV), Tadmor's spectral vanishing viscosity (SVV)
and QSV in the common form of a length scale times a velocity scale times a
kernel convolved with the strain rate (§2.2, Eq. (17), Table 1; page-local
$\ell$, $\upsilon$, $\mathcal K$, the SFS stress $\tau_{ij}$ and the
strain rate $S_{ij}$, which carry two indices and are not the registry's
$\tau$ or $S(u)$):
$$\tau_{ij}=\ell\,\upsilon\,(\mathcal K*S_{ij}),$$
with $\mathcal K=1$ for DYN, the Chollet–Lesieur plateau-cusp kernel for
SEV, the SVV kernel for SVV, and the residual $1-G_{\mathrm{qsv}}$ of the QSV filter
below. Two consequences are drawn (§2.2, §8):

- adding SVV to Burgers' equation, $\partial_tu+\tfrac12\partial_x(u^2)=\epsilon_{\mathrm{SV}}\partial_x(\mathcal K_{\mathrm{SV}}*\partial_xu)$
  (page-local $\epsilon_{\mathrm{SV}}$, $\mathcal K_{\mathrm{SV}}$; Tadmor's conditions
  $\epsilon_{\mathrm{SV}}\ge1/k_c$ and an activation wavenumber
  $\sim k_c^{\beta_{\mathrm{SV}}}$, $\beta_{\mathrm{SV}}<\tfrac12$, as recalled), is formally the
  closure of the filtered Burgers equation by an eddy viscosity, which in
  the authors' view explains why SVV "worked" when extended to turbulent
  LES;
- SEV is the residual of a test filter applied to the resolved strain,
  $-\tau^d_{ij}=\sqrt{2\bar\Delta E_{k_c}}\big((1-\widetilde G)*\bar S_{ij}\big)$
  (Eq. (12); $\bar\Delta$ the filter width, $E_{k_c}$ the energy at the
  cutoff wavenumber $k_c$, $\widetilde G$ a test filter, page-local), which
  makes its kinship with Germano's dynamic procedure explicit.

**A priori evidence on Burgers** (§2.3, Fig. 1). For the filtered inviscid
Burgers equation with $u_0=1+\tfrac12\sin(\pi x)$ on $[-1,1]$ (Fourier
pseudo-spectral, $N_x=128$, RK4, $t=1$), the exact SFS energy flux spans all
resolved wavenumbers and peaks near $k_c$. DYN gives a flat broadband
dissipation, too strong at large scales and too weak near the cutoff, with
pile-up a posteriori; SVV with an inviscid low-wavenumber range (activation at
$5\sqrt{k_c}$) under-damps the low wavenumbers and oscillates at the shock,
the more so the larger the inviscid range, while SVV active from $k=0$ does
better. The authors conclude that the closer the spectrum of the added
dissipation is to the exact SFS one, the better the resolved solution
(§2.3).

## Building blocks

Let $\vartheta=k_w\Delta x$ be the reduced wavenumber (registry §9), so that
the grid cutoff is $\vartheta=\pi$.

**Sixth-order Padé filter** (Lele, as recalled; Eqs. (20)–(22)):
$$\alpha_{\mathrm P}\tilde f_{i-1}+\tilde f_i+\alpha_{\mathrm P}\tilde f_{i+1}=a_0f_i+\sum_{j=1}^{3}\frac{a_j}{2}\big(f_{i+j}+f_{i-j}\big),\qquad
\hat G_{\mathrm P}(\vartheta)=\frac{a_0+\sum_{j=1}^3a_j\cos(j\vartheta)}{1+2\alpha_{\mathrm P}\cos\vartheta},$$
with $a_0=\frac{11+10\alpha_{\mathrm P}}{16}$, $a_1=\frac{15+34\alpha_{\mathrm P}}{32}$,
$a_2=\frac{-3+6\alpha_{\mathrm P}}{16}$, $a_3=\frac{1-2\alpha_{\mathrm P}}{32}$
and $\alpha_{\mathrm P}\in(0,\tfrac12)$ (page-local; larger is weaker), so
that $\hat G_{\mathrm P}(0)=1$ and $\hat G_{\mathrm P}(\pi)=0$
*(compiler check, not in the sources: $a_0+a_1+a_2+a_3=1+2\alpha_{\mathrm P}$ and
$a_0-a_1+a_2-a_3=0$ for every $\alpha_{\mathrm P}$)*.

**Cutoff-energy estimate** (§3.1, Eqs. (23)–(26)). The residual
$1-\hat G_{\mathrm P}$ concentrates near the cutoff, the more so as
$\alpha_{\mathrm P}\to\tfrac12$ (at the price of a wider physical-space
footprint). Its area
$A(\alpha_{\mathrm P})=\int_0^1\big(1-\hat G_{\mathrm P}\big)\,d(\vartheta/\pi)$
has the closed form of Eq. (25) ($5/16$ at $\alpha_{\mathrm P}=0$). Let
$\alpha_{k_c}$ be the strength at which $\hat G_{\mathrm P}=\tfrac12$ at the
last resolvable mode, $\vartheta=\pi(k_c-1)/k_c$ (Eq. (24); $0.4994$ for
$k_c=64$, *compiler check, not in the sources: $0.49940$ by bisection*). The
energy of velocity component $v_j$ at the cutoff in direction $i$ is
estimated as
$$\mathsf E^{(i)}(v_j)=\Big[\big(1-G^{(i)}_{\mathrm P}\big)*\tfrac12v_j^2\Big]\frac{A(\alpha_{\mathrm P})}{A(\alpha_{k_c})}$$
(page-local $\mathsf E^{(i)}$), with $\alpha_{\mathrm P}=0.45$ in every
problem and an optional Gaussian smoothing near grid-misaligned shocks
(§4.2).

**Truncated Fejér filter** (§3.2, Eqs. (27)–(34)). The Fejér (first-order
Vandeven) filter has the ideal transfer function $1-\vartheta/\pi$. Written
as a global periodic convolution in physical space, its weights decay fast
enough ("self-windowed") to be truncated to a half-width $n_w=8$, reduced
near non-periodic boundaries, with a transfer function close to the ideal
line (Fig. 3).

**QSV modulation** (§3.2, Eq. (35)):
$$\hat G_{\mathrm{qsv}}=w_{\mathrm{DC}}\Big[1-b_{\mathrm F}\,\hat G_{\mathrm P}(\alpha_{\mathrm P})+(1-b_{\mathrm F})\,\hat G_{\mathrm F}\Big],\qquad \alpha_{\mathrm P}=0.45,\ b_{\mathrm F}=0.8,\ w_{\mathrm{DC}}=0.85$$
(page-local; the source writes $\alpha$, $\beta$, $w$, the last called a
"DC offset"), applied as $1-G_{\mathrm{qsv}}$ in all three directions. The
parameters were tuned on Burgers and checked against exact a priori SFS
spectra of the Taylor–Green vortex and of a periodic Sod problem (Fig. 12,
Fig. A.21).

## The closure

For the Favre-filtered equations (after Nagarajan et al.; the SFS
kinetic-energy transport and heat dissipation terms neglected, Eqs.
(36)–(44)), with filter widths $\bar\Delta_j$, velocity scale
$\upsilon_i(v_j)=\sqrt{2\mathsf E^{(i)}(v_j)/\bar\Delta_i}$ and dissipation
magnitude tensor $\mathcal D_{ij}=\upsilon_i(v_j)\,\bar\Delta_j$ (page-local;
Eqs. (45)–(46)), the SFS stress and temperature flux are (Eqs. (47)–(51))
$$\tau_{ij}=-\frac{C_{\tau,ij}}{2}\Big(\mathcal D_{ij}\,\breve\partial_jv_i+\mathcal D_{ji}\,\breve\partial_iv_j\Big),\qquad \mathfrak q_j=-C_q\,\mathcal D_{jj}\,\breve\partial_jT,\qquad
\breve\partial_jv_i=(1-G_{\mathrm{qsv}})*\partial_{x_j}v_i,$$
with $C_{\tau,ij}=1.0$ for $i=j$, $0.6$ for $i\ne j$, and $C_q=0.8$
(page-local $\breve\partial$, $\mathfrak q_j$, $C_{\tau,ij}$, $C_q$, $T$ the
temperature; the source writes $q_j$),
informed by a priori analyses of Sod and the Taylor–Green vortex, where the
trace components of the exact SFS stress exceed the off-diagonal ones at all
resolved wavenumbers (§4.2, §6.1). A curvilinear formulation is given in
App. B. As constructed from sharp-spectral-filter a priori analyses, the
model "is only suitable for spectral or quasi-spectral high-order
discretizations" (§3.2).

## Evidence

The reference shock-capturing method is the local artificial diffusivity
(LAD) of Cook and Kawai–Lele (artificial shear and bulk viscosity and
conductivity, with an explicit Padé filter of strength 0.495), not written
out in the paper. All runs use sixth-order compact differences and a
third-order Runge–Kutta method.

| Test | Finding (Sousa & Scalo 2022) |
|---|---|
| [Sod](/benchmarks/sod-and-lax-shock-tubes.md), grid study, $t=0.2$ | QSV and LAD both converge, QSV slightly sharper at equal grid; LAD needs the explicit filter, QSV does not (an optional one at strength 0.499 attenuates residual oscillations) (§5.1, Fig. 4) |
| [Shu–Osher](/benchmarks/shu-osher-problem.md), scaled to $[-1,1]$, $t=0.36$ | trailing waves recovered alike; sharper shock with QSV; monotone convergence from very coarse grids (§5.1, Fig. 5) |
| strong shock–strong vortex ([shock–vortex interaction](/benchmarks/shock-vortex-interaction.md)), $192\times96$ to $768\times384$ | both miss the vortex splitting on the coarsest grid and converge to the same result; QSV sharper and less noisy, but with a smaller top-vortex core at $384\times192$; QSV sustains the shock on a sinusoidally distorted grid (§5.2, Figs. 6–7) |
| shock reflection off a sinusoidal wall, $1024\times256$ | at $M=1.5$, $\gamma=1.4$ triple points, Mach stems and slip lines reproduced with 8 times fewer degrees of freedom than Tonicello et al.; at $M=5$, $\gamma=1.15$ LAD oscillates strongly and breaks symmetry early, QSV keeps symmetry (§5.3, Figs. 8–11) |
| subsonic [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md), $M_t=0.1$, Re 5000, $96^3$ | the run without model diverges; QSV is closer to filtered DNS than DYN and the coherent-vorticity-preserving model from $tV_0/L\approx6$ and alone recovers the post-peak dissipation plateau; monotone improvement on $72^3$–$144^3$ (§6.1, Figs. 13–14) |
| compressible channel, $M_b=1.5$ and 6.0 | Vreman's model closer to the log law at each grid; QSV "may not be the best choice for simple wall-bounded turbulent flows" (§6.2–§6.3, Fig. 15) |
| supersonic Taylor–Green vortex, $M_t=1.2$, Re 5000 | without shock capturing every turbulence model blows up at $96^3$; with LAD added, all runs over-dissipate at the strongest shocklets; QSV alone stays closest to a $384^3$ QSV reference (§7.1, Figs. 16–19) |

Cost on the $96^3$ Taylor–Green vortex, relative to no model: Smagorinsky
+34.3%, CvP +37.7%, QSV with the stress only +64.7%, DYN +72.5%, full QSV
+78.5% (Table 2; hardware not stated). On the supersonic vortex the kinetic
energy is not monotone, and the paper measures dissipation with Myers'
exact compressible energy norm instead, which decays monotonically (§7.1).

## Qualifications

- All evidence is numerical; no stability or accuracy result is proved. The
  shock-capturing comparisons are against LAD only; there is no comparison
  with upwind, WENO or TENO schemes. The $M_t=1.2$ reference is itself a QSV
  run, justified by grid convergence of QSV and of Smagorinsky with LAD
  (§7.1).
- The model constants and filter parameters are tuned a priori on Burgers,
  Sod and the Taylor–Green vortex; the plateau-cusp argument is the basis
  of their claimed universality.
- **Printed slips (arXiv v2).** The closed form of the Fejér weights
  (Eqs. (31)–(32)) does not reproduce the definition (Eq. (30)): the
  diagonal weight is $\frac{4+2k_c}{2(2+2k_c)}$ against $\tfrac12$ from
  Eq. (30), and the off-diagonal weights are smaller by the factor
  $k_c/(k_c+1)$; the closed form has the transfer function
  $1-k/(k_c+1)$, not $1-k/k_c$ (e.g. diagonal 0.5556 against 0.5 and ratio
  1.125 at $k_c=8$; 0.5077 and 1.0156 at $k_c=64$) *(compiler check, not in
  the sources)*, an $O(1/k_c)$ inconsistency. The SEV length scale is
  written $1/k_c\approx2\bar\Delta$, while $k_c=\pi/\Delta$ (Eq. (22)) gives
  $1/k_c\approx0.32\Delta$. The constants are called "all of unitary value"
  (§4.2) against Eq. (51). Eq. (17) carries no minus sign, Eqs. (8), (11),
  (12), (19) and (47) do.

# Citations

- [Sousa & Scalo (2022)](/sources/sousa-2022.md) — arXiv v2: §1; §2.2 (Eqs. (8)–(17), Table 1); §2.3 (Fig. 1); §3.1 (Eqs. (20)–(26), Fig. 2); §3.2 (Eqs. (27)–(35), Fig. 3); §4.2 (Eqs. (36)–(51)); §5 (Figs. 4–11); §6 (Figs. 12–15, Tables 2–3); §7.1 (Figs. 16–19); §8; Apps. A–B.
