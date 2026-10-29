---
type: Method
title: "Compact finite-difference schemes"
description: "Compact (Padé-type) finite differences obtain derivatives, interpolations and low-pass filters from a banded implicit system; the page gives Lele's founding tridiagonal and pentadiagonal families, their modified wavenumbers and resolving efficiency, spectral-like coefficients, boundary closures and stability, and the stencils, filters and uses in DNS, implicit LES and shock-capturing hybrids."
status: established
aliases: [compact scheme, compact finite differences, Padé scheme, Lele scheme, sixth-order compact scheme, tridiagonal compact scheme, pentadiagonal compact scheme, spectral-like compact scheme, compact filter, compact interpolation, modified wavenumber analysis, resolving efficiency]
tags: [dns, implicit-les, numerical-dissipation, filtering, software]
timestamp: 2026-10-29T16:18:00Z
---

# Compact finite-difference schemes

A **compact** (or Padé-type, implicit) finite-difference scheme computes a
derivative, an interpolated value or a filtered value at all nodes of a
grid line at once, from a linear system in which each unknown is coupled
to its neighbours (a tridiagonal one in the sources below). For the first derivative
on a uniform grid of spacing $h$ the sixth-order member of the family is

$$\alpha_{\mathrm c}\phi'_{i-1}+\phi'_i+\alpha_{\mathrm c}\phi'_{i+1}=a_{\mathrm c}\frac{\phi_{i+1}-\phi_{i-1}}{2h}+b_{\mathrm c}\frac{\phi_{i+2}-\phi_{i-2}}{4h},\qquad \alpha_{\mathrm c}=\tfrac13,\ a_{\mathrm c}=\tfrac{14}9,\ b_{\mathrm c}=\tfrac19,$$

as printed by [Yan et al. (2024)](/sources/yan-2024.md), App. A1,
Eq. (A2), for the [Xcompact3d](/software/xcompact3d.md) framework, and with
the same coefficients by [Kang & Lee (2024)](/sources/kang-2024.md),
§II.B, Eq. (8), for their compressible DNS solver (Lele; Visbal & Gaitonde,
as cited). The historical review of
[Kim & Leonard (2024)](/sources/kim-2024-b.md), §4.8, records that these
schemes (Lele 1992, as cited there) were developed to minimize numerical
dispersion error, for computational aeroacoustics at NASA Ames.
The families themselves are constructed in
[Lele (1992)](/sources/lele-1992.md), where the sixth-order scheme above
is Eq. (2.1.7) (Lele credits the $\alpha_{\mathrm c}=\tfrac14,\tfrac13$
members to Collatz, cited). Lele, writing at the Center for Turbulence
Research, NASA Ames, states the motivation as direct numerical
simulation of phenomena with a range of scales, "turbulent fluid flows
being a common example", for which spectral methods are limited to simple
domains and boundary conditions (§1), and puts the emphasis on the
**resolution characteristics** of a scheme, how accurately it represents
the exact derivative over the full range of scales a mesh can carry,
rather than on its formal truncation error (§1).

