---
type: Method
title: "Spectral vanishing viscosity"
description: "Spectral vanishing viscosity concentrates an added viscosity on the highest resolved scales. The sources use an implicit finite-difference form, an explicit modal filter on a DG artificial flux made entropy stable, and a modal SVV in continuous spectral/hp elements; all serve as LES closures, and one source measures how little of the dissipation the SVV term itself supplies."
status: established
aliases: [SVV, implicit SVV, ISVV, implicit spectral vanishing viscosity, spectral viscosity, SVV-LES, entropy-stable SVV, modal SVV filter]
tags: [les, implicit-les, numerical-dissipation, sgs-model, dg, entropy-stable]
timestamp: 2026-10-29T07:40:00Z
---

# Spectral vanishing viscosity

**Spectral vanishing viscosity (SVV)** adds a viscosity that is small or
zero at large scales and acts mainly near the resolution limit.
[Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md) (§4) trace it to
Tadmor's analysis of the Burgers equation, which they cite. The sources
use it in two different constructions:

- **implicit SVV** ([Vicente Cruz & Lamballais 2023](/sources/vicentecruz-2023.md)):
  no term is added; the viscous-term finite-difference scheme is tuned so
  that its modified wavenumber over-dissipates near the mesh cutoff $k_c$;
- **explicit modal SVV** (Mateo-Gabín et al. 2022): an artificial viscous
  flux is added to a discontinuous Galerkin spectral element scheme and
  weighted, mode by mode in the Legendre basis of each element, by a filter
  kernel that grows with the mode index.

A third construction, a modal SVV term in continuous spectral/hp
element codes (Karamanos & Karniadakis, cited), is used by
[Saini et al. (2023)](/sources/saini-2023.md) and
[Slaughter et al. (2023)](/sources/slaughter-2023.md) in
[Nektar++](/software/nektar-plus-plus.md) (section below).
All act as an [implicit](/definitions/implicit-les.md) or mixed LES
closure; the explicit DG form is also used for shock capturing. The kernel,
the parameters and the evidence differ, so the three are kept apart below.

## Classical form

Mateo-Gabín et al. (2022, §4, Eqs. 65–67) cite Tadmor's SVV for the
Burgers equation,

$$\partial_tu+\tfrac12\partial_x(u^2)=\epsilon_N\,\partial_x\big[\mathcal F\star\partial_xu\big],\qquad \epsilon_N\sim\frac1{N^\beta\log N},\ \beta<1,$$

with $\mathcal F\star$ a spectral filter whose coefficients $\varphi_k$
(page-local) vanish below a cutoff mode $M$ (page-local). They cite two
kernels: the step $\varphi_k=0$ for $k\le M$, 1 for $k>M$; and the smooth
kernel of Maday et al. and Kaber, $\varphi_k=\exp[-(k-N)^2/(k-M)^2]$ for
$k>M$, with $M\approx5\sqrt N$. The authors recall SVV for under-resolved
turbulence (Karamanos & Karniadakis; Kirby & Sherwin) and its combination
with LES (SVV-LES; Kirby & Karniadakis; Pasquetti et al.).

## Implicit SVV (finite differences)

In the form used by Vicente Cruz & Lamballais (2023, §5.1), after Lamballais
et al. and Dairay et al. (cited), no term is added to the equations.
Instead, the coefficients of the sixth-order compact second-derivative
scheme of the viscous term are chosen so that its modified square
wavenumber $k''_i(k_i)$ (page-local) exceeds $k_i^2$ near $k_c$ while the
scheme keeps sixth-order accuracy. The resulting one-dimensional spectral
viscosity is (Eq. 30)

$$\frac{\nu''(k_i)}{\nu}=\frac{k''_i(k_i)}{k_i^2}-1 ,$$

which vanishes for $k_i\ll k_c$ because $k''_i\approx k_i^2$ there. Its
main parameter is $\nu_0=\nu''(k_c)$ (page-local), quoted as $\nu_0/\nu$
and constant in space; the sharpness of the kernel is set by imposing its
value at $k=2k_c/3$. The dissipation is hyperviscous and linear, and comes
only from the discrete differentiation, which is why the authors classify
it as [implicit LES](/definitions/implicit-les.md).

### Choosing $\nu_0$

Following Dairay et al. (cited), $\nu_0$ is set by a Pao-like spectral
closure (§5.2, Eqs. 31–36). Pao's equilibrium $T(k)=\varepsilon(k)$ is
written with the modified wavenumber, a Pao-type ODE is integrated for the
kernel, and $\nu_0$ is chosen so that the LES spectrum at $k_c$ equals the
DNS spectrum at the DNS-mesh cutoff $k_d$. Vicente Cruz & Lamballais (§5.3,
Eqs. 37–42) show that the three-dimensional $k''=\sum_jk''_j$ depends on
the wavevector, not only on $|\boldsymbol k|$: it is largest along the mesh
axes and smallest along the diagonals (Fig. 1, $\nu_0/\nu=100$). Using the
shell average $\langle k''\rangle(k)$ instead of the one-dimensional kernel
roughly doubles the predicted value: $\nu_0/\nu=181$ and 700 for
$k_d/k_c=10$ and 25, against 92 and 355 from the isotropic version. The
authors argue that the anisotropy of the dissipation is an asset, because
convective differentiation errors are also largest along the axes. In the
simulations, kinetic energy and SVV anisotropies are anticorrelated, so the
effective viscosity is below the shell-average estimate for $k\gtrsim k_c/2$
(§6.4).

