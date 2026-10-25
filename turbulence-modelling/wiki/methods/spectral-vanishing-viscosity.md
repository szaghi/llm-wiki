---
type: Method
title: "Spectral vanishing viscosity"
description: "Spectral vanishing viscosity concentrates an added viscosity on the highest resolved scales. The sources use two forms: an implicit one that boosts the modified wavenumber of the viscous scheme near the cutoff, and an explicit modal filter on a DG artificial-viscosity flux made entropy stable; both serve as LES models, the second also for shock capturing."
status: established
aliases: [SVV, implicit SVV, ISVV, implicit spectral vanishing viscosity, spectral viscosity, SVV-LES, entropy-stable SVV, modal SVV filter]
tags: [les, implicit-les, numerical-dissipation, sgs-model, dg, entropy-stable]
timestamp: 2026-10-25T19:46:00Z
---

# Spectral vanishing viscosity

**Spectral vanishing viscosity (SVV)** adds a viscosity that is small or
zero at large scales and acts mainly near the resolution limit. It goes
back to Tadmor's analysis of the Burgers equation, as recalled by
[Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md) (§4). The sources
use it in two different constructions:

- **implicit SVV** ([Vicente Cruz & Lamballais 2023](/sources/vicentecruz-2023.md)):
  no term is added; the viscous-term finite-difference scheme is tuned so
  that its modified wavenumber over-dissipates near the mesh cutoff $k_c$;
- **explicit modal SVV** (Mateo-Gabín et al. 2022): an artificial viscous
  flux is added to a discontinuous Galerkin spectral element scheme and
  weighted, mode by mode in the Legendre basis of each element, by a filter
  kernel that grows with the mode index.

Both act as an [implicit](/definitions/implicit-les.md) or mixed LES
closure; the explicit form is also used for shock capturing. The kernel,
the parameters and the evidence differ, so the two are kept apart below.

## Classical form

As recalled by Mateo-Gabín et al. (2022, §4, Eqs. 65–67), Tadmor's SVV for
the Burgers equation is

$$\partial_tu+\tfrac12\partial_x(u^2)=\epsilon_N\,\partial_x\big[\mathcal F\star\partial_xu\big],\qquad \epsilon_N\sim\frac1{N^\beta\log N},\ \beta<1,$$

with $\mathcal F\star$ a spectral filter whose coefficients $\varphi_k$
(page-local) vanish below a cutoff mode $M$ (page-local). Two kernels are
recalled: the step $\varphi_k=0$ for $k\le M$, 1 for $k>M$; and the smooth
kernel of Maday et al. and Kaber, $\varphi_k=\exp[-(k-N)^2/(k-M)^2]$ for
$k>M$, with $M\approx5\sqrt N$. The authors recall SVV for under-resolved
turbulence (Karamanos & Karniadakis; Kirby & Sherwin) and its combination
with LES (SVV-LES; Kirby & Karniadakis; Pasquetti et al.).

## Implicit SVV (finite differences)

In the form used by Vicente Cruz & Lamballais (2023, §5.1), after Lamballais
et al. and Dairay et al. (as recalled), no term is added to the equations.
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

Following Dairay et al. (as recalled), $\nu_0$ is set by a Pao-like spectral
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
  converged at standard resolution, unlike [Smagorinsky](/methods/smagorinsky-model.md);
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
approach in the paper's introduction.

## Related constructions

- [Flad & Gassner (2017)](/sources/flad-2017.md) (App. C) build a modal
  cusp eddy viscosity in DG polynomial space, acting through a high-pass
  filter on the gradients: like SVV it is concentrated at the highest
  resolved modes.
- [Beck & Kurz (2023)](/sources/beck-2023.md) (§III B) relate their
  element-wise quadratic Smagorinsky coefficient (RL-Quad) to spectral
  vanishing viscosity, but defined in physical rather than wavenumber
  space.

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
- The SVV values for the two Taylor–Green resolutions are given in §5.3 and
  not restated in §6.
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