Notation (page-local): $\phi_i$ a grid function at node $x_i$, primes its
discrete derivatives; $\alpha_{\mathrm c}$, $a_{\mathrm c}$, $b_{\mathrm c}$
the compact coefficients (not the registry's DG blending factor $\alpha$
or modal-filter strength $\alpha_f$), and $\beta_{\mathrm c}$,
$c_{\mathrm c}$ the extra coefficients of the pentadiagonal and
seven-point members; $\epsilon_{\mathrm r}$ an error tolerance and
$e_{\mathrm r}$ the resolving efficiency (below); $\alpha_{\mathrm{cf}}$ and $a_n$ the
parameter and coefficients of a compact filter, $\phi^{\mathrm f}_i$ the
filtered value (not the registry's test filter $\hat\phi$); $k'$, $k''$ the modified
wavenumbers of the first and second derivative; $k_c=\pi/h$ the grid
cut-off (registry §8).

## The general families (Lele 1992)

Lele (1992, §2.1, Eq. 2.1) writes the first derivative on a uniform mesh
as the five-point implicit, seven-point explicit relation

$$\beta_{\mathrm c}\phi'_{i-2}+\alpha_{\mathrm c}\phi'_{i-1}+\phi'_i+\alpha_{\mathrm c}\phi'_{i+1}+\beta_{\mathrm c}\phi'_{i+2}=c_{\mathrm c}\frac{\phi_{i+3}-\phi_{i-3}}{6h}+b_{\mathrm c}\frac{\phi_{i+2}-\phi_{i-2}}{4h}+a_{\mathrm c}\frac{\phi_{i+1}-\phi_{i-1}}{2h},$$

tridiagonal for $\beta_{\mathrm c}=0$ and pentadiagonal otherwise (cyclic
in the periodic case). Matching Taylor coefficients gives one constraint
per order,

$$\begin{aligned}
a_{\mathrm c}+b_{\mathrm c}+c_{\mathrm c}&=1+2\alpha_{\mathrm c}+2\beta_{\mathrm c} &&\text{(second order)},\\
a_{\mathrm c}+2^2b_{\mathrm c}+3^2c_{\mathrm c}&=2\tfrac{3!}{2!}\big(\alpha_{\mathrm c}+2^2\beta_{\mathrm c}\big) &&\text{(fourth order)},\\
a_{\mathrm c}+2^4b_{\mathrm c}+3^4c_{\mathrm c}&=2\tfrac{5!}{4!}\big(\alpha_{\mathrm c}+2^4\beta_{\mathrm c}\big) &&\text{(sixth order)},\\
a_{\mathrm c}+2^6b_{\mathrm c}+3^6c_{\mathrm c}&=2\tfrac{7!}{6!}\big(\alpha_{\mathrm c}+2^6\beta_{\mathrm c}\big) &&\text{(eighth order)},\\
a_{\mathrm c}+2^8b_{\mathrm c}+3^8c_{\mathrm c}&=2\tfrac{9!}{8!}\big(\alpha_{\mathrm c}+2^8\beta_{\mathrm c}\big) &&\text{(tenth order)}
\end{aligned}$$

(Eqs. 2.1.1–2.1.5), so fourth order leaves a three-parameter family,
sixth a two-parameter, eighth a one-parameter family, and a single
tenth-order scheme exists. The members Lele prints (§2.1, Table I) are:

- fourth-order tridiagonal ($\beta_{\mathrm c}=c_{\mathrm c}=0$):
  $a_{\mathrm c}=\tfrac23(\alpha_{\mathrm c}+2)$,
  $b_{\mathrm c}=\tfrac13(4\alpha_{\mathrm c}-1)$, truncation error
  $\tfrac4{5!}(3\alpha_{\mathrm c}-1)h^4\phi^{(5)}$ (Eq. 2.1.6);
  $\alpha_{\mathrm c}\to0$ is the explicit fourth-order central difference,
  $\alpha_{\mathrm c}=\tfrac14$ the classical Padé scheme, and
  $\alpha_{\mathrm c}=\tfrac13$ the sixth-order scheme of the lead
  (Eq. 2.1.7, error $\tfrac4{7!}h^6\phi^{(7)}$);
- tridiagonal with seven-point right side: sixth order for
  $a_{\mathrm c}=\tfrac16(\alpha_{\mathrm c}+9)$,
  $b_{\mathrm c}=\tfrac1{15}(32\alpha_{\mathrm c}-9)$,
  $c_{\mathrm c}=\tfrac1{10}(1-3\alpha_{\mathrm c})$, eighth order at
  $\alpha_{\mathrm c}=\tfrac38$, "the tridiagonal scheme with the highest
  formal accuracy" within the family (Eq. 2.1.8);
- pentadiagonal: eighth order with five-point right side at
  $\alpha_{\mathrm c}=\tfrac49$, $\beta_{\mathrm c}=\tfrac1{36}$,
  $a_{\mathrm c}=\tfrac{40}{27}$, $b_{\mathrm c}=\tfrac{25}{54}$ (Eq. 2.1.12),
  and tenth order at $\alpha_{\mathrm c}=\tfrac12$,
  $\beta_{\mathrm c}=\tfrac1{20}$, $a_{\mathrm c}=\tfrac{17}{12}$,
  $b_{\mathrm c}=\tfrac{101}{150}$, $c_{\mathrm c}=\tfrac1{100}$, error
  $\tfrac{144}{11!}h^{10}\phi^{(11)}$ (Eq. 2.1.14).

The members of highest formal accuracy for a given stencil are the
rational (Padé) approximations of the derivative operator tabulated by
Kopal, in whose table Lele reports two coefficients in error (§2.1,
footnote 1). The second derivative takes the same form with the
differences $(\phi_{i+m}-2\phi_i+\phi_{i-m})/(m^2h^2)$, $m=1,2,3$, on
the right (Eq. 2.2): the fourth-order tridiagonal family is
$a_{\mathrm c}=\tfrac43(1-\alpha_{\mathrm c})$,
$b_{\mathrm c}=\tfrac13(10\alpha_{\mathrm c}-1)$, with the Padé scheme at
$\alpha_{\mathrm c}=\tfrac1{10}$ and sixth order at
$\alpha_{\mathrm c}=\tfrac2{11}$, $a_{\mathrm c}=\tfrac{12}{11}$,
$b_{\mathrm c}=\tfrac3{11}$ (Eqs. 2.2.6–2.2.7), which is the
second-derivative stencil of Yan et al. below; again a single
tenth-order scheme closes the hierarchy (Eq. 2.2.11). Appendix A gives
tridiagonal third- and fourth-derivative schemes, Appendix B the
cell-centred (staggered) derivatives, Appendix C mid-point interpolation
and low-pass filters, all built the same way. The cost of a periodic
pentadiagonal solve is $7N$ multiplications per line against
$2N\log_2N$ for a radix-2 FFT ($N$ the number of points here, not a
polynomial degree; §3.1).

## Modified wavenumber and resolving efficiency

For a Fourier mode of scaled wavenumber $kh\in[0,\pi]$ the exact
derivative multiplies the mode by $\mathrm ik$; a central compact scheme
multiplies it by $\mathrm ik'$ with the real **modified wavenumber**

$$k'h=\frac{a_{\mathrm c}\sin(kh)+\tfrac{b_{\mathrm c}}2\sin(2kh)+\tfrac{c_{\mathrm c}}3\sin(3kh)}{1+2\alpha_{\mathrm c}\cos(kh)+2\beta_{\mathrm c}\cos(2kh)}$$

(Lele 1992, §3.1, Eq. 3.1.4), so central schemes carry no dissipative
error in the interior (§3); $k'/k$ is the numerical phase speed of
advection (Eq. 3.1.7). Lele measures resolution by the **resolving
efficiency** $e_{\mathrm r}=k_{\mathrm f}h/\pi$, with $k_{\mathrm f}$
(page-local) the upper end of the range in which
$|k'-k|/k\le\epsilon_{\mathrm r}$ (Eq. 3.1.3): the fraction of the
representable waves that are well resolved, independent of the number of
points, a notion Lele calls "analogous to, but more general than" the
points-per-wavelength measure, which senses only the longest waves (§1,
§3.1). Table III ($\epsilon_{\mathrm r}=0.1$, 0.01, 0.001):

| first-derivative scheme | $e_{\mathrm r}$ |
|---|---|
| second-order central | 0.25, 0.08, 0.02 |
| fourth-order central | 0.44, 0.23, 0.13 |
| sixth-order central | 0.54, 0.35, 0.23 |
| Padé, $\alpha_{\mathrm c}=\tfrac14$ | 0.59, 0.35, 0.20 |
| sixth-order tridiagonal, $\alpha_{\mathrm c}=\tfrac13$ | 0.70, 0.50, 0.35 |
| eighth-order tridiagonal | 0.75, 0.58, 0.44 |
| eighth-order pentadiagonal | 0.77, 0.61, 0.48 |
| tenth-order pentadiagonal | 0.81, 0.68, 0.56 |
| spectral-like pentadiagonal | 0.90, 0.83, 0.79 |

**Spectral-like schemes.** Giving up maximal order, Lele imposes
$k'(k_m)=k_m$ at $k_mh=2.2$, 2.3, 2.4 on the fourth-order pentadiagonal
family and obtains $\alpha_{\mathrm c}=0.5771439$,
$\beta_{\mathrm c}=0.0896406$, $a_{\mathrm c}=1.3025166$,
$b_{\mathrm c}=0.9935500$, $c_{\mathrm c}=0.03750245$, formally fourth
order, adding that "no attempt was made to optimize" the three points
(Eqs. 3.1.5–3.1.6); the second-derivative analogue (Eqs. 3.1.12–3.1.13)
reaches $e_{\mathrm r}=1.00$, 0.89, 0.84 (Table V). The same trade shows
inside the tridiagonal fourth-order family: a member with larger
$\alpha_{\mathrm c}$ resolves better at $\epsilon_{\mathrm r}=0.01$ and
0.001 than the sixth-order $\alpha_{\mathrm c}=\tfrac13$ member (Table IV;
the member's value is printed two ways, see Qualifications), which Lele
expects "to be a general feature": the dispersive error at
$kh\in(\pi/2,\pi)$ is not very sensitive to the formal truncation error
(§3.1). The optimization of stencils by such spectral objectives is
followed further on
[low-dissipation low-dispersion schemes](/methods/low-dissipation-low-dispersion-scheme.md).
For the second derivative the modified wavenumber $k''$ approximates
$k^2$, and its largest error, near $kh=\pi$, depends only weakly on the
formal order (Eq. 3.1.10, Table V, Fig. 5).

In two dimensions the phase speed depends on the propagation angle, with
least error along the diagonals; for the spectral-like scheme the
anisotropy is felt only by the shortest 20% of the waves (Eqs. 3.1.8–3.1.9,
Figs. 3–4). Lele warns that the improved resolution entails a possibility
of larger aliasing errors in nonlinear problems, to be removed by
spectral de-aliasing (periodic) or spectral-like filtering (non-periodic),
and that "more research is needed" (§3.1). On a cell-centred mesh the
compact schemes resolve better near $kh=\pi$ than collocated ones, the
pentadiagonal ones being "virtually indistinguishable" from exact
differentiation (App. B, Figs. 16–17).

## Boundary closures, conservation and stability

Near a non-periodic boundary Lele (1992, §4.1, Eq. 4.1.1) closes the
system by
$\phi'_1+\alpha_{\mathrm b}\phi'_2=h^{-1}(a_{\mathrm b}\phi_1+b_{\mathrm b}\phi_2+c_{\mathrm b}\phi_3+d_{\mathrm b}\phi_4)$
(subscript-b coefficients page-local), which keeps a tridiagonal interior
tridiagonal, with second-, third- and fourth-order families; the
fourth-order member is $\alpha_{\mathrm b}=3$,
$(a_{\mathrm b},b_{\mathrm b},c_{\mathrm b},d_{\mathrm b})=(-\tfrac{17}6,\tfrac32,\tfrac32,-\tfrac16)$
(Eq. 4.1.4), and the third-order one with $\alpha_{\mathrm b}=2$,
$d_{\mathrm b}=0$ has one-ninth of the truncation error of the explicit
third-order formula. A one-sided closure has a complex modified
wavenumber: its real part is the dispersive error and its imaginary part
the dissipative error, even-order closures erring mainly in dispersion and
third-order ones in dissipation. The imaginary part of many compact
closures has the opposite sign to that of explicit one-sided formulas,
and Lele calls it "erroneous" to infer instability from this: the
stability of the complete scheme must come from an eigenvalue analysis
(§4.1). A second-order closure with $\alpha_{\mathrm b}=4$,
$d_{\mathrm b}=-\tfrac12$ has virtually no dissipative error, which Lele
takes as evidence that the desired properties "are better achieved by
directly optimizing the scheme (in Fourier space)" (§4.1).

- **Global conservation** (§4.2, Eqs. 4.2.1–4.2.18). Writing the whole
  scheme as $\mathbf A\boldsymbol\phi'=h^{-1}\mathbf B\boldsymbol\phi$
  ($\mathbf A$, $\mathbf B$ page-local), the scheme satisfies a discrete
  conservation law when columns 2 to $N-1$ of $\mathbf B$ sum to zero,
  so that only boundary fluxes remain and the scheme implies quadrature
  weights near the boundary. It needs at least 10 nodes for a
  five-point interior right side and 14 for a seven-point one, and carries
  over to mapped non-uniform meshes.
- **Eigenvalue stability** (§4.5, Figs. 9–10): for advection with the
  tridiagonal fourth-order interior family and conservative,
  non-conservative compact or explicit closures, all semi-discrete
  eigenvalues lie in the stable half-plane up to $N=200$; the analysis
  and its exceptions are on
  [eigensolution analysis](/methods/eigensolution-analysis.md).
- **Tests with boundaries** (§4.4, Fig. 8): on 129 points, with the
  sixth-order interior, the conservative formulation and the third-order
  compact closure, random-phase multi-mode functions show the dominant
  error always at the boundary; even for the highest test modes "the
  interior is virtually error-free".
- **Explicit time-step limits** (§4.6, Eqs. 4.6.1–4.6.5): on a periodic
  domain, advection at speed $a$ (page-local) requires
  $a\Delta t/h\le s_{\mathrm i}/(k'h)_{\max}$ and diffusion
  $\nu\Delta t/h^2\le s_{\mathrm r}/(k''h^2)_{\max}$, with
  $s_{\mathrm i}=0$, $\sqrt3$, 2.85 and $s_{\mathrm r}=2$, 2.5, 2.9 the
  imaginary- and real-axis extents of the second-, third- and fourth-order
  Runge–Kutta stability regions (page-local). The printed
  $(k'h)_{\max}$ rise from 1.0 (second-order central) through $\sqrt3$
  (Padé) and 1.989 (sixth-order tridiagonal) to 2.324 (tenth-order) and
  $\pi$ (spectral), in the order of the resolving efficiencies of
  Table III, and Lele notes that spectral schemes have the most severe
  time-step restriction.

## Use without built-in dissipation

The schemes are purely central away from boundaries, with no built-in
artificial dissipation, so Lele (1992, §5) restricts them to problems
whose shortest scales are "determined *physically and not numerically*",
which excludes direct application to flows with discontinuities. The
viscous terms are differenced with the second-derivative scheme
(non-conservative form), because it damps the grid-to-grid ($kh=\pi$)
wave that two applications of the first-derivative scheme leave undamped;
the schemes are not monotone, and differentiating a step gives
grid-to-grid oscillations that decay exponentially away from it, against
the algebraic $x^{-1}$ decay of spectral Gibbs oscillations (§5).
Non-reflecting boundary conditions adapted from Thompson (cited) work
well with them, while conditions suited to dissipative low-order schemes
"may not perform well" (§5). Two applications are shown: a spatially
developing compressible mixing layer (Mach 2.0 and 1.2 streams,
convective Mach number 0.4, $601\times161$ points), whose roll-up and
pairing are captured with scalar gradients in the braids resolved by 7–8
points, and the viscous structure of a Mach 1.5 normal shock with 7–8
points across it, whose profiles vary smoothly (Figs. 11–13). Later
sources pair the schemes with filters, artificial diffusivity or WENO
switching instead (below, and Qualifications).

## Stencils in the sources

- **First derivative, sixth order** (above). Applied to $\phi=x$ both
  sides equal $\tfrac53$, and the modified wavenumber is
  $k'h=\big[a_{\mathrm c}\sin(kh)+\tfrac{b_{\mathrm c}}2\sin(2kh)\big]/\big[1+2\alpha_{\mathrm c}\cos(kh)\big]$,
  the $\beta_{\mathrm c}=c_{\mathrm c}=0$ case of Lele's Eq. (3.1.4). Kang & Lee use it on generalized
  curvilinear coordinates ($h=1$) with sixth-order one-sided compact
  closures at the boundaries (§II.B).
- **Second derivative, sixth order** (Yan et al. 2024, Eq. A3; Lele
  1992, Eq. 2.2.7):
  $$\tfrac2{11}\phi''_{i-1}+\phi''_i+\tfrac2{11}\phi''_{i+1}=\tfrac{12}{11}\frac{\phi_{i+1}-2\phi_i+\phi_{i-1}}{h^2}+\tfrac3{11}\frac{\phi_{i+2}-2\phi_i+\phi_{i-2}}{4h^2}.$$
  Widening the right-hand side to nine points leaves two free
  coefficients, which Xcompact3d uses to make the scheme over-dissipative
  near $k_c$: the implicit
  [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
  (Yan et al., App. B1; [Vicente Cruz & Lamballais 2023](/sources/vicentecruz-2023.md),
  §5.1).
- **Staggered first derivative, sixth order** (from nodes to mid-points;
  [Fang et al. 2025](/sources/fang-2025.md), §2.3, Eq. 15):
  $$\tfrac9{62}\phi'_{i-1/2}+\phi'_{i+1/2}+\tfrac9{62}\phi'_{i+3/2}=\tfrac{63}{62}\frac{\phi_{i+1}-\phi_i}{h}+\tfrac{17}{186}\frac{\phi_{i+2}-\phi_{i-1}}{h},$$
  exact for $\phi=x$ ($\tfrac{80}{62}$ on both sides) *(compiler check, not
  in the sources)*. It is the member $\alpha_{\mathrm c}=\tfrac9{62}$ of
  Lele's cell-centred tridiagonal family,
  $a_{\mathrm c}=\tfrac38(3-2\alpha_{\mathrm c})$,
  $b_{\mathrm c}=\tfrac18(22\alpha_{\mathrm c}-1)$ with the second
  difference divided by $3h$ (App. B, Eqs. B.1.1–B.1.2), which Lele calls
  sixth order and "quite close to exact differentiation": the printed
  formulas give $a_{\mathrm c}=\tfrac{63}{62}$ and
  $b_{\mathrm c}/3=\tfrac{17}{186}$ *(compiler check, not in the
  sources)*.
- **Mid-point interpolation, sixth order** (Fang et al. 2025, Eq. 16;
  Yan et al. 2024, Eq. A1):
  $$\tfrac3{10}\phi^I_{i-1/2}+\phi^I_{i+1/2}+\tfrac3{10}\phi^I_{i+3/2}=\tfrac34(\phi_{i+1}+\phi_i)+\tfrac1{20}(\phi_{i+2}+\phi_{i-1}),$$
  which reproduces a constant ($1.6$ on both sides) *(compiler check, not
  in the sources)*, and which is the tridiagonal member ($\beta_{\mathrm c}=c_{\mathrm c}=0$,
  $\alpha_{\mathrm c}=\tfrac3{10}$) of Lele's sixth-order interpolation family (App. C.1,
  Eq. C.1.4; right-side weights $\tfrac32\cdot\tfrac12$ and
  $\tfrac1{10}\cdot\tfrac12$ by the printed formulas, *compiler check, not
  in the sources*); it moves quantities
  between the velocity and pressure grids of a staggered or half-staggered
  arrangement (see Qualifications for Yan et al.'s printed form).

Fang et al. combine the staggered derivative in one direction with the
mid-point interpolation in the other to build the right-hand side of a
Poisson equation on the half-staggered pressure mesh, solved directly by
FFT; with the modified-wavenumber concept the discrete velocity
divergence vanishes "up to machine accuracy" (§2.3, Eq. 14, citing Lele
and Laizet & Lamballais). The same arrangement carries the magnetic
"pressure" correction of their MHD solver, whose divergence of the field
is about $10^{-13}$ after correction (§2.2).

## Spectral behaviour and induced filters

In the half-staggered
compact-difference code of [Caban et al. (2026)](/sources/caban-2026.md)
(sixth- and tenth-order compact derivatives, compact or spectral
interpolation), the filter induced by the first-derivative scheme changes
only the phase speed, the filter induced by the second-derivative scheme
lowers the viscous dissipation of the small scales, and two successive
interpolations act as a squared filter (§3.2, Eqs. 34–35); in the
transitional Taylor–Green vortex the interpolation order matters most
when it is close to the derivative order (§4.1, Fig. 5a; see
[discretization-consistent closures](/definitions/discretization-consistent-closure.md)).
The modified wavenumber of the first-derivative scheme above is real, so
that scheme adds no dissipation, as Lele (1992, §3) states for every
central scheme of the family.
The sources add instead
a skew-symmetric form of the convective term
([kinetic-energy preservation](/properties/kinetic-energy-preservation.md);
Fang et al. 2025, §2.1), an over-dissipative second derivative (the
implicit SVV above), or an explicit compact filter (below).

## Compact filters

A compact low-pass filter solves the same kind of system for the filtered
values $\phi^{\mathrm f}_i$:

$$\alpha_{\mathrm{cf}}\phi^{\mathrm f}_{i-1}+\phi^{\mathrm f}_i+\alpha_{\mathrm{cf}}\phi^{\mathrm f}_{i+1}=\sum_{n=0}^{4}\frac{a_n}2(\phi_{i+n}+\phi_{i-n}),$$

the eighth-order filter of Gaitonde & Visbal as printed by Kang & Lee
(2024), Eq. (9), with $a_0=(93+70\alpha_{\mathrm{cf}})/128$,
$a_1=(7+18\alpha_{\mathrm{cf}})/16$, $a_2=(-7+14\alpha_{\mathrm{cf}})/32$,
$a_3=(1-2\alpha_{\mathrm{cf}})/16$, $a_4=(-1+2\alpha_{\mathrm{cf}})/128$
and $-0.5<\alpha_{\mathrm{cf}}\le0.5$, less filtering as
$\alpha_{\mathrm{cf}}\to0.5$. Kang & Lee apply it with
$\alpha_{\mathrm{cf}}=0.47$ at every final Runge–Kutta stage and drop to a
second-order filter with $0.49$ at shocks flagged by a Ducros-type
[sensor](/definitions/shock-sensor.md), adding localized
[artificial diffusivity](/methods/artificial-viscosity-shock-capturing.md).
The full description of their scheme, with the check that the filter's
transfer function is one at zero wavenumber and zero at the grid Nyquist
wavenumber, is on
[low-dissipation low-dispersion schemes](/methods/low-dissipation-low-dispersion-scheme.md),
which also records the fourth-order compact filter ($\alpha_{\mathrm{cf}}=0.495$)
that Bernades et al. (2023) compare for real-gas flow. In the supersonic
Taylor–Green code comparison of
[Chapelier et al. (2024)](/sources/chapelier-2024.md) the NS3D solver runs
sixth-order compact differences with a tenth-order compact filter and no
shock capturing; replacing the compact derivatives by explicit
fourth-order ones in post-processing changes the solenoidal dissipation
by up to 5% (§III.B.d).

**Origin of the compact filters.** Lele (1992, App. C.2, Eqs. C.2.1–C.2.8)
builds the filters the same way as the derivatives: a pentadiagonal left
side (coefficients $\alpha_{\mathrm{cf}}$ and a second one at $i\pm2$) and
a seven-point symmetric right side, with transfer function
$$\hat G(kh)=\frac{a_0+a_1\cos(kh)+a_2\cos(2kh)+a_3\cos(3kh)}{1+2\alpha_{\mathrm{cf}}\cos(kh)+2\beta_{\mathrm{cf}}\cos(2kh)}$$
in the notation above ($\beta_{\mathrm{cf}}$ page-local; Eq. C.2.2),
required to vanish at $kh=\pi$, which also makes its slope vanish there,
optionally with vanishing second and fourth derivatives at $\pi$ for a
flatter cut. With $\beta_{\mathrm{cf}}=a_3=0$ the fourth-order family
(C.2.4) is the tridiagonal filter
$a_0=\tfrac18(5+6\alpha_{\mathrm{cf}})$,
$a_1=\tfrac12(1+2\alpha_{\mathrm{cf}})$,
$a_2=-\tfrac18(1-2\alpha_{\mathrm{cf}})$ *(compiler check, not in the
sources: the printed three-parameter coefficients at the stated zero
values)*, whose transfer function is one at $kh=0$ and zero at $kh=\pi$
for every $\alpha_{\mathrm{cf}}$; these are the coefficients
Bernades et al. (2023, Eq. 29) print for the fourth-order filter they run
with $0.495$ *(compiler check, not in the sources)*. Lele finds the tridiagonal compact
filters "much better low pass filters" than explicit second-, fourth- and
sixth-order ones, the filtering being confined to shorter waves as
$\alpha_{\mathrm{cf}}$ approaches 0.5 (Fig. 19 shows 0.4, 0.45, 0.475).
Two pentadiagonal filters place the cut-off by prescribing
$\hat G=0.95$ and 0.5 at two wavenumbers (Eqs. C.2.9–C.2.10), and
explicit fourth-order one-sided filters that remove the $kh=\pi$ wave
close the system at the first three nodes (Eq. C.2.11). Lele proposes
this "spectral-like filtering" against aliasing on non-periodic domains
(§3.1). Compact filters used as the closure of
under-resolved LES are on
[explicit modal filtering](/methods/explicit-modal-filtering.md).

**A one-parameter Padé filter as the LES model.** In the LES of
compressible round jets of [Rahatgaonkar & Ghosh (2025)](/sources/rahatgaonkar-2025.md),
§II B, Fig. 1, the filter of the single-step approximate-deconvolution
method is, in the periodic azimuthal direction, the Padé filter with
transfer function
$$\hat G(\omega)=\Big(\alpha_{\mathrm{cf}}+\tfrac12\Big)\frac{1+\cos\omega}{1+2\alpha_{\mathrm{cf}}\cos\omega},\qquad \alpha_{\mathrm{cf}}=0.2,$$
on the scaled wavenumber $\omega\in[0,\pi]$ ($\omega$ page-local here,
not the specific dissipation rate), with an explicit physical-space filter
of similar spectral behaviour in the non-periodic directions (after Stolz,
cited). It equals one at $\omega=0$ and zero at $\omega=\pi$ for any
$\alpha_{\mathrm{cf}}\neq-\tfrac12$ *(compiler check, not in the
sources)*. The filter is composed with the van Cittert approximate inverse
($N_{\mathrm{AD}}=6$ terms, registry §11) and applied twice per time step,
$(Q_N*G)^2$; the authors show that the transfer functions of $Q_N*G$ and
$(Q_N*G)^2$ decay smoothly to zero at high wavenumber. The method is on
[scale-similarity model](/methods/scale-similarity-model.md).

## Use in turbulence simulation

- **Incompressible DNS and implicit LES (Xcompact3d).** Sixth-order
  compact differences on a Cartesian mesh (optionally stretched in $y$),
  third-order Runge–Kutta or Adams–Bashforth time stepping, an FFT
  Poisson solver on a half-staggered mesh and a 2D pencil decomposition;
  Fang et al. (2025) add an MHD module to it and validate it on
  Orszag–Tang vortices and Hartmann channel flow, and Yan et al. (2024)
  run implicit-SVV LES with a wall-modelled immersed boundary in it. On a
  circular cylinder at $Re_D=3.9\times10^3$ the sixth-order scheme with
  implicit SVV gives $C_D=1.02$ and a recirculation length $1.42D$
  against 1.17 and $2.42D$ for second-order central differences with the
  [Smagorinsky model](/methods/smagorinsky-model.md) on the same mesh, at
  lower cost (Yan et al., §III A, Table II). Code details are on
  [Xcompact3d](/software/xcompact3d.md).
- **Compressible DNS with shocks.** Kang & Lee (2024) stabilize their
  curvilinear compact scheme by filtering and artificial diffusivity for
  a Mach 2.9 compression-ramp interaction (see
  [shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)).
  The reference DNS of [Zhang et al. (2022b)](/sources/zhang-2022-f.md),
  §III, and [Zhang et al. (2022d)](/sources/zhang-2022-h.md), §III A,
  instead switch between eighth-order compact differences in smooth
  regions (Lele's scheme, as the latter cites) and seventh-order WENO
  in shock regions (see
  [WENO](/methods/weno-scheme.md)).
- **LES of compressible round jets.** Rahatgaonkar & Ghosh (2025), §II A,
  compute all spatial derivatives of a characteristic (Sesterhenn) form of
  the compressible Navier–Stokes equations in cylindrical coordinates with
  Lele's sixth-order compact central differences, a low-storage
  third-order Runge–Kutta scheme and the Mohseni–Colonius axis treatment,
  on $512\times128\times120$ points over $60r_0\times20r_0$ ($r_0$ the
  inflow jet radius, page-local) at $Re=5\times10^5$; azimuthal spectra
  at $x/r_0=30$–50 decay at the highest resolved wavenumbers with a short
  $k^{-5/3}$ segment, which they take as evidence that grid and LES
  approach are adequate (§II D, Fig. 3). Results are on
  [turbulent round jet](/benchmarks/turbulent-round-jet.md).
- **Reference DNS and alternatives in shock-capturing studies.** The
  Taylor–Green DNS of Dairay et al. used as reference by
  [Kokkinakis & Drikakis (2025)](/sources/kokkinakis-2025.md), §III F
  ($512^3$), is a sixth-order compact computation, and the authors cite
  compact schemes (Lele) and hybrid compact–WENO schemes (Pirozzoli) as
  near-spectral alternatives to WENO (§I). The review of
  shock–turbulence interaction of [Cuadra et al. (2025)](/sources/cuadra-2025.md),
  §III A 1, lists compact schemes (Lele 1992) next to skew-symmetric
  central ones as smooth-region schemes of shock-capturing hybrids.
- **Compact nonlinear interpolation.** The weighted compact nonlinear
  scheme of [Ma et al. (2022)](/sources/ma-2022.md) makes a seventh-order
  tridiagonal compact interpolation nonlinear, so that the system
  decouples at discontinuities (see
  [weighted compact nonlinear schemes](/methods/weighted-compact-nonlinear-scheme.md)).

## Qualifications

- **Stability at high speed.** [Akbarzadeh & Borazjani (2025)](/sources/akbarzadeh-2025.md),
  §1, state that non-dissipative schemes, central and compact, "are
  unconditionally unstable" for high-speed flows governed by hyperbolic
  equations, which motivates their central/WENO hybrid; the claim is
  stated, not shown. The compact compressible solvers above are printed
  with filtering and artificial diffusivity (Kang & Lee, §II.B) or with
  WENO switching (Zhang et al. 2022b, 2022d), not as bare central compact
  schemes.
- **Printed slip (Kang & Lee 2024).** Eq. (8) prints the second
  right-hand-side term as $b_{\mathrm c}(\phi_{i+2}-\phi_{i-2})/(6h)$; with
  the printed $\alpha_{\mathrm c}=\tfrac13$, $a_{\mathrm c}=\tfrac{14}9$,
  $b_{\mathrm c}=\tfrac19$ the scheme is consistent only with the
  denominator $4h$ printed by Yan et al. (for $\phi=x$ the left side is
  $\tfrac53$, the right side $\tfrac{14}9+\tfrac19\cdot\tfrac46=\tfrac{44}{27}$
  as printed) *(compiler check, not in the sources)*.
- **Printed slip (Yan et al. 2024).** Eq. (A1) prints the mid-point
  interpolation with
  $\tfrac34\,\frac{\phi_{i+1}+\phi_i}2+\tfrac1{20}\,\frac{\phi_{i+2}+\phi_{i-1}}2$
  on the right; for a constant the right side is then $0.8$ against $1.6$
  on the left, half of Fang et al.'s consistent form
  *(compiler check, not in the sources)*.
- **Equation 16 of Fang et al. (2025)** applies the mid-point
  interpolation along $y$ to $x$-derivatives already at half nodes in $x$;
  the coefficients are those of the plain interpolation above.
- **Stability statement against Lele's analysis.** Akbarzadeh &
  Borazjani's statement concerns high-speed hyperbolic flows; Lele (1992,
  §4.5) shows linear semi-discrete stability of compact schemes with
  boundary closures for scalar advection, and restricts the bare schemes
  to flows whose smallest scales are "determined *physically and not
  numerically*" (§5).
- **Member (d) of Lele's Table IV is printed two ways.** The text (§3.1)
  names the fourth-order tridiagonal member that beats the sixth-order
  one "$\alpha=\tfrac3{14}$", the Fig. 2 caption $\alpha=\tfrac5{14}$;
  Table IV gives it $e_{\mathrm r}=0.74$, 0.59, 0.52. From Eq. (2.1.6)
  and the modified wavenumber, $\alpha_{\mathrm c}=\tfrac5{14}$ gives 0.743
  and 0.595 at $\epsilon_{\mathrm r}=0.1$ and 0.01, and
  $\alpha_{\mathrm c}=\tfrac3{14}$ gives 0.562, 0.327, 0.186, below the Padé
  scheme; at $\epsilon_{\mathrm r}=0.001$ the $\tfrac5{14}$ member exceeds
  the tolerance briefly near $kh\approx1.3$, so that the first
  wavenumber at which the tolerance is exceeded gives 0.32, and 0.52 only
  if that excursion is disregarded *(compiler check, not in the
  sources)*. The paper does not say how such excursions are counted.
- **Maximum modified wavenumbers (Lele 1992, §4.6).** The list for the
  first-derivative schemes of Fig. 1 has nine values for ten curves,
  without the spectral-like scheme, for which the printed coefficients
  give $(k'h)_{\max}=2.635$; for the spectral-like second-derivative
  scheme the list prints 9.108, while Eq. (4.6.5),
  $(k''h^2)_{\max}=4(a_{\mathrm c}+c_{\mathrm c}/9)/(1-2\alpha_{\mathrm c}+2\beta_{\mathrm c})$,
  with the printed coefficients (3.1.12) gives 8.779, the maximum being
  at $kh=\pi$ *(compiler check, not in the sources)*. The other printed
  values ($\sqrt3$ for Padé, 1.989 for the sixth-order tridiagonal scheme)
  are reproduced by the same formulas.
- **Filter wording (Lele 1992, App. C.2).** The text says the filtering
  is confined to shorter waves "by reducing the coefficient $\alpha$
  towards 0.5", while the values of the Fig. 19 caption, 0.4, 0.45,
  0.475, increase towards 0.5.

# Citations

- [Lele (1992)](/sources/lele-1992.md) — §1 (motivation, resolution against formal order); §2.1–2.2, Eqs. (2.1)–(2.2.11), Tables I–II (first- and second-derivative families up to tenth order, Padé connection, footnote 1); §3.1, Eqs. (3.1.3)–(3.1.13), Tables III–V, Figs. 1–5 (modified wavenumber, resolving efficiency, spectral-like schemes, phase speed, anisotropy, aliasing); §4.1–4.6, Eqs. (4.1.1)–(4.6.5), Figs. 6–10 (boundary closures, global conservation, tests, eigenvalue stability, time-step limits); §5, Figs. 11–13 (no built-in dissipation, viscous terms, non-monotonicity, mixing layer, shock structure); App. A–C, Eqs. (B.1.1)–(B.1.2), (C.1.4), (C.2.1)–(C.2.11), Figs. 16–19 (higher derivatives, cell-centred derivatives, interpolation, filters).
- [Yan et al. (2024)](/sources/yan-2024.md) — App. A1, Eqs. (A1)–(A3) (sixth-order compact interpolation, first and second derivatives); App. B1 (nine-point second derivative of the implicit SVV); §III A, Table II (sixth-order compact against second-order central).
- [Fang et al. (2025)](/sources/fang-2025.md) — §2.1 (skew-symmetric convection); §2.2 (magnetic correction); §2.3, Eqs. (14)–(16) (staggered derivative, mid-point interpolation, FFT Poisson solver, divergence to machine accuracy).
- [Kang & Lee (2024)](/sources/kang-2024.md) — §II.B, Eqs. (8)–(9) (sixth-order compact first derivative on curvilinear grids, eighth-order compact filter, adaptive shock filter).
- [Kim & Leonard (2024)](/sources/kim-2024-b.md) — §4.8 (compact schemes developed to minimize dispersion error; historical).
- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §5.1 (sixth-order compact second derivative tuned as implicit SVV).
- [Caban et al. (2026)](/sources/caban-2026.md) — §3.2, Eqs. (34)–(35); §4.1, Fig. 5a (filters induced by compact derivatives and interpolations).
- [Chapelier et al. (2024)](/sources/chapelier-2024.md) — HAL hal-04582857v1: §III.B.d (NS3D: sixth-order compact differences with a tenth-order compact filter).
- [Zhang et al. (2022b)](/sources/zhang-2022-f.md) — §III (compact/WENO hybrid of the reference DNS).
- [Zhang et al. (2022d)](/sources/zhang-2022-h.md) — §III A (compact/WENO hybrid of the reference DNS).
- [Ma et al. (2022)](/sources/ma-2022.md) — §2.2 (nonlinear tridiagonal compact interpolation).
- [Akbarzadeh & Borazjani (2025)](/sources/akbarzadeh-2025.md) — §1 (central and compact schemes stated unstable for high-speed flows).
- [Rahatgaonkar & Ghosh (2025)](/sources/rahatgaonkar-2025.md) — §II A (sixth-order compact differences in cylindrical coordinates); §II B, Fig. 1 (Padé filter $\alpha_{\mathrm{cf}}=0.2$ inside single-step ADM); §II D, Fig. 3.
- [Kokkinakis & Drikakis (2025)](/sources/kokkinakis-2025.md) — §I (compact and compact–WENO schemes cited); §III F (compact reference DNS; passing).
- [Cuadra et al. (2025)](/sources/cuadra-2025.md) — §III A 1 (compact schemes as smooth-region schemes in shock–turbulence simulation; review, passing).