### Results

On the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at
$Re=40\,000$ (DNS $5400^3$; LES $216^3$ and $540^3$), §6.4:

- SVV damps the spectrum for $k_c/2\lesssim k\lesssim k_c$, prevents the
  thermalization of no-model LES, reduces the spectral error for
  $k\lesssim k_c/2$ compared with Smagorinsky and captures the dissipation
  peak of the breakdown (Figs. 13–14);
- at fixed filter scale, runs with $\Delta=\Delta x$ and $\Delta=2.5\Delta x$
  are "virtually identical" (data not shown), so SVV LES is numerically
  converged in what the authors call the standard condition
  $\Delta=\Delta x$, unlike [Smagorinsky](/methods/smagorinsky-model.md);
- its effective filter is approximated by the super-Gaussian
  $\exp(-k^6\Delta^6/256)$, with a bump peaking near $k_c/4$: a
  **bottleneck**, i.e. a soft pile-up below $k_c/2$ that the authors call
  the main drawback of the method (Fig. 15, Eq. 50);
- its [spectral eddy viscosity](/methods/spectral-eddy-viscosity.md)
  reproduces the a priori cusp but vanishes at low $k$, where the a priori
  plateau carries up to 24% of the dissipation (Figs. 16–18).

Adding Smagorinsky ($C_s=0.1$ or 0.18) to SVV restores a plateau and
reduces ($C_s=0.1$) or removes ($C_s=0.18$) the bottleneck, but does not
improve the total dissipation. As $C_s$ goes from 0.18 to 0, SVV takes over
the missing explicit dissipation automatically (§6.5, Figs. 20–22).

In turbulent pipe flow on a Cartesian mesh with an immersed boundary,
$\nu_0/\nu=234$ at $\Delta x^+=\Delta y^+\approx9$ gives $u_\tau$ within
1.8% at $Re_\tau=1000$ and about 1.9% at $Re_\tau=2000$, with realistic
mean and normal-stress profiles. The authors argue that, because $\nu_0$
is constant and scale-selective, the near-wall large scales are unaffected
without any wall correction, and call this an "augmented wall-resolving"
property.
At $\Delta x^+=18$ ($\nu_0/\nu=756$) $u_\tau$ is underpredicted by more
than 12%, so SVV "cannot be used alone in the context of WMLES"
(§7.2–7.4).

### Closed-form coefficients, and use with an immersed-boundary wall model

[Yan et al. (2024)](/sources/yan-2024.md), App. B1, Eqs. (B1)–(B8), print
the scheme that produces the implicit SVV, the
[compact](/methods/compact-finite-difference-scheme.md) second derivative
on a stencil of three to nine nodes,

$$\alpha_{\mathrm c}\phi''_{i-1}+\phi''_i+\alpha_{\mathrm c}\phi''_{i+1}=a_{\mathrm c}\frac{\phi_{i+1}-2\phi_i+\phi_{i-1}}{h^2}+b_{\mathrm c}\frac{\phi_{i+2}-2\phi_i+\phi_{i-2}}{4h^2}+c_{\mathrm c}\frac{\phi_{i+3}-2\phi_i+\phi_{i-3}}{9h^2}+d_{\mathrm c}\frac{\phi_{i+4}-2\phi_i+\phi_{i-4}}{16h^2}$$

(registry-§11 compact coefficients $\alpha_{\mathrm c}$, $a_{\mathrm c}$,
$b_{\mathrm c}$, page-local $c_{\mathrm c}$, $d_{\mathrm c}$; the source's
$\alpha_f$, which is not the registry's modal-filter strength),
with modified square wavenumber

$$k''(k)\,h^2=\frac{2a_{\mathrm c}[1-\cos(kh)]+\tfrac{b_{\mathrm c}}2[1-\cos(2kh)]+\tfrac{2c_{\mathrm c}}9[1-\cos(3kh)]+\tfrac{d_{\mathrm c}}8[1-\cos(4kh)]}{1+2\alpha_{\mathrm c}\cos(kh)} .$$

Five Taylor conditions give a unique tenth-order scheme, three give the
sixth-order family (Eq. A3 is one member), and the two remaining degrees
of freedom fix $k''$ at $k_c=\pi/h$ and at $k_m=\tfrac23k_c$ so that
$k''=(1+\nu_{\mathrm{SVV}}/\nu)k^2$ there, with the kernel

$$\nu_{\mathrm{SVV}}(k)=\begin{cases}0,&k<0.3k_c,\\ \nu_0\exp\Big[-\Big(\dfrac{k_c-k}{0.3k_c-k}\Big)^2\Big],&0.3k_c\le k<k_c\end{cases}$$

(Eqs. B3–B7). The coefficients are then explicit rational functions of
$k''(k_c)h^2$ and $k''(k_m)h^2$ (Eq. B8). With the printed B8 the
modified wavenumber equals $k^2$ up to terms of order $h^6$ and takes the
two imposed values exactly *(compiler check, not in the sources)*. The
scheme applied to the viscous term "constitutes the iSVV model", with the
single parameter $\nu_0/\nu$, whose preliminary values come from the
Pao-like procedure of Dairay et al. described above (as cited).

Yan et al. run it in [Xcompact3d](/software/xcompact3d.md) with a
wall-modelled diffused-interface
[immersed boundary](/methods/immersed-boundary-method.md) and
$\nu_0/\nu=15$ (circular cylinder, $Re_D=3.9\times10^3$), 300 (circular
cylinder, $Re_D=1.4\times10^5$), 80 (square cylinder, $Re_D=2.2\times10^4$)
and 120 (flat roof, $Re_H\approx2\times10^4$) (§III). At $Re_D=3.9\times10^3$
on one $801\times387\times40$ mesh, the sixth-order scheme with iSVV gives
$C_D=1.02$, rms lift 0.113, recirculation length $1.42D$, base suction
0.93 and $St=0.229$, against 1.17, 0.017, $2.42D$, 0.59 and 0.223 for a
second-order central scheme with the [Smagorinsky model](/methods/smagorinsky-model.md)
on the same mesh (Table II), and costs 15.04 against 18.16 wall-clock
hours per $10^5$ steps on 96 cores, because no subgrid term is computed
explicitly (§III A). The iSVV is stated to be inapplicable to the
second-order scheme (App. B2). Wake spectra follow the $-5/3$ slope
(Fig. 5), which the authors relate to earlier iSVV validations on the
Taylor–Green vortex and wind-turbine wakes (as cited). The wall-model
results are on [wall-modelled LES](/methods/wall-modelled-les.md) and the
[circular-cylinder wake](/benchmarks/circular-cylinder-wake.md).

## Explicit modal SVV in DG, made entropy stable

Mateo-Gabín et al. (2022) build an SVV for the Gauss–Lobatto
[discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
that is provably entropy stable at the semi-discrete level.

**Artificial flux.** An artificial dissipative flux is added to the
compressible Navier–Stokes equations (§2, Eqs. 8–14), in two variants: the
Navier–Stokes viscous flux with an artificial viscosity $\mu_a$
(page-local), and the Guermond–Popov regularization flux, which adds a
density diffusion with coefficient $\mu_\rho$ (page-local; the paper's
$\alpha_a$) carried consistently into momentum and energy, plus a
viscosity $\mu_a$. Each is written as a symmetric positive semi-definite
matrix $\mathcal B$ times the gradient of entropy variables $\boldsymbol\psi$
(page-local), for two entropies: the kinetic energy $\rho\lvert\boldsymbol u\rvert^2/2$,
for [kinetic-energy-preserving](/properties/kinetic-energy-preservation.md)
split forms, and the thermodynamic entropy $-\rho s/(\gamma-1)$, for
entropy-stable split forms. The local dissipation
$(\nabla\boldsymbol\psi)^T\mathcal B\nabla\boldsymbol\psi$ is then
non-negative (§2.1–2.2). For the Navier–Stokes flux in kinetic-energy
variables it is $\mu_a\big(2S_{ij}S_{ij}-\tfrac23(\nabla\cdot\boldsymbol u)^2\big)=2\mu_aS^d_{ij}S^d_{ij}\ge0$
(Eq. 25; right-hand form *(compiler check, not in the sources)*). The authors give the Cholesky decomposition of the Guermond–Popov
matrix in thermodynamic entropy variables, with a non-negative diagonal
whenever $\rho,p\ge0$ (§2.2.3, Eqs. 28–30; App. D).

**Filter placement.** The SVV filters this flux modally, with Legendre
kernel coefficients $\varphi_j\ge0$ (§4.1). A filter applied naively to
$\mathcal B\nabla\boldsymbol\psi$ need not keep the dissipation
non-negative; the authors place it "in the middle" of a symmetric
factorization (§5, Eqs. 101–102). For $\mathcal B=a\,\mathcal C$ with a
scalar $a\ge0$ (page-local) and a constant matrix $\mathcal C$,

$$\boldsymbol F^{\mathcal F}=\sqrt{\frac aJ}\;\mathcal C\;\mathcal F\star\big(\sqrt{Ja}\,\nabla\boldsymbol\psi\big),$$

and for a general $\mathcal B=\mathcal L^T\Lambda\mathcal L$ (Cholesky,
$\Lambda$ diagonal, both page-local)

$$\boldsymbol F^{\mathcal F}=\frac1{\sqrt J}\,\mathcal L^T\Lambda^{1/2}\;\mathcal F\star\big(\sqrt J\,\Lambda^{1/2}\mathcal L\,\nabla\boldsymbol\psi\big),$$

with $J$ the element Jacobian. The filtered flux replaces the artificial
flux in volume and surface terms.

**Stability.** The proof rests on three properties of the Legendre
transforms on Gauss–Lobatto nodes (§4.1, Eqs. 72–84): the nodal-to-modal
and modal-to-nodal matrices are mutual inverses, a discrete Parseval
identity $\sum_iw_iU_iV_i=\sum_j\|L_j\|_N^2u_jv_j$ ($u_j$, $v_j$ the modal
coefficients, page-local), and (Theorem 1)

$$\langle Q,\mathcal F\star Q\rangle_N=\sum_j\|L_j\|_N^2\,\varphi_j\,q_j^2\ge0$$

for non-negative kernel coefficients, extended to tensor-product elements
(Theorem 2, Property 4). With BR1 interface fluxes the interior-face terms
of the filtered flux vanish, and so do the adiabatic-wall terms with the
paper's boundary treatment. The semi-discrete scheme is entropy stable for
the thermodynamic entropy, and kinetic-energy stable up to the
pressure-work term, which cannot be bounded (§5.1, Eqs. 109–118). The
authors say Lundquist & Nordström reached a similar conclusion with a
kernel $J^{-1/2}\mathcal F J^{1/2}$, and that, unlike the earlier
Smagorinsky-SVV of Manzanero et al. (same group), the new approach is
entropy stable (§5.1, §7).

**Kernels.** The 1D kernel is $\varphi_i=(i/N)^{P_{\mathrm{SVV}}}$ after
Moura et al. ($P_{\mathrm{SVV}}$ page-local); $P_{\mathrm{SVV}}=0$ recovers
the unfiltered viscous operator, and only $\mu_a=0$ removes the viscosity
(§5.2, Eq. 122). Two 3D kernels are built from it: the high-pass product
$\varphi_{ijk}=\varphi_i\varphi_j\varphi_k$ and the non-high-pass
$1-(1-\varphi_i)(1-\varphi_j)(1-\varphi_k)$ (Eqs. 97–98). The tensor form
is applied as three 1D matrix–vector products, which the authors state
reduces the cost from "$(N+1)^3$" to "$3(N+1)$" operations (Eqs. 95–96).
For $N=8$ and $P_{\mathrm{SVV}}=0.1$, $\varphi_1=(1/8)^{0.1}\approx0.81$
and $\varphi_8=1$ *(compiler check, not in the sources)*, so the kernel
differs from Tadmor's cutoff kernels, which vanish below $M$.

**Where it dissipates.** A von Neumann (eigensolution) analysis of 1D
advection–diffusion with $N=7$, upwind flux, BR1 and $\mu_a=0.01$
($P_{\mathrm{SVV}}=0$, 0.1, 1, 10) shows that the effect of
$P_{\mathrm{SVV}}$ is most evident at low wavenumbers, where the SVV
supplies almost all the dissipation; at other wavenumbers the added
viscosity is smaller than the Riemann-solver dissipation (§5.2, Figs. 2–3).
See [numerical dissipation](/properties/numerical-dissipation.md).

**LES results.** The SVV-LES uses the [Smagorinsky](/methods/smagorinsky-model.md)
viscosity, $C_s=0.2$, $\Delta^3=\mathrm{Vol}/(N+1)^3$, as $\mu_a$, filtered
by the high-pass kernel (§6.1, Eqs. 123–125). On the inviscid
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) with $8^3$
elements and $N=8$, the Pirozzoli kinetic-energy-preserving split form and
a low-dissipation Roe flux (Fig. 4):

- unfiltered Smagorinsky ($P_{\mathrm{SVV}}=0$) is excessively dissipative;
- $P_{\mathrm{SVV}}\approx0.1$ gives a spectrum close to $k^{-5/3}$ over
  most resolved wavenumbers at $t=20$; the SVV changes the highest modes
  little and acts on low-to-medium wavenumbers, avoiding a high-frequency
  pile-up;
- the dissipation rate is below that of the van Rees et al. reference
  ($768^3$) for the first five time units and comparable afterwards; that
  reference is a viscous simulation at $Re=1600$ whereas the test is
  inviscid.

The authors state that the SVV-LES "improves the results for a wide range
of values of the SVV exponent, reducing the impact of the choice of
$P_{\mathrm{SVV}}$" (§7).

**Shock capturing.** SVV alone does not control strong shocks. In the
Shu–Osher problem a density-gradient sensor switches to
$P_{\mathrm{SVV}}=0$ where it exceeds 10 and uses $P_{\mathrm{SVV}}=2$
elsewhere, with the SVV-filtered Guermond–Popov flux and Chandrashekar's
entropy-conservative split form; 50 and 100 elements ($N=5$, 8) reproduce
the flow features without most spurious oscillations (§6.2, Fig. 5). On the
Mach 3 forward-facing step (3653 unstructured quadrilaterals, $N=7$) the
main shock is captured within one element (§6.3, Figs. 6–7, qualitative).
Appendix A states that $P_{\mathrm{SVV}}=O(1)$ suits supersonic flows and
that turbulent cases need $P_{\mathrm{SVV}}\approx O(10^{-2})$ "even without
the help of the LES approach", and that no systematic strategy for choosing
$P_{\mathrm{SVV}}$ exists: the admissible range is found by trial and error
(Fig. 8). The shock-capturing family is contrasted with the
[subcell finite-volume](/methods/subcell-finite-volume-shock-capturing.md)
approach in the paper's introduction. The review of high-order
discontinuous schemes for multiphase flow of
[Lv & Ekaterinaris (2023)](/sources/lv-2023.md), §4.2, cites this
entropy-stable SVV as an instance of the "filtered forms" of artificial
viscosity that, with artificial viscosity proper, have become more
popular than limiting for LES with discontinuous schemes (see
[artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)).

## Modal SVV in continuous spectral/hp elements

**Form.** [Saini et al. (2023)](/sources/saini-2023.md) (§2.2, §2.3,
Eqs. 6–8, 13–15) write the SVV term of Nektar++'s incompressible solver,
after Karamanos & Karniadakis (cited), as
$\epsilon_{\mathrm{svv}}\partial_j\big(Q\star\partial_j\bar u_i\big)$, with
$Q\star$ a modal convolution and the amplitude and kernel of Moura et al.
(cited),

$$\epsilon_{\mathrm{svv}}=\epsilon_0\,U_l\,h/N,\qquad \hat Q(m)=(m/N)^{P_{\mathrm{SVV}}},\quad 0\le m\le N,$$

with $U_l$ a local advection speed, $h$ the element size (cube root of the
element volume), $N$ the polynomial degree, $m$ the mode index and
$\epsilon_0$, $P_{\mathrm{SVV}}$ parameters (page-local symbols; the
values are not printed, being referred to the authors' earlier paper). The
kernel has the same printed form, also after Moura et al., as the 1D
kernel of Mateo-Gabín et al. in DG above.

**Energy budget.** Multiplying by $\bar u_i$ splits the term into an SVV
dissipation $\int\epsilon_{\mathrm{svv}}(Q\star\partial_j\bar u_i)\,\partial_j\bar u_i\,dV$,
a surface flux and a term $\int\bar u_i(Q\star\partial_j\bar u_i)\,\partial_j\epsilon_{\mathrm{svv}}\,dV$
from the spatial variation of the amplitude, which they find below 5% of
the SVV dissipation (about 10% in one subdomain) and drop. They evaluate
the convolution by FFT on a three-times finer uniform grid with a Tukey
window and call this part of the procedure "less general and non-exact".

**How much the SVV term dissipates.** Measured against the residual of the
discrete resolved-energy budget (see [numerical dissipation](/properties/numerical-dissipation.md);
§5, Figs. 7–15), with polynomial degree 4 (nominally fifth order):

- Taylor–Green vortex at $Re=1600$, $8^3$ elements: the SVV term supplies
  10–20% of the non-viscous dissipation, the numerics the rest; its
  absolute dissipation is below the WALE dissipation of the $64^3$
  second-order finite-volume run;
- combustor port flow at $Re=2.25\times10^4$ (8.4 million points): the SVV
  share is about 20% (impingement region), 15% (recirculation zone) and
  44% (downstream), against about 10%, 8% and 20% for the
  [WALE](/methods/wale-model.md) share in the equal-cost second-order run;
  the total non-viscous dissipation of the high-order run is 40% and 25%
  lower in the first two regions, and its value normalized by the viscous
  dissipation is one-fifth in the third (§5.2).

The authors conclude that the accuracy-per-cost advantage of the high-order
solver comes mainly from its lower numerical dissipation, with the closure
(SVV or WALE) secondary (§6).

**SVV implicit LES with a wall model.** [Huang et al. (2022c)](/sources/huang-2022-c.md)
(§II B, Eqs. 8–13) restate the same lineage for Nektar++: Tadmor's Burgers
form with dissipation strength $\epsilon_N\approx N^{-1}$ in a Fourier
setting with $N$ modes, the kernel of Maday et al. acting on modes above
the cut-off $M\approx5\sqrt N$ with the same exponential form as above, and the Navier–Stokes form of Kirby & Sherwin,
an added term $\epsilon_{\mathrm{svv}}\partial_j\big(Q\star\partial_ju_i\big)$
on the incompressible momentum equation with no explicit subgrid model
(their "SVV-iLES"). They describe the "DG kernel" of Moura et al., a
kernel redesigned mode by mode so that continuous Galerkin with SVV
mimics the dissipation of upwind DG, calibrated by spatial eigenanalysis
([Tonicello et al. (2023)](/sources/tonicello-2023.md), §1, cite these
semi-discrete spatial analyses of Moura, Mengaldo and co-workers and
extend the analysis to a fully-discrete form, without discussing SVV; see
[eigensolution analysis](/methods/eigensolution-analysis.md)),
and cite Wang et al.'s (2021) finding that an optimized SVV implicit LES
does "at least as well as" a subgrid model in wall-resolved separated
flow. Their contribution is to replace the inner layer by an equilibrium
wall-stress model imposed as a Neumann condition, which they call the
first wall model for SVV implicit LES in a spectral/hp element method;
they argue that eddy-viscosity corrections of the wall model (Cabot &
Moin; Wu & Meyers, cited) do not apply to implicit LES and that the
Nek5000 framework of Pal et al. could not be coupled with SVV (§I,
stated, not demonstrated). On channel flow at $Re_\tau=550$, 950 and 2000
on one $12\times6\times10$-element mesh the mean velocity is within 2% at
950 and 5.4% at 2000 of DNS (§III B; wall-model results on
[wall-modelled LES](/methods/wall-modelled-les.md) and the
[spectral-element method](/methods/spectral-element-method.md)). Time
averaging of the wall-model input changes the results marginally
(§III D), the finding that Mukha et al. (below) cite as agreeing with
theirs. The kernel, the amplitude and the cut-off of their own runs are
not printed.

**SVV in one direction, gradient-jump penalty in the others.**
Slaughter et al. (2023) (§3.1, §3.6, Fig. 5) run a Fourier spectral/hp
implicit LES of a multi-element wing with polynomial degree 6, using SVV
with an exponential kernel (after Karniadakis & Sherwin, cited) only
in the Fourier direction, active on modes above the product of a cut-off
ratio and the polynomial order (ratio not printed), and the gradient-jump
penalty of Moura et al. in the plane. Relaying Moura et al., they state
that SVV at lower polynomial orders "can be overly diffusive, resulting in
a significant loss in resolution", and that the gradient-jump penalty "has
out-performed the SVV approach on canonical cases" (see
[jump-penalty stabilization](/methods/jump-penalty-stabilization.md)). The
spanwise modal energy falls to $10^{-7}$ before the SVV filter width,
which they read as evidence that further spanwise modes are not needed.
[Kou et al. (2023)](/sources/kou-2023.md) (§1) also recall SVV as an
alternative stabilization to interface penalties, complementary to the
Riemann-solver dissipation.

## SVV in the HORSES3D code

[Ferrer et al. (2023)](/sources/ferrer-2023.md), the software paper of
the [HORSES3D](/software/horses3d.md) DG code from the same group as
Mateo-Gabín et al., list both uses (§4.1, §4.4):

- **LES.** The SVV-Smagorinsky model (Manzanero et al., as cited) is
  offered with Smagorinsky, WALE and Vreman, with the stated property of
  keeping dissipation low in laminar flow while "providing the correct
  dissipation for all wave–number ranges in turbulent regimes"; among the
  [implicit-LES](/definitions/implicit-les.md) options, energy-stable split
  forms are combined with SVV. No equation or parameter is printed.
- **Shock capturing.** The artificial flux (Navier–Stokes or
  Guermond–Popov) is filtered by an SVV kernel in Legendre modal space,
  with the factorization $\mathcal B=\mathcal L^T\Lambda\mathcal L$ and
  the filter applied to "only one half" of the factorized flux (Eq. 18),
  the second formula above. A density-gradient sensor, the element integral
  of $J\lvert\nabla_\xi\rho\rvert^2$ (Eq. 19), adds unfiltered dissipation
  in troubled elements. The Mach 3 forward-facing step with 3653 elements
  and $N=7$ is shown (Fig. 9), adapted from the preprint of Mateo-Gabín et
  al., the same case as their §6.3.

The paper states that the approach "has proven to be useful for the
simulation of turbulent and supersonic flows", citing the group's work.

## Related constructions

- **A modal entropy correction contrasted with SVV.**
  [Alberti et al. (2025b)](/sources/alberti-2025-c.md), §II A 1,
  Eqs. (23)–(25), make a modal DG entropy conserving or entropy stable by
  a parameter-free element-wise correction (direct enforcement of the
  entropy balance, after Abgrall; on
  [entropy conservation](/properties/entropy-conservation.md)) whose
  amplitude is fixed by the entropy defect of the element and which is
  spread over all modal coefficients except the mean. They contrast it
  with SVV (Karamanos & Karniadakis, cited): SVV acts only at high
  wavenumbers, whereas their correction is "passive only at the first
  mode", and restricting it to the higher modes reduced the robustness of
  the solver in their experience (no data shown). The correction costs
  below 1% of the CPU time for $N\ge2$ (App. A, Table VI), and the
  authors state that it is "not designed to have shock-capturing
  capabilities" (§II A 1).
- [Flad & Gassner (2017)](/sources/flad-2017.md) (App. C) build a modal
  cusp eddy viscosity in DG polynomial space, acting through a high-pass
  filter on the gradients: like SVV it is concentrated at the highest
  resolved modes.
- [Beck & Kurz (2023)](/sources/beck-2023.md) (§III B) relate their
  element-wise quadratic Smagorinsky coefficient (RL-Quad) to spectral
  vanishing viscosity, but defined in physical rather than wavenumber
  space.
- **Modal solution filtering in flux reconstruction.**
  [Wang (2024)](/sources/wang-2024-b.md) stabilizes a DG-recovering
  [flux-reconstruction](/methods/flux-reconstruction.md) implicit LES of
  turbine cascades with the exponential modal filter of Hesthaven &
  Warburton (cited), with modal weights
  $\exp\{-\alpha_f[(\vartheta_m-\vartheta_c)/(1-\vartheta_c)]^{s_f}\}$
  above a cutoff $\vartheta_c$ of the normalized mode index $\vartheta_m$
  ($\alpha_f=36$, $s_f=6$, registry §11 shared symbols; the source's $\eta$, $\eta_c$, $\alpha$, $s$;
  $\vartheta_c$ not printed), applied after every
  Runge–Kutta stage only in elements whose Persson–Peraire smoothness
  indicator exceeds a threshold (§2.3, Eqs. 17–19). Like SVV it damps only
  the highest modes, but as a filter on the solution rather than a
  viscous flux. The author recalls that Lamballais et al. connected
  solution filtering to SVV in finite differences and leaves the FR
  analogue to future work (§2.3, §5); filtering adds local dissipation to
  the numerical dissipation on which implicit LES relies, and may cause
  time inconsistency (§2.3, §5, citing Edoh et al.). The method and its
  thresholds are on the
  [subcell finite-volume shock-capturing](/methods/subcell-finite-volume-shock-capturing.md)
  and [DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md)
  pages.
- **Modal relaxation filter in continuous spectral elements.**
  [Mukha et al. (2025)](/sources/mukha-2025.md) (§II.A, §III.C, Fig. 8) use
  the high-pass relaxation term of [Nek5000](/software/nek5000.md) as an
  implicit subgrid model in
  [wall-modelled LES](/methods/wall-modelled-les.md). The term is a
  momentum source $\chi_f(\boldsymbol u-\boldsymbol u^{\mathrm{lp}})$, with
  $\boldsymbol u^{\mathrm{lp}}$ (page-local, as on the spectral-element page; the source writes $\tilde u$)
  the velocity low-pass filtered in each element's Legendre modal expansion
  and $\chi_f$ a constant filter strength (registry §11). Following
  Gillyns et al., they filter the two highest modes with $\chi_f=100$.
  - On the finest channel mesh at $Re_\tau\approx8000$ ($N=7$) the filter
    gives more near-wall oscillations and core velocity variance than the
    [Vreman](/methods/vreman-model.md) model, and it over-predicts
    $\langle u'u'\rangle$.
  - The wall stress computed from the mean wall gradient then misses the
    modelled stress by −84.85%.
  - The authors conclude that filtering alone "does not introduce enough
    damping to avoid the contamination of the solution with numerical
    artifacts".
  - Mukha et al. also cite (§I, §III.B.3) Huang et al., who ran
    wall-modelled LES with spectral vanishing viscosity and polynomial
    refinement in a spectral/hp-element code and found no significant
    effect of time-averaging the wall-model input; Mukha et al. state that
    this agrees with their a posteriori result.

- **Explicit filtering of the solution as an alternative to SVV.**
  [Ranjbar et al. (2026)](/sources/ranjbar-2026.md) (§I, §II.B) review SVV
  from Tadmor to Mateo-Gabín et al. and argue for filtering the DGSEM
  solution in modal space instead: SVV's extra flux "increases the
  mathematical complexity and alters the structure of the governing
  equations" and needs its own von Neumann and dispersion–dissipation
  analyses (citing Manzanero et al.; Moura et al.). Their kernel acts on
  three-dimensional modes grouped by the radius of the mode index, not on a
  tensor product of one-dimensional kernels as in SVV, and its cutoff
  changes in each element and time step with the ratio of grid spacing to
  Kolmogorov length and with strain and rotation, against the fixed cutoff
  $M=5\sqrt N$ of Karamanos & Karniadakis cited above and the fixed
  cutoffs of later SVV work. The construction and its results are on the
  [explicit modal filtering](/methods/explicit-modal-filtering.md) page.
- **Vanishing spectral eddy viscosity in pseudo-spectral LES.**
  [Rajek & Pozorski (2026)](/sources/rajek-2026.md) (§V) align their
  conclusion with the SVV and numerical-dissipation literature they cite
  (Tadmor; Karamanos & Karniadakis; Dairay et al.; Lamballais et al.):
  accurate large scales in forced isotropic turbulence need no viscosity at
  low wavenumbers, and a positive low-wavenumber plateau of a spectral eddy
  viscosity is "highly undesirable". Their adaptively determined
  [spectral eddy viscosity](/methods/spectral-eddy-viscosity.md) is
  zero in the forcing band and below a transition wavenumber
  $k_t\lesssim0.1k_c$, joined to the active range by a $\tanh$ step, and is
  regulated towards a model spectrum rather than prescribed (§IV,
  Eqs. 18–36). Unlike the constructions above it is applied to Fourier
  modes of a de-aliased pseudo-spectral code, not to a finite-difference or
  element discretization.
- [Caban et al. (2026)](/sources/caban-2026.md) (§1) list SVV among the
  ways of adding dissipation in implicit LES; their own implicit LES uses
  an explicit compact filter of approximate-deconvolution form applied to
  the velocity at every time step (see
  [explicit modal filtering](/methods/explicit-modal-filtering.md)).

## Qualifications

- The two constructions are not the same model: the implicit form is a
  scale-selective hyperviscosity of a finite-difference scheme with one
  parameter $\nu_0$, the explicit DG form a modal weighting of an
  artificial flux with an amplitude $\mu_a$ and an exponent. No source
  compares them.
- Vicente Cruz & Lamballais (2023) print Eq. (38) without the shell factor
  $4\pi k^2$ in the numerator and Eq. (39) without the factor $\nu$ of
  Eq. (37) *(compiler check, not in the sources)*. Their Fig. 16 legend
  cites Eq. (40) where the caption and text cite Eq. (42).
- Saini et al. (2023, §2.2) call $\epsilon_{\mathrm{svv}}$ "the maximum value
  of the artificial viscosity" while Eq. (14) makes it a local quantity
  proportional to $U_lh/N$, and write it $\epsilon_{\mathrm{svv}}$ and
  $\epsilon_{\mathrm{SVV}}$ for the same quantity.
- The SVV values for the two Taylor–Green resolutions are given in §5.3 and
  not restated in §6.
- Huang et al. (2022c, Eq. 11) print the Maday cut-off $M\approx5\sqrt N$
  of the Fourier setting; for $N<25$ it exceeds $N$, so that formula
  damps no mode below 25 modes *(compiler check, not in the sources)*.
  The paper does not state the kernel or cut-off used in its elemental
  runs, so this concerns the printed formula only.
- Mateo-Gabín et al. (2022) print the parameter of Tadmor's step kernel as
  "$\varepsilon M=0.25$" (Eq. 66), which is not explained; they print the
  forward-facing-step switching rule with the sensor $s_1$ although the
  sensor defined for that case is $s_2$ (§6.3, Eq. 128); they write $\mu_a$,
  $\alpha_a$ in the text and $\mu_\alpha$, $\alpha_\alpha$ in Table 1 and
  §6.3; and they call the Taylor–Green time units "seconds" (§6.1). The
  values of $\mu_a$ and of the density-diffusion coefficient for the
  Shu–Osher runs are not printed.

# Citations

- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §5.1, Eq. (30); §5.2, Eqs. (31)–(36); §5.3, Eqs. (37)–(42), Figs. 1–2; §6.4, Eq. (50), Figs. 13–18; §6.5, Figs. 20–22; §7.2–7.4, Figs. 25–28.
- [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md) — §1; §2, Eqs. (8)–(30); §4, Eqs. (65)–(100); §5, Eqs. (101)–(122), Figs. 2–3; §6.1, Eqs. (123)–(125), Fig. 4; §6.2–6.3, Eqs. (126)–(128), Figs. 5–7; §7; App. A, Fig. 8; App. D.
- [Flad & Gassner (2017)](/sources/flad-2017.md) — App. C.
- [Beck & Kurz (2023)](/sources/beck-2023.md) — §III B.
- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — §4.1; §4.4, Eqs. (15)–(19), Fig. 9.
- [Saini et al. (2023)](/sources/saini-2023.md) — §2.2, Eqs. (6)–(8), (10); §2.3, Eqs. (13)–(15); §5.1–5.2, Figs. 7–15; §6.
- [Slaughter et al. (2023)](/sources/slaughter-2023.md) — §3.1; §3.6, Fig. 5.
- [Huang et al. (2022c)](/sources/huang-2022-c.md) — §I (SVV implicit LES limited to moderate Reynolds numbers; wall-model coupling); §II B, Eqs. (8)–(13) (Tadmor, Maday kernel, Kirby–Sherwin form, DG kernel of Moura et al.); §III B, §III D (channel results, time-averaged input).
- [Kou et al. (2023)](/sources/kou-2023.md) — §1.
- [Wang (2024)](/sources/wang-2024-b.md) — §2.3, Eqs. (17)–(19); §5.
- [Mukha et al. (2025)](/sources/mukha-2025.md) — arXiv v1: §I; §II.A, Eq. (4); §III.B.3; §III.C, Fig. 8.
- [Ranjbar et al. (2026)](/sources/ranjbar-2026.md) — arXiv v1: §I; §II.B.
- [Caban et al. (2026)](/sources/caban-2026.md) — §1.
- [Yan et al. (2024)](/sources/yan-2024.md) — App. A1, B1, Eqs. (A3), (B1)–(B8) (compact second derivative, SVV kernel, closed-form coefficients); App. B2; §III A, Table II, Fig. 5 (iSVV against second-order Smagorinsky, cost, spectra); §III (values of $\nu_0/\nu$).
- [Tonicello et al. (2023)](/sources/tonicello-2023.md) — §1 (semi-discrete spatial eigenanalyses of Moura et al. and Mengaldo et al., extended to fully discrete; passing).
- [Lv & Ekaterinaris (2023)](/sources/lv-2023.md) — §4.2 (entropy-stable SVV of Mateo-Gabín et al. cited as a filtered form of artificial viscosity for LES; passing).
- [Alberti et al. (2025b)](/sources/alberti-2025-c.md) — §II A 1, Eqs. (23)–(25) (entropy correction on all non-mean modes contrasted with SVV); App. A, Table VI.
- [Rajek & Pozorski (2026)](/sources/rajek-2026.md) — §IV, Eqs. (18)–(36); §V (spectral eddy viscosity vanishing at low wavenumbers, aligned with the SVV literature).
